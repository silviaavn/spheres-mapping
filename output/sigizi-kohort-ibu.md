# Output Form: SiGizi Kohort Ibu

Sumber: `mapping/phdt-data-dictionary-sigizi-kohort-ibu.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-sigizi-kohort-ibu.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 63 |
| Code (`jumlah code` = 1) | 109 |
| Code unik (code + CodeSystem) | 82 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 3 |
| Variabel BQ (unik) | 42 |
| Variabel raw (variabel dictionary; belum ada file mentah) | 42 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–24 | Patient | – | – | `nama` → `Patient.name.text` (2)<br>`nik` → `Patient.identifier.value` (5)<br>`alamat` → `Patient.address.use` (9)<br>_Nama Provinsi_ → `Patient.address.extension.url` (13, tanpa BQ)<br>`prov` → `Patient.address.extension.extension.valueCode` (15)<br>_Nama Kabupaten_ → `Patient.address.extension.url` (16, tanpa BQ)<br>`kabkota` → `Patient.address.extension.extension.valueCode` (18)<br>_Nama Kecamatan_ → `Patient.address.extension.url` (19, tanpa BQ)<br>`kec` → `Patient.address.extension.extension.valueCode` (21)<br>_Nama Desa_ → `Patient.address.extension.url` (22, tanpa BQ)<br>`desakel` → `Patient.address.extension.extension.valueCode` (24) |
| 2 | 110–118 | EpisodeOfCare | ANC | Antenatal Care | `hpht` → `EpisodeOfCare.statusHistory.period.start` (113) |
| 3 | 119–139 | Encounter | – | – | _Tanggal ANC_ → `Encounter.period.start` (133, tanpa BQ)<br>`posyandu` → `Encounter.location.location.reference` (135) 🔎 lookup master data<br>`pukesmas` → `Encounter.serviceProvider.reference` (139) 🔎 lookup master data |
| 4 | 140–146 | Condition | 134435003 | Routine antenatal care | – |
| 5 | 158–161 | RelatedPerson | – | – | `nama_suami` → `RelatedPerson.patient` (158) |
| 6 | 162–173 | Observation | SP000651 | Sumber Pembiayaan Pelayanan Kesehatan | `sumber_pembiayaan` → `Observation.valueCodeableConcept.coding` (165) |
| 7 | 174–185 | Observation | 424144002 | Current chronological age | `usia_ibu` → `Observation.valueQuantity.value` (177) |
| 8 | 186–197 | Observation | 11996-6 | [#] Pregnancies | `kehamilan_ke` → `Observation.valueInteger` (190) |
| 9 | 198–210 | Observation | OC000001 | Jarak kehamilan | `jarak_kehamilan` → `Observation.valueQuantity.value` (202) |
| 10 | 211–222 | Observation | 8665-2 | Last menstrual period start date | _HPHT_ → `Observation.valueDateTime` (215, tanpa BQ) |
| 11 | 223–235 | Observation | 29463-7 | Body weight | _Berat Badan_ → `Observation.status` (223, tanpa BQ)<br>`bb` → `Observation.valueQuantity.value` (227) |
| 12 | 236–248 | Observation | 8302-2 | Body height | _Tinggi_ → `Observation.status` (236, tanpa BQ)<br>`tb` → `Observation.valueQuantity.value` (240) |
| 13 | 249–273 | Observation | 284473002 | Mid upper arm circumference | `lila` → `Observation.valueQuantity.value` (253) |
| 14 | 274–300 | Observation | OC000010 | Indeks Massa Tubuh Sebelum Hamil | _IMT Sebelum Hamil_ → `Observation.valueRange.low.value` (278, tanpa BQ)<br>`imt` → `Observation.interpretation.coding` (282) |
| 15 | 301–320 | Immunization | – | – | _Riwayat Imun TT Terakhir_ → `Immunization.status` (301, tanpa BQ)<br>`skrining_imunisasi_tt_tanggal_imunisasi` → `Immunization.occurrenceDateTime` (307)<br>`skrining_imunisasi_tt_status_imunisasi` → `Immunization.protocolApplied.doseNumberPositiveInt` (313) |
| 16 | 321–330 | Immunization | – | – | – |
| 17 | 331–341 | Observation | SP000001 | Skrining Imunisasi Tetanus Toksoid | – |
| 18 | 342–351 | ServiceRequest | 718-7 | Hemoglobin [Mass/volume] in Blood | `pemeriksaan_lab_hb` → `ServiceRequest.category` (342) |
| 19 | 356–363 | Specimen | 122555007 | Venous blood specimen | – |
| 20 | 364–391 | Observation | 718-7 | Hemoglobin [Mass/volume] in Blood | – |
| 21 | 392–403 | DiagnosticReport | 718-7 | Hemoglobin [Mass/volume] in Blood | – |
| 22 | 404–413 | ServiceRequest | 2887-8 | Protein [Presence] in Urine | _Lab : Protein Urine_ → `ServiceRequest.category` (404, tanpa BQ) |
| 23 | 418–425 | Specimen | 122575003 | Urine specimen | – |
| 24 | 426–439 | Observation | 2887-8 | Protein [Presence] in Urine | `pemeriksaan_lab_protein_urin` → `Observation.valueCodeableConcept.coding` (430) |
| 25 | 440–451 | DiagnosticReport | 2887-8 | Protein [Presence] in Urine | – |
| 26 | 452–461 | ServiceRequest | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | _Lab : Gula Sewaktu_ → `ServiceRequest.category` (452, tanpa BQ) |
| 27 | 466–473 | Specimen | 122555007 | Venous blood specimen | – |
| 28 | 474–491 | Observation | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | `pemeriksaan_lab_gula_darah` → `Observation.interpretation.coding` (480) |
| 29 | 492–503 | DiagnosticReport | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | – |
| 30 | 504–523 | Encounter | – | – | `tahun_januari` → `Encounter.identifier` (504)<br>_Januari_ → `Encounter.period.start` (518, tanpa BQ)<br>_Januari_ → `Encounter.period.end` (519, tanpa BQ) |
| 31 | 524–530 | Condition | 134435003 | Routine antenatal care | – |
| 32 | 542–561 | Encounter | – | – | `tahun_februari` → `Encounter.identifier` (542)<br>_Februari_ → `Encounter.period.start` (556, tanpa BQ)<br>_Februari_ → `Encounter.period.end` (557, tanpa BQ) |
| 33 | 562–568 | Condition | 134435003 | Routine antenatal care | – |
| 34 | 580–599 | Encounter | – | – | `tahun_maret` → `Encounter.identifier` (580)<br>_Maret_ → `Encounter.period.start` (594, tanpa BQ)<br>_Maret_ → `Encounter.period.end` (595, tanpa BQ) |
| 35 | 600–606 | Condition | 134435003 | Routine antenatal care | – |
| 36 | 618–637 | Encounter | – | – | `tahun_april` → `Encounter.identifier` (618)<br>_April_ → `Encounter.period.start` (632, tanpa BQ)<br>_April_ → `Encounter.period.end` (633, tanpa BQ) |
| 37 | 638–644 | Condition | 134435003 | Routine antenatal care | – |
| 38 | 656–675 | Encounter | – | – | `tahun_mei` → `Encounter.identifier` (656)<br>_Mei_ → `Encounter.period.start` (670, tanpa BQ)<br>_Mei_ → `Encounter.period.end` (671, tanpa BQ) |
| 39 | 676–682 | Condition | 134435003 | Routine antenatal care | – |
| 40 | 694–713 | Encounter | – | – | `tahun_juni` → `Encounter.identifier` (694)<br>_Juni_ → `Encounter.period.start` (708, tanpa BQ)<br>_Juni_ → `Encounter.period.end` (709, tanpa BQ) |
| 41 | 714–720 | Condition | 134435003 | Routine antenatal care | – |
| 42 | 732–751 | Encounter | – | – | `tahun_juli` → `Encounter.identifier` (732)<br>_Juli_ → `Encounter.period.start` (746, tanpa BQ)<br>_Juli_ → `Encounter.period.end` (747, tanpa BQ) |
| 43 | 752–758 | Condition | 134435003 | Routine antenatal care | – |
| 44 | 770–789 | Encounter | – | – | `tahun_agustus` → `Encounter.identifier` (770)<br>_Agustus_ → `Encounter.period.start` (784, tanpa BQ)<br>_Agustus_ → `Encounter.period.end` (785, tanpa BQ) |
| 45 | 790–796 | Condition | 134435003 | Routine antenatal care | – |
| 46 | 808–827 | Encounter | – | – | `tahun_september` → `Encounter.identifier` (808)<br>_September_ → `Encounter.period.start` (822, tanpa BQ)<br>_September_ → `Encounter.period.end` (823, tanpa BQ) |
| 47 | 828–834 | Condition | 134435003 | Routine antenatal care | – |
| 48 | 846–865 | Encounter | – | – | `tahun_oktober` → `Encounter.identifier` (846)<br>_Oktober_ → `Encounter.period.start` (860, tanpa BQ)<br>_Oktober_ → `Encounter.period.end` (861, tanpa BQ) |
| 49 | 866–872 | Condition | 134435003 | Routine antenatal care | – |
| 50 | 884–903 | Encounter | – | – | `tahun_november` → `Encounter.identifier` (884)<br>_November_ → `Encounter.period.start` (898, tanpa BQ)<br>_November_ → `Encounter.period.end` (899, tanpa BQ) |
| 51 | 904–910 | Condition | 134435003 | Routine antenatal care | – |
| 52 | 922–941 | Encounter | – | – | `tahun_desember` → `Encounter.identifier` (922)<br>_Desember_ → `Encounter.period.start` (936, tanpa BQ)<br>_Desember_ → `Encounter.period.end` (937, tanpa BQ) |
| 53 | 942–948 | Condition | 134435003 | Routine antenatal care | – |
| 54 | 960–973 | EpisodeOfCare | ANC | Antenatal Care | `status_persalinan_tanggal_melahirkan` → `EpisodeOfCare.statusHistory.period.end` (964) |
| 55 | 974–993 | Encounter | – | – | _Tanggal Melahirkan_ → `Encounter.period.start` (988, tanpa BQ) |
| 56 | 994–1000 | Condition | 386337006 | Intrapartal care | – |
| 57 | 1012–1022 | Observation | 93857-1 | Date and time of obstetric delivery | _Tanggal Melahirkan_ → `Observation.valueDateTime` (1015, tanpa BQ)<br>`status_persalinan_penolong` → `Observation.performer.display` (1022) |
| 58 | 1023–1034 | Observation | 63893-2 | Outcome of pregnancy | `status_persalinan_lahir_hidup_lahir_mati` → `Observation.valueCodeableConcept.coding` (1025) |
| 59 | 1035–1041 | PractitionerRole | – | – | _Penolong_ → `PractitionerRole.active` (1035, tanpa BQ) |
| 60 | 1042–1055 | Observation | 57071-3 | Obstetric delivery method | `status_persalinan_cara_persalinan` → `Observation.valueCodeableConcept.coding` (1045)<br>_Penolong_ → `Observation.performer.reference` (1054, tanpa BQ) |
| 61 | 1056–1068 | Procedure | 73.59 | Other manually assisted delivery | _Cara Persalinan_ → `Procedure.category.coding` (1056, tanpa BQ)<br>_Penolong_ → `Procedure.performer.actor.reference` (1067, tanpa BQ) |
| 62 | 1069–1090 | Observation | 72150-6 | Delivery location | `status_persalinan_tempat` → `Observation.valueCodeableConcept.coding` (1072)<br>_Penolong_ → `Observation.performer.reference` (1089, tanpa BQ) |
| 63 | 1091–1102 | Condition | 161805006 | Past pregnancy history of cesarean section | `status_persalinan_penyulit_persalinan` → `Condition.clinicalStatus.coding` (1091) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 17 |
| Condition | 15 |
| Encounter | 14 |
| ServiceRequest | 3 |
| Specimen | 3 |
| DiagnosticReport | 3 |
| EpisodeOfCare | 2 |
| Immunization | 2 |
| Patient | 1 |
| RelatedPerson | 1 |
| PractitionerRole | 1 |
| Procedure | 1 |
| **Total** | **63** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 114 | EpisodeOfCare | `EpisodeOfCare.type.coding` | ANC | Antenatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 2 | 142 | Condition | `Condition.code.coding` | 134435003 | Routine antenatal care | http://snomed.info/sct |
| 3 | 164 | Observation | `Observation.code.coding` | SP000651 | Sumber Pembiayaan Pelayanan Kesehatan | http://terminology.kemkes.go.id/sp |
| 4 | 165 | Observation | `Observation.valueCodeableConcept.coding` | SP000652 | Jaminan Kesehatan Nasional (JKN) | http://terminology.kemkes.go.id/sp |
| 5 | 166 | Observation | `Observation.dataAbsentReason` | unknown | Unknown | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 6 | 176 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 7 | 188 | Observation | `Observation.code.coding` | 11996-6 | [#] Pregnancies | http://loinc.org |
| 8 | 189 | Observation | `Observation.code.coding` | ANC.B6.DE24 | Number of pregnancies (gravida) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 9 | 200 | Observation | `Observation.code.coding` | OC000001 | Jarak kehamilan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 10 | 201 | Observation | `Observation.code.coding` | ANC.SS.DE53 | Jarak kehamilan | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 11 | 213 | Observation | `Observation.code.coding` | 8665-2 | Last menstrual period start date | http://loinc.org |
| 12 | 214 | Observation | `Observation.code.coding` | ANC.B6.DE14 | Last menstrual period (LMP) date | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 13 | 225 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 14 | 226 | Observation | `Observation.code.coding` | ANC.B8.DE3 | Current weight | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 15 | 238 | Observation | `Observation.code.coding` | 8302-2 | Body height | http://loinc.org |
| 16 | 239 | Observation | `Observation.code.coding` | ANC.B8.DE1 | Height | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 17 | 251 | Observation | `Observation.code.coding` | 284473002 | Mid upper arm circumference | http://snomed.info/sct |
| 18 | 252 | Observation | `Observation.code.coding` | ANC.SS.DE3 | Lingkar Lengan Atas (LILA) | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 19 | 271 | Observation | `Observation.interpretation` | OI000018 | Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 20 | 272 | Observation | `Observation.interpretation` | OI000035 | Risiko Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 21 | 273 | Observation | `Observation.interpretation` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 22 | 276 | Observation | `Observation.code.coding` | OC000010 | Indeks Massa Tubuh Sebelum Hamil | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 23 | 277 | Observation | `Observation.code.coding` | ANC.SS.DE58 | IMT Sebelum Hamil | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 24 | 282 | Observation | `Observation.interpretation.coding` | 43664005 | Normal weight | http://snomed.info/sct |
| 25 | 285 | Observation | `Observation.interpretation.coding` | 248342006 | Underweight | http://snomed.info/sct |
| 26 | 290 | Observation | `Observation.interpretation.coding` | 238131007 | Overweight | http://snomed.info/sct |
| 27 | 293 | Observation | `Observation.interpretation.coding` | 414915002 | Obese | http://snomed.info/sct |
| 28 | 303 | Immunization | `Immunization.vaccineCode` | VG139 | Td | http://sys-ids.kemkes.go.id/kfa |
| 29 | 321 | Immunization | `Immunization.vaccineCode` | VG139 | Td | http://sys-ids.kemkes.go.id/kfa |
| 30 | 333 | Observation | `Observation.code.coding` | SP000001 | Skrining Imunisasi Tetanus Toksoid | http://terminology.kemkes.go.id/sp |
| 31 | 334 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 32 | 346 | ServiceRequest | `ServiceRequest.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 33 | 354 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002 | Laboratory worker | http://snomed.info/sct |
| 34 | 357 | Specimen | `Specimen.type.coding` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 35 | 366 | Observation | `Observation.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 36 | 367 | Observation | `Observation.code.coding` | ANC.B9.DE175 | Blood hemoglobin test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 37 | 370 | Observation | `Observation.interpretation.coding` | 860635002 | No anemia present | http://snomed.info/sct |
| 38 | 375 | Observation | `Observation.interpretation.coding` | OI000032 | Anemia ringan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 39 | 380 | Observation | `Observation.interpretation.coding` | OI000033 | Anemia sedang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 40 | 383 | Observation | `Observation.interpretation.coding` | OI000034 | Anemia berat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 41 | 384 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 42 | 394 | DiagnosticReport | `DiagnosticReport.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 43 | 408 | ServiceRequest | `ServiceRequest.code.coding` | 2887-8 | Protein [Presence] in Urine | http://loinc.org |
| 44 | 416 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002 | Laboratory worker | http://snomed.info/sct |
| 45 | 419 | Specimen | `Specimen.type.coding` | 122575003 | Urine specimen | http://snomed.info/sct |
| 46 | 428 | Observation | `Observation.code.coding` | 2887-8 | Protein [Presence] in Urine | http://loinc.org |
| 47 | 429 | Observation | `Observation.code.coding` | ANC.B9.DE114 | Urine test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 48 | 430 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 49 | 431 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 50 | 432 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 51 | 442 | DiagnosticReport | `DiagnosticReport.code.coding` | 2887-8 | Protein [Presence] in Urine | http://loinc.org |
| 52 | 456 | ServiceRequest | `ServiceRequest.code.coding` | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | http://loinc.org |
| 53 | 464 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002 | Laboratory worker | http://snomed.info/sct |
| 54 | 467 | Specimen | `Specimen.type.coding` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 55 | 476 | Observation | `Observation.code.coding` | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | http://loinc.org |
| 56 | 477 | Observation | `Observation.code.coding` | ANC.B9.DE159 | Blood glucose test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 57 | 480 | Observation | `Observation.interpretation.coding` | 166921001 | Blood glucose normal | http://snomed.info/sct |
| 58 | 483 | Observation | `Observation.interpretation.coding` | 166922008 | Blood glucose abnormal | http://snomed.info/sct |
| 59 | 484 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 60 | 494 | DiagnosticReport | `DiagnosticReport.code.coding` | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | http://loinc.org |
| 61 | 526 | Condition | `Condition.code.coding` | 134435003 | Routine antenatal care | http://snomed.info/sct |
| 62 | 564 | Condition | `Condition.code.coding` | 134435003 | Routine antenatal care | http://snomed.info/sct |
| 63 | 602 | Condition | `Condition.code.coding` | 134435003 | Routine antenatal care | http://snomed.info/sct |
| 64 | 640 | Condition | `Condition.code.coding` | 134435003 | Routine antenatal care | http://snomed.info/sct |
| 65 | 678 | Condition | `Condition.code.coding` | 134435003 | Routine antenatal care | http://snomed.info/sct |
| 66 | 716 | Condition | `Condition.code.coding` | 134435003 | Routine antenatal care | http://snomed.info/sct |
| 67 | 754 | Condition | `Condition.code.coding` | 134435003 | Routine antenatal care | http://snomed.info/sct |
| 68 | 792 | Condition | `Condition.code.coding` | 134435003 | Routine antenatal care | http://snomed.info/sct |
| 69 | 830 | Condition | `Condition.code.coding` | 134435003 | Routine antenatal care | http://snomed.info/sct |
| 70 | 868 | Condition | `Condition.code.coding` | 134435003 | Routine antenatal care | http://snomed.info/sct |
| 71 | 906 | Condition | `Condition.code.coding` | 134435003 | Routine antenatal care | http://snomed.info/sct |
| 72 | 944 | Condition | `Condition.code.coding` | 134435003 | Routine antenatal care | http://snomed.info/sct |
| 73 | 968 | EpisodeOfCare | `EpisodeOfCare.type.coding` | ANC | Antenatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 74 | 996 | Condition | `Condition.code.coding` | 386337006 | Intrapartal care | http://snomed.info/sct |
| 75 | 1014 | Observation | `Observation.code.coding` | 93857-1 | Date and time of obstetric delivery | http://loinc.org |
| 76 | 1024 | Observation | `Observation.code.coding` | 63893-2 | Outcome of pregnancy | http://loinc.org |
| 77 | 1025 | Observation | `Observation.valueCodeableConcept.coding` | LA14270-5 | Live birth | http://loinc.org |
| 78 | 1026 | Observation | `Observation.valueCodeableConcept.coding` | LA14271-3 | Stillborn | http://loinc.org |
| 79 | 1027 | Observation | `Observation.dataAbsentReason` | unknown | Unknown | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 80 | 1037 | PractitionerRole | `PractitionerRole.code.coding` | 309453006 | Registered midwife | http://snomed.info/sct |
| 81 | 1038 | PractitionerRole | `PractitionerRole.code.coding` | 309343006 | Physician | http://snomed.info/sct |
| 82 | 1039 | PractitionerRole | `PractitionerRole.code.coding` | 309367003 | Obstetrician and gynecologist | http://snomed.info/sct |
| 83 | 1040 | PractitionerRole | `PractitionerRole.code.coding` | 224535009 | Registered nurse | http://snomed.info/sct |
| 84 | 1044 | Observation | `Observation.code.coding` | 57071-3 | Obstetric delivery method | http://loinc.org |
| 85 | 1045 | Observation | `Observation.valueCodeableConcept.coding` | 48782003 | Delivery normal | http://snomed.info/sct |
| 86 | 1046 | Observation | `Observation.valueCodeableConcept.coding` | 200138003 | Vacuum extractor delivery - delivered | http://snomed.info/sct |
| 87 | 1047 | Observation | `Observation.valueCodeableConcept.coding` | 200130005 | Forceps delivery - delivered | http://snomed.info/sct |
| 88 | 1048 | Observation | `Observation.valueCodeableConcept.coding` | 200144004 | Deliveries by cesarean | http://snomed.info/sct |
| 89 | 1057 | Procedure | `Procedure.code.coding` | 73.59 | Other manually assisted delivery |  |
| 90 | 1058 | Procedure | `Procedure.code.coding` | 72.7 | Vacuum extraction |  |
| 91 | 1059 | Procedure | `Procedure.code.coding` | 72 | Low forceps delivery |  |
| 92 | 1060 | Procedure | `Procedure.code.coding` | 74.1 | Classical cesarean section |  |
| 93 | 1071 | Observation | `Observation.code.coding` | 72150-6 | Delivery location | http://loinc.org |
| 94 | 1072 | Observation | `Observation.valueCodeableConcept.coding` | 264362003 | Home | http://snomed.info/sct |
| 95 | 1073 | Observation | `Observation.valueCodeableConcept.coding` | OT000001 | Polindes | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 96 | 1074 | Observation | `Observation.valueCodeableConcept.coding` | OT000002 | Pustu | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 97 | 1075 | Observation | `Observation.valueCodeableConcept.coding` | 102 | Pusat Kesehatan Masyarakat | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 98 | 1076 | Observation | `Observation.valueCodeableConcept.coding` | 103 | Klinik | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 99 | 1077 | Observation | `Observation.valueCodeableConcept.coding` | OT000008 | Rumah Bersalin | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 100 | 1078 | Observation | `Observation.valueCodeableConcept.coding` | 82242000 | Children’s hospital | http://snomed.info/sct |
| 101 | 1079 | Observation | `Observation.valueCodeableConcept.coding` | 104 | Rumah Sakit | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 102 | 1080 | Observation | `Observation.valueCodeableConcept.coding` | OT000004 | Bidan Praktek Mandiri | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 103 | 1081 | Observation | `Observation.valueCodeableConcept.coding` | LT000008 | Dalam perjalanan dari rumah/masyarakat | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 104 | 1082 | Observation | `Observation.valueCodeableConcept.coding` | LT000009 | Dalam perjalanan ke faskes lain | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 105 | 1083 | Observation | `Observation.valueCodeableConcept.coding` | LT000007 | Rumah Dukun | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 106 | 1093 | Condition | `Condition.code.coding` | 161805006 | Past pregnancy history of cesarean section | http://snomed.info/sct |
| 107 | 1094 | Condition | `Condition.code.coding` | 16356006 | Multiple pregnancy | http://snomed.info/sct |
| 108 | 1095 | Condition | `Condition.code.coding` | 109894007 | Retained placenta | http://snomed.info/sct |
| 109 | 1096 | Condition | `Condition.code.coding` | 237361005 | Antepartum fetal death | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 43 |
| http://loinc.org | 21 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 7 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 7 |
| http://terminology.kemkes.go.id/CodeSystem/organization-type | 7 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 6 |
|  | 4 |
| http://terminology.kemkes.go.id/sp | 3 |
| http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes | 3 |
| http://terminology.kemkes.go.id/CodeSystem/location-type | 3 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 2 |
| http://sys-ids.kemkes.go.id/kfa | 2 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 1 |
| **Total** | **109** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
