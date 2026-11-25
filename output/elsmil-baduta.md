# Output Form: ELSMIL Baduta

Sumber: `mapping/phdt-data-dictionary-elsmil-baduta.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-elsmil-baduta.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 31 |
| Code (`jumlah code` = 1) | 84 |
| Code unik (code + CodeSystem) | 70 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 29 |
| Variabel BQ (unik) | 0 |
| Variabel raw (variabel dictionary; belum ada file mentah) | 38 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–7 | Patient | – | – | _Nama_ → `Patient.name.text` (2, tanpa BQ)<br>_NIK_ → `Patient.identifier.use` (3, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (4, tanpa BQ)<br>_Usia Ibu_ → `Patient.birthDate` (5, tanpa BQ)<br>_No Handphone/Whatsapp_ → `Patient.telecom` (6, tanpa BQ)<br>_Alamat_ → `Patient.address.use` (7, tanpa BQ)<br>_Nama_ → `Patient.name.text` (84, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (85, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (86, tanpa BQ)<br>_Usia_ → `Patient.birthDate` (88, tanpa BQ)<br>_Nama_ → `Patient.name.text` (183, tanpa BQ)<br>_Tanggal Lahir Baduta_ → `Patient.birthDate` (184, tanpa BQ)<br>_Usia_ → `Patient.gender` (185, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (186, tanpa BQ) |
| 2 | 8–18 | Observation | 103975-9 | Previous delivery date | _Tanggal Lahir anak sebelumnya_ → `Observation.valueDateTime` (11, tanpa BQ) |
| 3 | 19–29 | Observation | 243816001 | Contraception status | _Penggunaan Kontrasepsi saat ini_ → `Observation.valueBoolean` (22, tanpa BQ) |
| 4 | 30–48 | Observation | 8659-5 | Birth control method - Reported | _Apabila Ya, jenis alat/obat/cara KB (kontrasepsi) yang digunakan saat ini antara lain_ → `Observation.valueCodeableConcept.coding` (33, tanpa BQ) |
| 5 | 49–69 | Observation | 63719-9 | What was the primary source of drinking water at your home [Next-of-kin] | _Akses air minum yang layak?_ → `Observation.valueCodeableConcept.coding` (52, tanpa BQ) |
| 6 | 70–83 | Observation | SP000093 | Tempat BAB Layak | _Buang Air Besar di tempat yang layak?_ → `Observation.valueCodeableConcept.coding` (73, tanpa BQ) |
| 7 | 89–100 | Observation | 365475008 | Place in family order | _Urutan anak ke-_ → `Observation.valueInteger` (92, tanpa BQ) |
| 8 | 101–114 | Observation | 76516-4 | Gestational age—​at birth | _Umur kehamilan saat lahir_ → `Observation.valueQuantity.value` (104, tanpa BQ) |
| 9 | 115–128 | Observation | 89269-5 | Body height Measured --at birth | _Panjang badan saat lahir_ → `Observation.valueQuantity.value` (118, tanpa BQ) |
| 10 | 129–142 | Observation | 8339-4 | Birth weight Measured | _Berat badan saat lahir_ → `Observation.valueQuantity.value` (132, tanpa BQ) |
| 11 | 143–154 | Observation | SP000024 | Monitoring ASI Eksklusif Bulan 0 | _Pemerian ASI eksklusif_ → `Observation.valueCodeableConcept.coding` (146, tanpa BQ) |
| 12 | 155–171 | Immunization | – | – | _Apakah bayi sudah mendapatkan imunisasi Hepatitis B (HB0)_ → `Immunization.status` (155, tanpa BQ) |
| 13 | 172–182 | Observation | 16090371000119103 | Exposure to second hand tobacco smoke | _Terpapar asap rokok_ → `Observation.valueBoolean` (175, tanpa BQ) |
| 14 | 188–199 | Observation | 365475008 | Place in family order | _Urutan anak ke-_ → `Observation.valueInteger` (191, tanpa BQ) |
| 15 | 200–213 | Observation | 8306-3 | Body height --lying | _Panjang badan baduta_ → `Observation.valueQuantity.value` (203, tanpa BQ)<br>_Tanggal pengukuran_ → `Observation.effectiveDateTime` (210, tanpa BQ) |
| 16 | 214–227 | Observation | 8339-4 | Birth weight Measured | _Berat badan baduta_ → `Observation.valueQuantity.value` (217, tanpa BQ) |
| 17 | 228–238 | Observation | SP000152 | Baduta hanya diberikan ASI saja kecuali vitamin dan oralit | _Pertanyaan untuk baduta di bawah usia 6 bulan: "Apakah Baduta hanya diberikan ASI saja kecuali vitamin dan oralit?"_ → `Observation.valueBoolean` (231, tanpa BQ) |
| 18 | 239–250 | Observation | SP000153 | Baduta>= 6 bulan diberikan ASI | _Pertanyaan untuk baduta>= 6 bulan "Apakah baduta masih diberikan ASI"_ → `Observation.valueBoolean` (242, tanpa BQ) |
| 19 | 251–261 | Observation | – | – | _Pertanyaan untuk baduta > 6 bulan_ → `Observation.valueBoolean` (254, tanpa BQ) |
| 20 | 271–282 | Observation | IM-Baduta | Imunisasi Program Rutin Baduta | _Apakah baduta sudah mendapatkan imunisasi rutin?_ → `Observation.valueCodeableConcept.coding` (274, tanpa BQ) |
| 21 | 283–293 | Observation | SP000154 | Pengisian Kartu Kembang Anak (KKA) | _Pengisian Kartu Kembang Anak (KKA)_ → `Observation.valueBoolean` (286, tanpa BQ) |
| 22 | 294–305 | Observation | 1148955005 | Normal childhood development | _Jika ya_ → `Observation.valueBoolean` (297, tanpa BQ) |
| 23 | 306–316 | Observation | 16090371000119103 | Exposure to second hand tobacco smoke | _Terpapar asap rokok_ → `Observation.valueBoolean` (309, tanpa BQ) |
| 24 | 317–327 | Observation | SP000228 | Kehadiran pada Posyandu/BKB bulan ini | _Kehadiran pada Posyandu/BKB bulan ini_ → `Observation.valueBoolean` (320, tanpa BQ) |
| 25 | 328–338 | Observation | 385827001 | Health promotion education | _Memberikan penyuluhan/KIE_ → `Observation.valueBoolean` (331, tanpa BQ) |
| 26 | 339–350 | Observation | 171035004 | Health education given | _Jika Ya_ → `Observation.valueCodeableConcept.coding` (342, tanpa BQ) |
| 27 | 351–363 | Observation | 306206005 | Referral to service | _Memfasilitasi pelayanan rujukan_ → `Observation.valueCodeableConcept.coding` (354, tanpa BQ) |
| 28 | 364–377 | Observation | 405076007 | Social support status | _Memfasilitasi bantuan sosial_ → `Observation.valueCodeableConcept.coding` (367, tanpa BQ) |
| 29 | 378–392 | Observation | SP000145 | Bantuan sosial yang sedang dalam proses | _Sedang proses_ → `Observation.valueCodeableConcept.coding` (381, tanpa BQ) |
| 30 | 393–407 | Observation | SP000146 | Bantuan sosial yang sudah didapatkan | _Sudah mendapatkan bantuan sosial_ → `Observation.valueCodeableConcept.coding` (396, tanpa BQ) |
| 31 | 408–418 | Observation | SP000219 | Catatan TPK | _Catatan TPK_ → `Observation.valueString` (410, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 29 |
| Patient | 1 |
| Immunization | 1 |
| **Total** | **31** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 10 | Observation | `Observation.code.coding` | 103975-9 | Previous delivery date | http://loinc.org |
| 2 | 21 | Observation | `Observation.code.coding` | 243816001 | Contraception status | http://loinc.org |
| 3 | 32 | Observation | `Observation.code.coding` | 8659-5 | Birth control method - Reported | http://loinc.org |
| 4 | 33 | Observation | `Observation.valueCodeableConcept.coding` | 77543007 | Ligation of fallopian tube | http://snomed.info/sct |
| 5 | 34 | Observation | `Observation.valueCodeableConcept.coding` | 22523008 | Vasectomy | http://snomed.info/sct |
| 6 | 35 | Observation | `Observation.valueCodeableConcept.coding` | LA6527-1 | Intrauterine device | http://loinc.org |
| 7 | 36 | Observation | `Observation.valueCodeableConcept.coding` | SP000097 | Implan | http://terminology.kemkes.go.id/sp |
| 8 | 37 | Observation | `Observation.valueCodeableConcept.coding` | LA6525-5 | Injectable/implantable hormone | http://loinc.org |
| 9 | 38 | Observation | `Observation.valueCodeableConcept.coding` | LA6524-8 | Oral contraceptive pill | http://loinc.org |
| 10 | 39 | Observation | `Observation.valueCodeableConcept.coding` | LA6523-0 | Condom | http://loinc.org |
| 11 | 40 | Observation | `Observation.valueCodeableConcept.coding` | 237122005 | Lactational amenorrhea | http://snomed.info/sct |
| 12 | 41 | Observation | `Observation.valueCodeableConcept.coding` | 718701005 | Natural family planning method | http://snomed.info/sct |
| 13 | 51 | Observation | `Observation.code.coding` | 63719-9 | What was the primary source of drinking water at your home [Next-of-kin] | http://loinc.org |
| 14 | 52 | Observation | `Observation.valueCodeableConcept.coding` | LA14183-0 | Bottled water | http://loinc.org |
| 15 | 53 | Observation | `Observation.valueCodeableConcept.coding` | LA14182-2 | Community supply | http://loinc.org |
| 16 | 54 | Observation | `Observation.valueCodeableConcept.coding` | SP000066 | Sumur bor/pompa | http://terminology.kemkes.go.id/sp |
| 17 | 55 | Observation | `Observation.valueCodeableConcept.coding` | SP000067 | Sumur terlindungi | http://terminology.kemkes.go.id/sp |
| 18 | 56 | Observation | `Observation.valueCodeableConcept.coding` | SP000068 | Sumur tak terlindungi | http://terminology.kemkes.go.id/sp |
| 19 | 57 | Observation | `Observation.valueCodeableConcept.coding` | SP000069 | Mata air terlindungi | http://terminology.kemkes.go.id/sp |
| 20 | 58 | Observation | `Observation.valueCodeableConcept.coding` | SP000070 | Mata air tak terlindungi | http://terminology.kemkes.go.id/sp |
| 21 | 59 | Observation | `Observation.valueCodeableConcept.coding` | 421665008 | River water | http://snomed.info/sct |
| 22 | 60 | Observation | `Observation.valueCodeableConcept.coding` | 420492000 | Lake water | http://snomed.info/sct |
| 23 | 61 | Observation | `Observation.valueCodeableConcept.coding` | 421176006 | Pond water | http://snomed.info/sct |
| 24 | 62 | Observation | `Observation.valueCodeableConcept.coding` | SP000071 | Air hujan | http://terminology.kemkes.go.id/sp |
| 25 | 72 | Observation | `Observation.code.coding` | SP000093 | Tempat BAB Layak | http://terminology.kemkes.go.id/sp |
| 26 | 73 | Observation | `Observation.valueCodeableConcept.coding` | SP000094 | Jamban milik sendiri dengan leher angsa dan tangki septik/IPAL | http://terminology.kemkes.go.id/sp |
| 27 | 74 | Observation | `Observation.valueCodeableConcept.coding` | SP000095 | Jamban pada MCK komunal dengan leher angsa dan tangki septik/IPAL | http://terminology.kemkes.go.id/sp |
| 28 | 75 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 29 | 76 | Observation | `Observation.valueCodeableConcept.coding` | SP000096 | Tidak ada tempat BAB layak | http://terminology.kemkes.go.id/sp |
| 30 | 91 | Observation | `Observation.code.coding` | 365475008 | Place in family order | http://snomed.info/sct |
| 31 | 93 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 32 | 103 | Observation | `Observation.code.coding` | 76516-4 | Gestational age—​at birth | http://loinc.org |
| 33 | 113 | Observation | `Observation.interpretation.coding` | SP000224 | Cukup atau Lebih Bulan: Umur kehamilan saat lahir >= 37 minggu | http://terminology.kemkes.go.id/sp |
| 34 | 114 | Observation | `Observation.interpretation.coding` | 10761241000119104 | Preterm labor with preterm delivery (finding) |  |
| 35 | 117 | Observation | `Observation.code.coding` | 89269-5 | Body height Measured --at birth | https://loinc.org |
| 36 | 121 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 37 | 131 | Observation | `Observation.code.coding` | 8339-4 | Birth weight Measured | https://loinc.org |
| 38 | 135 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 39 | 145 | Observation | `Observation.code.coding` | SP000024 | Monitoring ASI Eksklusif Bulan 0 | http://terminology.kemkes.go.id/sp |
| 40 | 146 | Observation | `Observation.valueCodeableConcept.coding` | 1145307003 | Exclusively breastfed | http://snomed.info/sct |
| 41 | 147 | Observation | `Observation.valueCodeableConcept.coding` | SP000029 | Tidak ASI Eksklusif | http://terminology.kemkes.go.id/sp |
| 42 | 158 | Immunization | `Immunization.vaccineCode` | VG45 | HepB | http://sys-ids.kemkes.go.id/kfa |
| 43 | 174 | Observation | `Observation.code.coding` | 16090371000119103 | Exposure to second hand tobacco smoke | http://loinc.org |
| 44 | 190 | Observation | `Observation.code.coding` | 365475008 | Place in family order | http://snomed.info/sct |
| 45 | 192 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 46 | 202 | Observation | `Observation.code.coding` | 8306-3 | Body height --lying | https://loinc.org |
| 47 | 206 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 48 | 216 | Observation | `Observation.code.coding` | 8339-4 | Birth weight Measured | https://loinc.org |
| 49 | 220 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 50 | 230 | Observation | `Observation.code.coding` | SP000152 | Baduta hanya diberikan ASI saja kecuali vitamin dan oralit | http://terminology.kemkes.go.id/sp |
| 51 | 241 | Observation | `Observation.code.coding` | SP000153 | Baduta>= 6 bulan diberikan ASI | http://terminology.kemkes.go.id/sp |
| 52 | 273 | Observation | `Observation.code.coding` | IM-Baduta | Imunisasi Program Rutin Baduta | http://terminology.kemkes.go.id/CodeSystem/immunization-reason |
| 53 | 274 | Observation | `Observation.valueCodeableConcept.coding` | 255599008 | Incomplete | http://snomed.info/sct |
| 54 | 275 | Observation | `Observation.valueCodeableConcept.coding` | 255594003 | Complete | http://snomed.info/sct |
| 55 | 285 | Observation | `Observation.code.coding` | SP000154 | Pengisian Kartu Kembang Anak (KKA) | http://terminology.kemkes.go.id/sp |
| 56 | 296 | Observation | `Observation.code.coding` | 1148955005 | Normal childhood development | http://snomed.info/sct |
| 57 | 308 | Observation | `Observation.code.coding` | 16090371000119103 | Exposure to second hand tobacco smoke | http://loinc.org |
| 58 | 319 | Observation | `Observation.code.coding` | SP000228 | Kehadiran pada Posyandu/BKB bulan ini | http://terminology.kemkes.go.id/sp |
| 59 | 330 | Observation | `Observation.code.coding` | 385827001 | Health promotion education | http://loinc.org |
| 60 | 341 | Observation | `Observation.code.coding` | 171035004 | Health education given | http://snomed.info/sct |
| 61 | 342 | Observation | `Observation.valueCodeableConcept.coding` | 125676002 | Person | http://snomed.info/sct |
| 62 | 343 | Observation | `Observation.valueCodeableConcept.coding` | 389109008 | Group | http://snomed.info/sct |
| 63 | 353 | Observation | `Observation.code.coding` | 306206005 | Referral to service | http://snomed.info/sct |
| 64 | 354 | Observation | `Observation.valueCodeableConcept.coding` | 385651009 | In progress | http://snomed.info/sct |
| 65 | 355 | Observation | `Observation.valueCodeableConcept.coding` | 385658003 | Done | http://snomed.info/sct |
| 66 | 356 | Observation | `Observation.valueCodeableConcept.coding` | 385660001 | Not done | http://snomed.info/sct |
| 67 | 366 | Observation | `Observation.code.coding` | 405076007 | Social support status | http://snomed.info/sct |
| 68 | 367 | Observation | `Observation.valueCodeableConcept.coding` | LA32661-3 | Applied and waiting to receive | http://loinc.org |
| 69 | 368 | Observation | `Observation.valueCodeableConcept.coding` | LA32660-5 | Received | http://loinc.org |
| 70 | 369 | Observation | `Observation.valueCodeableConcept.coding` | LA32662-1 | Tried but was not able to apply for, or was not eligible | http://loinc.org |
| 71 | 370 | Observation | `Observation.valueCodeableConcept.coding` | LA32663-9 | Did not apply for | http://loinc.org |
| 72 | 380 | Observation | `Observation.code.coding` | SP000145 | Bantuan sosial yang sedang dalam proses | http://terminology.kemkes.go.id/sp |
| 73 | 381 | Observation | `Observation.valueCodeableConcept.coding` | SP000140 | Program Keluarga Harapan | http://terminology.kemkes.go.id/sp |
| 74 | 382 | Observation | `Observation.valueCodeableConcept.coding` | SP000141 | Bantu Non Tunai | http://terminology.kemkes.go.id/sp |
| 75 | 383 | Observation | `Observation.valueCodeableConcept.coding` | SP000142 | Program Indonesia Pintar | http://terminology.kemkes.go.id/sp |
| 76 | 384 | Observation | `Observation.valueCodeableConcept.coding` | SP000143 | Kartu Indonesia Sehat | http://terminology.kemkes.go.id/sp |
| 77 | 385 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 78 | 395 | Observation | `Observation.code.coding` | SP000146 | Bantuan sosial yang sudah didapatkan | http://terminology.kemkes.go.id/sp |
| 79 | 396 | Observation | `Observation.valueCodeableConcept.coding` | SP000140 | Program Keluarga Harapan | http://terminology.kemkes.go.id/sp |
| 80 | 397 | Observation | `Observation.valueCodeableConcept.coding` | SP000141 | Bantu Non Tunai | http://terminology.kemkes.go.id/sp |
| 81 | 398 | Observation | `Observation.valueCodeableConcept.coding` | SP000142 | Program Indonesia Pintar | http://terminology.kemkes.go.id/sp |
| 82 | 399 | Observation | `Observation.valueCodeableConcept.coding` | SP000143 | Kartu Indonesia Sehat | http://terminology.kemkes.go.id/sp |
| 83 | 400 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 84 | 409 | Observation | `Observation.code.coding` | SP000219 | Catatan TPK | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://terminology.kemkes.go.id/sp | 29 |
| http://snomed.info/sct | 24 |
| http://loinc.org | 18 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 6 |
| https://loinc.org | 4 |
|  | 1 |
| http://sys-ids.kemkes.go.id/kfa | 1 |
| http://terminology.kemkes.go.id/CodeSystem/immunization-reason | 1 |
| **Total** | **84** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
