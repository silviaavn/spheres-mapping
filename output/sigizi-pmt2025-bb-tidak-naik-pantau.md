# Output Form: SiGizi PMT 2025 BB Tidak Naik - Pantau

Sumber: `mapping/phdt-data-dictionary-sigizi-pmt2025-bb-tidak-naik-pantau.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-sigizi-pmt2025-bb-tidak-naik-pantau.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 15 |
| Code (`jumlah code` = 1) | 33 |
| Code unik (code + CodeSystem) | 24 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 17 |
| Variabel BQ (unik) | 24 |
| Variabel raw (variabel dictionary; belum ada file mentah) | 24 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 4–26 | Patient | – | – | `nama` → `Patient.name.text` (4)<br>`nik` → `Patient.identifier.value` (7)<br>`jk` → `Patient.gender` (9)<br>`tgl_lahir` → `Patient.birthDate` (11)<br>`prov` → `Patient.address.extension.extension.valueCode` (17)<br>`kabkota` → `Patient.address.extension.extension.valueCode` (20)<br>`kec` → `Patient.address.extension.extension.valueCode` (23)<br>`desakel` → `Patient.address.extension.extension.valueCode` (26) |
| 2 | 112–127 | Encounter | – | – | `tanggal_pengukuran_awal` → `Encounter.period.start` (121)<br>`posyandu` → `Encounter.location.location.reference` (123) 🔎 lookup master data<br>`pukesmas` → `Encounter.serviceProvider.reference` (127) 🔎 lookup master data<br>`tindakan` → `Encounter.extension.valueString` (147) |
| 3 | 128–134 | Condition | 385984007 | Growth and development treatments and procedures | – |
| 4 | 148–160 | Observation | SP000041 | Sumber Anggaran PMT | `sumber_anggaran` → `Observation.valueCodeableConcept.coding` (151) |
| 5 | 161–177 | Observation | SP000491 | Mitra Pemberi MT | `mitra` → `Observation.valueCodeableConcept.coding` (164) |
| 6 | 178–190 | Observation | 29463-7 | Body weight | `bb_awal` → `Observation.valueQuantity.value` (182) |
| 7 | 191–203 | Observation | 1153593003 | Weight for age z-score | `zs_bbu_awal` → `Observation.valueQuantity.value` (195) |
| 8 | 204–216 | Observation | 29463-7 | Body weight | `bb_minggu_1` → `Observation.valueQuantity.value` (208) |
| 9 | 217–229 | Observation | 1153593003 | Weight for age z-score | `zs_bbu_minggu_1` → `Observation.valueQuantity.value` (221) |
| 10 | 230–244 | Observation | 365910001 | Weight trend finding | `status_kenaikan_minggu_1` → `Observation.valueCodeableConcept.coding` (234) |
| 11 | 245–257 | Observation | 29463-7 | Body weight | `bb_minggu_2` → `Observation.valueQuantity.value` (249) |
| 12 | 258–270 | Observation | 1153593003 | Weight for age z-score | `zs_bbu_minggu_2` → `Observation.valueQuantity.value` (262) |
| 13 | 271–285 | Observation | 365910001 | Weight trend finding | `status_kenaikan_minggu_2` → `Observation.valueCodeableConcept.coding` (275) |
| 14 | 286–297 | Observation | SP000489 | Status Pemantauan Pemberian Makanan Tambahan | `status_pmt` → `Observation.valueCodeableConcept.coding` (289) |
| 15 | 298–308 | Observation | SP000490 | Siklus Pemberian Makanan Tambahan | `siklus_pmt` → `Observation.valueInteger` (301) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 12 |
| Patient | 1 |
| Encounter | 1 |
| Condition | 1 |
| **Total** | **15** |

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
| 15 | 194 | Observation | `Observation.code.coding` | 1153593003 | Weight for age z-score | http://snomed.info/sct |
| 16 | 207 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 17 | 220 | Observation | `Observation.code.coding` | 1153593003 | Weight for age z-score | http://snomed.info/sct |
| 18 | 233 | Observation | `Observation.code.coding` | 365910001 | Weight trend finding | http://snomed.info/sct |
| 19 | 234 | Observation | `Observation.valueCodeableConcept.coding` | SP000018 | Baru Pertama Kali Ditimbang | http://terminology.kemkes.go.id/sp |
| 20 | 235 | Observation | `Observation.valueCodeableConcept.coding` | 8943002 | Weight gain | http://snomed.info/sct |
| 21 | 236 | Observation | `Observation.valueCodeableConcept.coding` | SP000019 | Tidak Ditimbang Bulan Lalu | http://terminology.kemkes.go.id/sp |
| 22 | 237 | Observation | `Observation.valueCodeableConcept.coding` | 36440009 | Failure to gain weight | http://snomed.info/sct |
| 23 | 248 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 24 | 261 | Observation | `Observation.code.coding` | 1153593003 | Weight for age z-score | http://snomed.info/sct |
| 25 | 274 | Observation | `Observation.code.coding` | 365910001 | Weight trend finding | http://snomed.info/sct |
| 26 | 275 | Observation | `Observation.valueCodeableConcept.coding` | SP000018 | Baru Pertama Kali Ditimbang | http://terminology.kemkes.go.id/sp |
| 27 | 276 | Observation | `Observation.valueCodeableConcept.coding` | 8943002 | Weight gain | http://snomed.info/sct |
| 28 | 277 | Observation | `Observation.valueCodeableConcept.coding` | SP000019 | Tidak Ditimbang Bulan Lalu | http://terminology.kemkes.go.id/sp |
| 29 | 278 | Observation | `Observation.valueCodeableConcept.coding` | 36440009 | Failure to gain weight | http://snomed.info/sct |
| 30 | 288 | Observation | `Observation.code.coding` | SP000489 | Status Pemantauan Pemberian Makanan Tambahan | http://terminology.kemkes.go.id/sp |
| 31 | 289 | Observation | `Observation.valueCodeableConcept.coding` | 385658003 | Done | http://snomed.info/sct |
| 32 | 290 | Observation | `Observation.valueCodeableConcept.coding` | 385651009 | In progress | http://snomed.info/sct |
| 33 | 300 | Observation | `Observation.code.coding` | SP000490 | Siklus Pemberian Makanan Tambahan | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://terminology.kemkes.go.id/sp | 17 |
| http://snomed.info/sct | 12 |
| http://loinc.org | 3 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 1 |
| **Total** | **33** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
