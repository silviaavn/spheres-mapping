# Output Form: KuApps BidanKu - PHBS

Sumber: `mapping/phdt-data-dictionary-kuapps-bidanku-phbs.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-kuapps-bidanku-phbs.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 1 |
| Code (`jumlah code` = 1) | 3 |
| Code unik (code + CodeSystem) | 3 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 3 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–28 | QuestionnaireResponse | https://fhir.kemkes.go.id/sp/Questionnaire/Q00051 | – | _Apakah anda melakukan aktivitas fisik (olahraga) minimal 150 menit per minggu secara terus menerus?_ → `QuestionnaireResponse.item.linkId` (12, tanpa BQ)<br>_Apakah anda melakukan cuci tangan dengan menggunakan sabun dan air mengalir atau dengan hand sanitizer setiap tangan kotor dan waktu nya mencuci tangan?_ → `QuestionnaireResponse.item.linkId` (16, tanpa BQ)<br>_Apakah anda mengonsumsi buah dan sayur minimal 3 porsi (2 porsi sayur dan 1 porsi buah) setiap hari?_ → `QuestionnaireResponse.item.linkId` (20, tanpa BQ)<br>_Apakah Saat Ini Anda Perokok Aktif?_ → `QuestionnaireResponse.item.linkId` (25, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| QuestionnaireResponse | 1 |
| **Total** | **1** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 22 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000943 | > 3 porsi | http://terminology.kemkes.go.id/sp |
| 2 | 23 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000944 | 3 porsi | http://terminology.kemkes.go.id/sp |
| 3 | 24 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000945 | < 3 porsi | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://terminology.kemkes.go.id/sp | 3 |
| **Total** | **3** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
