# Output Form: KuApps BidanKu - PNC

Sumber: `mapping/phdt-data-dictionary-kuapps-bidanku-pnc.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-kuapps-bidanku-pnc.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 49 |
| Code (`jumlah code` = 1) | 143 |
| Code unik (code + CodeSystem) | 138 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 2 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 3–11 | EpisodeOfCare | PNC | Postnatal Care | _Mulai PNC_ → `EpisodeOfCare.identifier` (3, tanpa BQ) |
| 2 | 12–28 | Encounter | – | – | _Kunjungan PNC (KF)_ → `Encounter.identifier` (12, tanpa BQ)<br>_Tanggal kunjungan_ → `Encounter.period.start` (16, tanpa BQ) |
| 3 | 29–36 | Condition | Z39.2 | Routine postpartum follow-up | – |
| 4 | 47–59 | Observation | 8302-2 | Body height | _Tinggi (cm)_ → `Observation.valueQuantity.value` (51, tanpa BQ) |
| 5 | 60–71 | Observation | 29463-7 | Body weight | _Berat saat ini (kg)_ → `Observation.valueQuantity.value` (64, tanpa BQ) |
| 6 | 72–96 | Observation | 39156-5 | Body mass index (BMI) [Ratio] | _IMT_ → `Observation.valueQuantity.value` (75, tanpa BQ)<br>_Interpretasi IMT_ → `Observation.interpretation.coding` (77, tanpa BQ) |
| 7 | 97–116 | Observation | 284473002 | Mid upper arm circumference | _Lingkar Lengan Atas (LiLA)_ → `Observation.valueQuantity.value` (101, tanpa BQ)<br>_Status Gizi_ → `Observation.interpretation.coding` (103, tanpa BQ) |
| 8 | 117–129 | Observation | 8480-6 | Systolic blood pressure | _Tekanan darah sistolik_ → `Observation.valueQuantity.value` (121, tanpa BQ) |
| 9 | 130–141 | Observation | 8462-4 | Diastolic blood pressure | _Tekanan darah diastolik_ → `Observation.valueQuantity.value` (134, tanpa BQ) |
| 10 | 142–153 | Observation | 1285244000 | Mean arterial pressure | _Mean Arterial Pressure (MAP)_ → `Observation.valueQuantity.value` (145, tanpa BQ) |
| 11 | 154–167 | Observation | 8310-5 | Body temperature | _Suhu_ → `Observation.valueQuantity.value` (157, tanpa BQ)<br>_Interpretasi Suhu_ → `Observation.interpretation.coding` (159, tanpa BQ) |
| 12 | 168–178 | Observation | 8867-4 | Heart Rate | _Nadi_ → `Observation.valueQuantity.value` (171, tanpa BQ) |
| 13 | 179–189 | Observation | 9279-1 | Respiratory rate | _Pernafasan_ → `Observation.valueQuantity.value` (182, tanpa BQ) |
| 14 | 191–201 | Observation | 93857-1 | Date and time of obstetric delivery | _Tanggal bersalin_ → `Observation.valueDateTime` (194, tanpa BQ) |
| 15 | 202–220 | Observation | 72150-6 | Delivery location | _Tempat bersalin_ → `Observation.valueCodeableConcept` (205, tanpa BQ) |
| 16 | 221–231 | Observation | 11977-6 | [#] Parity | _Anak ke berapa_ → `Observation.valueInteger` (224, tanpa BQ) |
| 17 | 232–244 | Observation | 57071-3 | Obstetric delivery method | _Cara Persalinan_ → `Observation.valueCodeableConcept.coding` (235, tanpa BQ) |
| 18 | 245–262 | Observation | 67775-7 | Level of responsiveness | _Tingkat Kesadaran_ → `Observation.status` (245, tanpa BQ) |
| 19 | 263–283 | Observation | 267038008 | Edema | _Pemeriksaan edema_ → `Observation.valueBoolean` (267, tanpa BQ) |
| 20 | 284–294 | Observation | 289530006 | Vaginal bleeding | _Perdarahan Pervaginam_ → `Observation.valueBoolean` (287, tanpa BQ) |
| 21 | 295–305 | Observation | 81661-1 | Blood Loss [Volume] Measured | _Jumlah Pendarahan_ → `Observation.valueQuantity.value` (298, tanpa BQ) |
| 22 | 306–317 | Observation | 112648003 | Massive hemorrhage | _Perdarahan Masif_ → `Observation.valueBoolean` (309, tanpa BQ) |
| 23 | 318–324 | Condition | 112648003 | Massive hemorrhage | – |
| 24 | 325–336 | Observation | 91175000 | Seizure | _Kejang_ → `Observation.valueBoolean` (328, tanpa BQ) |
| 25 | 337–343 | Condition | 91175000 | Seizure | _date_ → `Condition.recordedDate` (343, tanpa BQ) |
| 26 | 344–355 | Observation | 27942005 | Shock | _Syok_ → `Observation.valueBoolean` (347, tanpa BQ) |
| 27 | 356–362 | Condition | 27942005 | Shock | _date_ → `Condition.recordedDate` (362, tanpa BQ) |
| 28 | 363–377 | Observation | 11881-0 | Uterus Fundal height Tape measure | _Kondisi Payudara_ → `Observation.valueCodeableConcept.coding` (366, tanpa BQ) |
| 29 | 378–389 | Observation | 413711008 | Breastfeeding (infant) | _Menyusui_ → `Observation.valueBoolean` (381, tanpa BQ) |
| 30 | 390–408 | Condition | 58703003 | Postpartum depression | _Komplikasi masa nifas_ → `Condition.clinicalStatus.coding` (390, tanpa BQ)<br>_Komplikasi lainnya_ → `Condition.code.text` (404, tanpa BQ) |
| 31 | 409–421 | Observation | OC000017 | Produksi ASI | _Produksi ASI_ → `Observation.valueCodeableConcept.coding` (412, tanpa BQ) |
| 32 | 422–433 | Observation | 11881-0 | Uterus Fundal height Tape measure | _Tinggi Fundus Uteri (TFU)_ → `Observation.valueQuantity.value` (425, tanpa BQ) |
| 33 | 434–445 | Observation | 289700000 | Uterine contractions present | _Kontraksi Uteri_ → `Observation.valueBoolean` (437, tanpa BQ) |
| 34 | 446–457 | Observation | OC000025 | Tanda Infeksi Luka Jahitan Sectio Caesaria | _Tanda Infeksi Luka Jahitan Sectio Caesaria_ → `Observation.valueBoolean` (449, tanpa BQ) |
| 35 | 458–472 | Observation | 364297003 | Female perineum observable | _Kondisi Perineum_ → `Observation.valueCodeableConcept.coding` (461, tanpa BQ) |
| 36 | 473–484 | Observation | OC000020 | Tanda Infeksi Perineum | _Tanda Infeksi Perineum_ → `Observation.valueBoolean` (476, tanpa BQ) |
| 37 | 485–498 | Observation | 249214003 | Color of lochia | _Warna Lokhia_ → `Observation.valueCodeableConcept.coding` (488, tanpa BQ) |
| 38 | 499–510 | Observation | 249215002 | Odor of lochia | _Bau Lokhia_ → `Observation.valueBoolean` (502, tanpa BQ) |
| 39 | 511–525 | Observation | 252041008 | Micturition finding | _Buang Air Kecil_ → `Observation.valueCodeableConcept.coding` (514, tanpa BQ) |
| 40 | 526–537 | Observation | 300375001 | Able to defecate | _Buang Air Besar_ → `Observation.valueBoolean` (529, tanpa BQ) |
| 41 | 538–547 | Procedure | 767224000 | Administration of vitamin A | _Pemberian Vitamin A_ → `Procedure.category.coding` (538, tanpa BQ) |
| 42 | 548–557 | Procedure | SP000008 | Pemberian Tablet Tambah Darah | _Pemberian Tablet Tambah Darah_ → `Procedure.category.coding` (548, tanpa BQ) |
| 43 | 558–567 | Procedure | SP000370 | Multiple Micronutrient Supplement | _Pemberian MMS_ → `Procedure.category.coding` (558, tanpa BQ) |
| 44 | 568–586 | Observation | 8659-5 | Birth control method - Reported | _Mengikuti KB Pasca Persalinan_ → `Observation.valueCodeableConcept.coding` (571, tanpa BQ) |
| 45 | 587–597 | Procedure | 385892002 | Mental health screening | _Skrining Kesehatan Jiwa_ → `Procedure.category.coding` (587, tanpa BQ) |
| 46 | 598–609 | Observation | 1155968006 | Mood | _Mood_ → `Observation.valueCodeableConcept.coding` (601, tanpa BQ) |
| 47 | 610–624 | Condition | 160357008 | Family history: Hypertension | _Riwayat Penyakit Keluarga_ → `Condition.clinicalStatus.coding` (610, tanpa BQ) |
| 48 | 626–631 | Procedure | 54070000 | Postpartum education | _Apakah dilakukan edukasi dan konseling_ → `Procedure.category.coding` (626, tanpa BQ)<br>_Sebutkan topik konseling yang dilakukan_ → `Procedure.code.coding.code` (630, tanpa BQ) |
| 49 | 632–646 | Procedure | ED000008 | Edukasi Tanda Bahaya Kehamilan, Bersalin dan Nifas | _Jika dijawab lainnya tambahkan mapping berikut_ → `Procedure.code.text` (639, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 35 |
| Condition | 6 |
| Procedure | 6 |
| EpisodeOfCare | 1 |
| Encounter | 1 |
| **Total** | **49** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 8 | EpisodeOfCare | `EpisodeOfCare.type.coding` | PNC | Postnatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 2 | 31 | Condition | `Condition.code.coding` | Z39.2 | Routine postpartum follow-up | http://hl7.org/fhir/sid/icd-10 |
| 3 | 49 | Observation | `Observation.code.coding` | 8302-2 | Body height | http://loinc.org |
| 4 | 50 | Observation | `Observation.code.coding` | ANC.B8.DE1 | Height | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 5 | 62 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 6 | 63 | Observation | `Observation.code.coding` | ANC.B8.DE3 | Current weight | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 7 | 74 | Observation | `Observation.code.coding` | 39156-5 | Body mass index (BMI) [Ratio] | http://loinc.org |
| 8 | 77 | Observation | `Observation.interpretation.coding` | 717933005 | Severe thinness in adulthood | http://snomed.info/sct |
| 9 | 79 | Observation | `Observation.interpretation.coding` | 248342006 | Underweight | http://snomed.info/sct |
| 10 | 82 | Observation | `Observation.interpretation.coding` | 43664005 | Normal weight | http://snomed.info/sct |
| 11 | 85 | Observation | `Observation.interpretation.coding` | 238131007 | Overweight | http://snomed.info/sct |
| 12 | 88 | Observation | `Observation.interpretation.coding` | 414915002 | Obese | http://snomed.info/sct |
| 13 | 99 | Observation | `Observation.code.coding` | 284473002 | Mid upper arm circumference | http://snomed.info/sct |
| 14 | 100 | Observation | `Observation.code.coding` | ANC.SS.DE3 | Lingkar Lengan Atas (LILA) | http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes |
| 15 | 103 | Observation | `Observation.interpretation.coding` | OI000018 | Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 16 | 105 | Observation | `Observation.interpretation.coding` | OI000035 | Risiko Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 17 | 108 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 18 | 119 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 19 | 120 | Observation | `Observation.code.coding` | ANC.B8.DE17 | Systolic blood pressure | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 20 | 132 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://loinc.org |
| 21 | 133 | Observation | `Observation.code.coding` | ANC.B8.DE19 | Diastolic blood pressure | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 22 | 144 | Observation | `Observation.code.coding` | 1285244000 | Mean arterial pressure | http://snomed.info/sct |
| 23 | 156 | Observation | `Observation.code.coding` | 8310-5 | Body temperature | http://loinc.org |
| 24 | 159 | Observation | `Observation.interpretation.coding` | 386689009 | Hypothermia | http://snomed.info/sct |
| 25 | 160 | Observation | `Observation.interpretation.coding` | 87273009 | Temperature norma | http://snomed.info/sct |
| 26 | 161 | Observation | `Observation.interpretation.coding` | 1197782006 | Hyperthermia | http://snomed.info/sct |
| 27 | 170 | Observation | `Observation.code.coding` | 8867-4 | Heart Rate | http://loinc.org |
| 28 | 181 | Observation | `Observation.code.coding` | 9279-1 | Respiratory rate | http://loinc.org |
| 29 | 193 | Observation | `Observation.code.coding` | 93857-1 | Date and time of obstetric delivery | http://loinc.org |
| 30 | 204 | Observation | `Observation.code.coding` | 72150-6 | Delivery location | http://loinc.org |
| 31 | 205 | Observation | `Observation.valueCodeableConcept` | 264362003 | Home | http://snomed.info/sct |
| 32 | 206 | Observation | `Observation.valueCodeableConcept` | OT000001 | Polindes | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 33 | 207 | Observation | `Observation.valueCodeableConcept` | OT000002 | Pustu | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 34 | 208 | Observation | `Observation.valueCodeableConcept` | 102 | Puskesmas | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 35 | 209 | Observation | `Observation.valueCodeableConcept` | 103 | Klinik | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 36 | 210 | Observation | `Observation.valueCodeableConcept` | OT000008 | Rumah Bersalin | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 37 | 211 | Observation | `Observation.valueCodeableConcept` | 104 | Rumah Sakit | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 38 | 212 | Observation | `Observation.valueCodeableConcept` | 82242000 | Children’s hospital | http://snomed.info/sct |
| 39 | 213 | Observation | `Observation.valueCodeableConcept` | OT000004 | Bidan Praktek Mandiri | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 40 | 223 | Observation | `Observation.code.coding` | 11977-6 | [#] Parity | http://loinc.org |
| 41 | 234 | Observation | `Observation.code.coding` | 57071-3 | Obstetric delivery method | http://loinc.org |
| 42 | 235 | Observation | `Observation.valueCodeableConcept.coding` | 48782003 | Delivery normal | http://snomed.info/sct |
| 43 | 236 | Observation | `Observation.valueCodeableConcept.coding` | 200144004 | Deliveries by cesarean | http://snomed.info/sct |
| 44 | 237 | Observation | `Observation.valueCodeableConcept.coding` | 200130005 | Forceps delivery - delivered | http://snomed.info/sct |
| 45 | 238 | Observation | `Observation.valueCodeableConcept.coding` | 200138003 | Vacuum extractor delivery - delivered | http://snomed.info/sct |
| 46 | 247 | Observation | `Observation.code.coding` | 67775-7 | Level of responsiveness | http://loinc.org |
| 47 | 248 | Observation | `Observation.valueCodeableConcept[i].coding` | 248234008 | Mentally alert | http://snomed.info/sct |
| 48 | 249 | Observation | `Observation.valueCodeableConcept[i].coding` | LA9340-6 | Alert | http://loinc.org |
| 49 | 250 | Observation | `Observation.valueCodeableConcept[i].coding` | 20602000 | Apathy | http://snomed.info/sct |
| 50 | 251 | Observation | `Observation.valueCodeableConcept[i].coding` | 2776000 | Delirium | http://snomed.info/sct |
| 51 | 252 | Observation | `Observation.valueCodeableConcept[i].coding` | 271782001 | Somnolence | http://snomed.info/sct |
| 52 | 253 | Observation | `Observation.valueCodeableConcept[i].coding` | LA25163-9 | Stuporous | http://loinc.org |
| 53 | 254 | Observation | `Observation.valueCodeableConcept[i].coding` | 274659008 | Semicoma | http://snomed.info/sct |
| 54 | 255 | Observation | `Observation.valueCodeableConcept[i].coding` | 371632003 | Coma | http://snomed.info/sct |
| 55 | 256 | Observation | `Observation.valueCodeableConcept[i].coding` | LA9343-0 | Unresponsive | http://loinc.org |
| 56 | 265 | Observation | `Observation.code.coding` | 267038008 | Edema | http://snomed.info/sct |
| 57 | 266 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 58 | 268 | Observation | `Observation.component.code.coding` | 445088006 | Edema of face | http://snomed.info/sct |
| 59 | 271 | Observation | `Observation.component.code.coding` | 2564009 | Edema of hand | http://snomed.info/sct |
| 60 | 274 | Observation | `Observation.component.code.coding` | 102576009 | Edema of foot | http://snomed.info/sct |
| 61 | 286 | Observation | `Observation.code.coding` | 289530006 | Vaginal bleeding | http://snomed.info/sct |
| 62 | 297 | Observation | `Observation.code.coding` | 81661-1 | Blood Loss [Volume] Measured | http://loinc.org |
| 63 | 308 | Observation | `Observation.code.coding` | 112648003 | Massive hemorrhage | http://snomed.info/sct |
| 64 | 320 | Condition | `Condition.code.coding` | 112648003 | Massive hemorrhage | http://snomed.info/sct |
| 65 | 327 | Observation | `Observation.code.coding` | 91175000 | Seizure | http://snomed.info/sct |
| 66 | 339 | Condition | `Condition.code.coding` | 91175000 | Seizure | http://snomed.info/sct |
| 67 | 346 | Observation | `Observation.code.coding` | 27942005 | Shock | http://snomed.info/sct |
| 68 | 358 | Condition | `Condition.code.coding` | 27942005 | Shock | http://snomed.info/sct |
| 69 | 365 | Observation | `Observation.code.coding` | 11881-0 | Uterus Fundal height Tape measure | http://loinc.org |
| 70 | 366 | Observation | `Observation.valueCodeableConcept.coding` | 300885006 | Swelling of breast | http://snomed.info/sct |
| 71 | 367 | Observation | `Observation.valueCodeableConcept.coding` | 290070001 | Red breast | http://snomed.info/sct |
| 72 | 368 | Observation | `Observation.valueCodeableConcept.coding` | 54302000 | Discharge from nipple | http://snomed.info/sct |
| 73 | 369 | Observation | `Observation.valueCodeableConcept.coding` | 53430007 | Pain of breast | http://snomed.info/sct |
| 74 | 370 | Observation | `Observation.valueCodeableConcept.coding` | 290084006 | Breast normal | http://snomed.info/sct |
| 75 | 380 | Observation | `Observation.code.coding` | 413711008 | Breastfeeding (infant) | http://snomed.info/sct |
| 76 | 392 | Condition | `Condition.code.coding` | 58703003 | Postpartum depression | http://snomed.info/sct |
| 77 | 393 | Condition | `Condition.code.coding` | 47821001 | Postpartum hemorrhage | http://snomed.info/sct |
| 78 | 394 | Condition | `Condition.code.coding` | 198188007 | Chronic uterine inflammatory disease | http://snomed.info/sct |
| 79 | 395 | Condition | `Condition.code.coding` | 111367007 | Pelvic abscess | http://snomed.info/sct |
| 80 | 396 | Condition | `Condition.code.coding` | 211063003 | Infected abrasion of perineum | http://snomed.info/sct |
| 81 | 397 | Condition | `Condition.code.coding` | 76902006 | Tetanus | http://snomed.info/sct |
| 82 | 398 | Condition | `Condition.code.coding` | 266579006 | Inflammatory disorder of breast | http://snomed.info/sct |
| 83 | 399 | Condition | `Condition.code.coding` | 49746001 | Engorgement of breasts | http://snomed.info/sct |
| 84 | 400 | Condition | `Condition.code.coding` | 82231009 | Inversion of nipple | http://snomed.info/sct |
| 85 | 401 | Condition | `Condition.code.coding` | 40521000119100 | Postpartum pregnancy-induced hypertension | http://snomed.info/sct |
| 86 | 402 | Condition | `Condition.code.coding` | 91302008 | Sepsis | http://snomed.info/sct |
| 87 | 403 | Condition | `Condition.code.coding` | O90.8 | Other complications of the puerperium, not elsewhere classified | http://hl7.org/fhir/sid/icd-10 |
| 88 | 411 | Observation | `Observation.code.coding` | OC000017 | Produksi ASI | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 89 | 412 | Observation | `Observation.valueCodeableConcept.coding` | OV000016 | Produksi ASI ada | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 90 | 413 | Observation | `Observation.valueCodeableConcept.coding` | OV000017 | Produksi ASI ada tapi sedikit | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 91 | 414 | Observation | `Observation.valueCodeableConcept.coding` | OV000018 | Produksi ASI tidak ada | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 92 | 424 | Observation | `Observation.code.coding` | 11881-0 | Uterus Fundal height Tape measure | http://loinc.org |
| 93 | 436 | Observation | `Observation.code.coding` | 289700000 | Uterine contractions present | http://snomed.info/sct |
| 94 | 448 | Observation | `Observation.code.coding` | OC000025 | Tanda Infeksi Luka Jahitan Sectio Caesaria | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 95 | 460 | Observation | `Observation.code.coding` | 364297003 | Female perineum observable | http://snomed.info/sct |
| 96 | 461 | Observation | `Observation.valueCodeableConcept.coding` | 57759005 | First degree perineal laceration | http://snomed.info/sct |
| 97 | 462 | Observation | `Observation.valueCodeableConcept.coding` | 6234006 | Second degree perineal laceration | http://snomed.info/sct |
| 98 | 463 | Observation | `Observation.valueCodeableConcept.coding` | 10217006 | Third degree perineal laceration | http://snomed.info/sct |
| 99 | 464 | Observation | `Observation.valueCodeableConcept.coding` | 399031001 | Fourth degree perineal laceration | http://snomed.info/sct |
| 100 | 465 | Observation | `Observation.valueCodeableConcept.coding` | 289854007 | Perineum intact | http://snomed.info/sct |
| 101 | 475 | Observation | `Observation.code.coding` | OC000020 | Tanda Infeksi Perineum | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 102 | 487 | Observation | `Observation.code.coding` | 249214003 | Color of lochia | http://snomed.info/sct |
| 103 | 488 | Observation | `Observation.valueCodeableConcept.coding` | 278072004 | Lochia rubra | http://snomed.info/sct |
| 104 | 489 | Observation | `Observation.valueCodeableConcept.coding` | 113291006 | Lochia sanguinolenta | http://snomed.info/sct |
| 105 | 490 | Observation | `Observation.valueCodeableConcept.coding` | 449828001 | Lochia serosa | http://snomed.info/sct |
| 106 | 491 | Observation | `Observation.valueCodeableConcept.coding` | 449827006 | Lochia alba | http://snomed.info/sct |
| 107 | 501 | Observation | `Observation.code.coding` | 249215002 | Odor of lochia | http://snomed.info/sct |
| 108 | 513 | Observation | `Observation.code.coding` | 252041008 | Micturition finding | http://snomed.info/sct |
| 109 | 514 | Observation | `Observation.valueCodeableConcept.coding` | 49650001 | Dysuria | http://snomed.info/sct |
| 110 | 515 | Observation | `Observation.valueCodeableConcept.coding` | 249288007 | Incomplete emptying of urinary bladder | http://snomed.info/sct |
| 111 | 516 | Observation | `Observation.valueCodeableConcept.coding` | 162116003 | Increased frequency of urination | http://snomed.info/sct |
| 112 | 517 | Observation | `Observation.valueCodeableConcept.coding` | 42112009 | Enuresis | http://snomed.info/sct |
| 113 | 518 | Observation | `Observation.valueCodeableConcept.coding` | 102834005 | Normal micturition | http://snomed.info/sct |
| 114 | 528 | Observation | `Observation.code.coding` | 300375001 | Able to defecate | http://snomed.info/sct |
| 115 | 539 | Procedure | `Procedure.code.coding` | 767224000 | Administration of vitamin A | http://snomed.info/sct |
| 116 | 549 | Procedure | `Procedure.code.coding` | SP000008 | Pemberian Tablet Tambah Darah | http://terminology.kemkes.go.id/sp |
| 117 | 559 | Procedure | `Procedure.code.coding` | SP000370 | Multiple Micronutrient Supplement | http://terminology.kemkes.go.id/sp |
| 118 | 570 | Observation | `Observation.code.coding` | 8659-5 | Birth control method - Reported | http://loinc.org |
| 119 | 571 | Observation | `Observation.valueCodeableConcept.coding` | 237122005 | Lactational amenorrhea | http://snomed.info/sct |
| 120 | 572 | Observation | `Observation.valueCodeableConcept.coding` | LA6523-0 | Condom | http://loinc.org |
| 121 | 573 | Observation | `Observation.valueCodeableConcept.coding` | LA6524-8 | Oral contraceptive pill | http://loinc.org |
| 122 | 574 | Observation | `Observation.valueCodeableConcept.coding` | LA6525-5 | Injectable/implantable hormone | http://loinc.org |
| 123 | 575 | Observation | `Observation.valueCodeableConcept.coding` | LA6527-1 | Intrauterine device | http://loinc.org |
| 124 | 576 | Observation | `Observation.valueCodeableConcept.coding` | 40388003 | Implant, device | http://snomed.info/sct |
| 125 | 577 | Observation | `Observation.valueCodeableConcept.coding` | 77543007 | Ligation of fallopian tube | http://snomed.info/sct |
| 126 | 578 | Observation | `Observation.valueCodeableConcept.coding` | 22523008 | Vasectomy | http://snomed.info/sct |
| 127 | 579 | Observation | `Observation.dataAbsentReason.coding` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 128 | 588 | Procedure | `Procedure.code.coding` | 385892002 | Mental health screening | http://snomed.info/sct |
| 129 | 600 | Observation | `Observation.code.coding` | 1155968006 | Mood | http://snomed.info/sct |
| 130 | 601 | Observation | `Observation.valueCodeableConcept.coding` | 704678007 | Depressed mood with postpartum onset | http://snomed.info/sct |
| 131 | 602 | Observation | `Observation.valueCodeableConcept.coding` | 225658008 | Mood stable | http://snomed.info/sct |
| 132 | 612 | Condition | `Condition.code.coding` | 160357008 | Family history: Hypertension | http://snomed.info/sct |
| 133 | 613 | Condition | `Condition.code.coding` | 160303001 | Family history of diabetes mellitus | http://snomed.info/sct |
| 134 | 614 | Condition | `Condition.code.coding` | 275104002 | Family history of stroke | http://snomed.info/sct |
| 135 | 615 | Condition | `Condition.code.coding` | 429959009 | Family history of heart failure | http://snomed.info/sct |
| 136 | 616 | Condition | `Condition.code.coding` | 160377001 | Family history: Asthma | http://snomed.info/sct |
| 137 | 617 | Condition | `Condition.code.coding` | 275937001 | Family history of malignant neoplasm (situation) | http://snomed.info/sct |
| 138 | 618 | Condition | `Condition.code.coding` | 160314003 | Family history: Hypercholesterolemia | http://snomed.info/sct |
| 139 | 619 | Condition | `Condition.code.coding` | 160324006 | Family history of mental disorder | http://snomed.info/sct |
| 140 | 620 | Condition | `Condition.code.coding` | 160266009 | No family history of clinical finding | http://snomed.info/sct |
| 141 | 627 | Procedure | `Procedure.code.coding` | 54070000 | Postpartum education | http://snomed.info/sct |
| 142 | 632 | Procedure | `Procedure.code.coding` | ED000008 | Edukasi Tanda Bahaya Kehamilan, Bersalin dan Nifas | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 143 | 633 | Procedure | `Procedure.code.coding` | ED000010 | Edukasi PHBS | http://terminology.kemkes.go.id/CodeSystem/clinical-term |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 89 |
| http://loinc.org | 24 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 10 |
| http://terminology.kemkes.go.id/CodeSystem/organization-type | 7 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 4 |
| http://hl7.org/fhir/sid/icd-10 | 2 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 2 |
| http://terminology.kemkes.go.id/sp | 2 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 1 |
| http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes | 1 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 1 |
| **Total** | **143** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 46 | – | Tanggal kunjungan | – | `` |
| 625 | – | Tanggal kunjungan | – | `` |
