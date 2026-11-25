# Output Form: SiGizi PMT 2025 Gizi Kurang - Riwayat

Sumber: `mapping/phdt-data-dictionary-sigizi-pmt2025-gizi-kurang-riwayat.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-sigizi-pmt2025-gizi-kurang-riwayat.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 19 |
| Code (`jumlah code` = 1) | 75 |
| Code unik (code + CodeSystem) | 43 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 23 |
| Variabel BQ (unik) | 34 |
| Variabel raw (variabel dictionary; belum ada file mentah) | 34 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 4–26 | Patient | – | – | `nama` → `Patient.name.text` (4)<br>`nik` → `Patient.identifier.value` (7)<br>`jk` → `Patient.gender` (9)<br>`tgl_lahir` → `Patient.birthDate` (11)<br>`prov` → `Patient.address.extension.extension.valueCode` (17)<br>`kabkota` → `Patient.address.extension.extension.valueCode` (20)<br>`kec` → `Patient.address.extension.extension.valueCode` (23)<br>`desakel` → `Patient.address.extension.extension.valueCode` (26) |
| 2 | 112–127 | Encounter | – | – | `tanggal_pengukuran_awal` → `Encounter.period.start` (121)<br>`posyandu` → `Encounter.location.location.reference` (123) 🔎 lookup master data<br>`pukesmas` → `Encounter.serviceProvider.reference` (127) 🔎 lookup master data<br>`tindakan` → `Encounter.extension.valueString` (147) |
| 3 | 128–134 | Condition | 385984007 | Growth and development treatments and procedures | – |
| 4 | 148–160 | Observation | SP000041 | Sumber Anggaran PMT | `sumber_anggaran` → `Observation.valueCodeableConcept.coding` (151) |
| 5 | 161–177 | Observation | SP000491 | Mitra Pemberi MT | `mitra` → `Observation.valueCodeableConcept.coding` (164) |
| 6 | 178–190 | Observation | 29463-7 | Body weight | `bb_awal` → `Observation.valueQuantity.value` (182) |
| 7 | 191–204 | Observation | 8308-9 | Body height --standing | `tb_awal` → `Observation.valueQuantity.value` (196) |
| 8 | 205–222 | Observation | 1153593003 | Weight for age z-score | `zs_bbu_awal` → `Observation.valueQuantity.value` (209)<br>`bbu_awal` → `Observation.interpretation.coding` (211) |
| 9 | 223–241 | Observation | 1153604005 | Body height for age z-score | `zs_tbu_awal` → `Observation.valueQuantity.value` (228)<br>`tbu_awal` → `Observation.interpretation.coding` (230) |
| 10 | 242–262 | Observation | 1153600001 | Weight for height z-score | `zs_bbtb_awal` → `Observation.valueQuantity.value` (247)<br>`bbtb_awal` → `Observation.interpretation.coding` (249) |
| 11 | 263–277 | Observation | 365910001 | Weight trend finding | `status_pertumbuhan` → `Observation.valueCodeableConcept.coding` (267) |
| 12 | 278–290 | Observation | 29463-7 | Body weight | `bb_akhir` → `Observation.valueQuantity.value` (282) |
| 13 | 291–304 | Observation | 8308-9 | Body height --standing | `tb_akhir` → `Observation.valueQuantity.value` (296) |
| 14 | 305–322 | Observation | 1153593003 | Weight for age z-score | `zs_bbu_akhir` → `Observation.valueQuantity.value` (309)<br>`bbu_akhir` → `Observation.interpretation.coding` (311) |
| 15 | 323–341 | Observation | 1153604005 | Body height for age z-score | `zs_tbu_akhir` → `Observation.valueQuantity.value` (328)<br>`tbu_akhir` → `Observation.interpretation.coding` (330) |
| 16 | 342–362 | Observation | 1153600001 | Weight for height z-score | `zs_bbtb_akhir` → `Observation.valueQuantity.value` (347)<br>`bbtb_akhir` → `Observation.interpretation.coding` (349) |
| 17 | 363–377 | Observation | 365910001 | Weight trend finding | `status_kenaikan_bb` → `Observation.valueCodeableConcept.coding` (367) |
| 18 | 378–388 | Observation | SP000490 | Siklus Pemberian Makanan Tambahan | `siklus_pmt` → `Observation.valueInteger` (381) |
| 19 | 389–399 | Observation | SP000492 | Jumlah Pemantauan PMT | `jumlah_pemantauan` → `Observation.valueInteger` (392) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 16 |
| Patient | 1 |
| Encounter | 1 |
| Condition | 1 |
| **Total** | **19** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 130 | Condition | `Condition.code.coding` | 385984007 | Growth and development treatments and procedures | http://snomed.info/sct |
| 2 | 150 | Observation | `Observation.code.coding` | SP000041 | Sumber Anggaran PMT | http://terminology.kemkes.go.id/sp |
| 3 | 151 | Observation | `Observation.valueCodeableConcept.coding` | SP000042 | APBD | http://terminology.kemkes.go.id/sp |
| 4 | 152 | Observation | `Observation.valueCodeableConcept.coding` | SP000159 | Mitra | http://terminology.kemkes.go.id/sp |
| 5 | 153 | Observation | `Observation.valueCodeableConcept.coding` | SP000158 | DAK (Dana Alokasi Khusus) | http://terminology.kemkes.go.id/sp |
| 6 | 163 | Observation | `Observation.code.coding` | SP000491 | Mitra Pemberi MT | http://terminology.kemkes.go.id/sp |
| 7 | 164 | Observation | `Observation.valueCodeableConcept.coding` | SP000483 | Benih Baik | http://terminology.kemkes.go.id/sp |
| 8 | 165 | Observation | `Observation.valueCodeableConcept.coding` | SP000484 | Astra | http://terminology.kemkes.go.id/sp |
| 9 | 166 | Observation | `Observation.valueCodeableConcept.coding` | SP000485 | Kadin | http://terminology.kemkes.go.id/sp |
| 10 | 167 | Observation | `Observation.valueCodeableConcept.coding` | SP000486 | APINDO | http://terminology.kemkes.go.id/sp |
| 11 | 168 | Observation | `Observation.valueCodeableConcept.coding` | SP000487 | Seruni | http://terminology.kemkes.go.id/sp |
| 12 | 169 | Observation | `Observation.valueCodeableConcept.coding` | SP000488 | Mitra Lain | http://terminology.kemkes.go.id/sp |
| 13 | 170 | Observation | `Observation.dataAbsentReason` | unknown | Unknown | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 14 | 181 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 15 | 194 | Observation | `Observation.code.coding` | 8308-9 | Body height --standing | http://loinc.org |
| 16 | 195 | Observation | `Observation.code.coding` | 8306-3 | Body height --lying | http://loinc.org |
| 17 | 208 | Observation | `Observation.code.coding` | 1153593003 | Weight for age z-score | http://snomed.info/sct |
| 18 | 211 | Observation | `Observation.interpretation.coding` | 248342006 | Underweight | http://snomed.info/sct |
| 19 | 212 | Observation | `Observation.interpretation.coding` | 43664005 | Normal weight | http://snomed.info/sct |
| 20 | 213 | Observation | `Observation.interpretation.coding` | SP000017 | Outlier | http://terminology.kemkes.go.id/sp |
| 21 | 214 | Observation | `Observation.interpretation.coding` | OI000010 | Risiko Berat Badan Lebih | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 22 | 215 | Observation | `Observation.interpretation.coding` | OI000007 | Berat Badan Sangat Kurang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 23 | 226 | Observation | `Observation.code.coding` | 1153604005 | Body height for age z-score | http://snomed.info/sct |
| 24 | 227 | Observation | `Observation.code.coding` | 1153590000 | Length for age z score | http://snomed.info/sct |
| 25 | 230 | Observation | `Observation.interpretation.coding` | 17489000 | Body height normal for age | http://snomed.info/sct |
| 26 | 231 | Observation | `Observation.interpretation.coding` | SP000017 | Outlier | http://terminology.kemkes.go.id/sp |
| 27 | 232 | Observation | `Observation.interpretation.coding` | 444000005 | Short stature for age | http://snomed.info/sct |
| 28 | 233 | Observation | `Observation.interpretation.coding` | OI000011 | Sangat Pendek | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 29 | 234 | Observation | `Observation.interpretation.coding` | 83077003 | Tall for age | http://snomed.info/sct |
| 30 | 245 | Observation | `Observation.code.coding` | 1153600001 | Weight for height z-score | http://snomed.info/sct |
| 31 | 246 | Observation | `Observation.code.coding` | 1153598007 | Weight for length z score | http://snomed.info/sct |
| 32 | 249 | Observation | `Observation.interpretation.coding` | 248324001 | Well nourished | http://snomed.info/sct |
| 33 | 250 | Observation | `Observation.interpretation.coding` | OI000001 | Gizi Buruk | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 34 | 251 | Observation | `Observation.interpretation.coding` | 248325000 | Undernourished | http://snomed.info/sct |
| 35 | 252 | Observation | `Observation.interpretation.coding` | 238131007 | Overweight | http://snomed.info/sct |
| 36 | 253 | Observation | `Observation.interpretation.coding` | 414915002 | Obese | http://snomed.info/sct |
| 37 | 254 | Observation | `Observation.interpretation.coding` | SP000017 | Outlier | http://terminology.kemkes.go.id/sp |
| 38 | 255 | Observation | `Observation.interpretation.coding` | OI000004 | Risiko Gizi Lebih | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 39 | 266 | Observation | `Observation.code.coding` | 365910001 | Weight trend finding | http://snomed.info/sct |
| 40 | 267 | Observation | `Observation.valueCodeableConcept.coding` | SP000018 | Baru Pertama Kali Ditimbang | http://terminology.kemkes.go.id/sp |
| 41 | 268 | Observation | `Observation.valueCodeableConcept.coding` | 8943002 | Weight gain | http://snomed.info/sct |
| 42 | 269 | Observation | `Observation.valueCodeableConcept.coding` | SP000019 | Tidak Ditimbang Bulan Lalu | http://terminology.kemkes.go.id/sp |
| 43 | 270 | Observation | `Observation.valueCodeableConcept.coding` | 36440009 | Failure to gain weight | http://snomed.info/sct |
| 44 | 281 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 45 | 294 | Observation | `Observation.code.coding` | 8308-9 | Body height --standing | http://loinc.org |
| 46 | 295 | Observation | `Observation.code.coding` | 8306-3 | Body height --lying | http://loinc.org |
| 47 | 308 | Observation | `Observation.code.coding` | 1153593003 | Weight for age z-score | http://snomed.info/sct |
| 48 | 311 | Observation | `Observation.interpretation.coding` | 248342006 | Underweight | http://snomed.info/sct |
| 49 | 312 | Observation | `Observation.interpretation.coding` | 43664005 | Normal weight | http://snomed.info/sct |
| 50 | 313 | Observation | `Observation.interpretation.coding` | SP000017 | Outlier | http://terminology.kemkes.go.id/sp |
| 51 | 314 | Observation | `Observation.interpretation.coding` | OI000010 | Risiko Berat Badan Lebih | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 52 | 315 | Observation | `Observation.interpretation.coding` | OI000007 | Berat Badan Sangat Kurang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 53 | 326 | Observation | `Observation.code.coding` | 1153604005 | Body height for age z-score | http://snomed.info/sct |
| 54 | 327 | Observation | `Observation.code.coding` | 1153590000 | Length for age z score | http://snomed.info/sct |
| 55 | 330 | Observation | `Observation.interpretation.coding` | 17489000 | Body height normal for age | http://snomed.info/sct |
| 56 | 331 | Observation | `Observation.interpretation.coding` | SP000017 | Outlier | http://terminology.kemkes.go.id/sp |
| 57 | 332 | Observation | `Observation.interpretation.coding` | 444000005 | Short stature for age | http://snomed.info/sct |
| 58 | 333 | Observation | `Observation.interpretation.coding` | OI000011 | Sangat Pendek | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 59 | 334 | Observation | `Observation.interpretation.coding` | 83077003 | Tall for age | http://snomed.info/sct |
| 60 | 345 | Observation | `Observation.code.coding` | 1153600001 | Weight for height z-score | http://snomed.info/sct |
| 61 | 346 | Observation | `Observation.code.coding` | 1153598007 | Weight for length z score | http://snomed.info/sct |
| 62 | 349 | Observation | `Observation.interpretation.coding` | 248324001 | Well nourished | http://snomed.info/sct |
| 63 | 350 | Observation | `Observation.interpretation.coding` | OI000001 | Gizi Buruk | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 64 | 351 | Observation | `Observation.interpretation.coding` | 248325000 | Undernourished | http://snomed.info/sct |
| 65 | 352 | Observation | `Observation.interpretation.coding` | 238131007 | Overweight | http://snomed.info/sct |
| 66 | 353 | Observation | `Observation.interpretation.coding` | 414915002 | Obese | http://snomed.info/sct |
| 67 | 354 | Observation | `Observation.interpretation.coding` | SP000017 | Outlier | http://terminology.kemkes.go.id/sp |
| 68 | 355 | Observation | `Observation.interpretation.coding` | OI000004 | Risiko Gizi Lebih | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 69 | 366 | Observation | `Observation.code.coding` | 365910001 | Weight trend finding | http://snomed.info/sct |
| 70 | 367 | Observation | `Observation.valueCodeableConcept.coding` | SP000018 | Baru Pertama Kali Ditimbang | http://terminology.kemkes.go.id/sp |
| 71 | 368 | Observation | `Observation.valueCodeableConcept.coding` | 8943002 | Weight gain | http://snomed.info/sct |
| 72 | 369 | Observation | `Observation.valueCodeableConcept.coding` | SP000019 | Tidak Ditimbang Bulan Lalu | http://terminology.kemkes.go.id/sp |
| 73 | 370 | Observation | `Observation.valueCodeableConcept.coding` | 36440009 | Failure to gain weight | http://snomed.info/sct |
| 74 | 380 | Observation | `Observation.code.coding` | SP000490 | Siklus Pemberian Makanan Tambahan | http://terminology.kemkes.go.id/sp |
| 75 | 391 | Observation | `Observation.code.coding` | SP000492 | Jumlah Pemantauan PMT | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 35 |
| http://terminology.kemkes.go.id/sp | 23 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 10 |
| http://loinc.org | 6 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 1 |
| **Total** | **75** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
