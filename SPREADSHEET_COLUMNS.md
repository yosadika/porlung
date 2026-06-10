# Mapping Kolom Spreadsheet — Transmission Fault Locator

Dokumen ini mendokumentasikan semua kolom yang dipakai dari setiap spreadsheet yang digunakan aplikasi. Diperbarui terakhir: 6 Juni 2026 (v1.0.30).

---

## 1. Main Database Spreadsheet

URL dikonfigurasi via `database_spreadsheet_url`. Berisi dua sheet utama.

---

### Sheet: `line_impedance` / `line_data`

Default sheet name untuk parameter saluran: `line_impedance` (dapat diubah via `line_data_sheet_name` / credentials `database_line_sheet`).  
Dibaca oleh `conductor_impedance_importer.py`, ditampilkan di `tabs/line_parameter.py`, difilter di sidebar `app.py`. Sheet `line_data` dipakai terpisah sebagai sumber utama zona R-X Locus via `rx_locus_line_data_sheet_name` / credentials `rx_locus_line_data_sheet` bila berisi kolom setting relay primary/secondary eksplisit.

#### Kolom Identitas

| Kolom di Spreadsheet | Kandidat Nama Alternatif | Dipakai Untuk |
|---|---|---|
| `No` | — | Nomor urut spreadsheet; diabaikan oleh kalkulasi |
| `UPT` | — | Identifikasi Unit Pelaksana Transmisi (opsional) |
| `Tegangan` | `NOMINAL VOLTAGE`, `VOLTAGE` | Metadata level tegangan; ditampilkan pada detail baris bila tersedia |
| `ULTG` | — | Filter sidebar ULTG |
| `GI` | `GI A`, `GIA` | Identifikasi GI pada baris line impedance |
| `BAY` | `BAY PHT`, `PHT`, `BAY_PHT` | Identifikasi bay/PHT; dipakai sebagai fallback nama line |
| `SEGMENT` | `NAMA SEGMENT`, `NAMA SEGMEN` | Primary identifier nama saluran |
| `NAMA SALURAN` | `LINE NAME` | Nama saluran alternatif |
| `LINE` | `NO LINE`, `SIRKIT`, `CIRCUIT` | Nomor line/circuit |
| `JENIS KONDUKTOR` | `KONDUKTOR`, `CONDUCTOR TYPE`, `TYPE` | Tipe konduktor |
| `JUMLAH SIRKIT` | `JLH`, `JLH SIRKIT`, `CIRCUIT` | Jumlah sirkit |

Struktur `line_impedance` aktif:

`No`, `UPT`, `Tegangan`, `ULTG`, `GI`, `BAY`, `LINE`, `SEGMENT`, `PANJANG KONDUKTOR (km)`, `JENIS KONDUKTOR`, `JUMLAH SIRKIT`, `Z1 REAL`, `Z1 IMG`, `Impedansi Z1`, `Z1 ABS`, `Z1 ANGLE`, `Z0 REAL`, `Z0 IMG`, `Impedansi Z0`, `Z0 ABS`, `Z0 ANGLE`.

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

> **Dihapus sejak v1.0.30:** Kolom `RATIO GI A CT/VT`, `RATIO GI B CT/VT`, `GI A`, `GI B` tidak lagi dibaca dari sheet `line_impedance`. CT/VT ratio utama berasal dari CFG atau input **Signal Assignment** (Local/Remote End). Fallback spreadsheet hanya memakai kolom rasio pada sheet `line_data` jika CFG berisi `1/1`.

#### Session State yang Diisi

| Key | Isi |
|---|---|
| `line_database_df` | DataFrame penuh dari sheet setelah load |
| `excel_impedance_data` | Dict hasil ekstraksi baris yang dipilih user |
| `excel_impedance_source` | String sumber data (`"Database Spreadsheet Line Data"` dst.) |

> Auto-pick di tab Line Parameter memakai filter sidebar Local End (`sidebar_filter_gi_local`, `sidebar_filter_bay_local`, `sidebar_filter_line_local`) untuk mencocokkan kolom `GI`, `BAY`, dan `LINE` pada `line_impedance`. `sidebar_filter_segment` berasal dari `tower_schedule` dan tidak lagi dipakai sebagai kunci pemilihan otomatis baris impedansi.

Pada sumber `Database Spreadsheet Line Data`, form `Nama segment` di tab Line Parameter dapat mengisi nama segment/line sesi berjalan dan tombol `Update Nama Segment` menulis ulang cell kolom `SEGMENT` pada baris `line_impedance` yang dipilih. Operasi update membutuhkan Google service account dengan akses Editor dan hanya mengubah cell `SEGMENT`, bukan seluruh baris.

