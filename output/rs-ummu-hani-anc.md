# Output Form: SIM RS Ummu Hani ANC

Sumber: `mapping/phdt-data-dictionary-rs-ummu-hani-anc.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-rs-ummu-hani-anc.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 23 |
| Code (`jumlah code` = 1) | 49 |
| Code unik (code + CodeSystem) | 44 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 3 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–27 | Patient | – | – | _Nama Ibu_ → `Patient.name.text` (2, tanpa BQ)<br>_NIK_ → `Patient.identifier.value` (6, tanpa BQ)<br>_No HP_ → `Patient.telecom` (7, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (10, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (11, tanpa BQ)<br>_Alamat Domisili_ → `Patient.address.line` (13, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (18, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (21, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.extension.valueCode` (24, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.extension.valueCode` (27, tanpa BQ) |
| 2 | 66–70 | Practitioner | – | – | _NIK_ → `Practitioner.identifier.value` (68, tanpa BQ)<br>_Nama Tenaga Kesehatan_ → `Practitioner.name.text` (70, tanpa BQ) |
| 3 | 71–78 | PractitionerRole | – | – | _Tenaga Pemeriksa_ → `PractitionerRole.code.coding` (75, tanpa BQ) |
| 4 | 79–83 | Practitioner | – | – | _NIK Pencatat_ → `Practitioner.identifier.value` (81, tanpa BQ)<br>_Nama Pencatat_ → `Practitioner.name.text` (83, tanpa BQ) |
| 5 | 84–91 | PractitionerRole | – | – | _Role Pencatat_ → `PractitionerRole.code.coding` (88, tanpa BQ) |
| 6 | 93–106 | Encounter | – | – | _Tanggal Kunjungan ANC_ → `Encounter.period.start` (101, tanpa BQ) |
| 7 | 107–114 | Condition | 134435003.0 | Routine antenatal care | _Kode ICD - Diagnosa_ → `Condition.clinicalStatus.coding` (107, tanpa BQ) |
| 8 | 125–133 | EpisodeOfCare | ANC | Antenatal Care | – |
| 9 | 134–145 | Observation | SP000132 | Memiliki Buku KIA | _Memiliki Buku KIA_ → `Observation.valueBoolean` (136, tanpa BQ) |
| 10 | 146–157 | Observation | 8665-2 | Last menstrual period start date | _HPHT_ → `Observation.valueDateTime` (150, tanpa BQ) |
| 11 | 158–170 | Observation | 8302-2 | Body height | _Tinggi Badan_ → `Observation.valueQuantity.value` (162, tanpa BQ) |
| 12 | 171–179 | Condition | 609496007.0 | Complication occurring during pregnancy | _Komplikasi_ → `Condition.clinicalStatus.coding` (171, tanpa BQ) |
| 13 | 180–198 | Immunization | – | – | _Riwayat Imunisasi TT_ → `Immunization.status` (180, tanpa BQ) |
| 14 | 199–214 | Observation | 18185-9 | Gestational age | _Usia Kehamilan (dalam minggu)_ → `Observation.valueQuantity.value` (203, tanpa BQ) |
| 15 | 215–227 | Observation | 29463-7 | Body weight | _Berat Badan (dalam kg)_ → `Observation.valueQuantity.value` (219, tanpa BQ) |
| 16 | 228–239 | Observation | 8480-6 | Systolic blood pressure | _Tekanan Darah Sistolik_ → `Observation.valueQuantity.value` (231, tanpa BQ) |
| 17 | 240–251 | Observation | 8462-4 | Diastolic blood pressure | _Tekanan Darah Diastolik_ → `Observation.valueQuantity.value` (243, tanpa BQ) |
| 18 | 252–263 | Observation | 284473002.0 | Mid upper arm circumference | _LiLA_ → `Observation.status` (252, tanpa BQ) |
| 19 | 264–278 | Observation | 883-9 | ABO group [Type] in Blood | _Lab : Golongan Darah_ → `Observation.valueCodeableConcept.coding` (268, tanpa BQ) |
| 20 | 279–291 | Observation | 55283-6 | Fetal Heart rate | _Denyut Jantung Janin_ → `Observation.valueQuantity.value` (283, tanpa BQ) |
| 21 | 292–308 | Observation | 72155-5 | Position in womb Fetus [RHEA] | _Presentasi Janin_ → `Observation.valueCodeableConcept.coding` (296, tanpa BQ) |
| 22 | 309–323 | Condition | 34842007.0 | Antepartum hemorrhage | _Komplikasi Kehamilan_ → `Condition.clinicalStatus.coding` (309, tanpa BQ) |
| 23 | 324–333 | Procedure | 88.78 | Diagnostic ultrasound of gravid uterus | _Dilakukan USG_ → `Procedure.category.coding` (324, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 11 |
| Condition | 3 |
| Practitioner | 2 |
| PractitionerRole | 2 |
| Patient | 1 |
| Encounter | 1 |
| EpisodeOfCare | 1 |
| Immunization | 1 |
| Procedure | 1 |
| **Total** | **23** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 75 | PractitionerRole | `PractitionerRole.code.coding` | 309453006.0 | Registered midwife | http://snomed.info/sct |
| 2 | 76 | PractitionerRole | `PractitionerRole.code.coding` | 309367003.0 | Obstetrician and gynecologist | http://snomed.info/sct |
| 3 | 77 | PractitionerRole | `PractitionerRole.code.coding` | 309343006.0 | Physician | http://snomed.info/sct |
| 4 | 78 | PractitionerRole | `PractitionerRole.code.coding` | 224535009.0 | Registered nurse | http://snomed.info/sct |
| 5 | 88 | PractitionerRole | `PractitionerRole.code.coding` | 309453006.0 | Registered midwife | http://snomed.info/sct |
| 6 | 89 | PractitionerRole | `PractitionerRole.code.coding` | 309367003.0 | Obstetrician and gynecologist | http://snomed.info/sct |
| 7 | 90 | PractitionerRole | `PractitionerRole.code.coding` | 309343006.0 | Physician | http://snomed.info/sct |
| 8 | 91 | PractitionerRole | `PractitionerRole.code.coding` | 224535009.0 | Registered nurse | http://snomed.info/sct |
| 9 | 109 | Condition | `Condition.code.coding` | 134435003.0 | Routine antenatal care | http://snomed.info/sct |
| 10 | 126 | EpisodeOfCare | `EpisodeOfCare.type.coding` | ANC | Antenatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 11 | 135 | Observation | `Observation.code.coding` | SP000132 | Memiliki Buku KIA | http://terminology.kemkes.go.id/sp |
| 12 | 148 | Observation | `Observation.code.coding` | 8665-2 | Last menstrual period start date | http://loinc.org |
| 13 | 149 | Observation | `Observation.code.coding` | ANC.B6.DE14 | Last menstrual period (LMP) date | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 14 | 160 | Observation | `Observation.code.coding` | 8302-2 | Body height | http://loinc.org |
| 15 | 161 | Observation | `Observation.code.coding` | ANC.B8.DE1 | Height | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 16 | 173 | Condition | `Condition.code.coding` | 609496007.0 | Complication occurring during pregnancy | http://snomed.info/sct |
| 17 | 183 | Immunization | `Immunization.vaccineCode` | VG139 | Td | http://sys-ids.kemkes.go.id/kfa |
| 18 | 201 | Observation | `Observation.code.coding` | 18185-9 | Gestational age | http://loinc.org |
| 19 | 202 | Observation | `Observation.code.coding` | ANC.B6.DE17 | Gestational age | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 20 | 205 | Observation | `Observation.component.code.coding` | 49052-4 | Gestational age in days | http://terminology.kemkes.go.id/sp |
| 21 | 217 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 22 | 218 | Observation | `Observation.code.coding` | ANC.B8.DE3 | Current weight | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 23 | 230 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 24 | 242 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://loinc.org |
| 25 | 254 | Observation | `Observation.code.coding` | 284473002.0 | Mid upper arm circumference | http://snomed.info/sct |
| 26 | 255 | Observation | `Observation.code.coding` | ANC.SS.DE3 | Lingkar Lengan Atas (LILA) | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 27 | 266 | Observation | `Observation.code.coding` | 883-9 | ABO group [Type] in Blood | http://loinc.org |
| 28 | 267 | Observation | `Observation.code.coding` | ANC.B9.DE24 | Blood type | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 29 | 268 | Observation | `Observation.valueCodeableConcept.coding` | LA19710-5 | Group A | http://loinc.org |
| 30 | 269 | Observation | `Observation.valueCodeableConcept.coding` | LA19709-7 | Group B | http://loinc.org |
| 31 | 270 | Observation | `Observation.valueCodeableConcept.coding` | LA19708-9 | Group O | http://loinc.org |
| 32 | 271 | Observation | `Observation.valueCodeableConcept.coding` | LA28449-9 | Group AB | http://loinc.org |
| 33 | 281 | Observation | `Observation.code.coding` | 55283-6 | Fetal Heart rate | http://loinc.org |
| 34 | 282 | Observation | `Observation.code.coding` | ANC.B8.DE107 | Fetal heart rate | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 35 | 294 | Observation | `Observation.code.coding` | 72155-5 | Position in womb Fetus [RHEA] | http://loinc.org |
| 36 | 295 | Observation | `Observation.code.coding` | ANC.B8.DE111 | Fetal presentation | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 37 | 296 | Observation | `Observation.valueCodeableConcept.coding` | 1209182005.0 | Cephalic fetal presentation | http://snomed.info/sct |
| 38 | 297 | Observation | `Observation.valueCodeableConcept.coding` | 6096002.0 | Breech presentation | http://snomed.info/sct |
| 39 | 298 | Observation | `Observation.valueCodeableConcept.coding` | 73161006.0 | Transverse lie | http://snomed.info/sct |
| 40 | 299 | Observation | `Observation.valueCodeableConcept.coding` | 63750008.0 | Oblique lie | http://snomed.info/sct |
| 41 | 300 | Observation | `Observation.valueCodeableConcept.coding` | SP000006 | Organ Tubuh Lainnya | http://terminology.kemkes.go.id/sp |
| 42 | 311 | Condition | `Condition.code.coding` | 34842007.0 | Antepartum hemorrhage | http://snomed.info/sct |
| 43 | 312 | Condition | `Condition.code.coding` | 15938005.0 | Eclampsia | http://snomed.info/sct |
| 44 | 313 | Condition | `Condition.code.coding` | 398254007.0 | Pre-eclampsia | http://snomed.info/sct |
| 45 | 314 | Condition | `Condition.code.coding` | 386639001.0 | Termination of pregnancy | http://snomed.info/sct |
| 46 | 315 | Condition | `Condition.code.coding` | 40733004.0 | Infectious disease | http://snomed.info/sct |
| 47 | 316 | Condition | `Condition.code.coding` | 91302008.0 | Sepsis | http://snomed.info/sct |
| 48 | 317 | Condition | `Condition.code.coding` | 609496007.0 | Complication occurring during pregnancy | http://snomed.info/sct |
| 49 | 325 | Procedure | `Procedure.code.coding` | 88.78 | Diagnostic ultrasound of gravid uterus | http://hl7.org/fhir/sid/icd-9-cm |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 22 |
| http://loinc.org | 13 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 7 |
| http://terminology.kemkes.go.id/sp | 3 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 1 |
| http://sys-ids.kemkes.go.id/kfa | 1 |
| http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes | 1 |
| http://hl7.org/fhir/sid/icd-9-cm | 1 |
| **Total** | **49** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 32 | – | Faskes yang Melayani ANC | Organization | `Organization.name` |
