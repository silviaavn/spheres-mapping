# Output Form: SiGizi Balita Mendapat PMT 2024

Sumber: `mapping/phdt-data-dictionary-sigizi-balita-mendapat-pmt-2024.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-sigizi-balita-mendapat-pmt-2024.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 15 |
| Code (`jumlah code` = 1) | 45 |
| Code unik (code + CodeSystem) | 41 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 14 |
| Variabel BQ (unik) | 30 |
| Variabel raw (variabel dictionary; belum ada file mentah) | 30 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 3–32 | Patient | – | – | `nama` → `Patient.name.text` (3)<br>`nik` → `Patient.identifier.value` (6)<br>`jk` → `Patient.gender` (8)<br>`tgl_lahir` → `Patient.birthDate` (10)<br>_Alamat Domisili_ → `Patient.address.use` (11, tanpa BQ)<br>`alamat` → `Patient.address.line` (12)<br>`kabkota` → `Patient.address.city` (13)<br>_Nama Provinsi_ → `Patient.address.extension.url` (15, tanpa BQ)<br>`prov` → `Patient.address.extension.extension.valueCode` (17)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (20, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.url` (21, tanpa BQ)<br>`kec` → `Patient.address.extension.extension.valueCode` (23)<br>_Nama Desa_ → `Patient.address.extension.url` (24, tanpa BQ)<br>`desakel` → `Patient.address.extension.extension.valueCode` (26)<br>`rw` → `Patient.address.extension.extension.valueCode` (29)<br>`rt` → `Patient.address.extension.extension.valueCode` (32) |
| 2 | 118–133 | Encounter | – | – | `tanggal_pemberian` → `Encounter.period.start` (127)<br>`posyandu` → `Encounter.location.location.reference` (129) 🔎 lookup master data<br>`puskesmas` → `Encounter.serviceProvider.reference` (133) 🔎 lookup master data<br>`detail` → `Encounter.extension.valueString` (153) |
| 3 | 134–140 | Condition | 385984007 | Growth and development treatments and procedures | – |
| 4 | 154–165 | Observation | 29463-7 | Body weight | `berat_badan_kg_awal` → `Observation.valueQuantity.value` (157)<br>`tanggal_pengukuran_awal` → `Observation.effectiveDateTime` (162) |
| 5 | 166–178 | Observation | 8308-9 | Body height --standing | `tinggi_badan_cm_awal` → `Observation.valueQuantity.value` (170) |
| 6 | 179–193 | Observation | 365910001 | Weight trend finding | `status_pertumbuhan` → `Observation.valueCodeableConcept.coding` (182) |
| 7 | 194–210 | Observation | 1153593003 | Weight for age z-score | `bbu_awal` → `Observation.status` (194)<br>`zs_bbu_awal` → `Observation.valueQuantity.value` (197) |
| 8 | 211–228 | Observation | 1153604005 | Body height for age z-score | `tbu_awal` → `Observation.status` (211)<br>_ZS TB/U Awal_ → `Observation.valueQuantity.value` (215, tanpa BQ) |
| 9 | 229–248 | Observation | 1153600001 | Weight for height z-score | `bbtb_awal` → `Observation.status` (229)<br>`zs_bbtb_awal` → `Observation.valueQuantity.value` (233) |
| 10 | 249–260 | Observation | SP000036 | Jenis PMT | `jenis_pmt` → `Observation.valueCodeableConcept.coding` (252) |
| 11 | 261–271 | Observation | SP000037 | Pemberian MT ke- | `pemberian_ke` → `Observation.valueInteger` (264) |
| 12 | 272–282 | Observation | SP000038 | Tahun Produksi MT | _Tahun Produksi PMT_ → `Observation.status` (272, tanpa BQ)<br>`tahun_produksi` → `Observation.valueDateTime` (275) |
| 13 | 283–293 | Observation | SP000039 | Jumlah Pemberian MT | `jumlah_pemberian` → `Observation.valueInteger` (286) |
| 14 | 294–305 | Observation | SP000040 | Alasan Pemberian MT | `alasan_pemberian` → `Observation.valueCodeableConcept.coding` (297) |
| 15 | 306–318 | Observation | SP000041 | Sumber Anggaran PMT | `sumber_anggaran` → `Observation.valueCodeableConcept.coding` (309) |

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
| 1 | 136 | Condition | `Condition.code.coding` | 385984007 | Growth and development treatments and procedures | http://snomed.info/sct |
| 2 | 156 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 3 | 168 | Observation | `Observation.code.coding` | 8308-9 | Body height --standing | http://loinc.org |
| 4 | 169 | Observation | `Observation.code.coding` | 8306-3 | Body height --lying | http://loinc.org |
| 5 | 181 | Observation | `Observation.code.coding` | 365910001 | Weight trend finding | http://snomed.info/sct |
| 6 | 182 | Observation | `Observation.valueCodeableConcept.coding` | SP000018 | Baru Pertama Kali Ditimbang | http://terminology.kemkes.go.id/sp |
| 7 | 183 | Observation | `Observation.valueCodeableConcept.coding` | 8943002 | Weight gain | http://snomed.info/sct |
| 8 | 184 | Observation | `Observation.valueCodeableConcept.coding` | SP000019 | Tidak Ditimbang Bulan Lalu | http://terminology.kemkes.go.id/sp |
| 9 | 185 | Observation | `Observation.valueCodeableConcept.coding` | 36440009 | Failure to gain weight | http://snomed.info/sct |
| 10 | 186 | Observation | `Observation.dataAbsentReason` | unknown | Unknown | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 11 | 196 | Observation | `Observation.code.coding` | 1153593003 | Weight for age z-score | http://snomed.info/sct |
| 12 | 199 | Observation | `Observation.interpretation.coding` | 248342006 | Underweight | http://snomed.info/sct |
| 13 | 200 | Observation | `Observation.interpretation.coding` | 43664005 | Normal weight | http://snomed.info/sct |
| 14 | 201 | Observation | `Observation.interpretation.coding` | SP000017 | Outlier | http://terminology.kemkes.go.id/sp |
| 15 | 202 | Observation | `Observation.interpretation.coding` | OI000010 | Risiko Berat Badan Lebih | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 16 | 203 | Observation | `Observation.interpretation.coding` | OI000007 | Berat Badan Sangat Kurang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 17 | 213 | Observation | `Observation.code.coding` | 1153604005 | Body height for age z-score | http://snomed.info/sct |
| 18 | 214 | Observation | `Observation.code.coding` | 1153590000 | Length for age z score | http://snomed.info/sct |
| 19 | 217 | Observation | `Observation.interpretation.coding` | 17489000 | Body height normal for age | http://snomed.info/sct |
| 20 | 218 | Observation | `Observation.interpretation.coding` | SP000017 | Outlier | http://terminology.kemkes.go.id/sp |
| 21 | 219 | Observation | `Observation.interpretation.coding` | 444000005 | Short stature for age | http://snomed.info/sct |
| 22 | 220 | Observation | `Observation.interpretation.coding` | OI000011 | Sangat Pendek | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 23 | 221 | Observation | `Observation.interpretation.coding` | 83077003 | Tall for age | http://snomed.info/sct |
| 24 | 231 | Observation | `Observation.code.coding` | 1153600001 | Weight for height z-score | http://snomed.info/sct |
| 25 | 232 | Observation | `Observation.code.coding` | 1153598007 | Weight for length z score | http://snomed.info/sct |
| 26 | 235 | Observation | `Observation.interpretation.coding` | 248324001 | Well nourished | http://snomed.info/sct |
| 27 | 236 | Observation | `Observation.interpretation.coding` | OI000001 | Gizi Buruk | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 28 | 237 | Observation | `Observation.interpretation.coding` | 248325000 | Undernourished | http://snomed.info/sct |
| 29 | 238 | Observation | `Observation.interpretation.coding` | 238131007 | Overweight | http://snomed.info/sct |
| 30 | 239 | Observation | `Observation.interpretation.coding` | 414915002 | Obese | http://snomed.info/sct |
| 31 | 240 | Observation | `Observation.interpretation.coding` | SP000017 | Outlier | http://terminology.kemkes.go.id/sp |
| 32 | 241 | Observation | `Observation.interpretation.coding` | OI000004 | Risiko Gizi Lebih | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 33 | 251 | Observation | `Observation.code.coding` | SP000036 | Jenis PMT | http://terminology.kemkes.go.id/sp |
| 34 | 252 | Observation | `Observation.valueCodeableConcept.coding` | FO000001 | MT Lokal | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 35 | 253 | Observation | `Observation.valueCodeableConcept.coding` | FO000002 | MT Pabrikan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 36 | 263 | Observation | `Observation.code.coding` | SP000037 | Pemberian MT ke- | http://terminology.kemkes.go.id/sp |
| 37 | 274 | Observation | `Observation.code.coding` | SP000038 | Tahun Produksi MT | http://terminology.kemkes.go.id/sp |
| 38 | 285 | Observation | `Observation.code.coding` | SP000039 | Jumlah Pemberian MT | http://terminology.kemkes.go.id/sp |
| 39 | 296 | Observation | `Observation.code.coding` | SP000040 | Alasan Pemberian MT | http://terminology.kemkes.go.id/sp |
| 40 | 297 | Observation | `Observation.valueCodeableConcept.coding` | 248342006 | Underweight | http://snomed.info/sct |
| 41 | 298 | Observation | `Observation.valueCodeableConcept.coding` | 36440009 | Failure to gain weight | http://snomed.info/sct |
| 42 | 308 | Observation | `Observation.code.coding` | SP000041 | Sumber Anggaran PMT | http://terminology.kemkes.go.id/sp |
| 43 | 309 | Observation | `Observation.valueCodeableConcept.coding` | SP000042 | APBD | http://terminology.kemkes.go.id/sp |
| 44 | 310 | Observation | `Observation.valueCodeableConcept.coding` | SP000159 | Mitra | http://terminology.kemkes.go.id/sp |
| 45 | 311 | Observation | `Observation.valueCodeableConcept.coding` | SP000158 | DAK (Dana Alokasi Khusus) | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 20 |
| http://terminology.kemkes.go.id/sp | 14 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 7 |
| http://loinc.org | 3 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 1 |
| **Total** | **45** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
