# Output Form: eKohort - Pelayanan Ibu ANC (Final Format)

Sumber: `mapping/phdt-data-dictionary-ekohort-anc.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-ekohort-anc.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 43 |
| Code (`jumlah code` = 1) | 78 |
| Code unik (code + CodeSystem) | 61 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 0 |
| Variabel BQ (unik) | 34 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–21 | Patient | – | – | `nama_ibu` → `Patient.name.text` (2)<br>`no_ktp` → `Patient.identifier.value` (5)<br>`nama_kabupaten` → `Patient.address.city` (8)<br>_Nama Provinsi_ → `Patient.address.extension.url` (10, tanpa BQ)<br>`nama_provinsi` → `Patient.address.extension.extension.valueCode` (12)<br>_Nama Kabupaten_ → `Patient.address.extension.url` (13, tanpa BQ)<br>`nama_kabupaten` → `Patient.address.extension.extension.valueCode` (15)<br>_Nama Kecamatan_ → `Patient.address.extension.url` (16, tanpa BQ)<br>`nama_kecamatan` → `Patient.address.extension.extension.valueCode` (18)<br>_Nama Desa_ → `Patient.address.extension.url` (19, tanpa BQ)<br>`nama_desa` → `Patient.address.extension.extension.valueCode` (21) |
| 2 | 64–84 | Practitioner | – | – | `nama_pemeriksa` → `Practitioner.name.text` (66) |
| 3 | 85–93 | EpisodeOfCare | ANC | Antenatal Care | `hpht or (tanggal_anc - usia_kehamilan)` → `EpisodeOfCare.statusHistory.period.start` (88)<br>`nama_ibu` → `EpisodeOfCare.patient.display` (91)<br>`hpht or (tanggal_anc - usia_kehamilan)` → `EpisodeOfCare.period.start` (93) |
| 4 | 94–115 | Encounter | – | – | `kunjungan_k` → `Encounter.identifier` (95)<br>`kunjungan_k` → `Encounter.identifier` (97)<br>`kunjungan_k` → `Encounter.identifier` (98)<br>`kunjungan_k` → `Encounter.identifier` (99)<br>`kunjungan_k` → `Encounter.identifier` (100)<br>`kunjungan_k` → `Encounter.identifier` (101)<br>`nama_ibu` → `Encounter.subject.display` (106)<br>`nama_pemeriksa` → `Encounter.participant.individual.display` (109)<br>`tanggal_anc` → `Encounter.period.start` (110)<br>`tanggal_anc` → `Encounter.period.end` (111)<br>`nama_lembaga` → `Encounter.location.location.display` (113)<br>`tanggal_anc` → `Encounter.statusHistory.period.start` (125)<br>`tanggal_anc` → `Encounter.statusHistory.period.end` (126)<br>`tanggal_anc` → `Encounter.statusHistory.period.start` (128)<br>`tanggal_anc` → `Encounter.statusHistory.period.end` (129)<br>`tanggal_anc` → `Encounter.statusHistory.period.start` (131)<br>`tanggal_anc` → `Encounter.statusHistory.period.end` (132) |
| 5 | 116–122 | Condition | 134435003 | Routine antenatal care | `nama_ibu` → `Condition.subject.display` (120)<br>`tanggal_anc` → `Condition.recordedDate` (122) |
| 6 | 134–145 | Observation | 8665-2 | Last menstrual period start date | _Hpht_ → `Observation.category.coding` (135, tanpa BQ)<br>`hpht` → `Observation.valueDateTime` (138)<br>`nama_ibu` → `Observation.subject.display` (140)<br>`tanggal_anc` → `Observation.effectiveDateTime` (142)<br>`tanggal_anc` → `Observation.issued` (143)<br>`nama_pemeriksa` → `Observation.performer.display` (145) |
| 7 | 146–157 | Observation | 11778-8 | Delivery date Estimated | _Hpl_ → `Observation.category.coding` (147, tanpa BQ)<br>`hpl` → `Observation.valueDateTime` (150)<br>`nama_ibu` → `Observation.subject.display` (152)<br>`tanggal_anc` → `Observation.effectiveDateTime` (154)<br>`tanggal_anc` → `Observation.issued` (155)<br>`nama_pemeriksa` → `Observation.performer.display` (157) |
| 8 | 158–170 | Observation | 8302-2 | Body height | _Tinggi badan_ → `Observation.status` (158, tanpa BQ)<br>`tinggibadan` → `Observation.valueQuantity.value` (162)<br>`nama_ibu` → `Observation.subject.display` (165)<br>`tanggal_anc` → `Observation.effectiveDateTime` (167)<br>`tanggal_anc` → `Observation.issued` (168)<br>`nama_pemeriksa` → `Observation.performer.display` (170) |
| 9 | 171–190 | Immunization | – | – | _Status Tt_ → `Immunization.status` (171, tanpa BQ)<br>`nama_ibu` → `Immunization.patient.display` (175)<br>`tanggal_anc` → `Immunization.occurrenceDateTime` (177)<br>`tanggal_anc` → `Immunization.recorded` (178)<br>`nama_pemeriksa` → `Immunization.performer.actor.display` (182)<br>`status_tt` → `Immunization.protocolApplied.doseNumberPositiveInt` (183)<br>`status_tt` → `Immunization.protocolApplied.doseNumberPositiveInt` (184)<br>`status_tt` → `Immunization.protocolApplied.doseNumberPositiveInt` (185)<br>`status_tt` → `Immunization.protocolApplied.doseNumberPositiveInt` (186)<br>`status_tt` → `Immunization.protocolApplied.doseNumberPositiveInt` (187)<br>`status_tt` → `Immunization.status` (189) |
| 10 | 191–201 | Immunization | – | – | `nama_ibu` → `Immunization.patient.display` (193)<br>`tanggal_anc` → `Immunization.occurrenceDateTime` (195)<br>`tanggal_anc` → `Immunization.recorded` (196)<br>`nama_pemeriksa` → `Immunization.performer.actor.display` (200) |
| 11 | 202–214 | Observation | 18185-9 | Gestational age | _Usia Kehamilan_ → `Observation.status` (202, tanpa BQ)<br>`usia_kehamilan` → `Observation.valueQuantity.value` (206)<br>`nama_ibu` → `Observation.subject.display` (209)<br>`tanggal_anc` → `Observation.effectiveDateTime` (211)<br>`tanggal_anc` → `Observation.issued` (212)<br>`nama_pemeriksa` → `Observation.performer.display` (214) |
| 12 | 215–226 | Observation | 32418-6 | Obstetric trimester Stated | _Tribulan Ke_ → `Observation.status` (215, tanpa BQ)<br>`tribulan_ke` → `Observation.valueInteger` (219)<br>`nama_ibu` → `Observation.subject.display` (221)<br>`tanggal_anc` → `Observation.effectiveDateTime` (223)<br>`tanggal_anc` → `Observation.issued` (224)<br>`nama_pemeriksa` → `Observation.performer.display` (226) |
| 13 | 227–237 | Observation | 3401000175105 | tion | _Kedatangan_ → `Observation.status` (227, tanpa BQ)<br>`kedatangan` → `Observation.valueInteger` (230)<br>`nama_ibu` → `Observation.subject.display` (232)<br>`tanggal_anc` → `Observation.effectiveDateTime` (234)<br>`tanggal_anc` → `Observation.issued` (235)<br>`nama_pemeriksa` → `Observation.performer.display` (237) |
| 14 | 238–250 | Observation | 29463-7 | Body weight | _Berat Badan_ → `Observation.status` (238, tanpa BQ)<br>`berat_badan` → `Observation.valueQuantity.value` (242)<br>`nama_ibu` → `Observation.subject.display` (245)<br>`tanggal_anc` → `Observation.effectiveDateTime` (247)<br>`tanggal_anc` → `Observation.issued` (248)<br>`nama_pemeriksa` → `Observation.performer.display` (250) |
| 15 | 251–263 | Observation | 8480-6 | Systolic blood pressure | _Tekanan Darah Sistolik_ → `Observation.status` (251, tanpa BQ)<br>`tekanan_darah` → `Observation.valueQuantity.value` (255)<br>`nama_ibu` → `Observation.subject.display` (258)<br>`tanggal_anc` → `Observation.effectiveDateTime` (260)<br>`tanggal_anc` → `Observation.issued` (261)<br>`nama_pemeriksa` → `Observation.performer.display` (263) |
| 16 | 264–276 | Observation | 8462-4 | Diastolic blood pressure | _Tekanan Darah Diastolik_ → `Observation.status` (264, tanpa BQ)<br>`tekanan_darah_di` → `Observation.valueQuantity.value` (268)<br>`nama_ibu` → `Observation.subject.display` (271)<br>`tanggal_anc` → `Observation.effectiveDateTime` (273)<br>`tanggal_anc` → `Observation.issued` (274)<br>`nama_pemeriksa` → `Observation.performer.display` (276) |
| 17 | 277–292 | Observation | 284473002 | Mid upper arm circumference | _Lila_ → `Observation.status` (277, tanpa BQ)<br>`lila` → `Observation.valueQuantity.value` (281)<br>`nama_ibu` → `Observation.subject.display` (284)<br>`tanggal_anc` → `Observation.effectiveDateTime` (286)<br>`tanggal_anc` → `Observation.issued` (287)<br>`nama_pemeriksa` → `Observation.performer.display` (289)<br>`status_gizi` → `Observation.interpretation` (290)<br>`status_gizi` → `Observation.interpretation` (291)<br>`status_gizi` → `Observation.interpretation` (292) |
| 18 | 293–305 | Observation | 11881-0 | Uterus Fundal height Tape measure | _Tinggi Fundus_ → `Observation.status` (293, tanpa BQ)<br>`tinggi_fundus` → `Observation.valueQuantity.value` (297)<br>`nama_ibu` → `Observation.subject.display` (300)<br>`tanggal_anc` → `Observation.effectiveDateTime` (302)<br>`tanggal_anc` → `Observation.issued` (303)<br>`nama_pemeriksa` → `Observation.performer.display` (305) |
| 19 | 306–318 | Observation | 8867-4 | Heart rate | _Nadi_ → `Observation.status` (306, tanpa BQ)<br>`nadi` → `Observation.valueQuantity.value` (309)<br>`nama_ibu` → `Observation.subject.display` (313)<br>`tanggal_anc` → `Observation.effectiveDateTime` (315)<br>`tanggal_anc` → `Observation.issued` (316)<br>`nama_pemeriksa` → `Observation.performer.display` (318) |
| 20 | 319–332 | Observation | 9279-1 | Respiratory rate | _Rr_ → `Observation.status` (319, tanpa BQ)<br>`rr` → `Observation.valueQuantity.value` (323)<br>`nama_ibu` → `Observation.subject.display` (327)<br>`tanggal_anc` → `Observation.effectiveDateTime` (329)<br>`tanggal_anc` → `Observation.issued` (330)<br>`nama_pemeriksa` → `Observation.performer.display` (332) |
| 21 | 333–345 | Observation | 55283-6 | Fetal Heart rate | _Denyut Jantung Janin_ → `Observation.status` (333, tanpa BQ)<br>`detak_jantung_janin` → `Observation.valueQuantity.value` (337)<br>`nama_ibu` → `Observation.subject.display` (340)<br>`tanggal_anc` → `Observation.effectiveDateTime` (342)<br>`tanggal_anc` → `Observation.issued` (343)<br>`nama_pemeriksa` → `Observation.performer.display` (345) |
| 22 | 346–358 | Observation | 89087-1 | Fetal Body weight Estimated | _Taksiran Berat Janin_ → `Observation.status` (346, tanpa BQ)<br>`berat_janin` → `Observation.valueQuantity.value` (350)<br>`nama_ibu` → `Observation.subject.display` (353)<br>`tanggal_anc` → `Observation.effectiveDateTime` (355)<br>`tanggal_anc` → `Observation.issued` (356)<br>`nama_pemeriksa` → `Observation.performer.display` (358) |
| 23 | 359–369 | Procedure | 88.78 | Diagnostic ultrasound of gravid uterus | _Usg_ → `Procedure.category.coding` (359, tanpa BQ)<br>`usg` → `Procedure.status` (361)<br>`usg` → `Procedure.status` (362)<br>`nama_ibu` → `Procedure.subject.display` (364)<br>`tanggal_anc` → `Procedure.performedPeriod.start` (366)<br>`tanggal_anc` → `Procedure.performedPeriod.end` (367)<br>`nama_pemeriksa` → `Procedure.performer.actor.display` (369) |
| 24 | 370–379 | ServiceRequest | – | – | _Hemoglobin_ → `ServiceRequest.category` (370, tanpa BQ)<br>`tanggal_anc` → `ServiceRequest.occurrenceDateTime` (377) |
| 25 | 384–391 | Specimen | – | – | `tanggal_anc` → `Specimen.collection.collectedDateTime` (387)<br>`nama_ibu` → `Specimen.subject.display` (389)<br>`tanggal_anc` → `Specimen.receivedTime` (391) |
| 26 | 392–404 | Observation | 718-7 | Hemoglobin [Mass/volume] in Blood | `hemoglobin` → `Observation.valueQuantity.value` (397)<br>`nama_ibu` → `Observation.subject.display` (399)<br>`tanggal_anc` → `Observation.effectiveDateTime` (401)<br>`tanggal_anc` → `Observation.issued` (402)<br>`nama_pemeriksa` → `Observation.performer.display` (404) |
| 27 | 405–416 | DiagnosticReport | 718-7 | Hemoglobin [Mass/volume] in Blood | `tanggal_anc` → `DiagnosticReport.effectiveDateTime` (410)<br>`tanggal_anc` → `DiagnosticReport.issued` (411) |
| 28 | 417–426 | ServiceRequest | – | – | _Pro Urin Hasil_ → `ServiceRequest.category` (417, tanpa BQ)<br>`tanggal_anc` → `ServiceRequest.occurrenceDateTime` (424) |
| 29 | 431–438 | Specimen | – | – | `tanggal_anc` → `Specimen.collection.collectedDateTime` (434)<br>`nama_ibu` → `Specimen.subject.display` (436)<br>`tanggal_anc` → `Specimen.receivedTime` (438) |
| 30 | 439–453 | Observation | 2887-8 | Protein [Presence] in Urine | `pro_urin_hasil` → `Observation.valueCodeableConcept.coding` (445)<br>`pro_urin_hasil` → `Observation.valueCodeableConcept.coding` (446)<br>`nama_ibu` → `Observation.subject.display` (448)<br>`tanggal_anc` → `Observation.effectiveDateTime` (450)<br>`tanggal_anc` → `Observation.issued` (451)<br>`nama_pemeriksa` → `Observation.performer.display` (453) |
| 31 | 454–465 | DiagnosticReport | 2887-8 | Protein [Presence] in Urine | `tanggal_anc` → `DiagnosticReport.effectiveDateTime` (459)<br>`tanggal_anc` → `DiagnosticReport.issued` (460) |
| 32 | 467–476 | ServiceRequest | – | – | _Sifilis_ → `ServiceRequest.category` (467, tanpa BQ)<br>`tanggal_anc` → `ServiceRequest.occurrenceDateTime` (474) |
| 33 | 481–488 | Specimen | – | – | `tanggal_anc` → `Specimen.collection.collectedDateTime` (484)<br>`nama_ibu` → `Specimen.subject.display` (486)<br>`tanggal_anc` → `Specimen.receivedTime` (488) |
| 34 | 489–501 | Observation | 22464-2 | Reagin Ab [Presence] in Specimen | `sifilis` → `Observation.valueCodeableConcept.coding` (493)<br>`sifilis` → `Observation.valueCodeableConcept.coding` (494)<br>`nama_ibu` → `Observation.subject.display` (496)<br>`tanggal_anc` → `Observation.effectiveDateTime` (498)<br>`tanggal_anc` → `Observation.issued` (499)<br>`nama_pemeriksa` → `Observation.performer.display` (501) |
| 35 | 502–513 | DiagnosticReport | – | – | `tanggal_anc` → `DiagnosticReport.effectiveDateTime` (507)<br>`tanggal_anc` → `DiagnosticReport.issued` (508) |
| 36 | 514–523 | ServiceRequest | – | – | _Hepb_ → `ServiceRequest.category` (514, tanpa BQ)<br>`tanggal_anc` → `ServiceRequest.occurrenceDateTime` (521) |
| 37 | 528–535 | Specimen | – | – | `tanggal_anc` → `Specimen.collection.collectedDateTime` (531)<br>`nama_ibu` → `Specimen.subject.display` (533)<br>`tanggal_anc` → `Specimen.receivedTime` (535) |
| 38 | 536–548 | Observation | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | `hepb` → `Observation.valueCodeableConcept.coding` (540)<br>`hepb` → `Observation.valueCodeableConcept.coding` (541)<br>`nama_ibu` → `Observation.subject.display` (543)<br>`tanggal_anc` → `Observation.effectiveDateTime` (545)<br>`tanggal_anc` → `Observation.issued` (546)<br>`nama_pemeriksa` → `Observation.performer.display` (548) |
| 39 | 549–560 | DiagnosticReport | – | – | `tanggal_anc` → `DiagnosticReport.effectiveDateTime` (554)<br>`tanggal_anc` → `DiagnosticReport.issued` (555) |
| 40 | 561–570 | ServiceRequest | – | – | _Hiv_ → `ServiceRequest.category` (561, tanpa BQ)<br>`tanggal_anc` → `ServiceRequest.occurrenceDateTime` (568) |
| 41 | 575–582 | Specimen | – | – | `tanggal_anc` → `Specimen.collection.collectedDateTime` (578)<br>`nama_ibu` → `Specimen.subject.display` (580)<br>`tanggal_anc` → `Specimen.receivedTime` (582) |
| 42 | 583–595 | Observation | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | `hiv` → `Observation.valueCodeableConcept.coding` (587)<br>`hiv` → `Observation.valueCodeableConcept.coding` (588)<br>`nama_ibu` → `Observation.subject.display` (590)<br>`tanggal_anc` → `Observation.effectiveDateTime` (592)<br>`tanggal_anc` → `Observation.issued` (593)<br>`nama_pemeriksa` → `Observation.performer.display` (595) |
| 43 | 596–607 | DiagnosticReport | – | – | `tanggal_anc` → `DiagnosticReport.effectiveDateTime` (601)<br>`tanggal_anc` → `DiagnosticReport.issued` (602) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 20 |
| ServiceRequest | 5 |
| Specimen | 5 |
| DiagnosticReport | 5 |
| Immunization | 2 |
| Patient | 1 |
| Practitioner | 1 |
| EpisodeOfCare | 1 |
| Encounter | 1 |
| Condition | 1 |
| Procedure | 1 |
| **Total** | **43** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 89 | EpisodeOfCare | `EpisodeOfCare.type.coding` | ANC | Antenatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 2 | 95 | Encounter | `Encounter.identifier` | K1M | Tidak ada | http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC |
| 3 | 96 | Encounter | `Encounter.identifier` | K1A | Tidak ada | http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC |
| 4 | 97 | Encounter | `Encounter.identifier` | K2 | Tidak ada | http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC |
| 5 | 98 | Encounter | `Encounter.identifier` | K3 | Tidak ada | http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC |
| 6 | 99 | Encounter | `Encounter.identifier` | K4 | Tidak ada | http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC |
| 7 | 100 | Encounter | `Encounter.identifier` | K5 | Tidak ada | http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC |
| 8 | 101 | Encounter | `Encounter.identifier` | K6 | Tidak ada | http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC |
| 9 | 118 | Condition | `Condition.code.coding` | 134435003 | Routine antenatal care | http://snomed.info/sct |
| 10 | 136 | Observation | `Observation.code.coding` | 8665-2 | Last menstrual period start date | http://loinc.org |
| 11 | 137 | Observation | `Observation.code.coding` | ANC.B6.DE14 | Last menstrual period (LMP) date | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 12 | 148 | Observation | `Observation.code.coding` | 11778-8 | Delivery date Estimated | http://loinc.org |
| 13 | 149 | Observation | `Observation.code.coding` | ANC.B6.DE22 | Expected date of delivery (EDD) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 14 | 160 | Observation | `Observation.code.coding` | 8302-2 | Body height | http://loinc.org |
| 15 | 161 | Observation | `Observation.code.coding` | ANC.B8.DE1 | Height | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 16 | 173 | Immunization | `Immunization.vaccineCode` | VG139 | Td | http://sys-ids.kemkes.go.id/kfa |
| 17 | 191 | Immunization | `Immunization.vaccineCode` | VG139 | Td | http://sys-ids.kemkes.go.id/kfa |
| 18 | 204 | Observation | `Observation.code.coding` | 18185-9 | Gestational age | http://loinc.org |
| 19 | 205 | Observation | `Observation.code.coding` | ANC.B6.DE17 | Gestational age | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 20 | 217 | Observation | `Observation.code.coding` | 32418-6 | Obstetric trimester Stated | http://loinc.org |
| 21 | 218 | Observation | `Observation.code.coding` | ANC.SS.DE13 | Trimester ke | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 22 | 229 | Observation | `Observation.code.coding` | 3401000175105 | tion | http://snomed.info/sct |
| 23 | 240 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 24 | 241 | Observation | `Observation.code.coding` | ANC.B8.DE3 | Current weight | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 25 | 253 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 26 | 254 | Observation | `Observation.code.coding` | ANC.B8.DE17 | Systolic blood pressure | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 27 | 266 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://loinc.org |
| 28 | 267 | Observation | `Observation.code.coding` | ANC.B8.DE19 | Diastolic blood pressure | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 29 | 279 | Observation | `Observation.code.coding` | 284473002 | Mid upper arm circumference | http://snomed.info/sct |
| 30 | 280 | Observation | `Observation.code.coding` | ANC.SS.DE3 | Lingkar Lengan Atas (LILA) | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 31 | 290 | Observation | `Observation.interpretation` | OI000018 | Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 32 | 291 | Observation | `Observation.interpretation` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 33 | 292 | Observation | `Observation.interpretation` | OI000035 | Risiko Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 34 | 295 | Observation | `Observation.code.coding` | 11881-0 | Uterus Fundal height Tape measure | http://loinc.org |
| 35 | 296 | Observation | `Observation.code.coding` | ANC.B8.DE105 | Symphysis-fundal height | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 36 | 308 | Observation | `Observation.code.coding` | 8867-4 | Heart rate | http://loinc.org |
| 37 | 321 | Observation | `Observation.code.coding` | 9279-1 | Respiratory rate | http://loinc.org |
| 38 | 322 | Observation | `Observation.code.coding` | ANC.SS.DE2 | Pernapasan | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 39 | 335 | Observation | `Observation.code.coding` | 55283-6 | Fetal Heart rate | http://loinc.org |
| 40 | 336 | Observation | `Observation.code.coding` | ANC.B8.DE107 | Fetal heart rate | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 41 | 348 | Observation | `Observation.code.coding` | 89087-1 | Fetal Body weight Estimated | http://loinc.org |
| 42 | 349 | Observation | `Observation.code.coding` | ANC.SS.DE1 | Taksiran Berat Janin (TBJ) | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 43 | 360 | Procedure | `Procedure.code.coding` | 88.78 | Diagnostic ultrasound of gravid uterus | http://hl7.org/fhir/sid/icd-9-cm |
| 44 | 374 | ServiceRequest | `ServiceRequest.code` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 45 | 385 | Specimen | `Specimen.type` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 46 | 394 | Observation | `Observation.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 47 | 395 | Observation | `Observation.code.coding` | ANC.B9.DE175 | Blood hemoglobin test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 48 | 407 | DiagnosticReport | `DiagnosticReport.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 49 | 421 | ServiceRequest | `ServiceRequest.code` | 2887-8 | Protein [Presence] in Urine | http://loinc.org |
| 50 | 432 | Specimen | `Specimen.type` | 122575003 | Urine specimen | http://snomed.info/sct |
| 51 | 441 | Observation | `Observation.code.coding` | 2887-8 | Protein [Presence] in Urine | http://loinc.org |
| 52 | 442 | Observation | `Observation.code.coding` | ANC.B9.DE114 | Urine test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 53 | 443 | Observation | `Observation.valueCodeableConcept.coding` | LA11843-2 | 3+ | http://loinc.org |
| 54 | 444 | Observation | `Observation.valueCodeableConcept.coding` | LA11842-4 | 2+ | http://loinc.org |
| 55 | 445 | Observation | `Observation.valueCodeableConcept.coding` | LA11841-6 | 1+ | http://loinc.org |
| 56 | 446 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 57 | 456 | DiagnosticReport | `DiagnosticReport.code.coding` | 2887-8 | Protein [Presence] in Urine | http://loinc.org |
| 58 | 471 | ServiceRequest | `ServiceRequest.code` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 59 | 482 | Specimen | `Specimen.type` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 60 | 491 | Observation | `Observation.code.coding` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 61 | 492 | Observation | `Observation.code.coding` | ANC.B9.DE96 | Syphilis test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 62 | 493 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 63 | 494 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 64 | 504 | DiagnosticReport | `DiagnosticReport.code` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 65 | 518 | ServiceRequest | `ServiceRequest.code` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 66 | 529 | Specimen | `Specimen.type` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 67 | 538 | Observation | `Observation.code.coding` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 68 | 539 | Observation | `Observation.code.coding` | ANC.B9.DE60 | Hepatitis B test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 69 | 540 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 70 | 541 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 71 | 551 | DiagnosticReport | `DiagnosticReport.code` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 72 | 565 | ServiceRequest | `ServiceRequest.code` | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 73 | 576 | Specimen | `Specimen.type` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 74 | 585 | Observation | `Observation.code.coding` | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 75 | 586 | Observation | `Observation.code.coding` | ANC.B9.DE32 | HIV test | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 76 | 587 | Observation | `Observation.valueCodeableConcept.coding` | LA15255-5 | Reactive | http://loinc.org |
| 77 | 588 | Observation | `Observation.valueCodeableConcept.coding` | LA15256-3 | Nonreactive | http://loinc.org |
| 78 | 598 | DiagnosticReport | `DiagnosticReport.code` | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://loinc.org | 38 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 14 |
| http://snomed.info/sct | 8 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC | 7 |
| http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes | 4 |
| http://sys-ids.kemkes.go.id/kfa | 2 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 2 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 1 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 1 |
| http://hl7.org/fhir/sid/icd-9-cm | 1 |
| **Total** | **78** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 25 | ⚠️ nama_lembaga | Nama Lembaga | Organization | `Organization.name` |
| 40 | ⚠️ nama_lembaga | – | Location | `Location.identifier` |
| 42 | ⚠️ nama_lembaga | – | Location | `Location.name` |
| 466 | – | Reduksi Guladarah | – | `` |
