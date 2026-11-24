# Output Form: SiGizi Balita MPASI

Sumber: `mapping/phdt-data-dictionary-sigizi-balita-mpasi.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-sigizi-balita-mpasi.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 9 |
| Code (`jumlah code` = 1) | 30 |
| Code unik (code + CodeSystem) | 30 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 2 |
| Variabel BQ (unik) | 27 |
| Variabel raw (variabel dictionary; belum ada file mentah) | 28 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 3–32 | Patient | – | – | `nama` → `Patient.name.text` (3)<br>`nik` → `Patient.identifier.value` (6)<br>`jk` → `Patient.gender` (8)<br>`tgl_lahir` → `Patient.birthDate` (10)<br>_Alamat Domisili_ → `Patient.address.use` (11, tanpa BQ)<br>`alamat` → `Patient.address.line` (12)<br>`kabkota` → `Patient.address.city` (13)<br>_Nama Provinsi_ → `Patient.address.extension.url` (15, tanpa BQ)<br>`prov` → `Patient.address.extension.extension.valueCode` (17)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (20, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.url` (21, tanpa BQ)<br>`kec` → `Patient.address.extension.extension.valueCode` (23)<br>_Nama Desa_ → `Patient.address.extension.url` (24, tanpa BQ)<br>`desakel` → `Patient.address.extension.extension.valueCode` (26)<br>`rw` → `Patient.address.extension.extension.valueCode` (29)<br>`rt` → `Patient.address.extension.extension.valueCode` (32) |
| 2 | 118–133 | Encounter | – | – | `tanggal_monitoring` → `Encounter.period.start` (127)<br>`posyandu` → `Encounter.location.reference` (129) 🔎 lookup master data<br>`puskesmas` → `Encounter.serviceProvider.reference` (133) 🔎 lookup master data<br>`detail` → `Encounter.extension.valueString` (156) |
| 3 | 134–140 | Condition | 385984007 | Growth and development treatments and procedures | – |
| 4 | 157–183 | Observation | 1153593003 | Weight for age z-score | `bbu` → `Observation.valueRange.low.value` (160) |
| 5 | 184–210 | Observation | 1153604005 | Body height for age z-score | `tbu` → `Observation.valueRange.low.value` (188) |
| 6 | 211–248 | Observation | 1153600001 | Weight for height z-score | `bbtb` → `Observation.valueRange.low.value` (215) |
| 7 | 249–260 | Observation | 63895-7 | Breastfeeding status | `asi` → `Observation.valueBoolean` (252) |
| 8 | 261–293 | Observation | SP000034 | Jenis MPASI | _Jenis MPASI_ → `Observation.valueBoolean` (264, tanpa BQ)<br>`sereal` → `Observation.component.code.coding` (266)<br>`kacangkacangan` → `Observation.component.code.coding` (269)<br>`susu_dan_produk_olahan` → `Observation.component.code.coding` (272)<br>`daging_ikan` → `Observation.component.code.coding` (275)<br>`telur` → `Observation.component.code.coding` (278)<br>`buah_dan_sayur_vit_a` → `Observation.component.code.coding` (281)<br>`buah_dan_sayur_sumber_lain` → `Observation.component.code.coding` (284) |
| 9 | 294–305 | Observation | SP000035 | Kualitas MPASI | _Kualitas MPASI_ → `Observation.status` (294, tanpa BQ)<br>`mpasi_baik` → `Observation.valueBoolean` (297) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 6 |
| Patient | 1 |
| Encounter | 1 |
| Condition | 1 |
| **Total** | **9** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 136 | Condition | `Condition.code.coding` | 385984007 | Growth and development treatments and procedures | http://snomed.info/sct |
| 2 | 159 | Observation | `Observation.code.coding` | 1153593003 | Weight for age z-score | http://snomed.info/sct |
| 3 | 164 | Observation | `Observation.interpretation.coding` | 248342006 | Underweight | http://snomed.info/sct |
| 4 | 169 | Observation | `Observation.interpretation.coding` | 43664005 | Normal weight | http://snomed.info/sct |
| 5 | 172 | Observation | `Observation.interpretation.coding` | OI000010 | Risiko Berat Badan Lebih | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 6 | 175 | Observation | `Observation.interpretation.coding` | OI000007 | Berat Badan Sangat Kurang |  |
| 7 | 186 | Observation | `Observation.code.coding` | 1153604005 | Body height for age z-score | http://snomed.info/sct |
| 8 | 187 | Observation | `Observation.code.coding` | 1153590000 | Length for age z score | http://snomed.info/sct |
| 9 | 192 | Observation | `Observation.interpretation.coding` | 17489000 | Body height normal for age | http://snomed.info/sct |
| 10 | 197 | Observation | `Observation.interpretation.coding` | 444000005 | Short stature for age | http://snomed.info/sct |
| 11 | 200 | Observation | `Observation.interpretation.coding` | OI000011 | Sangat Pendek | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 12 | 203 | Observation | `Observation.interpretation.coding` | 83077003 | Tall for age | http://snomed.info/sct |
| 13 | 213 | Observation | `Observation.code.coding` | 1153600001 | Weight for height z-score | http://snomed.info/sct |
| 14 | 214 | Observation | `Observation.code.coding` | 1153598007 | Weight for length z score | http://snomed.info/sct |
| 15 | 219 | Observation | `Observation.interpretation.coding` | 248324001 | Well nourished | http://snomed.info/sct |
| 16 | 222 | Observation | `Observation.interpretation.coding` | OI000001 | Gizi Buruk | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 17 | 227 | Observation | `Observation.interpretation.coding` | 248325000 | Undernourished | http://snomed.info/sct |
| 18 | 232 | Observation | `Observation.interpretation.coding` | 238131007 | Overweight | http://snomed.info/sct |
| 19 | 235 | Observation | `Observation.interpretation.coding` | 414915002 | Obese | http://snomed.info/sct |
| 20 | 240 | Observation | `Observation.interpretation.coding` | OI000004 | Risiko Gizi Lebih | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 21 | 251 | Observation | `Observation.code.coding` | 63895-7 | Breastfeeding status | http://loinc.org |
| 22 | 263 | Observation | `Observation.code.coding` | SP000034 | Jenis MPASI | http://terminology.kemkes.go.id/sp |
| 23 | 266 | Observation | `Observation.component.code.coding` | 23182003 | Cereal | http://snomed.info/sct |
| 24 | 269 | Observation | `Observation.component.code.coding` | 13577000 | Nut | http://snomed.info/sct |
| 25 | 272 | Observation | `Observation.component.code.coding` | QRI000007 | Susu dan produk olahannya | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 26 | 275 | Observation | `Observation.component.code.coding` | QRI000008 | Daging dan/atau ikan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 27 | 278 | Observation | `Observation.component.code.coding` | 102263004 | Eggs | http://snomed.info/sct |
| 28 | 281 | Observation | `Observation.component.code.coding` | QRI000010 | Buah dan sayur sumber vitamin A | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 29 | 284 | Observation | `Observation.component.code.coding` | QRI000011 | Buah dan sayur lainnya | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 30 | 296 | Observation | `Observation.code.coding` | SP000035 | Kualitas MPASI | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 18 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 8 |
| http://terminology.kemkes.go.id/sp | 2 |
|  | 1 |
| http://loinc.org | 1 |
| **Total** | **30** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
