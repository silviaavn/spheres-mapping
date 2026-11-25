# Output Form: KuApps BidanKu - Anak Usia Sekolah dan Remaja

Sumber: `mapping/phdt-data-dictionary-kuapps-bidanku-usekre.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-kuapps-bidanku-usekre.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 31 |
| Code (`jumlah code` = 1) | 83 |
| Code unik (code + CodeSystem) | 75 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 2 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–13 | Observation | 29463-7 | Body weight | _Berat Badan_ → `Observation.valueQuantity.value` (5, tanpa BQ) |
| 2 | 14–25 | Observation | 8302-2 | Body height | _Tinggi Badan_ → `Observation.valueQuantity.value` (17, tanpa BQ) |
| 3 | 27–56 | Observation | 39156-5 | Body mass index (BMI) [Ratio] | _IMT_ → `Observation.valueRange.high.value` (32, tanpa BQ) |
| 4 | 57–68 | Observation | vital-signs | Abdominal circumference | _Lingkar Perut_ → `Observation.valueQuantity.value` (60, tanpa BQ) |
| 5 | 69–80 | Observation | 8480-6 | Systolic blood pressure | _Tekanan Darah Sistole_ → `Observation.valueQuantity.value` (72, tanpa BQ) |
| 6 | 81–92 | Observation | 8462-4 | Diastolic blood pressure | _Tekanan Darah Diastole_ → `Observation.valueQuantity.value` (84, tanpa BQ) |
| 7 | 93–112 | Observation | 268607006 | Hypertension risk level | _Interpretasi tekanan darah_ → `Observation.valueRatio.numerator.value` (103, tanpa BQ) |
| 8 | 113–124 | Observation | SP000924 | Remaja memiliki Tablet Tambah Darah | _Apakah remaja memiliki Tablet Tambah Darah?_ → `Observation.valueBoolean` (116, tanpa BQ) |
| 9 | 125–136 | MedicationStatement | – | – | _Apakah mengonsumsi TTD minggu ini/ dalam 7 hari terakhir?_ → `MedicationStatement.category.coding` (125, tanpa BQ)<br>_Berapa jumlah TTD yang dikonsumsi dalam 1 bulan terakhir?_ → `MedicationStatement.dosage.doseAndRate.doseQuantity` (135, tanpa BQ) |
| 10 | 137–151 | Condition | 160357008 | Family history: Hypertension | _Riwayat keluarga_ → `Condition.clinicalStatus.coding` (137, tanpa BQ) |
| 11 | 152–165 | Condition | 161501007 | History of hypertension | _Riwayat penyakit diri sendiri_ → `Condition.clinicalStatus.coding` (152, tanpa BQ) |
| 12 | 166–183 | Condition | 84757009 | Epilepsy | _Penyakit penyerta_ → `Condition.clinicalStatus.coding` (166, tanpa BQ) |
| 13 | 184–194 | Observation | 1269496002 | Complaint | _Keluhan saat ini_ → `Observation.valueString` (187, tanpa BQ) |
| 14 | 195–208 | Observation | 72166-2 | Tobacco smoking status | _Perilaku Merokok_ → `Observation.valueCodeableConcept.coding` (198, tanpa BQ) |
| 15 | 209–220 | Observation | 63892-4 | Have you ever been pregnant [PhenX] | _Apakah pasien pernah hamil?_ → `Observation.valueBoolean` (212, tanpa BQ) |
| 16 | 221–232 | Observation | 386216000 | Human parturition, function | _Apakah pasien pernah melahirkan?_ → `Observation.valueBoolean` (224, tanpa BQ) |
| 17 | 233–244 | Observation | 1144561006 | Adequate sanitation | _Apakah memiliki jamban di rumah?_ → `Observation.valueBoolean` (236, tanpa BQ) |
| 18 | 245–256 | Observation | 1162942008 | Access to potable water | _Apakah memiliki akses untuk air bersih_ → `Observation.valueBoolean` (248, tanpa BQ) |
| 19 | 258–271 | Observation | 422256009 | Counts fingers - distance vision | _Mata Kanan_ → `Observation.valueCodeableConcept.coding` (262, tanpa BQ) |
| 20 | 272–285 | Observation | 422256009 | Counts fingers - distance vision | _Mata Kiri_ → `Observation.valueCodeableConcept.coding` (276, tanpa BQ) |
| 21 | 286–299 | Observation | 247301006 | Finding of ability to hear whisper | _Telinga Kanan_ → `Observation.valueCodeableConcept.coding` (290, tanpa BQ) |
| 22 | 300–313 | Observation | 247301006 | Finding of ability to hear whisper | _Telinga Kiri_ → `Observation.valueCodeableConcept.coding` (304, tanpa BQ) |
| 23 | 314–328 | Observation | 718-7 | Hemoglobin [Mass/volume] in Blood | _Kadar Hemoglobin_ → `Observation.valueQuantity.value` (317, tanpa BQ)<br>_Interpretasi Anemia_ → `Observation.interpretation.coding` (319, tanpa BQ) |
| 24 | 329–357 | MedicationRequest | 93015491 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | _Apakah diberikan TTD?_ → `MedicationRequest.contained.resourceType` (329, tanpa BQ) |
| 25 | 358–384 | MedicationDispense | 93015491 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | _Berapa jumlah TTD yang diberikan ?_ → `MedicationDispense.quantity.value` (381, tanpa BQ) |
| 26 | 385–396 | Procedure | – | – | _Apakah dilakukan skrining gula darah?_ → `Procedure.category.coding` (385, tanpa BQ) |
| 27 | 397–424 | Observation | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | _Hasil Gula Darah Sewaktu_ → `Observation.valueQuantity.value` (400, tanpa BQ)<br>_Interpretasi Gula Darah Sewaktu_ → `Observation.interpretation.coding` (409, tanpa BQ) |
| 28 | 425–450 | QuestionnaireResponse | https://fhir.kemkes.go.id/sp/Questionnaire/Q00016 | – | _Batuk Terus Menerus_ → `QuestionnaireResponse.item.text` (436, tanpa BQ)<br>_Demam lebih dari ≥ 2 minggu_ → `QuestionnaireResponse.item.linkId` (439, tanpa BQ)<br>_BB tidak naik atau turun dalam 2 bulan berturut-turut_ → `QuestionnaireResponse.item.linkId` (443, tanpa BQ)<br>_Kontak erat dengan Pasien TBC_ → `QuestionnaireResponse.item.linkId` (447, tanpa BQ) |
| 29 | 451–463 | Observation | 171126009 | Tuberculosis screening | _Interpretasi hasil skrining TBC_ → `Observation.valueQuantity.value` (451, tanpa BQ) |
| 30 | 464–505 | QuestionnaireResponse | https://fhir.kemkes.go.id/sp/Questionnaire/Q00018 | – | _Memiliki masalah di dalam rumah (Home)_ → `QuestionnaireResponse.item.linkId` (474, tanpa BQ)<br>_Memiliki Masalah dengan Pendidikan atau Pekerjaan (Education/Employment)_ → `QuestionnaireResponse.item.linkId` (478, tanpa BQ)<br>_Memiliki Masalah Dengan Pola Makan (Eating)_ → `QuestionnaireResponse.item.linkId` (482, tanpa BQ)<br>_Memiliki Masalah dengan Aktivitas (Activity)_ → `QuestionnaireResponse.item.linkId` (486, tanpa BQ)<br>_Memiliki masalah dengan obat-obatan (Drugs)_ → `QuestionnaireResponse.item.linkId` (490, tanpa BQ)<br>_Memiliki masalah dengan kesehatan seksual (Sexuality)_ → `QuestionnaireResponse.item.linkId` (494, tanpa BQ)<br>_Memiliki Masalah dengan Keamanan (Self Image)_ → `QuestionnaireResponse.item.linkId` (498, tanpa BQ)<br>_Memiliki keinginan bunuh diri/depresi (Safety)_ → `QuestionnaireResponse.item.linkId` (502, tanpa BQ) |
| 31 | 507–524 | Procedure | 410314003 | Health promotion education, guidance, and counseling | _Apakah dilakukan konseling_ → `Procedure.category.coding` (507, tanpa BQ)<br>_Sebutkan topik konseling yang dilakukan_ → `Procedure.code.coding.code` (511, tanpa BQ)<br>_Jika dijawab lainnya tambahkan mapping berikut_ → `Procedure.code.text` (517, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 21 |
| Condition | 3 |
| Procedure | 2 |
| QuestionnaireResponse | 2 |
| MedicationStatement | 1 |
| MedicationRequest | 1 |
| MedicationDispense | 1 |
| **Total** | **31** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 4 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 2 | 16 | Observation | `Observation.code.coding` | 8302-2 | Body height | http://loinc.org |
| 3 | 29 | Observation | `Observation.code.coding` | 39156-5 | Body mass index (BMI) [Ratio] | http://loinc.org |
| 4 | 30 | Observation | `Observation.interpretation.coding` | 717933005 | Severe thinness in adulthood | http://snomed.info/sct |
| 5 | 33 | Observation | `Observation.interpretation.coding` | 248342006 | Underweight | http://snomed.info/sct |
| 6 | 36 | Observation | `Observation.interpretation.coding` | 43664005 | Normal weight | http://snomed.info/sct |
| 7 | 41 | Observation | `Observation.interpretation.coding` | 238131007 | Overweight | http://snomed.info/sct |
| 8 | 46 | Observation | `Observation.interpretation.coding` | 414915002 | Obese | http://snomed.info/sct |
| 9 | 59 | Observation | `Observation.code.coding` | vital-signs | Abdominal circumference | http://snomed.info/sct |
| 10 | 71 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 11 | 83 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://snomed.info/sct |
| 12 | 95 | Observation | `Observation.code.coding` | 268607006 | Hypertension risk level | http://snomed.info/sct |
| 13 | 107 | Observation | `Observation.interpretation.coding` | OI000040 | Tekanan Darah Optimal | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 14 | 109 | Observation | `Observation.interpretation.coding` | 2004005 | Normal blood pressure | http://snomed.info/sct |
| 15 | 111 | Observation | `Observation.interpretation.coding` | OI000041 | Tekanan Darah Normal Tinggi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 16 | 115 | Observation | `Observation.code.coding` | SP000924 | Remaja memiliki Tablet Tambah Darah | http://terminology.kemkes.go.id/sp |
| 17 | 139 | Condition | `Condition.code.coding` | 160357008 | Family history: Hypertension | http://snomed.info/sct |
| 18 | 140 | Condition | `Condition.code.coding` | 160303001 | Family history of diabetes mellitus | http://snomed.info/sct |
| 19 | 141 | Condition | `Condition.code.coding` | 275104002 | Family history of stroke | http://snomed.info/sct |
| 20 | 142 | Condition | `Condition.code.coding` | 429959009 | Family history of heart failure | http://snomed.info/sct |
| 21 | 143 | Condition | `Condition.code.coding` | 160377001 | Family history: Asthma | http://snomed.info/sct |
| 22 | 144 | Condition | `Condition.code.coding` | 275937001 | Family history of malignant neoplasm (situation) | http://snomed.info/sct |
| 23 | 145 | Condition | `Condition.code.coding` | 160314003 | Family history: Hypercholesterolemia | http://snomed.info/sct |
| 24 | 146 | Condition | `Condition.code.coding` | 160324006 | Family history of mental disorder | http://snomed.info/sct |
| 25 | 147 | Condition | `Condition.code.coding` | 160266009 | No family history of clinical finding | http://snomed.info/sct |
| 26 | 154 | Condition | `Condition.code.coding` | 161501007 | History of hypertension | http://snomed.info/sct |
| 27 | 155 | Condition | `Condition.code.coding` | 161445009 | History of diabetes mellitus | http://snomed.info/sct |
| 28 | 156 | Condition | `Condition.code.coding` | 275526006 | History of cerebrovascular accident | http://snomed.info/sct |
| 29 | 157 | Condition | `Condition.code.coding` | 275544003 | History of heart disorder | http://snomed.info/sct |
| 30 | 158 | Condition | `Condition.code.coding` | 161527007 | History of asthma | http://snomed.info/sct |
| 31 | 159 | Condition | `Condition.code.coding` | 266987004 | History of malignant neoplasm | http://snomed.info/sct |
| 32 | 160 | Condition | `Condition.code.coding` | 414416008 | History of hypercholesterolemia | http://snomed.info/sct |
| 33 | 161 | Condition | `Condition.code.coding` | 443508001 | No history of clinical finding in subject | http://snomed.info/sct |
| 34 | 168 | Condition | `Condition.code.coding` | 84757009 | Epilepsy | http://snomed.info/sct |
| 35 | 169 | Condition | `Condition.code.coding` | 13213009 | Congenital heart disease | http://snomed.info/sct |
| 36 | 170 | Condition | `Condition.code.coding` | 90708001 | Kidney disease | http://snomed.info/sct |
| 37 | 171 | Condition | `Condition.code.coding` | 56265001 | Heart disease | http://snomed.info/sct |
| 38 | 172 | Condition | `Condition.code.coding` | 195967001 | Asthma | http://snomed.info/sct |
| 39 | 173 | Condition | `Condition.code.coding` | 1240414004 | Malignant neoplasm | http://snomed.info/sct |
| 40 | 174 | Condition | `Condition.code.coding` | 73211009 | Diabetes mellitus | http://snomed.info/sct |
| 41 | 175 | Condition | `Condition.code.coding` | 118940003 | Disorder of nervous system | http://snomed.info/sct |
| 42 | 176 | Condition | `Condition.code.coding` | 444896005 | Growth retardation | http://snomed.info/sct |
| 43 | 177 | Condition | `Condition.code.coding` | 5294002 | Developmental disorder | http://snomed.info/sct |
| 44 | 178 | Condition | `Condition.code.coding` | 128188000 | Cerebral palsy | http://snomed.info/sct |
| 45 | 179 | Condition | `Condition.code.coding` | 443508001 | No history of clinical finding in subject | http://snomed.info/sct |
| 46 | 186 | Observation | `Observation.code.coding` | 1269496002 | Complaint | http://snomed.info/sct |
| 47 | 197 | Observation | `Observation.code.coding` | 72166-2 | Tobacco smoking status | http://loinc.org |
| 48 | 198 | Observation | `Observation.valueCodeableConcept.coding` | 77176002 | Smoker | http://snomed.info/sct |
| 49 | 199 | Observation | `Observation.valueCodeableConcept.coding` | 43381005 | Passive smoker | http://snomed.info/sct |
| 50 | 200 | Observation | `Observation.valueCodeableConcept.coding` | 8517006 | Ex-smoker | http://snomed.info/sct |
| 51 | 201 | Observation | `Observation.valueCodeableConcept.coding` | 8392000 | Non-smoker | http://snomed.info/sct |
| 52 | 211 | Observation | `Observation.code.coding` | 63892-4 | Have you ever been pregnant [PhenX] | http://loinc.org |
| 53 | 223 | Observation | `Observation.code.coding` | 386216000 | Human parturition, function | http://snomed.info/sct |
| 54 | 235 | Observation | `Observation.code.coding` | 1144561006 | Adequate sanitation | http://snomed.info/sct |
| 55 | 247 | Observation | `Observation.code.coding` | 1162942008 | Access to potable water | http://snomed.info/sct |
| 56 | 260 | Observation | `Observation.code.coding` | 422256009 | Counts fingers - distance vision | http://snomed.info/sct |
| 57 | 262 | Observation | `Observation.valueCodeableConcept.coding` | 164727006 | Visual testing normal | http://snomed.info/sct |
| 58 | 263 | Observation | `Observation.valueCodeableConcept.coding` | 397540003 | Visual impairment | http://snomed.info/sct |
| 59 | 274 | Observation | `Observation.code.coding` | 422256009 | Counts fingers - distance vision | http://snomed.info/sct |
| 60 | 276 | Observation | `Observation.valueCodeableConcept.coding` | 164727006 | Visual testing normal | http://snomed.info/sct |
| 61 | 277 | Observation | `Observation.valueCodeableConcept.coding` | 397540003 | Visual impairment | http://snomed.info/sct |
| 62 | 288 | Observation | `Observation.code.coding` | 247301006 | Finding of ability to hear whisper | http://snomed.info/sct |
| 63 | 290 | Observation | `Observation.valueCodeableConcept.coding` | 275727004 | Hearing test normal | http://snomed.info/sct |
| 64 | 291 | Observation | `Observation.valueCodeableConcept.coding` | 300221005 | Hearing for whisper impaired | http://snomed.info/sct |
| 65 | 302 | Observation | `Observation.code.coding` | 247301006 | Finding of ability to hear whisper | http://snomed.info/sct |
| 66 | 304 | Observation | `Observation.valueCodeableConcept.coding` | 275727004 | Hearing test normal | http://snomed.info/sct |
| 67 | 305 | Observation | `Observation.valueCodeableConcept.coding` | 300221005 | Hearing for whisper impaired | http://snomed.info/sct |
| 68 | 316 | Observation | `Observation.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 69 | 319 | Observation | `Observation.interpretation.coding` | 860635002 | No anemia present | http://snomed.info/sct |
| 70 | 320 | Observation | `Observation.interpretation.coding` | OI000032 | Anemia ringan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 71 | 321 | Observation | `Observation.interpretation.coding` | OI000033 | Anemia sedang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 72 | 322 | Observation | `Observation.interpretation.coding` | OI000034 | Anemia berat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 73 | 332 | MedicationRequest | `MedicationRequest.contained.code.coding` | 93015491 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | http://sys-ids.kemkes.go.id/kfa |
| 74 | 361 | MedicationDispense | `MedicationDispense.contained.code.coding` | 93015491 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | http://sys-ids.kemkes.go.id/kfa |
| 75 | 399 | Observation | `Observation.code.coding` | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 76 | 409 | Observation | `Observation.interpretation.coding` | 302866003 | Hypoglycemia | http://snomed.info/sct |
| 77 | 412 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 78 | 417 | Observation | `Observation.interpretation.coding` | 714628002 | Prediabetes | http://snomed.info/sct |
| 79 | 422 | Observation | `Observation.interpretation.coding` | 80394007 | Hyperglycemia | http://snomed.info/sct |
| 80 | 452 | Observation | `Observation.interpretation.coding` | 772170009 | Tuberculosis suspected | http://snomed.info/sct |
| 81 | 453 | Observation | `Observation.interpretation.coding` | SP000789 | Bukan terduga TBC | http://terminology.kemkes.go.id/sp |
| 82 | 456 | Observation | `Observation.code.coding` | 171126009 | Tuberculosis screening | http://snomed.info/sct |
| 83 | 508 | Procedure | `Procedure.code.coding` | 410314003 | Health promotion education, guidance, and counseling | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 65 |
| http://loinc.org | 8 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 5 |
| http://terminology.kemkes.go.id/sp | 2 |
| http://sys-ids.kemkes.go.id/kfa | 2 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 1 |
| **Total** | **83** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 506 | – | Tanggal kunjungan | – | `` |
