# Output Form: KuApps BidanKu - ANC

Sumber: `mapping/phdt-data-dictionary-kuapps-bidanku-anc.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-kuapps-bidanku-anc.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 190 |
| Code (`jumlah code` = 1) | 440 |
| Code unik (code + CodeSystem) | 333 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 93 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 3–13 | Observation | SP000699 | Kelompok Dasawisma | _Kelompok Dasawisma_ → `Observation.valueString` (6, tanpa BQ) |
| 2 | 15–26 | Observation | SP000798 | Usia kehamilan saat melakukan pendaftaran posyandu | _Usia kehamilan Ibu saat pertama kali mengikuti posyandu (minggu)_ → `Observation.valueQuantity.value` (18, tanpa BQ) |
| 3 | 27–37 | Observation | SP000713 | Bulan Pendaftaran Posyandu | _Kapan Pertama Kali ibu mengikuti Posyandu Ibu hamil? (Bulan)_ → `Observation.valueDateTime` (30, tanpa BQ) |
| 4 | 39–51 | Observation | 8302-2 | Body height | _Tinggi Badan_ → `Observation.valueQuantity.value` (43, tanpa BQ) |
| 5 | 52–64 | Observation | 56077-1 | Body weight --pre current pregnancy | _Berat badan sebelum kehamilan_ → `Observation.valueQuantity.value` (56, tanpa BQ) |
| 6 | 65–104 | Observation | OC000010 | Indeks Massa Tubuh Sebelum Hamil | _IMT Sebelum Hamil_ → `Observation.valueQuantity.value` (69, tanpa BQ)<br>_Interpretasi IMT_ → `Observation.interpretation.coding` (78, tanpa BQ) |
| 7 | 105–117 | Observation | 29463-7 | Body weight | _Berat badan saat ini_ → `Observation.valueQuantity.value` (109, tanpa BQ) |
| 8 | 118–133 | Observation | 284473002 | Mid upper arm circumference | _LILA_ → `Observation.valueQuantity.value` (122, tanpa BQ)<br>_Status Gizi_ → `Observation.interpretation` (131, tanpa BQ) |
| 9 | 134–146 | Observation | 8480-6 | Systolic blood pressure | _Tekanan darah sistolik_ → `Observation.valueQuantity.value` (138, tanpa BQ) |
| 10 | 147–159 | Observation | 8462-4 | Diastolic blood pressure | _Tekanan darah diastolik_ → `Observation.valueQuantity.value` (151, tanpa BQ) |
| 11 | 160–171 | Observation | 1285244000 | Mean arterial pressure | _Mean Arteri Pressure (MAP)_ → `Observation.valueQuantity.value` (163, tanpa BQ) |
| 12 | 172–186 | Observation | SP000010 | Skrining Hipertensi dalam Kehamilan | _Skrining Hipertensi dalam kehamilan_ → `Observation.valueCodeableConcept.coding` (175, tanpa BQ) |
| 13 | 187–199 | Observation | 8310-5 | Body temperature | _Suhu_ → `Observation.valueQuantity.value` (191, tanpa BQ) |
| 14 | 200–212 | Observation | 8867-4 | Heart Rate | _Denyut nadi_ → `Observation.valueQuantity.value` (204, tanpa BQ) |
| 15 | 213–224 | Observation | 250554003 | Measurement of oxygen saturation at periphery | _Oksimetri_ → `Observation.valueQuantity.value` (216, tanpa BQ) |
| 16 | 226–239 | Condition | 68154008 | Chronic cough | _Apakah ada masalah kesehatan selama kehamilan_ → `Condition.clinicalStatus.coding` (226, tanpa BQ)<br>_Sebutkan masalah kesehatan lainnya!_ → `Condition.code.text` (235, tanpa BQ) |
| 17 | 240–286 | Observation | 416471007 | Family history of clinical finding | _Apakah ada riwayat penyakit keturunan keluarga_ → `Observation.valueBoolean` (243, tanpa BQ)<br>_Sebutkan risiko masalah kesehatan riwayat penyakit keluarga! *(Revisi wording)_ → `Observation.component.code.coding` (245, tanpa BQ)<br>_Sebutkan risiko masalah kesehatan riwayat penyakit keluarga lainnya!_ → `Observation.component.valueString` (279, tanpa BQ) |
| 18 | 287–333 | Observation | 417662000 | History of clinical finding in subject | _Apakah ada riwayat penyakit pribadi?_ → `Observation.valueBoolean` (290, tanpa BQ)<br>_Sebutkan riwayat penyakit pribadi yang dimiliki!_ → `Observation.component.code.coding` (292, tanpa BQ)<br>_Sebutkan riwayat penyakit pribadi lainnya!_ → `Observation.component.code.coding` (325, tanpa BQ) |
| 19 | 334–389 | Observation | SP000412 | Tanda Bahaya Kehamilan | _Apakah ada tanda bahaya kehamilan_ → `Observation.valueBoolean` (337, tanpa BQ)<br>_Sebutkan tanda bahaya kehamilan_ → `Observation.component.code.coding` (339, tanpa BQ)<br>_Sebutkan tanda bahaya kehamilan lainnya!_ → `Observation.component.valueString` (382, tanpa BQ) |
| 20 | 390–401 | Observation | 11996-6 | [#] Pregnancies | _Jumlah kehamilan, termasuk kehamilan saat ini (Gravida)_ → `Observation.valueInteger` (394, tanpa BQ) |
| 21 | 402–413 | Observation | 11977-6 | [#] Parity | _Jumlah kelahiran saat ini (partus)_ → `Observation.valueInteger` (406, tanpa BQ) |
| 22 | 414–425 | Observation | 69043-8 | Other pregnancy outcomes # | _Jumlah kehilangan kehamilan (Abortus)_ → `Observation.valueInteger` (418, tanpa BQ) |
| 23 | 426–437 | Condition | 86406008 | Human immunodeficiency virus infection | _Apakah ibu memiliki kondisi berikut?_ → `Condition.clinicalStatus.coding` (426, tanpa BQ) |
| 24 | 438–445 | FamilyMemberHistory | – | – | _Bagaimana status HIV pasangan ibu?_ → `FamilyMemberHistory.status` (438, tanpa BQ) |
| 25 | 446–460 | Immunization | – | – | _Apakah dilakukan imunisasi tetanus (TT) pada kunjungan ini?_ → `Immunization.status` (446, tanpa BQ)<br>_Riwayat imunisasi tetanus (TT) Ibu, termasuk apabila diberikan hari ini_ → `Immunization.status` (459, tanpa BQ) |
| 26 | 461–478 | Immunization | VG139 | Td | – |
| 27 | 479–489 | Immunization | – | – | – |
| 28 | 490–501 | Observation | SP000510 | Mendapat Makanan Bergizi Gratis (MBG) bulan ini | _Apakah Ibu hamil mendapatkan MBG?_ → `Observation.valueBoolean` (493, tanpa BQ) |
| 29 | 502–511 | MedicationStatement | – | – | _Apakah ibu hamil mengonsumsi tablet TTD_ → `MedicationStatement.category.coding` (502, tanpa BQ) |
| 30 | 512–523 | Observation | SP000955 | Mengonsumsi tablet tambah darah dalam 24 jam terakhir | _Apakah Ibu mengonsumsi TTD dalam 24 jam terakhir?_ → `Observation.valueBoolean` (515, tanpa BQ) |
| 31 | 524–537 | MedicationStatement | SP000370 | Multiple Micronutrient Supplement | _Berapa jumlah TTD yang dikonsumsi oleh Ibu hamil dalam 1 bulan terakhir?_ → `MedicationStatement.dosage.doseAndRate.doseQuantity` (524, tanpa BQ)<br>_Apakah ibu hamil mengonsumsi tablet MMS_ → `MedicationStatement.category.coding` (526, tanpa BQ)<br>_Berapa jumlah MMS yang dikonsumsi oleh Ibu hamil?_ → `MedicationStatement.dosage.doseAndRate.doseQuantity` (536, tanpa BQ) |
| 32 | 538–549 | Observation | SP000046 | Terapi Antiretroviral (ART) | _Apakah ibu mendapat terapi anti retroviral (ART)?_ → `Observation.valueBoolean` (541, tanpa BQ) |
| 33 | 550–570 | Observation | SP000124 | Obat anti malaria | _Apakah ibu konsumsi obat anti malaria?_ → `Observation.valueBoolean` (553, tanpa BQ)<br>_Jika ya, jenis obat anti malaria apa yang dikonsumsi?_ → `Observation.component.code.coding` (555, tanpa BQ) |
| 34 | 571–582 | Observation | SP000157 | Obat Diabetes Mellitus | _Apakah ibu konsumsi obat diabetes melitus?_ → `Observation.valueBoolean` (574, tanpa BQ) |
| 35 | 583–622 | Observation | SP000424 | Riwayat Perilaku Berisiko Sebelum Hamil | _Apakah ada faktor perilaku beresiko berikut?_ → `Observation.valueBoolean` (586, tanpa BQ)<br>_Sebutkan perilaku berisiko lainnya!_ → `Observation.component.valueString` (615, tanpa BQ) |
| 36 | 624–664 | Observation | 1156096005 | Past pregnancy history of complication occurring during labor and delivery | _Sebutkan riwayat kehamilan ibu sebelumnya_ → `Observation.valueBoolean` (627, tanpa BQ) |
| 37 | 665–679 | Condition | 34842007 | Antepartum hemorrhage | _Apakah ada komplikasi kehamilan pada kehamilan saat ini?_ → `Condition.clinicalStatus.coding` (665, tanpa BQ)<br>_Sebutkan komplikasi kehamilan lainnya pada kehamilan saat ini!_ → `Condition.code.text` (674, tanpa BQ) |
| 38 | 680–691 | Observation | 17566005 | Class in prenatal exercises | _Apakah ibu mengikuti kelas ibu hamil?_ → `Observation.valueBoolean` (683, tanpa BQ)<br>_Jika ya, kapan terakhir Ibu mengikuti kelas ibu hamil?_ → `Observation.effectiveDateTime` (688, tanpa BQ) |
| 39 | 692–702 | Observation | 52829-9 | Place of service | _Dimana ibu mengikuti kelas ibu hamil?_ → `Observation.valueString` (695, tanpa BQ) |
| 40 | 703–716 | Observation | SP000764 | Pendamping kelas ibu hamil | _Pendamping saat mengikuti kelas ibu hamil_ → `Observation.valueCodeableConcept.coding` (706, tanpa BQ) |
| 41 | 717–736 | MedicationRequest | 91000488 | Iodine | _Apakah ibu diberikan kapsul yodium?_ → `MedicationRequest.contained.resourceType` (717, tanpa BQ) |
| 42 | 737–752 | MedicationDispense | 91000488 | Iodine | – |
| 43 | 753–763 | Procedure | 385892002 | Mental health screening | _Apakah dilakukan skrining kesehatan jiwa pada ibu hamil?_ → `Procedure.category.coding` (753, tanpa BQ) |
| 44 | 764–776 | Observation | SP000730 | Tindak lanjut hasil skrining kesehatan jiwa | _Apa tindak lanjut dari hasil skrining kesehatan jiwa?_ → `Observation.valueBoolean` (767, tanpa BQ)<br>_Apakah diperlukan rujukan sesuai hasil skrining kesehatan jiwa?_ → `Observation.component.code.coding` (774, tanpa BQ) |
| 45 | 777–777 | Encounter | – | – | – |
| 46 | 778–784 | Observation | – | – | – |
| 47 | 785–799 | ServiceRequest | – | – | _Dimana fasillitas kesehatan tujuan rujukan?_ → `ServiceRequest.requester.reference` (794, tanpa BQ)<br>_Nama fasillitas kesehatan tujuan rujukan_ → `ServiceRequest.performer.display` (799, tanpa BQ) |
| 48 | 800–825 | QuestionnaireResponse | https://fhir.kemkes.go.id/sp/Questionnaire/Q00016 | – | _Batuk terus menerus_ → `QuestionnaireResponse.item.linkId` (810, tanpa BQ)<br>_Demam lebih dari ≥ 2 minggu_ → `QuestionnaireResponse.item.linkId` (814, tanpa BQ)<br>_BB tidak naik atau turun dalam 2 bulan berturut-turut_ → `QuestionnaireResponse.item.linkId` (818, tanpa BQ)<br>_Kontak erat dengan Pasien TBC_ → `QuestionnaireResponse.item.linkId` (822, tanpa BQ) |
| 49 | 826–838 | Observation | 171126009 | Tuberculosis screening | _Interpretasi hasil skrining TBC_ → `Observation.valueQuantity.value` (826, tanpa BQ) |
| 50 | 839–850 | Observation | SP000779 | Multipara dengan kehamilan oleh pasangan baru | _Multipara dengan kehamilan oleh pasangan baru_ → `Observation.valueBoolean` (842, tanpa BQ) |
| 51 | 851–862 | Observation | 813541000000100 | Pregnancy resulting from assisted conception | _Kehamilan dengan Teknologi Reproduksi Berbantu: Bayi Tabung, Obat Induksi Ovulasi_ → `Observation.valueBoolean` (854, tanpa BQ) |
| 52 | 863–874 | Observation | SP000780 | Umur ≥ 35 Tahun | _Umur ≥ 35 Tahun_ → `Observation.valueBoolean` (866, tanpa BQ) |
| 53 | 875–886 | Observation | 102877006 | Nulliparous | _Nulipara_ → `Observation.valueBoolean` (878, tanpa BQ) |
| 54 | 887–898 | Observation | SP000781 | Multipara yang Jarak Kehamilan Sebelumnya > 10 Tahun | _Multipara yang Jarak Kehamilan Sebelumnya > 10 Tahun_ → `Observation.valueBoolean` (890, tanpa BQ) |
| 55 | 899–910 | Observation | 700190003 | Family history of pre-eclampsia | _Riwayat Preeklampsia pada Ibu atau Saudara Perempuan_ → `Observation.valueBoolean` (902, tanpa BQ) |
| 56 | 911–922 | Observation | 162864005 | Body mass index 30+ - obesity | _Obesitas Sebelum Hamil (IMT > 30 kg/m2)_ → `Observation.valueBoolean` (914, tanpa BQ) |
| 57 | 923–934 | Observation | SP000782 | Multipara Dengan Riwayat Preeklampsia Sebelumnya | _Multipara Dengan Riwayat Preeklampsia Sebelumnya_ → `Observation.valueBoolean` (926, tanpa BQ) |
| 58 | 935–946 | Observation | 16356006 | Multiple pregnancy | _Kehamilan Multipel_ → `Observation.valueBoolean` (938, tanpa BQ) |
| 59 | 947–958 | Observation | 11687002 | Gestational diabetes mellitus | _Diabetes dalam Kehamilan_ → `Observation.valueBoolean` (950, tanpa BQ) |
| 60 | 959–970 | Observation | 8762007 | Chronic hypertension in obstetric context | _Hipertensi Kronik_ → `Observation.valueBoolean` (962, tanpa BQ) |
| 61 | 971–982 | Observation | 90708001 | Kidney disease | _Penyakit Ginjal_ → `Observation.valueBoolean` (974, tanpa BQ) |
| 62 | 983–994 | Observation | 85828009 | Autoimmune disease | _Penyakit Autoimun, SLE_ → `Observation.valueBoolean` (986, tanpa BQ) |
| 63 | 995–1006 | Observation | 26843008 | Antiphospholipid syndrome | _Anti Phospholipid Syndrome_ → `Observation.valueBoolean` (998, tanpa BQ) |
| 64 | 1007–1018 | Observation | SP000783 | Mean Arterial Presure > 90 mmHg | _Mean Arterial Presure > 90 mmHg_ → `Observation.valueBoolean` (1010, tanpa BQ) |
| 65 | 1019–1030 | Observation | 29738008 | Proteinuria | _Proteinuria_ → `Observation.valueBoolean` (1022, tanpa BQ) |
| 66 | 1031–1042 | Observation | SP000799 | Hasil skrining Preeklampsia | _Kesimpulan_ → `Observation.valueCodeableConcept.coding` (1034, tanpa BQ) |
| 67 | 1043–1054 | Observation | 1237486008 | Pale discoloration of entire skin of body | _Apakah ibu terlihat pucat?_ → `Observation.valueBoolean` (1046, tanpa BQ) |
| 68 | 1055–1094 | Observation | 106048009 | Respiratory finding | _Apakah dilakukan tes pernapasan?_ → `Observation.valueCodeableConcept.coding` (1058, tanpa BQ)<br>_Sebutkan masalah pernapasannya!_ → `Observation.component.code.coding` (1068, tanpa BQ)<br>_Sebutkan masalah pernapasan lainnya!_ → `Observation.component.valueString` (1087, tanpa BQ) |
| 69 | 1095–1105 | Procedure | 87431004 | Dilation of cervical canal | _Apakah dilakukan pemeriksaan dilatasi serviks?_ → `Procedure.category.coding` (1095, tanpa BQ) |
| 70 | 1106–1117 | Observation | 289825001 | Diameter of cervical dilatation | _Berapa cm dilatasi serviks?_ → `Observation.valueQuantity.value` (1109, tanpa BQ) |
| 71 | 1118–1129 | Observation | 267038008 | Edema | _Apakah ada edema?_ → `Observation.valueBoolean` (1121, tanpa BQ) |
| 72 | 1130–1144 | Observation | 44972-8 | Edema site | _Apa jenis edema yang diderita ibu?_ → `Observation.valueCodeableConcept.coding` (1133, tanpa BQ) |
| 73 | 1145–1158 | Observation | 423484008 | Grade of edema | _Tingkat keparahan edema_ → `Observation.valueCodeableConcept.coding` (1148, tanpa BQ) |
| 74 | 1159–1170 | Observation | vital-signs | Abdominal circumference | _Lingkar perut_ → `Observation.valueQuantity.value` (1162, tanpa BQ) |
| 75 | 1171–1198 | Observation | 11881-0 | Uterus Fundal height Tape measure | _TFU dalam cm_ → `Observation.valueQuantity.value` (1175, tanpa BQ)<br>_TFU dalam jari_ → `Observation.component.code.coding` (1177, tanpa BQ) |
| 76 | 1199–1211 | Observation | 55283-6 | Fetal Heart rate | _Detak Jantung Janin_ → `Observation.valueQuantity.value` (1203, tanpa BQ) |
| 77 | 1212–1223 | Observation | 246435002 | Number of fetuses | _Jumlah Janin_ → `Observation.valueInteger` (1216, tanpa BQ) |
| 78 | 1224–1239 | Observation | 72155-5 | Position in womb Fetus [RHEA] | _Presentasi Janin_ → `Observation.valueCodeableConcept.coding` (1228, tanpa BQ) |
| 79 | 1240–1250 | Procedure | 88.78 | Diagnostic ultrasound of gravid uterus | _Apakah dilakukan pemeriksaan USG?_ → `Procedure.category.coding` (1240, tanpa BQ) |
| 80 | 1252–1271 | Procedure | 88.78 | Diagnostic ultrasound of gravid uterus | _Dimana pemeriksaan USG dilakukan?_ → `Procedure.performer.actor.identifier` (1260, tanpa BQ)<br>_Nama fasilitas kesehatan pemeriksaan USG_ → `Procedure.performer.actor.display` (1265, tanpa BQ)<br>_Siapa nama tenaga kesehatan yang melakukan pemeriksaan?_ → `Procedure.performer.actor.identifier` (1266, tanpa BQ) |
| 81 | 1272–1283 | Observation | SP000729 | Sudah menjadwalkan pemeriksaan USG terdekat | _Apakah sudah menjadwalkan pemeriksaan USG terdekat?_ → `Observation.valueBoolean` (1275, tanpa BQ) |
| 82 | 1284–1301 | CarePlan | 773433004 | Obstetric antenatal care plan | _Kapan jadwal pemeriksaan USG terdekat?_ → `CarePlan.activity.detail.scheduledTiming.event` (1295, tanpa BQ)<br>_Dimana pemeriksaan USG terdekat dijadwalkan?_ → `CarePlan.activity.detail.performer.reference` (1296, tanpa BQ)<br>_Nama fasilitas kesehatan pemeriksaan USG terdekat dijadwalkan_ → `CarePlan.activity.detail.performer.display` (1301, tanpa BQ) |
| 83 | 1302–1327 | Observation | 268445003 | Ultrasound scan - obstetric | _Hasil pemeriksaan umum USG_ → `Observation.valueCodeableConcept.coding` (1305, tanpa BQ)<br>_Jika hasil tidak normal. Tidak normal karena apa?_ → `Observation.valueCodeableConcept.text` (1308, tanpa BQ)<br>_Kapan pemeriksaan USG dilakukan?_ → `Observation.effectiveDateTime` (1312, tanpa BQ) |
| 84 | 1328–1352 | Observation | 11888-5 | Gestational age US composite estimate | _Usia kehamilan berdasarkan USG - minggu_ → `Observation.valueQuantity.value` (1332, tanpa BQ)<br>_Usia kehamilan berdasarkan hasil USG - hari_ → `Observation.component.code.coding` (1334, tanpa BQ) |
| 85 | 1353–1373 | Observation | 11781-2 | Delivery date US composite estimate | _HPL berdasarkan USG_ → `Observation.valueDateTime` (1357, tanpa BQ) |
| 86 | 1374–1397 | Observation | 3156-7 | Volume of Amniotic fluid | _Jumlah cairan ketuban_ → `Observation.valueQuantity.value` (1377, tanpa BQ)<br>_Interpretasi cairan ketuban_ → `Observation.interpretation.coding` (1379, tanpa BQ) |
| 87 | 1398–1420 | Observation | 11994-1 | Placenta position US | _Lokasi Plasenta_ → `Observation.valueCodeableConcept.coding` (1401, tanpa BQ) |
| 88 | 1422–1433 | Observation | SP000892 | Metode pemantauan kepatuhan konsumsi MMS | _Jenis kegiatan pemantauan MMS yang dilakukan?_ → `Observation.valueCodeableConcept.coding` (1425, tanpa BQ) |
| 89 | 1434–1445 | Observation | 27342004 | Anemia of pregnancy | _Apakah ibu hamil mengalami anemia ?_ → `Observation.valueBoolean` (1437, tanpa BQ) |
| 90 | 1446–1457 | Observation | 182947002 | Administration of prophylactic iron during pregnancy | _Apakah Ibu pernah menerima TTD?_ → `Observation.valueBoolean` (1449, tanpa BQ) |
| 91 | 1458–1475 | MedicationDispense | 93027786 | MMS Multivitamin Ibu Hamil Tablet Salut Selaput (Umum) | _Pemberian MMS_ → `MedicationDispense.contained.resourceType` (1458, tanpa BQ)<br>_Jumlah MMS yang diberikan_ → `MedicationDispense.quantity.value` (1472, tanpa BQ)<br>_Tanggal pemberian MMS kemasan botol_ → `MedicationDispense.whenHandedOver` (1475, tanpa BQ) |
| 92 | 1476–1489 | QuestionnaireResponse | https://fhir.kemkes.go.id/sp/Questionnaire/Q00050 | – | _Apakah QRCode pada kemasan botol MMS bisa discan?_ → `QuestionnaireResponse.item.linkId` (1486, tanpa BQ) |
| 93 | 1490–1490 | MedicationDispense | – | – | _ID Botol MMS_ → `MedicationDispense.identifier.value` (1490, tanpa BQ) |
| 94 | 1491–1501 | Observation | SP000905 | Jumlah tablet MMS yang seharusnya dikonsumsi | _Jumlah tablet MMS yang seharusnya dikonsumsi_ → `Observation.valueInteger` (1494, tanpa BQ) |
| 95 | 1502–1512 | Observation | SP000906 | Jumlah tablet MMS yang sudah dikonsumsi | _Jumlah tablet MMS yang sudah dikonsumsi berdasarkan kartu pemantauan dan pengakuan ibu hamil_ → `Observation.valueInteger` (1505, tanpa BQ) |
| 96 | 1513–1524 | Observation | SP000907 | Hasil Timbangan MMS (gram) | _Hasil Timbangan MMS (gram)_ → `Observation.valueQuantity.value` (1516, tanpa BQ) |
| 97 | 1525–1535 | Observation | SP000908 | Jumlah tablet tersisa | _Jumlah tablet tersisa_ → `Observation.valueInteger` (1528, tanpa BQ) |
| 98 | 1536–1546 | Observation | SP000909 | Jumlah MMS telah dikonsumsi berdasarkan penimbangan | _Jumlah MMS telah dikonsumsi berdasarkan penimbangan_ → `Observation.valueInteger` (1539, tanpa BQ) |
| 99 | 1547–1549 | QuestionnaireResponse | tanpa-URL-1e2ae1 | Kuesioner tanpa URL: Apakah ada tablet MMS yang tidak dikonsumsi (Misal terbuang, | _Apakah ada tablet MMS yang tidak dikonsumsi (Misal terbuang, hilang, atau hal lainnya)? Jika tidak, tulis "0". Jika ada, tulis jumlah tablet yang tidak dikonsumsi!_ → `QuestionnaireResponse.item.linkId` (1547, tanpa BQ) |
| 100 | 1550–1560 | Observation | SP000911 | Total MMS yang telah dikonsumsi berdasarkan hasil penimbangan dan dikurangi MMS yang hilang | _Total MMS yang telah dikonsumsi berdasarkan hasil penimbangan dan dikurangi MMS yang hilang!_ → `Observation.valueInteger` (1553, tanpa BQ) |
| 101 | 1561–1564 | QuestionnaireResponse | tanpa-URL-9a6685 | Kuesioner tanpa URL: Apakah ibu mengonsumsi MMS setiap hari? | _Apakah ibu mengonsumsi MMS setiap hari?_ → `QuestionnaireResponse.item.linkId` (1561, tanpa BQ) |
| 102 | 1565–1583 | MedicationDispense | 93027786 | MMS Multivitamin Ibu Hamil Tablet Salut Selaput (Umum) | _Tanggal pemberian MMS Kemasan Blister pertama kali_ → `MedicationDispense.identifier` (1571, tanpa BQ) |
| 103 | 1584–1594 | Observation | SP000905 | Jumlah tablet MMS yang seharusnya dikonsumsi | _Jumlah tablet MMS yang seharusnya dikonsumsi dari pemberikan blister pertama hingga blister terakhir_ → `Observation.valueInteger` (1587, tanpa BQ) |
| 104 | 1595–1607 | MedicationDispense | – | – | _Tanggal pemberian MMS Kemasan Blister terakhir_ → `MedicationDispense.identifier` (1595, tanpa BQ) |
| 105 | 1608–1621 | QuestionnaireResponse | tanpa-URL-baris1608 | Kuesioner tanpa URL:  | _Apakah QRCode pada kemasan MMS 1 bisa discan?_ → `QuestionnaireResponse.questionnaire` (1608, tanpa BQ) |
| 106 | 1622–1622 | MedicationDispense | – | – | _ID Blister MMS 1_ → `MedicationDispense.identifier.value` (1622, tanpa BQ) |
| 107 | 1623–1634 | Observation | SP000906 | Jumlah tablet MMS yang sudah dikonsumsi | _Jumlah MMS yang sudah dikonsumsi pada blister MMS 1_ → `Observation.focus.display` (1623, tanpa BQ) |
| 108 | 1635–1638 | QuestionnaireResponse | tanpa-URL-062cb4 | Kuesioner tanpa URL: Apakah QRCode pada kemasan MMS 2 bisa discan? | _Apakah QRCode pada kemasan MMS 2 bisa discan?_ → `QuestionnaireResponse.item.linkId` (1635, tanpa BQ) |
| 109 | 1639–1639 | MedicationDispense | – | – | _ID Blister MMS 2_ → `MedicationDispense.identifier.value` (1639, tanpa BQ) |
| 110 | 1640–1651 | Observation | SP000906 | Jumlah tablet MMS yang sudah dikonsumsi | _Jumlah MMS yang sudah dikonsumsi pada blister MMS 2_ → `Observation.focus.display` (1640, tanpa BQ) |
| 111 | 1652–1655 | QuestionnaireResponse | tanpa-URL-9f5d34 | Kuesioner tanpa URL: Apakah QRCode pada kemasan MMS 3 bisa discan? | _Apakah QRCode pada kemasan MMS 3 bisa discan?_ → `QuestionnaireResponse.item.linkId` (1652, tanpa BQ) |
| 112 | 1656–1656 | MedicationDispense | – | – | _ID Blister MMS 3_ → `MedicationDispense.identifier.value` (1656, tanpa BQ) |
| 113 | 1657–1668 | Observation | SP000906 | Jumlah tablet MMS yang sudah dikonsumsi | _Jumlah MMS yang sudah dikonsumsi pada blister MMS 3_ → `Observation.focus.display` (1657, tanpa BQ) |
| 114 | 1669–1679 | Observation | SP000912 | Jumlah tablet MMS yang seharusnya dikonsumsi pada kemasan blister terakhir | _Jumlah tablet MMS yang seharusnya dikonsumsi pada kemasan blister terakhir_ → `Observation.valueInteger` (1672, tanpa BQ) |
| 115 | 1680–1689 | Observation | SP000913 | Jumlah tablet MMS yang sudah dikonsumsi pada kemasan blister terakhir | _Jumlah tablet MMS yang sudah dikonsumsi pada kemasan blister terakhir_ → `Observation.valueInteger` (1683, tanpa BQ) |
| 116 | 1690–1702 | MedicationDispense | – | – | _Berapa jumlah MMS tambahan (back up) yang ibu dapatkan?_ → `MedicationDispense.identifier` (1690, tanpa BQ) |
| 117 | 1703–1712 | Observation | SP000915 | Jumlah konsumsi MMS pada kemasan blister | _Kalkulasi jumlah konsumsi MMS pada "kemasan blister" dari awal sampai akhir. Jika ada, ditambah "konsumsi tablet dari blister tambahan"!_ → `Observation.valueInteger` (1706, tanpa BQ) |
| 118 | 1713–1722 | Observation | SP000914 | Jumlah tablet MMS yang telah dikonsumsi ibu hamil berdasarkan kartu pemantauan | _Kalkulasikan jumlah tablet MMS yang telah dikonsumsi ibu hamil "berdasarkan kartu pemantauan" dari awal sampai hari pemantauan ini_ → `Observation.valueInteger` (1716, tanpa BQ) |
| 119 | 1723–1726 | QuestionnaireResponse | tanpa-URL-9a6685 | Kuesioner tanpa URL: Apakah ibu mengonsumsi MMS setiap hari? | _Apakah ibu mengonsumsi MMS setiap hari?_ → `QuestionnaireResponse.item.linkId` (1723, tanpa BQ) |
| 120 | 1727–1746 | MedicationDispense | 93015491 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | _Pemberian TTD Pertama kali_ → `MedicationDispense.contained.resourceType` (1727, tanpa BQ)<br>_Jumlah TTD yang diberikan pertama kali_ → `MedicationDispense.quantity.value` (1743, tanpa BQ)<br>_Tanggal pemberian TTD pertama kali_ → `MedicationDispense.whenHandedOver` (1746, tanpa BQ) |
| 121 | 1747–1757 | Observation | SP000900 | Jumlah TTD yang seharusnya sudah dikonsumsi | _Jumlah TTD yang seharusnya sudah dikonsumsi_ → `Observation.valueInteger` (1750, tanpa BQ) |
| 122 | 1758–1769 | MedicationDispense | – | – | _Pemberian TTD terakhir kali_ → `MedicationDispense.identifier` (1758, tanpa BQ)<br>_Jumlah TTD yang diberikan terakhir kali_ → `MedicationDispense.quantity.value` (1766, tanpa BQ)<br>_Tanggal pemberian TTD terakhir_ → `MedicationDispense.whenHandedOver` (1769, tanpa BQ) |
| 123 | 1770–1780 | Observation | SP000901 | Jumlah TTD yang seharusnya dikonsumsi pada kemasan terakhir | _Jumlah TTD yang seharusnya dikonsumsi pada kemasan terakhir_ → `Observation.valueInteger` (1773, tanpa BQ) |
| 124 | 1781–1791 | Observation | SP000902 | Jumlah TTD yang telah dikonsumsi bulan ini | _Jumlah TTD yang telah dikonsumsi bulan ini_ → `Observation.valueInteger` (1784, tanpa BQ) |
| 125 | 1792–1802 | Observation | SP000903 | Jumlah TTD yang sudah dikonsumsi dari awal hingga hari ini | _Jumlah TTD yang sudah dikonsumsi dari awal hingga hari ini_ → `Observation.valueInteger` (1795, tanpa BQ) |
| 126 | 1803–1814 | Observation | SP000904 | Ibu mengonsumsi TTD setiap hari | _Apakah ibu mengonsumsi TTD setiap hari?_ → `Observation.valueBoolean` (1806, tanpa BQ) |
| 127 | 1815–1838 | QuestionnaireResponse | https://fhir.kemkes.go.id/sp/Questionnaire/Q00049 | – | _Apakah ada perubahan aroma pada MMS?_ → `QuestionnaireResponse.item.linkId` (1825, tanpa BQ)<br>_Deskripsikan perubahan aroma pada MMS_ → `QuestionnaireResponse.item.item.linkId` (1829, tanpa BQ)<br>_Apakah ada perubahan rasa pada MMS?_ → `QuestionnaireResponse.item.linkId` (1832, tanpa BQ)<br>_Deskripsikan perubahan rasa pada MMS_ → `QuestionnaireResponse.item.item.linkId` (1836, tanpa BQ) |
| 128 | 1839–1850 | Observation | 182948007 | Administration of prophylactic vitamin during pregnancy | _Apakah dalam 2 minggu terakhir ibu ada mengkonsumsi suplemen lain?_ → `Observation.valueBoolean` (1842, tanpa BQ) |
| 129 | 1851–1865 | MedicationStatement | – | – | _Nama suplemen yang dikonsumsi_ → `MedicationStatement.category.coding` (1851, tanpa BQ)<br>_Berapa kali sehari ibu mengkonsumsi suplemen tersebut?_ → `MedicationStatement.dosage.timing.repeat.frequency` (1860, tanpa BQ) |
| 130 | 1866–1868 | Medication | – | – | _Jenis suplemen yang dikonsumsi_ → `Medication.form.coding` (1866, tanpa BQ) |
| 131 | 1869–1878 | Condition | SP000899 | Ibu sakit dalam kurun waktu 2 minggu terakhir | _Apakah dalam 2 minggu terakhir ibu menderita sakit?_ → `Condition.clinicalStatus.coding` (1869, tanpa BQ)<br>_Tanggal mulai sakit_ → `Condition.onsetDateTime` (1873, tanpa BQ)<br>_Tanggal sembuh_ → `Condition.abatementDateTime` (1874, tanpa BQ) |
| 132 | 1879–1892 | Observation | 715035002 | Does take medication | _Apakah ibu mengonsumsi obat?_ → `Observation.valueBoolean` (1882, tanpa BQ) |
| 133 | 1893–1907 | MedicationStatement | – | – | _Nama obat yang dikonsumsi_ → `MedicationStatement.category.coding` (1893, tanpa BQ)<br>_Berapa kali sehari ibu mengkonsumsi obat tersebut?_ → `MedicationStatement.dosage.timing.repeat.frequency` (1902, tanpa BQ) |
| 134 | 1908–1910 | Medication | – | – | _Jenis obat yang dikonsumsi_ → `Medication.form.coding` (1908, tanpa BQ) |
| 135 | 1911–1923 | Observation | 55607006 | Problem | _Tambahkan keterangan atau temuan di lapangan Contoh: Ada tablet MMS yang terjatuh atau dibuang, Kemasan MMS dibuang, Kartu Pemantauan Hilang, dan temuan lainnya_ → `Observation.valueString` (1914, tanpa BQ) |
| 136 | 1926–1935 | ServiceRequest | – | – | – |
| 137 | 1940–1947 | Specimen | – | – | – |
| 138 | 1948–1961 | Observation | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | _Apakah dilakukan pemeriksaan glukosa darah sewaktu?_ → `Observation.status` (1948, tanpa BQ)<br>_Kapan pemeriksaan glukosa darah sewaktu dilakukan?_ → `Observation.effectiveDateTime` (1953, tanpa BQ)<br>_Hasil glukosa darah sewaktu_ → `Observation.valueQuantity.value` (1954, tanpa BQ) |
| 139 | 1962–1973 | DiagnosticReport | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | – |
| 140 | 1975–1997 | Observation | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | _Dimana pemeriksaan glukosa darah sewaktu dilakukan?_ → `Observation.performer.identifier` (1986, tanpa BQ)<br>_Nama fasilitas kesehatan tempat pemeriksaan glukosa darah sewaktu_ → `Observation.performer.display` (1991, tanpa BQ)<br>_Siapa nama tenaga kesehatan yang melakukan pemeriksaan?_ → `Observation.performer.identifier` (1992, tanpa BQ) |
| 141 | 1998–2007 | ServiceRequest | – | – | – |
| 142 | 2012–2019 | Specimen | – | – | – |
| 143 | 2020–2037 | Observation | 718-7 | Hemoglobin [Mass/volume] in Blood | _Apakah dilakukan pemeriksaan hemoglobin?_ → `Observation.status` (2020, tanpa BQ)<br>_Kapan pemeriksaan hemoglobin dilakukan?_ → `Observation.effectiveDateTime` (2025, tanpa BQ)<br>_Hasil pemeriksaan hemoglobin_ → `Observation.valueQuantity.value` (2026, tanpa BQ) |
| 144 | 2038–2049 | DiagnosticReport | 718-7 | Hemoglobin [Mass/volume] in Blood | – |
| 145 | 2050–2077 | Observation | 718-7 | Hemoglobin [Mass/volume] in Blood | _Apakah sudah dilakukan pemeriksaan hemoglobin pada kunjukan K saat ini?_ → `Observation.valueQuantity.value` (2056, tanpa BQ)<br>_Dimana pemeriksaan hemoglobin dilakukan?_ → `Observation.performer.identifier` (2066, tanpa BQ)<br>_Nama fasilitas kesehatan tempat pemeriksaan hemoglobin_ → `Observation.performer.display` (2071, tanpa BQ)<br>_Siapa nama tenaga kesehatan yang melakukan pemeriksaan?_ → `Observation.performer.identifier` (2072, tanpa BQ) |
| 146 | 2078–2087 | ServiceRequest | – | – | – |
| 147 | 2092–2099 | Specimen | – | – | – |
| 148 | 2100–2113 | Observation | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | _Apakah dilakukan pemeriksaan hepatitis B (HBsAG)?_ → `Observation.status` (2100, tanpa BQ)<br>_Kapan pemeriksaan hepatitis B (HBsAG) dilakukan?_ → `Observation.effectiveDateTime` (2105, tanpa BQ)<br>_Hasil pemeriksaan HBsAG dengan immunoassay_ → `Observation.valueCodeableConcept.coding` (2106, tanpa BQ) |
| 149 | 2114–2125 | DiagnosticReport | – | – | – |
| 150 | 2127–2149 | Observation | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | _Dimana pemeriksaan hepatitis B (HBsAG) dilakukan?_ → `Observation.performer.identifier` (2138, tanpa BQ)<br>_Nama fasilitas kesehatan tempat pemeriksaan hepatitis B (HBsAG)_ → `Observation.performer.display` (2143, tanpa BQ)<br>_Siapa nama tenaga kesehatan yang melakukan pemeriksaan?_ → `Observation.performer.identifier` (2144, tanpa BQ) |
| 151 | 2150–2160 | ServiceRequest | – | – | – |
| 152 | 2165–2172 | Specimen | – | – | – |
| 153 | 2173–2188 | Observation | 11258-1 | Hepatitis B virus DNA [Units/volume] in Serum | _Apakah dilakukan pemeriksaan lanjutan Hepatitis B (direkomendasikan di usia kehamilan 24 - 26 minggu)?_ → `Observation.status` (2173, tanpa BQ)<br>_Kapan pemeriksaan lanjutan hepatitis B dilakukan?_ → `Observation.effectiveDateTime` (2175, tanpa BQ)<br>_Jenis pemeriksaan lanjutan hepatitis B_ → `Observation.category.coding` (2176, tanpa BQ)<br>_Hasil pemeriksaan lanjutan hepatitis B dengan HBV DNA (IU/mL) (direkomendasikan)_ → `Observation.valueQuantity.value` (2179, tanpa BQ)<br>_Hasil pemeriksaan lanjutan hepatitis B dengan Diagnostik Cepat HBeAg (RDT)_ → `Observation.valueCodeableConcept.coding` (2181, tanpa BQ) |
| 154 | 2189–2191 | DiagnosticReport | – | – | – |
| 155 | 2192–2202 | DiagnosticReport | – | – | – |
| 156 | 2204–2228 | Observation | 11258-1 | Hepatitis B virus DNA [Units/volume] in Serum | _Dimana pemeriksaan lanjutan Hepatitis B dilakukan?_ → `Observation.performer.identifier` (2217, tanpa BQ)<br>_Nama fasilitas kesehatan tempat pemeriksaan lanjutan Hepatitis B_ → `Observation.performer.display` (2222, tanpa BQ)<br>_Siapa nama tenaga kesehatan yang melakukan pemeriksaan?_ → `Observation.performer.identifier` (2223, tanpa BQ) |
| 157 | 2229–2238 | ServiceRequest | – | – | – |
| 158 | 2243–2250 | Specimen | – | – | – |
| 159 | 2251–2264 | Observation | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | _Apakah dilakukan pemeriksaan HIV?_ → `Observation.status` (2251, tanpa BQ)<br>_Kapan pemeriksaan HIV dilakukan?_ → `Observation.effectiveDateTime` (2256, tanpa BQ)<br>_Hasil pemeriksaan HIV_ → `Observation.valueCodeableConcept.coding` (2257, tanpa BQ) |
| 160 | 2265–2276 | DiagnosticReport | – | – | – |
| 161 | 2278–2300 | Observation | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | _Dimana pemeriksaan HIV dilakukan?_ → `Observation.performer.identifier` (2289, tanpa BQ)<br>_Nama fasilitas kesehatan tempat pemeriksaan HIV_ → `Observation.performer.display` (2294, tanpa BQ)<br>_Siapa nama tenaga kesehatan yang melakukan pemeriksaan?_ → `Observation.performer.identifier` (2295, tanpa BQ) |
| 162 | 2301–2310 | ServiceRequest | – | – | – |
| 163 | 2315–2322 | Specimen | – | – | – |
| 164 | 2323–2336 | Observation | 22464-2 | Reagin Ab [Presence] in Specimen | _Apakah dilakukan pemeriksaan sifilis?_ → `Observation.status` (2323, tanpa BQ)<br>_Kapan pemeriksaan sifilis dilakukan?_ → `Observation.effectiveDateTime` (2328, tanpa BQ)<br>_Hasil pemeriksaan sifilis_ → `Observation.valueCodeableConcept.coding` (2329, tanpa BQ) |
| 165 | 2337–2348 | DiagnosticReport | – | – | – |
| 166 | 2350–2372 | Observation | 20508-8 | Reagin Ab [Units/volume] in Serum or Plasma by RPR | _Dimana pemeriksaan sifilis dilakukan?_ → `Observation.performer.identifier` (2361, tanpa BQ)<br>_Nama fasilitas kesehatan tempat pemeriksaan sifilis_ → `Observation.performer.display` (2366, tanpa BQ)<br>_Siapa nama tenaga kesehatan yang melakukan pemeriksaan?_ → `Observation.performer.identifier` (2367, tanpa BQ) |
| 167 | 2373–2382 | ServiceRequest | – | – | – |
| 168 | 2387–2394 | Specimen | – | – | – |
| 169 | 2395–2411 | Observation | 20454-5 | Protein [Presence] in Urine by Test strip | _Apakah dilakukan pemeriksaan dipstick protein urin?_ → `Observation.status` (2395, tanpa BQ)<br>_Kapan pemeriksaan dipstick protein urin dilakukan?_ → `Observation.effectiveDateTime` (2400, tanpa BQ)<br>_Hasil pemeriksaan dipstick urine - protein_ → `Observation.valueCodeableConcept.coding` (2401, tanpa BQ) |
| 170 | 2412–2423 | DiagnosticReport | – | – | – |
| 171 | 2425–2450 | Observation | 20454-5 | Protein [Presence] in Urine by Test strip | _Dimana pemeriksaan dipstick protein urin dilakukan?_ → `Observation.performer.identifier` (2439, tanpa BQ)<br>_Nama fasilitas kesehatan tempat pemeriksaan dipstick protein urin_ → `Observation.performer.display` (2444, tanpa BQ)<br>_Siapa nama tenaga kesehatan yang melakukan pemeriksaan?_ → `Observation.performer.identifier` (2445, tanpa BQ) |
| 172 | 2451–2460 | ServiceRequest | – | – | – |
| 173 | 2465–2472 | Specimen | – | – | – |
| 174 | 2473–2489 | Observation | 25428-4 | Glucose [Presence] in Urine by Test strip | _Apakah dilakukan pemeriksaan glukosa urin?_ → `Observation.status` (2473, tanpa BQ)<br>_Kapan pemeriksaan urin dilakukan?_ → `Observation.effectiveDateTime` (2478, tanpa BQ)<br>_Hasil pemeriksaan dipstick urine - glukosa_ → `Observation.valueCodeableConcept.coding` (2479, tanpa BQ) |
| 175 | 2490–2501 | DiagnosticReport | – | – | – |
| 176 | 2502–2511 | ServiceRequest | – | – | – |
| 177 | 2516–2523 | Specimen | – | – | – |
| 178 | 2524–2537 | Observation | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | _Apakah dilakukan pemeriksaan tuberkulosis?_ → `Observation.status` (2524, tanpa BQ)<br>_Kapan pemeriksaan tuberkulosis dilakukan?_ → `Observation.effectiveDateTime` (2528, tanpa BQ)<br>_Hasil pemeriksaan TCM tuberkulosis_ → `Observation.valueCodeableConcept.coding` (2529, tanpa BQ) |
| 179 | 2538–2549 | DiagnosticReport | – | – | – |
| 180 | 2550–2566 | Condition | 169943008 | Mother less than 20 years old | _Apakah ibu merupakan ibu dengan kehamilan resiko tinggi?_ → `Condition.clinicalStatus.coding` (2550, tanpa BQ)<br>_Apa resiko kehamilan ibu?_ → `Condition.code.coding` (2552, tanpa BQ) |
| 181 | 2567–2595 | MedicationRequest | 93015491 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | _Apakah ibu diberikan tablet TTD_ → `MedicationRequest.contained.resourceType` (2567, tanpa BQ) |
| 182 | 2596–2622 | MedicationDispense | 93015491 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | _Berapa jumlah TTD yang diberikan ke Ibu hamil?_ → `MedicationDispense.quantity.value` (2619, tanpa BQ) |
| 183 | 2623–2645 | MedicationRequest | SP000370 | Multiple Micronutrient Supplement | _Apakah Ibu diberikan tablet MMS?_ → `MedicationRequest.contained.resourceType` (2623, tanpa BQ) |
| 184 | 2646–2665 | MedicationDispense | SP000370 | Multiple Micronutrient Supplement | _Kapan tanggal diberikan MMS oleh tenaga kesehatan_ → `MedicationDispense.whenHandedOver` (2662, tanpa BQ)<br>_Berapa jumlah MMS yang diberikan ke Ibu Hamil?_ → `MedicationDispense.quantity.value` (2663, tanpa BQ) |
| 185 | 2666–2672 | Observation | SP000007 | Tatalaksana Anemia | _Apakah dilakukan tatalaksana anemia berikut?_ → `Observation.valueCodeableConcept.coding` (2669, tanpa BQ) |
| 186 | 2674–2710 | Observation | SP000012 | Tatalaksana Pre Eklampsia | _Sebutkan tatalaksana anemia lainnya!_ → `Observation.valueCodeableConcept.text` (2675, tanpa BQ)<br>_Apakah dilakukan tatalaksana preeklampsia berikut?_ → `Observation.valueBoolean` (2687, tanpa BQ)<br>_Sebutkan tatalaksana preeklampsia lainnya!_ → `Observation.component.valueString` (2703, tanpa BQ) |
| 187 | 2711–2721 | Observation | SP000014 | Tatalaksana KEK | _Apakah dilakukan tatalaksana KEK_ → `Observation.valueBoolean` (2714, tanpa BQ) |
| 188 | 2723–2742 | Observation | SP000016 | Tatalaksana Masalah Kesehatan | _Apakah diberikan tatalaksana risiko masalah kesehatan lainnya?_ → `Observation.valueBoolean` (2733, tanpa BQ)<br>_Sebutkan tatalaksana risiko masalah kesehatan lainnya!_ → `Observation.component.valueString` (2735, tanpa BQ) |
| 189 | 2743–2747 | Procedure | 1230101008 | Counseling for pregnancy | _Apakah dilakukan konseling Ibu hamil?_ → `Procedure.category.coding` (2743, tanpa BQ)<br>_Jika ya, topik konseling apa yang diberikan kepada Ibu hamil?_ → `Procedure.code.coding.code` (2747, tanpa BQ) |
| 190 | 2748–2767 | Procedure | ED000008 | Edukasi Tanda Bahaya Kehamilan, Bersalin dan Nifas | _Sebutkan topik konseling lainnya!_ → `Procedure.code.text` (2760, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 113 |
| MedicationDispense | 13 |
| ServiceRequest | 10 |
| DiagnosticReport | 10 |
| QuestionnaireResponse | 9 |
| Specimen | 9 |
| Procedure | 6 |
| Condition | 5 |
| MedicationStatement | 4 |
| Immunization | 3 |
| MedicationRequest | 3 |
| Medication | 2 |
| FamilyMemberHistory | 1 |
| Encounter | 1 |
| CarePlan | 1 |
| **Total** | **190** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 5 | Observation | `Observation.code.coding` | SP000699 | Kelompok Dasawisma | http://terminology.kemkes.go.id/sp |
| 2 | 17 | Observation | `Observation.code.coding` | SP000798 | Usia kehamilan saat melakukan pendaftaran posyandu | http://terminology.kemkes.go.id/sp |
| 3 | 29 | Observation | `Observation.code.coding` | SP000713 | Bulan Pendaftaran Posyandu | http://terminology.kemkes.go.id/sp |
| 4 | 41 | Observation | `Observation.code.coding` | 8302-2 | Body height | http://loinc.org |
| 5 | 42 | Observation | `Observation.code.coding` | ANC.B8.DE1 | Height | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 6 | 54 | Observation | `Observation.code.coding` | 56077-1 | Body weight --pre current pregnancy | http://loinc.org |
| 7 | 55 | Observation | `Observation.code.coding` | ANC.B8.DE2 | Pre-gestational weight | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 8 | 67 | Observation | `Observation.code.coding` | OC000010 | Indeks Massa Tubuh Sebelum Hamil | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 9 | 68 | Observation | `Observation.code.coding` | ANC.SS.DE58 | IMT Sebelum Hamil | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 10 | 78 | Observation | `Observation.interpretation.coding` | 717933005 | Severe thinness in adulthood | http://snomed.info/sct |
| 11 | 81 | Observation | `Observation.interpretation.coding` | 248342006 | Underweight | http://snomed.info/sct |
| 12 | 84 | Observation | `Observation.interpretation.coding` | 43664005 | Normal weight | http://snomed.info/sct |
| 13 | 89 | Observation | `Observation.interpretation.coding` | 238131007 | Overweight | http://snomed.info/sct |
| 14 | 94 | Observation | `Observation.interpretation.coding` | 414915002 | Obese | http://snomed.info/sct |
| 15 | 107 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 16 | 108 | Observation | `Observation.code.coding` | ANC.B8.DE3 | Current weight | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 17 | 120 | Observation | `Observation.code.coding` | 284473002 | Mid upper arm circumference | http://snomed.info/sct |
| 18 | 121 | Observation | `Observation.code.coding` | ANC.SS.DE3 | Lingkar Lengan Atas (LILA) | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 19 | 131 | Observation | `Observation.interpretation` | OI000018 | Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 20 | 132 | Observation | `Observation.interpretation` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 21 | 133 | Observation | `Observation.interpretation` | OI000035 | Risiko Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 22 | 136 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 23 | 137 | Observation | `Observation.code.coding` | ANC.B8.DE17 | Systolic blood pressure | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 24 | 149 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://loinc.org |
| 25 | 150 | Observation | `Observation.code.coding` | ANC.B8.DE19 | Diastolic blood pressure | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 26 | 162 | Observation | `Observation.code.coding` | 1285244000 | Mean arterial pressure | http://snomed.info/sct |
| 27 | 174 | Observation | `Observation.code.coding` | SP000010 | Skrining Hipertensi dalam Kehamilan | http://terminology.kemkes.go.id/sp |
| 28 | 175 | Observation | `Observation.valueCodeableConcept.coding` | SP000011 | Tidak Pre Eklampsia/ Eklampsia | http://terminology.kemkes.go.id/sp |
| 29 | 176 | Observation | `Observation.valueCodeableConcept.coding` | 48194001 | Pregnancy-induced hypertension | http://snomed.info/sct |
| 30 | 177 | Observation | `Observation.valueCodeableConcept.coding` | 398254007 | Pre-eclampsia | http://snomed.info/sct |
| 31 | 178 | Observation | `Observation.valueCodeableConcept.coding` | 15938005 | Eclampsia | http://snomed.info/sct |
| 32 | 179 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 33 | 189 | Observation | `Observation.code.coding` | 8310-5 | Body temperature | http://loinc.org |
| 34 | 190 | Observation | `Observation.code.coding` | ANC.B8.DE34 | Body temperature | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 35 | 202 | Observation | `Observation.code.coding` | 8867-4 | Heart Rate | http://loinc.org |
| 36 | 203 | Observation | `Observation.code.coding` | ANC.B8.DE36 | Pulse rate | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 37 | 215 | Observation | `Observation.code.coding` | 250554003 | Measurement of oxygen saturation at periphery | http://snomed.info/sct |
| 38 | 228 | Condition | `Condition.code.coding` | 68154008 | Chronic cough | http://snomed.info/sct |
| 39 | 229 | Condition | `Condition.code.coding` | SP000465 | Demam, menggigil, berkeringat | http://terminology.kemkes.go.id/sp |
| 40 | 230 | Condition | `Condition.code.coding` | SP000466 | Diare berulang | http://terminology.kemkes.go.id/sp |
| 41 | 231 | Condition | `Condition.code.coding` | 248657009 | Pounding heart | http://snomed.info/sct |
| 42 | 232 | Condition | `Condition.code.coding` | 29857009 | Chest pain | http://snomed.info/sct |
| 43 | 233 | Condition | `Condition.code.coding` | SP000467 | Sulit tidur dan cemas berlebihan | http://terminology.kemkes.go.id/sp |
| 44 | 234 | Condition | `Condition.code.coding` | 413320001 | Physical health problem | http://snomed.info/sct |
| 45 | 242 | Observation | `Observation.code.coding` | 416471007 | Family history of clinical finding | http://snomed.info/sct |
| 46 | 245 | Observation | `Observation.component.code.coding` | 160279000 | Family history of infectious disease | http://snomed.info/sct |
| 47 | 248 | Observation | `Observation.component.code.coding` | 160303001 | Family history of diabetes mellitus | http://snomed.info/sct |
| 48 | 251 | Observation | `Observation.component.code.coding` | 160311006 | Family history: Obesity | http://snomed.info/sct |
| 49 | 254 | Observation | `Observation.component.code.coding` | 160280002 | Family history: Tuberculosis | http://snomed.info/sct |
| 50 | 257 | Observation | `Observation.component.code.coding` | 429959009 | Family history of heart failure | http://snomed.info/sct |
| 51 | 260 | Observation | `Observation.component.code.coding` | 300933005 | Family history: Autoimmune disease | http://snomed.info/sct |
| 52 | 263 | Observation | `Observation.component.code.coding` | 275130003 | Family history: Hepatitis | http://snomed.info/sct |
| 53 | 266 | Observation | `Observation.component.code.coding` | 160281003 | Family history: Syphilis | http://snomed.info/sct |
| 54 | 269 | Observation | `Observation.component.code.coding` | 160357008 | Family history: Hypertension | http://snomed.info/sct |
| 55 | 272 | Observation | `Observation.component.code.coding` | 160324006 | Family history of mental disorder | http://snomed.info/sct |
| 56 | 275 | Observation | `Observation.component.code.coding` | 160377001 | Family history: Asthma | http://snomed.info/sct |
| 57 | 278 | Observation | `Observation.component.code.coding` | 74964007 | Other | http://snomed.info/sct |
| 58 | 289 | Observation | `Observation.code.coding` | 417662000 | History of clinical finding in subject | http://snomed.info/sct |
| 59 | 292 | Observation | `Observation.component.code.coding` | 40733004 | Infectious disease | http://snomed.info/sct |
| 60 | 295 | Observation | `Observation.component.code.coding` | 73211009 | Diabetes mellitus | http://snomed.info/sct |
| 61 | 298 | Observation | `Observation.component.code.coding` | 414916001 | Obesity | http://snomed.info/sct |
| 62 | 301 | Observation | `Observation.component.code.coding` | 56717001 | Tuberculosis | http://snomed.info/sct |
| 63 | 304 | Observation | `Observation.component.code.coding` | 56265001 | Heart disease | http://snomed.info/sct |
| 64 | 307 | Observation | `Observation.component.code.coding` | 85828009 | Autoimmune disease | http://snomed.info/sct |
| 65 | 310 | Observation | `Observation.component.code.coding` | 66071002 | Viral hepatitis type B | http://snomed.info/sct |
| 66 | 313 | Observation | `Observation.component.code.coding` | 76272004 | Syphilis | http://snomed.info/sct |
| 67 | 316 | Observation | `Observation.component.code.coding` | 38341003 | Hypertensive disorder, systemic arterial | http://snomed.info/sct |
| 68 | 319 | Observation | `Observation.component.code.coding` | 74732009 | Mental disorder | http://snomed.info/sct |
| 69 | 322 | Observation | `Observation.component.code.coding` | 195967001 | Asthma | http://snomed.info/sct |
| 70 | 325 | Observation | `Observation.component.code.coding` | 74964007 | Other | http://snomed.info/sct |
| 71 | 336 | Observation | `Observation.code.coding` | SP000412 | Tanda Bahaya Kehamilan | http://terminology.kemkes.go.id/sp |
| 72 | 339 | Observation | `Observation.component.code.coding` | SP000498 | Demam Tinggi | http://terminology.kemkes.go.id/sp |
| 73 | 342 | Observation | `Observation.component.code.coding` | 309737007 | Abdominal pain in pregnancy | http://snomed.info/sct |
| 74 | 345 | Observation | `Observation.component.code.coding` | 14094001 | Excessive vomiting in pregnancy | http://snomed.info/sct |
| 75 | 348 | Observation | `Observation.component.code.coding` | 289530006 | Vaginal bleeding | http://snomed.info/sct |
| 76 | 351 | Observation | `Observation.component.code.coding` | 49650001 | Dysuria | http://snomed.info/sct |
| 77 | 354 | Observation | `Observation.component.code.coding` | 428252001 | Vaginitis in pregnancy | http://snomed.info/sct |
| 78 | 357 | Observation | `Observation.component.code.coding` | 8765009 | Hematemesis | http://snomed.info/sct |
| 79 | 360 | Observation | `Observation.component.code.coding` | SP000459 | Nafas pendek dan jantung berbedar | http://terminology.kemkes.go.id/sp |
| 80 | 363 | Observation | `Observation.component.code.coding` | 111516008 | Blurring of visual image | http://snomed.info/sct |
| 81 | 366 | Observation | `Observation.component.code.coding` | 44223004 | Premature rupture of membranes | http://snomed.info/sct |
| 82 | 369 | Observation | `Observation.component.code.coding` | 37796009 | Migraine | http://snomed.info/sct |
| 83 | 372 | Observation | `Observation.component.code.coding` | 289432001 | Fetal movements absent | http://snomed.info/sct |
| 84 | 375 | Observation | `Observation.component.code.coding` | SP000499 | Ketuban pecah namun kontraksi | http://terminology.kemkes.go.id/sp |
| 85 | 378 | Observation | `Observation.component.code.coding` | SP000500 | Nyeri perut hebat di antara kontraksi | http://terminology.kemkes.go.id/sp |
| 86 | 381 | Observation | `Observation.component.code.coding` | 74964007 | Other | http://snomed.info/sct |
| 87 | 392 | Observation | `Observation.code.coding` | 11996-6 | [#] Pregnancies | http://loinc.org |
| 88 | 393 | Observation | `Observation.code.coding` | ANC.B6.DE24 | Number of pregnancies (gravida) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 89 | 404 | Observation | `Observation.code.coding` | 11977-6 | [#] Parity | http://loinc.org |
| 90 | 405 | Observation | `Observation.code.coding` | ANC.B6.DE32 | Parity | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 91 | 416 | Observation | `Observation.code.coding` | 69043-8 | Other pregnancy outcomes # | http://loinc.org |
| 92 | 417 | Observation | `Observation.code.coding` | ANC.B6.DE25 | Number of miscarriages and/or abortions | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 93 | 428 | Condition | `Condition.code.coding` | 86406008 | Human immunodeficiency virus infection | http://snomed.info/sct |
| 94 | 429 | Condition | `Condition.code.coding` | 161445009 | History of diabetes mellitus | http://snomed.info/sct |
| 95 | 430 | Condition | `Condition.code.coding` | 429721005 | History of hepatitis B | http://snomed.info/sct |
| 96 | 431 | Condition | `Condition.code.coding` | 1087151000119108 | History of syphilis | http://snomed.info/sct |
| 97 | 432 | Condition | `Condition.code.coding` | 161416007 | History of malaria | http://snomed.info/sct |
| 98 | 433 | Condition | `Condition.code.coding` | 161414005 | History of tuberculosis | http://snomed.info/sct |
| 99 | 449 | Immunization | `Immunization.vaccineCode` | VG139 | Td | http://sys-ids.kemkes.go.id/kfa |
| 100 | 461 | Immunization | `Immunization.vaccineCode.coding` | VG139 | Td | http://sys-ids.kemkes.go.id/kfa |
| 101 | 479 | Immunization | `Immunization.vaccineCode` | VG139 | Td | http://sys-ids.kemkes.go.id/kfa |
| 102 | 492 | Observation | `Observation.code.coding` | SP000510 | Mendapat Makanan Bergizi Gratis (MBG) bulan ini | http://terminology.kemkes.go.id/sp |
| 103 | 514 | Observation | `Observation.code.coding` | SP000955 | Mengonsumsi tablet tambah darah dalam 24 jam terakhir | http://terminology.kemkes.go.id/sp |
| 104 | 529 | MedicationStatement | `MedicationStatement.medicationCodeableConcept.coding` | SP000370 | Multiple Micronutrient Supplement | http://terminology.kemkes.go.id/sp |
| 105 | 540 | Observation | `Observation.code.coding` | SP000046 | Terapi Antiretroviral (ART) | http://terminology.kemkes.go.id/sp |
| 106 | 552 | Observation | `Observation.code.coding` | SP000124 | Obat anti malaria | http://terminology.kemkes.go.id/sp |
| 107 | 555 | Observation | `Observation.component.code.coding` | 432555000 | Product containing artesunate | http://snomed.info/sct |
| 108 | 558 | Observation | `Observation.component.code.coding` | 64115004 | Product containing amodiaquine | http://snomed.info/sct |
| 109 | 561 | Observation | `Observation.component.code.coding` | 324919005 | Product containing precisely quinine sulfate 200 milligram/1 each conventional release oral tablet | http://snomed.info/sct |
| 110 | 573 | Observation | `Observation.code.coding` | SP000157 | Obat Diabetes Mellitus | http://terminology.kemkes.go.id/sp |
| 111 | 585 | Observation | `Observation.code.coding` | SP000424 | Riwayat Perilaku Berisiko Sebelum Hamil | http://terminology.kemkes.go.id/sp |
| 112 | 587 | Observation | `Observation.component.code.coding` | 67961000119106 | Caffeine user | http://snomed.info/sct |
| 113 | 590 | Observation | `Observation.component.code.coding` | 110483000 | Tobacco user | http://snomed.info/sct |
| 114 | 593 | Observation | `Observation.component.code.coding` | 77176002 | Smoker | http://snomed.info/sct |
| 115 | 596 | Observation | `Observation.component.code.coding` | 94151000119101 | Smoker in household | http://snomed.info/sct |
| 116 | 599 | Observation | `Observation.component.code.coding` | 219006 | Current drinker of alcohol | http://snomed.info/sct |
| 117 | 602 | Observation | `Observation.component.code.coding` | 43994002 | Lack of physical activity | http://snomed.info/sct |
| 118 | 605 | Observation | `Observation.component.code.coding` | SP000426 | Penggunaan Kosmetik Yang Mengandung Zat Berbahaya | http://terminology.kemkes.go.id/sp |
| 119 | 608 | Observation | `Observation.component.code.coding` | SP000425 | Konsumsi Obat Teratogenik | http://terminology.kemkes.go.id/sp |
| 120 | 611 | Observation | `Observation.component.code.coding` | 308658001 | Abnormal eating pattern | http://snomed.info/sct |
| 121 | 614 | Observation | `Observation.component.code.coding` | 74964007 | Other | http://snomed.info/sct |
| 122 | 626 | Observation | `Observation.code.coding` | 1156096005 | Past pregnancy history of complication occurring during labor and delivery | http://snomed.info/sct |
| 123 | 628 | Observation | `Observation.component.code.coding` | 161744009 | Past pregnancy history of miscarriage | http://snomed.info/sct |
| 124 | 631 | Observation | `Observation.component.code.coding` | 16216731000119106 | Past pregnancy history of intrauterine fetal death | http://snomed.info/sct |
| 125 | 634 | Observation | `Observation.component.code.coding` | 161805006 | Past pregnancy history of cesarean section | http://snomed.info/sct |
| 126 | 637 | Observation | `Observation.component.code.coding` | 161810005 | Past pregnancy history of prolonged labor | http://snomed.info/sct |
| 127 | 640 | Observation | `Observation.component.code.coding` | 725948004 | Past pregnancy history of retained placenta | http://snomed.info/sct |
| 128 | 643 | Observation | `Observation.component.code.coding` | 726565008 | Past pregnancy history of small for gestational age baby | http://snomed.info/sct |
| 129 | 646 | Observation | `Observation.component.code.coding` | 32271000119102 | Past pregnancy history of delivery of macrosomal infant | http://snomed.info/sct |
| 130 | 649 | Observation | `Observation.component.code.coding` | 161804005 | Past pregnancy history of antepartum hemorrhage | http://snomed.info/sct |
| 131 | 652 | Observation | `Observation.component.code.coding` | 105651000119100 | Past pregnancy history of pre-eclampsia | http://snomed.info/sct |
| 132 | 655 | Observation | `Observation.component.code.coding` | 161806007 | Past pregnancy history of eclampsia | http://snomed.info/sct |
| 133 | 667 | Condition | `Condition.code.coding` | 34842007 | Antepartum hemorrhage | http://snomed.info/sct |
| 134 | 668 | Condition | `Condition.code.coding` | 15938005 | Eclampsia | http://snomed.info/sct |
| 135 | 669 | Condition | `Condition.code.coding` | 398254007 | Pre-eclampsia | http://snomed.info/sct |
| 136 | 670 | Condition | `Condition.code.coding` | 386639001 | Termination of pregnancy | http://snomed.info/sct |
| 137 | 671 | Condition | `Condition.code.coding` | 40733004 | Infectious disease | http://snomed.info/sct |
| 138 | 672 | Condition | `Condition.code.coding` | 91302008 | Sepsis | http://snomed.info/sct |
| 139 | 673 | Condition | `Condition.code.coding` | 74964007 | Other | http://snomed.info/sct |
| 140 | 682 | Observation | `Observation.code.coding` | 17566005 | Class in prenatal exercises | http://snomed.info/sct |
| 141 | 694 | Observation | `Observation.code.coding` | 52829-9 | Place of service | http://loinc.org |
| 142 | 705 | Observation | `Observation.code.coding` | SP000764 | Pendamping kelas ibu hamil | http://terminology.kemkes.go.id/sp |
| 143 | 706 | Observation | `Observation.valueCodeableConcept.coding` | 127848009 | Spouse | http://snomed.info/sct |
| 144 | 707 | Observation | `Observation.valueCodeableConcept.coding` | 375005 | Sibling | http://snomed.info/sct |
| 145 | 708 | Observation | `Observation.valueCodeableConcept.coding` | EHA000002 | Datang sendiri | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 146 | 709 | Observation | `Observation.valueCodeableConcept.coding` | EHA000001 | Kader/ Komunitas | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 147 | 720 | MedicationRequest | `MedicationRequest.contained.code.coding` | 91000488 | Iodine | http://sys-ids.kemkes.go.id/kfa |
| 148 | 740 | MedicationDispense | `MedicationDispense.contained.code.coding` | 91000488 | Iodine | http://sys-ids.kemkes.go.id/kfa |
| 149 | 754 | Procedure | `Procedure.code.coding` | 385892002 | Mental health screening | http://snomed.info/sct |
| 150 | 766 | Observation | `Observation.code.coding` | SP000730 | Tindak lanjut hasil skrining kesehatan jiwa | http://terminology.kemkes.go.id/sp |
| 151 | 768 | Observation | `Observation.component.code.coding` | 409073007 | Education | http://snomed.info/sct |
| 152 | 771 | Observation | `Observation.component.code.coding` | 409063005 | Counseling | http://snomed.info/sct |
| 153 | 774 | Observation | `Observation.component.code.coding` | 3457005 | Patient referral | http://snomed.info/sct |
| 154 | 789 | ServiceRequest | `ServiceRequest.code` | 737492002 | Outpatient care management | http://snomed.info/sct |
| 155 | 790 | ServiceRequest | `ServiceRequest.reasonCode.coding` | 306227000 | Referral for mental health counseling | http://snomed.info/sct |
| 156 | 827 | Observation | `Observation.interpretation.coding` | 772170009 | Tuberculosis suspected | http://snomed.info/sct |
| 157 | 828 | Observation | `Observation.interpretation.coding` | SP000789 | Bukan terduga TBC | http://terminology.kemkes.go.id/sp |
| 158 | 831 | Observation | `Observation.code.coding` | 171126009 | Tuberculosis screening | http://snomed.info/sct |
| 159 | 841 | Observation | `Observation.code.coding` | SP000779 | Multipara dengan kehamilan oleh pasangan baru | http://terminology.kemkes.go.id/sp |
| 160 | 853 | Observation | `Observation.code.coding` | 813541000000100 | Pregnancy resulting from assisted conception | http://snomed.info/sct |
| 161 | 865 | Observation | `Observation.code.coding` | SP000780 | Umur ≥ 35 Tahun | http://terminology.kemkes.go.id/sp |
| 162 | 877 | Observation | `Observation.code.coding` | 102877006 | Nulliparous | http://snomed.info/sct |
| 163 | 889 | Observation | `Observation.code.coding` | SP000781 | Multipara yang Jarak Kehamilan Sebelumnya > 10 Tahun | http://terminology.kemkes.go.id/sp |
| 164 | 901 | Observation | `Observation.code.coding` | 700190003 | Family history of pre-eclampsia | http://snomed.info/sct |
| 165 | 913 | Observation | `Observation.code.coding` | 162864005 | Body mass index 30+ - obesity | http://snomed.info/sct |
| 166 | 925 | Observation | `Observation.code.coding` | SP000782 | Multipara Dengan Riwayat Preeklampsia Sebelumnya | http://terminology.kemkes.go.id/sp |
| 167 | 937 | Observation | `Observation.code.coding` | 16356006 | Multiple pregnancy | http://snomed.info/sct |
| 168 | 949 | Observation | `Observation.code.coding` | 11687002 | Gestational diabetes mellitus | http://snomed.info/sct |
| 169 | 961 | Observation | `Observation.code.coding` | 8762007 | Chronic hypertension in obstetric context | http://snomed.info/sct |
| 170 | 973 | Observation | `Observation.code.coding` | 90708001 | Kidney disease | http://snomed.info/sct |
| 171 | 985 | Observation | `Observation.code.coding` | 85828009 | Autoimmune disease | http://snomed.info/sct |
| 172 | 997 | Observation | `Observation.code.coding` | 26843008 | Antiphospholipid syndrome | http://snomed.info/sct |
| 173 | 1009 | Observation | `Observation.code.coding` | SP000783 | Mean Arterial Presure > 90 mmHg | http://terminology.kemkes.go.id/sp |
| 174 | 1021 | Observation | `Observation.code.coding` | 29738008 | Proteinuria | http://snomed.info/sct |
| 175 | 1033 | Observation | `Observation.code.coding` | SP000799 | Hasil skrining Preeklampsia | http://terminology.kemkes.go.id/sp |
| 176 | 1034 | Observation | `Observation.valueCodeableConcept.coding` | SP000784 | Berisiko Preeklampsia | http://terminology.kemkes.go.id/sp |
| 177 | 1035 | Observation | `Observation.valueCodeableConcept.coding` | SP000785 | Tidak Berisiko Preeklampsia | http://terminology.kemkes.go.id/sp |
| 178 | 1045 | Observation | `Observation.code.coding` | 1237486008 | Pale discoloration of entire skin of body | http://snomed.info/sct |
| 179 | 1057 | Observation | `Observation.code.coding` | 106048009 | Respiratory finding | http://snomed.info/sct |
| 180 | 1058 | Observation | `Observation.valueCodeableConcept.coding` | 1156330008 | Normal respiratory system | http://snomed.info/sct |
| 181 | 1059 | Observation | `Observation.valueCodeableConcept.coding` | SP000501 | Pernapasan Tidak Normal | http://terminology.kemkes.go.id/sp |
| 182 | 1060 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 183 | 1068 | Observation | `Observation.component.code.coding` | 267036007 | Dyspnea | http://snomed.info/sct |
| 184 | 1071 | Observation | `Observation.component.code.coding` | 49727002 | Cough | http://snomed.info/sct |
| 185 | 1074 | Observation | `Observation.component.code.coding` | 271823003 | Tachypnea | http://snomed.info/sct |
| 186 | 1077 | Observation | `Observation.component.code.coding` | 86684002 | Slow respiration | http://snomed.info/sct |
| 187 | 1080 | Observation | `Observation.component.code.coding` | 56018004 | Wheezing | http://snomed.info/sct |
| 188 | 1083 | Observation | `Observation.component.code.coding` | 48409008 | Respiratory crackles | http://snomed.info/sct |
| 189 | 1086 | Observation | `Observation.component.code.coding` | 74964007 | Other | http://snomed.info/sct |
| 190 | 1096 | Procedure | `Procedure.code.coding` | 87431004 | Dilation of cervical canal | http://snomed.info/sct |
| 191 | 1108 | Observation | `Observation.code.coding` | 289825001 | Diameter of cervical dilatation | http://snomed.info/sct |
| 192 | 1120 | Observation | `Observation.code.coding` | 267038008 | Edema | http://snomed.info/sct |
| 193 | 1132 | Observation | `Observation.code.coding` | 44972-8 | Edema site | http://loinc.org |
| 194 | 1133 | Observation | `Observation.valueCodeableConcept.coding` | 445088006 | Edema of face | http://snomed.info/sct |
| 195 | 1134 | Observation | `Observation.valueCodeableConcept.coding` | 102576009 | Edema of foot | http://snomed.info/sct |
| 196 | 1135 | Observation | `Observation.valueCodeableConcept.coding` | 82014009 | Peripheral edema | http://snomed.info/sct |
| 197 | 1136 | Observation | `Observation.valueCodeableConcept.coding` | 262703009 | Edema of lumbar cord | http://snomed.info/sct |
| 198 | 1137 | Observation | `Observation.valueCodeableConcept.coding` | 449615005 | Swelling of lower leg | http://snomed.info/sct |
| 199 | 1147 | Observation | `Observation.code.coding` | 423484008 | Grade of edema | http://snomed.info/sct |
| 200 | 1148 | Observation | `Observation.valueCodeableConcept.coding` | 420829009 | 1+ pitting edema | http://snomed.info/sct |
| 201 | 1149 | Observation | `Observation.valueCodeableConcept.coding` | 421605005 | 2+ pitting edema | http://snomed.info/sct |
| 202 | 1150 | Observation | `Observation.valueCodeableConcept.coding` | 421346005 | 3+ pitting edema | http://snomed.info/sct |
| 203 | 1151 | Observation | `Observation.valueCodeableConcept.coding` | 421129002 | 4+ pitting edema | http://snomed.info/sct |
| 204 | 1161 | Observation | `Observation.code.coding` | vital-signs | Abdominal circumference | http://snomed.info/sct |
| 205 | 1173 | Observation | `Observation.code.coding` | 11881-0 | Uterus Fundal height Tape measure | http://loinc.org |
| 206 | 1174 | Observation | `Observation.code.coding` | ANC.B8.DE105 | Symphysis-fundal height | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 207 | 1177 | Observation | `Observation.component.code.coding` | SP000928 | TFU dalam Jari | http://terminology.kemkes.go.id/sp |
| 208 | 1178 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000929 | Teraba ballotement | http://terminology.kemkes.go.id/sp |
| 209 | 1179 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000930 | 1 jari diatas symphisis pubis | http://terminology.kemkes.go.id/sp |
| 210 | 1180 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000931 | 2 jari diatas symphisis pubis | http://terminology.kemkes.go.id/sp |
| 211 | 1181 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000932 | Pertengan pusar dan symphisis pubis | http://terminology.kemkes.go.id/sp |
| 212 | 1182 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000933 | 1 jari dibawah pusar | http://terminology.kemkes.go.id/sp |
| 213 | 1183 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000934 | 2 jari dibawah pusar | http://terminology.kemkes.go.id/sp |
| 214 | 1184 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000935 | 3 jari dibawah pusar | http://terminology.kemkes.go.id/sp |
| 215 | 1185 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000936 | Setinggi Pusar | http://terminology.kemkes.go.id/sp |
| 216 | 1186 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000937 | 1 jari diatas pusar | http://terminology.kemkes.go.id/sp |
| 217 | 1187 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000938 | 2 jari diatas pusar | http://terminology.kemkes.go.id/sp |
| 218 | 1188 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000939 | 3 jari diatas pusar | http://terminology.kemkes.go.id/sp |
| 219 | 1189 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000940 | 1 jari dibawah px | http://terminology.kemkes.go.id/sp |
| 220 | 1190 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000941 | 2 jari dibawah px | http://terminology.kemkes.go.id/sp |
| 221 | 1191 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000942 | 3 jari dibawah px | http://terminology.kemkes.go.id/sp |
| 222 | 1201 | Observation | `Observation.code.coding` | 55283-6 | Fetal Heart rate | http://loinc.org |
| 223 | 1202 | Observation | `Observation.code.coding` | ANC.B8.DE107 | Fetal heart rate | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 224 | 1214 | Observation | `Observation.code.coding` | 246435002 | Number of fetuses | http://snomed.info/sct |
| 225 | 1215 | Observation | `Observation.code.coding` | ANC.B8.DE109 | Number of fetuses | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 226 | 1226 | Observation | `Observation.code.coding` | 72155-5 | Position in womb Fetus [RHEA] | http://loinc.org |
| 227 | 1227 | Observation | `Observation.code.coding` | ANC.B8.DE111 | Fetal presentation | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 228 | 1228 | Observation | `Observation.valueCodeableConcept.coding` | 1209182005 | Cephalic fetal presentation | http://snomed.info/sct |
| 229 | 1229 | Observation | `Observation.valueCodeableConcept.coding` | 6096002 | Breech presentation | http://snomed.info/sct |
| 230 | 1230 | Observation | `Observation.valueCodeableConcept.coding` | 73161006 | Transverse lie | http://snomed.info/sct |
| 231 | 1231 | Observation | `Observation.valueCodeableConcept.coding` | SP000006 | Organ Tubuh Lainnya | http://terminology.kemkes.go.id/sp |
| 232 | 1232 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 233 | 1241 | Procedure | `Procedure.code.coding` | 88.78 | Diagnostic ultrasound of gravid uterus | http://hl7.org/fhir/sid/icd-9-cm |
| 234 | 1253 | Procedure | `Procedure.code.coding` | 88.78 | Diagnostic ultrasound of gravid uterus | http://hl7.org/fhir/sid/icd-9-cm |
| 235 | 1274 | Observation | `Observation.code.coding` | SP000729 | Sudah menjadwalkan pemeriksaan USG terdekat | http://terminology.kemkes.go.id/sp |
| 236 | 1293 | CarePlan | `CarePlan.activity.detail.code` | 88.78 | Diagnostic ultrasound of gravid uterus | http://hl7.org/fhir/sid/icd-9-cm |
| 237 | 1304 | Observation | `Observation.code.coding` | 268445003 | Ultrasound scan - obstetric | http://snomed.info/sct |
| 238 | 1305 | Observation | `Observation.valueCodeableConcept.coding` | 169221005 | Ultrasound obstetric scan normal | http://snomed.info/sct |
| 239 | 1306 | Observation | `Observation.valueCodeableConcept.coding` | 169255008 | Ultrasound scan abnormal | http://snomed.info/sct |
| 240 | 1307 | Observation | `Observation.dataAbsentReason.coding` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 241 | 1330 | Observation | `Observation.code.coding` | 11888-5 | Gestational age US composite estimate | http://loinc.org |
| 242 | 1331 | Observation | `Observation.code.coding` | ANC.B6.DE20 | Ultrasound | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 243 | 1334 | Observation | `Observation.component.code.coding` | SP000461 | Usia Kehamilan (Hari) | http://terminology.kemkes.go.id/sp |
| 244 | 1355 | Observation | `Observation.code.coding` | 11781-2 | Delivery date US composite estimate | http://loinc.org |
| 245 | 1356 | Observation | `Observation.code.coding` | ANC.B6.DE40 | Hari Perkiraan Lahir (HPL) USG | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 246 | 1376 | Observation | `Observation.code.coding` | 3156-7 | Volume of Amniotic fluid | http://loinc.org |
| 247 | 1379 | Observation | `Observation.interpretation.coding` | 278092006 | Amniotic fluid volume within reference range | http://snomed.info/sct |
| 248 | 1380 | Observation | `Observation.interpretation.coding` | 289293006 | Amniotic fluid volume above reference range | http://snomed.info/sct |
| 249 | 1381 | Observation | `Observation.interpretation.coding` | 1228877003 | Amniotic fluid volume below reference range | http://snomed.info/sct |
| 250 | 1400 | Observation | `Observation.code.coding` | 11994-1 | Placenta position US | http://loinc.org |
| 251 | 1401 | Observation | `Observation.valueCodeableConcept.coding` | 658101000005106 | Position of placenta in fundus uteri | http://snomed.info/sct |
| 252 | 1402 | Observation | `Observation.valueCodeableConcept.coding` | 23952005 | Body of uterus structure | http://snomed.info/sct |
| 253 | 1403 | Observation | `Observation.valueCodeableConcept.coding` | 445122007 | Low-lying placenta | http://snomed.info/sct |
| 254 | 1404 | Observation | `Observation.valueCodeableConcept.coding` | 36813001 | Placenta previa | http://snomed.info/sct |
| 255 | 1424 | Observation | `Observation.code.coding` | SP000892 | Metode pemantauan kepatuhan konsumsi MMS | http://terminology.kemkes.go.id/sp |
| 256 | 1425 | Observation | `Observation.valueCodeableConcept.coding` | SP000447 | Pemantauan Konsumsi MMS Botol | http://terminology.kemkes.go.id/sp |
| 257 | 1426 | Observation | `Observation.valueCodeableConcept.coding` | SP000448 | Pemantauan Konsumsi MMS Blister | http://terminology.kemkes.go.id/sp |
| 258 | 1436 | Observation | `Observation.code.coding` | 27342004 | Anemia of pregnancy | http://snomed.info/sct |
| 259 | 1448 | Observation | `Observation.code.coding` | 182947002 | Administration of prophylactic iron during pregnancy | http://snomed.info/sct |
| 260 | 1461 | MedicationDispense | `MedicationDispense.contained.code.coding` | 93027786 | MMS Multivitamin Ibu Hamil Tablet Salut Selaput (Umum) | http://sys-ids.kemkes.go.id/kfa |
| 261 | 1493 | Observation | `Observation.code.coding` | SP000905 | Jumlah tablet MMS yang seharusnya dikonsumsi | http://terminology.kemkes.go.id/sp |
| 262 | 1504 | Observation | `Observation.code.coding` | SP000906 | Jumlah tablet MMS yang sudah dikonsumsi | http://terminology.kemkes.go.id/sp |
| 263 | 1515 | Observation | `Observation.code.coding` | SP000907 | Hasil Timbangan MMS (gram) | http://terminology.kemkes.go.id/sp |
| 264 | 1527 | Observation | `Observation.code.coding` | SP000908 | Jumlah tablet tersisa | http://terminology.kemkes.go.id/sp |
| 265 | 1538 | Observation | `Observation.code.coding` | SP000909 | Jumlah MMS telah dikonsumsi berdasarkan penimbangan | http://terminology.kemkes.go.id/sp |
| 266 | 1552 | Observation | `Observation.code.coding` | SP000911 | Total MMS yang telah dikonsumsi berdasarkan hasil penimbangan dan dikurangi MMS yang hilang | http://terminology.kemkes.go.id/sp |
| 267 | 1568 | MedicationDispense | `MedicationDispense.contained.code.coding` | 93027786 | MMS Multivitamin Ibu Hamil Tablet Salut Selaput (Umum) | http://sys-ids.kemkes.go.id/kfa |
| 268 | 1586 | Observation | `Observation.code.coding` | SP000905 | Jumlah tablet MMS yang seharusnya dikonsumsi | http://terminology.kemkes.go.id/sp |
| 269 | 1626 | Observation | `Observation.code.coding` | SP000906 | Jumlah tablet MMS yang sudah dikonsumsi | http://terminology.kemkes.go.id/sp |
| 270 | 1643 | Observation | `Observation.code.coding` | SP000906 | Jumlah tablet MMS yang sudah dikonsumsi | http://terminology.kemkes.go.id/sp |
| 271 | 1660 | Observation | `Observation.code.coding` | SP000906 | Jumlah tablet MMS yang sudah dikonsumsi | http://terminology.kemkes.go.id/sp |
| 272 | 1671 | Observation | `Observation.code.coding` | SP000912 | Jumlah tablet MMS yang seharusnya dikonsumsi pada kemasan blister terakhir | http://terminology.kemkes.go.id/sp |
| 273 | 1682 | Observation | `Observation.code.coding` | SP000913 | Jumlah tablet MMS yang sudah dikonsumsi pada kemasan blister terakhir | http://terminology.kemkes.go.id/sp |
| 274 | 1705 | Observation | `Observation.code.coding` | SP000915 | Jumlah konsumsi MMS pada kemasan blister | http://terminology.kemkes.go.id/sp |
| 275 | 1715 | Observation | `Observation.code.coding` | SP000914 | Jumlah tablet MMS yang telah dikonsumsi ibu hamil berdasarkan kartu pemantauan | http://terminology.kemkes.go.id/sp |
| 276 | 1730 | MedicationDispense | `MedicationDispense.contained.code.coding` | 93015491 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | http://sys-ids.kemkes.go.id/kfa |
| 277 | 1749 | Observation | `Observation.code.coding` | SP000900 | Jumlah TTD yang seharusnya sudah dikonsumsi | http://terminology.kemkes.go.id/sp |
| 278 | 1772 | Observation | `Observation.code.coding` | SP000901 | Jumlah TTD yang seharusnya dikonsumsi pada kemasan terakhir | http://terminology.kemkes.go.id/sp |
| 279 | 1783 | Observation | `Observation.code.coding` | SP000902 | Jumlah TTD yang telah dikonsumsi bulan ini | http://terminology.kemkes.go.id/sp |
| 280 | 1794 | Observation | `Observation.code.coding` | SP000903 | Jumlah TTD yang sudah dikonsumsi dari awal hingga hari ini | http://terminology.kemkes.go.id/sp |
| 281 | 1805 | Observation | `Observation.code.coding` | SP000904 | Ibu mengonsumsi TTD setiap hari | http://terminology.kemkes.go.id/sp |
| 282 | 1841 | Observation | `Observation.code.coding` | 182948007 | Administration of prophylactic vitamin during pregnancy | http://snomed.info/sct |
| 283 | 1872 | Condition | `Condition.code.coding` | SP000899 | Ibu sakit dalam kurun waktu 2 minggu terakhir | http://terminology.kemkes.go.id/sp |
| 284 | 1881 | Observation | `Observation.code.coding` | 715035002 | Does take medication | http://snomed.info/sct |
| 285 | 1913 | Observation | `Observation.code.coding` | 55607006 | Problem | http://snomed.info/sct |
| 286 | 1930 | ServiceRequest | `ServiceRequest.code` | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | http://loinc.org |
| 287 | 1941 | Specimen | `Specimen.type` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 288 | 1950 | Observation | `Observation.code.coding` | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | http://loinc.org |
| 289 | 1951 | Observation | `Observation.code.coding` | ANC.B9.DE159 | Blood glucose test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 290 | 1952 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 291 | 1964 | DiagnosticReport | `DiagnosticReport.code.coding` | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | http://loinc.org |
| 292 | 1977 | Observation | `Observation.code.coding` | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | http://loinc.org |
| 293 | 1978 | Observation | `Observation.code.coding` | ANC.B9.DE159 | Blood glucose test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 294 | 2002 | ServiceRequest | `ServiceRequest.code` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 295 | 2013 | Specimen | `Specimen.type` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 296 | 2022 | Observation | `Observation.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 297 | 2023 | Observation | `Observation.code.coding` | ANC.B9.DE175 | Blood hemoglobin test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 298 | 2024 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 299 | 2028 | Observation | `Observation.interpretation.coding` | 860635002 | No anemia present | http://snomed.info/sct |
| 300 | 2029 | Observation | `Observation.interpretation.coding` | OI000032 | Anemia ringan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 301 | 2030 | Observation | `Observation.interpretation.coding` | OI000033 | Anemia sedang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 302 | 2031 | Observation | `Observation.interpretation.coding` | OI000034 | Anemia berat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 303 | 2040 | DiagnosticReport | `DiagnosticReport.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 304 | 2053 | Observation | `Observation.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 305 | 2054 | Observation | `Observation.code.coding` | ANC.B9.DE175 | Blood hemoglobin test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 306 | 2058 | Observation | `Observation.interpretation.coding` | 860635002 | No anemia present | http://snomed.info/sct |
| 307 | 2059 | Observation | `Observation.interpretation.coding` | OI000032 | Anemia ringan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 308 | 2060 | Observation | `Observation.interpretation.coding` | OI000033 | Anemia sedang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 309 | 2061 | Observation | `Observation.interpretation.coding` | OI000034 | Anemia berat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 310 | 2082 | ServiceRequest | `ServiceRequest.code` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 311 | 2093 | Specimen | `Specimen.type` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 312 | 2102 | Observation | `Observation.code.coding` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 313 | 2103 | Observation | `Observation.code.coding` | ANC.B9.DE60 | Hepatitis B test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 314 | 2104 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 315 | 2106 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 316 | 2107 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 317 | 2116 | DiagnosticReport | `DiagnosticReport.code` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 318 | 2129 | Observation | `Observation.code.coding` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 319 | 2130 | Observation | `Observation.code.coding` | ANC.B9.DE60 | Hepatitis B test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 320 | 2132 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 321 | 2133 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 322 | 2154 | ServiceRequest | `ServiceRequest.code` | 11258-1 | Hepatitis B virus DNA [Units/volume] in Serum | http://loinc.org |
| 323 | 2155 | ServiceRequest | `ServiceRequest.code` | 39007-0 | Hepatitis B virus e Ag [Presence] in Specimen | http://loinc.org |
| 324 | 2166 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 325 | 2174 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 326 | 2177 | Observation | `Observation.code.coding` | 11258-1 | Hepatitis B virus DNA [Units/volume] in Serum | http://loinc.org |
| 327 | 2178 | Observation | `Observation.code.coding` | 39007-0 | Hepatitis B virus e Ag [Presence] in Specimen | http://loinc.org |
| 328 | 2181 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 329 | 2182 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 330 | 2191 | DiagnosticReport | `DiagnosticReport.code` | 11258-1 | Hepatitis B virus DNA [Units/volume] in Serum | http://loinc.org |
| 331 | 2193 | DiagnosticReport | `DiagnosticReport.code` | 39007-0 | Hepatitis B virus e Ag [Presence] in Specimen | http://loinc.org |
| 332 | 2206 | Observation | `Observation.code.coding` | 11258-1 | Hepatitis B virus DNA [Units/volume] in Serum | http://loinc.org |
| 333 | 2207 | Observation | `Observation.code.coding` | 39007-0 | Hepatitis B virus e Ag [Presence] in Specimen | http://loinc.org |
| 334 | 2211 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 335 | 2212 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 336 | 2233 | ServiceRequest | `ServiceRequest.code` | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 337 | 2244 | Specimen | `Specimen.type` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 338 | 2253 | Observation | `Observation.code.coding` | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 339 | 2254 | Observation | `Observation.code.coding` | ANC.B9.DE32 | HIV test | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 340 | 2255 | Observation | `Observation.dataAbsentReason.coding` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 341 | 2257 | Observation | `Observation.valueCodeableConcept.coding` | 165816005 | Human immunodeficiency virus detected | http://snomed.info/sct |
| 342 | 2258 | Observation | `Observation.valueCodeableConcept.coding` | 165815009 | Human immunodeficiency virus not detected | http://snomed.info/sct |
| 343 | 2267 | DiagnosticReport | `DiagnosticReport.code` | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 344 | 2280 | Observation | `Observation.code.coding` | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 345 | 2281 | Observation | `Observation.code.coding` | ANC.B9.DE32 | HIV test | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 346 | 2283 | Observation | `Observation.valueCodeableConcept.coding` | 165816005 | Human immunodeficiency virus detected | http://snomed.info/sct |
| 347 | 2284 | Observation | `Observation.valueCodeableConcept.coding` | 165815009 | Human immunodeficiency virus not detected | http://snomed.info/sct |
| 348 | 2305 | ServiceRequest | `ServiceRequest.code` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 349 | 2316 | Specimen | `Specimen.type` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 350 | 2325 | Observation | `Observation.code.coding` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 351 | 2326 | Observation | `Observation.code.coding` | ANC.B9.DE96 | Syphilis test conducted | http://snomed.info/sct |
| 352 | 2327 | Observation | `Observation.dataAbsentReason.coding` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 353 | 2329 | Observation | `Observation.valueCodeableConcept.coding` | 11214006 | Reactive | http://snomed.info/sct |
| 354 | 2330 | Observation | `Observation.valueCodeableConcept.coding` | 131194007 | Non-Reactive | http://snomed.info/sct |
| 355 | 2339 | DiagnosticReport | `DiagnosticReport.code` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 356 | 2352 | Observation | `Observation.code.coding` | 20508-8 | Reagin Ab [Units/volume] in Serum or Plasma by RPR | http://loinc.org |
| 357 | 2353 | Observation | `Observation.code.coding` | ANC.B9.DE96 | Syphilis test conducted | http://snomed.info/sct |
| 358 | 2355 | Observation | `Observation.valueCodeableConcept.coding` | 11214006 | Reactive | http://snomed.info/sct |
| 359 | 2356 | Observation | `Observation.valueCodeableConcept.coding` | 131194007 | Non-Reactive | http://snomed.info/sct |
| 360 | 2377 | ServiceRequest | `ServiceRequest.code` | 20454-5 | Protein [Presence] in Urine by Test strip | http://loinc.org |
| 361 | 2388 | Specimen | `Specimen.type` | 122575003 | Urine specimen | http://snomed.info/sct |
| 362 | 2397 | Observation | `Observation.code.coding` | 20454-5 | Protein [Presence] in Urine by Test strip | http://loinc.org |
| 363 | 2398 | Observation | `Observation.code.coding` | ANC.B9.DE114 | Urine test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 364 | 2399 | Observation | `Observation.dataAbsentReason.coding` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 365 | 2401 | Observation | `Observation.valueCodeableConcept.coding` | LA11841-6 | 1+ | http://loinc.org |
| 366 | 2402 | Observation | `Observation.valueCodeableConcept.coding` | LA11842-4 | 2+ | http://loinc.org |
| 367 | 2403 | Observation | `Observation.valueCodeableConcept.coding` | LA11843-2 | 3+ | http://loinc.org |
| 368 | 2404 | Observation | `Observation.valueCodeableConcept.coding` | LA11844-0 | 4+ | http://loinc.org |
| 369 | 2405 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 370 | 2414 | DiagnosticReport | `DiagnosticReport.code` | 20454-5 | Protein [Presence] in Urine by Test strip | http://loinc.org |
| 371 | 2427 | Observation | `Observation.code.coding` | 20454-5 | Protein [Presence] in Urine by Test strip | http://loinc.org |
| 372 | 2428 | Observation | `Observation.code.coding` | ANC.B9.DE114 | Urine test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 373 | 2430 | Observation | `Observation.valueCodeableConcept.coding` | LA11841-6 | 1+ | http://loinc.org |
| 374 | 2431 | Observation | `Observation.valueCodeableConcept.coding` | LA11842-4 | 2+ | http://loinc.org |
| 375 | 2432 | Observation | `Observation.valueCodeableConcept.coding` | LA11843-2 | 3+ | http://loinc.org |
| 376 | 2433 | Observation | `Observation.valueCodeableConcept.coding` | LA11844-0 | 4+ | http://loinc.org |
| 377 | 2434 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 378 | 2455 | ServiceRequest | `ServiceRequest.code` | 25428-4 | Glucose [Presence] in Urine by Test strip | http://loinc.org |
| 379 | 2466 | Specimen | `Specimen.type` | 122575003 | Urine specimen | http://snomed.info/sct |
| 380 | 2475 | Observation | `Observation.code.coding` | 25428-4 | Glucose [Presence] in Urine by Test strip | http://loinc.org |
| 381 | 2476 | Observation | `Observation.code.coding` | ANC.B9.DE114 | Urine test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 382 | 2477 | Observation | `Observation.dataAbsentReason.coding` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 383 | 2479 | Observation | `Observation.valueCodeableConcept.coding` | LA11841-6 | 1+ | http://loinc.org |
| 384 | 2480 | Observation | `Observation.valueCodeableConcept.coding` | LA11842-4 | 2+ | http://loinc.org |
| 385 | 2481 | Observation | `Observation.valueCodeableConcept.coding` | LA11843-2 | 3+ | http://loinc.org |
| 386 | 2482 | Observation | `Observation.valueCodeableConcept.coding` | LA11844-0 | 4+ | http://loinc.org |
| 387 | 2483 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 388 | 2492 | DiagnosticReport | `DiagnosticReport.code` | 25428-4 | Glucose [Presence] in Urine by Test strip | http://loinc.org |
| 389 | 2506 | ServiceRequest | `ServiceRequest.code` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://snomed.info/sct |
| 390 | 2517 | Specimen | `Specimen.type` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 391 | 2526 | Observation | `Observation.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://snomed.info/sct |
| 392 | 2527 | Observation | `Observation.dataAbsentReason.coding` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 393 | 2529 | Observation | `Observation.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 394 | 2530 | Observation | `Observation.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 395 | 2531 | Observation | `Observation.dataAbsentReason.coding` | 419984006 | Inconclusive | http://snomed.info/sct |
| 396 | 2540 | DiagnosticReport | `DiagnosticReport.code` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 397 | 2552 | Condition | `Condition.code.coding` | 169943008 | Mother less than 20 years old | http://snomed.info/sct |
| 398 | 2553 | Condition | `Condition.code.coding` | SP000780 | Umur ≥ 35 Tahun | http://terminology.kemkes.go.id/sp |
| 399 | 2554 | Condition | `Condition.code.coding` | SP000893 | Tinggi ≤ 145 cm | http://terminology.kemkes.go.id/sp |
| 400 | 2555 | Condition | `Condition.code.coding` | SP000894 | Jarak kehamilan <2 tahun | http://terminology.kemkes.go.id/sp |
| 401 | 2556 | Condition | `Condition.code.coding` | 18656007 | Grand multipara | http://snomed.info/sct |
| 402 | 2557 | Condition | `Condition.code.coding` | 237145004 | Unexplained infertility | http://snomed.info/sct |
| 403 | 2558 | Condition | `Condition.code.coding` | 27624003 | Chronic disease | http://snomed.info/sct |
| 404 | 2559 | Condition | `Condition.code.coding` | 85828009 | Autoimmune disease | http://snomed.info/sct |
| 405 | 2560 | Condition | `Condition.code.coding` | 27342004 | Anemia of pregnancy | http://snomed.info/sct |
| 406 | 2561 | Condition | `Condition.code.coding` | 40733004 | Infectious disease | http://snomed.info/sct |
| 407 | 2570 | MedicationRequest | `MedicationRequest.contained.code.coding` | 93015491 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | http://sys-ids.kemkes.go.id/kfa |
| 408 | 2599 | MedicationDispense | `MedicationDispense.contained.code.coding` | 93015491 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | http://sys-ids.kemkes.go.id/kfa |
| 409 | 2626 | MedicationRequest | `MedicationRequest.contained.code.coding` | SP000370 | Multiple Micronutrient Supplement | http://terminology.kemkes.go.id/sp |
| 410 | 2649 | MedicationDispense | `MedicationDispense.contained.code.coding` | SP000370 | Multiple Micronutrient Supplement | http://terminology.kemkes.go.id/sp |
| 411 | 2668 | Observation | `Observation.code.coding` | SP000007 | Tatalaksana Anemia | http://terminology.kemkes.go.id/sp |
| 412 | 2669 | Observation | `Observation.valueCodeableConcept.coding` | SP000008 | Pemberian Tablet Tambah Darah | http://terminology.kemkes.go.id/sp |
| 413 | 2670 | Observation | `Observation.valueCodeableConcept.coding` | SP000009 | Pemberian Fe Parenteral | http://terminology.kemkes.go.id/sp |
| 414 | 2671 | Observation | `Observation.valueCodeableConcept.coding` | 116859006 | Transfusion of blood product | http://snomed.info/sct |
| 415 | 2672 | Observation | `Observation.valueCodeableConcept.coding` | 3457005 | Patient referral | http://snomed.info/sct |
| 416 | 2674 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 417 | 2685 | Observation | `Observation.code.coding` | SP000012 | Tatalaksana Pre Eklampsia | http://terminology.kemkes.go.id/sp |
| 418 | 2686 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 419 | 2688 | Observation | `Observation.component.code.coding` | 135840009 | Blood pressure monitoring | http://snomed.info/sct |
| 420 | 2691 | Observation | `Observation.component.code.coding` | 308116003 | Antihypertensive therapy | http://snomed.info/sct |
| 421 | 2694 | Observation | `Observation.component.code.coding` | SP000013 | Pemberian MgSO4 | http://terminology.kemkes.go.id/sp |
| 422 | 2697 | Observation | `Observation.component.code.coding` | SP000848 | Pemberian Aspirin low dose rutin dan 1,5 gr terapi kalsium | http://terminology.kemkes.go.id/sp |
| 423 | 2700 | Observation | `Observation.component.code.coding` | 74964007 | Other | http://snomed.info/sct |
| 424 | 2713 | Observation | `Observation.code.coding` | SP000014 | Tatalaksana KEK | http://terminology.kemkes.go.id/sp |
| 425 | 2716 | Observation | `Observation.component.code.coding` | 435591000124104 | Nutrition supplement therapy | http://snomed.info/sct |
| 426 | 2719 | Observation | `Observation.component.code.coding` | 3457005 | Patient referral | http://snomed.info/sct |
| 427 | 2732 | Observation | `Observation.code.coding` | SP000016 | Tatalaksana Masalah Kesehatan | http://terminology.kemkes.go.id/sp |
| 428 | 2744 | Procedure | `Procedure.code.coding` | 1230101008 | Counseling for pregnancy | http://snomed.info/sct |
| 429 | 2748 | Procedure | `Procedure.code.coding` | ED000008 | Edukasi Tanda Bahaya Kehamilan, Bersalin dan Nifas | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 430 | 2749 | Procedure | `Procedure.code.coding` | ED000009 | Edukasi IMD dan ASI Eksklusif | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 431 | 2750 | Procedure | `Procedure.code.coding` | ED000010 | Edukasi PHBS | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 432 | 2751 | Procedure | `Procedure.code.coding` | ED000011 | Edukasi KB pasca salin | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 433 | 2752 | Procedure | `Procedure.code.coding` | SP000664 | Edukasi konsumsi TTD | http://terminology.kemkes.go.id/sp |
| 434 | 2753 | Procedure | `Procedure.code.coding` | SP000665 | Edukasi pencegahan preeklampsia | http://terminology.kemkes.go.id/sp |
| 435 | 2754 | Procedure | `Procedure.code.coding` | SP000503 | Konseling positif hepatitis B | http://terminology.kemkes.go.id/sp |
| 436 | 2755 | Procedure | `Procedure.code.coding` | 1287707002 | Consultation for hypertension | http://snomed.info/sct |
| 437 | 2756 | Procedure | `Procedure.code.coding` | SP000504 | Konseling risiko HIV | http://terminology.kemkes.go.id/sp |
| 438 | 2757 | Procedure | `Procedure.code.coding` | 313077009 | Human immunodeficiency virus counseling | http://snomed.info/sct |
| 439 | 2758 | Procedure | `Procedure.code.coding` | SP000505 | Konseling dan perawatan sifilis | http://terminology.kemkes.go.id/sp |
| 440 | 2759 | Procedure | `Procedure.code.coding` | ED000012 | Edukasi Lainnya | http://terminology.kemkes.go.id/CodeSystem/clinical-term |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 194 |
| http://terminology.kemkes.go.id/sp | 93 |
| http://loinc.org | 80 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 26 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 16 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 14 |
| http://sys-ids.kemkes.go.id/kfa | 10 |
| http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes | 3 |
| http://hl7.org/fhir/sid/icd-9-cm | 3 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 1 |
| **Total** | **440** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 2 | – | Tanggal kunjungan | – | `` |
| 14 | – | Tanggal Posyandu | – | `` |
| 38 | – | Tanggal Posyandu | – | `` |
| 225 | – | Tanggal Posyandu | – | `` |
| 1251 | – | Apakah sudah dilakukan pemeriksaan USG pada kunjungan K saat ini? | – | `` |
| 1924 | – | Apakah dilakukan skrining kesehatan jiwa pada ibu hamil? | – | `` |
| 1974 | – | Apakah sudah dilakukan pemeriksaan glukosa darah sewaktu pada kunjukan K saat ini? | – | `` |
| 2126 | – | Apakah sudah dilakukan pemeriksaan hepatitis B (HBsAG) pada kunjukan K saat ini? | – | `` |
| 2203 | – | Apakah sudah dilakukan pemeriksaan lanjutan Hepatitis B pada kunjukan K saat ini? | – | `` |
| 2277 | – | Apakah sudah dilakukan pemeriksaan HIV pada kunjukan K saat ini? | – | `` |
| 2349 | – | Apakah sudah dilakukan pemeriksaan sifilis pada kunjukan K saat ini? | – | `` |
| 2424 | – | Apakah sudah dilakukan pemeriksaan dipstick protein urin pada kunjukan K saat ini? | – | `` |
