# Output Form: ePuskesmas Tumbuh Kembang - GPPH

Sumber: `mapping/phdt-data-dictionary-epus-tumbang-gpph.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-epus-tumbang-gpph.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 1 |
| Code (`jumlah code` = 1) | 40 |
| Code unik (code + CodeSystem) | 4 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 20 |
| Variabel BQ (unik) | 0 |
| Variabel raw (variabel dictionary; belum ada file mentah) | 10 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–69 | QuestionnaireResponse | tanpa-URL-1d3f9a | Kuesioner tanpa URL: Tidak kenal lelah atau aktvitas yang berlebihan | _Tidak kenal lelah atau aktvitas yang berlebihan_ → `QuestionnaireResponse.item.linkId` (10, tanpa BQ)<br>_Mudah menjadi gembira, impulsif_ → `QuestionnaireResponse.item.linkId` (16, tanpa BQ)<br>_Mengganggu anak-anak lain_ → `QuestionnaireResponse.item.linkId` (22, tanpa BQ)<br>_Gagal menyelesaikan kegiatan yang telah dimulai; rentang perhatian pendek_ → `QuestionnaireResponse.item.linkId` (28, tanpa BQ)<br>_Menggerak-gerakkan anggota badan atau kepala secara terus menerus_ → `QuestionnaireResponse.item.linkId` (34, tanpa BQ)<br>_Kurang memperhatikan, mudah teralihkan_ → `QuestionnaireResponse.item.linkId` (40, tanpa BQ)<br>_Permintaannya harus segera dipenuhi; mudah menjadi frustrasi_ → `QuestionnaireResponse.item.linkId` (46, tanpa BQ)<br>_Sering dan mudah menangis_ → `QuestionnaireResponse.item.linkId` (52, tanpa BQ)<br>_Suasana hatinya mudah berubah dengan cepat dan drastis_ → `QuestionnaireResponse.item.linkId` (58, tanpa BQ)<br>_Ledakan kekesalan, tingkah laku eksplosif dan tak terduga_ → `QuestionnaireResponse.item.linkId` (64, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| QuestionnaireResponse | 1 |
| **Total** | **1** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 12 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 373067005 | No | http://snomed.info/sct |
| 2 | 13 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP000363 | Kadang-Kadang | http://terminology.kemkes.go.id/sp |
| 3 | 14 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 70232002 | Frequent | http://snomed.info/sct |
| 4 | 15 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP000366 | Selalu | http://terminology.kemkes.go.id/sp |
| 5 | 18 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 373067005 | No | http://snomed.info/sct |
| 6 | 19 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP000363 | Kadang-Kadang | http://terminology.kemkes.go.id/sp |
| 7 | 20 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 70232002 | Frequent | http://snomed.info/sct |
| 8 | 21 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP000366 | Selalu | http://terminology.kemkes.go.id/sp |
| 9 | 24 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 373067005 | No | http://snomed.info/sct |
| 10 | 25 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP000363 | Kadang-Kadang | http://terminology.kemkes.go.id/sp |
| 11 | 26 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 70232002 | Frequent | http://snomed.info/sct |
| 12 | 27 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP000366 | Selalu | http://terminology.kemkes.go.id/sp |
| 13 | 30 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 373067005 | No | http://snomed.info/sct |
| 14 | 31 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP000363 | Kadang-Kadang | http://terminology.kemkes.go.id/sp |
| 15 | 32 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 70232002 | Frequent | http://snomed.info/sct |
| 16 | 33 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP000366 | Selalu | http://terminology.kemkes.go.id/sp |
| 17 | 36 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 373067005 | No | http://snomed.info/sct |
| 18 | 37 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP000363 | Kadang-Kadang | http://terminology.kemkes.go.id/sp |
| 19 | 38 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 70232002 | Frequent | http://snomed.info/sct |
| 20 | 39 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP000366 | Selalu | http://terminology.kemkes.go.id/sp |
| 21 | 42 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 373067005 | No | http://snomed.info/sct |
| 22 | 43 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP000363 | Kadang-Kadang | http://terminology.kemkes.go.id/sp |
| 23 | 44 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 70232002 | Frequent | http://snomed.info/sct |
| 24 | 45 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP000366 | Selalu | http://terminology.kemkes.go.id/sp |
| 25 | 48 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 373067005 | No | http://snomed.info/sct |
| 26 | 49 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP000363 | Kadang-Kadang | http://terminology.kemkes.go.id/sp |
| 27 | 50 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 70232002 | Frequent | http://snomed.info/sct |
| 28 | 51 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP000366 | Selalu | http://terminology.kemkes.go.id/sp |
| 29 | 54 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 373067005 | No | http://snomed.info/sct |
| 30 | 55 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP000363 | Kadang-Kadang | http://terminology.kemkes.go.id/sp |
| 31 | 56 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 70232002 | Frequent | http://snomed.info/sct |
| 32 | 57 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP000366 | Selalu | http://terminology.kemkes.go.id/sp |
| 33 | 60 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 373067005 | No | http://snomed.info/sct |
| 34 | 61 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP000363 | Kadang-Kadang | http://terminology.kemkes.go.id/sp |
| 35 | 62 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 70232002 | Frequent | http://snomed.info/sct |
| 36 | 63 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP000366 | Selalu | http://terminology.kemkes.go.id/sp |
| 37 | 66 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 373067005 | No | http://snomed.info/sct |
| 38 | 67 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP000363 | Kadang-Kadang | http://terminology.kemkes.go.id/sp |
| 39 | 68 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 70232002 | Frequent | http://snomed.info/sct |
| 40 | 69 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP000366 | Selalu | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 20 |
| http://terminology.kemkes.go.id/sp | 20 |
| **Total** | **40** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
