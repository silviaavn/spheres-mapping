# Output Form: Kobo - SDIDTK

Sumber: `mapping/phdt-data-dictionary-kobo-sdidtk.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-kobo-sdidtk.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 35 |
| Code (`jumlah code` = 1) | 68 |
| Code unik (code + CodeSystem) | 56 |
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
| 18 | 261–268 | QuestionnaireResponse | – | – | _Kuisioner Pra-Skrining Perkembangan (KPSP)_ → `QuestionnaireResponse.questionnaire` (261, tanpa BQ) |
| 19 | 269–275 | QuestionnaireResponse | – | – | _Tes Daya Dengar (TDD) Anak_ → `QuestionnaireResponse.questionnaire` (269, tanpa BQ) |
| 20 | 276–282 | QuestionnaireResponse | – | – | _Tes Daya Lihat_ → `QuestionnaireResponse.questionnaire` (276, tanpa BQ) |
| 21 | 283–289 | QuestionnaireResponse | – | – | _Pemeriksaan Pupil Putih_ → `QuestionnaireResponse.questionnaire` (283, tanpa BQ) |
| 22 | 290–304 | Observation | 284473002 | Mid upper arm circumference | _Lingkar Lengan Atas (LILA)_ → `Observation.valueQuantity.value` (293, tanpa BQ)<br>_Klasifikasi LILA_ → `Observation.interpretation.coding` (302, tanpa BQ) |
| 23 | 305–340 | Observation | 1153596006 | Body mass index for age z-score | _IMT/U (0-59 bulan)_ → `Observation.valueRange.high.value` (308, tanpa BQ) |
| 24 | 341–348 | QuestionnaireResponse | – | – | _Kuisioner Masalah Perilaku Emosional (KMPE)_ → `QuestionnaireResponse.questionnaire` (341, tanpa BQ) |
| 25 | 349–355 | QuestionnaireResponse | – | – | _Modified Checklist for Autism in Toddler (M-CHAT)_ → `QuestionnaireResponse.questionnaire` (349, tanpa BQ) |
| 26 | 356–363 | QuestionnaireResponse | – | – | _Gangguan Pemusatan Perhatian/Hiperaktivitas (GPPH)_ → `QuestionnaireResponse.questionnaire` (356, tanpa BQ) |
| 27 | 364–369 | QuestionnaireResponse | – | – | _Kesimpulan_ → `QuestionnaireResponse.questionnaire` (364, tanpa BQ) |
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
| 9 | 153 | Observation | `Observation.code.coding` | 1153600001 | Weight for height z-score | http://snomed.info/sct |
| 10 | 154 | Observation | `Observation.code.coding` | 1153598007 | Weight for length z score | http://snomed.info/sct |
| 11 | 190 | Observation | `Observation.code.coding` | 1153590000 | Length for age z-score | http://snomed.info/sct |
| 12 | 191 | Observation | `Observation.code.coding` | 1153604005 | Body height for age z score | http://snomed.info/sct |
| 13 | 217 | Observation | `Observation.code.coding` | 1153596006 | Body mass index for age z-score | http://snomed.info/sct |
| 14 | 248 | Observation | `Observation.code.coding` | SP000059 | Tren Pertumbuhan Anak | http://terminology.kemkes.go.id/sp |
| 15 | 249 | Observation | `Observation.valueCodeableConcept.coding` | 58236001 | Normal growth | http://snomed.info/sct |
| 16 | 250 | Observation | `Observation.valueCodeableConcept.coding` | 440301000124106 | Below expected growth rate | http://snomed.info/sct |
| 17 | 251 | Observation | `Observation.valueCodeableConcept.coding` | 704352005 | At increased risk of delayed growth | http://snomed.info/sct |
| 18 | 252 | Observation | `Observation.valueCodeableConcept.coding` | SP000057 | Perlambatan Pertumbuhan Linear | http://terminology.kemkes.go.id/sp |
| 19 | 253 | Observation | `Observation.valueCodeableConcept.coding` | SP000058 | Early Adiposity Rebound | http://terminology.kemkes.go.id/sp |
| 20 | 266 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | Ds | Perkembangan sesuai usia | http://terminology.kemkes.go.id/Codesystem/kpsp |
| 21 | 267 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | Dm | Perkembangan meragukan | http://terminology.kemkes.go.id/Codesystem/kpsp |
| 22 | 268 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | Dp | Perkembangan curiga adanya penyimpangan | http://terminology.kemkes.go.id/Codesystem/kpsp |
| 23 | 274 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 17621005 | Normal | http://snomed.info/sct |
| 24 | 275 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 410519009 | At risk | http://snomed.info/sct |
| 25 | 281 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 17621005 | Normal | http://snomed.info/sct |
| 26 | 282 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 410519009 | At risk | http://snomed.info/sct |
| 27 | 288 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 17621005 | Normal | http://snomed.info/sct |
| 28 | 289 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 410519009 | At risk | http://snomed.info/sct |
| 29 | 292 | Observation | `Observation.code.coding` | 284473002 | Mid upper arm circumference | http://snomed.info/sct |
| 30 | 302 | Observation | `Observation.interpretation.coding` | OI000001 | Gizi Buruk | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 31 | 303 | Observation | `Observation.interpretation.coding` | 248325000 | Undernourished | http://snomed.info/sct |
| 32 | 304 | Observation | `Observation.interpretation.coding` | 248324001 | Well nourished | http://snomed.info/sct |
| 33 | 307 | Observation | `Observation.code.coding` | 1153596006 | Body mass index for age z-score | http://snomed.info/sct |
| 34 | 346 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 17621005 | Normal | http://snomed.info/sct |
| 35 | 347 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 64957009 | Uncertain | http://snomed.info/sct |
| 36 | 348 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 410519009 | At risk | http://snomed.info/sct |
| 37 | 354 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 17621005 | Normal | http://snomed.info/sct |
| 38 | 355 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 410519009 | At risk | http://snomed.info/sct |
| 39 | 361 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 17621005 | Normal | http://snomed.info/sct |
| 40 | 362 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 64957009 | Uncertain | http://snomed.info/sct |
| 41 | 363 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 410519009 | At risk | http://snomed.info/sct |
| 42 | 371 | Procedure | `Procedure.code.coding` | 441041000124100 | Counseling about nutrition | http://hl7.org/fhir/sid/icd-9-cm |
| 43 | 382 | Procedure | `Procedure.code.coding` | 410295000 | Growth/development education, guidance, and counseling | http://hl7.org/fhir/sid/icd-9-cm |
| 44 | 393 | Procedure | `Procedure.code.coding` | SP000060 | Intervensi Dini Masalah Pertumbuhan Anak | http://terminology.kemkes.go.id/sp |
| 45 | 405 | Observation | `Observation.code.coding` | SP000061 | Intervensi Dini Masalah Perkembangan Anak | http://terminology.kemkes.go.id/sp |
| 46 | 406 | Observation | `Observation.valueCodeableConcept` | 170218003 | Child examination: gross motor development | http://snomed.info/sct |
| 47 | 407 | Observation | `Observation.valueCodeableConcept` | 170219006 | Child examination: fine motor development | http://snomed.info/sct |
| 48 | 408 | Observation | `Observation.valueCodeableConcept` | SP000062 | Pemeriksaan Anak: Bicara dan Bahasa | http://terminology.kemkes.go.id/sp |
| 49 | 417 | Procedure | `Procedure.code.coding` | SP000063 | Intervensi Dini Masalah Perilaku & Emosi | http://terminology.kemkes.go.id/sp |
| 50 | 429 | Observation | `Observation.code.coding` | SP000064 | Tindakan Pengobatan Lain | http://terminology.kemkes.go.id/sp |
| 51 | 443 | ServiceRequest | `ServiceRequest.code` | 737492002 | Outpatient care management | http://snomed.info/sct |
| 52 | 449 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 53 | 450 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 54 | 451 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 55 | 452 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 56 | 453 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000011 | Monitoring rutin | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 57 | 454 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000012 | PPIA | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 58 | 455 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 59 | 456 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SR000001 | Penanganan / perawatan lanjut pasien (medik) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 60 | 457 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SR000002 | Sarana dan prasarana (Ruang Perawatan Biasa) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 61 | 458 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SR000003 | Sarana dan prasarana (Ruang intensive (ICU, CVCU/ICCU, NICU, PICU, HCU)) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 62 | 459 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SR000004 | Sarana dan prasarana (Ruang Isolasi) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 63 | 460 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SR000005 | Dokter spesialis / sub spesialis tidak tersedia | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 64 | 461 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SR000006 | Tindakan Khusus | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 65 | 462 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SR000007 | Rujuk balik | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 66 | 463 | ServiceRequest | `ServiceRequest.reasonCode.coding` | 171128005 | Venereal disease screening | http://snomed.info/sct |
| 67 | 464 | ServiceRequest | `ServiceRequest.reasonCode.coding` | A15.0 | Tuberculosis of lung, confirmed by sputum microscopy with or without culture | http://hl7.org/fhir/sid/icd-10 |
| 68 | 467 | Observation | `Observation.code.coding` | OC000034 | Surat Pengantar Rujukan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 31 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 16 |
| http://terminology.kemkes.go.id/sp | 10 |
| http://loinc.org | 5 |
| http://terminology.kemkes.go.id/Codesystem/kpsp | 3 |
| http://hl7.org/fhir/sid/icd-9-cm | 2 |
| http://hl7.org/fhir/sid/icd-10 | 1 |
| **Total** | **68** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
