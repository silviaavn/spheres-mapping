# Output Form: ASIK - CKG Bayi Baru Lahir (versi 2, tarikan baru)

Sumber: `mapping/phdt-data-dictionary-asik-ckg-bbl.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-asik-ckg-bbl.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 25 |
| Code (`jumlah code` = 1) | 41 |
| Code unik (code + CodeSystem) | 24 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 1 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–27 | Patient | – | – | _Nama Pasien_ → `Patient.name.text` (2, tanpa BQ)<br>_NIK_ → `Patient.identifier.value` (5, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (7, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (9, tanpa BQ)<br>_No HP_ → `Patient.contact.telecom.value` (11, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (18, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (21, tanpa BQ) |
| 2 | 71–84 | Encounter | – | – | _Tanggal Pelayanan_ → `Encounter.period.start` (79, tanpa BQ) |
| 3 | 85–91 | Condition | Z01.8 | Other specified special examinations | – |
| 4 | 102–113 | Observation | 424144002 | Current chronological age | _Usia_ → `Observation.valueQuantity.value` (105, tanpa BQ) |
| 5 | 114–125 | Observation | 8339-4 | Birth weight Measured | _Berat Badan Lahir_ → `Observation.valueQuantity.value` (117, tanpa BQ) |
| 6 | 126–137 | Observation | 89269-5 | Body height Measured --at birth | _Panjang Badan Lahir_ → `Observation.valueQuantity.value` (129, tanpa BQ) |
| 7 | 138–149 | Observation | 29463-7 | Body weight | _Berat Badan Saat Ini_ → `Observation.valueQuantity.value` (141, tanpa BQ) |
| 8 | 150–162 | Observation | 103228002 | Hemoglobin saturation with oxygen | _Hasil Pemeriksaan Pulse Oksimetri Pada Tangan Kanan_ → `Observation.valueQuantity.value` (153, tanpa BQ) |
| 9 | 163–175 | Observation | 103228002 | Hemoglobin saturation with oxygen | _Hasil Pemeriksaan Pulse Oksimetri Pada Kaki_ → `Observation.valueQuantity.value` (166, tanpa BQ) |
| 10 | 176–187 | Observation | SP000449 | Hasil Pemeriksaan Skrining Penyakit Jantung Bawaan | _Hasil Pemeriksaan Penyakit Jantung Bawaan_ → `Observation.valueCodeableConcept.coding` (179, tanpa BQ) |
| 11 | 188–203 | Observation | 29575-8 | Thyrotropin [Units/volume] in DBS | _Hasil Pemeriksaan Lab Hipotiroid Kongenital_ → `Observation.valueRange.low.value` (191, tanpa BQ) |
| 12 | 204–219 | Observation | 32546-4 | Glucose-6-Phosphate dehydrogenase [Enzymatic activity/mass] in Red Blood Cells | _Hasil Pemeriksaan Lab G6PD_ → `Observation.valueRange.low.value` (207, tanpa BQ) |
| 13 | 220–233 | Observation | 57086-1 | Congenital adrenal hyperplasia newborn screening panel | _Hasil Pemeriksaan Lab Skrining HAK_ → `Observation.valueString` (223, tanpa BQ) |
| 14 | 234–246 | Procedure | 25179006 | Blood unit collection | _Pengambilan Darah Tumit_ → `Procedure.category.coding` (234, tanpa BQ)<br>_Pemeriksaan Tes Konfirmasi SHK_ → `Procedure.identifier` (246, tanpa BQ) |
| 15 | 247–257 | Procedure | 400984005 | Congenital hypothyroidism screening test | – |
| 16 | 258–274 | Observation | 3016-3 | Thyrotropin [Units/volume] in Serum or Plasma | _Hasil Tes Konfirmasi SHK_ → `Observation.identifier` (258, tanpa BQ) |
| 17 | 275–286 | Procedure | 252298007 | Glucose-6-phosphate dehydrogenase deficiency spot test | _Pemeriksaan Konfirmasi Defisiensi G6PD_ → `Procedure.identifier` (275, tanpa BQ) |
| 18 | 287–303 | Observation | 32546-4 | Glucose-6-Phosphate dehydrogenase [Enzymatic activity/mass] in Red Blood Cells | _Hasil Tes Konfirmasi Defisiensi G6PD_ → `Observation.identifier` (287, tanpa BQ) |
| 19 | 304–315 | Procedure | 431420002 | Screening for congenital adrenal hyperplasia | _Pemeriksaan Konfirmasi Skrining HAK_ → `Procedure.identifier` (304, tanpa BQ) |
| 20 | 316–330 | Observation | 57086-1 | Congenital adrenal hyperplasia newborn screening panel | _Hasil Tes Konfirmasi Skrining HAK_ → `Observation.identifier` (316, tanpa BQ) |
| 21 | 331–341 | Procedure | TK000151 | Edukasi skrining hiperbilirubinemia dan kelainan saluran empedu | _Edukasi Kelainan Saluran Empedu_ → `Procedure.category.coding` (331, tanpa BQ) |
| 22 | 343–354 | Observation | 267030001 | Yellow or jaundiced color | _Hasil Pemeriksaan Ikterus Skrining Kelainan Saluran Empedu Usia 14-28 Hari_ → `Observation.valueBoolean` (346, tanpa BQ) |
| 23 | 355–375 | Observation | 225592001 | Finding of color of stool | _Hasil Pemeriksaan Tinja Skrining Kelainan Saluran Empedu Usia 14-28 Hari_ → `Observation.valueRange.low.value` (357, tanpa BQ)<br>_Hasil Pemeriksaan Ikterus Skrining Kelainan Saluran Empedu Usia 2-4 Bulan_ → `Observation.status` (375, tanpa BQ) |
| 24 | 376–386 | Observation | 267030001 | Yellow or jaundiced color | – |
| 25 | 387–405 | Observation | 225592001 | Finding of color of stool | _Hasil Pemeriksaan Tinja Skrining Kelainan Saluran Empedu Usia 2-4 Bulan_ → `Observation.valueRange.low.value` (389, tanpa BQ) |

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
| 2 | 104 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 3 | 116 | Observation | `Observation.code.coding` | 8339-4 | Birth weight Measured | http://loinc.org |
| 4 | 128 | Observation | `Observation.code.coding` | 89269-5 | Body height Measured --at birth | http://loinc.org |
| 5 | 140 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 6 | 152 | Observation | `Observation.code.coding` | 103228002 | Hemoglobin saturation with oxygen | http://snomed.info/sct |
| 7 | 165 | Observation | `Observation.code.coding` | 103228002 | Hemoglobin saturation with oxygen | http://snomed.info/sct |
| 8 | 178 | Observation | `Observation.code.coding` | SP000449 | Hasil Pemeriksaan Skrining Penyakit Jantung Bawaan | http://terminology.kemkes.go.id/sp |
| 9 | 179 | Observation | `Observation.valueCodeableConcept.coding` | 410519009 | At risk | http://snomed.info/sct |
| 10 | 180 | Observation | `Observation.valueCodeableConcept.coding` | 260385009 | Negative | http://snomed.info/sct |
| 11 | 190 | Observation | `Observation.code.coding` | 29575-8 | Thyrotropin [Units/volume] in DBS | http://loinc.org |
| 12 | 193 | Observation | `Observation.interpretation.coding` | POS | Positve | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 13 | 196 | Observation | `Observation.interpretation.coding` | NEG | Negative | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 14 | 206 | Observation | `Observation.code.coding` | 32546-4 | Glucose-6-Phosphate dehydrogenase [Enzymatic activity/mass] in Red Blood Cells | http://loinc.org |
| 15 | 209 | Observation | `Observation.interpretation.coding` | POS | Positve | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 16 | 212 | Observation | `Observation.interpretation.coding` | NEG | Negative | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 17 | 222 | Observation | `Observation.code.coding` | 57086-1 | Congenital adrenal hyperplasia newborn screening panel | http://loinc.org |
| 18 | 224 | Observation | `Observation.interpretation.coding` | POS | Positve | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 19 | 226 | Observation | `Observation.interpretation.coding` | NEG | Negative | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 20 | 235 | Procedure | `Procedure.code.coding` | 25179006 | Blood unit collection | http://snomed.info/sct |
| 21 | 248 | Procedure | `Procedure.code.coding` | 400984005 | Congenital hypothyroidism screening test | http://snomed.info/sct |
| 22 | 261 | Observation | `Observation.code.coding` | 3016-3 | Thyrotropin [Units/volume] in Serum or Plasma | http://loinc.org |
| 23 | 264 | Observation | `Observation.interpretation.coding` | POS | Positve | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 24 | 267 | Observation | `Observation.interpretation.coding` | NEG | Negative | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 25 | 277 | Procedure | `Procedure.code.coding` | 252298007 | Glucose-6-phosphate dehydrogenase deficiency spot test | http://snomed.info/sct |
| 26 | 290 | Observation | `Observation.code.coding` | 32546-4 | Glucose-6-Phosphate dehydrogenase [Enzymatic activity/mass] in Red Blood Cells | http://loinc.org |
| 27 | 293 | Observation | `Observation.interpretation.coding` | POS | Positve | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 28 | 296 | Observation | `Observation.interpretation.coding` | NEG | Negative | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 29 | 306 | Procedure | `Procedure.code.coding` | 431420002 | Screening for congenital adrenal hyperplasia | http://snomed.info/sct |
| 30 | 319 | Observation | `Observation.code.coding` | 57086-1 | Congenital adrenal hyperplasia newborn screening panel | http://loinc.org |
| 31 | 321 | Observation | `Observation.interpretation.coding` | POS | Positve | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 32 | 323 | Observation | `Observation.interpretation.coding` | NEG | Negative | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 33 | 332 | Procedure | `Procedure.code.coding` | TK000151 | Edukasi skrining hiperbilirubinemia dan kelainan saluran empedu | http://terminology.kemkes.go.id |
| 34 | 345 | Observation | `Observation.code.coding` | 267030001 | Yellow or jaundiced color | http://snomed.info/sct |
| 35 | 356 | Observation | `Observation.code.coding` | 225592001 | Finding of color of stool | http://snomed.info/sct |
| 36 | 361 | Observation | `Observation.interpretation.coding` | 271863002 | Stool color abnormal | http://snomed.info/sct |
| 37 | 366 | Observation | `Observation.interpretation.coding` | 167605001 | Stool color normal | http://snomed.info/sct |
| 38 | 377 | Observation | `Observation.code.coding` | 267030001 | Yellow or jaundiced color | http://snomed.info/sct |
| 39 | 388 | Observation | `Observation.code.coding` | 225592001 | Finding of color of stool | http://snomed.info/sct |
| 40 | 393 | Observation | `Observation.interpretation.coding` | 271863002 | Stool color abnormal | http://snomed.info/sct |
| 41 | 398 | Observation | `Observation.interpretation.coding` | 167605001 | Stool color normal | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 17 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 12 |
| http://loinc.org | 9 |
| http://hl7.org/fhir/sid/icd-10 | 1 |
| http://terminology.kemkes.go.id/sp | 1 |
| http://terminology.kemkes.go.id | 1 |
| **Total** | **41** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 30 | – | ID Faskes | Organization | `Organization.id` |
| 31 | – | ihs_organization | Organization | `Organization.type` |
| 342 | – | Tanggal Pemeriksaan Skrining Kelainan Saluran Empedu Usia 14-28 Hari | – | `` |
| 374 | – | Tanggal Pemeriksaan Skrining Kelainan Saluran Empedu Usia 2-4 Bulan | – | `` |
| 406 | – | Kode Faskes | – | `` |
