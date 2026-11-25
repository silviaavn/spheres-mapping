# Output Form: Genomics - Dengue

Sumber: `mapping/phdt-data-dictionary-genomics-dengue.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-genomics-dengue.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 12 |
| Code (`jumlah code` = 1) | 22 |
| Code unik (code + CodeSystem) | 20 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 5 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–34 | Patient | – | – | _Nama_ → `Patient.name.text` (2, tanpa BQ)<br>_NIK_ → `Patient.identifier.value` (5, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (7, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (9, tanpa BQ)<br>_Nomor HP_ → `Patient.telecom` (10, tanpa BQ)<br>_Alamat Domisili_ → `Patient.address.use` (13, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (19, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (22, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.extension.valueCode` (25, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.extension.valueCode` (28, tanpa BQ)<br>_Latitude_ → `Patient.address.extension.extension.valueString` (31, tanpa BQ)<br>_Longitude_ → `Patient.address.extension.extension.valueString` (34, tanpa BQ) |
| 2 | 79–82 | PractitionerRole | – | – | _Tenaga Pemeriksa_ → `PractitionerRole.active` (79, tanpa BQ) |
| 3 | 84–98 | Encounter | – | – | – |
| 4 | 99–105 | Condition | – | – | – |
| 5 | 116–123 | Specimen | – | – | _Tanggal Pemeriksaan_ → `Specimen.collection.collectedDateTime` (119, tanpa BQ)<br>_Nama Pasien_ → `Specimen.subject.display` (121, tanpa BQ)<br>_Tanggal Pemeriksaan_ → `Specimen.receivedTime` (123, tanpa BQ) |
| 6 | 124–133 | ServiceRequest | – | – | – |
| 7 | 134–156 | Observation | 69548-6 | Genetic variant assessment | _Gene Identifier_ → `Observation.component.code.coding` (149, tanpa BQ)<br>_Protein Level Change_ → `Observation.component.code.coding` (155, tanpa BQ) |
| 8 | 157–169 | Observation | 86206-0 | Whole genome sequence analysis in Blood or Tissue by Molecular genetics method | _Sequence Length_ → `Observation.component.code.coding` (162, tanpa BQ)<br>_Completeness (N content)_ → `Observation.component.code.coding` (166, tanpa BQ) |
| 9 | 170–178 | Observation | 31343-7 | Dengue virus Ab [Presence] in Specimen | – |
| 10 | 180–197 | DiagnosticReport | – | – | _Report Status_ → `DiagnosticReport.status` (180, tanpa BQ)<br>_Performer Name_ → `DiagnosticReport.subject.reference` (183, tanpa BQ)<br>_Report Date_ → `DiagnosticReport.effectiveDateTime` (185, tanpa BQ)<br>_Performer Contact_ → `DiagnosticReport.performer.reference` (188, tanpa BQ)<br>_Summary_ → `DiagnosticReport.conclusion` (192, tanpa BQ) |
| 11 | 198–231 | Observation | SP000682 | Core genome MLST [Type] in Isolate by Sequencing | _cgMLST_ → `Observation.valueCodeableConcept.coding` (198, tanpa BQ)<br>_Loci Called_ → `Observation.component.code.coding` (220, tanpa BQ)<br>_Total Loci in Schema_ → `Observation.component.code.coding` (224, tanpa BQ)<br>_Call Rate_ → `Observation.component.code.coding` (228, tanpa BQ) |
| 12 | 232–243 | DiagnosticReport | – | – | _Report Status_ → `DiagnosticReport.status` (232, tanpa BQ)<br>_Performer Name_ → `DiagnosticReport.subject.reference` (235, tanpa BQ)<br>_Report Date_ → `DiagnosticReport.effectiveDateTime` (237, tanpa BQ)<br>_Performer Contact_ → `DiagnosticReport.performer.reference` (240, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 4 |
| DiagnosticReport | 2 |
| Patient | 1 |
| PractitionerRole | 1 |
| Encounter | 1 |
| Condition | 1 |
| Specimen | 1 |
| ServiceRequest | 1 |
| **Total** | **12** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 81 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002.0 | Laboratory Worker | http://snomed.info/sct |
| 2 | 117 | Specimen | `Specimen.type` | 119334006.0 | Sputum specimen | http://snomed.info/sct |
| 3 | 128 | ServiceRequest | `ServiceRequest.code` | 69548-6 | Genetic variant assessment | http://loinc.org |
| 4 | 137 | Observation | `Observation.code.coding` | 69548-6 | Genetic variant assessment | http://loinc.org |
| 5 | 138 | Observation | `Observation.valueCodeableConcept.coding` | LA9634-2 | Absent | http://loinc.org |
| 6 | 139 | Observation | `Observation.valueCodeableConcept.coding` | LA18198-4 | No Call | http://loinc.org |
| 7 | 140 | Observation | `Observation.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 8 | 141 | Observation | `Observation.valueCodeableConcept.coding` | LA9633-4 | Present | http://loinc.org |
| 9 | 149 | Observation | `Observation.component.code.coding` | 48018-6 | Gene studied [ID] | http://loinc.org |
| 10 | 155 | Observation | `Observation.component.code.coding` | 48005-3 | Amino acid change (pHGVS) | http://loinc.org |
| 11 | 160 | Observation | `Observation.code.coding` | 86206-0 | Whole genome sequence analysis in Blood or Tissue by Molecular genetics method | http://loinc.org |
| 12 | 161 | Observation | `Observation.code.coding` | valuestring |  | Viral Consensus Genome Sequence |
| 13 | 173 | Observation | `Observation.code.coding` | 31343-7 | Dengue virus Ab [Presence] in Specimen | http://loinc.org |
| 14 | 174 | Observation | `Observation.valueCodeableConcept.coding` | Serotype |  |  |
| 15 | 175 | Observation | `Observation.valueCodeableConcept.coding` | Genotype |  |  |
| 16 | 178 | Observation | `Observation.valueCodeableConcept.coding` | Confidence |  |  |
| 17 | 182 | DiagnosticReport | `DiagnosticReport.code` | 81247-9 | Master HL7 genetic variant reporting panel | http://loinc.org |
| 18 | 201 | Observation | `Observation.code.coding` | SP000682 | Core genome MLST [Type] in Isolate by Sequencing | http://terminology.kemkes.go.id/sp |
| 19 | 220 | Observation | `Observation.component.code.coding` | SP000690 | Loci called | http://terminology.kemkes.go.id/sp |
| 20 | 224 | Observation | `Observation.component.code.coding` | SP000691 | Total loci in scheme | http://terminology.kemkes.go.id/sp |
| 21 | 228 | Observation | `Observation.component.code.coding` | SP000692 | Call rate | http://terminology.kemkes.go.id/sp |
| 22 | 234 | DiagnosticReport | `DiagnosticReport.code` | SP000682 | Core genome MLST [Type] in Isolate by Sequencing | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://loinc.org | 11 |
| http://terminology.kemkes.go.id/sp | 5 |
|  | 3 |
| http://snomed.info/sct | 2 |
| Viral Consensus Genome Sequence | 1 |
| **Total** | **22** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 38 | – | Faskes | Organization | `Organization.name` |
| 179 | – | Report ID | – | `` |
