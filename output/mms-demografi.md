# Output Form: MMS - Survei Demografi (Listing Responden)

Sumber: `mapping/phdt-data-dictionary-mms-demografi.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-mms-demografi.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 12 |
| Code (`jumlah code` = 1) | 20 |
| Code unik (code + CodeSystem) | 19 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 14 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–6 | PractitionerRole | – | – | _Siapa yang melakukan entry data?_ → `PractitionerRole.active` (2, tanpa BQ)<br>_ID SID staff yang melakukan entry data_ → `PractitionerRole.identifier` (5, tanpa BQ)<br>_ID SID field staff yang mengumpulkan form_ → `PractitionerRole.identifier` (6, tanpa BQ) |
| 2 | 7–24 | Encounter | – | – | _Tanggal entry_ → `Encounter.episodeOfCare.reference` (7, tanpa BQ) |
| 3 | 25–31 | Condition | – | – | – |
| 4 | 43–58 | DocumentReference | – | – | _Nama File_ → `DocumentReference.identifier` (43, tanpa BQ) |
| 5 | 59–64 | Patient | – | – | _Nama Lengkap Ibu_ → `Patient.name.text` (59, tanpa BQ)<br>_Tulis Nomor Induk Kependudukan (NIK)_ → `Patient.identifier.value` (64, tanpa BQ)<br>_Tanggal lahir_ → `Patient.birthDate` (83, tanpa BQ)<br>_Asal Provinsi_ → `Patient.address.extension.url` (110, tanpa BQ)<br>_Asal Kabupaten_ → `Patient.address.extension.url` (113, tanpa BQ)<br>_Asal Kecamatan_ → `Patient.address.extension.url` (116, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.url` (123, tanpa BQ)<br>_Nama Dusun_ → `Patient.address.extension.url` (126, tanpa BQ)<br>_Posyandu_ → `Patient.managingOrganization.reference` (129, tanpa BQ)<br>_Nama jalan dan nomor rumah (jika ada)_ → `Patient.address.line` (163, tanpa BQ)<br>_RW_ → `Patient.address.extension.url` (164, tanpa BQ)<br>_RT_ → `Patient.address.extension.url` (167, tanpa BQ)<br>_Tulis nomor HP_ → `Patient.telecom` (172, tanpa BQ) |
| 6 | 65–78 | Observation | SP000403 | Alasan Tidak Ada Nomor Induk Kependudukan | _Pilih alasan tidak mempunyai Nomor Induk Kependudukan (NIK)_ → `Observation.valueCodeableConcept.coding` (68, tanpa BQ) |
| 7 | 79–80 | RelatedPerson | – | – | _Nama Lengkap Suami_ → `RelatedPerson.patient.reference` (79, tanpa BQ) |
| 8 | 84–95 | Observation | 424144002 | Current chronological age | _Usia_ → `Observation.valueQuantity.value` (87, tanpa BQ) |
| 9 | 98–109 | Observation | 8665-2 | Last menstrual period start date | _Tanggal HPHT_ → `Observation.valueDateTime` (102, tanpa BQ) |
| 10 | 149–162 | Observation | SP000519 | Tipe Intervensi Puskesmas | _Tipe Intervensi Puskesmas_ → `Observation.valueCodeableConcept.coding` (152, tanpa BQ) |
| 11 | 175–179 | RelatedPerson | – | – | _Nomor HP Keluarga/Lainnya_ → `RelatedPerson.telecom` (175, tanpa BQ) |
| 12 | 180–193 | Observation | 734005006 | Telephone number | _Bila tidak ada nomor HP, sebutkan alasan_ → `Observation.valueCodeableConcept.coding` (183, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 5 |
| RelatedPerson | 2 |
| PractitionerRole | 1 |
| Encounter | 1 |
| Condition | 1 |
| DocumentReference | 1 |
| Patient | 1 |
| **Total** | **12** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 3 | PractitionerRole | `PractitionerRole.code.coding` | SP000397 | Field staff | http://terminology.kemkes.go.id/sp |
| 2 | 4 | PractitionerRole | `PractitionerRole.code.coding` | SP000396 | Data entry staff | http://terminology.kemkes.go.id/sp |
| 3 | 67 | Observation | `Observation.code.coding` | SP000403 | Alasan Tidak Ada Nomor Induk Kependudukan | http://terminology.kemkes.go.id/sp |
| 4 | 68 | Observation | `Observation.valueCodeableConcept.coding` | SP000404 | Tidak Punya Kartu Tanda Penduduk | http://terminology.kemkes.go.id/sp |
| 5 | 69 | Observation | `Observation.valueCodeableConcept.coding` | SP000405 | Tidak Membawa Kartu Tanda Penduduk | http://terminology.kemkes.go.id/sp |
| 6 | 70 | Observation | `Observation.valueCodeableConcept.coding` | SP000406 | Kartu Tanda Penduduk Hilang | http://terminology.kemkes.go.id/sp |
| 7 | 71 | Observation | `Observation.valueCodeableConcept.coding` | 397644002 | Right to privacy maintained | http://snomed.info/sct |
| 8 | 86 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 9 | 100 | Observation | `Observation.code.coding` | 8665-2 | Last menstrual period start date | http://loinc.org |
| 10 | 101 | Observation | `Observation.code.coding` | ANC.B6.DE14 | Last menstrual period (LMP) date | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 11 | 151 | Observation | `Observation.code.coding` | SP000519 | Tipe Intervensi Puskesmas | http://terminology.kemkes.go.id/sp |
| 12 | 152 | Observation | `Observation.valueCodeableConcept.coding` | SP000520 | Blister Digital | http://terminology.kemkes.go.id/sp |
| 13 | 153 | Observation | `Observation.valueCodeableConcept.coding` | SP000521 | Blister Non Digital | http://terminology.kemkes.go.id/sp |
| 14 | 154 | Observation | `Observation.valueCodeableConcept.coding` | SP000522 | Botol Digital | http://terminology.kemkes.go.id/sp |
| 15 | 155 | Observation | `Observation.valueCodeableConcept.coding` | SP000523 | Botol Non Digital | http://terminology.kemkes.go.id/sp |
| 16 | 182 | Observation | `Observation.code.coding` | 734005006 | Telephone number | http://snomed.info/sct |
| 17 | 183 | Observation | `Observation.valueCodeableConcept.coding` | SP000516 | Tidak punya HP | http://terminology.kemkes.go.id/sp |
| 18 | 184 | Observation | `Observation.valueCodeableConcept.coding` | SP000517 | HP hilang | http://terminology.kemkes.go.id/sp |
| 19 | 185 | Observation | `Observation.valueCodeableConcept.coding` | 397644002 | Right to privacy maintained | http://snomed.info/sct |
| 20 | 186 | Observation | `Observation.valueCodeableConcept.coding` | SP000518 | Lupa nomor HP | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://terminology.kemkes.go.id/sp | 14 |
| http://snomed.info/sct | 4 |
| http://loinc.org | 1 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 1 |
| **Total** | **20** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 60 | – | Apakah mempunyai Nomor Induk Kependudukan (NIK) | – | `` |
| 81 | – | Tanggal lahir ibu diketahui? | – | `` |
| 96 | – | HPHT diketahui | – | `` |
| 119 | – | Asal Puskesmas | Organization | `Organization.active` |
| 170 | – | Nomor HP | – | `` |
