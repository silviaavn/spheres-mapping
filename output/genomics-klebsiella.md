# Output Form: Genomics - Klebsiella

Sumber: `mapping/phdt-data-dictionary-genomics-klebsiella.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-genomics-klebsiella.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 10 |
| Code (`jumlah code` = 1) | 31 |
| Code unik (code + CodeSystem) | 28 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 9 |
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
| 7 | 134–188 | Observation | 69548-6 | Genetic variant assessment | _Capsule Type_ → `Observation.component.code.coding` (156, tanpa BQ)<br>_Clonal Complex_ → `Observation.component.code.coding` (169, tanpa BQ)<br>_Gene Identifier_ → `Observation.component.code.coding` (171, tanpa BQ)<br>_Virulence Score_ → `Observation.component.code.coding` (173, tanpa BQ)<br>_Drug Susceptibility_ → `Observation.component.code.coding` (175, tanpa BQ)<br>_Lineage_ → `Observation.component.code.coding` (186, tanpa BQ)<br>_Notes_ → `Observation.note.text` (188, tanpa BQ) |
| 8 | 190–206 | DiagnosticReport | – | – | _Report Status_ → `DiagnosticReport.status` (190, tanpa BQ)<br>_Performer Name_ → `DiagnosticReport.subject.reference` (193, tanpa BQ)<br>_Report Date_ → `DiagnosticReport.effectiveDateTime` (195, tanpa BQ)<br>_Performer Contact_ → `DiagnosticReport.performer.reference` (198, tanpa BQ)<br>_Summary_ → `DiagnosticReport.conclusion` (202, tanpa BQ) |
| 9 | 207–240 | Observation | SP000682 | Core genome MLST [Type] in Isolate by Sequencing | _cgMLST_ → `Observation.valueCodeableConcept.coding` (207, tanpa BQ)<br>_Loci Called_ → `Observation.component.code.coding` (229, tanpa BQ)<br>_Total Loci in Schema_ → `Observation.component.code.coding` (233, tanpa BQ)<br>_Call Rate_ → `Observation.component.code.coding` (237, tanpa BQ) |
| 10 | 241–252 | DiagnosticReport | – | – | _Report Status_ → `DiagnosticReport.status` (241, tanpa BQ)<br>_Performer Name_ → `DiagnosticReport.subject.reference` (244, tanpa BQ)<br>_Report Date_ → `DiagnosticReport.effectiveDateTime` (246, tanpa BQ)<br>_Performer Contact_ → `DiagnosticReport.performer.reference` (249, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 2 |
| DiagnosticReport | 2 |
| Patient | 1 |
| PractitionerRole | 1 |
| Encounter | 1 |
| Condition | 1 |
| Specimen | 1 |
| ServiceRequest | 1 |
| **Total** | **10** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 81 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002.0 | Laboratory Worker | http://snomed.info/sct |
| 2 | 117 | Specimen | `Specimen.type` | 119334006.0 | Sputum specimen | http://snomed.info/sct |
| 3 | 128 | ServiceRequest | `ServiceRequest.code` | 69548-6 | Genetic variant assessment | http://loinc.org |
| 4 | 136 | Observation | `Observation.code.coding` | 69548-6 | Genetic variant assessment | http://loinc.org |
| 5 | 137 | Observation | `Observation.valueCodeableConcept.coding` | LA9634-2 | Absent | http://loinc.org |
| 6 | 138 | Observation | `Observation.valueCodeableConcept.coding` | LA18198-4 | No Call | http://loinc.org |
| 7 | 139 | Observation | `Observation.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 8 | 140 | Observation | `Observation.valueCodeableConcept.coding` | LA9633-4 | Present | http://loinc.org |
| 9 | 156 | Observation | `Observation.component.code.coding` | SP000678 | Klebsiella pneumoniae capsular type [Identifier] by genomic analysis | http://terminology.kemkes.go.id/sp |
| 10 | 169 | Observation | `Observation.component.code.coding` | SP000679 | Klebsiella pneumoniae clonal complex [Identifier] by genomic analysis | http://terminology.kemkes.go.id/sp |
| 11 | 171 | Observation | `Observation.component.code.coding` | 48018-6 | Gene studied [ID] | http://loinc.org |
| 12 | 173 | Observation | `Observation.component.code.coding` | SP000680 | Klebsiella pneumoniae virulence score [Numeric] by genomic analysis | http://terminology.kemkes.go.id/sp |
| 13 | 175 | Observation | `Observation.component.code.coding` | 51961-1 | Genetic variation's effect on drug efficacy | http://loinc.org |
| 14 | 176 | Observation | `Observation.component.valueCodeableConcept.coding` | 765422000.0 | Product containing beta-lactam | http://snomed.info/sct |
| 15 | 177 | Observation | `Observation.component.valueCodeableConcept.coding` | 324116004.0 | Product containing aminoglycoside | http://snomed.info/sct |
| 16 | 178 | Observation | `Observation.component.valueCodeableConcept.coding` | 1010205001.0 | Medicinal product containing fluoroquinolone and acting as antibacterial agent | http://snomed.info/sct |
| 17 | 179 | Observation | `Observation.component.valueCodeableConcept.coding` | 763878009.0 | Product containing macrolide | http://snomed.info/sct |
| 18 | 180 | Observation | `Observation.component.valueCodeableConcept.coding` | 66261008.0 | Product containing tetracycline | http://snomed.info/sct |
| 19 | 181 | Observation | `Observation.component.valueCodeableConcept.coding` | 763875007.0 | Product containing sulfonamide | http://snomed.info/sct |
| 20 | 182 | Observation | `Observation.component.valueCodeableConcept.coding` | 32792001.0 | Product containing trimethoprim | http://snomed.info/sct |
| 21 | 183 | Observation | `Observation.component.valueCodeableConcept.coding` | 57191001.0 | Product containing chloramphenicol | http://snomed.info/sct |
| 22 | 184 | Observation | `Observation.component.valueCodeableConcept.coding` | 73074003.0 | Product containing colistin | http://snomed.info/sct |
| 23 | 185 | Observation | `Observation.component.valueCodeableConcept.coding` | 350134005.0 | Product containing carbapenem | http://snomed.info/sct |
| 24 | 186 | Observation | `Observation.component.code.coding` | 612-2 | Bacterial strain [Type] in Isolate by Bacteria subtyping | http://loinc.org |
| 25 | 192 | DiagnosticReport | `DiagnosticReport.code` | 69548-6 | Genetic variant assessment | http://loinc.org |
| 26 | 206 | DiagnosticReport | `DiagnosticReport.conclusionCode.coding` | SP000681 | Extensively drug resistant klebsiella | http://terminology.kemkes.go.id/sp |
| 27 | 210 | Observation | `Observation.code.coding` | SP000682 | Core genome MLST [Type] in Isolate by Sequencing | http://terminology.kemkes.go.id/sp |
| 28 | 229 | Observation | `Observation.component.code.coding` | SP000690 | Loci called | http://terminology.kemkes.go.id/sp |
| 29 | 233 | Observation | `Observation.component.code.coding` | SP000691 | Total loci in scheme | http://terminology.kemkes.go.id/sp |
| 30 | 237 | Observation | `Observation.component.code.coding` | SP000692 | Call rate | http://terminology.kemkes.go.id/sp |
| 31 | 243 | DiagnosticReport | `DiagnosticReport.code` | SP000682 | Core genome MLST [Type] in Isolate by Sequencing | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 12 |
| http://loinc.org | 10 |
| http://terminology.kemkes.go.id/sp | 9 |
| **Total** | **31** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 38 | – | Faskes | Organization | `Organization.name` |
| 189 | – | Report ID | – | `` |