Untuk sumber `Database Spreadsheet Cable Data`, user dapat memilih beberapa baris konduktor dan panjang section masing-masing. Aplikasi menghitung impedansi ekuivalen berbobot panjang (`sum(Z_i * panjang_i) / sum(panjang_i)`) lalu menyimpan detail section di `excel_impedance_data["mixed_conductor_sections"]`.

`excel_impedance_data`, termasuk `mixed_conductor_sections`, disimpan ke case ZIP dan payload `saved_cases_data` saat case disimpan via spreadsheet.

#### Kolom Setting Relay Distance Opsional (`line_data`)

Jika sheet `line_data` menyediakan setting relay distance dalam satuan eksplisit, R-X Locus memakai kolom berikut:

| Kolom di Spreadsheet | Base | Dipakai Untuk |
|---|---|---|
| `GI` | — | Filter GI/Substation |
| `Nama Line` | `Bay`, `Nama Bay` | Filter Bay/nama line relay |
| `Nomor Line` | `No Line`, `Line`, `Nama Line dan Nomor Line` | Nomor line untuk auto-select setting; `Nama Line dan Nomor Line` hanya fallback format lama |
| `MERK` | — | Label setting |
| `Type` | — | Tipe relay |
| `Z1 Sec (Ω)`, `Z2 Sec (Ω)`, `Z3 Sec (Ω)` | secondary | X reach Zone 1/2/3 relay secondary |
| `R1P Sec (Ω)`, `R2P Sec (Ω)`, `R3P Sec (Ω)` | secondary | Resistive reach phase fault Zone 1/2/3 |
| `R1G Sec (Ω)`, `R2G Sec (Ω)`, `R3G Sec (Ω)` | secondary | Resistive reach ground fault Zone 1/2/3 |
| `Z1 Prim (Ω)`, `Z2 Prim (Ω)`, `Z3 Prim (Ω)` | primary | X reach Zone 1/2/3 primary |
| `R1P Prim (Ω)`, `R2P Prim (Ω)`, `R3P Prim (Ω)` | primary | Resistive reach phase fault Zone 1/2/3 |
| `R1G Prim (Ω)`, `R2G Prim (Ω)`, `R3G Prim (Ω)` | primary | Resistive reach ground fault Zone 1/2/3 |

> R-X Locus default memakai sumber `line_data` karena kolom `Sec`/`Prim` tidak ambigu. `distance_settings` tetap tersedia sebagai fallback.
> Struktur baru memisahkan `Nama Line` dan `Nomor Line`, sehingga filter R-X Locus mengikuti pola sheet lain: GI -> Bay/Nama Line -> Nomor Line. Format lama `Nama Line dan Nomor Line` masih didukung sebagai fallback.

#### Guardrail Detail `line_data` untuk R-X Locus

Struktur `line_data` aktif:

`No`, `UPT`, `Tegangan`, `ULTG`, `GI`, `Nama Line`, `Nomor Line`, `SEGMENT`, `Panjang (km)`, `Jenis Konduktor`, `Jumlah Sirkit`, `MERK`, `Type`, `VT Ratio primary`, `VT Ratio Secondary`, `CT Ratio Primary`, `CT Ratio Secondary`, `Z1 Sec (ohm)`, `tZ1 (s)`, `R1P Sec (ohm)`, `R1G Sec (ohm)`, `Z2 Sec (ohm)`, `tZ2 (s)`, `R2P Sec (ohm)`, `R2G Sec (ohm)`, `Z3 Sec (ohm)`, `tZ3 (s)`, `R3P Sec (ohm)`, `R3G Sec (ohm)`, `Line Impedance (ohm/km)`, `VTR/CTR`, `Z1 Prim (ohm)`, `tZ1 (s)`, `R1P Prim (ohm)`, `R1G Prim (ohm)`, `Z2 Prim (ohm)`, `tZ2 (s)`, `R2P Prim (ohm)`, `R2G Prim (ohm)`, `Z3 Prim (ohm)`, `tZ3 (s)`, `R3P Prim (ohm)`, `R3G Prim (ohm)`, `Z Line Prim (ohm)`, `R Load Prim (ohm)`, `Real/ABS`.

