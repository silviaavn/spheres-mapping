# Output Form: SIM RS Nirmala BBL

Sumber: `mapping/phdt-data-dictionary-rs-nirmala-bbl.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-rs-nirmala-bbl.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 82 |
| Code (`jumlah code` = 1) | 126 |
| Code unik (code + CodeSystem) | 105 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 2 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–32 | Patient | – | – | _Nama Bayi_ → `Patient.name.text` (2, tanpa BQ)<br>_NIK Bayi/ Ibu_ → `Patient.identifier.value` (6, tanpa BQ)<br>_NIK Ibu_ → `Patient.identifier.value` (9, tanpa BQ)<br>_No HP Orang Tua_ → `Patient.telecom` (10, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (13, tanpa BQ)<br>_Tempat Lahir_ → `Patient.extension.valueAddress.city` (15, tanpa BQ)<br>_Kembar_ → `Patient.multipleBirthBoolean` (16, tanpa BQ)<br>_Alamat Domisili_ → `Patient.address.line` (18, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (23, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (26, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.extension.valueCode` (29, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.extension.valueCode` (32, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (524, tanpa BQ)<br>_Domisili_ → `Patient.address.line` (942, tanpa BQ) |
| 2 | 33–39 | RelatedPerson | – | – | _Nama Ibu_ → `RelatedPerson.name.text` (33, tanpa BQ)<br>_NIK Ibu_ → `RelatedPerson.identifier` (34, tanpa BQ) |
| 3 | 40–46 | RelatedPerson | – | – | _Nama Ayah_ → `RelatedPerson.name.text` (40, tanpa BQ)<br>_NIK Ayah_ → `RelatedPerson.identifier` (41, tanpa BQ) |
| 4 | 85–91 | Practitioner | – | – | _NIK_ → `Practitioner.identifier.value` (87, tanpa BQ)<br>_Nama Tenaga Kesehatan_ → `Practitioner.name.text` (89, tanpa BQ)<br>_Jenis Kelamin Tenaga Kesehatan_ → `Practitioner.gender` (90, tanpa BQ) |
| 5 | 92–100 | PractitionerRole | – | – | _Tenaga Pemeriksa_ → `PractitionerRole.code.coding` (96, tanpa BQ) |
| 6 | 102–117 | Encounter | – | – | _Kunjungan Neonatus_ → `Encounter.identifier` (103, tanpa BQ)<br>_Tanggal INC (Bersalin)_ → `Encounter.period.start` (112, tanpa BQ)<br>_Tempat Pelayanan INC_ → `Encounter.location.location.display` (115, tanpa BQ)<br>_Kondisi Saat Pulang_ → `Encounter.hospitalization.dischargeDisposition.coding` (692, tanpa BQ) |
| 7 | 118–125 | Condition | Z00.1 | Routine child health examination | _Tanggal Diagnosis_ → `Condition.recordedDate` (124, tanpa BQ) |
| 8 | 136–144 | EpisodeOfCare | Neonate | Neonate | – |
| 9 | 145–155 | Observation | 365475008.0 | Place in family order | _Anak ke_ → `Observation.valueInteger` (148, tanpa BQ) |
| 10 | 156–166 | Observation | 57715-5 | Birth time | _Jam Lahir_ → `Observation.valueTime` (159, tanpa BQ) |
| 11 | 168–208 | Observation | 76516-4 | Gestational age—​at birth | _Usia Gestasi Saat Lahir_ → `Observation.valueQuantity.value` (171, tanpa BQ)<br>_Golongan darah_ → `Observation` (183, tanpa BQ)<br>_Rhesus_ → `Observation` (197, tanpa BQ) |
| 12 | 209–220 | Observation | 8339-4 | Birth weight Measured | _Berat Badan Saat Lahir (gram)_ → `Observation.valueQuantity.value` (212, tanpa BQ) |
| 13 | 221–232 | Observation | 89269-5 | Body height Measured --at birth | _Panjang Badan Saat Lahir_ → `Observation.valueQuantity.value` (224, tanpa BQ) |
| 14 | 233–244 | Observation | 8290-9 | Head Occipital-frontal circumference --at birth- by Tape measure | _Lingkar Kepala Saat Lahir_ → `Observation.valueQuantity.value` (236, tanpa BQ) |
| 15 | 245–269 | Observation | 9272-6 | 1 minute Apgar Score | _APGAR menit ke-1_ → `Observation.valueRange.low.value` (250, tanpa BQ) |
| 16 | 270–294 | Observation | 9274-2 | 5 minute Apgar Score | _APGAR menit ke-5_ → `Observation.valueRange.low.value` (275, tanpa BQ) |
| 17 | 295–319 | Observation | 9271-8 | 10 minute Apgar Score | _APGAR menit ke-10_ → `Observation.valueRange.low.value` (300, tanpa BQ) |
| 18 | 320–342 | Observation | 276654001.0 | Congenital malformation | _Kelainan Bawaan_ → `Observation.valueString` (323, tanpa BQ) |
| 19 | 343–354 | Observation | 8867-4 | Heart rate | _Frekuensi Denyut Jantung_ → `Observation.valueQuantity.value` (346, tanpa BQ) |
| 20 | 355–365 | Observation | 8310-5 | Body temperature | _Suhu_ → `Observation.valueQuantity.value` (358, tanpa BQ) |
| 21 | 366–376 | Observation | 9279-1 | Respiratory rate | _Pernapasan_ → `Observation.valueQuantity.value` (369, tanpa BQ) |
| 22 | 377–387 | Procedure | 386412000.0 | Resuscitation of neonate | _Apakah Diberikan Resusitasi_ → `Procedure.category.coding` (377, tanpa BQ) |
| 23 | 388–398 | Procedure | PC000003 | Manajemen Terpadu Bayi Muda (MTBM) | _Apakah dilakukan pemeriksaan kesehatan dengan pendekatan MTBM_ → `Procedure.category.coding` (388, tanpa BQ) |
| 24 | 399–409 | Procedure | SP000126 | ARV Profilaksis | _ARV Profilaksis pada bayi baru lahir_ → `Procedure.category.coding` (399, tanpa BQ) |
| 25 | 410–420 | Procedure | 448883004.0 | Injection of vitamin K1 | _Apakah diberikan vitamin K_ → `Procedure.category.coding` (410, tanpa BQ) |
| 26 | 421–431 | Procedure | PC000001 | Perawatan Tali Pusat | _Perawatan Tali Pusat_ → `Procedure.category.coding` (421, tanpa BQ) |
| 27 | 432–442 | Procedure | PC000002 | Pemberian Salep Antibiotik Mata | _Salep Antibiotik Mata_ → `Procedure.category.coding` (432, tanpa BQ) |
| 28 | 443–469 | Immunization | – | – | _Imunisasi Hepatitis B (HB0)_ → `Immunization.status` (443, tanpa BQ)<br>_Jika Tidak Imunisasi Hepatitis B(HB0)_ → `Immunization.statusReason.coding` (460, tanpa BQ)<br>_Hepatitis B Immunoglobulin (HBIG)_ → `Immunization.status` (467, tanpa BQ) |
| 29 | 470–490 | Immunization | – | – | – |
| 30 | 491–501 | Procedure | 431868002.0 | Initiation of breastfeeding | _Inisiasi Menyusu Dini (IMD)_ → `Procedure.category.coding` (491, tanpa BQ) |
| 31 | 502–513 | Observation | OC000016 | Waktu Inisiasi Menyusui Dini | _Waktu Inisiasi Menyusu Dini (IMD)_ → `Observation.valueCodeableConcept.coding` (505, tanpa BQ) |
| 32 | 514–523 | Observation | 424144002.0 | Current chronological age | _Usia Neonatus_ → `Observation.valueQuantity.value` (516, tanpa BQ) |
| 33 | 526–536 | Observation | 424144002.0 | Current chronological age | _Usia Ibu_ → `Observation.valueQuantity.value` (528, tanpa BQ) |
| 34 | 537–547 | Observation | 57071-3 | Obstetric delivery method | _Metode Persalinan_ → `Observation.valueCodeableConcept.coding` (539, tanpa BQ) |
| 35 | 548–557 | Observation | 12729009.0 | Prolonged rupture of membranes | _Pecah Ketuban > 18 Jam_ → `Observation.valueBoolean` (550, tanpa BQ) |
| 36 | 558–567 | Observation | 168092006.0 | Amniotic fluid -meconium stain | _Air Ketuban Bercampur Mekonium_ → `Observation.valueBoolean` (560, tanpa BQ) |
| 37 | 568–577 | Observation | 130955003.0 | Fetal distress | _Gawat Janin Intrauterin_ → `Observation.valueBoolean` (570, tanpa BQ) |
| 38 | 578–587 | Observation | 415105001.0 | Placental abruption | _Solusio Plasenta_ → `Observation.valueBoolean` (580, tanpa BQ) |
| 39 | 588–599 | Observation | 206376005.0 | Neonatal sepsis | _Onset Sepsis_ → `Observation.valueCodeableConcept.coding` (590, tanpa BQ) |
| 40 | 600–610 | Observation | OC000126 | Klasifikasi infeksi | _Klasifikasi Infeksi_ → `Observation.valueCodeableConcept.coding` (602, tanpa BQ) |
| 41 | 611–620 | Observation | 392230005.0 | Catheterization of vein | _Penggunaan Kateter Vena_ → `Observation.valueBoolean` (613, tanpa BQ) |
| 42 | 621–630 | Observation | 40617009.0 | Artificial ventilation | _Penggunaan Alat Bantu Napas_ → `Observation.valueBoolean` (623, tanpa BQ) |
| 43 | 631–640 | Observation | 281789004.0 | Antibiotic therapy | _Paparan Antibiotik_ → `Observation.valueBoolean` (633, tanpa BQ) |
| 44 | 641–657 | Observation | 305351004.0 | Admission to intensive care unit | _Status Admisi ke ICU_ → `Observation.component.valueCodeableConcept.coding` (644, tanpa BQ)<br>_Lama Perawatan di ICU_ → `Observation.component.code.coding` (649, tanpa BQ) |
| 45 | 658–667 | Observation | 183797002.0 | Duration of inpatient stay | _Lama Rawat Inap di RS_ → `Observation.valueQuantity.value` (660, tanpa BQ) |
| 46 | 668–675 | Condition | Z00.1 | Routine child health examination | _Outcome Klinis_ → `Condition.code.coding` (668, tanpa BQ) |
| 47 | 676–683 | Condition | Z00.1 | Routine child health examination | _Diagnosis Utama (dx_1)_ → `Condition.code.coding` (676, tanpa BQ) |
| 48 | 684–691 | Condition | Z00.1 | Routine child health examination | _Diagnosis Sekunder (dx_2)_ → `Condition.code.coding` (684, tanpa BQ) |
| 49 | 696–705 | Observation | 8480-6 | Systolic blood pressure | _Tekanan Darah Sistolik_ → `Observation.valueQuantity.value` (698, tanpa BQ) |
| 50 | 706–715 | Observation | 8462-4 | Diastolic blood pressure | _Tekanan Darah Diastolik_ → `Observation.valueQuantity.value` (708, tanpa BQ) |
| 51 | 716–725 | Observation | 1023001.0 | Apnea | _Apnea_ → `Observation.valueBoolean` (718, tanpa BQ) |
| 52 | 726–735 | Observation | 67909005.0 | Chest wall retraction | _Tarikan Dinding Dada_ → `Observation.valueBoolean` (728, tanpa BQ) |
| 53 | 736–745 | Observation | 248568003.0 | Nasal flaring | _Pelebaran Cuping Hidung_ → `Observation.valueBoolean` (738, tanpa BQ) |
| 54 | 746–755 | Observation | 62085005.0 | Grunting respiration | _Suara Merintih_ → `Observation.valueBoolean` (748, tanpa BQ) |
| 55 | 756–765 | Observation | 3415004.0 | Cyanosis | _Kulit Tampak Kebiruan_ → `Observation.valueBoolean` (758, tanpa BQ) |
| 56 | 766–775 | Observation | 91175000.0 | Seizure | _Kejang_ → `Observation.valueBoolean` (768, tanpa BQ) |
| 57 | 776–785 | Observation | 214264003.0 | Lethargy | _Tubuh Lemas_ → `Observation.valueBoolean` (778, tanpa BQ) |
| 58 | 786–795 | Observation | 247905005.0 | Lack of spontaneous movement | _Penurunan Gerakan Normal_ → `Observation.valueBoolean` (788, tanpa BQ) |
| 59 | 796–805 | Observation | 835279003.0 | Decreased reflex | _Refleks Lemah_ → `Observation.valueBoolean` (798, tanpa BQ) |
| 60 | 806–815 | Observation | 95631006.0 | Neonatal drowsiness | _Sulit Dibangunkan_ → `Observation.valueBoolean` (808, tanpa BQ) |
| 61 | 816–825 | Observation | 103019006.0 | Bulging fontanelle | _Ubun-Ubun Menonjol_ → `Observation.valueBoolean` (818, tanpa BQ) |
| 62 | 826–835 | Observation | 65668001.0 | Otorrhea | _Keluar Nanah dari Telinga_ → `Observation.valueBoolean` (828, tanpa BQ) |
| 63 | 836–845 | Observation | 239095007.0 | Omphalitis | _Kemerahan pada Umbilikus_ → `Observation.valueBoolean` (838, tanpa BQ) |
| 64 | 846–855 | Observation | 271760008.0 | Pustule | _Pustula Kulit_ → `Observation.valueBoolean` (848, tanpa BQ) |
| 65 | 856–865 | Observation | 18165001.0 | Jaundice | _Ikterus_ → `Observation.valueBoolean` (858, tanpa BQ) |
| 66 | 866–877 | Observation | 364826005.0 | Finding related to ability to perform breastfeeding | _Gangguan Menyusu_ → `Observation.valueCodeableConcept.coding` (868, tanpa BQ) |
| 67 | 878–888 | Observation | 26464-8 | Leukocytes [#/volume] in Blood | _Jumlah Leukosit_ → `Observation.valueQuantity.value` (880, tanpa BQ)<br>_Dilakukan Tes Jumlah Leukosit_ → `Observation.dataAbsentReason.coding` (882, tanpa BQ) |
| 68 | 889–899 | Observation | 26515-7 | Platelets [#/volume] in Blood | _Jumlah Trombosit_ → `Observation.valueQuantity.value` (891, tanpa BQ)<br>_Dilakukan Tes Jumlah Trombosit_ → `Observation.dataAbsentReason.coding` (893, tanpa BQ) |
| 69 | 900–910 | Observation | 26499-4 | Neutrophils [#/volume] in Blood | _Jumlah Neutrofil Absolut_ → `Observation.valueQuantity.value` (902, tanpa BQ)<br>_Dilakukan Tes Jumlah Neutrofil Absolut_ → `Observation.dataAbsentReason.coding` (904, tanpa BQ) |
| 70 | 911–921 | Observation | 30341-2 | Erythrocyte [Sedimentation Rate] in Blood | _Erythrocyte Sedimentation Rate (ESR)_ → `Observation.valueQuantity.value` (913, tanpa BQ)<br>_Dilakukan Tes Erythrocyte Sedimentation Rate (ESR)_ → `Observation.dataAbsentReason.coding` (915, tanpa BQ) |
| 71 | 922–931 | Observation | 33959-8 | Procalcitonin [Mass/volume] in Serum or Plasma | _Kadar Prokalsitonin_ → `Observation.valueQuantity.value` (924, tanpa BQ) |
| 72 | 932–941 | Observation | 1988-5 | C reactive protein [Mass/volume] in Serum or Plasma | _C-Reactive Protein_ → `Observation.valueQuantity.value` (934, tanpa BQ) |
| 73 | 943–952 | Observation | 76516-4 | Gestational age--at birth | _Usia Gestasi_ → `Observation.valueQuantity.value` (945, tanpa BQ) |
| 74 | 953–962 | Observation | 89269-5 | Body height Measured --at birth | _Panjang Badan Lahir_ → `Observation.valueQuantity.value` (955, tanpa BQ) |
| 75 | 963–972 | Observation | 8339-4 | Birth weight Measured | _Berat Badan Lahir_ → `Observation.valueQuantity.value` (965, tanpa BQ) |
| 76 | 973–980 | Observation | 9274-2 | 5 minute Apgar Score | _Skor APGAR Menit ke-5_ → `Observation.code.coding` (973, tanpa BQ) |
| 77 | 981–990 | Observation | 8867-4 | Heart rate | _Frekuensi Nadi_ → `Observation.valueQuantity.value` (983, tanpa BQ) |
| 78 | 991–1000 | Observation | 9279-1 | Respiratory rate | _Laju Pernapasan_ → `Observation.valueQuantity.value` (993, tanpa BQ) |
| 79 | 1001–1010 | Observation | 8310-5 | Body temperature | _Suhu Tubuh_ → `Observation.valueQuantity.value` (1003, tanpa BQ) |
| 80 | 1011–1020 | Observation | 11337-3 | History of Hospitalization | _Riwayat Rawat Inap Min. 1 Malam dalam 3 Bulan_ → `Observation.valueBoolean` (1013, tanpa BQ) |
| 81 | 1021–1030 | Observation | 11347-2 | History of Outpatient visits | _Riwayat Kunjungan Faskes dalam 3 Bulan_ → `Observation.valueBoolean` (1023, tanpa BQ) |
| 82 | 1031–1040 | Observation | 8690-0 | History of Surgical procedures | _Riwayat Tindakan Pembedahan dalam 3 Bulan_ → `Observation.valueBoolean` (1033, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 62 |
| Procedure | 7 |
| Condition | 4 |
| RelatedPerson | 2 |
| Immunization | 2 |
| Patient | 1 |
| Practitioner | 1 |
| PractitionerRole | 1 |
| Encounter | 1 |
| EpisodeOfCare | 1 |
| **Total** | **82** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 96 | PractitionerRole | `PractitionerRole.code.coding` | 309453006.0 | Registered midwife | http://snomed.info/sct |
| 2 | 97 | PractitionerRole | `PractitionerRole.code.coding` | 309367003.0 | Obstetrician and gynecologist | http://snomed.info/sct |
| 3 | 98 | PractitionerRole | `PractitionerRole.code.coding` | 309343006.0 | Physician | http://snomed.info/sct |
| 4 | 99 | PractitionerRole | `PractitionerRole.code.coding` | 224535009.0 | Registered nurse | http://snomed.info/sct |
| 5 | 100 | PractitionerRole | `PractitionerRole.code.coding` | 82296001.0 | Pediatrician | http://snomed.info/sct |
| 6 | 120 | Condition | `Condition.code.coding` | Z00.1 | Routine child health examination | http://hl7.org/fhir/sid/icd-10 |
| 7 | 137 | EpisodeOfCare | `EpisodeOfCare.type.coding` | Neonate | Neonate | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 8 | 147 | Observation | `Observation.code.coding` | 365475008.0 | Place in family order | http://snomed.info/sct |
| 9 | 158 | Observation | `Observation.code.coding` | 57715-5 | Birth time | http://loinc.org |
| 10 | 170 | Observation | `Observation.code.coding` | 76516-4 | Gestational age—​at birth | http://loinc.org |
| 11 | 173 | Observation | `Observation.component.code.coding` | SP000398 | Usia Kehamilan Saat Persalinan (hari) | http://terminology.kemkes.go.id/sp |
| 12 | 211 | Observation | `Observation.code.coding` | 8339-4 | Birth weight Measured | http://loinc.org |
| 13 | 223 | Observation | `Observation.code.coding` | 89269-5 | Body height Measured --at birth | http://loinc.org |
| 14 | 235 | Observation | `Observation.code.coding` | 8290-9 | Head Occipital-frontal circumference --at birth- by Tape measure | http://loinc.org |
| 15 | 247 | Observation | `Observation.code.coding` | 9272-6 | 1 minute Apgar Score | http://loinc.org |
| 16 | 248 | Observation | `Observation.interpretation.coding` | 57284007.0 | Severe birth asphyxia | http://snomed.info/sct |
| 17 | 253 | Observation | `Observation.interpretation.coding` | 77362009.0 | Mild to moderate birth asphyxia | http://snomed.info/sct |
| 18 | 258 | Observation | `Observation.interpretation.coding` | 275307002.0 | Apgar normal | http://snomed.info/sct |
| 19 | 272 | Observation | `Observation.code.coding` | 9274-2 | 5 minute Apgar Score | http://loinc.org |
| 20 | 273 | Observation | `Observation.interpretation.coding` | 57284007.0 | Severe birth asphyxia | http://snomed.info/sct |
| 21 | 278 | Observation | `Observation.interpretation.coding` | 77362009.0 | Mild to moderate birth asphyxia | http://snomed.info/sct |
| 22 | 283 | Observation | `Observation.interpretation.coding` | 275307002.0 | Apgar normal | http://snomed.info/sct |
| 23 | 297 | Observation | `Observation.code.coding` | 9271-8 | 10 minute Apgar Score | http://loinc.org |
| 24 | 298 | Observation | `Observation.interpretation.coding` | 57284007.0 | Severe birth asphyxia | http://snomed.info/sct |
| 25 | 303 | Observation | `Observation.interpretation.coding` | 77362009.0 | Mild to moderate birth asphyxia | http://snomed.info/sct |
| 26 | 308 | Observation | `Observation.interpretation.coding` | 275307002.0 | Apgar normal | http://snomed.info/sct |
| 27 | 322 | Observation | `Observation.code.coding` | 276654001.0 | Congenital malformation | http://snomed.info/sct |
| 28 | 324 | Observation | `Observation.valueCodeableConcept.coding` | 80281008.0 | Cleft lip | http://snomed.info/sct |
| 29 | 325 | Observation | `Observation.valueCodeableConcept.coding` | 13213009.0 | Congenital heart disease | http://snomed.info/sct |
| 30 | 326 | Observation | `Observation.valueCodeableConcept.coding` | 35045004.0 | Microtia | http://snomed.info/sct |
| 31 | 327 | Observation | `Observation.valueCodeableConcept.coding` | 22006008.0 | Hypertelorism | http://snomed.info/sct |
| 32 | 328 | Observation | `Observation.valueCodeableConcept.coding` | 367506006.0 | Polydactyly | http://snomed.info/sct |
| 33 | 329 | Observation | `Observation.valueCodeableConcept.coding` | 52781008.0 | Congenital hip dysplasia | http://snomed.info/sct |
| 34 | 330 | Observation | `Observation.valueCodeableConcept.coding` | 1156475005.0 | Congenital talipes equinovarus | http://snomed.info/sct |
| 35 | 331 | Observation | `Observation.valueCodeableConcept.coding` | 253098009.0 | Neural tube defect | http://snomed.info/sct |
| 36 | 332 | Observation | `Observation.valueCodeableConcept.coding` | 118928003.0 | Disorder of abdominal wall | http://snomed.info/sct |
| 37 | 333 | Observation | `Observation.valueCodeableConcept.coding` | 42030000.0 | Disorder of the genitourinary system | http://snomed.info/sct |
| 38 | 334 | Observation | `Observation.valueCodeableConcept.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 39 | 345 | Observation | `Observation.code.coding` | 8867-4 | Heart rate | http://loinc.org |
| 40 | 357 | Observation | `Observation.code.coding` | 8310-5 | Body temperature | http://loinc.org |
| 41 | 368 | Observation | `Observation.code.coding` | 9279-1 | Respiratory rate | http://loinc.org |
| 42 | 380 | Procedure | `Procedure.code.coding` | 386412000.0 | Resuscitation of neonate | http://snomed.info/sct |
| 43 | 391 | Procedure | `Procedure.code.coding` | PC000003 | Manajemen Terpadu Bayi Muda (MTBM) | http://terminology.kemkes.go.id/CodeSystem/clinical-term" |
| 44 | 402 | Procedure | `Procedure.code.coding` | SP000126 | ARV Profilaksis | http://terminology.kemkes.go.id/sp |
| 45 | 413 | Procedure | `Procedure.code.coding` | 448883004.0 | Injection of vitamin K1 | http://snomed.info/sct |
| 46 | 424 | Procedure | `Procedure.code.coding` | PC000001 | Perawatan Tali Pusat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 47 | 435 | Procedure | `Procedure.code.coding` | PC000002 | Pemberian Salep Antibiotik Mata | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 48 | 446 | Immunization | `Immunization.vaccineCode` | 8.0 | Hep B, adolescent or pediatric | http://hl7.org/fhir/sid/cvx |
| 49 | 447 | Immunization | `Immunization.vaccineCode` | VG45 | HepB | http://sys-ids.kemkes.go.id/kfa |
| 50 | 470 | Immunization | `Immunization.vaccineCode` | VG45 | HepB | http://sys-ids.kemkes.go.id/kfa |
| 51 | 471 | Immunization | `Immunization.vaccineCode` | 30.0 | hepatitis B immune globulin | http://hl7.org/fhir/sid/cvx |
| 52 | 494 | Procedure | `Procedure.code.coding` | 431868002.0 | Initiation of breastfeeding | http://snomed.info/sct |
| 53 | 504 | Observation | `Observation.code.coding` | OC000016 | Waktu Inisiasi Menyusui Dini | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 54 | 505 | Observation | `Observation.valueCodeableConcept.coding` | OV000014 | Kurang dari 1 Jam | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 55 | 506 | Observation | `Observation.valueCodeableConcept.coding` | OV000015 | Lebih dari 1 Jam | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 56 | 514 | Observation | `Observation.code.coding` | 424144002.0 | Current chronological age | http://snomed.info/sct |
| 57 | 526 | Observation | `Observation.code.coding` | 424144002.0 | Current chronological age | http://snomed.info/sct |
| 58 | 537 | Observation | `Observation.code.coding` | 57071-3 | Obstetric delivery method | http://loinc.org |
| 59 | 539 | Observation | `Observation.valueCodeableConcept.coding` | 48782003.0 | Delivery normal | http://snomed.info/sct |
| 60 | 540 | Observation | `Observation.valueCodeableConcept.coding` | 200144004.0 | Deliveries by cesarean | http://snomed.info/sct |
| 61 | 548 | Observation | `Observation.code.coding` | 12729009.0 | Prolonged rupture of membranes | http://snomed.info/sct |
| 62 | 558 | Observation | `Observation.code.coding` | 168092006.0 | Amniotic fluid -meconium stain | http://snomed.info/sct |
| 63 | 568 | Observation | `Observation.code.coding` | 130955003.0 | Fetal distress | http://snomed.info/sct |
| 64 | 578 | Observation | `Observation.code.coding` | 415105001.0 | Placental abruption | http://snomed.info/sct |
| 65 | 588 | Observation | `Observation.code.coding` | 206376005.0 | Neonatal sepsis | http://snomed.info/sct |
| 66 | 590 | Observation | `Observation.valueCodeableConcept.coding` | 765106006.0 | Early-onset neonatal sepsis | http://snomed.info/sct |
| 67 | 591 | Observation | `Observation.valueCodeableConcept.coding` | 765107002.0 | Late-onset neonatal sepsis | http://snomed.info/sct |
| 68 | 600 | Observation | `Observation.code.coding` | OC000126 | Klasifikasi infeksi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 69 | 602 | Observation | `Observation.valueCodeableConcept.coding` | 82353009.0 | Congenital infectious disease | http://snomed.info/sct |
| 70 | 603 | Observation | `Observation.valueCodeableConcept.coding` | 66844003.0 | Generalized infection during labor | http://snomed.info/sct |
| 71 | 604 | Observation | `Observation.valueCodeableConcept.coding` | 178280004.0 | Postnatal infection | http://snomed.info/sct |
| 72 | 611 | Observation | `Observation.code.coding` | 392230005.0 | Catheterization of vein | http://snomed.info/sct |
| 73 | 621 | Observation | `Observation.code.coding` | 40617009.0 | Artificial ventilation | http://snomed.info/sct |
| 74 | 631 | Observation | `Observation.code.coding` | 281789004.0 | Antibiotic therapy | http://snomed.info/sct |
| 75 | 641 | Observation | `Observation.code.coding` | 305351004.0 | Admission to intensive care unit | http://snomed.info/sct |
| 76 | 643 | Observation | `Observation.component.code.coding` | 272125009.0 | Priorities | http://snomed.info/sct |
| 77 | 644 | Observation | `Observation.component.valueCodeableConcept.coding` | 394849002.0 | High priority | http://snomed.info/sct |
| 78 | 645 | Observation | `Observation.component.valueCodeableConcept.coding` | 394848005.0 | Normal priority | http://snomed.info/sct |
| 79 | 646 | Observation | `Observation.component.valueCodeableConcept.coding` | 1251527002.0 | Low priority | http://snomed.info/sct |
| 80 | 649 | Observation | `Observation.component.code.coding` | 78033-8 | Hospital stay duration | http://loinc.org |
| 81 | 658 | Observation | `Observation.code.coding` | 183797002.0 | Duration of inpatient stay | http://snomed.info/sct |
| 82 | 668 | Condition | `Condition.code.coding` | Z00.1 | Routine child health examination | http://hl7.org/fhir/sid/icd-10 |
| 83 | 676 | Condition | `Condition.code.coding` | Z00.1 | Routine child health examination | http://hl7.org/fhir/sid/icd-10 |
| 84 | 684 | Condition | `Condition.code.coding` | Z00.1 | Routine child health examination | http://hl7.org/fhir/sid/icd-10 |
| 85 | 696 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 86 | 706 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://loinc.org |
| 87 | 716 | Observation | `Observation.code.coding` | 1023001.0 | Apnea | http://snomed.info/sct |
| 88 | 726 | Observation | `Observation.code.coding` | 67909005.0 | Chest wall retraction | http://snomed.info/sct |
| 89 | 736 | Observation | `Observation.code.coding` | 248568003.0 | Nasal flaring | http://snomed.info/sct |
| 90 | 746 | Observation | `Observation.code.coding` | 62085005.0 | Grunting respiration | http://snomed.info/sct |
| 91 | 756 | Observation | `Observation.code.coding` | 3415004.0 | Cyanosis | http://snomed.info/sct |
| 92 | 766 | Observation | `Observation.code.coding` | 91175000.0 | Seizure | http://snomed.info/sct |
| 93 | 776 | Observation | `Observation.code.coding` | 214264003.0 | Lethargy | http://snomed.info/sct |
| 94 | 786 | Observation | `Observation.code.coding` | 247905005.0 | Lack of spontaneous movement | http://snomed.info/sct |
| 95 | 796 | Observation | `Observation.code.coding` | 835279003.0 | Decreased reflex | http://snomed.info/sct |
| 96 | 806 | Observation | `Observation.code.coding` | 95631006.0 | Neonatal drowsiness | http://snomed.info/sct |
| 97 | 816 | Observation | `Observation.code.coding` | 103019006.0 | Bulging fontanelle | http://snomed.info/sct |
| 98 | 826 | Observation | `Observation.code.coding` | 65668001.0 | Otorrhea | http://snomed.info/sct |
| 99 | 836 | Observation | `Observation.code.coding` | 239095007.0 | Omphalitis | http://snomed.info/sct |
| 100 | 846 | Observation | `Observation.code.coding` | 271760008.0 | Pustule | http://snomed.info/sct |
| 101 | 856 | Observation | `Observation.code.coding` | 18165001.0 | Jaundice | http://snomed.info/sct |
| 102 | 866 | Observation | `Observation.code.coding` | 364826005.0 | Finding related to ability to perform breastfeeding | http://snomed.info/sct |
| 103 | 868 | Observation | `Observation.valueCodeableConcept.coding` | 289080009.0 | Able to perform breastfeeding | http://snomed.info/sct |
| 104 | 869 | Observation | `Observation.valueCodeableConcept.coding` | 289084000.0 | Difficulty performing breastfeeding | http://snomed.info/sct |
| 105 | 870 | Observation | `Observation.valueCodeableConcept.coding` | 289081008.0 | Unable to perform breastfeeding | http://snomed.info/sct |
| 106 | 871 | Observation | `Observation.valueCodeableConcept.coding` | unknown | Unknown | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 107 | 878 | Observation | `Observation.code.coding` | 26464-8 | Leukocytes [#/volume] in Blood | http://loinc.org |
| 108 | 882 | Observation | `Observation.dataAbsentReason.coding` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 109 | 889 | Observation | `Observation.code.coding` | 26515-7 | Platelets [#/volume] in Blood | http://loinc.org |
| 110 | 893 | Observation | `Observation.dataAbsentReason.coding` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 111 | 900 | Observation | `Observation.code.coding` | 26499-4 | Neutrophils [#/volume] in Blood | http://loinc.org |
| 112 | 904 | Observation | `Observation.dataAbsentReason.coding` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 113 | 911 | Observation | `Observation.code.coding` | 30341-2 | Erythrocyte [Sedimentation Rate] in Blood | http://loinc.org |
| 114 | 915 | Observation | `Observation.dataAbsentReason.coding` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 115 | 922 | Observation | `Observation.code.coding` | 33959-8 | Procalcitonin [Mass/volume] in Serum or Plasma | http://loinc.org |
| 116 | 932 | Observation | `Observation.code.coding` | 1988-5 | C reactive protein [Mass/volume] in Serum or Plasma | http://loinc.org |
| 117 | 943 | Observation | `Observation.code.coding` | 76516-4 | Gestational age--at birth | http://loinc.org |
| 118 | 953 | Observation | `Observation.code.coding` | 89269-5 | Body height Measured --at birth | http://loinc.org |
| 119 | 963 | Observation | `Observation.code.coding` | 8339-4 | Birth weight Measured | http://loinc.org |
| 120 | 973 | Observation | `Observation.code.coding` | 9274-2 | 5 minute Apgar Score | http://loinc.org |
| 121 | 981 | Observation | `Observation.code.coding` | 8867-4 | Heart rate | http://loinc.org |
| 122 | 991 | Observation | `Observation.code.coding` | 9279-1 | Respiratory rate | http://loinc.org |
| 123 | 1001 | Observation | `Observation.code.coding` | 8310-5 | Body temperature | http://loinc.org |
| 124 | 1011 | Observation | `Observation.code.coding` | 11337-3 | History of Hospitalization | http://loinc.org |
| 125 | 1021 | Observation | `Observation.code.coding` | 11347-2 | History of Outpatient visits | http://loinc.org |
| 126 | 1031 | Observation | `Observation.code.coding` | 8690-0 | History of Surgical procedures | http://loinc.org |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 72 |
| http://loinc.org | 31 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 6 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 5 |
| http://hl7.org/fhir/sid/icd-10 | 4 |
| http://terminology.kemkes.go.id/sp | 2 |
| http://hl7.org/fhir/sid/cvx | 2 |
| http://sys-ids.kemkes.go.id/kfa | 2 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 1 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term" | 1 |
| **Total** | **126** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 51 | – | Faskes yang Melayani INC | Organization | `Organization.name` |
