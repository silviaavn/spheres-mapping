# Output Form: Kobo Buku KIA 5 - Vaksinatorku

Sumber: `mapping/phdt-data-dictionary-kobo-kia5-vaksinator.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-kobo-kia5-vaksinator.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 40 |
| Code (`jumlah code` = 1) | 65 |
| Code unik (code + CodeSystem) | 27 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 13 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–6 | PractitionerRole | – | – | _Siapa yang melakukan entry data?_ → `PractitionerRole.active` (2, tanpa BQ) |
| 2 | 7–10 | Practitioner | – | – | _Nama lengkap tenaga kesehatan yang memberikan pelayanan kesehatan_ → `Practitioner.name.text` (7, tanpa BQ)<br>_ID tenaga kesehatan yang memberikan pelayanan kesehatan_ → `Practitioner.identifier` (8, tanpa BQ)<br>_ID SID staff yang melakukan entry data_ → `Practitioner.identifier` (9, tanpa BQ)<br>_ID SID field staff yang mengumpulkan form_ → `Practitioner.identifier` (10, tanpa BQ) |
| 3 | 11–55 | Patient | – | – | _Nama depan anak_ → `Patient.name.text` (11, tanpa BQ)<br>_Nama belakang anak_ → `Patient.name.text` (12, tanpa BQ)<br>_Tulis nomor ID anak_ → `Patient.identifier.value` (15, tanpa BQ)<br>_Tentukan tanggal lahir anak_ → `Patient.birthDate` (18, tanpa BQ)<br>_Alamat rumah/Asal Provinsi_ → `Patient.address.extension.extension.valueCode` (21, tanpa BQ)<br>_Alamat rumah/Asal Kabupaten_ → `Patient.address.extension.extension.valueCode` (24, tanpa BQ)<br>_Alamat rumah/Asal Kecamatan_ → `Patient.address.extension.extension.valueCode` (28, tanpa BQ)<br>_Kelurahan_ → `Patient.address.extension.extension.valueCode` (31, tanpa BQ)<br>_Alamat rumah/RW_ → `Patient.address.extension.extension.valueCode` (34, tanpa BQ)<br>_Alamat rumah/RT_ → `Patient.address.extension.extension.valueCode` (37, tanpa BQ)<br>__Tautan GPS rumah_latitude_ → `Patient.address.extension.extension.valueCode` (41, tanpa BQ)<br>__Tautan GPS rumah_longitude_ → `Patient.address.extension.extension.valueCode` (44, tanpa BQ)<br>__Tautan GPS rumah_altitude_ → `Patient.address.extension.extension.valueCode` (47, tanpa BQ)<br>_Alamat rumah/Nama jalan dan nomor rumah (jika ada)_ → `Patient.address.line` (50, tanpa BQ)<br>_Nomor telepon Ibu_ → `Patient.telecom` (53, tanpa BQ)<br>_Nomor telepon ibu (tulis kedua kali)_ → `Patient.telecom.value` (55, tanpa BQ) |
| 4 | 60–60 | RelatedPerson | – | – | _Nama depan ibu_ → `RelatedPerson.name.text` (60, tanpa BQ) |
| 5 | 61–70 | RelatedPerson | – | – | _Nama belakang ibu_ → `RelatedPerson.name.text` (61, tanpa BQ)<br>_Tulis Nomor Induk Kependudukan ibu (NIK)_ → `RelatedPerson.identifier.use` (65, tanpa BQ)<br>_Tulis Nomor Induk Kependudukan ibu (NIK) (Tulis kedua kali)_ → `RelatedPerson.identifier.value` (67, tanpa BQ)<br>_Nomor telepon Ibu_ → `RelatedPerson.telecom.use` (68, tanpa BQ)<br>_Nomor telepon ibu (tulis kedua kali)_ → `RelatedPerson.telecom.value` (70, tanpa BQ) |
| 6 | 76–76 | RelatedPerson | – | – | _Nama ayah_ → `RelatedPerson.name.text` (76, tanpa BQ) |
| 7 | 77–80 | RelatedPerson | – | – | _Nama belakang ayah_ → `RelatedPerson.name.text` (77, tanpa BQ) |
| 8 | 81–96 | DocumentReference | – | – | _Link File Original_ → `DocumentReference.identifier` (81, tanpa BQ) |
| 9 | 97–109 | Encounter | – | – | _Tanggal diberikan vaksin_ → `Encounter.period.start` (104, tanpa BQ) |
| 10 | 110–116 | Condition | Z26.9 | Need for immunization against unspecified infectious disease | – |
| 11 | 128–140 | Observation | SP000402 | Kepemilikan Nomor Induk Kependudukan | _Apakah ibu mempunyai nomor KTP (NIK)_ → `Observation.valueBoolean` (131, tanpa BQ) |
| 12 | 141–154 | Observation | SP000403 | Alasan Tidak Ada Nomor Induk Kependudukan | _Pilih alasan tidak mempunyai Nomor Induk Kependudukan (NIK)_ → `Observation.valueCodeableConcept.coding` (144, tanpa BQ) |
| 13 | 155–166 | Observation | SP000402 | Kepemilikan Nomor Induk Kependudukan | _Nomor ID anak_ → `Observation.valueBoolean` (158, tanpa BQ) |
| 14 | 167–182 | Observation | SP000403 | Alasan Tidak Ada Nomor Induk Kependudukan | _Alasan tidak ada ID anak_ → `Observation.valueCodeableConcept.coding` (170, tanpa BQ)<br>_Sebutkan alasan lainnya_ → `Observation.valueCodeableConcept.text` (175, tanpa BQ) |
| 15 | 203–214 | Observation | 424144002.0 | Current chronological age | _Isi usia anak dalam minggu_ → `Observation.valueQuantity.value` (206, tanpa BQ) |
| 16 | 215–228 | Immunization | VG45 | HepB | _Diberikan vaksin Hepatitis B (<24 jam)?_ → `Immunization.vaccineCode.coding` (215, tanpa BQ)<br>_Tanggal diberikan vaksin Hepatitis B (<24 jam)_ → `Immunization.occurrenceDateTime` (219, tanpa BQ) |
| 17 | 229–242 | Immunization | VG19 | BCG | _Diberikan vaksin BCG?_ → `Immunization.vaccineCode.coding` (229, tanpa BQ)<br>_Tanggal diberikan vaksin BCG_ → `Immunization.occurrenceDateTime` (233, tanpa BQ) |
| 18 | 243–258 | Immunization | VG89 | POLIO | _Diberikan vaksin Polio tetes 1?_ → `Immunization.vaccineCode.coding` (243, tanpa BQ)<br>_Tanggal diberikan vaksin Polio tetes 1_ → `Immunization.occurrenceDateTime` (249, tanpa BQ) |
| 19 | 259–276 | Immunization | – | – | _Diberikan vaksin DPT-HB-Hib 1?_ → `Immunization.vaccineCode` (259, tanpa BQ)<br>_Tanggal diberikan vaksin DPT-HB-Hib 1_ → `Immunization.occurrenceDateTime` (267, tanpa BQ) |
| 20 | 277–292 | Immunization | VG89 | POLIO | _Diberikan vaksin Polio tetes 2?_ → `Immunization.vaccineCode.coding` (277, tanpa BQ)<br>_Tanggal diberikan vaksin Polio tetes 2_ → `Immunization.occurrenceDateTime` (283, tanpa BQ) |
| 21 | 293–307 | Immunization | VG122 | ROTAVIRUS | _Diberikan vaksin Rota Virus (RV)1*?_ → `Immunization.vaccineCode.coding` (293, tanpa BQ)<br>_Tanggal diberikan vaksin Rota Virus (RV)1*_ → `Immunization.occurrenceDateTime` (298, tanpa BQ) |
| 22 | 308–322 | Immunization | VG152 | PneumoPCV | _Diberikan vaksin PCV 1?_ → `Immunization.vaccineCode.coding` (308, tanpa BQ)<br>_Tanggal diberikan vaksin PCV 1_ → `Immunization.occurrenceDateTime` (313, tanpa BQ) |
| 23 | 323–340 | Immunization | – | – | _Diberikan vaksin DPT-HB-Hib 2?_ → `Immunization.vaccineCode` (323, tanpa BQ)<br>_Tanggal diberikan vaksin DPT-HB-Hib 2_ → `Immunization.occurrenceDateTime` (331, tanpa BQ) |
| 24 | 341–356 | Immunization | VG89 | POLIO | _Diberikan vaksin Polio tetes 3?_ → `Immunization.vaccineCode.coding` (341, tanpa BQ)<br>_Tanggal diberikan vaksin Polio tetes 3_ → `Immunization.occurrenceDateTime` (347, tanpa BQ) |
| 25 | 357–371 | Immunization | VG122 | ROTAVIRUS | _Diberikan vaksin Rota Virus (RV)2*?_ → `Immunization.vaccineCode.coding` (357, tanpa BQ)<br>_Tanggal diberikan vaksin Rota Virus (RV)2*_ → `Immunization.occurrenceDateTime` (362, tanpa BQ) |
| 26 | 372–386 | Immunization | VG152 | PneumoPCV | _Diberikan vaksin PCV 2?_ → `Immunization.vaccineCode.coding` (372, tanpa BQ)<br>_Tanggal diberikan vaksin PCV 2_ → `Immunization.occurrenceDateTime` (377, tanpa BQ) |
| 27 | 387–404 | Immunization | – | – | _Diberikan vaksin DPT-HB-Hib 3?_ → `Immunization.vaccineCode` (387, tanpa BQ)<br>_Tanggal diberikan vaksin DPT-HB-Hib 3_ → `Immunization.occurrenceDateTime` (395, tanpa BQ) |
| 28 | 405–420 | Immunization | VG89 | POLIO | _Diberikan vaksin Polio tetes 4?_ → `Immunization.vaccineCode.coding` (405, tanpa BQ)<br>_Tanggal diberikan vaksin Polio tetes 4_ → `Immunization.occurrenceDateTime` (411, tanpa BQ) |
| 29 | 421–436 | Immunization | VG89 | POLIO | _Diberikan vaksin Polio Suntik (IPV) 1?_ → `Immunization.vaccineCode.coding` (421, tanpa BQ)<br>_Tanggal diberikan vaksin Polio Suntik (IPV) 1_ → `Immunization.occurrenceDateTime` (427, tanpa BQ) |
| 30 | 437–451 | Immunization | VG122 | ROTAVIRUS | _Diberikan vaksin Rota Virus (RV)3*?_ → `Immunization.vaccineCode.coding` (437, tanpa BQ)<br>_Tanggal diberikan vaksin Rota Virus (RV)3*_ → `Immunization.occurrenceDateTime` (442, tanpa BQ) |
| 31 | 452–467 | Immunization | VG03 | MMR | _Diberikan vaksin Campak-Rubella (MR)?_ → `Immunization.vaccineCode.coding` (452, tanpa BQ)<br>_Tanggal diberikan vaksin Campak-Rubella (MR)_ → `Immunization.occurrenceDateTime` (458, tanpa BQ) |
| 32 | 468–483 | Immunization | VG89 | POLIO | _Diberikan vaksin Polio Suntik (IPV) 2?_ → `Immunization.vaccineCode.coding` (468, tanpa BQ)<br>_Tanggal diberikan vaksin Polio Suntik (IPV) 2_ → `Immunization.occurrenceDateTime` (474, tanpa BQ) |
| 33 | 484–497 | Immunization | VG129 | Japanese encephalitis | _Diberikan vaksin *Japanese Encephalitis (JE)?_ → `Immunization.vaccineCode.coding` (484, tanpa BQ)<br>_Tanggal diberikan vaksin *Japanese Encephalitis (JE)_ → `Immunization.occurrenceDateTime` (488, tanpa BQ) |
| 34 | 498–512 | Immunization | VG152 | PneumoPCV | _Diberikan vaksin PCV 3?_ → `Immunization.vaccineCode.coding` (498, tanpa BQ)<br>_Tanggal diberikan vaksin PCV 3_ → `Immunization.occurrenceDateTime` (503, tanpa BQ) |
| 35 | 513–530 | Immunization | – | – | _Diberikan vaksin DPT-HB-Hib Lanjutan?_ → `Immunization.vaccineCode` (513, tanpa BQ)<br>_Tanggal diberikan vaksin DPT-HB-Hib Lanjutan_ → `Immunization.occurrenceDateTime` (521, tanpa BQ) |
| 36 | 531–546 | Immunization | VG03 | MMR | _Diberikan vaksin Campak-Rubella (MR) Lanjutan?_ → `Immunization.vaccineCode.coding` (531, tanpa BQ)<br>_Tanggal diberikan vaksin Campak-Rubella (MR) Lanjutan_ → `Immunization.occurrenceDateTime` (537, tanpa BQ) |
| 37 | 549–562 | Immunization | 787859002.0 | Vaccine product | _Tulis vaksin lain 1_ → `Immunization.vaccineCode.text` (550, tanpa BQ)<br>_Tanggal diberikan vaksin lain 1_ → `Immunization.occurrenceDateTime` (553, tanpa BQ) |
| 38 | 563–576 | Immunization | 787859002.0 | Vaccine product | _Tulis vaksin lain 2_ → `Immunization.vaccineCode.text` (564, tanpa BQ)<br>_Tanggal diberikan vaksin lain 2_ → `Immunization.occurrenceDateTime` (567, tanpa BQ) |
| 39 | 577–590 | Immunization | 787859002.0 | Vaccine product | _Tulis vaksin lain 3_ → `Immunization.vaccineCode.text` (578, tanpa BQ)<br>_Tanggal diberikan vaksin lain 3_ → `Immunization.occurrenceDateTime` (581, tanpa BQ) |
| 40 | 591–604 | Immunization | 787859002.0 | Vaccine product | _Tulis vaksin lain 4_ → `Immunization.vaccineCode.text` (592, tanpa BQ)<br>_Tanggal diberikan vaksin lain 4_ → `Immunization.occurrenceDateTime` (595, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Immunization | 25 |
| Observation | 5 |
| RelatedPerson | 4 |
| PractitionerRole | 1 |
| Practitioner | 1 |
| Patient | 1 |
| DocumentReference | 1 |
| Encounter | 1 |
| Condition | 1 |
| **Total** | **40** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 3 | PractitionerRole | `PractitionerRole.code.coding` | 223366009.0 | Healthcare professional | http://snomed.info/sct |
| 2 | 4 | PractitionerRole | `PractitionerRole.code.coding` | SP000396 | Data entry staff | http://terminology.kemkes.go.id/sp |
| 3 | 5 | PractitionerRole | `PractitionerRole.code.coding` | SP000397 | Field/call center staff | http://terminology.kemkes.go.id/sp |
| 4 | 95 | DocumentReference | `DocumentReference.content.format` | SP000732 | Buku KIA | http://terminology.kemkes.go.id/sp |
| 5 | 112 | Condition | `Condition.code.coding` | Z26.9 | Need for immunization against unspecified infectious disease | http://hl7.org/fhir/sid/icd-10 |
| 6 | 130 | Observation | `Observation.code.coding` | SP000402 | Kepemilikan Nomor Induk Kependudukan | http://terminology.kemkes.go.id/sp |
| 7 | 143 | Observation | `Observation.code.coding` | SP000403 | Alasan Tidak Ada Nomor Induk Kependudukan | http://terminology.kemkes.go.id/sp |
| 8 | 144 | Observation | `Observation.valueCodeableConcept.coding` | SP000404 | Tidak Punya Kartu Tanda Penduduk | http://terminology.kemkes.go.id/sp |
| 9 | 145 | Observation | `Observation.valueCodeableConcept.coding` | SP000405 | Tidak Membawa Kartu Tanda Penduduk | http://terminology.kemkes.go.id/sp |
| 10 | 146 | Observation | `Observation.valueCodeableConcept.coding` | SP000406 | Kartu Tanda Penduduk Hilang | http://terminology.kemkes.go.id/sp |
| 11 | 147 | Observation | `Observation.valueCodeableConcept.coding` | 397644002.0 | Right to privacy maintained | http://snomed.info/sct |
| 12 | 148 | Observation | `Observation.valueCodeableConcept.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 13 | 157 | Observation | `Observation.code.coding` | SP000402 | Kepemilikan Nomor Induk Kependudukan | http://terminology.kemkes.go.id/sp |
| 14 | 169 | Observation | `Observation.code.coding` | SP000403 | Alasan Tidak Ada Nomor Induk Kependudukan | http://terminology.kemkes.go.id/sp |
| 15 | 170 | Observation | `Observation.valueCodeableConcept.coding` | SP000404 | Tidak Punya Kartu Tanda Penduduk | http://terminology.kemkes.go.id/sp |
| 16 | 171 | Observation | `Observation.valueCodeableConcept.coding` | SP000405 | Tidak Membawa Kartu Tanda Penduduk | http://terminology.kemkes.go.id/sp |
| 17 | 172 | Observation | `Observation.valueCodeableConcept.coding` | SP000406 | Kartu Tanda Penduduk Hilang | http://terminology.kemkes.go.id/sp |
| 18 | 173 | Observation | `Observation.valueCodeableConcept.coding` | 397644002.0 | Right to privacy maintained | http://snomed.info/sct |
| 19 | 174 | Observation | `Observation.valueCodeableConcept.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 20 | 205 | Observation | `Observation.code.coding` | 424144002.0 | Current chronological age | http://snomed.info/sct |
| 21 | 215 | Immunization | `Immunization.vaccineCode.coding` | VG45 | HepB | http://sys-ids.kemkes.go.id/kfa |
| 22 | 229 | Immunization | `Immunization.vaccineCode.coding` | VG19 | BCG | http://sys-ids.kemkes.go.id/kfa |
| 23 | 243 | Immunization | `Immunization.vaccineCode.coding` | VG89 | POLIO | http://sys-ids.kemkes.go.id/kfa |
| 24 | 244 | Immunization | `Immunization.vaccineCode.coding` | 178.0 | OPV bivalent | http://hl7.org/fhir/sid/cvx |
| 25 | 259 | Immunization | `Immunization.vaccineCode` | 198.0 | DTP-hepB-Hib Pentavalent Non-US | http://hl7.org/fhir/sid/cvx |
| 26 | 260 | Immunization | `Immunization.vaccineCode` | VG107 | DTAP | http://sys-ids.kemkes.go.id/kfa |
| 27 | 261 | Immunization | `Immunization.vaccineCode` | VG45 | HepB | http://sys-ids.kemkes.go.id/kfa |
| 28 | 262 | Immunization | `Immunization.vaccineCode` | VG17 | HIB | http://sys-ids.kemkes.go.id/kfa |
| 29 | 277 | Immunization | `Immunization.vaccineCode.coding` | VG89 | POLIO | http://sys-ids.kemkes.go.id/kfa |
| 30 | 278 | Immunization | `Immunization.vaccineCode.coding` | 178.0 | OPV bivalent | http://hl7.org/fhir/sid/cvx |
| 31 | 293 | Immunization | `Immunization.vaccineCode.coding` | VG122 | ROTAVIRUS | http://sys-ids.kemkes.go.id/kfa |
| 32 | 308 | Immunization | `Immunization.vaccineCode.coding` | VG152 | PneumoPCV | http://sys-ids.kemkes.go.id/kfa |
| 33 | 323 | Immunization | `Immunization.vaccineCode` | 198.0 | DTP-hepB-Hib Pentavalent Non-US | http://hl7.org/fhir/sid/cvx |
| 34 | 324 | Immunization | `Immunization.vaccineCode` | VG107 | DTAP | http://sys-ids.kemkes.go.id/kfa |
| 35 | 325 | Immunization | `Immunization.vaccineCode` | VG45 | HepB | http://sys-ids.kemkes.go.id/kfa |
| 36 | 326 | Immunization | `Immunization.vaccineCode` | VG17 | HIB | http://sys-ids.kemkes.go.id/kfa |
| 37 | 341 | Immunization | `Immunization.vaccineCode.coding` | VG89 | POLIO | http://sys-ids.kemkes.go.id/kfa |
| 38 | 342 | Immunization | `Immunization.vaccineCode.coding` | 178.0 | OPV bivalent | http://hl7.org/fhir/sid/cvx |
| 39 | 357 | Immunization | `Immunization.vaccineCode.coding` | VG122 | ROTAVIRUS | http://sys-ids.kemkes.go.id/kfa |
| 40 | 372 | Immunization | `Immunization.vaccineCode.coding` | VG152 | PneumoPCV | http://sys-ids.kemkes.go.id/kfa |
| 41 | 387 | Immunization | `Immunization.vaccineCode` | 198.0 | DTP-hepB-Hib Pentavalent Non-US | http://hl7.org/fhir/sid/cvx |
| 42 | 388 | Immunization | `Immunization.vaccineCode` | VG107 | DTAP | http://sys-ids.kemkes.go.id/kfa |
| 43 | 389 | Immunization | `Immunization.vaccineCode` | VG45 | HepB | http://sys-ids.kemkes.go.id/kfa |
| 44 | 390 | Immunization | `Immunization.vaccineCode` | VG17 | HIB | http://sys-ids.kemkes.go.id/kfa |
| 45 | 405 | Immunization | `Immunization.vaccineCode.coding` | VG89 | POLIO | http://sys-ids.kemkes.go.id/kfa |
| 46 | 406 | Immunization | `Immunization.vaccineCode.coding` | 178.0 | OPV bivalent | http://hl7.org/fhir/sid/cvx |
| 47 | 421 | Immunization | `Immunization.vaccineCode.coding` | VG89 | POLIO | http://sys-ids.kemkes.go.id/kfa |
| 48 | 422 | Immunization | `Immunization.vaccineCode.coding` | 10.0 | IPV | http://hl7.org/fhir/sid/cvx |
| 49 | 437 | Immunization | `Immunization.vaccineCode.coding` | VG122 | ROTAVIRUS | http://sys-ids.kemkes.go.id/kfa |
| 50 | 452 | Immunization | `Immunization.vaccineCode.coding` | VG03 | MMR | http://sys-ids.kemkes.go.id/kfa |
| 51 | 453 | Immunization | `Immunization.vaccineCode.coding` | 04 | M/R | http://hl7.org/fhir/sid/cvx |
| 52 | 468 | Immunization | `Immunization.vaccineCode.coding` | VG89 | POLIO | http://sys-ids.kemkes.go.id/kfa |
| 53 | 469 | Immunization | `Immunization.vaccineCode.coding` | 10.0 | IPV | http://hl7.org/fhir/sid/cvx |
| 54 | 484 | Immunization | `Immunization.vaccineCode.coding` | VG129 | Japanese encephalitis | http://sys-ids.kemkes.go.id/kfa |
| 55 | 498 | Immunization | `Immunization.vaccineCode.coding` | VG152 | PneumoPCV | http://sys-ids.kemkes.go.id/kfa |
| 56 | 513 | Immunization | `Immunization.vaccineCode` | 198.0 | DTP-hepB-Hib Pentavalent Non-US | http://hl7.org/fhir/sid/cvx |
| 57 | 514 | Immunization | `Immunization.vaccineCode` | VG107 | DTAP | http://sys-ids.kemkes.go.id/kfa |
| 58 | 515 | Immunization | `Immunization.vaccineCode` | VG45 | HepB | http://sys-ids.kemkes.go.id/kfa |
| 59 | 516 | Immunization | `Immunization.vaccineCode` | VG17 | HIB | http://sys-ids.kemkes.go.id/kfa |
| 60 | 531 | Immunization | `Immunization.vaccineCode.coding` | VG03 | MMR | http://sys-ids.kemkes.go.id/kfa |
| 61 | 532 | Immunization | `Immunization.vaccineCode.coding` | 04 | M/R | http://hl7.org/fhir/sid/cvx |
| 62 | 549 | Immunization | `Immunization.vaccineCode.coding` | 787859002.0 | Vaccine product | http://snomed.info/sct |
| 63 | 563 | Immunization | `Immunization.vaccineCode.coding` | 787859002.0 | Vaccine product | http://snomed.info/sct |
| 64 | 577 | Immunization | `Immunization.vaccineCode.coding` | 787859002.0 | Vaccine product | http://snomed.info/sct |
| 65 | 591 | Immunization | `Immunization.vaccineCode.coding` | 787859002.0 | Vaccine product | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://sys-ids.kemkes.go.id/kfa | 29 |
| http://terminology.kemkes.go.id/sp | 13 |
| http://hl7.org/fhir/sid/cvx | 12 |
| http://snomed.info/sct | 10 |
| http://hl7.org/fhir/sid/icd-10 | 1 |
| **Total** | **65** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 16 | – | Tanggal lahir anak diketahui | – | `` |
| 38 | – | Tautan GPS rumah | – | `` |
| 48 | – | _Tautan GPS rumah_precision | – | `` |
| 51 | – | Alamat rumah/Foto rumah | – | `` |
| 52 | – | Alamat rumah/Foto rumah_URL | – | `` |
| 56 | – | Alamat rumah/Asal Puskesmas | Organization | `Organization.name` |
| 71 | – | Apakah Ibu memiliki handphone? | – | `` |
| 73 | – | Alasan | – | `` |
| 183 | – | Jenis ID tambahan | – | `` |
| 184 | – | Nomor SID ID | – | `` |
| 185 | – | Nomor SID ID (tulis kedua kali) | – | `` |
| 186 | – | Jenis ID Ibu tambahan | – | `` |
| 187 | – | Nomor SID ID Ibu | – | `` |
| 188 | – | Nomor SID ID Ibu (tulis kedua kali) | – | `` |
| 547 | – | Diberikan vaksin lain? | – | `` |
