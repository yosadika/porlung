# Distance Zone Literature

Folder ini menyimpan literatur referensi untuk implementasi dan validasi gambar R-X locus / distance zone.

## File

- `*.pdf`: sumber asli.
- `*.md`: hasil konversi `markitdown` dari PDF, nyaman untuk pencarian teks umum.
- `*.pages.md`: indeks per halaman PDF. Gunakan file ini saat perlu tahu halaman PDF yang relevan.

## Workflow Pencarian

1. Cari istilah di markdown:

   ```powershell
   rg -n -g "*.md" "quadrilateral|mho|Zone 1|apparent impedance|reach" literature\distance_zone
   ```

2. Jika perlu membuka halaman PDF tertentu, cari di file `*.pages.md`:

   ```powershell
   rg -n -g "*.pages.md" "quadrilateral" literature\distance_zone
   ```

3. Buka PDF asli pada heading `PDF page N` yang ditemukan.

## Catatan Implementasi

- `line_data` menyediakan setting distance relay primer/sekunder yang akan dipakai untuk zona R-X Locus.
- Literatur di folder ini dipakai sebagai referensi bentuk karakteristik, reach, dan interpretasi apparent impedance, bukan sebagai sumber data setting relay operasional.
