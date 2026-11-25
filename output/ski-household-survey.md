# Output Form: SKI - Sahabat Sehat Household Survey

Sumber: `mapping/phdt-data-dictionary-ski-household-survey.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-ski-household-survey.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 14 |
| Code (`jumlah code` = 1) | 102 |
| Code unik (code + CodeSystem) | 74 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 44 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 17–40 | Patient | – | – | _Nama ART_ → `Patient.name.text` (17, tanpa BQ)<br>_No Ktp_ → `Patient.identifier.value` (20, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (22, tanpa BQ)<br>_Tanggal lahir ART_ → `Patient.birthDate` (24, tanpa BQ)<br>_Alamat Domisili_ → `Patient.address.use` (25, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (31, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (34, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.extension.valueCode` (37, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.extension.valueCode` (40, tanpa BQ) |
| 2 | 41–60 | Practitioner | – | – | _ID Sahabat Sehat (3 angka terakhir)_ → `Practitioner.identifier` (41, tanpa BQ)<br>_Nama Practitioner_ → `Practitioner.name.text` (43, tanpa BQ)<br>_Jenis Kelamin_ → `Practitioner.gender` (44, tanpa BQ) |
| 3 | 61–74 | Encounter | – | – | _Start time_ → `Encounter.period.start` (69, tanpa BQ)<br>_Completion time_ → `Encounter.period.end` (70, tanpa BQ)<br>_Start time_ → `Encounter.statusHistory.period.start` (84, tanpa BQ)<br>_Start time_ → `Encounter.statusHistory.period.end` (85, tanpa BQ)<br>_Start time_ → `Encounter.statusHistory.period.start` (87, tanpa BQ)<br>_Completion time_ → `Encounter.statusHistory.period.end` (88, tanpa BQ)<br>_Completion time_ → `Encounter.statusHistory.period.start` (90, tanpa BQ)<br>_Completion time_ → `Encounter.statusHistory.period.end` (91, tanpa BQ) |
| 4 | 75–81 | Condition | 243790003.0 | Infection screening | _Start time_ → `Condition.recordedDate` (81, tanpa BQ) |
| 5 | 93–143 | QuestionnaireResponse | – | – | _Jenis Survei_ → `QuestionnaireResponse.identifier.type.coding` (94, tanpa BQ)<br>_Nama ART_ → `QuestionnaireResponse.subject.display` (100, tanpa BQ)<br>_Completion time_ → `QuestionnaireResponse.authored` (101, tanpa BQ)<br>_A01. Dalam 1 bulan terakhir, apakah [NAMA] pernah didiagnosis menderita diare oleh tenaga kesehatan?_ → `QuestionnaireResponse.item.item.linkId` (106, tanpa BQ)<br>_A02. Jenis tenaga kesehatan yang mendiagnosis [NAMA] diare?_ → `QuestionnaireResponse.item.item.linkId` (112, tanpa BQ)<br>_A03c. Dalam 1 bulan terakhir, apakah [NAMA] pernah mengalami Kotoran/ tinja lembek atau cair_ → `QuestionnaireResponse.item.item.linkId` (117, tanpa BQ)<br>_A03a. Dalam 1 bulan terakhir, apakah [NAMA] pernah mengalami BAB 3-6 kali dalam sehari_ → `QuestionnaireResponse.item.item.linkId` (123, tanpa BQ)<br>_A03b. Dalam 1 bulan terakhir, apakah [NAMA] pernah mengalami BAB > 6 kali dalam sehari_ → `QuestionnaireResponse.item.item.linkId` (129, tanpa BQ)<br>_Dalam 1 bulan terakhir, apakah responden pernah mengalami dehidrasi (kurang minum)?_ → `QuestionnaireResponse.item.item.linkId` (135, tanpa BQ)<br>_Apakah responden mengonsumsi hal-hal ini untuk mengatasi diare?_ → `QuestionnaireResponse.item.item.linkId` (141, tanpa BQ)<br>_A05. Dalam 1 bulan terakhir, apakah [NAMA] pernah didiagnosis ISPA oleh tenaga kesehatan?_ → `QuestionnaireResponse.item.item.linkId` (161, tanpa BQ)<br>_A06. Jenis tenaga kesehatan yang mendiagnosis [NAMA] ISPA? -> A09_ → `QuestionnaireResponse.item.item.linkId` (165, tanpa BQ)<br>_A07. Dalam 1 bulan terakhir, [NAMA] mengalami gejala berikut?_ → `QuestionnaireResponse.item.item.linkId` (171, tanpa BQ)<br>_*Apakah [NAMA] mengalami minimal satu gejala diatas?_ → `QuestionnaireResponse.item.item.linkId` (188, tanpa BQ)<br>_A08. Jika Ya, apakah [NAMA] terkonfirmasi COVID-19 melalui pemeriksaan antigen dan atau PCR?_ → `QuestionnaireResponse.item.item.linkId` (192, tanpa BQ)<br>_A09. Dalam 1 tahun terakhir, apakah [NAMA] pernah didiagnosis menderita radang paru (Pneumonia) oleh tenaga kesehatan?_ → `QuestionnaireResponse.item.item.linkId` (210, tanpa BQ)<br>_A10.Jenis tenaga kesehatan yang mendiagnosis [NAMA] radang paru (Pneumonia)?_ → `QuestionnaireResponse.item.item.linkId` (216, tanpa BQ)<br>_A11a. Dalam 1 tahun terakhir, apakah [NAMA] mengalami gejala sesak napas disertai gejala sebagai berikut:_ → `QuestionnaireResponse.item.item.linkId` (221, tanpa BQ)<br>_*Berapa Usia ART?_ → `QuestionnaireResponse.item.item.linkId` (238, tanpa BQ)<br>_A12. Dalam 1 tahun terakhir, apakah [NAMA] pernah didiagnosis TBC Paru / Flek paru oleh dokter?_ → `QuestionnaireResponse.item.item.linkId` (244, tanpa BQ)<br>_Pemeriksaan apa yang dilakukan untuk mendiagnosis TB pada responden?_ → `QuestionnaireResponse.item.item.linkId` (250, tanpa BQ)<br>_A14. Jenis obat yang diterima:_ → `QuestionnaireResponse.item.item.linkId` (266, tanpa BQ)<br>_Saat responden mengalami gejala yang berkaitan dengan TB, apakah responden menerima antibiotik lain selain obat antituberkulosis (OAT)?_ → `QuestionnaireResponse.item.item.linkId` (285, tanpa BQ)<br>_Saat responden mengalami gejala yang berkaitan dengan TB, apakah responden menerima antibiotik lain selain obat antituberkulosis (OAT)?_ → `QuestionnaireResponse.item.item.answer.valueBoolean` (287, tanpa BQ)<br>_Obat antibiotik apa yang dikonsumsi oleh responden selain OAT?_ → `QuestionnaireResponse.item.item.linkId` (289, tanpa BQ)<br>_A15. Apakah [NAMA] didiagnosis TB Resisten Obat oleh dokter?_ → `QuestionnaireResponse.item.item.linkId` (306, tanpa BQ)<br>_A16. Apakah ada anggota keluarga atau lainnya yang bertugas sebagai Pengawas Menelan Obat (PMO)?_ → `QuestionnaireResponse.item.item.linkId` (311, tanpa BQ)<br>_Apakah responden rutin menggunakan masker di tempat-tempat berikut?_ → `QuestionnaireResponse.item.item.linkId` (315, tanpa BQ)<br>_A17. Apakah saat ini [NAMA] masih menggunakan obat TBC paru secara rutin?_ → `QuestionnaireResponse.item.item.linkId` (319, tanpa BQ)<br>_A18. Alasan UTAMA [NAMA] tidak minum obat TBC paru secara rutin? ->A22_ → `QuestionnaireResponse.item.item.linkId` (324, tanpa BQ)<br>_Dalam 2 - 4 minggu terakhir, apakah responden secara rutin mengalami gejala-gejala berikut ini?_ → `QuestionnaireResponse.item.item.linkId` (333, tanpa BQ)<br>_A19. Dalam 1 tahun terakhir, apakah [NAMA] pernah di periksa TBC Paru karena ada anggota rumah tangga (ART) lain yang menderita TBC Paru?_ → `QuestionnaireResponse.item.item.linkId` (347, tanpa BQ)<br>_A20. Jika Ya, apakah [NAMA] mendapatkan Terapi/Obat Pencegahan Tuberkulosis?_ → `QuestionnaireResponse.item.item.linkId` (351, tanpa BQ)<br>_A21. Alasan UTAMA [NAMA] tidak mendapatkan Terapi/Obat Pencegahan Tuberkulosis?_ → `QuestionnaireResponse.item.item.linkId` (355, tanpa BQ)<br>_A22. Dalam 1 tahun terakhir, apakah [NAMA] pernah didiagnosis menderita hepatitis oleh dokter?_ → `QuestionnaireResponse.item.item.linkId` (362, tanpa BQ)<br>_A27. Dalam 1 tahun terakhir, Apakah [NAMA] pernah didiagnosis demam berdarah oleh dokter?_ → `QuestionnaireResponse.item.item.answer.valueBoolean` (370, tanpa BQ)<br>_A28. Dalam 1 tahun terakhir, apakah [NAMA] pernah menderita DEMAM disertai dengan tanda dan gejala dibawah ini secara bersamaan?_ → `QuestionnaireResponse.item.item.linkId` (372, tanpa BQ) |
| 6 | 144–158 | MedicationStatement | – | – | _Nama ART_ → `MedicationStatement.subject.display` (147, tanpa BQ)<br>_Completion time_ → `MedicationStatement.dateAsserted` (148, tanpa BQ)<br>_Name_ → `MedicationStatement.informationSource.display` (150, tanpa BQ)<br>_Apakah responden mengonsumsi hal-hal ini untuk mengatasi diare?_ → `MedicationStatement.medicationCodeableConcept.coding` (152, tanpa BQ) |
| 7 | 174–186 | Condition | 386661006.0 | Fever | _Nama ART_ → `Condition.subject.display` (177, tanpa BQ)<br>_Completion time_ → `Condition.recordedDate` (179, tanpa BQ)<br>_ID Sahabat Sehat (3 angka terakhir)_ → `Condition.recorder.reference` (180, tanpa BQ)<br>_A07. Dalam 1 bulan terakhir, [NAMA] mengalami gejala berikut?_ → `Condition.code.coding` (181, tanpa BQ) |
| 8 | 195–207 | Observation | SP000877 | Pemeriksaan Antigen dan/atau PCR COVID 19 | _A08. Jika Ya, apakah [NAMA] terkonfirmasi COVID-19 melalui pemeriksaan antigen dan atau PCR?_ → `Observation.valueCodeableConcept.coding` (198, tanpa BQ)<br>_Nama ART_ → `Observation.subject.display` (202, tanpa BQ)<br>_Completion time_ → `Observation.issued` (205, tanpa BQ)<br>_ID Sahabat Sehat (3 angka terakhir)_ → `Observation.performer.reference` (206, tanpa BQ) |
| 9 | 224–235 | Condition | 267036007.0 | Dyspnea | _Nama ART_ → `Condition.subject.display` (227, tanpa BQ)<br>_Completion time_ → `Condition.recordedDate` (229, tanpa BQ)<br>_ID Sahabat Sehat (3 angka terakhir)_ → `Condition.recorder.reference` (230, tanpa BQ)<br>_A11a. Dalam 1 tahun terakhir, apakah [NAMA] mengalami gejala sesak napas disertai gejala sebagai berikut:_ → `Condition.code.coding` (232, tanpa BQ) |
| 10 | 253–265 | Procedure | 424489006.0 | Mantoux test | _Pemeriksaan apa yang dilakukan untuk mendiagnosis TB pada responden?_ → `Procedure.status` (253, tanpa BQ)<br>_Pemeriksaan apa yang dilakukan untuk mendiagnosis TB pada responden?_ → `Procedure.code.coding` (255, tanpa BQ)<br>_Nama ART_ → `Procedure.subject.display` (262, tanpa BQ)<br>_ID Sahabat Sehat (3 angka terakhir)_ → `Procedure.recorder.reference` (264, tanpa BQ) |
| 11 | 269–284 | Observation | SP000884 | Jenis Obat Tuberkulosis Yang Diterima | _A14. Jenis obat yang diterima:_ → `Observation.component.valueBoolean` (273, tanpa BQ)<br>_Nama ART_ → `Observation.subject.display` (279, tanpa BQ)<br>_Completion time_ → `Observation.issued` (282, tanpa BQ)<br>_ID Sahabat Sehat (3 angka terakhir)_ → `Observation.performer.reference` (283, tanpa BQ) |
| 12 | 292–305 | Observation | SP000887 | Konsumsi Obat Antibiotik Selain OAT | _Saat responden mengalami gejala yang berkaitan dengan TB, apakah responden menerima antibiotik lain selain obat antituberkulosis (OAT)?_ → `Observation.valueBoolean` (295, tanpa BQ)<br>_Obat antibiotik apa yang dikonsumsi oleh responden selain OAT?_ → `Observation.component.code.coding` (297, tanpa BQ)<br>_Nama ART_ → `Observation.subject.display` (300, tanpa BQ)<br>_Completion time_ → `Observation.issued` (303, tanpa BQ)<br>_ID Sahabat Sehat (3 angka terakhir)_ → `Observation.performer.reference` (304, tanpa BQ) |
| 13 | 336–346 | Condition | 49727002.0 | Cough | _Nama ART_ → `Condition.subject.display` (339, tanpa BQ)<br>_Completion time_ → `Condition.recordedDate` (341, tanpa BQ)<br>_ID Sahabat Sehat (3 angka terakhir)_ → `Condition.recorder.reference` (342, tanpa BQ)<br>_Dalam 2 - 4 minggu terakhir, apakah responden secara rutin mengalami gejala-gejala berikut ini?_ → `Condition.code.coding` (343, tanpa BQ) |
| 14 | 375–394 | Condition | 386661006.0 | Fever | _Nama ART_ → `Condition.subject.display` (378, tanpa BQ)<br>_Completion time_ → `Condition.recordedDate` (380, tanpa BQ)<br>_ID Sahabat Sehat (3 angka terakhir)_ → `Condition.recorder.reference` (381, tanpa BQ)<br>_A28. Dalam 1 tahun terakhir, apakah [NAMA] pernah menderita DEMAM disertai dengan tanda dan gejala dibawah ini secara bersamaan?_ → `Condition.code.coding` (383, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Condition | 5 |
| Observation | 3 |
| Patient | 1 |
| Practitioner | 1 |
| Encounter | 1 |
| QuestionnaireResponse | 1 |
| MedicationStatement | 1 |
| Procedure | 1 |
| **Total** | **14** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 77 | Condition | `Condition.code.coding` | 243790003.0 | Infection screening | http://snomed.info/sct |
| 2 | 94 | QuestionnaireResponse | `QuestionnaireResponse.identifier.type.coding` | SP000834 | Survei umum | http://terminology.kemkes.go.id/sp |
| 3 | 95 | QuestionnaireResponse | `QuestionnaireResponse.identifier.type.coding` | SP000835 | Survei umum crosscheck | http://terminology.kemkes.go.id/sp |
| 4 | 96 | QuestionnaireResponse | `QuestionnaireResponse.identifier.type.coding` | SP000836 | Survei ibu hamil | http://terminology.kemkes.go.id/sp |
| 5 | 97 | QuestionnaireResponse | `QuestionnaireResponse.identifier.type.coding` | SP000837 | Survei ibu hamil crosscheck | http://terminology.kemkes.go.id/sp |
| 6 | 108 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000838 | Ya, ≤ 2 minggu terakhir | http://terminology.kemkes.go.id/sp |
| 7 | 109 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000839 | Ya, > 2 minggu - 1 bulan | http://terminology.kemkes.go.id/sp |
| 8 | 110 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | QRI000014 | Tidak | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 9 | 111 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 261665006.0 | Unknown | http://snomed.info/sct |
| 10 | 114 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 309343006.0 | Physician | http://snomed.info/sct |
| 11 | 115 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 309453006.0 | Registered midwife | http://snomed.info/sct |
| 12 | 116 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 224535009.0 | Registered nurse | http://snomed.info/sct |
| 13 | 119 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000838 | Ya, ≤ 2 minggu terakhir | http://terminology.kemkes.go.id/sp |
| 14 | 120 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000839 | Ya, > 2 minggu - 1 bulan | http://terminology.kemkes.go.id/sp |
| 15 | 121 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | QRI000014 | Tidak | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 16 | 122 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 261665006.0 | Unknown | http://snomed.info/sct |
| 17 | 125 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000838 | Ya, ≤ 2 minggu terakhir | http://terminology.kemkes.go.id/sp |
| 18 | 126 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000839 | Ya, > 2 minggu - 1 bulan | http://terminology.kemkes.go.id/sp |
| 19 | 127 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | QRI000014 | Tidak | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 20 | 128 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 261665006.0 | Unknown | http://snomed.info/sct |
| 21 | 131 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000838 | Ya, ≤ 2 minggu terakhir | http://terminology.kemkes.go.id/sp |
| 22 | 132 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000839 | Ya, > 2 minggu - 1 bulan | http://terminology.kemkes.go.id/sp |
| 23 | 133 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | QRI000014 | Tidak | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 24 | 134 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 261665006.0 | Unknown | http://snomed.info/sct |
| 25 | 137 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000838 | Ya, ≤ 2 minggu terakhir | http://terminology.kemkes.go.id/sp |
| 26 | 138 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000839 | Ya, > 2 minggu - 1 bulan | http://terminology.kemkes.go.id/sp |
| 27 | 139 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | QRI000014 | Tidak | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 28 | 140 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 261665006.0 | Unknown | http://snomed.info/sct |
| 29 | 152 | MedicationStatement | `MedicationStatement.medicationCodeableConcept.coding` | SP000872 | Oralit | http://terminology.kemkes.go.id/sp |
| 30 | 153 | MedicationStatement | `MedicationStatement.medicationCodeableConcept.coding` | SP000873 | Larutan Gula Garam (LGG) | http://terminology.kemkes.go.id/sp |
| 31 | 154 | MedicationStatement | `MedicationStatement.medicationCodeableConcept.coding` | SP000874 | Probiotik | http://terminology.kemkes.go.id/sp |
| 32 | 155 | MedicationStatement | `MedicationStatement.medicationCodeableConcept.coding` | SP000875 | Obat anti diare | http://terminology.kemkes.go.id/sp |
| 33 | 156 | MedicationStatement | `MedicationStatement.medicationCodeableConcept.coding` | SP000876 | Antibiotik | http://terminology.kemkes.go.id/sp |
| 34 | 167 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 309343006.0 | Physician | http://snomed.info/sct |
| 35 | 168 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 309453006.0 | Registered midwife | http://snomed.info/sct |
| 36 | 169 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 224535009.0 | Registered nurse | http://snomed.info/sct |
| 37 | 170 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 74964007.0 | Other | http://snomed.info/sct |
| 38 | 181 | Condition | `Condition.code.coding` | 386661006.0 | Fever | http://snomed.info/sct |
| 39 | 182 | Condition | `Condition.code.coding` | 788062371000119104 | Acute cough | http://snomed.info/sct |
| 40 | 184 | Condition | `Condition.code.coding` | 82272006.0 | Common cold | http://snomed.info/sct |
| 41 | 186 | Condition | `Condition.code.coding` | 267102003.0 | Sore throat | http://snomed.info/sct |
| 42 | 187 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000856 | Tidak Mengalami Gejala Apapun | http://terminology.kemkes.go.id/sp |
| 43 | 197 | Observation | `Observation.code.coding` | SP000877 | Pemeriksaan Antigen dan/atau PCR COVID 19 | http://terminology.kemkes.go.id/sp |
| 44 | 198 | Observation | `Observation.valueCodeableConcept.coding` | 1240581000000104 | Severe acute respiratory syndrome coronavirus 2 detected | http://snomed.info/sct |
| 45 | 199 | Observation | `Observation.valueCodeableConcept.coding` | 1240591000000102 | Severe acute respiratory syndrome coronavirus 2 not detected | http://snomed.info/sct |
| 46 | 200 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 47 | 212 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000878 | Ya, kurang dari 1 bulan terakhir | http://terminology.kemkes.go.id/sp |
| 48 | 213 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000879 | Ya, 1-12 bulan yang lalu | http://terminology.kemkes.go.id/sp |
| 49 | 214 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | QRI000014 | Tidak | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 50 | 215 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 261665006.0 | Unknown | http://snomed.info/sct |
| 51 | 231 | Condition | `Condition.code.coding` | 267036007.0 | Dyspnea | http://snomed.info/sct |
| 52 | 232 | Condition | `Condition.code.coding` | 386661006.0 | Fever | http://snomed.info/sct |
| 53 | 233 | Condition | `Condition.code.coding` | 49727002.0 | Cough | http://snomed.info/sct |
| 54 | 234 | Condition | `Condition.code.coding` | 230145002.0 | Difficulty breathing | http://snomed.info/sct |
| 55 | 236 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 162467007.0 | Free of symptoms | http://snomed.info/sct |
| 56 | 240 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000880 | Usia <5 Tahun | http://terminology.kemkes.go.id/sp |
| 57 | 241 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000881 | Usia ≥ 5 Tahun | http://terminology.kemkes.go.id/sp |
| 58 | 246 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000882 | Ya, dalam 6 bulan terakhir | http://terminology.kemkes.go.id/sp |
| 59 | 247 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000883 | Ya, lebih dari 6 bulan | http://terminology.kemkes.go.id/sp |
| 60 | 248 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | QRI000014 | Tidak | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 61 | 255 | Procedure | `Procedure.code.coding` | 424489006.0 | Mantoux test | http://snomed.info/sct |
| 62 | 256 | Procedure | `Procedure.code.coding` | 35140007.0 | Interferon gamma assay | http://snomed.info/sct |
| 63 | 257 | Procedure | `Procedure.code.coding` | 269911007.0 | Sputum examination | http://snomed.info/sct |
| 64 | 258 | Procedure | `Procedure.code.coding` | 167995008.0 | Sputum microscopy | http://snomed.info/sct |
| 65 | 259 | Procedure | `Procedure.code.coding` | SP000864 | Pemeriksaan Dahak (Tes Cepat Molekuler) | http://terminology.kemkes.go.id/sp |
| 66 | 260 | Procedure | `Procedure.code.coding` | 399208008.0 | Plain X-ray of chest | http://snomed.info/sct |
| 67 | 271 | Observation | `Observation.code.coding` | SP000884 | Jenis Obat Tuberkulosis Yang Diterima | http://terminology.kemkes.go.id/sp |
| 68 | 272 | Observation | `Observation.component.code.coding` | SP000885 | Kombinasi Dosis Tetap (KDT) | http://terminology.kemkes.go.id/sp |
| 69 | 274 | Observation | `Observation.component.code.coding` | SP000886 | Kombipak/ Lepasan | http://terminology.kemkes.go.id/sp |
| 70 | 276 | Observation | `Observation.component.code.coding` | 59108006.0 | Injection | http://snomed.info/sct |
| 71 | 294 | Observation | `Observation.code.coding` | SP000887 | Konsumsi Obat Antibiotik Selain OAT | http://terminology.kemkes.go.id/sp |
| 72 | 297 | Observation | `Observation.component.code.coding` | SP000888 | Jenis Obat Antibiotik Selain OAT | http://terminology.kemkes.go.id/sp |
| 73 | 310 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 261665006.0 | Unknown | http://snomed.info/sct |
| 74 | 317 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer[0].valueCoding` | 394778007.0 | Client's or patient's home | http://snomed.info/sct |
| 75 | 318 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer[1].valueCoding` | 276052003.0 | Public facilities | http://snomed.info/sct |
| 76 | 321 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 50811001.0 | Routine | http://snomed.info/sct |
| 77 | 322 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000871 | Tidak Rutin | http://terminology.kemkes.go.id/sp |
| 78 | 323 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 371001000.0 | Patient cured | http://snomed.info/sct |
| 79 | 326 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000852 | Merasa Sudah Sehat | http://terminology.kemkes.go.id/sp |
| 80 | 327 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000853 | Obat Tidak Tersedia di Fasilitas Pelayanan Kesehatan | http://terminology.kemkes.go.id/sp |
| 81 | 328 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 182897004.0 | Drug declined by patient - side effects | http://snomed.info/sct |
| 82 | 329 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000854 | Memilih Minum Obat Tradisional | http://terminology.kemkes.go.id/sp |
| 83 | 330 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000855 | Bosan/ Malas/ Sering Lupa | http://terminology.kemkes.go.id/sp |
| 84 | 331 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000869 | Akses ke Fasilitas Pelayanan Kesehatan Jauh | http://terminology.kemkes.go.id/sp |
| 85 | 332 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000870 | Tidak Memiliki BPJS/ Biaya Perawatan | http://terminology.kemkes.go.id/sp |
| 86 | 343 | Condition | `Condition.code.coding` | 49727002.0 | Cough | http://snomed.info/sct |
| 87 | 344 | Condition | `Condition.code.coding` | 386661006.0 | Fever | http://snomed.info/sct |
| 88 | 345 | Condition | `Condition.code.coding` | 448765001.0 | Unintentional weight loss | http://snomed.info/sct |
| 89 | 346 | Condition | `Condition.code.coding` | 42984000.0 | Night sweats | http://snomed.info/sct |
| 90 | 357 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000867 | Merasa Tidak Gejala/ Sakit | http://terminology.kemkes.go.id/sp |
| 91 | 358 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000853 | Obat Tidak Tersedia di Fasilitas Pelayanan Kesehatan | http://terminology.kemkes.go.id/sp |
| 92 | 359 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000868 | Tidak Diberikan Obat Oleh Nakes | http://terminology.kemkes.go.id/sp |
| 93 | 382 | Condition | `Condition.code.coding` | 386661006.0 | Fever | http://snomed.info/sct |
| 94 | 383 | Condition | `Condition.code.coding` | 267096005.0 | Frontal headache | http://snomed.info/sct |
| 95 | 385 | Condition | `Condition.code.coding` | 86260003.0 | Pain around eye | http://snomed.info/sct |
| 96 | 387 | Condition | `Condition.code.coding` | 279069000.0 | Musculoskeletal pain | http://snomed.info/sct |
| 97 | 389 | Condition | `Condition.code.coding` | 16331000.0 | Heartburn | http://snomed.info/sct |
| 98 | 390 | Condition | `Condition.code.coding` | SP000866 | Mual/ Muntah/ Tidak Nafsu Makan | http://terminology.kemkes.go.id/sp |
| 99 | 391 | Condition | `Condition.code.coding` | 13791008.0 | Asthenia | http://snomed.info/sct |
| 100 | 392 | Condition | `Condition.code.coding` | 771542000.0 | Cold extremity | http://snomed.info/sct |
| 101 | 393 | Condition | `Condition.code.coding` | 271813007.0 | Petechiae | http://snomed.info/sct |
| 102 | 394 | Condition | `Condition.code.coding` | 249366005.0 | Bleeding from nose | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 50 |
| http://terminology.kemkes.go.id/sp | 44 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 7 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 1 |
| **Total** | **102** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 2 | – | Id | – | `` |
| 3 | – | Response Id | – | `` |
| 4 | – | Survey Id | – | `` |
| 5 | – | Start time | – | `` |
| 6 | – | Sync time | – | `` |
| 7 | – | Survey submission status | – | `` |
| 9 | – | Completion time | – | `` |
| 10 | – | Email | – | `` |
| 11 | – | Name | – | `` |
| 12 | – | Nama ART | – | `` |
| 13 | – | Nama ART (konfirmasi) | – | `` |
| 14 | – | Tanggal lahir ART | – | `` |
| 15 | – | ID Sahabat Sehat (3 angka terakhir) | – | `` |
| 16 | – | ID rumah (dari DWS) | – | `` |
| 237 | – | A11b. Dalam 1 tahun terakhir, apakah [NAMA] mengalami gejala sesak napas disertai gejala sebagai berikut: | – | `` |
| 249 | – | *Apakah usia ART < 15 TAHUN? | – | `` |
