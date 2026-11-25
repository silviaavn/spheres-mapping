# Output Form: KuApps BidanKu - Daftar Kehamilan

Sumber: `mapping/phdt-data-dictionary-kuapps-bidanku-daftar-kehamilan.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-kuapps-bidanku-daftar-kehamilan.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 12 |
| Code (`jumlah code` = 1) | 32 |
| Code unik (code + CodeSystem) | 32 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 6 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–13 | Observation | SP000132 | Memiliki Buku KIA | _Apakah Anda memiliki buku KIA Ibu hamil?_ → `Observation.valueBoolean` (5, tanpa BQ) |
| 2 | 14–24 | Observation | 3401000175105 | Total number of prenatal care visits | _Jumlah kunjungan ke fasilitas kesehatan sejauh ini_ → `Observation.valueInteger` (17, tanpa BQ) |
| 3 | 25–37 | Observation | 8665-2 | Last menstrual period start date | _Apakah HPHT diketahui?_ → `Observation.status` (25, tanpa BQ)<br>_HPHT_ → `Observation.valueDateTime` (30, tanpa BQ) |
| 4 | 38–53 | Observation | 18185-9 | Gestational age | _Usia kehamilan-minggu_ → `Observation.valueQuantity.value` (42, tanpa BQ)<br>_Usia kehamilan-hari_ → `Observation.component.code.coding` (44, tanpa BQ) |
| 5 | 54–65 | Observation | 32418-6 | Obstetric trimester Stated | _Trimester_ → `Observation.valueInteger` (58, tanpa BQ) |
| 6 | 66–77 | Observation | 11778-8 | Delivery date Estimated | _HPL_ → `Observation.valueDateTime` (70, tanpa BQ) |
| 7 | 78–92 | Observation | 883-9 | ABO group [Type] in Blood | _Apa golongan darah Ibu?_ → `Observation.valueCodeableConcept.coding` (82, tanpa BQ) |
| 8 | 93–105 | Observation | 10331-7 | Rh [Type] in Blood | _Apa faktor Rh Ibu?_ → `Observation.valueCodeableConcept.coding` (97, tanpa BQ) |
| 9 | 106–117 | Observation | SP000462 | Ibu hamil sudah membuat rencana cara pergi ke rumah sakit untuk persalinan | _Sudah membuat rencana cara pergi ke rumah sakit untuk persalinan?_ → `Observation.valueBoolean` (109, tanpa BQ) |
| 10 | 118–133 | Observation | SP000497 | Rencana moda transportasi yang akan digunakan untuk persalinan di fasilitas kesehatan | _Bagaimana Ibu hamil akan berangkat ke fasilitas?_ → `Observation.valueCodeableConcept.coding` (121, tanpa BQ) |
| 11 | 134–145 | Observation | SP000463 | Ibu hamil punya dukungan keluarga untuk rencana persalinan | _Punya dukungan keluarga untuk rencana persalinan?_ → `Observation.valueBoolean` (137, tanpa BQ) |
| 12 | 146–157 | Observation | SP000464 | Ibu hamil sudah memiliki persiapan untuk melakukan ASI Eksklusif selama 6 bulan | _Apakah Ibu hamil sudah memiliki persiapan untuk melakukan ASI eksklusif selama 6 bulan?_ → `Observation.valueBoolean` (149, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 12 |
| **Total** | **12** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 4 | Observation | `Observation.code.coding` | SP000132 | Memiliki Buku KIA | http://terminology.kemkes.go.id/sp |
| 2 | 16 | Observation | `Observation.code.coding` | 3401000175105 | Total number of prenatal care visits | http://snomed.info/sct |
| 3 | 27 | Observation | `Observation.code.coding` | 8665-2 | Last menstrual period start date | http://loinc.org |
| 4 | 28 | Observation | `Observation.code.coding` | ANC.B6.DE14 | Last menstrual period (LMP) date | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 5 | 29 | Observation | `Observation.dataAbsentReason.coding` | unknown | Unknown | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 6 | 40 | Observation | `Observation.code.coding` | 18185-9 | Gestational age | http://loinc.org |
| 7 | 41 | Observation | `Observation.code.coding` | ANC.B6.DE17 | Gestational age | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 8 | 44 | Observation | `Observation.component.code.coding` | SP000461 | Usia Kehamilan (Hari) | http://terminology.kemkes.go.id/sp |
| 9 | 56 | Observation | `Observation.code.coding` | 32418-6 | Obstetric trimester Stated | http://loinc.org |
| 10 | 57 | Observation | `Observation.code.coding` | ANC.SS.DE13 | Trimester ke | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 11 | 68 | Observation | `Observation.code.coding` | 11778-8 | Delivery date Estimated | http://loinc.org |
| 12 | 69 | Observation | `Observation.code.coding` | ANC.B6.DE22 | Expected date of delivery (EDD) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 13 | 80 | Observation | `Observation.code.coding` | 883-9 | ABO group [Type] in Blood | http://loinc.org |
| 14 | 81 | Observation | `Observation.code.coding` | ANC.B9.DE24 | Blood type | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 15 | 82 | Observation | `Observation.valueCodeableConcept.coding` | LA19710-5 | Group A | http://loinc.org |
| 16 | 83 | Observation | `Observation.valueCodeableConcept.coding` | LA19709-7 | Group B | http://loinc.org |
| 17 | 84 | Observation | `Observation.valueCodeableConcept.coding` | LA19708-9 | Group O | http://loinc.org |
| 18 | 85 | Observation | `Observation.valueCodeableConcept.coding` | LA28449-9 | Group AB | http://loinc.org |
| 19 | 95 | Observation | `Observation.code.coding` | 10331-7 | Rh [Type] in Blood | http://loinc.org |
| 20 | 96 | Observation | `Observation.code.coding` | ANC.B9.DE29 | Rh factor | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 21 | 97 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 22 | 98 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 23 | 108 | Observation | `Observation.code.coding` | SP000462 | Ibu hamil sudah membuat rencana cara pergi ke rumah sakit untuk persalinan | http://terminology.kemkes.go.id/sp |
| 24 | 120 | Observation | `Observation.code.coding` | SP000497 | Rencana moda transportasi yang akan digunakan untuk persalinan di fasilitas kesehatan | http://terminology.kemkes.go.id/sp |
| 25 | 121 | Observation | `Observation.valueCodeableConcept.coding` | 870595007 | Walking | http://snomed.info/sct |
| 26 | 122 | Observation | `Observation.valueCodeableConcept.coding` | 22674006 | Motor bus, device | http://snomed.info/sct |
| 27 | 123 | Observation | `Observation.valueCodeableConcept.coding` | 70224005 | Bicycle, device | http://snomed.info/sct |
| 28 | 124 | Observation | `Observation.valueCodeableConcept.coding` | 90748009 | Motorcycle, device | http://snomed.info/sct |
| 29 | 125 | Observation | `Observation.valueCodeableConcept.coding` | 71783008 | Automobile, device | http://snomed.info/sct |
| 30 | 126 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 31 | 136 | Observation | `Observation.code.coding` | SP000463 | Ibu hamil punya dukungan keluarga untuk rencana persalinan | http://terminology.kemkes.go.id/sp |
| 32 | 148 | Observation | `Observation.code.coding` | SP000464 | Ibu hamil sudah memiliki persiapan untuk melakukan ASI Eksklusif selama 6 bulan | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://loinc.org | 12 |
| http://snomed.info/sct | 7 |
| http://terminology.kemkes.go.id/sp | 6 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 5 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 1 |
| http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes | 1 |
| **Total** | **32** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
