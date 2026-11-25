# Output Form: Kobo Modul ANC

Sumber: `mapping/phdt-data-dictionary-kobo-modul-anc.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-kobo-modul-anc.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 86 |
| Code (`jumlah code` = 1) | 189 |
| Code unik (code + CodeSystem) | 136 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 16 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–27 | Patient | – | – | _Nama Ibu_ → `Patient.name.text` (2, tanpa BQ)<br>_NIK_ → `Patient.identifier.value` (5, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (7, tanpa BQ)<br>_No HP_ → `Patient.telecom` (8, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (11, tanpa BQ)<br>_Alamat Domisili_ → `Patient.address.use` (12, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (18, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (21, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.extension.valueCode` (24, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.extension.valueCode` (27, tanpa BQ) |
| 2 | 74–80 | PractitionerRole | – | – | _Tenaga Pemeriksa_ → `PractitionerRole.active` (74, tanpa BQ) |
| 3 | 81–101 | Practitioner | – | – | _Nama Tenaga Kesehatan_ → `Practitioner.name.text` (83, tanpa BQ)<br>_Jenis Kelamin Tenaga Kesehatan_ → `Practitioner.gender` (84, tanpa BQ)<br>_Nama Provinsi_ → `Practitioner.address.extension.extension.valueCode` (91, tanpa BQ)<br>_Nama Kabupaten_ → `Practitioner.address.extension.extension.valueCode` (94, tanpa BQ)<br>_Nama Kecamatan_ → `Practitioner.address.extension.extension.valueCode` (97, tanpa BQ)<br>_Nama Desa_ → `Practitioner.address.extension.extension.valueCode` (100, tanpa BQ) |
| 4 | 102–110 | EpisodeOfCare | ANC | Antenatal Care | – |
| 5 | 111–125 | Encounter | – | – | _Tanggal Kunjungan ANC_ → `Encounter.period.start` (120, tanpa BQ) |
| 6 | 126–132 | Condition | 134435003.0 | Routine antenatal care | – |
| 7 | 145–156 | Observation | 424144002.0 | Current chronological age | _Umur_ → `Observation.valueQuantity.value` (148, tanpa BQ) |
| 8 | 157–168 | Observation | SP000132 | Memiliki Buku KIA | _Memiliki Buku KIA_ → `Observation.valueBoolean` (160, tanpa BQ) |
| 9 | 169–180 | Observation | 8665-2 | Last menstrual period start date | _HPHT_ → `Observation.valueDateTime` (173, tanpa BQ) |
| 10 | 181–192 | Observation | 11778-8 | Delivery date Estimated | _Tanggal Perkiraan Persalinan (HPL)_ → `Observation.valueDateTime` (185, tanpa BQ) |
| 11 | 193–205 | Observation | 56077-1 | Body weight --pre current pregnancy | _Berat Badan Sebelum Hamil_ → `Observation.valueQuantity.value` (197, tanpa BQ) |
| 12 | 206–218 | Observation | 8302-2 | Body height | _Tinggi Badan_ → `Observation.valueQuantity.value` (210, tanpa BQ) |
| 13 | 219–231 | Observation | OC000010 | Indeks Massa Tubuh Sebelum Hamil | _IMT Sebelum Hamil_ → `Observation.valueQuantity.value` (223, tanpa BQ) |
| 14 | 232–250 | Immunization | – | – | _Dilakukan Imunisasi TT (Pada Kunjungan Ini)_ → `Immunization.status` (232, tanpa BQ)<br>_Riwayat Imunisasi TT_ → `Immunization.status` (249, tanpa BQ) |
| 15 | 251–267 | Immunization | – | – | – |
| 16 | 268–278 | Immunization | – | – | – |
| 17 | 279–289 | Observation | SP000001 | Skrining Imunisasi Tetanus Toksoid | – |
| 18 | 290–300 | Observation | SP000002 | Kunjungan Pertama Pemeriksaan Kehamilan | _Pemeriksaan Pertama_ → `Observation.valueBoolean` (293, tanpa BQ) |
| 19 | 301–316 | Observation | 18185-9 | Gestational age | _Usia Kehamilan_ → `Observation.valueQuantity.value` (305, tanpa BQ) |
| 20 | 317–328 | Observation | 32418-6 | Obstetric trimester Stated | _Trimester 1_ → `Observation.valueInteger` (321, tanpa BQ) |
| 21 | 333–344 | Observation | 32418-6 | Obstetric trimester Stated | _Trimester 2_ → `Observation.valueInteger` (337, tanpa BQ) |
| 22 | 351–362 | Observation | 32418-6 | Obstetric trimester Stated | _Trimester 3_ → `Observation.valueInteger` (355, tanpa BQ) |
| 23 | 371–383 | Observation | 29463-7 | Body weight | _Berat Badan_ → `Observation.valueQuantity.value` (375, tanpa BQ) |
| 24 | 384–396 | Observation | 8480-6 | Systolic blood pressure | _Tekanan Darah Sistolik_ → `Observation.valueQuantity.value` (388, tanpa BQ) |
| 25 | 397–409 | Observation | 8462-4 | Diastolic blood pressure | _Tekanan Darah Diastolik_ → `Observation.valueQuantity.value` (401, tanpa BQ) |
| 26 | 410–424 | Observation | 284473002.0 | Mid upper arm circumference | _LILA_ → `Observation.status` (410, tanpa BQ)<br>_Status Gizi KEK/Tidak KEK_ → `Observation.interpretation` (422, tanpa BQ) |
| 27 | 425–437 | Observation | 11881-0 | Uterus Fundal height Tape measure | _Tinggi Fundus_ → `Observation.valueQuantity.value` (429, tanpa BQ) |
| 28 | 438–452 | Observation | 883-9 | ABO group [Type] in Blood | _Lab : Golongan Darah_ → `Observation.valueCodeableConcept.coding` (442, tanpa BQ) |
| 29 | 453–465 | Observation | 10331-7 | Rh [Type] in Blood | _Lab : Rhesus_ → `Observation.valueCodeableConcept.coding` (457, tanpa BQ) |
| 30 | 466–478 | Observation | 55283-6 | Fetal Heart rate | _Denyut Jantung Janin_ → `Observation.valueQuantity.value` (470, tanpa BQ) |
| 31 | 479–493 | Observation | 72155-5 | Position in womb Fetus [RHEA] | _Presentasi Janin_ → `Observation.valueCodeableConcept.coding` (483, tanpa BQ) |
| 32 | 494–508 | Condition | 34842007.0 | Antepartum hemorrhage | _Komplikasi Kehamilan_ → `Condition.clinicalStatus.coding` (494, tanpa BQ) |
| 33 | 509–519 | Procedure | 88.78 | Diagnostic ultrasound of gravid uterus | _USG_ → `Procedure.category.coding` (509, tanpa BQ) |
| 34 | 520–533 | Observation | 268445003.0 | Ultrasound scan - obstetric | _Diperiksa USG_ → `Observation.valueCodeableConcept.coding` (523, tanpa BQ)<br>_Jika diperiksa, hasil tidak normal. Tidak normal karena apa?_ → `Observation.valueCodeableConcept.text` (526, tanpa BQ) |
| 35 | 534–567 | MedicationRequest | 92000653.0 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula | _Jumlah TTD Diterima_ → `MedicationRequest.contained.resourceType` (534, tanpa BQ) |
| 36 | 568–599 | MedicationDispense | 93015491.0 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | – |
| 37 | 600–609 | ServiceRequest | – | – | _Lab : HIV_ → `ServiceRequest.category` (600, tanpa BQ) |
| 38 | 610–613 | PractitionerRole | – | – | – |
| 39 | 614–621 | Specimen | – | – | – |
| 40 | 622–635 | Observation | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | – |
| 41 | 636–647 | DiagnosticReport | – | – | – |
| 42 | 648–657 | ServiceRequest | – | – | _Lab : Hepatitis_ → `ServiceRequest.category` (648, tanpa BQ) |
| 43 | 658–661 | PractitionerRole | – | – | – |
| 44 | 662–669 | Specimen | – | – | – |
| 45 | 670–683 | Observation | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | – |
| 46 | 684–695 | DiagnosticReport | – | – | – |
| 47 | 696–705 | ServiceRequest | – | – | _Lab : Siphilis_ → `ServiceRequest.category` (696, tanpa BQ) |
| 48 | 706–709 | PractitionerRole | – | – | – |
| 49 | 710–717 | Specimen | – | – | – |
| 50 | 718–731 | Observation | 22464-2 | Reagin Ab [Presence] in Specimen | – |
| 51 | 732–743 | DiagnosticReport | – | – | – |
| 52 | 744–753 | ServiceRequest | – | – | _Lab : Protein Urine_ → `ServiceRequest.category` (744, tanpa BQ) |
| 53 | 754–757 | PractitionerRole | – | – | – |
| 54 | 758–765 | Specimen | – | – | – |
| 55 | 766–779 | Observation | 2887-8 | Protein [Presence] in Urine | – |
| 56 | 780–791 | DiagnosticReport | 2887-8 | Protein [Presence] in Urine | – |
| 57 | 792–801 | ServiceRequest | – | – | _Lab : Hb_ → `ServiceRequest.category` (792, tanpa BQ) |
| 58 | 802–805 | PractitionerRole | – | – | – |
| 59 | 806–813 | Specimen | – | – | – |
| 60 | 814–831 | Observation | 718-7 | Hemoglobin [Mass/volume] in Blood | – |
| 61 | 832–843 | DiagnosticReport | 718-7 | Hemoglobin [Mass/volume] in Blood | – |
| 62 | 844–853 | ServiceRequest | – | – | _Lab : Gula Sewaktu_ → `ServiceRequest.category` (844, tanpa BQ) |
| 63 | 854–857 | PractitionerRole | – | – | – |
| 64 | 858–865 | Specimen | – | – | – |
| 65 | 866–881 | Observation | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | – |
| 66 | 882–893 | DiagnosticReport | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | – |
| 67 | 894–908 | Observation | 15220000.0 | Laboratory test | _Lab : Lainnya_ → `Observation.valueCodeableConcept.coding` (897, tanpa BQ) |
| 68 | 909–917 | Observation | SP000007 | Tatalaksana Anemia | _Tatalaksana Anemia_ → `Observation.valueCodeableConcept.coding` (912, tanpa BQ) |
| 69 | 919–940 | Observation | SP000010 | Skrining Hipertensi dalam Kehamilan | _Pre Eklampsia_ → `Observation.valueCodeableConcept.coding` (929, tanpa BQ) |
| 70 | 941–959 | Observation | SP000012 | Tatalaksana Pre Eklampsia | _Tatalaksana Pre Eklampsia_ → `Observation.valueBoolean` (944, tanpa BQ) |
| 71 | 961–979 | Observation | SP000014 | Tatalaksana KEK | _Tatalaksana KEK_ → `Observation.valueBoolean` (972, tanpa BQ) |
| 72 | 981–1016 | Observation | SP000015 | Risiko Masalah Kesehatan | _Risiko Masalah Kesehatan Lainnya_ → `Observation.valueBoolean` (991, tanpa BQ) |
| 73 | 1017–1028 | Observation | SP000016 | Tatalaksana Masalah Kesehatan | _Diberikan Tatalaksana Risiko Masalah Kesehatan Lainnya_ → `Observation.valueBoolean` (1020, tanpa BQ) |
| 74 | 1029–1039 | Procedure | 1230101008.0 | Counseling for pregnancy | _Konseling_ → `Procedure.category.coding` (1029, tanpa BQ) |
| 75 | 1040–1051 | Procedure | 385892002.0 | Mental health screening | _Skrinning Keswa_ → `Procedure.category.coding` (1040, tanpa BQ) |
| 76 | 1052–1063 | Observation | 11996-6 | [#] Pregnancies | _Gravida_ → `Observation.valueInteger` (1056, tanpa BQ) |
| 77 | 1064–1075 | Observation | 11977-6 | [#] Parity | _Partus_ → `Observation.valueInteger` (1068, tanpa BQ) |
| 78 | 1076–1087 | Observation | 69043-8 | Other pregnancy outcomes # | _Abortus_ → `Observation.valueInteger` (1080, tanpa BQ) |
| 79 | 1088–1100 | Observation | OC000001 | Jarak kehamilan | _Jarak kehamilan saat ini dengan kehamilan sebelumnya_ → `Observation.valueQuantity.value` (1092, tanpa BQ) |
| 80 | 1101–1112 | Observation | 246435002.0 | Number of fetuses | _Jumlah Janin_ → `Observation.valueInteger` (1105, tanpa BQ) |
| 81 | 1113–1124 | Observation | 73211009.0 | Diabetes mellitus | _Diabetes_ → `Observation.valueBoolean` (1116, tanpa BQ) |
| 82 | 1125–1136 | Observation | 278977008.0 | Human immunodeficiency virus status | _HIV_ → `Observation.valueCodeableConcept.coding` (1128, tanpa BQ) |
| 83 | 1137–1148 | Observation | 66071002.0 | Viral hepatitis type B | _Hepatitis B_ → `Observation.valueBoolean` (1140, tanpa BQ) |
| 84 | 1149–1160 | Observation | 76272004.0 | Syphilis | _Sifilis_ → `Observation.valueBoolean` (1152, tanpa BQ) |
| 85 | 1161–1172 | Observation | 61462000.0 | Malaria | _Malaria_ → `Observation.valueBoolean` (1164, tanpa BQ) |
| 86 | 1173–1184 | Observation | 56717001.0 | Tuberculosis | _Tuberkulosis_ → `Observation.valueBoolean` (1176, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 47 |
| PractitionerRole | 7 |
| ServiceRequest | 6 |
| Specimen | 6 |
| DiagnosticReport | 6 |
| Immunization | 3 |
| Procedure | 3 |
| Condition | 2 |
| Patient | 1 |
| Practitioner | 1 |
| EpisodeOfCare | 1 |
| Encounter | 1 |
| MedicationRequest | 1 |
| MedicationDispense | 1 |
| **Total** | **86** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 76 | PractitionerRole | `PractitionerRole.code.coding` | 309453006.0 | Registered midwife | http://snomed.info/sct |
| 2 | 77 | PractitionerRole | `PractitionerRole.code.coding` | 309343006.0 | Physician | http://snomed.info/sct |
| 3 | 78 | PractitionerRole | `PractitionerRole.code.coding` | 309367003.0 | Obstetrician and gynecologist | http://snomed.info/sct |
| 4 | 79 | PractitionerRole | `PractitionerRole.code.coding` | 224535009.0 | Registered nurse | http://snomed.info/sct |
| 5 | 106 | EpisodeOfCare | `EpisodeOfCare.type.coding` | ANC | Antenatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 6 | 128 | Condition | `Condition.code.coding` | 134435003.0 | Routine antenatal care | http://snomed.info/sct |
| 7 | 147 | Observation | `Observation.code.coding` | 424144002.0 | Current chronological age | http://snomed.info/sct |
| 8 | 159 | Observation | `Observation.code.coding` | SP000132 | Memiliki Buku KIA | http://terminology.kemkes.go.id/sp |
| 9 | 171 | Observation | `Observation.code.coding` | 8665-2 | Last menstrual period start date | http://loinc.org |
| 10 | 172 | Observation | `Observation.code.coding` | ANC.B6.DE14 | Last menstrual period (LMP) date | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 11 | 183 | Observation | `Observation.code.coding` | 11778-8 | Delivery date Estimated | http://loinc.org |
| 12 | 184 | Observation | `Observation.code.coding` | ANC.B6.DE22 | Expected date of delivery (EDD) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 13 | 195 | Observation | `Observation.code.coding` | 56077-1 | Body weight --pre current pregnancy | http://loinc.org |
| 14 | 196 | Observation | `Observation.code.coding` | ANC.B8.DE2 | Pre-gestational weight | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 15 | 208 | Observation | `Observation.code.coding` | 8302-2 | Body height | http://loinc.org |
| 16 | 209 | Observation | `Observation.code.coding` | ANC.B8.DE1 | Height | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 17 | 221 | Observation | `Observation.code.coding` | OC000010 | Indeks Massa Tubuh Sebelum Hamil | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 18 | 222 | Observation | `Observation.code.coding` | ANC.SS.DE58 | IMT Sebelum Hamil | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 19 | 234 | Immunization | `Immunization.vaccineCode` | VG139 | Td | http://sys-ids.kemkes.go.id/kfa |
| 20 | 251 | Immunization | `Immunization.vaccineCode` | VG139 | Td | http://sys-ids.kemkes.go.id/kfa |
| 21 | 268 | Immunization | `Immunization.vaccineCode` | VG139 | Td | http://sys-ids.kemkes.go.id/kfa |
| 22 | 281 | Observation | `Observation.code.coding` | SP000001 | Skrining Imunisasi Tetanus Toksoid | http://terminology.kemkes.go.id/sp |
| 23 | 282 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 24 | 292 | Observation | `Observation.code.coding` | SP000002 | Kunjungan Pertama Pemeriksaan Kehamilan | http://terminology.kemkes.go.id/sp |
| 25 | 303 | Observation | `Observation.code.coding` | 18185-9 | Gestational age | http://loinc.org |
| 26 | 304 | Observation | `Observation.code.coding` | ANC.B6.DE17 | Gestational age | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 27 | 307 | Observation | `Observation.component.code.coding` | SP000461 | Usia Kehamilan (Hari) | http://terminology.kemkes.go.id/sp |
| 28 | 319 | Observation | `Observation.code.coding` | 32418-6 | Obstetric trimester Stated | http://loinc.org |
| 29 | 320 | Observation | `Observation.code.coding` | ANC.SS.DE13 | Trimester ke | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 30 | 335 | Observation | `Observation.code.coding` | 32418-6 | Obstetric trimester Stated | http://loinc.org |
| 31 | 336 | Observation | `Observation.code.coding` | ANC.SS.DE13 | Trimester ke | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 32 | 353 | Observation | `Observation.code.coding` | 32418-6 | Obstetric trimester Stated | http://loinc.org |
| 33 | 354 | Observation | `Observation.code.coding` | ANC.SS.DE13 | Trimester ke | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 34 | 373 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 35 | 374 | Observation | `Observation.code.coding` | ANC.B8.DE3 | Current weight | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 36 | 386 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 37 | 387 | Observation | `Observation.code.coding` | ANC.B8.DE17 | Systolic blood pressure | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 38 | 399 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://loinc.org |
| 39 | 400 | Observation | `Observation.code.coding` | ANC.B8.DE19 | Diastolic blood pressure | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 40 | 412 | Observation | `Observation.code.coding` | 284473002.0 | Mid upper arm circumference | http://snomed.info/sct |
| 41 | 413 | Observation | `Observation.code.coding` | ANC.SS.DE3 | Lingkar Lengan Atas (LILA) | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 42 | 422 | Observation | `Observation.interpretation` | OI000018 | Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 43 | 423 | Observation | `Observation.interpretation` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 44 | 424 | Observation | `Observation.interpretation` | OI000035 | Risiko Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 45 | 427 | Observation | `Observation.code.coding` | 11881-0 | Uterus Fundal height Tape measure | http://loinc.org |
| 46 | 428 | Observation | `Observation.code.coding` | ANC.B8.DE105 | Symphysis-fundal height | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 47 | 440 | Observation | `Observation.code.coding` | 883-9 | ABO group [Type] in Blood | http://loinc.org |
| 48 | 441 | Observation | `Observation.code.coding` | ANC.B9.DE24 | Blood type | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 49 | 442 | Observation | `Observation.valueCodeableConcept.coding` | LA19710-5 | Group A | http://loinc.org |
| 50 | 443 | Observation | `Observation.valueCodeableConcept.coding` | LA19709-7 | Group B | http://loinc.org |
| 51 | 444 | Observation | `Observation.valueCodeableConcept.coding` | LA19708-9 | Group O | http://loinc.org |
| 52 | 445 | Observation | `Observation.valueCodeableConcept.coding` | LA28449-9 | Group AB | http://loinc.org |
| 53 | 455 | Observation | `Observation.code.coding` | 10331-7 | Rh [Type] in Blood | http://loinc.org |
| 54 | 456 | Observation | `Observation.code.coding` | ANC.B9.DE29 | Rh factor | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 55 | 457 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 56 | 458 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 57 | 468 | Observation | `Observation.code.coding` | 55283-6 | Fetal Heart rate | http://loinc.org |
| 58 | 469 | Observation | `Observation.code.coding` | ANC.B8.DE107 | Fetal heart rate | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 59 | 481 | Observation | `Observation.code.coding` | 72155-5 | Position in womb Fetus [RHEA] | http://loinc.org |
| 60 | 482 | Observation | `Observation.code.coding` | ANC.B8.DE111 | Fetal presentation | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 61 | 483 | Observation | `Observation.valueCodeableConcept.coding` | 1209182005.0 | Cephalic fetal presentation | http://snomed.info/sct |
| 62 | 484 | Observation | `Observation.valueCodeableConcept.coding` | SP000005 | Letak Bokong/ Lintang | http://terminology.kemkes.go.id/sp |
| 63 | 485 | Observation | `Observation.valueCodeableConcept.coding` | SP000006 | Organ Tubuh Lainnya | http://terminology.kemkes.go.id/sp |
| 64 | 486 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 65 | 496 | Condition | `Condition.code.coding` | 34842007.0 | Antepartum hemorrhage | http://snomed.info/sct |
| 66 | 497 | Condition | `Condition.code.coding` | 15938005.0 | Eclampsia | http://snomed.info/sct |
| 67 | 498 | Condition | `Condition.code.coding` | 398254007.0 | Pre-eclampsia | http://snomed.info/sct |
| 68 | 499 | Condition | `Condition.code.coding` | 386639001.0 | Termination of pregnancy | http://snomed.info/sct |
| 69 | 500 | Condition | `Condition.code.coding` | 40733004.0 | Infectious disease | http://snomed.info/sct |
| 70 | 501 | Condition | `Condition.code.coding` | 91302008.0 | Sepsis | http://snomed.info/sct |
| 71 | 502 | Condition | `Condition.code.coding` | 404684003.0 | Clinical finding | http://snomed.info/sct |
| 72 | 510 | Procedure | `Procedure.code.coding` | 88.78 | Diagnostic ultrasound of gravid uterus | http://hl7.org/fhir/sid/icd-9-cm |
| 73 | 522 | Observation | `Observation.code.coding` | 268445003.0 | Ultrasound scan - obstetric | http://snomed.info/sct |
| 74 | 523 | Observation | `Observation.valueCodeableConcept.coding` | 169221005.0 | Ultrasound obstetric scan normal | http://snomed.info/sct |
| 75 | 524 | Observation | `Observation.valueCodeableConcept.coding` | 169255008.0 | Ultrasound scan abnormal | http://snomed.info/sct |
| 76 | 525 | Observation | `Observation.dataAbsentReason.coding` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 77 | 537 | MedicationRequest | `MedicationRequest.contained.code.coding` | 92000653.0 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula | http://sys-ids.kemkes.go.id/kf |
| 78 | 571 | MedicationDispense | `MedicationDispense.contained.code.coding` | 93015491.0 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | http://sys-ids.kemkes.go.id/kf |
| 79 | 604 | ServiceRequest | `ServiceRequest.code` | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 80 | 612 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002.0 | Laboratory worker | http://snomed.info/sct |
| 81 | 615 | Specimen | `Specimen.type` | 122555007.0 | Venous blood specimen | http://snomed.info/sct |
| 82 | 624 | Observation | `Observation.code.coding` | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 83 | 625 | Observation | `Observation.code.coding` | ANC.B9.DE32 | HIV test | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 84 | 626 | Observation | `Observation.valueCodeableConcept.coding` | LA15255-5 | Reactive | http://loinc.org |
| 85 | 627 | Observation | `Observation.valueCodeableConcept.coding` | LA15256-3 | Nonreactive | http://loinc.org |
| 86 | 628 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 87 | 638 | DiagnosticReport | `DiagnosticReport.code` | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 88 | 652 | ServiceRequest | `ServiceRequest.code` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 89 | 660 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002.0 | Laboratory worker | http://snomed.info/sct |
| 90 | 663 | Specimen | `Specimen.type` | 122555007.0 | Venous blood specimen | http://snomed.info/sct |
| 91 | 672 | Observation | `Observation.code.coding` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 92 | 673 | Observation | `Observation.code.coding` | ANC.B9.DE60 | Hepatitis B test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 93 | 674 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 94 | 675 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 95 | 676 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 96 | 686 | DiagnosticReport | `DiagnosticReport.code` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 97 | 700 | ServiceRequest | `ServiceRequest.code` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 98 | 708 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002.0 | Laboratory worker | http://snomed.info/sct |
| 99 | 711 | Specimen | `Specimen.type` | 122555007.0 | Venous blood specimen | http://snomed.info/sct |
| 100 | 720 | Observation | `Observation.code.coding` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 101 | 721 | Observation | `Observation.code.coding` | ANC.B9.DE96 | Syphilis test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 102 | 722 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 103 | 723 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 104 | 724 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 105 | 734 | DiagnosticReport | `DiagnosticReport.code` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 106 | 748 | ServiceRequest | `ServiceRequest.code` | 2887-8 | Protein [Presence] in Urine | http://loinc.org |
| 107 | 756 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002.0 | Laboratory worker | http://snomed.info/sct |
| 108 | 759 | Specimen | `Specimen.type` | 122575003.0 | Urine specimen | http://snomed.info/sct |
| 109 | 768 | Observation | `Observation.code.coding` | 2887-8 | Protein [Presence] in Urine | http://loinc.org |
| 110 | 769 | Observation | `Observation.code.coding` | ANC.B9.DE114 | Urine test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 111 | 770 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 112 | 771 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 113 | 772 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 114 | 782 | DiagnosticReport | `DiagnosticReport.code.coding` | 2887-8 | Protein [Presence] in Urine | http://loinc.org |
| 115 | 796 | ServiceRequest | `ServiceRequest.code` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 116 | 804 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002.0 | Laboratory worker | http://snomed.info/sct |
| 117 | 807 | Specimen | `Specimen.type` | 122555007.0 | Venous blood specimen | http://snomed.info/sct |
| 118 | 816 | Observation | `Observation.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 119 | 817 | Observation | `Observation.code.coding` | ANC.B9.DE175 | Blood hemoglobin test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 120 | 820 | Observation | `Observation.interpretation.coding` | 860635002.0 | No anemia present | http://snomed.info/sct |
| 121 | 821 | Observation | `Observation.interpretation.coding` | OI000032 | Anemia ringan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 122 | 822 | Observation | `Observation.interpretation.coding` | OI000033 | Anemia sedang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 123 | 823 | Observation | `Observation.interpretation.coding` | OI000034 | Anemia berat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 124 | 824 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 125 | 834 | DiagnosticReport | `DiagnosticReport.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 126 | 848 | ServiceRequest | `ServiceRequest.code` | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | http://loinc.org |
| 127 | 856 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002.0 | Laboratory worker | http://snomed.info/sct |
| 128 | 859 | Specimen | `Specimen.type` | 122555007.0 | Venous blood specimen | http://snomed.info/sct |
| 129 | 868 | Observation | `Observation.code.coding` | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | http://loinc.org |
| 130 | 869 | Observation | `Observation.code.coding` | ANC.B9.DE159 | Blood glucose test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 131 | 872 | Observation | `Observation.interpretation.coding` | 166921001.0 | Blood glucose normal | http://snomed.info/sct |
| 132 | 873 | Observation | `Observation.interpretation.coding` | 166922008.0 | Blood glucose abnormal | http://snomed.info/sct |
| 133 | 874 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 134 | 884 | DiagnosticReport | `DiagnosticReport.code.coding` | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | http://loinc.org |
| 135 | 896 | Observation | `Observation.code.coding` | 15220000.0 | Laboratory test | http://snomed.info/sct |
| 136 | 897 | Observation | `Observation.valueCodeableConcept.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 137 | 898 | Observation | `Observation.valueCodeableConcept.coding` | 76772-3 | Plasmodium falciparum Ag [Presence] in Blood by Rapid immunoassay | http://loinc.org |
| 138 | 899 | Observation | `Observation.valueCodeableConcept.coding` | 104742-2 | Ova and parasites identified in Specimen | http://loinc.org |
| 139 | 900 | Observation | `Observation.valueCodeableConcept.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 140 | 911 | Observation | `Observation.code.coding` | SP000007 | Tatalaksana Anemia | http://terminology.kemkes.go.id/sp |
| 141 | 912 | Observation | `Observation.valueCodeableConcept.coding` | SP000008 | Pemberian Tablet Tambah Darah | http://terminology.kemkes.go.id/sp |
| 142 | 913 | Observation | `Observation.valueCodeableConcept.coding` | SP000009 | Pemberian Fe Parenteral | http://terminology.kemkes.go.id/sp |
| 143 | 914 | Observation | `Observation.valueCodeableConcept.coding` | 116859006.0 | Transfusion of blood product | http://snomed.info/sct |
| 144 | 915 | Observation | `Observation.valueCodeableConcept.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 145 | 917 | Observation | `Observation.valueCodeableConcept.coding` | 3457005.0 | Patient referral | http://snomed.info/sct |
| 146 | 928 | Observation | `Observation.code.coding` | SP000010 | Skrining Hipertensi dalam Kehamilan | http://terminology.kemkes.go.id/sp |
| 147 | 929 | Observation | `Observation.valueCodeableConcept.coding` | SP000011 | Tidak Pre Eklampsia/ Eklampsia | http://terminology.kemkes.go.id/sp |
| 148 | 930 | Observation | `Observation.valueCodeableConcept.coding` | 48194001.0 | Pregnancy-induced hypertension | http://snomed.info/sct |
| 149 | 931 | Observation | `Observation.valueCodeableConcept.coding` | 398254007.0 | Pre-eclampsia | http://snomed.info/sct |
| 150 | 932 | Observation | `Observation.valueCodeableConcept.coding` | 15938005.0 | Eclampsia | http://snomed.info/sct |
| 151 | 933 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 152 | 943 | Observation | `Observation.code.coding` | SP000012 | Tatalaksana Pre Eklampsia | http://terminology.kemkes.go.id/sp |
| 153 | 946 | Observation | `Observation.component.code.coding` | 135840009.0 | Blood pressure monitoring | http://snomed.info/sct |
| 154 | 949 | Observation | `Observation.component.code.coding` | 308116003.0 | Antihypertensive therapy | http://snomed.info/sct |
| 155 | 952 | Observation | `Observation.component.code.coding` | SP000013 | Pemberian MgSO4 | http://terminology.kemkes.go.id/sp |
| 156 | 955 | Observation | `Observation.component.code.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 157 | 957 | Observation | `Observation.component.code.coding` | 3457005.0 | Patient referral | http://snomed.info/sct |
| 158 | 961 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 159 | 971 | Observation | `Observation.code.coding` | SP000014 | Tatalaksana KEK | http://terminology.kemkes.go.id/sp |
| 160 | 974 | Observation | `Observation.component.code.coding` | 435591000124104.0 | Nutrition supplement therapy | http://snomed.info/sct |
| 161 | 977 | Observation | `Observation.component.code.coding` | 3457005.0 | Patient referral | http://snomed.info/sct |
| 162 | 990 | Observation | `Observation.code.coding` | SP000015 | Risiko Masalah Kesehatan | http://terminology.kemkes.go.id/sp |
| 163 | 993 | Observation | `Observation.component.code.coding` | 40733004.0 | Infectious disease | http://snomed.info/sct |
| 164 | 996 | Observation | `Observation.component.code.coding` | 73211009.0 | Diabetes mellitus | http://snomed.info/sct |
| 165 | 999 | Observation | `Observation.component.code.coding` | 414916001.0 | Obesity | http://snomed.info/sct |
| 166 | 1002 | Observation | `Observation.component.code.coding` | 56717001.0 | Tuberculosis | http://snomed.info/sct |
| 167 | 1005 | Observation | `Observation.component.code.coding` | 56265001.0 | Heart disease | http://snomed.info/sct |
| 168 | 1008 | Observation | `Observation.component.code.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 169 | 1019 | Observation | `Observation.code.coding` | SP000016 | Tatalaksana Masalah Kesehatan | http://terminology.kemkes.go.id/sp |
| 170 | 1030 | Procedure | `Procedure.code.coding` | 1230101008.0 | Counseling for pregnancy | http://snomed.info/sct |
| 171 | 1041 | Procedure | `Procedure.code.coding` | 385892002.0 | Mental health screening | http://snomed.info/sct |
| 172 | 1054 | Observation | `Observation.code.coding` | 11996-6 | [#] Pregnancies | http://loinc.org |
| 173 | 1055 | Observation | `Observation.code.coding` | ANC.B6.DE24 | Number of pregnancies (gravida) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 174 | 1066 | Observation | `Observation.code.coding` | 11977-6 | [#] Parity | http://loinc.org |
| 175 | 1067 | Observation | `Observation.code.coding` | ANC.B6.DE32 | Parity | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 176 | 1078 | Observation | `Observation.code.coding` | 69043-8 | Other pregnancy outcomes # | http://loinc.org |
| 177 | 1079 | Observation | `Observation.code.coding` | ANC.B6.DE25 | Number of miscarriages and/or abortions | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 178 | 1090 | Observation | `Observation.code.coding` | OC000001 | Jarak kehamilan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 179 | 1091 | Observation | `Observation.code.coding` | ANC.SS.DE53 | Jarak kehamilan | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 180 | 1103 | Observation | `Observation.code.coding` | 246435002.0 | Number of fetuses | http://snomed.info/sct |
| 181 | 1104 | Observation | `Observation.code.coding` | ANC.B8.DE109 | Number of fetuses | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 182 | 1115 | Observation | `Observation.code.coding` | 73211009.0 | Diabetes mellitus | http://snomed.info/sct |
| 183 | 1127 | Observation | `Observation.code.coding` | 278977008.0 | Human immunodeficiency virus status | http://snomed.info/sct |
| 184 | 1128 | Observation | `Observation.valueCodeableConcept.coding` | 165816005.0 | Human immunodeficiency virus detected | http://snomed.info/sct |
| 185 | 1129 | Observation | `Observation.valueCodeableConcept.coding` | 165815009.0 | Human immunodeficiency virus not detected | http://snomed.info/sct |
| 186 | 1139 | Observation | `Observation.code.coding` | 66071002.0 | Viral hepatitis type B | http://snomed.info/sct |
| 187 | 1151 | Observation | `Observation.code.coding` | 76272004.0 | Syphilis | http://snomed.info/sct |
| 188 | 1163 | Observation | `Observation.code.coding` | 61462000.0 | Malaria | http://snomed.info/sct |
| 189 | 1175 | Observation | `Observation.code.coding` | 56717001.0 | Tuberculosis | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 64 |
| http://loinc.org | 54 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 23 |
| http://terminology.kemkes.go.id/sp | 16 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 11 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 7 |
| http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes | 6 |
| http://sys-ids.kemkes.go.id/kfa | 3 |
| http://sys-ids.kemkes.go.id/kf | 2 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 1 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 1 |
| http://hl7.org/fhir/sid/icd-9-cm | 1 |
| **Total** | **189** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 30 | – | Faskes yang Melayani ANC | Organization | `Organization.type` |
| 35 | – | Faskes yang Melayani ANC | Organization | `Organization.name` |
| 39 | – | Nama Provinsi | Organization | `Organization.address.extension.extension.url` |
| 42 | – | Nama Kabupaten | Organization | `Organization.address.extension.extension.url` |
| 45 | – | Nama Kecamatan | Organization | `Organization.address.extension.extension.url` |
| 48 | – | Nama Desa | Organization | `Organization.address.extension.extension.url` |
| 50 | – | Tempat Pelayanan ANC | Location | `Location.identifier` |
| 58 | – | Nama Provinsi | Location | `Location.address.extension.extension.url` |
| 61 | – | Nama Kabupaten | Location | `Location.address.extension.extension.url` |
| 64 | – | Nama Kecamatan | Location | `Location.address.extension.extension.url` |
| 67 | – | Nama Desa | Location | `Location.address.extension.extension.url` |
| 1185 | – | ART | – | `Observation` |
| 1197 | – | Obat Anti Malaria | – | `Observation` |
| 1218 | – | Obat Anti Tuberkulosis (OAT) | – | `Observation` |
| 1242 | – | Obat Diabetes Melitus | – | `Observation` |
