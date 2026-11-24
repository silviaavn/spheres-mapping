# Output Form: SIM RS Harapan Ibu BBL

Sumber: `mapping/phdt-data-dictionary-rs-harapan-ibu-bbl.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-rs-harapan-ibu-bbl.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 79 |
| Code (`jumlah code` = 1) | 110 |
| Code unik (code + CodeSystem) | 99 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 2 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–30 | Patient | – | – | _Nama Bayi_ → `Patient.name.text` (2, tanpa BQ)<br>_NIK Bayi/ Ibu_ → `Patient.identifier.value` (6, tanpa BQ)<br>_NIK Ibu_ → `Patient.identifier.value` (9, tanpa BQ)<br>_No HP Orang Tua_ → `Patient.telecom` (10, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (13, tanpa BQ)<br>_Tempat Lahir_ → `Patient.extension.valueAddress.city` (15, tanpa BQ)<br>_Alamat Domisili_ → `Patient.address.line` (16, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (21, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (24, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.extension.valueCode` (27, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.extension.valueCode` (30, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (447, tanpa BQ)<br>_Domisili_ → `Patient.address.line` (865, tanpa BQ) |
| 2 | 31–37 | RelatedPerson | – | – | _Nama Ibu_ → `RelatedPerson.name.text` (31, tanpa BQ)<br>_NIK Ibu_ → `RelatedPerson.identifier` (32, tanpa BQ) |
| 3 | 38–44 | RelatedPerson | – | – | _Nama Ayah_ → `RelatedPerson.name.text` (38, tanpa BQ)<br>_NIK Ayah_ → `RelatedPerson.identifier` (39, tanpa BQ) |
| 4 | 83–89 | Practitioner | – | – | _NIK_ → `Practitioner.identifier.value` (85, tanpa BQ)<br>_Nama Tenaga Kesehatan_ → `Practitioner.name.text` (87, tanpa BQ)<br>_Jenis Kelamin Tenaga Kesehatan_ → `Practitioner.gender` (88, tanpa BQ) |
| 5 | 90–98 | PractitionerRole | – | – | _Tenaga Pemeriksa_ → `PractitionerRole.code.coding` (94, tanpa BQ) |
| 6 | 100–115 | Encounter | – | – | _Kunjungan Neonatus_ → `Encounter.identifier` (101, tanpa BQ)<br>_Tanggal Kunjungan_ → `Encounter.period.start` (110, tanpa BQ)<br>_Tempat Pelayanan Kunjungan Neonatus_ → `Encounter.location.display` (113, tanpa BQ)<br>_Kondisi Saat Pulang_ → `Encounter.hospitalization.dischargeDisposition.coding` (615, tanpa BQ) |
| 7 | 116–123 | Condition | Z00.1 | Routine child health examination | _Tanggal Diagnosis_ → `Condition.recordedDate` (122, tanpa BQ) |
| 8 | 134–142 | EpisodeOfCare | Neonate | Neonate | – |
| 9 | 143–153 | Observation | 365475008.0 | Place in family order | _Anak ke_ → `Observation.valueInteger` (146, tanpa BQ) |
| 10 | 154–164 | Observation | 57715-5 | Birth time | _Jam Lahir_ → `Observation.valueTime` (157, tanpa BQ) |
| 11 | 166–206 | Observation | 76516-4 | Gestational age—​at birth | _Usia Gestasi Saat Lahir_ → `Observation.valueQuantity.value` (169, tanpa BQ)<br>_Golongan darah_ → `Observation` (181, tanpa BQ)<br>_Rhesus_ → `Observation` (195, tanpa BQ) |
| 12 | 207–218 | Observation | 8339-4 | Birth weight Measured | _Berat Badan Saat Lahir (gram)_ → `Observation.valueQuantity.value` (210, tanpa BQ) |
| 13 | 219–230 | Observation | 89269-5 | Body height Measured --at birth | _Panjang Badan Saat Lahir_ → `Observation.valueQuantity.value` (222, tanpa BQ) |
| 14 | 231–242 | Observation | 8290-9 | Head Occipital-frontal circumference --at birth- by Tape measure | _Lingkar Kepala Saat Lahir_ → `Observation.valueQuantity.value` (234, tanpa BQ) |
| 15 | 243–264 | Observation | 276654001.0 | Congenital malformation | _Kelainan Bawaan_ → `Observation.valueString` (246, tanpa BQ) |
| 16 | 265–276 | Observation | 8867-4 | Heart rate | _Frekuensi Denyut Jantung_ → `Observation.valueQuantity.value` (268, tanpa BQ) |
| 17 | 277–287 | Observation | 8310-5 | Body temperature | _Suhu_ → `Observation.valueQuantity.value` (280, tanpa BQ) |
| 18 | 288–298 | Observation | 9279-1 | Respiratory rate | _Pernapasan_ → `Observation.valueQuantity.value` (291, tanpa BQ) |
| 19 | 299–309 | Procedure | 386412000.0 | Resuscitation of neonate | _Apakah Diberikan Resusitasi_ → `Procedure.category.coding` (299, tanpa BQ) |
| 20 | 310–320 | Procedure | PC000003 | Manajemen Terpadu Bayi Muda (MTBM) | _Apakah dilakukan pemeriksaan kesehatan dengan pendekatan MTBM_ → `Procedure.category.coding` (310, tanpa BQ) |
| 21 | 321–331 | Procedure | SP000126 | ARV Profilaksis | _ARV Profilaksis pada bayi baru lahir_ → `Procedure.category.coding` (321, tanpa BQ) |
| 22 | 332–342 | Procedure | 448883004.0 | Injection of vitamin K1 | _Apakah diberikan vitamin K_ → `Procedure.category.coding` (332, tanpa BQ) |
| 23 | 343–353 | Procedure | PC000001 | Perawatan Tali Pusat | _Perawatan Tali Pusat_ → `Procedure.category.coding` (343, tanpa BQ) |
| 24 | 354–364 | Procedure | PC000002 | Pemberian Salep Antibiotik Mata | _Salep Antibiotik Mata_ → `Procedure.category.coding` (354, tanpa BQ) |
| 25 | 365–392 | Immunization | – | – | _Imunisasi Hepatitis B (HB0)_ → `Immunization.status` (365, tanpa BQ)<br>_Jika Tidak Imunisasi Hepatitis B(HB0)_ → `Immunization.statusReason.coding` (382, tanpa BQ)<br>_Imunisasi HBIg_ → `Immunization.status` (390, tanpa BQ) |
| 26 | 393–413 | Immunization | – | – | – |
| 27 | 414–424 | Procedure | 431868002.0 | Initiation of breastfeeding | _Inisiasi Menyusu Dini (IMD)_ → `Procedure.category.coding` (414, tanpa BQ) |
| 28 | 425–436 | Observation | OC000016 | Waktu Inisiasi Menyusui Dini | _Waktu Inisiasi Menyusu Dini (IMD)_ → `Observation.valueCodeableConcept.coding` (428, tanpa BQ) |
| 29 | 437–446 | Observation | 424144002.0 | Current chronological age | _Usia Neonatus_ → `Observation.valueQuantity.value` (439, tanpa BQ) |
| 30 | 449–459 | Observation | 424144002.0 | Current chronological age | _Usia Ibu_ → `Observation.valueQuantity.value` (451, tanpa BQ) |
| 31 | 460–470 | Observation | 57071-3 | Obstetric delivery method | _Metode Persalinan_ → `Observation.valueCodeableConcept.coding` (462, tanpa BQ) |
| 32 | 471–480 | Observation | 12729009.0 | Prolonged rupture of membranes | _Pecah Ketuban > 18 Jam_ → `Observation.valueBoolean` (473, tanpa BQ) |
| 33 | 481–490 | Observation | 168092006.0 | Amniotic fluid -meconium stain | _Air Ketuban Bercampur Mekonium_ → `Observation.valueBoolean` (483, tanpa BQ) |
| 34 | 491–500 | Observation | 130955003.0 | Fetal distress | _Gawat Janin Intrauterin_ → `Observation.valueBoolean` (493, tanpa BQ) |
| 35 | 501–510 | Observation | 415105001.0 | Placental abruption | _Solusio Plasenta_ → `Observation.valueBoolean` (503, tanpa BQ) |
| 36 | 511–522 | Observation | 206376005.0 | Neonatal sepsis | _Onset Sepsis_ → `Observation.valueCodeableConcept.coding` (513, tanpa BQ) |
| 37 | 523–533 | Observation | OC000126 | Klasifikasi infeksi | _Klasifikasi Infeksi_ → `Observation.valueCodeableConcept.coding` (525, tanpa BQ) |
| 38 | 534–543 | Observation | 392230005.0 | Catheterization of vein | _Penggunaan Kateter Vena_ → `Observation.valueBoolean` (536, tanpa BQ) |
| 39 | 544–553 | Observation | 40617009.0 | Artificial ventilation | _Penggunaan Alat Bantu Napas_ → `Observation.valueBoolean` (546, tanpa BQ) |
| 40 | 554–563 | Observation | 281789004.0 | Antibiotic therapy | _Paparan Antibiotik_ → `Observation.valueBoolean` (556, tanpa BQ) |
| 41 | 564–580 | Observation | 305351004.0 | Admission to intensive care unit | _Status Admisi ke ICU_ → `Observation.component.valueCodeableConcept.coding` (567, tanpa BQ)<br>_Lama Perawatan di ICU_ → `Observation.component.code.coding` (572, tanpa BQ) |
| 42 | 581–590 | Observation | 183797002.0 | Duration of inpatient stay | _Lama Rawat Inap di RS_ → `Observation.valueQuantity.value` (583, tanpa BQ) |
| 43 | 591–598 | Condition | Z00.1 | Routine child health examination | _Outcome Klinis_ → `Condition.code.coding` (591, tanpa BQ) |
| 44 | 599–606 | Condition | Z00.1 | Routine child health examination | _Diagnosis Utama (dx_1)_ → `Condition.code.coding` (599, tanpa BQ) |
| 45 | 607–614 | Condition | Z00.1 | Routine child health examination | _Diagnosis Sekunder (dx_2)_ → `Condition.code.coding` (607, tanpa BQ) |
| 46 | 619–628 | Observation | 8480-6 | Systolic blood pressure | _Tekanan Darah Sistolik_ → `Observation.valueQuantity.value` (621, tanpa BQ) |
| 47 | 629–638 | Observation | 8462-4 | Diastolic blood pressure | _Tekanan Darah Diastolik_ → `Observation.valueQuantity.value` (631, tanpa BQ) |
| 48 | 639–648 | Observation | 1023001.0 | Apnea | _Apnea_ → `Observation.valueBoolean` (641, tanpa BQ) |
| 49 | 649–658 | Observation | 67909005.0 | Chest wall retraction | _Tarikan Dinding Dada_ → `Observation.valueBoolean` (651, tanpa BQ) |
| 50 | 659–668 | Observation | 248568003.0 | Nasal flaring | _Pelebaran Cuping Hidung_ → `Observation.valueBoolean` (661, tanpa BQ) |
| 51 | 669–678 | Observation | 62085005.0 | Grunting respiration | _Suara Merintih_ → `Observation.valueBoolean` (671, tanpa BQ) |
| 52 | 679–688 | Observation | 3415004.0 | Cyanosis | _Kulit Tampak Kebiruan_ → `Observation.valueBoolean` (681, tanpa BQ) |
| 53 | 689–698 | Observation | 91175000.0 | Seizure | _Kejang_ → `Observation.valueBoolean` (691, tanpa BQ) |
| 54 | 699–708 | Observation | 214264003.0 | Lethargy | _Tubuh Lemas_ → `Observation.valueBoolean` (701, tanpa BQ) |
| 55 | 709–718 | Observation | 247905005.0 | Lack of spontaneous movement | _Penurunan Gerakan Normal_ → `Observation.valueBoolean` (711, tanpa BQ) |
| 56 | 719–728 | Observation | 835279003.0 | Decreased reflex | _Refleks Lemah_ → `Observation.valueBoolean` (721, tanpa BQ) |
| 57 | 729–738 | Observation | 95631006.0 | Neonatal drowsiness | _Sulit Dibangunkan_ → `Observation.valueBoolean` (731, tanpa BQ) |
| 58 | 739–748 | Observation | 103019006.0 | Bulging fontanelle | _Ubun-Ubun Menonjol_ → `Observation.valueBoolean` (741, tanpa BQ) |
| 59 | 749–758 | Observation | 65668001.0 | Otorrhea | _Keluar Nanah dari Telinga_ → `Observation.valueBoolean` (751, tanpa BQ) |
| 60 | 759–768 | Observation | 239095007.0 | Omphalitis | _Kemerahan pada Umbilikus_ → `Observation.valueBoolean` (761, tanpa BQ) |
| 61 | 769–778 | Observation | 271760008.0 | Pustule | _Pustula Kulit_ → `Observation.valueBoolean` (771, tanpa BQ) |
| 62 | 779–788 | Observation | 18165001.0 | Jaundice | _Ikterus_ → `Observation.valueBoolean` (781, tanpa BQ) |
| 63 | 789–800 | Observation | 364826005.0 | Finding related to ability to perform breastfeeding | _Gangguan Menyusu_ → `Observation.valueCodeableConcept.coding` (791, tanpa BQ) |
| 64 | 801–811 | Observation | 26464-8 | Leukocytes [#/volume] in Blood | _Jumlah Leukosit_ → `Observation.valueQuantity.value` (803, tanpa BQ)<br>_Dilakukan Tes Jumlah Leukosit_ → `Observation.dataAbsentReason.coding` (805, tanpa BQ) |
| 65 | 812–822 | Observation | 26515-7 | Platelets [#/volume] in Blood | _Jumlah Trombosit_ → `Observation.valueQuantity.value` (814, tanpa BQ)<br>_Dilakukan Tes Jumlah Trombosit_ → `Observation.dataAbsentReason.coding` (816, tanpa BQ) |
| 66 | 823–833 | Observation | 26499-4 | Neutrophils [#/volume] in Blood | _Jumlah Neutrofil Absolut_ → `Observation.valueQuantity.value` (825, tanpa BQ)<br>_Dilakukan Tes Jumlah Neutrofil Absolut_ → `Observation.dataAbsentReason.coding` (827, tanpa BQ) |
| 67 | 834–844 | Observation | 30341-2 | Erythrocyte [Sedimentation Rate] in Blood | _Erythrocyte Sedimentation Rate (ESR)_ → `Observation.valueQuantity.value` (836, tanpa BQ)<br>_Dilakukan Tes Erythrocyte Sedimentation Rate (ESR)_ → `Observation.dataAbsentReason.coding` (838, tanpa BQ) |
| 68 | 845–854 | Observation | 33959-8 | Procalcitonin [Mass/volume] in Serum or Plasma | _Kadar Prokalsitonin_ → `Observation.valueQuantity.value` (847, tanpa BQ) |
| 69 | 855–864 | Observation | 1988-5 | C reactive protein [Mass/volume] in Serum or Plasma | _C-Reactive Protein_ → `Observation.valueQuantity.value` (857, tanpa BQ) |
| 70 | 866–875 | Observation | 76516-4 | Gestational age--at birth | _Usia Gestasi_ → `Observation.valueQuantity.value` (868, tanpa BQ) |
| 71 | 876–885 | Observation | 89269-5 | Body height Measured --at birth | _Panjang Badan Lahir_ → `Observation.valueQuantity.value` (878, tanpa BQ) |
| 72 | 886–895 | Observation | 8339-4 | Birth weight Measured | _Berat Badan Lahir_ → `Observation.valueQuantity.value` (888, tanpa BQ) |
| 73 | 896–903 | Observation | 9274-2 | 5 minute Apgar Score | _Skor APGAR Menit ke-5_ → `Observation.code.coding` (896, tanpa BQ) |
| 74 | 904–913 | Observation | 8867-4 | Heart rate | _Frekuensi Nadi_ → `Observation.valueQuantity.value` (906, tanpa BQ) |
| 75 | 914–923 | Observation | 9279-1 | Respiratory rate | _Laju Pernapasan_ → `Observation.valueQuantity.value` (916, tanpa BQ) |
| 76 | 924–933 | Observation | 8310-5 | Body temperature | _Suhu Tubuh_ → `Observation.valueQuantity.value` (926, tanpa BQ) |
| 77 | 934–943 | Observation | 11337-3 | History of Hospitalization | _Riwayat Rawat Inap Min. 1 Malam dalam 3 Bulan_ → `Observation.valueBoolean` (936, tanpa BQ) |
| 78 | 944–953 | Observation | 11347-2 | History of Outpatient visits | _Riwayat Kunjungan Faskes dalam 3 Bulan_ → `Observation.valueBoolean` (946, tanpa BQ) |
| 79 | 954–963 | Observation | 8690-0 | History of Surgical procedures | _Riwayat Tindakan Pembedahan dalam 3 Bulan_ → `Observation.valueBoolean` (956, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 59 |
| Procedure | 7 |
| Condition | 4 |
| RelatedPerson | 2 |
| Immunization | 2 |
| Patient | 1 |
| Practitioner | 1 |
| PractitionerRole | 1 |
| Encounter | 1 |
| EpisodeOfCare | 1 |
| **Total** | **79** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 94 | PractitionerRole | `PractitionerRole.code.coding` | 309453006.0 | Registered midwife | http://snomed.info/sct |
| 2 | 95 | PractitionerRole | `PractitionerRole.code.coding` | 309367003.0 | Obstetrician and gynecologist | http://snomed.info/sct |
| 3 | 96 | PractitionerRole | `PractitionerRole.code.coding` | 309343006.0 | Physician | http://snomed.info/sct |
| 4 | 97 | PractitionerRole | `PractitionerRole.code.coding` | 224535009.0 | Registered nurse | http://snomed.info/sct |
| 5 | 98 | PractitionerRole | `PractitionerRole.code.coding` | 82296001.0 | Pediatrician | http://snomed.info/sct |
| 6 | 118 | Condition | `Condition.code.coding` | Z00.1 | Routine child health examination | http://hl7.org/fhir/sid/icd-10 |
| 7 | 135 | EpisodeOfCare | `EpisodeOfCare.type.coding` | Neonate | Neonate | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 8 | 145 | Observation | `Observation.code.coding` | 365475008.0 | Place in family order | http://snomed.info/sct |
| 9 | 156 | Observation | `Observation.code.coding` | 57715-5 | Birth time | http://loinc.org |
| 10 | 168 | Observation | `Observation.code.coding` | 76516-4 | Gestational age—​at birth | http://loinc.org |
| 11 | 171 | Observation | `Observation.component.code.coding` | SP000398 | Usia Kehamilan Saat Persalinan (hari) | http://terminology.kemkes.go.id/sp |
| 12 | 209 | Observation | `Observation.code.coding` | 8339-4 | Birth weight Measured | http://loinc.org |
| 13 | 221 | Observation | `Observation.code.coding` | 89269-5 | Body height Measured --at birth | http://loinc.org |
| 14 | 233 | Observation | `Observation.code.coding` | 8290-9 | Head Occipital-frontal circumference --at birth- by Tape measure | http://loinc.org |
| 15 | 245 | Observation | `Observation.code.coding` | 276654001.0 | Congenital malformation | http://snomed.info/sct |
| 16 | 247 | Observation | `Observation.valueCodeableConcept.coding` | 80281008.0 | Cleft lip | http://snomed.info/sct |
| 17 | 248 | Observation | `Observation.valueCodeableConcept.coding` | 13213009.0 | Congenital heart disease | http://snomed.info/sct |
| 18 | 249 | Observation | `Observation.valueCodeableConcept.coding` | 35045004.0 | Microtia | http://snomed.info/sct |
| 19 | 250 | Observation | `Observation.valueCodeableConcept.coding` | 22006008.0 | Hypertelorism | http://snomed.info/sct |
| 20 | 251 | Observation | `Observation.valueCodeableConcept.coding` | 367506006.0 | Polydactyly | http://snomed.info/sct |
| 21 | 252 | Observation | `Observation.valueCodeableConcept.coding` | 52781008.0 | Congenital hip dysplasia | http://snomed.info/sct |
| 22 | 253 | Observation | `Observation.valueCodeableConcept.coding` | 1156475005.0 | Congenital talipes equinovarus | http://snomed.info/sct |
| 23 | 254 | Observation | `Observation.valueCodeableConcept.coding` | 253098009.0 | Neural tube defect | http://snomed.info/sct |
| 24 | 255 | Observation | `Observation.valueCodeableConcept.coding` | 118928003.0 | Disorder of abdominal wall | http://snomed.info/sct |
| 25 | 256 | Observation | `Observation.valueCodeableConcept.coding` | 42030000.0 | Disorder of the genitourinary system | http://snomed.info/sct |
| 26 | 257 | Observation | `Observation.valueCodeableConcept.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 27 | 267 | Observation | `Observation.code.coding` | 8867-4 | Heart rate | http://loinc.org |
| 28 | 279 | Observation | `Observation.code.coding` | 8310-5 | Body temperature | http://loinc.org |
| 29 | 290 | Observation | `Observation.code.coding` | 9279-1 | Respiratory rate | http://loinc.org |
| 30 | 302 | Procedure | `Procedure.code.coding` | 386412000.0 | Resuscitation of neonate | http://snomed.info/sct |
| 31 | 313 | Procedure | `Procedure.code.coding` | PC000003 | Manajemen Terpadu Bayi Muda (MTBM) | http://terminology.kemkes.go.id/CodeSystem/clinical-term" |
| 32 | 324 | Procedure | `Procedure.code.coding` | SP000126 | ARV Profilaksis | http://terminology.kemkes.go.id/sp |
| 33 | 335 | Procedure | `Procedure.code.coding` | 448883004.0 | Injection of vitamin K1 | http://snomed.info/sct |
| 34 | 346 | Procedure | `Procedure.code.coding` | PC000001 | Perawatan Tali Pusat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 35 | 357 | Procedure | `Procedure.code.coding` | PC000002 | Pemberian Salep Antibiotik Mata | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 36 | 368 | Immunization | `Immunization.vaccineCode` | 8.0 | Hep B, adolescent or pediatric | http://hl7.org/fhir/sid/cvx |
| 37 | 369 | Immunization | `Immunization.vaccineCode` | VG45 | HepB | http://sys-ids.kemkes.go.id/kfa |
| 38 | 393 | Immunization | `Immunization.vaccineCode` | VG45 | HepB | http://sys-ids.kemkes.go.id/kfa |
| 39 | 394 | Immunization | `Immunization.vaccineCode` | 30.0 | hepatitis B immune globulin | http://hl7.org/fhir/sid/cvx |
| 40 | 417 | Procedure | `Procedure.code.coding` | 431868002.0 | Initiation of breastfeeding | http://snomed.info/sct |
| 41 | 427 | Observation | `Observation.code.coding` | OC000016 | Waktu Inisiasi Menyusui Dini | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 42 | 428 | Observation | `Observation.valueCodeableConcept.coding` | OV000014 | Kurang dari 1 Jam | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 43 | 429 | Observation | `Observation.valueCodeableConcept.coding` | OV000015 | Lebih dari 1 Jam | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 44 | 437 | Observation | `Observation.code.coding` | 424144002.0 | Current chronological age | http://snomed.info/sct |
| 45 | 449 | Observation | `Observation.code.coding` | 424144002.0 | Current chronological age | http://snomed.info/sct |
| 46 | 460 | Observation | `Observation.code.coding` | 57071-3 | Obstetric delivery method | http://loinc.org |
| 47 | 462 | Observation | `Observation.valueCodeableConcept.coding` | 48782003.0 | Delivery normal | http://snomed.info/sct |
| 48 | 463 | Observation | `Observation.valueCodeableConcept.coding` | 200144004.0 | Deliveries by cesarean | http://snomed.info/sct |
| 49 | 471 | Observation | `Observation.code.coding` | 12729009.0 | Prolonged rupture of membranes | http://snomed.info/sct |
| 50 | 481 | Observation | `Observation.code.coding` | 168092006.0 | Amniotic fluid -meconium stain | http://snomed.info/sct |
| 51 | 491 | Observation | `Observation.code.coding` | 130955003.0 | Fetal distress | http://snomed.info/sct |
| 52 | 501 | Observation | `Observation.code.coding` | 415105001.0 | Placental abruption | http://snomed.info/sct |
| 53 | 511 | Observation | `Observation.code.coding` | 206376005.0 | Neonatal sepsis | http://snomed.info/sct |
| 54 | 513 | Observation | `Observation.valueCodeableConcept.coding` | 765106006.0 | Early-onset neonatal sepsis | http://snomed.info/sct |
| 55 | 514 | Observation | `Observation.valueCodeableConcept.coding` | 765107002.0 | Late-onset neonatal sepsis | http://snomed.info/sct |
| 56 | 523 | Observation | `Observation.code.coding` | OC000126 | Klasifikasi infeksi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 57 | 525 | Observation | `Observation.valueCodeableConcept.coding` | 82353009.0 | Congenital infectious disease | http://snomed.info/sct |
| 58 | 526 | Observation | `Observation.valueCodeableConcept.coding` | 66844003.0 | Generalized infection during labor | http://snomed.info/sct |
| 59 | 527 | Observation | `Observation.valueCodeableConcept.coding` | 178280004.0 | Postnatal infection | http://snomed.info/sct |
| 60 | 534 | Observation | `Observation.code.coding` | 392230005.0 | Catheterization of vein | http://snomed.info/sct |
| 61 | 544 | Observation | `Observation.code.coding` | 40617009.0 | Artificial ventilation | http://snomed.info/sct |
| 62 | 554 | Observation | `Observation.code.coding` | 281789004.0 | Antibiotic therapy | http://snomed.info/sct |
| 63 | 564 | Observation | `Observation.code.coding` | 305351004.0 | Admission to intensive care unit | http://snomed.info/sct |
| 64 | 566 | Observation | `Observation.component.code.coding` | 272125009.0 | Priorities | http://snomed.info/sct |
| 65 | 567 | Observation | `Observation.component.valueCodeableConcept.coding` | 394849002.0 | High priority | http://snomed.info/sct |
| 66 | 568 | Observation | `Observation.component.valueCodeableConcept.coding` | 394848005.0 | Normal priority | http://snomed.info/sct |
| 67 | 569 | Observation | `Observation.component.valueCodeableConcept.coding` | 1251527002.0 | Low priority | http://snomed.info/sct |
| 68 | 572 | Observation | `Observation.component.code.coding` | 78033-8 | Hospital stay duration | http://loinc.org |
| 69 | 581 | Observation | `Observation.code.coding` | 183797002.0 | Duration of inpatient stay | http://snomed.info/sct |
| 70 | 591 | Condition | `Condition.code.coding` | Z00.1 | Routine child health examination | http://hl7.org/fhir/sid/icd-10 |
| 71 | 599 | Condition | `Condition.code.coding` | Z00.1 | Routine child health examination | http://hl7.org/fhir/sid/icd-10 |
| 72 | 607 | Condition | `Condition.code.coding` | Z00.1 | Routine child health examination | http://hl7.org/fhir/sid/icd-10 |
| 73 | 619 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 74 | 629 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://loinc.org |
| 75 | 639 | Observation | `Observation.code.coding` | 1023001.0 | Apnea | http://snomed.info/sct |
| 76 | 649 | Observation | `Observation.code.coding` | 67909005.0 | Chest wall retraction | http://snomed.info/sct |
| 77 | 659 | Observation | `Observation.code.coding` | 248568003.0 | Nasal flaring | http://snomed.info/sct |
| 78 | 669 | Observation | `Observation.code.coding` | 62085005.0 | Grunting respiration | http://snomed.info/sct |
| 79 | 679 | Observation | `Observation.code.coding` | 3415004.0 | Cyanosis | http://snomed.info/sct |
| 80 | 689 | Observation | `Observation.code.coding` | 91175000.0 | Seizure | http://snomed.info/sct |
| 81 | 699 | Observation | `Observation.code.coding` | 214264003.0 | Lethargy | http://snomed.info/sct |
| 82 | 709 | Observation | `Observation.code.coding` | 247905005.0 | Lack of spontaneous movement | http://snomed.info/sct |
| 83 | 719 | Observation | `Observation.code.coding` | 835279003.0 | Decreased reflex | http://snomed.info/sct |
| 84 | 729 | Observation | `Observation.code.coding` | 95631006.0 | Neonatal drowsiness | http://snomed.info/sct |
| 85 | 739 | Observation | `Observation.code.coding` | 103019006.0 | Bulging fontanelle | http://snomed.info/sct |
| 86 | 749 | Observation | `Observation.code.coding` | 65668001.0 | Otorrhea | http://snomed.info/sct |
| 87 | 759 | Observation | `Observation.code.coding` | 239095007.0 | Omphalitis | http://snomed.info/sct |
| 88 | 769 | Observation | `Observation.code.coding` | 271760008.0 | Pustule | http://snomed.info/sct |
| 89 | 779 | Observation | `Observation.code.coding` | 18165001.0 | Jaundice | http://snomed.info/sct |
| 90 | 789 | Observation | `Observation.code.coding` | 364826005.0 | Finding related to ability to perform breastfeeding | http://snomed.info/sct |
| 91 | 791 | Observation | `Observation.valueCodeableConcept.coding` | 289080009.0 | Able to perform breastfeeding | http://snomed.info/sct |
| 92 | 792 | Observation | `Observation.valueCodeableConcept.coding` | 289084000.0 | Difficulty performing breastfeeding | http://snomed.info/sct |
| 93 | 793 | Observation | `Observation.valueCodeableConcept.coding` | 289081008.0 | Unable to perform breastfeeding | http://snomed.info/sct |
| 94 | 794 | Observation | `Observation.valueCodeableConcept.coding` | unknown | Unknown | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 95 | 801 | Observation | `Observation.code.coding` | 26464-8 | Leukocytes [#/volume] in Blood | http://loinc.org |
| 96 | 812 | Observation | `Observation.code.coding` | 26515-7 | Platelets [#/volume] in Blood | http://loinc.org |
| 97 | 823 | Observation | `Observation.code.coding` | 26499-4 | Neutrophils [#/volume] in Blood | http://loinc.org |
| 98 | 834 | Observation | `Observation.code.coding` | 30341-2 | Erythrocyte [Sedimentation Rate] in Blood | http://loinc.org |
| 99 | 845 | Observation | `Observation.code.coding` | 33959-8 | Procalcitonin [Mass/volume] in Serum or Plasma | http://loinc.org |
| 100 | 855 | Observation | `Observation.code.coding` | 1988-5 | C reactive protein [Mass/volume] in Serum or Plasma | http://loinc.org |
| 101 | 866 | Observation | `Observation.code.coding` | 76516-4 | Gestational age--at birth | http://loinc.org |
| 102 | 876 | Observation | `Observation.code.coding` | 89269-5 | Body height Measured --at birth | http://loinc.org |
| 103 | 886 | Observation | `Observation.code.coding` | 8339-4 | Birth weight Measured | http://loinc.org |
| 104 | 896 | Observation | `Observation.code.coding` | 9274-2 | 5 minute Apgar Score | http://loinc.org |
| 105 | 904 | Observation | `Observation.code.coding` | 8867-4 | Heart rate | http://loinc.org |
| 106 | 914 | Observation | `Observation.code.coding` | 9279-1 | Respiratory rate | http://loinc.org |
| 107 | 924 | Observation | `Observation.code.coding` | 8310-5 | Body temperature | http://loinc.org |
| 108 | 934 | Observation | `Observation.code.coding` | 11337-3 | History of Hospitalization | http://loinc.org |
| 109 | 944 | Observation | `Observation.code.coding` | 11347-2 | History of Outpatient visits | http://loinc.org |
| 110 | 954 | Observation | `Observation.code.coding` | 8690-0 | History of Surgical procedures | http://loinc.org |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 63 |
| http://loinc.org | 28 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 6 |
| http://hl7.org/fhir/sid/icd-10 | 4 |
| http://terminology.kemkes.go.id/sp | 2 |
| http://hl7.org/fhir/sid/cvx | 2 |
| http://sys-ids.kemkes.go.id/kfa | 2 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 1 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term" | 1 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 1 |
| **Total** | **110** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 49 | – | Faskes yang Melayani Kunjungan Neonatus | Organization | `Organization.name` |
