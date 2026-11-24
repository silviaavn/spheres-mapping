# Output Form: Dapodik PAUD

Sumber: `mapping/phdt-data-dictionary-dapodik-paud.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-dapodik-paud.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 42 |
| Code (`jumlah code` = 1) | 190 |
| Code unik (code + CodeSystem) | 140 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 75 |
| Variabel BQ (unik) | 0 |
| Variabel raw (variabel dictionary; belum ada file mentah) | 75 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 3–29 | Patient | – | – | _Nama Lengkap_ → `Patient.name.text` (3, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (4, tanpa BQ)<br>_No Registrasi Akta Lahir_ → `Patient.identifier.value` (8, tanpa BQ)<br>_No KK_ → `Patient.identifier.value` (11, tanpa BQ)<br>_Tempat Lahir_ → `Patient.extension.url` (12, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (14, tanpa BQ)<br>_NIK/ No. KITAS (untuk WNA)_ → `Patient.identifier.value` (17, tanpa BQ)<br>_Agama & Kepercayaan_ → `Patient.extension.valueCodeableConcept.coding` (19, tanpa BQ)<br>_Kewarganegaraan_ → `Patient.extension.valueCode` (28, tanpa BQ)<br>_Alamat Jalan_ → `Patient.address.line` (42, tanpa BQ)<br>_RT_ → `Patient.address.extension.url` (45, tanpa BQ)<br>_RW_ → `Patient.address.extension.url` (48, tanpa BQ)<br>_Nama Dusun_ → `Patient.address.extension.url` (51, tanpa BQ)<br>_Nama Kelurahan/ Desa_ → `Patient.address.extension.url` (54, tanpa BQ)<br>_Kecamatan_ → `Patient.address.extension.url` (57, tanpa BQ)<br>_Kode Pos_ → `Patient.address.postalCode` (60, tanpa BQ)<br>_Lintang_ → `Patient.address.extension.url` (64, tanpa BQ)<br>_Bujur_ → `Patient.address.extension.url` (67, tanpa BQ)<br>_Nomor telepon Rumah_ → `Patient.telecom.use` (70, tanpa BQ)<br>_Nomor HP (Ibu)_ → `Patient.telecom.use` (73, tanpa BQ)<br>_Email_ → `Patient.telecom.use` (76, tanpa BQ) |
| 2 | 30–41 | Observation | 104890-9 | Nationality Person Narrative | – |
| 3 | 79–92 | Encounter | – | – | – |
| 4 | 93–99 | Condition | 170245002 | Child examination: school screening | – |
| 5 | 110–126 | Observation | 365481000 | Finding of household composition | _Tempat tinggal_ → `Observation.status` (110, tanpa BQ) |
| 6 | 127–151 | Observation | SP000241 | Moda Transportasi yang digunakan untuk bersekolah | _Moda Transportasi_ → `Observation.identifier.value` (151, tanpa BQ) |
| 7 | 152–162 | Observation | SP000239 | Kartu Perlindungan Sosial | – |
| 8 | 163–170 | RelatedPerson | – | – | _Nama ayah Kandung_ → `RelatedPerson.name.text` (163, tanpa BQ)<br>_Tahun Lahir_ → `RelatedPerson.birthDate` (164, tanpa BQ)<br>_NIK Ayah_ → `RelatedPerson.identifier.value` (170, tanpa BQ) |
| 9 | 171–205 | Observation | 82589-3 | Highest level of education | _Pendidikan_ → `Observation.status` (171, tanpa BQ) |
| 10 | 206–236 | Observation | OC000149 | Pekerjaan orang tua | _Pekerjaan_ → `Observation.status` (206, tanpa BQ) |
| 11 | 237–260 | Condition | 81323004 | Normal general body function | _Berkebutuhan Khusus_ → `Condition.clinicalStatus.coding` (237, tanpa BQ) |
| 12 | 261–278 | Observation | 365552003 | Finding of income details | _Penghasilan bulanan_ → `Observation.status` (261, tanpa BQ) |
| 13 | 279–286 | RelatedPerson | – | – | _Nama Ibu Kandung_ → `RelatedPerson.name.text` (279, tanpa BQ)<br>_Tahun Lahir_ → `RelatedPerson.birthDate` (280, tanpa BQ)<br>_NIK Ibu_ → `RelatedPerson.identifier.value` (286, tanpa BQ) |
| 14 | 287–321 | Observation | 82589-3 | Highest level of education | _Pendidikan_ → `Observation.status` (287, tanpa BQ) |
| 15 | 322–351 | Observation | OC000149 | Pekerjaan orang tua | _Pekerjaan_ → `Observation.status` (322, tanpa BQ) |
| 16 | 352–369 | Observation | 365552003 | Finding of income details | _Penghasilan bulanan_ → `Observation.status` (352, tanpa BQ) |
| 17 | 370–393 | Condition | 81323004 | Normal general body function | _Berkebutuhan Khusus_ → `Condition.clinicalStatus.coding` (370, tanpa BQ) |
| 18 | 394–401 | RelatedPerson | – | – | _Nama Wali_ → `RelatedPerson.name.text` (394, tanpa BQ)<br>_Tahun Lahir_ → `RelatedPerson.birthDate` (395, tanpa BQ)<br>_NIK Wali_ → `RelatedPerson.identifier.value` (401, tanpa BQ) |
| 19 | 402–436 | Observation | 82589-3 | Highest level of education | _Pendidikan_ → `Observation.status` (402, tanpa BQ) |
| 20 | 437–466 | Observation | OC000149 | Pekerjaan orang tua | _Pekerjaan_ → `Observation.status` (437, tanpa BQ) |
| 21 | 467–487 | Observation | 365552003 | Finding of income details | _Penghasilan bulanan_ → `Observation.identifier.value` (487, tanpa BQ) |
| 22 | 488–501 | Observation | SP000232 | Kartu Indonesia Pintar | _Apakah punya KIP_ → `Observation.valueBoolean` (489, tanpa BQ)<br>_Apakah peserta didik tersebut tetap akan menerima KIP_ → `Observation.component.code.coding` (491, tanpa BQ) |
| 23 | 502–508 | Account | – | – | – |
| 24 | 509–532 | Observation | SP000243 | Program Indonesia Pintar | _Alasan Layak PIP_ → `Observation.component.valueCodeableConcept.coding` (516, tanpa BQ) |
| 25 | 533–556 | Condition | 81323004 | Normal general body function | _Berkebutuhan Khusus_ → `Condition.clinicalStatus.coding` (533, tanpa BQ) |
| 26 | 557–567 | Observation | 365475008 | Place in family order | _Anak keberapa_ → `Observation.valueInteger` (560, tanpa BQ) |
| 27 | 568–592 | Observation | OC000149 | Pekerjaan orang tua | _Pekerjaan (diperuntukan untuk warga belajar)_ → `Observation.status` (568, tanpa BQ) |
| 28 | 593–604 | Observation | 29463-7 | Body weight | _Berat Badan_ → `Observation.valueQuantity.value` (596, tanpa BQ) |
| 29 | 605–616 | Observation | 8302-2 | Body height | _Tinggi Badan_ → `Observation.valueQuantity.value` (608, tanpa BQ) |
| 30 | 617–628 | Observation | 9843-4 | Head Occipital-frontal circumference | _Lingkar Kepala_ → `Observation.valueQuantity.value` (620, tanpa BQ) |
| 31 | 630–640 | Observation | 224095004 | Number of siblings | _Jumlah Saudara Kandung_ → `Observation.valueInteger` (633, tanpa BQ) |
| 32 | 642–653 | Observation | SP000230 | Jarak dari rumah ke sekolah | _Jarak tempat tinggal ke sekolah_ → `Observation.valueCodeableConcept.coding` (645, tanpa BQ) |
| 33 | 654–665 | Observation | SP000292 | Jarak dari rumah ke sekolah (km) | _Sebutkan dalam km_ → `Observation.valueQuantity.value` (657, tanpa BQ) |
| 34 | 666–676 | Observation | SP000293 | Waktu tempuh dari rumah ke sekolah | _Waktu tempuh ke sekolah (jam)_ → `Observation.status` (666, tanpa BQ)<br>_Waktu tempuh ke sekolah (menit)_ → `Observation.valueTime` (669, tanpa BQ) |
| 35 | 677–705 | Observation | 105421008 | Educational achievement | _Jenis_ → `Observation.component.code.coding` (680, tanpa BQ)<br>_Tingkat_ → `Observation.component.code.coding` (685, tanpa BQ)<br>_Nama Prestasi_ → `Observation.component.code.coding` (693, tanpa BQ)<br>_Tahun_ → `Observation.component.code.coding` (695, tanpa BQ)<br>_Penyelenggara_ → `Observation.component.code.coding` (697, tanpa BQ) |
| 36 | 706–726 | Observation | SP000309 | Beasiswa | _Jenis Beasiswa_ → `Observation.component.code.coding` (709, tanpa BQ)<br>_Keterangan_ → `Observation.component.valueString` (716, tanpa BQ)<br>_Tahun mulai_ → `Observation.component.valuePeriod.start` (718, tanpa BQ)<br>_Tahun selesai_ → `Observation.component.valuePeriod.end` (719, tanpa BQ) |
| 37 | 727–753 | Observation | SP000328 | Asuransi Kesejahteraan | _Jenis kesejahteraan_ → `Observation.code.coding` (729, tanpa BQ)<br>_No Kartu_ → `Observation.identifier.value` (740, tanpa BQ)<br>_Nama di Kartu_ → `Observation.focus.display` (741, tanpa BQ)<br>_NISN_ → `Observation.identifier.value` (753, tanpa BQ) |
| 38 | 754–797 | Observation | 276031006 | Details of education | _Kompetensi keahlian_ → `Observation.component.code.coding` (756, tanpa BQ)<br>_Jenis Pendaftaran_ → `Observation.component.code.coding` (758, tanpa BQ)<br>_Sekolah Asal_ → `Observation.component.code.coding` (762, tanpa BQ)<br>_Apakah PAUD formal_ → `Observation.component.code.coding` (764, tanpa BQ)<br>_Apakah PAUD Non-formal_ → `Observation.component.valueCodeableConcept.coding` (766, tanpa BQ)<br>_Tanggal Masuk Sekolah_ → `Observation.component.code.coding` (768, tanpa BQ)<br>_Rombel_ → `Observation.component.code.coding` (770, tanpa BQ)<br>_Nomor Peserta UN SMP/MTs_ → `Observation.component.code.coding` (772, tanpa BQ)<br>_No.Seri Ijazah SMP/MTs_ → `Observation.component.code.coding` (774, tanpa BQ)<br>_No. SKHUN SMP/MTs_ → `Observation.component.code.coding` (776, tanpa BQ)<br>_Keluar karena_ → `Observation.component.code.coding` (778, tanpa BQ)<br>_Tanggal keluar_ → `Observation.component.code.coding` (786, tanpa BQ)<br>_Alasan_ → `Observation.component.code.coding` (788, tanpa BQ)<br>_Hobi_ → `Observation.status` (797, tanpa BQ) |
| 39 | 798–834 | Observation | 63764-5 | Hobby [LIBCSP] | _Cita-cita_ → `Observation.status` (834, tanpa BQ) |
| 40 | 835–881 | Observation | SP000357 | Cita-cita | _Hobi_ → `Observation.status` (881, tanpa BQ) |
| 41 | 882–918 | Observation | 63764-5 | Hobby [LIBCSP] | _Cita-cita_ → `Observation.status` (918, tanpa BQ) |
| 42 | 919–963 | Observation | SP000357 | Cita-cita | – |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 32 |
| Condition | 4 |
| RelatedPerson | 3 |
| Patient | 1 |
| Encounter | 1 |
| Account | 1 |
| **Total** | **42** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 33 | Observation | `Observation.code.coding` | 104890-9 | Nationality Person Narrative | http://loinc.org |
| 2 | 95 | Condition | `Condition.code.coding` | 170245002 | Child examination: school screening | http://snomed.info/sct |
| 3 | 112 | Observation | `Observation.code.coding` | 365481000 | Finding of household composition | http://snomed.info/sct |
| 4 | 129 | Observation | `Observation.code.coding` | SP000241 | Moda Transportasi yang digunakan untuk bersekolah | http://terminology.kemkes.go.id/sp |
| 5 | 152 | Observation | `Observation.code.coding` | SP000239 | Kartu Perlindungan Sosial | http://terminology.kemkes.go.id/sp |
| 6 | 173 | Observation | `Observation.code.coding` | 82589-3 | Highest level of education | http://loinc.org |
| 7 | 208 | Observation | `Observation.code.coding` | OC000149 | Pekerjaan orang tua | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 8 | 239 | Condition | `Condition.code.coding` | 81323004 | Normal general body function | http://snomed.info/sct |
| 9 | 240 | Condition | `Condition.code.coding` | 397540003 | Visual impairment | http://snomed.info/sct |
| 10 | 241 | Condition | `Condition.code.coding` | 15188001 | Hearing loss | http://snomed.info/sct |
| 11 | 242 | Condition | `Condition.code.coding` | 86765009 | Mild intellectual disability | http://snomed.info/sct |
| 12 | 243 | Condition | `Condition.code.coding` | 61152003 | Moderate intellectual disability | http://snomed.info/sct |
| 13 | 244 | Condition | `Condition.code.coding` | 8510008 | Reduced mobility | http://snomed.info/sct |
| 14 | 245 | Condition | `Condition.code.coding` | 160693001 | Mobility poor | http://snomed.info/sct |
| 15 | 246 | Condition | `Condition.code.coding` | 5793009 | Mixed behavior and emotional disorder | http://snomed.info/sct |
| 16 | 247 | Condition | `Condition.code.coding` | 29164008 | Disturbance in speech | http://snomed.info/sct |
| 17 | 248 | Condition | `Condition.code.coding` | 406134008 | Multiple disability | http://snomed.info/sct |
| 18 | 249 | Condition | `Condition.code.coding` | 44548000 | Hyperactive behavior | http://snomed.info/sct |
| 19 | 250 | Condition | `Condition.code.coding` | 8273004 | Intelligence quotient high | http://snomed.info/sct |
| 20 | 251 | Condition | `Condition.code.coding` | 367358004 | Above average intellect | http://snomed.info/sct |
| 21 | 252 | Condition | `Condition.code.coding` | 1855002 | Developmental academic disorder | http://snomed.info/sct |
| 22 | 253 | Condition | `Condition.code.coding` | 70545002 | Narcotic drug user | http://snomed.info/sct |
| 23 | 254 | Condition | `Condition.code.coding` | 247701008 | Abnormal perception | http://snomed.info/sct |
| 24 | 255 | Condition | `Condition.code.coding` | 41040004 | Complete trisomy 21 syndrome | http://snomed.info/sct |
| 25 | 256 | Condition | `Condition.code.coding` | 35919005 | Pervasive developmental disorder | http://snomed.info/sct |
| 26 | 263 | Observation | `Observation.code.coding` | 365552003 | Finding of income details | http://snomed.info/sct |
| 27 | 289 | Observation | `Observation.code.coding` | 82589-3 | Highest level of education | http://loinc.org |
| 28 | 324 | Observation | `Observation.code.coding` | OC000149 | Pekerjaan orang tua | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 29 | 354 | Observation | `Observation.code.coding` | 365552003 | Finding of income details | http://snomed.info/sct |
| 30 | 372 | Condition | `Condition.code.coding` | 81323004 | Normal general body function | http://snomed.info/sct |
| 31 | 373 | Condition | `Condition.code.coding` | 397540003 | Visual impairment | http://snomed.info/sct |
| 32 | 374 | Condition | `Condition.code.coding` | 15188001 | Hearing loss | http://snomed.info/sct |
| 33 | 375 | Condition | `Condition.code.coding` | 86765009 | Mild intellectual disability | http://snomed.info/sct |
| 34 | 376 | Condition | `Condition.code.coding` | 61152003 | Moderate intellectual disability | http://snomed.info/sct |
| 35 | 377 | Condition | `Condition.code.coding` | 8510008 | Reduced mobility | http://snomed.info/sct |
| 36 | 378 | Condition | `Condition.code.coding` | 160693001 | Mobility poor | http://snomed.info/sct |
| 37 | 379 | Condition | `Condition.code.coding` | 5793009 | Mixed behavior and emotional disorder | http://snomed.info/sct |
| 38 | 380 | Condition | `Condition.code.coding` | 29164008 | Disturbance in speech | http://snomed.info/sct |
| 39 | 381 | Condition | `Condition.code.coding` | 406134008 | Multiple disability | http://snomed.info/sct |
| 40 | 382 | Condition | `Condition.code.coding` | 44548000 | Hyperactive behavior | http://snomed.info/sct |
| 41 | 383 | Condition | `Condition.code.coding` | 8273004 | Intelligence quotient high | http://snomed.info/sct |
| 42 | 384 | Condition | `Condition.code.coding` | 367358004 | Above average intellect | http://snomed.info/sct |
| 43 | 385 | Condition | `Condition.code.coding` | 1855002 | Developmental academic disorder | http://snomed.info/sct |
| 44 | 386 | Condition | `Condition.code.coding` | 70545002 | Narcotic drug user | http://snomed.info/sct |
| 45 | 387 | Condition | `Condition.code.coding` | 247701008 | Abnormal perception | http://snomed.info/sct |
| 46 | 388 | Condition | `Condition.code.coding` | 41040004 | Complete trisomy 21 syndrome | http://snomed.info/sct |
| 47 | 389 | Condition | `Condition.code.coding` | 35919005 | Pervasive developmental disorder | http://snomed.info/sct |
| 48 | 404 | Observation | `Observation.code.coding` | 82589-3 | Highest level of education | http://loinc.org |
| 49 | 439 | Observation | `Observation.code.coding` | OC000149 | Pekerjaan orang tua | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 50 | 469 | Observation | `Observation.code.coding` | 365552003 | Finding of income details | http://snomed.info/sct |
| 51 | 488 | Observation | `Observation.code.coding` | SP000232 | Kartu Indonesia Pintar | http://terminology.kemkes.go.id/sp |
| 52 | 491 | Observation | `Observation.component.code.coding` | SP000327 | Tetap akan menerima KIP | http://terminology.kemkes.go.id/sp |
| 53 | 511 | Observation | `Observation.code.coding` | SP000243 | Program Indonesia Pintar | http://terminology.kemkes.go.id/sp |
| 54 | 512 | Observation | `Observation.component.code.coding` | SP000317 | Layak menerima PIP | http://terminology.kemkes.go.id/sp |
| 55 | 515 | Observation | `Observation.component.code.coding` | SP000318 | Alasan Layak PIP | http://terminology.kemkes.go.id/sp |
| 56 | 516 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000319 | Daerah konflik | http://terminology.kemkes.go.id/sp |
| 57 | 517 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000320 | Dampak bencana | http://terminology.kemkes.go.id/sp |
| 58 | 518 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000321 | Kelainan fisik | http://terminology.kemkes.go.id/sp |
| 59 | 519 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000322 | Keluarga narapidana | http://terminology.kemkes.go.id/sp |
| 60 | 520 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000323 | Pemegang PKH/KPS/KKS | http://terminology.kemkes.go.id/sp |
| 61 | 521 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000324 | Pernah Dropout | http://terminology.kemkes.go.id/sp |
| 62 | 522 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000325 | Siswa miskin/rentan miskin | http://terminology.kemkes.go.id/sp |
| 63 | 523 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000326 | Yatim Piatu/Panti Asuhan/Panti Sosial | http://terminology.kemkes.go.id/sp |
| 64 | 535 | Condition | `Condition.code.coding` | 81323004 | Normal general body function | http://snomed.info/sct |
| 65 | 536 | Condition | `Condition.code.coding` | 397540003 | Visual impairment | http://snomed.info/sct |
| 66 | 537 | Condition | `Condition.code.coding` | 15188001 | Hearing loss | http://snomed.info/sct |
| 67 | 538 | Condition | `Condition.code.coding` | 86765009 | Mild intellectual disability | http://snomed.info/sct |
| 68 | 539 | Condition | `Condition.code.coding` | 61152003 | Moderate intellectual disability | http://snomed.info/sct |
| 69 | 540 | Condition | `Condition.code.coding` | 8510008 | Reduced mobility | http://snomed.info/sct |
| 70 | 541 | Condition | `Condition.code.coding` | 160693001 | Mobility poor | http://snomed.info/sct |
| 71 | 542 | Condition | `Condition.code.coding` | 5793009 | Mixed behavior and emotional disorder | http://snomed.info/sct |
| 72 | 543 | Condition | `Condition.code.coding` | 29164008 | Disturbance in speech | http://snomed.info/sct |
| 73 | 544 | Condition | `Condition.code.coding` | 406134008 | Multiple disability | http://snomed.info/sct |
| 74 | 545 | Condition | `Condition.code.coding` | 44548000 | Hyperactive behavior | http://snomed.info/sct |
| 75 | 546 | Condition | `Condition.code.coding` | 8273004 | Intelligence quotient high | http://snomed.info/sct |
| 76 | 547 | Condition | `Condition.code.coding` | 367358004 | Above average intellect | http://snomed.info/sct |
| 77 | 548 | Condition | `Condition.code.coding` | 1855002 | Developmental academic disorder | http://snomed.info/sct |
| 78 | 549 | Condition | `Condition.code.coding` | 70545002 | Narcotic drug user | http://snomed.info/sct |
| 79 | 550 | Condition | `Condition.code.coding` | 247701008 | Abnormal perception | http://snomed.info/sct |
| 80 | 551 | Condition | `Condition.code.coding` | 41040004 | Complete trisomy 21 syndrome | http://snomed.info/sct |
| 81 | 552 | Condition | `Condition.code.coding` | 35919005 | Pervasive developmental disorder | http://snomed.info/sct |
| 82 | 559 | Observation | `Observation.code.coding` | 365475008 | Place in family order | http://snomed.info/sct |
| 83 | 570 | Observation | `Observation.code.coding` | OC000149 | Pekerjaan orang tua | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 84 | 595 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 85 | 607 | Observation | `Observation.code.coding` | 8302-2 | Body height | http://loinc.org |
| 86 | 619 | Observation | `Observation.code.coding` | 9843-4 | Head Occipital-frontal circumference | http://loinc.org |
| 87 | 632 | Observation | `Observation.code.coding` | 224095004 | Number of siblings | http://snomed.info/sct |
| 88 | 644 | Observation | `Observation.code.coding` | SP000230 | Jarak dari rumah ke sekolah | http://terminology.kemkes.go.id/sp |
| 89 | 645 | Observation | `Observation.valueCodeableConcept.coding` | SP000290 | Kurang dari 1 km | http://terminology.kemkes.go.id/sp |
| 90 | 646 | Observation | `Observation.valueCodeableConcept.coding` | SP000291 | Lebih dari 1 km | http://terminology.kemkes.go.id/sp |
| 91 | 656 | Observation | `Observation.code.coding` | SP000292 | Jarak dari rumah ke sekolah (km) | http://terminology.kemkes.go.id/sp |
| 92 | 668 | Observation | `Observation.code.coding` | SP000293 | Waktu tempuh dari rumah ke sekolah | http://terminology.kemkes.go.id/sp |
| 93 | 679 | Observation | `Observation.code.coding` | 105421008 | Educational achievement | http://snomed.info/sct |
| 94 | 680 | Observation | `Observation.component.code.coding` | SP000294 | Jenis Prestasi | http://terminology.kemkes.go.id/sp |
| 95 | 681 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000300 | Sains | http://terminology.kemkes.go.id/sp |
| 96 | 682 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000301 | Seni | http://terminology.kemkes.go.id/sp |
| 97 | 683 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000302 | Olahraga | http://terminology.kemkes.go.id/sp |
| 98 | 684 | Observation | `Observation.component.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 99 | 685 | Observation | `Observation.component.code.coding` | SP000295 | Tingkatan Prestasi | http://terminology.kemkes.go.id/sp |
| 100 | 686 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000303 | Tingkat Sekolah | http://terminology.kemkes.go.id/sp |
| 101 | 687 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000304 | Tingkat Kecamatan | http://terminology.kemkes.go.id/sp |
| 102 | 688 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000305 | Tingkat Kabupaten | http://terminology.kemkes.go.id/sp |
| 103 | 689 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000306 | Tingkat Provinsi | http://terminology.kemkes.go.id/sp |
| 104 | 690 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000307 | Tingkat Nasional | http://terminology.kemkes.go.id/sp |
| 105 | 691 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000308 | Tingkat Internasional | http://terminology.kemkes.go.id/sp |
| 106 | 692 | Observation | `Observation.component.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 107 | 693 | Observation | `Observation.component.code.coding` | SP000297 | Nama Prestasi | http://terminology.kemkes.go.id/sp |
| 108 | 695 | Observation | `Observation.component.code.coding` | SP000298 | Tahun Prestasi | http://terminology.kemkes.go.id/sp |
| 109 | 697 | Observation | `Observation.component.code.coding` | SP000299 | Penyelenggara | http://terminology.kemkes.go.id/sp |
| 110 | 708 | Observation | `Observation.code.coding` | SP000309 | Beasiswa | http://terminology.kemkes.go.id/sp |
| 111 | 709 | Observation | `Observation.component.code.coding` | SP000310 | Jenis Beasiswa | http://terminology.kemkes.go.id/sp |
| 112 | 710 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000311 | Beasiswa Anak berprestasi | http://terminology.kemkes.go.id/sp |
| 113 | 711 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000312 | Beasiswa Anak miskin/kemiskinan | http://terminology.kemkes.go.id/sp |
| 114 | 712 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000313 | Beasiswa Pendidikan | http://terminology.kemkes.go.id/sp |
| 115 | 713 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000314 | Beasiswa Unggulan | http://terminology.kemkes.go.id/sp |
| 116 | 714 | Observation | `Observation.component.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 117 | 715 | Observation | `Observation.component.code.coding` | SP000315 | Keterangan Beasiswa | http://terminology.kemkes.go.id/sp |
| 118 | 717 | Observation | `Observation.component.code.coding` | SP000316 | Periode Beasiswa | http://terminology.kemkes.go.id/sp |
| 119 | 729 | Observation | `Observation.code.coding` | SP000328 | Asuransi Kesejahteraan | http://terminology.kemkes.go.id/sp |
| 120 | 730 | Observation | `Observation.code.coding` | SP000329 | Dana Pensiun | http://terminology.kemkes.go.id/sp |
| 121 | 731 | Observation | `Observation.code.coding` | SP000330 | Jamkesmas | http://terminology.kemkes.go.id/sp |
| 122 | 732 | Observation | `Observation.code.coding` | SP000331 | Jamsostek | http://terminology.kemkes.go.id/sp |
| 123 | 733 | Observation | `Observation.code.coding` | SP000332 | BPJS | http://terminology.kemkes.go.id/sp |
| 124 | 734 | Observation | `Observation.code.coding` | SP000333 | Kartu Keluarga Sejahtera | http://terminology.kemkes.go.id/sp |
| 125 | 735 | Observation | `Observation.code.coding` | SP000334 | Kartu Indonesia Sehat | http://terminology.kemkes.go.id/sp |
| 126 | 736 | Observation | `Observation.code.coding` | SP000335 | Otonomi Khusus Papua | http://terminology.kemkes.go.id/sp |
| 127 | 737 | Observation | `Observation.code.coding` | SP000336 | Program Keluarga Harapan | http://terminology.kemkes.go.id/sp |
| 128 | 738 | Observation | `Observation.code.coding` | SP000243 | Program Indonesia Pintar | http://terminology.kemkes.go.id/sp |
| 129 | 739 | Observation | `Observation.code.coding` | SP000239 | Kartu Perlindungan Sosial | http://terminology.kemkes.go.id/sp |
| 130 | 755 | Observation | `Observation.code.coding` | 276031006 | Details of education | http://snomed.info/sct |
| 131 | 756 | Observation | `Observation.component.code.coding` | SP000337 | Kompetensi Keahlian (SMK) | http://terminology.kemkes.go.id/sp |
| 132 | 758 | Observation | `Observation.component.code.coding` | SP000338 | Jenis Pendaftaran | http://terminology.kemkes.go.id/sp |
| 133 | 759 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000339 | Siswa baru | http://terminology.kemkes.go.id/sp |
| 134 | 760 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000340 | Siswa Pindahan | http://terminology.kemkes.go.id/sp |
| 135 | 761 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000341 | Kembali bersekolah | http://terminology.kemkes.go.id/sp |
| 136 | 762 | Observation | `Observation.component.code.coding` | 224293004 | Education received in the past | http://snomed.info/sct |
| 137 | 764 | Observation | `Observation.component.code.coding` | SP000342 | Jenis Lembaga Pendidikan | http://terminology.kemkes.go.id/sp |
| 138 | 765 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000343 | Formal | http://terminology.kemkes.go.id/sp |
| 139 | 766 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000344 | Informal | http://terminology.kemkes.go.id/sp |
| 140 | 768 | Observation | `Observation.component.code.coding` | SP000345 | Tanggal masuk sekolah | http://terminology.kemkes.go.id/sp |
| 141 | 770 | Observation | `Observation.component.code.coding` | SP000346 | Rombongan Belajar | http://terminology.kemkes.go.id/sp |
| 142 | 772 | Observation | `Observation.component.code.coding` | SP000347 | No Peserta Ujian Nasional | http://terminology.kemkes.go.id/sp |
| 143 | 774 | Observation | `Observation.component.code.coding` | SP000348 | No Seri Ijazah | http://terminology.kemkes.go.id/sp |
| 144 | 776 | Observation | `Observation.component.code.coding` | SP000349 | No SKHUN/SHUN | http://terminology.kemkes.go.id/sp |
| 145 | 778 | Observation | `Observation.component.code.coding` | SP000350 | Alasan utama keluar sekolah | http://terminology.kemkes.go.id/sp |
| 146 | 779 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000351 | Mutasi | http://terminology.kemkes.go.id/sp |
| 147 | 780 | Observation | `Observation.component.valueCodeableConcept.coding` | 228137002 | Excluded from school permanently |  |
| 148 | 781 | Observation | `Observation.component.valueCodeableConcept.coding` | 161131005 | Left school free will |  |
| 149 | 782 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000352 | Putus sekolah | http://terminology.kemkes.go.id/sp |
| 150 | 783 | Observation | `Observation.component.valueCodeableConcept.coding` | 419099009 | Dead |  |
| 151 | 784 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000353 | Hilang | http://terminology.kemkes.go.id/sp |
| 152 | 785 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000354 | Lulus | http://terminology.kemkes.go.id/sp |
| 153 | 786 | Observation | `Observation.component.code.coding` | SP000355 | Tanggal keluar sekolah | http://terminology.kemkes.go.id/sp |
| 154 | 788 | Observation | `Observation.component.code.coding` | SP000356 | Alasan khusus keluar sekolah | http://terminology.kemkes.go.id/sp |
| 155 | 799 | Observation | `Observation.code.coding` | 63764-5 | Hobby [LIBCSP] | http://loinc.org |
| 156 | 836 | Observation | `Observation.code.coding` | SP000357 | Cita-cita | http://terminology.kemkes.go.id/sp |
| 157 | 883 | Observation | `Observation.code.coding` | 63764-5 | Hobby [LIBCSP] | http://loinc.org |
| 158 | 884 | Observation | `Observation.valueCodeableConcept.coding` | 129011005 | Shopping | http://snomed.info/sct |
| 159 | 885 | Observation | `Observation.valueCodeableConcept.coding` | 10496000 | Camping | http://snomed.info/sct |
| 160 | 886 | Observation | `Observation.valueCodeableConcept.coding` | 418060005 | Running | http://snomed.info/sct |
| 161 | 888 | Observation | `Observation.valueCodeableConcept.coding` | 88289009 | Soccer | http://snomed.info/sct |
| 162 | 889 | Observation | `Observation.valueCodeableConcept.coding` | 26550000 | Tennis | http://snomed.info/sct |
| 163 | 895 | Observation | `Observation.valueCodeableConcept.coding` | 84096006 | Surfing | http://snomed.info/sct |
| 164 | 898 | Observation | `Observation.valueCodeableConcept.coding` | 1968006 | Jogging | http://snomed.info/sct |
| 165 | 901 | Observation | `Observation.valueCodeableConcept.coding` | 48263008 | Eating | http://snomed.info/sct |
| 166 | 902 | Observation | `Observation.valueCodeableConcept.coding` | 1137717005 | Fishing | http://snomed.info/sct |
| 167 | 903 | Observation | `Observation.valueCodeableConcept.coding` | 50360004 | Reading | http://snomed.info/sct |
| 168 | 904 | Observation | `Observation.valueCodeableConcept.coding` | 111055000 | Mountain climbing | http://snomed.info/sct |
| 169 | 908 | Observation | `Observation.valueCodeableConcept.coding` | 14468000 | Sports activity | http://snomed.info/sct |
| 170 | 909 | Observation | `Observation.valueCodeableConcept.coding` | 129018004 | Traveling | http://snomed.info/sct |
| 171 | 910 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 172 | 920 | Observation | `Observation.code.coding` | SP000357 | Cita-cita | http://terminology.kemkes.go.id/sp |
| 173 | 921 | Observation | `Observation.valueCodeableConcept.coding` | 308047006 | Architect | http://snomed.info/sct |
| 174 | 925 | Observation | `Observation.valueCodeableConcept.coding` | 106325008 | Athlete, sportsman/related worker | http://snomed.info/sct |
| 175 | 926 | Observation | `Observation.valueCodeableConcept.coding` | 75271001 | Professional midwife | http://snomed.info/sct |
| 176 | 930 | Observation | `Observation.valueCodeableConcept.coding` | 158965000 | Medical practitioner | http://snomed.info/sct |
| 177 | 931 | Observation | `Observation.valueCodeableConcept.coding` | 265945005 | Performer (entertainment) | http://snomed.info/sct |
| 178 | 933 | Observation | `Observation.valueCodeableConcept.coding` | 308207007 | Chef | http://snomed.info/sct |
| 179 | 935 | Observation | `Observation.valueCodeableConcept.coding` | 236297007 | Civil servant | http://snomed.info/sct |
| 180 | 941 | Observation | `Observation.valueCodeableConcept.coding` | 12877000 | Lawyer | http://snomed.info/sct |
| 181 | 944 | Observation | `Observation.valueCodeableConcept.coding` | 308004006 | Writer | http://snomed.info/sct |
| 182 | 945 | Observation | `Observation.valueCodeableConcept.coding` | 78705009 | Radio and television announcer | http://snomed.info/sct |
| 183 | 946 | Observation | `Observation.valueCodeableConcept.coding` | 106292003 | Professional nurse | http://snomed.info/sct |
| 184 | 947 | Observation | `Observation.valueCodeableConcept.coding` | 308040008 | Pilot - aircraft | http://snomed.info/sct |
| 185 | 948 | Observation | `Observation.valueCodeableConcept.coding` | 14406004 | Policeman | http://snomed.info/sct |
| 186 | 951 | Observation | `Observation.valueCodeableConcept.coding` | 159062006 | Artist | http://snomed.info/sct |
| 187 | 952 | Observation | `Observation.valueCodeableConcept.coding` | OV000433 | TNI/ Polri | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 188 | 953 | Observation | `Observation.valueCodeableConcept.coding` | 80409005 | Translator | http://snomed.info/sct |
| 189 | 955 | Observation | `Observation.valueCodeableConcept.coding` | 29536009 | Journalist | http://snomed.info/sct |
| 190 | 956 | Observation | `Observation.valueCodeableConcept.coding` | 160906004 | Self-employed | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 98 |
| http://terminology.kemkes.go.id/sp | 75 |
| http://loinc.org | 9 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 5 |
|  | 3 |
| **Total** | **190** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
