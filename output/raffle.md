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

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ (baris) |
|---|---|---|---|---|---|
| 1 | 8–20 | Patient | – | – | `nama_ibu` (8)<br>`nik_ibu` (10)<br>`nomor_telepon` (18) |
| 2 | 43–66 | Location | – | – | `lokasi_faskes` (43)<br>_Provinsi_ (51, tanpa BQ)<br>_Kabupaten/Kota_ (54, tanpa BQ)<br>`kecamatan` (57)<br>`kelurahan` (60) |
| 3 | 69–69 | Practitioner | – | – | `nama_bidan_desa` (69) |
| 4 | 70–70 | Practitioner | – | – | `nama_data_entry` (70) |
| 5 | 73–81 | EpisodeOfCare | ANC | Antenatal Care | – |
| 6 | 84–100 | Encounter | – | – | `nama_data_entry` (94)<br>`tanggal_kunjungan` (95) |
| 7 | 102–109 | Condition | SP001135 | Presensi Posyandu | `keterangan` (109) |
| 8 | 123–137 | Observation | 385438008 | Source of information | `input_data` (125) |

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
| 1 | 77 | EpisodeOfCare | `EpisodeOfCare.type.coding` | ANC | Antenatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 2 | 104 | Condition | `Condition.code.coding` | SP001135 | Presensi Posyandu | http://terminology.kemkes.go.id/sp |
| 3 | 125 | Observation | `Observation.code.coding` | 385438008 | Source of information | http://snomed.info/sct |
| 4 | 126 | Observation | `Observation.valueCodeableConcept.coding` | SP000776 | Sigizi | http://terminology.kemkes.go.id/sp |
| 5 | 127 | Observation | `Observation.valueCodeableConcept.coding` | SP000777 | E-pus PKD | http://terminology.kemkes.go.id/sp |
| 6 | 128 | Observation | `Observation.valueCodeableConcept.coding` | SP000778 | E-pus | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah | Code |
|---|---|---|
| http://terminology.kemkes.go.id/sp | 4 | SP001135, SP000776, SP000777, SP000778 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 1 | ANC |
| http://snomed.info/sct | 1 | 385438008 |
| **Total** | **6** | |

## Variabel di luar payload

Variabel yang ada di dictionary tapi tidak masuk blok payload mana pun (mis. master data).

| Baris | Variabel BQ | Variabel Kobo | Resource | Path |
|---|---|---|---|---|
| 27 | puskesmas | Puskesmas Pengampu | Organization | `Organization.name` |
| 31 | – | Provinsi | Organization | `Organization.address.extension.extension.url` |
| 34 | – | Kabupaten/Kota | Organization | `Organization.address.extension.extension.url` |
