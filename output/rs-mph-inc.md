# Output Form: SIM RS MPH INC

Sumber: `mapping/phdt-data-dictionary-rs-mph-inc.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-rs-mph-inc.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 40 |
| Code (`jumlah code` = 1) | 94 |
| Code unik (code + CodeSystem) | 87 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 8 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–27 | Patient | – | – | _Nama Ibu_ → `Patient.name.text` (2, tanpa BQ)<br>_NIK_ → `Patient.identifier.value` (6, tanpa BQ)<br>_No HP_ → `Patient.telecom` (7, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (10, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (11, tanpa BQ)<br>_Alamat Domisili_ → `Patient.address.line` (13, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (18, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (21, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.extension.valueCode` (24, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.extension.valueCode` (27, tanpa BQ) |
| 2 | 28–35 | RelatedPerson | – | – | _Nama Suami/ Pendamping_ → `RelatedPerson.patient.reference` (28, tanpa BQ)<br>_NIK Suami/ Pendamping_ → `RelatedPerson.identifier` (32, tanpa BQ) |
| 3 | 74–78 | Practitioner | – | – | _NIK_ → `Practitioner.identifier.value` (76, tanpa BQ)<br>_Nama Tenaga Kesehatan_ → `Practitioner.name.text` (78, tanpa BQ) |
| 4 | 79–88 | PractitionerRole | – | – | _Tenaga Pemeriksa_ → `PractitionerRole.code.coding` (83, tanpa BQ) |
| 5 | 89–93 | Practitioner | – | – | _NIK Pencatat_ → `Practitioner.identifier.value` (91, tanpa BQ)<br>_Nama Pencatat_ → `Practitioner.name.text` (93, tanpa BQ) |
| 6 | 94–102 | PractitionerRole | – | – | _Role Pencatat_ → `PractitionerRole.code.coding` (98, tanpa BQ) |
| 7 | 104–118 | Encounter | – | – | _Tanggal Masuk_ → `Encounter.period.start` (113, tanpa BQ)<br>_Tanggal Keluar INC_ → `Encounter.period.end` (114, tanpa BQ)<br>_Tempat Melahirkan_ → `Encounter.location.location.display` (116, tanpa BQ) |
| 8 | 119–126 | Condition | 386337006.0 | Intrapartal care | – |
| 9 | 137–150 | EpisodeOfCare | ANC | Antenatal Care | – |
| 10 | 151–159 | EpisodeOfCare | PNC | Postnatal Care | – |
| 11 | 160–171 | Observation | SP000383 | Keadaan Ibu Saat Tiba | _Keadaan Ibu Saat Tiba_ → `Observation.valueCodeableConcept.coding` (163, tanpa BQ) |
| 12 | 172–183 | Observation | 246435002.0 | Number of fetuses | _Jumlah Janin_ → `Observation.valueInteger` (176, tanpa BQ) |
| 13 | 184–194 | Observation | 81956-5 | Date and time of death [TimeStamp] | _Waktu Kematian_ → `Observation.valueDateTime` (187, tanpa BQ) |
| 14 | 195–205 | Observation | 79378-6 | Cause of death | _Diagnosa Penyebab Kematian_ → `Observation.valueString` (198, tanpa BQ) |
| 15 | 206–217 | Observation | 8480-6 | Systolic blood pressure | _Tekanan Darah Sistolik_ → `Observation.valueQuantity.value` (209, tanpa BQ) |
| 16 | 218–229 | Observation | 8462-4 | Diastolic blood pressure | _Tekanan Darah Diastolik_ → `Observation.valueQuantity.value` (221, tanpa BQ) |
| 17 | 230–242 | Observation | 8867-4 | Heart rate | _Frekuensi Nadi_ → `Observation.valueQuantity.value` (233, tanpa BQ) |
| 18 | 243–255 | Observation | 9279-1 | Respiratory rate | _Pernapasan_ → `Observation.valueQuantity.value` (246, tanpa BQ) |
| 19 | 256–268 | Observation | – | – | _Suhu Badan_ → `Observation.valueQuantity.value` (259, tanpa BQ) |
| 20 | 269–283 | Observation | 11881-0 | Uterus Fundal height Tape measure | _Tinggi Fundus Uteri_ → `Observation.valueQuantity.value` (272, tanpa BQ)<br>_Detak Jantung Janin_ → `Observation.identifier.value` (283, tanpa BQ) |
| 21 | 284–296 | Observation | 55283-6 | Fetal Heart rate | _Letak Janin_ → `Observation.identifier.value` (296, tanpa BQ) |
| 22 | 297–309 | Observation | 271692001.0 | Presentation of fetus | _Presentasi Janin_ → `Observation.identifier.value` (309, tanpa BQ) |
| 23 | 310–330 | Observation | 72155-5 | Position in womb Fetus [RHEA] | _Posisi Kepala Janin terhadap PAP (Pintu Atas Panggul)_ → `Observation.identifier.value` (330, tanpa BQ) |
| 24 | 331–344 | Observation | 249111004.0 | Engagement of head | _Kondisi Ketuban_ → `Observation.identifier.value` (344, tanpa BQ) |
| 25 | 345–357 | Observation | 289282009.0 | Amniotic membrane finding | _Faktor risiko INC_ → `Observation.status` (357, tanpa BQ) |
| 26 | 358–368 | Observation | SP000015 | Risiko Masalah Kesehatan | – |
| 27 | 369–383 | Observation | 76516-4 | Gestational age—​at birth | _Usia Kehamilan Saat Gestasi (minggu)_ → `Observation.valueQuantity.value` (371, tanpa BQ)<br>_Usia Kehamilan Saat Gestasi (hari)_ → `Observation.component.valueQuantity.value` (374, tanpa BQ)<br>_Tanggal dan Jam Persalinan_ → `Observation.status` (383, tanpa BQ) |
| 28 | 384–395 | Observation | 93857-1 | Date and time of obstetric delivery | _Penolong Persalinan_ → `Observation.status` (395, tanpa BQ) |
| 29 | 396–406 | Observation | OC000013 | Penolong Persalinan | _Cara Persalinan_ → `Observation.status` (406, tanpa BQ) |
| 30 | 407–421 | Observation | 57071-3 | Obstetric delivery method | – |
| 31 | 422–439 | Observation | 405195003.0 | Intrapartum maternal status | _Keadaan Ibu_ → `Observation.valueCodeableConcept.coding` (424, tanpa BQ) |
| 32 | 440–448 | Condition | 199745000.0 | Complication occurring during labor and delivery | _Komplikasi Persalinan_ → `Condition.clinicalStatus.coding` (440, tanpa BQ) |
| 33 | 449–459 | Observation | SP000379 | Tatalaksana Komplikasi Persalinan | _Tatalaksana Komplikasi Persalinan_ → `Observation.valueString` (452, tanpa BQ) |
| 34 | 460–473 | Observation | 63893-2 | Outcome of pregnancy | _Luaran Kehamilan_ → `Observation.valueCodeableConcept.coding` (463, tanpa BQ) |
| 35 | 474–484 | Procedure | SP000130 | Menggunakan Partograf | _Pelayanan Menggunakan Partograf_ → `Procedure.category.coding` (474, tanpa BQ) |
| 36 | 485–495 | Procedure | 431868002.0 | Initiation of breastfeeding | _Inisiasi Menyusu Dini (IMD)_ → `Procedure.category.coding` (485, tanpa BQ) |
| 37 | 496–498 | Procedure | 409063005.0 | Counselling | _Konseling_ → `Procedure.category.coding` (496, tanpa BQ) |
| 38 | 499–514 | Procedure | 409063005.0 | Counselling | – |
| 39 | 515–528 | Observation | 365662002.0 | Finding of amniotic fluid appearance | _Warna Ketuban_ → `Observation.valueCodeableConcept.coding` (517, tanpa BQ) |
| 40 | 531–552 | ServiceRequest | 409014006.0 | Delivery care management | _Faskes Rujukan_ → `ServiceRequest.locationCode.coding` (544, tanpa BQ)<br>_Nama Faskes Rujukan_ → `ServiceRequest.locationCode.text` (552, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 24 |
| Procedure | 4 |
| Practitioner | 2 |
| PractitionerRole | 2 |
| Condition | 2 |
| EpisodeOfCare | 2 |
| Patient | 1 |
| RelatedPerson | 1 |
| Encounter | 1 |
| ServiceRequest | 1 |
| **Total** | **40** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 83 | PractitionerRole | `PractitionerRole.code.coding` | 309453006.0 | Registered midwife | http://snomed.info/sct |
| 2 | 84 | PractitionerRole | `PractitionerRole.code.coding` | 309367003.0 | Obstetrician and gynecologist | http://snomed.info/sct |
| 3 | 85 | PractitionerRole | `PractitionerRole.code.coding` | 309343006.0 | Physician | http://snomed.info/sct |
| 4 | 86 | PractitionerRole | `PractitionerRole.code.coding` | 224535009.0 | Registered nurse | http://snomed.info/sct |
| 5 | 87 | PractitionerRole | `PractitionerRole.code.coding` | 224535009.0 | Registered nurse | http://snomed.info/sct |
| 6 | 98 | PractitionerRole | `PractitionerRole.code.coding` | 309453006.0 | Registered midwife | http://snomed.info/sct |
| 7 | 99 | PractitionerRole | `PractitionerRole.code.coding` | 309367003.0 | Obstetrician and gynecologist | http://snomed.info/sct |
| 8 | 100 | PractitionerRole | `PractitionerRole.code.coding` | 309343006.0 | Physician | http://snomed.info/sct |
| 9 | 101 | PractitionerRole | `PractitionerRole.code.coding` | 224535009.0 | Registered nurse | http://snomed.info/sct |
| 10 | 102 | PractitionerRole | `PractitionerRole.code.coding` | 56542007.0 | Medical record administrator | http://snomed.info/sct |
| 11 | 121 | Condition | `Condition.code.coding` | 386337006.0 | Intrapartal care | http://snomed.info/sct |
| 12 | 138 | EpisodeOfCare | `EpisodeOfCare.type.coding` | ANC | Antenatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 13 | 152 | EpisodeOfCare | `EpisodeOfCare.type.coding` | PNC | Postnatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 14 | 162 | Observation | `Observation.code.coding` | SP000383 | Keadaan Ibu Saat Tiba | http://terminology.kemkes.go.id/sp |
| 15 | 163 | Observation | `Observation.valueCodeableConcept.coding` | 438949009.0 | Alive | http://snomed.info/sct |
| 16 | 164 | Observation | `Observation.valueCodeableConcept.coding` | 419099009.0 | Dead | http://snomed.info/sct |
| 17 | 174 | Observation | `Observation.code.coding` | 246435002.0 | Number of fetuses | http://snomed.info/sct |
| 18 | 175 | Observation | `Observation.code.coding` | ANC.B8.DE109 | Number of fetuses | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 19 | 186 | Observation | `Observation.code.coding` | 81956-5 | Date and time of death [TimeStamp] | http://loinc.org |
| 20 | 197 | Observation | `Observation.code.coding` | 79378-6 | Cause of death | http://loinc.org |
| 21 | 208 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 22 | 220 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://loinc.org |
| 23 | 232 | Observation | `Observation.code.coding` | 8867-4 | Heart rate | http://loinc.org |
| 24 | 245 | Observation | `Observation.code.coding` | 9279-1 | Respiratory rate | http://loinc.org |
| 25 | 271 | Observation | `Observation.code.coding` | 11881-0 | Uterus Fundal height Tape measure | http://loinc.org |
| 26 | 285 | Observation | `Observation.code.coding` | 55283-6 | Fetal Heart rate | http://loinc.org |
| 27 | 298 | Observation | `Observation.code.coding` | 271692001.0 | Presentation of fetus | http://snomed.info/sct |
| 28 | 299 | Observation | `Observation.valueCodeableConcept.coding` | 398236008.0 | Intrauterine | http://snomed.info/sct |
| 29 | 300 | Observation | `Observation.valueCodeableConcept.coding` | 298109001.0 | Ectopic | http://snomed.info/sct |
| 30 | 311 | Observation | `Observation.code.coding` | 72155-5 | Position in womb Fetus [RHEA] | http://loinc.org |
| 31 | 312 | Observation | `Observation.valueCodeableConcept.coding` | 1209182005.0 | Cephalic fetal presentation | http://snomed.info/sct |
| 32 | 313 | Observation | `Observation.valueCodeableConcept.coding` | 70028003.0 | Vertex presentation | http://snomed.info/sct |
| 33 | 314 | Observation | `Observation.valueCodeableConcept.coding` | 249083005.0 | Posterior fontanelle presenting | http://snomed.info/sct |
| 34 | 315 | Observation | `Observation.valueCodeableConcept.coding` | 288203005.0 | Transverse/oblique lie | http://snomed.info/sct |
| 35 | 316 | Observation | `Observation.valueCodeableConcept.coding` | 23954006.0 | Acromion presentation | http://snomed.info/sct |
| 36 | 317 | Observation | `Observation.valueCodeableConcept.coding` | 6096002.0 | Breech presentation | http://snomed.info/sct |
| 37 | 318 | Observation | `Observation.valueCodeableConcept.coding` | 8014007.0 | Brow presentation of fetus | http://snomed.info/sct |
| 38 | 319 | Observation | `Observation.valueCodeableConcept.coding` | 8017000.0 | Face presentation | http://snomed.info/sct |
| 39 | 320 | Observation | `Observation.valueCodeableConcept.coding` | 249097002.0 | Footling breech presentation | http://snomed.info/sct |
| 40 | 321 | Observation | `Observation.valueCodeableConcept.coding` | 124736009.0 | Compound presentation | http://snomed.info/sct |
| 41 | 332 | Observation | `Observation.code.coding` | 249111004.0 | Engagement of head | http://snomed.info/sct |
| 42 | 333 | Observation | `Observation.valueCodeableConcept.coding` | 249112006.0 | Head engaged | http://snomed.info/sct |
| 43 | 334 | Observation | `Observation.valueCodeableConcept.coding` | 62098001.0 | Head not engaged | http://snomed.info/sct |
| 44 | 335 | Observation | `Observation.dataAbsentReason` | unknown | Unknown | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 45 | 346 | Observation | `Observation.code.coding` | 289282009.0 | Amniotic membrane finding | http://snomed.info/sct |
| 46 | 347 | Observation | `Observation.valueCodeableConcept.coding` | 249125003.0 | Intact membranes | http://snomed.info/sct |
| 47 | 348 | Observation | `Observation.valueCodeableConcept.coding` | SP000120 | Non-intact membrane | http://snomed.info/sct |
| 48 | 359 | Observation | `Observation.code.coding` | SP000015 | Risiko Masalah Kesehatan | http://terminology.kemkes.go.id/sp |
| 49 | 370 | Observation | `Observation.code.coding` | 76516-4 | Gestational age—​at birth | http://loinc.org |
| 50 | 373 | Observation | `Observation.component.code.coding` | SP000398 | Usia Kehamilan Saat Persalinan (hari) | http://terminology.kemkes.go.id/sp |
| 51 | 385 | Observation | `Observation.code.coding` | 93857-1 | Date and time of obstetric delivery | http://loinc.org |
| 52 | 397 | Observation | `Observation.code.coding` | OC000013 | Penolong Persalinan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 53 | 398 | Observation | `Observation.valueCodeableConcept.coding` | 11935004.0 | Obstetrician | http://snomed.info/sct |
| 54 | 408 | Observation | `Observation.code.coding` | 57071-3 | Obstetric delivery method | http://loinc.org |
| 55 | 409 | Observation | `Observation.valueCodeableConcept.coding` | 48782003.0 | Delivery normal | http://snomed.info/sct |
| 56 | 410 | Observation | `Observation.valueCodeableConcept.coding` | 200138003.0 | Vacuum extractor delivery - delivered | http://snomed.info/sct |
| 57 | 411 | Observation | `Observation.valueCodeableConcept.coding` | 200130005.0 | Forceps delivery - delivered | http://snomed.info/sct |
| 58 | 412 | Observation | `Observation.valueCodeableConcept.coding` | 200144004.0 | Deliveries by cesarean | http://snomed.info/sct |
| 59 | 413 | Observation | `Observation.valueCodeableConcept.coding` | 289259007.0 | Vaginal delivery | http://snomed.info/sct |
| 60 | 423 | Observation | `Observation.code.coding` | 405195003.0 | Intrapartum maternal status | http://snomed.info/sct |
| 61 | 424 | Observation | `Observation.valueCodeableConcept.coding` | 438949009.0 | Alive | http://snomed.info/sct |
| 62 | 425 | Observation | `Observation.valueCodeableConcept.coding` | 102514002.0 | Well female adult | http://snomed.info/sct |
| 63 | 426 | Observation | `Observation.valueCodeableConcept.coding` | 39104002.0 | Illness | http://snomed.info/sct |
| 64 | 427 | Observation | `Observation.valueCodeableConcept.coding` | 131148009.0 | Bleeding | http://snomed.info/sct |
| 65 | 428 | Observation | `Observation.valueCodeableConcept.coding` | 386661006.0 | Fever | http://snomed.info/sct |
| 66 | 429 | Observation | `Observation.valueCodeableConcept.coding` | 91175000.0 | Seizure | http://snomed.info/sct |
| 67 | 430 | Observation | `Observation.valueCodeableConcept.coding` | 249215002.0 | Odor of lochia | http://snomed.info/sct |
| 68 | 431 | Observation | `Observation.valueCodeableConcept.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 69 | 432 | Observation | `Observation.valueCodeableConcept.coding` | 59283008.0 | Maternal death | http://snomed.info/sct |
| 70 | 442 | Condition | `Condition.code.coding` | 199745000.0 | Complication occurring during labor and delivery | http://snomed.info/sct |
| 71 | 451 | Observation | `Observation.code.coding` | SP000379 | Tatalaksana Komplikasi Persalinan | http://terminology.kemkes.go.id/sp |
| 72 | 462 | Observation | `Observation.code.coding` | 63893-2 | Outcome of pregnancy | http://loinc.org |
| 73 | 463 | Observation | `Observation.valueCodeableConcept.coding` | LA14270-5 | Live birth | http://loinc.org |
| 74 | 464 | Observation | `Observation.valueCodeableConcept.coding` | LA14271-3 | Stillborn | http://loinc.org |
| 75 | 465 | Observation | `Observation.valueCodeableConcept.coding` | LA14272-1 | Miscarriage | http://loinc.org |
| 76 | 466 | Observation | `Observation.valueCodeableConcept.coding` | LA14273-9 | Induced abortion | http://loinc.org |
| 77 | 477 | Procedure | `Procedure.code.coding` | SP000130 | Menggunakan Partograf | http://terminology.kemkes.go.id/sp |
| 78 | 488 | Procedure | `Procedure.code.coding` | 431868002.0 | Initiation of breastfeeding | http://snomed.info/sct |
| 79 | 498 | Procedure | `Procedure.code.coding` | 409063005.0 | Counselling | http://snomed.info/sct |
| 80 | 500 | Procedure | `Procedure.code.coding` | 409063005.0 | Counselling | http://snomed.info/sct |
| 81 | 502 | Procedure | `Procedure.code.coding` | ED000008 | Edukasi Tanda Bahaya Kehamilan, Bersalin dan Nifas | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 82 | 503 | Procedure | `Procedure.code.coding` | SP000121 | Edukasi Tanda Bahaya Baru Lahir | http://terminology.kemkes.go.id/sp |
| 83 | 504 | Procedure | `Procedure.code.coding` | ED000009 | Edukasi IMD dan ASI Eksklusif | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 84 | 505 | Procedure | `Procedure.code.coding` | ED000005 | Edukasi Gizi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 85 | 506 | Procedure | `Procedure.code.coding` | PC000001 | Perawatan Tali Pusat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 86 | 507 | Procedure | `Procedure.code.coding` | ED000010 | Edukasi PHBS | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 87 | 516 | Observation | `Observation.code.coding` | 365662002.0 | Finding of amniotic fluid appearance | http://snomed.info/sct |
| 88 | 517 | Observation | `Observation.valueCodeableConcept.coding` | 168090003.0 | Amniotic fluid clear | http://snomed.info/sct |
| 89 | 518 | Observation | `Observation.valueCodeableConcept.coding` | 408781009.0 | Straw colored amniotic fluid | http://snomed.info/sct |
| 90 | 519 | Observation | `Observation.valueCodeableConcept.coding` | 249134008.0 | Bloodstained liquor | http://snomed.info/sct |
| 91 | 520 | Observation | `Observation.valueCodeableConcept.coding` | 168092006.0 | Amniotic fluid -meconium stain | http://snomed.info/sct |
| 92 | 535 | ServiceRequest | `ServiceRequest.code.coding` | 409014006.0 | Delivery care management | http://snomed.info/sct |
| 93 | 544 | ServiceRequest | `ServiceRequest.locationCode.coding` | SP000129 | Puskesmas PONED | http://terminology.kemkes.go.id/sp |
| 94 | 548 | ServiceRequest | `ServiceRequest.locationCode.coding` | SP000128 | Rumah Sakit Ibu dan Anak | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 59 |
| http://loinc.org | 17 |
| http://terminology.kemkes.go.id/sp | 8 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 6 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 2 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 1 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 1 |
| **Total** | **94** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 39 | – | Jenis Faskes | Organization | `Organization.type` |
| 40 | – | Nama Faskes | Organization | `Organization.name` |
| 529 | – | Rujuk | – | `` |
