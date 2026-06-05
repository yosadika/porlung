import html as _html

import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from plotly.subplots import make_subplots

from app_helpers import downsample_xy
from line_analysis_helpers import build_remote_single_signed_position
from waveform_helpers import fault_phase_to_current_channel, fault_phase_to_voltage_channel


def build_cause_table_html(rows: list, col_specs: list) -> str:
    """Bangun tabel HTML print-friendly dengan lebar kolom presisi + teks membungkus.

    ``rows``: list of dict. ``col_specs``: list of dict
    `{key, header, width, align}` (width mis. "22%", align "left"/"center").
    """
    is_dark = st.get_option("theme.base") == "dark"
    border = "#334155" if is_dark else "#e2e8f0"
    head_bg = "#1e293b" if is_dark else "#f1f5f9"
    txt = "#e2e8f0" if is_dark else "#0f172a"

    css = (
        "<style>"
        "table.porlung-cause{border-collapse:collapse;width:100%;font-size:0.85rem;"
        f"color:{txt};table-layout:fixed;}}"
        f"table.porlung-cause th,table.porlung-cause td{{border:1px solid {border};"
        "padding:6px 10px;text-align:left;vertical-align:top;word-break:break-word;"
        "overflow-wrap:anywhere;}"
        f"table.porlung-cause th{{background:{head_bg};font-weight:600;}}"
        "table.porlung-cause td.center,table.porlung-cause th.center{text-align:center;}"
        "</style>"
    )
    cols_html = "".join(
        f'<col style="width:{c.get("width","auto")}">' for c in col_specs
    )
    head = "".join(
        f'<th{" class=\"center\"" if c.get("align") == "center" else ""}>'
        f"{_html.escape(str(c['header']))}</th>"
        for c in col_specs
    )
    body = ""
    for r in rows:
        cells = ""
        for c in col_specs:
            cls = ' class="center"' if c.get("align") == "center" else ""
            cells += f"<td{cls}>{_html.escape(str(r.get(c['key'], '')))}</td>"
        body += f"<tr>{cells}</tr>"
    return (
        css
        + f'<table class="porlung-cause"><colgroup>{cols_html}</colgroup>'
        + f"<thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>"
    )


def choose_summary_fault_signals(local_fault_type_result, remote_fault_type_result):
    fault_type = (
        (local_fault_type_result or {}).get("fault_type")
        or (remote_fault_type_result or {}).get("fault_type")
        or ""
    )

    voltage_channel = fault_phase_to_voltage_channel(fault_type) or "Va"
    current_channel = fault_phase_to_current_channel(fault_type) or "Ia"

    return fault_type, voltage_channel, current_channel


def build_summary_focus_waveform(
    local_df,
    remote_df,
    local_fault_window,
    remote_fault_window,
    channel,
    title,
    seconds_before=0.08,
    seconds_after=0.12,
    remote_time_shift_s=0.0,
):
    fig = go.Figure()

    if local_df is not None and local_fault_window is not None and channel in local_df.columns:
        local_time = local_df["time"] - local_fault_window["fault_time"]
        local_mask = (local_time >= -seconds_before) & (local_time <= seconds_after)
        local_x, local_y = downsample_xy(local_time[local_mask], local_df.loc[local_mask, channel])
        fig.add_trace(
            go.Scatter(
                x=local_x,
                y=local_y,
                mode="lines",
                name=f"Local {channel}",
                line=dict(width=1.4),
            )
        )

    if remote_df is not None and remote_fault_window is not None and channel in remote_df.columns:
        remote_time = remote_df["time"] - remote_fault_window["fault_time"] + remote_time_shift_s
        remote_mask = (remote_time >= -seconds_before) & (remote_time <= seconds_after)
        remote_x, remote_y = downsample_xy(remote_time[remote_mask], remote_df.loc[remote_mask, channel])
        fig.add_trace(
            go.Scatter(
                x=remote_x,
                y=remote_y,
                mode="lines",
                name=f"Remote {channel}",
                line=dict(width=1.4, dash="dash"),
            )
        )

    fig.add_vline(
        x=0.0,
        line_dash="solid",
        annotation_text="Fault",
        annotation_position="top",
    )

    fig.update_layout(
        title=title,
        xaxis_title="Aligned Time from Fault (s)",
        yaxis_title="Instantaneous Primary Magnitude",
        legend_title="Signal",
        xaxis=dict(range=[-seconds_before, seconds_after], autorange=False),
    )

    return fig


