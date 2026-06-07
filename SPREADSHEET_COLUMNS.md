# Mapping Kolom Spreadsheet — Transmission Fault Locator

Dokumen ini mendokumentasikan semua kolom yang dipakai dari setiap spreadsheet yang digunakan aplikasi. Diperbarui terakhir: 6 Juni 2026 (v1.0.30).

---

## 1. Main Database Spreadsheet

URL dikonfigurasi via `database_spreadsheet_url`. Berisi dua sheet utama.

---

### Sheet: `line_impedance`

Default sheet name: `line_impedance` (dapat diubah via `line_data_sheet_name`).  
Dibaca oleh `conductor_impedance_importer.py`, ditampilkan di `tabs/line_parameter.py`, difilter di sidebar `app.py`.

#### Kolom Identitas

| Kolom di Spreadsheet | Kandidat Nama Alternatif | Dipakai Untuk |
|---|---|---|
| `UPT` | — | Identifikasi Unit Pelaksana Transmisi (opsional) |
| `ULTG` | — | Filter sidebar ULTG |
| `GI A` | `GIA` | Terminal GI A (sisi lokal) |
| `GI B` | `GIB` | Terminal GI B (sisi remote) |
| `BAY PHT` | `BAY`, `PHT`, `BAY_PHT` | Identifikasi bay/PHT; dipakai sebagai GI B fallback |
| `SEGMENT` | `NAMA SEGMENT`, `NAMA SEGMEN` | Primary identifier nama saluran |
| `NAMA SALURAN` | `LINE NAME` | Nama saluran alternatif |
| `LINE` | `NO LINE`, `SIRKIT`, `CIRCUIT` | Nomor line/circuit |
| `JENIS KONDUKTOR` | `KONDUKTOR`, `CONDUCTOR TYPE`, `TYPE` | Tipe konduktor |
| `JUMLAH SIRKIT` | `JLH`, `JLH SIRKIT`, `CIRCUIT` | Jumlah sirkit |

#### Kolom Geometri

| Kolom di Spreadsheet | Kandidat Nama Alternatif | Satuan | Dipakai Untuk |
|---|---|---|---|
| `PANJANG KONDUKTOR (km)` | `PANJANG KONDUKTOR`, `PANJANG`, `LENGTH`, `LINE LENGTH`, `KM` | km | Panjang saluran |

#### Kolom Impedansi Positif Sequence (Z1)

| Kolom di Spreadsheet | Kandidat Nama Alternatif | Satuan | Dipakai Untuk |
|---|---|---|---|
| `Z1 REAL` | `IMPEDANSI Z1 REAL`, `R1` | Ω/km | Resistansi Z1 per km |
| `Z1 IMG` | `IMPEDANSI Z1 IMG`, `X1` | Ω/km | Reaktansi Z1 per km |
| `Z1 ABS` | `IMPEDANSI Z1`, `Impedansi Z1`, `Z1 ABS` | Ω/km | Magnitude Z1 per km |
| `Z1 ANGLE` | `IMPEDANSI Z1 ANGLE` | derajat | Sudut impedansi Z1 |

#### Kolom Impedansi Zero Sequence (Z0)

| Kolom di Spreadsheet | Kandidat Nama Alternatif | Satuan | Dipakai Untuk |
|---|---|---|---|
| `Z0 REAL` | `IMPEDANSI Z0 REAL`, `R0` | Ω/km | Resistansi Z0 per km |
| `Z0 IMG` | `IMPEDANSI Z0 IMG`, `X0` | Ω/km | Reaktansi Z0 per km |
| `Z0 ABS` | `IMPEDANSI Z0 ABS` | Ω/km | Magnitude Z0 per km |
| `Z0 ANGLE` | `IMPEDANSI Z0 ANGLE` | derajat | Sudut impedansi Z0 |

> Deteksi impedansi dilakukan oleh `detect_impedance_columns()` di `conductor_impedance_importer.py`. Jika nama kolom tidak persis cocok, aplikasi mencari kolom berdasarkan posisi relatif (setelah kolom referensi yang ditemukan).

#### Kolom Rasio Transformator

