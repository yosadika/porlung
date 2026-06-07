# Transmission Fault Locator — Claude Context

Aplikasi Streamlit untuk analisis gangguan transmisi tenaga listrik. Membaca rekaman COMTRADE, menentukan fault type, menghitung lokasi gangguan single-end dan double-end, menggambar R-X locus, serta menampilkan tower schedule dan cuaca di titik gangguan.

**Spesifikasi lengkap:** [`PRD.md`](PRD.md)  
**Algoritma & rumus (fault cursor, SE, DE, HR):** [`FORMULAS.md`](FORMULAS.md) — sumber kebenaran matematis; perbarui saat formula di kode berubah, jangan duplikasi rumus di PRD/CLAUDE  
**Riwayat keputusan & guardrail:** [`memory/MEMORY.md`](memory/MEMORY.md) — baca sebelum mengubah kode

## Stack

- Python + Streamlit (multipage via `tabs/`)
- Pandas, NumPy, SciPy untuk kalkulasi sinyal dan impedansi
- Folium / streamlit-folium untuk peta tower
- Google Sheets API untuk line parameter dan tower schedule
- OpenWeather One Call 4.0 untuk cuaca; Open-Meteo sebagai fallback
- Google Drive API tersedia di backend tapi tidak diekspos di UI

## Struktur Modul

| File | Tanggung Jawab |
|---|---|
| `app.py` | Entry point, sidebar upload, tab utama, CSS global |
| `app_runtime.py` | Cache COMTRADE/Sheets, query tower schedule, monkey-patch dataframe |
| `app_helpers.py` | Helper umum lintas fitur (downsampling, validasi, normalisasi); konstanta `OHM = chr(0x03A9)`; `cached_style_format()` untuk cache `.style.format()`; `plotly_image_filename()` (nama file unduhan plot `porlungplot_{line}_{timestamp}`) |
| `auto_assignment.py` | Deteksi otomatis channel tegangan/arus dari COMTRADE; scoring dengan suffix/prefix match (bukan substring sembarangan) |
| `case_storage.py` | Runtime credentials, save/restore case ZIP; `CASE_SETTINGS_KEYS` menjamin kunci konfigurasi selalu tersimpan; `_WIDGET_RESTORE_CLEANUP_KEYS`/`_WIDGET_RESTORE_CLEANUP_PREFIXES` mencegah widget key masuk restore; `make_case_json_safe()` **drop objek figure Plotly/Matplotlib jadi `None`** (recompute saat restore) |
| `weather_services.py` | API cuaca (OpenWeather, Open-Meteo), formatter data |
| `weather_ui.py` | HTML kartu cuaca, icon, tren suhu, bar peluang hujan |
| `tower_map.py` | Interpolasi fault pada jalur tower, render Folium map, tabel tower dengan badge proteksi |
| `rx_locus.py` | Parse relay settings, overlay zona proteksi, trajectory R-X |
| `line_analysis_helpers.py` | Infer GI name, reverse DE, comparison dataframe, override panjang line |
| `waveform_helpers.py` | Plot waveform, phasor diagram, sync local/remote; `build_synchronized_fault_plot` mendukung dual subplot tegangan+arus |
| `waveform_signatures.py` | Tanda waveform penyebab gangguan dari raw COMTRADE: transien/HF (`di_dt_norm`, `hf_ratio`, `transient_sharp`), durasi gangguan, clear/reclose (temporer vs permanen). `compute_waveform_signatures(df, fault_window, samples_per_cycle, frequency)` |
| `cloud_cases.py` | Simpan/muat case via **spreadsheet** (TANPA Drive — service account personal tak punya kuota Drive): ZIP (`build_case_archive_bytes`) → base64 **chunked** ke sheet `saved_cases_data` (1 baris/case, kolom = chunk ≤49000 char), indeks ke `saved_cases` (upsert by `case_id`). `save_case_to_cloud()`, `list_saved_cases()` (urut `saved_at`), `load_case_from_cloud(url, case_id)` (rakit chunk → `restore_case_archive`). Melengkapi save/load ZIP manual |
| `fault_cause_dataset.py` | Pengumpulan dataset berlabel (jembatan rule→ML): `build_fault_cause_feature_row()` rakit feature-vector (43 kolom, `DATASET_COLUMNS`, kolom A=`case_id`), `append_feature_row_to_gsheet()` **upsert** ke sheet `fault_cause` (update bila `case_id` cocok, else append; header auto-migrasi) via Sheets API + service account; `make_case_id()`, `CONFIRMED_CAUSE_LABELS`. Fallback CSV download di UI |
| `single_ended.py` | Kalkulasi SE: loop impedansi, reactance/magnitude/projection method, Takagi fallback (Rf compensation) |
| `two_ended.py` | Kalkulasi DE: positive-sequence two-ended, quality scoring, candidate ranking, angle search untuk unsync |
| `fault_workflow_helpers.py` | Explanation text, threshold fault type, TWS location, timestamp parser; `render_se_formula_expander()`; `render_hr_formula_expander()`; `render_fault_cursor_explanation()` (dasar penentuan fault cursor dalam tabel + referensi literatur); `render_fault_cursor(..., settings_source_prefix)` — DE membaca pengaturan dari Local/Remote End; `_sync_checkbox`/`_FC_SYNC_PARTNERS` sinkron checkbox auto 2 arah |
| `summary_helpers.py` | Waveform fokus Summary, scoring SE/DE, grafik posisi SE/DE; `build_de_position_figure()`/`build_summary_location_plot()` (label both-GI, marker filled); `estimate_summary_disturbance_cause(..., fault_hour, fault_month, weather_context, waveform_signatures)` return `(label, detail_dict)` — candidate-scoring penyebab (petir/vegetasi/satwa/polusi/kebakaran) dari fault type + komponen simetris (rasio I2/I1, I0/I1, I0/I2 + sudut + impedansi Z0/Z1/Z2) + Rf + hour/bulan + cuaca lokasi + tanda waveform (transien/durasi/reclose), basis literatur `literature/fault_type/` (lihat memory `fault_cause_references`) |
| `tabs/line_parameter.py` | Render tab Line; **satu-satunya** selector sumber panjang line (`line_length_source`); simpan `effective_line_param` ke session_state; `@st.fragment` |
| `tabs/double_ended.py` | Render tab Double-End; `render_de_formula_expander()`; `@st.fragment`; plot Line Position draggable + label both-GI; Status Diagnostik human-readable; fault cursor compact pakai `settings_source_prefix` |
| `tabs/signal_assignment.py` | Render sub-tab Signals di Local End — **TIDAK `@st.fragment`** karena mengubah `assigned_df` yang menjadi fondasi semua kalkulasi; termasuk section **Koreksi Polaritas** (`local_invert_voltage`, `local_invert_current`) |

