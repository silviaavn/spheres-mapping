# Output Form: ePuskesmas Tumbuh Kembang - KMPE

Sumber: `mapping/phdt-data-dictionary-epus-tumbang-kmpe.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-epus-tumbang-kmpe.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 1 |
| Code (`jumlah code` = 1) | 0 |
| Code unik (code + CodeSystem) | 0 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 0 |
| Variabel BQ (unik) | 0 |
| Variabel raw (variabel dictionary; belum ada file mentah) | 14 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–65 | QuestionnaireResponse | – | – | _Apakah anak Anda sering bereaksi negatif, marah atau tegang tanpa sebab yang jelas? (Bereaksi negatif contohnya rewel, tidak sabaran, banyak menangis, mudah tersinggung atau bereaksi berlebihan bila merasa situasi tidak seperti yang diharapkannya atau kemauannya tidak terpenuhi)_ → `QuestionnaireResponse.item.linkId` (10, tanpa BQ)<br>_Apakah anak Anda tampak lebih memilih untuk menyendiri, bermain sendiri, atau menghindar dari anak seumurnya atau orang dewasa? (Ingin sendirian, menyendiri dengan ekspresi murung, tidak bersemangat, sedih, atau kehilangan minat terhadap hal-hal yang biasa sangat dinikmati)_ → `QuestionnaireResponse.item.linkId` (14, tanpa BQ)<br>_Apakah anak Anda cenderung bersikap menentang? (Membantah, melawan, tidak mau menurut atau melakukan hal yang sebaliknya dari apa yang diminta, serta tampak tidak peduli ketika diberitahu atau ditegur)_ → `QuestionnaireResponse.item.linkId` (18, tanpa BQ)<br>_Apakah anak Anda mudah takut atau cemas berlebihan tanpa sebab yang jelas? (Misalnya takut pada binatang atau benda yang tidak berbahaya, terlihat cemas ketika tidak melihat ibu atau pengasuh)_ → `QuestionnaireResponse.item.linkId` (22, tanpa BQ)<br>_Apakah anak Anda sering sulit konsentrasi, perhatiannya mudah teralihkan atau banyak bergerak atau tidak bisa diam? (Misalnya anak tidak bisa bertahan lama untuk bermain dengan satu permainan, mudah mengalihkan perhatian bila ada hal lain yang lebih menarik perhatian seperti bunyi atau gerakan, tidak bisa duduk dengan tenang, banyak bergerak atau cenderung berjalan atau berlari mondar-mandir)_ → `QuestionnaireResponse.item.linkId` (26, tanpa BQ)<br>_Apakah anak Anda lebih banyak menempel atau selalu minta ditemani, mudah cemas, dan tidak percaya diri? (Seakan minta perlindungan atau minta ditemani pada berbagai situasi, terutama ketika berada dalam situasi baru atau ada orang yang baru dikenalnya; mengekspresikan kecemasan serta terlihat tidak percaya diri)_ → `QuestionnaireResponse.item.linkId` (30, tanpa BQ)<br>_Apakah anak Anda menunjukkan adanya perubahan pola tidur? (Misalnya sulit tidur, terjaga sepanjang hari, sering terbangun di waktu tidur malam oleh karena mimpi buruk, mengigau, menangis di dalam tidurnya)_ → `QuestionnaireResponse.item.linkId` (34, tanpa BQ)<br>_Apakah anak Anda mengalami perubahan pola makan dari yang biasanya? (Kehilangan nafsu makan, tidak mau makan sama sekali, atau sebaliknya makan berlebihan, sangat memilih jenis makanan, atau membiarkan makanan lama di mulut tanpa dikunyah atau diemut)_ → `QuestionnaireResponse.item.linkId` (38, tanpa BQ)<br>_Apakah anak Anda seringkali mengeluh sakit kepala, sakit perut, atau keluhan fisik lainnya pada waktu-waktu tertentu?_ → `QuestionnaireResponse.item.linkId` (42, tanpa BQ)<br>_Apakah anak Anda mudah putus asa atau frustrasi dan sering menunjukkan emosi yang negatif? (Misalnya sedih atau kecewa yang berkepanjangan, mudah mengeluh, marah, atau protes. Misal ketika anak merasa kesulitan dalam menggambar, lalu berteriak minta tolong, marah, atau kertasnya disobek)_ → `QuestionnaireResponse.item.linkId` (46, tanpa BQ)<br>_Apakah anak Anda menunjukkan kemunduran pola perilaku dari kemampuan yang sudah dimilikinya? (Misalnya mengompol kembali, menghisap jempol, atau tidak mau berpisah dengan orangtua atau pengasuhnya)_ → `QuestionnaireResponse.item.linkId` (50, tanpa BQ)<br>_Apakah anak Anda sering berkelahi, bertengkar, atau menyerang anak lain baik secara verbal maupun non verbal? (Misalnya mengejek, meneriaki, merebut permainan, atau memukul temannya)_ → `QuestionnaireResponse.item.linkId` (54, tanpa BQ)<br>_Apakah anak Anda sering diperlakukan tidak menyenangkan oleh anak lain atau orang dewasa? (Misalnya ditinggal bermain, dihindari, diejek, dikata-katai, direbut mainannya, atau disakiti secara fisik)_ → `QuestionnaireResponse.item.linkId` (58, tanpa BQ)<br>_Apakah anak Anda cenderung berperilaku merusak atau cenderung selalu ingin menang atau menguasai? (Misalnya merusak benda, menyakiti dirinya atau binatang)_ → `QuestionnaireResponse.item.linkId` (62, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| QuestionnaireResponse | 1 |
| **Total** | **1** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| **Total** | **0** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
