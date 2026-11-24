# Output Form: ASIK - CKG Bayi Baru Lahir (versi 1)

Sumber: `mapping/phdt-data-dictionary-asik-ckg-bbl-v1.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-asik-ckg-bbl-v1.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 25 |
| Code (`jumlah code` = 1) | 56 |
| Code unik (code + CodeSystem) | 31 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 2 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–27 | Patient | – | – | _Nama Pasien_ → `Patient.name.text` (2, tanpa BQ)<br>_NIK_ → `Patient.identifier.value` (5, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (7, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (9, tanpa BQ)<br>_No HP_ → `Patient.contact.telecom.value` (11, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (18, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (21, tanpa BQ) |
| 2 | 71–84 | Encounter | – | – | _Tanggal Pelayanan_ → `Encounter.period.start` (79, tanpa BQ) |
| 3 | 85–91 | Condition | Z01.8 | Other specified special examinations | – |
| 4 | 102–116 | Observation | 424144002.0 | Current chronological age | _Usia_ → `Observation.valueQuantity.value` (105, tanpa BQ) |
| 5 | 117–144 | Observation | 8339-4 | Birth weight Measured | _Berat Badan Lahir_ → `Observation.valueQuantity.value` (120, tanpa BQ) |
| 6 | 145–167 | Observation | 89269-5 | Body height Measured --at birth | _Panjang Badan Lahir_ → `Observation.valueQuantity.value` (148, tanpa BQ) |
| 7 | 168–195 | Observation | 29463-7 | Body weight | _Berat Badan Saat Ini_ → `Observation.valueQuantity.value` (171, tanpa BQ) |
| 8 | 196–222 | Observation | 103228002.0 | Hemoglobin saturation with oxygen | _Hasil Pemeriksaan Pulse Oksimetri Pada Tangan Kanan_ → `Observation.valueQuantity.value` (199, tanpa BQ) |
| 9 | 223–249 | Observation | 103228002.0 | Hemoglobin saturation with oxygen | _Hasil Pemeriksaan Pulse Oksimetri Pada Kaki_ → `Observation.valueQuantity.value` (226, tanpa BQ) |
| 10 | 250–260 | Observation | SP000449 | Hasil Pemeriksaan Skrining Penyakit Jantung Bawaan | _Hasil Pemeriksaan Penyakit Jantung Bawaan_ → `Observation.valueCodeableConcept.coding` (253, tanpa BQ) |
| 11 | 261–276 | Observation | 29575-8 | Thyrotropin [Units/volume] in DBS | _Hasil Pemeriksaan Lab Hipotiroid Kongenital_ → `Observation.valueRange.low.value` (264, tanpa BQ) |
| 12 | 277–292 | Observation | 32546-4 | Glucose-6-Phosphate dehydrogenase [Enzymatic activity/mass] in Red Blood Cells | _Hasil Pemeriksaan Lab G6PD_ → `Observation.valueRange.low.value` (280, tanpa BQ) |
| 13 | 293–306 | Observation | 57086-1 | Congenital adrenal hyperplasia newborn screening panel | _Hasil Pemeriksaan Lab Skrining HAK_ → `Observation.valueString` (296, tanpa BQ) |
| 14 | 307–319 | Procedure | 25179006.0 | Blood unit collection | _Pengambilan Darah Tumit_ → `Procedure.category.coding` (307, tanpa BQ)<br>_Pemeriksaan Tes Konfirmasi SHK_ → `Procedure.indentifier` (319, tanpa BQ) |
| 15 | 320–330 | Procedure | 400984005.0 | Congenital hypothyroidism screening test | – |
| 16 | 331–347 | Observation | 3016-3 | Thyrotropin [Units/volume] in Serum or Plasma | _Hasil Tes Konfirmasi SHK_ → `Observation.identifier` (331, tanpa BQ) |
| 17 | 348–359 | Procedure | 252298007.0 | Glucose-6-phosphate dehydrogenase deficiency spot test | _Pemeriksaan Konfirmasi Defisiensi G6PD_ → `Procedure.indentifier` (348, tanpa BQ) |
| 18 | 360–376 | Observation | 32546-4 | Glucose-6-Phosphate dehydrogenase [Enzymatic activity/mass] in Red Blood Cells | _Hasil Tes Konfirmasi Defisiensi G6PD_ → `Observation.identifier` (360, tanpa BQ) |
| 19 | 377–388 | Procedure | 431420002.0 | Screening for congenital adrenal hyperplasia | _Pemeriksaan Konfirmasi Skrining HAK_ → `Procedure.indentifier` (377, tanpa BQ) |
| 20 | 389–403 | Observation | 57086-1 | Congenital adrenal hyperplasia newborn screening panel | _Hasil Tes Konfirmasi Skrining HAK_ → `Observation.identifier` (389, tanpa BQ) |
| 21 | 404–414 | Procedure | TK000151 | Edukasi skrining hiperbilirubinemia dan kelainan saluran empedu | _Edukasi Kelainan Saluran Empedu_ → `Procedure.category.coding` (404, tanpa BQ) |
| 22 | 416–427 | Observation | 267030001.0 | Yellow or jaundiced color | _Hasil Pemeriksaan Ikterus Skrining Kelainan Saluran Empedu Usia 14-28 Hari_ → `Observation.valueBoolean` (419, tanpa BQ) |
| 23 | 428–448 | Observation | 225592001.0 | Finding of color of stool | _Hasil Pemeriksaan Tinja Skrining Kelainan Saluran Empedu Usia 14-28 Hari_ → `Observation.valueRange.low.value` (430, tanpa BQ)<br>_Hasil Pemeriksaan Ikterus Skrining Kelainan Saluran Empedu Usia 2-4 Bulan_ → `Observation.status` (448, tanpa BQ) |
| 24 | 449–459 | Observation | 267030001.0 | Yellow or jaundiced color | – |
| 25 | 460–478 | Observation | 225592001.0 | Finding of color of stool | _Hasil Pemeriksaan Tinja Skrining Kelainan Saluran Empedu Usia 2-4 Bulan_ → `Observation.valueRange.low.value` (462, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 17 |
| Procedure | 5 |
| Patient | 1 |
| Encounter | 1 |
| Condition | 1 |
| **Total** | **25** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 87 | Condition | `Condition.code.coding` | Z01.8 | Other specified special examinations | http://hl7.org/fhir/sid/icd-10 |
| 2 | 104 | Observation | `Observation.code.coding` | 424144002.0 | Current chronological age | http://snomed.info/sct |
| 3 | 107 | Observation | `Observation.component.code.coding` | SP000020 | Umur Bulan | http://terminology.kemkes.go.id/sp |
| 4 | 119 | Observation | `Observation.code.coding` | 8339-4 | Birth weight Measured | http://loinc.org |
| 5 | 124 | Observation | `Observation.interpretation.coding` | 276613009.0 | High birth weight | http://snomed.info/sct |
| 6 | 129 | Observation | `Observation.interpretation.coding` | 276712009.0 | Normal birth weight | http://snomed.info/sct |
| 7 | 134 | Observation | `Observation.interpretation.coding` | 276610007.0 | Low birth weight infant | http://snomed.info/sct |
| 8 | 137 | Observation | `Observation.interpretation.coding` | 276611006.0 | Very low birth weight infant | http://snomed.info/sct |
| 9 | 147 | Observation | `Observation.code.coding` | 89269-5 | Body height Measured --at birth | http://loinc.org |
| 10 | 152 | Observation | `Observation.interpretation.coding` | OI000014 | Tinggi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 11 | 157 | Observation | `Observation.interpretation.coding` | OI000013 | Normal | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 12 | 160 | Observation | `Observation.interpretation.coding` | OI000012 | Pendek | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 13 | 170 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 14 | 175 | Observation | `Observation.interpretation.coding` | 276613009.0 | High birth weight | http://snomed.info/sct |
| 15 | 180 | Observation | `Observation.interpretation.coding` | 276712009.0 | Normal birth weight | http://snomed.info/sct |
| 16 | 185 | Observation | `Observation.interpretation.coding` | 276610007.0 | Low birth weight infant | http://snomed.info/sct |
| 17 | 188 | Observation | `Observation.interpretation.coding` | 276611006.0 | Very low birth weight infant | http://snomed.info/sct |
| 18 | 198 | Observation | `Observation.code.coding` | 103228002.0 | Hemoglobin saturation with oxygen | http://snomed.info/sct |
| 19 | 209 | Observation | `Observation.interpretation.coding` | POS | Positve | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 20 | 215 | Observation | `Observation.interpretation.coding` | NEG | Negative | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 21 | 225 | Observation | `Observation.code.coding` | 103228002.0 | Hemoglobin saturation with oxygen | http://snomed.info/sct |
| 22 | 236 | Observation | `Observation.interpretation.coding` | POS | Positve | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 23 | 242 | Observation | `Observation.interpretation.coding` | NEG | Negative | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 24 | 252 | Observation | `Observation.code.coding` | SP000449 | Hasil Pemeriksaan Skrining Penyakit Jantung Bawaan | http://terminology.kemkes.go.id/sp |
| 25 | 253 | Observation | `Observation.valueCodeableConcept.coding` | 410519009.0 | At risk | http://snomed.info/sct |
| 26 | 263 | Observation | `Observation.code.coding` | 29575-8 | Thyrotropin [Units/volume] in DBS | http://loinc.org |
| 27 | 266 | Observation | `Observation.interpretation.coding` | POS | Positve | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 28 | 269 | Observation | `Observation.interpretation.coding` | NEG | Negative | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 29 | 279 | Observation | `Observation.code.coding` | 32546-4 | Glucose-6-Phosphate dehydrogenase [Enzymatic activity/mass] in Red Blood Cells | http://loinc.org |
| 30 | 282 | Observation | `Observation.interpretation.coding` | POS | Positve | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 31 | 285 | Observation | `Observation.interpretation.coding` | NEG | Negative | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 32 | 295 | Observation | `Observation.code.coding` | 57086-1 | Congenital adrenal hyperplasia newborn screening panel | http://loinc.org |
| 33 | 297 | Observation | `Observation.interpretation.coding` | POS | Positve | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 34 | 299 | Observation | `Observation.interpretation.coding` | NEG | Negative | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 35 | 308 | Procedure | `Procedure.code.coding` | 25179006.0 | Blood unit collection | http://snomed.info/sct |
| 36 | 321 | Procedure | `Procedure.code.coding` | 400984005.0 | Congenital hypothyroidism screening test | http://snomed.info/sct |
| 37 | 334 | Observation | `Observation.code.coding` | 3016-3 | Thyrotropin [Units/volume] in Serum or Plasma | http://loinc.org |
| 38 | 337 | Observation | `Observation.interpretation.coding` | POS | Positve | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 39 | 340 | Observation | `Observation.interpretation.coding` | NEG | Negative | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 40 | 350 | Procedure | `Procedure.code.coding` | 252298007.0 | Glucose-6-phosphate dehydrogenase deficiency spot test | http://snomed.info/sct |
| 41 | 363 | Observation | `Observation.code.coding` | 32546-4 | Glucose-6-Phosphate dehydrogenase [Enzymatic activity/mass] in Red Blood Cells | http://loinc.org |
| 42 | 366 | Observation | `Observation.interpretation.coding` | POS | Positve | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 43 | 369 | Observation | `Observation.interpretation.coding` | NEG | Negative | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 44 | 379 | Procedure | `Procedure.code.coding` | 431420002.0 | Screening for congenital adrenal hyperplasia | http://snomed.info/sct |
| 45 | 392 | Observation | `Observation.code.coding` | 57086-1 | Congenital adrenal hyperplasia newborn screening panel | http://loinc.org |
| 46 | 394 | Observation | `Observation.interpretation.coding` | POS | Positve | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 47 | 396 | Observation | `Observation.interpretation.coding` | NEG | Negative | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 48 | 405 | Procedure | `Procedure.code.coding` | TK000151 | Edukasi skrining hiperbilirubinemia dan kelainan saluran empedu | http://terminology.kemkes.go.id |
| 49 | 418 | Observation | `Observation.code.coding` | 267030001.0 | Yellow or jaundiced color | http://snomed.info/sct |
| 50 | 429 | Observation | `Observation.code.coding` | 225592001.0 | Finding of color of stool | http://snomed.info/sct |
| 51 | 434 | Observation | `Observation.interpretation.coding` | 271863002.0 | Stool color abnormal | http://snomed.info/sct |
| 52 | 439 | Observation | `Observation.interpretation.coding` | 167605001.0 | Stool color normal | http://snomed.info/sct |
| 53 | 450 | Observation | `Observation.code.coding` | 267030001.0 | Yellow or jaundiced color | http://snomed.info/sct |
| 54 | 461 | Observation | `Observation.code.coding` | 225592001.0 | Finding of color of stool | http://snomed.info/sct |
| 55 | 466 | Observation | `Observation.interpretation.coding` | 271863002.0 | Stool color abnormal | http://snomed.info/sct |
| 56 | 471 | Observation | `Observation.interpretation.coding` | 167605001.0 | Stool color normal | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 24 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 16 |
| http://loinc.org | 9 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 3 |
| http://terminology.kemkes.go.id/sp | 2 |
| http://hl7.org/fhir/sid/icd-10 | 1 |
| http://terminology.kemkes.go.id | 1 |
| **Total** | **56** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 30 | – | ID Faskes | Organization | `Organization.id` |
| 415 | – | Tanggal Pemeriksaan Skrining Kelainan Saluran Empedu Usia 14-28 Hari | – | `` |
| 447 | – | Tanggal Pemeriksaan Skrining Kelainan Saluran Empedu Usia 2-4 Bulan | – | `` |
