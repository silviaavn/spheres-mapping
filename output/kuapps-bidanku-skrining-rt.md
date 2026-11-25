# Output Form: KuApps BidanKu - Skrining Rumah Tangga

Sumber: `mapping/phdt-data-dictionary-kuapps-bidanku-skrining-rt.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-kuapps-bidanku-skrining-rt.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 2 |
| Code (`jumlah code` = 1) | 9 |
| Code unik (code + CodeSystem) | 9 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 9 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–35 | QuestionnaireResponse | https://fhir.kemkes.go.id/sp/Questionnaire/Q00054 | – | _Jumlah Anggota Keluarga_ → `QuestionnaireResponse.item.linkId` (12, tanpa BQ)<br>_Jumlah Ibu Hamil_ → `QuestionnaireResponse.item.linkId` (15, tanpa BQ)<br>_Jumlah Ibu Bersalin dan Nifas_ → `QuestionnaireResponse.item.linkId` (18, tanpa BQ)<br>_Jumlah Bayi (0-6) Bulan_ → `QuestionnaireResponse.item.linkId` (21, tanpa BQ)<br>_Jumlah Balita (0-71) bulan_ → `QuestionnaireResponse.item.linkId` (24, tanpa BQ)<br>_Jumlah Usek dan Remaja_ → `QuestionnaireResponse.item.linkId` (27, tanpa BQ)<br>_Jumlah Dewasa_ → `QuestionnaireResponse.item.linkId` (30, tanpa BQ)<br>_Jumlah Lansia_ → `QuestionnaireResponse.item.linkId` (33, tanpa BQ) |
| 2 | 36–70 | QuestionnaireResponse | https://fhir.kemkes.go.id/sp/Questionnaire/Q00053 | – | _Berapa jumlah pendapatan Keluarga_ → `QuestionnaireResponse.item.linkId` (46, tanpa BQ)<br>_Apakah tersedia sarana air bersih di lingkungan rumah_ → `QuestionnaireResponse.item.linkId` (55, tanpa BQ)<br>_Apakah tersedia jamban keluarga_ → `QuestionnaireResponse.item.linkId` (59, tanpa BQ)<br>_Jika "Ya", apakah jambannya saniter?_ → `QuestionnaireResponse.item.linkId` (63, tanpa BQ)<br>_Apakah rumah memiliki ventilasi yang cukup_ → `QuestionnaireResponse.item.linkId` (67, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| QuestionnaireResponse | 2 |
| **Total** | **2** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 48 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000233 | < Rp. 500.000 | http://terminology.kemkes.go.id/sp |
| 2 | 49 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000234 | Rp. 500,000 - Rp. 999,999 | http://terminology.kemkes.go.id/sp |
| 3 | 50 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000235 | Rp. 1,000,000 - Rp. 1,999,999 | http://terminology.kemkes.go.id/sp |
| 4 | 51 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000956 | Rp. 2,000,000 - Rp. 2,999,999 | http://terminology.kemkes.go.id/sp |
| 5 | 52 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000957 | Rp. 3,000,000 - Rp. 4,999,999 | http://terminology.kemkes.go.id/sp |
| 6 | 53 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000958 | Rp. 5,000,000 - Rp. 9,999,999 | http://terminology.kemkes.go.id/sp |
| 7 | 54 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000959 | ≥ Rp 10.000.000 | http://terminology.kemkes.go.id/sp |
| 8 | 65 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000971 | Closet | http://terminology.kemkes.go.id/sp |
| 9 | 66 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000094 | Jamban milik sendiri dengan leher angsa dan tangki septik/IPAL | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://terminology.kemkes.go.id/sp | 9 |
| **Total** | **9** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
