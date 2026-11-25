# Output Form: SIM RS PKU INC

Sumber: `mapping/phdt-data-dictionary-rs-pku-inc.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-rs-pku-inc.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 66 |
| Code (`jumlah code` = 1) | 179 |
| Code unik (code + CodeSystem) | 166 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 19 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–27 | Patient | – | – | _Nama Ibu_ → `Patient.name.text` (2, tanpa BQ)<br>_NIK_ → `Patient.identifier.value` (6, tanpa BQ)<br>_No HP_ → `Patient.telecom` (7, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (10, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (11, tanpa BQ)<br>_Alamat Domisili_ → `Patient.address.use` (12, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (18, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (21, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.extension.valueCode` (24, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.extension.valueCode` (27, tanpa BQ) |
| 2 | 71–77 | Practitioner | – | – | _NIK_ → `Practitioner.identifier.value` (73, tanpa BQ)<br>_Nama Tenaga Kesehatan_ → `Practitioner.name.text` (75, tanpa BQ)<br>_Jenis Kelamin Tenaga Kesehatan_ → `Practitioner.gender` (76, tanpa BQ) |
| 3 | 78–85 | PractitionerRole | – | – | _Tenaga Pemeriksa_ → `PractitionerRole.code.coding` (82, tanpa BQ) |
| 4 | 87–102 | Encounter | – | – | _Jenis Kunjungan INC_ → `Encounter.class` (88, tanpa BQ)<br>_Tanggal Masuk INC_ → `Encounter.period.start` (97, tanpa BQ)<br>_Tanggal Keluar INC_ → `Encounter.period.end` (98, tanpa BQ)<br>_Tempat Pelayanan INC_ → `Encounter.location.location.display` (100, tanpa BQ) |
| 5 | 103–111 | Condition | 386337006 | Intrapartal care | _Diagnosis Masuk_ → `Condition.code.coding` (105, tanpa BQ) |
| 6 | 122–135 | EpisodeOfCare | ANC | Antenatal Care | _HPHT_ → `EpisodeOfCare.period.start` (125, tanpa BQ)<br>_Tanggal INC (Bersalin)_ → `EpisodeOfCare.period.end` (126, tanpa BQ)<br>_HPHT_ → `EpisodeOfCare.statusHistory.period.start` (128, tanpa BQ)<br>_Tanggal INC (Bersalin)_ → `EpisodeOfCare.statusHistory.period.end` (129, tanpa BQ)<br>_Tanggal INC (Bersalin)_ → `EpisodeOfCare.statusHistory.period.start` (131, tanpa BQ)<br>_Tanggal INC (Bersalin)_ → `EpisodeOfCare.statusHistory.period.end` (132, tanpa BQ) |
| 7 | 137–145 | EpisodeOfCare | PNC | Postnatal Care | _Tanggal INC (Bersalin)_ → `EpisodeOfCare.period.start` (140, tanpa BQ)<br>_Tanggal INC (Bersalin)_ → `EpisodeOfCare.statusHistory.period.start` (142, tanpa BQ) |
| 8 | 146–157 | Observation | SP000383 | Keadaan Ibu Saat Tiba | _Keadaan Ibu Saat Tiba_ → `Observation.valueCodeableConcept.coding` (149, tanpa BQ) |
| 9 | 158–169 | Observation | 8480-6 | Systolic blood pressure | _Tekanan Darah Sistolik_ → `Observation.valueQuantity.value` (161, tanpa BQ) |
| 10 | 170–181 | Observation | 8462-4 | Diastolic blood pressure | _Tekanan Darah Diastolik_ → `Observation.valueQuantity.value` (173, tanpa BQ) |
| 11 | 182–194 | Observation | 8867-4 | Heart rate | _Frekuensi Nadi_ → `Observation.valueQuantity.value` (185, tanpa BQ) |
| 12 | 195–207 | Observation | 9279-1 | Respiratory rate | _Pernapasan_ → `Observation.valueQuantity.value` (198, tanpa BQ) |
| 13 | 208–220 | Observation | – | – | _Suhu Badan_ → `Observation.valueQuantity.value` (211, tanpa BQ) |
| 14 | 221–232 | Observation | 284473002 | Mid upper arm circumference | _LiLA_ → `Observation.valueQuantity.value` (224, tanpa BQ) |
| 15 | 233–244 | Observation | 29463-7 | Body weight | _Berat Badan_ → `Observation.valueQuantity.value` (236, tanpa BQ) |
| 16 | 245–256 | Observation | 8302-2 | Body height | _Tinggi Badan_ → `Observation.valueQuantity.value` (248, tanpa BQ) |
| 17 | 257–268 | Observation | 11996-6 | [#] Pregnancies | _Gravida_ → `Observation.valueInteger` (261, tanpa BQ) |
| 18 | 269–280 | Observation | 11977-6 | [#] Parity | _Partus_ → `Observation.valueInteger` (273, tanpa BQ) |
| 19 | 281–292 | Observation | 69043-8 | Other pregnancy outcomes # | _Abortus_ → `Observation.valueInteger` (285, tanpa BQ) |
| 20 | 293–300 | Condition | – | – | _Kode ICD - Diagnosa_ → `Condition.clinicalStatus.coding` (293, tanpa BQ) |
| 21 | 301–311 | Observation | SP000683 | Tatalaksana Tindakan | _Tatalaksana (Tindakan)_ → `Observation.valueString` (304, tanpa BQ) |
| 22 | 312–322 | Observation | SP000684 | Tatalaksana Obat | _Tatalaksana Obat_ → `Observation.valueString` (315, tanpa BQ) |
| 23 | 323–331 | Condition | 199745000 | Complication occurring during labor and delivery | _Komplikasi_ → `Condition.clinicalStatus.coding` (323, tanpa BQ) |
| 24 | 332–345 | Observation | OC000001 | Jarak kehamilan | _Jarak kehamilan saat ini dengan kehamilan sebelumnya (dalam bulan)_ → `Observation.valueQuantity.value` (336, tanpa BQ) |
| 25 | 346–359 | Observation | 11881-0 | Uterus Fundal height Tape measure | _Tinggi Fundus Uteri_ → `Observation.valueQuantity.value` (349, tanpa BQ)<br>_Detak Jantung Janin_ → `Observation.identifier.value` (359, tanpa BQ) |
| 26 | 360–372 | Observation | 55283-6 | Fetal Heart rate | _Kondisi Detak Jantung Janin_ → `Observation.identifier.value` (372, tanpa BQ) |
| 27 | 373–387 | Observation | 289437007 | Finding of fetal heart rate | _Letak Janin_ → `Observation.identifier.value` (387, tanpa BQ) |
| 28 | 388–400 | Observation | 271692001 | Presentation of fetus | _Presentasi Janin_ → `Observation.identifier.value` (400, tanpa BQ) |
| 29 | 401–420 | Observation | 72155-5 | Position in womb Fetus [RHEA] | _Posisi Kepala Janin terhadap PAP (Pintu Atas Panggul)_ → `Observation.identifier.value` (420, tanpa BQ) |
| 30 | 421–434 | Observation | 249111004 | Engagement of head | _Kondisi Ketuban_ → `Observation.identifier.value` (434, tanpa BQ) |
| 31 | 435–447 | Observation | 289282009 | Amniotic membrane finding | _Faktor risiko INC_ → `Observation.status` (447, tanpa BQ) |
| 32 | 448–458 | Observation | SP000015 | Risiko Masalah Kesehatan | _Integrasi Program_ → `Observation.status` (458, tanpa BQ) |
| 33 | 459–472 | Observation | SP000123 | Integrasi Program | _Tempat Melahirkan_ → `Observation.status` (472, tanpa BQ) |
| 34 | 473–503 | Observation | 72150-6 | Delivery location | – |
| 35 | 519–533 | Observation | 76516-4 | Gestational age—​at birth | _Usia Kehamilan/ Gestasi pada saat Persalinan_ → `Observation.valueQuantity.value` (522, tanpa BQ) |
| 36 | 534–544 | Observation | 93857-1 | Date and time of obstetric delivery | _Tanggal dan Jam Persalinan_ → `Observation.valueDateTime` (537, tanpa BQ) |
| 37 | 545–555 | Observation | OC000013 | Penolong Persalinan | _Nama Penolong Persalinan_ → `Observation.status` (545, tanpa BQ) |
| 38 | 556–569 | Observation | 57071-3 | Obstetric delivery method | _Cara Persalinan_ → `Observation.valueCodeableConcept.coding` (559, tanpa BQ) |
| 39 | 570–588 | Observation | 405195003 | Intrapartum maternal status | _Keadaan Ibu_ → `Observation.valueCodeableConcept.coding` (573, tanpa BQ) |
| 40 | 589–602 | Observation | 387700009 | Prolonged latent phase of labor | _Kala I laten_ → `Observation.valueDateTime` (592, tanpa BQ) |
| 41 | 603–613 | Observation | 249120008 | Onset of labor first stage | _Kala I Aktif_ → `Observation.valueDateTime` (606, tanpa BQ) |
| 42 | 614–627 | Observation | 249160009 | Onset of labor second stage | _Kala II_ → `Observation.valueDateTime` (617, tanpa BQ) |
| 43 | 628–641 | Observation | OC000018 | Onset Kala III | _Kala III_ → `Observation.valueDateTime` (631, tanpa BQ) |
| 44 | 642–653 | Observation | 236994008 | Placental delivery procedure | _Plasenta lahir_ → `Observation.valueDateTime` (645, tanpa BQ) |
| 45 | 654–665 | Observation | 289267004 | Finding of completeness of placenta | _Kondisi Plasenta_ → `Observation.valueCodeableConcept.coding` (657, tanpa BQ) |
| 46 | 666–677 | Procedure | SP000127 | Injeksi Oksitosin | _Injeksi Oksitosin_ → `Procedure.category.coding` (666, tanpa BQ) |
| 47 | 678–689 | Procedure | 302384005 | Controlled cord traction of placenta | _Peregangan Tali Pusat_ → `Procedure.category.coding` (678, tanpa BQ) |
| 48 | 690–701 | Procedure | 236996005 | Abdominal uterine fundal massage | _Masase Fundus Uteri_ → `Procedure.category.coding` (690, tanpa BQ) |
| 49 | 702–715 | Observation | OC000019 | Onset Kala IV | _Kala IV_ → `Observation.valueDateTime` (705, tanpa BQ) |
| 50 | 716–729 | Condition | 9293002 | Atony of uterus | _Kondisi Kala 4_ → `Condition.clinicalStatus.coding` (716, tanpa BQ) |
| 51 | 730–742 | Observation | 719051004 | Quantity of postpartum maternal blood loss | _Jumlah Pendarahan Kala 4 (dalam cc)_ → `Observation.valueQuantity.value` (733, tanpa BQ) |
| 52 | 743–755 | Observation | 8480-6 | Systolic blood pressure | _Sistol Kala 4_ → `Observation.valueQuantity.value` (746, tanpa BQ) |
| 53 | 756–768 | Observation | 8462-4 | Diastolic blood pressure | _Diastol Kala 4_ → `Observation.valueQuantity.value` (759, tanpa BQ) |
| 54 | 769–781 | Procedure | 717809003 | Immediate postpartum care | _Pemantauan Kala 4_ → `Procedure.category.coding` (769, tanpa BQ) |
| 55 | 782–801 | Condition | 199746004 | Obstructed labor | _Komplikasi Persalinan_ → `Condition.clinicalStatus.coding` (782, tanpa BQ) |
| 56 | 802–820 | Observation | SP000379 | Tatalaksana Komplikasi Persalinan | _Tatalaksana Komplikasi Persalinan_ → `Observation.valueCodeableConcept.coding` (805, tanpa BQ) |
| 57 | 821–834 | Observation | 63893-2 | Outcome of pregnancy | _Luaran Kehamilan_ → `Observation.valueCodeableConcept.coding` (824, tanpa BQ) |
| 58 | 835–848 | Observation | 63893-2 | Outcome of pregnancy | _Luaran Kehamilan_ → `Observation.valueCodeableConcept.coding` (838, tanpa BQ) |
| 59 | 850–871 | ServiceRequest | 409014006 | Delivery care management | _Faskes Rujukan_ → `ServiceRequest.locationCode.coding` (863, tanpa BQ)<br>_Nama Faskes Rujukan_ → `ServiceRequest.locationCode.text` (871, tanpa BQ) |
| 60 | 872–884 | Observation | SP000122 | Catat di Buku KIA | _Catat di buku KIA_ → `Observation.valueBoolean` (874, tanpa BQ) |
| 61 | 885–900 | Procedure | SP000130 | Menggunakan Partograf | _Pelayanan Menggunakan Partograf_ → `Procedure.category.coding` (885, tanpa BQ)<br>_Inisiasi Menyusu Dini (IMD)_ → `Procedure.category.coding` (896, tanpa BQ) |
| 62 | 901–908 | Procedure | 431868002 | Initiation of breastfeeding | – |
| 63 | 909–921 | Observation | OC000016 | Waktu Inisiasi Menyusui Dini | _Waktu Inisiasi Menyusu Dini (IMD)_ → `Observation.valueCodeableConcept.coding` (911, tanpa BQ) |
| 64 | 922–935 | Observation | 365662002 | Finding of amniotic fluid appearance | _Warna Ketuban_ → `Observation.valueCodeableConcept.coding` (924, tanpa BQ) |
| 65 | 936–938 | Procedure | 409063005 | Counselling | _Konseling_ → `Procedure.category.coding` (936, tanpa BQ) |
| 66 | 939–953 | Procedure | 409063005 | Counselling | – |

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
| ServiceRequest | 1 |
| **Total** | **66** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 82 | PractitionerRole | `PractitionerRole.code.coding` | 309453006 | Registered midwife | http://snomed.info/sct |
| 2 | 83 | PractitionerRole | `PractitionerRole.code.coding` | 309367003 | Obstetrician and gynecologist | http://snomed.info/sct |
| 3 | 84 | PractitionerRole | `PractitionerRole.code.coding` | 309343006 | Physician | http://snomed.info/sct |
| 4 | 85 | PractitionerRole | `PractitionerRole.code.coding` | 224535009 | Registered nurse | http://snomed.info/sct |
| 5 | 106 | Condition | `Condition.code.coding` | 386337006 | Intrapartal care | http://snomed.info/sct |
| 6 | 123 | EpisodeOfCare | `EpisodeOfCare.type.coding` | ANC | Antenatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 7 | 138 | EpisodeOfCare | `EpisodeOfCare.type.coding` | PNC | Postnatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 8 | 148 | Observation | `Observation.code.coding` | SP000383 | Keadaan Ibu Saat Tiba | http://terminology.kemkes.go.id/sp |
| 9 | 149 | Observation | `Observation.valueCodeableConcept.coding` | 438949009 | Alive | http://snomed.info/sct |
| 10 | 150 | Observation | `Observation.valueCodeableConcept.coding` | 419099009 | Dead | http://snomed.info/sct |
| 11 | 160 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 12 | 172 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://loinc.org |
| 13 | 184 | Observation | `Observation.code.coding` | 8867-4 | Heart rate | http://loinc.org |
| 14 | 197 | Observation | `Observation.code.coding` | 9279-1 | Respiratory rate | http://loinc.org |
| 15 | 223 | Observation | `Observation.code.coding` | 284473002 | Mid upper arm circumference | http://snomed.info/sct |
| 16 | 235 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 17 | 247 | Observation | `Observation.code.coding` | 8302-2 | Body height | http://loinc.org |
| 18 | 259 | Observation | `Observation.code.coding` | 11996-6 | [#] Pregnancies | http://loinc.org |
| 19 | 260 | Observation | `Observation.code.coding` | ANC.B6.DE24 | Number of pregnancies (gravida) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 20 | 271 | Observation | `Observation.code.coding` | 11977-6 | [#] Parity | http://loinc.org |
| 21 | 272 | Observation | `Observation.code.coding` | ANC.B6.DE32 | Parity | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 22 | 283 | Observation | `Observation.code.coding` | 69043-8 | Other pregnancy outcomes # | http://loinc.org |
| 23 | 284 | Observation | `Observation.code.coding` | ANC.B6.DE25 | Number of miscarriages and/or abortions | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 24 | 303 | Observation | `Observation.code.coding` | SP000683 | Tatalaksana Tindakan | http://terminology.kemkes.go.id/sp |
| 25 | 314 | Observation | `Observation.code.coding` | SP000684 | Tatalaksana Obat | http://terminology.kemkes.go.id/sp |
| 26 | 325 | Condition | `Condition.code.coding` | 199745000 | Complication occurring during labor and delivery | http://snomed.info/sct |
| 27 | 334 | Observation | `Observation.code.coding` | OC000001 | Jarak kehamilan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 28 | 335 | Observation | `Observation.code.coding` | ANC.SS.DE53 | Jarak kehamilan | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 29 | 348 | Observation | `Observation.code.coding` | 11881-0 | Uterus Fundal height Tape measure | http://loinc.org |
| 30 | 361 | Observation | `Observation.code.coding` | 55283-6 | Fetal Heart rate | http://loinc.org |
| 31 | 374 | Observation | `Observation.code.coding` | 289437007 | Finding of fetal heart rate | http://snomed.info/sct |
| 32 | 375 | Observation | `Observation.valueCodeableConcept.coding` | 289441006 | Normal fetal heart rate | http://snomed.info/sct |
| 33 | 376 | Observation | `Observation.valueCodeableConcept.coding` | 289440007 | Fetal heart rate not observed | http://snomed.info/sct |
| 34 | 377 | Observation | `Observation.valueCodeableConcept.coding` | 312668007 | Abnormal fetal heart rate | http://snomed.info/sct |
| 35 | 378 | Observation | `Observation.valueCodeableConcept.coding` | 289439005 | Fetal heart rate absent | http://snomed.info/sct |
| 36 | 389 | Observation | `Observation.code.coding` | 271692001 | Presentation of fetus | http://snomed.info/sct |
| 37 | 390 | Observation | `Observation.valueCodeableConcept.coding` | 398236008 | Intrauterine | http://snomed.info/sct |
| 38 | 391 | Observation | `Observation.valueCodeableConcept.coding` | 298109001 | Ectopic | http://snomed.info/sct |
| 39 | 402 | Observation | `Observation.code.coding` | 72155-5 | Position in womb Fetus [RHEA] | http://loinc.org |
| 40 | 403 | Observation | `Observation.valueCodeableConcept.coding` | 70028003 | Vertex presentation | http://snomed.info/sct |
| 41 | 404 | Observation | `Observation.valueCodeableConcept.coding` | 249083005 | Posterior fontanelle presenting | http://snomed.info/sct |
| 42 | 405 | Observation | `Observation.valueCodeableConcept.coding` | 288203005 | Transverse/oblique lie | http://snomed.info/sct |
| 43 | 406 | Observation | `Observation.valueCodeableConcept.coding` | 23954006 | Acromion presentation | http://snomed.info/sct |
| 44 | 407 | Observation | `Observation.valueCodeableConcept.coding` | 6096002 | Breech presentation | http://snomed.info/sct |
| 45 | 408 | Observation | `Observation.valueCodeableConcept.coding` | 8014007 | Brow presentation of fetus | http://snomed.info/sct |
| 46 | 409 | Observation | `Observation.valueCodeableConcept.coding` | 8017000 | Face presentation | http://snomed.info/sct |
| 47 | 410 | Observation | `Observation.valueCodeableConcept.coding` | 249097002 | Footling breech presentation | http://snomed.info/sct |
| 48 | 411 | Observation | `Observation.valueCodeableConcept.coding` | 124736009 | Compound presentation | http://snomed.info/sct |
| 49 | 422 | Observation | `Observation.code.coding` | 249111004 | Engagement of head | http://snomed.info/sct |
| 50 | 423 | Observation | `Observation.valueCodeableConcept.coding` | 249112006 | Head engaged | http://snomed.info/sct |
| 51 | 424 | Observation | `Observation.valueCodeableConcept.coding` | 62098001 | Head not engaged | http://snomed.info/sct |
| 52 | 425 | Observation | `Observation.dataAbsentReason` | unknown | Unknown | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 53 | 436 | Observation | `Observation.code.coding` | 289282009 | Amniotic membrane finding | http://snomed.info/sct |
| 54 | 437 | Observation | `Observation.valueCodeableConcept.coding` | 249125003 | Intact membranes | http://snomed.info/sct |
| 55 | 438 | Observation | `Observation.valueCodeableConcept.coding` | SP000120 | Non-intact membrane | http://terminology.kemkes.go.id/sp |
| 56 | 449 | Observation | `Observation.code.coding` | SP000015 | Risiko Masalah Kesehatan | http://terminology.kemkes.go.id/sp |
| 57 | 460 | Observation | `Observation.code.coding` | SP000123 | Integrasi Program | http://terminology.kemkes.go.id/sp |
| 58 | 461 | Observation | `Observation.valueCodeableConcept.coding` | SP000046 | Terapi Antiretroviral (ART) | http://terminology.kemkes.go.id/sp |
| 59 | 462 | Observation | `Observation.valueCodeableConcept.coding` | SP000124 | Obat anti malaria | http://terminology.kemkes.go.id/sp |
| 60 | 463 | Observation | `Observation.valueCodeableConcept.coding` | SP000125 | Obar anti hepatitis B | http://terminology.kemkes.go.id/sp |
| 61 | 474 | Observation | `Observation.code.coding` | 72150-6 | Delivery location | http://loinc.org |
| 62 | 475 | Observation | `Observation.valueCodeableConcept.coding` | 264362003 | Home | http://snomed.info/sct |
| 63 | 476 | Observation | `Observation.valueCodeableConcept.coding` | OT000001 | Polindes | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 64 | 477 | Observation | `Observation.valueCodeableConcept.coding` | OT000002 | Pustu | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 65 | 478 | Observation | `Observation.valueCodeableConcept.coding` | 102 | Pusat Kesehatan Masyarakat | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 66 | 479 | Observation | `Observation.valueCodeableConcept.coding` | 103 | Klinik | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 67 | 480 | Observation | `Observation.valueCodeableConcept.coding` | OT000008 | Rumah Bersalin | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 68 | 481 | Observation | `Observation.valueCodeableConcept.coding` | 82242000 | Children’s hospital | http://snomed.info/sct |
| 69 | 482 | Observation | `Observation.valueCodeableConcept.coding` | 104 | Rumah Sakit | hhttp://terminology.kemkes.go.id/CodeSystem/organization-type |
| 70 | 483 | Observation | `Observation.valueCodeableConcept.coding` | OT000003 | RS ODHA | hhttp://terminology.kemkes.go.id/CodeSystem/organization-type |
| 71 | 484 | Observation | `Observation.valueCodeableConcept.coding` | OT000004 | Bidan Praktek Mandiri | hhttp://terminology.kemkes.go.id/CodeSystem/organization-type |
| 72 | 485 | Observation | `Observation.valueCodeableConcept.coding` | LT000008 | Dalam perjalanan dari rumah/masyarakat | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 73 | 486 | Observation | `Observation.valueCodeableConcept.coding` | LT000009 | Dalam perjalanan ke faskes lain | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 74 | 487 | Observation | `Observation.valueCodeableConcept.coding` | OT000006 | Rumah Sakit Pemerintah | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 75 | 488 | Observation | `Observation.valueCodeableConcept.coding` | OT000007 | Rumah Sakit Swasta | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 76 | 489 | Observation | `Observation.valueCodeableConcept.coding` | LT000006 | Rumah Ibu | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 77 | 490 | Observation | `Observation.valueCodeableConcept.coding` | OT000010 | Klinik Medis Utama | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 78 | 491 | Observation | `Observation.valueCodeableConcept.coding` | OT000011 | Klinik Medis Pratama | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 79 | 492 | Observation | `Observation.valueCodeableConcept.coding` | 101 | Tempat Praktik Mandiri Tenaga Kesehatan | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 80 | 493 | Observation | `Observation.valueCodeableConcept.coding` | 394573001 | Maternity clinic | http://snomed.info/sct |
| 81 | 494 | Observation | `Observation.valueCodeableConcept.coding` | LT000007 | Rumah Dukun | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 82 | 495 | Observation | `Observation.valueCodeableConcept.coding` | LT000010 | Lainnya | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 83 | 496 | Observation | `Observation.valueCodeableConcept.coding` | LT000011 | Belum Tahu | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 84 | 521 | Observation | `Observation.code.coding` | 76516-4 | Gestational age—​at birth | http://loinc.org |
| 85 | 524 | Observation | `Observation.component.code.coding` | SP000398 | Usia Kehamilan Saat Persalinan (hari) | http://terminology.kemkes.go.id/sp |
| 86 | 536 | Observation | `Observation.code.coding` | 93857-1 | Date and time of obstetric delivery | http://loinc.org |
| 87 | 547 | Observation | `Observation.code.coding` | OC000013 | Penolong Persalinan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 88 | 558 | Observation | `Observation.code.coding` | 57071-3 | Obstetric delivery method | http://loinc.org |
| 89 | 559 | Observation | `Observation.valueCodeableConcept.coding` | 48782003 | Delivery normal | http://snomed.info/sct |
| 90 | 560 | Observation | `Observation.valueCodeableConcept.coding` | 200138003 | Vacuum extractor delivery - delivered | http://snomed.info/sct |
| 91 | 561 | Observation | `Observation.valueCodeableConcept.coding` | 200130005 | Forceps delivery - delivered | http://snomed.info/sct |
| 92 | 562 | Observation | `Observation.valueCodeableConcept.coding` | 200144004 | Deliveries by cesarean | http://snomed.info/sct |
| 93 | 572 | Observation | `Observation.code.coding` | 405195003 | Intrapartum maternal status | http://snomed.info/sct |
| 94 | 573 | Observation | `Observation.valueCodeableConcept.coding` | 102514002 | Well female adult | http://snomed.info/sct |
| 95 | 574 | Observation | `Observation.valueCodeableConcept.coding` | 438949009 | Alive | http://snomed.info/sct |
| 96 | 575 | Observation | `Observation.valueCodeableConcept.coding` | 39104002 | Illness | http://snomed.info/sct |
| 97 | 576 | Observation | `Observation.valueCodeableConcept.coding` | 131148009 | Bleeding | http://snomed.info/sct |
| 98 | 577 | Observation | `Observation.valueCodeableConcept.coding` | 386661006 | Fever | http://snomed.info/sct |
| 99 | 578 | Observation | `Observation.valueCodeableConcept.coding` | 91175000 | Seizure | http://snomed.info/sct |
| 100 | 579 | Observation | `Observation.valueCodeableConcept.coding` | 249215002 | Odor of lochia | http://snomed.info/sct |
| 101 | 580 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 102 | 581 | Observation | `Observation.valueCodeableConcept.coding` | 59283008 | Maternal death | http://snomed.info/sct |
| 103 | 591 | Observation | `Observation.code.coding` | 387700009 | Prolonged latent phase of labor | http://snomed.info/sct |
| 104 | 605 | Observation | `Observation.code.coding` | 249120008 | Onset of labor first stage | http://snomed.info/sct |
| 105 | 616 | Observation | `Observation.code.coding` | 249160009 | Onset of labor second stage | http://snomed.info/sct |
| 106 | 630 | Observation | `Observation.code.coding` | OC000018 | Onset Kala III | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 107 | 644 | Observation | `Observation.code.coding` | 236994008 | Placental delivery procedure | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 108 | 656 | Observation | `Observation.code.coding` | 289267004 | Finding of completeness of placenta | http://snomed.info/sct |
| 109 | 657 | Observation | `Observation.valueCodeableConcept.coding` | 249170006 | Complete placenta at delivery | http://snomed.info/sct |
| 110 | 658 | Observation | `Observation.valueCodeableConcept.coding` | 268479002 | Incomplete placenta at delivery | http://snomed.info/sct |
| 111 | 669 | Procedure | `Procedure.code.coding` | SP000127 | Injeksi Oksitosin | http://terminology.kemkes.go.id/sp |
| 112 | 681 | Procedure | `Procedure.code.coding` | 302384005 | Controlled cord traction of placenta | http://snomed.info/sct |
| 113 | 693 | Procedure | `Procedure.code.coding` | 236996005 | Abdominal uterine fundal massage | http://snomed.info/sct |
| 114 | 704 | Observation | `Observation.code.coding` | OC000019 | Onset Kala IV | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 115 | 718 | Condition | `Condition.code.coding` | 9293002 | Atony of uterus | http://snomed.info/sct |
| 116 | 719 | Condition | `Condition.code.coding` | 48194001 | Postpartum hemorrhage | http://snomed.info/sct |
| 117 | 720 | Condition | `Condition.code.coding` | 1148943004 | Retention of placenta and uterine membrane | http://snomed.info/sct |
| 118 | 721 | Condition | `Condition.code.coding` | 283380005 | Laceration of perineum | http://snomed.info/sct |
| 119 | 722 | Condition | `Condition.code.coding` | 84007008 | Shock during AND/OR following labor AND/OR delivery | http://snomed.info/sct |
| 120 | 723 | Condition | `Condition.code.coding` | 118216002 | Labor finding | http://snomed.info/sct |
| 121 | 724 | Condition | `Condition.code.coding` | 10756061000119109 | Pain during postpartum period due to and following cesarean section | http://snomed.info/sct |
| 122 | 732 | Observation | `Observation.code.coding` | 719051004 | Quantity of postpartum maternal blood loss | http://snomed.info/sct |
| 123 | 745 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 124 | 758 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://snomed.info/sct |
| 125 | 772 | Procedure | `Procedure.code.coding` | 717809003 | Immediate postpartum care | http://snomed.info/sct |
| 126 | 784 | Condition | `Condition.code.coding` | 199746004 | Obstructed labor | http://snomed.info/sct |
| 127 | 785 | Condition | `Condition.code.coding` | 48194001 | Pregnancy-induced hypertension | http://snomed.info/sct |
| 128 | 786 | Condition | `Condition.code.coding` | 38010008 | Intrapartum hemorrhage | http://snomed.info/sct |
| 129 | 787 | Condition | `Condition.code.coding` | 40733004 | Infectious disease | http://snomed.info/sct |
| 130 | 788 | Condition | `Condition.code.coding` | 386639001 | Termination of pregnancy | http://snomed.info/sct |
| 131 | 789 | Condition | `Condition.code.coding` | 44223004 | Premature rupture of membranes | http://snomed.info/sct |
| 132 | 790 | Condition | `Condition.code.coding` | 38341003 | Hypertensive disorder, systemic arterial | http://snomed.info/sct |
| 133 | 791 | Condition | `Condition.code.coding` | 398254007 | Pre-eclampsia | http://snomed.info/sct |
| 134 | 792 | Condition | `Condition.code.coding` | 15938005 | Eclampsia | http://snomed.info/sct |
| 135 | 793 | Condition | `Condition.code.coding` | 9293002 | Atony of uterus | http://snomed.info/sct |
| 136 | 794 | Condition | `Condition.code.coding` | 283380005 | Laceration of perineum | http://snomed.info/sct |
| 137 | 795 | Condition | `Condition.code.coding` | 199745000 | Complication occurring during labor and delivery | http://snomed.info/sct |
| 138 | 804 | Observation | `Observation.code.coding` | SP000379 | Tatalaksana Komplikasi Persalinan | http://terminology.kemkes.go.id/sp |
| 139 | 805 | Observation | `Observation.valueCodeableConcept.coding` | 430701006 | Resuscitation using intravenous fluid | http://snomed.info/sct |
| 140 | 806 | Observation | `Observation.valueCodeableConcept.coding` | SP000156 | Pemberian Obat Uterotonik | http://terminology.kemkes.go.id/sp |
| 141 | 807 | Observation | `Observation.valueCodeableConcept.coding` | 236998006 | Bimanual uterine massage | http://snomed.info/sct |
| 142 | 808 | Observation | `Observation.valueCodeableConcept.coding` | 360362007 | Suture of laceration of perineum | http://snomed.info/sct |
| 143 | 809 | Observation | `Observation.valueCodeableConcept.coding` | 28233006 | Manual removal of retained placenta | http://snomed.info/sct |
| 144 | 810 | Observation | `Observation.valueCodeableConcept.coding` | SP000013 | Pemberian MgSO4 | http://terminology.kemkes.go.id/sp |
| 145 | 811 | Observation | `Observation.valueCodeableConcept.coding` | 308116003 | Antihypertensive therapy | http://snomed.info/sct |
| 146 | 812 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 147 | 823 | Observation | `Observation.code.coding` | 63893-2 | Outcome of pregnancy | http://loinc.org |
| 148 | 824 | Observation | `Observation.valueCodeableConcept.coding` | LA14270-5 | Live birth | http://loinc.org |
| 149 | 825 | Observation | `Observation.valueCodeableConcept.coding` | LA14271-3 | Stillborn | http://loinc.org |
| 150 | 826 | Observation | `Observation.valueCodeableConcept.coding` | LA14272-1 | Miscarriage | http://loinc.org |
| 151 | 827 | Observation | `Observation.valueCodeableConcept.coding` | LA14273-9 | Induced abortion | http://loinc.org |
| 152 | 837 | Observation | `Observation.code.coding` | 63893-2 | Outcome of pregnancy | http://loinc.org |
| 153 | 838 | Observation | `Observation.valueCodeableConcept.coding` | LA14270-5 | Live birth | http://loinc.org |
| 154 | 839 | Observation | `Observation.valueCodeableConcept.coding` | LA14271-3 | Stillborn | http://loinc.org |
| 155 | 840 | Observation | `Observation.valueCodeableConcept.coding` | LA14272-1 | Miscarriage | http://loinc.org |
| 156 | 841 | Observation | `Observation.valueCodeableConcept.coding` | LA14273-9 | Induced abortion | http://loinc.org |
| 157 | 854 | ServiceRequest | `ServiceRequest.code.coding` | 409014006 | Delivery care management | http://snomed.info/sct |
| 158 | 863 | ServiceRequest | `ServiceRequest.locationCode.coding` | SP000129 | Puskesmas PONED | http://terminology.kemkes.go.id/sp |
| 159 | 867 | ServiceRequest | `ServiceRequest.locationCode.coding` | SP000128 | Rumah Sakit Ibu dan Anak | http://terminology.kemkes.go.id/sp |
| 160 | 873 | Observation | `Observation.code.coding` | SP000122 | Catat di Buku KIA | http://terminology.kemkes.go.id/sp |
| 161 | 876 | Observation | `Observation.dataAbsentReason.coding` | not-applicable | Not Applicable | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 162 | 888 | Procedure | `Procedure.code.coding` | SP000130 | Menggunakan Partograf | http://terminology.kemkes.go.id/sp |
| 163 | 901 | Procedure | `Procedure.code.coding` | 431868002 | Initiation of breastfeeding | http://snomed.info/sct |
| 164 | 910 | Observation | `Observation.code.coding` | OC000016 | Waktu Inisiasi Menyusui Dini | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 165 | 911 | Observation | `Observation.valueCodeableConcept.coding` | OV000014 | Kurang dari 1 Jam | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 166 | 913 | Observation | `Observation.valueCodeableConcept.coding` | OV000015 | Lebih dari 1 Jam | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 167 | 923 | Observation | `Observation.code.coding` | 365662002 | Finding of amniotic fluid appearance | http://snomed.info/sct |
| 168 | 924 | Observation | `Observation.valueCodeableConcept.coding` | 168090003 | Amniotic fluid clear | http://snomed.info/sct |
| 169 | 925 | Observation | `Observation.valueCodeableConcept.coding` | 408781009 | Straw colored amniotic fluid | http://snomed.info/sct |
| 170 | 926 | Observation | `Observation.valueCodeableConcept.coding` | 249134008 | Bloodstained liquor | http://snomed.info/sct |
| 171 | 927 | Observation | `Observation.valueCodeableConcept.coding` | 168092006 | Amniotic fluid -meconium stain | http://snomed.info/sct |
| 172 | 938 | Procedure | `Procedure.code.coding` | 409063005 | Counselling | http://snomed.info/sct |
| 173 | 940 | Procedure | `Procedure.code.coding` | 409063005 | Counselling | http://snomed.info/sct |
| 174 | 941 | Procedure | `Procedure.code.coding` | ED000008 | Edukasi Tanda Bahaya Kehamilan, Bersalin dan Nifas | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 175 | 942 | Procedure | `Procedure.code.coding` | SP000121 | Edukasi Tanda Bahaya Baru Lahir | http://terminology.kemkes.go.id/sp |
| 176 | 943 | Procedure | `Procedure.code.coding` | ED000009 | Edukasi IMD dan ASI Eksklusif | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 177 | 944 | Procedure | `Procedure.code.coding` | ED000005 | Edukasi Gizi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 178 | 945 | Procedure | `Procedure.code.coding` | PC000001 | Perawatan Tali Pusat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 179 | 946 | Procedure | `Procedure.code.coding` | ED000010 | Edukasi PHBS | http://terminology.kemkes.go.id/CodeSystem/clinical-term |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 93 |
| http://loinc.org | 27 |
| http://terminology.kemkes.go.id/sp | 19 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 13 |
| http://terminology.kemkes.go.id/CodeSystem/organization-type | 10 |
| http://terminology.kemkes.go.id/CodeSystem/location-type | 6 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 3 |
| hhttp://terminology.kemkes.go.id/CodeSystem/organization-type | 3 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 2 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 2 |
| http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes | 1 |
| **Total** | **179** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 32 | – | Faskes yang Melayani INC | Organization | `Organization.name` |
| 47 | – | Tempat Pelayanan INC | Location | `Location.identifier` |
| 504 | – | Alamat Bersalin | Location | `Location.type.coding` |
| 849 | – | Rujuk | – | `` |
