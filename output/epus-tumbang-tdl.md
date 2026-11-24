# Output Form: ePuskesmas Tumbuh Kembang - TDL

Sumber: `mapping/phdt-data-dictionary-epus-tumbang-tdl.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-epus-tumbang-tdl.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 4 |
| Code (`jumlah code` = 1) | 8 |
| Code unik (code + CodeSystem) | 5 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 0 |
| Variabel BQ (unik) | 0 |
| Variabel raw (variabel dictionary; belum ada file mentah) | 6 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–30 | Observation | 863888006 | 6/60 visual acuity of left eye | _Arah kaki E ke 1_ → `Observation.component.code.coding` (9, tanpa BQ)<br>_Arah kaki E ke 2_ → `Observation.component.code.coding` (12, tanpa BQ)<br>_Arah kaki E ke 3_ → `Observation.component.code.coding` (15, tanpa BQ)<br>_Arah kaki E ke 4_ → `Observation.component.code.coding` (18, tanpa BQ)<br>_Arah kaki E ke 5_ → `Observation.component.code.coding` (21, tanpa BQ) |
| 2 | 31–59 | Observation | 863887001 | 6/60 visual acuity of right eye | _Arah kaki E ke 1_ → `Observation.component.code.coding` (38, tanpa BQ)<br>_Arah kaki E ke 2_ → `Observation.component.code.coding` (41, tanpa BQ)<br>_Arah kaki E ke 3_ → `Observation.component.code.coding` (44, tanpa BQ)<br>_Arah kaki E ke 4_ → `Observation.component.code.coding` (47, tanpa BQ)<br>_Arah kaki E ke 5_ → `Observation.component.code.coding` (50, tanpa BQ) |
| 3 | 60–88 | Observation | 836333004 | 6/12 visual acuity of left eye | _Arah kaki E ke 1_ → `Observation.component.code.coding` (67, tanpa BQ)<br>_Arah kaki E ke 2_ → `Observation.component.code.coding` (70, tanpa BQ)<br>_Arah kaki E ke 3_ → `Observation.component.code.coding` (73, tanpa BQ)<br>_Arah kaki E ke 4_ → `Observation.component.code.coding` (76, tanpa BQ)<br>_Arah kaki E ke 5_ → `Observation.component.code.coding` (79, tanpa BQ) |
| 4 | 89–117 | Observation | 836332009 | 6/12 visual acuity of right eye | _Arah kaki E ke 1_ → `Observation.component.code.coding` (96, tanpa BQ)<br>_Arah kaki E ke 2_ → `Observation.component.code.coding` (99, tanpa BQ)<br>_Arah kaki E ke 3_ → `Observation.component.code.coding` (102, tanpa BQ)<br>_Arah kaki E ke 4_ → `Observation.component.code.coding` (105, tanpa BQ)<br>_Arah kaki E ke 5_ → `Observation.component.code.coding` (108, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 4 |
| **Total** | **4** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 4 | Observation | `Observation.code.coding` | 863888006 | 6/60 visual acuity of left eye | http://snomed.info/sct |
| 2 | 8 | Observation | `Observation.method.coding` | 400911007 | Tumbling E test | http://snomed.info/sct |
| 3 | 33 | Observation | `Observation.code.coding` | 863887001 | 6/60 visual acuity of right eye | http://snomed.info/sct |
| 4 | 37 | Observation | `Observation.method.coding` | 400911007 | Tumbling E test | http://snomed.info/sct |
| 5 | 62 | Observation | `Observation.code.coding` | 836333004 | 6/12 visual acuity of left eye | http://snomed.info/sct |
| 6 | 66 | Observation | `Observation.method.coding` | 400911007 | Tumbling E test | http://snomed.info/sct |
| 7 | 91 | Observation | `Observation.code.coding` | 836332009 | 6/12 visual acuity of right eye | http://snomed.info/sct |
| 8 | 95 | Observation | `Observation.method.coding` | 400911007 | Tumbling E test | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 8 |
| **Total** | **8** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 118 | – | Interpretasi | – | `` |
