# FORMULAS — Algoritma & Rumus Transmission Fault Locator

Dokumen ini adalah **sumber kebenaran matematis** untuk deteksi fault cursor dan perhitungan Single-End (SE), Double-End (DE), serta High-Resistance (HR). Isi diturunkan langsung dari kode (`fault_detection.py`, `single_ended.py`, `two_ended.py`, `high_resistance.py`).

**Aturan dokumentasi:**
- Saat formula/algoritma di kode berubah, perbarui file ini.
- PRD.md dan CLAUDE.md cukup **merujuk** ke file ini, jangan menyalin ulang rumus (cegah drift).
- Setiap nilai yang **bukan** berasal dari literatur ditandai eksplisit sebagai **[engineering default]**.

Notasi: `V`, `I` = fasor kompleks (full-cycle DFT). `Z₁` = impedansi urutan positif per km. `L` = panjang saluran (km). `Im(·)`, `Re(·)` = bagian imajiner/real. `*` = konjugat kompleks.

---

## 1. Fault Detection & Cursor

Sumber: `fault_detection.py` — `detect_fault_inception`, `build_fault_window`.

### 1.1 RMS sliding window (1 siklus)

```
samples_per_cycle = round(fs / frequency)
rms[k] = sqrt( Σ_{j=k-N+1}^{k} x[j]² / N ),  N = samples_per_cycle
```

Backward-looking: `rms[k]` mencerminkan N sampel terakhir. Implikasi: untuk gangguan kecil/high-resistance, pickup dapat tercapai beberapa sampel setelah inception sebenarnya (keterbatasan diketahui metode RMS — Saha 2010).

### 1.2 Envelope tiga fasa

```
current_rms_max[k] = max( Ia_rms[k], Ib_rms[k], Ic_rms[k] )
voltage_rms_min[k] = min( Va_rms[k], Vb_rms[k], Vc_rms[k] )
```

Max untuk arus & min untuk tegangan memastikan gangguan fasa tunggal tetap terdeteksi.

### 1.3 Referensi pre-fault & threshold pickup

```
prefault_current = median( current_rms_max[ N : N·min_prefault_cycles ] )
prefault_voltage = median( voltage_rms_min[ N : N·min_prefault_cycles ] )
```

Referensi adaptif (jika nominal tersedia):
- `prefault_voltage < 0.97 × nominal_VT` → pakai `nominal_VT` (mode `nominal_vt_assisted`)
- `prefault_current > 1.20 × nominal_CT` → pakai `nominal_CT` (mode `nominal_ct_vt_assisted`)

Threshold pickup:
```
current_pickup = reference_current × 2.0        ← [engineering default]
voltage_pickup = reference_voltage × 0.85       ← [engineering default]
```

> **Catatan penting:** multiplier `2.0` dan `0.85` **bukan** berasal dari persamaan referensi tertentu. IEEE C37.114-2014 dan Saha (2010) tidak menetapkan nilai tetap; ini nilai praktis industri. Untuk gangguan high-resistance/weak-infeed, gunakan opsi adaptive-sigma atau superimposed.

### 1.4 Kriteria inception (kondisi OR)

```
pickup[k] = (current_rms_max[k] > current_pickup) OR (voltage_rms_min[k] < voltage_pickup)
fault_index = indeks pertama (≥ N·min_prefault_cycles) yang memenuhi pickup (persisten ≥ consecutive_samples)
```

Opsi lanjutan (jika `adaptive_threshold_sigma` aktif):
```
disturbance_score[k] = max( (current_rms_max[k] − prefault_current)/σ_I ,
                            (prefault_voltage − voltage_rms_min[k])/σ_V )
pickup[k] |= disturbance_score[k] ≥ adaptive_threshold_sigma
```
`σ` = robust sigma dari baseline pre-fault.

### 1.5 Superimposed (metode `hybrid_superimposed`)

Mendeteksi lonjakan energi komponen ΔV/ΔI (sinyal dikurangi referensi pre-fault siklus sebelumnya). Jika inception superimposed lebih awal dari RMS dan dalam ±2 siklus, dipakai sebagai inception. Ref: Eriksson dkk (1985) Sec. II; Saha (2010) Sec. 2.5.

### 1.6 Window analisis & DFT cursor

```
left_index  = max(0, fault_index − pre_fault_cycles · N)
right_index = min(len−1, fault_index + post_fault_cycles · N)
dft_index   = min(len−1, fault_index + N)        # 1 siklus SETELAH inception
```

