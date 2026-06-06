"""
Simpan & muat case via cloud — **tanpa Google Drive** (service account personal
tidak punya kuota Drive). Payload (ZIP) disimpan sebagai base64 yang dipecah ke
beberapa kolom dalam SATU baris di sheet `saved_cases_data` (kunci `case_id`),
dengan indeks ringkas di sheet `saved_cases`. Melengkapi save/load ZIP manual.

Alur:
- Save : `build_case_archive_bytes()` → base64 → tulis chunk ke `saved_cases_data`
         (upsert per baris case_id) → upsert indeks ke `saved_cases`.
- List : baca `saved_cases`, urut `saved_at` desc.
- Load : baca chunk `saved_cases_data` by `case_id` → rakit base64 → bytes →
         `restore_case_archive()`.

`case_id = sha1(line_name|fault_time_cfg)` — re-save event sama menimpa baris yang sama.
"""

import base64
from datetime import datetime

import streamlit as st

from case_storage import build_case_archive_bytes, restore_case_archive
from fault_cause_dataset import (
    _build_sheets_service,
    _col_letter,
    _extract_spreadsheet_id,
    make_case_id,
    read_sheet_records,
    upsert_row_to_gsheet,
)
from fault_workflow_helpers import parse_comtrade_timestamp
from line_analysis_helpers import infer_gi_names_from_line_name

SAVED_CASES_SHEET = "saved_cases"
SAVED_CASES_DATA_SHEET = "saved_cases_data"
# Aman di bawah batas 50.000 karakter per sel
_CHUNK_SIZE = 49000

SAVED_CASES_COLUMNS = [
    "case_id", "case_name", "line_name", "gi_local", "gi_remote",
    "fault_time_cfg", "saved_at", "filename", "size_bytes", "n_chunks",
]


def _ensure_sheet(ss, sid, name, cols: int = 0):
    """Pastikan sheet ada. `cols`>0 → set jumlah kolom grid (untuk payload lebar)."""
    titles = [s["properties"]["title"] for s in ss.get(spreadsheetId=sid).execute().get("sheets", [])]
    if name not in titles:
        props = {"title": name}
        if cols > 0:
            props["gridProperties"] = {"columnCount": cols}
        ss.batchUpdate(
            spreadsheetId=sid,
            body={"requests": [{"addSheet": {"properties": props}}]},
        ).execute()


def _write_payload_chunks(ss, sid, case_id: str, b64: str, sheet_name: str = SAVED_CASES_DATA_SHEET) -> int:
    """Tulis [case_id, chunk0, chunk1, ...] sebagai satu baris (upsert by case_id).

    Pakai valueInputOption RAW agar base64 tak diinterpretasi sebagai formula.
    Bila update & baris baru lebih sempit dari lama → sel sisa dikosongkan.
    """
    # 200 kolom ≈ payload s.d. ~10 MB (49000 char/chunk) — cukup luas untuk case tipikal
    _ensure_sheet(ss, sid, sheet_name, cols=200)
    chunks = [b64[i:i + _CHUNK_SIZE] for i in range(0, len(b64), _CHUNK_SIZE)] or [""]
    new_row = [case_id] + chunks

    col_a = ss.values().get(spreadsheetId=sid, range=f"{sheet_name}!A:A").execute().get("values", [])
    match = None
    for i, r in enumerate(col_a):
        if r and str(r[0]).strip() == case_id:
            match = i + 1
            break

    if match:
        old = ss.values().get(spreadsheetId=sid, range=f"{sheet_name}!{match}:{match}").execute().get("values", [[]])
        old_width = len(old[0]) if old and old[0] else 0
        width = max(old_width, len(new_row))
        padded = new_row + [""] * (width - len(new_row))
        ss.values().update(
            spreadsheetId=sid,
            range=f"{sheet_name}!A{match}:{_col_letter(width)}{match}",
            valueInputOption="RAW", body={"values": [padded]},
        ).execute()
    else:
        ss.values().append(
            spreadsheetId=sid, range=f"{sheet_name}!A1",
            valueInputOption="RAW", insertDataOption="INSERT_ROWS", body={"values": [new_row]},
        ).execute()
    return len(chunks)


