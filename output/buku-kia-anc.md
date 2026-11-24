# Output Form: Buku KIA - Identitas dan ANC (2024)

Sumber: `mapping/phdt-data-dictionary-buku-kia-anc.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-buku-kia-anc.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 206 |
| Code (`jumlah code` = 1) | 388 |
| Code unik (code + CodeSystem) | 251 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 39 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–2 | Patient | – | – | _Nama Ibu_ → `Patient.name.text` (2, tanpa BQ)<br>_Nama Ibu_ → `Patient.name.text` (6, tanpa BQ)<br>_NIK Ibu_ → `Patient.identifier.use` (13, tanpa BQ)<br>_No Buku_ → `Patient.identifier.use` (16, tanpa BQ)<br>_Tanggal Dikeluarkannya Buku_ → `Patient.identifier.period.start` (19, tanpa BQ)<br>_Alamat Rumah_ → `Patient.address.use` (30, tanpa BQ)<br>_Nomor Telepon_ → `Patient.telecom` (32, tanpa BQ)<br>_Nama Ibu_ → `Patient.name.text` (36, tanpa BQ)<br>_NIK Ibu_ → `Patient.identifier.use` (37, tanpa BQ)<br>_Tempat Lahir Ibu_ → `Patient.extension:birthPlace` (40, tanpa BQ)<br>_Tanggal Lahir Ibu_ → `Patient.birthDate` (41, tanpa BQ)<br>_Alamat Rumah_ → `Patient.address.use` (42, tanpa BQ)<br>_Kecamatan_ → `Patient.address.extension.url` (44, tanpa BQ)<br>_Kabupaten_ → `Patient.address.extension.url` (47, tanpa BQ)<br>_Telepon Ibu_ → `Patient.telecom` (50, tanpa BQ)<br>_No. Reg Ibu_ → `Patient.identifier.use` (130, tanpa BQ)<br>_No. Reg. Kohort Ibu_ → `Patient.identifier.use` (133, tanpa BQ)<br>_No. Reg. Kohort Bayi_ → `Patient.identifier.use` (136, tanpa BQ)<br>_No. Reg. Kohort Balita dan anak Pra-Sekolah_ → `Patient.identifier.use` (139, tanpa BQ)<br>_No. Catatan Medik RS Ibu_ → `Patient.identifier.use` (142, tanpa BQ) |
| 2 | 3–5 | RelatedPerson | – | – | _Nama Anak_ → `RelatedPerson.relationship` (3, tanpa BQ) |
| 3 | 7–11 | RelatedPerson | – | – | _Nama Suami_ → `RelatedPerson.relationship` (7, tanpa BQ)<br>_Nama Anak_ → `RelatedPerson.relationship` (10, tanpa BQ) |
| 4 | 12–12 | RelatedPerson | – | – | – |
| 5 | 54–60 | Coverage | – | – | _No JKN Ibu_ → `Coverage.identifier.value` (55, tanpa BQ) |
| 6 | 61–75 | Observation | 1586771000168103 | Primary healthcare service | _Puskesmas Domisili_ → `Observation.valueString` (64, tanpa BQ)<br>_Faskes Tk 1 Ibu_ → `Observation.component.code.coding` (65, tanpa BQ)<br>_Faskes Rujukan Ibu_ → `Observation.component.code.coding` (67, tanpa BQ) |
| 7 | 76–86 | Observation | 160538000 | Religious affiliation | _Agama Ibu_ → `Observation.valueString.coding` (79, tanpa BQ) |
| 8 | 87–97 | Observation | 82589-3 | Highest level of education | _Pendidikan Ibu_ → `Observation.valueString.coding` (90, tanpa BQ) |
| 9 | 98–108 | Observation | 85658-3 | Occupation [Type] | _Pekerjaan Ibu_ → `Observation.valueString.coding` (101, tanpa BQ) |
| 10 | 109–120 | Observation | 883-9 | ABO group [Type] in Blood | _Golongan Darah Ibu_ → `Observation.valueString.coding` (113, tanpa BQ) |
| 11 | 121–129 | Coverage | – | – | _Asuransi Lain Ibu_ → `Coverage.status` (121, tanpa BQ)<br>_Nomor Asuransi Lain Ibu_ → `Coverage.identifier.value` (125, tanpa BQ)<br>_Tanggal Berlaku Asuransi Ibu_ → `Coverage.period.start` (129, tanpa BQ) |
| 12 | 145–155 | Observation | SP001107 | Tanggal menerima buku KIA | _Tanggal menerima buku KIA_ → `Observation.valueDateTime` (148, tanpa BQ) |
| 13 | 156–160 | Practitioner | – | – | _Nama Tenaga kesehatan_ → `Practitioner.name` (156, tanpa BQ)<br>_No Telp tenaga kesehatan_ → `Practitioner.telecom` (157, tanpa BQ) |
| 14 | 161–166 | RelatedPerson | – | – | _Nama Suami_ → `RelatedPerson.name.text` (161, tanpa BQ)<br>_NIK Suami_ → `RelatedPerson.identifier.value` (164, tanpa BQ)<br>_Tempat Lahir Suami_ → `RelatedPerson.extension:birthPlace` (165, tanpa BQ)<br>_Tanggal Lahir Suami_ → `RelatedPerson.birthDate` (166, tanpa BQ) |
| 15 | 167–177 | Observation | 160538000 | Religious affiliation | _Agama suami_ → `Observation.valueString.coding` (170, tanpa BQ) |
| 16 | 178–185 | RelatedPerson | – | – | _Alamat Rumah Suami_ → `RelatedPerson.address.use` (178, tanpa BQ)<br>_Telepon Suami_ → `RelatedPerson.telecom` (180, tanpa BQ) |
| 17 | 186–192 | Coverage | – | – | _No JKN Suami_ → `Coverage.identifier.value` (187, tanpa BQ) |
| 18 | 193–207 | Observation | 1586771000168103 | Primary healthcare service | _Puskesmas Domisili Suami_ → `Observation.valueString` (196, tanpa BQ)<br>_Faskes Tk 1 Suami_ → `Observation.component.code.coding` (197, tanpa BQ)<br>_Faskes Rujukan Suami_ → `Observation.component.code.coding` (199, tanpa BQ) |
| 19 | 208–220 | Observation | 82589-3 | Highest level of education | _Pendidikan Suami_ → `Observation.valueString.coding` (211, tanpa BQ) |
| 20 | 221–231 | Observation | 85658-3 | Occupation [Type] | _Pekerjaan Suami_ → `Observation.valueString.coding` (224, tanpa BQ) |
| 21 | 232–242 | Observation | 883-9 | ABO group [Type] in Blood | _Golongan Darah Suami_ → `Observation.valueString.coding` (235, tanpa BQ) |
| 22 | 243–251 | Coverage | – | – | _Asuransi Lain Suami_ → `Coverage.status` (243, tanpa BQ)<br>_Nomor Asuransi Suami_ → `Coverage.identifier.value` (247, tanpa BQ)<br>_Tanggal Berlaku Asuransi Suami_ → `Coverage.period.start` (251, tanpa BQ) |
| 23 | 252–265 | RelatedPerson | – | – | _No. Catatan Medik RS Suami_ → `RelatedPerson.identifier.value` (254, tanpa BQ)<br>_Nama Anak_ → `RelatedPerson.relationship` (255, tanpa BQ)<br>_Jenis kelamin anak_ → `RelatedPerson.gender` (258, tanpa BQ)<br>_NIK Anak_ → `RelatedPerson.identifier.value` (262, tanpa BQ)<br>_No JKN Anak_ → `RelatedPerson.identifier.value` (265, tanpa BQ) |
| 24 | 266–276 | Observation | SP000674 | Fasilitas Kesehatan Tingkat Pertama (FKTP) | _Fasilitas Kesehatan Tingkat 1 Anak_ → `Observation.component.code.coding` (266, tanpa BQ)<br>_Fasilitas Kesehatan Rujukan Anak_ → `Observation.component.code.coding` (268, tanpa BQ) |
| 25 | 277–285 | RelatedPerson | – | – | _Tempat Lahir_ → `RelatedPerson.extension:birthPlace` (277, tanpa BQ)<br>_Tanggal Lahir Anak_ → `Patient.birthDate` (278, tanpa BQ)<br>_Alamat Rumah Anak_ → `RelatedPerson.address.use` (279, tanpa BQ)<br>_Telepon Anak_ → `RelatedPerson.telecom` (281, tanpa BQ) |
| 26 | 286–296 | Observation | 224098002 | Place in family order | _Anak ke-_ → `Observation.valueString.coding` (289, tanpa BQ) |
| 27 | 297–307 | Observation | 224095004 | Number of siblings | _Jumlah saudara_ → `Observation.valueString.coding` (300, tanpa BQ) |
| 28 | 308–313 | RelatedPerson | – | – | _Nomor Akte Kelahiran_ → `RelatedPerson.identifier` (308, tanpa BQ)<br>_NIK Anak_ → `RelatedPerson.identifier` (311, tanpa BQ) |
| 29 | 314–324 | Observation | 883-9 | ABO group [Type] in Blood | _Golongan Darah Anak_ → `Observation.valueString.coding` (317, tanpa BQ) |
| 30 | 325–333 | Coverage | – | – | _Asuransi Lain Anak_ → `Coverage.status` (325, tanpa BQ)<br>_Nomor Asuransi Anak_ → `Coverage.identifier.value` (329, tanpa BQ)<br>_Tanggal Berlaku Asuransi Anak_ → `Coverage.period.start` (333, tanpa BQ) |
| 31 | 334–335 | Observation | 1586771000168103 | Primary healthcare service | _Puskesmas Domisili Anak_ → `Observation.valueString` (335, tanpa BQ) |
| 32 | 336–338 | RelatedPerson | – | – | _No. Catatan Medik RS Anak_ → `RelatedPerson.identifier` (336, tanpa BQ) |
| 33 | 339–350 | Observation | 424144002 | Current chronological age | _Usia Ibu_ → `Observation.valueQuantity.value` (342, tanpa BQ) |
| 34 | 351–362 | Observation | 11996-6 | [#] Pregnancies | _Kehamilan Ke_ → `Observation.valueInteger` (355, tanpa BQ) |
| 35 | 363–373 | Observation | 726001007 | Past pregnancy history of live birth | _Jumlah Anak Lahir Hidup_ → `Observation.valueInteger` (366, tanpa BQ) |
| 36 | 374–385 | Observation | 69043-8 | Other pregnancy outcomes # | _Riwayat Keguguran_ → `Observation.valueInteger` (378, tanpa BQ) |
| 37 | 386–393 | Condition | 417662000 | History of clinical finding in subject | _Riwayat Penyakit_ → `Condition.clinicalStatus.coding` (386, tanpa BQ) |
| 38 | 394–405 | Observation | SP000775 | Usia Anak terakhir | _Anak Terakhir Umur_ → `Observation.valueQuantity.value` (397, tanpa BQ) |
| 39 | 407–418 | Observation | 8665-2 | Last menstrual period start date | _HPHT_ → `Observation.valueDateTime` (411, tanpa BQ) |
| 40 | 419–440 | Encounter | – | – | _Kunjungan Ke 1_ → `Encounter.identifier` (420, tanpa BQ)<br>_Kunjungan ke 2_ → `Encounter.identifier` (422, tanpa BQ)<br>_Kunjungan ke 3_ → `Encounter.identifier` (423, tanpa BQ)<br>_Kunjungan ke 4_ → `Encounter.identifier` (424, tanpa BQ)<br>_Kunjungan ke 5_ → `Encounter.identifier` (425, tanpa BQ)<br>_Kunjungan ke 6_ → `Encounter.identifier` (426, tanpa BQ)<br>_Tanggal Periksa_ → `Encounter.period.start` (435, tanpa BQ)<br>_Tanggal Periksa_ → `Encounter.period.start` (1136, tanpa BQ) |
| 41 | 441–448 | Condition | 134435003 | Routine antenatal care | – |
| 42 | 450–462 | Observation | 29463-7 | Body weight | _Berat Badan_ → `Observation.valueQuantity.value` (454, tanpa BQ) |
| 43 | 463–475 | Observation | 8302-2 | Body height | _Tinggi Badan_ → `Observation.valueQuantity.value` (467, tanpa BQ) |
| 44 | 476–487 | Observation | 284473002 | Mid upper arm circumference | _Lingkar Lengan Atas_ → `Observation.status` (476, tanpa BQ) |
| 45 | 488–500 | Observation | 8480-6 | Systolic blood pressure | _Tekanan Darah Sistolik_ → `Observation.valueQuantity.value` (492, tanpa BQ) |
| 46 | 501–513 | Observation | 8462-4 | Diastolic blood pressure | _Tekanan Darah Diastolik_ → `Observation.valueQuantity.value` (505, tanpa BQ) |
| 47 | 514–526 | Observation | 11881-0 | Uterus Fundal height Tape measure | _Tinggi Rahim_ → `Observation.valueQuantity.value` (518, tanpa BQ) |
| 48 | 527–538 | Observation | 72155-5 | Position in womb Fetus [RHEA] | _Letak Janin_ → `Observation.valueString.coding` (531, tanpa BQ) |
| 49 | 539–551 | Observation | 55283-6 | Fetal Heart rate | _Denyut Jantung Janin_ → `Observation.valueQuantity.value` (543, tanpa BQ) |
| 50 | 552–566 | Immunization | – | – | _Status dan Imunisasi Tetanus_ → `Immunization.status` (552, tanpa BQ) |
| 51 | 567–577 | Immunization | – | – | – |
| 52 | 578–588 | Procedure | 1230101008 | Counseling for pregnancy | _Konseling_ → `Procedure.status` (578, tanpa BQ) |
| 53 | 589–599 | Procedure | 243787009 | Antenatal screening | _Skrinning Dokter_ → `Procedure.status` (589, tanpa BQ) |
| 54 | 600–619 | MedicationRequest | 92000653 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula | _Tablet Tambah Darah_ → `MedicationRequest.contained.resourceType` (600, tanpa BQ) |
| 55 | 620–646 | MedicationDispense | 93015491 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | – |
| 56 | 647–656 | ServiceRequest | – | – | _Tes Hemoglobin_ → `ServiceRequest.category` (647, tanpa BQ) |
| 57 | 661–668 | Specimen | – | – | – |
| 58 | 669–681 | Observation | 718-7 | Hemoglobin [Mass/volume] in Blood | – |
| 59 | 682–693 | DiagnosticReport | 718-7 | Hemoglobin [Mass/volume] in Blood | – |
| 60 | 694–705 | Observation | 883-9 | ABO group [Type] in Blood | _Tes Golongan Darah_ → `Observation.valueString.coding` (698, tanpa BQ) |
| 61 | 706–715 | Procedure | 55052008 | Diagnostic ultrasound of gravid uterus | _USG_ → `Procedure.category.coding` (706, tanpa BQ) |
| 62 | 716–726 | Observation | 278977008 | Human immunodeficiency virus status | _Tripel Eliminasi HIV_ → `Observation.valueCodeableConcept.coding` (719, tanpa BQ) |
| 63 | 727–737 | Observation | 76272004 | Syphilis | _Tripel Eliminasi Sifilis_ → `Observation.valueString.coding` (730, tanpa BQ) |
| 64 | 738–749 | Observation | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | _Tripel Eliminasi Hepatitis B_ → `Observation.valueString` (742, tanpa BQ) |
| 65 | 750–760 | Observation | SP000016 | Tatalaksana Masalah Kesehatan | _Tata Laksana Kasus_ → `Observation.valueString` (753, tanpa BQ) |
| 66 | 762–771 | ServiceRequest | – | – | _Tes Lab Protein Urine_ → `ServiceRequest.category` (762, tanpa BQ) |
| 67 | 776–783 | Specimen | – | – | – |
| 68 | 784–800 | Observation | 20454-5 | Protein [Presence] in Urine by Test strip | – |
| 69 | 801–812 | DiagnosticReport | – | – | – |
| 70 | 813–822 | ServiceRequest | – | – | _Tes Gula Darah_ → `ServiceRequest.category` (813, tanpa BQ) |
| 71 | 827–834 | Specimen | – | – | – |
| 72 | 835–851 | Observation | 25428-4 | Glucose [Presence] in Urine by Test strip | – |
| 73 | 852–863 | DiagnosticReport | – | – | – |
| 74 | 866–877 | Observation | 11778-8 | Delivery date Estimated | _HPL_ → `Observation.valueDateTime` (870, tanpa BQ) |
| 75 | 878–890 | Observation | 29463-7 | Body weight | _Timbang BB dan TB_ → `Observation.status` (878, tanpa BQ)<br>_Berat Badan_ → `Observation.valueBoolean` (882, tanpa BQ) |
| 76 | 891–903 | Observation | 8302-2 | Body height | _Tinggi Badan_ → `Observation.valueBoolean` (895, tanpa BQ) |
| 77 | 904–916 | Observation | 8480-6 | Systolic blood pressure | _Ukur Tekanan Darah_ → `Observation.valueBoolean` (908, tanpa BQ) |
| 78 | 917–929 | Observation | 8462-4 | Diastolic blood pressure | – |
| 79 | 930–942 | Observation | 284473002 | Mid upper arm circumference | _Ukur LILA_ → `Observation.valueBoolean` (934, tanpa BQ) |
| 80 | 943–954 | Observation | 289625003 | Finding of fundal height of uterus | _Ukur TFU_ → `Observation.valueBoolean` (946, tanpa BQ) |
| 81 | 955–967 | Observation | 72155-5 | Position in womb Fetus [RHEA] | _Pemeriksaan presentasi bayi atau DJJ_ → `Observation.valueBoolean` (959, tanpa BQ) |
| 82 | 968–980 | Observation | 55283-6 | Fetal Heart rate | – |
| 83 | 981–992 | Observation | SP000676 | Pemberian TTD atau suplemen | _Pemberian TTD atau suplemen_ → `Observation.valueBoolean` (984, tanpa BQ) |
| 84 | 993–1005 | Observation | SP000001 | Skrining Imunisasi Tetanus Toksoid | _Status Imunisasi TT_ → `Observation.valueBoolean` (996, tanpa BQ) |
| 85 | 1006–1016 | Procedure | 385892002 | Mental health screening | _Skrinning Kesehatan Jiwa_ → `Procedure.category.coding` (1006, tanpa BQ) |
| 86 | 1017–1029 | Observation | SP000016 | Tatalaksana Masalah Kesehatan | _Tatalaksana Pelaksanaan Kasus_ → `Observation.valueBoolean` (1020, tanpa BQ) |
| 87 | 1030–1040 | Procedure | 1230101008 | Counseling for pregnancy | _Temu Wicara atau Konseling_ → `Procedure.category.coding` (1030, tanpa BQ) |
| 88 | 1041–1064 | Observation | 15220000 | Laboratory test | _Pemeriksaan Laboratorium_ → `Observation.component.valueBoolean` (1046, tanpa BQ) |
| 89 | 1065–1077 | Observation | 718-7 | Hemoglobin [Mass/volume] in Blood | _Pemeriksaan Laboratorium_ → `Observation.valueBoolean` (1069, tanpa BQ) |
| 90 | 1078–1090 | Observation | 20454-5 | Protein [Presence] in Urine by Test strip | – |
| 91 | 1091–1102 | Observation | SP001100 | Triple Eliminasi | – |
| 92 | 1103–1114 | Observation | 243787009 | Antenatal screening | – |
| 93 | 1115–1124 | Procedure | 88.78 | Diagnostic ultrasound of gravid uterus | _Pemeriksaan USG_ → `Procedure.category.coding` (1115, tanpa BQ) |
| 94 | 1125–1125 | Practitioner | – | – | _Nama Dokter_ → `Practitioner.name.text` (1125, tanpa BQ) |
| 95 | 1142–1149 | Condition | 134435003 | Routine antenatal care | – |
| 96 | 1153–1169 | Observation | OC000010 | Indeks Massa Tubuh Sebelum Hamil | _IMT_ → `Observation.valueQuantity.value` (1157, tanpa BQ) |
| 97 | 1170–1187 | Immunization | – | – | _Status Imunisasi TT_ → `Immunization.status` (1170, tanpa BQ) |
| 98 | 1188–1229 | Observation | SP000015 | Risiko Masalah Kesehatan | _Riwayat Kesehatan Ibu Sekarang_ → `Observation.component.valueBoolean` (1192, tanpa BQ) |
| 99 | 1230–1259 | Observation | SP000424 | Riwayat Perilaku Berisiko Sebelum Hamil | _Riwayat Perilaku Berisiko_ → `Observation.component.valueBoolean` (1234, tanpa BQ) |
| 100 | 1260–1301 | Observation | 281666001 | Family history of disorder | _Riwayat Penyakit Keluarga_ → `Observation.component.valueBoolean` (1264, tanpa BQ) |
| 101 | 1302–1313 | Observation | 248910006 | Uterine cervix finding | _Pemeriksaan Khusus Porsio_ → `Observation.valueCodeableConcept.coding` (1305, tanpa BQ) |
| 102 | 1314–1325 | Observation | 249300001 | Urethral finding | _Pemeriksaan Khusus Uretra_ → `Observation.valueCodeableConcept.coding` (1317, tanpa BQ) |
| 103 | 1326–1337 | Observation | 451024007 | Inspection of vagina using vaginal speculum | _Pemeriksaan Khusus Vagina_ → `Observation.valueCodeableConcept.coding` (1329, tanpa BQ) |
| 104 | 1338–1349 | Observation | 364223009 | Vulva observable | _Pemeriksaan Khusus Vulva_ → `Observation.valueCodeableConcept.coding` (1341, tanpa BQ) |
| 105 | 1350–1362 | Observation | 271939006 | Vaginal discharge | _Pemeriksaan Khusus Fluksus_ → `Observation.valueCodeableConcept.coding` (1354, tanpa BQ) |
| 106 | 1363–1375 | Observation | 289552002 | White vaginal discharge | _Pemeriksaan Khusus Fluor_ → `Observation.valueCodeableConcept.coding` (1367, tanpa BQ) |
| 107 | 1376–1388 | Observation | 93857-1 | Date and time of obstetric delivery | _Tahun Lahir_ → `Observation.valueDateTime` (1380, tanpa BQ) |
| 108 | 1389–1402 | Observation | 8339-4 | Birth weight Measured | _BB Lahir_ → `Observation.valueQuantity.value` (1392, tanpa BQ) |
| 109 | 1403–1415 | Observation | 57071-3 | Obstetric delivery method | _Proses Melahirkan_ → `Observation.valueString` (1407, tanpa BQ) |
| 110 | 1416–1428 | Observation | OC000013 | Penolong Persalinan | _Penolong Persalinan_ → `Observation.valueString` (1420, tanpa BQ) |
| 111 | 1429–1441 | Observation | 450891000124109 | Past pregnancy history of complication of pregnancy, childbirth and/or puerperium | _Masalah_ → `Observation.valueString` (1433, tanpa BQ) |
| 112 | 1446–1457 | Observation | 106167005 | Consciousness related finding | _Keadaan Umum_ → `Observation.valueString` (1449, tanpa BQ) |
| 113 | 1458–1470 | Observation | 246875002 | Conjunctival finding | _Konjungtiva_ → `Observation.status` (1458, tanpa BQ) |
| 114 | 1471–1483 | Observation | 366039006 | Finding of color of sclera | _Sklera_ → `Observation.status` (1471, tanpa BQ) |
| 115 | 1484–1496 | Observation | 106076001 | Skin finding | _Kulit_ → `Observation.status` (1484, tanpa BQ) |
| 116 | 1497–1509 | Observation | 298378000 | Finding of neck region | _Leher_ → `Observation.status` (1497, tanpa BQ) |
| 117 | 1510–1522 | Observation | 116337000 | Finding of internal part of mouth | _Gigi mulut_ → `Observation.status` (1510, tanpa BQ) |
| 118 | 1523–1535 | Observation | 297268004 | Ear, nose and throat finding | _THT_ → `Observation.status` (1523, tanpa BQ) |
| 119 | 1536–1548 | Observation | 10200-4 | Physical findings of Heart Narrative | _Jantung_ → `Observation.status` (1536, tanpa BQ) |
| 120 | 1549–1561 | Observation | 301230006 | Lung finding | _Paru_ → `Observation.status` (1549, tanpa BQ) |
| 121 | 1562–1574 | Observation | 118434000 | Stomach finding | _Perut_ → `Observation.status` (1562, tanpa BQ) |
| 122 | 1575–1587 | Observation | 116312005 | Finding of lower limb | _Tungkai_ → `Observation.status` (1575, tanpa BQ) |
| 123 | 1588–1599 | Observation | 8665-2 | Last menstrual period start date | _HPHT_ → `Observation.valueDateTime` (1592, tanpa BQ) |
| 124 | 1600–1612 | Observation | 248965005 | Finding of regularity of menstrual cycle | _Keteraturan haid_ → `Observation.status` (1600, tanpa BQ) |
| 125 | 1613–1625 | Observation | 18185-9 | Gestational age | _UK berdasarkan HPHT_ → `Observation.valueQuantity.value` (1617, tanpa BQ) |
| 126 | 1626–1637 | Observation | 11778-8 | Delivery date Estimated | _HPL berdasarkan HPHT_ → `Observation.valueDateTime` (1630, tanpa BQ) |
| 127 | 1638–1650 | Observation | 11888-5 | Gestational age US composite estimate | _UK berdasarkan USG_ → `Observation.valueQuantity.value` (1642, tanpa BQ) |
| 128 | 1651–1662 | Observation | 11781-2 | Delivery date US composite estimate | _HPL berdasarkan USG_ → `Observation.valueDateTime` (1655, tanpa BQ) |
| 129 | 1663–1674 | Observation | SP000672 | Jumlah kantong kehamilan | _Jumlah GS_ → `Observation.valueCodeableConcept.coding` (1666, tanpa BQ) |
| 130 | 1675–1693 | Observation | 11850-5 | Gestational sac Mean diameter US | _Diameter GS_ → `Observation.valueQuantity.value` (1679, tanpa BQ)<br>_Diameter GS sesuai dengan usia kehamilan (minggu)_ → `Observation.component.code.coding` (1681, tanpa BQ)<br>_Diameter GS sesuai dengan usia kehamilan (hari)_ → `Observation.component.code.coding` (1684, tanpa BQ) |
| 131 | 1694–1705 | Observation | 246435002 | Number of fetuses | _Jumlah bayi_ → `Observation.valueCodeableConcept.coding` (1697, tanpa BQ) |
| 132 | 1706–1724 | Observation | 11957-8 | Fetal Crown Rump length US | _CRL_ → `Observation.valueQuantity.value` (1710, tanpa BQ)<br>_CRL sesuai dengan usia kehamilan (minggu)_ → `Observation.component.code.coding` (1712, tanpa BQ)<br>_CRL sesuai dengan usia kehamilan (hari)_ → `Observation.component.code.coding` (1715, tanpa BQ) |
| 133 | 1725–1738 | Observation | 271692001 | Presentation of fetus | _Letak kehamilan_ → `Observation.valueCodeableConcept.coding` (1729, tanpa BQ) |
| 134 | 1739–1750 | Observation | 249042007 | Fetal heart finding | _Pulsasi jantung_ → `Observation.valueCodeableConcept.coding` (1742, tanpa BQ) |
| 135 | 1751–1763 | Observation | 28241000119109 | Ultrasonography of fetus abnormal | _Kecurigaan temuan abnormal_ → `Observation.valueBoolean` (1754, tanpa BQ)<br>_Sebutkan Kecurigaan temuan abnormal_ → `Observation.note` (1756, tanpa BQ) |
| 136 | 1765–1777 | Observation | 718-7 | Hemoglobin [Mass/volume] in Blood | _Hemoglobin_ → `Observation.valueQuantity.value` (1769, tanpa BQ)<br>_Rencana tindak lanjut_ → `Observation.note` (1771, tanpa BQ)<br>_Tanggal hasil laboratorium_ → `Observation.issued` (1775, tanpa BQ) |
| 137 | 1778–1789 | Observation | 883-9 | ABO group [Type] in Blood | _Golongan darah_ → `Observation.valueString` (1782, tanpa BQ)<br>_Rencana tindak lanjut_ → `Observation.note` (1783, tanpa BQ)<br>_Tanggal hasil laboratorium_ → `Observation.issued` (1787, tanpa BQ) |
| 138 | 1790–1802 | Observation | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | _Gula darah sewaktu_ → `Observation.valueQuantity.value` (1794, tanpa BQ)<br>_Rencana tindak lanjut_ → `Observation.note` (1796, tanpa BQ)<br>_Tanggal hasil laboratorium_ → `Observation.issued` (1800, tanpa BQ) |
| 139 | 1803–1815 | Observation | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | _HIV_ → `Observation.valueCodeableConcept.coding` (1807, tanpa BQ)<br>_Rencana tindak lanjut_ → `Observation.note` (1809, tanpa BQ)<br>_Tanggal hasil laboratorium_ → `Observation.issued` (1813, tanpa BQ) |
| 140 | 1816–1828 | Observation | 20508-8 | Reagin Ab [Units/volume] in Serum or Plasma by RPR | _Sifilis_ → `Observation.valueCodeableConcept.coding` (1820, tanpa BQ)<br>_Rencana tindak lanjut_ → `Observation.note` (1822, tanpa BQ)<br>_Tanggal hasil laboratorium_ → `Observation.issued` (1826, tanpa BQ) |
| 141 | 1829–1841 | Observation | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | _Hepatitis B_ → `Observation.valueCodeableConcept.coding` (1833, tanpa BQ)<br>_Rencana tindak lanjut_ → `Observation.note` (1835, tanpa BQ)<br>_Tanggal hasil laboratorium_ → `Observation.issued` (1839, tanpa BQ) |
| 142 | 1842–1852 | Procedure | 385892002 | Mental health screening | _Skrining kesehatan jiwa_ → `Procedure.category.coding` (1842, tanpa BQ)<br>_Tanggal skrinning kesehatan jiwa_ → `Procedure.performedPeriod.start` (1849, tanpa BQ) |
| 143 | 1853–1865 | Observation | SP000730 | Tindak lanjut hasil skrining kesehatan jiwa | _Tindak lanjut skrinning kesehatan jiwa_ → `Observation.valueBoolean` (1856, tanpa BQ)<br>_Perlu rujukan_ → `Observation.component.code.coding` (1863, tanpa BQ) |
| 144 | 1867–1883 | Observation | C54033 | Conclusion | _Kesimpulan_ → `Observation.valueString` (1877, tanpa BQ) |
| 145 | 1884–1893 | Observation | C25197 | Recommendation | _Rekomendasi_ → `Observation.valueString` (1887, tanpa BQ) |
| 146 | 1895–1906 | Observation | SP000779 | Multipara dengan kehamilan oleh pasangan baru | _Multipara dengan kehamilan oleh pasangan baru_ → `Observation.valueBoolean` (1898, tanpa BQ) |
| 147 | 1907–1918 | Observation | 813541000000100 | Pregnancy resulting from assisted conception | _Kehamilan dengan Teknologi Reproduksi Berbantu: Bayi Tabung, Obat Induksi Ovulasi_ → `Observation.valueBoolean` (1910, tanpa BQ) |
| 148 | 1919–1930 | Observation | SP000780 | Umur ≥ 35 Tahun | _Umur ≥ 35 Tahun_ → `Observation.valueBoolean` (1922, tanpa BQ) |
| 149 | 1931–1942 | Observation | 102877006 | Nulliparous | _Nulipara_ → `Observation.valueBoolean` (1934, tanpa BQ) |
| 150 | 1943–1954 | Observation | SP000781 | Multipara yang Jarak Kehamilan Sebelumnya > 10 Tahun | _Multipara yang Jarak Kehamilan Sebelumnya > 10 Tahun_ → `Observation.valueBoolean` (1946, tanpa BQ) |
| 151 | 1955–1966 | Observation | 700190003 | Family history of pre-eclampsia | _Riwayat Preeklampsia pada Ibu atau Saudara Perempuan_ → `Observation.valueBoolean` (1958, tanpa BQ) |
| 152 | 1967–1978 | Observation | 162864005 | Body mass index 30+ - obesity | _Obesitas Sebelum Hamil (IMT > 30 kg/m2)_ → `Observation.valueBoolean` (1970, tanpa BQ) |
| 153 | 1979–1990 | Observation | SP000782 | Multipara Dengan Riwayat Preeklampsia Sebelumnya | _Multipara Dengan Riwayat Preeklampsia Sebelumnya_ → `Observation.valueBoolean` (1982, tanpa BQ) |
| 154 | 1991–2002 | Observation | 16356006 | Multiple pregnancy | _Kehamilan Multipel_ → `Observation.valueBoolean` (1994, tanpa BQ) |
| 155 | 2003–2014 | Observation | 11687002 | Gestational diabetes mellitus | _Diabetes dalam Kehamilan_ → `Observation.valueBoolean` (2006, tanpa BQ) |
| 156 | 2015–2026 | Observation | 8762007 | Chronic hypertension in obstetric context | _Hipertensi Kronik_ → `Observation.valueBoolean` (2018, tanpa BQ) |
| 157 | 2027–2038 | Observation | 90708001 | Kidney disease | _Penyakit Ginjal_ → `Observation.valueBoolean` (2030, tanpa BQ) |
| 158 | 2039–2050 | Observation | 85828009 | Autoimmune disease | _Penyakit Autoimun, SLE_ → `Observation.valueBoolean` (2042, tanpa BQ) |
| 159 | 2051–2062 | Observation | 26843008 | Antiphospholipid syndrome | _Anti Phospholipid Syndrome_ → `Observation.valueBoolean` (2054, tanpa BQ) |
| 160 | 2063–2074 | Observation | SP000783 | Mean Arterial Presure > 90 mmHg | _Mean Arterial Presure > 90 mmHg_ → `Observation.valueBoolean` (2066, tanpa BQ) |
| 161 | 2075–2086 | Observation | 29738008 | Proteinuria | _Proteinuria_ → `Observation.valueBoolean` (2078, tanpa BQ) |
| 162 | 2087–2098 | Observation | SP000482 | Skrinning Preeklampsia | _Kesimpulan_ → `Observation.valueCodeableConcept.coding` (2090, tanpa BQ) |
| 163 | 2099–2112 | Observation | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | _Gula Darah Puasa_ → `Observation.valueQuantity.value` (2103, tanpa BQ)<br>_Tanggal periksa_ → `Observation.effectiveDateTime` (2108, tanpa BQ)<br>_Tanggal kunjungan_ → `Observation.issued` (2109, tanpa BQ)<br>_Dokter pemeriksa_ → `Observation.performer.reference` (2110, tanpa BQ)<br>_Rencana tindak lanjut_ → `Observation.note` (2112, tanpa BQ) |
| 164 | 2113–2126 | Observation | 1521-4 | Glucose [Mass/volume] in Serum or Plasma --2 hours post meal | _Gula Darah 2 Jam Post Prandial_ → `Observation.valueQuantity.value` (2117, tanpa BQ)<br>_Tanggal periksa_ → `Observation.effectiveDateTime` (2122, tanpa BQ)<br>_Tanggal kunjungan_ → `Observation.issued` (2123, tanpa BQ)<br>_Dokter pemeriksa_ → `Observation.performer.reference` (2124, tanpa BQ)<br>_Rencana tindak lanjut_ → `Observation.note` (2126, tanpa BQ) |
| 165 | 2127–2138 | Observation | 106167005 | Consciousness related finding | _Keadaan Umum_ → `Observation.valueString` (2130, tanpa BQ) |
| 166 | 2139–2151 | Observation | 246875002 | Conjunctival finding | _Konjungtiva_ → `Observation.status` (2139, tanpa BQ) |
| 167 | 2152–2164 | Observation | 366039006 | Finding of color of sclera | _Sklera_ → `Observation.status` (2152, tanpa BQ) |
| 168 | 2165–2177 | Observation | 106076001 | Skin finding | _Kulit_ → `Observation.status` (2165, tanpa BQ) |
| 169 | 2178–2190 | Observation | 298378000 | Finding of neck region | _Leher_ → `Observation.status` (2178, tanpa BQ) |
| 170 | 2191–2203 | Observation | 116337000 | Finding of internal part of mouth | _Gigi mulut_ → `Observation.status` (2191, tanpa BQ) |
| 171 | 2204–2216 | Observation | 297268004 | Ear, nose and throat finding | _THT_ → `Observation.status` (2204, tanpa BQ) |
| 172 | 2217–2229 | Observation | 10200-4 | Physical findings of Heart Narrative | _Jantung_ → `Observation.status` (2217, tanpa BQ) |
| 173 | 2230–2242 | Observation | 301230006 | Lung finding | _Paru_ → `Observation.status` (2230, tanpa BQ) |
| 174 | 2243–2255 | Observation | 118434000 | Stomach finding | _Perut_ → `Observation.status` (2243, tanpa BQ) |
| 175 | 2256–2268 | Observation | 116312005 | Finding of lower limb | _Tungkai_ → `Observation.status` (2256, tanpa BQ) |
| 176 | 2269–2279 | Procedure | 88.78 | Diagnostic ultrasound of gravid uterus | _USG TM 3 telah dilakukan_ → `Procedure.category.coding` (2269, tanpa BQ) |
| 177 | 2280–2293 | Observation | 11888-5 | Gestational age US composite estimate | _UK saat ini berdasarkan hasil USG TM 1_ → `Observation.valueQuantity.value` (2285, tanpa BQ) |
| 178 | 2294–2306 | Observation | 18185-9 | Gestational age | _UK saat ini berdasarkan HPHT_ → `Observation.valueQuantity.value` (2298, tanpa BQ) |
| 179 | 2307–2320 | Observation | 11888-5 | Gestational age US composite estimate | _UK berdasarkan biometri USG TM 3_ → `Observation.valueQuantity.value` (2312, tanpa BQ) |
| 180 | 2321–2332 | Observation | SP001099 | Ada selisih 3 minggu atau lebih antara UK USG TM 1/HPHT dengan UK USG TM3 | _Apakah ada selisih 3 minggu atau lebih antara UK USG TM 1/HPHT dengan UK USG TM3?_ → `Observation.valueBoolean` (2324, tanpa BQ) |
| 181 | 2333–2344 | Observation | 246435002 | Number of fetuses | _Jumlah bayi_ → `Observation.valueCodeableConcept.coding` (2336, tanpa BQ) |
| 182 | 2345–2358 | Observation | 271692001 | Presentation of fetus | _Letak bayi_ → `Observation.valueCodeableConcept.coding` (2349, tanpa BQ) |
| 183 | 2359–2372 | Observation | 72155-5 | Position in womb Fetus [RHEA] | _Presentasi bayi_ → `Observation.valueCodeableConcept.coding` (2363, tanpa BQ) |
| 184 | 2373–2384 | Observation | 404964004 | Antepartum fetal status | _Keadaan bayi_ → `Observation.valueCodeableConcept.coding` (2376, tanpa BQ) |
| 185 | 2385–2399 | Observation | 55283-6 | Fetal Heart rate | _DJJ_ → `Observation.valueQuantity.value` (2389, tanpa BQ) |
| 186 | 2400–2413 | Observation | 11994-1 | Placenta position US | _Lokasi plasenta_ → `Observation.valueCodeableConcept.coding` (2403, tanpa BQ) |
| 187 | 2414–2428 | Observation | 3156-7 | Volume of Amniotic fluid | _Jumlah cairan ketuban (SPD) cm_ → `Observation.valueQuantity.value` (2417, tanpa BQ) |
| 188 | 2429–2444 | Observation | 11820-8 | Fetal Head Diameter.biparietal US | _BPD (cm)_ → `Observation.valueQuantity.value` (2433, tanpa BQ)<br>_BPD (Sesuai ... minggu)_ → `Observation.component.coding` (2435, tanpa BQ) |
| 189 | 2445–2460 | Observation | 11984-2 | Fetal Head Circumference US | _HC (cm)_ → `Observation.valueQuantity.value` (2449, tanpa BQ)<br>_HC (Sesuai ... minggu)_ → `Observation.component.coding` (2451, tanpa BQ) |
| 190 | 2461–2476 | Observation | 11979-2 | Fetal Abdomen Circumference US | _AC (cm)_ → `Observation.valueQuantity.value` (2465, tanpa BQ)<br>_AC (Sesuai ... minggu)_ → `Observation.component.coding` (2467, tanpa BQ) |
| 191 | 2477–2492 | Observation | 11963-6 | Fetal Femur diaphysis [Length] US | _FL (cm)_ → `Observation.valueQuantity.value` (2481, tanpa BQ)<br>_FL (Sesuai ... minggu)_ → `Observation.component.coding` (2483, tanpa BQ) |
| 192 | 2493–2508 | Observation | 11727-5 | Fetal Body weight estimated by US | _EFW/TBJ (g)_ → `Observation.valueQuantity.value` (2497, tanpa BQ)<br>_EFW/TBJ (Sesuai ... minggu)_ → `Observation.component.coding` (2499, tanpa BQ) |
| 193 | 2509–2521 | Observation | 28241000119109 | Ultrasonography of fetus abnormal | _Kecurigaan temuan abnormal_ → `Observation.valueBoolean` (2512, tanpa BQ)<br>_Sebutkan temuan abnormal_ → `Observation.note` (2514, tanpa BQ) |
| 194 | 2522–2532 | Observation | 11525-3 | US for pregnancy | _Hasil USG_ → `Observation.valueString` (2525, tanpa BQ) |
| 195 | 2533–2546 | Observation | 718-7 | Hemoglobin [Mass/volume] in Blood | _Hemoglobin_ → `Observation.valueQuantity.value` (2537, tanpa BQ)<br>_Tanggal Pemeriksaan Lab_ → `Observation.effectiveDateTime` (2542, tanpa BQ)<br>_Rencana Tindak Lanjut_ → `Observation.note` (2546, tanpa BQ) |
| 196 | 2547–2560 | Observation | 5804-0 | Protein [Mass/volume] in Urine by Test strip | _Protein Urin_ → `Observation.valueQuantity.value` (2551, tanpa BQ)<br>_Tanggal Pemeriksaan Lab_ → `Observation.effectiveDateTime` (2556, tanpa BQ)<br>_Rencana Tindak Lanjut_ → `Observation.note` (2560, tanpa BQ) |
| 197 | 2561–2577 | Observation | 20454-5 | Protein [Presence] in Urine by Test strip | _Urin Reduksi_ → `Observation.valueCodeableConcept.coding` (2565, tanpa BQ)<br>_Tanggal Pemeriksaan Lab_ → `Observation.effectiveDateTime` (2573, tanpa BQ)<br>_Rencana Tindak Lanjut_ → `Observation.note` (2577, tanpa BQ) |
| 198 | 2578–2588 | Procedure | 385892002 | Mental health screening | _Skrining kesehatan jiwa_ → `Procedure.category.coding` (2578, tanpa BQ)<br>_Tanggal skrinning kesehatan jiwa_ → `Procedure.performedPeriod.start` (2585, tanpa BQ) |
| 199 | 2589–2608 | Observation | SP000730 | Tindak lanjut hasil skrining kesehatan jiwa | _Tindak lanjut skrinning kesehatan jiwa_ → `Observation.valueBoolean` (2592, tanpa BQ)<br>_Perlu Rujukan_ → `Observation.component.code.coding` (2599, tanpa BQ)<br>_Tanggal skrinning kesehatan jiwa_ → `Observation.effectiveDateTime` (2605, tanpa BQ) |
| 200 | 2609–2633 | CarePlan | – | – | _Rencana Konsultasi Lanjut_ → `CarePlan.title` (2609, tanpa BQ)<br>_Rencana Proses Melahirkan_ → `CarePlan.status` (2629, tanpa BQ)<br>_Penjelasan_ → `CarePlan.description` (2633, tanpa BQ) |
| 201 | 2634–2647 | CarePlan | – | – | _Pilihan rencana kontrasepsi_ → `CarePlan.status` (2644, tanpa BQ) |
| 202 | 2648–2661 | CarePlan | – | – | – |
| 203 | 2662–2673 | Observation | 306225008 | Referral to counseling service | _Kebutuhan Konseling_ → `Observation.valueBoolean` (2665, tanpa BQ) |
| 204 | 2674–2685 | Observation | 310585007 | Delivery place planned | _Rekomendasi Tempat Proses Melahirkan_ → `Observation.valueCodeableConcept.coding` (2677, tanpa BQ) |
| 205 | 2686–2696 | Observation | 89241-4 | Obstetrics Note | _Keluhan, Pemeriksaan, Tindakan dan Saran_ → `Observation.valueString` (2689, tanpa BQ)<br>_Tanggal periksa_ → `Observation.effectiveDateTime` (2693, tanpa BQ) |
| 206 | 2697–2706 | ServiceRequest | – | – | _Tanggal kembali_ → `ServiceRequest.occurrenceDateTime` (2697, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 158 |
| RelatedPerson | 9 |
| Procedure | 9 |
| Coverage | 5 |
| ServiceRequest | 4 |
| Condition | 3 |
| Immunization | 3 |
| Specimen | 3 |
| DiagnosticReport | 3 |
| CarePlan | 3 |
| Practitioner | 2 |
| Patient | 1 |
| Encounter | 1 |
| MedicationRequest | 1 |
| MedicationDispense | 1 |
| **Total** | **206** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 63 | Observation | `Observation.code.coding` | 1586771000168103 | Primary healthcare service | http://snomed.info/sct |
| 2 | 65 | Observation | `Observation.component.code.coding` | SP000674 | Fasilitas Kesehatan Tingkat Pertama (FKTP) | http://terminology.kemkes.go.id/sp |
| 3 | 67 | Observation | `Observation.component.code.coding` | SP000675 | Fasilitas Kesehatan Rujukan Tingkat Lanjutan (FKRTL) | http://terminology.kemkes.go.id/sp |
| 4 | 78 | Observation | `Observation.code.coding` | 160538000 | Religious affiliation | http://snomed.info/sct |
| 5 | 89 | Observation | `Observation.code.coding` | 82589-3 | Highest level of education | http://loinc.org |
| 6 | 100 | Observation | `Observation.code.coding` | 85658-3 | Occupation [Type] | http://loinc.org |
| 7 | 111 | Observation | `Observation.code.coding` | 883-9 | ABO group [Type] in Blood | http://loinc.org |
| 8 | 112 | Observation | `Observation.code.coding` | ANC.B9.DE24 | Blood type | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 9 | 147 | Observation | `Observation.code.coding` | SP001107 | Tanggal menerima buku KIA | http://terminology.kemkes.go.id/sp |
| 10 | 169 | Observation | `Observation.code.coding` | 160538000 | Religious affiliation | http://snomed.info/sct |
| 11 | 195 | Observation | `Observation.code.coding` | 1586771000168103 | Primary healthcare service | http://snomed.info/sct |
| 12 | 197 | Observation | `Observation.component.code.coding` | SP000674 | Fasilitas Kesehatan Tingkat Pertama (FKTP) | http://terminology.kemkes.go.id/sp |
| 13 | 199 | Observation | `Observation.component.code.coding` | SP000675 | Fasilitas Kesehatan Rujukan Tingkat Lanjutan (FKRTL) | http://terminology.kemkes.go.id/sp |
| 14 | 210 | Observation | `Observation.code.coding` | 82589-3 | Highest level of education | http://loinc.org |
| 15 | 223 | Observation | `Observation.code.coding` | 85658-3 | Occupation [Type] | http://loinc.org |
| 16 | 234 | Observation | `Observation.code.coding` | 883-9 | ABO group [Type] in Blood | http://loinc.org |
| 17 | 266 | Observation | `Observation.component.code.coding` | SP000674 | Fasilitas Kesehatan Tingkat Pertama (FKTP) | http://terminology.kemkes.go.id/sp |
| 18 | 268 | Observation | `Observation.component.code.coding` | SP000675 | Fasilitas Kesehatan Rujukan Tingkat Lanjutan (FKRTL) | http://terminology.kemkes.go.id/sp |
| 19 | 288 | Observation | `Observation.code.coding` | 224098002 | Place in family order | http://snomed.info/sct |
| 20 | 299 | Observation | `Observation.code.coding` | 224095004 | Number of siblings | http://snomed.info/sct |
| 21 | 316 | Observation | `Observation.code.coding` | 883-9 | ABO group [Type] in Blood | http://loinc.org |
| 22 | 334 | Observation | `Observation.code.coding` | 1586771000168103 | Primary healthcare service | http://snomed.info/sct |
| 23 | 341 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 24 | 353 | Observation | `Observation.code.coding` | 11996-6 | [#] Pregnancies | http://loinc.org |
| 25 | 354 | Observation | `Observation.code.coding` | ANC.B6.DE24 | Number of pregnancies (gravida) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 26 | 365 | Observation | `Observation.code.coding` | 726001007 | Past pregnancy history of live birth | http://snomed.info/sct |
| 27 | 376 | Observation | `Observation.code.coding` | 69043-8 | Other pregnancy outcomes # | http://loinc.org |
| 28 | 377 | Observation | `Observation.code.coding` | ANC.B6.DE25 | Number of miscarriages and/or abortions | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 29 | 388 | Condition | `Condition.code.coding` | 417662000 | History of clinical finding in subject | http://snomed.info/sct |
| 30 | 396 | Observation | `Observation.code.coding` | SP000775 | Usia Anak terakhir | http://terminology.kemkes.go.id/sp |
| 31 | 409 | Observation | `Observation.code.coding` | 8665-2 | Last menstrual period start date | http://loinc.org |
| 32 | 410 | Observation | `Observation.code.coding` | ANC.B6.DE14 | Last menstrual period (LMP) date | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 33 | 420 | Encounter | `Encounter.identifier` | K1A | Kunjungan K1 akses | http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC |
| 34 | 422 | Encounter | `Encounter.identifier` | K2 | Kunjungan K2 | http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC |
| 35 | 423 | Encounter | `Encounter.identifier` | K3 | Kunjungan K3 | http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC |
| 36 | 424 | Encounter | `Encounter.identifier` | K4 | Kunjungan K4 | http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC |
| 37 | 425 | Encounter | `Encounter.identifier` | K5 | Kunjungan K5 | http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC |
| 38 | 426 | Encounter | `Encounter.identifier` | K6 | Kunjungan K6 | http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC |
| 39 | 443 | Condition | `Condition.code.coding` | 134435003 | Routine antenatal care | http://snomed.info/sct |
| 40 | 452 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 41 | 453 | Observation | `Observation.code.coding` | ANC.B8.DE3 | Current weight | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 42 | 465 | Observation | `Observation.code.coding` | 8302-2 | Body height | http://loinc.org |
| 43 | 466 | Observation | `Observation.code.coding` | ANC.B8.DE1 | Height | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 44 | 478 | Observation | `Observation.code.coding` | 284473002 | Mid upper arm circumference | http://snomed.info/sct |
| 45 | 479 | Observation | `Observation.code.coding` | ANC.SS.DE3 | Lingkar Lengan Atas (LILA) | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 46 | 490 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 47 | 491 | Observation | `Observation.code.coding` | ANC.B8.DE17 | Systolic blood pressure | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 48 | 503 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://loinc.org |
| 49 | 504 | Observation | `Observation.code.coding` | ANC.B8.DE19 | Diastolic blood pressure | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 50 | 516 | Observation | `Observation.code.coding` | 11881-0 | Uterus Fundal height Tape measure | http://loinc.org |
| 51 | 517 | Observation | `Observation.code.coding` | ANC.B8.DE105 | Symphysis-fundal height | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 52 | 529 | Observation | `Observation.code.coding` | 72155-5 | Position in womb Fetus [RHEA] | http://loinc.org |
| 53 | 530 | Observation | `Observation.code.coding` | ANC.B8.DE111 | Fetal presentation | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 54 | 541 | Observation | `Observation.code.coding` | 55283-6 | Fetal Heart rate | http://loinc.org |
| 55 | 542 | Observation | `Observation.code.coding` | ANC.B8.DE107 | Fetal heart rate | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 56 | 554 | Immunization | `Immunization.vaccineCode` | VG139 | Td | http://sys-ids.kemkes.go.id/kfa |
| 57 | 567 | Immunization | `Immunization.vaccineCode` | VG139 | Td | http://sys-ids.kemkes.go.id/kfa |
| 58 | 580 | Procedure | `Procedure.code.coding` | 1230101008 | Counseling for pregnancy | http://snomed.info/sct |
| 59 | 591 | Procedure | `Procedure.code.coding` | 243787009 | Antenatal screening | http://snomed.info/sct |
| 60 | 603 | MedicationRequest | `MedicationRequest.contained.code.coding` | 92000653 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula | http://sys-ids.kemkes.go.id/kfa |
| 61 | 623 | MedicationDispense | `MedicationDispense.contained.code.coding` | 93015491 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | http://sys-ids.kemkes.go.id/kfa |
| 62 | 651 | ServiceRequest | `ServiceRequest.code` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 63 | 662 | Specimen | `Specimen.type` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 64 | 671 | Observation | `Observation.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 65 | 672 | Observation | `Observation.code.coding` | ANC.B9.DE175 | Blood hemoglobin test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 66 | 684 | DiagnosticReport | `DiagnosticReport.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 67 | 696 | Observation | `Observation.code.coding` | 883-9 | ABO group [Type] in Blood | http://loinc.org |
| 68 | 697 | Observation | `Observation.code.coding` | ANC.B9.DE24 | Blood type | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 69 | 707 | Procedure | `Procedure.code.coding` | 55052008 | Diagnostic ultrasound of gravid uterus | http://snomed.info/sct |
| 70 | 718 | Observation | `Observation.code.coding` | 278977008 | Human immunodeficiency virus status | http://snomed.info/sct |
| 71 | 719 | Observation | `Observation.valueCodeableConcept.coding` | 165816005 | Human immunodeficiency virus detected | http://snomed.info/sct |
| 72 | 729 | Observation | `Observation.code.coding` | 76272004 | Syphilis | http://snomed.info/sct |
| 73 | 740 | Observation | `Observation.code.coding` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 74 | 741 | Observation | `Observation.code.coding` | ANC.B9.DE60 | Hepatitis B test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 75 | 752 | Observation | `Observation.code.coding` | SP000016 | Tatalaksana Masalah Kesehatan | http://terminology.kemkes.go.id/sp |
| 76 | 766 | ServiceRequest | `ServiceRequest.code` | 20454-5 | Protein [Presence] in Urine by Test strip | http://loinc.org |
| 77 | 777 | Specimen | `Specimen.type` | 122575003 | Urine specimen | http://snomed.info/sct |
| 78 | 786 | Observation | `Observation.code.coding` | 20454-5 | Protein [Presence] in Urine by Test strip | http://loinc.org |
| 79 | 787 | Observation | `Observation.code.coding` | ANC.B9.DE114 | Urine test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 80 | 790 | Observation | `Observation.valueCodeableConcept.coding` | LA11841-6 | 1+ | http://loinc.org |
| 81 | 791 | Observation | `Observation.valueCodeableConcept.coding` | LA11842-4 | 2+ | http://loinc.org |
| 82 | 792 | Observation | `Observation.valueCodeableConcept.coding` | LA11843-2 | 3+ | http://loinc.org |
| 83 | 793 | Observation | `Observation.valueCodeableConcept.coding` | LA11844-0 | 4+ | http://loinc.org |
| 84 | 794 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 85 | 803 | DiagnosticReport | `DiagnosticReport.code` | 20454-5 | Protein [Presence] in Urine by Test strip | http://loinc.org |
| 86 | 817 | ServiceRequest | `ServiceRequest.code` | 25428-4 | Glucose [Presence] in Urine by Test strip | http://loinc.org |
| 87 | 828 | Specimen | `Specimen.type` | 122575003 | Urine specimen | http://snomed.info/sct |
| 88 | 837 | Observation | `Observation.code.coding` | 25428-4 | Glucose [Presence] in Urine by Test strip | http://loinc.org |
| 89 | 838 | Observation | `Observation.code.coding` | ANC.B9.DE114 | Urine test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 90 | 841 | Observation | `Observation.valueCodeableConcept.coding` | LA11841-6 | 1+ | http://loinc.org |
| 91 | 842 | Observation | `Observation.valueCodeableConcept.coding` | LA11842-4 | 2+ | http://loinc.org |
| 92 | 843 | Observation | `Observation.valueCodeableConcept.coding` | LA11843-2 | 3+ | http://loinc.org |
| 93 | 844 | Observation | `Observation.valueCodeableConcept.coding` | LA11844-0 | 4+ | http://loinc.org |
| 94 | 845 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 95 | 854 | DiagnosticReport | `DiagnosticReport.code` | 25428-4 | Glucose [Presence] in Urine by Test strip | http://loinc.org |
| 96 | 868 | Observation | `Observation.code.coding` | 11778-8 | Delivery date Estimated | http://loinc.org |
| 97 | 869 | Observation | `Observation.code.coding` | ANC.B6.DE22 | Expected date of delivery (EDD) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 98 | 880 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 99 | 881 | Observation | `Observation.code.coding` | ANC.B8.DE3 | Current weight | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 100 | 893 | Observation | `Observation.code.coding` | 8302-2 | Body height | http://loinc.org |
| 101 | 894 | Observation | `Observation.code.coding` | ANC.B8.DE1 | Height | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 102 | 906 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 103 | 907 | Observation | `Observation.code.coding` | ANC.B8.DE17 | Systolic blood pressure | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 104 | 919 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://loinc.org |
| 105 | 920 | Observation | `Observation.code.coding` | ANC.B8.DE19 | Diastolic blood pressure | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 106 | 932 | Observation | `Observation.code.coding` | 284473002 | Mid upper arm circumference | http://snomed.info/sct |
| 107 | 933 | Observation | `Observation.code.coding` | ANC.SS.DE3 | Lingkar Lengan Atas (LILA) | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 108 | 945 | Observation | `Observation.code.coding` | 289625003 | Finding of fundal height of uterus | http://snomed.info/sct |
| 109 | 957 | Observation | `Observation.code.coding` | 72155-5 | Position in womb Fetus [RHEA] | http://loinc.org |
| 110 | 958 | Observation | `Observation.code.coding` | ANC.B8.DE111 | Fetal presentation | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 111 | 970 | Observation | `Observation.code.coding` | 55283-6 | Fetal Heart rate | http://loinc.org |
| 112 | 971 | Observation | `Observation.code.coding` | ANC.B8.DE107 | Fetal heart rate | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 113 | 983 | Observation | `Observation.code.coding` | SP000676 | Pemberian TTD atau suplemen | http://terminology.kemkes.go.id/sp |
| 114 | 995 | Observation | `Observation.code.coding` | SP000001 | Skrining Imunisasi Tetanus Toksoid | http://terminology.kemkes.go.id/sp |
| 115 | 1007 | Procedure | `Procedure.code.coding` | 385892002 | Mental health screening | http://snomed.info/sct |
| 116 | 1019 | Observation | `Observation.code.coding` | SP000016 | Tatalaksana Masalah Kesehatan | http://terminology.kemkes.go.id/sp |
| 117 | 1031 | Procedure | `Procedure.code.coding` | 1230101008 | Counseling for pregnancy | http://snomed.info/sct |
| 118 | 1043 | Observation | `Observation.code.coding` | 15220000 | Laboratory test | http://snomed.info/sct |
| 119 | 1044 | Observation | `Observation.component.code.coding` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 120 | 1045 | Observation | `Observation.component.code.coding` | ANC.B9.DE60 | Hepatitis B test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 121 | 1048 | Observation | `Observation.component.code.coding` | 20454-5 | Protein [Presence] in Urine by Test strip | http://loinc.org |
| 122 | 1049 | Observation | `Observation.component.code.coding` | ANC.B9.DE114 | Urine test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 123 | 1052 | Observation | `Observation.component.code.coding` | SP001100 | Triple Eliminasi | http://terminology.kemkes.go.id/sp |
| 124 | 1055 | Observation | `Observation.component.code.coding` | SP001101 | Pemeriksaan lain sesuai indikasi | http://terminology.kemkes.go.id/sp |
| 125 | 1067 | Observation | `Observation.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 126 | 1068 | Observation | `Observation.code.coding` | ANC.B9.DE175 | Blood hemoglobin test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 127 | 1080 | Observation | `Observation.code.coding` | 20454-5 | Protein [Presence] in Urine by Test strip | http://loinc.org |
| 128 | 1081 | Observation | `Observation.code.coding` | ANC.B9.DE114 | Urine test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 129 | 1093 | Observation | `Observation.code.coding` | SP001100 | Triple Eliminasi | http://terminology.kemkes.go.id/sp |
| 130 | 1105 | Observation | `Observation.code.coding` | 243787009 | Antenatal screening | http://snomed.info/sct |
| 131 | 1116 | Procedure | `Procedure.code.coding` | 88.78 | Diagnostic ultrasound of gravid uterus | http://hl7.org/fhir/sid/icd-9-cm |
| 132 | 1144 | Condition | `Condition.code.coding` | 134435003 | Routine antenatal care | http://snomed.info/sct |
| 133 | 1155 | Observation | `Observation.code.coding` | OC000010 | Indeks Massa Tubuh Sebelum Hamil | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 134 | 1156 | Observation | `Observation.code.coding` | ANC.SS.DE58 | IMT Sebelum Hamil | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 135 | 1159 | Observation | `Observation.interpretation.coding` | 248342006 | Underweight | http://snomed.info/sct |
| 136 | 1160 | Observation | `Observation.interpretation.coding` | 43664005 | Normal weight | http://snomed.info/sct |
| 137 | 1161 | Observation | `Observation.interpretation.coding` | 238131007 | Overweight | http://snomed.info/sct |
| 138 | 1162 | Observation | `Observation.interpretation.coding` | 414915002 | Obese | http://snomed.info/sct |
| 139 | 1172 | Immunization | `Immunization.vaccineCode` | VG139 | Td | http://sys-ids.kemkes.go.id/kfa |
| 140 | 1190 | Observation | `Observation.code.coding` | SP000015 | Risiko Masalah Kesehatan | http://terminology.kemkes.go.id/sp |
| 141 | 1194 | Observation | `Observation.component.code.coding` | 85828009 | Autoimmune disease | http://snomed.info/sct |
| 142 | 1197 | Observation | `Observation.component.code.coding` | 66071002 | Viral hepatitis type B | http://snomed.info/sct |
| 143 | 1200 | Observation | `Observation.component.code.coding` | 56265001 | Heart disease | http://snomed.info/sct |
| 144 | 1203 | Observation | `Observation.component.code.coding` | 76272004 | Syphilis | http://snomed.info/sct |
| 145 | 1206 | Observation | `Observation.component.code.coding` | 195967001 | Asthma | http://snomed.info/sct |
| 146 | 1209 | Observation | `Observation.component.code.coding` | 73211009 | Diabetes mellitus | http://snomed.info/sct |
| 147 | 1212 | Observation | `Observation.component.code.coding` | 38341003 | Hypertensive disorder, systemic arterial | http://snomed.info/sct |
| 148 | 1215 | Observation | `Observation.component.code.coding` | 74732009 | Mental disorder | http://snomed.info/sct |
| 149 | 1218 | Observation | `Observation.component.code.coding` | 56717001 | Tuberculosis | http://snomed.info/sct |
| 150 | 1221 | Observation | `Observation.component.code.coding` | 74964007 | Other | http://snomed.info/sct |
| 151 | 1232 | Observation | `Observation.code.coding` | SP000424 | Riwayat Perilaku Berisiko Sebelum Hamil | http://terminology.kemkes.go.id/sp |
| 152 | 1233 | Observation | `Observation.component.code.coding` | 43994002 | Lack of physical activity | http://snomed.info/sct |
| 153 | 1236 | Observation | `Observation.component.code.coding` | SP000426 | Penggunaan Kosmetik Yang Mengandung Zat Berbahaya | http://terminology.kemkes.go.id/sp |
| 154 | 1239 | Observation | `Observation.component.code.coding` | SP000425 | Konsumsi Obat Teratogenik | http://terminology.kemkes.go.id/sp |
| 155 | 1242 | Observation | `Observation.component.code.coding` | SP000427 | Konsumsi Alkohol atau Obat-Obatan Terlarang | http://terminology.kemkes.go.id/sp |
| 156 | 1245 | Observation | `Observation.component.code.coding` | 77176002 | Smoker | http://snomed.info/sct |
| 157 | 1248 | Observation | `Observation.component.code.coding` | 308658001 | Abnormal eating pattern | http://snomed.info/sct |
| 158 | 1251 | Observation | `Observation.component.code.coding` | 74964007 | Other | http://snomed.info/sct |
| 159 | 1262 | Observation | `Observation.code.coding` | 281666001 | Family history of disorder | http://snomed.info/sct |
| 160 | 1263 | Observation | `Observation.component.code.coding` | 160469004 | Family history: Allergy | http://snomed.info/sct |
| 161 | 1266 | Observation | `Observation.component.code.coding` | 300933005 | Family history: Autoimmune disease | http://snomed.info/sct |
| 162 | 1269 | Observation | `Observation.component.code.coding` | 275130003 | Family history: Hepatitis | http://snomed.info/sct |
| 163 | 1272 | Observation | `Observation.component.code.coding` | 429959009 | Family history of heart failure | http://snomed.info/sct |
| 164 | 1275 | Observation | `Observation.component.code.coding` | 160281003 | Family history: Syphilis | http://snomed.info/sct |
| 165 | 1278 | Observation | `Observation.component.code.coding` | 160377001 | Family history: Asthma | http://snomed.info/sct |
| 166 | 1281 | Observation | `Observation.component.code.coding` | 160303001 | Family history of diabetes mellitus | http://snomed.info/sct |
| 167 | 1284 | Observation | `Observation.component.code.coding` | 160357008 | Family history: Hypertension | http://snomed.info/sct |
| 168 | 1287 | Observation | `Observation.component.code.coding` | 160324006 | Family history of mental disorder | http://snomed.info/sct |
| 169 | 1290 | Observation | `Observation.component.code.coding` | 160280002 | Family history: Tuberculosis | http://snomed.info/sct |
| 170 | 1293 | Observation | `Observation.component.code.coding` | 74964007 | Other | http://snomed.info/sct |
| 171 | 1304 | Observation | `Observation.code.coding` | 248910006 | Uterine cervix finding | http://snomed.info/sct |
| 172 | 1305 | Observation | `Observation.valueCodeableConcept.coding` | 17621005 | Normal | http://snomed.info/sct |
| 173 | 1306 | Observation | `Observation.valueCodeableConcept.coding` | 263654008 | Abnormal | http://snomed.info/sct |
| 174 | 1316 | Observation | `Observation.code.coding` | 249300001 | Urethral finding | http://snomed.info/sct |
| 175 | 1317 | Observation | `Observation.valueCodeableConcept.coding` | 17621005 | Normal | http://snomed.info/sct |
| 176 | 1318 | Observation | `Observation.valueCodeableConcept.coding` | 263654008 | Abnormal | http://snomed.info/sct |
| 177 | 1328 | Observation | `Observation.code.coding` | 451024007 | Inspection of vagina using vaginal speculum | http://snomed.info/sct |
| 178 | 1329 | Observation | `Observation.valueCodeableConcept.coding` | 17621005 | Normal | http://snomed.info/sct |
| 179 | 1330 | Observation | `Observation.valueCodeableConcept.coding` | 263654008 | Abnormal | http://snomed.info/sct |
| 180 | 1340 | Observation | `Observation.code.coding` | 364223009 | Vulva observable | http://snomed.info/sct |
| 181 | 1341 | Observation | `Observation.valueCodeableConcept.coding` | 17621005 | Normal | http://snomed.info/sct |
| 182 | 1342 | Observation | `Observation.valueCodeableConcept.coding` | 263654008 | Abnormal | http://snomed.info/sct |
| 183 | 1352 | Observation | `Observation.code.coding` | 271939006 | Vaginal discharge | http://snomed.info/sct |
| 184 | 1353 | Observation | `Observation.method.coding` | 451024007 | Inspection of vagina using vaginal speculum | http://snomed.info/sct |
| 185 | 1354 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 186 | 1355 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 187 | 1365 | Observation | `Observation.code.coding` | 289552002 | White vaginal discharge | http://snomed.info/sct |
| 188 | 1366 | Observation | `Observation.method.coding` | 451024007 | Inspection of vagina using vaginal speculum | http://snomed.info/sct |
| 189 | 1367 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 190 | 1368 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 191 | 1379 | Observation | `Observation.code.coding` | 93857-1 | Date and time of obstetric delivery | https://loinc.org |
| 192 | 1391 | Observation | `Observation.code.coding` | 8339-4 | Birth weight Measured | https://loinc.org |
| 193 | 1406 | Observation | `Observation.code.coding` | 57071-3 | Obstetric delivery method | http://loinc.org |
| 194 | 1419 | Observation | `Observation.code.coding` | OC000013 | Penolong Persalinan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 195 | 1432 | Observation | `Observation.code.coding` | 450891000124109 | Past pregnancy history of complication of pregnancy, childbirth and/or puerperium | http://snomed.info/sct |
| 196 | 1448 | Observation | `Observation.code.coding` | 106167005 | Consciousness related finding | http://snomed.info/sct |
| 197 | 1460 | Observation | `Observation.code.coding` | 246875002 | Conjunctival finding | http://snomed.info/sct |
| 198 | 1473 | Observation | `Observation.code.coding` | 366039006 | Finding of color of sclera | http://snomed.info/sct |
| 199 | 1486 | Observation | `Observation.code.coding` | 106076001 | Skin finding | http://snomed.info/sct |
| 200 | 1499 | Observation | `Observation.code.coding` | 298378000 | Finding of neck region | http://snomed.info/sct |
| 201 | 1512 | Observation | `Observation.code.coding` | 116337000 | Finding of internal part of mouth | http://snomed.info/sct |
| 202 | 1525 | Observation | `Observation.code.coding` | 297268004 | Ear, nose and throat finding | http://snomed.info/sct |
| 203 | 1538 | Observation | `Observation.code.coding` | 10200-4 | Physical findings of Heart Narrative | http://loinc.org |
| 204 | 1551 | Observation | `Observation.code.coding` | 301230006 | Lung finding | http://snomed.info/sct |
| 205 | 1564 | Observation | `Observation.code.coding` | 118434000 | Stomach finding | http://snomed.info/sct |
| 206 | 1577 | Observation | `Observation.code.coding` | 116312005 | Finding of lower limb | http://snomed.info/sct |
| 207 | 1590 | Observation | `Observation.code.coding` | 8665-2 | Last menstrual period start date | http://loinc.org |
| 208 | 1591 | Observation | `Observation.code.coding` | ANC.B6.DE14 | Last menstrual period (LMP) date | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 209 | 1602 | Observation | `Observation.code.coding` | 248965005 | Finding of regularity of menstrual cycle | http://snomed.info/sct |
| 210 | 1615 | Observation | `Observation.code.coding` | 18185-9 | Gestational age | http://loinc.org |
| 211 | 1616 | Observation | `Observation.code.coding` | ANC.B6.DE17 | Gestational age | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 212 | 1628 | Observation | `Observation.code.coding` | 11778-8 | Delivery date Estimated | http://loinc.org |
| 213 | 1629 | Observation | `Observation.code.coding` | ANC.B6.DE22 | Expected date of delivery (EDD) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 214 | 1640 | Observation | `Observation.code.coding` | 11888-5 | Gestational age US composite estimate | http://loinc.org |
| 215 | 1641 | Observation | `Observation.code.coding` | ANC.B6.DE20 | Ulrasound | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 216 | 1653 | Observation | `Observation.code.coding` | 11781-2 | Delivery date US composite estimate | http://loinc.org |
| 217 | 1654 | Observation | `Observation.code.coding` | ANC.SS.DE40 | Hari Perkiraan Lahir (HPL) USG | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 218 | 1665 | Observation | `Observation.code.coding` | SP000672 | Jumlah kantong kehamilan | http://terminology.kemkes.go.id/sp |
| 219 | 1666 | Observation | `Observation.valueCodeableConcept.coding` | 237244005 | Single pregnancy | http://snomed.info/sct |
| 220 | 1667 | Observation | `Observation.valueCodeableConcept.coding` | 65147003 | Twin pregnancy | http://snomed.info/sct |
| 221 | 1677 | Observation | `Observation.code.coding` | 11850-5 | Gestational sac Mean diameter US | http://loinc.org |
| 222 | 1678 | Observation | `Observation.code.coding` | ANC.SS.DE36 | Gestational sac (GS) USG | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 223 | 1681 | Observation | `Observation.component.code.coding` | SP001102 | Diameter GS sesuai dengan usia kehamilan (minggu) | http://terminology.kemkes.go.id/sp |
| 224 | 1684 | Observation | `Observation.component.code.coding` | SP001103 | Diameter GS sesuai dengan usia kehamilan (hari) | http://terminology.kemkes.go.id/sp |
| 225 | 1696 | Observation | `Observation.code.coding` | 246435002 | Number of fetuses | http://snomed.info/sct |
| 226 | 1697 | Observation | `Observation.valueCodeableConcept.coding` | 237244005 | Single pregnancy | http://snomed.info/sct |
| 227 | 1698 | Observation | `Observation.valueCodeableConcept.coding` | 65147003 | Twin pregnancy | http://snomed.info/sct |
| 228 | 1708 | Observation | `Observation.code.coding` | 11957-8 | Fetal Crown Rump length US | http://loinc.org |
| 229 | 1709 | Observation | `Observation.code.coding` | ANC.SS.DE37 | Fetal Crown Rump Length (CRL) USG | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 230 | 1712 | Observation | `Observation.component.code.coding` | SP001104 | CRL sesuai dengan usia kehamilan (minggu) | http://terminology.kemkes.go.id/sp |
| 231 | 1715 | Observation | `Observation.component.code.coding` | SP001105 | CRL sesuai dengan usia kehamilan (hari) | http://terminology.kemkes.go.id/sp |
| 232 | 1727 | Observation | `Observation.code.coding` | 271692001 | Presentation of fetus | http://snomed.info/sct |
| 233 | 1728 | Observation | `Observation.code.coding` | ANC.SS.DE41 | Letak Janin USG | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 234 | 1729 | Observation | `Observation.valueCodeableConcept.coding` | 398236008 | Intrauterine | http://snomed.info/sct |
| 235 | 1730 | Observation | `Observation.valueCodeableConcept.coding` | 298109001 | Ectopic | http://snomed.info/sct |
| 236 | 1731 | Observation | `Observation.valueCodeableConcept.coding` | 871479001 | Uncertain presentation of fetus | http://snomed.info/sct |
| 237 | 1741 | Observation | `Observation.code.coding` | 249042007 | Fetal heart finding | http://loinc.org |
| 238 | 1742 | Observation | `Observation.valueCodeableConcept.coding` | 52101004 | Present | http://snomed.info/sct |
| 239 | 1743 | Observation | `Observation.valueCodeableConcept.coding` | 2667000 | Absent | http://snomed.info/sct |
| 240 | 1753 | Observation | `Observation.code.coding` | 28241000119109 | Ultrasonography of fetus abnormal | http://snomed.info/sct |
| 241 | 1767 | Observation | `Observation.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 242 | 1768 | Observation | `Observation.code.coding` | ANC.B9.DE175 | Blood hemoglobin test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 243 | 1780 | Observation | `Observation.code.coding` | 883-9 | ABO group [Type] in Blood | http://loinc.org |
| 244 | 1781 | Observation | `Observation.code.coding` | ANC.B9.DE24 | Blood type | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 245 | 1792 | Observation | `Observation.code.coding` | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | http://loinc.org |
| 246 | 1793 | Observation | `Observation.code.coding` | ANC.B9.DE159 | Blood glucose test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 247 | 1805 | Observation | `Observation.code.coding` | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 248 | 1806 | Observation | `Observation.code.coding` | ANC.B9.DE32 | HIV test | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 249 | 1807 | Observation | `Observation.valueCodeableConcept.coding` | 11214006 | Reactive | http://snomed.info/sct |
| 250 | 1808 | Observation | `Observation.valueCodeableConcept.coding` | 131194007 | Non-Reactive | http://snomed.info/sct |
| 251 | 1818 | Observation | `Observation.code.coding` | 20508-8 | Reagin Ab [Units/volume] in Serum or Plasma by RPR | http://loinc.org |
| 252 | 1819 | Observation | `Observation.code.coding` | ANC.B9.DE96 | Syphilis test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 253 | 1820 | Observation | `Observation.valueCodeableConcept.coding` | 11214006 | Reactive | http://snomed.info/sct |
| 254 | 1821 | Observation | `Observation.valueCodeableConcept.coding` | 131194007 | Non-Reactive | http://snomed.info/sct |
| 255 | 1831 | Observation | `Observation.code.coding` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 256 | 1832 | Observation | `Observation.code.coding` | ANC.B9.DE60 | Hepatitis B test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 257 | 1833 | Observation | `Observation.valueCodeableConcept.coding` | 11214006 | Reactive | http://snomed.info/sct |
| 258 | 1834 | Observation | `Observation.valueCodeableConcept.coding` | 131194007 | Non-Reactive | http://snomed.info/sct |
| 259 | 1843 | Procedure | `Procedure.code.coding` | 385892002 | Mental health screening | http://snomed.info/sct |
| 260 | 1855 | Observation | `Observation.code.coding` | SP000730 | Tindak lanjut hasil skrining kesehatan jiwa | http://terminology.kemkes.go.id/sp |
| 261 | 1857 | Observation | `Observation.component.code.coding` | 409073007 | Education | http://snomed.info/sct |
| 262 | 1860 | Observation | `Observation.component.code.coding` | 409063005 | Counseling | http://snomed.info/sct |
| 263 | 1863 | Observation | `Observation.component.code.coding` | 3457005 | Patient referral | http://snomed.info/sct |
| 264 | 1876 | Observation | `Observation.code.coding` | C54033 | Conclusion | http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl |
| 265 | 1886 | Observation | `Observation.code.coding` | C25197 | Recommendation | http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl |
| 266 | 1897 | Observation | `Observation.code.coding` | SP000779 | Multipara dengan kehamilan oleh pasangan baru | http://terminology.kemkes.go.id/sp |
| 267 | 1909 | Observation | `Observation.code.coding` | 813541000000100 | Pregnancy resulting from assisted conception | http://snomed.info/sct |
| 268 | 1921 | Observation | `Observation.code.coding` | SP000780 | Umur ≥ 35 Tahun | http://terminology.kemkes.go.id/sp |
| 269 | 1933 | Observation | `Observation.code.coding` | 102877006 | Nulliparous | http://snomed.info/sct |
| 270 | 1945 | Observation | `Observation.code.coding` | SP000781 | Multipara yang Jarak Kehamilan Sebelumnya > 10 Tahun | http://terminology.kemkes.go.id/sp |
| 271 | 1957 | Observation | `Observation.code.coding` | 700190003 | Family history of pre-eclampsia | http://snomed.info/sct |
| 272 | 1969 | Observation | `Observation.code.coding` | 162864005 | Body mass index 30+ - obesity | http://snomed.info/sct |
| 273 | 1981 | Observation | `Observation.code.coding` | SP000782 | Multipara Dengan Riwayat Preeklampsia Sebelumnya | http://terminology.kemkes.go.id/sp |
| 274 | 1993 | Observation | `Observation.code.coding` | 16356006 | Multiple pregnancy | http://snomed.info/sct |
| 275 | 2005 | Observation | `Observation.code.coding` | 11687002 | Gestational diabetes mellitus | http://snomed.info/sct |
| 276 | 2017 | Observation | `Observation.code.coding` | 8762007 | Chronic hypertension in obstetric context | http://snomed.info/sct |
| 277 | 2029 | Observation | `Observation.code.coding` | 90708001 | Kidney disease | http://snomed.info/sct |
| 278 | 2041 | Observation | `Observation.code.coding` | 85828009 | Autoimmune disease | http://snomed.info/sct |
| 279 | 2053 | Observation | `Observation.code.coding` | 26843008 | Antiphospholipid syndrome | http://snomed.info/sct |
| 280 | 2065 | Observation | `Observation.code.coding` | SP000783 | Mean Arterial Presure > 90 mmHg | http://terminology.kemkes.go.id/sp |
| 281 | 2077 | Observation | `Observation.code.coding` | 29738008 | Proteinuria | http://snomed.info/sct |
| 282 | 2089 | Observation | `Observation.code.coding` | SP000482 | Skrinning Preeklampsia | http://terminology.kemkes.go.id/sp |
| 283 | 2090 | Observation | `Observation.valueCodeableConcept.coding` | SP000784 | Berisiko Preeklampsia | http://terminology.kemkes.go.id/sp |
| 284 | 2091 | Observation | `Observation.valueCodeableConcept.coding` | SP000785 | Tidak Berisiko Preeklampsia | http://terminology.kemkes.go.id/sp |
| 285 | 2101 | Observation | `Observation.code.coding` | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 286 | 2102 | Observation | `Observation.code.coding` | ANC.B9.DE159 | Blood glucose test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 287 | 2115 | Observation | `Observation.code.coding` | 1521-4 | Glucose [Mass/volume] in Serum or Plasma --2 hours post meal | http://loinc.org |
| 288 | 2116 | Observation | `Observation.code.coding` | ANC.B9.DE159 | Blood glucose test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 289 | 2129 | Observation | `Observation.code.coding` | 106167005 | Consciousness related finding | http://snomed.info/sct |
| 290 | 2141 | Observation | `Observation.code.coding` | 246875002 | Conjunctival finding | http://snomed.info/sct |
| 291 | 2154 | Observation | `Observation.code.coding` | 366039006 | Finding of color of sclera | http://snomed.info/sct |
| 292 | 2167 | Observation | `Observation.code.coding` | 106076001 | Skin finding | http://snomed.info/sct |
| 293 | 2180 | Observation | `Observation.code.coding` | 298378000 | Finding of neck region | http://snomed.info/sct |
| 294 | 2193 | Observation | `Observation.code.coding` | 116337000 | Finding of internal part of mouth | http://snomed.info/sct |
| 295 | 2206 | Observation | `Observation.code.coding` | 297268004 | Ear, nose and throat finding | http://snomed.info/sct |
| 296 | 2219 | Observation | `Observation.code.coding` | 10200-4 | Physical findings of Heart Narrative | http://loinc.org |
| 297 | 2232 | Observation | `Observation.code.coding` | 301230006 | Lung finding | http://snomed.info/sct |
| 298 | 2245 | Observation | `Observation.code.coding` | 118434000 | Stomach finding | http://snomed.info/sct |
| 299 | 2258 | Observation | `Observation.code.coding` | 116312005 | Finding of lower limb | http://snomed.info/sct |
| 300 | 2270 | Procedure | `Procedure.code.coding` | 88.78 | Diagnostic ultrasound of gravid uterus | http://hl7.org/fhir/sid/icd-9-cm |
| 301 | 2283 | Observation | `Observation.code.coding` | 11888-5 | Gestational age US composite estimate | http://loinc.org |
| 302 | 2284 | Observation | `Observation.code.coding` | ANC.B6.DE20 | Ulrasound | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 303 | 2296 | Observation | `Observation.code.coding` | 18185-9 | Gestational age | http://loinc.org |
| 304 | 2297 | Observation | `Observation.code.coding` | ANC.B6.DE17 | Gestational age | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 305 | 2310 | Observation | `Observation.code.coding` | 11888-5 | Gestational age US composite estimate | http://loinc.org |
| 306 | 2311 | Observation | `Observation.code.coding` | ANC.B6.DE20 | Ulrasound | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 307 | 2323 | Observation | `Observation.code.coding` | SP001099 | Ada selisih 3 minggu atau lebih antara UK USG TM 1/HPHT dengan UK USG TM3 | http://terminology.kemkes.go.id/sp |
| 308 | 2335 | Observation | `Observation.code.coding` | 246435002 | Number of fetuses | http://snomed.info/sct |
| 309 | 2336 | Observation | `Observation.valueCodeableConcept.coding` | 237244005 | Single pregnancy | http://snomed.info/sct |
| 310 | 2337 | Observation | `Observation.valueCodeableConcept.coding` | 65147003 | Twin pregnancy | http://snomed.info/sct |
| 311 | 2347 | Observation | `Observation.code.coding` | 271692001 | Presentation of fetus | http://snomed.info/sct |
| 312 | 2348 | Observation | `Observation.code.coding` | ANC.SS.DE41 | Letak Janin USG | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 313 | 2349 | Observation | `Observation.valueCodeableConcept.coding` | 398236008 | Intrauterine | http://snomed.info/sct |
| 314 | 2350 | Observation | `Observation.valueCodeableConcept.coding` | 298109001 | Ectopic | http://snomed.info/sct |
| 315 | 2351 | Observation | `Observation.valueCodeableConcept.coding` | 871479001 | Uncertain presentation of fetus | http://snomed.info/sct |
| 316 | 2361 | Observation | `Observation.code.coding` | 72155-5 | Position in womb Fetus [RHEA] | http://loinc.org |
| 317 | 2362 | Observation | `Observation.code.coding` | ANC.B8.DE111 | Fetal presentation | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 318 | 2363 | Observation | `Observation.valueCodeableConcept.coding` | 1209182005 | Cephalic fetal presentation | http://snomed.info/sct |
| 319 | 2364 | Observation | `Observation.valueCodeableConcept.coding` | 6096002 | Breech presentation | http://snomed.info/sct |
| 320 | 2365 | Observation | `Observation.valueCodeableConcept.coding` | 73161006 | Transverse lie | http://snomed.info/sct |
| 321 | 2375 | Observation | `Observation.code.coding` | 404964004 | Antepartum fetal status | http://snomed.info/sct |
| 322 | 2376 | Observation | `Observation.valueCodeableConcept.coding` | 830138009 | Viable fetus | http://snomed.info/sct |
| 323 | 2377 | Observation | `Observation.valueCodeableConcept.coding` | 445548006 | Dead fetus in utero | http://snomed.info/sct |
| 324 | 2387 | Observation | `Observation.code.coding` | 55283-6 | Fetal Heart rate | http://loinc.org |
| 325 | 2388 | Observation | `Observation.code.coding` | ANC.B8.DE107 | Fetal heart rate | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 326 | 2391 | Observation | `Observation.interpretation` | 289441006 | Normal fetal heart rate | http://snomed.info/sct |
| 327 | 2392 | Observation | `Observation.interpretation` | 312668007 | Abnormal fetal heart rate | http://snomed.info/sct |
| 328 | 2402 | Observation | `Observation.code.coding` | 11994-1 | Placenta position US | http://loinc.org |
| 329 | 2403 | Observation | `Observation.valueCodeableConcept.coding` | 658101000005106 | Position of placenta in fundus uteri | http://snomed.info/sct |
| 330 | 2404 | Observation | `Observation.valueCodeableConcept.coding` | 23952005 | Body of uterus structure | http://snomed.info/sct |
| 331 | 2405 | Observation | `Observation.valueCodeableConcept.coding` | 445122007 | Low-lying placenta | http://snomed.info/sct |
| 332 | 2406 | Observation | `Observation.valueCodeableConcept.coding` | 36813001 | Placenta previa | http://snomed.info/sct |
| 333 | 2416 | Observation | `Observation.code.coding` | 3156-7 | Volume of Amniotic fluid | http://loinc.org |
| 334 | 2419 | Observation | `Observation.interpretation` | 278092006 | Amniotic fluid volume within reference range | http://snomed.info/sct |
| 335 | 2420 | Observation | `Observation.interpretation` | 1228877003 | Amniotic fluid volume below reference range | http://snomed.info/sct |
| 336 | 2421 | Observation | `Observation.interpretation` | 289293006 | Amniotic fluid volume above reference range | http://snomed.info/sct |
| 337 | 2431 | Observation | `Observation.code.coding` | 11820-8 | Fetal Head Diameter.biparietal US | http://loinc.org |
| 338 | 2432 | Observation | `Observation.code.coding` | ANC.SS.DE59 | Biparietal Diameter (BPD) USG | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 339 | 2447 | Observation | `Observation.code.coding` | 11984-2 | Fetal Head Circumference US | http://loinc.org |
| 340 | 2448 | Observation | `Observation.code.coding` | ANC.SS.DE42 | Head Circumference (HC) USG | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 341 | 2463 | Observation | `Observation.code.coding` | 11979-2 | Fetal Abdomen Circumference US | http://loinc.org |
| 342 | 2464 | Observation | `Observation.code.coding` | ANC.SS.DE43 | Abdominal Circumference (AC) USG | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 343 | 2479 | Observation | `Observation.code.coding` | 11963-6 | Fetal Femur diaphysis [Length] US | http://loinc.org |
| 344 | 2480 | Observation | `Observation.code.coding` | ANC.SS.DE44 | Femur Length (FL) USG | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 345 | 2495 | Observation | `Observation.code.coding` | 11727-5 | Fetal Body weight estimated by US | http://loinc.org |
| 346 | 2496 | Observation | `Observation.code.coding` | ANC.SS.DE45 | Berat janin USG | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 347 | 2511 | Observation | `Observation.code.coding` | 28241000119109 | Ultrasonography of fetus abnormal | http://snomed.info/sct |
| 348 | 2524 | Observation | `Observation.code.coding` | 11525-3 | US for pregnancy | http://loinc.org |
| 349 | 2535 | Observation | `Observation.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 350 | 2536 | Observation | `Observation.code.coding` | ANC.B9.DE175 | Blood hemoglobin test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 351 | 2549 | Observation | `Observation.code.coding` | 5804-0 | Protein [Mass/volume] in Urine by Test strip | http://loinc.org |
| 352 | 2550 | Observation | `Observation.code.coding` | ANC.B9.DE114 | Urine test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 353 | 2563 | Observation | `Observation.code.coding` | 20454-5 | Protein [Presence] in Urine by Test strip | http://loinc.org |
| 354 | 2564 | Observation | `Observation.code.coding` | ANC.B9.DE114 | Urine test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 355 | 2565 | Observation | `Observation.valueCodeableConcept.coding` | LA11841-6 | 1+ | http://loinc.org |
| 356 | 2566 | Observation | `Observation.valueCodeableConcept.coding` | LA11842-4 | 2+ | http://loinc.org |
| 357 | 2567 | Observation | `Observation.valueCodeableConcept.coding` | LA11843-2 | 3+ | http://loinc.org |
| 358 | 2568 | Observation | `Observation.valueCodeableConcept.coding` | LA11844-0 | 4+ | http://loinc.org |
| 359 | 2569 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 360 | 2579 | Procedure | `Procedure.code.coding` | 385892002 | Mental health screening | http://snomed.info/sct |
| 361 | 2591 | Observation | `Observation.code.coding` | SP000730 | Tindak lanjut hasil skrining kesehatan jiwa | http://terminology.kemkes.go.id/sp |
| 362 | 2593 | Observation | `Observation.component.code.coding` | 409073007 | Education | http://snomed.info/sct |
| 363 | 2596 | Observation | `Observation.component.code.coding` | 409063005 | Counseling | http://snomed.info/sct |
| 364 | 2599 | Observation | `Observation.component.code.coding` | 3457005 | Patient referral | http://snomed.info/sct |
| 365 | 2613 | CarePlan | `CarePlan.activity.detail.code.coding` | 1240781000168102 | Nutrition service | http://snomed.info/sct |
| 366 | 2614 | CarePlan | `CarePlan.activity.detail.code.coding` | 714088003 | Midwifery service | http://snomed.info/sct |
| 367 | 2615 | CarePlan | `CarePlan.activity.detail.code.coding` | 310066004 | Pediatric service | http://snomed.info/sct |
| 368 | 2616 | CarePlan | `CarePlan.activity.detail.code.coding` | 792848000 | Internal medicine service | http://snomed.info/sct |
| 369 | 2617 | CarePlan | `CarePlan.activity.detail.code.coding` | 788005004 | Neurology service | http://snomed.info/sct |
| 370 | 2618 | CarePlan | `CarePlan.activity.detail.code.coding` | 310149003 | Ear, nose and throat service | http://snomed.info/sct |
| 371 | 2619 | CarePlan | `CarePlan.activity.detail.code.coding` | 310116007 | Psychiatry service | http://snomed.info/sct |
| 372 | 2620 | CarePlan | `CarePlan.activity.detail.code.coding` | 224891009 | Healthcare services | http://snomed.info/sct |
| 373 | 2641 | CarePlan | `CarePlan.activity.detail.code.coding` | 48782003 | Delivery normal | http://snomed.info/sct |
| 374 | 2642 | CarePlan | `CarePlan.activity.detail.code.coding` | 289259007 | Vaginal delivery | http://snomed.info/sct |
| 375 | 2643 | CarePlan | `CarePlan.activity.detail.code.coding` | 200144004 | Deliveries by cesarean | http://snomed.info/sct |
| 376 | 2655 | CarePlan | `CarePlan.activity.detail.code.coding` | LA6527-1 | Intrauterine device | http://loinc.org |
| 377 | 2656 | CarePlan | `CarePlan.activity.detail.code.coding` | LA6524-8 | Oral contraceptive pill | http://loinc.org |
| 378 | 2657 | CarePlan | `CarePlan.activity.detail.code.coding` | LA6525-5 | Injectable/implantable hormone | http://loinc.org |
| 379 | 2658 | CarePlan | `CarePlan.activity.detail.code.coding` | 77543007 | Ligation of fallopian tube | http://snomed.info/sct |
| 380 | 2659 | CarePlan | `CarePlan.activity.detail.code.coding` | 237122005 | Lactational amenorrhea | http://snomed.info/sct |
| 381 | 2660 | CarePlan | `CarePlan.activity.detail.code.coding` | SP000097 | Implan | http://terminology.kemkes.go.id/sp |
| 382 | 2661 | CarePlan | `CarePlan.activity.detail.code.coding` | 408822009 | Contraception status not decided | http://snomed.info/sct |
| 383 | 2664 | Observation | `Observation.code.coding` | 306225008 | Referral to counseling service | http://snomed.info/sct |
| 384 | 2676 | Observation | `Observation.code.coding` | 310585007 | Delivery place planned | http://snomed.info/sct |
| 385 | 2677 | Observation | `Observation.valueCodeableConcept.coding` | SP000674 | Fasilitas Kesehatan Tingkat Pertama (FKTP) | http://terminology.kemkes.go.id/sp |
| 386 | 2678 | Observation | `Observation.valueCodeableConcept.coding` | SP000675 | Fasilitas Kesehatan Rujukan Tingkat Lanjutan (FKRTL) | http://terminology.kemkes.go.id/sp |
| 387 | 2688 | Observation | `Observation.code.coding` | 89241-4 | Obstetrics Note | http://loinc.org |
| 388 | 2699 | ServiceRequest | `ServiceRequest.code` | 185389009 | Follow-up visit | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 173 |
| http://loinc.org | 97 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 57 |
| http://terminology.kemkes.go.id/sp | 39 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC | 6 |
| http://sys-ids.kemkes.go.id/kfa | 5 |
| http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes | 3 |
| http://hl7.org/fhir/sid/icd-9-cm | 2 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 2 |
| https://loinc.org | 2 |
| http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl | 2 |
| **Total** | **388** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 20 | – | Faskes yang Melayani ANC | Organization | `Organization.name` |
| 21 | – | Nama Kabupaten | Organization | `Organization.address.city` |
| 28 | – | Provinsi | Organization | `Organization.address.extension.extension.url` |
| 421 | – | Kunjungan Ke 1 | – | `` |
| 449 | – | Tempat Periksa | Organization | `Organization.name` |
| 1126 | – | Fasilitas Kesehatan | Organization | `Organization.name` |
| 1150 | – | Tinggi Badan | Tinggi Badan Variable | `` |
| 1151 | – | Berat Badan | Berat Badan | `` |
| 1152 | – | Lingkar Lengan Atas | Lingkar Lengan Atas | `` |
| 1444 | – | Nama Dokter | – | `` |
| 1445 | – | Tanggal Periksa | – | `` |
| 1764 | – | Hasil USG | – | `` |
