# Output Form: SKI - Kesehatan Bayi Balita

Sumber: `mapping/phdt-data-dictionary-ski-bayi-balita.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-ski-bayi-balita.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 5 |
| Code (`jumlah code` = 1) | 4 |
| Code unik (code + CodeSystem) | 4 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 4 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 10–33 | Patient | – | – | _Nama ART_ → `Patient.name.text` (10, tanpa BQ)<br>_No Ktp_ → `Patient.identifier.value` (13, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (15, tanpa BQ)<br>_Tanggal lahir ART_ → `Patient.birthDate` (17, tanpa BQ)<br>_Alamat Domisili_ → `Patient.address.use` (18, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (24, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (27, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.extension.valueCode` (30, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.extension.valueCode` (33, tanpa BQ) |
| 2 | 34–53 | Practitioner | – | – | _ID Sahabat Sehat (3 angka terakhir)_ → `Practitioner.identifier` (34, tanpa BQ)<br>_Nama Practitioner_ → `Practitioner.name.text` (36, tanpa BQ)<br>_Jenis Kelamin_ → `Practitioner.gender` (37, tanpa BQ) |
| 3 | 54–67 | Encounter | – | – | _Start time_ → `Encounter.period.start` (62, tanpa BQ)<br>_Completion time_ → `Encounter.period.end` (63, tanpa BQ)<br>_Start time_ → `Encounter.statusHistory.period.start` (77, tanpa BQ)<br>_Start time_ → `Encounter.statusHistory.period.end` (78, tanpa BQ)<br>_Start time_ → `Encounter.statusHistory.period.start` (80, tanpa BQ)<br>_Completion time_ → `Encounter.statusHistory.period.end` (81, tanpa BQ)<br>_Completion time_ → `Encounter.statusHistory.period.start` (83, tanpa BQ)<br>_Completion time_ → `Encounter.statusHistory.period.end` (84, tanpa BQ) |
| 4 | 68–74 | Condition | – | – | _Start time_ → `Condition.recordedDate` (74, tanpa BQ) |
| 5 | 86–406 | QuestionnaireResponse | – | – | _Jenis Survey_ → `QuestionnaireResponse.identifier.type.coding` (87, tanpa BQ)<br>_Nama ART_ → `QuestionnaireResponse.subject.display` (95, tanpa BQ)<br>_Completion time_ → `QuestionnaireResponse.authored` (96, tanpa BQ)<br>_ID Sahabat Sehat (3 angka terakhir)_ → `QuestionnaireResponse.author.reference` (97, tanpa BQ)<br>_Apakah responden berusia 0-59 bulan (balita)_ → `QuestionnaireResponse.item.item.linkId` (101, tanpa BQ)<br>_Apakah responden memiliki buku KIA._ → `QuestionnaireResponse.item.item.linkId` (107, tanpa BQ)<br>_Informasi apa saja yang terdapat dalam buku KIA responden?_ → `QuestionnaireResponse.item.item.linkId` (115, tanpa BQ)<br>_D03a. Riwayat kehamilan_ → `QuestionnaireResponse.item.item.item.linkId` (117, tanpa BQ)<br>_D03b. Riwayat persalinan_ → `QuestionnaireResponse.item.item.item.linkId` (123, tanpa BQ)<br>_D03c. Riwayat bayi baru lahir_ → `QuestionnaireResponse.item.item.item.linkId` (129, tanpa BQ)<br>_D03d. Pemeriksaan kesehatan pada saat sakit_ → `QuestionnaireResponse.item.item.item.linkId` (135, tanpa BQ)<br>_D03e. Pemantauan pertumbuhan_ → `QuestionnaireResponse.item.item.item.linkId` (141, tanpa BQ)<br>_D03f. Pemantauan perkembangan (SDIDTK)_ → `QuestionnaireResponse.item.item.item.linkId` (147, tanpa BQ)<br>_Apakah Buku KIA dimanfaatkan sebagai sumber informasi tumbuh kembang kesehatan Responden?_ → `QuestionnaireResponse.item.item.linkId` (153, tanpa BQ)<br>_Berapa usia kehamilan ketika Responden dilahirkan?_ → `QuestionnaireResponse.item.item.linkId` (159, tanpa BQ)<br>_Berapa berat badan Responden saat dilahirkan?_ → `QuestionnaireResponse.item.item.linkId` (162, tanpa BQ)<br>_Apa sumber data berat badan Responden saat dilahirkan_ → `QuestionnaireResponse.item.item.linkId` (165, tanpa BQ)<br>_Apakah berat lahir Responden lebih dari atau sama dengan 2500 gram?_ → `QuestionnaireResponse.item.item.linkId` (169, tanpa BQ)<br>_Jika berat lahir Responden kurang dari 2500 gram, tindakan apa yang dilakukan saat itu?_ → `QuestionnaireResponse.item.item.item.linkId` (173, tanpa BQ)<br>_Berapa panjang badan Responden saat dilahirkan?_ → `QuestionnaireResponse.item.item.linkId` (180, tanpa BQ)<br>_Apa sumber data panjang badan Responden saat dilahirkan?_ → `QuestionnaireResponse.item.item.linkId` (183, tanpa BQ)<br>_Berapa lingkar kepala responden saat dilahirkan_ → `QuestionnaireResponse.item.item.linkId` (187, tanpa BQ)<br>_Apa sumber data lingkar kepala Responden saat dilahirkan?_ → `QuestionnaireResponse.item.item.linkId` (190, tanpa BQ)<br>_Apakah Responden dilakukan pemeriksaan bayi baru lahir oleh tenaga kesehatan dalam waktu 6 - 48 jam setelah lahir?_ → `QuestionnaireResponse.item.item.linkId` (196, tanpa BQ)<br>_Di mana Responden diperiksa dalam waktu 6 - 48 jam setelah lahir?_ → `QuestionnaireResponse.item.item.item.linkId` (202, tanpa BQ)<br>_Siapa yang memeriksa Responden dalam waktu 6 - 48 jam setelah lahir?_ → `QuestionnaireResponse.item.item.item.linkId` (213, tanpa BQ)<br>_Apakah Responden dilakukan pemeriksaan bayi baru lahir oleh tenaga kesehatan dalam waktu 3 - 7 hari setelah lahir?_ → `QuestionnaireResponse.item.item.linkId` (221, tanpa BQ)<br>_Di mana responden diperiksa dalam waktu 3 - 7 hari setelah lahir?_ → `QuestionnaireResponse.item.item.item.linkId` (227, tanpa BQ)<br>_Siapa yang memeriksa Responden dalam waktu 3 - 7 hari setelah lahir?_ → `QuestionnaireResponse.item.item.item.linkId` (238, tanpa BQ)<br>_Apakah Responden dilakukan pemeriksaan bayi baru lahir oleh tenaga kesehatan dalam waktu 8 - 28 hari setelah lahir?_ → `QuestionnaireResponse.item.item.linkId` (246, tanpa BQ)<br>_Di mana Responden diperiksa dalam waktu 8 - 28 hari setelah lahir?_ → `QuestionnaireResponse.item.item.item.linkId` (252, tanpa BQ)<br>_Siapa yang memeriksa Responden dalam waktu 8 - 28 hari setelah lahir?_ → `QuestionnaireResponse.item.item.item.linkId` (263, tanpa BQ)<br>_Apakah Responden mendapatkan layanan neonatal berikut dari petugas kesehatan pada 0 - 28 hari?_ → `QuestionnaireResponse.item.item.linkId` (271, tanpa BQ)<br>_D15a. Pengukuran berat badan bayi_ → `QuestionnaireResponse.item.item.item.linkId` (273, tanpa BQ)<br>_D15b. Pengukuran panjang badan bayi_ → `QuestionnaireResponse.item.item.item.linkId` (278, tanpa BQ)<br>_D15c. Pengukuran suhu tubuh bayi_ → `QuestionnaireResponse.item.item.item.linkId` (283, tanpa BQ)<br>_D15d. Perawatan tali pusat bayi_ → `QuestionnaireResponse.item.item.item.linkId` (288, tanpa BQ)<br>_D15e. Pemberian imunisasi Hb-0 kepada bayi_ → `QuestionnaireResponse.item.item.item.linkId` (293, tanpa BQ)<br>_D15f. Pemberian vitamin K kepada bayi_ → `QuestionnaireResponse.item.item.item.linkId` (298, tanpa BQ)<br>_D15g. Pemberian salep mata_ → `QuestionnaireResponse.item.item.item.linkId` (303, tanpa BQ)<br>_D15h. Menanyakan status kesehatan_ → `QuestionnaireResponse.item.item.item.linkId` (308, tanpa BQ)<br>_D15i. Memberitahu cara pemberian ASI yang baik_ → `QuestionnaireResponse.item.item.item.linkId` (313, tanpa BQ)<br>_D15j. Menanyakan masalah dalam pemberian ASI_ → `QuestionnaireResponse.item.item.item.linkId` (318, tanpa BQ)<br>_D15k. Menanyakan bayi mengalami diare atau tidak_ → `QuestionnaireResponse.item.item.item.linkId` (323, tanpa BQ)<br>_D15l. Memberitahukan mengenai tanda bahaya pada bayi_ → `QuestionnaireResponse.item.item.item.linkId` (328, tanpa BQ)<br>_Apa yang dilakukan dalam perawatan tali pusat Responden saat baru lahir?_ → `QuestionnaireResponse.item.item.linkId` (333, tanpa BQ)<br>_Apakah Responden mempunyai kelainan bawaan sejak lahir?_ → `QuestionnaireResponse.item.item.linkId` (340, tanpa BQ)<br>_D19a. Kaki pengkor_ → `QuestionnaireResponse.item.item.item.linkId` (342, tanpa BQ)<br>_D19b. Hidrosefalus_ → `QuestionnaireResponse.item.item.item.linkId` (349, tanpa BQ)<br>_D19c. Bibir sumbing_ → `QuestionnaireResponse.item.item.item.linkId` (356, tanpa BQ)<br>_D19d. Kembar siam_ → `QuestionnaireResponse.item.item.item.linkId` (363, tanpa BQ)<br>_D19e. Tidak punya lubang anus_ → `QuestionnaireResponse.item.item.item.linkId` (370, tanpa BQ)<br>_D19f. Down syndrome_ → `QuestionnaireResponse.item.item.item.linkId` (377, tanpa BQ)<br>_D19g. Kelainan jantung bawaan_ → `QuestionnaireResponse.item.item.item.linkId` (384, tanpa BQ)<br>_D19h. Thalasemia_ → `QuestionnaireResponse.item.item.item.linkId` (391, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Patient | 1 |
| Practitioner | 1 |
| Encounter | 1 |
| Condition | 1 |
| QuestionnaireResponse | 1 |
| **Total** | **5** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 87 | QuestionnaireResponse | `QuestionnaireResponse.identifier.type.coding` | SP000834 | Survei umum | http://terminology.kemkes.go.id/sp |
| 2 | 88 | QuestionnaireResponse | `QuestionnaireResponse.identifier.type.coding` | SP000835 | Survei umum crosscheck | http://terminology.kemkes.go.id/sp |
| 3 | 89 | QuestionnaireResponse | `QuestionnaireResponse.identifier.type.coding` | SP000836 | Survei ibu hamil | http://terminology.kemkes.go.id/sp |
| 4 | 90 | QuestionnaireResponse | `QuestionnaireResponse.identifier.type.coding` | SP000837 | Survei ibu hamil crosscheck | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://terminology.kemkes.go.id/sp | 4 |
| **Total** | **4** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 2 | – | Response Id | – | `` |
| 3 | – | Survey Id | – | `` |
| 4 | – | Completion time | – | `` |
| 7 | – | Sync time | – | `` |
| 8 | – | Nama ART (konfirmasi) | – | `` |
| 9 | – | ID rumah (dari DWS) | – | `` |
