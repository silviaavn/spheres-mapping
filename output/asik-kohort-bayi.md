# Output Form: ASIK - Data Individu Kohort Bayi (Imunisasi)

Sumber: `mapping/phdt-data-dictionary-asik-kohort-bayi.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-asik-kohort-bayi.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 19 |
| Code (`jumlah code` = 1) | 27 |
| Code unik (code + CodeSystem) | 10 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 0 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–11 | Patient | – | – | _NIK Anak_ → `Patient.identifier.value` (4, tanpa BQ)<br>_Nama Anak_ → `Patient.name` (5, tanpa BQ)<br>_NIK Orang Tua_ → `Patient.identifier.value` (11, tanpa BQ) |
| 2 | 18–50 | Immunization | VG45 | – | _Tanggal Imunisasi HB0_ → `Immunization.occurrenceDateTime` (18, tanpa BQ)<br>_Tanggal Input HB0_ → `Immunization.recorded` (19, tanpa BQ)<br>_Pos Imunisasi HB0_ → `Immunization.location` (27, tanpa BQ)<br>_PKM Pemberi Imunisasi HB0_ → `Immunization.performer.actor.reference` (28, tanpa BQ)<br>_Status Imunisasi HB0_ → `Immunization.reasonCode[i].coding` (30, tanpa BQ)<br>_Tanggal Imunisasi BCG 1_ → `Immunization.occurrenceDateTime` (48, tanpa BQ)<br>_Tanggal Input BCG 1_ → `Immunization.recorded` (49, tanpa BQ) |
| 3 | 51–80 | Immunization | VG19 | – | _Pos Imunisasi BCG 1_ → `Immunization.location` (57, tanpa BQ)<br>_PKM Pemberi Imunisasi BCG 1_ → `Immunization.performer.actor.reference` (58, tanpa BQ)<br>_Status Imunisasi BCG 1_ → `Immunization.reasonCode[i].coding` (60, tanpa BQ)<br>_Tanggal Imunisasi POLIO 1_ → `Immunization.occurrenceDateTime` (78, tanpa BQ)<br>_Tanggal Input POLIO 1_ → `Immunization.recorded` (79, tanpa BQ) |
| 4 | 81–110 | Immunization | VG89 | – | _Pos Imunisasi POLIO 1_ → `Immunization.location` (87, tanpa BQ)<br>_PKM Pemberi Imunisasi POLIO 1_ → `Immunization.performer.actor.reference` (88, tanpa BQ)<br>_Status Imunisasi POLIO 1_ → `Immunization.reasonCode[i].coding` (90, tanpa BQ)<br>_Tanggal Imunisasi POLIO 2_ → `Immunization.occurrenceDateTime` (108, tanpa BQ)<br>_Tanggal Input POLIO 2_ → `Immunization.recorded` (109, tanpa BQ) |
| 5 | 111–140 | Immunization | VG89 | – | _Pos Imunisasi POLIO 2_ → `Immunization.location` (117, tanpa BQ)<br>_PKM Pemberi Imunisasi POLIO 2_ → `Immunization.performer.actor.reference` (118, tanpa BQ)<br>_Status Imunisasi POLIO 2_ → `Immunization.reasonCode[i].coding` (120, tanpa BQ)<br>_Tanggal Imunisasi POLIO 3_ → `Immunization.occurrenceDateTime` (138, tanpa BQ)<br>_Tanggal Input POLIO 3_ → `Immunization.recorded` (139, tanpa BQ) |
| 6 | 141–170 | Immunization | VG89 | – | _Pos Imunisasi POLIO 3_ → `Immunization.location` (147, tanpa BQ)<br>_PKM Pemberi Imunisasi POLIO 3_ → `Immunization.performer.actor.reference` (148, tanpa BQ)<br>_Status Imunisasi POLIO 3_ → `Immunization.reasonCode[i].coding` (150, tanpa BQ)<br>_Tanggal Imunisasi POLIO 4_ → `Immunization.occurrenceDateTime` (168, tanpa BQ)<br>_Tanggal Input POLIO 4_ → `Immunization.recorded` (169, tanpa BQ) |
| 7 | 171–200 | Immunization | VG89 | – | _Pos Imunisasi POLIO 4_ → `Immunization.location` (177, tanpa BQ)<br>_PKM Pemberi Imunisasi POLIO 4_ → `Immunization.performer.actor.reference` (178, tanpa BQ)<br>_Status Imunisasi POLIO 4_ → `Immunization.reasonCode[i].coding` (180, tanpa BQ)<br>_Tanggal Imunisasi DPT-Hb-Hib 1_ → `Immunization.occurrenceDateTime` (198, tanpa BQ)<br>_Tanggal Input DPT-Hb-Hib 1_ → `Immunization.recorded` (199, tanpa BQ) |
| 8 | 201–239 | Immunization | VG45 | – | _Pos Imunisasi DPT-Hb-Hib 1_ → `Immunization.location` (216, tanpa BQ)<br>_PKM Pemberi Imunisasi DPT-Hb-Hib 1_ → `Immunization.performer.actor.reference` (217, tanpa BQ)<br>_Status Imunisasi DPT-Hb-Hib 1_ → `Immunization.reasonCode[i].coding` (219, tanpa BQ)<br>_Tanggal Imunisasi DPT-Hb-Hib 2_ → `Immunization.occurrenceDateTime` (237, tanpa BQ)<br>_Tanggal Input DPT-Hb-Hib 2_ → `Immunization.recorded` (238, tanpa BQ) |
| 9 | 240–278 | Immunization | VG45 | – | _Pos Imunisasi DPT-Hb-Hib 2_ → `Immunization.location` (255, tanpa BQ)<br>_PKM Pemberi Imunisasi DPT-Hb-Hib 2_ → `Immunization.performer.actor.reference` (256, tanpa BQ)<br>_Status Imunisasi DPT-Hb-Hib 4_ → `Immunization.reasonCode[i].coding` (258, tanpa BQ)<br>_Tanggal Imunisasi DPT-Hb-Hib 3_ → `Immunization.occurrenceDateTime` (276, tanpa BQ)<br>_Tanggal Input DPT-Hb-Hib 3_ → `Immunization.recorded` (277, tanpa BQ) |
| 10 | 279–317 | Immunization | VG45 | – | _Pos Imunisasi DPT-Hb-Hib 3_ → `Immunization.location` (294, tanpa BQ)<br>_PKM Pemberi Imunisasi DPT-Hb-Hib 3_ → `Immunization.performer.actor.reference` (295, tanpa BQ)<br>_Status Imunisasi DPT-Hb-Hib 3_ → `Immunization.reasonCode[i].coding` (297, tanpa BQ)<br>_Tanggal Imunisasi IPV 1_ → `Immunization.occurrenceDateTime` (315, tanpa BQ)<br>_Tanggal Input IPV 1_ → `Immunization.recorded` (316, tanpa BQ) |
| 11 | 318–347 | Immunization | VG89 | – | _Pos Imunisasi IPV 1_ → `Immunization.location` (324, tanpa BQ)<br>_PKM Pemberi Imunisasi IPV 1_ → `Immunization.performer.actor.reference` (325, tanpa BQ)<br>_Status Imunisasi IPV 1_ → `Immunization.reasonCode[i].coding` (327, tanpa BQ)<br>_Tanggal Imunisasi IPV 2_ → `Immunization.occurrenceDateTime` (345, tanpa BQ)<br>_Tanggal Input IPV 2_ → `Immunization.recorded` (346, tanpa BQ) |
| 12 | 348–377 | Immunization | VG89 | – | _Pos Imunisasi IPV 2_ → `Immunization.location` (354, tanpa BQ)<br>_PKM Pemberi Imunisasi IPV 2_ → `Immunization.performer.actor.reference` (355, tanpa BQ)<br>_Status Imunisasi IPV 2_ → `Immunization.reasonCode[i].coding` (357, tanpa BQ)<br>_Tanggal Imunisasi ROTA 1_ → `Immunization.occurrenceDateTime` (375, tanpa BQ)<br>_Tanggal Input ROTA 1_ → `Immunization.recorded` (376, tanpa BQ) |
| 13 | 378–407 | Immunization | VG122 | – | _Pos Imunisasi ROTA 1_ → `Immunization.location` (384, tanpa BQ)<br>_PKM Pemberi Imunisasi ROTA 1_ → `Immunization.performer.actor.reference` (385, tanpa BQ)<br>_Status Imunisasi ROTA 1_ → `Immunization.reasonCode[i].coding` (387, tanpa BQ)<br>_Tanggal Imunisasi ROTA 2_ → `Immunization.occurrenceDateTime` (405, tanpa BQ)<br>_Tanggal Input ROTA 2_ → `Immunization.recorded` (406, tanpa BQ) |
| 14 | 408–437 | Immunization | VG122 | – | _Pos Imunisasi ROTA 2_ → `Immunization.location` (414, tanpa BQ)<br>_PKM Pemberi Imunisasi ROTA 2_ → `Immunization.performer.actor.reference` (415, tanpa BQ)<br>_Status Imunisasi ROTA 2_ → `Immunization.reasonCode[i].coding` (417, tanpa BQ)<br>_Tanggal Imunisasi ROTA 3_ → `Immunization.occurrenceDateTime` (435, tanpa BQ)<br>_Tanggal Input ROTA 3_ → `Immunization.recorded` (436, tanpa BQ) |
| 15 | 438–467 | Immunization | VG122 | – | _Pos Imunisasi ROTA 3_ → `Immunization.location` (444, tanpa BQ)<br>_PKM Pemberi Imunisasi ROTA 3_ → `Immunization.performer.actor.reference` (445, tanpa BQ)<br>_Status Imunisasi ROTA 3_ → `Immunization.reasonCode[i].coding` (447, tanpa BQ)<br>_Tanggal Imunisasi PCV 1_ → `Immunization.occurrenceDateTime` (465, tanpa BQ)<br>_Tanggal Input PCV 1_ → `Immunization.recorded` (466, tanpa BQ) |
| 16 | 468–497 | Immunization | VG152 | – | _Pos Imunisasi PCV 1_ → `Immunization.location` (474, tanpa BQ)<br>_PKM Pemberi Imunisasi PCV 1_ → `Immunization.performer.actor.reference` (475, tanpa BQ)<br>_Status Imunisasi PCV 1_ → `Immunization.reasonCode[i].coding` (477, tanpa BQ)<br>_Tanggal Imunisasi PCV 2_ → `Immunization.occurrenceDateTime` (495, tanpa BQ)<br>_Tanggal Input PCV 2_ → `Immunization.recorded` (496, tanpa BQ) |
| 17 | 498–527 | Immunization | VG152 | – | _Pos Imunisasi PCV 2_ → `Immunization.location` (504, tanpa BQ)<br>_PKM Pemberi Imunisasi PCV 2_ → `Immunization.performer.actor.reference` (505, tanpa BQ)<br>_Status Imunisasi PCV 2_ → `Immunization.reasonCode[i].coding` (507, tanpa BQ)<br>_Tanggal Imunisasi JE 1_ → `Immunization.occurrenceDateTime` (525, tanpa BQ)<br>_Tanggal Input JE 1_ → `Immunization.recorded` (526, tanpa BQ) |
| 18 | 528–557 | Immunization | VG129 | – | _Pos Imunisasi JE 1_ → `Immunization.location` (534, tanpa BQ)<br>_PKM Pemberi Imunisasi JE 1_ → `Immunization.performer.actor.reference` (535, tanpa BQ)<br>_Status Imunisasi JE 1_ → `Immunization.reasonCode[i].coding` (537, tanpa BQ)<br>_Tanggal Imunisasi MR 1_ → `Immunization.occurrenceDateTime` (555, tanpa BQ)<br>_Tanggal Input MR 1_ → `Immunization.recorded` (556, tanpa BQ) |
| 19 | 558–581 | Immunization | VG03 | – | _Pos Imunisasi MR 1_ → `Immunization.location` (564, tanpa BQ)<br>_PKM Pemberi Imunisasi MR 1_ → `Immunization.performer.actor.reference` (565, tanpa BQ)<br>_Status Imunisasi MR 1_ → `Immunization.reasonCode[i].coding` (567, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Immunization | 18 |
| Patient | 1 |
| **Total** | **19** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 21 | Immunization | `Immunization.vaccineCode.coding` | VG45 |  |  |
| 2 | 51 | Immunization | `Immunization.vaccineCode.coding` | VG19 |  |  |
| 3 | 81 | Immunization | `Immunization.vaccineCode.coding` | VG89 |  |  |
| 4 | 111 | Immunization | `Immunization.vaccineCode.coding` | VG89 |  |  |
| 5 | 141 | Immunization | `Immunization.vaccineCode.coding` | VG89 |  |  |
| 6 | 171 | Immunization | `Immunization.vaccineCode.coding` | VG89 |  |  |
| 7 | 201 | Immunization | `Immunization.vaccineCode.coding` | VG45 |  |  |
| 8 | 204 | Immunization | `Immunization.vaccineCode.coding` | VG17 |  |  |
| 9 | 207 | Immunization | `Immunization.vaccineCode.coding` | VG107 |  |  |
| 10 | 210 | Immunization | `Immunization.vaccineCode.coding` | 198 |  |  |
| 11 | 240 | Immunization | `Immunization.vaccineCode.coding` | VG45 |  |  |
| 12 | 243 | Immunization | `Immunization.vaccineCode.coding` | VG17 |  |  |
| 13 | 246 | Immunization | `Immunization.vaccineCode.coding` | VG107 |  |  |
| 14 | 249 | Immunization | `Immunization.vaccineCode.coding` | 198 |  |  |
| 15 | 279 | Immunization | `Immunization.vaccineCode.coding` | VG45 |  |  |
| 16 | 282 | Immunization | `Immunization.vaccineCode.coding` | VG17 |  |  |
| 17 | 285 | Immunization | `Immunization.vaccineCode.coding` | VG107 |  |  |
| 18 | 288 | Immunization | `Immunization.vaccineCode.coding` | 198 |  |  |
| 19 | 318 | Immunization | `Immunization.vaccineCode.coding` | VG89 |  |  |
| 20 | 348 | Immunization | `Immunization.vaccineCode.coding` | VG89 |  |  |
| 21 | 378 | Immunization | `Immunization.vaccineCode.coding` | VG122 |  |  |
| 22 | 408 | Immunization | `Immunization.vaccineCode.coding` | VG122 |  |  |
| 23 | 438 | Immunization | `Immunization.vaccineCode.coding` | VG122 |  |  |
| 24 | 468 | Immunization | `Immunization.vaccineCode.coding` | VG152 |  |  |
| 25 | 498 | Immunization | `Immunization.vaccineCode.coding` | VG152 |  |  |
| 26 | 528 | Immunization | `Immunization.vaccineCode.coding` | VG129 |  |  |
| 27 | 558 | Immunization | `Immunization.vaccineCode.coding` | VG03 |  |  |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
|  | 27 |
| **Total** | **27** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 6 | – | Tanggal Lahir Anak | – | `` |
| 7 | – | Jenis Kelamin Anak | – | `` |
| 12 | – | Nama Orang Tua | – | `` |
| 13 | – | Kelurahan atau Desa | – | `` |
| 14 | – | Kode Puskesmas | – | `` |
| 15 | – | Puskesmas | Organization | `Patient.identifier.use` |
| 41 | – | Sumber Pencatatan Imunisasi HB0 | – | `` |
| 71 | – | Sumber Pencatatan Imunisasi BCG 1 | – | `` |
| 101 | – | Sumber Pencatatan Imunisasi POLIO 1 | – | `` |
| 131 | – | Sumber Pencatatan Imunisasi POLIO 2 | – | `` |
| 161 | – | Sumber Pencatatan Imunisasi POLIO 3 | – | `` |
| 191 | – | Sumber Pencatatan Imunisasi POLIO 4 | – | `` |
| 230 | – | Sumber Pencatatan Imunisasi DPT-Hb-Hib 1 | – | `` |
| 269 | – | Sumber Pencatatan Imunisasi DPT-Hb-Hib 2 | – | `` |
| 308 | – | Sumber Pencatatan Imunisasi DPT-Hb-Hib 3 | – | `` |
| 338 | – | Sumber Pencatatan Imunisasi IPV 1 | – | `` |
| 368 | – | Sumber Pencatatan Imunisasi IPV 2 | – | `` |
| 398 | – | Sumber Pencatatan Imunisasi ROTA 1 | – | `` |
| 428 | – | Sumber Pencatatan Imunisasi ROTA 2 | – | `` |
| 458 | – | Sumber Pencatatan Imunisasi ROTA 3 | – | `` |
| 488 | – | Sumber Pencatatan Imunisasi PCV 1 | – | `` |
| 518 | – | Sumber Pencatatan Imunisasi PCV 2 | – | `` |
| 548 | – | Sumber Pencatatan Imunisasi JE 1 | – | `` |
| 578 | – | Sumber Pencatatan Imunisasi MR 1 | – | `` |
| 585 | – | Tanggal IDL 1 | – | `` |
| 586 | – | Tanggal Input IDL 1 | – | `` |
| 587 | – | Pos IDL 1 | – | `` |
| 588 | – | PKM Pembentuk IDL 1 | – | `` |
| 589 | – | Status IDL 1 | – | `` |
| 593 | – | Sumber Pencatatan IDL 1 | – | `` |
