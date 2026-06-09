# PRD — Transmission Fault Locator

Dokumen ini adalah sumber kebenaran tunggal untuk spesifikasi fitur, perilaku aplikasi, kontrak UI/backend, dan arsitektur modul. Gunakan dokumen ini sebagai referensi sebelum melakukan perubahan apapun.

**Algoritma & rumus detail** (fault cursor, SE, DE, HR) ada di [`FORMULAS.md`](FORMULAS.md) — PRD merujuk ke sana, tidak menyalin ulang rumus.

**Jangan hapus atau ubah fitur di dokumen ini tanpa konfirmasi eksplisit dari user.**

---

## Tujuan Aplikasi

- Membaca rekaman gangguan COMTRADE local end dan optional remote end.
- Mengubah channel asli menjadi variabel standar `Va/Vb/Vc/Ia/Ib/Ic/IE`.
- Menentukan fault cursor, fault type, phasor DFT, high resistance indication, lokasi gangguan Single-End, lokasi gangguan Double-End, trajectory R-X, relay distance locus, tower schedule, dan report summary.
- Mendukung workflow kasus normal internal line fault, reverse/backfeed/external fault, serta rekaman remote yang butuh adaptasi polaritas/sudut/arah arus.

---

## Navigasi Utama

- `Summary`
- `Setup DB`
- `Tower Schedule`
- `Case Storage` berada di dalam `Setup DB`; restore case ZIP berada di sidebar.
- `Local End`
- `Remote End`
- `Line`
- `HR Check`
- `Single-End`
- `Double-End`
- `R-X Locus`
- `Machine Learning`

`Tower Schedule` hanya tampil setelah pasangan rekaman GI lokal lengkap (`.cfg` + `.dat`). Jika belum lengkap, layar awal hanya menampilkan Summary ringkas.

---

## Arsitektur Modul

### Entry Point

`app.py` tetap menjadi entry point Streamlit. Mengatur:
- `st.set_page_config`
- CSS global dan print table styling
- Sidebar upload COMTRADE local/remote dan restore case ZIP
- Pembacaan COMTRADE local sebelum tab utama ditampilkan
- Pembuatan dan orkestrasi tab utama

### Modul Pendukung

- **`app_helpers.py`** — Helper umum lintas fitur: downsampling plot, validasi ekstensi upload, normalisasi kolom DataFrame untuk Streamlit, pembalikan phasor arus.
- **`app_runtime.py`** — Cache wrapper untuk COMTRADE dan Google Spreadsheet, query Tower Schedule via Google Visualization CSV, monkey-patch print-friendly `st.dataframe`.
- **`case_storage.py`** — Runtime credentials, restore/save case ZIP. Menyaring key sensitif dan bytes file mentah agar tidak masuk `case_state.json`. Mendefinisikan `CASE_SETTINGS_KEYS` (kunci konfigurasi yang selalu disimpan) dan `_CASE_SETTINGS_WIDGET_FALLBACK` (sync widget key saat restore).
- **`weather_services.py`** — API OpenWeather, Xweather, AccuWeather, fallback Open-Meteo. Formatter angka/deskripsi cuaca dan builder DataFrame.
- **`weather_ui.py`** — Rendering HTML kartu cuaca: icon/theme, tren suhu, bar peluang hujan, `weather_card_html()`. `app.py` hanya memanggil HTML yang sudah dibangun modul ini.
- **`tower_map.py`** — Normalisasi koordinat tower, interpolasi lokasi fault pada jalur tower, tabel tower sekitar fault, link Google Maps, `render_tower_map()`. Membaca `st.session_state` untuk pilihan sumber fault.
- **`rx_locus.py`** — Parsing distance relay settings dari `line_data` (utama, kolom Prim/Sec eksplisit) atau `distance_settings` (fallback), ekstraksi zone reach, overlay zona proteksi, builder trajectory R-X dari waveform/phasor. Flow widget dan penyimpanan summary R-X masih di `app.py`.
- **`line_analysis_helpers.py`** — Infer nama GI dari nama line, reverse line name, status operasi DE/backfeed, pemilihan DFT remote terbaik, reverse-result DE, comparison dataframe, override panjang line. Widget pemilihan sumber panjang tetap di `app.py`.
- **`waveform_helpers.py`** — Plot assigned waveform, fault-window plot, sync local/remote plot, estimasi time shift waveform, diagram phasor, tabel perbandingan prefault/fault. UI tab tetap di `app.py`.
- **`single_ended.py`** — Kalkulasi SE murni: loop impedansi per fault type, reactance/magnitude/projection method, Takagi fallback (kompensasi Rf via incremental phasor).
- **`two_ended.py`** — Kalkulasi DE murni: positive-sequence two-ended closed-form, quality scoring, candidate ranking, angle search untuk unsynchronized; menyimpan V1L/V1R/I1L/I1R di result dict.
- **`fault_workflow_helpers.py`** — Explanation text, tabel threshold fault type otomatis, parser timestamp COMTRADE, TWS time-based location, parameter auto fault detection; `render_se_formula_expander()` untuk display rumus SE + nilai aktual + referensi literatur inline.
- **`summary_helpers.py`** — Pemilihan sinyal fault utama, waveform fokus Summary, estimasi penyebab gangguan (candidate-scoring multi-fitur), scoring single-ended, grafik posisi SE/DE, `build_cause_table_html()`. Fungsi yang membaca `st.session_state` langsung tetap di `app.py`.
- **`waveform_signatures.py`** — Tanda waveform penyebab gangguan dari raw COMTRADE: transien/HF (`di_dt_norm`, `hf_ratio`, `transient_sharp`), durasi gangguan, clear/reclose. `compute_waveform_signatures()`.
- **`fault_cause_dataset.py`** — Dataset berlabel penyebab (jembatan rule→ML): `build_fault_cause_feature_row()` (48 kolom, kunci `case_id`), upsert ke sheet `fault_cause` via Sheets API. Helper generik `upsert_row_to_gsheet()`/`read_sheet_records()` (dipakai juga `cloud_cases`).
- **`fault_location_dataset.py`** — Dataset kalibrasi lokasi gangguan untuk ML residual DE: hasil SE/DE, parameter line, mixed conductor, Tower Schedule, dan lokasi aktual lapangan ke sheet `fault_location`.
- **`cloud_cases.py`** — Simpan/muat case via spreadsheet (payload ZIP base64 chunked ke `saved_cases_data`, indeks ke `saved_cases`; tanpa Drive). `save_case_to_cloud()`, `list_saved_cases()`, `load_case_from_cloud()`.
- **`tabs/`** — Modul render per-tab, masing-masing mengekspos `render(...)` yang dipanggil `app.py`:
  - `tabs/line_parameter.py` — Tab `Line`. Signature: `render()`.
  - `tabs/double_ended.py` — Tab `Double-End`. Signature: `render()`; `render_de_formula_expander()` untuk display rumus DE + nilai aktual + referensi literatur inline.
  - `tabs/signal_assignment.py` — Sub-tab `Signals` di `Local End`. Signature: `render(df)`.