- `Nama Line` adalah opsi Bay/nama line pada UI R-X Locus. Alias lama `Bay` dan `Nama Bay` tetap diterima.
- `Nomor Line` adalah nomor line untuk auto-select baris relay. Alias lama `No Line`, `Line`, dan `Nama Line dan Nomor Line` tetap fallback.
- `VT Ratio primary`, `VT Ratio Secondary`, `CT Ratio Primary`, dan `CT Ratio Secondary` dipakai untuk mengisi default Signal Assignment bila rasio CT/VT dari CFG adalah `1/1`; rasio CFG valid tetap prioritas.
- Kolom `Prim` dipakai saat `rx_locus_zone_setting_base_* = "primary"`.
- Kolom `Sec` dipakai saat `rx_locus_zone_setting_base_* = "secondary"`, lalu dikonversi ke primary ohm memakai CT/VT dari Signal Assignment aktif, bukan memakai rasio pada spreadsheet.
- Kolom `MERK` dan `Type` dipakai sebagai catatan kaki relay Local/Remote pada Summary berdasarkan filter sidebar GI/Bay/Line.
- Kolom waktu `tZ*`, `Z Line Prim`, `R Load Prim`, `Line Impedance`, `VTR/CTR`, `Real/ABS`, `UPT`, `Tegangan`, `ULTG`, `SEGMENT`, `Panjang`, `Jenis Konduktor`, dan `Jumlah Sirkit` adalah metadata/audit untuk saat ini; belum menentukan polygon overlay.
- Sheet khusus zona R-X adalah `rx_locus_line_data_sheet_name` / credentials `rx_locus_line_data_sheet` dengan default `line_data`. Jangan disamakan dengan `line_data_sheet_name` / `database_line_sheet` yang dipakai Line Parameter.
- Overlay zona R-X adalah visualisasi engineering quadrilateral/polygonal berbasis `R reach` dan `X reach`; bukan replica penuh relay vendor sampai tilt reactance, directional supervision, left/right blinder detail, load encroachment, memory/polarizing quantity, dan logic pabrikan dimodelkan.

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
| `rx_locus_line_data_sheet_name` | Nama sheet `line_data` khusus sumber zona R-X Locus |
| `rx_locus_zone_setting_source_local` / `remote` | Source zona relay: `line_data` atau `distance_settings` |
| `rx_locus_zone_setting_base_local` / `remote` | Base satuan setting: `primary` atau `secondary` |
| `rx_locus_setting_row_local` / `remote` | Label baris relay yang dipilih; disimpan ke case dan dipakai rebuild figure |

---

## 2. Tower Schedule Spreadsheet

URL dikonfigurasi via `tower_schedule_url`. Sheet: `tower_schedule` (dapat diubah via `tower_schedule_sheet_name`).  
Dibaca dan diproses oleh `tower_map.py`, difilter di `app.py`.

Struktur aktif `tower_schedule`:

`SPAN`, `JARAK`, `KUMULATIF`, `LATITUDE`, `LONGITUDE`, `SEGMENT`, `UPT`, `ULTG`, `TYPE STRING`, `JUMLAH STRING`, `CLEANING ISOLATOR L1`, `TANGGAL CLEANING L1`, `CLEANING ISOLATOR L2`, `TANGGAL CLEANING L2`, `PROTEKSI PETIR`, `DGS`, `TANGGAL PASANG DGS`, `MGGS`, `TANGGAL PASANG MGGS`, `TLA/NGLA`, `EGLA`, `TANGGAL PASANG EGLA`, `SUMUR BOR`, `TANGGAL PASANG SUMUR BOR`, `MDG`, `TANGGAL PASANG MDG`, `DMRG TIPE A`, `DMRG TIPE B`, `DMRG TIPE C`, `TANGGAL PASANG DMRG`, `MRG`, `TANGGAL PASANG MRG`, `DG`, `TANGGAL PASANG DG`, `JUMLAH PROTEKSI PETIR`, `DINDING PENAHAN TANAH`, `BALOK KOPEL`, `BRONJONG`, `DINDING BATU KALI`, `SHEET PILE`, `SHOTCRETE + SOIL NAILING`, `TOTAL DPT`, `KERAWANAN BINATANG`, `BURUNG`, `KERA`, `ULAR`, `TOTAL KERAWANAN`, `PROTEKSI BINATANG`, `JARING`, `TOGAR ABES`, `KAWAT DURI`, `TERASI KAPUR BARUS`, `TOTAL PROTEKSI BINATANG`.

### Kolom Wajib

| Kolom di Spreadsheet | Satuan Asli | Diproses Menjadi | Dipakai Untuk |
|---|---|---|---|
| `SPAN` | — | — | Label marker tower, identifier span |
| `JARAK` | meter | `JARAK km` (÷1000) | Jarak per span |
| `KUMULATIF` | meter | `KUMULATIF km` (÷1000) | Posisi kumulatif tower dari GI A; **dipakai untuk interpolasi fault** |
| `LATITUDE` | desimal atau koma | `lat` (numerik) | Koordinat lintang tower |
| `LONGITUDE` | desimal atau koma | `lon` (numerik) | Koordinat bujur tower |
| `SEGMENT` | — | — | Filter segmen; pre-fill dari sidebar |
| `UPT` | — | — | Nama Unit Pelaksana Transmisi; filter tampilan tower |
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

