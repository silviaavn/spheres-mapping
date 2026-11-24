# Output Form: SIM RS Goetoeng PNC

Sumber: `mapping/phdt-data-dictionary-rs-goetoeng-pnc.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-rs-goetoeng-pnc.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 9 |
| Code (`jumlah code` = 1) | 21 |
| Code unik (code + CodeSystem) | 21 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 11 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–3 | Practitioner | – | – | _Nama Dokter_ → `Practitioner.name.text` (2, tanpa BQ) |
| 2 | 4–25 | Patient | – | – | _NIK_ → `Patient.identifier[0].value` (6, tanpa BQ)<br>_Nomor Rekam Medis_ → `Patient.identifier[1].value` (9, tanpa BQ)<br>_Nama Pasien_ → `Patient.name.text` (11, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (12, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (14, tanpa BQ)<br>_Kabupaten/Kota_ → `Patient.address.extension.extension.valueCode` (19, tanpa BQ)<br>_Kecamatan_ → `Patient.address.extension.extension.valueCode` (22, tanpa BQ)<br>_Kelurahan_ → `Patient.address.extension.extension.valueCode` (25, tanpa BQ) |
| 3 | 26–66 | Encounter | – | – | _Nomor Pendaftaran_ → `Encounter.identifier.value` (28, tanpa BQ)<br>_Waktu Kunjungan_ → `Encounter.period.start` (30, tanpa BQ)<br>_Nama Klinik/Instalasi_ → `Encounter.location.location.display` (47, tanpa BQ)<br>_Asal Rujukan_ → `Encounter.hospitalization.admitSource.coding` (49, tanpa BQ) |
| 4 | 67–101 | Condition | – | – | _Diagnosa Utama (ICD-10)_ → `Condition.code.coding` (67, tanpa BQ)<br>_Diagnosa Sekunder 1_ → `Condition.code.coding.code` (74, tanpa BQ)<br>_Diagnosa Sekunder 2_ → `Condition.code.coding.code` (81, tanpa BQ)<br>_Diagnosa Sekunder 3_ → `Condition.code.coding.code` (88, tanpa BQ)<br>_Diagnosa Sekunder 4_ → `Condition.code.coding.code` (95, tanpa BQ) |
| 5 | 102–110 | Observation | 184061005.0 | Patient registration status | _Status Pendaftaran (Baru/Lama)_ → `Observation.valueCodeableConcept.coding` (104, tanpa BQ) |
| 6 | 111–119 | Observation | SP000815 | Jenis Kasus Pasien | _Jenis Kasus (Baru/Lama)_ → `Observation.valueCodeableConcept.coding` (113, tanpa BQ) |
| 7 | 120–134 | Observation | 82589-3 | Highest level of education | _Pendidikan Terakhir_ → `Observation.valueCodeableConcept.coding` (122, tanpa BQ) |
| 8 | 135–149 | Observation | 424144002.0 | Current chronological age | _Umur (Tahun)_ → `Observation.valueQuantity.value` (137, tanpa BQ)<br>_Umur (Bulan)_ → `Observation.component[bulan].valueQuantity.value` (140, tanpa BQ)<br>_Umur (Hari)_ → `Observation.component[hari].valueQuantity.value` (143, tanpa BQ) |
| 9 | 150–164 | Coverage | – | – | _Nomor JKN/BPJS_ → `Coverage.identifier.value` (153, tanpa BQ)<br>_Jenis Pembiayaan_ → `Coverage.payor.reference` (155, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 4 |
| Practitioner | 1 |
| Patient | 1 |
| Encounter | 1 |
| Condition | 1 |
| Coverage | 1 |
| **Total** | **9** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 49 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000117 | Rujukan dari Puskesmas | http://terminology.kemkes.go.id/sp |
| 2 | 50 | Encounter | `Encounter.hospitalization.admitSource.coding` | 1991000124105.0 | Referred by self | http://snomed.info/sct |
| 3 | 51 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000814 | Rujukan dari Dokter Praktik Mandiri | http://terminology.kemkes.go.id/sp |
| 4 | 102 | Observation | `Observation.code.coding` | 184061005.0 | Patient registration status | http://snomed.info/sct |
| 5 | 104 | Observation | `Observation.valueCodeableConcept.coding` | SP000812 | Pasien Baru | http://terminology.kemkes.go.id/sp |
| 6 | 105 | Observation | `Observation.valueCodeableConcept.coding` | SP000813 | Pasien Lama | http://terminology.kemkes.go.id/sp |
| 7 | 111 | Observation | `Observation.code.coding` | SP000815 | Jenis Kasus Pasien | http://terminology.kemkes.go.id/sp |
| 8 | 113 | Observation | `Observation.valueCodeableConcept.coding` | SP000816 | Kasus Baru | http://terminology.kemkes.go.id/sp |
| 9 | 114 | Observation | `Observation.valueCodeableConcept.coding` | SP000817 | Kasus Lama | http://terminology.kemkes.go.id/sp |
| 10 | 120 | Observation | `Observation.code.coding` | 82589-3 | Highest level of education | http://loinc.org |
| 11 | 122 | Observation | `Observation.valueCodeableConcept.coding` | 473463000.0 | Received elementary school education | http://snomed.info/sct |
| 12 | 123 | Observation | `Observation.valueCodeableConcept.coding` | 603435002.0 | Educated to junior high school level | http://snomed.info/sct |
| 13 | 124 | Observation | `Observation.valueCodeableConcept.coding` | 603434003.0 | Educated to senior high school level | http://snomed.info/sct |
| 14 | 125 | Observation | `Observation.valueCodeableConcept.coding` | 38861000087100.0 | Bachelor's degree achieved | http://snomed.info/sct |
| 15 | 126 | Observation | `Observation.valueCodeableConcept.coding` | 741725004.0 | Primary school started but not finished | http://snomed.info/sct |
| 16 | 127 | Observation | `Observation.valueCodeableConcept.coding` | SP000277 | D3 | http://terminology.kemkes.go.id/sp |
| 17 | 128 | Observation | `Observation.valueCodeableConcept.coding` | SP000834 | D1/D2 | http://terminology.kemkes.go.id/sp |
| 18 | 129 | Observation | `Observation.valueCodeableConcept.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 19 | 135 | Observation | `Observation.code.coding` | 424144002.0 | Current chronological age | http://snomed.info/sct |
| 20 | 139 | Observation | `Observation.component[bulan].code.coding` | SP000020 | Umur Bulan | http://terminology.kemkes.go.id/sp |
| 21 | 142 | Observation | `Observation.component[hari].code.coding` | SP000021 | Umur Hari | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://terminology.kemkes.go.id/sp | 11 |
| http://snomed.info/sct | 9 |
| http://loinc.org | 1 |
| **Total** | **21** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 165 | – | ? | – | `` |