| Kolom di Spreadsheet | Kandidat Nama Alternatif | Format | Dipakai Untuk |
|---|---|---|---|
| `RATIO GI A CT` | `GI A CT`, `GIA CT`, `CT GI A` | `primary/secondary` (mis. `300/1`) | CT ratio sisi lokal |
| `RATIO GI A VT` | `GI A VT`, `GIA VT`, `VT GI A` | `primary/secondary` (mis. `150000/110`) | VT ratio sisi lokal |
| `RATIO GI B CT` | `GI B CT`, `GIB CT`, `CT GI B` | `primary/secondary` | CT ratio sisi remote |
| `RATIO GI B VT` | `GI B VT`, `GIB VT`, `VT GI B` | `primary/secondary` | VT ratio sisi remote |

> **Dihapus sejak v1.0.30:** Kolom `RATIO GI A CT/VT`, `RATIO GI B CT/VT`, `GI A`, `GI B` tidak lagi dibaca dari spreadsheet. CT/VT ratio diinput langsung di **Signal Assignment** (Local/Remote End); nama GI diturunkan dari nama saluran via `infer_gi_names_from_line_name()`. Kolom boleh tetap ada di spreadsheet tanpa efek.

#### Session State yang Diisi

| Key | Isi |
|---|---|
| `line_database_df` | DataFrame penuh dari sheet setelah load |
| `excel_impedance_data` | Dict hasil ekstraksi baris yang dipilih user |
| `excel_impedance_source` | String sumber data (`"Database Excel Line Data"` dst.) |

---

### Sheet: `distance_settings`

Default sheet name: `distance_settings` (dapat diubah via `distance_settings_sheet_name`).  
Dibaca oleh `rx_locus.py`, difilter di sidebar `app.py`.

> Deteksi kolom dilakukan oleh `detect_locus_distance_setting_columns()` di `rx_locus.py` dengan normalisasi: strip spasi, tanda kurung, slash, underscore, titik, dan unit Ω/ohm.

#### Kolom Identitas

| Kolom di Spreadsheet | Kandidat Nama Alternatif | Dipakai Untuk |
|---|---|---|
| `GI` | `Substation` | Nama GI/Substation; dipakai filter sidebar |
| `BAY` | — | Nama bay; dipakai filter sidebar |
| `LINE` | — | Nomor line (dinormalisasi: `"1.0"` → `"1"`); dipakai filter sidebar |
| `Merk` | `Brand` | Merek/manufaktur relay |
| `Type` | — | Tipe relay |

#### Kolom Zone Reach (Reactance)

| Kolom di Spreadsheet | Kandidat Nama Alternatif | Satuan | Dipakai Untuk |
|---|---|---|---|
| `Z1/X1 (ohm)` | `Z1/X1`, `X1` | Ω | Reach Zone 1 (reactance) |
| `Z2/X2 (ohm)` | `Z2/X2`, `X2` | Ω | Reach Zone 2 (reactance) |
| `Z3/X3 (ohm)` | `Z3/X3`, `X3` | Ω | Reach Zone 3 (reactance) |

#### Kolom Zone Reach (Resistive — Quadrilateral)

| Kolom di Spreadsheet | Satuan | Dipakai Untuk |
|---|---|---|
| `Z1 Res Phi (ohm)` | Ω | Resistive reach Zone 1 — phase fault |
| `Z1 Res Gnd (ohm)` | Ω | Resistive reach Zone 1 — ground fault |
| `Z2 Res Phi (ohm)` | Ω | Resistive reach Zone 2 — phase fault |
| `Z2 Res Gnd (ohm)` | Ω | Resistive reach Zone 2 — ground fault |
| `Z3 Res Phi (ohm)` | Ω | Resistive reach Zone 3 — phase fault |
| `Z3 Res Gnd (ohm)` | Ω | Resistive reach Zone 3 — ground fault |

#### Kolom kN (Zero Sequence Compensation)

| Kolom di Spreadsheet | Kandidat Nama Alternatif | Dipakai Untuk |
|---|---|---|
| `kN` | `k0`, `RE/RL`, `XE/XL` | Faktor kompensasi zero sequence (magnitude) |
| `kN angle` | `k0 angle`, `kN ang` | Sudut faktor kN (derajat) |

#### Session State yang Diisi

| Key | Isi |
|---|---|
| `distance_settings_df` | DataFrame penuh dari sheet setelah load |
| `rx_locus_substation_local` | GI lokal yang dipilih (sync dari sidebar) |
| `rx_locus_bay_local` | Bay lokal yang dipilih |
| `rx_locus_substation_remote` | GI remote yang dipilih |
| `rx_locus_bay_remote` | Bay remote yang dipilih |