## Aturan Wajib

1. **Jangan hapus atau ubah fitur** yang terdaftar di PRD tanpa konfirmasi eksplisit dari user.
2. **Jangan hardcode** URL spreadsheet private atau API key — repo bersifat public.
3. **Jangan simpan** credentials sensitif (runtime credentials, service account, xweather/accuweather key) ke dalam case ZIP. OpenWeather API key **boleh** disimpan ke case ZIP karena dibutuhkan untuk restore konteks cuaca.
4. **Jangan gunakan `st.stop()`** di dalam tab; pakai `if/else` lokal.
5. **Fault inception ≠ DFT cursor:** inception untuk sync/trigger, DFT cursor untuk kalkulasi phasor/locus.
6. **Default yang tidak boleh diubah:**
   - Auto fault cursor detection: `off`
   - Referensi visual alignment DE: `fault_phase_voltage` jika tersedia, fallback `fault_cursor`
   - Metode visual alignment DE: Raw waveform correlation
   - Zone relay base: primary ohm
   - Tower Map Summary: default fault source = DE jika tersedia
7. **Setelah perubahan apapun**, jalankan:
   ```
   python -m py_compile app.py app_runtime.py app_helpers.py auto_assignment.py case_storage.py weather_services.py weather_ui.py tower_map.py rx_locus.py line_analysis_helpers.py waveform_helpers.py waveform_signatures.py fault_cause_dataset.py cloud_cases.py fault_workflow_helpers.py summary_helpers.py single_ended.py two_ended.py high_resistance.py fault_detection.py fault_type.py phasor.py comtrade_reader.py conductor_impedance_importer.py line_parameter.py signal_assignment.py tabs/line_parameter.py tabs/double_ended.py tabs/signal_assignment.py
   ```