### Runtime Flow

1. `app.py` memuat import, constant, cache wrapper, dan helper render.
2. `st.set_page_config` dijalankan.
3. Sidebar meminta upload: Local `.cfg`, Local `.dat`, Remote `.cfg` (opsional), Remote `.dat` (opsional), Load Case `.zip`. Filter GI/line berada di expander upload masing-masing end.
4. Jika user memilih Load Case `.zip`, `case_storage.restore_case_archive()` memulihkan state dan file, lalu aplikasi rerun.
5. Jika sidebar kosong tapi case restore punya file tersimpan, `case_storage.get_restored_upload()` membuat object upload pengganti.
6. Aplikasi validasi ekstensi local `.cfg` dan `.dat` via `app_helpers.validate_uploaded_extension()`.
7. Jika local belum lengkap, hanya Summary ringkas yang ditampilkan.
8. Jika local lengkap, COMTRADE dibaca dengan `read_comtrade_cached()`.
9. Auto signal assignment local dihitung dan disimpan di `st.session_state`.
10. Tab utama dibuat: Summary → Setup DB → Tower Schedule → Local End → Remote End → Line → HR Check → Single-End → Double-End → R-X Locus → Machine Learning.

### Flow Setup DB dan Case Storage

1. Setup DB membaca default config dari: `st.secrets` → environment variable → runtime credentials upload → input manual user.
2. Runtime credentials diparse oleh `case_storage.parse_runtime_credentials_upload()`.
3. Nilai credentials diterapkan ke `st.session_state` oleh `case_storage.apply_runtime_credentials()`.
4. Case ZIP dibuat oleh `case_storage.build_case_archive_bytes()`.
5. Case ZIP dapat di-download via tombol `Export Case ZIP` di Setup DB.

### Prinsip Refactor

- Pindahkan satu kelompok fungsi yang kohesif setiap tahap.
- Jangan ubah perilaku UI/kalkulasi bersamaan dengan pemindahan modul.
- Setelah setiap tahap jalankan `py_compile` seluruh modul (lihat CLAUDE.md).
- Jika modul baru dibuat, tambahkan catatan di dokumen ini.

---

## Data Input

- Local COMTRADE wajib: `.cfg` dan `.dat`.
- Remote COMTRADE opsional: dipakai untuk Double-End, remote HR, remote SE, remote R-X locus, dan perbandingan summary.
- Sidebar menerima `Load Case (.zip)` untuk memulihkan rekaman, parameter user, dan hasil kalkulasi.
- Filter upload Local End: UPT/ULTG dari `distance_settings`, Segment dari `tower_schedule` (difilter memakai UPT/ULTG lokal), GI dan Bay/Line dari `distance_settings`.
- Auto-pick `line_impedance` pada tab Line Parameter memakai pilihan filter Local End: `GI` + `BAY` + `LINE`. `SEGMENT` sidebar dipakai untuk konteks tower/line, bukan lagi sebagai kunci pemilihan otomatis impedansi saluran.
- Filter upload Remote End: UPT/ULTG dari `distance_settings`, GI dan Bay/Line dari `distance_settings`; remote tidak memilih Segment sendiri.
- Segment hanya dipilih di Local End agar satu segment/line menjadi konteks line/tower, tetapi UPT/ULTG local dan remote boleh berbeda untuk kasus GI local dan GI remote berada di UPT/ULTG berbeda. Legacy session key `sidebar_filter_upt` dan `sidebar_filter_ultg` tetap diisi dari pilihan Local End.
- Dropdown filter upload end hanya muncul jika Database Spreadsheet URL tersedia dari credentials, secret/env, atau input Setup DB. Jika belum tersedia, sidebar upload hanya menampilkan uploader rekaman.
- Database spreadsheet utama: line parameter dan distance relay settings.
- Spreadsheet tower schedule terpisah: data tower, panjang line alternatif, map, dan fault location map.
- Database Spreadsheet conductor/line impedance: sumber parameter konduktor/line opsional.

---

## COMTRADE Reader

- Membaca CFG/DAT via `comtrade_reader.read_comtrade`.
- Metadata yang dipakai: station name, frequency, total samples, analog channel metadata, timestamp start/trigger CFG, rasio CT/VT jika tersedia.
- Memiliki fallback untuk variasi format COMTRADE, normalisasi file type CFG, timestamp, dan parsing ratio channel.

---

## Signal Assignment

- Auto assignment via `auto_assignment.detect_voltage_current_channels`.
- Pemilihan manual tersedia untuk `Va`, `Vb`, `Vc`, `Ia`, `Ib`, `Ic`, `IE/IN/3I0`.
- Jika `IE` tidak dipilih: `IE = Ia + Ib + Ic`, `I0 = IE / 3`.
- Recorded side:
  - `secondary`: waveform dikalikan rasio CT/VT ke satuan primer.
  - `primary`: waveform dianggap sudah primer; rasio CT/VT tetap disimpan untuk dokumentasi dan locus secondary conversion.
- **Koreksi Polaritas** — dua checkbox per end (Local & Remote):
  - `invert_voltage`: kalikan Va/Vb/Vc dengan −1 setelah rasio VT. Digunakan bila VT terpasang terbalik di COMTRADE (gejala: Visual Sync Score DE ≈ −1).
  - `invert_current`: kalikan Ia/Ib/Ic/IE dengan −1 setelah rasio CT. Digunakan bila CT terpasang terbalik (gejala: lokasi SE/DE negatif atau >100%).
  - Implementasi: `apply_signal_assignment(..., invert_voltage, invert_current)` di `signal_assignment.py`.
- Transformer data disimpan untuk local dan remote: `ct_primary`, `ct_secondary`, `vt_primary`, `vt_secondary`, `invert_voltage`, `invert_current`, nominal phase voltage RMS, nominal current RMS.
- CT/VT ratio **tidak lagi** dibaca dari spreadsheet `line_impedance` — diinput langsung di Signal Assignment.
- Validasi duplikasi channel wajib: `Va/Vb/Vc/Ia/Ib/Ic` tidak boleh memakai channel yang sama lebih dari satu kali.

---

## Fault Cursor

