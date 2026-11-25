# Output Form: KuApps BidanKu - Tambah Pasien

Sumber: `mapping/phdt-data-dictionary-kuapps-bidanku-tambah-pasien.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-kuapps-bidanku-tambah-pasien.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 11 |
| Code (`jumlah code` = 1) | 33 |
| Code unik (code + CodeSystem) | 33 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 11 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–12 | Patient | – | – | _NIK_ → `Patient.identifier.value` (4, tanpa BQ)<br>_No KK_ → `Patient.identifier.value` (7, tanpa BQ)<br>_Nama Lengkap_ → `Patient.name.text` (8, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (12, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (26, tanpa BQ)<br>_No HP_ → `Patient.telecom.system` (82, tanpa BQ)<br>_Status Pernikahan_ → `Patient.maritalStatus.coding` (86, tanpa BQ)<br>_Alamat tempat tinggal sekarang_ → `Patient.address.line` (148, tanpa BQ)<br>_Kabupaten_ → `Patient.address.extension.url` (150, tanpa BQ)<br>_Kecamatan_ → `Patient.address.extension.url` (153, tanpa BQ)<br>_Desa_ → `Patient.address.extension.url` (161, tanpa BQ)<br>_Dusun_ → `Patient.address.extension.url` (164, tanpa BQ)<br>_RW_ → `Patient.address.extension.url` (167, tanpa BQ)<br>_RT_ → `Patient.address.extension.url` (170, tanpa BQ) |
| 2 | 14–25 | Observation | 424144002 | Current chronological age | _Usia_ → `Observation.valueQuantity.value` (17, tanpa BQ) |
| 3 | 28–38 | Observation | 224098002 | Place in family order | _Anak Ke-_ → `Observation.valueInteger` (31, tanpa BQ) |
| 4 | 39–56 | Observation | 82589-3 | Highest level of education | _Pendidikan_ → `Observation.valueCodeableConcept.coding` (42, tanpa BQ) |
| 5 | 57–81 | Observation | 14679004 | Occupation | _Pekerjaan_ → `Observation.valueCodeableConcept.coding` (60, tanpa BQ) |
| 6 | 92–97 | RelatedPerson | – | – | _Nama Suami_ → `RelatedPerson.patient` (92, tanpa BQ)<br>_Tanggal Lahir suami_ → `RelatedPerson.birthDate` (96, tanpa BQ)<br>_NIK suami_ → `RelatedPerson.identifier` (97, tanpa BQ)<br>_Nama Ibu/Wali_ → `RelatedPerson.patient` (100, tanpa BQ)<br>_NIK Ibu_ → `RelatedPerson.identifier` (104, tanpa BQ)<br>_Tanggal lahir ibu/Wali_ → `RelatedPerson.birthDate` (105, tanpa BQ)<br>_No HP Ibu_ → `RelatedPerson.telecom.system` (106, tanpa BQ)<br>_Nama Ayah_ → `RelatedPerson.patient` (111, tanpa BQ)<br>_NIK Ayah_ → `RelatedPerson.identifier` (114, tanpa BQ)<br>_Nama Kontak Keluarga_ → `RelatedPerson.name` (115, tanpa BQ)<br>_Nomor Telpon yang bisa dihubungi_ → `RelatedPerson.telecom.system` (116, tanpa BQ) |
| 7 | 119–132 | Observation | 87520-3 | Coverage type | _Apakah memiliki jaminan kesehatan?_ → `Observation.valueCodeableConcept` (122, tanpa BQ) |
| 8 | 133–135 | Coverage | – | – | _Nomor Jaminan_ → `Coverage.status` (133, tanpa BQ) |
| 9 | 136–147 | Observation | SP000132 | Memiliki Buku KIA | _Apakah memiliki buku KIA?_ → `Observation.valueBoolean` (139, tanpa BQ) |
| 10 | 177–181 | ServiceRequest | 737492002 | Outpatient care management | _Faskes Rujukan_ → `ServiceRequest.category.coding` (177, tanpa BQ) |
| 11 | 182–185 | Consent | – | – | _Tenaga kesehatan telah mendapatkan persetujuan dari individu atau wali untuk didaftarkan di aplikasi_ → `Consent.status` (182, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 6 |
| Patient | 1 |
| RelatedPerson | 1 |
| Coverage | 1 |
| ServiceRequest | 1 |
| Consent | 1 |
| **Total** | **11** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 16 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 2 | 30 | Observation | `Observation.code.coding` | 224098002 | Place in family order | http://snomed.info/sct |
| 3 | 41 | Observation | `Observation.code.coding` | 82589-3 | Highest level of education | http://loinc.org |
| 4 | 42 | Observation | `Observation.valueCodeableConcept.coding` | 473463000 | Received elementary school education | http://snomed.info/sct |
| 5 | 43 | Observation | `Observation.valueCodeableConcept.coding` | 603435002 | Educated to junior high school level | http://snomed.info/sct |
| 6 | 44 | Observation | `Observation.valueCodeableConcept.coding` | 603434003 | Educated to senior high school level | http://snomed.info/sct |
| 7 | 45 | Observation | `Observation.valueCodeableConcept.coding` | SP000277 | D3 | http://terminology.kemkes.go.id/sp |
| 8 | 46 | Observation | `Observation.valueCodeableConcept.coding` | 38861000087100 | Bachelor's degree achieved | http://snomed.info/sct |
| 9 | 47 | Observation | `Observation.valueCodeableConcept.coding` | 38881000087106 | Master's degree achieved | http://snomed.info/sct |
| 10 | 48 | Observation | `Observation.valueCodeableConcept.coding` | 440345007 | Doctorate degree achieved | http://snomed.info/sct |
| 11 | 49 | Observation | `Observation.valueCodeableConcept.coding` | 224294005 | No formal education | http://snomed.info/sct |
| 12 | 59 | Observation | `Observation.code.coding` | 14679004 | Occupation | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 13 | 60 | Observation | `Observation.valueCodeableConcept.coding` | 73438004 | Unemployed | http://snomed.info/sct |
| 14 | 61 | Observation | `Observation.valueCodeableConcept.coding` | 106540006 | Laborer | http://snomed.info/sct |
| 15 | 62 | Observation | `Observation.valueCodeableConcept.coding` | 160906004 | Self-employed | http://snomed.info/sct |
| 16 | 63 | Observation | `Observation.valueCodeableConcept.coding` | SP000244 | Pedagang kecil | http://terminology.kemkes.go.id/sp |
| 17 | 64 | Observation | `Observation.valueCodeableConcept.coding` | SP000362 | PNS/TNI/Polri | http://terminology.kemkes.go.id/sp |
| 18 | 65 | Observation | `Observation.valueCodeableConcept.coding` | SP000245 | Wirausaha | http://terminology.kemkes.go.id/sp |
| 19 | 66 | Observation | `Observation.valueCodeableConcept.coding` | TK000041 | Pegawai/karyawan swasta | http://terminology.kemkes.go.id |
| 20 | 67 | Observation | `Observation.valueCodeableConcept.coding` | 77715000 | Fisherman | http://snomed.info/sct |
| 21 | 68 | Observation | `Observation.valueCodeableConcept.coding` | 106388008 | Farmer | http://snomed.info/sct |
| 22 | 69 | Observation | `Observation.valueCodeableConcept.coding` | 36625000 | Livestock worker | http://snomed.info/sct |
| 23 | 70 | Observation | `Observation.valueCodeableConcept.coding` | SP000274 | Pedagang besar | http://terminology.kemkes.go.id/sp |
| 24 | 71 | Observation | `Observation.valueCodeableConcept.coding` | 105493001 | Retired, life even | http://snomed.info/sct |
| 25 | 72 | Observation | `Observation.valueCodeableConcept.coding` | SP000288 | Tenaga Kerja Indonesia | http://terminology.kemkes.go.id/sp |
| 26 | 73 | Observation | `Observation.valueCodeableConcept.coding` | SP000289 | Karyawan BUMN | http://terminology.kemkes.go.id/sp |
| 27 | 74 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 28 | 121 | Observation | `Observation.code.coding` | 87520-3 | Coverage type | http://loinc.org |
| 29 | 123 | Observation | `Observation.valueCodeableConcept` | SP000652 | Jaminan Kesehatan Nasional (JKN) | http://terminology.kemkes.go.id/sp |
| 30 | 124 | Observation | `Observation.valueCodeableConcept` | SP000926 | Jamkesda | http://terminology.kemkes.go.id/sp |
| 31 | 125 | Observation | `Observation.valueCodeableConcept` | SP000927 | Jampersal | http://terminology.kemkes.go.id/sp |
| 32 | 138 | Observation | `Observation.code.coding` | SP000132 | Memiliki Buku KIA | http://terminology.kemkes.go.id/sp |
| 33 | 178 | ServiceRequest | `ServiceRequest.code.coding` | 737492002 | Outpatient care management | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 18 |
| http://terminology.kemkes.go.id/sp | 11 |
| http://loinc.org | 2 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 1 |
| http://terminology.kemkes.go.id | 1 |
| **Total** | **33** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 9 | – | Nama Kepala Keluarga | – | `` |
| 10 | – | Apakah tanggal lahir diketahui | – | `` |
| 98 | – | Apakah anak memiliki wali | Tdk dimapping FHIR | `` |
| 109 | – | Apakah ayah masih hidup? | Tdk dimapping FHIR | `` |
| 156 | – | Puskesmas | Organization | `Organization.active` |
| 160 | – | Posyandu | – | `` |
| 173 | – | Faskes Tingkat 1 | Organization | `Organization.active` |
