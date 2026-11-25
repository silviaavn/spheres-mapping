# Output Form: Kobo Buku KIA 3 - PNC

Sumber: `mapping/phdt-data-dictionary-kobo-kia3-pnc.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-kobo-kia3-pnc.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 75 |
| Code (`jumlah code` = 1) | 175 |
| Code unik (code + CodeSystem) | 150 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 26 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 3–14 | Observation | SP000395 | Pendaftaran Pertama Formulir KoBo | _Apakah ini pendaftaran di KoBo form PNC pertama kali?_ → `Observation.valueBoolean` (6, tanpa BQ) |
| 2 | 15–19 | PractitionerRole | – | – | _Siapa yang melakukan entry data?_ → `PractitionerRole.active` (15, tanpa BQ) |
| 3 | 20–23 | Practitioner | – | – | _Nama lengkap tenaga kesehatan yang memberikan pelayanan kesehatan_ → `Practitioner.name.text` (20, tanpa BQ)<br>_ID tenaga kesehatan yang memberikan pelayanan kesehatan_ → `Practitioner.identifier` (21, tanpa BQ)<br>_ID SID staff yang melakukan entry data_ → `Practitioner.identifier` (22, tanpa BQ)<br>_ID SID field staff yang mengumpulkan form_ → `Practitioner.identifier` (23, tanpa BQ) |
| 4 | 41–88 | Patient | – | – | _Nama depan ibu_ → `Patient.name.text` (41, tanpa BQ)<br>_Nama belakang ibu_ → `Patient.name.text` (42, tanpa BQ)<br>_Tulis Nomor Induk Kependudukan (NIK)_ → `Patient.identifier.use` (43, tanpa BQ)<br>_Tulis Nomor Induk Kependudukan (NIK) (Tulis kedua kali)_ → `Patient.identifier.value` (45, tanpa BQ)<br>_Tanggal lahir ibu_ → `Patient.birthDate` (48, tanpa BQ)<br>_(Provinsi)_ → `Patient.address.extension.extension.valueCode` (51, tanpa BQ)<br>_(Kabupaten)_ → `Patient.address.extension.extension.valueCode` (54, tanpa BQ)<br>_Kecamatan_ → `Patient.address.extension.extension.valueCode` (58, tanpa BQ)<br>_Kelurahan_ → `Patient.address.extension.extension.valueCode` (61, tanpa BQ)<br>_RW_ → `Patient.address.extension.extension.valueCode` (64, tanpa BQ)<br>_RT_ → `Patient.address.extension.extension.valueCode` (67, tanpa BQ)<br>__Tautan GPS rumah_latitude_ → `Patient.address.extension.extension.valueCode` (71, tanpa BQ)<br>__Tautan GPS rumah_longitude_ → `Patient.address.extension.extension.valueCode` (74, tanpa BQ)<br>__Tautan GPS rumah_altitude_ → `Patient.address.extension.extension.valueCode` (77, tanpa BQ)<br>_Nama jalan dan nomor rumah (jika ada)_ → `Patient.address.line` (80, tanpa BQ)<br>_Tulis nomor HP_ → `Patient.telecom` (86, tanpa BQ)<br>_Nama depan bayi_ → `Patient.name.text` (794, tanpa BQ)<br>_Nama belakang bayi_ → `Patient.name.text` (795, tanpa BQ)<br>_(NIK bayi)_ → `Patient.identifier.use` (796, tanpa BQ)<br>_(NIK Ibu)_ → `Patient.identifier.use` (799, tanpa BQ)<br>_Tanggal lahir anak_ → `Patient.birthDate` (802, tanpa BQ)<br>_Jenis kelamin_ → `Patient.gender` (806, tanpa BQ) |
| 5 | 92–103 | Observation | – | – | _Apakah mempunyai Nomor Induk Kependudukan (NIK)_ → `Observation.valueBoolean` (95, tanpa BQ) |
| 6 | 104–117 | Observation | SP000403 | Alasan Tidak Ada Nomor Induk Kependudukan | _Pilih alasan_ → `Observation.valueCodeableConcept.coding` (107, tanpa BQ) |
| 7 | 121–133 | Observation | – | – | _Apakah Ibu terdaftar sebagai anggota BPJS?_ → `Observation.valueBoolean` (124, tanpa BQ) |
| 8 | 134–143 | Coverage | – | – | _Nomor BPJS Kesehatan_ → `Coverage.subscriberId` (134, tanpa BQ)<br>_Status keanggotaan BPJS_ → `Coverage.identifier` (136, tanpa BQ) |
| 9 | 144–155 | Observation | 424144002 | Current chronological age | _age_calc_ → `Observation.status` (144, tanpa BQ)<br>_Usia ibu_ → `Observation.valueQuantity.value` (147, tanpa BQ) |
| 10 | 156–183 | Observation | SP000409 | Rekan Serumah | _Rekan serumah_ → `Observation.status` (156, tanpa BQ)<br>_Rekan serumah/Orang tua_ → `Observation.component.code.coding` (159, tanpa BQ)<br>_Rekan serumah/Saudara (kakak atau adik)_ → `Observation.component.code.coding` (162, tanpa BQ)<br>_Rekan serumah/Keluarga besar_ → `Observation.component.code.coding` (165, tanpa BQ)<br>_Rekan serumah/Pasangan_ → `Observation.component.code.coding` (168, tanpa BQ)<br>_Rekan serumah/Teman_ → `Observation.component.code.coding` (171, tanpa BQ)<br>_Rekan serumah/Tinggal sendiri_ → `Observation.component.code.coding` (174, tanpa BQ) |
| 11 | 184–196 | Observation | 719051004 | Quantity of postpartum maternal blood loss | _Perdarahan kala IV 2 jam postpartum_ → `Observation.valueRange.high.value` (188, tanpa BQ) |
| 12 | 197–214 | Observation | OC000013 | Penolong Persalinan | _Penolong persalinan_ → `Observation.valueCodeableConcept.coding` (200, tanpa BQ)<br>_Penolong lain-lain_ → `Observation.valueCodeableConcept.text` (207, tanpa BQ) |
| 13 | 216–227 | Observation | OC000016 | Waktu Inisiasi Menyusui Dini | _Pelayanan/IMD < 1 jam_ → `Observation.valueCodeableConcept.coding` (218, tanpa BQ)<br>_Pelayanan/IMD ≥ 1 jam_ → `Observation.valueCodeableConcept.coding` (219, tanpa BQ) |
| 14 | 228–238 | Procedure | SP000130 | Menggunakan Partograf | _Pelayanan/Menggunakan partograf_ → `Procedure.category.coding` (228, tanpa BQ) |
| 15 | 239–251 | Observation | SP000122 | Catat di Buku KIA | _Pelayanan/Pencatatan di buku KIA_ → `Observation.valueBoolean` (241, tanpa BQ) |
| 16 | 253–263 | Condition | 199746004 | Obstructed labor | _Jenis komplikasi_ → `Condition.category.coding` (254, tanpa BQ)<br>_Jenis komplikasi/Distosia bahu_ → `Condition.code.coding` (255, tanpa BQ)<br>_Jenis komplikasi/Hipertensi dalam kehamilan_ → `Condition.code.coding` (256, tanpa BQ)<br>_Jenis komplikasi/Perdarahan postpartum_ → `Condition.code.coding` (257, tanpa BQ)<br>_Jenis komplikasi/Infeksi_ → `Condition.code.coding` (258, tanpa BQ)<br>_Jenis komplikasi/Sepsis maternal_ → `Condition.code.coding` (259, tanpa BQ)<br>_Jenis komplikasi/Preeklampsia_ → `Condition.code.coding` (260, tanpa BQ)<br>_Jenis komplikasi/Eklampsia_ → `Condition.code.coding` (261, tanpa BQ)<br>_Jenis komplikasi/Lain-lain_ → `Condition.code.coding` (262, tanpa BQ)<br>_Komplikasi lain-lain_ → `Condition.code.text` (263, tanpa BQ) |
| 17 | 264–276 | Observation | SP000127 | Tatalaksana Komplikasi Persalinan | _Penanganan diberikan?_ → `Observation.valueBoolean` (267, tanpa BQ)<br>_Deskripsikan penanganan yang diberikan_ → `Observation.note` (276, tanpa BQ) |
| 18 | 277–293 | ServiceRequest | 409014006 | Delivery care management | _Dirujuk ke_ → `ServiceRequest.status` (277, tanpa BQ) |
| 19 | 294–296 | ServiceRequest | 185389009 | Follow-up visit | _Dirujuk ke lain-lain_ → `ServiceRequest.locationCode.text` (296, tanpa BQ) |
| 20 | 297–325 | Encounter | – | – | _Nama Posyandu/ Polindes / Puskesmas / Rumah Sakit_ → `Encounter.location.location.display` (316, tanpa BQ)<br>_Lokasi periksa lainnya_ → `Encounter.location.location.display` (317, tanpa BQ)<br>_Tanggal kunjungan_ → `Encounter.period.start` (318, tanpa BQ)<br>_Hari ke-/ KF_ → `Encounter.identifier` (320, tanpa BQ)<br>_Nama Posyandu/ Polindes / Puskesmas / Rumah Sakit_ → `Encounter.location.location.display` (819, tanpa BQ)<br>_Lokasi periksa lainnya_ → `Encounter.location.location.display` (820, tanpa BQ)<br>_Kunjungan Neonatal/KN 1 (6-48 jam)_ → `Encounter.identifier` (823, tanpa BQ)<br>_Kunjungan Neonatal/KN 2 (3-7 hari)_ → `Encounter.identifier` (824, tanpa BQ)<br>_Kunjungan Neonatal/KN 3 (8-28 hari)_ → `Encounter.identifier` (825, tanpa BQ)<br>_Tanggal kunjungan_ → `Encounter.period.start` (833, tanpa BQ) |
| 21 | 326–333 | Condition | Z39.2 | Routine postpartum follow-up | – |
| 22 | 344–352 | EpisodeOfCare | PNC | Postnatal Care | _Tanggal lahir anak_ → `EpisodeOfCare.period.start` (348, tanpa BQ) |
| 23 | 353–360 | Condition | 359746009 | Patient's condition stable | _Keadaan ibu nifas_ → `Condition.clinicalStatus.coding` (353, tanpa BQ) |
| 24 | 361–372 | Observation | 8480-6 | Systolic blood pressure | _Tekanan darah sistolik (mmHg)_ → `Observation.valueQuantity.value` (364, tanpa BQ) |
| 25 | 373–384 | Observation | 8462-4 | Diastolic blood pressure | _Tekanan darah diastolik (mmHg)_ → `Observation.valueQuantity.value` (376, tanpa BQ) |
| 26 | 385–396 | Observation | 8310-5 | Body temperature | _Suhu tubuh (c)_ → `Observation.valueQuantity.value` (388, tanpa BQ) |
| 27 | 397–408 | Observation | 8867-4 | Heart rate | _Denyut nadi (kpm)_ → `Observation.valueQuantity.value` (400, tanpa BQ) |
| 28 | 409–420 | Observation | 9279-1 | Respiratory rate | _Pernapasan_ → `Observation.valueQuantity.value` (412, tanpa BQ) |
| 29 | 421–432 | Observation | 32422-8 | Physical findings of breast | _Pembengkakan payudara_ → `Observation.valueCodeableConcept.coding` (424, tanpa BQ) |
| 30 | 433–444 | Observation | OC000017 | Produksi ASI | _Produksi ASI_ → `Observation.valueCodeableConcept.coding` (436, tanpa BQ) |
| 31 | 445–456 | Observation | 11881-0 | Uterus Fundal height Tape measure | _Tinggi Fundus Uteri (TFU)_ → `Observation.valueQuantity.value` (448, tanpa BQ) |
| 32 | 457–468 | Observation | 289700000 | Uterine contractions present | _Kontraksi uterus_ → `Observation.valueBoolean` (460, tanpa BQ) |
| 33 | 471–482 | Observation | 252041008 | Micturition finding | _Buang air kecil_ → `Observation.valueCodeableConcept.coding` (474, tanpa BQ) |
| 34 | 483–494 | Observation | 300375001 | Able to defecate | _Buang air besar_ → `Observation.valueBoolean` (486, tanpa BQ) |
| 35 | 495–506 | Observation | OC000025 | Tanda Infeksi Luka Jahitan Sectio Caesaria | _Luka operasi_ → `Observation.valueBoolean` (498, tanpa BQ) |
| 36 | 507–520 | Observation | 249214003 | Color of lochia | _Lokia_ → `Observation.valueCodeableConcept.coding` (510, tanpa BQ) |
| 37 | 521–527 | Condition | 289530006 | Vaginal bleeding | _Perdarahan_ → `Condition.clinicalStatus.coding` (521, tanpa BQ) |
| 38 | 528–540 | Observation | OC000020 | Tanda Infeksi Perineum | _Hasil pemeriksaan luka perineum_ → `Observation.valueCodeableConcept.coding` (531, tanpa BQ) |
| 39 | 541–574 | MedicationRequest | 92000653 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula | _Pelayanan tablet tambah darah (Fe)_ → `MedicationRequest.contained.resourceType` (541, tanpa BQ) |
| 40 | 575–607 | MedicationDispense | 93015491 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | _Jika ya, jumlah tablet tambah darah (Fe) yang diberikan_ → `MedicationDispense.quantity.value` (604, tanpa BQ) |
| 41 | 608–618 | Procedure | 767224000 | Administration of vitamin A | _Vitamin A 2 Jam PP_ → `Procedure.category.coding` (608, tanpa BQ) |
| 42 | 619–629 | Procedure | 767224000 | Administration of vitamin A | _Vitamin A 24 Jam PP_ → `Procedure.category.coding` (619, tanpa BQ) |
| 43 | 630–642 | Condition | 211063003 | Infected abrasion of perineum | _Komplikasi_ → `Condition.clinicalStatus.coding` (630, tanpa BQ)<br>_Komplikasi/Infeksi nifas_ → `Condition.code.coding` (633, tanpa BQ)<br>_Komplikasi/Hipertensi post partum_ → `Condition.code.coding` (634, tanpa BQ)<br>_Komplikasi/Perdarahan postpartum_ → `Condition.code.coding` (635, tanpa BQ)<br>_Komplikasi/Mastitis_ → `Condition.code.coding` (636, tanpa BQ)<br>_Komplikasi/Lain-lain_ → `Condition.code.coding` (637, tanpa BQ)<br>_Komplikasi lain-lain_ → `Condition.code.text` (638, tanpa BQ) |
| 44 | 643–655 | Observation | SP000381 | Tatalaksana Komplikasi Infeksi | _Penanganan diberikan_ → `Observation.valueBoolean` (646, tanpa BQ)<br>_Deskripsikan penanganan yang diberikan_ → `Observation.note` (655, tanpa BQ) |
| 45 | 656–668 | Observation | 736286003 | Hypertension clinical management plan | _Penanganan diberikan_ → `Observation.valueBoolean` (659, tanpa BQ)<br>_Deskripsikan penanganan yang diberikan_ → `Observation.note` (668, tanpa BQ) |
| 46 | 669–681 | Observation | SP000380 | Tatalaksana Komplikasi Pendarahan | _Penanganan diberikan_ → `Observation.valueBoolean` (672, tanpa BQ)<br>_Deskripsikan penanganan yang diberikan_ → `Observation.note` (681, tanpa BQ) |
| 47 | 682–694 | Observation | SP000382 | Tatalaksana Komplikasi Mastitis | _Penanganan diberikan_ → `Observation.valueBoolean` (685, tanpa BQ)<br>_Deskripsikan penanganan yang diberikan_ → `Observation.note` (694, tanpa BQ) |
| 48 | 697–717 | ServiceRequest | 409014006 | Delivery care management | _Jika iya, rujuk ke_ → `ServiceRequest.status` (697, tanpa BQ)<br>_Dirujuk ke lainnya_ → `ServiceRequest.locationCode.text` (717, tanpa BQ) |
| 49 | 718–729 | Observation | SP000383 | Keadaan Ibu Saat Tiba | _Keadaan ibu saat tiba_ → `Observation.valueCodeableConcept.coding` (721, tanpa BQ) |
| 50 | 730–741 | Observation | SP000384 | Keadaan Ibu Saat Pulang | _Keadaan ibu saat pulang_ → `Observation.valueCodeableConcept.coding` (733, tanpa BQ) |
| 51 | 742–760 | Observation | PC000004 | KB Pasca Persalinan | _Metode kontrasepsi yang digunakan_ → `Observation.valueCodeableConcept.coding` (745, tanpa BQ) |
| 52 | 761–779 | Observation | 86651-7 | Birth control method at exit Reported --at exit | _Jika tidak ada, rencana kontrasepsi yang akan digunakan_ → `Observation.valueCodeableConcept.coding` (764, tanpa BQ) |
| 53 | 780–790 | Observation | 86653-3 | Reason for no birth control use - Reported --at exit | _Jika tidak ada rencana, sebutkan alasan_ → `Observation.valueString` (783, tanpa BQ) |
| 54 | 837–844 | Condition | Z00.1 | Routine child health examination | – |
| 55 | 854–862 | EpisodeOfCare | Neonate | Neonate | – |
| 56 | 863–881 | Condition | 102500002 | Good neonatal condition at birth | _Tanda bahaya_ → `Condition.clinicalStatus.coding` (863, tanpa BQ) |
| 57 | 882–893 | Observation | 63895-7 | Breastfeeding status | _Menyusu_ → `Observation.valueBoolean` (885, tanpa BQ) |
| 58 | 894–903 | Procedure | 431868002 | Initiation of breastfeeding | _Jenis pelayanan yang diberikan_ → `Procedure.category.coding` (894, tanpa BQ) |
| 59 | 904–913 | Procedure | 448883004 | Injection of vitamin K1 | – |
| 60 | 914–923 | Procedure | PC000002 | Pemberian Salep Antibiotik Mata | – |
| 61 | 924–933 | Procedure | 400984005 | Congenital hypothyroidism screening test | – |
| 62 | 934–944 | Procedure | 408989004 | Newborn care management | _Jenis pelayanan lainnya yang diberikan_ → `Procedure.code.text` (937, tanpa BQ) |
| 63 | 945–956 | Observation | 8345-1 | Body weight Measured --post partum | _Berat badan_ → `Observation.valueQuantity.value` (948, tanpa BQ) |
| 64 | 957–968 | Observation | 8306-3 | Body height --lying | _Panjang badan (cm)_ → `Observation.valueQuantity.value` (960, tanpa BQ) |
| 65 | 969–980 | Observation | 9843-4 | Head Occipital-frontal circumference | _Lingkar kepala (cm)_ → `Observation.valueQuantity.value` (972, tanpa BQ) |
| 66 | 981–992 | Observation | 8310-5 | Body temperature | _Suhu tubuh (c)_ → `Observation.valueQuantity.value` (984, tanpa BQ) |
| 67 | 993–1004 | Observation | 9279-1 | Respiratory rate | _Laju pernapasan (kpm)_ → `Observation.valueQuantity.value` (996, tanpa BQ) |
| 68 | 1005–1016 | Observation | 8867-4 | Heart rate | _Frekuensi jantung (kpm)_ → `Observation.valueQuantity.value` (1008, tanpa BQ) |
| 69 | 1017–1029 | Observation | 249229001 | Finding of umbilical stump | _Kondisi tali pusat_ → `Observation.valueCodeableConcept.coding` (1020, tanpa BQ) |
| 70 | 1030–1045 | Observation | 267030001 | Yellow or jaundiced color | _Identifikasi kuning_ → `Observation.valueCodeableConcept.coding` (1033, tanpa BQ) |
| 71 | 1046–1076 | Observation | 249222005 | Neonatal condition | _Kondisi bayi_ → `Observation.valueCodeableConcept.coding` (1049, tanpa BQ)<br>_Jika sakit_ → `Observation.component.code.coding` (1059, tanpa BQ)<br>_Jika lainnya_ → `Observation.component.valueString` (1076, tanpa BQ) |
| 72 | 1077–1088 | Observation | 81956-5 | Date and time of death [TimeStamp] | _Tanggal Meninggal_ → `Observation.valueDateTime` (1080, tanpa BQ) |
| 73 | 1089–1103 | Immunization | – | – | _Pemberian Imunisiasi HB0_ → `Immunization.status` (1089, tanpa BQ)<br>_Jika belum, alasan_ → `Immunization.statusReason.text` (1103, tanpa BQ) |
| 74 | 1105–1115 | ServiceRequest | 736282001 | Neonatal critical care plan | – |
| 75 | 1116–1126 | Procedure | 408989004 | Newborn care management | _Komplikasi tertangani_ → `Procedure.category.coding` (1116, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 45 |
| Procedure | 9 |
| Condition | 7 |
| ServiceRequest | 4 |
| EpisodeOfCare | 2 |
| PractitionerRole | 1 |
| Practitioner | 1 |
| Patient | 1 |
| Coverage | 1 |
| Encounter | 1 |
| MedicationRequest | 1 |
| MedicationDispense | 1 |
| Immunization | 1 |
| **Total** | **75** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 5 | Observation | `Observation.code.coding` | SP000395 | Pendaftaran Pertama Formulir KoBo | http://terminology.kemkes.go.id/sp |
| 2 | 16 | PractitionerRole | `PractitionerRole.code.coding` | 223366009 | Healthcare professional | http://snomed.info/sct |
| 3 | 17 | PractitionerRole | `PractitionerRole.code.coding` | SP000396 | Data entry staff | http://terminology.kemkes.go.id/sp |
| 4 | 18 | PractitionerRole | `PractitionerRole.code.coding` | SP000397 | Field/call center staff | http://terminology.kemkes.go.id/sp |
| 5 | 106 | Observation | `Observation.code.coding` | SP000403 | Alasan Tidak Ada Nomor Induk Kependudukan | http://terminology.kemkes.go.id/sp |
| 6 | 107 | Observation | `Observation.valueCodeableConcept.coding` | SP000404 | Tidak Punya Kartu Tanda Penduduk | http://terminology.kemkes.go.id/sp |
| 7 | 108 | Observation | `Observation.valueCodeableConcept.coding` | SP000405 | Tidak Membawa Kartu Tanda Penduduk | http://terminology.kemkes.go.id/sp |
| 8 | 109 | Observation | `Observation.valueCodeableConcept.coding` | SP000406 | Kartu Tanda Penduduk Hilang | http://terminology.kemkes.go.id/sp |
| 9 | 110 | Observation | `Observation.valueCodeableConcept.coding` | 397644002 | Right to privacy maintained | http://snomed.info/sct |
| 10 | 126 | Observation | `Observation.dataAbsentReason.coding` | unknown | Unknown | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 11 | 146 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 12 | 158 | Observation | `Observation.code.coding` | SP000409 | Rekan Serumah | http://terminology.kemkes.go.id/sp |
| 13 | 159 | Observation | `Observation.component.code.coding` | 40683002 | Parent | http://snomed.info/sct |
| 14 | 162 | Observation | `Observation.component.code.coding` | 375005 | Sibling | http://snomed.info/sct |
| 15 | 165 | Observation | `Observation.component.code.coding` | 303071001 | Family member | http://snomed.info/sct |
| 16 | 168 | Observation | `Observation.component.code.coding` | 127848009 | Spouse | http://snomed.info/sct |
| 17 | 171 | Observation | `Observation.component.code.coding` | 113163005 | Friend | http://snomed.info/sct |
| 18 | 174 | Observation | `Observation.component.code.coding` | 105529008 | Lives alone | http://snomed.info/sct |
| 19 | 186 | Observation | `Observation.code.coding` | 719051004 | Quantity of postpartum maternal blood loss | http://snomed.info/sct |
| 20 | 199 | Observation | `Observation.code.coding` | OC000013 | Penolong Persalinan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 21 | 200 | Observation | `Observation.valueCodeableConcept.coding` | 309453006 | Registered midwife | http://snomed.info/sct |
| 22 | 201 | Observation | `Observation.valueCodeableConcept.coding` | 309343006 | Physician | http://snomed.info/sct |
| 23 | 202 | Observation | `Observation.valueCodeableConcept.coding` | 11935004 | Obstetrician | http://snomed.info/sct |
| 24 | 203 | Observation | `Observation.valueCodeableConcept.coding` | 303071001 | Person in the family | http://snomed.info/sct |
| 25 | 204 | Observation | `Observation.valueCodeableConcept.coding` | OV000012 | Dukun | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 26 | 205 | Observation | `Observation.valueCodeableConcept.coding` | 1363121004 | Unassisted birth | http://snomed.info/sct |
| 27 | 206 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 28 | 217 | Observation | `Observation.code.coding` | OC000016 | Waktu Inisiasi Menyusui Dini | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 29 | 218 | Observation | `Observation.valueCodeableConcept.coding` | OV000014 | Kurang dari 1 Jam | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 30 | 219 | Observation | `Observation.valueCodeableConcept.coding` | OV000015 | Lebih dari 1 Jam | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 31 | 231 | Procedure | `Procedure.code.coding` | SP000130 | Menggunakan Partograf | http://terminology.kemkes.go.id/sp |
| 32 | 240 | Observation | `Observation.code.coding` | SP000122 | Catat di Buku KIA | http://terminology.kemkes.go.id/sp |
| 33 | 243 | Observation | `Observation.dataAbsentReason.coding` | not-applicable | Not Applicable | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 34 | 255 | Condition | `Condition.code.coding` | 199746004 | Obstructed labor | http://snomed.info/sct |
| 35 | 256 | Condition | `Condition.code.coding` | 48194001 | Pregnancy-induced hypertension | http://snomed.info/sct |
| 36 | 257 | Condition | `Condition.code.coding` | 47821001 | Postpartum hemorrhage | http://snomed.info/sct |
| 37 | 258 | Condition | `Condition.code.coding` | 40733004 | Infectious disease | http://snomed.info/sct |
| 38 | 259 | Condition | `Condition.code.coding` | 91302008 | Sepsis | http://snomed.info/sct |
| 39 | 260 | Condition | `Condition.code.coding` | 398254007 | Pre-eclampsia | http://snomed.info/sct |
| 40 | 261 | Condition | `Condition.code.coding` | 15938005 | Eclampsia | http://snomed.info/sct |
| 41 | 262 | Condition | `Condition.code.coding` | O75.9 | Complication of labour and delivery, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 42 | 266 | Observation | `Observation.code.coding` | SP000127 | Tatalaksana Komplikasi Persalinan | http://terminology.kemkes.go.id/sp |
| 43 | 281 | ServiceRequest | `ServiceRequest.code.coding` | 409014006 | Delivery care management | http://snomed.info/sct |
| 44 | 292 | ServiceRequest | `ServiceRequest.locationCode.coding` | SP000128 | Rumah Sakit Ibu dan Anak | http://terminology.kemkes.go.id/sp |
| 45 | 294 | ServiceRequest | `ServiceRequest.code.coding` | 185389009 | Follow-up visit | http://snomed.info/sct |
| 46 | 328 | Condition | `Condition.code.coding` | Z39.2 | Routine postpartum follow-up | http://hl7.org/fhir/sid/icd-10 |
| 47 | 349 | EpisodeOfCare | `EpisodeOfCare.type.coding` | PNC | Postnatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 48 | 355 | Condition | `Condition.code.coding` | 359746009 | Patient's condition stable | http://snomed.info/sct |
| 49 | 356 | Condition | `Condition.code.coding` | 162668006 | Patient’s condition unstable | http://snomed.info/sct |
| 50 | 363 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 51 | 375 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://loinc.org |
| 52 | 387 | Observation | `Observation.code.coding` | 8310-5 | Body temperature | http://loinc.org |
| 53 | 399 | Observation | `Observation.code.coding` | 8867-4 | Heart rate | http://loinc.org |
| 54 | 411 | Observation | `Observation.code.coding` | 9279-1 | Respiratory rate | http://loinc.org |
| 55 | 423 | Observation | `Observation.code.coding` | 32422-8 | Physical findings of breast | http://loinc.org |
| 56 | 424 | Observation | `Observation.valueCodeableConcept.coding` | 300885006 | Swelling of breast | http://snomed.info/sct |
| 57 | 425 | Observation | `Observation.valueCodeableConcept.coding` | 290084006 | Breast normal | http://snomed.info/sct |
| 58 | 435 | Observation | `Observation.code.coding` | OC000017 | Produksi ASI | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 59 | 436 | Observation | `Observation.valueCodeableConcept.coding` | OV000016 | Produksi ASI ada | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 60 | 437 | Observation | `Observation.valueCodeableConcept.coding` | OV000018 | Produksi ASI tidak ada | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 61 | 447 | Observation | `Observation.code.coding` | 11881-0 | Uterus Fundal height Tape measure | http://loinc.org |
| 62 | 459 | Observation | `Observation.code.coding` | 289700000 | Uterine contractions present | http://snomed.info/sct |
| 63 | 473 | Observation | `Observation.code.coding` | 252041008 | Micturition finding | http://snomed.info/sct |
| 64 | 474 | Observation | `Observation.valueCodeableConcept.coding` | 102834005 | Normal micturition | http://snomed.info/sct |
| 65 | 475 | Observation | `Observation.valueCodeableConcept.coding` | 49650001 | Dysuria | http://snomed.info/sct |
| 66 | 485 | Observation | `Observation.code.coding` | 300375001 | Able to defecate | http://snomed.info/sct |
| 67 | 497 | Observation | `Observation.code.coding` | OC000025 | Tanda Infeksi Luka Jahitan Sectio Caesaria | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 68 | 509 | Observation | `Observation.code.coding` | 249214003 | Color of lochia | http://snomed.info/sct |
| 69 | 510 | Observation | `Observation.valueCodeableConcept.coding` | 278072004 | Lochia rubra | http://snomed.info/sct |
| 70 | 511 | Observation | `Observation.valueCodeableConcept.coding` | 113291006 | Lochia sanguinolenta | http://snomed.info/sct |
| 71 | 512 | Observation | `Observation.valueCodeableConcept.coding` | 449828001 | Lochia serosa | http://snomed.info/sct |
| 72 | 513 | Observation | `Observation.valueCodeableConcept.coding` | 449827006 | Lochia alba | http://snomed.info/sct |
| 73 | 523 | Condition | `Condition.code.coding` | 289530006 | Vaginal bleeding | http://snomed.info/sct |
| 74 | 530 | Observation | `Observation.code.coding` | OC000020 | Tanda Infeksi Perineum | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 75 | 531 | Observation | `Observation.valueCodeableConcept.coding` | 210484005 | Open wound of perineum | http://snomed.info/sct |
| 76 | 532 | Observation | `Observation.valueCodeableConcept.coding` | 449891003 | Healing wound of perineum | http://snomed.info/sct |
| 77 | 533 | Observation | `Observation.valueCodeableConcept.coding` | 237339000 | Infection - perineal wound | http://snomed.info/sct |
| 78 | 544 | MedicationRequest | `MedicationRequest.contained.code.coding` | 92000653 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula | http://sys-ids.kemkes.go.id/kf |
| 79 | 578 | MedicationDispense | `MedicationDispense.contained.code.coding` | 93015491 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | http://sys-ids.kemkes.go.id/kf |
| 80 | 609 | Procedure | `Procedure.code.coding` | 767224000 | Administration of vitamin A | http://snomed.info/sct |
| 81 | 620 | Procedure | `Procedure.code.coding` | 767224000 | Administration of vitamin A | http://snomed.info/sct |
| 82 | 633 | Condition | `Condition.code.coding` | 211063003 | Infected abrasion of perineum | http://snomed.info/sct |
| 83 | 634 | Condition | `Condition.code.coding` | 40521000119100 | Postpartum pregnancy-induced hypertension | http://snomed.info/sct |
| 84 | 635 | Condition | `Condition.code.coding` | 47821001 | Postpartum hemorrhage | http://snomed.info/sct |
| 85 | 636 | Condition | `Condition.code.coding` | 266579006 | Inflammatory disorder of breast | http://snomed.info/sct |
| 86 | 637 | Condition | `Condition.code.coding` | O90.8 | Other complications of the puerperium, not elsewhere classified | http://hl7.org/fhir/sid/icd-10 |
| 87 | 645 | Observation | `Observation.code.coding` | SP000381 | Tatalaksana Komplikasi Infeksi | http://terminology.kemkes.go.id/sp |
| 88 | 658 | Observation | `Observation.code.coding` | 736286003 | Hypertension clinical management plan |  |
| 89 | 671 | Observation | `Observation.code.coding` | SP000380 | Tatalaksana Komplikasi Pendarahan | http://terminology.kemkes.go.id/sp |
| 90 | 684 | Observation | `Observation.code.coding` | SP000382 | Tatalaksana Komplikasi Mastitis | http://terminology.kemkes.go.id/sp |
| 91 | 701 | ServiceRequest | `ServiceRequest.code.coding` | 409014006 | Delivery care management | http://snomed.info/sct |
| 92 | 710 | ServiceRequest | `ServiceRequest.locationCode.coding` | SP000129 | Puskesmas PONED | http://terminology.kemkes.go.id/sp |
| 93 | 714 | ServiceRequest | `ServiceRequest.locationCode.coding` | SP000128 | Rumah Sakit Ibu dan Anak | http://terminology.kemkes.go.id/sp |
| 94 | 720 | Observation | `Observation.code.coding` | SP000383 | Keadaan Ibu Saat Tiba | http://terminology.kemkes.go.id/sp |
| 95 | 721 | Observation | `Observation.valueCodeableConcept.coding` | 438949009 | Alive | http://snomed.info/sct |
| 96 | 722 | Observation | `Observation.valueCodeableConcept.coding` | 419099009 | Dead | http://snomed.info/sct |
| 97 | 732 | Observation | `Observation.code.coding` | SP000384 | Keadaan Ibu Saat Pulang | http://terminology.kemkes.go.id/sp |
| 98 | 733 | Observation | `Observation.valueCodeableConcept.coding` | 438949009 | Alive | http://snomed.info/sct |
| 99 | 734 | Observation | `Observation.valueCodeableConcept.coding` | 419099009 | Dead | http://snomed.info/sct |
| 100 | 744 | Observation | `Observation.code.coding` | PC000004 | KB Pasca Persalinan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 101 | 745 | Observation | `Observation.valueCodeableConcept.coding` | 237122005 | Lactational amenorrhea | http://snomed.info/sct |
| 102 | 746 | Observation | `Observation.valueCodeableConcept.coding` | LA6523-0 | Condom | http://loinc.org |
| 103 | 747 | Observation | `Observation.valueCodeableConcept.coding` | LA6524-8 | Oral contraceptive pill | http://loinc.org |
| 104 | 748 | Observation | `Observation.valueCodeableConcept.coding` | LA6525-5 | Injectable/implantable hormone | http://loinc.org |
| 105 | 749 | Observation | `Observation.valueCodeableConcept.coding` | LA6527-1 | Intrauterine device | http://loinc.org |
| 106 | 750 | Observation | `Observation.valueCodeableConcept.coding` | SP000097 | Implan | http://terminology.kemkes.go.id/sp |
| 107 | 751 | Observation | `Observation.valueCodeableConcept.coding` | 77543007 | Ligation of fallopian tube | http://snomed.info/sct |
| 108 | 752 | Observation | `Observation.valueCodeableConcept.coding` | 22523008 | Vasectomy | http://snomed.info/sct |
| 109 | 753 | Observation | `Observation.dataAbsentReason.coding` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 110 | 763 | Observation | `Observation.code.coding` | 86651-7 | Birth control method at exit Reported --at exit | http://loinc.org |
| 111 | 764 | Observation | `Observation.valueCodeableConcept.coding` | 237122005 | Lactational amenorrhea | http://snomed.info/sct |
| 112 | 765 | Observation | `Observation.valueCodeableConcept.coding` | LA6523-0 | Condom | http://loinc.org |
| 113 | 766 | Observation | `Observation.valueCodeableConcept.coding` | LA6524-8 | Oral contraceptive pill | http://loinc.org |
| 114 | 767 | Observation | `Observation.valueCodeableConcept.coding` | LA6525-5 | Injectable/implantable hormone | http://loinc.org |
| 115 | 768 | Observation | `Observation.valueCodeableConcept.coding` | LA6527-1 | Intrauterine device | http://loinc.org |
| 116 | 769 | Observation | `Observation.valueCodeableConcept.coding` | SP000097 | Implan | http://terminology.kemkes.go.id/sp |
| 117 | 770 | Observation | `Observation.valueCodeableConcept.coding` | 77543007 | Ligation of fallopian tube | http://snomed.info/sct |
| 118 | 771 | Observation | `Observation.valueCodeableConcept.coding` | 22523008 | Vasectomy | http://snomed.info/sct |
| 119 | 772 | Observation | `Observation.dataAbsentReason.coding` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 120 | 782 | Observation | `Observation.code.coding` | 86653-3 | Reason for no birth control use - Reported --at exit | http://loinc.org |
| 121 | 839 | Condition | `Condition.code.coding` | Z00.1 | Routine child health examination |  |
| 122 | 859 | EpisodeOfCare | `EpisodeOfCare.type.coding` | Neonate | Neonate |  |
| 123 | 865 | Condition | `Condition.code.coding` | 102500002 | Good neonatal condition at birth | http://snomed.info/sct |
| 124 | 866 | Condition | `Condition.code.coding` | 42052009 | Omphalitis of newborn | http://snomed.info/sct |
| 125 | 867 | Condition | `Condition.code.coding` | 271863002 | Stool color abnormal | http://snomed.info/sct |
| 126 | 868 | Condition | `Condition.code.coding` | 95627000 | Fever of newborn | http://snomed.info/sct |
| 127 | 869 | Condition | `Condition.code.coding` | 268850004 | Neonatal diarrhea | http://snomed.info/sct |
| 128 | 870 | Condition | `Condition.code.coding` | 48000002 | Vomiting in newborn | http://snomed.info/sct |
| 129 | 871 | Condition | `Condition.code.coding` | 387712008 | Neonatal jaundice | http://snomed.info/sct |
| 130 | 872 | Condition | `Condition.code.coding` | 13791008 | Asthenia | http://snomed.info/sct |
| 131 | 873 | Condition | `Condition.code.coding` | 13629008 | Hypothermia of newborn | http://snomed.info/sct |
| 132 | 874 | Condition | `Condition.code.coding` | 95629002 | Excessive crying of newborn | http://snomed.info/sct |
| 133 | 875 | Condition | `Condition.code.coding` | 1179627006 | Neonatal respiratory distress | http://snomed.info/sct |
| 134 | 876 | Condition | `Condition.code.coding` | 87476004 | Neonatal seizure | http://snomed.info/sct |
| 135 | 877 | Condition | `Condition.code.coding` | 722934009 | Neonatal difficulty in feeding at breast | http://snomed.info/sct |
| 136 | 884 | Observation | `Observation.code.coding` | 63895-7 | Breastfeeding status | http://loinc.org |
| 137 | 896 | Procedure | `Procedure.code.coding` | 431868002 | Initiation of breastfeeding | http://snomed.info/sct |
| 138 | 906 | Procedure | `Procedure.code.coding` | 448883004 | Injection of vitamin K1 | http://snomed.info/sct |
| 139 | 916 | Procedure | `Procedure.code.coding` | PC000002 | Pemberian Salep Antibiotik Mata | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 140 | 926 | Procedure | `Procedure.code.coding` | 400984005 | Congenital hypothyroidism screening test | http://snomed.info/sct |
| 141 | 936 | Procedure | `Procedure.code.coding` | 408989004 | Newborn care management | http://snomed.info/sct |
| 142 | 947 | Observation | `Observation.code.coding` | 8345-1 | Body weight Measured --post partum | http://loinc.org |
| 143 | 959 | Observation | `Observation.code.coding` | 8306-3 | Body height --lying | http://loinc.org |
| 144 | 971 | Observation | `Observation.code.coding` | 9843-4 | Head Occipital-frontal circumference | http://loinc.org |
| 145 | 983 | Observation | `Observation.code.coding` | 8310-5 | Body temperature | http://loinc.org |
| 146 | 995 | Observation | `Observation.code.coding` | 9279-1 | Respiratory rate | http://loinc.org |
| 147 | 1007 | Observation | `Observation.code.coding` | 8867-4 | Heart rate | http://loinc.org |
| 148 | 1019 | Observation | `Observation.code.coding` | 249229001 | Finding of umbilical stump | http://loinc.org |
| 149 | 1020 | Observation | `Observation.valueCodeableConcept.coding` | 276402001 | Neonatal cord moist | http://snomed.info/sct |
| 150 | 1021 | Observation | `Observation.valueCodeableConcept.coding` | 276401008 | Neonatal cord dry | http://snomed.info/sct |
| 151 | 1022 | Observation | `Observation.valueCodeableConcept.coding` | 42052009 | Omphalitis of newborn | http://snomed.info/sct |
| 152 | 1032 | Observation | `Observation.code.coding` | 267030001 | Yellow or jaundiced color | http://snomed.info/sct |
| 153 | 1033 | Observation | `Observation.valueCodeableConcept.coding` | OV000180 | Tidak ada ikterus | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 154 | 1034 | Observation | `Observation.valueCodeableConcept.coding` | SP000390 | Ikterus derajat 1 | http://terminology.kemkes.go.id/sp |
| 155 | 1035 | Observation | `Observation.valueCodeableConcept.coding` | SP000391 | Ikterus derajat 2 | http://terminology.kemkes.go.id/sp |
| 156 | 1036 | Observation | `Observation.valueCodeableConcept.coding` | SP000392 | Ikterus derajat 3 | http://terminology.kemkes.go.id/sp |
| 157 | 1037 | Observation | `Observation.valueCodeableConcept.coding` | SP000393 | Ikterus derajat 4 | http://terminology.kemkes.go.id/sp |
| 158 | 1038 | Observation | `Observation.valueCodeableConcept.coding` | SP000394 | Ikterus derajat 5 | http://terminology.kemkes.go.id/sp |
| 159 | 1048 | Observation | `Observation.code.coding` | 249222005 | Neonatal condition | http://snomed.info/sct |
| 160 | 1049 | Observation | `Observation.valueCodeableConcept.coding` | 102500002 | Good neonatal condition at birth | http://snomed.info/sct |
| 161 | 1050 | Observation | `Observation.valueCodeableConcept.coding` | 276707008 | Infant in poor condition at birth | http://snomed.info/sct |
| 162 | 1051 | Observation | `Observation.valueCodeableConcept.coding` | 419099009 | Dead | http://snomed.info/sct |
| 163 | 1059 | Observation | `Observation.component.code.coding` | 413654009 | Birth asphyxia | http://snomed.info/sct |
| 164 | 1061 | Observation | `Observation.component.code.coding` | 56110009 | Fetal birth trauma | http://snomed.info/sct |
| 165 | 1063 | Observation | `Observation.component.code.coding` | 276659006 | Clinical infection of newborn | http://snomed.info/sct |
| 166 | 1065 | Observation | `Observation.component.code.coding` | 66091009 | Congenital disease | http://snomed.info/sct |
| 167 | 1067 | Observation | `Observation.component.code.coding` | 13629008 | Hypothermia of newborn | http://snomed.info/sct |
| 168 | 1069 | Observation | `Observation.component.code.coding` | 43424001 | Tetanus neonatorum | http://snomed.info/sct |
| 169 | 1071 | Observation | `Observation.component.code.coding` | 206376005 | Sepsis of the newborn | http://snomed.info/sct |
| 170 | 1073 | Observation | `Observation.component.code.coding` | 387712008 | Neonatal jaundice | http://snomed.info/sct |
| 171 | 1075 | Observation | `Observation.component.code.coding` | 22925008 | Neonatal disorde | http://snomed.info/sct |
| 172 | 1079 | Observation | `Observation.code.coding` | 81956-5 | Date and time of death [TimeStamp] | http://loinc.org |
| 173 | 1092 | Immunization | `Immunization.vaccineCode` | VG45 | HepB | http://sys-ids.kemkes.go.id/kfa |
| 174 | 1109 | ServiceRequest | `ServiceRequest.code.coding` | 736282001 | Neonatal critical care plan | http://snomed.info/sct |
| 175 | 1119 | Procedure | `Procedure.code.coding` | 408989004 | Newborn care management | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 96 |
| http://terminology.kemkes.go.id/sp | 26 |
| http://loinc.org | 26 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 13 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 4 |
| http://hl7.org/fhir/sid/icd-10 | 3 |
|  | 3 |
| http://sys-ids.kemkes.go.id/kf | 2 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 1 |
| http://sys-ids.kemkes.go.id/kfa | 1 |
| **Total** | **175** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 24 | – | Tanggal entry | – | `` |
| 25 | – | Link File Original | – | `` |
| 46 | – | Tanggal lahir ibu diketahui? | – | `` |
| 68 | – | Tautan GPS rumah | – | `` |
| 78 | – | _Tautan GPS rumah_precision | – | `` |
| 81 | – | Foto rumah | – | `` |
| 82 | – | Foto rumah_URL | – | `` |
| 83 | – | Nomor HP | – | `` |
| 89 | – | Alasan | – | `` |
| 118 | – | Jenis ID tambahan | – | `` |
| 119 | – | Nomor SID ID | – | `` |
| 120 | – | Nomor SID ID (tulis kedua kali) | – | `` |
| 215 | – | Pelayanan | – | `` |
| 252 | – | Komplikasi | – | `` |
| 305 | – | Lokasi periksa | – | `` |
| 469 | – | Kandung kemih | – | `` |
| 632 | – | Komplikasi/Tidak ada | – | `` |
| 695 | – | Apakah anda merujuk ibu hamil ke fasilitas kesehatan? | – | `` |
| 791 | – | Penggunaan KB | – | `` |
| 803 | – | Jenis ID tambahan | – | `` |
| 804 | – | Nomor SID ID bayi | – | `` |
| 805 | – | Nomor SID ID bayi (tulis kedua kali) | – | `` |
| 808 | – | Lokasi periksa | – | `` |
| 821 | – | Kunjungan Neonatal | – | `` |
| 822 | – | Kunjungan Neonatal/Segera setelah lahir (0-6 jam) | – | `` |
| 1104 | – | Apakah anda merujuk bayi ke fasilitas kesehatan? | – | `` |
