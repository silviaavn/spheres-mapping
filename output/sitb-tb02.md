# Output Form: SITB - TB 02 (Kartu Identitas Pasien)

Sumber: `mapping/phdt-data-dictionary-sitb-tb02.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-sitb-tb02.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 13 |
| Code (`jumlah code` = 1) | 15 |
| Code unik (code + CodeSystem) | 14 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 0 |
| Variabel BQ (unik) | 0 |
| Variabel raw (variabel dictionary; belum ada file mentah) | 22 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–5 | Patient | – | – | _Nama Lengkap_ → `Patient.name.text` (2, tanpa BQ)<br>_Alamat Lengkap_ → `Patient.address.line` (3, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (4, tanpa BQ) |
| 2 | 6–17 | Observation | 424144002 | Current chronological age | _Umur_ → `Observation.valueQuantity.value` (9, tanpa BQ) |
| 3 | 25–48 | Encounter | – | – | _Tahap Pengobatan_ → `Encounter.identifier.value` (27, tanpa BQ)<br>_Tanggal (Tanggal Perjanjian)_ → `Encounter.period.start` (35, tanpa BQ) |
| 4 | 49–57 | Condition | A16.2 | Tuberculosis of lung, without mention of bacteriological or histological confirmation | _Klasifikasi Penyakit_ → `Condition.clinicalStatus.coding` (49, tanpa BQ)<br>_Lokasi (klasifikasi penyakit)_ → `Condition.note` (57, tanpa BQ) |
| 5 | 58–76 | QuestionnaireResponse | – | – | _Tipe Pasien_ → `QuestionnaireResponse.item.item.linkId` (67, tanpa BQ)<br>_Lain-lain (sebutkan)_ → `QuestionnaireResponse.item.item.answer.valueString` (76, tanpa BQ) |
| 6 | 77–89 | CarePlan | – | – | _Tgl. Mulai Berobat_ → `CarePlan.period.start` (82, tanpa BQ)<br>_Paduan OAT yang diberikan_ → `CarePlan.activity.detail.description` (89, tanpa BQ) |
| 7 | 90–111 | MedicationRequest | – | – | – |
| 8 | 112–114 | MedicationDispense | – | – | – |
| 9 | 115–115 | MedicationRequest | – | – | – |
| 10 | 116–129 | MedicationDispense | – | – | _Jumlah OAT yang diberikan_ → `MedicationDispense.quantity.value` (128, tanpa BQ) |
| 11 | 130–140 | ServiceRequest | – | – | _Tanggal Harus Kembali_ → `ServiceRequest.occurenceDateTime` (140, tanpa BQ) |
| 12 | 141–153 | ServiceRequest | – | – | _Tanggal (Tanggal Perjanjian untuk periksa dahak ulang)_ → `ServiceRequest.occurenceDateTime` (151, tanpa BQ)<br>_Seminggu sebelum akhir bulan ke-_ → `ServiceRequest.reasonCode.text` (153, tanpa BQ) |
| 13 | 154–159 | ClinicalImpression | – | – | _Catatan Penting (oleh Dokter/Perawat)_ → `ClinicalImpression.note.text` (159, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| MedicationRequest | 2 |
| MedicationDispense | 2 |
| ServiceRequest | 2 |
| Patient | 1 |
| Observation | 1 |
| Encounter | 1 |
| Condition | 1 |
| QuestionnaireResponse | 1 |
| CarePlan | 1 |
| ClinicalImpression | 1 |
| **Total** | **13** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 8 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 2 | 51 | Condition | `Condition.code.coding` | A16.2 | Tuberculosis of lung, without mention of bacteriological or histological confirmation | http://hl7.org/fhir/sid/icd-10 |
| 3 | 52 | Condition | `Condition.code.coding` | A18 | Tuberculosis of other organs | http://hl7.org/fhir/sid/icd-10 |
| 4 | 69 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | new | Kasus Baru | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 5 | 70 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | relapse | Kasus Kambuh | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 6 | 71 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | loss-to-follow-up | Kasus Setelah Loss To Follow Up | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 7 | 72 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure | Kasus Pengobatan Setelah Gagal | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 8 | 73 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | not-eval | Pernah diobati tidak diketahui hasilnya | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 9 | 74 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | not-eval | Pernah diobati tidak diketahui hasilnya | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 10 | 75 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | other | Kasus lain-lain | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 11 | 85 | CarePlan | `CarePlan.activity.detail.code.coding` | TK000022 | Akan diobati/dirujuk | http://terminology.kemkes.go.id |
| 12 | 87 | CarePlan | `CarePlan.activity.detail.code.coding` | CP000006 | Paduan OAT | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 13 | 134 | ServiceRequest | `ServiceRequest.code` | 185389009 | Follow-up visit | http://snomed.info/sct |
| 14 | 145 | ServiceRequest | `ServiceRequest.code` | 269911007 | Sputum examination | http://snomed.info/sct |
| 15 | 152 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment | 7 |
| http://snomed.info/sct | 3 |
| http://hl7.org/fhir/sid/icd-10 | 2 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 2 |
| http://terminology.kemkes.go.id | 1 |
| **Total** | **15** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 18 | – | Nama UPK | Organization | `Organization.name` |
| 19 | – | Telp UPK | Organization | `Organization.telecom` |
| 22 | – | Provinsi | Organization | `Organization.address.state` |
| 23 | – | No. Reg. TBC UPK | – | `` |
| 24 | – | No. Reg. Kab/Kota | – | `` |
