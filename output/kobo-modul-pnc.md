# Output Form: Kobo Modul PNC

Sumber: `mapping/phdt-data-dictionary-kobo-modul-pnc.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-kobo-modul-pnc.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 98 |
| Code (`jumlah code` = 1) | 225 |
| Code unik (code + CodeSystem) | 191 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 27 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–8 | Patient | – | – | _Nama Ibu_ → `Patient.name.text` (2, tanpa BQ)<br>_NIK_ → `Patient.identifier.value` (5, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (8, tanpa BQ)<br>_No HP_ → `Patient.telecom` (21, tanpa BQ)<br>_Alamat Domisili_ → `Patient.address.use` (24, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.url` (28, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.url` (31, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.url` (34, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.url` (37, tanpa BQ) |
| 2 | 9–20 | Observation | 424144002.0 | Current chronological age | _Umur_ → `Observation.valueQuantity.value` (12, tanpa BQ) |
| 3 | 88–108 | Practitioner | – | – | _Dokter/Tenaga Medis_ → `Practitioner.identifier` (88, tanpa BQ) |
| 4 | 109–115 | PractitionerRole | – | – | _jenis_tenaga_kesehatan_ → `PractitionerRole.active` (109, tanpa BQ) |
| 5 | 116–118 | PractitionerRole | – | – | _siapa_yang_melakukan_entry_data_ → `PractitionerRole.code.coding` (116, tanpa BQ) |
| 6 | 119–120 | Practitioner | – | – | _nama_yang_melakukan_entry_data_ → `Practitioner.name.text` (120, tanpa BQ) |
| 7 | 122–130 | EpisodeOfCare | PNC | Postnatal Care | _Episode Of Care ID_ → `EpisodeOfCare.Identifer` (122, tanpa BQ)<br>_Kunjungan PNC_ → `EpisodeOfCare.type.coding` (126, tanpa BQ) |
| 8 | 131–149 | Encounter | – | – | _Kunjungan PNC (KF)_ → `Encounter.identifier` (132, tanpa BQ)<br>_Tanggal Kunjungan PNC_ → `Encounter.period.start` (144, tanpa BQ)<br>_Cara Masuk_ → `Encounter.hospitalization.admitSource.coding` (192, tanpa BQ) |
| 9 | 150–157 | Condition | Z39.2 | Routine postpartum follow-up | _Diagnosis_ → `Condition.code.coding` (152, tanpa BQ) |
| 10 | 158–180 | Condition | 404684003.0 | Clinical finding | _Keluhan_ → `Condition.code.coding` (161, tanpa BQ) |
| 11 | 199–209 | Observation | 93857-1 | Date and time of obstetric delivery | _Tanggal Persalinan_ → `Observation.valueDateTime` (202, tanpa BQ) |
| 12 | 210–220 | Observation | 11996-6 | [#] Pregnancies | _Gravida_ → `Observation.valueInteger` (213, tanpa BQ) |
| 13 | 221–231 | Observation | 11977-6 | [#] Parity | _Partus_ → `Observation.valueInteger` (224, tanpa BQ) |
| 14 | 232–242 | Observation | 69043-8 | Other pregnancy outcomes # | _Abortus_ → `Observation.valueInteger` (235, tanpa BQ) |
| 15 | 243–253 | Observation | – | – | _Hari ke Sejak Melahirkan_ → `Observation.valueInteger` (246, tanpa BQ) |
| 16 | 254–265 | Observation | SP000131 | Status Pindahan | _Status Pindahan_ → `Observation.valueBoolean` (257, tanpa BQ) |
| 17 | 266–287 | Observation | SP000134 | Jenis Lokasi Screening | _Lokasi Screening_ → `Observation.valueCodeableConcept.coding` (269, tanpa BQ)<br>_Nama Faskes Lokasi Screening_ → `Observation,note` (287, tanpa BQ) |
| 18 | 288–299 | Observation | 8480-6 | Systolic blood pressure | _Tekanan Darah Sistolik_ → `Observation.valueQuantity.value` (291, tanpa BQ) |
| 19 | 300–311 | Observation | 8462-4 | Diastolic blood pressure | _Tekanan Darah Diastolik_ → `Observation.valueQuantity.value` (303, tanpa BQ) |
| 20 | 312–323 | Observation | 8867-4 | Heart rate | _Nadi_ → `Observation.valueQuantity.value` (315, tanpa BQ) |
| 21 | 324–335 | Observation | 8310-5 | Body temperature | _Suhu_ → `Observation.valueQuantity.value` (327, tanpa BQ) |
| 22 | 336–347 | Observation | 9279-1 | Respiratory rate | _Pernapasan_ → `Observation.valueQuantity.value` (339, tanpa BQ) |
| 23 | 348–354 | Condition | 289530006.0 | Vaginal bleeding | _Pendarahan Pervaginam_ → `Condition.clinicalStatus.coding` (348, tanpa BQ) |
| 24 | 355–366 | Observation | 81661-1 | Blood Loss [Volume] Measured | _Jumlah Pendarahan_ → `Observation.valueQuantity.value` (358, tanpa BQ) |
| 25 | 367–381 | Observation | 364297003.0 | Female perineum observable | _Kondisi Perineum_ → `Observation.valueCodeableConcept.coding` (370, tanpa BQ) |
| 26 | 382–393 | Observation | OC000020 | Tanda Infeksi Perineum | _Tanda Infeksi Perineum_ → `Observation.valueBoolean` (385, tanpa BQ) |
| 27 | 394–405 | Observation | OC000025 | Tanda Infeksi Luka Jahitan Sectio Caesaria | _Tanda Infeksi Luka Jahitan Sectio Caesaria_ → `Observation.valueBoolean` (397, tanpa BQ) |
| 28 | 406–420 | Observation | 32422-8 | Physical findings of breast | _Kondisi Payudara_ → `Observation.valueCodeableConcept.coding` (409, tanpa BQ) |
| 29 | 421–432 | Observation | 289700000.0 | Uterine contractions present | _Kontraksi Uteri_ → `Observation.valueBoolean` (424, tanpa BQ) |
| 30 | 433–446 | Observation | 249214003.0 | Color of lochia | _Warna Lokhia_ → `Observation.valueCodeableConcept.coding` (436, tanpa BQ) |
| 31 | 447–458 | Observation | 249215002.0 | Odor of lochia | _Bau Lokhia_ → `Observation.valueBoolean` (450, tanpa BQ) |
| 32 | 459–471 | Observation | OC000017 | Produksi ASI | _Produksi ASI_ → `Observation.valueCodeableConcept.coding` (462, tanpa BQ) |
| 33 | 472–483 | Observation | 1145307003.0 | Exclusively breastfed | _ASI Eksklusif_ → `Observation.valueBoolean` (475, tanpa BQ) |
| 34 | 484–499 | Observation | 252041008.0 | Micturition finding | _Gangguan Buang Air Kecil_ → `Observation.valueCodeableConcept.coding` (487, tanpa BQ) |
| 35 | 500–511 | Observation | 300375001.0 | Able to defecate | _Gangguan Buang Air Besar_ → `Observation.valueBoolean` (503, tanpa BQ) |
| 36 | 512–522 | Procedure | 408988007.0 | Newborn care education | _Konseling Perawatan Bayi Baru Lahir_ → `Procedure.category.coding` (512, tanpa BQ) |
| 37 | 523–534 | Observation | 8345-1 | Body weight Measured --post partum | _Berat Badan_ → `Observation.valueQuantity.value` (526, tanpa BQ) |
| 38 | 535–546 | Observation | 8305-5 | Body height --post partum | _Tinggi Badan_ → `Observation.valueQuantity.value` (538, tanpa BQ) |
| 39 | 547–559 | Observation | 284473002.0 | Mid upper arm circumference | _LILA (LIngkar Lengan Atas_ → `Observation.status` (547, tanpa BQ)<br>_Status Gizi KEK/Tidak KEK_ → `Observation.interpretation` (558, tanpa BQ) |
| 40 | 560–571 | Observation | 11881-0 | Uterus Fundal height Tape measure | _TFU (Tinggi Fundus Uteri)_ → `Observation.valueQuantity.value` (563, tanpa BQ) |
| 41 | 572–586 | Observation | 67775-7 | Level of responsiveness | _Tingkat Kesadaran_ → `Observation.status` (572, tanpa BQ) |
| 42 | 587–598 | Observation | 112648003.0 | Massive hemorrhage | _Perdarahan Masif_ → `Observation.valueBoolean` (590, tanpa BQ) |
| 43 | 599–605 | Condition | 112648003.0 | Massive hemorrhage | _date_ → `Condition.recordedDate` (605, tanpa BQ) |
| 44 | 606–617 | Observation | 91175000.0 | Seizure | _Kejang_ → `Observation.valueBoolean` (609, tanpa BQ) |
| 45 | 618–624 | Condition | 91175000.0 | Seizure | _date_ → `Condition.recordedDate` (624, tanpa BQ) |
| 46 | 625–636 | Observation | 27942005.0 | Shock | _Syok_ → `Observation.valueBoolean` (628, tanpa BQ) |
| 47 | 637–643 | Condition | 27942005.0 | Shock | _date_ → `Condition.recordedDate` (643, tanpa BQ) |
| 48 | 644–661 | Condition | 47821001.0 | Postpartum hemorrhage | _Komplikasi Masa Nifas_ → `Condition.clinicalStatus.coding` (644, tanpa BQ) |
| 49 | 662–674 | Observation | 289084000.0 | Difficulty performing breastfeeding | _Apakah ada masalah memberikan ASI_ → `Observation.valueBoolean` (665, tanpa BQ)<br>_Catatan ASI_ → `Observation.note.text` (674, tanpa BQ) |
| 50 | 675–687 | Observation | 871562009.0 | Detection of severe acute respiratory syndrome coronavirus 2 | _Pemeriksaan COVID-19_ → `Observation.valueBoolean` (678, tanpa BQ)<br>_Catat dibuku KIA_ → `Observation.catgeory.coding` (687, tanpa BQ) |
| 51 | 688–698 | Observation | SP000122 | Catat di Buku KIA | – |
| 52 | 699–700 | MedicationDispense | – | – | _Diberikan Tablet FE_ → `MedicationDispense.status` (699, tanpa BQ) |
| 53 | 701–715 | Medication | – | – | – |
| 54 | 716–721 | MedicationRequest | – | – | – |
| 55 | 722–736 | Medication | – | – | – |
| 56 | 737–742 | MedicationDispense | – | – | – |
| 57 | 743–776 | MedicationRequest | 92000653.0 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula | _Jumlah Tablet Fe yang didapatkan_ → `MedicationRequest.contained.resourceType` (743, tanpa BQ) |
| 58 | 777–808 | MedicationDispense | 93015491.0 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | – |
| 59 | 809–819 | Procedure | 767224000.0 | Administration of vitamin A | _Pemberian Vitamin A_ → `Procedure.category.coding` (809, tanpa BQ)<br>_Catatan Pemberian Vit A_ → `Procedure.note` (819, tanpa BQ) |
| 60 | 820–846 | MedicationRequest | 92000809.0 | Retinol Palmitate 200.000 IU Kapsul Lunak | _Dosis Vitamin A_ → `MedicationRequest.contained.resourceType` (820, tanpa BQ) |
| 61 | 847–872 | MedicationDispense | 93018284.0 | Retinol Palmitate 200.000 IU Kapsul Lunak (Umum) | – |
| 62 | 873–883 | Procedure | 711029005.0 | Counseling about breastfeeding | _Konseling ASI_ → `Procedure.category.coding` (873, tanpa BQ) |
| 63 | 884–894 | Procedure | ED000008 | Edukasi Tanda Bahaya Kehamilan, Bersalin dan Nifas | _Tanda Bahaya Nifas_ → `Procedure.category.coding` (884, tanpa BQ) |
| 64 | 895–905 | Procedure | 72531000052105.0 | Counseling for contraception | _Konseling KB_ → `Procedure.category.coding` (895, tanpa BQ) |
| 65 | 906–916 | Procedure | SP000135 | Konseling Tanda Bahaya Bayi Baru Lahir | _Konseling Tanda Bahaya Bayi Baru Lahir_ → `Procedure.category.coding` (906, tanpa BQ) |
| 66 | 917–927 | Procedure | 441041000124100.0 | Counseling about nutrition | _Konseling Gizi_ → `Procedure.category.coding` (917, tanpa BQ) |
| 67 | 928–938 | Procedure | PC000001 | Perawatan Tali Pusat | _Konseling Perawatan Tali Pusar_ → `Procedure.category.coding` (928, tanpa BQ) |
| 68 | 939–949 | Procedure | ED000010 | Edukasi PHBS | _Konseling PHBS_ → `Procedure.category.coding` (939, tanpa BQ) |
| 69 | 950–960 | Procedure | ED000012 | Edukasi lainnya | _Konseling Jiwa Pascasalin_ → `Procedure.category.coding` (950, tanpa BQ) |
| 70 | 961–970 | ServiceRequest | – | – | _Tindak Lanjut CD4_ → `ServiceRequest.category` (961, tanpa BQ) |
| 71 | 971–973 | PractitionerRole | – | – | – |
| 72 | 974–981 | Specimen | – | – | – |
| 73 | 982–994 | Observation | 32515-9 | CD3+CD4+ (T4 helper) cells [#/volume] in Specimen | – |
| 74 | 995–1006 | DiagnosticReport | 32515-9 | CD3+CD4+ (T4 helper) cells [#/volume] in Specimen | – |
| 75 | 1007–1018 | Observation | SP000046 | Terapi Antiretroviral (ART) | _ART_ → `Observation.valueBoolean` (1010, tanpa BQ) |
| 76 | 1019–1039 | Observation | SP000124 | Obat anti malaria | _Obat Anti Malaria_ → `Observation.valueBoolean` (1022, tanpa BQ) |
| 77 | 1040–1063 | Observation | SP000125 | Obat anti tuberkulosis | _Obat Anti Tuberkulosis (OAT)_ → `Observation.valueBoolean` (1043, tanpa BQ) |
| 78 | 1064–1073 | ServiceRequest | – | – | _Foto Thorax_ → `ServiceRequest.category` (1064, tanpa BQ) |
| 79 | 1074–1077 | PractitionerRole | – | – | – |
| 80 | 1078–1090 | Observation | 24648-8 | XR Chest PA upright | – |
| 81 | 1091–1101 | DiagnosticReport | – | – | – |
| 82 | 1102–1119 | Observation | SP000139 | KB Pasca Plasenta | _Metode Kontrasepsi KB Pasca Plasenta_ → `Observation.valueCodeableConcept.coding` (1105, tanpa BQ) |
| 83 | 1120–1131 | Observation | SP000139 | KB Pasca Plasenta | _Pelaksanaan KB_ → `Observation.valueBoolean` (1123, tanpa BQ)<br>_Tanggal Pelaksanaan KB Plasenta_ → `Observation.effectiveDateTime` (1128, tanpa BQ) |
| 84 | 1132–1149 | Observation | PC000004 | KB Pasca Persalinan | _Metode Kontrasepsi KB Pasca Persalinan_ → `Observation.valueCodeableConcept.coding` (1135, tanpa BQ) |
| 85 | 1150–1161 | Observation | PC000004 | KB Pasca Persalinan | _Pelaksanaan KB Pasca Persalinan_ → `Observation.valueBoolean` (1153, tanpa BQ)<br>_Tanggal Pelaksanaan KB Pasca Persalinan_ → `Observation.effectiveDateTime` (1158, tanpa BQ) |
| 86 | 1162–1171 | CarePlan | – | – | _Rencana KB Pasca Persalinan_ → `CarePlan.status` (1162, tanpa BQ) |
| 87 | 1172–1191 | Observation | SP000380 | Tatalaksana Komplikasi Pendarahan | _Tatalaksana Komplikasi Pendarahan_ → `Observation.valueBoolean` (1175, tanpa BQ)<br>_Pemberian Tablet FE_ → `Observation.component.code.coding` (1177, tanpa BQ)<br>_Transfusi Darah_ → `Observation.component.code.coding` (1180, tanpa BQ)<br>_Lain-lain_ → `Observation.component.code.coding` (1183, tanpa BQ) |
| 88 | 1192–1211 | Observation | 736286003 | Hypertension clinical management plan | _Tatalaksana Komplikasi Hipertensi_ → `Observation.valueBoolean` (1195, tanpa BQ)<br>_Pantau Tekanan Darah_ → `Observation.component.code.coding` (1197, tanpa BQ)<br>_Pantau Protein Urin_ → `Observation.component.code.coding` (1200, tanpa BQ)<br>_Lain-lain_ → `Observation.component.code.coding` (1203, tanpa BQ) |
| 89 | 1212–1240 | Observation | SP000138 | Tatalaksana Komplikasi Pre Eklampsia | _Tatalaksana Komplikasi Pre Eklampsia dan Eklampsia_ → `Observation.valueBoolean` (1215, tanpa BQ)<br>_Pantau Tekanan Darah_ → `Observation.component.code.coding` (1217, tanpa BQ)<br>_Pantau Protein Urin_ → `Observation.component.code.coding` (1220, tanpa BQ)<br>_Lain-lain_ → `Observation.component.code.coding` (1223, tanpa BQ)<br>_Pemberian Anti Hipertensi_ → `Observation.component.code` (1224, tanpa BQ)<br>_Pemberian MgSO4_ → `Observation.component.code.coding` (1227, tanpa BQ)<br>_Pemberian Diazepam Injeksi_ → `Observation.component.code.coding` (1230, tanpa BQ)<br>_Lain-lain_ → `Observation.component.code.coding` (1233, tanpa BQ) |
| 90 | 1242–1259 | Observation | SP000389 | Keadaan Ibu | – |
| 91 | 1260–1268 | Condition | 359746009.0 | Patient’s condition stable | _Keadaan Pulang_ → `Condition.clinicalStatus.coding` (1260, tanpa BQ) |
| 92 | 1274–1294 | ServiceRequest | 409014006.0 | Delivery care management | _Apakah pasien dirujuk?_ → `ServiceRequest.performer.reference` (1285, tanpa BQ)<br>_Faskes Rujukan_ → `ServiceRequest.locationCode.coding` (1287, tanpa BQ)<br>_Nama Faskes Rujukan_ → `ServiceRequest.locationCode.text` (1294, tanpa BQ) |
| 93 | 1295–1356 | QuestionnaireResponse | – | – | _Tanggal_ → `QuestionnaireResponse.authored` (1300, tanpa BQ)<br>_Nama Kader/ Nakes_ → `QuestionnaireResponse.author.display` (1302, tanpa BQ) |
| 94 | 1357–1366 | Observation | 35025007.0 | Manual pelvic examination | _Periksa Jalan Lahir_ → `Observation.valueString` (1360, tanpa BQ) |
| 95 | 1371–1393 | Observation | 72150-6 | Delivery location | _Tempat Melahirkan_ → `Observation.valueCodeableConcept.coding` (1374, tanpa BQ)<br>_Alamat Bersalin_ → `Observation.note.text` (1393, tanpa BQ) |
| 96 | 1394–1406 | ServiceRequest | – | – | _Tanggal Kembali_ → `ServiceRequest.category` (1394, tanpa BQ)<br>_Saran_ → `ServiceRequest.patientInstruction` (1406, tanpa BQ) |
| 97 | 1407–1416 | Observation | SP000140 | Memberikan Nasihat PNC | _Memberikan nasihat yaitu: 1. Makan makanan yang beraneka ragam yang mengandung karbohidrat, protein hewani, protein nabati, sayur, dan buah-buahan. Sesuai 2. Kebutuhan air minum pada ibu menyusui pada 6 bulan pertama adalah 14 gelas sehari dan pada 6 bulan kedua adalah 12 gelas sehari 3. Menjaga kebersihan diri, termasuk kebersihan daerah kemaluan, ganti . Istirahat cukup, sat bay tidur ibu istirahat 5. Melakukan aktivitas fisik pasca melahirkan dengan intensitas ringan sampai sedang selama 30 menit, frekuensi 3 - 5 kali dalam seminggu 6. Bagi ibu yang melahirkan dengan cara operasi caesar maka harus menjaga kebersihan luka bekas operasi. Latihan fisik dapat dilakukan setelah 3 (tiga) bulan pasca melahirkan. 7. Cara menyusui yang benar dan hanya memberi ASI saja selama 6 bulan. 8. Perawatan bayi yang benar. 9. Jangan membiarkan bayi menangis terlalu lama, karena akan membuat bayi stres. 10. Lakukan stimulasi komunikasi dengan bayi sedini mungkin bersama suami dan keluarga 11. Untuk berkonsultasi kepada tenaga kesehatan untuk pelayanan KB setelah proses melahirkan._ → `Observation.valueBoolean` (1410, tanpa BQ) |
| 98 | 1417–1431 | ServiceRequest | – | – | _Tanggal_ → `ServiceRequest.occurrenceDateTime` (1424, tanpa BQ)<br>_Anjuran_ → `ServiceRequest.patientInstruction` (1429, tanpa BQ)<br>_Diagnosis Akhir_ → `ServiceRequest.reasonCode.coding` (1430, tanpa BQ)<br>_Resume hasil pemeriksaan dan tatalaksana di FKRTL:_ → `ServiceRequest.note` (1431, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 52 |
| Procedure | 10 |
| Condition | 8 |
| ServiceRequest | 5 |
| PractitionerRole | 4 |
| MedicationDispense | 4 |
| MedicationRequest | 3 |
| Practitioner | 2 |
| Medication | 2 |
| DiagnosticReport | 2 |
| Patient | 1 |
| EpisodeOfCare | 1 |
| Encounter | 1 |
| Specimen | 1 |
| CarePlan | 1 |
| QuestionnaireResponse | 1 |
| **Total** | **98** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 11 | Observation | `Observation.code.coding` | 424144002.0 | Current chronological age | http://snomed.info/sct |
| 2 | 111 | PractitionerRole | `PractitionerRole.code.coding` | 309453006.0 | Registered midwife | http://snomed.info/sct |
| 3 | 112 | PractitionerRole | `PractitionerRole.code.coding` | 309343006.0 | Physician | http://snomed.info/sct |
| 4 | 113 | PractitionerRole | `PractitionerRole.code.coding` | 309367003.0 | Obstetrician and gynecologist | http://snomed.info/sct |
| 5 | 114 | PractitionerRole | `PractitionerRole.code.coding` | 224535009.0 | Registered nurse | http://snomed.info/sct |
| 6 | 116 | PractitionerRole | `PractitionerRole.code.coding` | 223366009.0 | Healthcare professional | http://snomed.info/sct |
| 7 | 117 | PractitionerRole | `PractitionerRole.code.coding` | SP000396 | Data entry staff | http://terminology.kemkes.go.id/sp |
| 8 | 118 | PractitionerRole | `PractitionerRole.code.coding` | SP000397 | Field/call center staff | http://terminology.kemkes.go.id/sp |
| 9 | 126 | EpisodeOfCare | `EpisodeOfCare.type.coding` | PNC | Postnatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 10 | 152 | Condition | `Condition.code.coding` | Z39.2 | Routine postpartum follow-up | http://hl7.org/fhir/sid/icd-10 |
| 11 | 160 | Condition | `Condition.code.coding` | 404684003.0 | Clinical finding | http://snomed.info/sct |
| 12 | 161 | Condition | `Condition.code.coding` | 80313002.0 | Palpitations | http://snomed.info/sct |
| 13 | 162 | Condition | `Condition.code.coding` | 271939006.0 | Vaginal discharge | http://snomed.info/sct |
| 14 | 163 | Condition | `Condition.code.coding` | 267036007.0 | Dyspnea | http://snomed.info/sct |
| 15 | 164 | Condition | `Condition.code.coding` | 248858001.0 | Vulva finding | http://snomed.info/sct |
| 16 | 165 | Condition | `Condition.code.coding` | 274671002.0 | Pelvic and perineal pain | http://snomed.info/sct |
| 17 | 166 | Condition | `Condition.code.coding` | 47821001.0 | Postpartum hemorrhage | http://snomed.info/sct |
| 18 | 167 | Condition | `Condition.code.coding` | 289552002.0 | White vaginal discharge | http://snomed.info/sct |
| 19 | 168 | Condition | `Condition.code.coding` | 58703003.0 | Postpartum depression | http://snomed.info/sct |
| 20 | 169 | Condition | `Condition.code.coding` | 386661006.0 | Fever | http://snomed.info/sct |
| 21 | 170 | Condition | `Condition.code.coding` | 25064002.0 | Headache | http://snomed.info/sct |
| 22 | 171 | Condition | `Condition.code.coding` | 111516008.0 | Blurring of visual image | http://snomed.info/sct |
| 23 | 172 | Condition | `Condition.code.coding` | 79922009.0 | Epigastric pain | http://snomed.info/sct |
| 24 | 173 | Condition | `Condition.code.coding` | 118213005.0 | Postpartum finding | http://snomed.info/sct |
| 25 | 192 | Encounter | `Encounter.hospitalization.admitSource.coding` | EHA000002 | Datang sendiri | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 26 | 193 | Encounter | `Encounter.hospitalization.admitSource.coding` | 305956004.0 | Referral by physician | http://snomed.info/sct |
| 27 | 194 | Encounter | `Encounter.hospitalization.admitSource.coding` | 306052007.0 | Referral by midwife | http://snomed.info/sct |
| 28 | 195 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000116 | Rujukan dari Puskesmas Pembantu | http://terminology.kemkes.go.id/sp |
| 29 | 196 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000117 | Rujukan dari Puskesmas | http://terminology.kemkes.go.id/sp |
| 30 | 197 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000118 | Rujukan dari Rumah Bersalin / Klinik | http://terminology.kemkes.go.id/sp |
| 31 | 198 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000119 | Rujukan dari Rumah Sakit | http://terminology.kemkes.go.id/sp |
| 32 | 201 | Observation | `Observation.code.coding` | 93857-1 | Date and time of obstetric delivery | http://loinc.org |
| 33 | 212 | Observation | `Observation.code.coding` | 11996-6 | [#] Pregnancies | http://loinc.org |
| 34 | 223 | Observation | `Observation.code.coding` | 11977-6 | [#] Parity | http://loinc.org |
| 35 | 234 | Observation | `Observation.code.coding` | 69043-8 | Other pregnancy outcomes # | http://loinc.org |
| 36 | 256 | Observation | `Observation.code.coding` | SP000131 | Status Pindahan | http://terminology.kemkes.go.id/sp |
| 37 | 268 | Observation | `Observation.code.coding` | SP000134 | Jenis Lokasi Screening | http://terminology.kemkes.go.id/sp |
| 38 | 269 | Observation | `Observation.valueCodeableConcept.coding` | 264362003.0 | Home | http://snomed.info/sct |
| 39 | 270 | Observation | `Observation.valueCodeableConcept.coding` | OT000001 | Polindes | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 40 | 271 | Observation | `Observation.valueCodeableConcept.coding` | OT000002 | Pustu | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 41 | 272 | Observation | `Observation.valueCodeableConcept.coding` | 102.0 | Pusat Kesehatan Masyarakat | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 42 | 273 | Observation | `Observation.valueCodeableConcept.coding` | 103.0 | Klinik | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 43 | 274 | Observation | `Observation.valueCodeableConcept.coding` | OT000008 | Rumah Bersalin | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 44 | 275 | Observation | `Observation.valueCodeableConcept.coding` | 82242000.0 | Children’s hospital | http://snomed.info/sct |
| 45 | 276 | Observation | `Observation.valueCodeableConcept.coding` | 104.0 | Rumah Sakit | hhttp://terminology.kemkes.go.id/CodeSystem/organization-type |
| 46 | 277 | Observation | `Observation.valueCodeableConcept.coding` | OT000003 | RS ODHA | hhttp://terminology.kemkes.go.id/CodeSystem/organization-type |
| 47 | 278 | Observation | `Observation.valueCodeableConcept.coding` | OT000004 | Bidan Praktek Mandiri | hhttp://terminology.kemkes.go.id/CodeSystem/organization-type |
| 48 | 279 | Observation | `Observation.valueCodeableConcept.coding` | LT000008 | Dalam perjalanan dari rumah/masyarakat | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 49 | 290 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 50 | 302 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://loinc.org |
| 51 | 314 | Observation | `Observation.code.coding` | 8867-4 | Heart rate | http://loinc.org |
| 52 | 326 | Observation | `Observation.code.coding` | 8310-5 | Body temperature | http://loinc.org |
| 53 | 338 | Observation | `Observation.code.coding` | 9279-1 | Respiratory rate | http://loinc.org |
| 54 | 350 | Condition | `Condition.code.coding` | 289530006.0 | Vaginal bleeding | http://snomed.info/sct |
| 55 | 357 | Observation | `Observation.code.coding` | 81661-1 | Blood Loss [Volume] Measured | http://loinc.org |
| 56 | 369 | Observation | `Observation.code.coding` | 364297003.0 | Female perineum observable | http://loinc.org |
| 57 | 370 | Observation | `Observation.valueCodeableConcept.coding` | 289854007.0 | Perineum intact | http://snomed.info/sct |
| 58 | 371 | Observation | `Observation.valueCodeableConcept.coding` | 57759005.0 | First degree perineal laceration | http://snomed.info/sct |
| 59 | 372 | Observation | `Observation.valueCodeableConcept.coding` | 6234006.0 | Second degree perineal laceration | http://snomed.info/sct |
| 60 | 373 | Observation | `Observation.valueCodeableConcept.coding` | 10217006.0 | Third degree perineal laceration | http://snomed.info/sct |
| 61 | 374 | Observation | `Observation.valueCodeableConcept.coding` | 399031001.0 | Fourth degree perineal laceration | http://snomed.info/sct |
| 62 | 384 | Observation | `Observation.code.coding` | OC000020 | Tanda Infeksi Perineum | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 63 | 396 | Observation | `Observation.code.coding` | OC000025 | Tanda Infeksi Luka Jahitan Sectio Caesaria | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 64 | 408 | Observation | `Observation.code.coding` | 32422-8 | Physical findings of breast | http://loinc.org |
| 65 | 409 | Observation | `Observation.valueCodeableConcept.coding` | 300885006.0 | Swelling of breast | http://snomed.info/sct |
| 66 | 410 | Observation | `Observation.valueCodeableConcept.coding` | 290070001.0 | Red breast | http://snomed.info/sct |
| 67 | 411 | Observation | `Observation.valueCodeableConcept.coding` | 54302000.0 | Discharge from nipple | http://snomed.info/sct |
| 68 | 412 | Observation | `Observation.valueCodeableConcept.coding` | 53430007.0 | Pain of breast | http://snomed.info/sct |
| 69 | 413 | Observation | `Observation.valueCodeableConcept.coding` | 290084006.0 | Breast normal | http://snomed.info/sct |
| 70 | 423 | Observation | `Observation.code.coding` | 289700000.0 | Uterine contractions present | http://snomed.info/sct |
| 71 | 435 | Observation | `Observation.code.coding` | 249214003.0 | Color of lochia | http://snomed.info/sct |
| 72 | 436 | Observation | `Observation.valueCodeableConcept.coding` | 278072004.0 | Lochia rubra | http://snomed.info/sct |
| 73 | 437 | Observation | `Observation.valueCodeableConcept.coding` | 449828001.0 | Lochia serosa | http://snomed.info/sct |
| 74 | 438 | Observation | `Observation.valueCodeableConcept.coding` | 113291006.0 | Lochia sanguinolenta | http://snomed.info/sct |
| 75 | 439 | Observation | `Observation.valueCodeableConcept.coding` | 449827006.0 | Lochia alba | http://snomed.info/sct |
| 76 | 449 | Observation | `Observation.code.coding` | 249215002.0 | Odor of lochia | http://snomed.info/sct |
| 77 | 461 | Observation | `Observation.code.coding` | OC000017 | Produksi ASI | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 78 | 462 | Observation | `Observation.valueCodeableConcept.coding` | OV000016 | Produksi ASI ada | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 79 | 463 | Observation | `Observation.valueCodeableConcept.coding` | OV000017 | Produksi ASI ada tapi sedikit | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 80 | 464 | Observation | `Observation.valueCodeableConcept.coding` | OV000018 | Produksi ASI tidak ada | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 81 | 474 | Observation | `Observation.code.coding` | 1145307003.0 | Exclusively breastfed | http://snomed.info/sct |
| 82 | 486 | Observation | `Observation.code.coding` | 252041008.0 | Micturition finding | http://snomed.info/sct |
| 83 | 487 | Observation | `Observation.valueCodeableConcept.coding` | 49650001.0 | Dysuria | http://snomed.info/sct |
| 84 | 488 | Observation | `Observation.valueCodeableConcept.coding` | 249288007.0 | Incomplete emptying of urinary bladder | http://snomed.info/sct |
| 85 | 489 | Observation | `Observation.valueCodeableConcept.coding` | 162116003.0 | Increased frequency of urination | http://snomed.info/sct |
| 86 | 490 | Observation | `Observation.valueCodeableConcept.coding` | 42112009.0 | Enuresis | http://snomed.info/sct |
| 87 | 491 | Observation | `Observation.valueCodeableConcept.coding` | 102834005.0 | Normal micturition | http://snomed.info/sct |
| 88 | 492 | Observation | `Observation.valueCodeableConcept.coding` | 267064002.0 | Retention of urine | http://snomed.info/sct |
| 89 | 502 | Observation | `Observation.code.coding` | 300375001.0 | Able to defecate | http://snomed.info/sct |
| 90 | 513 | Procedure | `Procedure.code.coding` | 408988007.0 | Newborn care education | http://snomed.info/sct |
| 91 | 525 | Observation | `Observation.code.coding` | 8345-1 | Body weight Measured --post partum | http://loinc.org |
| 92 | 537 | Observation | `Observation.code.coding` | 8305-5 | Body height --post partum | http://loinc.org |
| 93 | 549 | Observation | `Observation.code.coding` | 284473002.0 | Mid upper arm circumference | http://snomed.info/sct |
| 94 | 558 | Observation | `Observation.interpretation` | OI000018 | Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 95 | 559 | Observation | `Observation.interpretation` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 96 | 562 | Observation | `Observation.code.coding` | 11881-0 | Uterus Fundal height Tape measure | http://loinc.org |
| 97 | 574 | Observation | `Observation.code.coding` | 67775-7 | Level of responsiveness | http://loinc.org |
| 98 | 575 | Observation | `Observation.valueCodeableConcept[i].coding` | 248234008.0 | Mentally alert | http://snomed.info/sct |
| 99 | 576 | Observation | `Observation.valueCodeableConcept[i].coding` | 20602000.0 | Apathy | http://snomed.info/sct |
| 100 | 577 | Observation | `Observation.valueCodeableConcept[i].coding` | 271782001.0 | Somnolence | http://snomed.info/sct |
| 101 | 578 | Observation | `Observation.valueCodeableConcept[i].coding` | LA25163-9 | Stuporous | http://loinc.org |
| 102 | 579 | Observation | `Observation.valueCodeableConcept[i].coding` | 371632003.0 | Coma | http://snomed.info/sct |
| 103 | 580 | Observation | `Observation.valueCodeableConcept[i].coding` | LA9343-0 | Unresponsive | http://loinc.org |
| 104 | 589 | Observation | `Observation.code.coding` | 112648003.0 | Massive hemorrhage | http://snomed.info/sct |
| 105 | 601 | Condition | `Condition.code.coding` | 112648003.0 | Massive hemorrhage | http://snomed.info/sct |
| 106 | 608 | Observation | `Observation.code.coding` | 91175000.0 | Seizure | http://snomed.info/sct |
| 107 | 620 | Condition | `Condition.code.coding` | 91175000.0 | Seizure | http://snomed.info/sct |
| 108 | 627 | Observation | `Observation.code.coding` | 27942005.0 | Shock | http://snomed.info/sct |
| 109 | 639 | Condition | `Condition.code.coding` | 27942005.0 | Shock | http://snomed.info/sct |
| 110 | 646 | Condition | `Condition.code.coding` | 47821001.0 | Postpartum hemorrhage | http://snomed.info/sct |
| 111 | 647 | Condition | `Condition.code.coding` | 198188007.0 | Chronic uterine inflammatory disease | http://snomed.info/sct |
| 112 | 648 | Condition | `Condition.code.coding` | 111367007.0 | Pelvic abscess | http://snomed.info/sct |
| 113 | 649 | Condition | `Condition.code.coding` | 211063003.0 | Infected abrasion of perineum | http://snomed.info/sct |
| 114 | 650 | Condition | `Condition.code.coding` | 76902006.0 | Tetanus | http://snomed.info/sct |
| 115 | 651 | Condition | `Condition.code.coding` | 266579006.0 | Inflammatory disorder of breast | http://snomed.info/sct |
| 116 | 652 | Condition | `Condition.code.coding` | 49746001.0 | Engorgement of breasts | http://snomed.info/sct |
| 117 | 653 | Condition | `Condition.code.coding` | 82231009.0 | Inversion of nipple | http://snomed.info/sct |
| 118 | 654 | Condition | `Condition.code.coding` | 58703003.0 | Postpartum depression | http://snomed.info/sct |
| 119 | 655 | Condition | `Condition.code.coding` | O13 | Gestational [pregnancy-induced] hypertension without signification proteinuria | http://hl7.org/fhir/sid/icd-10 |
| 120 | 656 | Condition | `Condition.code.coding` | O90.8 | Other complications of the puerperium, not elsewhere classified | http://hl7.org/fhir/sid/icd-10 |
| 121 | 664 | Observation | `Observation.code.coding` | 289084000.0 | Difficulty performing breastfeeding | http://snomed.info/sct |
| 122 | 677 | Observation | `Observation.code.coding` | 871562009.0 | Detection of severe acute respiratory syndrome coronavirus 2 | http://snomed.info/sct |
| 123 | 688 | Observation | `Observation.code.coding` | SP000122 | Catat di Buku KIA | http://terminology.kemkes.go.id/sp |
| 124 | 702 | Medication | `Medication.code` | 92000653.0 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula | http://sys-ids.kemkes.go.id/kf |
| 125 | 723 | Medication | `Medication.code` | 93015491.0 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | http://sys-ids.kemkes.go.id/kf |
| 126 | 746 | MedicationRequest | `MedicationRequest.contained.code.coding` | 92000653.0 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula | http://sys-ids.kemkes.go.id/kf |
| 127 | 780 | MedicationDispense | `MedicationDispense.contained.code.coding` | 93015491.0 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | http://sys-ids.kemkes.go.id/kf |
| 128 | 810 | Procedure | `Procedure.code.coding` | 767224000.0 | Administration of vitamin A | http://snomed.info/sct |
| 129 | 823 | MedicationRequest | `MedicationRequest.contained.code.coding` | 92000809.0 | Retinol Palmitate 200.000 IU Kapsul Lunak | http://sys-ids.kemkes.go.id/kf |
| 130 | 850 | MedicationDispense | `MedicationDispense.contained.code.coding` | 93018284.0 | Retinol Palmitate 200.000 IU Kapsul Lunak (Umum) | http://sys-ids.kemkes.go.id/kf |
| 131 | 874 | Procedure | `Procedure.code.coding` | 711029005.0 | Counseling about breastfeeding | http://snomed.info/sct |
| 132 | 885 | Procedure | `Procedure.code.coding` | ED000008 | Edukasi Tanda Bahaya Kehamilan, Bersalin dan Nifas | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 133 | 896 | Procedure | `Procedure.code.coding` | 72531000052105.0 | Counseling for contraception | http://snomed.info/sct |
| 134 | 907 | Procedure | `Procedure.code.coding` | SP000135 | Konseling Tanda Bahaya Bayi Baru Lahir | http://terminology.kemkes.go.id/sp |
| 135 | 918 | Procedure | `Procedure.code.coding` | 441041000124100.0 | Counseling about nutrition | http://snomed.info/sct |
| 136 | 929 | Procedure | `Procedure.code.coding` | PC000001 | Perawatan Tali Pusat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 137 | 940 | Procedure | `Procedure.code.coding` | ED000010 | Edukasi PHBS | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 138 | 951 | Procedure | `Procedure.code.coding` | ED000012 | Edukasi lainnya | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 139 | 965 | ServiceRequest | `ServiceRequest.code` | 32515-9 | CD3+CD4+ (T4 helper) cells [#/volume] in Specimen | http://loinc.org |
| 140 | 972 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002.0 | Laboratory worker | http://snomed.info/sct |
| 141 | 975 | Specimen | `Specimen.type` | 119297000.0 | Blood specimen | http://snomed.info/sct |
| 142 | 984 | Observation | `Observation.code.coding` | 32515-9 | CD3+CD4+ (T4 helper) cells [#/volume] in Specimen | http://loinc.org |
| 143 | 997 | DiagnosticReport | `DiagnosticReport.code.coding` | 32515-9 | CD3+CD4+ (T4 helper) cells [#/volume] in Specimen | http://loinc.org |
| 144 | 1009 | Observation | `Observation.code.coding` | SP000046 | Terapi Antiretroviral (ART) | http://terminology.kemkes.go.id/sp |
| 145 | 1021 | Observation | `Observation.code.coding` | SP000124 | Obat anti malaria | http://terminology.kemkes.go.id/sp |
| 146 | 1024 | Observation | `Observation.component.code.coding` | 432555000.0 | Product containing artesunate | http://snomed.info/sct |
| 147 | 1027 | Observation | `Observation.component.code.coding` | 64115004.0 | Product containing amodiaquine | http://snomed.info/sct |
| 148 | 1030 | Observation | `Observation.component.code.coding` | 324919005.0 | Product containing precisely quinine sulfate 200 milligram/1 each conventional release oral tablet | http://snomed.info/sct |
| 149 | 1042 | Observation | `Observation.code.coding` | SP000125 | Obat anti tuberkulosis | http://terminology.kemkes.go.id/sp |
| 150 | 1045 | Observation | `Observation.component.code.coding` | 29175007.0 | Product containing rifampicin | http://snomed.info/sct |
| 151 | 1048 | Observation | `Observation.component.code.coding` | 81335000.0 | Product containing isoniazid | http://snomed.info/sct |
| 152 | 1051 | Observation | `Observation.component.code.coding` | 13592004.0 | Product containing pyrazinamide | http://snomed.info/sct |
| 153 | 1054 | Observation | `Observation.component.code.coding` | 24450004.0 | Product containing ethambutol | http://snomed.info/sct |
| 154 | 1068 | ServiceRequest | `ServiceRequest.code` | 24648-8 | XR Chest PA upright | http://loinc.org |
| 155 | 1076 | PractitionerRole | `PractitionerRole.code.coding` | 159016003.0 | Medical radiographer | http://snomed.info/sct |
| 156 | 1080 | Observation | `Observation.code.coding` | 24648-8 | XR Chest PA upright | http://loinc.org |
| 157 | 1081 | Observation | `Observation.valueCodeableConcept.coding` | 707307002.0 | Tuberculosis screening chest X-ray abnormal | http://snomed.info/sct |
| 158 | 1082 | Observation | `Observation.valueCodeableConcept.coding` | 707308007.0 | Tuberculosis screening chest X-ray normal | http://snomed.info/sct |
| 159 | 1093 | DiagnosticReport | `DiagnosticReport.code` | 24648-8 | XR Chest PA upright | http://loinc.org |
| 160 | 1104 | Observation | `Observation.code.coding` | SP000139 | KB Pasca Plasenta | http://terminology.kemkes.go.id/sp |
| 161 | 1105 | Observation | `Observation.valueCodeableConcept.coding` | LA6524-8 | Oral contraceptive pill | http://loinc.org |
| 162 | 1106 | Observation | `Observation.valueCodeableConcept.coding` | 237122005.0 | Lactational amenorrhea | http://snomed.info/sct |
| 163 | 1107 | Observation | `Observation.valueCodeableConcept.coding` | LA6525-5 | Injectable/implantable hormone | http://loinc.org |
| 164 | 1108 | Observation | `Observation.valueCodeableConcept.coding` | LA6527-1 | Intrauterine device | http://loinc.org |
| 165 | 1109 | Observation | `Observation.valueCodeableConcept.coding` | SP000097 | Implan | http://terminology.kemkes.go.id/sp |
| 166 | 1110 | Observation | `Observation.valueCodeableConcept.coding` | LA6523-0 | Condom | http://loinc.org |
| 167 | 1111 | Observation | `Observation.valueCodeableConcept.coding` | 22523008.0 | Vasectomy | http://snomed.info/sct |
| 168 | 1112 | Observation | `Observation.valueCodeableConcept.coding` | 77543007.0 | Ligation of fallopian tube | http://snomed.info/sct |
| 169 | 1122 | Observation | `Observation.code.coding` | SP000139 | KB Pasca Plasenta | http://terminology.kemkes.go.id/sp |
| 170 | 1134 | Observation | `Observation.code.coding` | PC000004 | KB Pasca Persalinan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 171 | 1135 | Observation | `Observation.valueCodeableConcept.coding` | LA6524-8 | Oral contraceptive pill | http://loinc.org |
| 172 | 1136 | Observation | `Observation.valueCodeableConcept.coding` | 237122005.0 | Lactational amenorrhea | http://snomed.info/sct |
| 173 | 1137 | Observation | `Observation.valueCodeableConcept.coding` | LA6525-5 | Injectable/implantable hormone | http://loinc.org |
| 174 | 1138 | Observation | `Observation.valueCodeableConcept.coding` | LA6527-1 | Intrauterine device | http://loinc.org |
| 175 | 1139 | Observation | `Observation.valueCodeableConcept.coding` | SP000097 | Implan | http://terminology.kemkes.go.id/sp |
| 176 | 1140 | Observation | `Observation.valueCodeableConcept.coding` | LA6523-0 | Condom | http://loinc.org |
| 177 | 1141 | Observation | `Observation.valueCodeableConcept.coding` | 22523008.0 | Vasectomy | http://snomed.info/sct |
| 178 | 1142 | Observation | `Observation.valueCodeableConcept.coding` | 77543007.0 | Ligation of fallopian tube | http://snomed.info/sct |
| 179 | 1152 | Observation | `Observation.code.coding` | PC000004 | KB Pasca Persalinan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 180 | 1174 | Observation | `Observation.code.coding` | SP000380 | Tatalaksana Komplikasi Pendarahan | http://terminology.kemkes.go.id/sp |
| 181 | 1177 | Observation | `Observation.component.code.coding` | SP000008 | Pemberian Tablet Tambah Darah | http://terminology.kemkes.go.id/sp |
| 182 | 1180 | Observation | `Observation.component.code.coding` | 116859006.0 | Transfusion of blood product | http://snomed.info/sct |
| 183 | 1183 | Observation | `Observation.component.code.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 184 | 1194 | Observation | `Observation.code.coding` | 736286003 | Hypertension clinical management plan | http://snomed.info/sct |
| 185 | 1197 | Observation | `Observation.component.code.coding` | 135840009.0 | Blood pressure monitoring | http://snomed.info/sct |
| 186 | 1200 | Observation | `Observation.component.code.coding` | SP000133 | Pemantauan Protein Urin | http://terminology.kemkes.go.id/sp |
| 187 | 1203 | Observation | `Observation.component.code.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 188 | 1214 | Observation | `Observation.code.coding` | SP000138 | Tatalaksana Komplikasi Pre Eklampsia | http://terminology.kemkes.go.id/sp |
| 189 | 1217 | Observation | `Observation.component.code.coding` | 135840009.0 | Blood pressure monitoring | http://terminology.kemkes.go.id/sp |
| 190 | 1220 | Observation | `Observation.component.code.coding` | SP000133 | Pemantauan Protein Urin | http://terminology.kemkes.go.id/sp |
| 191 | 1223 | Observation | `Observation.component.code.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 192 | 1224 | Observation | `Observation.component.code` | 308116003.0 | Antihypertensive therapy | http://snomed.info/sct |
| 193 | 1227 | Observation | `Observation.component.code.coding` | SP000136 | Pemberian MgSO4 | http://terminology.kemkes.go.id/sp |
| 194 | 1230 | Observation | `Observation.component.code.coding` | SP000137 | Pemberian Diazepam Injeksi | http://terminology.kemkes.go.id/sp |
| 195 | 1233 | Observation | `Observation.component.code.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 196 | 1244 | Observation | `Observation.code.coding` | SP000389 | Keadaan Ibu | http://terminology.kemkes.go.id/sp |
| 197 | 1245 | Observation | `Observation.valueCodeableConcept.coding` | LA6112-2 | 1.0 | http://loinc.org |
| 198 | 1246 | Observation | `Observation.valueCodeableConcept.coding` | LA6113-0 | 2.0 | http://loinc.org |
| 199 | 1247 | Observation | `Observation.valueCodeableConcept.coding` | LA6114-8 | 3.0 | http://loinc.org |
| 200 | 1248 | Observation | `Observation.valueCodeableConcept.coding` | LA6115-5 | 4.0 | http://loinc.org |
| 201 | 1249 | Observation | `Observation.valueCodeableConcept.coding` | LA10137-0 | 5.0 | http://loinc.org |
| 202 | 1250 | Observation | `Observation.valueCodeableConcept.coding` | 63238001.0 | Dead on arrival at hospital | http://snomed.info/sct |
| 203 | 1251 | Observation | `Observation.valueCodeableConcept.coding` | 438949009.0 | Alive | http://snomed.info/sct |
| 204 | 1252 | Observation | `Observation.valueCodeableConcept.coding` | 419099009.0 | Dead | http://snomed.info/sct |
| 205 | 1262 | Condition | `Condition.code.coding` | 359746009.0 | Patient’s condition stable | http://snomed.info/sct |
| 206 | 1263 | Condition | `Condition.code.coding` | 162668006.0 | Patient’s condition unstable | http://snomed.info/sct |
| 207 | 1264 | Condition | `Condition.code.coding` | 268910001.0 | Patient’s condition improved | http://snomed.info/sct |
| 208 | 1278 | ServiceRequest | `ServiceRequest.code.coding` | 409014006.0 | Delivery care management | http://snomed.info/sct |
| 209 | 1359 | Observation | `Observation.code.coding` | 35025007.0 | Manual pelvic examination | http://snomed.info/sct |
| 210 | 1373 | Observation | `Observation.code.coding` | 72150-6 | Delivery location | http://loinc.org |
| 211 | 1374 | Observation | `Observation.valueCodeableConcept.coding` | 264362003.0 | Home | http://snomed.info/sct |
| 212 | 1375 | Observation | `Observation.valueCodeableConcept.coding` | OT000001 | Polindes | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 213 | 1376 | Observation | `Observation.valueCodeableConcept.coding` | OT000002 | Pustu | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 214 | 1377 | Observation | `Observation.valueCodeableConcept.coding` | 102.0 | Pusat Kesehatan Masyarakat | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 215 | 1378 | Observation | `Observation.valueCodeableConcept.coding` | 103.0 | Klinik | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 216 | 1379 | Observation | `Observation.valueCodeableConcept.coding` | OT000008 | Rumah Bersalin | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 217 | 1380 | Observation | `Observation.valueCodeableConcept.coding` | 82242000.0 | Children’s hospital | http://snomed.info/sct |
| 218 | 1381 | Observation | `Observation.valueCodeableConcept.coding` | 104.0 | Rumah Sakit | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 219 | 1382 | Observation | `Observation.valueCodeableConcept.coding` | OT000004 | Bidan Praktek Mandiri | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 220 | 1383 | Observation | `Observation.valueCodeableConcept.coding` | LT000008 | Dalam perjalanan dari rumah/masyarakat | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 221 | 1384 | Observation | `Observation.valueCodeableConcept.coding` | LT000009 | Dalam perjalanan ke faskes lain | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 222 | 1385 | Observation | `Observation.valueCodeableConcept.coding` | LT000007 | Rumah Dukun | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 223 | 1398 | ServiceRequest | `ServiceRequest.code` | 185389009.0 | Follow-up visit | http://snomed.info/sct |
| 224 | 1409 | Observation | `Observation.code.coding` | SP000140 | Memberikan Nasihat PNC | http://terminology.kemkes.go.id/sp |
| 225 | 1421 | ServiceRequest | `ServiceRequest.code` | 185389009.0 | Follow-up visit | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 116 |
| http://loinc.org | 38 |
| http://terminology.kemkes.go.id/sp | 27 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 14 |
| http://terminology.kemkes.go.id/CodeSystem/organization-type | 12 |
| http://sys-ids.kemkes.go.id/kf | 6 |
| http://terminology.kemkes.go.id/CodeSystem/location-type | 4 |
| http://hl7.org/fhir/sid/icd-10 | 3 |
| hhttp://terminology.kemkes.go.id/CodeSystem/organization-type | 3 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 1 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 1 |
| **Total** | **225** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 42 | – | Jenis Faskes | Organization | `Organization.type` |
| 46 | – | Nama Faskes | Organization | `Organization.name` |
| 1241 | – | Keadaan Ibu | – | `` |
| 1367 | – | Keadaan Bayi | – | `` |
