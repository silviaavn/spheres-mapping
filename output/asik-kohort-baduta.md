# Output Form: ASIK - Data Individu Kohort Baduta (Imunisasi)

Sumber: `mapping/phdt-data-dictionary-asik-kohort-baduta.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-asik-kohort-baduta.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 4 |
| Code (`jumlah code` = 1) | 6 |
| Code unik (code + CodeSystem) | 6 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 0 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–11 | Patient | – | – | _NIK Anak_ → `Patient.identifier.value` (4, tanpa BQ)<br>_Nama Anak_ → `Patient.name` (5, tanpa BQ)<br>_Tanggal Lahir Anak_ → `Patient.birthDate` (6, tanpa BQ)<br>_Jenis Kelamin Anak_ → `Patient.gender` (7, tanpa BQ)<br>_NIK Orang Tua_ → `Patient.identifier.value` (11, tanpa BQ) |
| 2 | 18–59 | Immunization | VG45 | – | _Tanggal Imunisasi DPT-Hb-Hib 4_ → `Immunization.occurrenceDateTime` (18, tanpa BQ)<br>_Tanggal Input DPT-Hb-Hib 4_ → `Immunization.recorded` (19, tanpa BQ)<br>_Pos Imunisasi DPT-Hb-Hib 4_ → `Immunization.location` (36, tanpa BQ)<br>_PKM Pemberi Imunisasi DPT-Hb-Hib 4_ → `Immunization.performer.actor.reference` (37, tanpa BQ)<br>_Status Imunisasi DPT-Hb-Hib 4_ → `Immunization.reasonCode[i].coding` (39, tanpa BQ)<br>_Tanggal Imunisasi MR 2_ → `Immunization.occurrenceDateTime` (57, tanpa BQ)<br>_Tanggal Input MR 2_ → `Immunization.recorded` (58, tanpa BQ) |
| 3 | 60–89 | Immunization | VG03 | – | _Pos Imunisasi MR 2_ → `Immunization.location` (66, tanpa BQ)<br>_PKM Pemberi Imunisasi MR 2_ → `Immunization.performer.actor.reference` (67, tanpa BQ)<br>_Status Imunisasi MR 2_ → `Immunization.reasonCode[i].coding` (69, tanpa BQ)<br>_Tanggal Imunisasi PCV 3_ → `Immunization.occurrenceDateTime` (87, tanpa BQ)<br>_Tanggal Input PCV 3_ → `Immunization.recorded` (88, tanpa BQ) |
| 4 | 90–113 | Immunization | VG152 | – | _Pos Imunisasi PCV 3_ → `Immunization.location` (96, tanpa BQ)<br>_PKM Pemberi Imunisasi PCV 3_ → `Immunization.performer.actor.reference` (97, tanpa BQ)<br>_Status Imunisasi PCV 3_ → `Immunization.reasonCode[i].coding` (99, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Immunization | 3 |
| Patient | 1 |
| **Total** | **4** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 21 | Immunization | `Immunization.vaccineCode.coding` | VG45 |  |  |
| 2 | 24 | Immunization | `Immunization.vaccineCode.coding` | VG17 |  |  |
| 3 | 27 | Immunization | `Immunization.vaccineCode.coding` | VG107 |  |  |
| 4 | 30 | Immunization | `Immunization.vaccineCode.coding` | 198 |  |  |
| 5 | 60 | Immunization | `Immunization.vaccineCode.coding` | VG03 |  |  |
| 6 | 90 | Immunization | `Immunization.vaccineCode.coding` | VG152 |  |  |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
|  | 6 |
| **Total** | **6** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 12 | – | Nama Orang Tua | – | `` |
| 13 | – | Kelurahan atau Desa | – | `` |
| 14 | – | Kode Puskesmas | – | `` |
| 15 | – | Puskesmas | Organization | `Patient.identifier.use` |
| 50 | – | Sumber Pencatatan Imunisasi DPT-Hb-Hib 4 | – | `` |
| 80 | – | Sumber Pencatatan Imunisasi MR 2 | – | `` |
| 110 | – | Sumber Pencatatan Imunisasi PCV 3 | – | `` |
