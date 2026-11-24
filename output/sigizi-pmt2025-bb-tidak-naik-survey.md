# Output Form: SiGizi PMT 2025 BB Tidak Naik - Survey

Sumber: `mapping/phdt-data-dictionary-sigizi-pmt2025-bb-tidak-naik-survey.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-sigizi-pmt2025-bb-tidak-naik-survey.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 5 |
| Code (`jumlah code` = 1) | 16 |
| Code unik (code + CodeSystem) | 15 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 4 |
| Variabel BQ (unik) | 20 |
| Variabel raw (variabel dictionary; belum ada file mentah) | 20 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 4–26 | Patient | – | – | `nama` → `Patient.name.text` (4)<br>`nik` → `Patient.identifier.value` (7)<br>`jk` → `Patient.gender` (9)<br>`tgl_lahir` → `Patient.birthDate` (11)<br>`prov` → `Patient.address.extension.extension.valueCode` (17)<br>`kabkota` → `Patient.address.extension.extension.valueCode` (20)<br>`kec` → `Patient.address.extension.extension.valueCode` (23)<br>`desakel` → `Patient.address.extension.extension.valueCode` (26) |
| 2 | 112–127 | Encounter | – | – | `posyandu` → `Encounter.location.reference` (123) 🔎 lookup master data<br>`pukesmas` → `Encounter.serviceProvider.reference` (127) 🔎 lookup master data<br>`tindakan` → `Encounter.extension.valueString` (147) |
| 3 | 128–134 | Condition | 385984007 | Growth and development treatments and procedures | – |
| 4 | 148–160 | Observation | SP000036 | Jenis PMT | `jenis_mt_yang_diberikan` → `Observation.valueCodeableConcept.coding` (151) |
| 5 | 161–207 | QuestionnaireResponse | – | – | `dimana_tempat_balita_diberikan_mt` → `QuestionnaireResponse.item.linkId` (171)<br>`berapa_kali_mt_diberikan_dalam_1_bulan` → `QuestionnaireResponse.item.linkId` (177)<br>`apakah_balita_menyukai_mt_yang_diberikan_aspek_organoleptik_rasa_penyajian_dll` → `QuestionnaireResponse.item.linkId` (181)<br>`alasan_jika_tidak_menyukai_mt` → `QuestionnaireResponse.item.item.linkId` (185)<br>`apakah_ada_keluhan_pada_saat_dan_setelah_mengonsumsi_mt` → `QuestionnaireResponse.item.linkId` (192)<br>`apakah_ibu_mendapat_penyuluhan_gizi_seimbang_pada_saat_pemberian_mt` → `QuestionnaireResponse.item.linkId` (196)<br>`apakah_ibu_mengerti_tentang_pesan_yang_disampaikan` → `QuestionnaireResponse.item.linkId` (200)<br>`apakah_ibu_dapat_mempraktikkan_pesan_yang_disampaikan_di_rumah` → `QuestionnaireResponse.item.linkId` (204) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Patient | 1 |
| Encounter | 1 |
| Condition | 1 |
| Observation | 1 |
| QuestionnaireResponse | 1 |
| **Total** | **5** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 130 | Condition | `Condition.code.coding` | 385984007 | Growth and development treatments and procedures | http://snomed.info/sct |
| 2 | 150 | Observation | `Observation.code.coding` | SP000036 | Jenis PMT | http://terminology.kemkes.go.id/sp |
| 3 | 151 | Observation | `Observation.valueCodeableConcept.coding` | SP000493 | Makanan Lengkap | http://terminology.kemkes.go.id/sp |
| 4 | 152 | Observation | `Observation.valueCodeableConcept.coding` | 228070005 | Snack food | http://snomed.info/sct |
| 5 | 153 | Observation | `Observation.valueCodeableConcept.coding` | SP000494 | Makanan Lengkap dan Makanan Kudapan | http://terminology.kemkes.go.id/sp |
| 6 | 173 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 131 | Posyandu | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 7 | 174 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP000495 | Kelas Ibu Hamil | http://terminology.kemkes.go.id/sp |
| 8 | 175 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 264362003 | Home | http://snomed.info/sct |
| 9 | 176 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 74964007 | Other | http://snomed.info/sct |
| 10 | 179 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | QRI000016 | Ya, setiap hari | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 11 | 180 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | QRI000015 | Ya, tidak setiap hari | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 12 | 187 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 248134002 | Aversion to food or drink | http://snomed.info/sct |
| 13 | 188 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 79890006 | Loss of appetite | http://snomed.info/sct |
| 14 | 189 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 261015003 | Full | http://snomed.info/sct |
| 15 | 190 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 39104002 | Illness | http://snomed.info/sct |
| 16 | 191 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 74964007 | Other | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 9 |
| http://terminology.kemkes.go.id/sp | 4 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 2 |
| http://terminology.kemkes.go.id/CodeSystem/organization-type | 1 |
| **Total** | **16** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
