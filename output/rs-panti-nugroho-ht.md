# Output Form: SIM RS Panti Nugroho Hipertensi

Sumber: `mapping/phdt-data-dictionary-rs-panti-nugroho-ht.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-rs-panti-nugroho-ht.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 23 |
| Code (`jumlah code` = 1) | 21 |
| Code unik (code + CodeSystem) | 19 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 4 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–35 | Patient | – | – | _NamaPasien_ → `Patient.name.text` (2, tanpa BQ)<br>_NRM_ → `Patient.identifier.value` (5, tanpa BQ)<br>_NIK_ → `Patient.identifier.value` (8, tanpa BQ)<br>_NoHP_ → `Patient.telecom` (9, tanpa BQ)<br>_TempatLahir_ → `Patient.extension:birthPlace` (12, tanpa BQ)<br>_TglLahir_ → `Patient.birthDate` (13, tanpa BQ)<br>_JenisKelamin_ → `Patient.gender` (14, tanpa BQ)<br>_AlamatDomisili_ → `Patient.address.use` (16, tanpa BQ)<br>_NamaProvinsi_ → `Patient.address.extension.extension.valueCode` (20, tanpa BQ)<br>_NamaKabupaten_ → `Patient.address.extension.extension.valueCode` (23, tanpa BQ)<br>_NamaKecamatan_ → `Patient.address.extension.extension.valueCode` (26, tanpa BQ)<br>_NamaDesa_ → `Patient.address.extension.extension.valueCode` (29, tanpa BQ)<br>_RT_ → `Patient.address.extension.extension.valueCode` (32, tanpa BQ)<br>_RW_ → `Patient.address.extension.extension.valueCode` (35, tanpa BQ) |
| 2 | 36–40 | PractitionerRole | – | – | _TenagaPemeriksa_ → `PractitionerRole.code.coding` (36, tanpa BQ) |
| 3 | 41–44 | Practitioner | – | – | _NIKDokter_ → `Practitioner.identifier.value` (43, tanpa BQ) |
| 4 | 45–70 | Encounter | – | – | _TglKunjungan_ → `Encounter.period.start` (52, tanpa BQ)<br>_TempatPelayanan_ → `Encounter.location.display` (55, tanpa BQ)<br>_FaskesMelayani_ → `Encounter.serviceProvider.reference` (66, tanpa BQ)<br>_JenisFaskes1_ → `Encounter.hospitalization.admitSource.coding` (67, tanpa BQ)<br>_"NamaFaskes1" / "AsalRujukan"_ → `Encounter.hospitalization.admitSource.text` (70, tanpa BQ) |
| 5 | 71–81 | Condition | I10 | Essential (primary) hypertension | _KodeICD10Utama_ → `Condition.code.coding.0.code` (73, tanpa BQ)<br>_DiagnosisUtama_ → `Condition.code.coding.0.display` (74, tanpa BQ)<br>_TglTegakDiagnosis_ → `Condition.onsetDateTime` (81, tanpa BQ) |
| 6 | 85–92 | Condition | – | – | _DiagnosisSekunder_ → `Condition.clinicalStatus.coding` (85, tanpa BQ) |
| 7 | 96–111 | Condition | – | – | _RiwayatPenyakitDahulu_ → `Condition.clinicalStatus.coding` (96, tanpa BQ)<br>_RiwayatPenyakitSekarang_ → `Condition.clinicalStatus.coding` (104, tanpa BQ) |
| 8 | 112–129 | Observation | 424144002.0 | Current chronological age | _Usia_ → `Observation.valueQuantity.value` (115, tanpa BQ) |
| 9 | 130–141 | Observation | 8480-6 | Systolic blood pressure | _TDSistolik_ → `Observation.valueQuantity.value` (133, tanpa BQ) |
| 10 | 142–153 | Observation | 8462-4 | Diastolic blood pressure | _TDDiastolik_ → `Observation.valueQuantity.value` (145, tanpa BQ) |
| 11 | 159–169 | ServiceRequest | 15220000.0 | Laboratory test | _HasilPemeriksaanLaboratorium_ → `ServiceRequest.category` (159, tanpa BQ) |
| 12 | 170–176 | Specimen | 123038009.0 | Specimen | – |
| 13 | 177–189 | Observation | 15220000.0 | Laboratory test | – |
| 14 | 190–202 | DiagnosticReport | 15220000.0 | Laboratory test | – |
| 15 | 203–213 | Procedure | TK000028 | Diagnostic procedure | _PemeriksaanPenunjangLain_ → `Procedure.category.coding` (203, tanpa BQ) |
| 16 | 223–235 | MedicationStatement | – | – | _RiwayatPenggunaanObat_ → `MedicationStatement.category.coding` (223, tanpa BQ)<br>_TerapiObat_ → `MedicationStatement.category.coding` (233, tanpa BQ) |
| 17 | 236–240 | MedicationStatement | – | – | – |
| 18 | 241–251 | Procedure | 277132007.0 | Therapeutic procedure | _TerapiTindakan_ → `Procedure.category.coding` (241, tanpa BQ) |
| 19 | 252–264 | ServiceRequest | 736286003.0 | Hypertension clinical management plan | _RencanaTindakLanjut_ → `ServiceRequest.status` (252, tanpa BQ) |
| 20 | 265–274 | Observation | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | _GDS_Tertinggi_ → `Observation.status` (265, tanpa BQ) |
| 21 | 275–284 | Observation | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | _GDP_Tertinggi_ → `Observation.status` (275, tanpa BQ) |
| 22 | 285–293 | Observation | 4548-4 | Hemoglobin A1c/Hemoglobin.total in Blood | _HBA1C_Tertinggi_ → `Observation.status` (285, tanpa BQ) |
| 23 | 294–305 | Coverage | – | – | _Penjamin_ → `Coverage.type.coding` (296, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 7 |
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
| Coverage | 1 |
| **Total** | **23** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 36 | PractitionerRole | `PractitionerRole.code.coding` | 69280009.0 | Specialized physician | http://snomed.info/sct |
| 2 | 37 | PractitionerRole | `PractitionerRole.code.coding` | 59058001.0 | General physician | http://snomed.info/sct |
| 3 | 67 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000117 | Rujukan dari Puskesmas | http://terminology.kemkes.go.id/sp |
| 4 | 68 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000925 | Rujukan dari Klinik | http://terminology.kemkes.go.id/sp |
| 5 | 69 | Encounter | `Encounter.hospitalization.admitSource.coding` | 305956004.0 | Referral by physician | http://snomed.info/sct |
| 6 | 76 | Condition | `Condition.code.coding` | I10 | Essential (primary) hypertension | http://hl7.org/fhir/sid/icd-10 |
| 7 | 114 | Observation | `Observation.code.coding` | 424144002.0 | Current chronological age | http://snomed.info/sct |
| 8 | 117 | Observation | `Observation.component.code.coding` | SP000020 | Umur Bulan | http://terminology.kemkes.go.id/sp |
| 9 | 120 | Observation | `Observation.component.code.coding` | SP000021 | Umur Hari | http://terminology.kemkes.go.id/sp |
| 10 | 132 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://snomed.info/sct |
| 11 | 144 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://snomed.info/sct |
| 12 | 163 | ServiceRequest | `ServiceRequest.code.coding` | 15220000.0 | Laboratory test | http://snomed.info/sct |
| 13 | 171 | Specimen | `Specimen.type.coding` | 123038009.0 | Specimen | http://snomed.info/sct |
| 14 | 179 | Observation | `Observation.code.coding` | 15220000.0 | Laboratory test | http://snomed.info/sct |
| 15 | 192 | DiagnosticReport | `DiagnosticReport.code.coding` | 15220000.0 | Laboratory test | http://snomed.info/sct |
| 16 | 205 | Procedure | `Procedure.code.coding` | TK000028 | Diagnostic procedure | http://terminology.kemkes.go.id |
| 17 | 243 | Procedure | `Procedure.code.coding` | 277132007.0 | Therapeutic procedure | http://snomed.info/sct |
| 18 | 256 | ServiceRequest | `ServiceRequest.code.coding` | 736286003.0 | Hypertension clinical management plan | http://snomed.info/sct |
| 19 | 267 | Observation | `Observation.code.coding` | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 20 | 277 | Observation | `Observation.code.coding` | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 21 | 287 | Observation | `Observation.code.coding` | 4548-4 | Hemoglobin A1c/Hemoglobin.total in Blood | http://loinc.org |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 12 |
| http://terminology.kemkes.go.id/sp | 4 |
| http://loinc.org | 3 |
| http://hl7.org/fhir/sid/icd-10 | 1 |
| http://terminology.kemkes.go.id | 1 |
| **Total** | **21** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
