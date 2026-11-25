# Output Form: SiGizi Balita Pemantauan PMT 2024

Sumber: `mapping/phdt-data-dictionary-sigizi-balita-pemantauan-pmt-2024.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-sigizi-balita-pemantauan-pmt-2024.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 9 |
| Code (`jumlah code` = 1) | 15 |
| Code unik (code + CodeSystem) | 14 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 5 |
| Variabel BQ (unik) | 18 |
| Variabel raw (variabel dictionary; belum ada file mentah) | 18 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 3–32 | Patient | – | – | `nama` → `Patient.name.text` (3)<br>`nik` → `Patient.identifier.value` (6)<br>`jk` → `Patient.gender` (8)<br>`tgl_lahir` → `Patient.birthDate` (10)<br>_Alamat Domisili_ → `Patient.address.use` (11, tanpa BQ)<br>`kabkota` → `Patient.address.city` (13)<br>_Nama Provinsi_ → `Patient.address.extension.url` (15, tanpa BQ)<br>`prov` → `Patient.address.extension.extension.valueCode` (17)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (20, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.url` (21, tanpa BQ)<br>`kec` → `Patient.address.extension.extension.valueCode` (23)<br>_Nama Desa_ → `Patient.address.extension.url` (24, tanpa BQ)<br>`desakel` → `Patient.address.extension.extension.valueCode` (26)<br>_RW_ → `Patient.address.extension.extension.valueCode` (29, tanpa BQ)<br>_RT_ → `Patient.address.extension.extension.valueCode` (32, tanpa BQ) |
| 2 | 118–133 | Encounter | – | – | `tanggal_pengukuran_awal` → `Encounter.period.start` (127)<br>`posyandu` → `Encounter.location.location.reference` (129) 🔎 lookup master data<br>`puskesmas` → `Encounter.serviceProvider.reference` (133) 🔎 lookup master data<br>`tindakan` → `Encounter.extension.valueString` (153) |
| 3 | 134–140 | Condition | 385984007 | Growth and development treatments and procedures | – |
| 4 | 154–167 | Observation | 29463-7 | Body weight | `berat_badan_kg_awal` → `Observation.valueQuantity.value` (158) |
| 5 | 168–182 | Observation | 8308-9 | Body height --standing | `tinggi_badan_cm_awal` → `Observation.valueQuantity.value` (173) |
| 6 | 183–197 | Observation | 365910001 | Weight trend finding | `status_pertumbuhan` → `Observation.valueCodeableConcept.coding` (186) |
| 7 | 198–208 | Observation | SP000043 | Pemantauan PMT ke- | `pemantauan_ke_jml_pemantauan_terupdateterakhir` → `Observation.valueInteger` (201) |
| 8 | 209–219 | Observation | SP000044 | Tanggal Pemantauan PMT Awal | `tanggal_pemantauan_awal` → `Observation.valueDateTime` (212) |
| 9 | 220–230 | Observation | SP000045 | Tanggal Pemantauan PMT Akhir | `tanggal_pemantauan_akhir` → `Observation.valueDateTime` (223) |

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
| 2 | 157 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 3 | 160 | Observation | `Observation.dataAbsentReason` | not-a-number | Not a Number (NaN) | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 4 | 171 | Observation | `Observation.code.coding` | 8308-9 | Body height --standing | http://loinc.org |
| 5 | 172 | Observation | `Observation.code.coding` | 8306-3 | Body height --lying | http://loinc.org |
| 6 | 175 | Observation | `Observation.dataAbsentReason` | not-a-number | Not a Number (NaN) | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 7 | 185 | Observation | `Observation.code.coding` | 365910001 | Weight trend finding | http://snomed.info/sct |
| 8 | 186 | Observation | `Observation.valueCodeableConcept.coding` | SP000018 | Baru Pertama Kali Ditimbang | http://terminology.kemkes.go.id/sp |
| 9 | 187 | Observation | `Observation.valueCodeableConcept.coding` | 8943002 | Weight gain | http://snomed.info/sct |
| 10 | 188 | Observation | `Observation.valueCodeableConcept.coding` | SP000019 | Tidak Ditimbang Bulan Lalu | http://terminology.kemkes.go.id/sp |
| 11 | 189 | Observation | `Observation.valueCodeableConcept.coding` | 36440009 | Failure to gain weight | http://snomed.info/sct |
| 12 | 190 | Observation | `Observation.dataAbsentReason` | unknown | Unknown | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 13 | 200 | Observation | `Observation.code.coding` | SP000043 | Pemantauan PMT ke- | http://terminology.kemkes.go.id/sp |
| 14 | 211 | Observation | `Observation.code.coding` | SP000044 | Tanggal Pemantauan PMT Awal | http://terminology.kemkes.go.id/sp |
| 15 | 222 | Observation | `Observation.code.coding` | SP000045 | Tanggal Pemantauan PMT Akhir | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://terminology.kemkes.go.id/sp | 5 |
| http://snomed.info/sct | 4 |
| http://loinc.org | 3 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 3 |
| **Total** | **15** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
