# Output Form: SISMAL - Regmal 1

Sumber: `mapping/phdt-data-dictionary-sismal-regmal1.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-sismal-regmal1.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 20 |
| Code (`jumlah code` = 1) | 54 |
| Code unik (code + CodeSystem) | 52 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 14 |
| Variabel BQ (unik) | 1 |
| Variabel raw (variabel dictionary; belum ada file mentah) | 49 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–14 | Patient | – | – | _WNA_ → `Patient.extension:citizenshipStatus` (2, tanpa BQ)<br>_Negara_ → `Patient.address.country` (4, tanpa BQ)<br>_No. Passpor/Pas Lintas Batas/Nomor Identitas_ → `Patient.identifier.value` (7, tanpa BQ)<br>_Nomor Identitas Kependudukan (NIK)_ → `Patient.identifier.value` (11, tanpa BQ)<br>_Nama Pasien_ → `Patient.name.text` (12, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (13, tanpa BQ)<br>_Provinsi Domisili_ → `Patient.address.extension.url` (42, tanpa BQ)<br>_Kab/Kota Domisili_ → `Patient.address.extension.url` (45, tanpa BQ)<br>_Kecamatan Domisili_ → `Patient.address.extension.url` (48, tanpa BQ)<br>_Desa Domisili_ → `Patient.address.extension.url` (51, tanpa BQ)<br>_Alamat Lengkap Domisili_ → `Patient.address.line` (54, tanpa BQ)<br>_Provinsi KTP_ → `Patient.address.extension.url` (69, tanpa BQ)<br>_Kab/Kota KTP_ → `Patient.address.extension.url` (72, tanpa BQ)<br>_Kecamatan KTP_ → `Patient.address.extension.url` (75, tanpa BQ)<br>_Alamat Lengkap KTP_ → `Patient.address.line` (78, tanpa BQ) |
| 2 | 15–27 | Observation | 424144002 | Current chronological age | _Usia_ → `Observation.valueQuantity.value` (18, tanpa BQ)<br>_Tahun/Bulan_ → `Observation.valueQuantity.code` (19, tanpa BQ) |
| 3 | 28–39 | Observation | SP000757 | Status Kependudukan (Khusus Papua) | _Status Kependudukan (Khusus Papua)_ → `Observation.valueCodeableConcept.coding` (31, tanpa BQ) |
| 4 | 56–66 | Observation | SP000760 | Pasien Beralamat (KTP) Diluar Wilayah | _Pasien Beralamat (KTP) Diluar Wilayah_ → `Observation.valueBoolean` (59, tanpa BQ) |
| 5 | 130–153 | Observation | 85658-3 | Occupation [Type] | `Pekerjaan` → `Observation.valueCodeableConcept.coding` (133) |
| 6 | 154–164 | Observation | 82810-3 | Pregnancy status | _Status Kehamilan_ → `Observation.valueCodeableConcept.coding` (157, tanpa BQ) |
| 7 | 165–169 | PractitionerRole | – | – | _Petugas_ → `PractitionerRole.active` (165, tanpa BQ) |
| 8 | 170–190 | Practitioner | – | – | _Nama Petugas_ → `Practitioner.name.text` (172, tanpa BQ) |
| 9 | 191–208 | Observation | 385438008 | Source of information | _Asal Penemuan_ → `Observation.valueCodeableConcept.coding` (194, tanpa BQ) |
| 10 | 209–227 | Observation | 418775008 | Finding method | _Kegiatan Penemuan_ → `Observation.valueCodeableConcept.coding` (212, tanpa BQ) |
| 11 | 228–238 | Observation | – | – | _SSR_ → `Observation.valueCodeableConcept.coding` (231, tanpa BQ) |
| 12 | 239–249 | Observation | – | – | _Penemuan Kasus oleh Kader Endemis tinggi_ → `Observation.valueBoolean` (242, tanpa BQ) |
| 13 | 250–262 | Observation | 424144002 | Current chronological age | _Jenis Pemeriksaan_ → `Observation.valueCodeableConcept.coding` (253, tanpa BQ) |
| 14 | 264–278 | Encounter | – | – | _Tanggal Kunjungan Pasien_ → `Encounter.period.start` (273, tanpa BQ) |
| 15 | 279–285 | Condition | – | – | – |
| 16 | 300–315 | Observation | 365690003 | Finding of presence of organism | _Jenis Parasit_ → `Observation.valueCodeableConcept.coding` (303, tanpa BQ) |
| 17 | 316–326 | Observation | – | – | _Total RDT_ → `Observation.valueInteger` (319, tanpa BQ) |
| 18 | 327–339 | Observation | 29463-7 | Body weight | _Berat badan (Kg)_ → `Observation.valueQuantity.value` (331, tanpa BQ) |
| 19 | 340–351 | Observation | 8310-5 | Body temperature | _Suhu Tubuh (Celcius)_ → `Observation.valueQuantity.value` (343, tanpa BQ) |
| 20 | 352–370 | ServiceRequest | – | – | _Rujuk_ → `ServiceRequest.status` (352, tanpa BQ)<br>_Faskes Rujukan_ → `ServiceRequest.locationCode.coding` (365, tanpa BQ)<br>_Nama Faskes Rujukan_ → `ServiceRequest.locationCode.text` (370, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 14 |
| Patient | 1 |
| PractitionerRole | 1 |
| Practitioner | 1 |
| Encounter | 1 |
| Condition | 1 |
| ServiceRequest | 1 |
| **Total** | **20** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 17 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 2 | 30 | Observation | `Observation.code.coding` | SP000757 | Status Kependudukan (Khusus Papua) | http://terminology.kemkes.go.id/sp |
| 3 | 31 | Observation | `Observation.valueCodeableConcept.coding` | SP000758 | Orang Asli Papua (OAP) | http://terminology.kemkes.go.id/sp |
| 4 | 32 | Observation | `Observation.valueCodeableConcept.coding` | SP000759 | Bukan Orang Asli Papua | http://terminology.kemkes.go.id/sp |
| 5 | 58 | Observation | `Observation.code.coding` | SP000760 | Pasien Beralamat (KTP) Diluar Wilayah | http://terminology.kemkes.go.id/sp |
| 6 | 132 | Observation | `Observation.code.coding` | 85658-3 | Occupation [Type] | http://loinc.org |
| 7 | 133 | Observation | `Observation.valueCodeableConcept.coding` | 67630004 | Miner | http://snomed.info/sct |
| 8 | 134 | Observation | `Observation.valueCodeableConcept.coding` | SP000754 | Pedagang | http://terminology.kemkes.go.id/sp |
| 9 | 135 | Observation | `Observation.valueCodeableConcept.coding` | 302314004 | Military personnel | http://snomed.info/sct |
| 10 | 136 | Observation | `Observation.valueCodeableConcept.coding` | 14406004 | Policeman | http://snomed.info/sct |
| 11 | 137 | Observation | `Observation.valueCodeableConcept.coding` | TK000041 | Pegawai/karyawan swasta | http://terminology.kemkes.go.id |
| 12 | 138 | Observation | `Observation.valueCodeableConcept.coding` | 73438004 | Unemployed | http://snomed.info/sct |
| 13 | 139 | Observation | `Observation.valueCodeableConcept.coding` | 77715000 | Fisherman | http://snomed.info/sct |
| 14 | 140 | Observation | `Observation.valueCodeableConcept.coding` | 106388008 | Farmer | http://snomed.info/sct |
| 15 | 141 | Observation | `Observation.valueCodeableConcept.coding` | 444168002 | Homemaker | http://snomed.info/sct |
| 16 | 142 | Observation | `Observation.valueCodeableConcept.coding` | 34484007 | Forestry worker | http://snomed.info/sct |
| 17 | 143 | Observation | `Observation.valueCodeableConcept.coding` | 65853000 | Student | http://snomed.info/sct |
| 18 | 144 | Observation | `Observation.valueCodeableConcept.coding` | 34024003 | Gardener | http://snomed.info/sct |
| 19 | 145 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 20 | 156 | Observation | `Observation.code.coding` | 82810-3 | Pregnancy status | http://loinc.org |
| 21 | 157 | Observation | `Observation.valueCodeableConcept.coding` | LA15173-0 | Pregnant | http://loinc.org |
| 22 | 158 | Observation | `Observation.valueCodeableConcept.coding` | LA26683-5 | Not pregnant | http://loinc.org |
| 23 | 167 | PractitionerRole | `PractitionerRole.code.coding` | 223366009 | Healthcare professional | http://snomed.info/sct |
| 24 | 168 | PractitionerRole | `PractitionerRole.code.coding` | SP000373 | Kader Kesehatan | http://terminology.kemkes.go.id/sp |
| 25 | 193 | Observation | `Observation.code.coding` | 385438008 | Source of information | http://snomed.info/sct |
| 26 | 194 | Observation | `Observation.valueCodeableConcept.coding` | SP000803 | Fasyankes Pencatat | http://terminology.kemkes.go.id/sp |
| 27 | 195 | Observation | `Observation.valueCodeableConcept.coding` | 138 | Puskesmas Pembantu | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 28 | 196 | Observation | `Observation.valueCodeableConcept.coding` | SP000761 | Faskes Swasta | http://terminology.kemkes.go.id/CodeSystem/organization-ownership |
| 29 | 197 | Observation | `Observation.valueCodeableConcept.coding` | 101 | Praktek mandiri | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 30 | 198 | Observation | `Observation.valueCodeableConcept.coding` | SP000804 | Kantor Kesehatan Pelabuhan | http://terminology.kemkes.go.id/sp |
| 31 | 199 | Observation | `Observation.valueCodeableConcept.coding` | SP000805 | Perdhaki | http://terminology.kemkes.go.id/sp |
| 32 | 200 | Observation | `Observation.valueCodeableConcept.coding` | SP000806 | Pos Kesehatan TNI | http://terminology.kemkes.go.id/sp |
| 33 | 201 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 34 | 211 | Observation | `Observation.code.coding` | 418775008 | Finding method | http://snomed.info/sct |
| 35 | 212 | Observation | `Observation.valueCodeableConcept.coding` | SP000807 | Passive Case Detection | http://terminology.kemkes.go.id/sp |
| 36 | 213 | Observation | `Observation.valueCodeableConcept.coding` | 185389009 | Follow-up visit | http://snomed.info/sct |
| 37 | 214 | Observation | `Observation.valueCodeableConcept.coding` | SP000808 | Mass Blood Survey | http://terminology.kemkes.go.id/sp |
| 38 | 215 | Observation | `Observation.valueCodeableConcept.coding` | 225368008 | Contact tracing | http://snomed.info/sct |
| 39 | 216 | Observation | `Observation.valueCodeableConcept.coding` | SP000809 | Survei Non PE | http://terminology.kemkes.go.id/sp |
| 40 | 217 | Observation | `Observation.valueCodeableConcept.coding` | 439708006 | Home visit | http://snomed.info/sct |
| 41 | 218 | Observation | `Observation.valueCodeableConcept.coding` | SP000810 | Surveilans Migrasi | http://terminology.kemkes.go.id/sp |
| 42 | 219 | Observation | `Observation.valueCodeableConcept.coding` | 702705002 | Mobile clinic | http://snomed.info/sct |
| 43 | 220 | Observation | `Observation.valueCodeableConcept.coding` | 131 | Posyandu | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 44 | 252 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 45 | 302 | Observation | `Observation.code.coding` | 365690003 | Finding of presence of organism | http://snomed.info/sct |
| 46 | 303 | Observation | `Observation.valueCodeableConcept.coding` | 30020004 | Plasmodium falciparum | http://snomed.info/sct |
| 47 | 304 | Observation | `Observation.valueCodeableConcept.coding` | 56395006 | Plasmodium malariae | http://snomed.info/sct |
| 48 | 305 | Observation | `Observation.valueCodeableConcept.coding` | 49918008 | Plasmodium knowlesi | http://snomed.info/sct |
| 49 | 306 | Observation | `Observation.valueCodeableConcept.coding` | 74746009 | Plasmodium vivax | http://snomed.info/sct |
| 50 | 307 | Observation | `Observation.valueCodeableConcept.coding` | 18508006 | Plasmodium ovale | http://snomed.info/sct |
| 51 | 308 | Observation | `Observation.valueCodeableConcept.coding` | 21070001 | Mixed malaria | http://snomed.info/sct |
| 52 | 329 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 53 | 330 | Observation | `Observation.code.coding` | ANC.B8.DE3 | Current weight | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 54 | 342 | Observation | `Observation.code.coding` | 8310-5 | Body temperature | http://loinc.org |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 28 |
| http://terminology.kemkes.go.id/sp | 14 |
| http://loinc.org | 6 |
| http://terminology.kemkes.go.id/CodeSystem/organization-type | 3 |
| http://terminology.kemkes.go.id | 1 |
| http://terminology.kemkes.go.id/CodeSystem/organization-ownership | 1 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 1 |
| **Total** | **54** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 81 | – | Kode Fasyankes | Organization | `Organization.identifier` |
| 82 | – | Jenis Faskes | Organization | `Organization.type` |
| 84 | – | Kepemilikan | Organization | `Organization.type` |
| 87 | – | Faskes Pencatat | Organization | `Organization.name` |
| 88 | – | No Telepon | Organization | `Organization.telecom` |
| 93 | – | Provinsi Pencatat | Organization | `Organization.address.extension.extension.valueCode` |
| 96 | – | Kabupaten Pencatat | Organization | `Organization.address.extension.extension.valueCode` |
| 101 | – | Desa | Organization | `Organization.address.extension.extension.url` |
| 103 | – | Dusun | Organization | `Organization.address.extension.url` |
| 263 | – | No Registrasi Pasien | – | `` |
| 297 | – | Tanggal Pemeriksaan Lab | – | `` |
| 298 | – | Nomor Urut Slide | – | `` |
| 299 | – | Kode Slide | – | `` |
