# Output Form: SIM RS Ummu Hani BBL

Sumber: `mapping/phdt-data-dictionary-rs-ummu-hani-bbl.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-rs-ummu-hani-bbl.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 30 |
| Code (`jumlah code` = 1) | 55 |
| Code unik (code + CodeSystem) | 51 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 2 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–28 | Patient | – | – | _Nama Bayi_ → `Patient.name.text` (2, tanpa BQ)<br>_NIK Bayi/ Ibu_ → `Patient.identifier.value` (4, tanpa BQ)<br>_No HP Orang Tua_ → `Patient.telecom` (8, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (11, tanpa BQ)<br>_Tempat Lahir_ → `Patient.extension.url` (12, tanpa BQ)<br>_Alamat Domisili_ → `Patient.address.line` (14, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (19, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (22, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.extension.valueCode` (25, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.extension.valueCode` (28, tanpa BQ) |
| 2 | 29–35 | RelatedPerson | – | – | _Nama Ibu_ → `RelatedPerson.name.text` (29, tanpa BQ)<br>_NIK Ibu_ → `RelatedPerson.identifier` (30, tanpa BQ) |
| 3 | 36–42 | RelatedPerson | – | – | _Nama Ayah_ → `RelatedPerson.name.text` (36, tanpa BQ)<br>_NIK Ayah_ → `RelatedPerson.identifier` (37, tanpa BQ) |
| 4 | 81–87 | Practitioner | – | – | _NIK_ → `Practitioner.identifier.value` (83, tanpa BQ)<br>_Nama Tenaga Kesehatan_ → `Practitioner.name.text` (85, tanpa BQ)<br>_Jenis Kelamin Tenaga Kesehatan_ → `Practitioner.gender` (86, tanpa BQ) |
| 5 | 88–96 | PractitionerRole | – | – | _Tenaga Pemeriksa_ → `PractitionerRole.code.coding` (92, tanpa BQ) |
| 6 | 98–113 | Encounter | – | – | _Kunjungan Neonatus_ → `Encounter.identifier` (99, tanpa BQ)<br>_Tanggal Kunjungan_ → `Encounter.period.start` (108, tanpa BQ)<br>_Tempat Pelayanan Kunjungan Neonatus/BBL_ → `Encounter.location.location.display` (111, tanpa BQ) |
| 7 | 114–121 | Condition | Z00.1 | Routine child health examination | – |
| 8 | 132–140 | EpisodeOfCare | Neonate | Neonate | – |
| 9 | 141–151 | Observation | 365475008 | Place in family order | _Anak ke_ → `Observation.valueInteger` (144, tanpa BQ) |
| 10 | 152–162 | Observation | 57715-5 | Birth time | _Jam Lahir_ → `Observation.valueTime` (155, tanpa BQ) |
| 11 | 163–177 | Observation | 76516-4 | Gestational age—​at birth | _Usia Gestasi Saat Lahir_ → `Observation.valueQuantity.value` (166, tanpa BQ) |
| 12 | 178–193 | Observation | 883-9 | ABO group [Type] in Blood | _Golongan darah_ → `Observation.valueCodeableConcept.coding` (181, tanpa BQ) |
| 13 | 194–207 | Observation | 10331-7 | Rh [Type] in Blood | _Rhesus_ → `Observation.valueCodeableConcept.coding` (197, tanpa BQ) |
| 14 | 208–219 | Observation | 8339-4 | Birth weight Measured | _Berat Badan Saat Lahir (gram)_ → `Observation.valueQuantity.value` (211, tanpa BQ) |
| 15 | 220–231 | Observation | 89269-5 | Body height Measured --at birth | _Panjang Badan Saat Lahir_ → `Observation.valueQuantity.value` (223, tanpa BQ) |
| 16 | 232–243 | Observation | 8290-9 | Head Occipital-frontal circumference --at birth- by Tape measure | _Lingkar Kepala Saat Lahir_ → `Observation.valueQuantity.value` (235, tanpa BQ) |
| 17 | 244–265 | Observation | 276654001 | Congenital malformation | _Kelainan Bawaan_ → `Observation.valueCodeableConcept.coding` (247, tanpa BQ) |
| 18 | 266–277 | Observation | 8867-4 | Heart rate | _Frekuensi Denyut Jantung_ → `Observation.valueQuantity.value` (269, tanpa BQ) |
| 19 | 278–288 | Observation | 8310-5 | Body temperature | _Suhu_ → `Observation.valueQuantity.value` (281, tanpa BQ) |
| 20 | 289–299 | Observation | 9279-1 | Respiratory rate | _Pernapasan_ → `Observation.valueQuantity.value` (292, tanpa BQ) |
| 21 | 300–310 | Procedure | 386412000 | Resuscitation of neonate | _Apakah Diberikan Resusitasi_ → `Procedure.category.coding` (300, tanpa BQ) |
| 22 | 311–321 | Procedure | PC000003 | Manajemen Terpadu Bayi Muda (MTBM) | _Apakah dilakukan pemeriksaan kesehatan dengan pendekatan MTBM_ → `Procedure.category.coding` (311, tanpa BQ) |
| 23 | 322–332 | Procedure | SP000126 | ARV Profilaksis | _ARV Profilaksis pada bayi baru lahir_ → `Procedure.category.coding` (322, tanpa BQ) |
| 24 | 333–343 | Procedure | 448883004 | Injection of vitamin K1 | _Apakah diberikan vitamin K_ → `Procedure.category.coding` (333, tanpa BQ) |
| 25 | 344–354 | Procedure | PC000001 | Perawatan Tali Pusat | _Perawatan Tali Pusat_ → `Procedure.category.coding` (344, tanpa BQ) |
| 26 | 355–365 | Procedure | PC000002 | Pemberian Salep Antibiotik Mata | _Salep Antibiotik Mata_ → `Procedure.category.coding` (355, tanpa BQ) |
| 27 | 366–393 | Immunization | – | – | _Imunisasi Hepatitis B (HB0)_ → `Immunization.status` (366, tanpa BQ)<br>_Jika Tidak Imunisasi Hepatitis B(HB0)_ → `Immunization.statusReason.coding` (383, tanpa BQ)<br>_Imunisasi HBIg_ → `Immunization.status` (391, tanpa BQ) |
| 28 | 394–405 | Immunization | – | – | – |
| 29 | 406–416 | Procedure | 431868002 | Initiation of breastfeeding | _Inisiasi Menyusu Dini (IMD)_ → `Procedure.category.coding` (406, tanpa BQ) |
| 30 | 417–428 | Observation | OC000016 | Waktu Inisiasi Menyusui Dini | _Waktu Inisiasi Menyusu Dini (IMD)_ → `Observation.valueCodeableConcept.coding` (420, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 13 |
| Procedure | 7 |
| RelatedPerson | 2 |
| Immunization | 2 |
| Patient | 1 |
| Practitioner | 1 |
| PractitionerRole | 1 |
| Encounter | 1 |
| Condition | 1 |
| EpisodeOfCare | 1 |
| **Total** | **30** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 92 | PractitionerRole | `PractitionerRole.code.coding` | 309453006 | Registered midwife | http://snomed.info/sct |
| 2 | 93 | PractitionerRole | `PractitionerRole.code.coding` | 309367003 | Obstetrician and gynecologist | http://snomed.info/sct |
| 3 | 94 | PractitionerRole | `PractitionerRole.code.coding` | 309343006 | Physician | http://snomed.info/sct |
| 4 | 95 | PractitionerRole | `PractitionerRole.code.coding` | 224535009 | Registered nurse | http://snomed.info/sct |
| 5 | 96 | PractitionerRole | `PractitionerRole.code.coding` | 82296001 | Pediatrician | http://snomed.info/sct |
| 6 | 116 | Condition | `Condition.code.coding` | Z00.1 | Routine child health examination | http://hl7.org/fhir/sid/icd-10 |
| 7 | 133 | EpisodeOfCare | `EpisodeOfCare.type.coding` | Neonate | Neonate | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 8 | 143 | Observation | `Observation.code.coding` | 365475008 | Place in family order | http://snomed.info/sct |
| 9 | 154 | Observation | `Observation.code.coding` | 57715-5 | Birth time | http://loinc.org |
| 10 | 165 | Observation | `Observation.code.coding` | 76516-4 | Gestational age—​at birth | http://loinc.org |
| 11 | 168 | Observation | `Observation.component.code.coding` | SP000398 | Usia Kehamilan Saat Persalinan (hari) | http://terminology.kemkes.go.id/sp |
| 12 | 180 | Observation | `Observation.code.coding` | 883-9 | ABO group [Type] in Blood | http://loinc.org |
| 13 | 181 | Observation | `Observation.valueCodeableConcept.coding` | LA19710-5 | Group A | http://loinc.org |
| 14 | 182 | Observation | `Observation.valueCodeableConcept.coding` | LA19709-7 | Group B | http://loinc.org |
| 15 | 183 | Observation | `Observation.valueCodeableConcept.coding` | LA19708-9 | Group O | http://loinc.org |
| 16 | 184 | Observation | `Observation.valueCodeableConcept.coding` | LA28449-9 | Group AB | http://loinc.org |
| 17 | 185 | Observation | `Observation.dataAbsentReason.coding` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 18 | 186 | Observation | `Observation.dataAbsentReason.coding` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 19 | 196 | Observation | `Observation.code.coding` | 10331-7 | Rh [Type] in Blood | http://loinc.org |
| 20 | 197 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 21 | 198 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 22 | 199 | Observation | `Observation.dataAbsentReason.coding` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 23 | 200 | Observation | `Observation.dataAbsentReason.coding` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 24 | 210 | Observation | `Observation.code.coding` | 8339-4 | Birth weight Measured | http://loinc.org |
| 25 | 222 | Observation | `Observation.code.coding` | 89269-5 | Body height Measured --at birth | http://loinc.org |
| 26 | 234 | Observation | `Observation.code.coding` | 8290-9 | Head Occipital-frontal circumference --at birth- by Tape measure | http://loinc.org |
| 27 | 246 | Observation | `Observation.code.coding` | 276654001 | Congenital malformation | http://snomed.info/sct |
| 28 | 247 | Observation | `Observation.valueCodeableConcept.coding` | 80281008 | Cleft lip | http://snomed.info/sct |
| 29 | 248 | Observation | `Observation.valueCodeableConcept.coding` | 13213009 | Congenital heart disease | http://snomed.info/sct |
| 30 | 249 | Observation | `Observation.valueCodeableConcept.coding` | 35045004 | Microtia | http://snomed.info/sct |
| 31 | 250 | Observation | `Observation.valueCodeableConcept.coding` | 22006008 | Hypertelorism | http://snomed.info/sct |
| 32 | 251 | Observation | `Observation.valueCodeableConcept.coding` | 367506006 | Polydactyly | http://snomed.info/sct |
| 33 | 252 | Observation | `Observation.valueCodeableConcept.coding` | 52781008 | Congenital hip dysplasia | http://snomed.info/sct |
| 34 | 253 | Observation | `Observation.valueCodeableConcept.coding` | 1156475005 | Congenital talipes equinovarus | http://snomed.info/sct |
| 35 | 254 | Observation | `Observation.valueCodeableConcept.coding` | 253098009 | Neural tube defect | http://snomed.info/sct |
| 36 | 255 | Observation | `Observation.valueCodeableConcept.coding` | 118928003 | Disorder of abdominal wall | http://snomed.info/sct |
| 37 | 256 | Observation | `Observation.valueCodeableConcept.coding` | 42030000 | Disorder of the genitourinary system | http://snomed.info/sct |
| 38 | 257 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 39 | 268 | Observation | `Observation.code.coding` | 8867-4 | Heart rate | http://loinc.org |
| 40 | 280 | Observation | `Observation.code.coding` | 8310-5 | Body temperature | http://loinc.org |
| 41 | 291 | Observation | `Observation.code.coding` | 9279-1 | Respiratory rate | http://loinc.org |
| 42 | 303 | Procedure | `Procedure.code.coding` | 386412000 | Resuscitation of neonate | http://snomed.info/sct |
| 43 | 314 | Procedure | `Procedure.code.coding` | PC000003 | Manajemen Terpadu Bayi Muda (MTBM) | http://terminology.kemkes.go.id/CodeSystem/clinical-term" |
| 44 | 325 | Procedure | `Procedure.code.coding` | SP000126 | ARV Profilaksis | http://terminology.kemkes.go.id/sp |
| 45 | 336 | Procedure | `Procedure.code.coding` | 448883004 | Injection of vitamin K1 | http://snomed.info/sct |
| 46 | 347 | Procedure | `Procedure.code.coding` | PC000001 | Perawatan Tali Pusat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 47 | 358 | Procedure | `Procedure.code.coding` | PC000002 | Pemberian Salep Antibiotik Mata | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 48 | 369 | Immunization | `Immunization.vaccineCode` | 8 | Hep B, adolescent or pediatric | http://hl7.org/fhir/sid/cvx |
| 49 | 370 | Immunization | `Immunization.vaccineCode` | VG45 | HepB | http://sys-ids.kemkes.go.id/kfa |
| 50 | 394 | Immunization | `Immunization.vaccineCode` | VG45 | HepB | http://sys-ids.kemkes.go.id/kfa |
| 51 | 395 | Immunization | `Immunization.vaccineCode` | 30 | hepatitis B immune globulin | http://hl7.org/fhir/sid/cvx |
| 52 | 409 | Procedure | `Procedure.code.coding` | 431868002 | Initiation of breastfeeding | http://snomed.info/sct |
| 53 | 419 | Observation | `Observation.code.coding` | OC000016 | Waktu Inisiasi Menyusui Dini | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 54 | 420 | Observation | `Observation.valueCodeableConcept.coding` | OV000014 | Kurang dari 1 Jam | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 55 | 421 | Observation | `Observation.valueCodeableConcept.coding` | OV000015 | Lebih dari 1 Jam | http://terminology.kemkes.go.id/CodeSystem/clinical-term |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 21 |
| http://loinc.org | 16 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 5 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 4 |
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
| 47 | – | Faskes yang Melayani Kunjungan Neonatus/BBL | Organization | `Organization.name` |
