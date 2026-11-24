# Output Form: SISMAL - Validasi Kasus Indigenous

Sumber: `mapping/phdt-data-dictionary-sismal-validasi-indigenous.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-sismal-validasi-indigenous.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 7 |
| Code (`jumlah code` = 1) | 12 |
| Code unik (code + CodeSystem) | 12 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 6 |
| Variabel BQ (unik) | 0 |
| Variabel raw (variabel dictionary; belum ada file mentah) | 14 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–5 | Patient | – | – | _Nama Pasien_ → `Patient.name.text` (3, tanpa BQ) |
| 2 | 43–67 | Encounter | – | – | _Tanggal Wawancara Kasus_ → `Encounter.period.start` (51, tanpa BQ)<br>_Fasyankes yang melakukan PE_ → `Encounter.serviceProvider.reference` (66, tanpa BQ)<br>_Fasyankes Pencatat_ → `Encounter.hospitalization.origin.reference` (67, tanpa BQ) |
| 3 | 68–77 | Condition | B54 | Unspecified malaria | _Kekambuhan_ → `Condition.clinicalStatus.coding` (68, tanpa BQ)<br>_Status Validasi_ → `Condition.verificationStatus.coding` (70, tanpa BQ) |
| 4 | 78–84 | Location | – | – | _Alamat Asal Penularan_ → `Location.address.line` (82, tanpa BQ)<br>_Titik Koordinat Penularan_ → `Location.position.latitude` (83, tanpa BQ) |
| 5 | 85–94 | Procedure | 225368008 | Contact tracing | _Kontak Survey_ → `Procedure.status` (85, tanpa BQ)<br>_Tanggal Survey Kontak_ → `Procedure.performedDateTime` (92, tanpa BQ) |
| 6 | 95–107 | Observation | 409496000 | Mode of transmission | _Asal Penularan_ → `Observation.valueCodeableConcept.coding` (98, tanpa BQ) |
| 7 | 108–122 | Observation | SP000740 | Kategori Wilayah Penularan | _Penularan_ → `Observation.valueCodeableConcept.coding` (111, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 2 |
| Patient | 1 |
| Encounter | 1 |
| Condition | 1 |
| Location | 1 |
| Procedure | 1 |
| **Total** | **7** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 73 | Condition | `Condition.code.coding` | B54 | Unspecified malaria | http://hl7.org/fhir/sid/icd-10 |
| 2 | 88 | Procedure | `Procedure.code.coding` | 225368008 | Contact tracing | http://snomed.info/sct |
| 3 | 97 | Observation | `Observation.code.coding` | 409496000 | Mode of transmission | http://snomed.info/sct |
| 4 | 98 | Observation | `Observation.valueCodeableConcept.coding` | 418427004 | Vector-borne transmission | http://snomed.info/sct |
| 5 | 99 | Observation | `Observation.valueCodeableConcept.coding` | 418912005 | Transfusion transmission | http://snomed.info/sct |
| 6 | 100 | Observation | `Observation.valueCodeableConcept.coding` | 417409004 | Transplacental transmission | http://snomed.info/sct |
| 7 | 110 | Observation | `Observation.code.coding` | SP000740 | Kategori Wilayah Penularan | http://terminology.kemkes.go.id/sp |
| 8 | 111 | Observation | `Observation.valueCodeableConcept.coding` | SP000741 | Dalam Wilayah Puskesmas | http://terminology.kemkes.go.id/sp |
| 9 | 112 | Observation | `Observation.valueCodeableConcept.coding` | SP000742 | Luar Wilayah Puskesmas | http://terminology.kemkes.go.id/sp |
| 10 | 113 | Observation | `Observation.valueCodeableConcept.coding` | SP000743 | Luar Wilayah Kabupaten/Kota | http://terminology.kemkes.go.id/sp |
| 11 | 114 | Observation | `Observation.valueCodeableConcept.coding` | SP000744 | Luar Wilayah Provinsi | http://terminology.kemkes.go.id/sp |
| 12 | 115 | Observation | `Observation.valueCodeableConcept.coding` | SP000745 | Luar Wilayah Negara | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://terminology.kemkes.go.id/sp | 6 |
| http://snomed.info/sct | 5 |
| http://hl7.org/fhir/sid/icd-10 | 1 |
| **Total** | **12** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 14 | – | Provinsi | Organization | `Organization.address.extension.extension.valueCode` |
| 17 | – | Kabupaten/Kota | Organization | `Organization.address.extension.extension.valueCode` |
