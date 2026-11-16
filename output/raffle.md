# Output Form: Raffle

Sumber: `mapping/kobo-data-dictionary-raffle.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 8 |
| Code (`jumlah code` = 1) | 6 |
| Code unik (code + CodeSystem) | 6 |
| Variabel BQ (unik) | 12 |
| Variabel BQ di luar payload | 0 ✅ |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 8–20 | Patient | – | – | `nama_ibu` → `Patient.name.text` (8)<br>`nik_ibu` → `Patient.identifier.value` (12)<br>`nomor_telepon` → `Patient.telecom.value` (20) |
| 2 | 25–48 | Location | – | – | `lokasi_faskes` → `Location.identifier` (25)<br>_Provinsi_ → `Location.address.extension.extension.valueCode` (34, tanpa BQ)<br>_Kabupaten/Kota_ → `Location.address.extension.extension.valueCode` (37, tanpa BQ)<br>`kecamatan` → `Location.address.extension.extension.valueCode` (40)<br>`kelurahan` → `Location.address.extension.extension.valueCode` (43) |
| 3 | 51–51 | Practitioner | – | – | `nama_bidan_desa` → `Practitioner.name.text` (51) |
| 4 | 52–52 | Practitioner | – | – | `nama_data_entry` → `Practitioner.name.text` (52) |
| 5 | 55–63 | EpisodeOfCare | ANC | Antenatal Care | – |
| 6 | 66–82 | Encounter | – | – | `nama_data_entry` → `Encounter.participant.individual.display` (76)<br>`tanggal_kunjungan` → `Encounter.period.start` (77)<br>`puskesmas` → `Encounter.serviceProvider.reference` (103) 🔎 lookup master data |
| 7 | 84–91 | Condition | SP001135 | Presensi Posyandu | `keterangan` → `Condition.note` (91) |
| 8 | 105–119 | Observation | 385438008 | Source of information | `input_data` → `Observation.valueCodeableConcept.coding` (108) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Practitioner | 2 |
| Patient | 1 |
| Location | 1 |
| EpisodeOfCare | 1 |
| Encounter | 1 |
| Condition | 1 |
| Observation | 1 |
| **Total** | **8** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 59 | EpisodeOfCare | `EpisodeOfCare.type.coding` | ANC | Antenatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 2 | 86 | Condition | `Condition.code.coding` | SP001135 | Presensi Posyandu | http://terminology.kemkes.go.id/sp |
| 3 | 107 | Observation | `Observation.code.coding` | 385438008 | Source of information | http://snomed.info/sct |
| 4 | 108 | Observation | `Observation.valueCodeableConcept.coding` | SP000776 | Sigizi | http://terminology.kemkes.go.id/sp |
| 5 | 109 | Observation | `Observation.valueCodeableConcept.coding` | SP000777 | E-pus PKD | http://terminology.kemkes.go.id/sp |
| 6 | 110 | Observation | `Observation.valueCodeableConcept.coding` | SP000778 | E-pus | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah | Code |
|---|---|---|
| http://terminology.kemkes.go.id/sp | 4 | SP001135, SP000776, SP000777, SP000778 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 1 | ANC |
| http://snomed.info/sct | 1 | 385438008 |
| **Total** | **6** | |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel Kobo | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
