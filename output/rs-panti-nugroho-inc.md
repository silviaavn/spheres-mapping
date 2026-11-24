# Output Form: SIM RS Panti Nugroho INC

Sumber: `mapping/phdt-data-dictionary-rs-panti-nugroho-inc.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-rs-panti-nugroho-inc.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 37 |
| Code (`jumlah code` = 1) | 118 |
| Code unik (code + CodeSystem) | 117 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 8 |
| Variabel BQ (unik) | 1 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–27 | Patient | – | – | _Nama Ibu_ → `Patient.name.text` (2, tanpa BQ)<br>_NIK_ → `Patient.identifier.value` (6, tanpa BQ)<br>_No HP_ → `Patient.telecom` (7, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (10, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (11, tanpa BQ)<br>_Alamat Domisili_ → `Patient.address.line` (13, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (18, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (21, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.extension.valueCode` (24, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.extension.valueCode` (27, tanpa BQ) |
| 2 | 28–35 | RelatedPerson | – | – | `True` → `RelatedPerson.name.text` (29)<br>`True` → `RelatedPerson.identifier.value` (34) |
| 3 | 74–80 | Practitioner | – | – | _NIK_ → `Practitioner.identifier.value` (76, tanpa BQ)<br>_Nama Tenaga Kesehatan_ → `Practitioner.name.text` (78, tanpa BQ)<br>_Jenis Kelamin Tenaga Kesehatan_ → `Practitioner.gender` (79, tanpa BQ) |
| 4 | 81–88 | PractitionerRole | – | – | _Tenaga Pemeriksa_ → `PractitionerRole.code.coding` (85, tanpa BQ) |
| 5 | 90–105 | Encounter | – | – | _Jenis Kunjungan INC_ → `Encounter.class` (91, tanpa BQ)<br>_Tanggal Masuk INC_ → `Encounter.period.start` (100, tanpa BQ)<br>_Tanggal Keluar INC_ → `Encounter.period.end` (101, tanpa BQ)<br>_Tempat Pelayanan INC_ → `Encounter.location.display` (103, tanpa BQ) |
| 6 | 106–114 | Condition | 386337006.0 | Intrapartal care | _Diagnosis Masuk_ → `Condition.code.coding` (108, tanpa BQ) |
| 7 | 125–138 | EpisodeOfCare | ANC | Antenatal Care | – |
| 8 | 140–148 | EpisodeOfCare | PNC | Postnatal Care | – |
| 9 | 149–160 | Observation | SP000383 | Keadaan Ibu Saat Tiba | _Keadaan Ibu Saat Tiba_ → `Observation.valueCodeableConcept.coding` (152, tanpa BQ) |
| 10 | 161–172 | Observation | 8480-6 | Systolic blood pressure | _Tekanan Darah Sistolik_ → `Observation.valueQuantity.value` (164, tanpa BQ) |
| 11 | 173–184 | Observation | 8462-4 | Diastolic blood pressure | _Tekanan Darah Diastolik_ → `Observation.valueQuantity.value` (176, tanpa BQ) |
| 12 | 185–197 | Observation | 8867-4 | Heart rate | _Frekuensi Nadi_ → `Observation.valueQuantity.value` (188, tanpa BQ) |
| 13 | 198–210 | Observation | 9279-1 | Respiratory rate | _Pernapasan_ → `Observation.valueQuantity.value` (201, tanpa BQ) |
| 14 | 211–223 | Observation | – | – | _Suhu Badan_ → `Observation.valueQuantity.value` (214, tanpa BQ) |
| 15 | 224–235 | Observation | 11881-0 | Uterus Fundal height Tape measure | _Tinggi Fundus Uteri_ → `Observation.valueQuantity.value` (227, tanpa BQ) |
| 16 | 236–249 | Observation | 246435002.0 | Number of fetuses | _JumlahJanin_ → `Observation.valueInteger` (240, tanpa BQ)<br>_Detak Jantung Janin_ → `Observation.identifier.value` (249, tanpa BQ) |
| 17 | 250–262 | Observation | 55283-6 | Fetal Heart rate | _Letak Janin_ → `Observation.identifier.value` (262, tanpa BQ) |
| 18 | 263–275 | Observation | 271692001.0 | Presentation of fetus | _Presentasi Janin_ → `Observation.identifier.value` (275, tanpa BQ) |
| 19 | 276–294 | Observation | 72155-5 | Position in womb Fetus [RHEA] | _Posisi Kepala Janin terhadap PAP (Pintu Atas Panggul)_ → `Observation.identifier.value` (294, tanpa BQ) |
| 20 | 295–308 | Observation | 249111004.0 | Engagement of head | _Kondisi Ketuban_ → `Observation.identifier.value` (308, tanpa BQ) |
| 21 | 309–321 | Observation | 289282009.0 | Amniotic membrane finding | _Faktor risiko INC_ → `Observation.status` (321, tanpa BQ) |
| 22 | 322–332 | Observation | SP000015 | Risiko Masalah Kesehatan | _Tempat Melahirkan_ → `Observation.status` (332, tanpa BQ) |
| 23 | 333–363 | Observation | 72150-6 | Delivery location | – |
| 24 | 379–393 | Observation | 76516-4 | Gestational age—​at birth | _Usia Kehamilan/ Gestasi pada saat Persalinan_ → `Observation.valueQuantity.value` (382, tanpa BQ) |
| 25 | 394–404 | Observation | 93857-1 | Date and time of obstetric delivery | _Tanggal dan Jam Persalinan_ → `Observation.valueDateTime` (397, tanpa BQ) |
| 26 | 405–415 | Observation | OC000013 | Penolong Persalinan | _Nama Penolong Persalinan_ → `Observation.status` (405, tanpa BQ) |
| 27 | 417–430 | Observation | 57071-3 | Obstetric delivery method | _Cara Persalinan_ → `Observation.valueCodeableConcept.coding` (420, tanpa BQ) |
| 28 | 431–448 | Observation | 405195003.0 | Intrapartum maternal status | _Keadaan Ibu_ → `Observation.valueCodeableConcept.coding` (434, tanpa BQ) |
| 29 | 449–468 | Condition | 199746004.0 | Obstructed labor | _Komplikasi Persalinan_ → `Condition.clinicalStatus.coding` (449, tanpa BQ) |
| 30 | 469–487 | Observation | SP000379 | Tatalaksana Komplikasi Persalinan | _Tatalaksana Komplikasi Persalinan_ → `Observation.valueCodeableConcept.coding` (472, tanpa BQ) |
| 31 | 488–501 | Observation | 63893-2 | Outcome of pregnancy | _Luaran Kehamilan_ → `Observation.valueCodeableConcept.coding` (491, tanpa BQ) |
| 32 | 503–524 | ServiceRequest | 409014006.0 | Delivery care management | _Faskes Rujukan_ → `ServiceRequest.locationCode.coding` (516, tanpa BQ)<br>_Nama Faskes Rujukan_ → `ServiceRequest.locationCode.text` (524, tanpa BQ) |
| 33 | 526–536 | Procedure | SP000130 | Menggunakan Partograf | _Pelayanan Menggunakan Partograf_ → `Procedure.category.coding` (526, tanpa BQ) |
| 34 | 537–550 | Observation | 365662002.0 | Finding of amniotic fluid appearance | _Warna Ketuban_ → `Observation.valueCodeableConcept.coding` (539, tanpa BQ) |
| 35 | 551–553 | Procedure | 409063005.0 | Counselling | _Konseling_ → `Procedure.category.coding` (551, tanpa BQ) |
| 36 | 554–567 | Procedure | ED000008 | Edukasi Tanda Bahaya Kehamilan, Bersalin dan Nifas | – |
| 37 | 568–572 | Practitioner | – | – | _No Ktp Pencatat_ → `Practitioner.identifier.value` (570, tanpa BQ)<br>_Nama Pencatat_ → `Practitioner.name` (572, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 23 |
| Procedure | 3 |
| Practitioner | 2 |
| Condition | 2 |
| EpisodeOfCare | 2 |
| Patient | 1 |
| RelatedPerson | 1 |
| PractitionerRole | 1 |
| Encounter | 1 |
| ServiceRequest | 1 |
| **Total** | **37** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 85 | PractitionerRole | `PractitionerRole.code.coding` | 309453006.0 | Registered midwife | http://snomed.info/sct |
| 2 | 86 | PractitionerRole | `PractitionerRole.code.coding` | 309367003.0 | Obstetrician and gynecologist | http://snomed.info/sct |
| 3 | 87 | PractitionerRole | `PractitionerRole.code.coding` | 309343006.0 | Physician | http://snomed.info/sct |
| 4 | 88 | PractitionerRole | `PractitionerRole.code.coding` | 224535009.0 | Registered nurse | http://snomed.info/sct |
| 5 | 109 | Condition | `Condition.code.coding` | 386337006.0 | Intrapartal care | http://snomed.info/sct |
| 6 | 126 | EpisodeOfCare | `EpisodeOfCare.type.coding` | ANC | Antenatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 7 | 141 | EpisodeOfCare | `EpisodeOfCare.type.coding` | PNC | Postnatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 8 | 151 | Observation | `Observation.code.coding` | SP000383 | Keadaan Ibu Saat Tiba | http://terminology.kemkes.go.id/sp |
| 9 | 152 | Observation | `Observation.valueCodeableConcept.coding` | 438949009.0 | Alive | http://snomed.info/sct |
| 10 | 153 | Observation | `Observation.valueCodeableConcept.coding` | 419099009.0 | Dead | http://snomed.info/sct |
| 11 | 163 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 12 | 175 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://loinc.org |
| 13 | 187 | Observation | `Observation.code.coding` | 8867-4 | Heart rate | http://loinc.org |
| 14 | 200 | Observation | `Observation.code.coding` | 9279-1 | Respiratory rate | http://loinc.org |
| 15 | 226 | Observation | `Observation.code.coding` | 11881-0 | Uterus Fundal height Tape measure | http://loinc.org |
| 16 | 238 | Observation | `Observation.code.coding` | 246435002.0 | Number of fetuses | http://snomed.info/sct |
| 17 | 239 | Observation | `Observation.code.coding` | ANC.B8.DE109 | Number of fetuses | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 18 | 251 | Observation | `Observation.code.coding` | 55283-6 | Fetal Heart rate | http://loinc.org |
| 19 | 264 | Observation | `Observation.code.coding` | 271692001.0 | Presentation of fetus | http://snomed.info/sct |
| 20 | 265 | Observation | `Observation.valueCodeableConcept.coding` | 398236008.0 | Intrauterine | http://snomed.info/sct |
| 21 | 266 | Observation | `Observation.valueCodeableConcept.coding` | 298109001.0 | Ectopic | http://snomed.info/sct |
| 22 | 277 | Observation | `Observation.code.coding` | 72155-5 | Position in womb Fetus [RHEA] | http://loinc.org |
| 23 | 278 | Observation | `Observation.valueCodeableConcept.coding` | 70028003.0 | Vertex presentation | http://snomed.info/sct |
| 24 | 279 | Observation | `Observation.valueCodeableConcept.coding` | 249083005.0 | Posterior fontanelle presenting | http://snomed.info/sct |
| 25 | 280 | Observation | `Observation.valueCodeableConcept.coding` | 288203005.0 | Transverse/oblique lie | http://snomed.info/sct |
| 26 | 281 | Observation | `Observation.valueCodeableConcept.coding` | 6096002.0 | Breech presentation | http://snomed.info/sct |
| 27 | 282 | Observation | `Observation.valueCodeableConcept.coding` | 8014007.0 | Brow presentation of fetus | http://snomed.info/sct |
| 28 | 283 | Observation | `Observation.valueCodeableConcept.coding` | 8017000.0 | Face presentation | http://snomed.info/sct |
| 29 | 284 | Observation | `Observation.valueCodeableConcept.coding` | 249097002.0 | Footling breech presentation | http://snomed.info/sct |
| 30 | 285 | Observation | `Observation.valueCodeableConcept.coding` | 124736009.0 | Compound presentation | http://snomed.info/sct |
| 31 | 296 | Observation | `Observation.code.coding` | 249111004.0 | Engagement of head | http://snomed.info/sct |
| 32 | 297 | Observation | `Observation.valueCodeableConcept.coding` | 249112006.0 | Head engaged | http://snomed.info/sct |
| 33 | 298 | Observation | `Observation.valueCodeableConcept.coding` | 62098001.0 | Head not engaged | http://snomed.info/sct |
| 34 | 310 | Observation | `Observation.code.coding` | 289282009.0 | Amniotic membrane finding | http://snomed.info/sct |
| 35 | 311 | Observation | `Observation.valueCodeableConcept.coding` | 249125003.0 | Intact membranes | http://snomed.info/sct |
| 36 | 312 | Observation | `Observation.valueCodeableConcept.coding` | SP000120 | Non-intact membrane | http://snomed.info/sct |
| 37 | 323 | Observation | `Observation.code.coding` | SP000015 | Risiko Masalah Kesehatan | http://terminology.kemkes.go.id/sp |
| 38 | 334 | Observation | `Observation.code.coding` | 72150-6 | Delivery location | http://loinc.org |
| 39 | 335 | Observation | `Observation.valueCodeableConcept.coding` | 264362003.0 | Home | http://snomed.info/sct |
| 40 | 336 | Observation | `Observation.valueCodeableConcept.coding` | OT000001 | Polindes | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 41 | 337 | Observation | `Observation.valueCodeableConcept.coding` | OT000002 | Pustu | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 42 | 338 | Observation | `Observation.valueCodeableConcept.coding` | 102.0 | Pusat Kesehatan Masyarakat | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 43 | 339 | Observation | `Observation.valueCodeableConcept.coding` | 103.0 | Klinik | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 44 | 340 | Observation | `Observation.valueCodeableConcept.coding` | OT000008 | Rumah Bersalin | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 45 | 341 | Observation | `Observation.valueCodeableConcept.coding` | 82242000.0 | Children’s hospital | http://snomed.info/sct |
| 46 | 342 | Observation | `Observation.valueCodeableConcept.coding` | 104.0 | Rumah Sakit | hhttp://terminology.kemkes.go.id/CodeSystem/organization-type |
| 47 | 343 | Observation | `Observation.valueCodeableConcept.coding` | OT000003 | RS ODHA | hhttp://terminology.kemkes.go.id/CodeSystem/organization-type |
| 48 | 344 | Observation | `Observation.valueCodeableConcept.coding` | OT000004 | Bidan Praktek Mandiri | hhttp://terminology.kemkes.go.id/CodeSystem/organization-type |
| 49 | 345 | Observation | `Observation.valueCodeableConcept.coding` | LT000008 | Dalam perjalanan dari rumah/masyarakat | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 50 | 346 | Observation | `Observation.valueCodeableConcept.coding` | LT000009 | Dalam perjalanan ke faskes lain | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 51 | 347 | Observation | `Observation.valueCodeableConcept.coding` | OT000006 | Rumah Sakit Pemerintah | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 52 | 348 | Observation | `Observation.valueCodeableConcept.coding` | OT000007 | Rumah Sakit Swasta | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 53 | 349 | Observation | `Observation.valueCodeableConcept.coding` | LT000006 | Rumah Ibu | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 54 | 350 | Observation | `Observation.valueCodeableConcept.coding` | OT000010 | Klinik Medis Utama | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 55 | 351 | Observation | `Observation.valueCodeableConcept.coding` | OT000011 | Klinik Medis Pratama | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 56 | 352 | Observation | `Observation.valueCodeableConcept.coding` | 101.0 | Tempat Praktik Mandiri Tenaga Kesehatan | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 57 | 353 | Observation | `Observation.valueCodeableConcept.coding` | 394573001.0 | Maternity clinic | http://snomed.info/sct |
| 58 | 354 | Observation | `Observation.valueCodeableConcept.coding` | LT000007 | Rumah Dukun | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 59 | 355 | Observation | `Observation.valueCodeableConcept.coding` | LT000010 | Lainnya | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 60 | 356 | Observation | `Observation.valueCodeableConcept.coding` | LT000011 | Belum Tahu | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 61 | 381 | Observation | `Observation.code.coding` | 76516-4 | Gestational age—​at birth | http://loinc.org |
| 62 | 384 | Observation | `Observation.component.code.coding` | SP000398 | Usia Kehamilan Saat Persalinan (hari) | http://terminology.kemkes.go.id/sp |
| 63 | 396 | Observation | `Observation.code.coding` | 93857-1 | Date and time of obstetric delivery | http://loinc.org |
| 64 | 407 | Observation | `Observation.code.coding` | OC000013 | Penolong Persalinan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 65 | 419 | Observation | `Observation.code.coding` | 57071-3 | Obstetric delivery method | http://loinc.org |
| 66 | 420 | Observation | `Observation.valueCodeableConcept.coding` | 48782003.0 | Delivery normal | http://snomed.info/sct |
| 67 | 421 | Observation | `Observation.valueCodeableConcept.coding` | 200138003.0 | Vacuum extractor delivery - delivered | http://snomed.info/sct |
| 68 | 422 | Observation | `Observation.valueCodeableConcept.coding` | 200130005.0 | Forceps delivery - delivered | http://snomed.info/sct |
| 69 | 423 | Observation | `Observation.valueCodeableConcept.coding` | 200144004.0 | Deliveries by cesarean | http://snomed.info/sct |
| 70 | 433 | Observation | `Observation.code.coding` | 405195003.0 | Intrapartum maternal status | http://snomed.info/sct |
| 71 | 434 | Observation | `Observation.valueCodeableConcept.coding` | 102514002.0 | Well female adult | http://snomed.info/sct |
| 72 | 435 | Observation | `Observation.valueCodeableConcept.coding` | 39104002.0 | Illness | http://snomed.info/sct |
| 73 | 436 | Observation | `Observation.valueCodeableConcept.coding` | 131148009.0 | Bleeding | http://snomed.info/sct |
| 74 | 437 | Observation | `Observation.valueCodeableConcept.coding` | 386661006.0 | Fever | http://snomed.info/sct |
| 75 | 438 | Observation | `Observation.valueCodeableConcept.coding` | 91175000.0 | Seizure | http://snomed.info/sct |
| 76 | 439 | Observation | `Observation.valueCodeableConcept.coding` | 249215002.0 | Odor of lochia | http://snomed.info/sct |
| 77 | 440 | Observation | `Observation.valueCodeableConcept.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 78 | 441 | Observation | `Observation.valueCodeableConcept.coding` | 59283008.0 | Maternal death | http://snomed.info/sct |
| 79 | 451 | Condition | `Condition.code.coding` | 199746004.0 | Obstructed labor | http://snomed.info/sct |
| 80 | 452 | Condition | `Condition.code.coding` | 48194001.0 | Pregnancy-induced hypertension | http://snomed.info/sct |
| 81 | 453 | Condition | `Condition.code.coding` | 38010008.0 | Intrapartum hemorrhage | http://snomed.info/sct |
| 82 | 454 | Condition | `Condition.code.coding` | 40733004.0 | Infectious disease | http://snomed.info/sct |
| 83 | 455 | Condition | `Condition.code.coding` | 386639001.0 | Termination of pregnancy | http://snomed.info/sct |
| 84 | 456 | Condition | `Condition.code.coding` | 44223004.0 | Premature rupture of membranes | http://snomed.info/sct |
| 85 | 457 | Condition | `Condition.code.coding` | 38341003.0 | Hypertensive disorder, systemic arterial | http://snomed.info/sct |
| 86 | 458 | Condition | `Condition.code.coding` | 398254007.0 | Pre-eclampsia | http://snomed.info/sct |
| 87 | 459 | Condition | `Condition.code.coding` | 15938005.0 | Eclampsia | http://snomed.info/sct |
| 88 | 460 | Condition | `Condition.code.coding` | 9293002.0 | Atony of uterus | http://snomed.info/sct |
| 89 | 461 | Condition | `Condition.code.coding` | 283380005.0 | Laceration of perineum | http://snomed.info/sct |
| 90 | 462 | Condition | `Condition.code.coding` | 199745000.0 | Complication occurring during labor and delivery | http://snomed.info/sct |
| 91 | 471 | Observation | `Observation.code.coding` | SP000379 | Tatalaksana Komplikasi Persalinan | http://terminology.kemkes.go.id/sp |
| 92 | 472 | Observation | `Observation.valueCodeableConcept.coding` | 430701006.0 | Resuscitation using intravenous fluid | http://snomed.info/sct |
| 93 | 473 | Observation | `Observation.valueCodeableConcept.coding` | SP000156 | Pemberian Obat Uterotonik | http://terminology.kemkes.go.id/sp |
| 94 | 474 | Observation | `Observation.valueCodeableConcept.coding` | 236998006.0 | Bimanual uterine massage | http://snomed.info/sct |
| 95 | 475 | Observation | `Observation.valueCodeableConcept.coding` | 360362007.0 | Suture of laceration of perineum | http://snomed.info/sct |
| 96 | 476 | Observation | `Observation.valueCodeableConcept.coding` | 28233006.0 | Manual removal of retained placenta | http://snomed.info/sct |
| 97 | 477 | Observation | `Observation.valueCodeableConcept.coding` | SP000013 | Pemberian MgSO4 | http://terminology.kemkes.go.id/sp |
| 98 | 478 | Observation | `Observation.valueCodeableConcept.coding` | 308116003.0 | Antihypertensive therapy | http://snomed.info/sct |
| 99 | 479 | Observation | `Observation.valueCodeableConcept.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 100 | 490 | Observation | `Observation.code.coding` | 63893-2 | Outcome of pregnancy | http://loinc.org |
| 101 | 491 | Observation | `Observation.valueCodeableConcept.coding` | LA14270-5 | Live birth | http://loinc.org |
| 102 | 492 | Observation | `Observation.valueCodeableConcept.coding` | LA14271-3 | Stillborn | http://loinc.org |
| 103 | 493 | Observation | `Observation.valueCodeableConcept.coding` | LA14272-1 | Miscarriage | http://loinc.org |
| 104 | 494 | Observation | `Observation.valueCodeableConcept.coding` | LA14273-9 | Induced abortion | http://loinc.org |
| 105 | 507 | ServiceRequest | `ServiceRequest.code.coding` | 409014006.0 | Delivery care management | http://snomed.info/sct |
| 106 | 529 | Procedure | `Procedure.code.coding` | SP000130 | Menggunakan Partograf | http://terminology.kemkes.go.id/sp |
| 107 | 538 | Observation | `Observation.code.coding` | 365662002.0 | Finding of amniotic fluid appearance | http://snomed.info/sct |
| 108 | 539 | Observation | `Observation.valueCodeableConcept.coding` | 168090003.0 | Amniotic fluid clear | http://snomed.info/sct |
| 109 | 540 | Observation | `Observation.valueCodeableConcept.coding` | 408781009.0 | Straw colored amniotic fluid | http://snomed.info/sct |
| 110 | 541 | Observation | `Observation.valueCodeableConcept.coding` | 249134008.0 | Bloodstained liquor | http://snomed.info/sct |
| 111 | 542 | Observation | `Observation.valueCodeableConcept.coding` | 168092006.0 | Amniotic fluid -meconium stain | http://snomed.info/sct |
| 112 | 553 | Procedure | `Procedure.code.coding` | 409063005.0 | Counselling | http://snomed.info/sct |
| 113 | 555 | Procedure | `Procedure.code.coding` | ED000008 | Edukasi Tanda Bahaya Kehamilan, Bersalin dan Nifas | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 114 | 556 | Procedure | `Procedure.code.coding` | SP000121 | Edukasi Tanda Bahaya Baru Lahir | http://terminology.kemkes.go.id/sp |
| 115 | 557 | Procedure | `Procedure.code.coding` | ED000009 | Edukasi IMD dan ASI Eksklusif | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 116 | 558 | Procedure | `Procedure.code.coding` | ED000005 | Edukasi Gizi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 117 | 559 | Procedure | `Procedure.code.coding` | PC000001 | Perawatan Tali Pusat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 118 | 560 | Procedure | `Procedure.code.coding` | ED000010 | Edukasi PHBS | http://terminology.kemkes.go.id/CodeSystem/clinical-term |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 66 |
| http://loinc.org | 16 |
| http://terminology.kemkes.go.id/CodeSystem/organization-type | 10 |
| http://terminology.kemkes.go.id/sp | 8 |
| http://terminology.kemkes.go.id/CodeSystem/location-type | 6 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 6 |
| hhttp://terminology.kemkes.go.id/CodeSystem/organization-type | 3 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 2 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 1 |
| **Total** | **118** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 40 | – | Faskes yang Melayani INC | Organization | `Organization.name` |
| 364 | – | Alamat Bersalin | Location | `Location.type.coding` |
| 416 | – | Jenis Penolong Persalinan | – | `` |
| 502 | – | Rujuk | – | `` |
| 525 | – | Jenis Rujukan | – | `` |