DFT cursor diletakkan 1 siklus setelah inception agar window DFT (di kirinya) tidak melintasi titik gangguan. **Fasor pada `dft_index` inilah input semua kalkulasi SE/DE/HR/R-X.** Ref: Phadke & Thorp (2009) Sec. 3.2.

**Default:** checkbox deteksi otomatis adaptif = **off** (local & remote). Fault inception ≠ DFT cursor — jangan dipertukarkan.

---

## 2. Single-End (SE)

Sumber: `single_ended.py`. Default method: **reactance**.

### 2.1 Impedansi loop per fault type

`K₀ = (Z₀ − Z₁)/Z₁`, `I₀ = IE/3`.

| Fault | Z_app |
|---|---|
| AG | `Va / (Ia + K₀·I₀)` |
| BG | `Vb / (Ib + K₀·I₀)` |
| CG | `Vc / (Ic + K₀·I₀)` |
| AB / ABG | `(Va − Vb) / (Ia − Ib)` |
| BC / BCG | `(Vb − Vc) / (Ib − Ic)` |
| CA / CAG | `(Vc − Va) / (Ic − Ia)` |
| ABC / ABCG | `V₁ / I₁` (fallback `Va/Ia`) |

DLG (ABG/BCG/CAG) memakai loop fase-fase sebagai pendekatan lokasi awal. Ref: Saha (2010) Eq. 6.3; Phadke & Thorp (2009) Eq. 9.33.

### 2.2 Tiga metode jarak

```
Magnitude   : d_|Z| = |Z_app| / |Z₁|
Reactance   : d_X   = Im(Z_app) / Im(Z₁)              ← default
Projection  : d_proj = Re(Z_app · û₁*) / |Z₁|,  û₁ = Z₁/|Z₁|
```
Ref: Saha (2010) Eq. 6.2; Phadke & Thorp (2009) Eq. 9.34. Projection lebih stabil untuk gangguan resistif.

### 2.3 Estimasi tahanan gangguan

```
Z_line_est = d_recommended · Z₁
Rf_est = Re( Z_app − Z_line_est )
```

### 2.4 Takagi (fallback SLG)

Aktif **hanya** untuk SLG (AG/BG/CG) bila prefault tersedia DAN jarak konvensional out-of-range DAN hasil Takagi masuk range:

```
ΔI_loop = (I_fault − I_prefault) + K₀·(I0_fault − I0_prefault)
d = Im( U_loop · ΔI_loop* ) / Im( Z₁ · I_loop · ΔI_loop* )
```

Rf tereliminasi eksak karena `Im(Rf·|ΔI|²) = 0`. Method name → `"takagi"`. Ref: Saha (2010) Eq. 6.8.

### 2.5 Status & warning

`status`: `VALID` (tanpa warning) → `CHECK` (ada warning) → `UNCERTAIN` (jarak < 0 atau > L pada konteks internal). Warning antara lain: jarak negatif, jarak > L, magnitude vs reactance beda > 15% L, `|Rf_est| > 10 Ω`, deviasi sudut Z_app vs Z₁ > 15°, arus fasa depressed (indikasi load-flow/backfeed).

---

## 3. Double-End (DE)

Sumber: `two_ended.py`. Metode: positive-sequence closed-form.

### 3.1 Persamaan dua ujung

Local di x=0, remote di x=L:
```
Vlocal(x)  = V1L − I1L · Z₁ · x
Vremote(x) = V1R − I1R · Z₁ · (L − x)
```
Titik gangguan saat `Vlocal(x) = Vremote(x)`:
```
x = ( V1L − V1R + I1R · Z₁ · L ) / ( Z₁ · (I1L + I1R) )
```
Jika arah arus remote `opposite_to_line` → `I1R = −I1R`. Imunitas Rf inheren (dua persamaan dua ujung). Setara IEEE C37.114-2014 & Saha (2010) Ch. 7 (versi positive-sequence); Eriksson (1985).

### 3.2 Output

```
distance_km        = Re(x)
distance_percent   = distance_km / L · 100
V_fault_from_local = V1L − I1L · Z₁ · distance_km
V_fault_from_remote= V1R − I1R · Z₁ · (L − distance_km)
voltage_mismatch   = V_fault_from_local − V_fault_from_remote
```

### 3.3 Quality score (0–10)

Mulai 10, lalu kurangi (`boundary_margin = 0.002·L`):

| Kondisi | Penalti |
|---|---|
| `d < −boundary_margin` | −4.0 |
| `d > L + boundary_margin` | −4.0 |
| `Im(x) > 0.05·L` | −2.0 |
| `0.02·L < Im(x) ≤ 0.05·L` | −0.5 |
| `mismatch_ratio > 0.10` | −1.5 |
| `0.05 < mismatch_ratio ≤ 0.10` | −0.5 |

