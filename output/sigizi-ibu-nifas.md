# Output Form: SiGizi Ibu Nifas

Sumber: `mapping/phdt-data-dictionary-sigizi-ibu-nifas.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-sigizi-ibu-nifas.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 11 |
| Code (`jumlah code` = 1) | 12 |
| Code unik (code + CodeSystem) | 12 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 3 |
| Variabel BQ (unik) | 14 |
| Variabel raw (variabel dictionary; belum ada file mentah) | 14 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–24 | Patient | – | – | `nama` → `Patient.name.text` (2)<br>`nik` → `Patient.identifier.value` (5)<br>`tgl_lahir` → `Patient.birthDate` (8)<br>_Alamat_ → `Patient.address.use` (9, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.url` (13, tanpa BQ)<br>`prov` → `Patient.address.extension.extension.valueCode` (15)<br>_Nama Kabupaten_ → `Patient.address.extension.url` (16, tanpa BQ)<br>`kabkota` → `Patient.address.extension.extension.valueCode` (18)<br>_Nama Kecamatan_ → `Patient.address.extension.url` (19, tanpa BQ)<br>`kec` → `Patient.address.extension.extension.valueCode` (21)<br>_Nama Desa_ → `Patient.address.extension.url` (22, tanpa BQ)<br>`desakel` → `Patient.address.extension.extension.valueCode` (24) |
| 2 | 110–133 | EpisodeOfCare | ANC | Antenatal Care | _Episode ANC Ibu_ → `EpisodeOfCare.identifier` (110, tanpa BQ)<br>`tgl_hpht` → `EpisodeOfCare.period.start` (112)<br>_Tanggal Melahirkan atau Tanggal Abortus_ → `EpisodeOfCare.period.end` (115, tanpa BQ)<br>_Tanggal HPHT_ → `EpisodeOfCare.statusHistory.period.start` (117, tanpa BQ)<br>_Tanggal Melahirkan atau Tanggal Abortus_ → `EpisodeOfCare.statusHistory.period.end` (120, tanpa BQ)<br>_Tanggal Melahirkan atau Tanggal Abortus_ → `EpisodeOfCare.statusHistory.period.start` (124, tanpa BQ)<br>_Tanggal Melahirkan atau Tanggal Abortus_ → `EpisodeOfCare.statusHistory.period.end` (127, tanpa BQ)<br>_Episode PNC Ibu_ → `EpisodeOfCare.identifier` (133, tanpa BQ) |
| 3 | 134–146 | EpisodeOfCare | PNC | Postnatal Care | `tgl_melahirkan` → `EpisodeOfCare.period.start` (138)<br>_Tanggal Melahirkan_ → `EpisodeOfCare.statusHistory.period.start` (142, tanpa BQ) |
| 4 | 147–163 | Encounter | – | – | `posyandu` → `Encounter.location.location.reference` (159) 🔎 lookup master data<br>`puskesmas` → `Encounter.serviceProvider.reference` (163) 🔎 lookup master data |
| 5 | 164–172 | Condition | 386337006 | Intrapartal care | – |
| 6 | 184–194 | Observation | 8665-2 | Last menstrual period start date | _Tanggal HPHT_ → `Observation.valueDateTime` (187, tanpa BQ) |
| 7 | 195–205 | Observation | 93857-1 | Date and time of obstetric delivery | _Tanggal dan Jam Persalinan_ → `Observation.valueDateTime` (198, tanpa BQ) |
| 8 | 206–216 | Procedure | 236973005 | Delivery procedure | _Prosedur Persalinan_ → `Procedure.status` (206, tanpa BQ)<br>`status` → `Procedure.code.coding` (208) |
| 9 | 217–227 | Observation | SP000724 | Tanggal Abortus | _Tanggal Abortus_ → `Observation.status` (217, tanpa BQ)<br>`tgl_abortus` → `Observation.valueDateTime` (220) |
| 10 | 228–238 | Procedure | 386639001 | Termination of pregnancy | _Prosedur Abortus_ → `Procedure.status` (228, tanpa BQ) |
| 11 | 239–249 | Procedure | SP000683 | Tatalaksana Tindakan | `tindakan` → `Procedure.status` (239) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 3 |
| Procedure | 3 |
| EpisodeOfCare | 2 |
| Patient | 1 |
| Encounter | 1 |
| Condition | 1 |
| **Total** | **11** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 128 | EpisodeOfCare | `EpisodeOfCare.type.coding` | ANC | Antenatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 2 | 134 | EpisodeOfCare | `EpisodeOfCare.type.coding` | PNC | Postnatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 3 | 166 | Condition | `Condition.code.coding` | 386337006 | Intrapartal care | http://snomed.info/sct |
| 4 | 167 | Condition | `Condition.code.coding` | SP000725 | Abortus | http://terminology.kemkes.go.id/sp |
| 5 | 186 | Observation | `Observation.code.coding` | 8665-2 | Last menstrual period start date | http://loinc.org |
| 6 | 197 | Observation | `Observation.code.coding` | 93857-1 | Date and time of obstetric delivery | http://loinc.org |
| 7 | 208 | Procedure | `Procedure.code.coding` | 236973005 | Delivery procedure | http://snomed.info/sct |
| 8 | 209 | Procedure | `Procedure.code.coding` | 73.59 | Other manually assisted delivery | http://hl7.org/fhir/sid/icd-9-cm |
| 9 | 219 | Observation | `Observation.code.coding` | SP000724 | Tanggal Abortus | http://terminology.kemkes.go.id/sp |
| 10 | 230 | Procedure | `Procedure.code.coding` | 386639001 | Termination of pregnancy | http://snomed.info/sct |
| 11 | 231 | Procedure | `Procedure.code.coding` | 69.51 | Aspiration curettage of uterus for termination of pregnancy | http://hl7.org/fhir/sid/icd-9-cm |
| 12 | 241 | Procedure | `Procedure.code.coding` | SP000683 | Tatalaksana Tindakan | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 3 |
| http://terminology.kemkes.go.id/sp | 3 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 2 |
| http://loinc.org | 2 |
| http://hl7.org/fhir/sid/icd-9-cm | 2 |
| **Total** | **12** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
