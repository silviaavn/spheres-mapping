# Output Form: SIM RS Siaga Medika Hepatitis

Sumber: `mapping/phdt-data-dictionary-rs-siaga-medika-hepatitis.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-rs-siaga-medika-hepatitis.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 20 |
| Code (`jumlah code` = 1) | 22 |
| Code unik (code + CodeSystem) | 15 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 0 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–28 | Patient | – | – | _Nama Pasien_ → `Patient.name.text` (2, tanpa BQ)<br>_No. RM_ → `Patient.identifier.value` (5, tanpa BQ)<br>_NIK_ → `Patient.identifier.value` (8, tanpa BQ)<br>_No HP_ → `Patient.telecom` (9, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (12, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (13, tanpa BQ)<br>_Alamat Domisili_ → `Patient.address.use` (15, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (19, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (22, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.extension.valueCode` (25, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.extension.valueCode` (28, tanpa BQ) |
| 2 | 29–35 | PractitionerRole | – | – | _Tenaga Pemeriksa (DPJP)_ → `PractitionerRole.code.coding` (29, tanpa BQ) |
| 3 | 36–40 | Practitioner | – | – | _NIK Tenaga Pemeriksa (DPJP)_ → `Practitioner.identifier.value` (38, tanpa BQ)<br>_Nama Tenaga Pemeriksa (DPJP)_ → `Practitioner.name.text` (40, tanpa BQ) |
| 4 | 41–64 | Encounter | – | – | _Tanggal Kunjungan_ → `Encounter.period.start` (48, tanpa BQ)<br>_Tempat Pelayanan_ → `Encounter.location.location.display` (51, tanpa BQ)<br>_Faskes yang Melayani_ → `Encounter.serviceProvider.reference` (62, tanpa BQ)<br>_Rujuk/Dikirim oleh - Nama Faskes 1_ → `Encounter.hospitalization.admitSource.text` (64, tanpa BQ) |
| 5 | 65–74 | Condition | B19 | Unspecified viral hepatitis | _Diagnosis utama (ICD10)_ → `Condition.code.coding.code` (68, tanpa BQ)<br>_Tanggal tegak diagnosis_ → `Condition.onsetDateTime` (74, tanpa BQ) |
| 6 | 78–87 | Condition | B19 | Unspecified viral hepatitis | _Diagnosis sekunder (ICD10)_ → `Condition.code.text` (82, tanpa BQ) |
| 7 | 91–108 | Condition | – | – | _Riwayat Penyakit dahulu_ → `Condition.identifier.value` (91, tanpa BQ)<br>_Riwayat Penyakit sekarang_ → `Condition.identifier.value` (100, tanpa BQ) |
| 8 | 109–120 | Observation | 424144002 | Current chronological age | _Usia_ → `Observation.valueQuantity.value` (112, tanpa BQ) |
| 9 | 121–132 | Observation | 82810-3 | Pregnancy status | _Status Hamil_ → `Observation.valueCodeableConcept.coding` (124, tanpa BQ) |
| 10 | 147–154 | PractitionerRole | – | – | _Tenaga Pemeriksa (Lab)_ → `PractitionerRole.code.coding` (151, tanpa BQ) |
| 11 | 155–159 | Practitioner | – | – | _NIK Tenaga Pemeriksa (Lab)_ → `Practitioner.identifier.value` (157, tanpa BQ)<br>_Nama Tenaga Pemeriksa (Lab)_ → `Practitioner.name.text` (159, tanpa BQ) |
| 12 | 160–170 | ServiceRequest | 15220000 | Laboratory test | _Jenis pemeriksaan_ → `ServiceRequest.code.text` (165, tanpa BQ)<br>_Tanggal Pemeriksaan_ → `ServiceRequest.occurrenceDateTime` (168, tanpa BQ) |
| 13 | 171–176 | Specimen | 123038009 | Specimen | – |
| 14 | 177–188 | Observation | 15220000 | Laboratory test | _Hasil pemeriksaan_ → `Observation.valueString` (181, tanpa BQ) |
| 15 | 189–202 | DiagnosticReport | 15220000 | Laboratory test | _Rencana Tindak Lanjut (pemeriksaan laboratorium)_ → `DiagnosticReport.conclusion` (197, tanpa BQ) |
| 16 | 203–213 | Procedure | TK000028 | Diagnostic procedure | _Pemeriksaan Penunjang Lainnya_ → `Procedure.category.coding` (203, tanpa BQ) |
| 17 | 223–233 | MedicationStatement | – | – | _Riwayat Penggunaan Obat_ → `MedicationStatement.category.coding` (223, tanpa BQ)<br>_Terapi - Obat_ → `MedicationStatement.category.coding` (231, tanpa BQ) |
| 18 | 234–238 | MedicationStatement | – | – | – |
| 19 | 239–249 | Procedure | 277132007 | Therapeutic procedure | _Terapi - Tindakan_ → `Procedure.category.coding` (239, tanpa BQ) |
| 20 | 250–261 | ServiceRequest | 1285318003 | Viral hepatitis disease management program | _Rencana Tindak Lanjut_ → `ServiceRequest.status` (250, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Condition | 3 |
| Observation | 3 |
| PractitionerRole | 2 |
| Practitioner | 2 |
| ServiceRequest | 2 |
| Procedure | 2 |
| MedicationStatement | 2 |
| Patient | 1 |
| Encounter | 1 |
| Specimen | 1 |
| DiagnosticReport | 1 |
| **Total** | **20** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 29 | PractitionerRole | `PractitionerRole.code.coding` | 309453006 | Registered midwife | http://snomed.info/sct |
| 2 | 30 | PractitionerRole | `PractitionerRole.code.coding` | 309343006 | Physician | http://snomed.info/sct |
| 3 | 31 | PractitionerRole | `PractitionerRole.code.coding` | 69280009 | Specialized physician | http://snomed.info/sct |
| 4 | 32 | PractitionerRole | `PractitionerRole.code.coding` | 224535009 | Registered nurse | http://snomed.info/sct |
| 5 | 69 | Condition | `Condition.code.coding` | B19 | Unspecified viral hepatitis | http://hl7.org/fhir/sid/icd-10 |
| 6 | 81 | Condition | `Condition.code.coding` | B19 | Unspecified viral hepatitis | http://hl7.org/fhir/sid/icd-10 |
| 7 | 111 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 8 | 123 | Observation | `Observation.code.coding` | 82810-3 | Pregnancy status | http://loinc.org |
| 9 | 124 | Observation | `Observation.valueCodeableConcept.coding` | LA15173-0 | Pregnant | http://loinc.org |
| 10 | 125 | Observation | `Observation.valueCodeableConcept.coding` | LA26683-5 | Not pregnant | http://loinc.org |
| 11 | 147 | PractitionerRole | `PractitionerRole.code.coding` | 69280009 | Specialized physician | http://snomed.info/sct |
| 12 | 148 | PractitionerRole | `PractitionerRole.code.coding` | 309343006 | Physician | http://snomed.info/sct |
| 13 | 149 | PractitionerRole | `PractitionerRole.code.coding` | 309453006 | Registered midwife | http://snomed.info/sct |
| 14 | 150 | PractitionerRole | `PractitionerRole.code.coding` | 224535009 | Registered nurse | http://snomed.info/sct |
| 15 | 151 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002 | Laboratory worker | http://snomed.info/sct |
| 16 | 164 | ServiceRequest | `ServiceRequest.code.coding` | 15220000 | Laboratory test | http://snomed.info/sct |
| 17 | 172 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 18 | 179 | Observation | `Observation.code.coding` | 15220000 | Laboratory test | http://snomed.info/sct |
| 19 | 191 | DiagnosticReport | `DiagnosticReport.code.coding` | 15220000 | Laboratory test | http://snomed.info/sct |
| 20 | 205 | Procedure | `Procedure.code.coding` | TK000028 | Diagnostic procedure | http://terminology.kemkes.go.id |
| 21 | 241 | Procedure | `Procedure.code.coding` | 277132007 | Therapeutic procedure | http://snomed.info/sct |
| 22 | 254 | ServiceRequest | `ServiceRequest.code.coding` | 1285318003 | Viral hepatitis disease management program | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 16 |
| http://loinc.org | 3 |
| http://hl7.org/fhir/sid/icd-10 | 2 |
| http://terminology.kemkes.go.id | 1 |
| **Total** | **22** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 63 | – | Rujuk/Dikirim oleh - Jenis Faskes 1 | – | `` |
| 133 | – | No. RM | – | `` |
| 134 | – | NIK | – | `` |
| 135 | – | No HP | – | `` |
| 136 | – | Tanggal Lahir | – | `` |
| 137 | – | Usia | – | `` |
| 138 | – | Jenis Kelamin | – | `` |
| 139 | – | Status Hamil | – | `` |
| 140 | – | Alamat Domisili | – | `` |
| 141 | – | Nama Provinsi | – | `` |
| 142 | – | Nama Kabupaten | – | `` |
| 143 | – | Nama Kecamatan | – | `` |
| 144 | – | Nama Desa | – | `` |
| 145 | – | Dokter perujuk | – | `` |
| 146 | – | Klinik rajal perujuk | – | `` |
