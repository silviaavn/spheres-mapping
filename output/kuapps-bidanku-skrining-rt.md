# Output Form: KuApps BidanKu - Skrining Rumah Tangga

Sumber: `mapping/phdt-data-dictionary-kuapps-bidanku-skrining-rt.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-kuapps-bidanku-skrining-rt.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 2 |
| Code (`jumlah code` = 1) | 0 |
| Code unik (code + CodeSystem) | 0 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 0 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–35 | QuestionnaireResponse | – | – | _Jumlah Anggota Keluarga_ → `QuestionnaireResponse.item.linkId` (12, tanpa BQ)<br>_Jumlah Ibu Hamil_ → `QuestionnaireResponse.item.linkId` (15, tanpa BQ)<br>_Jumlah Ibu Bersalin dan Nifas_ → `QuestionnaireResponse.item.linkId` (18, tanpa BQ)<br>_Jumlah Bayi (0-6) Bulan_ → `QuestionnaireResponse.item.linkId` (21, tanpa BQ)<br>_Jumlah Balita (0-71) bulan_ → `QuestionnaireResponse.item.linkId` (24, tanpa BQ)<br>_Jumlah Usek dan Remaja_ → `QuestionnaireResponse.item.linkId` (27, tanpa BQ)<br>_Jumlah Dewasa_ → `QuestionnaireResponse.item.linkId` (30, tanpa BQ)<br>_Jumlah Lansia_ → `QuestionnaireResponse.item.linkId` (33, tanpa BQ) |
| 2 | 36–70 | QuestionnaireResponse | – | – | _Berapa jumlah pendapatan Keluarga_ → `QuestionnaireResponse.item.linkId` (46, tanpa BQ)<br>_Apakah tersedia sarana air bersih di lingkungan rumah_ → `QuestionnaireResponse.item.linkId` (55, tanpa BQ)<br>_Apakah tersedia jamban keluarga_ → `QuestionnaireResponse.item.linkId` (59, tanpa BQ)<br>_Jika "Ya", apakah jambannya saniter?_ → `QuestionnaireResponse.item.linkId` (63, tanpa BQ)<br>_Apakah rumah memiliki ventilasi yang cukup_ → `QuestionnaireResponse.item.linkId` (67, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| QuestionnaireResponse | 2 |
| **Total** | **2** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| **Total** | **0** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
