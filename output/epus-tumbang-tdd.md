# Output Form: ePuskesmas Tumbuh Kembang - TDD

Sumber: `mapping/phdt-data-dictionary-epus-tumbang-tdd.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-epus-tumbang-tdd.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 8 |
| Code (`jumlah code` = 1) | 0 |
| Code unik (code + CodeSystem) | 0 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 0 |
| Variabel BQ (unik) | 0 |
| Variabel raw (variabel dictionary; belum ada file mentah) | 37 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 3–47 | QuestionnaireResponse | – | – | _Apakah bayi dapat mengatakan “Aaaaa”, “Ooooo”?_ → `QuestionnaireResponse.item.item.linkId` (13, tanpa BQ)<br>_Apakah bayi menatap wajah dan tampak mendengarkan Anda, lalu berbicara saat Anda diam?_ → `QuestionnaireResponse.item.item.linkId` (17, tanpa BQ)<br>_Apakah Anda dapat seolah-olah berbicara dengan bayi Anda?_ → `QuestionnaireResponse.item.item.linkId` (21, tanpa BQ)<br>_Apakah bayi kaget bila mendengar suara (mengejapkan mata, napas lebih cepat)?_ → `QuestionnaireResponse.item.item.linkId` (27, tanpa BQ)<br>_Apakah bayi kelihatan menoleh bila Anda berbicara di sebelahnya?_ → `QuestionnaireResponse.item.item.linkId` (31, tanpa BQ)<br>_Apakah bayi Anda dapat tersenyum?_ → `QuestionnaireResponse.item.item.linkId` (37, tanpa BQ)<br>_Apakah bayi Anda kenal dengan Anda, seperti tersenyum lebih cepat pada Anda dibandingkan orang lain?_ → `QuestionnaireResponse.item.item.linkId` (41, tanpa BQ) |
| 2 | 48–86 | QuestionnaireResponse | – | – | _Apakah bayi Anda dapat tertawa keras?_ → `QuestionnaireResponse.item.item.linkId` (56, tanpa BQ)<br>_Apakah bayi dapat bermain menggelembungkan mulut seperti meniup balon?_ → `QuestionnaireResponse.item.item.linkId` (60, tanpa BQ)<br>_Apakah bayi memberi respons tertentu, seperti menjadi lebih riang bila Anda datang?_ → `QuestionnaireResponse.item.item.linkId` (66, tanpa BQ)<br>_Pemeriksa duduk menghadap bayi yang dipangku orang tuanya, bunyikan bel disamping tanpa terlihat bayi, apakah bayi itu menoleh ke samping?_ → `QuestionnaireResponse.item.item.linkId` (70, tanpa BQ)<br>_Pemeriksa menatap mata bayi sekitar 45 cm, lalu gunakan mainan untuk menarik pandangan bayi ke kiri, kanan, atas, dan bawah. Apakah bayi dapat mengikutinya?_ → `QuestionnaireResponse.item.item.linkId` (76, tanpa BQ)<br>_Apakah bayi berkedip bila pemeriksa melakukan gerakan menusuk mata, lalu berhenti sekitar 3 cm tanpa menyentuh mata?_ → `QuestionnaireResponse.item.item.linkId` (80, tanpa BQ) |
| 3 | 87–125 | QuestionnaireResponse | – | – | _Apakah bayi dapat membuat suara berulang seperti ‘mamamama’, ‘babababa’?_ → `QuestionnaireResponse.item.item.linkId` (95, tanpa BQ)<br>_Apakah bayi dapat memanggil mama atau papa, walaupun tidak untuk memanggil orang tuanya?_ → `QuestionnaireResponse.item.item.linkId` (99, tanpa BQ)<br>_Pemeriksa duduk menghadap bayi yang dipangku orang tuanya, bunyikan bel di samping bawah tanpa terlihat bayi, apakah bayi langsung menoleh ke samping bawah?_ → `QuestionnaireResponse.item.item.linkId` (105, tanpa BQ)<br>_Apakah bayi mengikuti perintah tanpa dibantu gerakan badan, seperti “Stop, berikan mainanmu”?_ → `QuestionnaireResponse.item.item.linkId` (109, tanpa BQ)<br>_Apakah bayi mengikuti perintah dengan dibantu gerakan badan, seperti “Stop, berikan mainanmu”?_ → `QuestionnaireResponse.item.item.linkId` (115, tanpa BQ)<br>_Apakah bayi secara spontan memulai permainan dengan gerakan tubuh, seperti ‘Pok Ame-Ame’ atau ‘Cilukba’?_ → `QuestionnaireResponse.item.item.linkId` (119, tanpa BQ) |
| 4 | 126–164 | QuestionnaireResponse | – | – | _Apakah anak dapat memanggil ‘mama’ atau ‘papa’, hanya untuk memanggil orang tuanya?_ → `QuestionnaireResponse.item.item.linkId` (134, tanpa BQ)<br>_Apakah anak memulai menggunakan kata-kata lain, selain kata ‘mama’, ‘papa’, anggota keluarga lain, dan hewan peliharaan?_ → `QuestionnaireResponse.item.item.linkId` (138, tanpa BQ)<br>_Pemeriksa duduk menghadap bayi yang dipangku orang tuanya, bunyikan bel di samping bawah tanpa terlihat bayi, apakah bayi langsung menoleh ke samping bawah?_ → `QuestionnaireResponse.item.item.linkId` (144, tanpa BQ)<br>_Apakah anak mengikuti perintah tanpa dibantu gerakan badan, seperti “Stop, berikan mainanmu”?_ → `QuestionnaireResponse.item.item.linkId` (148, tanpa BQ)<br>_Apakah anak secara spontan memulai permainan dengan gerakan tubuh, seperti ‘Pok Ame-Ame’ atau ‘Cilukba’?_ → `QuestionnaireResponse.item.item.linkId` (154, tanpa BQ)<br>_Apakah anak Anda menunjuk dengan jari telunjuk bila ingin sesuatu, bukan dengan cara memegang dengan semua jari?_ → `QuestionnaireResponse.item.item.linkId` (158, tanpa BQ) |
| 5 | 165–203 | QuestionnaireResponse | – | – | _Apakah anak dapat mengucapkan 2 atau lebih kata yang menunjukkan keinginan, seperti “Susu”, “Minum”, “Lagi”?_ → `QuestionnaireResponse.item.item.linkId` (173, tanpa BQ)<br>_Apakah anak secara spontan mengatakan 2 kombinasi kata, seperti “Mau bobo”, “Lihat Papa”?_ → `QuestionnaireResponse.item.item.linkId` (177, tanpa BQ)<br>_Apakah anak dapat menunjukkan paling sedikit 1 anggota badan, misal “Mana hidungmu?”, “Mana matamu?” tanpa diberi contoh?_ → `QuestionnaireResponse.item.item.linkId` (183, tanpa BQ)<br>_Apakah anak dapat mengerjakan 2 macam perintah dalam satu kalimat, seperti “Ambil sepatumu dan taruh disini” tanpa diberi contoh?_ → `QuestionnaireResponse.item.item.linkId` (187, tanpa BQ)<br>_Apakah anak secara spontan memulai permainan dengan gerakan tubuh, seperti ‘Pok Ame-Ame’ atau ‘Cilukba’?_ → `QuestionnaireResponse.item.item.linkId` (193, tanpa BQ)<br>_Apakah anak Anda menunjuk dengan jari telunjuk bila ingin sesuatu, bukan dengan cara memegang dengan semua jari?_ → `QuestionnaireResponse.item.item.linkId` (197, tanpa BQ) |
| 6 | 204–242 | QuestionnaireResponse | – | – | _Apakah anak mulai menggunakan kata-kata lain, selain kata ‘mama’, ‘papa’, anggota keluarga lain, dan hewan peliharaan?_ → `QuestionnaireResponse.item.item.linkId` (212, tanpa BQ)<br>_Apakah anak mulai mengungkapkan kata yang berarti ‘milik’ misal “Susu kamu”, “Bonekaku”?_ → `QuestionnaireResponse.item.item.linkId` (216, tanpa BQ)<br>_Apakah anak dapat mengerjakan 2 macam perintah dalam satu kalimat, seperti “Ambil sepatu dan taruh disini” tanpa diberi contoh?_ → `QuestionnaireResponse.item.item.linkId` (222, tanpa BQ)<br>_Apakah anak dapat menunjuk minimal 2 nama benda di depannya (cangkir, bola, sendok)?_ → `QuestionnaireResponse.item.item.linkId` (226, tanpa BQ)<br>_Apakah anak secara spontan memulai permainan dengan gerakan tubuh, seperti ‘Pok Ame-Ame’ atau ‘Cilukba’?_ → `QuestionnaireResponse.item.item.linkId` (232, tanpa BQ)<br>_Apakah anak Anda menunjuk dengan jari telunjuk bila ingin sesuatu, bukan dengan cara memegang dengan semua jari?_ → `QuestionnaireResponse.item.item.linkId` (236, tanpa BQ) |
| 7 | 243–281 | QuestionnaireResponse | – | – | _Apakah anak dapat menyebutkan nama benda dan kegunaannya, seperti cangkir untuk minum, bola untuk dilempar, pensil warna untuk menggambar, sendok untuk makan?_ → `QuestionnaireResponse.item.item.linkId` (251, tanpa BQ)<br>_Apakah lebih dari tiga perempat orang mengerti apa yang dibicarakan anak Anda?_ → `QuestionnaireResponse.item.item.linkId` (255, tanpa BQ)<br>_Apakah anak dapat menunjukkan minimal 2 nama benda di depannya sesuai fungsinya (misal untuk minum: cangkir, untuk dilempar: bola, untuk makan: sendok, untuk menggambar: pensil warna)?_ → `QuestionnaireResponse.item.item.linkId` (261, tanpa BQ)<br>_Apakah anak dapat mengerjakan perintah yang disertai kata depan? (misal: “Sekarang kubus itu di bawah meja, tolong taruh di atas meja”)?_ → `QuestionnaireResponse.item.item.linkId` (265, tanpa BQ)<br>_Apakah anak secara spontan memulai permainan dengan gerakan tubuh, seperti ‘Pok Ame-Ame’ atau ‘Cilukba’?_ → `QuestionnaireResponse.item.item.linkId` (271, tanpa BQ)<br>_Apakah anak Anda menunjuk dengan jari telunjuk bila ingin sesuatu, bukan dengan cara memegang dengan semua jari?_ → `QuestionnaireResponse.item.item.linkId` (275, tanpa BQ) |
| 8 | 282–313 | QuestionnaireResponse | – | – | _Apakah anak dapat menyebutkan nama benda dan kegunaannya, seperti cangkir untuk minum, bola untuk dilempar, pensil warna untuk menggambar, sendok untuk makan?_ → `QuestionnaireResponse.item.item.linkId` (290, tanpa BQ)<br>_Apakah lebih dari tiga perempat orang mengerti apa yang dibicarakan anak Anda?_ → `QuestionnaireResponse.item.item.linkId` (294, tanpa BQ)<br>_Apakah anak Anda dapat menunjukkan minimal 2 nama benda di depannya sesuai fungsi (misal untuk minum: cangkir, untuk dilempar: bola, untuk makan: sendok, untuk menggambar: pensil warna?)_ → `QuestionnaireResponse.item.item.linkId` (300, tanpa BQ)<br>_Apakah anak secara spontan memulai permainan dengan gerakan tubuh, seperti ‘Pok Ame-Ame’ atau ‘Cilukba’?_ → `QuestionnaireResponse.item.item.linkId` (306, tanpa BQ)<br>_Apakah anak Anda menunjuk dengan jari telunjuk bila ingin sesuatu, bukan dengan cara memegang dengan semua jari?_ → `QuestionnaireResponse.item.item.linkId` (310, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| QuestionnaireResponse | 8 |
| **Total** | **8** |

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
