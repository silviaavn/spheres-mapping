# Output Form: ASIK - CKG Balita dan Anak Pra-Sekolah (versi 1)

Sumber: `mapping/phdt-data-dictionary-asik-ckg-balita-v1.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-asik-ckg-balita-v1.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 29 |
| Code (`jumlah code` = 1) | 99 |
| Code unik (code + CodeSystem) | 70 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 9 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–27 | Patient | – | – | _Nama Pasien_ → `Patient.name.text` (2, tanpa BQ)<br>_NIK_ → `Patient.identifier.value` (5, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (7, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (9, tanpa BQ)<br>_No HP_ → `Patient.contact.telecom.value` (11, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.url` (16, tanpa BQ)<br>_Kode Provinsi_ → `Patient.address.extension.extension.valueCode` (18, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.url` (19, tanpa BQ)<br>_Kode Kabupaten_ → `Patient.address.extension.extension.valueCode` (21, tanpa BQ) |
| 2 | 71–84 | Encounter | – | – | _Tanggal Pelayanan_ → `Encounter.period.start` (79, tanpa BQ) |
| 3 | 85–91 | Condition | Z01.8 | Other specified special examinations | – |
| 4 | 102–113 | Observation | 424144002.0 | Current chronological age | _Usia_ → `Observation.valueQuantity.value` (105, tanpa BQ) |
| 5 | 114–313 | QuestionnaireResponse | – | – | _Skrining Perkembangan 1_ → `QuestionnaireResponse.item.item.linkId` (155, tanpa BQ)<br>_Skrining Perkembangan 2_ → `QuestionnaireResponse.item.item.linkId` (159, tanpa BQ)<br>_Skrining Perkembangan 3_ → `QuestionnaireResponse.item.item.linkId` (163, tanpa BQ)<br>_KPSP_ → `QuestionnaireResponse.item.linkId` (167, tanpa BQ)<br>_KMPE_ → `QuestionnaireResponse.item.linkId` (172, tanpa BQ)<br>_MCHAT-R_ → `QuestionnaireResponse.item.linkId` (176, tanpa BQ)<br>_Apakah anak Anda pernah atau sedang mengalami batuk yang tidak sembuh-sembuh selama lebih dari 2 minggu?_ → `QuestionnaireResponse.item.item.linkId` (183, tanpa BQ)<br>_Apakah berat badan anak Anda turun tanpa alasan yang jelas?_ → `QuestionnaireResponse.item.item.linkId` (187, tanpa BQ)<br>_Apakah berat badan anak Anda tidak naik dalam dua bulan terakhir?_ → `QuestionnaireResponse.item.item.linkId` (191, tanpa BQ)<br>_Apakah anak Anda tidak atau berkurang nafsu makan?_ → `QuestionnaireResponse.item.item.linkId` (195, tanpa BQ)<br>_Apakah Anda tinggal serumah atau sering bertemu dengan orang yang menderita Tuberkulosis (TBC) atau batuk berkepanjangan?_ → `QuestionnaireResponse.item.item.linkId` (199, tanpa BQ)<br>_Demam yang tidak diketahui penyebabnya >= 2 pekan_ → `QuestionnaireResponse.item.item.linkId` (208, tanpa BQ)<br>_Pembesaran kelenjar limfe kolli, aksila, inguinal_ → `QuestionnaireResponse.item.item.linkId` (212, tanpa BQ)<br>_Pembengkakan tulang/sendi panggul, lutut_ → `QuestionnaireResponse.item.item.linkId` (217, tanpa BQ)<br>_Indurasi Tes Mantoux_ → `QuestionnaireResponse.item.item.linkId` (221, tanpa BQ)<br>_Hasil Tes Mantoux_ → `QuestionnaireResponse.item.item.linkId` (225, tanpa BQ)<br>_Hasil Skoring TB Anak Dengan Kontak_ → `QuestionnaireResponse.item.item.linkId` (235, tanpa BQ)<br>_Apakah Anda tinggal serumah atau sering bertemu dengan orang yang menderita Tuberkulosis (TBC) atau batuk berkepanjangan?_ → `QuestionnaireResponse.item.item.linkId` (244, tanpa BQ)<br>_Hasil Tes Daya Dengar_ → `QuestionnaireResponse.item.linkId` (248, tanpa BQ)<br>_Hasil Pemeriksaan Pupil Putih_ → `QuestionnaireResponse.item.item.linkId` (254, tanpa BQ)<br>_Hasil Tes Daya Lihat_ → `QuestionnaireResponse.item.item.linkId` (258, tanpa BQ)<br>_Gigi Karies_ → `QuestionnaireResponse.item.linkId` (262, tanpa BQ)<br>_Transfusi Darah Rutin - Talasemia_ → `QuestionnaireResponse.item.item.linkId` (268, tanpa BQ)<br>_Pembawa Sifat - Talasemia_ → `QuestionnaireResponse.item.item.linkId` (272, tanpa BQ)<br>_Gejala DM Anak 17_ → `QuestionnaireResponse.item.item.linkId` (284, tanpa BQ)<br>_Gejala DM Anak 18_ → `QuestionnaireResponse.item.item.linkId` (288, tanpa BQ)<br>_Gejala DM Anak 19_ → `QuestionnaireResponse.item.item.linkId` (292, tanpa BQ)<br>_Gejala DM Anak 20_ → `QuestionnaireResponse.item.item.linkId` (296, tanpa BQ)<br>_Gejala DM Anak 21_ → `QuestionnaireResponse.item.item.linkId` (300, tanpa BQ)<br>_Gejala DM Anak 22_ → `QuestionnaireResponse.item.item.linkId` (304, tanpa BQ) |
| 6 | 314–325 | Observation | 29463-7 | Body weight | _Berat Badan_ → `Observation.valueQuantity.value` (317, tanpa BQ) |
| 7 | 326–338 | Observation | 8308-9 | Body height --standing | _Tinggi Badan_ → `Observation.valueQuantity.value` (330, tanpa BQ) |
| 8 | 339–364 | Observation | 1153593003.0 | Weight for age z-score | _Status Gizi BB/U (1-5 Tahun)_ → `Observation.valueRange.low.value` (342, tanpa BQ) |
| 9 | 365–391 | Observation | 1153604005.0 | Body height for age z-score | _Status Gizi PB/U atau TB/U (1-5 Tahun)_ → `Observation.valueRange.low.value` (369, tanpa BQ) |
| 10 | 392–428 | Observation | 1153600001.0 | Weight for height z-score | _Status Gizi BB/PB atau BB/TB (1-5 Tahun)_ → `Observation.valueRange.low.value` (396, tanpa BQ) |
| 11 | 429–487 | Observation | 1153596006.0 | Body mass index for age z-score | _IMT/U (5-6 Tahun)_ → `Observation.valueRange.low.value` (433, tanpa BQ) |
| 12 | 488–508 | Observation | 1153594009.0 | Head circumference for age z-score | _Lingkar Kepala_ → `Observation.valueRange.low.value` (491, tanpa BQ) |
| 13 | 509–520 | Observation | SP000450 | Faktor Risiko Tuberkulosis | _Faktor Risiko Tuberkulosis Anak_ → `Observation.valueCodeableConcept.coding` (512, tanpa BQ) |
| 14 | 521–532 | Observation | SP000451 | Faktor Risiko Talasemia | _Faktor Risiko Talasemia_ → `Observation.valueCodeableConcept.coding` (524, tanpa BQ) |
| 15 | 533–544 | Observation | SP000452 | Keluhan dan Gejala Diabetes Melitus Pada Bayi dan Anak Prasekolah | _Keluhan dan Gejala DM Pada Bayi dan Anak Prasekolah_ → `Observation.valueCodeableConcept.coding` (536, tanpa BQ) |
| 16 | 545–554 | ServiceRequest | – | – | – |
| 17 | 555–558 | PractitionerRole | – | – | – |
| 18 | 559–566 | Specimen | – | – | – |
| 19 | 567–592 | Observation | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | _Pemeriksaan Gula Darah Sewaktu_ → `Observation.valueRange.low.value` (570, tanpa BQ) |
| 20 | 593–604 | DiagnosticReport | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | – |
| 21 | 605–614 | ServiceRequest | – | – | – |
| 22 | 615–618 | PractitionerRole | – | – | – |
| 23 | 619–626 | Specimen | – | – | – |
| 24 | 627–642 | Observation | 718-7 | Hemoglobin [Mass/volume] in Blood | _HB - Talasemia_ → `Observation.valueRange.high.value` (630, tanpa BQ) |
| 25 | 643–658 | Observation | 30428-7 | MCV [Entitic volume] | _Skrining Lanjutan Talasemia 1 (MCV)_ → `Observation.valueRange.high.value` (646, tanpa BQ) |
| 26 | 659–674 | Observation | 28539-5 | MCH [Entitic mass] | _Skrining Lanjutan Talasemia 2 (MCH)_ → `Observation.valueRange.high.value` (662, tanpa BQ) |
| 27 | 675–686 | Observation | 789-8 | Erythrocytes [#/volume] in Blood by Automated count | _Skrining Lanjutan Talasemia 3 (RBC)_ → `Observation.valueQuantity.value` (678, tanpa BQ) |
| 28 | 687–698 | Observation | 788-0 | Erythrocyte distribution width [Ratio] by Automated count | _Skrining Lanjutan Talasemia 4 (RDW)_ → `Observation.valueQuantity.value` (690, tanpa BQ) |
| 29 | 699–710 | DiagnosticReport | 58410-2 | CBC panel - Blood by Automated count | – |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 17 |
| ServiceRequest | 2 |
| PractitionerRole | 2 |
| Specimen | 2 |
| DiagnosticReport | 2 |
| Patient | 1 |
| Encounter | 1 |
| Condition | 1 |
| QuestionnaireResponse | 1 |
| **Total** | **29** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 87 | Condition | `Condition.code.coding` | Z01.8 | Other specified special examinations | http://hl7.org/fhir/sid/icd-10 |
| 2 | 104 | Observation | `Observation.code.coding` | 424144002.0 | Current chronological age | http://snomed.info/sct |
| 3 | 147 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 1145403003.0 | Macrocephaly | http://snomed.info/sct |
| 4 | 148 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 840673007.0 | Normal Head | http://snomed.info/sct |
| 5 | 149 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 1148757008.0 | Microcephaly | http://snomed.info/sct |
| 6 | 169 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | Ds | Perkembangan sesuai usia | http://terminology.kemkes.go.id/Codesystem/kpsp |
| 7 | 170 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | Dm | Perkembangan meragukan | http://terminology.kemkes.go.id/Codesystem/kpsp |
| 8 | 171 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | Dp | Perkembangan curiga adanya penyimpangan | http://terminology.kemkes.go.id/Codesystem/kpsp |
| 9 | 174 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 17621005.0 | Normal | http://snomed.info/sct |
| 10 | 175 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 410519009.0 | At risk | http://snomed.info/sct |
| 11 | 178 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 17621005.0 | Normal | http://snomed.info/sct |
| 12 | 179 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 410519009.0 | At risk | http://snomed.info/sct |
| 13 | 180 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 723509005.0 | High risk | http://snomed.info/sct |
| 14 | 214 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000154 | ≥1 cm, lebih dari 1 KGB, tidak nyeri | http://terminology.kemkes.go.id |
| 15 | 215 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000155 | <1 cm, lebih dari 1 KGB, tidak nyeri | http://terminology.kemkes.go.id |
| 16 | 216 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000156 | <1 cm, tidak nyeri | http://terminology.kemkes.go.id |
| 17 | 227 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000157 | Negatif <10 mm | http://terminology.kemkes.go.id |
| 18 | 228 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000158 | Negatif <5 mm pada imunokompromais | http://terminology.kemkes.go.id |
| 19 | 229 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000159 | Positif ≥10 mm | http://terminology.kemkes.go.id |
| 20 | 230 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000160 | Positif ≥5 mm pada imunokompromais | http://terminology.kemkes.go.id |
| 21 | 240 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000162 | Dugaan bukan Tuberkulosis klinis | http://terminology.kemkes.go.id |
| 22 | 243 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000161 | Dugaan Tuberkulosis klinis | http://terminology.kemkes.go.id |
| 23 | 250 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 17621005.0 | Normal | http://snomed.info/sct |
| 24 | 251 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 410519009.0 | At risk | http://snomed.info/sct |
| 25 | 256 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 17621005.0 | Normal | http://snomed.info/sct |
| 26 | 257 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000163 | Curiga kelainan pupil putih pada anak | http://terminology.kemkes.go.id |
| 27 | 260 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 45089002.0 | Normal vision | http://snomed.info/sct |
| 28 | 261 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 7973008.0 | Abnormal vision | http://snomed.info/sct |
| 29 | 316 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 30 | 328 | Observation | `Observation.code.coding` | 8308-9 | Body height --standing | http://loinc.org |
| 31 | 329 | Observation | `Observation.code.coding` | 8306-3 | Body height --lying | http://loinc.org |
| 32 | 341 | Observation | `Observation.code.coding` | 1153593003.0 | Weight for age z-score | http://snomed.info/sct |
| 33 | 346 | Observation | `Observation.interpretation.coding` | 248342006.0 | Underweight | http://snomed.info/sct |
| 34 | 351 | Observation | `Observation.interpretation.coding` | 43664005.0 | Normal weight | http://snomed.info/sct |
| 35 | 354 | Observation | `Observation.interpretation.coding` | OI000010 | Risiko Berat Badan Lebih | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 36 | 357 | Observation | `Observation.interpretation.coding` | OI000007 | Berat Badan Sangat Kurang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 37 | 367 | Observation | `Observation.code.coding` | 1153604005.0 | Body height for age z-score | http://snomed.info/sct |
| 38 | 368 | Observation | `Observation.code.coding` | 1153590000.0 | Length for age z score | http://snomed.info/sct |
| 39 | 373 | Observation | `Observation.interpretation.coding` | 17489000.0 | Body height normal for age | http://snomed.info/sct |
| 40 | 378 | Observation | `Observation.interpretation.coding` | 444000005.0 | Short stature for age | http://snomed.info/sct |
| 41 | 381 | Observation | `Observation.interpretation.coding` | OI000011 | Sangat Pendek | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 42 | 384 | Observation | `Observation.interpretation.coding` | 83077003.0 | Tall for age | http://snomed.info/sct |
| 43 | 394 | Observation | `Observation.code.coding` | 1153600001.0 | Weight for height z-score | http://snomed.info/sct |
| 44 | 395 | Observation | `Observation.code.coding` | 1153598007.0 | Weight for length z score | http://snomed.info/sct |
| 45 | 400 | Observation | `Observation.interpretation.coding` | 248324001.0 | Well nourished | http://snomed.info/sct |
| 46 | 403 | Observation | `Observation.interpretation.coding` | OI000001 | Gizi Buruk | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 47 | 408 | Observation | `Observation.interpretation.coding` | 248325000.0 | Undernourished | http://snomed.info/sct |
| 48 | 413 | Observation | `Observation.interpretation.coding` | 238131007.0 | Overweight | http://snomed.info/sct |
| 49 | 416 | Observation | `Observation.interpretation.coding` | 414915002.0 | Obese | http://snomed.info/sct |
| 50 | 421 | Observation | `Observation.interpretation.coding` | OI000004 | Risiko Gizi Lebih | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 51 | 431 | Observation | `Observation.code.coding` | 1153596006.0 | Body mass index for age z-score | http://snomed.info/sct |
| 52 | 437 | Observation | `Observation.interpretation.coding` | 248324001.0 | Well nourished | http://snomed.info/sct |
| 53 | 440 | Observation | `Observation.interpretation.coding` | OI000001 | Gizi Buruk | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 54 | 445 | Observation | `Observation.interpretation.coding` | 248325000.0 | Undernourished | http://snomed.info/sct |
| 55 | 450 | Observation | `Observation.interpretation.coding` | 238131007.0 | Overweight | http://snomed.info/sct |
| 56 | 453 | Observation | `Observation.interpretation.coding` | 414915002.0 | Obese | http://snomed.info/sct |
| 57 | 458 | Observation | `Observation.interpretation.coding` | OI000004 | Risiko Gizi Lebih | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 58 | 464 | Observation | `Observation.interpretation.coding` | 248324001.0 | Well nourished | http://snomed.info/sct |
| 59 | 467 | Observation | `Observation.interpretation.coding` | OI000001 | Gizi Buruk | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 60 | 472 | Observation | `Observation.interpretation.coding` | 248325000.0 | Undernourished | http://snomed.info/sct |
| 61 | 477 | Observation | `Observation.interpretation.coding` | 238131007.0 | Overweight | http://snomed.info/sct |
| 62 | 480 | Observation | `Observation.interpretation.coding` | 414915002.0 | Obese | http://snomed.info/sct |
| 63 | 490 | Observation | `Observation.code.coding` | 1153594009.0 | Head circumference for age z-score | http://snomed.info/sct |
| 64 | 495 | Observation | `Observation.interpretation.coding` | 840673007.0 | Normal head | http://snomed.info/sct |
| 65 | 498 | Observation | `Observation.interpretation.coding` | 1148757008.0 | Microcephaly | http://snomed.info/sct |
| 66 | 501 | Observation | `Observation.interpretation.coding` | 1145403003.0 | Macrocephaly | http://snomed.info/sct |
| 67 | 511 | Observation | `Observation.code.coding` | SP000450 | Faktor Risiko Tuberkulosis | http://terminology.kemkes.go.id/sp |
| 68 | 512 | Observation | `Observation.valueCodeableConcept.coding` | SP000455 | Ada Risiko | http://terminology.kemkes.go.id/sp |
| 69 | 513 | Observation | `Observation.valueCodeableConcept.coding` | SP000456 | Tidak Ada Risiko | http://terminology.kemkes.go.id/sp |
| 70 | 523 | Observation | `Observation.code.coding` | SP000451 | Faktor Risiko Talasemia | http://terminology.kemkes.go.id/sp |
| 71 | 524 | Observation | `Observation.valueCodeableConcept.coding` | SP000455 | Ada Risiko | http://terminology.kemkes.go.id/sp |
| 72 | 525 | Observation | `Observation.valueCodeableConcept.coding` | SP000456 | Tidak Ada Risiko | http://terminology.kemkes.go.id/sp |
| 73 | 535 | Observation | `Observation.code.coding` | SP000452 | Keluhan dan Gejala Diabetes Melitus Pada Bayi dan Anak Prasekolah | http://terminology.kemkes.go.id/sp |
| 74 | 536 | Observation | `Observation.valueCodeableConcept.coding` | SP000453 | Tidak Ada Keluhan dan Gejala Diabetes | http://terminology.kemkes.go.id/sp |
| 75 | 537 | Observation | `Observation.valueCodeableConcept.coding` | SP000454 | Ada Keluhan dan Gejala Diabetes | http://terminology.kemkes.go.id/sp |
| 76 | 549 | ServiceRequest | `ServiceRequest.code` | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 77 | 557 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002.0 | Laboratory worker | http://snomed.info/sct |
| 78 | 560 | Specimen | `Specimen.type` | 119297000.0 | Blood specimen | http://snomed.info/sct |
| 79 | 569 | Observation | `Observation.code.coding` | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 80 | 574 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 81 | 579 | Observation | `Observation.interpretation.coding` | 714628002.0 | Prediabetes | http://snomed.info/sct |
| 82 | 582 | Observation | `Observation.interpretation.coding` | 302866003.0 | Hypoglycemia | http://snomed.info/sct |
| 83 | 585 | Observation | `Observation.interpretation.coding` | 80394007.0 | Hyperglycemia | http://snomed.info/sct |
| 84 | 595 | DiagnosticReport | `DiagnosticReport.code.coding` | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 85 | 609 | ServiceRequest | `ServiceRequest.code` | 58410-2 | CBC panel - Blood by Automated count | http://loinc.org |
| 86 | 617 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002.0 | Laboratory worker | http://snomed.info/sct |
| 87 | 620 | Specimen | `Specimen.type` | 119297000.0 | Blood specimen | http://snomed.info/sct |
| 88 | 629 | Observation | `Observation.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 89 | 632 | Observation | `Observation.interpretation.coding` | 271737000.0 | Anemia | http://snomed.info/sct |
| 90 | 635 | Observation | `Observation.interpretation.coding` | 860635002.0 | No anemia present | http://snomed.info/sct |
| 91 | 645 | Observation | `Observation.code.coding` | 30428-7 | MCV [Entitic volume] | http://loinc.org |
| 92 | 648 | Observation | `Observation.interpretation.coding` | L | Low | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 93 | 651 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 94 | 661 | Observation | `Observation.code.coding` | 28539-5 | MCH [Entitic mass] | http://loinc.org |
| 95 | 664 | Observation | `Observation.interpretation.coding` | L | Low | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 96 | 667 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 97 | 677 | Observation | `Observation.code.coding` | 789-8 | Erythrocytes [#/volume] in Blood by Automated count | http://loinc.org |
| 98 | 689 | Observation | `Observation.code.coding` | 788-0 | Erythrocyte distribution width [Ratio] by Automated count | http://loinc.org |
| 99 | 701 | DiagnosticReport | `DiagnosticReport.code.coding` | 58410-2 | CBC panel - Blood by Automated count | http://loinc.org |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 50 |
| http://loinc.org | 13 |
| http://terminology.kemkes.go.id | 10 |
| http://terminology.kemkes.go.id/sp | 9 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 8 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 5 |
| http://terminology.kemkes.go.id/Codesystem/kpsp | 3 |
| http://hl7.org/fhir/sid/icd-10 | 1 |
| **Total** | **99** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 30 | – | ID Faskes | Organization | `Organization.id` |
| 32 | – | Nama Faskes | Organization | `Organization.name` |
| 711 | – | Skrining GPPH | – | `` |
| 712 | – | Skrining KPSP | – | `` |
| 713 | – | Skrining MCHAT | – | `` |
| 714 | – | Kode Faskes | – | `` |
