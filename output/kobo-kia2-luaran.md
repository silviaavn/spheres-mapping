# Output Form: Kobo Buku KIA 2 - Luaran Kehamilan

Sumber: `mapping/phdt-data-dictionary-kobo-kia2-luaran.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-kobo-kia2-luaran.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 38 |
| Code (`jumlah code` = 1) | 87 |
| Code unik (code + CodeSystem) | 80 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 3 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–6 | PractitionerRole | – | – | _Siapa yang melakukan entry data?_ → `PractitionerRole.code.coding` (2, tanpa BQ)<br>_jenis_tenaga_kesehatan_ → `PractitionerRole.active` (5, tanpa BQ) |
| 2 | 7–11 | PractitionerRole | – | – | – |
| 3 | 12–32 | Practitioner | – | – | _ID tenaga kesehatan yang menolong persalinan/luaran kehamilan_ → `Practitioner.identifier` (13, tanpa BQ)<br>_Nama lengkap tenaga kesehatan yang menolong persalinan/luaran kehamilan_ → `Practitioner.name.text` (14, tanpa BQ) |
| 4 | 33–47 | EpisodeOfCare | ANC | Antenatal Care | – |
| 5 | 48–63 | Encounter | – | – | _Tanggal Lahir Bayi/Tanggal Abortus_ → `Encounter.period.start` (58, tanpa BQ) |
| 6 | 64–71 | Condition | 386337006 | Intrapartal care | – |
| 7 | 83–92 | Patient | – | – | _Nama lengkap ibu_ → `Patient.name.text` (83, tanpa BQ)<br>_Tulis Nomor Induk Kependudukan (NIK)_ → `Patient.identifier.value` (86, tanpa BQ)<br>_Tulis Nomor Induk Kependudukan (NIK) (Tulis kedua kali)_ → `Patient.identifier.value` (90, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (92, tanpa BQ)<br>_Nama lengkap bayi_ → `Patient.name.text` (250, tanpa BQ)<br>_NIK Bayi_ → `Patient.identifier.use` (251, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (258, tanpa BQ)<br>_Tanggal lahir bayi_ → `Patient.birthDate` (260, tanpa BQ) |
| 8 | 93–104 | Observation | 30525-0 | Age | _Usia_ → `Observation.valueQuantity.value` (96, tanpa BQ) |
| 9 | 105–118 | Observation | 57722-1 | Birth plurality of Pregnancy | _Jumlah Janin_ → `Observation.valueInteger` (108, tanpa BQ) |
| 10 | 119–129 | Observation | 11638-4 | [#] Births.still living | _Sebutkan jumlah janin yang dilahirkan_ → `Observation.valueInteger` (122, tanpa BQ) |
| 11 | 130–144 | Observation | 63893-2 | Outcome of pregnancy | _Status ibu/ bayi saat konfirmasi?_ → `Observation.valueCodeableConcept.coding` (133, tanpa BQ) |
| 12 | 145–156 | Observation | 64710-7 | Was your pregnancy a live birth, stillbirth, miscarriage, abortion, or ectopic pregnancy [PhenX] | _Status bayi saat dilahirkan?_ → `Observation.valueCodeableConcept.coding` (148, tanpa BQ) |
| 13 | 157–169 | Observation | 249197004 | Maternal condition during puerperium (observable entity) | _Bagaimana keadaan Ibu setelah persalinan/luaran kehamilan?_ → `Observation.valueCodeableConcept.coding` (160, tanpa BQ) |
| 14 | 170–183 | Observation | 249222005 | Neonatal condition | _Bagaimana keadaan Bayi setelah persalinan/luaran kehamilan?_ → `Observation.valueCodeableConcept.coding` (173, tanpa BQ) |
| 15 | 184–195 | Observation | 11778-8 | Delivery date Estimated | _HPL_ → `Observation.valueDateTime` (188, tanpa BQ) |
| 16 | 196–207 | Condition | 398254007 | Pre-eclampsia | _Apakah Ibu memiliki kondisi medis tertentu?_ → `Condition.clinicalStatus.coding` (196, tanpa BQ)<br>_Kondisi apa?_ → `Condition.code.text` (202, tanpa BQ) |
| 17 | 208–226 | Observation | 8659-5 | Birth control method - Reported | _Metode kontrasepsi yang digunakan_ → `Observation.valueCodeableConcept.coding` (211, tanpa BQ) |
| 18 | 227–237 | Observation | 79192-1 | Maternal pregnancy information Narrative | _Keterangan tambahan (status ibu)_ → `Observation.valueString` (230, tanpa BQ)<br>_Keterangan tambahan (status ibu)_ → `Observation.performer.display` (237, tanpa BQ) |
| 19 | 238–249 | Observation | 76516-4 | Gestational age—​at birth | _Usia kehamilan saat lahir berapa minggu?_ → `Observation.valueQuantity.value` (241, tanpa BQ) |
| 20 | 261–274 | Observation | 72150-6 | Delivery location | _Tempat lahir_ → `Observation.valueCodeableConcept.coding` (264, tanpa BQ)<br>_Nama tempat_ → `Observation.note` (274, tanpa BQ) |
| 21 | 275–286 | Observation | 8339-4 | Birth weight Measured | _Berat Badan Saat Lahir_ → `Observation.valueQuantity.value` (278, tanpa BQ) |
| 22 | 287–298 | Observation | 89269-5 | Body height Measured --at birth | _Panjang Badan Saat Lahir_ → `Observation.valueQuantity.value` (290, tanpa BQ) |
| 23 | 299–310 | Observation | 8290-9 | Head Occipital-frontal circumference --at birth- by Tape measure | _Lingkar Kepala Saat Lahir_ → `Observation.valueQuantity.value` (302, tanpa BQ) |
| 24 | 311–325 | Observation | 57071-3 | Obstetric delivery method | _Metode persalinan_ → `Observation.valueCodeableConcept.coding` (314, tanpa BQ) |
| 25 | 326–336 | Observation | 57074-7 | Labor and delivery process Narrative | _Indikasi persalinan_ → `Observation.valueString` (329, tanpa BQ) |
| 26 | 337–355 | Observation | 302079008 | Finding of state at birth | _Kondisi bayi saat lahir_ → `Observation.valueCodeableConcept.coding` (340, tanpa BQ)<br>_Keterangan tambahan (status bayi)_ → `Observation.note` (355, tanpa BQ) |
| 27 | 356–367 | Observation | 76516-4 | Gestational age—​at birth | _Usia kehamilan?_ → `Observation.valueQuantity.value` (359, tanpa BQ) |
| 28 | 368–378 | Observation | 63963-3 | Date of end of pregnancy | _Tanggal abortus_ → `Observation.valueDateTime` (371, tanpa BQ) |
| 29 | 379–389 | Observation | 310506006 | Reason for termination of pregnancy | _Penyebab abortus_ → `Observation.valueString` (382, tanpa BQ) |
| 30 | 390–401 | Procedure | 69.0 | Dilation and curettage of uterus | _Kuretase?_ → `Procedure.category.coding` (390, tanpa BQ)<br>_Tempat kuretase_ → `Procedure.location.display` (401, tanpa BQ) |
| 31 | 402–412 | Observation | 82810-3 | Pregnancy status | _Apakah saat ini sudah dalam kondisi hamil kembali?_ → `Observation.valueCodeableConcept.coding` (405, tanpa BQ) |
| 32 | 413–423 | Observation | 81956-5 | Date and time of death [TimeStamp] | _Tanggal Ibu meninggal_ → `Observation.valueDateTime` (416, tanpa BQ) |
| 33 | 424–434 | Observation | LT000005 | Alamat Mati | _Tempat Ibu meninggal_ → `Observation.valueString` (427, tanpa BQ) |
| 34 | 435–445 | Observation | 79378-6 | Cause of death | _Penyebab kematian Ibu_ → `Observation.valueString` (438, tanpa BQ) |
| 35 | 446–458 | Observation | OC000026 | Masa terjadi Kematian Ibu | _Masa terjadi kematian Ibu_ → `Observation.valueCodeableConcept` (449, tanpa BQ) |
| 36 | 459–469 | Observation | 81956-5 | Date and time of death [TimeStamp] | _Tanggal bayi meninggal_ → `Observation.valueDateTime` (462, tanpa BQ) |
| 37 | 470–480 | Observation | LT000005 | Alamat Mati | _Tempat bayi meninggal_ → `Observation.valueString` (473, tanpa BQ) |
| 38 | 481–491 | Observation | 79378-6 | Cause of death | _Penyebab kematian_ → `Observation.valueString` (484, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 29 |
| PractitionerRole | 2 |
| Condition | 2 |
| Practitioner | 1 |
| EpisodeOfCare | 1 |
| Encounter | 1 |
| Patient | 1 |
| Procedure | 1 |
| **Total** | **38** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 2 | PractitionerRole | `PractitionerRole.code.coding` | 223366009 | Healthcare professional | http://snomed.info/sct |
| 2 | 3 | PractitionerRole | `PractitionerRole.code.coding` | SP000396 | Data entry staff | http://terminology.kemkes.go.id/sp |
| 3 | 4 | PractitionerRole | `PractitionerRole.code.coding` | SP000397 | Field/call center staff | http://terminology.kemkes.go.id/sp |
| 4 | 7 | PractitionerRole | `PractitionerRole.code.coding` | 309453006 | Registered midwife | http://snomed.info/sct |
| 5 | 8 | PractitionerRole | `PractitionerRole.code.coding` | 309343006 | Physician | http://snomed.info/sct |
| 6 | 9 | PractitionerRole | `PractitionerRole.code.coding` | 309367003 | Obstetrician and gynecologist | http://snomed.info/sct |
| 7 | 10 | PractitionerRole | `PractitionerRole.code.coding` | 224535009 | Registered nurse | http://snomed.info/sct |
| 8 | 41 | EpisodeOfCare | `EpisodeOfCare.type.coding` | ANC | Antenatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 9 | 66 | Condition | `Condition.code.coding` | 386337006 | Intrapartal care | http://snomed.info/sct |
| 10 | 95 | Observation | `Observation.code.coding` | 30525-0 | Age | http://loinc.org |
| 11 | 107 | Observation | `Observation.code.coding` | 57722-1 | Birth plurality of Pregnancy | http://loinc.org |
| 12 | 121 | Observation | `Observation.code.coding` | 11638-4 | [#] Births.still living | http://loinc.org |
| 13 | 132 | Observation | `Observation.code.coding` | 63893-2 | Outcome of pregnancy | http://loinc.org |
| 14 | 133 | Observation | `Observation.valueCodeableConcept.coding` | LA14270-5 | Live birth | http://loinc.org |
| 15 | 134 | Observation | `Observation.valueCodeableConcept.coding` | LA14273-9 | Induced abortion | http://loinc.org |
| 16 | 135 | Observation | `Observation.valueCodeableConcept.coding` | LA14271-3 | Stillborn | http://loinc.org |
| 17 | 136 | Observation | `Observation.valueCodeableConcept.coding` | LA14272-1 | Miscarriage | http://loinc.org |
| 18 | 137 | Observation | `Observation.valueCodeableConcept.coding` | 59283008 | Maternal death | http://snomed.info/sct |
| 19 | 147 | Observation | `Observation.code.coding` | 64710-7 | Was your pregnancy a live birth, stillbirth, miscarriage, abortion, or ectopic pregnancy [PhenX] | http://loinc.org |
| 20 | 148 | Observation | `Observation.valueCodeableConcept.coding` | 276507005 | Fetal death | http://snomed.info/sct |
| 21 | 149 | Observation | `Observation.valueCodeableConcept.coding` | 276506001 | Newborn death | http://snomed.info/sct |
| 22 | 159 | Observation | `Observation.code.coding` | 249197004 | Maternal condition during puerperium (observable entity) | http://snomed.info/sct |
| 23 | 160 | Observation | `Observation.valueCodeableConcept.coding` | 102514002 | Well female adult | http://snomed.info/sct |
| 24 | 161 | Observation | `Observation.valueCodeableConcept.coding` | 39104002 | Illness | http://snomed.info/sct |
| 25 | 162 | Observation | `Observation.valueCodeableConcept.coding` | 59283008 | Maternal death | http://snomed.info/sct |
| 26 | 172 | Observation | `Observation.code.coding` | 249222005 | Neonatal condition | http://snomed.info/sct |
| 27 | 173 | Observation | `Observation.valueCodeableConcept.coding` | 438949009 | Alive | http://snomed.info/sct |
| 28 | 174 | Observation | `Observation.valueCodeableConcept.coding` | 419099009 | Dead | http://snomed.info/sct |
| 29 | 175 | Observation | `Observation.valueCodeableConcept.coding` | 39104002 | Illness | http://snomed.info/sct |
| 30 | 186 | Observation | `Observation.code.coding` | 11778-8 | Delivery date Estimated | http://loinc.org |
| 31 | 187 | Observation | `Observation.code.coding` | ANC.B6.DE22 | Expected date of delivery (EDD) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 32 | 198 | Condition | `Condition.code.coding` | 398254007 | Pre-eclampsia | http://snomed.info/sct |
| 33 | 199 | Condition | `Condition.code.coding` | OI000018 | Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 34 | 200 | Condition | `Condition.code.coding` | 72892002 | Normal pregnancy | http://snomed.info/sct |
| 35 | 201 | Condition | `Condition.code.coding` | 198609003 | Complication of pregnancy, childbirth and/or puerperium | http://snomed.info/sct |
| 36 | 210 | Observation | `Observation.code.coding` | 8659-5 | Birth control method - Reported | http://loinc.org |
| 37 | 211 | Observation | `Observation.valueCodeableConcept.coding` | LA6524-8 | Oral contraceptive pill | http://loinc.org |
| 38 | 212 | Observation | `Observation.valueCodeableConcept.coding` | 237122005 | Lactational amenorrhea | http://snomed.info/sct |
| 39 | 213 | Observation | `Observation.valueCodeableConcept.coding` | LA6525-5 | Injectable/implantable hormone | http://loinc.org |
| 40 | 214 | Observation | `Observation.valueCodeableConcept.coding` | LA6527-1 | Intrauterine device | http://loinc.org |
| 41 | 215 | Observation | `Observation.valueCodeableConcept.coding` | SP000097 | Implan | http://terminology.kemkes.go.id/sp |
| 42 | 216 | Observation | `Observation.valueCodeableConcept.coding` | LA6523-0 | Condom | http://loinc.org |
| 43 | 217 | Observation | `Observation.valueCodeableConcept.coding` | 22523008 | Vasectomy | http://snomed.info/sct |
| 44 | 218 | Observation | `Observation.valueCodeableConcept.coding` | 77543007 | Ligation of fallopian tube | http://snomed.info/sct |
| 45 | 219 | Observation | `Observation.valueCodeableConcept.coding` | 445375000 | Does not use contraception | http://snomed.info/sct |
| 46 | 229 | Observation | `Observation.code.coding` | 79192-1 | Maternal pregnancy information Narrative | http://loinc.org |
| 47 | 240 | Observation | `Observation.code.coding` | 76516-4 | Gestational age—​at birth | http://loinc.org |
| 48 | 263 | Observation | `Observation.code.coding` | 72150-6 | Delivery location | http://loinc.org |
| 49 | 264 | Observation | `Observation.valueCodeableConcept.coding` | OT000001 | Polindes | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 50 | 265 | Observation | `Observation.valueCodeableConcept.coding` | 102 | Pusat Kesehatan Masyarakat | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 51 | 266 | Observation | `Observation.valueCodeableConcept.coding` | 104 | Rumah Sakit | hhttp://terminology.kemkes.go.id/CodeSystem/organization-type |
| 52 | 277 | Observation | `Observation.code.coding` | 8339-4 | Birth weight Measured | http://loinc.org |
| 53 | 289 | Observation | `Observation.code.coding` | 89269-5 | Body height Measured --at birth | http://loinc.org |
| 54 | 301 | Observation | `Observation.code.coding` | 8290-9 | Head Occipital-frontal circumference --at birth- by Tape measure | http://loinc.org |
| 55 | 313 | Observation | `Observation.code.coding` | 57071-3 | Obstetric delivery method | http://loinc.org |
| 56 | 314 | Observation | `Observation.valueCodeableConcept.coding` | 48782003 | Delivery normal | http://snomed.info/sct |
| 57 | 315 | Observation | `Observation.valueCodeableConcept.coding` | 236974004 | Instrumental delivery | http://snomed.info/sct |
| 58 | 316 | Observation | `Observation.valueCodeableConcept.coding` | 200138003 | Vacuum extractor delivery - delivered | http://snomed.info/sct |
| 59 | 317 | Observation | `Observation.valueCodeableConcept.coding` | 200130005 | Forceps delivery - delivered | http://snomed.info/sct |
| 60 | 318 | Observation | `Observation.valueCodeableConcept.coding` | 200144004 | Deliveries by cesarean | http://snomed.info/sct |
| 61 | 328 | Observation | `Observation.code.coding` | 57074-7 | Labor and delivery process Narrative | http://loinc.org |
| 62 | 339 | Observation | `Observation.code.coding` | 302079008 | Finding of state at birth | http://snomed.info/sct |
| 63 | 340 | Observation | `Observation.valueCodeableConcept.coding` | LA6727-7 | Good, strong cry; normal rate and effort of breathing | http://loinc.org |
| 64 | 341 | Observation | `Observation.valueCodeableConcept.coding` | LA6726-9 | Weak cry; may sound like whimpering, slow or irregular breathing | http://loinc.org |
| 65 | 342 | Observation | `Observation.valueCodeableConcept.coding` | LA6725-1 | Not breathing | http://loinc.org |
| 66 | 343 | Observation | `Observation.valueCodeableConcept.coding` | LA6724-4 | Good color all over | http://loinc.org |
| 67 | 344 | Observation | `Observation.valueCodeableConcept.coding` | LA6723-6 | Good color in body with bluish hands or feet | http://loinc.org |
| 68 | 345 | Observation | `Observation.valueCodeableConcept.coding` | LA6722-8 | The baby's whole body is completely bluish-gray or pale | http://loinc.org |
| 69 | 346 | Observation | `Observation.valueCodeableConcept.coding` | 276654001 | Congenital malformation | http://snomed.info/sct |
| 70 | 347 | Observation | `Observation.valueCodeableConcept.coding` | 419099009 | Dead | http://snomed.info/sct |
| 71 | 358 | Observation | `Observation.code.coding` | 76516-4 | Gestational age—​at birth | http://loinc.org |
| 72 | 370 | Observation | `Observation.code.coding` | 63963-3 | Date of end of pregnancy | http://loinc.org |
| 73 | 381 | Observation | `Observation.code.coding` | 310506006 | Reason for termination of pregnancy | http://snomed.info/sct |
| 74 | 393 | Procedure | `Procedure.code.coding` | 69.0 | Dilation and curettage of uterus | http://hl7.org/fhir/sid/icd-9-cm |
| 75 | 404 | Observation | `Observation.code.coding` | 82810-3 | Pregnancy status | http://loinc.org |
| 76 | 405 | Observation | `Observation.valueCodeableConcept.coding` | LA15173-0 | Pregnant | http://loinc.org |
| 77 | 406 | Observation | `Observation.valueCodeableConcept.coding` | LA26683-5 | Not pregnant | http://loinc.org |
| 78 | 415 | Observation | `Observation.code.coding` | 81956-5 | Date and time of death [TimeStamp] | http://loinc.org |
| 79 | 426 | Observation | `Observation.code.coding` | LT000005 | Alamat Mati | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 80 | 437 | Observation | `Observation.code.coding` | 79378-6 | Cause of death | http://loinc.org |
| 81 | 448 | Observation | `Observation.code.coding` | OC000026 | Masa terjadi Kematian Ibu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 82 | 449 | Observation | `Observation.valueCodeableConcept` | 1156679005 | Maternal antenatal period | http://snomed.info/sct |
| 83 | 450 | Observation | `Observation.valueCodeableConcept` | 1156682000 | Maternal intrapartum period | http://snomed.info/sct |
| 84 | 451 | Observation | `Observation.valueCodeableConcept` | 255410009 | Maternal postpartum | http://snomed.info/sct |
| 85 | 461 | Observation | `Observation.code.coding` | 81956-5 | Date and time of death [TimeStamp] | http://loinc.org |
| 86 | 472 | Observation | `Observation.code.coding` | LT000005 | Alamat Mati | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 87 | 483 | Observation | `Observation.code.coding` | 79378-6 | Cause of death | http://loinc.org |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://loinc.org | 38 |
| http://snomed.info/sct | 36 |
| http://terminology.kemkes.go.id/sp | 3 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 2 |
| http://terminology.kemkes.go.id/CodeSystem/organization-type | 2 |
| http://terminology.kemkes.go.id/CodeSystem/location-type | 2 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 1 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 1 |
| hhttp://terminology.kemkes.go.id/CodeSystem/organization-type | 1 |
| http://hl7.org/fhir/sid/icd-9-cm | 1 |
| **Total** | **87** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