_DISTURBANCE_CAUSE_REFERENCES = (
    "Minnaar (2014) *The Characterisation and Automatic Classification of Transmission Line Faults* "
    "(tesis, Univ. Cape Town) — fitur diskriminatif: hour-of-day (peringkat #1), bulan/musim, fault type, "
    "Rf, dan komponen sekuens (pos/neg/zero); "
    "SEL (2011) *Introduction to Symmetrical Components* — tanda sekuens per tipe gangguan "
    "(3-fasa: hanya positif; LL: positif+negatif tanpa zero; SLG: I0≈I1≈I2); "
    "*Transmission Line Fault-Cause Identification* (Appl. Sci. 11, 7804); "
    "*A Review and Taxonomy on Fault Analysis in Transmission Lines* (Computation 10, 144); "
    "IEEE Std C37.114-2014 Sec. 3.1; Saha et al. (2010) Ch. 2."
)


def estimate_summary_disturbance_cause(
    fault_type_result,
    high_resistance_result,
    phasors=None,
    prefault_phasors=None,
    single_result=None,
    two_result=None,
    two_quality=None,
    line_param=None,
    fault_hour=None,
    fault_month=None,
    weather_context=None,
    waveform_signatures=None,
):
    """Estimasi penyebab gangguan via candidate-scoring berbasis literatur.

    Mengembalikan ``(label, detail)``. ``detail`` berisi: ``basis`` (tabel fakta
    terukur), ``candidates`` (daftar kandidat ter-ranking + skor + bukti),
    ``explanation``, ``note``, ``references``.

    Fitur diskriminatif: fault type & ground involvement, komponen simetris,
    fault resistance (Rf), **hour-of-day** (puncak diurnal bird streamer ~06:00 &
    ~22:00), **bulan/musim** (kemarau Indonesia → kebakaran lahan), **cuaca**
    lokasi (badai petir/hujan/kabut → petir/polusi), dan **tanda waveform**
    (transien/HF, durasi, reclose). Konteks Indonesia/tropis.

    ``weather_context``: dict `{code,desc,rain_mm,humidity}` cuaca SAAT INI di
    lokasi (OpenWeather) — hanya valid untuk gangguan baru, beri caveat.
    ``waveform_signatures``: dict dari `waveform_signatures.py` (hf_ratio,
    di_dt_norm, duration_ms, cleared_in_record, transient_label, dst).
    """
    fault_type   = str((fault_type_result or {}).get("fault_type", "")).upper()
    hr_suspected = bool((high_resistance_result or {}).get("high_resistance_suspected"))
    rf_est       = float((high_resistance_result or {}).get("Rf_est_ohm") or 0.0)
    ft_conf      = float((fault_type_result or {}).get("confidence", 0.0))
    n_phases     = sum(1 for c in fault_type if c in "ABC")
    ground       = "G" in fault_type
    low_rf       = (not hr_suspected) and (rf_est < 8.0)
    try:
        hour = int(fault_hour) if fault_hour is not None else None
    except (TypeError, ValueError):
        hour = None
    bird_window = hour is not None and (hour in (5, 6, 7) or hour in (21, 22, 23, 0))

    # ── Konteks musim (Indonesia tropis: kemarau ~Mei–Okt, hujan ~Nov–Apr) ──
    try:
        month = int(fault_month) if fault_month is not None else None
    except (TypeError, ValueError):
        month = None
    dry_season = month in (5, 6, 7, 8, 9, 10) if month is not None else False
    wet_season = month in (11, 12, 1, 2, 3, 4) if month is not None else False

    # ── Konteks cuaca SAAT INI di lokasi (caveat: bukan saat kejadian) ──
    wx = weather_context or {}
    wx_code = wx.get("code")
    wx_rain = float(wx.get("rain_mm") or 0.0)
    wx_hum  = float(wx.get("humidity") or 0.0)
    wx_thunder = isinstance(wx_code, (int, float)) and 200 <= wx_code < 300
    wx_wet     = (wx_rain > 0) or (isinstance(wx_code, (int, float)) and (300 <= wx_code < 600 or 700 <= wx_code < 800)) or (wx_hum >= 90)
    wx_dryclear = isinstance(wx_code, (int, float)) and wx_code == 800 and wx_hum and wx_hum < 60

    # ── Tanda waveform (dari waveform_signatures.py) ──
    wf = waveform_signatures or {}
    wf_transient_sharp = bool(wf.get("transient_sharp"))   # HF/di-dt tinggi → impulsif
    wf_cleared = wf.get("cleared_in_record")               # True=clear (temporer), False=bertahan
    wf_duration_ms = wf.get("duration_ms")

    def _mag(d, key):
        return float((d or {}).get(key, {}).get("magnitude") or 0.0)

    def _row(p, v):
        return {"Parameter": p, "Nilai": v}

    # ── Tabel fakta terukur (basis) ──────────────────────────────────
    basis = []
    if fault_type:
        _gt = "ke tanah" if ground else "fase-fase"
        basis.append(_row("Fault Type", f"{fault_type} — {n_phases} fasa terganggu, {_gt}"))
    if ft_conf > 0:
        basis.append(_row("Keyakinan Klasifikasi", f"{ft_conf:.1f} / 10"))
    if hr_suspected:
        basis.append(_row("Resistansi Gangguan (Rf)", f"{rf_est:.1f} Ω — tinggi (indikasi high-resistance)"))
    elif rf_est > 0:
        basis.append(_row("Resistansi Gangguan (Rf)", f"≈ {rf_est:.1f} Ω — rendah/normal"))
    if hour is not None:
        basis.append(_row("Jam Kejadian (CFG)", f"{hour:02d}:xx"))
    # Arus/tegangan fasa terganggu vs pre-fault
    for ph in (fault_type_result or {}).get("faulted_phases", [])[:2]:
        if ph not in "ABC":
            continue
        i_f, i_p = _mag(phasors, f"I{ph.lower()}"), _mag(prefault_phasors, f"I{ph.lower()}")
        if i_f > 0:
            s = f"{i_f:,.1f} A (fault)"
            if i_p > 0:
                s += f"  ←  {i_p:,.1f} A (pre-fault),  naik +{(i_f / i_p * 100 - 100):.0f}%"
            basis.append(_row(f"Arus Fasa {ph}", s))
    ie_f, ie_p = _mag(phasors, "IE"), _mag(prefault_phasors, "IE")
    if ie_f > 0:
        s = f"{ie_f:,.1f} A (fault)"
        if ie_p > 0:
            s += f"  ←  {ie_p:,.1f} A (pre-fault)"
        basis.append(_row("Arus Netral IE", s))

    # ── Komponen simetris (SEL, Intro to Symmetrical Components) ──────
    # 3-fasa  → hanya positif (I2≈I0≈0); LL → positif+negatif tanpa zero (I0≈0);
    # SLG    → I0≈I1≈I2; zero-sequence hanya muncul pada gangguan ke tanah.
    i1_m, i2_m, i0_m = _mag(phasors, "I1"), _mag(phasors, "I2"), _mag(phasors, "I0")
    v2_m, v0_m = _mag(phasors, "V2"), _mag(phasors, "V0")
    r_i2_i1 = (i2_m / i1_m) if i1_m > 1e-6 else 0.0   # derajat asimetri
    r_i0_i1 = (i0_m / i1_m) if i1_m > 1e-6 else 0.0   # keterlibatan tanah
    r_i0_i2 = (i0_m / i2_m) if i2_m > 1e-6 else 0.0   # kemurnian SLG (≈1)

    # Flag untuk scoring (ambang konservatif)
    clean_slg_seq = (r_i0_i1 >= 0.5) and (0.6 <= r_i0_i2 <= 1.5)   # I0≈I1≈I2
    balanced_seq  = (r_i2_i1 < 0.10) and (r_i0_i1 < 0.10)          # nyaris hanya positif

    if i1_m > 0:
        basis.append(_row(
            "Negatif/Positif (I2/I1)",
            f"{r_i2_i1:.2f} — " + ("asimetri kuat (tak seimbang)" if r_i2_i1 >= 0.3 else "rendah (mendekati seimbang)"),
        ))
        basis.append(_row(
            "Zero/Positif (I0/I1)",
            f"{r_i0_i1:.2f} — " + ("keterlibatan tanah kuat" if r_i0_i1 >= 0.3 else "keterlibatan tanah lemah/tidak ada"),
        ))
        if i2_m > 1e-6 and ground:
            basis.append(_row(
                "Zero/Negatif (I0/I2)",
                f"{r_i0_i2:.2f} — " + ("≈1 → pola SLG murni (I0≈I1≈I2)" if 0.6 <= r_i0_i2 <= 1.5 else "menyimpang dari SLG murni"),
            ))
    # Rasio tegangan sekuens, sudut sekuens, impedansi sekuens (Z1/Z2/Z0)
    def _ang(key):
        return float((phasors or {}).get(key, {}).get("angle_deg") or 0.0)

    def _cplx(key):
        return (phasors or {}).get(key, {}).get("complex")

    v1_m = _mag(phasors, "V1")
    r_v2_v1 = (v2_m / v1_m) if v1_m > 1e-6 else 0.0
    r_v0_v1 = (v0_m / v1_m) if v1_m > 1e-6 else 0.0
    def _wrap(d):  # normalisasi beda sudut ke [-180, 180]
        return ((d + 180.0) % 360.0) - 180.0
    ang_i2_i1 = _wrap(_ang("I2") - _ang("I1")) if (i1_m > 1e-6 and i2_m > 1e-6) else None
    ang_i0_i1 = _wrap(_ang("I0") - _ang("I1")) if (i1_m > 1e-6 and i0_m > 1e-6) else None

    if v1_m > 0 and (v2_m > 0 or v0_m > 0):
        basis.append(_row(
            "Negatif/Positif Tegangan (V2/V1)",
            f"{r_v2_v1:.2f} — " + ("depresi tegangan asimetris kuat" if r_v2_v1 >= 0.15 else "rendah"),
        ))
        basis.append(_row("Zero/Positif Tegangan (V0/V1)", f"{r_v0_v1:.2f}"))
    if ang_i2_i1 is not None or ang_i0_i1 is not None:
        _parts = []
        if ang_i2_i1 is not None:
            _parts.append(f"∠I2−∠I1 = {ang_i2_i1:+.0f}°")
        if ang_i0_i1 is not None:
            _parts.append(f"∠I0−∠I1 = {ang_i0_i1:+.0f}°")
        basis.append(_row("Sudut Sekuens", ", ".join(_parts)))
    # Impedansi sekuens Z = V_seq / I_seq (magnitude, primary ohm)
    _zparts = []
    for _zn, _vn, _in_, _im in (("Z1", "V1", "I1", i1_m), ("Z2", "V2", "I2", i2_m), ("Z0", "V0", "I0", i0_m)):
        _vc, _ic = _cplx(_vn), _cplx(_in_)
        if _vc is not None and _ic is not None and _im > 1e-6:
            _zparts.append(f"|{_zn}| ≈ {abs(_vc / _ic):.1f} Ω")
    if _zparts:
        basis.append(_row("Impedansi Sekuens", ", ".join(_zparts)))

    # ── Konteks musim / cuaca / waveform ─────────────────────────────
    if month is not None:
        basis.append(_row("Bulan Kejadian", f"{month:02d} — " + ("musim kemarau" if dry_season else "musim hujan" if wet_season else "-")))
    if wx:
        _wxdesc = str(wx.get("desc") or "-")
        _wxextra = []
        if wx_thunder: _wxextra.append("badai petir")
        if wx_wet and not wx_thunder: _wxextra.append("basah/lembap")
        if wx_dryclear: _wxextra.append("cerah-kering")
        basis.append(_row("Cuaca Lokasi (saat ini)", f"{_wxdesc}" + (f" — {', '.join(_wxextra)}" if _wxextra else "") + "  *(bukan saat kejadian)*"))
    if wf:
        if wf_duration_ms is not None:
            basis.append(_row("Durasi Gangguan (rekaman)", f"≈ {wf_duration_ms:.0f} ms" + ("  (clear dalam rekaman)" if wf_cleared else "  (bertahan s.d. akhir rekaman)" if wf_cleared is False else "")))
        if "hf_ratio" in wf:
            basis.append(_row("Kandungan HF / Transien", f"HF ratio ≈ {wf.get('hf_ratio'):.2f}, di/dt ≈ {wf.get('di_dt_norm', 0):.1f}" + ("  → transien tajam (impulsif)" if wf_transient_sharp else "")))

    # ── Kasus 3 fasa simetris: power swing / non-eksternal ───────────
    if fault_type in ["ABC", "ABCG", "3PH", "3P"]:
        return (
            "Power Swing / Gangguan 3 Fasa",
            {
                "basis": basis,
                "candidates": [{
                    "Penyebab": "Power Swing / Gangguan 3 Fasa", "Skor": 0,
                    "Bukti": "Gangguan simetris 3 fasa jarang disebabkan petir/satwa — lebih sering power swing, eskalasi fault, atau kegagalan peralatan."
                    + (" Komponen sekuens nyaris hanya positif (I2/I1 & I0/I1 ≈ 0), konsisten gangguan seimbang." if balanced_seq else ""),
                }],
                "explanation": (
                    "Gangguan tiga fasa simetris perlu diverifikasi dengan event relay, catatan osilasi daya, "
                    "dan kondisi pembebanan sistem saat kejadian."
                ),
                "references": _DISTURBANCE_CAUSE_REFERENCES,
                "note": "Bandingkan dengan event CB, SOE relay, dan kondisi sistem untuk memastikan penyebab.",
            },
        )

    # ── Candidate scoring untuk gangguan 1–2 fasa (ke tanah/fase) ────
    candidates = []  # {label, score, evidence: [str]}

    def _cand(label, score, evidence):
        candidates.append({"label": label, "score": score, "evidence": evidence})

    # Petir / Sambaran Petir
    ev = []; sc = 0
    if ground:
        sc += 2; ev.append("gangguan ke tanah — pola umum flashover sambaran petir")
    if low_rf:
        sc += 2; ev.append("Rf rendah → busur cepat khas petir, bukan kontak resistif")
    if n_phases == 1:
        sc += 1; ev.append("SLG — tipe paling umum untuk induksi/sambaran petir")
    if clean_slg_seq:
        sc += 1; ev.append("komponen sekuens SLG murni (I0≈I1≈I2) — konsisten flashover satu fasa ke tanah")
    if wf_transient_sharp:
        sc += 2; ev.append("waveform: transien/HF tajam (impulsif) di awal gangguan — tanda kuat sambaran petir")
    if wf_cleared is True:
        sc += 1; ev.append("gangguan clear dalam rekaman (temporer) — konsisten flashover petir + reclose sukses")
    if wx_thunder:
        sc += 1; ev.append("cuaca lokasi saat ini: badai petir (caveat: bukan saat kejadian)")
    ev.append("Indonesia: kerapatan sambaran petir sangat tinggi sepanjang tahun")
    _cand("Sambaran Petir / Flashover", sc, ev)

    # Vegetasi / Pohon
    ev = []; sc = 0
    if hr_suspected or rf_est >= 10:
        sc += 3; ev.append(f"Rf tinggi (≈ {rf_est:.1f} Ω) → kontak resistif khas pohon/vegetasi")
    if ground:
        sc += 1; ev.append("gangguan ke tanah konsisten dengan kontak vegetasi")
    if (hr_suspected or rf_est >= 10) and r_i0_i1 >= 0.3:
        sc += 1; ev.append(f"zero-sequence kuat (I0/I1 ≈ {r_i0_i1:.2f}) menegaskan jalur arus ke tanah")
    if wf_cleared is False:
        sc += 1; ev.append("gangguan bertahan/tidak clear (cenderung permanen) — konsisten kontak vegetasi persisten")
    if wf_transient_sharp:
        sc -= 1; ev.append("transien tajam kurang konsisten dengan kontak resistif lambat")
    if low_rf:
        sc -= 2; ev.append("Rf rendah kurang konsisten dengan kontak vegetasi")
    _cand("Vegetasi / Pohon", sc, ev)

    # Satwa Liar (bird streamer / animal)
    ev = []; sc = 0
    if n_phases == 1 and ground:
        sc += 2; ev.append("SLG khas bird streamer / satwa menjembatani celah udara")
    if clean_slg_seq:
        sc += 1; ev.append("pola sekuens SLG murni (I0≈I1≈I2) khas streamer satu fasa ke tanah")
    if bird_window:
        sc += 3; ev.append(f"jam kejadian ({hour:02d}:xx) dekat puncak diurnal bird streamer ~06:00 & ~22:00 (Minnaar 2014)")
    elif hour is not None:
        ev.append(f"jam kejadian ({hour:02d}:xx) di luar puncak diurnal bird streamer")
    if wf_cleared is True and (wf_duration_ms is not None and wf_duration_ms <= 100):
        sc += 1; ev.append("durasi pendek + clear (temporer) — konsisten kontak satwa sesaat")
    if low_rf:
        sc += 1; ev.append("Rf rendah konsisten dengan flashover streamer")
    _cand("Satwa Liar (Bird Streamer)", sc, ev)

    # Flashover Polusi / Isolator
    ev = []; sc = 0
    if n_phases >= 2:
        sc += 1; ev.append("dapat melibatkan >1 fasa saat lapisan polutan basah flashover")
    if ground:
        sc += 1; ev.append("flashover sepanjang permukaan isolator ke tanah")
    if wx_wet:
        sc += 2; ev.append("cuaca lokasi basah/lembap (hujan/kabut/RH tinggi) — pemicu flashover polusi (caveat: bukan saat kejadian)")
    if wet_season:
        sc += 1; ev.append("musim hujan — pembasahan isolator lebih mungkin")
    ev.append("perlu pembasahan (kabut/embun/hujan ringan); sering berulang pada lokasi yang sama")
    _cand("Flashover Polusi / Isolator", sc, ev)

    # Kebakaran di bawah saluran
    ev = []; sc = 0
    if n_phases >= 2:
        sc += 1; ev.append("kebakaran lahan dapat menurunkan kuat dielektrik udara → flashover multi-fasa")
    if low_rf:
        sc += 1; ev.append("Rf rendah konsisten dengan flashover melalui udara terionisasi")
    if dry_season:
        sc += 1; ev.append("musim kemarau — risiko kebakaran lahan meningkat (Sumatra/Kalimantan)")
    if wx_dryclear:
        sc += 1; ev.append("cuaca lokasi cerah-kering — mendukung kondisi rawan kebakaran (caveat: bukan saat kejadian)")
    ev.append("verifikasi dengan hotspot AFIS/satelit di sekitar titik gangguan")
    _cand("Kebakaran di Bawah Saluran", sc, ev)

    candidates.sort(key=lambda c: -c["score"])
    top = candidates[0]
    runner = candidates[1] if len(candidates) > 1 else None
    # Ambang keyakinan: skor top rendah atau selisih tipis → belum yakin
    decisive = top["score"] >= 3 and (runner is None or top["score"] - runner["score"] >= 1)
    label = top["label"] if decisive else "Indikasi Awal (perlu validasi lapangan)"

    cand_rows = [
        {"Penyebab": c["label"], "Skor": c["score"], "Bukti": "; ".join(c["evidence"])}
        for c in candidates if c["score"] > 0
    ] or [{"Penyebab": top["label"], "Skor": top["score"], "Bukti": "; ".join(top["evidence"])}]

    explanation = (
        f"Kandidat terkuat: **{top['label']}** (skor {top['score']}). "
        + ("Selisih dengan kandidat berikutnya cukup jelas. " if decisive else
           "Selisih antar kandidat tipis — perlakukan sebagai indikasi awal, bukan kesimpulan. ")
        + "Skor disusun dari fault type, komponen simetris (I0/I1/I2 + sudut/impedansi), resistansi gangguan, jam & bulan kejadian, cuaca lokasi, dan tanda waveform (transien/durasi/reclose) sesuai fitur diskriminatif literatur."
    )

    return (
        label,
        {
            "basis": basis,
            "candidates": cand_rows,
            "explanation": explanation,
            "references": _DISTURBANCE_CAUSE_REFERENCES,
            "note": (
                "Penyebab final tetap perlu bukti eksternal: data sambaran petir (BMKG/lightning counter), "
                "hotspot kebakaran (AFIS/satelit), inspeksi tower (bekas flashover/streamer/jejak satwa), "
                "dan kondisi cuaca saat kejadian. Estimasi ini berbasis pola rekaman, bukan diagnosis pasti."
            ),
        },
    )