- Deteksi fault inception via `fault_detection.detect_fault_inception`.
- **Default checkbox deteksi otomatis adaptif: off** untuk local dan remote.
- Window fault via `build_fault_window`: left cursor = beberapa siklus sebelum fault, right cursor = beberapa siklus setelah fault, DFT cursor = 1 siklus setelah fault inception.
- Metode deteksi: RMS sliding 1 siklus, kenaikan RMS arus, penurunan RMS tegangan, optional superimposed detection, optional refine fault bar.
- Auto threshold memperhatikan prefault RMS, nominal jika tersedia, kondisi prefault voltage rendah atau current tinggi.
- **Fault inception** dipakai untuk sinkronisasi visual/record. **DFT cursor** dipakai untuk phasor dan locus fault point. Jangan pertukarkan kedua peran ini.
- Expander **"Dasar Penentuan Fault Cursor"** (`render_fault_cursor_explanation`) muncul di bawah plot fault window (Local End, Remote End, dan DE) berisi tabel: Hasil Deteksi (waktu inception, confidence, metode, DFT cursor, fault bar refinement), Referensi Pre-fault & Threshold Pickup (arus/tegangan aktual, referensi dipakai, pickup ×2.0/×0.85), tabel Superimposed bila hybrid aktif, langkah penentuan bernomor, dan referensi literatur (Saha 2010 Sec. 2.3–2.5; IEEE C37.114-2014 Sec. 5.2–5.3; Phadke & Thorp 2009 Sec. 3.2 & 9.2; Eriksson dkk 1985 Sec. II).
- **Sinkronisasi pengaturan fault cursor Local/Remote End ↔ DE:** di halaman DE, fault cursor compact membaca pengaturan dari halaman Local/Remote End (`settings_source_prefix`). Checkbox "deteksi otomatis" dapat diatur di kedua halaman dan **sinkron dua arah**. `fault_window`/`remote_fault_window` adalah key session_state bersama sehingga hasil selalu konsisten.

---

## Phasor

- Full-cycle DFT pada window DFT cursor.
- `phasor.calculate_all_phasors` menghitung: phasor fundamental tiap phase, residual/zero sequence, sequence components `V0/V1/V2` dan `I0/I1/I2`.
- Sequence component memakai operator `a = 1∠120°`.
- Phasor disimpan terpisah untuk fault dan prefault.

---

## Fault Type

- Via `fault_type.detect_fault_type`.
- Input: magnitude `Va/Vb/Vc/Ia/Ib/Ic/IE/I0`, optional prefault phasor, threshold current rise/voltage drop/ground current/delta current/delta voltage.
- Fasa terganggu dari gabungan: arus tinggi relatif terhadap minimum, tegangan drop relatif terhadap maksimum, delta current/voltage dari prefault.
- Ground involvement dari: rasio `IE` terhadap arus maksimum, rasio `I0` terhadap arus rata-rata, kenaikan `IE/I0` dari prefault.
- Klasifikasi: `AG/BG/CG`, `AB/BC/CA`, `ABG/BCG/CAG`, `ABC`, `ABCG`, `UNKNOWN`, `A?/B?/C?`.
- Confidence 0–10 dari kejelasan fault type, ground ratio, balance current/voltage, jumlah fasa terganggu.

---

## Line Parameter

- Dibaca dari spreadsheet utama.
- `line_param` berisi minimal: `line_name`, `length_km`, `Z1_per_km`, `Z0_per_km`, `Z1_total`, `Z0_total`, `K0`.
- Konversi panjang via `convert_length_to_km` (meter/kilometer/mile).
- Impedansi dapat dibangun dari: R/X, magnitude/angle, X dan phi, primary/secondary dengan konversi CT/VT.
- Jika sumber `Database Spreadsheet Cable Data` dipilih, user dapat mengaktifkan komposisi beberapa jenis konduktor per section. Aplikasi menghitung `Z1_per_km` dan `Z0_per_km` ekuivalen sebagai rata-rata berbobot panjang section: `sum(Z_i * panjang_i) / sum(panjang_i)`. Ini dipakai untuk meningkatkan akurasi SE/DE pada jalur transmisi dengan kombinasi tipe konduktor.
- Nama GI local dan remote diinfer dari `line_name`; jika tidak sesuai, user harus memperbaiki line parameter.
- **Sumber panjang line untuk kalkulasi:** selector global ada di tab Line (sebelum Normalize). Pilihan: `line_parameter` atau `tower_schedule`. Hasil disimpan ke `st.session_state["effective_line_param"]`.
- `effective_line_param` adalah dict identik `line_param` kecuali `length_km`, `Z1_total`, `Z0_total` yang sudah dioverride sesuai sumber yang dipilih.
- SE, DE, dan HR Check **selalu membaca dari `effective_line_param`**, bukan langsung dari `line_param`. Jika `effective_line_param` belum ada, fallback ke `line_param`.
- Perubahan selector sumber panjang **tidak langsung menghitung** — baru dihitung saat Normalize diklik, lalu `st.rerun(scope="app")` memperbarui semua tab.

---

## Tower Schedule

- Tidak ada URL default yang di-hardcode (repo public). URL diisi dari runtime credentials, Streamlit secrets, env var, atau input manual Setup DB.
- Sheet default: `tower_schedule`.
- Kolom utama: `SPAN`, `JARAK`, `KUMULATIF`, `LATITUDE`, `LONGITUDE`, `SEGMENT`, `UPT`, `ULTG`, `TYPE STRING`, `JUMLAH STRING`.
- Kolom tambahan spreadsheet harus tetap dipertahankan (cleaning, proteksi petir, DGS, MGGS, TLA/NGLA, EGLA, sumur bor, MDG, DMRG, MRG, DG, dinding penahan, kerawanan binatang, dll.).
- `JARAK` dan `KUMULATIF` dari spreadsheet dianggap meter. Aplikasi menambahkan `JARAK km` dan `KUMULATIF km`.
- Tampilan km: 6 desimal pada tabel utama (berpengaruh ke kalkulasi DE/SE).
- Panjang line dari tower schedule: prioritas `max(KUMULATIF km)`, fallback `sum(JARAK km)`, disimpan ke `tower_schedule_selected_length_km`.
- Filter awal load: fokus pada `Segment` saja (prefill dari filter upload Local End); tidak ada filter awal ULTG agar satu segment tetap dapat memuat tower dengan UPT/ULTG berbeda. Opsi `Load semua data` tersedia tapi tidak default. Segment matching adaptif terhadap variasi tanda hubung seperti `GNTUA-SBHAN` dan `GNTUA - SBHAN`.
- Filter setelah load: Segment, UPT, ULTG, Type String, pencarian span/teks.

