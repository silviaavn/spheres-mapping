# Output Form: SIM RS Siaga Medika INC

Sumber: `mapping/phdt-data-dictionary-rs-siaga-medika-inc.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-rs-siaga-medika-inc.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 42 |
| Code (`jumlah code` = 1) | 125 |
| Code unik (code + CodeSystem) | 125 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 13 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–33 | Patient | – | – | _Nama Pasien_ → `Patient.name.text` (2, tanpa BQ)<br>_NIK Pasien_ → `Patient.identifier.value` (6, tanpa BQ)<br>_No HP Pasien_ → `Patient.telecom` (7, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (10, tanpa BQ)<br>_Tempat Lahir_ → `Patient.extension:birthPlace.valueAddress.text` (11, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (12, tanpa BQ)<br>_Alamat_ → `Patient.address.line` (13, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (18, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (21, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.extension.valueCode` (24, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.extension.valueCode` (27, tanpa BQ)<br>_RW_ → `Patient.address.extension.extension.valueCode` (30, tanpa BQ)<br>_RT_ → `Patient.address.extension.extension.valueCode` (33, tanpa BQ) |
| 2 | 76–96 | Practitioner | – | – | _Nama Pemeriksa_ → `Practitioner.name.text` (78, tanpa BQ)<br>_Jenis Kelamin Nakes_ → `Practitioner.gender` (79, tanpa BQ) |
| 3 | 97–103 | RelatedPerson | – | – | _Nama Suami_ → `RelatedPerson.patient` (97, tanpa BQ)<br>_NIK Suami_ → `RelatedPerson.identifier` (101, tanpa BQ) |
| 4 | 104–127 | EpisodeOfCare | ANC | Antenatal Care | _Episode ANC Ibu_ → `EpisodeOfCare.identifier` (104, tanpa BQ)<br>_HPHT_ → `EpisodeOfCare.period.start` (107, tanpa BQ)<br>_Tanggal Persalinan_ → `EpisodeOfCare.period.end` (110, tanpa BQ)<br>_HPHT_ → `EpisodeOfCare.statusHistory.period.start` (112, tanpa BQ)<br>_Tanggal Persalinan_ → `EpisodeOfCare.statusHistory.period.end` (115, tanpa BQ)<br>_Tanggal Persalinan_ → `EpisodeOfCare.statusHistory.period.start` (119, tanpa BQ)<br>_Tanggal Persalinan_ → `EpisodeOfCare.statusHistory.period.end` (122, tanpa BQ)<br>_Episode PNC Ibu_ → `EpisodeOfCare.identifier` (127, tanpa BQ) |
| 5 | 128–140 | EpisodeOfCare | PNC | Postnatal Care | _Tanggal Persalinan_ → `EpisodeOfCare.period.start` (132, tanpa BQ)<br>_Tanggal Persalinan_ → `EpisodeOfCare.statusHistory.period.start` (136, tanpa BQ) |
| 6 | 141–158 | Encounter | – | – | _Tanggal Masuk_ → `Encounter.period.start` (151, tanpa BQ)<br>_Cara Masuk RS_ → `Encounter.hospitalization.admitSource.coding` (184, tanpa BQ)<br>_Cara Masuk RS_ → `Encounter.hospitalization.admitSource.coding` (185, tanpa BQ)<br>_Cara Masuk RS_ → `Encounter.hospitalization.admitSource.coding` (186, tanpa BQ) |
| 7 | 159–166 | Condition | 386337006.0 | Intrapartal care | _Diagnosis Masuk_ → `Condition.clinicalStatus.coding` (159, tanpa BQ) |
| 8 | 189–200 | Observation | SP000383 | Keadaan Ibu Saat Tiba | _Kondisi Ibu Saat Masuk RS_ → `Observation.valueCodeableConcept.coding` (192, tanpa BQ) |
| 9 | 201–211 | Observation | 8665-2 | Last menstrual period start date | _HPHT_ → `Observation.valueDateTime` (204, tanpa BQ) |
| 10 | 212–222 | Observation | 11778-8 | Delivery date Estimated | _HPL_ → `Observation.valueDateTime` (215, tanpa BQ) |
| 11 | 223–237 | Observation | 18185-9 | Gestational age | _Usia Kehamilan_ → `Observation.valueQuantity.value` (226, tanpa BQ) |
| 12 | 238–248 | Observation | 11996-6 | [#] Pregnancies | _Gravida_ → `Observation.valueInteger` (241, tanpa BQ) |
| 13 | 249–259 | Observation | 11977-6 | [#] Parity | _Partus_ → `Observation.valueInteger` (252, tanpa BQ) |
| 14 | 260–270 | Observation | 69043-8 | Other pregnancy outcomes # | _Abortus_ → `Observation.valueInteger` (263, tanpa BQ) |
| 15 | 271–282 | Observation | 8480-6 | Systolic blood pressure | _Tekanan Darah Sistolik_ → `Observation.valueQuantity.value` (274, tanpa BQ) |
| 16 | 283–294 | Observation | 8462-4 | Diastolic blood pressure | _Tekanan Darah Diastolik_ → `Observation.valueQuantity.value` (286, tanpa BQ) |
| 17 | 295–307 | Observation | 8867-4 | Heart rate | _Nadi_ → `Observation.valueQuantity.value` (298, tanpa BQ) |
| 18 | 308–320 | Observation | 9279-1 | Respiratory rate | _Respiratory Rate_ → `Observation.valueQuantity.value` (311, tanpa BQ) |
| 19 | 321–332 | Observation | 8310-5 | Body temperature | _Suhu_ → `Observation.valueQuantity.value` (324, tanpa BQ) |
| 20 | 333–344 | Observation | 11881-0 | Uterus Fundal height Tape measure | _Tinggi Fundus_ → `Observation.valueQuantity.value` (336, tanpa BQ) |
| 21 | 345–355 | Observation | 81956-5 | Date and time of death [TimeStamp] | _Waktu Meninggal Jika Ibu Meninggal_ → `Observation.valueDateTime` (348, tanpa BQ) |
| 22 | 356–366 | Observation | 79378-6 | Cause of death | _Penyebab Kematian Jika Ibu Meninggal_ → `Observation.valueString` (359, tanpa BQ) |
| 23 | 367–378 | Observation | 55283-6 | Fetal Heart rate | _Denyut Jantung Janin_ → `Observation.valueQuantity.value` (370, tanpa BQ) |
| 24 | 379–390 | Observation | 271692001.0 | Presentation of fetus | _Letak Janin_ → `Observation.valueCodeableConcept.coding` (382, tanpa BQ) |
| 25 | 391–407 | Observation | 72155-5 | Position in womb Fetus [RHEA] | _Presentasi Janin_ → `Observation.valueCodeableConcept.coding` (394, tanpa BQ) |
| 26 | 408–419 | Observation | 249111004.0 | Engagement of head | _Posisi Kepala Terhadap PAP_ → `Observation.valueCodeableConcept.coding` (411, tanpa BQ) |
| 27 | 420–431 | Observation | 289282009.0 | Amniotic membrane finding | _Kondisi Ketuban_ → `Observation.valueCodeableConcept.coding` (423, tanpa BQ) |
| 28 | 432–443 | Observation | SP000686 | Faktor Risiko Persalinan | _Faktor Risiko Persalinan_ → `Observation.valueCodeableConcept.coding` (435, tanpa BQ) |
| 29 | 444–466 | Observation | 72150-6 | Delivery location | _Tempat Melahirkan_ → `Observation.valueCodeableConcept.coding` (447, tanpa BQ) |
| 30 | 467–479 | Observation | 93857-1 | Date and time of obstetric delivery | _Tanggal dan Jam Persalinan_ → `Observation.valueDateTime` (472, tanpa BQ) |
| 31 | 480–502 | Observation | OC000013 | Penolong Persalinan | _Penolong Persalinan_ → `Observation.valueCodeableConcept.coding` (483, tanpa BQ) |
| 32 | 503–520 | Observation | 57071-3 | Obstetric delivery method | _Cara Persalinan_ → `Observation.valueCodeableConcept.coding` (506, tanpa BQ) |
| 33 | 521–537 | Procedure | 73.59 | Other manually assisted delivery | _Prosedur Persalinan_ → `Procedure.status` (521, tanpa BQ) |
| 34 | 538–557 | Observation | 405195003.0 | Intrapartum maternal status | _Keadaan Ibu_ → `Observation.valueCodeableConcept.coding` (541, tanpa BQ) |
| 35 | 558–581 | Condition | 38341003.0 | Hypertensive disorder, systemic arterial | _Komplikasi Persalinan_ → `Condition.clinicalStatus.coding` (558, tanpa BQ) |
| 36 | 582–604 | Observation | SP000379 | Tatalaksana Komplikasi Persalinan | _Tatalaksana Komplikasi Persalinan_ → `Observation.valueCodeableConcept.coding` (585, tanpa BQ) |
| 37 | 605–622 | Observation | 63893-2 | Outcome of pregnancy | _Luaran Kehamilan_ → `Observation.valueCodeableConcept.coding` (608, tanpa BQ) |
| 38 | 623–637 | Procedure | SP000130 | Menggunakan Partograf | _Pelayanan Menggunakan Partograf_ → `Procedure.category.coding` (623, tanpa BQ) |
| 39 | 638–652 | Procedure | 431868002.0 | Initiation of breastfeeding | _Inisiasi Menyusu Dini_ → `Procedure.category.coding` (638, tanpa BQ) |
| 40 | 653–655 | Procedure | 409063005.0 | Counselling | _Konseling_ → `Procedure.category.coding` (653, tanpa BQ) |
| 41 | 656–673 | Procedure | ED000008 | Edukasi Tanda Bahaya Kehamilan, Bersalin dan Nifas | – |
| 42 | 674–691 | Observation | 365662002.0 | Finding of amniotic fluid appearance | _Warna Ketuban_ → `Observation.valueCodeableConcept.coding` (677, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 29 |
| Procedure | 5 |
| EpisodeOfCare | 2 |
| Condition | 2 |
| Patient | 1 |
| Practitioner | 1 |
| RelatedPerson | 1 |
| Encounter | 1 |
| **Total** | **42** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 105 | EpisodeOfCare | `EpisodeOfCare.type.coding` | ANC | Antenatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 2 | 128 | EpisodeOfCare | `EpisodeOfCare.type.coding` | PNC | Postnatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 3 | 161 | Condition | `Condition.code.coding` | 386337006.0 | Intrapartal care | http://snomed.info/sct |
| 4 | 184 | Encounter | `Encounter.hospitalization.admitSource.coding` | EHA000002 | Datang sendiri | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 5 | 185 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000117 | Rujukan dari Puskesmas | http://terminology.kemkes.go.id/sp |
| 6 | 186 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000685 | Rujukan dari Bidan Praktik Mandiri (BPM) | http://terminology.kemkes.go.id/sp |
| 7 | 191 | Observation | `Observation.code.coding` | SP000383 | Keadaan Ibu Saat Tiba | http://terminology.kemkes.go.id/sp |
| 8 | 192 | Observation | `Observation.valueCodeableConcept.coding` | 438949009.0 | Alive | http://snomed.info/sct |
| 9 | 193 | Observation | `Observation.valueCodeableConcept.coding` | 419099009.0 | Dead | http://snomed.info/sct |
| 10 | 203 | Observation | `Observation.code.coding` | 8665-2 | Last menstrual period start date | http://loinc.org |
| 11 | 214 | Observation | `Observation.code.coding` | 11778-8 | Delivery date Estimated | http://loinc.org |
| 12 | 225 | Observation | `Observation.code.coding` | 18185-9 | Gestational age | http://loinc.org |
| 13 | 228 | Observation | `Observation.component.code.coding` | SP000461 | Usia Kehamilan (Hari) | http://terminology.kemkes.go.id/sp |
| 14 | 240 | Observation | `Observation.code.coding` | 11996-6 | [#] Pregnancies | http://loinc.org |
| 15 | 251 | Observation | `Observation.code.coding` | 11977-6 | [#] Parity | http://loinc.org |
| 16 | 262 | Observation | `Observation.code.coding` | 69043-8 | Other pregnancy outcomes # | http://loinc.org |
| 17 | 273 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 18 | 285 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://loinc.org |
| 19 | 297 | Observation | `Observation.code.coding` | 8867-4 | Heart rate | http://loinc.org |
| 20 | 310 | Observation | `Observation.code.coding` | 9279-1 | Respiratory rate | http://loinc.org |
| 21 | 323 | Observation | `Observation.code.coding` | 8310-5 | Body temperature | http://loinc.org |
| 22 | 335 | Observation | `Observation.code.coding` | 11881-0 | Uterus Fundal height Tape measure | http://loinc.org |
| 23 | 347 | Observation | `Observation.code.coding` | 81956-5 | Date and time of death [TimeStamp] | http://loinc.org |
| 24 | 358 | Observation | `Observation.code.coding` | 79378-6 | Cause of death | http://loinc.org |
| 25 | 369 | Observation | `Observation.code.coding` | 55283-6 | Fetal Heart rate | http://loinc.org |
| 26 | 381 | Observation | `Observation.code.coding` | 271692001.0 | Presentation of fetus | http://snomed.info/sct |
| 27 | 382 | Observation | `Observation.valueCodeableConcept.coding` | 398236008.0 | Intrauterine | http://snomed.info/sct |
| 28 | 383 | Observation | `Observation.valueCodeableConcept.coding` | 298109001.0 | Ectopic | http://snomed.info/sct |
| 29 | 393 | Observation | `Observation.code.coding` | 72155-5 | Position in womb Fetus [RHEA] | http://loinc.org |
| 30 | 394 | Observation | `Observation.valueCodeableConcept.coding` | 1209182005.0 | Cephalic fetal presentation | http://snomed.info/sct |
| 31 | 395 | Observation | `Observation.valueCodeableConcept.coding` | 6096002.0 | Breech presentation | http://snomed.info/sct |
| 32 | 396 | Observation | `Observation.valueCodeableConcept.coding` | 288203005.0 | Transverse/oblique lie | http://snomed.info/sct |
| 33 | 397 | Observation | `Observation.valueCodeableConcept.coding` | 8014007.0 | Brow presentation of fetus | http://snomed.info/sct |
| 34 | 398 | Observation | `Observation.valueCodeableConcept.coding` | 8017000.0 | Face presentation | http://snomed.info/sct |
| 35 | 399 | Observation | `Observation.valueCodeableConcept.coding` | 249097002.0 | Footling breech presentation | http://snomed.info/sct |
| 36 | 400 | Observation | `Observation.valueCodeableConcept.coding` | 124736009.0 | Compound presentation | http://snomed.info/sct |
| 37 | 410 | Observation | `Observation.code.coding` | 249111004.0 | Engagement of head | http://snomed.info/sct |
| 38 | 411 | Observation | `Observation.valueCodeableConcept.coding` | 249112006.0 | Head engaged | http://snomed.info/sct |
| 39 | 412 | Observation | `Observation.valueCodeableConcept.coding` | 62098001.0 | Head not engaged | http://snomed.info/sct |
| 40 | 422 | Observation | `Observation.code.coding` | 289282009.0 | Amniotic membrane finding | http://snomed.info/sct |
| 41 | 423 | Observation | `Observation.valueCodeableConcept.coding` | 249125003.0 | Intact membranes | http://snomed.info/sct |
| 42 | 424 | Observation | `Observation.valueCodeableConcept.coding` | SP000120 | Non-intact membrane | http://terminology.kemkes.go.id/sp |
| 43 | 434 | Observation | `Observation.code.coding` | SP000686 | Faktor Risiko Persalinan | http://terminology.kemkes.go.id/sp |
| 44 | 435 | Observation | `Observation.valueCodeableConcept.coding` | SP000687 | Tidak Ada Faktor Risiko Persalinan | http://terminology.kemkes.go.id/sp |
| 45 | 436 | Observation | `Observation.valueCodeableConcept.coding` | SP000688 | Ada Faktor Risiko Persalinan | http://terminology.kemkes.go.id/sp |
| 46 | 446 | Observation | `Observation.code.coding` | 72150-6 | Delivery location | http://loinc.org |
| 47 | 447 | Observation | `Observation.valueCodeableConcept.coding` | 104.0 | Rumah Sakit | hhttp://terminology.kemkes.go.id/CodeSystem/organization-type |
| 48 | 448 | Observation | `Observation.valueCodeableConcept.coding` | 264362003.0 | Home | http://snomed.info/sct |
| 49 | 449 | Observation | `Observation.valueCodeableConcept.coding` | OT000001 | Polindes | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 50 | 450 | Observation | `Observation.valueCodeableConcept.coding` | OT000002 | Pustu | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 51 | 451 | Observation | `Observation.valueCodeableConcept.coding` | 102.0 | Pusat Kesehatan Masyarakat | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 52 | 452 | Observation | `Observation.valueCodeableConcept.coding` | 103.0 | Klinik | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 53 | 453 | Observation | `Observation.valueCodeableConcept.coding` | OT000008 | Rumah Bersalin | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 54 | 454 | Observation | `Observation.valueCodeableConcept.coding` | 82242000.0 | Children’s hospital | http://snomed.info/sct |
| 55 | 455 | Observation | `Observation.valueCodeableConcept.coding` | OT000003 | RS ODHA | hhttp://terminology.kemkes.go.id/CodeSystem/organization-type |
| 56 | 456 | Observation | `Observation.valueCodeableConcept.coding` | OT000004 | Bidan Praktek Mandiri | hhttp://terminology.kemkes.go.id/CodeSystem/organization-type |
| 57 | 457 | Observation | `Observation.valueCodeableConcept.coding` | LT000008 | Dalam perjalanan dari rumah/masyarakat | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 58 | 458 | Observation | `Observation.valueCodeableConcept.coding` | LT000009 | Dalam perjalanan ke faskes lain | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 59 | 459 | Observation | `Observation.valueCodeableConcept.coding` | LT000007 | Rumah Dukun | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 60 | 469 | Observation | `Observation.code.coding` | 93857-1 | Date and time of obstetric delivery | http://loinc.org |
| 61 | 482 | Observation | `Observation.code.coding` | OC000013 | Penolong Persalinan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 62 | 483 | Observation | `Observation.valueCodeableConcept.coding` | 309453006.0 | Registered midwife | http://snomed.info/sct |
| 63 | 484 | Observation | `Observation.valueCodeableConcept.coding` | 309343006.0 | Physician | http://snomed.info/sct |
| 64 | 485 | Observation | `Observation.valueCodeableConcept.coding` | 11935004.0 | Obstetrician | http://snomed.info/sct |
| 65 | 486 | Observation | `Observation.valueCodeableConcept.coding` | 106292003.0 | Professional nurse | http://snomed.info/sct |
| 66 | 487 | Observation | `Observation.valueCodeableConcept.coding` | 303071001.0 | Person in the family | http://snomed.info/sct |
| 67 | 488 | Observation | `Observation.valueCodeableConcept.coding` | OV000012 | Dukun | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 68 | 489 | Observation | `Observation.valueCodeableConcept.coding` | 125677006.0 | Relative | http://snomed.info/sct |
| 69 | 490 | Observation | `Observation.valueCodeableConcept.coding` | 257514003.0 | Member of public involved incidentally | http://snomed.info/sct |
| 70 | 505 | Observation | `Observation.code.coding` | 57071-3 | Obstetric delivery method | http://loinc.org |
| 71 | 506 | Observation | `Observation.valueCodeableConcept.coding` | 48782003.0 | Delivery normal | http://snomed.info/sct |
| 72 | 507 | Observation | `Observation.valueCodeableConcept.coding` | 200144004.0 | Deliveries by cesarean | http://snomed.info/sct |
| 73 | 508 | Observation | `Observation.valueCodeableConcept.coding` | 200138003.0 | Vacuum extractor delivery - delivered | http://snomed.info/sct |
| 74 | 509 | Observation | `Observation.valueCodeableConcept.coding` | 200130005.0 | Forceps delivery - delivered | http://snomed.info/sct |
| 75 | 523 | Procedure | `Procedure.code.coding` | 73.59 | Other manually assisted delivery | http://hl7.org/fhir/sid/icd-9-cm |
| 76 | 524 | Procedure | `Procedure.code.coding` | 74.1 | Classical cesarean section | http://hl7.org/fhir/sid/icd-9-cm |
| 77 | 525 | Procedure | `Procedure.code.coding` | 72.7 | Vacuum extraction | http://hl7.org/fhir/sid/icd-9-cm |
| 78 | 526 | Procedure | `Procedure.code.coding` | 72.0 | Low forceps delivery | http://hl7.org/fhir/sid/icd-9-cm |
| 79 | 540 | Observation | `Observation.code.coding` | 405195003.0 | Intrapartum maternal status | http://snomed.info/sct |
| 80 | 541 | Observation | `Observation.valueCodeableConcept.coding` | 102514002.0 | Well female adult | http://snomed.info/sct |
| 81 | 542 | Observation | `Observation.valueCodeableConcept.coding` | 39104002.0 | Illness | http://snomed.info/sct |
| 82 | 543 | Observation | `Observation.valueCodeableConcept.coding` | 131148009.0 | Bleeding | http://snomed.info/sct |
| 83 | 544 | Observation | `Observation.valueCodeableConcept.coding` | 386661006.0 | Fever | http://snomed.info/sct |
| 84 | 545 | Observation | `Observation.valueCodeableConcept.coding` | 91175000.0 | Seizure | http://snomed.info/sct |
| 85 | 546 | Observation | `Observation.valueCodeableConcept.coding` | 59283008.0 | Maternal death | http://snomed.info/sct |
| 86 | 560 | Condition | `Condition.code.coding` | 38341003.0 | Hypertensive disorder, systemic arterial | http://snomed.info/sct |
| 87 | 561 | Condition | `Condition.code.coding` | 398254007.0 | Pre-eclampsia | http://snomed.info/sct |
| 88 | 562 | Condition | `Condition.code.coding` | 48194001.0 | Pregnancy-induced hypertension | http://snomed.info/sct |
| 89 | 563 | Condition | `Condition.code.coding` | 199746004.0 | Obstructed labor | http://snomed.info/sct |
| 90 | 564 | Condition | `Condition.code.coding` | 38010008.0 | Intrapartum hemorrhage | http://snomed.info/sct |
| 91 | 565 | Condition | `Condition.code.coding` | 40733004.0 | Infectious disease | http://snomed.info/sct |
| 92 | 566 | Condition | `Condition.code.coding` | 386639001.0 | Termination of pregnancy | http://snomed.info/sct |
| 93 | 567 | Condition | `Condition.code.coding` | 44223004.0 | Premature rupture of membranes | http://snomed.info/sct |
| 94 | 568 | Condition | `Condition.code.coding` | 15938005.0 | Eclampsia | http://snomed.info/sct |
| 95 | 569 | Condition | `Condition.code.coding` | 9293002.0 | Atony of uterus | http://snomed.info/sct |
| 96 | 570 | Condition | `Condition.code.coding` | 283380005.0 | Laceration of perineum | http://snomed.info/sct |
| 97 | 571 | Condition | `Condition.code.coding` | 199745000.0 | Complication occurring during labor and delivery | http://snomed.info/sct |
| 98 | 584 | Observation | `Observation.code.coding` | SP000379 | Tatalaksana Komplikasi Persalinan | http://terminology.kemkes.go.id/sp |
| 99 | 585 | Observation | `Observation.valueCodeableConcept.coding` | SP000013 | Pemberian MgSO4 | http://terminology.kemkes.go.id/sp |
| 100 | 586 | Observation | `Observation.valueCodeableConcept.coding` | 308116003.0 | Antihypertensive therapy | http://snomed.info/sct |
| 101 | 587 | Observation | `Observation.valueCodeableConcept.coding` | 430701006.0 | Resuscitation using intravenous fluid | http://snomed.info/sct |
| 102 | 588 | Observation | `Observation.valueCodeableConcept.coding` | SP000156 | Pemberian Obat Uterotonik | http://terminology.kemkes.go.id/sp |
| 103 | 589 | Observation | `Observation.valueCodeableConcept.coding` | 236998006.0 | Bimanual uterine massage | http://snomed.info/sct |
| 104 | 590 | Observation | `Observation.valueCodeableConcept.coding` | 360362007.0 | Suture of laceration of perineum | http://snomed.info/sct |
| 105 | 591 | Observation | `Observation.valueCodeableConcept.coding` | 28233006.0 | Manual removal of retained placenta | http://snomed.info/sct |
| 106 | 592 | Observation | `Observation.valueCodeableConcept.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 107 | 607 | Observation | `Observation.code.coding` | 63893-2 | Outcome of pregnancy | http://loinc.org |
| 108 | 608 | Observation | `Observation.valueCodeableConcept.coding` | LA14270-5 | Live birth | http://loinc.org |
| 109 | 609 | Observation | `Observation.valueCodeableConcept.coding` | LA14271-3 | Stillborn | http://loinc.org |
| 110 | 610 | Observation | `Observation.valueCodeableConcept.coding` | LA14272-1 | Miscarriage | http://loinc.org |
| 111 | 611 | Observation | `Observation.valueCodeableConcept.coding` | LA14273-9 | Induced abortion | http://loinc.org |
| 112 | 626 | Procedure | `Procedure.code.coding` | SP000130 | Menggunakan Partograf | http://terminology.kemkes.go.id/sp |
| 113 | 641 | Procedure | `Procedure.code.coding` | 431868002.0 | Initiation of breastfeeding | http://snomed.info/sct |
| 114 | 655 | Procedure | `Procedure.code.coding` | 409063005.0 | Counselling | http://snomed.info/sct |
| 115 | 657 | Procedure | `Procedure.code.coding` | ED000008 | Edukasi Tanda Bahaya Kehamilan, Bersalin dan Nifas | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 116 | 658 | Procedure | `Procedure.code.coding` | ED000009 | Edukasi IMD dan ASI Eksklusif | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 117 | 659 | Procedure | `Procedure.code.coding` | SP000121 | Edukasi Tanda Bahaya Baru Lahir | http://terminology.kemkes.go.id/sp |
| 118 | 660 | Procedure | `Procedure.code.coding` | ED000005 | Edukasi Gizi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 119 | 661 | Procedure | `Procedure.code.coding` | PC000001 | Perawatan Tali Pusat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 120 | 662 | Procedure | `Procedure.code.coding` | ED000010 | Edukasi PHBS | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 121 | 676 | Observation | `Observation.code.coding` | 365662002.0 | Finding of amniotic fluid appearance | http://snomed.info/sct |
| 122 | 677 | Observation | `Observation.valueCodeableConcept.coding` | 168090003.0 | Amniotic fluid clear | http://snomed.info/sct |
| 123 | 678 | Observation | `Observation.valueCodeableConcept.coding` | 408781009.0 | Straw colored amniotic fluid | http://snomed.info/sct |
| 124 | 679 | Observation | `Observation.valueCodeableConcept.coding` | 168092006.0 | Amniotic fluid -meconium stain | http://snomed.info/sct |
| 125 | 680 | Observation | `Observation.valueCodeableConcept.coding` | 249134008.0 | Bloodstained liquor | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 63 |
| http://loinc.org | 24 |
| http://terminology.kemkes.go.id/sp | 13 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 8 |
| http://terminology.kemkes.go.id/CodeSystem/organization-type | 5 |
| http://hl7.org/fhir/sid/icd-9-cm | 4 |
| hhttp://terminology.kemkes.go.id/CodeSystem/organization-type | 3 |
| http://terminology.kemkes.go.id/CodeSystem/location-type | 3 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 2 |
| **Total** | **125** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 37 | – | Nama Faskes | Organization | `Organization.name` |
