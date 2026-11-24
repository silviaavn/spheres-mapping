# Output Form: SIM RS Panti Nugroho Diabetes Melitus

Sumber: `mapping/phdt-data-dictionary-rs-panti-nugroho-dm.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-rs-panti-nugroho-dm.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 7 |
| Code (`jumlah code` = 1) | 4 |
| Code unik (code + CodeSystem) | 4 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 0 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–23 | Patient | – | – | _NRM_ → `Patient.identifier.value` (4, tanpa BQ)<br>_NamaPasien_ → `Patient.name.text` (5, tanpa BQ)<br>_NoKTP_ → `Patient.identifier.value` (8, tanpa BQ)<br>_TempatLahir_ → `Patient.extension:birthPlace` (9, tanpa BQ)<br>_TglLahir_ → `Patient.birthDate` (10, tanpa BQ)<br>_AlamatPasien_ → `Patient.address.use` (11, tanpa BQ)<br>_RT_ → `Patient.address.extension.extension.valueCode` (15, tanpa BQ)<br>_RW_ → `Patient.address.extension.extension.valueCode` (18, tanpa BQ)<br>_NamaJK_ → `Patient.gender` (19, tanpa BQ)<br>_NoHP_ → `Patient.telecom` (21, tanpa BQ) |
| 2 | 24–48 | Encounter | – | – | _TglReg_ → `Encounter.period.start` (31, tanpa BQ)<br>_NamaBagian_ → `Encounter.location.display` (34, tanpa BQ)<br>_AsalRujukan_ → `Encounter.hospitalization.admitSource.text` (48, tanpa BQ) |
| 3 | 49–59 | Condition | E14 | Unspecified diabetes mellitus | _KodeICD10_ → `Condition.code.coding.0.code` (51, tanpa BQ)<br>_NamaICD10_ → `Condition.code.coding.0.display` (52, tanpa BQ) |
| 4 | 60–71 | Coverage | – | – | _Penjamin_ → `Coverage.type.coding` (62, tanpa BQ) |
| 5 | 72–81 | Observation | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | _GDS_Tertinggi_ → `Observation.status` (72, tanpa BQ) |
| 6 | 82–91 | Observation | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | _GDP_Tertinggi_ → `Observation.status` (82, tanpa BQ) |
| 7 | 92–100 | Observation | 4548-4 | Hemoglobin A1c/Hemoglobin.total in Blood | _HBA1C_Tertinggi_ → `Observation.status` (92, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 3 |
| Patient | 1 |
| Encounter | 1 |
| Condition | 1 |
| Coverage | 1 |
| **Total** | **7** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 54 | Condition | `Condition.code.coding` | E14 | Unspecified diabetes mellitus | http://hl7.org/fhir/sid/icd-10 |
| 2 | 74 | Observation | `Observation.code.coding` | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 3 | 84 | Observation | `Observation.code.coding` | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 4 | 94 | Observation | `Observation.code.coding` | 4548-4 | Hemoglobin A1c/Hemoglobin.total in Blood | http://loinc.org |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://loinc.org | 3 |
| http://hl7.org/fhir/sid/icd-10 | 1 |
| **Total** | **4** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
