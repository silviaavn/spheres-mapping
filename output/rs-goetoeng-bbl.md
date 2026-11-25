# Output Form: SIM RS Goetoeng BBL

Sumber: `mapping/phdt-data-dictionary-rs-goetoeng-bbl.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-rs-goetoeng-bbl.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 68 |
| Code (`jumlah code` = 1) | 124 |
| Code unik (code + CodeSystem) | 47 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 14 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–26 | Patient | – | – | _Nama BBL_ → `Patient.name.text` (2, tanpa BQ)<br>_No KTP_ → `Patient.identifier.value` (5, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (7, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (9, tanpa BQ)<br>_Alamat Domisili_ → `Patient.address.use` (10, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (16, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (19, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.extension.valueCode` (23, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.extension.valueCode` (26, tanpa BQ) |
| 2 | 96–112 | Encounter | – | – | _DPJP_ → `Encounter.participant.individual.display` (104, tanpa BQ)<br>_Tanggal Masuk_ → `Encounter.period.start` (105, tanpa BQ)<br>_Tanggal Keluar_ → `Encounter.period.end` (106, tanpa BQ)<br>_Ruang_ → `Encounter.location.location.display` (108, tanpa BQ)<br>_Keterangan Rujuk_ → `Encounter.hospitalization.admitSource.coding` (120, tanpa BQ)<br>_TINDAK LANJUT_ → `Encounter.hospitalization.dischargeDisposition.coding` (151, tanpa BQ)<br>_KEADAAN PASIEN_ → `Encounter.hospitalization.dischargeDisposition.coding` (442, tanpa BQ) |
| 3 | 113–119 | Condition | Z00.1 | Routine child health examination | – |
| 4 | 156–164 | EpisodeOfCare | Neonate | Neonate | – |
| 5 | 165–181 | Coverage | – | – | _Cara Bayar_ → `Coverage.identifier` (165, tanpa BQ)<br>_KELAS_ → `Coverage.class.type.coding` (173, tanpa BQ) |
| 6 | 182–193 | Observation | 184061005 | Patient registration status | _P.BARU_ → `Observation.valueCodeableConcept.coding` (185, tanpa BQ) |
| 7 | 194–205 | Observation | 424144002 | Current chronological age | _Umur_ → `Observation.valueQuantity.value` (197, tanpa BQ) |
| 8 | 206–221 | Observation | SP000811 | Jalur Masuk Rawat Inap | _VIA_ → `Observation.valueCodeableConcept.coding` (209, tanpa BQ) |
| 9 | 222–243 | Condition | P22.0 | Respiratory distress syndrome of newborn | _DX1_ → `Condition.clinicalStatus.coding` (222, tanpa BQ)<br>_KODE1_ → `Condition.clinicalStatus.coding` (236, tanpa BQ) |
| 10 | 244–260 | Condition | P22.0 | Respiratory distress syndrome of newborn | _DX2_ → `Condition.clinicalStatus.coding` (253, tanpa BQ) |
| 11 | 261–280 | Condition | P23.9 | Congenital pneumonia, unspecified | _KODE2_ → `Condition.clinicalStatus.coding` (273, tanpa BQ) |
| 12 | 281–298 | Condition | P23.9 | Congenital pneumonia, unspecified | – |
| 13 | 299–309 | Procedure | 96.05 | Other intubation of respiratory tract | _Tindakan_ → `Procedure.status` (299, tanpa BQ)<br>_KODE ICD9_ → `Procedure.category.coding` (308, tanpa BQ) |
| 14 | 310–311 | Procedure | 87.44 | Routine chest x-ray, so described | – |
| 15 | 312–313 | Procedure | 88.09 | Other soft tissue x-ray of abdominal wall | – |
| 16 | 314–315 | Procedure | 90.59 | Microscopic examination of blood, Other microscopic examination | – |
| 17 | 316–317 | Procedure | 96.04 | Insertion of endotracheal tube | – |
| 18 | 318–319 | Procedure | 87.44 | Routine chest x-ray, so described | – |
| 19 | 320–321 | Procedure | 88.09 | Other soft tissue x-ray of abdominal wall | – |
| 20 | 322–323 | Procedure | 90.59 | Microscopic examination of blood, Other microscopic examination | – |
| 21 | 324–325 | Procedure | 90.41 | Microscopic examination of specimen from trachea, bronchus, pleura,lung,and other thoracic specimen, and of sputum, Bacterial smear | – |
| 22 | 326–327 | Procedure | 96.04 | Insertion of endotracheal tube | – |
| 23 | 328–329 | Procedure | 87.44 | Routine chest x-ray, so described | – |
| 24 | 330–331 | Procedure | 88.09 | Other soft tissue x-ray of abdominal wall | – |
| 25 | 332–333 | Procedure | 93.90 | Non-invasive mechanical ventilation | – |
| 26 | 334–335 | Procedure | 96.04 | Insertion of endotracheal tube | – |
| 27 | 336–337 | Procedure | 96.71 | Continuous invasive mechanical ventilation for less than 96 consecutive hours | – |
| 28 | 338–339 | Procedure | 90.59 | Microscopic examination of blood, Other microscopic examination | – |
| 29 | 340–341 | Procedure | 87.44 | Routine chest x-ray, so described | – |
| 30 | 342–343 | Procedure | 96.72 | Continuous invasive mechanical ventilation for 96 consecutive hours or more | – |
| 31 | 344–345 | Procedure | 87.44 | Routine chest x-ray, so described | – |
| 32 | 346–347 | Procedure | 88.09 | Other soft tissue x-ray of abdominal wall | – |
| 33 | 348–349 | Procedure | 93.90 | Non-invasive mechanical ventilation | – |
| 34 | 350–351 | Procedure | 99.60 | Cardiopulmonary resuscitation, not otherwise specified | – |
| 35 | 352–353 | Procedure | 87.44 | Routine chest x-ray, so described | – |
| 36 | 354–355 | Procedure | 99.60 | Cardiopulmonary resuscitation, not otherwise specified | – |
| 37 | 356–357 | Procedure | 99.04 | Transfusion of packed cells | – |
| 38 | 358–359 | Procedure | 87.44 | Routine chest x-ray, so described | – |
| 39 | 360–361 | Procedure | 88.09 | Other soft tissue x-ray of abdominal wall | – |
| 40 | 362–363 | Procedure | 96.04 | Insertion of endotracheal tube | – |
| 41 | 364–365 | Procedure | 96.71 | Continuous invasive mechanical ventilation for less than 96 consecutive hours | – |
| 42 | 366–367 | Procedure | 89.52 | Electrocardiogram | – |
| 43 | 368–369 | Procedure | 87.44 | Routine chest x-ray, so described | – |
| 44 | 370–371 | Procedure | 88.09 | Other soft tissue x-ray of abdominal wall | – |
| 45 | 372–373 | Procedure | 93.90 | Non-invasive mechanical ventilation | – |
| 46 | 374–375 | Procedure | 87.44 | Routine chest x-ray, so described | – |
| 47 | 376–377 | Procedure | 88.09 | Other soft tissue x-ray of abdominal wall | – |
| 48 | 378–379 | Procedure | 93.90 | Non-invasive mechanical ventilation | – |
| 49 | 380–381 | Procedure | 87.44 | Routine chest x-ray, so described | – |
| 50 | 382–383 | Procedure | 87.44 | Routine chest x-ray, so described | – |
| 51 | 384–385 | Procedure | 99.60 | Cardiopulmonary resuscitation, not otherwise specified | – |
| 52 | 386–396 | Procedure | 87.44 | Routine chest x-ray, so described | _Tindakan_ → `Procedure.status` (388, tanpa BQ) |
| 53 | 397–398 | Procedure | 96.05 | Other intubation of respiratory tract | _PROSEDUR KLINIS_ → `Procedure.category.coding` (397, tanpa BQ) |
| 54 | 399–400 | Procedure | 87.44 | Routine chest x-ray, so described | – |
| 55 | 401–402 | Procedure | 88.09 | Other soft tissue x-ray of abdominal wall | – |
| 56 | 403–404 | Procedure | 90.59 | Microscopic examination of blood, Other microscopic examination | – |
| 57 | 405–406 | Procedure | 96.04 | Insertion of endotracheal tube | – |
| 58 | 407–408 | Procedure | 90.41 | Microscopic examination of specimen from trachea, bronchus, pleura,lung,and other thoracic specimen, and of sputum, Bacterial smear | – |
| 59 | 409–410 | Procedure | 93.90 | Non-invasive mechanical ventilation | – |
| 60 | 411–412 | Procedure | 96.71 | Continuous invasive mechanical ventilation for less than 96 consecutive hours | – |
| 61 | 413–414 | Procedure | 96.72 | Continuous invasive mechanical ventilation for 96 consecutive hours or more | – |
| 62 | 415–416 | Procedure | 99.60 | Cardiopulmonary resuscitation, not otherwise specified | – |
| 63 | 417–418 | Procedure | 99.04 | Transfusion of packed cells | – |
| 64 | 419–420 | Procedure | 89.52 | Electrocardiogram | – |
| 65 | 421–431 | Composition | – | – | _DX RESUME PULANG_ → `Composition.status` (421, tanpa BQ) |
| 66 | 432–441 | Condition | 268910001 | Patient's condition improved | _KEADAAN PASIEN_ → `Condition.clinicalStatus.coding` (432, tanpa BQ) |
| 67 | 444–454 | Observation | 82589-3 | Highest level of education | _PENDIDIKAN_ → `Observation.valueCodeableConcept.coding` (447, tanpa BQ) |
| 68 | 455–466 | Observation | 183797002 | Duration of inpatient stay | _LAMA RAWAT (HARI)_ → `Observation.valueQuantity.value` (458, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Procedure | 52 |
| Condition | 6 |
| Observation | 5 |
| Patient | 1 |
| Encounter | 1 |
| EpisodeOfCare | 1 |
| Coverage | 1 |
| Composition | 1 |
| **Total** | **68** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 115 | Condition | `Condition.code.coding` | Z00.1 | Routine child health examination | http://hl7.org/fhir/sid/icd-10 |
| 2 | 120 | Encounter | `Encounter.hospitalization.admitSource.coding` | 1991000124105 | Referred by self | http://snomed.info/sct |
| 3 | 121 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000814 | Rujukan dari Dokter Praktik Mandiri | http://terminology.kemkes.go.id/sp |
| 4 | 122 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000119 | Rujukan dari Rumah Sakit | http://terminology.kemkes.go.id/sp |
| 5 | 124 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000117 | Rujukan dari Puskesmas | http://terminology.kemkes.go.id/sp |
| 6 | 125 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000117 | Rujukan dari Puskesmas | http://terminology.kemkes.go.id/sp |
| 7 | 127 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000117 | Rujukan dari Puskesmas | http://terminology.kemkes.go.id/sp |
| 8 | 129 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000117 | Rujukan dari Puskesmas | http://terminology.kemkes.go.id/sp |
| 9 | 131 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000117 | Rujukan dari Puskesmas | http://terminology.kemkes.go.id/sp |
| 10 | 133 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000117 | Rujukan dari Puskesmas | http://terminology.kemkes.go.id/sp |
| 11 | 135 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000117 | Rujukan dari Puskesmas | http://terminology.kemkes.go.id/sp |
| 12 | 137 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000117 | Rujukan dari Puskesmas | http://terminology.kemkes.go.id/sp |
| 13 | 139 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000117 | Rujukan dari Puskesmas | http://terminology.kemkes.go.id/sp |
| 14 | 157 | EpisodeOfCare | `EpisodeOfCare.type.coding` | Neonate | Neonate | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 15 | 184 | Observation | `Observation.code.coding` | 184061005 | Patient registration status | http://snomed.info/sct |
| 16 | 185 | Observation | `Observation.valueCodeableConcept.coding` | SP000812 | Pasien Baru | http://terminology.kemkes.go.id/sp |
| 17 | 186 | Observation | `Observation.valueCodeableConcept.coding` | SP000813 | Pasien Lama | http://terminology.kemkes.go.id/sp |
| 18 | 196 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 19 | 208 | Observation | `Observation.code.coding` | SP000811 | Jalur Masuk Rawat Inap | http://terminology.kemkes.go.id/sp |
| 20 | 209 | Observation | `Observation.valueCodeableConcept.coding` | 225728007 | Accident and Emergency department | http://snomed.info/sct |
| 21 | 211 | Observation | `Observation.valueCodeableConcept.coding` | 50849002 | Emergency room admission | http://snomed.info/sct |
| 22 | 212 | Observation | `Observation.valueCodeableConcept.coding` | 405606005 | Labor and delivery unit | http://snomed.info/sct |
| 23 | 230 | Condition | `Condition.code.coding` | P22.0 | Respiratory distress syndrome of newborn | http://hl7.org/fhir/sid/icd-10 |
| 24 | 231 | Condition | `Condition.code.coding` | E46 | Unspecified protein-energy malnutrition | http://hl7.org/fhir/sid/icd-10 |
| 25 | 232 | Condition | `Condition.code.coding` | P21.0 | Severe birth asphyxia | http://hl7.org/fhir/sid/icd-10 |
| 26 | 233 | Condition | `Condition.code.coding` | G41.9 | Status epilepticus, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 27 | 234 | Condition | `Condition.code.coding` | R56.0 | Febrile convulsions | http://hl7.org/fhir/sid/icd-10 |
| 28 | 235 | Condition | `Condition.code.coding` | P21.1 | Mild and moderate birth asphyxia | http://hl7.org/fhir/sid/icd-10 |
| 29 | 244 | Condition | `Condition.code.coding` | P22.0 | Respiratory distress syndrome of newborn | http://hl7.org/fhir/sid/icd-10 |
| 30 | 245 | Condition | `Condition.code.coding` | P22.0 | Respiratory distress syndrome of newborn | http://hl7.org/fhir/sid/icd-10 |
| 31 | 246 | Condition | `Condition.code.coding` | E46 | Unspecified protein-energy malnutrition | http://hl7.org/fhir/sid/icd-10 |
| 32 | 247 | Condition | `Condition.code.coding` | P21.0 | Severe birth asphyxia | http://hl7.org/fhir/sid/icd-10 |
| 33 | 248 | Condition | `Condition.code.coding` | P21.0 | Severe birth asphyxia | http://hl7.org/fhir/sid/icd-10 |
| 34 | 249 | Condition | `Condition.code.coding` | P21.0 | Severe birth asphyxia | http://hl7.org/fhir/sid/icd-10 |
| 35 | 250 | Condition | `Condition.code.coding` | G41.9 | Status epilepticus, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 36 | 251 | Condition | `Condition.code.coding` | R56.0 | Febrile convulsions | http://hl7.org/fhir/sid/icd-10 |
| 37 | 252 | Condition | `Condition.code.coding` | P21.1 | Mild and moderate birth asphyxia | http://hl7.org/fhir/sid/icd-10 |
| 38 | 261 | Condition | `Condition.code.coding` | P23.9 | Congenital pneumonia, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 39 | 262 | Condition | `Condition.code.coding` | P07.1 | Other low birth weight | http://hl7.org/fhir/sid/icd-10 |
| 40 | 263 | Condition | `Condition.code.coding` | R40.2 | Coma, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 41 | 264 | Condition | `Condition.code.coding` | P70.4 | Other neonatal hypoglycaemia | http://hl7.org/fhir/sid/icd-10 |
| 42 | 265 | Condition | `Condition.code.coding` | P59.9 | Neonatal jaundice, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 43 | 266 | Condition | `Condition.code.coding` | P90 | Convulsions of newborn | http://hl7.org/fhir/sid/icd-10 |
| 44 | 267 | Condition | `Condition.code.coding` | J96.9 | Respiratory failure, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 45 | 268 | Condition | `Condition.code.coding` | P03.4 | Fetus and newborn affected by caesarean delivery | http://hl7.org/fhir/sid/icd-10 |
| 46 | 269 | Condition | `Condition.code.coding` | P80.9 | Hypothermia of newborn, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 47 | 270 | Condition | `Condition.code.coding` | P39.9 | Infection specific to the perinatal period, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 48 | 271 | Condition | `Condition.code.coding` | P21.0 | Severe birth asphyxia | http://hl7.org/fhir/sid/icd-10 |
| 49 | 272 | Condition | `Condition.code.coding` | P21.1 | Mild and moderate birth asphyxia | http://hl7.org/fhir/sid/icd-10 |
| 50 | 281 | Condition | `Condition.code.coding` | P23.9 | Congenital pneumonia, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 51 | 282 | Condition | `Condition.code.coding` | P07.1 | Other low birth weight | http://hl7.org/fhir/sid/icd-10 |
| 52 | 283 | Condition | `Condition.code.coding` | R40.2 | Coma, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 53 | 284 | Condition | `Condition.code.coding` | P70.4 | Other neonatal hypoglycaemia | http://hl7.org/fhir/sid/icd-10 |
| 54 | 285 | Condition | `Condition.code.coding` | P59.9 | Neonatal jaundice, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 55 | 286 | Condition | `Condition.code.coding` | P90 | Convulsions of newborn | http://hl7.org/fhir/sid/icd-10 |
| 56 | 287 | Condition | `Condition.code.coding` | R40.2 | Coma, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 57 | 288 | Condition | `Condition.code.coding` | P23.9 | Congenital pneumonia, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 58 | 289 | Condition | `Condition.code.coding` | J96.9 | Respiratory failure, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 59 | 290 | Condition | `Condition.code.coding` | R40.2 | Coma, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 60 | 291 | Condition | `Condition.code.coding` | P03.4 | Fetus and newborn affected by caesarean delivery | http://hl7.org/fhir/sid/icd-10 |
| 61 | 292 | Condition | `Condition.code.coding` | P80.9 | Hypothermia of newborn, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 62 | 293 | Condition | `Condition.code.coding` | P39.9 | Infection specific to the perinatal period, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 63 | 294 | Condition | `Condition.code.coding` | P21.0 | Severe birth asphyxia | http://hl7.org/fhir/sid/icd-10 |
| 64 | 295 | Condition | `Condition.code.coding` | P21.1 | Mild and moderate birth asphyxia | http://hl7.org/fhir/sid/icd-10 |
| 65 | 296 | Condition | `Condition.code.coding` | P22.0 | Respiratory distress syndrome of newborn | http://hl7.org/fhir/sid/icd-10 |
| 66 | 297 | Condition | `Condition.code.coding` | P22.0 | Respiratory distress syndrome of newborn | http://hl7.org/fhir/sid/icd-10 |
| 67 | 298 | Condition | `Condition.code.coding` | P21.0 | Severe birth asphyxia | http://hl7.org/fhir/sid/icd-10 |
| 68 | 309 | Procedure | `Procedure.code.coding` | 96.05 | Other intubation of respiratory tract | http://hl7.org/fhir/sid/icd-9-cm |
| 69 | 311 | Procedure | `Procedure.code.coding` | 87.44 | Routine chest x-ray, so described | http://hl7.org/fhir/sid/icd-9-cm |
| 70 | 313 | Procedure | `Procedure.code.coding` | 88.09 | Other soft tissue x-ray of abdominal wall | http://hl7.org/fhir/sid/icd-9-cm |
| 71 | 315 | Procedure | `Procedure.code.coding` | 90.59 | Microscopic examination of blood, Other microscopic examination | http://hl7.org/fhir/sid/icd-9-cm |
| 72 | 317 | Procedure | `Procedure.code.coding` | 96.04 | Insertion of endotracheal tube | http://hl7.org/fhir/sid/icd-9-cm |
| 73 | 319 | Procedure | `Procedure.code.coding` | 87.44 | Routine chest x-ray, so described | http://hl7.org/fhir/sid/icd-9-cm |
| 74 | 321 | Procedure | `Procedure.code.coding` | 88.09 | Other soft tissue x-ray of abdominal wall | http://hl7.org/fhir/sid/icd-9-cm |
| 75 | 323 | Procedure | `Procedure.code.coding` | 90.59 | Microscopic examination of blood, Other microscopic examination | http://hl7.org/fhir/sid/icd-9-cm |
| 76 | 325 | Procedure | `Procedure.code.coding` | 90.41 | Microscopic examination of specimen from trachea, bronchus, pleura,lung,and other thoracic specimen, and of sputum, Bacterial smear | http://hl7.org/fhir/sid/icd-9-cm |
| 77 | 327 | Procedure | `Procedure.code.coding` | 96.04 | Insertion of endotracheal tube | http://hl7.org/fhir/sid/icd-9-cm |
| 78 | 329 | Procedure | `Procedure.code.coding` | 87.44 | Routine chest x-ray, so described | http://hl7.org/fhir/sid/icd-9-cm |
| 79 | 331 | Procedure | `Procedure.code.coding` | 88.09 | Other soft tissue x-ray of abdominal wall | http://hl7.org/fhir/sid/icd-9-cm |
| 80 | 333 | Procedure | `Procedure.code.coding` | 93.90 | Non-invasive mechanical ventilation | http://hl7.org/fhir/sid/icd-9-cm |
| 81 | 335 | Procedure | `Procedure.code.coding` | 96.04 | Insertion of endotracheal tube | http://hl7.org/fhir/sid/icd-9-cm |
| 82 | 337 | Procedure | `Procedure.code.coding` | 96.71 | Continuous invasive mechanical ventilation for less than 96 consecutive hours | http://hl7.org/fhir/sid/icd-9-cm |
| 83 | 339 | Procedure | `Procedure.code.coding` | 90.59 | Microscopic examination of blood, Other microscopic examination | http://hl7.org/fhir/sid/icd-9-cm |
| 84 | 341 | Procedure | `Procedure.code.coding` | 87.44 | Routine chest x-ray, so described | http://hl7.org/fhir/sid/icd-9-cm |
| 85 | 343 | Procedure | `Procedure.code.coding` | 96.72 | Continuous invasive mechanical ventilation for 96 consecutive hours or more | http://hl7.org/fhir/sid/icd-9-cm |
| 86 | 345 | Procedure | `Procedure.code.coding` | 87.44 | Routine chest x-ray, so described | http://hl7.org/fhir/sid/icd-9-cm |
| 87 | 347 | Procedure | `Procedure.code.coding` | 88.09 | Other soft tissue x-ray of abdominal wall | http://hl7.org/fhir/sid/icd-9-cm |
| 88 | 349 | Procedure | `Procedure.code.coding` | 93.90 | Non-invasive mechanical ventilation | http://hl7.org/fhir/sid/icd-9-cm |
| 89 | 351 | Procedure | `Procedure.code.coding` | 99.60 | Cardiopulmonary resuscitation, not otherwise specified | http://hl7.org/fhir/sid/icd-9-cm |
| 90 | 353 | Procedure | `Procedure.code.coding` | 87.44 | Routine chest x-ray, so described | http://hl7.org/fhir/sid/icd-9-cm |
| 91 | 355 | Procedure | `Procedure.code.coding` | 99.60 | Cardiopulmonary resuscitation, not otherwise specified | http://hl7.org/fhir/sid/icd-9-cm |
| 92 | 357 | Procedure | `Procedure.code.coding` | 99.04 | Transfusion of packed cells | http://hl7.org/fhir/sid/icd-9-cm |
| 93 | 359 | Procedure | `Procedure.code.coding` | 87.44 | Routine chest x-ray, so described | http://hl7.org/fhir/sid/icd-9-cm |
| 94 | 361 | Procedure | `Procedure.code.coding` | 88.09 | Other soft tissue x-ray of abdominal wall | http://hl7.org/fhir/sid/icd-9-cm |
| 95 | 363 | Procedure | `Procedure.code.coding` | 96.04 | Insertion of endotracheal tube | http://hl7.org/fhir/sid/icd-9-cm |
| 96 | 365 | Procedure | `Procedure.code.coding` | 96.71 | Continuous invasive mechanical ventilation for less than 96 consecutive hours | http://hl7.org/fhir/sid/icd-9-cm |
| 97 | 367 | Procedure | `Procedure.code.coding` | 89.52 | Electrocardiogram | http://hl7.org/fhir/sid/icd-9-cm |
| 98 | 369 | Procedure | `Procedure.code.coding` | 87.44 | Routine chest x-ray, so described | http://hl7.org/fhir/sid/icd-9-cm |
| 99 | 371 | Procedure | `Procedure.code.coding` | 88.09 | Other soft tissue x-ray of abdominal wall | http://hl7.org/fhir/sid/icd-9-cm |
| 100 | 373 | Procedure | `Procedure.code.coding` | 93.90 | Non-invasive mechanical ventilation | http://hl7.org/fhir/sid/icd-9-cm |
| 101 | 375 | Procedure | `Procedure.code.coding` | 87.44 | Routine chest x-ray, so described | http://hl7.org/fhir/sid/icd-9-cm |
| 102 | 377 | Procedure | `Procedure.code.coding` | 88.09 | Other soft tissue x-ray of abdominal wall | http://hl7.org/fhir/sid/icd-9-cm |
| 103 | 379 | Procedure | `Procedure.code.coding` | 93.90 | Non-invasive mechanical ventilation | http://hl7.org/fhir/sid/icd-9-cm |
| 104 | 381 | Procedure | `Procedure.code.coding` | 87.44 | Routine chest x-ray, so described | http://hl7.org/fhir/sid/icd-9-cm |
| 105 | 383 | Procedure | `Procedure.code.coding` | 87.44 | Routine chest x-ray, so described | http://hl7.org/fhir/sid/icd-9-cm |
| 106 | 385 | Procedure | `Procedure.code.coding` | 99.60 | Cardiopulmonary resuscitation, not otherwise specified | http://hl7.org/fhir/sid/icd-9-cm |
| 107 | 387 | Procedure | `Procedure.code.coding` | 87.44 | Routine chest x-ray, so described | http://hl7.org/fhir/sid/icd-9-cm |
| 108 | 398 | Procedure | `Procedure.code.coding` | 96.05 | Other intubation of respiratory tract | http://hl7.org/fhir/sid/icd-9-cm |
| 109 | 400 | Procedure | `Procedure.code.coding` | 87.44 | Routine chest x-ray, so described | http://hl7.org/fhir/sid/icd-9-cm |
| 110 | 402 | Procedure | `Procedure.code.coding` | 88.09 | Other soft tissue x-ray of abdominal wall | http://hl7.org/fhir/sid/icd-9-cm |
| 111 | 404 | Procedure | `Procedure.code.coding` | 90.59 | Microscopic examination of blood, Other microscopic examination | http://hl7.org/fhir/sid/icd-9-cm |
| 112 | 406 | Procedure | `Procedure.code.coding` | 96.04 | Insertion of endotracheal tube | http://hl7.org/fhir/sid/icd-9-cm |
| 113 | 408 | Procedure | `Procedure.code.coding` | 90.41 | Microscopic examination of specimen from trachea, bronchus, pleura,lung,and other thoracic specimen, and of sputum, Bacterial smear | http://hl7.org/fhir/sid/icd-9-cm |
| 114 | 410 | Procedure | `Procedure.code.coding` | 93.90 | Non-invasive mechanical ventilation | http://hl7.org/fhir/sid/icd-9-cm |
| 115 | 412 | Procedure | `Procedure.code.coding` | 96.71 | Continuous invasive mechanical ventilation for less than 96 consecutive hours | http://hl7.org/fhir/sid/icd-9-cm |
| 116 | 414 | Procedure | `Procedure.code.coding` | 96.72 | Continuous invasive mechanical ventilation for 96 consecutive hours or more | http://hl7.org/fhir/sid/icd-9-cm |
| 117 | 416 | Procedure | `Procedure.code.coding` | 99.60 | Cardiopulmonary resuscitation, not otherwise specified | http://hl7.org/fhir/sid/icd-9-cm |
| 118 | 418 | Procedure | `Procedure.code.coding` | 99.04 | Transfusion of packed cells | http://hl7.org/fhir/sid/icd-9-cm |
| 119 | 420 | Procedure | `Procedure.code.coding` | 89.52 | Electrocardiogram | http://hl7.org/fhir/sid/icd-9-cm |
| 120 | 434 | Condition | `Condition.code.coding` | 268910001 | Patient's condition improved | http://snomed.info/sct |
| 121 | 435 | Condition | `Condition.code.coding` | 371001000 | Patient cured | http://snomed.info/sct |
| 122 | 446 | Observation | `Observation.code.coding` | 82589-3 | Highest level of education | http://loinc.org |
| 123 | 447 | Observation | `Observation.valueCodeableConcept.coding` | 224294005 | No formal education | http://snomed.info/sct |
| 124 | 457 | Observation | `Observation.code.coding` | 183797002 | Duration of inpatient stay | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://hl7.org/fhir/sid/icd-9-cm | 52 |
| http://hl7.org/fhir/sid/icd-10 | 46 |
| http://terminology.kemkes.go.id/sp | 14 |
| http://snomed.info/sct | 10 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 1 |
| http://loinc.org | 1 |
| **Total** | **124** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 30 | – | Faskes yang melayani BBL | Organization | `Organization.name` |
| 70 | – | Ruang | Location | `Location.identifier` |
| 467 | – | TANGGAL | – | `` |
| 468 | – | NOMR | – | `` |
