# Output Form: SiGizi Balita BNBA

Sumber: `mapping/phdt-data-dictionary-sigizi-balita-bnba.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-sigizi-balita-bnba.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 24 |
| Code (`jumlah code` = 1) | 50 |
| Code unik (code + CodeSystem) | 46 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 10 |
| Variabel BQ (unik) | 35 |
| Variabel raw (variabel dictionary; belum ada file mentah) | 33 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 3–32 | Patient | – | – | `nama` → `Patient.name.text` (3)<br>`nik` → `Patient.identifier.value` (6)<br>`jk` → `Patient.gender` (8)<br>`tgl_lahir` → `Patient.birthDate` (10)<br>_Alamat Domisili_ → `Patient.address.use` (11, tanpa BQ)<br>`alamat` → `Patient.address.line` (12)<br>`kabkota` → `Patient.address.city` (13)<br>_Nama Provinsi_ → `Patient.address.extension.url` (15, tanpa BQ)<br>`prov` → `Patient.address.extension.extension.valueCode` (17)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (20, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.url` (21, tanpa BQ)<br>`kec` → `Patient.address.extension.extension.valueCode` (23)<br>_Nama Desa_ → `Patient.address.extension.url` (24, tanpa BQ)<br>`desakel` → `Patient.address.extension.extension.valueCode` (26)<br>`rw` → `Patient.address.extension.extension.valueCode` (29)<br>`rt` → `Patient.address.extension.extension.valueCode` (32) |
| 2 | 118–121 | RelatedPerson | – | – | `nama_ortu` → `RelatedPerson.patient` (118) |
| 3 | 122–137 | Encounter | – | – | `tanggal_pengukuran` → `Encounter.period.start` (131)<br>`posyandu` → `Encounter.location.location.reference` (133) 🔎 lookup master data<br>`pukesmas` → `Encounter.serviceProvider.reference` (137) 🔎 lookup master data<br>`detail` → `Encounter.extension.valueString` (157) |
| 4 | 138–144 | Condition | 385984007 | Growth and development treatments and procedures | – |
| 5 | 158–175 | Observation | 424144002 | Current chronological age | `usia_saat_ukur` → `Observation.valueQuantity.value` (161) |
| 6 | 176–188 | Observation | 8339-4 | Birth weight Measured | `bb_lahir` → `Observation.valueQuantity.value` (180) |
| 7 | 189–201 | Observation | 89269-5 | Body height Measured --at birth | `tb_lahir` → `Observation.valueQuantity.value` (193) |
| 8 | 202–213 | Observation | 29463-7 | Body weight | `berat` → `Observation.valueQuantity.value` (205) |
| 9 | 214–226 | Observation | 8308-9 | Body height --standing | `tinggi` → `Observation.valueQuantity.value` (218) |
| 10 | 227–238 | Observation | 50373000 | Body height measure | `cara_ukur` → `Observation.status` (227) |
| 11 | 239–250 | Observation | 284473002 | Mid upper arm circumference | `lila` → `Observation.valueQuantity.value` (242) |
| 12 | 251–264 | Observation | 365910001 | Weight trend finding | `naik_berat_badan` → `Observation.valueCodeableConcept.coding` (254) |
| 13 | 265–281 | Observation | 1153593003 | Weight for age z-score | `bbu` → `Observation.status` (265)<br>`zs_bbu` → `Observation.valueQuantity.value` (268) |
| 14 | 282–299 | Observation | 1153604005 | Body height for age z-score | `tbu` → `Observation.status` (282)<br>`zs_tbu` → `Observation.valueQuantity.value` (286) |
| 15 | 300–319 | Observation | 1153600001 | Weight for height z-score | `bbtb` → `Observation.status` (300)<br>`zs_bbtb` → `Observation.valueQuantity.value` (304) |
| 16 | 320–328 | Procedure | 767224000 | Administration of vitamin A | `jml_vit_a` → `Procedure.category.coding` (320) |
| 17 | 329–355 | MedicationRequest | 92000809 | Retinol Palmitate 200.000 IU Kapsul Lunak | _Jml Vit A_ → `MedicationRequest.contained.resourceType` (329, tanpa BQ) |
| 18 | 356–381 | MedicationDispense | 93018284 | Retinol Palmitate 200.000 IU Kapsul Lunak (Umum) | – |
| 19 | 382–408 | MedicationRequest | 92000354 | Retinol Palmitate 100.000 IU Kapsul Lunak | – |
| 20 | 409–434 | MedicationDispense | 93018284 | Retinol Palmitate 100.000 IU Kapsul Lunak (Umum) | – |
| 21 | 435–446 | Observation | SP000022 | KPSP | `kpsp` → `Observation.valueString` (438) |
| 22 | 447–458 | Observation | SP000023 | KIA | `kia` → `Observation.valueString` (450) |
| 23 | 459–470 | QuestionnaireResponse | https://fhir.kemkes.go.id/Questionnaire/Q0004 | – | `kelas_ibu_balita` → `QuestionnaireResponse.questionnaire` (459) |
| 24 | 471–481 | Observation | SP000510 | Mendapat Makanan Bergizi Gratis (MBG) bulan ini | _Menerima MBG Bulan Ini_ → `Observation.status` (471, tanpa BQ)<br>`mbg` → `Observation.valueBoolean` (474) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 14 |
| MedicationRequest | 2 |
| MedicationDispense | 2 |
| Patient | 1 |
| RelatedPerson | 1 |
| Encounter | 1 |
| Condition | 1 |
| Procedure | 1 |
| QuestionnaireResponse | 1 |
| **Total** | **24** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 140 | Condition | `Condition.code.coding` | 385984007 | Growth and development treatments and procedures | http://snomed.info/sct |
| 2 | 160 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 3 | 163 | Observation | `Observation.component.code.coding` | SP000020 | Umur Bulan | http://terminology.kemkes.go.id/sp |
| 4 | 166 | Observation | `Observation.component.code.coding` | SP000021 | Umur Hari | http://terminology.kemkes.go.id/sp |
| 5 | 179 | Observation | `Observation.code.coding` | 8339-4 | Birth weight Measured | http://loinc.org |
| 6 | 192 | Observation | `Observation.code.coding` | 89269-5 | Body height Measured --at birth | http://loinc.org |
| 7 | 204 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 8 | 216 | Observation | `Observation.code.coding` | 8308-9 | Body height --standing | http://loinc.org |
| 9 | 217 | Observation | `Observation.code.coding` | 8306-3 | Body height --lying | http://loinc.org |
| 10 | 229 | Observation | `Observation.code.coding` | 50373000 | Body height measure | http://loinc.org |
| 11 | 230 | Observation | `Observation.method.coding` | 10904000 | Standing position | http://snomed.info/sct |
| 12 | 231 | Observation | `Observation.method.coding` | 102538003 | Recumbent body position | http://snomed.info/sct |
| 13 | 241 | Observation | `Observation.code.coding` | 284473002 | Mid upper arm circumference | http://snomed.info/sct |
| 14 | 253 | Observation | `Observation.code.coding` | 365910001 | Weight trend finding | http://snomed.info/sct |
| 15 | 254 | Observation | `Observation.valueCodeableConcept.coding` | SP000018 | Baru Pertama Kali Ditimbang | http://terminology.kemkes.go.id/sp |
| 16 | 255 | Observation | `Observation.valueCodeableConcept.coding` | 8943002 | Weight gain | http://snomed.info/sct |
| 17 | 256 | Observation | `Observation.valueCodeableConcept.coding` | SP000019 | Tidak Ditimbang Bulan Lalu | http://terminology.kemkes.go.id/sp |
| 18 | 257 | Observation | `Observation.valueCodeableConcept.coding` | 36440009 | Failure to gain weight | http://snomed.info/sct |
| 19 | 267 | Observation | `Observation.code.coding` | 1153593003 | Weight for age z-score | http://snomed.info/sct |
| 20 | 270 | Observation | `Observation.interpretation.coding` | 248342006 | Underweight | http://snomed.info/sct |
| 21 | 271 | Observation | `Observation.interpretation.coding` | 43664005 | Normal weight | http://snomed.info/sct |
| 22 | 272 | Observation | `Observation.interpretation.coding` | SP000017 | Outlier | http://terminology.kemkes.go.id/sp |
| 23 | 273 | Observation | `Observation.interpretation.coding` | OI000010 | Risiko Berat Badan Lebih | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 24 | 274 | Observation | `Observation.interpretation.coding` | OI000007 | Berat Badan Sangat Kurang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 25 | 284 | Observation | `Observation.code.coding` | 1153604005 | Body height for age z-score | http://snomed.info/sct |
| 26 | 285 | Observation | `Observation.code.coding` | 1153590000 | Length for age z score | http://snomed.info/sct |
| 27 | 288 | Observation | `Observation.interpretation.coding` | 17489000 | Body height normal for age | http://snomed.info/sct |
| 28 | 289 | Observation | `Observation.interpretation.coding` | SP000017 | Outlier | http://terminology.kemkes.go.id/sp |
| 29 | 290 | Observation | `Observation.interpretation.coding` | 444000005 | Short stature for age | http://snomed.info/sct |
| 30 | 291 | Observation | `Observation.interpretation.coding` | OI000011 | Sangat Pendek | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 31 | 292 | Observation | `Observation.interpretation.coding` | 83077003 | Tall for age | http://snomed.info/sct |
| 32 | 302 | Observation | `Observation.code.coding` | 1153600001 | Weight for height z-score | http://snomed.info/sct |
| 33 | 303 | Observation | `Observation.code.coding` | 1153598007 | Weight for length z score | http://snomed.info/sct |
| 34 | 306 | Observation | `Observation.interpretation.coding` | 248324001 | Well nourished | http://snomed.info/sct |
| 35 | 307 | Observation | `Observation.interpretation.coding` | OI000001 | Gizi Buruk | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 36 | 308 | Observation | `Observation.interpretation.coding` | 248325000 | Undernourished | http://snomed.info/sct |
| 37 | 309 | Observation | `Observation.interpretation.coding` | 238131007 | Overweight | http://snomed.info/sct |
| 38 | 310 | Observation | `Observation.interpretation.coding` | 414915002 | Obese | http://snomed.info/sct |
| 39 | 311 | Observation | `Observation.interpretation.coding` | SP000017 | Outlier | http://terminology.kemkes.go.id/sp |
| 40 | 312 | Observation | `Observation.interpretation.coding` | OI000004 | Risiko Gizi Lebih | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 41 | 321 | Procedure | `Procedure.code.coding` | 767224000 | Administration of vitamin A | http://snomed.info/sct |
| 42 | 332 | MedicationRequest | `MedicationRequest.contained.code.coding` | 92000809 | Retinol Palmitate 200.000 IU Kapsul Lunak | http://sys-ids.kemkes.go.id/kfa |
| 43 | 359 | MedicationDispense | `MedicationDispense.contained.code.coding` | 93018284 | Retinol Palmitate 200.000 IU Kapsul Lunak (Umum) | http://sys-ids.kemkes.go.id/kfa |
| 44 | 385 | MedicationRequest | `MedicationRequest.contained.code.coding` | 92000354 | Retinol Palmitate 100.000 IU Kapsul Lunak | http://sys-ids.kemkes.go.id/kfa |
| 45 | 412 | MedicationDispense | `MedicationDispense.contained.code.coding` | 93018284 | Retinol Palmitate 100.000 IU Kapsul Lunak (Umum) | http://sys-ids.kemkes.go.id/kfa |
| 46 | 437 | Observation | `Observation.code.coding` | SP000022 | KPSP | http://terminology.kemkes.go.id/sp |
| 47 | 439 | Observation | `Observation.dataAbsentReason` | unknown | Unknown | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 48 | 449 | Observation | `Observation.code.coding` | SP000023 | KIA | http://terminology.kemkes.go.id/sp |
| 49 | 451 | Observation | `Observation.dataAbsentReason` | unknown | Unknown | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 50 | 473 | Observation | `Observation.code.coding` | SP000510 | Mendapat Makanan Bergizi Gratis (MBG) bulan ini | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 23 |
| http://terminology.kemkes.go.id/sp | 10 |
| http://loinc.org | 6 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 5 |
| http://sys-ids.kemkes.go.id/kfa | 4 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 2 |
| **Total** | **50** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
