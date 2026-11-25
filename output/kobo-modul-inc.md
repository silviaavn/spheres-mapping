# Output Form: Kobo Modul INC

Sumber: `mapping/phdt-data-dictionary-kobo-modul-inc.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-kobo-modul-inc.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 80 |
| Code (`jumlah code` = 1) | 248 |
| Code unik (code + CodeSystem) | 226 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 44 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–33 | Patient | – | – | _Nama Ibu_ → `Patient.name.text` (2, tanpa BQ)<br>_NIK Ibu_ → `Patient.identifier.value` (5, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (7, tanpa BQ)<br>_No HP_ → `Patient.telecom` (8, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (11, tanpa BQ)<br>_Alamat Domisili_ → `Patient.address.use` (12, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (18, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (21, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.extension.valueCode` (24, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.extension.valueCode` (27, tanpa BQ)<br>_RW_ → `Patient.address.extension.extension.valueCode` (30, tanpa BQ)<br>_RT_ → `Patient.address.extension.extension.valueCode` (33, tanpa BQ) |
| 2 | 34–41 | RelatedPerson | – | – | _Nama Pendamping_ → `RelatedPerson.name.text` (35, tanpa BQ)<br>_NIK Pendamping_ → `RelatedPerson.identifier.value` (40, tanpa BQ) |
| 3 | 91–93 | PractitionerRole | – | – | – |
| 4 | 94–97 | Practitioner | – | – | – |
| 5 | 98–104 | PractitionerRole | – | – | _Jenis Tenaga Pemeriksa_ → `PractitionerRole.active` (98, tanpa BQ) |
| 6 | 105–125 | Practitioner | – | – | _Nama Pemeriksa_ → `Practitioner.name.text` (107, tanpa BQ) |
| 7 | 126–141 | DocumentReference | SP000732 | Buku KIA | _Link File Original_ → `DocumentReference.identifier` (126, tanpa BQ) |
| 8 | 142–160 | Observation | 385438008.0 | Source of information | _Sumber Data_ → `Observation.valueCodeableConcept.coding` (145, tanpa BQ)<br>_Sumber lain_ → `Observation.valueCodeableConcept.text` (152, tanpa BQ) |
| 9 | 161–179 | EpisodeOfCare | ANC | Antenatal Care | _Episode ANC Ibu_ → `EpisodeOfCare.identifier` (161, tanpa BQ)<br>_HPHT_ → `EpisodeOfCare.statusHistory.period.start` (164, tanpa BQ)<br>_Episode PNC Ibu_ → `EpisodeOfCare.identifier` (176, tanpa BQ) |
| 10 | 180–184 | EpisodeOfCare | PNC | Postnatal Care | – |
| 11 | 185–200 | Encounter | – | – | _Jenis Kunjungan INC_ → `Encounter.class` (187, tanpa BQ)<br>_Tanggal Masuk INC_ → `Encounter.period.start` (195, tanpa BQ)<br>_Tanggal Keluar INC_ → `Encounter.period.end` (196, tanpa BQ) |
| 12 | 201–208 | Condition | 386337006.0 | Intrapartal care | _Diagnosis Masuk_ → `Condition.clinicalStatus.coding` (201, tanpa BQ) |
| 13 | 231–242 | Observation | SP000131 | Status Pindahan | _Status Pindahan_ → `Observation.valueBoolean` (234, tanpa BQ) |
| 14 | 243–254 | Observation | 30525-0 | Age | _Umur_ → `Observation.valueQuantity.value` (246, tanpa BQ) |
| 15 | 255–263 | Observation | 75910-0 | Canadian triage and acuity scale [CTAS] | _Keadaan Ibu Saat Tiba_ → `Observation.valueCodeableConcept.coding` (258, tanpa BQ) |
| 16 | 264–275 | Observation | SP000383 | Keadaan Ibu Saat Tiba | _Tekanan Darah Sistolik_ → `Observation.status` (274, tanpa BQ) |
| 17 | 276–287 | Observation | 8480-6 | Systolic blood pressure | _Tekanan Darah Diastolik_ → `Observation.status` (286, tanpa BQ) |
| 18 | 288–299 | Observation | 8462-4 | Diastolic blood pressure | _Frekuensi Nadi_ → `Observation.status` (298, tanpa BQ) |
| 19 | 300–312 | Observation | 8867-4 | Heart rate | _Respiratory Rate_ → `Observation.status` (311, tanpa BQ) |
| 20 | 313–325 | Observation | 9279-1 | Respiratory rate | _Suhu Badan_ → `Observation.status` (324, tanpa BQ) |
| 21 | 326–338 | Observation | 8310-5 | Body temperature | _LiLA_ → `Observation.status` (337, tanpa BQ) |
| 22 | 339–350 | Observation | 284473002.0 | Mid upper arm circumference | _Berat Badan_ → `Observation.status` (349, tanpa BQ) |
| 23 | 351–362 | Observation | 29463-7 | Body weight | _Tinggi Badan_ → `Observation.status` (361, tanpa BQ) |
| 24 | 363–374 | Observation | 8302-2 | Body height | _Gravida_ → `Observation.status` (373, tanpa BQ) |
| 25 | 375–386 | Observation | 11996-6 | [#] Pregnancies | _Partus_ → `Observation.status` (385, tanpa BQ) |
| 26 | 387–398 | Observation | 11977-6 | [#] Parity | _Abortus_ → `Observation.status` (397, tanpa BQ) |
| 27 | 399–410 | Observation | 69043-8 | Other pregnancy outcomes # | _Jarak kehamilan saat ini dengan kehamilan sebelumnya_ → `Observation.status` (409, tanpa BQ) |
| 28 | 411–423 | Observation | OC000001 | Jarak kehamilan | _Tinggi Fundus Uteri_ → `Observation.status` (422, tanpa BQ) |
| 29 | 424–436 | Observation | 11881-0 | Uterus Fundal height Tape measure | _Detak Jantung Janin_ → `Observation.identifier.value` (435, tanpa BQ) |
| 30 | 437–449 | Observation | 55283-6 | Fetal Heart rate | _Kondisi Detak Jantung Janin_ → `Observation.identifier.value` (448, tanpa BQ) |
| 31 | 450–464 | Observation | 289437007.0 | Finding of fetal heart rate | _Letak Janin_ → `Observation.identifier.value` (463, tanpa BQ) |
| 32 | 465–477 | Observation | 271692001.0 | Presentation of fetus | _Presentasi Janin_ → `Observation.identifier.value` (476, tanpa BQ) |
| 33 | 478–497 | Observation | 72155-5 | Position in womb Fetus [RHEA] | _Posisi Kepala Janin terhadap PAP (Pintu Atas Panggul)_ → `Observation.identifier.value` (496, tanpa BQ) |
| 34 | 498–511 | Observation | 249111004.0 | Engagement of head | _Kondisi Ketuban_ → `Observation.identifier.value` (510, tanpa BQ) |
| 35 | 512–521 | Observation | 289282009.0 | Amniotic membrane finding | – |
| 36 | 522–627 | QuestionnaireResponse | https://fhir.kemkes.go.id/sp/Questionnaire/Q0002 | – | _Faktor risiko INC_ → `QuestionnaireResponse.questionnaire` (522, tanpa BQ) |
| 37 | 628–640 | Observation | SP000123 | Integrasi Program | _Integrasi Program_ → `Observation.valueCodeableConcept.coding` (631, tanpa BQ) |
| 38 | 641–673 | Observation | 72150-6 | Delivery location | _Tempat Melahirkan_ → `Observation.valueCodeableConcept.coding` (644, tanpa BQ)<br>_Alamat Bersalin_ → `Observation.note` (673, tanpa BQ) |
| 39 | 689–703 | Observation | 76516-4 | Gestational age—​at birth | _Usia Kehamilan/ Gestasi pada saat Persalinan_ → `Observation.valueQuantity.value` (692, tanpa BQ) |
| 40 | 704–714 | Observation | 118215003.0 | Delivery finding | _Observasi dalam Persalinan_ → `Observation.valueString` (707, tanpa BQ) |
| 41 | 715–725 | Observation | 93857-1 | Date and time of obstetric delivery | _Tanggal dan Jam Persalinan_ → `Observation.valueDateTime` (718, tanpa BQ) |
| 42 | 726–747 | Observation | OC000013 | Penolong Persalinan | _Penolong Persalinan_ → `Observation.valueCodeableConcept.coding` (732, tanpa BQ)<br>_Nama Penolong Persalinan_ → `Observation.valueCodeableConcept.text` (740, tanpa BQ) |
| 43 | 748–767 | Observation | 57071-3 | Obstetric delivery method | _Cara Persalinan_ → `Observation.valueCodeableConcept.coding` (751, tanpa BQ) |
| 44 | 768–786 | Procedure | 73.59 | Other manually assisted delivery | _Prosedur Persalinan_ → `Procedure.category.coding` (768, tanpa BQ) |
| 45 | 787–804 | Observation | 405195003.0 | Intrapartum maternal status | _Keadaan Ibu_ → `Observation.valueCodeableConcept.coding` (790, tanpa BQ) |
| 46 | 805–825 | Observation | 387700009.0 | Prolonged latent phase of labor | _Kala I laten_ → `Observation.valueDateTime` (808, tanpa BQ) |
| 47 | 826–846 | Observation | 249120008.0 | Onset of labor first stage | _Kala I Aktif_ → `Observation.valueDateTime` (829, tanpa BQ) |
| 48 | 847–857 | Observation | 249160009.0 | Onset of labor second stage | _Kala II_ → `Observation.valueDateTime` (850, tanpa BQ) |
| 49 | 858–868 | Observation | OC000018 | Onset Kala III | _Kala III_ → `Observation.valueDateTime` (861, tanpa BQ) |
| 50 | 869–879 | Observation | 236994008.0 | Placental delivery procedure | _Plasenta lahir_ → `Observation.valueDateTime` (872, tanpa BQ) |
| 51 | 880–891 | Observation | 289267004.0 | Finding of completeness of placenta | _Kondisi Plasenta_ → `Observation.valueCodeableConcept.coding` (883, tanpa BQ) |
| 52 | 892–903 | Procedure | SP000127 | Injeksi Oksitosin | _Injeksi Oksitosin_ → `Procedure.category.coding` (892, tanpa BQ) |
| 53 | 904–915 | Procedure | 302384005.0 | Controlled cord traction of placenta | _Peregangan Tali Pusat_ → `Procedure.category.coding` (904, tanpa BQ) |
| 54 | 916–927 | Procedure | 236996005.0 | Abdominal uterine fundal massage | _Masase Fundus Uteri_ → `Procedure.category.coding` (916, tanpa BQ) |
| 55 | 928–938 | Observation | OC000019 | Onset Kala IV | _Kala IV_ → `Observation.valueDateTime` (931, tanpa BQ) |
| 56 | 939–953 | Condition | 9293002.0 | Atony of uterus | _Kondisi Kala 4_ → `Condition.clinicalStatus.coding` (939, tanpa BQ) |
| 57 | 954–967 | Observation | 719051004.0 | Quantity of postpartum maternal blood loss | _Jumlah Pendarahan Kala 4_ → `Observation.valueQuantity.value` (957, tanpa BQ) |
| 58 | 968–981 | Observation | 8480-6 | Systolic blood pressure | _Sistol Kala 4_ → `Observation.valueQuantity.value` (971, tanpa BQ) |
| 59 | 982–995 | Observation | 8462-4 | Diastolic blood pressure | _Diastol Kala 4_ → `Observation.valueQuantity.value` (985, tanpa BQ) |
| 60 | 996–1009 | Procedure | 717809003.0 | Immediate postpartum care | _Pemantauan Kala 4_ → `Procedure.category.coding` (996, tanpa BQ) |
| 61 | 1010–1029 | Condition | 199746004.0 | Obstructed labor | _Komplikasi Persalinan_ → `Condition.clinicalStatus.coding` (1010, tanpa BQ) |
| 62 | 1030–1056 | Observation | SP000379 | Tatalaksana Komplikasi Persalinan | _Tatalaksana Komplikasi Persalinan_ → `Observation.status` (1030, tanpa BQ)<br>_Resusitasi Cairan_ → `Observation.component.code.coding` (1033, tanpa BQ)<br>_Pemberian Obat Uterotonik_ → `Observation.component.code.coding` (1035, tanpa BQ)<br>_Kompresi bimanual_ → `Observation.component.code.coding` (1037, tanpa BQ)<br>_Penjahitan Jalan Lahir/Perineum_ → `Observation.component.code.coding` (1039, tanpa BQ)<br>_Manual Placenta_ → `Observation.component.code.coding` (1041, tanpa BQ)<br>_Pemberian MgSO4_ → `Observation.component.code.coding` (1043, tanpa BQ)<br>_Pemberian Anti Hipertensi_ → `Observation.component.code.coding` (1045, tanpa BQ)<br>_Lain-lain_ → `Observation.component.code.coding` (1047, tanpa BQ) |
| 63 | 1057–1070 | Observation | 63893-2 | Outcome of pregnancy | _Luaran Kehamilan_ → `Observation.valueCodeableConcept.coding` (1060, tanpa BQ) |
| 64 | 1071–1092 | ServiceRequest | 409014006.0 | Delivery care management | _Rujuk_ → `ServiceRequest.status` (1071, tanpa BQ)<br>_Faskes Rujukan_ → `ServiceRequest.locationCode.coding` (1084, tanpa BQ)<br>_Nama Faskes Rujukan_ → `ServiceRequest.locationCode.text` (1092, tanpa BQ) |
| 65 | 1093–1105 | Observation | SP000122 | Catat di Buku KIA | _Catat di buku KIA_ → `Observation.valueBoolean` (1095, tanpa BQ) |
| 66 | 1106–1121 | Procedure | SP000130 | Menggunakan Partograf | _Pelayanan Menggunakan Partograf_ → `Procedure.category.coding` (1106, tanpa BQ)<br>_Inisiasi Menyusu Dini (IMD)_ → `Procedure.category.coding` (1117, tanpa BQ) |
| 67 | 1122–1129 | Procedure | 431868002.0 | Initiation of breastfeeding | – |
| 68 | 1130–1141 | Observation | OC000016 | Waktu Inisiasi Menyusui Dini | _Waktu Inisiasi Menyusu Dini (IMD)_ → `Observation.valueCodeableConcept.coding` (1132, tanpa BQ) |
| 69 | 1142–1144 | Procedure | 409063005.0 | Counselling | _Konseling_ → `Procedure.category.coding` (1142, tanpa BQ) |
| 70 | 1145–1159 | Procedure | 409063005.0 | Counselling | – |
| 71 | 1160–1172 | Observation | SP000755 | Apakah Ibu pernah melakukan pemeriksaan kehamilan ke Faskes? | _Apakah Ibu pernah melakukan pemeriksaan kehamilan ke Faskes?_ → `Observation.valueCodeableConcept.coding` (1162, tanpa BQ) |
| 72 | 1173–1186 | Observation | 365662002.0 | Finding of amniotic fluid appearance | _Warna Ketuban_ → `Observation.valueCodeableConcept.coding` (1175, tanpa BQ) |
| 73 | 1187–1212 | Observation | 75204-8 | Prenatal care indicator [CDC.CS] | _Data Esensial ANC_ → `Observation.component.valueBoolean` (1190, tanpa BQ) |
| 74 | 1213–1224 | Observation | 246435002.0 | Number of fetuses | _jumlah janin_ → `Observation.valueInteger` (1217, tanpa BQ) |
| 75 | 1225–1235 | Observation | 81956-5 | Date and time of death [TimeStamp] | _waktu kematian ibu_ → `Observation.valueDateTime` (1228, tanpa BQ) |
| 76 | 1236–1246 | Observation | 79378-6 | Cause of death | _diagnosa dugaan penyebab kematian ibu_ → `Observation.valueString` (1239, tanpa BQ) |
| 77 | 1247–1257 | Observation | SP000139 | KB Pasca Plasenta | _kb iud pasca plasenta_ → `Observation.valueCodeableConcept.coding` (1250, tanpa BQ) |
| 78 | 1258–1268 | Observation | 63963-3 | Date of end of pregnancy | _Tanggal dan Jam Keguguran/Aborsi_ → `Observation.valueDateTime` (1261, tanpa BQ) |
| 79 | 1269–1280 | Observation | 81956-5 | Date and time of death [TimeStamp] | _Waktu Kematian Bayi_ → `Observation.valueDateTime` (1272, tanpa BQ) |
| 80 | 1281–1292 | Observation | 79378-6 | Cause of death | _Diagnosis Dugaan Sebab Kematian Bayi_ → `Observation.valueString` (1284, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 56 |
| Procedure | 9 |
| Condition | 3 |
| PractitionerRole | 2 |
| Practitioner | 2 |
| EpisodeOfCare | 2 |
| Patient | 1 |
| RelatedPerson | 1 |
| DocumentReference | 1 |
| Encounter | 1 |
| QuestionnaireResponse | 1 |
| ServiceRequest | 1 |
| **Total** | **80** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 91 | PractitionerRole | `PractitionerRole.code.coding` | 223366009.0 | Healthcare professional | http://snomed.info/sct |
| 2 | 92 | PractitionerRole | `PractitionerRole.code.coding` | SP000396 | Data entry staff | http://terminology.kemkes.go.id/sp |
| 3 | 93 | PractitionerRole | `PractitionerRole.code.coding` | SP000397 | Field/call center staff | http://terminology.kemkes.go.id/sp |
| 4 | 100 | PractitionerRole | `PractitionerRole.code.coding` | 309453006.0 | Registered midwife | http://snomed.info/sct |
| 5 | 101 | PractitionerRole | `PractitionerRole.code.coding` | 309343006.0 | Physician | http://snomed.info/sct |
| 6 | 102 | PractitionerRole | `PractitionerRole.code.coding` | 309367003.0 | Obstetrician and gynecologist | http://snomed.info/sct |
| 7 | 103 | PractitionerRole | `PractitionerRole.code.coding` | 224535009.0 | Registered nurse | http://snomed.info/sct |
| 8 | 140 | DocumentReference | `DocumentReference.content.format` | SP000732 | Buku KIA | http://terminology.kemkes.go.id/sp |
| 9 | 144 | Observation | `Observation.code.coding` | 385438008.0 | Source of information | http://snomed.info/sct |
| 10 | 145 | Observation | `Observation.valueCodeableConcept.coding` | SP000746 | Sumber data Manual Register Puskesmas | http://terminology.kemkes.go.id/sp |
| 11 | 146 | Observation | `Observation.valueCodeableConcept.coding` | SP000747 | Sumber data PNV Ruta | http://terminology.kemkes.go.id/sp |
| 12 | 147 | Observation | `Observation.valueCodeableConcept.coding` | SP000748 | Sumber data PNV Bides | http://terminology.kemkes.go.id/sp |
| 13 | 148 | Observation | `Observation.valueCodeableConcept.coding` | SP000749 | Sumber data Birth Confirmation | http://terminology.kemkes.go.id/sp |
| 14 | 149 | Observation | `Observation.valueCodeableConcept.coding` | SP000750 | Sumber data PMB (Praktik Mandiri Bidan) | http://terminology.kemkes.go.id/sp |
| 15 | 150 | Observation | `Observation.valueCodeableConcept.coding` | SP000751 | Sumber data Rumah Sakit | http://terminology.kemkes.go.id/sp |
| 16 | 151 | Observation | `Observation.valueCodeableConcept.coding` | SP000752 | Sumber data Lainnya | http://terminology.kemkes.go.id/sp |
| 17 | 169 | EpisodeOfCare | `EpisodeOfCare.type.coding` | ANC | Antenatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 18 | 180 | EpisodeOfCare | `EpisodeOfCare.type.coding` | PNC | Postnatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 19 | 203 | Condition | `Condition.code.coding` | 386337006.0 | Intrapartal care | http://snomed.info/sct |
| 20 | 220 | Encounter | `Encounter.hospitalization.admitSource.coding` | EHA000002 | Datang sendiri | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 21 | 221 | Encounter | `Encounter.hospitalization.admitSource.coding` | 305956004.0 | Referral by physician | http://snomed.info/sct |
| 22 | 222 | Encounter | `Encounter.hospitalization.admitSource.coding` | 306052007.0 | Referral by midwife | http://snomed.info/sct |
| 23 | 223 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000116 | Rujukan dari Puskesmas Pembantu | http://terminology.kemkes.go.id/sp |
| 24 | 224 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000117 | Rujukan dari Puskesmas | http://terminology.kemkes.go.id/sp |
| 25 | 225 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000118 | Rujukan dari Rumah Bersalin / Klinik | http://terminology.kemkes.go.id/sp |
| 26 | 226 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000119 | Rujukan dari Rumah Sakit | http://terminology.kemkes.go.id/sp |
| 27 | 227 | Encounter | `Encounter.hospitalization.admitSource.coding` | 185389009.0 | Follow-up visit | http://snomed.info/sct |
| 28 | 233 | Observation | `Observation.code.coding` | SP000131 | Status Pindahan | http://terminology.kemkes.go.id/sp |
| 29 | 245 | Observation | `Observation.code.coding` | 30525-0 | Age | http://loinc.org |
| 30 | 257 | Observation | `Observation.code.coding` | 75910-0 | Canadian triage and acuity scale [CTAS] | http://loinc.org |
| 31 | 258 | Observation | `Observation.valueCodeableConcept.coding` | LA6112-2 | 1.0 | http://loinc.org |
| 32 | 259 | Observation | `Observation.valueCodeableConcept.coding` | LA6113-0 | 2.0 | http://loinc.org |
| 33 | 260 | Observation | `Observation.valueCodeableConcept.coding` | LA6114-8 | 3.0 | http://loinc.org |
| 34 | 261 | Observation | `Observation.valueCodeableConcept.coding` | LA6115-5 | 4.0 | http://loinc.org |
| 35 | 262 | Observation | `Observation.valueCodeableConcept.coding` | LA10137-0 | 5.0 | http://loinc.org |
| 36 | 263 | Observation | `Observation.valueCodeableConcept.coding` | 63238001.0 | Dead on arrival at hospital | http://snomed.info/sct |
| 37 | 264 | Observation | `Observation.code.coding` | SP000383 | Keadaan Ibu Saat Tiba | http://terminology.kemkes.go.id/sp |
| 38 | 265 | Observation | `Observation.valueCodeableConcept.coding` | 438949009.0 | Alive | http://snomed.info/sct |
| 39 | 266 | Observation | `Observation.valueCodeableConcept.coding` | 419099009.0 | Dead | http://snomed.info/sct |
| 40 | 276 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 41 | 288 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://loinc.org |
| 42 | 300 | Observation | `Observation.code.coding` | 8867-4 | Heart rate | http://loinc.org |
| 43 | 313 | Observation | `Observation.code.coding` | 9279-1 | Respiratory rate | http://loinc.org |
| 44 | 326 | Observation | `Observation.code.coding` | 8310-5 | Body temperature | http://loinc.org |
| 45 | 339 | Observation | `Observation.code.coding` | 284473002.0 | Mid upper arm circumference | http://snomed.info/sct |
| 46 | 351 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 47 | 363 | Observation | `Observation.code.coding` | 8302-2 | Body height | http://loinc.org |
| 48 | 375 | Observation | `Observation.code.coding` | 11996-6 | [#] Pregnancies | http://loinc.org |
| 49 | 376 | Observation | `Observation.code.coding` | ANC.B6.DE24 | Number of pregnancies (gravida) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 50 | 387 | Observation | `Observation.code.coding` | 11977-6 | [#] Parity | http://loinc.org |
| 51 | 388 | Observation | `Observation.code.coding` | ANC.B6.DE32 | Parity | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 52 | 399 | Observation | `Observation.code.coding` | 69043-8 | Other pregnancy outcomes # | http://loinc.org |
| 53 | 400 | Observation | `Observation.code.coding` | ANC.B6.DE25 | Number of miscarriages and/or abortions | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 54 | 411 | Observation | `Observation.code.coding` | OC000001 | Jarak kehamilan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 55 | 412 | Observation | `Observation.code.coding` | ANC.SS.DE53 | Jarak kehamilan | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 56 | 424 | Observation | `Observation.code.coding` | 11881-0 | Uterus Fundal height Tape measure | http://loinc.org |
| 57 | 437 | Observation | `Observation.code.coding` | 55283-6 | Fetal Heart rate | http://loinc.org |
| 58 | 450 | Observation | `Observation.code.coding` | 289437007.0 | Finding of fetal heart rate | http://snomed.info/sct |
| 59 | 451 | Observation | `Observation.valueCodeableConcept.coding` | 289441006.0 | Normal fetal heart rate | http://snomed.info/sct |
| 60 | 452 | Observation | `Observation.valueCodeableConcept.coding` | 289440007.0 | Fetal heart rate not observed | http://snomed.info/sct |
| 61 | 453 | Observation | `Observation.valueCodeableConcept.coding` | 312668007.0 | Abnormal fetal heart rate | http://snomed.info/sct |
| 62 | 454 | Observation | `Observation.valueCodeableConcept.coding` | 289439005.0 | Fetal heart rate absent | http://snomed.info/sct |
| 63 | 465 | Observation | `Observation.code.coding` | 271692001.0 | Presentation of fetus | http://snomed.info/sct |
| 64 | 466 | Observation | `Observation.valueCodeableConcept.coding` | 398236008.0 | Intrauterine | http://snomed.info/sct |
| 65 | 467 | Observation | `Observation.valueCodeableConcept.coding` | 298109001.0 | Ectopic | http://snomed.info/sct |
| 66 | 478 | Observation | `Observation.code.coding` | 72155-5 | Position in womb Fetus [RHEA] | http://loinc.org |
| 67 | 479 | Observation | `Observation.valueCodeableConcept.coding` | 70028003.0 | Vertex presentation | http://snomed.info/sct |
| 68 | 480 | Observation | `Observation.valueCodeableConcept.coding` | 249083005.0 | Posterior fontanelle presenting | http://snomed.info/sct |
| 69 | 481 | Observation | `Observation.valueCodeableConcept.coding` | 288203005.0 | Transverse/oblique lie | http://snomed.info/sct |
| 70 | 482 | Observation | `Observation.valueCodeableConcept.coding` | 23954006.0 | Acromion presentation | http://snomed.info/sct |
| 71 | 483 | Observation | `Observation.valueCodeableConcept.coding` | 6096002.0 | Breech presentation | http://snomed.info/sct |
| 72 | 484 | Observation | `Observation.valueCodeableConcept.coding` | 8014007.0 | Brow presentation of fetus | http://snomed.info/sct |
| 73 | 485 | Observation | `Observation.valueCodeableConcept.coding` | 8017000.0 | Face presentation | http://snomed.info/sct |
| 74 | 486 | Observation | `Observation.valueCodeableConcept.coding` | 249097002.0 | Footling breech presentation | http://snomed.info/sct |
| 75 | 487 | Observation | `Observation.valueCodeableConcept.coding` | 124736009.0 | Compound presentation | http://snomed.info/sct |
| 76 | 498 | Observation | `Observation.code.coding` | 249111004.0 | Engagement of head | http://snomed.info/sct |
| 77 | 499 | Observation | `Observation.valueCodeableConcept.coding` | 249112006.0 | Head engaged | http://snomed.info/sct |
| 78 | 500 | Observation | `Observation.valueCodeableConcept.coding` | 62098001.0 | Head not engaged | http://snomed.info/sct |
| 79 | 501 | Observation | `Observation.dataAbsentReason` | unknown | Unknown | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 80 | 512 | Observation | `Observation.code.coding` | 289282009.0 | Amniotic membrane finding | http://snomed.info/sct |
| 81 | 513 | Observation | `Observation.valueCodeableConcept.coding` | 249125003.0 | Intact membranes | http://snomed.info/sct |
| 82 | 514 | Observation | `Observation.valueCodeableConcept.coding` | SP000120 | Non-intact membrane | http://terminology.kemkes.go.id/sp |
| 83 | 630 | Observation | `Observation.code.coding` | SP000123 | Integrasi Program | http://terminology.kemkes.go.id/sp |
| 84 | 631 | Observation | `Observation.valueCodeableConcept.coding` | SP000046 | Terapi Antiretroviral (ART) | http://terminology.kemkes.go.id/sp |
| 85 | 632 | Observation | `Observation.valueCodeableConcept.coding` | SP000124 | Obat anti malaria | http://terminology.kemkes.go.id/sp |
| 86 | 633 | Observation | `Observation.valueCodeableConcept.coding` | SP000125 | Obar anti hepatitis B | http://terminology.kemkes.go.id/sp |
| 87 | 643 | Observation | `Observation.code.coding` | 72150-6 | Delivery location | http://loinc.org |
| 88 | 644 | Observation | `Observation.valueCodeableConcept.coding` | 264362003.0 | Home | http://snomed.info/sct |
| 89 | 645 | Observation | `Observation.valueCodeableConcept.coding` | OT000001 | Polindes | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 90 | 646 | Observation | `Observation.valueCodeableConcept.coding` | OT000002 | Pustu | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 91 | 647 | Observation | `Observation.valueCodeableConcept.coding` | 102.0 | Pusat Kesehatan Masyarakat | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 92 | 648 | Observation | `Observation.valueCodeableConcept.coding` | 103.0 | Klinik | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 93 | 649 | Observation | `Observation.valueCodeableConcept.coding` | OT000008 | Rumah Bersalin | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 94 | 650 | Observation | `Observation.valueCodeableConcept.coding` | 82242000.0 | Children’s hospital | http://snomed.info/sct |
| 95 | 651 | Observation | `Observation.valueCodeableConcept.coding` | 104.0 | Rumah Sakit | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 96 | 652 | Observation | `Observation.valueCodeableConcept.coding` | OT000004 | Bidan Praktek Mandiri | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 97 | 653 | Observation | `Observation.valueCodeableConcept.coding` | LT000008 | Dalam perjalanan dari rumah/masyarakat | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 98 | 654 | Observation | `Observation.valueCodeableConcept.coding` | LT000009 | Dalam perjalanan ke faskes lain | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 99 | 655 | Observation | `Observation.valueCodeableConcept.coding` | LT000007 | Rumah Dukun | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 100 | 656 | Observation | `Observation.valueCodeableConcept.coding` | OT000003 | RS ODHA | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 101 | 657 | Observation | `Observation.valueCodeableConcept.coding` | OT000006 | Rumah Sakit Pemerintah | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 102 | 658 | Observation | `Observation.valueCodeableConcept.coding` | OT000007 | Rumah Sakit Swasta | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 103 | 659 | Observation | `Observation.valueCodeableConcept.coding` | LT000006 | Rumah Ibu | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 104 | 660 | Observation | `Observation.valueCodeableConcept.coding` | OT000010 | Klinik Medis Utama | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 105 | 661 | Observation | `Observation.valueCodeableConcept.coding` | OT000011 | Klinik Medis Pratama | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 106 | 662 | Observation | `Observation.valueCodeableConcept.coding` | 101.0 | Tempat Praktik Mandiri Tenaga Kesehatan | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 107 | 663 | Observation | `Observation.valueCodeableConcept.coding` | 394573001.0 | Maternity clinic | http://snomed.info/sct |
| 108 | 664 | Observation | `Observation.valueCodeableConcept.coding` | LT000010 | Lainnya | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 109 | 665 | Observation | `Observation.valueCodeableConcept.coding` | LT000011 | Belum Tahu | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 110 | 691 | Observation | `Observation.code.coding` | 76516-4 | Gestational age—​at birth | http://loinc.org |
| 111 | 694 | Observation | `Observation.component.code.coding` | SP000398 | Usia Kehamilan Saat Persalinan (hari) | http://terminology.kemkes.go.id/sp |
| 112 | 706 | Observation | `Observation.code.coding` | 118215003.0 | Delivery finding | http://snomed.info/sct |
| 113 | 717 | Observation | `Observation.code.coding` | 93857-1 | Date and time of obstetric delivery | http://loinc.org |
| 114 | 731 | Observation | `Observation.code.coding` | OC000013 | Penolong Persalinan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 115 | 732 | Observation | `Observation.valueCodeableConcept.coding` | 303071001.0 | Person in the family | http://snomed.info/sct |
| 116 | 733 | Observation | `Observation.valueCodeableConcept.coding` | OV000012 | Dukun | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 117 | 734 | Observation | `Observation.valueCodeableConcept.coding` | 309453006.0 | Registered midwife | http://snomed.info/sct |
| 118 | 735 | Observation | `Observation.valueCodeableConcept.coding` | 309343006.0 | Physician | http://snomed.info/sct |
| 119 | 736 | Observation | `Observation.valueCodeableConcept.coding` | 11935004.0 | Obstetrician | http://snomed.info/sct |
| 120 | 737 | Observation | `Observation.valueCodeableConcept.coding` | 125677006.0 | Relative | http://snomed.info/sct |
| 121 | 738 | Observation | `Observation.valueCodeableConcept.coding` | 106292003.0 | Professional nurse | http://snomed.info/sct |
| 122 | 739 | Observation | `Observation.valueCodeableConcept.coding` | 257514003.0 | Member of public involved incidentally | http://snomed.info/sct |
| 123 | 750 | Observation | `Observation.code.coding` | 57071-3 | Obstetric delivery method | http://loinc.org |
| 124 | 751 | Observation | `Observation.valueCodeableConcept.coding` | 48782003.0 | Delivery normal | http://snomed.info/sct |
| 125 | 752 | Observation | `Observation.valueCodeableConcept.coding` | 200138003.0 | Vacuum extractor delivery - delivered | http://snomed.info/sct |
| 126 | 753 | Observation | `Observation.valueCodeableConcept.coding` | 200130005.0 | Forceps delivery - delivered | http://snomed.info/sct |
| 127 | 754 | Observation | `Observation.valueCodeableConcept.coding` | 200144004.0 | Deliveries by cesarean | http://snomed.info/sct |
| 128 | 769 | Procedure | `Procedure.code.coding` | 73.59 | Other manually assisted delivery | http://hl7.org/fhir/sid/icd-9-cm |
| 129 | 770 | Procedure | `Procedure.code.coding` | 72.7 | Vacuum extraction | http://hl7.org/fhir/sid/icd-9-cm |
| 130 | 771 | Procedure | `Procedure.code.coding` | 72.0 | Low forceps delivery | http://hl7.org/fhir/sid/icd-9-cm |
| 131 | 772 | Procedure | `Procedure.code.coding` | 74.1 | Classical cesarean section | http://hl7.org/fhir/sid/icd-9-cm |
| 132 | 789 | Observation | `Observation.code.coding` | 405195003.0 | Intrapartum maternal status | http://snomed.info/sct |
| 133 | 790 | Observation | `Observation.valueCodeableConcept.coding` | 102514002.0 | Well female adult | http://snomed.info/sct |
| 134 | 791 | Observation | `Observation.valueCodeableConcept.coding` | 39104002.0 | Illness | http://snomed.info/sct |
| 135 | 792 | Observation | `Observation.valueCodeableConcept.coding` | 131148009.0 | Bleeding | http://snomed.info/sct |
| 136 | 793 | Observation | `Observation.valueCodeableConcept.coding` | 386661006.0 | Fever | http://snomed.info/sct |
| 137 | 794 | Observation | `Observation.valueCodeableConcept.coding` | 91175000.0 | Seizure | http://snomed.info/sct |
| 138 | 795 | Observation | `Observation.valueCodeableConcept.coding` | 249215002.0 | Odor of lochia | http://snomed.info/sct |
| 139 | 796 | Observation | `Observation.valueCodeableConcept.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 140 | 797 | Observation | `Observation.valueCodeableConcept.coding` | 59283008.0 | Maternal death | http://snomed.info/sct |
| 141 | 807 | Observation | `Observation.code.coding` | 387700009.0 | Prolonged latent phase of labor | http://snomed.info/sct |
| 142 | 816 | Observation | `Observation.component.code.coding` | 398143009.0 | Uterine contraction monitoring | http://snomed.info/sct |
| 143 | 817 | Observation | `Observation.component.valueCodeableConcept.coding` | 289708007.0 | Regular uterine contractions | http://snomed.info/sct |
| 144 | 818 | Observation | `Observation.component.valueCodeableConcept.coding` | 289739009.0 | Uterine contractions problem | http://snomed.info/sct |
| 145 | 819 | Observation | `Observation.component.code.coding` | 364270005.0 | Frequency of uterine contraction | http://snomed.info/sct |
| 146 | 822 | Observation | `Observation.component.code.coding` | 364274001.0 | Duration of uterine contraction | http://snomed.info/sct |
| 147 | 823 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000399 | <20 detik | http://terminology.kemkes.go.id/sp |
| 148 | 824 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000400 | 20-40 detik | http://terminology.kemkes.go.id/sp |
| 149 | 825 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000401 | >40 detik | http://terminology.kemkes.go.id/sp |
| 150 | 828 | Observation | `Observation.code.coding` | 249120008.0 | Onset of labor first stage | http://snomed.info/sct |
| 151 | 837 | Observation | `Observation.component.code.coding` | 398143009.0 | Uterine contraction monitoring | http://snomed.info/sct |
| 152 | 838 | Observation | `Observation.component.valueCodeableConcept.coding` | 289708007.0 | Regular uterine contractions | http://snomed.info/sct |
| 153 | 839 | Observation | `Observation.component.valueCodeableConcept.coding` | 289739009.0 | Uterine contractions problem | http://snomed.info/sct |
| 154 | 840 | Observation | `Observation.component.code.coding` | 364270005.0 | Frequency of uterine contraction | http://snomed.info/sct |
| 155 | 843 | Observation | `Observation.component.code.coding` | 364274001.0 | Duration of uterine contraction | http://snomed.info/sct |
| 156 | 844 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000399 | <20 detik | http://terminology.kemkes.go.id/sp |
| 157 | 845 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000400 | 20-40 detik | http://terminology.kemkes.go.id/sp |
| 158 | 846 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000401 | >40 detik | http://terminology.kemkes.go.id/sp |
| 159 | 849 | Observation | `Observation.code.coding` | 249160009.0 | Onset of labor second stage | http://snomed.info/sct |
| 160 | 860 | Observation | `Observation.code.coding` | OC000018 | Onset Kala III | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 161 | 871 | Observation | `Observation.code.coding` | 236994008.0 | Placental delivery procedure | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 162 | 882 | Observation | `Observation.code.coding` | 289267004.0 | Finding of completeness of placenta | http://snomed.info/sct |
| 163 | 883 | Observation | `Observation.valueCodeableConcept.coding` | 249170006.0 | Complete placenta at delivery | http://snomed.info/sct |
| 164 | 884 | Observation | `Observation.valueCodeableConcept.coding` | 268479002.0 | Incomplete placenta at delivery | http://snomed.info/sct |
| 165 | 894 | Procedure | `Procedure.code.coding` | SP000127 | Injeksi Oksitosin | http://terminology.kemkes.go.id/sp |
| 166 | 906 | Procedure | `Procedure.code.coding` | 302384005.0 | Controlled cord traction of placenta | http://snomed.info/sct |
| 167 | 918 | Procedure | `Procedure.code.coding` | 236996005.0 | Abdominal uterine fundal massage | http://snomed.info/sct |
| 168 | 930 | Observation | `Observation.code.coding` | OC000019 | Onset Kala IV | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 169 | 942 | Condition | `Condition.code.coding` | 9293002.0 | Atony of uterus | http://snomed.info/sct |
| 170 | 943 | Condition | `Condition.code.coding` | 48194001.0 | Postpartum hemorrhage | http://snomed.info/sct |
| 171 | 944 | Condition | `Condition.code.coding` | 1148943004.0 | Retention of placenta and uterine membrane | http://snomed.info/sct |
| 172 | 945 | Condition | `Condition.code.coding` | 283380005.0 | Laceration of perineum | http://snomed.info/sct |
| 173 | 946 | Condition | `Condition.code.coding` | 84007008.0 | Shock during AND/OR following labor AND/OR delivery | http://snomed.info/sct |
| 174 | 947 | Condition | `Condition.code.coding` | 118216002.0 | Labor finding | http://snomed.info/sct |
| 175 | 956 | Observation | `Observation.code.coding` | 719051004.0 | Quantity of postpartum maternal blood loss | http://snomed.info/sct |
| 176 | 970 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 177 | 984 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://loinc.org |
| 178 | 999 | Procedure | `Procedure.code.coding` | 717809003.0 | Immediate postpartum care | http://snomed.info/sct |
| 179 | 1013 | Condition | `Condition.code.coding` | 199746004.0 | Obstructed labor | http://snomed.info/sct |
| 180 | 1014 | Condition | `Condition.code.coding` | 48194001.0 | Pregnancy-induced hypertension | http://snomed.info/sct |
| 181 | 1015 | Condition | `Condition.code.coding` | 38010008.0 | Intrapartum hemorrhage | http://snomed.info/sct |
| 182 | 1016 | Condition | `Condition.code.coding` | 40733004.0 | Infectious disease | http://snomed.info/sct |
| 183 | 1017 | Condition | `Condition.code.coding` | 386639001.0 | Termination of pregnancy | http://snomed.info/sct |
| 184 | 1018 | Condition | `Condition.code.coding` | 44223004.0 | Premature rupture of membranes | http://snomed.info/sct |
| 185 | 1019 | Condition | `Condition.code.coding` | 398254007.0 | Pre-eclampsia | http://snomed.info/sct |
| 186 | 1020 | Condition | `Condition.code.coding` | 15938005.0 | Eclampsia | http://snomed.info/sct |
| 187 | 1021 | Condition | `Condition.code.coding` | 9293002.0 | Atony of uterus | http://snomed.info/sct |
| 188 | 1022 | Condition | `Condition.code.coding` | 283380005.0 | Laceration of perineum | http://snomed.info/sct |
| 189 | 1023 | Condition | `Condition.code.coding` | 199745000.0 | Complication occurring during labor and delivery | http://snomed.info/sct |
| 190 | 1032 | Observation | `Observation.code.coding` | SP000379 | Tatalaksana Komplikasi Persalinan | http://terminology.kemkes.go.id/sp |
| 191 | 1033 | Observation | `Observation.component.code.coding` | 430701006.0 | Resuscitation using intravenous fluid | http://snomed.info/sct |
| 192 | 1035 | Observation | `Observation.component.code.coding` | SP000156 | Pemberian Obat Uterotonik | http://terminology.kemkes.go.id/sp |
| 193 | 1037 | Observation | `Observation.component.code.coding` | 236998006.0 | Bimanual uterine massage | http://snomed.info/sct |
| 194 | 1039 | Observation | `Observation.component.code.coding` | 360362007.0 | Suture of laceration of perineum | http://snomed.info/sct |
| 195 | 1041 | Observation | `Observation.component.code.coding` | 28233006.0 | Manual removal of retained placenta | http://snomed.info/sct |
| 196 | 1043 | Observation | `Observation.component.code.coding` | SP000013 | Pemberian MgSO4 | http://terminology.kemkes.go.id/sp |
| 197 | 1045 | Observation | `Observation.component.code.coding` | 308116003.0 | Antihypertensive therapy | http://snomed.info/sct |
| 198 | 1047 | Observation | `Observation.component.code.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 199 | 1059 | Observation | `Observation.code.coding` | 63893-2 | Outcome of pregnancy | http://loinc.org |
| 200 | 1060 | Observation | `Observation.valueCodeableConcept.coding` | LA14270-5 | Live birth | http://loinc.org |
| 201 | 1061 | Observation | `Observation.valueCodeableConcept.coding` | LA14271-3 | Stillborn | http://loinc.org |
| 202 | 1062 | Observation | `Observation.valueCodeableConcept.coding` | LA14272-1 | Miscarriage | http://loinc.org |
| 203 | 1063 | Observation | `Observation.valueCodeableConcept.coding` | LA14273-9 | Induced abortion | http://loinc.org |
| 204 | 1075 | ServiceRequest | `ServiceRequest.code.coding` | 409014006.0 | Delivery care management | http://snomed.info/sct |
| 205 | 1084 | ServiceRequest | `ServiceRequest.locationCode.coding` | SP000129 | Puskesmas PONED | http://terminology.kemkes.go.id/sp |
| 206 | 1088 | ServiceRequest | `ServiceRequest.locationCode.coding` | SP000128 | Rumah Sakit Ibu dan Anak | http://terminology.kemkes.go.id/sp |
| 207 | 1094 | Observation | `Observation.code.coding` | SP000122 | Catat di Buku KIA | http://terminology.kemkes.go.id/sp |
| 208 | 1097 | Observation | `Observation.dataAbsentReason.coding` | not-applicable | Not Applicable | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 209 | 1109 | Procedure | `Procedure.code.coding` | SP000130 | Menggunakan Partograf | http://terminology.kemkes.go.id/sp |
| 210 | 1122 | Procedure | `Procedure.code.coding` | 431868002.0 | Initiation of breastfeeding | http://snomed.info/sct |
| 211 | 1131 | Observation | `Observation.code.coding` | OC000016 | Waktu Inisiasi Menyusui Dini | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 212 | 1132 | Observation | `Observation.valueCodeableConcept.coding` | OV000014 | Kurang dari 1 Jam | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 213 | 1133 | Observation | `Observation.valueCodeableConcept.coding` | OV000015 | Lebih dari 1 Jam | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 214 | 1144 | Procedure | `Procedure.code.coding` | 409063005.0 | Counselling | http://snomed.info/sct |
| 215 | 1146 | Procedure | `Procedure.code.coding` | 409063005.0 | Counselling | http://snomed.info/sct |
| 216 | 1147 | Procedure | `Procedure.code.coding` | ED000008 | Edukasi Tanda Bahaya Kehamilan, Bersalin dan Nifas | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 217 | 1148 | Procedure | `Procedure.code.coding` | SP000121 | Edukasi Tanda Bahaya Baru Lahir | http://terminology.kemkes.go.id/sp |
| 218 | 1149 | Procedure | `Procedure.code.coding` | ED000009 | Edukasi IMD dan ASI Eksklusif | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 219 | 1150 | Procedure | `Procedure.code.coding` | ED000005 | Edukasi Gizi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 220 | 1151 | Procedure | `Procedure.code.coding` | PC000001 | Perawatan Tali Pusat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 221 | 1152 | Procedure | `Procedure.code.coding` | ED000010 | Edukasi PHBS | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 222 | 1161 | Observation | `Observation.code.coding` | SP000755 | Apakah Ibu pernah melakukan pemeriksaan kehamilan ke Faskes? | http://terminology.kemkes.go.id/sp |
| 223 | 1162 | Observation | `Observation.valueCodeableConcept.coding` | SP000786 | Ya, pernah melakukan pemeriksaan kehamilan di fasilitas kesehatan | http://terminology.kemkes.go.id/sp |
| 224 | 1163 | Observation | `Observation.valueCodeableConcept.coding` | SP000787 | Ya, pernah melakukan pemeriksaan kehamilan di fasilitas kesehatan namun di luar kota | http://terminology.kemkes.go.id/sp |
| 225 | 1164 | Observation | `Observation.valueCodeableConcept.coding` | SP000788 | Tidak pernah melakukan pemeriksaan kehamilan di fasilitas kesehatan | http://terminology.kemkes.go.id/sp |
| 226 | 1174 | Observation | `Observation.code.coding` | 365662002.0 | Finding of amniotic fluid appearance | http://snomed.info/sct |
| 227 | 1175 | Observation | `Observation.valueCodeableConcept.coding` | 168090003.0 | Amniotic fluid clear | http://snomed.info/sct |
| 228 | 1176 | Observation | `Observation.valueCodeableConcept.coding` | 408781009.0 | Straw colored amniotic fluid | http://snomed.info/sct |
| 229 | 1177 | Observation | `Observation.valueCodeableConcept.coding` | 249134008.0 | Bloodstained liquor | http://snomed.info/sct |
| 230 | 1178 | Observation | `Observation.valueCodeableConcept.coding` | 168092006.0 | Amniotic fluid -meconium stain | http://snomed.info/sct |
| 231 | 1188 | Observation | `Observation.code.coding` | 75204-8 | Prenatal care indicator [CDC.CS] | http://loinc.org |
| 232 | 1189 | Observation | `Observation.component.code.coding` | 101572-6 | Prenatal visits for this pregnancy | http://loinc.org |
| 233 | 1191 | Observation | `Observation.component.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 234 | 1193 | Observation | `Observation.component.code.coding` | 8302-2 | Body height | http://loinc.org |
| 235 | 1195 | Observation | `Observation.component.code.coding` | 35094-2 | Blood pressure panel | http://loinc.org |
| 236 | 1197 | Observation | `Observation.component.code.coding` | 11881-0 | Uterus Fundal height Tape measure | http://loinc.org |
| 237 | 1199 | Observation | `Observation.component.code.coding` | SP000001 | Skrining Imunisasi Tetanus Toksoid | http://terminology.kemkes.go.id/sp |
| 238 | 1201 | Observation | `Observation.component.code.coding` | SP000008 | Pemberian Tablet Tambah Darah | http://terminology.kemkes.go.id/sp |
| 239 | 1203 | Observation | `Observation.component.code.coding` | 15220000.0 | Laboratory test | http://snomed.info/sct |
| 240 | 1215 | Observation | `Observation.code.coding` | 246435002.0 | Number of fetuses | http://snomed.info/sct |
| 241 | 1216 | Observation | `Observation.code.coding` | ANC.B8.DE109 | Number of fetuses | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 242 | 1227 | Observation | `Observation.code.coding` | 81956-5 | Date and time of death [TimeStamp] | http://loinc.org |
| 243 | 1238 | Observation | `Observation.code.coding` | 79378-6 | Cause of death | http://loinc.org |
| 244 | 1249 | Observation | `Observation.code.coding` | SP000139 | KB Pasca Plasenta | http://terminology.kemkes.go.id/sp |
| 245 | 1250 | Observation | `Observation.valueCodeableConcept.coding` | LA6527-1 | Intrauterine device | http://loinc.org |
| 246 | 1260 | Observation | `Observation.code.coding` | 63963-3 | Date of end of pregnancy | http://loinc.org |
| 247 | 1271 | Observation | `Observation.code.coding` | 81956-5 | Date and time of death [TimeStamp] | http://loinc.org |
| 248 | 1283 | Observation | `Observation.code.coding` | 79378-6 | Cause of death | http://loinc.org |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 114 |
| http://terminology.kemkes.go.id/sp | 44 |
| http://loinc.org | 43 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 15 |
| http://terminology.kemkes.go.id/CodeSystem/organization-type | 13 |
| http://terminology.kemkes.go.id/CodeSystem/location-type | 6 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 4 |
| http://hl7.org/fhir/sid/icd-9-cm | 4 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 2 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 2 |
| http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes | 1 |
| **Total** | **248** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 44 | – | Jenis Faskes | Organization | `Organization.type` |
| 48 | – | Nama Faskes INC | Organization | `Organization.name` |
| 64 | – | Email Faskes | Organization | `Organization.telecom.use` |
| 67 | – | Gedung Faskes | Location | `Location.identifier` |