def _read_payload_chunks(ss, sid, case_id: str, sheet_name: str = SAVED_CASES_DATA_SHEET) -> str:
    data = ss.values().get(spreadsheetId=sid, range=f"{sheet_name}").execute().get("values", [])
    for r in data:
        if r and str(r[0]).strip() == case_id:
            return "".join(str(c) for c in r[1:] if c)
    return ""


def save_case_to_cloud(spreadsheet_url: str, case_name: str = "", sheet_name: str = SAVED_CASES_SHEET):
    """Build ZIP → base64 chunked ke `saved_cases_data` → upsert indeks. Return (ok, message)."""
    if "line_param" not in st.session_state:
        return False, "Belum ada data case untuk disimpan (lakukan analisis dulu)."
    sid = _extract_spreadsheet_id(spreadsheet_url)
    if not sid:
        return False, "URL Database Spreadsheet tidak valid."

    line_name = str((st.session_state.get("line_param") or {}).get("line_name") or "")
    meta = st.session_state.get("local_metadata") or {}
    _ft_raw = meta.get("cfg_trigger_time") or meta.get("cfg_start_time") or ""
    _ft_dt = parse_comtrade_timestamp(str(_ft_raw))
    fault_time = _ft_dt.isoformat(timespec="seconds") if _ft_dt else str(_ft_raw)
    cid = make_case_id(line_name, fault_time)
    if not cid:
        return False, "Tidak dapat membuat case_id (line_name & waktu kejadian kosong)."

    gi_local = st.session_state.get("two_ended_local_gi_label")
    gi_remote = st.session_state.get("two_ended_remote_gi_label")
    if not gi_local or not gi_remote:
        _l, _r = infer_gi_names_from_line_name(line_name)
        gi_local = gi_local or _l
        gi_remote = gi_remote or _r

    try:
        filename, archive_bytes = build_case_archive_bytes(case_name)
        b64 = base64.b64encode(archive_bytes).decode("ascii")
        ss = _build_sheets_service().spreadsheets()
        n_chunks = _write_payload_chunks(ss, sid, cid, b64)
    except Exception as exc:
        return False, f"Gagal menyimpan payload case ke spreadsheet: {exc}"

    row = {
        "case_id": cid,
        "case_name": (case_name or line_name or filename).strip(),
        "line_name": line_name,
        "gi_local": gi_local or "",
        "gi_remote": gi_remote or "",
        "fault_time_cfg": fault_time,
        "saved_at": datetime.now().isoformat(timespec="seconds"),
        "filename": filename,
        "size_bytes": len(archive_bytes),
        "n_chunks": n_chunks,
    }
    ok, msg, action = upsert_row_to_gsheet(spreadsheet_url, row, SAVED_CASES_COLUMNS, sheet_name)
    if not ok:
        return False, msg
    verb = "diperbarui" if action == "update" else "disimpan"
    return True, f"Case '{row['case_name']}' {verb} ke spreadsheet ({n_chunks} chunk, {len(archive_bytes):,} byte)."


def list_saved_cases(spreadsheet_url: str, sheet_name: str = SAVED_CASES_SHEET) -> list:
    """Daftar case tersimpan, urut `saved_at` terbaru dulu."""
    recs = read_sheet_records(spreadsheet_url, sheet_name)
    recs = [r for r in recs if str(r.get("case_id", "")).strip()]
    recs.sort(key=lambda r: str(r.get("saved_at", "")), reverse=True)
    return recs


def load_case_from_cloud(spreadsheet_url: str, case_id: str):
    """Baca chunk by case_id → rakit → restore. Return (ok, message)."""
    sid = _extract_spreadsheet_id(spreadsheet_url)
    if not sid or not case_id:
        return False, "URL spreadsheet atau case_id tidak valid."
    try:
        ss = _build_sheets_service().spreadsheets()
        b64 = _read_payload_chunks(ss, sid, str(case_id).strip())
    except Exception as exc:
        return False, f"Gagal membaca payload case dari spreadsheet: {exc}"
    if not b64:
        return False, "Payload case tidak ditemukan di sheet `saved_cases_data`."
    try:
        archive_bytes = base64.b64decode(b64)
        restore_case_archive(archive_bytes)
    except Exception as exc:
        return False, f"Gagal memulihkan case: {exc}"
    return True, "Case berhasil dimuat dari spreadsheet."