8. **Setelah perubahan workflow**, validasi minimal: Summary, Setup DB, Local End, Remote End, Line, HR Check, Single-End, Double-End, R-X Locus.
9. **Setelah perubahan kalkulasi**, validasi: SE/DE memakai sumber panjang line yang dipilih, Tower Map fault interpolasi memakai `KUMULATIF km`, Summary tidak blank bila kalkulasi belum lengkap.

## Arsitektur Fragment (`@st.fragment`)

Beberapa fungsi render menggunakan `@st.fragment` agar perubahan dropdown tidak memicu full app rerun:

| Fragment | File | `st.rerun(scope="app")` dipanggil saat |
|---|---|---|
| `render()` | `tabs/line_parameter.py` | Normalize diklik |
| `render()` | `tabs/double_ended.py` | Calculate DE diklik |
| `render_single_ended_analysis` | `app.py` | Calculate SE diklik |
| `render_high_resistance_check` | `app.py` | — (display only) |
| `render_simple_rx_locus` | `app.py` | — (display only) |

**`tabs/signal_assignment.py` TIDAK di-fragment** — mengubah channel, CT/VT ratio, atau flag `invert_voltage`/`invert_current` mengubah `assigned_df` yang menjadi fondasi phasor, SE, DE. Tanpa full rerun, downstream state menjadi stale dan kalkulasi salah.

**Aturan fragment:** hanya gunakan jika perubahan widget di dalam TIDAK mempengaruhi state yang dibaca tab/fungsi lain, ATAU ada `st.rerun(scope="app")` setelah perubahan penting.

## Sumber Panjang Line (`effective_line_param`)

Selector sumber panjang line (Line Parameter vs Tower Schedule) **hanya** ada di **tab Line** — sudah dihapus dari halaman SE dan DE. Hasilnya disimpan ke `st.session_state["effective_line_param"]`. SE, DE, **HR Check**, dan R-X Locus membaca dari key ini via `resolve_end_analysis_context` (`effective_line_param or line_param`) — tidak ada kalkulasi ulang per-tab.

- Halaman SE/DE hanya menampilkan **caption** panjang line aktif + arahan ke tab Line (tidak ada widget pilih sumber).
- Perubahan selector → simpan pilihan saja (tidak hitung)
- Klik Normalize → hitung `effective_line_param` dan trigger `st.rerun(scope="app")`
- Jika `effective_line_param` tidak ada di session_state, fallback ke `line_param`

## Cache Version Bumping

Figure yang di-cache di session_state (`_de_viz_fig`, `_sloc_key`, `_summary_rx_cache`) menyertakan key versi/parameter di cache key. Saat label/format figure diubah, **bump versi string** agar cache lama otomatis dibuang. `_sloc_key` saat ini `"v3"`. **Cache figure yang dipengaruhi pilihan zona/relay (R-X Locus Summary) wajib menyertakan semua key relay** (`rx_locus_setting_row_*`, substation, bay, show_zone, zone_setting_base) — kalau tidak, Summary menyajikan figure stale.

**Cache waveform** (`_lw_fig_key`, `_rw_fig_key`, `_de_sync_fig_key`) **wajib menyertakan `invert_voltage` dan `invert_current`** dari `local_transformer_data`/`remote_transformer_data` — tanpanya, membalik polaritas tidak langsung memperbarui plot.

## Plot Line Position Visualization (DE & Summary)

