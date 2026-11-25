# Output Form: SIM RS Goetoeng Hipertensi

Sumber: `mapping/phdt-data-dictionary-rs-goetoeng-ht.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-rs-goetoeng-ht.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 5 |
| Code (`jumlah code` = 1) | 3 |
| Code unik (code + CodeSystem) | 3 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 0 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 3–12 | Patient | – | – | _Nama_ → `Patient.name.text` (3, tanpa BQ)<br>_NIK_ → `Patient.identifier.value` (6, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (7, tanpa BQ)<br>_Alamat_ → `Patient.address.use` (8, tanpa BQ)<br>_No HP_ → `Patient.telecom` (10, tanpa BQ) |
| 2 | 14–38 | Encounter | – | – | _Keterangan - Tgl Masuk_ → `Encounter.period.start` (21, tanpa BQ)<br>_Keterangan - Unit_ → `Encounter.location.location.display` (24, tanpa BQ)<br>_Rujukan_ → `Encounter.hospitalization.dischargeDisposition.text` (38, tanpa BQ) |
| 3 | 39–47 | Condition | I10 | Essential (primary) hypertension | _Hasil_ → `Condition.note` (47, tanpa BQ) |
| 4 | 48–59 | Observation | 8480-6 | Systolic blood pressure | _Hasil Pemeriksaan Tensi Darah - Sistol_ → `Observation.valueQuantity.value` (51, tanpa BQ) |
| 5 | 60–71 | Observation | 8462-4 | Diastolic blood pressure | _Hasil Pemeriksaan Tensi Darah - Diastol_ → `Observation.valueQuantity.value` (63, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 2 |
| Patient | 1 |
| Encounter | 1 |
| Condition | 1 |
| **Total** | **5** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 41 | Condition | `Condition.code.coding` | I10 | Essential (primary) hypertension | http://hl7.org/fhir/sid/icd-10 |
| 2 | 50 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://snomed.info/sct |
| 3 | 62 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 2 |
| http://hl7.org/fhir/sid/icd-10 | 1 |
| **Total** | **3** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 2 | – | No | – | `` |
| 13 | – | Keterangan - Bulan | – | `` |