---

## 2. Tower Schedule Spreadsheet

URL dikonfigurasi via `tower_schedule_url`. Sheet: `tower_schedule` (dapat diubah via `tower_schedule_sheet_name`).  
Dibaca dan diproses oleh `tower_map.py`, difilter di `app.py`.

### Kolom Wajib

| Kolom di Spreadsheet | Satuan Asli | Diproses Menjadi | Dipakai Untuk |
|---|---|---|---|
| `SPAN` | — | — | Label marker tower, identifier span |
| `JARAK` | meter | `JARAK km` (÷1000) | Jarak per span |
| `KUMULATIF` | meter | `KUMULATIF km` (÷1000) | Posisi kumulatif tower dari GI A; **dipakai untuk interpolasi fault** |
| `LATITUDE` | desimal atau koma | `lat` (numerik) | Koordinat lintang tower |
| `LONGITUDE` | desimal atau koma | `lon` (numerik) | Koordinat bujur tower |
| `SEGMENT` | — | — | Filter segmen; pre-fill dari sidebar |
| `ULTG` | — | — | Filter ULTG; pre-fill dari sidebar |

### Kolom Tampilan Tabel & Popup

| Kolom di Spreadsheet | Ditampilkan Di | Dipakai Untuk |
|---|---|---|
| `TYPE STRING` | Tabel tower, popup | Tipe string isolator |
| `JUMLAH STRING` | Tabel tower, popup | Jumlah string |

### Kolom Proteksi (Badge di Tabel Sekitar Fault)

Kolom-kolom ini tidak ditampilkan sebagai kolom tabel biasa, melainkan dirangkum menjadi **badge berwarna** di kolom "Proteksi Terpasang".

#### Kategori: Cleaning Isolator (badge hijau)

| Kolom | Kolom Tanggal |
|---|---|
| `CLEANING ISOLATOR L1` | `TANGGAL CLEANING L1` |
| `CLEANING ISOLATOR L2` | `TANGGAL CLEANING L2` |

#### Kategori: Proteksi Petir (badge kuning)

| Kolom | Kolom Tanggal |
|---|---|
| `PROTEKSI PETIR` | — |
| `DGS` | `TANGGAL PASANG DGS` |
| `MGGS` | `TANGGAL PASANG MGGS` |
| `TLA/NGLA` | — |
| `EGLA` | `TANGGAL PASANG EGLA` |
| `SUMUR BOR` | `TANGGAL PASANG SUMUR BOR` |
| `MDG` | `TANGGAL PASANG MDG` |
| `MRG` | `TANGGAL PASANG MRG` |
| `DG` | `TANGGAL PASANG DG` |
| `DMRG TIPE A` | `TANGGAL PASANG DMRG` |
| `DMRG TIPE B` | `TANGGAL PASANG DMRG` |
| `DMRG TIPE C` | `TANGGAL PASANG DMRG` |
| `JUMLAH PROTEKSI PETIR` | — |

> Badge induk "Proteksi Petir" hanya muncul jika tidak ada satu pun sub-device di atas yang terisi.

#### Kategori: Dinding Penahan Tanah (badge coklat)

| Kolom |
|---|
| `DINDING PENAHAN TANAH` |
| `BALOK KOPEL` |
| `BRONJONG` |
| `DINDING BATU KALI` |
| `SHEET PILE` |
| `SHOTCRETE + SOIL NAILING` |
| `TOTAL DPT` |

#### Kategori: Kerawanan Binatang (badge merah)

| Kolom |
|---|
| `KERAWAN BINATANG` / `KERAWANAN BINATANG` |
| `BURUNG` |
| `KERA` |
| `ULAR` |
| `TOTAL KERAWANAN` |

#### Kategori: Proteksi Binatang (badge ungu)

| Kolom |
|---|
| `PROTEKSI BINATANG` |
| `JARING` |
| `TOGAR ABES` |
| `KAWAT DURI` |
| `TERASI KAPUR BARUS` |
| `TOTAL PROTEKSI BINATANG` |

### Kolom yang Disembunyikan dari Tabel (tetap ada di DataFrame backend)

`Fault Context`, `Distance from Fault km`, `JARAK`, `KUMULATIF`, `JARAK km`, `KUMULATIF km`, `LATITUDE`, `LONGITUDE`, `SEGMENT`, `ULTG`

