# Output Form: ASIK - CKG Lansia (versi 2025)

Sumber: `mapping/phdt-data-dictionary-asik-ckg-lansia-2025.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-asik-ckg-lansia-2025.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 80 |
| Code (`jumlah code` = 1) | 457 |
| Code unik (code + CodeSystem) | 287 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 10 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–27 | Patient | – | – | _pasien_name_ → `Patient.name.text` (2, tanpa BQ)<br>_nik_ → `Patient.identifier.value` (5, tanpa BQ)<br>_pasien_id_ → `Patient.identifier.value` (8, tanpa BQ)<br>_jenis_kelamin_ → `Patient.gender` (10, tanpa BQ)<br>_tgl_lahir_ → `Patient.birthDate` (12, tanpa BQ)<br>_no_handphone_ → `Patient.telecom` (13, tanpa BQ)<br>_status_perkawinan_ → `Patient.maritalStatus.coding` (16, tanpa BQ)<br>_kabkota_name_ → `Patient.address.city` (20, tanpa BQ)<br>_provinsi_ → `Patient.address.extension.extension.valueCode` (24, tanpa BQ)<br>_kabkota_ → `Patient.address.extension.extension.valueCode` (27, tanpa BQ) |
| 2 | 66–79 | Encounter | – | – | _tgl_pelayanan_ → `Encounter.identifier` (66, tanpa BQ) |
| 3 | 80–87 | Condition | Z01.8 | Other specified special examinations | – |
| 4 | 98–109 | Observation | 424144002.0 | Current chronological age | _age_now_ → `Observation.valueQuantity.value` (101, tanpa BQ) |
| 5 | 110–121 | Observation | TK000144 | Rencana menikah 1 tahun ke depan | _rencana_menikah_dalam_kurun_waktu_1_tahun_ → `Observation.valueBoolean` (113, tanpa BQ) |
| 6 | 122–179 | QuestionnaireResponse | – | – | _apakah_merokok_dalam_setahun_terakhir_ → `QuestionnaireResponse.item.item.text` (134, tanpa BQ)<br>_sudah_berapa_tahun_merokok_ → `QuestionnaireResponse.item.item.answer.item.text` (138, tanpa BQ)<br>_berapa_batang_rokok_yang_dihisap_dalam_sehari_ → `QuestionnaireResponse.item.item.answer.item.text` (142, tanpa BQ)<br>_apakah_pernah_merokok_sebelumnya_ → `QuestionnaireResponse.item.item.text` (145, tanpa BQ)<br>_berapa_lama_merokok_sebelumnya_ → `QuestionnaireResponse.item.item.answer.item.text` (149, tanpa BQ)<br>_kapan_anda_berhenti_merokok_ → `QuestionnaireResponse.item.item.answer.item.text` (153, tanpa BQ)<br>_apakah_terpapar_asap_rokok_sebulan_terakhir_ → `QuestionnaireResponse.item.item.text` (157, tanpa BQ)<br>_apakah_rutin_melakukan_olahraga_ → `QuestionnaireResponse.item.item.text` (161, tanpa BQ)<br>_berapa_kali_berolahraga_dalam_seminggu_ → `QuestionnaireResponse.item.item.answer.item.text` (165, tanpa BQ)<br>_berapa_menit_berolahraga_ → `QuestionnaireResponse.item.item.answer.item.text` (168, tanpa BQ)<br>_tingkat_aktivitas_fisik_ → `QuestionnaireResponse.item.item.answer.item.linkId` (170, tanpa BQ)<br>_berat_badan_kg_ → `QuestionnaireResponse.item.item.item.text` (177, tanpa BQ) |
| 7 | 180–191 | Observation | 29463-7 | Body weight | – |
| 8 | 196–207 | Observation | 8302-2 | Body height | – |
| 9 | 212–238 | Observation | 39156-5 | Body mass index (BMI) [Ratio] | – |
| 10 | 243–262 | Observation | vital-signs | Abdominal circumference | – |
| 11 | 271–312 | Observation | 8480-6 | Systolic blood pressure | – |
| 12 | 315–356 | Observation | 8462-4 | Diastolic blood pressure | – |
| 13 | 359–379 | Observation | 268607006.0 | Hypertension risk level | – |
| 14 | 388–397 | ServiceRequest | – | – | – |
| 15 | 398–401 | PractitionerRole | – | – | – |
| 16 | 402–409 | Specimen | – | – | – |
| 17 | 410–435 | Observation | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | – |
| 18 | 436–447 | DiagnosticReport | – | – | – |
| 19 | 450–475 | Observation | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | – |
| 20 | 478–503 | Observation | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | – |
| 21 | 506–533 | Observation | 1521-4 | Glucose [Mass/volume] in Serum or Plasma --2 hours post meal | – |
| 22 | 536–556 | Observation | 4548-4 | Hemoglobin A1c/Hemoglobin.total in Blood | – |
| 23 | 561–598 | Observation | 34534-8 | 12 lead EKG panel | _hasil_detail_pemeriksaan_ekg_ → `Observation.component.code.coding` (575, tanpa BQ) |
| 24 | 604–623 | Observation | 2093-3 | Cholesterol [Mass/volume] in Serum or Plasma | – |
| 25 | 626–645 | Observation | 2085-9 | Cholesterol in HDL [Mass/volume] in Serum or Plasma | – |
| 26 | 648–667 | Observation | 2085-9 | Cholesterol in HDL [Mass/volume] in Serum or Plasma | – |
| 27 | 670–689 | Observation | 2571-8 | Triglyceride [Mass/volume] in Serum or Plasma | – |
| 28 | 692–705 | Observation | 100898-6 | Lipid panel - Serum or Plasma | – |
| 29 | 710–730 | Observation | OC000173 | Prediksi Risiko PTM tanpa Pemeriksaan Laboratorium | – |
| 30 | 735–752 | Observation | 20977-5 | Urea [Mass/volume] in Blood | – |
| 31 | 755–772 | Observation | 2160-0 | Creatinine [Mass/volume] in Serum or Plasma | – |
| 32 | 775–790 | Observation | 62238-1 | Glomerular filtration rate/1.73 sq M.predicted [Volume Rate/Area] in Serum, Plasma or Blood by Creatinine-based formula (CKD-EPI) | – |
| 33 | 832–844 | Observation | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | – |
| 34 | 847–858 | Observation | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | – |
| 35 | 861–872 | Observation | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | – |
| 36 | 875–886 | Observation | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | – |
| 37 | 889–900 | Observation | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | – |
| 38 | 903–915 | Observation | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | – |
| 39 | 918–930 | Observation | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | – |
| 40 | 933–945 | Observation | 89372-7 | Mycobacterium tuberculosis complex rpoB gene rifAMPin resistance mutation [Presence] by Molecular method | – |
| 41 | 948–960 | Observation | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | – |
| 42 | 963–975 | Observation | 89372-7 | Mycobacterium tuberculosis complex rpoB gene rifAMPin resistance mutation [Presence] by Molecular method | – |
| 43 | 978–990 | Observation | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | – |
| 44 | 993–1005 | Observation | 89372-7 | Mycobacterium tuberculosis complex rpoB gene rifAMPin resistance mutation [Presence] by Molecular method | – |
| 45 | 1066–1078 | Observation | 13607009.0 | Manual examination of breast | – |
| 46 | 1083–1095 | Observation | 24601-7 | US Breast | – |
| 47 | 1108–1119 | Observation | 451024007.0 | Inspection of vagina using vaginal speculum | – |
| 48 | 1124–1135 | Observation | X099241 | Tes IVA | – |
| 49 | 1140–1155 | Observation | 44550-2 | Human papilloma virus DNA [Presence] in Cervix by Probe | – |
| 50 | 1252–1263 | Observation | 410007005.0 | Rectal examination | – |
| 51 | 1268–1279 | Observation | 14563-1 | Hemoglobin.gastrointestinal [Presence] in Stool --1st specimen | – |
| 52 | 1288–1299 | Observation | 247301006.0 | Finding of ability to hear whisper | – |
| 53 | 1304–1315 | Observation | 76517002.0 | Otoscopy | – |
| 54 | 1327–1342 | Observation | 400911007.0 | Tumbling E test | _pemeriksaan_visus_e_tumbling_ → `Observation.valueCodeableConcept.coding` (1331, tanpa BQ) |
| 55 | 1343–1358 | Observation | 252973004.0 | Snellen chart assessment | _pemeriksaan_visus_snellen_chart_ → `Observation.valueCodeableConcept.coding` (1347, tanpa BQ) |
| 56 | 1362–1377 | Observation | 441841000.0 | Pinhole visual acuity test | – |
| 57 | 1381–1394 | Observation | 40137007.0 | Pupil light reflex | – |
| 58 | 1470–1483 | Observation | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | – |
| 59 | 1486–1498 | Observation | 72376-7 | Hepatitis C virus Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | – |
| 60 | 1522–1535 | Observation | 1920-8 | Aspartate aminotransferase [Enzymatic activity/volume] in Serum or Plasma | – |
| 61 | 1539–1551 | Observation | – | – | – |
| 62 | 1555–1576 | Observation | – | – | – |
| 63 | 1577–1588 | Observation | TK000144 | Rencana menikah 1 tahun ke depan | _rencana_menikah_dalam_kurun_waktu_1_tahun_ → `Observation.valueBoolean` (1580, tanpa BQ) |
| 64 | 1602–1617 | Observation | 30352-9 | Hemoglobin [Mass/volume] in Capillary blood | – |
| 65 | 1627–1638 | Observation | 22464-2 | Reagin Ab [Presence] in Specimen | – |
| 66 | 1648–1659 | Observation | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | – |
| 67 | 1660–1725 | QuestionnaireResponse | – | – | _apakah_dapat_mengingat_tiga_kata_ → `QuestionnaireResponse.item.item.text` (1672, tanpa BQ)<br>_tanggal_berapa_hari_ini_dimana_saat_ini_ → `QuestionnaireResponse.item.item.text` (1676, tanpa BQ)<br>_apakah_dapat_mengingat_tiga_kata_sebelumnya_ → `QuestionnaireResponse.item.item.text` (1681, tanpa BQ)<br>_hasil_interpretasi_skilas_penurunan_kognitif_ → `QuestionnaireResponse.item.item.text` (1686, tanpa BQ)<br>_apakah_dapat_berdiri_dari_kursi_skilas_ → `QuestionnaireResponse.item.item.text` (1691, tanpa BQ)<br>_apakah_berat_badan_berkurang_ → `QuestionnaireResponse.item.item.text` (1697, tanpa BQ)<br>_apakah_nafsu_makan_hilang_ → `QuestionnaireResponse.item.item.text` (1701, tanpa BQ)<br>_apakah_lila_kurang_dari_21_cm_ → `QuestionnaireResponse.item.item.text` (1705, tanpa BQ)<br>_hasil_interpretasi_skilas_malnutrisi_ → `QuestionnaireResponse.item.item.text` (1709, tanpa BQ)<br>_apakah_merasa_sedih_dalam_2_minggu_terakhir_ → `QuestionnaireResponse.item.item.text` (1715, tanpa BQ)<br>_apakah_minat_berkurang_dalam_berkegiatan_dalam_2_minggu_terakhir_ → `QuestionnaireResponse.item.item.text` (1719, tanpa BQ)<br>_hasil_interpretasi_gejala_depresi_ → `QuestionnaireResponse.item.item.text` (1723, tanpa BQ) |
| 68 | 1726–1758 | Observation | 48542-5 | Geriatric depression scale (GDS) panel | _hasil_interpretasi_gejala_depresi_1_ → `Observation.valueQuantity.value` (1730, tanpa BQ)<br>_apakah_merasa_puas_dengan_kehidupan_ → `Observation.component.code.coding` (1747, tanpa BQ)<br>_apakah_sering_merasa_bosan_ → `Observation.component.code.coding` (1750, tanpa BQ)<br>_apakah_sering_merasa_tidak_berdaya_ → `Observation.component.code.coding` (1753, tanpa BQ)<br>_apakah_merasa_tidak_berharga_ → `Observation.component.code.coding` (1756, tanpa BQ) |
| 69 | 1759–1831 | Observation | 96762-0 | Barthel index panel | _hasil_intrepretasi_adl_ → `Observation.valueRange.low.value` (1763, tanpa BQ)<br>_apakah_dapat_mengendalikan_rangsang_bab_ → `Observation.component.code.coding` (1792, tanpa BQ)<br>_apakah_dapat_mengendalikan_rangsang_bak_ → `Observation.component.code.coding` (1796, tanpa BQ)<br>_apakah_dapat_membersihkan_diri_sendiri_ → `Observation.component.code.coding` (1800, tanpa BQ)<br>_apakah_dapat_menggunakan_jamban_sendiri_ → `Observation.component.code.coding` (1803, tanpa BQ)<br>_apakah_dapat_makan_sendiri_ → `Observation.component.code.coding` (1807, tanpa BQ)<br>_apakah_dapat_merubah_sikap_dari_berbaring_ke_duduk_sendiri_ → `Observation.component.code.coding` (1811, tanpa BQ)<br>_apakah_dapat_berjalan_sendiri_ → `Observation.component.code.coding` (1816, tanpa BQ)<br>_apakah_dapat_berpakaian_sendiri_ → `Observation.component.code.coding` (1821, tanpa BQ)<br>_apakah_dapat_turun_naik_tangga_sendiri_ → `Observation.component.code.coding` (1825, tanpa BQ)<br>_apakah_dapat_mandi_sendiri_ → `Observation.component.code.coding` (1829, tanpa BQ) |
| 70 | 1832–1846 | Observation | 72234-8 | Mini-Cog | _hasil_mengingat_3_versi_kata_ → `Observation.valueCodeableConcept.coding` (1835, tanpa BQ)<br>_sudah_mendengarkan_dan_mengingat_3_versi_kata_ → `Observation.note` (1846, tanpa BQ) |
| 71 | 1847–1863 | Observation | 79150-9 | Clock drawing panel [GPCOG] | _apakah_dapat_menggambar_sesuai_perintah_ → `Observation.component.valueBoolean` (1852, tanpa BQ) |
| 72 | 1864–1877 | Observation | 72233-0 | Total score [Mini-Cog] | _hasil_interpretasi_mini_cog_ → `Observation.valueQuantity` (1868, tanpa BQ) |
| 73 | 1878–1929 | QuestionnaireResponse | – | – | _apakah_sulit_membuat_keputusan_ → `QuestionnaireResponse.questionnaire` (1878, tanpa BQ)<br>_apakah_sudah_tidak_menekuni_hobi_ → `QuestionnaireResponse.item.linkId` (1892, tanpa BQ)<br>_apakah_keluar_mengulang_pertanyaan_cerita_pernyataan_yang_sama_ → `QuestionnaireResponse.item.linkId` (1897, tanpa BQ)<br>_apakah_kesulitan_belajar_menggunakan_perkakas_dan_peralatan_ → `QuestionnaireResponse.item.linkId` (1902, tanpa BQ)<br>_apakah_lupa_nama_bulan_atau_tahun_ → `QuestionnaireResponse.item.linkId` (1907, tanpa BQ)<br>_apakah_kesulitan_mengatur_keuangan_ → `QuestionnaireResponse.item.linkId` (1912, tanpa BQ)<br>_apakah_sulit_mengingat_janji_ → `QuestionnaireResponse.item.linkId` (1917, tanpa BQ)<br>_apakah_mengalami_gangguan_memori_dan_pemikiran_yang_konsisten_ → `QuestionnaireResponse.item.linkId` (1922, tanpa BQ)<br>_hasil_interpretasi_ad_8_ → `QuestionnaireResponse.item.linkId` (1927, tanpa BQ) |
| 74 | 1930–1942 | Observation | 71722-3 | Total score [AD8] | – |
| 75 | 1943–1966 | Observation | 66248-6 | Balance test [PhenX] | _tes_keseimbangan_berdiri_berdampingan_ → `Observation.component.code.coding` (1946, tanpa BQ)<br>_tes_keseimbangan_berdiri_semi_tandem_ → `Observation.component.code.coding` (1950, tanpa BQ)<br>_tes_keseimbangan_berdiri_tandem_ → `Observation.component.code.coding` (1954, tanpa BQ) |
| 76 | 1967–1992 | Observation | 714283000.0 | Short Physical Performance Battery | _tes_kecepatan_berjalan_ → `Observation.component.code.coding` (1971, tanpa BQ)<br>_tes_berdiri_dari_kursi_ → `Observation.component.code.coding` (1977, tanpa BQ)<br>_hasil_interpretasi_spbb_ → `Observation.valueQuantity` (1983, tanpa BQ) |
| 77 | 1993–2037 | QuestionnaireResponse | – | – | _apakah_asupan_makan_turun_dalam_3_bulan_terakhir_ → `QuestionnaireResponse.item.text` (2003, tanpa BQ)<br>_apakah_berat_badan_turun_dalam_3_bulan_terakhir_ → `QuestionnaireResponse.item.item.linkId` (2009, tanpa BQ)<br>_kemampuan_melakukan_mobilitas_ → `QuestionnaireResponse.item.item.linkId` (2015, tanpa BQ)<br>_apakah_menderita_stress_atau_penyakit_akut_dalam_3_bulan_terakhir_ → `QuestionnaireResponse.item.item.linkId` (2020, tanpa BQ)<br>_apakah_mengalami_masalah_neuropsikologis_ → `QuestionnaireResponse.item.item.linkId` (2024, tanpa BQ)<br>_nilai_imt_ → `QuestionnaireResponse.item.item.linkId` (2029, tanpa BQ) |
| 78 | 2038–2050 | Observation | 39156-5 | Body mass index (BMI) [Ratio] | – |
| 79 | 2058–2070 | Observation | 8283-4 | Calf - right Maximum circumference | – |
| 80 | 2074–2088 | Observation | TK000195 | Mini Nutritional Assessment (MNA) SF | – |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 69 |
| QuestionnaireResponse | 4 |
| Patient | 1 |
| Encounter | 1 |
| Condition | 1 |
| ServiceRequest | 1 |
| PractitionerRole | 1 |
| Specimen | 1 |
| DiagnosticReport | 1 |
| **Total** | **80** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 82 | Condition | `Condition.code.coding` | Z01.8 | Other specified special examinations | http://hl7.org/fhir/sid/icd-10 |
| 2 | 100 | Observation | `Observation.code.coding` | 424144002.0 | Current chronological age | http://snomed.info/sct |
| 3 | 112 | Observation | `Observation.code.coding` | TK000144 | Rencana menikah 1 tahun ke depan | http://terminology.kemkes.go.id |
| 4 | 154 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | TK000145 | 1 tahun yang lalu | http://terminology.kemkes.go.id |
| 5 | 155 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | TK000146 | Lebih dari 1 tahun yang lalu | http://terminology.kemkes.go.id |
| 6 | 172 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 424805008.0 | Exercise above recommended level | http://snomed.info/sct |
| 7 | 173 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 413300002.0 | Exercise below recommended level | http://snomed.info/sct |
| 8 | 182 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 9 | 198 | Observation | `Observation.code.coding` | 8302-2 | Body height | http://loinc.org |
| 10 | 214 | Observation | `Observation.code.coding` | 39156-5 | Body mass index (BMI) [Ratio] | http://loinc.org |
| 11 | 215 | Observation | `Observation.interpretation.coding` | 248342006.0 | Underweight | http://snomed.info/sct |
| 12 | 218 | Observation | `Observation.interpretation.coding` | 43664005.0 | Normal weight | http://snomed.info/sct |
| 13 | 223 | Observation | `Observation.interpretation.coding` | 238131007.0 | Overweight | http://snomed.info/sct |
| 14 | 228 | Observation | `Observation.interpretation.coding` | 414915002.0 | Obese | http://snomed.info/sct |
| 15 | 245 | Observation | `Observation.code.coding` | vital-signs | Abdominal circumference | http://snomed.info/sct |
| 16 | 255 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 17 | 259 | Observation | `Observation.interpretation.coding` | 248311001.0 | Central obesity | http://snomed.info/sct |
| 18 | 273 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 19 | 283 | Observation | `Observation.interpretation.coding` | OI000040 | Tekanan Darah Optimal | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 20 | 288 | Observation | `Observation.interpretation.coding` | 2004005.0 | Normal blood pressure | http://snomed.info/sct |
| 21 | 293 | Observation | `Observation.interpretation.coding` | OI000041 | Tekanan Darah Normal Tinggi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 22 | 298 | Observation | `Observation.interpretation.coding` | 827069000.0 | Stage 1 hypertension | http://snomed.info/sct |
| 23 | 303 | Observation | `Observation.interpretation.coding` | 827068008.0 | Stage 1 hypertension | http://snomed.info/sct |
| 24 | 308 | Observation | `Observation.interpretation.coding` | OI000042 | Hipertensi Derajat 3 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 25 | 317 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://snomed.info/sct |
| 26 | 327 | Observation | `Observation.interpretation.coding` | OI000040 | Tekanan Darah Optimal | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 27 | 332 | Observation | `Observation.interpretation.coding` | 2004005.0 | Normal blood pressure | http://snomed.info/sct |
| 28 | 337 | Observation | `Observation.interpretation.coding` | OI000041 | Tekanan Darah Normal Tinggi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 29 | 342 | Observation | `Observation.interpretation.coding` | 827069000.0 | Stage 1 hypertension | http://snomed.info/sct |
| 30 | 347 | Observation | `Observation.interpretation.coding` | 827068008.0 | Stage 1 hypertension | http://snomed.info/sct |
| 31 | 352 | Observation | `Observation.interpretation.coding` | OI000042 | Hipertensi Derajat 3 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 32 | 361 | Observation | `Observation.code.coding` | 268607006.0 | Hypertension risk level | http://snomed.info/sct |
| 33 | 373 | Observation | `Observation.interpretation.coding` | OI000040 | Tekanan Darah Optimal | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 34 | 374 | Observation | `Observation.interpretation.coding` | 2004005.0 | Normal blood pressure | http://snomed.info/sct |
| 35 | 375 | Observation | `Observation.interpretation.coding` | OI000041 | Tekanan Darah Normal Tinggi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 36 | 376 | Observation | `Observation.interpretation.coding` | 827069000.0 | Stage 1 hypertension | http://snomed.info/sct |
| 37 | 377 | Observation | `Observation.interpretation.coding` | 827068008.0 | Stage 2 hypertension | http://snomed.info/sct |
| 38 | 378 | Observation | `Observation.interpretation.coding` | OI000042 | Hipertensi Derajat 3 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 39 | 379 | Observation | `Observation.interpretation.coding` | 56218007.0 | Systolic hypertension | http://snomed.info/sct |
| 40 | 392 | ServiceRequest | `ServiceRequest.code` | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 41 | 400 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002.0 | Laboratory worker | http://snomed.info/sct |
| 42 | 403 | Specimen | `Specimen.type` | 119297000.0 | Blood specimen | http://snomed.info/sct |
| 43 | 412 | Observation | `Observation.code.coding` | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 44 | 420 | Observation | `Observation.interpretation.coding` | 302866003.0 | Hypoglycemia | http://snomed.info/sct |
| 45 | 423 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 46 | 428 | Observation | `Observation.interpretation.coding` | 714628002.0 | Prediabetes | http://snomed.info/sct |
| 47 | 433 | Observation | `Observation.interpretation.coding` | 80394007.0 | Hyperglycemia | http://snomed.info/sct |
| 48 | 438 | DiagnosticReport | `DiagnosticReport.code` | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 49 | 452 | Observation | `Observation.code.coding` | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 50 | 460 | Observation | `Observation.interpretation.coding` | 302866003.0 | Hypoglycemia | http://snomed.info/sct |
| 51 | 463 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 52 | 468 | Observation | `Observation.interpretation.coding` | 714628002.0 | Prediabetes | http://snomed.info/sct |
| 53 | 473 | Observation | `Observation.interpretation.coding` | 73211009.0 | Diabetes mellitus | http://snomed.info/sct |
| 54 | 480 | Observation | `Observation.code.coding` | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 55 | 488 | Observation | `Observation.interpretation.coding` | 302866003.0 | Hypoglycemia | http://snomed.info/sct |
| 56 | 491 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 57 | 496 | Observation | `Observation.interpretation.coding` | 714628002.0 | Prediabetes | http://snomed.info/sct |
| 58 | 501 | Observation | `Observation.interpretation.coding` | 73211009.0 | Diabetes mellitus | http://snomed.info/sct |
| 59 | 508 | Observation | `Observation.code.coding` | 1521-4 | Glucose [Mass/volume] in Serum or Plasma --2 hours post meal | http://loinc.org |
| 60 | 518 | Observation | `Observation.interpretation.coding` | 302866003.0 | Hypoglycemia | http://snomed.info/sct |
| 61 | 521 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 62 | 526 | Observation | `Observation.interpretation.coding` | 714628002.0 | Prediabetes | http://snomed.info/sct |
| 63 | 531 | Observation | `Observation.interpretation.coding` | 73211009.0 | Diabetes mellitus | http://snomed.info/sct |
| 64 | 538 | Observation | `Observation.code.coding` | 4548-4 | Hemoglobin A1c/Hemoglobin.total in Blood | http://loinc.org |
| 65 | 546 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 66 | 549 | Observation | `Observation.interpretation.coding` | 714628002.0 | Prediabetes | http://snomed.info/sct |
| 67 | 554 | Observation | `Observation.interpretation.coding` | 73211009.0 | Diabetes mellitus | http://snomed.info/sct |
| 68 | 563 | Observation | `Observation.code.coding` | 34534-8 | 12 lead EKG panel | http://loinc.org |
| 69 | 564 | Observation | `Observation.valueCodeableConcept.coding` | 17621005.0 | Normal | http://snomed.info/sct |
| 70 | 565 | Observation | `Observation.interpretation.coding` | 164854000 | Electrocardiogram normal | http://snomed.info/sct |
| 71 | 566 | Observation | `Observation.valueCodeableConcept.coding` | 263654008 | Abnormal | http://snomed.info/sct |
| 72 | 567 | Observation | `Observation.interpretation.coding` | 102594003.0 | Electrocardiogram abnormal | http://snomed.info/sct |
| 73 | 575 | Observation | `Observation.component.code.coding` | 164854000 | Electrocardiogram normal | http://snomed.info/sct |
| 74 | 578 | Observation | `Observation.component.code.coding` | 26141007 | ST segment depression | http://snomed.info/sct |
| 75 | 581 | Observation | `Observation.component.code.coding` | 59931005 | Electrocardiogram normal | http://snomed.info/sct |
| 76 | 584 | Observation | `Observation.component.code.coding` | 164873001 | Electrocardiographic left ventricle hypertrophy | http://snomed.info/sct |
| 77 | 587 | Observation | `Observation.component.code.coding` | 164889003 | Electrocardiographic atrial fibrillation | http://snomed.info/sct |
| 78 | 590 | Observation | `Observation.component.code.coding` | 164918000 | Pathological Q wave | http://snomed.info/sct |
| 79 | 593 | Observation | `Observation.component.code.coding` | 76388001 | ST segment elevation | http://snomed.info/sct |
| 80 | 596 | Observation | `Observation.component.code.coding` | 102594003.0 | Electrocardiogram abnormal | http://snomed.info/sct |
| 81 | 606 | Observation | `Observation.code.coding` | 2093-3 | Cholesterol [Mass/volume] in Serum or Plasma | http://loinc.org |
| 82 | 616 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 83 | 620 | Observation | `Observation.interpretation.coding` | H | High | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 84 | 628 | Observation | `Observation.code.coding` | 2085-9 | Cholesterol in HDL [Mass/volume] in Serum or Plasma | http://loinc.org |
| 85 | 631 | Observation | `Observation.interpretation.coding` | L | Low | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 86 | 635 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 87 | 650 | Observation | `Observation.code.coding` | 2085-9 | Cholesterol in HDL [Mass/volume] in Serum or Plasma | http://loinc.org |
| 88 | 653 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 89 | 657 | Observation | `Observation.interpretation.coding` | H | High | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 90 | 672 | Observation | `Observation.code.coding` | 2571-8 | Triglyceride [Mass/volume] in Serum or Plasma | http://loinc.org |
| 91 | 675 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 92 | 679 | Observation | `Observation.interpretation.coding` | H | High | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 93 | 694 | Observation | `Observation.code.coding` | 100898-6 | Lipid panel - Serum or Plasma | http://loinc.org |
| 94 | 695 | Observation | `Observation.valueCodeableConcept.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 95 | 696 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 96 | 697 | Observation | `Observation.valueCodeableConcept.coding` | 370992007.0 | Dyslipidemia | http://snomed.info/sct |
| 97 | 698 | Observation | `Observation.interpretation.coding` | 370992007.0 | Dyslipidemia | http://snomed.info/sct |
| 98 | 712 | Observation | `Observation.code.coding` | OC000173 | Prediksi Risiko PTM tanpa Pemeriksaan Laboratorium | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 99 | 713 | Observation | `Observation.interpretation.coding` | 723505004.0 | Low risk | http://snomed.info/sct |
| 100 | 716 | Observation | `Observation.interpretation.coding` | 25594002.0 | Moderate risk of | http://snomed.info/sct |
| 101 | 721 | Observation | `Observation.interpretation.coding` | 723509005.0 | High risk | http://snomed.info/sct |
| 102 | 737 | Observation | `Observation.code.coding` | 20977-5 | Urea [Mass/volume] in Blood | http://loinc.org |
| 103 | 738 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 104 | 743 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 105 | 757 | Observation | `Observation.code.coding` | 2160-0 | Creatinine [Mass/volume] in Serum or Plasma | http://loinc.org |
| 106 | 758 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 107 | 763 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 108 | 777 | Observation | `Observation.code.coding` | 62238-1 | Glomerular filtration rate/1.73 sq M.predicted [Volume Rate/Area] in Serum, Plasma or Blood by Creatinine-based formula (CKD-EPI) | http://loinc.org |
| 109 | 778 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 110 | 781 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 111 | 834 | Observation | `Observation.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 112 | 835 | Observation | `Observation.method.coding` | 391483001.0 | Microscopy (acid fast bacilli) | http://snomed.info/sct |
| 113 | 836 | Observation | `Observation.valueCodeableConcept.coding` | 10828004.0 | Positive | http://snomed.info/sct |
| 114 | 837 | Observation | `Observation.valueCodeableConcept.coding` | 260385009.0 | Negative | http://snomed.info/sct |
| 115 | 849 | Observation | `Observation.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 116 | 850 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 117 | 851 | Observation | `Observation.dataAbsentReason.coding` | OD000001 | Tidak ada hasil | http://terminology.kemkes.go.id/CodeSystem/data-absent-reason |
| 118 | 863 | Observation | `Observation.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 119 | 864 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 120 | 865 | Observation | `Observation.dataAbsentReason.coding` | LA15841-2 | Invalid | http://loinc.org |
| 121 | 877 | Observation | `Observation.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 122 | 878 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 123 | 879 | Observation | `Observation.dataAbsentReason.coding` | error | Error | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 124 | 891 | Observation | `Observation.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 125 | 892 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 126 | 893 | Observation | `Observation.dataAbsentReason.coding` | OD000001 | Tidak ada hasil | http://terminology.kemkes.go.id/CodeSystem/data-absent-reason |
| 127 | 905 | Observation | `Observation.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 128 | 906 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 129 | 907 | Observation | `Observation.valueCodeableConcept.coding` | LA11883-8 | Not Detected | http://loinc.org |
| 130 | 908 | Observation | `Observation.interpretation.coding` | NEG | Negative | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 131 | 920 | Observation | `Observation.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 132 | 921 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 133 | 922 | Observation | `Observation.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 134 | 923 | Observation | `Observation.interpretation.coding` | NEG | Negative | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 135 | 935 | Observation | `Observation.code.coding` | 89372-7 | Mycobacterium tuberculosis complex rpoB gene rifAMPin resistance mutation [Presence] by Molecular method | http://loinc.org |
| 136 | 936 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 137 | 937 | Observation | `Observation.valueCodeableConcept.coding` | LA11883-8 | Not Detected | http://loinc.org |
| 138 | 938 | Observation | `Observation.interpretation.coding` | X099770 | Rifampisin sensitive | http://terminology.kemkes.go.id/CodeSystem/examination |
| 139 | 950 | Observation | `Observation.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 140 | 951 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 141 | 952 | Observation | `Observation.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 142 | 953 | Observation | `Observation.interpretation.coding` | NEG | Negative | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 143 | 965 | Observation | `Observation.code.coding` | 89372-7 | Mycobacterium tuberculosis complex rpoB gene rifAMPin resistance mutation [Presence] by Molecular method | http://loinc.org |
| 144 | 966 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 145 | 967 | Observation | `Observation.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 146 | 968 | Observation | `Observation.interpretation.coding` | X099771 | Rifampisin resistan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 147 | 980 | Observation | `Observation.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 148 | 981 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 149 | 982 | Observation | `Observation.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 150 | 983 | Observation | `Observation.interpretation.coding` | NEG | Negative | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 151 | 995 | Observation | `Observation.code.coding` | 89372-7 | Mycobacterium tuberculosis complex rpoB gene rifAMPin resistance mutation [Presence] by Molecular method | http://loinc.org |
| 152 | 996 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 153 | 997 | Observation | `Observation.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 154 | 998 | Observation | `Observation.interpretation.coding` | X099772 | Rifampisin indeterminate | http://terminology.kemkes.go.id/CodeSystem/examination |
| 155 | 1010 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | female | Female | http://hl7.org/fhir/administrative-gender |
| 156 | 1011 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | male | Male | http://hl7.org/fhir/administrative-gender |
| 157 | 1023 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | SP000435 | <20 bungkus per tahun | http://terminology.kemkes.go.id/sp |
| 158 | 1024 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | SP000436 | 20-30 bungkus per tahun | http://terminology.kemkes.go.id/sp |
| 159 | 1025 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | SP000437 | >30 bungkus per tahun | http://terminology.kemkes.go.id/sp |
| 160 | 1044 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | 723505004.0 | Low risk | http://snomed.info/sct |
| 161 | 1045 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | 723509005.0 | High risk | http://snomed.info/sct |
| 162 | 1068 | Observation | `Observation.code.coding` | 13607009.0 | Manual examination of breast | http://snomed.info/sct |
| 163 | 1076 | Observation | `Observation.valueCodeableConcept.coding` | 290084006.0 | Breast normal | http://snomed.info/sct |
| 164 | 1077 | Observation | `Observation.valueCodeableConcept.coding` | 89164003.0 | Breast lump | http://snomed.info/sct |
| 165 | 1078 | Observation | `Observation.valueCodeableConcept.coding` | 134405005.0 | Suspected breast cancer | http://snomed.info/sct |
| 166 | 1085 | Observation | `Observation.code.coding` | 24601-7 | US Breast | http://loinc.org |
| 167 | 1093 | Observation | `Observation.valueCodeableConcept.coding` | 290084006.0 | Breast normal | http://snomed.info/sct |
| 168 | 1094 | Observation | `Observation.valueCodeableConcept.coding` | 367644007.0 | Simple cyst | http://snomed.info/sct |
| 169 | 1095 | Observation | `Observation.valueCodeableConcept.coding` | 449837001.0 | Complex cyst of breast | http://snomed.info/sct |
| 170 | 1110 | Observation | `Observation.code.coding` | 451024007.0 | Inspection of vagina using vaginal speculum | http://snomed.info/sct |
| 171 | 1118 | Observation | `Observation.valueCodeableConcept.coding` | 395100000.0 | No evidence of cancer found | http://snomed.info/sct |
| 172 | 1119 | Observation | `Observation.valueCodeableConcept.coding` | 315266007.0 | Suspected cervical cancer | http://snomed.info/sct |
| 173 | 1126 | Observation | `Observation.code.coding` | X099241 | Tes IVA | http://terminology.kemkes.go.id/CodeSystem/examination |
| 174 | 1134 | Observation | `Observation.valueCodeableConcept.coding` | 300557001.0 | Aceto-white reaction positive | http://snomed.info/sct |
| 175 | 1135 | Observation | `Observation.valueCodeableConcept.coding` | 300558006.0 | Aceto-white reaction negative | http://snomed.info/sct |
| 176 | 1142 | Observation | `Observation.code.coding` | 44550-2 | Human papilloma virus DNA [Presence] in Cervix by Probe | http://loinc.org |
| 177 | 1150 | Observation | `Observation.valueCodeableConcept.coding` | 787724008.0 | Human papillomavirus deoxyribonucleic acid not detected | http://snomed.info/sct |
| 178 | 1151 | Observation | `Observation.valueCodeableConcept.coding` | 787723002.0 | Human papillomavirus deoxyribonucleic acid detected | http://snomed.info/sct |
| 179 | 1152 | Observation | `Observation.valueCodeableConcept.coding` | OV000351 | Positif (HPV tipe onkogenik lain) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 180 | 1153 | Observation | `Observation.valueCodeableConcept.coding` | 708311006.0 | Deoxyribonucleic acid of Human papillomavirus 52 | http://snomed.info/sct |
| 181 | 1154 | Observation | `Observation.valueCodeableConcept.coding` | 708299006.0 | Deoxyribonucleic acid of Human papillomavirus 18 | http://snomed.info/sct |
| 182 | 1155 | Observation | `Observation.valueCodeableConcept.coding` | 708298003.0 | Deoxyribonucleic acid of Human papillomavirus 16 | http://snomed.info/sct |
| 183 | 1162 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | female | Female | http://hl7.org/fhir/administrative-gender |
| 184 | 1163 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | male | Male | http://hl7.org/fhir/administrative-gender |
| 185 | 1166 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | SP000438 | <45 thn | http://terminology.kemkes.go.id/sp |
| 186 | 1167 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | SP000439 | 45-65 thn | http://terminology.kemkes.go.id/sp |
| 187 | 1168 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | SP000440 | >65 tahun | http://terminology.kemkes.go.id/sp |
| 188 | 1171 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | QRI000032 | Memiliki diagnosis kanker >5 tahun yang lalu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 189 | 1172 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | QRI000033 | Memiliki diagnosis kanker <5 tahun yang lalu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 190 | 1173 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | QRI000034 | Tidak pernah didiagnosis menderita kanker | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 191 | 1176 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | QRI000036 | Tidak ada keluarga yang terdiagnosis kanker | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 192 | 1177 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 429011007.0 | Family history of malignant neoplasm of lung | http://snomed.info/sct |
| 193 | 1178 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | QRI000035 | Memiliki keluarga yang terdiagnosis kanker lain | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 194 | 1181 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | QRI000023 | Perokok/bekas perokok berhenti <10 tahun lalu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 195 | 1182 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | QRI000022 | Perokok aktif (dalam 1 tahun ini masih merokok) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 196 | 1183 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 266919005.0 | Never smoked tobacco | http://snomed.info/sct |
| 197 | 1184 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 16090771000119104 | Occupational exposure to environmental tobacco smoke | http://snomed.info/sct |
| 198 | 1187 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | QRI000019 | Tidak memiliki tempat kerja mengandung zat karsinogenik | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 199 | 1188 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | QRI000018 | Tidak yakin memiliki tempat kerja mengandung zat karsinogenik | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 200 | 1189 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | QRI000017 | Memiliki tempat kerja mengandung zat karsinogenik | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 201 | 1192 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | QRI000024 | Memiliki tempat tinggal berpotensi tinggi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 202 | 1193 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | QRI000026 | Tidak memiliki tempat tinggal berpotensi tinggi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 203 | 1194 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | QRI000025 | Tidak yakin memiliki tempat tinggal berpotensi tinggi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 204 | 1197 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | QRI000029 | Memiliki lingkungan dalam rumah yang sehat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 205 | 1198 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | QRI000028 | Tidak yakin memiliki lingkungan dalam rumah yang tidak sehat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 206 | 1199 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | QRI000027 | Memiliki lingkungan dalam rumah yang tidak sehat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 207 | 1202 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 161414005.0 | History of tuberculosis | http://snomed.info/sct |
| 208 | 1203 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 414415007.0 | History of chronic lung disease | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 209 | 1204 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 160258000.0 | No history of respiratory system disease | http://snomed.info/sct |
| 210 | 1207 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 723505004.0 | Low risk | http://snomed.info/sct |
| 211 | 1208 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 25594002.0 | Moderate risk of | http://snomed.info/sct |
| 212 | 1209 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 723509005.0 | High risk | http://snomed.info/sct |
| 213 | 1212 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 17621005.0 | Normal | http://snomed.info/sct |
| 214 | 1213 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 263654008 | Abnormal | http://snomed.info/sct |
| 215 | 1220 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | female | Female | http://hl7.org/fhir/administrative-gender |
| 216 | 1221 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | male | Male | http://hl7.org/fhir/administrative-gender |
| 217 | 1224 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | SP000441 | <50 tahun | http://terminology.kemkes.go.id/sp |
| 218 | 1225 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | SP000442 | 50 - 69 tahun | http://terminology.kemkes.go.id/sp |
| 219 | 1226 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | SP000443 | >= 70 tahun | http://terminology.kemkes.go.id/sp |
| 220 | 1237 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 723505004.0 | Low risk | http://snomed.info/sct |
| 221 | 1238 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 25594002.0 | Moderate risk of | http://snomed.info/sct |
| 222 | 1239 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 723509005.0 | High risk | http://snomed.info/sct |
| 223 | 1254 | Observation | `Observation.code.coding` | 410007005.0 | Rectal examination | http://snomed.info/sct |
| 224 | 1262 | Observation | `Observation.valueCodeableConcept.coding` | 248523006.0 | Rectal mass | http://snomed.info/sct |
| 225 | 1263 | Observation | `Observation.valueCodeableConcept.coding` | 300870000.0 | No mass present | http://snomed.info/sct |
| 226 | 1270 | Observation | `Observation.code.coding` | 14563-1 | Hemoglobin.gastrointestinal [Presence] in Stool --1st specimen | http://loinc.org |
| 227 | 1278 | Observation | `Observation.valueCodeableConcept.coding` | 167667006.0 | Occult blood not detected in feces | http://snomed.info/sct |
| 228 | 1279 | Observation | `Observation.valueCodeableConcept.coding` | 59614000.0 | Occult blood detected in feces | http://snomed.info/sct |
| 229 | 1290 | Observation | `Observation.code.coding` | 247301006.0 | Finding of ability to hear whisper | http://snomed.info/sct |
| 230 | 1298 | Observation | `Observation.valueCodeableConcept.coding` | 275727004.0 | Hearing test normal | http://snomed.info/sct |
| 231 | 1299 | Observation | `Observation.valueCodeableConcept.coding` | 300221005.0 | Hearing for whisper impaired | http://snomed.info/sct |
| 232 | 1306 | Observation | `Observation.code.coding` | 76517002.0 | Otoscopy | http://snomed.info/sct |
| 233 | 1314 | Observation | `Observation.valueCodeableConcept.coding` | 275727004.0 | Hearing test normal | http://snomed.info/sct |
| 234 | 1315 | Observation | `Observation.valueCodeableConcept.coding` | 300221005.0 | Hearing for whisper impaired | http://snomed.info/sct |
| 235 | 1322 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.answer.valueCoding` | 400911007.0 | Tumbling E test | http://snomed.info/sct |
| 236 | 1323 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.answer.valueCoding` | 252973004.0 | Snellen chart assessment | http://snomed.info/sct |
| 237 | 1329 | Observation | `Observation.code.coding` | 400911007.0 | Tumbling E test | http://snomed.info/sct |
| 238 | 1330 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 239 | 1331 | Observation | `Observation.valueCodeableConcept.coding` | 45089002.0 | Normal vision | http://snomed.info/sct |
| 240 | 1332 | Observation | `Observation.interpretation.coding` | 45089002.0 | Normal vision | http://snomed.info/sct |
| 241 | 1333 | Observation | `Observation.valueCodeableConcept.coding` | 397540003.0 | Visual impairment | http://snomed.info/sct |
| 242 | 1334 | Observation | `Observation.interpretation.coding` | 397540003.0 | Visual impairment | http://snomed.info/sct |
| 243 | 1345 | Observation | `Observation.code.coding` | 252973004.0 | Snellen chart assessment | http://snomed.info/sct |
| 244 | 1346 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 245 | 1347 | Observation | `Observation.valueCodeableConcept.coding` | 45089002.0 | Normal vision | http://snomed.info/sct |
| 246 | 1348 | Observation | `Observation.interpretation.coding` | 45089002.0 | Normal vision | http://snomed.info/sct |
| 247 | 1349 | Observation | `Observation.valueCodeableConcept.coding` | 397540003.0 | Visual impairment | http://snomed.info/sct |
| 248 | 1350 | Observation | `Observation.interpretation.coding` | 397540003.0 | Visual impairment | http://snomed.info/sct |
| 249 | 1364 | Observation | `Observation.code.coding` | 441841000.0 | Pinhole visual acuity test | http://loinc.org |
| 250 | 1365 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 251 | 1366 | Observation | `Observation.valueCodeableConcept.coding` | 39021009.0 | Disorder of refraction | http://snomed.info/sct |
| 252 | 1367 | Observation | `Observation.interpretation.coding` | 39021009.0 | Disorder of refraction | http://snomed.info/sct |
| 253 | 1368 | Observation | `Observation.valueCodeableConcept.coding` | OI000044 | Kelainan organik | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 254 | 1369 | Observation | `Observation.interpretation.coding` | OI000044 | Kelainan organik | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 255 | 1383 | Observation | `Observation.code.coding` | 40137007.0 | Pupil light reflex | http://snomed.info/sct |
| 256 | 1384 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 257 | 1385 | Observation | `Observation.valueCodeableConcept.coding` | OV000393 | Suspek katarak | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 258 | 1386 | Observation | `Observation.valueCodeableConcept.coding` | 371405004.0 | Disorder of eye proper | http://snomed.info/sct |
| 259 | 1401 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.answer.valueCoding` | TK000147 | Tidak sama sekali | http://terminology.kemkes.go.id |
| 260 | 1402 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.answer.valueCoding` | TK000148 | Kurang dari satu minggu | http://terminology.kemkes.go.id |
| 261 | 1403 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.answer.valueCoding` | TK000149 | Lebih dari satu minggu | http://terminology.kemkes.go.id |
| 262 | 1404 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.answer.valueCoding` | TK000150 | Hampir setiap hari | http://terminology.kemkes.go.id |
| 263 | 1407 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.answer.valueCoding` | TK000147 | Tidak sama sekali | http://terminology.kemkes.go.id |
| 264 | 1408 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.answer.valueCoding` | TK000148 | Kurang dari satu minggu | http://terminology.kemkes.go.id |
| 265 | 1409 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.answer.valueCoding` | TK000149 | Lebih dari satu minggu | http://terminology.kemkes.go.id |
| 266 | 1410 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.answer.valueCoding` | TK000150 | Hampir setiap hari | http://terminology.kemkes.go.id |
| 267 | 1413 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.answer.valueCoding` | TK000147 | Tidak sama sekali | http://terminology.kemkes.go.id |
| 268 | 1414 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.answer.valueCoding` | TK000148 | Kurang dari satu minggu | http://terminology.kemkes.go.id |
| 269 | 1415 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.answer.valueCoding` | TK000149 | Lebih dari satu minggu | http://terminology.kemkes.go.id |
| 270 | 1416 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.answer.valueCoding` | TK000150 | Hampir setiap hari | http://terminology.kemkes.go.id |
| 271 | 1419 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.answer.valueCoding` | TK000147 | Tidak sama sekali | http://terminology.kemkes.go.id |
| 272 | 1420 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.answer.valueCoding` | TK000148 | Kurang dari satu minggu | http://terminology.kemkes.go.id |
| 273 | 1421 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.answer.valueCoding` | TK000149 | Lebih dari satu minggu | http://terminology.kemkes.go.id |
| 274 | 1422 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.answer.valueCoding` | TK000150 | Hampir setiap hari | http://terminology.kemkes.go.id |
| 275 | 1472 | Observation | `Observation.code.coding` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 276 | 1473 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 277 | 1474 | Observation | `Observation.valueCodeableConcept.coding` | 11214006.0 | Reactive | http://snomed.info/sct |
| 278 | 1475 | Observation | `Observation.valueCodeableConcept.coding` | 131194007.0 | Non-Reactive | http://snomed.info/sct |
| 279 | 1488 | Observation | `Observation.code.coding` | 72376-7 | Hepatitis C virus Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 280 | 1489 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 281 | 1490 | Observation | `Observation.valueCodeableConcept.coding` | 11214006.0 | Reactive | http://snomed.info/sct |
| 282 | 1491 | Observation | `Observation.valueCodeableConcept.coding` | 131194007.0 | Non-Reactive | http://snomed.info/sct |
| 283 | 1524 | Observation | `Observation.code.coding` | 1920-8 | Aspartate aminotransferase [Enzymatic activity/volume] in Serum or Plasma | http://loinc.org |
| 284 | 1525 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 285 | 1541 | Observation | `Observation.code.coding[x]` | 26515-7 | Platelets [#/volume] in Blood | http://loinc.org |
| 286 | 1557 | Observation | `Observation.code.coding[x]` | 86465-2 | AST to platelet ratio index in Serum and Blood by calculation | http://loinc.org |
| 287 | 1561 | Observation | `Observation.interpretation.coding` | N | Normal | http://termi nology.hl7. org/CodeSy stem/v3-Ob servationIn terpretation |
| 288 | 1566 | Observation | `Observation.interpretation.coding` | 112674009.0 | Fibrosis | http://snomed.info/sct |
| 289 | 1569 | Observation | `Observation.interpretation.coding` | 19943007.0 | Cirrhosis of liver | http://snomed.info/sct |
| 290 | 1579 | Observation | `Observation.code.coding` | TK000144 | Rencana menikah 1 tahun ke depan | http://terminology.kemkes.go.id |
| 291 | 1604 | Observation | `Observation.code.coding` | 30352-9 | Hemoglobin [Mass/volume] in Capillary blood | http://loinc.org |
| 292 | 1612 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 293 | 1615 | Observation | `Observation.interpretation.coding` | 271737000.0 | Anemia | http://snomed.info/sct |
| 294 | 1629 | Observation | `Observation.code.coding` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 295 | 1630 | Observation | `Observation.valueCodeableConcept.coding` | LA15255-5 | Reactive | http://loinc.org |
| 296 | 1631 | Observation | `Observation.valueCodeableConcept.coding` | LA15256-3 | Nonreactive | http://loinc.org |
| 297 | 1650 | Observation | `Observation.code.coding` | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 298 | 1651 | Observation | `Observation.valueCodeableConcept.coding` | LA15255-5 | Reactive | http://loinc.org |
| 299 | 1652 | Observation | `Observation.valueCodeableConcept.coding` | LA15256-3 | Nonreactive | http://loinc.org |
| 300 | 1677 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000169 | Benar semua kata | http://terminology.kemkes.go.id |
| 301 | 1678 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000444 | Salah satu/Dua | http://terminology.kemkes.go.id/sp |
| 302 | 1679 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000170 | Tidak dapat mengingat/mengulang kata | http://terminology.kemkes.go.id |
| 303 | 1687 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 38369006.0 | At increased risk for cognitive impairment | http://snomed.info/sct |
| 304 | 1688 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000173 | Kemungkinan tidak ada gangguan kognitif | http://terminology.kemkes.go.id |
| 305 | 1710 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 129845004.0 | At risk for malnutrition | http://snomed.info/sct |
| 306 | 1711 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 248324001.0 | Well nourished | http://snomed.info/sct |
| 307 | 1724 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000197 | Kemungkinan depresi | http://terminology.kemkes.go.id |
| 308 | 1725 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000196 | Tidak depresi | http://terminology.kemkes.go.id |
| 309 | 1728 | Observation | `Observation.code.coding` | 48542-5 | Geriatric depression scale (GDS) panel | http://loinc.org |
| 310 | 1729 | Observation | `Observation.interpretation.coding` | TK000196 | Tidak depresi | http://terminology.kemkes.go.id |
| 311 | 1732 | Observation | `Observation.interpretation.coding` | TK000197 | Kemungkinan depresi | http://terminology.kemkes.go.id |
| 312 | 1735 | Observation | `Observation.interpretation.coding` | 35489007.0 | Depression | http://snomed.info/sct |
| 313 | 1747 | Observation | `Observation.component.code.coding` | 48512-8 | Are you basically satisfied with your life [GDS] | http://loinc.org |
| 314 | 1750 | Observation | `Observation.component.code.coding` | 48515-1 | Do you often get bored [GDS] | http://loinc.org |
| 315 | 1753 | Observation | `Observation.component.code.coding` | 48521-9 | Do you often feel helpless [GDS] | http://loinc.org |
| 316 | 1756 | Observation | `Observation.component.code.coding` | 48528-4 | Do you feel pretty worthless the way you are now [GDS] | http://loinc.org |
| 317 | 1761 | Observation | `Observation.code.coding` | 96762-0 | Barthel index panel | http://loinc.org |
| 318 | 1762 | Observation | `Observation.interpretation.coding` | OI000048 | Ketergantungan total | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 319 | 1767 | Observation | `Observation.interpretation.coding` | OI000047 | Ketergantungan berat | http://snomed.info/sct |
| 320 | 1772 | Observation | `Observation.interpretation.coding` | OI000046 | Ketergantungan sedang | http://snomed.info/sct |
| 321 | 1777 | Observation | `Observation.interpretation.coding` | OI000045 | Ketergantungan ringan | http://snomed.info/sct |
| 322 | 1782 | Observation | `Observation.interpretation.coding` | 371153006.0 | Independent | http://snomed.info/sct |
| 323 | 1792 | Observation | `Observation.component.code.coding` | 96759-6 | Bowels | http://loinc.org |
| 324 | 1793 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31627-5 | Incontinent (or needs to be given enemas) | http://loinc.org |
| 325 | 1794 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31626-7 | Occasional accident | http://loinc.org |
| 326 | 1795 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31625-9 | Continent | http://loinc.org |
| 327 | 1796 | Observation | `Observation.component.code.coding` | 96760-4 | Bladder | http://loinc.org |
| 328 | 1797 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31628-3 | Incontinent, or catheterized and unable to manage alone | http://loinc.org |
| 329 | 1798 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31626-7 | Occasional accident | http://loinc.org |
| 330 | 1799 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31625-9 | Continent | http://loinc.org |
| 331 | 1800 | Observation | `Observation.component.code.coding` | 96767-9 | Grooming | http://loinc.org |
| 332 | 1801 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31643-2 | Needs help with personal care | http://loinc.org |
| 333 | 1802 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31644-0 | Independent face/hair/teeth/shaving (implements provided) | http://loinc.org |
| 334 | 1803 | Observation | `Observation.component.code.coding` | 83183-4 | Toilet Use | http://loinc.org |
| 335 | 1804 | Observation | `Observation.component.valueCodeableConcept.coding` | LA12304-4 | Dependent | http://loinc.org |
| 336 | 1805 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31631-7 | Needs some help, but can do something alone | http://loinc.org |
| 337 | 1806 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31632-5 | Independent (on and off, dressing, wiping) | http://loinc.org |
| 338 | 1807 | Observation | `Observation.component.code.coding` | 83184-2 | Feeding | http://loinc.org |
| 339 | 1808 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24937-7 | Unable | http://loinc.org |
| 340 | 1809 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31630-9 | Needs help cutting, spreading butter, etc., or requires modified diet | http://loinc.org |
| 341 | 1810 | Observation | `Observation.component.valueCodeableConcept.coding` | LA12302-8 | Independent | http://loinc.org |
| 342 | 1811 | Observation | `Observation.component.code.coding` | 83185-9 | Transfer | http://loinc.org |
| 343 | 1812 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31633-3 | Unable, no sitting balance | http://loinc.org |
| 344 | 1813 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31634-1 | Major help (one or two people, physical), can sit | http://loinc.org |
| 345 | 1814 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31635-8 | Minor help (verbal or physical) | http://loinc.org |
| 346 | 1815 | Observation | `Observation.component.valueCodeableConcept.coding` | LA12302-8 | Independent | http://loinc.org |
| 347 | 1816 | Observation | `Observation.component.code.coding` | 83186-7 | Mobility | http://loinc.org |
| 348 | 1817 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31639-0 | Immobile or <50 yards | http://loinc.org |
| 349 | 1818 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31640-8 | Wheelchair independent, including corners, >50 yards | http://loinc.org |
| 350 | 1819 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31641-6 | Walks with help of one person (verbal or physical) >50 yards | http://loinc.org |
| 351 | 1820 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31642-4 | Independent (but may use any aid; for example, stick) >50 yards | http://loinc.org |
| 352 | 1821 | Observation | `Observation.component.code.coding` | 83182-6 | Dressing | http://loinc.org |
| 353 | 1822 | Observation | `Observation.component.valueCodeableConcept.coding` | LA12304-4 | Dependent | http://loinc.org |
| 354 | 1823 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31637-4 | Needs help but can do about half unaided | http://loinc.org |
| 355 | 1824 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31638-2 | Independent (including buttons, zips, laces, etc.) | http://loinc.org |
| 356 | 1825 | Observation | `Observation.component.code.coding` | 96758-8 | Stairs | http://loinc.org |
| 357 | 1826 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24937-7 | Unable | http://loinc.org |
| 358 | 1827 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31629-1 | Needs help (verbal, physical, carrying aid) | http://loinc.org |
| 359 | 1828 | Observation | `Observation.component.valueCodeableConcept.coding` | LA12302-8 | Independent | http://loinc.org |
| 360 | 1829 | Observation | `Observation.component.code.coding` | 83181-8 | Bathing | http://loinc.org |
| 361 | 1830 | Observation | `Observation.component.valueCodeableConcept.coding` | LA12304-4 | Dependent | http://loinc.org |
| 362 | 1831 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31636-6 | Independent (or in shower) | http://loinc.org |
| 363 | 1834 | Observation | `Observation.code.coding` | 72234-8 | Mini-Cog | http://loinc.org |
| 364 | 1835 | Observation | `Observation.valueCodeableConcept.coding` | TK000167 | Benar 1 kata | http://terminology.kemkes.go.id |
| 365 | 1836 | Observation | `Observation.valueCodeableConcept.coding` | TK000168 | Benar 2 kata | http://terminology.kemkes.go.id |
| 366 | 1837 | Observation | `Observation.valueCodeableConcept.coding` | TK000169 | Benar semua kata | http://terminology.kemkes.go.id |
| 367 | 1838 | Observation | `Observation.valueCodeableConcept.coding` | TK000170 | Tidak dapat mengingat/mengulang kata | http://terminology.kemkes.go.id |
| 368 | 1849 | Observation | `Observation.code.coding` | 79150-9 | Clock drawing panel [GPCOG] | http://loinc.org |
| 369 | 1850 | Observation | `Observation.component.code.coding` | 79106-1 | Please mark in all the numbers to indicate the hours of a clock | http://loinc.org |
| 370 | 1851 | Observation | `Observation.component.code.coding` | 79107-9 | Please mark in hands to show 10 minutes past eleven o'clock (11:10) | http://loinc.org |
| 371 | 1855 | Observation | `Observation.interpretation.coding` | TK000171 | Gambar jam benar/tepat | http://terminology.kemkes.go.id |
| 372 | 1856 | Observation | `Observation.interpretation.coding` | TK000172 | Gambar jam salah/tidak tepat | http://terminology.kemkes.go.id |
| 373 | 1866 | Observation | `Observation.code.coding` | 72233-0 | Total score [Mini-Cog] | http://loinc.org |
| 374 | 1869 | Observation | `Observation.interpretation.coding` | 38369006.0 | At increased risk for cognitive impairment | http://snomed.info/sct |
| 375 | 1870 | Observation | `Observation.interpretation.coding` | TK000173 | Kemungkinan tidak ada gangguan kognitif | http://terminology.kemkes.go.id |
| 376 | 1889 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 263703002.0 | Changed | http://snomed.info/sct |
| 377 | 1890 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 260388006.0 | Unchanged | http://snomed.info/sct |
| 378 | 1891 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 261665006.0 | Unknown | http://snomed.info/sct |
| 379 | 1894 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 263703002.0 | Changed | http://snomed.info/sct |
| 380 | 1895 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 260388006.0 | Unchanged | http://snomed.info/sct |
| 381 | 1896 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 261665006.0 | Unknown | http://snomed.info/sct |
| 382 | 1899 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 263703002.0 | Changed | http://snomed.info/sct |
| 383 | 1900 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 260388006.0 | Unchanged | http://snomed.info/sct |
| 384 | 1901 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 261665006.0 | Unknown | http://snomed.info/sct |
| 385 | 1904 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 263703002.0 | Changed | http://snomed.info/sct |
| 386 | 1905 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 260388006.0 | Unchanged | http://snomed.info/sct |
| 387 | 1906 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 261665006.0 | Unknown | http://snomed.info/sct |
| 388 | 1909 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 263703002.0 | Changed | http://snomed.info/sct |
| 389 | 1910 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 260388006.0 | Unchanged | http://snomed.info/sct |
| 390 | 1911 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 261665006.0 | Unknown | http://snomed.info/sct |
| 391 | 1914 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 263703002.0 | Changed | http://snomed.info/sct |
| 392 | 1915 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 260388006.0 | Unchanged | http://snomed.info/sct |
| 393 | 1916 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 261665006.0 | Unknown | http://snomed.info/sct |
| 394 | 1919 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 263703002.0 | Changed | http://snomed.info/sct |
| 395 | 1920 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 260388006.0 | Unchanged | http://snomed.info/sct |
| 396 | 1921 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 261665006.0 | Unknown | http://snomed.info/sct |
| 397 | 1924 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 263703002.0 | Changed | http://snomed.info/sct |
| 398 | 1925 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 260388006.0 | Unchanged | http://snomed.info/sct |
| 399 | 1926 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 261665006.0 | Unknown | http://snomed.info/sct |
| 400 | 1932 | Observation | `Observation.code.coding` | 71722-3 | Total score [AD8] | http://loinc.org |
| 401 | 1934 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7. org/CodeSystem/v3-Ob servationInterpretatio n |
| 402 | 1935 | Observation | `Observation.interpretation.coding` | 698464007.0 | At risk of dementia | http://snomed.info/sct |
| 403 | 1945 | Observation | `Observation.code.coding` | 66248-6 | Balance test [PhenX] | http://loinc.org |
| 404 | 1946 | Observation | `Observation.component.code.coding` | LA18188-5 | Side by side stand | http://loinc.org |
| 405 | 1947 | Observation | `Observation.component.valueCodeableConcept.coding` | LA15186-2 | Held for 10 sec - 1 point | http://loinc.org |
| 406 | 1948 | Observation | `Observation.component.valueCodeableConcept.coding` | LA15187-0 | Not held for 10 sec - 0 points | http://loinc.org |
| 407 | 1949 | Observation | `Observation.component.valueCodeableConcept.coding` | LA15188-8 | Not attempted - 0 points | http://loinc.org |
| 408 | 1950 | Observation | `Observation.component.code.coding` | LA18189-3 | Semi tandem stand | http://loinc.org |
| 409 | 1951 | Observation | `Observation.component.valueCodeableConcept.coding` | LA15186-2 | Held for 10 sec - 1 point | http://loinc.org |
| 410 | 1952 | Observation | `Observation.component.valueCodeableConcept.coding` | LA15187-0 | Not held for 10 sec - 0 points | http://loinc.org |
| 411 | 1953 | Observation | `Observation.component.valueCodeableConcept.coding` | LA15188-8 | Not attempted - 0 points | http://loinc.org |
| 412 | 1954 | Observation | `Observation.component.code.coding` | LA18190-1 | Tandem stand | http://loinc.org |
| 413 | 1955 | Observation | `Observation.component.valueCodeableConcept.coding` | LA15186-2 | Held for 10 sec - 1 point | http://loinc.org |
| 414 | 1956 | Observation | `Observation.component.valueCodeableConcept.coding` | TK000174 | Bertahan 3 - 9.99 detik | http://terminology.kemkes.go.id |
| 415 | 1957 | Observation | `Observation.component.valueCodeableConcept.coding` | TK000175 | Bertahan <3 detik | http://terminology.kemkes.go.id |
| 416 | 1958 | Observation | `Observation.component.valueCodeableConcept.coding` | LA15188-8 | Not attempted - 0 points | http://loinc.org |
| 417 | 1969 | Observation | `Observation.code.coding` | 714283000.0 | Short Physical Performance Battery | http://snomed.info/sct |
| 418 | 1971 | Observation | `Observation.component.code.coding` | 66258-5 | For 4-Meter Walk | http://loinc.org |
| 419 | 1972 | Observation | `Observation.component.valueCodeableConcept.coding` | LA15201-9 | Time is less than 4.82 sec - 4 points | http://loinc.org |
| 420 | 1973 | Observation | `Observation.component.valueCodeableConcept.coding` | LA15200-1 | Time is 4.82 to 6.20 sec - 3 points | http://loinc.org |
| 421 | 1974 | Observation | `Observation.component.valueCodeableConcept.coding` | LA15199-5 | Time is 6.21 to 8.70 sec - 2 points | http://loinc.org |
| 422 | 1975 | Observation | `Observation.component.valueCodeableConcept.coding` | LA15198-7 | Time is more than 8.70 sec - 1 point | http://loinc.org |
| 423 | 1976 | Observation | `Observation.component.valueCodeableConcept.coding` | 66263-5 | Test not completed | http://loinc.org |
| 424 | 1977 | Observation | `Observation.component.code.coding` | 66264-3 | Safe to stand five times | http://loinc.org |
| 425 | 1978 | Observation | `Observation.component.valueCodeableConcept.coding` | TK000176 | <11.19 detik | http://terminology.kemkes.go.id |
| 426 | 1979 | Observation | `Observation.component.valueCodeableConcept.coding` | TK000177 | 11.2 - 13,69 detik | http://terminology.kemkes.go.id |
| 427 | 1980 | Observation | `Observation.component.valueCodeableConcept.coding` | TK000178 | 13.7 - 16.69 detik | http://terminology.kemkes.go.id |
| 428 | 1981 | Observation | `Observation.component.valueCodeableConcept.coding` | TK000179 | 16.7 - 59.9 detik | http://terminology.kemkes.go.id |
| 429 | 1982 | Observation | `Observation.component.valueCodeableConcept.coding` | 66263-5 | Test not completed | http://loinc.org |
| 430 | 1991 | Observation | `Observation.interpretation.coding` | 160697000.0 | Mobilitas fair | http://snomed.info/sct |
| 431 | 1992 | Observation | `Observation.interpretation.coding` | 82971005.0 | Limited mobility | http://snomed.info/sct |
| 432 | 2006 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 64379006.0 | Decrease in appetite | http://snomed.info/sct |
| 433 | 2007 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 79890006.0 | Loss of appetite | http://snomed.info/sct |
| 434 | 2008 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 161825005.0 | Appetite normal | http://snomed.info/sct |
| 435 | 2011 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000180 | Penurunan BB > 3 kg | http://terminology.kemkes.go.id |
| 436 | 2012 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 261665006.0 | Unknown | http://snomed.info/sct |
| 437 | 2013 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000181 | Penurunan BB antara 1-3 kg | http://terminology.kemkes.go.id |
| 438 | 2014 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000181 | Tidak ada penurunan BB | http://terminology.kemkes.go.id |
| 439 | 2017 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000183 | Harus berbaring di tempat tidur atau menggunakan kursi roda | http://terminology.kemkes.go.id |
| 440 | 2018 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000184 | Bisa bangun dari tempat tidur atau kursi roda, tetapi tidak bisa keluar rumah | http://terminology.kemkes.go.id |
| 441 | 2019 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000185 | Bisa bepergian keluar rumah | http://terminology.kemkes.go.id |
| 442 | 2026 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000186 | Demensia atau depresi berat | http://terminology.kemkes.go.id |
| 443 | 2027 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000187 | Demensia atau kepikunan ringan | http://terminology.kemkes.go.id |
| 444 | 2028 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000188 | Tidak ada masalah psikologis | http://terminology.kemkes.go.id |
| 445 | 2031 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000189 | IMT <19 | http://terminology.kemkes.go.id |
| 446 | 2032 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000190 | IMT 19 -<21 | http://terminology.kemkes.go.id |
| 447 | 2033 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000191 | IMT 21 -<23 | http://terminology.kemkes.go.id |
| 448 | 2034 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000192 | IMT >= 23 | http://terminology.kemkes.go.id |
| 449 | 2040 | Observation | `Observation.code.coding` | 39156-5 | Body mass index (BMI) [Ratio] | http://loinc.org |
| 450 | 2053 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000193 | <31 cm | http://terminology.kemkes.go.id |
| 451 | 2054 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000194 | >= 31 cm | http://terminology.kemkes.go.id |
| 452 | 2060 | Observation | `Observation.code.coding` | 8283-4 | Calf - right Maximum circumference | http://loinc.org |
| 453 | 2061 | Observation | `Observation.code.coding` | 8282-6 | Calf - left Maximum circumference | http://loinc.org |
| 454 | 2076 | Observation | `Observation.code.coding` | TK000195 | Mini Nutritional Assessment (MNA) SF | http://terminology.kemkes.go.id |
| 455 | 2079 | Observation | `Observation.interpretation.coding` | 248324001.0 | Well nourished | http://snomed.info/sct |
| 456 | 2080 | Observation | `Observation.interpretation.coding` | 129845004.0 | At risk for malnutrition | http://snomed.info/sct |
| 457 | 2081 | Observation | `Observation.interpretation.coding` | 2492009.0 | Malnutrition | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 178 |
| http://loinc.org | 131 |
| http://terminology.kemkes.go.id | 56 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 32 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 27 |
| http://terminology.kemkes.go.id/sp | 10 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 8 |
| http://hl7.org/fhir/administrative-gender | 6 |
| http://terminology.kemkes.go.id/CodeSystem/examination | 4 |
| http://terminology.kemkes.go.id/CodeSystem/data-absent-reason | 2 |
| http://hl7.org/fhir/sid/icd-10 | 1 |
| http://termi nology.hl7. org/CodeSy stem/v3-Ob servationIn terpretation | 1 |
| http://terminology.hl7. org/CodeSystem/v3-Ob servationInterpretatio n | 1 |
| **Total** | **457** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 30 | – | ihs_organization | Organization | `Organization.id` |
| 32 | – | organization_name | Organization | `Organization.name` |
| 33 | – | kabkota_name | Organization | `Organization.address.city` |
| 36 | – | provinsi | Organization | `Organization.address.extension.extension.url` |
| 39 | – | kabkota | Organization | `Organization.address.extension.extension.url` |
| 193 | – | tinggi_badan_cm | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.text` |
| 209 | – | index_massa_tubuh | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.text` |
| 240 | – | lingkar_perut | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.text` |
| 263 | – | apakah_pernah_dinyatakan_tekanan_darah_tinggi | QuestionnaireResponse | `QuestionnaireResponse.item.item.linkId` |
| 269 | – | sistolik | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueReference.reference` |
| 313 | – | diastolik | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueReference.reference` |
| 357 | – | tekanan_darah | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueReference.reference` |
| 381 | – | apakah_pernah_dinyatakan_diabetes_kencing_manis | QuestionnaireResponse | `QuestionnaireResponse.item.item.text` |
| 387 | – | gula_darah_sewaktu | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueReference.display` |
| 449 | – | gula_darah_puasa | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueReference.display` |
| 477 | – | gula_darah_puasa_lanjutan | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueReference.display` |
| 504 | – | gula_darah_2_jam_pp | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueReference.reference` |
| 535 | – | pemeriksaan_hb1ac | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueReference.display` |
| 558 | – | hasil_pemeriksaan_ekg | QuestionnaireResponse | `QuestionnaireResponse.item.item.text` |
| 602 | – | kolesterol_total | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueReference.display` |
| 603 | – | interpretasi_kolesterol_total | – | `` |
| 624 | – | masukkan_nilai_hdl | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueReference.reference` |
| 625 | – | interpretasi_hdl | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueReference.display` |
| 646 | – | masukkan_nilai_ldl | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueReference.reference` |
| 647 | – | interpretasi_ldl | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueReference.display` |
| 668 | – | masukkan_nilai_trigliserida | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueReference.reference` |
| 669 | – | hasil_interpretasi_trigliserida | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueReference.display` |
| 690 | – | hasil_interpretasi_dislipidemia | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueReference.reference` |
| 706 | – | prediksi_risiko_penyakit_kardiovaskular | QuestionnaireResponse | `QuestionnaireResponse.item.item.linkId` |
| 733 | – | hasil_pemeriksaan_ureum | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueReference.reference` |
| 753 | – | hasil_pemeriksaan_kreatinin | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueReference.reference` |
| 773 | – | hasil_pemeriksaan_elfg_ckd_epi | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueReference.reference` |
| 794 | – | hasil_pemeriksaan_gigi_karies | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.text` |
| 798 | – | hasil_pemeriksaan_gigi_hilang_dicabut | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.text` |
| 805 | – | hasil_pemeriksaan_pocket_periodontal | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.text` |
| 809 | – | hasil_pemeriksaan_gigi_goyang | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.text` |
| 816 | – | apakah_mengalami_batuk_lebih_dari_2_minggu | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.linkId` |
| 820 | – | apakah_sering_bertemu_dengan_penderita_tbc | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.linkId` |
| 824 | – | riwayat_kontak_tuberkulosis | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.linkId` |
| 829 | – | metode_pemeriksaan | QuestionnaireResponse | `QuestionnaireResponse.item.item.text` |
| 831 | – | hasil_pemeriksaan_bta | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueReference.display` |
| 846 | – | hasil_pemeriksaan_tb_tcm | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueReference.display` |
| 860 | – | hasil_pemeriksaan_tb_tcm | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueReference.display` |
| 874 | – | hasil_pemeriksaan_tb_tcm | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueReference.display` |
| 888 | – | hasil_pemeriksaan_tb_tcm | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueReference.display` |
| 1012 | – | usia_puma | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.linkId` |
| 1017 | – | apakah_mempunyai_riwayat_merokok | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.linkId` |
| 1021 | – | berapa_bungkus_rokok_dalam_1_tahun | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.linkId` |
| 1026 | – | apakah_pernah_merasa_napas_pendek_saat_jalan_cepat | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.linkId` |
| 1030 | – | apakah_mempunyai_dahak_atau_kesulitan_mengeluarkan_dahak | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.linkId` |
| 1034 | – | apakah_biasanya_batuk_ketika_tidak_menderita_flu | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.linkId` |
| 1038 | – | apakah_pernah_melakukan_spirometri | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.linkId` |
| 1042 | – | hasil_skor_puma | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.linkId` |
| 1053 | – | jenis_pemeriksaan | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.text` |
| 1062 | – | hasil_pemeriksaan_sadanis | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.linkId` |
| 1079 | – | hasil_pemeriksaan_usg_payudara | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.linkId` |
| 1100 | – | apakah_pernah_melakukan_hubungan_intim | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.linkId` |
| 1104 | – | hasil_pemeriksaan_inspekulo | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.linkId` |
| 1120 | – | hasil_pemeriksaan_iva | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.linkId` |
| 1136 | – | hasil_pemeriksaan_hpv | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.linkId` |
| 1161 | – | jenis_kelamin_1 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.text` |
| 1164 | – | usia | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.linkId` |
| 1169 | – | apakah_pernah_didiagnosa_menderita_kanker | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.linkId` |
| 1174 | – | apakah_ada_keluarga_yang_didiagnosa_menderita_kanker | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.linkId` |
| 1179 | – | riwayat_merokok_atau_paparan_asap_rokok | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.linkId` |
| 1185 | – | riwayat_tempat_kerja_mengandung_zat_karsinogenik | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.linkId` |
| 1190 | – | lingkungan_tempat_tinggal_berpotensi_tinggi | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.linkId` |
| 1195 | – | lingkungan_tempat_tinggal_berpotensi_tinggi_1 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.linkId` |
| 1200 | – | apakah_pernah_didiagnosis_penyakit_paru_kronik | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.linkId` |
| 1205 | – | apakah_pernah_didiagnosis_penyakit_paru_kronik_1 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.linkId` |
| 1211 | – | hasil_skrining_kanker_paru | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.text` |
| 1218 | – | jenis_kelamin_apcs | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.linkId` |
| 1222 | – | usia_skor_apcs | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.linkId` |
| 1227 | – | kankes_usus | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.linkId` |
| 1231 | – | riwayat_merokok_apcs | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.linkId` |
| 1235 | – | skor_apcs | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.linkId` |
| 1244 | – | kesediaan_colok_dubur | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.linkId` |
| 1248 | – | hasil_colok_dubur | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.linkId` |
| 1264 | – | hasil_darah_samar | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.linkId` |
| 1284 | – | hasil_pemeriksaan_tajam_pendengaran | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.linkId` |
| 1300 | – | hasil_pemeriksaan_otoskop_penala | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.linkId` |
| 1359 | – | hasil_pemeriksaan_pinhole | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.linkId` |
| 1379 | – | hasil_pemeriksaan_pupil | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.text` |
| 1400 | – | seberapa_sering_tidak_bersemangat_dalam_2_minggu | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.text` |
| 1406 | – | seberapa_sering_merasa_murung_tertekan_putus_asa_dalam_2_minggu | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.text` |
| 1412 | – | seberapa_sering_merasa_gugup_cemas_gelisah_dalam_2_minggu | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.text` |
| 1418 | – | seberapa_sering_merasa_khawatir_dalam_2_minggu | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.text` |
| 1424 | – | gejala_depresi | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.text` |
| 1428 | – | gejala_kecemasan | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.text` |
| 1435 | – | apakah_hasil_hepatitis_b_mendapat_positif | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.linkId` |
| 1439 | – | apakah_memiliki_keluarga_yang_menderita_hepatitis_b | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.linkId` |
| 1443 | – | apakah_pernah_melakukan_hubungan_intim_dengan_bebas | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.linkId` |
| 1447 | – | apakah_pernah_menerima_transfusi_darah | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.linkId` |
| 1451 | – | apakah_pernah_menjalani_cuci_darah | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.linkId` |
| 1455 | – | apakah_pernah_menggunakan_narkoba | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.linkId` |
| 1459 | – | apakah_anda_menderita_hiv | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.linkId` |
| 1463 | – | apakah_anda_mendapat_pengobatan_hepatitis_c_dan_tidak_sembuh | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.linkId` |
| 1467 | – | hasil_rapid_test_hepatitis_b | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.linkId` |
| 1484 | – | hasil_rapid_test_hepatitis_c | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.linkId` |
| 1499 | – | faktor_risiko_hepatitis_b | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.linkId` |
| 1503 | – | faktor_risiko_hepatitis_c | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.linkId` |
| 1507 | – | faktor_risiko_hepatitis | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.linkId` |
| 1515 | – | apakah_hasil_kolestrol_tinggi | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.linkId` |
| 1519 | – | nilai_sgot | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.linkId` |
| 1536 | – | pemeriksaan_trombosit | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.linkId` |
| 1552 | – | hasil_apri_score | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.linkId` |
| 1591 | – | rencana_menikah_dalam_kurun_waktu_1_tahun | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueBoolean` |
| 1592 | – | rencana_menikah_dalam_kurun_waktu_1_tahun | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueBoolean` |
| 1600 | – | hasil_pemeriksaan_rapid_test_hb | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.text` |
| 1625 | – | hasil_pemeriksaan_rapid_test_sifilis | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.text` |
| 1646 | – | hasil_pemeriksaan_rapid_test_hiv | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.text` |
| 2051 | – | lingkar_betis | QuestionnaireResponse | `QuestionnaireResponse.item.item.linkId` |
| 2071 | – | hasil_interpretasi_mnasf | QuestionnaireResponse | `QuestionnaireResponse.item.item.linkId` |
