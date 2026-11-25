# Output Form: ASIK - CKG Lansia (versi 2026)

Sumber: `mapping/phdt-data-dictionary-asik-ckg-lansia-2026.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-asik-ckg-lansia-2026.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 82 |
| Code (`jumlah code` = 1) | 462 |
| Code unik (code + CodeSystem) | 292 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 10 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–33 | Patient | – | – | _pasien_name_ → `Patient.name.text` (2, tanpa BQ)<br>_nik_ → `Patient.identifier.value` (5, tanpa BQ)<br>_pasien_id_ → `Patient.identifier.value` (8, tanpa BQ)<br>_jenis_kelamin_ → `Patient.gender` (10, tanpa BQ)<br>_tgl_lahir_ → `Patient.birthDate` (12, tanpa BQ)<br>_no_handphone_ → `Patient.telecom` (13, tanpa BQ)<br>_status_perkawinan_ → `Patient.maritalStatus.coding` (16, tanpa BQ)<br>_kabkota_name_ → `Patient.address.city` (20, tanpa BQ)<br>_provinsi_ → `Patient.address.extension.extension.valueCode` (24, tanpa BQ)<br>_kabkota_ → `Patient.address.extension.extension.valueCode` (27, tanpa BQ)<br>_kecamatan_ → `Patient.address.extension.extension.valueCode` (30, tanpa BQ)<br>_kelurahan_ → `Patient.address.extension.extension.valueCode` (33, tanpa BQ) |
| 2 | 72–85 | Encounter | – | – | _tgl_pelayanan_ → `Encounter.identifier` (72, tanpa BQ) |
| 3 | 86–93 | Condition | Z01.8 | Other specified special examinations | – |
| 4 | 104–115 | Observation | 424144002.0 | Current chronological age | _age_now_ → `Observation.valueQuantity.value` (107, tanpa BQ) |
| 5 | 116–127 | Observation | TK000144 | Rencana menikah 1 tahun ke depan | _rencana_menikah_dalam_kurun_waktu_1_tahun_ → `Observation.valueBoolean` (119, tanpa BQ) |
| 6 | 128–185 | QuestionnaireResponse | – | – | _apakah_merokok_dalam_setahun_terakhir_ → `QuestionnaireResponse.item.item.text` (140, tanpa BQ)<br>_sudah_berapa_tahun_merokok_ → `QuestionnaireResponse.item.item.answer.item.text` (144, tanpa BQ)<br>_berapa_batang_rokok_yang_dihisap_dalam_sehari_ → `QuestionnaireResponse.item.item.answer.item.text` (148, tanpa BQ)<br>_apakah_pernah_merokok_sebelumnya_ → `QuestionnaireResponse.item.item.text` (151, tanpa BQ)<br>_berapa_lama_merokok_sebelumnya_ → `QuestionnaireResponse.item.item.answer.item.text` (155, tanpa BQ)<br>_kapan_anda_berhenti_merokok_ → `QuestionnaireResponse.item.item.answer.item.text` (159, tanpa BQ)<br>_apakah_terpapar_asap_rokok_sebulan_terakhir_ → `QuestionnaireResponse.item.item.text` (163, tanpa BQ)<br>_apakah_rutin_melakukan_olahraga_ → `QuestionnaireResponse.item.item.text` (167, tanpa BQ)<br>_berapa_kali_berolahraga_dalam_seminggu_ → `QuestionnaireResponse.item.item.answer.item.text` (171, tanpa BQ)<br>_berapa_menit_berolahraga_ → `QuestionnaireResponse.item.item.answer.item.text` (174, tanpa BQ)<br>_tingkat_aktivitas_fisik_ → `QuestionnaireResponse.item.item.answer.item.linkId` (176, tanpa BQ)<br>_berat_badan_kg_ → `QuestionnaireResponse.item.item.item.text` (183, tanpa BQ) |
| 7 | 186–197 | Observation | 29463-7 | Body weight | – |
| 8 | 202–213 | Observation | 8302-2 | Body height | – |
| 9 | 218–244 | Observation | 39156-5 | Body mass index (BMI) [Ratio] | – |
| 10 | 249–268 | Observation | vital-signs | Abdominal circumference | – |
| 11 | 277–318 | Observation | 8480-6 | Systolic blood pressure | – |
| 12 | 321–362 | Observation | 8462-4 | Diastolic blood pressure | – |
| 13 | 365–385 | Observation | 268607006.0 | Hypertension risk level | – |
| 14 | 394–403 | ServiceRequest | – | – | – |
| 15 | 404–407 | PractitionerRole | – | – | – |
| 16 | 408–415 | Specimen | – | – | – |
| 17 | 416–441 | Observation | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | – |
| 18 | 442–453 | DiagnosticReport | – | – | – |
| 19 | 456–481 | Observation | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | – |
| 20 | 484–509 | Observation | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | – |
| 21 | 512–539 | Observation | 1521-4 | Glucose [Mass/volume] in Serum or Plasma --2 hours post meal | – |
| 22 | 542–562 | Observation | 4548-4 | Hemoglobin A1c/Hemoglobin.total in Blood | – |
| 23 | 567–604 | Observation | 34534-8 | 12 lead EKG panel | _hasil_detail_pemeriksaan_ekg_ → `Observation.component.code.coding` (581, tanpa BQ) |
| 24 | 610–629 | Observation | 2093-3 | Cholesterol [Mass/volume] in Serum or Plasma | – |
| 25 | 632–651 | Observation | 2085-9 | Cholesterol in HDL [Mass/volume] in Serum or Plasma | – |
| 26 | 654–673 | Observation | 2085-9 | Cholesterol in HDL [Mass/volume] in Serum or Plasma | – |
| 27 | 676–695 | Observation | 2571-8 | Triglyceride [Mass/volume] in Serum or Plasma | – |
| 28 | 698–711 | Observation | 100898-6 | Lipid panel - Serum or Plasma | – |
| 29 | 716–736 | Observation | OC000173 | Prediksi Risiko PTM tanpa Pemeriksaan Laboratorium | – |
| 30 | 741–758 | Observation | 20977-5 | Urea [Mass/volume] in Blood | – |
| 31 | 761–778 | Observation | 2160-0 | Creatinine [Mass/volume] in Serum or Plasma | – |
| 32 | 781–796 | Observation | 62238-1 | Glomerular filtration rate/1.73 sq M.predicted [Volume Rate/Area] in Serum, Plasma or Blood by Creatinine-based formula (CKD-EPI) | – |
| 33 | 837–846 | Procedure | 424489006.0 | Mantoux test | – |
| 34 | 848–859 | Observation | 23539-0 | Tuberculosis reaction wheal [Diameter] --3 days post dose mammalian tuberculin intradermal | – |
| 35 | 868–880 | Observation | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | – |
| 36 | 883–894 | Observation | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | – |
| 37 | 897–908 | Observation | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | – |
| 38 | 911–922 | Observation | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | – |
| 39 | 925–936 | Observation | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | – |
| 40 | 939–951 | Observation | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | – |
| 41 | 954–966 | Observation | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | – |
| 42 | 969–981 | Observation | 89372-7 | Mycobacterium tuberculosis complex rpoB gene rifAMPin resistance mutation [Presence] by Molecular method | – |
| 43 | 984–996 | Observation | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | – |
| 44 | 999–1011 | Observation | 89372-7 | Mycobacterium tuberculosis complex rpoB gene rifAMPin resistance mutation [Presence] by Molecular method | – |
| 45 | 1014–1026 | Observation | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | – |
| 46 | 1029–1041 | Observation | 89372-7 | Mycobacterium tuberculosis complex rpoB gene rifAMPin resistance mutation [Presence] by Molecular method | – |
| 47 | 1102–1114 | Observation | 13607009.0 | Manual examination of breast | – |
| 48 | 1119–1131 | Observation | 24601-7 | US Breast | – |
| 49 | 1144–1155 | Observation | 451024007.0 | Inspection of vagina using vaginal speculum | – |
| 50 | 1160–1171 | Observation | X099241 | Tes IVA | – |
| 51 | 1176–1191 | Observation | 44550-2 | Human papilloma virus DNA [Presence] in Cervix by Probe | – |
| 52 | 1288–1299 | Observation | 410007005.0 | Rectal examination | – |
| 53 | 1304–1315 | Observation | 14563-1 | Hemoglobin.gastrointestinal [Presence] in Stool --1st specimen | – |
| 54 | 1324–1335 | Observation | 247301006.0 | Finding of ability to hear whisper | – |
| 55 | 1340–1351 | Observation | 76517002.0 | Otoscopy | – |
| 56 | 1363–1378 | Observation | 400911007.0 | Tumbling E test | _pemeriksaan_visus_e_tumbling_ → `Observation.valueCodeableConcept.coding` (1367, tanpa BQ) |
| 57 | 1379–1394 | Observation | 252973004.0 | Snellen chart assessment | _pemeriksaan_visus_snellen_chart_ → `Observation.valueCodeableConcept.coding` (1383, tanpa BQ) |
| 58 | 1398–1413 | Observation | 441841000.0 | Pinhole visual acuity test | – |
| 59 | 1417–1430 | Observation | 40137007.0 | Pupil light reflex | – |
| 60 | 1506–1519 | Observation | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | – |
| 61 | 1522–1534 | Observation | 72376-7 | Hepatitis C virus Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | – |
| 62 | 1558–1571 | Observation | 1920-8 | Aspartate aminotransferase [Enzymatic activity/volume] in Serum or Plasma | – |
| 63 | 1575–1587 | Observation | – | – | – |
| 64 | 1591–1612 | Observation | – | – | – |
| 65 | 1613–1624 | Observation | TK000144 | Rencana menikah 1 tahun ke depan | _rencana_menikah_dalam_kurun_waktu_1_tahun_ → `Observation.valueBoolean` (1616, tanpa BQ) |
| 66 | 1638–1653 | Observation | 30352-9 | Hemoglobin [Mass/volume] in Capillary blood | – |
| 67 | 1663–1674 | Observation | 22464-2 | Reagin Ab [Presence] in Specimen | – |
| 68 | 1684–1695 | Observation | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | – |
| 69 | 1696–1761 | QuestionnaireResponse | – | – | _apakah_dapat_mengingat_tiga_kata_ → `QuestionnaireResponse.item.item.text` (1708, tanpa BQ)<br>_tanggal_berapa_hari_ini_dimana_saat_ini_ → `QuestionnaireResponse.item.item.text` (1712, tanpa BQ)<br>_apakah_dapat_mengingat_tiga_kata_sebelumnya_ → `QuestionnaireResponse.item.item.text` (1717, tanpa BQ)<br>_hasil_interpretasi_skilas_penurunan_kognitif_ → `QuestionnaireResponse.item.item.text` (1722, tanpa BQ)<br>_apakah_dapat_berdiri_dari_kursi_skilas_ → `QuestionnaireResponse.item.item.text` (1727, tanpa BQ)<br>_apakah_berat_badan_berkurang_ → `QuestionnaireResponse.item.item.text` (1733, tanpa BQ)<br>_apakah_nafsu_makan_hilang_ → `QuestionnaireResponse.item.item.text` (1737, tanpa BQ)<br>_apakah_lila_kurang_dari_21_cm_ → `QuestionnaireResponse.item.item.text` (1741, tanpa BQ)<br>_hasil_interpretasi_skilas_malnutrisi_ → `QuestionnaireResponse.item.item.text` (1745, tanpa BQ)<br>_apakah_merasa_sedih_dalam_2_minggu_terakhir_ → `QuestionnaireResponse.item.item.text` (1751, tanpa BQ)<br>_apakah_minat_berkurang_dalam_berkegiatan_dalam_2_minggu_terakhir_ → `QuestionnaireResponse.item.item.text` (1755, tanpa BQ)<br>_hasil_interpretasi_gejala_depresi_ → `QuestionnaireResponse.item.item.text` (1759, tanpa BQ) |
| 70 | 1762–1794 | Observation | 48542-5 | Geriatric depression scale (GDS) panel | _hasil_interpretasi_gejala_depresi_1_ → `Observation.valueQuantity.value` (1766, tanpa BQ)<br>_apakah_merasa_puas_dengan_kehidupan_ → `Observation.component.code.coding` (1783, tanpa BQ)<br>_apakah_sering_merasa_bosan_ → `Observation.component.code.coding` (1786, tanpa BQ)<br>_apakah_sering_merasa_tidak_berdaya_ → `Observation.component.code.coding` (1789, tanpa BQ)<br>_apakah_merasa_tidak_berharga_ → `Observation.component.code.coding` (1792, tanpa BQ) |
| 71 | 1795–1867 | Observation | 96762-0 | Barthel index panel | _hasil_intrepretasi_adl_ → `Observation.valueRange.low.value` (1799, tanpa BQ)<br>_apakah_dapat_mengendalikan_rangsang_bab_ → `Observation.component.code.coding` (1828, tanpa BQ)<br>_apakah_dapat_mengendalikan_rangsang_bak_ → `Observation.component.code.coding` (1832, tanpa BQ)<br>_apakah_dapat_membersihkan_diri_sendiri_ → `Observation.component.code.coding` (1836, tanpa BQ)<br>_apakah_dapat_menggunakan_jamban_sendiri_ → `Observation.component.code.coding` (1839, tanpa BQ)<br>_apakah_dapat_makan_sendiri_ → `Observation.component.code.coding` (1843, tanpa BQ)<br>_apakah_dapat_merubah_sikap_dari_berbaring_ke_duduk_sendiri_ → `Observation.component.code.coding` (1847, tanpa BQ)<br>_apakah_dapat_berjalan_sendiri_ → `Observation.component.code.coding` (1852, tanpa BQ)<br>_apakah_dapat_berpakaian_sendiri_ → `Observation.component.code.coding` (1857, tanpa BQ)<br>_apakah_dapat_turun_naik_tangga_sendiri_ → `Observation.component.code.coding` (1861, tanpa BQ)<br>_apakah_dapat_mandi_sendiri_ → `Observation.component.code.coding` (1865, tanpa BQ) |
| 72 | 1868–1882 | Observation | 72234-8 | Mini-Cog | _hasil_mengingat_3_versi_kata_ → `Observation.valueCodeableConcept.coding` (1871, tanpa BQ)<br>_sudah_mendengarkan_dan_mengingat_3_versi_kata_ → `Observation.note` (1882, tanpa BQ) |
| 73 | 1883–1899 | Observation | 79150-9 | Clock drawing panel [GPCOG] | _apakah_dapat_menggambar_sesuai_perintah_ → `Observation.component.valueBoolean` (1888, tanpa BQ) |
| 74 | 1900–1913 | Observation | 72233-0 | Total score [Mini-Cog] | _hasil_interpretasi_mini_cog_ → `Observation.valueQuantity` (1904, tanpa BQ) |
| 75 | 1914–1965 | QuestionnaireResponse | – | – | _apakah_sulit_membuat_keputusan_ → `QuestionnaireResponse.questionnaire` (1914, tanpa BQ)<br>_apakah_sudah_tidak_menekuni_hobi_ → `QuestionnaireResponse.item.linkId` (1928, tanpa BQ)<br>_apakah_keluar_mengulang_pertanyaan_cerita_pernyataan_yang_sama_ → `QuestionnaireResponse.item.linkId` (1933, tanpa BQ)<br>_apakah_kesulitan_belajar_menggunakan_perkakas_dan_peralatan_ → `QuestionnaireResponse.item.linkId` (1938, tanpa BQ)<br>_apakah_lupa_nama_bulan_atau_tahun_ → `QuestionnaireResponse.item.linkId` (1943, tanpa BQ)<br>_apakah_kesulitan_mengatur_keuangan_ → `QuestionnaireResponse.item.linkId` (1948, tanpa BQ)<br>_apakah_sulit_mengingat_janji_ → `QuestionnaireResponse.item.linkId` (1953, tanpa BQ)<br>_apakah_mengalami_gangguan_memori_dan_pemikiran_yang_konsisten_ → `QuestionnaireResponse.item.linkId` (1958, tanpa BQ)<br>_hasil_interpretasi_ad_8_ → `QuestionnaireResponse.item.linkId` (1963, tanpa BQ) |
| 76 | 1966–1978 | Observation | 71722-3 | Total score [AD8] | – |
| 77 | 1979–2002 | Observation | 66248-6 | Balance test [PhenX] | _tes_keseimbangan_berdiri_berdampingan_ → `Observation.component.code.coding` (1982, tanpa BQ)<br>_tes_keseimbangan_berdiri_semi_tandem_ → `Observation.component.code.coding` (1986, tanpa BQ)<br>_tes_keseimbangan_berdiri_tandem_ → `Observation.component.code.coding` (1990, tanpa BQ) |
| 78 | 2003–2028 | Observation | 714283000.0 | Short Physical Performance Battery | _tes_kecepatan_berjalan_ → `Observation.component.code.coding` (2007, tanpa BQ)<br>_tes_berdiri_dari_kursi_ → `Observation.component.code.coding` (2013, tanpa BQ)<br>_hasil_interpretasi_spbb_ → `Observation.valueQuantity` (2019, tanpa BQ) |
| 79 | 2029–2073 | QuestionnaireResponse | – | – | _apakah_asupan_makan_turun_dalam_3_bulan_terakhir_ → `QuestionnaireResponse.item.text` (2039, tanpa BQ)<br>_apakah_berat_badan_turun_dalam_3_bulan_terakhir_ → `QuestionnaireResponse.item.item.linkId` (2045, tanpa BQ)<br>_kemampuan_melakukan_mobilitas_ → `QuestionnaireResponse.item.item.linkId` (2051, tanpa BQ)<br>_apakah_menderita_stress_atau_penyakit_akut_dalam_3_bulan_terakhir_ → `QuestionnaireResponse.item.item.linkId` (2056, tanpa BQ)<br>_apakah_mengalami_masalah_neuropsikologis_ → `QuestionnaireResponse.item.item.linkId` (2060, tanpa BQ)<br>_nilai_imt_ → `QuestionnaireResponse.item.item.linkId` (2065, tanpa BQ) |
| 80 | 2074–2086 | Observation | 39156-5 | Body mass index (BMI) [Ratio] | – |
| 81 | 2094–2106 | Observation | 8283-4 | Calf - right Maximum circumference | – |
| 82 | 2110–2124 | Observation | TK000195 | Mini Nutritional Assessment (MNA) SF | – |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 70 |
| QuestionnaireResponse | 4 |
| Patient | 1 |
| Encounter | 1 |
| Condition | 1 |
| ServiceRequest | 1 |
| PractitionerRole | 1 |
| Specimen | 1 |
| DiagnosticReport | 1 |
| Procedure | 1 |
| **Total** | **82** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 88 | Condition | `Condition.code.coding` | Z01.8 | Other specified special examinations | http://hl7.org/fhir/sid/icd-10 |
| 2 | 106 | Observation | `Observation.code.coding` | 424144002.0 | Current chronological age | http://snomed.info/sct |
| 3 | 118 | Observation | `Observation.code.coding` | TK000144 | Rencana menikah 1 tahun ke depan | http://terminology.kemkes.go.id |
| 4 | 160 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | TK000145 | 1 tahun yang lalu | http://terminology.kemkes.go.id |
| 5 | 161 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | TK000146 | Lebih dari 1 tahun yang lalu | http://terminology.kemkes.go.id |
| 6 | 178 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 424805008.0 | Exercise above recommended level | http://snomed.info/sct |
| 7 | 179 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 413300002.0 | Exercise below recommended level | http://snomed.info/sct |
| 8 | 188 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 9 | 204 | Observation | `Observation.code.coding` | 8302-2 | Body height | http://loinc.org |
| 10 | 220 | Observation | `Observation.code.coding` | 39156-5 | Body mass index (BMI) [Ratio] | http://loinc.org |
| 11 | 221 | Observation | `Observation.interpretation.coding` | 248342006.0 | Underweight | http://snomed.info/sct |
| 12 | 224 | Observation | `Observation.interpretation.coding` | 43664005.0 | Normal weight | http://snomed.info/sct |
| 13 | 229 | Observation | `Observation.interpretation.coding` | 238131007.0 | Overweight | http://snomed.info/sct |
| 14 | 234 | Observation | `Observation.interpretation.coding` | 414915002.0 | Obese | http://snomed.info/sct |
| 15 | 251 | Observation | `Observation.code.coding` | vital-signs | Abdominal circumference | http://snomed.info/sct |
| 16 | 261 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 17 | 265 | Observation | `Observation.interpretation.coding` | 248311001.0 | Central obesity | http://snomed.info/sct |
| 18 | 279 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 19 | 289 | Observation | `Observation.interpretation.coding` | OI000040 | Tekanan Darah Optimal | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 20 | 294 | Observation | `Observation.interpretation.coding` | 2004005.0 | Normal blood pressure | http://snomed.info/sct |
| 21 | 299 | Observation | `Observation.interpretation.coding` | OI000041 | Tekanan Darah Normal Tinggi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 22 | 304 | Observation | `Observation.interpretation.coding` | 827069000.0 | Stage 1 hypertension | http://snomed.info/sct |
| 23 | 309 | Observation | `Observation.interpretation.coding` | 827068008.0 | Stage 1 hypertension | http://snomed.info/sct |
| 24 | 314 | Observation | `Observation.interpretation.coding` | OI000042 | Hipertensi Derajat 3 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 25 | 323 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://snomed.info/sct |
| 26 | 333 | Observation | `Observation.interpretation.coding` | OI000040 | Tekanan Darah Optimal | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 27 | 338 | Observation | `Observation.interpretation.coding` | 2004005.0 | Normal blood pressure | http://snomed.info/sct |
| 28 | 343 | Observation | `Observation.interpretation.coding` | OI000041 | Tekanan Darah Normal Tinggi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 29 | 348 | Observation | `Observation.interpretation.coding` | 827069000.0 | Stage 1 hypertension | http://snomed.info/sct |
| 30 | 353 | Observation | `Observation.interpretation.coding` | 827068008.0 | Stage 1 hypertension | http://snomed.info/sct |
| 31 | 358 | Observation | `Observation.interpretation.coding` | OI000042 | Hipertensi Derajat 3 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 32 | 367 | Observation | `Observation.code.coding` | 268607006.0 | Hypertension risk level | http://snomed.info/sct |
| 33 | 379 | Observation | `Observation.interpretation.coding` | OI000040 | Tekanan Darah Optimal | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 34 | 380 | Observation | `Observation.interpretation.coding` | 2004005.0 | Normal blood pressure | http://snomed.info/sct |
| 35 | 381 | Observation | `Observation.interpretation.coding` | OI000041 | Tekanan Darah Normal Tinggi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 36 | 382 | Observation | `Observation.interpretation.coding` | 827069000.0 | Stage 1 hypertension | http://snomed.info/sct |
| 37 | 383 | Observation | `Observation.interpretation.coding` | 827068008.0 | Stage 2 hypertension | http://snomed.info/sct |
| 38 | 384 | Observation | `Observation.interpretation.coding` | OI000042 | Hipertensi Derajat 3 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 39 | 385 | Observation | `Observation.interpretation.coding` | 56218007.0 | Systolic hypertension | http://snomed.info/sct |
| 40 | 398 | ServiceRequest | `ServiceRequest.code` | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 41 | 406 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002.0 | Laboratory worker | http://snomed.info/sct |
| 42 | 409 | Specimen | `Specimen.type` | 119297000.0 | Blood specimen | http://snomed.info/sct |
| 43 | 418 | Observation | `Observation.code.coding` | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 44 | 426 | Observation | `Observation.interpretation.coding` | 302866003.0 | Hypoglycemia | http://snomed.info/sct |
| 45 | 429 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 46 | 434 | Observation | `Observation.interpretation.coding` | 714628002.0 | Prediabetes | http://snomed.info/sct |
| 47 | 439 | Observation | `Observation.interpretation.coding` | 80394007.0 | Hyperglycemia | http://snomed.info/sct |
| 48 | 444 | DiagnosticReport | `DiagnosticReport.code` | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 49 | 458 | Observation | `Observation.code.coding` | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 50 | 466 | Observation | `Observation.interpretation.coding` | 302866003.0 | Hypoglycemia | http://snomed.info/sct |
| 51 | 469 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 52 | 474 | Observation | `Observation.interpretation.coding` | 714628002.0 | Prediabetes | http://snomed.info/sct |
| 53 | 479 | Observation | `Observation.interpretation.coding` | 73211009.0 | Diabetes mellitus | http://snomed.info/sct |
| 54 | 486 | Observation | `Observation.code.coding` | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 55 | 494 | Observation | `Observation.interpretation.coding` | 302866003.0 | Hypoglycemia | http://snomed.info/sct |
| 56 | 497 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 57 | 502 | Observation | `Observation.interpretation.coding` | 714628002.0 | Prediabetes | http://snomed.info/sct |
| 58 | 507 | Observation | `Observation.interpretation.coding` | 73211009.0 | Diabetes mellitus | http://snomed.info/sct |
| 59 | 514 | Observation | `Observation.code.coding` | 1521-4 | Glucose [Mass/volume] in Serum or Plasma --2 hours post meal | http://loinc.org |
| 60 | 524 | Observation | `Observation.interpretation.coding` | 302866003.0 | Hypoglycemia | http://snomed.info/sct |
| 61 | 527 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 62 | 532 | Observation | `Observation.interpretation.coding` | 714628002.0 | Prediabetes | http://snomed.info/sct |
| 63 | 537 | Observation | `Observation.interpretation.coding` | 73211009.0 | Diabetes mellitus | http://snomed.info/sct |
| 64 | 544 | Observation | `Observation.code.coding` | 4548-4 | Hemoglobin A1c/Hemoglobin.total in Blood | http://loinc.org |
| 65 | 552 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 66 | 555 | Observation | `Observation.interpretation.coding` | 714628002.0 | Prediabetes | http://snomed.info/sct |
| 67 | 560 | Observation | `Observation.interpretation.coding` | 73211009.0 | Diabetes mellitus | http://snomed.info/sct |
| 68 | 569 | Observation | `Observation.code.coding` | 34534-8 | 12 lead EKG panel | http://loinc.org |
| 69 | 570 | Observation | `Observation.valueCodeableConcept.coding` | 17621005.0 | Normal | http://snomed.info/sct |
| 70 | 571 | Observation | `Observation.interpretation.coding` | 164854000 | Electrocardiogram normal | http://snomed.info/sct |
| 71 | 572 | Observation | `Observation.valueCodeableConcept.coding` | 263654008 | Abnormal | http://snomed.info/sct |
| 72 | 573 | Observation | `Observation.interpretation.coding` | 102594003.0 | Electrocardiogram abnormal | http://snomed.info/sct |
| 73 | 581 | Observation | `Observation.component.code.coding` | 164854000 | Electrocardiogram normal | http://snomed.info/sct |
| 74 | 584 | Observation | `Observation.component.code.coding` | 26141007 | ST segment depression | http://snomed.info/sct |
| 75 | 587 | Observation | `Observation.component.code.coding` | 59931005 | Electrocardiogram normal | http://snomed.info/sct |
| 76 | 590 | Observation | `Observation.component.code.coding` | 164873001 | Electrocardiographic left ventricle hypertrophy | http://snomed.info/sct |
| 77 | 593 | Observation | `Observation.component.code.coding` | 164889003 | Electrocardiographic atrial fibrillation | http://snomed.info/sct |
| 78 | 596 | Observation | `Observation.component.code.coding` | 164918000 | Pathological Q wave | http://snomed.info/sct |
| 79 | 599 | Observation | `Observation.component.code.coding` | 76388001 | ST segment elevation | http://snomed.info/sct |
| 80 | 602 | Observation | `Observation.component.code.coding` | 102594003.0 | Electrocardiogram abnormal | http://snomed.info/sct |
| 81 | 612 | Observation | `Observation.code.coding` | 2093-3 | Cholesterol [Mass/volume] in Serum or Plasma | http://loinc.org |
| 82 | 622 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 83 | 626 | Observation | `Observation.interpretation.coding` | H | High | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 84 | 634 | Observation | `Observation.code.coding` | 2085-9 | Cholesterol in HDL [Mass/volume] in Serum or Plasma | http://loinc.org |
| 85 | 637 | Observation | `Observation.interpretation.coding` | L | Low | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 86 | 641 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 87 | 656 | Observation | `Observation.code.coding` | 2085-9 | Cholesterol in HDL [Mass/volume] in Serum or Plasma | http://loinc.org |
| 88 | 659 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 89 | 663 | Observation | `Observation.interpretation.coding` | H | High | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 90 | 678 | Observation | `Observation.code.coding` | 2571-8 | Triglyceride [Mass/volume] in Serum or Plasma | http://loinc.org |
| 91 | 681 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 92 | 685 | Observation | `Observation.interpretation.coding` | H | High | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 93 | 700 | Observation | `Observation.code.coding` | 100898-6 | Lipid panel - Serum or Plasma | http://loinc.org |
| 94 | 701 | Observation | `Observation.valueCodeableConcept.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 95 | 702 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 96 | 703 | Observation | `Observation.valueCodeableConcept.coding` | 370992007.0 | Dyslipidemia | http://snomed.info/sct |
| 97 | 704 | Observation | `Observation.interpretation.coding` | 370992007.0 | Dyslipidemia | http://snomed.info/sct |
| 98 | 718 | Observation | `Observation.code.coding` | OC000173 | Prediksi Risiko PTM tanpa Pemeriksaan Laboratorium | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 99 | 719 | Observation | `Observation.interpretation.coding` | 723505004.0 | Low risk | http://snomed.info/sct |
| 100 | 722 | Observation | `Observation.interpretation.coding` | 25594002.0 | Moderate risk of | http://snomed.info/sct |
| 101 | 727 | Observation | `Observation.interpretation.coding` | 723509005.0 | High risk | http://snomed.info/sct |
| 102 | 743 | Observation | `Observation.code.coding` | 20977-5 | Urea [Mass/volume] in Blood | http://loinc.org |
| 103 | 744 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 104 | 749 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 105 | 763 | Observation | `Observation.code.coding` | 2160-0 | Creatinine [Mass/volume] in Serum or Plasma | http://loinc.org |
| 106 | 764 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 107 | 769 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 108 | 783 | Observation | `Observation.code.coding` | 62238-1 | Glomerular filtration rate/1.73 sq M.predicted [Volume Rate/Area] in Serum, Plasma or Blood by Creatinine-based formula (CKD-EPI) | http://loinc.org |
| 109 | 784 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 110 | 787 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 111 | 838 | Procedure | `Procedure.code.coding` | 424489006.0 | Mantoux test | http://snomed.info/sct |
| 112 | 850 | Observation | `Observation.code.coding` | 23539-0 | Tuberculosis reaction wheal [Diameter] --3 days post dose mammalian tuberculin intradermal | http://loinc.org |
| 113 | 851 | Observation | `Observation.valueCodeableConcept.coding` | 268376005.0 | Mantoux: positive | http://snomed.info/sct |
| 114 | 852 | Observation | `Observation.valueCodeableConcept.coding` | 268375009.0 | Mantoux: negative | http://snomed.info/sct |
| 115 | 862 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | TK000161 | Dugaan Tuberkulosis klinis | http://terminology.kemkes.go.id |
| 116 | 870 | Observation | `Observation.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 117 | 871 | Observation | `Observation.method.coding` | 391483001.0 | Microscopy (acid fast bacilli) | http://snomed.info/sct |
| 118 | 872 | Observation | `Observation.valueCodeableConcept.coding` | 10828004.0 | Positive | http://snomed.info/sct |
| 119 | 873 | Observation | `Observation.valueCodeableConcept.coding` | 260385009.0 | Negative | http://snomed.info/sct |
| 120 | 885 | Observation | `Observation.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 121 | 886 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 122 | 887 | Observation | `Observation.dataAbsentReason.coding` | OD000001 | Tidak ada hasil | http://terminology.kemkes.go.id/CodeSystem/data-absent-reason |
| 123 | 899 | Observation | `Observation.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 124 | 900 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 125 | 901 | Observation | `Observation.dataAbsentReason.coding` | LA15841-2 | Invalid | http://loinc.org |
| 126 | 913 | Observation | `Observation.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 127 | 914 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 128 | 915 | Observation | `Observation.dataAbsentReason.coding` | error | Error | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 129 | 927 | Observation | `Observation.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 130 | 928 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 131 | 929 | Observation | `Observation.dataAbsentReason.coding` | OD000001 | Tidak ada hasil | http://terminology.kemkes.go.id/CodeSystem/data-absent-reason |
| 132 | 941 | Observation | `Observation.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 133 | 942 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 134 | 943 | Observation | `Observation.valueCodeableConcept.coding` | LA11883-8 | Not Detected | http://loinc.org |
| 135 | 944 | Observation | `Observation.interpretation.coding` | NEG | Negative | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 136 | 956 | Observation | `Observation.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 137 | 957 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 138 | 958 | Observation | `Observation.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 139 | 959 | Observation | `Observation.interpretation.coding` | NEG | Negative | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 140 | 971 | Observation | `Observation.code.coding` | 89372-7 | Mycobacterium tuberculosis complex rpoB gene rifAMPin resistance mutation [Presence] by Molecular method | http://loinc.org |
| 141 | 972 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 142 | 973 | Observation | `Observation.valueCodeableConcept.coding` | LA11883-8 | Not Detected | http://loinc.org |
| 143 | 974 | Observation | `Observation.interpretation.coding` | X099770 | Rifampisin sensitive | http://terminology.kemkes.go.id/CodeSystem/examination |
| 144 | 986 | Observation | `Observation.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 145 | 987 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 146 | 988 | Observation | `Observation.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 147 | 989 | Observation | `Observation.interpretation.coding` | NEG | Negative | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 148 | 1001 | Observation | `Observation.code.coding` | 89372-7 | Mycobacterium tuberculosis complex rpoB gene rifAMPin resistance mutation [Presence] by Molecular method | http://loinc.org |
| 149 | 1002 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 150 | 1003 | Observation | `Observation.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 151 | 1004 | Observation | `Observation.interpretation.coding` | X099771 | Rifampisin resistan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 152 | 1016 | Observation | `Observation.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 153 | 1017 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 154 | 1018 | Observation | `Observation.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 155 | 1019 | Observation | `Observation.interpretation.coding` | NEG | Negative | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 156 | 1031 | Observation | `Observation.code.coding` | 89372-7 | Mycobacterium tuberculosis complex rpoB gene rifAMPin resistance mutation [Presence] by Molecular method | http://loinc.org |
| 157 | 1032 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 158 | 1033 | Observation | `Observation.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 159 | 1034 | Observation | `Observation.interpretation.coding` | X099772 | Rifampisin indeterminate | http://terminology.kemkes.go.id/CodeSystem/examination |
| 160 | 1046 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | female | Female | http://hl7.org/fhir/administrative-gender |
| 161 | 1047 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | male | Male | http://hl7.org/fhir/administrative-gender |
| 162 | 1059 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | SP000435 | <20 bungkus per tahun | http://terminology.kemkes.go.id/sp |
| 163 | 1060 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | SP000436 | 20-30 bungkus per tahun | http://terminology.kemkes.go.id/sp |
| 164 | 1061 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | SP000437 | >30 bungkus per tahun | http://terminology.kemkes.go.id/sp |
| 165 | 1080 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | 723505004.0 | Low risk | http://snomed.info/sct |
| 166 | 1081 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | 723509005.0 | High risk | http://snomed.info/sct |
| 167 | 1104 | Observation | `Observation.code.coding` | 13607009.0 | Manual examination of breast | http://snomed.info/sct |
| 168 | 1112 | Observation | `Observation.valueCodeableConcept.coding` | 290084006.0 | Breast normal | http://snomed.info/sct |
| 169 | 1113 | Observation | `Observation.valueCodeableConcept.coding` | 89164003.0 | Breast lump | http://snomed.info/sct |
| 170 | 1114 | Observation | `Observation.valueCodeableConcept.coding` | 134405005.0 | Suspected breast cancer | http://snomed.info/sct |
| 171 | 1121 | Observation | `Observation.code.coding` | 24601-7 | US Breast | http://loinc.org |
| 172 | 1129 | Observation | `Observation.valueCodeableConcept.coding` | 290084006.0 | Breast normal | http://snomed.info/sct |
| 173 | 1130 | Observation | `Observation.valueCodeableConcept.coding` | 367644007.0 | Simple cyst | http://snomed.info/sct |
| 174 | 1131 | Observation | `Observation.valueCodeableConcept.coding` | 449837001.0 | Complex cyst of breast | http://snomed.info/sct |
| 175 | 1146 | Observation | `Observation.code.coding` | 451024007.0 | Inspection of vagina using vaginal speculum | http://snomed.info/sct |
| 176 | 1154 | Observation | `Observation.valueCodeableConcept.coding` | 395100000.0 | No evidence of cancer found | http://snomed.info/sct |
| 177 | 1155 | Observation | `Observation.valueCodeableConcept.coding` | 315266007.0 | Suspected cervical cancer | http://snomed.info/sct |
| 178 | 1162 | Observation | `Observation.code.coding` | X099241 | Tes IVA | http://terminology.kemkes.go.id/CodeSystem/examination |
| 179 | 1170 | Observation | `Observation.valueCodeableConcept.coding` | 300557001.0 | Aceto-white reaction positive | http://snomed.info/sct |
| 180 | 1171 | Observation | `Observation.valueCodeableConcept.coding` | 300558006.0 | Aceto-white reaction negative | http://snomed.info/sct |
| 181 | 1178 | Observation | `Observation.code.coding` | 44550-2 | Human papilloma virus DNA [Presence] in Cervix by Probe | http://loinc.org |
| 182 | 1186 | Observation | `Observation.valueCodeableConcept.coding` | 787724008.0 | Human papillomavirus deoxyribonucleic acid not detected | http://snomed.info/sct |
| 183 | 1187 | Observation | `Observation.valueCodeableConcept.coding` | 787723002.0 | Human papillomavirus deoxyribonucleic acid detected | http://snomed.info/sct |
| 184 | 1188 | Observation | `Observation.valueCodeableConcept.coding` | OV000351 | Positif (HPV tipe onkogenik lain) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 185 | 1189 | Observation | `Observation.valueCodeableConcept.coding` | 708311006.0 | Deoxyribonucleic acid of Human papillomavirus 52 | http://snomed.info/sct |
| 186 | 1190 | Observation | `Observation.valueCodeableConcept.coding` | 708299006.0 | Deoxyribonucleic acid of Human papillomavirus 18 | http://snomed.info/sct |
| 187 | 1191 | Observation | `Observation.valueCodeableConcept.coding` | 708298003.0 | Deoxyribonucleic acid of Human papillomavirus 16 | http://snomed.info/sct |
| 188 | 1198 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | female | Female | http://hl7.org/fhir/administrative-gender |
| 189 | 1199 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | male | Male | http://hl7.org/fhir/administrative-gender |
| 190 | 1202 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | SP000438 | <45 thn | http://terminology.kemkes.go.id/sp |
| 191 | 1203 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | SP000439 | 45-65 thn | http://terminology.kemkes.go.id/sp |
| 192 | 1204 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | SP000440 | >65 tahun | http://terminology.kemkes.go.id/sp |
| 193 | 1207 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | QRI000032 | Memiliki diagnosis kanker >5 tahun yang lalu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 194 | 1208 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | QRI000033 | Memiliki diagnosis kanker <5 tahun yang lalu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 195 | 1209 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | QRI000034 | Tidak pernah didiagnosis menderita kanker | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 196 | 1212 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | QRI000036 | Tidak ada keluarga yang terdiagnosis kanker | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 197 | 1213 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 429011007.0 | Family history of malignant neoplasm of lung | http://snomed.info/sct |
| 198 | 1214 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | QRI000035 | Memiliki keluarga yang terdiagnosis kanker lain | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 199 | 1217 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | QRI000023 | Perokok/bekas perokok berhenti <10 tahun lalu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 200 | 1218 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | QRI000022 | Perokok aktif (dalam 1 tahun ini masih merokok) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 201 | 1219 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 266919005.0 | Never smoked tobacco | http://snomed.info/sct |
| 202 | 1220 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 16090771000119104 | Occupational exposure to environmental tobacco smoke | http://snomed.info/sct |
| 203 | 1223 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | QRI000019 | Tidak memiliki tempat kerja mengandung zat karsinogenik | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 204 | 1224 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | QRI000018 | Tidak yakin memiliki tempat kerja mengandung zat karsinogenik | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 205 | 1225 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | QRI000017 | Memiliki tempat kerja mengandung zat karsinogenik | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 206 | 1228 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | QRI000024 | Memiliki tempat tinggal berpotensi tinggi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 207 | 1229 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | QRI000026 | Tidak memiliki tempat tinggal berpotensi tinggi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 208 | 1230 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | QRI000025 | Tidak yakin memiliki tempat tinggal berpotensi tinggi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 209 | 1233 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | QRI000029 | Memiliki lingkungan dalam rumah yang sehat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 210 | 1234 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | QRI000028 | Tidak yakin memiliki lingkungan dalam rumah yang tidak sehat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 211 | 1235 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | QRI000027 | Memiliki lingkungan dalam rumah yang tidak sehat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 212 | 1238 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 161414005.0 | History of tuberculosis | http://snomed.info/sct |
| 213 | 1239 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 414415007.0 | History of chronic lung disease | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 214 | 1240 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 160258000.0 | No history of respiratory system disease | http://snomed.info/sct |
| 215 | 1243 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 723505004.0 | Low risk | http://snomed.info/sct |
| 216 | 1244 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 25594002.0 | Moderate risk of | http://snomed.info/sct |
| 217 | 1245 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 723509005.0 | High risk | http://snomed.info/sct |
| 218 | 1248 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 17621005.0 | Normal | http://snomed.info/sct |
| 219 | 1249 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 263654008 | Abnormal | http://snomed.info/sct |
| 220 | 1256 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | female | Female | http://hl7.org/fhir/administrative-gender |
| 221 | 1257 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | male | Male | http://hl7.org/fhir/administrative-gender |
| 222 | 1260 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | SP000441 | <50 tahun | http://terminology.kemkes.go.id/sp |
| 223 | 1261 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | SP000442 | 50 - 69 tahun | http://terminology.kemkes.go.id/sp |
| 224 | 1262 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | SP000443 | >= 70 tahun | http://terminology.kemkes.go.id/sp |
| 225 | 1273 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 723505004.0 | Low risk | http://snomed.info/sct |
| 226 | 1274 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 25594002.0 | Moderate risk of | http://snomed.info/sct |
| 227 | 1275 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 723509005.0 | High risk | http://snomed.info/sct |
| 228 | 1290 | Observation | `Observation.code.coding` | 410007005.0 | Rectal examination | http://snomed.info/sct |
| 229 | 1298 | Observation | `Observation.valueCodeableConcept.coding` | 248523006.0 | Rectal mass | http://snomed.info/sct |
| 230 | 1299 | Observation | `Observation.valueCodeableConcept.coding` | 300870000.0 | No mass present | http://snomed.info/sct |
| 231 | 1306 | Observation | `Observation.code.coding` | 14563-1 | Hemoglobin.gastrointestinal [Presence] in Stool --1st specimen | http://loinc.org |
| 232 | 1314 | Observation | `Observation.valueCodeableConcept.coding` | 167667006.0 | Occult blood not detected in feces | http://snomed.info/sct |
| 233 | 1315 | Observation | `Observation.valueCodeableConcept.coding` | 59614000.0 | Occult blood detected in feces | http://snomed.info/sct |
| 234 | 1326 | Observation | `Observation.code.coding` | 247301006.0 | Finding of ability to hear whisper | http://snomed.info/sct |
| 235 | 1334 | Observation | `Observation.valueCodeableConcept.coding` | 275727004.0 | Hearing test normal | http://snomed.info/sct |
| 236 | 1335 | Observation | `Observation.valueCodeableConcept.coding` | 300221005.0 | Hearing for whisper impaired | http://snomed.info/sct |
| 237 | 1342 | Observation | `Observation.code.coding` | 76517002.0 | Otoscopy | http://snomed.info/sct |
| 238 | 1350 | Observation | `Observation.valueCodeableConcept.coding` | 275727004.0 | Hearing test normal | http://snomed.info/sct |
| 239 | 1351 | Observation | `Observation.valueCodeableConcept.coding` | 300221005.0 | Hearing for whisper impaired | http://snomed.info/sct |
| 240 | 1358 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.answer.valueCoding` | 400911007.0 | Tumbling E test | http://snomed.info/sct |
| 241 | 1359 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.answer.valueCoding` | 252973004.0 | Snellen chart assessment | http://snomed.info/sct |
| 242 | 1365 | Observation | `Observation.code.coding` | 400911007.0 | Tumbling E test | http://snomed.info/sct |
| 243 | 1366 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 244 | 1367 | Observation | `Observation.valueCodeableConcept.coding` | 45089002.0 | Normal vision | http://snomed.info/sct |
| 245 | 1368 | Observation | `Observation.interpretation.coding` | 45089002.0 | Normal vision | http://snomed.info/sct |
| 246 | 1369 | Observation | `Observation.valueCodeableConcept.coding` | 397540003.0 | Visual impairment | http://snomed.info/sct |
| 247 | 1370 | Observation | `Observation.interpretation.coding` | 397540003.0 | Visual impairment | http://snomed.info/sct |
| 248 | 1381 | Observation | `Observation.code.coding` | 252973004.0 | Snellen chart assessment | http://snomed.info/sct |
| 249 | 1382 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 250 | 1383 | Observation | `Observation.valueCodeableConcept.coding` | 45089002.0 | Normal vision | http://snomed.info/sct |
| 251 | 1384 | Observation | `Observation.interpretation.coding` | 45089002.0 | Normal vision | http://snomed.info/sct |
| 252 | 1385 | Observation | `Observation.valueCodeableConcept.coding` | 397540003.0 | Visual impairment | http://snomed.info/sct |
| 253 | 1386 | Observation | `Observation.interpretation.coding` | 397540003.0 | Visual impairment | http://snomed.info/sct |
| 254 | 1400 | Observation | `Observation.code.coding` | 441841000.0 | Pinhole visual acuity test | http://loinc.org |
| 255 | 1401 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 256 | 1402 | Observation | `Observation.valueCodeableConcept.coding` | 39021009.0 | Disorder of refraction | http://snomed.info/sct |
| 257 | 1403 | Observation | `Observation.interpretation.coding` | 39021009.0 | Disorder of refraction | http://snomed.info/sct |
| 258 | 1404 | Observation | `Observation.valueCodeableConcept.coding` | OI000044 | Kelainan organik | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 259 | 1405 | Observation | `Observation.interpretation.coding` | OI000044 | Kelainan organik | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 260 | 1419 | Observation | `Observation.code.coding` | 40137007.0 | Pupil light reflex | http://snomed.info/sct |
| 261 | 1420 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 262 | 1421 | Observation | `Observation.valueCodeableConcept.coding` | OV000393 | Suspek katarak | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 263 | 1422 | Observation | `Observation.valueCodeableConcept.coding` | 371405004.0 | Disorder of eye proper | http://snomed.info/sct |
| 264 | 1437 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.answer.valueCoding` | TK000147 | Tidak sama sekali | http://terminology.kemkes.go.id |
| 265 | 1438 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.answer.valueCoding` | TK000148 | Kurang dari satu minggu | http://terminology.kemkes.go.id |
| 266 | 1439 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.answer.valueCoding` | TK000149 | Lebih dari satu minggu | http://terminology.kemkes.go.id |
| 267 | 1440 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.answer.valueCoding` | TK000150 | Hampir setiap hari | http://terminology.kemkes.go.id |
| 268 | 1443 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.answer.valueCoding` | TK000147 | Tidak sama sekali | http://terminology.kemkes.go.id |
| 269 | 1444 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.answer.valueCoding` | TK000148 | Kurang dari satu minggu | http://terminology.kemkes.go.id |
| 270 | 1445 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.answer.valueCoding` | TK000149 | Lebih dari satu minggu | http://terminology.kemkes.go.id |
| 271 | 1446 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.answer.valueCoding` | TK000150 | Hampir setiap hari | http://terminology.kemkes.go.id |
| 272 | 1449 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.answer.valueCoding` | TK000147 | Tidak sama sekali | http://terminology.kemkes.go.id |
| 273 | 1450 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.answer.valueCoding` | TK000148 | Kurang dari satu minggu | http://terminology.kemkes.go.id |
| 274 | 1451 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.answer.valueCoding` | TK000149 | Lebih dari satu minggu | http://terminology.kemkes.go.id |
| 275 | 1452 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.answer.valueCoding` | TK000150 | Hampir setiap hari | http://terminology.kemkes.go.id |
| 276 | 1455 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.answer.valueCoding` | TK000147 | Tidak sama sekali | http://terminology.kemkes.go.id |
| 277 | 1456 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.answer.valueCoding` | TK000148 | Kurang dari satu minggu | http://terminology.kemkes.go.id |
| 278 | 1457 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.answer.valueCoding` | TK000149 | Lebih dari satu minggu | http://terminology.kemkes.go.id |
| 279 | 1458 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.answer.valueCoding` | TK000150 | Hampir setiap hari | http://terminology.kemkes.go.id |
| 280 | 1508 | Observation | `Observation.code.coding` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 281 | 1509 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 282 | 1510 | Observation | `Observation.valueCodeableConcept.coding` | 11214006.0 | Reactive | http://snomed.info/sct |
| 283 | 1511 | Observation | `Observation.valueCodeableConcept.coding` | 131194007.0 | Non-Reactive | http://snomed.info/sct |
| 284 | 1524 | Observation | `Observation.code.coding` | 72376-7 | Hepatitis C virus Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 285 | 1525 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 286 | 1526 | Observation | `Observation.valueCodeableConcept.coding` | 11214006.0 | Reactive | http://snomed.info/sct |
| 287 | 1527 | Observation | `Observation.valueCodeableConcept.coding` | 131194007.0 | Non-Reactive | http://snomed.info/sct |
| 288 | 1560 | Observation | `Observation.code.coding` | 1920-8 | Aspartate aminotransferase [Enzymatic activity/volume] in Serum or Plasma | http://loinc.org |
| 289 | 1561 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 290 | 1577 | Observation | `Observation.code.coding[x]` | 26515-7 | Platelets [#/volume] in Blood | http://loinc.org |
| 291 | 1593 | Observation | `Observation.code.coding[x]` | 86465-2 | AST to platelet ratio index in Serum and Blood by calculation | http://loinc.org |
| 292 | 1597 | Observation | `Observation.interpretation.coding` | N | Normal | http://termi nology.hl7. org/CodeSy stem/v3-Ob servationIn terpretation |
| 293 | 1602 | Observation | `Observation.interpretation.coding` | 112674009.0 | Fibrosis | http://snomed.info/sct |
| 294 | 1605 | Observation | `Observation.interpretation.coding` | 19943007.0 | Cirrhosis of liver | http://snomed.info/sct |
| 295 | 1615 | Observation | `Observation.code.coding` | TK000144 | Rencana menikah 1 tahun ke depan | http://terminology.kemkes.go.id |
| 296 | 1640 | Observation | `Observation.code.coding` | 30352-9 | Hemoglobin [Mass/volume] in Capillary blood | http://loinc.org |
| 297 | 1648 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 298 | 1651 | Observation | `Observation.interpretation.coding` | 271737000.0 | Anemia | http://snomed.info/sct |
| 299 | 1665 | Observation | `Observation.code.coding` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 300 | 1666 | Observation | `Observation.valueCodeableConcept.coding` | LA15255-5 | Reactive | http://loinc.org |
| 301 | 1667 | Observation | `Observation.valueCodeableConcept.coding` | LA15256-3 | Nonreactive | http://loinc.org |
| 302 | 1686 | Observation | `Observation.code.coding` | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 303 | 1687 | Observation | `Observation.valueCodeableConcept.coding` | LA15255-5 | Reactive | http://loinc.org |
| 304 | 1688 | Observation | `Observation.valueCodeableConcept.coding` | LA15256-3 | Nonreactive | http://loinc.org |
| 305 | 1713 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000169 | Benar semua kata | http://terminology.kemkes.go.id |
| 306 | 1714 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000444 | Salah satu/Dua | http://terminology.kemkes.go.id/sp |
| 307 | 1715 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000170 | Tidak dapat mengingat/mengulang kata | http://terminology.kemkes.go.id |
| 308 | 1723 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 38369006.0 | At increased risk for cognitive impairment | http://snomed.info/sct |
| 309 | 1724 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000173 | Kemungkinan tidak ada gangguan kognitif | http://terminology.kemkes.go.id |
| 310 | 1746 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 129845004.0 | At risk for malnutrition | http://snomed.info/sct |
| 311 | 1747 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 248324001.0 | Well nourished | http://snomed.info/sct |
| 312 | 1760 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000197 | Kemungkinan depresi | http://terminology.kemkes.go.id |
| 313 | 1761 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000196 | Tidak depresi | http://terminology.kemkes.go.id |
| 314 | 1764 | Observation | `Observation.code.coding` | 48542-5 | Geriatric depression scale (GDS) panel | http://loinc.org |
| 315 | 1765 | Observation | `Observation.interpretation.coding` | TK000196 | Tidak depresi | http://terminology.kemkes.go.id |
| 316 | 1768 | Observation | `Observation.interpretation.coding` | TK000197 | Kemungkinan depresi | http://terminology.kemkes.go.id |
| 317 | 1771 | Observation | `Observation.interpretation.coding` | 35489007.0 | Depression | http://snomed.info/sct |
| 318 | 1783 | Observation | `Observation.component.code.coding` | 48512-8 | Are you basically satisfied with your life [GDS] | http://loinc.org |
| 319 | 1786 | Observation | `Observation.component.code.coding` | 48515-1 | Do you often get bored [GDS] | http://loinc.org |
| 320 | 1789 | Observation | `Observation.component.code.coding` | 48521-9 | Do you often feel helpless [GDS] | http://loinc.org |
| 321 | 1792 | Observation | `Observation.component.code.coding` | 48528-4 | Do you feel pretty worthless the way you are now [GDS] | http://loinc.org |
| 322 | 1797 | Observation | `Observation.code.coding` | 96762-0 | Barthel index panel | http://loinc.org |
| 323 | 1798 | Observation | `Observation.interpretation.coding` | OI000048 | Ketergantungan total | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 324 | 1803 | Observation | `Observation.interpretation.coding` | OI000047 | Ketergantungan berat | http://snomed.info/sct |
| 325 | 1808 | Observation | `Observation.interpretation.coding` | OI000046 | Ketergantungan sedang | http://snomed.info/sct |
| 326 | 1813 | Observation | `Observation.interpretation.coding` | OI000045 | Ketergantungan ringan | http://snomed.info/sct |
| 327 | 1818 | Observation | `Observation.interpretation.coding` | 371153006.0 | Independent | http://snomed.info/sct |
| 328 | 1828 | Observation | `Observation.component.code.coding` | 96759-6 | Bowels | http://loinc.org |
| 329 | 1829 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31627-5 | Incontinent (or needs to be given enemas) | http://loinc.org |
| 330 | 1830 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31626-7 | Occasional accident | http://loinc.org |
| 331 | 1831 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31625-9 | Continent | http://loinc.org |
| 332 | 1832 | Observation | `Observation.component.code.coding` | 96760-4 | Bladder | http://loinc.org |
| 333 | 1833 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31628-3 | Incontinent, or catheterized and unable to manage alone | http://loinc.org |
| 334 | 1834 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31626-7 | Occasional accident | http://loinc.org |
| 335 | 1835 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31625-9 | Continent | http://loinc.org |
| 336 | 1836 | Observation | `Observation.component.code.coding` | 96767-9 | Grooming | http://loinc.org |
| 337 | 1837 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31643-2 | Needs help with personal care | http://loinc.org |
| 338 | 1838 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31644-0 | Independent face/hair/teeth/shaving (implements provided) | http://loinc.org |
| 339 | 1839 | Observation | `Observation.component.code.coding` | 83183-4 | Toilet Use | http://loinc.org |
| 340 | 1840 | Observation | `Observation.component.valueCodeableConcept.coding` | LA12304-4 | Dependent | http://loinc.org |
| 341 | 1841 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31631-7 | Needs some help, but can do something alone | http://loinc.org |
| 342 | 1842 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31632-5 | Independent (on and off, dressing, wiping) | http://loinc.org |
| 343 | 1843 | Observation | `Observation.component.code.coding` | 83184-2 | Feeding | http://loinc.org |
| 344 | 1844 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24937-7 | Unable | http://loinc.org |
| 345 | 1845 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31630-9 | Needs help cutting, spreading butter, etc., or requires modified diet | http://loinc.org |
| 346 | 1846 | Observation | `Observation.component.valueCodeableConcept.coding` | LA12302-8 | Independent | http://loinc.org |
| 347 | 1847 | Observation | `Observation.component.code.coding` | 83185-9 | Transfer | http://loinc.org |
| 348 | 1848 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31633-3 | Unable, no sitting balance | http://loinc.org |
| 349 | 1849 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31634-1 | Major help (one or two people, physical), can sit | http://loinc.org |
| 350 | 1850 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31635-8 | Minor help (verbal or physical) | http://loinc.org |
| 351 | 1851 | Observation | `Observation.component.valueCodeableConcept.coding` | LA12302-8 | Independent | http://loinc.org |
| 352 | 1852 | Observation | `Observation.component.code.coding` | 83186-7 | Mobility | http://loinc.org |
| 353 | 1853 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31639-0 | Immobile or <50 yards | http://loinc.org |
| 354 | 1854 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31640-8 | Wheelchair independent, including corners, >50 yards | http://loinc.org |
| 355 | 1855 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31641-6 | Walks with help of one person (verbal or physical) >50 yards | http://loinc.org |
| 356 | 1856 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31642-4 | Independent (but may use any aid; for example, stick) >50 yards | http://loinc.org |
| 357 | 1857 | Observation | `Observation.component.code.coding` | 83182-6 | Dressing | http://loinc.org |
| 358 | 1858 | Observation | `Observation.component.valueCodeableConcept.coding` | LA12304-4 | Dependent | http://loinc.org |
| 359 | 1859 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31637-4 | Needs help but can do about half unaided | http://loinc.org |
| 360 | 1860 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31638-2 | Independent (including buttons, zips, laces, etc.) | http://loinc.org |
| 361 | 1861 | Observation | `Observation.component.code.coding` | 96758-8 | Stairs | http://loinc.org |
| 362 | 1862 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24937-7 | Unable | http://loinc.org |
| 363 | 1863 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31629-1 | Needs help (verbal, physical, carrying aid) | http://loinc.org |
| 364 | 1864 | Observation | `Observation.component.valueCodeableConcept.coding` | LA12302-8 | Independent | http://loinc.org |
| 365 | 1865 | Observation | `Observation.component.code.coding` | 83181-8 | Bathing | http://loinc.org |
| 366 | 1866 | Observation | `Observation.component.valueCodeableConcept.coding` | LA12304-4 | Dependent | http://loinc.org |
| 367 | 1867 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31636-6 | Independent (or in shower) | http://loinc.org |
| 368 | 1870 | Observation | `Observation.code.coding` | 72234-8 | Mini-Cog | http://loinc.org |
| 369 | 1871 | Observation | `Observation.valueCodeableConcept.coding` | TK000167 | Benar 1 kata | http://terminology.kemkes.go.id |
| 370 | 1872 | Observation | `Observation.valueCodeableConcept.coding` | TK000168 | Benar 2 kata | http://terminology.kemkes.go.id |
| 371 | 1873 | Observation | `Observation.valueCodeableConcept.coding` | TK000169 | Benar semua kata | http://terminology.kemkes.go.id |
| 372 | 1874 | Observation | `Observation.valueCodeableConcept.coding` | TK000170 | Tidak dapat mengingat/mengulang kata | http://terminology.kemkes.go.id |
| 373 | 1885 | Observation | `Observation.code.coding` | 79150-9 | Clock drawing panel [GPCOG] | http://loinc.org |
| 374 | 1886 | Observation | `Observation.component.code.coding` | 79106-1 | Please mark in all the numbers to indicate the hours of a clock | http://loinc.org |
| 375 | 1887 | Observation | `Observation.component.code.coding` | 79107-9 | Please mark in hands to show 10 minutes past eleven o'clock (11:10) | http://loinc.org |
| 376 | 1891 | Observation | `Observation.interpretation.coding` | TK000171 | Gambar jam benar/tepat | http://terminology.kemkes.go.id |
| 377 | 1892 | Observation | `Observation.interpretation.coding` | TK000172 | Gambar jam salah/tidak tepat | http://terminology.kemkes.go.id |
| 378 | 1902 | Observation | `Observation.code.coding` | 72233-0 | Total score [Mini-Cog] | http://loinc.org |
| 379 | 1905 | Observation | `Observation.interpretation.coding` | 38369006.0 | At increased risk for cognitive impairment | http://snomed.info/sct |
| 380 | 1906 | Observation | `Observation.interpretation.coding` | TK000173 | Kemungkinan tidak ada gangguan kognitif | http://terminology.kemkes.go.id |
| 381 | 1925 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 263703002.0 | Changed | http://snomed.info/sct |
| 382 | 1926 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 260388006.0 | Unchanged | http://snomed.info/sct |
| 383 | 1927 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 261665006.0 | Unknown | http://snomed.info/sct |
| 384 | 1930 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 263703002.0 | Changed | http://snomed.info/sct |
| 385 | 1931 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 260388006.0 | Unchanged | http://snomed.info/sct |
| 386 | 1932 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 261665006.0 | Unknown | http://snomed.info/sct |
| 387 | 1935 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 263703002.0 | Changed | http://snomed.info/sct |
| 388 | 1936 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 260388006.0 | Unchanged | http://snomed.info/sct |
| 389 | 1937 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 261665006.0 | Unknown | http://snomed.info/sct |
| 390 | 1940 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 263703002.0 | Changed | http://snomed.info/sct |
| 391 | 1941 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 260388006.0 | Unchanged | http://snomed.info/sct |
| 392 | 1942 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 261665006.0 | Unknown | http://snomed.info/sct |
| 393 | 1945 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 263703002.0 | Changed | http://snomed.info/sct |
| 394 | 1946 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 260388006.0 | Unchanged | http://snomed.info/sct |
| 395 | 1947 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 261665006.0 | Unknown | http://snomed.info/sct |
| 396 | 1950 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 263703002.0 | Changed | http://snomed.info/sct |
| 397 | 1951 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 260388006.0 | Unchanged | http://snomed.info/sct |
| 398 | 1952 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 261665006.0 | Unknown | http://snomed.info/sct |
| 399 | 1955 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 263703002.0 | Changed | http://snomed.info/sct |
| 400 | 1956 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 260388006.0 | Unchanged | http://snomed.info/sct |
| 401 | 1957 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 261665006.0 | Unknown | http://snomed.info/sct |
| 402 | 1960 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 263703002.0 | Changed | http://snomed.info/sct |
| 403 | 1961 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 260388006.0 | Unchanged | http://snomed.info/sct |
| 404 | 1962 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 261665006.0 | Unknown | http://snomed.info/sct |
| 405 | 1968 | Observation | `Observation.code.coding` | 71722-3 | Total score [AD8] | http://loinc.org |
| 406 | 1970 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7. org/CodeSystem/v3-Ob servationInterpretatio n |
| 407 | 1971 | Observation | `Observation.interpretation.coding` | 698464007.0 | At risk of dementia | http://snomed.info/sct |
| 408 | 1981 | Observation | `Observation.code.coding` | 66248-6 | Balance test [PhenX] | http://loinc.org |
| 409 | 1982 | Observation | `Observation.component.code.coding` | LA18188-5 | Side by side stand | http://loinc.org |
| 410 | 1983 | Observation | `Observation.component.valueCodeableConcept.coding` | LA15186-2 | Held for 10 sec - 1 point | http://loinc.org |
| 411 | 1984 | Observation | `Observation.component.valueCodeableConcept.coding` | LA15187-0 | Not held for 10 sec - 0 points | http://loinc.org |
| 412 | 1985 | Observation | `Observation.component.valueCodeableConcept.coding` | LA15188-8 | Not attempted - 0 points | http://loinc.org |
| 413 | 1986 | Observation | `Observation.component.code.coding` | LA18189-3 | Semi tandem stand | http://loinc.org |
| 414 | 1987 | Observation | `Observation.component.valueCodeableConcept.coding` | LA15186-2 | Held for 10 sec - 1 point | http://loinc.org |
| 415 | 1988 | Observation | `Observation.component.valueCodeableConcept.coding` | LA15187-0 | Not held for 10 sec - 0 points | http://loinc.org |
| 416 | 1989 | Observation | `Observation.component.valueCodeableConcept.coding` | LA15188-8 | Not attempted - 0 points | http://loinc.org |
| 417 | 1990 | Observation | `Observation.component.code.coding` | LA18190-1 | Tandem stand | http://loinc.org |
| 418 | 1991 | Observation | `Observation.component.valueCodeableConcept.coding` | LA15186-2 | Held for 10 sec - 1 point | http://loinc.org |
| 419 | 1992 | Observation | `Observation.component.valueCodeableConcept.coding` | TK000174 | Bertahan 3 - 9.99 detik | http://terminology.kemkes.go.id |
| 420 | 1993 | Observation | `Observation.component.valueCodeableConcept.coding` | TK000175 | Bertahan <3 detik | http://terminology.kemkes.go.id |
| 421 | 1994 | Observation | `Observation.component.valueCodeableConcept.coding` | LA15188-8 | Not attempted - 0 points | http://loinc.org |
| 422 | 2005 | Observation | `Observation.code.coding` | 714283000.0 | Short Physical Performance Battery | http://snomed.info/sct |
| 423 | 2007 | Observation | `Observation.component.code.coding` | 66258-5 | For 4-Meter Walk | http://loinc.org |
| 424 | 2008 | Observation | `Observation.component.valueCodeableConcept.coding` | LA15201-9 | Time is less than 4.82 sec - 4 points | http://loinc.org |
| 425 | 2009 | Observation | `Observation.component.valueCodeableConcept.coding` | LA15200-1 | Time is 4.82 to 6.20 sec - 3 points | http://loinc.org |
| 426 | 2010 | Observation | `Observation.component.valueCodeableConcept.coding` | LA15199-5 | Time is 6.21 to 8.70 sec - 2 points | http://loinc.org |
| 427 | 2011 | Observation | `Observation.component.valueCodeableConcept.coding` | LA15198-7 | Time is more than 8.70 sec - 1 point | http://loinc.org |
| 428 | 2012 | Observation | `Observation.component.valueCodeableConcept.coding` | 66263-5 | Test not completed | http://loinc.org |
| 429 | 2013 | Observation | `Observation.component.code.coding` | 66264-3 | Safe to stand five times | http://loinc.org |
| 430 | 2014 | Observation | `Observation.component.valueCodeableConcept.coding` | TK000176 | <11.19 detik | http://terminology.kemkes.go.id |
| 431 | 2015 | Observation | `Observation.component.valueCodeableConcept.coding` | TK000177 | 11.2 - 13,69 detik | http://terminology.kemkes.go.id |
| 432 | 2016 | Observation | `Observation.component.valueCodeableConcept.coding` | TK000178 | 13.7 - 16.69 detik | http://terminology.kemkes.go.id |
| 433 | 2017 | Observation | `Observation.component.valueCodeableConcept.coding` | TK000179 | 16.7 - 59.9 detik | http://terminology.kemkes.go.id |
| 434 | 2018 | Observation | `Observation.component.valueCodeableConcept.coding` | 66263-5 | Test not completed | http://loinc.org |
| 435 | 2027 | Observation | `Observation.interpretation.coding` | 160697000.0 | Mobilitas fair | http://snomed.info/sct |
| 436 | 2028 | Observation | `Observation.interpretation.coding` | 82971005.0 | Limited mobility | http://snomed.info/sct |
| 437 | 2042 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 64379006.0 | Decrease in appetite | http://snomed.info/sct |
| 438 | 2043 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 79890006.0 | Loss of appetite | http://snomed.info/sct |
| 439 | 2044 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 161825005.0 | Appetite normal | http://snomed.info/sct |
| 440 | 2047 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000180 | Penurunan BB > 3 kg | http://terminology.kemkes.go.id |
| 441 | 2048 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 261665006.0 | Unknown | http://snomed.info/sct |
| 442 | 2049 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000181 | Penurunan BB antara 1-3 kg | http://terminology.kemkes.go.id |
| 443 | 2050 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000181 | Tidak ada penurunan BB | http://terminology.kemkes.go.id |
| 444 | 2053 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000183 | Harus berbaring di tempat tidur atau menggunakan kursi roda | http://terminology.kemkes.go.id |
| 445 | 2054 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000184 | Bisa bangun dari tempat tidur atau kursi roda, tetapi tidak bisa keluar rumah | http://terminology.kemkes.go.id |
| 446 | 2055 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000185 | Bisa bepergian keluar rumah | http://terminology.kemkes.go.id |
| 447 | 2062 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000186 | Demensia atau depresi berat | http://terminology.kemkes.go.id |
| 448 | 2063 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000187 | Demensia atau kepikunan ringan | http://terminology.kemkes.go.id |
| 449 | 2064 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000188 | Tidak ada masalah psikologis | http://terminology.kemkes.go.id |
| 450 | 2067 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000189 | IMT <19 | http://terminology.kemkes.go.id |
| 451 | 2068 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000190 | IMT 19 -<21 | http://terminology.kemkes.go.id |
| 452 | 2069 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000191 | IMT 21 -<23 | http://terminology.kemkes.go.id |
| 453 | 2070 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000192 | IMT >= 23 | http://terminology.kemkes.go.id |
| 454 | 2076 | Observation | `Observation.code.coding` | 39156-5 | Body mass index (BMI) [Ratio] | http://loinc.org |
| 455 | 2089 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000193 | <31 cm | http://terminology.kemkes.go.id |
| 456 | 2090 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000194 | >= 31 cm | http://terminology.kemkes.go.id |
| 457 | 2096 | Observation | `Observation.code.coding` | 8283-4 | Calf - right Maximum circumference | http://loinc.org |
| 458 | 2097 | Observation | `Observation.code.coding` | 8282-6 | Calf - left Maximum circumference | http://loinc.org |
| 459 | 2112 | Observation | `Observation.code.coding` | TK000195 | Mini Nutritional Assessment (MNA) SF | http://terminology.kemkes.go.id |
| 460 | 2115 | Observation | `Observation.interpretation.coding` | 248324001.0 | Well nourished | http://snomed.info/sct |
| 461 | 2116 | Observation | `Observation.interpretation.coding` | 129845004.0 | At risk for malnutrition | http://snomed.info/sct |
| 462 | 2117 | Observation | `Observation.interpretation.coding` | 2492009.0 | Malnutrition | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 181 |
| http://loinc.org | 132 |
| http://terminology.kemkes.go.id | 57 |
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
| **Total** | **462** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 36 | – | ihs_organization | Organization | `Organization.id` |
| 38 | – | organization_name | Organization | `Organization.name` |
| 39 | – | kabkota_name | Organization | `Organization.address.city` |
| 42 | – | provinsi | Organization | `Organization.address.extension.extension.url` |
| 45 | – | kabkota | Organization | `Organization.address.extension.extension.url` |
| 199 | – | tinggi_badan_cm | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.text` |
| 215 | – | index_massa_tubuh | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.text` |
| 246 | – | lingkar_perut | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.text` |
| 269 | – | apakah_pernah_dinyatakan_tekanan_darah_tinggi | QuestionnaireResponse | `QuestionnaireResponse.item.item.linkId` |
| 275 | – | sistolik | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueReference.reference` |
| 319 | – | diastolik | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueReference.reference` |
| 363 | – | tekanan_darah | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueReference.reference` |
| 387 | – | apakah_pernah_dinyatakan_diabetes_kencing_manis | QuestionnaireResponse | `QuestionnaireResponse.item.item.text` |
| 393 | – | gula_darah_sewaktu | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueReference.display` |
| 455 | – | gula_darah_puasa | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueReference.display` |
| 483 | – | gula_darah_puasa_lanjutan | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueReference.display` |
| 510 | – | gula_darah_2_jam_pp | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueReference.reference` |
| 541 | – | pemeriksaan_hb1ac | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueReference.display` |
| 564 | – | hasil_pemeriksaan_ekg | QuestionnaireResponse | `QuestionnaireResponse.item.item.text` |
| 608 | – | kolesterol_total | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueReference.display` |
| 609 | – | interpretasi_kolesterol_total | – | `` |
| 630 | – | masukkan_nilai_hdl | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueReference.reference` |
| 631 | – | interpretasi_hdl | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueReference.display` |
| 652 | – | masukkan_nilai_ldl | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueReference.reference` |
| 653 | – | interpretasi_ldl | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueReference.display` |
| 674 | – | masukkan_nilai_trigliserida | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueReference.reference` |
| 675 | – | hasil_interpretasi_trigliserida | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueReference.display` |
| 696 | – | hasil_interpretasi_dislipidemia | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueReference.reference` |
| 712 | – | prediksi_risiko_penyakit_kardiovaskular | QuestionnaireResponse | `QuestionnaireResponse.item.item.linkId` |
| 739 | – | hasil_pemeriksaan_ureum | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueReference.reference` |
| 759 | – | hasil_pemeriksaan_kreatinin | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueReference.reference` |
| 779 | – | hasil_pemeriksaan_elfg_ckd_epi | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueReference.reference` |
| 800 | – | hasil_pemeriksaan_gigi_karies | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.text` |
| 804 | – | hasil_pemeriksaan_gigi_hilang_dicabut | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.text` |
| 811 | – | hasil_pemeriksaan_pocket_periodontal | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.text` |
| 815 | – | hasil_pemeriksaan_gigi_goyang | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.text` |
| 822 | – | apakah_mengalami_batuk_lebih_dari_2_minggu | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.linkId` |
| 826 | – | apakah_sering_bertemu_dengan_penderita_tbc | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.linkId` |
| 830 | – | riwayat_kontak_tuberkulosis | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.linkId` |
| 865 | – | metode_pemeriksaan | QuestionnaireResponse | `QuestionnaireResponse.item.item.text` |
| 867 | – | hasil_pemeriksaan_bta | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueReference.display` |
| 882 | – | hasil_pemeriksaan_tb_tcm | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueReference.display` |
| 896 | – | hasil_pemeriksaan_tb_tcm | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueReference.display` |
| 910 | – | hasil_pemeriksaan_tb_tcm | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueReference.display` |
| 924 | – | hasil_pemeriksaan_tb_tcm | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueReference.display` |
| 1048 | – | usia_puma | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.linkId` |
| 1053 | – | apakah_mempunyai_riwayat_merokok | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.linkId` |
| 1057 | – | berapa_bungkus_rokok_dalam_1_tahun | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.linkId` |
| 1062 | – | apakah_pernah_merasa_napas_pendek_saat_jalan_cepat | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.linkId` |
| 1066 | – | apakah_mempunyai_dahak_atau_kesulitan_mengeluarkan_dahak | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.linkId` |
| 1070 | – | apakah_biasanya_batuk_ketika_tidak_menderita_flu | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.linkId` |
| 1074 | – | apakah_pernah_melakukan_spirometri | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.linkId` |
| 1078 | – | hasil_skor_puma | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.linkId` |
| 1089 | – | jenis_pemeriksaan | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.text` |
| 1098 | – | hasil_pemeriksaan_sadanis | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.linkId` |
| 1115 | – | hasil_pemeriksaan_usg_payudara | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.linkId` |
| 1136 | – | apakah_pernah_melakukan_hubungan_intim | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.linkId` |
| 1140 | – | hasil_pemeriksaan_inspekulo | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.linkId` |
| 1156 | – | hasil_pemeriksaan_iva | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.linkId` |
| 1172 | – | hasil_pemeriksaan_hpv | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.linkId` |
| 1197 | – | jenis_kelamin_1 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.text` |
| 1200 | – | usia | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.linkId` |
| 1205 | – | apakah_pernah_didiagnosa_menderita_kanker | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.linkId` |
| 1210 | – | apakah_ada_keluarga_yang_didiagnosa_menderita_kanker | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.linkId` |
| 1215 | – | riwayat_merokok_atau_paparan_asap_rokok | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.linkId` |
| 1221 | – | riwayat_tempat_kerja_mengandung_zat_karsinogenik | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.linkId` |
| 1226 | – | lingkungan_tempat_tinggal_berpotensi_tinggi | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.linkId` |
| 1231 | – | lingkungan_tempat_tinggal_berpotensi_tinggi_1 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.linkId` |
| 1236 | – | apakah_pernah_didiagnosis_penyakit_paru_kronik | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.linkId` |
| 1241 | – | apakah_pernah_didiagnosis_penyakit_paru_kronik_1 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.linkId` |
| 1247 | – | hasil_skrining_kanker_paru | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.text` |
| 1254 | – | jenis_kelamin_apcs | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.linkId` |
| 1258 | – | usia_skor_apcs | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.linkId` |
| 1263 | – | kankes_usus | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.linkId` |
| 1267 | – | riwayat_merokok_apcs | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.linkId` |
| 1271 | – | skor_apcs | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.linkId` |
| 1280 | – | kesediaan_colok_dubur | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.linkId` |
| 1284 | – | hasil_colok_dubur | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.linkId` |
| 1300 | – | hasil_darah_samar | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.linkId` |
| 1320 | – | hasil_pemeriksaan_tajam_pendengaran | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.linkId` |
| 1336 | – | hasil_pemeriksaan_otoskop_penala | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.linkId` |
| 1395 | – | hasil_pemeriksaan_pinhole | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.linkId` |
| 1415 | – | hasil_pemeriksaan_pupil | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.text` |
| 1436 | – | seberapa_sering_tidak_bersemangat_dalam_2_minggu | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.text` |
| 1442 | – | seberapa_sering_merasa_murung_tertekan_putus_asa_dalam_2_minggu | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.text` |
| 1448 | – | seberapa_sering_merasa_gugup_cemas_gelisah_dalam_2_minggu | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.text` |
| 1454 | – | seberapa_sering_merasa_khawatir_dalam_2_minggu | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.text` |
| 1460 | – | gejala_depresi | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.text` |
| 1464 | – | gejala_kecemasan | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.text` |
| 1471 | – | apakah_hasil_hepatitis_b_mendapat_positif | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.linkId` |
| 1475 | – | apakah_memiliki_keluarga_yang_menderita_hepatitis_b | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.linkId` |
| 1479 | – | apakah_pernah_melakukan_hubungan_intim_dengan_bebas | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.linkId` |
| 1483 | – | apakah_pernah_menerima_transfusi_darah | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.linkId` |
| 1487 | – | apakah_pernah_menjalani_cuci_darah | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.linkId` |
| 1491 | – | apakah_pernah_menggunakan_narkoba | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.linkId` |
| 1495 | – | apakah_anda_menderita_hiv | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.linkId` |
| 1499 | – | apakah_anda_mendapat_pengobatan_hepatitis_c_dan_tidak_sembuh | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.linkId` |
| 1503 | – | hasil_rapid_test_hepatitis_b | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.linkId` |
| 1520 | – | hasil_rapid_test_hepatitis_c | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.linkId` |
| 1535 | – | faktor_risiko_hepatitis_b | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.linkId` |
| 1539 | – | faktor_risiko_hepatitis_c | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.linkId` |
| 1543 | – | faktor_risiko_hepatitis | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.linkId` |
| 1551 | – | apakah_hasil_kolestrol_tinggi | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.linkId` |
| 1555 | – | nilai_sgot | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.linkId` |
| 1572 | – | pemeriksaan_trombosit | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.linkId` |
| 1588 | – | hasil_apri_score | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.linkId` |
| 1627 | – | rencana_menikah_dalam_kurun_waktu_1_tahun | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueBoolean` |
| 1628 | – | rencana_menikah_dalam_kurun_waktu_1_tahun | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueBoolean` |
| 1636 | – | hasil_pemeriksaan_rapid_test_hb | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.text` |
| 1661 | – | hasil_pemeriksaan_rapid_test_sifilis | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.text` |
| 1682 | – | hasil_pemeriksaan_rapid_test_hiv | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.text` |
| 2087 | – | lingkar_betis | QuestionnaireResponse | `QuestionnaireResponse.item.item.linkId` |
| 2107 | – | hasil_interpretasi_mnasf | QuestionnaireResponse | `QuestionnaireResponse.item.item.linkId` |
