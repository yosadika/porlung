"""
Ekstraksi tanda waveform untuk membedakan PENYEBAB gangguan (bukan hanya tipe).

Fitur (Benner & Russell; Minnaar 2014; Jian 2021/2022):
- Transien / kandungan frekuensi tinggi (HF) di awal gangguan → khas sambaran petir
  (busur impulsif, di/dt tajam, energi harmonik tinggi).
- Durasi gangguan & apakah clear dalam rekaman → temporer (petir/satwa) vs permanen
  (vegetasi/isolator).
- Indikasi reclose-onto-fault (arus turun lalu naik lagi) bila rekaman cukup panjang.

Semua dihitung dari raw COMTRADE (assigned_df) + fault_window. Konservatif: bila
data tidak memadai, kembalikan dict kosong / nilai None (jangan mengarang).
"""

import numpy as np

from fault_detection import calculate_rms_sliding

_PHASE_CURRENTS = ["Ia", "Ib", "Ic"]


def compute_waveform_signatures(df, fault_window, samples_per_cycle, frequency: float = 50.0) -> dict:
    """Hitung tanda waveform di sekitar fault inception.

    Output dict (key hanya ada bila terhitung):
      di_dt_norm      : max|di/dt| dinormalisasi terhadap di/dt sinusoid murni (≥~3 → impulsif)
      hf_ratio        : energi harmonik (≥2) / fundamental pada 1 siklus onset
      transient_sharp : bool, transien tajam (petir)
      duration_ms     : durasi gangguan dalam rekaman (ms)
      cleared_in_record : True=clear (temporer), False=bertahan s.d. akhir, None=tak tentu
      reclose_in_record : True bila terdeteksi arus naik-lagi setelah clear
    """
    cols = [c for c in _PHASE_CURRENTS if c in (df.columns if df is not None else [])]
    if df is None or fault_window is None or not cols or "time" not in df.columns:
        return {}

    t = np.asarray(df["time"].values, dtype=float)
    n = len(t)
    spc = max(4, int(samples_per_cycle or 0))
    fi = int(fault_window.get("fault_index", 0))
    if n < spc * 3 or fi < spc or fi > n - spc:
        return {}

    dt = float(np.median(np.diff(t)))
    if dt <= 0:
        return {}
    omega = 2.0 * np.pi * float(frequency)

    sig: dict = {}

    pre = slice(max(0, fi - 2 * spc), fi)
    post = slice(fi, min(n, fi + spc))

    # Fasa terganggu dominan = RMS tertinggi 1 siklus setelah fault
    rms_post = {c: float(np.sqrt(np.mean(np.asarray(df[c].values[post], float) ** 2))) for c in cols}
    dom = max(rms_post, key=rms_post.get)
    x = np.asarray(df[dom].values, dtype=float)

    # ── di/dt ternormalisasi (transien impulsif) ──────────────────────
    w0, w1 = max(0, fi - 2), min(n, fi + spc)
    didt = np.diff(x[w0:w1]) / dt
    i_peak = np.sqrt(2.0) * max(rms_post[dom], 1e-6)
    didt_sin_max = omega * i_peak                       # max di/dt sinusoid fundamental
    di_dt_norm = float(np.max(np.abs(didt)) / didt_sin_max) if didt_sin_max > 0 else 0.0
    sig["di_dt_norm"] = round(di_dt_norm, 2)

    # ── HF ratio: energi harmonik vs fundamental (1 siklus onset) ─────
    # Window rektangular ~1 periode → sinusoid murni hanya di bin fundamental;
    # spike impulsif menambah energi broadband (HF tinggi).
    seg = x[fi:min(n, fi + spc)]
    if len(seg) >= 8:
        sp = np.abs(np.fft.rfft(seg))
        fund = sp[1] if len(sp) > 1 else 0.0
        hf = float(np.sqrt(np.sum(sp[2:] ** 2))) if len(sp) > 2 else 0.0
        sig["hf_ratio"] = round(float(hf / fund), 2) if fund > 1e-9 else 0.0
    else:
        sig["hf_ratio"] = 0.0

    sig["transient_sharp"] = bool(di_dt_norm >= 3.0 or sig["hf_ratio"] >= 0.5)

    # ── Durasi & clear/reclose dari RMS sliding |max phase| ───────────
    i_matrix = np.vstack([np.abs(np.asarray(df[c].values, float)) for c in cols])
    i_max = np.max(i_matrix, axis=0)
    rms = calculate_rms_sliding(i_max, spc)

    pre_vals = rms[pre]
    pre_rms = float(np.nanmedian(pre_vals)) if np.any(np.isfinite(pre_vals)) else np.nan
    fault_seg = rms[fi:min(n, fi + 2 * spc)]
    fault_rms = float(np.nanmax(fault_seg)) if np.any(np.isfinite(fault_seg)) else np.nan

    if np.isfinite(pre_rms) and np.isfinite(fault_rms) and fault_rms > max(pre_rms * 2.0, 1e-6):
        thresh = pre_rms * 1.5 if pre_rms > 0 else fault_rms * 0.3
        after = np.nan_to_num(rms[fi:], nan=0.0)
        # 1) cari KENAIKAN: indeks pertama RMS ≥ thresh (fault benar-benar elevated)
        risen = np.where(after >= thresh)[0]
        if risen.size > 0:
            rise_off = int(risen[0])
            rise_idx = fi + rise_off
            # 2) cari PENURUNAN setelah naik: RMS kembali < thresh (clear)
            below_after = np.where(after[rise_off:] < thresh)[0]
            if below_after.size > 0:
                fall_idx = rise_idx + int(below_after[0])
                sig["cleared_in_record"] = True
                sig["duration_ms"] = round((t[fall_idx] - t[rise_idx]) * 1000.0, 1)
                # 3) reclose: setelah clear + dead time, RMS naik lagi ≥ thresh
                rest = after[(fall_idx - fi) + spc:]
                if rest.size > 0 and float(np.max(rest)) >= thresh:
                    sig["reclose_in_record"] = True
            else:
                sig["cleared_in_record"] = False
                sig["duration_ms"] = round((t[-1] - t[rise_idx]) * 1000.0, 1)

    return sig
