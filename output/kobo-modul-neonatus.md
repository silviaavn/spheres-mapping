# Output Form: Kobo Modul Neonatus

Sumber: `mapping/phdt-data-dictionary-kobo-modul-neonatus.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-kobo-modul-neonatus.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 50 |
| Code (`jumlah code` = 1) | 100 |
| Code unik (code + CodeSystem) | 85 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 4 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–33 | Patient | – | – | _Nama Bayi_ → `Patient.name.text` (2, tanpa BQ)<br>_NIK Bayi_ → `Patient.identifier.value` (5, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (7, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (9, tanpa BQ)<br>_Tempat lahir_ → `Patient.extension:birthPlace.valueAddress.text` (10, tanpa BQ)<br>_Kembar_ → `Patient.multipleBirthBoolean` (11, tanpa BQ)<br>_Alamat Domisili_ → `Patient.address.use` (12, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (18, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (21, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.extension.valueCode` (24, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.extension.valueCode` (27, tanpa BQ)<br>_RW_ → `Patient.address.extension.extension.valueCode` (30, tanpa BQ)<br>_RT_ → `Patient.address.extension.extension.valueCode` (33, tanpa BQ) |
| 2 | 34–44 | RelatedPerson | – | – | _Nama Ibu_ → `RelatedPerson.name.text` (35, tanpa BQ)<br>_No Hp Ibu_ → `RelatedPerson.telecom.value` (37, tanpa BQ)<br>_NIK Ibu_ → `RelatedPerson.identifier.value` (43, tanpa BQ) |
| 3 | 45–53 | RelatedPerson | – | – | _Nama Ayah_ → `RelatedPerson.name.text` (45, tanpa BQ)<br>_No Hp Ayah_ → `RelatedPerson.telecom.value` (47, tanpa BQ)<br>_NIK Ayah_ → `RelatedPerson.identifier.value` (53, tanpa BQ) |
| 4 | 103–109 | PractitionerRole | – | – | _Tenaga Pemeriksa_ → `PractitionerRole.active` (103, tanpa BQ) |
| 5 | 110–130 | Practitioner | – | – | _Nama Tenaga Kesehatan_ → `Practitioner.name.text` (112, tanpa BQ)<br>_Jenis Kelamin Tenaga Kesehatan_ → `Practitioner.gender` (113, tanpa BQ)<br>_Nama Provinsi_ → `Practitioner.address.extension.extension.valueCode` (120, tanpa BQ)<br>_Nama Kabupaten_ → `Practitioner.address.extension.extension.valueCode` (123, tanpa BQ)<br>_Nama Kecamatan_ → `Practitioner.address.extension.extension.valueCode` (126, tanpa BQ)<br>_Nama Desa_ → `Practitioner.address.extension.extension.valueCode` (129, tanpa BQ) |
| 6 | 131–139 | EpisodeOfCare | Neonate | Neonate | – |
| 7 | 140–157 | Encounter | – | – | _Kunjungan Neonatus_ → `Encounter.identifier` (141, tanpa BQ)<br>_Tanggal Kunjungan_ → `Encounter.period.start` (152, tanpa BQ) |
| 8 | 158–164 | Condition | Z00.1 | Routine child health examination | – |
| 9 | 179–189 | Observation | 365475008 | Place in family order | _Anak ke_ → `Observation.valueInteger` (182, tanpa BQ) |
| 10 | 190–200 | Observation | 57715-5 | Birth time | _Jam Lahir_ → `Observation.valueTime` (193, tanpa BQ) |
| 11 | 201–212 | Observation | 76516-4 | Gestational age—​at birth | _Usia Gestasi Saat Lahir_ → `Observation.valueQuantity.value` (204, tanpa BQ) |
| 12 | 213–226 | Observation | 883-9 | ABO group [Type] in Blood | _Golongan darah_ → `Observation.valueCodeableConcept.coding` (216, tanpa BQ) |
| 13 | 227–238 | Observation | 10331-7 | Rh [Type] in Blood | _Rhesus_ → `Observation.valueCodeableConcept.coding` (230, tanpa BQ) |
| 14 | 239–250 | Observation | 8339-4 | Birth weight Measured | _Berat Badan Saat Lahir_ → `Observation.valueQuantity.value` (242, tanpa BQ) |
| 15 | 251–262 | Observation | 89269-5 | Body height Measured --at birth | _Panjang Badan Saat Lahir_ → `Observation.valueQuantity.value` (254, tanpa BQ) |
| 16 | 263–274 | Observation | 8290-9 | Head Occipital-frontal circumference --at birth- by Tape measure | _Lingkar Kepala Saat Lahir_ → `Observation.valueQuantity.value` (266, tanpa BQ) |
| 17 | 275–296 | Observation | 276654001 | Congenital malformation | _Kelainan Bawaan_ → `Observation.valueCodeableConcept.coding` (278, tanpa BQ) |
| 18 | 297–308 | Observation | 8867-4 | Heart rate | _Frekuensi Denyut Jantung_ → `Observation.valueQuantity.value` (300, tanpa BQ) |
| 19 | 309–319 | Observation | 8310-5 | Body temperature | _Suhu_ → `Observation.valueQuantity.value` (312, tanpa BQ) |
| 20 | 320–330 | Observation | 9279-1 | Respiratory rate | _Pernapasan_ → `Observation.valueQuantity.value` (323, tanpa BQ) |
| 21 | 331–341 | Procedure | 386412000 | Resuscitation of neonate | _Apakah Diberikan Resusitasi_ → `Procedure.category.coding` (331, tanpa BQ) |
| 22 | 342–352 | Procedure | PC000003 | Manajemen Terpadu Bayi Muda (MTBM) | _Apakah dilakukan pemeriksaan kesehatan dengan pendekatan MTBM_ → `Procedure.category.coding` (342, tanpa BQ) |
| 23 | 353–363 | Procedure | SP000126 | ARV Profilaksis | _ARV Profilaksis pada bayi baru lahir_ → `Procedure.category.coding` (353, tanpa BQ) |
| 24 | 364–374 | Procedure | 448883004 | Injection of vitamin K1 | _Apakah diberikan vitamin K_ → `Procedure.category.coding` (364, tanpa BQ) |
| 25 | 375–385 | Procedure | PC000001 | Perawatan Tali Pusat | _Perawatan Tali Pusat_ → `Procedure.category.coding` (375, tanpa BQ) |
| 26 | 386–396 | Procedure | PC000002 | Pemberian Salep Antibiotik Mata | _Salep Antibiotik Mata_ → `Procedure.category.coding` (386, tanpa BQ) |
| 27 | 397–421 | Immunization | – | – | _Imunisasi Hepatitis B (HB0)_ → `Immunization.status` (397, tanpa BQ)<br>_Tanggal Pemberian Vaksin_ → `Immunization.occurrenceDateTime` (405, tanpa BQ)<br>_Nomor lot Vaksin_ → `Immunization.lotNumber` (412, tanpa BQ)<br>_Tanggal Kadaluarsa Vaksin_ → `Immunization.expirationDate` (413, tanpa BQ)<br>_Alasan Tidak Diberikan Vaksin HB0_ → `Immunization.statusReason.coding` (417, tanpa BQ) |
| 28 | 422–432 | Procedure | 431868002 | Initiation of breastfeeding | _Inisiasi Menyusu Dini (IMD)_ → `Procedure.category.coding` (422, tanpa BQ) |
| 29 | 433–444 | Observation | OC000016 | Waktu Inisiasi Menyusui Dini | _Waktu Inisiasi Menyusu Dini (IMD)_ → `Observation.valueCodeableConcept.coding` (436, tanpa BQ) |
| 30 | 445–457 | Observation | 10206-1 | Physical findings of Skin Narrative | _Pemeriksaan Kulit_ → `Observation.valueString` (448, tanpa BQ)<br>_Interpretasi Hasil Pemeriksaan Kulit_ → `Observation.interpretation.coding` (449, tanpa BQ) |
| 31 | 458–470 | Observation | 10199-8 | Physical findings of Head Narrative | _Pemeriksaan Kepala_ → `Observation.valueString` (461, tanpa BQ)<br>_Interpretasi Hasil Pemeriksaan Kepala_ → `Observation.interpretation.coding` (462, tanpa BQ) |
| 32 | 471–483 | Observation | 10197-2 | Physical findings of Eye Narrative | _Pemeriksaan Mata_ → `Observation.valueString` (474, tanpa BQ)<br>_Interpretasi Hasil Pemeriksaan Mata_ → `Observation.interpretation.coding` (475, tanpa BQ) |
| 33 | 484–496 | Observation | 32453-3 | Physical findings of Mouth | _Pemeriksaan Mulut_ → `Observation.valueString` (487, tanpa BQ)<br>_Interpretasi Hasil Pemeriksaan Mulut_ → `Observation.interpretation.coding` (488, tanpa BQ) |
| 34 | 497–509 | Observation | 10191-5 | Physical findings of Abdomen Narrative | _Pemeriksaan Perut_ → `Observation.valueString` (500, tanpa BQ)<br>_Interpretasi Hasil Pemeriksaan Perut_ → `Observation.interpretation.coding` (501, tanpa BQ) |
| 35 | 510–522 | Observation | 10192-3 | Physical findings of Back Narrative | _Pemeriksaan Punggung_ → `Observation.valueString` (513, tanpa BQ)<br>_Interpretasi Hasil Pemeriksaan Punggung_ → `Observation.interpretation.coding` (514, tanpa BQ) |
| 36 | 523–535 | Observation | 11388-6 | Physical findings of Buttocks Narrative | _Pemeriksaan Lubang Anus_ → `Observation.valueString` (526, tanpa BQ)<br>_Interpretasi Hasil Pemeriksaan Lubang Anus_ → `Observation.interpretation.coding` (527, tanpa BQ) |
| 37 | 536–548 | Observation | 11400-9 | Physical findings of Genitalia Narrative | _Pemeriksaan Alat Kelamin_ → `Observation.valueString` (539, tanpa BQ)<br>_Interpretasi Hasil Pemeriksaan Alat Kelamin_ → `Observation.interpretation.coding` (540, tanpa BQ) |
| 38 | 549–559 | Procedure | 400984005 | Congenital hypothyroidism screening test | _Apakah dilakukan SHK_ → `Procedure.category.coding` (549, tanpa BQ) |
| 39 | 560–574 | Observation | 29575-8 | Thyrotropin [Units/volume] in DBS | _Jika Ya, hasil pemeriksaan terakhir dari laboratorium_ → `Observation.valueQuantity.value` (563, tanpa BQ) |
| 40 | 575–586 | Observation | 1145307003 | Exclusively breastfed | _Apakah Diberikan ASI Eksklusi_ → `Observation.valueBoolean` (578, tanpa BQ) |
| 41 | 587–598 | Observation | 29463-7 | Body weight | _Berat Badan_ → `Observation.valueQuantity.value` (590, tanpa BQ) |
| 42 | 599–610 | Observation | 8306-3 | Body height --lying | _Tinggi Badan_ → `Observation.valueQuantity.value` (602, tanpa BQ) |
| 43 | 611–622 | QuestionnaireResponse | https://fhir.kemkes.go.id/Questionnaire/Q0004 | – | _Kelas Ibu Balita_ → `QuestionnaireResponse.questionnaire` (611, tanpa BQ) |
| 44 | 623–638 | Observation | 1153593003 | Weight for age z-score | _BB/U_ → `Observation.status` (623, tanpa BQ)<br>_ZS BB/U_ → `Observation.valueQuantity.value` (626, tanpa BQ)<br>_Interpretasi BB/U_ → `Observation.interpretation.coding` (628, tanpa BQ) |
| 45 | 639–654 | Observation | 1153590000 | Length for age z score | _PB/U_ → `Observation.status` (639, tanpa BQ)<br>_ZS PB/U_ → `Observation.valueQuantity.value` (642, tanpa BQ)<br>_Interpretasi PB/U_ → `Observation.interpretation.coding` (644, tanpa BQ) |
| 46 | 655–672 | Observation | 1153598007 | Weight for length z score | _BB/PB_ → `Observation.status` (655, tanpa BQ)<br>_ZS BB/PB_ → `Observation.valueQuantity.value` (658, tanpa BQ)<br>_Interpretasi BB/PB_ → `Observation.interpretation.coding` (660, tanpa BQ) |
| 47 | 673–688 | AllergyIntolerance | – | – | _Apakah ada alergi obat saat ini?_ → `AllergyIntolerance.clinicalStatus.coding` (673, tanpa BQ)<br>_Jika Ya, jenis obat?_ → `AllergyIntolerance.code.coding` (675, tanpa BQ) |
| 48 | 689–699 | Procedure | SP000296 | Skrining Penyakit Jantung Bawaan | _Apakah dilakukan PJB_ → `Procedure.category.coding` (689, tanpa BQ) |
| 49 | 700–721 | ServiceRequest | 736282001 | Neonatal critical care plan | _Rujuk_ → `ServiceRequest.status` (700, tanpa BQ)<br>_Faskes Rujukan_ → `ServiceRequest.locationCode.coding` (713, tanpa BQ)<br>_Nama Faskes Rujukan_ → `ServiceRequest.locationCode.text` (721, tanpa BQ) |
| 50 | 722–732 | Observation | 20564-1 | Oxygen saturation in Blood | _Saturasi Oksigen_ → `Observation.valueQuantity.value` (725, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 29 |
| Procedure | 9 |
| RelatedPerson | 2 |
| Patient | 1 |
| PractitionerRole | 1 |
| Practitioner | 1 |
| EpisodeOfCare | 1 |
| Encounter | 1 |
| Condition | 1 |
| Immunization | 1 |
| QuestionnaireResponse | 1 |
| AllergyIntolerance | 1 |
| ServiceRequest | 1 |
| **Total** | **50** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 105 | PractitionerRole | `PractitionerRole.code.coding` | 309453006 | Registered midwife | http://snomed.info/sct |
| 2 | 106 | PractitionerRole | `PractitionerRole.code.coding` | 309343006 | Physician | http://snomed.info/sct |
| 3 | 107 | PractitionerRole | `PractitionerRole.code.coding` | 309367003 | Obstetrician and gynecologist | http://snomed.info/sct |
| 4 | 108 | PractitionerRole | `PractitionerRole.code.coding` | 224535009 | Registered nurse | http://snomed.info/sct |
| 5 | 135 | EpisodeOfCare | `EpisodeOfCare.type.coding` | Neonate | Neonate | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 6 | 160 | Condition | `Condition.code.coding` | Z00.1 | Routine child health examination | http://hl7.org/fhir/sid/icd-10 |
| 7 | 181 | Observation | `Observation.code.coding` | 365475008 | Place in family order | http://snomed.info/sct |
| 8 | 192 | Observation | `Observation.code.coding` | 57715-5 | Birth time | http://loinc.org |
| 9 | 203 | Observation | `Observation.code.coding` | 76516-4 | Gestational age—​at birth | http://loinc.org |
| 10 | 215 | Observation | `Observation.code.coding` | 883-9 | ABO group [Type] in Blood | http://loinc.org |
| 11 | 216 | Observation | `Observation.valueCodeableConcept.coding` | LA19710-5 | Group A | http://loinc.org |
| 12 | 217 | Observation | `Observation.valueCodeableConcept.coding` | LA19709-7 | Group B | http://loinc.org |
| 13 | 218 | Observation | `Observation.valueCodeableConcept.coding` | LA19708-9 | Group O | http://loinc.org |
| 14 | 219 | Observation | `Observation.valueCodeableConcept.coding` | LA28449-9 | Group AB | http://loinc.org |
| 15 | 229 | Observation | `Observation.code.coding` | 10331-7 | Rh [Type] in Blood | http://loinc.org |
| 16 | 230 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 17 | 231 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 18 | 241 | Observation | `Observation.code.coding` | 8339-4 | Birth weight Measured | http://loinc.org |
| 19 | 253 | Observation | `Observation.code.coding` | 89269-5 | Body height Measured --at birth | http://loinc.org |
| 20 | 265 | Observation | `Observation.code.coding` | 8290-9 | Head Occipital-frontal circumference --at birth- by Tape measure | http://loinc.org |
| 21 | 277 | Observation | `Observation.code.coding` | 276654001 | Congenital malformation | http://snomed.info/sct |
| 22 | 278 | Observation | `Observation.valueCodeableConcept.coding` | 80281008 | Cleft lip | http://snomed.info/sct |
| 23 | 279 | Observation | `Observation.valueCodeableConcept.coding` | 13213009 | Congenital heart disease | http://snomed.info/sct |
| 24 | 280 | Observation | `Observation.valueCodeableConcept.coding` | 35045004 | Microtia | http://snomed.info/sct |
| 25 | 281 | Observation | `Observation.valueCodeableConcept.coding` | 22006008 | Hypertelorism | http://snomed.info/sct |
| 26 | 282 | Observation | `Observation.valueCodeableConcept.coding` | 367506006 | Polydactyly | http://snomed.info/sct |
| 27 | 283 | Observation | `Observation.valueCodeableConcept.coding` | 52781008 | Congenital hip dysplasia | http://snomed.info/sct |
| 28 | 284 | Observation | `Observation.valueCodeableConcept.coding` | 1156475005 | Congenital talipes equinovarus | http://snomed.info/sct |
| 29 | 285 | Observation | `Observation.valueCodeableConcept.coding` | 253098009 | Neural tube defect | http://snomed.info/sct |
| 30 | 286 | Observation | `Observation.valueCodeableConcept.coding` | 118928003 | Disorder of abdominal wall | http://snomed.info/sct |
| 31 | 287 | Observation | `Observation.valueCodeableConcept.coding` | 42030000 | Disorder of the genitourinary system | http://snomed.info/sct |
| 32 | 288 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 33 | 299 | Observation | `Observation.code.coding` | 8867-4 | Heart rate | http://loinc.org |
| 34 | 311 | Observation | `Observation.code.coding` | 8310-5 | Body temperature | http://loinc.org |
| 35 | 322 | Observation | `Observation.code.coding` | 9279-1 | Respiratory rate | http://loinc.org |
| 36 | 334 | Procedure | `Procedure.code.coding` | 386412000 | Resuscitation of neonate | http://snomed.info/sct |
| 37 | 345 | Procedure | `Procedure.code.coding` | PC000003 | Manajemen Terpadu Bayi Muda (MTBM) | http://terminology.kemkes.go.id/CodeSystem/clinical-term" |
| 38 | 356 | Procedure | `Procedure.code.coding` | SP000126 | ARV Profilaksis | http://terminology.kemkes.go.id/sp |
| 39 | 367 | Procedure | `Procedure.code.coding` | 448883004 | Injection of vitamin K1 | http://snomed.info/sct |
| 40 | 378 | Procedure | `Procedure.code.coding` | PC000001 | Perawatan Tali Pusat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 41 | 389 | Procedure | `Procedure.code.coding` | PC000002 | Pemberian Salep Antibiotik Mata | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 42 | 400 | Immunization | `Immunization.vaccineCode` | 8 | Hep B, adolescent or pediatric | http://hl7.org/fhir/sid/cvx |
| 43 | 401 | Immunization | `Immunization.vaccineCode` | VG45 | HepB | http://sys-ids.kemkes.go.id/kfa |
| 44 | 425 | Procedure | `Procedure.code.coding` | 431868002 | Initiation of breastfeeding | http://snomed.info/sct |
| 45 | 435 | Observation | `Observation.code.coding` | OC000016 | Waktu Inisiasi Menyusui Dini | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 46 | 436 | Observation | `Observation.valueCodeableConcept.coding` | OV000014 | Kurang dari 1 Jam | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 47 | 437 | Observation | `Observation.valueCodeableConcept.coding` | OV000015 | Lebih dari 1 Jam | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 48 | 447 | Observation | `Observation.code.coding` | 10206-1 | Physical findings of Skin Narrative | http://loinc.org |
| 49 | 449 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 50 | 450 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 51 | 460 | Observation | `Observation.code.coding` | 10199-8 | Physical findings of Head Narrative | http://loinc.org |
| 52 | 462 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 53 | 463 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 54 | 473 | Observation | `Observation.code.coding` | 10197-2 | Physical findings of Eye Narrative | http://loinc.org |
| 55 | 475 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 56 | 476 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 57 | 486 | Observation | `Observation.code.coding` | 32453-3 | Physical findings of Mouth | http://loinc.org |
| 58 | 488 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 59 | 489 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 60 | 499 | Observation | `Observation.code.coding` | 10191-5 | Physical findings of Abdomen Narrative | http://loinc.org |
| 61 | 501 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 62 | 502 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 63 | 512 | Observation | `Observation.code.coding` | 10192-3 | Physical findings of Back Narrative | http://loinc.org |
| 64 | 514 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 65 | 515 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 66 | 525 | Observation | `Observation.code.coding` | 11388-6 | Physical findings of Buttocks Narrative | http://loinc.org |
| 67 | 527 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 68 | 528 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 69 | 538 | Observation | `Observation.code.coding` | 11400-9 | Physical findings of Genitalia Narrative | http://loinc.org |
| 70 | 540 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 71 | 541 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 72 | 552 | Procedure | `Procedure.code.coding` | 400984005 | Congenital hypothyroidism screening test | http://snomed.info/sct |
| 73 | 562 | Observation | `Observation.code.coding` | 29575-8 | Thyrotropin [Units/volume] in DBS | http://loinc.org |
| 74 | 566 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 75 | 567 | Observation | `Observation.interpretation.coding` | H | High | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 76 | 577 | Observation | `Observation.code.coding` | 1145307003 | Exclusively breastfed | http://snomed.info/sct |
| 77 | 589 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 78 | 601 | Observation | `Observation.code.coding` | 8306-3 | Body height --lying | http://loinc.org |
| 79 | 625 | Observation | `Observation.code.coding` | 1153593003 | Weight for age z-score | http://snomed.info/sct |
| 80 | 628 | Observation | `Observation.interpretation.coding` | 248342006 | Underweight | http://snomed.info/sct |
| 81 | 629 | Observation | `Observation.interpretation.coding` | 43664005 | Normal weight | http://snomed.info/sct |
| 82 | 630 | Observation | `Observation.interpretation.coding` | OI000010 | Risiko Berat Badan Lebih | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 83 | 631 | Observation | `Observation.interpretation.coding` | OI000007 | Berat Badan Sangat Kurang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 84 | 641 | Observation | `Observation.code.coding` | 1153590000 | Length for age z score | http://snomed.info/sct |
| 85 | 644 | Observation | `Observation.interpretation.coding` | 17489000 | Body height normal for age | http://snomed.info/sct |
| 86 | 645 | Observation | `Observation.interpretation.coding` | 444000005 | Short stature for age | http://snomed.info/sct |
| 87 | 646 | Observation | `Observation.interpretation.coding` | OI000011 | Sangat Pendek | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 88 | 647 | Observation | `Observation.interpretation.coding` | 83077003 | Tall for age | http://snomed.info/sct |
| 89 | 657 | Observation | `Observation.code.coding` | 1153598007 | Weight for length z score | http://snomed.info/sct |
| 90 | 660 | Observation | `Observation.interpretation.coding` | 248324001 | Well nourished | http://snomed.info/sct |
| 91 | 661 | Observation | `Observation.interpretation.coding` | OI000001 | Gizi Buruk | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 92 | 662 | Observation | `Observation.interpretation.coding` | 248325000 | Undernourished | http://snomed.info/sct |
| 93 | 663 | Observation | `Observation.interpretation.coding` | 238131007 | Overweight | http://snomed.info/sct |
| 94 | 664 | Observation | `Observation.interpretation.coding` | 414915002 | Obese | http://snomed.info/sct |
| 95 | 665 | Observation | `Observation.interpretation.coding` | OI000004 | Risiko Gizi Lebih | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 96 | 692 | Procedure | `Procedure.code.coding` | SP000296 | Skrining Penyakit Jantung Bawaan | http://terminology.kemkes.go.id/sp |
| 97 | 704 | ServiceRequest | `ServiceRequest.code.coding` | 736282001 | Neonatal critical care plan | http://snomed.info/sct |
| 98 | 713 | ServiceRequest | `ServiceRequest.locationCode.coding` | SP000129 | Puskesmas PONED | http://terminology.kemkes.go.id/sp |
| 99 | 717 | ServiceRequest | `ServiceRequest.locationCode.coding` | SP000128 | Rumah Sakit Ibu dan Anak | http://terminology.kemkes.go.id/sp |
| 100 | 724 | Observation | `Observation.code.coding` | 20564-1 | Oxygen saturation in Blood | http://loinc.org |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 35 |
| http://loinc.org | 28 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 18 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 10 |
| http://terminology.kemkes.go.id/sp | 4 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 1 |
| http://hl7.org/fhir/sid/icd-10 | 1 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term" | 1 |
| http://hl7.org/fhir/sid/cvx | 1 |
| http://sys-ids.kemkes.go.id/kfa | 1 |
| **Total** | **100** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 57 | – | Jenis Faskes | Organization | `Organization.type` |
| 61 | – | Faskes yang melayani | Organization | `Organization.name` |
