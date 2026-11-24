# Output Form: SIM RS Narmada INC

Sumber: `mapping/phdt-data-dictionary-rs-narmada-inc.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-rs-narmada-inc.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 86 |
| Code (`jumlah code` = 1) | 262 |
| Code unik (code + CodeSystem) | 203 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 2 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–30 | Patient | – | – | _Nama Pasien_ → `Patient.name.text` (2, tanpa BQ)<br>_NIK_ → `Patient.identifier.value` (6, tanpa BQ)<br>_No Hp_ → `Patient.telecom` (7, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (10, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (11, tanpa BQ)<br>_Status Pernikahan_ → `Patient.maritalStatus.coding` (13, tanpa BQ)<br>_Alamat_ → `Patient.address.line` (16, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (21, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (24, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.extension.valueCode` (27, tanpa BQ)<br>_Nama Kelurahan_ → `Patient.address.extension.extension.valueCode` (30, tanpa BQ)<br>_Nama Pasien Bayi_ → `Patient.name` (1094, tanpa BQ)<br>_No KTP Bayi_ → `Patient.identifier.use` (1095, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (1098, tanpa BQ) |
| 2 | 69–82 | Practitioner | – | – | _Nama Dokter_ → `Practitioner.name` (72, tanpa BQ)<br>_Nama Pengkaji 1_ → `Practitioner.name` (77, tanpa BQ)<br>_Nama Pengkaji 2_ → `Practitioner.name` (82, tanpa BQ) |
| 3 | 84–103 | Encounter | – | – | _No Rawat_ → `Encounter.identifier` (84, tanpa BQ)<br>_Cara Masuk_ → `Encounter.hospitalization.admitSource.coding` (87, tanpa BQ)<br>_Tanggal_ → `Encounter.period.start` (98, tanpa BQ)<br>_No Rawat Bayi_ → `Encounter.identifier` (1050, tanpa BQ) |
| 4 | 104–112 | Condition | – | – | _Kode Diagnosis ICD10_ → `Condition.code.coding` (106, tanpa BQ)<br>_Deskripsi Diagnosis ICD10_ → `Condition.code.coding` (107, tanpa BQ) |
| 5 | 123–140 | EpisodeOfCare | ANC | Antenatal Care | – |
| 6 | 141–145 | EpisodeOfCare | PNC | Postnatal Care | – |
| 7 | 150–158 | Condition | 404684003.0 | Clinical finding | _Keluhan_ → `Condition.clinicalStatus.coding` (150, tanpa BQ) |
| 8 | 159–165 | FamilyMemberHistory | – | – | _Riwayat Penyakit Keluarga_ → `FamilyMemberHistory.status` (159, tanpa BQ) |
| 9 | 166–173 | Condition | 404684003.0 | Clinical finding | _Pemeriksaan Status Kesehatan_ → `Condition.clinicalStatus.coding` (166, tanpa BQ) |
| 10 | 174–181 | Condition | 417662000.0 | History of clinical finding in subject | _Riwayat Penyakit Pribadi_ → `Condition.clinicalStatus.coding` (174, tanpa BQ) |
| 11 | 182–190 | AllergyIntolerance | – | – | _Alergi_ → `AllergyIntolerance.clinicalStatus.coding` (182, tanpa BQ) |
| 12 | 191–205 | Observation | 450891000124109.0 | Past pregnancy history of complication of pregnancy, childbirth and/or puerperium | _Komplikasi Persalinan Sebelumnya_ → `Observation.valueBoolean` (194, tanpa BQ)<br>_Keterangan Komplikasi Persalinan Sebelumnya_ → `Observation.note.text` (205, tanpa BQ) |
| 13 | 227–238 | Observation | 11996-6 | [#] Pregnancies | _Riwayat Gravida_ → `Observation.valueInteger` (231, tanpa BQ) |
| 14 | 239–250 | Observation | 11977-6 | [#] Parity | _Riwayat Partus_ → `Observation.valueInteger` (243, tanpa BQ) |
| 15 | 251–262 | Observation | 69043-8 | Other pregnancy outcomes # | _Riwayat Abortus_ → `Observation.valueInteger` (255, tanpa BQ) |
| 16 | 263–273 | Observation | 726001007.0 | Past pregnancy history of live birth | _Riwayat Persalinan Hidup_ → `Observation.valueInteger` (266, tanpa BQ) |
| 17 | 274–285 | Observation | 8665-2 | Last menstrual period start date | _HPHT_ → `Observation.valueDateTime` (278, tanpa BQ) |
| 18 | 286–297 | Observation | 18185-9 | Gestational age | _Usia Kehamilan_ → `Observation.valueQuantity.value` (290, tanpa BQ) |
| 19 | 298–309 | Observation | 11778-8 | Delivery date Estimated | _HPL_ → `Observation.valueDateTime` (302, tanpa BQ) |
| 20 | 310–329 | Immunization | – | – | _Riwayat Imunisasi TT_ → `Immunization.status` (310, tanpa BQ) |
| 21 | 330–340 | Immunization | – | – | – |
| 22 | 341–351 | Observation | 3401000175105.0 | Total number of prenatal care visits | _Jumlah Kunjungan ANC_ → `Observation.valueInteger` (344, tanpa BQ) |
| 23 | 353–364 | Observation | 243826008.0 | Antenatal care status | _Keterangan Kunjungan ANC_ → `Observation.valueCodeableConcept.coding` (356, tanpa BQ) |
| 24 | 365–376 | Condition | 422587007.0 | Nausea | _Keluhan Hamil Muda_ → `Condition.clinicalStatus.coding` (365, tanpa BQ) |
| 25 | 378–387 | Condition | 422587007.0 | Nausea | _Keluhan Hamil Tua_ → `Condition.clinicalStatus.coding` (378, tanpa BQ) |
| 26 | 389–420 | Condition | 161805006.0 | Past pregnancy history of cesarean section | _Penyulit Kehamilan_ → `Condition.clinicalStatus.coding` (389, tanpa BQ) |
| 27 | 421–435 | Observation | 420209000.0 | History of contraceptive usage | _Riwayat KB_ → `Observation.valueCodeableConcept.coding` (424, tanpa BQ) |
| 28 | 437–449 | Observation | SP000644 | Komplikasi KB Sebelumnya | _Komplikasi KB Sebelumnya_ → `Observation.valueBoolean` (440, tanpa BQ)<br>_Keterangan Komplikasi KB Sebelumnya_ → `Observation.note` (442, tanpa BQ) |
| 29 | 451–461 | Observation | SP000645 | Alasan Berhenti KB | _Alasan Berhenti KB_ → `Observation.valueString` (454, tanpa BQ) |
| 30 | 462–476 | Condition | 56728002.0 | Chronic cervicitis | _Riwayat Ginekologi_ → `Condition.clinicalStatus.coding` (462, tanpa BQ) |
| 31 | 477–488 | MedicationStatement | – | – | _Kebiasaan Obat_ → `MedicationStatement.status` (477, tanpa BQ)<br>_Kebiasaan Keterangan Obat_ → `MedicationStatement.medicationCodeableConcept.text` (481, tanpa BQ) |
| 32 | 489–502 | Observation | 72166-2 | Tobacco smoking status | _Kebiasaan Merokok_ → `Observation.valueCodeableConcept.coding` (492, tanpa BQ)<br>_Kebiasaan Keterangan Merokok_ → `Observation.note.text` (502, tanpa BQ) |
| 33 | 503–515 | Observation | 11331-6 | History of Alcohol use | _Kebiasaan Alkohol_ → `Observation.valueCodeableConcept.coding` (506, tanpa BQ)<br>_Kebiasaan Keterangan Alkohol_ → `Observation.note.text` (515, tanpa BQ) |
| 34 | 517–532 | Observation | 67775-7 | Level of responsiveness | _Keadaan Mental_ → `Observation.valueCodeableConcept.coding` (520, tanpa BQ) |
| 35 | 533–546 | Observation | 75910-0 | Canadian triage and acuity scale [CTAS] | _Keadaan Umum_ → `Observation.valueCodeableConcept.coding` (536, tanpa BQ) |
| 36 | 547–558 | Observation | 9269-2 | Glasgow coma score total | _Glasgow Coma Scale_ → `Observation.valueQuantity.value` (551, tanpa BQ) |
| 37 | 560–572 | Observation | 8480-6 | Systolic blood pressure | _Tekanan Darah Sistol_ → `Observation.valueQuantity.value` (564, tanpa BQ) |
| 38 | 573–585 | Observation | 8462-4 | Diastolic blood pressure | _Tekanan Darah Diastol_ → `Observation.valueQuantity.value` (577, tanpa BQ) |
| 39 | 586–598 | Observation | 8867-4 | Heart Rate | _Nadi_ → `Observation.valueQuantity.value` (590, tanpa BQ) |
| 40 | 599–612 | Observation | 9279-1 | Respiratory rate | _Respiratory Rate_ → `Observation.valueQuantity.value` (603, tanpa BQ) |
| 41 | 613–625 | Observation | 8310-5 | Body temperature | _Suhu_ → `Observation.valueQuantity.value` (617, tanpa BQ) |
| 42 | 626–637 | Observation | 250554003.0 | Measurement of oxygen saturation at periphery | _Saturasi Oksigen_ → `Observation.valueQuantity.value` (629, tanpa BQ) |
| 43 | 638–650 | Observation | 29463-7 | Body weight | _Berat Badan_ → `Observation.valueQuantity.value` (642, tanpa BQ) |
| 44 | 651–663 | Observation | 8302-2 | Body height | _Tinggi Badan_ → `Observation.valueQuantity.value` (655, tanpa BQ) |
| 45 | 664–678 | Observation | 284473002.0 | Mid upper arm circumference | _LiLA_ → `Observation.status` (664, tanpa BQ) |
| 46 | 679–691 | Observation | 11881-0 | Uterus Fundal height Tape measure | _Tinggi Fundus_ → `Observation.valueQuantity.value` (683, tanpa BQ) |
| 47 | 692–707 | Observation | 89087-1 | Fetal Body weight Estimated | _Taksiran Berat Janin_ → `Observation.valueQuantity.value` (696, tanpa BQ)<br>_Presentasi_ → `Observation.identifier.value` (707, tanpa BQ) |
| 48 | 708–722 | Observation | 72155-5 | Position in womb Fetus [RHEA] | – |
| 49 | 723–743 | Observation | 57071-3 | Obstetric delivery method | _Cara Persalinan_ → `Observation.valueCodeableConcept.coding` (725, tanpa BQ)<br>_Penurunan_ → `Observation.identifier.value` (743, tanpa BQ) |
| 50 | 744–757 | Observation | 249111004.0 | Engagement of head | – |
| 51 | 758–778 | Observation | 249120008.0 | Onset of labor first stage | _Frekuensi HIS_ → `Observation.component.code.coding` (768, tanpa BQ)<br>_Kekuatan HIS_ → `Observation.component.code.coding` (771, tanpa BQ)<br>_Durasi HIS_ → `Observation.component.code.coding` (775, tanpa BQ)<br>_Denyut Jantung Janin_ → `Observation.status` (778, tanpa BQ) |
| 52 | 779–792 | Observation | 55283-6 | Fetal Heart rate | _Keterangan Denyut Jantung Janin_ → `Observation.identifier.value` (792, tanpa BQ) |
| 53 | 793–804 | Observation | 289437007.0 | Finding of fetal heart rate | _Portio_ → `Observation.status` (804, tanpa BQ) |
| 54 | 805–814 | Observation | 248910006.0 | Uterine cervix finding | – |
| 55 | 816–830 | Observation | 365662002.0 | Finding of amniotic fluid appearance | _Ketuban_ → `Observation.valueCodeableConcept.coding` (818, tanpa BQ) |
| 56 | 831–847 | Observation | 365662002.0 | Finding of amniotic fluid appearance | _Ketuban_ → `Observation.valueCodeableConcept.coding` (833, tanpa BQ)<br>_Hodge_ → `Observation.identifier.value` (847, tanpa BQ) |
| 57 | 848–865 | Observation | 249111004.0 | Engagement of head | _Inspekulo_ → `Observation.status` (865, tanpa BQ) |
| 58 | 866–878 | Observation | 32750006.0 | Inspection | _Keterangan Inspekulo_ → `Observation.note.text` (877, tanpa BQ)<br>_Pemeriksaan Lakmus Air Ketuban_ → `Observation.status` (878, tanpa BQ) |
| 59 | 879–890 | Observation | 424679001.0 | pH measurement, vaginal fluid | _Keterangan Pemeriksaan Lakmus Air Ketuban_ → `Observation.note.text` (890, tanpa BQ) |
| 60 | 892–902 | Procedure | 387672006.0 | Cardiotochogram | _Pemeriksaan Cardiotocography (CTG)_ → `Procedure.category.coding` (892, tanpa BQ) |
| 61 | 903–913 | Observation | 251666009.0 | Cardiotochogram finding | _Keterangan Pemeriksaan Cardiotocography (CTG)_ → `Observation.valueString` (906, tanpa BQ) |
| 62 | 1023–1031 | Condition | 404684003.0 | Clinical finding | _Masalah Kesehatan_ → `Condition.clinicalStatus.coding` (1023, tanpa BQ) |
| 63 | 1035–1049 | Procedure | – | – | _Kode Tindakan ICD9CM_ → `Procedure.code.coding` (1036, tanpa BQ)<br>_Deskripsi Tindakan ICD9CM_ → `Procedure.code.coding` (1037, tanpa BQ) |
| 64 | 1066–1073 | Condition | Z00.1 | Routine child health examination | – |
| 65 | 1084–1092 | EpisodeOfCare | Neonate | Neonate | – |
| 66 | 1100–1103 | RelatedPerson | – | – | _Nama Ayah_ → `RelatedPerson.patient` (1100, tanpa BQ) |
| 67 | 1105–1117 | Observation | 8339-4 | Birth weight Measured | _Berat Badan Lahir_ → `Observation.valueQuantity.value` (1109, tanpa BQ) |
| 68 | 1118–1130 | Observation | 89269-5 | Body height Measured --at birth | _Panjang Badan Lahir_ → `Observation.valueQuantity.value` (1122, tanpa BQ) |
| 69 | 1131–1142 | Observation | 169876006.0 | Birth head circumference | _Lingkar Kepala Lahir_ → `Observation.valueQuantity.value` (1134, tanpa BQ) |
| 70 | 1143–1153 | Observation | 365475008.0 | Place in family order | _Anak Ke-_ → `Observation.valueInteger` (1146, tanpa BQ) |
| 71 | 1154–1164 | Observation | 93857-1 | Date and time of obstetric delivery | _Jam Lahir_ → `Observation.valueDateTime` (1157, tanpa BQ) |
| 72 | 1171–1182 | Observation | 3941000175104.0 | Birth abdominal circumference | _Lingkar Perut Lahir_ → `Observation.valueQuantity.value` (1174, tanpa BQ) |
| 73 | 1183–1194 | Observation | 3931000175105.0 | Birth chest circumference | _Lingkar Dada Lahir_ → `Observation.valueQuantity.value` (1186, tanpa BQ) |
| 74 | 1196–1207 | Observation | 11996-6 | [#] Pregnancies | _Gravida_ → `Observation.valueInteger` (1200, tanpa BQ) |
| 75 | 1208–1219 | Observation | 11977-6 | [#] Parity | _Partus_ → `Observation.valueInteger` (1212, tanpa BQ) |
| 76 | 1220–1231 | Observation | 69043-8 | Other pregnancy outcomes # | _Abortus_ → `Observation.valueInteger` (1224, tanpa BQ) |
| 77 | 1232–1266 | Observation | 9272-6 | 1 minute Apgar Score | _Nilai APGAR 1_ → `Observation.valueQuantity.value` (1235, tanpa BQ)<br>_Appearance 1_ → `Observation.component.code.coding` (1247, tanpa BQ)<br>_Pulse 1_ → `Observation.component.code.coding` (1251, tanpa BQ)<br>_Grimance 1_ → `Observation.component.code.coding` (1255, tanpa BQ)<br>_Activity 1_ → `Observation.component.code.coding` (1259, tanpa BQ)<br>_Respiration 1_ → `Observation.component.code.coding` (1263, tanpa BQ) |
| 78 | 1267–1301 | Observation | 9274-2 | 5 minute Apgar Score | _Nilai APGAR 5_ → `Observation.valueQuantity.value` (1270, tanpa BQ)<br>_Appearance 5_ → `Observation.component.code.coding` (1282, tanpa BQ)<br>_Pulse 5_ → `Observation.component.code.coding` (1286, tanpa BQ)<br>_Grimance 5_ → `Observation.component.code.coding` (1290, tanpa BQ)<br>_Activity 5_ → `Observation.component.code.coding` (1294, tanpa BQ)<br>_Respiration 5_ → `Observation.component.code.coding` (1298, tanpa BQ) |
| 79 | 1302–1336 | Observation | 9271-8 | 10 minute Apgar Score | _Nilai APGAR 10_ → `Observation.valueQuantity.value` (1305, tanpa BQ)<br>_Appearance 10_ → `Observation.component.code.coding` (1317, tanpa BQ)<br>_Pulse 10_ → `Observation.component.code.coding` (1321, tanpa BQ)<br>_Grimance 10_ → `Observation.component.code.coding` (1325, tanpa BQ)<br>_Activity 10_ → `Observation.component.code.coding` (1329, tanpa BQ)<br>_Respiration 10_ → `Observation.component.code.coding` (1333, tanpa BQ) |
| 80 | 1337–1347 | Procedure | 386412000.0 | Resuscitation of neonate | – |
| 81 | 1348–1357 | Procedure | 448883004.0 | Injection of vitamin K1 | _Obat Diberikan_ → `Procedure.category.coding` (1348, tanpa BQ) |
| 82 | 1358–1367 | Procedure | PC000002 | Pemberian Salep Antibiotik Mata | – |
| 83 | 1368–1382 | Immunization | – | – | – |
| 84 | 1383–1394 | Immunization | – | – | – |
| 85 | 1395–1406 | Observation | 249278006.0 | Ability to pass urine | – |
| 86 | 1407–1418 | Observation | 276397000.0 | Has passed meconium | – |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 57 |
| Condition | 10 |
| Procedure | 5 |
| Immunization | 4 |
| EpisodeOfCare | 3 |
| Patient | 1 |
| Practitioner | 1 |
| Encounter | 1 |
| FamilyMemberHistory | 1 |
| AllergyIntolerance | 1 |
| MedicationStatement | 1 |
| RelatedPerson | 1 |
| **Total** | **86** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 87 | Encounter | `Encounter.hospitalization.admitSource.coding` | emd | From accident/emergency department | http://terminology.hl7.org/CodeSystem/admit-source |
| 2 | 88 | Encounter | `Encounter.hospitalization.admitSource.coding` | outp | From outpatient department | http://terminology.hl7.org/CodeSystem/admit-source |
| 3 | 89 | Encounter | `Encounter.hospitalization.admitSource.coding` | other | Other | http://terminology.hl7.org/CodeSystem/admit-source |
| 4 | 131 | EpisodeOfCare | `EpisodeOfCare.type.coding` | ANC | Antenatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 5 | 141 | EpisodeOfCare | `EpisodeOfCare.type.coding` | PNC | Postnatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 6 | 152 | Condition | `Condition.code.coding` | 404684003.0 | Clinical finding | http://snomed.info/sct |
| 7 | 168 | Condition | `Condition.code.coding` | 404684003.0 | Clinical finding | http://snomed.info/sct |
| 8 | 176 | Condition | `Condition.code.coding` | 417662000.0 | History of clinical finding in subject | http://snomed.info/sct |
| 9 | 193 | Observation | `Observation.code.coding` | 450891000124109.0 | Past pregnancy history of complication of pregnancy, childbirth and/or puerperium | http://snomed.info/sct |
| 10 | 196 | Observation | `Observation.component.code.coding` | 161809000.0 | Past pregnancy history of postpartum hemorrhage | http://snomed.info/sct |
| 11 | 199 | Observation | `Observation.component.code.coding` | 161806007.0 | Past pregnancy history of eclampsia | http://snomed.info/sct |
| 12 | 202 | Observation | `Observation.component.code.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 13 | 229 | Observation | `Observation.code.coding` | 11996-6 | [#] Pregnancies | http://loinc.org |
| 14 | 230 | Observation | `Observation.code.coding` | ANC.B6.DE24 | Number of pregnancies (gravida) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 15 | 241 | Observation | `Observation.code.coding` | 11977-6 | [#] Parity | http://loinc.org |
| 16 | 242 | Observation | `Observation.code.coding` | ANC.B6.DE32 | Parity | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 17 | 253 | Observation | `Observation.code.coding` | 69043-8 | Other pregnancy outcomes # | http://loinc.org |
| 18 | 254 | Observation | `Observation.code.coding` | ANC.B6.DE25 | Number of miscarriages and/or abortions | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 19 | 265 | Observation | `Observation.code.coding` | 726001007.0 | Past pregnancy history of live birth | http://snomed.info/sct |
| 20 | 276 | Observation | `Observation.code.coding` | 8665-2 | Last menstrual period start date | http://loinc.org |
| 21 | 277 | Observation | `Observation.code.coding` | ANC.B6.DE14 | Last menstrual period (LMP) date | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 22 | 288 | Observation | `Observation.code.coding` | 18185-9 | Gestational age | http://loinc.org |
| 23 | 289 | Observation | `Observation.code.coding` | ANC.B6.DE17 | Gestational age | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 24 | 300 | Observation | `Observation.code.coding` | 11778-8 | Delivery date Estimated | http://loinc.org |
| 25 | 301 | Observation | `Observation.code.coding` | ANC.B6.DE22 | Expected date of delivery (EDD) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 26 | 312 | Immunization | `Immunization.vaccineCode` | VG139 | Td | http://sys-ids.kemkes.go.id/kfa |
| 27 | 330 | Immunization | `Immunization.vaccineCode` | VG139 | Td | http://sys-ids.kemkes.go.id/kfa |
| 28 | 343 | Observation | `Observation.code.coding` | 3401000175105.0 | Total number of prenatal care visits | http://snomed.info/sct |
| 29 | 355 | Observation | `Observation.code.coding` | 243826008.0 | Antenatal care status | http://snomed.info/sct |
| 30 | 356 | Observation | `Observation.valueCodeableConcept.coding` | 17854005.0 | Regular | http://snomed.info/sct |
| 31 | 357 | Observation | `Observation.valueCodeableConcept.coding` | 49608001.0 | Irregular | http://snomed.info/sct |
| 32 | 368 | Condition | `Condition.code.coding` | 422587007.0 | Nausea | http://snomed.info/sct |
| 33 | 369 | Condition | `Condition.code.coding` | 422400008.0 | Vomiting | http://snomed.info/sct |
| 34 | 370 | Condition | `Condition.code.coding` | 289530006.0 | Vaginal bleeding | http://snomed.info/sct |
| 35 | 371 | Condition | `Condition.code.coding` | 413320001.0 | Physical health problem | http://snomed.info/sct |
| 36 | 381 | Condition | `Condition.code.coding` | 422587007.0 | Nausea | http://snomed.info/sct |
| 37 | 382 | Condition | `Condition.code.coding` | 413320001.0 | Physical health problem | http://snomed.info/sct |
| 38 | 391 | Condition | `Condition.code.coding` | 161805006.0 | Past pregnancy history of cesarean section | http://snomed.info/sct |
| 39 | 392 | Condition | `Condition.code.coding` | 10741751000119100 | Anemia in mother complicating childbirth | http://snomed.info/sct |
| 40 | 393 | Condition | `Condition.code.coding` | 199746004.0 | Obstructed labor | http://snomed.info/sct |
| 41 | 394 | Condition | `Condition.code.coding` | 48194001.0 | Pregnancy-induced hypertension | http://snomed.info/sct |
| 42 | 395 | Condition | `Condition.code.coding` | 38010008.0 | Intrapartum hemorrhage | http://snomed.info/sct |
| 43 | 396 | Condition | `Condition.code.coding` | 40733004.0 | Infectious disease | http://snomed.info/sct |
| 44 | 397 | Condition | `Condition.code.coding` | 386639001.0 | Termination of pregnancy | http://snomed.info/sct |
| 45 | 398 | Condition | `Condition.code.coding` | 44223004.0 | Premature rupture of membranes | http://snomed.info/sct |
| 46 | 399 | Condition | `Condition.code.coding` | 38341003.0 | Hypertensive disorder, systemic arterial | http://snomed.info/sct |
| 47 | 400 | Condition | `Condition.code.coding` | 398254007.0 | Pre-eclampsia | http://snomed.info/sct |
| 48 | 401 | Condition | `Condition.code.coding` | 15938005.0 | Eclampsia | http://snomed.info/sct |
| 49 | 402 | Condition | `Condition.code.coding` | 9293002.0 | Atony of uterus | http://snomed.info/sct |
| 50 | 403 | Condition | `Condition.code.coding` | 283380005.0 | Laceration of perineum | http://snomed.info/sct |
| 51 | 404 | Condition | `Condition.code.coding` | 199745000.0 | Complication occurring during labor and delivery | http://snomed.info/sct |
| 52 | 405 | Condition | `Condition.code.coding` | 161805006.0 | Past pregnancy history of cesarean section | http://snomed.info/sct |
| 53 | 406 | Condition | `Condition.code.coding` | 59566000.0 | Oligohydramnios | http://snomed.info/sct |
| 54 | 407 | Condition | `Condition.code.coding` | 53443007.0 | Prolonged labor | http://snomed.info/sct |
| 55 | 408 | Condition | `Condition.code.coding` | 1365934004.0 | Failed attempted induction of labor | http://snomed.info/sct |
| 56 | 409 | Condition | `Condition.code.coding` | 130955003.0 | Fetal distress | http://snomed.info/sct |
| 57 | 410 | Condition | `Condition.code.coding` | 199747008.0 | Obstructed labor due to fetal malposition | http://snomed.info/sct |
| 58 | 411 | Condition | `Condition.code.coding` | 199397009.0 | Cephalopelvic disproportion | http://snomed.info/sct |
| 59 | 412 | Condition | `Condition.code.coding` | 371380006.0 | Amniotic fluid leaking | http://snomed.info/sct |
| 60 | 413 | Condition | `Condition.code.coding` | 433068007.0 | Aneurysm of thoracic aorta | http://snomed.info/sct |
| 61 | 414 | Condition | `Condition.code.coding` | 38206000.0 | Exceptionally large at birth | http://snomed.info/sct |
| 62 | 415 | Condition | `Condition.code.coding` | 740597009.0 | Umbilical cord complication during labor and delivery | http://snomed.info/sct |
| 63 | 423 | Observation | `Observation.code.coding` | 420209000.0 | History of contraceptive usage | http://snomed.info/sct |
| 64 | 424 | Observation | `Observation.valueCodeableConcept.coding` | 161772002.0 | History of oral contraceptive usage | http://snomed.info/sct |
| 65 | 425 | Observation | `Observation.valueCodeableConcept.coding` | 473093002.0 | History of use of depot contraception | http://snomed.info/sct |
| 66 | 426 | Observation | `Observation.valueCodeableConcept.coding` | 161773007.0 | History of intrauterine contraceptive device usage | http://snomed.info/sct |
| 67 | 427 | Observation | `Observation.valueCodeableConcept.coding` | 267020005.0 | History of tubal ligation | http://snomed.info/sct |
| 68 | 428 | Observation | `Observation.valueCodeableConcept.coding` | 473387004.0 | Never used contraception | http://snomed.info/sct |
| 69 | 439 | Observation | `Observation.code.coding` | SP000644 | Komplikasi KB Sebelumnya | http://terminology.kemkes.go.id/sp |
| 70 | 453 | Observation | `Observation.code.coding` | SP000645 | Alasan Berhenti KB | http://terminology.kemkes.go.id/sp |
| 71 | 464 | Condition | `Condition.code.coding` | 56728002.0 | Chronic cervicitis | http://snomed.info/sct |
| 72 | 465 | Condition | `Condition.code.coding` | 129103003.0 | Endometriosis | http://snomed.info/sct |
| 73 | 466 | Condition | `Condition.code.coding` | 6738008.0 | Female infertility | http://snomed.info/sct |
| 74 | 467 | Condition | `Condition.code.coding` | 371973000.0 | Malignant neoplasm of uterus | http://snomed.info/sct |
| 75 | 468 | Condition | `Condition.code.coding` | 1156875002.0 | Myoma | http://snomed.info/sct |
| 76 | 469 | Condition | `Condition.code.coding` | 8098009.0 | Sexually transmitted infectious disease | http://snomed.info/sct |
| 77 | 470 | Condition | `Condition.code.coding` | 65576009.0 | Polyp of cervix | http://snomed.info/sct |
| 78 | 471 | Condition | `Condition.code.coding` | 267011001.0 | Gynecological history | http://snomed.info/sct |
| 79 | 491 | Observation | `Observation.code.coding` | 72166-2 | Tobacco smoking status | http://loinc.org |
| 80 | 492 | Observation | `Observation.valueCodeableConcept.coding` | 8392000.0 | Non-smoker | http://snomed.info/sct |
| 81 | 493 | Observation | `Observation.valueCodeableConcept.coding` | 43381005.0 | Passive smoker | http://snomed.info/sct |
| 82 | 494 | Observation | `Observation.valueCodeableConcept.coding` | 77176002.0 | Smoker | http://snomed.info/sct |
| 83 | 505 | Observation | `Observation.code.coding` | 11331-6 | History of Alcohol use | http://loinc.org |
| 84 | 506 | Observation | `Observation.valueCodeableConcept.coding` | 105542008.0 | Non - drinker | http://snomed.info/sct |
| 85 | 507 | Observation | `Observation.valueCodeableConcept.coding` | 219006.0 | Current drinker | http://snomed.info/sct |
| 86 | 519 | Observation | `Observation.code.coding` | 67775-7 | Level of responsiveness | http://loinc.org |
| 87 | 520 | Observation | `Observation.valueCodeableConcept.coding` | 248234008.0 | Mentally alert | http://snomed.info/sct |
| 88 | 521 | Observation | `Observation.valueCodeableConcept.coding` | 300202002.0 | Response to voice | http://snomed.info/sct |
| 89 | 522 | Observation | `Observation.valueCodeableConcept.coding` | 450847001.0 | Response to pain | http://snomed.info/sct |
| 90 | 523 | Observation | `Observation.valueCodeableConcept.coding` | 422768004.0 | Unresponsive | http://snomed.info/sct |
| 91 | 524 | Observation | `Observation.valueCodeableConcept.coding` | 130987000.0 | Acute confusion | http://snomed.info/sct |
| 92 | 525 | Observation | `Observation.valueCodeableConcept.coding` | 2776000.0 | Delirium | http://snomed.info/sct |
| 93 | 535 | Observation | `Observation.code.coding` | 75910-0 | Canadian triage and acuity scale [CTAS] | http://loinc.org |
| 94 | 536 | Observation | `Observation.valueCodeableConcept.coding` | LA10137-0 | 5.0 | http://loinc.org |
| 95 | 538 | Observation | `Observation.valueCodeableConcept.coding` | LA6115-5 | 4.0 | http://loinc.org |
| 96 | 549 | Observation | `Observation.code.coding` | 9269-2 | Glasgow coma score total | http://loinc.org |
| 97 | 562 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 98 | 563 | Observation | `Observation.code.coding` | ANC.B8.DE17 | Systolic blood pressure | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 99 | 575 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://loinc.org |
| 100 | 576 | Observation | `Observation.code.coding` | ANC.B8.DE19 | Diastolic blood pressure | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 101 | 588 | Observation | `Observation.code.coding` | 8867-4 | Heart Rate | http://loinc.org |
| 102 | 589 | Observation | `Observation.code.coding` | ANC.B8.DE36 | Pulse rate | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 103 | 601 | Observation | `Observation.code.coding` | 9279-1 | Respiratory rate | http://loinc.org |
| 104 | 602 | Observation | `Observation.code.coding` | ANC.SS.DE2 | Pernapasan | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 105 | 615 | Observation | `Observation.code.coding` | 8310-5 | Body temperature | http://loinc.org |
| 106 | 616 | Observation | `Observation.code.coding` | ANC.B8.DE34 | Body temperature | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 107 | 628 | Observation | `Observation.code.coding` | 250554003.0 | Measurement of oxygen saturation at periphery | http://snomed.info/sct |
| 108 | 640 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 109 | 641 | Observation | `Observation.code.coding` | ANC.B8.DE3 | Current weight | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 110 | 653 | Observation | `Observation.code.coding` | 8302-2 | Body height | http://loinc.org |
| 111 | 654 | Observation | `Observation.code.coding` | ANC.B8.DE1 | Height | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 112 | 666 | Observation | `Observation.code.coding` | 284473002.0 | Mid upper arm circumference | http://snomed.info/sct |
| 113 | 667 | Observation | `Observation.code.coding` | ANC.SS.DE3 | Lingkar Lengan Atas (LILA) | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 114 | 676 | Observation | `Observation.interpretation` | OI000018 | Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 115 | 677 | Observation | `Observation.interpretation` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 116 | 678 | Observation | `Observation.interpretation` | OI000035 | Risiko Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 117 | 681 | Observation | `Observation.code.coding` | 11881-0 | Uterus Fundal height Tape measure | http://loinc.org |
| 118 | 682 | Observation | `Observation.code.coding` | ANC.B8.DE105 | Symphysis-fundal height | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 119 | 694 | Observation | `Observation.code.coding` | 89087-1 | Fetal Body weight Estimated | http://loinc.org |
| 120 | 695 | Observation | `Observation.code.coding` | ANC.SS.DE1 | Taksiran Berat Janin (TBJ) | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 121 | 709 | Observation | `Observation.code.coding` | 72155-5 | Position in womb Fetus [RHEA] | http://loinc.org |
| 122 | 710 | Observation | `Observation.valueCodeableConcept.coding` | 1209182005.0 | Cephalic fetal presentation | http://snomed.info/sct |
| 123 | 711 | Observation | `Observation.valueCodeableConcept.coding` | 1209182005.0 | Cephalic fetal presentation | http://snomed.info/sct |
| 124 | 712 | Observation | `Observation.valueCodeableConcept.coding` | 1209182005.0 | Cephalic fetal presentation | http://snomed.info/sct |
| 125 | 713 | Observation | `Observation.valueCodeableConcept.coding` | 8017000.0 | Face presentation | http://snomed.info/sct |
| 126 | 714 | Observation | `Observation.valueCodeableConcept.coding` | 249097002.0 | Footling breech presentation | http://snomed.info/sct |
| 127 | 715 | Observation | `Observation.valueCodeableConcept.coding` | 124736009.0 | Compound presentation | http://snomed.info/sct |
| 128 | 724 | Observation | `Observation.code.coding` | 57071-3 | Obstetric delivery method | http://loinc.org |
| 129 | 725 | Observation | `Observation.valueCodeableConcept.coding` | 48782003.0 | Delivery normal | http://snomed.info/sct |
| 130 | 726 | Observation | `Observation.valueCodeableConcept.coding` | 200138003.0 | Vacuum extractor delivery - delivered | http://snomed.info/sct |
| 131 | 727 | Observation | `Observation.valueCodeableConcept.coding` | 200130005.0 | Forceps delivery - delivered | http://snomed.info/sct |
| 132 | 728 | Observation | `Observation.valueCodeableConcept.coding` | 200144004.0 | Deliveries by cesarean | http://snomed.info/sct |
| 133 | 745 | Observation | `Observation.code.coding` | 249111004.0 | Engagement of head | http://snomed.info/sct |
| 134 | 746 | Observation | `Observation.valueCodeableConcept.coding` | 249112006.0 | Head engaged | http://snomed.info/sct |
| 135 | 748 | Observation | `Observation.valueCodeableConcept.coding` | 62098001.0 | Head not engaged | http://snomed.info/sct |
| 136 | 759 | Observation | `Observation.code.coding` | 249120008.0 | Onset of labor first stage | http://snomed.info/sct |
| 137 | 768 | Observation | `Observation.component.code.coding` | 364270005.0 | Frequency of uterine contraction | http://snomed.info/sct |
| 138 | 771 | Observation | `Observation.component.code.coding` | 398143009.0 | Uterine contraction monitoring | http://snomed.info/sct |
| 139 | 772 | Observation | `Observation.component.valueCodeableConcept.coding` | 289719005.0 | Strong uterine contractions | http://snomed.info/sct |
| 140 | 773 | Observation | `Observation.component.valueCodeableConcept.coding` | 289716003.0 | Moderate uterine contractions | http://snomed.info/sct |
| 141 | 774 | Observation | `Observation.component.valueCodeableConcept.coding` | 289715004.0 | Mild uterine contractions | http://snomed.info/sct |
| 142 | 775 | Observation | `Observation.component.code.coding` | 364274001.0 | Duration of uterine contraction | http://snomed.info/sct |
| 143 | 780 | Observation | `Observation.code.coding` | 55283-6 | Fetal Heart rate | http://loinc.org |
| 144 | 781 | Observation | `Observation.code.coding` | ANC.B8.DE107 | Fetal heart rate | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 145 | 794 | Observation | `Observation.code.coding` | 289437007.0 | Finding of fetal heart rate | http://snomed.info/sct |
| 146 | 795 | Observation | `Observation.valueCodeableConcept.coding` | 289441006.0 | Normal fetal heart rate | http://snomed.info/sct |
| 147 | 796 | Observation | `Observation.valueCodeableConcept.coding` | 312668007.0 | Abnormal fetal heart rate | http://snomed.info/sct |
| 148 | 806 | Observation | `Observation.code.coding` | 248910006.0 | Uterine cervix finding | http://loinc.org |
| 149 | 817 | Observation | `Observation.code.coding` | 365662002.0 | Finding of amniotic fluid appearance | http://snomed.info/sct |
| 150 | 818 | Observation | `Observation.valueCodeableConcept.coding` | 168090003.0 | Amniotic fluid clear | http://snomed.info/sct |
| 151 | 819 | Observation | `Observation.valueCodeableConcept.coding` | 408781009.0 | Straw colored amniotic fluid | http://snomed.info/sct |
| 152 | 820 | Observation | `Observation.valueCodeableConcept.coding` | 249134008.0 | Bloodstained liquor | http://snomed.info/sct |
| 153 | 821 | Observation | `Observation.valueCodeableConcept.coding` | 168092006.0 | Amniotic fluid -meconium stain | http://snomed.info/sct |
| 154 | 832 | Observation | `Observation.code.coding` | 365662002.0 | Finding of amniotic fluid appearance | http://snomed.info/sct |
| 155 | 833 | Observation | `Observation.valueCodeableConcept.coding` | 168090003.0 | Amniotic fluid clear | http://snomed.info/sct |
| 156 | 834 | Observation | `Observation.valueCodeableConcept.coding` | 408781009.0 | Straw colored amniotic fluid | http://snomed.info/sct |
| 157 | 835 | Observation | `Observation.valueCodeableConcept.coding` | 249134008.0 | Bloodstained liquor | http://snomed.info/sct |
| 158 | 836 | Observation | `Observation.valueCodeableConcept.coding` | 168092006.0 | Amniotic fluid -meconium stain | http://snomed.info/sct |
| 159 | 849 | Observation | `Observation.code.coding` | 249111004.0 | Engagement of head | http://snomed.info/sct |
| 160 | 850 | Observation | `Observation.valueCodeableConcept.coding` | 249112006.0 | Head engaged | http://snomed.info/sct |
| 161 | 852 | Observation | `Observation.valueCodeableConcept.coding` | 62098001.0 | Head not engaged | http://snomed.info/sct |
| 162 | 867 | Observation | `Observation.code.coding` | 32750006.0 | Inspection | http://snomed.info/sct |
| 163 | 880 | Observation | `Observation.code.coding` | 424679001.0 | pH measurement, vaginal fluid | http://snomed.info/sct |
| 164 | 893 | Procedure | `Procedure.code.coding` | 387672006.0 | Cardiotochogram | http://snomed.info/sct |
| 165 | 905 | Observation | `Observation.code.coding` | 251666009.0 | Cardiotochogram finding | http://snomed.info/sct |
| 166 | 1025 | Condition | `Condition.code.coding` | 404684003.0 | Clinical finding | http://snomed.info/sct |
| 167 | 1053 | Encounter | `Encounter.hospitalization.admitSource.coding` | born | Born in hospital | http://terminology.hl7.org/CodeSystem/admit-source |
| 168 | 1068 | Condition | `Condition.code.coding` | Z00.1 | Routine child health examination | http://hl7.org/fhir/sid/icd-10 |
| 169 | 1088 | EpisodeOfCare | `EpisodeOfCare.type.coding` | Neonate | Neonate | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 170 | 1108 | Observation | `Observation.code.coding` | 8339-4 | Birth weight Measured | http://loinc.org |
| 171 | 1121 | Observation | `Observation.code.coding` | 89269-5 | Body height Measured --at birth | http://loinc.org |
| 172 | 1133 | Observation | `Observation.code.coding` | 169876006.0 | Birth head circumference | http://snomed.info/sct |
| 173 | 1145 | Observation | `Observation.code.coding` | 365475008.0 | Place in family order | http://snomed.info/sct |
| 174 | 1156 | Observation | `Observation.code.coding` | 93857-1 | Date and time of obstetric delivery | http://loinc.org |
| 175 | 1173 | Observation | `Observation.code.coding` | 3941000175104.0 | Birth abdominal circumference | http://snomed.info/sct |
| 176 | 1185 | Observation | `Observation.code.coding` | 3931000175105.0 | Birth chest circumference | http://snomed.info/sct |
| 177 | 1198 | Observation | `Observation.code.coding` | 11996-6 | [#] Pregnancies | http://loinc.org |
| 178 | 1199 | Observation | `Observation.code.coding` | ANC.B6.DE24 | Number of pregnancies (gravida) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 179 | 1210 | Observation | `Observation.code.coding` | 11977-6 | [#] Parity | http://loinc.org |
| 180 | 1211 | Observation | `Observation.code.coding` | ANC.B6.DE32 | Parity | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 181 | 1222 | Observation | `Observation.code.coding` | 69043-8 | Other pregnancy outcomes # | http://loinc.org |
| 182 | 1223 | Observation | `Observation.code.coding` | ANC.B6.DE25 | Number of miscarriages and/or abortions | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 183 | 1234 | Observation | `Observation.code.coding` | 9272-6 | 1 minute Apgar Score | http://loinc.org |
| 184 | 1244 | Observation | `Observation.interpretation.coding` | 57284007.0 | Severe birth asphyxia | http://snomed.info/sct |
| 185 | 1245 | Observation | `Observation.interpretation.coding` | 77362009.0 | Mild to moderate birth asphyxia | http://snomed.info/sct |
| 186 | 1246 | Observation | `Observation.interpretation.coding` | 275307002.0 | Apgar normal | http://snomed.info/sct |
| 187 | 1247 | Observation | `Observation.component.code.coding` | 32406-1 | 1 minute Apgar Color | http://loinc.org |
| 188 | 1248 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6722-8 | The baby's whole body is completely bluish-gray or pale | http://loinc.org |
| 189 | 1249 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6723-6 | Good color in body with bluish hands or feet | http://loinc.org |
| 190 | 1250 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6724-4 | Good color all over | http://loinc.org |
| 191 | 1251 | Observation | `Observation.component.code.coding` | 32407-9 | 1 minute Apgar Heart rate | http://loinc.org |
| 192 | 1252 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6716-0 | No heart rate | http://loinc.org |
| 193 | 1253 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6717-8 | Fewer than 100 beats per minute | http://loinc.org |
| 194 | 1254 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6718-6 | At least 100 beats per minute | http://loinc.org |
| 195 | 1255 | Observation | `Observation.component.code.coding` | 32409-5 | 1 minute Apgar Reflex irritability | http://loinc.org |
| 196 | 1256 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6719-4 | No response to airways being suctioned | http://loinc.org |
| 197 | 1257 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6720-2 | Grimace during suctioning | http://loinc.org |
| 198 | 1258 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6721-0 | Grimace and pulling away, cough, or sneeze during suctioning | http://loinc.org |
| 199 | 1259 | Observation | `Observation.component.code.coding` | 32408-7 | 1 minute Apgar Muscle tone | http://loinc.org |
| 200 | 1260 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6713-7 | Limp; no movement | http://loinc.org |
| 201 | 1261 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6714-5 | Some flexion of arms and legs | http://loinc.org |
| 202 | 1262 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6715-2 | Active motion | http://loinc.org |
| 203 | 1263 | Observation | `Observation.component.code.coding` | 32410-3 | 1 minute Apgar Respiratory effort | http://loinc.org |
| 204 | 1264 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6725-1 | Not breathing | http://loinc.org |
| 205 | 1265 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6726-9 | Weak cry; may sound like whimpering, slow or irregular breathing | http://loinc.org |
| 206 | 1266 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6727-7 | Good, strong cry; normal rate and effort of breathing | http://loinc.org |
| 207 | 1269 | Observation | `Observation.code.coding` | 9274-2 | 5 minute Apgar Score | http://loinc.org |
| 208 | 1279 | Observation | `Observation.interpretation.coding` | 57284007.0 | Severe birth asphyxia | http://snomed.info/sct |
| 209 | 1280 | Observation | `Observation.interpretation.coding` | 77362009.0 | Mild to moderate birth asphyxia | http://snomed.info/sct |
| 210 | 1281 | Observation | `Observation.interpretation.coding` | 275307002.0 | Apgar normal | http://snomed.info/sct |
| 211 | 1282 | Observation | `Observation.component.code.coding` | 32411-1 | 5 minute Apgar Color | http://loinc.org |
| 212 | 1283 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6722-8 | The baby's whole body is completely bluish-gray or pale | http://loinc.org |
| 213 | 1284 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6723-6 | Good color in body with bluish hands or feet | http://loinc.org |
| 214 | 1285 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6724-4 | Good color all over | http://loinc.org |
| 215 | 1286 | Observation | `Observation.component.code.coding` | 32412-9 | 5 minute Apgar Heart rate | http://loinc.org |
| 216 | 1287 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6716-0 | No heart rate | http://loinc.org |
| 217 | 1288 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6717-8 | Fewer than 100 beats per minute | http://loinc.org |
| 218 | 1289 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6718-6 | At least 100 beats per minute | http://loinc.org |
| 219 | 1290 | Observation | `Observation.component.code.coding` | 32414-5 | 5 minute Apgar Reflex irritability | http://loinc.org |
| 220 | 1291 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6719-4 | No response to airways being suctioned | http://loinc.org |
| 221 | 1292 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6720-2 | Grimace during suctioning | http://loinc.org |
| 222 | 1293 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6721-0 | Grimace and pulling away, cough, or sneeze during suctioning | http://loinc.org |
| 223 | 1294 | Observation | `Observation.component.code.coding` | 32413-7 | 5 minute Apgar Muscle tone | http://loinc.org |
| 224 | 1295 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6713-7 | Limp; no movement | http://loinc.org |
| 225 | 1296 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6714-5 | Some flexion of arms and legs | http://loinc.org |
| 226 | 1297 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6715-2 | Active motion | http://loinc.org |
| 227 | 1298 | Observation | `Observation.component.code.coding` | 32415-2 | 5 minute Apgar Respiratory effort | http://loinc.org |
| 228 | 1299 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6725-1 | Not breathing | http://loinc.org |
| 229 | 1300 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6726-9 | Weak cry; may sound like whimpering, slow or irregular breathing | http://loinc.org |
| 230 | 1301 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6727-7 | Good, strong cry; normal rate and effort of breathing | http://loinc.org |
| 231 | 1304 | Observation | `Observation.code.coding` | 9271-8 | 10 minute Apgar Score | http://loinc.org |
| 232 | 1314 | Observation | `Observation.interpretation.coding` | 57284007.0 | Severe birth asphyxia | http://snomed.info/sct |
| 233 | 1315 | Observation | `Observation.interpretation.coding` | 77362009.0 | Mild to moderate birth asphyxia | http://snomed.info/sct |
| 234 | 1316 | Observation | `Observation.interpretation.coding` | 275307002.0 | Apgar normal | http://snomed.info/sct |
| 235 | 1317 | Observation | `Observation.component.code.coding` | 32401-2 | 10 minute Apgar Color | http://loinc.org |
| 236 | 1318 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6722-8 | The baby's whole body is completely bluish-gray or pale | http://loinc.org |
| 237 | 1319 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6723-6 | Good color in body with bluish hands or feet | http://loinc.org |
| 238 | 1320 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6724-4 | Good color all over | http://loinc.org |
| 239 | 1321 | Observation | `Observation.component.code.coding` | 32402-0 | 10 minute Apgar Heart rate | http://loinc.org |
| 240 | 1322 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6716-0 | No heart rate | http://loinc.org |
| 241 | 1323 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6717-8 | Fewer than 100 beats per minute | http://loinc.org |
| 242 | 1324 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6718-6 | At least 100 beats per minute | http://loinc.org |
| 243 | 1325 | Observation | `Observation.component.code.coding` | 32404-6 | 10 minute Apgar Reflex irritability | http://loinc.org |
| 244 | 1326 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6719-4 | No response to airways being suctioned | http://loinc.org |
| 245 | 1327 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6720-2 | Grimace during suctioning | http://loinc.org |
| 246 | 1328 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6721-0 | Grimace and pulling away, cough, or sneeze during suctioning | http://loinc.org |
| 247 | 1329 | Observation | `Observation.component.code.coding` | 32403-8 | 10 minute Apgar Muscle tone | http://loinc.org |
| 248 | 1330 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6713-7 | Limp; no movement | http://loinc.org |
| 249 | 1331 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6714-5 | Some flexion of arms and legs | http://loinc.org |
| 250 | 1332 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6715-2 | Active motion | http://loinc.org |
| 251 | 1333 | Observation | `Observation.component.code.coding` | 32405-3 | 10 minute Apgar Respiratory effort | http://loinc.org |
| 252 | 1334 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6725-1 | Not breathing | http://loinc.org |
| 253 | 1335 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6726-9 | Weak cry; may sound like whimpering, slow or irregular breathing | http://loinc.org |
| 254 | 1336 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6727-7 | Good, strong cry; normal rate and effort of breathing | http://loinc.org |
| 255 | 1338 | Procedure | `Procedure.code.coding` | 386412000.0 | Resuscitation of neonate | http://snomed.info/sct |
| 256 | 1350 | Procedure | `Procedure.code.coding` | 448883004.0 | Injection of vitamin K1 | http://snomed.info/sct |
| 257 | 1360 | Procedure | `Procedure.code.coding` | PC000002 | Pemberian Salep Antibiotik Mata | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 258 | 1370 | Immunization | `Immunization.vaccineCode` | VG45 | HepB | http://sys-ids.kemkes.go.id/kfa |
| 259 | 1383 | Immunization | `Immunization.vaccineCode` | VG45 | HepB | http://sys-ids.kemkes.go.id/kfa |
| 260 | 1384 | Immunization | `Immunization.vaccineCode` | 30.0 | hepatitis B immune globulin | http://hl7.org/fhir/sid/cvx |
| 261 | 1397 | Observation | `Observation.code.coding` | 249278006.0 | Ability to pass urine | http://snomed.info/sct |
| 262 | 1409 | Observation | `Observation.code.coding` | 276397000.0 | Has passed meconium | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 128 |
| http://loinc.org | 95 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 17 |
| http://terminology.hl7.org/CodeSystem/admit-source | 4 |
| http://sys-ids.kemkes.go.id/kfa | 4 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 3 |
| http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes | 3 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 3 |
| http://terminology.kemkes.go.id/sp | 2 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 1 |
| http://hl7.org/fhir/sid/icd-10 | 1 |
| http://hl7.org/fhir/sid/cvx | 1 |
| **Total** | **262** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 35 | – | Nama Faskes | Organization | `Organization.name` |
| 73 | – | Kode Dokter | – | `` |
| 78 | – | NIP Pengkaji 1 | – | `` |
| 83 | – | NIP Pengkaji 2 | – | `` |
| 146 | – | Informasi | – | `` |
| 147 | – | Kondisi Saat Tiba di Ruang Rawat | – | `` |
| 206 | – | Riwayat - Usia Pertama Menstruasi | – | `` |
| 207 | – | Riwayat - Lama Waktu Menstruasi | – | `` |
| 208 | – | Riwayat - Banyaknya Menstruasi | – | `` |
| 209 | – | Riwayat - Siklus Menstruasi | – | `` |
| 210 | – | Riwayat - Keterangan Siklus Menstruasi | – | `` |
| 212 | – | Riwayat - Kondisi Menstruasi Yang Dirasakan | – | `` |
| 214 | – | Riwayat - Jumlah Pernikahan | – | `` |
| 215 | – | Riwayat - Lama Masa Pernikahan Ke-1 | – | `` |
| 216 | – | Riwayat - Status Pernikahan Ke-1 | – | `` |
| 219 | – | Riwayat - Lama Masa Pernikahan Ke-2 | – | `` |
| 220 | – | Riwayat - Status Pernikahan Ke-2 | – | `` |
| 223 | – | Riwayat - Lama Masa Pernikahan Ke-3 | – | `` |
| 224 | – | Riwayat - Status Pernikahan Ke-3 | – | `` |
| 352 | – | ANC Ke | – | `` |
| 436 | – | Riwayat Durasi KB | – | `` |
| 450 | – | Kapan Berhenti KB | – | `` |
| 516 | – | Kebiasaan Narkoba | – | `` |
| 559 | – | Tekanan Darah | – | `` |
| 705 | – | Letak Janin | – | `` |
| 815 | – | Pembukaan | – | `` |
| 861 | – | Panggul | – | `` |
| 914 | – | Pemeriksaan Umum Kepala | – | `` |
| 916 | – | Pemeriksaan Umum Muka | – | `` |
| 917 | – | Pemeriksaan Umum Mata | – | `` |
| 919 | – | Pemeriksaan Umum Hidung | – | `` |
| 920 | – | Pemeriksaan Umum Telinga | – | `` |
| 921 | – | Pemeriksaan Umum Mulut | – | `` |
| 922 | – | Pemeriksaan Umum Leher | – | `` |
| 925 | – | Pemeriksaan Umum Dada | – | `` |
| 926 | – | Pemeriksaan Umum Perut | – | `` |
| 930 | – | Pemeriksaan Umum Genitalia | – | `` |
| 932 | – | Pemeriksaan Umum Ekstremitas | – | `` |
| 933 | – | Fungsi Kemampuan Aktivitas | – | `` |
| 934 | – | Fungsi Berjalan | – | `` |
| 935 | – | Keterangan Fungsi Berjalan | – | `` |
| 936 | – | Tirah Baring | – | `` |
| 938 | – | Fungsi Ambulasi | – | `` |
| 941 | – | Fungsi Ekstremitas Atas | – | `` |
| 942 | – | Keterangan Fungsi Ekstremitas Atas | – | `` |
| 943 | – | Fungsi Ekstremitas Bawah | – | `` |
| 945 | – | Keterangan Fungsi Ekstremitas Bawah | – | `` |
| 946 | – | Fungsi Kemampuan Menggenggam | – | `` |
| 947 | – | Keterangan Fungsi Kemampuan Menggenggam | – | `` |
| 948 | – | Fungsi Koordinasi | – | `` |
| 950 | – | Keterangan Fungsi Koordinasi | – | `` |
| 951 | – | Gangguan Fungsi | – | `` |
| 952 | – | Riwayat Psiko - Kondisi Psiko | – | `` |
| 954 | – | Riwayat Psiko - Perilaku | – | `` |
| 955 | – | Riwayat Psiko - Keterangan Perilaku | – | `` |
| 956 | – | Riwayat Psiko - Gangguan Jiwa | – | `` |
| 957 | – | Riwayat Psiko - Hubungan Pasien | – | `` |
| 958 | – | Riwayat Psiko - Tinggal Dengan | – | `` |
| 961 | – | Riwayat Psiko - Keterangan Tinggal Dengan | – | `` |
| 962 | – | Riwayat Psiko - Budaya | – | `` |
| 964 | – | Riwayat Psiko - Keterangan Budaya | – | `` |
| 965 | – | Riwayat Psiko - Pendidikan | – | `` |
| 968 | – | Riwayat Psiko - Edukasi Pada | – | `` |
| 970 | – | Riwayat Psiko - Keterangan Edukasi Pada | – | `` |
| 971 | – | Penilaian Nyeri | – | `` |
| 973 | – | Penyebab Nyeri | – | `` |
| 975 | – | Keterangan Penyebab Nyeri | – | `` |
| 976 | – | Penilaian Kualitas Nyeri | – | `` |
| 978 | – | Keterangan Kualitas Nyeri | – | `` |
| 979 | – | Penilaian Nyeri - Lokasi | – | `` |
| 980 | – | Penilaian Nyeri - Menyebar | – | `` |
| 982 | – | Penilaian Nyeri - Skala | – | `` |
| 983 | – | Penilaian Nyeri - Waktu | – | `` |
| 984 | – | Penilaian Nyeri - Hilang | – | `` |
| 986 | – | Penilaian Nyeri - Keterangan Hilang | – | `` |
| 987 | – | Penilaian Nyeri - Diberitahukan Dokter | – | `` |
| 989 | – | Penilaian Nyeri - Jam Diberitahukan Dokter | – | `` |
| 990 | – | Penilaian Jatuh Skala 1 | – | `` |
| 992 | – | Penilaian Jatuh Nilai 1 | – | `` |
| 993 | – | Penilaian Jatuh Skala 2 | – | `` |
| 995 | – | Penilaian Jatuh Nilai 2 | – | `` |
| 996 | – | Penilaian Jatuh Skala 3 | – | `` |
| 998 | – | Penilaian Jatuh Nilai 3 | – | `` |
| 999 | – | Penilaian Jatuh Skala 4 | – | `` |
| 1001 | – | Penilaian Jatuh Nilai 4 | – | `` |
| 1002 | – | Penilaian Jatuh Skala 5 | – | `` |
| 1004 | – | Penilaian Jatuh Nilai 5 | – | `` |
| 1005 | – | Penilaian Jatuh Skala 6 | – | `` |
| 1006 | – | Penilaian Jatuh Nilai 6 | – | `` |
| 1007 | – | Penilaian Jatuh Total Nilai | – | `` |
| 1008 | – | Skrining Gizi Ke-1 | – | `` |
| 1010 | – | Nilai Gizi Ke-1 | – | `` |
| 1011 | – | Skrining Gizi Ke-2 | – | `` |
| 1013 | – | Nilai Gizi Ke-2 | – | `` |
| 1014 | – | Nama Bahasa | – | `` |
| 1017 | – | Nilai Total Gizi | – | `` |
| 1018 | – | Skrining Gizi - Diagnosa Khusus | – | `` |
| 1019 | – | Skrining Gizi - Keterangan Diagnosa Khusus | – | `` |
| 1020 | – | Skrining Gizi - Diketahui Dietisien | – | `` |
| 1022 | – | Skrining Gizi - Jam Diketahui Dietisien | – | `` |
| 1032 | – | Rencana Tatalaksana atau Tindakan | – | `` |
| 1033 | – | Tindakan drpr | – | `` |
| 1034 | – | Tindakan dr | – | `` |
| 1093 | – | No Rekam Medis | – | `` |
| 1099 | – | Umur Ibu | – | `` |
| 1104 | – | Umur Ayah | – | `` |
| 1166 | – | Keterangan | – | `` |
| 1170 | – | Diagnosis Bayi | – | `` |
