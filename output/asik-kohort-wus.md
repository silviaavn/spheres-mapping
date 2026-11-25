# Output Form: ASIK - Data Individu Kohort WUS (Imunisasi)

Sumber: `mapping/phdt-data-dictionary-asik-kohort-wus.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-asik-kohort-wus.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 12 |
| Code (`jumlah code` = 1) | 20 |
| Code unik (code + CodeSystem) | 4 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 0 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–6 | Patient | – | – | _NIK_ → `Patient.identifier.value` (4, tanpa BQ)<br>_Nama_ → `Patient.name` (5, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (6, tanpa BQ) |
| 2 | 12–24 | Immunization | VG139 | – | _Status T1_ → `Immunization.vaccineCode.coding.system` (12, tanpa BQ)<br>_Tanggal Status T1_ → `Immunization.occurrenceDateTime` (19, tanpa BQ)<br>_Tanggal Input Status T1_ → `Immunization.recorded` (20, tanpa BQ)<br>_Pos Imunisasi Status T1_ → `Immunization.location` (21, tanpa BQ)<br>_Status Imunisasi Status T1_ → `Immunization.reasonCode[i].coding` (22, tanpa BQ) |
| 3 | 27–30 | Observation | 82810-3 | Pregnancy status | _Status Hamil_ → `Observation.valueCodeableConcept.coding` (29, tanpa BQ) |
| 4 | 32–50 | Immunization | VG139 | – | _Status T2_ → `Immunization.vaccineCode.coding.system` (38, tanpa BQ)<br>_Tanggal Status T2_ → `Immunization.occurrenceDateTime` (45, tanpa BQ)<br>_Tanggal Input Status T2_ → `Immunization.recorded` (46, tanpa BQ)<br>_Pos Imunisasi Status T2_ → `Immunization.location` (47, tanpa BQ)<br>_Status Imunisasi Status T2_ → `Immunization.reasonCode[i].coding` (48, tanpa BQ) |
| 5 | 53–56 | Observation | 82810-3 | Pregnancy status | _Status Hamil_ → `Observation.valueCodeableConcept.coding` (55, tanpa BQ) |
| 6 | 58–76 | Immunization | VG139 | – | _Status T3_ → `Immunization.vaccineCode.coding.system` (64, tanpa BQ)<br>_Tanggal Status T3_ → `Immunization.occurrenceDateTime` (71, tanpa BQ)<br>_Tanggal Input Status T3_ → `Immunization.recorded` (72, tanpa BQ)<br>_Pos Imunisasi Status T3_ → `Immunization.location` (73, tanpa BQ)<br>_Status Imunisasi Status T3_ → `Immunization.reasonCode[i].coding` (74, tanpa BQ) |
| 7 | 79–82 | Observation | 82810-3 | Pregnancy status | _Status Hamil_ → `Observation.valueCodeableConcept.coding` (81, tanpa BQ) |
| 8 | 84–102 | Immunization | VG139 | – | _Status T4_ → `Immunization.vaccineCode.coding.system` (90, tanpa BQ)<br>_Tanggal Status T4_ → `Immunization.occurrenceDateTime` (97, tanpa BQ)<br>_Tanggal Input Status T4_ → `Immunization.recorded` (98, tanpa BQ)<br>_Pos Imunisasi Status T4_ → `Immunization.location` (99, tanpa BQ)<br>_Status Imunisasi Status T4_ → `Immunization.reasonCode[i].coding` (100, tanpa BQ) |
| 9 | 105–108 | Observation | 82810-3 | Pregnancy status | _Status Hamil_ → `Observation.valueCodeableConcept.coding` (107, tanpa BQ) |
| 10 | 110–128 | Immunization | VG139 | – | _Status T5_ → `Immunization.vaccineCode.coding.system` (116, tanpa BQ)<br>_Tanggal Status T5_ → `Immunization.occurrenceDateTime` (123, tanpa BQ)<br>_Tanggal Input Status T5_ → `Immunization.recorded` (124, tanpa BQ)<br>_Pos Imunisasi Status T5_ → `Immunization.location` (125, tanpa BQ)<br>_Status Imunisasi Status T5_ → `Immunization.reasonCode[i].coding` (126, tanpa BQ) |
| 11 | 131–134 | Observation | 82810-3 | Pregnancy status | _Status Hamil_ → `Observation.valueCodeableConcept.coding` (133, tanpa BQ) |
| 12 | 136–138 | Immunization | – | – | – |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Immunization | 6 |
| Observation | 5 |
| Patient | 1 |
| **Total** | **12** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 13 | Immunization | `Immunization.vaccineCode.coding` | VG139 |  |  |
| 2 | 28 | Observation | `Observation.code.coding` | 82810-3 | Pregnancy status | http://loinc.org |
| 3 | 29 | Observation | `Observation.valueCodeableConcept.coding` | LA15173-0 | Pregnant | http://loinc.org |
| 4 | 30 | Observation | `Observation.valueCodeableConcept.coding` | LA26683-5 | Not pregnant | http://loinc.org |
| 5 | 39 | Immunization | `Immunization.vaccineCode.coding` | VG139 |  |  |
| 6 | 54 | Observation | `Observation.code.coding` | 82810-3 | Pregnancy status | http://loinc.org |
| 7 | 55 | Observation | `Observation.valueCodeableConcept.coding` | LA15173-0 | Pregnant | http://loinc.org |
| 8 | 56 | Observation | `Observation.valueCodeableConcept.coding` | LA26683-5 | Not pregnant | http://loinc.org |
| 9 | 65 | Immunization | `Immunization.vaccineCode.coding` | VG139 |  |  |
| 10 | 80 | Observation | `Observation.code.coding` | 82810-3 | Pregnancy status | http://loinc.org |
| 11 | 81 | Observation | `Observation.valueCodeableConcept.coding` | LA15173-0 | Pregnant | http://loinc.org |
| 12 | 82 | Observation | `Observation.valueCodeableConcept.coding` | LA26683-5 | Not pregnant | http://loinc.org |
| 13 | 91 | Immunization | `Immunization.vaccineCode.coding` | VG139 |  |  |
| 14 | 106 | Observation | `Observation.code.coding` | 82810-3 | Pregnancy status | http://loinc.org |
| 15 | 107 | Observation | `Observation.valueCodeableConcept.coding` | LA15173-0 | Pregnant | http://loinc.org |
| 16 | 108 | Observation | `Observation.valueCodeableConcept.coding` | LA26683-5 | Not pregnant | http://loinc.org |
| 17 | 117 | Immunization | `Immunization.vaccineCode.coding` | VG139 |  |  |
| 18 | 132 | Observation | `Observation.code.coding` | 82810-3 | Pregnancy status | http://loinc.org |
| 19 | 133 | Observation | `Observation.valueCodeableConcept.coding` | LA15173-0 | Pregnant | http://loinc.org |
| 20 | 134 | Observation | `Observation.valueCodeableConcept.coding` | LA26683-5 | Not pregnant | http://loinc.org |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://loinc.org | 15 |
|  | 5 |
| **Total** | **20** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 7 | – | Kelurahan atau Desa | – | `` |
| 8 | – | Kode Puskesmas | – | `` |
| 9 | – | Puskesmas | Organization | `Patient.identifier.use` |
| 31 | – | Sumber | – | `` |
| 57 | – | Sumber | – | `` |
| 83 | – | Sumber | – | `` |
| 109 | – | Sumber | – | `` |
| 135 | – | Sumber | – | `` |
| 142 | – | Status T2+ | – | `` |
| 149 | – | Tanggal Status T2+ | – | `` |
| 150 | – | Tanggal Input Status T2+ | – | `` |
| 151 | – | Pos Imunisasi Status T2+ | – | `` |
| 152 | – | Status Hamil | – | `` |
| 154 | – | Sumber | – | `` |
