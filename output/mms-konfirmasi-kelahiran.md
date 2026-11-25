# Output Form: MMS - Konfirmasi Kelahiran dan Luaran Kehamilan

Sumber: `mapping/phdt-data-dictionary-mms-konfirmasi-kelahiran.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-mms-konfirmasi-kelahiran.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 50 |
| Code (`jumlah code` = 1) | 193 |
| Code unik (code + CodeSystem) | 138 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 18 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–9 | PractitionerRole | – | – | _Siapa yang melakukan entry data?_ → `PractitionerRole.active` (2, tanpa BQ) |
| 2 | 10–13 | Practitioner | – | – | _Nama Kader yang melakukan entry data_ → `Practitioner.name.text` (10, tanpa BQ)<br>_ID SID Kader yang mengumpulkan form_ → `Practitioner.identifier` (11, tanpa BQ)<br>_ID SID staff yang melakukan entry data_ → `Practitioner.identifier` (12, tanpa BQ)<br>_ID SID field staff yang mengumpulkan form_ → `Practitioner.identifier` (13, tanpa BQ) |
| 3 | 16–19 | Patient | – | – | _Nomor SID Ibu_ → `Patient.identifier.value` (18, tanpa BQ)<br>_Nama Lengkap Ibu_ → `Patient.name.text` (19, tanpa BQ)<br>_Tulis Nomor Induk Kependudukan (NIK)_ → `Patient.identifier.use` (25, tanpa BQ)<br>_Tanggal lahir_ → `Patient.birthDate` (44, tanpa BQ)<br>_Asal kota/kabupaten tempat ibu melahirkan_ → `Patient.address.extension.url` (57, tanpa BQ)<br>_Nomor SID ID Bayi_ → `Patient.identifier.value` (341, tanpa BQ)<br>_Nama lengkap_ → `Patient.name.text` (342, tanpa BQ)<br>_Tulis Nomor Induk Kependudukan (NIK)_ → `Patient.identifier.use` (345, tanpa BQ)<br>_Tanggal lahir bayi_ → `Patient.birthDate` (386, tanpa BQ)<br>_Jenis kelamin bayi_ → `Patient.gender` (420, tanpa BQ) |
| 4 | 20–22 | RelatedPerson | – | – | _Nama Lengkap Suami_ → `RelatedPerson.patient.reference` (20, tanpa BQ) |
| 5 | 28–41 | Observation | SP000403 | Alasan Tidak Ada Nomor Induk Kependudukan | _Pilih alasan tidak mempunyai Nomor Induk Kependudukan (NIK)_ → `Observation.valueCodeableConcept.coding` (31, tanpa BQ) |
| 6 | 45–56 | Observation | 424144002.0 | Current chronological age | _Usia_ → `Observation.valueQuantity.value` (48, tanpa BQ) |
| 7 | 60–75 | Observation | SP000502 | Alasan kehamilan selesai | _Alasan kehamilan selesai?_ → `Observation.valueCodeableConcept.coding` (63, tanpa BQ) |
| 8 | 76–88 | Observation | OC000013 | Penolong Persalinan | _Penolong Persalinan_ → `Observation.valueCodeableConcept.coding` (79, tanpa BQ) |
| 9 | 89–99 | Observation | 93857-1 | Date and time of obstetric delivery | _Tanggal Melahirkan_ → `Observation.valueDateTime` (92, tanpa BQ) |
| 10 | 100–112 | Observation | 57722-1 | Birth plurality of Pregnancy | _Jumlah Janin_ → `Observation.valueCodeableConcept.coding` (103, tanpa BQ) |
| 11 | 113–126 | Observation | 272058002.0 | Past pregnancy history of delivery procedure | _Metode persalinan_ → `Observation.valueCodeableConcept.coding` (116, tanpa BQ) |
| 12 | 127–137 | Observation | 432678004.0 | Indication for procedure | _Indikasi persalinan_ → `Observation.valueString` (130, tanpa BQ) |
| 13 | 138–151 | Observation | 249197004.0 | Postpartum condition of mother | _Bagaimana keadaan Ibu setelah persalinan/luaran kehamilan?_ → `Observation.valueCodeableConcept.coding` (141, tanpa BQ) |
| 14 | 152–163 | Observation | 8665-2 | Last menstrual period start date | _HPHT (Hari Pertama Haid Terakhir)_ → `Observation.valueDateTime` (156, tanpa BQ) |
| 15 | 164–175 | Observation | 11778-8 | Delivery date Estimated | _HPL menurut HPHT_ → `Observation.valueDateTime` (168, tanpa BQ) |
| 16 | 176–187 | Observation | 11781-2 | Delivery date US composite estimate | _HPL menurut USG_ → `Observation.valueDateTime` (180, tanpa BQ) |
| 17 | 188–199 | Condition | 398254007.0 | Pre-eclampsia | _Apakah Ibu memiliki kondisi medis tertentu?_ → `Condition.clinicalStatus.coding` (188, tanpa BQ)<br>_Kondisi apa?_ → `Condition.note` (194, tanpa BQ) |
| 18 | 200–218 | Observation | PC000004 | KB Pasca Persalinan | _Metode kontrasepsi yang digunakan_ → `Observation.valueCodeableConcept.coding` (203, tanpa BQ) |
| 19 | 219–228 | Observation | 81954-0 | Date of death [Date] | _Tanggal Ibu meninggal_ → `Observation.valueDateTime` (222, tanpa BQ) |
| 20 | 229–238 | Observation | 81955-7 | Time of death [ClockTime] | _Waktu ibu meninggal_ → `Observation.valueDateTime` (232, tanpa BQ) |
| 21 | 239–260 | Observation | OC000028 | Jenis Tempat Meninggal | _Tempat Ibu meninggal_ → `Observation.valueCodeableConcept.coding` (242, tanpa BQ) |
| 22 | 261–273 | Composition | – | – | _Nama fasilitas kesehatan tempat ibu meninggal_ → `Composition.contained.resourceType` (261, tanpa BQ) |
| 23 | 275–286 | Observation | 39016-1 | Age at death | _Umur saat Meninggal_ → `Observation.valueQuantity.value` (278, tanpa BQ) |
| 24 | 287–326 | Observation | 79378-6 | Cause of death | _Penyebab kematian Ibu_ → `Observation.component.valueCodeableConcept.coding` (291, tanpa BQ)<br>_Penyebab kematian lainnya_ → `Observation.component.valueString` (319, tanpa BQ) |
| 25 | 327–340 | Observation | OC000026 | Date and time of death [TimeStamp] | _Masa terjadi kematian Ibu_ → `Observation.valueCodeableConcept.coding` (331, tanpa BQ) |
| 26 | 348–361 | Observation | SP000403 | Alasan Tidak Ada Nomor Induk Kependudukan | _Pilih alasan tidak mempunyai Nomor Induk Kependudukan (NIK)_ → `Observation.valueCodeableConcept.coding` (351, tanpa BQ) |
| 27 | 362–374 | Observation | 249222005.0 | Neonatal condition | _Bagaimana keadaan Bayi setelah persalinan?_ → `Observation.valueCodeableConcept.coding` (365, tanpa BQ) |
| 28 | 375–385 | Observation | 76516-4 | Gestational age—​at birth | _Usia kehamilan saat lahir berapa minggu?_ → `Observation.valueQuantity.value` (378, tanpa BQ) |
| 29 | 387–396 | Observation | 57715-5 | Birth time | _Waktu lahir bayi_ → `Observation.valueTime` (390, tanpa BQ) |
| 30 | 397–418 | Observation | 72150-6 | Delivery location | _Tempat lahir bayi_ → `Observation.valueCodeableConcept.coding` (400, tanpa BQ) |
| 31 | 423–434 | Observation | 8339-4 | Birth weight Measured | _Berat badan bayi lahir_ → `Observation.valueQuantity.value` (426, tanpa BQ) |
| 32 | 435–446 | Observation | 89269-5 | Body height Measured --at birth | _Panjang badan bayi lahir_ → `Observation.valueQuantity.value` (438, tanpa BQ) |
| 33 | 447–458 | Observation | 8290-9 | Head Occipital-frontal circumference --at birth- by Tape measure | _Lingkar Kepala bayi lahir_ → `Observation.valueQuantity.value` (450, tanpa BQ) |
| 34 | 459–475 | Observation | 249222005.0 | Neonatal condition | _Kondisi bayi saat lahir_ → `Observation.valueCodeableConcept.coding` (462, tanpa BQ) |
| 35 | 477–484 | Condition | 386639001.0 | Termination of pregnancy | _Tanggal abortus dan Waktu abortus_ → `Condition.onsetDateTime` (484, tanpa BQ) |
| 36 | 485–499 | Observation | 18185-9 | Gestational age | _Usia kehamilan (UK) - minggu_ → `Observation.valueQuantity.value` (489, tanpa BQ)<br>_Usia kehamilan (UK) - hari_ → `Observation.component.code.coding` (491, tanpa BQ) |
| 37 | 500–510 | Observation | – | – | _Penyebab abortus_ → `Observation.valueString` (503, tanpa BQ) |
| 38 | 511–522 | Observation | 68688001.0 | Curettage | _Kuretase?_ → `Observation.valueBoolean` (514, tanpa BQ) |
| 39 | 523–538 | Observation | SP000515 | Tempat kuretase | _Tempat kuretase_ → `Observation.valueCodeableConcept.coding` (526, tanpa BQ) |
| 40 | 540–551 | Observation | 82810-3 | Pregnancy status | _Apakah saat ini sudah dalam kondisi hamil kembali?_ → `Observation.valueCodeableConcept.coding` (543, tanpa BQ) |
| 41 | 552–562 | Observation | 81954-0 | Date of death [Date] | _Tanggal bayi meninggal_ → `Observation.valueDateTime` (555, tanpa BQ) |
| 42 | 563–573 | Observation | 81955-7 | Time of death [ClockTime] | _Waktu bayi meninggal_ → `Observation.valueTime` (566, tanpa BQ) |
| 43 | 574–595 | Observation | OC000028 | Jenis Tempat Meninggal | _Tempat bayi meninggal_ → `Observation.valueCodeableConcept.coding` (577, tanpa BQ) |
| 44 | 596–601 | Composition | – | – | _Nama fasilitas kesehatan tempat bayi meninggal_ → `Composition.contained.location.type.coding` (596, tanpa BQ) |
| 45 | 603–644 | Observation | 79378-6 | Cause of death | _Penyebab kematian bayi_ → `Observation.component.valueCodeableConcept.coding` (607, tanpa BQ)<br>_Penyebab kematian lainnya_ → `Observation.component.valueString` (637, tanpa BQ) |
| 46 | 645–657 | Observation | 64710-7 | Was your pregnancy a live birth, stillbirth, miscarriage, abortion, or ectopic pregnancy [PhenX] | _Masa terjadi kematian bayi_ → `Observation.valueCodeableConcept.coding` (648, tanpa BQ) |
| 47 | 658–669 | Observation | 52480-1 | Anthropometric Measures | _Apakah pengukuran antropometri oleh CHP dilakukan?_ → `Observation.valueCodeableConcept.coding` (661, tanpa BQ) |
| 48 | 670–681 | Observation | 29463-7 | Body weight | _Berat badan bayi_ → `Observation.valueQuantity.value` (673, tanpa BQ) |
| 49 | 682–693 | Observation | 8306-3 | Body height --lying | _Panjang badan bayi_ → `Observation.valueQuantity.value` (685, tanpa BQ) |
| 50 | 694–705 | Observation | 9843-4 | Head Occipital-frontal circumference | _Lingkar Kepala bayi_ → `Observation.valueQuantity.value` (697, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 42 |
| Condition | 2 |
| Composition | 2 |
| PractitionerRole | 1 |
| Practitioner | 1 |
| Patient | 1 |
| RelatedPerson | 1 |
| **Total** | **50** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 3 | PractitionerRole | `PractitionerRole.code` | SP000373 | Kader Kesehatan | http://terminology.kemkes.go.id/sp |
| 2 | 4 | PractitionerRole | `PractitionerRole.code` | 309453006.0 | Registered midwife | http://snomed.info/sct |
| 3 | 5 | PractitionerRole | `PractitionerRole.code.coding` | SP000397 | Field/call center staff | http://terminology.kemkes.go.id/sp |
| 4 | 6 | PractitionerRole | `PractitionerRole.code.coding` | SP000508 | Call Centre | http://terminology.kemkes.go.id/sp |
| 5 | 7 | PractitionerRole | `PractitionerRole.code.coding` | SP000509 | Operator | http://terminology.kemkes.go.id/sp |
| 6 | 8 | PractitionerRole | `PractitionerRole.code.coding` | SP000396 | Data entry staff | http://terminology.kemkes.go.id/sp |
| 7 | 30 | Observation | `Observation.code.coding` | SP000403 | Alasan Tidak Ada Nomor Induk Kependudukan | http://terminology.kemkes.go.id/sp |
| 8 | 31 | Observation | `Observation.valueCodeableConcept.coding` | SP000404 | Tidak Punya Kartu Tanda Penduduk | http://terminology.kemkes.go.id/sp |
| 9 | 32 | Observation | `Observation.valueCodeableConcept.coding` | SP000405 | Tidak Membawa Kartu Tanda Penduduk | http://terminology.kemkes.go.id/sp |
| 10 | 33 | Observation | `Observation.valueCodeableConcept.coding` | SP000406 | Kartu Tanda Penduduk Hilang | http://terminology.kemkes.go.id/sp |
| 11 | 34 | Observation | `Observation.valueCodeableConcept.coding` | 397644002.0 | Right to privacy maintained | http://snomed.info/sct |
| 12 | 47 | Observation | `Observation.code.coding` | 424144002.0 | Current chronological age | http://snomed.info/sct |
| 13 | 62 | Observation | `Observation.code.coding` | SP000502 | Alasan kehamilan selesai | http://terminology.kemkes.go.id/sp |
| 14 | 63 | Observation | `Observation.valueCodeableConcept.coding` | 281050002.0 | Livebirth | http://snomed.info/sct |
| 15 | 64 | Observation | `Observation.valueCodeableConcept.coding` | 386639001.0 | Termination of pregnancy | http://snomed.info/sct |
| 16 | 65 | Observation | `Observation.valueCodeableConcept.coding` | 237364002.0 | Stillbirth | http://snomed.info/sct |
| 17 | 66 | Observation | `Observation.valueCodeableConcept.coding` | 59283008.0 | Maternal death | http://snomed.info/sct |
| 18 | 67 | Observation | `Observation.valueCodeableConcept.coding` | 57797005.0 | Induced termination of pregnancy | http://snomed.info/sct |
| 19 | 68 | Observation | `Observation.valueCodeableConcept.coding` | 77386006.0 | Pregnancy | http://snomed.info/sct |
| 20 | 78 | Observation | `Observation.code.coding` | OC000013 | Penolong Persalinan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 21 | 79 | Observation | `Observation.valueCodeableConcept.coding` | 11935004.0 | Obstetrician Occupation | http://snomed.info/sct |
| 22 | 80 | Observation | `Observation.valueCodeableConcept.coding` | 309343006.0 | Physician Occupation | http://snomed.info/sct |
| 23 | 81 | Observation | `Observation.valueCodeableConcept.coding` | 309453006.0 | Registered midwife | http://snomed.info/sct |
| 24 | 91 | Observation | `Observation.code.coding` | 93857-1 | Date and time of obstetric delivery | http://loinc.org |
| 25 | 102 | Observation | `Observation.code.coding` | 57722-1 | Birth plurality of Pregnancy | http://loinc.org |
| 26 | 103 | Observation | `Observation.valueCodeableConcept.coding` | 237244005.0 | Single pregnancy | http://snomed.info/sct |
| 27 | 104 | Observation | `Observation.valueCodeableConcept.coding` | 65147003.0 | Twin pregnancy | http://snomed.info/sct |
| 28 | 105 | Observation | `Observation.valueCodeableConcept.coding` | 64254006.0 | Triplet pregnancy | http://snomed.info/sct |
| 29 | 115 | Observation | `Observation.code.coding` | 272058002.0 | Past pregnancy history of delivery procedure | http://snomed.info/sct |
| 30 | 116 | Observation | `Observation.valueCodeableConcept.coding` | 161805006.0 | Past pregnancy history of cesarean section | http://snomed.info/sct |
| 31 | 117 | Observation | `Observation.valueCodeableConcept.coding` | 726624001.0 | Past pregnancy history of previous delivery by vacuum extraction | http://snomed.info/sct |
| 32 | 118 | Observation | `Observation.valueCodeableConcept.coding` | 161813007.0 | Past pregnancy history of previous forceps delivery | http://snomed.info/sct |
| 33 | 119 | Observation | `Observation.valueCodeableConcept.coding` | 275568006.0 | Past pregnancy history of normal delivery | http://snomed.info/sct |
| 34 | 129 | Observation | `Observation.code.coding` | 432678004.0 | Indication for procedure | http://snomed.info/sct |
| 35 | 140 | Observation | `Observation.code.coding` | 249197004.0 | Postpartum condition of mother | http://snomed.info/sct |
| 36 | 141 | Observation | `Observation.valueCodeableConcept.coding` | 102514002.0 | Well female adult | http://snomed.info/sct |
| 37 | 142 | Observation | `Observation.valueCodeableConcept.coding` | 419620001.0 | Death | http://snomed.info/sct |
| 38 | 143 | Observation | `Observation.valueCodeableConcept.coding` | 39104002.0 | Illness | http://snomed.info/sct |
| 39 | 154 | Observation | `Observation.code.coding` | 8665-2 | Last menstrual period start date | http://loinc.org |
| 40 | 155 | Observation | `Observation.code.coding` | ANC.B6.DE14 | Last menstrual period (LMP) date | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 41 | 166 | Observation | `Observation.code.coding` | 11778-8 | Delivery date Estimated | http://loinc.org |
| 42 | 167 | Observation | `Observation.code.coding` | ANC.B6.DE22 | Expected date of delivery (EDD) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 43 | 178 | Observation | `Observation.code.coding` | 11781-2 | Delivery date US composite estimate | http://loinc.org |
| 44 | 179 | Observation | `Observation.code.coding` | ANC.B6.DE40 | Hari Perkiraan Lahir (HPL) USG | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 45 | 190 | Condition | `Condition.code.coding` | 398254007.0 | Pre-eclampsia | http://snomed.info/sct |
| 46 | 191 | Condition | `Condition.code.coding` | OI000018 | Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 47 | 192 | Condition | `Condition.code.coding` | 404684003.0 | Clinical finding | http://snomed.info/sct |
| 48 | 202 | Observation | `Observation.code.coding` | PC000004 | KB Pasca Persalinan |  |
| 49 | 203 | Observation | `Observation.valueCodeableConcept.coding` | 237122005.0 | Lactational amenorrhea | http://snomed.info/sct |
| 50 | 204 | Observation | `Observation.valueCodeableConcept.coding` | LA6523-0 | Condom | http://loinc.org |
| 51 | 205 | Observation | `Observation.valueCodeableConcept.coding` | LA6524-8 | Oral contraceptive pill | http://loinc.org |
| 52 | 206 | Observation | `Observation.valueCodeableConcept.coding` | LA6525-5 | Injectable/implantable hormone | http://loinc.org |
| 53 | 207 | Observation | `Observation.valueCodeableConcept.coding` | LA6527-1 | Intrauterine device | http://loinc.org |
| 54 | 208 | Observation | `Observation.valueCodeableConcept.coding` | SP000097 | Implan | http://terminology.kemkes.go.id/sp |
| 55 | 209 | Observation | `Observation.valueCodeableConcept.coding` | 77543007.0 | Ligation of fallopian tube | http://snomed.info/sct |
| 56 | 210 | Observation | `Observation.valueCodeableConcept.coding` | 22523008.0 | Vasectomy | http://snomed.info/sct |
| 57 | 211 | Observation | `Observation.valueCodeableConcept.coding` | 445375000.0 | Does not use contraception | http://snomed.info/sct |
| 58 | 221 | Observation | `Observation.code.coding` | 81954-0 | Date of death [Date] | http://loinc.org |
| 59 | 231 | Observation | `Observation.code.coding` | 81955-7 | Time of death [ClockTime] | http://loinc.org |
| 60 | 241 | Observation | `Observation.code.coding` | OC000028 | Jenis Tempat Meninggal | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 61 | 242 | Observation | `Observation.valueCodeableConcept.coding` | OT000001 | Polindes | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 62 | 243 | Observation | `Observation.valueCodeableConcept.coding` | OT000002 | Pustu | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 63 | 244 | Observation | `Observation.valueCodeableConcept.coding` | 102.0 | Pusat Kesehatan Masyarakat | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 64 | 245 | Observation | `Observation.valueCodeableConcept.coding` | 103.0 | Klinik | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 65 | 246 | Observation | `Observation.valueCodeableConcept.coding` | 104.0 | Rumah Sakit | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 66 | 247 | Observation | `Observation.valueCodeableConcept.coding` | 101.0 | Tempat Praktik Mandiri Tenaga Kesehatan | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 67 | 248 | Observation | `Observation.valueCodeableConcept.coding` | 264362003.0 | Home (environment) | http://snomed.info/sct |
| 68 | 249 | Observation | `Observation.valueCodeableConcept.coding` | LT000007 | Rumah Dukun | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 69 | 250 | Observation | `Observation.valueCodeableConcept.coding` | LT000008 | Dalam perjalanan dari rumah/ masyarakat | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 70 | 251 | Observation | `Observation.valueCodeableConcept.coding` | LT000009 | Dalam perjalanan ke faskes lain | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 71 | 252 | Observation | `Observation.valueCodeableConcept.coding` | LT000010 | Tempat Meninggal Lainnya | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 72 | 253 | Observation | `Observation.valueCodeableConcept.coding` | LT000011 | Belum Tahu Jenis Tempat Meninggal | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 73 | 277 | Observation | `Observation.code.coding` | 39016-1 | Age at death | http://loinc.org |
| 74 | 289 | Observation | `Observation.code.coding` | 79378-6 | Cause of death | http://loinc.org |
| 75 | 290 | Observation | `Observation.component.code.coding` | TK000019 | Kode group | http://terminology.kemkes.go.id |
| 76 | 291 | Observation | `Observation.component.valueCodeableConcept.coding` | GROUP-3 | Obstetric haemorrhage | http://terminology.kemkes.go.id/CodeSystem/icd-10-mm |
| 77 | 293 | Observation | `Observation.component.valueCodeableConcept.coding` | O46 | Antepartum haemorrhage, not elsewhere classified | http://terminology.kemkes.go.id/CodeSystem/icd-10-mm |
| 78 | 294 | Observation | `Observation.component.valueCodeableConcept.coding` | GROUP-3 | Obstetric haemorrhage | http://terminology.kemkes.go.id/CodeSystem/icd-10-mm |
| 79 | 296 | Observation | `Observation.component.valueCodeableConcept.coding` | O72 | Postpartum haemorrhage | http://terminology.kemkes.go.id/CodeSystem/icd-10-mm |
| 80 | 297 | Observation | `Observation.component.valueCodeableConcept.coding` | GROUP-4 | Pregnancy-related infection | http://terminology.kemkes.go.id/CodeSystem/icd-10-mm |
| 81 | 299 | Observation | `Observation.component.valueCodeableConcept.coding` | O85 | Puerperal sepsis | http://terminology.kemkes.go.id/CodeSystem/icd-10-mm |
| 82 | 300 | Observation | `Observation.component.valueCodeableConcept.coding` | Diagnose | ICD-10 | http://terminology.kemkes.go.id/CodeSystem/icd-10-mm |
| 83 | 302 | Observation | `Observation.component.valueCodeableConcept.coding` | O66.9 | Obstructed labour, unspecified | http://terminology.kemkes.go.id/CodeSystem/icd-10-mm |
| 84 | 303 | Observation | `Observation.component.valueCodeableConcept.coding` | GROUP-2 | Hypertensive disorders in pregnancy, childbirth, and the puerperium | http://terminology.kemkes.go.id/CodeSystem/icd-10-mm |
| 85 | 305 | Observation | `Observation.component.valueCodeableConcept.coding` | O14.9 | Pre-eclampsia, unspecified | http://terminology.kemkes.go.id/CodeSystem/icd-10-mm |
| 86 | 306 | Observation | `Observation.component.valueCodeableConcept.coding` | GROUP-2 | Hypertensive disorders in pregnancy, childbirth, and the puerperium | http://terminology.kemkes.go.id/CodeSystem/icd-10-mm |
| 87 | 308 | Observation | `Observation.component.valueCodeableConcept.coding` | O15 | Eclampsia | http://terminology.kemkes.go.id/CodeSystem/icd-10-mm |
| 88 | 309 | Observation | `Observation.component.valueCodeableConcept.coding` | GROUP-3 | Obstetric haemorrhage | http://terminology.kemkes.go.id/CodeSystem/icd-10-mm |
| 89 | 311 | Observation | `Observation.component.valueCodeableConcept.coding` | O71.1 | Rupture of uterus during labour | http://terminology.kemkes.go.id/CodeSystem/icd-10-mm |
| 90 | 312 | Observation | `Observation.component.valueCodeableConcept.coding` | GROUP-1 | Pregnancy with abortive outcome | http://terminology.kemkes.go.id/CodeSystem/icd-10-mm |
| 91 | 314 | Observation | `Observation.component.valueCodeableConcept.coding` | O07.8 | Other and unspecified failed attempted abortion, with other and unspecified complications | http://terminology.kemkes.go.id/CodeSystem/icd-10-mm |
| 92 | 315 | Observation | `Observation.component.valueCodeableConcept.coding` | GROUP-7 | Non-obstetric complications | http://terminology.kemkes.go.id/CodeSystem/icd-10-mm |
| 93 | 317 | Observation | `Observation.component.valueCodeableConcept.coding` | O99.8 | Other specified diseases and conditions complicating pregnancy, childbirth and the puerperium | http://terminology.kemkes.go.id/CodeSystem/icd-10-mm |
| 94 | 318 | Observation | `Observation.component.code.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 95 | 329 | Observation | `Observation.code.coding` | OC000026 | Date and time of death [TimeStamp] | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 96 | 331 | Observation | `Observation.valueCodeableConcept.coding` | 1156679005.0 | Maternal antenatal period | http://snomed.info/sct |
| 97 | 332 | Observation | `Observation.valueCodeableConcept.coding` | 1156682000.0 | Maternal intrapartum period | http://snomed.info/sct |
| 98 | 333 | Observation | `Observation.valueCodeableConcept.coding` | 255410009.0 | Maternal postpartum | http://snomed.info/sct |
| 99 | 350 | Observation | `Observation.code.coding` | SP000403 | Alasan Tidak Ada Nomor Induk Kependudukan | http://terminology.kemkes.go.id/sp |
| 100 | 351 | Observation | `Observation.valueCodeableConcept.coding` | SP000511 | Belum Ada Akta Kelahiran | http://terminology.kemkes.go.id/sp |
| 101 | 352 | Observation | `Observation.valueCodeableConcept.coding` | SP000512 | Belum Melengkapi Kebutuhan Administrasi | http://terminology.kemkes.go.id/sp |
| 102 | 353 | Observation | `Observation.valueCodeableConcept.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 103 | 364 | Observation | `Observation.code.coding` | 249222005.0 | Neonatal condition | http://snomed.info/sct |
| 104 | 365 | Observation | `Observation.valueCodeableConcept.coding` | 278978003.0 | Well baby | http://snomed.info/sct |
| 105 | 366 | Observation | `Observation.valueCodeableConcept.coding` | 39104002.0 | Illness | http://snomed.info/sct |
| 106 | 367 | Observation | `Observation.valueCodeableConcept.coding` | 276506001.0 | Neonatal death | http://snomed.info/sct |
| 107 | 377 | Observation | `Observation.code.coding` | 76516-4 | Gestational age—​at birth | http://loinc.org |
| 108 | 389 | Observation | `Observation.code.coding` | 57715-5 | Birth time | http://loinc.org |
| 109 | 399 | Observation | `Observation.code.coding` | 72150-6 | Delivery location | http://loinc.org |
| 110 | 400 | Observation | `Observation.valueCodeableConcept.coding` | OT000001 | Polindes | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 111 | 401 | Observation | `Observation.valueCodeableConcept.coding` | OT000002 | Pustu | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 112 | 402 | Observation | `Observation.valueCodeableConcept.coding` | 102.0 | Pusat Kesehatan Masyarakat | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 113 | 403 | Observation | `Observation.valueCodeableConcept.coding` | 103.0 | Klinik | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 114 | 404 | Observation | `Observation.valueCodeableConcept.coding` | 104.0 | Rumah Sakit | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 115 | 405 | Observation | `Observation.valueCodeableConcept.coding` | 101.0 | Tempat Praktik Mandiri Tenaga Kesehatan | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 116 | 406 | Observation | `Observation.valueCodeableConcept.coding` | 264362003.0 | Home (environment) | http://snomed.info/sct |
| 117 | 407 | Observation | `Observation.valueCodeableConcept.coding` | LT000007 | Rumah Dukun | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 118 | 408 | Observation | `Observation.valueCodeableConcept.coding` | LT000008 | Dalam perjalanan dari rumah/ masyarakat | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 119 | 409 | Observation | `Observation.valueCodeableConcept.coding` | LT000009 | Dalam perjalanan ke faskes lain | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 120 | 410 | Observation | `Observation.valueCodeableConcept.coding` | LT000010 | Tempat Meninggal Lainnya | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 121 | 411 | Observation | `Observation.valueCodeableConcept.coding` | LT000011 | Belum Tahu Jenis Tempat Meninggal | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 122 | 425 | Observation | `Observation.code.coding` | 8339-4 | Birth weight Measured | http://loinc.org |
| 123 | 437 | Observation | `Observation.code.coding` | 89269-5 | Body height Measured --at birth | http://loinc.org |
| 124 | 449 | Observation | `Observation.code.coding` | 8290-9 | Head Occipital-frontal circumference --at birth- by Tape measure | http://loinc.org |
| 125 | 461 | Observation | `Observation.code.coding` | 249222005.0 | Neonatal condition | http://snomed.info/sct |
| 126 | 462 | Observation | `Observation.valueCodeableConcept.coding` | SP000513 | Segera menangis | http://terminology.kemkes.go.id/sp |
| 127 | 463 | Observation | `Observation.valueCodeableConcept.coding` | SP000514 | Menangis beberapa saat | http://terminology.kemkes.go.id/sp |
| 128 | 464 | Observation | `Observation.valueCodeableConcept.coding` | 715041009.0 | Does not cry | http://snomed.info/sct |
| 129 | 465 | Observation | `Observation.valueCodeableConcept.coding` | LA6724-4 | Good color all over | http://loinc.org |
| 130 | 466 | Observation | `Observation.valueCodeableConcept.coding` | 95442007.0 | Peripheral cyanosis | http://snomed.info/sct |
| 131 | 467 | Observation | `Observation.valueCodeableConcept.coding` | 95617006.0 | Neonatal cyanosis | http://snomed.info/sct |
| 132 | 468 | Observation | `Observation.valueCodeableConcept.coding` | 255399007.0 | Congenital | http://snomed.info/sct |
| 133 | 479 | Condition | `Condition.code.coding` | 386639001.0 | Termination of pregnancy | http://snomed.info/sct |
| 134 | 487 | Observation | `Observation.code.coding` | 18185-9 | Gestational age | http://loinc.org |
| 135 | 488 | Observation | `Observation.code.coding` | ANC.B6.DE17 | Gestational age | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 136 | 491 | Observation | `Observation.component.code.coding` | SP000461 | Usia Kehamilan (Hari) | http://terminology.kemkes.go.id/sp |
| 137 | 513 | Observation | `Observation.code.coding` | 68688001.0 | Curettage | http://snomed.info/sct |
| 138 | 525 | Observation | `Observation.code.coding` | SP000515 | Tempat kuretase | http://terminology.kemkes.go.id/sp |
| 139 | 526 | Observation | `Observation.valueCodeableConcept.coding` | OT000002 | Pustu | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 140 | 527 | Observation | `Observation.valueCodeableConcept.coding` | 102.0 | Pusat Kesehatan Masyarakat | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 141 | 528 | Observation | `Observation.valueCodeableConcept.coding` | 103.0 | Klinik | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 142 | 529 | Observation | `Observation.valueCodeableConcept.coding` | 104.0 | Rumah Sakit | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 143 | 530 | Observation | `Observation.valueCodeableConcept.coding` | LT000010 | Tempat Meninggal Lainnya | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 144 | 531 | Observation | `Observation.valueCodeableConcept.coding` | LT000011 | Belum Tahu Jenis Tempat Meninggal | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 145 | 542 | Observation | `Observation.code.coding` | 82810-3 | Pregnancy status | http://loinc.org |
| 146 | 554 | Observation | `Observation.code.coding` | 81954-0 | Date of death [Date] | http://loinc.org |
| 147 | 565 | Observation | `Observation.code.coding` | 81955-7 | Time of death [ClockTime] | http://loinc.org |
| 148 | 576 | Observation | `Observation.code.coding` | OC000028 | Jenis Tempat Meninggal | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 149 | 577 | Observation | `Observation.valueCodeableConcept.coding` | OT000001 | Polindes | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 150 | 578 | Observation | `Observation.valueCodeableConcept.coding` | OT000002 | Pustu | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 151 | 579 | Observation | `Observation.valueCodeableConcept.coding` | 102.0 | Pusat Kesehatan Masyarakat | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 152 | 580 | Observation | `Observation.valueCodeableConcept.coding` | 103.0 | Klinik | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 153 | 581 | Observation | `Observation.valueCodeableConcept.coding` | 104.0 | Rumah Sakit | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 154 | 582 | Observation | `Observation.valueCodeableConcept.coding` | 101.0 | Tempat Praktik Mandiri Tenaga Kesehatan | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 155 | 583 | Observation | `Observation.valueCodeableConcept.coding` | 264362003.0 | Home (environment) | http://snomed.info/sct |
| 156 | 584 | Observation | `Observation.valueCodeableConcept.coding` | LT000007 | Rumah Dukun | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 157 | 585 | Observation | `Observation.valueCodeableConcept.coding` | LT000008 | Dalam perjalanan dari rumah/ masyarakat | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 158 | 586 | Observation | `Observation.valueCodeableConcept.coding` | LT000009 | Dalam perjalanan ke faskes lain | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 159 | 587 | Observation | `Observation.valueCodeableConcept.coding` | LT000010 | Tempat Meninggal Lainnya | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 160 | 588 | Observation | `Observation.valueCodeableConcept.coding` | LT000011 | Belum Tahu Jenis Tempat Meninggal | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 161 | 605 | Observation | `Observation.code.coding` | 79378-6 | Cause of death | http://loinc.org |
| 162 | 606 | Observation | `Observation.component.code.coding` | TK000019 | Kode group | http://terminology.kemkes.go.id |
| 163 | 607 | Observation | `Observation.component.valueCodeableConcept.coding` | N | Neonatal death | http://terminology.kemkes.go.id/CodeSystem/icd-10-pm |
| 164 | 608 | Observation | `Observation.component.code.coding` | TK000020 | Kode subgroup | http://terminology.kemkes.go.id |
| 165 | 609 | Observation | `Observation.component.valueCodeableConcept.coding` | N9 | Low birth weight and prematurity | http://terminology.kemkes.go.id/CodeSystem/icd-10-pm |
| 166 | 611 | Observation | `Observation.component.valueCodeableConcept.coding` | P07 | Disorders related to short gestation and low birth weight, not elsewhere classified | http://terminology.kemkes.go.id/CodeSystem/icd-10-pm |
| 167 | 612 | Observation | `Observation.component.code.coding` | TK000020 | Kode subgroup | http://terminology.kemkes.go.id |
| 168 | 613 | Observation | `Observation.component.valueCodeableConcept.coding` | N4 | Complications of intrapartum events | http://terminology.kemkes.go.id/CodeSystem/icd-10-pm |
| 169 | 615 | Observation | `Observation.component.valueCodeableConcept.coding` | P21 | Birth asphyxia | http://terminology.kemkes.go.id/CodeSystem/icd-10-pm |
| 170 | 616 | Observation | `Observation.component.code.coding` | TK000020 | Kode subgroup | http://terminology.kemkes.go.id |
| 171 | 617 | Observation | `Observation.component.valueCodeableConcept.coding` | N6 | Infection | http://terminology.kemkes.go.id/CodeSystem/icd-10-pm |
| 172 | 619 | Observation | `Observation.component.valueCodeableConcept.coding` | A33 | Tetanus neonatorum | http://terminology.kemkes.go.id/CodeSystem/icd-10-pm |
| 173 | 620 | Observation | `Observation.component.code.coding` | TK000020 | Kode subgroup | http://terminology.kemkes.go.id |
| 174 | 621 | Observation | `Observation.component.valueCodeableConcept.coding` | N6 | Infection | http://terminology.kemkes.go.id/CodeSystem/icd-10-pm |
| 175 | 623 | Observation | `Observation.component.valueCodeableConcept.coding` | G03.9 | Meningitis, unspecified | http://terminology.kemkes.go.id/CodeSystem/icd-10-pm |
| 176 | 624 | Observation | `Observation.component.code.coding` | TK000020 | Kode subgroup | http://terminology.kemkes.go.id |
| 177 | 625 | Observation | `Observation.component.valueCodeableConcept.coding` | N6 | Infection | http://terminology.kemkes.go.id/CodeSystem/icd-10-pm |
| 178 | 627 | Observation | `Observation.component.valueCodeableConcept.coding` | P23 | Congenital pneumonia | http://terminology.kemkes.go.id/CodeSystem/icd-10-pm |
| 179 | 628 | Observation | `Observation.component.code.coding` | TK000020 | Kode subgroup | http://terminology.kemkes.go.id |
| 180 | 629 | Observation | `Observation.component.valueCodeableConcept.coding` | N6 | Infection | http://terminology.kemkes.go.id/CodeSystem/icd-10-pm |
| 181 | 631 | Observation | `Observation.component.valueCodeableConcept.coding` | P36 | Bacterial sepsis of newborn | http://terminology.kemkes.go.id/CodeSystem/icd-10-pm |
| 182 | 632 | Observation | `Observation.component.code.coding` | TK000020 | Kode subgroup | http://terminology.kemkes.go.id |
| 183 | 633 | Observation | `Observation.component.valueCodeableConcept.coding` | N1 | Congenital malformations, deformations and chromosomal abnormalities | http://terminology.kemkes.go.id/CodeSystem/icd-10-pm |
| 184 | 635 | Observation | `Observation.component.valueCodeableConcept.coding` | Q89 | Other congenital malformations, not elsewhere classified | http://terminology.kemkes.go.id/CodeSystem/icd-10-pm |
| 185 | 636 | Observation | `Observation.component.code.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 186 | 647 | Observation | `Observation.code.coding` | 64710-7 | Was your pregnancy a live birth, stillbirth, miscarriage, abortion, or ectopic pregnancy [PhenX] | http://loinc.org |
| 187 | 648 | Observation | `Observation.valueCodeableConcept.coding` | 237361005.0 | Antepartum fetal death | http://snomed.info/sct |
| 188 | 649 | Observation | `Observation.valueCodeableConcept.coding` | 237362003.0 | Intrapartum fetal death | http://snomed.info/sct |
| 189 | 650 | Observation | `Observation.valueCodeableConcept.coding` | 276506001.0 | Newborn death | http://snomed.info/sct |
| 190 | 660 | Observation | `Observation.code.coding` | 52480-1 | Anthropometric Measures | http://loinc.org |
| 191 | 672 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 192 | 684 | Observation | `Observation.code.coding` | 8306-3 | Body height --lying | http://loinc.org |
| 193 | 696 | Observation | `Observation.code.coding` | 9843-4 | Head Occipital-frontal circumference | http://loinc.org |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 54 |
| http://loinc.org | 30 |
| http://terminology.kemkes.go.id/CodeSystem/organization-type | 22 |
| http://terminology.kemkes.go.id/sp | 18 |
| http://terminology.kemkes.go.id/CodeSystem/icd-10-mm | 18 |
| http://terminology.kemkes.go.id/CodeSystem/location-type | 17 |
| http://terminology.kemkes.go.id/CodeSystem/icd-10-pm | 15 |
| http://terminology.kemkes.go.id | 9 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 5 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 3 |
| http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes | 1 |
|  | 1 |
| **Total** | **193** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 14 | – | Tanggal entry | – | `` |
| 15 | – | Waktu entry | – | `` |
| 23 | – | Apakah mempunyai Nomor Induk Kependudukan (NIK) | Tidak dimapping FHIR | `` |
| 42 | – | Apakah tanggal lahir diketahui? | Tidak dimapping FHIR | `` |
| 274 | – | Tempat Ibu meninggal (tidak ada di pilihan) | – | `` |
| 343 | – | Apakah mempunyai Nomor Induk Kependudukan (NIK) | Tidak dimapping FHIR | `` |
| 419 | – | Nama fasilitas kesehatan tempat bayi dilahirkan (lainnya) | – | `` |
| 476 | – | Keterangan tambahan (status bayi) | – | `` |
| 539 | – | Nama fasilitas kesehatan tempat kuretase | – | `` |
| 602 | – | Nama fasilitas kesehatan tempat bayi meninggal (lainnya) | – | `` |
