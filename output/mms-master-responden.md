# Output Form: MMS - Master Database Responden

Sumber: `mapping/phdt-data-dictionary-mms-master-responden.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-mms-master-responden.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 16 |
| Code (`jumlah code` = 1) | 33 |
| Code unik (code + CodeSystem) | 27 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 20 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–4 | PractitionerRole | – | – | _Siapa yang melakukan entry data_ → `PractitionerRole.active` (2, tanpa BQ) |
| 2 | 5–6 | Practitioner | – | – | _ID SID staff yang melakukan entry data_ → `Practitioner.identifier` (5, tanpa BQ)<br>_ID SID field staff yang mengumpulkan form_ → `Practitioner.identifier` (6, tanpa BQ) |
| 3 | 8–9 | Patient | – | – | _Nomor SID ID_ → `Patient.identifier` (8, tanpa BQ)<br>_Nama Lengkap Ibu_ → `Patient.name.text` (9, tanpa BQ)<br>_Tulis Nomor Induk Kependudukan (NIK)_ → `Patient.identifier.use` (24, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (44, tanpa BQ)<br>_Tulis nomor HP_ → `Patient.telecom` (78, tanpa BQ)<br>_Alamat Email_ → `Patient.telecom` (96, tanpa BQ)<br>_Asal Provinsi_ → `Patient.address.extension.url` (146, tanpa BQ)<br>_Asal Kabupaten_ → `Patient.address.extension.url` (149, tanpa BQ)<br>_Asal Kecamatan_ → `Patient.address.extension.url` (152, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.url` (159, tanpa BQ)<br>_Nama Dusun_ → `Patient.address.extension.url` (162, tanpa BQ)<br>_Nama jalan dan nomor rumah (jika ada)_ → `Patient.address.line` (183, tanpa BQ)<br>_RW_ → `Patient.address.extension.url` (184, tanpa BQ)<br>_RT_ → `Patient.address.extension.url` (187, tanpa BQ)<br>_Status Pernikahan_ → `Patient.maritalStatus.coding` (205, tanpa BQ) |
| 4 | 10–11 | RelatedPerson | – | – | _Nama Lengkap Suami_ → `RelatedPerson.patient.reference` (10, tanpa BQ) |
| 5 | 12–23 | Observation | SP000402 | Kepemilikan Nomor Induk Kependudukan | _Apakah Ibu punya NIK_ → `Observation.valueBoolean` (15, tanpa BQ) |
| 6 | 27–40 | Observation | SP000403 | Alasan Tidak Ada Nomor Induk Kependudukan | _Pilih alasan tidak mempunyai Nomor Induk Kependudukan (NIK)_ → `Observation.valueCodeableConcept.coding` (30, tanpa BQ) |
| 7 | 45–56 | Observation | 424144002.0 | Current chronological age | _Usia_ → `Observation.valueQuantity.value` (48, tanpa BQ) |
| 8 | 57–63 | Coverage | – | – | _Status BPJS_ → `Coverage.identifier` (57, tanpa BQ) |
| 9 | 64–75 | Observation | SP000408 | Kepemilikan BPJS | – |
| 10 | 81–93 | Observation | 734005006.0 | Telephone number | _Alasan jika ibu tidak memiliki nomor Hp_ → `Observation.valueCodeableConcept.coding` (84, tanpa BQ) |
| 11 | 99–126 | Observation | SP000409 | Rekan Serumah | _Rekan serumah_ → `Observation.component.valueBoolean` (103, tanpa BQ) |
| 12 | 129–131 | RelatedPerson | – | – | _Nomor HP Rekan Satu Rumah_ → `RelatedPerson.telecom` (129, tanpa BQ) |
| 13 | 132–145 | Observation | SP000403 | Alasan Tidak Ada Nomor Induk Kependudukan | _Alasan jika rekan serumah tidak memiliki nomor HP_ → `Observation.valueCodeableConcept.coding` (135, tanpa BQ) |
| 14 | 169–182 | Observation | SP000519 | Tipe Intervensi Puskesmas | _Tipe Intervensi Puskesmas_ → `Observation.valueCodeableConcept.coding` (172, tanpa BQ) |
| 15 | 190–204 | Observation | 82589-3 | Highest level of education | _Tingkat Pendidikan Tertinggi_ → `Observation.status` (190, tanpa BQ) |
| 16 | 211–230 | Observation | 85658-3 | Occupation [Type] | _Pekerjaan_ → `Observation.status` (211, tanpa BQ)<br>_Sebutkan_ → `Observation.note` (223, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 10 |
| RelatedPerson | 2 |
| PractitionerRole | 1 |
| Practitioner | 1 |
| Patient | 1 |
| Coverage | 1 |
| **Total** | **16** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 3 | PractitionerRole | `PractitionerRole.code.coding` | SP000397 | Field staff | http://terminology.kemkes.go.id/sp |
| 2 | 4 | PractitionerRole | `PractitionerRole.code.coding` | SP000396 | Data entry staff | http://terminology.kemkes.go.id/sp |
| 3 | 14 | Observation | `Observation.code.coding` | SP000402 | Kepemilikan Nomor Induk Kependudukan | http://terminology.kemkes.go.id/sp |
| 4 | 29 | Observation | `Observation.code.coding` | SP000403 | Alasan Tidak Ada Nomor Induk Kependudukan | http://terminology.kemkes.go.id/sp |
| 5 | 30 | Observation | `Observation.valueCodeableConcept.coding` | SP000404 | Tidak Punya Kartu Tanda Penduduk | http://terminology.kemkes.go.id/sp |
| 6 | 31 | Observation | `Observation.valueCodeableConcept.coding` | SP000405 | Tidak Membawa Kartu Tanda Penduduk | http://terminology.kemkes.go.id/sp |
| 7 | 32 | Observation | `Observation.valueCodeableConcept.coding` | SP000406 | Kartu Tanda Penduduk Hilang | http://terminology.kemkes.go.id/sp |
| 8 | 33 | Observation | `Observation.valueCodeableConcept.coding` | 397644002.0 | Right to privacy maintained | http://snomed.info/sct |
| 9 | 47 | Observation | `Observation.code.coding` | 424144002.0 | Current chronological age | http://snomed.info/sct |
| 10 | 66 | Observation | `Observation.code.coding` | SP000408 | Kepemilikan BPJS | http://terminology.kemkes.go.id/sp |
| 11 | 83 | Observation | `Observation.code.coding` | 734005006.0 | Telephone number | http://snomed.info/sct |
| 12 | 84 | Observation | `Observation.valueCodeableConcept.coding` | SP000516 | Tidak punya HP | http://terminology.kemkes.go.id/sp |
| 13 | 85 | Observation | `Observation.valueCodeableConcept.coding` | SP000517 | HP hilang | http://terminology.kemkes.go.id/sp |
| 14 | 86 | Observation | `Observation.valueCodeableConcept.coding` | 397644002.0 | Right to privacy maintained | http://snomed.info/sct |
| 15 | 101 | Observation | `Observation.code.coding` | SP000409 | Rekan Serumah | http://terminology.kemkes.go.id/sp |
| 16 | 102 | Observation | `Observation.component.code.coding` | 40683002.0 | Parent | http://snomed.info/sct |
| 17 | 105 | Observation | `Observation.component.code.coding` | 375005.0 | Sibling | http://snomed.info/sct |
| 18 | 108 | Observation | `Observation.component.code.coding` | 303071001.0 | Family member | http://snomed.info/sct |
| 19 | 111 | Observation | `Observation.component.code.coding` | 127848009.0 | Spouse | http://snomed.info/sct |
| 20 | 114 | Observation | `Observation.component.code.coding` | 113163005.0 | Friend | http://snomed.info/sct |
| 21 | 117 | Observation | `Observation.component.code.coding` | 105529008.0 | Lives alone | http://snomed.info/sct |
| 22 | 134 | Observation | `Observation.code.coding` | SP000403 | Alasan Tidak Ada Nomor Induk Kependudukan | http://terminology.kemkes.go.id/sp |
| 23 | 135 | Observation | `Observation.valueCodeableConcept.coding` | SP000404 | Tidak Punya Kartu Tanda Penduduk | http://terminology.kemkes.go.id/sp |
| 24 | 136 | Observation | `Observation.valueCodeableConcept.coding` | SP000405 | Tidak Membawa Kartu Tanda Penduduk | http://terminology.kemkes.go.id/sp |
| 25 | 137 | Observation | `Observation.valueCodeableConcept.coding` | SP000406 | Kartu Tanda Penduduk Hilang | http://terminology.kemkes.go.id/sp |
| 26 | 138 | Observation | `Observation.valueCodeableConcept.coding` | 397644002.0 | Right to privacy maintained | http://snomed.info/sct |
| 27 | 171 | Observation | `Observation.code.coding` | SP000519 | Tipe Intervensi Puskesmas | http://terminology.kemkes.go.id/sp |
| 28 | 172 | Observation | `Observation.valueCodeableConcept.coding` | SP000520 | Blister Digital | http://terminology.kemkes.go.id/sp |
| 29 | 173 | Observation | `Observation.valueCodeableConcept.coding` | SP000521 | Blister Non Digital | http://terminology.kemkes.go.id/sp |
| 30 | 174 | Observation | `Observation.valueCodeableConcept.coding` | SP000522 | Botol Digital | http://terminology.kemkes.go.id/sp |
| 31 | 175 | Observation | `Observation.valueCodeableConcept.coding` | SP000523 | Botol Non Digital | http://terminology.kemkes.go.id/sp |
| 32 | 192 | Observation | `Observation.code.coding` | 82589-3 | Highest level of education | http://loinc.org |
| 33 | 213 | Observation | `Observation.code.coding` | 85658-3 | Occupation [Type] | http://loinc.org |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://terminology.kemkes.go.id/sp | 20 |
| http://snomed.info/sct | 11 |
| http://loinc.org | 2 |
| **Total** | **33** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 7 | – | Tanggal entry | – | `` |
| 41 | – | Tanggal lahir ibu diketahui? | – | `` |
| 76 | – | Nomor HP | – | `` |
| 94 | – | Apakah ibu memiliki alamat email? | – | `` |
| 127 | – | Apakah rekan serumah memiliki nomor HP | – | `` |
| 155 | – | Asal Puskesmas | Organization | `Organization.active` |
| 165 | – | Posyandu | Organization | `Organization.active` |
