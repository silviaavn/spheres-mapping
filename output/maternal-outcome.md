# Output Form: Maternal Outcome

Sumber: `mapping/kobo-data-dictionary-maternal-outcome.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 12 |
| Code (`jumlah code` = 1) | 14 |
| Code unik (code + CodeSystem) | 14 |
| Variabel BQ (unik) | 12 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ (baris) |
|---|---|---|---|---|---|
| 1 | 6–8 | PractitionerRole | – | – | `data_entry_clerk_type` (6) |
| 2 | 9–12 | Practitioner | – | – | `data_entry_clerk_staff_id` (9)<br>`nik_yang_melakukan_entry_data` (10) |
| 3 | 14–19 | Patient | – | – | `nama_ibu` (14)<br>`nik_ibu` (15) |
| 4 | 55–69 | Encounter | – | – | `data_entry_clerk_staff_id` (62)<br>`tanggal_pencatatan` (63) |
| 5 | 71–78 | Condition | SP000738 | Kunjungan pemantauan luaran maternal | – |
| 6 | 92–93 | EpisodeOfCare | ANC | Antenatal Care | – |
| 7 | 95–96 | EpisodeOfCare | PNC | Postnatal Care | – |
| 8 | 101–113 | Observation | SP000389 | Keadaan Ibu | `outcome_001` (101) |
| 9 | 115–125 | Observation | 93857-1 | Date and time of obstetric delivery | `delivery_date` (115) |
| 10 | 127–138 | Observation | 81956-5 | Date and time of death [TimeStamp] | `tanggal_meninggal` (127) |
| 11 | 140–151 | Observation | LT000005 | Alamat Mati | `tempat_meninggal` (140) |
| 12 | 153–164 | Observation | 79378-6 | Cause of death | `sebab_meninggal` (153) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 5 |
| EpisodeOfCare | 2 |
| PractitionerRole | 1 |
| Practitioner | 1 |
| Patient | 1 |
| Encounter | 1 |
| Condition | 1 |
| **Total** | **12** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 6 | PractitionerRole | `PractitionerRole.code.coding` | 223366009 | Healthcare professional | http://snomed.info/sct |
| 2 | 7 | PractitionerRole | `PractitionerRole.code.coding` | SP000396 | Data entry staff | http://terminology.kemkes.go.id/sp |
| 3 | 8 | PractitionerRole | `PractitionerRole.code.coding` | SP000397 | Field/call center staff | http://terminology.kemkes.go.id/sp |
| 4 | 73 | Condition | `Condition.code.coding` | SP000738 | Kunjungan pemantauan luaran maternal | http://terminology.kemkes.go.id/sp |
| 5 | 92 | EpisodeOfCare | `EpisodeOfCare.type.coding` | ANC | Antenatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 6 | 95 | EpisodeOfCare | `EpisodeOfCare.type.coding` | PNC | Postnatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 7 | 103 | Observation | `Observation.code.coding` | SP000389 | Keadaan Ibu | http://terminology.kemkes.go.id/sp |
| 8 | 104 | Observation | `Observation.valueCodeableConcept.coding` | 102514002 | Well female adult | http://snomed.info/sct |
| 9 | 105 | Observation | `Observation.valueCodeableConcept.coding` | 39104002 | Illness | http://snomed.info/sct |
| 10 | 106 | Observation | `Observation.valueCodeableConcept.coding` | 419099009 | Dead | http://snomed.info/sct |
| 11 | 117 | Observation | `Observation.code.coding` | 93857-1 | Date and time of obstetric delivery | http://loinc.org |
| 12 | 129 | Observation | `Observation.code.coding` | 81956-5 | Date and time of death [TimeStamp] | http://loinc.org |
| 13 | 142 | Observation | `Observation.code.coding` | LT000005 | Alamat Mati | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 14 | 155 | Observation | `Observation.code.coding` | 79378-6 | Cause of death | http://loinc.org |

### Code per CodeSystem

| CodeSystem | Jumlah | Code |
|---|---|---|
| http://snomed.info/sct | 4 | 223366009, 102514002, 39104002, 419099009 |
| http://terminology.kemkes.go.id/sp | 4 | SP000396, SP000397, SP000738, SP000389 |
| http://loinc.org | 3 | 93857-1, 81956-5, 79378-6 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 2 | ANC, PNC |
| http://terminology.kemkes.go.id/CodeSystem/location-type | 1 | LT000005 |
| **Total** | **14** | |

## Variabel di luar payload

Variabel yang ada di dictionary tapi tidak masuk blok payload mana pun (mis. master data).

| Baris | Variabel BQ | Variabel Kobo | Resource | Path |
|---|---|---|---|---|
| 26 | puskesmas_name | Puskesmas | Organization | `Organization.name` |
