# Output Form: SKI - Individu Bagian B (Penyakit)

Sumber: `mapping/phdt-data-dictionary-ski-individu-penyakit.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-ski-individu-penyakit.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 12 |
| Code (`jumlah code` = 1) | 56 |
| Code unik (code + CodeSystem) | 46 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 25 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 18–41 | Patient | – | – | _Nama ART_ → `Patient.name.text` (18, tanpa BQ)<br>_No Ktp_ → `Patient.identifier.value` (21, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (23, tanpa BQ)<br>_Tanggal lahir ART_ → `Patient.birthDate` (25, tanpa BQ)<br>_Alamat Domisili_ → `Patient.address.use` (26, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (32, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (35, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.extension.valueCode` (38, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.extension.valueCode` (41, tanpa BQ) |
| 2 | 42–61 | Practitioner | – | – | _ID Sahabat Sehat (3 angka terakhir)_ → `Practitioner.identifier` (42, tanpa BQ)<br>_Nama Practitioner_ → `Practitioner.name.text` (44, tanpa BQ)<br>_Jenis Kelamin_ → `Practitioner.gender` (45, tanpa BQ) |
| 3 | 62–75 | Encounter | – | – | _Start time_ → `Encounter.period.start` (70, tanpa BQ)<br>_Completion time_ → `Encounter.period.end` (71, tanpa BQ)<br>_Start time_ → `Encounter.statusHistory.period.start` (85, tanpa BQ)<br>_Start time_ → `Encounter.statusHistory.period.end` (86, tanpa BQ)<br>_Start time_ → `Encounter.statusHistory.period.start` (88, tanpa BQ)<br>_Completion time_ → `Encounter.statusHistory.period.end` (89, tanpa BQ)<br>_Completion time_ → `Encounter.statusHistory.period.start` (91, tanpa BQ)<br>_Completion time_ → `Encounter.statusHistory.period.end` (92, tanpa BQ) |
| 4 | 76–82 | Condition | 312851005.0 | Screening for disorder | _Start time_ → `Condition.recordedDate` (82, tanpa BQ) |
| 5 | 94–113 | QuestionnaireResponse | – | – | _Jenis Survei_ → `QuestionnaireResponse.identifier.type.coding` (95, tanpa BQ)<br>_Nama ART_ → `QuestionnaireResponse.subject.display` (101, tanpa BQ)<br>_Completion time_ → `QuestionnaireResponse.authored` (102, tanpa BQ)<br>_ID Sahabat Sehat (3 angka terakhir)_ → `QuestionnaireResponse.author.reference` (103, tanpa BQ)<br>_B07a. Apakah [NAMA] pernah didiagnosis diabetes mellitus (DM)/ kencing manis oleh dokter?_ → `QuestionnaireResponse.item.item.linkId` (107, tanpa BQ)<br>_B07b. Tipe atau jenis diabetes mellitus (DM)/ kencing manis yang diderita oleh [NAMA]?_ → `QuestionnaireResponse.item.item.linkId` (111, tanpa BQ)<br>_B08. Umur berapa [NAMA] pertama kali didiagnosis diabetes mellitus (DM)/ kencing manis?_ → `QuestionnaireResponse.item.item.linkId` (125, tanpa BQ)<br>_Apakah responden menerima obat untuk mengatasi diabetes mellitus (DM)/kencing manis?_ → `QuestionnaireResponse.item.item.linkId` (129, tanpa BQ)<br>_B09. Jenis pengobatan apa yang diperoleh [NAMA]?_ → `QuestionnaireResponse.item.item.linkId` (133, tanpa BQ)<br>_B09a. Apakah pada jawaban sebelumnya, [NAMA] menjawab belum butuh obat anti DM?_ → `QuestionnaireResponse.item.item.linkId` (156, tanpa BQ)<br>_B10. Apakah [NAMA] minum/suntik obat anti diabetes sesuai petunjuk dokter?_ → `QuestionnaireResponse.item.item.linkId` (160, tanpa BQ)<br>_B11. Alasan UTAMA [NAMA] tidak minum/suntik obat DM sesuai petunjuk dokter?_ → `QuestionnaireResponse.item.item.linkId` (164, tanpa BQ)<br>_B12. Apakah [NAMA] memeriksakan ulang (kontrol) penyakit DM ke fasilitas pelayanan kesehatan?_ → `QuestionnaireResponse.item.item.linkId` (171, tanpa BQ)<br>_B13. Apakah [NAMA] pernah mendapatkan informasi/penjelasan bahwa obat DM harus diminum terus menerus/ seumur hidup?_ → `QuestionnaireResponse.item.item.linkId` (177, tanpa BQ)<br>_B14. Apa yang [NAMA] lakukan untuk mengendalikan diabetes mellitus? ->B16_ → `QuestionnaireResponse.item.item.linkId` (181, tanpa BQ)<br>_B15. Apakah [NAMA] dalam 1 bulan terakhir mengalami gejala:_ → `QuestionnaireResponse.item.item.linkId` (186, tanpa BQ)<br>_Pemeriksaan apa yang terakhir kali responden lakukan dalam mengontrol diabetes mellitus (DM)/kencing manis?_ → `QuestionnaireResponse.item.item.linkId` (201, tanpa BQ)<br>_Apakah responden rutin melakukan pemeriksaan HbA1c?_ → `QuestionnaireResponse.item.item.linkId` (215, tanpa BQ)<br>_Berapa nilai HbA1c terakhir responden?_ → `QuestionnaireResponse.item.item.linkId` (222, tanpa BQ)<br>_B16. Apakah [NAMA] pernah didiagnosis menderita sakit jantung oleh dokter?_ → `QuestionnaireResponse.item.item.linkId` (238, tanpa BQ)<br>_B17. Umur berapa [NAMA] pertama kali didiagnosis penyakit jantung?_ → `QuestionnaireResponse.item.item.linkId` (242, tanpa BQ)<br>_*Apakah [NAMA] berusia ≥ 15 TAHUN ?_ → `QuestionnaireResponse.item.item.linkId` (248, tanpa BQ)<br>_B18. Apakah [NAMA] pernah didiagnosis menderita hipertensi oleh dokter?_ → `QuestionnaireResponse.item.item.linkId` (252, tanpa BQ)<br>_B19. Umur berapa [NAMA] pertama kali didiagnosis hipertensi?_ → `QuestionnaireResponse.item.item.linkId` (256, tanpa BQ)<br>_B20. Apakah [NAMA] memeriksakan ulang (kontrol) penyakit hipertensi yang dialami ke fasilitas pelayanan kesehatan?_ → `QuestionnaireResponse.item.item.linkId` (260, tanpa BQ)<br>_Seberapa sering responden mengukur tekanan darah di tempat berikut?_ → `QuestionnaireResponse.item.item.linkId` (266, tanpa BQ)<br>_B21. Apakah [NAMA] minum obat anti hipertensi? PERLIHATKAN BUKU PERAGA_ → `QuestionnaireResponse.item.item.linkId` (273, tanpa BQ)<br>_B22. Alasan UTAMA [NAMA] tidak teratur / tidak minum obat anti hipertensi?_ → `QuestionnaireResponse.item.item.linkId` (278, tanpa BQ)<br>_B23. Apakah [NAMA] pernah mendapatkan informasi/penjelasan bahwa obat anti hipertensi harus diminum terus menerus/ seumur hidup?_ → `QuestionnaireResponse.item.item.linkId` (287, tanpa BQ)<br>_Apa nama obat hipertensi yang diterima oleh responden?_ → `QuestionnaireResponse.item.item.linkId` (291, tanpa BQ)<br>_B24. Apakah [NAMA] pernah didiagnosis menderita stroke oleh dokter?_ → `QuestionnaireResponse.item.item.linkId` (296, tanpa BQ)<br>_B25. Umur berapa [NAMA] pertama kali didiagnosis stroke?_ → `QuestionnaireResponse.item.item.linkId` (300, tanpa BQ)<br>_B26. Apakah [NAMA] memeriksakan ulang (kontrol) penyakit stroke yang dialami ke fasilitas pelayanan kesehatan?_ → `QuestionnaireResponse.item.item.linkId` (304, tanpa BQ)<br>_B27. Apakah [NAMA] pernah didiagnosis oleh dokter, menderita penyakit ginjal kronis (minimal ginjal sakit selama 3 bulan berturut-turut)?_ → `QuestionnaireResponse.item.item.linkId` (311, tanpa BQ)<br>_B28. Umur berapa [NAMA] pertama kali didiagnosis penyakit ginjal kronis?_ → `QuestionnaireResponse.item.item.linkId` (315, tanpa BQ)<br>_B29. Apakah [NAMA] pernah/ sedang menjalani cuci darah (haemodialisa)?_ → `QuestionnaireResponse.item.item.linkId` (319, tanpa BQ) |
| 6 | 114–124 | Condition | 472970003.0 | History of diabetes mellitus type 1 | _Nama ART_ → `Condition.subject.display` (117, tanpa BQ)<br>_Completion time_ → `Condition.recordedDate` (119, tanpa BQ)<br>_ID Sahabat Sehat (3 angka terakhir)_ → `Condition.recorder.reference` (120, tanpa BQ)<br>_B07b. Tipe atau jenis diabetes mellitus (DM)/ kencing manis yang diderita oleh [NAMA]?_ → `Condition.code.coding` (121, tanpa BQ) |
| 7 | 136–147 | MedicationStatement | – | – | _B09. Jenis pengobatan apa yang diperoleh [NAMA]?_ → `MedicationStatement.category.coding` (136, tanpa BQ)<br>_Nama ART_ → `MedicationStatement.subject.display` (139, tanpa BQ)<br>_Completion time_ → `MedicationStatement.dateAsserted` (140, tanpa BQ)<br>_Nama ART_ → `MedicationStatement.informationSource.display` (142, tanpa BQ) |
| 8 | 148–155 | Procedure | 308755006.0 | Subcutaneous injection of insulin | _Nama ART_ → `Procedure.subject.display` (152, tanpa BQ)<br>_ID Sahabat Sehat (3 angka terakhir)_ → `Procedure.recorder.reference` (154, tanpa BQ) |
| 9 | 189–199 | Condition | 249472009.0 | Always hungry | _Nama ART_ → `Condition.subject.display` (192, tanpa BQ)<br>_Completion time_ → `Condition.recordedDate` (194, tanpa BQ)<br>_ID Sahabat Sehat (3 angka terakhir)_ → `Condition.recorder.reference` (195, tanpa BQ)<br>_B15. Apakah [NAMA] dalam 1 bulan terakhir mengalami gejala:_ → `Condition.code.coding` (196, tanpa BQ) |
| 10 | 204–214 | Procedure | 271061004.0 | Random blood glucose measurement | _Pemeriksaan apa yang terakhir kali responden lakukan dalam mengontrol diabetes mellitus (DM)/kencing manis?_ → `Procedure.status` (204, tanpa BQ)<br>_Nama ART_ → `Procedure.subject.display` (211, tanpa BQ)<br>_ID Sahabat Sehat (3 angka terakhir)_ → `Procedure.recorder.reference` (213, tanpa BQ) |
| 11 | 225–235 | Observation | 4548-4 | Hemoglobin A1c/Hemoglobin.total in Blood | _Berapa nilai HbA1c terakhir responden?_ → `Observation.valueQuantity.value` (227, tanpa BQ)<br>_Nama ART_ → `Observation.subject.display` (230, tanpa BQ)<br>_Completion time_ → `Observation.issued` (233, tanpa BQ)<br>_ID Sahabat Sehat (3 angka terakhir)_ → `Observation.performer.reference` (234, tanpa BQ) |
| 12 | 322–332 | Procedure | 302497006.0 | Hemodialysis | _B29. Apakah [NAMA] pernah/ sedang menjalani cuci darah (haemodialisa)?_ → `Procedure.category.coding` (322, tanpa BQ)<br>_Nama ART_ → `Procedure.subject.display` (327, tanpa BQ)<br>_ID Sahabat Sehat (3 angka terakhir)_ → `Procedure.recorder.reference` (331, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Condition | 3 |
| Procedure | 3 |
| Patient | 1 |
| Practitioner | 1 |
| Encounter | 1 |
| QuestionnaireResponse | 1 |
| MedicationStatement | 1 |
| Observation | 1 |
| **Total** | **12** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 78 | Condition | `Condition.code.coding` | 312851005.0 | Screening for disorder | http://snomed.info/sct |
| 2 | 121 | Condition | `Condition.code.coding` | 472970003.0 | History of diabetes mellitus type 1 | http://snomed.info/sct |
| 3 | 122 | Condition | `Condition.code.coding` | 472969004.0 | History of diabetes mellitus type 2 | http://snomed.info/sct |
| 4 | 123 | Condition | `Condition.code.coding` | 472971004.0 | History of gestational diabetes mellitus | http://snomed.info/sct |
| 5 | 124 | Condition | `Condition.code.coding` | 161445009.0 | H/O: diabetes mellitus | http://snomed.info/sct |
| 6 | 149 | Procedure | `Procedure.code.coding` | 308755006.0 | Subcutaneous injection of insulin | http://snomed.info/sct |
| 7 | 166 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000852 | Merasa Sudah Sehat | http://terminology.kemkes.go.id/sp |
| 8 | 167 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000853 | Obat Tidak Tersedia di Fasilitas Pelayanan Kesehatan | http://terminology.kemkes.go.id/sp |
| 9 | 168 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 182897004.0 | Drug declined by patient - side effects | http://snomed.info/sct |
| 10 | 169 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000854 | Memilih Minum Obat Tradisional | http://terminology.kemkes.go.id/sp |
| 11 | 170 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000855 | Bosan/ Malas/ Sering Lupa | http://terminology.kemkes.go.id/sp |
| 12 | 173 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000849 | Selalu rutin sesuai waktu yang ditentukan | http://terminology.kemkes.go.id/sp |
| 13 | 174 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000850 | Rutin, namun terlambat/bolos sekali atau dua kali | http://terminology.kemkes.go.id/sp |
| 14 | 175 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000363 | Kadang-Kadang | http://terminology.kemkes.go.id/sp |
| 15 | 176 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000851 | Jarang | http://terminology.kemkes.go.id/sp |
| 16 | 183 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer[x].valueCoding` | 410175003.0 | Dietary regime management | http://snomed.info/sct |
| 17 | 184 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer[x].valueCoding` | 256235009.0 | Exercise | http://snomed.info/sct |
| 18 | 185 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer[x].valueCoding` | 414392008.0 | Herbal therapy | http://snomed.info/sct |
| 19 | 196 | Condition | `Condition.code.coding` | 249472009.0 | Always hungry | http://snomed.info/sct |
| 20 | 197 | Condition | `Condition.code.coding` | 17173007.0 | Excessive thirst | http://snomed.info/sct |
| 21 | 198 | Condition | `Condition.code.coding` | 28442001.0 | Polyuria | http://snomed.info/sct |
| 22 | 199 | Condition | `Condition.code.coding` | 309257005.0 | Excessive weight loss | http://snomed.info/sct |
| 23 | 200 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000856 | Tidak Mengalami Gejala Apapun | http://terminology.kemkes.go.id/sp |
| 24 | 206 | Procedure | `Procedure.code.coding` | 271061004.0 | Random blood glucose measurement | http://snomed.info/sct |
| 25 | 207 | Procedure | `Procedure.code.coding` | 271062006.0 | Fasting blood glucose measurement | http://snomed.info/sct |
| 26 | 208 | Procedure | `Procedure.code.coding` | 88856000.0 | Glucose measurement, 2 hour post prandial | http://snomed.info/sct |
| 27 | 209 | Procedure | `Procedure.code.coding` | 43396009.0 | Hemoglobin A1c measurement | http://snomed.info/sct |
| 28 | 217 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 89185003.0 | Monthly | http://snomed.info/sct |
| 29 | 218 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 3015006.0 | Trimonthly | http://snomed.info/sct |
| 30 | 219 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 396149002.0 | Every six months | http://snomed.info/sct |
| 31 | 220 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000857 | Hanya Sekali di Awal | http://terminology.kemkes.go.id/sp |
| 32 | 221 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000858 | Tidak Pernah Sama Sekali | http://terminology.kemkes.go.id/sp |
| 33 | 226 | Observation | `Observation.code.coding` | 4548-4 | Hemoglobin A1c/Hemoglobin.total in Blood | http://loinc.org |
| 34 | 262 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000849 | Selalu rutin sesuai waktu yang ditentukan | http://terminology.kemkes.go.id/sp |
| 35 | 263 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000850 | Rutin, namun terlambat/bolos sekali atau dua kali | http://terminology.kemkes.go.id/sp |
| 36 | 264 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000363 | Kadang-Kadang | http://terminology.kemkes.go.id/sp |
| 37 | 265 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000851 | Jarang | http://terminology.kemkes.go.id/sp |
| 38 | 268 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer[x].valueCoding` | 394778007.0 | Client's or patient's home | http://snomed.info/sct |
| 39 | 269 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer[x].valueCoding` | SP000859 | Posyandu/ Posbindu | http://terminology.kemkes.go.id/sp |
| 40 | 270 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer[x].valueCoding` | 102.0 | Pusat Kesehatan Masyarakat | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 41 | 271 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer[x].valueCoding` | 104.0 | Rumah Sakit | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 42 | 272 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer[x].valueCoding` | 101.0 | Tempat Praktik Mandiri Tenaga Kesehatan | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 43 | 275 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000862 | Ya, Teratur | http://terminology.kemkes.go.id/sp |
| 44 | 276 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000863 | Ya Tidak Teratur | http://terminology.kemkes.go.id/sp |
| 45 | 277 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 715036001.0 | Does not take medication | http://snomed.info/sct |
| 46 | 280 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000852 | Merasa Sudah Sehat | http://terminology.kemkes.go.id/sp |
| 47 | 281 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000853 | Obat Tidak Tersedia di Fasilitas Pelayanan Kesehatan | http://terminology.kemkes.go.id/sp |
| 48 | 282 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 182897004.0 | Drug declined by patient - side effects | http://snomed.info/sct |
| 49 | 283 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000854 | Memilih Minum Obat Tradisional | http://terminology.kemkes.go.id/sp |
| 50 | 284 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000855 | Bosan/ Malas/ Sering Lupa | http://terminology.kemkes.go.id/sp |
| 51 | 285 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000860 | Obat Hipertensi Hanya Diminum Saat Kehamilan/ Pasca Persalinan | http://terminology.kemkes.go.id/sp |
| 52 | 286 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 74964007.0 | Other | http://snomed.info/sct |
| 53 | 306 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 50811001.0 | Routine | http://snomed.info/sct |
| 54 | 307 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000363 | Kadang-Kadang | http://terminology.kemkes.go.id/sp |
| 55 | 308 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000865 | Tidak Melakukan Pemeriksaan Ulang | http://terminology.kemkes.go.id/sp |
| 56 | 323 | Procedure | `Procedure.code.coding` | 302497006.0 | Hemodialysis | http://hl7.org/fhir/sid/icd-9-cm |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 26 |
| http://terminology.kemkes.go.id/sp | 25 |
| http://terminology.kemkes.go.id/CodeSystem/organization-type | 3 |
| http://loinc.org | 1 |
| http://hl7.org/fhir/sid/icd-9-cm | 1 |
| **Total** | **56** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 2 | – | Id | – | `` |
| 3 | – | Response Id | – | `` |
| 4 | – | Survey Id | – | `` |
| 5 | – | Start time | – | `` |
| 7 | – | Sync time | – | `` |
| 8 | – | Survey submission status | – | `` |
| 10 | – | Completion time | – | `` |
| 11 | – | Email | – | `` |
| 12 | – | Name | – | `` |
| 13 | – | Nama ART | – | `` |
| 14 | – | Nama ART (konfirmasi) | – | `` |
| 15 | – | Tanggal lahir ART | – | `` |
| 16 | – | ID Sahabat Sehat (3 angka terakhir) | – | `` |
| 17 | – | ID rumah (dari DWS) | – | `` |
