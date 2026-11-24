# Output Form: ePuskesmas KIA Harian MTBM

Sumber: `mapping/phdt-data-dictionary-epus-mtbm.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-epus-mtbm.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 57 |
| Code (`jumlah code` = 1) | 139 |
| Code unik (code + CodeSystem) | 119 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 20 |
| Variabel BQ (unik) | 0 |
| Variabel raw (variabel dictionary; belum ada file mentah) | 105 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 3–31 | Patient | – | – | _Nama Bayi_ → `Patient.name.text` (3, tanpa BQ)<br>_NIK_ → `Patient.identifier.value` (6, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (8, tanpa BQ)<br>_Alamat_ → `Patient.address.extension.extension.valueCode` (16, tanpa BQ) |
| 2 | 74–94 | Practitioner | – | – | _Dokter/Tenaga Medis dan/atau Perawat / Bidan / Nutrisionist / Sanitarian_ → `Practitioner.identifier` (74, tanpa BQ) |
| 3 | 95–98 | RelatedPerson | – | – | _Nama Ibu_ → `RelatedPerson.patient` (95, tanpa BQ) |
| 4 | 99–107 | EpisodeOfCare | Neonate | Neonate | – |
| 5 | 108–125 | Encounter | – | – | _Tanggal Kunjungan_ → `Encounter.period.start` (120, tanpa BQ) |
| 6 | 126–132 | Condition | PC000003 | Manajemen Terpadu Bayi Muda (MTBM) | – |
| 7 | 146–163 | Observation | 424144002 | Current chronological age | _Umur_ → `Observation.valueQuantity.value` (149, tanpa BQ) |
| 8 | 164–175 | Observation | 9843-4 | Head Occipital-frontal circumference | _Lingkar Kepala_ → `Observation.valueQuantity.value` (167, tanpa BQ) |
| 9 | 176–187 | Observation | 8310-5 | Body temperature | _Suhu_ → `Observation.valueQuantity.value` (179, tanpa BQ) |
| 10 | 188–194 | Condition | – | – | _Anak sakit apa_ → `Condition.clinicalStatus.coding` (188, tanpa BQ) |
| 11 | 195–206 | Observation | SP000261 | Tipe Kunjungan | _Tipe Kunjungan_ → `Observation.valueCodeableConcept.coding` (198, tanpa BQ) |
| 12 | 207–488 | QuestionnaireResponse | – | – | _Tindakan_ → `QuestionnaireResponse.item.item.item.answer.valueString` (229, tanpa BQ)<br>_Apakah bayi kuning_ → `QuestionnaireResponse.item.item.item.linkId` (242, tanpa BQ)<br>_Tindakan_ → `QuestionnaireResponse.item.item.item.answer.valueString` (254, tanpa BQ)<br>_Apakah anak menderita diare?_ → `QuestionnaireResponse.item.item.item.linkId` (261, tanpa BQ)<br>_Tindakan_ → `QuestionnaireResponse.item.item.item.answer.valueString` (279, tanpa BQ)<br>_Apakah ibu pernah test HIV?_ → `QuestionnaireResponse.item.item.item.linkId` (289, tanpa BQ)<br>_Apakah bayi pernah test HIV?_ → `QuestionnaireResponse.item.item.item.linkId` (299, tanpa BQ)<br>_Apakah bayi pernah mendapat ASI sebelum atau saat pemeriksaan HIV?_ → `QuestionnaireResponse.item.item.item.item.linkId` (319, tanpa BQ)<br>_Apakah ibu dalam pengobatan antiretroviral?_ → `QuestionnaireResponse.item.item.item.item.linkId` (323, tanpa BQ)<br>_Apakah bayi diberikan profilaksis antiretroviral?_ → `QuestionnaireResponse.item.item.item.item.linkId` (327, tanpa BQ)<br>_Tindakan_ → `QuestionnaireResponse.item.item.item.answer.valueString` (336, tanpa BQ)<br>_Apakah bayi diberi ASI_ → `QuestionnaireResponse.item.item.item.linkId` (346, tanpa BQ)<br>_Berapa kali ASI dalam 24 jam?_ → `QuestionnaireResponse.item.item.item.item.linkId` (353, tanpa BQ)<br>_Apakah bayi diberi makanan/minuman selain ASI?_ → `QuestionnaireResponse.item.item.item.item.linkId` (356, tanpa BQ)<br>_Berapa kali diberi makanan/minuman tersebut dalam 24 jam?_ → `QuestionnaireResponse.item.item.item.item.item.linkId` (360, tanpa BQ)<br>_Alat apa yang digunakan_ → `QuestionnaireResponse.item.item.item.item.item.linkId` (363, tanpa BQ)<br>_Tindakan_ → `QuestionnaireResponse.item.item.item.answer.valueString` (392, tanpa BQ)<br>_Susu apa yang diberikan?_ → `QuestionnaireResponse.item.item.item.item.linkId` (410, tanpa BQ)<br>_Berapa kali pemberian susu dalam 24 jam?_ → `QuestionnaireResponse.item.item.item.item.linkId` (413, tanpa BQ)<br>_Berapa jumlah yang diberikan setiap pemberian minum?_ → `QuestionnaireResponse.item.item.item.item.linkId` (416, tanpa BQ)<br>_Bagaimana cara ibu menyiapkan dan memberikan susu kepada bayi? Apakah sudah benar?_ → `QuestionnaireResponse.item.item.item.item.linkId` (421, tanpa BQ)<br>_Apakah sudah higienis?_ → `QuestionnaireResponse.item.item.item.item.linkId` (425, tanpa BQ)<br>_Alat apa yang digunakan untuk memberi susu bayi?_ → `QuestionnaireResponse.item.item.item.item.linkId` (429, tanpa BQ)<br>_Apakah cara ibu membersihkan alat minum sudah benar?_ → `QuestionnaireResponse.item.item.item.item.linkId` (433, tanpa BQ)<br>_Apa minuman yang diberikan sebagai tambahan minuman pengganti?_ → `QuestionnaireResponse.item.item.item.linkId` (437, tanpa BQ)<br>_Tindakan_ → `QuestionnaireResponse.item.item.item.answer.valueString` (451, tanpa BQ)<br>_Tuliskan jika ada masalah atau keluhan lain_ → `QuestionnaireResponse.item.item.item.linkId` (483, tanpa BQ)<br>_Tuliskan jika ada masalah atau keluhan ibu_ → `QuestionnaireResponse.item.item.item.linkId` (486, tanpa BQ) |
| 13 | 489–501 | Observation | 9279-1 | Respiratory rate | _Laju Pernapasan ke-1_ → `Observation.identifier` (489, tanpa BQ) |
| 14 | 502–514 | Observation | 9279-1 | Respiratory rate | _Laju Pernapasan ke-2_ → `Observation.identifier` (502, tanpa BQ) |
| 15 | 515–527 | Observation | 103228002 | Hemoglobin saturation with oxygen | _Saturasi Oksigen Tangan Kanan_ → `Observation.valueQuantity.value` (518, tanpa BQ) |
| 16 | 528–540 | Observation | 103228002 | Hemoglobin saturation with oxygen | _Saturasi Oksigen Kaki Kiri_ → `Observation.valueQuantity.value` (531, tanpa BQ) |
| 17 | 541–633 | Observation | OC000078 | Pemeriksaan tanda dan gejala infeksi | _Pemeriksaan Infeksi_ → `Observation.valueBoolean` (544, tanpa BQ)<br>_Apakah bayi ada tanda biru di sekitar mulut saat menangis dan/atau disertai sesak napas?_ → `Observation.component.code.coding` (546, tanpa BQ)<br>_Apakah bayi tidak buang air besar 48 jam setelah lahir?_ → `Observation.component.code.coding` (549, tanpa BQ)<br>_Apakah bayi muntah berisi susu atau cairan berwarna hijau?_ → `Observation.component.code.coding` (552, tanpa BQ)<br>_Apakah perut bayi kembung dan sulit bernapas?_ → `Observation.component.code.coding` (555, tanpa BQ)<br>_Apakah perut bayi kembung dan sulit bernapas?_ → `Observation.component.code.coding` (558, tanpa BQ)<br>_Apakah bayi tampak lemah/tidak mau mengisap?_ → `Observation.component.code.coding` (561, tanpa BQ)<br>_Apakah bayi kejang?_ → `Observation.component.code.coding` (564, tanpa BQ)<br>_Apakah ada tanda biru di sekitar mulut saat bayi sedang menangis atau sedang mengisap_ → `Observation.component.code.coding` (567, tanpa BQ)<br>_Apakah ada tanda sesak napas seperti napas cuping hidung dan atau tarikan dinding dada ke dalam yang sangat kuat?_ → `Observation.component.code.coding` (570, tanpa BQ)<br>_Apakah bayi lemah, tidak kuat bergerak dan tidak mau mengisap?_ → `Observation.component.code.coding` (573, tanpa BQ)<br>_Apakah bayi lemah, tidak kuat bergerak dan tidak mau mengisap?_ → `Observation.component.code.coding` (576, tanpa BQ)<br>_Apakah bayi lemah, tidak kuat bergerak dan tidak mau mengisap?_ → `Observation.component.code.coding` (579, tanpa BQ)<br>_Apakah bayi muntah susu atau cairan berwarna hijau?_ → `Observation.component.code.coding` (582, tanpa BQ)<br>_Apakah ada gerakan kejang: gerakan spontan tidak terkendali dan tidak berhenti saat dipegang dan atau ditahan?_ → `Observation.component.code.coding` (585, tanpa BQ)<br>_Suhu tubuh anak_ → `Observation.component.code.coding` (588, tanpa BQ)<br>_Apakah bayi muntah berisi susu atau cairan berwarna hijau?_ → `Observation.component.code.coding` (591, tanpa BQ)<br>_Apakah perut bayi kembung dan sulit bernapas?_ → `Observation.component.code.coding` (594, tanpa BQ)<br>_Apakah perut bayi kembung dan sulit bernapas?_ → `Observation.component.code.coding` (597, tanpa BQ)<br>_Apakah tidak ada lubang anus atau kotoran keluar pada lubang tidak normal di sekitar anus?_ → `Observation.component.code.coding` (600, tanpa BQ)<br>_Mata bernanah_ → `Observation.component.code.coding` (603, tanpa BQ)<br>_Apakah pusar kemerahan?_ → `Observation.component.code.coding` (606, tanpa BQ)<br>_Apakah pusar kemerahan meluas sampai dinding perut > 1 cm?_ → `Observation.component.code.coding` (609, tanpa BQ)<br>_Apakah pusar bernanah_ → `Observation.component.code.coding` (612, tanpa BQ)<br>_Apakah ada pustul di kulit?_ → `Observation.component.code.coding` (615, tanpa BQ)<br>_Dengar suara napas, adakah suara merintih?_ → `Observation.component.code.coding` (618, tanpa BQ)<br>_Terdapat perbedaan hasil SpO2 > 3%_ → `Observation.component.code.coding` (621, tanpa BQ)<br>_Apakah napas cepat atau lambat?_ → `Observation.component.code.coding` (624, tanpa BQ) |
| 18 | 634–646 | Observation | OC000126 | Klasifikasi infeksi | _Klasifikasi Infeksi_ → `Observation.valueCodeableConcept.coding` (637, tanpa BQ) |
| 19 | 647–657 | Procedure | – | – | _Tindakan Infeksi_ → `Procedure.category.coding` (647, tanpa BQ) |
| 20 | 658–664 | Condition | 18165001 | Jaundice | _Kondisi Kuning_ → `Condition.clinicalStatus.coding` (658, tanpa BQ) |
| 21 | 665–677 | Observation | OC000128 | Umur pertama kali timbul kuning | _Umur Pertama Kali Timbul Kuning_ → `Observation.valueCodeableConcept.coding` (668, tanpa BQ) |
| 22 | 678–695 | Observation | SP000214 | Pemeriksaan Kondisi Ikterus | _Pemeriksaan Ikterus_ → `Observation.valueBoolean` (681, tanpa BQ)<br>_Ada kuning di mata atau kulit?_ → `Observation.component.code.coding` (683, tanpa BQ)<br>_Lihat telapak tangan dan telapak kaki bayi, apakah kuning_ → `Observation.component.code.coding` (686, tanpa BQ) |
| 23 | 696–708 | Observation | OC000129 | Klasifikasi ikterus | _Klasifikasi Ikterus_ → `Observation.valueCodeableConcept.coding` (699, tanpa BQ) |
| 24 | 709–719 | Procedure | – | – | _Tindakan Ikterus_ → `Procedure.category.coding` (709, tanpa BQ) |
| 25 | 720–726 | Condition | 62315008 | Diarrhea | _Kondisi Diare_ → `Condition.clinicalStatus.coding` (720, tanpa BQ) |
| 26 | 727–738 | Observation | OC000113 | Durasi diare | _Durasi Diare_ → `Observation.valueQuantity.value` (730, tanpa BQ) |
| 27 | 739–769 | Observation | OC000097 | Pemeriksaan tanda dan gejala diare | _Pemeriksaan Diare_ → `Observation.valueBoolean` (742, tanpa BQ)<br>_Apakah bayi bergerak atas kemauan sendiri?_ → `Observation.component.code.coding` (744, tanpa BQ)<br>_Apakah bayi bergerak hanya ketika dirangsang?_ → `Observation.component.code.coding` (747, tanpa BQ)<br>_Apakah bayi tidak bergerak sama sekali?_ → `Observation.component.code.coding` (750, tanpa BQ)<br>_Apakah bayi gelisah/rewel?_ → `Observation.component.code.coding` (753, tanpa BQ)<br>_Lihat apakah matanya cekung?_ → `Observation.component.code.coding` (756, tanpa BQ)<br>_Cubit kulit perut, apakah kembalinya_ → `Observation.component.code.coding` (759, tanpa BQ) |
| 28 | 770–782 | Observation | OC000098 | Klasifikasi diare | _Klasifikasi Diare_ → `Observation.valueCodeableConcept.coding` (773, tanpa BQ) |
| 29 | 783–793 | Procedure | – | – | _Tindakan Diare_ → `Procedure.category.coding` (783, tanpa BQ) |
| 30 | 794–805 | Observation | PC000013 | Riwayat tes HIV ibu | _Apakah ibu pernah test HIV?_ → `Observation.valueBoolean` (797, tanpa BQ) |
| 31 | 806–817 | Observation | OC000079 | Tes serologis HIV ibu | _Hasil test serologis HIV ibu_ → `Observation.valueCodeableConcept.coding` (809, tanpa BQ) |
| 32 | 818–828 | Procedure | PC000014 | Riwayat tes HIV anak | _Apakah bayi pernah test HIV?_ → `Procedure.category.coding` (818, tanpa BQ) |
| 33 | 829–840 | Observation | OC000084 | Tes virologis HIV anak | _Hasil test virologis HIV bayi_ → `Observation.valueCodeableConcept.coding` (832, tanpa BQ) |
| 34 | 841–852 | Observation | OC000083 | Tes serologis HIV anak | _Hasil test serologis HIV bayi_ → `Observation.valueCodeableConcept.coding` (844, tanpa BQ) |
| 35 | 853–864 | Observation | 63895-7 | Breastfeeding status | _Status Menyusu Anak_ → `Observation.valueBoolean` (856, tanpa BQ) |
| 36 | 865–878 | Observation | 254387007 | Human immunodeficiency virus infection classification systems | _Klasifikasi Pemeriksaan HIV_ → `Observation.valueCodeableConcept.coding` (868, tanpa BQ) |
| 37 | 879–889 | Procedure | – | – | _Tindakan Infeksi HIV_ → `Procedure.category.coding` (879, tanpa BQ) |
| 38 | 890–901 | Observation | 63895-7 | Breastfeeding status | _Status Menyusu_ → `Observation.valueBoolean` (893, tanpa BQ) |
| 39 | 902–916 | Observation | 1153593003 | Weight for age z-score | _Berat Badan Menurut Umur_ → `Observation.valueCodeableConcept.coding` (905, tanpa BQ) |
| 40 | 917–928 | Observation | 79740000 | Candidiasis of mouth | _Bercak Putih di Mulut_ → `Observation.valueBoolean` (920, tanpa BQ) |
| 41 | 929–940 | Observation | SP000271 | Terdapat Celah Bibir atau Langit-Langit | _Celah Bibir atau Langit-Langit_ → `Observation.valueBoolean` (932, tanpa BQ) |
| 42 | 941–952 | Observation | OC000082 | Posisi menyusu bayi | _Posisi Menyusu Bayi_ → `Observation.valueCodeableConcept.coding` (944, tanpa BQ) |
| 43 | 953–965 | Observation | OC000081 | Posisi pelekatan bayi pada puting | _Posisi Pelekatan Bayi Pada Puting_ → `Observation.valueCodeableConcept.coding` (956, tanpa BQ) |
| 44 | 966–978 | Observation | OC000080 | Efektifitas hisapan bayi | _Efektifitas Hisapan Bayi_ → `Observation.valueCodeableConcept.coding` (969, tanpa BQ) |
| 45 | 979–991 | Observation | OC000085 | Klasifikasi berat badan menurut umur dan/atau masalah pemberian ASI | _Klasifikasi Berat Badan Menurut Umur dan/atau Masalah Pemberian ASI_ → `Observation.valueCodeableConcept.coding` (982, tanpa BQ) |
| 46 | 992–1002 | Procedure | – | – | _Tindakan Berat Badan Rendah Menurut Umur dan Masalah Pemberian ASI_ → `Procedure.category.coding` (992, tanpa BQ) |
| 47 | 1003–1017 | Observation | 1153593003 | Weight for age z-score | _Berat Badan Menurut Umur_ → `Observation.valueCodeableConcept.coding` (1006, tanpa BQ) |
| 48 | 1018–1029 | Observation | 79740000 | Candidiasis of mouth | _Bercak Putih di Mulut_ → `Observation.valueBoolean` (1021, tanpa BQ) |
| 49 | 1030–1041 | Observation | SP000271 | Terdapat Celah Bibir atau Langit-Langit | _Celah Bibir atau Langit-Langit_ → `Observation.valueBoolean` (1033, tanpa BQ) |
| 50 | 1042–1054 | Observation | OC000086 | Klasifikasi Berat Badan Menurut Umur dan/atau Masalah Pemberian Minum | _Klasifikasi Berat Badan Menurut Umur dan/atau Masalah Pemberian Minum_ → `Observation.valueCodeableConcept.coding` (1045, tanpa BQ) |
| 51 | 1055–1065 | Procedure | – | – | _Tindakan Berat Badan Rendah Menurut Umur dan Masalah Pemberian Minum_ → `Procedure.category.coding` (1055, tanpa BQ) |
| 52 | 1066–1077 | Observation | OC000087 | Pemberian Vitamin K pada Bayi Baru Lahir | _Pemberian Vitamin K Setelah Lahir_ → `Observation.valueBoolean` (1069, tanpa BQ) |
| 53 | 1078–1088 | Procedure | 448883004 | Injection of vitamin K1 | _Pemberian Vitamin K_ → `Procedure.category.coding` (1078, tanpa BQ) |
| 54 | 1089–1104 | Immunization | – | – | _HB 0_ → `Immunization.status` (1089, tanpa BQ)<br>_BCG_ → `Immunization.status` (1103, tanpa BQ) |
| 55 | 1105–1117 | Immunization | – | – | _OPV 0_ → `Immunization.status` (1116, tanpa BQ) |
| 56 | 1118–1129 | Immunization | – | – | – |
| 57 | 1130–1141 | ServiceRequest | – | – | _Kunjungan Ulang_ → `ServiceRequest.category` (1130, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 35 |
| Procedure | 8 |
| Condition | 4 |
| Immunization | 3 |
| Patient | 1 |
| Practitioner | 1 |
| RelatedPerson | 1 |
| EpisodeOfCare | 1 |
| Encounter | 1 |
| QuestionnaireResponse | 1 |
| ServiceRequest | 1 |
| **Total** | **57** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 103 | EpisodeOfCare | `EpisodeOfCare.type.coding` | Neonate | Neonate | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 2 | 128 | Condition | `Condition.code.coding` | PC000003 | Manajemen Terpadu Bayi Muda (MTBM) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 3 | 148 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 4 | 151 | Observation | `Observation.component.code.coding` | SP000020 | Umur Bulan | http://terminology.kemkes.go.id/sp |
| 5 | 154 | Observation | `Observation.component.code.coding` | SP000021 | Umur Hari | http://terminology.kemkes.go.id/sp |
| 6 | 166 | Observation | `Observation.code.coding` | 9843-4 | Head Occipital-frontal circumference | http://loinc.org |
| 7 | 178 | Observation | `Observation.code.coding` | 8310-5 | Body temperature | http://loinc.org |
| 8 | 197 | Observation | `Observation.code.coding` | SP000261 | Tipe Kunjungan | http://terminology.kemkes.go.id/sp |
| 9 | 198 | Observation | `Observation.valueCodeableConcept.coding` | SP000262 | Kunjungan Pertama | http://terminology.kemkes.go.id/sp |
| 10 | 199 | Observation | `Observation.valueCodeableConcept.coding` | SP000263 | Kunjungan Ulang | http://terminology.kemkes.go.id/sp |
| 11 | 365 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.item.item.answer.valueCoding` | 68276009 | Bottle, device | http://snomed.info/sct |
| 12 | 366 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.item.item.answer.valueCoding` | 468332001 | Drinking cup | http://snomed.info/sct |
| 13 | 367 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.item.item.answer.valueCoding` | 394841004 | Other category | http://snomed.info/sct |
| 14 | 431 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.item.answer.valueCoding` | 68276009 | Bottle, device | http://snomed.info/sct |
| 15 | 432 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.item.answer.valueCoding` | 468332001 | Drinking cup | http://snomed.info/sct |
| 16 | 492 | Observation | `Observation.code.coding` | 9279-1 | Respiratory rate | http://loinc.org |
| 17 | 505 | Observation | `Observation.code.coding` | 9279-1 | Respiratory rate | http://loinc.org |
| 18 | 517 | Observation | `Observation.code.coding` | 103228002 | Hemoglobin saturation with oxygen | http://snomed.info/sct |
| 19 | 530 | Observation | `Observation.code.coding` | 103228002 | Hemoglobin saturation with oxygen | http://snomed.info/sct |
| 20 | 543 | Observation | `Observation.code.coding` | OC000078 | Pemeriksaan tanda dan gejala infeksi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 21 | 546 | Observation | `Observation.component.code.coding` | 3415004 | Cyanosis | http://snomed.info/sct |
| 22 | 549 | Observation | `Observation.component.code.coding` | OV000167 | Bayi tidak BAB 48 jam setelah lahir | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 23 | 552 | Observation | `Observation.component.code.coding` | SP000264 | Muntah Berisi Susu atau Cairan Berwarna Hijau | http://terminology.kemkes.go.id/sp |
| 24 | 555 | Observation | `Observation.component.code.coding` | 116289008 | Abdominal bloating | http://snomed.info/sct |
| 25 | 558 | Observation | `Observation.component.code.coding` | 230145002 | Difficulty breathing | http://snomed.info/sct |
| 26 | 561 | Observation | `Observation.component.code.coding` | SP000265 | Bayi Tampak Lemah atau Tidak Mau Menghisap | http://terminology.kemkes.go.id/sp |
| 27 | 564 | Observation | `Observation.component.code.coding` | 91175000 | Seizure | http://snomed.info/sct |
| 28 | 567 | Observation | `Observation.component.code.coding` | SP000266 | Ada Tanda Biru di Sekitar Mulut Saat Menangis atau Menghisap | http://terminology.kemkes.go.id/sp |
| 29 | 570 | Observation | `Observation.component.code.coding` | 267036007 | Dyspnea | http://snomed.info/sct |
| 30 | 573 | Observation | `Observation.component.code.coding` | 260407003 | Weak | http://snomed.info/sct |
| 31 | 576 | Observation | `Observation.component.code.coding` | 284511008 | Difficulty in initiating movement | http://snomed.info/sct |
| 32 | 579 | Observation | `Observation.component.code.coding` | OV000124 | Bayi tidak mau mengisap | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 33 | 582 | Observation | `Observation.component.code.coding` | SP000264 | Muntah Berisi Susu atau Cairan Berwarna Hijau | http://terminology.kemkes.go.id/sp |
| 34 | 585 | Observation | `Observation.component.code.coding` | SP000267 | Ada Gerakan Kejang | http://terminology.kemkes.go.id/sp |
| 35 | 588 | Observation | `Observation.component.code.coding` | 8310-5 | Body temperature | http://loinc.org |
| 36 | 589 | Observation | `Observation.component.valueCodeableConcept.coding` | OV000125 | Suhu tubuh >37,5°C | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 37 | 590 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000268 | Suhu tubuh <37,5°C | http://terminology.kemkes.go.id/sp |
| 38 | 591 | Observation | `Observation.component.code.coding` | SP000264 | Muntah Berisi Susu atau Cairan Berwarna Hijau | http://terminology.kemkes.go.id/sp |
| 39 | 594 | Observation | `Observation.component.code.coding` | 116289008 | Abdominal bloating | http://snomed.info/sct |
| 40 | 597 | Observation | `Observation.component.code.coding` | 230145002 | Difficulty breathing | http://snomed.info/sct |
| 41 | 600 | Observation | `Observation.component.code.coding` | 204712000 | Anal atresia | http://snomed.info/sct |
| 42 | 603 | Observation | `Observation.component.code.coding` | SP000269 | Kondisi Mata Bernanah | http://terminology.kemkes.go.id/sp |
| 43 | 604 | Observation | `Observation.component.valueCodeableConcept.coding` | OV000130 | Mata bernanah banyak | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 44 | 605 | Observation | `Observation.component.valueCodeableConcept.coding` | OV000131 | Mata bernanah sedikit | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 45 | 606 | Observation | `Observation.component.code.coding` | OV000132 | Pusar kemerahan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 46 | 609 | Observation | `Observation.component.code.coding` | OV000282 | Pusar kemerahan meluas sampai dinding perut >1 cm | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 47 | 612 | Observation | `Observation.component.code.coding` | 35745008 | Umbilical discharge | http://snomed.info/sct |
| 48 | 615 | Observation | `Observation.component.code.coding` | 271760008 | Pustule | http://snomed.info/sct |
| 49 | 618 | Observation | `Observation.component.code.coding` | 62085005 | Grunting respiration | http://snomed.info/sct |
| 50 | 621 | Observation | `Observation.component.code.coding` | OV000133 | Perbedaan saturasi oksigen >3% | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 51 | 624 | Observation | `Observation.component.code.coding` | 301283003 | Finding of rate of respiration | http://snomed.info/sct |
| 52 | 625 | Observation | `Observation.component.valueCodeableConcept.coding` | 271823003 | Tachypnea | http://snomed.info/sct |
| 53 | 626 | Observation | `Observation.component.valueCodeableConcept.coding` | 86684002 | Bradypnea | http://snomed.info/sct |
| 54 | 636 | Observation | `Observation.code.coding` | OC000126 | Klasifikasi infeksi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 55 | 637 | Observation | `Observation.valueCodeableConcept.coding` | OV000134 | Infeksi bakteri berat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 56 | 638 | Observation | `Observation.valueCodeableConcept.coding` | OV000135 | Infeksi bakteri lokal | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 57 | 639 | Observation | `Observation.valueCodeableConcept.coding` | OV000136 | Mungkin bukan infeksi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 58 | 660 | Condition | `Condition.code.coding` | 18165001 | Jaundice | http://snomed.info/sct |
| 59 | 667 | Observation | `Observation.code.coding` | OC000128 | Umur pertama kali timbul kuning | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 60 | 668 | Observation | `Observation.valueCodeableConcept.coding` | OV000174 | Timbul kuning pada hari pertama (<24 jam) setelah lahir | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 61 | 669 | Observation | `Observation.valueCodeableConcept.coding` | OV000175 | Timbul kuning pada umur >24 jam sampai dengan umur 14 hari | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 62 | 670 | Observation | `Observation.valueCodeableConcept.coding` | OV000176 | Timbul kuning pada umur >14 hari | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 63 | 680 | Observation | `Observation.code.coding` | SP000214 | Pemeriksaan Kondisi Ikterus | http://terminology.kemkes.go.id/sp |
| 64 | 683 | Observation | `Observation.component.code.coding` | SP000215 | Kuning Pada Mata atau Kulit | http://terminology.kemkes.go.id/sp |
| 65 | 686 | Observation | `Observation.component.code.coding` | SP000216 | Kuning Pada Telapak Tangan dan Telapak Kaki | http://terminology.kemkes.go.id/sp |
| 66 | 698 | Observation | `Observation.code.coding` | OC000129 | Klasifikasi ikterus | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 67 | 699 | Observation | `Observation.valueCodeableConcept.coding` | OV000179 | Ikterus berat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 68 | 700 | Observation | `Observation.valueCodeableConcept.coding` | 18165001 | Jaundice | http://snomed.info/sct |
| 69 | 701 | Observation | `Observation.valueCodeableConcept.coding` | OV000180 | Tidak ada ikterus | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 70 | 722 | Condition | `Condition.code.coding` | 62315008 | Diarrhea | http://snomed.info/sct |
| 71 | 729 | Observation | `Observation.code.coding` | OC000113 | Durasi diare | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 72 | 741 | Observation | `Observation.code.coding` | OC000097 | Pemeriksaan tanda dan gejala diare | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 73 | 744 | Observation | `Observation.component.code.coding` | OV000127 | Bayi bergerak atas kemauan sendiri | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 74 | 747 | Observation | `Observation.component.code.coding` | OV000128 | Bayi bergerak hanya ketika dirangsang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 75 | 750 | Observation | `Observation.component.code.coding` | 302001007 | Does not move | http://snomed.info/sct |
| 76 | 753 | Observation | `Observation.component.code.coding` | SP000270 | Gelisah atau Rewel | http://terminology.kemkes.go.id/sp |
| 77 | 756 | Observation | `Observation.component.code.coding` | 246923005 | Sunken eyes | http://snomed.info/sct |
| 78 | 759 | Observation | `Observation.component.code.coding` | SP000255 | Turgor Kulit Perut | http://terminology.kemkes.go.id/sp |
| 79 | 760 | Observation | `Observation.component.valueCodeableConcept.coding` | OV000181 | Cubitan kulit perut kembalinya sangat lambat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 80 | 761 | Observation | `Observation.component.valueCodeableConcept.coding` | OV000182 | Cubitan kulit perut kembalinya lambat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 81 | 762 | Observation | `Observation.component.valueCodeableConcept.coding` | OV000183 | Cubitan kulit perut kembali segera | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 82 | 772 | Observation | `Observation.code.coding` | OC000098 | Klasifikasi diare | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 83 | 773 | Observation | `Observation.valueCodeableConcept.coding` | OV000184 | Diare dehidrasi berat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 84 | 774 | Observation | `Observation.valueCodeableConcept.coding` | OV000185 | Diare dehidrasi ringan/sedang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 85 | 775 | Observation | `Observation.valueCodeableConcept.coding` | OV000186 | Diare tanpa dehidrasi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 86 | 796 | Observation | `Observation.code.coding` | PC000013 | Riwayat tes HIV ibu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 87 | 808 | Observation | `Observation.code.coding` | OC000079 | Tes serologis HIV ibu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 88 | 809 | Observation | `Observation.valueCodeableConcept.coding` | LA15255-5 | Reactive | http://loinc.org |
| 89 | 810 | Observation | `Observation.valueCodeableConcept.coding` | LA15256-3 | Nonreactive | http://loinc.org |
| 90 | 819 | Procedure | `Procedure.code.coding` | PC000014 | Riwayat tes HIV anak | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 91 | 831 | Observation | `Observation.code.coding` | OC000084 | Tes virologis HIV anak | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 92 | 832 | Observation | `Observation.valueCodeableConcept.coding` | LA15255-5 | Reactive | http://loinc.org |
| 93 | 833 | Observation | `Observation.valueCodeableConcept.coding` | LA15256-3 | Nonreactive | http://loinc.org |
| 94 | 843 | Observation | `Observation.code.coding` | OC000083 | Tes serologis HIV anak | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 95 | 844 | Observation | `Observation.valueCodeableConcept.coding` | LA15255-5 | Reactive | http://loinc.org |
| 96 | 845 | Observation | `Observation.valueCodeableConcept.coding` | LA15256-3 | Nonreactive | http://loinc.org |
| 97 | 855 | Observation | `Observation.code.coding` | 63895-7 | Breastfeeding status | http://loinc.org |
| 98 | 867 | Observation | `Observation.code.coding` | 254387007 | Human immunodeficiency virus infection classification systems | http://snomed.info/sct |
| 99 | 868 | Observation | `Observation.valueCodeableConcept.coding` | 165816005 | Human immunodeficiency virus positive | http://snomed.info/sct |
| 100 | 869 | Observation | `Observation.valueCodeableConcept.coding` | OV000187 | Terpajan HIV: mungkin infeksi HIV | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 101 | 870 | Observation | `Observation.valueCodeableConcept.coding` | OV000188 | Infeksi HIV tidak diketahui | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 102 | 871 | Observation | `Observation.valueCodeableConcept.coding` | OV000189 | Bukan infeksi HIV | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 103 | 892 | Observation | `Observation.code.coding` | 63895-7 | Breastfeeding status | http://loinc.org |
| 104 | 904 | Observation | `Observation.code.coding` | 1153593003 | Weight for age z-score | http://snomed.info/sct |
| 105 | 905 | Observation | `Observation.valueCodeableConcept.coding` | OV000190 | < 2 kg (umur < 7 hari) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 106 | 919 | Observation | `Observation.code.coding` | 79740000 | Candidiasis of mouth | http://snomed.info/sct |
| 107 | 931 | Observation | `Observation.code.coding` | SP000271 | Terdapat Celah Bibir atau Langit-Langit | http://terminology.kemkes.go.id/sp |
| 108 | 943 | Observation | `Observation.code.coding` | OC000082 | Posisi menyusu bayi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 109 | 944 | Observation | `Observation.valueCodeableConcept.coding` | OV000193 | Posisi menyusu bayi benar | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 110 | 945 | Observation | `Observation.valueCodeableConcept.coding` | OV000194 | Posisi menyusu bayi salah | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 111 | 955 | Observation | `Observation.code.coding` | OC000081 | Posisi pelekatan bayi pada puting | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 112 | 956 | Observation | `Observation.valueCodeableConcept.coding` | OV000195 | Tidak melekat sama sekali | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 113 | 957 | Observation | `Observation.valueCodeableConcept.coding` | OV000196 | Tidak melekat dengan baik | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 114 | 958 | Observation | `Observation.valueCodeableConcept.coding` | OV000197 | Melekat dengan baik | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 115 | 968 | Observation | `Observation.code.coding` | OC000080 | Efektifitas hisapan bayi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 116 | 969 | Observation | `Observation.valueCodeableConcept.coding` | OV000198 | Tidak mengisap sama sekali | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 117 | 970 | Observation | `Observation.valueCodeableConcept.coding` | OV000199 | Tidak mengisap dengan efektif | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 118 | 971 | Observation | `Observation.valueCodeableConcept.coding` | OV000200 | Mengisap dengan efektif | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 119 | 981 | Observation | `Observation.code.coding` | OC000085 | Klasifikasi berat badan menurut umur dan/atau masalah pemberian ASI | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 120 | 982 | Observation | `Observation.valueCodeableConcept.coding` | OV000201 | Berat badan sangat rendah menurut umur | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 121 | 983 | Observation | `Observation.valueCodeableConcept.coding` | OV000202 | Berat badan rendah menurut umur dan/atau masalah pemberian ASI | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 122 | 984 | Observation | `Observation.valueCodeableConcept.coding` | OV000203 | Berat badan tidak rendah menurut umur dan tidak ada masalah pemberian ASI | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 123 | 1005 | Observation | `Observation.code.coding` | 1153593003 | Weight for age z-score | http://snomed.info/sct |
| 124 | 1006 | Observation | `Observation.valueCodeableConcept.coding` | OV000190 | < 2 kg (umur < 7 hari) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 125 | 1020 | Observation | `Observation.code.coding` | 79740000 | Candidiasis of mouth | http://snomed.info/sct |
| 126 | 1032 | Observation | `Observation.code.coding` | SP000271 | Terdapat Celah Bibir atau Langit-Langit | http://terminology.kemkes.go.id/sp |
| 127 | 1044 | Observation | `Observation.code.coding` | OC000086 | Klasifikasi Berat Badan Menurut Umur dan/atau Masalah Pemberian Minum | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 128 | 1045 | Observation | `Observation.valueCodeableConcept.coding` | OV000201 | Berat badan sangat rendah menurut umur | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 129 | 1046 | Observation | `Observation.valueCodeableConcept.coding` | OV000204 | Berat badan rendah menurut umur dan/atau masalah pemberian minum | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 130 | 1047 | Observation | `Observation.valueCodeableConcept.coding` | OV000205 | Berat badan tidak rendah menurut umur dan tidak ada masalah pemberian minum | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 131 | 1068 | Observation | `Observation.code.coding` | OC000087 | Pemberian Vitamin K pada Bayi Baru Lahir | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 132 | 1079 | Procedure | `Procedure.code.coding` | 448883004 | Injection of vitamin K1 | http://snomed.info/sct |
| 133 | 1091 | Immunization | `Immunization.vaccineCode` | 8 | Hep B, adolescent or pediatric | http://hl7.org/fhir/sid/cvx |
| 134 | 1092 | Immunization | `Immunization.vaccineCode` | VG45 | HepB | http://sys-ids.kemkes.go.id/kfa |
| 135 | 1105 | Immunization | `Immunization.vaccineCode` | 19 | BCG | http://hl7.org/fhir/sid/cvx |
| 136 | 1106 | Immunization | `Immunization.vaccineCode` | VG19 | BCG | http://sys-ids.kemkes.go.id/kfa |
| 137 | 1118 | Immunization | `Immunization.vaccineCode` | 02 | OPV | http://hl7.org/fhir/sid/cvx |
| 138 | 1119 | Immunization | `Immunization.vaccineCode` | VG89 | POLIO | http://sys-ids.kemkes.go.id/kfa |
| 139 | 1134 | ServiceRequest | `ServiceRequest.code` | 185389009 | Follow-up visit | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 62 |
| http://snomed.info/sct | 37 |
| http://terminology.kemkes.go.id/sp | 20 |
| http://loinc.org | 13 |
| http://hl7.org/fhir/sid/cvx | 3 |
| http://sys-ids.kemkes.go.id/kfa | 3 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 1 |
| **Total** | **139** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 35 | – | Puskesmas | Organization | `Organization.name` |
