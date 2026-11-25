# Output Form: SiGizi Balita ASI Eksklusif

Sumber: `mapping/phdt-data-dictionary-sigizi-balita-asi-eksklusif.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-sigizi-balita-asi-eksklusif.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 11 |
| Code (`jumlah code` = 1) | 36 |
| Code unik (code + CodeSystem) | 12 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 28 |
| Variabel BQ (unik) | 22 |
| Variabel raw (variabel dictionary; belum ada file mentah) | 22 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 3–32 | Patient | – | – | `nama` → `Patient.name.text` (3)<br>`nik` → `Patient.identifier.value` (6)<br>`jk` → `Patient.gender` (8)<br>`tgl_lahir` → `Patient.birthDate` (10)<br>_Alamat Domisili_ → `Patient.address.use` (11, tanpa BQ)<br>`alamat` → `Patient.address.line` (12)<br>`kabkota` → `Patient.address.city` (13)<br>_Nama Provinsi_ → `Patient.address.extension.url` (15, tanpa BQ)<br>`prov` → `Patient.address.extension.extension.valueCode` (17)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (20, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.url` (21, tanpa BQ)<br>`kec` → `Patient.address.extension.extension.valueCode` (23)<br>_Nama Desa_ → `Patient.address.extension.url` (24, tanpa BQ)<br>`desakel` → `Patient.address.extension.extension.valueCode` (26)<br>`rw` → `Patient.address.extension.extension.valueCode` (29)<br>`rt` → `Patient.address.extension.extension.valueCode` (32) |
| 2 | 118–121 | RelatedPerson | – | – | `nama_ortu` → `RelatedPerson.patient` (118) |
| 3 | 122–137 | Encounter | – | – | _Tanggal Pengukuran_ → `Encounter.period.start` (131, tanpa BQ)<br>`posyandu` → `Encounter.location.location.reference` (133) 🔎 lookup master data<br>`pukesmas` → `Encounter.serviceProvider.reference` (137) 🔎 lookup master data<br>`detail` → `Encounter.extension.valueString` (160) |
| 4 | 138–144 | Condition | 385984007 | Growth and development treatments and procedures | – |
| 5 | 161–174 | Observation | SP000024 | Monitoring ASI Eksklusif Bulan 0 | `bulan_0` → `Observation.valueCodeableConcept.coding` (164) |
| 6 | 175–188 | Observation | SP000025 | Monitoring ASI Eksklusif Bulan 1 | `bulan_1` → `Observation.valueCodeableConcept.coding` (178) |
| 7 | 189–202 | Observation | SP000026 | Monitoring ASI Eksklusif Bulan 2 | `bulan_2` → `Observation.valueCodeableConcept.coding` (192) |
| 8 | 203–216 | Observation | SP000027 | Monitoring ASI Eksklusif Bulan 3 | `bulan_3` → `Observation.valueCodeableConcept.coding` (206) |
| 9 | 217–230 | Observation | SP000028 | Monitoring ASI Eksklusif Bulan 4 | `bulan_4` → `Observation.valueCodeableConcept.coding` (220) |
| 10 | 231–244 | Observation | SP000032 | Monitoring ASI Eksklusif Bulan 5 | `bulan_5` → `Observation.valueCodeableConcept.coding` (234) |
| 11 | 245–258 | Observation | SP000033 | Monitoring ASI Eksklusif Bulan 6 | `bulan_6` → `Observation.valueCodeableConcept.coding` (248) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 7 |
| Patient | 1 |
| RelatedPerson | 1 |
| Encounter | 1 |
| Condition | 1 |
| **Total** | **11** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 140 | Condition | `Condition.code.coding` | 385984007 | Growth and development treatments and procedures | http://snomed.info/sct |
| 2 | 163 | Observation | `Observation.code.coding` | SP000024 | Monitoring ASI Eksklusif Bulan 0 | http://terminology.kemkes.go.id/sp |
| 3 | 164 | Observation | `Observation.valueCodeableConcept.coding` | 1145307003 | Exclusively breastfed | http://snomed.info/sct |
| 4 | 165 | Observation | `Observation.valueCodeableConcept.coding` | SP000029 | Tidak ASI Eksklusif | http://terminology.kemkes.go.id/sp |
| 5 | 166 | Observation | `Observation.valueCodeableConcept.coding` | SP000030 | Belum Diukur | http://terminology.kemkes.go.id/sp |
| 6 | 167 | Observation | `Observation.valueCodeableConcept.coding` | SP000031 | Tidak Direcall | http://terminology.kemkes.go.id/sp |
| 7 | 177 | Observation | `Observation.code.coding` | SP000025 | Monitoring ASI Eksklusif Bulan 1 | http://terminology.kemkes.go.id/sp |
| 8 | 178 | Observation | `Observation.valueCodeableConcept.coding` | 1145307003 | Exclusively breastfed | http://snomed.info/sct |
| 9 | 179 | Observation | `Observation.valueCodeableConcept.coding` | SP000029 | Tidak ASI Eksklusif | http://terminology.kemkes.go.id/sp |
| 10 | 180 | Observation | `Observation.valueCodeableConcept.coding` | SP000030 | Belum Diukur | http://terminology.kemkes.go.id/sp |
| 11 | 181 | Observation | `Observation.valueCodeableConcept.coding` | SP000031 | Tidak Direcall | http://terminology.kemkes.go.id/sp |
| 12 | 191 | Observation | `Observation.code.coding` | SP000026 | Monitoring ASI Eksklusif Bulan 2 | http://terminology.kemkes.go.id/sp |
| 13 | 192 | Observation | `Observation.valueCodeableConcept.coding` | 1145307003 | Exclusively breastfed | http://snomed.info/sct |
| 14 | 193 | Observation | `Observation.valueCodeableConcept.coding` | SP000029 | Tidak ASI Eksklusif | http://terminology.kemkes.go.id/sp |
| 15 | 194 | Observation | `Observation.valueCodeableConcept.coding` | SP000030 | Belum Diukur | http://terminology.kemkes.go.id/sp |
| 16 | 195 | Observation | `Observation.valueCodeableConcept.coding` | SP000031 | Tidak Direcall | http://terminology.kemkes.go.id/sp |
| 17 | 205 | Observation | `Observation.code.coding` | SP000027 | Monitoring ASI Eksklusif Bulan 3 | http://terminology.kemkes.go.id/sp |
| 18 | 206 | Observation | `Observation.valueCodeableConcept.coding` | 1145307003 | Exclusively breastfed | http://snomed.info/sct |
| 19 | 207 | Observation | `Observation.valueCodeableConcept.coding` | SP000029 | Tidak ASI Eksklusif | http://terminology.kemkes.go.id/sp |
| 20 | 208 | Observation | `Observation.valueCodeableConcept.coding` | SP000030 | Belum Diukur | http://terminology.kemkes.go.id/sp |
| 21 | 209 | Observation | `Observation.valueCodeableConcept.coding` | SP000031 | Tidak Direcall | http://terminology.kemkes.go.id/sp |
| 22 | 219 | Observation | `Observation.code.coding` | SP000028 | Monitoring ASI Eksklusif Bulan 4 | http://terminology.kemkes.go.id/sp |
| 23 | 220 | Observation | `Observation.valueCodeableConcept.coding` | 1145307003 | Exclusively breastfed | http://snomed.info/sct |
| 24 | 221 | Observation | `Observation.valueCodeableConcept.coding` | SP000029 | Tidak ASI Eksklusif | http://terminology.kemkes.go.id/sp |
| 25 | 222 | Observation | `Observation.valueCodeableConcept.coding` | SP000030 | Belum Diukur | http://terminology.kemkes.go.id/sp |
| 26 | 223 | Observation | `Observation.valueCodeableConcept.coding` | SP000031 | Tidak Direcall | http://terminology.kemkes.go.id/sp |
| 27 | 233 | Observation | `Observation.code.coding` | SP000032 | Monitoring ASI Eksklusif Bulan 5 | http://terminology.kemkes.go.id/sp |
| 28 | 234 | Observation | `Observation.valueCodeableConcept.coding` | 1145307003 | Exclusively breastfed | http://snomed.info/sct |
| 29 | 235 | Observation | `Observation.valueCodeableConcept.coding` | SP000029 | Tidak ASI Eksklusif | http://terminology.kemkes.go.id/sp |
| 30 | 236 | Observation | `Observation.valueCodeableConcept.coding` | SP000030 | Belum Diukur | http://terminology.kemkes.go.id/sp |
| 31 | 237 | Observation | `Observation.valueCodeableConcept.coding` | SP000031 | Tidak Direcall | http://terminology.kemkes.go.id/sp |
| 32 | 247 | Observation | `Observation.code.coding` | SP000033 | Monitoring ASI Eksklusif Bulan 6 | http://terminology.kemkes.go.id/sp |
| 33 | 248 | Observation | `Observation.valueCodeableConcept.coding` | 1145307003 | Exclusively breastfed | http://snomed.info/sct |
| 34 | 249 | Observation | `Observation.valueCodeableConcept.coding` | SP000029 | Tidak ASI Eksklusif | http://terminology.kemkes.go.id/sp |
| 35 | 250 | Observation | `Observation.valueCodeableConcept.coding` | SP000030 | Belum Diukur | http://terminology.kemkes.go.id/sp |
| 36 | 251 | Observation | `Observation.valueCodeableConcept.coding` | SP000031 | Tidak Direcall | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://terminology.kemkes.go.id/sp | 28 |
| http://snomed.info/sct | 8 |
| **Total** | **36** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