def single_ended_plot_score(single_result):
    if not single_result:
        return 0.0
    base_score = {
        "VALID": 9.0,
        "CHECK": 6.0,
        "UNCERTAIN": 3.0,
    }.get(str(single_result.get("status", "")).upper(), 5.0)
    warning_count = len(single_result.get("warnings", []) or [])
    return max(0.0, min(10.0, base_score - 0.4 * warning_count))


def build_summary_location_plot(
    line_param,
    local_gi_label,
    remote_gi_label,
    single_result,
    remote_single_result,
    two_result,
    reverse_two_result,
):
    if not line_param:
        return None

    line_length = float(line_param.get("length_km", 0.0) or 0.0)
    if line_length <= 0:
        return None

    points = []

    if single_result:
        points.append(
            {
                "label": f"SE {local_gi_label}",
                "distance": float(single_result.get("recommended_distance_km", 0.0)),
                "score": single_ended_plot_score(single_result),
                "symbol": "circle",
                "color": "#009e73",
            }
        )

    if remote_single_result:
        remote_position = build_remote_single_signed_position(
            line_length_km=line_length,
            remote_single_result=remote_single_result,
            scenario=st.session_state.get("two_ended_fault_scenario", "normal_internal_line_fault"),
            two_result=two_result,
        )
        points.append(
            {
                "label": f"SE {remote_gi_label}",
                "distance": remote_position["distance_from_local_km"],
                "score": single_ended_plot_score(remote_single_result),
                "symbol": "circle",
                "color": "#e67300",
            }
        )

    if two_result:
        points.append(
            {
                "label": f"DE {line_param.get('line_name', 'Original')}",
                "distance": float(two_result.get("distance_from_original_local_km", two_result.get("distance_km", 0.0))),
                "score": float(st.session_state.get("two_ended_quality", {}).get("quality_score", 10.0)),
                "symbol": "diamond",
                "color": "#2563eb",
            }
        )

    if reverse_two_result:
        points.append(
            {
                "label": f"DE {remote_gi_label}-{local_gi_label}",
                "distance": float(reverse_two_result.get("distance_from_original_local_km", reverse_two_result.get("distance_km", 0.0))),
                "score": float(st.session_state.get("two_ended_reverse_quality", {}).get("quality_score", 10.0)),
                "symbol": "diamond",
                "color": "#7c3aed",
            }
        )

    if not points:
        return None

    point_distances = [float(point["distance"]) for point in points]
    external_padding = max(0.05 * line_length, 1.0)
    x_min = min(0.0, min(point_distances) - external_padding)
    x_max = max(line_length, max(point_distances) + external_padding)

    marker_rows = []
    for point in points:
        distance = float(point["distance"])
        score = max(0.0, min(10.0, float(point["score"])))
        track = "Double-ended" if str(point["label"]).startswith("DE ") else "Single-ended"
        marker_rows.append(
            {
                "Point": point["label"],
                "Distance km": distance,
                "Distance %": 100.0 * distance / line_length,
                "Score": score,
                "Track": track,
                "Color": point["color"],
                "Symbol": point["symbol"],
                "Legend Name": point["label"],
            }
        )

    sorted_marker_rows = sorted(marker_rows, key=lambda item: float(item["Distance km"]))
    min_gap_km = max(0.02 * line_length, 0.75)
    grouped_marker_rows = []

    for row in sorted_marker_rows:
        if (
            not grouped_marker_rows
            or abs(
                float(row["Distance km"])
                - float(grouped_marker_rows[-1][-1]["Distance km"])
            )
            >= min_gap_km
        ):
            grouped_marker_rows.append([row])
        else:
            grouped_marker_rows[-1].append(row)

    label_layout = {}
    double_slots = [
        (-64, -160),
        (-64, 160),
        (-100, -160),
        (-100, 160),
    ]
    single_slots = [
        (96, -190),
        (96, 190),
        (150, -190),
        (150, 190),
    ]

    for group in grouped_marker_rows:
        double_rows = [row for row in group if row["Track"] == "Double-ended"]
        single_rows = [row for row in group if row["Track"] == "Single-ended"]

        if len(group) == 1:
            row = group[0]
            label_layout[id(row)] = (
                (-64, 0) if row["Track"] == "Double-ended" else (108, 0)
            )
        else:
            for index, row in enumerate(double_rows):
                label_layout[id(row)] = double_slots[index % len(double_slots)]

            for index, row in enumerate(single_rows):
                label_layout[id(row)] = single_slots[index % len(single_slots)]

    for row in marker_rows:
        _d_remote = line_length - row["Distance km"]
        _p_remote = _d_remote / line_length * 100.0 if line_length > 0 else 0.0
        row["Label"] = (
            f"<b>{row['Point']}</b><br>"
            f"{row['Distance km']:.2f} km ({row['Distance %']:.1f}%) dari {local_gi_label}<br>"
            f"{_d_remote:.2f} km ({_p_remote:.1f}%) dari {remote_gi_label}<br>"
            f"{row['Score']:.1f}/10"
        )
        row["Annotation Ay"], row["Annotation Ax"] = label_layout.get(
            id(row),
            (-64, 0) if row["Track"] == "Double-ended" else (108, 0),
        )

    marker_df = pd.DataFrame(marker_rows)
    x_profile = [
        x_min + i * (x_max - x_min) / 300.0
        for i in range(301)
    ]

    theme_base = st.get_option("theme.base")
    theme_background = st.get_option("theme.backgroundColor")
    if theme_base is None and theme_background:
        bg = str(theme_background).lstrip("#")
        if len(bg) >= 6:
            r = int(bg[0:2], 16)
            g = int(bg[2:4], 16)
            b = int(bg[4:6], 16)
            is_dark_theme = (0.2126 * r + 0.7152 * g + 0.0722 * b) < 128
        else:
            is_dark_theme = False
    else:
        is_dark_theme = theme_base == "dark"

    plot_template = "plotly_dark" if is_dark_theme else "plotly_white"
    plot_bg = "#0b1220" if is_dark_theme else "#ffffff"
    text_color = "#f8fafc" if is_dark_theme else "#111827"
    muted_text_color = "#cbd5e1" if is_dark_theme else "#475569"
    axis_title_color = "#f8fafc" if is_dark_theme else "#0f172a"
    annotation_bg = "rgba(15,23,42,0.92)" if is_dark_theme else "rgba(255,255,255,0.96)"
    annotation_border = "#94a3b8" if is_dark_theme else "#cbd5e1"
    terminal_color = "#f8fafc" if is_dark_theme else "#111827"

    fig = make_subplots(
        rows=2,
        cols=1,
        shared_xaxes=True,
        row_heights=[0.18, 0.82],
        vertical_spacing=0.08,
    )

    fig.add_shape(
        type="line",
        x0=0,
        x1=line_length,
        y0=0.5,
        y1=0.5,
        line=dict(color=muted_text_color, width=2),
        row=1,
        col=1,
    )

    fig.add_trace(
        go.Scatter(
            x=[0, line_length],
            y=[0.5, 0.5],
            mode="markers",
            marker=dict(size=12, color=[terminal_color, terminal_color], symbol="square"),
            hoverinfo="skip",
            showlegend=False,
        ),
        row=1,
        col=1,
    )
    fig.add_annotation(
        x=0,
        y=0.5,
        text=local_gi_label,
        showarrow=False,
        xanchor="left",
        yanchor="bottom",
        xshift=8,
        yshift=12,
        font=dict(color=text_color, size=13),
        row=1,
        col=1,
    )
    fig.add_annotation(
        x=line_length,
        y=0.5,
        text=remote_gi_label,
        showarrow=False,
        xanchor="right",
        yanchor="bottom",
        xshift=-8,
        yshift=12,
        font=dict(color=text_color, size=13),
        row=1,
        col=1,
    )

    for _, row in marker_df.sort_values(["Distance km", "Track"]).iterrows():
        fig.add_trace(
            go.Scatter(
                x=[row["Distance km"]],
                y=[0.5],
                mode="markers",
                marker=dict(
                    size=13,
                    color=row["Color"],
                    symbol=row["Symbol"],
                    line=dict(width=2, color=terminal_color),
                ),
                name=row["Legend Name"],
                legendgroup=row["Point"],
                showlegend=True,
                hovertemplate=(
                    f"{row['Point']}<br>"
                    f"{row['Distance km']:.2f} km ({row['Distance %']:.1f}%)<br>"
                    f"Score {row['Score']:.1f}/10"
                    "<extra></extra>"
                ),
            ),
            row=1,
            col=1,
        )

    for _, row in marker_df.iterrows():
        center = float(row["Distance km"])
        score = float(row["Score"])
        curve_width = max(line_length * (0.09 if row["Track"] == "Double-ended" else 0.06), 2.5)
        curve_y = [
            score / (1.0 + abs(x - center) / curve_width)
            for x in x_profile
        ]

        fig.add_trace(
            go.Scatter(
                x=x_profile,
                y=curve_y,
                mode="lines",
                line=dict(color=row["Color"], width=1.5),
                opacity=0.9,
                hoverinfo="skip",
                legendgroup=row["Point"],
                showlegend=False,
            ),
            row=2,
            col=1,
        )
        fig.add_trace(
            go.Scatter(
                x=[row["Distance km"]],
                y=[score],
                mode="markers",
                marker=dict(
                    size=16,
                    color=row["Color"],
                    symbol=row["Symbol"],
                    line=dict(width=2, color=terminal_color),
                ),
                name=row["Legend Name"],
                showlegend=False,
                legendgroup=row["Point"],
                customdata=[[row["Point"], row["Distance km"], row["Distance %"], row["Score"]]],
                hovertemplate=(
                    "%{customdata[0]}<br>"
                    "%{customdata[1]:.2f} km (%{customdata[2]:.1f}%)<br>"
                    "Score %{customdata[3]:.1f}/10"
                    "<extra></extra>"
                ),
            ),
            row=2,
            col=1,
        )
        fig.add_shape(
            type="line",
            x0=row["Distance km"],
            x1=row["Distance km"],
            y0=0,
            y1=score,
            line=dict(color=row["Color"], width=1.4),
            row=2,
            col=1,
        )

        fig.add_annotation(
            x=row["Distance km"],
            y=score,
            text=row["Label"],
            showarrow=True,
            arrowhead=2,
            arrowsize=0.8,
            arrowwidth=1.4,
            arrowcolor=row["Color"],
            ax=row["Annotation Ax"],
            ay=row["Annotation Ay"],
            bgcolor=annotation_bg,
            bordercolor=annotation_border,
            borderwidth=1,
            borderpad=4,
            font=dict(color=text_color, size=11),
            row=2,
            col=1,
        )

    fig.update_layout(
        title=f"Grafik SE dan DE - {line_param.get('line_name', '')}",
        template=plot_template,
        paper_bgcolor=plot_bg,
        plot_bgcolor=plot_bg,
        font=dict(color=text_color),
        height=800,
        margin=dict(l=58, r=34, t=118, b=92),
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.12,
            xanchor="right",
            x=1,
            bgcolor="rgba(15,23,42,0.85)" if is_dark_theme else "rgba(255,255,255,0.90)",
            bordercolor="#475569" if is_dark_theme else "#cbd5e1",
            borderwidth=1,
            font=dict(color=text_color),
        ),
    )
    fig.update_xaxes(
        range=[x_min, x_max],
        autorange=False,
        showgrid=False,
        zeroline=False,
        showticklabels=False,
        color=text_color,
        row=1,
        col=1,
    )
    fig.update_yaxes(
        range=[0.0, 1.0],
        autorange=False,
        showgrid=False,
        zeroline=False,
        showticklabels=False,
        color=text_color,
        row=1,
        col=1,
    )
    fig.update_xaxes(
        title=dict(
            text=f"Distance from {local_gi_label} (km)",
            font=dict(color=axis_title_color),
        ),
        range=[x_min, x_max],
        autorange=False,
        zeroline=False,
        color=text_color,
        tickfont=dict(color=muted_text_color),
        gridcolor="rgba(148,163,184,0.22)" if is_dark_theme else "rgba(148,163,184,0.35)",
        row=2,
        col=1,
    )
    fig.update_yaxes(
        title=dict(
            text="Quality / Confidence (0-10)",
            font=dict(color=axis_title_color),
        ),
        range=[-0.4, 11.4],
        showgrid=True,
        gridcolor="rgba(148,163,184,0.14)" if is_dark_theme else "rgba(148,163,184,0.22)",
        zeroline=False,
        color=text_color,
        tickfont=dict(color=muted_text_color),
        row=2,
        col=1,
    )

    return fig
