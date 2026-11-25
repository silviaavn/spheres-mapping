# Output Form: Dapodik PAUD

Sumber: `mapping/phdt-data-dictionary-dapodik-paud.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-dapodik-paud.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 42 |
| Code (`jumlah code` = 1) | 378 |
| Code unik (code + CodeSystem) | 205 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 161 |
| Variabel BQ (unik) | 0 |
| Variabel raw (variabel dictionary; belum ada file mentah) | 75 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 3–29 | Patient | – | – | _Nama Lengkap_ → `Patient.name.text` (3, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (4, tanpa BQ)<br>_No Registrasi Akta Lahir_ → `Patient.identifier.value` (8, tanpa BQ)<br>_No KK_ → `Patient.identifier.value` (11, tanpa BQ)<br>_Tempat Lahir_ → `Patient.extension.url` (12, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (14, tanpa BQ)<br>_NIK/ No. KITAS (untuk WNA)_ → `Patient.identifier.value` (17, tanpa BQ)<br>_Agama & Kepercayaan_ → `Patient.extension.valueCodeableConcept.coding` (19, tanpa BQ)<br>_Kewarganegaraan_ → `Patient.extension.valueCode` (28, tanpa BQ)<br>_Alamat Jalan_ → `Patient.address.line` (42, tanpa BQ)<br>_RT_ → `Patient.address.extension.url` (45, tanpa BQ)<br>_RW_ → `Patient.address.extension.url` (48, tanpa BQ)<br>_Nama Dusun_ → `Patient.address.extension.url` (51, tanpa BQ)<br>_Nama Kelurahan/ Desa_ → `Patient.address.extension.url` (54, tanpa BQ)<br>_Kecamatan_ → `Patient.address.extension.url` (57, tanpa BQ)<br>_Kode Pos_ → `Patient.address.postalCode` (60, tanpa BQ)<br>_Lintang_ → `Patient.address.extension.url` (64, tanpa BQ)<br>_Bujur_ → `Patient.address.extension.url` (67, tanpa BQ)<br>_Nomor telepon Rumah_ → `Patient.telecom.use` (70, tanpa BQ)<br>_Nomor HP (Ibu)_ → `Patient.telecom.use` (73, tanpa BQ)<br>_Email_ → `Patient.telecom.use` (76, tanpa BQ) |
| 2 | 30–41 | Observation | 104890-9 | Nationality Person Narrative | – |
| 3 | 79–92 | Encounter | – | – | – |
| 4 | 93–99 | Condition | 170245002 | Child examination: school screening | – |
| 5 | 110–126 | Observation | 365481000 | Finding of household composition | _Tempat tinggal_ → `Observation.valueCodeableConcept.coding` (113, tanpa BQ) |
| 6 | 127–151 | Observation | SP000241 | Moda Transportasi yang digunakan untuk bersekolah | _Moda Transportasi_ → `Observation.valueCodeableConcept.coding` (130, tanpa BQ) |
| 7 | 152–162 | Observation | SP000239 | Kartu Perlindungan Sosial | – |
| 8 | 163–170 | RelatedPerson | – | – | _Nama ayah Kandung_ → `RelatedPerson.name.text` (163, tanpa BQ)<br>_Tahun Lahir_ → `RelatedPerson.birthDate` (164, tanpa BQ)<br>_NIK Ayah_ → `RelatedPerson.identifier.value` (170, tanpa BQ) |
| 9 | 171–205 | Observation | 82589-3 | Highest level of education | _Pendidikan_ → `Observation.valueCodeableConcept.coding` (174, tanpa BQ) |
| 10 | 206–236 | Observation | OC000149 | Pekerjaan orang tua | _Pekerjaan_ → `Observation.valueCodeableConcept.coding` (209, tanpa BQ) |
| 11 | 237–260 | Condition | 81323004 | Normal general body function | _Berkebutuhan Khusus_ → `Condition.clinicalStatus.coding` (237, tanpa BQ) |
| 12 | 261–278 | Observation | 365552003 | Finding of income details | _Penghasilan bulanan_ → `Observation.valueCodeableConcept.coding` (264, tanpa BQ) |
| 13 | 279–286 | RelatedPerson | – | – | _Nama Ibu Kandung_ → `RelatedPerson.name.text` (279, tanpa BQ)<br>_Tahun Lahir_ → `RelatedPerson.birthDate` (280, tanpa BQ)<br>_NIK Ibu_ → `RelatedPerson.identifier.value` (286, tanpa BQ) |
| 14 | 287–321 | Observation | 82589-3 | Highest level of education | _Pendidikan_ → `Observation.valueCodeableConcept.coding` (290, tanpa BQ) |
| 15 | 322–351 | Observation | OC000149 | Pekerjaan orang tua | _Pekerjaan_ → `Observation.valueCodeableConcept.coding` (325, tanpa BQ) |
| 16 | 352–369 | Observation | 365552003 | Finding of income details | _Penghasilan bulanan_ → `Observation.valueCodeableConcept.coding` (355, tanpa BQ) |
| 17 | 370–393 | Condition | 81323004 | Normal general body function | _Berkebutuhan Khusus_ → `Condition.clinicalStatus.coding` (370, tanpa BQ) |
| 18 | 394–401 | RelatedPerson | – | – | _Nama Wali_ → `RelatedPerson.name.text` (394, tanpa BQ)<br>_Tahun Lahir_ → `RelatedPerson.birthDate` (395, tanpa BQ)<br>_NIK Wali_ → `RelatedPerson.identifier.value` (401, tanpa BQ) |
| 19 | 402–436 | Observation | 82589-3 | Highest level of education | _Pendidikan_ → `Observation.valueCodeableConcept.coding` (405, tanpa BQ) |
| 20 | 437–466 | Observation | OC000149 | Pekerjaan orang tua | _Pekerjaan_ → `Observation.valueCodeableConcept.coding` (440, tanpa BQ) |
| 21 | 467–487 | Observation | 365552003 | Finding of income details | _Penghasilan bulanan_ → `Observation.valueCodeableConcept.coding` (470, tanpa BQ) |
| 22 | 488–501 | Observation | SP000232 | Kartu Indonesia Pintar | _Apakah punya KIP_ → `Observation.valueBoolean` (489, tanpa BQ)<br>_Apakah peserta didik tersebut tetap akan menerima KIP_ → `Observation.component.code.coding` (491, tanpa BQ) |
| 23 | 502–508 | Account | – | – | – |
| 24 | 509–532 | Observation | SP000243 | Program Indonesia Pintar | _Alasan Layak PIP_ → `Observation.component.valueCodeableConcept.coding` (516, tanpa BQ) |
| 25 | 533–556 | Condition | 81323004 | Normal general body function | _Berkebutuhan Khusus_ → `Condition.clinicalStatus.coding` (533, tanpa BQ) |
| 26 | 557–567 | Observation | 365475008 | Place in family order | _Anak keberapa_ → `Observation.valueInteger` (560, tanpa BQ) |
| 27 | 568–592 | Observation | OC000149 | Pekerjaan orang tua | _Pekerjaan (diperuntukan untuk warga belajar)_ → `Observation.valueCodeableConcept.coding` (571, tanpa BQ) |
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
| 1 | 25 | Patient | `Patient.extension.valueCodeableConcept.coding` | SP000272 | Kepercayaan kepada Tuhan Yang Maha Esa | http://terminology.kemkes.go.id/sp |
| 2 | 33 | Observation | `Observation.code.coding` | 104890-9 | Nationality Person Narrative | http://loinc.org |
| 3 | 95 | Condition | `Condition.code.coding` | 170245002 | Child examination: school screening | http://snomed.info/sct |
| 4 | 112 | Observation | `Observation.code.coding` | 365481000 | Finding of household composition | http://snomed.info/sct |
| 5 | 113 | Observation | `Observation.valueCodeableConcept.coding` | 224137008 | Lives with parents | http://snomed.info/sct |
| 6 | 114 | Observation | `Observation.valueCodeableConcept.coding` | 25801000087105 | Lives with guardian | http://snomed.info/sct |
| 7 | 115 | Observation | `Observation.valueCodeableConcept.coding` | 1256010001 | Lives with others in shared housing | http://snomed.info/sct |
| 8 | 116 | Observation | `Observation.valueCodeableConcept.coding` | 307106009 | Lives in boarding school | http://snomed.info/sct |
| 9 | 117 | Observation | `Observation.valueCodeableConcept.coding` | 74056004 | Orphanage | http://snomed.info/sct |
| 10 | 118 | Observation | `Observation.valueCodeableConcept.coding` | SP000240 | Pesantren | http://terminology.kemkes.go.id/sp |
| 11 | 119 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 12 | 129 | Observation | `Observation.code.coding` | SP000241 | Moda Transportasi yang digunakan untuk bersekolah | http://terminology.kemkes.go.id/sp |
| 13 | 130 | Observation | `Observation.valueCodeableConcept.coding` | 129006008 | Walking | http://snomed.info/sct |
| 14 | 131 | Observation | `Observation.valueCodeableConcept.coding` | SP000242 | Angkutan umum | http://terminology.kemkes.go.id/sp |
| 15 | 132 | Observation | `Observation.valueCodeableConcept.coding` | SP000358 | Mobil/bus antar jemput | http://terminology.kemkes.go.id/sp |
| 16 | 133 | Observation | `Observation.valueCodeableConcept.coding` | 62193008 | Railway train, device | http://snomed.info/sct |
| 17 | 134 | Observation | `Observation.valueCodeableConcept.coding` | SP000359 | Ojek | http://terminology.kemkes.go.id/sp |
| 18 | 135 | Observation | `Observation.valueCodeableConcept.coding` | SP000360 | Andong/bendi/sado/dokar/delman/becak | http://terminology.kemkes.go.id/sp |
| 19 | 136 | Observation | `Observation.valueCodeableConcept.coding` | 12561005 | Watercraft, device | http://snomed.info/sct |
| 20 | 137 | Observation | `Observation.valueCodeableConcept.coding` | SP000361 | Kuda | http://terminology.kemkes.go.id/sp |
| 21 | 138 | Observation | `Observation.valueCodeableConcept.coding` | 70224005 | Bicycle, device | http://snomed.info/sct |
| 22 | 139 | Observation | `Observation.valueCodeableConcept.coding` | 90748009 | Motorcycle, device | http://snomed.info/sct |
| 23 | 140 | Observation | `Observation.valueCodeableConcept.coding` | 71783008 | Automobile, device | http://snomed.info/sct |
| 24 | 141 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 25 | 152 | Observation | `Observation.code.coding` | SP000239 | Kartu Perlindungan Sosial | http://terminology.kemkes.go.id/sp |
| 26 | 173 | Observation | `Observation.code.coding` | 82589-3 | Highest level of education | http://loinc.org |
| 27 | 174 | Observation | `Observation.valueCodeableConcept.coding` | 473463000 | Received elementary school education | http://snomed.info/sct |
| 28 | 175 | Observation | `Observation.valueCodeableConcept.coding` | 603435002 | Educated to junior high school level | http://snomed.info/sct |
| 29 | 176 | Observation | `Observation.valueCodeableConcept.coding` | 603434003 | Educated to senior high school level | http://snomed.info/sct |
| 30 | 177 | Observation | `Observation.valueCodeableConcept.coding` | 38861000087100 | Bachelor's degree achieved | http://snomed.info/sct |
| 31 | 178 | Observation | `Observation.valueCodeableConcept.coding` | 38881000087106 | Master's degree achieved | http://snomed.info/sct |
| 32 | 179 | Observation | `Observation.valueCodeableConcept.coding` | 440345007 | Doctorate degree achieved | http://snomed.info/sct |
| 33 | 180 | Observation | `Observation.valueCodeableConcept.coding` | 224294005 | No formal education | http://snomed.info/sct |
| 34 | 181 | Observation | `Observation.valueCodeableConcept.coding` | 741725004 | Primary school started but not finished | http://snomed.info/sct |
| 35 | 182 | Observation | `Observation.valueCodeableConcept.coding` | SP000275 | D1 | http://terminology.kemkes.go.id/sp |
| 36 | 183 | Observation | `Observation.valueCodeableConcept.coding` | SP000276 | D2 | http://terminology.kemkes.go.id/sp |
| 37 | 184 | Observation | `Observation.valueCodeableConcept.coding` | SP000277 | D3 | http://terminology.kemkes.go.id/sp |
| 38 | 185 | Observation | `Observation.valueCodeableConcept.coding` | SP000278 | Pendidikan Informal | http://terminology.kemkes.go.id/sp |
| 39 | 186 | Observation | `Observation.valueCodeableConcept.coding` | SP000279 | Pendidikan non formal | http://terminology.kemkes.go.id/sp |
| 40 | 187 | Observation | `Observation.valueCodeableConcept.coding` | SP000280 | Paket A | http://terminology.kemkes.go.id/sp |
| 41 | 188 | Observation | `Observation.valueCodeableConcept.coding` | SP000281 | Paket B | http://terminology.kemkes.go.id/sp |
| 42 | 189 | Observation | `Observation.valueCodeableConcept.coding` | SP000282 | Paket C | http://terminology.kemkes.go.id/sp |
| 43 | 190 | Observation | `Observation.valueCodeableConcept.coding` | 266982005 | Attending nursery school | http://snomed.info/sct |
| 44 | 191 | Observation | `Observation.valueCodeableConcept.coding` | SP000283 | Pendidikan Profesi | http://terminology.kemkes.go.id/sp |
| 45 | 192 | Observation | `Observation.valueCodeableConcept.coding` | SP000284 | S2 Terapan | http://terminology.kemkes.go.id/sp |
| 46 | 193 | Observation | `Observation.valueCodeableConcept.coding` | SP000285 | S3 Terapan | http://terminology.kemkes.go.id/sp |
| 47 | 194 | Observation | `Observation.valueCodeableConcept.coding` | SP000286 | Sekolah Profesi 1 | http://terminology.kemkes.go.id/sp |
| 48 | 195 | Observation | `Observation.valueCodeableConcept.coding` | SP000287 | Sekolah Profesi 2 | http://terminology.kemkes.go.id/sp |
| 49 | 196 | Observation | `Observation.valueCodeableConcept.coding` | 266983000 | Attending play group | http://snomed.info/sct |
| 50 | 197 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 51 | 208 | Observation | `Observation.code.coding` | OC000149 | Pekerjaan orang tua | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 52 | 209 | Observation | `Observation.valueCodeableConcept.coding` | 106540006 | Laborer | http://snomed.info/sct |
| 53 | 210 | Observation | `Observation.valueCodeableConcept.coding` | 160906004 | Self-employed | http://snomed.info/sct |
| 54 | 211 | Observation | `Observation.valueCodeableConcept.coding` | SP000244 | Pedagang kecil | http://terminology.kemkes.go.id/sp |
| 55 | 212 | Observation | `Observation.valueCodeableConcept.coding` | SP000362 | PNS/TNI/Polri | http://terminology.kemkes.go.id/sp |
| 56 | 213 | Observation | `Observation.valueCodeableConcept.coding` | 236297007 | Civil servant | http://snomed.info/sct |
| 57 | 214 | Observation | `Observation.valueCodeableConcept.coding` | 302314004 | Military personnel | http://snomed.info/sct |
| 58 | 215 | Observation | `Observation.valueCodeableConcept.coding` | 14406004 | Policeman | http://snomed.info/sct |
| 59 | 216 | Observation | `Observation.valueCodeableConcept.coding` | SP000245 | Wirausaha | http://terminology.kemkes.go.id/sp |
| 60 | 217 | Observation | `Observation.valueCodeableConcept.coding` | TK000041 | Pegawai/karyawan swasta | http://terminology.kemkes.go.id |
| 61 | 218 | Observation | `Observation.valueCodeableConcept.coding` | 73438004 | Unemployed | http://snomed.info/sct |
| 62 | 219 | Observation | `Observation.valueCodeableConcept.coding` | 77715000 | Fisherman | http://snomed.info/sct |
| 63 | 220 | Observation | `Observation.valueCodeableConcept.coding` | 106388008 | Farmer | http://snomed.info/sct |
| 64 | 221 | Observation | `Observation.valueCodeableConcept.coding` | 36625000 | Livestock worker | http://snomed.info/sct |
| 65 | 222 | Observation | `Observation.valueCodeableConcept.coding` | SP000274 | Pedagang besar | http://terminology.kemkes.go.id/sp |
| 66 | 223 | Observation | `Observation.valueCodeableConcept.coding` | 105493001 | Retired, life even | http://snomed.info/sct |
| 67 | 224 | Observation | `Observation.valueCodeableConcept.coding` | SP000288 | Tenaga Kerja Indonesia | http://terminology.kemkes.go.id/sp |
| 68 | 225 | Observation | `Observation.valueCodeableConcept.coding` | SP000289 | Karyawan BUMN | http://terminology.kemkes.go.id/sp |
| 69 | 226 | Observation | `Observation.valueCodeableConcept.coding` | 419099009 | Dead | http://snomed.info/sct |
| 70 | 227 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 71 | 228 | Observation | `Observation.dataAbsentReason.coding` | not-applicable | Not Applicable | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 72 | 238 | Condition | `Condition.category.coding` | special-needs | Special Needs | http://terminology.kemkes.go.id/sp |
| 73 | 239 | Condition | `Condition.code.coding` | 81323004 | Normal general body function | http://snomed.info/sct |
| 74 | 240 | Condition | `Condition.code.coding` | 397540003 | Visual impairment | http://snomed.info/sct |
| 75 | 241 | Condition | `Condition.code.coding` | 15188001 | Hearing loss | http://snomed.info/sct |
| 76 | 242 | Condition | `Condition.code.coding` | 86765009 | Mild intellectual disability | http://snomed.info/sct |
| 77 | 243 | Condition | `Condition.code.coding` | 61152003 | Moderate intellectual disability | http://snomed.info/sct |
| 78 | 244 | Condition | `Condition.code.coding` | 8510008 | Reduced mobility | http://snomed.info/sct |
| 79 | 245 | Condition | `Condition.code.coding` | 160693001 | Mobility poor | http://snomed.info/sct |
| 80 | 246 | Condition | `Condition.code.coding` | 5793009 | Mixed behavior and emotional disorder | http://snomed.info/sct |
| 81 | 247 | Condition | `Condition.code.coding` | 29164008 | Disturbance in speech | http://snomed.info/sct |
| 82 | 248 | Condition | `Condition.code.coding` | 406134008 | Multiple disability | http://snomed.info/sct |
| 83 | 249 | Condition | `Condition.code.coding` | 44548000 | Hyperactive behavior | http://snomed.info/sct |
| 84 | 250 | Condition | `Condition.code.coding` | 8273004 | Intelligence quotient high | http://snomed.info/sct |
| 85 | 251 | Condition | `Condition.code.coding` | 367358004 | Above average intellect | http://snomed.info/sct |
| 86 | 252 | Condition | `Condition.code.coding` | 1855002 | Developmental academic disorder | http://snomed.info/sct |
| 87 | 253 | Condition | `Condition.code.coding` | 70545002 | Narcotic drug user | http://snomed.info/sct |
| 88 | 254 | Condition | `Condition.code.coding` | 247701008 | Abnormal perception | http://snomed.info/sct |
| 89 | 255 | Condition | `Condition.code.coding` | 41040004 | Complete trisomy 21 syndrome | http://snomed.info/sct |
| 90 | 256 | Condition | `Condition.code.coding` | 35919005 | Pervasive developmental disorder | http://snomed.info/sct |
| 91 | 263 | Observation | `Observation.code.coding` | 365552003 | Finding of income details | http://snomed.info/sct |
| 92 | 264 | Observation | `Observation.valueCodeableConcept.coding` | 425111004 | No income | http://snomed.info/sct |
| 93 | 265 | Observation | `Observation.valueCodeableConcept.coding` | SP000233 | < Rp. 500.000 | http://terminology.kemkes.go.id/sp |
| 94 | 266 | Observation | `Observation.valueCodeableConcept.coding` | SP000234 | Rp. 500,000 - Rp. 999,999 | http://terminology.kemkes.go.id/sp |
| 95 | 267 | Observation | `Observation.valueCodeableConcept.coding` | SP000235 | Rp. 1,000,000 - Rp. 1,999,999 | http://terminology.kemkes.go.id/sp |
| 96 | 268 | Observation | `Observation.valueCodeableConcept.coding` | SP000236 | Rp. 2,000,000 - Rp. 4,999,999 | http://terminology.kemkes.go.id/sp |
| 97 | 269 | Observation | `Observation.valueCodeableConcept.coding` | SP000237 | Rp. 5,000,000 - Rp. 20.000.000 | http://terminology.kemkes.go.id/sp |
| 98 | 270 | Observation | `Observation.valueCodeableConcept.coding` | SP000238 | > Rp. 20.000.000 | http://terminology.kemkes.go.id/sp |
| 99 | 289 | Observation | `Observation.code.coding` | 82589-3 | Highest level of education | http://loinc.org |
| 100 | 290 | Observation | `Observation.valueCodeableConcept.coding` | 473463000 | Received elementary school education | http://snomed.info/sct |
| 101 | 291 | Observation | `Observation.valueCodeableConcept.coding` | 603435002 | Educated to junior high school level | http://snomed.info/sct |
| 102 | 292 | Observation | `Observation.valueCodeableConcept.coding` | 603434003 | Educated to senior high school level | http://snomed.info/sct |
| 103 | 293 | Observation | `Observation.valueCodeableConcept.coding` | 38861000087100 | Bachelor's degree achieved | http://snomed.info/sct |
| 104 | 294 | Observation | `Observation.valueCodeableConcept.coding` | 38881000087106 | Master's degree achieved | http://snomed.info/sct |
| 105 | 295 | Observation | `Observation.valueCodeableConcept.coding` | 440345007 | Doctorate degree achieved | http://snomed.info/sct |
| 106 | 296 | Observation | `Observation.valueCodeableConcept.coding` | 224294005 | No formal education | http://snomed.info/sct |
| 107 | 297 | Observation | `Observation.valueCodeableConcept.coding` | 741725004 | Primary school started but not finished | http://snomed.info/sct |
| 108 | 298 | Observation | `Observation.valueCodeableConcept.coding` | SP000275 | D1 | http://terminology.kemkes.go.id/sp |
| 109 | 299 | Observation | `Observation.valueCodeableConcept.coding` | SP000276 | D2 | http://terminology.kemkes.go.id/sp |
| 110 | 300 | Observation | `Observation.valueCodeableConcept.coding` | SP000277 | D3 | http://terminology.kemkes.go.id/sp |
| 111 | 301 | Observation | `Observation.valueCodeableConcept.coding` | SP000278 | Pendidikan Informal | http://terminology.kemkes.go.id/sp |
| 112 | 302 | Observation | `Observation.valueCodeableConcept.coding` | SP000279 | Pendidikan non formal | http://terminology.kemkes.go.id/sp |
| 113 | 303 | Observation | `Observation.valueCodeableConcept.coding` | SP000280 | Paket A | http://terminology.kemkes.go.id/sp |
| 114 | 304 | Observation | `Observation.valueCodeableConcept.coding` | SP000281 | Paket B | http://terminology.kemkes.go.id/sp |
| 115 | 305 | Observation | `Observation.valueCodeableConcept.coding` | SP000282 | Paket C | http://terminology.kemkes.go.id/sp |
| 116 | 306 | Observation | `Observation.valueCodeableConcept.coding` | 266982005 | Attending nursery school | http://snomed.info/sct |
| 117 | 307 | Observation | `Observation.valueCodeableConcept.coding` | SP000283 | Pendidikan Profesi | http://terminology.kemkes.go.id/sp |
| 118 | 308 | Observation | `Observation.valueCodeableConcept.coding` | SP000284 | S2 Terapan | http://terminology.kemkes.go.id/sp |
| 119 | 309 | Observation | `Observation.valueCodeableConcept.coding` | SP000285 | S3 Terapan | http://terminology.kemkes.go.id/sp |
| 120 | 310 | Observation | `Observation.valueCodeableConcept.coding` | SP000286 | Sekolah Profesi 1 | http://terminology.kemkes.go.id/sp |
| 121 | 311 | Observation | `Observation.valueCodeableConcept.coding` | SP000287 | Sekolah Profesi 2 | http://terminology.kemkes.go.id/sp |
| 122 | 312 | Observation | `Observation.valueCodeableConcept.coding` | 266983000 | Attending play group | http://snomed.info/sct |
| 123 | 313 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 124 | 324 | Observation | `Observation.code.coding` | OC000149 | Pekerjaan orang tua | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 125 | 325 | Observation | `Observation.valueCodeableConcept.coding` | 106540006 | Laborer | http://snomed.info/sct |
| 126 | 326 | Observation | `Observation.valueCodeableConcept.coding` | 160906004 | Self-employed | http://snomed.info/sct |
| 127 | 327 | Observation | `Observation.valueCodeableConcept.coding` | SP000244 | Pedagang kecil | http://terminology.kemkes.go.id/sp |
| 128 | 328 | Observation | `Observation.valueCodeableConcept.coding` | 236297007 | Civil servant | http://snomed.info/sct |
| 129 | 329 | Observation | `Observation.valueCodeableConcept.coding` | 302314004 | Military personnel | http://snomed.info/sct |
| 130 | 330 | Observation | `Observation.valueCodeableConcept.coding` | 14406004 | Policeman | http://snomed.info/sct |
| 131 | 331 | Observation | `Observation.valueCodeableConcept.coding` | SP000245 | Wirausaha | http://terminology.kemkes.go.id/sp |
| 132 | 332 | Observation | `Observation.valueCodeableConcept.coding` | TK000041 | Pegawai/karyawan swasta | http://terminology.kemkes.go.id |
| 133 | 333 | Observation | `Observation.valueCodeableConcept.coding` | 73438004 | Unemployed | http://snomed.info/sct |
| 134 | 334 | Observation | `Observation.valueCodeableConcept.coding` | 77715000 | Fisherman | http://snomed.info/sct |
| 135 | 335 | Observation | `Observation.valueCodeableConcept.coding` | 106388008 | Farmer | http://snomed.info/sct |
| 136 | 336 | Observation | `Observation.valueCodeableConcept.coding` | 36625000 | Livestock worker | http://snomed.info/sct |
| 137 | 337 | Observation | `Observation.valueCodeableConcept.coding` | SP000274 | Pedagang besar | http://terminology.kemkes.go.id/sp |
| 138 | 338 | Observation | `Observation.valueCodeableConcept.coding` | 105493001 | Retired, life even | http://snomed.info/sct |
| 139 | 339 | Observation | `Observation.valueCodeableConcept.coding` | SP000288 | Tenaga Kerja Indonesia | http://terminology.kemkes.go.id/sp |
| 140 | 340 | Observation | `Observation.valueCodeableConcept.coding` | SP000289 | Karyawan BUMN | http://terminology.kemkes.go.id/sp |
| 141 | 341 | Observation | `Observation.valueCodeableConcept.coding` | 419099009 | Dead | http://snomed.info/sct |
| 142 | 342 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 143 | 343 | Observation | `Observation.dataAbsentReason.coding` | not-applicable | Not Applicable | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 144 | 354 | Observation | `Observation.code.coding` | 365552003 | Finding of income details | http://snomed.info/sct |
| 145 | 355 | Observation | `Observation.valueCodeableConcept.coding` | 425111004 | No income | http://snomed.info/sct |
| 146 | 356 | Observation | `Observation.valueCodeableConcept.coding` | SP000233 | < Rp. 500.000 | http://terminology.kemkes.go.id/sp |
| 147 | 357 | Observation | `Observation.valueCodeableConcept.coding` | SP000234 | Rp. 500,000 - Rp. 999,999 | http://terminology.kemkes.go.id/sp |
| 148 | 358 | Observation | `Observation.valueCodeableConcept.coding` | SP000235 | Rp. 1,000,000 - Rp. 1,999,999 | http://terminology.kemkes.go.id/sp |
| 149 | 359 | Observation | `Observation.valueCodeableConcept.coding` | SP000236 | Rp. 2,000,000 - Rp. 4,999,999 | http://terminology.kemkes.go.id/sp |
| 150 | 360 | Observation | `Observation.valueCodeableConcept.coding` | SP000237 | Rp. 5,000,000 - Rp. 20.000.000 | http://terminology.kemkes.go.id/sp |
| 151 | 361 | Observation | `Observation.valueCodeableConcept.coding` | SP000238 | > Rp. 20.000.000 | http://terminology.kemkes.go.id/sp |
| 152 | 371 | Condition | `Condition.category.coding` | special-needs | Special Needs | http://terminology.kemkes.go.id/sp |
| 153 | 372 | Condition | `Condition.code.coding` | 81323004 | Normal general body function | http://snomed.info/sct |
| 154 | 373 | Condition | `Condition.code.coding` | 397540003 | Visual impairment | http://snomed.info/sct |
| 155 | 374 | Condition | `Condition.code.coding` | 15188001 | Hearing loss | http://snomed.info/sct |
| 156 | 375 | Condition | `Condition.code.coding` | 86765009 | Mild intellectual disability | http://snomed.info/sct |
| 157 | 376 | Condition | `Condition.code.coding` | 61152003 | Moderate intellectual disability | http://snomed.info/sct |
| 158 | 377 | Condition | `Condition.code.coding` | 8510008 | Reduced mobility | http://snomed.info/sct |
| 159 | 378 | Condition | `Condition.code.coding` | 160693001 | Mobility poor | http://snomed.info/sct |
| 160 | 379 | Condition | `Condition.code.coding` | 5793009 | Mixed behavior and emotional disorder | http://snomed.info/sct |
| 161 | 380 | Condition | `Condition.code.coding` | 29164008 | Disturbance in speech | http://snomed.info/sct |
| 162 | 381 | Condition | `Condition.code.coding` | 406134008 | Multiple disability | http://snomed.info/sct |
| 163 | 382 | Condition | `Condition.code.coding` | 44548000 | Hyperactive behavior | http://snomed.info/sct |
| 164 | 383 | Condition | `Condition.code.coding` | 8273004 | Intelligence quotient high | http://snomed.info/sct |
| 165 | 384 | Condition | `Condition.code.coding` | 367358004 | Above average intellect | http://snomed.info/sct |
| 166 | 385 | Condition | `Condition.code.coding` | 1855002 | Developmental academic disorder | http://snomed.info/sct |
| 167 | 386 | Condition | `Condition.code.coding` | 70545002 | Narcotic drug user | http://snomed.info/sct |
| 168 | 387 | Condition | `Condition.code.coding` | 247701008 | Abnormal perception | http://snomed.info/sct |
| 169 | 388 | Condition | `Condition.code.coding` | 41040004 | Complete trisomy 21 syndrome | http://snomed.info/sct |
| 170 | 389 | Condition | `Condition.code.coding` | 35919005 | Pervasive developmental disorder | http://snomed.info/sct |
| 171 | 404 | Observation | `Observation.code.coding` | 82589-3 | Highest level of education | http://loinc.org |
| 172 | 405 | Observation | `Observation.valueCodeableConcept.coding` | 473463000 | Received elementary school education | http://snomed.info/sct |
| 173 | 406 | Observation | `Observation.valueCodeableConcept.coding` | 603435002 | Educated to junior high school level | http://snomed.info/sct |
| 174 | 407 | Observation | `Observation.valueCodeableConcept.coding` | 603434003 | Educated to senior high school level | http://snomed.info/sct |
| 175 | 408 | Observation | `Observation.valueCodeableConcept.coding` | 38861000087100 | Bachelor's degree achieved | http://snomed.info/sct |
| 176 | 409 | Observation | `Observation.valueCodeableConcept.coding` | 38881000087106 | Master's degree achieved | http://snomed.info/sct |
| 177 | 410 | Observation | `Observation.valueCodeableConcept.coding` | 440345007 | Doctorate degree achieved | http://snomed.info/sct |
| 178 | 411 | Observation | `Observation.valueCodeableConcept.coding` | 224294005 | No formal education | http://snomed.info/sct |
| 179 | 412 | Observation | `Observation.valueCodeableConcept.coding` | 741725004 | Primary school started but not finished | http://snomed.info/sct |
| 180 | 413 | Observation | `Observation.valueCodeableConcept.coding` | SP000275 | D1 | http://terminology.kemkes.go.id/sp |
| 181 | 414 | Observation | `Observation.valueCodeableConcept.coding` | SP000276 | D2 | http://terminology.kemkes.go.id/sp |
| 182 | 415 | Observation | `Observation.valueCodeableConcept.coding` | SP000277 | D3 | http://terminology.kemkes.go.id/sp |
| 183 | 416 | Observation | `Observation.valueCodeableConcept.coding` | SP000278 | Pendidikan Informal | http://terminology.kemkes.go.id/sp |
| 184 | 417 | Observation | `Observation.valueCodeableConcept.coding` | SP000279 | Pendidikan non formal | http://terminology.kemkes.go.id/sp |
| 185 | 418 | Observation | `Observation.valueCodeableConcept.coding` | SP000280 | Paket A | http://terminology.kemkes.go.id/sp |
| 186 | 419 | Observation | `Observation.valueCodeableConcept.coding` | SP000281 | Paket B | http://terminology.kemkes.go.id/sp |
| 187 | 420 | Observation | `Observation.valueCodeableConcept.coding` | SP000282 | Paket C | http://terminology.kemkes.go.id/sp |
| 188 | 421 | Observation | `Observation.valueCodeableConcept.coding` | 266982005 | Attending nursery school | http://snomed.info/sct |
| 189 | 422 | Observation | `Observation.valueCodeableConcept.coding` | SP000283 | Pendidikan Profesi | http://terminology.kemkes.go.id/sp |
| 190 | 423 | Observation | `Observation.valueCodeableConcept.coding` | SP000284 | S2 Terapan | http://terminology.kemkes.go.id/sp |
| 191 | 424 | Observation | `Observation.valueCodeableConcept.coding` | SP000285 | S3 Terapan | http://terminology.kemkes.go.id/sp |
| 192 | 425 | Observation | `Observation.valueCodeableConcept.coding` | SP000286 | Sekolah Profesi 1 | http://terminology.kemkes.go.id/sp |
| 193 | 426 | Observation | `Observation.valueCodeableConcept.coding` | SP000287 | Sekolah Profesi 2 | http://terminology.kemkes.go.id/sp |
| 194 | 427 | Observation | `Observation.valueCodeableConcept.coding` | 266983000 | Attending play group | http://snomed.info/sct |
| 195 | 428 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 196 | 439 | Observation | `Observation.code.coding` | OC000149 | Pekerjaan orang tua | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 197 | 440 | Observation | `Observation.valueCodeableConcept.coding` | 106540006 | Laborer | http://snomed.info/sct |
| 198 | 441 | Observation | `Observation.valueCodeableConcept.coding` | 160906004 | Self-employed | http://snomed.info/sct |
| 199 | 442 | Observation | `Observation.valueCodeableConcept.coding` | SP000244 | Pedagang kecil | http://terminology.kemkes.go.id/sp |
| 200 | 443 | Observation | `Observation.valueCodeableConcept.coding` | 236297007 | Civil servant | http://snomed.info/sct |
| 201 | 444 | Observation | `Observation.valueCodeableConcept.coding` | 302314004 | Military personnel | http://snomed.info/sct |
| 202 | 445 | Observation | `Observation.valueCodeableConcept.coding` | 14406004 | Policeman | http://snomed.info/sct |
| 203 | 446 | Observation | `Observation.valueCodeableConcept.coding` | SP000245 | Wirausaha | http://terminology.kemkes.go.id/sp |
| 204 | 447 | Observation | `Observation.valueCodeableConcept.coding` | TK000041 | Pegawai/karyawan swasta | http://terminology.kemkes.go.id |
| 205 | 448 | Observation | `Observation.valueCodeableConcept.coding` | 73438004 | Unemployed | http://snomed.info/sct |
| 206 | 449 | Observation | `Observation.valueCodeableConcept.coding` | 77715000 | Fisherman | http://snomed.info/sct |
| 207 | 450 | Observation | `Observation.valueCodeableConcept.coding` | 106388008 | Farmer | http://snomed.info/sct |
| 208 | 451 | Observation | `Observation.valueCodeableConcept.coding` | 36625000 | Livestock worker | http://snomed.info/sct |
| 209 | 452 | Observation | `Observation.valueCodeableConcept.coding` | SP000274 | Pedagang besar | http://terminology.kemkes.go.id/sp |
| 210 | 453 | Observation | `Observation.valueCodeableConcept.coding` | 105493001 | Retired, life even | http://snomed.info/sct |
| 211 | 454 | Observation | `Observation.valueCodeableConcept.coding` | SP000288 | Tenaga Kerja Indonesia | http://terminology.kemkes.go.id/sp |
| 212 | 455 | Observation | `Observation.valueCodeableConcept.coding` | SP000289 | Karyawan BUMN | http://terminology.kemkes.go.id/sp |
| 213 | 456 | Observation | `Observation.valueCodeableConcept.coding` | 419099009 | Dead | http://snomed.info/sct |
| 214 | 457 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 215 | 458 | Observation | `Observation.dataAbsentReason.coding` | not-applicable | Not Applicable | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 216 | 469 | Observation | `Observation.code.coding` | 365552003 | Finding of income details | http://snomed.info/sct |
| 217 | 470 | Observation | `Observation.valueCodeableConcept.coding` | 425111004 | No income | http://snomed.info/sct |
| 218 | 471 | Observation | `Observation.valueCodeableConcept.coding` | SP000233 | < Rp. 500.000 | http://terminology.kemkes.go.id/sp |
| 219 | 472 | Observation | `Observation.valueCodeableConcept.coding` | SP000234 | Rp. 500,000 - Rp. 999,999 | http://terminology.kemkes.go.id/sp |
| 220 | 473 | Observation | `Observation.valueCodeableConcept.coding` | SP000235 | Rp. 1,000,000 - Rp. 1,999,999 | http://terminology.kemkes.go.id/sp |
| 221 | 474 | Observation | `Observation.valueCodeableConcept.coding` | SP000236 | Rp. 2,000,000 - Rp. 4,999,999 | http://terminology.kemkes.go.id/sp |
| 222 | 475 | Observation | `Observation.valueCodeableConcept.coding` | SP000237 | Rp. 5,000,000 - Rp. 20.000.000 | http://terminology.kemkes.go.id/sp |
| 223 | 476 | Observation | `Observation.valueCodeableConcept.coding` | SP000238 | > Rp. 20.000.000 | http://terminology.kemkes.go.id/sp |
| 224 | 488 | Observation | `Observation.code.coding` | SP000232 | Kartu Indonesia Pintar | http://terminology.kemkes.go.id/sp |
| 225 | 491 | Observation | `Observation.component.code.coding` | SP000327 | Tetap akan menerima KIP | http://terminology.kemkes.go.id/sp |
| 226 | 511 | Observation | `Observation.code.coding` | SP000243 | Program Indonesia Pintar | http://terminology.kemkes.go.id/sp |
| 227 | 512 | Observation | `Observation.component.code.coding` | SP000317 | Layak menerima PIP | http://terminology.kemkes.go.id/sp |
| 228 | 515 | Observation | `Observation.component.code.coding` | SP000318 | Alasan Layak PIP | http://terminology.kemkes.go.id/sp |
| 229 | 516 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000319 | Daerah konflik | http://terminology.kemkes.go.id/sp |
| 230 | 517 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000320 | Dampak bencana | http://terminology.kemkes.go.id/sp |
| 231 | 518 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000321 | Kelainan fisik | http://terminology.kemkes.go.id/sp |
| 232 | 519 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000322 | Keluarga narapidana | http://terminology.kemkes.go.id/sp |
| 233 | 520 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000323 | Pemegang PKH/KPS/KKS | http://terminology.kemkes.go.id/sp |
| 234 | 521 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000324 | Pernah Dropout | http://terminology.kemkes.go.id/sp |
| 235 | 522 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000325 | Siswa miskin/rentan miskin | http://terminology.kemkes.go.id/sp |
| 236 | 523 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000326 | Yatim Piatu/Panti Asuhan/Panti Sosial | http://terminology.kemkes.go.id/sp |
| 237 | 534 | Condition | `Condition.category.coding` | special-needs | Special Needs | http://terminology.kemkes.go.id/sp |
| 238 | 535 | Condition | `Condition.code.coding` | 81323004 | Normal general body function | http://snomed.info/sct |
| 239 | 536 | Condition | `Condition.code.coding` | 397540003 | Visual impairment | http://snomed.info/sct |
| 240 | 537 | Condition | `Condition.code.coding` | 15188001 | Hearing loss | http://snomed.info/sct |
| 241 | 538 | Condition | `Condition.code.coding` | 86765009 | Mild intellectual disability | http://snomed.info/sct |
| 242 | 539 | Condition | `Condition.code.coding` | 61152003 | Moderate intellectual disability | http://snomed.info/sct |
| 243 | 540 | Condition | `Condition.code.coding` | 8510008 | Reduced mobility | http://snomed.info/sct |
| 244 | 541 | Condition | `Condition.code.coding` | 160693001 | Mobility poor | http://snomed.info/sct |
| 245 | 542 | Condition | `Condition.code.coding` | 5793009 | Mixed behavior and emotional disorder | http://snomed.info/sct |
| 246 | 543 | Condition | `Condition.code.coding` | 29164008 | Disturbance in speech | http://snomed.info/sct |
| 247 | 544 | Condition | `Condition.code.coding` | 406134008 | Multiple disability | http://snomed.info/sct |
| 248 | 545 | Condition | `Condition.code.coding` | 44548000 | Hyperactive behavior | http://snomed.info/sct |
| 249 | 546 | Condition | `Condition.code.coding` | 8273004 | Intelligence quotient high | http://snomed.info/sct |
| 250 | 547 | Condition | `Condition.code.coding` | 367358004 | Above average intellect | http://snomed.info/sct |
| 251 | 548 | Condition | `Condition.code.coding` | 1855002 | Developmental academic disorder | http://snomed.info/sct |
| 252 | 549 | Condition | `Condition.code.coding` | 70545002 | Narcotic drug user | http://snomed.info/sct |
| 253 | 550 | Condition | `Condition.code.coding` | 247701008 | Abnormal perception | http://snomed.info/sct |
| 254 | 551 | Condition | `Condition.code.coding` | 41040004 | Complete trisomy 21 syndrome | http://snomed.info/sct |
| 255 | 552 | Condition | `Condition.code.coding` | 35919005 | Pervasive developmental disorder | http://snomed.info/sct |
| 256 | 559 | Observation | `Observation.code.coding` | 365475008 | Place in family order | http://snomed.info/sct |
| 257 | 570 | Observation | `Observation.code.coding` | OC000149 | Pekerjaan orang tua | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 258 | 571 | Observation | `Observation.valueCodeableConcept.coding` | 73438004 | Unemployed | http://snomed.info/sct |
| 259 | 572 | Observation | `Observation.valueCodeableConcept.coding` | 77715000 | Fisherman | http://snomed.info/sct |
| 260 | 573 | Observation | `Observation.valueCodeableConcept.coding` | 106388008 | Farmer | http://snomed.info/sct |
| 261 | 574 | Observation | `Observation.valueCodeableConcept.coding` | 36625000 | Livestock worker | http://snomed.info/sct |
| 262 | 575 | Observation | `Observation.valueCodeableConcept.coding` | 236297007 | Civil servant | http://snomed.info/sct |
| 263 | 576 | Observation | `Observation.valueCodeableConcept.coding` | 302314004 | Military personnel | http://snomed.info/sct |
| 264 | 577 | Observation | `Observation.valueCodeableConcept.coding` | 14406004 | Policeman | http://snomed.info/sct |
| 265 | 578 | Observation | `Observation.valueCodeableConcept.coding` | TK000041 | Pegawai/karyawan swasta | http://terminology.kemkes.go.id |
| 266 | 579 | Observation | `Observation.valueCodeableConcept.coding` | SP000244 | Pedagang kecil | http://terminology.kemkes.go.id/sp |
| 267 | 580 | Observation | `Observation.valueCodeableConcept.coding` | SP000274 | Pedagang besar | http://terminology.kemkes.go.id/sp |
| 268 | 581 | Observation | `Observation.valueCodeableConcept.coding` | 160906004 | Self-employed | http://snomed.info/sct |
| 269 | 582 | Observation | `Observation.valueCodeableConcept.coding` | SP000245 | Wirausaha | http://terminology.kemkes.go.id/sp |
| 270 | 583 | Observation | `Observation.valueCodeableConcept.coding` | 106540006 | Laborer | http://snomed.info/sct |
| 271 | 584 | Observation | `Observation.valueCodeableConcept.coding` | 105493001 | Retired, life even | http://snomed.info/sct |
| 272 | 595 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 273 | 607 | Observation | `Observation.code.coding` | 8302-2 | Body height | http://loinc.org |
| 274 | 619 | Observation | `Observation.code.coding` | 9843-4 | Head Occipital-frontal circumference | http://loinc.org |
| 275 | 632 | Observation | `Observation.code.coding` | 224095004 | Number of siblings | http://snomed.info/sct |
| 276 | 644 | Observation | `Observation.code.coding` | SP000230 | Jarak dari rumah ke sekolah | http://terminology.kemkes.go.id/sp |
| 277 | 645 | Observation | `Observation.valueCodeableConcept.coding` | SP000290 | Kurang dari 1 km | http://terminology.kemkes.go.id/sp |
| 278 | 646 | Observation | `Observation.valueCodeableConcept.coding` | SP000291 | Lebih dari 1 km | http://terminology.kemkes.go.id/sp |
| 279 | 656 | Observation | `Observation.code.coding` | SP000292 | Jarak dari rumah ke sekolah (km) | http://terminology.kemkes.go.id/sp |
| 280 | 668 | Observation | `Observation.code.coding` | SP000293 | Waktu tempuh dari rumah ke sekolah | http://terminology.kemkes.go.id/sp |
| 281 | 679 | Observation | `Observation.code.coding` | 105421008 | Educational achievement | http://snomed.info/sct |
| 282 | 680 | Observation | `Observation.component.code.coding` | SP000294 | Jenis Prestasi | http://terminology.kemkes.go.id/sp |
| 283 | 681 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000300 | Sains | http://terminology.kemkes.go.id/sp |
| 284 | 682 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000301 | Seni | http://terminology.kemkes.go.id/sp |
| 285 | 683 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000302 | Olahraga | http://terminology.kemkes.go.id/sp |
| 286 | 684 | Observation | `Observation.component.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 287 | 685 | Observation | `Observation.component.code.coding` | SP000295 | Tingkatan Prestasi | http://terminology.kemkes.go.id/sp |
| 288 | 686 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000303 | Tingkat Sekolah | http://terminology.kemkes.go.id/sp |
| 289 | 687 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000304 | Tingkat Kecamatan | http://terminology.kemkes.go.id/sp |
| 290 | 688 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000305 | Tingkat Kabupaten | http://terminology.kemkes.go.id/sp |
| 291 | 689 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000306 | Tingkat Provinsi | http://terminology.kemkes.go.id/sp |
| 292 | 690 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000307 | Tingkat Nasional | http://terminology.kemkes.go.id/sp |
| 293 | 691 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000308 | Tingkat Internasional | http://terminology.kemkes.go.id/sp |
| 294 | 692 | Observation | `Observation.component.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 295 | 693 | Observation | `Observation.component.code.coding` | SP000297 | Nama Prestasi | http://terminology.kemkes.go.id/sp |
| 296 | 695 | Observation | `Observation.component.code.coding` | SP000298 | Tahun Prestasi | http://terminology.kemkes.go.id/sp |
| 297 | 697 | Observation | `Observation.component.code.coding` | SP000299 | Penyelenggara | http://terminology.kemkes.go.id/sp |
| 298 | 708 | Observation | `Observation.code.coding` | SP000309 | Beasiswa | http://terminology.kemkes.go.id/sp |
| 299 | 709 | Observation | `Observation.component.code.coding` | SP000310 | Jenis Beasiswa | http://terminology.kemkes.go.id/sp |
| 300 | 710 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000311 | Beasiswa Anak berprestasi | http://terminology.kemkes.go.id/sp |
| 301 | 711 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000312 | Beasiswa Anak miskin/kemiskinan | http://terminology.kemkes.go.id/sp |
| 302 | 712 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000313 | Beasiswa Pendidikan | http://terminology.kemkes.go.id/sp |
| 303 | 713 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000314 | Beasiswa Unggulan | http://terminology.kemkes.go.id/sp |
| 304 | 714 | Observation | `Observation.component.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 305 | 715 | Observation | `Observation.component.code.coding` | SP000315 | Keterangan Beasiswa | http://terminology.kemkes.go.id/sp |
| 306 | 717 | Observation | `Observation.component.code.coding` | SP000316 | Periode Beasiswa | http://terminology.kemkes.go.id/sp |
| 307 | 729 | Observation | `Observation.code.coding` | SP000328 | Asuransi Kesejahteraan | http://terminology.kemkes.go.id/sp |
| 308 | 730 | Observation | `Observation.code.coding` | SP000329 | Dana Pensiun | http://terminology.kemkes.go.id/sp |
| 309 | 731 | Observation | `Observation.code.coding` | SP000330 | Jamkesmas | http://terminology.kemkes.go.id/sp |
| 310 | 732 | Observation | `Observation.code.coding` | SP000331 | Jamsostek | http://terminology.kemkes.go.id/sp |
| 311 | 733 | Observation | `Observation.code.coding` | SP000332 | BPJS | http://terminology.kemkes.go.id/sp |
| 312 | 734 | Observation | `Observation.code.coding` | SP000333 | Kartu Keluarga Sejahtera | http://terminology.kemkes.go.id/sp |
| 313 | 735 | Observation | `Observation.code.coding` | SP000334 | Kartu Indonesia Sehat | http://terminology.kemkes.go.id/sp |
| 314 | 736 | Observation | `Observation.code.coding` | SP000335 | Otonomi Khusus Papua | http://terminology.kemkes.go.id/sp |
| 315 | 737 | Observation | `Observation.code.coding` | SP000336 | Program Keluarga Harapan | http://terminology.kemkes.go.id/sp |
| 316 | 738 | Observation | `Observation.code.coding` | SP000243 | Program Indonesia Pintar | http://terminology.kemkes.go.id/sp |
| 317 | 739 | Observation | `Observation.code.coding` | SP000239 | Kartu Perlindungan Sosial | http://terminology.kemkes.go.id/sp |
| 318 | 755 | Observation | `Observation.code.coding` | 276031006 | Details of education | http://snomed.info/sct |
| 319 | 756 | Observation | `Observation.component.code.coding` | SP000337 | Kompetensi Keahlian (SMK) | http://terminology.kemkes.go.id/sp |
| 320 | 758 | Observation | `Observation.component.code.coding` | SP000338 | Jenis Pendaftaran | http://terminology.kemkes.go.id/sp |
| 321 | 759 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000339 | Siswa baru | http://terminology.kemkes.go.id/sp |
| 322 | 760 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000340 | Siswa Pindahan | http://terminology.kemkes.go.id/sp |
| 323 | 761 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000341 | Kembali bersekolah | http://terminology.kemkes.go.id/sp |
| 324 | 762 | Observation | `Observation.component.code.coding` | 224293004 | Education received in the past | http://snomed.info/sct |
| 325 | 764 | Observation | `Observation.component.code.coding` | SP000342 | Jenis Lembaga Pendidikan | http://terminology.kemkes.go.id/sp |
| 326 | 765 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000343 | Formal | http://terminology.kemkes.go.id/sp |
| 327 | 766 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000344 | Informal | http://terminology.kemkes.go.id/sp |
| 328 | 768 | Observation | `Observation.component.code.coding` | SP000345 | Tanggal masuk sekolah | http://terminology.kemkes.go.id/sp |
| 329 | 770 | Observation | `Observation.component.code.coding` | SP000346 | Rombongan Belajar | http://terminology.kemkes.go.id/sp |
| 330 | 772 | Observation | `Observation.component.code.coding` | SP000347 | No Peserta Ujian Nasional | http://terminology.kemkes.go.id/sp |
| 331 | 774 | Observation | `Observation.component.code.coding` | SP000348 | No Seri Ijazah | http://terminology.kemkes.go.id/sp |
| 332 | 776 | Observation | `Observation.component.code.coding` | SP000349 | No SKHUN/SHUN | http://terminology.kemkes.go.id/sp |
| 333 | 778 | Observation | `Observation.component.code.coding` | SP000350 | Alasan utama keluar sekolah | http://terminology.kemkes.go.id/sp |
| 334 | 779 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000351 | Mutasi | http://terminology.kemkes.go.id/sp |
| 335 | 780 | Observation | `Observation.component.valueCodeableConcept.coding` | 228137002 | Excluded from school permanently |  |
| 336 | 781 | Observation | `Observation.component.valueCodeableConcept.coding` | 161131005 | Left school free will |  |
| 337 | 782 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000352 | Putus sekolah | http://terminology.kemkes.go.id/sp |
| 338 | 783 | Observation | `Observation.component.valueCodeableConcept.coding` | 419099009 | Dead |  |
| 339 | 784 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000353 | Hilang | http://terminology.kemkes.go.id/sp |
| 340 | 785 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000354 | Lulus | http://terminology.kemkes.go.id/sp |
| 341 | 786 | Observation | `Observation.component.code.coding` | SP000355 | Tanggal keluar sekolah | http://terminology.kemkes.go.id/sp |
| 342 | 788 | Observation | `Observation.component.code.coding` | SP000356 | Alasan khusus keluar sekolah | http://terminology.kemkes.go.id/sp |
| 343 | 799 | Observation | `Observation.code.coding` | 63764-5 | Hobby [LIBCSP] | http://loinc.org |
| 344 | 836 | Observation | `Observation.code.coding` | SP000357 | Cita-cita | http://terminology.kemkes.go.id/sp |
| 345 | 883 | Observation | `Observation.code.coding` | 63764-5 | Hobby [LIBCSP] | http://loinc.org |
| 346 | 884 | Observation | `Observation.valueCodeableConcept.coding` | 129011005 | Shopping | http://snomed.info/sct |
| 347 | 885 | Observation | `Observation.valueCodeableConcept.coding` | 10496000 | Camping | http://snomed.info/sct |
| 348 | 886 | Observation | `Observation.valueCodeableConcept.coding` | 418060005 | Running | http://snomed.info/sct |
| 349 | 888 | Observation | `Observation.valueCodeableConcept.coding` | 88289009 | Soccer | http://snomed.info/sct |
| 350 | 889 | Observation | `Observation.valueCodeableConcept.coding` | 26550000 | Tennis | http://snomed.info/sct |
| 351 | 895 | Observation | `Observation.valueCodeableConcept.coding` | 84096006 | Surfing | http://snomed.info/sct |
| 352 | 898 | Observation | `Observation.valueCodeableConcept.coding` | 1968006 | Jogging | http://snomed.info/sct |
| 353 | 901 | Observation | `Observation.valueCodeableConcept.coding` | 48263008 | Eating | http://snomed.info/sct |
| 354 | 902 | Observation | `Observation.valueCodeableConcept.coding` | 1137717005 | Fishing | http://snomed.info/sct |
| 355 | 903 | Observation | `Observation.valueCodeableConcept.coding` | 50360004 | Reading | http://snomed.info/sct |
| 356 | 904 | Observation | `Observation.valueCodeableConcept.coding` | 111055000 | Mountain climbing | http://snomed.info/sct |
| 357 | 908 | Observation | `Observation.valueCodeableConcept.coding` | 14468000 | Sports activity | http://snomed.info/sct |
| 358 | 909 | Observation | `Observation.valueCodeableConcept.coding` | 129018004 | Traveling | http://snomed.info/sct |
| 359 | 910 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 360 | 920 | Observation | `Observation.code.coding` | SP000357 | Cita-cita | http://terminology.kemkes.go.id/sp |
| 361 | 921 | Observation | `Observation.valueCodeableConcept.coding` | 308047006 | Architect | http://snomed.info/sct |
| 362 | 925 | Observation | `Observation.valueCodeableConcept.coding` | 106325008 | Athlete, sportsman/related worker | http://snomed.info/sct |
| 363 | 926 | Observation | `Observation.valueCodeableConcept.coding` | 75271001 | Professional midwife | http://snomed.info/sct |
| 364 | 930 | Observation | `Observation.valueCodeableConcept.coding` | 158965000 | Medical practitioner | http://snomed.info/sct |
| 365 | 931 | Observation | `Observation.valueCodeableConcept.coding` | 265945005 | Performer (entertainment) | http://snomed.info/sct |
| 366 | 933 | Observation | `Observation.valueCodeableConcept.coding` | 308207007 | Chef | http://snomed.info/sct |
| 367 | 935 | Observation | `Observation.valueCodeableConcept.coding` | 236297007 | Civil servant | http://snomed.info/sct |
| 368 | 941 | Observation | `Observation.valueCodeableConcept.coding` | 12877000 | Lawyer | http://snomed.info/sct |
| 369 | 944 | Observation | `Observation.valueCodeableConcept.coding` | 308004006 | Writer | http://snomed.info/sct |
| 370 | 945 | Observation | `Observation.valueCodeableConcept.coding` | 78705009 | Radio and television announcer | http://snomed.info/sct |
| 371 | 946 | Observation | `Observation.valueCodeableConcept.coding` | 106292003 | Professional nurse | http://snomed.info/sct |
| 372 | 947 | Observation | `Observation.valueCodeableConcept.coding` | 308040008 | Pilot - aircraft | http://snomed.info/sct |
| 373 | 948 | Observation | `Observation.valueCodeableConcept.coding` | 14406004 | Policeman | http://snomed.info/sct |
| 374 | 951 | Observation | `Observation.valueCodeableConcept.coding` | 159062006 | Artist | http://snomed.info/sct |
| 375 | 952 | Observation | `Observation.valueCodeableConcept.coding` | OV000433 | TNI/ Polri | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 376 | 953 | Observation | `Observation.valueCodeableConcept.coding` | 80409005 | Translator | http://snomed.info/sct |
| 377 | 955 | Observation | `Observation.valueCodeableConcept.coding` | 29536009 | Journalist | http://snomed.info/sct |
| 378 | 956 | Observation | `Observation.valueCodeableConcept.coding` | 160906004 | Self-employed | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 193 |
| http://terminology.kemkes.go.id/sp | 161 |
| http://loinc.org | 9 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 5 |
| http://terminology.kemkes.go.id | 4 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 3 |
|  | 3 |
| **Total** | **378** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
