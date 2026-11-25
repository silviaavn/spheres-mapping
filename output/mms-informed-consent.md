# Output Form: MMS - Informed Consent

Sumber: `mapping/phdt-data-dictionary-mms-informed-consent.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-mms-informed-consent.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 8 |
| Code (`jumlah code` = 1) | 5 |
| Code unik (code + CodeSystem) | 5 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 0 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–2 | Practitioner | – | – | _ID Field Staff SID_ → `Practitioner.identifier` (2, tanpa BQ) |
| 2 | 3–11 | Consent | – | – | _Tanggal Persetujuan/Enrollment_ → `Consent.dateTime` (3, tanpa BQ)<br>_Jenis Informed Consent_ → `Consent.status` (4, tanpa BQ) |
| 3 | 12–12 | Patient | – | – | _Nama lengkap responden_ → `Patient.name` (12, tanpa BQ) |
| 4 | 37–66 | QuestionnaireResponse | – | – | _Apakah responden bersedia untuk dihubungi dan dikunjungi?_ → `QuestionnaireResponse.item.linkId` (47, tanpa BQ)<br>_Apakah Anda setuju untuk ikut serta dalam program ini?_ → `QuestionnaireResponse.item.linkId` (51, tanpa BQ)<br>_Apakah Anda setuju untuk berkomitmen mengkonsumsi MMS dan Kalsium Secara rutin?_ → `QuestionnaireResponse.item.linkId` (55, tanpa BQ)<br>_Apakah anda setuju untuk pemeriksaan sampel darah, untuk pemeriksaan kepatuhan konsumsi MMS dan status kesehatan?_ → `QuestionnaireResponse.item.linkId` (59, tanpa BQ)<br>_Apakah keluarga mendapat penjelasan IC dan menandatangani IC tersebut?_ → `QuestionnaireResponse.item.linkId` (63, tanpa BQ) |
| 5 | 67–68 | Consent | – | – | _Foto lembar persetujuan setelah penjelasan (PSP)_ → `Consent.sourceAttachment` (67, tanpa BQ)<br>_Foto lembar pernyataan persetujuan (Tanda Tangan)_ → `Consent.sourceAttachment` (68, tanpa BQ) |
| 6 | 69–81 | Observation | 313334002.0 | Blood sample taken | _Jenis pengambilan sampel darah_ → `Observation.valueCodeableConcept.coding` (72, tanpa BQ) |
| 7 | 82–93 | Observation | 3157-5 | Volume of Blood | _Volume sampel darah_ → `Observation.valueQuantity.value` (85, tanpa BQ) |
| 8 | 94–94 | Consent | – | – | _Foto lembar persejutuan pengambilan sub-sampel darah_ → `Consent.sourceAttachment` (94, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Consent | 3 |
| Observation | 2 |
| Practitioner | 1 |
| Patient | 1 |
| QuestionnaireResponse | 1 |
| **Total** | **8** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 71 | Observation | `Observation.code.coding` | 313334002.0 | Blood sample taken | http://snomed.info/sct |
| 2 | 72 | Observation | `Observation.valueCodeableConcept.coding` | 385652002.0 | Started | http://snomed.info/sct |
| 3 | 73 | Observation | `Observation.valueCodeableConcept.coding` | 399488007.0 | Midline | http://snomed.info/sct |
| 4 | 74 | Observation | `Observation.valueCodeableConcept.coding` | 261782000.0 | End | http://snomed.info/sct |
| 5 | 84 | Observation | `Observation.code.coding` | 3157-5 | Volume of Blood | http://loinc.org |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 4 |
| http://loinc.org | 1 |
| **Total** | **5** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 13 | – | ID Ibu Hamil | – | `` |
| 14 | – | Tanggal lahir ibu diketahui? | – | `` |
| 16 | – | Tanggal lahir | – | `` |
| 17 | – | Usia | – | `` |
| 18 | – | HPHT diketahui | – | `` |
| 20 | – | Tentukan tanggal HPHT | – | `` |
| 21 | – | Hasil USG: Taksiran persalinan | – | `` |
| 22 | – | Usia Kehamilan (KIA/KI) | – | `` |
| 23 | – | Nomor HP | – | `` |
| 25 | – | Tulis nomor HP | – | `` |
| 26 | – | Tulis nomor WA | – | `` |
| 27 | – | Asal Provinsi | – | `` |
| 28 | – | Asal Kabupaten | – | `` |
| 29 | – | Asal Kecamatan | – | `` |
| 30 | – | Asal Puskesmas | – | `` |
| 31 | – | Nama Desa | – | `` |
| 32 | – | Nama Dusun | – | `` |
| 33 | – | Posyandu | – | `` |
| 34 | – | Nama kampung (Gubuk), nama jalan dan nomor rumah (jika ada) | – | `` |
| 35 | – | RW | – | `` |
| 36 | – | RT | – | `` |
