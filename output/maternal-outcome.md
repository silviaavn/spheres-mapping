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
| Variabel BQ di luar payload | 0 ✅ |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 6–8 | PractitionerRole | – | – | `data_entry_clerk_type` → `PractitionerRole.code.coding` (6) |
| 2 | 9–12 | Practitioner | – | – | `data_entry_clerk_staff_id` → `Practitioner.name.text` (9)<br>`nik_yang_melakukan_entry_data` → `Practitioner.identifier.value` (12) |
| 3 | 14–19 | Patient | – | – | `nama_ibu` → `Patient.name.text` (14)<br>`nik_ibu` → `Patient.identifier.value` (17) |
| 4 | 23–37 | Encounter | – | – | `data_entry_clerk_staff_id` → `Encounter.participant.individual.display` (30)<br>`tanggal_pencatatan` → `Encounter.period.start` (31)<br>`puskesmas_name` → `Encounter.serviceProvider.reference` (58) 🔎 lookup master data |
| 5 | 39–46 | Condition | SP000738 | Kunjungan pemantauan luaran maternal | – |
| 6 | 60–61 | EpisodeOfCare | ANC | Antenatal Care | – |
| 7 | 63–64 | EpisodeOfCare | PNC | Postnatal Care | – |
| 8 | 69–81 | Observation | SP000389 | Keadaan Ibu | `outcome_001` → `Observation.valueCodeableConcept.coding` (72) |
| 9 | 83–93 | Observation | 93857-1 | Date and time of obstetric delivery | `delivery_date` → `Observation.valueDateTime` (86) |
| 10 | 95–106 | Observation | 81956-5 | Date and time of death [TimeStamp] | `tanggal_meninggal` → `Observation.valueDateTime` (98) |
| 11 | 108–119 | Observation | LT000005 | Alamat Mati | `tempat_meninggal` → `Observation.valueString` (111) |
| 12 | 121–132 | Observation | 79378-6 | Cause of death | `sebab_meninggal` → `Observation.valueString` (124) |

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
| 4 | 41 | Condition | `Condition.code.coding` | SP000738 | Kunjungan pemantauan luaran maternal | http://terminology.kemkes.go.id/sp |
| 5 | 60 | EpisodeOfCare | `EpisodeOfCare.type.coding` | ANC | Antenatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 6 | 63 | EpisodeOfCare | `EpisodeOfCare.type.coding` | PNC | Postnatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 7 | 71 | Observation | `Observation.code.coding` | SP000389 | Keadaan Ibu | http://terminology.kemkes.go.id/sp |
| 8 | 72 | Observation | `Observation.valueCodeableConcept.coding` | 102514002 | Well female adult | http://snomed.info/sct |
| 9 | 73 | Observation | `Observation.valueCodeableConcept.coding` | 39104002 | Illness | http://snomed.info/sct |
| 10 | 74 | Observation | `Observation.valueCodeableConcept.coding` | 419099009 | Dead | http://snomed.info/sct |
| 11 | 85 | Observation | `Observation.code.coding` | 93857-1 | Date and time of obstetric delivery | http://loinc.org |
| 12 | 97 | Observation | `Observation.code.coding` | 81956-5 | Date and time of death [TimeStamp] | http://loinc.org |
| 13 | 110 | Observation | `Observation.code.coding` | LT000005 | Alamat Mati | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 14 | 123 | Observation | `Observation.code.coding` | 79378-6 | Cause of death | http://loinc.org |

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

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel Kobo | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
