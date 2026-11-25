# Output Form: SIM RS Narmada KIA

Sumber: `mapping/phdt-data-dictionary-rs-narmada-kia.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-rs-narmada-kia.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 50 |
| Code (`jumlah code` = 1) | 110 |
| Code unik (code + CodeSystem) | 104 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 2 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–30 | Patient | – | – | _Nama Pasien_ → `Patient.name.text` (2, tanpa BQ)<br>_NIK_ → `Patient.identifier.value` (6, tanpa BQ)<br>_No Hp_ → `Patient.telecom` (7, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (10, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (11, tanpa BQ)<br>_Status Pernikahan_ → `Patient.maritalStatus.coding` (13, tanpa BQ)<br>_Alamat_ → `Patient.address.line` (16, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (21, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.extension.valueCode` (27, tanpa BQ)<br>_Nama Kelurahan_ → `Patient.address.extension.extension.valueCode` (30, tanpa BQ) |
| 2 | 69–80 | Practitioner | – | – | _Nama Dokter_ → `Practitioner.name` (72, tanpa BQ)<br>_Nama Pengkaji 1_ → `Practitioner.name` (76, tanpa BQ) |
| 3 | 81–100 | Encounter | – | – | _No Rawat_ → `Encounter.identifier` (81, tanpa BQ)<br>_Tanggal_ → `Encounter.period.start` (95, tanpa BQ) |
| 4 | 101–114 | Condition | 1255917009.0 | Maternal perinatal care | – |
| 5 | 127–146 | EpisodeOfCare | ANC | Antenatal Care | – |
| 6 | 147–151 | EpisodeOfCare | PNC | Postnatal Care | – |
| 7 | 152–160 | Condition | 404684003.0 | Clinical finding | _Keluhan_ → `Condition.clinicalStatus.coding` (152, tanpa BQ) |
| 8 | 161–172 | Observation | 11996-6 | [#] Pregnancies | _Riwayat Gravida_ → `Observation.valueInteger` (165, tanpa BQ) |
| 9 | 173–184 | Observation | 11977-6 | [#] Parity | _Riwayat Partus_ → `Observation.valueInteger` (177, tanpa BQ) |
| 10 | 185–196 | Observation | 69043-8 | Other pregnancy outcomes # | _Riwayat Abortus_ → `Observation.valueInteger` (189, tanpa BQ) |
| 11 | 197–207 | Observation | 726001007.0 | Past pregnancy history of live birth | _Riwayat Persalinan Hidup_ → `Observation.valueInteger` (200, tanpa BQ) |
| 12 | 210–228 | Immunization | – | – | _Jumlah Imunisasi TT_ → `Immunization.status` (210, tanpa BQ) |
| 13 | 229–240 | Observation | 8665-2 | Last menstrual period start date | _HPHT_ → `Observation.valueDateTime` (233, tanpa BQ) |
| 14 | 241–252 | Observation | 18185-9 | Gestational age | _Usia Kehamilan_ → `Observation.valueQuantity.value` (245, tanpa BQ) |
| 15 | 253–264 | Observation | 11778-8 | Delivery date Estimated | _HPL_ → `Observation.valueDateTime` (257, tanpa BQ) |
| 16 | 265–279 | Observation | 420209000.0 | History of contraceptive usage | _Riwayat KB_ → `Observation.valueCodeableConcept.coding` (268, tanpa BQ) |
| 17 | 280–292 | Observation | SP000644 | Komplikasi KB Sebelumnya | _Komplikasi KB Sebelumnya_ → `Observation.valueBoolean` (283, tanpa BQ)<br>_Keterangan Komplikasi KB Sebelumnya_ → `Observation.note` (285, tanpa BQ) |
| 18 | 293–303 | Observation | SP000645 | Alasan Berhenti KB | _Alasan Berhenti KB_ → `Observation.valueString` (296, tanpa BQ) |
| 19 | 304–318 | Condition | 56728002.0 | Chronic cervicitis | _Riwayat Ginekologi_ → `Condition.clinicalStatus.coding` (304, tanpa BQ) |
| 20 | 319–330 | MedicationStatement | – | – | _Kebiasaan Obat_ → `MedicationStatement.status` (319, tanpa BQ)<br>_Kebiasaan Keterangan Obat_ → `MedicationStatement.medicationCodeableConcept.text` (323, tanpa BQ) |
| 21 | 331–344 | Observation | 72166-2 | Tobacco smoking status | _Kebiasaan Merokok_ → `Observation.valueCodeableConcept.coding` (334, tanpa BQ)<br>_Kebiasaan Keterangan Merokok_ → `Observation.note.text` (344, tanpa BQ) |
| 22 | 345–357 | Observation | 11331-6 | History of Alcohol use | _Kebiasaan Alkohol_ → `Observation.valueCodeableConcept.coding` (348, tanpa BQ)<br>_Kebiasaan Keterangan Alkohol_ → `Observation.note.text` (357, tanpa BQ) |
| 23 | 358–369 | Observation | 9269-2 | Glasgow coma score total | _Glasgow Coma Scale_ → `Observation.valueQuantity.value` (362, tanpa BQ) |
| 24 | 370–382 | Observation | 8480-6 | Systolic blood pressure | _Tekanan Darah_ → `Observation.code.coding` (373, tanpa BQ)<br>_Tekanan Darah Sistol_ → `Observation.valueQuantity.value` (374, tanpa BQ) |
| 25 | 383–395 | Observation | 8462-4 | Diastolic blood pressure | _Tekanan Darah Diastol_ → `Observation.valueQuantity.value` (387, tanpa BQ) |
| 26 | 396–408 | Observation | 8867-4 | Heart Rate | _Nadi_ → `Observation.valueQuantity.value` (400, tanpa BQ) |
| 27 | 409–422 | Observation | 9279-1 | Respiratory rate | _Respiratory Rate_ → `Observation.valueQuantity.value` (413, tanpa BQ) |
| 28 | 423–435 | Observation | 8310-5 | Body temperature | _Suhu_ → `Observation.valueQuantity.value` (427, tanpa BQ) |
| 29 | 436–448 | Observation | 29463-7 | Body weight | _Berat Badan_ → `Observation.valueQuantity.value` (440, tanpa BQ) |
| 30 | 449–461 | Observation | 8302-2 | Body height | _Tinggi Badan_ → `Observation.valueQuantity.value` (453, tanpa BQ) |
| 31 | 462–473 | Observation | 39156-5 | Body mass index (BMI) [Ratio] | _Indeks Massa Tubuh_ → `Observation.valueQuantity.value` (465, tanpa BQ) |
| 32 | 474–488 | Observation | 284473002.0 | Mid upper arm circumference | _LiLA_ → `Observation.status` (474, tanpa BQ) |
| 33 | 489–501 | Observation | 11881-0 | Uterus Fundal height Tape measure | _Tinggi Fundus_ → `Observation.valueQuantity.value` (493, tanpa BQ) |
| 34 | 502–516 | Observation | 89087-1 | Fetal Body weight Estimated | _Taksiran Berat Janin_ → `Observation.valueQuantity.value` (506, tanpa BQ)<br>_Presentasi_ → `Observation.identifier.value` (516, tanpa BQ) |
| 35 | 517–533 | Observation | 72155-5 | Position in womb Fetus [RHEA] | _Penurunan_ → `Observation.identifier.value` (533, tanpa BQ) |
| 36 | 534–547 | Observation | 249111004.0 | Engagement of head | – |
| 37 | 548–568 | Observation | 249120008.0 | Onset of labor first stage | _Frekuensi HIS_ → `Observation.component.code.coding` (558, tanpa BQ)<br>_Kekuatan HIS_ → `Observation.component.code.coding` (561, tanpa BQ)<br>_Durasi HIS_ → `Observation.component.code.coding` (565, tanpa BQ)<br>_Denyut Jantung Janin_ → `Observation.status` (568, tanpa BQ) |
| 38 | 569–582 | Observation | 55283-6 | Fetal Heart rate | _Keterangan Denyut Jantung Janin_ → `Observation.identifier.value` (582, tanpa BQ) |
| 39 | 583–594 | Observation | 289437007.0 | Finding of fetal heart rate | _Portio_ → `Observation.status` (594, tanpa BQ) |
| 40 | 595–604 | Observation | 248910006.0 | Uterine cervix finding | – |
| 41 | 605–621 | Observation | 365662002.0 | Finding of amniotic fluid appearance | _Ketuban_ → `Observation.valueCodeableConcept.coding` (607, tanpa BQ)<br>_Hodge_ → `Observation.identifier.value` (621, tanpa BQ) |
| 42 | 622–635 | Observation | 249111004.0 | Engagement of head | _Inspekulo_ → `Observation.status` (635, tanpa BQ) |
| 43 | 636–648 | Observation | 32750006.0 | Inspection | _Keterangan Inspekulo_ → `Observation.note.text` (647, tanpa BQ)<br>_Pemeriksaan Lakmus Air Ketuban_ → `Observation.status` (648, tanpa BQ) |
| 44 | 649–660 | Observation | 424679001.0 | pH measurement, vaginal fluid | _Keterangan Pemeriksaan Lakmus Air Ketuban_ → `Observation.note.text` (660, tanpa BQ) |
| 45 | 662–672 | Procedure | 387672006.0 | Cardiotochogram | _Pemeriksaan Cardiotocography (CTG)_ → `Procedure.category.coding` (662, tanpa BQ) |
| 46 | 673–683 | Observation | 251666009.0 | Cardiotochogram finding | _Keterangan Pemeriksaan Cardiotocography (CTG)_ → `Observation.valueString` (676, tanpa BQ) |
| 47 | 684–694 | Procedure | 88.78 | Diagnostic ultrasound of gravid uterus | _USG_ → `Procedure.category.coding` (684, tanpa BQ) |
| 48 | 695–705 | Observation | 11525-3 | US for pregnancy | _Keterangan USG_ → `Observation.valueString` (698, tanpa BQ) |
| 49 | 706–718 | Observation | 243787009 | Antenatal screening | _Laboratorium_ → `Observation.dataAbsentReason` (709, tanpa BQ)<br>_Keterangan Laboratorium_ → `Observation.note.text` (718, tanpa BQ) |
| 50 | 719–727 | Condition | 404684003.0 | Clinical finding | _Masalah Kesehatan_ → `Condition.clinicalStatus.coding` (719, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 37 |
| Condition | 4 |
| EpisodeOfCare | 2 |
| Procedure | 2 |
| Patient | 1 |
| Practitioner | 1 |
| Encounter | 1 |
| Immunization | 1 |
| MedicationStatement | 1 |
| **Total** | **50** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 103 | Condition | `Condition.code.coding` | 1255917009.0 | Maternal perinatal care | http://snomed.info/sct |
| 2 | 106 | Condition | `Condition.code.coding` | 134435003.0 | Routine antenatal care | http://snomed.info/sct |
| 3 | 109 | Condition | `Condition.code.coding` | Z39.2 | Routine postpartum follow-up | http://hl7.org/fhir/sid/icd-10 |
| 4 | 135 | EpisodeOfCare | `EpisodeOfCare.type.coding` | ANC | Antenatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 5 | 147 | EpisodeOfCare | `EpisodeOfCare.type.coding` | PNC | Postnatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 6 | 154 | Condition | `Condition.code.coding` | 404684003.0 | Clinical finding | http://snomed.info/sct |
| 7 | 163 | Observation | `Observation.code.coding` | 11996-6 | [#] Pregnancies | http://loinc.org |
| 8 | 164 | Observation | `Observation.code.coding` | ANC.B6.DE24 | Number of pregnancies (gravida) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 9 | 175 | Observation | `Observation.code.coding` | 11977-6 | [#] Parity | http://loinc.org |
| 10 | 176 | Observation | `Observation.code.coding` | ANC.B6.DE32 | Parity | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 11 | 187 | Observation | `Observation.code.coding` | 69043-8 | Other pregnancy outcomes # | http://loinc.org |
| 12 | 188 | Observation | `Observation.code.coding` | ANC.B6.DE25 | Number of miscarriages and/or abortions | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 13 | 199 | Observation | `Observation.code.coding` | 726001007.0 | Past pregnancy history of live birth | http://snomed.info/sct |
| 14 | 212 | Immunization | `Immunization.vaccineCode` | VG139 | Td | http://sys-ids.kemkes.go.id/kfa |
| 15 | 231 | Observation | `Observation.code.coding` | 8665-2 | Last menstrual period start date | http://loinc.org |
| 16 | 232 | Observation | `Observation.code.coding` | ANC.B6.DE14 | Last menstrual period (LMP) date | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 17 | 243 | Observation | `Observation.code.coding` | 18185-9 | Gestational age | http://loinc.org |
| 18 | 244 | Observation | `Observation.code.coding` | ANC.B6.DE17 | Gestational age | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 19 | 255 | Observation | `Observation.code.coding` | 11778-8 | Delivery date Estimated | http://loinc.org |
| 20 | 256 | Observation | `Observation.code.coding` | ANC.B6.DE22 | Expected date of delivery (EDD) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 21 | 267 | Observation | `Observation.code.coding` | 420209000.0 | History of contraceptive usage | http://snomed.info/sct |
| 22 | 268 | Observation | `Observation.valueCodeableConcept.coding` | 161772002.0 | History of oral contraceptive usage | http://snomed.info/sct |
| 23 | 269 | Observation | `Observation.valueCodeableConcept.coding` | 473093002.0 | History of use of depot contraception | http://snomed.info/sct |
| 24 | 270 | Observation | `Observation.valueCodeableConcept.coding` | 161773007.0 | History of intrauterine contraceptive device usage | http://snomed.info/sct |
| 25 | 271 | Observation | `Observation.valueCodeableConcept.coding` | 267020005.0 | History of tubal ligation | http://snomed.info/sct |
| 26 | 272 | Observation | `Observation.valueCodeableConcept.coding` | 473387004.0 | Never used contraception | http://snomed.info/sct |
| 27 | 282 | Observation | `Observation.code.coding` | SP000644 | Komplikasi KB Sebelumnya | http://terminology.kemkes.go.id/sp |
| 28 | 295 | Observation | `Observation.code.coding` | SP000645 | Alasan Berhenti KB | http://terminology.kemkes.go.id/sp |
| 29 | 306 | Condition | `Condition.code.coding` | 56728002.0 | Chronic cervicitis | http://snomed.info/sct |
| 30 | 307 | Condition | `Condition.code.coding` | 129103003.0 | Endometriosis | http://snomed.info/sct |
| 31 | 308 | Condition | `Condition.code.coding` | 6738008.0 | Female infertility | http://snomed.info/sct |
| 32 | 309 | Condition | `Condition.code.coding` | 371973000.0 | Malignant neoplasm of uterus | http://snomed.info/sct |
| 33 | 310 | Condition | `Condition.code.coding` | 1156875002.0 | Myoma | http://snomed.info/sct |
| 34 | 311 | Condition | `Condition.code.coding` | 8098009.0 | Sexually transmitted infectious disease | http://snomed.info/sct |
| 35 | 312 | Condition | `Condition.code.coding` | 65576009.0 | Polyp of cervix | http://snomed.info/sct |
| 36 | 313 | Condition | `Condition.code.coding` | 267011001.0 | Gynecological history | http://snomed.info/sct |
| 37 | 333 | Observation | `Observation.code.coding` | 72166-2 | Tobacco smoking status | http://loinc.org |
| 38 | 334 | Observation | `Observation.valueCodeableConcept.coding` | 8392000.0 | Non-smoker | http://snomed.info/sct |
| 39 | 335 | Observation | `Observation.valueCodeableConcept.coding` | 43381005.0 | Passive smoker | http://snomed.info/sct |
| 40 | 336 | Observation | `Observation.valueCodeableConcept.coding` | 77176002.0 | Smoker | http://snomed.info/sct |
| 41 | 347 | Observation | `Observation.code.coding` | 11331-6 | History of Alcohol use | http://loinc.org |
| 42 | 348 | Observation | `Observation.valueCodeableConcept.coding` | 105542008.0 | Non - drinker | http://snomed.info/sct |
| 43 | 349 | Observation | `Observation.valueCodeableConcept.coding` | 219006.0 | Current drinker | http://snomed.info/sct |
| 44 | 360 | Observation | `Observation.code.coding` | 9269-2 | Glasgow coma score total | http://loinc.org |
| 45 | 372 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 46 | 373 | Observation | `Observation.code.coding` | ANC.B8.DE17 | Systolic blood pressure | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 47 | 385 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://loinc.org |
| 48 | 386 | Observation | `Observation.code.coding` | ANC.B8.DE19 | Diastolic blood pressure | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 49 | 398 | Observation | `Observation.code.coding` | 8867-4 | Heart Rate | http://loinc.org |
| 50 | 399 | Observation | `Observation.code.coding` | ANC.B8.DE36 | Pulse rate | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 51 | 411 | Observation | `Observation.code.coding` | 9279-1 | Respiratory rate | http://loinc.org |
| 52 | 412 | Observation | `Observation.code.coding` | ANC.SS.DE2 | Pernapasan | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 53 | 425 | Observation | `Observation.code.coding` | 8310-5 | Body temperature | http://loinc.org |
| 54 | 426 | Observation | `Observation.code.coding` | ANC.B8.DE34 | Body temperature | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 55 | 438 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 56 | 439 | Observation | `Observation.code.coding` | ANC.B8.DE3 | Current weight | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 57 | 451 | Observation | `Observation.code.coding` | 8302-2 | Body height | http://loinc.org |
| 58 | 452 | Observation | `Observation.code.coding` | ANC.B8.DE1 | Height | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 59 | 464 | Observation | `Observation.code.coding` | 39156-5 | Body mass index (BMI) [Ratio] | http://loinc.org |
| 60 | 476 | Observation | `Observation.code.coding` | 284473002.0 | Mid upper arm circumference | http://snomed.info/sct |
| 61 | 477 | Observation | `Observation.code.coding` | ANC.SS.DE3 | Lingkar Lengan Atas (LILA) | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 62 | 486 | Observation | `Observation.interpretation` | OI000018 | Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 63 | 487 | Observation | `Observation.interpretation` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 64 | 488 | Observation | `Observation.interpretation` | OI000035 | Risiko Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 65 | 491 | Observation | `Observation.code.coding` | 11881-0 | Uterus Fundal height Tape measure | http://loinc.org |
| 66 | 492 | Observation | `Observation.code.coding` | ANC.B8.DE105 | Symphysis-fundal height | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 67 | 504 | Observation | `Observation.code.coding` | 89087-1 | Fetal Body weight Estimated | http://loinc.org |
| 68 | 505 | Observation | `Observation.code.coding` | ANC.SS.DE1 | Taksiran Berat Janin (TBJ) | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 69 | 518 | Observation | `Observation.code.coding` | 72155-5 | Position in womb Fetus [RHEA] | http://loinc.org |
| 70 | 519 | Observation | `Observation.valueCodeableConcept.coding` | 1209182005.0 | Cephalic fetal presentation | http://snomed.info/sct |
| 71 | 520 | Observation | `Observation.valueCodeableConcept.coding` | 288203005.0 | Transverse/oblique lie | http://snomed.info/sct |
| 72 | 521 | Observation | `Observation.valueCodeableConcept.coding` | 6096002.0 | Breech presentation | http://snomed.info/sct |
| 73 | 522 | Observation | `Observation.valueCodeableConcept.coding` | 8017000.0 | Face presentation | http://snomed.info/sct |
| 74 | 523 | Observation | `Observation.valueCodeableConcept.coding` | 249097002.0 | Footling breech presentation | http://snomed.info/sct |
| 75 | 524 | Observation | `Observation.valueCodeableConcept.coding` | 124736009.0 | Compound presentation | http://snomed.info/sct |
| 76 | 535 | Observation | `Observation.code.coding` | 249111004.0 | Engagement of head | http://snomed.info/sct |
| 77 | 536 | Observation | `Observation.valueCodeableConcept.coding` | 249112006.0 | Head engaged | http://snomed.info/sct |
| 78 | 538 | Observation | `Observation.valueCodeableConcept.coding` | 62098001.0 | Head not engaged | http://snomed.info/sct |
| 79 | 549 | Observation | `Observation.code.coding` | 249120008.0 | Onset of labor first stage | http://snomed.info/sct |
| 80 | 558 | Observation | `Observation.component.code.coding` | 364270005.0 | Frequency of uterine contraction | http://snomed.info/sct |
| 81 | 561 | Observation | `Observation.component.code.coding` | 398143009.0 | Uterine contraction monitoring | http://snomed.info/sct |
| 82 | 562 | Observation | `Observation.component.valueCodeableConcept.coding` | 289719005.0 | Strong uterine contractions | http://snomed.info/sct |
| 83 | 563 | Observation | `Observation.component.valueCodeableConcept.coding` | 289716003.0 | Moderate uterine contractions | http://snomed.info/sct |
| 84 | 564 | Observation | `Observation.component.valueCodeableConcept.coding` | 289715004.0 | Mild uterine contractions | http://snomed.info/sct |
| 85 | 565 | Observation | `Observation.component.code.coding` | 364274001.0 | Duration of uterine contraction | http://snomed.info/sct |
| 86 | 570 | Observation | `Observation.code.coding` | 55283-6 | Fetal Heart rate | http://loinc.org |
| 87 | 571 | Observation | `Observation.code.coding` | ANC.B8.DE107 | Fetal heart rate | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 88 | 584 | Observation | `Observation.code.coding` | 289437007.0 | Finding of fetal heart rate | http://snomed.info/sct |
| 89 | 585 | Observation | `Observation.valueCodeableConcept.coding` | 289441006.0 | Normal fetal heart rate | http://snomed.info/sct |
| 90 | 586 | Observation | `Observation.valueCodeableConcept.coding` | 312668007.0 | Abnormal fetal heart rate | http://snomed.info/sct |
| 91 | 596 | Observation | `Observation.code.coding` | 248910006.0 | Uterine cervix finding | http://loinc.org |
| 92 | 606 | Observation | `Observation.code.coding` | 365662002.0 | Finding of amniotic fluid appearance | http://snomed.info/sct |
| 93 | 607 | Observation | `Observation.valueCodeableConcept.coding` | 168090003.0 | Amniotic fluid clear | http://snomed.info/sct |
| 94 | 608 | Observation | `Observation.valueCodeableConcept.coding` | 408781009.0 | Straw colored amniotic fluid | http://snomed.info/sct |
| 95 | 609 | Observation | `Observation.valueCodeableConcept.coding` | 249134008.0 | Bloodstained liquor | http://snomed.info/sct |
| 96 | 610 | Observation | `Observation.valueCodeableConcept.coding` | 168092006.0 | Amniotic fluid -meconium stain | http://snomed.info/sct |
| 97 | 623 | Observation | `Observation.code.coding` | 249111004.0 | Engagement of head | http://snomed.info/sct |
| 98 | 624 | Observation | `Observation.valueCodeableConcept.coding` | 249112006.0 | Head engaged | http://snomed.info/sct |
| 99 | 626 | Observation | `Observation.valueCodeableConcept.coding` | 62098001.0 | Head not engaged | http://snomed.info/sct |
| 100 | 637 | Observation | `Observation.code.coding` | 32750006.0 | Inspection | http://snomed.info/sct |
| 101 | 639 | Observation | `Observation.dataAbsentReason.coding` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 102 | 650 | Observation | `Observation.code.coding` | 424679001.0 | pH measurement, vaginal fluid | http://snomed.info/sct |
| 103 | 652 | Observation | `Observation.dataAbsentReason.coding` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 104 | 663 | Procedure | `Procedure.code.coding` | 387672006.0 | Cardiotochogram | http://snomed.info/sct |
| 105 | 675 | Observation | `Observation.code.coding` | 251666009.0 | Cardiotochogram finding | http://snomed.info/sct |
| 106 | 685 | Procedure | `Procedure.code.coding` | 88.78 | Diagnostic ultrasound of gravid uterus | http://hl7.org/fhir/sid/icd-9-cm |
| 107 | 697 | Observation | `Observation.code.coding` | 11525-3 | US for pregnancy | http://loinc.org |
| 108 | 708 | Observation | `Observation.code.coding` | 243787009 | Antenatal screening | http://loinc.org |
| 109 | 709 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 110 | 721 | Condition | `Condition.code.coding` | 404684003.0 | Clinical finding | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 56 |
| http://loinc.org | 24 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 14 |
| http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes | 3 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 3 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 2 |
| http://terminology.kemkes.go.id/sp | 2 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 2 |
| http://hl7.org/fhir/sid/icd-10 | 1 |
| http://sys-ids.kemkes.go.id/kfa | 1 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 1 |
| http://hl7.org/fhir/sid/icd-9-cm | 1 |
| **Total** | **110** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 35 | – | Nama Faskes | Organization | `Organization.name` |
| 208 | – | Status Imunisasi TT | – | `` |
