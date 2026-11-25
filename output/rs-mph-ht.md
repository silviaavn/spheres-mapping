# Output Form: SIM RS MPH Hipertensi

Sumber: `mapping/phdt-data-dictionary-rs-mph-ht.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-rs-mph-ht.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 20 |
| Code (`jumlah code` = 1) | 22 |
| Code unik (code + CodeSystem) | 20 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 3 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 3–29 | Patient | – | – | _NamaPasien_ → `Patient.name.text` (3, tanpa BQ)<br>_No. RM_ → `Patient.identifier.value` (6, tanpa BQ)<br>_NIK_ → `Patient.identifier.value` (9, tanpa BQ)<br>_No HP_ → `Patient.telecom` (10, tanpa BQ)<br>_Tanggal Lahir (dd mm yy)_ → `Patient.birthDate` (13, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (14, tanpa BQ)<br>_Alamat Domisili_ → `Patient.address.use` (16, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (20, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (23, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.extension.valueCode` (26, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.extension.valueCode` (29, tanpa BQ) |
| 2 | 30–36 | PractitionerRole | – | – | _Tenaga Pemeriksa_ → `PractitionerRole.code.coding` (30, tanpa BQ) |
| 3 | 37–41 | Practitioner | – | – | _NIK (Tenaga Kesehatan)_ → `Practitioner.identifier.value` (39, tanpa BQ)<br>_Nama Tenaga Kesehatan_ → `Practitioner.name.text` (41, tanpa BQ) |
| 4 | 42–71 | Encounter | – | – | _Tanggal Kunjungan (dd mm yy)_ → `Encounter.period.start` (52, tanpa BQ)<br>_Tempat Pelayanan_ → `Encounter.location.location.display` (55, tanpa BQ)<br>_Faskes yang Melayani_ → `Encounter.serviceProvider.reference` (66, tanpa BQ)<br>_Rujuk/Dikirim oleh - Jenis Faskes 1_ → `Encounter.hospitalization.admitSource.coding` (67, tanpa BQ)<br>_Rujuk/Dikirim oleh - Nama Faskes 1_ → `Encounter.hospitalization.admitSource.text` (71, tanpa BQ) |
| 5 | 72–80 | Condition | I10 | Essential (primary) hypertension | _Diagnosis utama (ICD 10)_ → `Condition.code.coding.code` (74, tanpa BQ)<br>_Tanggal tegak diagnosis (dd mm yy)_ → `Condition.onsetDateTime` (80, tanpa BQ) |
| 6 | 84–91 | Condition | – | – | _Diagnosis sekunder (ICD 10)_ → `Condition.clinicalStatus.coding` (84, tanpa BQ) |
| 7 | 95–110 | Condition | – | – | _Riwayat Penyakit dahulu_ → `Condition.clinicalStatus.coding` (95, tanpa BQ)<br>_Riwayat Penyakit sekarang_ → `Condition.clinicalStatus.coding` (103, tanpa BQ) |
| 8 | 111–122 | Observation | 424144002 | Current chronological age | _Usia_ → `Observation.valueQuantity.value` (114, tanpa BQ) |
| 9 | 123–134 | Observation | 82810-3 | Pregnancy status | _StatusHamil_ → `Observation.valueCodeableConcept.coding` (126, tanpa BQ) |
| 10 | 135–146 | Observation | 8480-6 | Systolic blood pressure | _TD (Sistolik)_ → `Observation.valueQuantity.value` (138, tanpa BQ) |
| 11 | 147–158 | Observation | 8462-4 | Diastolic blood pressure | _TD (Diastolik)_ → `Observation.valueQuantity.value` (150, tanpa BQ) |
| 12 | 164–174 | ServiceRequest | 15220000 | Laboratory test | _Pemeriksaan Laboratorium_ → `ServiceRequest.category` (164, tanpa BQ) |
| 13 | 175–181 | Specimen | 123038009 | Specimen | – |
| 14 | 182–194 | Observation | 15220000 | Laboratory test | – |
| 15 | 195–207 | DiagnosticReport | 15220000 | Laboratory test | – |
| 16 | 208–218 | Procedure | TK000028 | Diagnostic procedure | _Pemeriksaan Penunjang Lainnya_ → `Procedure.category.coding` (208, tanpa BQ) |
| 17 | 228–240 | MedicationStatement | – | – | _Riwayat Penggunaan Obat_ → `MedicationStatement.category.coding` (228, tanpa BQ)<br>_Terapi - Obat_ → `MedicationStatement.category.coding` (238, tanpa BQ) |
| 18 | 241–245 | MedicationStatement | – | – | – |
| 19 | 246–256 | Procedure | 277132007 | Therapeutic procedure | _Terapi - Tindakan_ → `Procedure.category.coding` (246, tanpa BQ) |
| 20 | 257–269 | ServiceRequest | 736286003 | Hypertension clinical management plan | _Rencana Tindak Lanjut_ → `ServiceRequest.status` (257, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 5 |
| Condition | 3 |
| ServiceRequest | 2 |
| Procedure | 2 |
| MedicationStatement | 2 |
| Patient | 1 |
| PractitionerRole | 1 |
| Practitioner | 1 |
| Encounter | 1 |
| Specimen | 1 |
| DiagnosticReport | 1 |
| **Total** | **20** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 30 | PractitionerRole | `PractitionerRole.code.coding` | 69280009 | Specialized physician | http://snomed.info/sct |
| 2 | 31 | PractitionerRole | `PractitionerRole.code.coding` | 59058001 | General physician | http://snomed.info/sct |
| 3 | 32 | PractitionerRole | `PractitionerRole.code.coding` | 309453006 | Registered midwife | http://snomed.info/sct |
| 4 | 33 | PractitionerRole | `PractitionerRole.code.coding` | 224535009 | Registered nurse | http://snomed.info/sct |
| 5 | 67 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000117 | Rujukan dari Puskesmas | http://terminology.kemkes.go.id/sp |
| 6 | 68 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000925 | Rujukan dari Klinik | http://terminology.kemkes.go.id/sp |
| 7 | 69 | Encounter | `Encounter.hospitalization.admitSource.coding` | 305956004 | Referral by physician | http://snomed.info/sct |
| 8 | 70 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000119 | Rujukan dari Rumah Sakit | http://terminology.kemkes.go.id/sp |
| 9 | 75 | Condition | `Condition.code.coding` | I10 | Essential (primary) hypertension | http://hl7.org/fhir/sid/icd-10 |
| 10 | 113 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 11 | 125 | Observation | `Observation.code.coding` | 82810-3 | Pregnancy status | http://loinc.org |
| 12 | 126 | Observation | `Observation.valueCodeableConcept.coding` | LA15173-0 | Pregnant | http://loinc.org |
| 13 | 127 | Observation | `Observation.valueCodeableConcept.coding` | LA26683-5 | Not pregnant | http://loinc.org |
| 14 | 137 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://snomed.info/sct |
| 15 | 149 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://snomed.info/sct |
| 16 | 168 | ServiceRequest | `ServiceRequest.code.coding` | 15220000 | Laboratory test | http://snomed.info/sct |
| 17 | 176 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 18 | 184 | Observation | `Observation.code.coding` | 15220000 | Laboratory test | http://snomed.info/sct |
| 19 | 197 | DiagnosticReport | `DiagnosticReport.code.coding` | 15220000 | Laboratory test | http://snomed.info/sct |
| 20 | 210 | Procedure | `Procedure.code.coding` | TK000028 | Diagnostic procedure | http://terminology.kemkes.go.id |
| 21 | 248 | Procedure | `Procedure.code.coding` | 277132007 | Therapeutic procedure | http://snomed.info/sct |
| 22 | 261 | ServiceRequest | `ServiceRequest.code.coding` | 736286003 | Hypertension clinical management plan | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 14 |
| http://terminology.kemkes.go.id/sp | 3 |
| http://loinc.org | 3 |
| http://hl7.org/fhir/sid/icd-10 | 1 |
| http://terminology.kemkes.go.id | 1 |
| **Total** | **22** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 2 | – | No | – | `` |
