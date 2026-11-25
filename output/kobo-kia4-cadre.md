# Output Form: Kobo Buku KIA 4 - Cadre

Sumber: `mapping/phdt-data-dictionary-kobo-kia4-cadre.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-kobo-kia4-cadre.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 44 |
| Code (`jumlah code` = 1) | 51 |
| Code unik (code + CodeSystem) | 50 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 15 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–13 | Observation | SP000395 | Pendaftaran Pertama Formulir KoBo | _Apakah ini pendaftaran di KoBo form pertama kali?_ → `Observation.valueBoolean` (5, tanpa BQ) |
| 2 | 14–18 | PractitionerRole | – | – | _Siapa yang melakukan entry data?_ → `PractitionerRole.active` (14, tanpa BQ) |
| 3 | 19–22 | Practitioner | – | – | _Nama lengkap tenaga kesehatan yang memberikan pelayanan kesehatan_ → `Practitioner.name.text` (19, tanpa BQ)<br>_ID tenaga kesehatan yang memberikan pelayanan kesehatan_ → `Practitioner.identifier` (20, tanpa BQ)<br>_ID SID staff yang melakukan entry data_ → `Practitioner.identifier` (21, tanpa BQ)<br>_ID SID field staff yang mengumpulkan form_ → `Practitioner.identifier` (22, tanpa BQ) |
| 4 | 23–23 | Practitioner | – | – | _Nama Depan Kader_ → `Practitioner.name.text` (23, tanpa BQ) |
| 5 | 24–24 | Practitioner | – | – | _Nama Belakang Kader_ → `Practitioner.name.text` (24, tanpa BQ) |
| 6 | 25–26 | PractitionerRole | – | – | – |
| 7 | 27–27 | RelatedPerson | – | – | _Nama Depan Ibu_ → `RelatedPerson.name.text` (27, tanpa BQ) |
| 8 | 28–38 | RelatedPerson | – | – | _Nama Belakang Ibu_ → `RelatedPerson.name.text` (28, tanpa BQ)<br>_Tulis nomor Induk Kependudukan (NIK) Ibu_ → `RelatedPerson.identifier.use` (32, tanpa BQ)<br>_Tulis nomor Induk Kependudukan (NIK) Ibu (tulis kedua kali)_ → `RelatedPerson.identifier.value` (34, tanpa BQ)<br>_Tanggal lahir Ibu_ → `RelatedPerson.birthDate` (35, tanpa BQ)<br>_Nomor telepon Ibu_ → `RelatedPerson.telecom.use` (36, tanpa BQ)<br>_Nomor telepon ibu (tulis kedua kali)_ → `RelatedPerson.telecom.value` (38, tanpa BQ) |
| 9 | 40–40 | RelatedPerson | – | – | _Nama Belakang Ayah_ → `RelatedPerson.name.text` (40, tanpa BQ) |
| 10 | 41–44 | RelatedPerson | – | – | – |
| 11 | 46–84 | Patient | – | – | _Nama Depan Bayi/Balita_ → `Patient.name.text` (46, tanpa BQ)<br>_Nama Belakang Bayi/Balita_ → `Patient.name.text` (47, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (48, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (53, tanpa BQ)<br>_Asal Provinsi_ → `Patient.address.extension.extension.valueCode` (55, tanpa BQ)<br>_Asal Kabupaten_ → `Patient.address.extension.extension.valueCode` (58, tanpa BQ)<br>_Asal Kecamatan_ → `Patient.address.extension.extension.valueCode` (62, tanpa BQ)<br>_Kelurahan_ → `Patient.address.extension.extension.valueCode` (65, tanpa BQ)<br>_RW_ → `Patient.address.extension.extension.valueCode` (68, tanpa BQ)<br>_RT_ → `Patient.address.extension.extension.valueCode` (71, tanpa BQ)<br>__Tautan GPS rumah_latitude_ → `Patient.address.extension.extension.valueCode` (75, tanpa BQ)<br>__Tautan GPS rumah_longitude_ → `Patient.address.extension.extension.valueCode` (78, tanpa BQ)<br>__Tautan GPS rumah_altitude_ → `Patient.address.extension.extension.valueCode` (81, tanpa BQ)<br>_Nama jalan dan nomor rumah (jika ada)_ → `Patient.address.line` (84, tanpa BQ) |
| 12 | 89–101 | Encounter | – | – | _Tanggal Posyandu_ → `Encounter.period.start` (96, tanpa BQ) |
| 13 | 102–108 | Condition | Z00.1 | Routine child health examination | – |
| 14 | 120–134 | Observation | 365552003 | Finding of income details | _Pendapatan per bulan keluarga_ → `Observation.valueCodeableConcept.coding` (123, tanpa BQ) |
| 15 | 135–147 | Observation | SP000402 | Kepemilikan Nomor Induk Kependudukan | _Apakah ibu mempunyai nomor KTP (NIK)_ → `Observation.valueBoolean` (138, tanpa BQ) |
| 16 | 148–161 | Observation | SP000403 | Alasan Tidak Ada Nomor Induk Kependudukan | _Pilih alasan tidak mempunyai Nomor Induk Kependudukan (NIK)_ → `Observation.valueCodeableConcept.coding` (151, tanpa BQ) |
| 17 | 162–173 | Observation | 424144002 | Current chronological age | _months_ → `Observation.valueQuantity.value` (165, tanpa BQ) |
| 18 | 174–185 | Observation | 8339-4 | Birth weight Measured | _Berat badan lahir_ → `Observation.valueQuantity.value` (177, tanpa BQ) |
| 19 | 186–196 | Observation | 365475008 | Place in family order | _Urutan anak ke_ → `Observation.valueInteger` (189, tanpa BQ) |
| 20 | 197–209 | Observation | 76516-4 | Gestational age—​at birth | _Usia kehamilan terakhir saat lahir_ → `Observation.valueQuantity.value` (200, tanpa BQ) |
| 21 | 210–222 | Observation | 8338-6 | Body weight Measured --ante partum | _Berat badan terakhir saat hamil_ → `Observation.valueQuantity.value` (213, tanpa BQ) |
| 22 | 223–234 | Observation | 1145307003 | Exclusively breastfed | _Pemberian ASI ekslusif_ → `Observation.valueBoolean` (226, tanpa BQ) |
| 23 | 236–247 | Observation | 8287-5 | Head Occipital-frontal circumference by Tape measure | _Lingkar Kepala_ → `Observation.valueQuantity.value` (239, tanpa BQ) |
| 24 | 248–257 | Procedure | 767224000 | Administration of vitamin A | _Apakah bayi/balita menerima Vitamin A saat posyandu?_ → `Procedure.category.coding` (248, tanpa BQ) |
| 25 | 258–269 | Observation | OC000164 | Jumlah kapsul vitamin A yang diberikan | _Berapa dosis Vitamin A yang diberikan saat posyandu?_ → `Observation.valueCodeableConcept.coding` (261, tanpa BQ) |
| 26 | 270–281 | Observation | SP000647 | Mendapatkan makanan tambahan | _Apakah bayi/balita menerima makanan tambahan saat posyandu?_ → `Observation.valueBoolean` (273, tanpa BQ) |
| 27 | 282–293 | Observation | 29463-7 | Body weight | _Berat Badan_ → `Observation.valueQuantity.value` (285, tanpa BQ) |
| 28 | 294–306 | Observation | 8308-9 | Body height --standing | _Panjang/Tinggi Badan Balita_ → `Observation.valueQuantity.value` (298, tanpa BQ) |
| 29 | 307–318 | Observation | 365856005 | Screening finding | _Hasil Skrining_ → `Observation.valueCodeableConcept.coding` (310, tanpa BQ) |
| 30 | 319–334 | Immunization | VG88 | FLU | _Jenis vaksin yang diberikan/Influenza_ → `Immunization.vaccineCode.coding` (321, tanpa BQ)<br>_Influenza dosis ke berapa?_ → `Immunization.protocolApplied.doseNumberPositiveInt` (322, tanpa BQ) |
| 31 | 335–348 | Immunization | VG129 | Japanese encephalitis | _Jenis vaksin yang diberikan/JE_ → `Immunization.vaccineCode.coding` (335, tanpa BQ)<br>_JE dosis ke berapa?_ → `Immunization.protocolApplied.doseNumberPositiveInt` (336, tanpa BQ) |
| 32 | 349–362 | Immunization | VG21 | VARICELLA | _Jenis vaksin yang diberikan/Varisela_ → `Immunization.vaccineCode.coding` (349, tanpa BQ)<br>_Varisela dosis ke berapa?_ → `Immunization.protocolApplied.doseNumberPositiveInt` (350, tanpa BQ) |
| 33 | 363–376 | Immunization | VG85 | HepA | _Jenis vaksin yang diberikan/Hepatitis A_ → `Immunization.vaccineCode.coding` (363, tanpa BQ)<br>_Hepatitis A dosis ke berapa?_ → `Immunization.protocolApplied.doseNumberPositiveInt` (364, tanpa BQ) |
| 34 | 377–390 | Immunization | VG91 | TYPHOID | _Jenis vaksin yang diberikan/Tifoid_ → `Immunization.vaccineCode.coding` (377, tanpa BQ)<br>_Tifoid dosis ke berapa?_ → `Immunization.protocolApplied.doseNumberPositiveInt` (378, tanpa BQ) |
| 35 | 391–404 | Immunization | 787859002 | Vaccine product | _Jenis vaksin yang diberikan/Lainnya_ → `Immunization.vaccineCode.coding` (391, tanpa BQ)<br>_Tulis jenis vaksin lainnya yang diberikan_ → `Immunization.vaccineCode.text` (392, tanpa BQ) |
| 36 | 405–417 | Immunization | VG19 | BCG | _Jenis vaksin yang diberikan/BCG_ → `Immunization.vaccineCode.coding` (405, tanpa BQ) |
| 37 | 418–439 | Immunization | VG45 | HepB | _Jenis vaksin yang diberikan/Hepatitis B_ → `Immunization.vaccineCode.coding` (418, tanpa BQ) |
| 38 | 440–461 | Immunization | VG89 | POLIO | _Jenis vaksin yang diberikan/Polio_ → `Immunization.vaccineCode.coding` (440, tanpa BQ)<br>_Polio dosis ke berapa?_ → `Immunization.protocolApplied.doseNumberPositiveInt` (441, tanpa BQ) |
| 39 | 462–483 | Immunization | VG107 | DTAP | _Jenis vaksin yang diberikan/DTP_ → `Immunization.vaccineCode.coding` (462, tanpa BQ)<br>_DTP dosis ke berapa?_ → `Immunization.protocolApplied.doseNumberPositiveInt` (463, tanpa BQ) |
| 40 | 484–503 | Immunization | VG17 | HIB | _Jenis vaksin yang diberikan/Hib_ → `Immunization.vaccineCode.coding` (484, tanpa BQ)<br>_Hib dosis ke berapa?_ → `Immunization.protocolApplied.doseNumberPositiveInt` (485, tanpa BQ) |
| 41 | 504–523 | Immunization | VG152 | PneumoPCV | _Jenis vaksin yang diberikan/PCV_ → `Immunization.vaccineCode.coding` (504, tanpa BQ)<br>_PCV dosis ke berapa?_ → `Immunization.protocolApplied.doseNumberPositiveInt` (505, tanpa BQ) |
| 42 | 524–541 | Immunization | VG122 | ROTAVIRUS | _Jenis vaksin yang diberikan/Rotavirus_ → `Immunization.vaccineCode.coding` (524, tanpa BQ)<br>_Rotavirus dosis ke berapa?_ → `Immunization.protocolApplied.doseNumberPositiveInt` (525, tanpa BQ) |
| 43 | 542–557 | Immunization | VG03 | MMR | _Jenis vaksin yang diberikan/MR/ MMR_ → `Immunization.vaccineCode.coding` (542, tanpa BQ)<br>_MR/ MMR dosis ke berapa?_ → `Immunization.protocolApplied.doseNumberPositiveInt` (543, tanpa BQ) |
| 44 | 558–568 | Immunization | 787859002 | Vaccine product | _Jenis vaksin yang diberikan/Tidak diberikan_ → `Immunization.vaccineCode.coding` (558, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 16 |
| Immunization | 15 |
| RelatedPerson | 4 |
| Practitioner | 3 |
| PractitionerRole | 2 |
| Patient | 1 |
| Encounter | 1 |
| Condition | 1 |
| Procedure | 1 |
| **Total** | **44** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 4 | Observation | `Observation.code.coding` | SP000395 | Pendaftaran Pertama Formulir KoBo | http://terminology.kemkes.go.id/sp |
| 2 | 15 | PractitionerRole | `PractitionerRole.code.coding` | 223366009 | Healthcare professional | http://snomed.info/sct |
| 3 | 16 | PractitionerRole | `PractitionerRole.code.coding` | SP000396 | Data entry staff | http://terminology.kemkes.go.id/sp |
| 4 | 17 | PractitionerRole | `PractitionerRole.code.coding` | SP000397 | Field/call center staff | http://terminology.kemkes.go.id/sp |
| 5 | 25 | PractitionerRole | `PractitionerRole.code` | SP000373 | Kader Kesehatan | http://terminology.kemkes.go.id/sp |
| 6 | 104 | Condition | `Condition.code.coding` | Z00.1 | Routine child health examination | http://hl7.org/fhir/sid/icd-10 |
| 7 | 122 | Observation | `Observation.code.coding` | 365552003 | Finding of income details | http://snomed.info/sct |
| 8 | 123 | Observation | `Observation.valueCodeableConcept.coding` | SP000654 | <Rp 1500000 | http://terminology.kemkes.go.id/sp |
| 9 | 124 | Observation | `Observation.valueCodeableConcept.coding` | SP000655 | Rp 1500000- Rp 2500000 | http://terminology.kemkes.go.id/sp |
| 10 | 125 | Observation | `Observation.valueCodeableConcept.coding` | SP000656 | Rp 2500001 - Rp 3500000 | http://terminology.kemkes.go.id/sp |
| 11 | 126 | Observation | `Observation.valueCodeableConcept.coding` | SP000657 | >Rp 3500000 | http://terminology.kemkes.go.id/sp |
| 12 | 137 | Observation | `Observation.code.coding` | SP000402 | Kepemilikan Nomor Induk Kependudukan | http://terminology.kemkes.go.id/sp |
| 13 | 150 | Observation | `Observation.code.coding` | SP000403 | Alasan Tidak Ada Nomor Induk Kependudukan | http://terminology.kemkes.go.id/sp |
| 14 | 151 | Observation | `Observation.valueCodeableConcept.coding` | SP000404 | Tidak Punya Kartu Tanda Penduduk | http://terminology.kemkes.go.id/sp |
| 15 | 152 | Observation | `Observation.valueCodeableConcept.coding` | SP000405 | Tidak Membawa Kartu Tanda Penduduk | http://terminology.kemkes.go.id/sp |
| 16 | 153 | Observation | `Observation.valueCodeableConcept.coding` | SP000406 | Kartu Tanda Penduduk Hilang | http://terminology.kemkes.go.id/sp |
| 17 | 154 | Observation | `Observation.valueCodeableConcept.coding` | 397644002 | Right to privacy maintained | http://snomed.info/sct |
| 18 | 155 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 19 | 164 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 20 | 176 | Observation | `Observation.code.coding` | 8339-4 | Birth weight Measured | http://loinc.org |
| 21 | 188 | Observation | `Observation.code.coding` | 365475008 | Place in family order | http://snomed.info/sct |
| 22 | 199 | Observation | `Observation.code.coding` | 76516-4 | Gestational age—​at birth | http://loinc.org |
| 23 | 212 | Observation | `Observation.code.coding` | 8338-6 | Body weight Measured --ante partum | http://loinc.org |
| 24 | 225 | Observation | `Observation.code.coding` | 1145307003 | Exclusively breastfed | http://snomed.info/sct |
| 25 | 238 | Observation | `Observation.code.coding` | 8287-5 | Head Occipital-frontal circumference by Tape measure | http://loinc.org |
| 26 | 249 | Procedure | `Procedure.code.coding` | 767224000 | Administration of vitamin A | http://snomed.info/sct |
| 27 | 260 | Observation | `Observation.code.coding` | OC000164 | Jumlah kapsul vitamin A yang diberikan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 28 | 261 | Observation | `Observation.valueCodeableConcept.coding` | OV000310 | 1 kapsul biru | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 29 | 262 | Observation | `Observation.valueCodeableConcept.coding` | SP000653 | 1 kapsul merah | http://terminology.kemkes.go.id/sp |
| 30 | 272 | Observation | `Observation.code.coding` | SP000647 | Mendapatkan makanan tambahan | http://terminology.kemkes.go.id/sp |
| 31 | 284 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 32 | 296 | Observation | `Observation.code.coding` | 8308-9 | Body height --standing | http://loinc.org |
| 33 | 297 | Observation | `Observation.code.coding` | 8306-3 | Body height --lying | http://loinc.org |
| 34 | 309 | Observation | `Observation.code.coding` | 365856005 | Screening finding | http://snomed.info/sct |
| 35 | 310 | Observation | `Observation.valueCodeableConcept.coding` | 102506008 | Well child | http://snomed.info/sct |
| 36 | 311 | Observation | `Observation.valueCodeableConcept.coding` | 704352005 | At increased risk of delayed growth | http://snomed.info/sct |
| 37 | 321 | Immunization | `Immunization.vaccineCode.coding` | VG88 | FLU | http://sys-ids.kemkes.go.id/kfa |
| 38 | 335 | Immunization | `Immunization.vaccineCode.coding` | VG129 | Japanese encephalitis | http://sys-ids.kemkes.go.id/kfa |
| 39 | 349 | Immunization | `Immunization.vaccineCode.coding` | VG21 | VARICELLA | http://sys-ids.kemkes.go.id/kfa |
| 40 | 363 | Immunization | `Immunization.vaccineCode.coding` | VG85 | HepA | http://sys-ids.kemkes.go.id/kfa |
| 41 | 377 | Immunization | `Immunization.vaccineCode.coding` | VG91 | TYPHOID | http://sys-ids.kemkes.go.id/kfa |
| 42 | 391 | Immunization | `Immunization.vaccineCode.coding` | 787859002 | Vaccine product | http://snomed.info/sct |
| 43 | 405 | Immunization | `Immunization.vaccineCode.coding` | VG19 | BCG | http://sys-ids.kemkes.go.id/kfa |
| 44 | 418 | Immunization | `Immunization.vaccineCode.coding` | VG45 | HepB | http://sys-ids.kemkes.go.id/kfa |
| 45 | 440 | Immunization | `Immunization.vaccineCode.coding` | VG89 | POLIO | http://sys-ids.kemkes.go.id/kfa |
| 46 | 462 | Immunization | `Immunization.vaccineCode.coding` | VG107 | DTAP | http://sys-ids.kemkes.go.id/kfa |
| 47 | 484 | Immunization | `Immunization.vaccineCode.coding` | VG17 | HIB | http://sys-ids.kemkes.go.id/kfa |
| 48 | 504 | Immunization | `Immunization.vaccineCode.coding` | VG152 | PneumoPCV | http://sys-ids.kemkes.go.id/kfa |
| 49 | 524 | Immunization | `Immunization.vaccineCode.coding` | VG122 | ROTAVIRUS | http://sys-ids.kemkes.go.id/kfa |
| 50 | 542 | Immunization | `Immunization.vaccineCode.coding` | VG03 | MMR | http://sys-ids.kemkes.go.id/kfa |
| 51 | 558 | Immunization | `Immunization.vaccineCode.coding` | 787859002 | Vaccine product | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://terminology.kemkes.go.id/sp | 15 |
| http://snomed.info/sct | 13 |
| http://sys-ids.kemkes.go.id/kfa | 13 |
| http://loinc.org | 7 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 2 |
| http://hl7.org/fhir/sid/icd-10 | 1 |
| **Total** | **51** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 39 | – | Nama Depan Ayah | – | `` |
| 45 | – | age_calc | – | `` |
| 50 | – | Jenis ID bayi/balita tambahan | – | `` |
| 51 | – | Nomor SID ID bayi/balita | – | `` |
| 52 | – | Nomor SID ID bayi/balita (tulis kedua kali) | – | `` |
| 72 | – | Tautan GPS rumah | – | `` |
| 82 | – | _Tautan GPS rumah_precision | – | `` |
| 85 | – | Asal Puskesmas | Organization | `Organization.name` |
| 235 | – | Tanggal Posyandu | – | `` |
| 419 | – | Hepatitis B dosis ke berapa? | – | `` |
