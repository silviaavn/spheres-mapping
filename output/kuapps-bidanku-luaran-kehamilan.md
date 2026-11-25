# Output Form: KuApps BidanKu - Luaran Kehamilan (tanpa baris tracker)

Sumber: `mapping/phdt-data-dictionary-kuapps-bidanku-luaran-kehamilan.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-kuapps-bidanku-luaran-kehamilan.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 31 |
| Code (`jumlah code` = 1) | 146 |
| Code unik (code + CodeSystem) | 104 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 5 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 4–18 | EpisodeOfCare | ANC | Antenatal Care | _Episode of Care ANC_ → `EpisodeOfCare.identifer` (4, tanpa BQ) |
| 2 | 19–32 | Encounter | – | – | – |
| 3 | 33–56 | Observation | 63893-2 | Outcome of pregnancy | _Apa alasan kehamilan selesai?_ → `Observation.valueCodeableConcept.coding` (36, tanpa BQ) |
| 4 | 57–69 | Observation | 405195003 | Intrapartum maternal status | _Keadaan Ibu_ → `Observation.valueCodeableConcept.coding` (60, tanpa BQ) |
| 5 | 70–82 | Observation | 93857-1 | Date and time of obstetric delivery | _Taksiran Persalinan_ → `Observation.valueDateTime` (75, tanpa BQ) |
| 6 | 83–93 | Observation | 93857-1 | Date and time of obstetric delivery | _Tanggal dan Jam Persalinan_ → `Observation.valueDateTime` (86, tanpa BQ) |
| 7 | 94–116 | Observation | 72150-6 | Delivery location | _Tempat persalinan_ → `Observation.valueCodeableConcept.coding` (97, tanpa BQ)<br>_Alamat Bersalin_ → `Observation.note.text` (116, tanpa BQ) |
| 8 | 117–132 | Observation | OC000013 | Penolong Persalinan | _Penolong Persalinan_ → `Observation.valueCodeableConcept.coding` (120, tanpa BQ)<br>_Nama Penolong Persalinan_ → `Observation.valueCodeableConcept.text` (125, tanpa BQ) |
| 9 | 133–147 | Observation | 76516-4 | Gestational age—​at birth | _Usia Kehamilan/ Gestasi pada saat Persalinan_ → `Observation.valueQuantity.value` (136, tanpa BQ)<br>_[Minggu]_ → `Observation.valueQuantity.code` (137, tanpa BQ)<br>_[Hari]_ → `Observation.component.valueQuantity.code` (140, tanpa BQ) |
| 10 | 148–158 | Observation | 11977-6 | [#] Parity | _Partus (P)_ → `Observation.valueInteger` (151, tanpa BQ) |
| 11 | 159–169 | Observation | 69043-8 | Other pregnancy outcomes # | _Abortus (A)_ → `Observation.valueInteger` (162, tanpa BQ) |
| 12 | 170–182 | Observation | 246435002 | Number of fetuses | _Jumlah Janin_ → `Observation.valueCodeableConcept.coding` (173, tanpa BQ) |
| 13 | 183–193 | Observation | 11636-8 | [#] Births.live | _Jumlah anak lahir hidup (pada kehamilan saat ini)_ → `Observation.valueInteger` (186, tanpa BQ) |
| 14 | 194–207 | Observation | 57071-3 | Obstetric delivery method | _Cara Persalinan_ → `Observation.valueCodeableConcept.coding` (197, tanpa BQ) |
| 15 | 208–230 | Condition | 38010008 | Intrapartum hemorrhage | _Komplikasi Persalinan_ → `Condition.clinicalStatus.coding` (208, tanpa BQ) |
| 16 | 231–240 | Procedure | 431868002 | Initiation of breastfeeding | _Inisiasi Menyusui Dini_ → `Procedure.category.coding` (231, tanpa BQ) |
| 17 | 241–252 | Observation | OC000016 | Waktu Inisiasi Menyusui Dini | _Jika Ya, Waktu Inisiasi Menyusui Dini_ → `Observation.valueCodeableConcept.coding` (244, tanpa BQ) |
| 18 | 253–272 | ServiceRequest | 409014006 | Delivery care management | _Rujukan_ → `ServiceRequest.status` (253, tanpa BQ)<br>_Faskes Rujukan_ → `ServiceRequest.locationCode.coding` (265, tanpa BQ)<br>_Nama Faskes Rujukan_ → `ServiceRequest.locationCode.text` (272, tanpa BQ) |
| 19 | 274–285 | Observation | SP000724 | Tanggal Abortus | _Tanggal waktu abortus_ → `Observation.valueDateTime` (277, tanpa BQ)<br>_Penyebab abortus_ → `Observation.performer.display` (285, tanpa BQ) |
| 20 | 286–307 | Observation | SP000890 | Penyebab abortus | _Sebutkan alasan lainnya_ → `Observation.note` (300, tanpa BQ) |
| 21 | 308–317 | Procedure | LA33555-6 | Dilation of cervix uteri and curettage for termination of pregnancy | _Kuretase?_ → `Procedure.category.coding` (308, tanpa BQ) |
| 22 | 318–339 | Observation | SP000515 | Tempat kuretase | _Tempat kuretase_ → `Observation.valueCodeableConcept.coding` (321, tanpa BQ)<br>_Nama fasilitas kesehatan tempat kuretase_ → `Observation.note` (339, tanpa BQ) |
| 23 | 341–351 | Observation | 81956-5 | Date and time of death [TimeStamp] | _Tanggal dan Jam bayi meninggal_ → `Observation.valueDateTime` (344, tanpa BQ) |
| 24 | 352–373 | Observation | OC000028 | Jenis Tempat Meninggal | _Tempat bayi meninggal_ → `Observation.valueCodeableConcept.coding` (355, tanpa BQ)<br>_Nama Fasilitas Bayi Meninggal_ → `Observation.note` (366, tanpa BQ) |
| 25 | 374–398 | Observation | 57062-2 | [#] Births.stillborn | _Jumlah anak lahir mati (pada kehamilan saat ini)_ → `Observation.valueInteger` (377, tanpa BQ)<br>_Penyebab kematian_ → `Observation.component.code.coding` (385, tanpa BQ) |
| 26 | 399–411 | Observation | 64710-7 | Was your pregnancy a live birth, stillbirth, miscarriage, abortion, or ectopic pregnancy [PhenX] | _Masa terjadi kematian bayi_ → `Observation.status` (399, tanpa BQ) |
| 27 | 413–423 | Observation | 81956-5 | Date and time of death [TimeStamp] | _Tanggal dan Jam Meninggal_ → `Observation.valueDateTime` (416, tanpa BQ) |
| 28 | 424–445 | Observation | OC000028 | Jenis Tempat Meninggal | _Tempat ibu Meninggal_ → `Observation.valueCodeableConcept.coding` (427, tanpa BQ)<br>_Nama Fasilitas Ibu Meninggal_ → `Observation.note` (438, tanpa BQ) |
| 29 | 446–457 | Observation | 39016-1 | Age at death | _Umur Ibu Saat Meninggal_ → `Observation.valueQuantity.value` (449, tanpa BQ) |
| 30 | 458–478 | Observation | 79378-6 | Cause of death | _Diagnosa Penyebab Kematian_ → `Observation.valueCodeableConcept.coding` (461, tanpa BQ) |
| 31 | 479–492 | Observation | OC000026 | Date and time of death [TimeStamp] | _Masa terjadi kematian Ibu_ → `Observation.valueCodeableConcept.coding` (483, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 25 |
| Procedure | 2 |
| EpisodeOfCare | 1 |
| Encounter | 1 |
| Condition | 1 |
| ServiceRequest | 1 |
| **Total** | **31** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 12 | EpisodeOfCare | `EpisodeOfCare.type.coding` | ANC | Antenatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 2 | 35 | Observation | `Observation.code.coding` | 63893-2 | Outcome of pregnancy | http://loinc.org |
| 3 | 36 | Observation | `Observation.valueCodeableConcept.coding` | LA14270-5 | Live birth | http://loinc.org |
| 4 | 37 | Observation | `Observation.valueCodeableConcept.coding` | LA14271-3 | Stillborn | http://loinc.org |
| 5 | 38 | Observation | `Observation.valueCodeableConcept.coding` | LA14272-1 | Miscarriage | http://loinc.org |
| 6 | 39 | Observation | `Observation.valueCodeableConcept.coding` | LA14273-9 | Induced abortion | http://loinc.org |
| 7 | 59 | Observation | `Observation.code.coding` | 405195003 | Intrapartum maternal status | http://snomed.info/sct |
| 8 | 60 | Observation | `Observation.valueCodeableConcept.coding` | 102514002 | Well female adult | http://snomed.info/sct |
| 9 | 61 | Observation | `Observation.valueCodeableConcept.coding` | 59283008 | Maternal death | http://snomed.info/sct |
| 10 | 62 | Observation | `Observation.valueCodeableConcept.coding` | 39104002 | Illness | http://snomed.info/sct |
| 11 | 72 | Observation | `Observation.code.coding` | 93857-1 | Date and time of obstetric delivery | http://loinc.org |
| 12 | 73 | Observation | `Observation.code.coding` | 11778-8 | Delivery date Estimated | http://loinc.org |
| 13 | 74 | Observation | `Observation.code.coding` | ANC.B6.DE22 | Expected date of delivery (EDD) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 14 | 85 | Observation | `Observation.code.coding` | 93857-1 | Date and time of obstetric delivery | http://loinc.org |
| 15 | 96 | Observation | `Observation.code.coding` | 72150-6 | Delivery location | http://loinc.org |
| 16 | 97 | Observation | `Observation.valueCodeableConcept.coding` | 264362003 | Home | http://snomed.info/sct |
| 17 | 98 | Observation | `Observation.valueCodeableConcept.coding` | OT000001 | Polindes | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 18 | 99 | Observation | `Observation.valueCodeableConcept.coding` | OT000002 | Pustu | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 19 | 100 | Observation | `Observation.valueCodeableConcept.coding` | 102 | Pusat Kesehatan Masyarakat | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 20 | 101 | Observation | `Observation.valueCodeableConcept.coding` | 103 | Klinik | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 21 | 102 | Observation | `Observation.valueCodeableConcept.coding` | OT000008 | Rumah Bersalin | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 22 | 103 | Observation | `Observation.valueCodeableConcept.coding` | 82242000 | Children’s hospital | http://snomed.info/sct |
| 23 | 104 | Observation | `Observation.valueCodeableConcept.coding` | 104 | Rumah Sakit | hhttp://terminology.kemkes.go.id/CodeSystem/organization-type |
| 24 | 105 | Observation | `Observation.valueCodeableConcept.coding` | OT000004 | Bidan Praktek Mandiri | hhttp://terminology.kemkes.go.id/CodeSystem/organization-type |
| 25 | 106 | Observation | `Observation.valueCodeableConcept.coding` | LT000008 | Dalam perjalanan dari rumah/masyarakat | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 26 | 107 | Observation | `Observation.valueCodeableConcept.coding` | LT000009 | Dalam perjalanan ke faskes lain | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 27 | 108 | Observation | `Observation.valueCodeableConcept.coding` | LT000007 | Rumah Dukun | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 28 | 119 | Observation | `Observation.code.coding` | OC000013 | Penolong Persalinan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 29 | 120 | Observation | `Observation.valueCodeableConcept.coding` | 303071001 | Person in the family | http://snomed.info/sct |
| 30 | 121 | Observation | `Observation.valueCodeableConcept.coding` | OV000012 | Dukun | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 31 | 122 | Observation | `Observation.valueCodeableConcept.coding` | 309453006 | Registered midwife | http://snomed.info/sct |
| 32 | 123 | Observation | `Observation.valueCodeableConcept.coding` | 309343006 | Physician | http://snomed.info/sct |
| 33 | 124 | Observation | `Observation.valueCodeableConcept.coding` | 11935004 | Obstetrician | http://snomed.info/sct |
| 34 | 135 | Observation | `Observation.code.coding` | 76516-4 | Gestational age—​at birth | http://loinc.org |
| 35 | 138 | Observation | `Observation.component.code.coding` | SP000398 | Usia Kehamilan Saat Persalinan (hari) | http://terminology.kemkes.go.id/sp |
| 36 | 150 | Observation | `Observation.code.coding` | 11977-6 | [#] Parity | http://loinc.org |
| 37 | 161 | Observation | `Observation.code.coding` | 69043-8 | Other pregnancy outcomes # | http://loinc.org |
| 38 | 172 | Observation | `Observation.code.coding` | 246435002 | Number of fetuses | http://snomed.info/sct |
| 39 | 173 | Observation | `Observation.valueCodeableConcept.coding` | 1290152008 | Singleton pregnancy | http://snomed.info/sct |
| 40 | 174 | Observation | `Observation.valueCodeableConcept.coding` | 65147003 | Twin pregnancy | http://snomed.info/sct |
| 41 | 175 | Observation | `Observation.valueCodeableConcept.coding` | 64254006 | Triplet pregnancy | http://snomed.info/sct |
| 42 | 185 | Observation | `Observation.code.coding` | 11636-8 | [#] Births.live | http://loinc.org |
| 43 | 196 | Observation | `Observation.code.coding` | 57071-3 | Obstetric delivery method | http://loinc.org |
| 44 | 197 | Observation | `Observation.valueCodeableConcept.coding` | 48782003 | Delivery normal | http://snomed.info/sct |
| 45 | 198 | Observation | `Observation.valueCodeableConcept.coding` | 200144004 | Deliveries by cesarean | http://snomed.info/sct |
| 46 | 199 | Observation | `Observation.valueCodeableConcept.coding` | 200138003 | Vacuum extractor delivery - delivered | http://snomed.info/sct |
| 47 | 200 | Observation | `Observation.valueCodeableConcept.coding` | 200130005 | Forceps delivery - delivered | http://snomed.info/sct |
| 48 | 210 | Condition | `Condition.code.coding` | 38010008 | Intrapartum hemorrhage | http://snomed.info/sct |
| 49 | 211 | Condition | `Condition.code.coding` | 36813001 | Placenta previa | http://snomed.info/sct |
| 50 | 212 | Condition | `Condition.code.coding` | 415105001 | Placental abruption | http://snomed.info/sct |
| 51 | 213 | Condition | `Condition.code.coding` | 270500004 | Prolapsed cord | http://snomed.info/sct |
| 52 | 214 | Condition | `Condition.code.coding` | 199746004 | Obstructed labor | http://snomed.info/sct |
| 53 | 215 | Condition | `Condition.code.coding` | 15028002 | Abnormal fetal presentation | http://snomed.info/sct |
| 54 | 216 | Condition | `Condition.code.coding` | 6096002 | Breech presentation | http://snomed.info/sct |
| 55 | 217 | Condition | `Condition.code.coding` | 398254007 | Pre-eclampsia | http://snomed.info/sct |
| 56 | 218 | Condition | `Condition.code.coding` | 15938005 | Eclampsia | http://snomed.info/sct |
| 57 | 219 | Condition | `Condition.code.coding` | 283380005 | Laceration of perineum | http://snomed.info/sct |
| 58 | 220 | Condition | `Condition.code.coding` | 199745000 | Complication occurring during labor and delivery | http://snomed.info/sct |
| 59 | 221 | Condition | `Condition.code.coding` | 48194001 | Pregnancy-induced hypertension | http://snomed.info/sct |
| 60 | 222 | Condition | `Condition.code.coding` | 40733004 | Infectious disease | http://snomed.info/sct |
| 61 | 223 | Condition | `Condition.code.coding` | 386639001 | Termination of pregnancy | http://snomed.info/sct |
| 62 | 224 | Condition | `Condition.code.coding` | 44223004 | Premature rupture of membranes | http://snomed.info/sct |
| 63 | 225 | Condition | `Condition.code.coding` | 9293002 | Atony of uterus | http://snomed.info/sct |
| 64 | 232 | Procedure | `Procedure.code.coding` | 431868002 | Initiation of breastfeeding | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 65 | 243 | Observation | `Observation.code.coding` | OC000016 | Waktu Inisiasi Menyusui Dini | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 66 | 244 | Observation | `Observation.valueCodeableConcept.coding` | OV000014 | Kurang dari 1 jam | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 67 | 245 | Observation | `Observation.valueCodeableConcept.coding` | OV000015 | Lebih dari 1 jam | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 68 | 257 | ServiceRequest | `ServiceRequest.code.coding` | 409014006 | Delivery care management | http://snomed.info/sct |
| 69 | 276 | Observation | `Observation.code.coding` | SP000724 | Tanggal Abortus | http://terminology.kemkes.go.id/sp |
| 70 | 288 | Observation | `Observation.code.coding` | SP000890 | Penyebab abortus | http://terminology.kemkes.go.id/sp |
| 71 | 289 | Observation | `Observation.valueCodeableConcept.coding` | 66091009 | Congenital disease | http://snomed.info/sct |
| 72 | 290 | Observation | `Observation.valueCodeableConcept.coding` | 70591005 | Fetal disorder | http://snomed.info/sct |
| 73 | 291 | Observation | `Observation.valueCodeableConcept.coding` | 40733004 | Infectious disease | http://snomed.info/sct |
| 74 | 292 | Observation | `Observation.valueCodeableConcept.coding` | 17382005 | Cervical incompetence | http://snomed.info/sct |
| 75 | 293 | Observation | `Observation.valueCodeableConcept.coding` | 37849005 | Congenital uterine anomaly | http://snomed.info/sct |
| 76 | 294 | Observation | `Observation.valueCodeableConcept.coding` | 417746004 | Traumatic injury | http://snomed.info/sct |
| 77 | 295 | Observation | `Observation.valueCodeableConcept.coding` | 34801009 | Ectopic pregnancy | http://snomed.info/sct |
| 78 | 296 | Observation | `Observation.valueCodeableConcept.coding` | 417044008 | Hydatidiform mole, benign | http://snomed.info/sct |
| 79 | 297 | Observation | `Observation.valueCodeableConcept.coding` | 35999006 | Blighted ovum | http://snomed.info/sct |
| 80 | 298 | Observation | `Observation.valueCodeableConcept.coding` | 261665006 | Unknown | http://snomed.info/sct |
| 81 | 299 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 82 | 309 | Procedure | `Procedure.code.coding` | LA33555-6 | Dilation of cervix uteri and curettage for termination of pregnancy | http://loinc.org |
| 83 | 320 | Observation | `Observation.code.coding` | SP000515 | Tempat kuretase | http://terminology.kemkes.go.id/sp |
| 84 | 321 | Observation | `Observation.valueCodeableConcept.coding` | 264362003 | Home | http://snomed.info/sct |
| 85 | 322 | Observation | `Observation.valueCodeableConcept.coding` | OT000001 | Polindes | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 86 | 323 | Observation | `Observation.valueCodeableConcept.coding` | OT000002 | Pustu | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 87 | 324 | Observation | `Observation.valueCodeableConcept.coding` | 102 | Pusat Kesehatan Masyarakat | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 88 | 325 | Observation | `Observation.valueCodeableConcept.coding` | 103 | Klinik | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 89 | 326 | Observation | `Observation.valueCodeableConcept.coding` | OT000008 | Rumah Bersalin | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 90 | 327 | Observation | `Observation.valueCodeableConcept.coding` | 104 | Rumah Sakit | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 91 | 328 | Observation | `Observation.valueCodeableConcept.coding` | OT000004 | Bidan Praktek Mandiri | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 92 | 329 | Observation | `Observation.valueCodeableConcept.coding` | LT000008 | Dalam perjalanan dari rumah/masyarakat | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 93 | 330 | Observation | `Observation.valueCodeableConcept.coding` | LT000009 | Dalam perjalanan ke faskes lain | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 94 | 331 | Observation | `Observation.valueCodeableConcept.coding` | LT000007 | Rumah Dukun | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 95 | 343 | Observation | `Observation.code.coding` | 81956-5 | Date and time of death [TimeStamp] | http://loinc.org |
| 96 | 354 | Observation | `Observation.code.coding` | OC000028 | Jenis Tempat Meninggal | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 97 | 355 | Observation | `Observation.valueCodeableConcept.coding` | 264362003 | Home | http://snomed.info/sct |
| 98 | 356 | Observation | `Observation.valueCodeableConcept.coding` | OT000001 | Polindes | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 99 | 357 | Observation | `Observation.valueCodeableConcept.coding` | OT000002 | Pustu | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 100 | 358 | Observation | `Observation.valueCodeableConcept.coding` | 102 | Pusat Kesehatan Masyarakat | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 101 | 359 | Observation | `Observation.valueCodeableConcept.coding` | 103 | Klinik | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 102 | 360 | Observation | `Observation.valueCodeableConcept.coding` | OT000008 | Rumah Bersalin | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 103 | 361 | Observation | `Observation.valueCodeableConcept.coding` | 104 | Rumah Sakit | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 104 | 362 | Observation | `Observation.valueCodeableConcept.coding` | OT000004 | Bidan Praktek Mandiri | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 105 | 363 | Observation | `Observation.valueCodeableConcept.coding` | LT000008 | Dalam perjalanan dari rumah/masyarakat | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 106 | 364 | Observation | `Observation.valueCodeableConcept.coding` | LT000009 | Dalam perjalanan ke faskes lain | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 107 | 365 | Observation | `Observation.valueCodeableConcept.coding` | LT000007 | Rumah Dukun | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 108 | 376 | Observation | `Observation.code.coding` | 57062-2 | [#] Births.stillborn | http://loinc.org |
| 109 | 385 | Observation | `Observation.component.code.coding` | TK000019 | Kode group | http://terminology.kemkes.go.id |
| 110 | 386 | Observation | `Observation.component.valueCodeableConcept.coding` | N | Neonatal death | http://terminology.kemkes.go.id/CodeSystem/icd-10-pm |
| 111 | 387 | Observation | `Observation.component.code.coding` | TK000020 | Kode subgroup | http://terminology.kemkes.go.id |
| 112 | 388 | Observation | `Observation.component.valueCodeableConcept.coding` | P07 | Disorders related to short gestation and low birth weight, not elsewhere classified | http://terminology.kemkes.go.id/CodeSystem/icd-10-pm |
| 113 | 389 | Observation | `Observation.component.valueCodeableConcept.coding` | P21 | Birth asphyxia | http://terminology.kemkes.go.id/CodeSystem/icd-10-pm |
| 114 | 390 | Observation | `Observation.component.valueCodeableConcept.coding` | N6 | Infection | http://terminology.kemkes.go.id/CodeSystem/icd-10-pm |
| 115 | 391 | Observation | `Observation.component.valueCodeableConcept.coding` | N1 | Congenital malformations, deformations and chromosomal abnormalities | http://terminology.kemkes.go.id/CodeSystem/icd-10-pm |
| 116 | 401 | Observation | `Observation.code.coding` | 64710-7 | Was your pregnancy a live birth, stillbirth, miscarriage, abortion, or ectopic pregnancy [PhenX] | http://loinc.org |
| 117 | 415 | Observation | `Observation.code.coding` | 81956-5 | Date and time of death [TimeStamp] | http://loinc.org |
| 118 | 426 | Observation | `Observation.code.coding` | OC000028 | Jenis Tempat Meninggal | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 119 | 427 | Observation | `Observation.valueCodeableConcept.coding` | 264362003 | Home | http://snomed.info/sct |
| 120 | 428 | Observation | `Observation.valueCodeableConcept.coding` | OT000001 | Polindes | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 121 | 429 | Observation | `Observation.valueCodeableConcept.coding` | OT000002 | Pustu | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 122 | 430 | Observation | `Observation.valueCodeableConcept.coding` | 102 | Pusat Kesehatan Masyarakat | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 123 | 431 | Observation | `Observation.valueCodeableConcept.coding` | 103 | Klinik | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 124 | 432 | Observation | `Observation.valueCodeableConcept.coding` | OT000008 | Rumah Bersalin | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 125 | 433 | Observation | `Observation.valueCodeableConcept.coding` | 104 | Rumah Sakit | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 126 | 434 | Observation | `Observation.valueCodeableConcept.coding` | OT000004 | Bidan Praktek Mandiri | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 127 | 435 | Observation | `Observation.valueCodeableConcept.coding` | LT000008 | Dalam perjalanan dari rumah/masyarakat | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 128 | 436 | Observation | `Observation.valueCodeableConcept.coding` | LT000009 | Dalam perjalanan ke faskes lain | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 129 | 437 | Observation | `Observation.valueCodeableConcept.coding` | LT000007 | Rumah Dukun | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 130 | 448 | Observation | `Observation.code.coding` | 39016-1 | Age at death | http://loinc.org |
| 131 | 460 | Observation | `Observation.code.coding` | 79378-6 | Cause of death | http://loinc.org |
| 132 | 461 | Observation | `Observation.valueCodeableConcept.coding` | SP000460 | Komplikasi terkait aborsi | http://terminology.kemkes.go.id/sp |
| 133 | 462 | Observation | `Observation.valueCodeableConcept.coding` | 199746004 | Obstructed labor | http://snomed.info/sct |
| 134 | 463 | Observation | `Observation.valueCodeableConcept.coding` | 398254007 | Pre-eclampsia | http://snomed.info/sct |
| 135 | 464 | Observation | `Observation.valueCodeableConcept.coding` | 15938005 | Eclampsia | http://snomed.info/sct |
| 136 | 465 | Observation | `Observation.valueCodeableConcept.coding` | 131148009 | Bleeding | http://snomed.info/sct |
| 137 | 466 | Observation | `Observation.valueCodeableConcept.coding` | 415105001 | Placental abruption | http://snomed.info/sct |
| 138 | 467 | Observation | `Observation.valueCodeableConcept.coding` | 36813001 | Placenta previa | http://snomed.info/sct |
| 139 | 468 | Observation | `Observation.valueCodeableConcept.coding` | 34430009 | Rupture of uterus | http://snomed.info/sct |
| 140 | 469 | Observation | `Observation.valueCodeableConcept.coding` | 91302008 | Sepsis | http://snomed.info/sct |
| 141 | 470 | Observation | `Observation.valueCodeableConcept.coding` | 40733004 | Infectious disease | http://snomed.info/sct |
| 142 | 471 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 143 | 481 | Observation | `Observation.code.coding` | OC000026 | Date and time of death [TimeStamp] | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 144 | 483 | Observation | `Observation.valueCodeableConcept.coding` | 1156679005 | Maternal antenatal period | http://snomed.info/sct |
| 145 | 484 | Observation | `Observation.valueCodeableConcept.coding` | 1156682000 | Maternal intrapartum period | http://snomed.info/sct |
| 146 | 485 | Observation | `Observation.valueCodeableConcept.coding` | 255410009 | Maternal postpartum | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 62 |
| http://terminology.kemkes.go.id/CodeSystem/organization-type | 26 |
| http://loinc.org | 21 |
| http://terminology.kemkes.go.id/CodeSystem/location-type | 12 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 9 |
| http://terminology.kemkes.go.id/sp | 5 |
| http://terminology.kemkes.go.id/CodeSystem/icd-10-pm | 5 |
| hhttp://terminology.kemkes.go.id/CodeSystem/organization-type | 2 |
| http://terminology.kemkes.go.id | 2 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 1 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 1 |
| **Total** | **146** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 2 | – | EoC ketika mendaftarkan luaran kehamilan dengan hasil apapun, maka sudah start untuk PNC | – | `` |
| 3 | – | EoC ANC Ibu ditutup | – | `` |
