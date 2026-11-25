# Output Form: Genomics - TB

Sumber: `mapping/phdt-data-dictionary-genomics-tb.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-genomics-tb.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 8 |
| Code (`jumlah code` = 1) | 43 |
| Code unik (code + CodeSystem) | 42 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 4 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–34 | Patient | – | – | _Nama_ → `Patient.name.text` (2, tanpa BQ)<br>_NIK_ → `Patient.identifier.value` (5, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (7, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (9, tanpa BQ)<br>_Nomor HP_ → `Patient.telecom` (10, tanpa BQ)<br>_Alamat Domisili_ → `Patient.address.use` (13, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (19, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (22, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.extension.valueCode` (25, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.extension.valueCode` (28, tanpa BQ)<br>_Latitude_ → `Patient.address.extension.extension.valueString` (31, tanpa BQ)<br>_Longitude_ → `Patient.address.extension.extension.valueString` (34, tanpa BQ) |
| 2 | 79–82 | PractitionerRole | – | – | _Tenaga Pemeriksa_ → `PractitionerRole.active` (79, tanpa BQ) |
| 3 | 84–98 | Encounter | – | – | – |
| 4 | 99–105 | Condition | – | – | – |
| 5 | 116–123 | Specimen | – | – | _Tanggal Pemeriksaan_ → `Specimen.collectedDateTime` (119, tanpa BQ)<br>_Nama Pasien_ → `Specimen.subject.display` (121, tanpa BQ)<br>_Tanggal Pemeriksaan_ → `Specimen.receivedTime` (123, tanpa BQ) |
| 6 | 124–133 | ServiceRequest | – | – | – |
| 7 | 134–210 | Observation | 69548-6 | Genetic variant assessment | _Protein Level Change_ → `Observation.component.code.coding` (157, tanpa BQ)<br>_DNA/RNA changes_ → `Observation.component.code.coding` (159, tanpa BQ)<br>_Reference genome_ → `Observation.component.code.coding` (165, tanpa BQ)<br>_Read Depth_ → `Observation.component.code.coding` (172, tanpa BQ)<br>_Gene Identifier_ → `Observation.component.code.coding` (176, tanpa BQ)<br>_Variant Location_ → `Observation.component.code.coding` (178, tanpa BQ)<br>_Drug Susceptibility_ → `Observation.component.code.coding` (181, tanpa BQ)<br>_DNA Change Type_ → `Observation.component.code.coding` (200, tanpa BQ)<br>_Genetic Variation Clinical Significance_ → `Observation.component.code.coding` (202, tanpa BQ)<br>_Lineage_ → `Observation.component.code.coding` (208, tanpa BQ)<br>_Notes_ → `Observation.note.text` (210, tanpa BQ) |
| 8 | 212–234 | DiagnosticReport | – | – | _Report Status_ → `DiagnosticReport.status` (212, tanpa BQ)<br>_Performer Name_ → `DiagnosticReport.subject.reference` (216, tanpa BQ)<br>_Report Date_ → `DiagnosticReport.effectiveDateTime` (218, tanpa BQ)<br>_Performer Contact_ → `DiagnosticReport.performer.reference` (221, tanpa BQ)<br>_Summary_ → `DiagnosticReport.conclusion` (228, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Patient | 1 |
| PractitionerRole | 1 |
| Encounter | 1 |
| Condition | 1 |
| Specimen | 1 |
| ServiceRequest | 1 |
| Observation | 1 |
| DiagnosticReport | 1 |
| **Total** | **8** |

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
| 9 | 157 | Observation | `Observation.component.code.coding` | 48005-3 | Amino acid change (pHGVS) | http://loinc.org |
| 10 | 159 | Observation | `Observation.component.code.coding` | 81290-9 | Genomic DNA change (gHGVS) | http://loinc.org |
| 11 | 165 | Observation | `Observation.component.code.coding` | 48013-7 | Genomic reference sequence [ID] | http://loinc.org |
| 12 | 172 | Observation | `Observation.component.code.coding` | 82121-5 | Allelic read depth | http://loinc.org |
| 13 | 176 | Observation | `Observation.component.code.coding` | 48018-6 | Gene studied [ID] | http://loinc.org |
| 14 | 177 | Observation | `Observation.component.valueCodeableConcept.coding` | 887081.0 | gyrB | https://www.ncbi.nlm.nih.gov/gene |
| 15 | 178 | Observation | `Observation.component.code.coding` | 81254-5 | Genomic allele start-end | http://loinc.org |
| 16 | 181 | Observation | `Observation.component.code.coding` | 51961-1 | Genetic variation's effect on drug efficacy | http://loinc.org |
| 17 | 182 | Observation | `Observation.component.valueCodeableConcept.coding` | 29175007.0 | Product containing rifampicin | http://snomed.info/sct |
| 18 | 183 | Observation | `Observation.component.valueCodeableConcept.coding` | 81335000.0 | Product containing isoniazid | http://snomed.info/sct |
| 19 | 184 | Observation | `Observation.component.valueCodeableConcept.coding` | 13592004.0 | Product containing pyrazinamide | http://snomed.info/sct |
| 20 | 185 | Observation | `Observation.component.valueCodeableConcept.coding` | 24450004.0 | Product containing ethambutol | http://snomed.info/sct |
| 21 | 186 | Observation | `Observation.component.valueCodeableConcept.coding` | 40877002.0 | Product containing streptomycin | http://snomed.info/sct |
| 22 | 187 | Observation | `Observation.component.valueCodeableConcept.coding` | 1010205001.0 | Medicinal product containing fluoroquinolone and acting as antibacterial agent | http://snomed.info/sct |
| 23 | 188 | Observation | `Observation.component.valueCodeableConcept.coding` | 96087006.0 | Product containing levofloxacin | http://snomed.info/sct |
| 24 | 189 | Observation | `Observation.component.valueCodeableConcept.coding` | 371296007.0 | Product containing moxifloxacin | http://snomed.info/sct |
| 25 | 190 | Observation | `Observation.component.valueCodeableConcept.coding` | 96086002.0 | Product containing ofloxacin | http://snomed.info/sct |
| 26 | 191 | Observation | `Observation.component.valueCodeableConcept.coding` | 7577004.0 | Product containing ciprofloxacin | http://snomed.info/sct |
| 27 | 192 | Observation | `Observation.component.valueCodeableConcept.coding` | 371238005.0 | Product containing gatifloxacin | http://snomed.info/sct |
| 28 | 193 | Observation | `Observation.component.valueCodeableConcept.coding` | 48836000.0 | Product containing amikacin | http://snomed.info/sct |
| 29 | 194 | Observation | `Observation.component.valueCodeableConcept.coding` | 71451001.0 | Product containing kanamycin | http://snomed.info/sct |
| 30 | 195 | Observation | `Observation.component.valueCodeableConcept.coding` | 14170004.0 | Product containing capreomycin | http://snomed.info/sct |
| 31 | 196 | Observation | `Observation.component.valueCodeableConcept.coding` | 414148003.0 | Product containing ethionamide | http://snomed.info/sct |
| 32 | 197 | Observation | `Observation.component.valueCodeableConcept.coding` | 125695009.0 | Product containing linezolid | http://snomed.info/sct |
| 33 | 198 | Observation | `Observation.component.valueCodeableConcept.coding` | 714087008.0 | Product containing bedaquiline | http://snomed.info/sct |
| 34 | 199 | Observation | `Observation.component.valueCodeableConcept.coding` | 72924009.0 | Product containing clofazimine | http://snomed.info/sct |
| 35 | 200 | Observation | `Observation.component.code.coding` | 48019-4 | DNA change type | http://loinc.org |
| 36 | 202 | Observation | `Observation.component.code.coding` | 53037-8 | Genetic variation clinical significance [Imp] | http://loinc.org |
| 37 | 203 | Observation | `Observation.component.valueCodeableConcept.coding` | LA26333-7 | Uncertain significance | http://loinc.org |
| 38 | 204 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000478 | Assoc w R | http://terminology.kemkes.go.id/sp |
| 39 | 205 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000479 | Assoc w R - Interim | http://terminology.kemkes.go.id/sp |
| 40 | 206 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000480 | Not assoc w R - Interim | http://terminology.kemkes.go.id/sp |
| 41 | 207 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000481 | Not assoc w R | http://terminology.kemkes.go.id/sp |
| 42 | 208 | Observation | `Observation.component.code.coding` | 614-8 | Mycobacterial strain [Type] in Isolate by Mycobacterial subtyping | http://loinc.org |
| 43 | 214 | DiagnosticReport | `DiagnosticReport.code` | 90246-0 | Bacterial whole genome [Nucleotide sequence] in Isolate by Sequencing | http://loinc.org |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 20 |
| http://loinc.org | 18 |
| http://terminology.kemkes.go.id/sp | 4 |
| https://www.ncbi.nlm.nih.gov/gene | 1 |
| **Total** | **43** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 38 | – | Faskes | Organization | `Organization.name` |
| 211 | – | Report ID | – | `` |
| 235 | – | genomic ref allel belum masuk | – | `` |
