# Output Form: SIM RS Goetoeng Diabetes Melitus

Sumber: `mapping/phdt-data-dictionary-rs-goetoeng-dm.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-rs-goetoeng-dm.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 6 |
| Code (`jumlah code` = 1) | 4 |
| Code unik (code + CodeSystem) | 4 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 0 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 3–12 | Patient | – | – | _Nama_ → `Patient.name.text` (3, tanpa BQ)<br>_NIK_ → `Patient.identifier.value` (6, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (7, tanpa BQ)<br>_Alamat_ → `Patient.address.use` (8, tanpa BQ)<br>_No HP_ → `Patient.telecom` (10, tanpa BQ) |
| 2 | 13–36 | Encounter | – | – | _Keterangan - Tgl Masuk_ → `Encounter.period.start` (20, tanpa BQ)<br>_Keterangan - Unit_ → `Encounter.location.display` (23, tanpa BQ) |
| 3 | 37–45 | Condition | E14 | Unspecified diabetes mellitus | _Hasil_ → `Condition.note` (45, tanpa BQ) |
| 4 | 46–55 | Observation | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | _Hasil Pemeriksaan Gula Darah - GDS_ → `Observation.status` (46, tanpa BQ) |
| 5 | 56–65 | Observation | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | _Hasil Pemeriksaan Gula Darah - GDP_ → `Observation.status` (56, tanpa BQ) |
| 6 | 66–74 | Observation | 4548-4 | Hemoglobin A1c/Hemoglobin.total in Blood | _Hasil Pemeriksaan Gula Darah - HbA1C_ → `Observation.status` (66, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 3 |
| Patient | 1 |
| Encounter | 1 |
| Condition | 1 |
| **Total** | **6** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 39 | Condition | `Condition.code.coding` | E14 | Unspecified diabetes mellitus | http://hl7.org/fhir/sid/icd-10 |
| 2 | 48 | Observation | `Observation.code.coding` | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 3 | 58 | Observation | `Observation.code.coding` | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 4 | 68 | Observation | `Observation.code.coding` | 4548-4 | Hemoglobin A1c/Hemoglobin.total in Blood | http://loinc.org |

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
| 2 | – | No | – | `` |