- Label annotation **draggable** via `st.plotly_chart(..., config={"editable": True, "edits": {...}})`. `edits` mengaktifkan hanya `annotationPosition`/`annotationTail`; `titleText`/`axisTitleText`/`legendText` di-`False` agar teks "Click to enter..." tidak muncul.
- **JANGAN implementasi auto-placement label kompleks** (free-zone, candidate offset) — terbukti boros iterasi & overthinking. Draggable bawaan Plotly lebih reliable.
- Label & hover menampilkan jarak dari **kedua GI** (lokal + remote). Semua marker **filled** (tanpa `-open`); distinksi lokal/remote lewat warna.

## Sinkronisasi Fault Cursor Local/Remote ↔ DE

- DE memanggil `render_fault_cursor(..., settings_source_prefix="local_fc"/"remote_fc")` → tidak render widget parameter, baca nilai dari halaman Local/Remote End. `fault_window`/`remote_fault_window` adalah key session_state bersama (dipakai juga R-X Locus).
- Checkbox "Gunakan deteksi otomatis" sinkron **dua arah** via `_sync_checkbox(src, dst)` (callback `on_change` set partner = nilai sama) + dict `_FC_SYNC_PARTNERS`. Checkbox **tanpa `value=`** (murni dari session_state). Jangan pakai pola delete-key + `value=partner` → menyebabkan inversi.

## Risiko yang Perlu Diperhatikan

- `app.py` masih besar; banyak state saling bergantung — refactor bertahap, satu kelompok fungsi per tahap.
- CSS/DOM selector Streamlit bawaan rapuh; scope selector ke class komponen.
- Folium map: gunakan `key`, `center`, `zoom` eksplisit saat ingin fokus ke titik fault.
- Summary dirender lebih awal; hasil kalkulasi yang dihitung setelahnya baru tampil pada rerun berikutnya.
- Fragment + session_state: perubahan di dalam fragment baru terlihat tab lain setelah full rerun. Selalu pastikan `st.rerun(scope="app")` dipanggil setelah perubahan penting.
- **Sync sidebar→widget lintas-tab: authoritative** (set tiap run saat filter aktif, sebelum tabs render) lebih reliable dari change-guard yang rapuh terhadap restore. R-X Locus substation/bay di-set tiap run dari sidebar bila `_sb_ia` aktif.
- **Upload-end filter hierarchy:** filter GI/line berada di expander upload rekaman masing-masing end. Local End: UPT/ULTG dari `distance_settings` → Segment dari `line_impedance` → GI/Bay-Line dari `distance_settings`. Remote End: UPT/ULTG dari `distance_settings` → GI/Bay-Line dari `distance_settings`. Segment hanya dipilih di Local End agar satu segment/line menjadi konteks tower/line, sementara UPT/ULTG local dan remote boleh berbeda. Legacy key `sidebar_filter_upt`/`sidebar_filter_ultg` tetap diisi dari pilihan Local End untuk kompatibilitas downstream. **Jangan kembalikan ULTG ke `line_impedance`** — sudah dipindah ke `distance_settings` agar hierarki UPT→ULTG konsisten.
- **Koreksi polaritas channel:** `invert_voltage`/`invert_current` di `local_transformer_data`/`remote_transformer_data`. Bila Visual Sync Score DE ≈ −1, kemungkinan VT remote terbalik → centang "Balik Polaritas Tegangan Remote". Jangan tambah logika pembalikan di tempat lain selain `apply_signal_assignment()`.
- **Selectbox: jangan campur `index=` + `key=`** bila session_state di-set dari luar → konflik. Pakai `key=` saja + seed default ke session_state bila kosong/invalid (lihat R-X Locus substation).
- **Normalisasi nilai numerik konsisten** antara sumber & konsumen: `"1.0"` (spreadsheet) vs `"1"` (sidebar `_nv`) — gunakan helper normalisasi sama (`_nv_line`) saat mencocokkan.
- **Case snapshot: objek figure (Plotly/Matplotlib) di-DROP jadi `None`** (`make_case_json_safe`) — bukan JSON-safe, `str()` menghasilkan string sampah raksasa yang membengkakkan payload (locus/figure berisi ribuan titik). Figure & cache-nya **dihitung ulang dari state saat restore** (locus dari `rx_locus_setting_row_*` + assigned_df + fault_window). Selection (string/angka) tetap tersimpan via general snapshot loop. Jangan simpan objek render ke case.

