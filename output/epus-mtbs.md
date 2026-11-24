# Output Form: ePuskesmas KIA Harian MTBS

Sumber: `mapping/phdt-data-dictionary-epus-mtbs.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-epus-mtbs.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 125 |
| Code (`jumlah code` = 1) | 268 |
| Code unik (code + CodeSystem) | 197 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 19 |
| Variabel BQ (unik) | 0 |
| Variabel raw (variabel dictionary; belum ada file mentah) | 187 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 3–31 | Patient | – | – | _Nama Anak_ → `Patient.name.text` (3, tanpa BQ)<br>_NIK_ → `Patient.identifier.value` (6, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (8, tanpa BQ)<br>_Alamat_ → `Patient.address.extension.extension.valueCode` (16, tanpa BQ) |
| 2 | 74–94 | Practitioner | – | – | _Dokter/Tenaga Medis dan/atau Perawat / Bidan / Nutrisionist / Sanitarian_ → `Practitioner.identifier` (74, tanpa BQ) |
| 3 | 95–98 | RelatedPerson | – | – | _Nama Ibu_ → `RelatedPerson.patient` (95, tanpa BQ) |
| 4 | 99–112 | Encounter | – | – | _Tanggal Kunjungan_ → `Encounter.period.start` (107, tanpa BQ) |
| 5 | 113–119 | Condition | SP000273 | Integrated management of childhood illness | – |
| 6 | 133–150 | Observation | 424144002 | Current chronological age | _Umur_ → `Observation.valueQuantity.value` (136, tanpa BQ) |
| 7 | 151–162 | Observation | 284473002 | Mid upper arm circumference | _LILA_ → `Observation.valueQuantity.value` (154, tanpa BQ) |
| 8 | 163–174 | Observation | 9843-4 | Head Occipital-frontal circumference | _Lingkar Kepala_ → `Observation.valueQuantity.value` (166, tanpa BQ) |
| 9 | 175–186 | Observation | 8310-5 | Body temperature | _Suhu_ → `Observation.valueQuantity.value` (178, tanpa BQ) |
| 10 | 187–193 | Condition | – | – | _Anak sakit apa_ → `Condition.clinicalStatus.coding` (187, tanpa BQ) |
| 11 | 194–205 | Observation | SP000261 | Tipe Kunjungan | _Tipe Kunjungan_ → `Observation.valueCodeableConcept.coding` (197, tanpa BQ) |
| 12 | 206–217 | Observation | OC000099 | Status daerah endemis malaria tempat tinggal | _Daerah Endemis Malaria_ → `Observation.valueCodeableConcept.coding` (209, tanpa BQ) |
| 13 | 218–648 | QuestionnaireResponse | – | – | _Apakah anak menderita batuk dan/atau sukar bernapas?_ → `QuestionnaireResponse.item.item.item.linkId` (247, tanpa BQ)<br>_Apakah anak menderita diare_ → `QuestionnaireResponse.item.item.item.linkId` (272, tanpa BQ)<br>_Apakah anak demam_ → `QuestionnaireResponse.item.item.item.linkId` (300, tanpa BQ)<br>_Apakah pernah menderita malaria atau minum obat anti malaria?_ → `QuestionnaireResponse.item.item.item.item.item.linkId` (311, tanpa BQ)<br>_Apakah demam setiap hari?_ → `QuestionnaireResponse.item.item.item.item.item.linkId` (338, tanpa BQ)<br>_Apakah anak menderita campak dalam 3 bulan terakhir?_ → `QuestionnaireResponse.item.item.item.linkId` (367, tanpa BQ)<br>_Apakah anak mempunyai masalah telinga_ → `QuestionnaireResponse.item.item.item.linkId` (415, tanpa BQ)<br>_Jika anak berusia > 6 bulan, apakah BB anak < 4 kg?_ → `QuestionnaireResponse.item.item.item.item.linkId` (438, tanpa BQ)<br>_Lihat dan raba, apakah ada edema bilateral yang bersifat pitting_ → `QuestionnaireResponse.item.item.item.linkId` (442, tanpa BQ)<br>_Apakah ada komplikasi medis_ → `QuestionnaireResponse.item.item.item.item.linkId` (459, tanpa BQ)<br>_Umur anak_ → `QuestionnaireResponse.item.item.item.linkId` (484, tanpa BQ)<br>_Apakah ditemukan pucat/sangat pucat pada telapak tangan, konjungtiva, bibir, lidah dan bantalan kuku_ → `QuestionnaireResponse.item.item.item.linkId` (503, tanpa BQ)<br>_Apakah ibu pernah test HIV?_ → `QuestionnaireResponse.item.item.item.linkId` (527, tanpa BQ)<br>_Apakah anak pernah test HIV?_ → `QuestionnaireResponse.item.item.item.linkId` (537, tanpa BQ)<br>_Apakah anak sedang mendapat ASI pada saat tes HIV atau 6 minggu sebelum dilakukan tes HIV?_ → `QuestionnaireResponse.item.item.item.item.linkId` (557, tanpa BQ)<br>_Jika mendapat ASI, apakah ibu dan anak saat ini mendapat ARV profilaksis?_ → `QuestionnaireResponse.item.item.item.item.linkId` (561, tanpa BQ)<br>_Apakah ibu menyusui anak ini?_ → `QuestionnaireResponse.item.item.item.linkId` (602, tanpa BQ)<br>_Jika YA, berapa kali sehari_ → `QuestionnaireResponse.item.item.item.item.linkId` (606, tanpa BQ)<br>_Apakah ibu menyusui juga pada malam hari?_ → `QuestionnaireResponse.item.item.item.item.linkId` (609, tanpa BQ)<br>_Apakah anak mendapat makanan atau minuman lain?_ → `QuestionnaireResponse.item.item.item.linkId` (613, tanpa BQ)<br>_Jika Ya, makanan dan minuman apa?_ → `QuestionnaireResponse.item.item.item.item.linkId` (617, tanpa BQ)<br>_Berapa kali sehari_ → `QuestionnaireResponse.item.item.item.item.linkId` (620, tanpa BQ)<br>_Alat apa yang digunakan untuk memberi makan/minum anak?_ → `QuestionnaireResponse.item.item.item.item.linkId` (623, tanpa BQ)<br>_Berapa banyak makanan/minuman yang diberikan kepada anak?_ → `QuestionnaireResponse.item.item.item.linkId` (632, tanpa BQ)<br>_Apakah anak mendapat porsi sendiri?_ → `QuestionnaireResponse.item.item.item.linkId` (635, tanpa BQ)<br>_Siapa yang memberi makan anak dan bagaimana caranya?_ → `QuestionnaireResponse.item.item.item.linkId` (639, tanpa BQ)<br>_Selama anak sakit ini, apakah pemberian makanan berubah?_ → `QuestionnaireResponse.item.item.item.linkId` (642, tanpa BQ)<br>_Jika YA, bagaimana?_ → `QuestionnaireResponse.item.item.item.item.linkId` (646, tanpa BQ) |
| 14 | 649–711 | Observation | OC000088 | Pemeriksaan tanda bahaya umum | _Pemeriksaan Segitiga Asesmen Gawat Anak_ → `Observation.valueBoolean` (652, tanpa BQ)<br>_Apakah anak bisa minum atau menyusu_ → `Observation.component.code.coding` (654, tanpa BQ)<br>_Apakah anak memuntahkan semua makanan dan minuman?_ → `Observation.component.code.coding` (657, tanpa BQ)<br>_Apakah anak pernah kejang selama sakit ini?_ → `Observation.component.code.coding` (660, tanpa BQ)<br>_Apakah anak kejang?_ → `Observation.component.code.coding` (663, tanpa BQ)<br>_Apakah anak tidak dapat berinteraksi dengan lingkungan atau tidak sadar?_ → `Observation.component.code.coding` (666, tanpa BQ)<br>_Apakah anak gelisah, rewel, dan tidak dapat ditenangkan?_ → `Observation.component.code.coding` (669, tanpa BQ)<br>_Apakah anak gelisah, rewel, dan tidak dapat ditenangkan?_ → `Observation.component.code.coding` (672, tanpa BQ)<br>_Apakah anak gelisah, rewel, dan tidak dapat ditenangkan?_ → `Observation.component.code.coding` (675, tanpa BQ)<br>_Apakah anak mempunyai pandangan kosong atau mata tidak membuka?_ → `Observation.component.code.coding` (678, tanpa BQ)<br>_Apakah anak tidak bersuara atau justru menangis melengking?_ → `Observation.component.code.coding` (681, tanpa BQ)<br>_Apakah terdapat tarikan dinding dada ke dalam?_ → `Observation.component.code.coding` (684, tanpa BQ)<br>_Apakah terdengar stridor?_ → `Observation.component.code.coding` (687, tanpa BQ)<br>_Apakah terdapat napas cuping hidung?_ → `Observation.component.code.coding` (690, tanpa BQ)<br>_Apakah anak mencari posisi paling nyaman dan menolak berbaring?_ → `Observation.component.code.coding` (693, tanpa BQ)<br>_Apakah anak tampak pucat?_ → `Observation.component.code.coding` (696, tanpa BQ)<br>_Apakah tampak warna biru (sianosis)?_ → `Observation.component.code.coding` (699, tanpa BQ)<br>_Apakah tampak gambaran kutis marmorata atau kulit seperti marmer?_ → `Observation.component.code.coding` (702, tanpa BQ) |
| 15 | 712–722 | Procedure | – | – | _Tindakan Segitiga Asesmen Gawat Anak_ → `Procedure.category.coding` (712, tanpa BQ) |
| 16 | 723–735 | Observation | OC000089 | Klasifikasi status kegawatan | _Klasifikasi Segitiga Asesmen Gawat Anak_ → `Observation.valueCodeableConcept.coding` (726, tanpa BQ) |
| 17 | 736–742 | Condition | – | – | _Kondisi Batuk dan/atau Sukar Bernapas?_ → `Condition.clinicalStatus.coding` (736, tanpa BQ) |
| 18 | 743–755 | Observation | – | – | _Lama Batuk dan/atau Sukar Bernapas_ → `Observation.valueQuantity.value` (746, tanpa BQ) |
| 19 | 756–768 | Observation | 9279-1 | Respiratory rate | _Jumlah nafas_ → `Observation.valueQuantity.value` (759, tanpa BQ) |
| 20 | 769–781 | Observation | 103228002 | Hemoglobin saturation with oxygen | _Saturasi oksigen_ → `Observation.valueQuantity.value` (772, tanpa BQ) |
| 21 | 782–792 | Observation | OC000090 | Pemeriksaan tanda dan gejala sukar bernafas | _Pemeriksaan Batuk dan/atau Sukar Bernapas_ → `Observation.valueBoolean` (785, tanpa BQ)<br>_Apakah ada tarikan dinding dada ke dalam?_ → `Observation.component.code.coding` (787, tanpa BQ)<br>_Apakah ada wheezing?_ → `Observation.component.code.coding` (790, tanpa BQ) |
| 22 | 793–805 | Observation | OC000091 | Klasifikasi batuk dan/atau sukar bernapas | _Klasifikasi Batuk dan/atau Sukar Bernapas_ → `Observation.valueCodeableConcept.coding` (796, tanpa BQ) |
| 23 | 806–816 | Procedure | – | – | _Tindakan Batuk dan/atau Sukar Bernapas_ → `Procedure.category.coding` (806, tanpa BQ) |
| 24 | 817–823 | Condition | 62315008 | Diarrhea | _Kondisi Diare_ → `Condition.clinicalStatus.coding` (817, tanpa BQ) |
| 25 | 824–836 | Observation | OC000113 | Durasi diare | _Durasi Diare_ → `Observation.valueQuantity.value` (827, tanpa BQ) |
| 26 | 837–848 | Observation | 405729008 | Hematochezia | _Apakah ada darah dalam tinja?_ → `Observation.valueBoolean` (840, tanpa BQ) |
| 27 | 849–871 | Observation | OC000097 | Pemeriksaan tanda dan gejala diare | _Pemeriksaan Diare_ → `Observation.valueBoolean` (852, tanpa BQ)<br>_Letargi atau tidak sadar?_ → `Observation.component.code.coding` (854, tanpa BQ)<br>_Rewel/mudah marah?_ → `Observation.component.code.coding` (857, tanpa BQ)<br>_Mata cekung?_ → `Observation.component.code.coding` (860, tanpa BQ)<br>_Tidak bisa atau malas minum?_ → `Observation.component.code.coding` (863, tanpa BQ)<br>_Haus, minum dengan lahap?_ → `Observation.component.code.coding` (866, tanpa BQ)<br>_Cubit kulit perut untuk mengetahui turgor. Apakah kembalinya:_ → `Observation.component.code.coding` (869, tanpa BQ) |
| 28 | 872–887 | Observation | OC000098 | Klasifikasi diare | _Klasifikasi Diare_ → `Observation.valueCodeableConcept.coding` (875, tanpa BQ) |
| 29 | 888–898 | Procedure | – | – | _Tindakan Diare_ → `Procedure.category.coding` (888, tanpa BQ) |
| 30 | 899–908 | Condition | 386661006 | Fever | _Kondisi Demam_ → `Condition.clinicalStatus.coding` (899, tanpa BQ)<br>_Apakah_ → `Condition.evidence.code.coding` (906, tanpa BQ) |
| 31 | 909–921 | Observation | OC000099 | Status daerah endemis malaria tempat tinggal | _Daerah Endemis Malaria_ → `Observation.valueCodeableConcept.coding` (912, tanpa BQ) |
| 32 | 922–934 | Observation | 81264-4 | Fever duration | _Lama Demam_ → `Observation.valueQuantity.value` (925, tanpa BQ) |
| 33 | 935–945 | Observation | OC000121 | Pemeriksaan tanda dan gejala demam | _Pemeriksaan Tanda/Gejala Demam_ → `Observation.valueBoolean` (938, tanpa BQ)<br>_Lihat dan raba, apakah ada kaku kuduk?_ → `Observation.component.code.coding` (940, tanpa BQ)<br>_Apakah ada penyebab lain dari demam?_ → `Observation.component.code.coding` (943, tanpa BQ) |
| 34 | 946–955 | ServiceRequest | – | – | _RDT_ → `ServiceRequest.category` (946, tanpa BQ) |
| 35 | 959–966 | Specimen | – | – | – |
| 36 | 967–978 | Observation | 76772-3 | Plasmodium falciparum Ag [Presence] in Blood by Rapid immunoassay | _Hasil tes RDT Malaria_ → `Observation.valueCodeableConcept.coding` (970, tanpa BQ) |
| 37 | 979–990 | DiagnosticReport | 76772-3 | Plasmodium falciparum Ag [Presence] in Blood by Rapid immunoassay | – |
| 38 | 991–1000 | ServiceRequest | – | – | _Mikroskopis_ → `ServiceRequest.category` (991, tanpa BQ) |
| 39 | 1004–1011 | Specimen | – | – | – |
| 40 | 1012–1023 | Observation | 32700-7 | Microscopic observation [Identifier] in Blood by Malaria smear | _Hasil tes Mikroskopis Malaria_ → `Observation.valueCodeableConcept.coding` (1015, tanpa BQ) |
| 41 | 1024–1035 | DiagnosticReport | 32700-7 | Microscopic observation [Identifier] in Blood by Malaria smear | – |
| 42 | 1036–1050 | Observation | OC000100 | Klasifikasi demam | _Klasifikasi Demam dan Malaria_ → `Observation.valueCodeableConcept.coding` (1039, tanpa BQ) |
| 43 | 1051–1061 | Procedure | – | – | _Tindakan Demam atau Malaria_ → `Procedure.category.coding` (1051, tanpa BQ) |
| 44 | 1062–1068 | Condition | 14189004 | Measles | _Kondisi Campak_ → `Condition.clinicalStatus.coding` (1062, tanpa BQ) |
| 45 | 1069–1091 | Observation | OC000101 | Pemeriksaan tanda dan gejala campak | _Pemeriksaan Tanda dan Gejala Campak_ → `Observation.valueBoolean` (1072, tanpa BQ)<br>_Ruam kemerahan di kulit yang menyeluruh_ → `Observation.component.code.coding` (1074, tanpa BQ)<br>_Terdapat salah satu tanda berikut: batuk, pilek, mata merah_ → `Observation.component.code.coding` (1077, tanpa BQ)<br>_Apakah ada ada luka di mulut?_ → `Observation.component.code.coding` (1080, tanpa BQ)<br>_Apakah lukanya dalam/luas?_ → `Observation.component.code.coding` (1083, tanpa BQ)<br>_Apakah ada nanah pada mata_ → `Observation.component.code.coding` (1086, tanpa BQ)<br>_Apakah ada kekeruhan pada kornea_ → `Observation.component.code.coding` (1089, tanpa BQ) |
| 46 | 1092–1104 | Observation | OC000102 | Klasifikasi campak | _Klasifikasi Campak_ → `Observation.valueCodeableConcept.coding` (1095, tanpa BQ) |
| 47 | 1105–1115 | Procedure | – | – | _Tindakan Campak_ → `Procedure.category.coding` (1105, tanpa BQ) |
| 48 | 1116–1192 | Observation | OC000104 | Pemeriksaan infeksi dengue | _Pemeriksaan Infeksi Dengue_ → `Observation.valueBoolean` (1119, tanpa BQ)<br>_Apakah demam mendadak tinggi dan terus menerus?_ → `Observation.component.code.coding` (1121, tanpa BQ)<br>_Apakah badan teraba dingin?_ → `Observation.component.code.coding` (1124, tanpa BQ)<br>_Apakah anak lemas/gelisah?_ → `Observation.component.code.coding` (1127, tanpa BQ)<br>_Adakah mual?_ → `Observation.component.code.coding` (1130, tanpa BQ)<br>_Adakah muntah?_ → `Observation.component.code.coding` (1133, tanpa BQ)<br>_Apakah muntahnya terus menerus?_ → `Observation.component.code.coding` (1136, tanpa BQ)<br>_Adakah nyeri perut?_ → `Observation.component.code.coding` (1139, tanpa BQ)<br>_Adakah perdarahan berupa mimisan/muntah darah atau coklat seperti kopi/BAB berdarah/berwarna hitam?_ → `Observation.component.code.coding` (1142, tanpa BQ)<br>_Apakah muncul ruam?_ → `Observation.component.code.coding` (1145, tanpa BQ)<br>_Apakah ada rasa sakit dan nyeri badan?_ → `Observation.component.code.coding` (1148, tanpa BQ)<br>_Apakah BAK terakhir ≥ 6 jam?_ → `Observation.component.code.coding` (1151, tanpa BQ)<br>_Kaki/tangan tampak pucat_ → `Observation.component.code.coding` (1154, tanpa BQ)<br>_Waktu pengisian kapiler > 2 detik_ → `Observation.component.code.coding` (1157, tanpa BQ)<br>_Kaki/tangan teraba dingin_ → `Observation.component.code.coding` (1160, tanpa BQ)<br>_Nadi lemah atau tidak teraba_ → `Observation.component.code.coding` (1163, tanpa BQ)<br>_Nadi cepat_ → `Observation.component.code.coding` (1166, tanpa BQ)<br>_Apakah ada nyeri perut (tekan perut kanan atas)?_ → `Observation.component.code.coding` (1169, tanpa BQ)<br>_Apakah ada klinis akumulasi cairan?_ → `Observation.component.code.coding` (1172, tanpa BQ)<br>_Perdarahan kulit (petekie), perdarahan hidung (mimisan)?_ → `Observation.component.code.coding` (1175, tanpa BQ)<br>_Perdarahan kulit (petekie), perdarahan hidung (mimisan)?_ → `Observation.component.code.coding` (1178, tanpa BQ)<br>_Ikterik_ → `Observation.component.code.coding` (1181, tanpa BQ)<br>_Letargi, gelisah_ → `Observation.component.code.coding` (1184, tanpa BQ)<br>_Sesak napas, napas cepat_ → `Observation.component.code.coding` (1187, tanpa BQ)<br>_Apakah ada pembesaran hepar > 2cm_ → `Observation.component.code.coding` (1190, tanpa BQ) |
| 49 | 1193–1204 | Observation | 38520-3 | Capillary fragility | _Uji Tourniquet jika tidak syok dan tidak ada perdarahan. Hasil:_ → `Observation.valueCodeableConcept.coding` (1196, tanpa BQ) |
| 50 | 1205–1214 | ServiceRequest | – | – | _Hemoglobin_ → `ServiceRequest.category` (1205, tanpa BQ) |
| 51 | 1218–1225 | Specimen | – | – | – |
| 52 | 1226–1237 | Observation | 718-7 | Hemoglobin [Mass/volume] in Blood | _Hemoglobin_ → `Observation.valueQuantity.value` (1229, tanpa BQ) |
| 53 | 1238–1249 | DiagnosticReport | 718-7 | Hemoglobin [Mass/volume] in Blood | – |
| 54 | 1250–1259 | ServiceRequest | – | – | _Hematokrit_ → `ServiceRequest.category` (1250, tanpa BQ) |
| 55 | 1263–1270 | Specimen | – | – | – |
| 56 | 1271–1282 | Observation | 20570-8 | Hematocrit [Volume Fraction] of Blood | _Hematokrit_ → `Observation.valueQuantity.value` (1274, tanpa BQ) |
| 57 | 1283–1294 | DiagnosticReport | 20570-8 | Hematocrit [Volume Fraction] of Blood | – |
| 58 | 1295–1304 | ServiceRequest | – | – | _Leukosit_ → `ServiceRequest.category` (1295, tanpa BQ) |
| 59 | 1308–1315 | Specimen | – | – | – |
| 60 | 1316–1327 | Observation | 26464-8 | Leukocytes [#/volume] in Blood | _Leukosit_ → `Observation.valueQuantity.value` (1319, tanpa BQ) |
| 61 | 1328–1339 | DiagnosticReport | 26464-8 | Leukocytes [#/volume] in Blood | – |
| 62 | 1340–1349 | ServiceRequest | – | – | _Trombosit_ → `ServiceRequest.category` (1340, tanpa BQ) |
| 63 | 1353–1360 | Specimen | – | – | – |
| 64 | 1361–1372 | Observation | 26515-7 | Platelets [#/volume] in Blood | _Trombosit_ → `Observation.valueQuantity.value` (1364, tanpa BQ) |
| 65 | 1373–1384 | DiagnosticReport | 26515-7 | Platelets [#/volume] in Blood | – |
| 66 | 1385–1394 | ServiceRequest | – | – | _NS-1_ → `ServiceRequest.category` (1385, tanpa BQ) |
| 67 | 1398–1405 | Specimen | – | – | – |
| 68 | 1406–1417 | Observation | 75377-2 | Dengue virus NS1 Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | _NS-1_ → `Observation.valueCodeableConcept.coding` (1409, tanpa BQ) |
| 69 | 1418–1429 | DiagnosticReport | 75377-2 | Dengue virus NS1 Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | – |
| 70 | 1430–1443 | Observation | OC000105 | Klasifikasi infeksi dengue | _Klasifikasi Infeksi Dengue_ → `Observation.valueCodeableConcept.coding` (1433, tanpa BQ) |
| 71 | 1444–1454 | Procedure | – | – | _Tindakan Infeksi Dengue_ → `Procedure.category.coding` (1444, tanpa BQ) |
| 72 | 1455–1461 | Condition | 300197009 | Ear problem | _Kondisi Masalah Telinga_ → `Condition.clinicalStatus.coding` (1455, tanpa BQ) |
| 73 | 1462–1484 | Observation | OC000106 | Pemeriksaan tanda dan gejala masalah telinga | _Pemeriksaan Tanda dan Gejala Masalah Telinga_ → `Observation.valueBoolean` (1465, tanpa BQ)<br>_Apakah anak mempunyai masalah telinga?_ → `Observation.component.code.coding` (1467, tanpa BQ)<br>_Apakah ada nyeri telinga?_ → `Observation.component.code.coding` (1470, tanpa BQ)<br>_Apakah ada rasa penuh di telinga?_ → `Observation.component.code.coding` (1473, tanpa BQ)<br>_Adakah cairan/nanah keluar dari telinga?_ → `Observation.component.code.coding` (1476, tanpa BQ)<br>_Lihat, adakah cairan/nanah keluar dari telinga?_ → `Observation.component.code.coding` (1479, tanpa BQ)<br>_Raba, adakah pembengkakan yang nyeri di belakang telinga?_ → `Observation.component.code.coding` (1482, tanpa BQ) |
| 74 | 1485–1498 | Observation | OC000107 | Klasifikasi masalah telinga | _Klasifikasi Masalah Telinga_ → `Observation.valueCodeableConcept.coding` (1488, tanpa BQ) |
| 75 | 1499–1509 | Procedure | – | – | _Tindakan Masalah Telinga_ → `Procedure.category.coding` (1499, tanpa BQ) |
| 76 | 1510–1522 | Observation | 284521000 | Pitting edema | _Derajat Edema_ → `Observation.valueCodeableConcept.coding` (1513, tanpa BQ) |
| 77 | 1523–1559 | Observation | 1153600001 | Weight for height z-score | _Tentukan BB/PB (TB) (sesuai grafik IMT/U)_ → `Observation.valueRange.high.value` (1527, tanpa BQ) |
| 78 | 1560–1580 | Observation | 284473002 | Mid upper arm circumference | _Tentukan lingkar lengan atas (LiLA) untuk umur 6 bulan atau lebih_ → `Observation.valueRange.high.value` (1563, tanpa BQ) |
| 79 | 1581–1592 | Observation | OV000253 | Terlalu lemah untuk menyusu | _Apakah anak terlalu lemah untuk menyusu?_ → `Observation.valueBoolean` (1584, tanpa BQ) |
| 80 | 1593–1604 | Observation | 271398006 | Weight steady | _Berat badan tidak naik atau turun_ → `Observation.valueBoolean` (1596, tanpa BQ) |
| 81 | 1605–1621 | Observation | OC000108 | Klasifikasi status gizi | _Klasifikasi Status Gizi_ → `Observation.valueCodeableConcept` (1608, tanpa BQ) |
| 82 | 1622–1632 | Procedure | – | – | _Tindakan Status Gizi_ → `Procedure.category.coding` (1622, tanpa BQ) |
| 83 | 1633–1659 | Observation | 1153604005 | Body height for age z-score | _Tentukan panjang badan (PB) atau tinggi badan (TB) menurut umur sesuai dengan jenis kelamin:_ → `Observation.valueRange.high.value` (1637, tanpa BQ) |
| 84 | 1660–1670 | Procedure | – | – | _Tindakan PB/U atau TB/U_ → `Procedure.category.coding` (1660, tanpa BQ) |
| 85 | 1671–1691 | Observation | 1153594009 | Head circumference for age z-score | _Tentukan lingkar kepala menurut umur sesuai dengan jenis kelamin:_ → `Observation.valueRange.high.value` (1674, tanpa BQ) |
| 86 | 1692–1702 | Procedure | – | – | _Tindakan LK/U_ → `Procedure.category.coding` (1692, tanpa BQ) |
| 87 | 1703–1715 | Observation | OC000111 | Klasifikasi anemia | _Klasifikasi Anemia_ → `Observation.valueCodeableConcept.coding` (1706, tanpa BQ) |
| 88 | 1716–1725 | ServiceRequest | – | – | _Hemoglobin_ → `ServiceRequest.category` (1716, tanpa BQ) |
| 89 | 1729–1736 | Specimen | – | – | – |
| 90 | 1737–1748 | Observation | 718-7 | Hemoglobin [Mass/volume] in Blood | _Hasil pemeriksaan Hb_ → `Observation.valueQuantity.value` (1740, tanpa BQ) |
| 91 | 1749–1760 | DiagnosticReport | 718-7 | Hemoglobin [Mass/volume] in Blood | – |
| 92 | 1761–1771 | Procedure | – | – | _Tindakan Anemia_ → `Procedure.category.coding` (1761, tanpa BQ) |
| 93 | 1772–1783 | Observation | PC000013 | Riwayat tes HIV ibu | _Apakah ibu pernah test HIV?_ → `Observation.valueBoolean` (1775, tanpa BQ) |
| 94 | 1784–1795 | Observation | SP000247 | Hasil Tes HIV Ibu | _Hasil test HIV ibu_ → `Observation.valueCodeableConcept.coding` (1787, tanpa BQ) |
| 95 | 1796–1806 | Procedure | PC000014 | Riwayat tes HIV anak | _Apakah anak pernah test HIV?_ → `Procedure.category.coding` (1796, tanpa BQ) |
| 96 | 1807–1818 | Observation | SP000248 | Hasil Tes HIV Anak | _Hasil test HIV anak_ → `Observation.valueCodeableConcept.coding` (1810, tanpa BQ) |
| 97 | 1819–1830 | Observation | OC000084 | Tes virologis HIV anak | _Hasil test Virologi_ → `Observation.valueCodeableConcept.coding` (1822, tanpa BQ) |
| 98 | 1831–1842 | Observation | OC000083 | Tes serologis HIV anak | _Hasil test Serologi_ → `Observation.valueCodeableConcept.coding` (1834, tanpa BQ) |
| 99 | 1843–1854 | Observation | 63895-7 | Breastfeeding status | _Status Menyusu Anak_ → `Observation.valueBoolean` (1846, tanpa BQ) |
| 100 | 1855–1867 | Observation | 254387007 | Human immunodeficiency virus infection classification systems | _Klasifikasi Pemeriksaan HIV_ → `Observation.valueCodeableConcept.coding` (1858, tanpa BQ) |
| 101 | 1868–1878 | Procedure | – | – | _Tindakan HIV_ → `Procedure.category.coding` (1868, tanpa BQ) |
| 102 | 1879–1894 | Immunization | – | – | _HB 0_ → `Immunization.status` (1879, tanpa BQ)<br>_DPT-HB-HiB 2_ → `Immunization.status` (1893, tanpa BQ) |
| 103 | 1895–1910 | Immunization | – | – | _Japanese Encephalitis (lanjutan)_ → `Immunization.status` (1909, tanpa BQ) |
| 104 | 1911–1923 | Immunization | – | – | _BCG_ → `Immunization.status` (1922, tanpa BQ) |
| 105 | 1924–1936 | Immunization | – | – | _OPV 2_ → `Immunization.status` (1935, tanpa BQ) |
| 106 | 1937–1950 | Immunization | – | – | _PCV 3 (lanjutan)_ → `Immunization.status` (1949, tanpa BQ) |
| 107 | 1951–1964 | Immunization | – | – | _OPV 0_ → `Immunization.status` (1963, tanpa BQ) |
| 108 | 1965–1978 | Immunization | – | – | _PCV 2_ → `Immunization.status` (1977, tanpa BQ) |
| 109 | 1979–1992 | Immunization | – | – | _DPT-HB-Hib (lanjutan)_ → `Immunization.status` (1991, tanpa BQ) |
| 110 | 1993–2008 | Immunization | – | – | _DPT-HB-Hib-1_ → `Immunization.status` (2007, tanpa BQ) |
| 111 | 2009–2024 | Immunization | – | – | _DPT-HB-HiB 3_ → `Immunization.status` (2023, tanpa BQ) |
| 112 | 2025–2040 | Immunization | – | – | _Campak Rubella (lanjutan)_ → `Immunization.status` (2039, tanpa BQ) |
| 113 | 2041–2054 | Immunization | – | – | _OPV 1_ → `Immunization.status` (2053, tanpa BQ) |
| 114 | 2055–2068 | Immunization | – | – | _OPV3/IPV_ → `Immunization.status` (2067, tanpa BQ) |
| 115 | 2069–2082 | Immunization | – | – | – |
| 116 | 2083–2096 | Immunization | – | – | _PCV 1_ → `Immunization.status` (2095, tanpa BQ) |
| 117 | 2097–2110 | Immunization | – | – | _Campak Rubella_ → `Immunization.status` (2109, tanpa BQ) |
| 118 | 2111–2122 | Immunization | – | – | – |
| 119 | 2123–2134 | Observation | OC000114 | Membutuhkan suplemen vitamin A | _Anak Membutuhkan Vitamin A_ → `Observation.valueBoolean` (2126, tanpa BQ) |
| 120 | 2135–2143 | Procedure | 767224000 | Administration of vitamin A | _Prosedur Pemberian Vitamin A_ → `Procedure.category.coding` (2135, tanpa BQ) |
| 121 | 2144–2170 | MedicationRequest | 92000809 | Retinol Palmitate 200.000 IU Kapsul Lunak | _Jml Vit A_ → `MedicationRequest.contained.resourceType` (2144, tanpa BQ) |
| 122 | 2171–2196 | MedicationDispense | 93018284 | Retinol Palmitate 200.000 IU Kapsul Lunak (Umum) | – |
| 123 | 2197–2223 | MedicationRequest | 92000354 | Retinol Palmitate 100.000 IU Kapsul Lunak | – |
| 124 | 2224–2249 | MedicationDispense | 93018284 | Retinol Palmitate 100.000 IU Kapsul Lunak (Umum) | – |
| 125 | 2250–2261 | ServiceRequest | – | – | _Kunjungan Ulang_ → `ServiceRequest.category` (2250, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 53 |
| Immunization | 17 |
| Procedure | 14 |
| ServiceRequest | 9 |
| Specimen | 8 |
| DiagnosticReport | 8 |
| Condition | 7 |
| MedicationRequest | 2 |
| MedicationDispense | 2 |
| Patient | 1 |
| Practitioner | 1 |
| RelatedPerson | 1 |
| Encounter | 1 |
| QuestionnaireResponse | 1 |
| **Total** | **125** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 115 | Condition | `Condition.code.coding` | SP000273 | Integrated management of childhood illness | http://terminology.kemkes.go.id/sp |
| 2 | 135 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 3 | 138 | Observation | `Observation.component.code.coding` | SP000020 | Umur Bulan | http://terminology.kemkes.go.id/sp |
| 4 | 141 | Observation | `Observation.component.code.coding` | SP000021 | Umur Hari | http://terminology.kemkes.go.id/sp |
| 5 | 153 | Observation | `Observation.code.coding` | 284473002 | Mid upper arm circumference | http://snomed.info/sct |
| 6 | 165 | Observation | `Observation.code.coding` | 9843-4 | Head Occipital-frontal circumference | http://loinc.org |
| 7 | 177 | Observation | `Observation.code.coding` | 8310-5 | Body temperature | http://loinc.org |
| 8 | 196 | Observation | `Observation.code.coding` | SP000261 | Tipe Kunjungan | http://terminology.kemkes.go.id/sp |
| 9 | 197 | Observation | `Observation.valueCodeableConcept.coding` | SP000262 | Kunjungan Pertama | http://terminology.kemkes.go.id/sp |
| 10 | 198 | Observation | `Observation.valueCodeableConcept.coding` | SP000263 | Kunjungan Ulang | http://terminology.kemkes.go.id/sp |
| 11 | 208 | Observation | `Observation.code.coding` | OC000099 | Status daerah endemis malaria tempat tinggal | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 12 | 210 | Observation | `Observation.valueCodeableConcept.coding` | OV000221 | Daerah non endemis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 13 | 505 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | OV000321 | Sangat pucat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 14 | 506 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | 1237486008 | Pale discoloration of entire skin of body | http://snomed.info/sct |
| 15 | 507 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | OV000322 | Tidak pucat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 16 | 651 | Observation | `Observation.code.coding` | OC000088 | Pemeriksaan tanda bahaya umum | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 17 | 654 | Observation | `Observation.component.code.coding` | 288853006 | Able to drink | http://snomed.info/sct |
| 18 | 657 | Observation | `Observation.component.code.coding` | OV000207 | Anak memuntahkan semua makanan dan minuman | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 19 | 660 | Observation | `Observation.component.code.coding` | SP000260 | Riwayat Kejang Selama Sakit | http://terminology.kemkes.go.id/sp |
| 20 | 663 | Observation | `Observation.component.code.coding` | 91175000 | Seizure | http://snomed.info/sct |
| 21 | 666 | Observation | `Observation.component.code.coding` | 422768004 | Unresponsive | http://snomed.info/sct |
| 22 | 669 | Observation | `Observation.component.code.coding` | 130987000 | Acute confusion | http://snomed.info/sct |
| 23 | 672 | Observation | `Observation.component.code.coding` | OV000171 | Rewel | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 24 | 675 | Observation | `Observation.component.code.coding` | OV000208 | Anak tidak dapat ditenangkan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 25 | 678 | Observation | `Observation.component.code.coding` | SP000259 | Pandangan Kosong atau Mata Tidak Membuka | http://terminology.kemkes.go.id/sp |
| 26 | 681 | Observation | `Observation.component.code.coding` | SP000258 | Anak Tidak Bersuara atau Menangis Melengking | http://terminology.kemkes.go.id/sp |
| 27 | 684 | Observation | `Observation.component.code.coding` | 67909005 | Chest wall retraction | http://snomed.info/sct |
| 28 | 687 | Observation | `Observation.component.code.coding` | 70407001 | Stridor | http://snomed.info/sct |
| 29 | 690 | Observation | `Observation.component.code.coding` | 248568003 | Nasal flaring | http://snomed.info/sct |
| 30 | 693 | Observation | `Observation.component.code.coding` | OV000211 | Anak mencari posisi paling nyaman dan menolak berbaring | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 31 | 696 | Observation | `Observation.component.code.coding` | 1237486008 | Pale discoloration of entire skin of body | http://snomed.info/sct |
| 32 | 699 | Observation | `Observation.component.code.coding` | 3415004 | Cyanosis | http://snomed.info/sct |
| 33 | 702 | Observation | `Observation.component.code.coding` | 26825009 | Cutis marmorata | http://snomed.info/sct |
| 34 | 725 | Observation | `Observation.code.coding` | OC000089 | Klasifikasi status kegawatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 35 | 726 | Observation | `Observation.valueCodeableConcept.coding` | 359746009 | Patient's condition stable | http://snomed.info/sct |
| 36 | 727 | Observation | `Observation.valueCodeableConcept.coding` | 410429000 | Cardiac arrest | http://snomed.info/sct |
| 37 | 728 | Observation | `Observation.valueCodeableConcept.coding` | OV000137 | Penyakit sangat berat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 38 | 758 | Observation | `Observation.code.coding` | 9279-1 | Respiratory rate | http://loinc.org |
| 39 | 771 | Observation | `Observation.code.coding` | 103228002 | Hemoglobin saturation with oxygen | http://snomed.info/sct |
| 40 | 784 | Observation | `Observation.code.coding` | OC000090 | Pemeriksaan tanda dan gejala sukar bernafas | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 41 | 787 | Observation | `Observation.component.code.coding` | 67909005 | Chest wall retraction | http://snomed.info/sct |
| 42 | 790 | Observation | `Observation.component.code.coding` | 56018004 | Wheezing | http://snomed.info/sct |
| 43 | 795 | Observation | `Observation.code.coding` | OC000091 | Klasifikasi batuk dan/atau sukar bernapas | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 44 | 796 | Observation | `Observation.valueCodeableConcept.coding` | OV000287 | Pneumonia berat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 45 | 797 | Observation | `Observation.valueCodeableConcept.coding` | 233604007 | Pneumonia | http://snomed.info/sct |
| 46 | 798 | Observation | `Observation.valueCodeableConcept.coding` | OV000288 | Batuk bukan pneumonia | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 47 | 819 | Condition | `Condition.code.coding` | 62315008 | Diarrhea | http://snomed.info/sct |
| 48 | 826 | Observation | `Observation.code.coding` | OC000113 | Durasi diare | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 49 | 839 | Observation | `Observation.code.coding` | 405729008 | Hematochezia | http://snomed.info/sct |
| 50 | 851 | Observation | `Observation.code.coding` | OC000097 | Pemeriksaan tanda dan gejala diare | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 51 | 854 | Observation | `Observation.component.code.coding` | 214264003 | Lethargy | http://snomed.info/sct |
| 52 | 857 | Observation | `Observation.component.code.coding` | SP000257 | Rewel atau Mudah Marah | http://terminology.kemkes.go.id/sp |
| 53 | 860 | Observation | `Observation.component.code.coding` | 246923005 | Sunken eyes | http://snomed.info/sct |
| 54 | 863 | Observation | `Observation.component.code.coding` | SP000256 | Tidak Bisa Minum atau Malas Minum | http://terminology.kemkes.go.id/sp |
| 55 | 866 | Observation | `Observation.component.code.coding` | 17173007 | Excessive thirst | http://snomed.info/sct |
| 56 | 869 | Observation | `Observation.component.code.coding` | SP000255 | Turgor Kulit Perut | http://terminology.kemkes.go.id/sp |
| 57 | 870 | Observation | `Observation.component.valueCodeableConcept.coding` | OV000181 | Cubitan kulit perut kembalinya sangat lambat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 58 | 871 | Observation | `Observation.component.valueCodeableConcept.coding` | OV000182 | Cubitan kulit perut kembalinya lambat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 59 | 874 | Observation | `Observation.code.coding` | OC000098 | Klasifikasi diare | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 60 | 875 | Observation | `Observation.valueCodeableConcept.coding` | OV000217 | Diare persisten berat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 61 | 876 | Observation | `Observation.valueCodeableConcept.coding` | OV000218 | Diare persisten | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 62 | 877 | Observation | `Observation.valueCodeableConcept.coding` | 46799006 | Dysenteric diarrhea | http://snomed.info/sct |
| 63 | 878 | Observation | `Observation.valueCodeableConcept.coding` | OV000214 | Diare dehidrasi berat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 64 | 879 | Observation | `Observation.valueCodeableConcept.coding` | OV000215 | Diare dehidrasi ringan/sedang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 65 | 880 | Observation | `Observation.valueCodeableConcept.coding` | OV000186 | Diare tanpa dehidrasi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 66 | 901 | Condition | `Condition.code.coding` | 386661006 | Fever | http://snomed.info/sct |
| 67 | 911 | Observation | `Observation.code.coding` | OC000099 | Status daerah endemis malaria tempat tinggal | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 68 | 912 | Observation | `Observation.valueCodeableConcept.coding` | OV000219 | Daerah endemis tinggi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 69 | 913 | Observation | `Observation.valueCodeableConcept.coding` | OV000220 | Daerah endemis rendah | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 70 | 914 | Observation | `Observation.valueCodeableConcept.coding` | OV000221 | Daerah non endemis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 71 | 924 | Observation | `Observation.code.coding` | 81264-4 | Fever duration | http://loinc.org |
| 72 | 937 | Observation | `Observation.code.coding` | OC000121 | Pemeriksaan tanda dan gejala demam | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 73 | 940 | Observation | `Observation.component.code.coding` | 405947006 | Nuchal rigidity | http://snomed.info/sct |
| 74 | 943 | Observation | `Observation.component.code.coding` | OV000222 | Ada penyebab lain dari demam | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 75 | 950 | ServiceRequest | `ServiceRequest.code` | 76772-3 | Plasmodium falciparum Ag [Presence] in Blood by Rapid immunoassay | http://loinc.org |
| 76 | 960 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 77 | 969 | Observation | `Observation.code.coding` | 76772-3 | Plasmodium falciparum Ag [Presence] in Blood by Rapid immunoassay | http://loinc.org |
| 78 | 970 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 79 | 971 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 80 | 981 | DiagnosticReport | `DiagnosticReport.code.coding` | 76772-3 | Plasmodium falciparum Ag [Presence] in Blood by Rapid immunoassay | http://loinc.org |
| 81 | 995 | ServiceRequest | `ServiceRequest.code` | 32700-7 | Microscopic observation [Identifier] in Blood by Malaria smear | http://loinc.org |
| 82 | 1005 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 83 | 1014 | Observation | `Observation.code.coding` | 32700-7 | Microscopic observation [Identifier] in Blood by Malaria smear | http://loinc.org |
| 84 | 1015 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 85 | 1016 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 86 | 1026 | DiagnosticReport | `DiagnosticReport.code.coding` | 32700-7 | Microscopic observation [Identifier] in Blood by Malaria smear | http://loinc.org |
| 87 | 1038 | Observation | `Observation.code.coding` | OC000100 | Klasifikasi demam | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 88 | 1039 | Observation | `Observation.valueCodeableConcept.coding` | OV000223 | Penyakit berat dengan demam | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 89 | 1040 | Observation | `Observation.valueCodeableConcept.coding` | 61462000 | Malaria | http://snomed.info/sct |
| 90 | 1041 | Observation | `Observation.valueCodeableConcept.coding` | OV000224 | Demam mungkin bukan malaria | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 91 | 1042 | Observation | `Observation.valueCodeableConcept.coding` | OV000225 | Penyakit berat dengan demam | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 92 | 1043 | Observation | `Observation.valueCodeableConcept.coding` | OV000226 | Demam bukan malaria | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 93 | 1064 | Condition | `Condition.code.coding` | 14189004 | Measles | http://snomed.info/sct |
| 94 | 1071 | Observation | `Observation.code.coding` | OC000101 | Pemeriksaan tanda dan gejala campak | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 95 | 1074 | Observation | `Observation.component.code.coding` | 271807003 | Eruption of skin | http://snomed.info/sct |
| 96 | 1077 | Observation | `Observation.component.code.coding` | SP000253 | Batuk atau Pilek atau Mata Merah | http://terminology.kemkes.go.id/sp |
| 97 | 1080 | Observation | `Observation.component.code.coding` | 1071000119107 | Oral lesion | http://snomed.info/sct |
| 98 | 1083 | Observation | `Observation.component.code.coding` | OV000228 | Ada luka di mulut dalam atau luas | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 99 | 1086 | Observation | `Observation.component.code.coding` | 246679005 | Discharge from eye | http://snomed.info/sct |
| 100 | 1089 | Observation | `Observation.component.code.coding` | 64634000 | Corneal opacity | http://snomed.info/sct |
| 101 | 1094 | Observation | `Observation.code.coding` | OC000102 | Klasifikasi campak | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 102 | 1095 | Observation | `Observation.valueCodeableConcept.coding` | OV000229 | Campak dengan komplikasi berat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 103 | 1096 | Observation | `Observation.valueCodeableConcept.coding` | SP000252 | Campak Dengan Komplikasi Pada Mata Dan/Atau Mulut | http://terminology.kemkes.go.id/sp |
| 104 | 1097 | Observation | `Observation.valueCodeableConcept.coding` | 14189004 | Measles | http://snomed.info/sct |
| 105 | 1118 | Observation | `Observation.code.coding` | OC000104 | Pemeriksaan infeksi dengue | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 106 | 1121 | Observation | `Observation.component.code.coding` | OV000273 | Demam tinggi terus menerus | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 107 | 1124 | Observation | `Observation.component.code.coding` | OV000274 | Badan teraba dingin | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 108 | 1127 | Observation | `Observation.component.code.coding` | SP000251 | Lemas atau Gelisah | http://terminology.kemkes.go.id/sp |
| 109 | 1130 | Observation | `Observation.component.code.coding` | 422587007 | Nausea | http://snomed.info/sct |
| 110 | 1133 | Observation | `Observation.component.code.coding` | 422400008 | Vomiting | http://snomed.info/sct |
| 111 | 1136 | Observation | `Observation.component.code.coding` | OV000275 | Muntah terus menerus | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 112 | 1139 | Observation | `Observation.component.code.coding` | 21522001 | Abdominal pain | http://snomed.info/sct |
| 113 | 1142 | Observation | `Observation.component.code.coding` | SP000250 | Perdarahan Berupa Mimisan atau Muntah Darah (Coklat Seperti Kopi) atau BAB Berdarah (Berwarna Hitam) | http://terminology.kemkes.go.id/sp |
| 114 | 1145 | Observation | `Observation.component.code.coding` | 271807003 | Eruption of skin | http://snomed.info/sct |
| 115 | 1148 | Observation | `Observation.component.code.coding` | 279001004 | Pain finding at anatomical site | http://snomed.info/sct |
| 116 | 1151 | Observation | `Observation.component.code.coding` | OV000276 | BAK terakhir ≥6 jam | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 117 | 1154 | Observation | `Observation.component.code.coding` | OV000233 | Kaki/ tangan tampak pucat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 118 | 1157 | Observation | `Observation.component.code.coding` | OV000234 | Waktu pengisian kapiler >2 detik | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 119 | 1160 | Observation | `Observation.component.code.coding` | 771542000 | Cold extremity | http://snomed.info/sct |
| 120 | 1163 | Observation | `Observation.component.code.coding` | 64661000 | Thready pulse | http://snomed.info/sct |
| 121 | 1166 | Observation | `Observation.component.code.coding` | 86651002 | Pulse fast | http://snomed.info/sct |
| 122 | 1169 | Observation | `Observation.component.code.coding` | OV000235 | Nyeri tekan perut kanan atas | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 123 | 1172 | Observation | `Observation.component.code.coding` | 17672001 | Accumulation of fluid | http://snomed.info/sct |
| 124 | 1175 | Observation | `Observation.component.code.coding` | 271813007 | Petechiae | http://snomed.info/sct |
| 125 | 1178 | Observation | `Observation.component.code.coding` | 249366005 | Bleeding from nose | http://snomed.info/sct |
| 126 | 1181 | Observation | `Observation.component.code.coding` | 18165001 | Jaundice | http://snomed.info/sct |
| 127 | 1184 | Observation | `Observation.component.code.coding` | 214264003 | Lethargy | http://snomed.info/sct |
| 128 | 1187 | Observation | `Observation.component.code.coding` | 17077006 | Abnormal respiratory rate | http://snomed.info/sct |
| 129 | 1190 | Observation | `Observation.component.code.coding` | OV000236 | Ada pembesaran hepar >2 cm | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 130 | 1195 | Observation | `Observation.code.coding` | 38520-3 | Capillary fragility | http://loinc.org |
| 131 | 1196 | Observation | `Observation.valueCodeableConcept.coding` | 846603004 | Positive capillary fragility test | http://snomed.info/sct |
| 132 | 1197 | Observation | `Observation.valueCodeableConcept.coding` | 829990003 | Negative capillary fragility test | http://snomed.info/sct |
| 133 | 1209 | ServiceRequest | `ServiceRequest.code` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 134 | 1219 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 135 | 1228 | Observation | `Observation.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 136 | 1240 | DiagnosticReport | `DiagnosticReport.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 137 | 1254 | ServiceRequest | `ServiceRequest.code` | 20570-8 | Hematocrit [Volume Fraction] of Blood | http://loinc.org |
| 138 | 1264 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 139 | 1273 | Observation | `Observation.code.coding` | 20570-8 | Hematocrit [Volume Fraction] of Blood | http://loinc.org |
| 140 | 1285 | DiagnosticReport | `DiagnosticReport.code.coding` | 20570-8 | Hematocrit [Volume Fraction] of Blood | http://loinc.org |
| 141 | 1299 | ServiceRequest | `ServiceRequest.code` | 26464-8 | Leukocytes [#/volume] in Blood | http://loinc.org |
| 142 | 1309 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 143 | 1318 | Observation | `Observation.code.coding` | 26464-8 | Leukocytes [#/volume] in Blood | http://loinc.org |
| 144 | 1330 | DiagnosticReport | `DiagnosticReport.code.coding` | 26464-8 | Leukocytes [#/volume] in Blood | http://loinc.org |
| 145 | 1344 | ServiceRequest | `ServiceRequest.code` | 26515-7 | Platelets [#/volume] in Blood | http://loinc.org |
| 146 | 1354 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 147 | 1363 | Observation | `Observation.code.coding` | 26515-7 | Platelets [#/volume] in Blood | http://loinc.org |
| 148 | 1375 | DiagnosticReport | `DiagnosticReport.code.coding` | 26515-7 | Platelets [#/volume] in Blood | http://loinc.org |
| 149 | 1389 | ServiceRequest | `ServiceRequest.code` | 75377-2 | Dengue virus NS1 Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 150 | 1399 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 151 | 1408 | Observation | `Observation.code.coding` | 75377-2 | Dengue virus NS1 Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 152 | 1409 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 153 | 1410 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 154 | 1420 | DiagnosticReport | `DiagnosticReport.code.coding` | 75377-2 | Dengue virus NS1 Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 155 | 1432 | Observation | `Observation.code.coding` | OC000105 | Klasifikasi infeksi dengue | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 156 | 1433 | Observation | `Observation.valueCodeableConcept.coding` | 20927009 | Dengue hemorrhagic fever | http://snomed.info/sct |
| 157 | 1434 | Observation | `Observation.valueCodeableConcept.coding` | 722863008 | Dengue with warning signs | http://snomed.info/sct |
| 158 | 1435 | Observation | `Observation.valueCodeableConcept.coding` | 722862003 | Dengue without warning signs | http://snomed.info/sct |
| 159 | 1436 | Observation | `Observation.valueCodeableConcept.coding` | OV000129 | Demam mungkin bukan dengue | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 160 | 1457 | Condition | `Condition.code.coding` | 300197009 | Ear problem | http://snomed.info/sct |
| 161 | 1464 | Observation | `Observation.code.coding` | OC000106 | Pemeriksaan tanda dan gejala masalah telinga | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 162 | 1467 | Observation | `Observation.component.code.coding` | 300197009 | Ear problem | http://snomed.info/sct |
| 163 | 1470 | Observation | `Observation.component.code.coding` | 301354004 | Pain of ear | http://snomed.info/sct |
| 164 | 1473 | Observation | `Observation.component.code.coding` | OV000278 | Ada rasa penuh di telinga | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 165 | 1476 | Observation | `Observation.component.code.coding` | 300132001 | Ear discharge | http://snomed.info/sct |
| 166 | 1479 | Observation | `Observation.component.code.coding` | 162364004 | Ear discharge present | http://snomed.info/sct |
| 167 | 1482 | Observation | `Observation.component.code.coding` | 300874009 | Swelling of ear | http://snomed.info/sct |
| 168 | 1487 | Observation | `Observation.code.coding` | OC000107 | Klasifikasi masalah telinga | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 169 | 1488 | Observation | `Observation.valueCodeableConcept.coding` | 52404001 | Mastoiditis | http://snomed.info/sct |
| 170 | 1489 | Observation | `Observation.valueCodeableConcept.coding` | OV000241 | Infeksi telinga akut | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 171 | 1490 | Observation | `Observation.valueCodeableConcept.coding` | OV000289 | Infeksi telinga kronis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 172 | 1491 | Observation | `Observation.valueCodeableConcept.coding` | OV000242 | Tidak ada infeksi telinga | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 173 | 1512 | Observation | `Observation.code.coding` | 284521000 | Pitting edema | http://snomed.info/sct |
| 174 | 1513 | Observation | `Observation.valueCodeableConcept.coding` | 420829009 | 1+ pitting edema | http://snomed.info/sct |
| 175 | 1514 | Observation | `Observation.valueCodeableConcept.coding` | 421605005 | 2+ pitting edema | http://snomed.info/sct |
| 176 | 1515 | Observation | `Observation.valueCodeableConcept.coding` | 421346005 | 3+ pitting edema | http://snomed.info/sct |
| 177 | 1525 | Observation | `Observation.code.coding` | 1153600001 | Weight for height z-score | http://snomed.info/sct |
| 178 | 1526 | Observation | `Observation.code.coding` | 1153598007 | Weight for length z score | http://snomed.info/sct |
| 179 | 1562 | Observation | `Observation.code.coding` | 284473002 | Mid upper arm circumference | http://snomed.info/sct |
| 180 | 1583 | Observation | `Observation.code.coding` | OV000253 | Terlalu lemah untuk menyusu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 181 | 1595 | Observation | `Observation.code.coding` | 271398006 | Weight steady | http://snomed.info/sct |
| 182 | 1607 | Observation | `Observation.code.coding` | OC000108 | Klasifikasi status gizi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 183 | 1608 | Observation | `Observation.valueCodeableConcept` | 414915002 | Obese | http://snomed.info/sct |
| 184 | 1609 | Observation | `Observation.valueCodeableConcept` | 238131007 | Overweight | http://snomed.info/sct |
| 185 | 1610 | Observation | `Observation.valueCodeableConcept` | OI000004 | Risiko Gizi Lebih | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 186 | 1611 | Observation | `Observation.valueCodeableConcept` | OV000254 | Gizi buruk dengan komplikasi berat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 187 | 1612 | Observation | `Observation.valueCodeableConcept` | OV000255 | Gizi buruk tanpa komplikasi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 188 | 1613 | Observation | `Observation.valueCodeableConcept` | 248325000 | Undernourished | http://snomed.info/sct |
| 189 | 1614 | Observation | `Observation.valueCodeableConcept` | 248324001 | Well nourished | http://snomed.info/sct |
| 190 | 1635 | Observation | `Observation.code.coding` | 1153604005 | Body height for age z-score | http://snomed.info/sct |
| 191 | 1636 | Observation | `Observation.code.coding` | 1153598007 | Weight for length z score | http://snomed.info/sct |
| 192 | 1673 | Observation | `Observation.code.coding` | 1153594009 | Head circumference for age z-score | http://snomed.info/sct |
| 193 | 1705 | Observation | `Observation.code.coding` | OC000111 | Klasifikasi anemia | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 194 | 1706 | Observation | `Observation.valueCodeableConcept.coding` | OV000272 | Anemia berat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 195 | 1707 | Observation | `Observation.valueCodeableConcept.coding` | 271737000 | Anemia | http://snomed.info/sct |
| 196 | 1708 | Observation | `Observation.valueCodeableConcept.coding` | 860635002 | No anemia present | http://snomed.info/sct |
| 197 | 1720 | ServiceRequest | `ServiceRequest.code` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 198 | 1730 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 199 | 1739 | Observation | `Observation.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 200 | 1751 | DiagnosticReport | `DiagnosticReport.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 201 | 1774 | Observation | `Observation.code.coding` | PC000013 | Riwayat tes HIV ibu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 202 | 1786 | Observation | `Observation.code.coding` | SP000247 | Hasil Tes HIV Ibu | http://terminology.kemkes.go.id/sp |
| 203 | 1787 | Observation | `Observation.valueCodeableConcept.coding` | LA15255-5 | Reactive | http://loinc.org |
| 204 | 1788 | Observation | `Observation.valueCodeableConcept.coding` | LA15256-3 | Nonreactive | http://loinc.org |
| 205 | 1797 | Procedure | `Procedure.code.coding` | PC000014 | Riwayat tes HIV anak | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 206 | 1809 | Observation | `Observation.code.coding` | SP000248 | Hasil Tes HIV Anak | http://terminology.kemkes.go.id/sp |
| 207 | 1810 | Observation | `Observation.valueCodeableConcept.coding` | LA15255-5 | Reactive | http://loinc.org |
| 208 | 1811 | Observation | `Observation.valueCodeableConcept.coding` | LA15256-3 | Nonreactive | http://loinc.org |
| 209 | 1821 | Observation | `Observation.code.coding` | OC000084 | Tes virologis HIV anak | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 210 | 1822 | Observation | `Observation.valueCodeableConcept.coding` | LA15255-5 | Reactive | http://loinc.org |
| 211 | 1823 | Observation | `Observation.valueCodeableConcept.coding` | LA15256-3 | Nonreactive | http://loinc.org |
| 212 | 1833 | Observation | `Observation.code.coding` | OC000083 | Tes serologis HIV anak | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 213 | 1834 | Observation | `Observation.valueCodeableConcept.coding` | LA15255-5 | Reactive | http://loinc.org |
| 214 | 1835 | Observation | `Observation.valueCodeableConcept.coding` | LA15256-3 | Nonreactive | http://loinc.org |
| 215 | 1845 | Observation | `Observation.code.coding` | 63895-7 | Breastfeeding status | http://loinc.org |
| 216 | 1857 | Observation | `Observation.code.coding` | 254387007 | Human immunodeficiency virus infection classification systems | http://snomed.info/sct |
| 217 | 1858 | Observation | `Observation.valueCodeableConcept.coding` | 165816005 | Human immunodeficiency virus positive | http://snomed.info/sct |
| 218 | 1859 | Observation | `Observation.valueCodeableConcept.coding` | OV000187 | Terpajan HIV: mungkin infeksi HIV | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 219 | 1860 | Observation | `Observation.valueCodeableConcept.coding` | SP000249 | Mungkin Bukan Infeksi HIV | http://terminology.kemkes.go.id/sp |
| 220 | 1881 | Immunization | `Immunization.vaccineCode` | 8 | Hep B, adolescent or pediatric | http://hl7.org/fhir/sid/cvx |
| 221 | 1882 | Immunization | `Immunization.vaccineCode` | VG45 | HepB | http://sys-ids.kemkes.go.id/kfa |
| 222 | 1895 | Immunization | `Immunization.vaccineCode` | 198 | DTP-hepB-Hib Pentavalent Non-US | http://hl7.org/fhir/sid/cvx |
| 223 | 1896 | Immunization | `Immunization.vaccineCode` | VG107 | DTAP | http://sys-ids.kemkes.go.id/kfa |
| 224 | 1897 | Immunization | `Immunization.vaccineCode` | VG45 | HepB | http://sys-ids.kemkes.go.id/kfa |
| 225 | 1898 | Immunization | `Immunization.vaccineCode` | VG17 | HIB | http://sys-ids.kemkes.go.id/kfa |
| 226 | 1911 | Immunization | `Immunization.vaccineCode` | 129 | Japanese Encephalitis, unspecified formulation | http://hl7.org/fhir/sid/cvx |
| 227 | 1912 | Immunization | `Immunization.vaccineCode` | VG129 | Japanese encephalitis | http://sys-ids.kemkes.go.id/kfa |
| 228 | 1924 | Immunization | `Immunization.vaccineCode` | 19 | BCG | http://hl7.org/fhir/sid/cvx |
| 229 | 1925 | Immunization | `Immunization.vaccineCode` | VG19 | BCG | http://sys-ids.kemkes.go.id/kfa |
| 230 | 1937 | Immunization | `Immunization.vaccineCode` | 02 | OPV | http://hl7.org/fhir/sid/cvx |
| 231 | 1938 | Immunization | `Immunization.vaccineCode` | VG89 | POLIO | http://sys-ids.kemkes.go.id/kfa |
| 232 | 1951 | Immunization | `Immunization.vaccineCode` | 152 | Pneumococcal Conjugate, unspecified formulation | http://hl7.org/fhir/sid/cvx |
| 233 | 1952 | Immunization | `Immunization.vaccineCode` | VG152 | PneumoPCV | http://sys-ids.kemkes.go.id/kfa |
| 234 | 1965 | Immunization | `Immunization.vaccineCode` | 02 | OPV | http://hl7.org/fhir/sid/cvx |
| 235 | 1966 | Immunization | `Immunization.vaccineCode` | VG89 | POLIO | http://sys-ids.kemkes.go.id/kfa |
| 236 | 1979 | Immunization | `Immunization.vaccineCode` | 152 | Pneumococcal Conjugate, unspecified formulation | http://hl7.org/fhir/sid/cvx |
| 237 | 1980 | Immunization | `Immunization.vaccineCode` | VG152 | PneumoPCV | http://sys-ids.kemkes.go.id/kfa |
| 238 | 1993 | Immunization | `Immunization.vaccineCode` | 198 | DTP-hepB-Hib Pentavalent Non-US | http://hl7.org/fhir/sid/cvx |
| 239 | 1994 | Immunization | `Immunization.vaccineCode` | VG107 | DTAP | http://sys-ids.kemkes.go.id/kfa |
| 240 | 1995 | Immunization | `Immunization.vaccineCode` | VG45 | HepB | http://sys-ids.kemkes.go.id/kfa |
| 241 | 1996 | Immunization | `Immunization.vaccineCode` | VG17 | HIB | http://sys-ids.kemkes.go.id/kfa |
| 242 | 2009 | Immunization | `Immunization.vaccineCode` | 198 | DTP-hepB-Hib Pentavalent Non-US | http://hl7.org/fhir/sid/cvx |
| 243 | 2010 | Immunization | `Immunization.vaccineCode` | VG107 | DTAP | http://sys-ids.kemkes.go.id/kfa |
| 244 | 2011 | Immunization | `Immunization.vaccineCode` | VG45 | HepB | http://sys-ids.kemkes.go.id/kfa |
| 245 | 2012 | Immunization | `Immunization.vaccineCode` | VG17 | HIB | http://sys-ids.kemkes.go.id/kfa |
| 246 | 2025 | Immunization | `Immunization.vaccineCode` | 198 | DTP-hepB-Hib Pentavalent Non-US | http://hl7.org/fhir/sid/cvx |
| 247 | 2026 | Immunization | `Immunization.vaccineCode` | VG107 | DTAP | http://sys-ids.kemkes.go.id/kfa |
| 248 | 2027 | Immunization | `Immunization.vaccineCode` | VG45 | HepB | http://sys-ids.kemkes.go.id/kfa |
| 249 | 2028 | Immunization | `Immunization.vaccineCode` | VG17 | HIB | http://sys-ids.kemkes.go.id/kfa |
| 250 | 2041 | Immunization | `Immunization.vaccineCode` | 04 | M/R | http://hl7.org/fhir/sid/cvx |
| 251 | 2042 | Immunization | `Immunization.vaccineCode` | VG03 | MMR | http://sys-ids.kemkes.go.id/kfa |
| 252 | 2055 | Immunization | `Immunization.vaccineCode` | 02 | OPV | http://hl7.org/fhir/sid/cvx |
| 253 | 2056 | Immunization | `Immunization.vaccineCode` | VG89 | POLIO | http://sys-ids.kemkes.go.id/kfa |
| 254 | 2069 | Immunization | `Immunization.vaccineCode` | 02 | OPV | http://hl7.org/fhir/sid/cvx |
| 255 | 2070 | Immunization | `Immunization.vaccineCode` | VG89 | POLIO | http://sys-ids.kemkes.go.id/kfa |
| 256 | 2083 | Immunization | `Immunization.vaccineCode` | 10 | IPV | http://hl7.org/fhir/sid/cvx |
| 257 | 2084 | Immunization | `Immunization.vaccineCode` | VG89 | POLIO | http://sys-ids.kemkes.go.id/kfa |
| 258 | 2097 | Immunization | `Immunization.vaccineCode` | 152 | Pneumococcal Conjugate, unspecified formulation | http://hl7.org/fhir/sid/cvx |
| 259 | 2098 | Immunization | `Immunization.vaccineCode` | VG152 | PneumoPCV | http://sys-ids.kemkes.go.id/kfa |
| 260 | 2111 | Immunization | `Immunization.vaccineCode` | 04 | M/R | http://hl7.org/fhir/sid/cvx |
| 261 | 2112 | Immunization | `Immunization.vaccineCode` | VG03 | MMR | http://sys-ids.kemkes.go.id/kfa |
| 262 | 2125 | Observation | `Observation.code.coding` | OC000114 | Membutuhkan suplemen vitamin A | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 263 | 2136 | Procedure | `Procedure.code.coding` | 767224000 | Administration of vitamin A | http://snomed.info/sct |
| 264 | 2147 | MedicationRequest | `MedicationRequest.contained.code.coding` | 92000809 | Retinol Palmitate 200.000 IU Kapsul Lunak | http://sys-ids.kemkes.go.id/kf |
| 265 | 2174 | MedicationDispense | `MedicationDispense.contained.code.coding` | 93018284 | Retinol Palmitate 200.000 IU Kapsul Lunak (Umum) | http://sys-ids.kemkes.go.id/kf |
| 266 | 2200 | MedicationRequest | `MedicationRequest.contained.code.coding` | 92000354 | Retinol Palmitate 100.000 IU Kapsul Lunak | http://sys-ids.kemkes.go.id/kf |
| 267 | 2227 | MedicationDispense | `MedicationDispense.contained.code.coding` | 93018284 | Retinol Palmitate 100.000 IU Kapsul Lunak (Umum) | http://sys-ids.kemkes.go.id/kf |
| 268 | 2254 | ServiceRequest | `ServiceRequest.code` | 185389009 | Follow-up visit | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 89 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 70 |
| http://loinc.org | 44 |
| http://sys-ids.kemkes.go.id/kfa | 25 |
| http://terminology.kemkes.go.id/sp | 19 |
| http://hl7.org/fhir/sid/cvx | 17 |
| http://sys-ids.kemkes.go.id/kf | 4 |
| **Total** | **268** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 35 | – | Puskesmas | Organization | `Organization.name` |
