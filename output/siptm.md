# Output Form: SIPTM

Sumber: `mapping/phdt-data-dictionary-siptm.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-siptm.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 52 |
| Code (`jumlah code` = 1) | 214 |
| Code unik (code + CodeSystem) | 121 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 7 |
| Variabel BQ (unik) | 0 |
| Variabel raw (variabel dictionary; belum ada file mentah) | 60 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–24 | Patient | – | – | _IDENTITAS PESERTA PUSKESMAS-NIK--_ → `Patient.identifier.value` (4, tanpa BQ)<br>_IDENTITAS PESERTA PUSKESMAS-NAMA PASIEN*--_ → `Patient.name.text` (5, tanpa BQ)<br>_IDENTITAS PESERTA PUSKESMAS-JENIS KELAMIN *--_ → `Patient.gender` (7, tanpa BQ)<br>_IDENTITAS PESERTA PUSKESMAS-NO.TELP/HP--_ → `Patient.telecom.value` (10, tanpa BQ)<br>_IDENTITAS PESERTA PUSKESMAS-PROVINSI ASAL PASIEN (JIKA TIDAK DIISI AKAN MENGIKUTI PROVINSI PUSKESMAS)--_ → `Patient.address.extension.extension.valueCode` (14, tanpa BQ)<br>_IDENTITAS PESERTA PUSKESMAS-KOTA/KAB. ASAL PASIEN (JIKA TIDAK DIISI AKAN MENGIKUTI KAB.KOT PUSKESMAS)--_ → `Patient.address.extension.extension.valueCode` (17, tanpa BQ)<br>_IDENTITAS PESERTA PUSKESMAS-ALAMAT*--_ → `Patient.address.line` (18, tanpa BQ)<br>_IDENTITAS PESERTA PUSKESMAS-TANGGAL LAHIR *--_ → `Patient.birthDate` (21, tanpa BQ)<br>_IDENTITAS PESERTA PUSKESMAS-STATUS PERKAWINAN--_ → `Patient.maritalStatus.coding` (22, tanpa BQ) |
| 2 | 25–41 | Observation | 82589-3 | Highest level of education | _IDENTITAS PESERTA PUSKESMAS-STATUS PENDIDIKAN--_ → `Observation.valueCodeableConcept.coding` (28, tanpa BQ) |
| 3 | 42–72 | Observation | 85658-3 | Occupation [Type] | _IDENTITAS PESERTA PUSKESMAS-PEKERJAAN--_ → `Observation.valueCodeableConcept.coding` (45, tanpa BQ) |
| 4 | 73–86 | Observation | 883-9 | ABO group [Type] in Blood | _IDENTITAS PESERTA PUSKESMAS-GOLONGAN DARAH--_ → `Observation.valueCodeableConcept.coding` (76, tanpa BQ) |
| 5 | 87–100 | Encounter | – | – | _TANGGAL PEMERIKSAAN*---_ → `Encounter.identifier` (87, tanpa BQ)<br>_FORM UBM-RUJUK UBM--_ → `Encounter.hospitalization.dischargeDisposition.coding` (755, tanpa BQ) |
| 6 | 101–107 | Condition | Z00.8 | Other general exemination | – |
| 7 | 119–130 | Observation | 8480-6 | Systolic blood pressure | _TEKANAN DARAH-SISTOL--_ → `Observation.valueQuantity.value` (122, tanpa BQ) |
| 8 | 131–142 | Observation | 8462-4 | Diastolic blood pressure | _TEKANAN DARAH-DIASTOL--_ → `Observation.valueQuantity.value` (134, tanpa BQ) |
| 9 | 143–152 | ServiceRequest | – | – | _PEMERIKSAAN GULA---_ → `ServiceRequest.category` (143, tanpa BQ) |
| 10 | 157–164 | Specimen | – | – | – |
| 11 | 165–176 | Observation | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | – |
| 12 | 177–188 | DiagnosticReport | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | – |
| 13 | 189–200 | Observation | 8302-2 | Body height | _IMT-TINGGI BADAN(CM)--_ → `Observation.valueQuantity.value` (192, tanpa BQ) |
| 14 | 201–212 | Observation | 29463-7 | Body weight | _IMT-BERAT BADAN (KG)--_ → `Observation.valueQuantity.value` (204, tanpa BQ) |
| 15 | 213–223 | Observation | 396552003 | Abdominal circumference | _LINGKAR PERUT(CM)---_ → `Observation.valueQuantity.value` (215, tanpa BQ) |
| 16 | 224–235 | Observation | 21324001 | Refraction of eye, function (observable entity) | _GANGGUAN INDERA-GANGGUAN PENGLIHATAN-KELAINAN REFRAKSI-MATA KANAN_ → `Observation.valueBoolean` (227, tanpa BQ) |
| 17 | 236–247 | Observation | 21324001 | Refraction of eye, function (observable entity) | _GANGGUAN INDERA-GANGGUAN PENGLIHATAN-KELAINAN REFRAKSI-MATA KIRI_ → `Observation.valueBoolean` (239, tanpa BQ) |
| 18 | 248–258 | ServiceRequest | – | – | _GANGGUAN INDERA-GANGGUAN PENGLIHATAN-KELAINAN REFRAKSI-RUJUK RS_ → `ServiceRequest.category` (248, tanpa BQ)<br>_GANGGUAN INDERA-GANGGUAN PENGLIHATAN-KATARAK-RUJUK RS_ → `ServiceRequest.status` (249, tanpa BQ)<br>_GANGGUAN INDERA-GANGGUAN PENDENGARAN-SERUMEN-RUJUK RS_ → `ServiceRequest.intent` (250, tanpa BQ)<br>_GANGGUAN INDERA-GANGGUAN PENDENGARAN-(OMSK/CONGEK)-RUJUK RS_ → `ServiceRequest.priority` (251, tanpa BQ) |
| 19 | 259–269 | Observation | 816120008 | Cataract of right eye | _GANGGUAN INDERA-GANGGUAN PENGLIHATAN-KATARAK-MATA KANAN_ → `Observation.valueBoolean` (261, tanpa BQ) |
| 20 | 270–280 | Observation | 816119002 | Cataract of left eye | _GANGGUAN INDERA-GANGGUAN PENGLIHATAN-KATARAK-MATA KIRI_ → `Observation.valueBoolean` (272, tanpa BQ) |
| 21 | 281–292 | Observation | OC000150 | Suspek tuli kongenital | _GANGGUAN INDERA-GANGGUAN PENDENGARAN-CURIGA TULI KONGENITAL-TELINGA KANAN_ → `Observation.valueBoolean` (284, tanpa BQ) |
| 22 | 293–304 | Observation | OC000150 | Suspek tuli kongenital | _GANGGUAN INDERA-GANGGUAN PENDENGARAN-CURIGA TULI KONGENITAL-TELINGA KIRI_ → `Observation.valueBoolean` (296, tanpa BQ) |
| 23 | 306–317 | Observation | 18070006 | Impacted cerumen | _GANGGUAN INDERA-GANGGUAN PENDENGARAN-SERUMEN-TELINGA KANAN_ → `Observation.valueBoolean` (309, tanpa BQ) |
| 24 | 318–329 | Observation | 18070006 | Impacted cerumen | _GANGGUAN INDERA-GANGGUAN PENDENGARAN-SERUMEN-TELINGA KIRI_ → `Observation.valueBoolean` (321, tanpa BQ) |
| 25 | 330–341 | Observation | 1091181000119108 | Chronic suppurative otitis media of right middle ear | _GANGGUAN INDERA-GANGGUAN PENDENGARAN-(OMSK/CONGEK)-TELINGA KANAN_ → `Observation.valueBoolean` (333, tanpa BQ) |
| 26 | 342–353 | Observation | 1088571000119107 | Chronic suppurative otitis media of left middle ear | _GANGGUAN INDERA-GANGGUAN PENDENGARAN-(OMSK/CONGEK)-TELINGA KIRI_ → `Observation.valueBoolean` (345, tanpa BQ) |
| 27 | 354–366 | Observation | X099241 | Tes IVA | _PEMERIKSAAN IVA & SADANIS-PEMERIKSAAN IVA-HASIL IVA-_ → `Observation.valueCodeableConcept.coding` (356, tanpa BQ) |
| 28 | 367–377 | Observation | – | – | _PEMERIKSAAN IVA & SADANIS-PEMERIKSAAN IVA-TINDAK LANJUT IVA POSITIF-_ → `Observation.valueCodeableConcept.coding` (369, tanpa BQ) |
| 29 | 379–390 | Observation | 13607009 | Manual examination of breast | _PEMERIKSAAN IVA & SADANIS-PEMERIKSAAN SADANIS-HASIL SADANIS-_ → `Observation.valueCodeableConcept.coding` (381, tanpa BQ) |
| 30 | 391–400 | Observation | – | – | _PEMERIKSAAN IVA & SADANIS-PEMERIKSAAN SADANIS-TINDAK LANJUT SADANIS-_ → `Observation.valueCodeableConcept.coding` (393, tanpa BQ) |
| 31 | 402–440 | FamilyMemberHistory | – | – | _RIWAYAT PENYAKIT TIDAK MENULAR PADA KELUARGA-RIWAYAT 1--_ → `FamilyMemberHistory.status` (402, tanpa BQ)<br>_RIWAYAT PENYAKIT TIDAK MENULAR PADA KELUARGA-RIWAYAT 2--_ → `FamilyMemberHistory.status` (415, tanpa BQ)<br>_RIWAYAT PENYAKIT TIDAK MENULAR PADA KELUARGA-RIWAYAT 3--_ → `FamilyMemberHistory.status` (428, tanpa BQ) |
| 32 | 441–453 | Condition | 161445009 | H/O: diabetes mellitus | _RIWAYAT PENYAKIT TIDAK MENULAR PADA DIRI SENDIRI-RIWAYAT 1--_ → `Condition.clinicalStatus.coding` (441, tanpa BQ) |
| 33 | 454–466 | Condition | 161445009 | H/O: diabetes mellitus | _RIWAYAT PENYAKIT TIDAK MENULAR PADA DIRI SENDIRI-RIWAYAT 2--_ → `Condition.clinicalStatus.coding` (454, tanpa BQ) |
| 34 | 467–479 | Condition | 161445009 | H/O: diabetes mellitus | _RIWAYAT PENYAKIT TIDAK MENULAR PADA DIRI SENDIRI-RIWAYAT 3--_ → `Condition.clinicalStatus.coding` (467, tanpa BQ) |
| 35 | 480–490 | Observation | 110483000 | Tobacco user | _FAKTOR RISIKO-MEROKOK--_ → `Observation.valueBoolean` (483, tanpa BQ) |
| 36 | 491–501 | Observation | 43994002 | Lack of physical activity | _FAKTOR RISIKO-KURANG AKTIFITAS FISIK--_ → `Observation.valueBoolean` (494, tanpa BQ) |
| 37 | 502–512 | Observation | 412744006 | High sugar diet | _FAKTOR RISIKO-POLA MAKAN-GULA BERLEBIHAN-_ → `Observation.valueBoolean` (505, tanpa BQ) |
| 38 | 513–523 | Observation | 440921000124100 | Excessive sodium intake | _FAKTOR RISIKO-POLA MAKAN-GARAM BERLEBIHAN-_ → `Observation.valueBoolean` (516, tanpa BQ) |
| 39 | 524–534 | Observation | 846619006 | Excessive intake of fat and oil | _FAKTOR RISIKO-POLA MAKAN-LEMAK BERLEBIHAN-_ → `Observation.valueBoolean` (527, tanpa BQ) |
| 40 | 535–545 | Observation | SP000650 | Pola Makan Kurang Makan Buah dan Sayur | _FAKTOR RISIKO-POLA MAKAN-KURANG MAKAN BUAH DAN SAYUR-_ → `Observation.valueBoolean` (538, tanpa BQ) |
| 41 | 546–556 | Observation | 219006 | Current drinker of alcohol | _FAKTOR RISIKO-KONSUMSI ALKOHOL--_ → `Observation.valueBoolean` (549, tanpa BQ) |
| 42 | 557–598 | Condition | E11.9 | Non-insulin-dependent diabetes mellitus | _DIAGNOSIS-DIAGNOSIS 1--_ → `Condition.clinicalStatus.coding` (557, tanpa BQ) |
| 43 | 599–640 | Condition | E11.9 | Non-insulin-dependent diabetes mellitus | _DIAGNOSIS-DIAGNOSIS 2--_ → `Condition.clinicalStatus.coding` (599, tanpa BQ) |
| 44 | 641–682 | Condition | E11.9 | Non-insulin-dependent diabetes mellitus | _DIAGNOSIS-DIAGNOSIS 3--_ → `Condition.clinicalStatus.coding` (641, tanpa BQ) |
| 45 | 683–695 | MedicationRequest | – | – | _TERAPI FARMAKOLOGI---_ → `MedicationRequest.status` (683, tanpa BQ) |
| 46 | 696–706 | Procedure | 61310001 | Nutrition education | _KONSELING, INFORMASI DAN EDUKASI KESAHATAN---_ → `Procedure.category.coding` (696, tanpa BQ) |
| 47 | 707–723 | Procedure | 94.4 | Other psychotherapy and counselling | _FORM UBM-KONSELING--_ → `Procedure.category.coding` (707, tanpa BQ) |
| 48 | 724–742 | Goal | – | – | _FORM UBM-CAR--_ → `Goal.category.coding` (724, tanpa BQ)<br>_FORM UBM-KONDISI--_ → `Goal.category.coding` (735, tanpa BQ) |
| 49 | 743–751 | Goal | – | – | – |
| 50 | 752–754 | Goal | – | – | – |
| 51 | 756–769 | Observation | SP000649 | Status CAR saat dirujuk | – |
| 52 | 770–781 | ServiceRequest | – | – | – |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 31 |
| Condition | 7 |
| ServiceRequest | 3 |
| Goal | 3 |
| Procedure | 2 |
| Patient | 1 |
| Encounter | 1 |
| Specimen | 1 |
| DiagnosticReport | 1 |
| FamilyMemberHistory | 1 |
| MedicationRequest | 1 |
| **Total** | **52** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 27 | Observation | `Observation.code.coding` | 82589-3 | Highest level of education | http://loinc.org |
| 2 | 28 | Observation | `Observation.valueCodeableConcept.coding` | 473463000 | Received elementary school education | http://snomed.info/sct |
| 3 | 29 | Observation | `Observation.valueCodeableConcept.coding` | 603435002 | Educated to junior high school level | http://snomed.info/sct |
| 4 | 30 | Observation | `Observation.valueCodeableConcept.coding` | 603434003 | Educated to senior high school level | http://snomed.info/sct |
| 5 | 31 | Observation | `Observation.valueCodeableConcept.coding` | 38861000087100 | Bachelor's degree achieved | http://snomed.info/sct |
| 6 | 32 | Observation | `Observation.valueCodeableConcept.coding` | 440344006 | Received postgraduate education | http://snomed.info/sct |
| 7 | 33 | Observation | `Observation.valueCodeableConcept.coding` | 224294005 | No formal education | http://snomed.info/sct |
| 8 | 34 | Observation | `Observation.valueCodeableConcept.coding` | 38901000087109 | University diploma achieved | http://snomed.info/sct |
| 9 | 44 | Observation | `Observation.code.coding` | 85658-3 | Occupation [Type] | http://loinc.org |
| 10 | 45 | Observation | `Observation.valueCodeableConcept.coding` | 106540006 | Laborer | http://snomed.info/sct |
| 11 | 46 | Observation | `Observation.valueCodeableConcept.coding` | 160906004 | Self-employed | http://snomed.info/sct |
| 12 | 47 | Observation | `Observation.valueCodeableConcept.coding` | SP000244 | Pedagang kecil | http://terminology.kemkes.go.id/sp |
| 13 | 48 | Observation | `Observation.valueCodeableConcept.coding` | 236297007 | Civil servant | http://snomed.info/sct |
| 14 | 49 | Observation | `Observation.valueCodeableConcept.coding` | 302314004 | Military personnel | http://snomed.info/sct |
| 15 | 50 | Observation | `Observation.valueCodeableConcept.coding` | 14406004 | Policeman | http://snomed.info/sct |
| 16 | 51 | Observation | `Observation.valueCodeableConcept.coding` | TK000041 | Pegawai/karyawan swasta | http://terminology.kemkes.go.id |
| 17 | 52 | Observation | `Observation.valueCodeableConcept.coding` | 73438004 | Unemployed | http://snomed.info/sct |
| 18 | 53 | Observation | `Observation.valueCodeableConcept.coding` | 77715000 | Fisherman | http://snomed.info/sct |
| 19 | 54 | Observation | `Observation.valueCodeableConcept.coding` | 106388008 | Farmer | http://snomed.info/sct |
| 20 | 55 | Observation | `Observation.valueCodeableConcept.coding` | 36625000 | Livestock worker | http://snomed.info/sct |
| 21 | 56 | Observation | `Observation.valueCodeableConcept.coding` | 105493001 | Retired, life even | http://snomed.info/sct |
| 22 | 57 | Observation | `Observation.valueCodeableConcept.coding` | SP000288 | Tenaga Kerja Indonesia | http://terminology.kemkes.go.id/sp |
| 23 | 58 | Observation | `Observation.valueCodeableConcept.coding` | 444168002 | Homemaker | http://snomed.info/sct |
| 24 | 59 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 25 | 60 | Observation | `Observation.valueCodeableConcept.coding` | 236320001 | Vehicle driver | http://snomed.info/sct |
| 26 | 61 | Observation | `Observation.valueCodeableConcept.coding` | 158891000 | University lecturer | http://snomed.info/sct |
| 27 | 62 | Observation | `Observation.valueCodeableConcept.coding` | 106304008 | Teacher | http://snomed.info/sct |
| 28 | 63 | Observation | `Observation.valueCodeableConcept.coding` | 158965000 | Medical practitioner | http://snomed.info/sct |
| 29 | 64 | Observation | `Observation.valueCodeableConcept.coding` | 309453006 | Registered midwife | http://snomed.info/sct |
| 30 | 65 | Observation | `Observation.valueCodeableConcept.coding` | 65853000 | Student | http://snomed.info/sct |
| 31 | 75 | Observation | `Observation.code.coding` | 883-9 | ABO group [Type] in Blood | http://loinc.org |
| 32 | 76 | Observation | `Observation.valueCodeableConcept.coding` | LA19710-5 | Group A | http://loinc.org |
| 33 | 77 | Observation | `Observation.valueCodeableConcept.coding` | LA19709-7 | Group B | http://loinc.org |
| 34 | 78 | Observation | `Observation.valueCodeableConcept.coding` | LA19708-9 | Group O | http://loinc.org |
| 35 | 79 | Observation | `Observation.valueCodeableConcept.coding` | LA28449-9 | Group AB | http://loinc.org |
| 36 | 103 | Condition | `Condition.code.coding` | Z00.8 | Other general exemination | http://hl7.org/fhir/sid/icd-10 |
| 37 | 121 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 38 | 133 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://loinc.org |
| 39 | 147 | ServiceRequest | `ServiceRequest.code` | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | http://loinc.org |
| 40 | 158 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 41 | 167 | Observation | `Observation.code.coding` | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | http://loinc.org |
| 42 | 179 | DiagnosticReport | `DiagnosticReport.code.coding` | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | http://loinc.org |
| 43 | 191 | Observation | `Observation.code.coding` | 8302-2 | Body height | http://loinc.org |
| 44 | 203 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 45 | 214 | Observation | `Observation.code.coding` | 396552003 | Abdominal circumference | http://snomed.info/sct |
| 46 | 225 | Observation | `Observation.code.coding` | 21324001 | Refraction of eye, function (observable entity) | http://snomed.info/sct |
| 47 | 237 | Observation | `Observation.code.coding` | 21324001 | Refraction of eye, function (observable entity) | http://snomed.info/sct |
| 48 | 252 | ServiceRequest | `ServiceRequest.code` | 737492002 | Outpatient care management | http://snomed.info/sct |
| 49 | 260 | Observation | `Observation.code.coding` | 816120008 | Cataract of right eye | http://snomed.info/sct |
| 50 | 271 | Observation | `Observation.code.coding` | 816119002 | Cataract of left eye | http://snomed.info/sct |
| 51 | 282 | Observation | `Observation.code.coding` | OC000150 | Suspek tuli kongenital | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 52 | 294 | Observation | `Observation.code.coding` | OC000150 | Suspek tuli kongenital | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 53 | 307 | Observation | `Observation.code.coding` | 18070006 | Impacted cerumen | http://snomed.info/sct |
| 54 | 319 | Observation | `Observation.code.coding` | 18070006 | Impacted cerumen | http://snomed.info/sct |
| 55 | 331 | Observation | `Observation.code.coding` | 1091181000119108 | Chronic suppurative otitis media of right middle ear | http://snomed.info/sct |
| 56 | 343 | Observation | `Observation.code.coding` | 1088571000119107 | Chronic suppurative otitis media of left middle ear | http://snomed.info/sct |
| 57 | 355 | Observation | `Observation.code.coding` | X099241 | Tes IVA | http://terminology.kemkes.go.id/CodeSystem/examination |
| 58 | 356 | Observation | `Observation.valueCodeableConcept.coding` | 300558006 | Aceto-white reaction negative | http://snomed.info/sct |
| 59 | 357 | Observation | `Observation.valueCodeableConcept.coding` | 300557001 | Aceto-white reaction positive | http://snomed.info/sct |
| 60 | 358 | Observation | `Observation.valueCodeableConcept.coding` | 37610005 | Inflammation of cervix | http://snomed.info/sct |
| 61 | 359 | Observation | `Observation.valueCodeableConcept.coding` | 315266007 | Suspected cervical cancer | http://snomed.info/sct |
| 62 | 369 | Observation | `Observation.valueCodeableConcept.coding` | 26782000 | Cryotherapy | http://snomed.info/sct |
| 63 | 370 | Observation | `Observation.valueCodeableConcept.coding` | 3457005 | Patient referral | http://snomed.info/sct |
| 64 | 380 | Observation | `Observation.code.coding` | 13607009 | Manual examination of breast | http://snomed.info/sct |
| 65 | 381 | Observation | `Observation.valueCodeableConcept.coding` | 89164003 | Breast lump | http://snomed.info/sct |
| 66 | 382 | Observation | `Observation.valueCodeableConcept.coding` | 290084006 | Breast normal | http://snomed.info/sct |
| 67 | 383 | Observation | `Observation.valueCodeableConcept.coding` | 134405005 | Suspected breast cancer | http://snomed.info/sct |
| 68 | 393 | Observation | `Observation.valueCodeableConcept.coding` | 3457005 | Patient referral | http://snomed.info/sct |
| 69 | 443 | Condition | `Condition.code.coding` | 161445009 | H/O: diabetes mellitus | http://snomed.info/sct |
| 70 | 444 | Condition | `Condition.code.coding` | 161501007 | H/O: hypertension | http://snomed.info/sct |
| 71 | 445 | Condition | `Condition.code.coding` | 266995000 | H/O: cardiovascular disease | http://snomed.info/sct |
| 72 | 446 | Condition | `Condition.code.coding` | 275526006 | History of cerebrovascular accident | http://snomed.info/sct |
| 73 | 447 | Condition | `Condition.code.coding` | 161527007 | H/O: asthma | http://snomed.info/sct |
| 74 | 448 | Condition | `Condition.code.coding` | 266987004 | History of malignant neoplasm | http://snomed.info/sct |
| 75 | 449 | Condition | `Condition.code.coding` | 414416008 | History of hypercholesterolemia | http://snomed.info/sct |
| 76 | 456 | Condition | `Condition.code.coding` | 161445009 | H/O: diabetes mellitus | http://snomed.info/sct |
| 77 | 457 | Condition | `Condition.code.coding` | 161501007 | H/O: hypertension | http://snomed.info/sct |
| 78 | 458 | Condition | `Condition.code.coding` | 266995000 | H/O: cardiovascular disease | http://snomed.info/sct |
| 79 | 459 | Condition | `Condition.code.coding` | 275526006 | History of cerebrovascular accident | http://snomed.info/sct |
| 80 | 460 | Condition | `Condition.code.coding` | 161527007 | H/O: asthma | http://snomed.info/sct |
| 81 | 461 | Condition | `Condition.code.coding` | 266987004 | History of malignant neoplasm | http://snomed.info/sct |
| 82 | 462 | Condition | `Condition.code.coding` | 414416008 | History of hypercholesterolemia | http://snomed.info/sct |
| 83 | 469 | Condition | `Condition.code.coding` | 161445009 | H/O: diabetes mellitus | http://snomed.info/sct |
| 84 | 470 | Condition | `Condition.code.coding` | 161501007 | H/O: hypertension | http://snomed.info/sct |
| 85 | 471 | Condition | `Condition.code.coding` | 266995000 | H/O: cardiovascular disease | http://snomed.info/sct |
| 86 | 472 | Condition | `Condition.code.coding` | 275526006 | History of cerebrovascular accident | http://snomed.info/sct |
| 87 | 473 | Condition | `Condition.code.coding` | 161527007 | H/O: asthma | http://snomed.info/sct |
| 88 | 474 | Condition | `Condition.code.coding` | 266987004 | History of malignant neoplasm | http://snomed.info/sct |
| 89 | 475 | Condition | `Condition.code.coding` | 414416008 | History of hypercholesterolemia | http://snomed.info/sct |
| 90 | 482 | Observation | `Observation.code.coding` | 110483000 | Tobacco user | http://snomed.info/sct |
| 91 | 493 | Observation | `Observation.code.coding` | 43994002 | Lack of physical activity | http://snomed.info/sct |
| 92 | 504 | Observation | `Observation.code.coding` | 412744006 | High sugar diet | http://snomed.info/sct |
| 93 | 515 | Observation | `Observation.code.coding` | 440921000124100 | Excessive sodium intake | http://snomed.info/sct |
| 94 | 526 | Observation | `Observation.code.coding` | 846619006 | Excessive intake of fat and oil | http://snomed.info/sct |
| 95 | 537 | Observation | `Observation.code.coding` | SP000650 | Pola Makan Kurang Makan Buah dan Sayur | http://terminology.kemkes.go.id/sp |
| 96 | 548 | Observation | `Observation.code.coding` | 219006 | Current drinker of alcohol | http://snomed.info/sct |
| 97 | 559 | Condition | `Condition.code.coding` | E11.9 | Non-insulin-dependent diabetes mellitus | http://hl7.org/fhir/sid/icd-10 |
| 98 | 560 | Condition | `Condition.code.coding` | J45.9 | Asthma, unspecified |  |
| 99 | 561 | Condition | `Condition.code.coding` | E78.0 | Pure hypercholesterolaemia |  |
| 100 | 562 | Condition | `Condition.code.coding` | O24.4 | Diabetes mellitus arising in pregnancy |  |
| 101 | 563 | Condition | `Condition.code.coding` | E10.9 | Insulin-dependent diabetes mellitus |  |
| 102 | 564 | Condition | `Condition.code.coding` | SP000648 | Diabetes Mellitus dengan Tuberkulosis | http://terminology.kemkes.go.id/sp |
| 103 | 565 | Condition | `Condition.code.coding` | I50.9 | Heart failure, unspecified |  |
| 104 | 566 | Condition | `Condition.code.coding` | H52.7 | Disorder of refraction, unspecified |  |
| 105 | 567 | Condition | `Condition.code.coding` | N18.9 | Chronic kidney disease, unspecified |  |
| 106 | 568 | Condition | `Condition.code.coding` | H40.9 | Glaucoma, unspecified |  |
| 107 | 569 | Condition | `Condition.code.coding` | I10 | Essential (primary) hypertension |  |
| 108 | 570 | Condition | `Condition.code.coding` | E05.9 | Thyrotoxicosis, unspecified |  |
| 109 | 571 | Condition | `Condition.code.coding` | N40 | Hyperplasia of prostate |  |
| 110 | 572 | Condition | `Condition.code.coding` | E03.9 | Hypothyroidism, unspecified |  |
| 111 | 573 | Condition | `Condition.code.coding` | I25.1 | Atherosclerotic heart disease |  |
| 112 | 574 | Condition | `Condition.code.coding` | C19 | Malignant neoplasm of rectosigmoid junction |  |
| 113 | 575 | Condition | `Condition.code.coding` | C50.9 | Breast, unspecified |  |
| 114 | 576 | Condition | `Condition.code.coding` | C53.9 | Cervix uteri, unspecified |  |
| 115 | 577 | Condition | `Condition.code.coding` | H26.9 | Cataract, unspecified |  |
| 116 | 578 | Condition | `Condition.code.coding` | C95.9 | Leukaemia, unspecified |  |
| 117 | 579 | Condition | `Condition.code.coding` | M32.9 | Systemic lupus erythematosus, unspecified |  |
| 118 | 580 | Condition | `Condition.code.coding` | H83.3 | Noise effects on inner ear |  |
| 119 | 581 | Condition | `Condition.code.coding` | E66.9 | Obesity, unspecified |  |
| 120 | 582 | Condition | `Condition.code.coding` | H66.3 | Other chronic suppurative otitis media |  |
| 121 | 583 | Condition | `Condition.code.coding` | M81.9 | Osteoporosis, unspecified |  |
| 122 | 584 | Condition | `Condition.code.coding` | J44.9 | Chronic obstructive pulmonary disease, unspecified |  |
| 123 | 585 | Condition | `Condition.code.coding` | H91.1 | Presbycusis |  |
| 124 | 586 | Condition | `Condition.code.coding` | L40.0 | Psoriasis vulgaris |  |
| 125 | 587 | Condition | `Condition.code.coding` | M06.9 | Rheumatoid arthritis, unspecified |  |
| 126 | 588 | Condition | `Condition.code.coding` | C69.2 | Retina |  |
| 127 | 589 | Condition | `Condition.code.coding` | H61.2 | Impacted cerumen |  |
| 128 | 590 | Condition | `Condition.code.coding` | I64 | Stroke, not specified as haemorrhage or infarction |  |
| 129 | 591 | Condition | `Condition.code.coding` | D56.9 | Thalassaemia, unspecified |  |
| 130 | 592 | Condition | `Condition.code.coding` | E07.9 | Disorder of thyroid, unspecified |  |
| 131 | 593 | Condition | `Condition.code.coding` | H90.5 | Sensorineural hearing loss, unspecified |  |
| 132 | 594 | Condition | `Condition.code.coding` | N87.0 | Mild cervical dysplasia |  |
| 133 | 601 | Condition | `Condition.code.coding` | E11.9 | Non-insulin-dependent diabetes mellitus | http://hl7.org/fhir/sid/icd-10 |
| 134 | 602 | Condition | `Condition.code.coding` | J45.9 | Asthma, unspecified |  |
| 135 | 603 | Condition | `Condition.code.coding` | E78.0 | Pure hypercholesterolaemia |  |
| 136 | 604 | Condition | `Condition.code.coding` | O24.4 | Diabetes mellitus arising in pregnancy |  |
| 137 | 605 | Condition | `Condition.code.coding` | E10.9 | Insulin-dependent diabetes mellitus |  |
| 138 | 606 | Condition | `Condition.code.coding` | SP000648 | Diabetes Mellitus dengan Tuberkulosis | http://terminology.kemkes.go.id/sp |
| 139 | 607 | Condition | `Condition.code.coding` | I50.9 | Heart failure, unspecified |  |
| 140 | 608 | Condition | `Condition.code.coding` | H52.7 | Disorder of refraction, unspecified |  |
| 141 | 609 | Condition | `Condition.code.coding` | N18.9 | Chronic kidney disease, unspecified |  |
| 142 | 610 | Condition | `Condition.code.coding` | H40.9 | Glaucoma, unspecified |  |
| 143 | 611 | Condition | `Condition.code.coding` | I10 | Essential (primary) hypertension |  |
| 144 | 612 | Condition | `Condition.code.coding` | E05.9 | Thyrotoxicosis, unspecified |  |
| 145 | 613 | Condition | `Condition.code.coding` | N40 | Hyperplasia of prostate |  |
| 146 | 614 | Condition | `Condition.code.coding` | E03.9 | Hypothyroidism, unspecified |  |
| 147 | 615 | Condition | `Condition.code.coding` | I25.1 | Atherosclerotic heart disease |  |
| 148 | 616 | Condition | `Condition.code.coding` | C19 | Malignant neoplasm of rectosigmoid junction |  |
| 149 | 617 | Condition | `Condition.code.coding` | C50.9 | Breast, unspecified |  |
| 150 | 618 | Condition | `Condition.code.coding` | C53.9 | Cervix uteri, unspecified |  |
| 151 | 619 | Condition | `Condition.code.coding` | H26.9 | Cataract, unspecified |  |
| 152 | 620 | Condition | `Condition.code.coding` | C95.9 | Leukaemia, unspecified |  |
| 153 | 621 | Condition | `Condition.code.coding` | M32.9 | Systemic lupus erythematosus, unspecified |  |
| 154 | 622 | Condition | `Condition.code.coding` | H83.3 | Noise effects on inner ear |  |
| 155 | 623 | Condition | `Condition.code.coding` | E66.9 | Obesity, unspecified |  |
| 156 | 624 | Condition | `Condition.code.coding` | H66.3 | Other chronic suppurative otitis media |  |
| 157 | 625 | Condition | `Condition.code.coding` | M81.9 | Osteoporosis, unspecified |  |
| 158 | 626 | Condition | `Condition.code.coding` | J44.9 | Chronic obstructive pulmonary disease, unspecified |  |
| 159 | 627 | Condition | `Condition.code.coding` | H91.1 | Presbycusis |  |
| 160 | 628 | Condition | `Condition.code.coding` | L40.0 | Psoriasis vulgaris |  |
| 161 | 629 | Condition | `Condition.code.coding` | M06.9 | Rheumatoid arthritis, unspecified |  |
| 162 | 630 | Condition | `Condition.code.coding` | C69.2 | Retina |  |
| 163 | 631 | Condition | `Condition.code.coding` | H61.2 | Impacted cerumen |  |
| 164 | 632 | Condition | `Condition.code.coding` | I64 | Stroke, not specified as haemorrhage or infarction |  |
| 165 | 633 | Condition | `Condition.code.coding` | D56.9 | Thalassaemia, unspecified |  |
| 166 | 634 | Condition | `Condition.code.coding` | E07.9 | Disorder of thyroid, unspecified |  |
| 167 | 635 | Condition | `Condition.code.coding` | H90.5 | Sensorineural hearing loss, unspecified |  |
| 168 | 636 | Condition | `Condition.code.coding` | N87.0 | Mild cervical dysplasia |  |
| 169 | 643 | Condition | `Condition.code.coding` | E11.9 | Non-insulin-dependent diabetes mellitus | http://hl7.org/fhir/sid/icd-10 |
| 170 | 644 | Condition | `Condition.code.coding` | J45.9 | Asthma, unspecified |  |
| 171 | 645 | Condition | `Condition.code.coding` | E78.0 | Pure hypercholesterolaemia |  |
| 172 | 646 | Condition | `Condition.code.coding` | O24.4 | Diabetes mellitus arising in pregnancy |  |
| 173 | 647 | Condition | `Condition.code.coding` | E10.9 | Insulin-dependent diabetes mellitus |  |
| 174 | 648 | Condition | `Condition.code.coding` | SP000648 | Diabetes Mellitus dengan Tuberkulosis | http://terminology.kemkes.go.id/sp |
| 175 | 649 | Condition | `Condition.code.coding` | I50.9 | Heart failure, unspecified |  |
| 176 | 650 | Condition | `Condition.code.coding` | H52.7 | Disorder of refraction, unspecified |  |
| 177 | 651 | Condition | `Condition.code.coding` | N18.9 | Chronic kidney disease, unspecified |  |
| 178 | 652 | Condition | `Condition.code.coding` | H40.9 | Glaucoma, unspecified |  |
| 179 | 653 | Condition | `Condition.code.coding` | I10 | Essential (primary) hypertension |  |
| 180 | 654 | Condition | `Condition.code.coding` | E05.9 | Thyrotoxicosis, unspecified |  |
| 181 | 655 | Condition | `Condition.code.coding` | N40 | Hyperplasia of prostate |  |
| 182 | 656 | Condition | `Condition.code.coding` | E03.9 | Hypothyroidism, unspecified |  |
| 183 | 657 | Condition | `Condition.code.coding` | I25.1 | Atherosclerotic heart disease |  |
| 184 | 658 | Condition | `Condition.code.coding` | C19 | Malignant neoplasm of rectosigmoid junction |  |
| 185 | 659 | Condition | `Condition.code.coding` | C50.9 | Breast, unspecified |  |
| 186 | 660 | Condition | `Condition.code.coding` | C53.9 | Cervix uteri, unspecified |  |
| 187 | 661 | Condition | `Condition.code.coding` | H26.9 | Cataract, unspecified |  |
| 188 | 662 | Condition | `Condition.code.coding` | C95.9 | Leukaemia, unspecified |  |
| 189 | 663 | Condition | `Condition.code.coding` | M32.9 | Systemic lupus erythematosus, unspecified |  |
| 190 | 664 | Condition | `Condition.code.coding` | H83.3 | Noise effects on inner ear |  |
| 191 | 665 | Condition | `Condition.code.coding` | E66.9 | Obesity, unspecified |  |
| 192 | 666 | Condition | `Condition.code.coding` | H66.3 | Other chronic suppurative otitis media |  |
| 193 | 667 | Condition | `Condition.code.coding` | M81.9 | Osteoporosis, unspecified |  |
| 194 | 668 | Condition | `Condition.code.coding` | J44.9 | Chronic obstructive pulmonary disease, unspecified |  |
| 195 | 669 | Condition | `Condition.code.coding` | H91.1 | Presbycusis |  |
| 196 | 670 | Condition | `Condition.code.coding` | L40.0 | Psoriasis vulgaris |  |
| 197 | 671 | Condition | `Condition.code.coding` | M06.9 | Rheumatoid arthritis, unspecified |  |
| 198 | 672 | Condition | `Condition.code.coding` | C69.2 | Retina |  |
| 199 | 673 | Condition | `Condition.code.coding` | H61.2 | Impacted cerumen |  |
| 200 | 674 | Condition | `Condition.code.coding` | I64 | Stroke, not specified as haemorrhage or infarction |  |
| 201 | 675 | Condition | `Condition.code.coding` | D56.9 | Thalassaemia, unspecified |  |
| 202 | 676 | Condition | `Condition.code.coding` | E07.9 | Disorder of thyroid, unspecified |  |
| 203 | 677 | Condition | `Condition.code.coding` | H90.5 | Sensorineural hearing loss, unspecified |  |
| 204 | 678 | Condition | `Condition.code.coding` | N87.0 | Mild cervical dysplasia |  |
| 205 | 697 | Procedure | `Procedure.code.coding` | 61310001 | Nutrition education | http://snomed.info/sct |
| 206 | 698 | Procedure | `Procedure.code.coding` | 304507003 | Exercise education | http://snomed.info/sct |
| 207 | 708 | Procedure | `Procedure.code.coding` | 94.4 | Other psychotherapy and counselling | http://hl7.org/fhir/sid/icd-9-cm |
| 208 | 758 | Observation | `Observation.code.coding` | SP000649 | Status CAR saat dirujuk | http://terminology.kemkes.go.id/sp |
| 209 | 759 | Observation | `Observation.valueCodeableConcept.coding` | TK000108 | CAR 3 | http://terminology.kemkes.go.id |
| 210 | 760 | Observation | `Observation.valueCodeableConcept.coding` | TK000109 | CAR 6 | http://terminology.kemkes.go.id |
| 211 | 761 | Observation | `Observation.valueCodeableConcept.coding` | TK000110 | CAR 9 | http://terminology.kemkes.go.id |
| 212 | 762 | Observation | `Observation.valueCodeableConcept.coding` | TK000111 | CAR 12 | http://terminology.kemkes.go.id |
| 213 | 774 | ServiceRequest | `ServiceRequest.code` | 737492002 | Outpatient care management | http://snomed.info/sct |
| 214 | 781 | ServiceRequest | `ServiceRequest.reasonCode.coding` | Z72.0 | Tobacco Use | http://hl7.org/fhir/sid/icd-10 |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
|  | 102 |
| http://snomed.info/sct | 77 |
| http://loinc.org | 14 |
| http://terminology.kemkes.go.id/sp | 7 |
| http://terminology.kemkes.go.id | 5 |
| http://hl7.org/fhir/sid/icd-10 | 5 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 2 |
| http://terminology.kemkes.go.id/CodeSystem/examination | 1 |
| http://hl7.org/fhir/sid/icd-9-cm | 1 |
| **Total** | **214** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 305 | – | GANGGUAN INDERA-GANGGUAN PENDENGARAN-CURIGA TULI KONGENITAL-RUJUK RS | – | `` |