### Session State yang Diisi

| Key | Isi |
|---|---|
| `tower_schedule_df` | DataFrame penuh setelah load (sebelum filter tampilan) |
| `tower_schedule_filtered_df` | DataFrame setelah filter ULTG/Segment/Type String |
| `tower_schedule_selected_length_km` | Panjang saluran dari tower schedule (km) |
| `tower_schedule_selected_length_source` | Keterangan sumber panjang (`"max(KUMULATIF km)"` dst.) |
| `tower_schedule_selected_segment` | Segment yang aktif |
| `tower_schedule_selected_ultg` | ULTG yang aktif |

---

## 3. Upload End Filter — Session State Keys

Filter GI/line berada di sidebar, tetapi dikelompokkan di expander upload rekaman Local End dan Remote End. Segment hanya dipilih di Local End agar satu segment menjadi konteks line/tower, sementara UPT/ULTG local dan remote boleh berbeda.

| Key | Sumber Kolom | Sheet | Keterangan |
|---|---|---|---|
| `sidebar_filter_upt_local` | `UPT` | `distance_settings` | UPT Local End |
| `sidebar_filter_ultg_local` | `ULTG` | `distance_settings` | ULTG Local End, difilter UPT local |
| `sidebar_filter_segment` | `SEGMENT` | `line_impedance` | Segment Local End, difilter UPT/ULTG local |
| `sidebar_filter_gi_local` | `GI` | `distance_settings` | GI Local End |
| `sidebar_filter_bay_line_local` | `BAY` + `LINE` | `distance_settings` | Pilihan gabungan Bay/Line Local End |
| `sidebar_filter_bay_local` | `BAY` | `distance_settings` | Bay Local End hasil parse dari `sidebar_filter_bay_line_local` |
| `sidebar_filter_line_local` | `LINE` | `distance_settings` | Line Local End hasil parse dari `sidebar_filter_bay_line_local` |
| `sidebar_filter_upt_remote` | `UPT` | `distance_settings` | UPT Remote End |
| `sidebar_filter_ultg_remote` | `ULTG` | `distance_settings` | ULTG Remote End, difilter UPT remote |
| `sidebar_filter_gi_remote` | `GI` | `distance_settings` | GI Remote End |
| `sidebar_filter_bay_line_remote` | `BAY` + `LINE` | `distance_settings` | Pilihan gabungan Bay/Line Remote End |
| `sidebar_filter_bay_remote` | `BAY` | `distance_settings` | Bay Remote End hasil parse dari `sidebar_filter_bay_line_remote` |
| `sidebar_filter_line_remote` | `LINE` | `distance_settings` | Line Remote End hasil parse dari `sidebar_filter_bay_line_remote` |
| `sidebar_filter_upt` | `UPT` | `distance_settings` | Legacy alias dari `sidebar_filter_upt_local` |
| `sidebar_filter_ultg` | `ULTG` | `distance_settings` | Legacy alias dari `sidebar_filter_ultg_local` |

> **Perubahan v1.0.30+:** ULTG diambil dari `distance_settings` agar hierarki UPT→ULTG konsisten. Filter Local/Remote End sekarang punya UPT/ULTG masing-masing untuk mengakomodir GI local dan GI remote yang berada di UPT/ULTG berbeda.

---

## 4. Catatan Teknis

### Normalisasi Kolom

Setiap sheet menggunakan helper normalisasi yang berbeda:

