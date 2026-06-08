"""
Pengumpulan dataset berlabel untuk penentuan PENYEBAB gangguan (jembatan rule → ML).

Setiap kasus yang dianalisis menghasilkan satu baris feature-vector (fitur yang
sama dipakai `estimate_summary_disturbance_cause`) + label penyebab terkonfirmasi
(diisi user setelah inspeksi lapangan). Baris di-append ke Google Sheet
`fault_cause_dataset` agar dataset tumbuh untuk pelatihan ML kemudian.

Storage: Google Sheet (Sheets API v4) via service account — reuse pola
`case_storage`. Fallback: CSV download di UI bila kredensial tulis tak tersedia.
"""

import hashlib
import re

import streamlit as st

# Label penyebab terkonfirmasi (target ML). "Belum diketahui" = belum diinspeksi.
CONFIRMED_CAUSE_LABELS = [
    "Sambaran Petir",
    "Vegetasi / Pohon",
    "Satwa Liar",
    "Flashover Polusi / Isolator",
    "Kebakaran di Bawah Saluran",
    "Benda Asing / Layangan",
    "Gangguan Permanen (Peralatan)",
    "Lainnya",
    "Belum Diketahui",
]

DATASET_SHEET_NAME = "fault_cause"

# Urutan kolom dataset (header). Konsisten = wajib agar append rapi.
# `case_id` (kolom A) = kunci unik untuk upsert (update baris yang cocok, bukan duplikat).
DATASET_COLUMNS = [
    "case_id",
    "timestamp_analyzed", "fault_time_cfg", "line_name", "gi_local", "gi_remote",
    "upt", "ultg",
    "fault_type", "n_phases", "ground", "ft_confidence",
    "I0_A", "I1_A", "I2_A", "r_i2_i1", "r_i0_i1", "r_i0_i2",
    "ang_i2_i1_deg", "ang_i0_i1_deg", "r_v2_v1", "r_v0_v1",
    "Z1_ohm", "Z2_ohm", "Z0_ohm",
    "rf_est_ohm", "hr_suspected",
    "hour", "month",
    "weather_code", "weather_desc", "rain_mm", "humidity_pct",
    "di_dt_norm", "hf_ratio", "transient_sharp", "duration_ms",
    "cleared_in_record", "reclose_in_record",
    "se_distance_km", "de_distance_km", "de_quality",
    "predicted_cause", "predicted_score",
    "confirmed_cause",
    "upt_local", "ultg_local", "upt_remote", "ultg_remote", "segment",
]


def make_case_id(line_name: str, fault_time_cfg) -> str:
    """ID unik & deterministik untuk satu event gangguan = hash(line_name|fault_time).

    Re-analisis rekaman yang sama (line + waktu kejadian sama) → case_id sama →
    baris di-update, bukan duplikat. Kosong bila kedua identitas tak tersedia.
    """
    ln = str(line_name or "").strip()
    ft = str(fault_time_cfg or "").strip()
    if not ln and not ft:
        return ""
    return hashlib.sha1(f"{ln}|{ft}".encode("utf-8")).hexdigest()[:16]


def _f(d, key, default=0.0):
    try:
        return float((d or {}).get(key, default) or default)
    except (TypeError, ValueError):
        return default


def _mag(phasors, key):
    return float((phasors or {}).get(key, {}).get("magnitude") or 0.0)


def _ang(phasors, key):
    return float((phasors or {}).get(key, {}).get("angle_deg") or 0.0)


def _cplx(phasors, key):
    return (phasors or {}).get(key, {}).get("complex")


def _wrap(d):
    return ((d + 180.0) % 360.0) - 180.0


