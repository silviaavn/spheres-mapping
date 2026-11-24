# Output Form: SIM RS Ummu Hani PNC

Sumber: `mapping/phdt-data-dictionary-rs-ummu-hani-pnc.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-rs-ummu-hani-pnc.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 53 |
| Code (`jumlah code` = 1) | 110 |
| Code unik (code + CodeSystem) | 95 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 6 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–27 | Patient | – | – | _Nama Ibu_ → `Patient.name.text` (2, tanpa BQ)<br>_NIK_ → `Patient.identifier.value` (6, tanpa BQ)<br>_No HP_ → `Patient.telecom` (7, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (10, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (11, tanpa BQ)<br>_Alamat Domisili_ → `Patient.address.line` (13, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (18, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (21, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.extension.valueCode` (24, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.extension.valueCode` (27, tanpa BQ) |
| 2 | 28–35 | RelatedPerson | – | – | _Nama Suami/ Pendamping_ → `RelatedPerson.patient.reference` (28, tanpa BQ)<br>_NIK Suami/ Pendamping_ → `RelatedPerson.identifier` (32, tanpa BQ) |
| 3 | 71–75 | Practitioner | – | – | _NIK_ → `Practitioner.identifier.value` (73, tanpa BQ)<br>_Nama Tenaga Kesehatan_ → `Practitioner.name.text` (75, tanpa BQ) |
| 4 | 76–85 | PractitionerRole | – | – | _Tenaga Pemeriksa_ → `PractitionerRole.code.coding` (80, tanpa BQ) |
| 5 | 86–90 | Practitioner | – | – | _NIK Pencatat_ → `Practitioner.identifier.value` (88, tanpa BQ)<br>_Nama Pencatat_ → `Practitioner.name.text` (90, tanpa BQ) |
| 6 | 91–99 | PractitionerRole | – | – | _Role Pencatat_ → `PractitionerRole.code.coding` (95, tanpa BQ) |
| 7 | 100–115 | Encounter | – | – | _Kunjungan Nifas (KF)_ → `Encounter.identifier` (100, tanpa BQ)<br>_Tanggal Masuk PNC_ → `Encounter.period.start` (110, tanpa BQ)<br>_Cara Masuk_ → `Encounter.hospitalization.admitSource.coding` (145, tanpa BQ) |
| 8 | 116–123 | Condition | 386337006.0 | Intrapartal care | – |
| 9 | 126–134 | Condition | 404684003.0 | Clinical finding | _Keluhan_ → `Condition.clinicalStatus.coding` (126, tanpa BQ) |
| 10 | 147–155 | EpisodeOfCare | PNC | Postnatal Care | – |
| 11 | 156–167 | Observation | 11996-6 | [#] Pregnancies | _Gravida_ → `Observation.valueInteger` (160, tanpa BQ) |
| 12 | 168–179 | Observation | 11977-6 | [#] Parity | _Partus_ → `Observation.valueInteger` (172, tanpa BQ) |
| 13 | 180–191 | Observation | 69043-8 | Other pregnancy outcomes # | _Abortus_ → `Observation.valueInteger` (184, tanpa BQ) |
| 14 | 192–203 | Observation | 8480-6 | Systolic blood pressure | _Tekanan Darah Sistolik_ → `Observation.valueQuantity.value` (195, tanpa BQ) |
| 15 | 204–215 | Observation | 8462-4 | Diastolic blood pressure | _Tekanan Darah Diastolik_ → `Observation.valueQuantity.value` (207, tanpa BQ) |
| 16 | 216–228 | Observation | 8867-4 | Heart rate | _Frekuensi Nadi_ → `Observation.valueQuantity.value` (219, tanpa BQ) |
| 17 | 229–241 | Observation | 9279-1 | Respiratory rate | _Pernapasan_ → `Observation.valueQuantity.value` (232, tanpa BQ) |
| 18 | 242–254 | Observation | – | – | _Suhu_ → `Observation.valueQuantity.value` (245, tanpa BQ) |
| 19 | 256–262 | Condition | 289530006.0 | Vaginal bleeding | _Pendarahan Pervaginam_ → `Condition.clinicalStatus.coding` (256, tanpa BQ) |
| 20 | 263–277 | Observation | 364297003.0 | Female perineum observable | _Kondisi Perineum_ → `Observation.valueCodeableConcept.coding` (266, tanpa BQ) |
| 21 | 278–289 | Observation | OC000020 | Tanda Infeksi Perineum | _Tanda Infeksi Perineum_ → `Observation.valueBoolean` (281, tanpa BQ) |
| 22 | 290–301 | Observation | OC000025 | Tanda Infeksi Luka Jahitan Sectio Caesaria | _Tanda Infeksi Luka Jahitan Sectio Caesaria_ → `Observation.valueBoolean` (293, tanpa BQ) |
| 23 | 302–316 | Observation | 32422-8 | Physical findings of breast | _Kondisi Payudara_ → `Observation.valueCodeableConcept.coding` (305, tanpa BQ) |
| 24 | 317–328 | Observation | 289700000.0 | Uterine contractions present | _Kontraksi Uteri_ → `Observation.valueBoolean` (320, tanpa BQ) |
| 25 | 329–342 | Observation | 249214003.0 | Color of lochia | _Warna Lokhia_ → `Observation.valueCodeableConcept.coding` (332, tanpa BQ) |
| 26 | 343–354 | Observation | 249215002.0 | Odor of lochia | _Bau Lokhia_ → `Observation.valueBoolean` (346, tanpa BQ) |
| 27 | 355–370 | Observation | 252041008.0 | Micturition finding | _Gangguan Buang Air Kecil_ → `Observation.valueCodeableConcept.coding` (358, tanpa BQ) |
| 28 | 371–382 | Observation | 300375001.0 | Able to defecate | _Gangguan Buang Air Besar_ → `Observation.valueBoolean` (374, tanpa BQ) |
| 29 | 383–393 | Procedure | 408988007.0 | Newborn care education | _Konseling Perawatan Bayi Baru Lahir_ → `Procedure.category.coding` (383, tanpa BQ) |
| 30 | 394–405 | Observation | 8345-1 | Body weight Measured --post partum | _Berat Badan_ → `Observation.valueQuantity.value` (397, tanpa BQ) |
| 31 | 406–417 | Observation | 8305-5 | Body height --post partum | _Tinggi Badan_ → `Observation.valueQuantity.value` (409, tanpa BQ) |
| 32 | 418–431 | Observation | 284473002.0 | Mid upper arm circumference | _LILA_ → `Observation.valueQuantity.value` (421, tanpa BQ)<br>_Status Gizi KEK/Tidak KEK_ → `Observation.interpretation` (430, tanpa BQ) |
| 33 | 432–444 | Observation | 11881-0 | Uterus Fundal height Tape measure | _TFU_ → `Observation.valueString` (435, tanpa BQ) |
| 34 | 445–455 | Procedure | 409019001.0 | Postpartum care management | _Tatalaksana PNC_ → `Procedure.category.coding` (445, tanpa BQ) |
| 35 | 456–473 | Condition | 47821001.0 | Postpartum hemorrhage | _Komplikasi Masa Nifas_ → `Condition.clinicalStatus.coding` (456, tanpa BQ) |
| 36 | 474–486 | Observation | 289084000.0 | Difficulty performing breastfeeding | _Apakah ada masalah memberikan ASI_ → `Observation.valueBoolean` (477, tanpa BQ)<br>_Catatan ASI_ → `Observation.note.text` (486, tanpa BQ) |
| 37 | 487–500 | Observation | OC000017 | Produksi ASI | _Produksi ASI_ → `Observation.valueCodeableConcept.coding` (490, tanpa BQ)<br>_Catat dibuku KIA_ → `Observation.catgeory.coding` (500, tanpa BQ) |
| 38 | 501–513 | Observation | SP000122 | Catat di Buku KIA | _Metode Kontrasepsi KB Pasca Plasenta_ → `Observation.status` (512, tanpa BQ) |
| 39 | 514–531 | Observation | SP000139 | KB Pasca Plasenta | _Metode Kontrasepsi KB Pasca Persalinan_ → `Observation.status` (530, tanpa BQ) |
| 40 | 532–547 | Observation | PC000004 | KB Pasca Persalinan | – |
| 41 | 548–549 | MedicationDispense | – | – | _Diberikan Tablet FE_ → `MedicationDispense.status` (548, tanpa BQ) |
| 42 | 550–564 | Medication | – | – | – |
| 43 | 565–570 | MedicationRequest | – | – | – |
| 44 | 571–585 | Medication | – | – | – |
| 45 | 586–591 | MedicationDispense | – | – | – |
| 46 | 592–625 | MedicationRequest | 92000653.0 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula | _Jumlah Tablet Fe yang didapatkan (butir)_ → `MedicationRequest.contained.resourceType` (592, tanpa BQ) |
| 47 | 626–657 | MedicationDispense | 93015491.0 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | – |
| 48 | 658–668 | Procedure | 711029005.0 | Counseling about breastfeeding | _Konseling ASI_ → `Procedure.category.coding` (658, tanpa BQ) |
| 49 | 669–679 | Procedure | 72531000052105.0 | Counseling for contraception | _Konseling KB_ → `Procedure.category.coding` (669, tanpa BQ) |
| 50 | 680–690 | Procedure | 441041000124100.0 | Counseling about nutrition | _Konseling Gizi_ → `Procedure.category.coding` (680, tanpa BQ) |
| 51 | 691–701 | Observation | SP000138 | Tatalaksana Komplikasi Pre Eklampsia | _Tatalaksana Komplikasi Pre Eklampsia dan Eklampsia_ → `Observation.valueString` (694, tanpa BQ) |
| 52 | 703–714 | Observation | SP000389 | Keadaan Ibu | – |
| 53 | 716–736 | ServiceRequest | 409014006.0 | Delivery care management | _Faskes Rujukan_ → `ServiceRequest.locationCode.coding` (729, tanpa BQ)<br>_Nama Faskes Rujukan_ → `ServiceRequest.locationCode.text` (736, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 28 |
| Procedure | 5 |
| Condition | 4 |
| MedicationDispense | 3 |
| Practitioner | 2 |
| PractitionerRole | 2 |
| Medication | 2 |
| MedicationRequest | 2 |
| Patient | 1 |
| RelatedPerson | 1 |
| Encounter | 1 |
| EpisodeOfCare | 1 |
| ServiceRequest | 1 |
| **Total** | **53** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 80 | PractitionerRole | `PractitionerRole.code.coding` | 309453006.0 | Registered midwife | http://snomed.info/sct |
| 2 | 81 | PractitionerRole | `PractitionerRole.code.coding` | 309367003.0 | Obstetrician and gynecologist | http://snomed.info/sct |
| 3 | 82 | PractitionerRole | `PractitionerRole.code.coding` | 309343006.0 | Physician | http://snomed.info/sct |
| 4 | 83 | PractitionerRole | `PractitionerRole.code.coding` | 224535009.0 | Registered nurse | http://snomed.info/sct |
| 5 | 84 | PractitionerRole | `PractitionerRole.code.coding` | 224535009.0 | Registered nurse | http://snomed.info/sct |
| 6 | 95 | PractitionerRole | `PractitionerRole.code.coding` | 309453006.0 | Registered midwife | http://snomed.info/sct |
| 7 | 96 | PractitionerRole | `PractitionerRole.code.coding` | 309367003.0 | Obstetrician and gynecologist | http://snomed.info/sct |
| 8 | 97 | PractitionerRole | `PractitionerRole.code.coding` | 309343006.0 | Physician | http://snomed.info/sct |
| 9 | 98 | PractitionerRole | `PractitionerRole.code.coding` | 224535009.0 | Registered nurse | http://snomed.info/sct |
| 10 | 99 | PractitionerRole | `PractitionerRole.code.coding` | 56542007.0 | Medical record administrator | http://snomed.info/sct |
| 11 | 118 | Condition | `Condition.code.coding` | 386337006.0 | Intrapartal care | http://snomed.info/sct |
| 12 | 128 | Condition | `Condition.code.coding` | 404684003.0 | Clinical finding | http://snomed.info/sct |
| 13 | 145 | Encounter | `Encounter.hospitalization.admitSource.coding` | EHA000002 | Datang sendiri | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 14 | 146 | Encounter | `Encounter.hospitalization.admitSource.coding` | 3457005.0 | Patient referral | http://snomed.info/sct |
| 15 | 148 | EpisodeOfCare | `EpisodeOfCare.type.coding` | PNC | Postnatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 16 | 158 | Observation | `Observation.code.coding` | 11996-6 | [#] Pregnancies | http://loinc.org |
| 17 | 159 | Observation | `Observation.code.coding` | ANC.B6.DE24 | Number of pregnancies (gravida) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 18 | 170 | Observation | `Observation.code.coding` | 11977-6 | [#] Parity | http://loinc.org |
| 19 | 171 | Observation | `Observation.code.coding` | ANC.B6.DE32 | Parity | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 20 | 182 | Observation | `Observation.code.coding` | 69043-8 | Other pregnancy outcomes # | http://loinc.org |
| 21 | 183 | Observation | `Observation.code.coding` | ANC.B6.DE25 | Number of miscarriages and/or abortions | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 22 | 194 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 23 | 206 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://loinc.org |
| 24 | 218 | Observation | `Observation.code.coding` | 8867-4 | Heart rate | http://loinc.org |
| 25 | 231 | Observation | `Observation.code.coding` | 9279-1 | Respiratory rate | http://loinc.org |
| 26 | 258 | Condition | `Condition.code.coding` | 289530006.0 | Vaginal bleeding | http://snomed.info/sct |
| 27 | 265 | Observation | `Observation.code.coding` | 364297003.0 | Female perineum observable | http://loinc.org |
| 28 | 266 | Observation | `Observation.valueCodeableConcept.coding` | 289854007.0 | Perineum intact | http://snomed.info/sct |
| 29 | 267 | Observation | `Observation.valueCodeableConcept.coding` | 57759005.0 | First degree perineal laceration | http://snomed.info/sct |
| 30 | 268 | Observation | `Observation.valueCodeableConcept.coding` | 6234006.0 | Second degree perineal laceration | http://snomed.info/sct |
| 31 | 269 | Observation | `Observation.valueCodeableConcept.coding` | 10217006.0 | Third degree perineal laceration | http://snomed.info/sct |
| 32 | 270 | Observation | `Observation.valueCodeableConcept.coding` | 399031001.0 | Fourth degree perineal laceration | http://snomed.info/sct |
| 33 | 280 | Observation | `Observation.code.coding` | OC000020 | Tanda Infeksi Perineum | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 34 | 292 | Observation | `Observation.code.coding` | OC000025 | Tanda Infeksi Luka Jahitan Sectio Caesaria | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 35 | 304 | Observation | `Observation.code.coding` | 32422-8 | Physical findings of breast | http://loinc.org |
| 36 | 305 | Observation | `Observation.valueCodeableConcept.coding` | 300885006.0 | Swelling of breast | http://snomed.info/sct |
| 37 | 306 | Observation | `Observation.valueCodeableConcept.coding` | 290070001.0 | Red breast | http://snomed.info/sct |
| 38 | 307 | Observation | `Observation.valueCodeableConcept.coding` | 54302000.0 | Discharge from nipple | http://snomed.info/sct |
| 39 | 308 | Observation | `Observation.valueCodeableConcept.coding` | 53430007.0 | Pain of breast | http://snomed.info/sct |
| 40 | 309 | Observation | `Observation.valueCodeableConcept.coding` | 290084006.0 | Breast normal | http://snomed.info/sct |
| 41 | 319 | Observation | `Observation.code.coding` | 289700000.0 | Uterine contractions present | http://snomed.info/sct |
| 42 | 331 | Observation | `Observation.code.coding` | 249214003.0 | Color of lochia | http://snomed.info/sct |
| 43 | 332 | Observation | `Observation.valueCodeableConcept.coding` | 278072004.0 | Lochia rubra | http://snomed.info/sct |
| 44 | 333 | Observation | `Observation.valueCodeableConcept.coding` | 449828001.0 | Lochia serosa | http://snomed.info/sct |
| 45 | 334 | Observation | `Observation.valueCodeableConcept.coding` | 113291006.0 | Lochia sanguinolenta | http://snomed.info/sct |
| 46 | 335 | Observation | `Observation.valueCodeableConcept.coding` | 449827006.0 | Lochia alba | http://snomed.info/sct |
| 47 | 345 | Observation | `Observation.code.coding` | 249215002.0 | Odor of lochia | http://snomed.info/sct |
| 48 | 357 | Observation | `Observation.code.coding` | 252041008.0 | Micturition finding | http://snomed.info/sct |
| 49 | 358 | Observation | `Observation.valueCodeableConcept.coding` | 49650001.0 | Dysuria | http://snomed.info/sct |
| 50 | 359 | Observation | `Observation.valueCodeableConcept.coding` | 249288007.0 | Incomplete emptying of urinary bladder | http://snomed.info/sct |
| 51 | 360 | Observation | `Observation.valueCodeableConcept.coding` | 162116003.0 | Increased frequency of urination | http://snomed.info/sct |
| 52 | 361 | Observation | `Observation.valueCodeableConcept.coding` | 42112009.0 | Enuresis | http://snomed.info/sct |
| 53 | 362 | Observation | `Observation.valueCodeableConcept.coding` | 102834005.0 | Normal micturition | http://snomed.info/sct |
| 54 | 363 | Observation | `Observation.valueCodeableConcept.coding` | 267064002.0 | Retention of urine | http://snomed.info/sct |
| 55 | 373 | Observation | `Observation.code.coding` | 300375001.0 | Able to defecate | http://snomed.info/sct |
| 56 | 384 | Procedure | `Procedure.code.coding` | 408988007.0 | Newborn care education | http://snomed.info/sct |
| 57 | 396 | Observation | `Observation.code.coding` | 8345-1 | Body weight Measured --post partum | http://loinc.org |
| 58 | 408 | Observation | `Observation.code.coding` | 8305-5 | Body height --post partum | http://loinc.org |
| 59 | 420 | Observation | `Observation.code.coding` | 284473002.0 | Mid upper arm circumference | http://snomed.info/sct |
| 60 | 430 | Observation | `Observation.interpretation` | OI000018 | Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 61 | 431 | Observation | `Observation.interpretation` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 62 | 434 | Observation | `Observation.code.coding` | 11881-0 | Uterus Fundal height Tape measure | http://loinc.org |
| 63 | 446 | Procedure | `Procedure.code.coding` | 409019001.0 | Postpartum care management | http://snomed.info/sct |
| 64 | 458 | Condition | `Condition.code.coding` | 47821001.0 | Postpartum hemorrhage | http://snomed.info/sct |
| 65 | 459 | Condition | `Condition.code.coding` | 198188007.0 | Chronic uterine inflammatory disease | http://snomed.info/sct |
| 66 | 460 | Condition | `Condition.code.coding` | 111367007.0 | Pelvic abscess | http://snomed.info/sct |
| 67 | 461 | Condition | `Condition.code.coding` | 211063003.0 | Infected abrasion of perineum | http://snomed.info/sct |
| 68 | 462 | Condition | `Condition.code.coding` | 76902006.0 | Tetanus | http://snomed.info/sct |
| 69 | 463 | Condition | `Condition.code.coding` | 266579006.0 | Inflammatory disorder of breast | http://snomed.info/sct |
| 70 | 464 | Condition | `Condition.code.coding` | 49746001.0 | Engorgement of breasts | http://snomed.info/sct |
| 71 | 465 | Condition | `Condition.code.coding` | 82231009.0 | Inversion of nipple | http://snomed.info/sct |
| 72 | 466 | Condition | `Condition.code.coding` | 58703003.0 | Postpartum depression | http://snomed.info/sct |
| 73 | 467 | Condition | `Condition.code.coding` | O13 | Gestational [pregnancy-induced] hypertension without signification proteinuria | http://hl7.org/fhir/sid/icd-10 |
| 74 | 468 | Condition | `Condition.code.coding` | O90.8 | Other complications of the puerperium, not elsewhere classified | http://hl7.org/fhir/sid/icd-10 |
| 75 | 476 | Observation | `Observation.code.coding` | 289084000.0 | Difficulty performing breastfeeding | http://snomed.info/sct |
| 76 | 489 | Observation | `Observation.code.coding` | OC000017 | Produksi ASI | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 77 | 490 | Observation | `Observation.valueCodeableConcept.coding` | OV000016 | Produksi ASI ada | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 78 | 491 | Observation | `Observation.valueCodeableConcept.coding` | OV000017 | Produksi ASI ada tapi sedikit | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 79 | 492 | Observation | `Observation.valueCodeableConcept.coding` | OV000018 | Produksi ASI tidak ada | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 80 | 501 | Observation | `Observation.code.coding` | SP000122 | Catat di Buku KIA | http://terminology.kemkes.go.id/sp |
| 81 | 514 | Observation | `Observation.code.coding` | SP000139 | KB Pasca Plasenta | http://terminology.kemkes.go.id/sp |
| 82 | 515 | Observation | `Observation.valueCodeableConcept.coding` | LA6524-8 | Oral contraceptive pill | http://loinc.org |
| 83 | 516 | Observation | `Observation.valueCodeableConcept.coding` | 237122005.0 | Lactational amenorrhea | http://snomed.info/sct |
| 84 | 517 | Observation | `Observation.valueCodeableConcept.coding` | LA6525-5 | Injectable/implantable hormone | http://loinc.org |
| 85 | 518 | Observation | `Observation.valueCodeableConcept.coding` | LA6527-1 | Intrauterine device | http://loinc.org |
| 86 | 519 | Observation | `Observation.valueCodeableConcept.coding` | SP000097 | Implan | http://terminology.kemkes.go.id/sp |
| 87 | 520 | Observation | `Observation.valueCodeableConcept.coding` | LA6523-0 | Condom | http://loinc.org |
| 88 | 521 | Observation | `Observation.valueCodeableConcept.coding` | 22523008.0 | Vasectomy | http://snomed.info/sct |
| 89 | 522 | Observation | `Observation.valueCodeableConcept.coding` | 77543007.0 | Ligation of fallopian tube | http://snomed.info/sct |
| 90 | 532 | Observation | `Observation.code.coding` | PC000004 | KB Pasca Persalinan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 91 | 533 | Observation | `Observation.valueCodeableConcept.coding` | LA6524-8 | Oral contraceptive pill | http://loinc.org |
| 92 | 534 | Observation | `Observation.valueCodeableConcept.coding` | 237122005.0 | Lactational amenorrhea | http://snomed.info/sct |
| 93 | 535 | Observation | `Observation.valueCodeableConcept.coding` | LA6525-5 | Injectable/implantable hormone | http://loinc.org |
| 94 | 536 | Observation | `Observation.valueCodeableConcept.coding` | LA6527-1 | Intrauterine device | http://loinc.org |
| 95 | 537 | Observation | `Observation.valueCodeableConcept.coding` | SP000097 | Implan | http://terminology.kemkes.go.id/sp |
| 96 | 538 | Observation | `Observation.valueCodeableConcept.coding` | LA6523-0 | Condom | http://loinc.org |
| 97 | 539 | Observation | `Observation.valueCodeableConcept.coding` | 22523008.0 | Vasectomy | http://snomed.info/sct |
| 98 | 540 | Observation | `Observation.valueCodeableConcept.coding` | 77543007.0 | Ligation of fallopian tube | http://snomed.info/sct |
| 99 | 551 | Medication | `Medication.code` | 92000653.0 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula | http://sys-ids.kemkes.go.id/kf |
| 100 | 572 | Medication | `Medication.code` | 93015491.0 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | http://sys-ids.kemkes.go.id/kf |
| 101 | 595 | MedicationRequest | `MedicationRequest.contained.code.coding` | 92000653.0 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula | http://sys-ids.kemkes.go.id/kf |
| 102 | 629 | MedicationDispense | `MedicationDispense.contained.code.coding` | 93015491.0 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | http://sys-ids.kemkes.go.id/kf |
| 103 | 659 | Procedure | `Procedure.code.coding` | 711029005.0 | Counseling about breastfeeding | http://snomed.info/sct |
| 104 | 670 | Procedure | `Procedure.code.coding` | 72531000052105.0 | Counseling for contraception | http://snomed.info/sct |
| 105 | 681 | Procedure | `Procedure.code.coding` | 441041000124100.0 | Counseling about nutrition | http://snomed.info/sct |
| 106 | 693 | Observation | `Observation.code.coding` | SP000138 | Tatalaksana Komplikasi Pre Eklampsia | http://terminology.kemkes.go.id/sp |
| 107 | 705 | Observation | `Observation.code.coding` | SP000389 | Keadaan Ibu | http://terminology.kemkes.go.id/sp |
| 108 | 706 | Observation | `Observation.valueCodeableConcept.coding` | 438949009.0 | Alive | http://snomed.info/sct |
| 109 | 707 | Observation | `Observation.valueCodeableConcept.coding` | 419099009.0 | Dead | http://snomed.info/sct |
| 110 | 720 | ServiceRequest | `ServiceRequest.code.coding` | 409014006.0 | Delivery care management | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 64 |
| http://loinc.org | 20 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 9 |
| http://terminology.kemkes.go.id/sp | 6 |
| http://sys-ids.kemkes.go.id/kf | 4 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 3 |
| http://hl7.org/fhir/sid/icd-10 | 2 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 1 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 1 |
| **Total** | **110** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 36 | – | Jenis Faskes | Organization | `Organization.type` |
| 37 | – | Nama Faskes | Organization | `Organization.name` |
| 702 | – | Keadaan Ibu | – | `` |
| 715 | – | Rujuk | – | `` |
