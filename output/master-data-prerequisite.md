# Output Form: Master Data (Prerequisite)

Sumber: `mapping/phdt-data-dictionary-master-data-prerequisite.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-master-data-prerequisite.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 0 |
| Code (`jumlah code` = 1) | 15 |
| Code unik (code + CodeSystem) | 15 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 15 |
| Variabel BQ (unik) | 0 |
| Variabel raw (variabel dictionary; belum ada file mentah) | 15 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|

### Payload per resource

| Resource | Jumlah |
|---|---|
| **Total** | **0** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 2 | PractitionerRole | `PractitionerRole.code.coding` | SP000048 | Pengelola Sistem Informasi dan Basis Data (Database) | http://terminology.kemkes.go.id/sp |
| 2 | 3 | PractitionerRole | `PractitionerRole.code.coding` | SP000049 | Cleaning Service | http://terminology.kemkes.go.id/sp |
| 3 | 4 | PractitionerRole | `PractitionerRole.code.coding` | SP000434 | Vaksinator | http://terminology.kemkes.go.id/sp |
| 4 | 5 | PractitionerRole | `PractitionerRole.code.coding` | SP000677 | PJ SITB | http://terminology.kemkes.go.id/sp |
| 5 | 6 | PractitionerRole | `PractitionerRole.code.coding` | SP000714 | PJ KIA | http://terminology.kemkes.go.id/sp |
| 6 | 7 | PractitionerRole | `PractitionerRole.specialty.coding` | SP001124 | Kader Madya | http://terminology.kemkes.go.id/sp |
| 7 | 8 | PractitionerRole | `PractitionerRole.specialty.coding` | SP001125 | Kader Purwa | http://terminology.kemkes.go.id/sp |
| 8 | 9 | PractitionerRole | `PractitionerRole.specialty.coding` | SP001126 | Kader Utama | http://terminology.kemkes.go.id/sp |
| 9 | 10 | Organization | `Organization.type.coding` | SP000385 | Taman Kanak-Kanak | http://terminology.kemkes.go.id/CodeSystem/organization-type/sp |
| 10 | 11 | Organization | `Organization.type.coding` | SP000386 | Kelompok Bermain | http://terminology.kemkes.go.id/CodeSystem/organization-type/sp |
| 11 | 12 | Organization | `Organization.type.coding` | SP000387 | Taman Penitipan Anak | http://terminology.kemkes.go.id/CodeSystem/organization-type/sp |
| 12 | 13 | Organization | `Organization.type.coding` | SP000388 | Satuan PAUD Sejenis | http://terminology.kemkes.go.id/CodeSystem/organization-type/sp |
| 13 | 14 | Organization | `Organization.type.coding` | SP000457 | Pendidikan Anak Usia Dini Al-Quran | http://terminology.kemkes.go.id/CodeSystem/organization-type/sp |
| 14 | 15 | Organization | `Organization.type.coding` | SP000458 | Raudhatul Athfal | http://terminology.kemkes.go.id/CodeSystem/organization-type/sp |
| 15 | 16 | Organization | `Organization.type.coding` | SP000753 | Kelurahan | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://terminology.kemkes.go.id/sp | 9 |
| http://terminology.kemkes.go.id/CodeSystem/organization-type/sp | 6 |
| **Total** | **15** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 2 | – | Pengelola Sistem Informasi dan Basis Data (Database) | PractitionerRole | `PractitionerRole.code.coding` |
| 3 | – | Cleaning Service | PractitionerRole | `PractitionerRole.code.coding` |
| 4 | – | Vaksinator | PractitionerRole | `PractitionerRole.code.coding` |
| 5 | – | PJ SITB | PractitionerRole | `PractitionerRole.code.coding` |
| 6 | – | PJ KIA | PractitionerRole | `PractitionerRole.code.coding` |
| 7 | – | Kader Madya | PractitionerRole | `PractitionerRole.specialty.coding` |
| 8 | – | Kader Purwa | PractitionerRole | `PractitionerRole.specialty.coding` |
| 9 | – | Kader Utama | PractitionerRole | `PractitionerRole.specialty.coding` |
| 10 | – | Taman Kanak-Kanak | Organization | `Organization.type.coding` |
| 11 | – | Kelompok Bermain | Organization | `Organization.type.coding` |
| 12 | – | Taman Penitipan Anak | Organization | `Organization.type.coding` |
| 13 | – | Satuan PAUD Sejenis | Organization | `Organization.type.coding` |
| 14 | – | Pendidikan Anak Usia Dini Al-Quran | Organization | `Organization.type.coding` |
| 15 | – | Raudhatul Athfal | Organization | `Organization.type.coding` |
| 16 | – | Kelurahan | Organization | `Organization.type.coding` |
