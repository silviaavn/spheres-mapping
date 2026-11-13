# Revisi Data Dictionary — Form Kobo

Terakhir diperbarui: 2026-11-13

Daftar hal yang perlu diperbaiki di data dictionary. Ubah status jadi `done` kalau sudah dibetulkan.

## Form: Maternal Outcome

### Koreksi kolom `jumlah instance`

| # | Baris CSV | Sekarang | Seharusnya | Status |
|---|---|---|---|---|
| 1 | 12 (baris kosong) | 1 | kosong (pindahkan ke baris Patient) | open |
| 2 | 13 (Patient.name.text) | kosong | 1 | open |
| 3 | Organization / Location | kosong | tetap kosong (master data) | ok |

Setelah koreksi: total = 12.

### Temuan mapping

| # | Temuan | Status |
|---|---|---|
| 1 | Keadaan Ibu: Value Name bergeser 1 baris (sehat→Illness, sakit→Dead). Seharusnya sehat→102514002, sakit→39104002, meninggal→419099009 | open |
| 2 | PractitionerRole: display SP000396 / SP000397 tertukar dengan value name | open |
| 3 | Typo `ofiicial` di Practitioner.identifier | open |
| 4 | Baris 45: path `Organization.address.extension.url` di blok Location | open |
| 5 | URL organization-type ada spasi di akhir | open |

## Log perubahan revisi
- 2026-11-13: Dibuat dari review Maternal Outcome.