## Efisiensi Token (berlaku untuk semua sesi)

- **Jangan re-read file yang sudah ada di konteks** — jika konten sudah terlihat dari turn sebelumnya, gunakan langsung untuk `Edit`.
- **Jangan re-read setelah `Edit` sukses** — `Edit`/`Write` error jika gagal; re-read konfirmasi = token mubazir.
- **Gunakan `Grep -C 3`** untuk menemukan string target sebelum edit — `-C` maksimal 5–10; lebih dari itu mubazir.
- **`Read` dengan `offset`+`limit`** jika hanya butuh sebagian file besar (app.py ~4000 baris).
- **Satu `Read` blok luas, bukan beberapa `Read` kecil yang overlap** — hitung rentang sekali, baca semua sekaligus.
- **PRD.md: jangan baca penuh kecuali diminta eksplisit** — gunakan `Grep` + `Read offset+limit` untuk section relevan saja.
- **Literatur: baca file `.md` hasil markitdown, BUKAN PDF.** PDF di `literature/calculations/` & `literature/fault_type/` sudah dikonversi ke `.md`. `Grep` hanya bekerja pada `.md` → temukan kata kunci dulu, lalu `Read offset+limit` blok relevan saja (jauh lebih hemat token daripada `Read` PDF per-halaman).
- **`.md` = indeks pencarian konsep, BUKAN sumber rumus presisi.** markitdown (pdfminer, bukan OCR) sering merusak notasi matematis: subscript/superscript hilang, simbol Yunani/pecahan/matriks acak, PDF scan (mis. IEEE C37.114) hampir kosong. Untuk rumus eksak, verifikasi ke PDF/teori baku — **jangan salin mentah notasi dari `.md`**. SSOT rumus tetap di `FORMULAS.md` (ditulis dari teori, bukan dari `.md`).
- **PDF tanpa `.md`: buat `.md`-nya otomatis dulu, baru baca.** Sebelum membaca PDF apa pun di repo: cek `.md` yang mencakupnya lewat **[`literature/README.md`](literature/README.md)** (indeks pemetaan PDF↔.md; `calculations/` pakai nama bersih legacy, `fault_type/` pakai basename identik). Jika benar belum ada, konversi dengan markitdown (terpasang di venv: `markitdown[pdf]`) memakai **konvensi basename identik** (`file.pdf` → `file.md`), perbarui indeks, lalu Grep/Read `.md`-nya. Pola konversi:
  ```python
  from markitdown import MarkItDown
  res = MarkItDown().convert("path/ke/file.pdf")
  open("path/ke/file.md", "w", encoding="utf-8").write(res.text_content or "")
  ```
  Catat di output bila hasil `< 5000 char` (kemungkinan PDF scan → perlu OCR, jangan andalkan teksnya). Tujuan: jangan pernah `Read` PDF per-halaman bila `.md` bisa dibuat sekali dan dipakai untuk semua pencarian berikutnya.
