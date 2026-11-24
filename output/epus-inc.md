# Output Form: ePuskesmas KIA Harian INC

Sumber: `mapping/phdt-data-dictionary-epus-inc.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-epus-inc.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 69 |
| Code (`jumlah code` = 1) | 206 |
| Code unik (code + CodeSystem) | 180 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 22 |
| Variabel BQ (unik) | 0 |
| Variabel raw (variabel dictionary; belum ada file mentah) | 93 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–33 | Patient | – | – | _Nama Ibu_ → `Patient.name.text` (2, tanpa BQ)<br>_NIK Ibu_ → `Patient.identifier.value` (5, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (7, tanpa BQ)<br>_No HP_ → `Patient.telecom` (8, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (11, tanpa BQ)<br>_Alamat Domisili_ → `Patient.address.use` (12, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (18, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (21, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.extension.valueCode` (24, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.extension.valueCode` (27, tanpa BQ)<br>_RW_ → `Patient.address.extension.extension.valueCode` (30, tanpa BQ)<br>_RT_ → `Patient.address.extension.extension.valueCode` (33, tanpa BQ)<br>_Nama Bayi_ → `Patient.name.text` (1071, tanpa BQ)<br>_Jenis Kelamin Bayi_ → `Patient.gender` (1072, tanpa BQ)<br>_Tanggal lahir bayi_ → `Patient.birthDate` (1074, tanpa BQ) |
| 2 | 34–41 | RelatedPerson | – | – | _Nama Pendamping_ → `RelatedPerson.name.text` (35, tanpa BQ)<br>_NIK Pendamping_ → `RelatedPerson.identifier.value` (40, tanpa BQ) |
| 3 | 88–94 | PractitionerRole | – | – | _Jenis Tenaga Pemeriksa_ → `PractitionerRole.active` (88, tanpa BQ) |
| 4 | 95–115 | Practitioner | – | – | _Nama Pemeriksa_ → `Practitioner.name.text` (97, tanpa BQ) |
| 5 | 116–130 | EpisodeOfCare | ANC | Antenatal Care | _Episode ANC Ibu_ → `EpisodeOfCare.identifer` (116, tanpa BQ)<br>_HPHT_ → `EpisodeOfCare.statusHistory.period.start` (119, tanpa BQ) |
| 6 | 131–146 | Encounter | – | – | _Jenis Kunjungan INC_ → `Encounter.class` (133, tanpa BQ)<br>_Tanggal Masuk INC_ → `Encounter.period.start` (141, tanpa BQ)<br>_Tanggal Keluar INC_ → `Encounter.period.end` (142, tanpa BQ) |
| 7 | 147–154 | Condition | 386337006 | Intrapartal care | _Diagnosis Masuk_ → `Condition.clinicalStatus.coding` (147, tanpa BQ) |
| 8 | 177–188 | Observation | SP000131 | Status Pindahan | _Status Pindahan_ → `Observation.valueBoolean` (180, tanpa BQ) |
| 9 | 189–200 | Observation | 30525-0 | Age | _Umur_ → `Observation.valueQuantity.value` (192, tanpa BQ) |
| 10 | 201–212 | Observation | SP000383 | Keadaan Ibu Saat Tiba | _Keadaan Ibu Saat Tiba_ → `Observation.valueCodeableConcept.coding` (204, tanpa BQ) |
| 11 | 213–224 | Observation | 8480-6 | Systolic blood pressure | _Tekanan Darah Sistolik_ → `Observation.valueQuantity.value` (216, tanpa BQ) |
| 12 | 225–236 | Observation | 8462-4 | Diastolic blood pressure | _Tekanan Darah Diastolik_ → `Observation.valueQuantity.value` (228, tanpa BQ) |
| 13 | 237–249 | Observation | 8867-4 | Heart rate | _Frekuensi Nadi_ → `Observation.valueQuantity.value` (240, tanpa BQ) |
| 14 | 250–262 | Observation | 9279-1 | Respiratory rate | _Respiratory Rate_ → `Observation.valueQuantity.value` (253, tanpa BQ) |
| 15 | 263–275 | Observation | – | – | _Suhu Badan_ → `Observation.valueQuantity.value` (266, tanpa BQ) |
| 16 | 276–287 | Observation | 284473002 | Mid upper arm circumference | _LiLA_ → `Observation.valueQuantity.value` (279, tanpa BQ) |
| 17 | 288–299 | Observation | 29463-7 | Body weight | _Berat Badan_ → `Observation.valueQuantity.value` (291, tanpa BQ) |
| 18 | 300–311 | Observation | 8302-2 | Body height | _Tinggi Badan_ → `Observation.valueQuantity.value` (303, tanpa BQ) |
| 19 | 312–324 | Observation | OC000001 | Jarak kehamilan | _Jarak kehamilan saat ini dengan kehamilan sebelumnya_ → `Observation.valueQuantity.value` (316, tanpa BQ) |
| 20 | 325–338 | Observation | 11881-0 | Uterus Fundal height Tape measure | _Tinggi Fundus Uteri_ → `Observation.valueQuantity.value` (328, tanpa BQ)<br>_Detak Jantung Janin_ → `Observation.identifier.value` (338, tanpa BQ) |
| 21 | 339–351 | Observation | 55283-6 | Fetal Heart rate | _Kondisi Detak Jantung Janin_ → `Observation.identifier.value` (351, tanpa BQ) |
| 22 | 352–366 | Observation | 289437007 | Finding of fetal heart rate | _Letak Janin_ → `Observation.identifier.value` (366, tanpa BQ) |
| 23 | 367–380 | Observation | 271692001 | Presentation of fetus | _Presentasi Janin_ → `Observation.identifier.value` (380, tanpa BQ) |
| 24 | 381–405 | Observation | 72155-5 | Position in womb Fetus [RHEA] | _Posisi Kepala Janin terhadap PAP (Pintu Atas Panggul)_ → `Observation.identifier.value` (405, tanpa BQ) |
| 25 | 406–419 | Observation | 249111004 | Engagement of head | _Kondisi Ketuban_ → `Observation.identifier.value` (419, tanpa BQ) |
| 26 | 420–431 | Observation | 289282009 | Amniotic membrane finding | – |
| 27 | 432–537 | QuestionnaireResponse | – | – | _Faktor risiko INC_ → `QuestionnaireResponse.questionnaire` (432, tanpa BQ) |
| 28 | 538–550 | Observation | SP000123 | Integrasi Program | _Integrasi Program_ → `Observation.valueCodeableConcept.coding` (541, tanpa BQ) |
| 29 | 551–582 | Observation | 72150-6 | Delivery location | _Tempat Melahirkan_ → `Observation.valueCodeableConcept.coding` (554, tanpa BQ) |
| 30 | 598–609 | Observation | 18185-9 | Gestational age | _Usia Kehamilan menurut HPHT_ → `Observation.valueQuantity.value` (601, tanpa BQ) |
| 31 | 610–621 | Observation | 76516-4 | Gestational age—​at birth | _Usia Kehamilan/ Gestasi pada saat Persalinan_ → `Observation.valueQuantity.value` (613, tanpa BQ) |
| 32 | 622–632 | Observation | 118215003 | Delivery finding | _Observasi dalam Persalinan_ → `Observation.valueString` (625, tanpa BQ) |
| 33 | 633–643 | Observation | 93857-1 | Date and time of obstetric delivery | _Tanggal dan Jam Persalinan_ → `Observation.valueDateTime` (636, tanpa BQ) |
| 34 | 644–663 | Observation | OC000013 | Penolong Persalinan | _Penolong Persalinan_ → `Observation.valueCodeableConcept.coding` (647, tanpa BQ)<br>_Nama Penolong Persalinan_ → `Observation.valueCodeableConcept.text` (656, tanpa BQ) |
| 35 | 664–677 | Observation | 57071-3 | Obstetric delivery method | _Cara Persalinan_ → `Observation.valueCodeableConcept.coding` (667, tanpa BQ) |
| 36 | 678–697 | Observation | 405195003 | Intrapartum maternal status | _Keadaan Ibu_ → `Observation.valueCodeableConcept.coding` (681, tanpa BQ) |
| 37 | 698–718 | Observation | 387700009 | Prolonged latent phase of labor | _Kala I laten_ → `Observation.valueDateTime` (701, tanpa BQ) |
| 38 | 719–739 | Observation | 249120008 | Onset of labor first stage | _Kala I Aktif_ → `Observation.valueDateTime` (722, tanpa BQ) |
| 39 | 740–750 | Observation | 249160009 | Onset of labor second stage | _Kala II_ → `Observation.valueDateTime` (743, tanpa BQ) |
| 40 | 751–761 | Observation | OC000018 | Onset Kala III | _Kala III_ → `Observation.valueDateTime` (754, tanpa BQ) |
| 41 | 762–772 | Observation | 236994008 | Placental delivery procedure | _Plasenta lahir_ → `Observation.valueDateTime` (765, tanpa BQ) |
| 42 | 773–784 | Observation | 289267004 | Finding of completeness of placenta | _Kondisi Plasenta_ → `Observation.valueCodeableConcept.coding` (776, tanpa BQ) |
| 43 | 785–795 | Procedure | SP000127 | Injeksi Oksitosin | _Injeksi Oksitosin_ → `Procedure.category.coding` (785, tanpa BQ) |
| 44 | 796–806 | Procedure | 302384005 | Controlled cord traction of placenta | _Peregangan Tali Pusat_ → `Procedure.category.coding` (796, tanpa BQ) |
| 45 | 807–817 | Procedure | 236996005 | Abdominal uterine fundal massage | _Masase Fundus Uteri_ → `Procedure.category.coding` (807, tanpa BQ) |
| 46 | 818–828 | Observation | OC000019 | Onset Kala IV | _Kala IV_ → `Observation.valueDateTime` (821, tanpa BQ) |
| 47 | 829–842 | Condition | 9293002 | Atony of uterus | _Kondisi Kala 4_ → `Condition.clinicalStatus.coding` (829, tanpa BQ) |
| 48 | 843–855 | Observation | 719051004 | Quantity of postpartum maternal blood loss | _Jumlah Pendarahan Kala 4_ → `Observation.valueQuantity.value` (846, tanpa BQ) |
| 49 | 856–868 | Observation | 717809003 | Immediate postpartum care | _Sistol Kala 4_ → `Observation.valueQuantity.value` (859, tanpa BQ) |
| 50 | 869–881 | Observation | 8462-4 | Diastolic blood pressure | _Diastol Kala 4_ → `Observation.valueQuantity.value` (872, tanpa BQ) |
| 51 | 882–894 | Procedure | 717809003 | Immediate postpartum care | _Pemantauan Kala 4_ → `Procedure.category.coding` (882, tanpa BQ) |
| 52 | 895–915 | Condition | 199746004 | Obstructed labor | _Komplikasi Persalinan_ → `Condition.clinicalStatus.coding` (895, tanpa BQ) |
| 53 | 916–926 | Observation | SP000379 | Tatalaksana Komplikasi Persalinan | _Tatalaksana Komplikasi Persalinan_ → `Observation.valueString` (919, tanpa BQ) |
| 54 | 927–942 | Observation | 63893-2 | Outcome of pregnancy | _Luaran Kehamilan_ → `Observation.valueCodeableConcept.coding` (930, tanpa BQ) |
| 55 | 943–964 | ServiceRequest | 409014006 | Delivery care management | _Rujuk_ → `ServiceRequest.status` (943, tanpa BQ)<br>_Faskes Rujukan_ → `ServiceRequest.locationCode.coding` (956, tanpa BQ)<br>_Nama Faskes Rujukan_ → `ServiceRequest.locationCode.text` (964, tanpa BQ) |
| 56 | 966–978 | Observation | SP000122 | Catat di Buku KIA | _Catat di buku KIA_ → `Observation.valueBoolean` (968, tanpa BQ) |
| 57 | 979–995 | Procedure | SP000130 | Menggunakan Partograf | _Pelayanan Menggunakan Partograf_ → `Procedure.category.coding` (979, tanpa BQ)<br>_Inisiasi Menyusu Dini (IMD)_ → `Procedure.category.coding` (991, tanpa BQ) |
| 58 | 996–1003 | Procedure | 431868002 | Initiation of breastfeeding | – |
| 59 | 1004–1015 | Observation | OC000016 | Waktu Inisiasi Menyusui Dini | _Waktu Inisiasi Menyusu Dini (IMD)_ → `Observation.valueCodeableConcept.coding` (1006, tanpa BQ) |
| 60 | 1016–1018 | Procedure | 409063005 | Counselling | _Konseling_ → `Procedure.category.coding` (1016, tanpa BQ) |
| 61 | 1019–1033 | Procedure | 409063005 | Counselling | – |
| 62 | 1034–1046 | Observation | – | – | _Apakah Ibu pernah melakukan pemeriksaan kehamilan ke Faskes?_ → `Observation.valueCodeableConcept.coding` (1036, tanpa BQ) |
| 63 | 1047–1060 | Observation | 365662002 | Finding of amniotic fluid appearance | _Warna Ketuban_ → `Observation.valueCodeableConcept.coding` (1049, tanpa BQ) |
| 64 | 1061–1070 | Observation | 81956-5 | Date and time of death [TimeStamp] | _Tanggal dan Jam Kematian Ibu_ → `Observation.valueDateTime` (1064, tanpa BQ) |
| 65 | 1075–1085 | Observation | 57715-5 | Birth time | _Jam Lahir_ → `Observation.valueTime` (1078, tanpa BQ) |
| 66 | 1086–1099 | Observation | 883-9 | ABO group [Type] in Blood | _Golongan darah bayi_ → `Observation.valueCodeableConcept.coding` (1089, tanpa BQ) |
| 67 | 1100–1111 | Observation | 8339-4 | Birth weight Measured | _Berat badan saat lahir_ → `Observation.valueQuantity.value` (1103, tanpa BQ) |
| 68 | 1112–1122 | Procedure | SP000126 | ARV Profilaksis | _ARV Profilaksis pada bayi baru lahir_ → `Procedure.category.coding` (1112, tanpa BQ) |
| 69 | 1123–1135 | Observation | 249222005 | Neonatal condition | _Keadaan bayi_ → `Observation.valueCodeableConcept.coding` (1126, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 49 |
| Procedure | 9 |
| Condition | 3 |
| Patient | 1 |
| RelatedPerson | 1 |
| PractitionerRole | 1 |
| Practitioner | 1 |
| EpisodeOfCare | 1 |
| Encounter | 1 |
| QuestionnaireResponse | 1 |
| ServiceRequest | 1 |
| **Total** | **69** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 90 | PractitionerRole | `PractitionerRole.code.coding` | 309453006 | Registered midwife | http://snomed.info/sct |
| 2 | 91 | PractitionerRole | `PractitionerRole.code.coding` | 309343006 | Physician | http://snomed.info/sct |
| 3 | 92 | PractitionerRole | `PractitionerRole.code.coding` | 309367003 | Obstetrician and gynecologist | http://snomed.info/sct |
| 4 | 93 | PractitionerRole | `PractitionerRole.code.coding` | 224535009 | Registered nurse | http://snomed.info/sct |
| 5 | 124 | EpisodeOfCare | `EpisodeOfCare.type.coding` | ANC | Antenatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 6 | 149 | Condition | `Condition.code.coding` | 386337006 | Intrapartal care | http://snomed.info/sct |
| 7 | 166 | Encounter | `Encounter.hospitalization.admitSource.coding` | EHA000002 | Datang sendiri | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 8 | 167 | Encounter | `Encounter.hospitalization.admitSource.coding` | 305956004 | Referral by physician | http://snomed.info/sct |
| 9 | 168 | Encounter | `Encounter.hospitalization.admitSource.coding` | 306052007 | Referral by midwife | http://snomed.info/sct |
| 10 | 169 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000116 | Rujukan dari Puskesmas Pembantu | http://terminology.kemkes.go.id/sp |
| 11 | 170 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000117 | Rujukan dari Puskesmas | http://terminology.kemkes.go.id/sp |
| 12 | 171 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000118 | Rujukan dari Rumah Bersalin / Klinik | http://terminology.kemkes.go.id/sp |
| 13 | 172 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000119 | Rujukan dari Rumah Sakit | http://terminology.kemkes.go.id/sp |
| 14 | 173 | Encounter | `Encounter.hospitalization.admitSource.coding` | 185389009 | Follow-up visit | http://snomed.info/sct |
| 15 | 179 | Observation | `Observation.code.coding` | SP000131 | Status Pindahan | http://terminology.kemkes.go.id/sp |
| 16 | 191 | Observation | `Observation.code.coding` | 30525-0 | Age | http://loinc.org |
| 17 | 203 | Observation | `Observation.code.coding` | SP000383 | Keadaan Ibu Saat Tiba | http://terminology.kemkes.go.id/sp |
| 18 | 204 | Observation | `Observation.valueCodeableConcept.coding` | 438949009 | Alive | http://snomed.info/sct |
| 19 | 205 | Observation | `Observation.valueCodeableConcept.coding` | 419099009 | Dead | http://snomed.info/sct |
| 20 | 215 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 21 | 227 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://loinc.org |
| 22 | 239 | Observation | `Observation.code.coding` | 8867-4 | Heart rate | http://loinc.org |
| 23 | 252 | Observation | `Observation.code.coding` | 9279-1 | Respiratory rate | http://loinc.org |
| 24 | 278 | Observation | `Observation.code.coding` | 284473002 | Mid upper arm circumference | http://snomed.info/sct |
| 25 | 290 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 26 | 302 | Observation | `Observation.code.coding` | 8302-2 | Body height | http://loinc.org |
| 27 | 314 | Observation | `Observation.code.coding` | OC000001 | Jarak kehamilan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 28 | 315 | Observation | `Observation.code.coding` | ANC.SS.DE53 | Jarak kehamilan | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 29 | 327 | Observation | `Observation.code.coding` | 11881-0 | Uterus Fundal height Tape measure | http://loinc.org |
| 30 | 340 | Observation | `Observation.code.coding` | 55283-6 | Fetal Heart rate | http://loinc.org |
| 31 | 353 | Observation | `Observation.code.coding` | 289437007 | Finding of fetal heart rate | http://snomed.info/sct |
| 32 | 354 | Observation | `Observation.valueCodeableConcept.coding` | 289441006 | Normal fetal heart rate | http://snomed.info/sct |
| 33 | 355 | Observation | `Observation.valueCodeableConcept.coding` | 289440007 | Fetal heart rate not observed | http://snomed.info/sct |
| 34 | 356 | Observation | `Observation.valueCodeableConcept.coding` | 312668007 | Abnormal fetal heart rate | http://snomed.info/sct |
| 35 | 357 | Observation | `Observation.valueCodeableConcept.coding` | 289439005 | Fetal heart rate absent | http://snomed.info/sct |
| 36 | 368 | Observation | `Observation.code.coding` | 271692001 | Presentation of fetus | http://snomed.info/sct |
| 37 | 370 | Observation | `Observation.valueCodeableConcept.coding` | 398236008 | Intrauterine | http://snomed.info/sct |
| 38 | 371 | Observation | `Observation.valueCodeableConcept.coding` | 298109001 | Ectopic | http://snomed.info/sct |
| 39 | 382 | Observation | `Observation.code.coding` | 72155-5 | Position in womb Fetus [RHEA] | http://loinc.org |
| 40 | 384 | Observation | `Observation.valueCodeableConcept.coding` | 1209182005 | Cephalic fetal presentation | http://snomed.info/sct |
| 41 | 385 | Observation | `Observation.valueCodeableConcept.coding` | 6096002 | Breech presentation | http://snomed.info/sct |
| 42 | 386 | Observation | `Observation.valueCodeableConcept.coding` | 288203005 | Transverse/oblique lie | http://snomed.info/sct |
| 43 | 387 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 44 | 388 | Observation | `Observation.valueCodeableConcept.coding` | 70028003 | Vertex presentation | http://snomed.info/sct |
| 45 | 389 | Observation | `Observation.valueCodeableConcept.coding` | 249083005 | Posterior fontanelle presenting | http://snomed.info/sct |
| 46 | 390 | Observation | `Observation.valueCodeableConcept.coding` | 288203005 | Transverse/oblique lie | http://snomed.info/sct |
| 47 | 391 | Observation | `Observation.valueCodeableConcept.coding` | 23954006 | Acromion presentation | http://snomed.info/sct |
| 48 | 392 | Observation | `Observation.valueCodeableConcept.coding` | 6096002 | Breech presentation | http://snomed.info/sct |
| 49 | 393 | Observation | `Observation.valueCodeableConcept.coding` | 8014007 | Brow presentation of fetus | http://snomed.info/sct |
| 50 | 394 | Observation | `Observation.valueCodeableConcept.coding` | 8017000 | Face presentation | http://snomed.info/sct |
| 51 | 395 | Observation | `Observation.valueCodeableConcept.coding` | 249097002 | Footling breech presentation | http://snomed.info/sct |
| 52 | 396 | Observation | `Observation.valueCodeableConcept.coding` | 124736009 | Compound presentation | http://snomed.info/sct |
| 53 | 407 | Observation | `Observation.code.coding` | 249111004 | Engagement of head | http://snomed.info/sct |
| 54 | 408 | Observation | `Observation.valueCodeableConcept.coding` | 249112006 | Head engaged | http://snomed.info/sct |
| 55 | 409 | Observation | `Observation.valueCodeableConcept.coding` | 62098001 | Head not engaged | http://snomed.info/sct |
| 56 | 421 | Observation | `Observation.code.coding` | 289282009 | Amniotic membrane finding | http://snomed.info/sct |
| 57 | 422 | Observation | `Observation.valueCodeableConcept.coding` | 249125003 | Intact membranes | http://snomed.info/sct |
| 58 | 423 | Observation | `Observation.valueCodeableConcept.coding` | SP000120 | Non-intact membrane | http://snomed.info/sct |
| 59 | 540 | Observation | `Observation.code.coding` | SP000123 | Integrasi Program | http://terminology.kemkes.go.id/sp |
| 60 | 541 | Observation | `Observation.valueCodeableConcept.coding` | SP000046 | Terapi Antiretroviral (ART) | http://terminology.kemkes.go.id/sp |
| 61 | 542 | Observation | `Observation.valueCodeableConcept.coding` | SP000124 | Obat anti malaria | http://terminology.kemkes.go.id/sp |
| 62 | 543 | Observation | `Observation.valueCodeableConcept.coding` | SP000125 | Obar anti hepatitis B | http://terminology.kemkes.go.id/sp |
| 63 | 553 | Observation | `Observation.code.coding` | 72150-6 | Delivery location | http://loinc.org |
| 64 | 554 | Observation | `Observation.valueCodeableConcept.coding` | 264362003 | Home | http://snomed.info/sct |
| 65 | 555 | Observation | `Observation.valueCodeableConcept.coding` | OT000001 | Polindes | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 66 | 556 | Observation | `Observation.valueCodeableConcept.coding` | OT000002 | Pustu | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 67 | 557 | Observation | `Observation.valueCodeableConcept.coding` | 102 | Pusat Kesehatan Masyarakat | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 68 | 558 | Observation | `Observation.valueCodeableConcept.coding` | 103 | Klinik | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 69 | 559 | Observation | `Observation.valueCodeableConcept.coding` | OT000008 | Rumah Bersalin | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 70 | 560 | Observation | `Observation.valueCodeableConcept.coding` | 82242000 | Children’s hospital | http://snomed.info/sct |
| 71 | 561 | Observation | `Observation.valueCodeableConcept.coding` | 104 | Rumah Sakit | hhttp://terminology.kemkes.go.id/CodeSystem/organization-type |
| 72 | 562 | Observation | `Observation.valueCodeableConcept.coding` | OT000003 | RS ODHA | hhttp://terminology.kemkes.go.id/CodeSystem/organization-type |
| 73 | 563 | Observation | `Observation.valueCodeableConcept.coding` | OT000004 | Bidan Praktek Mandiri | hhttp://terminology.kemkes.go.id/CodeSystem/organization-type |
| 74 | 564 | Observation | `Observation.valueCodeableConcept.coding` | LT000008 | Dalam perjalanan dari rumah/masyarakat | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 75 | 565 | Observation | `Observation.valueCodeableConcept.coding` | LT000009 | Dalam perjalanan ke faskes lain | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 76 | 566 | Observation | `Observation.valueCodeableConcept.coding` | OT000006 | Rumah Sakit Pemerintah | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 77 | 567 | Observation | `Observation.valueCodeableConcept.coding` | OT000007 | Rumah Sakit Swasta | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 78 | 568 | Observation | `Observation.valueCodeableConcept.coding` | LT000006 | Rumah Ibu | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 79 | 569 | Observation | `Observation.valueCodeableConcept.coding` | OT000010 | Klinik Medis Utama | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 80 | 570 | Observation | `Observation.valueCodeableConcept.coding` | OT000011 | Klinik Medis Pratama | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 81 | 571 | Observation | `Observation.valueCodeableConcept.coding` | 101 | Tempat Praktik Mandiri Tenaga Kesehatan | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 82 | 572 | Observation | `Observation.valueCodeableConcept.coding` | 394573001 | Maternity clinic | http://snomed.info/sct |
| 83 | 573 | Observation | `Observation.valueCodeableConcept.coding` | LT000007 | Rumah Dukun | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 84 | 574 | Observation | `Observation.valueCodeableConcept.coding` | LT000010 | Lainnya | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 85 | 575 | Observation | `Observation.valueCodeableConcept.coding` | LT000011 | Belum Tahu | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 86 | 600 | Observation | `Observation.code.coding` | 18185-9 | Gestational age | http://loinc.org |
| 87 | 612 | Observation | `Observation.code.coding` | 76516-4 | Gestational age—​at birth | http://loinc.org |
| 88 | 624 | Observation | `Observation.code.coding` | 118215003 | Delivery finding | http://snomed.info/sct |
| 89 | 635 | Observation | `Observation.code.coding` | 93857-1 | Date and time of obstetric delivery | http://loinc.org |
| 90 | 646 | Observation | `Observation.code.coding` | OC000013 | Penolong Persalinan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 91 | 647 | Observation | `Observation.valueCodeableConcept.coding` | 303071001 | Person in the family | http://snomed.info/sct |
| 92 | 648 | Observation | `Observation.valueCodeableConcept.coding` | OV000012 | Dukun | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 93 | 649 | Observation | `Observation.valueCodeableConcept.coding` | 309453006 | Registered midwife | http://snomed.info/sct |
| 94 | 650 | Observation | `Observation.valueCodeableConcept.coding` | 309343006 | Physician | http://snomed.info/sct |
| 95 | 651 | Observation | `Observation.valueCodeableConcept.coding` | 11935004 | Obstetrician | http://snomed.info/sct |
| 96 | 652 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 97 | 653 | Observation | `Observation.valueCodeableConcept.coding` | 125677006 | Relative | http://snomed.info/sct |
| 98 | 654 | Observation | `Observation.valueCodeableConcept.coding` | 106292003 | Professional nurse | http://snomed.info/sct |
| 99 | 655 | Observation | `Observation.valueCodeableConcept.coding` | 257514003 | Member of public involved incidentally | http://snomed.info/sct |
| 100 | 666 | Observation | `Observation.code.coding` | 57071-3 | Obstetric delivery method | http://loinc.org |
| 101 | 667 | Observation | `Observation.valueCodeableConcept.coding` | 48782003 | Delivery normal | http://snomed.info/sct |
| 102 | 668 | Observation | `Observation.valueCodeableConcept.coding` | 200138003 | Vacuum extractor delivery - delivered | http://snomed.info/sct |
| 103 | 669 | Observation | `Observation.valueCodeableConcept.coding` | 200130005 | Forceps delivery - delivered | http://snomed.info/sct |
| 104 | 670 | Observation | `Observation.valueCodeableConcept.coding` | 200144004 | Deliveries by cesarean | http://snomed.info/sct |
| 105 | 680 | Observation | `Observation.code.coding` | 405195003 | Intrapartum maternal status | http://snomed.info/sct |
| 106 | 681 | Observation | `Observation.valueCodeableConcept.coding` | 102514002 | Well female adult | http://snomed.info/sct |
| 107 | 682 | Observation | `Observation.valueCodeableConcept.coding` | 39104002 | Illness | http://snomed.info/sct |
| 108 | 683 | Observation | `Observation.valueCodeableConcept.coding` | 131148009 | Bleeding | http://snomed.info/sct |
| 109 | 684 | Observation | `Observation.valueCodeableConcept.coding` | 386661006 | Fever | http://snomed.info/sct |
| 110 | 685 | Observation | `Observation.valueCodeableConcept.coding` | 91175000 | Seizure | http://snomed.info/sct |
| 111 | 686 | Observation | `Observation.valueCodeableConcept.coding` | 249215002 | Odor of lochia | http://snomed.info/sct |
| 112 | 687 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 113 | 688 | Observation | `Observation.valueCodeableConcept.coding` | 59283008 | Maternal death | http://snomed.info/sct |
| 114 | 689 | Observation | `Observation.valueCodeableConcept.coding` | 438949009 | Alive | http://snomed.info/sct |
| 115 | 690 | Observation | `Observation.valueCodeableConcept.coding` | 419099009 | Dead | http://snomed.info/sct |
| 116 | 700 | Observation | `Observation.code.coding` | 387700009 | Prolonged latent phase of labor | http://snomed.info/sct |
| 117 | 709 | Observation | `Observation.component.code.coding` | 398143009 | Uterine contraction monitoring | http://snomed.info/sct |
| 118 | 710 | Observation | `Observation.component.valueCodeableConcept.coding` | 289708007 | Regular uterine contractions | http://snomed.info/sct |
| 119 | 711 | Observation | `Observation.component.valueCodeableConcept.coding` | 289739009 | Uterine contractions problem | http://snomed.info/sct |
| 120 | 712 | Observation | `Observation.component.code.coding` | 364270005 | Frequency of uterine contraction | http://snomed.info/sct |
| 121 | 715 | Observation | `Observation.component.code.coding` | 364274001 | Duration of uterine contraction | http://snomed.info/sct |
| 122 | 716 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000399 | <20 detik | http://terminology.kemkes.go.id/sp |
| 123 | 717 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000400 | 20-40 detik | http://terminology.kemkes.go.id/sp |
| 124 | 718 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000401 | >40 detik | http://terminology.kemkes.go.id/sp |
| 125 | 721 | Observation | `Observation.code.coding` | 249120008 | Onset of labor first stage | http://snomed.info/sct |
| 126 | 730 | Observation | `Observation.component.code.coding` | 398143009 | Uterine contraction monitoring | http://snomed.info/sct |
| 127 | 731 | Observation | `Observation.component.valueCodeableConcept.coding` | 289708007 | Regular uterine contractions | http://snomed.info/sct |
| 128 | 732 | Observation | `Observation.component.valueCodeableConcept.coding` | 289739009 | Uterine contractions problem | http://snomed.info/sct |
| 129 | 733 | Observation | `Observation.component.code.coding` | 364270005 | Frequency of uterine contraction | http://snomed.info/sct |
| 130 | 736 | Observation | `Observation.component.code.coding` | 364274001 | Duration of uterine contraction | http://snomed.info/sct |
| 131 | 737 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000399 | <20 detik | http://terminology.kemkes.go.id/sp |
| 132 | 738 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000400 | 20-40 detik | http://terminology.kemkes.go.id/sp |
| 133 | 739 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000401 | >40 detik | http://terminology.kemkes.go.id/sp |
| 134 | 742 | Observation | `Observation.code.coding` | 249160009 | Onset of labor second stage | http://snomed.info/sct |
| 135 | 753 | Observation | `Observation.code.coding` | OC000018 | Onset Kala III | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 136 | 764 | Observation | `Observation.code.coding` | 236994008 | Placental delivery procedure | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 137 | 775 | Observation | `Observation.code.coding` | 289267004 | Finding of completeness of placenta | http://snomed.info/sct |
| 138 | 776 | Observation | `Observation.valueCodeableConcept.coding` | 249170006 | Complete placenta at delivery | http://snomed.info/sct |
| 139 | 777 | Observation | `Observation.valueCodeableConcept.coding` | 268479002 | Incomplete placenta at delivery | http://snomed.info/sct |
| 140 | 787 | Procedure | `Procedure.code.coding` | SP000127 | Injeksi Oksitosin | http://terminology.kemkes.go.id/sp |
| 141 | 798 | Procedure | `Procedure.code.coding` | 302384005 | Controlled cord traction of placenta | http://snomed.info/sct |
| 142 | 809 | Procedure | `Procedure.code.coding` | 236996005 | Abdominal uterine fundal massage | http://snomed.info/sct |
| 143 | 820 | Observation | `Observation.code.coding` | OC000019 | Onset Kala IV | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 144 | 831 | Condition | `Condition.code.coding` | 9293002 | Atony of uterus | http://snomed.info/sct |
| 145 | 832 | Condition | `Condition.code.coding` | 48194001 | Postpartum hemorrhage | http://snomed.info/sct |
| 146 | 833 | Condition | `Condition.code.coding` | 1148943004 | Retention of placenta and uterine membrane | http://snomed.info/sct |
| 147 | 834 | Condition | `Condition.code.coding` | 283380005 | Laceration of perineum | http://snomed.info/sct |
| 148 | 835 | Condition | `Condition.code.coding` | 84007008 | Shock during AND/OR following labor AND/OR delivery | http://snomed.info/sct |
| 149 | 836 | Condition | `Condition.code.coding` | 118216002 | Labor finding | http://snomed.info/sct |
| 150 | 845 | Observation | `Observation.code.coding` | 719051004 | Quantity of postpartum maternal blood loss | http://snomed.info/sct |
| 151 | 858 | Observation | `Observation.code.coding` | 717809003 | Immediate postpartum care | http://snomed.info/sct |
| 152 | 871 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://snomed.info/sct |
| 153 | 885 | Procedure | `Procedure.code.coding` | 717809003 | Immediate postpartum care | http://snomed.info/sct |
| 154 | 897 | Condition | `Condition.code.coding` | 199746004 | Obstructed labor | http://snomed.info/sct |
| 155 | 898 | Condition | `Condition.code.coding` | 48194001 | Pregnancy-induced hypertension | http://snomed.info/sct |
| 156 | 899 | Condition | `Condition.code.coding` | 38010008 | Intrapartum hemorrhage | http://snomed.info/sct |
| 157 | 900 | Condition | `Condition.code.coding` | 40733004 | Infectious disease | http://snomed.info/sct |
| 158 | 901 | Condition | `Condition.code.coding` | 386639001 | Termination of pregnancy | http://snomed.info/sct |
| 159 | 902 | Condition | `Condition.code.coding` | 44223004 | Premature rupture of membranes | http://snomed.info/sct |
| 160 | 903 | Condition | `Condition.code.coding` | 199745000 | Complication occurring during labor and delivery | http://snomed.info/sct |
| 161 | 904 | Condition | `Condition.code.coding` | 38010008 | Intrapartum hemorrhage | http://snomed.info/sct |
| 162 | 905 | Condition | `Condition.code.coding` | 38341003 | Hypertensive disorder, systemic arterial | http://snomed.info/sct |
| 163 | 906 | Condition | `Condition.code.coding` | 398254007 | Pre-eclampsia | http://snomed.info/sct |
| 164 | 907 | Condition | `Condition.code.coding` | 15938005 | Eclampsia | http://snomed.info/sct |
| 165 | 908 | Condition | `Condition.code.coding` | 9293002 | Atony of uterus | http://snomed.info/sct |
| 166 | 909 | Condition | `Condition.code.coding` | 199745000 | Complication occurring during labor and delivery | http://snomed.info/sct |
| 167 | 918 | Observation | `Observation.code.coding` | SP000379 | Tatalaksana Komplikasi Persalinan | http://terminology.kemkes.go.id/sp |
| 168 | 929 | Observation | `Observation.code.coding` | 63893-2 | Outcome of pregnancy | http://loinc.org |
| 169 | 930 | Observation | `Observation.valueCodeableConcept.coding` | LA14270-5 | Live birth | http://loinc.org |
| 170 | 931 | Observation | `Observation.valueCodeableConcept.coding` | LA14271-3 | Stillborn | http://loinc.org |
| 171 | 932 | Observation | `Observation.valueCodeableConcept.coding` | LA14270-5 | Live birth | http://loinc.org |
| 172 | 933 | Observation | `Observation.valueCodeableConcept.coding` | LA14271-3 | Stillborn | http://loinc.org |
| 173 | 934 | Observation | `Observation.valueCodeableConcept.coding` | LA14272-1 | Miscarriage | http://loinc.org |
| 174 | 935 | Observation | `Observation.valueCodeableConcept.coding` | LA14273-9 | Induced abortion | http://loinc.org |
| 175 | 947 | ServiceRequest | `ServiceRequest.code.coding` | 409014006 | Delivery care management | http://snomed.info/sct |
| 176 | 967 | Observation | `Observation.code.coding` | SP000122 | Catat di Buku KIA | http://terminology.kemkes.go.id/sp |
| 177 | 982 | Procedure | `Procedure.code.coding` | SP000130 | Menggunakan Partograf | http://terminology.kemkes.go.id/sp |
| 178 | 996 | Procedure | `Procedure.code.coding` | 431868002 | Initiation of breastfeeding | http://snomed.info/sct |
| 179 | 1005 | Observation | `Observation.code.coding` | OC000016 | Waktu Inisiasi Menyusui Dini | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 180 | 1006 | Observation | `Observation.valueCodeableConcept.coding` | OV000014 | Kurang dari 1 Jam | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 181 | 1007 | Observation | `Observation.valueCodeableConcept.coding` | OV000015 | Lebih dari 1 Jam | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 182 | 1018 | Procedure | `Procedure.code.coding` | 409063005 | Counselling | http://snomed.info/sct |
| 183 | 1020 | Procedure | `Procedure.code.coding` | 409063005 | Counselling | http://snomed.info/sct |
| 184 | 1021 | Procedure | `Procedure.code.coding` | ED000008 | Edukasi Tanda Bahaya Kehamilan, Bersalin dan Nifas | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 185 | 1022 | Procedure | `Procedure.code.coding` | SP000121 | Edukasi Tanda Bahaya Baru Lahir | http://terminology.kemkes.go.id/sp |
| 186 | 1023 | Procedure | `Procedure.code.coding` | ED000009 | Edukasi IMD dan ASI Eksklusif | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 187 | 1024 | Procedure | `Procedure.code.coding` | ED000005 | Edukasi Gizi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 188 | 1025 | Procedure | `Procedure.code.coding` | PC000001 | Perawatan Tali Pusat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 189 | 1026 | Procedure | `Procedure.code.coding` | ED000010 | Edukasi PHBS | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 190 | 1048 | Observation | `Observation.code.coding` | 365662002 | Finding of amniotic fluid appearance | http://snomed.info/sct |
| 191 | 1049 | Observation | `Observation.valueCodeableConcept.coding` | 168090003 | Amniotic fluid clear | http://snomed.info/sct |
| 192 | 1050 | Observation | `Observation.valueCodeableConcept.coding` | 408781009 | Straw colored amniotic fluid | http://snomed.info/sct |
| 193 | 1051 | Observation | `Observation.valueCodeableConcept.coding` | 249134008 | Bloodstained liquor | http://snomed.info/sct |
| 194 | 1052 | Observation | `Observation.valueCodeableConcept.coding` | 168092006 | Amniotic fluid -meconium stain | http://snomed.info/sct |
| 195 | 1063 | Observation | `Observation.code.coding` | 81956-5 | Date and time of death [TimeStamp] | http://loinc.org |
| 196 | 1077 | Observation | `Observation.code.coding` | 57715-5 | Birth time | http://loinc.org |
| 197 | 1088 | Observation | `Observation.code.coding` | 883-9 | ABO group [Type] in Blood | http://loinc.org |
| 198 | 1089 | Observation | `Observation.valueCodeableConcept.coding` | LA19710-5 | Group A | http://loinc.org |
| 199 | 1090 | Observation | `Observation.valueCodeableConcept.coding` | LA19709-7 | Group B | http://loinc.org |
| 200 | 1091 | Observation | `Observation.valueCodeableConcept.coding` | LA19708-9 | Group O | http://loinc.org |
| 201 | 1092 | Observation | `Observation.valueCodeableConcept.coding` | LA28449-9 | Group AB | http://loinc.org |
| 202 | 1102 | Observation | `Observation.code.coding` | 8339-4 | Birth weight Measured | http://loinc.org |
| 203 | 1115 | Procedure | `Procedure.code.coding` | SP000126 | ARV Profilaksis | http://terminology.kemkes.go.id/sp |
| 204 | 1125 | Observation | `Observation.code.coding` | 249222005 | Neonatal condition | http://snomed.info/sct |
| 205 | 1126 | Observation | `Observation.valueCodeableConcept.coding` | 438949009 | Alive | http://snomed.info/sct |
| 206 | 1127 | Observation | `Observation.valueCodeableConcept.coding` | 419099009 | Dead | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 118 |
| http://loinc.org | 30 |
| http://terminology.kemkes.go.id/sp | 22 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 15 |
| http://terminology.kemkes.go.id/CodeSystem/organization-type | 10 |
| http://terminology.kemkes.go.id/CodeSystem/location-type | 6 |
| hhttp://terminology.kemkes.go.id/CodeSystem/organization-type | 3 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 1 |
| http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes | 1 |
| **Total** | **206** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 44 | – | Jenis Faskes | Organization | `Organization.type` |
| 48 | – | Nama Faskes INC | Organization | `Organization.name` |
| 64 | – | Gedung Faskes | Location | `Location.identifier` |
| 583 | – | Alamat Bersalin | Location | `Location.type.coding` |