`mismatch_ratio = |voltage_mismatch| / max(|V_fault_local|, |V_fault_remote|, 1)`. Dikunci ke [0, 10]. Ref: pendekatan Saha (2010).

### 3.4 Adaptasi remote & unsynchronized

`transform_remote_phasors` menerapkan `e^{jθ}` (angle shift), polaritas VT, polaritas CT sebelum rumus. Untuk unsynchronized, `choose_best_two_ended_adaptation` melakukan brute-force angle search (default step 5°, urut dari |θ| terkecil, early-exit bila score < 10). Mode: `auto_adapt_record`, `auto_current_direction_only`, manual `into_line`/`opposite_to_line`.

### 3.5 Visual Sync Quality

Visual Sync Score = **Pearson correlation instantaneous** waveform tegangan fasa terganggu (2 siklus sekitar DFT cursor, setelah alignment). **Bukan** perbandingan sudut DFT — sudut DFT tidak valid antar recorder non-GPS. Threshold: ≥0.85 Sinkron; 0.50–0.85 Cukup; <0.50 Kurang; <0 Terbalik.

---

## 4. High-Resistance Check (HR)

Sumber: `high_resistance.py`. Loop impedance & tiga metode jarak identik SE (bagian 2.1–2.2).

```
Z_line_est = d_X · Z₁
Rf_est = Re( Z_app − Z_line_est )
Δθ = | ∠Z_app − ∠Z₁ |
```

Indikator HR (high_resistance_suspected) bila salah satu:
- `Rf_est ≥ rf_threshold_ohm` (default 10 Ω) **[engineering default]**
- `Δθ ≥ angle_deviation_threshold_deg` (default 10°) **[engineering default]**
- deviasi `d_X` vs `d_|Z|` ≥ `distance_deviation_threshold_percent` (default 15%) **[engineering default]**
- jarak keluar dari range saluran

Confidence 0–10 + evidence score ditampilkan. Ref: Saha (2010) Ch. 6; IEEE C37.114-2014 Sec. 5.4.

---

## 5. Pemetaan Literatur & Status Implementasi

PDF sumber ada di [`literature/`](literature/). Ringkasan pembanding di memory `fault_location_references.md`.

| Topik | Formula | Referensi | Status |
|---|---|---|---|
| Deteksi inception (RMS, kriteria OR) | Sec. 1.1–1.4 | Saha (2010) Sec. 2.3–2.4; IEEE C37.114 Sec. 5.2 | ✅ |
| Superimposed inception | Sec. 1.5 | Eriksson (1985) Sec. II; Saha Sec. 2.5 | ✅ (opsional hybrid) |
| DFT cursor placement | Sec. 1.6 | Phadke & Thorp (2009) Sec. 3.2 | ✅ |
| SE reactance/magnitude/projection | Sec. 2.2 | Saha Eq. 6.2; Phadke Eq. 9.34 | ✅ |
| SE Takagi (SLG) | Sec. 2.4 | Saha Eq. 6.8; Phadke Eq. 9.36 | ✅ (fallback) |
| SE Eriksson quadratic (infeed) | — | Eriksson (1985) Eq. 14 | ❌ belum |
| DE positive-sequence | Sec. 3.1 | IEEE C37.114; Saha Ch. 7; Eriksson | ✅ |
| DE negative-sequence | — | IEEE C37.114 | ❌ belum (bisa lebih robust untuk asimetris) |
| DE unsynchronized (θ-elimination analitik) | — | Saha (Newton-Raphson) | ⚠️ pakai brute-force angle search (Sec. 3.4) |
| DE distributed-parameter (cosh/sinh) | — | Saha Eq. 7.8 | ❌ tidak relevan (database tak punya admitansi Y) |

**Threshold yang merupakan engineering default (bukan dari literatur):** pickup arus ×2.0, pickup tegangan ×0.85 (Sec. 1.3); `rf_threshold` 10 Ω, `angle_deviation` 10°, `distance_deviation` 15% (Sec. 4).

---

## 6. Tampilan In-App

Formula + nilai aktual ditampilkan ke user via expander:
- SE: `render_se_formula_expander` (`fault_workflow_helpers.py`)
- DE: `render_de_formula_expander` (`tabs/double_ended.py`)
- HR: `render_hr_formula_expander` (`fault_workflow_helpers.py`)
- Fault cursor: `render_fault_cursor_explanation` (`fault_workflow_helpers.py`) — tabel + langkah + referensi

Expander adalah representasi runtime; **file ini adalah referensi statis** untuk audit/review.
