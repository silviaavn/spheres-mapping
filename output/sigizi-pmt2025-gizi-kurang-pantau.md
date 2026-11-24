# Output Form: SiGizi PMT 2025 Gizi Kurang - Pantau

Sumber: `mapping/phdt-data-dictionary-sigizi-pmt2025-gizi-kurang-pantau.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-sigizi-pmt2025-gizi-kurang-pantau.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 42 |
| Code (`jumlah code` = 1) | 101 |
| Code unik (code + CodeSystem) | 26 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 29 |
| Variabel BQ (unik) | 51 |
| Variabel raw (variabel dictionary; belum ada file mentah) | 51 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 3–25 | Patient | – | – | `nama` → `Patient.name.text` (3)<br>`nik` → `Patient.identifier.value` (6)<br>`jk` → `Patient.gender` (8)<br>`tgl_lahir` → `Patient.birthDate` (10)<br>`prov` → `Patient.address.extension.extension.valueCode` (16)<br>`kabkota` → `Patient.address.extension.extension.valueCode` (19)<br>`kec` → `Patient.address.extension.extension.valueCode` (22)<br>`desakel` → `Patient.address.extension.extension.valueCode` (25) |
| 2 | 111–126 | Encounter | – | – | `tanggal_pengukuran_awal` → `Encounter.period.start` (120)<br>`posyandu` → `Encounter.location.reference` (122) 🔎 lookup master data<br>`pukesmas` → `Encounter.serviceProvider.reference` (126) 🔎 lookup master data<br>`tindakan` → `Encounter.extension.valueString` (146) |
| 3 | 127–133 | Condition | 385984007 | Growth and development treatments and procedures | – |
| 4 | 147–159 | Observation | SP000041 | Sumber Anggaran PMT | `sumber_anggaran` → `Observation.valueCodeableConcept.coding` (150) |
| 5 | 160–176 | Observation | SP000491 | Mitra Pemberi MT | `mitra` → `Observation.valueCodeableConcept.coding` (163) |
| 6 | 177–189 | Observation | 29463-7 | Body weight | `bb_awal` → `Observation.valueQuantity.value` (181) |
| 7 | 190–203 | Observation | 8308-9 | Body height --standing | `tb_awal` → `Observation.valueQuantity.value` (195) |
| 8 | 204–217 | Observation | 1153600001 | Weight for height z-score | `zs_bbtb_awal` → `Observation.valueQuantity.value` (209) |
| 9 | 218–230 | Observation | 29463-7 | Body weight | `bb_minggu_1` → `Observation.valueQuantity.value` (222) |
| 10 | 231–244 | Observation | 8308-9 | Body height --standing | `tb_minggu_1` → `Observation.valueQuantity.value` (236) |
| 11 | 245–258 | Observation | 1153600001 | Weight for height z-score | `zs_bbtb_minggu_1` → `Observation.valueQuantity.value` (250) |
| 12 | 259–273 | Observation | 365910001 | Weight trend finding | `status_kenaikan_minggu_1` → `Observation.valueCodeableConcept.coding` (263) |
| 13 | 274–286 | Observation | 29463-7 | Body weight | `bb_minggu_2` → `Observation.valueQuantity.value` (278) |
| 14 | 287–300 | Observation | 8308-9 | Body height --standing | `tb_minggu_2` → `Observation.valueQuantity.value` (292) |
| 15 | 301–314 | Observation | 1153600001 | Weight for height z-score | `zs_bbtb_minggu_2` → `Observation.valueQuantity.value` (306) |
| 16 | 315–329 | Observation | 365910001 | Weight trend finding | `status_kenaikan_minggu_2` → `Observation.valueCodeableConcept.coding` (319) |
| 17 | 330–342 | Observation | 29463-7 | Body weight | `bb_minggu_3` → `Observation.valueQuantity.value` (334) |
| 18 | 343–356 | Observation | 8308-9 | Body height --standing | `tb_minggu_3` → `Observation.valueQuantity.value` (348) |
| 19 | 357–370 | Observation | 1153600001 | Weight for height z-score | `zs_bbtb_minggu_3` → `Observation.valueQuantity.value` (362) |
| 20 | 371–385 | Observation | 365910001 | Weight trend finding | `status_kenaikan_minggu_3` → `Observation.valueCodeableConcept.coding` (375) |
| 21 | 386–398 | Observation | 29463-7 | Body weight | `bb_minggu_4` → `Observation.valueQuantity.value` (390) |
| 22 | 399–412 | Observation | 8308-9 | Body height --standing | `tb_minggu_4` → `Observation.valueQuantity.value` (404) |
| 23 | 413–426 | Observation | 1153600001 | Weight for height z-score | `zs_bbtb_minggu_4` → `Observation.valueQuantity.value` (418) |
| 24 | 427–441 | Observation | 365910001 | Weight trend finding | `status_kenaikan_minggu_4` → `Observation.valueCodeableConcept.coding` (431) |
| 25 | 442–454 | Observation | 29463-7 | Body weight | `bb_minggu_5` → `Observation.valueQuantity.value` (446) |
| 26 | 455–468 | Observation | 8308-9 | Body height --standing | `tb_minggu_5` → `Observation.valueQuantity.value` (460) |
| 27 | 469–482 | Observation | 1153600001 | Weight for height z-score | `zs_bbtb_minggu_5` → `Observation.valueQuantity.value` (474) |
| 28 | 483–497 | Observation | 365910001 | Weight trend finding | `status_kenaikan_minggu_5` → `Observation.valueCodeableConcept.coding` (487) |
| 29 | 498–510 | Observation | 29463-7 | Body weight | `bb_minggu_6` → `Observation.valueQuantity.value` (502) |
| 30 | 511–524 | Observation | 8308-9 | Body height --standing | `tb_minggu_6` → `Observation.valueQuantity.value` (516) |
| 31 | 525–538 | Observation | 1153600001 | Weight for height z-score | `zs_bbtb_minggu_6` → `Observation.valueQuantity.value` (530) |
| 32 | 539–553 | Observation | 365910001 | Weight trend finding | `status_kenaikan_minggu_6` → `Observation.valueCodeableConcept.coding` (543) |
| 33 | 554–566 | Observation | 29463-7 | Body weight | `bb_minggu_7` → `Observation.valueQuantity.value` (558) |
| 34 | 567–580 | Observation | 8308-9 | Body height --standing | `tb_minggu_7` → `Observation.valueQuantity.value` (572) |
| 35 | 581–594 | Observation | 1153600001 | Weight for height z-score | `zs_bbtb_minggu_7` → `Observation.valueQuantity.value` (586) |
| 36 | 595–609 | Observation | 365910001 | Weight trend finding | `status_kenaikan_minggu_7` → `Observation.valueCodeableConcept.coding` (599) |
| 37 | 610–622 | Observation | 29463-7 | Body weight | `bb_minggu_8` → `Observation.valueQuantity.value` (614) |
| 38 | 623–636 | Observation | 8308-9 | Body height --standing | `tb_minggu_8` → `Observation.valueQuantity.value` (628) |
| 39 | 637–650 | Observation | 1153600001 | Weight for height z-score | `zs_bbtb_minggu_8` → `Observation.valueQuantity.value` (642) |
| 40 | 651–665 | Observation | 365910001 | Weight trend finding | `status_kenaikan_minggu_8` → `Observation.valueCodeableConcept.coding` (655) |
| 41 | 666–677 | Observation | SP000489 | Status Pemantauan Pemberian Makanan Tambahan | `status_pmt` → `Observation.valueCodeableConcept.coding` (669) |
| 42 | 678–688 | Observation | SP000490 | Siklus Pemberian Makanan Tambahan | `siklus_pmt` → `Observation.valueInteger` (681) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 39 |
| Patient | 1 |
| Encounter | 1 |
| Condition | 1 |
| **Total** | **42** |

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
| 13 | 180 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 14 | 193 | Observation | `Observation.code.coding` | 8308-9 | Body height --standing | http://loinc.org |
| 15 | 194 | Observation | `Observation.code.coding` | 8306-3 | Body height --lying | http://loinc.org |
| 16 | 207 | Observation | `Observation.code.coding` | 1153600001 | Weight for height z-score | http://snomed.info/sct |
| 17 | 208 | Observation | `Observation.code.coding` | 1153598007 | Weight for length z score | http://snomed.info/sct |
| 18 | 221 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 19 | 234 | Observation | `Observation.code.coding` | 8308-9 | Body height --standing | http://loinc.org |
| 20 | 235 | Observation | `Observation.code.coding` | 8306-3 | Body height --lying | http://loinc.org |
| 21 | 248 | Observation | `Observation.code.coding` | 1153600001 | Weight for height z-score | http://snomed.info/sct |
| 22 | 249 | Observation | `Observation.code.coding` | 1153598007 | Weight for length z score | http://snomed.info/sct |
| 23 | 262 | Observation | `Observation.code.coding` | 365910001 | Weight trend finding | http://snomed.info/sct |
| 24 | 263 | Observation | `Observation.valueCodeableConcept.coding` | SP000018 | Baru Pertama Kali Ditimbang | http://terminology.kemkes.go.id/sp |
| 25 | 264 | Observation | `Observation.valueCodeableConcept.coding` | 8943002 | Weight gain | http://snomed.info/sct |
| 26 | 265 | Observation | `Observation.valueCodeableConcept.coding` | SP000019 | Tidak Ditimbang Bulan Lalu | http://terminology.kemkes.go.id/sp |
| 27 | 266 | Observation | `Observation.valueCodeableConcept.coding` | 36440009 | Failure to gain weight | http://snomed.info/sct |
| 28 | 277 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 29 | 290 | Observation | `Observation.code.coding` | 8308-9 | Body height --standing | http://loinc.org |
| 30 | 291 | Observation | `Observation.code.coding` | 8306-3 | Body height --lying | http://loinc.org |
| 31 | 304 | Observation | `Observation.code.coding` | 1153600001 | Weight for height z-score | http://snomed.info/sct |
| 32 | 305 | Observation | `Observation.code.coding` | 1153598007 | Weight for length z score | http://snomed.info/sct |
| 33 | 318 | Observation | `Observation.code.coding` | 365910001 | Weight trend finding | http://snomed.info/sct |
| 34 | 319 | Observation | `Observation.valueCodeableConcept.coding` | SP000018 | Baru Pertama Kali Ditimbang | http://terminology.kemkes.go.id/sp |
| 35 | 320 | Observation | `Observation.valueCodeableConcept.coding` | 8943002 | Weight gain | http://snomed.info/sct |
| 36 | 321 | Observation | `Observation.valueCodeableConcept.coding` | SP000019 | Tidak Ditimbang Bulan Lalu | http://terminology.kemkes.go.id/sp |
| 37 | 322 | Observation | `Observation.valueCodeableConcept.coding` | 36440009 | Failure to gain weight | http://snomed.info/sct |
| 38 | 333 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 39 | 346 | Observation | `Observation.code.coding` | 8308-9 | Body height --standing | http://loinc.org |
| 40 | 347 | Observation | `Observation.code.coding` | 8306-3 | Body height --lying | http://loinc.org |
| 41 | 360 | Observation | `Observation.code.coding` | 1153600001 | Weight for height z-score | http://snomed.info/sct |
| 42 | 361 | Observation | `Observation.code.coding` | 1153598007 | Weight for length z score | http://snomed.info/sct |
| 43 | 374 | Observation | `Observation.code.coding` | 365910001 | Weight trend finding | http://snomed.info/sct |
| 44 | 375 | Observation | `Observation.valueCodeableConcept.coding` | SP000018 | Baru Pertama Kali Ditimbang | http://terminology.kemkes.go.id/sp |
| 45 | 376 | Observation | `Observation.valueCodeableConcept.coding` | 8943002 | Weight gain | http://snomed.info/sct |
| 46 | 377 | Observation | `Observation.valueCodeableConcept.coding` | SP000019 | Tidak Ditimbang Bulan Lalu | http://terminology.kemkes.go.id/sp |
| 47 | 378 | Observation | `Observation.valueCodeableConcept.coding` | 36440009 | Failure to gain weight | http://snomed.info/sct |
| 48 | 389 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 49 | 402 | Observation | `Observation.code.coding` | 8308-9 | Body height --standing | http://loinc.org |
| 50 | 403 | Observation | `Observation.code.coding` | 8306-3 | Body height --lying | http://loinc.org |
| 51 | 416 | Observation | `Observation.code.coding` | 1153600001 | Weight for height z-score | http://snomed.info/sct |
| 52 | 417 | Observation | `Observation.code.coding` | 1153598007 | Weight for length z score | http://snomed.info/sct |
| 53 | 430 | Observation | `Observation.code.coding` | 365910001 | Weight trend finding | http://snomed.info/sct |
| 54 | 431 | Observation | `Observation.valueCodeableConcept.coding` | SP000018 | Baru Pertama Kali Ditimbang | http://terminology.kemkes.go.id/sp |
| 55 | 432 | Observation | `Observation.valueCodeableConcept.coding` | 8943002 | Weight gain | http://snomed.info/sct |
| 56 | 433 | Observation | `Observation.valueCodeableConcept.coding` | SP000019 | Tidak Ditimbang Bulan Lalu | http://terminology.kemkes.go.id/sp |
| 57 | 434 | Observation | `Observation.valueCodeableConcept.coding` | 36440009 | Failure to gain weight | http://snomed.info/sct |
| 58 | 445 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 59 | 458 | Observation | `Observation.code.coding` | 8308-9 | Body height --standing | http://loinc.org |
| 60 | 459 | Observation | `Observation.code.coding` | 8306-3 | Body height --lying | http://loinc.org |
| 61 | 472 | Observation | `Observation.code.coding` | 1153600001 | Weight for height z-score | http://snomed.info/sct |
| 62 | 473 | Observation | `Observation.code.coding` | 1153598007 | Weight for length z score | http://snomed.info/sct |
| 63 | 486 | Observation | `Observation.code.coding` | 365910001 | Weight trend finding | http://snomed.info/sct |
| 64 | 487 | Observation | `Observation.valueCodeableConcept.coding` | SP000018 | Baru Pertama Kali Ditimbang | http://terminology.kemkes.go.id/sp |
| 65 | 488 | Observation | `Observation.valueCodeableConcept.coding` | 8943002 | Weight gain | http://snomed.info/sct |
| 66 | 489 | Observation | `Observation.valueCodeableConcept.coding` | SP000019 | Tidak Ditimbang Bulan Lalu | http://terminology.kemkes.go.id/sp |
| 67 | 490 | Observation | `Observation.valueCodeableConcept.coding` | 36440009 | Failure to gain weight | http://snomed.info/sct |
| 68 | 501 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 69 | 514 | Observation | `Observation.code.coding` | 8308-9 | Body height --standing | http://loinc.org |
| 70 | 515 | Observation | `Observation.code.coding` | 8306-3 | Body height --lying | http://loinc.org |
| 71 | 528 | Observation | `Observation.code.coding` | 1153600001 | Weight for height z-score | http://snomed.info/sct |
| 72 | 529 | Observation | `Observation.code.coding` | 1153598007 | Weight for length z score | http://snomed.info/sct |
| 73 | 542 | Observation | `Observation.code.coding` | 365910001 | Weight trend finding | http://snomed.info/sct |
| 74 | 543 | Observation | `Observation.valueCodeableConcept.coding` | SP000018 | Baru Pertama Kali Ditimbang | http://terminology.kemkes.go.id/sp |
| 75 | 544 | Observation | `Observation.valueCodeableConcept.coding` | 8943002 | Weight gain | http://snomed.info/sct |
| 76 | 545 | Observation | `Observation.valueCodeableConcept.coding` | SP000019 | Tidak Ditimbang Bulan Lalu | http://terminology.kemkes.go.id/sp |
| 77 | 546 | Observation | `Observation.valueCodeableConcept.coding` | 36440009 | Failure to gain weight | http://snomed.info/sct |
| 78 | 557 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 79 | 570 | Observation | `Observation.code.coding` | 8308-9 | Body height --standing | http://loinc.org |
| 80 | 571 | Observation | `Observation.code.coding` | 8306-3 | Body height --lying | http://loinc.org |
| 81 | 584 | Observation | `Observation.code.coding` | 1153600001 | Weight for height z-score | http://snomed.info/sct |
| 82 | 585 | Observation | `Observation.code.coding` | 1153598007 | Weight for length z score | http://snomed.info/sct |
| 83 | 598 | Observation | `Observation.code.coding` | 365910001 | Weight trend finding | http://snomed.info/sct |
| 84 | 599 | Observation | `Observation.valueCodeableConcept.coding` | SP000018 | Baru Pertama Kali Ditimbang | http://terminology.kemkes.go.id/sp |
| 85 | 600 | Observation | `Observation.valueCodeableConcept.coding` | 8943002 | Weight gain | http://snomed.info/sct |
| 86 | 601 | Observation | `Observation.valueCodeableConcept.coding` | SP000019 | Tidak Ditimbang Bulan Lalu | http://terminology.kemkes.go.id/sp |
| 87 | 602 | Observation | `Observation.valueCodeableConcept.coding` | 36440009 | Failure to gain weight | http://snomed.info/sct |
| 88 | 613 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 89 | 626 | Observation | `Observation.code.coding` | 8308-9 | Body height --standing | http://loinc.org |
| 90 | 627 | Observation | `Observation.code.coding` | 8306-3 | Body height --lying | http://loinc.org |
| 91 | 640 | Observation | `Observation.code.coding` | 1153600001 | Weight for height z-score | http://snomed.info/sct |
| 92 | 641 | Observation | `Observation.code.coding` | 1153598007 | Weight for length z score | http://snomed.info/sct |
| 93 | 654 | Observation | `Observation.code.coding` | 365910001 | Weight trend finding | http://snomed.info/sct |
| 94 | 655 | Observation | `Observation.valueCodeableConcept.coding` | SP000018 | Baru Pertama Kali Ditimbang | http://terminology.kemkes.go.id/sp |
| 95 | 656 | Observation | `Observation.valueCodeableConcept.coding` | 8943002 | Weight gain | http://snomed.info/sct |
| 96 | 657 | Observation | `Observation.valueCodeableConcept.coding` | SP000019 | Tidak Ditimbang Bulan Lalu | http://terminology.kemkes.go.id/sp |
| 97 | 658 | Observation | `Observation.valueCodeableConcept.coding` | 36440009 | Failure to gain weight | http://snomed.info/sct |
| 98 | 668 | Observation | `Observation.code.coding` | SP000489 | Status Pemantauan Pemberian Makanan Tambahan | http://terminology.kemkes.go.id/sp |
| 99 | 669 | Observation | `Observation.valueCodeableConcept.coding` | 385658003 | Done | http://snomed.info/sct |
| 100 | 670 | Observation | `Observation.valueCodeableConcept.coding` | 385651009 | In progress | http://snomed.info/sct |
| 101 | 680 | Observation | `Observation.code.coding` | SP000490 | Siklus Pemberian Makanan Tambahan | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 45 |
| http://terminology.kemkes.go.id/sp | 29 |
| http://loinc.org | 27 |
| **Total** | **101** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
