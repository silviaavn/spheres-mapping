# Output Form: SIM RS Panti Nugroho Stroke

Sumber: `mapping/phdt-data-dictionary-rs-panti-nugroho-stroke.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-rs-panti-nugroho-stroke.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 20 |
| Code (`jumlah code` = 1) | 23 |
| Code unik (code + CodeSystem) | 21 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 4 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–28 | Patient | – | – | _NamaPasien_ → `Patient.name.text` (2, tanpa BQ)<br>_NRM_ → `Patient.identifier.value` (5, tanpa BQ)<br>_NIK_ → `Patient.identifier.value` (8, tanpa BQ)<br>_NoHP_ → `Patient.telecom` (9, tanpa BQ)<br>_TglLahir_ → `Patient.birthDate` (12, tanpa BQ)<br>_JenisKelamin_ → `Patient.gender` (13, tanpa BQ)<br>_AlamatDomisili_ → `Patient.address.use` (15, tanpa BQ)<br>_NamaProvinsi_ → `Patient.address.extension.extension.valueCode` (19, tanpa BQ)<br>_NamaKabupaten_ → `Patient.address.extension.extension.valueCode` (22, tanpa BQ)<br>_NamaKecamatan_ → `Patient.address.extension.extension.valueCode` (25, tanpa BQ)<br>_NamaDesa_ → `Patient.address.extension.extension.valueCode` (28, tanpa BQ) |
| 2 | 29–36 | PractitionerRole | – | – | _TenagaPemeriksa_ → `PractitionerRole.code.coding` (29, tanpa BQ) |
| 3 | 37–41 | Practitioner | – | – | _NamaTenagaKesehatan_ → `Practitioner.name` (37, tanpa BQ)<br>_NIKDokter_ → `Practitioner.identifier.value` (41, tanpa BQ) |
| 4 | 42–71 | Encounter | – | – | _TglKunjungan_ → `Encounter.period.start` (53, tanpa BQ)<br>_TempatPelayanan_ → `Encounter.location.location.display` (56, tanpa BQ)<br>_FaskesMelayani_ → `Encounter.serviceProvider.reference` (67, tanpa BQ)<br>_JenisFaskes1_ → `Encounter.hospitalization.admitSource.coding` (68, tanpa BQ)<br>_NamaFaskes1_ → `Encounter.hospitalization.admitSource.text` (71, tanpa BQ) |
| 5 | 72–82 | Condition | I64 | Stroke, not specified as haemorrhage or infarction | _KodeICD10Utama_ → `Condition.code.coding.code` (74, tanpa BQ)<br>_DiagnosisUtama_ → `Condition.code.coding.display` (75, tanpa BQ)<br>_TglTegakDiagnosis_ → `Condition.onsetDateTime` (82, tanpa BQ) |
| 6 | 86–93 | Condition | – | – | _DiagnosisSekunder_ → `Condition.clinicalStatus.coding` (86, tanpa BQ) |
| 7 | 97–112 | Condition | – | – | _RiwayatPenyakitDahulu_ → `Condition.clinicalStatus.coding` (97, tanpa BQ)<br>_RiwayatPenyakitSekarang_ → `Condition.clinicalStatus.coding` (105, tanpa BQ) |
| 8 | 113–130 | Observation | 424144002.0 | Current chronological age | _Usia_ → `Observation.valueQuantity.value` (116, tanpa BQ) |
| 9 | 131–142 | Observation | 82810-3 | Pregnancy status | _StatusHamil_ → `Observation.valueCodeableConcept.coding` (134, tanpa BQ) |
| 10 | 143–154 | Observation | 8480-6 | Systolic blood pressure | _TDSistolik_ → `Observation.valueQuantity.value` (146, tanpa BQ) |
| 11 | 155–166 | Observation | 8462-4 | Diastolic blood pressure | _TDDiastolik_ → `Observation.valueQuantity.value` (158, tanpa BQ) |
| 12 | 171–181 | ServiceRequest | 15220000.0 | Laboratory test | _PemeriksaanLaboratorium_ → `ServiceRequest.category` (171, tanpa BQ) |
| 13 | 182–188 | Specimen | 123038009.0 | Specimen | – |
| 14 | 189–201 | Observation | 15220000.0 | Laboratory test | – |
| 15 | 202–214 | DiagnosticReport | 15220000.0 | Laboratory test | – |
| 16 | 215–225 | Procedure | 80051000119107.0 | Stroke care management | _PemeriksaanPenunjangLain_ → `Procedure.category.coding` (215, tanpa BQ) |
| 17 | 235–247 | MedicationStatement | – | – | _RiwayatPenggunaanObat_ → `MedicationStatement.category.coding` (235, tanpa BQ)<br>_TerapiObat_ → `MedicationStatement.category.coding` (245, tanpa BQ) |
| 18 | 248–252 | MedicationStatement | – | – | – |
| 19 | 253–263 | Procedure | 277132007.0 | Therapeutic procedure | _TerapiTindakan_ → `Procedure.category.coding` (253, tanpa BQ) |
| 20 | 264–276 | ServiceRequest | 736251000.0 | Stroke care plan | _RencanaTindakLanjut_ → `ServiceRequest.status` (264, tanpa BQ) |

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
| 1 | 29 | PractitionerRole | `PractitionerRole.code.coding` | 69280009.0 | Specialized physician | http://snomed.info/sct |
| 2 | 31 | PractitionerRole | `PractitionerRole.code.coding` | 59058001.0 | General physician | http://snomed.info/sct |
| 3 | 32 | PractitionerRole | `PractitionerRole.code.coding` | 309453006.0 | Registered midwife | http://snomed.info/sct |
| 4 | 33 | PractitionerRole | `PractitionerRole.code.coding` | 224535009.0 | Registered nurse | http://snomed.info/sct |
| 5 | 68 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000117 | Rujukan dari Puskesmas | http://terminology.kemkes.go.id/sp |
| 6 | 69 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000925 | Rujukan dari Klinik | http://terminology.kemkes.go.id/sp |
| 7 | 70 | Encounter | `Encounter.hospitalization.admitSource.coding` | 305956004.0 | Referral by physician | http://snomed.info/sct |
| 8 | 77 | Condition | `Condition.code.coding` | I64 | Stroke, not specified as haemorrhage or infarction | http://hl7.org/fhir/sid/icd-10 |
| 9 | 115 | Observation | `Observation.code.coding` | 424144002.0 | Current chronological age | http://snomed.info/sct |
| 10 | 118 | Observation | `Observation.component.code.coding` | SP000020 | Umur Bulan | http://terminology.kemkes.go.id/sp |
| 11 | 121 | Observation | `Observation.component.code.coding` | SP000021 | Umur Hari | http://terminology.kemkes.go.id/sp |
| 12 | 133 | Observation | `Observation.code.coding` | 82810-3 | Pregnancy status | http://loinc.org |
| 13 | 134 | Observation | `Observation.valueCodeableConcept.coding` | LA15173-0 | Pregnant | http://loinc.org |
| 14 | 135 | Observation | `Observation.valueCodeableConcept.coding` | LA26683-5 | Not pregnant | http://loinc.org |
| 15 | 145 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 16 | 157 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://loinc.org |
| 17 | 175 | ServiceRequest | `ServiceRequest.code.coding` | 15220000.0 | Laboratory test | http://snomed.info/sct |
| 18 | 183 | Specimen | `Specimen.type.coding` | 123038009.0 | Specimen | http://snomed.info/sct |
| 19 | 191 | Observation | `Observation.code.coding` | 15220000.0 | Laboratory test | http://snomed.info/sct |
| 20 | 204 | DiagnosticReport | `DiagnosticReport.code.coding` | 15220000.0 | Laboratory test | http://snomed.info/sct |
| 21 | 217 | Procedure | `Procedure.code.coding` | 80051000119107.0 | Stroke care management | http://snomed.info/sct |
| 22 | 255 | Procedure | `Procedure.code.coding` | 277132007.0 | Therapeutic procedure | http://snomed.info/sct |
| 23 | 268 | ServiceRequest | `ServiceRequest.code.coding` | 736251000.0 | Stroke care plan | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 13 |
| http://loinc.org | 5 |
| http://terminology.kemkes.go.id/sp | 4 |
| http://hl7.org/fhir/sid/icd-10 | 1 |
| **Total** | **23** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
