# Revisi Data Dictionary — Form Kobo

Terakhir diperbarui: 2026-11-13
File dictionary terbaru: Maternal Outcome → `mapping/kobo-data-dictionary-maternal-outcome.csv`; Raffle → `mapping/kobo-data-dictionary-raffle.csv` (nomor baris di bawah mengikuti CSV asli; di `mapping/` baris setelah 91 bergeser +2)

> Maternal Outcome: nomor baris di bawah mengikuti Kobo_3. Di file `mapping/`, baris setelah 11 bergeser +1 karena ada baris baru `Practitioner.identifier.value`.

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

### Tally variabel BQ vs dictionary

Kolom **Nama Column BQ** sudah ditambahkan di `mapping/` (sebelum "Nama Column Raw"). Hasil: **12 variabel BQ = 12 variabel Kobo** ✅

| Variabel BQ | Variabel Kobo | Path FHIR | Cocok? |
|---|---|---|---|
| data_entry_clerk_type | Siapa yang melakukan entry data? | PractitionerRole.code | ✅ |
| data_entry_clerk_staff_id | Nama yang melakukan entry data | Practitioner.name.text | ⚠️ lihat #8 |
| nik_yang_melakukan_entry_data | NIK yang melakukan entry data | Practitioner.identifier (nik) | ✅ |
| nama_ibu | Nama Ibu | Patient.name.text | ✅ |
| nik_ibu | NIK Ibu | Patient.identifier (nik) | ✅ |
| puskesmas_name | Puskesmas | Organization.name (lookup master data) | ✅ |
| tanggal_pencatatan | Tanggal Pencatatan | Encounter.period.start | ✅ |
| outcome_001 | Keadaan Ibu | Observation SP000389 | ✅ |
| delivery_date | Tanggal Persalinan | Observation 93857-1 | ✅ |
| tanggal_meninggal | Tanggal Meninggal | Observation 81956-5 | ✅ |
| tempat_meninggal | Tempat Meninggal | Observation LT000005 | ✅ |
| sebab_meninggal | Penyebab Meninggal | Observation 79378-6 | ✅ |

| # | Temuan | Status |
|---|---|---|
| 9 | Nama data entry juga masuk ke `Encounter.participant` (type ADM admitter). Kolom Variables di baris `Encounter.participant.individual.display` diisi "Nama yang melakukan entry data" | done (mapping/) |
| 8 | `data_entry_clerk_staff_id` kelihatannya ID, bukan nama, tapi di dictionary dipasang ke "Nama yang melakukan entry data" → `Practitioner.name.text`. Kalau memang ID, seharusnya jadi `Practitioner.identifier` kedua (kemungkinan system `nakes-his-number` yang sebelumnya dihapus), dan `Practitioner.name.text` tidak punya sumber data dari form | open (perlu konfirmasi) |

## Form: Raffle

Sumber: Kobo - Data Dictionary - Kobo Raffle (nomor baris = baris CSV asli, header 7 baris). Versi revisi: `mapping/kobo-data-dictionary-raffle.csv` (kolom BQ terisi, kolom `jumlah code` = 6 dan `jumlah instance` = 7 ditambahkan).

### Tally variabel BQ vs dictionary

**11 variabel BQ = 11 variabel Kobo** ✅ (setelah revisi R1, R2). Input Data belum punya kolom BQ (R12).

| Variabel BQ | Variabel Kobo (baris) | Path FHIR | Cocok? |
|---|---|---|---|
| nama_data_entry | Nama Data Entry (baris baru) | Encounter.participant.individual.display (type ADM) | ✅ |
| puskesmas | Puskesmas Pengampu (27) | Organization.name (lookup master data) | ✅ |
| kecamatan | Kecamatan (57) | Location.address district | ✅ |
| kelurahan | Kelurahan (60) | Location.address village | ✅ |
| lokasi_faskes | Lokasi/Fasilitas Kesehatan (43) | Location (dibuat dari form) | ✅ |
| nama_bidan_desa | Nama Bidan Desa (69) | Practitioner.name.text | ✅ |
| nik_ibu | NIK Ibu (10) | Patient.identifier (nik) | ✅ |
| nama_ibu | Nama Ibu (8) | Patient.name.text | ✅ |
| nomor_telepon | Nomor Telepon (18) | Patient.telecom | ✅ |
| tanggal_kunjungan | Tanggal Kunjungan Pelayanan (92) | Encounter.period.start | ✅ |
| keterangan | Keterangan (106) | Condition.note | ✅ |
| – | Input Data (122) | Observation 385438008 | ⚠️ R12 |