---

## Tower Map

- Memakai Folium/streamlit-folium. Default tile: Esri World Imagery/satellite. Alternatif: OpenStreetMap/street.
- Layer: Tower, Fault Location, Tower path/polyline.
- Kontrol peta dalam expander `Map Settings`: default tertutup di Summary/report, default terbuka di Tower Schedule/exploration.
- Kontrol layer bawaan Leaflet/Folium disembunyikan; pilihan layer dikendalikan oleh kontrol Streamlit.
- Marker tower: size 10, label ringkas dari kolom `SPAN` (contoh: `#0164`), nama lengkap di hover/popup.
- Popup tower: SPAN, JARAK, KUMULATIF, SEGMENT, UPT, ULTG, TYPE STRING, JUMLAH STRING, LATITUDE/LONGITUDE, link `Open Maps` dan `Directions`.
- Fault location source: default DE jika tersedia, fallback SE local. SE remote dikonversi ke `line_length - remote_distance`.
- Fault interpolation: memakai `KUMULATIF km`, mencari dua tower pengapit, koordinat dihitung dengan interpolasi linear latitude/longitude. Jika fault di luar range data, marker di ujung dan warning muncul.
- Marker fault: crosshair presisi, span pengapit di-highlight merah, label permanen menampilkan sumber/jarak/rasio span, label diposisikan adaptif menjauh dari arah span pengapit.
- Popup fault: sumber kalkulasi, distance, plotted distance, tower pengapit, jarak dari/ke tower A/B, tower terdekat, jarak ke tower terdekat, panjang span, rasio span, quality/status, lat/lon, link Maps fault dan tower terdekat.
- Summary Tower Map fokus otomatis ke dua tower pengapit dan titik fault, bukan seluruh jalur.
- Tabel `Data tower sekitar titik gangguan (-5 / +5)` di bawah Tower Map: 5 tower sebelum dan sesudah span fault. Ditampilkan sebagai tabel HTML dengan kolom: No, SPAN, TYPE STRING, JUMLAH STRING, dan **Proteksi Terpasang**.
  - Kolom Proteksi Terpasang menampilkan badge berwarna per kategori: Cleaning (hijau), Proteksi Petir — termasuk DGS/MGGS/TLA/NGLA/EGLA/Sumur Bor/MDG/MRG/DG/DMRG (kuning), Dinding Penahan Tanah (coklat), Kerawanan Binatang (merah), Proteksi Binatang (ungu).
  - Badge induk (misal "Proteksi Petir") hanya muncul jika tidak ada satu pun sub-device yang terisi.
  - Badge menampilkan tanggal pemasangan jika tersedia di spreadsheet.
  - Baris `Before fault span` / `After fault span` ditandai dengan background merah muda; `Closest tower` dengan kuning.
  - Kolom Fault Context, Distance from Fault km, JARAK, KUMULATIF, LATITUDE, LONGITUDE, SEGMENT, UPT, ULTG disembunyikan dari tabel (tetap ada di DataFrame backend).
- Cuaca terkini di titik gangguan ditampilkan di bawah Tower Map (lihat bagian Weather).

---

## High Resistance Check

- Sub-view local dan remote. Judul end memakai nama GI/lokasi.
- Memakai `effective_line_param` (sumber panjang line dari tab Line) via `resolve_end_analysis_context` — konsisten dengan SE/DE/R-X Locus.
- Loop impedance per fault type (ground loop, phase loop, 3-phase fallback), tiga metode jarak (magnitude/reactance/projection), dan estimasi Rf — **rumus di [`FORMULAS.md`](FORMULAS.md) Sec. 4** (loop & jarak identik SE Sec. 2.1–2.2).
- Indikator HR: Rf_est ≥ threshold, deviasi sudut Zapp vs Z1, deviasi distance magnitude vs reactance, distance keluar line. Nilai threshold default → FORMULAS.md Sec. 4.
- Confidence 0–10 dan evidence score ditampilkan.
- Simbol ohm harus tampil sebagai `Ω`, bukan karakter rusak.
- Formula expander `render_hr_formula_expander()` menampilkan: loop impedansi, Zapp, tiga metode jarak, estimasi Rf, deviasi sudut, dan logika deteksi HR dengan nilai aktual inline.

---

## Single-End Fault Locator

- Sub-view local dan remote.
- Input: phasor fault, prefault phasor jika tersedia, fault type, `effective_line_param`.
- **Sumber panjang line tidak dipilih di halaman SE** — selalu memakai `effective_line_param` yang ditetapkan di tab Line (via `resolve_end_analysis_context`). Halaman SE hanya menampilkan caption panjang line aktif + arahan ke tab Line.
- Loop impedance per fault type + tiga metode jarak (magnitude/reactance/projection). **Recommended default: reactance.** Rumus → [`FORMULAS.md`](FORMULAS.md) Sec. 2.1–2.2.
- Fault context: internal line fault atau reverse/backfeed external fault.
- Mode reverse/backfeed: signed distance dipertahankan; jarak negatif atau > line length tidak langsung salah.
- Takagi fallback: untuk ground fault (SLG) bila prefault tersedia, mengeliminasi Rf secara eksak; menggantikan recommended distance jika konvensional out-of-range dan hasil Takagi masuk range. Rumus → FORMULAS.md Sec. 2.4 (Saha 2010 Eq. 6.8).
- Status: `VALID`, `CHECK`, `UNCERTAIN`.
- Warning: jarak negatif, jarak melebihi line, magnitude vs reactance berbeda signifikan, Rf tinggi, sudut Zapp menyimpang, indikasi load-flow/backfeed.
- Hasil disimpan: `single_ended_result`, `remote_single_ended_result`, dataframe detail masing-masing.

---

## Double-End Fault Locator

