# Output Form: Kobo - SDIDTK

Sumber: `mapping/phdt-data-dictionary-kobo-sdidtk.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-kobo-sdidtk.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 35 |
| Code (`jumlah code` = 1) | 92 |
| Code unik (code + CodeSystem) | 66 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 10 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–7 | Encounter | – | – | _Tanggal_ → `Encounter.period.start` (2, tanpa BQ) |
| 2 | 8–14 | Condition | – | – | – |
| 3 | 28–48 | Practitioner | – | – | _Nama Petugas_ → `Practitioner.identifier` (28, tanpa BQ) |
| 4 | 49–51 | Patient | – | – | _Nama Pasien_ → `Patient.name.text` (49, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (50, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (60, tanpa BQ) |
| 5 | 52–58 | RelatedPerson | – | – | _Nama Ayah_ → `RelatedPerson.patient` (52, tanpa BQ)<br>_Nama Ibu_ → `RelatedPerson.patient` (56, tanpa BQ) |
| 6 | 59–59 | RelatedPerson | – | – | – |
| 7 | 61–78 | Observation | 424144002 | Current chronological age | _Umur Anak_ → `Observation.valueQuantity.value` (64, tanpa BQ) |
| 8 | 79–85 | Condition | – | – | _Keluhan utama_ → `Condition.clinicalStatus.coding` (79, tanpa BQ) |
| 9 | 86–92 | Condition | – | – | _Masalah tumbuh kembang_ → `Condition.clinicalStatus.coding` (86, tanpa BQ) |
| 10 | 93–104 | Observation | 29463-7 | Body weight | _Berat Badan (BB)_ → `Observation.valueQuantity.value` (96, tanpa BQ) |
| 11 | 105–117 | Observation | 8308-9 | Body height --standing | _PB atau Tinggi Badan (TB)_ → `Observation.valueQuantity.value` (109, tanpa BQ) |
| 12 | 118–129 | Observation | 9843-4 | Head Occipital-frontal circumference | _Lingkar Kepala (LK)_ → `Observation.valueQuantity.value` (121, tanpa BQ) |
| 13 | 130–150 | Observation | 1153594009 | Head circumference for age z-score | _Lingkar Kepala / Umur_ → `Observation.valueRange.high.value` (133, tanpa BQ) |
| 14 | 151–187 | Observation | 1153600001 | Weight for height z-score | _Berat Badan / Tinggi Badan_ → `Observation.valueRange.high.value` (155, tanpa BQ) |
| 15 | 188–214 | Observation | 1153590000 | Length for age z-score | _Tinggi Badan / Umur_ → `Observation.valueRange.high.value` (192, tanpa BQ) |
| 16 | 215–245 | Observation | 1153596006 | Body mass index for age z-score | _IMT/U (60-72 bulan)_ → `Observation.valueRange.high.value` (218, tanpa BQ) |
| 17 | 246–260 | Observation | SP000059 | Tren Pertumbuhan Anak | _Tren Pertumbuhan_ → `Observation.valueCodeableConcept.coding` (249, tanpa BQ) |
| 18 | 261–268 | QuestionnaireResponse | https://fhir.kemkes.go.id/Questionnaire/Q0003 | – | _Kuisioner Pra-Skrining Perkembangan (KPSP)_ → `QuestionnaireResponse.questionnaire` (261, tanpa BQ) |
| 19 | 269–275 | QuestionnaireResponse | https://fhir.kemkes.go.id/Questionnaire/Q0003 | – | _Tes Daya Dengar (TDD) Anak_ → `QuestionnaireResponse.questionnaire` (269, tanpa BQ) |
| 20 | 276–282 | QuestionnaireResponse | https://fhir.kemkes.go.id/Questionnaire/Q0003 | – | _Tes Daya Lihat_ → `QuestionnaireResponse.questionnaire` (276, tanpa BQ) |
| 21 | 283–289 | QuestionnaireResponse | https://fhir.kemkes.go.id/Questionnaire/Q0003 | – | _Pemeriksaan Pupil Putih_ → `QuestionnaireResponse.questionnaire` (283, tanpa BQ) |
| 22 | 290–304 | Observation | 284473002 | Mid upper arm circumference | _Lingkar Lengan Atas (LILA)_ → `Observation.valueQuantity.value` (293, tanpa BQ)<br>_Klasifikasi LILA_ → `Observation.interpretation.coding` (302, tanpa BQ) |
| 23 | 305–340 | Observation | 1153596006 | Body mass index for age z-score | _IMT/U (0-59 bulan)_ → `Observation.valueRange.high.value` (308, tanpa BQ) |
| 24 | 341–348 | QuestionnaireResponse | https://fhir.kemkes.go.id/Questionnaire/Q0003 | – | _Kuisioner Masalah Perilaku Emosional (KMPE)_ → `QuestionnaireResponse.questionnaire` (341, tanpa BQ) |
| 25 | 349–355 | QuestionnaireResponse | https://fhir.kemkes.go.id/Questionnaire/Q0003 | – | _Modified Checklist for Autism in Toddler (M-CHAT)_ → `QuestionnaireResponse.questionnaire` (349, tanpa BQ) |
| 26 | 356–363 | QuestionnaireResponse | https://fhir.kemkes.go.id/Questionnaire/Q0003 | – | _Gangguan Pemusatan Perhatian/Hiperaktivitas (GPPH)_ → `QuestionnaireResponse.questionnaire` (356, tanpa BQ) |
| 27 | 364–369 | QuestionnaireResponse | https://fhir.kemkes.go.id/Questionnaire/Q0003 | – | _Kesimpulan_ → `QuestionnaireResponse.questionnaire` (364, tanpa BQ) |
| 28 | 370–380 | Procedure | 441041000124100 | Counseling about nutrition | _Konseling Gizi_ → `Procedure.category.coding` (370, tanpa BQ) |
| 29 | 381–391 | Procedure | 410295000 | Growth/development education, guidance, and counseling | _Konseling Stimulasi Perkembangan_ → `Procedure.category.coding` (381, tanpa BQ) |
| 30 | 392–402 | Procedure | SP000060 | Intervensi Dini Masalah Pertumbuhan Anak | _Intervensi Dini Masalah Pertumbuhan_ → `Procedure.category.coding` (392, tanpa BQ) |
| 31 | 403–415 | Observation | SP000061 | Intervensi Dini Masalah Perkembangan Anak | _Intervensi Dini Masalah Perkembangan_ → `Observation.valueCodeableConcept` (406, tanpa BQ) |
| 32 | 416–426 | Procedure | SP000063 | Intervensi Dini Masalah Perilaku & Emosi | _Intervensi Dini Masalah Perilaku & Emosi_ → `Procedure.category.coding` (416, tanpa BQ) |
| 33 | 427–438 | Observation | SP000064 | Tindakan Pengobatan Lain | _Tindakan Pengobatan Lain_ → `Observation.valueBoolean` (430, tanpa BQ) |
| 34 | 439–464 | ServiceRequest | – | – | _Dirujuk ke_ → `ServiceRequest.category` (439, tanpa BQ)<br>_Alasan dirujuk_ → `ServiceRequest.reasonCode.coding` (449, tanpa BQ) |
| 35 | 465–476 | Observation | OC000034 | Surat Pengantar Rujukan | _Surat rujukan_ → `Observation.valueBoolean` (468, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 14 |
| QuestionnaireResponse | 8 |
| Procedure | 4 |
| Condition | 3 |
| RelatedPerson | 2 |
| Encounter | 1 |
| Practitioner | 1 |
| Patient | 1 |
| ServiceRequest | 1 |
| **Total** | **35** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 63 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 2 | 66 | Observation | `Observation.component.code.coding` | SP000020 | Umur Bulan | http://terminology.kemkes.go.id/sp |
| 3 | 69 | Observation | `Observation.component.code.coding` | SP000021 | Umur Hari | http://terminology.kemkes.go.id/sp |
| 4 | 95 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 5 | 107 | Observation | `Observation.code.coding` | 8308-9 | Body height --standing | http://loinc.org |
| 6 | 108 | Observation | `Observation.code.coding` | 8306-3 | Body height --lying | http://loinc.org |
| 7 | 120 | Observation | `Observation.code.coding` | 9843-4 | Head Occipital-frontal circumference | http://loinc.org |
| 8 | 132 | Observation | `Observation.code.coding` | 1153594009 | Head circumference for age z-score | http://loinc.org |
| 9 | 135 | Observation | `Observation.interpretation.coding` | 1148757008 | Microcephaly | http://snomed.info/sct |
| 10 | 140 | Observation | `Observation.interpretation.coding` | 840673007 | Normal head | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 11 | 143 | Observation | `Observation.interpretation.coding` | 1145403003 | Macrocephaly | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 12 | 153 | Observation | `Observation.code.coding` | 1153600001 | Weight for height z-score | http://snomed.info/sct |
| 13 | 154 | Observation | `Observation.code.coding` | 1153598007 | Weight for length z score | http://snomed.info/sct |
| 14 | 157 | Observation | `Observation.interpretation.coding` | OI000001 | Gizi Buruk | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 15 | 162 | Observation | `Observation.interpretation.coding` | 248325000 | Undernourished | http://snomed.info/sct |
| 16 | 167 | Observation | `Observation.interpretation.coding` | 248324001 | Well nourished | http://snomed.info/sct |
| 17 | 172 | Observation | `Observation.interpretation.coding` | OI000004 | Risiko Gizi Lebih | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 18 | 177 | Observation | `Observation.interpretation.coding` | 238131007 | Overweight | http://snomed.info/sct |
| 19 | 180 | Observation | `Observation.interpretation.coding` | 414915002 | Obese | http://snomed.info/sct |
| 20 | 190 | Observation | `Observation.code.coding` | 1153590000 | Length for age z-score | http://snomed.info/sct |
| 21 | 191 | Observation | `Observation.code.coding` | 1153604005 | Body height for age z score | http://snomed.info/sct |
| 22 | 194 | Observation | `Observation.interpretation.coding` | OI000011 | Sangat Pendek | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 23 | 199 | Observation | `Observation.interpretation.coding` | 444000005 | Short stature for age | http://snomed.info/sct |
| 24 | 204 | Observation | `Observation.interpretation.coding` | 17489000 | Body height normal for age | http://snomed.info/sct |
| 25 | 207 | Observation | `Observation.interpretation.coding` | 83077003 | Tall for age | http://snomed.info/sct |
| 26 | 217 | Observation | `Observation.code.coding` | 1153596006 | Body mass index for age z-score | http://snomed.info/sct |
| 27 | 220 | Observation | `Observation.interpretation.coding` | OI000001 | Gizi Buruk | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 28 | 225 | Observation | `Observation.interpretation.coding` | 248325000 | Undernourished | http://snomed.info/sct |
| 29 | 230 | Observation | `Observation.interpretation.coding` | 248324001 | Well nourished | http://snomed.info/sct |
| 30 | 235 | Observation | `Observation.interpretation.coding` | 238131007 | Overweight | http://snomed.info/sct |
| 31 | 238 | Observation | `Observation.interpretation.coding` | 414915002 | Obese | http://snomed.info/sct |
| 32 | 248 | Observation | `Observation.code.coding` | SP000059 | Tren Pertumbuhan Anak | http://terminology.kemkes.go.id/sp |
| 33 | 249 | Observation | `Observation.valueCodeableConcept.coding` | 58236001 | Normal growth | http://snomed.info/sct |
| 34 | 250 | Observation | `Observation.valueCodeableConcept.coding` | 440301000124106 | Below expected growth rate | http://snomed.info/sct |
| 35 | 251 | Observation | `Observation.valueCodeableConcept.coding` | 704352005 | At increased risk of delayed growth | http://snomed.info/sct |
| 36 | 252 | Observation | `Observation.valueCodeableConcept.coding` | SP000057 | Perlambatan Pertumbuhan Linear | http://terminology.kemkes.go.id/sp |
| 37 | 253 | Observation | `Observation.valueCodeableConcept.coding` | SP000058 | Early Adiposity Rebound | http://terminology.kemkes.go.id/sp |
| 38 | 266 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | Ds | Perkembangan sesuai usia | http://terminology.kemkes.go.id/Codesystem/kpsp |
| 39 | 267 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | Dm | Perkembangan meragukan | http://terminology.kemkes.go.id/Codesystem/kpsp |
| 40 | 268 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | Dp | Perkembangan curiga adanya penyimpangan | http://terminology.kemkes.go.id/Codesystem/kpsp |
| 41 | 274 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 17621005 | Normal | http://snomed.info/sct |
| 42 | 275 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 410519009 | At risk | http://snomed.info/sct |
| 43 | 281 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 17621005 | Normal | http://snomed.info/sct |
| 44 | 282 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 410519009 | At risk | http://snomed.info/sct |
| 45 | 288 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 17621005 | Normal | http://snomed.info/sct |
| 46 | 289 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 410519009 | At risk | http://snomed.info/sct |
| 47 | 292 | Observation | `Observation.code.coding` | 284473002 | Mid upper arm circumference | http://snomed.info/sct |
| 48 | 302 | Observation | `Observation.interpretation.coding` | OI000001 | Gizi Buruk | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 49 | 303 | Observation | `Observation.interpretation.coding` | 248325000 | Undernourished | http://snomed.info/sct |
| 50 | 304 | Observation | `Observation.interpretation.coding` | 248324001 | Well nourished | http://snomed.info/sct |
| 51 | 307 | Observation | `Observation.code.coding` | 1153596006 | Body mass index for age z-score | http://snomed.info/sct |
| 52 | 310 | Observation | `Observation.interpretation.coding` | OI000001 | Gizi Buruk | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 53 | 315 | Observation | `Observation.interpretation.coding` | 248325000 | Undernourished | http://snomed.info/sct |
| 54 | 320 | Observation | `Observation.interpretation.coding` | 248324001 | Well nourished | http://snomed.info/sct |
| 55 | 325 | Observation | `Observation.interpretation.coding` | OI000004 | Risiko Gizi Lebih | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 56 | 330 | Observation | `Observation.interpretation.coding` | 238131007 | Overweight | http://snomed.info/sct |
| 57 | 333 | Observation | `Observation.interpretation.coding` | 414915002 | Obese | http://snomed.info/sct |
| 58 | 346 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 17621005 | Normal | http://snomed.info/sct |
| 59 | 347 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 64957009 | Uncertain | http://snomed.info/sct |
| 60 | 348 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 410519009 | At risk | http://snomed.info/sct |
| 61 | 354 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 17621005 | Normal | http://snomed.info/sct |
| 62 | 355 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 410519009 | At risk | http://snomed.info/sct |
| 63 | 361 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 17621005 | Normal | http://snomed.info/sct |
| 64 | 362 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 64957009 | Uncertain | http://snomed.info/sct |
| 65 | 363 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 410519009 | At risk | http://snomed.info/sct |
| 66 | 371 | Procedure | `Procedure.code.coding` | 441041000124100 | Counseling about nutrition | http://hl7.org/fhir/sid/icd-9-cm |
| 67 | 382 | Procedure | `Procedure.code.coding` | 410295000 | Growth/development education, guidance, and counseling | http://hl7.org/fhir/sid/icd-9-cm |
| 68 | 393 | Procedure | `Procedure.code.coding` | SP000060 | Intervensi Dini Masalah Pertumbuhan Anak | http://terminology.kemkes.go.id/sp |
| 69 | 405 | Observation | `Observation.code.coding` | SP000061 | Intervensi Dini Masalah Perkembangan Anak | http://terminology.kemkes.go.id/sp |
| 70 | 406 | Observation | `Observation.valueCodeableConcept` | 170218003 | Child examination: gross motor development | http://snomed.info/sct |
| 71 | 407 | Observation | `Observation.valueCodeableConcept` | 170219006 | Child examination: fine motor development | http://snomed.info/sct |
| 72 | 408 | Observation | `Observation.valueCodeableConcept` | SP000062 | Pemeriksaan Anak: Bicara dan Bahasa | http://terminology.kemkes.go.id/sp |
| 73 | 417 | Procedure | `Procedure.code.coding` | SP000063 | Intervensi Dini Masalah Perilaku & Emosi | http://terminology.kemkes.go.id/sp |
| 74 | 429 | Observation | `Observation.code.coding` | SP000064 | Tindakan Pengobatan Lain | http://terminology.kemkes.go.id/sp |
| 75 | 443 | ServiceRequest | `ServiceRequest.code` | 737492002 | Outpatient care management | http://snomed.info/sct |
| 76 | 449 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 77 | 450 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 78 | 451 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 79 | 452 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 80 | 453 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000011 | Monitoring rutin | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 81 | 454 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000012 | PPIA | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 82 | 455 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 83 | 456 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SR000001 | Penanganan / perawatan lanjut pasien (medik) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 84 | 457 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SR000002 | Sarana dan prasarana (Ruang Perawatan Biasa) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 85 | 458 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SR000003 | Sarana dan prasarana (Ruang intensive (ICU, CVCU/ICCU, NICU, PICU, HCU)) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 86 | 459 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SR000004 | Sarana dan prasarana (Ruang Isolasi) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 87 | 460 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SR000005 | Dokter spesialis / sub spesialis tidak tersedia | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 88 | 461 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SR000006 | Tindakan Khusus | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 89 | 462 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SR000007 | Rujuk balik | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 90 | 463 | ServiceRequest | `ServiceRequest.reasonCode.coding` | 171128005 | Venereal disease screening | http://snomed.info/sct |
| 91 | 464 | ServiceRequest | `ServiceRequest.reasonCode.coding` | A15.0 | Tuberculosis of lung, confirmed by sputum microscopy with or without culture | http://hl7.org/fhir/sid/icd-10 |
| 92 | 467 | Observation | `Observation.code.coding` | OC000034 | Surat Pengantar Rujukan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 47 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 24 |
| http://terminology.kemkes.go.id/sp | 10 |
| http://loinc.org | 5 |
| http://terminology.kemkes.go.id/Codesystem/kpsp | 3 |
| http://hl7.org/fhir/sid/icd-9-cm | 2 |
| http://hl7.org/fhir/sid/icd-10 | 1 |
| **Total** | **92** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
