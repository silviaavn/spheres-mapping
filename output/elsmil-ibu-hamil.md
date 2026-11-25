# Output Form: ELSMIL Ibu Hamil

Sumber: `mapping/phdt-data-dictionary-elsmil-ibu-hamil.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-elsmil-ibu-hamil.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 36 |
| Code (`jumlah code` = 1) | 105 |
| Code unik (code + CodeSystem) | 96 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 33 |
| Variabel BQ (unik) | 0 |
| Variabel raw (variabel dictionary; belum ada file mentah) | 36 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–12 | Patient | – | – | _Nama_ → `Patient.name.text` (2, tanpa BQ)<br>_NIK_ → `Patient.identifier.value` (5, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (8, tanpa BQ)<br>_Usia_ → `Patient.birthDate` (9, tanpa BQ)<br>_No HP_ → `Patient.telecom` (10, tanpa BQ)<br>_Alamat_ → `Patient.address.use` (11, tanpa BQ) |
| 2 | 13–26 | Encounter | – | – | _Tanggal Kunjungan_ → `Encounter.identifier` (13, tanpa BQ) |
| 3 | 27–33 | Condition | 134435003 | Routine antenatal care | – |
| 4 | 48–58 | Observation | 1362035007 | Number of biological children | _Jumlah Anak_ → `Observation.valueInteger` (51, tanpa BQ) |
| 5 | 59–69 | Observation | SP000065 | Tanggal Lahir Anak Terakhir | _Tanggal Lahir Anak Terakhir_ → `Observation.valueDateTime` (62, tanpa BQ) |
| 6 | 70–82 | Observation | 18185-9 | Gestational age | _Usia kehamilan saat ini_ → `Observation.valueQuantity.value` (74, tanpa BQ) |
| 7 | 83–95 | Observation | 11881-0 | Uterus Fundal height Tape measure | _TFU (cm)_ → `Observation.valueQuantity.value` (87, tanpa BQ) |
| 8 | 96–108 | Observation | 8302-2 | Body height | _Tinggi Badan (cm)_ → `Observation.valueQuantity.value` (100, tanpa BQ) |
| 9 | 109–121 | Observation | 56077-1 | Body weight --pre current pregnancy | _Berat Badan (kg) Sebelum hamil/ BB Pada Trimester 1_ → `Observation.valueQuantity.value` (113, tanpa BQ) |
| 10 | 122–134 | Observation | OC000010 | Indeks Massa Tubuh Sebelum Hamil | _Indeks Masa Tubuh (IMT}_ → `Observation.valueQuantity.value` (126, tanpa BQ) |
| 11 | 135–147 | Observation | 29463-7 | Body weight | _Berat Badan Saat Ini_ → `Observation.valueQuantity.value` (139, tanpa BQ) |
| 12 | 148–159 | Condition | 161501007 | H/O: hypertension | _Riwayat Penyakit_ → `Condition.clinicalStatus.coding` (148, tanpa BQ) |
| 13 | 160–169 | ServiceRequest | – | – | _Apakah Ibu hamil melakukan pemeriksaan HB_ → `ServiceRequest.category` (160, tanpa BQ) |
| 14 | 173–180 | Specimen | – | – | – |
| 15 | 181–195 | Observation | 718-7 | Hemoglobin [Mass/volume] in Blood | – |
| 16 | 196–207 | DiagnosticReport | 718-7 | Hemoglobin [Mass/volume] in Blood | – |
| 17 | 208–222 | Observation | SP000223 | Alasan tidak diperiksa HB | _Alasan tidak diperiksa HB_ → `Observation.valueString` (210, tanpa BQ) |
| 18 | 223–235 | Observation | 284473002 | Mid upper arm circumference | _Lingkar Lengan Atas (cm)_ → `Observation.valueQuantity.value` (227, tanpa BQ) |
| 19 | 236–248 | Observation | 89087-1 | Fetal Body weight Estimated | _Taksiran Berat Janin (gr)_ → `Observation.valueQuantity.value` (240, tanpa BQ) |
| 20 | 249–259 | Observation | 72166-2 | Tobacco smoking status | _Apakah merokok/terpapar rokok_ → `Observation.valueBoolean` (252, tanpa BQ) |
| 21 | 260–280 | Observation | 63719-9 | What was the primary source of drinking water at your home [Next-of-kin] | _Akses air minum yang layak?_ → `Observation.valueCodeableConcept.coding` (263, tanpa BQ) |
| 22 | 281–294 | Observation | SP000093 | Tempat BAB Layak | _Buang Air Besar di tempat yang layak?_ → `Observation.valueCodeableConcept.coding` (284, tanpa BQ) |
| 23 | 295–305 | Observation | 398780007 | Contraception education | _Apakah ibu sudah mendapatkan informasi terkait metode kontrasepsi?_ → `Observation.valueBoolean` (298, tanpa BQ) |
| 24 | 306–316 | Observation | 423925001 | Family planning observable | _Apakah sudah memutuskan untuk menggunakan alat kontrasepsi pasca persalinan?_ → `Observation.valueBoolean` (309, tanpa BQ) |
| 25 | 317–332 | Observation | 8659-5 | Birth control method - Reported | _Jika Ya_ → `Observation.valueCodeableConcept.coding` (320, tanpa BQ) |
| 26 | 333–354 | Observation | 736796006 | Reason for no contraception (observable entity) | _Jika Tidak_ → `Observation.valueCodeableConcept.coding` (336, tanpa BQ) |
| 27 | 355–365 | Observation | 385827001 | Health promotion education | _Memberikan penyuluhan/KIE_ → `Observation.valueBoolean` (358, tanpa BQ) |
| 28 | 366–377 | Observation | 171035004 | Health education given | _Jika Ya_ → `Observation.valueCodeableConcept.coding` (369, tanpa BQ) |
| 29 | 378–388 | Observation | 182947002 | Administration of prophylactic iron during pregnancy (procedure) | _Apakah Ibu Hamil sudah mendapatkan tablet tambah darah_ → `Observation.valueBoolean` (381, tanpa BQ) |
| 30 | 389–399 | Observation | SP000144 | Sudah mengonsumsi tablet tambah darah | _Apakah Ibu Hamil sudah meminum tablet tambah darah_ → `Observation.valueBoolean` (392, tanpa BQ) |
| 31 | 400–412 | Observation | 306206005 | Referral to service | _Memfasilitasi pelayanan rujukan_ → `Observation.valueCodeableConcept.coding` (403, tanpa BQ) |
| 32 | 413–426 | Observation | 405076007 | Social support status | _Memfasilitasi bantuan sosial_ → `Observation.valueCodeableConcept.coding` (416, tanpa BQ) |
| 33 | 427–441 | Observation | SP000145 | Bantuan sosial yang sedang dalam proses | _Sedang proses_ → `Observation.valueCodeableConcept.coding` (430, tanpa BQ) |
| 34 | 442–456 | Observation | SP000146 | Bantuan sosial yang sudah didapatkan | _Sudah mendapatkan bantuan sosial_ → `Observation.valueCodeableConcept.coding` (445, tanpa BQ) |
| 35 | 457–466 | ServiceRequest | – | – | _Tanggal Kunjungan Berikutnya_ → `ServiceRequest.category` (457, tanpa BQ) |
| 36 | 467–477 | Observation | SP000219 | Catatan TPK | _Catatan TPK_ → `Observation.valueString` (469, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 28 |
| Condition | 2 |
| ServiceRequest | 2 |
| Patient | 1 |
| Encounter | 1 |
| Specimen | 1 |
| DiagnosticReport | 1 |
| **Total** | **36** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 29 | Condition | `Condition.code.coding` | 134435003 | Routine antenatal care | http://snomed.info/sct |
| 2 | 50 | Observation | `Observation.code.coding` | 1362035007 | Number of biological children | http://snomed.info/sct |
| 3 | 61 | Observation | `Observation.code.coding` | SP000065 | Tanggal Lahir Anak Terakhir | http://terminology.kemkes.go.id/sp |
| 4 | 72 | Observation | `Observation.code.coding` | 18185-9 | Gestational age | http://loinc.org |
| 5 | 73 | Observation | `Observation.code.coding` | ANC.B6.DE17 | Gestational age | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 6 | 85 | Observation | `Observation.code.coding` | 11881-0 | Uterus Fundal height Tape measure | http://loinc.org |
| 7 | 86 | Observation | `Observation.code.coding` | ANC.B8.DE105 | Symphysis-fundal height | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 8 | 98 | Observation | `Observation.code.coding` | 8302-2 | Body height | http://loinc.org |
| 9 | 99 | Observation | `Observation.code.coding` | ANC.B8.DE1 | Height | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 10 | 111 | Observation | `Observation.code.coding` | 56077-1 | Body weight --pre current pregnancy | http://loinc.org |
| 11 | 112 | Observation | `Observation.code.coding` | ANC.B8.DE2 | Pre-gestational weight | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 12 | 124 | Observation | `Observation.code.coding` | OC000010 | Indeks Massa Tubuh Sebelum Hamil | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 13 | 125 | Observation | `Observation.code.coding` | ANC.SS.DE58 | IMT Sebelum Hamil | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 14 | 137 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 15 | 138 | Observation | `Observation.code.coding` | ANC.B8.DE3 | Current weight | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 16 | 150 | Condition | `Condition.code.coding` | 161501007 | H/O: hypertension | http://snomed.info/sct |
| 17 | 151 | Condition | `Condition.code.coding` | 161445009 | H/O: diabetes mellitus | http://snomed.info/sct |
| 18 | 152 | Condition | `Condition.code.coding` | 275536003 | H/O: thyroid disorder | http://snomed.info/sct |
| 19 | 153 | Condition | `Condition.code.coding` | 266995000 | H/O: cardiovascular disease | http://snomed.info/sct |
| 20 | 154 | Condition | `Condition.code.coding` | 161414005 | H/O: tuberculosis | http://snomed.info/sct |
| 21 | 155 | Condition | `Condition.code.coding` | 161527007 | H/O: asthma | http://snomed.info/sct |
| 22 | 164 | ServiceRequest | `ServiceRequest.code` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 23 | 174 | Specimen | `Specimen.type` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 24 | 183 | Observation | `Observation.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 25 | 184 | Observation | `Observation.code.coding` | ANC.B9.DE175 | Blood hemoglobin test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 26 | 195 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 27 | 198 | DiagnosticReport | `DiagnosticReport.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 28 | 209 | Observation | `Observation.code.coding` | SP000223 | Alasan tidak diperiksa HB | http://terminology.kemkes.go.id/sp |
| 29 | 211 | Observation | `Observation.valueCodeableConcept.coding` | SP000220 | Tidak terdapat sarana pemeriksaan HB | http://terminology.kemkes.go.id/sp |
| 30 | 212 | Observation | `Observation.valueCodeableConcept.coding` | SP000221 | Kesulitan akses menuju Fasilitas Kesehatan | http://terminology.kemkes.go.id/sp |
| 31 | 213 | Observation | `Observation.valueCodeableConcept.coding` | SP000222 | Ibu Hamil tidak mampu melakukan pemeriksaan | http://terminology.kemkes.go.id/sp |
| 32 | 214 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 33 | 225 | Observation | `Observation.code.coding` | 284473002 | Mid upper arm circumference | http://snomed.info/sct |
| 34 | 226 | Observation | `Observation.code.coding` | ANC.SS.DE3 | Lingkar Lengan Atas (LILA) | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 35 | 238 | Observation | `Observation.code.coding` | 89087-1 | Fetal Body weight Estimated | http://loinc.org |
| 36 | 239 | Observation | `Observation.code.coding` | ANC.SS.DE1 | Taksiran Berat Janin (TBJ) | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 37 | 251 | Observation | `Observation.code.coding` | 72166-2 | Tobacco smoking status | http://loinc.org |
| 38 | 262 | Observation | `Observation.code.coding` | 63719-9 | What was the primary source of drinking water at your home [Next-of-kin] | http://loinc.org |
| 39 | 263 | Observation | `Observation.valueCodeableConcept.coding` | LA14183-0 | Bottled water | http://loinc.org |
| 40 | 264 | Observation | `Observation.valueCodeableConcept.coding` | LA14182-2 | Community supply | http://loinc.org |
| 41 | 265 | Observation | `Observation.valueCodeableConcept.coding` | SP000066 | Sumur bor/pompa | http://terminology.kemkes.go.id/sp |
| 42 | 266 | Observation | `Observation.valueCodeableConcept.coding` | SP000067 | Sumur terlindungi | http://terminology.kemkes.go.id/sp |
| 43 | 267 | Observation | `Observation.valueCodeableConcept.coding` | SP000068 | Sumur tak terlindungi | http://terminology.kemkes.go.id/sp |
| 44 | 268 | Observation | `Observation.valueCodeableConcept.coding` | SP000069 | Mata air terlindungi | http://terminology.kemkes.go.id/sp |
| 45 | 269 | Observation | `Observation.valueCodeableConcept.coding` | SP000070 | Mata air tak terlindungi | http://terminology.kemkes.go.id/sp |
| 46 | 270 | Observation | `Observation.valueCodeableConcept.coding` | 421665008 | River water | http://snomed.info/sct |
| 47 | 271 | Observation | `Observation.valueCodeableConcept.coding` | 420492000 | Lake water | http://snomed.info/sct |
| 48 | 272 | Observation | `Observation.valueCodeableConcept.coding` | 421176006 | Pond water | http://snomed.info/sct |
| 49 | 273 | Observation | `Observation.valueCodeableConcept.coding` | SP000071 | Air hujan | http://terminology.kemkes.go.id/sp |
| 50 | 283 | Observation | `Observation.code.coding` | SP000093 | Tempat BAB Layak | http://terminology.kemkes.go.id/sp |
| 51 | 284 | Observation | `Observation.valueCodeableConcept.coding` | SP000094 | Jamban milik sendiri dengan leher angsa dan tangki septik/IPAL | http://terminology.kemkes.go.id/sp |
| 52 | 285 | Observation | `Observation.valueCodeableConcept.coding` | SP000095 | Jamban pada MCK komunal dengan leher angsa dan tangki septik/IPAL | http://terminology.kemkes.go.id/sp |
| 53 | 286 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 54 | 287 | Observation | `Observation.valueCodeableConcept.coding` | SP000096 | Tidak ada tempat BAB layak | http://terminology.kemkes.go.id/sp |
| 55 | 297 | Observation | `Observation.code.coding` | 398780007 | Contraception education | http://snomed.info/sct |
| 56 | 308 | Observation | `Observation.code.coding` | 423925001 | Family planning observable | http://snomed.info/sct |
| 57 | 319 | Observation | `Observation.code.coding` | 8659-5 | Birth control method - Reported | http://loinc.org |
| 58 | 320 | Observation | `Observation.valueCodeableConcept.coding` | LA6524-8 | Oral contraceptive pill | http://loinc.org |
| 59 | 321 | Observation | `Observation.valueCodeableConcept.coding` | 237122005 | Lactational amenorrhea | http://snomed.info/sct |
| 60 | 322 | Observation | `Observation.valueCodeableConcept.coding` | LA6525-5 | Injectable/implantable hormone | http://loinc.org |
| 61 | 323 | Observation | `Observation.valueCodeableConcept.coding` | LA6527-1 | Intrauterine device | http://loinc.org |
| 62 | 324 | Observation | `Observation.valueCodeableConcept.coding` | SP000097 | Implan | http://terminology.kemkes.go.id/sp |
| 63 | 325 | Observation | `Observation.valueCodeableConcept.coding` | LA6528-9 | Vasectomy/tubal ligation/hysterectomy | http://loinc.org |
| 64 | 335 | Observation | `Observation.code.coding` | 736796006 | Reason for no contraception (observable entity) | http://snomed.info/sct |
| 65 | 336 | Observation | `Observation.valueCodeableConcept.coding` | 276367008 | Wanted pregnancy (finding) | http://snomed.info/sct |
| 66 | 337 | Observation | `Observation.valueCodeableConcept.coding` | 440552008 | Contraception need complicated by medical condition | http://snomed.info/sct |
| 67 | 338 | Observation | `Observation.valueCodeableConcept.coding` | SP000072 | Efek samping kontrasepsi | http://terminology.kemkes.go.id/sp |
| 68 | 339 | Observation | `Observation.valueCodeableConcept.coding` | 724073007 | Declined by caregiver of subject (qualifier value) | http://snomed.info/sct |
| 69 | 340 | Observation | `Observation.valueCodeableConcept.coding` | SP000074 | Suami jauh | http://terminology.kemkes.go.id/sp |
| 70 | 341 | Observation | `Observation.valueCodeableConcept.coding` | 424670002 | Dissatisfaction with contraception method (finding) | http://snomed.info/sct |
| 71 | 342 | Observation | `Observation.valueCodeableConcept.coding` | 183945002 | Procedure declined for religious reason (situation) | http://snomed.info/sct |
| 72 | 343 | Observation | `Observation.valueCodeableConcept.coding` | 423875000 | Deficient knowledge of family planning methods | http://snomed.info/sct |
| 73 | 344 | Observation | `Observation.valueCodeableConcept.coding` | 422704000 | Difficulty obtaining contraception | http://snomed.info/sct |
| 74 | 345 | Observation | `Observation.valueCodeableConcept.coding` | SP000073 | Alat Kontrasepsi Mahal | http://terminology.kemkes.go.id/sp |
| 75 | 346 | Observation | `Observation.valueCodeableConcept.coding` | SP000091 | Alat/cara KB tidak tersedia | http://terminology.kemkes.go.id/sp |
| 76 | 347 | Observation | `Observation.valueCodeableConcept.coding` | SP000092 | Belum dapat informasi dari petugas pelayanan KB | http://terminology.kemkes.go.id/sp |
| 77 | 357 | Observation | `Observation.code.coding` | 385827001 | Health promotion education | http://loinc.org |
| 78 | 368 | Observation | `Observation.code.coding` | 171035004 | Health education given | http://snomed.info/sct |
| 79 | 369 | Observation | `Observation.valueCodeableConcept.coding` | 125676002 | Person | http://snomed.info/sct |
| 80 | 370 | Observation | `Observation.valueCodeableConcept.coding` | 389109008 | Group | http://snomed.info/sct |
| 81 | 380 | Observation | `Observation.code.coding` | 182947002 | Administration of prophylactic iron during pregnancy (procedure) | http://loinc.org |
| 82 | 391 | Observation | `Observation.code.coding` | SP000144 | Sudah mengonsumsi tablet tambah darah | http://terminology.kemkes.go.id/sp |
| 83 | 402 | Observation | `Observation.code.coding` | 306206005 | Referral to service | http://snomed.info/sct |
| 84 | 403 | Observation | `Observation.valueCodeableConcept.coding` | 385651009 | In progress | http://snomed.info/sct |
| 85 | 404 | Observation | `Observation.valueCodeableConcept.coding` | 385658003 | Done | http://snomed.info/sct |
| 86 | 405 | Observation | `Observation.valueCodeableConcept.coding` | 385660001 | Not done | http://snomed.info/sct |
| 87 | 415 | Observation | `Observation.code.coding` | 405076007 | Social support status | http://snomed.info/sct |
| 88 | 416 | Observation | `Observation.valueCodeableConcept.coding` | LA32661-3 | Applied and waiting to receive | http://loinc.org |
| 89 | 417 | Observation | `Observation.valueCodeableConcept.coding` | LA32660-5 | Received | http://loinc.org |
| 90 | 418 | Observation | `Observation.valueCodeableConcept.coding` | LA32662-1 | Tried but was not able to apply for, or was not eligible | http://loinc.org |
| 91 | 419 | Observation | `Observation.valueCodeableConcept.coding` | LA32663-9 | Did not apply for | http://loinc.org |
| 92 | 429 | Observation | `Observation.code.coding` | SP000145 | Bantuan sosial yang sedang dalam proses | http://terminology.kemkes.go.id/sp |
| 93 | 430 | Observation | `Observation.valueCodeableConcept.coding` | SP000140 | Program Keluarga Harapan | http://terminology.kemkes.go.id/sp |
| 94 | 431 | Observation | `Observation.valueCodeableConcept.coding` | SP000141 | Bantu Non Tunai | http://terminology.kemkes.go.id/sp |
| 95 | 432 | Observation | `Observation.valueCodeableConcept.coding` | SP000142 | Program Indonesia Pintar | http://terminology.kemkes.go.id/sp |
| 96 | 433 | Observation | `Observation.valueCodeableConcept.coding` | SP000143 | Kartu Indonesia Sehat | http://terminology.kemkes.go.id/sp |
| 97 | 434 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 98 | 444 | Observation | `Observation.code.coding` | SP000146 | Bantuan sosial yang sudah didapatkan | http://terminology.kemkes.go.id/sp |
| 99 | 445 | Observation | `Observation.valueCodeableConcept.coding` | SP000140 | Program Keluarga Harapan | http://terminology.kemkes.go.id/sp |
| 100 | 446 | Observation | `Observation.valueCodeableConcept.coding` | SP000141 | Bantu Non Tunai | http://terminology.kemkes.go.id/sp |
| 101 | 447 | Observation | `Observation.valueCodeableConcept.coding` | SP000142 | Program Indonesia Pintar | http://terminology.kemkes.go.id/sp |
| 102 | 448 | Observation | `Observation.valueCodeableConcept.coding` | SP000143 | Kartu Indonesia Sehat | http://terminology.kemkes.go.id/sp |
| 103 | 449 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 104 | 461 | ServiceRequest | `ServiceRequest.code` | 185389009 | Follow-up visit | http://snomed.info/sct |
| 105 | 468 | Observation | `Observation.code.coding` | SP000219 | Catatan TPK | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 37 |
| http://terminology.kemkes.go.id/sp | 33 |
| http://loinc.org | 24 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 6 |
| http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes | 3 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 1 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 1 |
| **Total** | **105** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