`Fault Context`, `Distance from Fault km`, `JARAK`, `KUMULATIF`, `JARAK km`, `KUMULATIF km`, `LATITUDE`, `LONGITUDE`, `SEGMENT`, `UPT`, `ULTG`

### Session State yang Diisi

| Key | Isi |
|---|---|
| `tower_schedule_df` | DataFrame penuh setelah load (sebelum filter tampilan) |
| `tower_schedule_filtered_df` | DataFrame setelah filter ULTG/Segment/Type String |
| `tower_schedule_selected_length_km` | Panjang saluran dari tower schedule (km) |
| `tower_schedule_selected_length_source` | Keterangan sumber panjang (`"max(KUMULATIF km)"` dst.) |
| `tower_schedule_selected_segment` | Segment yang aktif |
| `tower_schedule_selected_upt` | UPT yang aktif |
| `tower_schedule_selected_ultg` | ULTG yang aktif |

---

## 3. Upload End Filter — Session State Keys

Filter GI/line berada di sidebar, tetapi dikelompokkan di expander upload rekaman Local End dan Remote End. Segment hanya dipilih di Local End agar satu segment menjadi konteks line/tower, sementara UPT/ULTG local dan remote boleh berbeda.

| Key | Sumber Kolom | Sheet | Keterangan |
|---|---|---|---|
| `sidebar_filter_upt_local` | `UPT` | `distance_settings` | UPT Local End |
| `sidebar_filter_ultg_local` | `ULTG` | `distance_settings` | ULTG Local End, difilter UPT local |
| `sidebar_filter_segment` | `SEGMENT` | `tower_schedule` | Segment Local End, difilter memakai UPT/ULTG local |
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

Dirakit oleh `fault_cause_dataset.build_fault_cause_feature_row()` (48 kolom, `DATASET_COLUMNS`):

Selain tombol manual `Machine Learning > Dataset Penyebab > Tambah ke Sheet Penyebab`, baris ini juga di-upsert oleh tombol **Simpan Case ke Cloud** di sidebar dan Setup DB sebagai bagian dari general save. Nilai `confirmed_cause` mengikuti isian terakhir widget `dataset_confirmed_cause`; jika belum pernah diisi, default `Belum Diketahui`.

| Grup | Kolom |
|---|---|
| **Kunci unik** | `case_id` (kolom A — upsert key) |
| Metadata | `timestamp_analyzed`, `fault_time_cfg`, `line_name`, `gi_local`, `gi_remote`, `upt`, `ultg`, `upt_local`, `ultg_local`, `upt_remote`, `ultg_remote`, `segment` |
| Fault type | `fault_type`, `n_phases`, `ground`, `ft_confidence` |
| Komponen simetris | `I0_A`,`I1_A`,`I2_A`, `r_i2_i1`,`r_i0_i1`,`r_i0_i2`, `ang_i2_i1_deg`,`ang_i0_i1_deg`, `r_v2_v1`,`r_v0_v1`, `Z1_ohm`,`Z2_ohm`,`Z0_ohm` |
| Resistansi | `rf_est_ohm`, `hr_suspected` |
| Waktu | `hour`, `month` |
| Cuaca | `weather_code`, `weather_desc`, `rain_mm`, `humidity_pct` |
| Waveform | `di_dt_norm`, `hf_ratio`, `transient_sharp`, `duration_ms`, `cleared_in_record`, `reclose_in_record` |
| Lokasi | `se_distance_km`, `de_distance_km`, `de_quality` |
| Prediksi rule | `predicted_cause`, `predicted_score` |
| **Target (label)** | `confirmed_cause` (diisi user dari `CONFIRMED_CAUSE_LABELS` setelah inspeksi) |

Catatan prediksi rule: `predicted_cause`/`predicted_score` berasal dari `summary_helpers.estimate_summary_disturbance_cause()`. Skor kandidat dapat dipengaruhi **Evidence PANEN RISOL** (`R/X`, `X/R`, rasio `3I0/loop`, rasio `3V0/loop`, beda sudut loop) selain fitur komponen simetris, Rf/HR, waktu, cuaca, waveform, dan hasil SE/DE. Tidak ada kolom baru untuk PANEN RISOL; kontribusinya tercermin di `predicted_cause`, `predicted_score`, dan bukti kandidat pada Summary.

