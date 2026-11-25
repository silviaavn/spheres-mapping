# Output Form: KuApps BidanKu - Dewasa

Sumber: `mapping/phdt-data-dictionary-kuapps-bidanku-dewasa.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-kuapps-bidanku-dewasa.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 39 |
| Code (`jumlah code` = 1) | 122 |
| Code unik (code + CodeSystem) | 102 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 25 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 4–15 | Observation | 29463-7 | Body weight | _Berat Badan_ → `Observation.valueQuantity.value` (7, tanpa BQ) |
| 2 | 16–27 | Observation | 8302-2 | Body height | _Tinggi Badan_ → `Observation.valueQuantity.value` (19, tanpa BQ) |
| 3 | 29–58 | Observation | 39156-5 | Body mass index (BMI) [Ratio] | _IMT_ → `Observation.status` (29, tanpa BQ)<br>_Interpretasi IMT_ → `Observation.interpretation.coding` (32, tanpa BQ) |
| 4 | 59–78 | Observation | 396552003 | Abdominal circumference | _Lingkar Perut_ → `Observation.valueQuantity.value` (62, tanpa BQ)<br>_Interpretasi lingkar perut_ → `Observation.interpretation.coding` (64, tanpa BQ) |
| 5 | 79–93 | Observation | 284473002 | Mid upper arm circumference | _LiLA_ → `Observation.valueQuantity.value` (82, tanpa BQ)<br>_Status Gizi_ → `Observation.interpretation` (91, tanpa BQ) |
| 6 | 94–105 | Observation | 8480-6 | Systolic blood pressure | _Tekanan Darah Sistole_ → `Observation.valueQuantity.value` (97, tanpa BQ) |
| 7 | 106–117 | Observation | 8462-4 | Diastolic blood pressure | _Tekanan Darah Diastole_ → `Observation.valueQuantity.value` (109, tanpa BQ) |
| 8 | 118–137 | Observation | 268607006 | Hypertension risk level | _Interpretasi tekanan darah_ → `Observation.valueRatio.numerator.value` (128, tanpa BQ) |
| 9 | 138–152 | Observation | 8310-5 | Body temperature | _Suhu_ → `Observation.valueQuantity.value` (142, tanpa BQ)<br>_Interpretasi Suhu_ → `Observation.interpretation.coding` (144, tanpa BQ) |
| 10 | 153–166 | Condition | 160357008 | Family history: Hypertension | _Riwayat Keluarga_ → `Condition.clinicalStatus.coding` (153, tanpa BQ) |
| 11 | 167–183 | Condition | 161501007 | History of hypertension | _Riwayat diri Sendiri_ → `Condition.clinicalStatus.coding` (167, tanpa BQ) |
| 12 | 184–205 | Observation | SP000658 | Perilaku Berisiko Diri Sendiri | _Perilaku Berisiko Diri Sendiri_ → `Observation.component.valueBoolean` (188, tanpa BQ) |
| 13 | 206–219 | Observation | 67744-3 | Approximately how many cigarettes did you smoke on average | _Jika merokok, berapa jumlah batang rokok yang dikonsumsi dalam sehari?_ → `Observation.valueRatio.numerator.value` (209, tanpa BQ) |
| 14 | 220–242 | Observation | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | _Gula Darah Sewaktu_ → `Observation.valueQuantity.value` (223, tanpa BQ)<br>_Interpretasi Gula Darah Sewaktu_ → `Observation.interpretation.coding` (232, tanpa BQ) |
| 15 | 243–254 | Observation | 243816001 | Contraception status | _Menggunakan alat kontrasepsi_ → `Observation.valueBoolean` (246, tanpa BQ) |
| 16 | 256–269 | Observation | 422256009 | Counts fingers - distance vision | _Mata Kanan_ → `Observation.valueCodeableConcept.coding` (260, tanpa BQ) |
| 17 | 270–283 | Observation | 422256009 | Counts fingers - distance vision | _Mata Kiri_ → `Observation.valueCodeableConcept.coding` (274, tanpa BQ) |
| 18 | 284–297 | Observation | 247301006 | Finding of ability to hear whisper | _Telinga Kanan_ → `Observation.valueCodeableConcept.coding` (288, tanpa BQ) |
| 19 | 298–311 | Observation | 247301006 | Finding of ability to hear whisper | _Telinga Kiri_ → `Observation.valueCodeableConcept.coding` (302, tanpa BQ) |
| 20 | 312–351 | QuestionnaireResponse | https://fhir.kemkes.go.id/sp/Questionnaire/Q00015 | – | _Jenis Kelamin_ → `QuestionnaireResponse.item.linkId` (322, tanpa BQ)<br>_Usia_ → `QuestionnaireResponse.item.linkId` (326, tanpa BQ)<br>_Merokok_ → `QuestionnaireResponse.item.linkId` (331, tanpa BQ)<br>_Apakah Anda Pernah merasa napas pendek ketika berjalan lebih cepat pada jalan yang datar atau pada jalan yang sedikit menanjak?_ → `QuestionnaireResponse.item.linkId` (336, tanpa BQ)<br>_Apakah anda mempunyai dahak yang berasal dari paru atau kesulitan mengeluarkan dahak saat Anda sedang tidak menderita flu?_ → `QuestionnaireResponse.item.linkId` (340, tanpa BQ)<br>_Apakah anda Biasanya batuk saat Anda sedang tidak menderita flu?_ → `QuestionnaireResponse.item.linkId` (344, tanpa BQ)<br>_Apakah Dokter atau tenaga kesehatan lainnya pernah meminta Anda untuk melakukan pemeriksaan spirometri atau peakflow meter (meniup ke dalam suatu alat)?_ → `QuestionnaireResponse.item.linkId` (348, tanpa BQ) |
| 21 | 352–365 | Observation | SP000111 | Hasil Kuesioner PUMA | _Skor PUMA_ → `Observation.status` (352, tanpa BQ) |
| 22 | 366–391 | QuestionnaireResponse | https://fhir.kemkes.go.id/sp/Questionnaire/Q00016 | – | _Batuk terus menerus_ → `QuestionnaireResponse.item.linkId` (376, tanpa BQ)<br>_Demam lebih dari ≥ 2 minggu_ → `QuestionnaireResponse.item.linkId` (380, tanpa BQ)<br>_BB tidak naik atau turun dalam 2 bulan berturut-turut_ → `QuestionnaireResponse.item.linkId` (384, tanpa BQ)<br>_Kontak erat dengan Pasien TBC_ → `QuestionnaireResponse.item.linkId` (388, tanpa BQ) |
| 23 | 392–404 | Observation | 171126009 | Tuberculosis screening | – |
| 24 | 405–416 | Observation | 3457005 | Patient referral | _Rujuk_ → `Observation.valueBoolean` (408, tanpa BQ) |
| 25 | 417–502 | QuestionnaireResponse | https://fhir.kemkes.go.id/sp/Questionnaire/Q00017 | – | _Apakah Anda sering merasa sakit kepala?_ → `QuestionnaireResponse.item.linkId` (427, tanpa BQ)<br>_Apakah Anda kehilangan nafsu makan?_ → `QuestionnaireResponse.item.linkId` (431, tanpa BQ)<br>_Apakah tidur Anda tidak nyenyak?_ → `QuestionnaireResponse.item.linkId` (435, tanpa BQ)<br>_Apakah Anda mudah merasa takut?_ → `QuestionnaireResponse.item.linkId` (439, tanpa BQ)<br>_Apakah tangan Anda gemetar?_ → `QuestionnaireResponse.item.linkId` (443, tanpa BQ)<br>_Apakah Anda mengalami gangguan pencernaan?_ → `QuestionnaireResponse.item.linkId` (447, tanpa BQ)<br>_Apakah Anda merasa sulit berpikir jernih?_ → `QuestionnaireResponse.item.linkId` (451, tanpa BQ)<br>_Apakah Anda merasa tidak bahagia?_ → `QuestionnaireResponse.item.linkId` (455, tanpa BQ)<br>_Apakah Anda lebih sering menangis?_ → `QuestionnaireResponse.item.linkId` (459, tanpa BQ)<br>_Apakah Anda merasa sulit untuk menikmati aktivitas sehari-hari?_ → `QuestionnaireResponse.item.linkId` (463, tanpa BQ)<br>_Apakah Anda mengalami kesulitan untuk mengambil keputusan?_ → `QuestionnaireResponse.item.linkId` (467, tanpa BQ)<br>_Apakah aktivitas/ tugas sehari-hari Anda terbengkalai?_ → `QuestionnaireResponse.item.linkId` (471, tanpa BQ)<br>_Apakah Anda merasa tidak mampu berperan dalam kehidupan ini?_ → `QuestionnaireResponse.item.linkId` (475, tanpa BQ)<br>_Apakah Anda kehilangan minat terhadap banyak hal?_ → `QuestionnaireResponse.item.linkId` (479, tanpa BQ)<br>_Apakah Anda merasa tidak berharga?_ → `QuestionnaireResponse.item.linkId` (483, tanpa BQ)<br>_Apakah Anda mempunyai pikiran untuk mengakhiri hidup Anda?_ → `QuestionnaireResponse.item.linkId` (487, tanpa BQ)<br>_Apakah Anda merasa lelah sepanjang waktu?_ → `QuestionnaireResponse.item.linkId` (491, tanpa BQ)<br>_Apakah Anda merasa tidak enak di perut?_ → `QuestionnaireResponse.item.linkId` (495, tanpa BQ)<br>_Apakah Anda mudah lelah?_ → `QuestionnaireResponse.item.linkId` (499, tanpa BQ) |
| 26 | 504–515 | Observation | 3457005 | Patient referral | _Rujuk_ → `Observation.valueBoolean` (507, tanpa BQ) |
| 27 | 516–530 | Observation | SP000700 | Tahap Keluarga Sejahtera | _Apakah klasifikasi keluarga saat ini (Tahapan Keluarga Sejahtera)?"_ → `Observation.valueCodeableConcept.coding` (519, tanpa BQ) |
| 28 | 531–541 | Observation | 726001007 | Past pregnancy history of live birth | _Jumlah anak yang hidup_ → `Observation.valueInteger` (534, tanpa BQ) |
| 29 | 542–552 | Observation | SP000710 | Jumlah anak yang meninggal | _Jumlah anak yang meninggal_ → `Observation.valueInteger` (545, tanpa BQ) |
| 30 | 553–564 | Observation | 92662-6 | Current age or age at death of Family member | _Berapa usia anak yang meninggal? (mengikuti jumlah anak meninggal)_ → `Observation.valueQuantity.value` (556, tanpa BQ) |
| 31 | 565–576 | Observation | 104759008 | Iodine measurement | _Apakah dilakuan pemantauan yodium?_ → `Observation.valueBoolean` (568, tanpa BQ) |
| 32 | 577–589 | Observation | SP000706 | Pemantauan Yodium | _Bagaimana kandungan yodium?_ → `Observation.valueCodeableConcept.coding` (580, tanpa BQ) |
| 33 | 590–607 | Immunization | VG139 | Td | _Status TT_ → `Immunization.status` (590, tanpa BQ) |
| 34 | 608–626 | Observation | 8659-5 | Birth control method - Reported | _Apakah jenis kontrasepsi yang digunakan saat ini?_ → `Observation.valueCodeableConcept.coding` (611, tanpa BQ) |
| 35 | 627–638 | Observation | SP000711 | Rencana mengganti kontrasepsi | _Apakah ada rencana untuk mengganti kontrasepsi?_ → `Observation.valueBoolean` (630, tanpa BQ) |
| 36 | 639–649 | Observation | SP000712 | Tanggal rencana mulai mengganti kontrasepsi | _Kapan rencana mengganti kontrasepsi?_ → `Observation.valueDateTime` (642, tanpa BQ) |
| 37 | 650–668 | Observation | – | – | _Apakah rencana jenis kontrasepsi baru yang akan digunakan?_ → `Observation.valueCodeableConcept.coding` (653, tanpa BQ) |
| 38 | 670–687 | Procedure | 410314003 | Health promotion education, guidance, and counseling | _Apakah dilakukan konseling_ → `Procedure.category.coding` (670, tanpa BQ)<br>_Sebutkan topik konseling yang dilakukan_ → `Procedure.code.coding.code` (674, tanpa BQ)<br>_Jika dijawab lainnya tambahkan mapping berikut_ → `Procedure.code.text` (680, tanpa BQ) |
| 39 | 688–693 | Observation | – | – | – |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 32 |
| QuestionnaireResponse | 3 |
| Condition | 2 |
| Immunization | 1 |
| Procedure | 1 |
| **Total** | **39** |

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
| 10 | 64 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 11 | 66 | Observation | `Observation.interpretation.coding` | 248311001 | Central Obesity | http://snomed.info/sct |
| 12 | 68 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 13 | 70 | Observation | `Observation.interpretation.coding` | 248311001 | Central Obesity | http://snomed.info/sct |
| 14 | 81 | Observation | `Observation.code.coding` | 284473002 | Mid upper arm circumference | http://snomed.info/sct |
| 15 | 91 | Observation | `Observation.interpretation` | OI000018 | Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 16 | 92 | Observation | `Observation.interpretation` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 17 | 93 | Observation | `Observation.interpretation` | OI000035 | Risiko Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 18 | 96 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 19 | 108 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://snomed.info/sct |
| 20 | 120 | Observation | `Observation.code.coding` | 268607006 | Hypertension risk level | http://snomed.info/sct |
| 21 | 132 | Observation | `Observation.interpretation.coding` | OI000040 | Tekanan Darah Optimal | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 22 | 134 | Observation | `Observation.interpretation.coding` | 2004005 | Normal blood pressure | http://snomed.info/sct |
| 23 | 136 | Observation | `Observation.interpretation.coding` | OI000041 | Tekanan Darah Normal Tinggi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 24 | 140 | Observation | `Observation.code.coding` | 8310-5 | Body temperature | http://loinc.org |
| 25 | 141 | Observation | `Observation.code.coding` | ANC.B8.DE34 | Body temperature | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 26 | 144 | Observation | `Observation.interpretation.coding` | 386689009 | Hypothermia | http://snomed.info/sct |
| 27 | 145 | Observation | `Observation.interpretation.coding` | 87273009 | Temperature norma | http://snomed.info/sct |
| 28 | 146 | Observation | `Observation.interpretation.coding` | 1197782006 | Hyperthermia | http://snomed.info/sct |
| 29 | 155 | Condition | `Condition.code.coding` | 160357008 | Family history: Hypertension | http://snomed.info/sct |
| 30 | 156 | Condition | `Condition.code.coding` | 160303001 | Family history of diabetes mellitus | http://snomed.info/sct |
| 31 | 157 | Condition | `Condition.code.coding` | 275104002 | Family history of stroke | http://snomed.info/sct |
| 32 | 158 | Condition | `Condition.code.coding` | 429959009 | Family history of heart failure | http://snomed.info/sct |
| 33 | 159 | Condition | `Condition.code.coding` | 275937001 | Family history of malignant neoplasm |  |
| 34 | 160 | Condition | `Condition.code.coding` | 160314003 | Family history: Hypercholesterolemia | http://snomed.info/sct |
| 35 | 161 | Condition | `Condition.code.coding` | 160324006 | Family history of mental disorder | http://snomed.info/sct |
| 36 | 162 | Condition | `Condition.code.coding` | 160266009 | No family history of clinical finding | http://snomed.info/sct |
| 37 | 169 | Condition | `Condition.code.coding` | 161501007 | History of hypertension | http://snomed.info/sct |
| 38 | 170 | Condition | `Condition.code.coding` | 161445009 | History of diabetes mellitus | http://snomed.info/sct |
| 39 | 171 | Condition | `Condition.code.coding` | 275526006 | History of cerebrovascular accident | http://snomed.info/sct |
| 40 | 172 | Condition | `Condition.code.coding` | 275544003 | History of heart disorder | http://snomed.info/sct |
| 41 | 173 | Condition | `Condition.code.coding` | 266987004 | History of malignant neoplasm | http://snomed.info/sct |
| 42 | 174 | Condition | `Condition.code.coding` | 414416008 | History of hypercholesterolemia | http://snomed.info/sct |
| 43 | 175 | Condition | `Condition.code.coding` | 429721005 | History of hepatitis B |  |
| 44 | 176 | Condition | `Condition.code.coding` | 161414005 | History of tuberculosis |  |
| 45 | 177 | Condition | `Condition.code.coding` | 686976671000119100 | History of administration of human immunodeficiency virus pre-exposure prophylaxis |  |
| 46 | 179 | Condition | `Condition.code.coding` | 443508001 | No history of clinical finding in subject | http://snomed.info/sct |
| 47 | 186 | Observation | `Observation.code.coding` | SP000658 | Perilaku Berisiko Diri Sendiri | http://terminology.kemkes.go.id/sp |
| 48 | 187 | Observation | `Observation.component.code.coding` | 77176002 | Smoker | http://snomed.info/sct |
| 49 | 190 | Observation | `Observation.valueCodeableConcept.coding` | SP000659 | Konsumsi Tinggi Gula | http://terminology.kemkes.go.id/sp |
| 50 | 193 | Observation | `Observation.valueCodeableConcept.coding` | SP000660 | Konsumsi Tinggi Garam | http://terminology.kemkes.go.id/sp |
| 51 | 196 | Observation | `Observation.valueCodeableConcept.coding` | SP000661 | Konsumsi Tinggi Lemak | http://terminology.kemkes.go.id/sp |
| 52 | 208 | Observation | `Observation.code.coding` | 67744-3 | Approximately how many cigarettes did you smoke on average | http://loinc.org |
| 53 | 222 | Observation | `Observation.code.coding` | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 54 | 232 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 55 | 235 | Observation | `Observation.interpretation.coding` | 714628002 | Pre-diabetes | http://snomed.info/sct |
| 56 | 240 | Observation | `Observation.interpretation.coding` | 73211009 | Diabetes mellitus | http://snomed.info/sct |
| 57 | 245 | Observation | `Observation.code.coding` | 243816001 | Contraception status | http://snomed.info/sct |
| 58 | 258 | Observation | `Observation.code.coding` | 422256009 | Counts fingers - distance vision | http://snomed.info/sct |
| 59 | 260 | Observation | `Observation.valueCodeableConcept.coding` | 164727006 | Visual testing normal | http://snomed.info/sct |
| 60 | 261 | Observation | `Observation.valueCodeableConcept.coding` | 397540003 | Visual impairment | http://snomed.info/sct |
| 61 | 272 | Observation | `Observation.code.coding` | 422256009 | Counts fingers - distance vision | http://snomed.info/sct |
| 62 | 274 | Observation | `Observation.valueCodeableConcept.coding` | 164727006 | Visual testing normal | http://snomed.info/sct |
| 63 | 275 | Observation | `Observation.valueCodeableConcept.coding` | 397540003 | Visual impairment | http://snomed.info/sct |
| 64 | 286 | Observation | `Observation.code.coding` | 247301006 | Finding of ability to hear whisper | http://snomed.info/sct |
| 65 | 288 | Observation | `Observation.valueCodeableConcept.coding` | 275727004 | Hearing test normal | http://snomed.info/sct |
| 66 | 289 | Observation | `Observation.valueCodeableConcept.coding` | 300221005 | Hearing for whisper impaired | http://snomed.info/sct |
| 67 | 300 | Observation | `Observation.code.coding` | 247301006 | Finding of ability to hear whisper | http://snomed.info/sct |
| 68 | 302 | Observation | `Observation.valueCodeableConcept.coding` | 275727004 | Hearing test normal | http://snomed.info/sct |
| 69 | 303 | Observation | `Observation.valueCodeableConcept.coding` | 300221005 | Hearing for whisper impaired | http://snomed.info/sct |
| 70 | 324 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | female | Perempuan | http://hl7.org/fhir/administrative-gender |
| 71 | 325 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | male | Laki-Laki | http://hl7.org/fhir/administrative-gender |
| 72 | 328 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000726 | 40-49 tahun | http://terminology.kemkes.go.id/sp |
| 73 | 329 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000727 | 50-59 tahun | http://terminology.kemkes.go.id/sp |
| 74 | 330 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000728 | >= 60 tahun | http://terminology.kemkes.go.id/sp |
| 75 | 333 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000435 | <20 bungkus per tahun | http://terminology.kemkes.go.id/sp |
| 76 | 334 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000436 | 20-30 bungkus per tahun | http://terminology.kemkes.go.id/sp |
| 77 | 335 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000437 | >30 bungkus per tahun | http://terminology.kemkes.go.id/sp |
| 78 | 354 | Observation | `Observation.code.coding` | SP000111 | Hasil Kuesioner PUMA | http://terminology.kemkes.go.id/sp |
| 79 | 356 | Observation | `Observation.interpretation.coding` | 723505004 | Low risk | http://snomed.info/sct |
| 80 | 358 | Observation | `Observation.interpretation.coding` | 723509005 | High risk | http://snomed.info/sct |
| 81 | 393 | Observation | `Observation.interpretation.coding` | 772170009 | Tuberculosis suspected | http://snomed.info/sct |
| 82 | 394 | Observation | `Observation.interpretation.coding` | SP000789 | Bukan terduga TBC | http://terminology.kemkes.go.id/sp |
| 83 | 397 | Observation | `Observation.code.coding` | 171126009 | Tuberculosis screening | http://snomed.info/sct |
| 84 | 407 | Observation | `Observation.code.coding` | 3457005 | Patient referral | http://snomed.info/sct |
| 85 | 506 | Observation | `Observation.code.coding` | 3457005 | Patient referral | http://snomed.info/sct |
| 86 | 518 | Observation | `Observation.code.coding` | SP000700 | Tahap Keluarga Sejahtera | http://terminology.kemkes.go.id/sp |
| 87 | 519 | Observation | `Observation.valueCodeableConcept.coding` | SP000701 | Pra KS | http://terminology.kemkes.go.id/sp |
| 88 | 520 | Observation | `Observation.valueCodeableConcept.coding` | SP000702 | KS I | http://terminology.kemkes.go.id/sp |
| 89 | 521 | Observation | `Observation.valueCodeableConcept.coding` | SP000703 | KS II | http://terminology.kemkes.go.id/sp |
| 90 | 522 | Observation | `Observation.valueCodeableConcept.coding` | SP000704 | KS III | http://terminology.kemkes.go.id/sp |
| 91 | 523 | Observation | `Observation.valueCodeableConcept.coding` | SP000705 | KS III+ | http://terminology.kemkes.go.id/sp |
| 92 | 533 | Observation | `Observation.code.coding` | 726001007 | Past pregnancy history of live birth | http://snomed.info/sct |
| 93 | 544 | Observation | `Observation.code.coding` | SP000710 | Jumlah anak yang meninggal | http://terminology.kemkes.go.id/sp |
| 94 | 555 | Observation | `Observation.code.coding` | 92662-6 | Current age or age at death of Family member | http://loinc.org |
| 95 | 567 | Observation | `Observation.code.coding` | 104759008 | Iodine measurement | http://snomed.info/sct |
| 96 | 579 | Observation | `Observation.code.coding` | SP000706 | Pemantauan Yodium | http://terminology.kemkes.go.id/sp |
| 97 | 580 | Observation | `Observation.valueCodeableConcept.coding` | SP000707 | Garam mengandung cukup yodium | http://terminology.kemkes.go.id/sp |
| 98 | 581 | Observation | `Observation.valueCodeableConcept.coding` | SP000708 | Garam memiiki yodium dalam batas rendah | http://terminology.kemkes.go.id/sp |
| 99 | 582 | Observation | `Observation.valueCodeableConcept.coding` | SP000709 | Garam tanpa yodium | http://terminology.kemkes.go.id/sp |
| 100 | 592 | Immunization | `Immunization.vaccineCode.coding` | VG139 | Td | http://sys-ids.kemkes.go.id/kfa |
| 101 | 610 | Observation | `Observation.code.coding` | 8659-5 | Birth control method - Reported | http://loinc.org |
| 102 | 611 | Observation | `Observation.valueCodeableConcept.coding` | 237122005 | Lactational amenorrhea | http://snomed.info/sct |
| 103 | 612 | Observation | `Observation.valueCodeableConcept.coding` | LA6523-0 | Condom | http://loinc.org |
| 104 | 613 | Observation | `Observation.valueCodeableConcept.coding` | LA6524-8 | Oral contraceptive pill | http://loinc.org |
| 105 | 614 | Observation | `Observation.valueCodeableConcept.coding` | LA6525-5 | Injectable/implantable hormone | http://loinc.org |
| 106 | 615 | Observation | `Observation.valueCodeableConcept.coding` | LA6527-1 | Intrauterine device | http://loinc.org |
| 107 | 616 | Observation | `Observation.valueCodeableConcept.coding` | 40388003 | Implant, device | http://snomed.info/sct |
| 108 | 617 | Observation | `Observation.valueCodeableConcept.coding` | 77543007 | Ligation of fallopian tube | http://snomed.info/sct |
| 109 | 618 | Observation | `Observation.valueCodeableConcept.coding` | 22523008 | Vasectomy | http://snomed.info/sct |
| 110 | 619 | Observation | `Observation.dataAbsentReason.coding` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 111 | 629 | Observation | `Observation.code.coding` | SP000711 | Rencana mengganti kontrasepsi | http://terminology.kemkes.go.id/sp |
| 112 | 641 | Observation | `Observation.code.coding` | SP000712 | Tanggal rencana mulai mengganti kontrasepsi | http://terminology.kemkes.go.id/sp |
| 113 | 653 | Observation | `Observation.valueCodeableConcept.coding` | 237122005 | Lactational amenorrhea | http://snomed.info/sct |
| 114 | 654 | Observation | `Observation.valueCodeableConcept.coding` | LA6523-0 | Condom | http://loinc.org |
| 115 | 655 | Observation | `Observation.valueCodeableConcept.coding` | LA6524-8 | Oral contraceptive pill | http://loinc.org |
| 116 | 656 | Observation | `Observation.valueCodeableConcept.coding` | LA6525-5 | Injectable/implantable hormone | http://loinc.org |
| 117 | 657 | Observation | `Observation.valueCodeableConcept.coding` | LA6527-1 | Intrauterine device | http://loinc.org |
| 118 | 658 | Observation | `Observation.valueCodeableConcept.coding` | 40388003 | Implant, device | http://snomed.info/sct |
| 119 | 659 | Observation | `Observation.valueCodeableConcept.coding` | 77543007 | Ligation of fallopian tube | http://snomed.info/sct |
| 120 | 660 | Observation | `Observation.valueCodeableConcept.coding` | 22523008 | Vasectomy | http://snomed.info/sct |
| 121 | 661 | Observation | `Observation.dataAbsentReason.coding` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 122 | 671 | Procedure | `Procedure.code.coding` | 410314003 | Health promotion education, guidance, and counseling | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 62 |
| http://terminology.kemkes.go.id/sp | 25 |
| http://loinc.org | 17 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 4 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 4 |
|  | 4 |
| http://hl7.org/fhir/administrative-gender | 2 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 2 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 1 |
| http://sys-ids.kemkes.go.id/kfa | 1 |
| **Total** | **122** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 2 | – | Tanggal kunjungan | – | `` |
| 3 | – | Kelompok Dasawisma | – | `` |
| 669 | – | Tanggal kunjungan | – | `` |
