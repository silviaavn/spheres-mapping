# Revisi Data Dictionary — Form Kobo

Terakhir diperbarui: 2026-11-13
File dictionary terbaru: `mapping/kobo-data-dictionary-maternal-outcome.csv` (Kobo_3 + revisi di bawah)

> Nomor baris di bawah mengikuti Kobo_3. Di file `mapping/`, baris setelah 11 bergeser +1 karena ada baris baru `Practitioner.identifier.value`.

Daftar hal yang perlu diperbaiki di data dictionary. Ubah status jadi `done` kalau sudah dibetulkan.

## Form: Maternal Outcome

### Koreksi kolom `jumlah instance`

| # | Baris CSV | Sebelumnya | Seharusnya | Status |
|---|---|---|---|---|
| 1 | 12 (baris kosong) | 1 | kosong (pindahkan ke baris Patient) | done |
| 2 | 13 (Patient.name.text) | kosong | 1 | done |
| 3 | Organization / Location | kosong | tetap kosong (master data) | ok |
| 4 | 71 (Condition.category) | 1 | pindah ke baris 70 (baris pertama Condition) supaya konsisten dengan aturan | done (mapping/) |

Hasil Kobo_3: jumlah instance = 12, jumlah code = 14 (sesuai).

### Temuan mapping

| # | Temuan | Status |
|---|---|---|
| 1 | Keadaan Ibu: Value Name bergeser 1 baris (sehat→Illness, sakit→Dead). Seharusnya sehat→102514002, sakit→39104002, meninggal→419099009 | done (Kobo_3) |
| 2 | PractitionerRole: display SP000396 / SP000397 tertukar dengan value name | done (Kobo_3): data_entry_staff→SP000396, field_or_call_center_staff→SP000397 |
| 3 | Typo `ofiicial` di Practitioner.identifier | done (Kobo_3) |
| 4 | Baris 45: path `Organization.address.extension.url` di blok Location | done (mapping/): jadi `Location.address.extension.url`, sama seperti baris 36, 39, 42 |
| 5 | URL organization-type ada spasi di akhir | done (Kobo_3) |
| 6 | Practitioner.identifier (baris 10–11) tidak konsisten. Input-nya NIK, tapi baris 10 pakai system `nakes-his-number`, sedangkan baris 11 `identifier.use` pakai system `nik`. Belum ada baris `.system` / `.value` seperti di Patient (baris 14–16) | done (mapping/): disamakan dengan Patient jadi 3 baris `.use` official, `.system` nik, `.value`. System `nakes-his-number` dihapus karena yang diinput NIK |
| 7 | Baris 13: Subcategory tertulis "Identitas Bayi", padahal isinya Nama Ibu / NIK Ibu | done (mapping/): jadi "Identitas Ibu" |

## Log perubahan revisi
- 2026-11-13: Semua item open dibetulkan langsung di `mapping/kobo-data-dictionary-maternal-outcome.csv`. Tidak ada item open tersisa.
- 2026-11-13: Cek Kobo_3. #1, #2, #3, #5 dan koreksi instance done. #4 masih salah (path berubah tapi belum benar). Tambah #6, #7, dan koreksi instance #4.
- 2026-11-13: Dibuat dari review Maternal Outcome.