- Remote setup berada di tab `Remote End`, bukan di halaman DE.
- Input: local positive sequence phasor `V1/I1`, remote `V1/I1`, `effective_line_param`, remote record adaptation, scenario gangguan.
- **Sumber panjang line tidak dipilih di halaman DE** — selalu memakai `effective_line_param` dari tab Line. Halaman DE hanya menampilkan caption panjang line aktif + arahan ke tab Line.
- Metode: positive-sequence closed-form (local x=0, remote x=L). Jika remote current direction `opposite_to_line`, `I1R` diinversi. **Persamaan lengkap → [`FORMULAS.md`](FORMULAS.md) Sec. 3.1.**
- Output utama: distance complex, distance km dari local, distance percent, distance dari remote, voltage fault dari local/remote, mismatch tegangan fault, quality score.
- Quality score: penalti distance negatif/> line length/imaginary, penalti mismatch tegangan, dikunci 0–10. Rincian penalti → FORMULAS.md Sec. 3.3.
- Remote adaptation: `auto_adapt_record`, `auto_current_direction_only`, manual `into_line`, manual `opposite_to_line`.
- Candidate ranking: distance keluar line, imaginary distance, mismatch ratio, quality score, penalti angle shift, penalti polaritas/arah tertentu.
- Visual sync: **referensi default `fault_phase_voltage` (jika tersedia, fallback `fault_cursor`)**, **metode default raw waveform correlation**, opsi sinkronisasi fault cursor/time/visual. Fault inception untuk alignment, DFT cursor untuk kalkulasi phasor.
- Grafik sync waveform: default menampilkan **tegangan dan arus fasa terganggu** sekaligus. Tegangan di subplot atas (Y: Tegangan Primary), arus di subplot bawah (Y: Arus Primary), X axis shared. `build_synchronized_fault_plot` mendukung `current_channels` parameter untuk layout dual subplot.
- **Visual Sync Quality** ditampilkan setelah grafik sync: 5 metrik (DE Remote DFT Time, DE Remote DFT Index, Waveform Sync Score, Visual Sync Score, Sync Status). Visual Sync Score = Pearson correlation instantaneous waveform tegangan fasa terganggu di 2 siklus sekitar DFT cursor setelah alignment. Threshold: ≥0.85 Sinkron, 0.50–0.85 Cukup Sinkron, <0.50 Kurang Sinkron, <0 Terbalik/Tidak Sinkron.
- Optional TWS/time-based: estimasi jarak dari selisih waktu kedatangan gelombang, warning bila delta time/distance tidak realistis (rumus → FORMULAS.md jika diimplementasi penuh).
- Scenario: internal line fault atau reverse/backfeed/external fault. SOTF/parallel/adjacent line diperlakukan sebagai konteks reverse/backfeed, bukan label wajib.
- Perbandingan SE pada halaman DE memakai `effective_line_param` yang sama.
- **Status Diagnostik DE** ditampilkan dengan label bahasa Indonesia berbasis teks ASCII (`[OK]`, `[PERHATIAN]`, `[TIDAK BERLAKU]`) agar aman dari mojibake; jangan tampilkan kode mentah seperti `NORMAL_INTERNAL_LINE_FAULT`. Catatan kondisi ada di expander "Detail kondisi yang terdeteksi"; rekomendasi sebagai `st.info`.
- **Warning DE** ditulis dengan pola apa-yang-terjadi → mengapa → tindakan (disimpan di sumber `two_ended.py` agar konsisten di DE dan Summary).
- **Line Position Visualization** (Grafik SE dan DE, juga di Summary): label annotation **draggable** (Plotly `config editable`, tanpa teks "Click to enter"); label & hover menampilkan jarak dari **kedua GI** (lokal + remote); semua marker **filled** (distinksi lokal/remote lewat warna). **Tidak ada auto-placement label** — overlap diatasi dengan drag manual. Nama file saat tombol kamera (download) ditekan: `porlungplot_{nama_line}_{YYYYMMDD}_{HHMMSS}` via `toImageButtonOptions.filename` (`app_helpers.plotly_image_filename()`).
- Hasil disimpan: `two_ended_result`, `two_ended_quality`, `two_ended_reverse_result`, `two_ended_reverse_quality`, `two_ended_comparison_df`, local/remote SE comparison result.

---

## R-X Locus

- Sub-view local dan remote.
- Membaca distance relay setting dari sheet `line_data` secara default; `distance_settings` tetap tersedia sebagai fallback/manual source.
- Filter relay setting: GI/Substation, Bay, search text.
- **Selector "Pilih setting relay distance" default placeholder** (`— Pilih setting relay distance —`) — tidak auto-pick baris pertama (rawan salah GI).
- **Sinkronisasi dari filter upload end (authoritative):** bila filter GI/Bay/Line di expander upload Local/Remote aktif, GI/Substation + Bay + baris relay di halaman locus **otomatis terpilih** mengikuti filter end terkait (set tiap run sebelum widget). Pencocokan baris relay memakai kolom LINE dengan normalisasi numerik (`"1.0"`=`"1"`). Bila filter masih placeholder, halaman locus pakai default sendiri + bisa dipilih manual.
- Zone setting base: **default primary ohm**. Jika sumber `line_data`, kolom `Z1/Z2/Z3 Prim` + `R* Prim` dipakai untuk primary, dan kolom `Z1/Z2/Z3 Sec` + `R* Sec` dipakai untuk secondary. Jika sumber `distance_settings`, base dipilih manual karena satuan sheet tidak selalu eksplisit.
- Parameter zona: `Z1/Z2/Z3 Res Ph`, `Z1/Z2/Z3 Res Gnd`, kN dan kN angle jika tersedia.
- Zona quadrilateral: X reach dan R reach/resistive reach, phase/gnd reach dipilih sesuai loop fault.
- Trajectory: apparent impedance dari waveform sepanjang window, titik DFT cursor ditandai, Z Line Total sebagai referensi.
- Plot focus: default fokus ke relay zones; dapat menampilkan trajectory penuh bila user pilih.
- Summary menampilkan R-X Locus local dan remote sebagai section terpisah agar print tidak menumpuk. Cache figure Summary (`_summary_rx_cache`/`_rx_key`) menyertakan key pilihan zona (source, setting row, substation, bay, show_zone, zone_setting_base) agar ikut update saat relay setting dipilih di halaman Locus.

### Guardrail R-X Locus dan Literatur

