# Output Form: SIM RS MPH Diabetes Melitus

Sumber: `mapping/phdt-data-dictionary-rs-mph-dm.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-rs-mph-dm.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 24 |
| Code (`jumlah code` = 1) | 37 |
| Code unik (code + CodeSystem) | 26 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 3 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 3–29 | Patient | – | – | _NamaPasien_ → `Patient.name.text` (3, tanpa BQ)<br>_No. RM_ → `Patient.identifier.value` (6, tanpa BQ)<br>_NIK_ → `Patient.identifier.value` (9, tanpa BQ)<br>_No HP_ → `Patient.telecom` (10, tanpa BQ)<br>_Tanggal Lahir (dd mm yy)_ → `Patient.birthDate` (13, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (14, tanpa BQ)<br>_Alamat Domisili_ → `Patient.address.use` (16, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (20, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (23, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.extension.valueCode` (26, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.extension.valueCode` (29, tanpa BQ) |
| 2 | 30–34 | PractitionerRole | – | – | _Tenaga Pemeriksa_ → `PractitionerRole.code.coding` (30, tanpa BQ) |
| 3 | 35–39 | Practitioner | – | – | _NIK (Tenaga Kesehatan)_ → `Practitioner.identifier.value` (37, tanpa BQ)<br>_Nama Tenaga Kesehatan_ → `Practitioner.name.text` (39, tanpa BQ) |
| 4 | 40–69 | Encounter | – | – | _Tanggal Kunjungan (dd mm yy)_ → `Encounter.period.start` (50, tanpa BQ)<br>_Tempat Pelayanan_ → `Encounter.location.location.display` (53, tanpa BQ)<br>_Faskes yang Melayani_ → `Encounter.serviceProvider.reference` (64, tanpa BQ)<br>_Rujuk/Dikirim oleh - Jenis Faskes 1_ → `Encounter.hospitalization.admitSource.coding` (65, tanpa BQ)<br>_Rujuk/Dikirim oleh - Nama Faskes 1_ → `Encounter.hospitalization.admitSource.text` (69, tanpa BQ) |
| 5 | 70–79 | Condition | E14 | Unspecified diabetes mellitus | _Diagnosis utama_ → `Condition.code.coding.code` (73, tanpa BQ)<br>_Tanggal tegak diagnosis_ → `Condition.onsetDateTime` (79, tanpa BQ) |
| 6 | 83–91 | Condition | – | – | _Diagnosis sekunder_ → `Condition.clinicalStatus.coding` (83, tanpa BQ) |
| 7 | 95–110 | Condition | – | – | _Riwayat Penyakit dahulu_ → `Condition.clinicalStatus.coding` (95, tanpa BQ)<br>_Riwayat Penyakit sekarang_ → `Condition.clinicalStatus.coding` (103, tanpa BQ) |
| 8 | 111–122 | Observation | 424144002 | Current chronological age | _Usia_ → `Observation.valueQuantity.value` (114, tanpa BQ) |
| 9 | 123–134 | Observation | 82810-3 | Pregnancy status | _StatusHamil_ → `Observation.valueCodeableConcept.coding` (126, tanpa BQ) |
| 10 | 135–146 | Observation | 8480-6 | Systolic blood pressure | _TD (Sistolik)_ → `Observation.valueQuantity.value` (138, tanpa BQ) |
| 11 | 147–158 | Observation | 8462-4 | Diastolic blood pressure | _TD (Diastolik)_ → `Observation.valueQuantity.value` (150, tanpa BQ) |
| 12 | 173–181 | PractitionerRole | – | – | _Tenaga Pemeriksa_ → `PractitionerRole.practitioner.reference` (173, tanpa BQ) |
| 13 | 182–186 | Practitioner | – | – | _NIK (Tenaga Kesehatan Pemeriksaan Laboratorium)_ → `Practitioner.identifier.value` (184, tanpa BQ)<br>_Nama Tenaga Kesehatan Pemeriksaan Laboratorium_ → `Practitioner.name.text` (186, tanpa BQ) |
| 14 | 187–201 | ServiceRequest | 15220000 | Laboratory test | _Jenis pemeriksaan_ → `ServiceRequest.code.coding` (191, tanpa BQ)<br>_Tanggal Kunjungan (pemeriksaan laboratorium)_ → `ServiceRequest.occurrenceDateTime` (199, tanpa BQ) |
| 15 | 202–208 | Specimen | 123038009 | Specimen | – |
| 16 | 209–224 | Observation | 15220000 | Laboratory test | _Hasil pemeriksaan_ → `Observation.valueString` (217, tanpa BQ) |
| 17 | 225–228 | DiagnosticReport | 15220000 | Laboratory test | – |
| 18 | 229–232 | Observation | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | – |
| 19 | 233–242 | DiagnosticReport | – | – | _Rencana Tindak Lanjut (pemeriksaan laboratorium)_ → `DiagnosticReport.conclusion` (237, tanpa BQ) |
| 20 | 243–253 | Procedure | TK000028 | Diagnostic procedure | _Pemeriksaan Penunjang Lainnya_ → `Procedure.category.coding` (243, tanpa BQ) |
| 21 | 263–273 | MedicationStatement | – | – | _Riwayat Penggunaan Obat_ → `MedicationStatement.category.coding` (263, tanpa BQ)<br>_Terapi - Obat_ → `MedicationStatement.category.coding` (271, tanpa BQ) |
| 22 | 274–278 | MedicationStatement | – | – | – |
| 23 | 279–289 | Procedure | 277132007 | Therapeutic procedure | _Terapi - Tindakan_ → `Procedure.category.coding` (279, tanpa BQ) |
| 24 | 290–302 | ServiceRequest | 736284000 | Diabetes clinical management plan | _Rencana Tindak Lanjut_ → `ServiceRequest.status` (290, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 6 |
| Condition | 3 |
| PractitionerRole | 2 |
| Practitioner | 2 |
| ServiceRequest | 2 |
| DiagnosticReport | 2 |
| Procedure | 2 |
| MedicationStatement | 2 |
| Patient | 1 |
| Encounter | 1 |
| Specimen | 1 |
| **Total** | **24** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 30 | PractitionerRole | `PractitionerRole.code.coding` | 69280009 | Specialized physician | http://snomed.info/sct |
| 2 | 31 | PractitionerRole | `PractitionerRole.code.coding` | 59058001 | General physician | http://snomed.info/sct |
| 3 | 65 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000117 | Rujukan dari Puskesmas | http://terminology.kemkes.go.id/sp |
| 4 | 66 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000925 | Rujukan dari Klinik | http://terminology.kemkes.go.id/sp |
| 5 | 67 | Encounter | `Encounter.hospitalization.admitSource.coding` | 305956004 | Referral by physician | http://snomed.info/sct |
| 6 | 68 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000119 | Rujukan dari Rumah Sakit | http://terminology.kemkes.go.id/sp |
| 7 | 74 | Condition | `Condition.code.coding` | E14 | Unspecified diabetes mellitus | http://hl7.org/fhir/sid/icd-10 |
| 8 | 113 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 9 | 125 | Observation | `Observation.code.coding` | 82810-3 | Pregnancy status | http://loinc.org |
| 10 | 126 | Observation | `Observation.valueCodeableConcept.coding` | LA15173-0 | Pregnant | http://loinc.org |
| 11 | 127 | Observation | `Observation.valueCodeableConcept.coding` | LA26683-5 | Not pregnant | http://loinc.org |
| 12 | 137 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://snomed.info/sct |
| 13 | 149 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://snomed.info/sct |
| 14 | 177 | PractitionerRole | `PractitionerRole.code.coding` | 69280009 | Specialized physician | http://snomed.info/sct |
| 15 | 178 | PractitionerRole | `PractitionerRole.code.coding` | 309343006 | Physician | http://snomed.info/sct |
| 16 | 179 | PractitionerRole | `PractitionerRole.code.coding` | 309453006 | Registered midwife | http://snomed.info/sct |
| 17 | 180 | PractitionerRole | `PractitionerRole.code.coding` | 224535009 | Registered nurse | http://snomed.info/sct |
| 18 | 181 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002 | Laboratory worker | http://snomed.info/sct |
| 19 | 191 | ServiceRequest | `ServiceRequest.code.coding` | 15220000 | Laboratory test | http://snomed.info/sct |
| 20 | 193 | ServiceRequest | `ServiceRequest.code.coding` | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 21 | 194 | ServiceRequest | `ServiceRequest.code.coding` | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 22 | 195 | ServiceRequest | `ServiceRequest.code.coding` | 4548-4 | Hemoglobin A1c/Hemoglobin.total in Blood | http://loinc.org |
| 23 | 196 | ServiceRequest | `ServiceRequest.code.coding` | 113076002 | Glucose tolerance test | http://snomed.info/sct |
| 24 | 203 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 25 | 211 | Observation | `Observation.code.coding` | 15220000 | Laboratory test | http://snomed.info/sct |
| 26 | 213 | Observation | `Observation.code.coding` | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 27 | 214 | Observation | `Observation.code.coding` | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 28 | 215 | Observation | `Observation.code.coding` | 4548-4 | Hemoglobin A1c/Hemoglobin.total in Blood | http://loinc.org |
| 29 | 216 | Observation | `Observation.code.coding` | 113076002 | Glucose tolerance test | http://snomed.info/sct |
| 30 | 227 | DiagnosticReport | `DiagnosticReport.code.coding` | 15220000 | Laboratory test | http://snomed.info/sct |
| 31 | 229 | Observation | `DiagnosticReport.code.coding` | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 32 | 230 | Observation | `DiagnosticReport.code.coding` | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 33 | 231 | Observation | `DiagnosticReport.code.coding` | 4548-4 | Hemoglobin A1c/Hemoglobin.total in Blood | http://loinc.org |
| 34 | 232 | Observation | `DiagnosticReport.code.coding` | 113076002 | Glucose tolerance test | http://snomed.info/sct |
| 35 | 245 | Procedure | `Procedure.code.coding` | TK000028 | Diagnostic procedure | http://terminology.kemkes.go.id |
| 36 | 281 | Procedure | `Procedure.code.coding` | 277132007 | Therapeutic procedure | http://snomed.info/sct |
| 37 | 294 | ServiceRequest | `ServiceRequest.code.coding` | 736284000 | Diabetes clinical management plan | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 20 |
| http://loinc.org | 12 |
| http://terminology.kemkes.go.id/sp | 3 |
| http://hl7.org/fhir/sid/icd-10 | 1 |
| http://terminology.kemkes.go.id | 1 |
| **Total** | **37** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 2 | – | No | – | `` |
| 159 | – | No. RM | – | `` |
| 160 | – | NIK | – | `` |
| 161 | – | No HP | – | `` |
| 162 | – | Tanggal Lahir | – | `` |
| 163 | – | Usia | – | `` |
| 164 | – | Jenis Kelamin | – | `` |
| 165 | – | Status Hamil | – | `` |
| 166 | – | Alamat Domisili | – | `` |
| 167 | – | Nama Provinsi | – | `` |
| 168 | – | Nama Kabupaten | – | `` |
| 169 | – | Nama Kecamatan | – | `` |
| 170 | – | Nama Desa | – | `` |
| 171 | – | Dokter perujuk | – | `` |
| 172 | – | Klinik rajal perujuk | – | `` |
