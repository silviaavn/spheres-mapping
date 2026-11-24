# Output Form: ASIK - Data Skrining PTM

Sumber: `mapping/phdt-data-dictionary-asik-skrining-ptm.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-asik-skrining-ptm.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 104 |
| Code (`jumlah code` = 1) | 146 |
| Code unik (code + CodeSystem) | 60 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 10 |
| Variabel BQ (unik) | 0 |
| Variabel raw (variabel dictionary; belum ada file mentah) | 67 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–26 | Patient | – | – | _Nama Peserta_ → `Patient.name.text` (2, tanpa BQ)<br>_NIK_ → `Patient.identifier.value` (5, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (7, tanpa BQ)<br>_No Tlp atau HP_ → `Patient.telecom.value` (10, tanpa BQ)<br>_Alamat Peserta_ → `Patient.address.line` (12, tanpa BQ)<br>_Provinsi Peserta_ → `Patient.address.extension.extension.valueCode` (17, tanpa BQ)<br>_Kabko Peserta_ → `Patient.address.extension.extension.valueCode` (20, tanpa BQ)<br>_Kecamatan Peserta_ → `Patient.address.extension.extension.valueCode` (23, tanpa BQ)<br>_Desa atau Kelurahan Peserta_ → `Patient.address.extension.extension.valueCode` (26, tanpa BQ) |
| 2 | 70–83 | Encounter | – | – | _//PJ PTM Puskesmas_ → `Encounter.participant.individual.reference` (76, tanpa BQ)<br>_Tanggal Pemeriksaan_ → `Encounter.period.start` (78, tanpa BQ) |
| 3 | 84–90 | Condition | Z00.8 | Other general exemination | – |
| 4 | 102–113 | Observation | 424144002 | Current chronological age | _Usia_ → `Observation.valueQuantity.value` (105, tanpa BQ)<br>_//PJ PTM Puskesmas_ → `Observation.performer.reference` (112, tanpa BQ) |
| 5 | 114–125 | Observation | 8480-6 | Systolic blood pressure | _Sistol_ → `Observation.valueQuantity.value` (117, tanpa BQ)<br>_//PJ PTM Puskesmas_ → `Observation.performer.reference` (124, tanpa BQ) |
| 6 | 126–137 | Observation | 8462-4 | Diastolic blood pressure | _Diastol_ → `Observation.valueQuantity.value` (129, tanpa BQ)<br>_//PJ PTM Puskesmas_ → `Observation.performer.reference` (136, tanpa BQ) |
| 7 | 138–154 | Observation | 268607006 | Hypertension risk level | _Status - Tekanan Darah_ → `Observation.valueRatio.numerator.value` (141, tanpa BQ)<br>_//PJ PTM Puskesmas_ → `Observation.performer.reference` (153, tanpa BQ) |
| 8 | 155–164 | ServiceRequest | – | – | _Gula Darah Sewaktu_ → `ServiceRequest.category` (155, tanpa BQ) |
| 9 | 169–176 | Specimen | – | – | – |
| 10 | 177–191 | Observation | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | _Status - Gula Darah Sewaktu_ → `Observation.Interpretation.coding` (182, tanpa BQ)<br>_//PJ PTM Puskesmas_ → `Observation.performer.reference` (190, tanpa BQ) |
| 11 | 192–203 | DiagnosticReport | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | – |
| 12 | 204–213 | ServiceRequest | – | – | _Gula Darah Puasa_ → `ServiceRequest.category` (204, tanpa BQ) |
| 13 | 218–225 | Specimen | – | – | – |
| 14 | 226–240 | Observation | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | _Status - Gula Darah Puasa_ → `Observation.Interpretation.coding` (231, tanpa BQ)<br>_//PJ PTM Puskesmas_ → `Observation.performer.reference` (239, tanpa BQ) |
| 15 | 241–252 | DiagnosticReport | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | – |
| 16 | 253–262 | ServiceRequest | – | – | _Gula Darah 2 Jam PP_ → `ServiceRequest.category` (253, tanpa BQ) |
| 17 | 267–274 | Specimen | – | – | – |
| 18 | 275–289 | Observation | 1521-4 | Glucose [Mass/volume] in Serum or Plasma --2 hours post meal | _Status - Gula Darah 2 Jam PP_ → `Observation.Interpretation.coding` (280, tanpa BQ)<br>_//PJ PTM Puskesmas_ → `Observation.performer.reference` (288, tanpa BQ) |
| 19 | 290–301 | DiagnosticReport | 1521-4 | Glucose [Mass/volume] in Serum or Plasma --2 hours post meal | – |
| 20 | 302–311 | ServiceRequest | – | – | _HbA1c_ → `ServiceRequest.category` (302, tanpa BQ) |
| 21 | 316–323 | Specimen | – | – | – |
| 22 | 324–338 | Observation | 4548-4 | Hemoglobin A1c/Hemoglobin.total in Blood | _Status - Gula Darah HbA1c_ → `Observation.Interpretation.coding` (329, tanpa BQ)<br>_//PJ PTM Puskesmas_ → `Observation.performer.reference` (337, tanpa BQ) |
| 23 | 339–350 | DiagnosticReport | 4548-4 | Hemoglobin A1c/Hemoglobin.total in Blood | – |
| 24 | 351–367 | Observation | 39156-5 | Body mass index (BMI) [Ratio] | _IMT_ → `Observation.valueQuantity.value` (354, tanpa BQ)<br>_Status - IMT_ → `Observation.Interpretation.coding` (356, tanpa BQ)<br>_//PJ PTM Puskesmas_ → `Observation.performer.reference` (366, tanpa BQ) |
| 25 | 368–381 | Observation | 396552003 | Abdominal circumference | _Lingkar Perut_ → `Observation.valueQuantity.value` (370, tanpa BQ)<br>_Status - Lingkar Perut_ → `Observation.Interpretation.coding` (372, tanpa BQ)<br>_//PJ PTM Puskesmas_ → `Observation.performer.reference` (379, tanpa BQ)<br>_Sadanis Kanan_ → `Observation.status` (381, tanpa BQ) |
| 26 | 382–395 | Observation | 13607009 | Manual examination of breast | _//PJ PTM Puskesmas_ → `Observation.performer.reference` (393, tanpa BQ)<br>_Sadanis Kiri_ → `Observation.status` (395, tanpa BQ) |
| 27 | 396–409 | Observation | 13607009 | Manual examination of breast | _//PJ PTM Puskesmas_ → `Observation.performer.reference` (407, tanpa BQ)<br>_IVA_ → `Observation.status` (409, tanpa BQ) |
| 28 | 410–422 | Observation | X099241 | Tes IVA | _//PJ PTM Puskesmas_ → `Observation.performer.reference` (420, tanpa BQ)<br>_Status - Tajam Penglihatan_ → `Observation.status` (422, tanpa BQ) |
| 29 | 423–437 | Observation | 260246004 | Visual acuity finding | _//PJ PTM Puskesmas_ → `Observation.performer.reference` (435, tanpa BQ)<br>_Status - Tajam Pendengaran_ → `Observation.status` (437, tanpa BQ) |
| 30 | 438–449 | Observation | 247300007 | Finding of ability to hear voice | _//PJ PTM Puskesmas_ → `Observation.performer.reference` (447, tanpa BQ)<br>_Status - Presbikusis_ → `Observation.status` (449, tanpa BQ) |
| 31 | 450–461 | Observation | OC000151 | Suspek Presbikusis | _//PJ PTM Puskesmas_ → `Observation.performer.reference` (459, tanpa BQ)<br>_Status - Congek (OMSK)_ → `Observation.status` (461, tanpa BQ) |
| 32 | 462–473 | Observation | 38394007 | Chronic purulent otitis media | _//PJ PTM Puskesmas_ → `Observation.performer.reference` (471, tanpa BQ)<br>_Status - Mata Katarak_ → `Observation.status` (473, tanpa BQ) |
| 33 | 474–485 | Observation | SP000101 | Suspek Katarak | _//PJ PTM Puskesmas_ → `Observation.performer.reference` (483, tanpa BQ)<br>_Kuesioner PUMA_ → `Observation.status` (485, tanpa BQ) |
| 34 | 486–498 | Observation | SP000111 | Hasil Kuesioner PUMA | _Level Puma_ → `Observation.valueRange.high` (488, tanpa BQ)<br>_Status - Puma PPOK_ → `Observation.Interpretation.coding` (489, tanpa BQ)<br>_//PJ PTM Puskesmas_ → `Observation.performer.reference` (497, tanpa BQ) |
| 35 | 499–508 | ServiceRequest | – | – | _Kolesterol Total_ → `ServiceRequest.category` (499, tanpa BQ) |
| 36 | 512–519 | Specimen | – | – | – |
| 37 | 520–534 | Observation | 2093-3 | Cholesterol [Mass/volume] in Serum or Plasma | _Status - Kolesterol Total_ → `Observation.Interpretation.coding` (526, tanpa BQ) |
| 38 | 535–546 | DiagnosticReport | 2093-3 | Cholesterol [Mass/volume] in Serum or Plasma | – |
| 39 | 547–556 | ServiceRequest | – | – | _LDL_ → `ServiceRequest.category` (547, tanpa BQ) |
| 40 | 560–567 | Specimen | – | – | – |
| 41 | 568–582 | Observation | 2089-1 | Cholesterol in LDL [Mass/volume] in Serum or Plasma | _Status - LDL_ → `Observation.Interpretation.coding` (574, tanpa BQ) |
| 42 | 583–594 | DiagnosticReport | 2089-1 | Cholesterol in LDL [Mass/volume] in Serum or Plasma | – |
| 43 | 595–604 | ServiceRequest | – | – | _HDL_ → `ServiceRequest.category` (595, tanpa BQ) |
| 44 | 608–615 | Specimen | – | – | – |
| 45 | 616–630 | Observation | 2085-9 | Cholesterol in HDL [Mass/volume] in Serum or Plasma | _Status - HDL_ → `Observation.Interpretation.coding` (622, tanpa BQ) |
| 46 | 631–642 | DiagnosticReport | 2085-9 | Cholesterol in HDL [Mass/volume] in Serum or Plasma | – |
| 47 | 643–652 | ServiceRequest | – | – | _Trigliserida_ → `ServiceRequest.category` (643, tanpa BQ) |
| 48 | 656–663 | Specimen | – | – | – |
| 49 | 664–678 | Observation | 2571-8 | Triglyceride [Mass/volume] in Serum or Plasma | _Status - Trigliserida_ → `Observation.Interpretation.coding` (670, tanpa BQ) |
| 50 | 679–690 | DiagnosticReport | 2571-8 | Triglyceride [Mass/volume] in Serum or Plasma | – |
| 51 | 691–700 | ServiceRequest | – | – | _Status - Lemak Darah_ → `ServiceRequest.category` (691, tanpa BQ) |
| 52 | 704–711 | Specimen | – | – | – |
| 53 | 712–726 | Observation | 2569-2 | Lipids [Mass/volume] in Serum | – |
| 54 | 727–738 | DiagnosticReport | 2569-2 | Lipids [Mass/volume] in Serum | – |
| 55 | 739–748 | ServiceRequest | – | – | _Status - Lemak Darah (Hipertensi atau Diabetes Melitus)_ → `ServiceRequest.category` (739, tanpa BQ) |
| 56 | 752–759 | Specimen | – | – | – |
| 57 | 760–775 | Observation | 2569-2 | Lipids [Mass/volume] in Serum | – |
| 58 | 776–787 | DiagnosticReport | 2569-2 | Lipids [Mass/volume] in Serum | – |
| 59 | 788–797 | ServiceRequest | – | – | _Status - Lemak Darah (Hipertensi dan Diabetes Melitus)_ → `ServiceRequest.category` (788, tanpa BQ) |
| 60 | 801–808 | Specimen | – | – | – |
| 61 | 809–824 | Observation | 2569-2 | Lipids [Mass/volume] in Serum | – |
| 62 | 825–836 | DiagnosticReport | 2569-2 | Lipids [Mass/volume] in Serum | – |
| 63 | 837–846 | ServiceRequest | – | – | _Status - Lemak Darah (Diabetes Melitus)_ → `ServiceRequest.category` (837, tanpa BQ) |
| 64 | 850–857 | Specimen | – | – | – |
| 65 | 858–873 | Observation | 2569-2 | Lipids [Mass/volume] in Serum | – |
| 66 | 874–885 | DiagnosticReport | 2569-2 | Lipids [Mass/volume] in Serum | – |
| 67 | 886–895 | ServiceRequest | – | – | _Status - Lemak Darah (Hipertensi)_ → `ServiceRequest.category` (886, tanpa BQ) |
| 68 | 899–906 | Specimen | – | – | – |
| 69 | 907–922 | Observation | 2569-2 | Lipids [Mass/volume] in Serum | – |
| 70 | 923–934 | DiagnosticReport | 2569-2 | Lipids [Mass/volume] in Serum | – |
| 71 | 935–944 | ServiceRequest | – | – | _Status - Rekam Irama Jantung_ → `ServiceRequest.category` (935, tanpa BQ) |
| 72 | 945–947 | PractitionerRole | – | – | – |
| 73 | 948–959 | Observation | – | – | – |
| 74 | 960–970 | DiagnosticReport | 271921002 | Electrocardiogram finding | – |
| 75 | 971–980 | ServiceRequest | – | – | _Status - Rekam Irama Jantung - Hipertensi atau Diabetes Melitus_ → `ServiceRequest.category` (971, tanpa BQ) |
| 76 | 981–983 | PractitionerRole | – | – | – |
| 77 | 984–996 | Observation | – | – | – |
| 78 | 997–1007 | DiagnosticReport | 271921002 | Electrocardiogram finding | – |
| 79 | 1008–1017 | ServiceRequest | – | – | _Status - Rekam Irama Jantung - Hipertensi dan Diabetes Melitus_ → `ServiceRequest.category` (1008, tanpa BQ) |
| 80 | 1018–1020 | PractitionerRole | – | – | – |
| 81 | 1021–1033 | Observation | – | – | – |
| 82 | 1034–1044 | DiagnosticReport | 271921002 | Electrocardiogram finding | – |
| 83 | 1045–1054 | ServiceRequest | – | – | _Status - Rekam Irama Jantung - Diabetes Melitus_ → `ServiceRequest.category` (1045, tanpa BQ) |
| 84 | 1055–1057 | PractitionerRole | – | – | – |
| 85 | 1058–1070 | Observation | – | – | – |
| 86 | 1071–1081 | DiagnosticReport | 271921002 | Electrocardiogram finding | – |
| 87 | 1082–1091 | ServiceRequest | – | – | _Status - Rekam Irama Jantung - Hipertensi_ → `ServiceRequest.category` (1082, tanpa BQ) |
| 88 | 1092–1094 | PractitionerRole | – | – | – |
| 89 | 1095–1107 | Observation | – | – | – |
| 90 | 1108–1118 | DiagnosticReport | 271921002 | Electrocardiogram finding | – |
| 91 | 1119–1131 | Observation | – | – | _Status - Kanker Payudara - Sadanis_ → `final` (1119, tanpa BQ) |
| 92 | 1132–1141 | ServiceRequest | – | – | _Status - Kanker Payudara - USG_ → `ServiceRequest.category` (1132, tanpa BQ) |
| 93 | 1142–1144 | PractitionerRole | – | – | – |
| 94 | 1145–1157 | Observation | – | – | – |
| 95 | 1158–1168 | DiagnosticReport | 24601-7 | US Breast | – |
| 96 | 1169–1181 | Observation | X099241 | Tes IVA | _Status - Kanker Serviks - IVA_ → `Observation.valueCodeableConcept.coding` (1172, tanpa BQ) |
| 97 | 1182–1191 | ServiceRequest | – | – | _Status - Kanker Serviks - HPV DNA_ → `ServiceRequest.category` (1182, tanpa BQ) |
| 98 | 1195–1202 | Specimen | – | – | – |
| 99 | 1203–1215 | Observation | 44550-2 | Human papillomavirus DNA [Presence] in Cervix by Probe | – |
| 100 | 1216–1227 | DiagnosticReport | 44550-2 | Human papillomavirus DNA [Presence] in Cervix by Probe | – |
| 101 | 1228–1240 | Observation | 275981009 | Screening for malignant neoplasm of lung | _Status - Kanker Paru - Kuesioner_ → `Observation.valueCodeableConcept.coding` (1231, tanpa BQ) |
| 102 | 1241–1253 | Observation | SP000107 | Hasil Kuesioner Kanker Kolorektal | _Status - Kanker Kolorektal - Kuesioner_ → `Observation.valueCodeableConcept.coding` (1244, tanpa BQ) |
| 103 | 1254–1268 | Observation | SP000112 | Hasil Kuesioner Kanker Kolorektal dengan Risiko Tinggi | _Status - Kanker Kolorektal - Risiko Tinggi_ → `Observation.valueCodeableConcept.coding` (1257, tanpa BQ) |
| 104 | 1269–1280 | Observation | SP000114 | Suspek Thalassemia | _Status - Thalassemia_ → `Observation.valueBoolean` (1272, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 41 |
| ServiceRequest | 20 |
| DiagnosticReport | 20 |
| Specimen | 14 |
| PractitionerRole | 6 |
| Patient | 1 |
| Encounter | 1 |
| Condition | 1 |
| **Total** | **104** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 86 | Condition | `Condition.code.coding` | Z00.8 | Other general exemination | http://hl7.org/fhir/sid/icd-10 |
| 2 | 104 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 3 | 116 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 4 | 128 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://loinc.org |
| 5 | 140 | Observation | `Observation.code.coding` | 268607006 | Hypertension risk level | http://snomed.info/sct |
| 6 | 159 | ServiceRequest | `ServiceRequest.code` | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | http://loinc.org |
| 7 | 170 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 8 | 179 | Observation | `Observation.code.coding` | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | http://loinc.org |
| 9 | 194 | DiagnosticReport | `DiagnosticReport.code.coding` | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | http://loinc.org |
| 10 | 208 | ServiceRequest | `ServiceRequest.code` | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 11 | 219 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 12 | 228 | Observation | `Observation.code.coding` | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 13 | 243 | DiagnosticReport | `DiagnosticReport.code.coding` | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 14 | 257 | ServiceRequest | `ServiceRequest.code` | 1521-4 | Glucose [Mass/volume] in Serum or Plasma --2 hours post meal | http://loinc.org |
| 15 | 268 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 16 | 277 | Observation | `Observation.code.coding` | 1521-4 | Glucose [Mass/volume] in Serum or Plasma --2 hours post meal | http://loinc.org |
| 17 | 292 | DiagnosticReport | `DiagnosticReport.code.coding` | 1521-4 | Glucose [Mass/volume] in Serum or Plasma --2 hours post meal | http://loinc.org |
| 18 | 306 | ServiceRequest | `ServiceRequest.code` | 4548-4 | Hemoglobin A1c/Hemoglobin.total in Blood | http://loinc.org |
| 19 | 317 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 20 | 326 | Observation | `Observation.code.coding` | 4548-4 | Hemoglobin A1c/Hemoglobin.total in Blood | http://loinc.org |
| 21 | 341 | DiagnosticReport | `DiagnosticReport.code.coding` | 4548-4 | Hemoglobin A1c/Hemoglobin.total in Blood | http://loinc.org |
| 22 | 353 | Observation | `Observation.code.coding` | 39156-5 | Body mass index (BMI) [Ratio] | http://loinc.org |
| 23 | 369 | Observation | `Observation.code.coding` | 396552003 | Abdominal circumference | http://snomed.info/sct |
| 24 | 383 | Observation | `Observation.code.coding` | 13607009 | Manual examination of breast | http://snomed.info/sct |
| 25 | 384 | Observation | `Observation.valueCodeableConcept.coding` | 290084006 | Breast normal | http://snomed.info/sct |
| 26 | 385 | Observation | `Observation.valueCodeableConcept.coding` | 89164003 | Breast lump | http://snomed.info/sct |
| 27 | 386 | Observation | `Observation.valueCodeableConcept.coding` | 134405005 | Suspected breast cancer | http://snomed.info/sct |
| 28 | 397 | Observation | `Observation.code.coding` | 13607009 | Manual examination of breast | http://snomed.info/sct |
| 29 | 398 | Observation | `Observation.valueCodeableConcept.coding` | 290084006 | Breast normal | http://snomed.info/sct |
| 30 | 399 | Observation | `Observation.valueCodeableConcept.coding` | 89164003 | Breast lump | http://snomed.info/sct |
| 31 | 400 | Observation | `Observation.valueCodeableConcept.coding` | 134405005 | Suspected breast cancer | http://snomed.info/sct |
| 32 | 411 | Observation | `Observation.code.coding` | X099241 | Tes IVA | http://terminology.kemkes.go.id/CodeSystem/examination |
| 33 | 412 | Observation | `Observation.valueCodeableConcept.coding` | 300557001 | Aceto-white reaction positive | http://snomed.info/sct |
| 34 | 413 | Observation | `Observation.valueCodeableConcept.coding` | 300558006 | Aceto-white reaction negative | http://snomed.info/sct |
| 35 | 414 | Observation | `Observation.valueCodeableConcept.coding` | 315266007 | Suspected cervical cancer | http://snomed.info/sct |
| 36 | 424 | Observation | `Observation.code.coding` | 260246004 | Visual acuity finding | http://snomed.info/sct |
| 37 | 425 | Observation | `Observation.valueCodeableConcept.coding` | 45089002 | Normal visual acuity | http://snomed.info/sct |
| 38 | 426 | Observation | `Observation.valueCodeableConcept.coding` | 397543001 | Mild visual impairment | http://snomed.info/sct |
| 39 | 427 | Observation | `Observation.valueCodeableConcept.coding` | 397542006 | Moderate visual impairment | http://snomed.info/sct |
| 40 | 428 | Observation | `Observation.valueCodeableConcept.coding` | 397541004 | Severe visual impairment | http://snomed.info/sct |
| 41 | 429 | Observation | `Observation.valueCodeableConcept.coding` | SP000100 | Buta | http://terminology.kemkes.go.id/sp |
| 42 | 439 | Observation | `Observation.code.coding` | 247300007 | Finding of ability to hear voice | http://snomed.info/sct |
| 43 | 440 | Observation | `Observation.valueCodeableConcept.coding` | 300226000 | Normal ability to hear voice | http://snomed.info/sct |
| 44 | 441 | Observation | `Observation.valueCodeableConcept.coding` | 300227009 | Hearing for voice impaired | http://snomed.info/sct |
| 45 | 451 | Observation | `Observation.code.coding` | OC000151 | Suspek Presbikusis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 46 | 463 | Observation | `Observation.code.coding` | 38394007 | Chronic purulent otitis media | http://snomed.info/sct |
| 47 | 475 | Observation | `Observation.code.coding` | SP000101 | Suspek Katarak | http://terminology.kemkes.go.id/sp |
| 48 | 487 | Observation | `Observation.code.coding` | SP000111 | Hasil Kuesioner PUMA | http://terminology.kemkes.go.id/sp |
| 49 | 503 | ServiceRequest | `ServiceRequest.code` | 2093-3 | Cholesterol [Mass/volume] in Serum or Plasma | http://loinc.org |
| 50 | 513 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 51 | 522 | Observation | `Observation.code.coding` | 2093-3 | Cholesterol [Mass/volume] in Serum or Plasma | http://loinc.org |
| 52 | 537 | DiagnosticReport | `DiagnosticReport.code.coding` | 2093-3 | Cholesterol [Mass/volume] in Serum or Plasma | http://loinc.org |
| 53 | 551 | ServiceRequest | `ServiceRequest.code` | 2089-1 | Cholesterol in LDL [Mass/volume] in Serum or Plasma | http://loinc.org |
| 54 | 561 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 55 | 570 | Observation | `Observation.code.coding` | 2089-1 | Cholesterol in LDL [Mass/volume] in Serum or Plasma | http://loinc.org |
| 56 | 585 | DiagnosticReport | `DiagnosticReport.code.coding` | 2089-1 | Cholesterol in LDL [Mass/volume] in Serum or Plasma | http://loinc.org |
| 57 | 599 | ServiceRequest | `ServiceRequest.code` | 2085-9 | Cholesterol in HDL [Mass/volume] in Serum or Plasma | http://loinc.org |
| 58 | 609 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 59 | 618 | Observation | `Observation.code.coding` | 2085-9 | Cholesterol in HDL [Mass/volume] in Serum or Plasma | http://loinc.org |
| 60 | 633 | DiagnosticReport | `DiagnosticReport.code.coding` | 2085-9 | Cholesterol in HDL [Mass/volume] in Serum or Plasma | http://loinc.org |
| 61 | 647 | ServiceRequest | `ServiceRequest.code` | 2571-8 | Triglyceride [Mass/volume] in Serum or Plasma | http://loinc.org |
| 62 | 657 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 63 | 666 | Observation | `Observation.code.coding` | 2571-8 | Triglyceride [Mass/volume] in Serum or Plasma | http://loinc.org |
| 64 | 681 | DiagnosticReport | `DiagnosticReport.code.coding` | 2571-8 | Triglyceride [Mass/volume] in Serum or Plasma | http://loinc.org |
| 65 | 695 | ServiceRequest | `ServiceRequest.code` | 2569-2 | Lipids [Mass/volume] in Serum | http://loinc.org |
| 66 | 705 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 67 | 714 | Observation | `Observation.code.coding` | 2569-2 | Lipids [Mass/volume] in Serum | http://loinc.org |
| 68 | 729 | DiagnosticReport | `DiagnosticReport.code.coding` | 2569-2 | Lipids [Mass/volume] in Serum | http://loinc.org |
| 69 | 743 | ServiceRequest | `ServiceRequest.code` | 2569-2 | Lipids [Mass/volume] in Serum | http://loinc.org |
| 70 | 753 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 71 | 762 | Observation | `Observation.code.coding` | 2569-2 | Lipids [Mass/volume] in Serum | http://loinc.org |
| 72 | 778 | DiagnosticReport | `DiagnosticReport.code.coding` | 2569-2 | Lipids [Mass/volume] in Serum | http://loinc.org |
| 73 | 792 | ServiceRequest | `ServiceRequest.code` | 2569-2 | Lipids [Mass/volume] in Serum | http://loinc.org |
| 74 | 802 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 75 | 811 | Observation | `Observation.code.coding` | 2569-2 | Lipids [Mass/volume] in Serum | http://loinc.org |
| 76 | 827 | DiagnosticReport | `DiagnosticReport.code.coding` | 2569-2 | Lipids [Mass/volume] in Serum | http://loinc.org |
| 77 | 841 | ServiceRequest | `ServiceRequest.code` | 2569-2 | Lipids [Mass/volume] in Serum | http://loinc.org |
| 78 | 851 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 79 | 860 | Observation | `Observation.code.coding` | 2569-2 | Lipids [Mass/volume] in Serum | http://loinc.org |
| 80 | 876 | DiagnosticReport | `DiagnosticReport.code.coding` | 2569-2 | Lipids [Mass/volume] in Serum | http://loinc.org |
| 81 | 890 | ServiceRequest | `ServiceRequest.code` | 2569-2 | Lipids [Mass/volume] in Serum | http://loinc.org |
| 82 | 900 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 83 | 909 | Observation | `Observation.code.coding` | 2569-2 | Lipids [Mass/volume] in Serum | http://loinc.org |
| 84 | 925 | DiagnosticReport | `DiagnosticReport.code.coding` | 2569-2 | Lipids [Mass/volume] in Serum | http://loinc.org |
| 85 | 939 | ServiceRequest | `ServiceRequest.code` | 271921002 | Electrocardiogram finding | http://snomed.info/sct |
| 86 | 946 | PractitionerRole | `PractitionerRole.code.coding` | 66862007 | Radiologist | http://snomed.info/sct |
| 87 | 950 | Observation | `Observation.code.coding[x]` | 271921002 | Electrocardiogram finding | http://snomed.info/sct |
| 88 | 951 | Observation | `Observation.valueCodeableConcept.coding` | 164854000 | Electrocardiogram normal | http://snomed.info/sct |
| 89 | 952 | Observation | `Observation.valueCodeableConcept.coding` | 102594003 | Electrocardiogram abnormal | http://snomed.info/sct |
| 90 | 962 | DiagnosticReport | `DiagnosticReport.code.coding` | 271921002 | Electrocardiogram finding | http://snomed.info/sct |
| 91 | 975 | ServiceRequest | `ServiceRequest.code` | 271921002 | Electrocardiogram finding | http://snomed.info/sct |
| 92 | 982 | PractitionerRole | `PractitionerRole.code.coding` | 66862007 | Radiologist | http://snomed.info/sct |
| 93 | 986 | Observation | `Observation.code.coding[x]` | 271921002 | Electrocardiogram finding | http://snomed.info/sct |
| 94 | 987 | Observation | `Observation.valueCodeableConcept.coding` | 164854000 | Electrocardiogram normal | http://snomed.info/sct |
| 95 | 988 | Observation | `Observation.valueCodeableConcept.coding` | 102594003 | Electrocardiogram abnormal | http://snomed.info/sct |
| 96 | 999 | DiagnosticReport | `DiagnosticReport.code.coding` | 271921002 | Electrocardiogram finding | http://snomed.info/sct |
| 97 | 1012 | ServiceRequest | `ServiceRequest.code` | 271921002 | Electrocardiogram finding | http://snomed.info/sct |
| 98 | 1019 | PractitionerRole | `PractitionerRole.code.coding` | 66862007 | Radiologist | http://snomed.info/sct |
| 99 | 1023 | Observation | `Observation.code.coding[x]` | 271921002 | Electrocardiogram finding | http://snomed.info/sct |
| 100 | 1024 | Observation | `Observation.valueCodeableConcept.coding` | 164854000 | Electrocardiogram normal | http://snomed.info/sct |
| 101 | 1025 | Observation | `Observation.valueCodeableConcept.coding` | 102594003 | Electrocardiogram abnormal | http://snomed.info/sct |
| 102 | 1036 | DiagnosticReport | `DiagnosticReport.code.coding` | 271921002 | Electrocardiogram finding | http://snomed.info/sct |
| 103 | 1049 | ServiceRequest | `ServiceRequest.code` | 271921002 | Electrocardiogram finding | http://snomed.info/sct |
| 104 | 1056 | PractitionerRole | `PractitionerRole.code.coding` | 66862007 | Radiologist | http://snomed.info/sct |
| 105 | 1060 | Observation | `Observation.code.coding[x]` | 271921002 | Electrocardiogram finding | http://snomed.info/sct |
| 106 | 1061 | Observation | `Observation.valueCodeableConcept.coding` | 164854000 | Electrocardiogram normal | http://snomed.info/sct |
| 107 | 1062 | Observation | `Observation.valueCodeableConcept.coding` | 102594003 | Electrocardiogram abnormal | http://snomed.info/sct |
| 108 | 1073 | DiagnosticReport | `DiagnosticReport.code.coding` | 271921002 | Electrocardiogram finding | http://snomed.info/sct |
| 109 | 1086 | ServiceRequest | `ServiceRequest.code` | 271921002 | Electrocardiogram finding | http://snomed.info/sct |
| 110 | 1093 | PractitionerRole | `PractitionerRole.code.coding` | 66862007 | Radiologist | http://snomed.info/sct |
| 111 | 1097 | Observation | `Observation.code.coding[x]` | 271921002 | Electrocardiogram finding | http://snomed.info/sct |
| 112 | 1098 | Observation | `Observation.valueCodeableConcept.coding` | 164854000 | Electrocardiogram normal | http://snomed.info/sct |
| 113 | 1099 | Observation | `Observation.valueCodeableConcept.coding` | 102594003 | Electrocardiogram abnormal | http://snomed.info/sct |
| 114 | 1110 | DiagnosticReport | `DiagnosticReport.code.coding` | 271921002 | Electrocardiogram finding | http://snomed.info/sct |
| 115 | 1136 | ServiceRequest | `ServiceRequest.code` | 24601-7 | US Breast | http://loinc.org |
| 116 | 1143 | PractitionerRole | `PractitionerRole.code.coding` | 66862007 | Radiologist | http://snomed.info/sct |
| 117 | 1147 | Observation | `Observation.code.coding[x]` | 24601-7 | US Breast | http://loinc.org |
| 118 | 1148 | Observation | `Observation.valueCodeableConcept.coding` | 290084006 | Breast normal | http://snomed.info/sct |
| 119 | 1149 | Observation | `Observation.valueCodeableConcept.coding` | 367644007 | Simple cyst | http://snomed.info/sct |
| 120 | 1150 | Observation | `Observation.valueCodeableConcept.coding` | 449837001 | Complex cyst of breast | http://snomed.info/sct |
| 121 | 1160 | DiagnosticReport | `DiagnosticReport.code.coding` | 24601-7 | US Breast | http://loinc.org |
| 122 | 1171 | Observation | `Observation.code.coding` | X099241 | Tes IVA | http://terminology.kemkes.go.id/CodeSystem/examination |
| 123 | 1172 | Observation | `Observation.valueCodeableConcept.coding` | 300557001 | Aceto-white reaction positive | http://snomed.info/sct |
| 124 | 1173 | Observation | `Observation.valueCodeableConcept.coding` | 300558006 | Aceto-white reaction negative | http://snomed.info/sct |
| 125 | 1174 | Observation | `Observation.valueCodeableConcept.coding` | 315266007 | Suspected cervical cancer | http://snomed.info/sct |
| 126 | 1186 | ServiceRequest | `ServiceRequest.code` | 44550-2 | Human papillomavirus DNA [Presence] in Cervix by Probe | http://loinc.org |
| 127 | 1196 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 128 | 1205 | Observation | `Observation.code.coding` | 44550-2 | Human papillomavirus DNA [Presence] in Cervix by Probe | http://loinc.org |
| 129 | 1206 | Observation | `Observation.valueCodeableConcept.coding` | 787724008 | Human papillomavirus deoxyribonucleic acid not detected | http://snomed.info/sct |
| 130 | 1207 | Observation | `Observation.valueCodeableConcept.coding` | SP000106 | HPV DNA Tipe 16/18 | http://terminology.kemkes.go.id/sp |
| 131 | 1208 | Observation | `Observation.valueCodeableConcept.coding` | OV000351 | Positif (HPV tipe onkogenik lain) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 132 | 1218 | DiagnosticReport | `DiagnosticReport.code.coding` | 44550-2 | Human papillomavirus DNA [Presence] in Cervix by Probe | http://loinc.org |
| 133 | 1230 | Observation | `Observation.code.coding` | 275981009 | Screening for malignant neoplasm of lung | http://snomed.info/sct |
| 134 | 1231 | Observation | `Observation.valueCodeableConcept.coding` | 723505004 | Low risk | http://snomed.info/sct |
| 135 | 1232 | Observation | `Observation.valueCodeableConcept.coding` | 25594002 | Moderate risk of | http://snomed.info/sct |
| 136 | 1233 | Observation | `Observation.valueCodeableConcept.coding` | 723509005 | High risk | http://snomed.info/sct |
| 137 | 1243 | Observation | `Observation.code.coding` | SP000107 | Hasil Kuesioner Kanker Kolorektal | http://terminology.kemkes.go.id/sp |
| 138 | 1244 | Observation | `Observation.valueCodeableConcept.coding` | 723505004 | Low risk | http://snomed.info/sct |
| 139 | 1245 | Observation | `Observation.valueCodeableConcept.coding` | 25594002 | Moderate risk of | http://snomed.info/sct |
| 140 | 1246 | Observation | `Observation.valueCodeableConcept.coding` | 723509005 | High risk | http://snomed.info/sct |
| 141 | 1256 | Observation | `Observation.code.coding` | SP000112 | Hasil Kuesioner Kanker Kolorektal dengan Risiko Tinggi | http://terminology.kemkes.go.id/sp |
| 142 | 1257 | Observation | `Observation.valueCodeableConcept.coding` | SP000108 | Tidak Curiga Kanker Kolorektal | http://terminology.kemkes.go.id/sp |
| 143 | 1258 | Observation | `Observation.valueCodeableConcept.coding` | SP000109 | Curiga Tumor Jinak Kolorektal | http://terminology.kemkes.go.id/sp |
| 144 | 1259 | Observation | `Observation.valueCodeableConcept.coding` | SP000110 | Curiga Kanker Kolorektal | http://terminology.kemkes.go.id/sp |
| 145 | 1260 | Observation | `Observation.valueCodeableConcept.coding` | 162572001 | Suspected malignancy | http://snomed.info/sct |
| 146 | 1271 | Observation | `Observation.code.coding` | SP000114 | Suspek Thalassemia | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 83 |
| http://loinc.org | 48 |
| http://terminology.kemkes.go.id/sp | 10 |
| http://terminology.kemkes.go.id/CodeSystem/examination | 2 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 2 |
| http://hl7.org/fhir/sid/icd-10 | 1 |
| **Total** | **146** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 29 | – | Kode Puskesmas | Organization | `Organization.identifier.value` |
| 31 | – | Puskesmas | Organization | `Organization.name` |
| 165 | – | //Petugas Lab | PractitionerRole | `PractitionerRole.active` |
| 214 | – | //Petugas Lab | PractitionerRole | `PractitionerRole.active` |
| 263 | – | //Petugas Lab | PractitionerRole | `PractitionerRole.active` |
| 312 | – | //Petugas Lab | PractitionerRole | `PractitionerRole.active` |