def build_fault_cause_feature_row(
    *,
    timestamp_analyzed: str,
    fault_time_cfg,
    line_name: str,
    gi_local: str,
    gi_remote: str,
    upt: str,
    ultg: str,
    upt_local: str,
    ultg_local: str,
    upt_remote: str,
    ultg_remote: str,
    segment: str,
    fault_type_result: dict,
    high_resistance_result: dict,
    phasors: dict,
    fault_hour,
    fault_month,
    weather_context: dict,
    waveform_signatures: dict,
    single_result: dict,
    two_result: dict,
    two_quality: dict,
    predicted_cause: str,
    predicted_score,
    confirmed_cause: str,
) -> dict:
    """Rakit satu baris feature-vector dataset (flat dict sesuai DATASET_COLUMNS)."""
    ft = fault_type_result or {}
    fault_type = str(ft.get("fault_type", "")).upper()
    n_phases = sum(1 for c in fault_type if c in "ABC")
    ground = "G" in fault_type

    i0, i1, i2 = _mag(phasors, "I0"), _mag(phasors, "I1"), _mag(phasors, "I2")
    v0, v1, v2 = _mag(phasors, "V0"), _mag(phasors, "V1"), _mag(phasors, "V2")

    def _ratio(a, b):
        return round(a / b, 4) if b > 1e-6 else 0.0

    def _zmag(vn, in_):
        vc, ic = _cplx(phasors, vn), _cplx(phasors, in_)
        return round(abs(vc / ic), 3) if (vc is not None and ic is not None and abs(ic) > 1e-6) else 0.0

    wx = weather_context or {}
    wf = waveform_signatures or {}

    row = {
        "case_id": make_case_id(line_name, fault_time_cfg),
        "timestamp_analyzed": timestamp_analyzed,
        "fault_time_cfg": str(fault_time_cfg or ""),
        "line_name": line_name or "",
        "gi_local": gi_local or "",
        "gi_remote": gi_remote or "",
        "upt": upt or "",
        "ultg": ultg or "",
        "upt_local": upt_local or upt or "",
        "ultg_local": ultg_local or ultg or "",
        "upt_remote": upt_remote or "",
        "ultg_remote": ultg_remote or "",
        "segment": segment or "",
        "fault_type": fault_type,
        "n_phases": n_phases,
        "ground": int(bool(ground)),
        "ft_confidence": round(_f(ft, "confidence"), 2),
        "I0_A": round(i0, 2), "I1_A": round(i1, 2), "I2_A": round(i2, 2),
        "r_i2_i1": _ratio(i2, i1), "r_i0_i1": _ratio(i0, i1), "r_i0_i2": _ratio(i0, i2),
        "ang_i2_i1_deg": round(_wrap(_ang(phasors, "I2") - _ang(phasors, "I1")), 1) if (i1 > 1e-6 and i2 > 1e-6) else "",
        "ang_i0_i1_deg": round(_wrap(_ang(phasors, "I0") - _ang(phasors, "I1")), 1) if (i1 > 1e-6 and i0 > 1e-6) else "",
        "r_v2_v1": _ratio(v2, v1), "r_v0_v1": _ratio(v0, v1),
        "Z1_ohm": _zmag("V1", "I1"), "Z2_ohm": _zmag("V2", "I2"), "Z0_ohm": _zmag("V0", "I0"),
        "rf_est_ohm": round(_f(high_resistance_result, "Rf_est_ohm"), 2),
        "hr_suspected": int(bool((high_resistance_result or {}).get("high_resistance_suspected"))),
        "hour": fault_hour if fault_hour is not None else "",
        "month": fault_month if fault_month is not None else "",
        "weather_code": wx.get("code", ""),
        "weather_desc": str(wx.get("desc") or ""),
        "rain_mm": wx.get("rain_mm", ""),
        "humidity_pct": wx.get("humidity", ""),
        "di_dt_norm": wf.get("di_dt_norm", ""),
        "hf_ratio": wf.get("hf_ratio", ""),
        "transient_sharp": int(bool(wf.get("transient_sharp"))) if "transient_sharp" in wf else "",
        "duration_ms": wf.get("duration_ms", ""),
        "cleared_in_record": ("" if wf.get("cleared_in_record") is None else int(bool(wf.get("cleared_in_record")))),
        "reclose_in_record": int(bool(wf.get("reclose_in_record"))) if "reclose_in_record" in wf else "",
        "se_distance_km": round(_f(single_result, "recommended_distance_km"), 3) if single_result else "",
        "de_distance_km": round(_f(two_result, "distance_from_original_local_km") or _f(two_result, "distance_km"), 3) if two_result else "",
        "de_quality": round(_f(two_quality, "quality_score"), 1) if two_quality else "",
        "predicted_cause": predicted_cause or "",
        "predicted_score": predicted_score if predicted_score is not None else "",
        "confirmed_cause": confirmed_cause or "",
    }
    return row


def _extract_spreadsheet_id(url: str):
    m = re.search(r"/spreadsheets/d/([A-Za-z0-9_-]+)", str(url or ""))
    return m.group(1) if m else None