| Sheet | Helper | Normalisasi yang Dilakukan |
|---|---|---|
| `line_impedance` | `find_column()` di `conductor_impedance_importer.py` | Case-insensitive substring match; strip spasi |
| `distance_settings` | `normalize_distance_setting_column()` di `rx_locus.py` | Hapus spasi, `()`, `-`, `_`, `/`, `\`, `.`, unit Ω/ohm |
| `tower_schedule` | Langsung di `tower_map.py` | Komma → titik untuk koordinat desimal |

### Prioritas Panjang Saluran dari Tower Schedule

1. `max(KUMULATIF km)` — prioritas utama
2. `sum(JARAK km)` — fallback jika KUMULATIF tidak tersedia

### Interpolasi Fault pada Tower Map

Posisi fault diinterpolasi dari kolom `KUMULATIF km` (bukan `JARAK km`). Dua tower pengapit dicari berdasarkan nilai KUMULATIF yang mengapit jarak fault, lalu koordinat lat/lon diinterpolasi secara linear.

---

## Sheet: `fault_cause` (ditulis aplikasi)

Default sheet name: `fault_cause` (override opsional via `fault_cause_sheet_name`). Berada di **Database Spreadsheet** (sama dengan `distance_settings`, tower schedule, data konduktor).

Dataset berlabel untuk pelatihan ML penentuan penyebab gangguan. **Ditulis** oleh aplikasi via Sheets API v4 (service account, scope `spreadsheets`) — bukan dibaca. Header auto-migrasi bila berbeda dari `DATASET_COLUMNS`; sheet dibuat otomatis bila belum ada. Spreadsheet harus di-share **Editor** ke email service account.

**Upsert berdasarkan `case_id` (kolom A):** `case_id = sha1(line_name|fault_time_cfg)[:16]`. Bila `case_id` cocok dengan baris yang ada → baris **di-update** (bukan duplikat); bila tidak → append. Re-analisis rekaman yang sama (line + waktu kejadian sama) memperbarui baris yang sama. `case_id` kosong (tak ada identitas) → selalu append.

Dirakit oleh `fault_cause_dataset.build_fault_cause_feature_row()` (43 kolom, `DATASET_COLUMNS`):

| Grup | Kolom |
|---|---|
| **Kunci unik** | `case_id` (kolom A — upsert key) |
| Metadata | `timestamp_analyzed`, `fault_time_cfg`, `line_name`, `gi_local`, `gi_remote`, `upt`, `ultg` |
| Fault type | `fault_type`, `n_phases`, `ground`, `ft_confidence` |
| Komponen simetris | `I0_A`,`I1_A`,`I2_A`, `r_i2_i1`,`r_i0_i1`,`r_i0_i2`, `ang_i2_i1_deg`,`ang_i0_i1_deg`, `r_v2_v1`,`r_v0_v1`, `Z1_ohm`,`Z2_ohm`,`Z0_ohm` |
| Resistansi | `rf_est_ohm`, `hr_suspected` |
| Waktu | `hour`, `month` |
| Cuaca | `weather_code`, `weather_desc`, `rain_mm`, `humidity_pct` |
| Waveform | `di_dt_norm`, `hf_ratio`, `transient_sharp`, `duration_ms`, `cleared_in_record`, `reclose_in_record` |
| Lokasi | `se_distance_km`, `de_distance_km`, `de_quality` |
| Prediksi rule | `predicted_cause`, `predicted_score` |
| **Target (label)** | `confirmed_cause` (diisi user dari `CONFIRMED_CAUSE_LABELS` setelah inspeksi) |

---

## Sheet: `saved_cases` + `saved_cases_data` (ditulis & dibaca aplikasi)

Simpan/muat case via spreadsheet — **TANPA Google Drive** (service account akun personal tidak punya kuota Drive → `storageQuotaExceeded`). **Ditulis & dibaca** via Sheets API (service account). Upsert by `case_id` (kolom A). Di **Database Spreadsheet**. Override sheet name via `saved_cases_sheet_name`.

**`saved_cases`** = indeks ringkas (1 baris/case):

| Kolom | Isi |
|---|---|
| `case_id` | `sha1(line_name\|fault_time_cfg)[:16]` — kunci upsert |
| `case_name` | Nama case (slug line) |
| `line_name`, `gi_local`, `gi_remote` | Identitas saluran |
| `fault_time_cfg` | Timestamp CFG (trigger/start) |
| `saved_at` | ISO timestamp saat disimpan (untuk urut daftar) |
| `filename` | Nama file ZIP internal |
| `size_bytes` | Ukuran ZIP |
| `n_chunks` | Jumlah chunk payload di `saved_cases_data` |

**`saved_cases_data`** = payload (1 baris/case, dibuat dgn ~200 kolom): `[case_id, chunk0, chunk1, ...]`. Payload = ZIP case → base64, dipecah ≤49000 char/sel (di bawah batas 50.000). Ditulis RAW (agar base64 tak jadi formula). Load: pilih dari `saved_cases` (urut `saved_at` desc) → cari baris by `case_id` di `saved_cases_data` → gabung sel chunk → base64 decode → `restore_case_archive`. Objek figure (Plotly) di-drop saat snapshot (dihitung ulang dari selection), jadi payload ramping.
