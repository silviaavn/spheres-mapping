# Output Form: SiGizi ANC

Sumber: `mapping/kobo-data-dictionary-sigizi-anc.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 66 |
| Code (`jumlah code` = 1) | 147 |
| Code unik (code + CodeSystem) | 114 |
| Variabel BQ (unik) | 47 |
| Variabel BQ di luar payload | 1 ⚠️ |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 8–37 | Patient | – | – | `nama` → `Patient.name.text` (8)<br>`nik` → `Patient.identifier.value` (12)<br>`tanggal_lahir` → `Patient.birthDate` (18)<br>`alamat_domisili` → `Patient.address.line` (21)<br>`kabkota_domisili` → `Patient.address.city` (23)<br>`prov_domisili` → `Patient.address.extension.extension.valueCode` (28)<br>`kabkota_domisili` → `Patient.address.extension.extension.valueCode` (31)<br>`kec_domisili` → `Patient.address.extension.extension.valueCode` (34)<br>`desakel_domisili` → `Patient.address.extension.extension.valueCode` (37)<br>`posyandu_domisili` → `Patient.managingOrganization.reference` (1026) |
| 2 | 85–91 | PractitionerRole | – | – | `pemeriksaan_anc_tenaga_pemeriksa` → `PractitionerRole.code.coding` (87) |
| 3 | 94–102 | EpisodeOfCare | ANC | Antenatal Care | `tanggal_hpht` → `EpisodeOfCare.statusHistory.period.start` (97) |
| 4 | 105–127 | Encounter | – | – | `pemeriksaan_pertama` → `Encounter.identifier` (106)<br>`pemeriksaan_anc_tanggal_anc` → `Encounter.period.start` (122)<br>`faskes_yang_melayani_anc` → `Encounter.location.display` (125) |
| 5 | 129–135 | Condition | 134435003 | Routine antenatal care | – |
| 6 | 150–161 | Observation | 424144002 | Current chronological age | `umur` → `Observation.valueQuantity.value` (153) |
| 7 | 164–175 | Observation | 8665-2 | Last menstrual period start date | `tanggal_hpht` → `Observation.valueDateTime` (168) |
| 8 | 177–188 | Observation | 11778-8 | Delivery date Estimated | `pemeriksaan_anc_tanggal_perkiraan_persalinan` → `Observation.valueDateTime` (181) |
| 9 | 190–202 | Observation | 8302-2 | Body height | `pemeriksaan_anc_tinggi` → `Observation.valueQuantity.value` (194) |
| 10 | 204–216 | Observation | OC000010 | Indeks Massa Tubuh Sebelum Hamil | `pemeriksaan_anc_imt_sebelum_hamil` → `Observation.valueQuantity.value` (208) |
| 11 | 218–249 | Immunization | VG139 | Td | `pemeriksaan_anc_riwayat_imun_tt_terakhir` → `Immunization.protocolApplied.doseNumberPositiveInt` (230) |
| 12 | 251–261 | Observation | SP000001 | Skrining Imunisasi Tetanus Toksoid | `pemeriksaan_anc_riwayat_imun_tt_terakhir` → `Observation.dataAbsentReason` (254) |
| 13 | 264–275 | Observation | SP000002 | Kunjungan Pertama Pemeriksaan Kehamilan | `pemeriksaan_pertama` → `Observation.valueBoolean` (267) |
| 14 | 278–290 | Observation | 29463-7 | Body weight | `pemeriksaan_anc_berat` → `Observation.valueQuantity.value` (282) |
| 15 | 292–304 | Observation | 392570002 | Blood pressure finding | `pemeriksaan_anc_tekanan_darah` → `Observation.valueCodeableConcept.coding` (295) |
| 16 | 306–321 | Observation | 284473002 | Mid upper arm circumference | `pemeriksaan_anc_lila` → `Observation.valueQuantity.value` (310)<br>`pemeriksaan_anc_status_gizi_kektidak_kek` → `Observation.interpretation.coding` (319) |
| 17 | 323–334 | Observation | 289625003 | Finding of fundal height of uterus | `pemeriksaan_anc_tfu` → `Observation.valueCodeableConcept.coding` (326) |
| 18 | 336–350 | Observation | 883-9 | ABO group [Type] in Blood | `pemeriksaan_anc_lab_golongan_darah` → `Observation.valueCodeableConcept.coding` (340) |
| 19 | 352–364 | Observation | 10331-7 | Rh [Type] in Blood | `pemeriksaan_anc_lab_rhesus` → `Observation.valueCodeableConcept.coding` (356) |
| 20 | 367–380 | Observation | 289437007 | Finding of fetal heart rate | `pemeriksaan_anc_djj` → `Observation.valueCodeableConcept.coding` (370) |
| 21 | 382–396 | Observation | 72155-5 | Position in womb Fetus [RHEA] | `pemeriksaan_anc_presentasi_janin` → `Observation.valueCodeableConcept.coding` (386) |
| 22 | 398–408 | Procedure | 88.78 | Diagnostic ultrasound of gravid uterus | `pemeriksaan_anc_diperiksa_usg` → `Procedure.status` (400) |
| 23 | 410–422 | Observation | 268445003 | Ultrasound scan - obstetric | `pemeriksaan_anc_diperiksa_usg` → `Observation.valueCodeableConcept.coding` (413) |
| 24 | 425–459 | MedicationRequest | 92000653 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula | `pemeriksaan_anc_jumlah_ttd_diterima` → `MedicationRequest.dispenseRequest.quantity.value` (458) |
| 25 | 461–493 | MedicationDispense | 93015491 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | `pemeriksaan_anc_jumlah_ttd_diterima` → `MedicationDispense.quantity.value` (491) |
| 26 | 495–517 | MedicationRequest | SP000370 | Multiple Micronutrient Supplement | `pemeriksaan_anc_jumlah_mms_diterima` → `MedicationRequest.dispenseRequest.quantity.value` (516) |
| 27 | 519–539 | MedicationDispense | SP000370 | Multiple Micronutrient Supplement | `pemeriksaan_anc_jumlah_mms_diterima` → `MedicationDispense.quantity.value` (537) |
| 28 | 543–552 | ServiceRequest | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | `pemeriksaan_anc_lab_hiv` → `ServiceRequest.code.coding` (547) |
| 29 | 554–557 | PractitionerRole | – | – | – |
| 30 | 559–566 | Specimen | 122555007 | Venous blood specimen | – |
| 31 | 568–581 | Observation | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | `pemeriksaan_anc_lab_hiv` → `Observation.valueCodeableConcept.coding` (572) |
| 32 | 583–594 | DiagnosticReport | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | – |
| 33 | 596–605 | ServiceRequest | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | `pemeriksaan_anc_lab_hepatitis` → `ServiceRequest.code.coding` (600) |
| 34 | 607–610 | PractitionerRole | – | – | – |
| 35 | 612–619 | Specimen | 122555007 | Venous blood specimen | – |
| 36 | 621–634 | Observation | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | `pemeriksaan_anc_lab_hepatitis` → `Observation.valueCodeableConcept.coding` (625) |
| 37 | 636–647 | DiagnosticReport | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | – |
| 38 | 649–658 | ServiceRequest | 22464-2 | Reagin Ab [Presence] in Specimen | `pemeriksaan_anc_lab_siphilis` → `ServiceRequest.code.coding` (653) |
| 39 | 660–663 | PractitionerRole | – | – | – |
| 40 | 665–672 | Specimen | 122555007 | Venous blood specimen | – |
| 41 | 674–687 | Observation | 22464-2 | Reagin Ab [Presence] in Specimen | `pemeriksaan_anc_lab_siphilis` → `Observation.valueCodeableConcept.coding` (678) |
| 42 | 689–700 | DiagnosticReport | 22464-2 | Reagin Ab [Presence] in Specimen | – |
| 43 | 702–711 | ServiceRequest | 2887-8 | Protein [Presence] in Urine | `pemeriksaan_anc_lab_protein_urine` → `ServiceRequest.code.coding` (706) |
| 44 | 713–716 | PractitionerRole | – | – | – |
| 45 | 718–725 | Specimen | 122575003 | Urine specimen | – |
| 46 | 727–740 | Observation | 2887-8 | Protein [Presence] in Urine | `pemeriksaan_anc_lab_protein_urine` → `Observation.valueCodeableConcept.coding` (731) |
| 47 | 742–753 | DiagnosticReport | 2887-8 | Protein [Presence] in Urine | – |
| 48 | 755–764 | ServiceRequest | 718-7 | Hemoglobin [Mass/volume] in Blood | `pemeriksaan_anc_lab_hb` → `ServiceRequest.code.coding` (759) |
| 49 | 766–769 | PractitionerRole | – | – | – |
| 50 | 771–778 | Specimen | 122555007 | Venous blood specimen | – |
| 51 | 780–813 | Observation | 718-7 | Hemoglobin [Mass/volume] in Blood | `pemeriksaan_anc_lab_hb` → `Observation.valueRange.low.value` (785) |
| 52 | 815–826 | DiagnosticReport | 718-7 | Hemoglobin [Mass/volume] in Blood | – |
| 53 | 828–837 | ServiceRequest | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | `pemeriksaan_anc_lab_gula_sewaktu` → `ServiceRequest.code.coding` (832) |
| 54 | 839–842 | PractitionerRole | – | – | – |
| 55 | 844–851 | Specimen | 122555007 | Venous blood specimen | – |
| 56 | 853–874 | Observation | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | `pemeriksaan_anc_lab_gula_sewaktu` → `Observation.valueRange.high.value` (858) |
| 57 | 876–887 | DiagnosticReport | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | – |
| 58 | 889–902 | Observation | 15220000 | Laboratory test | `pemeriksaan_anc_lab_lainnya` → `Observation.valueCodeableConcept.coding` (892) |
| 59 | 905–912 | Observation | SP000007 | Tatalaksana Anemia | `pemeriksaan_anc_tatalaksana_anemia` → `Observation.valueCodeableConcept.coding` (908) |
| 60 | 922–936 | Observation | SP000010 | Skrining Hipertensi dalam Kehamilan | `pemeriksaan_anc_pre_eklampsia` → `Observation.valueCodeableConcept.coding` (925) |
| 61 | 938–945 | Observation | SP000012 | Tatalaksana Pre Eklampsia | `pemeriksaan_anc_tatalaksana_pre_eklampsia` → `Observation.valueCodeableConcept.coding` (941) |
| 62 | 956–960 | Observation | SP000014 | Tatalaksana KEK | `pemeriksaan_anc_tatalaksana_kek` → `Observation.valueCodeableConcept.coding` (959) |
| 63 | 970–985 | Observation | SP000015 | Risiko Masalah Kesehatan | `pemeriksaan_anc_risiko_masalah_kesehatan_lainnya` → `Observation.valueCodeableConcept.coding` (973) |
| 64 | 987–998 | Observation | SP000016 | Tatalaksana Masalah Kesehatan | `pemeriksaan_anc_diberikan_tatalaksana_masalah_kesehatan_lainnya` → `Observation.valueBoolean` (990) |
| 65 | 1000–1010 | Procedure | 1230101008 | Counseling for pregnancy | `pemeriksaan_anc_konseling` → `Procedure.status` (1002) |
| 66 | 1012–1023 | Procedure | 385892002 | Mental health screening | `pemeriksaan_anc_skrinning_keswa` → `Procedure.status` (1014) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 29 |
| PractitionerRole | 7 |
| ServiceRequest | 6 |
| Specimen | 6 |
| DiagnosticReport | 6 |
| Procedure | 3 |
| MedicationRequest | 2 |
| MedicationDispense | 2 |
| Patient | 1 |
| EpisodeOfCare | 1 |
| Encounter | 1 |
| Condition | 1 |
| Immunization | 1 |
| **Total** | **66** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 87 | PractitionerRole | `PractitionerRole.code.coding` | 309453006 | Registered midwife | http://snomed.info/sct |
| 2 | 88 | PractitionerRole | `PractitionerRole.code.coding` | 309343006 | Physician | http://snomed.info/sct |
| 3 | 89 | PractitionerRole | `PractitionerRole.code.coding` | 309367003 | Obstetrician and gynecologist | http://snomed.info/sct |
| 4 | 90 | PractitionerRole | `PractitionerRole.code.coding` | 224535009 | Registered nurse | http://snomed.info/sct |
| 5 | 98 | EpisodeOfCare | `EpisodeOfCare.type.coding` | ANC | Antenatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 6 | 106 | Encounter | `Encounter.identifier` | K1M | Tidak ada | http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC |
| 7 | 107 | Encounter | `Encounter.identifier` | K1A | Tidak ada | http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC |
| 8 | 131 | Condition | `Condition.code.coding` | 134435003 | Routine antenatal care | http://snomed.info/sct |
| 9 | 152 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 10 | 166 | Observation | `Observation.code.coding` | 8665-2 | Last menstrual period start date | http://loinc.org |
| 11 | 167 | Observation | `Observation.code.coding` | ANC.B6.DE14 | Last menstrual period (LMP) date | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 12 | 179 | Observation | `Observation.code.coding` | 11778-8 | Delivery date Estimated | http://loinc.org |
| 13 | 180 | Observation | `Observation.code.coding` | ANC.B6.DE22 | Expected date of delivery (EDD) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 14 | 192 | Observation | `Observation.code.coding` | 8302-2 | Body height | http://loinc.org |
| 15 | 193 | Observation | `Observation.code.coding` | ANC.B8.DE1 | Height | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 16 | 206 | Observation | `Observation.code.coding` | OC000010 | Indeks Massa Tubuh Sebelum Hamil | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 17 | 207 | Observation | `Observation.code.coding` | ANC.SS.DE58 | IMT Sebelum Hamil | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 18 | 220 | Immunization | `Immunization.vaccineCode.coding` | VG139 | Td | http://sys-ids.kemkes.go.id/kfa |
| 19 | 253 | Observation | `Observation.code.coding` | SP000001 | Skrining Imunisasi Tetanus Toksoid | http://terminology.kemkes.go.id/sp |
| 20 | 266 | Observation | `Observation.code.coding` | SP000002 | Kunjungan Pertama Pemeriksaan Kehamilan | http://terminology.kemkes.go.id/sp |
| 21 | 280 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 22 | 281 | Observation | `Observation.code.coding` | ANC.B8.DE3 | Current weight | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 23 | 294 | Observation | `Observation.code.coding` | 392570002 | Blood pressure finding | http://snomed.info/sct |
| 24 | 295 | Observation | `Observation.valueCodeableConcept.coding` | 2004005 | Normal blood pressure | http://snomed.info/sct |
| 25 | 296 | Observation | `Observation.valueCodeableConcept.coding` | 38341003 | Hypertension | http://snomed.info/sct |
| 26 | 297 | Observation | `Observation.valueCodeableConcept.coding` | 45007003 | Hypotension | http://snomed.info/sct |
| 27 | 308 | Observation | `Observation.code.coding` | 284473002 | Mid upper arm circumference | http://snomed.info/sct |
| 28 | 309 | Observation | `Observation.code.coding` | ANC.SS.DE3 | Lingkar Lengan Atas (LILA) | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 29 | 319 | Observation | `Observation.interpretation.coding` | OI000018 | Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 30 | 320 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 31 | 321 | Observation | `Observation.interpretation.coding` | OI000035 | Risiko Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 32 | 325 | Observation | `Observation.code.coding` | 289625003 | Finding of fundal height of uterus | http://snomed.info/sct |
| 33 | 326 | Observation | `Observation.valueCodeableConcept.coding` | SP000003 | Sesuai Usia Kehamilan | http://terminology.kemkes.go.id/sp |
| 34 | 327 | Observation | `Observation.valueCodeableConcept.coding` | SP000004 | Tidak Sesuai Usia Kehamilan | http://terminology.kemkes.go.id/sp |
| 35 | 338 | Observation | `Observation.code.coding` | 883-9 | ABO group [Type] in Blood | http://loinc.org |
| 36 | 339 | Observation | `Observation.code.coding` | ANC.B9.DE24 | Blood type | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 37 | 340 | Observation | `Observation.valueCodeableConcept.coding` | LA19710-5 | Group A | http://loinc.org |
| 38 | 341 | Observation | `Observation.valueCodeableConcept.coding` | LA19709-7 | Group B | http://loinc.org |
| 39 | 342 | Observation | `Observation.valueCodeableConcept.coding` | LA19708-9 | Group O | http://loinc.org |
| 40 | 343 | Observation | `Observation.valueCodeableConcept.coding` | LA28449-9 | Group AB | http://loinc.org |
| 41 | 354 | Observation | `Observation.code.coding` | 10331-7 | Rh [Type] in Blood | http://loinc.org |
| 42 | 355 | Observation | `Observation.code.coding` | ANC.B9.DE29 | Rh factor | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 43 | 356 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 44 | 357 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 45 | 369 | Observation | `Observation.code.coding` | 289437007 | Finding of fetal heart rate | http://snomed.info/sct |
| 46 | 370 | Observation | `Observation.valueCodeableConcept.coding` | 289441006 | Normal fetal heart rate | http://snomed.info/sct |
| 47 | 371 | Observation | `Observation.valueCodeableConcept.coding` | 289440007 | Fetal heart rate not observed | http://snomed.info/sct |
| 48 | 372 | Observation | `Observation.valueCodeableConcept.coding` | 312668007 | Abnormal fetal heart rate | http://snomed.info/sct |
| 49 | 373 | Observation | `Observation.valueCodeableConcept.coding` | 289439005 | Fetal heart rate absent | http://snomed.info/sct |
| 50 | 384 | Observation | `Observation.code.coding` | 72155-5 | Position in womb Fetus [RHEA] | http://loinc.org |
| 51 | 385 | Observation | `Observation.code.coding` | ANC.B8.DE111 | Fetal presentation | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 52 | 386 | Observation | `Observation.valueCodeableConcept.coding` | 1209182005 | Cephalic fetal presentation | http://snomed.info/sct |
| 53 | 387 | Observation | `Observation.valueCodeableConcept.coding` | SP000005 | Letak Bokong/ Lintang | http://terminology.kemkes.go.id/sp |
| 54 | 388 | Observation | `Observation.valueCodeableConcept.coding` | SP000006 | Organ Tubuh Lainnya | http://terminology.kemkes.go.id/sp |
| 55 | 399 | Procedure | `Procedure.code.coding` | 88.78 | Diagnostic ultrasound of gravid uterus | http://hl7.org/fhir/sid/icd-9-cm |
| 56 | 412 | Observation | `Observation.code.coding` | 268445003 | Ultrasound scan - obstetric | http://snomed.info/sct |
| 57 | 413 | Observation | `Observation.valueCodeableConcept.coding` | 169221005 | Ultrasound obstetric scan normal | http://snomed.info/sct |
| 58 | 414 | Observation | `Observation.valueCodeableConcept.coding` | 169255008 | Ultrasound scan abnormal | http://snomed.info/sct |
| 59 | 428 | MedicationRequest | `MedicationRequest.contained.code.coding` | 92000653 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula | http://sys-ids.kemkes.go.id/kfa |
| 60 | 464 | MedicationDispense | `MedicationDispense.contained.code.coding` | 93015491 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | http://sys-ids.kemkes.go.id/kfa |
| 61 | 498 | MedicationRequest | `MedicationRequest.contained.code.coding` | SP000370 | Multiple Micronutrient Supplement | http://terminology.kemkes.go.id/sp |
| 62 | 522 | MedicationDispense | `MedicationDispense.contained.code.coding` | SP000370 | Multiple Micronutrient Supplement | http://terminology.kemkes.go.id/sp |
| 63 | 547 | ServiceRequest | `ServiceRequest.code.coding` | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 64 | 556 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002 | Laboratory worker | http://snomed.info/sct |
| 65 | 560 | Specimen | `Specimen.type.coding` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 66 | 570 | Observation | `Observation.code.coding` | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 67 | 571 | Observation | `Observation.code.coding` | ANC.B9.DE32 | HIV test | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 68 | 572 | Observation | `Observation.valueCodeableConcept.coding` | LA15255-5 | Reactive | http://loinc.org |
| 69 | 573 | Observation | `Observation.valueCodeableConcept.coding` | LA15256-3 | Nonreactive | http://loinc.org |
| 70 | 585 | DiagnosticReport | `DiagnosticReport.code.coding` | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 71 | 600 | ServiceRequest | `ServiceRequest.code.coding` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 72 | 609 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002 | Laboratory worker | http://snomed.info/sct |
| 73 | 613 | Specimen | `Specimen.type.coding` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 74 | 623 | Observation | `Observation.code.coding` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 75 | 624 | Observation | `Observation.code.coding` | ANC.B9.DE60 | Hepatitis B test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 76 | 625 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 77 | 626 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 78 | 638 | DiagnosticReport | `DiagnosticReport.code.coding` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 79 | 653 | ServiceRequest | `ServiceRequest.code.coding` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 80 | 662 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002 | Laboratory worker | http://snomed.info/sct |
| 81 | 666 | Specimen | `Specimen.type.coding` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 82 | 676 | Observation | `Observation.code.coding` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 83 | 677 | Observation | `Observation.code.coding` | ANC.B9.DE96 | Syphilis test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 84 | 678 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 85 | 679 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 86 | 691 | DiagnosticReport | `DiagnosticReport.code.coding` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 87 | 706 | ServiceRequest | `ServiceRequest.code.coding` | 2887-8 | Protein [Presence] in Urine | http://loinc.org |
| 88 | 715 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002 | Laboratory worker | http://snomed.info/sct |
| 89 | 719 | Specimen | `Specimen.type.coding` | 122575003 | Urine specimen | http://snomed.info/sct |
| 90 | 729 | Observation | `Observation.code.coding` | 2887-8 | Protein [Presence] in Urine | http://loinc.org |
| 91 | 730 | Observation | `Observation.code.coding` | ANC.B9.DE114 | Urine test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 92 | 731 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 93 | 732 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 94 | 744 | DiagnosticReport | `DiagnosticReport.code.coding` | 2887-8 | Protein [Presence] in Urine | http://loinc.org |
| 95 | 759 | ServiceRequest | `ServiceRequest.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 96 | 768 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002 | Laboratory worker | http://snomed.info/sct |
| 97 | 772 | Specimen | `Specimen.type.coding` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 98 | 782 | Observation | `Observation.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 99 | 783 | Observation | `Observation.code.coding` | ANC.B9.DE175 | Blood hemoglobin test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 100 | 787 | Observation | `Observation.interpretation.coding` | 860635002 | No anemia present | http://snomed.info/sct |
| 101 | 793 | Observation | `Observation.interpretation.coding` | OI000032 | Anemia ringan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 102 | 799 | Observation | `Observation.interpretation.coding` | OI000033 | Anemia sedang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 103 | 803 | Observation | `Observation.interpretation.coding` | what do yo eeeee | Anemia berat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 104 | 817 | DiagnosticReport | `DiagnosticReport.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 105 | 832 | ServiceRequest | `ServiceRequest.code.coding` | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | http://loinc.org |
| 106 | 841 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002 | Laboratory worker | http://snomed.info/sct |
| 107 | 845 | Specimen | `Specimen.type.coding` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 108 | 855 | Observation | `Observation.code.coding` | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | http://loinc.org |
| 109 | 856 | Observation | `Observation.code.coding` | ANC.B9.DE159 | Blood glucose test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 110 | 860 | Observation | `Observation.interpretation.coding` | 166921001 | Blood glucose normal | http://snomed.info/sct |
| 111 | 864 | Observation | `Observation.interpretation.coding` | 166922008 | Blood glucose abnormal | http://snomed.info/sct |
| 112 | 878 | DiagnosticReport | `DiagnosticReport.code.coding` | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | http://loinc.org |
| 113 | 891 | Observation | `Observation.code.coding` | 15220000 | Laboratory test | http://snomed.info/sct |
| 114 | 892 | Observation | `Observation.valueCodeableConcept.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 115 | 893 | Observation | `Observation.valueCodeableConcept.coding` | 76772-3 | Plasmodium falciparum Ag [Presence] in Blood by Rapid immunoassay | http://loinc.org |
| 116 | 894 | Observation | `Observation.valueCodeableConcept.coding` | 104742-2 | Ova and parasites identified in Specimen | http://loinc.org |
| 117 | 895 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 118 | 907 | Observation | `Observation.code.coding` | SP000007 | Tatalaksana Anemia | http://terminology.kemkes.go.id/sp |
| 119 | 908 | Observation | `Observation.valueCodeableConcept.coding` | SP000008 | Pemberian Tablet Tambah Darah | http://terminology.kemkes.go.id/sp |
| 120 | 909 | Observation | `Observation.valueCodeableConcept.coding` | SP000009 | Pemberian Fe Parenteral | http://terminology.kemkes.go.id/sp |
| 121 | 910 | Observation | `Observation.valueCodeableConcept.coding` | 116859006 | Transfusion of blood product | http://snomed.info/sct |
| 122 | 911 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 123 | 912 | Observation | `Observation.valueCodeableConcept.coding` | 3457005 | Patient referral | http://snomed.info/sct |
| 124 | 924 | Observation | `Observation.code.coding` | SP000010 | Skrining Hipertensi dalam Kehamilan | http://terminology.kemkes.go.id/sp |
| 125 | 925 | Observation | `Observation.valueCodeableConcept.coding` | SP000011 | Tidak Pre Eklampsia/ Eklampsia | http://terminology.kemkes.go.id/sp |
| 126 | 926 | Observation | `Observation.valueCodeableConcept.coding` | 48194001 | Pregnancy-induced hypertension | http://snomed.info/sct |
| 127 | 927 | Observation | `Observation.valueCodeableConcept.coding` | 398254007 | Pre-eclampsia | http://snomed.info/sct |
| 128 | 928 | Observation | `Observation.valueCodeableConcept.coding` | 15938005 | Eclampsia | http://snomed.info/sct |
| 129 | 940 | Observation | `Observation.code.coding` | SP000012 | Tatalaksana Pre Eklampsia | http://terminology.kemkes.go.id/sp |
| 130 | 941 | Observation | `Observation.valueCodeableConcept.coding` | 135840009 | Blood pressure monitoring | http://snomed.info/sct |
| 131 | 942 | Observation | `Observation.valueCodeableConcept.coding` | 308116003 | Antihypertensive therapy | http://snomed.info/sct |
| 132 | 943 | Observation | `Observation.valueCodeableConcept.coding` | SP000013 | Pemberian MgSO4 | http://terminology.kemkes.go.id/sp |
| 133 | 944 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 134 | 945 | Observation | `Observation.valueCodeableConcept.coding` | 3457005 | Patient referral | http://snomed.info/sct |
| 135 | 958 | Observation | `Observation.code.coding` | SP000014 | Tatalaksana KEK | http://terminology.kemkes.go.id/sp |
| 136 | 959 | Observation | `Observation.valueCodeableConcept.coding` | 435591000124104 | Nutrition supplement therapy | http://snomed.info/sct |
| 137 | 960 | Observation | `Observation.valueCodeableConcept.coding` | 3457005 | Patient referral | http://snomed.info/sct |
| 138 | 972 | Observation | `Observation.code.coding` | SP000015 | Risiko Masalah Kesehatan | http://terminology.kemkes.go.id/sp |
| 139 | 973 | Observation | `Observation.valueCodeableConcept.coding` | 40733004 | Infectious disease | http://snomed.info/sct |
| 140 | 974 | Observation | `Observation.valueCodeableConcept.coding` | 73211009 | Diabetes mellitus | http://snomed.info/sct |
| 141 | 975 | Observation | `Observation.valueCodeableConcept.coding` | 414916001 | Obesity | http://snomed.info/sct |
| 142 | 976 | Observation | `Observation.valueCodeableConcept.coding` | 56717001 | Tuberculosis | http://snomed.info/sct |
| 143 | 977 | Observation | `Observation.valueCodeableConcept.coding` | 56265001 | Heart disease | http://snomed.info/sct |
| 144 | 978 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 145 | 989 | Observation | `Observation.code.coding` | SP000016 | Tatalaksana Masalah Kesehatan | http://terminology.kemkes.go.id/sp |
| 146 | 1001 | Procedure | `Procedure.code.coding` | 1230101008 | Counseling for pregnancy | http://snomed.info/sct |
| 147 | 1013 | Procedure | `Procedure.code.coding` | 385892002 | Mental health screening | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah | Code |
|---|---|---|
| http://snomed.info/sct | 58 | 309453006, 309343006, 309367003, 224535009, 134435003, 424144002, 392570002, 2004005, 38341003, 45007003, 284473002, 289625003, 289437007, 289441006, 289440007, 312668007, 289439005, 1209182005, 268445003, 169221005, 169255008, 1290220002, 122555007, 1290220002, 122555007, 1290220002, 122555007, 1290220002, 122575003, 1290220002, 122555007, 860635002, 1290220002, 122555007, 166921001, 166922008, 15220000, 74964007, 116859006, 74964007, 3457005, 48194001, 398254007, 15938005, 135840009, 308116003, 74964007, 3457005, 435591000124104, 3457005, 40733004, 73211009, 414916001, 56717001, 56265001, 74964007, 1230101008, 385892002 |
| http://loinc.org | 42 | 8665-2, 11778-8, 8302-2, 29463-7, 883-9, LA19710-5, LA19709-7, LA19708-9, LA28449-9, 10331-7, LA6576-8, LA6577-6, 72155-5, 68961-2, 68961-2, LA15255-5, LA15256-3, 68961-2, 75410-1, 75410-1, LA6576-8, LA6577-6, 75410-1, 22464-2, 22464-2, LA6576-8, LA6577-6, 22464-2, 2887-8, 2887-8, LA6576-8, LA6577-6, 2887-8, 718-7, 718-7, 718-7, 74774-1, 74774-1, 74774-1, 88874-3, 76772-3, 104742-2 |
| http://terminology.kemkes.go.id/sp | 18 | SP000001, SP000002, SP000003, SP000004, SP000005, SP000006, SP000370, SP000370, SP000007, SP000008, SP000009, SP000010, SP000011, SP000012, SP000013, SP000014, SP000015, SP000016 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 13 | ANC.B6.DE14, ANC.B6.DE22, ANC.B8.DE1, ANC.B8.DE3, ANC.B9.DE24, ANC.B9.DE29, ANC.B8.DE111, ANC.B9.DE32, ANC.B9.DE60, ANC.B9.DE96, ANC.B9.DE114, ANC.B9.DE175, ANC.B9.DE159 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 6 | OC000010, OI000018, OI000035, OI000032, OI000033, what do yo eeeee |
| http://sys-ids.kemkes.go.id/kfa | 3 | VG139, 92000653, 93015491 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC | 2 | K1M, K1A |
| http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes | 2 | ANC.SS.DE58, ANC.SS.DE3 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 1 | ANC |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 1 | N |
| http://hl7.org/fhir/sid/icd-9-cm | 1 | 88.78 |
| **Total** | **147** | |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel Kobo | Resource | Path |
|---|---|---|---|---|
| 43 | ⚠️ faskes_yang_melayani_anc | Faskes yang melayani ANC | Organization | `Organization.name` |
| 1047 | ⚠️ puskesmas_domisili | Puskesmas Domisili | Organization | `Organization.partOf` |
