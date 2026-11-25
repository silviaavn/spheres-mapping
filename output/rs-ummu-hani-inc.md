# Output Form: SIM RS Ummu Hani INC

Sumber: `mapping/phdt-data-dictionary-rs-ummu-hani-inc.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-rs-ummu-hani-inc.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 41 |
| Code (`jumlah code` = 1) | 97 |
| Code unik (code + CodeSystem) | 85 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 9 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–27 | Patient | – | – | _Nama Ibu_ → `Patient.name.text` (2, tanpa BQ)<br>_NIK_ → `Patient.identifier.value` (6, tanpa BQ)<br>_No HP_ → `Patient.telecom` (7, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (10, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (11, tanpa BQ)<br>_Alamat Domisili_ → `Patient.address.line` (13, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (18, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (21, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.extension.valueCode` (24, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.extension.valueCode` (27, tanpa BQ) |
| 2 | 28–35 | RelatedPerson | – | – | _Nama Suami/ Pendamping_ → `RelatedPerson.patient.reference` (28, tanpa BQ)<br>_NIK Suami/ Pendamping_ → `RelatedPerson.identifier` (32, tanpa BQ) |
| 3 | 75–79 | Practitioner | – | – | _NIK_ → `Practitioner.identifier.value` (77, tanpa BQ)<br>_Nama Tenaga Kesehatan_ → `Practitioner.name.text` (79, tanpa BQ) |
| 4 | 80–89 | PractitionerRole | – | – | _Tenaga Pemeriksa_ → `PractitionerRole.code.coding` (84, tanpa BQ) |
| 5 | 90–94 | Practitioner | – | – | _NIK_ → `Practitioner.identifier.value` (92, tanpa BQ)<br>_Nama Tenaga Kesehatan_ → `Practitioner.name.text` (94, tanpa BQ) |
| 6 | 95–104 | PractitionerRole | – | – | _Tenaga Pemeriksa_ → `PractitionerRole.code.coding` (99, tanpa BQ) |
| 7 | 105–109 | Practitioner | – | – | _NIK Pencatat_ → `Practitioner.identifier.value` (107, tanpa BQ)<br>_Nama Pencatat_ → `Practitioner.name.text` (109, tanpa BQ) |
| 8 | 110–118 | PractitionerRole | – | – | _Role Pencatat_ → `PractitionerRole.code.coding` (114, tanpa BQ) |
| 9 | 120–135 | Encounter | – | – | _Jenis Kunjungan INC_ → `Encounter.class` (121, tanpa BQ)<br>_Tanggal Masuk INC_ → `Encounter.period.start` (130, tanpa BQ)<br>_Tanggal Keluar INC_ → `Encounter.period.end` (131, tanpa BQ)<br>_Tempat Pelayanan INC_ → `Encounter.location.location.display` (133, tanpa BQ) |
| 10 | 136–144 | Condition | 386337006.0 | Intrapartal care | _Diagnosis Masuk_ → `Condition.code.coding` (138, tanpa BQ) |
| 11 | 155–168 | EpisodeOfCare | ANC | Antenatal Care | – |
| 12 | 170–178 | EpisodeOfCare | PNC | Postnatal Care | – |
| 13 | 179–190 | Observation | SP000383 | Keadaan Ibu Saat Tiba | _Keadaan Ibu Saat Tiba_ → `Observation.valueCodeableConcept.coding` (182, tanpa BQ) |
| 14 | 191–202 | Observation | 246435002.0 | Number of fetuses | _Jumlah Janin_ → `Observation.valueInteger` (195, tanpa BQ) |
| 15 | 203–213 | Observation | 81956-5 | Date and time of death [TimeStamp] | _Waktu Kematian_ → `Observation.valueDateTime` (206, tanpa BQ) |
| 16 | 214–224 | Observation | 79378-6 | Cause of death | _Diagnosa Penyebab Kematian_ → `Observation.valueString` (217, tanpa BQ) |
| 17 | 225–236 | Observation | 8480-6 | Systolic blood pressure | _Tekanan Darah Sistolik_ → `Observation.valueQuantity.value` (228, tanpa BQ) |
| 18 | 237–248 | Observation | 8462-4 | Diastolic blood pressure | _Tekanan Darah Diastolik_ → `Observation.valueQuantity.value` (240, tanpa BQ) |
| 19 | 249–261 | Observation | 8867-4 | Heart rate | _Frekuensi Nadi_ → `Observation.valueQuantity.value` (252, tanpa BQ) |
| 20 | 262–274 | Observation | 9279-1 | Respiratory rate | _Pernapasan_ → `Observation.valueQuantity.value` (265, tanpa BQ) |
| 21 | 275–287 | Observation | – | – | _Suhu Badan_ → `Observation.valueQuantity.value` (278, tanpa BQ) |
| 22 | 288–302 | Observation | 11881-0 | Uterus Fundal height Tape measure | _Tinggi Fundus Uteri_ → `Observation.valueQuantity.value` (291, tanpa BQ)<br>_Detak Jantung Janin_ → `Observation.identifier.value` (302, tanpa BQ) |
| 23 | 303–315 | Observation | 55283-6 | Fetal Heart rate | _Letak Janin_ → `Observation.identifier.value` (315, tanpa BQ) |
| 24 | 316–328 | Observation | 271692001.0 | Presentation of fetus | _Presentasi Janin_ → `Observation.identifier.value` (328, tanpa BQ) |
| 25 | 329–349 | Observation | 72155-5 | Position in womb Fetus [RHEA] | _Posisi Kepala Janin terhadap PAP (Pintu Atas Panggul)_ → `Observation.identifier.value` (349, tanpa BQ) |
| 26 | 350–363 | Observation | 249111004.0 | Engagement of head | _Kondisi Ketuban_ → `Observation.identifier.value` (363, tanpa BQ) |
| 27 | 364–376 | Observation | 289282009.0 | Amniotic membrane finding | _Faktor risiko INC_ → `Observation.status` (376, tanpa BQ) |
| 28 | 377–387 | Observation | SP000015 | Risiko Masalah Kesehatan | – |
| 29 | 388–402 | Observation | 76516-4 | Gestational age—​at birth | _Usia Kehamilan Saat Gestasi (minggu)_ → `Observation.valueQuantity.value` (390, tanpa BQ)<br>_Usia Kehamilan Saat Gestasi (hari)_ → `Observation.component.valueQuantity.value` (393, tanpa BQ)<br>_Tanggal dan Jam Persalinan_ → `Observation.status` (402, tanpa BQ) |
| 30 | 403–413 | Observation | 93857-1 | Date and time of obstetric delivery | _Cara Persalinan_ → `Observation.status` (413, tanpa BQ) |
| 31 | 414–428 | Observation | 57071-3 | Obstetric delivery method | – |
| 32 | 429–446 | Observation | 405195003.0 | Intrapartum maternal status | _Keadaan Ibu_ → `Observation.valueCodeableConcept.coding` (431, tanpa BQ) |
| 33 | 447–455 | Condition | 199745000.0 | Complication occurring during labor and delivery | _Komplikasi Persalinan_ → `Condition.clinicalStatus.coding` (447, tanpa BQ) |
| 34 | 456–466 | Observation | SP000379 | Tatalaksana Komplikasi Persalinan | _Tatalaksana Komplikasi Persalinan_ → `Observation.valueString` (459, tanpa BQ) |
| 35 | 467–480 | Observation | 63893-2 | Outcome of pregnancy | _Luaran Kehamilan_ → `Observation.valueCodeableConcept.coding` (470, tanpa BQ) |
| 36 | 481–491 | Procedure | SP000130 | Menggunakan Partograf | _Pelayanan Menggunakan Partograf_ → `Procedure.category.coding` (481, tanpa BQ) |
| 37 | 492–502 | Procedure | 431868002.0 | Initiation of breastfeeding | _Inisiasi Menyusu Dini (IMD)_ → `Procedure.category.coding` (492, tanpa BQ) |
| 38 | 503–505 | Procedure | 409063005.0 | Counselling | _Konseling_ → `Procedure.category.coding` (503, tanpa BQ) |
| 39 | 506–521 | Procedure | 409063005.0 | Counselling | – |
| 40 | 522–535 | Observation | 365662002.0 | Finding of amniotic fluid appearance | _Warna Ketuban_ → `Observation.valueCodeableConcept.coding` (524, tanpa BQ) |
| 41 | 538–559 | ServiceRequest | 409014006.0 | Delivery care management | _Faskes Rujukan_ → `ServiceRequest.locationCode.coding` (551, tanpa BQ)<br>_Nama Faskes Rujukan_ → `ServiceRequest.locationCode.text` (559, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 23 |
| Procedure | 4 |
| Practitioner | 3 |
| PractitionerRole | 3 |
| Condition | 2 |
| EpisodeOfCare | 2 |
| Patient | 1 |
| RelatedPerson | 1 |
| Encounter | 1 |
| ServiceRequest | 1 |
| **Total** | **41** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 84 | PractitionerRole | `PractitionerRole.code.coding` | 309453006.0 | Registered midwife | http://snomed.info/sct |
| 2 | 85 | PractitionerRole | `PractitionerRole.code.coding` | 309367003.0 | Obstetrician and gynecologist | http://snomed.info/sct |
| 3 | 86 | PractitionerRole | `PractitionerRole.code.coding` | 309343006.0 | Physician | http://snomed.info/sct |
| 4 | 87 | PractitionerRole | `PractitionerRole.code.coding` | 224535009.0 | Registered nurse | http://snomed.info/sct |
| 5 | 88 | PractitionerRole | `PractitionerRole.code.coding` | 224535009.0 | Registered nurse | http://snomed.info/sct |
| 6 | 99 | PractitionerRole | `PractitionerRole.code.coding` | 309453006.0 | Registered midwife | http://snomed.info/sct |
| 7 | 100 | PractitionerRole | `PractitionerRole.code.coding` | 309367003.0 | Obstetrician and gynecologist | http://snomed.info/sct |
| 8 | 101 | PractitionerRole | `PractitionerRole.code.coding` | 309343006.0 | Physician | http://snomed.info/sct |
| 9 | 102 | PractitionerRole | `PractitionerRole.code.coding` | 224535009.0 | Registered nurse | http://snomed.info/sct |
| 10 | 103 | PractitionerRole | `PractitionerRole.code.coding` | 224535009.0 | Registered nurse | http://snomed.info/sct |
| 11 | 114 | PractitionerRole | `PractitionerRole.code.coding` | 309453006.0 | Registered midwife | http://snomed.info/sct |
| 12 | 115 | PractitionerRole | `PractitionerRole.code.coding` | 309367003.0 | Obstetrician and gynecologist | http://snomed.info/sct |
| 13 | 116 | PractitionerRole | `PractitionerRole.code.coding` | 309343006.0 | Physician | http://snomed.info/sct |
| 14 | 117 | PractitionerRole | `PractitionerRole.code.coding` | 224535009.0 | Registered nurse | http://snomed.info/sct |
| 15 | 118 | PractitionerRole | `PractitionerRole.code.coding` | 56542007.0 | Medical record administrator | http://snomed.info/sct |
| 16 | 139 | Condition | `Condition.code.coding` | 386337006.0 | Intrapartal care | http://snomed.info/sct |
| 17 | 156 | EpisodeOfCare | `EpisodeOfCare.type.coding` | ANC | Antenatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 18 | 171 | EpisodeOfCare | `EpisodeOfCare.type.coding` | PNC | Postnatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 19 | 181 | Observation | `Observation.code.coding` | SP000383 | Keadaan Ibu Saat Tiba | http://terminology.kemkes.go.id/sp |
| 20 | 182 | Observation | `Observation.valueCodeableConcept.coding` | 438949009.0 | Alive | http://snomed.info/sct |
| 21 | 183 | Observation | `Observation.valueCodeableConcept.coding` | 419099009.0 | Dead | http://snomed.info/sct |
| 22 | 193 | Observation | `Observation.code.coding` | 246435002.0 | Number of fetuses | http://snomed.info/sct |
| 23 | 194 | Observation | `Observation.code.coding` | ANC.B8.DE109 | Number of fetuses | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 24 | 205 | Observation | `Observation.code.coding` | 81956-5 | Date and time of death [TimeStamp] | http://loinc.org |
| 25 | 216 | Observation | `Observation.code.coding` | 79378-6 | Cause of death | http://loinc.org |
| 26 | 227 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 27 | 239 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://loinc.org |
| 28 | 251 | Observation | `Observation.code.coding` | 8867-4 | Heart rate | http://loinc.org |
| 29 | 264 | Observation | `Observation.code.coding` | 9279-1 | Respiratory rate | http://loinc.org |
| 30 | 290 | Observation | `Observation.code.coding` | 11881-0 | Uterus Fundal height Tape measure | http://loinc.org |
| 31 | 304 | Observation | `Observation.code.coding` | 55283-6 | Fetal Heart rate | http://loinc.org |
| 32 | 317 | Observation | `Observation.code.coding` | 271692001.0 | Presentation of fetus | http://snomed.info/sct |
| 33 | 318 | Observation | `Observation.valueCodeableConcept.coding` | 398236008.0 | Intrauterine | http://snomed.info/sct |
| 34 | 319 | Observation | `Observation.valueCodeableConcept.coding` | 298109001.0 | Ectopic | http://snomed.info/sct |
| 35 | 330 | Observation | `Observation.code.coding` | 72155-5 | Position in womb Fetus [RHEA] | http://loinc.org |
| 36 | 331 | Observation | `Observation.valueCodeableConcept.coding` | 1209182005.0 | Cephalic fetal presentation | http://snomed.info/sct |
| 37 | 332 | Observation | `Observation.valueCodeableConcept.coding` | 70028003.0 | Vertex presentation | http://snomed.info/sct |
| 38 | 333 | Observation | `Observation.valueCodeableConcept.coding` | 249083005.0 | Posterior fontanelle presenting | http://snomed.info/sct |
| 39 | 334 | Observation | `Observation.valueCodeableConcept.coding` | 288203005.0 | Transverse/oblique lie | http://snomed.info/sct |
| 40 | 335 | Observation | `Observation.valueCodeableConcept.coding` | 23954006.0 | Acromion presentation | http://snomed.info/sct |
| 41 | 336 | Observation | `Observation.valueCodeableConcept.coding` | 6096002.0 | Breech presentation | http://snomed.info/sct |
| 42 | 337 | Observation | `Observation.valueCodeableConcept.coding` | 8014007.0 | Brow presentation of fetus | http://snomed.info/sct |
| 43 | 338 | Observation | `Observation.valueCodeableConcept.coding` | 8017000.0 | Face presentation | http://snomed.info/sct |
| 44 | 339 | Observation | `Observation.valueCodeableConcept.coding` | 249097002.0 | Footling breech presentation | http://snomed.info/sct |
| 45 | 340 | Observation | `Observation.valueCodeableConcept.coding` | 124736009.0 | Compound presentation | http://snomed.info/sct |
| 46 | 351 | Observation | `Observation.code.coding` | 249111004.0 | Engagement of head | http://snomed.info/sct |
| 47 | 352 | Observation | `Observation.valueCodeableConcept.coding` | 249112006.0 | Head engaged | http://snomed.info/sct |
| 48 | 353 | Observation | `Observation.valueCodeableConcept.coding` | 62098001.0 | Head not engaged | http://snomed.info/sct |
| 49 | 354 | Observation | `Observation.dataAbsentReason` | unknown | Unknown | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 50 | 365 | Observation | `Observation.code.coding` | 289282009.0 | Amniotic membrane finding | http://snomed.info/sct |
| 51 | 366 | Observation | `Observation.valueCodeableConcept.coding` | 249125003.0 | Intact membranes | http://snomed.info/sct |
| 52 | 367 | Observation | `Observation.valueCodeableConcept.coding` | SP000120 | Non-intact membrane | http://terminology.kemkes.go.id/sp |
| 53 | 378 | Observation | `Observation.code.coding` | SP000015 | Risiko Masalah Kesehatan | http://terminology.kemkes.go.id/sp |
| 54 | 389 | Observation | `Observation.code.coding` | 76516-4 | Gestational age—​at birth | http://loinc.org |
| 55 | 392 | Observation | `Observation.component.code.coding` | SP000398 | Usia Kehamilan Saat Persalinan (hari) | http://terminology.kemkes.go.id/sp |
| 56 | 404 | Observation | `Observation.code.coding` | 93857-1 | Date and time of obstetric delivery | http://loinc.org |
| 57 | 415 | Observation | `Observation.code.coding` | 57071-3 | Obstetric delivery method | http://loinc.org |
| 58 | 416 | Observation | `Observation.valueCodeableConcept.coding` | 48782003.0 | Delivery normal | http://snomed.info/sct |
| 59 | 417 | Observation | `Observation.valueCodeableConcept.coding` | 200138003.0 | Vacuum extractor delivery - delivered | http://snomed.info/sct |
| 60 | 418 | Observation | `Observation.valueCodeableConcept.coding` | 200130005.0 | Forceps delivery - delivered | http://snomed.info/sct |
| 61 | 419 | Observation | `Observation.valueCodeableConcept.coding` | 200144004.0 | Deliveries by cesarean | http://snomed.info/sct |
| 62 | 420 | Observation | `Observation.valueCodeableConcept.coding` | 289259007.0 | Vaginal delivery | http://snomed.info/sct |
| 63 | 430 | Observation | `Observation.code.coding` | 405195003.0 | Intrapartum maternal status | http://snomed.info/sct |
| 64 | 431 | Observation | `Observation.valueCodeableConcept.coding` | 438949009.0 | Alive | http://snomed.info/sct |
| 65 | 432 | Observation | `Observation.valueCodeableConcept.coding` | 102514002.0 | Well female adult | http://snomed.info/sct |
| 66 | 433 | Observation | `Observation.valueCodeableConcept.coding` | 39104002.0 | Illness | http://snomed.info/sct |
| 67 | 434 | Observation | `Observation.valueCodeableConcept.coding` | 131148009.0 | Bleeding | http://snomed.info/sct |
| 68 | 435 | Observation | `Observation.valueCodeableConcept.coding` | 386661006.0 | Fever | http://snomed.info/sct |
| 69 | 436 | Observation | `Observation.valueCodeableConcept.coding` | 91175000.0 | Seizure | http://snomed.info/sct |
| 70 | 437 | Observation | `Observation.valueCodeableConcept.coding` | 249215002.0 | Odor of lochia | http://snomed.info/sct |
| 71 | 438 | Observation | `Observation.valueCodeableConcept.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 72 | 439 | Observation | `Observation.valueCodeableConcept.coding` | 59283008.0 | Maternal death | http://snomed.info/sct |
| 73 | 449 | Condition | `Condition.code.coding` | 199745000.0 | Complication occurring during labor and delivery | http://snomed.info/sct |
| 74 | 458 | Observation | `Observation.code.coding` | SP000379 | Tatalaksana Komplikasi Persalinan | http://terminology.kemkes.go.id/sp |
| 75 | 469 | Observation | `Observation.code.coding` | 63893-2 | Outcome of pregnancy | http://loinc.org |
| 76 | 470 | Observation | `Observation.valueCodeableConcept.coding` | LA14270-5 | Live birth | http://loinc.org |
| 77 | 471 | Observation | `Observation.valueCodeableConcept.coding` | LA14271-3 | Stillborn | http://loinc.org |
| 78 | 472 | Observation | `Observation.valueCodeableConcept.coding` | LA14272-1 | Miscarriage | http://loinc.org |
| 79 | 473 | Observation | `Observation.valueCodeableConcept.coding` | LA14273-9 | Induced abortion | http://loinc.org |
| 80 | 484 | Procedure | `Procedure.code.coding` | SP000130 | Menggunakan Partograf | http://terminology.kemkes.go.id/sp |
| 81 | 495 | Procedure | `Procedure.code.coding` | 431868002.0 | Initiation of breastfeeding | http://snomed.info/sct |
| 82 | 505 | Procedure | `Procedure.code.coding` | 409063005.0 | Counselling | http://snomed.info/sct |
| 83 | 507 | Procedure | `Procedure.code.coding` | 409063005.0 | Counselling | http://snomed.info/sct |
| 84 | 509 | Procedure | `Procedure.code.coding` | ED000008 | Edukasi Tanda Bahaya Kehamilan, Bersalin dan Nifas | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 85 | 510 | Procedure | `Procedure.code.coding` | SP000121 | Edukasi Tanda Bahaya Baru Lahir | http://terminology.kemkes.go.id/sp |
| 86 | 511 | Procedure | `Procedure.code.coding` | ED000009 | Edukasi IMD dan ASI Eksklusif | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 87 | 512 | Procedure | `Procedure.code.coding` | ED000005 | Edukasi Gizi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 88 | 513 | Procedure | `Procedure.code.coding` | PC000001 | Perawatan Tali Pusat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 89 | 514 | Procedure | `Procedure.code.coding` | ED000010 | Edukasi PHBS | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 90 | 523 | Observation | `Observation.code.coding` | 365662002.0 | Finding of amniotic fluid appearance | http://snomed.info/sct |
| 91 | 524 | Observation | `Observation.valueCodeableConcept.coding` | 168090003.0 | Amniotic fluid clear | http://snomed.info/sct |
| 92 | 525 | Observation | `Observation.valueCodeableConcept.coding` | 408781009.0 | Straw colored amniotic fluid | http://snomed.info/sct |
| 93 | 526 | Observation | `Observation.valueCodeableConcept.coding` | 249134008.0 | Bloodstained liquor | http://snomed.info/sct |
| 94 | 527 | Observation | `Observation.valueCodeableConcept.coding` | 168092006.0 | Amniotic fluid -meconium stain | http://snomed.info/sct |
| 95 | 542 | ServiceRequest | `ServiceRequest.code.coding` | 409014006.0 | Delivery care management | http://snomed.info/sct |
| 96 | 551 | ServiceRequest | `ServiceRequest.locationCode.coding` | SP000129 | Puskesmas PONED | http://terminology.kemkes.go.id/sp |
| 97 | 555 | ServiceRequest | `ServiceRequest.locationCode.coding` | SP000128 | Rumah Sakit Ibu dan Anak | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 62 |
| http://loinc.org | 17 |
| http://terminology.kemkes.go.id/sp | 9 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 5 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 2 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 1 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 1 |
| **Total** | **97** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 40 | – | Faskes yang Melayani INC | Organization | `Organization.name` |
| 536 | – | Rujuk | – | `` |
