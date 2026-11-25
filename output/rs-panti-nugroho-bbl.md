# Output Form: SIM RS Panti Nugroho BBL

Sumber: `mapping/phdt-data-dictionary-rs-panti-nugroho-bbl.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-rs-panti-nugroho-bbl.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 31 |
| Code (`jumlah code` = 1) | 55 |
| Code unik (code + CodeSystem) | 48 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 2 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–32 | Patient | – | – | _Nama Bayi_ → `Patient.name.text` (2, tanpa BQ)<br>_NIK Bayi/ Ibu_ → `Patient.identifier.value` (6, tanpa BQ)<br>_NIK Ibu_ → `Patient.identifier.value` (9, tanpa BQ)<br>_No HP Orang Tua_ → `Patient.telecom` (10, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (13, tanpa BQ)<br>_Tempat Lahir_ → `Patient.extension.valueAddress.city` (15, tanpa BQ)<br>_Kembar_ → `Patient.multipleBirthBoolean` (16, tanpa BQ)<br>_Alamat Domisili_ → `Patient.address.line` (18, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (23, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (26, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.extension.valueCode` (29, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.extension.valueCode` (32, tanpa BQ) |
| 2 | 33–39 | RelatedPerson | – | – | _Nama Ibu_ → `RelatedPerson.name.text` (33, tanpa BQ)<br>_NIK Ibu_ → `RelatedPerson.identifier` (34, tanpa BQ) |
| 3 | 40–46 | RelatedPerson | – | – | _Nama Ayah_ → `RelatedPerson.name.text` (40, tanpa BQ)<br>_NIK Ayah_ → `RelatedPerson.identifier` (41, tanpa BQ) |
| 4 | 85–91 | Practitioner | – | – | _NIK_ → `Practitioner.identifier.value` (87, tanpa BQ)<br>_Nama Tenaga Kesehatan_ → `Practitioner.name.text` (89, tanpa BQ)<br>_Jenis Kelamin Tenaga Kesehatan_ → `Practitioner.gender` (90, tanpa BQ) |
| 5 | 92–100 | PractitionerRole | – | – | _Tenaga Pemeriksa_ → `PractitionerRole.code.coding` (96, tanpa BQ) |
| 6 | 102–117 | Encounter | – | – | _Kunjungan Neonatus_ → `Encounter.identifier` (103, tanpa BQ)<br>_Tanggal INC (Bersalin)_ → `Encounter.period.start` (112, tanpa BQ)<br>_Tempat Pelayanan INC_ → `Encounter.location.location.display` (115, tanpa BQ) |
| 7 | 118–125 | Condition | Z00.1 | Routine child health examination | – |
| 8 | 136–144 | EpisodeOfCare | Neonate | Neonate | – |
| 9 | 145–155 | Observation | 365475008 | Place in family order | _Anak ke_ → `Observation.valueInteger` (148, tanpa BQ) |
| 10 | 156–166 | Observation | 57715-5 | Birth time | _Jam Lahir_ → `Observation.valueTime` (159, tanpa BQ) |
| 11 | 168–208 | Observation | 76516-4 | Gestational age—​at birth | _Usia Gestasi Saat Lahir_ → `Observation.valueQuantity.value` (171, tanpa BQ)<br>_Golongan darah_ → `Observation` (183, tanpa BQ)<br>_Rhesus_ → `Observation` (197, tanpa BQ) |
| 12 | 209–220 | Observation | 8339-4 | Birth weight Measured | _Berat Badan Saat Lahir (gram)_ → `Observation.valueQuantity.value` (212, tanpa BQ) |
| 13 | 221–232 | Observation | 89269-5 | Body height Measured --at birth | _Panjang Badan Saat Lahir_ → `Observation.valueQuantity.value` (224, tanpa BQ) |
| 14 | 233–244 | Observation | 8290-9 | Head Occipital-frontal circumference --at birth- by Tape measure | _Lingkar Kepala Saat Lahir_ → `Observation.valueQuantity.value` (236, tanpa BQ) |
| 15 | 245–269 | Observation | 9272-6 | 1 minute Apgar Score | _APGAR menit ke-1_ → `Observation.valueRange.low.value` (250, tanpa BQ) |
| 16 | 270–294 | Observation | 9274-2 | 5 minute Apgar Score | _APGAR menit ke-5_ → `Observation.valueRange.low.value` (275, tanpa BQ) |
| 17 | 295–319 | Observation | 9271-8 | 10 minute Apgar Score | _APGAR menit ke-10_ → `Observation.valueRange.low.value` (300, tanpa BQ) |
| 18 | 320–342 | Observation | 276654001 | Congenital malformation | _Kelainan Bawaan_ → `Observation.valueString` (323, tanpa BQ) |
| 19 | 343–354 | Observation | 8867-4 | Heart rate | _Frekuensi Denyut Jantung_ → `Observation.valueQuantity.value` (346, tanpa BQ) |
| 20 | 355–365 | Observation | 8310-5 | Body temperature | _Suhu_ → `Observation.valueQuantity.value` (358, tanpa BQ) |
| 21 | 366–376 | Observation | 9279-1 | Respiratory rate | _Pernapasan_ → `Observation.valueQuantity.value` (369, tanpa BQ) |
| 22 | 377–387 | Procedure | 386412000 | Resuscitation of neonate | _Apakah Diberikan Resusitasi_ → `Procedure.category.coding` (377, tanpa BQ) |
| 23 | 388–398 | Procedure | PC000003 | Manajemen Terpadu Bayi Muda (MTBM) | _Apakah dilakukan pemeriksaan kesehatan dengan pendekatan MTBM_ → `Procedure.category.coding` (388, tanpa BQ) |
| 24 | 399–409 | Procedure | SP000126 | ARV Profilaksis | _ARV Profilaksis pada bayi baru lahir_ → `Procedure.category.coding` (399, tanpa BQ) |
| 25 | 410–420 | Procedure | 448883004 | Injection of vitamin K1 | _Apakah diberikan vitamin K_ → `Procedure.category.coding` (410, tanpa BQ) |
| 26 | 421–431 | Procedure | PC000001 | Perawatan Tali Pusat | _Perawatan Tali Pusat_ → `Procedure.category.coding` (421, tanpa BQ) |
| 27 | 432–442 | Procedure | PC000002 | Pemberian Salep Antibiotik Mata | _Salep Antibiotik Mata_ → `Procedure.category.coding` (432, tanpa BQ) |
| 28 | 443–469 | Immunization | – | – | _Imunisasi Hepatitis B (HB0)_ → `Immunization.status` (443, tanpa BQ)<br>_Jika Tidak Imunisasi Hepatitis B(HB0)_ → `Immunization.statusReason.coding` (460, tanpa BQ)<br>_Hepatitis B Immunoglobulin (HBIG)_ → `Immunization.status` (467, tanpa BQ) |
| 29 | 470–490 | Immunization | – | – | – |
| 30 | 491–501 | Procedure | 431868002 | Initiation of breastfeeding | _Inisiasi Menyusu Dini (IMD)_ → `Procedure.category.coding` (491, tanpa BQ) |
| 31 | 502–513 | Observation | OC000016 | Waktu Inisiasi Menyusui Dini | _Waktu Inisiasi Menyusu Dini (IMD)_ → `Observation.valueCodeableConcept.coding` (505, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 14 |
| Procedure | 7 |
| RelatedPerson | 2 |
| Immunization | 2 |
| Patient | 1 |
| Practitioner | 1 |
| PractitionerRole | 1 |
| Encounter | 1 |
| Condition | 1 |
| EpisodeOfCare | 1 |
| **Total** | **31** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 96 | PractitionerRole | `PractitionerRole.code.coding` | 309453006 | Registered midwife | http://snomed.info/sct |
| 2 | 97 | PractitionerRole | `PractitionerRole.code.coding` | 309367003 | Obstetrician and gynecologist | http://snomed.info/sct |
| 3 | 98 | PractitionerRole | `PractitionerRole.code.coding` | 309343006 | Physician | http://snomed.info/sct |
| 4 | 99 | PractitionerRole | `PractitionerRole.code.coding` | 224535009 | Registered nurse | http://snomed.info/sct |
| 5 | 100 | PractitionerRole | `PractitionerRole.code.coding` | 82296001 | Pediatrician | http://snomed.info/sct |
| 6 | 120 | Condition | `Condition.code.coding` | Z00.1 | Routine child health examination | http://hl7.org/fhir/sid/icd-10 |
| 7 | 137 | EpisodeOfCare | `EpisodeOfCare.type.coding` | Neonate | Neonate | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 8 | 147 | Observation | `Observation.code.coding` | 365475008 | Place in family order | http://snomed.info/sct |
| 9 | 158 | Observation | `Observation.code.coding` | 57715-5 | Birth time | http://loinc.org |
| 10 | 170 | Observation | `Observation.code.coding` | 76516-4 | Gestational age—​at birth | http://loinc.org |
| 11 | 173 | Observation | `Observation.component.code.coding` | SP000398 | Usia Kehamilan Saat Persalinan (hari) | http://terminology.kemkes.go.id/sp |
| 12 | 211 | Observation | `Observation.code.coding` | 8339-4 | Birth weight Measured | http://loinc.org |
| 13 | 223 | Observation | `Observation.code.coding` | 89269-5 | Body height Measured --at birth | http://loinc.org |
| 14 | 235 | Observation | `Observation.code.coding` | 8290-9 | Head Occipital-frontal circumference --at birth- by Tape measure | http://loinc.org |
| 15 | 247 | Observation | `Observation.code.coding` | 9272-6 | 1 minute Apgar Score | http://loinc.org |
| 16 | 248 | Observation | `Observation.interpretation.coding` | 57284007 | Severe birth asphyxia | http://snomed.info/sct |
| 17 | 253 | Observation | `Observation.interpretation.coding` | 77362009 | Mild to moderate birth asphyxia | http://snomed.info/sct |
| 18 | 258 | Observation | `Observation.interpretation.coding` | 275307002 | Apgar normal | http://snomed.info/sct |
| 19 | 272 | Observation | `Observation.code.coding` | 9274-2 | 5 minute Apgar Score | http://loinc.org |
| 20 | 273 | Observation | `Observation.interpretation.coding` | 57284007 | Severe birth asphyxia | http://snomed.info/sct |
| 21 | 278 | Observation | `Observation.interpretation.coding` | 77362009 | Mild to moderate birth asphyxia | http://snomed.info/sct |
| 22 | 283 | Observation | `Observation.interpretation.coding` | 275307002 | Apgar normal | http://snomed.info/sct |
| 23 | 297 | Observation | `Observation.code.coding` | 9271-8 | 10 minute Apgar Score | http://loinc.org |
| 24 | 298 | Observation | `Observation.interpretation.coding` | 57284007 | Severe birth asphyxia | http://snomed.info/sct |
| 25 | 303 | Observation | `Observation.interpretation.coding` | 77362009 | Mild to moderate birth asphyxia | http://snomed.info/sct |
| 26 | 308 | Observation | `Observation.interpretation.coding` | 275307002 | Apgar normal | http://snomed.info/sct |
| 27 | 322 | Observation | `Observation.code.coding` | 276654001 | Congenital malformation | http://snomed.info/sct |
| 28 | 324 | Observation | `Observation.valueCodeableConcept.coding` | 80281008 | Cleft lip | http://snomed.info/sct |
| 29 | 325 | Observation | `Observation.valueCodeableConcept.coding` | 13213009 | Congenital heart disease | http://snomed.info/sct |
| 30 | 326 | Observation | `Observation.valueCodeableConcept.coding` | 35045004 | Microtia | http://snomed.info/sct |
| 31 | 327 | Observation | `Observation.valueCodeableConcept.coding` | 22006008 | Hypertelorism | http://snomed.info/sct |
| 32 | 328 | Observation | `Observation.valueCodeableConcept.coding` | 367506006 | Polydactyly | http://snomed.info/sct |
| 33 | 329 | Observation | `Observation.valueCodeableConcept.coding` | 52781008 | Congenital hip dysplasia | http://snomed.info/sct |
| 34 | 330 | Observation | `Observation.valueCodeableConcept.coding` | 1156475005 | Congenital talipes equinovarus | http://snomed.info/sct |
| 35 | 331 | Observation | `Observation.valueCodeableConcept.coding` | 253098009 | Neural tube defect | http://snomed.info/sct |
| 36 | 332 | Observation | `Observation.valueCodeableConcept.coding` | 118928003 | Disorder of abdominal wall | http://snomed.info/sct |
| 37 | 333 | Observation | `Observation.valueCodeableConcept.coding` | 42030000 | Disorder of the genitourinary system | http://snomed.info/sct |
| 38 | 334 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 39 | 345 | Observation | `Observation.code.coding` | 8867-4 | Heart rate | http://loinc.org |
| 40 | 357 | Observation | `Observation.code.coding` | 8310-5 | Body temperature | http://loinc.org |
| 41 | 368 | Observation | `Observation.code.coding` | 9279-1 | Respiratory rate | http://loinc.org |
| 42 | 380 | Procedure | `Procedure.code.coding` | 386412000 | Resuscitation of neonate | http://snomed.info/sct |
| 43 | 391 | Procedure | `Procedure.code.coding` | PC000003 | Manajemen Terpadu Bayi Muda (MTBM) | http://terminology.kemkes.go.id/CodeSystem/clinical-term" |
| 44 | 402 | Procedure | `Procedure.code.coding` | SP000126 | ARV Profilaksis | http://terminology.kemkes.go.id/sp |
| 45 | 413 | Procedure | `Procedure.code.coding` | 448883004 | Injection of vitamin K1 | http://snomed.info/sct |
| 46 | 424 | Procedure | `Procedure.code.coding` | PC000001 | Perawatan Tali Pusat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 47 | 435 | Procedure | `Procedure.code.coding` | PC000002 | Pemberian Salep Antibiotik Mata | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 48 | 446 | Immunization | `Immunization.vaccineCode` | 8 | Hep B, adolescent or pediatric | http://hl7.org/fhir/sid/cvx |
| 49 | 447 | Immunization | `Immunization.vaccineCode` | VG45 | HepB | http://sys-ids.kemkes.go.id/kfa |
| 50 | 470 | Immunization | `Immunization.vaccineCode` | VG45 | HepB | http://sys-ids.kemkes.go.id/kfa |
| 51 | 471 | Immunization | `Immunization.vaccineCode` | 30 | hepatitis B immune globulin | http://hl7.org/fhir/sid/cvx |
| 52 | 494 | Procedure | `Procedure.code.coding` | 431868002 | Initiation of breastfeeding | http://snomed.info/sct |
| 53 | 504 | Observation | `Observation.code.coding` | OC000016 | Waktu Inisiasi Menyusui Dini | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 54 | 505 | Observation | `Observation.valueCodeableConcept.coding` | OV000014 | Kurang dari 1 Jam | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 55 | 506 | Observation | `Observation.valueCodeableConcept.coding` | OV000015 | Lebih dari 1 Jam | http://terminology.kemkes.go.id/CodeSystem/clinical-term |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 30 |
| http://loinc.org | 11 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 5 |
| http://terminology.kemkes.go.id/sp | 2 |
| http://hl7.org/fhir/sid/cvx | 2 |
| http://sys-ids.kemkes.go.id/kfa | 2 |
| http://hl7.org/fhir/sid/icd-10 | 1 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 1 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term" | 1 |
| **Total** | **55** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 51 | – | Faskes yang Melayani INC | Organization | `Organization.name` |
