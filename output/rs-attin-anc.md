# Output Form: SIM RS At tin ANC

Sumber: `mapping/phdt-data-dictionary-rs-attin-anc.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-rs-attin-anc.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 89 |
| Code (`jumlah code` = 1) | 194 |
| Code unik (code + CodeSystem) | 143 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 22 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–27 | Patient | – | – | _Nama Ibu_ → `Patient.name.text` (2, tanpa BQ)<br>_NIK_ → `Patient.identifier.value` (6, tanpa BQ)<br>_No HP_ → `Patient.telecom` (7, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (10, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (11, tanpa BQ)<br>_Alamat Domisili_ → `Patient.address.line` (13, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (18, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (21, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.extension.valueCode` (24, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.extension.valueCode` (27, tanpa BQ) |
| 2 | 66–72 | Practitioner | – | – | _NIK_ → `Practitioner.identifier.value` (68, tanpa BQ)<br>_Nama Tenaga Kesehatan_ → `Practitioner.name.text` (70, tanpa BQ)<br>_Jenis Kelamin Tenaga Kesehatan_ → `Practitioner.gender` (71, tanpa BQ) |
| 3 | 73–80 | PractitionerRole | – | – | _Tenaga Pemeriksa_ → `PractitionerRole.code.coding` (77, tanpa BQ) |
| 4 | 82–95 | Encounter | – | – | _Tanggal Kunjungan ANC_ → `Encounter.period.start` (90, tanpa BQ)<br>_Tempat Pelayanan ANC_ → `Encounter.location.location.display` (93, tanpa BQ) |
| 5 | 96–104 | Condition | 134435003.0 | Routine antenatal care | _Kode ICD - Diagnosa_ → `Condition.clinicalStatus.coding` (96, tanpa BQ) |
| 6 | 115–123 | EpisodeOfCare | ANC | Antenatal Care | – |
| 7 | 124–135 | Observation | SP000132 | Memiliki Buku KIA | _Memiliki Buku KIA_ → `Observation.valueBoolean` (126, tanpa BQ) |
| 8 | 136–147 | Observation | 8665-2 | Last menstrual period start date | _HPHT_ → `Observation.valueDateTime` (140, tanpa BQ) |
| 9 | 148–159 | Observation | 11778-8 | Delivery date Estimated | _Tanggal Perkiraan Persalinan (HPL)_ → `Observation.valueDateTime` (152, tanpa BQ) |
| 10 | 160–172 | Observation | 56077-1 | Body weight --pre current pregnancy | _Berat Badan Sebelum Hamil_ → `Observation.valueQuantity.value` (164, tanpa BQ) |
| 11 | 173–185 | Observation | 8302-2 | Body height | _Tinggi Badan_ → `Observation.valueQuantity.value` (177, tanpa BQ) |
| 12 | 186–196 | Observation | SP000683 | Tatalaksana Tindakan | _Tatalaksana (Tindakan)_ → `Observation.valueString` (189, tanpa BQ) |
| 13 | 197–207 | Observation | SP000684 | Tatalaksana Obat | _Tatalaksana Obat_ → `Observation.valueString` (200, tanpa BQ) |
| 14 | 208–216 | Condition | 609496007.0 | Complication occurring during pregnancy | _Komplikasi_ → `Condition.clinicalStatus.coding` (208, tanpa BQ) |
| 15 | 217–229 | Observation | OC000010 | Indeks Massa Tubuh Sebelum Hamil | _IMT Sebelum Hamil_ → `Observation.valueQuantity.value` (221, tanpa BQ) |
| 16 | 230–248 | Immunization | – | – | _Dilakukan Imunisasi TT (Pada Kunjungan Ini)_ → `Immunization.status` (230, tanpa BQ)<br>_Riwayat Imunisasi TT_ → `Immunization.status` (247, tanpa BQ) |
| 17 | 249–265 | Immunization | – | – | – |
| 18 | 266–276 | Immunization | – | – | – |
| 19 | 277–287 | Observation | SP000001 | Skrining Imunisasi Tetanus Toksoid | – |
| 20 | 288–298 | Observation | SP000002 | Kunjungan Pertama Pemeriksaan Kehamilan | _Pemeriksaan ANC Pertama_ → `Observation.valueBoolean` (291, tanpa BQ) |
| 21 | 299–314 | Observation | 18185-9 | Gestational age | _Usia Kehamilan (dalam minggu)_ → `Observation.valueQuantity.value` (303, tanpa BQ) |
| 22 | 315–326 | Observation | 32418-6 | Obstetric trimester Stated | _Trimester_ → `Observation.valueInteger` (319, tanpa BQ) |
| 23 | 327–339 | Observation | 29463-7 | Body weight | _Berat Badan (dalam kg)_ → `Observation.valueQuantity.value` (331, tanpa BQ) |
| 24 | 340–351 | Observation | 8480-6 | Systolic blood pressure | _Tekanan Darah Sistolik_ → `Observation.valueQuantity.value` (343, tanpa BQ) |
| 25 | 352–363 | Observation | 8462-4 | Diastolic blood pressure | _Tekanan Darah Diastolik_ → `Observation.valueQuantity.value` (355, tanpa BQ) |
| 26 | 364–378 | Observation | 284473002.0 | Mid upper arm circumference | _LiLA_ → `Observation.status` (364, tanpa BQ)<br>_Status Gizi KEK/Tidak KEK_ → `Observation.interpretation` (376, tanpa BQ) |
| 27 | 379–393 | Observation | 11881-0 | Uterus Fundal height Tape measure | _Tinggi Fundus_ → `Observation.valueQuantity.value` (383, tanpa BQ) |
| 28 | 394–408 | Observation | 883-9 | ABO group [Type] in Blood | _Lab : Golongan Darah_ → `Observation.valueCodeableConcept.coding` (398, tanpa BQ) |
| 29 | 409–421 | Observation | 10331-7 | Rh [Type] in Blood | _Lab : Rhesus_ → `Observation.valueCodeableConcept.coding` (413, tanpa BQ) |
| 30 | 422–434 | Observation | 55283-6 | Fetal Heart rate | _Denyut Jantung Janin_ → `Observation.valueQuantity.value` (426, tanpa BQ) |
| 31 | 435–449 | Observation | 72155-5 | Position in womb Fetus [RHEA] | _Presentasi Janin_ → `Observation.valueCodeableConcept.coding` (439, tanpa BQ) |
| 32 | 450–464 | Condition | 34842007.0 | Antepartum hemorrhage | _Komplikasi Kehamilan_ → `Condition.clinicalStatus.coding` (450, tanpa BQ) |
| 33 | 465–478 | Observation | 268445003.0 | Ultrasound scan - obstetric | _Diperiksa USG_ → `Observation.valueCodeableConcept.coding` (468, tanpa BQ)<br>_Jika diperiksa, hasil tidak normal. Tidak normal karena apa?_ → `Observation.valueCodeableConcept.text` (470, tanpa BQ) |
| 34 | 479–490 | Observation | 11996-6 | [#] Pregnancies | _Gravida_ → `Observation.valueInteger` (483, tanpa BQ) |
| 35 | 491–502 | Observation | 11977-6 | [#] Parity | _Partus_ → `Observation.valueInteger` (495, tanpa BQ) |
| 36 | 503–514 | Observation | 69043-8 | Other pregnancy outcomes # | _Abortus_ → `Observation.valueInteger` (507, tanpa BQ) |
| 37 | 515–524 | ServiceRequest | – | – | _Lab : HIV_ → `ServiceRequest.category` (515, tanpa BQ) |
| 38 | 525–528 | PractitionerRole | – | – | – |
| 39 | 529–536 | Specimen | – | – | – |
| 40 | 537–550 | Observation | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | – |
| 41 | 551–562 | DiagnosticReport | – | – | – |
| 42 | 563–572 | ServiceRequest | – | – | _Lab : Hepatitis_ → `ServiceRequest.category` (563, tanpa BQ) |
| 43 | 573–576 | PractitionerRole | – | – | – |
| 44 | 577–584 | Specimen | – | – | – |
| 45 | 585–598 | Observation | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | – |
| 46 | 599–610 | DiagnosticReport | – | – | – |
| 47 | 611–620 | ServiceRequest | – | – | _Lab : Siphilis_ → `ServiceRequest.category` (611, tanpa BQ) |
| 48 | 621–624 | PractitionerRole | – | – | – |
| 49 | 625–632 | Specimen | – | – | – |
| 50 | 633–646 | Observation | 22464-2 | Reagin Ab [Presence] in Specimen | – |
| 51 | 647–658 | DiagnosticReport | – | – | – |
| 52 | 659–668 | ServiceRequest | – | – | _Lab : Protein Urine_ → `ServiceRequest.category` (659, tanpa BQ) |
| 53 | 669–672 | PractitionerRole | – | – | – |
| 54 | 673–680 | Specimen | – | – | – |
| 55 | 681–694 | Observation | 2887-8 | Protein [Presence] in Urine | – |
| 56 | 695–706 | DiagnosticReport | 2887-8 | Protein [Presence] in Urine | – |
| 57 | 707–716 | ServiceRequest | – | – | _Lab : Hb_ → `ServiceRequest.category` (707, tanpa BQ) |
| 58 | 717–720 | PractitionerRole | – | – | – |
| 59 | 721–728 | Specimen | – | – | – |
| 60 | 729–746 | Observation | 718-7 | Hemoglobin [Mass/volume] in Blood | – |
| 61 | 747–758 | DiagnosticReport | 718-7 | Hemoglobin [Mass/volume] in Blood | – |
| 62 | 759–768 | ServiceRequest | – | – | _Lab : Gula Sewaktu_ → `ServiceRequest.category` (759, tanpa BQ) |
| 63 | 769–772 | PractitionerRole | – | – | – |
| 64 | 773–780 | Specimen | – | – | – |
| 65 | 781–796 | Observation | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | – |
| 66 | 797–808 | DiagnosticReport | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | – |
| 67 | 809–817 | Observation | SP000007 | Tatalaksana Anemia | _Tatalaksana Anemia_ → `Observation.valueCodeableConcept.coding` (812, tanpa BQ) |
| 68 | 819–840 | Observation | SP000010 | Skrining Hipertensi dalam Kehamilan | _Pre Eklampsia_ → `Observation.valueCodeableConcept.coding` (829, tanpa BQ) |
| 69 | 841–860 | Observation | SP000012 | Tatalaksana Pre Eklampsia | _Tatalaksana Pre Eklampsia_ → `Observation.valueString` (844, tanpa BQ) |
| 70 | 862–886 | Observation | SP000014 | Tatalaksana KEK | _Tatalaksana KEK_ → `Observation.valueString` (873, tanpa BQ) |
| 71 | 887–916 | Observation | SP000015 | Risiko Masalah Kesehatan | _Risiko Masalah Kesehatan Lainnya_ → `Observation.valueString` (890, tanpa BQ) |
| 72 | 917–928 | Observation | SP000016 | Tatalaksana Masalah Kesehatan | _Diberikan Tatalaksana Risiko Masalah Kesehatan Lainnya_ → `Observation.valueBoolean` (920, tanpa BQ) |
| 73 | 929–939 | Procedure | 1230101008.0 | Counseling for pregnancy | _Konseling_ → `Procedure.category.coding` (929, tanpa BQ) |
| 74 | 940–951 | Procedure | 385892002.0 | Mental health screening | _Skrinning Keswa_ → `Procedure.category.coding` (940, tanpa BQ) |
| 75 | 952–964 | Observation | OC000001 | Jarak kehamilan | _Jarak kehamilan saat ini dengan kehamilan sebelumnya_ → `Observation.valueQuantity.value` (956, tanpa BQ) |
| 76 | 965–976 | Observation | 246435002.0 | Number of fetuses | _Jumlah Janin_ → `Observation.valueInteger` (969, tanpa BQ) |
| 77 | 977–988 | Observation | 73211009.0 | Diabetes mellitus | _Diabetes_ → `Observation.valueBoolean` (980, tanpa BQ) |
| 78 | 989–1000 | Observation | 278977008.0 | Human immunodeficiency virus status | _HIV_ → `Observation.valueCodeableConcept.coding` (992, tanpa BQ) |
| 79 | 1001–1012 | Observation | 66071002.0 | Viral hepatitis type B | _Hepatitis B_ → `Observation.valueBoolean` (1004, tanpa BQ) |
| 80 | 1013–1024 | Observation | 11258-1 | Hepatitis B virus DNA [Units/volume] in Serum | _Nilai Hasil Pemeriksaan Lanjutan Hepatitis (HBV DNA) (range: >= 10 dan <= 100000000)_ → `Observation.valueQuantity.value` (1016, tanpa BQ) |
| 81 | 1025–1036 | Observation | 39007-0 | Hepatitis B virus e Ag [Presence] in Specimen | _Hasil Pemeriksaan Lanjutan Hepatitis (HBeAg)_ → `Observation.valueCodeableConcept.coding` (1028, tanpa BQ) |
| 82 | 1037–1048 | Observation | 76272004.0 | Syphilis | _Sifilis_ → `Observation.valueBoolean` (1040, tanpa BQ) |
| 83 | 1049–1060 | Observation | 61462000.0 | Malaria | _Malaria_ → `Observation.valueBoolean` (1052, tanpa BQ) |
| 84 | 1061–1072 | Observation | 56717001.0 | Tuberculosis | _Tuberkulosis_ → `Observation.valueBoolean` (1064, tanpa BQ) |
| 85 | 1073–1084 | Observation | SP000046 | Terapi Antiretroviral (ART) | _ART_ → `Observation.valueBoolean` (1076, tanpa BQ) |
| 86 | 1085–1105 | Observation | SP000124 | Obat anti malaria | _Obat Anti Malaria_ → `Observation.valueBoolean` (1088, tanpa BQ) |
| 87 | 1106–1129 | Observation | SP000125 | Obat anti tuberkulosis | _Obat Anti Tuberkulosis (OAT)_ → `Observation.valueBoolean` (1109, tanpa BQ) |
| 88 | 1130–1141 | Observation | 395264002.0 | Product containing tenofovir | _Obat Hepatitis (Tenofovir)_ → `Observation.valueBoolean` (1133, tanpa BQ) |
| 89 | 1142–1153 | Observation | SP000157 | Obat Diabetes Mellitus | _Obat Diabetes Melitus_ → `Observation.valueBoolean` (1145, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 52 |
| PractitionerRole | 7 |
| ServiceRequest | 6 |
| Specimen | 6 |
| DiagnosticReport | 6 |
| Condition | 3 |
| Immunization | 3 |
| Procedure | 2 |
| Patient | 1 |
| Practitioner | 1 |
| Encounter | 1 |
| EpisodeOfCare | 1 |
| **Total** | **89** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 77 | PractitionerRole | `PractitionerRole.code.coding` | 309453006.0 | Registered midwife | http://snomed.info/sct |
| 2 | 78 | PractitionerRole | `PractitionerRole.code.coding` | 309367003.0 | Obstetrician and gynecologist | http://snomed.info/sct |
| 3 | 79 | PractitionerRole | `PractitionerRole.code.coding` | 309343006.0 | Physician | http://snomed.info/sct |
| 4 | 80 | PractitionerRole | `PractitionerRole.code.coding` | 224535009.0 | Registered nurse | http://snomed.info/sct |
| 5 | 99 | Condition | `Condition.code.coding` | 134435003.0 | Routine antenatal care | http://snomed.info/sct |
| 6 | 116 | EpisodeOfCare | `EpisodeOfCare.type.coding` | ANC | Antenatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 7 | 125 | Observation | `Observation.code.coding` | SP000132 | Memiliki Buku KIA | http://terminology.kemkes.go.id/sp |
| 8 | 138 | Observation | `Observation.code.coding` | 8665-2 | Last menstrual period start date | http://loinc.org |
| 9 | 139 | Observation | `Observation.code.coding` | ANC.B6.DE14 | Last menstrual period (LMP) date | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 10 | 150 | Observation | `Observation.code.coding` | 11778-8 | Delivery date Estimated | http://loinc.org |
| 11 | 151 | Observation | `Observation.code.coding` | ANC.B6.DE22 | Expected date of delivery (EDD) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 12 | 162 | Observation | `Observation.code.coding` | 56077-1 | Body weight --pre current pregnancy | http://loinc.org |
| 13 | 163 | Observation | `Observation.code.coding` | ANC.B8.DE2 | Pre-gestational weight | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 14 | 175 | Observation | `Observation.code.coding` | 8302-2 | Body height | http://loinc.org |
| 15 | 176 | Observation | `Observation.code.coding` | ANC.B8.DE1 | Height | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 16 | 188 | Observation | `Observation.code.coding` | SP000683 | Tatalaksana Tindakan | http://terminology.kemkes.go.id/sp |
| 17 | 199 | Observation | `Observation.code.coding` | SP000684 | Tatalaksana Obat | http://terminology.kemkes.go.id/sp |
| 18 | 210 | Condition | `Condition.code.coding` | 609496007.0 | Complication occurring during pregnancy | http://snomed.info/sct |
| 19 | 219 | Observation | `Observation.code.coding` | OC000010 | Indeks Massa Tubuh Sebelum Hamil | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 20 | 220 | Observation | `Observation.code.coding` | ANC.SS.DE58 | IMT Sebelum Hamil | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 21 | 232 | Immunization | `Immunization.vaccineCode` | VG139 | Td | http://sys-ids.kemkes.go.id/kfa |
| 22 | 249 | Immunization | `Immunization.vaccineCode` | VG139 | Td | http://sys-ids.kemkes.go.id/kfa |
| 23 | 266 | Immunization | `Immunization.vaccineCode` | VG139 | Td | http://sys-ids.kemkes.go.id/kfa |
| 24 | 279 | Observation | `Observation.code.coding` | SP000001 | Skrining Imunisasi Tetanus Toksoid | http://terminology.kemkes.go.id/sp |
| 25 | 280 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 26 | 290 | Observation | `Observation.code.coding` | SP000002 | Kunjungan Pertama Pemeriksaan Kehamilan | http://terminology.kemkes.go.id/sp |
| 27 | 301 | Observation | `Observation.code.coding` | 18185-9 | Gestational age | http://loinc.org |
| 28 | 302 | Observation | `Observation.code.coding` | ANC.B6.DE17 | Gestational age | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 29 | 305 | Observation | `Observation.component.code.coding` | 49052-4 | Gestational age in days | http://terminology.kemkes.go.id/sp |
| 30 | 317 | Observation | `Observation.code.coding` | 32418-6 | Obstetric trimester Stated | http://loinc.org |
| 31 | 318 | Observation | `Observation.code.coding` | ANC.SS.DE13 | Trimester ke | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 32 | 329 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 33 | 330 | Observation | `Observation.code.coding` | ANC.B8.DE3 | Current weight | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 34 | 342 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 35 | 354 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://loinc.org |
| 36 | 366 | Observation | `Observation.code.coding` | 284473002.0 | Mid upper arm circumference | http://snomed.info/sct |
| 37 | 367 | Observation | `Observation.code.coding` | ANC.SS.DE3 | Lingkar Lengan Atas (LILA) | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 38 | 376 | Observation | `Observation.interpretation` | OI000018 | Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 39 | 377 | Observation | `Observation.interpretation` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 40 | 378 | Observation | `Observation.interpretation` | OI000035 | Risiko Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 41 | 381 | Observation | `Observation.code.coding` | 11881-0 | Uterus Fundal height Tape measure | http://loinc.org |
| 42 | 382 | Observation | `Observation.code.coding` | ANC.B8.DE105 | Symphysis-fundal height | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 43 | 385 | Observation | `Observation.dataAbsentReason.coding` | unsupported | Unsupported | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 44 | 396 | Observation | `Observation.code.coding` | 883-9 | ABO group [Type] in Blood | http://loinc.org |
| 45 | 397 | Observation | `Observation.code.coding` | ANC.B9.DE24 | Blood type | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 46 | 398 | Observation | `Observation.valueCodeableConcept.coding` | LA19710-5 | Group A | http://loinc.org |
| 47 | 399 | Observation | `Observation.valueCodeableConcept.coding` | LA19709-7 | Group B | http://loinc.org |
| 48 | 400 | Observation | `Observation.valueCodeableConcept.coding` | LA19708-9 | Group O | http://loinc.org |
| 49 | 401 | Observation | `Observation.valueCodeableConcept.coding` | LA28449-9 | Group AB | http://loinc.org |
| 50 | 411 | Observation | `Observation.code.coding` | 10331-7 | Rh [Type] in Blood | http://loinc.org |
| 51 | 412 | Observation | `Observation.code.coding` | ANC.B9.DE29 | Rh factor | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 52 | 413 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 53 | 414 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 54 | 424 | Observation | `Observation.code.coding` | 55283-6 | Fetal Heart rate | http://loinc.org |
| 55 | 425 | Observation | `Observation.code.coding` | ANC.B8.DE107 | Fetal heart rate | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 56 | 437 | Observation | `Observation.code.coding` | 72155-5 | Position in womb Fetus [RHEA] | http://loinc.org |
| 57 | 438 | Observation | `Observation.code.coding` | ANC.B8.DE111 | Fetal presentation | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 58 | 439 | Observation | `Observation.valueCodeableConcept.coding` | 1209182005.0 | Cephalic fetal presentation | http://snomed.info/sct |
| 59 | 440 | Observation | `Observation.valueCodeableConcept.coding` | SP000005 | Letak Bokong/ Lintang | http://terminology.kemkes.go.id/sp |
| 60 | 441 | Observation | `Observation.valueCodeableConcept.coding` | SP000006 | Organ Tubuh Lainnya | http://terminology.kemkes.go.id/sp |
| 61 | 442 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 62 | 452 | Condition | `Condition.code.coding` | 34842007.0 | Antepartum hemorrhage | http://snomed.info/sct |
| 63 | 453 | Condition | `Condition.code.coding` | 15938005.0 | Eclampsia | http://snomed.info/sct |
| 64 | 454 | Condition | `Condition.code.coding` | 398254007.0 | Pre-eclampsia | http://snomed.info/sct |
| 65 | 455 | Condition | `Condition.code.coding` | 386639001.0 | Termination of pregnancy | http://snomed.info/sct |
| 66 | 456 | Condition | `Condition.code.coding` | 40733004.0 | Infectious disease | http://snomed.info/sct |
| 67 | 457 | Condition | `Condition.code.coding` | 91302008.0 | Sepsis | http://snomed.info/sct |
| 68 | 458 | Condition | `Condition.code.coding` | 609496007.0 | Complication occurring during pregnancy | http://snomed.info/sct |
| 69 | 467 | Observation | `Observation.code.coding` | 268445003.0 | Ultrasound scan - obstetric | http://snomed.info/sct |
| 70 | 468 | Observation | `Observation.valueCodeableConcept.coding` | 169221005.0 | Ultrasound obstetric scan normal | http://snomed.info/sct |
| 71 | 469 | Observation | `Observation.valueCodeableConcept.coding` | 169255008.0 | Ultrasound scan abnormal | http://snomed.info/sct |
| 72 | 471 | Observation | `Observation.dataAbsentReason.coding` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 73 | 481 | Observation | `Observation.code.coding` | 11996-6 | [#] Pregnancies | http://loinc.org |
| 74 | 482 | Observation | `Observation.code.coding` | ANC.B6.DE24 | Number of pregnancies (gravida) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 75 | 493 | Observation | `Observation.code.coding` | 11977-6 | [#] Parity | http://loinc.org |
| 76 | 494 | Observation | `Observation.code.coding` | ANC.B6.DE32 | Parity | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 77 | 505 | Observation | `Observation.code.coding` | 69043-8 | Other pregnancy outcomes # | http://loinc.org |
| 78 | 506 | Observation | `Observation.code.coding` | ANC.B6.DE25 | Number of miscarriages and/or abortions | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 79 | 519 | ServiceRequest | `ServiceRequest.code` | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 80 | 527 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002.0 | Laboratory worker | http://snomed.info/sct |
| 81 | 530 | Specimen | `Specimen.type` | 122555007.0 | Venous blood specimen | http://snomed.info/sct |
| 82 | 539 | Observation | `Observation.code.coding` | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 83 | 540 | Observation | `Observation.code.coding` | ANC.B9.DE32 | HIV test | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 84 | 541 | Observation | `Observation.valueCodeableConcept.coding` | LA15255-5 | Reactive | http://loinc.org |
| 85 | 542 | Observation | `Observation.valueCodeableConcept.coding` | LA15256-3 | Nonreactive | http://loinc.org |
| 86 | 543 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 87 | 553 | DiagnosticReport | `DiagnosticReport.code` | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 88 | 567 | ServiceRequest | `ServiceRequest.code` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 89 | 575 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002.0 | Laboratory worker | http://snomed.info/sct |
| 90 | 578 | Specimen | `Specimen.type` | 122555007.0 | Venous blood specimen | http://snomed.info/sct |
| 91 | 587 | Observation | `Observation.code.coding` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 92 | 588 | Observation | `Observation.code.coding` | ANC.B9.DE60 | Hepatitis B test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 93 | 589 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 94 | 590 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 95 | 591 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 96 | 601 | DiagnosticReport | `DiagnosticReport.code` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 97 | 615 | ServiceRequest | `ServiceRequest.code` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 98 | 623 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002.0 | Laboratory worker | http://snomed.info/sct |
| 99 | 626 | Specimen | `Specimen.type` | 122555007.0 | Venous blood specimen | http://snomed.info/sct |
| 100 | 635 | Observation | `Observation.code.coding` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 101 | 636 | Observation | `Observation.code.coding` | ANC.B9.DE96 | Syphilis test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 102 | 637 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 103 | 638 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 104 | 639 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 105 | 649 | DiagnosticReport | `DiagnosticReport.code` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 106 | 663 | ServiceRequest | `ServiceRequest.code` | 2887-8 | Protein [Presence] in Urine | http://loinc.org |
| 107 | 671 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002.0 | Laboratory worker | http://snomed.info/sct |
| 108 | 674 | Specimen | `Specimen.type` | 122575003.0 | Urine specimen | http://snomed.info/sct |
| 109 | 683 | Observation | `Observation.code.coding` | 2887-8 | Protein [Presence] in Urine | http://loinc.org |
| 110 | 684 | Observation | `Observation.code.coding` | ANC.B9.DE114 | Urine test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 111 | 685 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 112 | 686 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 113 | 687 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 114 | 697 | DiagnosticReport | `DiagnosticReport.code.coding` | 2887-8 | Protein [Presence] in Urine | http://loinc.org |
| 115 | 711 | ServiceRequest | `ServiceRequest.code` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 116 | 719 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002.0 | Laboratory worker | http://snomed.info/sct |
| 117 | 722 | Specimen | `Specimen.type` | 122555007.0 | Venous blood specimen | http://snomed.info/sct |
| 118 | 731 | Observation | `Observation.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 119 | 732 | Observation | `Observation.code.coding` | ANC.B9.DE175 | Blood hemoglobin test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 120 | 735 | Observation | `Observation.interpretation.coding` | 860635002.0 | No anemia present | http://snomed.info/sct |
| 121 | 736 | Observation | `Observation.interpretation.coding` | OI000032 | Anemia ringan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 122 | 737 | Observation | `Observation.interpretation.coding` | OI000033 | Anemia sedang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 123 | 738 | Observation | `Observation.interpretation.coding` | OI000034 | Anemia berat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 124 | 739 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 125 | 749 | DiagnosticReport | `DiagnosticReport.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 126 | 763 | ServiceRequest | `ServiceRequest.code` | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | http://loinc.org |
| 127 | 771 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002.0 | Laboratory worker | http://snomed.info/sct |
| 128 | 774 | Specimen | `Specimen.type` | 122555007.0 | Venous blood specimen | http://snomed.info/sct |
| 129 | 783 | Observation | `Observation.code.coding` | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | http://loinc.org |
| 130 | 784 | Observation | `Observation.code.coding` | ANC.B9.DE159 | Blood glucose test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 131 | 787 | Observation | `Observation.interpretation.coding` | 166921001.0 | Blood glucose normal | http://snomed.info/sct |
| 132 | 788 | Observation | `Observation.interpretation.coding` | 166922008.0 | Blood glucose abnormal | http://snomed.info/sct |
| 133 | 789 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 134 | 799 | DiagnosticReport | `DiagnosticReport.code.coding` | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | http://loinc.org |
| 135 | 811 | Observation | `Observation.code.coding` | SP000007 | Tatalaksana Anemia | http://terminology.kemkes.go.id/sp |
| 136 | 812 | Observation | `Observation.valueCodeableConcept.coding` | SP000008 | Pemberian Tablet Tambah Darah | http://terminology.kemkes.go.id/sp |
| 137 | 813 | Observation | `Observation.valueCodeableConcept.coding` | SP000009 | Pemberian Fe Parenteral | http://terminology.kemkes.go.id/sp |
| 138 | 814 | Observation | `Observation.valueCodeableConcept.coding` | 116859006.0 | Transfusion of blood product | http://snomed.info/sct |
| 139 | 815 | Observation | `Observation.valueCodeableConcept.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 140 | 817 | Observation | `Observation.valueCodeableConcept.coding` | 3457005.0 | Patient referral | http://snomed.info/sct |
| 141 | 828 | Observation | `Observation.code.coding` | SP000010 | Skrining Hipertensi dalam Kehamilan | http://terminology.kemkes.go.id/sp |
| 142 | 829 | Observation | `Observation.valueCodeableConcept.coding` | SP000011 | Tidak Pre Eklampsia/ Eklampsia | http://terminology.kemkes.go.id/sp |
| 143 | 830 | Observation | `Observation.valueCodeableConcept.coding` | 48194001.0 | Pregnancy-induced hypertension | http://snomed.info/sct |
| 144 | 831 | Observation | `Observation.valueCodeableConcept.coding` | 398254007.0 | Pre-eclampsia | http://snomed.info/sct |
| 145 | 832 | Observation | `Observation.valueCodeableConcept.coding` | 15938005.0 | Eclampsia | http://snomed.info/sct |
| 146 | 833 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 147 | 843 | Observation | `Observation.code.coding` | SP000012 | Tatalaksana Pre Eklampsia | http://terminology.kemkes.go.id/sp |
| 148 | 847 | Observation | `Observation.component.code.coding` | 135840009.0 | Blood pressure monitoring | http://snomed.info/sct |
| 149 | 850 | Observation | `Observation.component.code.coding` | 308116003.0 | Antihypertensive therapy | http://snomed.info/sct |
| 150 | 853 | Observation | `Observation.component.code.coding` | SP000013 | Pemberian MgSO4 | http://terminology.kemkes.go.id/sp |
| 151 | 856 | Observation | `Observation.component.code.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 152 | 858 | Observation | `Observation.component.code.coding` | 3457005.0 | Patient referral | http://snomed.info/sct |
| 153 | 862 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 154 | 872 | Observation | `Observation.code.coding` | SP000014 | Tatalaksana KEK | http://terminology.kemkes.go.id/sp |
| 155 | 874 | Observation | `Observation.component.code.coding` | 435591000124104.0 | Nutrition supplement therapy | http://snomed.info/sct |
| 156 | 877 | Observation | `Observation.component.code.coding` | 3457005.0 | Patient referral | http://snomed.info/sct |
| 157 | 889 | Observation | `Observation.code.coding` | SP000015 | Risiko Masalah Kesehatan | http://terminology.kemkes.go.id/sp |
| 158 | 893 | Observation | `Observation.component.code.coding` | 40733004.0 | Infectious disease | http://snomed.info/sct |
| 159 | 896 | Observation | `Observation.component.code.coding` | 73211009.0 | Diabetes mellitus | http://snomed.info/sct |
| 160 | 899 | Observation | `Observation.component.code.coding` | 414916001.0 | Obesity | http://snomed.info/sct |
| 161 | 902 | Observation | `Observation.component.code.coding` | 56717001.0 | Tuberculosis | http://snomed.info/sct |
| 162 | 905 | Observation | `Observation.component.code.coding` | 56265001.0 | Heart disease | http://snomed.info/sct |
| 163 | 908 | Observation | `Observation.component.code.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 164 | 919 | Observation | `Observation.code.coding` | SP000016 | Tatalaksana Masalah Kesehatan | http://terminology.kemkes.go.id/sp |
| 165 | 930 | Procedure | `Procedure.code.coding` | 1230101008.0 | Counseling for pregnancy | http://snomed.info/sct |
| 166 | 941 | Procedure | `Procedure.code.coding` | 385892002.0 | Mental health screening | http://snomed.info/sct |
| 167 | 954 | Observation | `Observation.code.coding` | OC000001 | Jarak kehamilan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 168 | 955 | Observation | `Observation.code.coding` | ANC.SS.DE53 | Jarak kehamilan | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 169 | 967 | Observation | `Observation.code.coding` | 246435002.0 | Number of fetuses | http://snomed.info/sct |
| 170 | 968 | Observation | `Observation.code.coding` | ANC.B8.DE109 | Number of fetuses | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 171 | 979 | Observation | `Observation.code.coding` | 73211009.0 | Diabetes mellitus | http://snomed.info/sct |
| 172 | 991 | Observation | `Observation.code.coding` | 278977008.0 | Human immunodeficiency virus status | http://snomed.info/sct |
| 173 | 992 | Observation | `Observation.valueCodeableConcept.coding` | 165816005.0 | Human immunodeficiency virus detected | http://snomed.info/sct |
| 174 | 993 | Observation | `Observation.valueCodeableConcept.coding` | 165815009.0 | Human immunodeficiency virus not detected | http://snomed.info/sct |
| 175 | 1003 | Observation | `Observation.code.coding` | 66071002.0 | Viral hepatitis type B | http://snomed.info/sct |
| 176 | 1015 | Observation | `Observation.code.coding` | 11258-1 | Hepatitis B virus DNA [Units/volume] in Serum | http://loinc.org |
| 177 | 1027 | Observation | `Observation.code.coding` | 39007-0 | Hepatitis B virus e Ag [Presence] in Specimen | http://loinc.org |
| 178 | 1028 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 179 | 1029 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 180 | 1039 | Observation | `Observation.code.coding` | 76272004.0 | Syphilis | http://snomed.info/sct |
| 181 | 1051 | Observation | `Observation.code.coding` | 61462000.0 | Malaria | http://snomed.info/sct |
| 182 | 1063 | Observation | `Observation.code.coding` | 56717001.0 | Tuberculosis | http://snomed.info/sct |
| 183 | 1075 | Observation | `Observation.code.coding` | SP000046 | Terapi Antiretroviral (ART) | http://terminology.kemkes.go.id/sp |
| 184 | 1087 | Observation | `Observation.code.coding` | SP000124 | Obat anti malaria | http://terminology.kemkes.go.id/sp |
| 185 | 1090 | Observation | `Observation.component.code.coding` | 432555000.0 | Product containing artesunate | http://snomed.info/sct |
| 186 | 1093 | Observation | `Observation.component.code.coding` | 64115004.0 | Product containing amodiaquine | http://snomed.info/sct |
| 187 | 1096 | Observation | `Observation.component.code.coding` | 324919005.0 | Product containing precisely quinine sulfate 200 milligram/1 each conventional release oral tablet | http://snomed.info/sct |
| 188 | 1108 | Observation | `Observation.code.coding` | SP000125 | Obat anti tuberkulosis | http://terminology.kemkes.go.id/sp |
| 189 | 1111 | Observation | `Observation.component.code.coding` | 29175007.0 | Product containing rifampicin | http://snomed.info/sct |
| 190 | 1114 | Observation | `Observation.component.code.coding` | 81335000.0 | Product containing isoniazid | http://snomed.info/sct |
| 191 | 1117 | Observation | `Observation.component.code.coding` | 13592004.0 | Product containing pyrazinamide | http://snomed.info/sct |
| 192 | 1120 | Observation | `Observation.component.code.coding` | 24450004.0 | Product containing ethambutol | http://snomed.info/sct |
| 193 | 1132 | Observation | `Observation.code.coding` | 395264002.0 | Product containing tenofovir | http://snomed.info/sct |
| 194 | 1144 | Observation | `Observation.code.coding` | SP000157 | Obat Diabetes Mellitus | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 70 |
| http://loinc.org | 53 |
| http://terminology.kemkes.go.id/sp | 22 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 21 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 12 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 7 |
| http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes | 4 |
| http://sys-ids.kemkes.go.id/kfa | 3 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 1 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 1 |
| **Total** | **194** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 32 | – | Faskes yang Melayani ANC | Organization | `Organization.name` |