Provinsi dan Kabupaten/Kota (31, 34, 51, 54) tidak perlu kolom BQ karena di-hardcode sesuai deployment.

### Temuan

| # | Temuan | Status |
|---|---|---|
| R1 | `nama_data_entry` (BQ) tidak ada di dictionary, sedangkan "Input Data" (Observation 385438008, nilai Sigizi / E-pus PKD / E-pus) tidak ada di BQ. Kemungkinan keduanya pasangan yang sama, yaitu sistem tempat data di-input. Kalau ternyata `nama_data_entry` adalah nama orang yang meng-input, berarti perlu payload Practitioner/PractitionerRole tambahan dan Input Data belum punya kolom BQ | done (mapping/): `nama_data_entry` masuk ke `Encounter.participant` type ADM admitter, `individual.display`. Ditambah 2 baris baru setelah baris 91 |
| R2 | Kecamatan dan Kelurahan muncul 2x (blok Organization dan blok Location), tapi di BQ hanya ada 1 kolom masing-masing. Perlu ditentukan kolom BQ dipakai untuk resource yang mana, atau keduanya diisi dari kolom yang sama | done (mapping/): Kecamatan & Kelurahan hanya untuk Location. Variabel di blok Organization (37, 40) dikosongkan. Location sekarang dibuat dari form dan dihitung sebagai payload |
| R3 | **SP000776 dipakai dengan 2 arti berbeda**: Condition.code = "Presensi Posyandu" (101) dan value Input Data = "Sigizi" (123). Satu code hanya boleh punya 1 arti, jadi salah satunya harus diganti | done (mapping/): Condition.code jadi SP001135 Presensi Posyandu. SP000776 tetap untuk Sigizi |
| R4 | Variabel "Puskesmas Pengampu" ditaruh di baris Organization.type (26). Seharusnya di baris Organization.name (27), karena yang diisi adalah nama puskesmas | done (mapping/) |
| R5 | Baris 59: path `Organization.address.extension.url` di blok Location. Seharusnya `Location.address.extension.url` (sama dengan temuan Maternal Outcome #4) | done (mapping/) |
| R6 | Baris 18–20 Patient.telecom: "phone" ditaruh di kolom CodeSystem baris `Patient.telecom`. Seharusnya ada baris `Patient.telecom.system` = phone. Baris 19–20 kolom Resource kosong | done (mapping/): baris 18 jadi `Patient.telecom.system` = phone; Resource baris 19–20 diisi Patient |
| R7 | Baris 85: Encounter.class `FLD` tapi display "ambulatory". FLD = field, ambulatory = AMB. Pilih salah satu sesuai jenis kunjungan | done (mapping/): FLD dipertahankan (kunjungan posyandu = lapangan), display jadi "field". Ganti ke AMB kalau ternyata di faskes |
| R8 | Baris 72: typo `EpisodeOfCare.Identifer` → `EpisodeOfCare.identifier` | done (mapping/) |
| R9 | Baris 90: Encounter.participant mereferensi PractitionerRole, tapi tidak ada blok PractitionerRole di dictionary (yang ada hanya Practitioner) | done (mapping/): reference diganti ke Practitioner (bidan desa) |
| R10 | Baris 43, 45: placeholder "Gedung {Tempat yang melayani ANC}" ditaruh di kolom Display. Seharusnya di kolom Definisi Operasional | done (mapping/) |
| R11 | Dictionary Raffle belum punya kolom `jumlah code` dan `jumlah instance` | done (mapping/) |
| R12 | "Input Data" (Observation 385438008: Sigizi / E-pus PKD / E-pus) tidak punya kolom BQ. Apakah nilainya di-hardcode per deployment, atau ada kolom BQ yang belum masuk daftar? | open (perlu konfirmasi) |

## Log perubahan revisi
- 2026-11-13: Raffle R1–R11 done di `mapping/kobo-data-dictionary-raffle.csv`. Tambah R12. Maternal Outcome: nama data entry diisi di Encounter.participant ADM (#9).
- 2026-11-13: Tambah review form Raffle: tally BQ dan temuan R1–R11.
- 2026-11-13: Tambah kolom Nama Column BQ dan tally variabel BQ (12 = 12). Tambah temuan #8.
- 2026-11-13: Semua item open dibetulkan langsung di `mapping/kobo-data-dictionary-maternal-outcome.csv`. Tidak ada item open tersisa.
- 2026-11-13: Cek Kobo_3. #1, #2, #3, #5 dan koreksi instance done. #4 masih salah (path berubah tapi belum benar). Tambah #6, #7, dan koreksi instance #4.
- 2026-11-13: Dibuat dari review Maternal Outcome.
