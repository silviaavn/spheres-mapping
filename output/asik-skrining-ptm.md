# Output Form: ASIK - Data Skrining PTM

Sumber: `mapping/phdt-data-dictionary-asik-skrining-ptm.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-asik-skrining-ptm.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 104 |
| Code (`jumlah code` = 1) | 215 |
| Code unik (code + CodeSystem) | 79 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 19 |
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
| 10 | 177–191 | Observation | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | _Status - Gula Darah Sewaktu_ → `Observation.interpretation.coding` (182, tanpa BQ)<br>_//PJ PTM Puskesmas_ → `Observation.performer.reference` (190, tanpa BQ) |
| 11 | 192–203 | DiagnosticReport | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | – |
| 12 | 204–213 | ServiceRequest | – | – | _Gula Darah Puasa_ → `ServiceRequest.category` (204, tanpa BQ) |
| 13 | 218–225 | Specimen | – | – | – |
| 14 | 226–240 | Observation | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | _Status - Gula Darah Puasa_ → `Observation.interpretation.coding` (231, tanpa BQ)<br>_//PJ PTM Puskesmas_ → `Observation.performer.reference` (239, tanpa BQ) |
| 15 | 241–252 | DiagnosticReport | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | – |
| 16 | 253–262 | ServiceRequest | – | – | _Gula Darah 2 Jam PP_ → `ServiceRequest.category` (253, tanpa BQ) |
| 17 | 267–274 | Specimen | – | – | – |
| 18 | 275–289 | Observation | 1521-4 | Glucose [Mass/volume] in Serum or Plasma --2 hours post meal | _Status - Gula Darah 2 Jam PP_ → `Observation.interpretation.coding` (280, tanpa BQ)<br>_//PJ PTM Puskesmas_ → `Observation.performer.reference` (288, tanpa BQ) |
| 19 | 290–301 | DiagnosticReport | 1521-4 | Glucose [Mass/volume] in Serum or Plasma --2 hours post meal | – |
| 20 | 302–311 | ServiceRequest | – | – | _HbA1c_ → `ServiceRequest.category` (302, tanpa BQ) |
| 21 | 316–323 | Specimen | – | – | – |
| 22 | 324–338 | Observation | 4548-4 | Hemoglobin A1c/Hemoglobin.total in Blood | _Status - Gula Darah HbA1c_ → `Observation.interpretation.coding` (329, tanpa BQ)<br>_//PJ PTM Puskesmas_ → `Observation.performer.reference` (337, tanpa BQ) |
| 23 | 339–350 | DiagnosticReport | 4548-4 | Hemoglobin A1c/Hemoglobin.total in Blood | – |
| 24 | 351–367 | Observation | 39156-5 | Body mass index (BMI) [Ratio] | _IMT_ → `Observation.valueQuantity.value` (354, tanpa BQ)<br>_Status - IMT_ → `Observation.interpretation.coding` (356, tanpa BQ)<br>_//PJ PTM Puskesmas_ → `Observation.performer.reference` (366, tanpa BQ) |
| 25 | 368–381 | Observation | 396552003 | Abdominal circumference | _Lingkar Perut_ → `Observation.valueQuantity.value` (370, tanpa BQ)<br>_Status - Lingkar Perut_ → `Observation.interpretation.coding` (372, tanpa BQ)<br>_//PJ PTM Puskesmas_ → `Observation.performer.reference` (379, tanpa BQ)<br>_Sadanis Kanan_ → `Observation.status` (381, tanpa BQ) |
| 26 | 382–395 | Observation | 13607009 | Manual examination of breast | _//PJ PTM Puskesmas_ → `Observation.performer.reference` (393, tanpa BQ)<br>_Sadanis Kiri_ → `Observation.status` (395, tanpa BQ) |
| 27 | 396–409 | Observation | 13607009 | Manual examination of breast | _//PJ PTM Puskesmas_ → `Observation.performer.reference` (407, tanpa BQ)<br>_IVA_ → `Observation.status` (409, tanpa BQ) |
| 28 | 410–422 | Observation | X099241 | Tes IVA | _//PJ PTM Puskesmas_ → `Observation.performer.reference` (420, tanpa BQ)<br>_Status - Tajam Penglihatan_ → `Observation.status` (422, tanpa BQ) |
| 29 | 423–437 | Observation | 260246004 | Visual acuity finding | _//PJ PTM Puskesmas_ → `Observation.performer.reference` (435, tanpa BQ)<br>_Status - Tajam Pendengaran_ → `Observation.status` (437, tanpa BQ) |
| 30 | 438–449 | Observation | 247300007 | Finding of ability to hear voice | _//PJ PTM Puskesmas_ → `Observation.performer.reference` (447, tanpa BQ)<br>_Status - Presbikusis_ → `Observation.status` (449, tanpa BQ) |
| 31 | 450–461 | Observation | OC000151 | Suspek Presbikusis | _//PJ PTM Puskesmas_ → `Observation.performer.reference` (459, tanpa BQ)<br>_Status - Congek (OMSK)_ → `Observation.status` (461, tanpa BQ) |
| 32 | 462–473 | Observation | 38394007 | Chronic purulent otitis media | _//PJ PTM Puskesmas_ → `Observation.performer.reference` (471, tanpa BQ)<br>_Status - Mata Katarak_ → `Observation.status` (473, tanpa BQ) |
| 33 | 474–485 | Observation | SP000101 | Suspek Katarak | _//PJ PTM Puskesmas_ → `Observation.performer.reference` (483, tanpa BQ)<br>_Kuesioner PUMA_ → `Observation.status` (485, tanpa BQ) |
| 34 | 486–498 | Observation | SP000111 | Hasil Kuesioner PUMA | _Level Puma_ → `Observation.valueRange.high` (488, tanpa BQ)<br>_Status - Puma PPOK_ → `Observation.interpretation.coding` (489, tanpa BQ)<br>_//PJ PTM Puskesmas_ → `Observation.performer.reference` (497, tanpa BQ) |
| 35 | 499–508 | ServiceRequest | – | – | _Kolesterol Total_ → `ServiceRequest.category` (499, tanpa BQ) |
| 36 | 512–519 | Specimen | – | – | – |
| 37 | 520–534 | Observation | 2093-3 | Cholesterol [Mass/volume] in Serum or Plasma | _Status - Kolesterol Total_ → `Observation.interpretation.coding` (526, tanpa BQ) |
| 38 | 535–546 | DiagnosticReport | 2093-3 | Cholesterol [Mass/volume] in Serum or Plasma | – |
| 39 | 547–556 | ServiceRequest | – | – | _LDL_ → `ServiceRequest.category` (547, tanpa BQ) |
| 40 | 560–567 | Specimen | – | – | – |
| 41 | 568–582 | Observation | 2089-1 | Cholesterol in LDL [Mass/volume] in Serum or Plasma | _Status - LDL_ → `Observation.interpretation.coding` (574, tanpa BQ) |
| 42 | 583–594 | DiagnosticReport | 2089-1 | Cholesterol in LDL [Mass/volume] in Serum or Plasma | – |
| 43 | 595–604 | ServiceRequest | – | – | _HDL_ → `ServiceRequest.category` (595, tanpa BQ) |
| 44 | 608–615 | Specimen | – | – | – |
| 45 | 616–630 | Observation | 2085-9 | Cholesterol in HDL [Mass/volume] in Serum or Plasma | _Status - HDL_ → `Observation.interpretation.coding` (622, tanpa BQ) |
| 46 | 631–642 | DiagnosticReport | 2085-9 | Cholesterol in HDL [Mass/volume] in Serum or Plasma | – |
| 47 | 643–652 | ServiceRequest | – | – | _Trigliserida_ → `ServiceRequest.category` (643, tanpa BQ) |
| 48 | 656–663 | Specimen | – | – | – |
| 49 | 664–678 | Observation | 2571-8 | Triglyceride [Mass/volume] in Serum or Plasma | _Status - Trigliserida_ → `Observation.interpretation.coding` (670, tanpa BQ) |
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
| 91 | 1119–1131 | Observation | 13607009 | Manual examination of breast | _Status - Kanker Payudara - Sadanis_ → `Observation.valueCodeableConcept.coding` (1122, tanpa BQ) |
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
| 6 | 145 | Observation | `Observation.interpretation.coding` | 38341003 | Hypertensive disorder, systemic arterial | http://snomed.info/sct |
| 7 | 146 | Observation | `Observation.interpretation.coding` | 2004005 | Normal blood pressure | http://snomed.info/sct |
| 8 | 147 | Observation | `Observation.interpretation.coding` | 702817009 | Prehypertension | http://snomed.info/sct |
| 9 | 159 | ServiceRequest | `ServiceRequest.code` | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | http://loinc.org |
| 10 | 167 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002 | Laboratory worker | http://snomed.info/sct |
| 11 | 170 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 12 | 179 | Observation | `Observation.code.coding` | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | http://loinc.org |
| 13 | 182 | Observation | `Observation.interpretation.coding` | 166921001 | Blood glucose normal | http://snomed.info/sct |
| 14 | 183 | Observation | `Observation.interpretation.coding` | 714628002 | Pre-diabetes | http://snomed.info/sct |
| 15 | 184 | Observation | `Observation.interpretation.coding` | 80394007 | Hyperglycemia | http://snomed.info/sct |
| 16 | 194 | DiagnosticReport | `DiagnosticReport.code.coding` | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | http://loinc.org |
| 17 | 208 | ServiceRequest | `ServiceRequest.code` | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 18 | 216 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002 | Laboratory worker | http://snomed.info/sct |
| 19 | 219 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 20 | 228 | Observation | `Observation.code.coding` | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 21 | 231 | Observation | `Observation.interpretation.coding` | 166921001 | Blood glucose normal | http://snomed.info/sct |
| 22 | 232 | Observation | `Observation.interpretation.coding` | 714628002 | Pre-diabetes | http://snomed.info/sct |
| 23 | 233 | Observation | `Observation.interpretation.coding` | 80394007 | Hyperglycemia | http://snomed.info/sct |
| 24 | 243 | DiagnosticReport | `DiagnosticReport.code.coding` | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 25 | 257 | ServiceRequest | `ServiceRequest.code` | 1521-4 | Glucose [Mass/volume] in Serum or Plasma --2 hours post meal | http://loinc.org |
| 26 | 265 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002 | Laboratory worker | http://snomed.info/sct |
| 27 | 268 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 28 | 277 | Observation | `Observation.code.coding` | 1521-4 | Glucose [Mass/volume] in Serum or Plasma --2 hours post meal | http://loinc.org |
| 29 | 280 | Observation | `Observation.interpretation.coding` | 166921001 | Blood glucose normal | http://snomed.info/sct |
| 30 | 281 | Observation | `Observation.interpretation.coding` | 714628002 | Pre-diabetes | http://snomed.info/sct |
| 31 | 282 | Observation | `Observation.interpretation.coding` | 80394007 | Hyperglycemia | http://snomed.info/sct |
| 32 | 292 | DiagnosticReport | `DiagnosticReport.code.coding` | 1521-4 | Glucose [Mass/volume] in Serum or Plasma --2 hours post meal | http://loinc.org |
| 33 | 306 | ServiceRequest | `ServiceRequest.code` | 4548-4 | Hemoglobin A1c/Hemoglobin.total in Blood | http://loinc.org |
| 34 | 314 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002 | Laboratory worker | http://snomed.info/sct |
| 35 | 317 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 36 | 326 | Observation | `Observation.code.coding` | 4548-4 | Hemoglobin A1c/Hemoglobin.total in Blood | http://loinc.org |
| 37 | 329 | Observation | `Observation.interpretation.coding` | 166921001 | Blood glucose normal | http://snomed.info/sct |
| 38 | 330 | Observation | `Observation.interpretation.coding` | 714628002 | Pre-diabetes | http://snomed.info/sct |
| 39 | 331 | Observation | `Observation.interpretation.coding` | 80394007 | Hyperglycemia | http://snomed.info/sct |
| 40 | 341 | DiagnosticReport | `DiagnosticReport.code.coding` | 4548-4 | Hemoglobin A1c/Hemoglobin.total in Blood | http://loinc.org |
| 41 | 353 | Observation | `Observation.code.coding` | 39156-5 | Body mass index (BMI) [Ratio] | http://loinc.org |
| 42 | 356 | Observation | `Observation.interpretation.coding` | 248342006 | Underweight | http://snomed.info/sct |
| 43 | 357 | Observation | `Observation.interpretation.coding` | 238131007 | Overweight | http://snomed.info/sct |
| 44 | 358 | Observation | `Observation.interpretation.coding` | 238131007 | Overweight | http://snomed.info/sct |
| 45 | 359 | Observation | `Observation.interpretation.coding` | 43664005 | Normal weight | http://snomed.info/sct |
| 46 | 360 | Observation | `Observation.interpretation.coding` | 414915002 | Obese | http://snomed.info/sct |
| 47 | 369 | Observation | `Observation.code.coding` | 396552003 | Abdominal circumference | http://snomed.info/sct |
| 48 | 372 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 49 | 373 | Observation | `Observation.interpretation.coding` | 248311001 | Central obesity | http://snomed.info/sct |
| 50 | 383 | Observation | `Observation.code.coding` | 13607009 | Manual examination of breast | http://snomed.info/sct |
| 51 | 384 | Observation | `Observation.valueCodeableConcept.coding` | 290084006 | Breast normal | http://snomed.info/sct |
| 52 | 385 | Observation | `Observation.valueCodeableConcept.coding` | 89164003 | Breast lump | http://snomed.info/sct |
| 53 | 386 | Observation | `Observation.valueCodeableConcept.coding` | 134405005 | Suspected breast cancer | http://snomed.info/sct |
| 54 | 397 | Observation | `Observation.code.coding` | 13607009 | Manual examination of breast | http://snomed.info/sct |
| 55 | 398 | Observation | `Observation.valueCodeableConcept.coding` | 290084006 | Breast normal | http://snomed.info/sct |
| 56 | 399 | Observation | `Observation.valueCodeableConcept.coding` | 89164003 | Breast lump | http://snomed.info/sct |
| 57 | 400 | Observation | `Observation.valueCodeableConcept.coding` | 134405005 | Suspected breast cancer | http://snomed.info/sct |
| 58 | 411 | Observation | `Observation.code.coding` | X099241 | Tes IVA | http://terminology.kemkes.go.id/CodeSystem/examination |
| 59 | 412 | Observation | `Observation.valueCodeableConcept.coding` | 300557001 | Aceto-white reaction positive | http://snomed.info/sct |
| 60 | 413 | Observation | `Observation.valueCodeableConcept.coding` | 300558006 | Aceto-white reaction negative | http://snomed.info/sct |
| 61 | 414 | Observation | `Observation.valueCodeableConcept.coding` | 315266007 | Suspected cervical cancer | http://snomed.info/sct |
| 62 | 424 | Observation | `Observation.code.coding` | 260246004 | Visual acuity finding | http://snomed.info/sct |
| 63 | 425 | Observation | `Observation.valueCodeableConcept.coding` | 45089002 | Normal visual acuity | http://snomed.info/sct |
| 64 | 426 | Observation | `Observation.valueCodeableConcept.coding` | 397543001 | Mild visual impairment | http://snomed.info/sct |
| 65 | 427 | Observation | `Observation.valueCodeableConcept.coding` | 397542006 | Moderate visual impairment | http://snomed.info/sct |
| 66 | 428 | Observation | `Observation.valueCodeableConcept.coding` | 397541004 | Severe visual impairment | http://snomed.info/sct |
| 67 | 429 | Observation | `Observation.valueCodeableConcept.coding` | SP000100 | Buta | http://terminology.kemkes.go.id/sp |
| 68 | 439 | Observation | `Observation.code.coding` | 247300007 | Finding of ability to hear voice | http://snomed.info/sct |
| 69 | 440 | Observation | `Observation.valueCodeableConcept.coding` | 300226000 | Normal ability to hear voice | http://snomed.info/sct |
| 70 | 441 | Observation | `Observation.valueCodeableConcept.coding` | 300227009 | Hearing for voice impaired | http://snomed.info/sct |
| 71 | 451 | Observation | `Observation.code.coding` | OC000151 | Suspek Presbikusis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 72 | 463 | Observation | `Observation.code.coding` | 38394007 | Chronic purulent otitis media | http://snomed.info/sct |
| 73 | 475 | Observation | `Observation.code.coding` | SP000101 | Suspek Katarak | http://terminology.kemkes.go.id/sp |
| 74 | 487 | Observation | `Observation.code.coding` | SP000111 | Hasil Kuesioner PUMA | http://terminology.kemkes.go.id/sp |
| 75 | 489 | Observation | `Observation.interpretation.coding` | 723505004 | Low risk | http://snomed.info/sct |
| 76 | 491 | Observation | `Observation.interpretation.coding` | 723509005 | High risk | http://snomed.info/sct |
| 77 | 503 | ServiceRequest | `ServiceRequest.code` | 2093-3 | Cholesterol [Mass/volume] in Serum or Plasma | http://loinc.org |
| 78 | 510 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002 | Laboratory worker | http://snomed.info/sct |
| 79 | 513 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 80 | 522 | Observation | `Observation.code.coding` | 2093-3 | Cholesterol [Mass/volume] in Serum or Plasma | http://loinc.org |
| 81 | 526 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 82 | 527 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 83 | 537 | DiagnosticReport | `DiagnosticReport.code.coding` | 2093-3 | Cholesterol [Mass/volume] in Serum or Plasma | http://loinc.org |
| 84 | 551 | ServiceRequest | `ServiceRequest.code` | 2089-1 | Cholesterol in LDL [Mass/volume] in Serum or Plasma | http://loinc.org |
| 85 | 558 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002 | Laboratory worker | http://snomed.info/sct |
| 86 | 561 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 87 | 570 | Observation | `Observation.code.coding` | 2089-1 | Cholesterol in LDL [Mass/volume] in Serum or Plasma | http://loinc.org |
| 88 | 574 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 89 | 575 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 90 | 585 | DiagnosticReport | `DiagnosticReport.code.coding` | 2089-1 | Cholesterol in LDL [Mass/volume] in Serum or Plasma | http://loinc.org |
| 91 | 599 | ServiceRequest | `ServiceRequest.code` | 2085-9 | Cholesterol in HDL [Mass/volume] in Serum or Plasma | http://loinc.org |
| 92 | 606 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002 | Laboratory worker | http://snomed.info/sct |
| 93 | 609 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 94 | 618 | Observation | `Observation.code.coding` | 2085-9 | Cholesterol in HDL [Mass/volume] in Serum or Plasma | http://loinc.org |
| 95 | 622 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 96 | 623 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 97 | 633 | DiagnosticReport | `DiagnosticReport.code.coding` | 2085-9 | Cholesterol in HDL [Mass/volume] in Serum or Plasma | http://loinc.org |
| 98 | 647 | ServiceRequest | `ServiceRequest.code` | 2571-8 | Triglyceride [Mass/volume] in Serum or Plasma | http://loinc.org |
| 99 | 654 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002 | Laboratory worker | http://snomed.info/sct |
| 100 | 657 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 101 | 666 | Observation | `Observation.code.coding` | 2571-8 | Triglyceride [Mass/volume] in Serum or Plasma | http://loinc.org |
| 102 | 670 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 103 | 671 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 104 | 681 | DiagnosticReport | `DiagnosticReport.code.coding` | 2571-8 | Triglyceride [Mass/volume] in Serum or Plasma | http://loinc.org |
| 105 | 695 | ServiceRequest | `ServiceRequest.code` | 2569-2 | Lipids [Mass/volume] in Serum | http://loinc.org |
| 106 | 702 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002 | Laboratory worker | http://snomed.info/sct |
| 107 | 705 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 108 | 714 | Observation | `Observation.code.coding` | 2569-2 | Lipids [Mass/volume] in Serum | http://loinc.org |
| 109 | 718 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 110 | 719 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 111 | 729 | DiagnosticReport | `DiagnosticReport.code.coding` | 2569-2 | Lipids [Mass/volume] in Serum | http://loinc.org |
| 112 | 743 | ServiceRequest | `ServiceRequest.code` | 2569-2 | Lipids [Mass/volume] in Serum | http://loinc.org |
| 113 | 750 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002 | Laboratory worker | http://snomed.info/sct |
| 114 | 753 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 115 | 762 | Observation | `Observation.code.coding` | 2569-2 | Lipids [Mass/volume] in Serum | http://loinc.org |
| 116 | 766 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 117 | 767 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 118 | 768 | Observation | `Observation.referenceRange.appliesTo.coding` | SP000103 | Orang dengan Hipertensi atau Diabetes | http://terminology.kemkes.go.id/sp |
| 119 | 778 | DiagnosticReport | `DiagnosticReport.code.coding` | 2569-2 | Lipids [Mass/volume] in Serum | http://loinc.org |
| 120 | 792 | ServiceRequest | `ServiceRequest.code` | 2569-2 | Lipids [Mass/volume] in Serum | http://loinc.org |
| 121 | 799 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002 | Laboratory worker | http://snomed.info/sct |
| 122 | 802 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 123 | 811 | Observation | `Observation.code.coding` | 2569-2 | Lipids [Mass/volume] in Serum | http://loinc.org |
| 124 | 815 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 125 | 816 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 126 | 817 | Observation | `Observation.referenceRange.appliesTo.coding` | SP000102 | Orang dengan Hipertensi dan Diabetes | http://terminology.kemkes.go.id/sp |
| 127 | 827 | DiagnosticReport | `DiagnosticReport.code.coding` | 2569-2 | Lipids [Mass/volume] in Serum | http://loinc.org |
| 128 | 841 | ServiceRequest | `ServiceRequest.code` | 2569-2 | Lipids [Mass/volume] in Serum | http://loinc.org |
| 129 | 848 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002 | Laboratory worker | http://snomed.info/sct |
| 130 | 851 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 131 | 860 | Observation | `Observation.code.coding` | 2569-2 | Lipids [Mass/volume] in Serum | http://loinc.org |
| 132 | 864 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 133 | 865 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 134 | 866 | Observation | `Observation.referenceRange.appliesTo.coding` | SP000105 | Orang dengan Diabetes | http://terminology.kemkes.go.id/sp |
| 135 | 876 | DiagnosticReport | `DiagnosticReport.code.coding` | 2569-2 | Lipids [Mass/volume] in Serum | http://loinc.org |
| 136 | 890 | ServiceRequest | `ServiceRequest.code` | 2569-2 | Lipids [Mass/volume] in Serum | http://loinc.org |
| 137 | 897 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002 | Laboratory worker | http://snomed.info/sct |
| 138 | 900 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 139 | 909 | Observation | `Observation.code.coding` | 2569-2 | Lipids [Mass/volume] in Serum | http://loinc.org |
| 140 | 913 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 141 | 914 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 142 | 915 | Observation | `Observation.referenceRange.appliesTo.coding` | SP000104 | Orang dengan Hipertensi | http://terminology.kemkes.go.id/sp |
| 143 | 925 | DiagnosticReport | `DiagnosticReport.code.coding` | 2569-2 | Lipids [Mass/volume] in Serum | http://loinc.org |
| 144 | 939 | ServiceRequest | `ServiceRequest.code` | 271921002 | Electrocardiogram finding | http://snomed.info/sct |
| 145 | 946 | PractitionerRole | `PractitionerRole.code.coding` | 66862007 | Radiologist | http://snomed.info/sct |
| 146 | 950 | Observation | `Observation.code.coding[x]` | 271921002 | Electrocardiogram finding | http://snomed.info/sct |
| 147 | 951 | Observation | `Observation.valueCodeableConcept.coding` | 164854000 | Electrocardiogram normal | http://snomed.info/sct |
| 148 | 952 | Observation | `Observation.valueCodeableConcept.coding` | 102594003 | Electrocardiogram abnormal | http://snomed.info/sct |
| 149 | 962 | DiagnosticReport | `DiagnosticReport.code.coding` | 271921002 | Electrocardiogram finding | http://snomed.info/sct |
| 150 | 975 | ServiceRequest | `ServiceRequest.code` | 271921002 | Electrocardiogram finding | http://snomed.info/sct |
| 151 | 982 | PractitionerRole | `PractitionerRole.code.coding` | 66862007 | Radiologist | http://snomed.info/sct |
| 152 | 986 | Observation | `Observation.code.coding[x]` | 271921002 | Electrocardiogram finding | http://snomed.info/sct |
| 153 | 987 | Observation | `Observation.valueCodeableConcept.coding` | 164854000 | Electrocardiogram normal | http://snomed.info/sct |
| 154 | 988 | Observation | `Observation.valueCodeableConcept.coding` | 102594003 | Electrocardiogram abnormal | http://snomed.info/sct |
| 155 | 989 | Observation | `Observation.referenceRange.appliesTo.coding` | SP000103 | Orang dengan Hipertensi atau Diabetes | http://terminology.kemkes.go.id/sp |
| 156 | 999 | DiagnosticReport | `DiagnosticReport.code.coding` | 271921002 | Electrocardiogram finding | http://snomed.info/sct |
| 157 | 1012 | ServiceRequest | `ServiceRequest.code` | 271921002 | Electrocardiogram finding | http://snomed.info/sct |
| 158 | 1019 | PractitionerRole | `PractitionerRole.code.coding` | 66862007 | Radiologist | http://snomed.info/sct |
| 159 | 1023 | Observation | `Observation.code.coding[x]` | 271921002 | Electrocardiogram finding | http://snomed.info/sct |
| 160 | 1024 | Observation | `Observation.valueCodeableConcept.coding` | 164854000 | Electrocardiogram normal | http://snomed.info/sct |
| 161 | 1025 | Observation | `Observation.valueCodeableConcept.coding` | 102594003 | Electrocardiogram abnormal | http://snomed.info/sct |
| 162 | 1026 | Observation | `Observation.referenceRange.appliesTo.coding` | SP000102 | Orang dengan Hipertensi dan Diabetes | http://terminology.kemkes.go.id/sp |
| 163 | 1036 | DiagnosticReport | `DiagnosticReport.code.coding` | 271921002 | Electrocardiogram finding | http://snomed.info/sct |
| 164 | 1049 | ServiceRequest | `ServiceRequest.code` | 271921002 | Electrocardiogram finding | http://snomed.info/sct |
| 165 | 1056 | PractitionerRole | `PractitionerRole.code.coding` | 66862007 | Radiologist | http://snomed.info/sct |
| 166 | 1060 | Observation | `Observation.code.coding[x]` | 271921002 | Electrocardiogram finding | http://snomed.info/sct |
| 167 | 1061 | Observation | `Observation.valueCodeableConcept.coding` | 164854000 | Electrocardiogram normal | http://snomed.info/sct |
| 168 | 1062 | Observation | `Observation.valueCodeableConcept.coding` | 102594003 | Electrocardiogram abnormal | http://snomed.info/sct |
| 169 | 1063 | Observation | `Observation.referenceRange.appliesTo.coding` | SP000105 | Orang dengan Diabetes | http://terminology.kemkes.go.id/sp |
| 170 | 1073 | DiagnosticReport | `DiagnosticReport.code.coding` | 271921002 | Electrocardiogram finding | http://snomed.info/sct |
| 171 | 1086 | ServiceRequest | `ServiceRequest.code` | 271921002 | Electrocardiogram finding | http://snomed.info/sct |
| 172 | 1093 | PractitionerRole | `PractitionerRole.code.coding` | 66862007 | Radiologist | http://snomed.info/sct |
| 173 | 1097 | Observation | `Observation.code.coding[x]` | 271921002 | Electrocardiogram finding | http://snomed.info/sct |
| 174 | 1098 | Observation | `Observation.valueCodeableConcept.coding` | 164854000 | Electrocardiogram normal | http://snomed.info/sct |
| 175 | 1099 | Observation | `Observation.valueCodeableConcept.coding` | 102594003 | Electrocardiogram abnormal | http://snomed.info/sct |
| 176 | 1100 | Observation | `Observation.referenceRange.appliesTo.coding` | SP000104 | Orang dengan Hipertensi | http://terminology.kemkes.go.id/sp |
| 177 | 1110 | DiagnosticReport | `DiagnosticReport.code.coding` | 271921002 | Electrocardiogram finding | http://snomed.info/sct |
| 178 | 1121 | Observation | `Observation.code.coding` | 13607009 | Manual examination of breast | http://snomed.info/sct |
| 179 | 1122 | Observation | `Observation.valueCodeableConcept.coding` | 290084006 | Breast normal | http://snomed.info/sct |
| 180 | 1123 | Observation | `Observation.valueCodeableConcept.coding` | 89164003 | Breast lump | http://snomed.info/sct |
| 181 | 1124 | Observation | `Observation.valueCodeableConcept.coding` | 134405005 | Suspected breast cancer | http://snomed.info/sct |
| 182 | 1136 | ServiceRequest | `ServiceRequest.code` | 24601-7 | US Breast | http://loinc.org |
| 183 | 1143 | PractitionerRole | `PractitionerRole.code.coding` | 66862007 | Radiologist | http://snomed.info/sct |
| 184 | 1147 | Observation | `Observation.code.coding[x]` | 24601-7 | US Breast | http://loinc.org |
| 185 | 1148 | Observation | `Observation.valueCodeableConcept.coding` | 290084006 | Breast normal | http://snomed.info/sct |
| 186 | 1149 | Observation | `Observation.valueCodeableConcept.coding` | 367644007 | Simple cyst | http://snomed.info/sct |
| 187 | 1150 | Observation | `Observation.valueCodeableConcept.coding` | 449837001 | Complex cyst of breast | http://snomed.info/sct |
| 188 | 1160 | DiagnosticReport | `DiagnosticReport.code.coding` | 24601-7 | US Breast | http://loinc.org |
| 189 | 1171 | Observation | `Observation.code.coding` | X099241 | Tes IVA | http://terminology.kemkes.go.id/CodeSystem/examination |
| 190 | 1172 | Observation | `Observation.valueCodeableConcept.coding` | 300557001 | Aceto-white reaction positive | http://snomed.info/sct |
| 191 | 1173 | Observation | `Observation.valueCodeableConcept.coding` | 300558006 | Aceto-white reaction negative | http://snomed.info/sct |
| 192 | 1174 | Observation | `Observation.valueCodeableConcept.coding` | 315266007 | Suspected cervical cancer | http://snomed.info/sct |
| 193 | 1186 | ServiceRequest | `ServiceRequest.code` | 44550-2 | Human papillomavirus DNA [Presence] in Cervix by Probe | http://loinc.org |
| 194 | 1193 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002 | Laboratory worker | http://snomed.info/sct |
| 195 | 1196 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 196 | 1205 | Observation | `Observation.code.coding` | 44550-2 | Human papillomavirus DNA [Presence] in Cervix by Probe | http://loinc.org |
| 197 | 1206 | Observation | `Observation.valueCodeableConcept.coding` | 787724008 | Human papillomavirus deoxyribonucleic acid not detected | http://snomed.info/sct |
| 198 | 1207 | Observation | `Observation.valueCodeableConcept.coding` | SP000106 | HPV DNA Tipe 16/18 | http://terminology.kemkes.go.id/sp |
| 199 | 1208 | Observation | `Observation.valueCodeableConcept.coding` | OV000351 | Positif (HPV tipe onkogenik lain) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 200 | 1218 | DiagnosticReport | `DiagnosticReport.code.coding` | 44550-2 | Human papillomavirus DNA [Presence] in Cervix by Probe | http://loinc.org |
| 201 | 1230 | Observation | `Observation.code.coding` | 275981009 | Screening for malignant neoplasm of lung | http://snomed.info/sct |
| 202 | 1231 | Observation | `Observation.valueCodeableConcept.coding` | 723505004 | Low risk | http://snomed.info/sct |
| 203 | 1232 | Observation | `Observation.valueCodeableConcept.coding` | 25594002 | Moderate risk of | http://snomed.info/sct |
| 204 | 1233 | Observation | `Observation.valueCodeableConcept.coding` | 723509005 | High risk | http://snomed.info/sct |
| 205 | 1243 | Observation | `Observation.code.coding` | SP000107 | Hasil Kuesioner Kanker Kolorektal | http://terminology.kemkes.go.id/sp |
| 206 | 1244 | Observation | `Observation.valueCodeableConcept.coding` | 723505004 | Low risk | http://snomed.info/sct |
| 207 | 1245 | Observation | `Observation.valueCodeableConcept.coding` | 25594002 | Moderate risk of | http://snomed.info/sct |
| 208 | 1246 | Observation | `Observation.valueCodeableConcept.coding` | 723509005 | High risk | http://snomed.info/sct |
| 209 | 1256 | Observation | `Observation.code.coding` | SP000112 | Hasil Kuesioner Kanker Kolorektal dengan Risiko Tinggi | http://terminology.kemkes.go.id/sp |
| 210 | 1257 | Observation | `Observation.valueCodeableConcept.coding` | SP000108 | Tidak Curiga Kanker Kolorektal | http://terminology.kemkes.go.id/sp |
| 211 | 1258 | Observation | `Observation.valueCodeableConcept.coding` | SP000109 | Curiga Tumor Jinak Kolorektal | http://terminology.kemkes.go.id/sp |
| 212 | 1259 | Observation | `Observation.valueCodeableConcept.coding` | SP000110 | Curiga Kanker Kolorektal | http://terminology.kemkes.go.id/sp |
| 213 | 1260 | Observation | `Observation.valueCodeableConcept.coding` | 162572001 | Suspected malignancy | http://snomed.info/sct |
| 214 | 1261 | Observation | `Observation.referenceRange.appliesTo.coding` | SP000113 | Orang dengan Risiko Tinggi Kanker Kolorektal | http://terminology.kemkes.go.id/sp |
| 215 | 1271 | Observation | `Observation.code.coding` | SP000114 | Suspek Thalassemia | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 124 |
| http://loinc.org | 48 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 19 |
| http://terminology.kemkes.go.id/sp | 19 |
| http://terminology.kemkes.go.id/CodeSystem/examination | 2 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 2 |
| http://hl7.org/fhir/sid/icd-10 | 1 |
| **Total** | **215** |

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
