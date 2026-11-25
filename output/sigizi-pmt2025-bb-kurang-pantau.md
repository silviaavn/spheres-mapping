# Output Form: SiGizi PMT 2025 BB Kurang - Pantau

Sumber: `mapping/phdt-data-dictionary-sigizi-pmt2025-bb-kurang-pantau.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-sigizi-pmt2025-bb-kurang-pantau.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 21 |
| Code (`jumlah code` = 1) | 47 |
| Code unik (code + CodeSystem) | 24 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 21 |
| Variabel BQ (unik) | 24 |
| Variabel raw (variabel dictionary; belum ada file mentah) | 24 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 3–25 | Patient | – | – | `nama` → `Patient.name.text` (3)<br>`nik` → `Patient.identifier.value` (6)<br>`jk` → `Patient.gender` (8)<br>`tgl_lahir` → `Patient.birthDate` (10)<br>`prov` → `Patient.address.extension.extension.valueCode` (16)<br>`kabkota` → `Patient.address.extension.extension.valueCode` (19)<br>`kec` → `Patient.address.extension.extension.valueCode` (22)<br>`desakel` → `Patient.address.extension.extension.valueCode` (25) |
| 2 | 111–126 | Encounter | – | – | `tanggal_pengukuran_awal` → `Encounter.period.start` (120)<br>`posyandu` → `Encounter.location.location.reference` (122) 🔎 lookup master data<br>`pukesmas` → `Encounter.serviceProvider.reference` (126) 🔎 lookup master data<br>`tindakan` → `Encounter.extension.valueString` (146) |
| 3 | 127–133 | Condition | 385984007 | Growth and development treatments and procedures | – |
| 4 | 147–159 | Observation | SP000041 | Sumber Anggaran PMT | `sumber_anggaran` → `Observation.valueCodeableConcept.coding` (150) |
| 5 | 160–176 | Observation | SP000491 | Mitra Pemberi MT | `mitra` → `Observation.valueCodeableConcept.coding` (163) |
| 6 | 177–189 | Observation | 29463-7 | Body weight | `bb_awal` → `Observation.valueQuantity.value` (181) |
| 7 | 190–202 | Observation | 1153593003 | Weight for age z-score | `zs_bbu_awal` → `Observation.valueQuantity.value` (194) |
| 8 | 203–215 | Observation | 29463-7 | Body weight | `bb_minggu_1` → `Observation.valueQuantity.value` (207) |
| 9 | 216–228 | Observation | 1153593003 | Weight for age z-score | `zs_bbu_minggu_1` → `Observation.valueQuantity.value` (220) |
| 10 | 229–243 | Observation | 365910001 | Weight trend finding | `status_kenaikan_minggu_1` → `Observation.valueCodeableConcept.coding` (233) |
| 11 | 244–256 | Observation | 29463-7 | Body weight | `bb_minggu_2` → `Observation.valueQuantity.value` (248) |
| 12 | 257–269 | Observation | 1153593003 | Weight for age z-score | `zs_bbu_minggu_2` → `Observation.valueQuantity.value` (261) |
| 13 | 270–284 | Observation | 365910001 | Weight trend finding | `status_kenaikan_minggu_2` → `Observation.valueCodeableConcept.coding` (274) |
| 14 | 285–297 | Observation | 29463-7 | Body weight | _BB Minggu 3_ → `Observation.valueQuantity.value` (289, tanpa BQ) |
| 15 | 298–310 | Observation | 1153593003 | Weight for age z-score | _ZS BB/U Minggu 3_ → `Observation.valueQuantity.value` (302, tanpa BQ) |
| 16 | 311–325 | Observation | 365910001 | Weight trend finding | _Status Kenaikan Minggu 3_ → `Observation.valueCodeableConcept.coding` (315, tanpa BQ) |
| 17 | 326–338 | Observation | 29463-7 | Body weight | _BB Minggu 4_ → `Observation.valueQuantity.value` (330, tanpa BQ) |
| 18 | 339–351 | Observation | 1153593003 | Weight for age z-score | _ZS BB/U Minggu 4_ → `Observation.valueQuantity.value` (343, tanpa BQ) |
| 19 | 352–366 | Observation | 365910001 | Weight trend finding | _Status Kenaikan Minggu 4_ → `Observation.valueCodeableConcept.coding` (356, tanpa BQ) |
| 20 | 367–378 | Observation | SP000489 | Status Pemantauan Pemberian Makanan Tambahan | `status_pmt` → `Observation.valueCodeableConcept.coding` (370) |
| 21 | 379–389 | Observation | SP000490 | Siklus Pemberian Makanan Tambahan | `siklus_pmt` → `Observation.valueInteger` (382) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 18 |
| Patient | 1 |
| Encounter | 1 |
| Condition | 1 |
| **Total** | **21** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 129 | Condition | `Condition.code.coding` | 385984007 | Growth and development treatments and procedures | http://snomed.info/sct |
| 2 | 149 | Observation | `Observation.code.coding` | SP000041 | Sumber Anggaran PMT | http://terminology.kemkes.go.id/sp |
| 3 | 150 | Observation | `Observation.valueCodeableConcept.coding` | SP000042 | APBD | http://terminology.kemkes.go.id/sp |
| 4 | 151 | Observation | `Observation.valueCodeableConcept.coding` | SP000159 | Mitra | http://terminology.kemkes.go.id/sp |
| 5 | 152 | Observation | `Observation.valueCodeableConcept.coding` | SP000158 | DAK (Dana Alokasi Khusus) | http://terminology.kemkes.go.id/sp |
| 6 | 162 | Observation | `Observation.code.coding` | SP000491 | Mitra Pemberi MT | http://terminology.kemkes.go.id/sp |
| 7 | 163 | Observation | `Observation.valueCodeableConcept.coding` | SP000483 | Benih Baik | http://terminology.kemkes.go.id/sp |
| 8 | 164 | Observation | `Observation.valueCodeableConcept.coding` | SP000484 | Astra | http://terminology.kemkes.go.id/sp |
| 9 | 165 | Observation | `Observation.valueCodeableConcept.coding` | SP000485 | Kadin | http://terminology.kemkes.go.id/sp |
| 10 | 166 | Observation | `Observation.valueCodeableConcept.coding` | SP000486 | APINDO | http://terminology.kemkes.go.id/sp |
| 11 | 167 | Observation | `Observation.valueCodeableConcept.coding` | SP000487 | Seruni | http://terminology.kemkes.go.id/sp |
| 12 | 168 | Observation | `Observation.valueCodeableConcept.coding` | SP000488 | Mitra Lain | http://terminology.kemkes.go.id/sp |
| 13 | 169 | Observation | `Observation.dataAbsentReason` | unknown | Unknown | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 14 | 180 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 15 | 193 | Observation | `Observation.code.coding` | 1153593003 | Weight for age z-score | http://snomed.info/sct |
| 16 | 206 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 17 | 219 | Observation | `Observation.code.coding` | 1153593003 | Weight for age z-score | http://snomed.info/sct |
| 18 | 232 | Observation | `Observation.code.coding` | 365910001 | Weight trend finding | http://snomed.info/sct |
| 19 | 233 | Observation | `Observation.valueCodeableConcept.coding` | SP000018 | Baru Pertama Kali Ditimbang | http://terminology.kemkes.go.id/sp |
| 20 | 234 | Observation | `Observation.valueCodeableConcept.coding` | 8943002 | Weight gain | http://snomed.info/sct |
| 21 | 235 | Observation | `Observation.valueCodeableConcept.coding` | SP000019 | Tidak Ditimbang Bulan Lalu | http://terminology.kemkes.go.id/sp |
| 22 | 236 | Observation | `Observation.valueCodeableConcept.coding` | 36440009 | Failure to gain weight | http://snomed.info/sct |
| 23 | 247 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 24 | 260 | Observation | `Observation.code.coding` | 1153593003 | Weight for age z-score | http://snomed.info/sct |
| 25 | 273 | Observation | `Observation.code.coding` | 365910001 | Weight trend finding | http://snomed.info/sct |
| 26 | 274 | Observation | `Observation.valueCodeableConcept.coding` | SP000018 | Baru Pertama Kali Ditimbang | http://terminology.kemkes.go.id/sp |
| 27 | 275 | Observation | `Observation.valueCodeableConcept.coding` | 8943002 | Weight gain | http://snomed.info/sct |
| 28 | 276 | Observation | `Observation.valueCodeableConcept.coding` | SP000019 | Tidak Ditimbang Bulan Lalu | http://terminology.kemkes.go.id/sp |
| 29 | 277 | Observation | `Observation.valueCodeableConcept.coding` | 36440009 | Failure to gain weight | http://snomed.info/sct |
| 30 | 288 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 31 | 301 | Observation | `Observation.code.coding` | 1153593003 | Weight for age z-score | http://snomed.info/sct |
| 32 | 314 | Observation | `Observation.code.coding` | 365910001 | Weight trend finding | http://snomed.info/sct |
| 33 | 315 | Observation | `Observation.valueCodeableConcept.coding` | SP000018 | Baru Pertama Kali Ditimbang | http://terminology.kemkes.go.id/sp |
| 34 | 316 | Observation | `Observation.valueCodeableConcept.coding` | 8943002 | Weight gain | http://snomed.info/sct |
| 35 | 317 | Observation | `Observation.valueCodeableConcept.coding` | SP000019 | Tidak Ditimbang Bulan Lalu | http://terminology.kemkes.go.id/sp |
| 36 | 318 | Observation | `Observation.valueCodeableConcept.coding` | 36440009 | Failure to gain weight | http://snomed.info/sct |
| 37 | 329 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 38 | 342 | Observation | `Observation.code.coding` | 1153593003 | Weight for age z-score | http://snomed.info/sct |
| 39 | 355 | Observation | `Observation.code.coding` | 365910001 | Weight trend finding | http://snomed.info/sct |
| 40 | 356 | Observation | `Observation.valueCodeableConcept.coding` | SP000018 | Baru Pertama Kali Ditimbang | http://terminology.kemkes.go.id/sp |
| 41 | 357 | Observation | `Observation.valueCodeableConcept.coding` | 8943002 | Weight gain | http://snomed.info/sct |
| 42 | 358 | Observation | `Observation.valueCodeableConcept.coding` | SP000019 | Tidak Ditimbang Bulan Lalu | http://terminology.kemkes.go.id/sp |
| 43 | 359 | Observation | `Observation.valueCodeableConcept.coding` | 36440009 | Failure to gain weight | http://snomed.info/sct |
| 44 | 369 | Observation | `Observation.code.coding` | SP000489 | Status Pemantauan Pemberian Makanan Tambahan | http://terminology.kemkes.go.id/sp |
| 45 | 370 | Observation | `Observation.valueCodeableConcept.coding` | 385658003 | Done | http://snomed.info/sct |
| 46 | 371 | Observation | `Observation.valueCodeableConcept.coding` | 385651009 | In progress | http://snomed.info/sct |
| 47 | 381 | Observation | `Observation.code.coding` | SP000490 | Siklus Pemberian Makanan Tambahan | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://terminology.kemkes.go.id/sp | 21 |
| http://snomed.info/sct | 20 |
| http://loinc.org | 5 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 1 |
| **Total** | **47** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
