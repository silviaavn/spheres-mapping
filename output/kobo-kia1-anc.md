# Output Form: Kobo Buku KIA 1 - ANC

Sumber: `mapping/phdt-data-dictionary-kobo-kia1-anc.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-kobo-kia1-anc.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 167 |
| Code (`jumlah code` = 1) | 733 |
| Code unik (code + CodeSystem) | 518 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 71 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–13 | Observation | SP000395 | Pendaftaran Pertama Formulir KoBo | _Apakah ini pendaftaran di KoBo form pertama kali?_ → `Observation.valueBoolean` (5, tanpa BQ) |
| 2 | 14–18 | PractitionerRole | – | – | _Siapa yang melakukan entry data?_ → `PractitionerRole.active` (14, tanpa BQ) |
| 3 | 19–23 | PractitionerRole | – | – | _Siapa yang melakukan entry data?_ → `PractitionerRole.active` (19, tanpa BQ) |
| 4 | 24–27 | Practitioner | – | – | _Nama lengkap tenaga kesehatan yang memberikan pelayanan kesehatan_ → `Practitioner.name.text` (24, tanpa BQ)<br>_ID tenaga kesehatan yang memberikan pelayanan kesehatan_ → `Practitioner.identifier` (25, tanpa BQ)<br>_ID SID staff yang melakukan entry data_ → `Practitioner.identifier` (26, tanpa BQ)<br>_ID SID field staff yang mengumpulkan form_ → `Practitioner.identifier` (27, tanpa BQ) |
| 5 | 29–44 | DocumentReference | – | – | – |
| 6 | 46–48 | Patient | – | – | _Nama depan ibu_ → `Patient.name.text` (46, tanpa BQ)<br>_Nama belakang ibu_ → `Patient.name.text` (47, tanpa BQ)<br>_Nama Lengkap Ibu_ → `Patient.name.text` (48, tanpa BQ)<br>_Tulis Nomor Induk Kependudukan (NIK)_ → `Patient.identifier.use` (75, tanpa BQ)<br>_Tulis Nomor Induk Kependudukan (NIK) (Tulis kedua kali)_ → `Patient.identifier.use` (78, tanpa BQ)<br>_Jenis ID tambahan_ → `Patient.identifier.system` (81, tanpa BQ)<br>_Nomor ID tambahan_ → `Patient.identifier.value` (82, tanpa BQ)<br>_Nomor ID tambahan (tulis kedua kali)_ → `Patient.identifier.use` (83, tanpa BQ)<br>_Tanggal lahir_ → `Patient.birthDate` (111, tanpa BQ)<br>_Asal Provinsi_ → `Patient.address.extension.url` (125, tanpa BQ)<br>_Asal Kabupaten_ → `Patient.address.extension.url` (130, tanpa BQ)<br>_Asal Kecamatan_ → `Patient.address.extension.url` (137, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.url` (144, tanpa BQ)<br>_Nama Dusun_ → `Patient.address.extension.url` (147, tanpa BQ)<br>_Nama jalan dan nomor rumah (jika ada)_ → `Patient.address.line` (150, tanpa BQ)<br>_RW_ → `Patient.address.extension.url` (152, tanpa BQ)<br>_RT_ → `Patient.address.extension.url` (155, tanpa BQ)<br>__Tautan GPS rumah_latitude_ → `Patient.address.extension.url` (159, tanpa BQ)<br>__Tautan GPS rumah_longitude_ → `Patient.address.extension.url` (162, tanpa BQ)<br>__Tautan GPS rumah_altitude_ → `Patient.address.extension.extension.url` (166, tanpa BQ)<br>_Tulis nomor HP_ → `Patient.telecom` (173, tanpa BQ)<br>_Tulis nomor HP (tulis kedua kali)_ → `Patient.telecom` (174, tanpa BQ)<br>_Status pernikahan_ → `Patient.maritalStatus.coding` (448, tanpa BQ) |
| 7 | 49–60 | Observation | SP000402 | Kepemilikan Nomor Induk Kependudukan | _Apakah mempunyai Nomor Induk Kependudukan (NIK)_ → `Observation.valueBoolean` (52, tanpa BQ) |
| 8 | 61–74 | Observation | SP000403 | Alasan Tidak Ada Nomor Induk Kependudukan | _Pilih alasan tidak mempunyai Nomor Induk Kependudukan (NIK)_ → `Observation.valueCodeableConcept.coding` (64, tanpa BQ) |
| 9 | 85–91 | Coverage | – | – | _Status BPJS_ → `Coverage.identifier` (85, tanpa BQ) |
| 10 | 92–103 | Observation | SP000408 | Kepemilikan BPJS | – |
| 11 | 104–107 | Coverage | – | – | _Nomor BPJS Kesehatan_ → `Coverage.subscriberId` (104, tanpa BQ)<br>_Nomor BPJS Kesehatan (tulis kedua kali)_ → `Coverage.subscriberId` (106, tanpa BQ) |
| 12 | 113–124 | Observation | 424144002.0 | Current chronological age | _Usia_ → `Observation.valueQuantity.value` (116, tanpa BQ) |
| 13 | 179–206 | Observation | SP000409 | Rekan Serumah | _Rekan serumah_ → `Observation.component.valueBoolean` (183, tanpa BQ) |
| 14 | 209–223 | Encounter | – | – | _Tanggal kunjungan_ → `Encounter.period.start` (218, tanpa BQ)<br>_Nama faskes_ → `Encounter.serviceProvider.display` (242, tanpa BQ) |
| 15 | 224–230 | Condition | 134435003.0 | Routine antenatal care | – |
| 16 | 243–255 | Observation | 29298-7 | Reason for visit | _Alasan berkunjung_ → `Observation.valueCodeableConcept.coding` (246, tanpa BQ) |
| 17 | 256–262 | Condition | 77386006.0 | Pregnancy | – |
| 18 | 263–290 | Observation | 3401000175105.0 | Total number of prenatal care visits | _Kunjungan ke berapa?_ → `Observation.valueInteger` (266, tanpa BQ) |
| 19 | 291–341 | Observation | SP000412 | Tanda Bahaya Kehamilan | _Tanda bahaya_ → `Observation.valueBoolean` (294, tanpa BQ) |
| 20 | 342–382 | Observation | SP000412 | Tanda Bahaya Kehamilan | _Tanda Bahaya_ → `Observation.valueBoolean` (345, tanpa BQ) |
| 21 | 383–430 | Condition | 289567003.0 | Vaginal discharge problem | _Pilih masalah kesehatan_ → `Condition.clinicalStatus.coding` (383, tanpa BQ) |
| 22 | 432–447 | Observation | 82589-3 | Highest level of education | _Tingkat pendidikan tertinggi_ → `Observation.valueCodeableConcept.coding` (435, tanpa BQ) |
| 23 | 455–473 | Observation | 85658-3 | Occupation [Type] | _Pekerjaan_ → `Observation.valueCodeableConcept.coding` (458, tanpa BQ)<br>_Sebutkan_ → `Observation.note` (466, tanpa BQ) |
| 24 | 474–487 | Observation | 8665-2 | Last menstrual period start date | _HPHT diketahui_ → `Observation.status` (474, tanpa BQ)<br>_Tentukan tanggal HPHT_ → `Observation.valueDateTime` (480, tanpa BQ) |
| 25 | 488–501 | Observation | 18185-9 | Gestational age | _Usia kehamilan berdasarkan HPHT_ → `Observation.valueQuantity.value` (493, tanpa BQ) |
| 26 | 502–515 | Observation | 11778-8 | Delivery date Estimated | _Taksiran persalinan berdasarkan HPHT_ → `Observation.valueDateTime` (507, tanpa BQ) |
| 27 | 516–525 | Procedure | 88.78 | Diagnostic ultrasound of gravid uterus | _USG sudah dilakukan?_ → `Procedure.category.coding` (516, tanpa BQ)<br>_Tentukan tanggal USG_ → `Procedure.performedDateTime` (523, tanpa BQ) |
| 28 | 526–538 | Observation | 11888-5 | Gestational age US composite estimate | _Usia kehamilan berdasarkan hasil USG jika sudah dilakukan_ → `Observation.valueQuantity.value` (530, tanpa BQ) |
| 29 | 539–550 | Observation | 11781-2 | Delivery date US composite estimate | _Taksiran persalinan berdasarkan USG_ → `Observation.valueDateTime` (543, tanpa BQ) |
| 30 | 551–569 | Observation | 11996-6 | [#] Pregnancies | _Jumlah kehamilan (termasuk saat ini)_ → `Observation.valueInteger` (555, tanpa BQ) |
| 31 | 570–581 | Observation | SP000416 | Tahun Hamil | _Tahun hamil anak ke-1_ → `Observation.identifier` (570, tanpa BQ) |
| 32 | 582–594 | Observation | 161744009.0 | Past pregnancy history of miscarriage | _Apakah ada kehilangan kehamilan (sebelum 22 minggu/ 5 bulan) di hamil anak ke-1?_ → `Observation.identifier` (582, tanpa BQ) |
| 33 | 595–607 | Observation | 8339-4 | Birth weight Measured | _Berat lahir anak ke-1_ → `Observation.valueQuantity.value` (598, tanpa BQ) |
| 34 | 608–622 | Observation | 272058002.0 | Past pregnancy history of delivery procedure | _Jenis persalinan anak ke-1_ → `Observation.identifier` (608, tanpa BQ) |
| 35 | 623–641 | Observation | SP000417 | Riwayat Penolong Persalinan Sebelumnya | _Penolong persalinan anak ke-1_ → `Observation.identifier` (623, tanpa BQ)<br>_Sebutkan penolong persalinan lain-lain (anak ke-1)_ → `Observation.note` (634, tanpa BQ) |
| 36 | 642–678 | Observation | 450891000124109.0 | Past pregnancy history of complication of pregnancy, childbirth and/or puerperium | _Komplikasi kehamilan anak ke-1_ → `Observation.identifier` (642, tanpa BQ) |
| 37 | 679–690 | Observation | SP000416 | Tahun Hamil | _Tahun hamil anak ke-2_ → `Observation.identifier` (679, tanpa BQ) |
| 38 | 691–703 | Observation | 161744009.0 | Past pregnancy history of miscarriage | _Apakah ada kehilangan kehamilan (sebelum 22 minggu/ 5 bulan) di hamil anak ke-2?_ → `Observation.identifier` (691, tanpa BQ) |
| 39 | 704–717 | Observation | 8339-4 | Birth weight Measured | _Berat lahir anak ke-2_ → `Observation.valueQuantity.value` (707, tanpa BQ) |
| 40 | 718–732 | Observation | 272058002.0 | Past pregnancy history of delivery procedure | _Jenis persalinan anak ke-2_ → `Observation.identifier` (718, tanpa BQ) |
| 41 | 733–751 | Observation | SP000417 | Riwayat Penolong Persalinan Sebelumnya | _Penolong persalinan anak ke-2_ → `Observation.identifier` (733, tanpa BQ)<br>_Sebutkan penolong persalinan lain-lain (anak ke-2)_ → `Observation.note` (744, tanpa BQ) |
| 42 | 752–788 | Observation | 450891000124109.0 | Past pregnancy history of complication of pregnancy, childbirth and/or puerperium | _Komplikasi kehamilan anak ke-2_ → `Observation.identifier` (752, tanpa BQ) |
| 43 | 957–968 | Observation | 69043-8 | Other pregnancy outcomes # | _Jumlah kehilangan kehamilan (sebelum 22 minggu/ 5 bulan)_ → `Observation.valueInteger` (961, tanpa BQ) |
| 44 | 969–980 | Observation | 11977-6 | [#] Parity | _Jumlah angka lahir hidup (setelah 22 minggu)_ → `Observation.valueInteger` (973, tanpa BQ) |
| 45 | 981–991 | Observation | 252112002.0 | Number of stillbirths | _Jumlah lahir mati (setelah 22 minggu)_ → `Observation.valueInteger` (984, tanpa BQ) |
| 46 | 992–1048 | Observation | 450891000124109.0 | Past pregnancy history of complication of pregnancy, childbirth and/or puerperium | _Adakah masalah pada kehamilan sebelumnya?_ → `Observation.valueBoolean` (995, tanpa BQ)<br>_Sebutkan masalah pada kehamilan sebelumnya lainnya_ → `Observation.component.valueString` (1041, tanpa BQ) |
| 47 | 1049–1061 | Observation | 473011001.0 | Allergic condition | _Ada alergi?_ → `Observation.valueCodeableConcept.coding` (1052, tanpa BQ) |
| 48 | 1062–1092 | AllergyIntolerance | – | – | _Pilih jenis alergi_ → `AllergyIntolerance.clinicalStatus.coding` (1062, tanpa BQ) |
| 49 | 1093–1094 | Observation | 106203-3 | Allergy intolerance list | _Sebutkan jenis alergi lainnya_ → `Observation.component.valueString` (1094, tanpa BQ) |
| 50 | 1095–1114 | Procedure | 161615003.0 | History of surgery | _Pernah operasi?_ → `Procedure.status` (1095, tanpa BQ)<br>_Pilih jenis operasi_ → `Procedure.code.coding` (1100, tanpa BQ)<br>_Sebutkan jenis operasi lainnya_ → `Procedure.note` (1108, tanpa BQ) |
| 51 | 1115–1127 | Observation | 417662000.0 | History of clinical finding in subject | _Ada kondisi kesehatan masa lalu atau kronis?_ → `Observation.valueCodeableConcept.coding` (1118, tanpa BQ) |
| 52 | 1128–1145 | Condition | 472968007.0 | History of autoimmune disorder of endocrine system | _Pilih kondisi kesehatan masa lalu atau kronis_ → `Condition.clinicalStatus.coding` (1128, tanpa BQ) |
| 53 | 1146–1147 | Observation | 74964007.0 | Other | _Sebutkan kondisi kesehatan masa lalu atau kronis lainnya_ → `Observation.component.valueString` (1147, tanpa BQ) |
| 54 | 1148–1168 | Condition | 161501007.0 | History of hypertension | _Riwayat kesehatan ibu sekarang_ → `Condition.clinicalStatus.coding` (1148, tanpa BQ)<br>_Sebutkan riwayat kesehatan ibu sekarang lainnya_ → `Condition.code.text` (1164, tanpa BQ) |
| 55 | 1169–1187 | FamilyMemberHistory | – | – | _Riwayat penyakit keluarga_ → `FamilyMemberHistory.status` (1169, tanpa BQ)<br>_Sebutkan riwayat penyakit keluarga lainnya_ → `FamilyMemberHistory.condition.code.text` (1184, tanpa BQ) |
| 56 | 1188–1206 | Immunization | VG213 | COVID-19 | _Status vaksinasi COVID-19_ → `Immunization.status` (1188, tanpa BQ) |
| 57 | 1207–1217 | Immunization | – | – | – |
| 58 | 1218–1231 | Observation | SP000422 | Status Imunisasi Tetanus | _Status imunisasi TT_ → `Observation.valueCodeableConcept.coding` (1221, tanpa BQ) |
| 59 | 1232–1248 | Immunization | VG139 | Td | _Jumlah imunisasi TT yang sudah diberikan_ → `Immunization.status` (1232, tanpa BQ) |
| 60 | 1250–1289 | MedicationStatement | – | – | _Pengobatan saat ini_ → `MedicationStatement.category.coding` (1250, tanpa BQ)<br>_Sebutkan pengobatan saat ini lainnya_ → `MedicationStatement.medicationCodeableConcept.text` (1283, tanpa BQ) |
| 61 | 1290–1304 | Observation | 1208604004.0 | Caffeine intake | _Asupan kafein harian_ → `Observation.valueCodeableConcept.coding` (1293, tanpa BQ) |
| 62 | 1305–1341 | Observation | SP000424 | Riwayat Perilaku Berisiko Sebelum Hamil | _Riwayat perilaku berisiko 1 bulan sebelum hamil_ → `Observation.valueBoolean` (1310, tanpa BQ)<br>_Sebutkan lainnya_ → `Observation.component.valueString` (1334, tanpa BQ) |
| 63 | 1342–1354 | Observation | 365980008.0 | Finding of tobacco use and exposure | _Menggunakan produk tembakau?_ → `Observation.valueCodeableConcept.coding` (1345, tanpa BQ) |
| 64 | 1355–1361 | FamilyMemberHistory | – | – | _Adakah anggota keluarga di rumah tangga menggunakan produk tembakau?_ → `FamilyMemberHistory.status` (1355, tanpa BQ) |
| 65 | 1362–1373 | Observation | 1237409004.0 | Uses condom as protection for sex | _Menggunakan kondom (pria atau wanita) saat berhubungan seksual?_ → `Observation.valueBoolean` (1365, tanpa BQ) |
| 66 | 1374–1383 | Procedure | 428211000124100.0 | Assessment of substance use | _Penyelidikan klinis terkait konsumsi alkohol dan penggunaan obat-obatan terlarang sudah dilakukan_ → `Procedure.category.coding` (1374, tanpa BQ) |
| 67 | 1384–1409 | Observation | SP000427 | Konsumsi Alkohol atau Obat-Obatan Terlarang | _Konsumsi alkohol atau obat-obatan terlarang?_ → `Observation.valueBoolean` (1387, tanpa BQ)<br>_Sebutkan jenis konsumsi alkohol atau obat-obatan terlarang lainnya_ → `Observation.component.valueString` (1402, tanpa BQ) |
| 68 | 1410–1417 | FamilyMemberHistory | – | – | _Status HIV pasangan_ → `FamilyMemberHistory.status` (1410, tanpa BQ) |
| 69 | 1419–1444 | Condition | 16932000.0 | Nausea and vomiting | _Adakah gejala fisiologis/ ketidaknyamanan?_ → `Condition.clinicalStatus.coding` (1419, tanpa BQ)<br>_Ada gejala lain?_ → `Condition.code.coding` (1430, tanpa BQ)<br>_Sebutkan jenis gejala lain lainnya_ → `Condition.code.text` (1440, tanpa BQ) |
| 70 | 1446–1458 | Observation | 8302-2 | Body height | _Tinggi badan (cm)_ → `Observation.valueQuantity.value` (1450, tanpa BQ) |
| 71 | 1459–1473 | Observation | 56077-1 | Body weight --pre current pregnancy | _Berat badan pra-kehamilan diketahui?_ → `Observation.status` (1459, tanpa BQ)<br>_Tuliskan BB pra-kehamilan (kg)_ → `Observation.valueQuantity.value` (1465, tanpa BQ) |
| 72 | 1474–1486 | Observation | 29463-7 | Body weight | _Berat badan saat ini (kg)_ → `Observation.valueQuantity.value` (1478, tanpa BQ) |
| 73 | 1487–1503 | Observation | OC000010 | Indeks Massa Tubuh Sebelum Hamil | _IMT sebelum hamil_ → `Observation.valueQuantity.value` (1491, tanpa BQ) |
| 74 | 1504–1516 | Observation | 284473002.0 | Mid upper arm circumference | _Lingkar Lengan Atas/ LILA (cm)_ → `Observation.valueQuantity.value` (1508, tanpa BQ) |
| 75 | 1517–1529 | Observation | 8480-6 | Systolic blood pressure | _Tekanan darah sistolik (mmHg)_ → `Observation.valueQuantity.value` (1521, tanpa BQ) |
| 76 | 1530–1542 | Observation | 8462-4 | Diastolic blood pressure | _Tekanan darah diastolik (mmHg)_ → `Observation.valueQuantity.value` (1534, tanpa BQ) |
| 77 | 1543–1555 | Observation | 8310-5 | Body temperature | _Suhu tubuh (c)_ → `Observation.valueQuantity.value` (1547, tanpa BQ) |
| 78 | 1556–1568 | Observation | 8867-4 | Heart Rate | _Denyut nadi (kpm)_ → `Observation.valueQuantity.value` (1560, tanpa BQ) |
| 79 | 1569–1580 | Observation | 1237486008.0 | Pale discoloration of entire skin of body | _Ibu pucat?_ → `Observation.valueBoolean` (1572, tanpa BQ) |
| 80 | 1581–1596 | Observation | 10197-2 | Physical findings of Eye Narrative | _Konjungtiva_ → `Observation.valueString` (1586, tanpa BQ) |
| 81 | 1597–1612 | Observation | 10197-2 | Physical findings of Eye Narrative | _Sklera_ → `Observation.valueString` (1602, tanpa BQ) |
| 82 | 1613–1626 | Observation | 10206-1 | Physical findings of Skin Narrative | _Kulit_ → `Observation.valueString` (1616, tanpa BQ) |
| 83 | 1627–1641 | Observation | 11411-6 | Physical findings of Neck Narrative | _Leher_ → `Observation.valueString` (1631, tanpa BQ) |
| 84 | 1642–1656 | Observation | 423066003.0 | Finding of mouth region | _Gigi mulut_ → `Observation.valueString` (1646, tanpa BQ) |
| 85 | 1657–1671 | Observation | 297268004.0 | Ear, nose and throat finding | _Telinga, Hidung, Tenggorokan (THT)_ → `Observation.valueString` (1661, tanpa BQ) |
| 86 | 1672–1687 | Observation | 116312005.0 | Finding of lower limb | _Tungkai_ → `Observation.valueString` (1676, tanpa BQ) |
| 87 | 1688–1700 | Observation | 9279-1 | Respiratory rate | _Laju pernapasan (kpm)_ → `Observation.valueQuantity.value` (1692, tanpa BQ) |
| 88 | 1701–1736 | Observation | 11412-4 | Physical findings of Respiratory system Narrative | _Pemeriksaan pernapasan_ → `Observation.valueString` (1705, tanpa BQ)<br>_Sebutkan kondisi pernapasan abnormal lainnya_ → `Observation.component.valueString` (1729, tanpa BQ) |
| 89 | 1737–1776 | Observation | 10200-4 | Physical findings of Heart Narrative | _Pemeriksaan jantung_ → `Observation.valueString` (1742, tanpa BQ)<br>_Sebutkan kondisi jantung abnormal lainnya_ → `Observation.component.valueString` (1769, tanpa BQ) |
| 90 | 1777–1812 | Observation | 10193-1 | Physical findings of Breasts Narrative | _Pemeriksaan payudara_ → `Observation.valueString` (1781, tanpa BQ)<br>_Sebutkan kondisi payudara abnormal lainnya_ → `Observation.component.valueString` (1805, tanpa BQ) |
| 91 | 1813–1842 | Observation | 10191-5 | Physical findings of Abdomen Narrative | _Pemeriksaan abdomen_ → `Observation.valueString` (1818, tanpa BQ)<br>_Sebutkan jenis pemeriksaan abdomen abnormal lainnya_ → `Observation.component.valueString` (1836, tanpa BQ) |
| 92 | 1843–1890 | Observation | 35025007.0 | Manual pelvic examination | _Pemeriksaan panggul visual_ → `Observation.valueString` (1847, tanpa BQ)<br>_Sebutkan hasil pemeriksaan panggul visual abnormal lainnya_ → `Observation.component.valueString` (1883, tanpa BQ) |
| 93 | 1891–1900 | Procedure | 113023007.0 | Examination of vagina | _Pemeriksaan panggul/ pemeriksaan dalam_ → `Procedure.category.coding` (1891, tanpa BQ) |
| 94 | 1901–1912 | Observation | 177194007.0 | Manual dilation of cervix | _Berapa sentimeter (cm) dilatasi serviks?_ → `Observation.valueQuantity.value` (1904, tanpa BQ) |
| 95 | 1913–1925 | Observation | 364223009.0 | Vulva observable | _Inspekulo vulva_ → `Observation.valueCodeableConcept.coding` (1916, tanpa BQ) |
| 96 | 1926–1938 | Observation | 249300001.0 | Urethral finding | _Inspekulo uretra_ → `Observation.valueCodeableConcept.coding` (1929, tanpa BQ) |
| 97 | 1939–1951 | Observation | 451024007.0 | Inspection of vagina using vaginal speculum | _Inspekulo vagina_ → `Observation.valueCodeableConcept.coding` (1942, tanpa BQ) |
| 98 | 1952–1965 | Observation | 271939006.0 | Vaginal discharge | _Inspekulo fluksus_ → `Observation.valueCodeableConcept.coding` (1956, tanpa BQ) |
| 99 | 1966–1979 | Observation | 289552002.0 | White vaginal discharge | _Inspekulo flour_ → `Observation.valueCodeableConcept.coding` (1970, tanpa BQ) |
| 100 | 1980–1992 | Observation | 248910006.0 | Uterine cervix finding | _Inspekulo porsio_ → `Observation.valueCodeableConcept.coding` (1983, tanpa BQ) |
| 101 | 1993–2004 | Observation | 267038008.0 | Edema | _Ada edema?_ → `Observation.valueBoolean` (1996, tanpa BQ) |
| 102 | 2005–2018 | Observation | 44972-8 | Edema site | _Jenis edema_ → `Observation.valueCodeableConcept.coding` (2008, tanpa BQ) |
| 103 | 2019–2032 | Observation | 423484008.0 | Grade of edema | _Keparahan edema_ → `Observation.valueCodeableConcept.coding` (2022, tanpa BQ) |
| 104 | 2033–2044 | Observation | SP000433 | Usia Kehamilan Saat Pengukuran Tinggi Fundus Uteri | _Pengukuran Tinggi Fundus Uteri (TFU)_ → `Observation.valueCodeableConcept.coding` (2036, tanpa BQ) |
| 105 | 2045–2057 | Observation | 11881-0 | Uterus Fundal height Tape measure | _TFU dalam cm_ → `Observation.valueQuantity.value` (2049, tanpa BQ) |
| 106 | 2058–2074 | Observation | 246435002.0 | Number of fetuses | _Jumlah janin_ → `Observation.valueInteger` (2062, tanpa BQ) |
| 107 | 2075–2088 | Observation | 289437007.0 | Finding of fetal heart rate | _Detak jantung janin (ke-1) ada?_ → `Observation.valueCodeableConcept.coding` (2078, tanpa BQ) |
| 108 | 2089–2102 | Observation | 55283-6 | Fetal Heart rate | _Detak Jantung Janin (ke-1) (DJJ) (kpm)_ → `Observation.valueQuantity.value` (2093, tanpa BQ) |
| 109 | 2123–2136 | Observation | 32279003.0 | Fetal movement finding | _Gerakan janin (ke-1) ada?_ → `Observation.valueCodeableConcept.coding` (2126, tanpa BQ) |
| 110 | 2137–2149 | Observation | 364619008.0 | Measure of fetal movement | _Frekuensi gerakan janin (ke-1) dalam 1 jam (kali)_ → `Observation.valueQuantity.value` (2140, tanpa BQ) |
| 111 | 2170–2186 | Observation | 72155-5 | Position in womb Fetus [RHEA] | _Presentasi janin (ke-1)_ → `Observation.valueCodeableConcept.coding` (2174, tanpa BQ) |
| 112 | 2212–2224 | Procedure | 88.78 | Diagnostic ultrasound of gravid uterus | _USG_ → `Procedure.category.coding` (2212, tanpa BQ) |
| 113 | 2225–2237 | Observation | 88.78 | Diagnostic ultrasound of gravid uterus | _USG di trimester berapa_ → `Observation.valueCodeableConcept.coding` (2228, tanpa BQ)<br>_Tanggal USG_ → `Observation.effectiveDateTime` (2234, tanpa BQ) |
| 114 | 2238–2251 | Observation | SP000672 | Jumlah kantong kehamilan | _Hasil USG: Jumlah Gestational Sac (GS)_ → `Observation.valueCodeableConcept.coding` (2242, tanpa BQ) |
| 115 | 2252–2267 | Observation | 11878-6 | Number of fetuses by US | _Hasil USG: Jumlah janin_ → `Observation.valueInteger` (2255, tanpa BQ) |
| 116 | 2268–2281 | Observation | 11850-5 | Gestational sac Mean diameter US | _Hasil USG: GS (Gestational Sac) janin ke-1 (mm)_ → `Observation.valueQuantity.value` (2272, tanpa BQ) |
| 117 | 2282–2295 | Observation | 11957-8 | Fetal Crown Rump length US | _Hasil USG: CRL (Crown-rump Length) janin ke-1 (mm)_ → `Observation.valueQuantity.value` (2286, tanpa BQ) |
| 118 | 2304–2316 | Observation | 11888-5 | Gestational age US composite estimate | _Hasil USG: Usia kehamilan (minggu)_ → `Observation.valueQuantity.value` (2308, tanpa BQ) |
| 119 | 2317–2329 | Observation | SP000673 | Letak kantong kehamilan | _Hasil USG: Letak kantong kehamilan_ → `Observation.valueCodeableConcept.coding` (2320, tanpa BQ) |
| 120 | 2330–2341 | Observation | 11615-2 | Fetal Heart Activity US | _Hasil USG: Pulsasi Jantung_ → `Observation.valueCodeableConcept.coding` (2332, tanpa BQ)<br>_Hasil USG: Taksiran persalinan_ → `Observation.status` (2341, tanpa BQ) |
| 121 | 2342–2353 | Observation | 11781-2 | Delivery date US composite estimate | _Hasil USG: Presentasi janin ke-1_ → `Observation.status` (2353, tanpa BQ) |
| 122 | 2354–2367 | Observation | 11877-8 | Fetal presentation US | _Hasil USG: Status janin ke-1_ → `Observation.status` (2367, tanpa BQ) |
| 123 | 2368–2379 | Observation | 404964004 | Antepartum fetal status | _Hasil USG: Letak janin ke-1_ → `Observation.status` (2379, tanpa BQ) |
| 124 | 2380–2393 | Observation | 271692001 | Presentation of fetus | _Hasil USG: Berat janin ke-1_ → `Observation.status` (2393, tanpa BQ) |
| 125 | 2394–2407 | Observation | 11727-5 | Fetal Body weight estimated by US | _Hasil USG: Detak jantung janin ke-1_ → `Observation.status` (2407, tanpa BQ) |
| 126 | 2408–2489 | Observation | 11948-7 | Fetal Heart rate US | _Hasil USG: Cairan amnion_ → `Observation.status` (2489, tanpa BQ) |
| 127 | 2490–2502 | Observation | 77012006 | Amniotic fluid | _Hasil USG: Plasenta_ → `Observation.status` (2502, tanpa BQ) |
| 128 | 2503–2514 | Observation | 78067005 | Placental structure | _Hasil USG: Lokasi plasenta_ → `Observation.status` (2514, tanpa BQ) |
| 129 | 2515–2532 | Observation | 11994-1 | Placenta position US | _Hasil USG: BPD (cm) janin ke-1_ → `Observation.status` (2532, tanpa BQ) |
| 130 | 2533–2546 | Observation | 11820-8 | Fetal Head Diameter.biparietal US | _Hasil USG: HC (cm) janin ke-1_ → `Observation.status` (2546, tanpa BQ) |
| 131 | 2547–2560 | Observation | 11984-2 | Fetal Head Circumference US | _Hasil USG: AC (cm) janin ke-1_ → `Observation.status` (2560, tanpa BQ) |
| 132 | 2561–2574 | Observation | 11979-2 | Fetal Abdomen Circumference US | _Hasil USG: FL (cm) janin ke-1_ → `Observation.status` (2574, tanpa BQ) |
| 133 | 2575–2604 | Observation | 11963-6 | Fetal Femur diaphysis [Length] US | _Hasil USG: SPD cairan ketuban (cm)_ → `Observation.status` (2604, tanpa BQ) |
| 134 | 2605–2616 | Observation | 11832-3 | Fetal Amniotic fluid space Maximum diameter largest pocket US | _Hasil USG: Taksiran berat janin (TBJ)_ → `Observation.status` (2616, tanpa BQ) |
| 135 | 2617–2629 | Observation | 11727-5 | Fetal Body weight estimated by US | _Hasil USG: Kecurigaan temuan abnormal_ → `Observation.status` (2629, tanpa BQ) |
| 136 | 2630–2641 | Observation | 425551008.0 | Antenatal ultrasound scan for possible abnormality | _Sebutkan kecurigaan temuan abnormal_ → `Observation.note.text` (2641, tanpa BQ) |
| 137 | 2643–2655 | Procedure | 88.78 | Diagnostic ultrasound of gravid uterus | _Alasan_ → `Procedure.category.coding` (2643, tanpa BQ)<br>_Sebutkan alasan lainnya_ → `Procedure.statusReason.text` (2649, tanpa BQ) |
| 138 | 2656–2673 | Observation | 883-9 | ABO group [Type] in Blood | _Tes golongan darah_ → `Observation.category.coding` (2656, tanpa BQ)<br>_Tanggal tes golongan darah_ → `Observation.effectiveDateTime` (2663, tanpa BQ)<br>_Golongan darah_ → `Observation.valueCodeableConcept.coding` (2664, tanpa BQ) |
| 139 | 2674–2686 | Observation | 10331-7 | Rh [Type] in Blood | _Rh faktor_ → `Observation.valueCodeableConcept.coding` (2678, tanpa BQ) |
| 140 | 2687–2713 | Observation | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | _Tes HIV_ → `Observation.category.coding` (2687, tanpa BQ)<br>_Tanggal tes HIV_ → `Observation.effectiveDateTime` (2694, tanpa BQ)<br>_Hasil tes_ → `Observation.valueCodeableConcept.coding` (2695, tanpa BQ)<br>_Alasan_ → `Observation.dataAbsentReason.coding` (2698, tanpa BQ)<br>_Sebutkan alasan lainnya_ → `Observation.dataAbsentReason.text` (2701, tanpa BQ)<br>_Tes hepatitis B_ → `Observation.category.coding` (2708, tanpa BQ)<br>_Tanggal tes hepatitis B_ → `Observation.effectiveDateTime` (2713, tanpa BQ) |
| 141 | 2714–2718 | Observation | ANC.B9.DE60 | Hepatitis B test conducted | _Jenis tes hepatitis B_ → `Observation.code.coding` (2714, tanpa BQ) |
| 142 | 2719–2740 | Observation | 712853001.0 | Antenatal screening for viral hepatitis type B | _Alasan_ → `Observation.dataAbsentReason.coding` (2724, tanpa BQ)<br>_Sebutkan alasan lainnya_ → `Observation.dataAbsentReason.text` (2727, tanpa BQ)<br>_Tes lanjutan hepatitis B (HBV DNA atau HbeAg)_ → `Observation.category.coding` (2735, tanpa BQ)<br>_Tanggal tes lanjutan hepatitis B_ → `Observation.effectiveDateTime` (2740, tanpa BQ) |
| 143 | 2741–2766 | Observation | ANC.B9.DE60 | Hepatitis B test conducted | _Jenis tes lanjutan hepatitis B_ → `Observation.code.coding` (2741, tanpa BQ)<br>_Hasil tes lanjutan hepatitis B - HBV DNA (IU/mL)_ → `Observation.valueQuantity.value` (2744, tanpa BQ)<br>_Sebutkan alasan lainnya_ → `Observation.dataAbsentReason.text` (2753, tanpa BQ)<br>_Tes sifilis_ → `Observation.category.coding` (2761, tanpa BQ)<br>_Tanggal tes sifilis_ → `Observation.effectiveDateTime` (2766, tanpa BQ) |
| 144 | 2767–2771 | Observation | ANC.B9.DE96 | Syphilis test conducted | _Jenis tes sifilis_ → `Observation.code.coding` (2767, tanpa BQ) |
| 145 | 2772–2796 | Observation | 169698000.0 | Antenatal syphilis screening | _Sebutkan alasan lainnya_ → `Observation.dataAbsentReason.text` (2781, tanpa BQ)<br>_Tes urin_ → `Observation.category.coding` (2788, tanpa BQ)<br>_Tanggal tes urin_ → `Observation.effectiveDateTime` (2796, tanpa BQ) |
| 146 | 2798–2850 | Observation | 117010004.0 | Urine culture | _Sebutkan alasan lainnya_ → `Observation.dataAbsentReason.text` (2816, tanpa BQ)<br>_Hasil tes dipstick urin - nitrit_ → `Observation.component.code.coding` (2823, tanpa BQ)<br>_Hasil tes dipstick urin - leukosit_ → `Observation.component.code.coding` (2830, tanpa BQ)<br>_Hasil tes dipstick urin - protein_ → `Observation.component.code.coding` (2837, tanpa BQ)<br>_Hasil tes dipstick urin - glukosa_ → `Observation.component.code.coding` (2844, tanpa BQ) |
| 147 | 2851–2860 | Observation | 5809-9 | Reducing substances [Presence] in Urine | _Hasil tes urin reduksi_ → `Observation.valueCodeableConcept.coding` (2852, tanpa BQ)<br>_Tes HB (Hemoglobin Darah)_ → `Observation.category.coding` (2860, tanpa BQ) |
| 148 | 2861–2902 | Observation | 718-7 | Hemoglobin [Mass/volume] in Blood | _Tanggal tes HB_ → `Observation.effectiveDateTime` (2867, tanpa BQ)<br>_Hasil tes HB- hitung darah lengkap (gr/dL)_ → `Observation.component.code.coding` (2879, tanpa BQ)<br>_Hematokrit (Ht)_ → `Observation.component.code.coding` (2882, tanpa BQ)<br>_Jumlah leukosit_ → `Observation.component.code.coding` (2885, tanpa BQ)<br>_Jumlah trombosit_ → `Observation.component.code.coding` (2888, tanpa BQ)<br>_Hasil tes HB- hemoglobinometer_ → `Observation.valueQuantity.code` (2891, tanpa BQ)<br>_Hasil tes HB- skala warna hemoglobin_ → `Observation.valueQuantity.code` (2893, tanpa BQ)<br>_Hasil tes HB- jenis tes tidak diketahui_ → `Observation.valueQuantity.code` (2895, tanpa BQ)<br>_Sebutkan alasan lainnya_ → `Observation.dataAbsentReason.text` (2901, tanpa BQ)<br>_Tes HIV pasangan_ → `Observation.category.coding` (2902, tanpa BQ) |
| 149 | 2903–2929 | Observation | SP000670 | Hasil Tes HIV Pasangan | _Tanggal tes HIV_ → `Observation.effectiveDateTime` (2911, tanpa BQ)<br>_Hasil tes HIV pasangan_ → `Observation.valueCodeableConcept.coding` (2912, tanpa BQ)<br>_Tes glukosa darah_ → `Observation.category.coding` (2918, tanpa BQ)<br>_Tanggal tes glukosa darah_ → `Observation.effectiveDateTime` (2926, tanpa BQ) |
| 150 | 2930–2954 | Observation | ANC.B9.DE159 | Blood glucose test conducted | _Jenis tes glukosa darah_ → `Observation.code.coding` (2930, tanpa BQ)<br>_Hasil glukosa darah puasa (mg/dL)_ → `Observation.valueQuantity.code` (2936, tanpa BQ)<br>_TTGO 75g- hasil glukosa puasa (mg/dL)_ → `Observation.component.code.coding` (2938, tanpa BQ)<br>_TTGO 75g- hasil setelah 1 jam (mg/dL)_ → `Observation.component.code.coding` (2941, tanpa BQ)<br>_TTGO 75g- hasil setelah 2 jam (mg/dL)_ → `Observation.component.code.coding` (2944, tanpa BQ)<br>_Hasil tes glukosa darah sewaktu (mg/dL)_ → `Observation.valueQuantity.code` (2947, tanpa BQ)<br>_Hasil tes glukosa darah- jenis tes tidak diketahui (mg/dL)_ → `Observation.valueQuantity.code` (2949, tanpa BQ)<br>_Tes lainnya_ → `Observation.category.coding` (2951, tanpa BQ)<br>_Tanggal tes lainnya_ → `Observation.effectiveDateTime` (2954, tanpa BQ) |
| 151 | 2955–2963 | Observation | 243787009 | Antenatal screening | _Nama tes_ → `Observation.code.coding` (2955, tanpa BQ)<br>_Hasil tes_ → `Observation.valueString` (2957, tanpa BQ) |
| 152 | 2965–2982 | Procedure | 61310001.0 | Nutrition Education | _Apakah ibu sudah mendapatkan konseling oleh tenaga kesehatan?_ → `Procedure.category.coding` (2965, tanpa BQ)<br>_Tanggal konseling_ → `Procedure.performedDateTime` (2972, tanpa BQ)<br>_Topik konseling lainnya_ → `Procedure.code.text` (2982, tanpa BQ) |
| 153 | 2983–2999 | Procedure | 385892002.0 | Mental health screening | _Skrining Kesehatan Jiwa_ → `Procedure.category.coding` (2983, tanpa BQ)<br>_Tanggal Skrining Kesehatan Jiwa_ → `Procedure.performedDateTime` (2991, tanpa BQ) |
| 154 | 3000–3028 | Observation | – | – | _Pernah mendapatkan skrining preeklampsia_ → `Observation.category.coding` (3000, tanpa BQ)<br>_Tanggal Skrining Preeklampsia_ → `Observation.effectiveDateTime` (3005, tanpa BQ)<br>_Skrining Diabetes Mellitus Gestasional_ → `Observation.category.coding` (3018, tanpa BQ)<br>_Tanggal Skrining Diabetes Mellitus Gestasional_ → `Observation.effectiveDateTime` (3025, tanpa BQ) |
| 155 | 3030–3044 | Observation | 1268646002.0 | Gestational diabetes mellitus screening | _Berapa hasil gula darah puasa (g/dL) ibu?_ → `Observation.valueQuantity.value` (3034, tanpa BQ)<br>_Berapa hasil gula darah 2 jam post prandia (g/dL) ibu?_ → `Observation.valueQuantity.value` (3036, tanpa BQ) |
| 156 | 3045–3063 | ServiceRequest | 185389009.0 | Follow-up visit | _Rencana tindak lanjut dari hasil skrining diabetes melitus gestasional_ → `ServiceRequest.category.coding` (3045, tanpa BQ)<br>_Rencana tindak lanjut dari hasil skrining diabetes melitus gestasional lainnya_ → `ServiceRequest.code.text` (3051, tanpa BQ)<br>_Detail rujukan kunjungan lanjutan_ → `ServiceRequest.patientInstruction` (3052, tanpa BQ)<br>_Detail rujukan konsultasi_ → `ServiceRequest.patientInstruction` (3053, tanpa BQ)<br>_Detail rujukan rawat jalan_ → `ServiceRequest.patientInstruction` (3054, tanpa BQ)<br>_Detail rujukan rawat inap_ → `ServiceRequest.patientInstruction` (3055, tanpa BQ) |
| 157 | 3065–3090 | MedicationRequest | 92000653.0 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula | _Apakah ibu mendapatkan tablet tambah darah_ → `MedicationRequest.contained.resourceType` (3065, tanpa BQ) |
| 158 | 3091–3116 | MedicationDispense | 93015491.0 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | _Tanggal mendapatkan tablet tambah darah_ → `MedicationDispense.whenPrepared` (3113, tanpa BQ)<br>_Berapa jumlah tablet tambah darah yang didapatkan_ → `MedicationDispense.quantity.value` (3115, tanpa BQ) |
| 159 | 3119–3130 | Procedure | 409073007.0 | Education | _Tanggal mendapatkan tindakan/pengobatan dari dokter/tenaga kesehatan_ → `Procedure.performedDateTime` (3127, tanpa BQ) |
| 160 | 3131–3132 | Procedure | 409063005.0 | Counselling | – |
| 161 | 3133–3134 | Procedure | 103693007.0 | Diagnostic procedure | – |
| 162 | 3135–3136 | Procedure | 182832007.0 | Procedure related to management of drug administration | – |
| 163 | 3137–3138 | Procedure | 61310001.0 | Nutrition education | – |
| 164 | 3139–3153 | Procedure | 409011003.0 | Antenatal care management | _Tindakan/pengobatan lainnya_ → `Procedure.code.text` (3141, tanpa BQ)<br>_Detail Edukasi yang diberikan_ → `Procedure.note` (3149, tanpa BQ)<br>_Detail Konseling yang diberikan_ → `Procedure.note` (3150, tanpa BQ)<br>_Detail Prosedur Diagnosis_ → `Procedure.note` (3151, tanpa BQ)<br>_Detail Pengobatan yang diberikan_ → `Procedure.note` (3152, tanpa BQ)<br>_Detail Diet yang diberikan_ → `Procedure.note` (3153, tanpa BQ) |
| 165 | 3155–3178 | CarePlan | – | – | _Rencana Konsultasi Lanjut_ → `CarePlan.title` (3155, tanpa BQ)<br>_Rencana Proses Melahirkan_ → `CarePlan.status` (3175, tanpa BQ) |
| 166 | 3179–3193 | CarePlan | – | – | _Pilihan rencana kontrasepsi_ → `CarePlan.status` (3190, tanpa BQ) |
| 167 | 3194–3207 | CarePlan | – | – | – |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 125 |
| Procedure | 14 |
| Condition | 6 |
| FamilyMemberHistory | 3 |
| Immunization | 3 |
| CarePlan | 3 |
| PractitionerRole | 2 |
| Coverage | 2 |
| Practitioner | 1 |
| DocumentReference | 1 |
| Patient | 1 |
| Encounter | 1 |
| AllergyIntolerance | 1 |
| MedicationStatement | 1 |
| ServiceRequest | 1 |
| MedicationRequest | 1 |
| MedicationDispense | 1 |
| **Total** | **167** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 4 | Observation | `Observation.code.coding` | SP000395 | Pendaftaran Pertama Formulir KoBo | http://terminology.kemkes.go.id/sp |
| 2 | 15 | PractitionerRole | `PractitionerRole.code.coding` | 223366009.0 | Healthcare professional | http://snomed.info/sct |
| 3 | 16 | PractitionerRole | `PractitionerRole.code.coding` | SP000397 | Field/call center staff | http://terminology.kemkes.go.id/sp |
| 4 | 17 | PractitionerRole | `PractitionerRole.code.coding` | SP000396 | Data entry staff | http://terminology.kemkes.go.id/sp |
| 5 | 20 | PractitionerRole | `PractitionerRole.code.coding` | SP000396 | Data entry staff | http://terminology.kemkes.go.id/sp |
| 6 | 21 | PractitionerRole | `PractitionerRole.code.coding` | SP000397 | Field/call center staff | http://terminology.kemkes.go.id/sp |
| 7 | 22 | PractitionerRole | `PractitionerRole.code.coding` | 309453006.0 | Registered midwife | http://snomed.info/sct |
| 8 | 23 | PractitionerRole | `PractitionerRole.code` | SP000373 | Kader Kesehatan | http://terminology.kemkes.go.id/sp |
| 9 | 43 | DocumentReference | `DocumentReference.content.format` | SP000732 | Buku KIA | http://terminology.kemkes.go.id/sp |
| 10 | 51 | Observation | `Observation.code.coding` | SP000402 | Kepemilikan Nomor Induk Kependudukan | http://terminology.kemkes.go.id/sp |
| 11 | 63 | Observation | `Observation.code.coding` | SP000403 | Alasan Tidak Ada Nomor Induk Kependudukan | http://terminology.kemkes.go.id/sp |
| 12 | 64 | Observation | `Observation.valueCodeableConcept.coding` | SP000404 | Tidak Punya Kartu Tanda Penduduk | http://terminology.kemkes.go.id/sp |
| 13 | 65 | Observation | `Observation.valueCodeableConcept.coding` | SP000405 | Tidak Membawa Kartu Tanda Penduduk | http://terminology.kemkes.go.id/sp |
| 14 | 66 | Observation | `Observation.valueCodeableConcept.coding` | SP000406 | Kartu Tanda Penduduk Hilang | http://terminology.kemkes.go.id/sp |
| 15 | 67 | Observation | `Observation.valueCodeableConcept.coding` | SP000407 | Privasi | http://terminology.kemkes.go.id/sp |
| 16 | 94 | Observation | `Observation.code.coding` | SP000408 | Kepemilikan BPJS | http://terminology.kemkes.go.id/sp |
| 17 | 115 | Observation | `Observation.code.coding` | 424144002.0 | Current chronological age | http://snomed.info/sct |
| 18 | 181 | Observation | `Observation.code.coding` | SP000409 | Rekan Serumah | http://terminology.kemkes.go.id/sp |
| 19 | 182 | Observation | `Observation.component.code.coding` | 40683002.0 | Parent | http://snomed.info/sct |
| 20 | 185 | Observation | `Observation.component.code.coding` | 375005.0 | Sibling | http://snomed.info/sct |
| 21 | 188 | Observation | `Observation.component.code.coding` | 303071001.0 | Family member | http://snomed.info/sct |
| 22 | 191 | Observation | `Observation.component.code.coding` | 127848009.0 | Spouse | http://snomed.info/sct |
| 23 | 194 | Observation | `Observation.component.code.coding` | 113163005.0 | Friend | http://snomed.info/sct |
| 24 | 197 | Observation | `Observation.component.code.coding` | 105529008.0 | Lives alone | http://snomed.info/sct |
| 25 | 226 | Condition | `Condition.code.coding` | 134435003.0 | Routine antenatal care | http://snomed.info/sct |
| 26 | 245 | Observation | `Observation.code.coding` | 29298-7 | Reason for visit | http://loinc.org |
| 27 | 246 | Observation | `Observation.valueCodeableConcept.coding` | SP000002 | Kunjungan Pertama Pemeriksaan Kehamilan | http://terminology.kemkes.go.id/sp |
| 28 | 247 | Observation | `Observation.valueCodeableConcept.coding` | SP000410 | Kunjungan Terjadwal | http://terminology.kemkes.go.id/sp |
| 29 | 248 | Observation | `Observation.valueCodeableConcept.coding` | SP000411 | Pemeriksaan Masalah Kesehatan | http://terminology.kemkes.go.id/sp |
| 30 | 258 | Condition | `Condition.code.coding` | 77386006.0 | Pregnancy | http://snomed.info/sct |
| 31 | 265 | Observation | `Observation.code.coding` | 3401000175105.0 | Total number of prenatal care visits | http://snomed.info/sct |
| 32 | 293 | Observation | `Observation.code.coding` | SP000412 | Tanda Bahaya Kehamilan | http://terminology.kemkes.go.id/sp |
| 33 | 296 | Observation | `Observation.component.code.coding` | 289530006.0 | Vaginal bleeding | http://snomed.info/sct |
| 34 | 299 | Observation | `Observation.component.code.coding` | 95837007.0 | Central cyanosis | http://snomed.info/sct |
| 35 | 302 | Observation | `Observation.component.code.coding` | 91175000.0 | Seizure | http://snomed.info/sct |
| 36 | 305 | Observation | `Observation.component.code.coding` | 386661006.0 | Fever | http://snomed.info/sct |
| 37 | 308 | Observation | `Observation.component.code.coding` | 25064002.0 | Headache | http://snomed.info/sct |
| 38 | 311 | Observation | `Observation.component.code.coding` | 397540003.0 | Visual impairment | http://snomed.info/sct |
| 39 | 314 | Observation | `Observation.component.code.coding` | 282020008.0 | Premature delivery | http://snomed.info/sct |
| 40 | 317 | Observation | `Observation.component.code.coding` | 3950001.0 | Birth | http://snomed.info/sct |
| 41 | 320 | Observation | `Observation.component.code.coding` | SP000413 | Terlihat Sangat Sakit | http://terminology.kemkes.go.id/sp |
| 42 | 323 | Observation | `Observation.component.code.coding` | 14094001.0 | Excessive vomiting in pregnancy | http://snomed.info/sct |
| 43 | 326 | Observation | `Observation.component.code.coding` | 76948002.0 | Severe pain | http://snomed.info/sct |
| 44 | 329 | Observation | `Observation.component.code.coding` | 21522001.0 | Abdominal pain | http://snomed.info/sct |
| 45 | 332 | Observation | `Observation.component.code.coding` | 418107008.0 | Unconscious | http://snomed.info/sct |
| 46 | 344 | Observation | `Observation.code.coding` | SP000412 | Tanda Bahaya Kehamilan | http://terminology.kemkes.go.id/sp |
| 47 | 347 | Observation | `Observation.component.code.coding` | OV000273 | Demam tinggi terus menerus | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 48 | 350 | Observation | `Observation.component.code.coding` | 21522001.0 | Abdominal pain | http://snomed.info/sct |
| 49 | 353 | Observation | `Observation.component.code.coding` | 289530006.0 | Vaginal bleeding | http://snomed.info/sct |
| 50 | 356 | Observation | `Observation.component.code.coding` | 8765009.0 | Hematemesis | http://snomed.info/sct |
| 51 | 359 | Observation | `Observation.component.code.coding` | SP000459 | Nafas pendek dan jantung berbedar | http://terminology.kemkes.go.id/sp |
| 52 | 362 | Observation | `Observation.component.code.coding` | 111516008.0 | Blurring of visual image | http://snomed.info/sct |
| 53 | 365 | Observation | `Observation.component.code.coding` | 25064002.0 | Headache | http://snomed.info/sct |
| 54 | 368 | Observation | `Observation.component.code.coding` | 289567003.0 | Vaginal discharge problem | http://snomed.info/sct |
| 55 | 371 | Observation | `Observation.component.code.coding` | 289432001.0 | Fetal movements absent | http://snomed.info/sct |
| 56 | 374 | Observation | `Observation.component.code.coding` | 10759661000119108 | Preterm premature rupture of membranes with onset of labor unknown | http://snomed.info/sct |
| 57 | 377 | Observation | `Observation.component.code.coding` | 249196008.0 | Distress from pain in labor | http://snomed.info/sct |
| 58 | 380 | Observation | `Observation.component.code.coding` | 14094001.0 | Excessive vomiting in pregnancy | http://snomed.info/sct |
| 59 | 385 | Condition | `Condition.code.coding` | 289567003.0 | Vaginal discharge problem | http://snomed.info/sct |
| 60 | 386 | Condition | `Condition.code.coding` | 38341003.0 | Hypertensive disorder, systemic arterial | http://snomed.info/sct |
| 61 | 387 | Condition | `Condition.code.coding` | 45007003.0 | Low blood pressure | http://snomed.info/sct |
| 62 | 388 | Condition | `Condition.code.coding` | 14760008.0 | Constipation | http://snomed.info/sct |
| 63 | 389 | Condition | `Condition.code.coding` | 70514001.0 | Uterine contraction, function | http://snomed.info/sct |
| 64 | 390 | Condition | `Condition.code.coding` | 49727002.0 | Cough | http://snomed.info/sct |
| 65 | 391 | Condition | `Condition.code.coding` | 62315008.0 | Diarrhea | http://snomed.info/sct |
| 66 | 392 | Condition | `Condition.code.coding` | 404640003.0 | Dizziness | http://snomed.info/sct |
| 67 | 393 | Condition | `Condition.code.coding` | 289432001.0 | Fetal movements absent | http://snomed.info/sct |
| 68 | 394 | Condition | `Condition.code.coding` | 276372004.0 | Weak fetal movements | http://snomed.info/sct |
| 69 | 395 | Condition | `Condition.code.coding` | 386661006.0 | Fever |  |
| 70 | 396 | Condition | `Condition.code.coding` | 6142004.0 | Influenza | http://snomed.info/sct |
| 71 | 397 | Condition | `Condition.code.coding` | 251846002.0 | Fluid loss | http://snomed.info/sct |
| 72 | 398 | Condition | `Condition.code.coding` | 25064002.0 | Headache | http://snomed.info/sct |
| 73 | 399 | Condition | `Condition.code.coding` | 16331000.0 | Heartburn | http://snomed.info/sct |
| 74 | 400 | Condition | `Condition.code.coding` | 417163006.0 | Traumatic or non-traumatic injury | http://snomed.info/sct |
| 75 | 401 | Condition | `Condition.code.coding` | 1279539008.0 | Victim of domestic violence | http://snomed.info/sct |
| 76 | 402 | Condition | `Condition.code.coding` | 18165001.0 | Jaundice | http://snomed.info/sct |
| 77 | 403 | Condition | `Condition.code.coding` | 449918009.0 | Cramp in lower leg | http://snomed.info/sct |
| 78 | 404 | Condition | `Condition.code.coding` | SP000414 | Kaki Kemerahan | http://terminology.kemkes.go.id/sp |
| 79 | 405 | Condition | `Condition.code.coding` | 48694002.0 | Anxiety | http://snomed.info/sct |
| 80 | 406 | Condition | `Condition.code.coding` | 35489007.0 | Depressive disorder | http://snomed.info/sct |
| 81 | 407 | Condition | `Condition.code.coding` | 413307004.0 | Mental health problem | http://snomed.info/sct |
| 82 | 408 | Condition | `Condition.code.coding` | 422587007.0 | Nausea | http://snomed.info/sct |
| 83 | 409 | Condition | `Condition.code.coding` | 267038008.0 | Edema | http://snomed.info/sct |
| 84 | 410 | Condition | `Condition.code.coding` | 131148009.0 | Bleeding |  |
| 85 | 411 | Condition | `Condition.code.coding` | 297982009.0 | Skin problem | http://snomed.info/sct |
| 86 | 412 | Condition | `Condition.code.coding` | SP000415 | Jenis Kekerasan Lainnya | http://terminology.kemkes.go.id/sp |
| 87 | 413 | Condition | `Condition.code.coding` | 21522001.0 | Abdominal pain | http://snomed.info/sct |
| 88 | 414 | Condition | `Condition.code.coding` | 49650001.0 | Dysuria | http://snomed.info/sct |
| 89 | 415 | Condition | `Condition.code.coding` | 275707000.0 | Acute pelvic pain | http://snomed.info/sct |
| 90 | 416 | Condition | `Condition.code.coding` | 47933007.0 | Foot pain | http://snomed.info/sct |
| 91 | 417 | Condition | `Condition.code.coding` | 279039007.0 | Low back pain | http://snomed.info/sct |
| 92 | 418 | Condition | `Condition.code.coding` | 203508001.0 | Bony pelvic pain | http://snomed.info/sct |
| 93 | 419 | Condition | `Condition.code.coding` | 22253000.0 | Pain | http://snomed.info/sct |
| 94 | 420 | Condition | `Condition.code.coding` | 418363000.0 | Itching of skin | http://snomed.info/sct |
| 95 | 421 | Condition | `Condition.code.coding` | 267036007.0 | Dypsnea | http://snomed.info/sct |
| 96 | 422 | Condition | `Condition.code.coding` | 84229001.0 | Fatigue | http://snomed.info/sct |
| 97 | 423 | Condition | `Condition.code.coding` | 289530006.0 | Bleeding from vagina | http://snomed.info/sct |
| 98 | 424 | Condition | `Condition.code.coding` | 397540003.0 | Visual impairment | http://snomed.info/sct |
| 99 | 425 | Condition | `Condition.code.coding` | 422400008.0 | Vomiting | http://snomed.info/sct |
| 100 | 426 | Condition | `Condition.code.coding` | 413320001.0 | Physical health problem | http://snomed.info/sct |
| 101 | 434 | Observation | `Observation.code.coding` | 82589-3 | Highest level of education | http://loinc.org |
| 102 | 435 | Observation | `Observation.valueCodeableConcept.coding` | 473463000.0 | Received elementary school education | http://snomed.info/sct |
| 103 | 436 | Observation | `Observation.valueCodeableConcept.coding` | 603435002.0 | Educated to junior high school level | http://snomed.info/sct |
| 104 | 437 | Observation | `Observation.valueCodeableConcept.coding` | 603434003.0 | Educated to senior high school level | http://snomed.info/sct |
| 105 | 438 | Observation | `Observation.valueCodeableConcept.coding` | 38861000087100.0 | Bachelor's degree achieved | http://snomed.info/sct |
| 106 | 439 | Observation | `Observation.valueCodeableConcept.coding` | 224294005.0 | No formal education | http://snomed.info/sct |
| 107 | 440 | Observation | `Observation.dataAbsentReason.coding` | unknown | Unknown | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 108 | 457 | Observation | `Observation.code.coding` | 85658-3 | Occupation [Type] | http://loinc.org |
| 109 | 458 | Observation | `Observation.valueCodeableConcept.coding` | 741062008.0 | Not in labor force | http://snomed.info/sct |
| 110 | 459 | Observation | `Observation.valueCodeableConcept.coding` | 65853000.0 | Student | http://snomed.info/sct |
| 111 | 460 | Observation | `Observation.valueCodeableConcept.coding` | 236297007.0 | Civil servant | http://snomed.info/sct |
| 112 | 461 | Observation | `Observation.valueCodeableConcept.coding` | SP000218 | Karyawan Swasta | http://terminology.kemkes.go.id/sp |
| 113 | 462 | Observation | `Observation.valueCodeableConcept.coding` | 160906004.0 | Self-employed | http://snomed.info/sct |
| 114 | 463 | Observation | `Observation.valueCodeableConcept.coding` | 444168002.0 | Homemaker | http://snomed.info/sct |
| 115 | 464 | Observation | `Observation.valueCodeableConcept.coding` | 702479006.0 | At high risk of sexually transmitted infection | http://snomed.info/sct |
| 116 | 465 | Observation | `Observation.valueCodeableConcept.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 117 | 476 | Observation | `Observation.code.coding` | 8665-2 | Last menstrual period start date | http://loinc.org |
| 118 | 477 | Observation | `Observation.code.coding` | ANC.B6.DE14 | Last menstrual period (LMP) date | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 119 | 478 | Observation | `Observation.dataAbsentReason.coding` | unknown | Unknown | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 120 | 490 | Observation | `Observation.code.coding` | 18185-9 | Gestational age | http://loinc.org |
| 121 | 491 | Observation | `Observation.code.coding` | ANC.B6.DE17 | Gestational age | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 122 | 492 | Observation | `Observation.code.coding` | 11885-1 | Gestational age Estimated from last menstrual period | http://loinc.org |
| 123 | 495 | Observation | `Observation.method.coding` | 8665-2 | Last menstrual period start date | http://loinc.org |
| 124 | 504 | Observation | `Observation.code.coding` | 11778-8 | Delivery date Estimated | http://loinc.org |
| 125 | 505 | Observation | `Observation.code.coding` | ANC.B6.DE22 | Expected date of delivery (EDD) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 126 | 506 | Observation | `Observation.code.coding` | 11779-6 | Delivery date Estimated from last menstrual period | http://loinc.org |
| 127 | 508 | Observation | `Observation.method.coding` | 8665-2 | Last menstrual period start date | http://loinc.org |
| 128 | 517 | Procedure | `Procedure.code.coding` | 88.78 | Diagnostic ultrasound of gravid uterus | http://hl7.org/fhir/sid/icd-9-cm |
| 129 | 528 | Observation | `Observation.code.coding` | 11888-5 | Gestational age US composite estimate | http://loinc.org |
| 130 | 529 | Observation | `Observation.code.coding` | ANC.B6.DE20 | Ultrasound | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 131 | 541 | Observation | `Observation.code.coding` | 11781-2 | Delivery date US composite estimate | http://loinc.org |
| 132 | 542 | Observation | `Observation.code.coding` | ANC.B6.DE40 | Hari Perkiraan Lahir (HPL) USG | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 133 | 553 | Observation | `Observation.code.coding` | 11996-6 | [#] Pregnancies | http://loinc.org |
| 134 | 554 | Observation | `Observation.code.coding` | ANC.B6.DE24 | Number of pregnancies (gravida) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 135 | 573 | Observation | `Observation.code.coding` | SP000416 | Tahun Hamil | http://terminology.kemkes.go.id/sp |
| 136 | 585 | Observation | `Observation.code.coding` | 161744009.0 | Past pregnancy history of miscarriage | http://snomed.info/sct |
| 137 | 597 | Observation | `Observation.code.coding` | 8339-4 | Birth weight Measured | http://loinc.org |
| 138 | 611 | Observation | `Observation.code.coding` | 272058002.0 | Past pregnancy history of delivery procedure | http://snomed.info/sct |
| 139 | 612 | Observation | `Observation.valueCodeableConcept.coding` | 275568006.0 | Past pregnancy history of normal delivery | http://snomed.info/sct |
| 140 | 613 | Observation | `Observation.valueCodeableConcept.coding` | 726624001.0 | Past pregnancy history of previous delivery by vacuum extraction | http://snomed.info/sct |
| 141 | 614 | Observation | `Observation.valueCodeableConcept.coding` | 161813007.0 | Past pregnancy history of previous forceps delivery | http://snomed.info/sct |
| 142 | 615 | Observation | `Observation.valueCodeableConcept.coding` | 161805006.0 | Past pregnancy history of cesarean section | http://snomed.info/sct |
| 143 | 626 | Observation | `Observation.code.coding` | SP000417 | Riwayat Penolong Persalinan Sebelumnya | http://terminology.kemkes.go.id/sp |
| 144 | 627 | Observation | `Observation.valueCodeableConcept.coding` | 303071001.0 | Person in the family | http://snomed.info/sct |
| 145 | 628 | Observation | `Observation.valueCodeableConcept.coding` | OV000012 | Dukun | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 146 | 629 | Observation | `Observation.valueCodeableConcept.coding` | 309453006.0 | Registered midwife | http://snomed.info/sct |
| 147 | 630 | Observation | `Observation.valueCodeableConcept.coding` | 309343006.0 | Physician Occupation | http://snomed.info/sct |
| 148 | 631 | Observation | `Observation.valueCodeableConcept.coding` | 11935004.0 | Obstetrician Occupation | http://snomed.info/sct |
| 149 | 632 | Observation | `Observation.valueCodeableConcept.coding` | 260413007.0 | None | http://snomed.info/sct |
| 150 | 633 | Observation | `Observation.valueCodeableConcept.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 151 | 645 | Observation | `Observation.code.coding` | 450891000124109.0 | Past pregnancy history of complication of pregnancy, childbirth and/or puerperium | http://snomed.info/sct |
| 152 | 648 | Observation | `Observation.component.code.coding` | 816150000.0 | Past pregnancy history of shoulder dystocia | http://snomed.info/sct |
| 153 | 651 | Observation | `Observation.component.code.coding` | 709881001.0 | Past pregnancy history of gestational hypertension | http://snomed.info/sct |
| 154 | 654 | Observation | `Observation.component.code.coding` | 161809000.0 | Past pregnancy history of postpartum hemorrhage | http://snomed.info/sct |
| 155 | 657 | Observation | `Observation.component.code.coding` | 161413004.0 | History of infectious disease | http://snomed.info/sct |
| 156 | 660 | Observation | `Observation.component.code.coding` | 2858002.0 | Puerperal sepsis | http://snomed.info/sct |
| 157 | 663 | Observation | `Observation.component.code.coding` | 105651000119100.0 | Past pregnancy history of pre-eclampsia | http://snomed.info/sct |
| 158 | 666 | Observation | `Observation.component.code.coding` | 161806007.0 | Past pregnancy history of eclampsia | http://snomed.info/sct |
| 159 | 669 | Observation | `Observation.component.code.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 160 | 682 | Observation | `Observation.code.coding` | SP000416 | Tahun Hamil | http://terminology.kemkes.go.id/sp |
| 161 | 694 | Observation | `Observation.code.coding` | 161744009.0 | Past pregnancy history of miscarriage | http://snomed.info/sct |
| 162 | 706 | Observation | `Observation.code.coding` | 8339-4 | Birth weight Measured | http://loinc.org |
| 163 | 721 | Observation | `Observation.code.coding` | 272058002.0 | Past pregnancy history of delivery procedure | http://snomed.info/sct |
| 164 | 722 | Observation | `Observation.valueCodeableConcept.coding` | 275568006.0 | Past pregnancy history of normal delivery | http://snomed.info/sct |
| 165 | 723 | Observation | `Observation.valueCodeableConcept.coding` | 726624001.0 | Past pregnancy history of previous delivery by vacuum extraction | http://snomed.info/sct |
| 166 | 724 | Observation | `Observation.valueCodeableConcept.coding` | 161813007.0 | Past pregnancy history of previous forceps delivery | http://snomed.info/sct |
| 167 | 725 | Observation | `Observation.valueCodeableConcept.coding` | 161805006.0 | Past pregnancy history of cesarean section | http://snomed.info/sct |
| 168 | 736 | Observation | `Observation.code.coding` | SP000417 | Riwayat Penolong Persalinan Sebelumnya | http://terminology.kemkes.go.id/sp |
| 169 | 737 | Observation | `Observation.valueCodeableConcept.coding` | 303071001.0 | Person in the family | http://snomed.info/sct |
| 170 | 738 | Observation | `Observation.valueCodeableConcept.coding` | OV000012 | Dukun | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 171 | 739 | Observation | `Observation.valueCodeableConcept.coding` | 309453006.0 | Registered midwife | http://snomed.info/sct |
| 172 | 740 | Observation | `Observation.valueCodeableConcept.coding` | 309343006.0 | Physician Occupation | http://snomed.info/sct |
| 173 | 741 | Observation | `Observation.valueCodeableConcept.coding` | 11935004.0 | Obstetrician Occupation | http://snomed.info/sct |
| 174 | 742 | Observation | `Observation.valueCodeableConcept.coding` | 260413007.0 | None | http://snomed.info/sct |
| 175 | 743 | Observation | `Observation.valueCodeableConcept.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 176 | 755 | Observation | `Observation.code.coding` | 450891000124109.0 | Past pregnancy history of complication of pregnancy, childbirth and/or puerperium | http://snomed.info/sct |
| 177 | 758 | Observation | `Observation.component.code.coding` | 816150000.0 | Past pregnancy history of shoulder dystocia | http://snomed.info/sct |
| 178 | 761 | Observation | `Observation.component.code.coding` | 709881001.0 | Past pregnancy history of gestational hypertension | http://snomed.info/sct |
| 179 | 764 | Observation | `Observation.component.code.coding` | 161809000.0 | Past pregnancy history of postpartum hemorrhage | http://snomed.info/sct |
| 180 | 767 | Observation | `Observation.component.code.coding` | 161413004.0 | History of infectious disease | http://snomed.info/sct |
| 181 | 770 | Observation | `Observation.component.code.coding` | 2858002.0 | Puerperal sepsis | http://snomed.info/sct |
| 182 | 773 | Observation | `Observation.component.code.coding` | 105651000119100.0 | Past pregnancy history of pre-eclampsia | http://snomed.info/sct |
| 183 | 776 | Observation | `Observation.component.code.coding` | 161806007.0 | Past pregnancy history of eclampsia | http://snomed.info/sct |
| 184 | 779 | Observation | `Observation.component.code.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 185 | 959 | Observation | `Observation.code.coding` | 69043-8 | Other pregnancy outcomes # | http://loinc.org |
| 186 | 960 | Observation | `Observation.code.coding` | ANC.B6.DE25 | Number of miscarriages and/or abortions | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 187 | 971 | Observation | `Observation.code.coding` | 11977-6 | [#] Parity | http://loinc.org |
| 188 | 972 | Observation | `Observation.code.coding` | ANC.B6.DE32 | Parity | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 189 | 983 | Observation | `Observation.code.coding` | 252112002.0 | Number of stillbirths | http://snomed.info/sct |
| 190 | 994 | Observation | `Observation.code.coding` | 450891000124109.0 | Past pregnancy history of complication of pregnancy, childbirth and/or puerperium | http://snomed.info/sct |
| 191 | 997 | Observation | `Observation.dataAbsentReason.coding` | unknown | Unknown | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 192 | 998 | Observation | `Observation.component.code.coding` | 709881001.0 | Past pregnancy history of gestational hypertension | http://snomed.info/sct |
| 193 | 1001 | Observation | `Observation.component.code.coding` | 105651000119100.0 | Past pregnancy history of pre-eclampsia | http://snomed.info/sct |
| 194 | 1004 | Observation | `Observation.component.code.coding` | 161806007.0 | Past pregnancy history of eclampsia | http://snomed.info/sct |
| 195 | 1007 | Observation | `Observation.component.code.coding` | 1290882004.0 | History of seizure | http://snomed.info/sct |
| 196 | 1010 | Observation | `Observation.component.code.coding` | 472971004.0 | Past pregnancy history of gestational diabetes mellitus | http://snomed.info/sct |
| 197 | 1013 | Observation | `Observation.component.code.coding` | 110483000.0 | Tobacco user | http://snomed.info/sct |
| 198 | 1016 | Observation | `Observation.component.code.coding` | 219006.0 | Current drinker of alcohol | http://snomed.info/sct |
| 199 | 1019 | Observation | `Observation.component.code.coding` | 361055000.0 | Misuses drugs | http://snomed.info/sct |
| 200 | 1022 | Observation | `Observation.component.code.coding` | 267016006.0 | History of abnormal uterine bleeding | http://snomed.info/sct |
| 201 | 1025 | Observation | `Observation.component.code.coding` | 1290170006.0 | Past pregnancy history of early neonatal death | http://snomed.info/sct |
| 202 | 1028 | Observation | `Observation.component.code.coding` | 38206000.0 | Exceptionally large at birth | http://snomed.info/sct |
| 203 | 1031 | Observation | `Observation.component.code.coding` | 161813007.0 | Past pregnancy history of previous forceps delivery | http://snomed.info/sct |
| 204 | 1034 | Observation | `Observation.component.code.coding` | 726624001.0 | Past pregnancy history of previous delivery by vacuum extraction | http://snomed.info/sct |
| 205 | 1037 | Observation | `Observation.component.code.coding` | 15758941000119102 | History of perineal laceration | http://snomed.info/sct |
| 206 | 1040 | Observation | `Observation.component.code.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 207 | 1051 | Observation | `Observation.code.coding` | 473011001.0 | Allergic condition | http://snomed.info/sct |
| 208 | 1052 | Observation | `Observation.valueCodeableConcept.coding` | 260413007.0 | None | http://snomed.info/sct |
| 209 | 1053 | Observation | `Observation.valueCodeableConcept.coding` | 716186003.0 | No known allergy | http://snomed.info/sct |
| 210 | 1054 | Observation | `Observation.valueCodeableConcept.coding` | SP000418 | Memiliki Alergi | http://terminology.kemkes.go.id/sp |
| 211 | 1093 | Observation | `Observation.component.code.coding` | 106203-3 | Allergy intolerance list | http://loinc.org |
| 212 | 1099 | Procedure | `Procedure.code.coding` | 161615003.0 | History of surgery | http://snomed.info/sct |
| 213 | 1100 | Procedure | `Procedure.code.coding` | 11401008.0 | Dilation and curettage of uterus | http://snomed.info/sct |
| 214 | 1101 | Procedure | `Procedure.code.coding` | 42010004.0 | Uterine myomectomy | http://snomed.info/sct |
| 215 | 1102 | Procedure | `Procedure.code.coding` | 387741004.0 | Excision of cyst of ovary | http://snomed.info/sct |
| 216 | 1103 | Procedure | `Procedure.code.coding` | 83152002.0 | Oophorectomy | http://snomed.info/sct |
| 217 | 1104 | Procedure | `Procedure.code.coding` | 120053002.0 | Fallopian tube excision | http://snomed.info/sct |
| 218 | 1105 | Procedure | `Procedure.code.coding` | 120038005.0 | Cervix excision | http://snomed.info/sct |
| 219 | 1106 | Procedure | `Procedure.code.coding` | 12658000.0 | Operation on female genital organs | http://snomed.info/sct |
| 220 | 1107 | Procedure | `Procedure.code.coding` | 161615003.0 | History of surgery | http://snomed.info/sct |
| 221 | 1117 | Observation | `Observation.code.coding` | 417662000.0 | History of clinical finding in subject | http://snomed.info/sct |
| 222 | 1118 | Observation | `Observation.valueCodeableConcept.coding` | 443508001.0 | No history of clinical finding in subject | http://snomed.info/sct |
| 223 | 1119 | Observation | `Observation.valueCodeableConcept.coding` | 396782006.0 | Medical history unknown | http://snomed.info/sct |
| 224 | 1120 | Observation | `Observation.valueCodeableConcept.coding` | SP000419 | Memiliki Riwayat Penyakit Terdahulu | http://terminology.kemkes.go.id/sp |
| 225 | 1130 | Condition | `Condition.code.coding` | 472968007.0 | History of autoimmune disorder of endocrine system | http://snomed.info/sct |
| 226 | 1131 | Condition | `Condition.code.coding` | 266992002.0 | History of blood disorder | http://snomed.info/sct |
| 227 | 1132 | Condition | `Condition.code.coding` | SP000420 | Riwayat Kanker Ginekologi | http://terminology.kemkes.go.id/sp |
| 228 | 1133 | Condition | `Condition.code.coding` | 266987004.0 | History of cancer | http://snomed.info/sct |
| 229 | 1134 | Condition | `Condition.code.coding` | 472971004.0 | Past pregnancy history of gestational diabetes mellitus | http://snomed.info/sct |
| 230 | 1135 | Condition | `Condition.code.coding` | 161445009.0 | History of diabetes mellitus | http://snomed.info/sct |
| 231 | 1136 | Condition | `Condition.code.coding` | 472970003.0 | History of diabetes mellitus type 1 | http://snomed.info/sct |
| 232 | 1137 | Condition | `Condition.code.coding` | 472969004.0 | History of diabetes mellitus type 2 | http://snomed.info/sct |
| 233 | 1138 | Condition | `Condition.code.coding` | 161480008.0 | History of epilepsy | http://snomed.info/sct |
| 234 | 1139 | Condition | `Condition.code.coding` | 278977008.0 | Human immunodeficiency virus status | http://snomed.info/sct |
| 235 | 1140 | Condition | `Condition.code.coding` | 161501007.0 | History of hypertension | http://snomed.info/sct |
| 236 | 1141 | Condition | `Condition.code.coding` | 275552000.0 | History of kidney disease | http://snomed.info/sct |
| 237 | 1146 | Observation | `Observation.component.code.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 238 | 1150 | Condition | `Condition.code.coding` | 161501007.0 | History of hypertension | http://snomed.info/sct |
| 239 | 1151 | Condition | `Condition.code.coding` | 275544003.0 | History of heart disorder | http://snomed.info/sct |
| 240 | 1152 | Condition | `Condition.code.coding` | 275536003.0 | History of thyroid disorder | http://snomed.info/sct |
| 241 | 1153 | Condition | `Condition.code.coding` | 161614004.0 | H/O: multiple allergies | http://snomed.info/sct |
| 242 | 1154 | Condition | `Condition.code.coding` | 107921000119107.0 | History of immune disorder | http://snomed.info/sct |
| 243 | 1155 | Condition | `Condition.code.coding` | 161445009.0 | History of diabetes mellitus | http://snomed.info/sct |
| 244 | 1156 | Condition | `Condition.code.coding` | 161527007.0 | History of asthma | http://snomed.info/sct |
| 245 | 1157 | Condition | `Condition.code.coding` | 161414005.0 | History of tuberculosis | http://snomed.info/sct |
| 246 | 1158 | Condition | `Condition.code.coding` | 429721005.0 | History of hepatitis B | http://snomed.info/sct |
| 247 | 1159 | Condition | `Condition.code.coding` | 161464003.0 | History of psychiatric disorder | http://snomed.info/sct |
| 248 | 1160 | Condition | `Condition.code.coding` | 1087151000119108 | History of syphilis | http://snomed.info/sct |
| 249 | 1161 | Condition | `Condition.code.coding` | 691501000119103.0 | History of gastritis | http://snomed.info/sct |
| 250 | 1162 | Condition | `Condition.code.coding` | 443508001.0 | No history of clinical finding in subject | http://snomed.info/sct |
| 251 | 1163 | Condition | `Condition.code.coding` | 281667005.0 | Maternal history of disorder | http://snomed.info/sct |
| 252 | 1190 | Immunization | `Immunization.vaccineCode.coding` | VG213 | COVID-19 | http://sys-ids.kemkes.go.id/kfa |
| 253 | 1207 | Immunization | `Immunization.vaccineCode` | VG213 | COVID-19 | http://sys-ids.kemkes.go.id/kfa |
| 254 | 1220 | Observation | `Observation.code.coding` | SP000422 | Status Imunisasi Tetanus | http://terminology.kemkes.go.id/sp |
| 255 | 1221 | Observation | `Observation.valueCodeableConcept.coding` | OV000283 | Imunisasi lengkap | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 256 | 1222 | Observation | `Observation.valueCodeableConcept.coding` | 171279008.0 | Immunization due | http://snomed.info/sct |
| 257 | 1223 | Observation | `Observation.valueCodeableConcept.coding` | 90351000119108.0 | Vaccination not done | http://snomed.info/sct |
| 258 | 1224 | Observation | `Observation.valueCodeableConcept.coding` | 171278000.0 | Immunization status unknown | http://snomed.info/sct |
| 259 | 1234 | Immunization | `Immunization.vaccineCode.coding` | VG139 | Td | http://sys-ids.kemkes.go.id/kfa |
| 260 | 1265 | MedicationStatement | `MedicationStatement.medicationCodeableConcept.coding` | SP000124 | Obat anti malaria | http://terminology.kemkes.go.id/sp |
| 261 | 1267 | MedicationStatement | `MedicationStatement.medicationCodeableConcept.coding` | SP000157 | Obat Diabetes Mellitus | http://terminology.kemkes.go.id/sp |
| 262 | 1278 | MedicationStatement | `MedicationStatement.medicationCodeableConcept.coding` | SP000423 | Obat Ambeien | http://terminology.kemkes.go.id/sp |
| 263 | 1292 | Observation | `Observation.code.coding` | 1208604004.0 | Caffeine intake | http://snomed.info/sct |
| 264 | 1293 | Observation | `Observation.valueCodeableConcept.coding` | SP000375 | Lebih dari 2 cangkir kopi (diseduh, disaring, instan, atau espresso) | http://terminology.kemkes.go.id/sp |
| 265 | 1294 | Observation | `Observation.valueCodeableConcept.coding` | SP000376 | Lebih dari 4 cangkir teh | http://terminology.kemkes.go.id/sp |
| 266 | 1295 | Observation | `Observation.valueCodeableConcept.coding` | SP000377 | Lebih dari 12 batang (50g) coklat | http://terminology.kemkes.go.id/sp |
| 267 | 1296 | Observation | `Observation.valueCodeableConcept.coding` | SP000378 | Lebih dari 1 kaleng soda atau minuman berenergi | http://terminology.kemkes.go.id/sp |
| 268 | 1297 | Observation | `Observation.valueCodeableConcept.coding` | 1222873005.0 | Does not use caffeine | http://snomed.info/sct |
| 269 | 1307 | Observation | `Observation.code.coding` | SP000424 | Riwayat Perilaku Berisiko Sebelum Hamil | http://terminology.kemkes.go.id/sp |
| 270 | 1309 | Observation | `Observation.dataAbsentReason` | unknown | Unknown | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 271 | 1312 | Observation | `Observation.component.code.coding` | 308658001.0 | Abnormal eating pattern | http://snomed.info/sct |
| 272 | 1315 | Observation | `Observation.component.code.coding` | 43994002.0 | Lack of physical activity | http://snomed.info/sct |
| 273 | 1318 | Observation | `Observation.component.code.coding` | SP000425 | Konsumsi Obat Teratogenik | http://terminology.kemkes.go.id/sp |
| 274 | 1321 | Observation | `Observation.component.code.coding` | SP000426 | Penggunaan Kosmetik Yang Mengandung Zat Berbahaya | http://terminology.kemkes.go.id/sp |
| 275 | 1324 | Observation | `Observation.component.code.coding` | 285140009.0 | At risk environment | http://snomed.info/sct |
| 276 | 1327 | Observation | `Observation.component.code.coding` | SP000427 | Konsumsi Alkohol atau Obat-Obatan Terlarang | http://terminology.kemkes.go.id/sp |
| 277 | 1330 | Observation | `Observation.component.code.coding` | 110483000.0 | Tobacco user | http://snomed.info/sct |
| 278 | 1333 | Observation | `Observation.component.code.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 279 | 1344 | Observation | `Observation.code.coding` | 365980008.0 | Finding of tobacco use and exposure | http://snomed.info/sct |
| 280 | 1345 | Observation | `Observation.valueCodeableConcept.coding` | 110483000.0 | Tobacco user | http://snomed.info/sct |
| 281 | 1346 | Observation | `Observation.valueCodeableConcept.coding` | 702979003.0 | Never used tobacco | http://snomed.info/sct |
| 282 | 1347 | Observation | `Observation.valueCodeableConcept.coding` | 702975009.0 | Ex-tobacco user | http://snomed.info/sct |
| 283 | 1364 | Observation | `Observation.code.coding` | 1237409004.0 | Uses condom as protection for sex | http://snomed.info/sct |
| 284 | 1375 | Procedure | `Procedure.code.coding` | 428211000124100.0 | Assessment of substance use | http://snomed.info/sct |
| 285 | 1386 | Observation | `Observation.code.coding` | SP000427 | Konsumsi Alkohol atau Obat-Obatan Terlarang | http://terminology.kemkes.go.id/sp |
| 286 | 1389 | Observation | `Observation.component.code.coding` | 219006.0 | Current drinker of alcohol | http://snomed.info/sct |
| 287 | 1392 | Observation | `Observation.component.code.coding` | 733460004.0 | Marijuana user | http://snomed.info/sct |
| 288 | 1395 | Observation | `Observation.component.code.coding` | 733461000.0 | Cocaine user | http://snomed.info/sct |
| 289 | 1398 | Observation | `Observation.component.code.coding` | SP000428 | Obat Terlarang Suntik | http://terminology.kemkes.go.id/sp |
| 290 | 1401 | Observation | `Observation.component.code.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 291 | 1421 | Condition | `Condition.code.coding` | 16932000.0 | Nausea and vomiting | http://snomed.info/sct |
| 292 | 1422 | Condition | `Condition.code.coding` | 16331000.0 | Heartburn | http://snomed.info/sct |
| 293 | 1423 | Condition | `Condition.code.coding` | 102551008.0 | Cramp in foot | http://snomed.info/sct |
| 294 | 1424 | Condition | `Condition.code.coding` | 13016151000119101 | Constipation during pregnancy | http://snomed.info/sct |
| 295 | 1425 | Condition | `Condition.code.coding` | 9121000119106.0 | Low back pain in pregnancy | http://snomed.info/sct |
| 296 | 1426 | Condition | `Condition.code.coding` | 70781000052101.0 | Pelvic girdle pain during pregnancy | http://snomed.info/sct |
| 297 | 1427 | Condition | `Condition.code.coding` | 1156031002.0 | Venous varices in pregnancy | http://snomed.info/sct |
| 298 | 1428 | Condition | `Condition.code.coding` | 237285000.0 | Gestational edema | http://snomed.info/sct |
| 299 | 1430 | Condition | `Condition.code.coding` | 289567003.0 | Vaginal discharge problem | http://snomed.info/sct |
| 300 | 1431 | Condition | `Condition.code.coding` | 230145002.0 | Difficulty breathing | http://snomed.info/sct |
| 301 | 1432 | Condition | `Condition.code.coding` | 60845006.0 | Dyspnea on exertion | http://snomed.info/sct |
| 302 | 1433 | Condition | `Condition.code.coding` | 68154008.0 | Chronic cough | http://snomed.info/sct |
| 303 | 1434 | Condition | `Condition.code.coding` | 386661006.0 | Fever | http://snomed.info/sct |
| 304 | 1435 | Condition | `Condition.code.coding` | 84229001.0 | Fatigue | http://snomed.info/sct |
| 305 | 1436 | Condition | `Condition.code.coding` | 289530006.0 | Bleeding from vagina | http://snomed.info/sct |
| 306 | 1437 | Condition | `Condition.code.coding` | 397540003.0 | Visual impairment | http://snomed.info/sct |
| 307 | 1439 | Condition | `Condition.code.coding` | 404684003.0 | Clinical finding | http://snomed.info/sct |
| 308 | 1448 | Observation | `Observation.code.coding` | 8302-2 | Body height | http://loinc.org |
| 309 | 1449 | Observation | `Observation.code.coding` | ANC.B8.DE1 | Height | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 310 | 1461 | Observation | `Observation.code.coding` | 56077-1 | Body weight --pre current pregnancy | http://loinc.org |
| 311 | 1462 | Observation | `Observation.code.coding` | ANC.B8.DE2 | Pre-gestational weight | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 312 | 1463 | Observation | `Observation.dataAbsentReason` | unknown | Unknown | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 313 | 1476 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 314 | 1477 | Observation | `Observation.code.coding` | ANC.B8.DE3 | Current weight | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 315 | 1489 | Observation | `Observation.code.coding` | OC000010 | Indeks Massa Tubuh Sebelum Hamil | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 316 | 1490 | Observation | `Observation.code.coding` | ANC.SS.DE58 | IMT Sebelum Hamil | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 317 | 1493 | Observation | `Observation.interpretation.coding` | 248342006.0 | Underweight | http://snomed.info/sct |
| 318 | 1494 | Observation | `Observation.interpretation.coding` | 43664005.0 | Normal weight | http://snomed.info/sct |
| 319 | 1495 | Observation | `Observation.interpretation.coding` | 238131007.0 | Overweight | http://snomed.info/sct |
| 320 | 1496 | Observation | `Observation.interpretation.coding` | 414915002.0 | Obese | http://snomed.info/sct |
| 321 | 1506 | Observation | `Observation.code.coding` | 284473002.0 | Mid upper arm circumference | http://snomed.info/sct |
| 322 | 1507 | Observation | `Observation.code.coding` | ANC.SS.DE3 | Lingkar Lengan Atas (LILA) | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 323 | 1519 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 324 | 1520 | Observation | `Observation.code.coding` | ANC.B8.DE17 | Systolic blood pressure | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 325 | 1532 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://loinc.org |
| 326 | 1533 | Observation | `Observation.code.coding` | ANC.B8.DE19 | Diastolic blood pressure | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 327 | 1545 | Observation | `Observation.code.coding` | 8310-5 | Body temperature | http://loinc.org |
| 328 | 1546 | Observation | `Observation.code.coding` | ANC.B8.DE34 | Body temperature | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 329 | 1558 | Observation | `Observation.code.coding` | 8867-4 | Heart Rate | http://loinc.org |
| 330 | 1559 | Observation | `Observation.code.coding` | ANC.B8.DE36 | Pulse rate | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 331 | 1571 | Observation | `Observation.code.coding` | 1237486008.0 | Pale discoloration of entire skin of body | http://snomed.info/sct |
| 332 | 1583 | Observation | `Observation.code.coding` | 10197-2 | Physical findings of Eye Narrative | http://loinc.org |
| 333 | 1584 | Observation | `Observation.code.coding` | ANC.SS.DE26 | Pemeriksaan Fisik Konjungtiva | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 334 | 1587 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 335 | 1589 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 336 | 1599 | Observation | `Observation.code.coding` | 10197-2 | Physical findings of Eye Narrative | http://loinc.org |
| 337 | 1600 | Observation | `Observation.code.coding` | ANC.SS.DE27 | Pemeriksaan Fisik Sklera | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 338 | 1603 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 339 | 1605 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 340 | 1615 | Observation | `Observation.code.coding` | 10206-1 | Physical findings of Skin Narrative | http://loinc.org |
| 341 | 1617 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 342 | 1619 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 343 | 1629 | Observation | `Observation.code.coding` | 11411-6 | Physical findings of Neck Narrative | http://loinc.org |
| 344 | 1630 | Observation | `Observation.code.coding` | ANC.SS.DE28 | Pemeriksaan Fisik Leher | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 345 | 1632 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 346 | 1634 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 347 | 1644 | Observation | `Observation.code.coding` | 423066003.0 | Finding of mouth region | http://snomed.info/sct |
| 348 | 1645 | Observation | `Observation.code.coding` | ANC.SS.DE29 | Pemeriksaan Fisik Area Mulut | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 349 | 1647 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 350 | 1649 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 351 | 1659 | Observation | `Observation.code.coding` | 297268004.0 | Ear, nose and throat finding | http://snomed.info/sct |
| 352 | 1660 | Observation | `Observation.code.coding` | ANC.SS.DE30 | Pemeriksaan Fisik Telinga Hidung dan Tenggorokan (THT) | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 353 | 1662 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 354 | 1664 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 355 | 1674 | Observation | `Observation.code.coding` | 116312005.0 | Finding of lower limb | http://snomed.info/sct |
| 356 | 1675 | Observation | `Observation.code.coding` | ANC.SS.DE34 | Pemeriksaan Fisik Tungkai | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 357 | 1677 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 358 | 1679 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 359 | 1680 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 360 | 1690 | Observation | `Observation.code.coding` | 9279-1 | Respiratory rate | http://loinc.org |
| 361 | 1691 | Observation | `Observation.code.coding` | ANC.SS.DE2 | Pernapasan | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 362 | 1703 | Observation | `Observation.code.coding` | 11412-4 | Physical findings of Respiratory system Narrative | http://loinc.org |
| 363 | 1704 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 364 | 1706 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 365 | 1708 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 366 | 1710 | Observation | `Observation.component.code.coding` | 267036007.0 | Dyspnea | http://snomed.info/sct |
| 367 | 1713 | Observation | `Observation.component.code.coding` | 49727002.0 | Cough | http://snomed.info/sct |
| 368 | 1716 | Observation | `Observation.component.code.coding` | 271823003.0 | Tachypnea | http://snomed.info/sct |
| 369 | 1719 | Observation | `Observation.component.code.coding` | 86684002.0 | Slow respiration | http://snomed.info/sct |
| 370 | 1722 | Observation | `Observation.component.code.coding` | 56018004.0 | Wheezing | http://snomed.info/sct |
| 371 | 1725 | Observation | `Observation.component.code.coding` | 48409008.0 | Respiratory crackles | http://snomed.info/sct |
| 372 | 1728 | Observation | `Observation.component.code.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 373 | 1739 | Observation | `Observation.code.coding` | 10200-4 | Physical findings of Heart Narrative | http://loinc.org |
| 374 | 1740 | Observation | `Observation.code.coding` | ANC.SS.DE31 | Pemeriksaan Fisik Dada (Auskultasi Jantung) |  |
| 375 | 1741 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 376 | 1743 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 377 | 1745 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 378 | 1747 | Observation | `Observation.component.code.coding` | 88610006.0 | Heart murmur | http://snomed.info/sct |
| 379 | 1750 | Observation | `Observation.component.code.coding` | 64661000.0 | Thready pulse | http://snomed.info/sct |
| 380 | 1753 | Observation | `Observation.component.code.coding` | 3424008.0 | Tachycardia | http://snomed.info/sct |
| 381 | 1756 | Observation | `Observation.component.code.coding` | 48867003.0 | Bradycardia | http://snomed.info/sct |
| 382 | 1759 | Observation | `Observation.component.code.coding` | 698247007.0 | Cardiac arrhythmia | http://snomed.info/sct |
| 383 | 1762 | Observation | `Observation.component.code.coding` | 3415004.0 | Cyanosis | http://snomed.info/sct |
| 384 | 1765 | Observation | `Observation.component.code.coding` | 83547004.0 | Cold sweat | http://snomed.info/sct |
| 385 | 1768 | Observation | `Observation.component.code.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 386 | 1779 | Observation | `Observation.code.coding` | 10193-1 | Physical findings of Breasts Narrative | http://loinc.org |
| 387 | 1780 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 388 | 1782 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 389 | 1784 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 390 | 1786 | Observation | `Observation.component.code.coding` | 290074005.0 | Nodule of skin of breast | http://snomed.info/sct |
| 391 | 1789 | Observation | `Observation.component.code.coding` | 271941007.0 | Discharge from the breast | http://snomed.info/sct |
| 392 | 1792 | Observation | `Observation.component.code.coding` | 238810007.0 | Flushing | http://snomed.info/sct |
| 393 | 1795 | Observation | `Observation.component.code.coding` | 112104007.0 | Localized pain | http://snomed.info/sct |
| 394 | 1798 | Observation | `Observation.component.code.coding` | 52297004.0 | Bleeding from breast | http://snomed.info/sct |
| 395 | 1801 | Observation | `Observation.component.code.coding` | 50177009.0 | Body temperature above reference range | http://snomed.info/sct |
| 396 | 1804 | Observation | `Observation.component.code.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 397 | 1815 | Observation | `Observation.code.coding` | 10191-5 | Physical findings of Abdomen Narrative | http://loinc.org |
| 398 | 1816 | Observation | `Observation.code.coding` | ANC.SS.DE33 | Pemeriksaan Fisik Perut | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 399 | 1817 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 400 | 1819 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 401 | 1821 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 402 | 1823 | Observation | `Observation.component.code.coding` | 128050000.0 | Neoplasm of abdomen | http://snomed.info/sct |
| 403 | 1826 | Observation | `Observation.component.code.coding` | SP000429 | Nyeri Saat Palpasi Ringan | http://terminology.kemkes.go.id/sp |
| 404 | 1829 | Observation | `Observation.component.code.coding` | SP000430 | Nyeri Saat Palpasi Dalam | http://terminology.kemkes.go.id/sp |
| 405 | 1832 | Observation | `Observation.component.code.coding` | SP000431 | Nyeri Saat Dekompresi | http://terminology.kemkes.go.id/sp |
| 406 | 1835 | Observation | `Observation.component.code.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 407 | 1845 | Observation | `Observation.code.coding` | 35025007.0 | Manual pelvic examination | http://snomed.info/sct |
| 408 | 1846 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 409 | 1848 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 410 | 1850 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 411 | 1852 | Observation | `Observation.component.code.coding` | 289567003.0 | Vaginal discharge problem | http://snomed.info/sct |
| 412 | 1855 | Observation | `Observation.component.code.coding` | 371380006.0 | Amniotic fluid leaking | http://snomed.info/sct |
| 413 | 1858 | Observation | `Observation.component.code.coding` | 1351322008.0 | Foul smelling amniotic fluid | http://snomed.info/sct |
| 414 | 1861 | Observation | `Observation.component.code.coding` | 25694009.0 | Papule | http://snomed.info/sct |
| 415 | 1864 | Observation | `Observation.component.code.coding` | 82515000.0 | Vesicle | http://snomed.info/sct |
| 416 | 1867 | Observation | `Observation.component.code.coding` | 427788009.0 | Ulcer of genital labium | http://snomed.info/sct |
| 417 | 1870 | Observation | `Observation.component.code.coding` | 30746006.0 | Lymphadenopathy | http://snomed.info/sct |
| 418 | 1873 | Observation | `Observation.component.code.coding` | SP000432 | Friability Cervix | http://terminology.kemkes.go.id/sp |
| 419 | 1876 | Observation | `Observation.component.code.coding` | 836474000.0 | Mucopurulent discharge | http://snomed.info/sct |
| 420 | 1879 | Observation | `Observation.component.code.coding` | 289553007.0 | Creamy vaginal discharge | http://snomed.info/sct |
| 421 | 1882 | Observation | `Observation.component.code.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 422 | 1892 | Procedure | `Procedure.code.coding` | 113023007.0 | Examination of vagina | http://snomed.info/sct |
| 423 | 1903 | Observation | `Observation.code.coding` | 177194007.0 | Manual dilation of cervix | http://snomed.info/sct |
| 424 | 1915 | Observation | `Observation.code.coding` | 364223009.0 | Vulva observable | http://snomed.info/sct |
| 425 | 1916 | Observation | `Observation.valueCodeableConcept.coding` | 17621005.0 | Normal | http://snomed.info/sct |
| 426 | 1917 | Observation | `Observation.valueCodeableConcept.coding` | 263654008.0 | Abnormal | http://snomed.info/sct |
| 427 | 1918 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 428 | 1928 | Observation | `Observation.code.coding` | 249300001.0 | Urethral finding | http://snomed.info/sct |
| 429 | 1929 | Observation | `Observation.valueCodeableConcept.coding` | 17621005.0 | Normal | http://snomed.info/sct |
| 430 | 1930 | Observation | `Observation.valueCodeableConcept.coding` | 263654008.0 | Abnormal | http://snomed.info/sct |
| 431 | 1931 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 432 | 1941 | Observation | `Observation.code.coding` | 451024007.0 | Inspection of vagina using vaginal speculum | http://snomed.info/sct |
| 433 | 1942 | Observation | `Observation.valueCodeableConcept.coding` | 17621005.0 | Normal | http://snomed.info/sct |
| 434 | 1943 | Observation | `Observation.valueCodeableConcept.coding` | 263654008.0 | Abnormal | http://snomed.info/sct |
| 435 | 1944 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 436 | 1954 | Observation | `Observation.code.coding` | 271939006.0 | Vaginal discharge | http://snomed.info/sct |
| 437 | 1955 | Observation | `Observation.method.coding` | 451024007.0 | Inspection of vagina using vaginal speculum | http://snomed.info/sct |
| 438 | 1956 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 439 | 1957 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 440 | 1958 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 441 | 1968 | Observation | `Observation.code.coding` | 289552002.0 | White vaginal discharge | http://snomed.info/sct |
| 442 | 1969 | Observation | `Observation.method.coding` | 451024007.0 | Inspection of vagina using vaginal speculum | http://snomed.info/sct |
| 443 | 1970 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 444 | 1971 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 445 | 1972 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 446 | 1982 | Observation | `Observation.code.coding` | 248910006.0 | Uterine cervix finding | http://snomed.info/sct |
| 447 | 1983 | Observation | `Observation.valueCodeableConcept.coding` | 17621005.0 | Normal | http://snomed.info/sct |
| 448 | 1984 | Observation | `Observation.valueCodeableConcept.coding` | 263654008.0 | Abnormal | http://snomed.info/sct |
| 449 | 1985 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 450 | 1995 | Observation | `Observation.code.coding` | 267038008.0 | Edema | http://snomed.info/sct |
| 451 | 2007 | Observation | `Observation.code.coding` | 44972-8 | Edema site | http://loinc.org |
| 452 | 2008 | Observation | `Observation.valueCodeableConcept.coding` | 26237000.0 | Ankle edema | http://snomed.info/sct |
| 453 | 2009 | Observation | `Observation.valueCodeableConcept.coding` | 82014009.0 | Peripheral edema | http://snomed.info/sct |
| 454 | 2010 | Observation | `Observation.valueCodeableConcept.coding` | 262703009.0 | Edema of lumbar cord | http://snomed.info/sct |
| 455 | 2011 | Observation | `Observation.valueCodeableConcept.coding` | 449615005.0 | Swelling of lower leg | http://snomed.info/sct |
| 456 | 2021 | Observation | `Observation.code.coding` | 423484008.0 | Grade of edema | http://snomed.info/sct |
| 457 | 2022 | Observation | `Observation.valueCodeableConcept.coding` | 420829009.0 | 1+ pitting edema | http://snomed.info/sct |
| 458 | 2023 | Observation | `Observation.valueCodeableConcept.coding` | 421605005.0 | 2+ pitting edema | http://snomed.info/sct |
| 459 | 2024 | Observation | `Observation.valueCodeableConcept.coding` | 421346005.0 | 3+ pitting edema | http://snomed.info/sct |
| 460 | 2025 | Observation | `Observation.valueCodeableConcept.coding` | 421129002.0 | 4+ pitting edema | http://snomed.info/sct |
| 461 | 2035 | Observation | `Observation.code.coding` | SP000433 | Usia Kehamilan Saat Pengukuran Tinggi Fundus Uteri | http://terminology.kemkes.go.id/sp |
| 462 | 2036 | Observation | `Observation.valueCodeableConcept.coding` | 313178001.0 | Gestation less than 24 weeks | http://snomed.info/sct |
| 463 | 2037 | Observation | `Observation.valueCodeableConcept.coding` | 313180007.0 | Gestation greater than 24 weeks | http://snomed.info/sct |
| 464 | 2047 | Observation | `Observation.code.coding` | 11881-0 | Uterus Fundal height Tape measure | http://loinc.org |
| 465 | 2048 | Observation | `Observation.code.coding` | ANC.B8.DE105 | Symphysis-fundal height | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 466 | 2060 | Observation | `Observation.code.coding` | 246435002.0 | Number of fetuses | http://snomed.info/sct |
| 467 | 2061 | Observation | `Observation.code.coding` | ANC.B8.DE109 | Number of fetuses | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 468 | 2067 | Observation | `Observation.dataAbsentReason` | unknown | Unknown | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 469 | 2077 | Observation | `Observation.code.coding` | 289437007.0 | Finding of fetal heart rate | http://snomed.info/sct |
| 470 | 2078 | Observation | `Observation.valueCodeableConcept.coding` | 289438002.0 | Fetal heart rate present | http://snomed.info/sct |
| 471 | 2079 | Observation | `Observation.valueCodeableConcept.coding` | 289439005.0 | Fetal heart rate absent | http://snomed.info/sct |
| 472 | 2080 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 473 | 2091 | Observation | `Observation.code.coding` | 55283-6 | Fetal Heart rate | http://loinc.org |
| 474 | 2092 | Observation | `Observation.code.coding` | ANC.B8.DE107 | Fetal heart rate | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 475 | 2125 | Observation | `Observation.code.coding` | 32279003.0 | Fetal movement finding | http://snomed.info/sct |
| 476 | 2126 | Observation | `Observation.valueCodeableConcept.coding` | 289431008.0 | Fetal movements present | http://snomed.info/sct |
| 477 | 2127 | Observation | `Observation.valueCodeableConcept.coding` | 289432001.0 | Fetal movements absent | http://snomed.info/sct |
| 478 | 2128 | Observation | `Observation.dataAbsentReason` | not-asked | Not Asked | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 479 | 2139 | Observation | `Observation.code.coding` | 364619008.0 | Measure of fetal movement | http://loinc.org |
| 480 | 2172 | Observation | `Observation.code.coding` | 72155-5 | Position in womb Fetus [RHEA] | http://loinc.org |
| 481 | 2173 | Observation | `Observation.code.coding` | ANC.B8.DE111 | Fetal presentation | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 482 | 2174 | Observation | `Observation.valueCodeableConcept.coding` | 1209182005.0 | Cephalic fetal presentation | http://snomed.info/sct |
| 483 | 2175 | Observation | `Observation.valueCodeableConcept.coding` | 6096002.0 | Breech presentation | http://terminology.kemkes.go.id/sp |
| 484 | 2176 | Observation | `Observation.valueCodeableConcept.coding` | 288203005.0 | Transverse/oblique lie | http://terminology.kemkes.go.id/sp |
| 485 | 2177 | Observation | `Observation.valueCodeableConcept.coding` | SP000006 | Organ Tubuh Lainnya | http://terminology.kemkes.go.id/sp |
| 486 | 2178 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 487 | 2213 | Procedure | `Procedure.code.coding` | 88.78 | Diagnostic ultrasound of gravid uterus | http://hl7.org/fhir/sid/icd-9-cm |
| 488 | 2227 | Observation | `Observation.code.coding` | 88.78 | Diagnostic ultrasound of gravid uterus | http://hl7.org/fhir/sid/icd-9-cm |
| 489 | 2228 | Observation | `Observation.valueCodeableConcept.coding` | 57630001.0 | First trimester pregnancy | http://snomed.info/sct |
| 490 | 2229 | Observation | `Observation.valueCodeableConcept.coding` | 59466002.0 | Second trimester pregnancy | http://snomed.info/sct |
| 491 | 2230 | Observation | `Observation.valueCodeableConcept.coding` | 41587001.0 | Third trimester pregnancy | http://snomed.info/sct |
| 492 | 2240 | Observation | `Observation.code.coding` | SP000672 | Jumlah kantong kehamilan | http://terminology.kemkes.go.id/sp |
| 493 | 2241 | Observation | `Observation.code.coding` | ANC.SS.DE36 | Gestational sac (GS) USG | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 494 | 2242 | Observation | `Observation.valueCodeableConcept.coding` | 50607009.0 | Singular | http://snomed.info/sct |
| 495 | 2243 | Observation | `Observation.valueCodeableConcept.coding` | 255204007.0 | Multiple | http://snomed.info/sct |
| 496 | 2254 | Observation | `Observation.code.coding` | 11878-6 | Number of fetuses by US | http://loinc.org |
| 497 | 2260 | Observation | `Observation.dataAbsentReason` | unknown | Unknown | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 498 | 2270 | Observation | `Observation.code.coding` | 11850-5 | Gestational sac Mean diameter US | http://loinc.org |
| 499 | 2271 | Observation | `Observation.code.coding` | ANC.SS.DE36 | Gestational sac (GS) USG | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 500 | 2284 | Observation | `Observation.code.coding` | 11957-8 | Fetal Crown Rump length US | http://loinc.org |
| 501 | 2285 | Observation | `Observation.code.coding` | ANC.SS.DE37 | Fetal Crown Rump Length (CRL) USG | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 502 | 2306 | Observation | `Observation.code.coding` | 11888-5 | Gestational age US composite estimate | http://loinc.org |
| 503 | 2307 | Observation | `Observation.code.coding` | ANC.B6.DE20 | Ultrasound | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 504 | 2319 | Observation | `Observation.code.coding` | SP000673 | Letak kantong kehamilan | http://terminology.kemkes.go.id/sp |
| 505 | 2320 | Observation | `Observation.valueCodeableConcept.coding` | 398236008.0 | Intrauterine | http://snomed.info/sct |
| 506 | 2321 | Observation | `Observation.valueCodeableConcept.coding` | 298109001.0 | Ectopic | http://snomed.info/sct |
| 507 | 2322 | Observation | `Observation.valueCodeableConcept.coding` | 1156316003.0 | Cannot be determined | http://snomed.info/sct |
| 508 | 2331 | Observation | `Observation.code.coding` | 11615-2 | Fetal Heart Activity US | http://loinc.org |
| 509 | 2332 | Observation | `Observation.valueCodeableConcept.coding` | LA9633-4 | Present | http://loinc.org |
| 510 | 2333 | Observation | `Observation.valueCodeableConcept.coding` | LA9634-2 | Absent | http://loinc.org |
| 511 | 2343 | Observation | `Observation.code.coding` | 11781-2 | Delivery date US composite estimate | http://loinc.org |
| 512 | 2344 | Observation | `Observation.code.coding` | ANC.SS.DE40 | Hari Perkiraan Lahir (HPL) USG | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 513 | 2355 | Observation | `Observation.code.coding` | 11877-8 | Fetal presentation US | http://loinc.org |
| 514 | 2356 | Observation | `Observation.valueCodeableConcept.coding` | 1209182005.0 | Cephalic fetal presentation | http://snomed.info/sct |
| 515 | 2357 | Observation | `Observation.valueCodeableConcept.coding` | 6096002.0 | Breech presentation | http://snomed.info/sct |
| 516 | 2358 | Observation | `Observation.valueCodeableConcept.coding` | 288203005.0 | Transverse/oblique lie | http://snomed.info/sct |
| 517 | 2359 | Observation | `Observation.valueCodeableConcept.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 518 | 2369 | Observation | `Observation.code.coding` | 404964004 | Antepartum fetal status | http://snomed.info/sct |
| 519 | 2370 | Observation | `Observation.valueCodeableConcept.coding` | 438949009.0 | Alive | http://snomed.info/sct |
| 520 | 2371 | Observation | `Observation.valueCodeableConcept.coding` | 419099009.0 | Dead | http://snomed.info/sct |
| 521 | 2381 | Observation | `Observation.code.coding` | 271692001 | Presentation of fetus | http://snomed.info/sct |
| 522 | 2382 | Observation | `Observation.code.coding` | ANC.SS.DE41 | Letak Janin USG | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 523 | 2383 | Observation | `Observation.valueCodeableConcept.coding` | 398236008.0 | Intrauterine | http://snomed.info/sct |
| 524 | 2384 | Observation | `Observation.valueCodeableConcept.coding` | 298109001.0 | Ectopic | http://snomed.info/sct |
| 525 | 2385 | Observation | `Observation.valueCodeableConcept.coding` | 1156316003.0 | Cannot be determined | http://snomed.info/sct |
| 526 | 2395 | Observation | `Observation.code.coding` | 11727-5 | Fetal Body weight estimated by US | http://loinc.org |
| 527 | 2396 | Observation | `Observation.code.coding[i]` | ANC.SS.DE45 | Berat janin USG | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 528 | 2409 | Observation | `Observation.code.coding` | 11948-7 | Fetal Heart rate US | http://loinc.org |
| 529 | 2410 | Observation | `Observation.code.coding` | ANC.SS.DE38 | Denyut Jantung Janin (DJJ) USG | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 530 | 2491 | Observation | `Observation.code.coding` | 77012006 | Amniotic fluid | http://loinc.org |
| 531 | 2492 | Observation | `Observation.valueCodeableConcept.coding` | 17621005.0 | Normal | http://snomed.info/sct |
| 532 | 2493 | Observation | `Observation.valueCodeableConcept.coding` | 1228877003.0 | Amniotic fluid volume below reference range | http://snomed.info/sct |
| 533 | 2494 | Observation | `Observation.valueCodeableConcept.coding` | 289293006.0 | Amniotic fluid volume above reference range | http://snomed.info/sct |
| 534 | 2504 | Observation | `Observation.code.coding` | 78067005 | Placental structure | http://snomed.info/sct |
| 535 | 2505 | Observation | `Observation.valueCodeableConcept.coding` | 17621005.0 | Normal | http://snomed.info/sct |
| 536 | 2506 | Observation | `Observation.valueCodeableConcept.coding` | 263654008.0 | Abnormal | http://snomed.info/sct |
| 537 | 2516 | Observation | `Observation.code.coding` | 11994-1 | Placenta position US | http://loinc.org |
| 538 | 2517 | Observation | `Observation.valueCodeableConcept.coding` | 36813001.0 | Placenta previa | http://snomed.info/sct |
| 539 | 2518 | Observation | `Observation.valueCodeableConcept.coding` | 445122007.0 | Low-lying placenta | http://snomed.info/sct |
| 540 | 2519 | Observation | `Observation.valueCodeableConcept.coding` | 658011000005105.0 | Position of placenta low in anterior wall of uterus | http://snomed.info/sct |
| 541 | 2520 | Observation | `Observation.valueCodeableConcept.coding` | 658031000005101.0 | Position of placenta low in posterior wall of uterus | http://snomed.info/sct |
| 542 | 2521 | Observation | `Observation.valueCodeableConcept.coding` | 658091000005102.0 | Position of placenta in right side of uterus | http://snomed.info/sct |
| 543 | 2522 | Observation | `Observation.valueCodeableConcept.coding` | 658081000005100.0 | Position of placenta in left side of uterus | http://snomed.info/sct |
| 544 | 2523 | Observation | `Observation.valueCodeableConcept.coding` | 658101000005106.0 | Position of placenta in fundus uteri | http://snomed.info/sct |
| 545 | 2524 | Observation | `Observation.valueCodeableConcept.coding` | 23952005.0 | Body of uterus structure | http://snomed.info/sct |
| 546 | 2534 | Observation | `Observation.code.coding` | 11820-8 | Fetal Head Diameter.biparietal US | http://loinc.org |
| 547 | 2535 | Observation | `Observation.code.coding` | ANC.SS.DE59 | Biparietal Diameter (BPD) USG | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 548 | 2548 | Observation | `Observation.code.coding` | 11984-2 | Fetal Head Circumference US | http://loinc.org |
| 549 | 2549 | Observation | `Observation.code.coding` | ANC.SS.DE42 | Head Circumference (HC) USG | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 550 | 2562 | Observation | `Observation.code.coding` | 11979-2 | Fetal Abdomen Circumference US | http://loinc.org |
| 551 | 2563 | Observation | `Observation.code.coding` | ANC.SS.DE43 | Abdominal Circumference (AC) USG | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 552 | 2576 | Observation | `Observation.code.coding` | 11963-6 | Fetal Femur diaphysis [Length] US | http://loinc.org |
| 553 | 2577 | Observation | `Observation.code.coding` | ANC.SS.DE44 | Femur Length (FL) USG | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 554 | 2606 | Observation | `Observation.code.coding` | 11832-3 | Fetal Amniotic fluid space Maximum diameter largest pocket US | http://loinc.org |
| 555 | 2618 | Observation | `Observation.code.coding` | 11727-5 | Fetal Body weight estimated by US | http://loinc.org |
| 556 | 2619 | Observation | `Observation.code.coding` | ANC.SS.DE45 | Berat janin USG | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 557 | 2631 | Observation | `Observation.code.coding` | 425551008.0 | Antenatal ultrasound scan for possible abnormality | http://snomed.info/sct |
| 558 | 2644 | Procedure | `Procedure.code.coding` | 88.78 | Diagnostic ultrasound of gravid uterus | http://hl7.org/fhir/sid/icd-9-cm |
| 559 | 2657 | Observation | `Observation.code.coding` | 883-9 | ABO group [Type] in Blood | http://loinc.org |
| 560 | 2658 | Observation | `Observation.code.coding` | ANC.B9.DE24 | Blood type | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 561 | 2664 | Observation | `Observation.valueCodeableConcept.coding` | LA19710-5 | Group A | http://loinc.org |
| 562 | 2665 | Observation | `Observation.valueCodeableConcept.coding` | LA19709-7 | Group B | http://loinc.org |
| 563 | 2666 | Observation | `Observation.valueCodeableConcept.coding` | LA19708-9 | Group O | http://loinc.org |
| 564 | 2667 | Observation | `Observation.valueCodeableConcept.coding` | LA28449-9 | Group AB | http://loinc.org |
| 565 | 2676 | Observation | `Observation.code.coding` | 10331-7 | Rh [Type] in Blood | http://loinc.org |
| 566 | 2677 | Observation | `Observation.code.coding` | ANC.B9.DE29 | Rh factor | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 567 | 2678 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 568 | 2679 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 569 | 2688 | Observation | `Observation.code.coding` | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 570 | 2689 | Observation | `Observation.code.coding` | ANC.B9.DE32 | HIV test | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 571 | 2695 | Observation | `Observation.valueCodeableConcept.coding` | 165816005.0 | Human immunodeficiency virus detected | http://snomed.info/sct |
| 572 | 2696 | Observation | `Observation.valueCodeableConcept.coding` | 165815009.0 | Human immunodeficiency virus not detected | http://snomed.info/sct |
| 573 | 2697 | Observation | `Observation.dataAbsentReason.coding` | 419984006.0 | Inconclusive | http://snomed.info/sct |
| 574 | 2698 | Observation | `Observation.dataAbsentReason.coding` | SP000668 | Stok Habis | http://terminology.kemkes.go.id/sp |
| 575 | 2699 | Observation | `Observation.dataAbsentReason.coding` | SP000669 | Stok Kadaluarsa | http://terminology.kemkes.go.id/sp |
| 576 | 2700 | Observation | `Observation.dataAbsentReason.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 577 | 2714 | Observation | `Observation.code.coding` | ANC.B9.DE60 | Hepatitis B test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 578 | 2715 | Observation | `Observation.code.coding` | 5196-1 | Hepatitis B virus surface Ag [Presence] in Serum or Plasma by Immunoassay | http://loinc.org |
| 579 | 2716 | Observation | `Observation.code.coding` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 580 | 2717 | Observation | `Observation.code.coding` | 712853001.0 | Antenatal screening for viral hepatitis type B | http://snomed.info/sct |
| 581 | 2718 | Observation | `Observation.method.coding` | 440500007.0 | Dried blood spot specimen | http://snomed.info/sct |
| 582 | 2719 | Observation | `Observation.code.coding` | 712853001.0 | Antenatal screening for viral hepatitis type B | http://snomed.info/sct |
| 583 | 2720 | Observation | `Observation.method.coding` | 261665006.0 | Unknown | http://snomed.info/sct |
| 584 | 2722 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 585 | 2723 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 586 | 2724 | Observation | `Observation.dataAbsentReason.coding` | SP000668 | Stok Habis | http://terminology.kemkes.go.id/sp |
| 587 | 2725 | Observation | `Observation.dataAbsentReason.coding` | SP000669 | Stok Kadaluarsa | http://terminology.kemkes.go.id/sp |
| 588 | 2726 | Observation | `Observation.dataAbsentReason.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 589 | 2741 | Observation | `Observation.code.coding` | ANC.B9.DE60 | Hepatitis B test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 590 | 2742 | Observation | `Observation.code.coding` | 11258-1 | Hepatitis B virus DNA [Units/volume] in Serum | http://loinc.org |
| 591 | 2743 | Observation | `Observation.code.coding` | 75408-5 | Hepatitis B virus e Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 592 | 2747 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 593 | 2748 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 594 | 2750 | Observation | `Observation.dataAbsentReason.coding` | SP000668 | Stok Habis | http://terminology.kemkes.go.id/sp |
| 595 | 2751 | Observation | `Observation.dataAbsentReason.coding` | SP000669 | Stok Kadaluarsa | http://terminology.kemkes.go.id/sp |
| 596 | 2752 | Observation | `Observation.dataAbsentReason.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 597 | 2767 | Observation | `Observation.code.coding` | ANC.B9.DE96 | Syphilis test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 598 | 2768 | Observation | `Observation.code.coding` | 24110-9 | Treponema pallidum Ab [Presence] in Serum by Immunoassay | http://loinc.org |
| 599 | 2769 | Observation | `Observation.code.coding` | 20507-0 | Reagin Ab [Presence] in Serum by RPR | http://loinc.org |
| 600 | 2770 | Observation | `Observation.code.coding` | 169698000.0 | Antenatal syphilis screening | http://snomed.info/sct |
| 601 | 2771 | Observation | `Observation.method.coding` | 708184003.0 | Clinical pathology service | http://snomed.info/sct |
| 602 | 2772 | Observation | `Observation.code.coding` | 169698000.0 | Antenatal syphilis screening | http://snomed.info/sct |
| 603 | 2773 | Observation | `Observation.method.coding` | 261665006.0 | Unknown | http://snomed.info/sct |
| 604 | 2775 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 605 | 2776 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 606 | 2778 | Observation | `Observation.dataAbsentReason.coding` | SP000668 | Stok Habis | http://terminology.kemkes.go.id/sp |
| 607 | 2779 | Observation | `Observation.dataAbsentReason.coding` | SP000669 | Stok Kadaluarsa | http://terminology.kemkes.go.id/sp |
| 608 | 2780 | Observation | `Observation.dataAbsentReason.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 609 | 2798 | Observation | `Observation.code.coding` | 117010004.0 | Urine culture | http://snomed.info/sct |
| 610 | 2799 | Observation | `Observation.code.coding` | 653-6 | Microscopic observation [Identifier] in Urine by Gram stain | http://loinc.org |
| 611 | 2800 | Observation | `Observation.code.coding` | 337439000.0 | Urinalysis test strips | http://snomed.info/sct |
| 612 | 2801 | Observation | `Observation.code.coding` | 5809-9 | Reducing substances [Presence] in Urine | http://loinc.org |
| 613 | 2802 | Observation | `Observation.code.coding` | 27171005.0 | Urinalysis | http://snomed.info/sct |
| 614 | 2803 | Observation | `Observation.method.coding` | 261665006.0 | Unknown | http://snomed.info/sct |
| 615 | 2805 | Observation | `Observation.valueCodeableConcept.coding` | 630-4 | Bacteria identified in Urine by Culture | http://loinc.org |
| 616 | 2806 | Observation | `Observation.valueCodeableConcept.coding` | 102104-7 | Streptococcus agalactiae [Susceptibility] in Urine by Culture | http://loinc.org |
| 617 | 2807 | Observation | `Observation.valueCodeableConcept.coding` | 260385009.0 | Negative | http://snomed.info/sct |
| 618 | 2808 | Observation | `Observation.dataAbsentReason.coding` | temp-unknown | Temporarily Unknown | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 619 | 2810 | Observation | `Observation.valueCodeableConcept.coding` | 8745002.0 | Gram-positive bacterium | http://snomed.info/sct |
| 620 | 2811 | Observation | `Observation.valueCodeableConcept.coding` | 81325006.0 | Gram-negative bacterium | http://snomed.info/sct |
| 621 | 2813 | Observation | `Observation.dataAbsentReason.coding` | SP000668 | Stok Habis | http://terminology.kemkes.go.id/sp |
| 622 | 2814 | Observation | `Observation.dataAbsentReason.coding` | SP000669 | Stok Kadaluarsa | http://terminology.kemkes.go.id/sp |
| 623 | 2815 | Observation | `Observation.dataAbsentReason.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 624 | 2823 | Observation | `Observation.component.code.coding` | 5802-4 | Nitrite [Presence] in Urine by Test strip | http://loinc.org |
| 625 | 2824 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 626 | 2825 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11841-6 | 1+ | http://loinc.org |
| 627 | 2826 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11842-4 | 2+ | http://loinc.org |
| 628 | 2827 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11843-2 | 3+ | http://loinc.org |
| 629 | 2828 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11844-0 | 4+ | http://loinc.org |
| 630 | 2829 | Observation | `Observation.component.dataAbsentReason.coding` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 631 | 2830 | Observation | `Observation.component.code.coding` | 5799-2 | Leukocyte esterase [Presence] in Urine by Test strip | http://loinc.org |
| 632 | 2831 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 633 | 2832 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11841-6 | 1+ | http://loinc.org |
| 634 | 2833 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11842-4 | 2+ | http://loinc.org |
| 635 | 2834 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11843-2 | 3+ | http://loinc.org |
| 636 | 2835 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11844-0 | 4+ | http://loinc.org |
| 637 | 2836 | Observation | `Observation.component.dataAbsentReason.coding` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 638 | 2837 | Observation | `Observation.component.code.coding` | 20454-5 | Protein [Presence] in Urine by Test strip | http://loinc.org |
| 639 | 2838 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 640 | 2839 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11841-6 | 1+ | http://loinc.org |
| 641 | 2840 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11842-4 | 2+ | http://loinc.org |
| 642 | 2841 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11843-2 | 3+ | http://loinc.org |
| 643 | 2842 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11844-0 | 4+ | http://loinc.org |
| 644 | 2843 | Observation | `Observation.component.dataAbsentReason.coding` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 645 | 2844 | Observation | `Observation.component.code.coding` | 25428-4 | Glucose [Presence] in Urine by Test strip | http://loinc.org |
| 646 | 2845 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 647 | 2846 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11841-6 | 1+ | http://loinc.org |
| 648 | 2847 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11842-4 | 2+ | http://loinc.org |
| 649 | 2848 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11843-2 | 3+ | http://loinc.org |
| 650 | 2849 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11844-0 | 4+ | http://loinc.org |
| 651 | 2850 | Observation | `Observation.component.dataAbsentReason.coding` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 652 | 2851 | Observation | `Observation.code.coding` | 5809-9 | Reducing substances [Presence] in Urine | http://loinc.org |
| 653 | 2852 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 654 | 2853 | Observation | `Observation.valueCodeableConcept.coding` | LA11841-6 | 1+ | http://loinc.org |
| 655 | 2854 | Observation | `Observation.valueCodeableConcept.coding` | LA11842-4 | 2+ | http://loinc.org |
| 656 | 2855 | Observation | `Observation.valueCodeableConcept.coding` | LA11843-2 | 3+ | http://loinc.org |
| 657 | 2856 | Observation | `Observation.valueCodeableConcept.coding` | LA11844-0 | 4+ | http://loinc.org |
| 658 | 2858 | Observation | `Observation.valueCodeableConcept.coding` | LA15255-5 | Reactive | http://loinc.org |
| 659 | 2859 | Observation | `Observation.valueCodeableConcept.coding` | LA15256-3 | Nonreactive | http://loinc.org |
| 660 | 2861 | Observation | `Observation.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 661 | 2862 | Observation | `Observation.code.coding` | ANC.B9.DE175 | Blood hemoglobin test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 662 | 2869 | Observation | `Observation.method.coding` | 26604007.0 | Complete blood count | http://snomed.info/sct |
| 663 | 2870 | Observation | `Observation.method.coding` | PC000015 | Point of Care Testing HB Meter | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 664 | 2871 | Observation | `Observation.method.coding` | 413885003.0 | Colorimetric laboratory test | http://snomed.info/sct |
| 665 | 2872 | Observation | `Observation.method.coding` | 261665006.0 | Unknown | http://snomed.info/sct |
| 666 | 2879 | Observation | `Observation.component.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 667 | 2882 | Observation | `Observation.component.code.coding` | 4544-3 | Hematocrit [Volume Fraction] of Blood by Automated count | http://loinc.org |
| 668 | 2885 | Observation | `Observation.component.code.coding` | 6690-2 | Leukocytes [#/volume] in Blood by Automated count | http://loinc.org |
| 669 | 2888 | Observation | `Observation.component.code.coding` | 96354-6 | Platelets Large [#/volume] in Blood by Automated count | http://loinc.org |
| 670 | 2898 | Observation | `Observation.dataAbsentReason.coding` | SP000668 | Stok Habis | http://terminology.kemkes.go.id/sp |
| 671 | 2899 | Observation | `Observation.dataAbsentReason.coding` | SP000669 | Stok Kadaluarsa | http://terminology.kemkes.go.id/sp |
| 672 | 2900 | Observation | `Observation.dataAbsentReason.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 673 | 2903 | Observation | `Observation.code.coding` | SP000670 | Hasil Tes HIV Pasangan | http://terminology.kemkes.go.id/sp |
| 674 | 2912 | Observation | `Observation.valueCodeableConcept.coding` | 165816005.0 | Human immunodeficiency virus detected | http://snomed.info/sct |
| 675 | 2913 | Observation | `Observation.valueCodeableConcept.coding` | 165815009.0 | Human immunodeficiency virus not detected | http://snomed.info/sct |
| 676 | 2914 | Observation | `Observation.valueCodeableConcept.coding` | 419984006.0 | Inconclusive | http://snomed.info/sct |
| 677 | 2930 | Observation | `Observation.code.coding` | ANC.B9.DE159 | Blood glucose test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 678 | 2931 | Observation | `Observation.code.coding` | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 679 | 2932 | Observation | `Observation.code.coding` | 113076002.0 | Glucose tolerance test | http://snomed.info/sct |
| 680 | 2933 | Observation | `Observation.code.coding` | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | http://loinc.org |
| 681 | 2934 | Observation | `Observation.code.coding` | 33747003.0 | Glucose measurement, blood |  |
| 682 | 2935 | Observation | `Observation.method.coding` | 261665006.0 | Unknown | http://snomed.info/sct |
| 683 | 2938 | Observation | `Observation.component.code.coding` | 1552-9 | Glucose [Mass/volume] in Serum or Plasma --pre 75 g glucose PO | http://loinc.org |
| 684 | 2941 | Observation | `Observation.component.code.coding` | 1507-3 | Glucose [Mass/volume] in Serum or Plasma --1 hour post 75 g glucose PO | http://loinc.org |
| 685 | 2944 | Observation | `Observation.component.code.coding` | 1518-0 | Glucose [Mass/volume] in Serum or Plasma --2 hours post 75 g glucose PO | http://loinc.org |
| 686 | 2955 | Observation | `Observation.code.coding` | 243787009 | Antenatal screening | http://loinc.org |
| 687 | 2976 | Procedure | `Procedure.code.coding` | 61310001.0 | Nutrition Education | http://snomed.info/sct |
| 688 | 2977 | Procedure | `Procedure.code.coding` | ED000008 | Edukasi Tanda Bahaya Kehamilan, Bersalin dan Nifas | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 689 | 2978 | Procedure | `Procedure.code.coding` | ED000009 | Edukasi IMD dan ASI Eksklusif | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 690 | 2979 | Procedure | `Procedure.code.coding` | ED000010 | Edukasi PHBS | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 691 | 2980 | Procedure | `Procedure.code.coding` | ED000011 | Edukasi KB pasca salin | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 692 | 2981 | Procedure | `Procedure.code.coding` | ED000012 | Edukasi Lainnya | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 693 | 2984 | Procedure | `Procedure.code.coding` | 385892002.0 | Mental health screening | http://snomed.info/sct |
| 694 | 2999 | Procedure | `Procedure.followUp.coding` | SP000671 | Tidak perlu dirujuk | http://terminology.kemkes.go.id/sp |
| 695 | 3007 | Observation | `Observation.valueCodeableConcept.coding` | 723509005.0 | High risk | http://snomed.info/sct |
| 696 | 3008 | Observation | `Observation.valueCodeableConcept.coding` | 723505004.0 | Low risk | http://snomed.info/sct |
| 697 | 3009 | Observation | `Observation.valueCodeableConcept.coding` | 25594002.0 | Moderate risk of | http://snomed.info/sct |
| 698 | 3010 | Observation | `Observation.dataAbsentReason` | unknown | Unknown | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 699 | 3030 | Observation | `Observation.code.coding` | 1268646002.0 | Gestational diabetes mellitus screening | http://snomed.info/sct |
| 700 | 3031 | Observation | `Observation.code.coding` | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | http://loinc.org |
| 701 | 3032 | Observation | `Observation.code.coding` | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 702 | 3033 | Observation | `Observation.code.coding` | 1521-4 | Glucose [Mass/volume] in Serum or Plasma --2 hours post meal | http://loinc.org |
| 703 | 3046 | ServiceRequest | `ServiceRequest.code.coding` | 185389009.0 | Follow-up visit | http://snomed.info/sct |
| 704 | 3047 | ServiceRequest | `ServiceRequest.code.coding` | 11429006.0 | Consultation | http://snomed.info/sct |
| 705 | 3048 | ServiceRequest | `ServiceRequest.code.coding` | 737492002.0 | Outpatient care management | http://snomed.info/sct |
| 706 | 3049 | ServiceRequest | `ServiceRequest.code.coding` | 737481003.0 | Inpatient care management | http://snomed.info/sct |
| 707 | 3050 | ServiceRequest | `ServiceRequest.code.coding` | 3457005.0 | Patient referral | http://snomed.info/sct |
| 708 | 3068 | MedicationRequest | `MedicationRequest.contained.code.coding` | 92000653.0 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula | http://sys-ids.kemkes.go.id/kf |
| 709 | 3094 | MedicationDispense | `MedicationDispense.contained.code.coding` | 93015491.0 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | http://sys-ids.kemkes.go.id/kfa |
| 710 | 3130 | Procedure | `Procedure.code.coding` | 409073007.0 | Education | http://snomed.info/sct |
| 711 | 3132 | Procedure | `Procedure.code.coding` | 409063005.0 | Counselling | http://snomed.info/sct |
| 712 | 3134 | Procedure | `Procedure.code.coding` | 103693007.0 | Diagnostic procedure | http://snomed.info/sct |
| 713 | 3136 | Procedure | `Procedure.code.coding` | 182832007.0 | Procedure related to management of drug administration | http://snomed.info/sct |
| 714 | 3138 | Procedure | `Procedure.code.coding` | 61310001.0 | Nutrition education | http://snomed.info/sct |
| 715 | 3140 | Procedure | `Procedure.code.coding` | 409011003.0 | Antenatal care management | http://snomed.info/sct |
| 716 | 3159 | CarePlan | `CarePlan.activity.detail.code.coding` | 1240781000168102 | Nutrition service | http://snomed.info/sct |
| 717 | 3160 | CarePlan | `CarePlan.activity.detail.code.coding` | 714088003.0 | Midwifery service | http://snomed.info/sct |
| 718 | 3161 | CarePlan | `CarePlan.activity.detail.code.coding` | 310066004.0 | Pediatric service | http://snomed.info/sct |
| 719 | 3162 | CarePlan | `CarePlan.activity.detail.code.coding` | 792848000.0 | Internal medicine service | http://snomed.info/sct |
| 720 | 3163 | CarePlan | `CarePlan.activity.detail.code.coding` | 788005004.0 | Neurology service | http://snomed.info/sct |
| 721 | 3164 | CarePlan | `CarePlan.activity.detail.code.coding` | 310149003.0 | Ear, nose and throat service | http://snomed.info/sct |
| 722 | 3165 | CarePlan | `CarePlan.activity.detail.code.coding` | 310116007.0 | Psychiatry service | http://snomed.info/sct |
| 723 | 3166 | CarePlan | `CarePlan.activity.detail.code.coding` | 224891009.0 | Healthcare services | http://snomed.info/sct |
| 724 | 3187 | CarePlan | `CarePlan.activity.detail.code.coding` | 48782003.0 | Delivery normal | http://snomed.info/sct |
| 725 | 3188 | CarePlan | `CarePlan.activity.detail.code.coding` | 289259007.0 | Vaginal delivery | http://snomed.info/sct |
| 726 | 3189 | CarePlan | `CarePlan.activity.detail.code.coding` | 200144004.0 | Deliveries by cesarean | http://snomed.info/sct |
| 727 | 3201 | CarePlan | `CarePlan.activity.detail.code.coding` | LA6527-1 | Intrauterine device | http://loinc.org |
| 728 | 3202 | CarePlan | `CarePlan.activity.detail.code.coding` | LA6524-8 | Oral contraceptive pill | http://loinc.org |
| 729 | 3203 | CarePlan | `CarePlan.activity.detail.code.coding` | LA6525-5 | Injectable/implantable hormone | http://loinc.org |
| 730 | 3204 | CarePlan | `CarePlan.activity.detail.code.coding` | 77543007.0 | Ligation of fallopian tube | http://snomed.info/sct |
| 731 | 3205 | CarePlan | `CarePlan.activity.detail.code.coding` | 237122005.0 | Lactational amenorrhea | http://snomed.info/sct |
| 732 | 3206 | CarePlan | `CarePlan.activity.detail.code.coding` | SP000097 | Implan | http://terminology.kemkes.go.id/sp |
| 733 | 3207 | CarePlan | `CarePlan.activity.detail.code.coding` | 408822009.0 | Contraception status not decided | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 400 |
| http://loinc.org | 136 |
| http://terminology.kemkes.go.id/sp | 71 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 28 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 27 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 25 |
| http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes | 22 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 11 |
|  | 4 |
| http://hl7.org/fhir/sid/icd-9-cm | 4 |
| http://sys-ids.kemkes.go.id/kfa | 4 |
| http://sys-ids.kemkes.go.id/kf | 1 |
| **Total** | **733** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 28 | – | Tanggal entry | – | `` |
| 45 | – | IDENTITAS IBU | – | `` |
| 84 | – | DATA IBU | – | `` |
| 108 | – | Tanggal lahir diketahui? | – | `` |
| 112 | – | calculate | – | `` |
| 140 | – | Asal Puskesmas | Organization | `Organization.active` |
| 158 | – | Tautan GPS rumah | – | `` |
| 168 | – | _Tautan GPS rumah_precision | – | `` |
| 169 | – | Foto rumah | – | `` |
| 170 | – | Nomor HP | – | `` |
| 175 | – | Alasan | – | `` |
| 207 | – | QUICK CHECK | – | `` |
| 208 | – | Tanggal posyandu | – | `` |
| 431 | – | ANC PROFILE | – | `` |
| 789 | – | Tahun hamil anak ke-3 | – | `` |
| 790 | – | Apakah ada kehilangan kehamilan (sebelum 22 minggu/ 5 bulan) di hamil anak ke-3? | – | `DST` |
| 793 | – | Berat lahir anak ke-3 | – | `` |
| 794 | – | Jenis persalinan anak ke-3 | – | `` |
| 798 | – | Penolong persalinan anak ke-3 | – | `` |
| 806 | – | Sebutkan penolong persalinan lain-lain (anak ke-3) | – | `` |
| 807 | – | Komplikasi kehamilan anak ke-3 | – | `` |
| 817 | – | Tahun hamil anak ke-4 | – | `` |
| 818 | – | Apakah ada kehilangan kehamilan (sebelum 22 minggu/ 5 bulan) di hamil anak ke-4? | – | `` |
| 821 | – | Berat lahir anak ke-4 | – | `` |
| 822 | – | Jenis persalinan anak ke-4 | – | `` |
| 826 | – | Penolong persalinan anak ke-4 | – | `` |
| 834 | – | Sebutkan penolong persalinan lain-lain (anak ke-4) | – | `` |
| 835 | – | Komplikasi kehamilan anak ke-4 | – | `` |
| 845 | – | Tahun hamil anak ke-5 | – | `` |
| 846 | – | Apakah ada kehilangan kehamilan (sebelum 22 minggu/ 5 bulan) di hamil anak ke-5? | – | `` |
| 849 | – | Berat lahir anak ke-5 | – | `` |
| 850 | – | Jenis persalinan anak ke-5 | – | `` |
| 854 | – | Penolong persalinan anak ke-5 | – | `` |
| 862 | – | Sebutkan penolong persalinan lain-lain (anak ke-5) | – | `` |
| 863 | – | Komplikasi kehamilan anak ke-5 | – | `` |
| 873 | – | Tahun hamil anak ke-6 | – | `` |
| 874 | – | Apakah ada kehilangan kehamilan (sebelum 22 minggu/ 5 bulan) di hamil anak ke-6? | – | `` |
| 877 | – | Berat lahir anak ke-6 | – | `` |
| 878 | – | Jenis persalinan anak ke-6 | – | `` |
| 882 | – | Penolong persalinan anak ke-6 | – | `` |
| 890 | – | Sebutkan penolong persalinan lain-lain (anak ke-6) | – | `` |
| 891 | – | Komplikasi kehamilan anak ke-6 | – | `` |
| 901 | – | Tahun hamil anak ke-7 | – | `` |
| 902 | – | Apakah ada kehilangan kehamilan (sebelum 22 minggu/ 5 bulan) di hamil anak ke-7? | – | `` |
| 905 | – | Berat lahir anak ke-7 | – | `` |
| 906 | – | Jenis persalinan anak ke-7 | – | `` |
| 910 | – | Penolong persalinan anak ke-7 | – | `` |
| 918 | – | Sebutkan penolong persalinan lain-lain (anak ke-7) | – | `` |
| 919 | – | Komplikasi kehamilan anak ke-7 | – | `` |
| 929 | – | Tahun hamil anak ke-8 | – | `` |
| 930 | – | Apakah ada kehilangan kehamilan (sebelum 22 minggu/ 5 bulan) di hamil anak ke-8? | – | `` |
| 933 | – | Berat lahir anak ke-8 | – | `` |
| 934 | – | Jenis persalinan anak ke-8 | – | `` |
| 938 | – | Penolong persalinan anak ke-8 | – | `` |
| 946 | – | Sebutkan penolong persalinan lain-lain (anak ke-8) | – | `` |
| 947 | – | Komplikasi kehamilan anak ke-8 | – | `` |
| 1418 | – | GEJALA DAN TINDAK LANJUT | – | `` |
| 1445 | – | PEMERIKSAAN FISIK | – | `` |
| 1709 | – | Pemeriksaan pernapasan: abnormal | – | `` |
| 1746 | – | Pemeriksaan jantung: abnormal | – | `` |
| 1785 | – | Pemeriksaan payudara: abnormal | – | `` |
| 1822 | – | Pemeriksaan abdomen: abnormal | – | `` |
| 1851 | – | Pemeriksaan panggul visual - abnormal | – | `` |
| 2103 | – | Detak jantung janin (ke-2) ada? | – | `` |
| 2107 | – | Detak Jantung Janin (ke-2) (DJJ) (kpm) | – | `` |
| 2108 | – | Detak jantung janin (ke-3) ada? | – | `` |
| 2112 | – | Detak Jantung Janin (ke-3) (DJJ) (kpm) | – | `` |
| 2113 | – | Detak jantung janin (ke-4) ada? | – | `` |
| 2117 | – | Detak Jantung Janin (ke-4) (DJJ) (kpm) | – | `` |
| 2118 | – | Detak jantung janin (ke-5) ada? | – | `` |
| 2122 | – | Detak Jantung Janin (ke-5) (DJJ) (kpm) | – | `` |
| 2150 | – | Gerakan janin (ke-2) ada? | – | `` |
| 2154 | – | Frekuensi gerakan janin (ke-2) dalam 1 jam (kali) | – | `` |
| 2155 | – | Gerakan janin (ke-3) ada? | – | `` |
| 2159 | – | Frekuensi gerakan janin (ke-3) dalam 1 jam (kali) | – | `` |
| 2160 | – | Gerakan janin (ke-4) ada? | – | `` |
| 2164 | – | Frekuensi gerakan janin (ke-4) dalam 1 jam (kali) | – | `` |
| 2165 | – | Gerakan janin (ke-5) ada? | – | `` |
| 2169 | – | Frekuensi gerakan janin (ke-5) dalam 1 jam (kali) | – | `` |
| 2187 | – | Presentasi janin (ke-2) | – | `` |
| 2193 | – | Presentasi janin (ke-3) | – | `` |
| 2199 | – | Presentasi janin (ke-4) | – | `` |
| 2205 | – | Presentasi janin (ke-5) | – | `` |
| 2211 | – | TES | – | `` |
| 2296 | – | Hasil USG: GS (Gestational Sac) janin ke-2 (mm) | – | `` |
| 2297 | – | Hasil USG: CRL (Crown-rump Length) janin ke-2 (mm) | – | `` |
| 2298 | – | Hasil USG: GS (Gestational Sac) janin ke-3 (mm) | – | `` |
| 2299 | – | Hasil USG: CRL (Crown-rump Length) janin ke-3 (mm) | – | `` |
| 2300 | – | Hasil USG: GS (Gestational Sac) janin ke-4 (mm) | – | `` |
| 2301 | – | Hasil USG: CRL (Crown-rump Length) janin ke-4 (mm) | – | `` |
| 2302 | – | Hasil USG: GS (Gestational Sac) janin ke-5 (mm) | – | `` |
| 2303 | – | Hasil USG: CRL (Crown-rump Length) janin ke-5 (mm) | – | `` |
| 2421 | – | Hasil USG: Presentasi janin ke-2 | – | `` |
| 2426 | – | Hasil USG: Status janin ke-2 | – | `` |
| 2431 | – | Hasil USG: Letak janin ke-2 | – | `` |
| 2436 | – | Hasil USG: Berat janin ke-2 | – | `` |
| 2437 | – | Hasil USG: Detak jantung janin ke-2 | – | `` |
| 2438 | – | Hasil USG: Presentasi janin ke-3 | – | `` |
| 2443 | – | Hasil USG: Status janin ke-3 | – | `` |
| 2448 | – | Hasil USG: Letak janin ke-3 | – | `` |
| 2453 | – | Hasil USG: Berat janin ke-3 | – | `` |
| 2454 | – | Hasil USG: Detak jantung janin ke-3 | – | `` |
| 2455 | – | Hasil USG: Presentasi janin ke-4 | – | `` |
| 2460 | – | Hasil USG: Status janin ke-4 | – | `` |
| 2465 | – | Hasil USG: Letak janin ke-4 | – | `` |
| 2470 | – | Hasil USG: Berat janin ke-4 | – | `` |
| 2471 | – | Hasil USG: Detak jantung janin ke-4 | – | `` |
| 2472 | – | Hasil USG: Presentasi janin ke-5 | – | `` |
| 2477 | – | Hasil USG: Status janin ke-5 | – | `` |
| 2482 | – | Hasil USG: Letak janin ke-5 | – | `` |
| 2487 | – | Hasil USG: Berat janin ke-5 | – | `` |
| 2488 | – | Hasil USG: Detak jantung janin ke-5 | – | `` |
| 2588 | – | Hasil USG: BPD (cm) janin ke-2 | – | `` |
| 2589 | – | Hasil USG: HC (cm) janin ke-2 | – | `` |
| 2590 | – | Hasil USG: AC (cm) janin ke-2 | – | `` |
| 2591 | – | Hasil USG: FL (cm) janin ke-2 | – | `` |
| 2592 | – | Hasil USG: BPD (cm) janin ke-3 | – | `` |
| 2593 | – | Hasil USG: HC (cm) janin ke-3 | – | `` |
| 2594 | – | Hasil USG: AC (cm) janin ke-3 | – | `` |
| 2595 | – | Hasil USG: FL (cm) janin ke-3 | – | `` |
| 2596 | – | Hasil USG: BPD (cm) janin ke-4 | – | `` |
| 2597 | – | Hasil USG: HC (cm) janin ke-4 | – | `` |
| 2598 | – | Hasil USG: AC (cm) janin ke-4 | – | `` |
| 2599 | – | Hasil USG: FL (cm) janin ke-4 | – | `` |
| 2600 | – | Hasil USG: BPD (cm) janin ke-5 | – | `` |
| 2601 | – | Hasil USG: HC (cm) janin ke-5 | – | `` |
| 2602 | – | Hasil USG: AC (cm) janin ke-5 | – | `` |
| 2603 | – | Hasil USG: FL (cm) janin ke-5 | – | `` |
| 2642 | – | Hasil USG: Usia kehamilan (minggu) | – | `` |
| 2721 | – | Hasil tes | – | `` |
| 2746 | – | Hasil tes lanjutan hepatitis B - Test Diagnostik Cepat HbeAg (RDT) | – | `` |
| 2749 | – | Alasan | – | `` |
| 2774 | – | Hasil tes sifilis | – | `` |
| 2777 | – | Alasan | – | `` |
| 2797 | – | Jenis tes urin | – | `` |
| 2804 | – | Hasil kultur urin midstream | – | `` |
| 2809 | – | Hasil tes pewarnaan gram urin midstream | – | `` |
| 2812 | – | Alasan tidak dilakukan tes urin | – | `` |
| 2857 | – | Hasil tes urin | – | `` |
| 2868 | – | Jenis tes HB | – | `` |
| 2897 | – | Alasan | – | `` |
| 2964 | – | KONSELING DAN SKRINING | – | `` |
| 2975 | – | Topik konseling yang didapatkan | – | `` |
| 2994 | – | Tindak lanjut hasil skrining kesehatan jiwa | – | `` |
| 2997 | – | Perlu rujukan kesehatan jiwa | – | `` |
| 3006 | – | Kesimpulan Skrining Preeklampsia | – | `` |
| 3029 | – | Jenis skrining diabetes melitus gestasional yang dilakukan | – | `` |
| 3064 | – | PEMBERIAN TABLET TAMBAH DARAH | – | `` |
| 3117 | – | TATALAKSANA KASUS PADA KEHAMILAN | – | `` |
| 3118 | – | Apakah ibu mendapatkan tindakan/pengobatan dari dokter/tenaga kesehatan? | – | `` |
| 3128 | – | Apa tindakan/pengobatan yang diberikan dokter/tenaga kesehatan? | – | `` |
