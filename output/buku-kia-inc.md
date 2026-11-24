# Output Form: Buku KIA - INC (2024)

Sumber: `mapping/phdt-data-dictionary-buku-kia-inc.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-buku-kia-inc.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 60 |
| Code (`jumlah code` = 1) | 108 |
| Code unik (code + CodeSystem) | 97 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 4 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 3–9 | CarePlan | – | – | – |
| 2 | 10–13 | Patient | – | – | _Saya (Nama Ibu)_ → `Patient.name.text` (11, tanpa BQ)<br>_Alamat_ → `Patient.address.line` (13, tanpa BQ)<br>_Nama Ibu_ → `Patient.name.text` (94, tanpa BQ)<br>_NIK Ibu_ → `Patient.identifier.use` (95, tanpa BQ)<br>_Jenis Kelamin Ibu_ → `Patient.gender` (98, tanpa BQ)<br>_Nama Anak_ → `Patient.name.text` (100, tanpa BQ)<br>_NIK Anak_ → `Patient.identifier.use` (101, tanpa BQ)<br>_Jenis Kelamin Anak_ → `Patient.gender` (105, tanpa BQ)<br>_Diberi nama (nama bayi)_ → `Patient.name.text` (445, tanpa BQ)<br>_Alamat (nama jalan)_ → `Patient.address.line` (447, tanpa BQ)<br>_RT_ → `Patient.address.extension.extension.url` (449, tanpa BQ)<br>_RW_ → `Patient.address.extension.extension.url` (452, tanpa BQ)<br>_Kecamatan_ → `Patient.address.extension.extension.url` (455, tanpa BQ)<br>_Kab./Kota_ → `Patient.address.extension.extension.url` (458, tanpa BQ) |
| 3 | 14–17 | CarePlan | – | – | _Bulan, tahun (HPL)_ → `CarePlan.supportingInfo.reference` (17, tanpa BQ) |
| 4 | 18–29 | Observation | 11778-8 | Delivery date Estimated | – |
| 5 | 30–30 | CarePlan | – | – | _Asuransi_ → `CarePlan.supportingInfo.reference` (30, tanpa BQ) |
| 6 | 31–39 | Coverage | – | – | – |
| 7 | 41–49 | CarePlan | – | – | _Bidan/dokter_ → `CarePlan.activity.detail.performer.display` (44, tanpa BQ)<br>_Nama fasyankes_ → `CarePlan.activity.detail.performer.display` (46, tanpa BQ)<br>_Untuk kendaraan/ambulan desa oleh_ → `CarePlan.activity.detail.code.coding` (48, tanpa BQ) |
| 8 | 50–53 | Practitioner | – | – | _(Nama PJ Ambulans)_ → `Practitioner.name.text` (50, tanpa BQ)<br>_HP (No HP PJ Ambulans)_ → `Practitioner.telecom` (51, tanpa BQ) |
| 9 | 54–56 | CarePlan | – | – | _Untuk sumbangan darah ..._ → `CarePlan.activity.detail.code.coding` (55, tanpa BQ) |
| 10 | 57–70 | Observation | 883-9 | ABO group [Type] in Blood | _Golongan darah_ → `Observation.valueCodeableConcept.coding` (61, tanpa BQ) |
| 11 | 71–71 | CarePlan | – | – | – |
| 12 | 72–84 | Observation | 10331-7 | Rh [Type] in Blood | _Rhesus_ → `Observation.valueCodeableConcept.coding` (76, tanpa BQ) |
| 13 | 85–86 | CarePlan | – | – | _Dibantu oleh_ → `CarePlan.activity.detail.performer.reference` (85, tanpa BQ) |
| 14 | 87–92 | RelatedPerson | – | – | _(Nama Penyumbang Darah)_ → `RelatedPerson.name.text` (88, tanpa BQ)<br>_HP (No HP Penyumbang Darah)_ → `RelatedPerson.telecom` (89, tanpa BQ) |
| 15 | 107–122 | Encounter | – | – | _Encounter INC_ → `Encounter.identifier` (107, tanpa BQ)<br>_Encounter bayi_ → `Encounter.identifier` (167, tanpa BQ) |
| 16 | 123–130 | Condition | 386337006 | Intrapartal care | – |
| 17 | 142–161 | EpisodeOfCare | ANC | Antenatal Care | _Menutup EOC ANC_ → `EpisodeOfCare.identifier` (142, tanpa BQ)<br>_Membuat EOC PNC_ → `EpisodeOfCare.identifier` (157, tanpa BQ) |
| 18 | 162–165 | EpisodeOfCare | PNC | Postnatal Care | – |
| 19 | 182–188 | Condition | Z00.1 | Routine child health examination | – |
| 20 | 200–208 | EpisodeOfCare | Neonate | Neonate | _Membuat EOC Neo_ → `EpisodeOfCare.Identifer` (200, tanpa BQ) |
| 21 | 209–220 | Observation | 93857-1 | Date and time of obstetric delivery | _Tanggal Melahirkan, Pukul_ → `Observation.valueDateTime` (212, tanpa BQ)<br>_Keterangan Tambahan_ → `Observation.note` (220, tanpa BQ) |
| 22 | 221–235 | Observation | 76516-4 | Gestational age—​at birth | _Umur Kehamilan_ → `Observation.valueQuantity.value` (224, tanpa BQ) |
| 23 | 236–249 | Observation | OC000013 | Penolong Persalinan | _Penolong Proses Melahirkan_ → `Observation.valueCodeableConcept.coding` (239, tanpa BQ)<br>_(Nama Penolong Persalinan)_ → `Observation.valueCodeableConcept.text` (242, tanpa BQ) |
| 24 | 250–260 | Observation | 57071-3 | Obstetric delivery method | _Cara Melahirkan_ → `Observation.valueCodeableConcept.coding` (253, tanpa BQ) |
| 25 | 261–279 | Observation | 405195003 | Intrapartum maternal status | _Keadaan Ibu_ → `Observation.valueCodeableConcept.coding` (264, tanpa BQ) |
| 26 | 280–298 | Observation | SP000139 | KB Pasca Plasenta | _KB Pasca Melahirkan_ → `Observation.valueString` (283, tanpa BQ) |
| 27 | 299–309 | Observation | 365475008 | Place in family order | _Anak ke_ → `Observation.valueInteger` (302, tanpa BQ) |
| 28 | 310–321 | Observation | 8339-4 | Birth weight Measured | _Berat Lahir_ → `Observation.valueQuantity.value` (313, tanpa BQ) |
| 29 | 322–333 | Observation | 89269-5 | Body height Measured --at birth | _Panjang Badan_ → `Observation.valueQuantity.value` (325, tanpa BQ) |
| 30 | 334–345 | Observation | 8290-9 | Head Occipital-frontal circumference --at birth- by Tape measure | _Lingkar Kepala_ → `Observation.valueQuantity.value` (337, tanpa BQ) |
| 31 | 346–358 | Observation | 76689-9 | Sex assigned at birth | _Jenis Kelamin_ → `Observation.valueCodeableConcept.coding` (349, tanpa BQ) |
| 32 | 359–378 | Observation | 249222005 | Neonatal condition | _Kondisi bayi saat lahir_ → `Observation.valueCodeableConcept.coding` (362, tanpa BQ)<br>_Keterangan tambahan_ → `Observation.note` (378, tanpa BQ) |
| 33 | 379–388 | Procedure | 431868002 | Initiation of breastfeeding | _Asuhan Bayi Baru Lahir_ → `Procedure.category.coding` (379, tanpa BQ) |
| 34 | 389–400 | Observation | OC000016 | Waktu Inisiasi Menyusui Dini | – |
| 35 | 401–411 | Procedure | 448883004 | Injection of vitamin K1 | _Suntikan Vitamin K1_ → `Procedure.category.coding` (401, tanpa BQ) |
| 36 | 412–422 | Procedure | PC000002 | Pemberian Salep Antibiotik Mata | _Salep mata Antibiotika Profilaksis_ → `Procedure.category.coding` (412, tanpa BQ) |
| 37 | 423–436 | Immunization | – | – | _Imunisasi HB0_ → `Immunization.status` (423, tanpa BQ) |
| 38 | 438–444 | Composition | – | – | _No_ → `Composition.identifier.value` (439, tanpa BQ) |
| 39 | 460–469 | Composition | – | – | _Tanggal ... 20..._ → `Composition.date` (461, tanpa BQ)<br>_Pada hari ini Tanggal Pukul_ → `Composition.section.entry.reference` (467, tanpa BQ) |
| 40 | 470–484 | Observation | OC000013 | Penolong Persalinan | _Jenis Kelahiran_ → `Observation.valueCodeableConcept.coding` (473, tanpa BQ) |
| 41 | 485–490 | Composition | – | – | _Anak ke-_ → `Composition.section.entry.reference` (485, tanpa BQ)<br>_Usia gestasi_ → `Composition.section.entry.reference` (486, tanpa BQ)<br>_Berat Lahir_ → `Composition.section.entry.reference` (487, tanpa BQ)<br>_Panjang Badan_ → `Composition.section.entry.reference` (488, tanpa BQ)<br>_Lingkar Kepala_ → `Composition.section.entry.reference` (489, tanpa BQ) |
| 42 | 491–504 | Observation | 72150-6 | Delivery location | _Di (jenis faskes)_ → `Observation.valueCodeableConcept.coding` (494, tanpa BQ) |
| 43 | 505–509 | Composition | – | – | _di (nama faskes)_ → `Composition.section.entry.reference` (505, tanpa BQ)<br>_Alamat (faskes)_ → `Composition.section.entry.reference` (506, tanpa BQ) |
| 44 | 510–516 | RelatedPerson | – | – | _Nama Ibu_ → `RelatedPerson.name.text` (513, tanpa BQ)<br>_NIK (Ibu)_ → `RelatedPerson.identifier.value` (516, tanpa BQ) |
| 45 | 517–528 | Observation | 85724-3 | Age of Mother --at delivery | – |
| 46 | 529–535 | RelatedPerson | – | – | _Nama Ayah_ → `RelatedPerson.name.text` (532, tanpa BQ)<br>_NIK (Ayah)_ → `RelatedPerson.identifier.value` (535, tanpa BQ) |
| 47 | 536–546 | Observation | OC000149 | Pekerjaan orang tua | _Pekerjaan_ → `Observation.valueString` (539, tanpa BQ) |
| 48 | 552–563 | Observation | 11996-6 | [#] Pregnancies | _G_ → `Observation.valueInteger` (556, tanpa BQ) |
| 49 | 564–575 | Observation | 11977-6 | [#] Parity | _P_ → `Observation.valueInteger` (568, tanpa BQ) |
| 50 | 576–587 | Observation | 69043-8 | Other pregnancy outcomes # | _A_ → `Observation.valueInteger` (580, tanpa BQ) |
| 51 | 588–600 | Observation | 93857-1 | Date and time of obstetric delivery | _Pada Hari ..., Tanggal ..., Pukul ..._ → `Observation.valueDateTime` (592, tanpa BQ) |
| 52 | 601–610 | Observation | 57071-3 | Obstetric delivery method | _Cara Persalinan_ → `Observation.valueCodeableConcept.coding` (604, tanpa BQ) |
| 53 | 611–623 | Procedure | 73.59 | Other manually assisted delivery | _Dengan Tindakan_ → `Procedure.category.coding` (611, tanpa BQ) |
| 54 | 624–636 | Observation | OC000013 | Penolong Persalinan | _Penolong Kelahiran_ → `Observation.valueCodeableConcept.coding` (627, tanpa BQ) |
| 55 | 637–648 | Observation | 11778-8 | Delivery date Estimated | _Taksiran Melahirkan_ → `Observation.valueDateTime` (641, tanpa BQ) |
| 56 | 649–659 | Observation | 72150-6 | Delivery location | _Fasyankes (tempat melahirkan)_ → `Observation.valueString` (652, tanpa BQ) |
| 57 | 660–673 | ServiceRequest | 409014006 | Delivery care management | _Rujukan_ → `ServiceRequest.status` (660, tanpa BQ) |
| 58 | 674–684 | Procedure | 431868002 | Initiation of breastfeeding | _Inisiasi Menyusu Dini_ → `Procedure.category.coding` (674, tanpa BQ) |
| 59 | 685–695 | Procedure | 50475006 | Foot printing of newborn infant | _Cap Kaki Bayi_ → `Procedure.category.coding` (685, tanpa BQ) |
| 60 | 696–698 | BodyStructure | – | – | – |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 28 |
| CarePlan | 7 |
| Procedure | 6 |
| Composition | 4 |
| RelatedPerson | 3 |
| EpisodeOfCare | 3 |
| Condition | 2 |
| Patient | 1 |
| Coverage | 1 |
| Practitioner | 1 |
| Encounter | 1 |
| Immunization | 1 |
| ServiceRequest | 1 |
| BodyStructure | 1 |
| **Total** | **60** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 20 | Observation | `Observation.code.coding` | 11778-8 | Delivery date Estimated | http://loinc.org |
| 2 | 21 | Observation | `Observation.code.coding` | ANC.B6.DE22 | Expected date of delivery (EDD) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 3 | 42 | CarePlan | `CarePlan.activity.detail.code.coding` | 236973005 | Delivery procedure | http://snomed.info/sct |
| 4 | 48 | CarePlan | `CarePlan.activity.detail.code.coding` | 424483007 | Transportation details | http://snomed.info/sct |
| 5 | 55 | CarePlan | `CarePlan.activity.detail.code.coding` | 105470007 | Blood donor | http://snomed.info/sct |
| 6 | 59 | Observation | `Observation.code.coding` | 883-9 | ABO group [Type] in Blood | http://loinc.org |
| 7 | 60 | Observation | `Observation.code.coding` | ANC.B9.DE24 | Blood type | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 8 | 61 | Observation | `Observation.valueCodeableConcept.coding` | LA19710-5 | Group A | http://loinc.org |
| 9 | 62 | Observation | `Observation.valueCodeableConcept.coding` | LA19709-7 | Group B | http://loinc.org |
| 10 | 63 | Observation | `Observation.valueCodeableConcept.coding` | LA19708-9 | Group O | http://loinc.org |
| 11 | 64 | Observation | `Observation.valueCodeableConcept.coding` | LA28449-9 | Group AB | http://loinc.org |
| 12 | 74 | Observation | `Observation.code.coding` | 10331-7 | Rh [Type] in Blood | http://loinc.org |
| 13 | 75 | Observation | `Observation.code.coding` | ANC.B9.DE29 | Rh factor | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 14 | 76 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 15 | 77 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 16 | 125 | Condition | `Condition.code.coding` | 386337006 | Intrapartal care | http://snomed.info/sct |
| 17 | 150 | EpisodeOfCare | `EpisodeOfCare.type.coding` | ANC | Antenatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 18 | 162 | EpisodeOfCare | `EpisodeOfCare.type.coding` | PNC | Postnatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 19 | 184 | Condition | `Condition.code.coding` | Z00.1 | Routine child health examination | http://hl7.org/fhir/sid/icd-10 |
| 20 | 205 | EpisodeOfCare | `EpisodeOfCare.type.coding` | Neonate | Neonate | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 21 | 211 | Observation | `Observation.code.coding` | 93857-1 | Date and time of obstetric delivery | http://loinc.org |
| 22 | 223 | Observation | `Observation.code.coding` | 76516-4 | Gestational age—​at birth | http://loinc.org |
| 23 | 226 | Observation | `Observation.component.code.coding` | SP000398 | Usia Kehamilan Saat Persalinan (hari) | http://terminology.kemkes.go.id/sp |
| 24 | 238 | Observation | `Observation.code.coding` | OC000013 | Penolong Persalinan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 25 | 239 | Observation | `Observation.valueCodeableConcept.coding` | 11935004 | Obstetrician | http://snomed.info/sct |
| 26 | 240 | Observation | `Observation.valueCodeableConcept.coding` | 309343006 | Physician | http://snomed.info/sct |
| 27 | 241 | Observation | `Observation.valueCodeableConcept.coding` | 309453006 | Registered midwife | http://snomed.info/sct |
| 28 | 252 | Observation | `Observation.code.coding` | 57071-3 | Obstetric delivery method | http://loinc.org |
| 29 | 253 | Observation | `Observation.valueCodeableConcept.coding` | 48782003 | Delivery normal | http://snomed.info/sct |
| 30 | 254 | Observation | `Observation.valueCodeableConcept.coding` | SP000689 | Persalinan dengan Tindakan | http://terminology.kemkes.go.id/sp |
| 31 | 263 | Observation | `Observation.code.coding` | 405195003 | Intrapartum maternal status | http://snomed.info/sct |
| 32 | 264 | Observation | `Observation.valueCodeableConcept.coding` | 102514002 | Well female adult | http://snomed.info/sct |
| 33 | 265 | Observation | `Observation.valueCodeableConcept.coding` | 39104002 | Illness | http://snomed.info/sct |
| 34 | 266 | Observation | `Observation.valueCodeableConcept.coding` | 131148009 | Bleeding | http://snomed.info/sct |
| 35 | 267 | Observation | `Observation.valueCodeableConcept.coding` | 386661006 | Fever | http://snomed.info/sct |
| 36 | 268 | Observation | `Observation.valueCodeableConcept.coding` | 91175000 | Seizure | http://snomed.info/sct |
| 37 | 269 | Observation | `Observation.valueCodeableConcept.coding` | 249215002 | Odor of lochia | http://snomed.info/sct |
| 38 | 270 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 39 | 272 | Observation | `Observation.valueCodeableConcept.coding` | 59283008 | Maternal death | http://snomed.info/sct |
| 40 | 282 | Observation | `Observation.code.coding` | SP000139 | KB Pasca Plasenta | http://terminology.kemkes.go.id/sp |
| 41 | 284 | Observation | `Observation.valueCodeableConcept.coding` | LA6524-8 | Oral contraceptive pill | http://loinc.org |
| 42 | 285 | Observation | `Observation.valueCodeableConcept.coding` | 237122005 | Lactational amenorrhea | http://snomed.info/sct |
| 43 | 286 | Observation | `Observation.valueCodeableConcept.coding` | LA6525-5 | Injectable/implantable hormone | http://loinc.org |
| 44 | 287 | Observation | `Observation.valueCodeableConcept.coding` | LA6527-1 | Intrauterine device | http://loinc.org |
| 45 | 288 | Observation | `Observation.valueCodeableConcept.coding` | SP000097 | Implan | http://terminology.kemkes.go.id/sp |
| 46 | 289 | Observation | `Observation.valueCodeableConcept.coding` | LA6523-0 | Condom | http://loinc.org |
| 47 | 290 | Observation | `Observation.valueCodeableConcept.coding` | 22523008 | Vasectomy | http://snomed.info/sct |
| 48 | 291 | Observation | `Observation.valueCodeableConcept.coding` | 77543007 | Ligation of fallopian tube | http://snomed.info/sct |
| 49 | 301 | Observation | `Observation.code.coding` | 365475008 | Place in family order | http://snomed.info/sct |
| 50 | 312 | Observation | `Observation.code.coding` | 8339-4 | Birth weight Measured | http://loinc.org |
| 51 | 324 | Observation | `Observation.code.coding` | 89269-5 | Body height Measured --at birth | http://loinc.org |
| 52 | 336 | Observation | `Observation.code.coding` | 8290-9 | Head Occipital-frontal circumference --at birth- by Tape measure | http://loinc.org |
| 53 | 348 | Observation | `Observation.code.coding` | 76689-9 | Sex assigned at birth | http://loinc.org |
| 54 | 349 | Observation | `Observation.valueCodeableConcept.coding` | LA2-8 | Male | http://loinc.org |
| 55 | 350 | Observation | `Observation.valueCodeableConcept.coding` | LA3-6 | Female | http://loinc.org |
| 56 | 351 | Observation | `Observation.valueCodeableConcept.coding` | LA4489-6 | Unknown | http://loinc.org |
| 57 | 361 | Observation | `Observation.code.coding` | 249222005 | Neonatal condition | http://snomed.info/sct |
| 58 | 362 | Observation | `Observation.valueCodeableConcept.coding` | LA6727-7 | Good, strong cry; normal rate and effort of breathing | http://loinc.org |
| 59 | 363 | Observation | `Observation.valueCodeableConcept.coding` | LA6726-9 | Weak cry; may sound like whimpering, slow or irregular breathing | http://loinc.org |
| 60 | 364 | Observation | `Observation.valueCodeableConcept.coding` | LA6725-1 | Not breathing | http://loinc.org |
| 61 | 365 | Observation | `Observation.valueCodeableConcept.coding` | LA6724-4 | Good color all over | http://loinc.org |
| 62 | 366 | Observation | `Observation.valueCodeableConcept.coding` | LA6723-6 | Good color in body with bluish hands or feet | http://loinc.org |
| 63 | 367 | Observation | `Observation.valueCodeableConcept.coding` | LA6722-8 | The baby's whole body is completely bluish-gray or pale | http://loinc.org |
| 64 | 368 | Observation | `Observation.valueCodeableConcept.coding` | 66091009 | Congenital disease | http://snomed.info/sct |
| 65 | 370 | Observation | `Observation.valueCodeableConcept.coding` | 419099009 | Dead | http://snomed.info/sct |
| 66 | 381 | Procedure | `Procedure.code.coding` | 431868002 | Initiation of breastfeeding | http://snomed.info/sct |
| 67 | 390 | Observation | `Observation.code.coding` | OC000016 | Waktu Inisiasi Menyusui Dini | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 68 | 391 | Observation | `Observation.valueCodeableConcept.coding` | OV000014 | Kurang dari 1 Jam | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 69 | 392 | Observation | `Observation.valueCodeableConcept.coding` | OV000015 | Lebih dari 1 Jam | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 70 | 404 | Procedure | `Procedure.code.coding` | 448883004 | Injection of vitamin K1 | http://snomed.info/sct |
| 71 | 415 | Procedure | `Procedure.code.coding` | PC000002 | Pemberian Salep Antibiotik Mata | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 72 | 426 | Immunization | `Immunization.vaccineCode` | VG45 | HepB | http://sys-ids.kemkes.go.id/kfa |
| 73 | 472 | Observation | `Observation.code.coding` | OC000013 | Penolong Persalinan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 74 | 473 | Observation | `Observation.valueCodeableConcept.coding` | Observation | Observation.valueCodeableConcept.coding | 237244005 |
| 75 | 474 | Observation | `Observation.valueCodeableConcept.coding` | Observation | Observation.valueCodeableConcept.coding | 65147003 |
| 76 | 475 | Observation | `Observation.valueCodeableConcept.coding` | Observation | Observation.valueCodeableConcept.coding | 64254006 |
| 77 | 476 | Observation | `Observation.valueCodeableConcept.coding` | Observation | Observation.valueCodeableConcept.coding | OV000394 |
| 78 | 493 | Observation | `Observation.code.coding` | 72150-6 | Delivery location | http://loinc.org |
| 79 | 494 | Observation | `Observation.valueCodeableConcept.coding` | 104 | Rumah Sakit | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 80 | 495 | Observation | `Observation.valueCodeableConcept.coding` | 102 | Pusat Kesehatan Masyarakat | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 81 | 496 | Observation | `Observation.valueCodeableConcept.coding` | OT000008 | Rumah Bersalin | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 82 | 497 | Observation | `Observation.valueCodeableConcept.coding` | OT000004 | Bidan Praktek Mandiri | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 83 | 519 | Observation | `Observation.code.coding` | 85724-3 | Age of Mother --at delivery | http://loinc.org |
| 84 | 538 | Observation | `Observation.code.coding` | OC000149 | Pekerjaan orang tua | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 85 | 554 | Observation | `Observation.code.coding` | 11996-6 | [#] Pregnancies | http://loinc.org |
| 86 | 555 | Observation | `Observation.code.coding` | ANC.B6.DE24 | Number of pregnancies (gravida) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 87 | 566 | Observation | `Observation.code.coding` | 11977-6 | [#] Parity | http://loinc.org |
| 88 | 567 | Observation | `Observation.code.coding` | ANC.B6.DE32 | Parity | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 89 | 578 | Observation | `Observation.code.coding` | 69043-8 | Other pregnancy outcomes # | http://loinc.org |
| 90 | 579 | Observation | `Observation.code.coding` | ANC.B6.DE25 | Number of miscarriages and/or abortions | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 91 | 590 | Observation | `Observation.code.coding` | 93857-1 | Date and time of obstetric delivery | http://loinc.org |
| 92 | 603 | Observation | `Observation.code.coding` | 57071-3 | Obstetric delivery method | http://loinc.org |
| 93 | 604 | Observation | `Observation.valueCodeableConcept.coding` | 177184002 | Normal delivery procedure | http://snomed.info/sct |
| 94 | 605 | Observation | `Observation.valueCodeableConcept.coding` | 237311001 | Breech delivery | http://snomed.info/sct |
| 95 | 612 | Procedure | `Procedure.code.coding` | 73.59 | Other manually assisted delivery | http://hl7.org/fhir/sid/icd-9-cm |
| 96 | 613 | Procedure | `Procedure.code.coding` | 72.7 | Vacuum extraction | http://hl7.org/fhir/sid/icd-9-cm |
| 97 | 614 | Procedure | `Procedure.code.coding` | 72 | Low forceps delivery | http://hl7.org/fhir/sid/icd-9-cm |
| 98 | 615 | Procedure | `Procedure.code.coding` | 74.1 | Classical cesarean section | http://hl7.org/fhir/sid/icd-9-cm |
| 99 | 626 | Observation | `Observation.code.coding` | OC000013 | Penolong Persalinan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 100 | 627 | Observation | `Observation.valueCodeableConcept.coding` | 11935004 | Obstetrician | http://snomed.info/sct |
| 101 | 628 | Observation | `Observation.valueCodeableConcept.coding` | 309343006 | Physician | http://snomed.info/sct |
| 102 | 629 | Observation | `Observation.valueCodeableConcept.coding` | 309453006 | Registered midwife | http://snomed.info/sct |
| 103 | 639 | Observation | `Observation.code.coding` | 11778-8 | Delivery date Estimated | http://loinc.org |
| 104 | 640 | Observation | `Observation.code.coding` | ANC.B6.DE22 | Expected date of delivery (EDD) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 105 | 651 | Observation | `Observation.code.coding` | 72150-6 | Delivery location | http://loinc.org |
| 106 | 664 | ServiceRequest | `ServiceRequest.code.coding` | 409014006 | Delivery care management | http://snomed.info/sct |
| 107 | 676 | Procedure | `Procedure.code.coding` | 431868002 | Initiation of breastfeeding | http://snomed.info/sct |
| 108 | 687 | Procedure | `Procedure.code.coding` | 50475006 | Foot printing of newborn infant | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://loinc.org | 38 |
| http://snomed.info/sct | 34 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 8 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 7 |
| http://terminology.kemkes.go.id/sp | 4 |
| http://terminology.kemkes.go.id/CodeSystem/organization-type | 4 |
| http://hl7.org/fhir/sid/icd-9-cm | 4 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 3 |
| http://hl7.org/fhir/sid/icd-10 | 1 |
| http://sys-ids.kemkes.go.id/kfa | 1 |
| 237244005 | 1 |
| 65147003 | 1 |
| 64254006 | 1 |
| OV000394 | 1 |
| **Total** | **108** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 547 | – | TTD Saksi I | – | `` |
| 548 | – | TTD Saksi II | – | `` |
| 549 | – | TTD Penolong Kelahiran | – | `` |
| 551 | – | Encounter INC | – | `` |
