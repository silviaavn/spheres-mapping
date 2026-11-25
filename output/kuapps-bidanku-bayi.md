# Output Form: KuApps BidanKu - Bayi

Sumber: `mapping/phdt-data-dictionary-kuapps-bidanku-bayi.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-kuapps-bidanku-bayi.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 101 |
| Code (`jumlah code` = 1) | 242 |
| Code unik (code + CodeSystem) | 203 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 17 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–14 | Encounter | – | – | _Tanggal kunjungan_ → `Encounter.period.start` (2, tanpa BQ) |
| 2 | 15–22 | Condition | Z00.1 | Routine child health examination | – |
| 3 | 32–42 | Observation | SP000699 | Kelompok Dasawisma | _Dasawisma group_ → `Observation.valueString` (35, tanpa BQ) |
| 4 | 43–54 | Observation | SP000132 | Memiliki Buku KIA | _Apakah pasien memiliki buku KIA?_ → `Observation.valueBoolean` (46, tanpa BQ) |
| 5 | 55–66 | Observation | 76516-4 | Gestational age—​at birth | _Usia Gestasi_ → `Observation.valueQuantity.value` (58, tanpa BQ) |
| 6 | 67–76 | Procedure | 431868002 | Initiation of breastfeeding | _Inisiasi Menyusui Dini_ → `Procedure.category.coding` (67, tanpa BQ) |
| 7 | 77–88 | Observation | OC000016 | Waktu Inisiasi Menyusui Dini | _Jika Ya, Waktu Inisiasi Menyusui Dini_ → `Observation.valueCodeableConcept.coding` (80, tanpa BQ) |
| 8 | 89–100 | Observation | 89269-5 | Body height Measured --at birth | _Panjang Badan Bayi Saat Lahir_ → `Observation.valueQuantity.value` (92, tanpa BQ) |
| 9 | 101–117 | Observation | 8339-4 | Birth weight Measured | _Berat Badan Bayi Saat Lahir_ → `Observation.valueQuantity.value` (104, tanpa BQ)<br>_Interpretasi_ → `Observation.interpretation.coding` (106, tanpa BQ) |
| 10 | 118–129 | Observation | 8290-9 | Head Occipital-frontal circumference --at birth- by Tape measure | _Lingkar Kepala Saat Lahir_ → `Observation.valueQuantity.value` (121, tanpa BQ) |
| 11 | 130–144 | Observation | 284473002 | Mid upper arm circumference | _Lingkar Lengan Atas_ → `Observation.valueQuantity.value` (133, tanpa BQ)<br>_Interpretasi Lila_ → `Observation.interpretation.coding` (135, tanpa BQ) |
| 12 | 145–156 | Observation | 8306-3 | Body height --lying | _Panjang Badan_ → `Observation.valueQuantity.value` (148, tanpa BQ) |
| 13 | 157–168 | Observation | 29463-7 | Body weight | _Berat Badan_ → `Observation.valueQuantity.value` (160, tanpa BQ) |
| 14 | 169–197 | Observation | 816159004 | Measured weight gain | _Penimbangan BB bayi dibandingkan pengukuran sebelumnya_ → `Observation.valueCodeableConcept.coding` (189, tanpa BQ) |
| 15 | 198–225 | Observation | 1153598007 | Weight for length z score | _BB/PB_ → `Observation.valueQuantity.value` (201, tanpa BQ) |
| 16 | 226–247 | Observation | 1153593003 | Weight for age z-score | _BB/U_ → `Observation.valueQuantity.value` (229, tanpa BQ) |
| 17 | 248–274 | Observation | 1153590000 | Length for age z-score | _PB/U_ → `Observation.valueQuantity.value` (251, tanpa BQ) |
| 18 | 275–286 | Observation | 8287-5 | Head Occipital-frontal circumference by Tape measure | _Lingkar kepala_ → `Observation.valueQuantity.value` (278, tanpa BQ) |
| 19 | 287–309 | Observation | 1153594009 | Head circumference for age z-score | _LK/U_ → `Observation.valueQuantity.value` (290, tanpa BQ) |
| 20 | 310–321 | Observation | 8867-4 | Heart rate | _Frekuensi Denyut Jantung_ → `Observation.valueQuantity.value` (313, tanpa BQ) |
| 21 | 322–333 | Observation | 8310-5 | Body temperature | _Suhu_ → `Observation.valueQuantity.value` (325, tanpa BQ) |
| 22 | 334–345 | Observation | 9279-1 | Respiratory rate | _Pernapasan_ → `Observation.valueQuantity.value` (337, tanpa BQ) |
| 23 | 346–357 | Observation | 10206-1 | Physical findings of Skin Narrative | _Kulit_ → `Observation.valueCodeableConcept.coding` (349, tanpa BQ) |
| 24 | 358–369 | Observation | 10199-8 | Physical findings of Head Narrative | _Kepala_ → `Observation.valueCodeableConcept.coding` (361, tanpa BQ) |
| 25 | 370–381 | Observation | 10197-2 | Physical findings of Eye Narrative | _Mata_ → `Observation.valueCodeableConcept.coding` (373, tanpa BQ) |
| 26 | 382–393 | Observation | 32453-3 | Physical findings of Mouth | _Mulut_ → `Observation.valueCodeableConcept.coding` (385, tanpa BQ) |
| 27 | 394–405 | Observation | 32453-3 | Physical findings of Abdomen Narrative | _Perut_ → `Observation.valueCodeableConcept.coding` (397, tanpa BQ) |
| 28 | 406–417 | Observation | 10192-3 | Physical findings of Back Narrative | _Punggung_ → `Observation.valueCodeableConcept.coding` (409, tanpa BQ) |
| 29 | 418–429 | Observation | 53505006 | Anal structure (body structure) | _Lubang Anus_ → `Observation.valueCodeableConcept.coding` (421, tanpa BQ) |
| 30 | 430–441 | Observation | 11400-9 | Physical findings of Genitalia Narrative | _Alat kelamin_ → `Observation.valueCodeableConcept.coding` (433, tanpa BQ) |
| 31 | 443–457 | Condition | 160357008 | Family history: Hypertension | _Riwayat keluarga_ → `Condition.clinicalStatus.coding` (443, tanpa BQ) |
| 32 | 458–469 | Observation | 1145307003 | Exclusively breastfed | _Pemberian ASI Eksklusif_ → `Observation.valueBoolean` (461, tanpa BQ) |
| 33 | 470–481 | Observation | 61432-1 | How old was sample person when he or she was first fed something other than breast milk or water [PhenX] | _Hingga umur berapa diberikan ASI eksklusif?_ → `Observation.valueQuantity.value` (473, tanpa BQ) |
| 34 | 482–493 | Observation | 413711008 | Breastfeeding (infant) | _Apakah saat ini anak masih diberikan ASI?_ → `Observation.valueBoolean` (485, tanpa BQ) |
| 35 | 494–503 | Procedure | 767224000 | Administration of vitamin A | _Apakah dilakukan pemberian vitamin A pada bayi?_ → `Procedure.category.coding` (494, tanpa BQ) |
| 36 | 504–513 | Procedure | SP000693 | Pelayanan Bawah Garis Merah | _Apakah bayi mendapatkan pelayan Berat Badan Bawah Garis Merah (BGM)?_ → `Procedure.category.coding` (504, tanpa BQ) |
| 37 | 514–523 | Procedure | SP000695 | PMT Pemulihan | _Apakah diberikan PMT Pemulihan_ → `Procedure.category.coding` (514, tanpa BQ) |
| 38 | 524–536 | Observation | SP000036 | Jenis PMT | _Jika ya, apa PMT yang diberikan?_ → `Observation.valueCodeableConcept.coding` (527, tanpa BQ) |
| 39 | 537–574 | Observation | OC000009 | Makanan Pendamping ASI (MPASI) | _MPASI_ → `Observation.valueBoolean` (540, tanpa BQ)<br>_Jenis MPASI yang diberikan_ → `Observation.component.code.coding` (542, tanpa BQ)<br>_Jika diberikan MPASI Protein hewani, sebutkan jenis proteinnya_ → `Observation.valueCodeableConcept.coding` (561, tanpa BQ) |
| 40 | 575–589 | Condition | 289084000 | Difficulty performing breastfeeding | _Gejala sakit_ → `Condition.clinicalStatus.coding` (575, tanpa BQ)<br>_Jika memiliki gejala, sebutkan_ → `Condition.category.coding` (576, tanpa BQ)<br>_Jika lainnya, sebutkan_ → `Condition.code.text` (585, tanpa BQ) |
| 41 | 590–600 | MedicationStatement | – | – | _Apakah bayi mengonsumsi obat cacing?_ → `MedicationStatement.category.coding` (590, tanpa BQ) |
| 42 | 601–620 | MedicationRequest | 92002848 | Sodium Chloride 0,52 g / Sodium Citrate Dihydrate 0,58 g / Dextrose Anhydrate 2,70 g / Potassium Chloride 0,30 g Serbuk Oral | _Apakah bayi diberikan oralit_ → `MedicationRequest.contained.resourceType` (601, tanpa BQ) |
| 43 | 621–636 | MedicationDispense | 92002848 | Sodium Chloride 0,52 g / Sodium Citrate Dihydrate 0,58 g / Dextrose Anhydrate 2,70 g / Potassium Chloride 0,30 g Serbuk Oral | – |
| 44 | 637–647 | MedicationStatement | – | – | _Apakah dalam 1 bulan terakhir bayi mengonsumsi oralit_ → `MedicationStatement.category.coding` (637, tanpa BQ) |
| 45 | 648–657 | Procedure | SP000694 | Pelayanan 2T | _Apakah bayi mendapatkan pelayanan 2T?_ → `Procedure.category.coding` (648, tanpa BQ) |
| 46 | 658–660 | Observation | 3457005 | Patient referral | _Rujuk_ → `Observation.component.code.coding` (658, tanpa BQ) |
| 47 | 662–668 | Observation | – | – | – |
| 48 | 669–683 | ServiceRequest | – | – | _Dimana fasillitas kesehatan tujuan rujukan?_ → `ServiceRequest.performer.reference` (679, tanpa BQ)<br>_Nama fasillitas kesehatan tujuan rujukan_ → `ServiceRequest.performer.display` (683, tanpa BQ) |
| 49 | 684–695 | Observation | 1144561006 | Adequate sanitation | _Apakah memiliki jamban di rumah?_ → `Observation.valueBoolean` (687, tanpa BQ) |
| 50 | 696–707 | Observation | 1162942008 | Access to potable water | _Apakah memiliki akses untuk air bersih_ → `Observation.valueBoolean` (699, tanpa BQ) |
| 51 | 710–725 | QuestionnaireResponse | https://fhir.kemkes.go.id/Questionnaire/Q0011 | – | _Apakah dilakukan Pemeriksaan Infeksi?_ → `QuestionnaireResponse.questionnaire` (710, tanpa BQ) |
| 52 | 726–798 | Observation | 1153455005 | Assessment of signs and symptoms of infection | _Jika Ya, maka tanyakan hasil pemeriksaan berikut :_ → `Observation.status` (726, tanpa BQ)<br>_Biru sekitar mulut saat bayi menangis/mengisap_ → `Observation.component.code.coding` (729, tanpa BQ)<br>_Saturasi oksigen < 95% pada tangan kanan dan kaki kiri_ → `Observation.component.code.coding` (732, tanpa BQ)<br>_Terdapat perbedaan saturasi oksigen > 3% antara tangan kanan dan kaki kiri_ → `Observation.component.code.coding` (735, tanpa BQ)<br>_Napas cepat (≥ 60 kali/menit)_ → `Observation.component.code.coding` (738, tanpa BQ)<br>_Napas lambat (< 40 kali/menit)_ → `Observation.component.code.coding` (741, tanpa BQ)<br>_Merintih_ → `Observation.component.code.coding` (744, tanpa BQ)<br>_Pernapasan cuping hidung_ → `Observation.component.code.coding` (747, tanpa BQ)<br>_Tarikan dinding dada ke dalam yang sangat kuat_ → `Observation.component.code.coding` (750, tanpa BQ)<br>_Bayi lemah, tidak kuat bergerak/mengisap_ → `Observation.component.code.coding` (753, tanpa BQ)<br>_Kejang atau gerakan spontan tidak terkendali_ → `Observation.component.code.coding` (756, tanpa BQ)<br>_Suhu tubuh > 37,5˚C_ → `Observation.component.code.coding` (759, tanpa BQ)<br>_Suhu tubuh < 36,5˚C_ → `Observation.component.code.coding` (762, tanpa BQ)<br>_Tidak buang air besar 48 jam setelah lahir_ → `Observation.component.code.coding` (765, tanpa BQ)<br>_Muntah berisi susu atau cairan berwarna hijau_ → `Observation.component.code.coding` (768, tanpa BQ)<br>_Perut kembung dan sulit bernapas_ → `Observation.component.code.coding` (771, tanpa BQ)<br>_Tidak didapatkan lubang anus, atau kotoran keluar dari lubang tidak normal di sekitar anus_ → `Observation.component.code.coding` (774, tanpa BQ)<br>_Mata bernanah_ → `Observation.component.code.coding` (777, tanpa BQ)<br>_Pusar bernanah_ → `Observation.component.code.coding` (780, tanpa BQ)<br>_Pusar kemerahan meluas sampai dinding perut > 1 cm_ → `Observation.component.code.coding` (783, tanpa BQ)<br>_Pusar kemerahan_ → `Observation.component.code.coding` (786, tanpa BQ)<br>_Pustul di kulit_ → `Observation.component.code.coding` (789, tanpa BQ) |
| 53 | 799–811 | Observation | OC000126 | Klasifikasi infeksi | _Klasifikasi Infeksi_ → `Observation.valueCodeableConcept.coding` (802, tanpa BQ) |
| 54 | 812–825 | QuestionnaireResponse | https://fhir.kemkes.go.id/Questionnaire/Q0011 | – | _Apakah dilakukan pemeriksaan Ikterus?_ → `QuestionnaireResponse.questionnaire` (812, tanpa BQ)<br>_Apakah bayi kuning?_ → `QuestionnaireResponse.item.item.linkId` (819, tanpa BQ)<br>_Jika Ya, pada umur berapa pertama kali timbul kuning? (Hari)_ → `QuestionnaireResponse.item.item.linkId` (823, tanpa BQ) |
| 55 | 826–837 | Observation | OC000129 | Klasifikasi Ikterus | _Klasifikasi Ikterus_ → `Observation.valueCodeableConcept.coding` (828, tanpa BQ) |
| 56 | 838–851 | QuestionnaireResponse | https://fhir.kemkes.go.id/Questionnaire/Q0011 | – | _Apakah dilakukan pemeriksaan diare?_ → `QuestionnaireResponse.questionnaire` (838, tanpa BQ)<br>_Apakah bayi diare?_ → `QuestionnaireResponse.item.item.linkId` (845, tanpa BQ)<br>_Hasil Pemeriksaan Diare_ → `QuestionnaireResponse.item.item. answer.item.answer.item.linkId` (849, tanpa BQ) |
| 57 | 852–863 | Observation | OC000098 | Klasifikasi Diare | _Klasifikasi Diare Pada Bayi Muda_ → `Observation.valueCodeableConcept.coding` (854, tanpa BQ) |
| 58 | 864–873 | QuestionnaireResponse | https://fhir.kemkes.go.id/Questionnaire/Q0011 | – | _Apakah dilakukan pemeriksaan HIV?_ → `QuestionnaireResponse.questionnaire` (864, tanpa BQ)<br>_Hasil Pemeriksaan HIV_ → `QuestionnaireResponse.item.item.answer.item.linkId` (871, tanpa BQ) |
| 59 | 874–886 | Observation | 254387007 | Human immunodeficiency virus infection classification systems | _Klasifikasi Infeksi HIV_ → `Observation.valueCodeableConcept.coding` (876, tanpa BQ) |
| 60 | 887–896 | QuestionnaireResponse | https://fhir.kemkes.go.id/Questionnaire/Q0011 | – | _Dilakukan Pemeriksaan Berat Badan Menurut Umur dan/atau Masalah Pemberian ASI_ → `QuestionnaireResponse.questionnaire` (887, tanpa BQ)<br>_Hasil Pemeriksaan Berat Badan Menurut Umur dan/atau Masalah Pemberian ASI_ → `QuestionnaireResponse.item.item.answer.item.linkId` (894, tanpa BQ) |
| 61 | 897–908 | Observation | OC000085 | Klasifikasi berat badan menurut umur dan/atau masalah pemberian ASI | _Klasifikasi Berat Badan Menurut Umur dan/atau Masalah Pemberian ASI_ → `Observation.valueCodeableConcept.coding` (899, tanpa BQ) |
| 62 | 909–922 | QuestionnaireResponse | https://fhir.kemkes.go.id/Questionnaire/Q0011 | – | _Ibu HIV Positif dan Tidak Menyusui_ → `QuestionnaireResponse.questionnaire` (909, tanpa BQ)<br>_Dilakukan Pemeriksaan Berat Badan Menurut Umur dan/atau Masalah Pemberian Minum_ → `QuestionnaireResponse.item.item.linkId` (916, tanpa BQ)<br>_Hasil Pemeriksaan Berat Badan Menurut Umur dan/atau Masalah Pemberian Minum_ → `QuestionnaireResponse.item.item.answer.item.linkId` (920, tanpa BQ) |
| 63 | 923–934 | Observation | OC000086 | Klasifikasi Berat Badan Menurut umur dan/atau Masalah Pemberian Minum | _Klasifikasi Berat Badan Menurut Umur dan/atau Masalah Pemberian Minum_ → `Observation.valueCodeableConcept.coding` (925, tanpa BQ) |
| 64 | 936–945 | QuestionnaireResponse | https://fhir.kemkes.go.id/Questionnaire/Q0027 | – | _Dilakukan Pemeriksaan Tanda Bahaya Umum (Status Kegawatan)_ → `QuestionnaireResponse.item.item.linkId` (939, tanpa BQ)<br>_Hasil Pemeriksaan Tanda Bahaya Umum (Status Kegawatan)_ → `QuestionnaireResponse.item.item.answer.item.linkId` (943, tanpa BQ) |
| 65 | 946–957 | Observation | OC000089 | Klasifikasi Status Kegawatan | _Klasifikasi Status Kegawatan_ → `Observation.valueCodeableConcept.coding` (948, tanpa BQ) |
| 66 | 958–971 | QuestionnaireResponse | https://fhir.kemkes.go.id/Questionnaire/Q0027 | – | _Apakah dilakukan pemeriksaan batuk dan/atau sukar bernapas?_ → `QuestionnaireResponse.item.item.linkId` (961, tanpa BQ)<br>_Anak Menderita Batuk dan/atau Sukar Bernapas_ → `QuestionnaireResponse.item.item.answer.item.linkId` (965, tanpa BQ)<br>_Hasil Pemeriksaan Batuk dan/atau Sukar Bernapas_ → `QuestionnaireResponse.item.item.answer.item.answer.item.linkId` (969, tanpa BQ) |
| 67 | 972–983 | Observation | OC000091 | Klasifikasi batuk dan/atau sukar bernapas | _Klasifikasi Batuk dan/atau Sukar Bernapas_ → `Observation.valueCodeableConcept.coding` (974, tanpa BQ) |
| 68 | 984–997 | QuestionnaireResponse | https://fhir.kemkes.go.id/Questionnaire/Q0027 | – | _Apakah dilakukan Pemeriksaan Diare?_ → `QuestionnaireResponse.item.item.linkId` (987, tanpa BQ)<br>_Apakah anak diare?_ → `QuestionnaireResponse.item.item.answer.item.linkId` (991, tanpa BQ)<br>_Hasil pemeriksaan diare_ → `QuestionnaireResponse.item.item.answer.item.answer.item.linkId` (995, tanpa BQ) |
| 69 | 998–1013 | Observation | OC000098 | Klasifikasi Diare | _Klasifikasi Diare_ → `Observation.valueCodeableConcept.coding` (1000, tanpa BQ) |
| 70 | 1014–1031 | QuestionnaireResponse | https://fhir.kemkes.go.id/Questionnaire/Q0027 | – | _Apakah dilakukan pemeriksaan demam?_ → `QuestionnaireResponse.questionnaire` (1014, tanpa BQ)<br>_Apakah anak demam?_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1021, tanpa BQ)<br>_Apakah dilakukan Pemeriksaan Malaria?_ → `QuestionnaireResponse.item.item.answer.item.answer.item.linkId` (1025, tanpa BQ)<br>_Hasil Pemeriksaan Demam dan Malaria_ → `QuestionnaireResponse.item.item.answer.item.answer.item.linkId` (1029, tanpa BQ) |
| 71 | 1032–1045 | Observation | OC000100 | Klasifikasi Demam | _Klasifikasi Demam_ → `Observation.valueCodeableConcept.coding` (1034, tanpa BQ) |
| 72 | 1046–1059 | QuestionnaireResponse | https://fhir.kemkes.go.id/Questionnaire/Q0027 | – | _Dilakukan Pemeriksaan Campak_ → `QuestionnaireResponse.item.item.linkId` (1049, tanpa BQ)<br>_Anak Campak Saat Ini_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1053, tanpa BQ)<br>_Hasil Pemeriksaan Campak_ → `QuestionnaireResponse.item.item.answer.item.answer.item.linkId` (1057, tanpa BQ) |
| 73 | 1060–1073 | Observation | OC000102 | Klasifikasi campak | _Klasifikasi Campak_ → `Observation.valueCodeableConcept.coding` (1062, tanpa BQ) |
| 74 | 1074–1083 | QuestionnaireResponse | https://fhir.kemkes.go.id/Questionnaire/Q0027 | – | _Apakah dilakukan Pemeriksaan Infeksi Dengue?_ → `QuestionnaireResponse.questionnaire` (1074, tanpa BQ)<br>_Hasil Pemeriksaan Infeksi Dengue_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1081, tanpa BQ) |
| 75 | 1084–1096 | Observation | OC000105 | Klasifikasi infeksi dengue | _Klasifikasi Infeksi Dengue_ → `Observation.valueCodeableConcept.coding` (1086, tanpa BQ) |
| 76 | 1097–1106 | QuestionnaireResponse | https://fhir.kemkes.go.id/Questionnaire/Q0027 | – | _Apakah dilakukan pemeriksaan masalah telinga?_ → `QuestionnaireResponse.item.item.linkId` (1100, tanpa BQ)<br>_Hasil Pemeriksaan Masalah Telinga_ → `QuestionnaireResponse.item.item.linkId` (1104, tanpa BQ) |
| 77 | 1107–1119 | Observation | OC000107 | Klasifikasi masalah telinga | _Klasifikasi Masalah Telinga_ → `Observation.valueCodeableConcept.coding` (1109, tanpa BQ) |
| 78 | 1120–1129 | QuestionnaireResponse | https://fhir.kemkes.go.id/Questionnaire/Q0027 | – | _Apakah dilakukan Pemeriksaan Status Gizi?_ → `QuestionnaireResponse.item.item.linkId` (1123, tanpa BQ)<br>_Hasil Pemeriksaan Status Gizi_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1127, tanpa BQ) |
| 79 | 1130–1145 | Observation | OC000108 | Klasifikasi status gizi | _Klasifikasi Status Gizi_ → `Observation.valueCodeableConcept.coding` (1132, tanpa BQ) |
| 80 | 1146–1159 | QuestionnaireResponse | https://fhir.kemkes.go.id/Questionnaire/Q0027 | – | _Apakah dilakukan Pemeriksaan Status Pertumbuhan?_ → `QuestionnaireResponse.item.item.linkId` (1149, tanpa BQ)<br>_Apakah anak berumur < 2 tahun?_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1153, tanpa BQ)<br>_Hasil Pemeriksaan Status Pertumbuhan_ → `QuestionnaireResponse.item.item. answer.item.linkId` (1157, tanpa BQ) |
| 81 | 1160–1187 | Observation | 1153590000 | Length for age z-score | _Pemeriksaan Status Pertumbuhan (PB/U atau TB/U)_ → `Observation.valueQuantity.value` (1164, tanpa BQ) |
| 82 | 1188–1190 | QuestionnaireResponse | – | – | _Hasil Pemeriksaan Lingkar Kepala Menurut Umur_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1188, tanpa BQ) |
| 83 | 1191–1213 | Observation | 1153594009 | Head circumference for age z-score | _Pemeriksaan Lingkar Kepala Menurut Umur (LK/U)_ → `Observation.valueQuantity.value` (1194, tanpa BQ) |
| 84 | 1214–1223 | QuestionnaireResponse | https://fhir.kemkes.go.id/Questionnaire/Q0027 | – | _Apakah dilakukan Pemeriksaan Anemia?_ → `QuestionnaireResponse.questionnaire` (1214, tanpa BQ)<br>_Hasil Pemeriksaan Anemia_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1221, tanpa BQ) |
| 85 | 1224–1235 | Observation | OC000111 | Klasifikasi anemia | _Klasifikasi Anemia_ → `Observation.valueCodeableConcept.coding` (1226, tanpa BQ) |
| 86 | 1236–1245 | QuestionnaireResponse | https://fhir.kemkes.go.id/Questionnaire/Q0027 | – | _Apakah dilakukan Pemeriksaan HIV?_ → `QuestionnaireResponse.questionnaire` (1236, tanpa BQ)<br>_Hasil Pemeriksaan HIV_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1243, tanpa BQ) |
| 87 | 1246–1258 | Observation | 254387007 | Human immunodeficiency virus infection classification systems | _Klasifikasi Infeksi HIV_ → `Observation.valueCodeableConcept.coding` (1248, tanpa BQ) |
| 88 | 1259–1268 | Procedure | 400984005 | Congenital hypothyroidism screening test | _Apakah dilakukan SHK_ → `Procedure.category.coding` (1259, tanpa BQ) |
| 89 | 1269–1280 | Observation | 29575-8 | Thyrotropin [Units/volume] in DBS | _Jika Ya, hasil pemeriksaan terakhir dari laboratorium_ → `Observation.valueQuantity.value` (1272, tanpa BQ) |
| 90 | 1281–1306 | QuestionnaireResponse | https://fhir.kemkes.go.id/sp/Questionnaire/Q00016 | – | _Batuk terus menerus_ → `QuestionnaireResponse.item.linkId` (1291, tanpa BQ)<br>_Demam lebih dari ≥ 2 minggu_ → `QuestionnaireResponse.item.text` (1296, tanpa BQ)<br>_BB tidak naik atau turun dalam 2 bulan berturut-turut_ → `QuestionnaireResponse.item.text` (1300, tanpa BQ)<br>_Kontak erat dengan Pasien TBC_ → `QuestionnaireResponse.item.text` (1304, tanpa BQ) |
| 91 | 1307–1319 | Observation | 171126009 | Tuberculosis screening | _Interpretasi hasil skrining TBC_ → `Observation.valueQuantity.value` (1307, tanpa BQ) |
| 92 | 1324–1371 | QuestionnaireResponse | https://fhir.kemkes.go.id/sp/Questionnaire/Q00025 | – | _Pada saat bayi terlentang, apakah masing-masing lengan dan tungkai bergerak dengan mudah? Jawab ‘Tidak’ bila salah satu atau kedua tungkai atau lengan bayi bergerak tak terarah atau tak terkendali_ → `QuestionnaireResponse.item.linkId` (1332, tanpa BQ)<br>_Jangan membuat suara apapun. Pada saat bayi terlentang apakah ia melihat dan menatap wajah Anda_ → `QuestionnaireResponse.item.linkId` (1336, tanpa BQ)<br>_Pada saat Anda mengajak bayi berbicara dan tersenyum, apakah ia tersenyum kembali kepada Anda?_ → `QuestionnaireResponse.item.linkId` (1340, tanpa BQ)<br>_Apakah bayi dapat mengeluarkan suara-suara lain (mengoceh) selain menangis?_ → `QuestionnaireResponse.item.linkId` (1344, tanpa BQ)<br>_Apakah bayi suka tertawa keras walau tidak digelitik atau diraba-raba?_ → `QuestionnaireResponse.item.linkId` (1348, tanpa BQ)<br>_Ambil gulungan wool merah, lalu letakkan di atas wajah di depan mata bayi. Gerakkan wool dari samping kiri ke kanan kepala atau sebaliknya. Apakah ia dapat mengikuti gerakan Anda dengan menggerakkan kepalanya dari kanan atau kiri ke tengah?_ → `QuestionnaireResponse.item.linkId` (1352, tanpa BQ)<br>_Ambil gulungan wool merah, lalu letakkan di atas wajah di depan mata bayi. Gerakkan wool dari samping kiri ke kanan kepala atau sebaliknya. Apakah ia dapat mengikuti gerakan Anda dengan menggerakkan kepalanya dari satu sisi hampir sampai pada sisi yang lain?_ → `QuestionnaireResponse.item.linkId` (1356, tanpa BQ)<br>_Pada saat bayi tengkurap di alas yang datar, apakah ia dapat mengangkat kepalanya seperti pada gambar?_ → `QuestionnaireResponse.item.linkId` (1360, tanpa BQ)<br>_Pada saat bayi tengkurap di alas yang datar, apakah ia dapat mengangkat kepalanya sehingga membentuk sudut 45 ̊ seperti pada gambar?_ → `QuestionnaireResponse.item.linkId` (1364, tanpa BQ)<br>_Pada saat bayi tengkurap di alas yang datar, apakah ia dapat mengangkat kepalanya dengan tegak seperti pada gambar?_ → `QuestionnaireResponse.item.linkId` (1368, tanpa BQ) |
| 93 | 1373–1420 | QuestionnaireResponse | https://fhir.kemkes.go.id/sp/Questionnaire/Q00026 | – | _Bayi diposisikan terlentang. Ambil gulungan wool merah, letakkan di atas wajah di depan mata bayi. Gerakkan wool dari samping kiri ke kanan kepala. Apakah ia dapat mengikuti gerakan Anda dengan menggerakkan kepala sepenuhnya dari satu ke sisi yang lain?_ → `QuestionnaireResponse.item.linkId` (1381, tanpa BQ)<br>_Pada posisi bayi terlentang, pegang kedua tangannya lalu tarik perlahan ke posisi duduk. Dapatkah bayi mempertahankan lehernya secara kaku seperti pada gambar? Jawab ‘Tidak’ bila kepala bayi jatuh kembali seperti gambar_ → `QuestionnaireResponse.item.linkId` (1385, tanpa BQ)<br>_Ketika bayi tengkurap di alas yang datar, apakah ia dapat mengangkat dada dengan kedua lengannya sebagai penyangga seperti pada gambar?_ → `QuestionnaireResponse.item.linkId` (1389, tanpa BQ)<br>_Bayi dipangku orang tua atau pengasuh. Dapatkah bayi mempertahankan posisi kepala dalam keadaan tegak dan stabil? Jawab ‘Tidak’ bila kepala bayi cenderung jatuh ke kanan, kiri, atau ke dadanya_ → `QuestionnaireResponse.item.linkId` (1393, tanpa BQ)<br>_Bayi dipangku orang tua atau pengasuh. Sentuhkan pensil di punggung tangan atau ujung jari bayi (jangan meletakkan di atas telapak tangan bayi). Apakah bayi dapat menggenggam pensil itu selama beberapa detik?_ → `QuestionnaireResponse.item.linkId` (1397, tanpa BQ)<br>_Bayi dipangku orang tua atau pengasuh. Dapatkah bayi mengarahkan matanya pada benda kecil sebesar kacang, kismis atau uang logam? Jawab ‘Tidak’ jika ia tidak dapat mengarahkan matanya_ → `QuestionnaireResponse.item.linkId` (1401, tanpa BQ)<br>_Bayi dipangku orang tua atau pengasuh. Dapatkah bayi meraih mainan yang diletakkan agak jauh namun masih berada dalam jangkauan tangannya?_ → `QuestionnaireResponse.item.linkId` (1405, tanpa BQ)<br>_Tanyakan kepada orang tua atau pengasuh, pernahkah bayi berbalik paling sedikit 2 kali, dari terlentang ke tengkurap atau sebaliknya?_ → `QuestionnaireResponse.item.linkId` (1409, tanpa BQ)<br>_Tanyakan kepada orang tua atau pengasuh, pernahkah bayi mengeluarkan suara gembira bernada tinggi atau memekik tetapi bukan menangis?_ → `QuestionnaireResponse.item.linkId` (1413, tanpa BQ)<br>_Tanyakan kepada orang tua atau pengasuh, pernahkah orang tua atau pengasuh melihat bayi tersenyum ketika melihat mainan yang lucu, gambar, atau binatang peliharaan pada saat ia bermain sendiri?_ → `QuestionnaireResponse.item.linkId` (1417, tanpa BQ) |
| 94 | 1422–1469 | QuestionnaireResponse | https://fhir.kemkes.go.id/sp/Questionnaire/Q00027 | – | _Bayi dipangku orang tua atau pengasuh, Taruh kismis di atas meja. Dapatkah bayi memungut dengan tangannya benda−benda kecil seperti kismis, kacang-kacangan, potongan biskuit dengan gerakan miring atau menggerapai seperti gambar?_ → `QuestionnaireResponse.item.linkId` (1430, tanpa BQ)<br>_Bayi dipangku orang tua atau pengasuh. Taruh 2 kubus di atas meja, buat agar bayi dapat memungut dan memegang kubus pada masing-masing tangannya. Dapatkah ia melakukannya?_ → `QuestionnaireResponse.item.linkId` (1434, tanpa BQ)<br>_Bayi dipangku orang tua atau pengasuh. Tarik perhatian bayi dengan memperlihatkan gulungan wool merah, kemudian jatuhkan ke lantai. Apakah bayi mencoba mencari benda tersebut, misalnya mencari di bawah meja atau di belakang kursi?_ → `QuestionnaireResponse.item.linkId` (1438, tanpa BQ)<br>_Bayi dipangku orang tua atau pengasuh. Letakkan suatu mainan yang diinginkan bayi di luar jangkauannya, apakah ia mencoba mendapatkan mainan dengan mengulurkan lengan atau badannya?_ → `QuestionnaireResponse.item.linkId` (1442, tanpa BQ)<br>_Tanyakan kepada orang tua atau pengasuh, apakah bayi menengok ke belakang seperti mendengar kedatangan seseorang pada saat bayi sedang bermain sendiri dan seseorang diam-diam datang berdiri di belakangnya? Suara keras tidak ikut dihitung. Jawab ‘Ya’ hanya jika melihat reaksinya terhadap suara yang perlahan atau bisikan_ → `QuestionnaireResponse.item.linkId` (1446, tanpa BQ)<br>_Tanyakan kepada orang tua atau pengasuh, apakah anak dapat mengatakan 2 suku kata yang sama, misalnya: “Ma-ma”, “Da-da” atau “Pa-pa”? Jawab ‘Ya’ bila ia dapat mengeluarkan salah satu suara tersebut_ → `QuestionnaireResponse.item.linkId` (1450, tanpa BQ)<br>_Tanyakan kepada orang tua atau pengasuh, apakah bayi dapat makan kue kering sendiri?_ → `QuestionnaireResponse.item.linkId` (1454, tanpa BQ)<br>_Tanyakan kepada orang tua atau pengasuh apakah pernah melihat bayi memindahkan mainan atau kue kering dari satu tangan ke tangan yang lain? Benda−benda panjang seperti sendok atau kerincingan bertangkai tidak ikut dinilai_ → `QuestionnaireResponse.item.linkId` (1458, tanpa BQ)<br>_Tanpa disangga oleh bantal, kursi atau dinding, dapatkah bayi duduk sendiri selama 60 detik?_ → `QuestionnaireResponse.item.linkId` (1462, tanpa BQ)<br>_Jika Anda mengangkat bayi melalui ketiaknya ke posisi berdiri, dapatkah ia menyangga sebagian berat badan dengan kedua kakinya? Jawab ‘Ya’ bila ia mencoba berdiri dan sebagian berat badan tertumpu pada kedua kakinya_ → `QuestionnaireResponse.item.linkId` (1466, tanpa BQ) |
| 95 | 1470–1482 | Observation | 1280010004 | Screening for child developmental disorder | _Interpretasi hasil SDIDTK_ → `Observation.valueCodeableConcept.coding` (1473, tanpa BQ) |
| 96 | 1485–1520 | QuestionnaireResponse | https://fhir.kemkes.go.id/sp/Questionnaire/Q00041 | – | _Apakah bayi dapat mengatakan Aaaa atau Oooo_ → `QuestionnaireResponse.item.linkId` (1493, tanpa BQ)<br>_Apakah bayi menatap wajah dan tampak mendengerkan Anda, lalu berbicara saat Anda diam?_ → `QuestionnaireResponse.item.linkId` (1497, tanpa BQ)<br>_Apakah Anda dapat seolah-olah berbicara dengan bayi Anda?_ → `QuestionnaireResponse.item.linkId` (1501, tanpa BQ)<br>_Apakah bayi kaget bila mendengar suara (mengejapkan mata, napas lebih cepat)?_ → `QuestionnaireResponse.item.linkId` (1505, tanpa BQ)<br>_Apakah bayi kelihatan menoleh bila Anda berbicara di sebelahnya?_ → `QuestionnaireResponse.item.linkId` (1509, tanpa BQ)<br>_Apakah bayi Anda dapat tersenyum?_ → `QuestionnaireResponse.item.linkId` (1513, tanpa BQ)<br>_Apakah bayi Anda kendal dengan Anda, seperti tersenyum lebih cepat pada Anda dibandingkan orang lain?_ → `QuestionnaireResponse.item.linkId` (1517, tanpa BQ) |
| 97 | 1522–1586 | QuestionnaireResponse | https://fhir.kemkes.go.id/sp/Questionnaire/Q00042 | – | _Apakah bayi Anda dapat tertawa keras?_ → `QuestionnaireResponse.item.linkId` (1530, tanpa BQ)<br>_Apakah bayi dapat bermain menggelembungkan mulut seperti meniup balon?_ → `QuestionnaireResponse.item.linkId` (1534, tanpa BQ)<br>_Apakah bayi memberi respons tertentu, seperti menjadi lebih riang bila Anda datang?_ → `QuestionnaireResponse.item.linkId` (1538, tanpa BQ)<br>_Pemeriksa duduk menghadap bayi yang dipangku orangtuanya, bunyikan bel disamping tanpa terlihat bayi, apakah bayi menoleh ke samping?_ → `QuestionnaireResponse.item.linkId` (1542, tanpa BQ)<br>_Pemeriksa menatap bayi sekitar 45 cm, lalu gunakan mainan untuk menarik pandangan bayi ke kiri, kanan, atas, dan bawah, apakah bayi dapat mengikutinya?_ → `QuestionnaireResponse.item.linkId` (1546, tanpa BQ)<br>_Apakah bayi berkedip bila pemeriksa melakukan gerakan menusuk mata, lalu berhenti sekitar 3 cm tanpa menyentuh mata?_ → `QuestionnaireResponse.item.linkId` (1550, tanpa BQ)<br>_Apakah bayi dapat membuat suara berulang seperti "mamama", "bababa"?_ → `QuestionnaireResponse.item.linkId` (1563, tanpa BQ)<br>_Apakah bayi dapat memanggil mama atau papa, walaupun tidak untuk memanggil orang tuanya?_ → `QuestionnaireResponse.item.linkId` (1567, tanpa BQ)<br>_Pemeriksa duduk menghadap bayi yang dipangku orang tuanya, bunyikan bel disampiing bawah tanpa terlihat bayi, apakah bayi langsung menoleh ke samping bawah?_ → `QuestionnaireResponse.item.linkId` (1571, tanpa BQ)<br>_Apakah anak mengikuti perintah tanpa dibantu gerakan badan, seperti "Stop, berikan mainanmu?"_ → `QuestionnaireResponse.item.linkId` (1575, tanpa BQ)<br>_Apakah bayi mengikuti perintah dengan dibantu gerakan badan, seperti "Stop, berikan mainanmu"?_ → `QuestionnaireResponse.item.linkId` (1579, tanpa BQ)<br>_Apakah bayi secara spontan memulai permainan dengan gerakan tubuh, seperti "Pok Ame-Ame" atau Cilukba?_ → `QuestionnaireResponse.item.linkId` (1583, tanpa BQ) |
| 98 | 1587–1598 | Observation | 252957005 | Children's hearing test | _Interpretasi Tes Daya Dengar_ → `Observation.valueCodeableConcept.coding` (1590, tanpa BQ) |
| 99 | 1606–1620 | Observation | 252963001 | Children's vision test | _Hasil Tes Daya Lihat_ → `Observation.valueCodeableConcept.coding` (1609, tanpa BQ)<br>_Dilakukan rujukan_ → `Observation.component.code.coding` (1618, tanpa BQ) |
| 100 | 1622–1628 | Observation | – | – | – |
| 101 | 1630–1646 | Procedure | 410314003 | Health promotion education, guidance, and counseling | _Apakah dilakukan konseling_ → `Procedure.category.coding` (1630, tanpa BQ)<br>_Sebutkan topik konseling yang dilakukan_ → `Procedure.code.coding.code` (1634, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 61 |
| QuestionnaireResponse | 24 |
| Procedure | 7 |
| Condition | 3 |
| MedicationStatement | 2 |
| Encounter | 1 |
| MedicationRequest | 1 |
| MedicationDispense | 1 |
| ServiceRequest | 1 |
| **Total** | **101** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 17 | Condition | `Condition.code.coding` | Z00.1 | Routine child health examination | http://hl7.org/fhir/sid/icd-10 |
| 2 | 34 | Observation | `Observation.code.coding` | SP000699 | Kelompok Dasawisma | http://terminology.kemkes.go.id/sp |
| 3 | 45 | Observation | `Observation.code.coding` | SP000132 | Memiliki Buku KIA | http://terminology.kemkes.go.id/sp |
| 4 | 57 | Observation | `Observation.code.coding` | 76516-4 | Gestational age—​at birth | http://loinc.org |
| 5 | 68 | Procedure | `Procedure.code.coding` | 431868002 | Initiation of breastfeeding | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 6 | 79 | Observation | `Observation.code.coding` | OC000016 | Waktu Inisiasi Menyusui Dini | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 7 | 80 | Observation | `Observation.valueCodeableConcept.coding` | OV000014 | Kurang dari 1 jam | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 8 | 81 | Observation | `Observation.valueCodeableConcept.coding` | OV000015 | Lebih dari 1 jam | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 9 | 91 | Observation | `Observation.code.coding` | 89269-5 | Body height Measured --at birth | http://loinc.org |
| 10 | 103 | Observation | `Observation.code.coding` | 8339-4 | Birth weight Measured | http://loinc.org |
| 11 | 106 | Observation | `Observation.interpretation.coding` | 276613009 | High birth weight | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 12 | 107 | Observation | `Observation.interpretation.coding` | 276712009 | Normal birth weight | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 13 | 108 | Observation | `Observation.interpretation.coding` | 276610007 | Low birth weight infant | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 14 | 109 | Observation | `Observation.interpretation.coding` | 276611006 | Very low birth weight infant | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 15 | 110 | Observation | `Observation.interpretation.coding` | 276612004 | Extremely low birth weight | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 16 | 120 | Observation | `Observation.code.coding` | 8290-9 | Head Occipital-frontal circumference --at birth- by Tape measure | http://loinc.org |
| 17 | 132 | Observation | `Observation.code.coding` | 284473002 | Mid upper arm circumference | http://snomed.info/sct |
| 18 | 135 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 19 | 136 | Observation | `Observation.interpretation.coding` | 248325000 | Undernourished | http://snomed.info/sct |
| 20 | 137 | Observation | `Observation.interpretation.coding` | OI000001 | Gizi Buruk | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 21 | 147 | Observation | `Observation.code.coding` | 8306-3 | Body height --lying | http://loinc.org |
| 22 | 159 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 23 | 179 | Observation | `Observation.code.coding` | 816159004 | Measured weight gain | http://snomed.info/sct |
| 24 | 189 | Observation | `Observation.valueCodeableConcept.coding` | 262286000 | Weight increased | http://snomed.info/sct |
| 25 | 190 | Observation | `Observation.valueCodeableConcept.coding` | 36440009 | Failure to gain weight | http://snomed.info/sct |
| 26 | 200 | Observation | `Observation.code.coding` | 1153598007 | Weight for length z score | http://snomed.info/sct |
| 27 | 203 | Observation | `Observation.interpretation.coding` | OI000011 | Gizi Buruk | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 28 | 205 | Observation | `Observation.interpretation.coding` | 248325000 | Undernourished | http://snomed.info/sct |
| 29 | 208 | Observation | `Observation.interpretation.coding` | 248324001 | Well nourished | http://snomed.info/sct |
| 30 | 211 | Observation | `Observation.interpretation.coding` | OI000004 | Risiko Gizi Lebih | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 31 | 214 | Observation | `Observation.interpretation.coding` | 238131007 | Overweight | http://snomed.info/sct |
| 32 | 217 | Observation | `Observation.interpretation.coding` | 414915002 | Obese | http://snomed.info/sct |
| 33 | 228 | Observation | `Observation.code.coding` | 1153593003 | Weight for age z-score | http://snomed.info/sct |
| 34 | 250 | Observation | `Observation.code.coding` | 1153590000 | Length for age z-score | http://snomed.info/sct |
| 35 | 277 | Observation | `Observation.code.coding` | 8287-5 | Head Occipital-frontal circumference by Tape measure | http://loinc.org |
| 36 | 289 | Observation | `Observation.code.coding` | 1153594009 | Head circumference for age z-score | http://loinc.org |
| 37 | 292 | Observation | `Observation.interpretation.coding` | 840673007 | Normal head | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 38 | 297 | Observation | `Observation.interpretation.coding` | 1148757008 | Microcephaly | http://snomed.info/sct |
| 39 | 300 | Observation | `Observation.interpretation.coding` | 1145403003 | Macrocephaly | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 40 | 312 | Observation | `Observation.code.coding` | 8867-4 | Heart rate | http://loinc.org |
| 41 | 324 | Observation | `Observation.code.coding` | 8310-5 | Body temperature | http://loinc.org |
| 42 | 336 | Observation | `Observation.code.coding` | 9279-1 | Respiratory rate | http://loinc.org |
| 43 | 348 | Observation | `Observation.code.coding` | 10206-1 | Physical findings of Skin Narrative | http://loinc.org |
| 44 | 349 | Observation | `Observation.valueCodeableConcept.coding` | 17621005 | Normal | http://snomed.info/sct |
| 45 | 350 | Observation | `Observation.valueCodeableConcept.coding` | 263654008 | Abnormal | http://snomed.info/sct |
| 46 | 360 | Observation | `Observation.code.coding` | 10199-8 | Physical findings of Head Narrative | http://loinc.org |
| 47 | 361 | Observation | `Observation.valueCodeableConcept.coding` | 17621005 | Normal | http://snomed.info/sct |
| 48 | 362 | Observation | `Observation.valueCodeableConcept.coding` | 263654008 | Abnormal | http://snomed.info/sct |
| 49 | 372 | Observation | `Observation.code.coding` | 10197-2 | Physical findings of Eye Narrative | http://loinc.org |
| 50 | 373 | Observation | `Observation.valueCodeableConcept.coding` | 17621005 | Normal | http://snomed.info/sct |
| 51 | 374 | Observation | `Observation.valueCodeableConcept.coding` | 263654008 | Abnormal | http://snomed.info/sct |
| 52 | 384 | Observation | `Observation.code.coding` | 32453-3 | Physical findings of Mouth | http://loinc.org |
| 53 | 385 | Observation | `Observation.valueCodeableConcept.coding` | 17621005 | Normal | http://snomed.info/sct |
| 54 | 386 | Observation | `Observation.valueCodeableConcept.coding` | 263654008 | Abnormal | http://snomed.info/sct |
| 55 | 396 | Observation | `Observation.code.coding` | 32453-3 | Physical findings of Abdomen Narrative | http://loinc.org |
| 56 | 397 | Observation | `Observation.valueCodeableConcept.coding` | 17621005 | Normal | http://snomed.info/sct |
| 57 | 398 | Observation | `Observation.valueCodeableConcept.coding` | 263654008 | Abnormal | http://snomed.info/sct |
| 58 | 408 | Observation | `Observation.code.coding` | 10192-3 | Physical findings of Back Narrative | http://loinc.org |
| 59 | 409 | Observation | `Observation.valueCodeableConcept.coding` | 17621005 | Normal | http://snomed.info/sct |
| 60 | 410 | Observation | `Observation.valueCodeableConcept.coding` | 263654008 | Abnormal | http://snomed.info/sct |
| 61 | 420 | Observation | `Observation.code.coding` | 53505006 | Anal structure (body structure) | http://snomed.info/sct |
| 62 | 421 | Observation | `Observation.valueCodeableConcept.coding` | 17621005 | Normal | http://snomed.info/sct |
| 63 | 422 | Observation | `Observation.valueCodeableConcept.coding` | 263654008 | Abnormal | http://snomed.info/sct |
| 64 | 432 | Observation | `Observation.code.coding` | 11400-9 | Physical findings of Genitalia Narrative | http://loinc.org |
| 65 | 433 | Observation | `Observation.valueCodeableConcept.coding` | 17621005 | Normal | http://snomed.info/sct |
| 66 | 434 | Observation | `Observation.valueCodeableConcept.coding` | 263654008 | Abnormal | http://snomed.info/sct |
| 67 | 445 | Condition | `Condition.code.coding` | 160357008 | Family history: Hypertension | http://snomed.info/sct |
| 68 | 446 | Condition | `Condition.code.coding` | 160303001 | Family history of diabetes mellitus | http://snomed.info/sct |
| 69 | 447 | Condition | `Condition.code.coding` | 275104002 | Family history of stroke | http://snomed.info/sct |
| 70 | 448 | Condition | `Condition.code.coding` | 429959009 | Family history of heart failure | http://snomed.info/sct |
| 71 | 449 | Condition | `Condition.code.coding` | 160377001 | Family history: Asthma | http://snomed.info/sct |
| 72 | 450 | Condition | `Condition.code.coding` | 275937001 | Family history of malignant neoplasm (situation) | http://snomed.info/sct |
| 73 | 451 | Condition | `Condition.code.coding` | 160314003 | Family history: Hypercholesterolemia | http://snomed.info/sct |
| 74 | 452 | Condition | `Condition.code.coding` | 160324006 | Family history of mental disorder | http://snomed.info/sct |
| 75 | 453 | Condition | `Condition.code.coding` | 160266009 | No family history of clinical finding | http://snomed.info/sct |
| 76 | 460 | Observation | `Observation.code.coding` | 1145307003 | Exclusively breastfed | http://snomed.info/sct |
| 77 | 472 | Observation | `Observation.code.coding` | 61432-1 | How old was sample person when he or she was first fed something other than breast milk or water [PhenX] | http://loinc.org |
| 78 | 484 | Observation | `Observation.code.coding` | 413711008 | Breastfeeding (infant) | http://snomed.info/sct |
| 79 | 495 | Procedure | `Procedure.code.coding` | 767224000 | Administration of vitamin A | http://snomed.info/sct |
| 80 | 505 | Procedure | `Procedure.code.coding` | SP000693 | Pelayanan Bawah Garis Merah | http://terminology.kemkes.go.id/sp |
| 81 | 515 | Procedure | `Procedure.code.coding` | SP000695 | PMT Pemulihan | http://terminology.kemkes.go.id/sp |
| 82 | 526 | Observation | `Observation.code.coding` | SP000036 | Jenis PMT | http://terminology.kemkes.go.id/sp |
| 83 | 527 | Observation | `Observation.valueCodeableConcept.coding` | SP000493 | Makanan Lengkap | http://terminology.kemkes.go.id/sp |
| 84 | 528 | Observation | `Observation.valueCodeableConcept.coding` | 228070005 | Snack food | http://snomed.info/sct |
| 85 | 529 | Observation | `Observation.valueCodeableConcept.coding` | SP000494 | Makanan Lengkap dan Makanan Kudapan | http://terminology.kemkes.go.id/sp |
| 86 | 539 | Observation | `Observation.code.coding` | OC000009 | Makanan Pendamping ASI (MPASI) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 87 | 542 | Observation | `Observation.component.code.coding` | QRI000005 | Sereal, akar dan umbi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 88 | 545 | Observation | `Observation.component.code.coding` | 13577000 | Nut | http://snomed.info/sct |
| 89 | 548 | Observation | `Observation.component.code.coding` | QRI000007 | Susu dan produk olahannya | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 90 | 551 | Observation | `Observation.component.code.coding` | 102263004 | Eggs | http://snomed.info/sct |
| 91 | 554 | Observation | `Observation.component.code.coding` | QRI000010 | Buah dan sayur sumber vitamin A | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 92 | 557 | Observation | `Observation.component.code.coding` | QRI000011 | Buah dan sayur lainnya | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 93 | 560 | Observation | `Observation.component.code.coding` | QRI000008 | Daging dan/atau ikan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 94 | 561 | Observation | `Observation.valueCodeableConcept.coding` | 226915003 | Red meat | http://snomed.info/sct |
| 95 | 562 | Observation | `Observation.valueCodeableConcept.coding` | 226955001 | Chicken - meat | http://snomed.info/sct |
| 96 | 563 | Observation | `Observation.valueCodeableConcept.coding` | 278840001 | Shrimp | http://snomed.info/sct |
| 97 | 564 | Observation | `Observation.valueCodeableConcept.coding` | 735006003 | Squid | http://snomed.info/sct |
| 98 | 565 | Observation | `Observation.valueCodeableConcept.coding` | 90580008 | Fish | http://snomed.info/sct |
| 99 | 566 | Observation | `Observation.valueCodeableConcept.coding` | 102263004 | Eggs | http://snomed.info/sct |
| 100 | 567 | Observation | `Observation.valueCodeableConcept.coding` | 226983004 | Heart - meat | http://snomed.info/sct |
| 101 | 577 | Condition | `Condition.code.coding` | 289084000 | Difficulty performing breastfeeding | http://snomed.info/sct |
| 102 | 578 | Condition | `Condition.code.coding` | 289081008 | Unable to perform breastfeeding | http://snomed.info/sct |
| 103 | 579 | Condition | `Condition.code.coding` | 422400008 | Vomiting | http://snomed.info/sct |
| 104 | 580 | Condition | `Condition.code.coding` | 386661006 | Fever | http://snomed.info/sct |
| 105 | 581 | Condition | `Condition.code.coding` | 62315008 | Diarrhea | http://snomed.info/sct |
| 106 | 582 | Condition | `Condition.code.coding` | 18165001 | Jaundice | http://snomed.info/sct |
| 107 | 583 | Condition | `Condition.code.coding` | 62085005 | Grunting respiration | http://snomed.info/sct |
| 108 | 584 | Condition | `Condition.code.coding` | 249222005 | Neonatal condition | http://snomed.info/sct |
| 109 | 604 | MedicationRequest | `MedicationRequest.contained.code.coding` | 92002848 | Sodium Chloride 0,52 g / Sodium Citrate Dihydrate 0,58 g / Dextrose Anhydrate 2,70 g / Potassium Chloride 0,30 g Serbuk Oral | http://sys-ids.kemkes.go.id/kfa |
| 110 | 624 | MedicationDispense | `MedicationDispense.contained.code.coding` | 92002848 | Sodium Chloride 0,52 g / Sodium Citrate Dihydrate 0,58 g / Dextrose Anhydrate 2,70 g / Potassium Chloride 0,30 g Serbuk Oral | http://sys-ids.kemkes.go.id/kfa |
| 111 | 649 | Procedure | `Procedure.code.coding` | SP000694 | Pelayanan 2T | http://terminology.kemkes.go.id/sp |
| 112 | 658 | Observation | `Observation.component.code.coding` | 3457005 | Patient referral | http://snomed.info/sct |
| 113 | 673 | ServiceRequest | `ServiceRequest.code` | 737492002 | Outpatient care management | http://snomed.info/sct |
| 114 | 674 | ServiceRequest | `ServiceRequest.reasonCode.coding` | 306227000 | Referral for mental health counseling | http://snomed.info/sct |
| 115 | 686 | Observation | `Observation.code.coding` | 1144561006 | Adequate sanitation | http://snomed.info/sct |
| 116 | 698 | Observation | `Observation.code.coding` | 1162942008 | Access to potable water | http://snomed.info/sct |
| 117 | 728 | Observation | `Observation.code.coding` | 1153455005 | Assessment of signs and symptoms of infection | http://snomed.info/sct |
| 118 | 729 | Observation | `Observation.component.code.coding` | SP000921 | Biru sekitar mulut saat bayi menangis/mengisap | http://terminology.kemkes.go.id/sp |
| 119 | 732 | Observation | `Observation.component.code.coding` | SP000922 | Saturasi oksigen < 95% pada tangan kanan dan kaki kiri | http://terminology.kemkes.go.id/sp |
| 120 | 735 | Observation | `Observation.component.code.coding` | SP000923 | Terdapat perbedaan saturasi oksigen > 3% antara tangan kanan dan kaki kiri | http://terminology.kemkes.go.id/sp |
| 121 | 738 | Observation | `Observation.component.code.coding` | 271823003 | Tachypnea | http://snomed.info/sct |
| 122 | 741 | Observation | `Observation.component.code.coding` | 86684002 | Slow respiration | http://snomed.info/sct |
| 123 | 744 | Observation | `Observation.component.code.coding` | 62085005 | Grunting respiration | http://snomed.info/sct |
| 124 | 747 | Observation | `Observation.component.code.coding` | 21558008 | Flaring of alae nasi | http://snomed.info/sct |
| 125 | 750 | Observation | `Observation.component.code.coding` | 67909005 | Chest wall retraction | http://snomed.info/sct |
| 126 | 753 | Observation | `Observation.component.code.coding` | 214264003 | Lethargy | http://snomed.info/sct |
| 127 | 756 | Observation | `Observation.component.code.coding` | 91175000 | Seizure | http://snomed.info/sct |
| 128 | 759 | Observation | `Observation.component.code.coding` | 386661006 | Fever | http://snomed.info/sct |
| 129 | 762 | Observation | `Observation.component.code.coding` | 386689009 | Hypothermia | http://snomed.info/sct |
| 130 | 765 | Observation | `Observation.component.code.coding` | SP000916 | Tidak buang air besar 48 jam setelah lahir | http://terminology.kemkes.go.id/sp |
| 131 | 768 | Observation | `Observation.component.code.coding` | SP000917 | Muntah berisi susu atau cairan berwarna hijau | http://terminology.kemkes.go.id/sp |
| 132 | 771 | Observation | `Observation.component.code.coding` | SP000918 | Perut kembung dan sulit bernapas | http://terminology.kemkes.go.id/sp |
| 133 | 774 | Observation | `Observation.component.code.coding` | 204712000 | Anal atresia | http://snomed.info/sct |
| 134 | 777 | Observation | `Observation.component.code.coding` | 423243008 | Purulent conjunctival discharge | http://snomed.info/sct |
| 135 | 778 | Observation | `Observation.valueCodeableConcept.coding` | 255509001 | Large | http://snomed.info/sct |
| 136 | 779 | Observation | `Observation.valueCodeableConcept.coding` | 255507004 | Small | http://snomed.info/sct |
| 137 | 780 | Observation | `Observation.component.code.coding` | 42052009 | Neonatal infection of umbilical cord stump | http://snomed.info/sct |
| 138 | 783 | Observation | `Observation.component.code.coding` | SP000919 | Pusar kemerahan meluas sampai dinding perut > 1 cm | http://terminology.kemkes.go.id/sp |
| 139 | 786 | Observation | `Observation.component.code.coding` | SP000920 | Pusar kemerahan | http://terminology.kemkes.go.id/sp |
| 140 | 789 | Observation | `Observation.component.code.coding` | 271760008 | Pustule | http://snomed.info/sct |
| 141 | 801 | Observation | `Observation.code.coding` | OC000126 | Klasifikasi infeksi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 142 | 802 | Observation | `Observation.valueCodeableConcept.coding` | OV000134 | Infeksi bakteri berat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 143 | 803 | Observation | `Observation.valueCodeableConcept.coding` | OV000135 | Infeksi bakteri lokal | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 144 | 804 | Observation | `Observation.valueCodeableConcept.coding` | OV000136 | Mungkin bukan infeksi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 145 | 827 | Observation | `Observation.code.coding` | OC000129 | Klasifikasi Ikterus | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 146 | 828 | Observation | `Observation.valueCodeableConcept.coding` | OV000179 | Ikterus Berat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 147 | 829 | Observation | `Observation.valueCodeableConcept.coding` | 18165001 | Jaundice | http://snomed.info/sct |
| 148 | 830 | Observation | `Observation.valueCodeableConcept.coding` | OV000180 | Tidak ada ikterus | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 149 | 853 | Observation | `Observation.code.coding` | OC000098 | Klasifikasi Diare | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 150 | 854 | Observation | `Observation.valueCodeableConcept.coding` | OV000184 | Diare Dehidrasi Berat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 151 | 855 | Observation | `Observation.valueCodeableConcept.coding` | OV000185 | Diare Dehidrasi Ringan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 152 | 856 | Observation | `Observation.valueCodeableConcept.coding` | OV000186 | Diare Tanda Dehidrasi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 153 | 875 | Observation | `Observation.code.coding` | 254387007 | Human immunodeficiency virus infection classification systems | http://snomed.info/sct |
| 154 | 876 | Observation | `Observation.valueCodeableConcept.coding` | 165816005 | Human immunodeficiency virus positive | http://snomed.info/sct |
| 155 | 877 | Observation | `Observation.valueCodeableConcept.coding` | OV000187 | Terpajan HIV: mungkin infeksi HIV | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 156 | 878 | Observation | `Observation.valueCodeableConcept.coding` | OV000188 | Infeksi HIV tidak diketahui | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 157 | 879 | Observation | `Observation.valueCodeableConcept.coding` | OV000189 | Bukan infeksi HIV |  |
| 158 | 898 | Observation | `Observation.code.coding` | OC000085 | Klasifikasi berat badan menurut umur dan/atau masalah pemberian ASI | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 159 | 899 | Observation | `Observation.valueCodeableConcept.coding` | OV000201 | Berat badan sangat rendah menurut umur | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 160 | 900 | Observation | `Observation.valueCodeableConcept.coding` | OV000202 | Berat badan rendah menurut umur dan/atau masalah pemberian ASI | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 161 | 901 | Observation | `Observation.valueCodeableConcept.coding` | OV000203 | Berat badan tidak rendah menurut umur dan tidak ada masalah pemberian ASI | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 162 | 924 | Observation | `Observation.code.coding` | OC000086 | Klasifikasi Berat Badan Menurut umur dan/atau Masalah Pemberian Minum | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 163 | 925 | Observation | `Observation.valueCodeableConcept.coding` | OV000201 | Berat badan sangat rendah menurut umur | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 164 | 926 | Observation | `Observation.valueCodeableConcept.coding` | OV000204 | Berat badan rendah menurut umur dan/atau masalah pemberian minum | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 165 | 927 | Observation | `Observation.valueCodeableConcept.coding` | OV000205 | Berat badan tidak rendah menurut umur dan tidak ada masalah pemberian minum | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 166 | 947 | Observation | `Observation.code.coding` | OC000089 | Klasifikasi Status Kegawatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 167 | 948 | Observation | `Observation.valueCodeableConcept.coding` | 410429000 | Cardiac arrest | http://snomed.info/sct |
| 168 | 949 | Observation | `Observation.valueCodeableConcept.coding` | OV000137 | Penyakit sangat berat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 169 | 950 | Observation | `Observation.valueCodeableConcept.coding` | 359746009 | Patient's condition stable | http://snomed.info/sct |
| 170 | 973 | Observation | `Observation.code.coding` | OC000091 | Klasifikasi batuk dan/atau sukar bernapas | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 171 | 974 | Observation | `Observation.valueCodeableConcept.coding` | OV000287 | Pneumonia berat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 172 | 975 | Observation | `Observation.valueCodeableConcept.coding` | 233604007 | Pneumonia | http://snomed.info/sct |
| 173 | 976 | Observation | `Observation.valueCodeableConcept.coding` | OV000288 | Batuk bukan pneumonia | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 174 | 999 | Observation | `Observation.code.coding` | OC000098 | Klasifikasi Diare | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 175 | 1000 | Observation | `Observation.valueCodeableConcept.coding` | 162104009 | Diarrhea not present | http://snomed.info/sct |
| 176 | 1001 | Observation | `Observation.valueCodeableConcept.coding` | OV000214 | Diare dehidrasi berat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 177 | 1002 | Observation | `Observation.valueCodeableConcept.coding` | OV000215 | Diare dehidrasi ringan/sedang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 178 | 1003 | Observation | `Observation.valueCodeableConcept.coding` | OV000186 | Diare tanpa dehidrasi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 179 | 1004 | Observation | `Observation.valueCodeableConcept.coding` | OV000217 | Diare persisten berat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 180 | 1005 | Observation | `Observation.valueCodeableConcept.coding` | OV000218 | Diare persisten | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 181 | 1006 | Observation | `Observation.valueCodeableConcept.coding` | 46799006 | Dysenteric diarrhea | http://snomed.info/sct |
| 182 | 1033 | Observation | `Observation.code.coding` | OC000100 | Klasifikasi Demam | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 183 | 1034 | Observation | `Observation.valueCodeableConcept.coding` | OV000223 | Penyakit berat dengan demam | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 184 | 1035 | Observation | `Observation.valueCodeableConcept.coding` | 61462000 | Malaria | http://snomed.info/sct |
| 185 | 1036 | Observation | `Observation.valueCodeableConcept.coding` | OV000224 | Demam mungkin bukan malaria | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 186 | 1037 | Observation | `Observation.valueCodeableConcept.coding` | OV000225 | Penyakit berat dengan demam | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 187 | 1038 | Observation | `Observation.valueCodeableConcept.coding` | OV000226 | Demam bukan malaria | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 188 | 1061 | Observation | `Observation.code.coding` | OC000102 | Klasifikasi campak | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 189 | 1062 | Observation | `Observation.valueCodeableConcept.coding` | OV000229 | Campak dengan komplikasi berat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 190 | 1063 | Observation | `Observation.valueCodeableConcept.coding` | OV000230 | Campak dengan komplikasi pada mata | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 191 | 1064 | Observation | `Observation.valueCodeableConcept.coding` | OV000231 | Campak dengan komplikasi pada mulut | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 192 | 1065 | Observation | `Observation.valueCodeableConcept.coding` | OV000232 | Campak dengan komplikasi pada mata dan mulut | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 193 | 1085 | Observation | `Observation.code.coding` | OC000105 | Klasifikasi infeksi dengue | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 194 | 1086 | Observation | `Observation.valueCodeableConcept.coding` | 20927009 | Dengue hemorrhagic fever | http://snomed.info/sct |
| 195 | 1087 | Observation | `Observation.valueCodeableConcept.coding` | 722863008 | Dengue with warning signs | http://snomed.info/sct |
| 196 | 1088 | Observation | `Observation.valueCodeableConcept.coding` | 722862003 | Dengue without warning signs | http://snomed.info/sct |
| 197 | 1089 | Observation | `Observation.valueCodeableConcept.coding` | OV000129 | Demam mungkin bukan dengue | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 198 | 1108 | Observation | `Observation.code.coding` | OC000107 | Klasifikasi masalah telinga | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 199 | 1109 | Observation | `Observation.valueCodeableConcept.coding` | 52404001 | Mastoiditis | http://snomed.info/sct |
| 200 | 1110 | Observation | `Observation.valueCodeableConcept.coding` | OV000241 | Infeksi telinga akut | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 201 | 1111 | Observation | `Observation.valueCodeableConcept.coding` | OV000289 | Infeksi telinga kronis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 202 | 1112 | Observation | `Observation.valueCodeableConcept.coding` | OV000242 | Tidak ada infeksi telinga | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 203 | 1131 | Observation | `Observation.code.coding` | OC000108 | Klasifikasi status gizi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 204 | 1132 | Observation | `Observation.valueCodeableConcept.coding` | OV000254 | Gizi buruk dengan komplikasi berat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 205 | 1133 | Observation | `Observation.valueCodeableConcept.coding` | OV000255 | Gizi buruk tanpa komplikasi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 206 | 1134 | Observation | `Observation.valueCodeableConcept.coding` | 65404009 | Undernutrition | http://snomed.info/sct |
| 207 | 1135 | Observation | `Observation.valueCodeableConcept.coding` | 248324001 | Well nourished | http://snomed.info/sct |
| 208 | 1136 | Observation | `Observation.valueCodeableConcept.coding` | OV000258 | Risiko Gizi Lebih | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 209 | 1137 | Observation | `Observation.valueCodeableConcept.coding` | 302872003 | Overnutrition | http://snomed.info/sct |
| 210 | 1138 | Observation | `Observation.valueCodeableConcept.coding` | 414915002 | Obese | http://snomed.info/sct |
| 211 | 1162 | Observation | `Observation.code.coding` | 1153590000 | Length for age z-score | http://snomed.info/sct |
| 212 | 1163 | Observation | `Observation.code.coding` | 1153604005 | Body height for age z-score | http://snomed.info/sct |
| 213 | 1193 | Observation | `Observation.code.coding` | 1153594009 | Head circumference for age z-score | http://loinc.org |
| 214 | 1196 | Observation | `Observation.interpretation.coding` | 840673007 | Normal head | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 215 | 1201 | Observation | `Observation.interpretation.coding` | 1148757008 | Microcephaly | http://snomed.info/sct |
| 216 | 1204 | Observation | `Observation.interpretation.coding` | 1145403003 | Macrocephaly | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 217 | 1225 | Observation | `Observation.code.coding` | OC000111 | Klasifikasi anemia | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 218 | 1226 | Observation | `Observation.valueCodeableConcept.coding` | OV000272 | Anemia berat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 219 | 1227 | Observation | `Observation.valueCodeableConcept.coding` | 271737000 | Anemia | http://snomed.info/sct |
| 220 | 1228 | Observation | `Observation.valueCodeableConcept.coding` | 860635002 | No anemia present | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 221 | 1247 | Observation | `Observation.code.coding` | 254387007 | Human immunodeficiency virus infection classification systems | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 222 | 1248 | Observation | `Observation.valueCodeableConcept.coding` | 165816005 | Human immunodeficiency virus positive | http://snomed.info/sct |
| 223 | 1249 | Observation | `Observation.valueCodeableConcept.coding` | OV000187 | Terpajan HIV: mungkin infeksi HIV | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 224 | 1250 | Observation | `Observation.valueCodeableConcept.coding` | OV000188 | Infeksi HIV tidak diketahui | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 225 | 1251 | Observation | `Observation.valueCodeableConcept.coding` | OV000189 | Bukan infeksi HIV |  |
| 226 | 1260 | Procedure | `Procedure.code.coding` | 400984005 | Congenital hypothyroidism screening test | http://snomed.info/sct |
| 227 | 1271 | Observation | `Observation.code.coding` | 29575-8 | Thyrotropin [Units/volume] in DBS | http://loinc.org |
| 228 | 1308 | Observation | `Observation.interpretation.coding` | 772170009 | Tuberculosis suspected | http://snomed.info/sct |
| 229 | 1309 | Observation | `Observation.interpretation.coding` | SP000789 | Bukan terduga TBC | http://terminology.kemkes.go.id/sp |
| 230 | 1312 | Observation | `Observation.code.coding` | 171126009 | Tuberculosis screening | http://snomed.info/sct |
| 231 | 1472 | Observation | `Observation.code.coding` | 1280010004 | Screening for child developmental disorder | http://snomed.info/sct |
| 232 | 1473 | Observation | `Observation.valueCodeableConcept.coding` | Ds | Perkembangan sesuai usia | http://terminology.kemkes.go.id/Codesystem/kpsp |
| 233 | 1474 | Observation | `Observation.valueCodeableConcept.coding` | Dm | Perkembangan meragukan | http://terminology.kemkes.go.id/Codesystem/kpsp |
| 234 | 1475 | Observation | `Observation.valueCodeableConcept.coding` | Dp | Perkembangan curiga adanya penyimpangan | http://terminology.kemkes.go.id/Codesystem/kpsp |
| 235 | 1589 | Observation | `Observation.code.coding` | 252957005 | Children's hearing test | http://snomed.info/sct |
| 236 | 1590 | Observation | `Observation.valueCodeableConcept.coding` | 17621005 | Normal | http://snomed.info/sct |
| 237 | 1591 | Observation | `Observation.valueCodeableConcept.coding` | 410519009 | At risk | http://snomed.info/sct |
| 238 | 1608 | Observation | `Observation.code.coding` | 252963001 | Children's vision test | http://snomed.info/sct |
| 239 | 1609 | Observation | `Observation.valueCodeableConcept.coding` | 17621005 | Normal | http://snomed.info/sct |
| 240 | 1610 | Observation | `Observation.valueCodeableConcept.coding` | 410519009 | At risk | http://snomed.info/sct |
| 241 | 1618 | Observation | `Observation.component.code.coding` | 3457005 | Patient referral | http://snomed.info/sct |
| 242 | 1631 | Procedure | `Procedure.code.coding` | 410314003 | Health promotion education, guidance, and counseling | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 115 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 80 |
| http://loinc.org | 21 |
| http://terminology.kemkes.go.id/sp | 17 |
| http://terminology.kemkes.go.id/Codesystem/kpsp | 3 |
| http://sys-ids.kemkes.go.id/kfa | 2 |
|  | 2 |
| http://hl7.org/fhir/sid/icd-10 | 1 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 1 |
| **Total** | **242** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 442 | – | Tanggal kunjungan | – | `` |
| 1629 | – | Tanggal kunjungan | – | `` |
