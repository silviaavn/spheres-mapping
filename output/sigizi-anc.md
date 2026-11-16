# Output Form: SiGizi ANC

Sumber: `mapping/phdt-data-dictionary-sigizi-anc.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 61 |
| Code (`jumlah code` = 1) | 142 |
| Code unik (code + CodeSystem) | 114 |
| Variabel BQ (unik) | 49 |
| Variabel di Excel export | 49 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 8–37 | Patient | – | – | `nama` → `Patient.name.text` (8)<br>`nik` → `Patient.identifier.value` (12)<br>`tanggal_lahir` → `Patient.birthDate` (18)<br>`alamat_domisili` → `Patient.address.line` (21)<br>`kabkota_domisili` → `Patient.address.city` (23)<br>`prov_domisili` → `Patient.address.extension.extension.valueCode` (28)<br>`kabkota_domisili` → `Patient.address.extension.extension.valueCode` (31)<br>`kec_domisili` → `Patient.address.extension.extension.valueCode` (34)<br>`desakel_domisili` → `Patient.address.extension.extension.valueCode` (37)<br>`posyandu_domisili` → `Patient.managingOrganization.reference` (967) 🔎 lookup master data<br>`puskesmas_domisili` → `Patient.managingOrganization.reference` (968) 🔎 lookup master data |
| 2 | 41–47 | PractitionerRole | – | – | `pemeriksaan_anc_tenaga_pemeriksa` → `PractitionerRole.code.coding` (43) |
| 3 | 50–58 | EpisodeOfCare | ANC | Antenatal Care | `tanggal_hpht` → `EpisodeOfCare.statusHistory.period.start` (53) |
| 4 | 61–85 | Encounter | – | – | `pemeriksaan_pertama` → `Encounter.identifier` (62)<br>`pemeriksaan_anc_tanggal_anc` → `Encounter.period.start` (78)<br>`faskes_yang_melayani_anc` → `Encounter.location.display` (81)<br>`pemeriksaan_anc_aksi` → `Encounter.extension.valueUrl` (85)<br>`faskes_yang_melayani_anc` → `Encounter.serviceProvider.reference` (105) 🔎 lookup master data |
| 5 | 87–93 | Condition | 134435003 | Routine antenatal care | – |
| 6 | 108–119 | Observation | 424144002 | Current chronological age | `umur` → `Observation.valueQuantity.value` (111) |
| 7 | 122–133 | Observation | 8665-2 | Last menstrual period start date | `tanggal_hpht` → `Observation.valueDateTime` (126) |
| 8 | 135–146 | Observation | 18185-9 | Gestational age | `pemeriksaan_anc_usia_kehamilan` → `Observation.valueQuantity.value` (138) |
| 9 | 148–159 | Observation | 11778-8 | Delivery date Estimated | `pemeriksaan_anc_tanggal_perkiraan_persalinan` → `Observation.valueDateTime` (152) |
| 10 | 161–173 | Observation | 8302-2 | Body height | `pemeriksaan_anc_tinggi` → `Observation.valueQuantity.value` (165) |
| 11 | 175–187 | Observation | OC000010 | Indeks Massa Tubuh Sebelum Hamil | `pemeriksaan_anc_imt_sebelum_hamil` → `Observation.valueQuantity.value` (179) |
| 12 | 189–220 | Immunization | VG139 | Td | `pemeriksaan_anc_riwayat_imun_tt_terakhir` → `Immunization.protocolApplied.doseNumberPositiveInt` (201) |
| 13 | 222–232 | Observation | SP000001 | Skrining Imunisasi Tetanus Toksoid | `pemeriksaan_anc_riwayat_imun_tt_terakhir` → `Observation.dataAbsentReason` (225) |
| 14 | 235–246 | Observation | SP000002 | Kunjungan Pertama Pemeriksaan Kehamilan | `pemeriksaan_pertama` → `Observation.valueBoolean` (238) |
| 15 | 249–261 | Observation | 29463-7 | Body weight | `pemeriksaan_anc_berat` → `Observation.valueQuantity.value` (253) |
| 16 | 263–275 | Observation | 392570002 | Blood pressure finding | `pemeriksaan_anc_tekanan_darah` → `Observation.valueCodeableConcept.coding` (266) |
| 17 | 277–292 | Observation | 284473002 | Mid upper arm circumference | `pemeriksaan_anc_lila` → `Observation.valueQuantity.value` (281)<br>`pemeriksaan_anc_status_gizi_kektidak_kek` → `Observation.interpretation.coding` (290) |
| 18 | 294–305 | Observation | 289625003 | Finding of fundal height of uterus | `pemeriksaan_anc_tfu` → `Observation.valueCodeableConcept.coding` (297) |
| 19 | 307–321 | Observation | 883-9 | ABO group [Type] in Blood | `pemeriksaan_anc_lab_golongan_darah` → `Observation.valueCodeableConcept.coding` (311) |
| 20 | 323–335 | Observation | 10331-7 | Rh [Type] in Blood | `pemeriksaan_anc_lab_rhesus` → `Observation.valueCodeableConcept.coding` (327) |
| 21 | 338–351 | Observation | 289437007 | Finding of fetal heart rate | `pemeriksaan_anc_djj` → `Observation.valueCodeableConcept.coding` (341) |
| 22 | 353–367 | Observation | 72155-5 | Position in womb Fetus [RHEA] | `pemeriksaan_anc_presentasi_janin` → `Observation.valueCodeableConcept.coding` (357) |
| 23 | 369–379 | Procedure | 88.78 | Diagnostic ultrasound of gravid uterus | `pemeriksaan_anc_diperiksa_usg` → `Procedure.status` (371) |
| 24 | 381–393 | Observation | 268445003 | Ultrasound scan - obstetric | `pemeriksaan_anc_diperiksa_usg` → `Observation.valueCodeableConcept.coding` (384) |
| 25 | 396–430 | MedicationRequest | 92000653 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula | `pemeriksaan_anc_jumlah_ttd_diterima` → `MedicationRequest.dispenseRequest.quantity.value` (429) |
| 26 | 432–464 | MedicationDispense | 93015491 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | `pemeriksaan_anc_jumlah_ttd_diterima` → `MedicationDispense.quantity.value` (462) |
| 27 | 466–488 | MedicationRequest | SP000370 | Multiple Micronutrient Supplement | `pemeriksaan_anc_jumlah_mms_diterima` → `MedicationRequest.dispenseRequest.quantity.value` (487) |
| 28 | 490–510 | MedicationDispense | SP000370 | Multiple Micronutrient Supplement | `pemeriksaan_anc_jumlah_mms_diterima` → `MedicationDispense.quantity.value` (508) |
| 29 | 514–523 | ServiceRequest | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | `pemeriksaan_anc_lab_hiv` → `ServiceRequest.code.coding` (518) |
| 30 | 525–532 | Specimen | 122555007 | Venous blood specimen | – |
| 31 | 534–547 | Observation | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | `pemeriksaan_anc_lab_hiv` → `Observation.valueCodeableConcept.coding` (538) |
| 32 | 549–560 | DiagnosticReport | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | – |
| 33 | 562–571 | ServiceRequest | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | `pemeriksaan_anc_lab_hepatitis` → `ServiceRequest.code.coding` (566) |
| 34 | 573–580 | Specimen | 122555007 | Venous blood specimen | – |
| 35 | 582–595 | Observation | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | `pemeriksaan_anc_lab_hepatitis` → `Observation.valueCodeableConcept.coding` (586) |
| 36 | 597–608 | DiagnosticReport | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | – |
| 37 | 610–619 | ServiceRequest | 22464-2 | Reagin Ab [Presence] in Specimen | `pemeriksaan_anc_lab_siphilis` → `ServiceRequest.code.coding` (614) |
| 38 | 621–628 | Specimen | 122555007 | Venous blood specimen | – |
| 39 | 630–643 | Observation | 22464-2 | Reagin Ab [Presence] in Specimen | `pemeriksaan_anc_lab_siphilis` → `Observation.valueCodeableConcept.coding` (634) |
| 40 | 645–656 | DiagnosticReport | 22464-2 | Reagin Ab [Presence] in Specimen | – |
| 41 | 658–667 | ServiceRequest | 2887-8 | Protein [Presence] in Urine | `pemeriksaan_anc_lab_protein_urine` → `ServiceRequest.code.coding` (662) |
| 42 | 669–676 | Specimen | 122575003 | Urine specimen | – |
| 43 | 678–691 | Observation | 2887-8 | Protein [Presence] in Urine | `pemeriksaan_anc_lab_protein_urine` → `Observation.valueCodeableConcept.coding` (682) |
| 44 | 693–704 | DiagnosticReport | 2887-8 | Protein [Presence] in Urine | – |
| 45 | 706–715 | ServiceRequest | 718-7 | Hemoglobin [Mass/volume] in Blood | `pemeriksaan_anc_lab_hb` → `ServiceRequest.code.coding` (710) |
| 46 | 717–724 | Specimen | 122555007 | Venous blood specimen | – |
| 47 | 726–759 | Observation | 718-7 | Hemoglobin [Mass/volume] in Blood | `pemeriksaan_anc_lab_hb` → `Observation.valueRange.low.value` (731) |
| 48 | 761–772 | DiagnosticReport | 718-7 | Hemoglobin [Mass/volume] in Blood | – |
| 49 | 774–783 | ServiceRequest | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | `pemeriksaan_anc_lab_gula_sewaktu` → `ServiceRequest.code.coding` (778) |
| 50 | 785–792 | Specimen | 122555007 | Venous blood specimen | – |
| 51 | 794–815 | Observation | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | `pemeriksaan_anc_lab_gula_sewaktu` → `Observation.valueRange.high.value` (799) |
| 52 | 817–828 | DiagnosticReport | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | – |
| 53 | 830–843 | Observation | 15220000 | Laboratory test | `pemeriksaan_anc_lab_lainnya` → `Observation.valueCodeableConcept.coding` (833) |
| 54 | 846–853 | Observation | SP000007 | Tatalaksana Anemia | `pemeriksaan_anc_tatalaksana_anemia` → `Observation.valueCodeableConcept.coding` (849) |
| 55 | 863–877 | Observation | SP000010 | Skrining Hipertensi dalam Kehamilan | `pemeriksaan_anc_pre_eklampsia` → `Observation.valueCodeableConcept.coding` (866) |
| 56 | 879–886 | Observation | SP000012 | Tatalaksana Pre Eklampsia | `pemeriksaan_anc_tatalaksana_pre_eklampsia` → `Observation.valueCodeableConcept.coding` (882) |
| 57 | 897–901 | Observation | SP000014 | Tatalaksana KEK | `pemeriksaan_anc_tatalaksana_kek` → `Observation.valueCodeableConcept.coding` (900) |
| 58 | 911–926 | Observation | SP000015 | Risiko Masalah Kesehatan | `pemeriksaan_anc_risiko_masalah_kesehatan_lainnya` → `Observation.valueCodeableConcept.coding` (914) |
| 59 | 928–939 | Observation | SP000016 | Tatalaksana Masalah Kesehatan | `pemeriksaan_anc_diberikan_tatalaksana_masalah_kesehatan_lainnya` → `Observation.valueBoolean` (931) |
| 60 | 941–951 | Procedure | 1230101008 | Counseling for pregnancy | `pemeriksaan_anc_konseling` → `Procedure.status` (943) |
| 61 | 953–964 | Procedure | 385892002 | Mental health screening | `pemeriksaan_anc_skrinning_keswa` → `Procedure.status` (955) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 30 |
| ServiceRequest | 6 |
| Specimen | 6 |
| DiagnosticReport | 6 |
| Procedure | 3 |
| MedicationRequest | 2 |
| MedicationDispense | 2 |
| Patient | 1 |
| PractitionerRole | 1 |
| EpisodeOfCare | 1 |
| Encounter | 1 |
| Condition | 1 |
| Immunization | 1 |
| **Total** | **61** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 43 | PractitionerRole | `PractitionerRole.code.coding` | 309453006 | Registered midwife | http://snomed.info/sct |
| 2 | 44 | PractitionerRole | `PractitionerRole.code.coding` | 309343006 | Physician | http://snomed.info/sct |
| 3 | 45 | PractitionerRole | `PractitionerRole.code.coding` | 309367003 | Obstetrician and gynecologist | http://snomed.info/sct |
| 4 | 46 | PractitionerRole | `PractitionerRole.code.coding` | 224535009 | Registered nurse | http://snomed.info/sct |
| 5 | 54 | EpisodeOfCare | `EpisodeOfCare.type.coding` | ANC | Antenatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 6 | 62 | Encounter | `Encounter.identifier` | K1M | Tidak ada | http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC |
| 7 | 63 | Encounter | `Encounter.identifier` | K1A | Tidak ada | http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC |
| 8 | 89 | Condition | `Condition.code.coding` | 134435003 | Routine antenatal care | http://snomed.info/sct |
| 9 | 110 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 10 | 124 | Observation | `Observation.code.coding` | 8665-2 | Last menstrual period start date | http://loinc.org |
| 11 | 125 | Observation | `Observation.code.coding` | ANC.B6.DE14 | Last menstrual period (LMP) date | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 12 | 137 | Observation | `Observation.code.coding` | 18185-9 | Gestational age | http://loinc.org |
| 13 | 150 | Observation | `Observation.code.coding` | 11778-8 | Delivery date Estimated | http://loinc.org |
| 14 | 151 | Observation | `Observation.code.coding` | ANC.B6.DE22 | Expected date of delivery (EDD) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 15 | 163 | Observation | `Observation.code.coding` | 8302-2 | Body height | http://loinc.org |
| 16 | 164 | Observation | `Observation.code.coding` | ANC.B8.DE1 | Height | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 17 | 177 | Observation | `Observation.code.coding` | OC000010 | Indeks Massa Tubuh Sebelum Hamil | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 18 | 178 | Observation | `Observation.code.coding` | ANC.SS.DE58 | IMT Sebelum Hamil | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 19 | 191 | Immunization | `Immunization.vaccineCode.coding` | VG139 | Td | http://sys-ids.kemkes.go.id/kfa |
| 20 | 224 | Observation | `Observation.code.coding` | SP000001 | Skrining Imunisasi Tetanus Toksoid | http://terminology.kemkes.go.id/sp |
| 21 | 237 | Observation | `Observation.code.coding` | SP000002 | Kunjungan Pertama Pemeriksaan Kehamilan | http://terminology.kemkes.go.id/sp |
| 22 | 251 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 23 | 252 | Observation | `Observation.code.coding` | ANC.B8.DE3 | Current weight | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 24 | 265 | Observation | `Observation.code.coding` | 392570002 | Blood pressure finding | http://snomed.info/sct |
| 25 | 266 | Observation | `Observation.valueCodeableConcept.coding` | 2004005 | Normal blood pressure | http://snomed.info/sct |
| 26 | 267 | Observation | `Observation.valueCodeableConcept.coding` | 38341003 | Hypertension | http://snomed.info/sct |
| 27 | 268 | Observation | `Observation.valueCodeableConcept.coding` | 45007003 | Hypotension | http://snomed.info/sct |
| 28 | 279 | Observation | `Observation.code.coding` | 284473002 | Mid upper arm circumference | http://snomed.info/sct |
| 29 | 280 | Observation | `Observation.code.coding` | ANC.SS.DE3 | Lingkar Lengan Atas (LILA) | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 30 | 290 | Observation | `Observation.interpretation.coding` | OI000018 | Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 31 | 291 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 32 | 292 | Observation | `Observation.interpretation.coding` | OI000035 | Risiko Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 33 | 296 | Observation | `Observation.code.coding` | 289625003 | Finding of fundal height of uterus | http://snomed.info/sct |
| 34 | 297 | Observation | `Observation.valueCodeableConcept.coding` | SP000003 | Sesuai Usia Kehamilan | http://terminology.kemkes.go.id/sp |
| 35 | 298 | Observation | `Observation.valueCodeableConcept.coding` | SP000004 | Tidak Sesuai Usia Kehamilan | http://terminology.kemkes.go.id/sp |
| 36 | 309 | Observation | `Observation.code.coding` | 883-9 | ABO group [Type] in Blood | http://loinc.org |
| 37 | 310 | Observation | `Observation.code.coding` | ANC.B9.DE24 | Blood type | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 38 | 311 | Observation | `Observation.valueCodeableConcept.coding` | LA19710-5 | Group A | http://loinc.org |
| 39 | 312 | Observation | `Observation.valueCodeableConcept.coding` | LA19709-7 | Group B | http://loinc.org |
| 40 | 313 | Observation | `Observation.valueCodeableConcept.coding` | LA19708-9 | Group O | http://loinc.org |
| 41 | 314 | Observation | `Observation.valueCodeableConcept.coding` | LA28449-9 | Group AB | http://loinc.org |
| 42 | 325 | Observation | `Observation.code.coding` | 10331-7 | Rh [Type] in Blood | http://loinc.org |
| 43 | 326 | Observation | `Observation.code.coding` | ANC.B9.DE29 | Rh factor | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 44 | 327 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 45 | 328 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 46 | 340 | Observation | `Observation.code.coding` | 289437007 | Finding of fetal heart rate | http://snomed.info/sct |
| 47 | 341 | Observation | `Observation.valueCodeableConcept.coding` | 289441006 | Normal fetal heart rate | http://snomed.info/sct |
| 48 | 342 | Observation | `Observation.valueCodeableConcept.coding` | 289440007 | Fetal heart rate not observed | http://snomed.info/sct |
| 49 | 343 | Observation | `Observation.valueCodeableConcept.coding` | 312668007 | Abnormal fetal heart rate | http://snomed.info/sct |
| 50 | 344 | Observation | `Observation.valueCodeableConcept.coding` | 289439005 | Fetal heart rate absent | http://snomed.info/sct |
| 51 | 355 | Observation | `Observation.code.coding` | 72155-5 | Position in womb Fetus [RHEA] | http://loinc.org |
| 52 | 356 | Observation | `Observation.code.coding` | ANC.B8.DE111 | Fetal presentation | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 53 | 357 | Observation | `Observation.valueCodeableConcept.coding` | 1209182005 | Cephalic fetal presentation | http://snomed.info/sct |
| 54 | 358 | Observation | `Observation.valueCodeableConcept.coding` | SP000005 | Letak Bokong/ Lintang | http://terminology.kemkes.go.id/sp |
| 55 | 359 | Observation | `Observation.valueCodeableConcept.coding` | SP000006 | Organ Tubuh Lainnya | http://terminology.kemkes.go.id/sp |
| 56 | 370 | Procedure | `Procedure.code.coding` | 88.78 | Diagnostic ultrasound of gravid uterus | http://hl7.org/fhir/sid/icd-9-cm |
| 57 | 383 | Observation | `Observation.code.coding` | 268445003 | Ultrasound scan - obstetric | http://snomed.info/sct |
| 58 | 384 | Observation | `Observation.valueCodeableConcept.coding` | 169221005 | Ultrasound obstetric scan normal | http://snomed.info/sct |
| 59 | 385 | Observation | `Observation.valueCodeableConcept.coding` | 169255008 | Ultrasound scan abnormal | http://snomed.info/sct |
| 60 | 399 | MedicationRequest | `MedicationRequest.contained.code.coding` | 92000653 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula | http://sys-ids.kemkes.go.id/kfa |
| 61 | 435 | MedicationDispense | `MedicationDispense.contained.code.coding` | 93015491 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | http://sys-ids.kemkes.go.id/kfa |
| 62 | 469 | MedicationRequest | `MedicationRequest.contained.code.coding` | SP000370 | Multiple Micronutrient Supplement | http://terminology.kemkes.go.id/sp |
| 63 | 493 | MedicationDispense | `MedicationDispense.contained.code.coding` | SP000370 | Multiple Micronutrient Supplement | http://terminology.kemkes.go.id/sp |
| 64 | 518 | ServiceRequest | `ServiceRequest.code.coding` | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 65 | 526 | Specimen | `Specimen.type.coding` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 66 | 536 | Observation | `Observation.code.coding` | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 67 | 537 | Observation | `Observation.code.coding` | ANC.B9.DE32 | HIV test | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 68 | 538 | Observation | `Observation.valueCodeableConcept.coding` | LA15255-5 | Reactive | http://loinc.org |
| 69 | 539 | Observation | `Observation.valueCodeableConcept.coding` | LA15256-3 | Nonreactive | http://loinc.org |
| 70 | 551 | DiagnosticReport | `DiagnosticReport.code.coding` | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 71 | 566 | ServiceRequest | `ServiceRequest.code.coding` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 72 | 574 | Specimen | `Specimen.type.coding` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 73 | 584 | Observation | `Observation.code.coding` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 74 | 585 | Observation | `Observation.code.coding` | ANC.B9.DE60 | Hepatitis B test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 75 | 586 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 76 | 587 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 77 | 599 | DiagnosticReport | `DiagnosticReport.code.coding` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 78 | 614 | ServiceRequest | `ServiceRequest.code.coding` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 79 | 622 | Specimen | `Specimen.type.coding` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 80 | 632 | Observation | `Observation.code.coding` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 81 | 633 | Observation | `Observation.code.coding` | ANC.B9.DE96 | Syphilis test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 82 | 634 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 83 | 635 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 84 | 647 | DiagnosticReport | `DiagnosticReport.code.coding` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 85 | 662 | ServiceRequest | `ServiceRequest.code.coding` | 2887-8 | Protein [Presence] in Urine | http://loinc.org |
| 86 | 670 | Specimen | `Specimen.type.coding` | 122575003 | Urine specimen | http://snomed.info/sct |
| 87 | 680 | Observation | `Observation.code.coding` | 2887-8 | Protein [Presence] in Urine | http://loinc.org |
| 88 | 681 | Observation | `Observation.code.coding` | ANC.B9.DE114 | Urine test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 89 | 682 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 90 | 683 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 91 | 695 | DiagnosticReport | `DiagnosticReport.code.coding` | 2887-8 | Protein [Presence] in Urine | http://loinc.org |
| 92 | 710 | ServiceRequest | `ServiceRequest.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 93 | 718 | Specimen | `Specimen.type.coding` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 94 | 728 | Observation | `Observation.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 95 | 729 | Observation | `Observation.code.coding` | ANC.B9.DE175 | Blood hemoglobin test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 96 | 733 | Observation | `Observation.interpretation.coding` | 860635002 | No anemia present | http://snomed.info/sct |
| 97 | 739 | Observation | `Observation.interpretation.coding` | OI000032 | Anemia ringan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 98 | 745 | Observation | `Observation.interpretation.coding` | OI000033 | Anemia sedang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 99 | 749 | Observation | `Observation.interpretation.coding` | OI000034 | Anemia berat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 100 | 763 | DiagnosticReport | `DiagnosticReport.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 101 | 778 | ServiceRequest | `ServiceRequest.code.coding` | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | http://loinc.org |
| 102 | 786 | Specimen | `Specimen.type.coding` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 103 | 796 | Observation | `Observation.code.coding` | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | http://loinc.org |
| 104 | 797 | Observation | `Observation.code.coding` | ANC.B9.DE159 | Blood glucose test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 105 | 801 | Observation | `Observation.interpretation.coding` | 166921001 | Blood glucose normal | http://snomed.info/sct |
| 106 | 805 | Observation | `Observation.interpretation.coding` | 166922008 | Blood glucose abnormal | http://snomed.info/sct |
| 107 | 819 | DiagnosticReport | `DiagnosticReport.code.coding` | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | http://loinc.org |
| 108 | 832 | Observation | `Observation.code.coding` | 15220000 | Laboratory test | http://snomed.info/sct |
| 109 | 833 | Observation | `Observation.valueCodeableConcept.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 110 | 834 | Observation | `Observation.valueCodeableConcept.coding` | 76772-3 | Plasmodium falciparum Ag [Presence] in Blood by Rapid immunoassay | http://loinc.org |
| 111 | 835 | Observation | `Observation.valueCodeableConcept.coding` | 104742-2 | Ova and parasites identified in Specimen | http://loinc.org |
| 112 | 836 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 113 | 848 | Observation | `Observation.code.coding` | SP000007 | Tatalaksana Anemia | http://terminology.kemkes.go.id/sp |
| 114 | 849 | Observation | `Observation.valueCodeableConcept.coding` | SP000008 | Pemberian Tablet Tambah Darah | http://terminology.kemkes.go.id/sp |
| 115 | 850 | Observation | `Observation.valueCodeableConcept.coding` | SP000009 | Pemberian Fe Parenteral | http://terminology.kemkes.go.id/sp |
| 116 | 851 | Observation | `Observation.valueCodeableConcept.coding` | 116859006 | Transfusion of blood product | http://snomed.info/sct |
| 117 | 852 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 118 | 853 | Observation | `Observation.valueCodeableConcept.coding` | 3457005 | Patient referral | http://snomed.info/sct |
| 119 | 865 | Observation | `Observation.code.coding` | SP000010 | Skrining Hipertensi dalam Kehamilan | http://terminology.kemkes.go.id/sp |
| 120 | 866 | Observation | `Observation.valueCodeableConcept.coding` | SP000011 | Tidak Pre Eklampsia/ Eklampsia | http://terminology.kemkes.go.id/sp |
| 121 | 867 | Observation | `Observation.valueCodeableConcept.coding` | 48194001 | Pregnancy-induced hypertension | http://snomed.info/sct |
| 122 | 868 | Observation | `Observation.valueCodeableConcept.coding` | 398254007 | Pre-eclampsia | http://snomed.info/sct |
| 123 | 869 | Observation | `Observation.valueCodeableConcept.coding` | 15938005 | Eclampsia | http://snomed.info/sct |
| 124 | 881 | Observation | `Observation.code.coding` | SP000012 | Tatalaksana Pre Eklampsia | http://terminology.kemkes.go.id/sp |
| 125 | 882 | Observation | `Observation.valueCodeableConcept.coding` | 135840009 | Blood pressure monitoring | http://snomed.info/sct |
| 126 | 883 | Observation | `Observation.valueCodeableConcept.coding` | 308116003 | Antihypertensive therapy | http://snomed.info/sct |
| 127 | 884 | Observation | `Observation.valueCodeableConcept.coding` | SP000013 | Pemberian MgSO4 | http://terminology.kemkes.go.id/sp |
| 128 | 885 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 129 | 886 | Observation | `Observation.valueCodeableConcept.coding` | 3457005 | Patient referral | http://snomed.info/sct |
| 130 | 899 | Observation | `Observation.code.coding` | SP000014 | Tatalaksana KEK | http://terminology.kemkes.go.id/sp |
| 131 | 900 | Observation | `Observation.valueCodeableConcept.coding` | 435591000124104 | Nutrition supplement therapy | http://snomed.info/sct |
| 132 | 901 | Observation | `Observation.valueCodeableConcept.coding` | 3457005 | Patient referral | http://snomed.info/sct |
| 133 | 913 | Observation | `Observation.code.coding` | SP000015 | Risiko Masalah Kesehatan | http://terminology.kemkes.go.id/sp |
| 134 | 914 | Observation | `Observation.valueCodeableConcept.coding` | 40733004 | Infectious disease | http://snomed.info/sct |
| 135 | 915 | Observation | `Observation.valueCodeableConcept.coding` | 73211009 | Diabetes mellitus | http://snomed.info/sct |
| 136 | 916 | Observation | `Observation.valueCodeableConcept.coding` | 414916001 | Obesity | http://snomed.info/sct |
| 137 | 917 | Observation | `Observation.valueCodeableConcept.coding` | 56717001 | Tuberculosis | http://snomed.info/sct |
| 138 | 918 | Observation | `Observation.valueCodeableConcept.coding` | 56265001 | Heart disease | http://snomed.info/sct |
| 139 | 919 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 140 | 930 | Observation | `Observation.code.coding` | SP000016 | Tatalaksana Masalah Kesehatan | http://terminology.kemkes.go.id/sp |
| 141 | 942 | Procedure | `Procedure.code.coding` | 1230101008 | Counseling for pregnancy | http://snomed.info/sct |
| 142 | 954 | Procedure | `Procedure.code.coding` | 385892002 | Mental health screening | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah | Code |
|---|---|---|
| http://snomed.info/sct | 52 | 309453006, 309343006, 309367003, 224535009, 134435003, 424144002, 392570002, 2004005, 38341003, 45007003, 284473002, 289625003, 289437007, 289441006, 289440007, 312668007, 289439005, 1209182005, 268445003, 169221005, 169255008, 122555007, 122555007, 122555007, 122575003, 122555007, 860635002, 122555007, 166921001, 166922008, 15220000, 74964007, 116859006, 74964007, 3457005, 48194001, 398254007, 15938005, 135840009, 308116003, 74964007, 3457005, 435591000124104, 3457005, 40733004, 73211009, 414916001, 56717001, 56265001, 74964007, 1230101008, 385892002 |
| http://loinc.org | 43 | 8665-2, 18185-9, 11778-8, 8302-2, 29463-7, 883-9, LA19710-5, LA19709-7, LA19708-9, LA28449-9, 10331-7, LA6576-8, LA6577-6, 72155-5, 68961-2, 68961-2, LA15255-5, LA15256-3, 68961-2, 75410-1, 75410-1, LA6576-8, LA6577-6, 75410-1, 22464-2, 22464-2, LA6576-8, LA6577-6, 22464-2, 2887-8, 2887-8, LA6576-8, LA6577-6, 2887-8, 718-7, 718-7, 718-7, 74774-1, 74774-1, 74774-1, 88874-3, 76772-3, 104742-2 |
| http://terminology.kemkes.go.id/sp | 18 | SP000001, SP000002, SP000003, SP000004, SP000005, SP000006, SP000370, SP000370, SP000007, SP000008, SP000009, SP000010, SP000011, SP000012, SP000013, SP000014, SP000015, SP000016 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 13 | ANC.B6.DE14, ANC.B6.DE22, ANC.B8.DE1, ANC.B8.DE3, ANC.B9.DE24, ANC.B9.DE29, ANC.B8.DE111, ANC.B9.DE32, ANC.B9.DE60, ANC.B9.DE96, ANC.B9.DE114, ANC.B9.DE175, ANC.B9.DE159 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 6 | OC000010, OI000018, OI000035, OI000032, OI000033, OI000034 |
| http://sys-ids.kemkes.go.id/kfa | 3 | VG139, 92000653, 93015491 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC | 2 | K1M, K1A |
| http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes | 2 | ANC.SS.DE58, ANC.SS.DE3 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 1 | ANC |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 1 | N |
| http://hl7.org/fhir/sid/icd-9-cm | 1 | 88.78 |
| **Total** | **142** | |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
