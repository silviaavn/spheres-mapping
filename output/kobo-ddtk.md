# Output Form: Kobo DDTK

Sumber: `mapping/phdt-data-dictionary-kobo-ddtk.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-kobo-ddtk.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 11 |
| Code (`jumlah code` = 1) | 10 |
| Code unik (code + CodeSystem) | 10 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 0 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–10 | Patient | – | – | _Nama Siswa_ → `Patient.name.text` (2, tanpa BQ)<br>_NIK Siswa_ → `Patient.identifier.value` (5, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (7, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (9, tanpa BQ)<br>_Tempat lahir_ → `Patient.extension:birthPlace.valueAddress.text` (10, tanpa BQ) |
| 2 | 11–21 | RelatedPerson | – | – | _Nama Ibu_ → `RelatedPerson.name.text` (12, tanpa BQ)<br>_No Hp Ibu_ → `RelatedPerson.telecom.value` (14, tanpa BQ)<br>_NIK Ibu_ → `RelatedPerson.identifier.value` (20, tanpa BQ) |
| 3 | 22–30 | RelatedPerson | – | – | _Nama Ayah_ → `RelatedPerson.name.text` (22, tanpa BQ)<br>_No Hp Ayah_ → `RelatedPerson.telecom.value` (24, tanpa BQ)<br>_NIK Ayah_ → `RelatedPerson.identifier.value` (30, tanpa BQ) |
| 4 | 73–80 | PractitionerRole | – | – | _Tenaga Pemeriksa_ → `PractitionerRole.active` (73, tanpa BQ) |
| 5 | 81–86 | Practitioner | – | – | _Nama Tenaga Pemeriksa_ → `Practitioner.name.text` (83, tanpa BQ)<br>_Jenis Kelamin Tenaga Pemeriksa_ → `Practitioner.gender` (84, tanpa BQ) |
| 6 | 87–98 | Observation | 8287-5 | Head Occipital-frontal circumference by Tape measure | _Lingkar Kepala Saat Ini_ → `Observation.valueQuantity.value` (90, tanpa BQ) |
| 7 | 99–109 | Observation | 284473002 | Mid upper arm circumference | _LILA saat ini_ → `Observation.status` (99, tanpa BQ) |
| 8 | 110–121 | Observation | 29463-7 | Body weight | _Berat Badan_ → `Observation.valueQuantity.value` (113, tanpa BQ) |
| 9 | 122–133 | Observation | 8306-3 | Body height --lying | _Tinggi Badan_ → `Observation.valueQuantity.value` (125, tanpa BQ) |
| 10 | 134–147 | Encounter | – | – | _Tanggal Kunjungan/Pengukuran_ → `Encounter.identifier` (134, tanpa BQ) |
| 11 | 148–154 | Condition | 170245002 | Child examination: school screening | – |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 4 |
| RelatedPerson | 2 |
| Patient | 1 |
| PractitionerRole | 1 |
| Practitioner | 1 |
| Encounter | 1 |
| Condition | 1 |
| **Total** | **11** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 75 | PractitionerRole | `PractitionerRole.code.coding` | 106304008 | Teacher | http://snomed.info/sct |
| 2 | 76 | PractitionerRole | `PractitionerRole.code.coding` | 158922001 | Physical training teacher | http://snomed.info/sct |
| 3 | 77 | PractitionerRole | `PractitionerRole.code.coding` | 309453006 | Registered midwife | http://snomed.info/sct |
| 4 | 78 | PractitionerRole | `PractitionerRole.code.coding` | 309343006 | Physician | http://snomed.info/sct |
| 5 | 79 | PractitionerRole | `PractitionerRole.code.coding` | 224535009 | Registered nurse | http://snomed.info/sct |
| 6 | 89 | Observation | `Observation.code.coding` | 8287-5 | Head Occipital-frontal circumference by Tape measure | http://loinc.org |
| 7 | 101 | Observation | `Observation.code.coding` | 284473002 | Mid upper arm circumference | http://snomed.info/sct |
| 8 | 112 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 9 | 124 | Observation | `Observation.code.coding` | 8306-3 | Body height --lying | http://loinc.org |
| 10 | 150 | Condition | `Condition.code.coding` | 170245002 | Child examination: school screening | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 7 |
| http://loinc.org | 3 |
| **Total** | **10** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 34 | – | Sekolah yang melayani | Organization | `Organization.name` |
