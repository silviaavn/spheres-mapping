# Output Form: SIM RS MPH ANC

Sumber: `mapping/phdt-data-dictionary-rs-mph-anc.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-rs-mph-anc.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 33 |
| Code (`jumlah code` = 1) | 90 |
| Code unik (code + CodeSystem) | 75 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 11 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–27 | Patient | – | – | _Nama Ibu_ → `Patient.name.text` (2, tanpa BQ)<br>_NIK_ → `Patient.identifier.value` (6, tanpa BQ)<br>_No HP_ → `Patient.telecom` (7, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (10, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (11, tanpa BQ)<br>_Alamat Domisili_ → `Patient.address.line` (13, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (18, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (21, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.extension.valueCode` (24, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.extension.valueCode` (27, tanpa BQ) |
| 2 | 66–70 | Practitioner | – | – | _NIK_ → `Practitioner.identifier.value` (68, tanpa BQ)<br>_Nama Tenaga Kesehatan_ → `Practitioner.name.text` (70, tanpa BQ) |
| 3 | 71–80 | PractitionerRole | – | – | _Tenaga Pemeriksa_ → `PractitionerRole.code.coding` (75, tanpa BQ) |
| 4 | 81–85 | Practitioner | – | – | _NIK Pencatat_ → `Practitioner.identifier.value` (83, tanpa BQ)<br>_Nama Pencatat_ → `Practitioner.name.text` (85, tanpa BQ) |
| 5 | 86–94 | PractitionerRole | – | – | _Role Pencatat_ → `PractitionerRole.code.coding` (90, tanpa BQ) |
| 6 | 96–109 | Encounter | – | – | _Tanggal Kunjungan ANC_ → `Encounter.period.start` (104, tanpa BQ) |
| 7 | 110–117 | Condition | 134435003 | Routine antenatal care | _Kode ICD - Diagnosa_ → `Condition.clinicalStatus.coding` (110, tanpa BQ) |
| 8 | 128–136 | EpisodeOfCare | ANC | Antenatal Care | – |
| 9 | 137–148 | Observation | SP000132 | Memiliki Buku KIA | _Memiliki Buku KIA_ → `Observation.valueBoolean` (139, tanpa BQ) |
| 10 | 149–160 | Observation | 8665-2 | Last menstrual period start date | _HPHT_ → `Observation.valueDateTime` (153, tanpa BQ) |
| 11 | 161–173 | Observation | 8302-2 | Body height | _Tinggi Badan_ → `Observation.valueQuantity.value` (165, tanpa BQ) |
| 12 | 174–182 | Condition | 609496007 | Complication occurring during pregnancy | _Komplikasi_ → `Condition.clinicalStatus.coding` (174, tanpa BQ) |
| 13 | 183–195 | Observation | 11881-0 | Uterus Fundal height Tape measure | _Tinggi Fundus Uteri (TFU)_ → `Observation.valueQuantity.value` (187, tanpa BQ) |
| 14 | 196–214 | Immunization | – | – | _Riwayat Imunisasi TT_ → `Immunization.status` (196, tanpa BQ) |
| 15 | 215–230 | Observation | 18185-9 | Gestational age | _Usia Kehamilan (dalam minggu)_ → `Observation.valueQuantity.value` (219, tanpa BQ) |
| 16 | 231–243 | Observation | 29463-7 | Body weight | _Berat Badan (dalam kg)_ → `Observation.valueQuantity.value` (235, tanpa BQ) |
| 17 | 244–255 | Observation | 8480-6 | Systolic blood pressure | _Tekanan Darah Sistolik_ → `Observation.valueQuantity.value` (247, tanpa BQ) |
| 18 | 256–267 | Observation | 8462-4 | Diastolic blood pressure | _Tekanan Darah Diastolik_ → `Observation.valueQuantity.value` (259, tanpa BQ) |
| 19 | 268–282 | Observation | 284473002 | Mid upper arm circumference | _LiLA_ → `Observation.status` (268, tanpa BQ)<br>_Status Gizi KEK/Tidak KEK_ → `Observation.interpretation` (280, tanpa BQ) |
| 20 | 283–297 | Observation | 883-9 | ABO group [Type] in Blood | _Lab : Golongan Darah_ → `Observation.valueCodeableConcept.coding` (287, tanpa BQ) |
| 21 | 298–310 | Observation | 55283-6 | Fetal Heart rate | _Denyut Jantung Janin_ → `Observation.valueQuantity.value` (302, tanpa BQ) |
| 22 | 311–328 | Observation | 72155-5 | Position in womb Fetus [RHEA] | _Presentasi Janin_ → `Observation.valueCodeableConcept.coding` (315, tanpa BQ) |
| 23 | 329–343 | Condition | 34842007 | Antepartum hemorrhage | _Komplikasi Kehamilan_ → `Condition.clinicalStatus.coding` (329, tanpa BQ) |
| 24 | 344–353 | Procedure | 88.78 | Diagnostic ultrasound of gravid uterus | _Dilakukan USG_ → `Procedure.category.coding` (344, tanpa BQ) |
| 25 | 354–364 | Observation | 243787009 | Antenatal screening | _Pemeriksaan Laboratorium_ → `Observation.valueString` (357, tanpa BQ) |
| 26 | 365–398 | MedicationRequest | 92000653 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula | _Jumlah TTD Diterima_ → `MedicationRequest.contained.resourceType` (365, tanpa BQ) |
| 27 | 399–430 | MedicationDispense | 93015491 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | – |
| 28 | 431–439 | Observation | SP000007 | Tatalaksana Anemia | _Tatalaksana Anemia_ → `Observation.valueCodeableConcept.coding` (434, tanpa BQ) |
| 29 | 441–462 | Observation | SP000010 | Skrining Hipertensi dalam Kehamilan | _Pre Eklampsia_ → `Observation.valueCodeableConcept.coding` (451, tanpa BQ) |
| 30 | 463–481 | Observation | SP000012 | Tatalaksana Pre Eklampsia | _Tatalaksana Pre Eklampsia_ → `Observation.valueBoolean` (466, tanpa BQ) |
| 31 | 483–501 | Observation | SP000014 | Tatalaksana KEK | _Tatalaksana KEK_ → `Observation.valueBoolean` (494, tanpa BQ) |
| 32 | 503–538 | Observation | SP000015 | Risiko Masalah Kesehatan | _Risiko Masalah Kesehatan Lainnya_ → `Observation.valueBoolean` (513, tanpa BQ) |
| 33 | 539–550 | Procedure | 385892002 | Mental health screening | _Skrinning Keswa_ → `Procedure.category.coding` (539, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 18 |
| Condition | 3 |
| Practitioner | 2 |
| PractitionerRole | 2 |
| Procedure | 2 |
| Patient | 1 |
| Encounter | 1 |
| EpisodeOfCare | 1 |
| Immunization | 1 |
| MedicationRequest | 1 |
| MedicationDispense | 1 |
| **Total** | **33** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 75 | PractitionerRole | `PractitionerRole.code.coding` | 309453006 | Registered midwife | http://snomed.info/sct |
| 2 | 76 | PractitionerRole | `PractitionerRole.code.coding` | 309367003 | Obstetrician and gynecologist | http://snomed.info/sct |
| 3 | 77 | PractitionerRole | `PractitionerRole.code.coding` | 309343006 | Physician | http://snomed.info/sct |
| 4 | 78 | PractitionerRole | `PractitionerRole.code.coding` | 224535009 | Registered nurse | http://snomed.info/sct |
| 5 | 79 | PractitionerRole | `PractitionerRole.code.coding` | 224535009 | Registered nurse | http://snomed.info/sct |
| 6 | 90 | PractitionerRole | `PractitionerRole.code.coding` | 309453006 | Registered midwife | http://snomed.info/sct |
| 7 | 91 | PractitionerRole | `PractitionerRole.code.coding` | 309367003 | Obstetrician and gynecologist | http://snomed.info/sct |
| 8 | 92 | PractitionerRole | `PractitionerRole.code.coding` | 309343006 | Physician | http://snomed.info/sct |
| 9 | 93 | PractitionerRole | `PractitionerRole.code.coding` | 224535009 | Registered nurse | http://snomed.info/sct |
| 10 | 94 | PractitionerRole | `PractitionerRole.code.coding` | 56542007 | Medical record administrator | http://snomed.info/sct |
| 11 | 112 | Condition | `Condition.code.coding` | 134435003 | Routine antenatal care | http://snomed.info/sct |
| 12 | 129 | EpisodeOfCare | `EpisodeOfCare.type.coding` | ANC | Antenatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 13 | 138 | Observation | `Observation.code.coding` | SP000132 | Memiliki Buku KIA | http://terminology.kemkes.go.id/sp |
| 14 | 151 | Observation | `Observation.code.coding` | 8665-2 | Last menstrual period start date | http://loinc.org |
| 15 | 152 | Observation | `Observation.code.coding` | ANC.B6.DE14 | Last menstrual period (LMP) date | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 16 | 163 | Observation | `Observation.code.coding` | 8302-2 | Body height | http://loinc.org |
| 17 | 164 | Observation | `Observation.code.coding` | ANC.B8.DE1 | Height | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 18 | 176 | Condition | `Condition.code.coding` | 609496007 | Complication occurring during pregnancy | http://snomed.info/sct |
| 19 | 185 | Observation | `Observation.code.coding` | 11881-0 | Uterus Fundal height Tape measure | http://loinc.org |
| 20 | 186 | Observation | `Observation.code.coding` | ANC.B8.DE105 | Symphysis-fundal height | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 21 | 199 | Immunization | `Immunization.vaccineCode` | VG139 | Td | http://sys-ids.kemkes.go.id/kfa |
| 22 | 217 | Observation | `Observation.code.coding` | 18185-9 | Gestational age | http://loinc.org |
| 23 | 218 | Observation | `Observation.code.coding` | ANC.B6.DE17 | Gestational age | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 24 | 221 | Observation | `Observation.component.code.coding` | 49052-4 | Gestational age in days | http://loinc.org |
| 25 | 233 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 26 | 234 | Observation | `Observation.code.coding` | ANC.B8.DE3 | Current weight | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 27 | 246 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 28 | 258 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://loinc.org |
| 29 | 270 | Observation | `Observation.code.coding` | 284473002 | Mid upper arm circumference | http://snomed.info/sct |
| 30 | 271 | Observation | `Observation.code.coding` | ANC.SS.DE3 | Lingkar Lengan Atas (LILA) | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 31 | 280 | Observation | `Observation.interpretation` | OI000018 | Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 32 | 281 | Observation | `Observation.interpretation` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 33 | 282 | Observation | `Observation.interpretation` | OI000035 | Risiko Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 34 | 285 | Observation | `Observation.code.coding` | 883-9 | ABO group [Type] in Blood | http://loinc.org |
| 35 | 286 | Observation | `Observation.code.coding` | ANC.B9.DE24 | Blood type | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 36 | 287 | Observation | `Observation.valueCodeableConcept.coding` | LA19710-5 | Group A | http://loinc.org |
| 37 | 288 | Observation | `Observation.valueCodeableConcept.coding` | LA19709-7 | Group B | http://loinc.org |
| 38 | 289 | Observation | `Observation.valueCodeableConcept.coding` | LA19708-9 | Group O | http://loinc.org |
| 39 | 290 | Observation | `Observation.valueCodeableConcept.coding` | LA28449-9 | Group AB | http://loinc.org |
| 40 | 300 | Observation | `Observation.code.coding` | 55283-6 | Fetal Heart rate | http://loinc.org |
| 41 | 301 | Observation | `Observation.code.coding` | ANC.B8.DE107 | Fetal heart rate | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 42 | 313 | Observation | `Observation.code.coding` | 72155-5 | Position in womb Fetus [RHEA] | http://loinc.org |
| 43 | 314 | Observation | `Observation.code.coding` | ANC.B8.DE111 | Fetal presentation | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 44 | 315 | Observation | `Observation.valueCodeableConcept.coding` | 1209182005 | Cephalic fetal presentation | http://snomed.info/sct |
| 45 | 316 | Observation | `Observation.valueCodeableConcept.coding` | 6096002 | Breech presentation | http://snomed.info/sct |
| 46 | 317 | Observation | `Observation.valueCodeableConcept.coding` | 73161006 | Transverse lie | http://snomed.info/sct |
| 47 | 318 | Observation | `Observation.valueCodeableConcept.coding` | 63750008 | Oblique lie | http://snomed.info/sct |
| 48 | 319 | Observation | `Observation.valueCodeableConcept.coding` | SP000006 | Organ Tubuh Lainnya | http://terminology.kemkes.go.id/sp |
| 49 | 321 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 50 | 331 | Condition | `Condition.code.coding` | 34842007 | Antepartum hemorrhage | http://snomed.info/sct |
| 51 | 332 | Condition | `Condition.code.coding` | 15938005 | Eclampsia | http://snomed.info/sct |
| 52 | 333 | Condition | `Condition.code.coding` | 398254007 | Pre-eclampsia | http://snomed.info/sct |
| 53 | 334 | Condition | `Condition.code.coding` | 386639001 | Termination of pregnancy | http://snomed.info/sct |
| 54 | 335 | Condition | `Condition.code.coding` | 40733004 | Infectious disease | http://snomed.info/sct |
| 55 | 336 | Condition | `Condition.code.coding` | 91302008 | Sepsis | http://snomed.info/sct |
| 56 | 337 | Condition | `Condition.code.coding` | 609496007 | Complication occurring during pregnancy | http://snomed.info/sct |
| 57 | 345 | Procedure | `Procedure.code.coding` | 88.78 | Diagnostic ultrasound of gravid uterus | http://hl7.org/fhir/sid/icd-9-cm |
| 58 | 356 | Observation | `Observation.code.coding` | 243787009 | Antenatal screening | http://loinc.org |
| 59 | 368 | MedicationRequest | `MedicationRequest.contained.code.coding` | 92000653 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula | http://sys-ids.kemkes.go.id/kf |
| 60 | 402 | MedicationDispense | `MedicationDispense.contained.code.coding` | 93015491 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | http://sys-ids.kemkes.go.id/kf |
| 61 | 433 | Observation | `Observation.code.coding` | SP000007 | Tatalaksana Anemia | http://terminology.kemkes.go.id/sp |
| 62 | 434 | Observation | `Observation.valueCodeableConcept.coding` | SP000008 | Pemberian Tablet Tambah Darah | http://terminology.kemkes.go.id/sp |
| 63 | 435 | Observation | `Observation.valueCodeableConcept.coding` | SP000009 | Pemberian Fe Parenteral | http://terminology.kemkes.go.id/sp |
| 64 | 436 | Observation | `Observation.valueCodeableConcept.coding` | 116859006 | Transfusion of blood product | http://snomed.info/sct |
| 65 | 437 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 66 | 439 | Observation | `Observation.valueCodeableConcept.coding` | 3457005 | Patient referral | http://snomed.info/sct |
| 67 | 450 | Observation | `Observation.code.coding` | SP000010 | Skrining Hipertensi dalam Kehamilan | http://terminology.kemkes.go.id/sp |
| 68 | 451 | Observation | `Observation.valueCodeableConcept.coding` | SP000011 | Tidak Pre Eklampsia/ Eklampsia | http://terminology.kemkes.go.id/sp |
| 69 | 452 | Observation | `Observation.valueCodeableConcept.coding` | 48194001 | Pregnancy-induced hypertension | http://snomed.info/sct |
| 70 | 453 | Observation | `Observation.valueCodeableConcept.coding` | 398254007 | Pre-eclampsia | http://snomed.info/sct |
| 71 | 454 | Observation | `Observation.valueCodeableConcept.coding` | 15938005 | Eclampsia | http://snomed.info/sct |
| 72 | 455 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 73 | 465 | Observation | `Observation.code.coding` | SP000012 | Tatalaksana Pre Eklampsia | http://terminology.kemkes.go.id/sp |
| 74 | 468 | Observation | `Observation.component.code.coding` | 135840009 | Blood pressure monitoring | http://snomed.info/sct |
| 75 | 471 | Observation | `Observation.component.code.coding` | 308116003 | Antihypertensive therapy | http://snomed.info/sct |
| 76 | 474 | Observation | `Observation.component.code.coding` | SP000013 | Pemberian MgSO4 | http://terminology.kemkes.go.id/sp |
| 77 | 477 | Observation | `Observation.component.code.coding` | 74964007 | Other | http://snomed.info/sct |
| 78 | 479 | Observation | `Observation.component.code.coding` | 3457005 | Patient referral | http://snomed.info/sct |
| 79 | 483 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 80 | 493 | Observation | `Observation.code.coding` | SP000014 | Tatalaksana KEK | http://terminology.kemkes.go.id/sp |
| 81 | 496 | Observation | `Observation.component.code.coding` | 435591000124104 | Nutrition supplement therapy | http://snomed.info/sct |
| 82 | 499 | Observation | `Observation.component.code.coding` | 3457005 | Patient referral | http://snomed.info/sct |
| 83 | 512 | Observation | `Observation.code.coding` | SP000015 | Risiko Masalah Kesehatan | http://terminology.kemkes.go.id/sp |
| 84 | 515 | Observation | `Observation.component.code.coding` | 40733004 | Infectious disease | http://snomed.info/sct |
| 85 | 518 | Observation | `Observation.component.code.coding` | 73211009 | Diabetes mellitus | http://snomed.info/sct |
| 86 | 521 | Observation | `Observation.component.code.coding` | 414916001 | Obesity | http://snomed.info/sct |
| 87 | 524 | Observation | `Observation.component.code.coding` | 56717001 | Tuberculosis | http://snomed.info/sct |
| 88 | 527 | Observation | `Observation.component.code.coding` | 56265001 | Heart disease | http://snomed.info/sct |
| 89 | 530 | Observation | `Observation.component.code.coding` | 74964007 | Other | http://snomed.info/sct |
| 90 | 540 | Procedure | `Procedure.code.coding` | 385892002 | Mental health screening | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 43 |
| http://loinc.org | 16 |
| http://terminology.kemkes.go.id/sp | 11 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 8 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 3 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 2 |
| http://sys-ids.kemkes.go.id/kf | 2 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 1 |
| http://sys-ids.kemkes.go.id/kfa | 1 |
| http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes | 1 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 1 |
| http://hl7.org/fhir/sid/icd-9-cm | 1 |
| **Total** | **90** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 32 | – | Faskes yang Melayani ANC | Organization | `Organization.name` |