---

## Sheet: `fault_location` (ditulis aplikasi)

Default sheet name: `fault_location` (override via `fault_location_sheet_name` / credentials `fault_location_sheet`). Berada di **Database Spreadsheet**. Ditulis oleh tab `Machine Learning > Kalibrasi Lokasi` via Sheets API dan upsert by `case_id`.

Dataset ini menjadi fondasi ML kalibrasi lokasi gangguan. Target awal model adalah residual DE: `actual_distance_km - de_raw_km`.

Selain tombol manual `Machine Learning > Kalibrasi Lokasi > Tambah ke Sheet Lokasi`, baris ini juga di-upsert oleh tombol **Simpan Case ke Cloud** di sidebar dan Setup DB jika `two_ended_result` sudah tersedia. Bila Double-End belum dihitung, general save melewati `fault_location` dan tetap menyimpan case serta dataset penyebab.

| Grup | Kolom |
|---|---|
| Kunci unik | `case_id` |
| Metadata | `timestamp_analyzed`, `fault_time_cfg`, `line_name`, `gi_local`, `gi_remote`, `upt_local`, `ultg_local`, `upt_remote`, `ultg_remote`, `segment` |
| Fault type | `fault_type_local`, `fault_type_remote` |
| Line parameter | `line_length_km`, `line_length_source`, `z1_r_ohm_per_km`, `z1_x_ohm_per_km`, `z0_r_ohm_per_km`, `z0_x_ohm_per_km` |
| Mixed conductor | `mixed_conductor_used`, `mixed_conductor_sections` |
| Kalkulasi aplikasi | `se_local_km`, `se_remote_from_remote_km`, `se_remote_from_local_km`, `de_raw_km`, `de_raw_pct`, `de_quality`, `de_status` |
| Tower schedule | `tower_length_km`, `tower_length_source` |
| Label lapangan | `actual_distance_km`, `actual_distance_pct`, `de_calculated_tower`, `actual_tower_inspected`, `actual_source`, `field_notes` |
| Target ML | `de_error_km`, `de_abs_error_km`, `de_error_pct`, `ml_ready` |

---

## Sheet: `saved_cases` + `saved_cases_data` (ditulis & dibaca aplikasi)

Simpan/muat case via spreadsheet — **TANPA Google Drive** (service account akun personal tidak punya kuota Drive → `storageQuotaExceeded`). **Ditulis & dibaca** via Sheets API (service account). Upsert by `case_id` (kolom A). Di **Database Spreadsheet**. Override sheet name via `saved_cases_sheet_name`.

Tombol **Simpan Case ke Cloud** sekarang berperan sebagai general save: menulis `saved_cases`/`saved_cases_data`, lalu upsert `fault_cause`, dan upsert `fault_location` bila hasil Double-End sudah ada. Status tiap bagian ditampilkan terpisah agar kegagalan satu sheet mudah didiagnosis.

**`saved_cases`** = indeks ringkas (1 baris/case):

| Kolom | Isi |
|---|---|
| `case_id` | `sha1(line_name\|fault_time_cfg)[:16]` — kunci upsert |
| `case_name` | Nama case (slug line) |
| `line_name`, `gi_local`, `gi_remote` | Identitas saluran |
| `upt`, `ultg` | Legacy alias pilihan UPT/ULTG Local End |
| `upt_local`, `ultg_local` | Pilihan filter UPT/ULTG Local End saat case disimpan; dipakai sebagai fallback restore filter saat load dari spreadsheet |
| `upt_remote`, `ultg_remote` | Pilihan filter UPT/ULTG Remote End saat case disimpan |
| `segment` | Pilihan filter Segment Local End saat case disimpan |
| `fault_time_cfg` | Timestamp CFG (trigger/start) |
| `saved_at` | ISO timestamp saat disimpan (untuk urut daftar) |
| `filename` | Nama file ZIP internal |
| `size_bytes` | Ukuran ZIP |
| `n_chunks` | Jumlah chunk payload di `saved_cases_data` |

**`saved_cases_data`** = payload (1 baris/case, dibuat dgn ~200 kolom): `[case_id, chunk0, chunk1, ...]`. Payload = ZIP case → base64, dipecah ≤49000 char/sel (di bawah batas 50.000). Ditulis RAW (agar base64 tak jadi formula). Load: pilih dari `saved_cases` (urut `saved_at` desc) → cari baris by `case_id` di `saved_cases_data` → gabung sel chunk → base64 decode → `restore_case_archive`. Objek figure (Plotly) di-drop saat snapshot (dihitung ulang dari selection), jadi payload ramping.
