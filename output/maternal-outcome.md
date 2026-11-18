# Output Form: Maternal Outcome

Sumber: `mapping/kobo-data-dictionary-maternal-outcome.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/kobo-data-dictionary-maternal-outcome.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 12 |
| Code (`jumlah code` = 1) | 14 |
| Code unik (code + CodeSystem) | 14 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 4 |
| Variabel BQ (unik) | 12 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 6–9 | PractitionerRole | – | – | `data_entry_clerk_type` → `PractitionerRole.code.coding` (6) |
| 2 | 10–13 | Practitioner | – | – | `data_entry_clerk_staff_id` → `Practitioner.name.text` (10)<br>`nik_yang_melakukan_entry_data` → `Practitioner.identifier.value` (13) |
| 3 | 15–20 | Patient | – | – | `nama_ibu` → `Patient.name.text` (15)<br>`nik_ibu` → `Patient.identifier.value` (18) |
| 4 | 24–38 | Encounter | – | – | `data_entry_clerk_staff_id` → `Encounter.participant.individual.display` (31)<br>`tanggal_pencatatan` → `Encounter.period.start` (32)<br>`puskesmas_name` → `Encounter.serviceProvider.reference` (59) 🔎 lookup master data |
| 5 | 40–47 | Condition | SP000738 | Kunjungan pemantauan luaran maternal | – |
| 6 | 61–63 | EpisodeOfCare | ANC | Antenatal Care | – |
| 7 | 65–67 | EpisodeOfCare | PNC | Postnatal Care | – |
| 8 | 72–84 | Observation | SP000389 | Keadaan Ibu | `outcome_001` → `Observation.valueCodeableConcept.coding` (75) |
| 9 | 86–96 | Observation | 93857-1 | Date and time of obstetric delivery | `delivery_date` → `Observation.valueDateTime` (89) |
| 10 | 98–108 | Observation | 81956-5 | Date and time of death [TimeStamp] | `tanggal_meninggal` → `Observation.valueDateTime` (101) |
| 11 | 110–120 | Observation | LT000005 | Alamat Mati | `tempat_meninggal` → `Observation.valueString` (113) |
| 12 | 122–132 | Observation | 79378-6 | Cause of death | `sebab_meninggal` → `Observation.valueString` (125) |

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
| 4 | 42 | Condition | `Condition.code.coding` | SP000738 | Kunjungan pemantauan luaran maternal | http://terminology.kemkes.go.id/sp |
| 5 | 61 | EpisodeOfCare | `EpisodeOfCare.type.coding` | ANC | Antenatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 6 | 65 | EpisodeOfCare | `EpisodeOfCare.type.coding` | PNC | Postnatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 7 | 74 | Observation | `Observation.code.coding` | SP000389 | Keadaan Ibu | http://terminology.kemkes.go.id/sp |
| 8 | 75 | Observation | `Observation.valueCodeableConcept.coding` | 102514002 | Well female adult | http://snomed.info/sct |
| 9 | 76 | Observation | `Observation.valueCodeableConcept.coding` | 39104002 | Illness | http://snomed.info/sct |
| 10 | 77 | Observation | `Observation.valueCodeableConcept.coding` | 419099009 | Dead | http://snomed.info/sct |
| 11 | 88 | Observation | `Observation.code.coding` | 93857-1 | Date and time of obstetric delivery | http://loinc.org |
| 12 | 100 | Observation | `Observation.code.coding` | 81956-5 | Date and time of death [TimeStamp] | http://loinc.org |
| 13 | 112 | Observation | `Observation.code.coding` | LT000005 | Alamat Mati | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 14 | 124 | Observation | `Observation.code.coding` | 79378-6 | Cause of death | http://loinc.org |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 4 |
| http://terminology.kemkes.go.id/sp | 4 |
| http://loinc.org | 3 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 2 |
| http://terminology.kemkes.go.id/CodeSystem/location-type | 1 |
| **Total** | **14** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
