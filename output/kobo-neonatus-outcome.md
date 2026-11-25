# Output Form: Kobo Neonatus Outcome

Sumber: `mapping/phdt-data-dictionary-kobo-neonatus-outcome.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-kobo-neonatus-outcome.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 14 |
| Code (`jumlah code` = 1) | 25 |
| Code unik (code + CodeSystem) | 25 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 5 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–4 | PractitionerRole | – | – | – |
| 2 | 5–7 | Practitioner | – | – | _Nama yang melakukan entry data_ → `Practitioner.name.text` (5, tanpa BQ)<br>_NIK yang melakukan entry data_ → `Practitioner.identifier` (6, tanpa BQ) |
| 3 | 8–15 | Patient | – | – | _Nama Bayi_ → `Patient.name.text` (8, tanpa BQ)<br>_NIK Bayi_ → `Patient.identifier.value` (11, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (13, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (15, tanpa BQ)<br>_Kembar_ → `Patient.multipleBirthBoolean` (32, tanpa BQ)<br>_Alamat Domisili_ → `Patient.address.use` (45, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.url` (49, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.url` (52, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.url` (55, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.url` (58, tanpa BQ)<br>_RW_ → `Patient.address.extension.url` (61, tanpa BQ)<br>_RT_ → `Patient.address.extension.url` (64, tanpa BQ) |
| 4 | 16–31 | Observation | 72150-6 | Delivery location | _Tempat lahir_ → `Observation.valueCodeableConcept.coding` (19, tanpa BQ)<br>_Nama Tempat Melahirkan_ → `Observation.note.text` (31, tanpa BQ) |
| 5 | 33–44 | Observation | 246435002 | Number of fetuses | _Jumlah bayi kembar_ → `Observation.valueInteger` (37, tanpa BQ) |
| 6 | 67–77 | RelatedPerson | – | – | _Nama Ibu_ → `RelatedPerson.name.text` (68, tanpa BQ)<br>_No Hp Ibu_ → `RelatedPerson.telecom.value` (70, tanpa BQ)<br>_NIK Ibu_ → `RelatedPerson.identifier.value` (76, tanpa BQ) |
| 7 | 78–86 | RelatedPerson | – | – | _Nama Ayah_ → `RelatedPerson.name.text` (78, tanpa BQ)<br>_No Hp Ayah_ → `RelatedPerson.telecom.value` (80, tanpa BQ)<br>_NIK Ayah_ → `RelatedPerson.identifier.value` (86, tanpa BQ) |
| 8 | 136–143 | EpisodeOfCare | Neonate | Neonate | – |
| 9 | 144–158 | Observation | 249222005 | Neonatal condition | – |
| 10 | 159–174 | Observation | 424144002 | Current chronological age | – |
| 11 | 175–186 | Observation | 81956-5 | Date and time of death [TimeStamp] | – |
| 12 | 187–198 | Observation | 79378-6 | Cause of death | – |
| 13 | 199–210 | Observation | LT000005 | Alamat Mati | – |
| 14 | 211–224 | Observation | 39016-1 | Age at death | – |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 8 |
| RelatedPerson | 2 |
| PractitionerRole | 1 |
| Practitioner | 1 |
| Patient | 1 |
| EpisodeOfCare | 1 |
| **Total** | **14** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 2 | PractitionerRole | `PractitionerRole.code.coding` | 223366009 | Healthcare professional | http://snomed.info/sct |
| 2 | 3 | PractitionerRole | `PractitionerRole.code.coding` | SP000396 | Data entry staff | http://terminology.kemkes.go.id/sp |
| 3 | 4 | PractitionerRole | `PractitionerRole.code.coding` | SP000397 | Field/call center staff | http://terminology.kemkes.go.id/sp |
| 4 | 18 | Observation | `Observation.code.coding` | 72150-6 | Delivery location | http://loinc.org |
| 5 | 19 | Observation | `Observation.valueCodeableConcept.coding` | 264362003 | Home | http://snomed.info/sct |
| 6 | 20 | Observation | `Observation.valueCodeableConcept.coding` | 104 | Rumah Sakit | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 7 | 21 | Observation | `Observation.valueCodeableConcept.coding` | 102 | Pusat Kesehatan Masyarakat | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 8 | 22 | Observation | `Observation.valueCodeableConcept.coding` | 103 | Klinik | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 9 | 23 | Observation | `Observation.valueCodeableConcept.coding` | OT000004 | Bidan Praktek Mandiri | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 10 | 35 | Observation | `Observation.code.coding` | 246435002 | Number of fetuses | http://snomed.info/sct |
| 11 | 36 | Observation | `Observation.code.coding` | ANC.B8.DE109 | Number of fetuses | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 12 | 139 | EpisodeOfCare | `EpisodeOfCare.type.coding` | Neonate | Neonate | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 13 | 146 | Observation | `Observation.code.coding` | 249222005 | Neonatal condition | http://snomed.info/sct |
| 14 | 147 | Observation | `Observation.valueCodeableConcept.coding` | 102500002 | Good neonatal condition at birth | http://snomed.info/sct |
| 15 | 148 | Observation | `Observation.valueCodeableConcept.coding` | 276707008 | Infant in poor condition at birth | http://snomed.info/sct |
| 16 | 149 | Observation | `Observation.valueCodeableConcept.coding` | 419099009 | Dead | http://snomed.info/sct |
| 17 | 157 | Observation | `Observation.component.code.coding` | 22925008 | Neonatal disorder | http://snomed.info/sct |
| 18 | 161 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 19 | 162 | Observation | `Observation.component.code.coding` | SP000715 | Umur Minggu | http://terminology.kemkes.go.id/sp |
| 20 | 165 | Observation | `Observation.component.code.coding` | SP000021 | Umur Hari | http://terminology.kemkes.go.id/sp |
| 21 | 177 | Observation | `Observation.code.coding` | 81956-5 | Date and time of death [TimeStamp] | http://loinc.org |
| 22 | 189 | Observation | `Observation.code.coding` | 79378-6 | Cause of death | http://loinc.org |
| 23 | 201 | Observation | `Observation.code.coding` | LT000005 | Alamat Mati | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 24 | 213 | Observation | `Observation.code.coding` | 39016-1 | Age at death | http://loinc.org |
| 25 | 216 | Observation | `Observation.component.code.coding` | SP000719 | Umur Minggu (saat meninggal) | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 9 |
| http://terminology.kemkes.go.id/sp | 5 |
| http://loinc.org | 4 |
| http://terminology.kemkes.go.id/CodeSystem/organization-type | 4 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 1 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 1 |
| http://terminology.kemkes.go.id/CodeSystem/location-type | 1 |
| **Total** | **25** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 90 | – | Jenis Faskes | Organization | `Organization.type` |
| 94 | – | Faskes yang melayani | Organization | `Organization.name` |
