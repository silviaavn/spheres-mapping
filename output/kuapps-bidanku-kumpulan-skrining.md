# Output Form: KuApps BidanKu - Kumpulan Skrinning

Sumber: `mapping/phdt-data-dictionary-kuapps-bidanku-kumpulan-skrining.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-kuapps-bidanku-kumpulan-skrining.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 23 |
| Code (`jumlah code` = 1) | 30 |
| Code unik (code + CodeSystem) | 30 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 15 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–27 | QuestionnaireResponse | – | – | _Batuk terus menerus_ → `QuestionnaireResponse.item.linkId` (12, tanpa BQ)<br>_Demam lebih dari ≥ 2 minggu_ → `QuestionnaireResponse.item.linkId` (16, tanpa BQ)<br>_BB tidak naik atau turun dalam 2 bulan berturut-turut_ → `QuestionnaireResponse.item.linkId` (20, tanpa BQ)<br>_Kontak erat dengan Pasien TBC_ → `QuestionnaireResponse.item.linkId` (24, tanpa BQ) |
| 2 | 28–69 | QuestionnaireResponse | – | – | _Memiliki masalah di dalam rumah (Home)_ → `QuestionnaireResponse.item.linkId` (38, tanpa BQ)<br>_Memiliki Masalah dengan Pendidikan atau Pekerjaan (Education/Employment)_ → `QuestionnaireResponse.item.linkId` (42, tanpa BQ)<br>_Memiliki Masalah Dengan Pola Makan (Eating)_ → `QuestionnaireResponse.item.linkId` (46, tanpa BQ)<br>_Memiliki Masalah dengan Aktivitas (Activity)_ → `QuestionnaireResponse.item.linkId` (50, tanpa BQ)<br>_Memiliki masalah dengan obat-obatan (Drugs)_ → `QuestionnaireResponse.item.linkId` (54, tanpa BQ)<br>_Memiliki masalah dengan kesehatan seksual (Sexuality)_ → `QuestionnaireResponse.item.linkId` (58, tanpa BQ)<br>_Memiliki Masalah dengan Keamanan (Self Image)_ → `QuestionnaireResponse.item.linkId` (62, tanpa BQ)<br>_Memiliki keinginan bunuh diri/depresi (Safety)_ → `QuestionnaireResponse.item.linkId` (66, tanpa BQ) |
| 3 | 70–109 | QuestionnaireResponse | – | – | _Kuesioner PPOK_ → `QuestionnaireResponse.questionnaire` (70, tanpa BQ)<br>_Jenis Kelamin_ → `QuestionnaireResponse.item.linkId` (80, tanpa BQ)<br>_Usia_ → `QuestionnaireResponse.item.linkId` (84, tanpa BQ)<br>_Merokok_ → `QuestionnaireResponse.item.linkId` (89, tanpa BQ)<br>_Apakah Anda Pernah merasa napas pendek ketika berjalan lebih cepat pada jalan yang datar atau pada jalan yang sedikit menanjak?_ → `QuestionnaireResponse.item.linkId` (94, tanpa BQ)<br>_Apakah anda mempunyai dahak yang berasal dari paru atau kesulitan mengeluarkan dahak saat Anda sedang tidak menderita flu?_ → `QuestionnaireResponse.item.linkId` (98, tanpa BQ)<br>_Apakah anda Biasanya batuk saat Anda sedang tidak menderita flu?_ → `QuestionnaireResponse.item.linkId` (102, tanpa BQ)<br>_Apakah Dokter atau tenaga kesehatan lainnya pernah meminta Anda untuk melakukan pemeriksaan spirometri atau peakflow meter (meniup ke dalam suatu alat)?_ → `QuestionnaireResponse.item.linkId` (106, tanpa BQ) |
| 4 | 110–123 | Observation | SP000111 | Hasil Kuesioner PUMA | _Skor PUMA_ → `Observation.status` (110, tanpa BQ) |
| 5 | 124–209 | QuestionnaireResponse | – | – | _Apakah Anda sering merasa sakit kepala?_ → `QuestionnaireResponse.item.linkId` (134, tanpa BQ)<br>_Apakah Anda kehilangan nafsu makan?_ → `QuestionnaireResponse.item.linkId` (138, tanpa BQ)<br>_Apakah tidur Anda tidak nyenyak?_ → `QuestionnaireResponse.item.linkId` (142, tanpa BQ)<br>_Apakah Anda mudah merasa takut?_ → `QuestionnaireResponse.item.linkId` (146, tanpa BQ)<br>_Apakah tangan Anda gemetar?_ → `QuestionnaireResponse.item.linkId` (150, tanpa BQ)<br>_Apakah Anda mengalami gangguan pencernaan?_ → `QuestionnaireResponse.item.linkId` (154, tanpa BQ)<br>_Apakah Anda merasa sulit berpikir jernih?_ → `QuestionnaireResponse.item.linkId` (158, tanpa BQ)<br>_Apakah Anda merasa tidak bahagia?_ → `QuestionnaireResponse.item.linkId` (162, tanpa BQ)<br>_Apakah Anda lebih sering menangis?_ → `QuestionnaireResponse.item.linkId` (166, tanpa BQ)<br>_Apakah Anda merasa sulit untuk menikmati aktivitas sehari-hari?_ → `QuestionnaireResponse.item.linkId` (170, tanpa BQ)<br>_Apakah Anda mengalami kesulitan untuk mengambil keputusan?_ → `QuestionnaireResponse.item.linkId` (174, tanpa BQ)<br>_Apakah aktivitas/ tugas sehari-hari Anda terbengkalai?_ → `QuestionnaireResponse.item.linkId` (178, tanpa BQ)<br>_Apakah Anda merasa tidak mampu berperan dalam kehidupan ini?_ → `QuestionnaireResponse.item.linkId` (182, tanpa BQ)<br>_Apakah Anda kehilangan minat terhadap banyak hal?_ → `QuestionnaireResponse.item.linkId` (186, tanpa BQ)<br>_Apakah Anda merasa tidak berharga?_ → `QuestionnaireResponse.item.linkId` (190, tanpa BQ)<br>_Apakah Anda mempunyai pikiran untuk mengakhiri hidup Anda?_ → `QuestionnaireResponse.item.linkId` (194, tanpa BQ)<br>_Apakah Anda merasa lelah sepanjang waktu?_ → `QuestionnaireResponse.item.linkId` (198, tanpa BQ)<br>_Apakah Anda merasa tidak enak di perut?_ → `QuestionnaireResponse.item.linkId` (202, tanpa BQ)<br>_Apakah Anda mudah lelah?_ → `QuestionnaireResponse.item.linkId` (206, tanpa BQ) |
| 6 | 210–274 | QuestionnaireResponse | – | – | _Skrining Lansia Sederhana (SKILAS)_ → `QuestionnaireResponse.questionnaire` (210, tanpa BQ)<br>_Penurunan Kognitif_ → `QuestionnaireResponse.item.linkId` (219, tanpa BQ)<br>_Orientasi waktu dan tempat_ → `QuestionnaireResponse.item.item.text` (222, tanpa BQ)<br>_Mengulang ketiga kata_ → `QuestionnaireResponse.item.item.text` (226, tanpa BQ)<br>_Keterbatasan Mobilisasi_ → `QuestionnaireResponse.item.linkId` (229, tanpa BQ)<br>_Tes Berdiri dari Kursi_ → `QuestionnaireResponse.item.item.text` (232, tanpa BQ)<br>_Malnutrisi_ → `QuestionnaireResponse.item.linkId` (235, tanpa BQ)<br>_BB berkurang >3kg dalam 3 bulan terakhir atau pakaian jadi lebih longgar_ → `QuestionnaireResponse.item.item.linkId` (237, tanpa BQ)<br>_Hilang nafsu makan/ kesulitan/ makan_ → `QuestionnaireResponse.item.item.linkId` (241, tanpa BQ)<br>_LiLA < 21 cm_ → `QuestionnaireResponse.item.item.linkId` (245, tanpa BQ)<br>_Gejala Depresi (dalam 2 minggu terakhir)_ → `QuestionnaireResponse.item.linkId` (249, tanpa BQ)<br>_Perasaan sedih, tertekan, atau putus asa_ → `QuestionnaireResponse.item.item.linkId` (251, tanpa BQ)<br>_Sedikit minat atau kesenangan dalam melakukan sesuatu_ → `QuestionnaireResponse.item.item.linkId` (255, tanpa BQ)<br>_Gangguan Penglihatan_ → `QuestionnaireResponse.item.linkId` (259, tanpa BQ)<br>_Masalah pada mata (sulit lihat jauh, membaca, penyakit mata, sedang dalam pengobatan Hipertensi/ diabetes)_ → `QuestionnaireResponse.item.item.linkId` (261, tanpa BQ)<br>_Tes Melihat_ → `QuestionnaireResponse.item.item.linkId` (265, tanpa BQ)<br>_Gangguan Pendengaran_ → `QuestionnaireResponse.item.linkId` (269, tanpa BQ)<br>_Tes Bisik_ → `QuestionnaireResponse.item.answer.item.linkId` (271, tanpa BQ) |
| 7 | 276–287 | Observation | SP000779 | Multipara dengan kehamilan oleh pasangan baru | _Multipara dengan kehamilan oleh pasangan baru_ → `Observation.valueBoolean` (279, tanpa BQ) |
| 8 | 288–299 | Observation | 813541000000100 | Pregnancy resulting from assisted conception | _Kehamilan dengan Teknologi Reproduksi Berbantu: Bayi Tabung, Obat Induksi Ovulasi_ → `Observation.valueBoolean` (291, tanpa BQ) |
| 9 | 300–311 | Observation | SP000780 | Umur ≥ 35 Tahun | _Umur ≥ 35 Tahun_ → `Observation.valueBoolean` (303, tanpa BQ) |
| 10 | 312–323 | Observation | 102877006 | Nulliparous | _Nulipara_ → `Observation.valueBoolean` (315, tanpa BQ) |
| 11 | 324–335 | Observation | SP000781 | Multipara yang Jarak Kehamilan Sebelumnya > 10 Tahun | _Multipara yang Jarak Kehamilan Sebelumnya > 10 Tahun_ → `Observation.valueBoolean` (327, tanpa BQ) |
| 12 | 336–347 | Observation | 700190003 | Family history of pre-eclampsia | _Riwayat Preeklampsia pada Ibu atau Saudara Perempuan_ → `Observation.valueBoolean` (339, tanpa BQ) |
| 13 | 348–359 | Observation | 162864005 | Body mass index 30+ - obesity | _Obesitas Sebelum Hamil (IMT > 30 kg/m2)_ → `Observation.valueBoolean` (351, tanpa BQ) |
| 14 | 360–371 | Observation | SP000782 | Multipara Dengan Riwayat Preeklampsia Sebelumnya | _Multipara Dengan Riwayat Preeklampsia Sebelumnya_ → `Observation.valueBoolean` (363, tanpa BQ) |
| 15 | 372–383 | Observation | 16356006 | Multiple pregnancy | _Kehamilan Multipel_ → `Observation.valueBoolean` (375, tanpa BQ) |
| 16 | 384–395 | Observation | 11687002 | Gestational diabetes mellitus | _Diabetes dalam Kehamilan_ → `Observation.valueBoolean` (387, tanpa BQ) |
| 17 | 396–407 | Observation | 8762007 | Chronic hypertension in obstetric context | _Hipertensi Kronik_ → `Observation.valueBoolean` (399, tanpa BQ) |
| 18 | 408–419 | Observation | 90708001 | Kidney disease | _Penyakit Ginjal_ → `Observation.valueBoolean` (411, tanpa BQ) |
| 19 | 420–431 | Observation | 85828009 | Autoimmune disease | _Penyakit Autoimun, SLE_ → `Observation.valueBoolean` (423, tanpa BQ) |
| 20 | 432–443 | Observation | 26843008 | Antiphospholipid syndrome | _Anti Phospholipid Syndrome_ → `Observation.valueBoolean` (435, tanpa BQ) |
| 21 | 444–455 | Observation | SP000783 | Mean Arterial Presure > 90 mmHg | _Mean Arterial Presure > 90 mmHg_ → `Observation.valueBoolean` (447, tanpa BQ) |
| 22 | 456–467 | Observation | 29738008 | Proteinuria | _Proteinuria_ → `Observation.valueBoolean` (459, tanpa BQ) |
| 23 | 468–479 | Observation | SP000799 | Hasil skrining Preeklampsia | _Kesimpulan_ → `Observation.valueCodeableConcept.coding` (471, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 18 |
| QuestionnaireResponse | 5 |
| **Total** | **23** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 82 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | female | Perempuan | http://hl7.org/fhir/administrative-gender |
| 2 | 83 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | male | Laki-Laki | http://hl7.org/fhir/administrative-gender |
| 3 | 86 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000726 | 40-49 tahun | http://terminology.kemkes.go.id/sp |
| 4 | 87 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000727 | 50-59 tahun | http://terminology.kemkes.go.id/sp |
| 5 | 88 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000728 | >= 60 tahun | http://terminology.kemkes.go.id/sp |
| 6 | 91 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000435 | <20 bungkus per tahun | http://terminology.kemkes.go.id/sp |
| 7 | 92 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000436 | 20-30 bungkus per tahun | http://terminology.kemkes.go.id/sp |
| 8 | 93 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000437 | >30 bungkus per tahun | http://terminology.kemkes.go.id/sp |
| 9 | 112 | Observation | `Observation.code.coding` | SP000111 | Hasil Kuesioner PUMA | http://terminology.kemkes.go.id/sp |
| 10 | 114 | Observation | `Observation.interpretation.coding` | 723505004 | Low risk | http://snomed.info/sct |
| 11 | 116 | Observation | `Observation.interpretation.coding` | 723509005 | High risk | http://snomed.info/sct |
| 12 | 278 | Observation | `Observation.code.coding` | SP000779 | Multipara dengan kehamilan oleh pasangan baru | http://terminology.kemkes.go.id/sp |
| 13 | 290 | Observation | `Observation.code.coding` | 813541000000100 | Pregnancy resulting from assisted conception | http://snomed.info/sct |
| 14 | 302 | Observation | `Observation.code.coding` | SP000780 | Umur ≥ 35 Tahun | http://terminology.kemkes.go.id/sp |
| 15 | 314 | Observation | `Observation.code.coding` | 102877006 | Nulliparous | http://snomed.info/sct |
| 16 | 326 | Observation | `Observation.code.coding` | SP000781 | Multipara yang Jarak Kehamilan Sebelumnya > 10 Tahun | http://terminology.kemkes.go.id/sp |
| 17 | 338 | Observation | `Observation.code.coding` | 700190003 | Family history of pre-eclampsia | http://snomed.info/sct |
| 18 | 350 | Observation | `Observation.code.coding` | 162864005 | Body mass index 30+ - obesity | http://snomed.info/sct |
| 19 | 362 | Observation | `Observation.code.coding` | SP000782 | Multipara Dengan Riwayat Preeklampsia Sebelumnya | http://terminology.kemkes.go.id/sp |
| 20 | 374 | Observation | `Observation.code.coding` | 16356006 | Multiple pregnancy | http://snomed.info/sct |
| 21 | 386 | Observation | `Observation.code.coding` | 11687002 | Gestational diabetes mellitus | http://snomed.info/sct |
| 22 | 398 | Observation | `Observation.code.coding` | 8762007 | Chronic hypertension in obstetric context | http://snomed.info/sct |
| 23 | 410 | Observation | `Observation.code.coding` | 90708001 | Kidney disease | http://snomed.info/sct |
| 24 | 422 | Observation | `Observation.code.coding` | 85828009 | Autoimmune disease | http://snomed.info/sct |
| 25 | 434 | Observation | `Observation.code.coding` | 26843008 | Antiphospholipid syndrome | http://snomed.info/sct |
| 26 | 446 | Observation | `Observation.code.coding` | SP000783 | Mean Arterial Presure > 90 mmHg | http://terminology.kemkes.go.id/sp |
| 27 | 458 | Observation | `Observation.code.coding` | 29738008 | Proteinuria | http://snomed.info/sct |
| 28 | 470 | Observation | `Observation.code.coding` | SP000799 | Hasil skrining Preeklampsia | http://terminology.kemkes.go.id/sp |
| 29 | 471 | Observation | `Observation.valueCodeableConcept.coding` | SP000784 | Berisiko Preeklampsia | http://terminology.kemkes.go.id/sp |
| 30 | 472 | Observation | `Observation.valueCodeableConcept.coding` | SP000785 | Tidak Berisiko Preeklampsia | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://terminology.kemkes.go.id/sp | 15 |
| http://snomed.info/sct | 13 |
| http://hl7.org/fhir/administrative-gender | 2 |
| **Total** | **30** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 480 | – | REKAP | – | `` |
| 481 | – | JUDUL SKRINING | – | `` |
| 482 | – | Skrinning Gejala TBC | – | `` |
| 483 | – | Skrinnig HEEADSSS | – | `` |
| 484 | – | Kuesioner PPOK | – | `` |
| 485 | – | Kuesioner Pemeriksaan Kesehatan Jiwa | – | `` |
| 486 | – | Skrining Lansia Sederhana (SKILAS) | – | `` |
| 487 | – | Skrining Preeklampsia | – | `` |
