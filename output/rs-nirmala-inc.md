# Output Form: SIM RS Nirmala INC

Sumber: `mapping/phdt-data-dictionary-rs-nirmala-inc.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-rs-nirmala-inc.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 67 |
| Code (`jumlah code` = 1) | 164 |
| Code unik (code + CodeSystem) | 157 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 18 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–27 | Patient | – | – | _Nama Ibu_ → `Patient.name.text` (2, tanpa BQ)<br>_NIK_ → `Patient.identifier.value` (6, tanpa BQ)<br>_No HP_ → `Patient.telecom` (7, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (10, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (11, tanpa BQ)<br>_Alamat Domisili_ → `Patient.address.line` (13, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (18, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (21, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.extension.valueCode` (24, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.extension.valueCode` (27, tanpa BQ) |
| 2 | 67–73 | Practitioner | – | – | _NIK_ → `Practitioner.identifier.value` (69, tanpa BQ)<br>_Nama Tenaga Kesehatan_ → `Practitioner.name.text` (71, tanpa BQ)<br>_Jenis Kelamin Tenaga Kesehatan_ → `Practitioner.gender` (72, tanpa BQ) |
| 3 | 74–81 | PractitionerRole | – | – | _Tenaga Pemeriksa_ → `PractitionerRole.code.coding` (78, tanpa BQ) |
| 4 | 83–98 | Encounter | – | – | _Jenis Kunjungan INC_ → `Encounter.class` (84, tanpa BQ)<br>_Tanggal Masuk INC_ → `Encounter.period.start` (93, tanpa BQ)<br>_Tanggal Keluar INC_ → `Encounter.period.end` (94, tanpa BQ)<br>_Tempat Pelayanan INC_ → `Encounter.location.location.display` (96, tanpa BQ) |
| 5 | 99–107 | Condition | 386337006.0 | Intrapartal care | _Diagnosis Masuk_ → `Condition.code.coding` (101, tanpa BQ) |
| 6 | 118–131 | EpisodeOfCare | ANC | Antenatal Care | – |
| 7 | 133–141 | EpisodeOfCare | PNC | Postnatal Care | – |
| 8 | 142–153 | Observation | SP000383 | Keadaan Ibu Saat Tiba | _Keadaan Ibu Saat Tiba_ → `Observation.valueCodeableConcept.coding` (145, tanpa BQ) |
| 9 | 154–165 | Observation | 8480-6 | Systolic blood pressure | _Tekanan Darah Sistolik_ → `Observation.valueQuantity.value` (157, tanpa BQ) |
| 10 | 166–177 | Observation | 8462-4 | Diastolic blood pressure | _Tekanan Darah Diastolik_ → `Observation.valueQuantity.value` (169, tanpa BQ) |
| 11 | 178–190 | Observation | 8867-4 | Heart rate | _Frekuensi Nadi_ → `Observation.valueQuantity.value` (181, tanpa BQ) |
| 12 | 191–203 | Observation | 9279-1 | Respiratory rate | _Pernapasan_ → `Observation.valueQuantity.value` (194, tanpa BQ) |
| 13 | 204–216 | Observation | – | – | _Suhu Badan_ → `Observation.valueQuantity.value` (207, tanpa BQ) |
| 14 | 217–228 | Observation | 284473002.0 | Mid upper arm circumference | _LiLA_ → `Observation.valueQuantity.value` (220, tanpa BQ) |
| 15 | 229–240 | Observation | 29463-7 | Body weight | _Berat Badan_ → `Observation.valueQuantity.value` (232, tanpa BQ) |
| 16 | 241–252 | Observation | 8302-2 | Body height | _Tinggi Badan_ → `Observation.valueQuantity.value` (244, tanpa BQ) |
| 17 | 253–264 | Observation | 11996-6 | [#] Pregnancies | _Gravida_ → `Observation.valueInteger` (257, tanpa BQ) |
| 18 | 265–276 | Observation | 11977-6 | [#] Parity | _Partus_ → `Observation.valueInteger` (269, tanpa BQ) |
| 19 | 277–288 | Observation | 69043-8 | Other pregnancy outcomes # | _Abortus_ → `Observation.valueInteger` (281, tanpa BQ) |
| 20 | 289–296 | Condition | – | – | _Kode ICD - Diagnosa_ → `Condition.clinicalStatus.coding` (289, tanpa BQ) |
| 21 | 297–307 | Observation | SP000683 | Tatalaksana Tindakan | _Tatalaksana (Tindakan)_ → `Observation.valueString` (300, tanpa BQ) |
| 22 | 308–318 | Observation | SP000684 | Tatalaksana Obat | _Tatalaksana Obat_ → `Observation.valueString` (311, tanpa BQ) |
| 23 | 319–327 | Condition | 199745000.0 | Complication occurring during labor and delivery | _Komplikasi_ → `Condition.clinicalStatus.coding` (319, tanpa BQ) |
| 24 | 328–341 | Observation | OC000001 | Jarak kehamilan | _Jarak kehamilan saat ini dengan kehamilan sebelumnya (dalam bulan)_ → `Observation.valueQuantity.value` (332, tanpa BQ) |
| 25 | 342–355 | Observation | 11881-0 | Uterus Fundal height Tape measure | _Tinggi Fundus Uteri_ → `Observation.valueQuantity.value` (345, tanpa BQ)<br>_Detak Jantung Janin_ → `Observation.identifier.value` (355, tanpa BQ) |
| 26 | 356–368 | Observation | 55283-6 | Fetal Heart rate | _Kondisi Detak Jantung Janin_ → `Observation.identifier.value` (368, tanpa BQ) |
| 27 | 369–383 | Observation | 289437007.0 | Finding of fetal heart rate | _Letak Janin_ → `Observation.identifier.value` (383, tanpa BQ) |
| 28 | 384–396 | Observation | 271692001.0 | Presentation of fetus | _Presentasi Janin_ → `Observation.identifier.value` (396, tanpa BQ) |
| 29 | 397–416 | Observation | 72155-5 | Position in womb Fetus [RHEA] | _Posisi Kepala Janin terhadap PAP (Pintu Atas Panggul)_ → `Observation.identifier.value` (416, tanpa BQ) |
| 30 | 417–430 | Observation | 249111004.0 | Engagement of head | _Kondisi Ketuban_ → `Observation.identifier.value` (430, tanpa BQ) |
| 31 | 431–443 | Observation | 289282009.0 | Amniotic membrane finding | _Faktor risiko INC_ → `Observation.status` (443, tanpa BQ) |
| 32 | 444–453 | Observation | SP000015 | Risiko Masalah Kesehatan | – |
| 33 | 454–493 | QuestionnaireResponse | – | – | – |
| 34 | 494–507 | Observation | SP000123 | Integrasi Program | _Integrasi Program_ → `Observation.valueCodeableConcept.coding` (497, tanpa BQ) |
| 35 | 508–529 | Observation | 72150-6 | Delivery location | _Tempat Melahirkan_ → `Observation.valueCodeableConcept.coding` (511, tanpa BQ) |
| 36 | 545–559 | Observation | 76516-4 | Gestational age—​at birth | _Usia Kehamilan/ Gestasi pada saat Persalinan_ → `Observation.valueQuantity.value` (548, tanpa BQ) |
| 37 | 560–570 | Observation | 93857-1 | Date and time of obstetric delivery | _Tanggal dan Jam Persalinan_ → `Observation.valueDateTime` (563, tanpa BQ) |
| 38 | 571–581 | Observation | OC000013 | Penolong Persalinan | _Nama Penolong Persalinan_ → `Observation.status` (571, tanpa BQ) |
| 39 | 582–595 | Observation | 57071-3 | Obstetric delivery method | _Cara Persalinan_ → `Observation.valueCodeableConcept.coding` (585, tanpa BQ) |
| 40 | 596–613 | Observation | 405195003.0 | Intrapartum maternal status | _Keadaan Ibu_ → `Observation.valueCodeableConcept.coding` (599, tanpa BQ) |
| 41 | 614–627 | Observation | 387700009.0 | Prolonged latent phase of labor | _Kala I laten_ → `Observation.valueDateTime` (617, tanpa BQ) |
| 42 | 628–638 | Observation | 249120008.0 | Onset of labor first stage | _Kala I Aktif_ → `Observation.valueDateTime` (631, tanpa BQ) |
| 43 | 639–652 | Observation | 249160009.0 | Onset of labor second stage | _Kala II_ → `Observation.valueDateTime` (642, tanpa BQ) |
| 44 | 653–666 | Observation | OC000018 | Onset Kala III | _Kala III_ → `Observation.valueDateTime` (656, tanpa BQ) |
| 45 | 667–678 | Observation | 236994008.0 | Placental delivery procedure | _Plasenta lahir_ → `Observation.valueDateTime` (670, tanpa BQ) |
| 46 | 679–690 | Observation | 289267004.0 | Finding of completeness of placenta | _Kondisi Plasenta_ → `Observation.valueCodeableConcept.coding` (682, tanpa BQ) |
| 47 | 691–702 | Procedure | SP000127 | Injeksi Oksitosin | _Injeksi Oksitosin_ → `Procedure.category.coding` (691, tanpa BQ) |
| 48 | 703–714 | Procedure | 302384005.0 | Controlled cord traction of placenta | _Peregangan Tali Pusat_ → `Procedure.category.coding` (703, tanpa BQ) |
| 49 | 715–726 | Procedure | 236996005.0 | Abdominal uterine fundal massage | _Masase Fundus Uteri_ → `Procedure.category.coding` (715, tanpa BQ) |
| 50 | 727–740 | Observation | OC000019 | Onset Kala IV | _Kala IV_ → `Observation.valueDateTime` (730, tanpa BQ) |
| 51 | 741–754 | Condition | 9293002.0 | Atony of uterus | _Kondisi Kala 4_ → `Condition.clinicalStatus.coding` (741, tanpa BQ) |
| 52 | 755–767 | Observation | 719051004.0 | Quantity of postpartum maternal blood loss | _Jumlah Pendarahan Kala 4 (dalam cc)_ → `Observation.valueQuantity.value` (758, tanpa BQ) |
| 53 | 768–780 | Observation | 8480-6 | Systolic blood pressure | _Sistol Kala 4_ → `Observation.valueQuantity.value` (771, tanpa BQ) |
| 54 | 781–793 | Observation | 8462-4 | Diastolic blood pressure | _Diastol Kala 4_ → `Observation.valueQuantity.value` (784, tanpa BQ) |
| 55 | 794–806 | Procedure | 717809003.0 | Immediate postpartum care | _Pemantauan Kala 4_ → `Procedure.category.coding` (794, tanpa BQ) |
| 56 | 807–826 | Condition | 199746004.0 | Obstructed labor | _Komplikasi Persalinan_ → `Condition.clinicalStatus.coding` (807, tanpa BQ) |
| 57 | 827–845 | Observation | SP000379 | Tatalaksana Komplikasi Persalinan | _Tatalaksana Komplikasi Persalinan_ → `Observation.valueCodeableConcept.coding` (830, tanpa BQ) |
| 58 | 846–859 | Observation | 63893-2 | Outcome of pregnancy | _Luaran Kehamilan_ → `Observation.valueCodeableConcept.coding` (849, tanpa BQ) |
| 59 | 861–883 | ServiceRequest | 409014006.0 | Delivery care management | _Faskes Rujukan_ → `ServiceRequest.locationCode.coding` (874, tanpa BQ)<br>_Nama Faskes Rujukan_ → `ServiceRequest.locationCode.text` (882, tanpa BQ)<br>_Tindak Lanjut_ → `ServiceRequest.patientInstruction` (883, tanpa BQ) |
| 60 | 884–896 | Observation | SP000122 | Catat di Buku KIA | _Catat di buku KIA_ → `Observation.valueBoolean` (886, tanpa BQ) |
| 61 | 897–912 | Procedure | SP000130 | Menggunakan Partograf | _Pelayanan Menggunakan Partograf_ → `Procedure.category.coding` (897, tanpa BQ)<br>_Inisiasi Menyusu Dini (IMD)_ → `Procedure.category.coding` (908, tanpa BQ) |
| 62 | 913–920 | Procedure | 431868002.0 | Initiation of breastfeeding | – |
| 63 | 921–933 | Observation | OC000016 | Waktu Inisiasi Menyusui Dini | _Waktu Inisiasi Menyusu Dini (IMD)_ → `Observation.valueCodeableConcept.coding` (923, tanpa BQ) |
| 64 | 934–947 | Observation | 365662002.0 | Finding of amniotic fluid appearance | _Warna Ketuban_ → `Observation.valueCodeableConcept.coding` (936, tanpa BQ) |
| 65 | 948–950 | Procedure | 409063005.0 | Counselling | _Konseling_ → `Procedure.category.coding` (948, tanpa BQ) |
| 66 | 951–959 | Procedure | 409063005.0 | Counselling | – |
| 67 | 960–970 | Observation | 57074-7 | Labor and delivery process Narrative | _Catatan Persalinan_ → `Observation.valueString` (963, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 46 |
| Procedure | 8 |
| Condition | 5 |
| EpisodeOfCare | 2 |
| Patient | 1 |
| Practitioner | 1 |
| PractitionerRole | 1 |
| Encounter | 1 |
| QuestionnaireResponse | 1 |
| ServiceRequest | 1 |
| **Total** | **67** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 78 | PractitionerRole | `PractitionerRole.code.coding` | 309453006.0 | Registered midwife | http://snomed.info/sct |
| 2 | 79 | PractitionerRole | `PractitionerRole.code.coding` | 309367003.0 | Obstetrician and gynecologist | http://snomed.info/sct |
| 3 | 80 | PractitionerRole | `PractitionerRole.code.coding` | 309343006.0 | Physician | http://snomed.info/sct |
| 4 | 81 | PractitionerRole | `PractitionerRole.code.coding` | 224535009.0 | Registered nurse | http://snomed.info/sct |
| 5 | 102 | Condition | `Condition.code.coding` | 386337006.0 | Intrapartal care | http://snomed.info/sct |
| 6 | 119 | EpisodeOfCare | `EpisodeOfCare.type.coding` | ANC | Antenatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 7 | 134 | EpisodeOfCare | `EpisodeOfCare.type.coding` | PNC | Postnatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 8 | 144 | Observation | `Observation.code.coding` | SP000383 | Keadaan Ibu Saat Tiba | http://terminology.kemkes.go.id/sp |
| 9 | 145 | Observation | `Observation.valueCodeableConcept.coding` | 438949009.0 | Alive | http://snomed.info/sct |
| 10 | 146 | Observation | `Observation.valueCodeableConcept.coding` | 419099009.0 | Dead | http://snomed.info/sct |
| 11 | 156 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 12 | 168 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://loinc.org |
| 13 | 180 | Observation | `Observation.code.coding` | 8867-4 | Heart rate | http://loinc.org |
| 14 | 193 | Observation | `Observation.code.coding` | 9279-1 | Respiratory rate | http://loinc.org |
| 15 | 219 | Observation | `Observation.code.coding` | 284473002.0 | Mid upper arm circumference | http://snomed.info/sct |
| 16 | 231 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 17 | 243 | Observation | `Observation.code.coding` | 8302-2 | Body height | http://loinc.org |
| 18 | 255 | Observation | `Observation.code.coding` | 11996-6 | [#] Pregnancies | http://loinc.org |
| 19 | 256 | Observation | `Observation.code.coding` | ANC.B6.DE24 | Number of pregnancies (gravida) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 20 | 267 | Observation | `Observation.code.coding` | 11977-6 | [#] Parity | http://loinc.org |
| 21 | 268 | Observation | `Observation.code.coding` | ANC.B6.DE32 | Parity | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 22 | 279 | Observation | `Observation.code.coding` | 69043-8 | Other pregnancy outcomes # | http://loinc.org |
| 23 | 280 | Observation | `Observation.code.coding` | ANC.B6.DE25 | Number of miscarriages and/or abortions | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 24 | 299 | Observation | `Observation.code.coding` | SP000683 | Tatalaksana Tindakan | http://terminology.kemkes.go.id/sp |
| 25 | 310 | Observation | `Observation.code.coding` | SP000684 | Tatalaksana Obat | http://terminology.kemkes.go.id/sp |
| 26 | 321 | Condition | `Condition.code.coding` | 199745000.0 | Complication occurring during labor and delivery | http://snomed.info/sct |
| 27 | 330 | Observation | `Observation.code.coding` | OC000001 | Jarak kehamilan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 28 | 331 | Observation | `Observation.code.coding` | ANC.SS.DE53 | Jarak kehamilan | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 29 | 344 | Observation | `Observation.code.coding` | 11881-0 | Uterus Fundal height Tape measure | http://loinc.org |
| 30 | 357 | Observation | `Observation.code.coding` | 55283-6 | Fetal Heart rate | http://loinc.org |
| 31 | 370 | Observation | `Observation.code.coding` | 289437007.0 | Finding of fetal heart rate | http://snomed.info/sct |
| 32 | 371 | Observation | `Observation.valueCodeableConcept.coding` | 289441006.0 | Normal fetal heart rate | http://snomed.info/sct |
| 33 | 372 | Observation | `Observation.valueCodeableConcept.coding` | 289440007.0 | Fetal heart rate not observed | http://snomed.info/sct |
| 34 | 373 | Observation | `Observation.valueCodeableConcept.coding` | 312668007.0 | Abnormal fetal heart rate | http://snomed.info/sct |
| 35 | 374 | Observation | `Observation.valueCodeableConcept.coding` | 289439005.0 | Fetal heart rate absent | http://snomed.info/sct |
| 36 | 385 | Observation | `Observation.code.coding` | 271692001.0 | Presentation of fetus | http://snomed.info/sct |
| 37 | 386 | Observation | `Observation.valueCodeableConcept.coding` | 398236008.0 | Intrauterine | http://snomed.info/sct |
| 38 | 387 | Observation | `Observation.valueCodeableConcept.coding` | 298109001.0 | Ectopic | http://snomed.info/sct |
| 39 | 398 | Observation | `Observation.code.coding` | 72155-5 | Position in womb Fetus [RHEA] | http://loinc.org |
| 40 | 399 | Observation | `Observation.valueCodeableConcept.coding` | 70028003.0 | Vertex presentation | http://snomed.info/sct |
| 41 | 400 | Observation | `Observation.valueCodeableConcept.coding` | 249083005.0 | Posterior fontanelle presenting | http://snomed.info/sct |
| 42 | 401 | Observation | `Observation.valueCodeableConcept.coding` | 288203005.0 | Transverse/oblique lie | http://snomed.info/sct |
| 43 | 402 | Observation | `Observation.valueCodeableConcept.coding` | 23954006.0 | Acromion presentation | http://snomed.info/sct |
| 44 | 403 | Observation | `Observation.valueCodeableConcept.coding` | 6096002.0 | Breech presentation | http://snomed.info/sct |
| 45 | 404 | Observation | `Observation.valueCodeableConcept.coding` | 8014007.0 | Brow presentation of fetus | http://snomed.info/sct |
| 46 | 405 | Observation | `Observation.valueCodeableConcept.coding` | 8017000.0 | Face presentation | http://snomed.info/sct |
| 47 | 406 | Observation | `Observation.valueCodeableConcept.coding` | 249097002.0 | Footling breech presentation | http://snomed.info/sct |
| 48 | 407 | Observation | `Observation.valueCodeableConcept.coding` | 124736009.0 | Compound presentation | http://snomed.info/sct |
| 49 | 418 | Observation | `Observation.code.coding` | 249111004.0 | Engagement of head | http://snomed.info/sct |
| 50 | 419 | Observation | `Observation.valueCodeableConcept.coding` | 249112006.0 | Head engaged | http://snomed.info/sct |
| 51 | 420 | Observation | `Observation.valueCodeableConcept.coding` | 62098001.0 | Head not engaged | http://snomed.info/sct |
| 52 | 421 | Observation | `Observation.dataAbsentReason` | unknown | Unknown | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 53 | 432 | Observation | `Observation.code.coding` | 289282009.0 | Amniotic membrane finding | http://snomed.info/sct |
| 54 | 433 | Observation | `Observation.valueCodeableConcept.coding` | 249125003.0 | Intact membranes | http://snomed.info/sct |
| 55 | 434 | Observation | `Observation.valueCodeableConcept.coding` | SP000120 | Non-intact membrane | http://snomed.info/sct |
| 56 | 445 | Observation | `Observation.code.coding` | SP000015 | Risiko Masalah Kesehatan | http://terminology.kemkes.go.id/sp |
| 57 | 496 | Observation | `Observation.code.coding` | SP000123 | Integrasi Program | http://terminology.kemkes.go.id/sp |
| 58 | 497 | Observation | `Observation.valueCodeableConcept.coding` | SP000046 | Terapi Antiretroviral (ART) | http://terminology.kemkes.go.id/sp |
| 59 | 498 | Observation | `Observation.valueCodeableConcept.coding` | SP000124 | Obat anti malaria | http://terminology.kemkes.go.id/sp |
| 60 | 499 | Observation | `Observation.valueCodeableConcept.coding` | SP000125 | Obar anti hepatitis B | http://terminology.kemkes.go.id/sp |
| 61 | 510 | Observation | `Observation.code.coding` | 72150-6 | Delivery location | http://loinc.org |
| 62 | 511 | Observation | `Observation.valueCodeableConcept.coding` | 264362003.0 | Home | http://snomed.info/sct |
| 63 | 512 | Observation | `Observation.valueCodeableConcept.coding` | OT000001 | Polindes | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 64 | 513 | Observation | `Observation.valueCodeableConcept.coding` | OT000002 | Pustu | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 65 | 514 | Observation | `Observation.valueCodeableConcept.coding` | 102.0 | Pusat Kesehatan Masyarakat | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 66 | 515 | Observation | `Observation.valueCodeableConcept.coding` | 103.0 | Klinik | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 67 | 516 | Observation | `Observation.valueCodeableConcept.coding` | OT000008 | Rumah Bersalin | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 68 | 517 | Observation | `Observation.valueCodeableConcept.coding` | 82242000.0 | Children’s hospital | http://snomed.info/sct |
| 69 | 518 | Observation | `Observation.valueCodeableConcept.coding` | 104.0 | Rumah Sakit | hhttp://terminology.kemkes.go.id/CodeSystem/organization-type |
| 70 | 519 | Observation | `Observation.valueCodeableConcept.coding` | OT000004 | Bidan Praktek Mandiri | hhttp://terminology.kemkes.go.id/CodeSystem/organization-type |
| 71 | 520 | Observation | `Observation.valueCodeableConcept.coding` | LT000008 | Dalam perjalanan dari rumah/masyarakat | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 72 | 521 | Observation | `Observation.valueCodeableConcept.coding` | LT000009 | Dalam perjalanan ke faskes lain | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 73 | 522 | Observation | `Observation.valueCodeableConcept.coding` | LT000007 | Rumah Dukun | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 74 | 547 | Observation | `Observation.code.coding` | 76516-4 | Gestational age—​at birth | http://loinc.org |
| 75 | 550 | Observation | `Observation.component.code.coding` | SP000398 | Usia Kehamilan Saat Persalinan (hari) | http://terminology.kemkes.go.id/sp |
| 76 | 562 | Observation | `Observation.code.coding` | 93857-1 | Date and time of obstetric delivery | http://loinc.org |
| 77 | 573 | Observation | `Observation.code.coding` | OC000013 | Penolong Persalinan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 78 | 584 | Observation | `Observation.code.coding` | 57071-3 | Obstetric delivery method | http://loinc.org |
| 79 | 585 | Observation | `Observation.valueCodeableConcept.coding` | 48782003.0 | Delivery normal | http://snomed.info/sct |
| 80 | 586 | Observation | `Observation.valueCodeableConcept.coding` | 200138003.0 | Vacuum extractor delivery - delivered | http://snomed.info/sct |
| 81 | 587 | Observation | `Observation.valueCodeableConcept.coding` | 200130005.0 | Forceps delivery - delivered | http://snomed.info/sct |
| 82 | 588 | Observation | `Observation.valueCodeableConcept.coding` | 200144004.0 | Deliveries by cesarean | http://snomed.info/sct |
| 83 | 598 | Observation | `Observation.code.coding` | 405195003.0 | Intrapartum maternal status | http://snomed.info/sct |
| 84 | 599 | Observation | `Observation.valueCodeableConcept.coding` | 102514002.0 | Well female adult | http://snomed.info/sct |
| 85 | 600 | Observation | `Observation.valueCodeableConcept.coding` | 39104002.0 | Illness | http://snomed.info/sct |
| 86 | 601 | Observation | `Observation.valueCodeableConcept.coding` | 131148009.0 | Bleeding | http://snomed.info/sct |
| 87 | 602 | Observation | `Observation.valueCodeableConcept.coding` | 386661006.0 | Fever | http://snomed.info/sct |
| 88 | 603 | Observation | `Observation.valueCodeableConcept.coding` | 91175000.0 | Seizure | http://snomed.info/sct |
| 89 | 604 | Observation | `Observation.valueCodeableConcept.coding` | 249215002.0 | Odor of lochia | http://snomed.info/sct |
| 90 | 605 | Observation | `Observation.valueCodeableConcept.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 91 | 606 | Observation | `Observation.valueCodeableConcept.coding` | 59283008.0 | Maternal death | http://snomed.info/sct |
| 92 | 616 | Observation | `Observation.code.coding` | 387700009.0 | Prolonged latent phase of labor | http://snomed.info/sct |
| 93 | 630 | Observation | `Observation.code.coding` | 249120008.0 | Onset of labor first stage | http://snomed.info/sct |
| 94 | 641 | Observation | `Observation.code.coding` | 249160009.0 | Onset of labor second stage | http://snomed.info/sct |
| 95 | 655 | Observation | `Observation.code.coding` | OC000018 | Onset Kala III | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 96 | 669 | Observation | `Observation.code.coding` | 236994008.0 | Placental delivery procedure | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 97 | 681 | Observation | `Observation.code.coding` | 289267004.0 | Finding of completeness of placenta | http://snomed.info/sct |
| 98 | 682 | Observation | `Observation.valueCodeableConcept.coding` | 249170006.0 | Complete placenta at delivery | http://snomed.info/sct |
| 99 | 683 | Observation | `Observation.valueCodeableConcept.coding` | 268479002.0 | Incomplete placenta at delivery | http://snomed.info/sct |
| 100 | 694 | Procedure | `Procedure.code.coding` | SP000127 | Injeksi Oksitosin | http://terminology.kemkes.go.id/sp |
| 101 | 706 | Procedure | `Procedure.code.coding` | 302384005.0 | Controlled cord traction of placenta | http://snomed.info/sct |
| 102 | 718 | Procedure | `Procedure.code.coding` | 236996005.0 | Abdominal uterine fundal massage | http://snomed.info/sct |
| 103 | 729 | Observation | `Observation.code.coding` | OC000019 | Onset Kala IV | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 104 | 743 | Condition | `Condition.code.coding` | 9293002.0 | Atony of uterus | http://snomed.info/sct |
| 105 | 744 | Condition | `Condition.code.coding` | 48194001.0 | Postpartum hemorrhage | http://snomed.info/sct |
| 106 | 745 | Condition | `Condition.code.coding` | 1148943004.0 | Retention of placenta and uterine membrane | http://snomed.info/sct |
| 107 | 746 | Condition | `Condition.code.coding` | 283380005.0 | Laceration of perineum | http://snomed.info/sct |
| 108 | 747 | Condition | `Condition.code.coding` | 84007008.0 | Shock during AND/OR following labor AND/OR delivery | http://snomed.info/sct |
| 109 | 748 | Condition | `Condition.code.coding` | 118216002.0 | Labor finding | http://snomed.info/sct |
| 110 | 749 | Condition | `Condition.code.coding` | 10756061000119109 | Pain during postpartum period due to and following cesarean section | http://snomed.info/sct |
| 111 | 757 | Observation | `Observation.code.coding` | 719051004.0 | Quantity of postpartum maternal blood loss | http://snomed.info/sct |
| 112 | 770 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 113 | 783 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://snomed.info/sct |
| 114 | 797 | Procedure | `Procedure.code.coding` | 717809003.0 | Immediate postpartum care | http://snomed.info/sct |
| 115 | 809 | Condition | `Condition.code.coding` | 199746004.0 | Obstructed labor | http://snomed.info/sct |
| 116 | 810 | Condition | `Condition.code.coding` | 48194001.0 | Pregnancy-induced hypertension | http://snomed.info/sct |
| 117 | 811 | Condition | `Condition.code.coding` | 38010008.0 | Intrapartum hemorrhage | http://snomed.info/sct |
| 118 | 812 | Condition | `Condition.code.coding` | 40733004.0 | Infectious disease | http://snomed.info/sct |
| 119 | 813 | Condition | `Condition.code.coding` | 386639001.0 | Termination of pregnancy | http://snomed.info/sct |
| 120 | 814 | Condition | `Condition.code.coding` | 44223004.0 | Premature rupture of membranes | http://snomed.info/sct |
| 121 | 815 | Condition | `Condition.code.coding` | 38341003.0 | Hypertensive disorder, systemic arterial | http://snomed.info/sct |
| 122 | 816 | Condition | `Condition.code.coding` | 398254007.0 | Pre-eclampsia | http://snomed.info/sct |
| 123 | 817 | Condition | `Condition.code.coding` | 15938005.0 | Eclampsia | http://snomed.info/sct |
| 124 | 818 | Condition | `Condition.code.coding` | 9293002.0 | Atony of uterus | http://snomed.info/sct |
| 125 | 819 | Condition | `Condition.code.coding` | 283380005.0 | Laceration of perineum | http://snomed.info/sct |
| 126 | 820 | Condition | `Condition.code.coding` | 199745000.0 | Complication occurring during labor and delivery | http://snomed.info/sct |
| 127 | 829 | Observation | `Observation.code.coding` | SP000379 | Tatalaksana Komplikasi Persalinan | http://terminology.kemkes.go.id/sp |
| 128 | 830 | Observation | `Observation.valueCodeableConcept.coding` | 430701006.0 | Resuscitation using intravenous fluid | http://snomed.info/sct |
| 129 | 831 | Observation | `Observation.valueCodeableConcept.coding` | SP000156 | Pemberian Obat Uterotonik | http://terminology.kemkes.go.id/sp |
| 130 | 832 | Observation | `Observation.valueCodeableConcept.coding` | 236998006.0 | Bimanual uterine massage | http://snomed.info/sct |
| 131 | 833 | Observation | `Observation.valueCodeableConcept.coding` | 360362007.0 | Suture of laceration of perineum | http://snomed.info/sct |
| 132 | 834 | Observation | `Observation.valueCodeableConcept.coding` | 28233006.0 | Manual removal of retained placenta | http://snomed.info/sct |
| 133 | 835 | Observation | `Observation.valueCodeableConcept.coding` | SP000013 | Pemberian MgSO4 | http://terminology.kemkes.go.id/sp |
| 134 | 836 | Observation | `Observation.valueCodeableConcept.coding` | 308116003.0 | Antihypertensive therapy | http://snomed.info/sct |
| 135 | 837 | Observation | `Observation.valueCodeableConcept.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 136 | 848 | Observation | `Observation.code.coding` | 63893-2 | Outcome of pregnancy | http://loinc.org |
| 137 | 849 | Observation | `Observation.valueCodeableConcept.coding` | LA14270-5 | Live birth | http://loinc.org |
| 138 | 850 | Observation | `Observation.valueCodeableConcept.coding` | LA14271-3 | Stillborn | http://loinc.org |
| 139 | 851 | Observation | `Observation.valueCodeableConcept.coding` | LA14272-1 | Miscarriage | http://loinc.org |
| 140 | 852 | Observation | `Observation.valueCodeableConcept.coding` | LA14273-9 | Induced abortion | http://loinc.org |
| 141 | 865 | ServiceRequest | `ServiceRequest.code.coding` | 409014006.0 | Delivery care management | http://snomed.info/sct |
| 142 | 874 | ServiceRequest | `ServiceRequest.locationCode.coding` | SP000129 | Puskesmas PONED | http://terminology.kemkes.go.id/sp |
| 143 | 878 | ServiceRequest | `ServiceRequest.locationCode.coding` | SP000128 | Rumah Sakit Ibu dan Anak | http://terminology.kemkes.go.id/sp |
| 144 | 885 | Observation | `Observation.code.coding` | SP000122 | Catat di Buku KIA | http://terminology.kemkes.go.id/sp |
| 145 | 888 | Observation | `Observation.dataAbsentReason.coding` | not-applicable | Not Applicable | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 146 | 900 | Procedure | `Procedure.code.coding` | SP000130 | Menggunakan Partograf | http://terminology.kemkes.go.id/sp |
| 147 | 913 | Procedure | `Procedure.code.coding` | 431868002.0 | Initiation of breastfeeding | http://snomed.info/sct |
| 148 | 922 | Observation | `Observation.code.coding` | OC000016 | Waktu Inisiasi Menyusui Dini | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 149 | 923 | Observation | `Observation.valueCodeableConcept.coding` | OV000014 | Kurang dari 1 Jam | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 150 | 925 | Observation | `Observation.valueCodeableConcept.coding` | OV000015 | Lebih dari 1 Jam | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 151 | 935 | Observation | `Observation.code.coding` | 365662002.0 | Finding of amniotic fluid appearance | http://snomed.info/sct |
| 152 | 936 | Observation | `Observation.valueCodeableConcept.coding` | 168090003.0 | Amniotic fluid clear | http://snomed.info/sct |
| 153 | 937 | Observation | `Observation.valueCodeableConcept.coding` | 408781009.0 | Straw colored amniotic fluid | http://snomed.info/sct |
| 154 | 938 | Observation | `Observation.valueCodeableConcept.coding` | 249134008.0 | Bloodstained liquor | http://snomed.info/sct |
| 155 | 939 | Observation | `Observation.valueCodeableConcept.coding` | 168092006.0 | Amniotic fluid -meconium stain | http://snomed.info/sct |
| 156 | 950 | Procedure | `Procedure.code.coding` | 409063005.0 | Counselling | http://snomed.info/sct |
| 157 | 952 | Procedure | `Procedure.code.coding` | 409063005.0 | Counselling | http://snomed.info/sct |
| 158 | 953 | Procedure | `Procedure.code.coding` | ED000008 | Edukasi Tanda Bahaya Kehamilan, Bersalin dan Nifas | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 159 | 954 | Procedure | `Procedure.code.coding` | SP000121 | Edukasi Tanda Bahaya Baru Lahir | http://terminology.kemkes.go.id/sp |
| 160 | 955 | Procedure | `Procedure.code.coding` | ED000009 | Edukasi IMD dan ASI Eksklusif | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 161 | 956 | Procedure | `Procedure.code.coding` | ED000005 | Edukasi Gizi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 162 | 957 | Procedure | `Procedure.code.coding` | PC000001 | Perawatan Tali Pusat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 163 | 958 | Procedure | `Procedure.code.coding` | ED000010 | Edukasi PHBS | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 164 | 962 | Observation | `Observation.code.coding` | 57074-7 | Labor and delivery process Narrative | http://loinc.org |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 92 |
| http://loinc.org | 23 |
| http://terminology.kemkes.go.id/sp | 18 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 13 |
| http://terminology.kemkes.go.id/CodeSystem/organization-type | 5 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 3 |
| http://terminology.kemkes.go.id/CodeSystem/location-type | 3 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 2 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 2 |
| hhttp://terminology.kemkes.go.id/CodeSystem/organization-type | 2 |
| http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes | 1 |
| **Total** | **164** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 32 | – | Faskes yang Melayani INC | Organization | `Organization.name` |
| 530 | – | Alamat Bersalin | Location | `Location.type.coding` |
| 860 | – | Rujuk | – | `` |
