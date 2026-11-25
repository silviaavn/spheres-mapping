# Output Form: SIM RS Siaga Medika PNC

Sumber: `mapping/phdt-data-dictionary-rs-siaga-medika-pnc.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-rs-siaga-medika-pnc.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 49 |
| Code (`jumlah code` = 1) | 110 |
| Code unik (code + CodeSystem) | 102 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 15 |
| Variabel BQ (unik) | 1 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–27 | Patient | – | – | _Nama Ibu_ → `Patient.name.text` (2, tanpa BQ)<br>_NIK_ → `Patient.identifier.value` (6, tanpa BQ)<br>_No HP_ → `Patient.telecom` (7, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (10, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (11, tanpa BQ)<br>_Alamat Domisili_ → `Patient.address.line` (13, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (18, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (21, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.extension.valueCode` (24, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.extension.valueCode` (27, tanpa BQ) |
| 2 | 28–35 | RelatedPerson | – | – | _Nama Suami/Pendamping_ → `RelatedPerson.name.text` (29, tanpa BQ)<br>_NIK Suami/Pendamping_ → `RelatedPerson.identifier.value` (34, tanpa BQ) |
| 3 | 74–80 | Practitioner | – | – | _NIK_ → `Practitioner.identifier.value` (76, tanpa BQ)<br>_Nama Tenaga Kesehatan_ → `Practitioner.name.text` (78, tanpa BQ)<br>_Jenis Kelamin Tenaga Kesehatan_ → `Practitioner.gender` (79, tanpa BQ) |
| 4 | 81–88 | PractitionerRole | – | – | _Tenaga Pemeriksa_ → `PractitionerRole.code.coding` (85, tanpa BQ) |
| 5 | 89–107 | Encounter | – | – | _Kunjungan_KF_ → `Encounter.identifier` (90, tanpa BQ)<br>_Tanggal_PNC_ → `Encounter.period.start` (102, tanpa BQ)<br>_Cara Masuk_ → `Encounter.hospitalization.admitSource.coding` (137, tanpa BQ) |
| 6 | 108–116 | Condition | 404684003.0 | Clinical finding | _Keluhan_ → `Condition.clinicalStatus.coding` (108, tanpa BQ) |
| 7 | 127–136 | Condition | Z39.2 | Routine postpartum follow-up | _Diagnosis_ → `Condition.code.coding` (129, tanpa BQ) |
| 8 | 144–152 | EpisodeOfCare | PNC | Postnatal Care | – |
| 9 | 153–164 | Observation | 93857-1 | Date and time of obstetric delivery | _Tanggal Persalinan_ → `Observation.valueDateTime` (156, tanpa BQ) |
| 10 | 169–180 | Observation | 11996-6 | [#] Pregnancies | _Gravida_ → `Observation.valueInteger` (173, tanpa BQ) |
| 11 | 181–192 | Observation | 11977-6 | [#] Parity | _Partus_ → `Observation.valueInteger` (185, tanpa BQ) |
| 12 | 193–204 | Observation | 69043-8 | Other pregnancy outcomes # | _Abortus_ → `Observation.valueInteger` (197, tanpa BQ) |
| 13 | 205–216 | Observation | 8462-4 | Diastolic blood pressure | _Tekanan Darah Diastolik_ → `Observation.valueQuantity.value` (208, tanpa BQ) |
| 14 | 217–229 | Observation | 8867-4 | Heart rate | _Nadi_ → `Observation.valueQuantity.value` (220, tanpa BQ) |
| 15 | 230–242 | Observation | – | – | _Suhu_ → `Observation.valueQuantity.value` (233, tanpa BQ) |
| 16 | 243–255 | Observation | 9279-1 | Respiratory rate | _Pernapasan_ → `Observation.valueQuantity.value` (246, tanpa BQ) |
| 17 | 257–263 | Condition | 289530006.0 | Vaginal bleeding | _Pendarahan Pervaginam_ → `Condition.clinicalStatus.coding` (257, tanpa BQ) |
| 18 | 264–275 | Observation | 81661-1 | Blood Loss [Volume] Measured | _Jumlah Pendarahan_ → `Observation.valueQuantity.value` (267, tanpa BQ) |
| 19 | 276–286 | Observation | 364297003.0 | Female perineum observable | _Kondisi Perineum_ → `Observation.valueString` (279, tanpa BQ) |
| 20 | 287–298 | Observation | OC000020 | Tanda Infeksi Perineum | _Tanda Infeksi Perineum_ → `Observation.valueBoolean` (290, tanpa BQ) |
| 21 | 299–310 | Observation | OC000025 | Tanda Infeksi Luka Jahitan Sectio Caesaria | _Tanda Infeksi Luka Jahitan Sectio Caesaria_ → `Observation.valueBoolean` (302, tanpa BQ) |
| 22 | 311–325 | Observation | 32422-8 | Physical findings of breast | _Kondisi Payudara_ → `Observation.valueCodeableConcept.coding` (314, tanpa BQ) |
| 23 | 326–337 | Observation | 289700000.0 | Uterine contractions present | _Kontraksi Uteri_ → `Observation.valueBoolean` (329, tanpa BQ) |
| 24 | 338–351 | Observation | 249214003.0 | Color of lochia | _Warna Lokhia_ → `Observation.valueCodeableConcept.coding` (341, tanpa BQ) |
| 25 | 352–363 | Observation | 249215002.0 | Odor of lochia | _Bau Lokhia_ → `Observation.valueBoolean` (355, tanpa BQ) |
| 26 | 364–381 | Observation | 252041008.0 | Micturition finding | _Gangguan Buang Air Kecil_ → `Observation.valueBoolean` (367, tanpa BQ) |
| 27 | 382–393 | Observation | 300375001.0 | Able to defecate | _Gangguan Buang Air Besar_ → `Observation.valueBoolean` (385, tanpa BQ) |
| 28 | 394–404 | Procedure | 408988007.0 | Newborn care education | _Konseling Perawatan Bayi Baru Lahir_ → `Procedure.category.coding` (394, tanpa BQ) |
| 29 | 405–416 | Observation | 8345-1 | Body weight Measured --post partum | _Berat Badan_ → `Observation.valueQuantity.value` (408, tanpa BQ) |
| 30 | 417–428 | Observation | 8305-5 | Body height --post partum | _Tinggi Badan_ → `Observation.valueQuantity.value` (420, tanpa BQ) |
| 31 | 429–442 | Observation | 284473002.0 | Mid upper arm circumference | _LILA_ → `Observation.valueQuantity.value` (432, tanpa BQ)<br>_Status Gizi KEK/Tidak KEK_ → `Observation.interpretation` (441, tanpa BQ) |
| 32 | 443–455 | Observation | 11881-0 | Uterus Fundal height Tape measure | _TFU_ → `Observation.valueString` (446, tanpa BQ) |
| 33 | 456–466 | Observation | SP000683 | Tatalaksana Tindakan | _Tatalaksana (Tindakan)_ → `Observation.valueString` (459, tanpa BQ) |
| 34 | 467–483 | Condition | 47821001.0 | Postpartum hemorrhage | _Komplikasi Masa Nifas_ → `Condition.clinicalStatus.coding` (467, tanpa BQ) |
| 35 | 484–496 | Observation | 289084000.0 | Difficulty performing breastfeeding | _Apakah ada masalah memberikan ASI_ → `Observation.valueBoolean` (487, tanpa BQ) |
| 36 | 497–510 | Observation | OC000017 | Produksi ASI | _Produksi ASI_ → `Observation.valueCodeableConcept.coding` (500, tanpa BQ)<br>_Catat dibuku KIA_ → `Observation.category.coding` (510, tanpa BQ) |
| 37 | 511–523 | Observation | SP000122 | Catat di Buku KIA | _Metode Kontrasepsi KB Pasca Persalinan_ → `Observation.status` (522, tanpa BQ) |
| 38 | 524–540 | Observation | PC000004 | KB Pasca Persalinan | _Metode Kontrasepsi KB Pasca Plasenta_ → `Observation.status` (539, tanpa BQ) |
| 39 | 541–556 | Observation | SP000139 | KB Pasca Plasenta | – |
| 40 | 557–567 | Procedure | 711029005.0 | Counseling about breastfeeding | _Konseling ASI_ → `Procedure.category.coding` (557, tanpa BQ) |
| 41 | 568–578 | Procedure | ED000008 | Edukasi Tanda Bahaya Kehamilan, Bersalin dan Nifas | _Tanda Bahaya Nifas_ → `Procedure.category.coding` (568, tanpa BQ) |
| 42 | 579–589 | Procedure | 72531000052105.0 | Counseling for contraception | _Konseling KB_ → `Procedure.category.coding` (579, tanpa BQ) |
| 43 | 590–600 | Procedure | SP000135 | Konseling Tanda Bahaya Bayi Baru Lahir | _Konseling Tanda Bahaya Bayi Baru Lahir_ → `Procedure.category.coding` (590, tanpa BQ) |
| 44 | 601–611 | Procedure | 441041000124100.0 | Counseling about nutrition | _Konseling Gizi_ → `Procedure.category.coding` (601, tanpa BQ) |
| 45 | 612–622 | Procedure | PC000001 | Perawatan Tali Pusat | _Konseling Perawatan Tali Pusar_ → `Procedure.category.coding` (612, tanpa BQ) |
| 46 | 623–633 | Procedure | ED000010 | Edukasi PHBS | _Konseling PHBS_ → `Procedure.category.coding` (623, tanpa BQ) |
| 47 | 634–644 | Procedure | ED000012 | Edukasi lainnya | _Konseling Jiwa Pascasalin_ → `Procedure.category.coding` (634, tanpa BQ) |
| 48 | 645–671 | Observation | SP000138 | Tatalaksana Komplikasi Pre Eklampsia | `TATA LAKSANA PE` → `Observation.valueBoolean` (648)<br>_Pantau Tekanan Darah_ → `Observation.component.code.coding` (650, tanpa BQ)<br>_Pantau Protein Urin_ → `Observation.component.code.coding` (653, tanpa BQ)<br>_Pemberian Anti Hipertensi_ → `Observation.component.code` (656, tanpa BQ)<br>_Pemberian MgSO4_ → `Observation.component.code.coding` (659, tanpa BQ)<br>_Pemberian Diazepam Injeksi_ → `Observation.component.code.coding` (662, tanpa BQ) |
| 49 | 673–684 | Observation | SP000389 | Keadaan Ibu | – |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 30 |
| Procedure | 9 |
| Condition | 4 |
| Patient | 1 |
| RelatedPerson | 1 |
| Practitioner | 1 |
| PractitionerRole | 1 |
| Encounter | 1 |
| EpisodeOfCare | 1 |
| **Total** | **49** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 85 | PractitionerRole | `PractitionerRole.code.coding` | 309453006.0 | Registered midwife | http://snomed.info/sct |
| 2 | 86 | PractitionerRole | `PractitionerRole.code.coding` | 309367003.0 | Obstetrician and gynecologist | http://snomed.info/sct |
| 3 | 87 | PractitionerRole | `PractitionerRole.code.coding` | 309343006.0 | Physician | http://snomed.info/sct |
| 4 | 88 | PractitionerRole | `PractitionerRole.code.coding` | 224535009.0 | Registered nurse | http://snomed.info/sct |
| 5 | 110 | Condition | `Condition.code.coding` | 404684003.0 | Clinical finding | http://snomed.info/sct |
| 6 | 129 | Condition | `Condition.code.coding` | Z39.2 | Routine postpartum follow-up | http://hl7.org/fhir/sid/icd-10 |
| 7 | 137 | Encounter | `Encounter.hospitalization.admitSource.coding` | EHA000002 | Datang sendiri | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 8 | 138 | Encounter | `Encounter.hospitalization.admitSource.coding` | 305956004.0 | Referral by physician | http://snomed.info/sct |
| 9 | 139 | Encounter | `Encounter.hospitalization.admitSource.coding` | 306052007.0 | Referral by midwife | http://snomed.info/sct |
| 10 | 140 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000116 | Rujukan dari Puskesmas Pembantu | http://terminology.kemkes.go.id/sp |
| 11 | 141 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000117 | Rujukan dari Puskesmas | http://terminology.kemkes.go.id/sp |
| 12 | 142 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000118 | Rujukan dari Rumah Bersalin / Klinik | http://terminology.kemkes.go.id/sp |
| 13 | 143 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000119 | Rujukan dari Rumah Sakit | http://terminology.kemkes.go.id/sp |
| 14 | 145 | EpisodeOfCare | `EpisodeOfCare.type.coding` | PNC | Postnatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 15 | 155 | Observation | `Observation.code.coding` | 93857-1 | Date and time of obstetric delivery | http://loinc.org |
| 16 | 171 | Observation | `Observation.code.coding` | 11996-6 | [#] Pregnancies | http://loinc.org |
| 17 | 172 | Observation | `Observation.code.coding` | ANC.B6.DE24 | Number of pregnancies (gravida) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 18 | 183 | Observation | `Observation.code.coding` | 11977-6 | [#] Parity | http://loinc.org |
| 19 | 184 | Observation | `Observation.code.coding` | ANC.B6.DE32 | Parity | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 20 | 195 | Observation | `Observation.code.coding` | 69043-8 | Other pregnancy outcomes # | http://loinc.org |
| 21 | 196 | Observation | `Observation.code.coding` | ANC.B6.DE25 | Number of miscarriages and/or abortions | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 22 | 207 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://loinc.org |
| 23 | 219 | Observation | `Observation.code.coding` | 8867-4 | Heart rate | http://loinc.org |
| 24 | 245 | Observation | `Observation.code.coding` | 9279-1 | Respiratory rate | http://loinc.org |
| 25 | 259 | Condition | `Condition.code.coding` | 289530006.0 | Vaginal bleeding | http://snomed.info/sct |
| 26 | 266 | Observation | `Observation.code.coding` | 81661-1 | Blood Loss [Volume] Measured | http://loinc.org |
| 27 | 278 | Observation | `Observation.code.coding` | 364297003.0 | Female perineum observable | http://loinc.org |
| 28 | 289 | Observation | `Observation.code.coding` | OC000020 | Tanda Infeksi Perineum | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 29 | 301 | Observation | `Observation.code.coding` | OC000025 | Tanda Infeksi Luka Jahitan Sectio Caesaria | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 30 | 313 | Observation | `Observation.code.coding` | 32422-8 | Physical findings of breast | http://loinc.org |
| 31 | 314 | Observation | `Observation.valueCodeableConcept.coding` | 300885006.0 | Swelling of breast | http://snomed.info/sct |
| 32 | 315 | Observation | `Observation.valueCodeableConcept.coding` | 290070001.0 | Red breast | http://snomed.info/sct |
| 33 | 316 | Observation | `Observation.valueCodeableConcept.coding` | 54302000.0 | Discharge from nipple | http://snomed.info/sct |
| 34 | 317 | Observation | `Observation.valueCodeableConcept.coding` | 53430007.0 | Pain of breast | http://snomed.info/sct |
| 35 | 318 | Observation | `Observation.valueCodeableConcept.coding` | 290084006.0 | Breast normal | http://snomed.info/sct |
| 36 | 328 | Observation | `Observation.code.coding` | 289700000.0 | Uterine contractions present | http://snomed.info/sct |
| 37 | 340 | Observation | `Observation.code.coding` | 249214003.0 | Color of lochia | http://snomed.info/sct |
| 38 | 341 | Observation | `Observation.valueCodeableConcept.coding` | 278072004.0 | Lochia rubra | http://snomed.info/sct |
| 39 | 342 | Observation | `Observation.valueCodeableConcept.coding` | 449828001.0 | Lochia serosa | http://snomed.info/sct |
| 40 | 343 | Observation | `Observation.valueCodeableConcept.coding` | 113291006.0 | Lochia sanguinolenta | http://snomed.info/sct |
| 41 | 344 | Observation | `Observation.valueCodeableConcept.coding` | 449827006.0 | Lochia alba | http://snomed.info/sct |
| 42 | 354 | Observation | `Observation.code.coding` | 249215002.0 | Odor of lochia | http://snomed.info/sct |
| 43 | 366 | Observation | `Observation.code.coding` | 252041008.0 | Micturition finding | http://snomed.info/sct |
| 44 | 369 | Observation | `Observation.valueCodeableConcept.coding` | 49650001.0 | Dysuria | http://snomed.info/sct |
| 45 | 370 | Observation | `Observation.valueCodeableConcept.coding` | 249288007.0 | Incomplete emptying of urinary bladder | http://snomed.info/sct |
| 46 | 371 | Observation | `Observation.valueCodeableConcept.coding` | 162116003.0 | Increased frequency of urination | http://snomed.info/sct |
| 47 | 372 | Observation | `Observation.valueCodeableConcept.coding` | 42112009.0 | Enuresis | http://snomed.info/sct |
| 48 | 373 | Observation | `Observation.valueCodeableConcept.coding` | 102834005.0 | Normal micturition | http://snomed.info/sct |
| 49 | 374 | Observation | `Observation.valueCodeableConcept.coding` | 267064002.0 | Retention of urine | http://snomed.info/sct |
| 50 | 384 | Observation | `Observation.code.coding` | 300375001.0 | Able to defecate | http://snomed.info/sct |
| 51 | 395 | Procedure | `Procedure.code.coding` | 408988007.0 | Newborn care education | http://snomed.info/sct |
| 52 | 407 | Observation | `Observation.code.coding` | 8345-1 | Body weight Measured --post partum | http://loinc.org |
| 53 | 419 | Observation | `Observation.code.coding` | 8305-5 | Body height --post partum | http://loinc.org |
| 54 | 431 | Observation | `Observation.code.coding` | 284473002.0 | Mid upper arm circumference | http://snomed.info/sct |
| 55 | 441 | Observation | `Observation.interpretation` | OI000018 | Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 56 | 442 | Observation | `Observation.interpretation` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 57 | 445 | Observation | `Observation.code.coding` | 11881-0 | Uterus Fundal height Tape measure | http://loinc.org |
| 58 | 458 | Observation | `Observation.code.coding` | SP000683 | Tatalaksana Tindakan | http://terminology.kemkes.go.id/sp |
| 59 | 469 | Condition | `Condition.code.coding` | 47821001.0 | Postpartum hemorrhage | http://snomed.info/sct |
| 60 | 470 | Condition | `Condition.code.coding` | 198188007.0 | Chronic uterine inflammatory disease | http://snomed.info/sct |
| 61 | 471 | Condition | `Condition.code.coding` | 111367007.0 | Pelvic abscess | http://snomed.info/sct |
| 62 | 472 | Condition | `Condition.code.coding` | 211063003.0 | Infected abrasion of perineum | http://snomed.info/sct |
| 63 | 473 | Condition | `Condition.code.coding` | 76902006.0 | Tetanus | http://snomed.info/sct |
| 64 | 474 | Condition | `Condition.code.coding` | 266579006.0 | Inflammatory disorder of breast | http://snomed.info/sct |
| 65 | 475 | Condition | `Condition.code.coding` | 49746001.0 | Engorgement of breasts | http://snomed.info/sct |
| 66 | 476 | Condition | `Condition.code.coding` | 82231009.0 | Inversion of nipple | http://snomed.info/sct |
| 67 | 477 | Condition | `Condition.code.coding` | 58703003.0 | Postpartum depression | http://snomed.info/sct |
| 68 | 478 | Condition | `Condition.code.coding` | O13 | Gestational [pregnancy-induced] hypertension without signification proteinuria | http://hl7.org/fhir/sid/icd-10 |
| 69 | 479 | Condition | `Condition.code.coding` | O90.8 | Other complications of the puerperium, not elsewhere classified | http://hl7.org/fhir/sid/icd-10 |
| 70 | 486 | Observation | `Observation.code.coding` | 289084000.0 | Difficulty performing breastfeeding | http://snomed.info/sct |
| 71 | 499 | Observation | `Observation.code.coding` | OC000017 | Produksi ASI | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 72 | 500 | Observation | `Observation.valueCodeableConcept.coding` | OV000016 | Produksi ASI ada | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 73 | 501 | Observation | `Observation.valueCodeableConcept.coding` | OV000017 | Produksi ASI ada tapi sedikit | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 74 | 502 | Observation | `Observation.valueCodeableConcept.coding` | OV000018 | Produksi ASI tidak ada | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 75 | 511 | Observation | `Observation.code.coding` | SP000122 | Catat di Buku KIA | http://terminology.kemkes.go.id/sp |
| 76 | 524 | Observation | `Observation.code.coding` | PC000004 | KB Pasca Persalinan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 77 | 525 | Observation | `Observation.valueCodeableConcept.coding` | LA6524-8 | Oral contraceptive pill | http://loinc.org |
| 78 | 526 | Observation | `Observation.valueCodeableConcept.coding` | 237122005.0 | Lactational amenorrhea | http://snomed.info/sct |
| 79 | 527 | Observation | `Observation.valueCodeableConcept.coding` | LA6525-5 | Injectable/implantable hormone | http://loinc.org |
| 80 | 528 | Observation | `Observation.valueCodeableConcept.coding` | LA6527-1 | Intrauterine device | http://loinc.org |
| 81 | 529 | Observation | `Observation.valueCodeableConcept.coding` | SP000097 | Implan | http://terminology.kemkes.go.id/sp |
| 82 | 530 | Observation | `Observation.valueCodeableConcept.coding` | LA6523-0 | Condom | http://loinc.org |
| 83 | 531 | Observation | `Observation.valueCodeableConcept.coding` | 22523008.0 | Vasectomy | http://snomed.info/sct |
| 84 | 532 | Observation | `Observation.valueCodeableConcept.coding` | 77543007.0 | Ligation of fallopian tube | http://snomed.info/sct |
| 85 | 541 | Observation | `Observation.code.coding` | SP000139 | KB Pasca Plasenta | http://terminology.kemkes.go.id/sp |
| 86 | 542 | Observation | `Observation.valueCodeableConcept.coding` | LA6524-8 | Oral contraceptive pill | http://loinc.org |
| 87 | 543 | Observation | `Observation.valueCodeableConcept.coding` | 237122005.0 | Lactational amenorrhea | http://snomed.info/sct |
| 88 | 544 | Observation | `Observation.valueCodeableConcept.coding` | LA6525-5 | Injectable/implantable hormone | http://loinc.org |
| 89 | 545 | Observation | `Observation.valueCodeableConcept.coding` | LA6527-1 | Intrauterine device | http://loinc.org |
| 90 | 546 | Observation | `Observation.valueCodeableConcept.coding` | SP000097 | Implan | http://terminology.kemkes.go.id/sp |
| 91 | 547 | Observation | `Observation.valueCodeableConcept.coding` | LA6523-0 | Condom | http://loinc.org |
| 92 | 548 | Observation | `Observation.valueCodeableConcept.coding` | 22523008.0 | Vasectomy | http://snomed.info/sct |
| 93 | 549 | Observation | `Observation.valueCodeableConcept.coding` | 77543007.0 | Ligation of fallopian tube | http://snomed.info/sct |
| 94 | 558 | Procedure | `Procedure.code.coding` | 711029005.0 | Counseling about breastfeeding | http://snomed.info/sct |
| 95 | 569 | Procedure | `Procedure.code.coding` | ED000008 | Edukasi Tanda Bahaya Kehamilan, Bersalin dan Nifas | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 96 | 580 | Procedure | `Procedure.code.coding` | 72531000052105.0 | Counseling for contraception | http://snomed.info/sct |
| 97 | 591 | Procedure | `Procedure.code.coding` | SP000135 | Konseling Tanda Bahaya Bayi Baru Lahir | http://terminology.kemkes.go.id/sp |
| 98 | 602 | Procedure | `Procedure.code.coding` | 441041000124100.0 | Counseling about nutrition | http://snomed.info/sct |
| 99 | 613 | Procedure | `Procedure.code.coding` | PC000001 | Perawatan Tali Pusat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 100 | 624 | Procedure | `Procedure.code.coding` | ED000010 | Edukasi PHBS | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 101 | 635 | Procedure | `Procedure.code.coding` | ED000012 | Edukasi lainnya | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 102 | 647 | Observation | `Observation.code.coding` | SP000138 | Tatalaksana Komplikasi Pre Eklampsia | http://terminology.kemkes.go.id/sp |
| 103 | 650 | Observation | `Observation.component.code.coding` | 135840009 | Blood pressure monitoring | http://snomed.info/sct |
| 104 | 653 | Observation | `Observation.component.code.coding` | SP000133 | Pemantauan Protein Urin | http://terminology.kemkes.go.id/sp |
| 105 | 656 | Observation | `Observation.component.code` | 308116003.0 | Antihypertensive therapy | http://snomed.info/sct |
| 106 | 659 | Observation | `Observation.component.code.coding` | SP000136 | Pemberian MgSO4 | http://terminology.kemkes.go.id/sp |
| 107 | 662 | Observation | `Observation.component.code.coding` | SP000137 | Pemberian Diazepam Injeksi | http://terminology.kemkes.go.id/sp |
| 108 | 675 | Observation | `Observation.code.coding` | SP000389 | Keadaan Ibu | http://terminology.kemkes.go.id/sp |
| 109 | 676 | Observation | `Observation.valueCodeableConcept.coding` | 438949009.0 | Alive | http://snomed.info/sct |
| 110 | 677 | Observation | `Observation.valueCodeableConcept.coding` | 419099009.0 | Dead | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 53 |
| http://loinc.org | 21 |
| http://terminology.kemkes.go.id/sp | 15 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 13 |
| http://hl7.org/fhir/sid/icd-10 | 3 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 3 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 1 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 1 |
| **Total** | **110** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 40 | – | Faskes yang Melayani PNC | Organization | `Organization.name` |
| 672 | – | Keadaan Ibu | – | `` |
| 685 | – | Apakah pasien dirujuk? | – | `ServiceRequest` |
| 698 | – | Faskes Rujukan | – | `ServiceRequest` |
| 705 | – | Nama Faskes Rujukan | – | `ServiceRequest` |
