# Output Form: MPDN Kematian Ibu

Sumber: `mapping/phdt-data-dictionary-mpdn-kematian-ibu.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-mpdn-kematian-ibu.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 10 |
| Code (`jumlah code` = 1) | 50 |
| Code unik (code + CodeSystem) | 50 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 17 |
| Variabel BQ (unik) | 0 |
| Variabel raw (variabel dictionary; belum ada file mentah) | 24 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 4–27 | Patient | – | – | _Nama Ibu Hamil_ → `Patient.name` (4, tanpa BQ)<br>_Status Pernikahan_ → `Patient.maritalStatus.coding` (8, tanpa BQ)<br>_KTP/NIK_ → `Patient.identifier.value` (14, tanpa BQ)<br>_Nomor Hp/Kontak Keluarga_ → `Patient.telecom.value` (17, tanpa BQ)<br>_Kabupaten/Kota KTP_ → `Patient.address.city` (18, tanpa BQ)<br>_Provinsi KTP_ → `Patient.address.extension:administrativeCode.extension:province.valueCode` (21, tanpa BQ)<br>_Kabupaten/Kota KTP_ → `Patient.address.extension:administrativeCode.extension:city.valueCode` (22, tanpa BQ)<br>_Provinsi Domisili_ → `Patient.address.extension:administrativeCode.extension:province.valueCode` (24, tanpa BQ)<br>_Kabupaten/Kota Domisili_ → `Patient.address.extension:administrativeCode.extension:city.valueCode` (25, tanpa BQ)<br>_Kecamatan Domisili_ → `Patient.address.extension:administrativeCode.extension:district.valueCode` (26, tanpa BQ)<br>_Desa/Kelurahan Domisili_ → `Patient.address.extension:administrativeCode.extension:village.valueCode` (27, tanpa BQ) |
| 2 | 28–34 | Condition | – | – | _Kode ICD_ → `Condition.category.coding` (29, tanpa BQ)<br>_Nama Diagnosa_ → `Condition.code.coding` (30, tanpa BQ)<br>_Nama Ibu Hamil_ → `Condition.subject.display` (32, tanpa BQ)<br>_Tgl. Meninggal_ → `Condition.onsetDateTime` (33, tanpa BQ)<br>_Wkt. Lapor_ → `Condition.recordedDate` (34, tanpa BQ) |
| 3 | 35–44 | Observation | 81956-5 | Date and time of death [TimeStamp] | _Tgl. Meninggal_ → `Observation.category.coding` (36, tanpa BQ)<br>_Tgl. Meninggal_ → `Observation.valueDateTime` (38, tanpa BQ)<br>_Nama Ibu Hamil_ → `Observation.subject.display` (40, tanpa BQ)<br>_Tgl. Meninggal_ → `Observation.effectiveDateTime` (41, tanpa BQ)<br>_Wkt. Lapor_ → `Observation.issued` (42, tanpa BQ)<br>_//PJ MPDN_ → `Observation.performer.display` (44, tanpa BQ) |
| 4 | 45–56 | Observation | 39016-1 | Age at death | _Umur_ → `Observation.valueQuantity.value` (48, tanpa BQ)<br>_Nama Ibu Hamil_ → `Observation.subject.display` (52, tanpa BQ)<br>_Tgl. Meninggal_ → `Observation.effectiveDateTime` (53, tanpa BQ)<br>_Wkt. Lapor_ → `Observation.issued` (54, tanpa BQ)<br>_//PJ MPDN_ → `Observation.performer.display` (56, tanpa BQ) |
| 5 | 57–67 | Observation | 11996-6 | [#] Pregnancies | _Hamil ke_ → `Observation.valueInteger[0]` (61, tanpa BQ)<br>_Nama Ibu Hamil_ → `Observation.subject.display` (63, tanpa BQ)<br>_Tgl. Meninggal_ → `Observation.effectiveDateTime` (64, tanpa BQ)<br>_Wkt. Lapor_ → `Observation.issued` (65, tanpa BQ)<br>_//PJ MPDN_ → `Observation.performer.display` (67, tanpa BQ) |
| 6 | 68–79 | Observation | OC000026 | Masa terjadi Kematian Ibu | _Masa Terjadi_ → `Observation.valueCodeableConcept` (71, tanpa BQ)<br>_Nama Ibu Hamil_ → `Observation.subject.display` (75, tanpa BQ)<br>_Tgl. Meninggal_ → `Observation.effectiveDateTime` (76, tanpa BQ)<br>_Wkt. Lapor_ → `Observation.issued` (77, tanpa BQ)<br>_//PJ MPDN_ → `Observation.performer.display` (79, tanpa BQ) |
| 7 | 80–92 | Observation | 79378-6 | Cause of death | _Dugaan Sebab_ → `Observation.component.valueCodeableConcept.coding` (84, tanpa BQ)<br>_Dugaan Sebab_ → `Observation.component.valueCodeableConcept.coding` (86, tanpa BQ)<br>_Nama Ibu Hamil_ → `Observation.subject.display` (88, tanpa BQ)<br>_Tgl. Meninggal_ → `Observation.effectiveDateTime` (89, tanpa BQ)<br>_Wkt. Lapor_ → `Observation.issued` (90, tanpa BQ)<br>_//PJ MPDN_ → `Observation.performer.display` (92, tanpa BQ) |
| 8 | 93–122 | Observation | OC000028 | Jenis Tempat Meninggal | _Tempat Meninggal_ → `Observation.valueCodeableConcept.coding` (96, tanpa BQ)<br>_Nama Ibu Hamil_ → `Observation.subject.display` (118, tanpa BQ)<br>_Tgl. Meninggal_ → `Observation.effectiveDateTime` (119, tanpa BQ)<br>_Wkt. Lapor_ → `Observation.issued` (120, tanpa BQ)<br>_//PJ MPDN_ → `Observation.performer.display` (122, tanpa BQ) |
| 9 | 123–147 | Observation | SP000098 | Tipe Penyelenggara Faskes Meninggal | _Tipe - Penyelenggara Faskes_ → `Observation.valueCodeableConcept.coding` (127, tanpa BQ)<br>_Nama Ibu Hamil_ → `Observation.subject.display` (143, tanpa BQ)<br>_Tgl. Meninggal_ → `Observation.effectiveDateTime` (144, tanpa BQ)<br>_Wkt. Lapor_ → `Observation.issued` (145, tanpa BQ)<br>_//PJ MPDN_ → `Observation.performer.display` (147, tanpa BQ) |
| 10 | 148–188 | Composition | – | – | _Faskes Meninggal_ → `Composition.contained.name` (150, tanpa BQ)<br>_Kabupaten/Kota Meninggal_ → `Composition.contained.address.city` (153, tanpa BQ)<br>_Provinsi Meninggal_ → `Composition.contained.address.extension:administrativeCode.extension:province` (155, tanpa BQ)<br>_Kabupaten/Kota Meninggal_ → `Composition.contained.address.extension:administrativeCode.extension:city` (156, tanpa BQ)<br>_Nama Ibu Hamil_ → `Composition.subject.display` (159, tanpa BQ)<br>_//PJ MPDN_ → `Composition.author.display` (161, tanpa BQ)<br>_Wkt. Lapor_ → `Composition.date` (163, tanpa BQ)<br>_Status Data_ → `Composition.status` (164, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 7 |
| Patient | 1 |
| Condition | 1 |
| Composition | 1 |
| **Total** | **10** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 37 | Observation | `Observation.code.coding` | 81956-5 | Date and time of death [TimeStamp] | http://loinc.org |
| 2 | 47 | Observation | `Observation.code.coding` | 39016-1 | Age at death | http://loinc.org |
| 3 | 59 | Observation | `Observation.code.coding` | 11996-6 | [#] Pregnancies | http://loinc.org |
| 4 | 60 | Observation | `Observation.code.coding` | ANC.B6.DE24 | Number of pregnancies (gravida) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 5 | 70 | Observation | `Observation.code.coding` | OC000026 | Masa terjadi Kematian Ibu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 6 | 71 | Observation | `Observation.valueCodeableConcept` | 1156679005 | Maternal antenatal period | http://snomed.info/sct |
| 7 | 72 | Observation | `Observation.valueCodeableConcept` | 1156682000 | Maternal intrapartum period | http://snomed.info/sct |
| 8 | 73 | Observation | `Observation.valueCodeableConcept` | 255410009 | Maternal postpartum | http://snomed.info/sct |
| 9 | 82 | Observation | `Observation.code.coding` | 79378-6 | Cause of death | http://loinc.org |
| 10 | 83 | Observation | `Observation.component.code.coding` | TK000019 | Kode group | http://terminology.kemkes.go.id |
| 11 | 85 | Observation | `Observation.component.code.coding` | TK000021 | Kode detail | http://terminology.kemkes.go.id |
| 12 | 95 | Observation | `Observation.code.coding` | OC000028 | Jenis Tempat Meninggal | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 13 | 96 | Observation | `Observation.valueCodeableConcept.coding` | LT000008 | Dalam perjalanan dari rumah/masyarakat | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 14 | 97 | Observation | `Observation.valueCodeableConcept.coding` | LT000009 | Dalam perjalanan ke faskes lain | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 15 | 98 | Observation | `Observation.valueCodeableConcept.coding` | SP000099 | FASKES | http://terminology.kemkes.go.id/sp |
| 16 | 99 | Observation | `Observation.valueCodeableConcept.coding` | 102 | Pusat Kesehatan Masyarakat | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 17 | 100 | Observation | `Observation.valueCodeableConcept.coding` | OT000006 | Rumah Sakit Pemerintah | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 18 | 101 | Observation | `Observation.valueCodeableConcept.coding` | OT000007 | Rumah Sakit Swasta | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 19 | 102 | Observation | `Observation.valueCodeableConcept.coding` | LT000006 | Rumah Ibu | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 20 | 103 | Observation | `Observation.valueCodeableConcept.coding` | 104 | Rumah Sakit | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 21 | 104 | Observation | `Observation.valueCodeableConcept.coding` | OT000002 | Pustu | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 22 | 105 | Observation | `Observation.valueCodeableConcept.coding` | OT000010 | Klinik Medis Utama | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 23 | 106 | Observation | `Observation.valueCodeableConcept.coding` | OT000011 | Klinik Medis Pratama | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 24 | 107 | Observation | `Observation.valueCodeableConcept.coding` | 103 | Klinik | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 25 | 108 | Observation | `Observation.valueCodeableConcept.coding` | 101 | Tempat Praktik Mandiri Tenaga Kesehatan | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 26 | 109 | Observation | `Observation.valueCodeableConcept.coding` | OT000004 | Bidan Praktek Mandiri | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 27 | 110 | Observation | `Observation.valueCodeableConcept.coding` | OT000008 | Rumah Bersalin | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 28 | 111 | Observation | `Observation.valueCodeableConcept.coding` | 394573001 | Maternity clinic | http://snomed.info/sct |
| 29 | 112 | Observation | `Observation.valueCodeableConcept.coding` | OT000001 | Polindes | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 30 | 113 | Observation | `Observation.valueCodeableConcept.coding` | 264362003 | Home (environment) | http://snomed.info/sct |
| 31 | 114 | Observation | `Observation.valueCodeableConcept.coding` | LT000007 | Rumah Dukun | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 32 | 115 | Observation | `Observation.valueCodeableConcept.coding` | LT000010 | Lainnya | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 33 | 116 | Observation | `Observation.valueCodeableConcept.coding` | LT000011 | Belum Tahu | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 34 | 126 | Observation | `Observation.code.coding` | SP000098 | Tipe Penyelenggara Faskes Meninggal | http://terminology.kemkes.go.id/sp |
| 35 | 127 | Observation | `Observation.valueCodeableConcept.coding` | SP000076 | RSU - Pemprop | http://terminology.kemkes.go.id/sp |
| 36 | 128 | Observation | `Observation.valueCodeableConcept.coding` | SP000077 | PUSKESMAS - Pemkab | http://terminology.kemkes.go.id/sp |
| 37 | 129 | Observation | `Observation.valueCodeableConcept.coding` | SP000078 | RSU - Pemkot | http://terminology.kemkes.go.id/sp |
| 38 | 130 | Observation | `Observation.valueCodeableConcept.coding` | SP000079 | RSU - Pemkab | http://terminology.kemkes.go.id/sp |
| 39 | 131 | Observation | `Observation.valueCodeableConcept.coding` | SP000080 | RSIA - Perusahaan | http://terminology.kemkes.go.id/sp |
| 40 | 132 | Observation | `Observation.valueCodeableConcept.coding` | SP000081 | RSU - TNI AD | http://terminology.kemkes.go.id/sp |
| 41 | 133 | Observation | `Observation.valueCodeableConcept.coding` | SP000082 | RS Bersalin - Swasta/Lainnya | http://terminology.kemkes.go.id/sp |
| 42 | 134 | Observation | `Observation.valueCodeableConcept.coding` | SP000083 | RS - Organisasi Islam | http://terminology.kemkes.go.id/sp |
| 43 | 135 | Observation | `Observation.valueCodeableConcept.coding` | SP000084 | RS Bersalin - Pemkab | http://terminology.kemkes.go.id/sp |
| 44 | 136 | Observation | `Observation.valueCodeableConcept.coding` | SP000085 | RSU - Swasta/Lainnya | http://terminology.kemkes.go.id/sp |
| 45 | 137 | Observation | `Observation.valueCodeableConcept.coding` | SP000086 | RSU - KEMENKES | http://terminology.kemkes.go.id/sp |
| 46 | 138 | Observation | `Observation.valueCodeableConcept.coding` | SP000087 | RSU - Perusahaan | http://terminology.kemkes.go.id/sp |
| 47 | 139 | Observation | `Observation.valueCodeableConcept.coding` | SP000088 | RSU - Organisasi Islam | http://terminology.kemkes.go.id/sp |
| 48 | 140 | Observation | `Observation.valueCodeableConcept.coding` | SP000089 | RSU - Organisasi Sosial | http://terminology.kemkes.go.id/sp |
| 49 | 141 | Observation | `Observation.valueCodeableConcept.coding` | SP000090 | RS - Swasta/Lainnya | http://terminology.kemkes.go.id/sp |
| 50 | 157 | Composition | `Composition.type.coding` | COM000001 | Formulir Informasi Kematian Maternal | http://terminology.kemkes.go.id/CodeSystem/composition-type |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://terminology.kemkes.go.id/sp | 17 |
| http://terminology.kemkes.go.id/CodeSystem/organization-type | 12 |
| http://terminology.kemkes.go.id/CodeSystem/location-type | 6 |
| http://snomed.info/sct | 5 |
| http://loinc.org | 4 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 2 |
| http://terminology.kemkes.go.id | 2 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 1 |
| http://terminology.kemkes.go.id/CodeSystem/composition-type | 1 |
| **Total** | **50** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