- **Pemisahan sumber sheet:** `database_line_sheet` / `line_data_sheet_name` dipakai oleh tab Line Parameter dan boleh menunjuk `line_impedance`. R-X Locus memakai key terpisah `rx_locus_line_data_sheet` / `rx_locus_line_data_sheet_name` dengan default `line_data`. Jangan mengembalikan R-X Locus agar membaca `line_data_sheet_name`, karena itu membuat Line Parameter dan zona relay saling tarik-menarik.
- **Struktur `line_data` aktif:** `No`, `UPT`, `Tegangan`, `ULTG`, `GI`, `Nama Line`, `Nomor Line`, `SEGMENT`, `Panjang (km)`, `Jenis Konduktor`, `Jumlah Sirkit`, `MERK`, `VT Ratio primary`, `VT Ratio Secondary`, `CT Ratio Primary`, `CT Ratio Secondary`, `Z1/Z2/Z3 Sec`, `R*P/R*G Sec`, `Line Impedance`, `VTR/CTR`, `Z1/Z2/Z3 Prim`, `R*P/R*G Prim`, `Z Line Prim`, `R Load Prim`, `Real/ABS`.
- **Restore/filter:** sidebar Local/Remote End adalah sumber kebenaran saat filter aktif. `GI` di sidebar harus memilih `GI/Substation` R-X, `Bay` di sidebar harus memilih `Nama Line`/Bay R-X, dan `Line` di sidebar harus memilih baris relay melalui `Nomor Line`. Format lama `Nama Line dan Nomor Line` tetap fallback, tetapi bukan struktur utama.
- **Base setting:** sumber `line_data` harus memilih kolom `Prim` saat base `primary` dan kolom `Sec` saat base `secondary`; source `distance_settings` tetap fallback karena satuannya tidak selalu eksplisit.
- **Trajectory:** apparent loop impedance dihitung dari fasor sliding DFT (`calculate_locus_loop_impedance`), bukan dari fault inception mentah. Fault inception untuk sinkronisasi/trigger, DFT cursor untuk titik phasor/locus.
- **Zona:** overlay adalah visualisasi engineering quadrilateral/polygonal berbasis `X reach` dan `R reach`. Untuk loop ground pakai `R*G`, untuk phase loop pakai `R*P`. Jangan klaim sebagai replica penuh relay vendor sampai ada model tilt reactance, directional supervision, left/right blinder detail, load encroachment, memory/polarizing quantity, dan logic pabrikan.
- **Catatan literatur:** setelah gambar locus harus ada expander `Catatan literatur R-X Locus dan zona distance` yang menjelaskan kesesuaian dengan R-X diagram/apparent impedance serta keterbatasan model overlay. Referensi lokal diambil dari `literature/distance_zone/*.pages.md`.
- **Literatur distance_zone:** PDF di `literature/distance_zone/` sudah dikonversi ke `.md` dengan MarkItDown dan memiliki sidecar `*.pages.md` per halaman. Gunakan `.md` untuk pencarian konsep dan `*.pages.md` untuk membuka halaman PDF relevan.

---

## Weather Summary

### Backend

- Koordinat cuaca dari titik gangguan hasil interpolasi Tower Schedule.
- Default sumber fault: Tower Map Summary (DE jika tersedia).
- OpenWeather One Call 4.0: sumber utama current weather dan forecast. Open-Meteo: fallback untuk cuaca saat ini bila OpenWeather gagal.
- Forecast OpenWeather dari timeline 15 menit, diagregasi ke bucket per 1 jam relatif terhadap waktu akses.
- Tiap bucket forecast menyimpan: waktu label, temperatur rata-rata, peluang hujan maksimum, presipitasi total, weather code/deskripsi dominan.
- Ringkasan hujan memakai probabilitas/akumulasi, bukan data petir.
- Jangan request histori thunderstorm/petir jika tidak ditampilkan.
- OpenWeather API key dibaca dari: `st.session_state["openweather_lightning_api_key"]` → widget → `st.secrets["OPENWEATHER_API_KEY"]` → env var `OPENWEATHER_API_KEY`. Input kosong tidak boleh menimpa key yang sudah tersimpan.

### UI Contract

- Judul section: `Cuaca Terkini`.
- Caption menjelaskan bahwa data adalah cuaca dari OpenWeather, bukan data sambaran petir.
- Pengaturan cuaca dalam expander tertutup.
- Satu card untuk titik gangguan, bukan dua card tower.
- Layout desktop: panel kiri (kondisi saat ini) + panel kanan (tren, forecast). Layout mobile: stack vertikal, tidak ada scroll internal.
- Panel kiri wajib: lokasi fault + span pengapit, timestamp cuaca, simbol cuaca, deskripsi bahasa Indonesia, temperatur `°C`, terasa seperti, hujan saat ini `mm`, angin `km/h`, kelembapan `%`, tutupan awan `%`, kumulatif fault `km`.
- Panel kanan wajib: tren suhu `°C`, peluang hujan `%`, ringkasan titik gangguan, peluang hujan tertinggi, perkiraan hujan total, sub-card forecast per 1 jam, footer koordinat + sumber API.
- Grafik tren: titik/batang vertikal sederhana tanpa garis penghubung; grafik hujan: bar sederhana. Tidak boleh terpotong/clipping.
- Simbol/status cuaca memakai label teks ASCII (mis. `Cloud`, `Storm`, `Rain`), bukan emoji mentah atau karakter simbol yang rawan encoding mojibake.
- Terjemahan deskripsi cuaca: `Broken Clouds` → `Berawan`, `Scattered Clouds` → `Berawan sebagian`, `Overcast Clouds` → `Mendung`, `Mainly Clear` → `Umumnya cerah`, `Clear Sky` → `Cerah`, `Light Rain` → `Hujan ringan`.
- Teks ringkasan hujan: `Tidak ada indikasi hujan dalam 12 jam ke depan.` / `Ada peluang hujan mulai sekitar HH:MM.` — jangan gunakan `hujan kuat/lebat` tanpa klasifikasi intensitas.
- Jangan tampilkan widget atau label petir/badai tanpa provider lightning aktual.
- Kartu print-friendly; jika API gagal, tampilkan pesan gagal tanpa menghentikan Summary.

---

## Summary

