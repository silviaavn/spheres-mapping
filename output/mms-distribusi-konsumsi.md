# Output Form: MMS - Pemantauan Distribusi dan Konsumsi

Sumber: `mapping/phdt-data-dictionary-mms-distribusi-konsumsi.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-mms-distribusi-konsumsi.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 22 |
| Code (`jumlah code` = 1) | 58 |
| Code unik (code + CodeSystem) | 52 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 30 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–5 | PractitionerRole | – | – | _Siapa yang melakukan entry data_ → `PractitionerRole.active` (2, tanpa BQ) |
| 2 | 6–13 | Practitioner | – | – | _Nama Lengkap Kader_ → `Practitioner.name.text` (6, tanpa BQ)<br>_ID Kader_ → `Practitioner.identifier` (7, tanpa BQ)<br>_ID SID staff yang melakukan entry data_ → `Practitioner.identifier` (8, tanpa BQ)<br>_ID SID field staff yang mengumpulkan form_ → `Practitioner.identifier` (9, tanpa BQ)<br>_Nomor SID ID_ → `Practitioner.identifier` (13, tanpa BQ) |
| 3 | 14–14 | Patient | – | – | _Nama Lengkap Ibu_ → `Patient.name.text` (14, tanpa BQ)<br>_Tulis Nomor Induk Kependudukan (NIK)_ → `Patient.identifier.use` (31, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (51, tanpa BQ)<br>_Asal Provinsi_ → `Patient.address.extension.url` (64, tanpa BQ)<br>_Asal Kabupaten_ → `Patient.address.extension.url` (69, tanpa BQ)<br>_Asal Kecamatan_ → `Patient.address.extension.url` (72, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.url` (79, tanpa BQ)<br>_Nama Dusun_ → `Patient.address.extension.url` (82, tanpa BQ)<br>_Nama Jalan dan Nomor Rumah_ → `Patient.address.line` (103, tanpa BQ)<br>_RW_ → `Patient.address.extension.url` (105, tanpa BQ)<br>_RT_ → `Patient.address.extension.url` (108, tanpa BQ) |
| 4 | 15–18 | RelatedPerson | – | – | _Nama Lengkap Suami_ → `RelatedPerson.patient` (15, tanpa BQ) |
| 5 | 19–30 | Observation | SP000402 | Kepemilikan Nomor Induk Kependudukan | _Apakah Ibu punya NIK_ → `Observation.valueBoolean` (22, tanpa BQ) |
| 6 | 34–47 | Observation | SP000403 | Alasan Tidak Ada Nomor Induk Kependudukan | _Pilih alasan tidak mempunyai Nomor Induk Kependudukan (NIK)_ → `Observation.valueCodeableConcept.coding` (37, tanpa BQ) |
| 7 | 52–63 | Observation | 424144002.0 | Current chronological age | _Usia_ → `Observation.valueQuantity.value` (55, tanpa BQ) |
| 8 | 89–102 | Observation | SP000519 | Tipe Intervensi Puskesmas | _Tipe intervensi puskesmas_ → `Observation.valueCodeableConcept.coding` (92, tanpa BQ) |
| 9 | 113–125 | Observation | 280147009.0 | Type of activity | _Jenis kegiatan pemantauan yang dilakukan_ → `Observation.valueCodeableConcept.coding` (116, tanpa BQ) |
| 10 | 126–136 | Observation | 280147009.0 | Type of activity | _Apakah pemantauan kalsium dilakukan?_ → `Observation.valueBoolean` (129, tanpa BQ) |
| 11 | 137–149 | Observation | SP000469 | Jenis Pemantauan Kalsium | _Jenis pemantauan kalsium yang dilakukan_ → `Observation.valueCodeableConcept.coding` (140, tanpa BQ) |
| 12 | 150–241 | Medication | 92006039.0 | MMS Multivitamin Ibu Hamil Tablet Salut Selaput | _MMS_ → `Medication.id` (150, tanpa BQ)<br>_Kalsium_ → `Medication.identifier` (231, tanpa BQ) |
| 13 | 242–267 | MedicationRequest | 93022220.0 | Calcium Lactate 500 mg Tablet (MERSIFARMA TIRMAKU MERCUSANA) | _Tanggal pemberian blister_ → `MedicationRequest.contained.resourceType` (242, tanpa BQ)<br>_{tanggal pemberian kalsium}_ → `MedicationRequest.authoredOn` (262, tanpa BQ) |
| 14 | 268–289 | MedicationDispense | 93022220.0 | Calcium Lactate 500 mg Tablet (MERSIFARMA TIRMAKU MERCUSANA) | – |
| 15 | 292–304 | MedicationRequest | – | – | _Id Blister Calcium 1_ → `MedicationRequest.contained.batch.lotNumber` (292, tanpa BQ)<br>_Id Blister Calcium 1 (Manual entry)_ → `MedicationRequest.contained.batch.lotNumber` (293, tanpa BQ)<br>_Id Blister Calcium 1 (Manual entry kedua kali)_ → `MedicationRequest.contained.batch.lotNumber` (294, tanpa BQ)<br>_Id Blister Calcium 2_ → `MedicationRequest.contained.batch.lotNumber` (297, tanpa BQ)<br>_Id Blister Calcium 2 (Manual entry)_ → `MedicationRequest.contained.batch.lotNumber` (298, tanpa BQ)<br>_Id Blister Calcium 2 (Manual entry kedua kali)_ → `MedicationRequest.contained.batch.lotNumber` (299, tanpa BQ)<br>_Id Blister Calcium 3_ → `MedicationRequest.contained.batch.lotNumber` (302, tanpa BQ)<br>_Id Blister Calcium 3 (Manual entry)_ → `MedicationRequest.contained.batch.lotNumber` (303, tanpa BQ)<br>_Id Blister Calcium 3 (Manual entry kedua kali)_ → `MedicationRequest.contained.batch.lotNumber` (304, tanpa BQ) |
| 16 | 305–308 | MedicationStatement | – | – | _Tanggal pemberian kalsium pertama kali_ → `MedicationStatement.status` (305, tanpa BQ)<br>_Jumlah kalsium yang seharusnya sudah dikonsumsi_ → `` (308, tanpa BQ) |
| 17 | 325–336 | Observation | SP000640 | Konsumsi kalsium setiap hari | _Apakah ibu mengonsumsi kalsium setiap hari?_ → `Observation.valueBoolean` (328, tanpa BQ) |
| 18 | 337–355 | Observation | SP000642 | Alasan tidak mengonsumsi kalsium | _Jika tidak, apa alasannya?_ → `Observation.valueCodeableConcept.coding` (340, tanpa BQ) |
| 19 | 357–360 | MedicationStatement | – | – | _Tanggal Pemberian MMS Kemasan Botol*_ → `MedicationStatement.effectivePeriod.start` (357, tanpa BQ)<br>_Id Botol MMS_ → `MedicationStatement.medicationReference` (360, tanpa BQ) |
| 20 | 375–392 | MedicationDispense | – | – | _Jumlah tablet MMS yang sudah dikonsumsi berdasarkan kartu pemantauan atau pengakuan ibu hamil_ → `MedicationDispense.quantity.value` (375, tanpa BQ)<br>_Id Blister MMS_ → `MedicationDispense.status` (386, tanpa BQ)<br>_Tanggal pemberian MMS Kemasan Blister pertama kali_ → `MedicationStatement.effectiveDateTime` (392, tanpa BQ) |
| 21 | 393–404 | MedicationStatement | – | – | _Jumlah tablet MMS yang seharusnya dikonsumsi_ → `MedicationStatement.dosage.doseAndRate.doseQuantity.value` (397, tanpa BQ)<br>_Jumlah tablet MMS yang sudah dikonsumsi_ → `MedicationStatement.dosage.doseAndRate.doseQuantity.value` (403, tanpa BQ) |
| 22 | 455–536 | Observation | SP000482 | Skrinning Preeklampsia | _Apakah sudah dilakukan skrining preeklampsia pada ibu hamil usia 17-19 minggu?_ → `Observation.valueBoolean` (458, tanpa BQ)<br>_Skrining Preeklampsia (UK <20 Minggu)_ → `Observation.component.code.coding` (460, tanpa BQ)<br>_Kesimpulan Skrining Preeklampsia_ → `Observation.interpretation.coding` (527, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 10 |
| MedicationStatement | 3 |
| MedicationRequest | 2 |
| MedicationDispense | 2 |
| PractitionerRole | 1 |
| Practitioner | 1 |
| Patient | 1 |
| RelatedPerson | 1 |
| Medication | 1 |
| **Total** | **22** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 3 | PractitionerRole | `PractitionerRole.code.coding` | EHA000001 | Kader/ Komunitas | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 2 | 4 | PractitionerRole | `PractitionerRole.code.coding` | SP000396 | Data entry staff | http://terminology.kemkes.go.id/sp |
| 3 | 5 | PractitionerRole | `PractitionerRole.code.coding` | SP000397 | Field/call center staff | http://terminology.kemkes.go.id/sp |
| 4 | 21 | Observation | `Observation.code.coding` | SP000402 | Kepemilikan Nomor Induk Kependudukan | http://terminology.kemkes.go.id/sp |
| 5 | 36 | Observation | `Observation.code.coding` | SP000403 | Alasan Tidak Ada Nomor Induk Kependudukan | http://terminology.kemkes.go.id/sp |
| 6 | 37 | Observation | `Observation.valueCodeableConcept.coding` | SP000404 | Tidak Punya Kartu Tanda Penduduk | http://terminology.kemkes.go.id/sp |
| 7 | 38 | Observation | `Observation.valueCodeableConcept.coding` | SP000405 | Tidak Membawa Kartu Tanda Penduduk | http://terminology.kemkes.go.id/sp |
| 8 | 39 | Observation | `Observation.valueCodeableConcept.coding` | SP000406 | Kartu Tanda Penduduk Hilang | http://terminology.kemkes.go.id/sp |
| 9 | 40 | Observation | `Observation.valueCodeableConcept.coding` | 397644002.0 | Right to privacy maintained | http://snomed.info/sct |
| 10 | 54 | Observation | `Observation.code.coding` | 424144002.0 | Current chronological age | http://snomed.info/sct |
| 11 | 91 | Observation | `Observation.code.coding` | SP000519 | Tipe Intervensi Puskesmas | http://terminology.kemkes.go.id/sp |
| 12 | 92 | Observation | `Observation.valueCodeableConcept.coding` | SP000520 | Blister Digital | http://terminology.kemkes.go.id/sp |
| 13 | 93 | Observation | `Observation.valueCodeableConcept.coding` | SP000521 | Blister Non Digital | http://terminology.kemkes.go.id/sp |
| 14 | 94 | Observation | `Observation.valueCodeableConcept.coding` | SP000522 | Botol Digital | http://terminology.kemkes.go.id/sp |
| 15 | 95 | Observation | `Observation.valueCodeableConcept.coding` | SP000523 | Botol Non Digital | http://terminology.kemkes.go.id/sp |
| 16 | 115 | Observation | `Observation.code.coding` | 280147009.0 | Type of activity | http://snomed.info/sct |
| 17 | 116 | Observation | `Observation.valueCodeableConcept.coding` | SP000445 | Pemantauan Distribusi MMS Botol | http://terminology.kemkes.go.id/sp |
| 18 | 117 | Observation | `Observation.valueCodeableConcept.coding` | SP000446 | Pemantauan Distribusi MMS Blister | http://terminology.kemkes.go.id/sp |
| 19 | 118 | Observation | `Observation.valueCodeableConcept.coding` | SP000447 | Pemantauan Konsumsi MMS Botol | http://terminology.kemkes.go.id/sp |
| 20 | 119 | Observation | `Observation.valueCodeableConcept.coding` | SP000448 | Pemantauan Konsumsi MMS Blister | http://terminology.kemkes.go.id/sp |
| 21 | 128 | Observation | `Observation.code.coding` | 280147009.0 | Type of activity | http://snomed.info/sct |
| 22 | 139 | Observation | `Observation.code.coding` | SP000469 | Jenis Pemantauan Kalsium | http://terminology.kemkes.go.id/sp |
| 23 | 140 | Observation | `Observation.valueCodeableConcept.coding` | SP000470 | Pemantauan Distribusi Kalsium | http://terminology.kemkes.go.id/sp |
| 24 | 141 | Observation | `Observation.valueCodeableConcept.coding` | SP000471 | Pemantauan Konsumsi Kalsium | http://terminology.kemkes.go.id/sp |
| 25 | 151 | Medication | `Medication.code` | 92006039.0 | MMS Multivitamin Ibu Hamil Tablet Salut Selaput | http://sys-ids.kemkes.go.id/kf |
| 26 | 233 | Medication | `Medication.code.coding` | 93022220.0 | Calcium Lactate 500 mg Tablet (MERSIFARMA TIRMAKU MERCUSANA) | http://sys-ids.kemkes.go.id/kf |
| 27 | 245 | MedicationRequest | `MedicationRequest.contained.code.coding` | 93022220.0 | Calcium Lactate 500 mg Tablet (MERSIFARMA TIRMAKU MERCUSANA) | http://sys-ids.kemkes.go.id/kf |
| 28 | 271 | MedicationDispense | `MedicationDispense.contained.code.coding` | 93022220.0 | Calcium Lactate 500 mg Tablet (MERSIFARMA TIRMAKU MERCUSANA) | http://sys-ids.kemkes.go.id/kf |
| 29 | 327 | Observation | `Observation.code.coding` | SP000640 | Konsumsi kalsium setiap hari | http://terminology.kemkes.go.id/sp |
| 30 | 339 | Observation | `Observation.code.coding` | SP000642 | Alasan tidak mengonsumsi kalsium | http://terminology.kemkes.go.id/sp |
| 31 | 340 | Observation | `Observation.valueCodeableConcept.coding` | 1303576005.0 | Forgets to take medication | http://snomed.info/sct |
| 32 | 341 | Observation | `Observation.valueCodeableConcept.coding` | 182844005.0 | Drug not taken - dislike taste | http://snomed.info/sct |
| 33 | 342 | Observation | `Observation.valueCodeableConcept.coding` | SP000636 | Malas mengonsumsi | http://terminology.kemkes.go.id/sp |
| 34 | 343 | Observation | `Observation.valueCodeableConcept.coding` | SP000637 | Minum vitamin lain | http://terminology.kemkes.go.id/sp |
| 35 | 344 | Observation | `Observation.valueCodeableConcept.coding` | 275929009.0 | Tablets too large to swallow | http://snomed.info/sct |
| 36 | 345 | Observation | `Observation.valueCodeableConcept.coding` | 182856006.0 | Drug not available due to being out of stock | http://snomed.info/sct |
| 37 | 346 | Observation | `Observation.valueCodeableConcept.coding` | 419219000.0 | Nausea and vomiting caused by drug | http://snomed.info/sct |
| 38 | 347 | Observation | `Observation.valueCodeableConcept.coding` | SP000639 | Bau tidak enak | http://terminology.kemkes.go.id/sp |
| 39 | 348 | Observation | `Observation.valueCodeableConcept.coding` | 182863006.0 | Drug not taken - dislike form |  |
| 40 | 349 | Observation | `Observation.valueCodeableConcept.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 41 | 438 | MedicationStatement | `MedicationStatement.statusReason.coding` | SP000636 | Malas mengonsumsi | http://terminology.kemkes.go.id/sp |
| 42 | 439 | MedicationStatement | `MedicationStatement.statusReason.coding` | SP000637 | Minum vitamin lain | http://terminology.kemkes.go.id/sp |
| 43 | 440 | MedicationStatement | `MedicationStatement.statusReason.coding` | SP000638 | Warna MMS berubah | http://terminology.kemkes.go.id/sp |
| 44 | 443 | MedicationStatement | `MedicationStatement.statusReason.coding` | SP000639 | Bau tidak enak | http://terminology.kemkes.go.id/sp |
| 45 | 446 | MedicationStatement | `MedicationStatement.medicationCodeableConcept.coding` | SP000370 | Multiple Micronutrient Supplement | http://terminology.kemkes.go.id/sp |
| 46 | 457 | Observation | `Observation.code.coding` | SP000482 | Skrinning Preeklampsia | http://terminology.kemkes.go.id/sp |
| 47 | 469 | Observation | `Observation.component.code.coding` | 102877006.0 | Nulliparous |  |
| 48 | 475 | Observation | `Observation.component.code.coding` | 105651000119100.0 | Past pregnancy history of pre-eclampsia |  |
| 49 | 478 | Observation | `Observation.component.code.coding` | 700190003.0 | Family history of pre-eclampsia | http://snomed.info/sct |
| 50 | 487 | Observation | `Observation.component.code.coding` | 16356006.0 | Multiple pregnancy | http://snomed.info/sct |
| 51 | 490 | Observation | `Observation.component.code.coding` | 11687002.0 | Gestational diabetes mellitus | http://snomed.info/sct |
| 52 | 493 | Observation | `Observation.component.code.coding` | 8762007.0 | Chronic hypertension in obstetric context | http://snomed.info/sct |
| 53 | 496 | Observation | `Observation.component.code.coding` | 90708001.0 | Kidney disease | http://snomed.info/sct |
| 54 | 499 | Observation | `Observation.component.code.coding` | 85828009.0 | Autoimmune disease | http://snomed.info/sct |
| 55 | 502 | Observation | `Observation.component.code.coding` | 55464009.0 | Systemic lupus erythematosus | http://snomed.info/sct |
| 56 | 511 | Observation | `Observation.component.code.coding` | 167275009.0 | Urine protein test = + | http://snomed.info/sct |
| 57 | 527 | Observation | `Observation.interpretation.coding` | 1303255001.0 | Medium risk pregnancy | http://snomed.info/sct |
| 58 | 536 | Observation | `Observation.interpretation.coding` | 47200007.0 | High risk pregnancy | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://terminology.kemkes.go.id/sp | 30 |
| http://snomed.info/sct | 20 |
| http://sys-ids.kemkes.go.id/kf | 4 |
|  | 3 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 1 |
| **Total** | **58** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 10 | – | Tangga visit | – | `` |
| 11 | – | Tanggal Entry | – | `` |
| 12 | – | Jenis ID Tambahan | – | `` |
| 48 | – | Tanggal lahir ibu diketahui | – | `` |
| 75 | – | Asal Puskesmas | Organization | `Organization.active` |
| 85 | – | Posyandu | Organization | `Organization.active` |
| 111 | – | Tautan GPS rumah | – | `` |
| 112 | – | Foto rumah | – | `` |
| 290 | – | Apakah barcode pada kemasan kalsium 1 bisa discan? | – | `` |
| 295 | – | Apakah barcode pada kemasan kalsium 2 bisa discan? | – | `` |
| 300 | – | Apakah barcode pada kemasan kalsium 3 bisa discan? | – | `` |
| 309 | – | Tanggal pemberian kalsium terakhir | – | `` |
| 310 | – | Apakah QRCode pada kemasan kalsium 1 bisa discan? | – | `` |
| 312 | – | Id Blister Kalsium 1 | – | `` |
| 313 | – | Jumlah kalsium yang sudah dikonsumsi pada blister kalsium 1 | – | `` |
| 314 | – | Apakah QRCode pada kemasan kalsium 2 bisa discan? | – | `` |
| 316 | – | Id Blister Kalsium 2 | – | `` |
| 317 | – | Jumlah kalsium yang sudah dikonsumsi pada blister kalsium 2 | – | `` |
| 318 | – | Apakah QRCode pada kemasan kalsium 3 bisa discan? | – | `` |
| 320 | – | Id Blister Kalsium 3 | – | `` |
| 321 | – | Jumlah kalsium yang sudah dikonsumsi pada blister kalsium 3 | – | `` |
| 322 | – | Jumlah kalsium yang harus konsumsi pada kemasan blister terakhir | – | `` |
| 323 | – | Jumlah konsumsi kalsium pada kemasan blister terakhir | – | `` |
| 324 | – | Jumlah tablet kalsium yang sudah dikonsumsi dari blister pertama hingga blister terakhir | – | `` |
| 356 | – | Foto calcium | – | `` |
| 358 | – | Apakah barcode pada kemasan MMS bisa discan? | – | `` |
| 361 | – | Berat kemasan botol | – | `` |
| 362 | – | Apakah barcode pada kemasan MMS bisa discan? | – | `` |
| 364 | – | Id Blister MMS | – | `` |
| 365 | – | Id Blister MMS (Manual entry) | – | `` |
| 366 | – | Id Blister MMS (Manual entry kedua kali) | – | `` |
| 367 | – | Apakah barcode pada kemasan MMS bisa discan? | – | `` |
| 369 | – | Id Botol MMS | – | `` |
| 370 | – | Id Botol MMS (Manual entry) | – | `` |
| 371 | – | Id Botol MMS (Manual entry kedua kali) | – | `` |
| 372 | – | Tanggal pemberian MMS Kemasan Botol | – | `` |
| 373 | – | Jumlah tablet MMS yang seharusnya dikonsumsi | – | `` |
| 374 | – | Timbang berat MMS saat kunjungan | – | `` |
| 378 | – | Jumlah sisa tablet dalam botol berdasarkan hasil penimbangan | – | `` |
| 379 | – | Apakah ibu mengonsumsi MMS setiap hari? | – | `` |
| 381 | – | Foto botol MMS beserta hasil timbangan | – | `` |
| 382 | – | Foto botol MMS | – | `` |
| 383 | – | Foto kartu pemantauan | – | `` |
| 384 | – | Apakah barcode pada kemasan MMS bisa discan? | – | `` |
| 390 | – | Id Blister MMS (Manual entry) | – | `` |
| 391 | – | Id Blister MMS (Manual entry kedua kali) | – | `` |
| 405 | – | Tanggal pemberian MMS Kemasan Blister terakhir | MedicationDispense | `` |
| 406 | – | Jumlah MMS yang harus konsumsi pada kemasan blister terakhir | MedicationStatement | `MedicationStatement.identifier` |
| 413 | – | Jumlah konsumsi MMS pada kemasan blister terakhir | MedicationStatement | `MedicationStatement.identifier` |
| 420 | – | Jumlah sisa tablet MMS pada blister terakhir | MedicationStatement | `MedicationStatement.identifier` |
| 433 | – | Apakah ibu mengonsumsi MMS setiap hari? | MedicationStatement | `MedicationStatement.category.coding` |
| 436 | – | Jika tidak, apa alasannya? | MedicationStatement | `MedicationStatement.statusReason.coding` |
| 453 | – | Foto blister | – | `` |
| 454 | – | Foto kartu pemantauan | – | `` |
