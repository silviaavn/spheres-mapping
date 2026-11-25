# Output Form: SIM RS Siaga Medika ANC

Sumber: `mapping/phdt-data-dictionary-rs-siaga-medika-anc.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-rs-siaga-medika-anc.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 100 |
| Code (`jumlah code` = 1) | 193 |
| Code unik (code + CodeSystem) | 120 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 12 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–27 | Patient | – | – | _Nama Pasien_ → `Patient.name.text` (2, tanpa BQ)<br>_NIK_ → `Patient.identifier.value` (5, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (7, tanpa BQ)<br>_No Hp_ → `Patient.telecom.value` (10, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (11, tanpa BQ)<br>_Alamat Domisili_ → `Patient.address.use` (12, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (18, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (21, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.extension.valueCode` (24, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.extension.valueCode` (27, tanpa BQ) |
| 2 | 70–73 | PractitionerRole | – | – | _Jabatan_ → `PractitionerRole.code.coding` (72, tanpa BQ) |
| 3 | 74–101 | Practitioner | – | – | _No Ktp Pencatat_ → `Practitioner.identifier.value` (76, tanpa BQ)<br>_Nama Pencatat_ → `Practitioner.name` (78, tanpa BQ)<br>_No Ktp Pemeriksa_ → `Practitioner.identifier.value` (81, tanpa BQ)<br>_Nama Pemeriksa_ → `Practitioner.name` (83, tanpa BQ)<br>_Jenis Kelamin Pemeriksa_ → `Practitioner.gender` (84, tanpa BQ)<br>_Nama Provinsi_ → `Practitioner.address.extension.extension.valueCode` (91, tanpa BQ)<br>_Nama Kabupaten_ → `Practitioner.address.extension.extension.valueCode` (94, tanpa BQ)<br>_Nama Kecamatan_ → `Practitioner.address.extension.extension.valueCode` (97, tanpa BQ)<br>_Nama Desa_ → `Practitioner.address.extension.extension.valueCode` (100, tanpa BQ) |
| 4 | 102–109 | EpisodeOfCare | ANC | Antenatal Care | – |
| 5 | 110–113 | Encounter | – | – | _Tanggal ANC_ → `Encounter.period.start` (110, tanpa BQ) |
| 6 | 114–127 | Observation | 8665-2 | Last menstrual period start date | _HPHT_ → `Observation.valueDateTime` (118, tanpa BQ) |
| 7 | 129–133 | Observation | SP000132 | Memiliki Buku KIA | _Buku KIA_ → `Observation.valueBoolean` (132, tanpa BQ) |
| 8 | 134–148 | Observation | 8302-2 | Body height | _Tinggi Badan_ → `Observation.valueQuantity.value` (138, tanpa BQ) |
| 9 | 149–163 | Observation | 29463-7 | Body weight | _Berat Badan_ → `Observation.valueQuantity.value` (153, tanpa BQ) |
| 10 | 164–181 | Observation | 284473002 | Mid upper arm circumference | _LILA_ → `Observation.valueQuantity.value` (168, tanpa BQ)<br>_Status Gizi KEK/Tidak KEK_ → `Observation.interpretation` (179, tanpa BQ) |
| 11 | 183–197 | Observation | 8480-6 | Systolic blood pressure | _Tekanan Darah Sistol_ → `Observation.valueQuantity.value` (187, tanpa BQ) |
| 12 | 198–212 | Observation | 8462-4 | Diastolic blood pressure | _Tekanan Darah Diastol_ → `Observation.valueQuantity.value` (202, tanpa BQ) |
| 13 | 213–225 | Observation | 289625003 | Finding of fundal height of uterus | _TFU_ → `Observation.valueString` (216, tanpa BQ) |
| 14 | 226–247 | Immunization | – | – | _Status Imunisasi TT_ → `Immunization.status` (226, tanpa BQ) |
| 15 | 248–260 | Immunization | – | – | – |
| 16 | 261–273 | Observation | SP000001 | Skrining Imunisasi Tetanus Toksoid | – |
| 17 | 274–292 | Immunization | – | – | _Imunisasi TT pada Kunjungan Saat Ini_ → `Immunization.status` (274, tanpa BQ) |
| 18 | 293–310 | Condition | 34842007 | Antepartum hemorrhage | _Komplikasi Kehamilan_ → `Condition.clinicalStatus.coding` (293, tanpa BQ) |
| 19 | 311–326 | Observation | 55283-6 | Fetal Heart rate | _DJJ_ → `Observation.valueQuantity.value` (315, tanpa BQ) |
| 20 | 327–344 | Observation | 72155-5 | Position in womb Fetus [RHEA] | _Presentasi_ → `Observation.valueCodeableConcept.coding` (332, tanpa BQ) |
| 21 | 345–356 | Procedure | 88.78 | Diagnostic ultrasound of gravid uterus | _USG_ → `Procedure.category.coding` (345, tanpa BQ) |
| 22 | 357–366 | ServiceRequest | – | – | _USG_GS_ → `ServiceRequest.category` (357, tanpa BQ) |
| 23 | 367–369 | PractitionerRole | – | – | – |
| 24 | 370–383 | Observation | – | – | – |
| 25 | 384–394 | DiagnosticReport | 11850-5 | Gestational sac Mean diameter US | – |
| 26 | 395–404 | ServiceRequest | – | – | _USG_CRL_ → `ServiceRequest.category` (395, tanpa BQ) |
| 27 | 405–407 | PractitionerRole | – | – | – |
| 28 | 408–421 | Observation | – | – | – |
| 29 | 422–432 | DiagnosticReport | 11957-8 | Fetal Crown Rump length US | – |
| 30 | 433–442 | ServiceRequest | – | – | _USG_DJJ_ → `ServiceRequest.category` (433, tanpa BQ) |
| 31 | 443–445 | PractitionerRole | – | – | – |
| 32 | 446–459 | Observation | – | – | – |
| 33 | 460–470 | DiagnosticReport | 11948-7 | Fetal Heart rate US | – |
| 34 | 471–480 | ServiceRequest | – | – | _USG_BPD_ → `ServiceRequest.category` (471, tanpa BQ) |
| 35 | 481–483 | PractitionerRole | – | – | – |
| 36 | 484–496 | Observation | – | – | – |
| 37 | 497–507 | DiagnosticReport | 11820-8 | Fetal Head Diameter.biparietal US | – |
| 38 | 508–517 | ServiceRequest | – | – | _USG_HC_ → `ServiceRequest.category` (508, tanpa BQ) |
| 39 | 518–520 | PractitionerRole | – | – | – |
| 40 | 521–533 | Observation | – | – | – |
| 41 | 534–544 | DiagnosticReport | 11984-2 | Fetal Head Circumference US | – |
| 42 | 545–554 | ServiceRequest | – | – | _USG_SDP_Ketuban_ → `ServiceRequest.category` (545, tanpa BQ) |
| 43 | 555–557 | PractitionerRole | – | – | – |
| 44 | 558–570 | Observation | – | – | – |
| 45 | 571–581 | DiagnosticReport | 11832-3 | Fetal Amniotic fluid space Maximum diameter largest pocket US | – |
| 46 | 582–595 | Observation | 365662002 | Finding of amniotic fluid appearance | _USG_SDP_Ketuban_ → `Observation.valueCodeableConcept.coding` (584, tanpa BQ) |
| 47 | 596–605 | ServiceRequest | – | – | _USG_Letak_Janin_ → `ServiceRequest.category` (596, tanpa BQ) |
| 48 | 606–608 | PractitionerRole | – | – | – |
| 49 | 609–621 | Observation | – | – | – |
| 50 | 622–632 | DiagnosticReport | 72155-5 | Position in womb Fetus [RHEA] | – |
| 51 | 633–642 | ServiceRequest | – | – | _USG_Presentasi_ → `ServiceRequest.category` (633, tanpa BQ) |
| 52 | 643–645 | PractitionerRole | – | – | – |
| 53 | 646–660 | Observation | – | – | – |
| 54 | 661–671 | DiagnosticReport | 11877-8 | Fetal presentation US | – |
| 55 | 672–681 | ServiceRequest | – | – | _Jumlah_Janin_ → `ServiceRequest.category` (672, tanpa BQ) |
| 56 | 682–684 | PractitionerRole | – | – | – |
| 57 | 685–696 | Observation | – | – | – |
| 58 | 697–707 | DiagnosticReport | 11878-6 | Number of fetuses by US | – |
| 59 | 708–724 | Observation | 883-9 | ABO group [Type] in Blood | _Golongan Darah_ → `Observation.valueCodeableConcept.coding` (712, tanpa BQ) |
| 60 | 725–739 | Observation | 10331-7 | Rh [Type] in Blood | _Rhesus_ → `Observation.valueCodeableConcept.coding` (729, tanpa BQ) |
| 61 | 740–749 | ServiceRequest | – | – | _HIV_ → `ServiceRequest.category` (740, tanpa BQ) |
| 62 | 750–753 | PractitionerRole | – | – | – |
| 63 | 754–761 | Specimen | – | – | – |
| 64 | 762–777 | Observation | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | – |
| 65 | 778–789 | DiagnosticReport | – | – | – |
| 66 | 790–799 | ServiceRequest | – | – | _Hepatitis_ → `ServiceRequest.category` (790, tanpa BQ) |
| 67 | 800–803 | PractitionerRole | – | – | – |
| 68 | 804–811 | Specimen | – | – | – |
| 69 | 812–827 | Observation | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | – |
| 70 | 828–839 | DiagnosticReport | – | – | – |
| 71 | 840–849 | ServiceRequest | – | – | _Siphilis_ → `ServiceRequest.category` (840, tanpa BQ) |
| 72 | 850–853 | PractitionerRole | – | – | – |
| 73 | 854–861 | Specimen | – | – | – |
| 74 | 862–877 | Observation | 22464-2 | Reagin Ab [Presence] in Specimen | – |
| 75 | 878–889 | DiagnosticReport | – | – | – |
| 76 | 890–899 | ServiceRequest | – | – | _Protein Urin_ → `ServiceRequest.category` (890, tanpa BQ) |
| 77 | 900–903 | PractitionerRole | – | – | – |
| 78 | 904–911 | Specimen | – | – | – |
| 79 | 912–927 | Observation | 2887-8 | Protein [Presence] in Urine | – |
| 80 | 928–939 | DiagnosticReport | 2887-8 | Protein [Presence] in Urine | – |
| 81 | 940–949 | ServiceRequest | – | – | _Hemoglobin_ → `ServiceRequest.category` (940, tanpa BQ) |
| 82 | 950–953 | PractitionerRole | – | – | – |
| 83 | 954–961 | Specimen | – | – | – |
| 84 | 962–977 | Observation | 718-7 | Hemoglobin [Mass/volume] in Blood | – |
| 85 | 978–989 | DiagnosticReport | 718-7 | Hemoglobin [Mass/volume] in Blood | – |
| 86 | 990–999 | ServiceRequest | – | – | _Gula Darah Sewaktu_ → `ServiceRequest.category` (990, tanpa BQ) |
| 87 | 1000–1003 | PractitionerRole | – | – | – |
| 88 | 1004–1011 | Specimen | – | – | – |
| 89 | 1012–1027 | Observation | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | – |
| 90 | 1028–1039 | DiagnosticReport | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | – |
| 91 | 1040–1056 | Observation | 15220000 | Laboratory test | _Lab Lainnya_ → `Observation.valueCodeableConcept.coding` (1043, tanpa BQ) |
| 92 | 1057–1090 | MedicationRequest | 92000653 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula | _Jumlah Tablet Tambah Darah_ → `MedicationRequest.contained.resourceType` (1057, tanpa BQ) |
| 93 | 1091–1122 | MedicationDispense | 93015491 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | – |
| 94 | 1123–1132 | Observation | SP000007 | Tatalaksana Anemia | _Tata Laksana Anemia_ → `Observation.valueCodeableConcept.coding` (1126, tanpa BQ) |
| 95 | 1134–1159 | Observation | SP000010 | Skrining Hipertensi dalam Kehamilan | _Skrining Pre-Eklampsia_ → `Observation.valueCodeableConcept.coding` (1146, tanpa BQ) |
| 96 | 1160–1168 | Observation | SP000012 | Tatalaksana Pre Eklampsia | _Tata Laksana Pre-Eklampsia_ → `Observation.component.valueString` (1167, tanpa BQ) |
| 97 | 1170–1184 | Observation | SP000014 | Tatalaksana KEK | _Tata Laksana KEK_ → `Observation.valueCodeableConcept.coding` (1183, tanpa BQ) |
| 98 | 1186–1214 | Observation | SP000015 | Risiko Masalah Kesehatan | _Risiko Kesehatan Lain_ → `Observation.status` (1196, tanpa BQ) |
| 99 | 1215–1219 | Procedure | 385892002 | Mental health screening | _Skrinning Keswa_ → `Procedure.category.coding` (1215, tanpa BQ) |
| 100 | 1220–1228 | Observation | – | – | – |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 36 |
| PractitionerRole | 16 |
| ServiceRequest | 15 |
| DiagnosticReport | 15 |
| Specimen | 6 |
| Immunization | 3 |
| Procedure | 2 |
| Patient | 1 |
| Practitioner | 1 |
| EpisodeOfCare | 1 |
| Encounter | 1 |
| Condition | 1 |
| MedicationRequest | 1 |
| MedicationDispense | 1 |
| **Total** | **100** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 72 | PractitionerRole | `PractitionerRole.code.coding` | 309453006 | Registered midwife | http://snomed.info/sct |
| 2 | 106 | EpisodeOfCare | `EpisodeOfCare.type.coding` | ANC | Antenatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 3 | 116 | Observation | `Observation.code.coding` | 8665-2 | Last menstrual period start date | http://loinc.org |
| 4 | 117 | Observation | `Observation.code.coding` | ANC.B6.DE14 | Last menstrual period (LMP) date | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 5 | 131 | Observation | `Observation.code.coding` | SP000132 | Memiliki Buku KIA | http://terminology.kemkes.go.id/sp |
| 6 | 136 | Observation | `Observation.code.coding` | 8302-2 | Body height | http://loinc.org |
| 7 | 137 | Observation | `Observation.code.coding` | ANC.B8.DE1 | Height | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 8 | 151 | Observation | `Observation.code.coding` | 29463-7 | Body weight |  |
| 9 | 152 | Observation | `Observation.code.coding` | ANC.B8.DE3 | Current weight |  |
| 10 | 166 | Observation | `Observation.code.coding` | 284473002 | Mid upper arm circumference | http://snomed.info/sct |
| 11 | 167 | Observation | `Observation.code.coding` | ANC.SS.DE3 | Lingkar Lengan Atas (LILA) | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 12 | 179 | Observation | `Observation.interpretation` | OI000018 | Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 13 | 180 | Observation | `Observation.interpretation` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 14 | 181 | Observation | `Observation.interpretation` | OI000035 | Risiko Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 15 | 185 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 16 | 186 | Observation | `Observation.code.coding` | ANC.B8.DE17 | Systolic blood pressure | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 17 | 200 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://loinc.org |
| 18 | 201 | Observation | `Observation.code.coding` | ANC.B8.DE19 | Diastolic blood pressure | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 19 | 215 | Observation | `Observation.code.coding` | 289625003 | Finding of fundal height of uterus | http://snomed.info/sct |
| 20 | 228 | Immunization | `Immunization.vaccineCode` | VG139 | Td | http://sys-ids.kemkes.go.id/kfa |
| 21 | 248 | Immunization | `Immunization.vaccineCode` | VG139 | Td | http://sys-ids.kemkes.go.id/kfa |
| 22 | 263 | Observation | `Observation.code.coding` | SP000001 | Skrining Imunisasi Tetanus Toksoid | http://terminology.kemkes.go.id/sp |
| 23 | 264 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 24 | 276 | Immunization | `Immunization.vaccineCode` | VG139 | Td | http://sys-ids.kemkes.go.id/kfa |
| 25 | 295 | Condition | `Condition.code.coding` | 34842007 | Antepartum hemorrhage | http://snomed.info/sct |
| 26 | 296 | Condition | `Condition.code.coding` | 15938005 | Eclampsia | http://snomed.info/sct |
| 27 | 297 | Condition | `Condition.code.coding` | 398254007 | Pre-eclampsia | http://snomed.info/sct |
| 28 | 298 | Condition | `Condition.code.coding` | 386639001 | Termination of pregnancy | http://snomed.info/sct |
| 29 | 299 | Condition | `Condition.code.coding` | 40733004 | Infectious disease | http://snomed.info/sct |
| 30 | 300 | Condition | `Condition.code.coding` | 91302008 | Sepsis | http://snomed.info/sct |
| 31 | 301 | Condition | `Condition.code.coding` | 74964007 | Other | http://snomed.info/sct |
| 32 | 313 | Observation | `Observation.code.coding` | 55283-6 | Fetal Heart rate | http://loinc.org |
| 33 | 314 | Observation | `Observation.code.coding` | ANC.B8.DE107 | Fetal heart rate | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 34 | 329 | Observation | `Observation.code.coding` | 72155-5 | Position in womb Fetus [RHEA] | http://loinc.org |
| 35 | 330 | Observation | `Observation.code.coding` | ANC.B8.DE111 | Fetal presentation | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 36 | 332 | Observation | `Observation.valueCodeableConcept.coding` | 1209182005 | Cephalic fetal presentation | http://snomed.info/sct |
| 37 | 333 | Observation | `Observation.valueCodeableConcept.coding` | 288203005 | Transverse/oblique lie | http://snomed.info/sct |
| 38 | 334 | Observation | `Observation.valueCodeableConcept.coding` | 6096002 | Breech presentation | http://snomed.info/sct |
| 39 | 335 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 40 | 346 | Procedure | `Procedure.code.coding` | 88.78 | Diagnostic ultrasound of gravid uterus | http://hl7.org/fhir/sid/icd-9-cm |
| 41 | 361 | ServiceRequest | `ServiceRequest.code` | 11850-5 | Gestational sac Mean diameter US | http://loinc.org |
| 42 | 368 | PractitionerRole | `PractitionerRole.code.coding` | 66862007 | Radiologist | http://snomed.info/sct |
| 43 | 372 | Observation | `Observation.code.coding[x]` | 11850-5 | Gestational sac Mean diameter US | http://loinc.org |
| 44 | 373 | Observation | `Observation.code.coding[x]` | ANC.SS.DE36 | Gestational sac (GS) USG | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 45 | 386 | DiagnosticReport | `DiagnosticReport.code.coding` | 11850-5 | Gestational sac Mean diameter US | http://loinc.org |
| 46 | 399 | ServiceRequest | `ServiceRequest.code` | 11525-3 | US for pregnancy | http://loinc.org |
| 47 | 406 | PractitionerRole | `PractitionerRole.code.coding` | 66862007 | Radiologist | http://snomed.info/sct |
| 48 | 410 | Observation | `Observation.code.coding[x]` | 11957-8 | Fetal Crown Rump length US | http://loinc.org |
| 49 | 411 | Observation | `Observation.code.coding[x]` | ANC.SS.DE37 | Fetal Crown Rump Length (CRL) USG | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 50 | 424 | DiagnosticReport | `DiagnosticReport.code.coding` | 11957-8 | Fetal Crown Rump length US | http://loinc.org |
| 51 | 437 | ServiceRequest | `ServiceRequest.code` | 11525-3 | US for pregnancy | http://loinc.org |
| 52 | 444 | PractitionerRole | `PractitionerRole.code.coding` | 66862007 | Radiologist | http://snomed.info/sct |
| 53 | 448 | Observation | `Observation.code.coding[x]` | 11948-7 | Fetal Heart rate US | http://loinc.org |
| 54 | 449 | Observation | `Observation.code.coding[x]` | ANC.SS.DE38 | Denyut Jantung Janin (DJJ) USG |  |
| 55 | 462 | DiagnosticReport | `DiagnosticReport.code.coding` | 11948-7 | Fetal Heart rate US | http://loinc.org |
| 56 | 475 | ServiceRequest | `ServiceRequest.code` | 11525-3 | US for pregnancy | http://loinc.org |
| 57 | 482 | PractitionerRole | `PractitionerRole.code.coding` | 66862007 | Radiologist | http://snomed.info/sct |
| 58 | 486 | Observation | `Observation.code.coding[x]` | 11820-8 | Fetal Head Diameter.biparietal US | http://loinc.org |
| 59 | 499 | DiagnosticReport | `DiagnosticReport.code.coding` | 11820-8 | Fetal Head Diameter.biparietal US | http://loinc.org |
| 60 | 512 | ServiceRequest | `ServiceRequest.code` | 11525-3 | US for pregnancy | http://loinc.org |
| 61 | 519 | PractitionerRole | `PractitionerRole.code.coding` | 66862007 | Radiologist | http://snomed.info/sct |
| 62 | 523 | Observation | `Observation.code.coding[x]` | 11984-2 | Fetal Head Circumference US | http://loinc.org |
| 63 | 536 | DiagnosticReport | `DiagnosticReport.code.coding` | 11984-2 | Fetal Head Circumference US | http://loinc.org |
| 64 | 549 | ServiceRequest | `ServiceRequest.code` | 11525-3 | US for pregnancy | http://loinc.org |
| 65 | 556 | PractitionerRole | `PractitionerRole.code.coding` | 66862007 | Radiologist | http://snomed.info/sct |
| 66 | 560 | Observation | `Observation.code.coding[x]` | 11832-3 | Fetal Amniotic fluid space Maximum diameter largest pocket US | http://loinc.org |
| 67 | 573 | DiagnosticReport | `DiagnosticReport.code.coding` | 11832-3 | Fetal Amniotic fluid space Maximum diameter largest pocket US | http://loinc.org |
| 68 | 583 | Observation | `Observation.code.coding` | 365662002 | Finding of amniotic fluid appearance | http://snomed.info/sct |
| 69 | 584 | Observation | `Observation.valueCodeableConcept.coding` | 168090003 | Amniotic fluid clear | http://snomed.info/sct |
| 70 | 585 | Observation | `Observation.valueCodeableConcept.coding` | 408781009 | Straw colored amniotic fluid | http://snomed.info/sct |
| 71 | 586 | Observation | `Observation.valueCodeableConcept.coding` | 249134008 | Bloodstained liquor | http://snomed.info/sct |
| 72 | 587 | Observation | `Observation.valueCodeableConcept.coding` | 168092006 | Amniotic fluid -meconium stain | http://snomed.info/sct |
| 73 | 600 | ServiceRequest | `ServiceRequest.code` | 11525-3 | US for pregnancy | http://snomed.info/sct |
| 74 | 607 | PractitionerRole | `PractitionerRole.code.coding` | 66862007 | Radiologist | http://snomed.info/sct |
| 75 | 611 | Observation | `Observation.code.coding[x]` | 271692001 | Presentation of fetus | http://snomed.info/sct |
| 76 | 612 | Observation | `Observation.code.coding[x]` | ANC.SS.DE41 | Letak Janin USG | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 77 | 613 | Observation | `Observation.valueCodeableConcept[0].coding[0]` | 398236008 | Intrauterine | http://snomed.info/sct |
| 78 | 614 | Observation | `Observation.valueCodeableConcept[0].coding[0]` | 298109001 | Ectopic | http://snomed.info/sct |
| 79 | 624 | DiagnosticReport | `DiagnosticReport.code.coding` | 72155-5 | Position in womb Fetus [RHEA] | http://snomed.info/sct |
| 80 | 637 | ServiceRequest | `ServiceRequest.code` | 11525-3 | US for pregnancy | http://snomed.info/sct |
| 81 | 644 | PractitionerRole | `PractitionerRole.code.coding` | 66862007 | Radiologist | http://snomed.info/sct |
| 82 | 648 | Observation | `Observation.code.coding[x]` | 11877-8 | Fetal presentation US | http://loinc.org |
| 83 | 649 | Observation | `Observation.code.coding[x]` | ANC.B8.DE111 | Fetal presentation | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 84 | 650 | Observation | `Observation.valueCodeableConcept.coding` | 1209182005 | Cephalic fetal presentation | http://snomed.info/sct |
| 85 | 651 | Observation | `Observation.valueCodeableConcept.coding` | 6096002 | Breech presentation | http://snomed.info/sct |
| 86 | 652 | Observation | `Observation.valueCodeableConcept.coding` | SP000006 | Organ Tubuh Lainnya | http://terminology.kemkes.go.id/sp |
| 87 | 653 | Observation | `Observation.valueCodeableConcept.coding` | 260415000 | Not detected | http://snomed.info/sct |
| 88 | 663 | DiagnosticReport | `DiagnosticReport.code.coding` | 11877-8 | Fetal presentation US | http://loinc.org |
| 89 | 676 | ServiceRequest | `ServiceRequest.code` | 11525-3 | US for pregnancy | http://loinc.org |
| 90 | 683 | PractitionerRole | `PractitionerRole.code.coding` | 66862007 | Radiologist | http://snomed.info/sct |
| 91 | 687 | Observation | `Observation.code.coding[x]` | 11878-6 | Number of fetuses by US | http://loinc.org |
| 92 | 688 | Observation | `Observation.code.coding[x]` | ANC.B8.DE109 | Number of fetuses | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 93 | 699 | DiagnosticReport | `DiagnosticReport.code.coding` | 11878-6 | Number of fetuses by US | http://loinc.org |
| 94 | 710 | Observation | `Observation.code.coding` | 883-9 | ABO group [Type] in Blood | http://loinc.org |
| 95 | 711 | Observation | `Observation.code.coding` | ANC.B9.DE24 | Blood type | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 96 | 712 | Observation | `Observation.valueCodeableConcept.coding` | LA19710-5 | Group A | http://loinc.org |
| 97 | 713 | Observation | `Observation.valueCodeableConcept.coding` | LA19709-7 | Group B | http://loinc.org |
| 98 | 714 | Observation | `Observation.valueCodeableConcept.coding` | LA19708-9 | Group O | http://loinc.org |
| 99 | 715 | Observation | `Observation.valueCodeableConcept.coding` | LA28449-9 | Group AB | http://loinc.org |
| 100 | 727 | Observation | `Observation.code.coding` | 10331-7 | Rh [Type] in Blood | http://loinc.org |
| 101 | 728 | Observation | `Observation.code.coding` | ANC.B9.DE29 | Rh factor | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 102 | 729 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 103 | 730 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 104 | 744 | ServiceRequest | `ServiceRequest.code` | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 105 | 752 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002 | Laboratory worker | http://snomed.info/sct |
| 106 | 755 | Specimen | `Specimen.type` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 107 | 764 | Observation | `Observation.code.coding` | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 108 | 765 | Observation | `Observation.code.coding` | ANC.B9.DE32 | HIV test | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 109 | 766 | Observation | `Observation.valueCodeableConcept.coding` | LA15255-5 | Reactive | http://loinc.org |
| 110 | 767 | Observation | `Observation.valueCodeableConcept.coding` | LA15256-3 | Nonreactive | http://loinc.org |
| 111 | 768 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 112 | 780 | DiagnosticReport | `DiagnosticReport.code` | 68961-2 |  |  |
| 113 | 794 | ServiceRequest | `ServiceRequest.code` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 114 | 802 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002 | Laboratory worker | http://snomed.info/sct |
| 115 | 805 | Specimen | `Specimen.type` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 116 | 814 | Observation | `Observation.code.coding` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 117 | 815 | Observation | `Observation.code.coding` | ANC.B9.DE60 | Hepatitis B test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 118 | 816 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 119 | 817 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 120 | 818 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 121 | 830 | DiagnosticReport | `DiagnosticReport.code` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 122 | 844 | ServiceRequest | `ServiceRequest.code` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 123 | 852 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002 | Laboratory worker | http://snomed.info/sct |
| 124 | 855 | Specimen | `Specimen.type` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 125 | 864 | Observation | `Observation.code.coding` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 126 | 865 | Observation | `Observation.code.coding` | ANC.B9.DE96 | Syphilis test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 127 | 866 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 128 | 867 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 129 | 868 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 130 | 880 | DiagnosticReport | `DiagnosticReport.code` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 131 | 894 | ServiceRequest | `ServiceRequest.code` | 2887-8 | Protein [Presence] in Urine | http://loinc.org |
| 132 | 902 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002 | Laboratory worker | http://snomed.info/sct |
| 133 | 905 | Specimen | `Specimen.type` | 122575003 | Urine specimen | http://snomed.info/sct |
| 134 | 914 | Observation | `Observation.code.coding` | 2887-8 | Protein [Presence] in Urine | http://loinc.org |
| 135 | 915 | Observation | `Observation.code.coding` | ANC.B9.DE114 | Urine test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 136 | 916 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 137 | 917 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 138 | 918 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 139 | 930 | DiagnosticReport | `DiagnosticReport.code.coding` | 2887-8 | Protein [Presence] in Urine | http://loinc.org |
| 140 | 944 | ServiceRequest | `ServiceRequest.code` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 141 | 952 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002 | Laboratory worker | http://snomed.info/sct |
| 142 | 955 | Specimen | `Specimen.type` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 143 | 964 | Observation | `Observation.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 144 | 965 | Observation | `Observation.code.coding` | ANC.B9.DE175 | Blood hemoglobin test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 145 | 968 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 146 | 980 | DiagnosticReport | `DiagnosticReport.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 147 | 994 | ServiceRequest | `ServiceRequest.code` | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | http://loinc.org |
| 148 | 1002 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002 | Laboratory worker | http://snomed.info/sct |
| 149 | 1005 | Specimen | `Specimen.type` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 150 | 1014 | Observation | `Observation.code.coding` | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | http://loinc.org |
| 151 | 1015 | Observation | `Observation.code.coding` | ANC.B9.DE159 | Blood glucose test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 152 | 1018 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 153 | 1030 | DiagnosticReport | `DiagnosticReport.code.coding` | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | http://loinc.org |
| 154 | 1042 | Observation | `Observation.code.coding` | 15220000 | Laboratory test | http://snomed.info/sct |
| 155 | 1043 | Observation | `Observation.valueCodeableConcept.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 156 | 1044 | Observation | `Observation.valueCodeableConcept.coding` | 76772-3 | Plasmodium falciparum Ag [Presence] in Blood by Rapid immunoassay | http://loinc.org |
| 157 | 1045 | Observation | `Observation.valueCodeableConcept.coding` | 104742-2 | Ova and parasites identified in Specimen | http://loinc.org |
| 158 | 1046 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 159 | 1060 | MedicationRequest | `MedicationRequest.contained.code.coding` | 92000653 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula | http://sys-ids.kemkes.go.id/kf |
| 160 | 1094 | MedicationDispense | `MedicationDispense.contained.code.coding` | 93015491 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | http://sys-ids.kemkes.go.id/kf |
| 161 | 1125 | Observation | `Observation.code.coding` | SP000007 | Tatalaksana Anemia | http://terminology.kemkes.go.id/sp |
| 162 | 1126 | Observation | `Observation.valueCodeableConcept.coding` | SP000008 | Pemberian Tablet Tambah Darah | http://terminology.kemkes.go.id/sp |
| 163 | 1127 | Observation | `Observation.valueCodeableConcept.coding` | SP000009 | Pemberian Fe Parenteral | http://terminology.kemkes.go.id/sp |
| 164 | 1128 | Observation | `Observation.valueCodeableConcept.coding` | 116859006 | Transfusion of blood product | http://snomed.info/sct |
| 165 | 1129 | Observation | `Observation.valueCodeableConcept.coding` | 438791000124102 | Vitamin C supplement therapy | http://snomed.info/sct |
| 166 | 1130 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 167 | 1132 | Observation | `Observation.valueCodeableConcept.coding` | 3457005 | Patient referral | http://snomed.info/sct |
| 168 | 1145 | Observation | `Observation.code.coding` | SP000010 | Skrining Hipertensi dalam Kehamilan | http://terminology.kemkes.go.id/sp |
| 169 | 1146 | Observation | `Observation.valueCodeableConcept.coding` | SP000011 | Tidak Pre Eklampsia/ Eklampsia | http://terminology.kemkes.go.id/sp |
| 170 | 1147 | Observation | `Observation.valueCodeableConcept.coding` | 48194001 | Pregnancy-induced hypertension | http://snomed.info/sct |
| 171 | 1148 | Observation | `Observation.valueCodeableConcept.coding` | 398254007 | Pre-eclampsia | http://snomed.info/sct |
| 172 | 1149 | Observation | `Observation.valueCodeableConcept.coding` | 15938005 | Eclampsia | http://snomed.info/sct |
| 173 | 1150 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 174 | 1162 | Observation | `Observation.code.coding` | SP000012 | Tatalaksana Pre Eklampsia | http://terminology.kemkes.go.id/sp |
| 175 | 1163 | Observation | `Observation.component.code.coding` | 135840009 | Blood pressure monitoring | http://snomed.info/sct |
| 176 | 1164 | Observation | `Observation.component.code.coding` | 308116003 | Antihypertensive therapy | http://snomed.info/sct |
| 177 | 1165 | Observation | `Observation.component.code.coding` | SP000013 | Pemberian MgSO4 | http://terminology.kemkes.go.id/sp |
| 178 | 1166 | Observation | `Observation.component.code.coding` | 74964007 | Other | http://snomed.info/sct |
| 179 | 1168 | Observation | `Observation.component.code.coding` | 3457005 | Patient referral | http://snomed.info/sct |
| 180 | 1170 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 181 | 1182 | Observation | `Observation.code.coding` | SP000014 | Tatalaksana KEK | http://terminology.kemkes.go.id/sp |
| 182 | 1183 | Observation | `Observation.valueCodeableConcept.coding` | 435591000124104 | Nutrition supplement therapy | http://snomed.info/sct |
| 183 | 1184 | Observation | `Observation.valueCodeableConcept.coding` | 3457005 | Patient referral | http://snomed.info/sct |
| 184 | 1186 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed |  |
| 185 | 1198 | Observation | `Observation.code.coding` | SP000015 | Risiko Masalah Kesehatan | http://terminology.kemkes.go.id/sp |
| 186 | 1199 | Observation | `Observation.component.code.coding` | 40733004 | Infectious disease | http://snomed.info/sct |
| 187 | 1200 | Observation | `Observation.component.code.coding` | 73211009 | Diabetes mellitus | http://snomed.info/sct |
| 188 | 1201 | Observation | `Observation.component.code.coding` | 414916001 | Obesity | http://snomed.info/sct |
| 189 | 1202 | Observation | `Observation.component.code.coding` | 56717001 | Tuberculosis | http://snomed.info/sct |
| 190 | 1203 | Observation | `Observation.component.code.coding` | 56265001 | Heart disease | http://snomed.info/sct |
| 191 | 1204 | Observation | `Observation.component.code.coding` | 74964007 | Other | http://snomed.info/sct |
| 192 | 1205 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed |  |
| 193 | 1216 | Procedure | `Procedure.code.coding` | 385892002 | Mental health screening | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 70 |
| http://loinc.org | 65 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 17 |
| http://terminology.kemkes.go.id/sp | 12 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 10 |
|  | 6 |
| http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes | 3 |
| http://sys-ids.kemkes.go.id/kfa | 3 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 2 |
| http://sys-ids.kemkes.go.id/kf | 2 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 1 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 1 |
| http://hl7.org/fhir/sid/icd-9-cm | 1 |
| **Total** | **193** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 30 | – | Jenis Fasilitas | Organization | `Organization.type` |
| 31 | – | Nama Faskes | Organization | `Organization.name` |
| 35 | – | Nama Provinsi | Organization | `Organization.address.extension.extension.url` |
| 38 | – | Nama Kabupaten | Organization | `Organization.address.extension.extension.url` |
| 41 | – | Nama Kecamatan | Organization | `Organization.address.extension.extension.url` |
| 44 | – | Nama Desa | Organization | `Organization.address.extension.extension.url` |
| 46 | – | Tempat Pelayanan ANC | Location | `Location.identifier` |
| 54 | – | Nama Provinsi | Location | `Location.address.extension.extension.url` |
| 57 | – | Nama Kabupaten | Location | `Location.address.extension.extension.url` |
| 60 | – | Nama Kecamatan | Location | `Location.address.extension.extension.url` |
| 63 | – | Nama Desa | Location | `Location.address.extension.extension.url` |
| 182 | – | Tekanan Darah | – | `` |