def _build_sheets_service():
    from google.oauth2 import service_account
    from googleapiclient.discovery import build

    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    info = None
    try:
        info = st.session_state.get("runtime_gdrive_service_account") or st.secrets.get("gdrive_service_account")
    except Exception:
        info = st.session_state.get("runtime_gdrive_service_account")
    if not info:
        raise RuntimeError(
            "Kredensial Google service account belum tersedia. Upload credentials dengan "
            "google_service_account, lalu share spreadsheet ke email service account (akses Editor)."
        )
    credentials = service_account.Credentials.from_service_account_info(dict(info), scopes=scopes)
    return build("sheets", "v4", credentials=credentials, cache_discovery=False)


def _col_letter(n: int) -> str:
    """Indeks kolom (1-based) → huruf A1 (mis. 43 → AQ)."""
    s = ""
    while n > 0:
        n, r = divmod(n - 1, 26)
        s = chr(65 + r) + s
    return s


def upsert_row_to_gsheet(spreadsheet_url: str, row: dict, columns: list, sheet_name: str):
    """Upsert generik satu baris ke sheet berdasarkan nilai kolom pertama (`columns[0]`).

    Bila nilai kunci (kolom A) cocok dengan baris yang ada → di-UPDATE; bila tidak →
    di-APPEND. Buat sheet bila belum ada; header auto-migrasi bila berbeda dari `columns`.
    Kunci kosong → selalu append. Return (ok: bool, message: str, action: str|None).
    """
    sid = _extract_spreadsheet_id(spreadsheet_url)
    if not sid:
        return False, "URL spreadsheet tidak valid.", None
    try:
        ss = _build_sheets_service().spreadsheets()
        titles = [s["properties"]["title"] for s in ss.get(spreadsheetId=sid).execute().get("sheets", [])]
        if sheet_name not in titles:
            ss.batchUpdate(
                spreadsheetId=sid,
                body={"requests": [{"addSheet": {"properties": {"title": sheet_name}}}]},
            ).execute()

        header = ss.values().get(spreadsheetId=sid, range=f"{sheet_name}!1:1").execute().get("values", [])
        if (header[0] if header else []) != columns:
            ss.values().update(
                spreadsheetId=sid, range=f"{sheet_name}!A1",
                valueInputOption="USER_ENTERED", body={"values": [columns]},
            ).execute()

        values = [[("" if row.get(c) is None else row.get(c)) for c in columns]]
        last_col = _col_letter(len(columns))
        key_val = str(row.get(columns[0]) or "").strip()

        match_row = None
        if key_val:
            col_a = ss.values().get(spreadsheetId=sid, range=f"{sheet_name}!A:A").execute().get("values", [])
            for i, r in enumerate(col_a):
                if i > 0 and r and str(r[0]).strip() == key_val:
                    match_row = i + 1
                    break

        if match_row:
            ss.values().update(
                spreadsheetId=sid, range=f"{sheet_name}!A{match_row}:{last_col}{match_row}",
                valueInputOption="RAW", body={"values": values},
            ).execute()
            return True, f"Baris DIPERBARUI (baris {match_row}) di sheet '{sheet_name}'.", "update"
        ss.values().append(
            spreadsheetId=sid, range=f"{sheet_name}!A1",
            valueInputOption="RAW", insertDataOption="INSERT_ROWS", body={"values": values},
        ).execute()
        return True, f"Baris baru ditambahkan ke sheet '{sheet_name}'.", "append"
    except Exception as exc:
        return False, f"Gagal menulis ke Google Sheet: {exc}", None


def read_sheet_records(spreadsheet_url: str, sheet_name: str) -> list:
    """Baca sheet → list of dict (header baris 1 sebagai kunci). Kosong bila gagal/kosong."""
    sid = _extract_spreadsheet_id(spreadsheet_url)
    if not sid:
        return []
    try:
        ss = _build_sheets_service().spreadsheets()
        data = ss.values().get(spreadsheetId=sid, range=f"{sheet_name}").execute().get("values", [])
        if len(data) < 2:
            return []
        header = data[0]
        records = []
        for r in data[1:]:
            r = list(r) + [""] * (len(header) - len(r))
            records.append({header[i]: r[i] for i in range(len(header))})
        return records
    except Exception:
        return []


def append_feature_row_to_gsheet(spreadsheet_url: str, row: dict, sheet_name: str = DATASET_SHEET_NAME):
    """Upsert baris dataset penyebab (kunci `case_id`). Return (ok, message)."""
    ok, msg, _ = upsert_row_to_gsheet(spreadsheet_url, row, DATASET_COLUMNS, sheet_name)
    return ok, msg
