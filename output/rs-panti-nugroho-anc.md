# Output Form: SIM RS Panti Nugroho ANC

Sumber: `mapping/phdt-data-dictionary-rs-panti-nugroho-anc.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-rs-panti-nugroho-anc.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 31 |
| Code (`jumlah code` = 1) | 77 |
| Code unik (code + CodeSystem) | 64 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 11 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–27 | Patient | – | – | _Nama Pasien_ → `Patient.name.text` (2, tanpa BQ)<br>_No Ktp_ → `Patient.identifier.value` (5, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (7, tanpa BQ)<br>_No Hp_ → `Patient.telecom.value` (10, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (11, tanpa BQ)<br>_Alamat Domisili_ → `Patient.address.use` (12, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (18, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (21, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.extension.valueCode` (24, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.extension.valueCode` (27, tanpa BQ) |
| 2 | 70–75 | PractitionerRole | – | – | _Jabatan Pencatat_ → `PractitionerRole.code.coding` (72, tanpa BQ)<br>_Jabatan Pencatat_ → `PractitionerRole.code.coding` (73, tanpa BQ)<br>_Jabatan Pemeriksa_ → `PractitionerRole.code.coding` (74, tanpa BQ) |
| 3 | 76–103 | Practitioner | – | – | _No Ktp Pencatat_ → `Practitioner.identifier.value` (78, tanpa BQ)<br>_Nama Pencatat_ → `Practitioner.name` (80, tanpa BQ)<br>_No Ktp Pemeriksa_ → `Practitioner.identifier.value` (83, tanpa BQ)<br>_Nama Pemeriksa_ → `Practitioner.name` (85, tanpa BQ)<br>_Jenis Kelamin Pemeriksa_ → `Practitioner.gender` (86, tanpa BQ)<br>_Nama Provinsi_ → `Practitioner.address.extension.extension.valueCode` (93, tanpa BQ)<br>_Nama Kabupaten_ → `Practitioner.address.extension.extension.valueCode` (96, tanpa BQ)<br>_Nama Kecamatan_ → `Practitioner.address.extension.extension.valueCode` (99, tanpa BQ)<br>_Nama Desa_ → `Practitioner.address.extension.extension.valueCode` (102, tanpa BQ) |
| 4 | 104–111 | EpisodeOfCare | ANC | Antenatal Care | – |
| 5 | 112–115 | Encounter | – | – | _Tanggal ANC_ → `Encounter.period.start` (112, tanpa BQ) |
| 6 | 116–118 | Condition | – | – | – |
| 7 | 129–142 | Observation | 8665-2 | Last menstrual period start date | _HPHT_ → `Observation.valueDateTime` (133, tanpa BQ) |
| 8 | 143–155 | Observation | 3401000175105 | Total number of prenatal care visits | – |
| 9 | 156–169 | Observation | SP000132 | Memiliki Buku KIA | _Kepemilikan Buku KIA_ → `Observation.valueBoolean` (159, tanpa BQ) |
| 10 | 170–184 | Observation | 8302-2 | Body height | _Tinggi Badan_ → `Observation.valueQuantity.value` (174, tanpa BQ) |
| 11 | 185–199 | Observation | 29463-7 | Body weight | _Berat Badan_ → `Observation.valueQuantity.value` (189, tanpa BQ) |
| 12 | 200–231 | Observation | 8480-6 | Systolic blood pressure | _Tekanan darah sistol_ → `Observation.valueQuantity.value` (204, tanpa BQ)<br>_LILA_ → `Observation.status` (215, tanpa BQ)<br>_Status Gizi_ → `Observation.interpretation` (229, tanpa BQ) |
| 13 | 232–246 | Observation | 8462-4 | Diastolic blood pressure | _Tekanan darah diastol_ → `Observation.valueQuantity.value` (236, tanpa BQ) |
| 14 | 247–270 | Observation | 11881-0 | Uterus Fundal height Tape measure | _TFU_ → `Observation.valueQuantity.value` (250, tanpa BQ) |
| 15 | 271–292 | Immunization | – | – | _Status Imunisasi TT_ → `Immunization.status` (271, tanpa BQ) |
| 16 | 293–305 | Immunization | – | – | – |
| 17 | 306–318 | Observation | SP000001 | Skrining Imunisasi Tetanus Toksoid | – |
| 18 | 319–337 | Immunization | – | – | _Imunisasi TT Saat Ini_ → `Immunization.status` (319, tanpa BQ) |
| 19 | 338–353 | Observation | 55283-6 | Fetal Heart rate | _DJJ_ → `Observation.valueQuantity.value` (342, tanpa BQ) |
| 20 | 354–370 | Observation | 72155-5 | Position in womb Fetus [RHEA] | _Presentasi Janin_ → `Observation.valueCodeableConcept.coding` (358, tanpa BQ) |
| 21 | 371–383 | Procedure | 88.78 | Diagnostic ultrasound of gravid uterus | _Pemeriksaan USG_ → `Procedure.category.coding` (371, tanpa BQ) |
| 22 | 384–401 | Condition | 34842007 | Antepartum hemorrhage | _Komplikasi Kehamilan_ → `Condition.clinicalStatus.coding` (384, tanpa BQ) |
| 23 | 402–435 | MedicationRequest | 92000653 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula | _Jumlah TTD Yang Diterima_ → `MedicationRequest.contained.resourceType` (402, tanpa BQ) |
| 24 | 436–467 | MedicationDispense | 93015491 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | – |
| 25 | 468–476 | Observation | SP000007 | Tatalaksana Anemia | _Tatalaksana Anemia_ → `Observation.valueCodeableConcept.coding` (471, tanpa BQ) |
| 26 | 478–502 | Observation | SP000010 | Skrining Hipertensi dalam Kehamilan | _Skrining pre eklamsia_ → `Observation.valueCodeableConcept.coding` (491, tanpa BQ) |
| 27 | 503–511 | Observation | SP000012 | Tatalaksana Pre Eklampsia | _Tatalaksana Pre Eklamsia_ → `Observation.component.valueString` (510, tanpa BQ) |
| 28 | 513–527 | Observation | SP000014 | Tatalaksana KEK | _Tatalaksana KEK_ → `Observation.valueCodeableConcept.coding` (526, tanpa BQ) |
| 29 | 529–557 | Observation | SP000015 | Risiko Masalah Kesehatan | _Risiko Kesehatan Lain_ → `Observation.status` (539, tanpa BQ) |
| 30 | 558–562 | Procedure | 385892002 | Mental health screening | _Skrinning Keswa_ → `Procedure.category.coding` (558, tanpa BQ) |
| 31 | 563–571 | Observation | – | – | – |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 17 |
| Immunization | 3 |
| Condition | 2 |
| Procedure | 2 |
| Patient | 1 |
| PractitionerRole | 1 |
| Practitioner | 1 |
| EpisodeOfCare | 1 |
| Encounter | 1 |
| MedicationRequest | 1 |
| MedicationDispense | 1 |
| **Total** | **31** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 72 | PractitionerRole | `PractitionerRole.code.coding` | 309453006 | Registered midwife | http://snomed.info/sct |
| 2 | 73 | PractitionerRole | `PractitionerRole.code.coding` | 224535009 | Registered nurse | http://snomed.info/sct |
| 3 | 74 | PractitionerRole | `PractitionerRole.code.coding` | 309367003 | Obstetrician and gynecologist | http://snomed.info/sct |
| 4 | 108 | EpisodeOfCare | `EpisodeOfCare.type.coding` | ANC | Antenatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 5 | 131 | Observation | `Observation.code.coding` | 8665-2 | Last menstrual period start date | http://loinc.org |
| 6 | 132 | Observation | `Observation.code.coding` | ANC.B6.DE14 | Last menstrual period (LMP) date | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 7 | 145 | Observation | `Observation.code.coding` | 3401000175105 | Total number of prenatal care visits | http://snomed.info/sct |
| 8 | 158 | Observation | `Observation.code.coding` | SP000132 | Memiliki Buku KIA | http://terminology.kemkes.go.id/sp |
| 9 | 172 | Observation | `Observation.code.coding` | 8302-2 | Body height | http://loinc.org |
| 10 | 173 | Observation | `Observation.code.coding` | ANC.B8.DE1 | Height | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 11 | 187 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 12 | 188 | Observation | `Observation.code.coding` | ANC.B8.DE3 | Current weight | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 13 | 202 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 14 | 203 | Observation | `Observation.code.coding` | ANC.B8.DE17 | Systolic blood pressure | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 15 | 217 | Observation | `Observation.code.coding` | 284473002 | Mid upper arm circumference | http://snomed.info/sct |
| 16 | 218 | Observation | `Observation.code.coding` | ANC.SS.DE3 | Lingkar Lengan Atas (LILA) | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 17 | 229 | Observation | `Observation.interpretation` | OI000018 | Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 18 | 230 | Observation | `Observation.interpretation` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 19 | 231 | Observation | `Observation.interpretation` | OI000035 | Risiko Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 20 | 234 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://loinc.org |
| 21 | 235 | Observation | `Observation.code.coding` | ANC.B8.DE19 | Diastolic blood pressure | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 22 | 249 | Observation | `Observation.code.coding` | 11881-0 | Uterus Fundal height Tape measure | http://loinc.org |
| 23 | 252 | Observation | `Observation.dataAbsentReason` | not-performed | - | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 24 | 273 | Immunization | `Immunization.vaccineCode` | VG139 | Td | http://sys-ids.kemkes.go.id/kfa |
| 25 | 293 | Immunization | `Immunization.vaccineCode` | VG139 | Td | http://sys-ids.kemkes.go.id/kfa |
| 26 | 308 | Observation | `Observation.code.coding` | SP000001 | Skrining Imunisasi Tetanus Toksoid | http://terminology.kemkes.go.id/sp |
| 27 | 309 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 28 | 321 | Immunization | `Immunization.vaccineCode` | VG139 | Td | http://sys-ids.kemkes.go.id/kfa |
| 29 | 340 | Observation | `Observation.code.coding` | 55283-6 | Fetal Heart rate | http://loinc.org |
| 30 | 341 | Observation | `Observation.code.coding` | ANC.B8.DE107 | Fetal heart rate | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 31 | 356 | Observation | `Observation.code.coding` | 72155-5 | Position in womb Fetus [RHEA] | http://loinc.org |
| 32 | 357 | Observation | `Observation.code.coding` | ANC.B8.DE111 | Fetal presentation | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 33 | 358 | Observation | `Observation.valueCodeableConcept.coding` | 1209182005 | Cephalic fetal presentation | http://snomed.info/sct |
| 34 | 359 | Observation | `Observation.valueCodeableConcept.coding` | 288203005 | Transverse/oblique lie | http://snomed.info/sct |
| 35 | 360 | Observation | `Observation.valueCodeableConcept.coding` | 6096002 | Breech presentation | http://snomed.info/sct |
| 36 | 361 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 37 | 372 | Procedure | `Procedure.code.coding` | 88.78 | Diagnostic ultrasound of gravid uterus | http://hl7.org/fhir/sid/icd-9-cm |
| 38 | 386 | Condition | `Condition.code.coding` | 34842007 | Antepartum hemorrhage | http://snomed.info/sct |
| 39 | 387 | Condition | `Condition.code.coding` | 15938005 | Eclampsia | http://snomed.info/sct |
| 40 | 388 | Condition | `Condition.code.coding` | 398254007 | Pre-eclampsia | http://snomed.info/sct |
| 41 | 389 | Condition | `Condition.code.coding` | 386639001 | Termination of pregnancy | http://snomed.info/sct |
| 42 | 390 | Condition | `Condition.code.coding` | 40733004 | Infectious disease | http://snomed.info/sct |
| 43 | 391 | Condition | `Condition.code.coding` | 91302008 | Sepsis | http://snomed.info/sct |
| 44 | 392 | Condition | `Condition.code.coding` | 74964007 | Other | http://snomed.info/sct |
| 45 | 405 | MedicationRequest | `MedicationRequest.contained.code.coding` | 92000653 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula | http://sys-ids.kemkes.go.id/kf |
| 46 | 439 | MedicationDispense | `MedicationDispense.contained.code.coding` | 93015491 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | http://sys-ids.kemkes.go.id/kf |
| 47 | 470 | Observation | `Observation.code.coding` | SP000007 | Tatalaksana Anemia | http://terminology.kemkes.go.id/sp |
| 48 | 471 | Observation | `Observation.valueCodeableConcept.coding` | SP000008 | Pemberian Tablet Tambah Darah | http://terminology.kemkes.go.id/sp |
| 49 | 472 | Observation | `Observation.valueCodeableConcept.coding` | SP000009 | Pemberian Fe Parenteral | http://terminology.kemkes.go.id/sp |
| 50 | 473 | Observation | `Observation.valueCodeableConcept.coding` | 116859006 | Transfusion of blood product | http://snomed.info/sct |
| 51 | 474 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 52 | 476 | Observation | `Observation.valueCodeableConcept.coding` | 3457005 | Patient referral | http://snomed.info/sct |
| 53 | 478 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 54 | 490 | Observation | `Observation.code.coding` | SP000010 | Skrining Hipertensi dalam Kehamilan | http://terminology.kemkes.go.id/sp |
| 55 | 491 | Observation | `Observation.valueCodeableConcept.coding` | SP000011 | Tidak Pre Eklampsia/ Eklampsia | http://terminology.kemkes.go.id/sp |
| 56 | 492 | Observation | `Observation.valueCodeableConcept.coding` | 48194001 | Pregnancy-induced hypertension | http://snomed.info/sct |
| 57 | 493 | Observation | `Observation.interpretation.coding` | 12763006 | Blood pressure below reference range (finding) | http://snomed.info/sct |
| 58 | 505 | Observation | `Observation.code.coding` | SP000012 | Tatalaksana Pre Eklampsia | http://terminology.kemkes.go.id/sp |
| 59 | 506 | Observation | `Observation.component.code.coding` | 135840009 | Blood pressure monitoring | http://snomed.info/sct |
| 60 | 507 | Observation | `Observation.component.code.coding` | 308116003 | Antihypertensive therapy | http://snomed.info/sct |
| 61 | 508 | Observation | `Observation.component.code.coding` | SP000013 | Pemberian MgSO4 | http://terminology.kemkes.go.id/sp |
| 62 | 509 | Observation | `Observation.component.code.coding` | 74964007 | Other | http://snomed.info/sct |
| 63 | 511 | Observation | `Observation.component.code.coding` | 3457005 | Patient referral | http://snomed.info/sct |
| 64 | 513 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 65 | 525 | Observation | `Observation.code.coding` | SP000014 | Tatalaksana KEK | http://terminology.kemkes.go.id/sp |
| 66 | 526 | Observation | `Observation.valueCodeableConcept.coding` | 435591000124104 | Nutrition supplement therapy | http://snomed.info/sct |
| 67 | 527 | Observation | `Observation.valueCodeableConcept.coding` | 3457005 | Patient referral | http://snomed.info/sct |
| 68 | 529 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed |  |
| 69 | 541 | Observation | `Observation.code.coding` | SP000015 | Risiko Masalah Kesehatan | http://terminology.kemkes.go.id/sp |
| 70 | 542 | Observation | `Observation.component.code.coding` | 40733004 | Infectious disease | http://snomed.info/sct |
| 71 | 543 | Observation | `Observation.component.code.coding` | 73211009 | Diabetes mellitus | http://snomed.info/sct |
| 72 | 544 | Observation | `Observation.component.code.coding` | 414916001 | Obesity | http://snomed.info/sct |
| 73 | 545 | Observation | `Observation.component.code.coding` | 56717001 | Tuberculosis | http://snomed.info/sct |
| 74 | 546 | Observation | `Observation.component.code.coding` | 56265001 | Heart disease | http://snomed.info/sct |
| 75 | 547 | Observation | `Observation.component.code.coding` | 74964007 | Other | http://snomed.info/sct |
| 76 | 548 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed |  |
| 77 | 559 | Procedure | `Procedure.code.coding` | 385892002 | Mental health screening | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 33 |
| http://terminology.kemkes.go.id/sp | 11 |
| http://loinc.org | 8 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 7 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 5 |
| http://sys-ids.kemkes.go.id/kfa | 3 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 2 |
| http://sys-ids.kemkes.go.id/kf | 2 |
|  | 2 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 1 |
| http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes | 1 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 1 |
| http://hl7.org/fhir/sid/icd-9-cm | 1 |
| **Total** | **77** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 30 | – | Faskes yang Melayani ANC | Organization | `Organization.type` |
| 31 | – | Nama Faskes | Organization | `Organization.name` |
| 35 | – | Nama Provinsi | Organization | `Organization.address.extension.extension.url` |
| 38 | – | Nama Kabupaten | Organization | `Organization.address.extension.extension.url` |
| 41 | – | Nama Kecamatan | Organization | `Organization.address.extension.extension.url` |
| 44 | – | Nama Desa | Organization | `Organization.address.extension.extension.url` |
| 46 | – | Tempat Pelayanan ANC | Location | `Location.identifier` |
| 54 | – | Nama Provinsi | Location | `Location.address.extension.extension.url` |
| 57 | – | Nama Kabupaten | Location | `Location.address.extension.extension.url` |
| 60 | – | Nama Kecamatan | Location | `Location.address.extension.extension.url` |
| 63 | – | Nama Desa | Location | `Location.address.extension.extension.url` |