- Tampil setelah COMTRADE lokal berhasil dibaca.
- Jika kalkulasi belum lengkap, tampilkan `Pending`, bukan halaman blank.
- Konten: metadata local/remote, status Signal Assignment/Fault Cursor/Phasor/Fault Type/Line Parameter/SE/DE, Key Results, Status Diagnostik DE, IE source local/remote, perbandingan prefault/fault, waveform fokus opsional, estimasi penyebab gangguan, grafik SE/DE, Tower Map Fault Location, cuaca terkini + forecast, R-X Locus local/remote, warning kualitas DE/HR.
- **Key Results** disusun 2 baris: (1) Fault Type GI lokal + Fault Type GI remote (mengakomodir fasa terganggu berbeda antar ujung) + Prediksi Penyebab (ringkas); (2) SE dari GI lokal, SE dari GI remote (jarak asli dari masing-masing GI), DE dari GI lokal, DE dari GI remote — semua dengan persen. DE Quality dan Status DE tidak lagi di Key Results (ada di Status Diagnostik DE).
- **Estimasi Penyebab Gangguan otomatis** (tanpa selectbox manual): `estimate_summary_disturbance_cause` memakai **candidate-scoring multi-fitur berbasis literatur**:
  - **Komponen simetris** — rasio I2/I1, I0/I1, I0/I2 (tanda sekuens per tipe, SEL), plus sudut sekuens (∠I2−∠I1, ∠I0−∠I1), rasio tegangan (V2/V1, V0/V1), dan impedansi sekuens (Z0/Z1/Z2).
  - **Resistansi gangguan (Rf)** — rendah → flashover/petir/satwa; tinggi → vegetasi.
  - **Waktu kejadian** — hour-of-day (fitur diskriminatif #1 per Minnaar 2014; puncak diurnal bird streamer ~06:00 & ~22:00) dan bulan/musim (kemarau Indonesia → kebakaran lahan).
  - **Cuaca lokasi** (OpenWeather) — badai petir → petir; hujan/kabut/RH tinggi → polusi; cerah-kering → kebakaran. *Caveat: cuaca SAAT INI, bukan saat kejadian* (lag 1 rerun; valid untuk gangguan baru).
  - **Tanda waveform** (`waveform_signatures.py` dari raw COMTRADE) — transien/HF tajam (`di_dt_norm`, `hf_ratio`) → petir; durasi + clear/reclose → temporer (petir/satwa) vs permanen (vegetasi/isolator).
  - Kandidat: Sambaran Petir, Vegetasi/Pohon, Satwa Liar (Bird Streamer), Flashover Polusi/Isolator, Kebakaran di Bawah Saluran; 3-fasa simetris → Power Swing.
  - Output: tabel **fakta terukur** + tabel **kandidat ter-ranking** (skor + bukti) — keduanya dalam **expander** (tertutup default), tabel HTML print-friendly (`build_cause_table_html`); plus penjelasan, catatan validasi, referensi. Ambang `decisive` (skor top ≥3 & selisih ≥1) → label tegas; jika tidak → "Indikasi Awal (perlu validasi lapangan)". Konteks **Indonesia/tropis**. Referensi penyebab di `literature/fault_type/` (`.md`).
- **Dataset Penyebab (jembatan rule → ML)**: dipindahkan ke tab `Machine Learning > Dataset Penyebab`. Panel merekam **feature-vector** kasus (48 kolom, kolom A = `case_id = sha1(line_name|fault_time_cfg)`: metadata filter UPT/ULTG/segment, komponen simetris, Rf, jam/bulan, cuaca, tanda waveform, jarak SE/DE, prediksi rule) + **penyebab terkonfirmasi** (label user pasca-inspeksi) ke sheet `fault_cause` pada Database Spreadsheet (upsert by `case_id`; Sheets API + service account), fallback unduh CSV.
- Grafik SE/DE: memakai hasil paling update dari session; scoring SE via status `VALID/CHECK/UNCERTAIN` + warning count; scoring DE via `quality_score`; line length mengikuti `effective_line_param`. Label draggable + both-GI + marker filled (lihat Double-End).
- Tower Map Summary: default DE jika tersedia, fallback SE; fokus ke dua tower pengapit; Map Settings default tertutup; tabel -5/+5 tower default terbuka saat focus fault.
- Weather Summary: tampil setelah Tower Map punya data tower dan sumber fault.

## Machine Learning

- Tab `Machine Learning` memusatkan dataset berlabel dan fondasi model masa depan.
- Sub-tab `Dataset Penyebab`: menyimpan feature-vector penyebab gangguan ke sheet `fault_cause`.
- Sub-tab `Kalibrasi Lokasi`: menyimpan hasil kalkulasi SE/DE, parameter line/effective line, mixed conductor, panjang Tower Schedule, dan label aktual lapangan ke sheet `fault_location`.
- Form kalibrasi lokasi menampilkan tiga field utama: `Jarak Hasil Perhitungan DE` (disabled), `Nomor Tower Hasil Kalkulasi DE` (disabled, tower terdekat dari jarak DE), dan `Nomor Tower Aktual Hasil Inspeksi Lapangan` (opsi dari kolom `SPAN` bila Tower Schedule sudah dimuat; fallback teks jika belum).
- Target model lokasi tahap awal adalah **residual correction**, bukan mengganti rumus proteksi: `DE corrected = DE raw + prediksi(actual_distance_km - de_raw_km)`.
- Raw DE harus tetap ditampilkan terpisah dari koreksi ML. Jika dataset belum cukup, tampilkan status belum siap, bukan prediksi palsu.
- Credentials dapat mendefinisikan `fault_cause_sheet` dan `fault_location_sheet` pada section `[spreadsheet]` atau `[machine_learning]`.

---

## Case Storage

- Format: arsip ZIP berisi `records/local_cfg`, `records/local_dat`, `records/remote_cfg`, `records/remote_dat`, `manifest.json`, `case_state.json`.
- `manifest.json`: schema, timestamp, nama case, folder Drive target, daftar file.
- `case_state.json`: snapshot `st.session_state` yang JSON-safe (DataFrame → records+columns, complex → real/imag, numpy → tipe JSON; bytes rekaman tidak masuk JSON).
- Restore: dari sidebar sebelum validasi local COMTRADE; file dari ZIP dibungkus sebagai upload virtual dengan `.name` dan `.getvalue()`. Restore memakai MD5 hash untuk mencegah restore loop berulang.
- Export: tombol `Export Case ZIP` di `Setup DB > Case Storage`. Nama file digenerate otomatis: `porlungcase_{line_name}_{YYYYMMDD}_{HHMMSS}.zip`.
- **Simpan/Muat Case via Spreadsheet** (`cloud_cases.py`, di Setup DB > Case Storage): ZIP case → base64 **chunked** ke sheet `saved_cases_data` (1 baris/case, payload dipecah ≤49000 char/sel), indeks ringkas ke sheet `saved_cases` (upsert by `case_id = sha1(line_name|fault_time_cfg)`) termasuk metadata filter UPT/ULTG Local/Remote dan Segment. Daftar case dimuat **diurut `saved_at` terbaru**; pilih → rakit chunk → `restore_case_archive`; metadata indeks dipakai sebagai fallback restore filter untuk case lama. **Loader tersedia di sidebar "Case Storage"** (muncul begitu credentials/Database URL ada) sehingga user bisa memilih case tersimpan **di landing page tanpa upload COMTRADE/ZIP**; juga ada di Setup DB > Case Storage (untuk save). **TANPA Google Drive** — service account akun personal tidak punya kuota Drive (`storageQuotaExceeded`), jadi payload disimpan langsung di spreadsheet. **Melengkapi** (tidak menggantikan) save/load ZIP manual.
- **Yang disimpan ke case ZIP:** semua session state kecuali key sensitif. `CASE_SETTINGS_KEYS` menjamin kunci berikut selalu disimpan: DB URLs, sheet names, signal assignment (channel selections + CT/VT + recorded side), line param/effective line param, sumber line parameter, data impedansi spreadsheet termasuk `mixed_conductor_sections`, OpenWeather API key.
- **Yang tidak disimpan:** runtime credentials file, service account, xweather/accuweather key, bytes file upload sementara.

### Runtime Credentials

- Format: file `credentials.toml` atau `credentials.json`. **Upload dilakukan di panel `Credentials` sidebar** (bukan lagi di Setup DB). Setup DB hanya menyisakan indikator credentials aktif, tombol Download Template, dan Clear (tanpa expander show/hide, tanpa uploader).
- Hanya dibaca ke memory/session; tidak ditulis ke disk, tidak dicetak, tidak diekspor.
- Dapat mengisi otomatis: Database Spreadsheet URL, Line/Cable/Distance sheet names, Tower Schedule URL + sheet, Machine Learning sheet names (`fault_cause_sheet`, `fault_location_sheet`), OpenWeather API key, Google service account opsional.
- Tombol `Clear Runtime Credentials from Session` (di Setup DB) tersedia.
- `.gitignore` harus mengecualikan `.streamlit/secrets.toml`, folder `credentials/` (beserta isinya), dan `*credentials*.toml`/`*credentials*.json` (prefix apa pun, mis. `porlung_credentials.toml`).
- **Auto-load credentials lokal:** saat startup, bila belum ada credentials dimuat, aplikasi membaca `credentials/porlung_credentials.toml` (atau `credentials/credentials.toml`/`.json`), parse + apply otomatis. Tambahan: bila `runtime_gdrive_service_account` belum ada, aplikasi memindai `credentials/*.json` untuk file service account (`"type":"service_account"` + `private_key`) dan memuatnya. Service account dipakai untuk **tulis** Sheets API (dataset `fault_cause`, `saved_cases`/`saved_cases_data`). Semua file di `credentials/` **tidak pernah** di-commit (gitignored).

### Prioritas Konfigurasi

1. Uploaded runtime credentials di session
2. Streamlit secrets / `.streamlit/secrets.toml`
3. Environment variables
4. Input manual UI
5. Default demo/public (hanya jika benar-benar aman)

---

## UI/UX dan Frontend

- Aplikasi adalah tool engineering/reporting, bukan landing page. Tampilan padat, rapi, mudah discan.
- Hindari dekorasi berlebihan, shadow besar, gradient mencolok.
- Section besar memakai heading jelas dan ringkas. Data penting terlihat tanpa scroll di dalam card.
- HTML custom via `st.html` jika tersedia; fallback `components.html`. Hindari `st.markdown(..., unsafe_allow_html=True)` untuk blok HTML panjang.
- CSS scoped pada class komponen, bukan selector global Streamlit, kecuali untuk print/report.
- Card: radius kecil-menengah, border halus, background terang, tidak ada shadow besar.
- Mobile: layout card menjadi satu kolom, konten tidak terpotong, tidak ada overflow/scroll internal sebagai solusi utama, grid forecast turun menjadi 4 kolom lalu 2 kolom.
- Tabel data engineering boleh memakai Streamlit dataframe untuk eksplorasi; Summary/report memakai card/tabel HTML print-friendly.
- Jangan tambah label/widget yang menyebut data tidak tersedia (misalnya petir/badai) kecuali backend punya provider aktual.
- Istilah teknis boleh untuk protection engineer; istilah cuaca/provider diterjemahkan ke bahasa Indonesia.

### Print/Report

- Summary harus print-friendly.
- Sidebar, uploader, toolbar, kontrol eksplorasi tidak dicetak.
- Card/tabel/plot besar tidak boleh pecah buruk di tengah halaman.
- Dataframe interaktif disembunyikan saat print jika ada tabel HTML pengganti.
- Penomoran baris tabel default dari 1, bukan 0.

---

## Session State Penting

**Local:**
`assigned_df`, `local_transformer_data`, `fault_window`, `phasors`, `prefault_phasors`, `fault_type_result`

**Remote:**
`remote_assigned_df`, `remote_transformer_data`, `remote_fault_window`, `remote_phasors`, `remote_prefault_phasors`, `remote_fault_type_result`

**Line:**
`line_param`, `effective_line_param` (override length+Z_total dari sumber yang dipilih; dibaca oleh SE/DE/HR), `line_length_source` ("line_parameter" atau "tower_schedule")

**Tower:**
`tower_schedule_df`, `tower_schedule_filtered_df`, `tower_schedule_selected_length_km`, `tower_schedule_selected_length_source`, `tower_schedule_selected_segment`, `tower_schedule_selected_upt`, `tower_schedule_selected_ultg`

**Case Storage:**
`case_name`, `case_drive_folder_url`, `case_drive_folder_id`, `case_local_cfg_name`, `case_local_cfg_bytes`, `case_local_dat_name`, `case_local_dat_bytes`, `case_remote_cfg_name`, `case_remote_cfg_bytes`, `case_remote_dat_name`, `case_remote_dat_bytes`

**HR:**
`high_resistance_result` (+ remote equivalent jika dihitung)

**SE:**
`single_ended_result`, `remote_single_ended_result`, `single_ended_df`, `remote_single_ended_df`

**DE:**
`two_ended_result`, `two_ended_quality`, `two_ended_reverse_result`, `two_ended_reverse_quality`, `two_ended_local_single_result`, `two_ended_remote_single_result`, `two_ended_remote_sync_shift_s`, `two_ended_remote_sync_method`, `two_ended_operating_status`

**R-X:**
`rx_locus_summary_fig_local`, `rx_locus_summary_fig_remote` (+ metadata masing-masing)

---

## External Links

- Popup tower dan fault menyediakan `Open Maps` dan `Directions` via Google Maps query/directions berbasis latitude/longitude.

---

## Risiko Teknis

- `app.py` masih besar; banyak state saling bergantung — refactor bertahap, satu kelompok fungsi per tahap.
- `st.stop()` di dalam tab dapat menghentikan render seluruh aplikasi; gunakan `if/else` lokal.
- Summary dirender lebih awal; hasil kalkulasi yang dihitung setelahnya baru tampil pada rerun berikutnya.
- CSS/DOM selector Streamlit bawaan rapuh; scope ke class komponen.
- Folium map: gunakan `key`, `center`, `zoom` eksplisit saat memaksa fokus fault.
- Banyak kalkulasi sangat bergantung pada kualitas signal assignment, polaritas CT/VT, dan kecocokan line/tower data.
