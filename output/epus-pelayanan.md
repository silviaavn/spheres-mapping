# Output Form: ePuskesmas Pelayanan Pasien

Sumber: `mapping/phdt-data-dictionary-epus-pelayanan.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-epus-pelayanan.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 47 |
| Code (`jumlah code` = 1) | 62 |
| Code unik (code + CodeSystem) | 58 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 2 |
| Variabel BQ (unik) | 0 |
| Variabel raw (variabel dictionary; belum ada file mentah) | 81 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–6 | Encounter | – | – | _Tanggal selesai_ → `Encounter.period.end` (2, tanpa BQ)<br>_No._ → `Encounter.identifier` (3, tanpa BQ)<br>_Tanggal_ → `Encounter.period.start` (5, tanpa BQ)<br>_Tanggal Pemeriksaan_ → `Encounter.period.start` (32, tanpa BQ)<br>_Jenis Kunjungan_ → `Encounter.status` (42, tanpa BQ)<br>_Poli/Ruangan_ → `Encounter.location` (48, tanpa BQ)<br>_Pendaftaran/rujukan internal_ → `Encounter.hospitaliz ation.admitSource.co ding` (309, tanpa BQ)<br>_Lama antrean_ → `Encounter.statusHistory.status` (311, tanpa BQ)<br>_Lama pemeriksaan_ → `Encounter.statusHistory.status` (314, tanpa BQ)<br>_Lama pelayanan_ → `Encounter.period.start` (317, tanpa BQ) |
| 2 | 7–28 | Patient | – | – | _Nama Pasien_ → `Patient.name` (7, tanpa BQ)<br>_No.eRM_ → `Patient.identifier.value` (10, tanpa BQ)<br>_NIK_ → `Patient.identifier.value` (13, tanpa BQ)<br>_No.KK_ → `Patient.identifier.value` (16, tanpa BQ)<br>_No. RM Lama_ → `Patient.name` (17, tanpa BQ)<br>_No. Dokumen RM_ → `Patient.name` (20, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (23, tanpa BQ)<br>_Alamat_ → `Patient.address.line` (25, tanpa BQ)<br>_RT Pasien_ → `Patient.address.line` (27, tanpa BQ)<br>_RW Pasien_ → `Patient.address.line` (28, tanpa BQ)<br>_Kelurahan_ → `Patient.address.extension:administrativeCode.extension:village` (34, tanpa BQ)<br>_Tempat Lahir_ → `Patient.extension:birthPlace` (35, tanpa BQ)<br>_Tgl.Lahir_ → `Patient.birthDate` (36, tanpa BQ)<br>_Umur tahun_ → `Patient.birthDate` (37, tanpa BQ)<br>_Umur bulan_ → `Patient.birthDate` (38, tanpa BQ)<br>_Umur hari_ → `Patient.birthDate` (39, tanpa BQ)<br>_Nama ayah_ → `Patient.contact.name` (40, tanpa BQ)<br>_Nama Ibu_ → `Patient.contact.name` (41, tanpa BQ) |
| 3 | 29–31 | Observation | 85658-3 | Occupation [Type] | _Pekerjaan_ → `Observation.code.coding` (29, tanpa BQ) |
| 4 | 71–78 | Coverage | – | – | _Asuransi_ → `Coverage.type.coding` (74, tanpa BQ)<br>_No.Asuransi_ → `Coverage.identifier.value` (78, tanpa BQ) |
| 5 | 79–81 | Observation | 161572004 | History of congenital anomaly | _Kelainan_ → `Observation.valueString` (81, tanpa BQ) |
| 6 | 82–89 | Practitioner | – | – | _Dokter / Tenaga Medis_ → `Practitioner.identifier.value` (84, tanpa BQ)<br>_Perawat / Bidan / Nutrisionist / Sanitarian_ → `Practitioner.identifier.value` (88, tanpa BQ) |
| 7 | 90–91 | Observation | 51848-0 | Evaluation note | _SOAP Assesment_ → `Observation.category.coding` (90, tanpa BQ) |
| 8 | 92–93 | Observation | 61150-9 | Subjective Narrative | _SOAP Subjective_ → `Observation.category.coding` (92, tanpa BQ) |
| 9 | 94–95 | Observation | 72225-6 | Objective Narrative | _SOAP Object_ → `Observation.category.coding` (94, tanpa BQ) |
| 10 | 96–96 | CarePlan | – | – | _SOAP Planning_ → `Careplan.category.coding` (96, tanpa BQ) |
| 11 | 97–99 | Condition | – | – | _Keluhan Utama_ → `Condition.category.coding` (97, tanpa BQ) |
| 12 | 102–103 | Condition | – | – | _Keluhan Tambahan_ → `Condition.category.coding` (102, tanpa BQ) |
| 13 | 104–105 | Observation | 77977-7 | Illness duration | _Lama Sakit_ → `Observation.category.coding` (104, tanpa BQ) |
| 14 | 106–109 | Observation | 72166-2 | Tobacco smoking status | _Merokok_ → `Observation.category.coding` (106, tanpa BQ) |
| 15 | 110–113 | Observation | 11331-6 | History of Alcohol use | _Konsumsi Alkohol_ → `Observation.category.coding` (110, tanpa BQ) |
| 16 | 114–117 | Observation | 878899005 | Inadequate intake of plant fiber | _Kurang Sayur_ → `Observation.category.coding` (114, tanpa BQ) |
| 17 | 118–118 | CarePlan | – | – | _Terapi_ → `Careplan.category.coding` (118, tanpa BQ) |
| 18 | 119–121 | Procedure | 84635008 | Disease process or condition education | _Edukasi_ → `Procedure.category.coding` (119, tanpa BQ) |
| 19 | 122–123 | CarePlan | – | – | _Tindakan Keperawatan_ → `Careplan.category.coding` (122, tanpa BQ)<br>_Keterangan_ → `Careplan.note` (123, tanpa BQ) |
| 20 | 124–126 | Condition | – | – | _RPS_ → `Condition.category.coding` (124, tanpa BQ) |
| 21 | 127–129 | Condition | – | – | _RPD_ → `Condition.category.coding` (127, tanpa BQ) |
| 22 | 130–131 | FamilyMemberHistory | – | – | _RPK_ → `FamilyMemberHistory.relationship.coding` (130, tanpa BQ) |
| 23 | 132–136 | AllergyIntolerance | – | – | _Alergi_ → `AllergyIntolerance.code.coding` (132, tanpa BQ) |
| 24 | 137–147 | Observation | 67775-7 | Level of responsiveness | _Kesadaran_ → `Observation.category[i].coding` (137, tanpa BQ) |
| 25 | 148–153 | Observation | 75910-0 | Canadian triage and acuity scale [CTAS] | _Triage_ → `Observation.valueCodeableConcept.coding` (150, tanpa BQ) |
| 26 | 154–158 | Observation | 8302-2 | Body height | _Tinggi_ → `Observation.category[i].coding[i]` (154, tanpa BQ) |
| 27 | 159–163 | Observation | 29463-7 | Body weight | _Berat badan_ → `Observation.category[i].coding[i]` (159, tanpa BQ) |
| 28 | 164–168 | Observation | 276361009 | Waist circumference | _Lingkar perut_ → `Observation.category[i].coding[i]` (164, tanpa BQ) |
| 29 | 169–174 | Observation | 39156-5 | Body mass index (BMI) [Ratio] | _IMT_ → `Observation.category[i].coding[i]` (169, tanpa BQ) |
| 30 | 175–188 | Observation | 59575-1 | Body mass index (BMI) [Percentile] Per age | _IMT/U_ → `Observation.category[i].coding[i]` (175, tanpa BQ)<br>_Hasil IMT_ → `Observation.referenceRange` (180, tanpa BQ) |
| 31 | 189–193 | Observation | 8480-6 | Systolic blood pressure | _Sistole_ → `Observation.category[i].coding[i]` (189, tanpa BQ) |
| 32 | 194–198 | Observation | 8462-4 | Diastolic blood pressure | _Diastole_ → `Observation.category[i].coding[i]` (194, tanpa BQ) |
| 33 | 199–203 | Observation | 9279-1 | Respiratory rate | _Nafas_ → `Observation.category[i].coding[i]` (199, tanpa BQ) |
| 34 | 204–208 | Observation | 8867-4 | Heart rate | _Detak nadi_ → `Observation.category[i].coding[i]` (204, tanpa BQ) |
| 35 | 209–212 | Observation | 8884-9 | Heart rate rythm | _Detak jantung_ → `Observation.category[i].coding[i]` (209, tanpa BQ) |
| 36 | 213–217 | Observation | 8310-5 | Body temperature | _Suhu_ → `Observation.category[i].coding[i]` (213, tanpa BQ) |
| 37 | 218–220 | Observation | 129861002 | Physical activity finding | _Aktifitas Fisik dan Assessment Fungsional_ → `Observation.valueString` (220, tanpa BQ) |
| 38 | 221–229 | Observation | 80316-3 | Pain scale [Type] | _Skala nyeri_ → `Observation.valueCodeableConcept.coding` (223, tanpa BQ) |
| 39 | 230–235 | Condition | – | – | _Diagnosa 1_ → `Condition.category.coding` (230, tanpa BQ)<br>_Jenis kasus 1_ → `Condition.onset.dateTime` (233, tanpa BQ) |
| 40 | 236–241 | Condition | – | – | _Diagnosa 2_ → `Condition.category.coding` (236, tanpa BQ)<br>_Jenis kasus 2_ → `Condition.onset.dateTime` (239, tanpa BQ) |
| 41 | 242–247 | Condition | – | – | _Diagnosa 3_ → `Condition.category.coding` (242, tanpa BQ)<br>_Jenis kasus 3_ → `Condition.onset.dateTime` (245, tanpa BQ) |
| 42 | 248–253 | Condition | – | – | _Diagnosa 4_ → `Condition.category.coding` (248, tanpa BQ)<br>_Jenis kasus 4_ → `Condition.onset.dateTime` (251, tanpa BQ) |
| 43 | 254–259 | Condition | – | – | _Diagnosa 5_ → `Condition.category.coding` (254, tanpa BQ)<br>_Jenis kasus 5_ → `Condition.onset.dateTime` (257, tanpa BQ) |
| 44 | 260–262 | ServiceRequest | – | – | _Tindakan_ → `ServiceRequest.category.coding` (260, tanpa BQ) |
| 45 | 263–264 | Procedure | – | – | – |
| 46 | 266–287 | MedicationRequest | SP000370 | Multiple Micronutrient Supplement | – |
| 47 | 288–307 | MedicationDispense | SP000370 | Multiple Micronutrient Supplement | – |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 24 |
| Condition | 9 |
| CarePlan | 3 |
| Procedure | 2 |
| Encounter | 1 |
| Patient | 1 |
| Coverage | 1 |
| Practitioner | 1 |
| FamilyMemberHistory | 1 |
| AllergyIntolerance | 1 |
| ServiceRequest | 1 |
| MedicationRequest | 1 |
| MedicationDispense | 1 |
| **Total** | **47** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 29 | Observation | `Observation.code.coding` | 85658-3 | Occupation [Type] | http://loinc.org |
| 2 | 80 | Observation | `Observation.code.coding` | 161572004 | History of congenital anomaly | http://snomed.info/sct |
| 3 | 91 | Observation | `Observation.code.coding` | 51848-0 | Evaluation note | http://loinc.org |
| 4 | 93 | Observation | `Observation.code.coding` | 61150-9 | Subjective Narrative | http://loinc.org |
| 5 | 95 | Observation | `Observation.code.coding` | 72225-6 | Objective Narrative | http://loinc.org |
| 6 | 105 | Observation | `Observation.code.coding` | 77977-7 | Illness duration | http://loinc.org |
| 7 | 107 | Observation | `Observation.code.coding` | 72166-2 | Tobacco smoking status | http://loinc.org |
| 8 | 108 | Observation | `Observation.valueCodeableConcept[i].coding` | 77176002 | Smoker | http://snomed.info/sct |
| 9 | 109 | Observation | `Observation.valueCodeableConcept[i].coding` | 8392000 | Non-smoker | http://snomed.info/sct |
| 10 | 111 | Observation | `Observation.code.coding` | 11331-6 | History of Alcohol use | http://loinc.org |
| 11 | 112 | Observation | `Observation.valueCodeableConcept[i].coding` | 219006 | Current drinker | http://snomed.info/sct |
| 12 | 113 | Observation | `Observation.valueCodeableConcept[i].coding` | 105542008 | Non - drinker | http://snomed.info/sct |
| 13 | 115 | Observation | `Observation.code.coding` | 878899005 | Inadequate intake of plant fiber | http://loinc.org |
| 14 | 120 | Procedure | `Procedure.code.coding` | 84635008 | Disease process or condition education | http://snomed.info/sct |
| 15 | 121 | Procedure | `Procedure.code.coding` | 10913 | Edukasi Kesehatan Individu | http://terminology.kemkes.go.id/CodeSystem/kptl |
| 16 | 138 | Observation | `Observation.code.coding` | 67775-7 | Level of responsiveness | http://loinc.org |
| 17 | 139 | Observation | `Observation.valueCodeableConcept[i].coding` | 248234008 | Mentally alert | http://snomed.info/sct |
| 18 | 140 | Observation | `Observation.valueCodeableConcept[i].coding` | LA9340-6 | Alert | http://loinc.org |
| 19 | 141 | Observation | `Observation.valueCodeableConcept[i].coding` | 20602000 | Apathy | http://snomed.info/sct |
| 20 | 142 | Observation | `Observation.valueCodeableConcept[i].coding` | 2776000 | Delirium | http://snomed.info/sct |
| 21 | 143 | Observation | `Observation.valueCodeableConcept[i].coding` | 271782001 | Somnolence | http://snomed.info/sct |
| 22 | 144 | Observation | `Observation.valueCodeableConcept[i].coding` | LA25163-9 | Stuporous | http://loinc.org |
| 23 | 145 | Observation | `Observation.valueCodeableConcept[i].coding` | 274659008 | Semicoma | http://snomed.info/sct |
| 24 | 146 | Observation | `Observation.valueCodeableConcept[i].coding` | 371632003 | Coma | http://snomed.info/sct |
| 25 | 147 | Observation | `Observation.valueCodeableConcept[i].coding` | LA9343-0 | Unresponsive | http://loinc.org |
| 26 | 149 | Observation | `Observation.code.coding` | 75910-0 | Canadian triage and acuity scale [CTAS] | http://loinc.org |
| 27 | 150 | Observation | `Observation.valueCodeableConcept.coding` | LA6113-0 | 2 | http://loinc.org |
| 28 | 151 | Observation | `Observation.valueCodeableConcept.coding` | LA6114-8 | 3 | http://loinc.org |
| 29 | 152 | Observation | `Observation.valueCodeableConcept.coding` | LA10137-0 | 5 | http://loinc.org |
| 30 | 155 | Observation | `Observation.code.coding` | 8302-2 | Body height | http://loinc.org |
| 31 | 160 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 32 | 165 | Observation | `Observation.code.coding` | 276361009 | Waist circumference | http://snomed.info/sct |
| 33 | 170 | Observation | `Observation.code.coding` | 39156-5 | Body mass index (BMI) [Ratio] | http://loinc.org |
| 34 | 176 | Observation | `Observation.code.coding` | 59575-1 | Body mass index (BMI) [Percentile] Per age | http://loinc.org |
| 35 | 181 | Observation | `Observation.interpretation.coding` | 248324001 | Well nourished | http://snomed.info/sct |
| 36 | 182 | Observation | `Observation.interpretation.coding` | 248325000 | Undernourished | http://snomed.info/sct |
| 37 | 183 | Observation | `Observation.interpretation.coding` | OI000001 | Gizi Buruk | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 38 | 184 | Observation | `Observation.interpretation.coding` | 248342006 | Underweight | http://snomed.info/sct |
| 39 | 185 | Observation | `Observation.interpretation.coding` | 43664005 | Normal weight | http://snomed.info/sct |
| 40 | 187 | Observation | `Observation.interpretation.coding` | 238131007 | Overweight | http://snomed.info/sct |
| 41 | 188 | Observation | `Observation.interpretation.coding` | 414915002 | Obese | http://snomed.info/sct |
| 42 | 190 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 43 | 195 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://loinc.org |
| 44 | 200 | Observation | `Observation.code.coding` | 9279-1 | Respiratory rate | http://loinc.org |
| 45 | 205 | Observation | `Observation.code.coding` | 8867-4 | Heart rate | http://loinc.org |
| 46 | 210 | Observation | `Observation.code.coding` | 8884-9 | Heart rate rythm | http://loinc.org |
| 47 | 211 | Observation | `Observation.valueCodeableConcept.coding` | 271636001 | Pulse regular | http://snomed.info/sct |
| 48 | 212 | Observation | `Observation.valueCodeableConcept.coding` | 61086009 | Pulse irregular | http://snomed.info/sct |
| 49 | 214 | Observation | `Observation.code.coding` | 8310-5 | Body temperature | http://loinc.org |
| 50 | 219 | Observation | `Observation.code.coding` | 129861002 | Physical activity finding | http://snomed.info/sct |
| 51 | 222 | Observation | `Observation.code.coding` | 80316-3 | Pain scale [Type] | http://loinc.org |
| 52 | 223 | Observation | `Observation.valueCodeableConcept.coding` | 81765008 | No pain | http://snomed.info/sct |
| 53 | 224 | Observation | `Observation.valueCodeableConcept.coding` | 40196000 | Mild pain | http://snomed.info/sct |
| 54 | 225 | Observation | `Observation.valueCodeableConcept.coding` | 40196000 | Mild pain | http://snomed.info/sct |
| 55 | 226 | Observation | `Observation.valueCodeableConcept.coding` | 50415004 | Moderate pain | http://snomed.info/sct |
| 56 | 227 | Observation | `Observation.valueCodeableConcept.coding` | 50415004 | Moderate pain | http://snomed.info/sct |
| 57 | 228 | Observation | `Observation.valueCodeableConcept.coding` | 76948002 | Severe pain | http://snomed.info/sct |
| 58 | 229 | Observation | `Observation.valueCodeableConcept.coding` | 76948002 | Severe pain | http://snomed.info/sct |
| 59 | 269 | MedicationRequest | `MedicationRequest.contained.code.coding` | SP000370 | Multiple Micronutrient Supplement | http://terminology.kemkes.go.id/sp |
| 60 | 291 | MedicationDispense | `MedicationDispense.contained.code.coding` | SP000370 | Multiple Micronutrient Supplement | http://terminology.kemkes.go.id/sp |
| 61 | 309 | Encounter | `Encounter.hospitaliz ation.admitSource.co ding` | 1991000124105 | Referred by self | http://snomed.info/sct |
| 62 | 310 | Encounter | `Encounter.hospitaliz ation.admitSource.co ding` | outp | From outpatient department | http://terminology.hl7. org/CodeSystem/admit -source |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 30 |
| http://loinc.org | 27 |
| http://terminology.kemkes.go.id/sp | 2 |
| http://terminology.kemkes.go.id/CodeSystem/kptl | 1 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 1 |
| http://terminology.hl7. org/CodeSystem/admit -source | 1 |
| **Total** | **62** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 265 | – | Resep | – | `` |
| 308 | – | Apoteker | – | `` |
