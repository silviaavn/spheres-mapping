# Output Form: Kobo Neonatus Outcome v2

Sumber: `mapping/phdt-data-dictionary-kobo-neonatus-outcome-v2.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-kobo-neonatus-outcome-v2.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 89 |
| Code (`jumlah code` = 1) | 239 |
| Code unik (code + CodeSystem) | 91 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 57 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–6 | PractitionerRole | – | – | _Siapa yang melakukan entry data?_ → `PractitionerRole.code.coding` (2, tanpa BQ) |
| 2 | 7–11 | Practitioner | – | – | _Nama yang melakukan entry data_ → `Practitioner.name.text` (7, tanpa BQ)<br>_NIK yang melakukan entry data_ → `Practitioner.identifier.value` (8, tanpa BQ)<br>_ID Sahabat Sehat_ → `Practitioner.identifier.value` (10, tanpa BQ) |
| 3 | 12–23 | Encounter | – | – | _Task ID_ → `Encounter.identifier.value` (12, tanpa BQ)<br>_Tanggal konfirmasi/kunjungan_ → `Encounter.period.start` (21, tanpa BQ)<br>_Task ID (Bayi 2)_ → `Encounter.identifier.value` (44, tanpa BQ)<br>_Task ID (Bayi 3)_ → `Encounter.identifier.value` (66, tanpa BQ) |
| 4 | 36–43 | Condition | Z00.1 | Routine child health examination | – |
| 5 | 58–65 | Condition | Z00.1 | Routine child health examination | – |
| 6 | 80–87 | Condition | Z00.1 | Routine child health examination | – |
| 7 | 88–103 | Observation | 89009-5 | Encounter location [Type] | _Lokasi Konfirmasi Data Neonatal Outcome_ → `Observation.valueCodeableConcept.coding` (91, tanpa BQ) |
| 8 | 104–111 | RelatedPerson | – | – | _Nama Ibu_ → `RelatedPerson.name.text` (104, tanpa BQ)<br>_NIK Ibu_ → `RelatedPerson.identifier.value` (105, tanpa BQ)<br>_Tulis nomor HP_ → `RelatedPerson.telecom.value` (107, tanpa BQ) |
| 9 | 112–128 | Observation | SP001121 | Kepemilikan Nomor Telepon | _Nomor HP_ → `Observation.valueBoolean` (115, tanpa BQ)<br>_Alasan_ → `Observation.component.code.coding` (117, tanpa BQ) |
| 10 | 129–143 | Observation | 57071-3 | Obstetric delivery method | _Cara persalinan_ → `Observation.valueCodeableConcept.coding` (132, tanpa BQ) |
| 11 | 144–180 | Observation | 248982007.0 | Pregnancy, childbirth and puerperium finding | _Komplikasi ibu selama kehamilan, persalinan, atau nifas_ → `Observation.component.valueBoolean` (148, tanpa BQ)<br>_Sebutkan komplikasi ibu lainnya_ → `Observation.component.valueString` (172, tanpa BQ) |
| 12 | 181–194 | Observation | SP000389 | Keadaan Ibu | _Keadaan ibu saat ini_ → `Observation.valueCodeableConcept.coding` (184, tanpa BQ) |
| 13 | 196–207 | Observation | 81956-5 | Date and time of death [TimeStamp] | _Tanggal Meninggal Ibu_ → `Observation.valueDateTime` (199, tanpa BQ) |
| 14 | 209–220 | Observation | LT000005 | Alamat Mati | _Tempat Meninggal Ibu_ → `Observation.valueString` (212, tanpa BQ) |
| 15 | 221–232 | Observation | 79378-6 | Cause of death | _Penyebab Meninggal Ibu_ → `Observation.valueString` (224, tanpa BQ) |
| 16 | 233–240 | RelatedPerson | – | – | _Nama Ayah_ → `RelatedPerson.name.text` (233, tanpa BQ)<br>_NIK Ayah_ → `RelatedPerson.identifier.value` (234, tanpa BQ)<br>_Tulis nomor HP_ → `RelatedPerson.telecom.value` (236, tanpa BQ) |
| 17 | 241–257 | Observation | SP001121 | Kepemilikan Nomor Telepon | _Nomor HP_ → `Observation.valueBoolean` (244, tanpa BQ)<br>_Alasan_ → `Observation.component.code.coding` (246, tanpa BQ) |
| 18 | 258–269 | Observation | – | – | – |
| 19 | 270–274 | Consent | – | – | _Apakah ibu/keluarga bersedia dihubungi SPHERES untuk menerima informasi medis penting atau pengingat jadwal pemeriksaan/kontrol?_ → `Consent.category.coding` (270, tanpa BQ) |
| 20 | 275–280 | Patient | – | – | _Siapa anggota keluarga atau wali terdekat yang dapat dihubungi?_ → `Patient.contact.relationship.coding` (275, tanpa BQ)<br>_Apakah bayi kembar?_ → `Patient.multipleBirthBoolean` (330, tanpa BQ)<br>_Nama Bayi_ → `Patient.name.text` (344, tanpa BQ)<br>_Tulis Nomor Induk Kependudukan (NIK)_ → `Patient.identifier.value` (345, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (347, tanpa BQ)<br>_Nama jalan dan nomor rumah (jika ada)_ → `Patient.address.line` (349, tanpa BQ)<br>_Kecamatan_ → `Patient.address.extension.url` (350, tanpa BQ)<br>_Kelurahan_ → `Patient.address.extension.url` (353, tanpa BQ)<br>_Tanggal lahir_ → `Patient.birthDate` (390, tanpa BQ)<br>_Nama Bayi (Bayi 2)_ → `Patient.name.text` (673, tanpa BQ)<br>_Tulis Nomor Induk Kependudukan (NIK) (Bayi 2)_ → `Patient.identifier.value` (674, tanpa BQ)<br>_Jenis Kelamin (Bayi 2)_ → `Patient.gender` (676, tanpa BQ)<br>_Nama jalan dan nomor rumah (jika ada) (Bayi 2)_ → `Patient.address.line` (678, tanpa BQ)<br>_Kecamatan (Bayi 2)_ → `Patient.address.extension.url` (679, tanpa BQ)<br>_Kelurahan (Bayi 2)_ → `Patient.address.extension.url` (682, tanpa BQ)<br>_Tanggal lahir (Bayi 2)_ → `Patient.birthDate` (719, tanpa BQ)<br>_Nama Bayi (Bayi 3)_ → `Patient.name.text` (1002, tanpa BQ)<br>_Tulis Nomor Induk Kependudukan (NIK) (Bayi 3)_ → `Patient.identifier.value` (1003, tanpa BQ)<br>_Jenis Kelamin (Bayi 3)_ → `Patient.gender` (1005, tanpa BQ)<br>_Nama jalan dan nomor rumah (jika ada) (Bayi 3)_ → `Patient.address.line` (1007, tanpa BQ)<br>_Kecamatan (Bayi 3)_ → `Patient.address.extension.url` (1008, tanpa BQ)<br>_Kelurahan (Bayi 3)_ → `Patient.address.extension.url` (1011, tanpa BQ)<br>_Tanggal lahir (Bayi 3)_ → `Patient.birthDate` (1048, tanpa BQ)<br>_Titik koordinat rumah penerima manfaat (beneficiary)_ → `Patient.address.extension.url` (1347, tanpa BQ) |
| 21 | 281–287 | RelatedPerson | – | – | _Siapa nama orang tersebut?_ → `RelatedPerson.name.text` (281, tanpa BQ)<br>_Apa hubungan orang tersebut dengan bayi?_ → `RelatedPerson.relationship.text` (282, tanpa BQ)<br>_Berapa nomor telepon aktif orang tersebut?_ → `RelatedPerson.telecom.value` (284, tanpa BQ) |
| 22 | 288–300 | Observation | SP001121 | Kepemilikan Nomor Telepon | _Apakah orang tersebut memiliki nomor telepon aktif?_ → `Observation.valueBoolean` (291, tanpa BQ) |
| 23 | 301–329 | QuestionnaireResponse | – | – | _Apakah nomor ${kontak_nomor_final} dapat menerima pesan WhatsApp?_ → `QuestionnaireResponse.item.text` (312, tanpa BQ)<br>_Bagaimana hasil percobaan menelepon nomor keluarga/wali tersebut (${kontak_nomor_final}) saat kunjungan ini?_ → `QuestionnaireResponse.item.text` (317, tanpa BQ)<br>_Apakah nomor telepon SPHERES (${nomor_resmi_spheres}) sudah diberikan kepada ibu/keluarga dan mereka sudah diminta menyimpannya dengan nama "SPHERES Dinkes Purbalingga"?_ → `QuestionnaireResponse.item.text` (323, tanpa BQ)<br>_Mengapa nomor SPHERES belum diberikan?_ → `QuestionnaireResponse.item.answer.item.text` (328, tanpa BQ) |
| 24 | 332–343 | Observation | 246435002.0 | Number of fetuses | _Jumlah bayi kembar_ → `Observation.valueInteger` (336, tanpa BQ) |
| 25 | 357–368 | Observation | SP000402 | Kepemilikan Nomor Induk Kependudukan | _Apakah bayi mempunyai Nomor Induk Kependudukan (NIK)_ → `Observation.valueBoolean` (360, tanpa BQ) |
| 26 | 369–386 | Observation | 21842-0 | Birthplace | _Tempat lahir diketahui?_ → `Observation.dataAbsentReason.coding` (372, tanpa BQ)<br>_Tempat lahir_ → `Observation.valueCodeableConcept.coding` (374, tanpa BQ)<br>_Nama Tempat Lahir_ → `Observation.note.text` (386, tanpa BQ) |
| 27 | 391–408 | Observation | 424144002.0 | Current chronological age | _Apakah perkiraan umur bayi saat ini diketahui?_ → `Observation.status` (391, tanpa BQ)<br>_Usia saat ini (dalam minggu)_ → `Observation.component.code.coding` (396, tanpa BQ)<br>_Berapa perkiraan umur bayi saat ini (dalam hari)?_ → `Observation.component.code.coding` (399, tanpa BQ) |
| 28 | 409–429 | Observation | 249222005.0 | Neonatal condition | _Bagaimana kondisi bayi saat konfirmasi ini?_ → `Observation.valueCodeableConcept.coding` (412, tanpa BQ)<br>_Mengapa kondisi bayi belum dapat diketahui?_ → `Observation.component.code.coding` (423, tanpa BQ)<br>_Sebutkan alasan lainnya_ → `Observation.component.valueCodeableConcept.text` (429, tanpa BQ) |
| 29 | 430–442 | Observation | 249222005.0 | Neonatal condition | _Apakah keluarga atau catatan yang tersedia menyebutkan keluhan atau penyakit bayi?_ → `Observation.dataAbsentReason.coding` (433, tanpa BQ)<br>_Apa keluhan atau penyakit bayi menurut keluarga/catatan yang tersedia?_ → `Observation.valueString` (435, tanpa BQ) |
| 30 | 443–450 | Observation | 8339-4 | Birth weight Measured | _Apakah berat bayi saat lahir diketahui?_ → `Observation.dataAbsentReason.coding` (446, tanpa BQ)<br>_Berapa berat bayi saat lahir (gram)?_ → `Observation.valueQuantity.code` (450, tanpa BQ) |
| 31 | 451–462 | Observation | 29463-7 | Body weight | _Berapa berat bayi saat terakhir ditimbang (gram)?_ → `Observation.valueQuantity.value` (454, tanpa BQ)<br>_Kapan bayi terakhir ditimbang?_ → `Observation.effectiveDateTime` (459, tanpa BQ) |
| 32 | 463–487 | Observation | 364586004.0 | State at birth | _Komplikasi atau kondisi bayi saat lahir_ → `Observation.component.valueBoolean` (467, tanpa BQ)<br>_Sebutkan kelainan bawaan, jika diketahui_ → `Observation.note` (478, tanpa BQ)<br>_Sebutkan komplikasi atau kondisi bayi lainnya_ → `Observation.component.valueString` (480, tanpa BQ) |
| 33 | 488–499 | Procedure | 448883004.0 | Injection of vitamin K1 | _Apakah bayi mendapat suntikan vitamin K1 setelah lahir?_ → `Procedure.category.coding` (488, tanpa BQ) |
| 34 | 500–512 | Observation | 427390007.0 | History of hepatitis B vaccination | _Apakah bayi mendapat imunisasi hepatitis B dosis lahir/HB0?_ → `Observation.valueBoolean` (503, tanpa BQ) |
| 35 | 513–527 | Immunization | – | – | – |
| 36 | 528–539 | Procedure | PC000002 | Pemberian Salep Antibiotik Mata | _Apakah bayi mendapat salep/tetes mata dari tenaga kesehatan segera setelah lahir?_ → `Procedure.category.coding` (528, tanpa BQ) |
| 37 | 540–550 | Observation | 81956-5 | Date and time of death [TimeStamp] | _Kapan bayi meninggal?_ → `Observation.valueDateTime` (543, tanpa BQ) |
| 38 | 558–579 | Observation | 39016-1 | Age at death | _(tidak ada label - field tersembunyi/calculate)_ → `Observation.valueQuantity.value` (561, tanpa BQ)<br>_Berapa umur bayi saat meninggal (dalam hari)?_ → `Observation.valueQuantity.value` (562, tanpa BQ)<br>_Berapa umur bayi saat meninggal (dalam jam)?_ → `Observation.component.valueQuantity.value` (565, tanpa BQ) |
| 39 | 580–595 | Observation | OC000028 | Jenis Tempat Meninggal | _Di mana bayi meninggal?_ → `Observation.valueCodeableConcept.coding` (583, tanpa BQ)<br>_Sebutkan lokasi meninggal lainnya_ → `Observation.valueCodeableConcept.text` (588, tanpa BQ) |
| 40 | 596–618 | Observation | SP000098 | Tipe Penyelenggara Faskes Meninggal | _Apa jenis fasilitas kesehatan tempat bayi meninggal?_ → `Observation.valueCodeableConcept.coding` (599, tanpa BQ)<br>_Apa nama Puskesmas tempat bayi meninggal?_ → `Observation.valueCodeableConcept.text` (600, tanpa BQ)<br>_Apa nama Rumah Sakit tempat bayi meninggal?_ → `Observation.valueCodeableConcept.text` (602, tanpa BQ)<br>_Apa nama Praktik Mandiri Bidan/PMB tempat bayi meninggal?_ → `Observation.valueCodeableConcept.text` (604, tanpa BQ)<br>_Apa nama Klinik tempat bayi meninggal?_ → `Observation.valueCodeableConcept.text` (606, tanpa BQ)<br>_Apa nama fasilitas kesehatan tempat bayi meninggal?_ → `Observation.valueCodeableConcept.text` (609, tanpa BQ)<br>_Alamat email Faskes_ → `Observation.note` (618, tanpa BQ) |
| 41 | 622–634 | Observation | 79378-6 | Cause of death | _Apakah keluarga mengetahui penyebab bayi meninggal?_ → `Observation.dataAbsentReason.coding` (625, tanpa BQ)<br>_Menurut keluarga, apa penyebab bayi meninggal?_ → `Observation.valueString` (627, tanpa BQ) |
| 42 | 635–649 | Observation | SP001133 | Pernah diperiksa di fasilitas kesehatan | _Sebelum meninggal, apakah bayi pernah diperiksa atau dirawat di fasilitas kesehatan?_ → `Observation.valueBoolean` (639, tanpa BQ)<br>_Sebelum meninggal, bayi terakhir diperiksa atau dirawat di fasilitas kesehatan mana?_ → `Observation.note` (649, tanpa BQ) |
| 43 | 650–662 | Observation | SP001133 | Pernah diperiksa di fasilitas kesehatan | _Apakah ibu/keluarga menggunakan Buku KIA sebagai sumber informasi saat menjawab pertanyaan dalam form ini?_ → `Observation.valueBoolean` (654, tanpa BQ) |
| 44 | 663–669 | PractitionerRole | – | – | _Jenis tenaga kesehatan yang memeriksa bayi hidup/menyatakan bayi meninggal_ → `PractitionerRole.code.coding` (663, tanpa BQ) |
| 45 | 670–672 | Practitioner | – | – | _Nama lengkap tenaga kesehatan yang memeriksa bayi/menyatakan meninggal_ → `Practitioner.name.text` (670, tanpa BQ)<br>_NIK tenaga kesehatan yang memeriksa bayi/menyatakan meninggal_ → `Practitioner.identifier.value` (671, tanpa BQ) |
| 46 | 686–697 | Observation | SP000402 | Kepemilikan Nomor Induk Kependudukan | _Apakah bayi mempunyai Nomor Induk Kependudukan (NIK) (Bayi 2)_ → `Observation.valueBoolean` (689, tanpa BQ) |
| 47 | 698–715 | Observation | 21842-0 | Birthplace | _Tempat lahir diketahui? (Bayi 2)_ → `Observation.dataAbsentReason.coding` (701, tanpa BQ)<br>_Tempat lahir (Bayi 2)_ → `Observation.valueCodeableConcept.coding` (703, tanpa BQ)<br>_Nama Tempat Lahir (Bayi 2)_ → `Observation.note.text` (715, tanpa BQ) |
| 48 | 720–737 | Observation | 424144002.0 | Current chronological age | _Apakah perkiraan umur bayi saat ini diketahui? (Bayi 2)_ → `Observation.status` (720, tanpa BQ)<br>_Usia saat ini (dalam minggu) (Bayi 2)_ → `Observation.component.code.coding` (725, tanpa BQ)<br>_Berapa perkiraan umur bayi saat ini (dalam hari)? (Bayi 2)_ → `Observation.component.code.coding` (728, tanpa BQ) |
| 49 | 738–758 | Observation | 249222005.0 | Neonatal condition | _Bagaimana kondisi bayi saat konfirmasi ini? (Bayi 2)_ → `Observation.valueCodeableConcept.coding` (741, tanpa BQ)<br>_Mengapa kondisi bayi belum dapat diketahui? (Bayi 2)_ → `Observation.component.code.coding` (752, tanpa BQ)<br>_Sebutkan alasan lainnya (Bayi 2)_ → `Observation.component.valueCodeableConcept.text` (758, tanpa BQ) |
| 50 | 759–771 | Observation | 249222005.0 | Neonatal condition | _Apakah keluarga atau catatan yang tersedia menyebutkan keluhan atau penyakit bayi? (Bayi 2)_ → `Observation.dataAbsentReason.coding` (762, tanpa BQ)<br>_Apa keluhan atau penyakit bayi menurut keluarga/catatan yang tersedia? (Bayi 2)_ → `Observation.valueString` (764, tanpa BQ) |
| 51 | 772–779 | Observation | 8339-4 | Birth weight Measured | _Apakah berat bayi saat lahir diketahui? (Bayi 2)_ → `Observation.dataAbsentReason.coding` (775, tanpa BQ)<br>_Berapa berat bayi saat lahir (gram)? (Bayi 2)_ → `Observation.valueQuantity.code` (779, tanpa BQ) |
| 52 | 780–791 | Observation | 29463-7 | Body weight | _Berapa berat bayi saat terakhir ditimbang (gram)? (Bayi 2)_ → `Observation.valueQuantity.value` (783, tanpa BQ)<br>_Kapan bayi terakhir ditimbang? (Bayi 2)_ → `Observation.effectiveDateTime` (788, tanpa BQ) |
| 53 | 792–816 | Observation | 364586004.0 | State at birth | _Komplikasi atau kondisi bayi saat lahir (Bayi 2)_ → `Observation.component.valueBoolean` (796, tanpa BQ)<br>_Sebutkan kelainan bawaan, jika diketahui (Bayi 2)_ → `Observation.note` (807, tanpa BQ)<br>_Sebutkan komplikasi atau kondisi bayi lainnya (Bayi 2)_ → `Observation.component.valueString` (809, tanpa BQ) |
| 54 | 817–828 | Procedure | 448883004.0 | Injection of vitamin K1 | _Apakah bayi mendapat suntikan vitamin K1 setelah lahir? (Bayi 2)_ → `Procedure.category.coding` (817, tanpa BQ) |
| 55 | 829–841 | Observation | 427390007.0 | History of hepatitis B vaccination | _Apakah bayi mendapat imunisasi hepatitis B dosis lahir/HB0? (Bayi 2)_ → `Observation.valueBoolean` (832, tanpa BQ) |
| 56 | 842–856 | Immunization | – | – | – |
| 57 | 857–868 | Procedure | PC000002 | Pemberian Salep Antibiotik Mata | _Apakah bayi mendapat salep/tetes mata dari tenaga kesehatan segera setelah lahir? (Bayi 2)_ → `Procedure.category.coding` (857, tanpa BQ) |
| 58 | 869–879 | Observation | 81956-5 | Date and time of death [TimeStamp] | _Kapan bayi meninggal? (Bayi 2)_ → `Observation.valueDateTime` (872, tanpa BQ) |
| 59 | 887–908 | Observation | 39016-1 | Age at death | _(tidak ada label - field tersembunyi/calculate) (Bayi 2)_ → `Observation.valueQuantity.value` (890, tanpa BQ)<br>_Berapa umur bayi saat meninggal (dalam hari)? (Bayi 2)_ → `Observation.valueQuantity.value` (891, tanpa BQ)<br>_Berapa umur bayi saat meninggal (dalam jam)? (Bayi 2)_ → `Observation.component.valueQuantity.value` (894, tanpa BQ) |
| 60 | 909–924 | Observation | OC000028 | Jenis Tempat Meninggal | _Di mana bayi meninggal? (Bayi 2)_ → `Observation.valueCodeableConcept.coding` (912, tanpa BQ)<br>_Sebutkan lokasi meninggal lainnya (Bayi 2)_ → `Observation.valueCodeableConcept.text` (917, tanpa BQ) |
| 61 | 925–947 | Observation | SP000098 | Tipe Penyelenggara Faskes Meninggal | _Apa jenis fasilitas kesehatan tempat bayi meninggal? (Bayi 2)_ → `Observation.valueCodeableConcept.coding` (928, tanpa BQ)<br>_Apa nama Puskesmas tempat bayi meninggal? (Bayi 2)_ → `Observation.valueCodeableConcept.text` (929, tanpa BQ)<br>_Apa nama Rumah Sakit tempat bayi meninggal? (Bayi 2)_ → `Observation.valueCodeableConcept.text` (931, tanpa BQ)<br>_Apa nama Praktik Mandiri Bidan/PMB tempat bayi meninggal? (Bayi 2)_ → `Observation.valueCodeableConcept.text` (933, tanpa BQ)<br>_Apa nama Klinik tempat bayi meninggal? (Bayi 2)_ → `Observation.valueCodeableConcept.text` (935, tanpa BQ)<br>_Apa nama fasilitas kesehatan tempat bayi meninggal? (Bayi 2)_ → `Observation.valueCodeableConcept.text` (938, tanpa BQ)<br>_Alamat email Faskes (Bayi 2)_ → `Observation.note` (947, tanpa BQ) |
| 62 | 951–963 | Observation | 79378-6 | Cause of death | _Apakah keluarga mengetahui penyebab bayi meninggal? (Bayi 2)_ → `Observation.dataAbsentReason.coding` (954, tanpa BQ)<br>_Menurut keluarga, apa penyebab bayi meninggal? (Bayi 2)_ → `Observation.valueString` (956, tanpa BQ) |
| 63 | 964–978 | Observation | SP001133 | Pernah diperiksa di fasilitas kesehatan | _Sebelum meninggal, apakah bayi pernah diperiksa atau dirawat di fasilitas kesehatan? (Bayi 2)_ → `Observation.valueBoolean` (968, tanpa BQ)<br>_Sebelum meninggal, bayi terakhir diperiksa atau dirawat di fasilitas kesehatan mana? (Bayi 2)_ → `Observation.note` (978, tanpa BQ) |
| 64 | 979–991 | Observation | SP001133 | Pernah diperiksa di fasilitas kesehatan | _Apakah ibu/keluarga menggunakan Buku KIA sebagai sumber informasi saat menjawab pertanyaan dalam form ini? (Bayi 2)_ → `Observation.valueBoolean` (983, tanpa BQ) |
| 65 | 992–998 | PractitionerRole | – | – | _Jenis tenaga kesehatan yang memeriksa bayi hidup/menyatakan bayi meninggal (Bayi 2)_ → `PractitionerRole.code.coding` (992, tanpa BQ) |
| 66 | 999–1001 | Practitioner | – | – | _Nama lengkap tenaga kesehatan yang memeriksa bayi/menyatakan meninggal (Bayi 2)_ → `Practitioner.name.text` (999, tanpa BQ)<br>_NIK tenaga kesehatan yang memeriksa bayi/menyatakan meninggal (Bayi 2)_ → `Practitioner.identifier.value` (1000, tanpa BQ) |
| 67 | 1015–1026 | Observation | SP000402 | Kepemilikan Nomor Induk Kependudukan | _Apakah bayi mempunyai Nomor Induk Kependudukan (NIK) (Bayi 3)_ → `Observation.valueBoolean` (1018, tanpa BQ) |
| 68 | 1027–1044 | Observation | 21842-0 | Birthplace | _Tempat lahir diketahui? (Bayi 3)_ → `Observation.dataAbsentReason.coding` (1030, tanpa BQ)<br>_Tempat lahir (Bayi 3)_ → `Observation.valueCodeableConcept.coding` (1032, tanpa BQ)<br>_Nama Tempat Lahir (Bayi 3)_ → `Observation.note.text` (1044, tanpa BQ) |
| 69 | 1049–1066 | Observation | 424144002.0 | Current chronological age | _Apakah perkiraan umur bayi saat ini diketahui? (Bayi 3)_ → `Observation.status` (1049, tanpa BQ)<br>_Usia saat ini (dalam minggu) (Bayi 3)_ → `Observation.component.code.coding` (1054, tanpa BQ)<br>_Berapa perkiraan umur bayi saat ini (dalam hari)? (Bayi 3)_ → `Observation.component.code.coding` (1057, tanpa BQ) |
| 70 | 1067–1087 | Observation | 249222005.0 | Neonatal condition | _Bagaimana kondisi bayi saat konfirmasi ini? (Bayi 3)_ → `Observation.valueCodeableConcept.coding` (1070, tanpa BQ)<br>_Mengapa kondisi bayi belum dapat diketahui? (Bayi 3)_ → `Observation.component.code.coding` (1081, tanpa BQ)<br>_Sebutkan alasan lainnya (Bayi 3)_ → `Observation.component.valueCodeableConcept.text` (1087, tanpa BQ) |
| 71 | 1088–1100 | Observation | 249222005.0 | Neonatal condition | _Apakah keluarga atau catatan yang tersedia menyebutkan keluhan atau penyakit bayi? (Bayi 3)_ → `Observation.dataAbsentReason.coding` (1091, tanpa BQ)<br>_Apa keluhan atau penyakit bayi menurut keluarga/catatan yang tersedia? (Bayi 3)_ → `Observation.valueString` (1093, tanpa BQ) |
| 72 | 1101–1108 | Observation | 8339-4 | Birth weight Measured | _Apakah berat bayi saat lahir diketahui? (Bayi 3)_ → `Observation.dataAbsentReason.coding` (1104, tanpa BQ)<br>_Berapa berat bayi saat lahir (gram)? (Bayi 3)_ → `Observation.valueQuantity.code` (1108, tanpa BQ) |
| 73 | 1109–1120 | Observation | 29463-7 | Body weight | _Berapa berat bayi saat terakhir ditimbang (gram)? (Bayi 3)_ → `Observation.valueQuantity.value` (1112, tanpa BQ)<br>_Kapan bayi terakhir ditimbang? (Bayi 3)_ → `Observation.effectiveDateTime` (1117, tanpa BQ) |
| 74 | 1121–1145 | Observation | 364586004.0 | State at birth | _Komplikasi atau kondisi bayi saat lahir (Bayi 3)_ → `Observation.component.valueBoolean` (1125, tanpa BQ)<br>_Sebutkan kelainan bawaan, jika diketahui (Bayi 3)_ → `Observation.note` (1136, tanpa BQ)<br>_Sebutkan komplikasi atau kondisi bayi lainnya (Bayi 3)_ → `Observation.component.valueString` (1138, tanpa BQ) |
| 75 | 1146–1157 | Procedure | 448883004.0 | Injection of vitamin K1 | _Apakah bayi mendapat suntikan vitamin K1 setelah lahir? (Bayi 3)_ → `Procedure.category.coding` (1146, tanpa BQ) |
| 76 | 1158–1170 | Observation | 427390007.0 | History of hepatitis B vaccination | _Apakah bayi mendapat imunisasi hepatitis B dosis lahir/HB0? (Bayi 3)_ → `Observation.valueBoolean` (1161, tanpa BQ) |
| 77 | 1171–1185 | Immunization | – | – | – |
| 78 | 1186–1197 | Procedure | PC000002 | Pemberian Salep Antibiotik Mata | _Apakah bayi mendapat salep/tetes mata dari tenaga kesehatan segera setelah lahir? (Bayi 3)_ → `Procedure.category.coding` (1186, tanpa BQ) |
| 79 | 1198–1208 | Observation | 81956-5 | Date and time of death [TimeStamp] | _Kapan bayi meninggal? (Bayi 3)_ → `Observation.valueDateTime` (1201, tanpa BQ) |
| 80 | 1216–1237 | Observation | 39016-1 | Age at death | _(tidak ada label - field tersembunyi/calculate) (Bayi 3)_ → `Observation.valueQuantity.value` (1219, tanpa BQ)<br>_Berapa umur bayi saat meninggal (dalam hari)? (Bayi 3)_ → `Observation.valueQuantity.value` (1220, tanpa BQ)<br>_Berapa umur bayi saat meninggal (dalam jam)? (Bayi 3)_ → `Observation.component.valueQuantity.value` (1223, tanpa BQ) |
| 81 | 1238–1253 | Observation | OC000028 | Jenis Tempat Meninggal | _Di mana bayi meninggal? (Bayi 3)_ → `Observation.valueCodeableConcept.coding` (1241, tanpa BQ)<br>_Sebutkan lokasi meninggal lainnya (Bayi 3)_ → `Observation.valueCodeableConcept.text` (1246, tanpa BQ) |
| 82 | 1254–1276 | Observation | SP000098 | Tipe Penyelenggara Faskes Meninggal | _Apa jenis fasilitas kesehatan tempat bayi meninggal? (Bayi 3)_ → `Observation.valueCodeableConcept.coding` (1257, tanpa BQ)<br>_Apa nama Puskesmas tempat bayi meninggal? (Bayi 3)_ → `Observation.valueCodeableConcept.text` (1258, tanpa BQ)<br>_Apa nama Rumah Sakit tempat bayi meninggal? (Bayi 3)_ → `Observation.valueCodeableConcept.text` (1260, tanpa BQ)<br>_Apa nama Praktik Mandiri Bidan/PMB tempat bayi meninggal? (Bayi 3)_ → `Observation.valueCodeableConcept.text` (1262, tanpa BQ)<br>_Apa nama Klinik tempat bayi meninggal? (Bayi 3)_ → `Observation.valueCodeableConcept.text` (1264, tanpa BQ)<br>_Apa nama fasilitas kesehatan tempat bayi meninggal? (Bayi 3)_ → `Observation.valueCodeableConcept.text` (1267, tanpa BQ)<br>_Alamat email Faskes (Bayi 3)_ → `Observation.note` (1276, tanpa BQ) |
| 83 | 1280–1292 | Observation | 79378-6 | Cause of death | _Apakah keluarga mengetahui penyebab bayi meninggal? (Bayi 3)_ → `Observation.dataAbsentReason.coding` (1283, tanpa BQ)<br>_Menurut keluarga, apa penyebab bayi meninggal? (Bayi 3)_ → `Observation.valueString` (1285, tanpa BQ) |
| 84 | 1293–1307 | Observation | SP001133 | Pernah diperiksa di fasilitas kesehatan | _Sebelum meninggal, apakah bayi pernah diperiksa atau dirawat di fasilitas kesehatan? (Bayi 3)_ → `Observation.valueBoolean` (1297, tanpa BQ)<br>_Sebelum meninggal, bayi terakhir diperiksa atau dirawat di fasilitas kesehatan mana? (Bayi 3)_ → `Observation.note` (1307, tanpa BQ) |
| 85 | 1308–1320 | Observation | SP001133 | Pernah diperiksa di fasilitas kesehatan | _Apakah ibu/keluarga menggunakan Buku KIA sebagai sumber informasi saat menjawab pertanyaan dalam form ini? (Bayi 3)_ → `Observation.valueBoolean` (1312, tanpa BQ) |
| 86 | 1321–1327 | PractitionerRole | – | – | _Jenis tenaga kesehatan yang memeriksa bayi hidup/menyatakan bayi meninggal (Bayi 3)_ → `PractitionerRole.code.coding` (1321, tanpa BQ) |
| 87 | 1328–1330 | Practitioner | – | – | _Nama lengkap tenaga kesehatan yang memeriksa bayi/menyatakan meninggal (Bayi 3)_ → `Practitioner.name.text` (1328, tanpa BQ)<br>_NIK tenaga kesehatan yang memeriksa bayi/menyatakan meninggal (Bayi 3)_ → `Practitioner.identifier.value` (1329, tanpa BQ) |
| 88 | 1331–1343 | Media | – | – | _Foto kader bersama penerima manfaat (beneficiary)_ → `Media.status` (1331, tanpa BQ)<br>_Foto rumah penerima manfaat (beneficiary)_ → `Media.status` (1339, tanpa BQ) |
| 89 | 1344–1346 | Media | – | – | – |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 60 |
| Procedure | 6 |
| PractitionerRole | 4 |
| Practitioner | 4 |
| Condition | 3 |
| RelatedPerson | 3 |
| Immunization | 3 |
| Media | 2 |
| Encounter | 1 |
| Consent | 1 |
| Patient | 1 |
| QuestionnaireResponse | 1 |
| **Total** | **89** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 2 | PractitionerRole | `PractitionerRole.code.coding` | 223366009.0 | Healthcare professional | http://snomed.info/sct |
| 2 | 3 | PractitionerRole | `PractitionerRole.code.coding` | SP000396 | Data entry staff | http://terminology.kemkes.go.id/sp |
| 3 | 4 | PractitionerRole | `PractitionerRole.code.coding` | SP001120 | Sahabat Sehat | http://terminology.kemkes.go.id/sp |
| 4 | 5 | PractitionerRole | `PractitionerRole.code.coding` | SP000397 | Field/call center staff | http://terminology.kemkes.go.id/sp |
| 5 | 38 | Condition | `Condition.code.coding` | Z00.1 | Routine child health examination | http://hl7.org/fhir/sid/icd-10 |
| 6 | 60 | Condition | `Condition.code.coding` | Z00.1 | Routine child health examination | http://hl7.org/fhir/sid/icd-10 |
| 7 | 82 | Condition | `Condition.code.coding` | Z00.1 | Routine child health examination | http://hl7.org/fhir/sid/icd-10 |
| 8 | 90 | Observation | `Observation.code.coding` | 89009-5 | Encounter location [Type] |  |
| 9 | 91 | Observation | `Observation.valueCodeableConcept.coding` | 264362003.0 | Home | http://snomed.info/sct |
| 10 | 92 | Observation | `Observation.valueCodeableConcept.coding` | 102.0 | Pusat Kesehatan Masyarakat | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 11 | 93 | Observation | `Observation.valueCodeableConcept.coding` | 104.0 | Rumah Sakit | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 12 | 94 | Observation | `Observation.valueCodeableConcept.coding` | 131.0 | Posyandu | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 13 | 95 | Observation | `Observation.valueCodeableConcept.coding` | 103.0 | Klinik | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 14 | 96 | Observation | `Observation.valueCodeableConcept.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 15 | 114 | Observation | `Observation.code.coding` | SP001121 | Kepemilikan Nomor Telepon | http://terminology.kemkes.go.id/sp |
| 16 | 117 | Observation | `Observation.component.code.coding` | SP001122 | Alasan Tidak Ada Nomor Telepon | http://terminology.kemkes.go.id/sp |
| 17 | 118 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000516 | Tidak punya HP | http://terminology.kemkes.go.id/sp |
| 18 | 119 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000517 | HP hilang | http://terminology.kemkes.go.id/sp |
| 19 | 120 | Observation | `Observation.component.valueCodeableConcept.coding` | 397644002.0 | Right to privacy maintained | http://snomed.info/sct |
| 20 | 131 | Observation | `Observation.code.coding` | 57071-3 | Obstetric delivery method | http://loinc.org |
| 21 | 132 | Observation | `Observation.valueCodeableConcept.coding` | 48782003.0 | Delivery normal | http://snomed.info/sct |
| 22 | 133 | Observation | `Observation.valueCodeableConcept.coding` | 200138003.0 | Vacuum extractor delivery - delivered | http://snomed.info/sct |
| 23 | 134 | Observation | `Observation.valueCodeableConcept.coding` | 288266004.0 | Born after induced labor | http://snomed.info/sct |
| 24 | 135 | Observation | `Observation.valueCodeableConcept.coding` | 200144004.0 | Deliveries by cesarean | http://snomed.info/sct |
| 25 | 146 | Observation | `Observation.code.coding` | 248982007.0 | Pregnancy, childbirth and puerperium finding | http://snomed.info/sct |
| 26 | 147 | Observation | `Observation.component.code.coding` | 131148009.0 | Bleeding | http://snomed.info/sct |
| 27 | 150 | Observation | `Observation.component.code.coding` | 48194001.0 | Pregnancy-induced hypertension | http://snomed.info/sct |
| 28 | 153 | Observation | `Observation.component.code.coding` | 40733004.0 | Infectious disease | http://snomed.info/sct |
| 29 | 156 | Observation | `Observation.component.code.coding` | 271737000.0 | Anemia | http://snomed.info/sct |
| 30 | 159 | Observation | `Observation.component.code.coding` | 56265001.0 | Heart disease | http://snomed.info/sct |
| 31 | 162 | Observation | `Observation.component.code.coding` | 19829001.0 | Disorder of lung | http://snomed.info/sct |
| 32 | 165 | Observation | `Observation.component.code.coding` | 44223004.0 | Premature rupture of membranes | http://snomed.info/sct |
| 33 | 168 | Observation | `Observation.component.code.coding` | 14094001.0 | Excessive vomiting in pregnancy | http://snomed.info/sct |
| 34 | 171 | Observation | `Observation.component.code.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 35 | 183 | Observation | `Observation.code.coding` | SP000389 | Keadaan Ibu | http://terminology.kemkes.go.id/sp |
| 36 | 184 | Observation | `Observation.valueCodeableConcept.coding` | 102499006.0 | Fit and well | http://snomed.info/sct |
| 37 | 185 | Observation | `Observation.valueCodeableConcept.coding` | 213257006.0 | Generally unwell | http://snomed.info/sct |
| 38 | 186 | Observation | `Observation.valueCodeableConcept.coding` | 419099009.0 | Dead | http://snomed.info/sct |
| 39 | 198 | Observation | `Observation.code.coding` | 81956-5 | Date and time of death [TimeStamp] | http://loinc.org |
| 40 | 211 | Observation | `Observation.code.coding` | LT000005 | Alamat Mati | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 41 | 223 | Observation | `Observation.code.coding` | 79378-6 | Cause of death | http://loinc.org |
| 42 | 243 | Observation | `Observation.code.coding` | SP001121 | Kepemilikan Nomor Telepon | http://terminology.kemkes.go.id/sp |
| 43 | 246 | Observation | `Observation.component.code.coding` | SP001122 | Alasan Tidak Ada Nomor Telepon | http://terminology.kemkes.go.id/sp |
| 44 | 247 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000516 | Tidak punya HP | http://terminology.kemkes.go.id/sp |
| 45 | 248 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000517 | HP hilang | http://terminology.kemkes.go.id/sp |
| 46 | 249 | Observation | `Observation.component.valueCodeableConcept.coding` | 397644002.0 | Right to privacy maintained | http://snomed.info/sct |
| 47 | 290 | Observation | `Observation.code.coding` | SP001121 | Kepemilikan Nomor Telepon | http://terminology.kemkes.go.id/sp |
| 48 | 313 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | LA33-6 | Yes | http://loinc.org |
| 49 | 314 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | LA32-8 | No | http://loinc.org |
| 50 | 315 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | LA4489-6 | Unknown | http://loinc.org |
| 51 | 318 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001111 | Nomor HP tervalidasi dapat terhubung | http://terminology.kemkes.go.id/sp |
| 52 | 319 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001112 | Nomor HP tervalidasi tidak dapat terhubung | http://terminology.kemkes.go.id/sp |
| 53 | 320 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001113 | Tidak ada nomor HP yang terhubung | http://terminology.kemkes.go.id/sp |
| 54 | 321 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001127 | Nomor HP yang diberikan salah sambung | http://terminology.kemkes.go.id/sp |
| 55 | 324 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | LA19705-5 | Given | http://loinc.org |
| 56 | 325 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | LA19761-8 | Not given | http://loinc.org |
| 57 | 326 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001110 | Tidak ada nomor HP pribadi/suami/istri/orang tua/anak/kader/tetangga | http://terminology.kemkes.go.id/sp |
| 58 | 334 | Observation | `Observation.code.coding` | 246435002.0 | Number of fetuses | http://snomed.info/sct |
| 59 | 335 | Observation | `Observation.code.coding` | ANC.B8.DE109 | Number of fetuses | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 60 | 359 | Observation | `Observation.code.coding` | SP000402 | Kepemilikan Nomor Induk Kependudukan | http://terminology.kemkes.go.id/sp |
| 61 | 371 | Observation | `Observation.code.coding` | 21842-0 | Birthplace | http://loinc.org |
| 62 | 374 | Observation | `Observation.valueCodeableConcept.coding` | 264362003.0 | Home | http://snomed.info/sct |
| 63 | 375 | Observation | `Observation.valueCodeableConcept.coding` | 104.0 | Rumah Sakit | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 64 | 376 | Observation | `Observation.valueCodeableConcept.coding` | 102.0 | Pusat Kesehatan Masyarakat | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 65 | 377 | Observation | `Observation.valueCodeableConcept.coding` | 103.0 | Klinik | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 66 | 378 | Observation | `Observation.valueCodeableConcept.coding` | OT000004 | Bidan Praktek Mandiri | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 67 | 393 | Observation | `Observation.code.coding` | 424144002.0 | Current chronological age | http://snomed.info/sct |
| 68 | 396 | Observation | `Observation.component.code.coding` | SP000715 | Umur Minggu | http://terminology.kemkes.go.id/sp |
| 69 | 399 | Observation | `Observation.component.code.coding` | SP000021 | Umur Hari | http://terminology.kemkes.go.id/sp |
| 70 | 411 | Observation | `Observation.code.coding` | 249222005.0 | Neonatal condition | http://snomed.info/sct |
| 71 | 412 | Observation | `Observation.valueCodeableConcept.coding` | 102500002.0 | Good neonatal condition at birth | http://snomed.info/sct |
| 72 | 413 | Observation | `Observation.valueCodeableConcept.coding` | 276707008.0 | Infant in poor condition at birth | http://terminology.kemkes.go.id/sp |
| 73 | 414 | Observation | `Observation.valueCodeableConcept.coding` | 419099009.0 | Dead | http://snomed.info/sct |
| 74 | 423 | Observation | `Observation.component.code.coding` | C166267 | Unknown Status Reason | http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl |
| 75 | 424 | Observation | `Observation.component.valueCodeableConcept.coding` | C80217 | Not Asked | http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl |
| 76 | 425 | Observation | `Observation.component.valueCodeableConcept.coding` | C192586 | Patient Has Moved Away | http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl |
| 77 | 426 | Observation | `Observation.component.valueCodeableConcept.coding` | C51024 | Response Declined | http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl |
| 78 | 427 | Observation | `Observation.component.valueCodeableConcept.coding` | C54352 | Limited Or No Information | http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl |
| 79 | 428 | Observation | `Observation.component.valueCodeableConcept.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 80 | 432 | Observation | `Observation.code.coding` | 249222005.0 | Neonatal condition | http://snomed.info/sct |
| 81 | 445 | Observation | `Observation.code.coding` | 8339-4 | Birth weight Measured | http://loinc.org |
| 82 | 453 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 83 | 465 | Observation | `Observation.code.coding` | 364586004.0 | State at birth | http://snomed.info/sct |
| 84 | 466 | Observation | `Observation.component.code.coding` | 367494004.0 | Premature birth of newborn | http://snomed.info/sct |
| 85 | 469 | Observation | `Observation.component.code.coding` | 413654009.0 | Birth asphyxia | http://snomed.info/sct |
| 86 | 472 | Observation | `Observation.component.code.coding` | 206376005.0 | Neonatal sepsis | http://snomed.info/sct |
| 87 | 475 | Observation | `Observation.component.code.coding` | 276654001.0 | Congenital malformation | http://snomed.info/sct |
| 88 | 479 | Observation | `Observation.component.code.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 89 | 492 | Procedure | `Procedure.code.coding` | 448883004.0 | Injection of vitamin K1 | http://snomed.info/sct |
| 90 | 502 | Observation | `Observation.code.coding` | 427390007.0 | History of hepatitis B vaccination | http://snomed.info/sct |
| 91 | 516 | Immunization | `Immunization.vaccineCode` | VG45 | HepB | http://sys-ids.kemkes.go.id/kfa |
| 92 | 532 | Procedure | `Procedure.code.coding` | PC000002 | Pemberian Salep Antibiotik Mata | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 93 | 542 | Observation | `Observation.code.coding` | 81956-5 | Date and time of death [TimeStamp] | http://loinc.org |
| 94 | 560 | Observation | `Observation.code.coding` | 39016-1 | Age at death | http://loinc.org |
| 95 | 564 | Observation | `Observation.component.code.coding` | SP000716 | Umur Jam (saat meninggal) | http://terminology.kemkes.go.id/sp |
| 96 | 567 | Observation | `Observation.component.code.coding` | SP000717 | Umur Menit (saat meninggal) | http://terminology.kemkes.go.id/sp |
| 97 | 570 | Observation | `Observation.component.code.coding` | SP000718 | Umur Detik (saat meninggal) | http://terminology.kemkes.go.id/sp |
| 98 | 582 | Observation | `Observation.code.coding` | OC000028 | Jenis Tempat Meninggal | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 99 | 583 | Observation | `Observation.valueCodeableConcept.coding` | SP000099 | Faskes | http://terminology.kemkes.go.id/sp |
| 100 | 584 | Observation | `Observation.valueCodeableConcept.coding` | 264362003.0 | Home | http://snomed.info/sct |
| 101 | 585 | Observation | `Observation.valueCodeableConcept.coding` | LT000008 | Dalam perjalanan dari rumah/masyarakat | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 102 | 586 | Observation | `Observation.valueCodeableConcept.coding` | LT000011 | Belum Tahu | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 103 | 587 | Observation | `Observation.valueCodeableConcept.coding` | LT000010 | Lainnya | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 104 | 598 | Observation | `Observation.code.coding` | SP000098 | Tipe Penyelenggara Faskes Meninggal | http://terminology.kemkes.go.id/sp |
| 105 | 599 | Observation | `Observation.valueCodeableConcept.coding` | 102.0 | Pusat Kesehatan Masyarakat | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 106 | 601 | Observation | `Observation.valueCodeableConcept.coding` | 104.0 | Rumah Sakit | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 107 | 603 | Observation | `Observation.valueCodeableConcept.coding` | OT000004 | Bidan Praktek Mandiri | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 108 | 605 | Observation | `Observation.valueCodeableConcept.coding` | 103.0 | Klinik | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 109 | 607 | Observation | `Observation.valueCodeableConcept.coding` | 264362003.0 | Home | http://snomed.info/sct |
| 110 | 608 | Observation | `Observation.valueCodeableConcept.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 111 | 624 | Observation | `Observation.code.coding` | 79378-6 | Cause of death | http://loinc.org |
| 112 | 637 | Observation | `Observation.code.coding` | SP001133 | Pernah diperiksa di fasilitas kesehatan | http://terminology.kemkes.go.id/sp |
| 113 | 652 | Observation | `Observation.code.coding` | SP001133 | Pernah diperiksa di fasilitas kesehatan | http://terminology.kemkes.go.id/sp |
| 114 | 663 | PractitionerRole | `PractitionerRole.code.coding` | 309453006.0 | Registered midwife | http://snomed.info/sct |
| 115 | 664 | PractitionerRole | `PractitionerRole.code.coding` | 309343006.0 | Physician | http://snomed.info/sct |
| 116 | 665 | PractitionerRole | `PractitionerRole.code.coding` | 309367003.0 | Obstetrician and gynecologist | http://snomed.info/sct |
| 117 | 666 | PractitionerRole | `PractitionerRole.code.coding` | 224535009.0 | Registered nurse | http://snomed.info/sct |
| 118 | 667 | PractitionerRole | `PractitionerRole.code.coding` | SP001120 | Sahabat Sehat | http://terminology.kemkes.go.id/sp |
| 119 | 668 | PractitionerRole | `PractitionerRole.code.coding` | 158999002.0 | Community midwife | http://terminology.kemkes.go.id/sp |
| 120 | 688 | Observation | `Observation.code.coding` | SP000402 | Kepemilikan Nomor Induk Kependudukan | http://terminology.kemkes.go.id/sp |
| 121 | 700 | Observation | `Observation.code.coding` | 21842-0 | Birthplace | http://loinc.org |
| 122 | 703 | Observation | `Observation.valueCodeableConcept.coding` | 264362003.0 | Home | http://snomed.info/sct |
| 123 | 704 | Observation | `Observation.valueCodeableConcept.coding` | 104.0 | Rumah Sakit | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 124 | 705 | Observation | `Observation.valueCodeableConcept.coding` | 102.0 | Pusat Kesehatan Masyarakat | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 125 | 706 | Observation | `Observation.valueCodeableConcept.coding` | 103.0 | Klinik | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 126 | 707 | Observation | `Observation.valueCodeableConcept.coding` | OT000004 | Bidan Praktek Mandiri | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 127 | 722 | Observation | `Observation.code.coding` | 424144002.0 | Current chronological age | http://snomed.info/sct |
| 128 | 725 | Observation | `Observation.component.code.coding` | SP000715 | Umur Minggu | http://terminology.kemkes.go.id/sp |
| 129 | 728 | Observation | `Observation.component.code.coding` | SP000021 | Umur Hari | http://terminology.kemkes.go.id/sp |
| 130 | 740 | Observation | `Observation.code.coding` | 249222005.0 | Neonatal condition | http://snomed.info/sct |
| 131 | 741 | Observation | `Observation.valueCodeableConcept.coding` | 102500002.0 | Good neonatal condition at birth | http://snomed.info/sct |
| 132 | 742 | Observation | `Observation.valueCodeableConcept.coding` | 276707008.0 | Infant in poor condition at birth | http://terminology.kemkes.go.id/sp |
| 133 | 743 | Observation | `Observation.valueCodeableConcept.coding` | 419099009.0 | Dead | http://snomed.info/sct |
| 134 | 752 | Observation | `Observation.component.code.coding` | C166267 | Unknown Status Reason | http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl |
| 135 | 753 | Observation | `Observation.component.valueCodeableConcept.coding` | C80217 | Not Asked | http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl |
| 136 | 754 | Observation | `Observation.component.valueCodeableConcept.coding` | C192586 | Patient Has Moved Away | http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl |
| 137 | 755 | Observation | `Observation.component.valueCodeableConcept.coding` | C51024 | Response Declined | http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl |
| 138 | 756 | Observation | `Observation.component.valueCodeableConcept.coding` | C54352 | Limited Or No Information | http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl |
| 139 | 757 | Observation | `Observation.component.valueCodeableConcept.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 140 | 761 | Observation | `Observation.code.coding` | 249222005.0 | Neonatal condition | http://snomed.info/sct |
| 141 | 774 | Observation | `Observation.code.coding` | 8339-4 | Birth weight Measured | http://loinc.org |
| 142 | 782 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 143 | 794 | Observation | `Observation.code.coding` | 364586004.0 | State at birth | http://snomed.info/sct |
| 144 | 795 | Observation | `Observation.component.code.coding` | 367494004.0 | Premature birth of newborn | http://snomed.info/sct |
| 145 | 798 | Observation | `Observation.component.code.coding` | 413654009.0 | Birth asphyxia | http://snomed.info/sct |
| 146 | 801 | Observation | `Observation.component.code.coding` | 206376005.0 | Neonatal sepsis | http://snomed.info/sct |
| 147 | 804 | Observation | `Observation.component.code.coding` | 276654001.0 | Congenital malformation | http://snomed.info/sct |
| 148 | 808 | Observation | `Observation.component.code.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 149 | 821 | Procedure | `Procedure.code.coding` | 448883004.0 | Injection of vitamin K1 | http://snomed.info/sct |
| 150 | 831 | Observation | `Observation.code.coding` | 427390007.0 | History of hepatitis B vaccination | http://snomed.info/sct |
| 151 | 845 | Immunization | `Immunization.vaccineCode` | VG45 | HepB | http://sys-ids.kemkes.go.id/kfa |
| 152 | 861 | Procedure | `Procedure.code.coding` | PC000002 | Pemberian Salep Antibiotik Mata | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 153 | 871 | Observation | `Observation.code.coding` | 81956-5 | Date and time of death [TimeStamp] | http://loinc.org |
| 154 | 889 | Observation | `Observation.code.coding` | 39016-1 | Age at death | http://loinc.org |
| 155 | 893 | Observation | `Observation.component.code.coding` | SP000716 | Umur Jam (saat meninggal) | http://terminology.kemkes.go.id/sp |
| 156 | 896 | Observation | `Observation.component.code.coding` | SP000717 | Umur Menit (saat meninggal) | http://terminology.kemkes.go.id/sp |
| 157 | 899 | Observation | `Observation.component.code.coding` | SP000718 | Umur Detik (saat meninggal) | http://terminology.kemkes.go.id/sp |
| 158 | 911 | Observation | `Observation.code.coding` | OC000028 | Jenis Tempat Meninggal | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 159 | 912 | Observation | `Observation.valueCodeableConcept.coding` | SP000099 | Faskes | http://terminology.kemkes.go.id/sp |
| 160 | 913 | Observation | `Observation.valueCodeableConcept.coding` | 264362003.0 | Home | http://snomed.info/sct |
| 161 | 914 | Observation | `Observation.valueCodeableConcept.coding` | LT000008 | Dalam perjalanan dari rumah/masyarakat | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 162 | 915 | Observation | `Observation.valueCodeableConcept.coding` | LT000011 | Belum Tahu | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 163 | 916 | Observation | `Observation.valueCodeableConcept.coding` | LT000010 | Lainnya | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 164 | 927 | Observation | `Observation.code.coding` | SP000098 | Tipe Penyelenggara Faskes Meninggal | http://terminology.kemkes.go.id/sp |
| 165 | 928 | Observation | `Observation.valueCodeableConcept.coding` | 102.0 | Pusat Kesehatan Masyarakat | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 166 | 930 | Observation | `Observation.valueCodeableConcept.coding` | 104.0 | Rumah Sakit | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 167 | 932 | Observation | `Observation.valueCodeableConcept.coding` | OT000004 | Bidan Praktek Mandiri | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 168 | 934 | Observation | `Observation.valueCodeableConcept.coding` | 103.0 | Klinik | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 169 | 936 | Observation | `Observation.valueCodeableConcept.coding` | 264362003.0 | Home | http://snomed.info/sct |
| 170 | 937 | Observation | `Observation.valueCodeableConcept.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 171 | 953 | Observation | `Observation.code.coding` | 79378-6 | Cause of death | http://loinc.org |
| 172 | 966 | Observation | `Observation.code.coding` | SP001133 | Pernah diperiksa di fasilitas kesehatan | http://terminology.kemkes.go.id/sp |
| 173 | 981 | Observation | `Observation.code.coding` | SP001133 | Pernah diperiksa di fasilitas kesehatan | http://terminology.kemkes.go.id/sp |
| 174 | 992 | PractitionerRole | `PractitionerRole.code.coding` | 309453006.0 | Registered midwife | http://snomed.info/sct |
| 175 | 993 | PractitionerRole | `PractitionerRole.code.coding` | 309343006.0 | Physician | http://snomed.info/sct |
| 176 | 994 | PractitionerRole | `PractitionerRole.code.coding` | 309367003.0 | Obstetrician and gynecologist | http://snomed.info/sct |
| 177 | 995 | PractitionerRole | `PractitionerRole.code.coding` | 224535009.0 | Registered nurse | http://snomed.info/sct |
| 178 | 996 | PractitionerRole | `PractitionerRole.code.coding` | SP001120 | Sahabat Sehat | http://terminology.kemkes.go.id/sp |
| 179 | 997 | PractitionerRole | `PractitionerRole.code.coding` | 158999002.0 | Community midwife | http://terminology.kemkes.go.id/sp |
| 180 | 1017 | Observation | `Observation.code.coding` | SP000402 | Kepemilikan Nomor Induk Kependudukan | http://terminology.kemkes.go.id/sp |
| 181 | 1029 | Observation | `Observation.code.coding` | 21842-0 | Birthplace | http://loinc.org |
| 182 | 1032 | Observation | `Observation.valueCodeableConcept.coding` | 264362003.0 | Home | http://snomed.info/sct |
| 183 | 1033 | Observation | `Observation.valueCodeableConcept.coding` | 104.0 | Rumah Sakit | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 184 | 1034 | Observation | `Observation.valueCodeableConcept.coding` | 102.0 | Pusat Kesehatan Masyarakat | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 185 | 1035 | Observation | `Observation.valueCodeableConcept.coding` | 103.0 | Klinik | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 186 | 1036 | Observation | `Observation.valueCodeableConcept.coding` | OT000004 | Bidan Praktek Mandiri | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 187 | 1051 | Observation | `Observation.code.coding` | 424144002.0 | Current chronological age | http://snomed.info/sct |
| 188 | 1054 | Observation | `Observation.component.code.coding` | SP000715 | Umur Minggu | http://terminology.kemkes.go.id/sp |
| 189 | 1057 | Observation | `Observation.component.code.coding` | SP000021 | Umur Hari | http://terminology.kemkes.go.id/sp |
| 190 | 1069 | Observation | `Observation.code.coding` | 249222005.0 | Neonatal condition | http://snomed.info/sct |
| 191 | 1070 | Observation | `Observation.valueCodeableConcept.coding` | 102500002.0 | Good neonatal condition at birth | http://snomed.info/sct |
| 192 | 1071 | Observation | `Observation.valueCodeableConcept.coding` | 276707008.0 | Infant in poor condition at birth | http://terminology.kemkes.go.id/sp |
| 193 | 1072 | Observation | `Observation.valueCodeableConcept.coding` | 419099009.0 | Dead | http://snomed.info/sct |
| 194 | 1081 | Observation | `Observation.component.code.coding` | C166267 | Unknown Status Reason | http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl |
| 195 | 1082 | Observation | `Observation.component.valueCodeableConcept.coding` | C80217 | Not Asked | http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl |
| 196 | 1083 | Observation | `Observation.component.valueCodeableConcept.coding` | C192586 | Patient Has Moved Away | http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl |
| 197 | 1084 | Observation | `Observation.component.valueCodeableConcept.coding` | C51024 | Response Declined | http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl |
| 198 | 1085 | Observation | `Observation.component.valueCodeableConcept.coding` | C54352 | Limited Or No Information | http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl |
| 199 | 1086 | Observation | `Observation.component.valueCodeableConcept.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 200 | 1090 | Observation | `Observation.code.coding` | 249222005.0 | Neonatal condition | http://snomed.info/sct |
| 201 | 1103 | Observation | `Observation.code.coding` | 8339-4 | Birth weight Measured | http://loinc.org |
| 202 | 1111 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 203 | 1123 | Observation | `Observation.code.coding` | 364586004.0 | State at birth | http://snomed.info/sct |
| 204 | 1124 | Observation | `Observation.component.code.coding` | 367494004.0 | Premature birth of newborn | http://snomed.info/sct |
| 205 | 1127 | Observation | `Observation.component.code.coding` | 413654009.0 | Birth asphyxia | http://snomed.info/sct |
| 206 | 1130 | Observation | `Observation.component.code.coding` | 206376005.0 | Neonatal sepsis | http://snomed.info/sct |
| 207 | 1133 | Observation | `Observation.component.code.coding` | 276654001.0 | Congenital malformation | http://snomed.info/sct |
| 208 | 1137 | Observation | `Observation.component.code.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 209 | 1150 | Procedure | `Procedure.code.coding` | 448883004.0 | Injection of vitamin K1 | http://snomed.info/sct |
| 210 | 1160 | Observation | `Observation.code.coding` | 427390007.0 | History of hepatitis B vaccination | http://snomed.info/sct |
| 211 | 1174 | Immunization | `Immunization.vaccineCode` | VG45 | HepB | http://sys-ids.kemkes.go.id/kfa |
| 212 | 1190 | Procedure | `Procedure.code.coding` | PC000002 | Pemberian Salep Antibiotik Mata | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 213 | 1200 | Observation | `Observation.code.coding` | 81956-5 | Date and time of death [TimeStamp] | http://loinc.org |
| 214 | 1218 | Observation | `Observation.code.coding` | 39016-1 | Age at death | http://loinc.org |
| 215 | 1222 | Observation | `Observation.component.code.coding` | SP000716 | Umur Jam (saat meninggal) | http://terminology.kemkes.go.id/sp |
| 216 | 1225 | Observation | `Observation.component.code.coding` | SP000717 | Umur Menit (saat meninggal) | http://terminology.kemkes.go.id/sp |
| 217 | 1228 | Observation | `Observation.component.code.coding` | SP000718 | Umur Detik (saat meninggal) | http://terminology.kemkes.go.id/sp |
| 218 | 1240 | Observation | `Observation.code.coding` | OC000028 | Jenis Tempat Meninggal | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 219 | 1241 | Observation | `Observation.valueCodeableConcept.coding` | SP000099 | Faskes | http://terminology.kemkes.go.id/sp |
| 220 | 1242 | Observation | `Observation.valueCodeableConcept.coding` | 264362003.0 | Home | http://snomed.info/sct |
| 221 | 1243 | Observation | `Observation.valueCodeableConcept.coding` | LT000008 | Dalam perjalanan dari rumah/masyarakat | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 222 | 1244 | Observation | `Observation.valueCodeableConcept.coding` | LT000011 | Belum Tahu | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 223 | 1245 | Observation | `Observation.valueCodeableConcept.coding` | LT000010 | Lainnya | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 224 | 1256 | Observation | `Observation.code.coding` | SP000098 | Tipe Penyelenggara Faskes Meninggal | http://terminology.kemkes.go.id/sp |
| 225 | 1257 | Observation | `Observation.valueCodeableConcept.coding` | 102.0 | Pusat Kesehatan Masyarakat | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 226 | 1259 | Observation | `Observation.valueCodeableConcept.coding` | 104.0 | Rumah Sakit | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 227 | 1261 | Observation | `Observation.valueCodeableConcept.coding` | OT000004 | Bidan Praktek Mandiri | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 228 | 1263 | Observation | `Observation.valueCodeableConcept.coding` | 103.0 | Klinik | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 229 | 1265 | Observation | `Observation.valueCodeableConcept.coding` | 264362003.0 | Home | http://snomed.info/sct |
| 230 | 1266 | Observation | `Observation.valueCodeableConcept.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 231 | 1282 | Observation | `Observation.code.coding` | 79378-6 | Cause of death | http://loinc.org |
| 232 | 1295 | Observation | `Observation.code.coding` | SP001133 | Pernah diperiksa di fasilitas kesehatan | http://terminology.kemkes.go.id/sp |
| 233 | 1310 | Observation | `Observation.code.coding` | SP001133 | Pernah diperiksa di fasilitas kesehatan | http://terminology.kemkes.go.id/sp |
| 234 | 1321 | PractitionerRole | `PractitionerRole.code.coding` | 309453006.0 | Registered midwife | http://snomed.info/sct |
| 235 | 1322 | PractitionerRole | `PractitionerRole.code.coding` | 309343006.0 | Physician | http://snomed.info/sct |
| 236 | 1323 | PractitionerRole | `PractitionerRole.code.coding` | 309367003.0 | Obstetrician and gynecologist | http://snomed.info/sct |
| 237 | 1324 | PractitionerRole | `PractitionerRole.code.coding` | 224535009.0 | Registered nurse | http://snomed.info/sct |
| 238 | 1325 | PractitionerRole | `PractitionerRole.code.coding` | SP001120 | Sahabat Sehat | http://terminology.kemkes.go.id/sp |
| 239 | 1326 | PractitionerRole | `PractitionerRole.code.coding` | 158999002.0 | Community midwife | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 89 |
| http://terminology.kemkes.go.id/sp | 57 |
| http://terminology.kemkes.go.id/CodeSystem/organization-type | 28 |
| http://loinc.org | 26 |
| http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl | 15 |
| http://terminology.kemkes.go.id/CodeSystem/location-type | 10 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 6 |
| http://hl7.org/fhir/sid/icd-10 | 3 |
| http://sys-ids.kemkes.go.id/kfa | 3 |
|  | 1 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 1 |
| **Total** | **239** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 24 | – | Jenis Fasilitas Kesehatan | Location | `Location.type.coding` |
| 28 | – | Pilih Nama Puskesmas | Location | `Location.name` |
| 29 | – | Tuliskan nama Rumah Sakit | Location | `Location.name` |
| 30 | – | Tuliskan nama Praktik Mandiri Bidan/ PMB | Location | `Location.name` |
| 31 | – | Tuliskan nama Klinik | Location | `Location.name` |
| 32 | – | Alamat email Faskes | Location | `Location.telecom.value` |
| 387 | – | Tanggal lahir diketahui? | – | `` |
| 551 | – | Apakah umur bayi saat meninggal diketahui? | – | `` |
| 554 | – | Umur bayi saat meninggal dicatat dalam jam atau hari? | – | `` |
| 557 | – | Usia saat meninggal (dalam minggu) | – | `` |
| 619 | – | Apakah nama fasilitas kesehatan tempat bayi meninggal diketahui? | – | `` |
| 716 | – | Tanggal lahir diketahui? (Bayi 2) | – | `` |
| 880 | – | Apakah umur bayi saat meninggal diketahui? (Bayi 2) | – | `` |
| 883 | – | Umur bayi saat meninggal dicatat dalam jam atau hari? (Bayi 2) | – | `` |
| 886 | – | Usia saat meninggal (dalam minggu) (Bayi 2) | – | `` |
| 948 | – | Apakah nama fasilitas kesehatan tempat bayi meninggal diketahui? (Bayi 2) | – | `` |
| 1045 | – | Tanggal lahir diketahui? (Bayi 3) | – | `` |
| 1209 | – | Apakah umur bayi saat meninggal diketahui? (Bayi 3) | – | `` |
| 1212 | – | Umur bayi saat meninggal dicatat dalam jam atau hari? (Bayi 3) | – | `` |
| 1215 | – | Usia saat meninggal (dalam minggu) (Bayi 3) | – | `` |
| 1277 | – | Apakah nama fasilitas kesehatan tempat bayi meninggal diketahui? (Bayi 3) | – | `` |
