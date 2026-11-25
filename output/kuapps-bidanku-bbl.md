# Output Form: KuApps BidanKu - BBL

Sumber: `mapping/phdt-data-dictionary-kuapps-bidanku-bbl.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-kuapps-bidanku-bbl.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 48 |
| Code (`jumlah code` = 1) | 103 |
| Code unik (code + CodeSystem) | 88 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 4 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 3–11 | EpisodeOfCare | Neonate | Neonate | – |
| 2 | 12–27 | Encounter | – | – | _Kunjungan Neonatus (KN)_ → `Encounter.identifier` (12, tanpa BQ)<br>_Tanggal Posyandu_ → `Encounter.period.start` (15, tanpa BQ) |
| 3 | 28–35 | Condition | Z00.1 | Routine child health examination | – |
| 4 | 45–55 | Observation | SP000699 | Kelompok Dasawisma | _Dasawisma group_ → `Observation.valueString` (48, tanpa BQ) |
| 5 | 56–67 | Observation | SP000132 | Memiliki Buku KIA | _Apakah pasien memiliki buku KIA?_ → `Observation.valueBoolean` (59, tanpa BQ) |
| 6 | 68–79 | Observation | 89269-5 | Body height Measured --at birth | _Panjang Badan Bayi Saat Lahir (cm)_ → `Observation.valueQuantity.value` (71, tanpa BQ) |
| 7 | 80–96 | Observation | 8339-4 | Birth weight Measured | _Berat Badan Bayi Saat Lahir (gram)_ → `Observation.valueQuantity.value` (83, tanpa BQ)<br>_Interpretasi_ → `Observation.interpretation.coding` (85, tanpa BQ) |
| 8 | 97–108 | Observation | 8290-9 | Head Occipital-frontal circumference --at birth- by Tape measure | _Lingkar Kepala Saat Lahir (cm)_ → `Observation.valueQuantity.value` (100, tanpa BQ) |
| 9 | 109–120 | Observation | 8306-3 | Body height --lying | _Panjang Badan (cm)_ → `Observation.valueQuantity.value` (112, tanpa BQ) |
| 10 | 121–132 | Observation | 29463-7 | Body weight | _Berat Badan (gram)_ → `Observation.valueQuantity.value` (124, tanpa BQ) |
| 11 | 133–144 | Observation | 816159004 | Measured weight gain | _Penimbangan BB bayi dibandingkan pengukuran sebelumnya_ → `Observation.valueCodeableConcept.coding` (136, tanpa BQ) |
| 12 | 145–172 | Observation | 1153598007 | Weight for length z score | _BB/PB_ → `Observation.valueQuantity.value` (148, tanpa BQ) |
| 13 | 173–194 | Observation | 1153593003 | Weight for age z-score | _BB/U_ → `Observation.valueQuantity.value` (176, tanpa BQ) |
| 14 | 195–221 | Observation | 1153590000 | Length for age z-score | _PB/U_ → `Observation.valueQuantity.value` (198, tanpa BQ) |
| 15 | 222–233 | Observation | 8287-5 | Head Occipital-frontal circumference by Tape measure | _Lingkar kepala (cm)_ → `Observation.valueQuantity.value` (225, tanpa BQ) |
| 16 | 234–256 | Observation | 1153594009 | Head circumference for age z-score | _LK/U_ → `Observation.valueQuantity.value` (237, tanpa BQ) |
| 17 | 257–268 | Observation | 8867-4 | Heart rate | _Frekuensi Denyut Jantung (/menit)_ → `Observation.valueQuantity.value` (260, tanpa BQ) |
| 18 | 269–280 | Observation | 8310-5 | Body temperature | _Suhu (Cel)_ → `Observation.valueQuantity.value` (272, tanpa BQ) |
| 19 | 281–292 | Observation | 9279-1 | Respiratory rate | _Pernapasan_ → `Observation.valueQuantity.value` (284, tanpa BQ) |
| 20 | 293–304 | Observation | 76516-4 | Gestational age—​at birth | _Usia Gestasi (minggu)_ → `Observation.valueQuantity.value` (296, tanpa BQ) |
| 21 | 305–316 | Observation | 10206-1 | Physical findings of Skin Narrative | _Kulit_ → `Observation.valueCodeableConcept.coding` (308, tanpa BQ) |
| 22 | 317–328 | Observation | 10199-8 | Physical findings of Head Narrative | _Kepala_ → `Observation.valueCodeableConcept.coding` (320, tanpa BQ) |
| 23 | 329–340 | Observation | 10197-2 | Physical findings of Eye Narrative | _Mata_ → `Observation.valueCodeableConcept.coding` (332, tanpa BQ) |
| 24 | 341–352 | Observation | 32453-3 | Physical findings of Mouth | _Mulut_ → `Observation.valueCodeableConcept.coding` (344, tanpa BQ) |
| 25 | 353–364 | Observation | 32453-3 | Physical findings of Abdomen Narrative | _Perut_ → `Observation.valueCodeableConcept.coding` (356, tanpa BQ) |
| 26 | 365–376 | Observation | 10192-3 | Physical findings of Back Narrative | _Punggung_ → `Observation.valueCodeableConcept.coding` (368, tanpa BQ) |
| 27 | 377–389 | Observation | 11388-6 | Physical findings of Buttocks Narrative | _Lubang Anus_ → `Observation.valueCodeableConcept.coding` (381, tanpa BQ) |
| 28 | 390–401 | Observation | 11400-9 | Physical findings of Genitalia Narrative | _Alat kelamin_ → `Observation.valueCodeableConcept.coding` (393, tanpa BQ) |
| 29 | 402–411 | Procedure | PC000002 | Pemberian Salep Antibiotik Mata | _Salep Antibiotik Mata_ → `Procedure.category.coding` (402, tanpa BQ) |
| 30 | 412–421 | Procedure | 448883004 | Injection of vitamin K1 | _Apakah diberikan vitamin K_ → `Procedure.category.coding` (412, tanpa BQ) |
| 31 | 422–431 | Procedure | PC000001 | Perawatan Tali Pusat | _Perawatan Tali Pusat_ → `Procedure.category.coding` (422, tanpa BQ) |
| 32 | 432–441 | Procedure | 431868002 | Initiation of breastfeeding | _Inisiasi Menyusui Dini_ → `Procedure.category.coding` (432, tanpa BQ) |
| 33 | 442–453 | Observation | OC000016 | Waktu Inisiasi Menyusui Dini | _Jika Ya, Waktu Inisiasi Menyusui Dini_ → `Observation.valueCodeableConcept.coding` (445, tanpa BQ) |
| 34 | 454–465 | Observation | 1145307003 | Exclusively breastfed | _Pemberian ASI Eksklusif_ → `Observation.valueBoolean` (457, tanpa BQ) |
| 35 | 466–477 | Observation | SP000889 | Frekuensi Menyusui | _Frekuensi menyusui (kali/hari)_ → `Observation.valueQuantity.value` (469, tanpa BQ) |
| 36 | 478–508 | Observation | 249222005 | Neonatal condition | _Kondisi bayi_ → `Observation.valueCodeableConcept.coding` (481, tanpa BQ)<br>_Pilih Penyakit_ → `Observation.component.code.coding` (484, tanpa BQ) |
| 37 | 509–523 | Condition | 160357008 | Family history: Hypertension | _Riwayat Penyakit Keluarga_ → `Condition.clinicalStatus.coding` (509, tanpa BQ) |
| 38 | 524–539 | AllergyIntolerance | – | – | _Apakah ada alergi obat saat ini?_ → `AllergyIntolerance.clinicalStatus.coding` (524, tanpa BQ)<br>_Jika Ya, jenis obat?_ → `AllergyIntolerance.code.coding` (526, tanpa BQ) |
| 39 | 540–551 | Observation | 300471006 | Finding of frequency of urination | _Frekuensi BAK (kali/hari)_ → `Observation.valueQuantity.value` (543, tanpa BQ) |
| 40 | 552–563 | Observation | 300380005 | Finding of frequency of defecation | _Frekuensi BAB (kali/hari)_ → `Observation.valueQuantity.value` (555, tanpa BQ) |
| 41 | 564–575 | Observation | 1144561006 | Adequate sanitation | _Apakah memiliki jamban di rumah?_ → `Observation.valueBoolean` (567, tanpa BQ) |
| 42 | 576–587 | Observation | 1162942008 | Access to potable water | _Apakah memiliki akses untuk air bersih_ → `Observation.valueBoolean` (579, tanpa BQ) |
| 43 | 588–597 | Procedure | 400984005 | Congenital hypothyroidism screening test | _Apakah dilakukan SHK_ → `Procedure.category.coding` (588, tanpa BQ) |
| 44 | 598–611 | Observation | 29575-8 | Thyrotropin [Units/volume] in DBS | _Jika Ya, Berapa hasil pemeriksaan terakhir dari laboratorium_ → `Observation.valueQuantity.value` (598, tanpa BQ)<br>_Jika Ya, Interpretasi hasil SHK_ → `Observation.interpretation.coding` (600, tanpa BQ) |
| 45 | 612–637 | QuestionnaireResponse | – | – | _Batuk terus menerus_ → `QuestionnaireResponse.item.linkId` (622, tanpa BQ)<br>_Demam lebih dari ≥ 2 minggu_ → `QuestionnaireResponse.item.linkId` (626, tanpa BQ)<br>_BB tidak naik atau turun dalam 2 bulan berturut-turut_ → `QuestionnaireResponse.item.linkId` (630, tanpa BQ)<br>_Kontak erat dengan Pasien TBC_ → `QuestionnaireResponse.item.linkId` (634, tanpa BQ) |
| 46 | 638–650 | Observation | 171126009 | Tuberculosis screening | _Interpretasi hasil skrining TBC_ → `Observation.valueQuantity.value` (638, tanpa BQ) |
| 47 | 651–667 | Procedure | 54070000 | Postpartum education | _Apakah dilakukan konseling_ → `Procedure.category.coding` (651, tanpa BQ)<br>_Sebutkan topik konseling yang dilakukan_ → `Procedure.code.coding.code` (655, tanpa BQ)<br>_Jika lainnya, Sebutkan konseling lainnya_ → `Procedure.code.text` (660, tanpa BQ) |
| 48 | 670–705 | QuestionnaireResponse | – | – | _Apakah bayi dapat mengatakan Aaaa atau Oooo_ → `QuestionnaireResponse.item.linkId` (678, tanpa BQ)<br>_Apakah bayi menatap wajah dan tampak mendengerkan Anda, lalu berbicara saat Anda diam?_ → `QuestionnaireResponse.item.linkId` (682, tanpa BQ)<br>_Apakah Anda dapat seolah-olah berbicara dengan bayi Anda?_ → `QuestionnaireResponse.item.linkId` (686, tanpa BQ)<br>_Apakah bayi kaget bila mendengar suara (mengejapkan mata, napas lebih cepat)?_ → `QuestionnaireResponse.item.linkId` (690, tanpa BQ)<br>_Apakah bayi kelihatan menoleh bila Anda berbicara di sebelahnya?_ → `QuestionnaireResponse.item.linkId` (694, tanpa BQ)<br>_Apakah bayi Anda dapat tersenyum?_ → `QuestionnaireResponse.item.linkId` (698, tanpa BQ)<br>_Apakah bayi Anda kendal dengan Anda, seperti tersenyum lebih cepat pada Anda dibandingkan orang lain?_ → `QuestionnaireResponse.item.linkId` (702, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 35 |
| Procedure | 6 |
| Condition | 2 |
| QuestionnaireResponse | 2 |
| EpisodeOfCare | 1 |
| Encounter | 1 |
| AllergyIntolerance | 1 |
| **Total** | **48** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 8 | EpisodeOfCare | `EpisodeOfCare.type.coding` | Neonate | Neonate | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 2 | 30 | Condition | `Condition.code.coding` | Z00.1 | Routine child health examination | http://hl7.org/fhir/sid/icd-10 |
| 3 | 47 | Observation | `Observation.code.coding` | SP000699 | Kelompok Dasawisma | http://terminology.kemkes.go.id/sp |
| 4 | 58 | Observation | `Observation.code.coding` | SP000132 | Memiliki Buku KIA | http://terminology.kemkes.go.id/sp |
| 5 | 70 | Observation | `Observation.code.coding` | 89269-5 | Body height Measured --at birth | http://loinc.org |
| 6 | 82 | Observation | `Observation.code.coding` | 8339-4 | Birth weight Measured | http://loinc.org |
| 7 | 85 | Observation | `Observation.interpretation.coding` | 276613009 | High birth weight | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 8 | 86 | Observation | `Observation.interpretation.coding` | 276712009 | Normal birth weight | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 9 | 87 | Observation | `Observation.interpretation.coding` | 276610007 | Low birth weight infant | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 10 | 88 | Observation | `Observation.interpretation.coding` | 276611006 | Very low birth weight infant | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 11 | 89 | Observation | `Observation.interpretation.coding` | 276612004 | Extremely low birth weight | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 12 | 99 | Observation | `Observation.code.coding` | 8290-9 | Head Occipital-frontal circumference --at birth- by Tape measure | http://loinc.org |
| 13 | 111 | Observation | `Observation.code.coding` | 8306-3 | Body height --lying | http://loinc.org |
| 14 | 123 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 15 | 135 | Observation | `Observation.code.coding` | 816159004 | Measured weight gain | http://snomed.info/sct |
| 16 | 136 | Observation | `Observation.valueCodeableConcept.coding` | 262286000 | Weight increased | http://snomed.info/sct |
| 17 | 137 | Observation | `Observation.valueCodeableConcept.coding` | 36440009 | Failure to gain weight | http://snomed.info/sct |
| 18 | 147 | Observation | `Observation.code.coding` | 1153598007 | Weight for length z score | http://snomed.info/sct |
| 19 | 150 | Observation | `Observation.interpretation.coding` | OI000011 | Gizi Buruk | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 20 | 152 | Observation | `Observation.interpretation.coding` | 248325000 | Undernourished | http://snomed.info/sct |
| 21 | 155 | Observation | `Observation.interpretation.coding` | 248324001 | Well nourished | http://snomed.info/sct |
| 22 | 158 | Observation | `Observation.interpretation.coding` | OI000004 | Risiko Gizi Lebih | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 23 | 161 | Observation | `Observation.interpretation.coding` | 238131007 | Overweight | http://snomed.info/sct |
| 24 | 164 | Observation | `Observation.interpretation.coding` | 414915002 | Obese | http://snomed.info/sct |
| 25 | 175 | Observation | `Observation.code.coding` | 1153593003 | Weight for age z-score | http://snomed.info/sct |
| 26 | 197 | Observation | `Observation.code.coding` | 1153590000 | Length for age z-score | http://snomed.info/sct |
| 27 | 224 | Observation | `Observation.code.coding` | 8287-5 | Head Occipital-frontal circumference by Tape measure | http://loinc.org |
| 28 | 236 | Observation | `Observation.code.coding` | 1153594009 | Head circumference for age z-score | http://loinc.org |
| 29 | 239 | Observation | `Observation.interpretation.coding` | 840673007 | Normal head | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 30 | 244 | Observation | `Observation.interpretation.coding` | 1148757008 | Microcephaly | http://snomed.info/sct |
| 31 | 247 | Observation | `Observation.interpretation.coding` | 1145403003 | Macrocephaly | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 32 | 259 | Observation | `Observation.code.coding` | 8867-4 | Heart rate | http://loinc.org |
| 33 | 271 | Observation | `Observation.code.coding` | 8310-5 | Body temperature | http://loinc.org |
| 34 | 283 | Observation | `Observation.code.coding` | 9279-1 | Respiratory rate | http://loinc.org |
| 35 | 295 | Observation | `Observation.code.coding` | 76516-4 | Gestational age—​at birth | http://loinc.org |
| 36 | 307 | Observation | `Observation.code.coding` | 10206-1 | Physical findings of Skin Narrative | http://loinc.org |
| 37 | 308 | Observation | `Observation.valueCodeableConcept.coding` | 17621005 | Normal | http://snomed.info/sct |
| 38 | 309 | Observation | `Observation.valueCodeableConcept.coding` | 263654008 | Abnormal | http://snomed.info/sct |
| 39 | 319 | Observation | `Observation.code.coding` | 10199-8 | Physical findings of Head Narrative | http://loinc.org |
| 40 | 320 | Observation | `Observation.valueCodeableConcept.coding` | 17621005 | Normal | http://snomed.info/sct |
| 41 | 321 | Observation | `Observation.valueCodeableConcept.coding` | 263654008 | Abnormal | http://snomed.info/sct |
| 42 | 331 | Observation | `Observation.code.coding` | 10197-2 | Physical findings of Eye Narrative | http://loinc.org |
| 43 | 332 | Observation | `Observation.valueCodeableConcept.coding` | 17621005 | Normal | http://snomed.info/sct |
| 44 | 333 | Observation | `Observation.valueCodeableConcept.coding` | 263654008 | Abnormal | http://snomed.info/sct |
| 45 | 343 | Observation | `Observation.code.coding` | 32453-3 | Physical findings of Mouth | http://loinc.org |
| 46 | 344 | Observation | `Observation.valueCodeableConcept.coding` | 17621005 | Normal | http://snomed.info/sct |
| 47 | 345 | Observation | `Observation.valueCodeableConcept.coding` | 263654008 | Abnormal | http://snomed.info/sct |
| 48 | 355 | Observation | `Observation.code.coding` | 32453-3 | Physical findings of Abdomen Narrative | http://loinc.org |
| 49 | 356 | Observation | `Observation.valueCodeableConcept.coding` | 17621005 | Normal | http://snomed.info/sct |
| 50 | 357 | Observation | `Observation.valueCodeableConcept.coding` | 263654008 | Abnormal | http://snomed.info/sct |
| 51 | 367 | Observation | `Observation.code.coding` | 10192-3 | Physical findings of Back Narrative | http://loinc.org |
| 52 | 368 | Observation | `Observation.valueCodeableConcept.coding` | 17621005 | Normal | http://snomed.info/sct |
| 53 | 369 | Observation | `Observation.valueCodeableConcept.coding` | 263654008 | Abnormal | http://snomed.info/sct |
| 54 | 379 | Observation | `Observation.code.coding` | 11388-6 | Physical findings of Buttocks Narrative | http://loinc.org |
| 55 | 380 | Observation | `Observation.code.coding` | 53505006 | Anal structure (body structure) | http://snomed.info/sct |
| 56 | 381 | Observation | `Observation.valueCodeableConcept.coding` | 17621005 | Normal | http://snomed.info/sct |
| 57 | 382 | Observation | `Observation.valueCodeableConcept.coding` | 263654008 | Abnormal | http://snomed.info/sct |
| 58 | 392 | Observation | `Observation.code.coding` | 11400-9 | Physical findings of Genitalia Narrative | http://loinc.org |
| 59 | 393 | Observation | `Observation.valueCodeableConcept.coding` | 17621005 | Normal | http://snomed.info/sct |
| 60 | 394 | Observation | `Observation.valueCodeableConcept.coding` | 263654008 | Abnormal | http://snomed.info/sct |
| 61 | 403 | Procedure | `Procedure.code.coding` | PC000002 | Pemberian Salep Antibiotik Mata | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 62 | 413 | Procedure | `Procedure.code.coding` | 448883004 | Injection of vitamin K1 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 63 | 423 | Procedure | `Procedure.code.coding` | PC000001 | Perawatan Tali Pusat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 64 | 433 | Procedure | `Procedure.code.coding` | 431868002 | Initiation of breastfeeding | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 65 | 444 | Observation | `Observation.code.coding` | OC000016 | Waktu Inisiasi Menyusui Dini | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 66 | 445 | Observation | `Observation.valueCodeableConcept.coding` | OV000014 | Kurang dari 1 jam | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 67 | 446 | Observation | `Observation.valueCodeableConcept.coding` | OV000015 | Lebih dari 1 jam | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 68 | 456 | Observation | `Observation.code.coding` | 1145307003 | Exclusively breastfed | http://snomed.info/sct |
| 69 | 468 | Observation | `Observation.code.coding` | SP000889 | Frekuensi Menyusui | http://terminology.kemkes.go.id/sp |
| 70 | 480 | Observation | `Observation.code.coding` | 249222005 | Neonatal condition | http://snomed.info/sct |
| 71 | 481 | Observation | `Observation.valueCodeableConcept.coding` | 102500002 | Good neonatal condition at birth | http://snomed.info/sct |
| 72 | 482 | Observation | `Observation.valueCodeableConcept.coding` | 276707008 | Infant in poor condition at birth | http://snomed.info/sct |
| 73 | 483 | Observation | `Observation.valueCodeableConcept.coding` | 419099009 | Dead | http://snomed.info/sct |
| 74 | 484 | Observation | `Observation.component.code.coding` | 413654009 | Birth asphyxia | http://snomed.info/sct |
| 75 | 486 | Observation | `Observation.component.code.coding` | 56110009 | Fetal birth trauma | http://snomed.info/sct |
| 76 | 488 | Observation | `Observation.component.code.coding` | 276659006 | Clinical infection of newborn | http://snomed.info/sct |
| 77 | 490 | Observation | `Observation.component.code.coding` | 66091009 | Congenital disease | http://snomed.info/sct |
| 78 | 492 | Observation | `Observation.component.code.coding` | 13629008 | Hypothermia of newborn | http://snomed.info/sct |
| 79 | 494 | Observation | `Observation.component.code.coding` | 43424001 | Tetanus neonatorum | http://snomed.info/sct |
| 80 | 496 | Observation | `Observation.component.code.coding` | 206376005 | Sepsis of the newborn | http://snomed.info/sct |
| 81 | 498 | Observation | `Observation.component.code.coding` | 387712008 | Neonatal jaundice | http://snomed.info/sct |
| 82 | 500 | Observation | `Observation.component.code.coding` | 22925008 | Neonatal disorde | http://snomed.info/sct |
| 83 | 511 | Condition | `Condition.code.coding` | 160357008 | Family history: Hypertension | http://snomed.info/sct |
| 84 | 512 | Condition | `Condition.code.coding` | 160303001 | Family history of diabetes mellitus | http://snomed.info/sct |
| 85 | 513 | Condition | `Condition.code.coding` | 275104002 | Family history of stroke | http://snomed.info/sct |
| 86 | 514 | Condition | `Condition.code.coding` | 429959009 | Family history of heart failure | http://snomed.info/sct |
| 87 | 515 | Condition | `Condition.code.coding` | 160377001 | Family history: Asthma | http://snomed.info/sct |
| 88 | 516 | Condition | `Condition.code.coding` | 275937001 | Family history of malignant neoplasm (situation) | http://snomed.info/sct |
| 89 | 517 | Condition | `Condition.code.coding` | 160314003 | Family history: Hypercholesterolemia | http://snomed.info/sct |
| 90 | 518 | Condition | `Condition.code.coding` | 160324006 | Family history of mental disorder | http://snomed.info/sct |
| 91 | 519 | Condition | `Condition.code.coding` | 160266009 | No family history of clinical finding | http://snomed.info/sct |
| 92 | 542 | Observation | `Observation.code.coding` | 300471006 | Finding of frequency of urination | http://snomed.info/sct |
| 93 | 554 | Observation | `Observation.code.coding` | 300380005 | Finding of frequency of defecation | http://snomed.info/sct |
| 94 | 566 | Observation | `Observation.code.coding` | 1144561006 | Adequate sanitation | http://snomed.info/sct |
| 95 | 578 | Observation | `Observation.code.coding` | 1162942008 | Access to potable water | http://snomed.info/sct |
| 96 | 589 | Procedure | `Procedure.code.coding` | 400984005 | Congenital hypothyroidism screening test | http://snomed.info/sct |
| 97 | 600 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 98 | 601 | Observation | `Observation.interpretation.coding` | H | High | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 99 | 604 | Observation | `Observation.code.coding` | 29575-8 | Thyrotropin [Units/volume] in DBS | http://loinc.org |
| 100 | 639 | Observation | `Observation.interpretation.coding` | 772170009 | Tuberculosis suspected | http://snomed.info/sct |
| 101 | 640 | Observation | `Observation.interpretation.coding` | SP000789 | Bukan terduga TBC | http://terminology.kemkes.go.id/sp |
| 102 | 643 | Observation | `Observation.code.coding` | 171126009 | Tuberculosis screening | http://snomed.info/sct |
| 103 | 652 | Procedure | `Procedure.code.coding` | 54070000 | Postpartum education | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 59 |
| http://loinc.org | 20 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 16 |
| http://terminology.kemkes.go.id/sp | 4 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 2 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 1 |
| http://hl7.org/fhir/sid/icd-10 | 1 |
| **Total** | **103** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
