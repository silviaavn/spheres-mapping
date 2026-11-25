# Output Form: KuApps BidanKu - Lansia

Sumber: `mapping/phdt-data-dictionary-kuapps-bidanku-lansia.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-kuapps-bidanku-lansia.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 29 |
| Code (`jumlah code` = 1) | 121 |
| Code unik (code + CodeSystem) | 100 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 11 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 4–15 | Observation | 29463-7 | Body weight | _Berat Badan_ → `Observation.valueQuantity.value` (7, tanpa BQ) |
| 2 | 16–27 | Observation | 8302-2 | Body height | _Tinggi Badan_ → `Observation.valueQuantity.value` (19, tanpa BQ) |
| 3 | 29–58 | Observation | 39156-5 | Body mass index (BMI) [Ratio] | _IMT_ → `Observation.valueRange.high.value` (34, tanpa BQ) |
| 4 | 59–70 | Observation | 396552003 | Abdominal circumference | _Lingkar Perut_ → `Observation.valueQuantity.value` (62, tanpa BQ) |
| 5 | 71–81 | Observation | 284473002 | Mid upper arm circumference | _LiLA_ → `Observation.valueQuantity.value` (74, tanpa BQ) |
| 6 | 82–93 | Observation | 8480-6 | Systolic blood pressure | _Tekanan Darah Sistole_ → `Observation.valueQuantity.value` (85, tanpa BQ) |
| 7 | 94–105 | Observation | 8462-4 | Diastolic blood pressure | _Tekanan Darah Diastole_ → `Observation.valueQuantity.value` (97, tanpa BQ) |
| 8 | 106–125 | Observation | 268607006 | Hypertension risk level | _Interpretasi tekanan darah_ → `Observation.valueRatio.numerator.value` (116, tanpa BQ) |
| 9 | 126–137 | Observation | 8310-5 | Body temperature | _Suhu_ → `Observation.valueQuantity.value` (129, tanpa BQ) |
| 10 | 138–151 | Condition | 160357008 | Family history: Hypertension | _Riwayat Keluarga_ → `Condition.clinicalStatus.coding` (138, tanpa BQ) |
| 11 | 152–164 | Condition | 161501007 | History of hypertension | _Riwayat diri Sendiri_ → `Condition.clinicalStatus.coding` (152, tanpa BQ) |
| 12 | 165–177 | Condition | 161501007 | History of hypertension | _Riwayat Penyakit Tidak Menular_ → `Condition.clinicalStatus.coding` (165, tanpa BQ) |
| 13 | 178–199 | Observation | SP000658 | Perilaku Berisiko Diri Sendiri | _Perilaku Berisiko Diri Sendiri_ → `Observation.component.valueBoolean` (182, tanpa BQ) |
| 14 | 200–222 | Observation | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | _Gula Darah Sewaktu_ → `Observation.valueQuantity.value` (203, tanpa BQ)<br>_Interpretasi Gula Darah Sewaktu_ → `Observation.interpretation.coding` (212, tanpa BQ) |
| 15 | 223–248 | QuestionnaireResponse | https://fhir.kemkes.go.id/sp/Questionnaire/Q00016 | – | _Batuk terus menerus_ → `QuestionnaireResponse.item.linkId` (233, tanpa BQ)<br>_Demam lebih dari ≥ 2 minggu_ → `QuestionnaireResponse.item.linkId` (237, tanpa BQ)<br>_BB tidak naik atau turun dalam 2 bulan berturut-turut_ → `QuestionnaireResponse.item.linkId` (241, tanpa BQ)<br>_Kontak erat dengan Pasien TBC_ → `QuestionnaireResponse.item.linkId` (245, tanpa BQ) |
| 16 | 249–260 | Observation | 3457005 | Patient referral | _Rujuk_ → `Observation.valueBoolean` (252, tanpa BQ) |
| 17 | 262–275 | Observation | 422256009 | Counts fingers - distance vision | _Mata Kanan_ → `Observation.valueCodeableConcept.coding` (266, tanpa BQ) |
| 18 | 276–289 | Observation | 422256009 | Counts fingers - distance vision | _Mata Kiri_ → `Observation.valueCodeableConcept.coding` (280, tanpa BQ) |
| 19 | 290–303 | Observation | 247301006 | Finding of ability to hear whisper | _Telinga Kanan_ → `Observation.valueCodeableConcept.coding` (294, tanpa BQ) |
| 20 | 304–317 | Observation | 247301006 | Finding of ability to hear whisper | _Telinga Kiri_ → `Observation.valueCodeableConcept.coding` (308, tanpa BQ) |
| 21 | 318–357 | QuestionnaireResponse | https://fhir.kemkes.go.id/sp/Questionnaire/Q00015 | – | _Jenis Kelamin_ → `QuestionnaireResponse.item.linkId` (328, tanpa BQ)<br>_Usia_ → `QuestionnaireResponse.item.text` (333, tanpa BQ)<br>_Merokok_ → `QuestionnaireResponse.item.linkId` (337, tanpa BQ)<br>_Apakah Anda Pernah merasa napas pendek ketika berjalan lebih cepat pada jalan yang datar atau pada jalan yang sedikit menanjak?_ → `QuestionnaireResponse.item.linkId` (342, tanpa BQ)<br>_Apakah anda mempunyai dahak yang berasal dari paru atau kesulitan mengeluarkan dahak saat Anda sedang tidak menderita flu?_ → `QuestionnaireResponse.item.linkId` (346, tanpa BQ)<br>_Apakah anda Biasanya batuk saat Anda sedang tidak menderita flu?_ → `QuestionnaireResponse.item.linkId` (350, tanpa BQ)<br>_Apakah Dokter atau tenaga kesehatan lainnya pernah meminta Anda untuk melakukan pemeriksaan spirometri atau peakflow meter (meniup ke dalam suatu alat)?_ → `QuestionnaireResponse.item.linkId` (354, tanpa BQ) |
| 22 | 358–371 | Observation | SP000111 | Hasil Kuesioner PUMA | _Skor PUMA_ → `Observation.status` (358, tanpa BQ) |
| 23 | 372–414 | Observation | 304492001 | Activities of daily living assessment | _Mengendalikan rangsang Buang Air Besar (BAB)_ → `Observation.component.code.coding` (375, tanpa BQ)<br>_Mengendalikan rangsang Buang Air Kecil (BAK)_ → `Observation.component.code.coding` (379, tanpa BQ)<br>_Membersihkan diri (mencuci wajah, menyikat Rambut, mencukur kumis, sikat gigi)_ → `Observation.component.code.coding` (383, tanpa BQ)<br>_Penggunaan WC (keluar masuk WC, melepas/memakai celana, cebok, menyiram)_ → `Observation.component.code.coding` (386, tanpa BQ)<br>_Makan minum (jika makan harus berupa potongan, dianggap dibantu)_ → `Observation.component.code.coding` (390, tanpa BQ)<br>_Bergerak dari kursi roda ke tempat tidur dan sebaliknya (termasuk duduk di tempat tidur)_ → `Observation.component.code.coding` (394, tanpa BQ)<br>_Berjalan di tempat rata (atau jika tidak bisa berjalan, menjalankan kursi roda)_ → `Observation.component.code.coding` (399, tanpa BQ)<br>_Berpakaian (termasuk memasang tali sepatu, Mengencangkan sabuk)_ → `Observation.component.code.coding` (404, tanpa BQ)<br>_Naik turun tangga_ → `Observation.component.code.coding` (408, tanpa BQ)<br>_Mandi_ → `Observation.component.code.coding` (412, tanpa BQ) |
| 24 | 415–440 | Observation | 96762-0 | Barthel index panel | _Tingkat Ketergantungan_ → `Observation.valueQuantity.value` (419, tanpa BQ) |
| 25 | 441–505 | QuestionnaireResponse | https://fhir.kemkes.go.id/Questionnaire/Q0042 | – | _Penurunan Kognitif_ → `QuestionnaireResponse.item.linkId` (450, tanpa BQ)<br>_Orientasi waktu dan tempat_ → `QuestionnaireResponse.item.item.text` (453, tanpa BQ)<br>_Mengulang ketiga kata_ → `QuestionnaireResponse.item.item.text` (457, tanpa BQ)<br>_Keterbatasan Mobilisasi_ → `QuestionnaireResponse.item.linkId` (460, tanpa BQ)<br>_Tes Berdiri dari Kursi_ → `QuestionnaireResponse.item.item.text` (463, tanpa BQ)<br>_Malnutrisi_ → `QuestionnaireResponse.item.linkId` (466, tanpa BQ)<br>_BB berkurang >3kg dalam 3 bulan terakhir atau pakaian jadi lebih longgar_ → `QuestionnaireResponse.item.item.linkId` (468, tanpa BQ)<br>_Hilang nafsu makan/ kesulitan/ makan_ → `QuestionnaireResponse.item.item.linkId` (472, tanpa BQ)<br>_LiLA < 21 cm_ → `QuestionnaireResponse.item.item.linkId` (476, tanpa BQ)<br>_Gejala Depresi (dalam 2 minggu terakhir)_ → `QuestionnaireResponse.item.linkId` (480, tanpa BQ)<br>_Perasaan sedih, tertekan, atau putus asa_ → `QuestionnaireResponse.item.item.linkId` (482, tanpa BQ)<br>_Sedikit minat atau kesenangan dalam melakukan sesuatu_ → `QuestionnaireResponse.item.item.linkId` (486, tanpa BQ)<br>_Gangguan Penglihatan_ → `QuestionnaireResponse.item.linkId` (490, tanpa BQ)<br>_Masalah pada mata (sulit lihat jauh, membaca, penyakit mata, sedang dalam pengobatan Hipertensi/ diabetes)_ → `QuestionnaireResponse.item.item.linkId` (492, tanpa BQ)<br>_Tes Melihat_ → `QuestionnaireResponse.item.item.linkId` (496, tanpa BQ)<br>_Gangguan Pendengaran_ → `QuestionnaireResponse.item.linkId` (500, tanpa BQ)<br>_Tes Bisik_ → `QuestionnaireResponse.item.answer.item.linkId` (502, tanpa BQ) |
| 26 | 506–591 | QuestionnaireResponse | https://fhir.kemkes.go.id/sp/Questionnaire/Q00017 | – | _Apakah Anda sering merasa sakit kepala?_ → `QuestionnaireResponse.item.linkId` (516, tanpa BQ)<br>_Apakah Anda kehilangan nafsu makan?_ → `QuestionnaireResponse.item.linkId` (520, tanpa BQ)<br>_Apakah tidur Anda tidak nyenyak?_ → `QuestionnaireResponse.item.linkId` (524, tanpa BQ)<br>_Apakah Anda mudah merasa takut?_ → `QuestionnaireResponse.item.linkId` (528, tanpa BQ)<br>_Apakah tangan Anda gemetar?_ → `QuestionnaireResponse.item.linkId` (532, tanpa BQ)<br>_Apakah Anda mengalami gangguan pencernaan?_ → `QuestionnaireResponse.item.linkId` (536, tanpa BQ)<br>_Apakah Anda merasa sulit berpikir jernih?_ → `QuestionnaireResponse.item.linkId` (540, tanpa BQ)<br>_Apakah Anda merasa tidak bahagia?_ → `QuestionnaireResponse.item.linkId` (544, tanpa BQ)<br>_Apakah Anda lebih sering menangis?_ → `QuestionnaireResponse.item.linkId` (548, tanpa BQ)<br>_Apakah Anda merasa sulit untuk menikmati aktivitas sehari-hari?_ → `QuestionnaireResponse.item.linkId` (552, tanpa BQ)<br>_Apakah Anda mengalami kesulitan untuk mengambil keputusan?_ → `QuestionnaireResponse.item.linkId` (556, tanpa BQ)<br>_Apakah aktivitas/ tugas sehari-hari Anda terbengkalai?_ → `QuestionnaireResponse.item.linkId` (560, tanpa BQ)<br>_Apakah Anda merasa tidak mampu berperan dalam kehidupan ini?_ → `QuestionnaireResponse.item.linkId` (564, tanpa BQ)<br>_Apakah Anda kehilangan minat terhadap banyak hal?_ → `QuestionnaireResponse.item.linkId` (568, tanpa BQ)<br>_Apakah Anda merasa tidak berharga?_ → `QuestionnaireResponse.item.linkId` (572, tanpa BQ)<br>_Apakah Anda mempunyai pikiran untuk mengakhiri hidup Anda?_ → `QuestionnaireResponse.item.linkId` (576, tanpa BQ)<br>_Apakah Anda merasa lelah sepanjang waktu?_ → `QuestionnaireResponse.item.linkId` (580, tanpa BQ)<br>_Apakah Anda merasa tidak enak di perut?_ → `QuestionnaireResponse.item.linkId` (584, tanpa BQ)<br>_Apakah Anda mudah lelah?_ → `QuestionnaireResponse.item.linkId` (588, tanpa BQ) |
| 27 | 593–604 | Observation | 3457005 | Patient referral | _Rujuk_ → `Observation.valueBoolean` (596, tanpa BQ) |
| 28 | 606–625 | Procedure | 410314003 | Health promotion education, guidance, and counseling | _Apakah dilakukan konseling_ → `Procedure.category.coding` (606, tanpa BQ)<br>_Sebutkan topik konseling yang dilakukan_ → `Procedure.code.coding.code` (610, tanpa BQ)<br>_Jika dijawab lainnya tambahkan mapping berikut_ → `Procedure.code.text` (618, tanpa BQ) |
| 29 | 626–631 | Observation | – | – | – |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 21 |
| QuestionnaireResponse | 4 |
| Condition | 3 |
| Procedure | 1 |
| **Total** | **29** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 6 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 2 | 18 | Observation | `Observation.code.coding` | 8302-2 | Body height | http://loinc.org |
| 3 | 31 | Observation | `Observation.code.coding` | 39156-5 | Body mass index (BMI) [Ratio] | http://loinc.org |
| 4 | 32 | Observation | `Observation.interpretation.coding` | 717933005 | Severe thinness in adulthood | http://snomed.info/sct |
| 5 | 35 | Observation | `Observation.interpretation.coding` | 248342006 | Underweight | http://snomed.info/sct |
| 6 | 38 | Observation | `Observation.interpretation.coding` | 43664005 | Normal weight | http://snomed.info/sct |
| 7 | 43 | Observation | `Observation.interpretation.coding` | 238131007 | Overweight | http://snomed.info/sct |
| 8 | 48 | Observation | `Observation.interpretation.coding` | 414915002 | Obese | http://snomed.info/sct |
| 9 | 61 | Observation | `Observation.code.coding` | 396552003 | Abdominal circumference | http://snomed.info/sct |
| 10 | 73 | Observation | `Observation.code.coding` | 284473002 | Mid upper arm circumference | http://snomed.info/sct |
| 11 | 84 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 12 | 96 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://snomed.info/sct |
| 13 | 108 | Observation | `Observation.code.coding` | 268607006 | Hypertension risk level | http://snomed.info/sct |
| 14 | 120 | Observation | `Observation.interpretation.coding` | OI000040 | Tekanan Darah Optimal | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 15 | 122 | Observation | `Observation.interpretation.coding` | 2004005 | Normal blood pressure | http://snomed.info/sct |
| 16 | 124 | Observation | `Observation.interpretation.coding` | OI000041 | Tekanan Darah Normal Tinggi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 17 | 128 | Observation | `Observation.code.coding` | 8310-5 | Body temperature | http://loinc.org |
| 18 | 140 | Condition | `Condition.code.coding` | 160357008 | Family history: Hypertension | http://snomed.info/sct |
| 19 | 141 | Condition | `Condition.code.coding` | 160303001 | Family history of diabetes mellitus | http://snomed.info/sct |
| 20 | 142 | Condition | `Condition.code.coding` | 275104002 | Family history of stroke | http://snomed.info/sct |
| 21 | 143 | Condition | `Condition.code.coding` | 429959009 | Family history of heart failure | http://snomed.info/sct |
| 22 | 144 | Condition | `Condition.code.coding` | 275937001 | Family history of malignant neoplasm |  |
| 23 | 145 | Condition | `Condition.code.coding` | 160314003 | Family history: Hypercholesterolemia | http://snomed.info/sct |
| 24 | 146 | Condition | `Condition.code.coding` | 160324006 | Family history of mental disorder | http://snomed.info/sct |
| 25 | 147 | Condition | `Condition.code.coding` | 160266009 | No family history of clinical finding | http://snomed.info/sct |
| 26 | 154 | Condition | `Condition.code.coding` | 161501007 | History of hypertension | http://snomed.info/sct |
| 27 | 155 | Condition | `Condition.code.coding` | 161445009 | History of diabetes mellitus | http://snomed.info/sct |
| 28 | 156 | Condition | `Condition.code.coding` | 275526006 | History of cerebrovascular accident | http://snomed.info/sct |
| 29 | 157 | Condition | `Condition.code.coding` | 275544003 | History of heart disorder | http://snomed.info/sct |
| 30 | 158 | Condition | `Condition.code.coding` | 266987004 | History of malignant neoplasm | http://snomed.info/sct |
| 31 | 159 | Condition | `Condition.code.coding` | 414416008 | History of hypercholesterolemia | http://snomed.info/sct |
| 32 | 160 | Condition | `Condition.code.coding` | 443508001 | No history of clinical finding in subject | http://snomed.info/sct |
| 33 | 167 | Condition | `Condition.code.coding` | 161501007 | History of hypertension | http://snomed.info/sct |
| 34 | 168 | Condition | `Condition.code.coding` | 161445009 | History of diabetes mellitus | http://snomed.info/sct |
| 35 | 169 | Condition | `Condition.code.coding` | 275526006 | History of cerebrovascular accident | http://snomed.info/sct |
| 36 | 170 | Condition | `Condition.code.coding` | 275544003 | History of heart disorder | http://snomed.info/sct |
| 37 | 171 | Condition | `Condition.code.coding` | 266987004 | History of malignant neoplasm | http://snomed.info/sct |
| 38 | 172 | Condition | `Condition.code.coding` | 414416008 | History of hypercholesterolemia | http://snomed.info/sct |
| 39 | 173 | Condition | `Condition.code.coding` | 443508001 | No history of clinical finding in subject | http://snomed.info/sct |
| 40 | 180 | Observation | `Observation.code.coding` | SP000658 | Perilaku Berisiko Diri Sendiri | http://terminology.kemkes.go.id/sp |
| 41 | 181 | Observation | `Observation.component.code.coding` | 77176002 | Smoker | http://snomed.info/sct |
| 42 | 184 | Observation | `Observation.valueCodeableConcept.coding` | SP000659 | Konsumsi Tinggi Gula | http://terminology.kemkes.go.id/sp |
| 43 | 187 | Observation | `Observation.valueCodeableConcept.coding` | SP000660 | Konsumsi Tinggi Garam | http://terminology.kemkes.go.id/sp |
| 44 | 190 | Observation | `Observation.valueCodeableConcept.coding` | SP000661 | Konsumsi Tinggi Lemak | http://terminology.kemkes.go.id/sp |
| 45 | 202 | Observation | `Observation.code.coding` | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 46 | 212 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 47 | 215 | Observation | `Observation.interpretation.coding` | 714628002 | Pre-diabetes | http://snomed.info/sct |
| 48 | 220 | Observation | `Observation.interpretation.coding` | 73211009 | Diabetes mellitus | http://snomed.info/sct |
| 49 | 251 | Observation | `Observation.code.coding` | 3457005 | Patient referral | http://snomed.info/sct |
| 50 | 264 | Observation | `Observation.code.coding` | 422256009 | Counts fingers - distance vision | http://snomed.info/sct |
| 51 | 266 | Observation | `Observation.valueCodeableConcept.coding` | 164727006 | Visual testing normal | http://snomed.info/sct |
| 52 | 267 | Observation | `Observation.valueCodeableConcept.coding` | 397540003 | Visual impairment | http://snomed.info/sct |
| 53 | 278 | Observation | `Observation.code.coding` | 422256009 | Counts fingers - distance vision | http://snomed.info/sct |
| 54 | 280 | Observation | `Observation.valueCodeableConcept.coding` | 164727006 | Visual testing normal | http://snomed.info/sct |
| 55 | 281 | Observation | `Observation.valueCodeableConcept.coding` | 397540003 | Visual impairment | http://snomed.info/sct |
| 56 | 292 | Observation | `Observation.code.coding` | 247301006 | Finding of ability to hear whisper | http://snomed.info/sct |
| 57 | 294 | Observation | `Observation.valueCodeableConcept.coding` | 275727004 | Hearing test normal | http://snomed.info/sct |
| 58 | 295 | Observation | `Observation.valueCodeableConcept.coding` | 300221005 | Hearing for whisper impaired | http://snomed.info/sct |
| 59 | 306 | Observation | `Observation.code.coding` | 247301006 | Finding of ability to hear whisper | http://snomed.info/sct |
| 60 | 308 | Observation | `Observation.valueCodeableConcept.coding` | 275727004 | Hearing test normal | http://snomed.info/sct |
| 61 | 309 | Observation | `Observation.valueCodeableConcept.coding` | 300221005 | Hearing for whisper impaired | http://snomed.info/sct |
| 62 | 330 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | female | Perempuan | http://hl7.org/fhir/administrative-gender |
| 63 | 331 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | male | Laki-Laki | http://hl7.org/fhir/administrative-gender |
| 64 | 334 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000726 | 40-49 tahun | http://terminology.kemkes.go.id/sp |
| 65 | 335 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000727 | 50-59 tahun | http://terminology.kemkes.go.id/sp |
| 66 | 336 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000728 | >= 60 tahun | http://terminology.kemkes.go.id/sp |
| 67 | 339 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000435 | <20 bungkus per tahun | http://terminology.kemkes.go.id/sp |
| 68 | 340 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000436 | 20-30 bungkus per tahun | http://terminology.kemkes.go.id/sp |
| 69 | 341 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000437 | >30 bungkus per tahun | http://terminology.kemkes.go.id/sp |
| 70 | 360 | Observation | `Observation.code.coding` | SP000111 | Hasil Kuesioner PUMA | http://terminology.kemkes.go.id/sp |
| 71 | 362 | Observation | `Observation.interpretation.coding` | 723505004 | Low risk | http://snomed.info/sct |
| 72 | 364 | Observation | `Observation.interpretation.coding` | 723509005 | High risk | http://snomed.info/sct |
| 73 | 374 | Observation | `Observation.code.coding` | 304492001 | Activities of daily living assessment | http://snomed.info/sct |
| 74 | 375 | Observation | `Observation.component.code.coding` | 96759-6 | Bowels | http://loinc.org |
| 75 | 376 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31627-5 | Incontinent (or needs to be given enemas) | http://loinc.org |
| 76 | 377 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31626-7 | Occasional accident | http://loinc.org |
| 77 | 378 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31625-9 | Continent | http://loinc.org |
| 78 | 379 | Observation | `Observation.component.code.coding` | 96760-4 | Bladder | http://loinc.org |
| 79 | 380 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31628-3 | Incontinent, or catheterized and unable to manage alone | http://loinc.org |
| 80 | 381 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31626-7 | Occasional accident | http://loinc.org |
| 81 | 382 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31625-9 | Continent | http://loinc.org |
| 82 | 383 | Observation | `Observation.component.code.coding` | 96767-9 | Grooming | http://loinc.org |
| 83 | 384 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31643-2 | Needs help with personal care | http://loinc.org |
| 84 | 385 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31644-0 | Independent face/hair/teeth/shaving (implements provided) | http://loinc.org |
| 85 | 386 | Observation | `Observation.component.code.coding` | 83183-4 | Toilet Use | http://loinc.org |
| 86 | 387 | Observation | `Observation.component.valueCodeableConcept.coding` | LA12304-4 | Dependent | http://loinc.org |
| 87 | 388 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31631-7 | Needs some help, but can do something alone | http://loinc.org |
| 88 | 389 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31632-5 | Independent (on and off, dressing, wiping) | http://loinc.org |
| 89 | 390 | Observation | `Observation.component.code.coding` | 83184-2 | Feeding | http://loinc.org |
| 90 | 391 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24937-7 | Unable | http://loinc.org |
| 91 | 392 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31630-9 | Needs help cutting, spreading butter, etc., or requires modified diet | http://loinc.org |
| 92 | 393 | Observation | `Observation.component.valueCodeableConcept.coding` | LA12302-8 | Independent | http://loinc.org |
| 93 | 394 | Observation | `Observation.component.code.coding` | 83185-9 | Transfer | http://loinc.org |
| 94 | 395 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31633-3 | Unable, no sitting balance | http://loinc.org |
| 95 | 396 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31634-1 | Major help (one or two people, physical), can sit | http://loinc.org |
| 96 | 397 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31635-8 | Minor help (verbal or physical) | http://loinc.org |
| 97 | 398 | Observation | `Observation.component.valueCodeableConcept.coding` | LA12302-8 | Independent | http://loinc.org |
| 98 | 399 | Observation | `Observation.component.code.coding` | 83186-7 | Mobility | http://loinc.org |
| 99 | 400 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31639-0 | Immobile or <50 yards | http://loinc.org |
| 100 | 401 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31640-8 | Wheelchair independent, including corners, >50 yards | http://loinc.org |
| 101 | 402 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31641-6 | Walks with help of one person (verbal or physical) >50 yards | http://loinc.org |
| 102 | 403 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31642-4 | Independent (but may use any aid; for example, stick) >50 yards | http://loinc.org |
| 103 | 404 | Observation | `Observation.component.code.coding` | 83182-6 | Dressing | http://loinc.org |
| 104 | 405 | Observation | `Observation.component.valueCodeableConcept.coding` | LA12304-4 | Dependent | http://loinc.org |
| 105 | 406 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31637-4 | Needs help but can do about half unaided | http://loinc.org |
| 106 | 407 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31638-2 | Independent (including buttons, zips, laces, etc.) | http://loinc.org |
| 107 | 408 | Observation | `Observation.component.code.coding` | 96758-8 | Stairs | http://loinc.org |
| 108 | 409 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24937-7 | Unable | http://loinc.org |
| 109 | 410 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31629-1 | Needs help (verbal, physical, carrying aid) | http://loinc.org |
| 110 | 411 | Observation | `Observation.component.valueCodeableConcept.coding` | LA12302-8 | Independent | http://loinc.org |
| 111 | 412 | Observation | `Observation.component.code.coding` | 83181-8 | Bathing | http://loinc.org |
| 112 | 413 | Observation | `Observation.component.valueCodeableConcept.coding` | LA12304-4 | Dependent | http://loinc.org |
| 113 | 414 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31636-6 | Independent (or in shower) | http://loinc.org |
| 114 | 417 | Observation | `Observation.code.coding` | 96762-0 | Barthel index panel | http://loinc.org |
| 115 | 418 | Observation | `Observation.interpretation.coding` | 371153006 | Independent | http://snomed.info/sct |
| 116 | 421 | Observation | `Observation.interpretation.coding` | OI000045 | Ketergantungan ringan | http://snomed.info/sct |
| 117 | 426 | Observation | `Observation.interpretation.coding` | OI000046 | Ketergantungan sedang | http://snomed.info/sct |
| 118 | 431 | Observation | `Observation.interpretation.coding` | OI000047 | Ketergantungan berat | http://snomed.info/sct |
| 119 | 436 | Observation | `Observation.interpretation.coding` | OI000048 | Ketergantungan total | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 120 | 595 | Observation | `Observation.code.coding` | 3457005 | Patient referral | http://snomed.info/sct |
| 121 | 607 | Procedure | `Procedure.code.coding` | 410314003 | Health promotion education, guidance, and counseling | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 56 |
| http://loinc.org | 47 |
| http://terminology.kemkes.go.id/sp | 11 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 3 |
| http://hl7.org/fhir/administrative-gender | 2 |
|  | 1 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 1 |
| **Total** | **121** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 2 | – | Tanggal kunjungan | – | `` |
| 3 | – | Kelompok Dasawisma | – | `` |
| 605 | – | Tanggal kunjungan | – | `` |
