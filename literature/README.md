# Literatur — Indeks PDF ↔ Markdown

Setiap PDF dikonversi ke `.md` via **markitdown** (`markitdown[pdf]`) agar bisa di-`Grep` dan dibaca hemat token. **`.md` = indeks pencarian konsep, BUKAN sumber rumus presisi** (markitdown memakai pdfminer/teks, bukan OCR — notasi matematis sering rusak; verifikasi rumus ke PDF/teori baku).

**Konvensi untuk konversi BARU:** nama `.md` = basename PDF identik (`namafile.pdf` → `namafile.md`) agar pengecekan sibling otomatis bekerja. Folder `calculations/` memakai nama bersih (legacy) — lihat pemetaan di bawah.

## `calculations/` — referensi LOKASI gangguan (fault location)

| PDF | Markdown | Status ekstraksi |
|---|---|---|
| Arun G. Phadke, James S. Thorp - Computer Relaying… (2009) | `phadke_thorp_2009.md` | ✅ teks lengkap |
| [Power Systems] Saha, Izykowski, Rosolowski - Fault Location on Power Networks (2010) | `saha_2010.md` | ✅ teks lengkap |
| eriksson1985.pdf | `eriksson_1985.md` | ✅ teks lengkap |
| IEEE Std C37.114-2014 Guide for Determining Fault Location… | `ieee_c37114_2014.md` | ⚠️ minim teks (PDF scan — perlu OCR) |

## `fault_type/` — referensi PENYEBAB gangguan (fault cause)

Memakai konvensi basename identik (`x.pdf` → `x.md`):

| PDF / Markdown (basename sama) | Isi |
|---|---|
| `thesis_ebe_2014_minnaar_u` | Minnaar (2014) — karakterisasi & klasifikasi otomatis penyebab; fitur diskriminatif hour-of-day #1 |
| `6066_IntroSymmetrical_SZ_20110510_Web` | SEL — Introduction to Symmetrical Components (tanda sekuens per tipe gangguan) |
| `applsci-11-07804` | Transmission Line Fault-Cause Identification |
| `computation-10-00144-v2` | A Review and Taxonomy on Fault Analysis in Transmission Lines |
| `AutomatingTransmissionLineFaultRootCauseAnalysis` | Automating TL Fault Root-Cause Analysis (IEEE) |
| `KulkarniPES2010` | Kulkarni PES 2010 — fault cause |
| `1-s2.0-S2352484722004334-main` | Artikel ScienceDirect — fault analysis |

## Cara konversi (jika ada PDF baru tanpa `.md`)

```python
from markitdown import MarkItDown
res = MarkItDown().convert("literature/<folder>/<file>.pdf")
open("literature/<folder>/<file>.md", "w", encoding="utf-8").write(res.text_content or "")
```
Jika hasil `< 5000 char` → kemungkinan PDF scan (isi gambar); butuh OCR, jangan andalkan teksnya.
