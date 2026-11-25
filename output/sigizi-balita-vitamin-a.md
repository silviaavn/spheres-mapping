# Output Form: SiGizi Balita Vitamin A

Sumber: `mapping/phdt-data-dictionary-sigizi-balita-vitamin-a.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-sigizi-balita-vitamin-a.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 22 |
| Code (`jumlah code` = 1) | 51 |
| Code unik (code + CodeSystem) | 47 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 9 |
| Variabel BQ (unik) | 34 |
| Variabel raw (variabel dictionary; belum ada file mentah) | 14 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 3–32 | Patient | – | – | `nama` → `Patient.name.text` (3)<br>`nik` → `Patient.identifier.value` (6)<br>`jk` → `Patient.gender` (8)<br>`tgl_lahir` → `Patient.birthDate` (10)<br>_Alamat Domisili_ → `Patient.address.use` (11, tanpa BQ)<br>`alamat` → `Patient.address.line` (12)<br>`kabkota` → `Patient.address.city` (13)<br>_Nama Provinsi_ → `Patient.address.extension.url` (15, tanpa BQ)<br>`prov` → `Patient.address.extension.extension.valueCode` (17)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (20, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.url` (21, tanpa BQ)<br>`kec` → `Patient.address.extension.extension.valueCode` (23)<br>_Nama Desa_ → `Patient.address.extension.url` (24, tanpa BQ)<br>`desakel` → `Patient.address.extension.extension.valueCode` (26)<br>`rw` → `Patient.address.extension.extension.valueCode` (29)<br>`rt` → `Patient.address.extension.extension.valueCode` (32) |
| 2 | 118–121 | RelatedPerson | – | – | `nama_ortu` → `RelatedPerson.patient` (118) |
| 3 | 122–137 | Encounter | – | – | `tanggal_pengukuran` → `Encounter.period.start` (131)<br>`posyandu` → `Encounter.location.location.reference` (133) 🔎 lookup master data<br>`pukesmas` → `Encounter.serviceProvider.reference` (137) 🔎 lookup master data<br>`detail` → `Encounter.extension.valueString` (160) |
| 4 | 138–144 | Condition | 385984007 | Growth and development treatments and procedures | – |
| 5 | 161–178 | Observation | 424144002 | Current chronological age | `usia_saat_ukur` → `Observation.valueQuantity.value` (164) |
| 6 | 179–191 | Observation | 8339-4 | Birth weight Measured | `bb_lahir` → `Observation.valueQuantity.value` (183) |
| 7 | 192–204 | Observation | 89269-5 | Body height Measured --at birth | `tb_lahir` → `Observation.valueQuantity.value` (196) |
| 8 | 205–217 | Observation | 29463-7 | Body weight | `berat` → `Observation.valueQuantity.value` (208) |
| 9 | 218–231 | Observation | 8308-9 | Body height --standing | `tinggi` → `Observation.valueQuantity.value` (222) |
| 10 | 232–243 | Observation | 50373000 | Body height measure | `cara_ukur` → `Observation.status` (232) |
| 11 | 244–255 | Observation | 284473002 | Mid upper arm circumference | `lila` → `Observation.valueQuantity.value` (247) |
| 12 | 256–269 | Observation | 365910001 | Weight trend finding | `naik_berat_badan` → `Observation.valueCodeableConcept.coding` (259) |
| 13 | 270–286 | Observation | 1153593003 | Weight for age z-score | `bbu` → `Observation.status` (270)<br>`zs_bbu` → `Observation.valueQuantity.value` (273) |
| 14 | 287–304 | Observation | 1153604005 | Body height for age z-score | `tbu` → `Observation.status` (287)<br>`zs_tbu` → `Observation.valueQuantity.value` (291) |
| 15 | 305–324 | Observation | 1153600001 | Weight for height z-score | `bbtb` → `Observation.status` (305)<br>`zs_bbtb` → `Observation.valueQuantity.value` (309) |
| 16 | 325–334 | Procedure | 767224000 | Administration of vitamin A | `jml_vit_a` → `Procedure.category.coding` (325)<br>`tanggal_pemberian` → `Procedure.performedPeriod.start` (331) |
| 17 | 335–361 | MedicationRequest | 92000809 | Retinol Palmitate 200.000 IU Kapsul Lunak | _Jml Vit A_ → `MedicationRequest.contained.resourceType` (335, tanpa BQ) |
| 18 | 362–387 | MedicationDispense | 93018284 | Retinol Palmitate 200.000 IU Kapsul Lunak (Umum) | – |
| 19 | 388–414 | MedicationRequest | 92000354 | Retinol Palmitate 100.000 IU Kapsul Lunak | – |
| 20 | 415–440 | MedicationDispense | 93018284 | Retinol Palmitate 100.000 IU Kapsul Lunak (Umum) | – |
| 21 | 441–452 | Observation | SP000022 | KPSP | `kpsp` → `Observation.valueString` (444) |
| 22 | 453–464 | Observation | SP000023 | KIA | `kia` → `Observation.valueString` (456) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 13 |
| MedicationRequest | 2 |
| MedicationDispense | 2 |
| Patient | 1 |
| RelatedPerson | 1 |
| Encounter | 1 |
| Condition | 1 |
| Procedure | 1 |
| **Total** | **22** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 140 | Condition | `Condition.code.coding` | 385984007 | Growth and development treatments and procedures | http://snomed.info/sct |
| 2 | 163 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 3 | 166 | Observation | `Observation.component.code.coding` | SP000020 | Umur Bulan | http://terminology.kemkes.go.id/sp |
| 4 | 169 | Observation | `Observation.component.code.coding` | SP000021 | Umur Hari | http://terminology.kemkes.go.id/sp |
| 5 | 182 | Observation | `Observation.code.coding` | 8339-4 | Birth weight Measured | http://loinc.org |
| 6 | 195 | Observation | `Observation.code.coding` | 89269-5 | Body height Measured --at birth | http://loinc.org |
| 7 | 207 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 8 | 210 | Observation | `Observation.dataAbsentReason` | not-a-number | Not a Number (NaN) | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 9 | 220 | Observation | `Observation.code.coding` | 8308-9 | Body height --standing | http://loinc.org |
| 10 | 221 | Observation | `Observation.code.coding` | 8306-3 | Body height --lying | http://loinc.org |
| 11 | 224 | Observation | `Observation.dataAbsentReason` | not-a-number | Not a Number (NaN) | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 12 | 234 | Observation | `Observation.code.coding` | 50373000 | Body height measure | http://loinc.org |
| 13 | 235 | Observation | `Observation.method.coding` | 10904000 | Standing position | http://snomed.info/sct |
| 14 | 236 | Observation | `Observation.method.coding` | 102538003 | Recumbent body position | http://snomed.info/sct |
| 15 | 246 | Observation | `Observation.code.coding` | 284473002 | Mid upper arm circumference | http://snomed.info/sct |
| 16 | 258 | Observation | `Observation.code.coding` | 365910001 | Weight trend finding | http://snomed.info/sct |
| 17 | 259 | Observation | `Observation.valueCodeableConcept.coding` | SP000018 | Baru Pertama Kali Ditimbang | http://terminology.kemkes.go.id/sp |
| 18 | 260 | Observation | `Observation.valueCodeableConcept.coding` | 8943002 | Weight gain | http://snomed.info/sct |
| 19 | 261 | Observation | `Observation.valueCodeableConcept.coding` | SP000019 | Tidak Ditimbang Bulan Lalu | http://terminology.kemkes.go.id/sp |
| 20 | 262 | Observation | `Observation.valueCodeableConcept.coding` | 36440009 | Failure to gain weight | http://snomed.info/sct |
| 21 | 272 | Observation | `Observation.code.coding` | 1153593003 | Weight for age z-score | http://snomed.info/sct |
| 22 | 275 | Observation | `Observation.interpretation.coding` | 248342006 | Underweight | http://snomed.info/sct |
| 23 | 276 | Observation | `Observation.interpretation.coding` | 43664005 | Normal weight | http://snomed.info/sct |
| 24 | 277 | Observation | `Observation.interpretation.coding` | SP000017 | Outlier | http://terminology.kemkes.go.id/sp |
| 25 | 278 | Observation | `Observation.interpretation.coding` | OI000010 | Risiko Berat Badan Lebih | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 26 | 279 | Observation | `Observation.interpretation.coding` | OI000007 | Berat Badan Sangat Kurang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 27 | 289 | Observation | `Observation.code.coding` | 1153604005 | Body height for age z-score | http://snomed.info/sct |
| 28 | 290 | Observation | `Observation.code.coding` | 1153590000 | Length for age z score | http://snomed.info/sct |
| 29 | 293 | Observation | `Observation.interpretation.coding` | 17489000 | Body height normal for age | http://snomed.info/sct |
| 30 | 294 | Observation | `Observation.interpretation.coding` | SP000017 | Outlier | http://terminology.kemkes.go.id/sp |
| 31 | 295 | Observation | `Observation.interpretation.coding` | 444000005 | Short stature for age | http://snomed.info/sct |
| 32 | 296 | Observation | `Observation.interpretation.coding` | OI000011 | Sangat Pendek | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 33 | 297 | Observation | `Observation.interpretation.coding` | 83077003 | Tall for age | http://snomed.info/sct |
| 34 | 307 | Observation | `Observation.code.coding` | 1153600001 | Weight for height z-score | http://snomed.info/sct |
| 35 | 308 | Observation | `Observation.code.coding` | 1153598007 | Weight for length z score | http://snomed.info/sct |
| 36 | 311 | Observation | `Observation.interpretation.coding` | 248324001 | Well nourished | http://snomed.info/sct |
| 37 | 312 | Observation | `Observation.interpretation.coding` | OI000001 | Gizi Buruk | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 38 | 313 | Observation | `Observation.interpretation.coding` | 248325000 | Undernourished | http://snomed.info/sct |
| 39 | 314 | Observation | `Observation.interpretation.coding` | 238131007 | Overweight | http://snomed.info/sct |
| 40 | 315 | Observation | `Observation.interpretation.coding` | 414915002 | Obese | http://snomed.info/sct |
| 41 | 316 | Observation | `Observation.interpretation.coding` | SP000017 | Outlier | http://terminology.kemkes.go.id/sp |
| 42 | 317 | Observation | `Observation.interpretation.coding` | OI000004 | Risiko Gizi Lebih | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 43 | 326 | Procedure | `Procedure.code.coding` | 767224000 | Administration of vitamin A | http://snomed.info/sct |
| 44 | 338 | MedicationRequest | `MedicationRequest.contained.code.coding` | 92000809 | Retinol Palmitate 200.000 IU Kapsul Lunak | http://sys-ids.kemkes.go.id/kf |
| 45 | 365 | MedicationDispense | `MedicationDispense.contained.code.coding` | 93018284 | Retinol Palmitate 200.000 IU Kapsul Lunak (Umum) | http://sys-ids.kemkes.go.id/kf |
| 46 | 391 | MedicationRequest | `MedicationRequest.contained.code.coding` | 92000354 | Retinol Palmitate 100.000 IU Kapsul Lunak | http://sys-ids.kemkes.go.id/kf |
| 47 | 418 | MedicationDispense | `MedicationDispense.contained.code.coding` | 93018284 | Retinol Palmitate 100.000 IU Kapsul Lunak (Umum) | http://sys-ids.kemkes.go.id/kfa |
| 48 | 443 | Observation | `Observation.code.coding` | SP000022 | KPSP | http://terminology.kemkes.go.id/sp |
| 49 | 445 | Observation | `Observation.dataAbsentReason` | unknown | Unknown | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 50 | 455 | Observation | `Observation.code.coding` | SP000023 | KIA | http://terminology.kemkes.go.id/sp |
| 51 | 457 | Observation | `Observation.dataAbsentReason` | unknown | Unknown | http://terminology.hl7.org/CodeSystem/data-absent-reason |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 23 |
| http://terminology.kemkes.go.id/sp | 9 |
| http://loinc.org | 6 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 5 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 4 |
| http://sys-ids.kemkes.go.id/kf | 3 |
| http://sys-ids.kemkes.go.id/kfa | 1 |
| **Total** | **51** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
