# Output Form: ASIK - CKG Balita dan Anak Pra-Sekolah (versi 2, tarikan baru)

Sumber: `mapping/phdt-data-dictionary-asik-ckg-balita.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-asik-ckg-balita.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 32 |
| Code (`jumlah code` = 1) | 102 |
| Code unik (code + CodeSystem) | 73 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 10 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–27 | Patient | – | – | _Nama Pasien_ → `Patient.name.text` (2, tanpa BQ)<br>_NIK_ → `Patient.identifier.value` (5, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (7, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (9, tanpa BQ)<br>_No HP_ → `Patient.contact.telecom.value` (11, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (18, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (21, tanpa BQ) |
| 2 | 71–84 | Encounter | – | – | _Tanggal Pelayanan_ → `Encounter.period.start` (79, tanpa BQ) |
| 3 | 85–91 | Condition | Z01.8 | Other specified special examinations | – |
| 4 | 102–113 | Observation | 424144002.0 | Current chronological age | _Usia_ → `Observation.valueQuantity.value` (105, tanpa BQ) |
| 5 | 114–299 | QuestionnaireResponse | – | – | _KPSP_ → `QuestionnaireResponse.item.linkId` (153, tanpa BQ)<br>_KMPE_ → `QuestionnaireResponse.item.linkId` (158, tanpa BQ)<br>_MCHAT-R_ → `QuestionnaireResponse.item.linkId` (162, tanpa BQ)<br>_Apakah anak Anda pernah atau sedang mengalami batuk yang tidak sembuh-sembuh selama lebih dari 2 minggu?_ → `QuestionnaireResponse.item.item.linkId` (169, tanpa BQ)<br>_Apakah berat badan anak Anda turun tanpa alasan yang jelas?_ → `QuestionnaireResponse.item.item.linkId` (173, tanpa BQ)<br>_Apakah berat badan anak Anda tidak naik dalam dua bulan terakhir?_ → `QuestionnaireResponse.item.item.linkId` (177, tanpa BQ)<br>_Apakah anak Anda tidak atau berkurang nafsu makan?_ → `QuestionnaireResponse.item.item.linkId` (181, tanpa BQ)<br>_Apakah Anda tinggal serumah atau sering bertemu dengan orang yang menderita Tuberkulosis (TBC) atau batuk berkepanjangan?_ → `QuestionnaireResponse.item.item.linkId` (185, tanpa BQ)<br>_Demam yang tidak diketahui penyebabnya >= 2 pekan_ → `QuestionnaireResponse.item.item.linkId` (194, tanpa BQ)<br>_Pembesaran kelenjar limfe kolli, aksila, inguinal_ → `QuestionnaireResponse.item.item.linkId` (198, tanpa BQ)<br>_Pembengkakan tulang/sendi panggul, lutut_ → `QuestionnaireResponse.item.item.linkId` (203, tanpa BQ)<br>_Indurasi Tes Mantoux_ → `QuestionnaireResponse.item.item.linkId` (207, tanpa BQ)<br>_Hasil Tes Mantoux_ → `QuestionnaireResponse.item.item.linkId` (211, tanpa BQ)<br>_Hasil Skoring TB Anak Dengan Kontak_ → `QuestionnaireResponse.item.item.linkId` (221, tanpa BQ)<br>_Apakah Anda tinggal serumah atau sering bertemu dengan orang yang menderita Tuberkulosis (TBC) atau batuk berkepanjangan?_ → `QuestionnaireResponse.item.item.linkId` (230, tanpa BQ)<br>_Hasil Tes Daya Dengar_ → `QuestionnaireResponse.item.linkId` (234, tanpa BQ)<br>_Hasil Pemeriksaan Pupil Putih_ → `QuestionnaireResponse.item.item.linkId` (240, tanpa BQ)<br>_Hasil Tes Daya Lihat_ → `QuestionnaireResponse.item.item.linkId` (244, tanpa BQ)<br>_Gigi Karies_ → `QuestionnaireResponse.item.linkId` (248, tanpa BQ)<br>_Transfusi Darah Rutin - Talasemia_ → `QuestionnaireResponse.item.item.linkId` (254, tanpa BQ)<br>_Pembawa Sifat - Talasemia_ → `QuestionnaireResponse.item.item.linkId` (258, tanpa BQ)<br>_Gejala DM Anak 17_ → `QuestionnaireResponse.item.item.linkId` (270, tanpa BQ)<br>_Gejala DM Anak 18_ → `QuestionnaireResponse.item.item.linkId` (274, tanpa BQ)<br>_Gejala DM Anak 19_ → `QuestionnaireResponse.item.item.linkId` (278, tanpa BQ)<br>_Gejala DM Anak 20_ → `QuestionnaireResponse.item.item.linkId` (282, tanpa BQ)<br>_Gejala DM Anak 21_ → `QuestionnaireResponse.item.item.linkId` (286, tanpa BQ)<br>_Gejala DM Anak 22_ → `QuestionnaireResponse.item.item.linkId` (290, tanpa BQ) |
| 6 | 300–311 | Observation | 29463-7 | Body weight | _Berat Badan_ → `Observation.valueQuantity.value` (303, tanpa BQ) |
| 7 | 312–324 | Observation | 8308-9 | Body height --standing | _Tinggi Badan_ → `Observation.valueQuantity.value` (316, tanpa BQ) |
| 8 | 325–350 | Observation | 1153593003.0 | Weight for age z-score | _Status Gizi BB/U (1-5 Tahun)_ → `Observation.valueRange.low.value` (328, tanpa BQ) |
| 9 | 351–377 | Observation | 1153604005.0 | Body height for age z-score | _Status Gizi PB/U atau TB/U (1-5 Tahun)_ → `Observation.valueRange.low.value` (355, tanpa BQ) |
| 10 | 378–414 | Observation | 1153600001.0 | Weight for height z-score | _Status Gizi BB/PB atau BB/TB (1-5 Tahun)_ → `Observation.valueRange.low.value` (382, tanpa BQ) |
| 11 | 415–473 | Observation | 1153596006.0 | Body mass index for age z-score | _IMT/U (5-6 Tahun)_ → `Observation.valueRange.low.value` (419, tanpa BQ) |
| 12 | 474–494 | Observation | 1153594009.0 | Head circumference for age z-score | _Lingkar Kepala_ → `Observation.valueRange.low.value` (477, tanpa BQ) |
| 13 | 495–506 | Observation | SP000450 | Faktor Risiko Tuberkulosis | _Faktor Risiko Tuberkulosis Anak_ → `Observation.valueCodeableConcept.coding` (498, tanpa BQ) |
| 14 | 507–518 | Observation | SP000451 | Faktor Risiko Talasemia | _Faktor Risiko Talasemia_ → `Observation.valueCodeableConcept.coding` (510, tanpa BQ) |
| 15 | 519–530 | Observation | SP000452 | Keluhan dan Gejala Diabetes Melitus Pada Bayi dan Anak Prasekolah | _Keluhan dan Gejala DM Pada Bayi dan Anak Prasekolah_ → `Observation.valueCodeableConcept.coding` (522, tanpa BQ) |
| 16 | 531–540 | ServiceRequest | – | – | – |
| 17 | 541–544 | PractitionerRole | – | – | – |
| 18 | 545–552 | Specimen | – | – | – |
| 19 | 553–578 | Observation | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | _Pemeriksaan Gula Darah Sewaktu_ → `Observation.valueRange.low.value` (556, tanpa BQ) |
| 20 | 579–590 | DiagnosticReport | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | – |
| 21 | 591–600 | ServiceRequest | – | – | – |
| 22 | 601–604 | PractitionerRole | – | – | – |
| 23 | 605–612 | Specimen | – | – | – |
| 24 | 613–628 | Observation | 718-7 | Hemoglobin [Mass/volume] in Blood | _HB - Talasemia_ → `Observation.valueRange.high.value` (616, tanpa BQ) |
| 25 | 629–644 | Observation | 30428-7 | MCV [Entitic volume] | _Skrining Lanjutan Talasemia 1 (MCV)_ → `Observation.valueRange.high.value` (632, tanpa BQ) |
| 26 | 645–660 | Observation | 28539-5 | MCH [Entitic mass] | _Skrining Lanjutan Talasemia 2 (MCH)_ → `Observation.valueRange.high.value` (648, tanpa BQ) |
| 27 | 661–672 | Observation | 789-8 | Erythrocytes [#/volume] in Blood by Automated count | _Skrining Lanjutan Talasemia 3 (RBC)_ → `Observation.valueQuantity.value` (664, tanpa BQ) |
| 28 | 673–684 | Observation | 788-0 | Erythrocyte distribution width [Ratio] by Automated count | _Skrining Lanjutan Talasemia 4 (RDW)_ → `Observation.valueQuantity.value` (676, tanpa BQ) |
| 29 | 685–696 | DiagnosticReport | 58410-2 | CBC panel - Blood by Automated count | – |
| 30 | 697–707 | Procedure | SP000496 | Skrining Gangguan Pemusatan Perhatian dan Hiperaktivitas (GPPH) | _Skrining GPPH_ → `Procedure.category.coding` (697, tanpa BQ) |
| 31 | 708–719 | Procedure | 710075007.0 | Screening for child development | _Skrining KPSP_ → `Procedure.category.coding` (708, tanpa BQ) |
| 32 | 720–731 | Procedure | 866042005.0 | Screening for autistic disorder | _Skrining MCHAT_ → `Procedure.category.coding` (720, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 17 |
| Procedure | 3 |
| ServiceRequest | 2 |
| PractitionerRole | 2 |
| Specimen | 2 |
| DiagnosticReport | 2 |
| Patient | 1 |
| Encounter | 1 |
| Condition | 1 |
| QuestionnaireResponse | 1 |
| **Total** | **32** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 87 | Condition | `Condition.code.coding` | Z01.8 | Other specified special examinations | http://hl7.org/fhir/sid/icd-10 |
| 2 | 104 | Observation | `Observation.code.coding` | 424144002.0 | Current chronological age | http://snomed.info/sct |
| 3 | 147 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 1145403003.0 | Macrocephaly | http://snomed.info/sct |
| 4 | 148 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 840673007.0 | Normal Head | http://snomed.info/sct |
| 5 | 149 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 1148757008.0 | Microcephaly | http://snomed.info/sct |
| 6 | 155 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | Ds | Perkembangan sesuai usia | http://terminology.kemkes.go.id/Codesystem/kpsp |
| 7 | 156 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | Dm | Perkembangan meragukan | http://terminology.kemkes.go.id/Codesystem/kpsp |
| 8 | 157 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | Dp | Perkembangan curiga adanya penyimpangan | http://terminology.kemkes.go.id/Codesystem/kpsp |
| 9 | 160 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 17621005.0 | Normal | http://snomed.info/sct |
| 10 | 161 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 410519009.0 | At risk | http://snomed.info/sct |
| 11 | 164 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 17621005.0 | Normal | http://snomed.info/sct |
| 12 | 165 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 410519009.0 | At risk | http://snomed.info/sct |
| 13 | 166 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 723509005.0 | High risk | http://snomed.info/sct |
| 14 | 200 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000154 | ≥1 cm, lebih dari 1 KGB, tidak nyeri | http://terminology.kemkes.go.id |
| 15 | 201 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000155 | <1 cm, lebih dari 1 KGB, tidak nyeri | http://terminology.kemkes.go.id |
| 16 | 202 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000156 | <1 cm, tidak nyeri | http://terminology.kemkes.go.id |
| 17 | 213 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000157 | Negatif <10 mm | http://terminology.kemkes.go.id |
| 18 | 214 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000158 | Negatif <5 mm pada imunokompromais | http://terminology.kemkes.go.id |
| 19 | 215 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000159 | Positif ≥10 mm | http://terminology.kemkes.go.id |
| 20 | 216 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000160 | Positif ≥5 mm pada imunokompromais | http://terminology.kemkes.go.id |
| 21 | 226 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000162 | Dugaan bukan Tuberkulosis klinis | http://terminology.kemkes.go.id |
| 22 | 229 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000161 | Dugaan Tuberkulosis klinis | http://terminology.kemkes.go.id |
| 23 | 236 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 17621005.0 | Normal | http://snomed.info/sct |
| 24 | 237 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 410519009.0 | At risk | http://snomed.info/sct |
| 25 | 242 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 17621005.0 | Normal | http://snomed.info/sct |
| 26 | 243 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000163 | Curiga kelainan pupil putih pada anak | http://terminology.kemkes.go.id |
| 27 | 246 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 45089002.0 | Normal vision | http://snomed.info/sct |
| 28 | 247 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 7973008.0 | Abnormal vision | http://snomed.info/sct |
| 29 | 302 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 30 | 314 | Observation | `Observation.code.coding` | 8308-9 | Body height --standing | http://loinc.org |
| 31 | 315 | Observation | `Observation.code.coding` | 8306-3 | Body height --lying | http://loinc.org |
| 32 | 327 | Observation | `Observation.code.coding` | 1153593003.0 | Weight for age z-score | http://snomed.info/sct |
| 33 | 332 | Observation | `Observation.interpretation.coding` | 248342006.0 | Underweight | http://snomed.info/sct |
| 34 | 337 | Observation | `Observation.interpretation.coding` | 43664005.0 | Normal weight | http://snomed.info/sct |
| 35 | 340 | Observation | `Observation.interpretation.coding` | OI000010 | Risiko Berat Badan Lebih | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 36 | 343 | Observation | `Observation.interpretation.coding` | OI000007 | Berat Badan Sangat Kurang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 37 | 353 | Observation | `Observation.code.coding` | 1153604005.0 | Body height for age z-score | http://snomed.info/sct |
| 38 | 354 | Observation | `Observation.code.coding` | 1153590000.0 | Length for age z score | http://snomed.info/sct |
| 39 | 359 | Observation | `Observation.interpretation.coding` | 17489000.0 | Body height normal for age | http://snomed.info/sct |
| 40 | 364 | Observation | `Observation.interpretation.coding` | 444000005.0 | Short stature for age | http://snomed.info/sct |
| 41 | 367 | Observation | `Observation.interpretation.coding` | OI000011 | Sangat Pendek | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 42 | 370 | Observation | `Observation.interpretation.coding` | 83077003.0 | Tall for age | http://snomed.info/sct |
| 43 | 380 | Observation | `Observation.code.coding` | 1153600001.0 | Weight for height z-score | http://snomed.info/sct |
| 44 | 381 | Observation | `Observation.code.coding` | 1153598007.0 | Weight for length z score | http://snomed.info/sct |
| 45 | 386 | Observation | `Observation.interpretation.coding` | 248324001.0 | Well nourished | http://snomed.info/sct |
| 46 | 389 | Observation | `Observation.interpretation.coding` | OI000001 | Gizi Buruk | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 47 | 394 | Observation | `Observation.interpretation.coding` | 248325000.0 | Undernourished | http://snomed.info/sct |
| 48 | 399 | Observation | `Observation.interpretation.coding` | 238131007.0 | Overweight | http://snomed.info/sct |
| 49 | 402 | Observation | `Observation.interpretation.coding` | 414915002.0 | Obese | http://snomed.info/sct |
| 50 | 407 | Observation | `Observation.interpretation.coding` | OI000004 | Risiko Gizi Lebih | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 51 | 417 | Observation | `Observation.code.coding` | 1153596006.0 | Body mass index for age z-score | http://snomed.info/sct |
| 52 | 423 | Observation | `Observation.interpretation.coding` | 248324001.0 | Well nourished | http://snomed.info/sct |
| 53 | 426 | Observation | `Observation.interpretation.coding` | OI000001 | Gizi Buruk | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 54 | 431 | Observation | `Observation.interpretation.coding` | 248325000.0 | Undernourished | http://snomed.info/sct |
| 55 | 436 | Observation | `Observation.interpretation.coding` | 238131007.0 | Overweight | http://snomed.info/sct |
| 56 | 439 | Observation | `Observation.interpretation.coding` | 414915002.0 | Obese | http://snomed.info/sct |
| 57 | 444 | Observation | `Observation.interpretation.coding` | OI000004 | Risiko Gizi Lebih | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 58 | 450 | Observation | `Observation.interpretation.coding` | 248324001.0 | Well nourished | http://snomed.info/sct |
| 59 | 453 | Observation | `Observation.interpretation.coding` | OI000001 | Gizi Buruk | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 60 | 458 | Observation | `Observation.interpretation.coding` | 248325000.0 | Undernourished | http://snomed.info/sct |
| 61 | 463 | Observation | `Observation.interpretation.coding` | 238131007.0 | Overweight | http://snomed.info/sct |
| 62 | 466 | Observation | `Observation.interpretation.coding` | 414915002.0 | Obese | http://snomed.info/sct |
| 63 | 476 | Observation | `Observation.code.coding` | 1153594009.0 | Head circumference for age z-score | http://snomed.info/sct |
| 64 | 481 | Observation | `Observation.interpretation.coding` | 840673007.0 | Normal head | http://snomed.info/sct |
| 65 | 484 | Observation | `Observation.interpretation.coding` | 1148757008.0 | Microcephaly | http://snomed.info/sct |
| 66 | 487 | Observation | `Observation.interpretation.coding` | 1145403003.0 | Macrocephaly | http://snomed.info/sct |
| 67 | 497 | Observation | `Observation.code.coding` | SP000450 | Faktor Risiko Tuberkulosis | http://terminology.kemkes.go.id/sp |
| 68 | 498 | Observation | `Observation.valueCodeableConcept.coding` | SP000455 | Ada Risiko | http://terminology.kemkes.go.id/sp |
| 69 | 499 | Observation | `Observation.valueCodeableConcept.coding` | SP000456 | Tidak Ada Risiko | http://terminology.kemkes.go.id/sp |
| 70 | 509 | Observation | `Observation.code.coding` | SP000451 | Faktor Risiko Talasemia | http://terminology.kemkes.go.id/sp |
| 71 | 510 | Observation | `Observation.valueCodeableConcept.coding` | SP000455 | Ada Risiko | http://terminology.kemkes.go.id/sp |
| 72 | 511 | Observation | `Observation.valueCodeableConcept.coding` | SP000456 | Tidak Ada Risiko | http://terminology.kemkes.go.id/sp |
| 73 | 521 | Observation | `Observation.code.coding` | SP000452 | Keluhan dan Gejala Diabetes Melitus Pada Bayi dan Anak Prasekolah | http://terminology.kemkes.go.id/sp |
| 74 | 522 | Observation | `Observation.valueCodeableConcept.coding` | SP000453 | Tidak Ada Keluhan dan Gejala Diabetes | http://terminology.kemkes.go.id/sp |
| 75 | 523 | Observation | `Observation.valueCodeableConcept.coding` | SP000454 | Ada Keluhan dan Gejala Diabetes | http://terminology.kemkes.go.id/sp |
| 76 | 535 | ServiceRequest | `ServiceRequest.code` | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 77 | 543 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002.0 | Laboratory worker | http://snomed.info/sct |
| 78 | 546 | Specimen | `Specimen.type` | 119297000.0 | Blood specimen | http://snomed.info/sct |
| 79 | 555 | Observation | `Observation.code.coding` | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 80 | 560 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 81 | 565 | Observation | `Observation.interpretation.coding` | 714628002.0 | Prediabetes | http://snomed.info/sct |
| 82 | 568 | Observation | `Observation.interpretation.coding` | 302866003.0 | Hypoglycemia | http://snomed.info/sct |
| 83 | 571 | Observation | `Observation.interpretation.coding` | 80394007.0 | Hyperglycemia | http://snomed.info/sct |
| 84 | 581 | DiagnosticReport | `DiagnosticReport.code.coding` | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 85 | 595 | ServiceRequest | `ServiceRequest.code` | 58410-2 | CBC panel - Blood by Automated count | http://loinc.org |
| 86 | 603 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002.0 | Laboratory worker | http://snomed.info/sct |
| 87 | 606 | Specimen | `Specimen.type` | 119297000.0 | Blood specimen | http://snomed.info/sct |
| 88 | 615 | Observation | `Observation.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 89 | 618 | Observation | `Observation.interpretation.coding` | 271737000.0 | Anemia | http://snomed.info/sct |
| 90 | 621 | Observation | `Observation.interpretation.coding` | 860635002.0 | No anemia present | http://snomed.info/sct |
| 91 | 631 | Observation | `Observation.code.coding` | 30428-7 | MCV [Entitic volume] | http://loinc.org |
| 92 | 634 | Observation | `Observation.interpretation.coding` | L | Low | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 93 | 637 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 94 | 647 | Observation | `Observation.code.coding` | 28539-5 | MCH [Entitic mass] | http://loinc.org |
| 95 | 650 | Observation | `Observation.interpretation.coding` | L | Low | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 96 | 653 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 97 | 663 | Observation | `Observation.code.coding` | 789-8 | Erythrocytes [#/volume] in Blood by Automated count | http://loinc.org |
| 98 | 675 | Observation | `Observation.code.coding` | 788-0 | Erythrocyte distribution width [Ratio] by Automated count | http://loinc.org |
| 99 | 687 | DiagnosticReport | `DiagnosticReport.code.coding` | 58410-2 | CBC panel - Blood by Automated count | http://loinc.org |
| 100 | 698 | Procedure | `Procedure.code.coding` | SP000496 | Skrining Gangguan Pemusatan Perhatian dan Hiperaktivitas (GPPH) | http://terminology.kemkes.go.id/sp |
| 101 | 709 | Procedure | `Procedure.code.coding` | 710075007.0 | Screening for child development | http://snomed.info/sct |
| 102 | 721 | Procedure | `Procedure.code.coding` | 866042005.0 | Screening for autistic disorder | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 52 |
| http://loinc.org | 13 |
| http://terminology.kemkes.go.id | 10 |
| http://terminology.kemkes.go.id/sp | 10 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 8 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 5 |
| http://terminology.kemkes.go.id/Codesystem/kpsp | 3 |
| http://hl7.org/fhir/sid/icd-10 | 1 |
| **Total** | **102** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 30 | – | ID Faskes | Organization | `Organization.id` |
| 32 | – | Nama Faskes | Organization | `Organization.name` |
| 732 | – | Kode Faskes | – | `` |
