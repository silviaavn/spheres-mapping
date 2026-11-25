# Output Form: Buku KIA - PNC (2024)

Sumber: `mapping/phdt-data-dictionary-buku-kia-pnc.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-buku-kia-pnc.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 14 |
| Code (`jumlah code` = 1) | 32 |
| Code unik (code + CodeSystem) | 31 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 4 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 12–39 | Encounter | – | – | _Hari ke-/ KF_ → `Encounter.identifier` (12, tanpa BQ)<br>_Tanggal periksa_ → `Encounter.period.start` (24, tanpa BQ)<br>_Tempat Periksa_ → `Encounter.location.location.display` (28, tanpa BQ) |
| 2 | 40–47 | Condition | Z39.2 | Routine postpartum follow-up | – |
| 3 | 49–57 | EpisodeOfCare | PNC | Postnatal Care | _Tanggal melahirkan_ → `EpisodeOfCare.period.start` (53, tanpa BQ) |
| 4 | 58–69 | Observation | 32422-8 | Physical findings of breast | _Periksa Payudara (ASI)_ → `Observation.performer.display` (58, tanpa BQ) |
| 5 | 70–80 | Observation | 289530006 | Vaginal bleeding | _Periksa Pendarahan_ → `Observation.valueString` (73, tanpa BQ) |
| 6 | 81–91 | Observation | 35025007 | Manual pelvic examination | _Periksa Jalan Lahir_ → `Observation.valueString` (84, tanpa BQ) |
| 7 | 92–101 | Procedure | 767224000 | Administration of vitamin A | _Vitamin A_ → `Procedure.category.coding` (92, tanpa BQ) |
| 8 | 102–120 | Observation | SP000139 | KB Pasca Plasenta | _KB Pasca Melahirkan_ → `Observation.valueString` (105, tanpa BQ) |
| 9 | 121–131 | Procedure | 385892002 | Mental health screening | _Skrining Kesehatan Jiwa_ → `Procedure.category.coding` (121, tanpa BQ) |
| 10 | 132–142 | Procedure | 409063005 | Counseling | _Konseling_ → `Procedure.category.coding` (132, tanpa BQ) |
| 11 | 143–153 | Procedure | 409019001 | Postpartum care management | _Tatalaksana Kasus_ → `Procedure.category.coding` (143, tanpa BQ) |
| 12 | 154–167 | Observation | SP000389 | Keadaan Ibu | _Keadaan ibu_ → `Observation.valueCodeableConcept.coding` (157, tanpa BQ)<br>_Kesimpulan_ → `Observation.note` (167, tanpa BQ) |
| 13 | 168–181 | Observation | 249222005 | Neonatal condition | _Keadaan Bayi_ → `Observation.valueCodeableConcept.coding` (171, tanpa BQ) |
| 14 | 182–196 | Observation | 118213005 | Postpartum finding | _Masalah Nifas_ → `Observation.valueCodeableConcept.coding` (185, tanpa BQ)<br>_Masalah Nifas (Lainnya)_ → `Observation.valueCodeableConcept.text` (189, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 7 |
| Procedure | 4 |
| Encounter | 1 |
| Condition | 1 |
| EpisodeOfCare | 1 |
| **Total** | **14** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 42 | Condition | `Condition.code.coding` | Z39.2 | Routine postpartum follow-up | http://hl7.org/fhir/sid/icd-10 |
| 2 | 54 | EpisodeOfCare | `EpisodeOfCare.type.coding` | PNC | Postnatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 3 | 61 | Observation | `Observation.code.coding` | 32422-8 | Physical findings of breast | http://loinc.org |
| 4 | 72 | Observation | `Observation.code.coding` | 289530006 | Vaginal bleeding | http://snomed.info/sct |
| 5 | 83 | Observation | `Observation.code.coding` | 35025007 | Manual pelvic examination | http://snomed.info/sct |
| 6 | 93 | Procedure | `Procedure.code.coding` | 767224000 | Administration of vitamin A | http://snomed.info/sct |
| 7 | 104 | Observation | `Observation.code.coding` | SP000139 | KB Pasca Plasenta | http://terminology.kemkes.go.id/sp |
| 8 | 106 | Observation | `Observation.valueCodeableConcept.coding` | LA6524-8 | Oral contraceptive pill | http://loinc.org |
| 9 | 107 | Observation | `Observation.valueCodeableConcept.coding` | 237122005 | Lactational amenorrhea | http://snomed.info/sct |
| 10 | 108 | Observation | `Observation.valueCodeableConcept.coding` | LA6525-5 | Injectable/implantable hormone | http://loinc.org |
| 11 | 109 | Observation | `Observation.valueCodeableConcept.coding` | LA6527-1 | Intrauterine device | http://loinc.org |
| 12 | 110 | Observation | `Observation.valueCodeableConcept.coding` | SP000097 | Implan | http://terminology.kemkes.go.id/sp |
| 13 | 111 | Observation | `Observation.valueCodeableConcept.coding` | LA6523-0 | Condom | http://loinc.org |
| 14 | 112 | Observation | `Observation.valueCodeableConcept.coding` | 22523008 | Vasectomy | http://snomed.info/sct |
| 15 | 113 | Observation | `Observation.valueCodeableConcept.coding` | 77543007 | Ligation of fallopian tube | http://snomed.info/sct |
| 16 | 122 | Procedure | `Procedure.code.coding` | 385892002 | Mental health screening | http://snomed.info/sct |
| 17 | 133 | Procedure | `Procedure.code.coding` | 409063005 | Counseling | http://snomed.info/sct |
| 18 | 144 | Procedure | `Procedure.code.coding` | 409019001 | Postpartum care management | http://snomed.info/sct |
| 19 | 156 | Observation | `Observation.code.coding` | SP000389 | Keadaan Ibu | http://terminology.kemkes.go.id/sp |
| 20 | 157 | Observation | `Observation.valueCodeableConcept.coding` | 438949009 | Alive | http://snomed.info/sct |
| 21 | 158 | Observation | `Observation.valueCodeableConcept.coding` | 419099009 | Dead | http://snomed.info/sct |
| 22 | 159 | Observation | `Observation.valueCodeableConcept.coding` | 39104002 | Illness | http://snomed.info/sct |
| 23 | 170 | Observation | `Observation.code.coding` | 249222005 | Neonatal condition | http://snomed.info/sct |
| 24 | 171 | Observation | `Observation.valueCodeableConcept.coding` | 102500002 | Good neonatal condition at birth | http://snomed.info/sct |
| 25 | 172 | Observation | `Observation.valueCodeableConcept.coding` | 276707008 | Infant in poor condition at birth | http://terminology.kemkes.go.id/sp |
| 26 | 173 | Observation | `Observation.valueCodeableConcept.coding` | 419099009 | Dead | http://snomed.info/sct |
| 27 | 174 | Observation | `Observation.valueCodeableConcept.coding` | 66091009 | Congenital disease | http://snomed.info/sct |
| 28 | 184 | Observation | `Observation.code.coding` | 118213005 | Postpartum finding | http://snomed.info/sct |
| 29 | 185 | Observation | `Observation.valueCodeableConcept.coding` | 47821001 | Postpartum hemorrhage | http://snomed.info/sct |
| 30 | 186 | Observation | `Observation.valueCodeableConcept.coding` | 40733004 | Infectious disease | http://snomed.info/sct |
| 31 | 187 | Observation | `Observation.valueCodeableConcept.coding` | 38341003 | Hypertensive disorder, systemic arterial | http://snomed.info/sct |
| 32 | 188 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 21 |
| http://loinc.org | 5 |
| http://terminology.kemkes.go.id/sp | 4 |
| http://hl7.org/fhir/sid/icd-10 | 1 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 1 |
| **Total** | **32** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 2 | – | Jantung berdebar | – | `` |
| 3 | – | Keluar cairan dari jalan lahir. | – | `` |
| 4 | – | Napas pendek/ terengah-engah. | – | `` |
| 5 | – | Payudara bengkak/ nyeri/ada benjolan. | – | `` |
| 6 | – | Gangguan buang air kecil. | – | `` |
| 7 | – | Area kelamin bengkak/ nyeri/luka. | – | `` |
| 8 | – | Darah nifas berbau/ mengalir/ perut nyeri. | – | `` |
| 9 | – | Pendarahan > 2 pembalut kurun 5 menit. | – | `` |
| 10 | – | Keputihan. | – | `` |
