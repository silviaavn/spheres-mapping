# Output Form: SiHepi - Form Rekap 3e (Registrasi Ibu Hamil Triple Eliminasi)

Sumber: `mapping/phdt-data-dictionary-sihepi-rekap-3e.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-sihepi-rekap-3e.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 65 |
| Code (`jumlah code` = 1) | 118 |
| Code unik (code + CodeSystem) | 89 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 49 |
| Variabel BQ (unik) | 2 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 3–31 | Patient | – | – | `TRUE` → `Patient.name.text` (3)<br>`TRUE` → `Patient.identifier.value` (6)<br>`TRUE` → `Patient.telecom.value` (9)<br>`FALSE` → `Patient.address.use` (10)<br>`FALSE` → `Patient.address.extension.extension.valueCode` (16)<br>`FALSE` → `Patient.address.extension.extension.valueCode` (19)<br>`FALSE` → `Patient.address.extension.extension.valueCode` (22)<br>`TRUE` → `Patient.address.extension.extension.valueCode` (25)<br>`FALSE` → `Patient.address.extension.extension.valueCode` (28)<br>`FALSE` → `Patient.address.extension.extension.valueCode` (31) |
| 2 | 74–94 | Practitioner | – | – | – |
| 3 | 95–103 | EpisodeOfCare | ANC | Antenatal Care | – |
| 4 | 104–118 | Encounter | – | – | `FALSE` → `Encounter.period.start` (113) |
| 5 | 119–125 | Condition | 134435003 | Routine antenatal care | – |
| 6 | 138–149 | Observation | 424144002 | Current chronological age | `TRUE` → `Observation.valueQuantity.value` (141) |
| 7 | 150–166 | Observation | 85658-3 | Occupation [Type] | `TRUE` → `Observation.valueCodeableConcept.coding` (153) |
| 8 | 167–178 | Observation | 11996-6 | [#] Pregnancies | `TRUE` → `Observation.valueInteger` (171) |
| 9 | 179–190 | Observation | 11977-6 | [#] Parity | `TRUE` → `Observation.valueInteger` (183) |
| 10 | 191–202 | Observation | 69043-8 | Other pregnancy outcomes # | `TRUE` → `Observation.valueInteger` (195) |
| 11 | 203–214 | Observation | 11778-8 | Delivery date Estimated | `TRUE` → `Observation.valueDateTime` (207) |
| 12 | 215–227 | Observation | 18185-9 | Gestational age | `TRUE` → `Observation.valueQuantity.value` (219) |
| 13 | 228–237 | ServiceRequest | – | – | `FALSE` → `ServiceRequest.category` (228)<br>`TRUE` → `ServiceRequest.occurrenceDateTime` (235) |
| 14 | 242–249 | Specimen | – | – | – |
| 15 | 250–262 | Observation | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | `TRUE` → `Observation.valueCodeableConcept.coding` (254) |
| 16 | 263–274 | DiagnosticReport | – | – | – |
| 17 | 275–284 | ServiceRequest | – | – | `FALSE` → `ServiceRequest.category` (275)<br>`TRUE` → `ServiceRequest.occurrenceDateTime` (282) |
| 18 | 289–296 | Specimen | – | – | – |
| 19 | 297–309 | Observation | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | `TRUE` → `Observation.valueCodeableConcept.coding` (301) |
| 20 | 310–321 | DiagnosticReport | – | – | – |
| 21 | 322–331 | ServiceRequest | – | – | `FALSE` → `ServiceRequest.category` (322)<br>`TRUE` → `ServiceRequest.occurrenceDateTime` (329) |
| 22 | 336–343 | Specimen | – | – | – |
| 23 | 344–356 | Observation | 22464-2 | Reagin Ab [Presence] in Specimen | `TRUE` → `Observation.valueCodeableConcept.coding` (348) |
| 24 | 357–368 | DiagnosticReport | – | – | – |
| 25 | 369–379 | Observation | SP000160 | Tanggal Masuk Perawatan, Dukungan, dan Pengobatan (PDP) HIV | `TRUE` → `Observation.valueDateTime` (372) |
| 26 | 380–390 | Observation | SP000161 | Tanggal Mendapat atau Memulai ARV | `TRUE` → `Observation.valueDateTime` (383) |
| 27 | 391–402 | Observation | SP000162 | Sifilis Ditangani | `TRUE` → `Observation.valueBoolean` (394) |
| 28 | 403–414 | Observation | SP000163 | Sifilis Diobati Adekuat | `TRUE` → `Observation.valueBoolean` (406) |
| 29 | 415–426 | Observation | SP000164 | Hepatitis B Ditangani atau Dirujuk | `TRUE` → `Observation.valueBoolean` (418) |
| 30 | 427–436 | ServiceRequest | – | – | `TRUE` → `ServiceRequest.category` (427)<br>`FALSE` → `ServiceRequest.authoredOn` (434) |
| 31 | 437–448 | Observation | 72181-1 | HIV results shared with partner [RHEA] | `TRUE` → `Observation.valueBoolean` (440) |
| 32 | 449–460 | Observation | SP000165 | Pasangan Diperiksa Sifilis | `TRUE` → `Observation.valueBoolean` (452) |
| 33 | 461–471 | Observation | SP000166 | Jumlah Anak Dilahirkan | `TRUE` → `Observation.valueInteger` (464) |
| 34 | 472–491 | Observation | 72150-6 | Delivery location | `TRUE` → `Observation.valueCodeableConcept` (475) |
| 35 | 492–502 | Observation | 93857-1 | Date and time of obstetric delivery | `TRUE` → `Observation.valueDateTime` (495) |
| 36 | 503–535 | Observation | SP000169 | Pemantauan Anak dari Ibu HIV | `FALSE` → `Observation.valueBoolean` (506)<br>`TRUE` → `Observation.component.code.coding` (508)<br>`TRUE` → `Observation.component.code.coding` (510)<br>`TRUE` → `Observation.component.code.coding` (512)<br>`TRUE` → `Observation.component.code.coding` (515)<br>`TRUE` → `Observation.component.code.coding` (517)<br>`TRUE` → `Observation.component.code.coding` (520)<br>`TRUE` → `Observation.component.code.coding` (522)<br>`TRUE` → `Observation.component.code.coding` (525)<br>`TRUE` → `Observation.component.code.coding` (527) |
| 37 | 536–545 | Procedure | SP000126 | ARV Profilaksis | `FALSE` → `Procedure.category.coding` (536) |
| 38 | 546–556 | Observation | SP000167 | Hasil Dry Blood Spot Early Infant Diagnosis Pada Usia 6-8 Minggu | `FALSE` → `Observation.status` (546)<br>`FALSE` → `Observation.valueString` (549)<br>`FALSE` → `Observation.effectiveDateTime` (553) |
| 39 | 557–567 | Observation | SP000168 | Hasil Konfirmasi Dry Blood Spot Early Infant Diagnosis dalam 12 Bulan | `FALSE` → `Observation.status` (557)<br>`FALSE` → `Observation.valueString` (560)<br>`FALSE` → `Observation.effectiveDateTime` (564) |
| 40 | 568–578 | Observation | – | – | `FALSE` → `Observation.status` (568)<br>`FALSE` → `Observation.valueString` (571)<br>`FALSE` → `Observation.effectiveDateTime` (575) |
| 41 | 579–589 | Observation | – | – | `FALSE` → `Observation.status` (579)<br>`FALSE` → `Observation.valueDateTime` (582) |
| 42 | 590–600 | Observation | – | – | `FALSE` → `Observation.status` (590)<br>`FALSE` → `Observation.valueDateTime` (593) |
| 43 | 601–620 | Observation | SP000177 | Pemantauan Anak dari Ibu Sifilis | `FALSE` → `Observation.valueBoolean` (604)<br>`TRUE` → `Observation.component.code.coding` (606)<br>`TRUE` → `Observation.component.code.coding` (609)<br>`TRUE` → `Observation.component.code.coding` (611) |
| 44 | 621–632 | Observation | – | – | `FALSE` → `Observation.valueBoolean` (624) |
| 45 | 633–643 | Observation | – | – | `FALSE` → `Observation.status` (633)<br>`FALSE` → `Observation.valueString` (636) |
| 46 | 644–677 | Observation | SP000181 | Pemantauan Anak dari Ibu Hepatitis | `FALSE` → `Observation.valueBoolean` (647)<br>`TRUE` → `Observation.component.code.coding` (649)<br>`TRUE` → `Observation.component.code.coding` (652)<br>`TRUE` → `Observation.component.code.coding` (655)<br>`TRUE` → `Observation.component.code.coding` (657)<br>`TRUE` → `Observation.component.code.coding` (659)<br>`TRUE` → `Observation.component.code.coding` (661)<br>`TRUE` → `Observation.component.code.coding` (663)<br>`TRUE` → `Observation.component.code.coding` (666)<br>`TRUE` → `Observation.component.code.coding` (668) |
| 47 | 678–693 | Immunization | – | – | `FALSE` → `Immunization.status` (678)<br>`FALSE` → `Immunization.occurenceDateTime` (684)<br>`FALSE` → `Immunization.status` (692) |
| 48 | 694–707 | Immunization | – | – | `FALSE` → `Immunization.occurenceDateTime` (698)<br>`FALSE` → `Immunization.status` (706) |
| 49 | 708–721 | Immunization | – | – | `FALSE` → `Immunization.occurenceDateTime` (712)<br>`FALSE` → `Immunization.status` (720) |
| 50 | 722–735 | Immunization | – | – | `FALSE` → `Immunization.occurenceDateTime` (726)<br>`FALSE` → `Immunization.status` (734) |
| 51 | 736–747 | Immunization | – | – | `FALSE` → `Immunization.occurenceDateTime` (740) |
| 52 | 748–758 | Observation | – | – | `FALSE` → `Observation.status` (748)<br>`FALSE` → `Observation.valueString` (751)<br>`FALSE` → `Observation.effectiveDateTime` (755) |
| 53 | 759–769 | Observation | – | – | `FALSE` → `Observation.status` (759)<br>`FALSE` → `Observation.valueString` (762)<br>`FALSE` → `Observation.effectiveDateTime` (766) |
| 54 | 770–780 | Observation | 121912002 | Hepatitis B virus deoxyribonucleic acid assay | `FALSE` → `Observation.status` (770)<br>`TRUE` → `Observation.valueString` (773)<br>`TRUE` → `Observation.effectiveDateTime` (777) |
| 55 | 781–791 | Observation | 313476009 | Hepatitis B e antigen test | `FALSE` → `Observation.status` (781)<br>`TRUE` → `Observation.valueString` (784)<br>`TRUE` → `Observation.effectiveDateTime` (788) |
| 56 | 792–802 | Observation | 34608000 | Alanine aminotransferase measurement | `FALSE` → `Observation.status` (792)<br>`TRUE` → `Observation.valueString` (795)<br>`TRUE` → `Observation.effectiveDateTime` (799) |
| 57 | 803–814 | Observation | SP000193 | Memenuhi Kriteria Pengobatan Pencegahan Hepatitis B | `TRUE` → `Observation.valueBoolean` (806) |
| 58 | 815–825 | Observation | SP000194 | Metode Pemeriksaan Sirosis | `TRUE` → `Observation.valueString` (818) |
| 59 | 826–836 | Observation | SP000195 | Status Sirosis | `TRUE` → `Observation.valueString` (829) |
| 60 | 837–847 | Observation | SP000196 | Status Pengobatan Pencegahan Hepatitis B | `TRUE` → `Observation.valueString` (840) |
| 61 | 848–859 | Observation | SP000197 | Tanggal Pengambilan Obat Pencegahan Hepatitis B | `TRUE` → `Observation.identifier` (848) |
| 62 | 860–871 | Observation | SP000197 | Tanggal Pengambilan Obat Pencegahan Hepatitis B | `TRUE` → `Observation.identifier` (860) |
| 63 | 872–883 | Observation | SP000197 | Tanggal Pengambilan Obat Pencegahan Hepatitis B | `TRUE` → `Observation.identifier` (872) |
| 64 | 884–895 | Observation | SP000197 | Tanggal Pengambilan Obat Pencegahan Hepatitis B | `TRUE` → `Observation.identifier` (884) |
| 65 | 896–906 | Observation | SP000198 | Status Akhir Pengobatan Pencegahan Hepatitis B | `TRUE` → `Observation.valueString` (899) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 44 |
| Immunization | 5 |
| ServiceRequest | 4 |
| Specimen | 3 |
| DiagnosticReport | 3 |
| Patient | 1 |
| Practitioner | 1 |
| EpisodeOfCare | 1 |
| Encounter | 1 |
| Condition | 1 |
| Procedure | 1 |
| **Total** | **65** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 99 | EpisodeOfCare | `EpisodeOfCare.type.coding` | ANC | Antenatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 2 | 121 | Condition | `Condition.code.coding` | 134435003 | Routine antenatal care | http://snomed.info/sct |
| 3 | 140 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 4 | 152 | Observation | `Observation.code.coding` | 85658-3 | Occupation [Type] | http://loinc.org |
| 5 | 154 | Observation | `Observation.valueCodeableConcept.coding` | 741062008 | Not in labor force | http://snomed.info/sct |
| 6 | 155 | Observation | `Observation.valueCodeableConcept.coding` | SP000217 | PNS/BUMN/TNI/POLRI | http://terminology.kemkes.go.id/sp |
| 7 | 156 | Observation | `Observation.valueCodeableConcept.coding` | 160906004 | Self-employed | http://snomed.info/sct |
| 8 | 157 | Observation | `Observation.valueCodeableConcept.coding` | SP000218 | Karyawan Swasta | http://terminology.kemkes.go.id/sp |
| 9 | 158 | Observation | `Observation.valueCodeableConcept.coding` | 159812002 | Farming/fishing occupation | http://snomed.info/sct |
| 10 | 159 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 11 | 169 | Observation | `Observation.code.coding` | 11996-6 | [#] Pregnancies | http://loinc.org |
| 12 | 170 | Observation | `Observation.code.coding` | ANC.B6.DE24 | Number of pregnancies (gravida) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 13 | 181 | Observation | `Observation.code.coding` | 11977-6 | [#] Parity | http://loinc.org |
| 14 | 182 | Observation | `Observation.code.coding` | ANC.B6.DE32 | Parity | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 15 | 193 | Observation | `Observation.code.coding` | 69043-8 | Other pregnancy outcomes # | http://loinc.org |
| 16 | 194 | Observation | `Observation.code.coding` | ANC.B6.DE25 | Number of miscarriages and/or abortions | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 17 | 205 | Observation | `Observation.code.coding` | 11778-8 | Delivery date Estimated | http://loinc.org |
| 18 | 206 | Observation | `Observation.code.coding` | ANC.B6.DE22 | Expected date of delivery (EDD) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 19 | 217 | Observation | `Observation.code.coding` | 18185-9 | Gestational age | http://loinc.org |
| 20 | 218 | Observation | `Observation.code.coding` | ANC.B6.DE17 | Gestational age | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 21 | 232 | ServiceRequest | `ServiceRequest.code` | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 22 | 243 | Specimen | `Specimen.type` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 23 | 252 | Observation | `Observation.code.coding` | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 24 | 253 | Observation | `Observation.code.coding` | ANC.B9.DE32 | HIV test | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 25 | 254 | Observation | `Observation.valueCodeableConcept.coding` | LA15255-5 | Reactive | http://loinc.org |
| 26 | 255 | Observation | `Observation.valueCodeableConcept.coding` | LA15256-3 | Nonreactive | http://loinc.org |
| 27 | 265 | DiagnosticReport | `DiagnosticReport.code` | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 28 | 279 | ServiceRequest | `ServiceRequest.code` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 29 | 290 | Specimen | `Specimen.type` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 30 | 299 | Observation | `Observation.code.coding` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 31 | 300 | Observation | `Observation.code.coding` | ANC.B9.DE60 | Hepatitis B test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 32 | 301 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 33 | 302 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 34 | 312 | DiagnosticReport | `DiagnosticReport.code` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 35 | 326 | ServiceRequest | `ServiceRequest.code` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 36 | 337 | Specimen | `Specimen.type` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 37 | 346 | Observation | `Observation.code.coding` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 38 | 347 | Observation | `Observation.code.coding` | ANC.B9.DE96 | Syphilis test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 39 | 348 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 40 | 349 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 41 | 359 | DiagnosticReport | `DiagnosticReport.code` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 42 | 371 | Observation | `Observation.code.coding` | SP000160 | Tanggal Masuk Perawatan, Dukungan, dan Pengobatan (PDP) HIV | http://terminology.kemkes.go.id/sp |
| 43 | 382 | Observation | `Observation.code.coding` | SP000161 | Tanggal Mendapat atau Memulai ARV | http://terminology.kemkes.go.id/sp |
| 44 | 393 | Observation | `Observation.code.coding` | SP000162 | Sifilis Ditangani | http://terminology.kemkes.go.id/sp |
| 45 | 405 | Observation | `Observation.code.coding` | SP000163 | Sifilis Diobati Adekuat | http://terminology.kemkes.go.id/sp |
| 46 | 417 | Observation | `Observation.code.coding` | SP000164 | Hepatitis B Ditangani atau Dirujuk | http://terminology.kemkes.go.id/sp |
| 47 | 431 | ServiceRequest | `ServiceRequest.code` | 737492002 | Outpatient care management | http://snomed.info/sct |
| 48 | 439 | Observation | `Observation.code.coding` | 72181-1 | HIV results shared with partner [RHEA] | http://loinc.org |
| 49 | 451 | Observation | `Observation.code.coding` | SP000165 | Pasangan Diperiksa Sifilis | http://terminology.kemkes.go.id/sp |
| 50 | 463 | Observation | `Observation.code.coding` | SP000166 | Jumlah Anak Dilahirkan | http://terminology.kemkes.go.id/sp |
| 51 | 474 | Observation | `Observation.code.coding` | 72150-6 | Delivery location | http://loinc.org |
| 52 | 475 | Observation | `Observation.valueCodeableConcept` | 264362003 | Home | http://snomed.info/sct |
| 53 | 476 | Observation | `Observation.valueCodeableConcept` | OT000001 | Polindes | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 54 | 477 | Observation | `Observation.valueCodeableConcept` | OT000002 | Pustu | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 55 | 478 | Observation | `Observation.valueCodeableConcept` | 102 | Pusat Kesehatan Masyarakat | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 56 | 479 | Observation | `Observation.valueCodeableConcept` | 103 | Klinik | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 57 | 480 | Observation | `Observation.valueCodeableConcept` | OT000008 | Rumah Bersalin | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 58 | 481 | Observation | `Observation.valueCodeableConcept` | 82242000 | Children’s hospital | http://snomed.info/sct |
| 59 | 482 | Observation | `Observation.valueCodeableConcept` | 104 | Rumah Sakit | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 60 | 483 | Observation | `Observation.valueCodeableConcept` | OT000003 | RS ODHA | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 61 | 484 | Observation | `Observation.valueCodeableConcept` | OT000004 | Bidan Praktek Mandiri | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 62 | 494 | Observation | `Observation.code.coding` | 93857-1 | Date and time of obstetric delivery | http://loinc.org |
| 63 | 505 | Observation | `Observation.code.coding` | SP000169 | Pemantauan Anak dari Ibu HIV | http://terminology.kemkes.go.id/sp |
| 64 | 508 | Observation | `Observation.component.code.coding` | SP000170 | Tanggal ARV Profilaksis | http://terminology.kemkes.go.id/sp |
| 65 | 510 | Observation | `Observation.component.code.coding` | SP000171 | Tanggal Dry Blood Spot Early Infant Diagnosis Pada Usia 6-8 Minggu | http://terminology.kemkes.go.id/sp |
| 66 | 512 | Observation | `Observation.component.code.coding` | SP000167 | Hasil Dry Blood Spot Early Infant Diagnosis Pada Usia 6-8 Minggu | http://terminology.kemkes.go.id/sp |
| 67 | 513 | Observation | `Observation.component.valueCodeableConcept.coding` | LA15255-5 | Reactive | http://loinc.org |
| 68 | 514 | Observation | `Observation.component.valueCodeableConcept.coding` | LA15256-3 | Nonreactive | http://loinc.org |
| 69 | 515 | Observation | `Observation.component.code.coding` | SP000172 | Tanggal Konfirmasi Dry Blood Spot Early Infant Diagnosis dalam 12 Bulan | http://terminology.kemkes.go.id/sp |
| 70 | 517 | Observation | `Observation.component.code.coding` | SP000168 | Hasil Konfirmasi Dry Blood Spot Early Infant Diagnosis dalam 12 Bulan | http://terminology.kemkes.go.id/sp |
| 71 | 518 | Observation | `Observation.component.valueCodeableConcept.coding` | LA15255-5 | Reactive | http://loinc.org |
| 72 | 519 | Observation | `Observation.component.valueCodeableConcept.coding` | LA15256-3 | Nonreactive | http://loinc.org |
| 73 | 520 | Observation | `Observation.component.code.coding` | SP000173 | Tanggal Deteksi Serologis HIV Usia > 9 Bulan | http://terminology.kemkes.go.id/sp |
| 74 | 522 | Observation | `Observation.component.code.coding` | SP000174 | Hasil Deteksi Serologis HIV Usia > 9 Bulan | http://terminology.kemkes.go.id/sp |
| 75 | 523 | Observation | `Observation.component.valueCodeableConcept.coding` | LA15255-5 | Reactive | http://loinc.org |
| 76 | 524 | Observation | `Observation.component.valueCodeableConcept.coding` | LA15256-3 | Nonreactive | http://loinc.org |
| 77 | 525 | Observation | `Observation.component.code.coding` | SP000175 | Tanggal Dirawat di Perawatan, Dukungan, dan Pengobatan (PDP) Saat Balita | http://terminology.kemkes.go.id/sp |
| 78 | 527 | Observation | `Observation.component.code.coding` | SP000176 | Tanggal Mendapat ARV Profilaksis Saat Balita | http://terminology.kemkes.go.id/sp |
| 79 | 537 | Procedure | `Procedure.code.coding` | SP000126 | ARV Profilaksis | http://terminology.kemkes.go.id/sp |
| 80 | 548 | Observation | `Observation.code.coding` | SP000167 | Hasil Dry Blood Spot Early Infant Diagnosis Pada Usia 6-8 Minggu | http://terminology.kemkes.go.id/sp |
| 81 | 559 | Observation | `Observation.code.coding` | SP000168 | Hasil Konfirmasi Dry Blood Spot Early Infant Diagnosis dalam 12 Bulan | http://terminology.kemkes.go.id/sp |
| 82 | 603 | Observation | `Observation.code.coding` | SP000177 | Pemantauan Anak dari Ibu Sifilis | http://terminology.kemkes.go.id/sp |
| 83 | 606 | Observation | `Observation.component.code.coding` | SP000178 | Bayi Ditangani atau Dirujuk | http://terminology.kemkes.go.id/sp |
| 84 | 609 | Observation | `Observation.component.code.coding` | SP000179 | Tanggal Screening Sifilis Pada Usia < 2 Tahun | http://terminology.kemkes.go.id/sp |
| 85 | 611 | Observation | `Observation.component.code.coding` | SP000180 | Hasil Pemeriksaan Sifilis Pada Usia < 2 Tahun | http://terminology.kemkes.go.id/sp |
| 86 | 612 | Observation | `Observation.component.valueCodeableConcept.coding` | LA15255-5 | Reactive | http://loinc.org |
| 87 | 613 | Observation | `Observation.component.valueCodeableConcept.coding` | LA15256-3 | Nonreactive | http://loinc.org |
| 88 | 646 | Observation | `Observation.code.coding` | SP000181 | Pemantauan Anak dari Ibu Hepatitis | http://terminology.kemkes.go.id/sp |
| 89 | 649 | Observation | `Observation.component.code.coding` | SP000182 | Tanggal atau Jam Imunisasi HB 0 | http://terminology.kemkes.go.id/sp |
| 90 | 650 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000183 | < 24 jam | http://terminology.kemkes.go.id/sp |
| 91 | 651 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000184 | ≥ 24 jam | http://terminology.kemkes.go.id/sp |
| 92 | 652 | Observation | `Observation.component.code.coding` | SP000185 | Tanggal atau Jam Imunisasi HBIg | http://terminology.kemkes.go.id/sp |
| 93 | 653 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000183 | < 24 jam | http://terminology.kemkes.go.id/sp |
| 94 | 654 | Observation | `Observation.component.valueCodeableConcept.coding` | SP000184 | ≥ 24 jam | http://terminology.kemkes.go.id/sp |
| 95 | 655 | Observation | `Observation.component.code.coding` | SP000186 | Tanggal Imunisasi DPT/HB 1 | http://terminology.kemkes.go.id/sp |
| 96 | 657 | Observation | `Observation.component.code.coding` | SP000187 | Tanggal Imunisasi DPT/HB 2 | http://terminology.kemkes.go.id/sp |
| 97 | 659 | Observation | `Observation.component.code.coding` | SP000188 | Tanggal Imunisasi DPT/HB 3 | http://terminology.kemkes.go.id/sp |
| 98 | 661 | Observation | `Observation.component.code.coding` | SP000189 | Tanggal Screening HBsAg Pada Usia 9-12 Bulan | http://terminology.kemkes.go.id/sp |
| 99 | 663 | Observation | `Observation.component.code.coding` | SP000190 | Hasil Pemeriksaan HBsAg Pada Usia 9-12 Bulan | http://terminology.kemkes.go.id/sp |
| 100 | 664 | Observation | `Observation.component.valueCodeableConcept.coding` | LA15255-5 | Reactive | http://loinc.org |
| 101 | 665 | Observation | `Observation.component.valueCodeableConcept.coding` | LA15256-3 | Nonreactive | http://loinc.org |
| 102 | 666 | Observation | `Observation.component.code.coding` | SP000191 | Tanggal Screening Anti HBs Pada Usia 9 - 12 Bulan | http://terminology.kemkes.go.id/sp |
| 103 | 668 | Observation | `Observation.component.code.coding` | SP000192 | Hasil Pemeriksaan Anti HBs Pada Usia 9 - 12 Bulan | http://terminology.kemkes.go.id/sp |
| 104 | 669 | Observation | `Observation.component.valueCodeableConcept.coding` | LA15255-5 | Reactive | http://loinc.org |
| 105 | 670 | Observation | `Observation.component.valueCodeableConcept.coding` | LA15256-3 | Nonreactive | http://loinc.org |
| 106 | 680 | Immunization | `Immunization.vaccineCode` | VG45 | HepB | http://sys-ids.kemkes.go.id/kfa |
| 107 | 772 | Observation | `Observation.code.coding` | 121912002 | Hepatitis B virus deoxyribonucleic acid assay | http://snomed.info/sct |
| 108 | 783 | Observation | `Observation.code.coding` | 313476009 | Hepatitis B e antigen test | http://snomed.info/sct |
| 109 | 794 | Observation | `Observation.code.coding` | 34608000 | Alanine aminotransferase measurement | http://snomed.info/sct |
| 110 | 805 | Observation | `Observation.code.coding` | SP000193 | Memenuhi Kriteria Pengobatan Pencegahan Hepatitis B | http://terminology.kemkes.go.id/sp |
| 111 | 817 | Observation | `Observation.code.coding` | SP000194 | Metode Pemeriksaan Sirosis | http://terminology.kemkes.go.id/sp |
| 112 | 828 | Observation | `Observation.code.coding` | SP000195 | Status Sirosis | http://terminology.kemkes.go.id/sp |
| 113 | 839 | Observation | `Observation.code.coding` | SP000196 | Status Pengobatan Pencegahan Hepatitis B | http://terminology.kemkes.go.id/sp |
| 114 | 851 | Observation | `Observation.code.coding` | SP000197 | Tanggal Pengambilan Obat Pencegahan Hepatitis B | http://terminology.kemkes.go.id/sp |
| 115 | 863 | Observation | `Observation.code.coding` | SP000197 | Tanggal Pengambilan Obat Pencegahan Hepatitis B | http://terminology.kemkes.go.id/sp |
| 116 | 875 | Observation | `Observation.code.coding` | SP000197 | Tanggal Pengambilan Obat Pencegahan Hepatitis B | http://terminology.kemkes.go.id/sp |
| 117 | 887 | Observation | `Observation.code.coding` | SP000197 | Tanggal Pengambilan Obat Pencegahan Hepatitis B | http://terminology.kemkes.go.id/sp |
| 118 | 898 | Observation | `Observation.code.coding` | SP000198 | Status Akhir Pengobatan Pencegahan Hepatitis B | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://terminology.kemkes.go.id/sp | 49 |
| http://loinc.org | 36 |
| http://snomed.info/sct | 15 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 8 |
| http://terminology.kemkes.go.id/CodeSystem/organization-type | 8 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 1 |
| http://sys-ids.kemkes.go.id/kfa | 1 |
| **Total** | **118** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 907 | ⚠️ TRUE | Keterangan | – | `` |