- **Compile check: jalankan langsung tanpa `cd`** — working directory sudah benar sejak awal session; `cd /d` adalah sintaks PowerShell/cmd, bukan Bash.
- **Jangan spawn subagent untuk edit < 50 baris di 1 file** — cold-start subagent (~10K token) lebih mahal dari mengerjakan inline.
- **Batch edit dalam satu turn** jika ada beberapa perubahan kecil di file yang sama.
- **Fungsi baru > 20 baris: gunakan `Write`/`Edit`, bukan `cat >>` via Bash** — heredoc append rawan escape sequence bug (`\_`, `\ `) yang baru ketahuan saat compile, menghasilkan extra turns.
- **Mulai sesi baru** untuk topik/fitur yang tidak berkaitan — jangan akumulasi 60+ turn dalam satu sesi.
- **Verifikasi asumsi framework sebelum coding** — Edit yang kemudian di-revert adalah pemborosan terbesar; lebih murah investigasi 1 menit daripada 3 attempt salah.
- **UI behavior Streamlit: investigasi dulu, coding kemudian** — sebelum mengimplementasi show/hide/accordion, verifikasi: apakah widget menulis balik ke session_state? Apakah `expanded=` controlled atau initial-state-only? Jika tidak yakin, solusi client-side (JS) lebih reliable dari Python/session_state.
- **Sidebar accordion rules:** `install_sidebar_accordion_rules()` di `app.py` memakai `st.html(..., unsafe_allow_javascript=True)` untuk menutup expander sidebar lain saat satu expander dibuka. Jangan hapus saat mengganti API deprecated `components.v1.html`; `expanded=` Streamlit hanya initial state dan tidak cukup untuk rules show/hide client-side.
- **Upload sidebar card tidak auto-hide saat rekaman lengkap:** panel Upload Local/Remote End tetap boleh terbuka setelah `.cfg + .dat` lengkap agar user bisa melihat/mengubah filter GI/line dan mengganti rekaman. Jangan kembalikan kondisi `and not _local_complete`/`and not _remote_complete` pada `expanded=`.
- **Filter upload end conditional:** dropdown UPT/ULTG/Segment/GI/Bay-Line di sidebar hanya dirender jika `database_spreadsheet_url` tersedia dari credentials, secret/env, atau input Setup DB. Jika URL belum ada, panel upload hanya menampilkan uploader rekaman.
- **Encoding UI:** hindari emoji/simbol mentah di label tombol, status, formula helper, dan card cuaca. Pakai teks ASCII (`[OK]`, `[PERHATIAN]`, `ohm`, `deg`, `->`) atau escape Unicode eksplisit untuk simbol yang memang perlu (mis. tombol refresh `\u21bb`). Setelah edit, scan `*.py` untuk pola mojibake `â|Â|Î|Ã|ð|Ÿ|œ|š|á`.
- **Tombol berdampingan di Streamlit: selalu `use_container_width=True`** — tanpanya tombol tidak mengisi lebar kolom dan tampak terpisah jauh meski kolom sudah sempit.
- **Label tombol dan teks UI: title case EYD** — "Refresh Nama File", bukan "Refresh nama file". Berlaku untuk semua label `st.button`, `st.download_button`, heading, dan caption UI.
- **Context overhead ~3,250 token per turn adalah biaya tetap** — gabungkan beberapa perubahan kecil dalam satu sesi agar overhead diamortisasi, bukan dibayar ulang per task.
- **Prompt efektif = screenshot + deskripsi masalah + arah solusi** — ketiga elemen ini menghasilkan penyelesaian 1 prompt. Jika arah solusi tidak ada, tanya dulu sebelum coding.

## Pemilihan Model Dinamis (Routing)

Untuk menghemat biaya, eksekusi berat/ringan dirutekan ke model berbeda lewat **subagent**. Jalankan sesi orchestrator di **Sonnet** (seimbang), lalu delegasikan:

| Tier | Kriteria | Subagent (`.claude/agents/`) | Model |
|---|---|---|---|
| LIGHT | 1 file, sepele (typo, rename lokal, teks UI, formatting), tanpa ubah session_state | `porlung-light` | Haiku |
| STANDARD | 1-2 file dalam satu area fitur, tanpa ubah kontrak session_state lintas halaman | `porlung-standard` | Sonnet |
| HEAVY | `app.py` + ≥2 modul, ATAU ubah/tambah session_state keys lintas halaman, ATAU refactor/alur workflow | `porlung-heavy` | Opus |

- Gunakan **`/route <deskripsi tugas>`** untuk scoping + delegasi otomatis.
- Patokan HEAVY: perubahan menyentuh kunci di "Session State Penting" (PRD.md) karena itu kontrak lintas-halaman (Summary/SE/DE/Tower Map/Weather saling bergantung).
- Di perbatasan dua tier, pilih yang lebih tinggi.
- Catatan: subagent mulai dingin dan membaca ulang konteks — untuk tugas benar-benar sepele saat sesi sudah di model murah, kerjakan inline daripada spawn.
- Hook **tidak bisa** mengganti model; pemilihan hanya di awal sesi (`/model`, `opusplan`) atau di batas spawn subagent.
