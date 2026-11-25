# Output Form: SIM RS MPH PNC

Sumber: `mapping/phdt-data-dictionary-rs-mph-pnc.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-rs-mph-pnc.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 43 |
| Code (`jumlah code` = 1) | 104 |
| Code unik (code + CodeSystem) | 91 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 6 |
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
| 7 | 103–118 | Encounter | – | – | _Kunjungan Nifas (KF)_ → `Encounter.identifier` (103, tanpa BQ)<br>_Tanggal Masuk PNC_ → `Encounter.period.start` (113, tanpa BQ)<br>_Cara Masuk_ → `Encounter.hospitalization.admitSource.coding` (148, tanpa BQ) |
| 8 | 119–126 | Condition | 386337006 | Intrapartal care | – |
| 9 | 129–137 | Condition | 404684003 | Clinical finding | _Keluhan_ → `Condition.clinicalStatus.coding` (129, tanpa BQ) |
| 10 | 150–158 | EpisodeOfCare | PNC | Postnatal Care | – |
| 11 | 159–170 | Observation | 11996-6 | [#] Pregnancies | _Gravida_ → `Observation.valueInteger` (163, tanpa BQ) |
| 12 | 171–182 | Observation | 11977-6 | [#] Parity | _Partus_ → `Observation.valueInteger` (175, tanpa BQ) |
| 13 | 183–194 | Observation | 69043-8 | Other pregnancy outcomes # | _Abortus_ → `Observation.valueInteger` (187, tanpa BQ) |
| 14 | 195–206 | Observation | 8480-6 | Systolic blood pressure | _Tekanan Darah Sistolik_ → `Observation.valueQuantity.value` (198, tanpa BQ) |
| 15 | 207–218 | Observation | 8462-4 | Diastolic blood pressure | _Tekanan Darah Diastolik_ → `Observation.valueQuantity.value` (210, tanpa BQ) |
| 16 | 219–231 | Observation | 8867-4 | Heart rate | _Frekuensi Nadi_ → `Observation.valueQuantity.value` (222, tanpa BQ) |
| 17 | 232–244 | Observation | 9279-1 | Respiratory rate | _Pernapasan_ → `Observation.valueQuantity.value` (235, tanpa BQ) |
| 18 | 246–252 | Condition | 289530006 | Vaginal bleeding | _Pendarahan Pervaginam_ → `Condition.clinicalStatus.coding` (246, tanpa BQ) |
| 19 | 253–267 | Observation | 364297003 | Female perineum observable | _Kondisi Perineum_ → `Observation.valueCodeableConcept.coding` (256, tanpa BQ) |
| 20 | 268–279 | Observation | OC000020 | Tanda Infeksi Perineum | _Tanda Infeksi Perineum_ → `Observation.valueBoolean` (271, tanpa BQ) |
| 21 | 280–291 | Observation | OC000025 | Tanda Infeksi Luka Jahitan Sectio Caesaria | _Tanda Infeksi Luka Jahitan Sectio Caesaria_ → `Observation.valueBoolean` (283, tanpa BQ) |
| 22 | 292–306 | Observation | 32422-8 | Physical findings of breast | _Kondisi Payudara_ → `Observation.valueCodeableConcept.coding` (295, tanpa BQ) |
| 23 | 307–318 | Observation | 289700000 | Uterine contractions present | _Kontraksi Uteri_ → `Observation.valueBoolean` (310, tanpa BQ) |
| 24 | 319–332 | Observation | 249214003 | Color of lochia | _Warna Lokhia_ → `Observation.valueCodeableConcept.coding` (322, tanpa BQ) |
| 25 | 333–344 | Observation | 249215002 | Odor of lochia | _Bau Lokhia_ → `Observation.valueBoolean` (336, tanpa BQ) |
| 26 | 345–360 | Observation | 252041008 | Micturition finding | _Gangguan Buang Air Kecil_ → `Observation.valueCodeableConcept.coding` (348, tanpa BQ) |
| 27 | 361–372 | Observation | 300375001 | Able to defecate | _Gangguan Buang Air Besar_ → `Observation.valueBoolean` (364, tanpa BQ) |
| 28 | 373–383 | Procedure | 408988007 | Newborn care education | _Konseling Perawatan Bayi Baru Lahir_ → `Procedure.category.coding` (373, tanpa BQ) |
| 29 | 384–395 | Observation | 8345-1 | Body weight Measured --post partum | _Berat Badan_ → `Observation.valueQuantity.value` (387, tanpa BQ) |
| 30 | 396–407 | Observation | 8305-5 | Body height --post partum | _Tinggi Badan_ → `Observation.valueQuantity.value` (399, tanpa BQ) |
| 31 | 408–421 | Observation | 284473002 | Mid upper arm circumference | _LILA_ → `Observation.valueQuantity.value` (411, tanpa BQ)<br>_Status Gizi KEK/Tidak KEK_ → `Observation.interpretation` (420, tanpa BQ) |
| 32 | 422–434 | Observation | 11881-0 | Uterus Fundal height Tape measure | _TFU_ → `Observation.valueString` (425, tanpa BQ) |
| 33 | 435–452 | Condition | 47821001 | Postpartum hemorrhage | _Komplikasi Masa Nifas_ → `Condition.clinicalStatus.coding` (435, tanpa BQ) |
| 34 | 453–465 | Observation | 289084000 | Difficulty performing breastfeeding | _Apakah ada masalah memberikan ASI_ → `Observation.valueBoolean` (456, tanpa BQ)<br>_Catatan ASI_ → `Observation.note.text` (465, tanpa BQ) |
| 35 | 466–479 | Observation | OC000017 | Produksi ASI | _Produksi ASI_ → `Observation.valueCodeableConcept.coding` (469, tanpa BQ)<br>_Catat dibuku KIA_ → `Observation.category.coding` (479, tanpa BQ) |
| 36 | 480–492 | Observation | SP000122 | Catat di Buku KIA | _Metode Kontrasepsi KB Pasca Plasenta_ → `Observation.status` (491, tanpa BQ) |
| 37 | 493–510 | Observation | SP000139 | KB Pasca Plasenta | _Metode Kontrasepsi KB Pasca Persalinan_ → `Observation.status` (509, tanpa BQ) |
| 38 | 511–526 | Observation | PC000004 | KB Pasca Persalinan | – |
| 39 | 527–537 | Procedure | 409019001 | Postpartum care management | _Tatalaksana PNC_ → `Procedure.category.coding` (527, tanpa BQ) |
| 40 | 538–548 | Observation | SP000138 | Tatalaksana Komplikasi Pre Eklampsia | _Tatalaksana Komplikasi Pre Eklampsia dan Eklampsia_ → `Observation.valueString` (541, tanpa BQ) |
| 41 | 550–561 | Observation | SP000389 | Keadaan Ibu | – |
| 42 | 563–576 | ServiceRequest | 409014006 | Delivery care management | _Nama Faskes Rujukan_ → `ServiceRequest.locationCode.text` (576, tanpa BQ) |
| 43 | 577–591 | ServiceRequest | 185389009 | Follow-up visit | _Tindak Lanjut_ → `ServiceRequest.status` (577, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 27 |
| Condition | 4 |
| Practitioner | 2 |
| PractitionerRole | 2 |
| Procedure | 2 |
| ServiceRequest | 2 |
| Patient | 1 |
| RelatedPerson | 1 |
| Encounter | 1 |
| EpisodeOfCare | 1 |
| **Total** | **43** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 83 | PractitionerRole | `PractitionerRole.code.coding` | 309453006 | Registered midwife | http://snomed.info/sct |
| 2 | 84 | PractitionerRole | `PractitionerRole.code.coding` | 309367003 | Obstetrician and gynecologist | http://snomed.info/sct |
| 3 | 85 | PractitionerRole | `PractitionerRole.code.coding` | 309343006 | Physician | http://snomed.info/sct |
| 4 | 86 | PractitionerRole | `PractitionerRole.code.coding` | 224535009 | Registered nurse | http://snomed.info/sct |
| 5 | 87 | PractitionerRole | `PractitionerRole.code.coding` | 224535009 | Registered nurse | http://snomed.info/sct |
| 6 | 98 | PractitionerRole | `PractitionerRole.code.coding` | 309453006 | Registered midwife | http://snomed.info/sct |
| 7 | 99 | PractitionerRole | `PractitionerRole.code.coding` | 309367003 | Obstetrician and gynecologist | http://snomed.info/sct |
| 8 | 100 | PractitionerRole | `PractitionerRole.code.coding` | 309343006 | Physician | http://snomed.info/sct |
| 9 | 101 | PractitionerRole | `PractitionerRole.code.coding` | 224535009 | Registered nurse | http://snomed.info/sct |
| 10 | 102 | PractitionerRole | `PractitionerRole.code.coding` | 56542007 | Medical record administrator | http://snomed.info/sct |
| 11 | 121 | Condition | `Condition.code.coding` | 386337006 | Intrapartal care | http://snomed.info/sct |
| 12 | 131 | Condition | `Condition.code.coding` | 404684003 | Clinical finding | http://snomed.info/sct |
| 13 | 148 | Encounter | `Encounter.hospitalization.admitSource.coding` | EHA000002 | Datang sendiri | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 14 | 149 | Encounter | `Encounter.hospitalization.admitSource.coding` | 3457005 | Patient referral | http://snomed.info/sct |
| 15 | 151 | EpisodeOfCare | `EpisodeOfCare.type.coding` | PNC | Postnatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 16 | 161 | Observation | `Observation.code.coding` | 11996-6 | [#] Pregnancies | http://loinc.org |
| 17 | 162 | Observation | `Observation.code.coding` | ANC.B6.DE24 | Number of pregnancies (gravida) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 18 | 173 | Observation | `Observation.code.coding` | 11977-6 | [#] Parity | http://loinc.org |
| 19 | 174 | Observation | `Observation.code.coding` | ANC.B6.DE32 | Parity | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 20 | 185 | Observation | `Observation.code.coding` | 69043-8 | Other pregnancy outcomes # | http://loinc.org |
| 21 | 186 | Observation | `Observation.code.coding` | ANC.B6.DE25 | Number of miscarriages and/or abortions | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 22 | 197 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 23 | 209 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://loinc.org |
| 24 | 221 | Observation | `Observation.code.coding` | 8867-4 | Heart rate | http://loinc.org |
| 25 | 234 | Observation | `Observation.code.coding` | 9279-1 | Respiratory rate | http://loinc.org |
| 26 | 248 | Condition | `Condition.code.coding` | 289530006 | Vaginal bleeding | http://snomed.info/sct |
| 27 | 255 | Observation | `Observation.code.coding` | 364297003 | Female perineum observable | http://loinc.org |
| 28 | 256 | Observation | `Observation.valueCodeableConcept.coding` | 289854007 | Perineum intact | http://snomed.info/sct |
| 29 | 257 | Observation | `Observation.valueCodeableConcept.coding` | 57759005 | First degree perineal laceration | http://snomed.info/sct |
| 30 | 258 | Observation | `Observation.valueCodeableConcept.coding` | 6234006 | Second degree perineal laceration | http://snomed.info/sct |
| 31 | 259 | Observation | `Observation.valueCodeableConcept.coding` | 10217006 | Third degree perineal laceration | http://snomed.info/sct |
| 32 | 260 | Observation | `Observation.valueCodeableConcept.coding` | 399031001 | Fourth degree perineal laceration | http://snomed.info/sct |
| 33 | 270 | Observation | `Observation.code.coding` | OC000020 | Tanda Infeksi Perineum | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 34 | 282 | Observation | `Observation.code.coding` | OC000025 | Tanda Infeksi Luka Jahitan Sectio Caesaria | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 35 | 294 | Observation | `Observation.code.coding` | 32422-8 | Physical findings of breast | http://loinc.org |
| 36 | 295 | Observation | `Observation.valueCodeableConcept.coding` | 300885006 | Swelling of breast | http://snomed.info/sct |
| 37 | 296 | Observation | `Observation.valueCodeableConcept.coding` | 290070001 | Red breast | http://snomed.info/sct |
| 38 | 297 | Observation | `Observation.valueCodeableConcept.coding` | 54302000 | Discharge from nipple | http://snomed.info/sct |
| 39 | 298 | Observation | `Observation.valueCodeableConcept.coding` | 53430007 | Pain of breast | http://snomed.info/sct |
| 40 | 299 | Observation | `Observation.valueCodeableConcept.coding` | 290084006 | Breast normal | http://snomed.info/sct |
| 41 | 309 | Observation | `Observation.code.coding` | 289700000 | Uterine contractions present | http://snomed.info/sct |
| 42 | 321 | Observation | `Observation.code.coding` | 249214003 | Color of lochia | http://snomed.info/sct |
| 43 | 322 | Observation | `Observation.valueCodeableConcept.coding` | 278072004 | Lochia rubra | http://snomed.info/sct |
| 44 | 323 | Observation | `Observation.valueCodeableConcept.coding` | 449828001 | Lochia serosa | http://snomed.info/sct |
| 45 | 324 | Observation | `Observation.valueCodeableConcept.coding` | 113291006 | Lochia sanguinolenta | http://snomed.info/sct |
| 46 | 325 | Observation | `Observation.valueCodeableConcept.coding` | 449827006 | Lochia alba | http://snomed.info/sct |
| 47 | 335 | Observation | `Observation.code.coding` | 249215002 | Odor of lochia | http://snomed.info/sct |
| 48 | 347 | Observation | `Observation.code.coding` | 252041008 | Micturition finding | http://snomed.info/sct |
| 49 | 348 | Observation | `Observation.valueCodeableConcept.coding` | 49650001 | Dysuria | http://snomed.info/sct |
| 50 | 349 | Observation | `Observation.valueCodeableConcept.coding` | 249288007 | Incomplete emptying of urinary bladder | http://snomed.info/sct |
| 51 | 350 | Observation | `Observation.valueCodeableConcept.coding` | 162116003 | Increased frequency of urination | http://snomed.info/sct |
| 52 | 351 | Observation | `Observation.valueCodeableConcept.coding` | 42112009 | Enuresis | http://snomed.info/sct |
| 53 | 352 | Observation | `Observation.valueCodeableConcept.coding` | 102834005 | Normal micturition | http://snomed.info/sct |
| 54 | 353 | Observation | `Observation.valueCodeableConcept.coding` | 267064002 | Retention of urine | http://snomed.info/sct |
| 55 | 363 | Observation | `Observation.code.coding` | 300375001 | Able to defecate | http://snomed.info/sct |
| 56 | 374 | Procedure | `Procedure.code.coding` | 408988007 | Newborn care education | http://snomed.info/sct |
| 57 | 386 | Observation | `Observation.code.coding` | 8345-1 | Body weight Measured --post partum | http://loinc.org |
| 58 | 398 | Observation | `Observation.code.coding` | 8305-5 | Body height --post partum | http://loinc.org |
| 59 | 410 | Observation | `Observation.code.coding` | 284473002 | Mid upper arm circumference | http://snomed.info/sct |
| 60 | 420 | Observation | `Observation.interpretation` | OI000018 | Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 61 | 421 | Observation | `Observation.interpretation` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 62 | 424 | Observation | `Observation.code.coding` | 11881-0 | Uterus Fundal height Tape measure | http://loinc.org |
| 63 | 437 | Condition | `Condition.code.coding` | 47821001 | Postpartum hemorrhage | http://snomed.info/sct |
| 64 | 438 | Condition | `Condition.code.coding` | 198188007 | Chronic uterine inflammatory disease | http://snomed.info/sct |
| 65 | 439 | Condition | `Condition.code.coding` | 111367007 | Pelvic abscess | http://snomed.info/sct |
| 66 | 440 | Condition | `Condition.code.coding` | 211063003 | Infected abrasion of perineum | http://snomed.info/sct |
| 67 | 441 | Condition | `Condition.code.coding` | 76902006 | Tetanus | http://snomed.info/sct |
| 68 | 442 | Condition | `Condition.code.coding` | 266579006 | Inflammatory disorder of breast | http://snomed.info/sct |
| 69 | 443 | Condition | `Condition.code.coding` | 49746001 | Engorgement of breasts | http://snomed.info/sct |
| 70 | 444 | Condition | `Condition.code.coding` | 82231009 | Inversion of nipple | http://snomed.info/sct |
| 71 | 445 | Condition | `Condition.code.coding` | 58703003 | Postpartum depression | http://snomed.info/sct |
| 72 | 446 | Condition | `Condition.code.coding` | O13 | Gestational [pregnancy-induced] hypertension without signification proteinuria | http://hl7.org/fhir/sid/icd-10 |
| 73 | 447 | Condition | `Condition.code.coding` | O90.8 | Other complications of the puerperium, not elsewhere classified | http://hl7.org/fhir/sid/icd-10 |
| 74 | 455 | Observation | `Observation.code.coding` | 289084000 | Difficulty performing breastfeeding | http://snomed.info/sct |
| 75 | 468 | Observation | `Observation.code.coding` | OC000017 | Produksi ASI | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 76 | 469 | Observation | `Observation.valueCodeableConcept.coding` | OV000016 | Produksi ASI ada | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 77 | 470 | Observation | `Observation.valueCodeableConcept.coding` | OV000017 | Produksi ASI ada tapi sedikit | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 78 | 471 | Observation | `Observation.valueCodeableConcept.coding` | OV000018 | Produksi ASI tidak ada | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 79 | 480 | Observation | `Observation.code.coding` | SP000122 | Catat di Buku KIA | http://terminology.kemkes.go.id/sp |
| 80 | 493 | Observation | `Observation.code.coding` | SP000139 | KB Pasca Plasenta | http://terminology.kemkes.go.id/sp |
| 81 | 494 | Observation | `Observation.valueCodeableConcept.coding` | LA6524-8 | Oral contraceptive pill | http://loinc.org |
| 82 | 495 | Observation | `Observation.valueCodeableConcept.coding` | 237122005 | Lactational amenorrhea | http://snomed.info/sct |
| 83 | 496 | Observation | `Observation.valueCodeableConcept.coding` | LA6525-5 | Injectable/implantable hormone | http://loinc.org |
| 84 | 497 | Observation | `Observation.valueCodeableConcept.coding` | LA6527-1 | Intrauterine device | http://loinc.org |
| 85 | 498 | Observation | `Observation.valueCodeableConcept.coding` | SP000097 | Implan | http://terminology.kemkes.go.id/sp |
| 86 | 499 | Observation | `Observation.valueCodeableConcept.coding` | LA6523-0 | Condom | http://loinc.org |
| 87 | 500 | Observation | `Observation.valueCodeableConcept.coding` | 22523008 | Vasectomy | http://snomed.info/sct |
| 88 | 501 | Observation | `Observation.valueCodeableConcept.coding` | 77543007 | Ligation of fallopian tube | http://snomed.info/sct |
| 89 | 511 | Observation | `Observation.code.coding` | PC000004 | KB Pasca Persalinan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 90 | 512 | Observation | `Observation.valueCodeableConcept.coding` | LA6524-8 | Oral contraceptive pill | http://loinc.org |
| 91 | 513 | Observation | `Observation.valueCodeableConcept.coding` | 237122005 | Lactational amenorrhea | http://snomed.info/sct |
| 92 | 514 | Observation | `Observation.valueCodeableConcept.coding` | LA6525-5 | Injectable/implantable hormone | http://loinc.org |
| 93 | 515 | Observation | `Observation.valueCodeableConcept.coding` | LA6527-1 | Intrauterine device | http://loinc.org |
| 94 | 516 | Observation | `Observation.valueCodeableConcept.coding` | SP000097 | Implan | http://terminology.kemkes.go.id/sp |
| 95 | 517 | Observation | `Observation.valueCodeableConcept.coding` | LA6523-0 | Condom | http://loinc.org |
| 96 | 518 | Observation | `Observation.valueCodeableConcept.coding` | 22523008 | Vasectomy | http://snomed.info/sct |
| 97 | 519 | Observation | `Observation.valueCodeableConcept.coding` | 77543007 | Ligation of fallopian tube | http://snomed.info/sct |
| 98 | 528 | Procedure | `Procedure.code.coding` | 409019001 | Postpartum care management | http://snomed.info/sct |
| 99 | 540 | Observation | `Observation.code.coding` | SP000138 | Tatalaksana Komplikasi Pre Eklampsia | http://terminology.kemkes.go.id/sp |
| 100 | 552 | Observation | `Observation.code.coding` | SP000389 | Keadaan Ibu | http://terminology.kemkes.go.id/sp |
| 101 | 553 | Observation | `Observation.valueCodeableConcept.coding` | 438949009 | Alive | http://snomed.info/sct |
| 102 | 554 | Observation | `Observation.valueCodeableConcept.coding` | 419099009 | Dead | http://snomed.info/sct |
| 103 | 567 | ServiceRequest | `ServiceRequest.code.coding` | 409014006 | Delivery care management | http://snomed.info/sct |
| 104 | 581 | ServiceRequest | `ServiceRequest.code.coding` | 185389009 | Follow-up visit | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 62 |
| http://loinc.org | 20 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 9 |
| http://terminology.kemkes.go.id/sp | 6 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 3 |
| http://hl7.org/fhir/sid/icd-10 | 2 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 1 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 1 |
| **Total** | **104** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 39 | – | Jenis Faskes | Organization | `Organization.type` |
| 40 | – | Nama Faskes | Organization | `Organization.name` |
| 549 | – | Keadaan Ibu | – | `` |
| 562 | – | Rujuk | – | `` |
