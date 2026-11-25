# Output Form: ePuskesmas Kunjungan Ibu Hamil

Sumber: `mapping/phdt-data-dictionary-epus-kunjungan-ibu-hamil.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-epus-kunjungan-ibu-hamil.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 114 |
| Code (`jumlah code` = 1) | 206 |
| Code unik (code + CodeSystem) | 111 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 11 |
| Variabel BQ (unik) | 0 |
| Variabel raw (variabel dictionary; belum ada file mentah) | 68 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–6 | Encounter | – | – | _No_ → `Encounter.identifier` (2, tanpa BQ)<br>_Register Kunjungan_ → `Encounter.identifier.value` (4, tanpa BQ)<br>_Tanggal_ → `Encounter.period.start` (6, tanpa BQ)<br>_Faskes Asal_ → `Encounter.hospitaliz ation.admitSource.co ding` (65, tanpa BQ)<br>_Keadaan Pulang_ → `Encounter.hospitalization.dischargeDisposition` (1231, tanpa BQ) |
| 2 | 7–16 | Patient | – | – | _NIK_ → `Patient.identifier.value` (9, tanpa BQ)<br>_No Ibu_ → `Patient.identifier.value` (12, tanpa BQ)<br>_Nama Ibu_ → `Patient.name` (13, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (14, tanpa BQ)<br>_No Telp_ → `Patient.telecom` (15, tanpa BQ)<br>_Alamat_ → `Patient.address.line` (16, tanpa BQ) |
| 3 | 17–23 | Coverage | – | – | _Jamkesmas_ → `Coverage.subscriberId` (17, tanpa BQ) |
| 4 | 24–41 | Observation | 424144002 | Current chronological age | _Umur_ → `Observation.valueQuantity.value` (27, tanpa BQ) |
| 5 | 42–45 | Observation | 8665-2 | Last menstrual period start date | _Tanggal HPHT_ → `Observation.valueDateTime` (45, tanpa BQ) |
| 6 | 46–56 | Observation | 11778-8 | Delivery date Estimated | _Taksiran Persalinan_ → `Observation.valueDateTime` (49, tanpa BQ) |
| 7 | 57–60 | Observation | 18185-9 | Gestational age | _Usia Kehamilan_ → `Observation.valueQuantity.value` (60, tanpa BQ) |
| 8 | 61–64 | Observation | 32418-6 | Obstetric trimester Stated | _Trisemester ke-_ → `Observation.valueInteger` (64, tanpa BQ) |
| 9 | 66–68 | Condition | – | – | _Anamnesis_ → `Condition.category.coding` (66, tanpa BQ) |
| 10 | 71–75 | Observation | 29463-7 | Body weight | _BB(kg)_ → `Observation.category[i].coding[i]` (71, tanpa BQ) |
| 11 | 76–80 | Observation | 8302-2 | Body height | _Tinggi Badan_ → `Observation.category[i].coding[i]` (76, tanpa BQ) |
| 12 | 81–85 | Observation | 8480-6 | Systolic blood pressure | _TD(mmHg)_ → `Observation.category[i].coding[i]` (81, tanpa BQ) |
| 13 | 86–90 | Observation | 8462-4 | Diastolic blood pressure | – |
| 14 | 91–95 | Observation | 284473002 | Mid upper arm circumference | _LILA(cm)_ → `Observation.valueQuantity.value` (94, tanpa BQ) |
| 15 | 96–99 | Observation | – | – | _Status Gizi2)_ → `Observation.category.coding` (96, tanpa BQ) |
| 16 | 100–104 | Observation | 11881-0 | Uterus Fundal height Tape measure | _TFU(cm)_ → `Observation.valueQuantity.value` (103, tanpa BQ) |
| 17 | 105–108 | Observation | 32392-3 | Deep tendon reflex of Patellar | _Refleks Patella(+/-)_ → `Observation.valueCodeableConcept.coding` (107, tanpa BQ) |
| 18 | 109–115 | Observation | 55283-6 | Fetal Heart rate | _DJJ(x/menit)_ → `Observation.valueQuantity.value` (113, tanpa BQ)<br>_Kepala thd PAP3)_ → `Observation.category.coding` (115, tanpa BQ) |
| 19 | 116–120 | Observation | 249111004 | Engagement of head | _TBJ(gr)_ → `Observation.category.coding` (120, tanpa BQ) |
| 20 | 121–125 | Observation | 89087-1 | Fetal Body weight Estimated | _Presentasi4)_ → `Observation.category.coding` (125, tanpa BQ) |
| 21 | 126–131 | Observation | 72155-5 | Position in womb Fetus [RHEA] | – |
| 22 | 132–136 | Observation | 55283-6 | Fetal Heart rate | _DJJ(x/menit)_ → `Observation.valueQuantity.value` (134, tanpa BQ)<br>_Kepala thd PAP3)_ → `Observation.category.coding` (136, tanpa BQ) |
| 23 | 137–141 | Observation | 249111004 | Engagement of head | _TBJ(gr)_ → `Observation.category.coding` (141, tanpa BQ) |
| 24 | 142–146 | Observation | 89087-1 | Fetal Body weight Estimated | _Presentasi4)_ → `Observation.category.coding` (146, tanpa BQ) |
| 25 | 147–151 | Observation | 72155-5 | Position in womb Fetus [RHEA] | _Jumlah Janin_ → `Observation.category.coding` (151, tanpa BQ) |
| 26 | 152–156 | Observation | 246435002 | Number of fetuses | – |
| 27 | 157–167 | Observation | 246435002 | Number of fetuses | – |
| 28 | 168–178 | Procedure | 1230101008 | Counseling for pregnancy | _Konseling_ → `Procedure.category.coding` (168, tanpa BQ) |
| 29 | 179–196 | Immunization | – | – | _Status Imunasi TT_ → `Immunization.status` (179, tanpa BQ)<br>_Injeksi TT_ → `Immunization.status` (195, tanpa BQ) |
| 30 | 197–210 | Immunization | – | – | – |
| 31 | 211–221 | Procedure | 99.38 | Administration of tetanus toxoid | – |
| 32 | 222–233 | Observation | SP000122 | Catat di Buku KIA | _Catat dibuku KIA_ → `Observation.valueBoolean` (224, tanpa BQ) |
| 33 | 234–267 | MedicationRequest | 92000653 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula | _Fe(Tab/Botol)_ → `MedicationRequest.contained.resourceType` (234, tanpa BQ) |
| 34 | 268–299 | MedicationDispense | 93015491 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | – |
| 35 | 300–309 | ServiceRequest | – | – | _Dilakukan*_ → `ServiceRequest.category` (300, tanpa BQ)<br>_Hasil(gr/dl)_ → `ServiceRequest.performer.reference` (309, tanpa BQ) |
| 36 | 313–320 | Specimen | – | – | – |
| 37 | 321–334 | Observation | 718-7 | Hemoglobin [Mass/volume] in Blood | – |
| 38 | 335–346 | DiagnosticReport | 718-7 | Hemoglobin [Mass/volume] in Blood | – |
| 39 | 347–356 | ServiceRequest | – | – | _Protein Uria (+/-)_ → `ServiceRequest.category` (347, tanpa BQ) |
| 40 | 360–367 | Specimen | – | – | – |
| 41 | 368–384 | Observation | 2887-8 | Protein [Presence] in Urine | – |
| 42 | 385–396 | DiagnosticReport | 2887-8 | Protein [Presence] in Urine | – |
| 43 | 397–406 | ServiceRequest | – | – | _Gula Darah_ → `ServiceRequest.category` (397, tanpa BQ) |
| 44 | 410–417 | Specimen | – | – | – |
| 45 | 418–433 | Observation | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | – |
| 46 | 434–445 | DiagnosticReport | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | – |
| 47 | 446–455 | ServiceRequest | – | – | _Sifilis(+/-)_ → `ServiceRequest.category` (446, tanpa BQ) |
| 48 | 460–467 | Specimen | – | – | – |
| 49 | 468–483 | Observation | 22464-2 | Reagin Ab [Presence] in Specimen | – |
| 50 | 484–495 | DiagnosticReport | – | – | – |
| 51 | 496–505 | ServiceRequest | – | – | _HBsAg(+/-)_ → `ServiceRequest.category` (496, tanpa BQ) |
| 52 | 509–516 | Specimen | – | – | – |
| 53 | 517–531 | Observation | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | – |
| 54 | 532–543 | DiagnosticReport | – | – | – |
| 55 | 544–553 | ServiceRequest | – | – | _Thalasemia(+/-)_ → `ServiceRequest.category` (544, tanpa BQ) |
| 56 | 557–564 | Specimen | – | – | – |
| 57 | 565–569 | Observation | SP000115 | Pemeriksaan Laboratorium Thalassemia | – |
| 58 | 570–581 | DiagnosticReport | – | – | – |
| 59 | 582–591 | ServiceRequest | – | – | _Anemia(+/-)_ → `ServiceRequest.category` (582, tanpa BQ) |
| 60 | 595–602 | Specimen | – | – | – |
| 61 | 603–607 | Observation | 718-7 | Hemoglobin [Mass/volume] in Blood | – |
| 62 | 608–619 | DiagnosticReport | – | – | – |
| 63 | 620–631 | Observation | 278977008 | Human immunodeficiency virus status | _Datang dengan HIV(+/-)_ → `Observation.valueCodeableConcept.coding` (623, tanpa BQ) |
| 64 | 632–641 | Procedure | TK000016 | Edukasi Tes HIV | _Ditawarkan Tes_ → `Procedure.category.coding` (632, tanpa BQ) |
| 65 | 642–652 | ServiceRequest | – | – | _Dilakukan Tes_ → `ServiceRequest.category` (642, tanpa BQ) |
| 66 | 656–663 | Specimen | – | – | – |
| 67 | 664–676 | Observation | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | _Hasil Tes HIV(+/-)_ → `Observation.valueCodeableConcept.coding` (668, tanpa BQ) |
| 68 | 677–688 | DiagnosticReport | – | – | – |
| 69 | 689–699 | Procedure | SP000046 | Terapi Antiretroviral (ART) | _Mendapatkan ART_ → `Procedure.category.coding` (689, tanpa BQ) |
| 70 | 700–711 | Observation | 57071-3 | Obstetric delivery method | _Persalinan Pervaginaan4)_ → `Observation.valueCodeableConcept.coding` (702, tanpa BQ)<br>_Persalinan Pravdoinan4)_ → `Observation.valueCodeableConcept.coding` (703, tanpa BQ) |
| 71 | 712–722 | Observation | 72178-7 | Given a mosquito net [RHEA] | _Diberikan Kelambu Berinsteksida_ → `Observation.valueBoolean` (715, tanpa BQ) |
| 72 | 723–732 | ServiceRequest | – | – | _Diperiksa RDT_ → `ServiceRequest.category` (723, tanpa BQ) |
| 73 | 736–743 | Specimen | – | – | – |
| 74 | 744–755 | Observation | 70569-9 | Plasmodium sp Ag [Identifier] in Blood by Rapid immunoassay | – |
| 75 | 756–767 | DiagnosticReport | 70569-9 | Plasmodium sp Ag [Identifier] in Blood by Rapid immunoassay | – |
| 76 | 768–777 | ServiceRequest | – | – | _Mikroskopis_ → `ServiceRequest.category` (768, tanpa BQ) |
| 77 | 781–788 | Specimen | – | – | – |
| 78 | 789–800 | Observation | 32700-7 | Microscopic observation [Identifier] in Blood by Malaria smear | – |
| 79 | 801–812 | DiagnosticReport | 32700-7 | Microscopic observation [Identifier] in Blood by Malaria smear | – |
| 80 | 813–822 | ServiceRequest | – | – | _Diperiksa RDT_ → `ServiceRequest.category` (813, tanpa BQ) |
| 81 | 826–833 | Specimen | – | – | – |
| 82 | 834–845 | Observation | 70569-9 | Plasmodium sp Ag [Identifier] in Blood by Rapid immunoassay | – |
| 83 | 846–857 | DiagnosticReport | 70569-9 | Plasmodium sp Ag [Identifier] in Blood by Rapid immunoassay | – |
| 84 | 858–867 | ServiceRequest | – | – | _Mikroskopis_ → `ServiceRequest.status` (859, tanpa BQ) |
| 85 | 871–878 | Specimen | – | – | – |
| 86 | 879–890 | Observation | 32700-7 | Microscopic observation [Identifier] in Blood by Malaria smear | – |
| 87 | 891–902 | DiagnosticReport | 32700-7 | Microscopic observation [Identifier] in Blood by Malaria smear | – |
| 88 | 903–914 | Observation | 50687-3 | Plasmodium sp Ag [Presence] in Blood | _Hasil Tes Darah Malaria(+/-)_ → `Observation.valueCodeableConcept.coding` (906, tanpa BQ) |
| 89 | 915–924 | MedicationStatement | – | – | _Obat Kina/ACT***_ → `MedicationStatement.status` (915, tanpa BQ) |
| 90 | 925–934 | ServiceRequest | – | – | _Diperiksa dahak*_ → `ServiceRequest.category` (925, tanpa BQ) |
| 91 | 938–945 | Specimen | – | – | – |
| 92 | 946–960 | Observation | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | _TBC(+/-)_ → `Observation.valueCodeableConcept.coding` (949, tanpa BQ) |
| 93 | 961–972 | DiagnosticReport | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | – |
| 94 | 973–983 | MedicationStatement | SP000125 | Obat anti tuberkulosis | _Obat***_ → `MedicationStatement.status` (973, tanpa BQ) |
| 95 | 984–993 | ServiceRequest | – | – | _Diperiksa Ankylostoma_ → `ServiceRequest.category` (984, tanpa BQ) |
| 96 | 997–1004 | Specimen | – | – | – |
| 97 | 1005–1016 | Observation | 5045-0 | Ancylostoma sp Ab [Units/volume] in Serum | _Ibu Hamil Tes(+/-)_ → `Observation.valueCodeableConcept.coding` (1008, tanpa BQ) |
| 98 | 1017–1028 | DiagnosticReport | 5045-0 | Ancylostoma sp Ab [Units/volume] in Serum | – |
| 99 | 1029–1038 | ServiceRequest | – | – | _Diperiksa IMS_ → `ServiceRequest.category` (1029, tanpa BQ) |
| 100 | 1043–1050 | Specimen | – | – | – |
| 101 | 1051–1064 | Observation | 22464-2 | Reagin Ab [Presence] in Specimen | _Hasil Tes(+/-)_ → `Observation.valueCodeableConcept.coding` (1055, tanpa BQ) |
| 102 | 1065–1076 | DiagnosticReport | – | – | – |
| 103 | 1077–1087 | Procedure | 830039004 | Genitourinary medicine service | _Diterapi_ → `Procedure.category.coding` (1077, tanpa BQ) |
| 104 | 1088–1097 | ServiceRequest | – | – | _Diperiksa Hepatitis_ → `ServiceRequest.category` (1088, tanpa BQ) |
| 105 | 1101–1108 | Specimen | – | – | – |
| 106 | 1109–1121 | Observation | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | _Hasil Tes(+/-)_ → `Observation.valueCodeableConcept.coding` (1113, tanpa BQ) |
| 107 | 1122–1133 | DiagnosticReport | – | – | – |
| 108 | 1134–1152 | Observation | 386413005 | Risk identification | _Resiko Terdeteksi Oleh**_ → `Observation.valueCodeableConcept.coding` (1137, tanpa BQ) |
| 109 | 1153–1166 | Condition | 134435003 | Routine antenatal care | _Komplikasi**_ → `Condition.category.coding` (1153, tanpa BQ) |
| 110 | 1167–1183 | ServiceRequest | 737492002 | Outpatient care management | _Kegiatan Rujukan**_ → `ServiceRequest.category` (1167, tanpa BQ) |
| 111 | 1184–1195 | Observation | SP000383 | Keadaan Ibu Saat Tiba | _Keadaan Tiba_ → `Observation.valueCodeableConcept.coding` (1187, tanpa BQ) |
| 112 | 1210–1216 | Condition | 134435003 | Routine antenatal care | – |
| 113 | 1233–1239 | Condition | – | – | – |
| 114 | 1240–1248 | EpisodeOfCare | ANC | Antenatal Care | – |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 46 |
| ServiceRequest | 17 |
| Specimen | 16 |
| DiagnosticReport | 16 |
| Procedure | 5 |
| Condition | 4 |
| Immunization | 2 |
| MedicationStatement | 2 |
| Encounter | 1 |
| Patient | 1 |
| Coverage | 1 |
| MedicationRequest | 1 |
| MedicationDispense | 1 |
| EpisodeOfCare | 1 |
| **Total** | **114** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 26 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 2 | 29 | Observation | `Observation.component.code.coding` | SP000020 | Umur Bulan | http://terminology.kemkes.go.id/sp |
| 3 | 32 | Observation | `Observation.component.code.coding` | SP000021 | Umur Hari | http://terminology.kemkes.go.id/sp |
| 4 | 43 | Observation | `Observation.code.coding` | 8665-2 | Last menstrual period start date | http://loinc.org |
| 5 | 44 | Observation | `Observation.code.coding` | ANC.B6.DE14 | Last menstrual period (LMP) date | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 6 | 47 | Observation | `Observation.code.coding` | 11778-8 | Delivery date Estimated | http://loinc.org |
| 7 | 48 | Observation | `Observation.code.coding` | ANC.B6.DE22 | Expected date of delivery (EDD) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 8 | 58 | Observation | `Observation.code.coding` | 18185-9 | Gestational age | http://loinc.org |
| 9 | 59 | Observation | `Observation.code.coding` | ANC.B6.DE17 | Gestational age | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 10 | 62 | Observation | `Observation.code.coding` | 32418-6 | Obstetric trimester Stated | http://loinc.org |
| 11 | 63 | Observation | `Observation.code.coding` | ANC.SS.DE13 | Trimester ke | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 12 | 65 | Encounter | `Encounter.hospitaliz ation.admitSource.co ding` | hosp-trans | Transferred from other hospital | http://terminology.hl7.org/CodeSystem/admit-source |
| 13 | 72 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 14 | 77 | Observation | `Observation.code.coding` | 8302-2 | Body height | http://loinc.org |
| 15 | 82 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 16 | 87 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://loinc.org |
| 17 | 92 | Observation | `Observation.code.coding` | 284473002 | Mid upper arm circumference | http://snomed.info/sct |
| 18 | 93 | Observation | `Observation.code.coding` | ANC.SS.DE3 | Lingkar Lengan Atas (LILA) | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 19 | 98 | Observation | `Observation.interpretation` | OI000035 | Risiko Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 20 | 99 | Observation | `Observation.interpretation` | OI000018 | Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 21 | 101 | Observation | `Observation.code.coding` | 11881-0 | Uterus Fundal height Tape measure | http://loinc.org |
| 22 | 102 | Observation | `Observation.code.coding` | ANC.B8.DE105 | Symphysis-fundal height | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 23 | 106 | Observation | `Observation.code.coding` | 32392-3 | Deep tendon reflex of Patellar | http://loinc.org |
| 24 | 107 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 25 | 108 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 26 | 109 | Observation | `Observation.code.coding` | 55283-6 | Fetal Heart rate | http://loinc.org |
| 27 | 110 | Observation | `Observation.code.coding` | ANC.B8.DE107 | Fetal heart rate | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 28 | 116 | Observation | `Observation.code.coding` | 249111004 | Engagement of head | http://loinc.org |
| 29 | 117 | Observation | `Observation.code.coding` | ANC.SS.DE46 | Kepala Terhadap PAP | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 30 | 118 | Observation | `Observation.valueCodeableConcept.coding` | 62098001 | Head not engaged | http://snomed.info/sct |
| 31 | 119 | Observation | `Observation.valueCodeableConcept.coding` | 249112006 | Head engaged | http://snomed.info/sct |
| 32 | 121 | Observation | `Observation.code.coding` | 89087-1 | Fetal Body weight Estimated | http://loinc.org |
| 33 | 122 | Observation | `Observation.code.coding` | ANC.SS.DE1 | Taksiran Berat Janin (TBJ) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 34 | 126 | Observation | `Observation.code.coding` | 72155-5 | Position in womb Fetus [RHEA] | http://loinc.org |
| 35 | 127 | Observation | `Observation.code.coding` | ANC.B8.DE111 | Fetal presentation | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 36 | 128 | Observation | `Observation.valueCodeableConcept.coding` | 1209182005 | Cephalic fetal presentation | http://snomed.info/sct |
| 37 | 129 | Observation | `Observation.valueCodeableConcept.coding` | 6096002 | Breech presentation | http://snomed.info/sct |
| 38 | 130 | Observation | `Observation.valueCodeableConcept.coding` | SP000006 | Organ Tubuh Lainnya | http://terminology.kemkes.go.id/sp |
| 39 | 131 | Observation | `Observation.valueCodeableConcept.coding` | 260415000 | Not detected | http://snomed.info/sct |
| 40 | 132 | Observation | `Observation.code.coding` | 55283-6 | Fetal Heart rate | http://loinc.org |
| 41 | 133 | Observation | `Observation.code.coding` | ANC.B8.DE107 | Fetal heart rate | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 42 | 137 | Observation | `Observation.code.coding` | 249111004 | Engagement of head | http://loinc.org |
| 43 | 138 | Observation | `Observation.code.coding` | ANC.SS.DE46 | Kepala Terhadap PAP | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 44 | 139 | Observation | `Observation.valueCodeableConcept.coding` | 62098001 | Head not engaged | http://snomed.info/sct |
| 45 | 140 | Observation | `Observation.valueCodeableConcept.coding` | 249112006 | Head engaged | http://snomed.info/sct |
| 46 | 142 | Observation | `Observation.code.coding` | 89087-1 | Fetal Body weight Estimated | http://loinc.org |
| 47 | 143 | Observation | `Observation.code.coding` | ANC.SS.DE1 | Taksiran Berat Janin (TBJ) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 48 | 147 | Observation | `Observation.code.coding` | 72155-5 | Position in womb Fetus [RHEA] | http://loinc.org |
| 49 | 148 | Observation | `Observation.code.coding` | ANC.B8.DE111 | Fetal presentation | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 50 | 149 | Observation | `Observation.valueCodeableConcept.coding` | 1209182005 | Cephalic fetal presentation | http://snomed.info/sct |
| 51 | 150 | Observation | `Observation.valueCodeableConcept.coding` | 6096002 | Breech presentation | http://snomed.info/sct |
| 52 | 152 | Observation | `Observation.code.coding` | 246435002 | Number of fetuses | http://snomed.info/sct |
| 53 | 153 | Observation | `Observation.code.coding` | ANC.B8.DE109 | Number of fetuses | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 54 | 157 | Observation | `Observation.code.coding` | 246435002 | Number of fetuses | http://snomed.info/sct |
| 55 | 158 | Observation | `Observation.code.coding` | ANC.B8.DE109 | Number of fetuses | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 56 | 160 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 57 | 169 | Procedure | `Procedure.code.coding` | 1230101008 | Counseling for pregnancy | http://snomed.info/sct |
| 58 | 181 | Immunization | `Immunization.vaccineCode` | VG139 | Td | http://sys-ids.kemkes.go.id/kfa |
| 59 | 197 | Immunization | `Immunization.vaccineCode` | VG139 | Td | http://sys-ids.kemkes.go.id/kfa |
| 60 | 212 | Procedure | `Procedure.code.coding` | 99.38 | Administration of tetanus toxoid | http://hl7.org/fhir/sid/icd-9-cm |
| 61 | 223 | Observation | `Observation.code.coding` | SP000122 | Catat di Buku KIA | http://terminology.kemkes.go.id/sp |
| 62 | 226 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 63 | 237 | MedicationRequest | `MedicationRequest.contained.code.coding` | 92000653 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula | http://sys-ids.kemkes.go.id/kfa |
| 64 | 271 | MedicationDispense | `MedicationDispense.contained.code.coding` | 93015491 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | http://sys-ids.kemkes.go.id/kfa |
| 65 | 304 | ServiceRequest | `ServiceRequest.code` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 66 | 314 | Specimen | `Specimen.type` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 67 | 323 | Observation | `Observation.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 68 | 324 | Observation | `Observation.code.coding` | ANC.B9.DE175 | Blood hemoglobin test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 69 | 337 | DiagnosticReport | `DiagnosticReport.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 70 | 351 | ServiceRequest | `ServiceRequest.code` | 2887-8 | Protein [Presence] in Urine | http://loinc.org |
| 71 | 361 | Specimen | `Specimen.type` | 122575003 | Urine specimen | http://snomed.info/sct |
| 72 | 370 | Observation | `Observation.code.coding` | 2887-8 | Protein [Presence] in Urine | http://loinc.org |
| 73 | 371 | Observation | `Observation.code.coding` | ANC.B9.DE114 | Urine test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 74 | 372 | Observation | `Observation.valueCodeableConcept.coding` | LA11843-2 | 3+ | http://loinc.org |
| 75 | 373 | Observation | `Observation.valueCodeableConcept.coding` | LA11842-4 | 2+ | http://loinc.org |
| 76 | 374 | Observation | `Observation.valueCodeableConcept.coding` | LA11841-6 | 1+ | http://loinc.org |
| 77 | 375 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 78 | 387 | DiagnosticReport | `DiagnosticReport.code.coding` | 2887-8 | Protein [Presence] in Urine | http://loinc.org |
| 79 | 401 | ServiceRequest | `ServiceRequest.code` | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | http://loinc.org |
| 80 | 411 | Specimen | `Specimen.type` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 81 | 420 | Observation | `Observation.code.coding` | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | http://loinc.org |
| 82 | 421 | Observation | `Observation.code.coding` | ANC.B9.DE159 | Blood glucose test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 83 | 436 | DiagnosticReport | `DiagnosticReport.code.coding` | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | http://loinc.org |
| 84 | 450 | ServiceRequest | `ServiceRequest.code` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 85 | 461 | Specimen | `Specimen.type` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 86 | 470 | Observation | `Observation.code.coding` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 87 | 471 | Observation | `Observation.code.coding` | ANC.B9.DE96 | Syphilis test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 88 | 472 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 89 | 473 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 90 | 476 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 91 | 486 | DiagnosticReport | `DiagnosticReport.code` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 92 | 500 | ServiceRequest | `ServiceRequest.code` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 93 | 510 | Specimen | `Specimen.type` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 94 | 519 | Observation | `Observation.code.coding` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 95 | 520 | Observation | `Observation.code.coding` | ANC.B9.DE60 | Hepatitis B test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 96 | 521 | Observation | `Observation.valueCodeableConcept.coding` | LA15255-5 | Reactive | http://loinc.org |
| 97 | 522 | Observation | `Observation.valueCodeableConcept.coding` | LA15256-3 | Nonreactive | http://loinc.org |
| 98 | 534 | DiagnosticReport | `DiagnosticReport.code` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 99 | 548 | ServiceRequest | `ServiceRequest.code` | SP000115 | Pemeriksaan Laboratorium Thalassemia | http://terminology.kemkes.go.id/sp |
| 100 | 558 | Specimen | `Specimen.type` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 101 | 567 | Observation | `Observation.code.coding` | SP000115 | Pemeriksaan Laboratorium Thalassemia | http://terminology.kemkes.go.id/sp |
| 102 | 572 | DiagnosticReport | `DiagnosticReport.code` | 94537-8 | Hemoglobin panel - Blood by HPLC | http://loinc.org |
| 103 | 586 | ServiceRequest | `ServiceRequest.code` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 104 | 596 | Specimen | `Specimen.type` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 105 | 605 | Observation | `Observation.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 106 | 610 | DiagnosticReport | `DiagnosticReport.code` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 107 | 622 | Observation | `Observation.code.coding` | 278977008 | Human immunodeficiency virus status | http://snomed.info/sct |
| 108 | 623 | Observation | `Observation.valueCodeableConcept.coding` | 165816005 | Human immunodeficiency virus detected | http://snomed.info/sct |
| 109 | 624 | Observation | `Observation.valueCodeableConcept.coding` | 165815009 | Human immunodeficiency virus not detected | http://snomed.info/sct |
| 110 | 625 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 111 | 633 | Procedure | `Procedure.code.coding` | TK000016 | Edukasi Tes HIV | http://terminology.kemkes.go.id |
| 112 | 647 | ServiceRequest | `ServiceRequest.code` | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 113 | 657 | Specimen | `Specimen.type` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 114 | 666 | Observation | `Observation.code.coding` | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 115 | 667 | Observation | `Observation.code.coding` | ANC.B9.DE32 | HIV test | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 116 | 668 | Observation | `Observation.valueCodeableConcept.coding` | LA15255-5 | Reactive | http://loinc.org |
| 117 | 669 | Observation | `Observation.valueCodeableConcept.coding` | LA15256-3 | Nonreactive | http://loinc.org |
| 118 | 679 | DiagnosticReport | `DiagnosticReport.code` | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 119 | 690 | Procedure | `Procedure.code.coding` | SP000046 | Terapi Antiretroviral (ART) | http://terminology.kemkes.go.id/sp |
| 120 | 701 | Observation | `Observation.code.coding` | 57071-3 | Obstetric delivery method | https://loinc.org |
| 121 | 702 | Observation | `Observation.valueCodeableConcept.coding` | 48782003 | Delivery normal | http://snomed.info/sct |
| 122 | 703 | Observation | `Observation.valueCodeableConcept.coding` | 200144004 | Deliveries by cesarean | http://snomed.info/sct |
| 123 | 714 | Observation | `Observation.code.coding` | 72178-7 | Given a mosquito net [RHEA] | http://loinc.org |
| 124 | 727 | ServiceRequest | `ServiceRequest.code` | 70569-9 | Plasmodium sp Ag [Identifier] in Blood by Rapid immunoassay | http://loinc.org |
| 125 | 737 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 126 | 746 | Observation | `Observation.code.coding` | 70569-9 | Plasmodium sp Ag [Identifier] in Blood by Rapid immunoassay | http://loinc.org |
| 127 | 747 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 128 | 748 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 129 | 758 | DiagnosticReport | `DiagnosticReport.code.coding` | 70569-9 | Plasmodium sp Ag [Identifier] in Blood by Rapid immunoassay | http://loinc.org |
| 130 | 772 | ServiceRequest | `ServiceRequest.code` | 32700-7 | Microscopic observation [Identifier] in Blood by Malaria smear | http://loinc.org |
| 131 | 782 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 132 | 791 | Observation | `Observation.code.coding` | 32700-7 | Microscopic observation [Identifier] in Blood by Malaria smear | http://loinc.org |
| 133 | 792 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 134 | 793 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 135 | 803 | DiagnosticReport | `DiagnosticReport.code.coding` | 32700-7 | Microscopic observation [Identifier] in Blood by Malaria smear | http://loinc.org |
| 136 | 817 | ServiceRequest | `ServiceRequest.code` | 70569-9 | Plasmodium sp Ag [Identifier] in Blood by Rapid immunoassay | http://loinc.org |
| 137 | 827 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 138 | 836 | Observation | `Observation.code.coding` | 70569-9 | Plasmodium sp Ag [Identifier] in Blood by Rapid immunoassay | http://loinc.org |
| 139 | 837 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 140 | 838 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 141 | 848 | DiagnosticReport | `DiagnosticReport.code.coding` | 70569-9 | Plasmodium sp Ag [Identifier] in Blood by Rapid immunoassay | http://loinc.org |
| 142 | 862 | ServiceRequest | `ServiceRequest.code` | 32700-7 | Microscopic observation [Identifier] in Blood by Malaria smear | http://loinc.org |
| 143 | 872 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 144 | 881 | Observation | `Observation.code.coding` | 32700-7 | Microscopic observation [Identifier] in Blood by Malaria smear | http://loinc.org |
| 145 | 882 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 146 | 883 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 147 | 893 | DiagnosticReport | `DiagnosticReport.code.coding` | 32700-7 | Microscopic observation [Identifier] in Blood by Malaria smear | http://loinc.org |
| 148 | 905 | Observation | `Observation.code.coding` | 50687-3 | Plasmodium sp Ag [Presence] in Blood | http://loinc.org |
| 149 | 906 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 150 | 907 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 151 | 929 | ServiceRequest | `ServiceRequest.code` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 152 | 939 | Specimen | `Specimen.type` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 153 | 948 | Observation | `Observation.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 154 | 949 | Observation | `Observation.valueCodeableConcept.coding` | 260385009 | Negative | http://snomed.info/sct |
| 155 | 950 | Observation | `Observation.valueCodeableConcept.coding` | LA11841-6 | 1+ | http://loinc.org |
| 156 | 951 | Observation | `Observation.valueCodeableConcept.coding` | LA11842-4 | 2+ | http://loinc.org |
| 157 | 952 | Observation | `Observation.valueCodeableConcept.coding` | LA11843-2 | 3+ | http://loinc.org |
| 158 | 960 | Observation | `Observation.dataAbsentReason.coding` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 159 | 963 | DiagnosticReport | `DiagnosticReport.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 160 | 976 | MedicationStatement | `MedicationStatement.medicationCodeableConcept.coding` | SP000125 | Obat anti tuberkulosis | http://terminology.kemkes.go.id/sp |
| 161 | 988 | ServiceRequest | `ServiceRequest.code` | 5045-0 | Ancylostoma sp Ab [Units/volume] in Serum | http://loinc.org |
| 162 | 998 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 163 | 1007 | Observation | `Observation.code.coding` | 5045-0 | Ancylostoma sp Ab [Units/volume] in Serum | http://loinc.org |
| 164 | 1008 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 165 | 1009 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 166 | 1019 | DiagnosticReport | `DiagnosticReport.code.coding` | 5045-0 | Ancylostoma sp Ab [Units/volume] in Serum | http://loinc.org |
| 167 | 1033 | ServiceRequest | `ServiceRequest.code` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 168 | 1044 | Specimen | `Specimen.type` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 169 | 1053 | Observation | `Observation.code.coding` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 170 | 1054 | Observation | `Observation.code.coding` | ANC.B9.DE96 | Syphilis test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 171 | 1055 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 172 | 1056 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 173 | 1057 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 174 | 1067 | DiagnosticReport | `DiagnosticReport.code` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 175 | 1078 | Procedure | `Procedure.code.coding` | 830039004 | Genitourinary medicine service | http://snomed.info/sct |
| 176 | 1092 | ServiceRequest | `ServiceRequest.code` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 177 | 1102 | Specimen | `Specimen.type` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 178 | 1111 | Observation | `Observation.code.coding` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 179 | 1112 | Observation | `Observation.code.coding` | ANC.B9.DE60 | Hepatitis B test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 180 | 1113 | Observation | `Observation.valueCodeableConcept.coding` | LA15255-5 | Reactive | http://loinc.org |
| 181 | 1114 | Observation | `Observation.valueCodeableConcept.coding` | LA15256-3 | Nonreactive | http://loinc.org |
| 182 | 1124 | DiagnosticReport | `DiagnosticReport.code` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 183 | 1136 | Observation | `Observation.code.coding` | 386413005 | Risk identification | http://snomed.info/sct |
| 184 | 1137 | Observation | `Observation.valueCodeableConcept.coding` | 1156040003 | Self reported | http://snomed.info/sct |
| 185 | 1138 | Observation | `Observation.valueCodeableConcept.coding` | 303071001 | Person in the family | http://snomed.info/sct |
| 186 | 1139 | Observation | `Observation.valueCodeableConcept.coding` | 257514003 | Member of public involved incidentally | http://snomed.info/sct |
| 187 | 1140 | Observation | `Observation.valueCodeableConcept.coding` | OV000012 | Dukun | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 188 | 1141 | Observation | `Observation.valueCodeableConcept.coding` | SP000373 | Kader Kesehatan | http://terminology.kemkes.go.id/sp |
| 189 | 1142 | Observation | `Observation.valueCodeableConcept.coding` | 309453006 | Registered midwife | http://snomed.info/sct |
| 190 | 1143 | Observation | `Observation.valueCodeableConcept.coding` | 106292003 | Professional nurse | http://snomed.info/sct |
| 191 | 1144 | Observation | `Observation.valueCodeableConcept.coding` | 309343006 | Physician | http://snomed.info/sct |
| 192 | 1145 | Observation | `Observation.valueCodeableConcept.coding` | 11935004 | Obstetrician | http://snomed.info/sct |
| 193 | 1156 | Condition | `Condition.code.coding` | 134435003 | Routine antenatal care | http://snomed.info/sct |
| 194 | 1157 | Condition | `Condition.code.coding` | O13 | Gestational [pregnancy-induced] hypertension without significant proteinuria | http://hl7.org/fhir/sid/icd-10 |
| 195 | 1158 | Condition | `Condition.code.coding` | O06.9 | Unspecified abortion Complete or unspecified, without complication | http://hl7.org/fhir/sid/icd-10 |
| 196 | 1159 | Condition | `Condition.code.coding` | O20.9 | Haemorrhage in early pregnancy, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 197 | 1160 | Condition | `Condition.code.coding` | O98.9 | Unspecified maternal infectious or parasitic disease complicating pregnancy, childbirth and the puerperium | http://hl7.org/fhir/sid/icd-10 |
| 198 | 1161 | Condition | `Condition.code.coding` | O42.9 | Premature rupture of membranes, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 199 | 1162 | Condition | `Condition.code.coding` | O99.8 | Other specified diseases and conditions complicating pregnancy, childbirth and the puerperium | http://hl7.org/fhir/sid/icd-10 |
| 200 | 1168 | ServiceRequest | `ServiceRequest.code.coding` | 737492002 | Outpatient care management | http://snomed.info/sct |
| 201 | 1175 | ServiceRequest | `ServiceRequest.locationCode.coding` | SP000128 | Rumah Sakit Ibu dan Anak | http://terminology.kemkes.go.id/sp |
| 202 | 1186 | Observation | `Observation.code.coding` | SP000383 | Keadaan Ibu Saat Tiba | http://terminology.kemkes.go.id/sp |
| 203 | 1187 | Observation | `Observation.valueCodeableConcept.coding` | 63238001 | Dead on arrival at hospital | http://snomed.info/sct |
| 204 | 1188 | Observation | `Observation.valueCodeableConcept.coding` | 438949009 | Alive | http://snomed.info/sct |
| 205 | 1212 | Condition | `Condition.code.coding` | 134435003 | Routine antenatal care | http://snomed.info/sct |
| 206 | 1244 | EpisodeOfCare | `EpisodeOfCare.type.coding` | ANC | Antenatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://loinc.org | 97 |
| http://snomed.info/sct | 50 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 22 |
| http://terminology.kemkes.go.id/sp | 11 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 6 |
| http://hl7.org/fhir/sid/icd-10 | 6 |
| http://sys-ids.kemkes.go.id/kfa | 4 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 3 |
| http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes | 2 |
| http://terminology.hl7.org/CodeSystem/admit-source | 1 |
| http://hl7.org/fhir/sid/icd-9-cm | 1 |
| http://terminology.kemkes.go.id | 1 |
| https://loinc.org | 1 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 1 |
| **Total** | **206** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
