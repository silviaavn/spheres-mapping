# Output Form: ePuskesmas KIA Harian ANC

Sumber: `mapping/phdt-data-dictionary-epus-anc.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-epus-anc.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 155 |
| Code (`jumlah code` = 1) | 321 |
| Code unik (code + CodeSystem) | 219 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 24 |
| Variabel BQ (unik) | 0 |
| Variabel raw (variabel dictionary; belum ada file mentah) | 123 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–27 | Patient | – | – | _Nama_Pasien_ → `Patient.name.text` (2, tanpa BQ)<br>_NIK_ → `Patient.identifier.value` (5, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (7, tanpa BQ)<br>_No HP_ → `Patient.telecom` (8, tanpa BQ)<br>_Tanggal_Lahir_ → `Patient.birthDate` (11, tanpa BQ)<br>_Alamat Domisili_ → `Patient.address.use` (12, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (18, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (21, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.extension.valueCode` (24, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.extension.valueCode` (27, tanpa BQ) |
| 2 | 74–80 | PractitionerRole | – | – | _Role Tenaga Pemeriksa_ → `PractitionerRole.active` (74, tanpa BQ) |
| 3 | 81–101 | Practitioner | – | – | _Nama Tenaga Pemeriksa_ → `Practitioner.name.text` (83, tanpa BQ)<br>_Jenis Kelamin Tenaga Pemeriksa_ → `Practitioner.gender` (84, tanpa BQ)<br>_Nama Provinsi_ → `Practitioner.address.extension.extension.valueCode` (91, tanpa BQ)<br>_Nama Kabupaten_ → `Practitioner.address.extension.extension.valueCode` (94, tanpa BQ)<br>_Nama Kecamatan_ → `Practitioner.address.extension.extension.valueCode` (97, tanpa BQ)<br>_Nama Desa_ → `Practitioner.address.extension.extension.valueCode` (100, tanpa BQ) |
| 4 | 102–105 | EpisodeOfCare | – | – | – |
| 5 | 106–129 | Encounter | – | – | _Kunjungan_K_ → `Encounter.identifier` (107, tanpa BQ)<br>_Tanggal_Antenatal_ → `Encounter.period.start` (122, tanpa BQ)<br>_Faskes_Perujuk_ → `Encounter.hospitaliz ation.admitSource.text` (129, tanpa BQ)<br>_Cara_Masuk_ → `Encounter.hospitalization.admitSource.coding` (149, tanpa BQ)<br>_Faskes_Perujuk_ → `Encounter.hospitalization.admitSource.text` (163, tanpa BQ) |
| 6 | 130–136 | Condition | 134435003 | Routine antenatal care | _Diagnosis_ → `Condition.clinicalStatus.coding` (130, tanpa BQ) |
| 7 | 164–174 | Observation | 11996-6 | [#] Pregnancies | _Gravida_ → `Observation.valueInteger` (167, tanpa BQ) |
| 8 | 175–185 | Observation | 11977-6 | [#] Parity | _Partus_ → `Observation.valueInteger` (178, tanpa BQ) |
| 9 | 186–196 | Observation | 69043-8 | Other pregnancy outcomes # | _Abortus_ → `Observation.valueInteger` (189, tanpa BQ) |
| 10 | 197–208 | Observation | 11977-6 | [#] Parity | _Jumlah_Bayi_Hidup_ → `Observation.valueInteger` (201, tanpa BQ) |
| 11 | 209–220 | Observation | 8665-2 | Last menstrual period start date | _Tanggal_HPHT_ → `Observation.valueDateTime` (213, tanpa BQ) |
| 12 | 221–232 | Observation | 11778-8 | Delivery date Estimated | _Tanggal_Taksiran_Persalinan_ → `Observation.valueDateTime` (225, tanpa BQ) |
| 13 | 233–245 | Observation | SP000050 | Riwayat Onset Persalinan | _Tanggal_Persalinan_Sebelumnya_ → `Observation.identifier` (233, tanpa BQ) |
| 14 | 246–257 | Observation | SP000132 | Memiliki Buku KIA | _Memiliki_Buku_KIA_ → `Observation.valueBoolean` (249, tanpa BQ) |
| 15 | 258–270 | Observation | 56077-1 | Body weight --pre current pregnancy | _BB_Sebelum_Hamil_ → `Observation.valueQuantity.value` (262, tanpa BQ) |
| 16 | 271–283 | Observation | 18185-9 | Gestational age | _Usia_Kehamilan_ → `Observation.valueQuantity.value` (275, tanpa BQ) |
| 17 | 284–295 | Observation | 32418-6 | Obstetric trimester Stated | _Trimester_ke_ → `Observation.valueInteger` (288, tanpa BQ) |
| 18 | 296–304 | Condition | 404684003 | Clinical finding | _Keluhan_Ibu_Saat_Ini_ → `Condition.clinicalStatus.coding` (296, tanpa BQ) |
| 19 | 305–315 | Observation | 3401000175105 | Total number of prenatal care visits | _Kedatangan_ke_ → `Observation.valueInteger` (308, tanpa BQ) |
| 20 | 316–336 | Observation | SP000134 | Jenis Lokasi Screening | _Lokasi Screening_ → `Observation.valueCodeableConcept.coding` (319, tanpa BQ) |
| 21 | 337–348 | Observation | SP000131 | Status Pindahan | _Status Pindahan_ → `Observation.valueBoolean` (340, tanpa BQ) |
| 22 | 350–362 | Observation | 29463-7 | Body weight | _Berat Badan Saat Ini_ → `Observation.valueQuantity.value` (354, tanpa BQ) |
| 23 | 363–375 | Observation | 8302-2 | Body height | _Tinggi Badan_ → `Observation.valueQuantity.value` (367, tanpa BQ) |
| 24 | 376–389 | Observation | 284473002 | Mid upper arm circumference | _LILA (LIngkar Lengan Atas_ → `Observation.status` (376, tanpa BQ)<br>_Status Gizi KEK/Tidak KEK_ → `Observation.interpretation` (387, tanpa BQ) |
| 25 | 390–404 | Observation | 10197-2 | Physical findings of Eye Narrative | _Data_Pemeriksaan_Fisik_Konjungtiva_ → `Observation.valueString` (397, tanpa BQ) |
| 26 | 405–419 | Observation | 10197-2 | Physical findings of Eye Narrative | _Data_Pemeriksaan_Fisik_Sklera_ → `Observation.valueString` (412, tanpa BQ) |
| 27 | 420–432 | Observation | 10206-1 | Physical findings of Skin Narrative | _Data_Pemeriksaan_Fisik_Kulit_ → `Observation.valueString` (423, tanpa BQ) |
| 28 | 433–446 | Observation | 11411-6 | Physical findings of Neck Narrative | _Data_Pemeriksaan_Fisik_Leher_ → `Observation.valueString` (439, tanpa BQ) |
| 29 | 447–460 | Observation | 32453-3 | Physical findings of Mouth | _Data_Pemeriksaan_Fisik_Gigi_Mulut_ → `Observation.valueString` (451, tanpa BQ) |
| 30 | 461–474 | Observation | 297268004 | Ear, nose and throat finding | _Data_Pemeriksaan_Fisik_THT_ → `Observation.valueString` (467, tanpa BQ) |
| 31 | 475–488 | Observation | 10200-4 | Physical findings of Heart Narrative | _Data_Pemeriksaan_Fisik_Jantung_ → `Observation.valueString` (481, tanpa BQ) |
| 32 | 489–502 | Observation | 301230006 | Lung finding | _Data_Pemeriksaan_Fisik_Paru_ → `Observation.valueString` (495, tanpa BQ) |
| 33 | 503–516 | Observation | 10191-5 | Physical findings of Abdomen Narrative | _Data_Pemeriksaan_Fisik_Perut_ → `Observation.valueString` (507, tanpa BQ) |
| 34 | 517–530 | Observation | 116307009 | Finding of upper limb | _Data_Pemeriksaan_Fisik_Tungkai_Atas_ → `Observation.valueString` (523, tanpa BQ) |
| 35 | 531–544 | Observation | 116312005 | Finding of lower limb | _Data_Pemeriksaan_Fisik_Tungkai_Bawah_ → `Observation.valueString` (537, tanpa BQ) |
| 36 | 545–558 | Observation | 102572006 | Edema of lower extremity (finding) | _Data_Pemeriksaan_Fisik_Kaki_Bengkak_ → `Observation.valueString` (551, tanpa BQ) |
| 37 | 559–572 | Observation | 299412000 | Finding of patella structure | _Data_Pemeriksaan_Fisik_Patella_ → `Observation.valueString` (565, tanpa BQ) |
| 38 | 573–585 | Observation | 8480-6 | Systolic blood pressure | _Sistole_ → `Observation.valueQuantity.value` (577, tanpa BQ) |
| 39 | 586–598 | Observation | 8462-4 | Diastolic blood pressure | _Diastole_ → `Observation.valueQuantity.value` (590, tanpa BQ) |
| 40 | 599–611 | Observation | 8867-4 | Heart rate | _Frekuensi_Nadi_ → `Observation.valueQuantity.value` (602, tanpa BQ) |
| 41 | 612–623 | Observation | 8310-5 | Body temperature | _Suhu_ → `Observation.valueQuantity.value` (615, tanpa BQ) |
| 42 | 624–637 | Observation | 9279-1 | Respiratory rate | _Respiratory_ → `Observation.valueQuantity.value` (628, tanpa BQ) |
| 43 | 638–650 | Observation | 8478-0 | Mean blood pressure | _MAP_ → `Observation.valueQuantity.value` (641, tanpa BQ) |
| 44 | 651–662 | Observation | SP000634 | Tinggi fundus terdeteksi | _Tinggi_Fundus_Uteri_Terdeteksi_ → `Observation.valueBoolean` (654, tanpa BQ) |
| 45 | 663–674 | Observation | 11881-0 | Uterus Fundal height Tape measure | _Tinggi_Fundus_ → `Observation.valueQuantity.value` (666, tanpa BQ)<br>_Satuan_Tinggi_Fundus_ → `Observation.valueQuantity.code` (667, tanpa BQ) |
| 46 | 675–686 | Observation | SP000635 | Tinggi fundus jari | _Tinggi_Fundus_Jari_ → `Observation.valueQuantity.value` (678, tanpa BQ)<br>_Satuan_Tinggi_Fundus_ → `Observation.valueQuantity.code` (679, tanpa BQ) |
| 47 | 687–698 | Procedure | 88.78 | Diagnostic ultrasound of gravid uterus | _USG_ → `Procedure.category.coding` (687, tanpa BQ)<br>_USG_Keterangan_Tambahan_ → `Procedure.note` (698, tanpa BQ) |
| 48 | 699–708 | ServiceRequest | – | – | _USG_GS_ → `ServiceRequest.category` (699, tanpa BQ) |
| 49 | 709–711 | PractitionerRole | – | – | – |
| 50 | 712–725 | Observation | – | – | – |
| 51 | 726–736 | DiagnosticReport | 11850-5 | Gestational sac Mean diameter US | – |
| 52 | 737–746 | ServiceRequest | – | – | _USG_CRL_ → `ServiceRequest.category` (737, tanpa BQ) |
| 53 | 747–749 | PractitionerRole | – | – | – |
| 54 | 750–763 | Observation | – | – | – |
| 55 | 764–774 | DiagnosticReport | 11957-8 | Fetal Crown Rump length US | – |
| 56 | 775–784 | ServiceRequest | – | – | _USG_DJJ_ → `ServiceRequest.category` (775, tanpa BQ) |
| 57 | 785–787 | PractitionerRole | – | – | – |
| 58 | 788–801 | Observation | – | – | – |
| 59 | 802–812 | DiagnosticReport | 11948-7 | Fetal Heart rate US | – |
| 60 | 813–822 | ServiceRequest | – | – | _USG_BPD_ → `ServiceRequest.category` (813, tanpa BQ) |
| 61 | 823–825 | PractitionerRole | – | – | – |
| 62 | 826–838 | Observation | – | – | – |
| 63 | 839–849 | DiagnosticReport | 11820-8 | Fetal Head Diameter.biparietal US | – |
| 64 | 850–859 | ServiceRequest | – | – | _USG_HC_ → `ServiceRequest.category` (850, tanpa BQ) |
| 65 | 860–862 | PractitionerRole | – | – | – |
| 66 | 863–875 | Observation | – | – | – |
| 67 | 876–886 | DiagnosticReport | 11984-2 | Fetal Head Circumference US | – |
| 68 | 887–896 | ServiceRequest | – | – | _USG_AC_ → `ServiceRequest.category` (887, tanpa BQ) |
| 69 | 897–899 | PractitionerRole | – | – | – |
| 70 | 900–912 | Observation | – | – | – |
| 71 | 913–923 | DiagnosticReport | 11979-2 | Fetal Abdomen Circumference US | – |
| 72 | 924–933 | ServiceRequest | – | – | _USG_FL_ → `ServiceRequest.category` (924, tanpa BQ) |
| 73 | 934–936 | PractitionerRole | – | – | – |
| 74 | 937–949 | Observation | – | – | – |
| 75 | 950–960 | DiagnosticReport | 11963-6 | Fetal Femur diaphysis [Length] US | – |
| 76 | 961–970 | ServiceRequest | – | – | _USG_SDP_Ketuban_ → `ServiceRequest.category` (961, tanpa BQ) |
| 77 | 971–973 | PractitionerRole | – | – | – |
| 78 | 974–986 | Observation | – | – | – |
| 79 | 987–997 | DiagnosticReport | 11832-3 | Fetal Amniotic fluid space Maximum diameter largest pocket US | – |
| 80 | 998–1011 | Observation | 365662002 | Finding of amniotic fluid appearance | _USG_SDP_Ketuban_ → `Observation.valueCodeableConcept.coding` (1000, tanpa BQ) |
| 81 | 1012–1021 | ServiceRequest | – | – | _USG_Letak_Janin_ → `ServiceRequest.category` (1012, tanpa BQ) |
| 82 | 1022–1024 | PractitionerRole | – | – | – |
| 83 | 1025–1037 | Observation | – | – | – |
| 84 | 1038–1048 | DiagnosticReport | 72155-5 | Position in womb Fetus [RHEA] | – |
| 85 | 1049–1058 | ServiceRequest | – | – | _USG_Presentasi_ → `ServiceRequest.category` (1049, tanpa BQ) |
| 86 | 1059–1061 | PractitionerRole | – | – | – |
| 87 | 1062–1076 | Observation | – | – | – |
| 88 | 1077–1087 | DiagnosticReport | 11877-8 | Fetal presentation US | – |
| 89 | 1088–1097 | ServiceRequest | – | – | _Jumlah_Janin_ → `ServiceRequest.category` (1088, tanpa BQ) |
| 90 | 1098–1100 | PractitionerRole | – | – | – |
| 91 | 1101–1112 | Observation | – | – | – |
| 92 | 1113–1123 | DiagnosticReport | 11878-6 | Number of fetuses by US | – |
| 93 | 1124–1142 | Observation | 55283-6 | Fetal Heart rate | _Denyut_Jantung_Janin_ → `Observation.valueQuantity.value` (1128, tanpa BQ)<br>_Kondisi_Detak_Jantung_Janin_ → `Observation.interpretation.coding` (1137, tanpa BQ)<br>_Posisi_Bagian_Terbawah_Janin_terhadap_Pintu_Atas_Panggul_ → `Observation.identifier.value` (1142, tanpa BQ) |
| 94 | 1143–1155 | Observation | 249111004 | Engagement of head | _Presentasi_ → `Observation.status` (1155, tanpa BQ) |
| 95 | 1156–1170 | Observation | 72155-5 | Position in womb Fetus [RHEA] | _TBJ_ → `Observation.status` (1170, tanpa BQ) |
| 96 | 1171–1182 | Observation | 89087-1 | Fetal Body weight Estimated | – |
| 97 | 1183–1192 | ServiceRequest | – | – | _USG_Usia_Kehamilan_ → `ServiceRequest.category` (1183, tanpa BQ) |
| 98 | 1193–1195 | PractitionerRole | – | – | – |
| 99 | 1196–1209 | Observation | – | – | – |
| 100 | 1210–1220 | DiagnosticReport | 11888-5 | Gestational age US composite estimate | – |
| 101 | 1221–1230 | ServiceRequest | – | – | _USG_Perkiraan_Lahir_ → `ServiceRequest.status` (1222, tanpa BQ) |
| 102 | 1231–1233 | PractitionerRole | – | – | – |
| 103 | 1234–1245 | Observation | – | – | – |
| 104 | 1246–1256 | DiagnosticReport | 11781-2 | Delivery date US composite estimate | – |
| 105 | 1258–1276 | Immunization | – | – | _Dilakukan Imunisasi TT (Pada Kunjungan Ini)_ → `Immunization.status` (1258, tanpa BQ)<br>_Riwayat Imunisasi TT_ → `Immunization.status` (1275, tanpa BQ) |
| 106 | 1277–1293 | Immunization | – | – | – |
| 107 | 1294–1304 | Immunization | – | – | – |
| 108 | 1305–1315 | Observation | SP000001 | Skrining Imunisasi Tetanus Toksoid | – |
| 109 | 1316–1326 | Observation | SP000002 | Kunjungan Pertama Pemeriksaan Kehamilan | _Pemeriksaan Pertama_ → `Observation.valueBoolean` (1319, tanpa BQ) |
| 110 | 1327–1341 | Observation | 883-9 | ABO group [Type] in Blood | _Golongan Darah_ → `Observation.valueCodeableConcept.coding` (1331, tanpa BQ) |
| 111 | 1342–1354 | Observation | 10331-7 | Rh [Type] in Blood | _Rhesus_ → `Observation.valueCodeableConcept.coding` (1346, tanpa BQ) |
| 112 | 1355–1368 | Condition | 34842007 | Antepartum hemorrhage | _Komplikasi Kehamilan_ → `Condition.clinicalStatus.coding` (1355, tanpa BQ) |
| 113 | 1369–1382 | Observation | 268445003 | Ultrasound scan - obstetric | _Diperiksa USG_ → `Observation.valueCodeableConcept.coding` (1372, tanpa BQ)<br>_Jika diperiksa, hasil tidak normal. Tidak normal karena apa?_ → `Observation.dataAbsentReason.text` (1375, tanpa BQ) |
| 114 | 1383–1416 | MedicationRequest | 92000653 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula | _Jumlah TTD Diterima_ → `MedicationRequest.contained.resourceType` (1383, tanpa BQ) |
| 115 | 1417–1448 | MedicationDispense | 93015491 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | – |
| 116 | 1449–1458 | ServiceRequest | – | – | _Lab : HIV_ → `ServiceRequest.category` (1449, tanpa BQ) |
| 117 | 1463–1470 | Specimen | – | – | – |
| 118 | 1471–1484 | Observation | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | – |
| 119 | 1485–1496 | DiagnosticReport | – | – | – |
| 120 | 1497–1506 | ServiceRequest | – | – | _Lab : Hepatitis_ → `ServiceRequest.category` (1497, tanpa BQ) |
| 121 | 1511–1518 | Specimen | – | – | – |
| 122 | 1519–1532 | Observation | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | – |
| 123 | 1533–1544 | DiagnosticReport | – | – | – |
| 124 | 1545–1554 | ServiceRequest | – | – | _Lab : Siphilis_ → `ServiceRequest.category` (1545, tanpa BQ) |
| 125 | 1559–1566 | Specimen | – | – | – |
| 126 | 1567–1580 | Observation | 22464-2 | Reagin Ab [Presence] in Specimen | – |
| 127 | 1581–1592 | DiagnosticReport | – | – | – |
| 128 | 1593–1602 | ServiceRequest | – | – | _Lab : Protein Urine_ → `ServiceRequest.category` (1593, tanpa BQ) |
| 129 | 1607–1614 | Specimen | – | – | – |
| 130 | 1615–1628 | Observation | 2887-8 | Protein [Presence] in Urine | – |
| 131 | 1629–1640 | DiagnosticReport | 2887-8 | Protein [Presence] in Urine | – |
| 132 | 1641–1650 | ServiceRequest | – | – | _Lab : Hb_ → `ServiceRequest.category` (1641, tanpa BQ) |
| 133 | 1655–1662 | Specimen | – | – | – |
| 134 | 1663–1680 | Observation | 718-7 | Hemoglobin [Mass/volume] in Blood | – |
| 135 | 1681–1692 | DiagnosticReport | 718-7 | Hemoglobin [Mass/volume] in Blood | – |
| 136 | 1693–1702 | ServiceRequest | – | – | _Lab : Gula Sewaktu_ → `ServiceRequest.category` (1693, tanpa BQ) |
| 137 | 1707–1714 | Specimen | – | – | – |
| 138 | 1715–1730 | Observation | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | – |
| 139 | 1731–1742 | DiagnosticReport | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | – |
| 140 | 1743–1757 | Observation | 15220000 | Laboratory test | _Lab : Lainnya_ → `Observation.valueCodeableConcept.coding` (1746, tanpa BQ) |
| 141 | 1758–1766 | Observation | SP000007 | Tatalaksana Anemia | _Tatalaksana Anemia_ → `Observation.valueCodeableConcept.coding` (1761, tanpa BQ) |
| 142 | 1768–1789 | Observation | SP000010 | Skrining Hipertensi dalam Kehamilan | _Pre Eklampsia_ → `Observation.valueCodeableConcept.coding` (1778, tanpa BQ) |
| 143 | 1790–1808 | Observation | SP000012 | Tatalaksana Pre Eklampsia | _Tatalaksana Pre Eklampsia_ → `Observation.valueBoolean` (1793, tanpa BQ) |
| 144 | 1810–1828 | Observation | SP000014 | Tatalaksana KEK | _Tatalaksana KEK_ → `Observation.valueBoolean` (1821, tanpa BQ) |
| 145 | 1830–1865 | Observation | SP000015 | Risiko Masalah Kesehatan | _Risiko Masalah Kesehatan Lainnya_ → `Observation.valueBoolean` (1840, tanpa BQ) |
| 146 | 1866–1877 | Observation | SP000016 | Tatalaksana Masalah Kesehatan | _Diberikan Tatalaksana Risiko Masalah Kesehatan Lainnya_ → `Observation.valueBoolean` (1869, tanpa BQ) |
| 147 | 1878–1888 | Procedure | 1230101008 | Counseling for pregnancy | _Konseling_ → `Procedure.category.coding` (1878, tanpa BQ) |
| 148 | 1889–1900 | Procedure | 385892002 | Mental health screening | _Skrinning Keswa_ → `Procedure.category.coding` (1889, tanpa BQ) |
| 149 | 1901–1913 | Observation | OC000001 | Jarak kehamilan | _Jarak kehamilan saat ini dengan kehamilan sebelumnya_ → `Observation.valueQuantity.value` (1905, tanpa BQ) |
| 150 | 1914–1925 | Observation | 73211009 | Diabetes mellitus | _Diabetes_ → `Observation.valueBoolean` (1917, tanpa BQ) |
| 151 | 1926–1937 | Observation | 278977008 | Human immunodeficiency virus status | _HIV_ → `Observation.valueCodeableConcept.coding` (1929, tanpa BQ) |
| 152 | 1938–1949 | Observation | 66071002 | Viral hepatitis type B | _Hepatitis B_ → `Observation.valueBoolean` (1941, tanpa BQ) |
| 153 | 1950–1961 | Observation | 76272004 | Syphilis | _Sifilis_ → `Observation.valueBoolean` (1953, tanpa BQ) |
| 154 | 1962–1973 | Observation | 61462000 | Malaria | _Malaria_ → `Observation.valueBoolean` (1965, tanpa BQ) |
| 155 | 1974–1985 | Observation | 56717001 | Tuberculosis | _Tuberkulosis_ → `Observation.valueBoolean` (1977, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 82 |
| ServiceRequest | 19 |
| DiagnosticReport | 19 |
| PractitionerRole | 14 |
| Specimen | 6 |
| Condition | 3 |
| Procedure | 3 |
| Immunization | 3 |
| Patient | 1 |
| Practitioner | 1 |
| EpisodeOfCare | 1 |
| Encounter | 1 |
| MedicationRequest | 1 |
| MedicationDispense | 1 |
| **Total** | **155** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 76 | PractitionerRole | `PractitionerRole.code.coding` | 309453006 | Registered midwife | http://snomed.info/sct |
| 2 | 77 | PractitionerRole | `PractitionerRole.code.coding` | 309343006 | Physician | http://snomed.info/sct |
| 3 | 78 | PractitionerRole | `PractitionerRole.code.coding` | 309367003 | Obstetrician and gynecologist | http://snomed.info/sct |
| 4 | 79 | PractitionerRole | `PractitionerRole.code.coding` | 224535009 | Registered nurse | http://snomed.info/sct |
| 5 | 107 | Encounter | `Encounter.identifier` | K1M | Tidak ada | http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC |
| 6 | 108 | Encounter | `Encounter.identifier` | K1A | Tidak ada | http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC |
| 7 | 109 | Encounter | `Encounter.identifier` | K2 | Tidak ada | http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC |
| 8 | 110 | Encounter | `Encounter.identifier` | K3 | Tidak ada | http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC |
| 9 | 111 | Encounter | `Encounter.identifier` | K4 | Tidak ada | http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC |
| 10 | 112 | Encounter | `Encounter.identifier` | K5 | Tidak ada | http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC |
| 11 | 113 | Encounter | `Encounter.identifier` | K6 | Tidak ada | http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC |
| 12 | 128 | Encounter | `Encounter.hospitaliz ation.admitSource.co ding` | hosp-trans | Transferred from other hospital | http://terminology.hl7.org/CodeSystem/admit-source |
| 13 | 132 | Condition | `Condition.code.coding` | 134435003 | Routine antenatal care | http://snomed.info/sct |
| 14 | 149 | Encounter | `Encounter.hospitalization.admitSource.coding` | EHA000002 | Datang sendiri | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 15 | 150 | Encounter | `Encounter.hospitalization.admitSource.coding` | 305956004 | Referral by physician | http://snomed.info/sct |
| 16 | 151 | Encounter | `Encounter.hospitalization.admitSource.coding` | 306052007 | Referral by midwife | http://snomed.info/sct |
| 17 | 152 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000116 | Rujukan dari Puskesmas Pembantu | http://terminology.kemkes.go.id/sp |
| 18 | 153 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000117 | Rujukan dari Puskesmas | http://terminology.kemkes.go.id/sp |
| 19 | 154 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000118 | Rujukan dari Rumah Bersalin / Klinik | http://terminology.kemkes.go.id/sp |
| 20 | 155 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000119 | Rujukan dari Rumah Sakit | http://terminology.kemkes.go.id/sp |
| 21 | 166 | Observation | `Observation.code.coding` | 11996-6 | [#] Pregnancies | http://loinc.org |
| 22 | 177 | Observation | `Observation.code.coding` | 11977-6 | [#] Parity | http://loinc.org |
| 23 | 188 | Observation | `Observation.code.coding` | 69043-8 | Other pregnancy outcomes # | http://loinc.org |
| 24 | 199 | Observation | `Observation.code.coding` | 11977-6 | [#] Parity | http://loinc.org |
| 25 | 200 | Observation | `Observation.code.coding` | ANC.B6.DE32 | Parity | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 26 | 211 | Observation | `Observation.code.coding` | 8665-2 | Last menstrual period start date | http://loinc.org |
| 27 | 212 | Observation | `Observation.code.coding` | ANC.B6.DE14 | Last menstrual period (LMP) date | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 28 | 223 | Observation | `Observation.code.coding` | 11778-8 | Delivery date Estimated | http://loinc.org |
| 29 | 224 | Observation | `Observation.code.coding` | ANC.B6.DE22 | Expected date of delivery (EDD) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 30 | 236 | Observation | `Observation.code.coding` | SP000050 | Riwayat Onset Persalinan | http://loinc.org |
| 31 | 248 | Observation | `Observation.code.coding` | SP000132 | Memiliki Buku KIA | http://terminology.kemkes.go.id/sp |
| 32 | 260 | Observation | `Observation.code.coding` | 56077-1 | Body weight --pre current pregnancy | http://loinc.org |
| 33 | 261 | Observation | `Observation.code.coding` | ANC.B8.DE2 | Pre-gestational weight | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 34 | 273 | Observation | `Observation.code.coding` | 18185-9 | Gestational age | http://loinc.org |
| 35 | 274 | Observation | `Observation.code.coding` | ANC.B6.DE17 | Gestational age | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 36 | 286 | Observation | `Observation.code.coding` | 32418-6 | Obstetric trimester Stated | http://loinc.org |
| 37 | 287 | Observation | `Observation.code.coding` | ANC.SS.DE13 | Trimester ke | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 38 | 298 | Condition | `Condition.code.coding` | 404684003 | Clinical finding | http://snomed.info/sct |
| 39 | 307 | Observation | `Observation.code.coding` | 3401000175105 | Total number of prenatal care visits | http://snomed.info/sct |
| 40 | 318 | Observation | `Observation.code.coding` | SP000134 | Jenis Lokasi Screening | http://terminology.kemkes.go.id/sp |
| 41 | 319 | Observation | `Observation.valueCodeableConcept.coding` | 264362003 | Home | http://snomed.info/sct |
| 42 | 320 | Observation | `Observation.valueCodeableConcept.coding` | OT000001 | Polindes | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 43 | 321 | Observation | `Observation.valueCodeableConcept.coding` | OT000002 | Pustu | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 44 | 322 | Observation | `Observation.valueCodeableConcept.coding` | 102 | Pusat Kesehatan Masyarakat | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 45 | 323 | Observation | `Observation.valueCodeableConcept.coding` | 103 | Klinik | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 46 | 324 | Observation | `Observation.valueCodeableConcept.coding` | OT000008 | Rumah Bersalin | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 47 | 325 | Observation | `Observation.valueCodeableConcept.coding` | 82242000 | Children’s hospital | http://snomed.info/sct |
| 48 | 326 | Observation | `Observation.valueCodeableConcept.coding` | 104 | Rumah Sakit | hhttp://terminology.kemkes.go.id/CodeSystem/organization-type |
| 49 | 327 | Observation | `Observation.valueCodeableConcept.coding` | OT000003 | RS ODHA | hhttp://terminology.kemkes.go.id/CodeSystem/organization-type |
| 50 | 328 | Observation | `Observation.valueCodeableConcept.coding` | OT000004 | Bidan Praktek Mandiri | hhttp://terminology.kemkes.go.id/CodeSystem/organization-type |
| 51 | 329 | Observation | `Observation.valueCodeableConcept.coding` | LT000008 | Dalam perjalanan dari rumah/masyarakat | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 52 | 339 | Observation | `Observation.code.coding` | SP000131 | Status Pindahan | http://terminology.kemkes.go.id/sp |
| 53 | 352 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 54 | 353 | Observation | `Observation.code.coding` | ANC.B8.DE3 | Current weight | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 55 | 365 | Observation | `Observation.code.coding` | 8302-2 | Body height | http://loinc.org |
| 56 | 366 | Observation | `Observation.code.coding` | ANC.B8.DE1 | Height | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 57 | 378 | Observation | `Observation.code.coding` | 284473002 | Mid upper arm circumference | http://snomed.info/sct |
| 58 | 387 | Observation | `Observation.interpretation` | OI000018 | Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 59 | 388 | Observation | `Observation.interpretation` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 60 | 389 | Observation | `Observation.interpretation` | OI000035 | Risiko Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 61 | 392 | Observation | `Observation.code.coding` | 10197-2 | Physical findings of Eye Narrative | http://loinc.org |
| 62 | 393 | Observation | `Observation.code.coding` | ANC.SS.DE26 | Pemeriksaan Fisik Konjungtiva | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 63 | 395 | Observation | `Observation.interpretation[0].coding[0]` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 64 | 396 | Observation | `Observation.interpretation[0].coding[0]` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 65 | 407 | Observation | `Observation.code.coding` | 10197-2 | Physical findings of Eye Narrative | http://loinc.org |
| 66 | 408 | Observation | `Observation.code.coding` | ANC.SS.DE27 | Pemeriksaan Fisik Sklera | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 67 | 410 | Observation | `Observation.interpretation[0].coding[0]` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 68 | 411 | Observation | `Observation.interpretation[0].coding[0]` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 69 | 422 | Observation | `Observation.code.coding` | 10206-1 | Physical findings of Skin Narrative | http://loinc.org |
| 70 | 424 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 71 | 425 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 72 | 435 | Observation | `Observation.code.coding` | 11411-6 | Physical findings of Neck Narrative | http://loinc.org |
| 73 | 436 | Observation | `Observation.code.coding` | ANC.SS.DE28 | Pemeriksaan Fisik Leher | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 74 | 437 | Observation | `Observation.interpretation[0].coding[0]` | N | Normal | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 75 | 438 | Observation | `Observation.interpretation[0].coding[0]` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 76 | 449 | Observation | `Observation.code.coding` | 32453-3 | Physical findings of Mouth | http://loinc.org |
| 77 | 450 | Observation | `Observation.code.coding` | ANC.SS.DE29 | Pemeriksaan Fisik Area Mulut | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 78 | 452 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 79 | 453 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 80 | 463 | Observation | `Observation.code.coding` | 297268004 | Ear, nose and throat finding | http://snomed.info/sct |
| 81 | 464 | Observation | `Observation.code.coding` | ANC.SS.DE30 | Pemeriksaan Fisik Telinga Hidung dan Tenggorokan (THT) | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 82 | 465 | Observation | `Observation.interpretation[0].coding[0]` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 83 | 466 | Observation | `Observation.interpretation[0].coding[0]` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 84 | 477 | Observation | `Observation.code.coding` | 10200-4 | Physical findings of Heart Narrative | http://loinc.org |
| 85 | 478 | Observation | `Observation.code.coding` | ANC.SS.DE31 | Pemeriksaan Fisik Dada (Auskultasi Jantung) | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 86 | 479 | Observation | `Observation.interpretation[0].coding[0]` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 87 | 480 | Observation | `Observation.interpretation[0].coding[0]` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 88 | 491 | Observation | `Observation.code.coding` | 301230006 | Lung finding | http://snomed.info/sct |
| 89 | 492 | Observation | `Observation.code.coding` | ANC.SS.DE32 | Pemeriksaan Fisik Dada (Auskultasi Paru) | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 90 | 493 | Observation | `Observation.interpretation[0].coding[0]` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 91 | 494 | Observation | `Observation.interpretation[0].coding[0]` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 92 | 505 | Observation | `Observation.code.coding` | 10191-5 | Physical findings of Abdomen Narrative | http://loinc.org |
| 93 | 506 | Observation | `Observation.code.coding` | ANC.SS.DE33 | Pemeriksaan Fisik Perut | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 94 | 508 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 95 | 509 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 96 | 519 | Observation | `Observation.code.coding` | 116307009 | Finding of upper limb | http://snomed.info/sct |
| 97 | 520 | Observation | `Observation.code.coding` | ANC.SS.DE34 | Pemeriksaan Fisik Tungkai | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 98 | 521 | Observation | `Observation.interpretation[0].coding[0]` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 99 | 522 | Observation | `Observation.interpretation[0].coding[0]` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 100 | 533 | Observation | `Observation.code.coding` | 116312005 | Finding of lower limb | http://snomed.info/sct |
| 101 | 534 | Observation | `Observation.code.coding` | ANC.SS.DE34 | Pemeriksaan Fisik Tungkai | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 102 | 535 | Observation | `Observation.interpretation[0].coding[0]` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 103 | 536 | Observation | `Observation.interpretation[0].coding[0]` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 104 | 547 | Observation | `Observation.code.coding` | 102572006 | Edema of lower extremity (finding) | http://snomed.info/sct |
| 105 | 548 | Observation | `Observation.code.coding` | ANC.SS.DE34 | Pemeriksaan Fisik Tungkai | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 106 | 549 | Observation | `Observation.interpretation[0].coding[0]` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 107 | 550 | Observation | `Observation.interpretation[0].coding[0]` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 108 | 561 | Observation | `Observation.code.coding` | 299412000 | Finding of patella structure | http://snomed.info/sct |
| 109 | 562 | Observation | `Observation.code.coding` | ANC.SS.DE34 | Pemeriksaan Fisik Tungkai | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 110 | 563 | Observation | `Observation.interpretation[0].coding[0]` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 111 | 564 | Observation | `Observation.interpretation[0].coding[0]` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 112 | 575 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 113 | 576 | Observation | `Observation.code.coding` | ANC.B8.DE17 | Systolic blood pressure | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 114 | 588 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://loinc.org |
| 115 | 589 | Observation | `Observation.code.coding` | ANC.B8.DE19 | Diastolic blood pressure | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 116 | 601 | Observation | `Observation.code.coding` | 8867-4 | Heart rate | http://loinc.org |
| 117 | 614 | Observation | `Observation.code.coding` | 8310-5 | Body temperature | http://loinc.org |
| 118 | 626 | Observation | `Observation.code.coding` | 9279-1 | Respiratory rate | http://loinc.org |
| 119 | 627 | Observation | `Observation.code.coding` | ANC.SS.DE2 | Pernapasan | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 120 | 640 | Observation | `Observation.code.coding` | 8478-0 | Mean blood pressure | http://loinc.org |
| 121 | 653 | Observation | `Observation.code.coding` | SP000634 | Tinggi fundus terdeteksi | http://terminology.kemkes.go.id/sp |
| 122 | 665 | Observation | `Observation.code.coding` | 11881-0 | Uterus Fundal height Tape measure | http://loinc.org |
| 123 | 677 | Observation | `Observation.code.coding` | SP000635 | Tinggi fundus jari | http://terminology.kemkes.go.id/sp |
| 124 | 688 | Procedure | `Procedure.code.coding` | 88.78 | Diagnostic ultrasound of gravid uterus | http://hl7.org/fhir/sid/icd-9-cm |
| 125 | 703 | ServiceRequest | `ServiceRequest.code` | 11525-3 | US for pregnancy | http://loinc.org |
| 126 | 710 | PractitionerRole | `PractitionerRole.code.coding` | 66862007 | Radiologist | http://snomed.info/sct |
| 127 | 714 | Observation | `Observation.code.coding[x]` | 11850-5 | Gestational sac Mean diameter US | http://loinc.org |
| 128 | 715 | Observation | `Observation.code.coding[x]` | ANC.SS.DE36 | Gestational sac (GS) USG | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 129 | 728 | DiagnosticReport | `DiagnosticReport.code.coding` | 11850-5 | Gestational sac Mean diameter US | http://loinc.org |
| 130 | 741 | ServiceRequest | `ServiceRequest.code` | 11525-3 | US for pregnancy | http://loinc.org |
| 131 | 748 | PractitionerRole | `PractitionerRole.code.coding` | 66862007 | Radiologist | http://snomed.info/sct |
| 132 | 752 | Observation | `Observation.code.coding[x]` | 11957-8 | Fetal Crown Rump length US | http://loinc.org |
| 133 | 753 | Observation | `Observation.code.coding[x]` | ANC.SS.DE37 | Fetal Crown Rump Length (CRL) USG | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 134 | 766 | DiagnosticReport | `DiagnosticReport.code.coding` | 11957-8 | Fetal Crown Rump length US | http://loinc.org |
| 135 | 779 | ServiceRequest | `ServiceRequest.code` | 11525-3 | US for pregnancy | http://loinc.org |
| 136 | 786 | PractitionerRole | `PractitionerRole.code.coding` | 66862007 | Radiologist | http://snomed.info/sct |
| 137 | 790 | Observation | `Observation.code.coding[x]` | 11948-7 | Fetal Heart rate US | http://loinc.org |
| 138 | 791 | Observation | `Observation.code.coding[x]` | ANC.SS.DE38 | Denyut Jantung Janin (DJJ) USG | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 139 | 804 | DiagnosticReport | `DiagnosticReport.code.coding` | 11948-7 | Fetal Heart rate US | http://loinc.org |
| 140 | 817 | ServiceRequest | `ServiceRequest.code` | 11525-3 | US for pregnancy | http://loinc.org |
| 141 | 824 | PractitionerRole | `PractitionerRole.code.coding` | 66862007 | Radiologist | http://snomed.info/sct |
| 142 | 828 | Observation | `Observation.code.coding[x]` | 11820-8 | Fetal Head Diameter.biparietal US | http://loinc.org |
| 143 | 841 | DiagnosticReport | `DiagnosticReport.code.coding` | 11820-8 | Fetal Head Diameter.biparietal US | http://loinc.org |
| 144 | 854 | ServiceRequest | `ServiceRequest.code` | 11525-3 | US for pregnancy | http://loinc.org |
| 145 | 861 | PractitionerRole | `PractitionerRole.code.coding` | 66862007 | Radiologist | http://snomed.info/sct |
| 146 | 865 | Observation | `Observation.code.coding[x]` | 11984-2 | Fetal Head Circumference US | http://loinc.org |
| 147 | 878 | DiagnosticReport | `DiagnosticReport.code.coding` | 11984-2 | Fetal Head Circumference US | http://loinc.org |
| 148 | 891 | ServiceRequest | `ServiceRequest.code` | 11525-3 | US for pregnancy | http://loinc.org |
| 149 | 898 | PractitionerRole | `PractitionerRole.code.coding` | 66862007 | Radiologist | http://snomed.info/sct |
| 150 | 902 | Observation | `Observation.code.coding[x]` | 11979-2 | Fetal Abdomen Circumference US | http://loinc.org |
| 151 | 915 | DiagnosticReport | `DiagnosticReport.code.coding` | 11979-2 | Fetal Abdomen Circumference US | http://loinc.org |
| 152 | 928 | ServiceRequest | `ServiceRequest.code` | 11525-3 | US for pregnancy | http://loinc.org |
| 153 | 935 | PractitionerRole | `PractitionerRole.code.coding` | 66862007 | Radiologist | http://snomed.info/sct |
| 154 | 939 | Observation | `Observation.code.coding[x]` | 11963-6 | Fetal Femur diaphysis [Length] US | http://loinc.org |
| 155 | 952 | DiagnosticReport | `DiagnosticReport.code.coding` | 11963-6 | Fetal Femur diaphysis [Length] US | http://loinc.org |
| 156 | 965 | ServiceRequest | `ServiceRequest.code` | 11525-3 | US for pregnancy | http://loinc.org |
| 157 | 972 | PractitionerRole | `PractitionerRole.code.coding` | 66862007 | Radiologist | http://snomed.info/sct |
| 158 | 976 | Observation | `Observation.code.coding[x]` | 11832-3 | Fetal Amniotic fluid space Maximum diameter largest pocket US | http://loinc.org |
| 159 | 989 | DiagnosticReport | `DiagnosticReport.code.coding` | 11832-3 | Fetal Amniotic fluid space Maximum diameter largest pocket US | http://loinc.org |
| 160 | 999 | Observation | `Observation.code.coding` | 365662002 | Finding of amniotic fluid appearance | http://snomed.info/sct |
| 161 | 1000 | Observation | `Observation.valueCodeableConcept.coding` | 168090003 | Amniotic fluid clear | http://snomed.info/sct |
| 162 | 1001 | Observation | `Observation.valueCodeableConcept.coding` | 408781009 | Straw colored amniotic fluid | http://snomed.info/sct |
| 163 | 1002 | Observation | `Observation.valueCodeableConcept.coding` | 249134008 | Bloodstained liquor | http://snomed.info/sct |
| 164 | 1003 | Observation | `Observation.valueCodeableConcept.coding` | 168092006 | Amniotic fluid -meconium stain | http://snomed.info/sct |
| 165 | 1016 | ServiceRequest | `ServiceRequest.code` | 11525-3 | US for pregnancy | http://snomed.info/sct |
| 166 | 1023 | PractitionerRole | `PractitionerRole.code.coding` | 66862007 | Radiologist | http://snomed.info/sct |
| 167 | 1027 | Observation | `Observation.code.coding[x]` | 271692001 | Presentation of fetus | http://snomed.info/sct |
| 168 | 1028 | Observation | `Observation.code.coding[x]` | ANC.SS.DE41 | Letak Janin USG | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 169 | 1029 | Observation | `Observation.valueCodeableConcept[0].coding[0]` | 398236008 | Intrauterine | http://snomed.info/sct |
| 170 | 1030 | Observation | `Observation.valueCodeableConcept[0].coding[0]` | 298109001 | Ectopic | http://snomed.info/sct |
| 171 | 1040 | DiagnosticReport | `DiagnosticReport.code.coding` | 72155-5 | Position in womb Fetus [RHEA] | http://snomed.info/sct |
| 172 | 1053 | ServiceRequest | `ServiceRequest.code` | 11525-3 | US for pregnancy | http://snomed.info/sct |
| 173 | 1060 | PractitionerRole | `PractitionerRole.code.coding` | 66862007 | Radiologist | http://snomed.info/sct |
| 174 | 1064 | Observation | `Observation.code.coding[x]` | 11877-8 | Fetal presentation US | http://loinc.org |
| 175 | 1065 | Observation | `Observation.code.coding[x]` | ANC.B8.DE111 | Fetal presentation | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 176 | 1066 | Observation | `Observation.valueCodeableConcept.coding` | 1209182005 | Cephalic fetal presentation | http://snomed.info/sct |
| 177 | 1067 | Observation | `Observation.valueCodeableConcept.coding` | 6096002 | Breech presentation | http://snomed.info/sct |
| 178 | 1068 | Observation | `Observation.valueCodeableConcept.coding` | SP000006 | Organ Tubuh Lainnya | http://terminology.kemkes.go.id/sp |
| 179 | 1069 | Observation | `Observation.valueCodeableConcept.coding` | 260415000 | Not detected | http://snomed.info/sct |
| 180 | 1079 | DiagnosticReport | `DiagnosticReport.code.coding` | 11877-8 | Fetal presentation US | http://loinc.org |
| 181 | 1092 | ServiceRequest | `ServiceRequest.code` | 11525-3 | US for pregnancy | http://loinc.org |
| 182 | 1099 | PractitionerRole | `PractitionerRole.code.coding` | 66862007 | Radiologist | http://snomed.info/sct |
| 183 | 1103 | Observation | `Observation.code.coding[x]` | 11878-6 | Number of fetuses by US | http://loinc.org |
| 184 | 1104 | Observation | `Observation.code.coding[x]` | ANC.B8.DE109 | Number of fetuses | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 185 | 1115 | DiagnosticReport | `DiagnosticReport.code.coding` | 11878-6 | Number of fetuses by US | http://loinc.org |
| 186 | 1126 | Observation | `Observation.code.coding` | 55283-6 | Fetal Heart rate | http://loinc.org |
| 187 | 1127 | Observation | `Observation.code.coding` | ANC.B8.DE107 | Fetal heart rate | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 188 | 1137 | Observation | `Observation.interpretation.coding` | 289441006 | Normal fetal heart rate | http://snomed.info/sct |
| 189 | 1138 | Observation | `Observation.interpretation.coding` | 289440007 | Fetal heart rate not observed | http://snomed.info/sct |
| 190 | 1139 | Observation | `Observation.interpretation.coding` | 312668007 | Abnormal fetal heart rate | http://snomed.info/sct |
| 191 | 1140 | Observation | `Observation.interpretation.coding` | 289439005 | Fetal heart rate absent | http://snomed.info/sct |
| 192 | 1144 | Observation | `Observation.code.coding` | 249111004 | Engagement of head | http://snomed.info/sct |
| 193 | 1145 | Observation | `Observation.valueCodeableConcept.coding` | 249112006 | Head engaged | http://snomed.info/sct |
| 194 | 1146 | Observation | `Observation.valueCodeableConcept.coding` | 62098001 | Head not engaged | http://snomed.info/sct |
| 195 | 1157 | Observation | `Observation.code.coding` | 72155-5 | Position in womb Fetus [RHEA] | http://loinc.org |
| 196 | 1158 | Observation | `Observation.code.coding` | ANC.B8.DE111 | Fetal presentation | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 197 | 1159 | Observation | `Observation.valueCodeableConcept.coding` | 1209182005 | Cephalic fetal presentation | http://snomed.info/sct |
| 198 | 1160 | Observation | `Observation.valueCodeableConcept.coding` | SP000005 | Letak Bokong/ Lintang | http://terminology.kemkes.go.id/sp |
| 199 | 1161 | Observation | `Observation.valueCodeableConcept.coding` | SP000006 | Organ Tubuh Lainnya | http://terminology.kemkes.go.id/sp |
| 200 | 1172 | Observation | `Observation.code.coding` | 89087-1 | Fetal Body weight Estimated | http://loinc.org |
| 201 | 1173 | Observation | `Observation.code.coding` | ANC.SS.DE1 | Taksiran Berat Janin (TBJ) | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 202 | 1187 | ServiceRequest | `ServiceRequest.code` | 11525-3 | US for pregnancy | http://loinc.org |
| 203 | 1194 | PractitionerRole | `PractitionerRole.code.coding` | 66862007 | Radiologist | http://snomed.info/sct |
| 204 | 1198 | Observation | `Observation.code.coding[x]` | 11888-5 | Gestational age US composite estimate | http://loinc.org |
| 205 | 1199 | Observation | `Observation.code.coding[x]` | ANC.B6.DE20 | Ultrasound | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 206 | 1212 | DiagnosticReport | `DiagnosticReport.code.coding` | 11888-5 | Gestational age US composite estimate | http://loinc.org |
| 207 | 1225 | ServiceRequest | `ServiceRequest.code` | 11525-3 | US for pregnancy | http://loinc.org |
| 208 | 1232 | PractitionerRole | `PractitionerRole.code.coding` | 66862007 | Radiologist | http://snomed.info/sct |
| 209 | 1236 | Observation | `Observation.code.coding[x]` | 11781-2 | Delivery date US composite estimate | http://loinc.org |
| 210 | 1237 | Observation | `Observation.code.coding[x]` | ANC.SS.DE40 | Hari Perkiraan Lahir (HPL) USG | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 211 | 1248 | DiagnosticReport | `DiagnosticReport.code.coding` | 11781-2 | Delivery date US composite estimate | http://loinc.org |
| 212 | 1260 | Immunization | `Immunization.vaccineCode` | VG139 | Td | http://sys-ids.kemkes.go.id/kfa |
| 213 | 1277 | Immunization | `Immunization.vaccineCode` | VG139 | Td | http://sys-ids.kemkes.go.id/kfa |
| 214 | 1294 | Immunization | `Immunization.vaccineCode` | VG139 | Td | http://sys-ids.kemkes.go.id/kfa |
| 215 | 1307 | Observation | `Observation.code.coding` | SP000001 | Skrining Imunisasi Tetanus Toksoid | http://terminology.kemkes.go.id/sp |
| 216 | 1318 | Observation | `Observation.code.coding` | SP000002 | Kunjungan Pertama Pemeriksaan Kehamilan | http://terminology.kemkes.go.id/sp |
| 217 | 1329 | Observation | `Observation.code.coding` | 883-9 | ABO group [Type] in Blood | http://loinc.org |
| 218 | 1330 | Observation | `Observation.code.coding` | ANC.B9.DE24 | Blood type | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 219 | 1331 | Observation | `Observation.valueCodeableConcept.coding` | LA19710-5 | Group A | http://loinc.org |
| 220 | 1332 | Observation | `Observation.valueCodeableConcept.coding` | LA19709-7 | Group B | http://loinc.org |
| 221 | 1333 | Observation | `Observation.valueCodeableConcept.coding` | LA19708-9 | Group O | http://loinc.org |
| 222 | 1334 | Observation | `Observation.valueCodeableConcept.coding` | LA28449-9 | Group AB | http://loinc.org |
| 223 | 1344 | Observation | `Observation.code.coding` | 10331-7 | Rh [Type] in Blood | http://loinc.org |
| 224 | 1345 | Observation | `Observation.code.coding` | ANC.B9.DE29 | Rh factor | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 225 | 1346 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 226 | 1347 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 227 | 1357 | Condition | `Condition.code.coding` | 34842007 | Antepartum hemorrhage | http://snomed.info/sct |
| 228 | 1358 | Condition | `Condition.code.coding` | 15938005 | Eclampsia | http://snomed.info/sct |
| 229 | 1359 | Condition | `Condition.code.coding` | 398254007 | Pre-eclampsia | http://snomed.info/sct |
| 230 | 1360 | Condition | `Condition.code.coding` | 386639001 | Termination of pregnancy | http://snomed.info/sct |
| 231 | 1361 | Condition | `Condition.code.coding` | 40733004 | Infectious disease | http://snomed.info/sct |
| 232 | 1362 | Condition | `Condition.code.coding` | 91302008 | Sepsis | http://snomed.info/sct |
| 233 | 1363 | Condition | `Condition.code.coding` | 74964007 | Other | http://snomed.info/sct |
| 234 | 1371 | Observation | `Observation.code.coding` | 268445003 | Ultrasound scan - obstetric | http://snomed.info/sct |
| 235 | 1372 | Observation | `Observation.valueCodeableConcept.coding` | 169221005 | Ultrasound obstetric scan normal | http://snomed.info/sct |
| 236 | 1373 | Observation | `Observation.valueCodeableConcept.coding` | 169255008 | Ultrasound scan abnormal | http://snomed.info/sct |
| 237 | 1386 | MedicationRequest | `MedicationRequest.contained.code.coding` | 92000653 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula | http://sys-ids.kemkes.go.id/kf |
| 238 | 1420 | MedicationDispense | `MedicationDispense.contained.code.coding` | 93015491 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | http://sys-ids.kemkes.go.id/kfa |
| 239 | 1453 | ServiceRequest | `ServiceRequest.code` | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 240 | 1464 | Specimen | `Specimen.type` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 241 | 1473 | Observation | `Observation.code.coding` | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 242 | 1474 | Observation | `Observation.code.coding` | ANC.B9.DE32 | HIV test | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 243 | 1475 | Observation | `Observation.valueCodeableConcept.coding` | LA15255-5 | Reactive | http://loinc.org |
| 244 | 1476 | Observation | `Observation.valueCodeableConcept.coding` | LA15256-3 | Nonreactive | http://loinc.org |
| 245 | 1487 | DiagnosticReport | `DiagnosticReport.code` | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 246 | 1501 | ServiceRequest | `ServiceRequest.code` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 247 | 1512 | Specimen | `Specimen.type` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 248 | 1521 | Observation | `Observation.code.coding` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 249 | 1522 | Observation | `Observation.code.coding` | ANC.B9.DE60 | Hepatitis B test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 250 | 1523 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 251 | 1524 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 252 | 1535 | DiagnosticReport | `DiagnosticReport.code` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 253 | 1549 | ServiceRequest | `ServiceRequest.code` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 254 | 1560 | Specimen | `Specimen.type` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 255 | 1569 | Observation | `Observation.code.coding` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 256 | 1570 | Observation | `Observation.code.coding` | ANC.B9.DE96 | Syphilis test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 257 | 1571 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 258 | 1572 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 259 | 1583 | DiagnosticReport | `DiagnosticReport.code` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 260 | 1597 | ServiceRequest | `ServiceRequest.code` | 2887-8 | Protein [Presence] in Urine | http://loinc.org |
| 261 | 1608 | Specimen | `Specimen.type` | 122575003 | Urine specimen | http://snomed.info/sct |
| 262 | 1617 | Observation | `Observation.code.coding` | 2887-8 | Protein [Presence] in Urine | http://loinc.org |
| 263 | 1618 | Observation | `Observation.code.coding` | ANC.B9.DE114 | Urine test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 264 | 1619 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 265 | 1620 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 266 | 1631 | DiagnosticReport | `DiagnosticReport.code.coding` | 2887-8 | Protein [Presence] in Urine | http://loinc.org |
| 267 | 1645 | ServiceRequest | `ServiceRequest.code` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 268 | 1656 | Specimen | `Specimen.type` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 269 | 1665 | Observation | `Observation.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 270 | 1666 | Observation | `Observation.code.coding` | ANC.B9.DE175 | Blood hemoglobin test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 271 | 1683 | DiagnosticReport | `DiagnosticReport.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 272 | 1697 | ServiceRequest | `ServiceRequest.code` | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | http://loinc.org |
| 273 | 1708 | Specimen | `Specimen.type` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 274 | 1717 | Observation | `Observation.code.coding` | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | http://loinc.org |
| 275 | 1718 | Observation | `Observation.code.coding` | ANC.B9.DE159 | Blood glucose test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 276 | 1733 | DiagnosticReport | `DiagnosticReport.code.coding` | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | http://loinc.org |
| 277 | 1745 | Observation | `Observation.code.coding` | 15220000 | Laboratory test | http://snomed.info/sct |
| 278 | 1746 | Observation | `Observation.valueCodeableConcept.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 279 | 1747 | Observation | `Observation.valueCodeableConcept.coding` | 76772-3 | Plasmodium falciparum Ag [Presence] in Blood by Rapid immunoassay | http://loinc.org |
| 280 | 1748 | Observation | `Observation.valueCodeableConcept.coding` | 104742-2 | Ova and parasites identified in Specimen | http://loinc.org |
| 281 | 1749 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 282 | 1760 | Observation | `Observation.code.coding` | SP000007 | Tatalaksana Anemia | http://terminology.kemkes.go.id/sp |
| 283 | 1761 | Observation | `Observation.valueCodeableConcept.coding` | SP000008 | Pemberian Tablet Tambah Darah | http://terminology.kemkes.go.id/sp |
| 284 | 1762 | Observation | `Observation.valueCodeableConcept.coding` | SP000009 | Pemberian Fe Parenteral | http://terminology.kemkes.go.id/sp |
| 285 | 1763 | Observation | `Observation.valueCodeableConcept.coding` | 116859006 | Transfusion of blood product | http://snomed.info/sct |
| 286 | 1764 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 287 | 1766 | Observation | `Observation.valueCodeableConcept.coding` | 3457005 | Patient referral | http://snomed.info/sct |
| 288 | 1777 | Observation | `Observation.code.coding` | SP000010 | Skrining Hipertensi dalam Kehamilan | http://terminology.kemkes.go.id/sp |
| 289 | 1778 | Observation | `Observation.valueCodeableConcept.coding` | SP000011 | Tidak Pre Eklampsia/ Eklampsia | http://terminology.kemkes.go.id/sp |
| 290 | 1779 | Observation | `Observation.valueCodeableConcept.coding` | 48194001 | Pregnancy-induced hypertension | http://snomed.info/sct |
| 291 | 1780 | Observation | `Observation.valueCodeableConcept.coding` | 398254007 | Pre-eclampsia | http://snomed.info/sct |
| 292 | 1781 | Observation | `Observation.valueCodeableConcept.coding` | 15938005 | Eclampsia | http://snomed.info/sct |
| 293 | 1792 | Observation | `Observation.code.coding` | SP000012 | Tatalaksana Pre Eklampsia | http://terminology.kemkes.go.id/sp |
| 294 | 1795 | Observation | `Observation.component.code.coding` | 135840009 | Blood pressure monitoring | http://snomed.info/sct |
| 295 | 1798 | Observation | `Observation.component.code.coding` | 308116003 | Antihypertensive therapy | http://snomed.info/sct |
| 296 | 1801 | Observation | `Observation.component.code.coding` | SP000013 | Pemberian MgSO4 | http://terminology.kemkes.go.id/sp |
| 297 | 1804 | Observation | `Observation.component.code.coding` | 74964007 | Other | http://snomed.info/sct |
| 298 | 1806 | Observation | `Observation.component.code.coding` | 3457005 | Patient referral | http://snomed.info/sct |
| 299 | 1820 | Observation | `Observation.code.coding` | SP000014 | Tatalaksana KEK | http://terminology.kemkes.go.id/sp |
| 300 | 1823 | Observation | `Observation.component.code.coding` | 435591000124104 | Nutrition supplement therapy | http://snomed.info/sct |
| 301 | 1826 | Observation | `Observation.component.code.coding` | 3457005 | Patient referral | http://snomed.info/sct |
| 302 | 1839 | Observation | `Observation.code.coding` | SP000015 | Risiko Masalah Kesehatan | http://terminology.kemkes.go.id/sp |
| 303 | 1842 | Observation | `Observation.component.code.coding` | 40733004 | Infectious disease | http://snomed.info/sct |
| 304 | 1845 | Observation | `Observation.component.code.coding` | 73211009 | Diabetes mellitus | http://snomed.info/sct |
| 305 | 1848 | Observation | `Observation.component.code.coding` | 414916001 | Obesity | http://snomed.info/sct |
| 306 | 1851 | Observation | `Observation.component.code.coding` | 56717001 | Tuberculosis | http://snomed.info/sct |
| 307 | 1854 | Observation | `Observation.component.code.coding` | 56265001 | Heart disease | http://snomed.info/sct |
| 308 | 1857 | Observation | `Observation.component.code.coding` | 74964007 | Other | http://snomed.info/sct |
| 309 | 1868 | Observation | `Observation.code.coding` | SP000016 | Tatalaksana Masalah Kesehatan | http://terminology.kemkes.go.id/sp |
| 310 | 1879 | Procedure | `Procedure.code.coding` | 1230101008 | Counseling for pregnancy | http://snomed.info/sct |
| 311 | 1890 | Procedure | `Procedure.code.coding` | 385892002 | Mental health screening | http://snomed.info/sct |
| 312 | 1903 | Observation | `Observation.code.coding` | OC000001 | Jarak kehamilan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 313 | 1904 | Observation | `Observation.code.coding` | ANC.SS.DE53 | Jarak kehamilan | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 314 | 1916 | Observation | `Observation.code.coding` | 73211009 | Diabetes mellitus | http://snomed.info/sct |
| 315 | 1928 | Observation | `Observation.code.coding` | 278977008 | Human immunodeficiency virus status | http://snomed.info/sct |
| 316 | 1929 | Observation | `Observation.valueCodeableConcept.coding` | 165816005 | Human immunodeficiency virus detected | http://snomed.info/sct |
| 317 | 1930 | Observation | `Observation.valueCodeableConcept.coding` | 165815009 | Human immunodeficiency virus not detected | http://snomed.info/sct |
| 318 | 1940 | Observation | `Observation.code.coding` | 66071002 | Viral hepatitis type B | http://snomed.info/sct |
| 319 | 1952 | Observation | `Observation.code.coding` | 76272004 | Syphilis | http://snomed.info/sct |
| 320 | 1964 | Observation | `Observation.code.coding` | 61462000 | Malaria | http://snomed.info/sct |
| 321 | 1976 | Observation | `Observation.code.coding` | 56717001 | Tuberculosis | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://loinc.org | 101 |
| http://snomed.info/sct | 99 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 27 |
| http://terminology.kemkes.go.id/sp | 24 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 23 |
| http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes | 20 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC | 7 |
| http://terminology.kemkes.go.id/CodeSystem/organization-type | 5 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 4 |
| http://sys-ids.kemkes.go.id/kfa | 4 |
| hhttp://terminology.kemkes.go.id/CodeSystem/organization-type | 3 |
| http://terminology.hl7.org/CodeSystem/admit-source | 1 |
| http://terminology.kemkes.go.id/CodeSystem/location-type | 1 |
| http://hl7.org/fhir/sid/icd-9-cm | 1 |
| http://sys-ids.kemkes.go.id/kf | 1 |
| **Total** | **321** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 30 | – | Faskes yang Melayani ANC | Organization | `Organization.type` |
| 35 | – | nama_faskes | Organization | `Organization.name` |
| 39 | – | provinsi | Organization | `Organization.address.extension.extension.url` |
| 42 | – | kota | Organization | `Organization.address.extension.extension.url` |
| 45 | – | Nama Kecamatan | Organization | `Organization.address.extension.extension.url` |
| 48 | – | Nama Desa | Organization | `Organization.address.extension.extension.url` |
| 50 | – | Tempat Pelayanan ANC | Location | `Location.identifier` |
| 58 | – | Nama Provinsi | Location | `Location.address.extension.extension.url` |
| 61 | – | Nama Kabupaten | Location | `Location.address.extension.extension.url` |
| 64 | – | Nama Kecamatan | Location | `Location.address.extension.extension.url` |
| 67 | – | Nama Desa | Location | `Location.address.extension.extension.url` |
| 349 | – | Status_Faskes | – | `` |
| 1141 | – | Posisi_Janin | – | `` |
| 1257 | – | Status | – | `` |
| 1986 | – | ART | – | `Observation` |
| 1998 | – | Obat Anti Malaria | – | `Observation` |
| 2019 | – | Obat Anti Tuberkulosis (OAT) | – | `Observation` |
| 2043 | – | Obat Diabetes Melitus | – | `Observation` |
