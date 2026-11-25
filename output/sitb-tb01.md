# Output Form: SITB - TB 01 (Kartu Pengobatan Pasien)

Sumber: `mapping/phdt-data-dictionary-sitb-tb01.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-sitb-tb01.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 37 |
| Code (`jumlah code` = 1) | 101 |
| Code unik (code + CodeSystem) | 89 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 15 |
| Variabel BQ (unik) | 0 |
| Variabel raw (variabel dictionary; belum ada file mentah) | 82 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–12 | Patient | – | – | _Nama Pasien TBC_ → `Patient.name.text` (2, tanpa BQ)<br>_No. Telp/HP Pasien_ → `Patient.telecom` (3, tanpa BQ)<br>_Nomor Induk / NIK_ → `Patient.identifier.value` (8, tanpa BQ)<br>_Alamat Lengkap_ → `Patient.address.line` (9, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (10, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (12, tanpa BQ) |
| 2 | 13–36 | EpisodeOfCare | TB-SO | Tuberkulosis Sensitif Obat | – |
| 3 | 37–44 | EpisodeOfCare | TB-RO | Tuberkulosis Resisten Obat | – |
| 4 | 45–75 | Encounter | – | – | _Dirujuk oleh_ → `Encounter.hospitalization.admitSource.coding[0]` (68, tanpa BQ)<br>_Pindah pengobatan_ → `Encounter.hospitalization.dischargeDisposition.coding` (80, tanpa BQ)<br>_Nama Faskes Tujuan_ → `Encounter.hospitalization.destination.display` (82, tanpa BQ)<br>_Kab/Kota Tujuan_ → `Encounter.hospitalization.destination.display` (83, tanpa BQ)<br>_Provinsi Tujuan_ → `Encounter.hospitalization.destination.display` (84, tanpa BQ) |
| 5 | 85–93 | Condition | A16.2 | Tuberculosis of lung, without mention of bacteriological or histological confirmation | _Klasifikasi berdasarkan lokasi anatomi_ → `Condition.clinicalStatus.coding` (85, tanpa BQ)<br>_Lokasi (jika Ekstra Paru)_ → `Condition.note` (93, tanpa BQ) |
| 6 | 94–108 | Observation | 424144002 | Current chronological age | _Umur (tahun)_ → `Observation.valueQuantity.value` (97, tanpa BQ)<br>_Umur (bulan)_ → `Observation.component.code.coding` (99, tanpa BQ) |
| 7 | 109–120 | Observation | 82810-3 | Pregnancy status | _Status kehamilan_ → `Observation.valueCodeableConcept.coding` (112, tanpa BQ) |
| 8 | 121–133 | Observation | 29463-7 | Body weight | _Berat Badan_ → `Observation.valueQuantity.value` (124, tanpa BQ) |
| 9 | 134–146 | Observation | 8302-2 | Body height | _Tinggi Badan_ → `Observation.valueQuantity.value` (137, tanpa BQ) |
| 10 | 147–159 | Observation | 827034002 | Scar of skin following Bacillus Calmette-Guerin immunization | _Perut BCG_ → `Observation.valueCodeableConcept.coding` (150, tanpa BQ) |
| 11 | 160–171 | Observation | OC000191 | Jumlah Skoring TBC Anak | _Jumlah Skoring TBC Anak_ → `Observation.valueInteger` (163, tanpa BQ) |
| 12 | 172–179 | RelatedPerson | – | – | _Nama PMO_ → `RelatedPerson.name.text` (173, tanpa BQ)<br>_No. Telp/HP PMO_ → `RelatedPerson.telecom` (174, tanpa BQ)<br>_Alamat PMO_ → `RelatedPerson.address.line` (179, tanpa BQ) |
| 13 | 186–197 | Observation | 106229004 | Qualifier for type of diagnosis | _Tipe Diagnosis_ → `Observation.valueCodeableConcept.coding` (189, tanpa BQ) |
| 14 | 198–215 | QuestionnaireResponse | – | – | _Klasifikasi riwayat pengobatan_ → `QuestionnaireResponse.questionnaire` (198, tanpa BQ) |
| 15 | 216–228 | Observation | 365866002 | Finding of human immunodeficiency virus status | _Klasifikasi status HIV_ → `Observation.effectiveDateTime` (216, tanpa BQ) |
| 16 | 229–248 | Observation | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | _No. Reg Lab_ → `Observation.identifier` (229, tanpa BQ)<br>_Hasil BTA_ → `Observation.code.coding` (232, tanpa BQ)<br>_Hasil Biakan_ → `Observation.code.coding` (233, tanpa BQ)<br>_Hasil Tes Cepat_ → `Observation.valueCodeableConcept.coding` (235, tanpa BQ)<br>_Tanggal Pemeriksaan_ → `Observation.effectiveDateTime` (245, tanpa BQ) |
| 17 | 249–260 | Observation | 23539-0 | Tuberculosis reaction wheal [Diameter] --3 days post dose mammalian tuberculin intradermal | _Uji Tuberkulin_ → `Observation.valueQuantity` (252, tanpa BQ) |
| 18 | 261–272 | Observation | 24648-8 | XR Chest PA upright | _Foto Thorax No. Seri_ → `Observation.identifier` (261, tanpa BQ)<br>_Foto Toraks Kesan_ → `Observation.valueString` (265, tanpa BQ)<br>_Foto Toraks Tanggal_ → `Observation.effectiveDateTime` (269, tanpa BQ) |
| 19 | 273–283 | Observation | 48635004 | Fine needle biopsy | _Biopsi jarum halus (FNAB) Hasil_ → `Observation.valueString` (276, tanpa BQ)<br>_Biopsi Jarum Halus (FNAB) Tanggal_ → `Observation.effectiveDateTime` (280, tanpa BQ) |
| 20 | 284–294 | Observation | X099388 | Biakan TB | _Biakan hasil contoh uji selain dahak_ → `Observation.component.valueCodeableConcept.coding` (289, tanpa BQ)<br>_Sebutkan_ → `Observation.note` (294, tanpa BQ) |
| 21 | 295–306 | Observation | 33248-6 | Diabetes status | _Riwayat DM_ → `Observation.valueCodeableConcept.coding` (298, tanpa BQ) |
| 22 | 307–318 | Observation | SP000047 | Hasil Tes Diabetes Melitus | _Hasil Tes DM_ → `Observation.valueCodeableConcept.coding` (310, tanpa BQ) |
| 23 | 319–330 | Observation | 1284985006 | Diabetes mellitus management program | _Terapi DM_ → `Observation.valueCodeableConcept.coding` (322, tanpa BQ) |
| 24 | 332–341 | RelatedPerson | – | – | _Nama Kontak_ → `RelatedPerson.name.text` (333, tanpa BQ)<br>_Jenis Kelamin Kontak_ → `RelatedPerson.gender` (334, tanpa BQ) |
| 25 | 342–354 | Observation | 424144002 | Current chronological age | _Umur Kontak_ → `Observation.valueQuantity.value` (345, tanpa BQ) |
| 26 | 355–365 | Observation | SP000790 | Hasil Pemeriksaan Kontak TBC | _Hasil Pemeriksaan Kontak_ → `Observation.valueCodeableConcept.coding` (357, tanpa BQ)<br>_Tindak Lanjut_ → `Observation.note` (365, tanpa BQ) |
| 27 | 366–402 | CarePlan | – | – | _Bentuk OAT_ → `CarePlan.activity.detail.status` (376, tanpa BQ)<br>_Paduan OAT_ → `CarePlan.activity.detail.status` (381, tanpa BQ)<br>_Sumber Obat_ → `CarePlan.activity.detail.status` (386, tanpa BQ)<br>_Hasil Akhir Pengobatan_ → `CarePlan.activity.outcomeCodeableConcept.coding` (394, tanpa BQ)<br>_Tanggal Hasil Akhir_ → `CarePlan.period.end` (401, tanpa BQ)<br>_Catatan (baca petunjuk pengisian)_ → `CarePlan.note` (402, tanpa BQ) |
| 28 | 403–436 | MedicationStatement | – | – | _KDT_ → `MedicationStatement.contained[0]..amount.numerator.value` (408, tanpa BQ)<br>_No Batch (KDT)_ → `MedicationStatement.contained[0]..batch.lotNumber` (414, tanpa BQ)<br>_Streptomisin_ → `MedicationStatement.contained[1]..amount.numerator.value` (421, tanpa BQ)<br>_No Batch (Streptomisin)_ → `MedicationStatement.contained[1]..batch.lotNumber` (427, tanpa BQ)<br>_Tanggal konsumsi obat (tabel)_ → `MedicationStatement.effectiveDateTime` (433, tanpa BQ)<br>_Konsumsi Obat (tabel)_ → `MedicationStatement.informationSource.reference` (434, tanpa BQ) |
| 29 | 437–449 | Observation | SP000796 | Jumlah OAT | _Jumlah_ → `Observation.identifier` (437, tanpa BQ) |
| 30 | 450–463 | Observation | 29463-7 | Body weight | _BB (kg)_ → `Observation.identifier` (450, tanpa BQ) |
| 31 | 464–497 | MedicationStatement | – | – | _KDT_ → `MedicationStatement.contained[0]..amount.numerator.value` (469, tanpa BQ)<br>_No Batch (KDT)_ → `MedicationStatement.contained[0]..batch.lotNumber` (475, tanpa BQ)<br>_Etambutol_ → `MedicationStatement.contained[1]..amount.numerator.value` (482, tanpa BQ)<br>_No Batch (Etambutol)_ → `MedicationStatement.contained[1]..batch.lotNumber` (488, tanpa BQ)<br>_Tanggal konsumsi obat (tabel)_ → `MedicationStatement.effectiveDateTime` (494, tanpa BQ)<br>_Konsumsi Obat (tabel)_ → `MedicationStatement.informationSource.reference` (495, tanpa BQ) |
| 32 | 498–510 | Observation | SP000796 | Jumlah OAT | _Jumlah_ → `Observation.identifier` (498, tanpa BQ) |
| 33 | 511–524 | Observation | 29463-7 | Body weight | _BB (kg)_ → `Observation.identifier` (511, tanpa BQ) |
| 34 | 525–533 | Procedure | TK000016 | Edukasi Tes HIV | _Tanggal dianjurkan Tes_ → `Procedure.category.coding` (525, tanpa BQ) |
| 35 | 534–547 | Observation | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | _Tanggal Tes HIV_ → `Observation.effectiveDateTime` (534, tanpa BQ)<br>_Hasil Tes HIV_ → `Observation.valueCodeableConcept.coding` (539, tanpa BQ)<br>_No. Reg. Nasional_ → `Observation.identifier.value` (547, tanpa BQ) |
| 36 | 548–562 | Observation | SP000123 | Integrasi Program | _PPK (Perawatan, Dukungan, Pengobatan)_ → `Observation.component.valueBoolean` (551, tanpa BQ)<br>_ART_ → `Observation.component.valueBoolean` (554, tanpa BQ)<br>_Nama Faskes PDP_ → `Observation.performer[1].display` (561, tanpa BQ)<br>_Pindah Register Pasien TB RO_ → `Observation.status` (562, tanpa BQ) |
| 37 | 563–573 | Observation | SP000797 | Pindah Register Pasien TB RO | – |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 25 |
| EpisodeOfCare | 2 |
| RelatedPerson | 2 |
| MedicationStatement | 2 |
| Patient | 1 |
| Encounter | 1 |
| Condition | 1 |
| QuestionnaireResponse | 1 |
| CarePlan | 1 |
| Procedure | 1 |
| **Total** | **37** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 19 | EpisodeOfCare | `EpisodeOfCare.type.coding` | TB-SO | Tuberkulosis Sensitif Obat | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 2 | 37 | EpisodeOfCare | `EpisodeOfCare.type.coding` | TB-RO | Tuberkulosis Resisten Obat | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 3 | 68 | Encounter | `Encounter.hospitalization.admitSource.coding[0]` | EHA000002 | Datang sendiri | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 4 | 69 | Encounter | `Encounter.hospitalization.admitSource.coding[0]` | 257622000 | Healthcare facility | http://snomed.info/sct |
| 5 | 70 | Encounter | `Encounter.hospitalization.admitSource.coding[0]` | EHA000001 | Kader/ Komunitas | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 6 | 71 | Encounter | `Encounter.hospitalization.admitSource.coding[0]` | gp | General Practitioner referral | http://terminology.hl7.org/CodeSystem/admit-source |
| 7 | 72 | Encounter | `Encounter.hospitalization.admitSource.coding[0]` | TK000031 | Rujukan Poli | http://terminology.kemkes.go.id |
| 8 | 73 | Encounter | `Encounter.hospitalization.admitSource.coding[0]` | other | Other | http://terminology.hl7.org/CodeSystem/admit-source |
| 9 | 87 | Condition | `Condition.code.coding` | A16.2 | Tuberculosis of lung, without mention of bacteriological or histological confirmation | http://hl7.org/fhir/sid/icd-10 |
| 10 | 88 | Condition | `Condition.code.coding` | A18 | Tuberculosis of other organs | http://hl7.org/fhir/sid/icd-10 |
| 11 | 96 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 12 | 99 | Observation | `Observation.component.code.coding` | SP000020 | Umur Bulan | http://terminology.kemkes.go.id/sp |
| 13 | 111 | Observation | `Observation.code.coding` | 82810-3 | Pregnancy status | http://loinc.org |
| 14 | 112 | Observation | `Observation.valueCodeableConcept.coding` | LA15173-0 | Pregnant | http://loinc.org |
| 15 | 113 | Observation | `Observation.valueCodeableConcept.coding` | LA26683-5 | Not Pregnant | http://loinc.org |
| 16 | 123 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 17 | 126 | Observation | `Observation.dataAbsentReason` | not-a-number | Not a Number (NaN) | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 18 | 136 | Observation | `Observation.code.coding` | 8302-2 | Body height | http://loinc.org |
| 19 | 139 | Observation | `Observation.dataAbsentReason` | not-a-number | Not a Number (NaN) | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 20 | 149 | Observation | `Observation.code.coding` | 827034002 | Scar of skin following Bacillus Calmette-Guerin immunization | http://snomed.info/sct |
| 21 | 150 | Observation | `Observation.valueCodeableConcept.coding` | 2667000 | Absent | http://snomed.info/sct |
| 22 | 151 | Observation | `Observation.valueCodeableConcept.coding` | 52101004 | Present | http://snomed.info/sct |
| 23 | 152 | Observation | `Observation.dataAbsentReason` | not-a-number | Not a Number (NaN) | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 24 | 162 | Observation | `Observation.code.coding` | OC000191 | Jumlah Skoring TBC Anak | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 25 | 164 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 26 | 188 | Observation | `Observation.code.coding` | 106229004 | Qualifier for type of diagnosis | http://snomed.info/sct |
| 27 | 189 | Observation | `Observation.valueCodeableConcept.coding` | tb-bac | Terkonfirmasi bakteriologis | http://terminology.kemkes.go.id/CodeSystem/tb-case-definition |
| 28 | 190 | Observation | `Observation.valueCodeableConcept.coding` | tb-clin | Terdiagnosis klinis | http://terminology.kemkes.go.id/CodeSystem/tb-case-definition |
| 29 | 209 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | new | Kasus Baru | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 30 | 210 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | relapse | Kasus Kambuh | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 31 | 211 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | loss-to-follow-up | Kasus Setelah Loss To Follow Up | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 32 | 212 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure | Kasus Pengobatan Setelah Gagal | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 33 | 213 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | not-eval | Pernah diobati tidak diketahui hasilnya | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 34 | 214 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | other | Kasus lain-lain | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 35 | 220 | Observation | `Observation.code.coding` | 365866002 | Finding of human immunodeficiency virus status | http://snomed.info/sct |
| 36 | 221 | Observation | `Observation.valueCodeableConcept.coding` | 165816005 | Human immunodeficiency virus detected | http://snomed.info/sct |
| 37 | 222 | Observation | `Observation.valueCodeableConcept.coding` | 165815009 | Human immunodeficiency virus not detected | http://snomed.info/sct |
| 38 | 223 | Observation | `Observation.dataAbsentReason` | unknown | Unknown | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 39 | 232 | Observation | `Observation.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 40 | 233 | Observation | `Observation.code.coding` | X099388 | Biakan TB | http://terminology.kemkes.go.id/CodeSystem/examination |
| 41 | 234 | Observation | `Observation.code.coding` | 89372-7 | MTB complex DNA and rpoB RIF resistance mutation panel [Presence] | http://loinc.org |
| 42 | 235 | Observation | `Observation.valueCodeableConcept.coding` | 260385009 | Negative | http://snomed.info/sct |
| 43 | 236 | Observation | `Observation.valueCodeableConcept.coding` | LA11841-6 | 1+ | http://loinc.org |
| 44 | 237 | Observation | `Observation.valueCodeableConcept.coding` | LA11842-4 | 2+ | http://loinc.org |
| 45 | 238 | Observation | `Observation.valueCodeableConcept.coding` | LA11843-2 | 3+ | http://loinc.org |
| 46 | 241 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 47 | 251 | Observation | `Observation.code.coding` | 23539-0 | Tuberculosis reaction wheal [Diameter] --3 days post dose mammalian tuberculin intradermal | http://loinc.org |
| 48 | 264 | Observation | `Observation.code.coding` | 24648-8 | XR Chest PA upright | http://loinc.org |
| 49 | 275 | Observation | `Observation.code.coding` | 48635004 | Fine needle biopsy | http://snomed.info/sct |
| 50 | 286 | Observation | `Observation.code.coding` | X099388 | Biakan TB | http://terminology.kemkes.go.id/CodeSystem/examination |
| 51 | 288 | Observation | `Observation.component.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 52 | 289 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 53 | 290 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 54 | 297 | Observation | `Observation.code.coding` | 33248-6 | Diabetes status | http://loinc.org |
| 55 | 298 | Observation | `Observation.valueCodeableConcept.coding` | 10828004 | Positive | http://snomed.info/sct |
| 56 | 299 | Observation | `Observation.valueCodeableConcept.coding` | 260385009 | Negative | http://snomed.info/sct |
| 57 | 309 | Observation | `Observation.code.coding` | SP000047 | Hasil Tes Diabetes Melitus | http://terminology.kemkes.go.id/sp |
| 58 | 310 | Observation | `Observation.valueCodeableConcept.coding` | 10828004 | Positive | http://snomed.info/sct |
| 59 | 311 | Observation | `Observation.valueCodeableConcept.coding` | 260385009 | Negative | http://snomed.info/sct |
| 60 | 321 | Observation | `Observation.code.coding` | 1284985006 | Diabetes mellitus management program | http://snomed.info/sct |
| 61 | 322 | Observation | `Observation.valueCodeableConcept.coding` | SP000372 | Obat Hipoglikemik Oral | http://terminology.kemkes.go.id/sp |
| 62 | 323 | Observation | `Observation.valueCodeableConcept.coding` | 308755006 | Subcutaneous injection of insulin | http://snomed.info/sct |
| 63 | 344 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 64 | 356 | Observation | `Observation.code.coding` | SP000790 | Hasil Pemeriksaan Kontak TBC | http://terminology.kemkes.go.id/sp |
| 65 | 357 | Observation | `Observation.valueCodeableConcept.coding` | SP000208 | Tidak TBC | http://terminology.kemkes.go.id/sp |
| 66 | 358 | Observation | `Observation.valueCodeableConcept.coding` | 11999007 | Inactive tuberculosis | http://snomed.info/sct |
| 67 | 359 | Observation | `Observation.valueCodeableConcept.coding` | 56717001 | Tuberculosis | http://snomed.info/sct |
| 68 | 377 | CarePlan | `CarePlan.activity.detail.code.coding` | CP000004 | Bentuk OAT | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 69 | 378 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000091 | KDT | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 70 | 379 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000092 | Kombipak | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 71 | 380 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000093 | Obat Lepas | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 72 | 382 | CarePlan | `CarePlan.activity.detail.code.coding` | CP000006 | Paduan OAT | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 73 | 383 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000007 | OAT Kategori 1 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 74 | 384 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000008 | OAT Kategori 2 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 75 | 385 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000009 | OAT Kategori Anak | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 76 | 387 | CarePlan | `CarePlan.activity.detail.code.coding` | SP000795 | Sumber Obat | http://terminology.kemkes.go.id/sp |
| 77 | 388 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | SP000791 | Program TBC | http://terminology.kemkes.go.id/sp |
| 78 | 389 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | SP000792 | Asuransi | http://terminology.kemkes.go.id/sp |
| 79 | 391 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | SP000793 | Bayar Sendiri | http://terminology.kemkes.go.id/sp |
| 80 | 392 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 81 | 394 | CarePlan | `CarePlan.activity.outcomeCodeableConcept.coding` | 371001000 | Patient cured | http://snomed.info/sct |
| 82 | 395 | CarePlan | `CarePlan.activity.outcomeCodeableConcept.coding` | 182992009 | Treatment completed | http://snomed.info/sct |
| 83 | 396 | CarePlan | `CarePlan.activity.outcomeCodeableConcept.coding` | 419099009 | Dead | http://snomed.info/sct |
| 84 | 397 | CarePlan | `CarePlan.activity.outcomeCodeableConcept.coding` | CP000094 | Pengobatan Gagal | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 85 | 398 | CarePlan | `CarePlan.activity.outcomeCodeableConcept.coding` | 399307001 | Lost to follow-up | http://snomed.info/sct |
| 86 | 399 | CarePlan | `CarePlan.activity.outcomeCodeableConcept.coding` | CP000096 | Tidak dievaluasi/pindah | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 87 | 440 | Observation | `Observation.code.coding` | SP000796 | Jumlah OAT | http://terminology.kemkes.go.id/sp |
| 88 | 453 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 89 | 454 | Observation | `Observation.code.coding` | ANC.B8.DE3 | Current weight | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 90 | 501 | Observation | `Observation.code.coding` | SP000796 | Jumlah OAT | http://terminology.kemkes.go.id/sp |
| 91 | 514 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 92 | 515 | Observation | `Observation.code.coding` | ANC.B8.DE3 | Current weight | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 93 | 526 | Procedure | `Procedure.code.coding` | TK000016 | Edukasi Tes HIV | http://terminology.kemkes.go.id |
| 94 | 538 | Observation | `Observation.code.coding` | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 95 | 539 | Observation | `Observation.valueCodeableConcept.coding` | LA15255-5 | Reactive | http://loinc.org |
| 96 | 540 | Observation | `Observation.valueCodeableConcept.coding` | LA15256-3 | Nonreactive | http://loinc.org |
| 97 | 541 | Observation | `Observation.dataAbsentReason` | LA9663-1 | Inconclusive | http://loinc.org |
| 98 | 549 | Observation | `Observation.code.coding` | SP000123 | Integrasi Program | http://terminology.kemkes.go.id/sp |
| 99 | 550 | Observation | `Observation.component.code.coding` | SP000371 | Cotrimoxazole | http://terminology.kemkes.go.id/sp |
| 100 | 553 | Observation | `Observation.component.code.coding` | SP000046 | Terapi Antiretroviral (ART) | http://terminology.kemkes.go.id/sp |
| 101 | 564 | Observation | `Observation.code.coding` | SP000797 | Pindah Register Pasien TB RO | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 25 |
| http://loinc.org | 22 |
| http://terminology.kemkes.go.id/sp | 15 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 13 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 6 |
| http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment | 6 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 2 |
| http://terminology.hl7.org/CodeSystem/admit-source | 2 |
| http://terminology.kemkes.go.id | 2 |
| http://hl7.org/fhir/sid/icd-10 | 2 |
| http://terminology.kemkes.go.id/CodeSystem/tb-case-definition | 2 |
| http://terminology.kemkes.go.id/CodeSystem/examination | 2 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 2 |
| **Total** | **101** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 76 | – | Nama Faskes (Pindahan dari) | Organization | `Organization.name` |
| 77 | – | Alamat Faskes (Pindahan dari) | Organization | `Organization.address.line` |
| 78 | – | Kab/Kota (Pindahan dari) | Organization | `Organization.address.city` |
| 79 | – | Provinsi (Pindahan dari) | Organization | `Organization.address.state` |
| 180 | – | Nama Faskes | Organization | `Organization.name` |
| 181 | – | Kab/Kota | Organization | `Organization.address.city` |
| 182 | – | Provinsi | Organization | `Organization.address.state` |
| 183 | – | No. Reg TBC.03 Faskes | – | `` |
| 184 | – | Tahun | – | `` |
| 185 | – | No. Reg TBC.03 Kab/Kota | – | `` |
| 331 | – | No. Urut Kontak | – | `` |
