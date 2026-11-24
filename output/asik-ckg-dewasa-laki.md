# Output Form: ASIK - CKG Dewasa Laki-laki

Sumber: `mapping/phdt-data-dictionary-asik-ckg-dewasa-laki.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-asik-ckg-dewasa-laki.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 61 |
| Code (`jumlah code` = 1) | 202 |
| Code unik (code + CodeSystem) | 111 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 3 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–27 | Patient | – | – | _pasien_name_ → `Patient.name.text` (2, tanpa BQ)<br>_nik_ → `Patient.identifier.value` (5, tanpa BQ)<br>_pasien_id_ → `Patient.identifier.value` (8, tanpa BQ)<br>_jenis_kelamin_ → `Patient.gender` (10, tanpa BQ)<br>_tgl_lahir_ → `Patient.birthDate` (12, tanpa BQ)<br>_no_handphone_ → `Patient.telecom` (13, tanpa BQ)<br>_status_perkawinan_ → `Patient.maritalStatus.coding` (16, tanpa BQ)<br>_kabkota_name_ → `Patient.address.city` (20, tanpa BQ)<br>_provinsi_ → `Patient.address.extension.extension.valueCode` (24, tanpa BQ)<br>_kabkota_ → `Patient.address.extension.extension.valueCode` (27, tanpa BQ) |
| 2 | 66–79 | Encounter | – | – | _tgl_pelayanan_ → `Encounter.identifier` (66, tanpa BQ) |
| 3 | 80–87 | Condition | Z01.8 | Other specified special examinations | – |
| 4 | 98–109 | Observation | 424144002.0 | Current chronological age | _age_now_ → `Observation.valueQuantity.value` (101, tanpa BQ) |
| 5 | 110–121 | Observation | TK000144 | Rencana menikah 1 tahun ke depan | _rencana_menikah_dalam_kurun_waktu_1_tahun_ → `Observation.valueBoolean` (113, tanpa BQ) |
| 6 | 122–179 | QuestionnaireResponse | – | – | _apakah_merokok_dalam_setahun_terakhir_ → `QuestionnaireResponse.item.item.text` (134, tanpa BQ)<br>_sudah_berapa_tahun_merokok_ → `QuestionnaireResponse.item.item.answer.item.text` (138, tanpa BQ)<br>_berapa_batang_rokok_yang_dihisap_dalam_sehari_ → `QuestionnaireResponse.item.item.answer.item.text` (142, tanpa BQ)<br>_apakah_pernah_merokok_sebelumnya_ → `QuestionnaireResponse.item.item.text` (145, tanpa BQ)<br>_berapa_lama_merokok_sebelumnya_ → `QuestionnaireResponse.item.item.answer.item.text` (149, tanpa BQ)<br>_kapan_anda_berhenti_merokok_ → `QuestionnaireResponse.item.item.answer.item.text` (153, tanpa BQ)<br>_apakah_terpapar_asap_rokok_sebulan_terakhir_ → `QuestionnaireResponse.item.item.text` (157, tanpa BQ)<br>_apakah_rutin_melakukan_olahraga_ → `QuestionnaireResponse.item.item.text` (161, tanpa BQ)<br>_berapa_kali_berolahraga_dalam_seminggu_ → `QuestionnaireResponse.item.item.answer.item.text` (165, tanpa BQ)<br>_berapa_menit_berolahraga_ → `QuestionnaireResponse.item.item.answer.item.text` (168, tanpa BQ)<br>_tingkat_aktivitas_fisik_ → `QuestionnaireResponse.item.item.answer.item.linkId` (170, tanpa BQ)<br>_berat_badan_kg_ → `QuestionnaireResponse.item.item.item.text` (177, tanpa BQ)<br>_tinggi_badan_cm_ → `QuestionnaireResponse.item.item.item.text` (193, tanpa BQ)<br>_index_massa_tubuh_ → `QuestionnaireResponse.item.item.item.text` (209, tanpa BQ)<br>_lingkar_perut_ → `QuestionnaireResponse.item.item.item.text` (240, tanpa BQ)<br>_apakah_pernah_dinyatakan_tekanan_darah_tinggi_ → `QuestionnaireResponse.item.item.linkId` (263, tanpa BQ)<br>_sistolik_ → `QuestionnaireResponse.item.item.item.answer.valueReference.reference` (269, tanpa BQ)<br>_diastolik_ → `QuestionnaireResponse.item.item.item.answer.valueReference.reference` (313, tanpa BQ)<br>_tekanan_darah_ → `QuestionnaireResponse.item.item.item.answer.valueReference.reference` (357, tanpa BQ)<br>_apakah_pernah_dinyatakan_diabetes_kencing_manis_ → `QuestionnaireResponse.item.item.text` (381, tanpa BQ)<br>_gula_darah_sewaktu_ → `QuestionnaireResponse.item.item.item.answer.valueReference.display` (387, tanpa BQ)<br>_gula_darah_puasa_ → `QuestionnaireResponse.item.item.item.answer.valueReference.display` (449, tanpa BQ)<br>_gula_darah_puasa_lanjutan_ → `QuestionnaireResponse.item.item.item.answer.valueReference.display` (477, tanpa BQ)<br>_gula_darah_2_jam_pp_ → `QuestionnaireResponse.item.item.item.answer.valueReference.reference` (504, tanpa BQ)<br>_pemeriksaan_hb1ac_ → `QuestionnaireResponse.item.item.item.answer.valueReference.display` (535, tanpa BQ)<br>_hasil_pemeriksaan_ekg_ → `QuestionnaireResponse.item.item.text` (558, tanpa BQ)<br>_kolesterol_total_ → `QuestionnaireResponse.item.item.answer.valueReference.display` (602, tanpa BQ)<br>_masukkan_nilai_hdl_ → `QuestionnaireResponse.item.item.answer.valueReference.reference` (624, tanpa BQ)<br>_interpretasi_hdl_ → `QuestionnaireResponse.item.item.answer.valueReference.display` (625, tanpa BQ)<br>_masukkan_nilai_ldl_ → `QuestionnaireResponse.item.item.answer.valueReference.reference` (646, tanpa BQ)<br>_interpretasi_ldl_ → `QuestionnaireResponse.item.item.answer.valueReference.display` (647, tanpa BQ)<br>_masukkan_nilai_trigliserida_ → `QuestionnaireResponse.item.item.answer.valueReference.reference` (668, tanpa BQ)<br>_interpretasi_trigliserida_ → `QuestionnaireResponse.item.item.answer.valueReference.display` (669, tanpa BQ)<br>_interpretasi_dislipidemia_ → `QuestionnaireResponse.item.item.answer.valueReference.reference` (690, tanpa BQ)<br>_prediksi_risiko_penyakit_kardiovaskular_ → `QuestionnaireResponse.item.item.linkId` (706, tanpa BQ)<br>_hasil_ureum_ → `QuestionnaireResponse.item.item.answer.valueReference.reference` (733, tanpa BQ)<br>_hasil_kreatinin_ → `QuestionnaireResponse.item.item.answer.valueReference.reference` (753, tanpa BQ)<br>_hasil_elfg_ckd_epi_ → `QuestionnaireResponse.item.item.answer.valueReference.reference` (773, tanpa BQ)<br>_hasil_pemeriksaan_gigi_karies_ → `QuestionnaireResponse.item.item.item.text` (794, tanpa BQ)<br>_hasil_pemeriksaan_gigi_hilang_dicabut_ → `QuestionnaireResponse.item.item.item.text` (798, tanpa BQ)<br>_hasil_pemeriksaan_pocket_periodontal_ → `QuestionnaireResponse.item.item.answer.item.text` (805, tanpa BQ)<br>_hasil_pemeriksaan_gigi_goyang_ → `QuestionnaireResponse.item.item.answer.item.text` (809, tanpa BQ)<br>_apakah_mengalami_batuk_lebih_dari_2_minggu_ → `QuestionnaireResponse.item.item.item.linkId` (816, tanpa BQ)<br>_apakah_sering_bertemu_dengan_penderita_tbc_ → `QuestionnaireResponse.item.item.item.linkId` (820, tanpa BQ)<br>_riwayat_kontak_tuberkulosis_ → `QuestionnaireResponse.item.item.item.linkId` (824, tanpa BQ)<br>_metode_pemeriksaan_ → `QuestionnaireResponse.item.item.text` (829, tanpa BQ)<br>_hasil_pemeriksaan_bta_ → `QuestionnaireResponse.item.item.answer.valueReference.display` (831, tanpa BQ)<br>_hasil_pemeriksaan_tb_tcm_ → `QuestionnaireResponse.item.item.answer.valueReference.display` (846, tanpa BQ)<br>_hasil_pemeriksaan_tb_tcm_ → `QuestionnaireResponse.item.item.answer.valueReference.display` (860, tanpa BQ)<br>_hasil_pemeriksaan_tb_tcm_ → `QuestionnaireResponse.item.item.answer.valueReference.display` (874, tanpa BQ)<br>_hasil_pemeriksaan_tb_tcm_ → `QuestionnaireResponse.item.item.answer.valueReference.display` (888, tanpa BQ)<br>_usia_puma_ → `QuestionnaireResponse.item.item.item.linkId` (1012, tanpa BQ)<br>_apakah_mempunyai_riwayat_merokok_ → `QuestionnaireResponse.item.item.item.linkId` (1017, tanpa BQ)<br>_berapa_bungkus_rokok_dalam_1_tahun_ → `QuestionnaireResponse.item.item.item.linkId` (1021, tanpa BQ)<br>_apakah_pernah_merasa_napas_pendek_saat_jalan_cepat_ → `QuestionnaireResponse.item.item.item.linkId` (1026, tanpa BQ)<br>_apakah_mempunyai_dahak_atau_kesulitan_mengeluarkan_dahak_ → `QuestionnaireResponse.item.item.item.linkId` (1030, tanpa BQ)<br>_apakah_biasanya_batuk_ketika_tidak_menderita_flu_ → `QuestionnaireResponse.item.item.item.linkId` (1034, tanpa BQ)<br>_apakah_pernah_melakukan_spirometri_ → `QuestionnaireResponse.item.item.item.linkId` (1038, tanpa BQ)<br>_hasil_skor_puma_ → `QuestionnaireResponse.item.item.item.linkId` (1042, tanpa BQ)<br>_jenis_kelamin_paru_ → `QuestionnaireResponse.item.item.answer.item.text` (1053, tanpa BQ)<br>_usia_paru_ → `QuestionnaireResponse.item.item.item.linkId` (1056, tanpa BQ)<br>_apakah_pernah_didiagnosa_menderita_kanker_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1061, tanpa BQ)<br>_apakah_ada_keluarga_yang_didiagnosa_menderita_kanker_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1066, tanpa BQ)<br>_riwayat_merokok_atau_paparan_asap_rokok_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1071, tanpa BQ)<br>_riwayat_tempat_kerja_mengandung_zat_karsinogenik_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1077, tanpa BQ)<br>_lingkungan_tempat_tinggal_berpotensi_tinggi_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1082, tanpa BQ)<br>_lingkungan_tempat_tinggal_berpotensi_tinggi_1_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1087, tanpa BQ)<br>_apakah_pernah_didiagnosis_penyakit_paru_kronik_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1092, tanpa BQ)<br>_apakah_pernah_didiagnosis_penyakit_paru_kronik_1_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1097, tanpa BQ)<br>_hasil_skrining_kanker_paru_ → `QuestionnaireResponse.item.item.answer.item.text` (1103, tanpa BQ)<br>_jenis_kelamin_apcs_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1110, tanpa BQ)<br>_usia_skor_apcs_ → `QuestionnaireResponse.item.item.item.linkId` (1114, tanpa BQ)<br>_kankes_usus_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1119, tanpa BQ)<br>_riwayat_merokok_apcs_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1123, tanpa BQ)<br>_skor_apcs_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1127, tanpa BQ)<br>_kesediaan_colok_dubur_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1136, tanpa BQ)<br>_hasil_colok_dubur_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1140, tanpa BQ)<br>_hasil_darah_samar_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1156, tanpa BQ)<br>_hasil_pemeriksaan_tajam_pendengaran_ → `QuestionnaireResponse.item.answer.item.linkId` (1176, tanpa BQ)<br>_hasil_pemeriksaan_pinhole_ → `QuestionnaireResponse.item.answer.item.linkId` (1251, tanpa BQ)<br>_hasil_pemeriksaan_pupil_ → `QuestionnaireResponse.item.answer.item.text` (1271, tanpa BQ)<br>_seberapa_sering_tidak_bersemangat_dalam_2_minggu_ → `QuestionnaireResponse.item.answer.item.text` (1292, tanpa BQ)<br>_seberapa_sering_merasa_murung_tertekan_putus_asa_dalam_2_minggu_ → `QuestionnaireResponse.item.answer.item.text` (1298, tanpa BQ)<br>_seberapa_sering_merasa_gugup_cemas_gelisah_dalam_2_minggu_ → `QuestionnaireResponse.item.answer.item.text` (1304, tanpa BQ)<br>_seberapa_sering_merasa_khawatir_dalam_2_minggu_ → `QuestionnaireResponse.item.answer.item.text` (1310, tanpa BQ)<br>_gejala_depresi_ → `QuestionnaireResponse.item.answer.item.text` (1316, tanpa BQ)<br>_gejala_kecemasan_ → `QuestionnaireResponse.item.answer.item.text` (1320, tanpa BQ)<br>_apakah_hasil_hepatitis_b_mendapat_positif_ → `QuestionnaireResponse.item.answer.item.linkId` (1327, tanpa BQ)<br>_apakah_memiliki_keluarga_yang_menderita_hepatitis_b_ → `QuestionnaireResponse.item.answer.item.linkId` (1331, tanpa BQ)<br>_apakah_pernah_melakukan_hubungan_intim_dengan_bebas_ → `QuestionnaireResponse.item.answer.item.linkId` (1335, tanpa BQ)<br>_apakah_pernah_menerima_transfusi_darah_ → `QuestionnaireResponse.item.answer.item.linkId` (1339, tanpa BQ)<br>_apakah_pernah_menjalani_cuci_darah_ → `QuestionnaireResponse.item.answer.item.linkId` (1343, tanpa BQ)<br>_apakah_pernah_menggunakan_narkoba_ → `QuestionnaireResponse.item.answer.item.linkId` (1347, tanpa BQ)<br>_apakah_anda_menderita_hiv_ → `QuestionnaireResponse.item.answer.item.linkId` (1351, tanpa BQ)<br>_apakah_anda_mendapat_pengobatan_hepatitis_c_dan_tidak_sembuh_ → `QuestionnaireResponse.item.answer.item.linkId` (1355, tanpa BQ)<br>_hasil_rapid_test_hepatitis_b_ → `QuestionnaireResponse.item.answer.item.linkId` (1359, tanpa BQ)<br>_hasil_rapid_test_hepatitis_c_ → `QuestionnaireResponse.item.answer.item.linkId` (1376, tanpa BQ)<br>_faktor_risiko_hepatitis_b_ → `QuestionnaireResponse.item.answer.item.linkId` (1391, tanpa BQ)<br>_faktor_risiko_hepatitis_c_ → `QuestionnaireResponse.item.answer.item.linkId` (1395, tanpa BQ)<br>_faktor_risiko_hepatitis_ → `QuestionnaireResponse.item.answer.item.linkId` (1399, tanpa BQ)<br>_apakah_hasil_kolestrol_tinggi_ → `QuestionnaireResponse.item.answer.item.linkId` (1407, tanpa BQ)<br>_nilai_sgot_ → `QuestionnaireResponse.item.answer.item.linkId` (1411, tanpa BQ)<br>_pemeriksaan_trombosit_ → `QuestionnaireResponse.item.answer.item.linkId` (1428, tanpa BQ)<br>_hasil_apri_score_ → `QuestionnaireResponse.item.answer.item.linkId` (1444, tanpa BQ)<br>_rencana_menikah_dalam_kurun_waktu_1_tahun_ → `QuestionnaireResponse.item.answer.valueBoolean` (1483, tanpa BQ)<br>_rencana_menikah_dalam_kurun_waktu_1_tahun_ → `QuestionnaireResponse.item.answer.valueBoolean` (1484, tanpa BQ)<br>_hasil_pemeriksaan_rapid_test_hb_ → `QuestionnaireResponse.item.answer.item.item.text` (1492, tanpa BQ)<br>_hasil_pemeriksaan_rapid_test_sifilis_ → `QuestionnaireResponse.item.answer.item.item.text` (1517, tanpa BQ)<br>_hasil_pemeriksaan_rapid_test_hiv_ → `QuestionnaireResponse.item.answer.item.item.text` (1538, tanpa BQ) |
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
| 45 | 1144–1155 | Observation | 410007005.0 | Rectal examination | – |
| 46 | 1160–1171 | Observation | 14563-1 | Hemoglobin.gastrointestinal [Presence] in Stool --1st specimen | – |
| 47 | 1180–1191 | Observation | 247301006.0 | Finding of ability to hear whisper | – |
| 48 | 1196–1207 | Observation | 76517002.0 | Otoscopy | – |
| 49 | 1219–1234 | Observation | 400911007.0 | Tumbling E test | _pemeriksaan_visus_e_tumbling_ → `Observation.valueCodeableConcept.coding` (1223, tanpa BQ) |
| 50 | 1235–1250 | Observation | 252973004.0 | Snellen chart assessment | _pemeriksaan_visus_snellen_chart_ → `Observation.valueCodeableConcept.coding` (1239, tanpa BQ) |
| 51 | 1254–1269 | Observation | 441841000.0 | Pinhole visual acuity test | – |
| 52 | 1273–1286 | Observation | 40137007.0 | Pupil light reflex | – |
| 53 | 1362–1375 | Observation | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | – |
| 54 | 1378–1390 | Observation | 72376-7 | Hepatitis C virus Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | – |
| 55 | 1414–1427 | Observation | 1920-8 | Aspartate aminotransferase [Enzymatic activity/volume] in Serum or Plasma | – |
| 56 | 1431–1443 | Observation | – | – | – |
| 57 | 1447–1468 | Observation | – | – | – |
| 58 | 1469–1480 | Observation | TK000144 | Rencana menikah 1 tahun ke depan | _rencana_menikah_dalam_kurun_waktu_1_tahun_ → `Observation.valueBoolean` (1472, tanpa BQ) |
| 59 | 1494–1509 | Observation | 30352-9 | Hemoglobin [Mass/volume] in Capillary blood | – |
| 60 | 1519–1530 | Observation | 22464-2 | Reagin Ab [Presence] in Specimen | – |
| 61 | 1540–1551 | Observation | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | – |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 53 |
| Patient | 1 |
| Encounter | 1 |
| Condition | 1 |
| QuestionnaireResponse | 1 |
| ServiceRequest | 1 |
| PractitionerRole | 1 |
| Specimen | 1 |
| DiagnosticReport | 1 |
| **Total** | **61** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 82 | Condition | `Condition.code.coding` | Z01.8 | Other specified special examinations | http://hl7.org/fhir/sid/icd-10 |
| 2 | 100 | Observation | `Observation.code.coding` | 424144002.0 | Current chronological age | http://snomed.info/sct |
| 3 | 112 | Observation | `Observation.code.coding` | TK000144 | Rencana menikah 1 tahun ke depan | http://terminology.kemkes.go.id |
| 4 | 182 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 5 | 198 | Observation | `Observation.code.coding` | 8302-2 | Body height | http://loinc.org |
| 6 | 214 | Observation | `Observation.code.coding` | 39156-5 | Body mass index (BMI) [Ratio] | http://loinc.org |
| 7 | 215 | Observation | `Observation.interpretation.coding` | 248342006.0 | Underweight | http://snomed.info/sct |
| 8 | 218 | Observation | `Observation.interpretation.coding` | 43664005.0 | Normal weight | http://snomed.info/sct |
| 9 | 223 | Observation | `Observation.interpretation.coding` | 238131007.0 | Overweight | http://snomed.info/sct |
| 10 | 228 | Observation | `Observation.interpretation.coding` | 414915002.0 | Obese | http://snomed.info/sct |
| 11 | 245 | Observation | `Observation.code.coding` | vital-signs | Abdominal circumference | http://snomed.info/sct |
| 12 | 255 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 13 | 259 | Observation | `Observation.interpretation.coding` | 248311001.0 | Central obesity | http://snomed.info/sct |
| 14 | 273 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 15 | 283 | Observation | `Observation.interpretation.coding` | OI000040 | Tekanan Darah Optimal | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 16 | 288 | Observation | `Observation.interpretation.coding` | 2004005.0 | Normal blood pressure | http://snomed.info/sct |
| 17 | 293 | Observation | `Observation.interpretation.coding` | OI000041 | Tekanan Darah Normal Tinggi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 18 | 298 | Observation | `Observation.interpretation.coding` | 827069000.0 | Stage 1 hypertension | http://snomed.info/sct |
| 19 | 303 | Observation | `Observation.interpretation.coding` | 827068008.0 | Stage 1 hypertension | http://snomed.info/sct |
| 20 | 308 | Observation | `Observation.interpretation.coding` | OI000042 | Hipertensi Derajat 3 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 21 | 317 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://snomed.info/sct |
| 22 | 327 | Observation | `Observation.interpretation.coding` | OI000040 | Tekanan Darah Optimal | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 23 | 332 | Observation | `Observation.interpretation.coding` | 2004005.0 | Normal blood pressure | http://snomed.info/sct |
| 24 | 337 | Observation | `Observation.interpretation.coding` | OI000041 | Tekanan Darah Normal Tinggi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 25 | 342 | Observation | `Observation.interpretation.coding` | 827069000.0 | Stage 1 hypertension | http://snomed.info/sct |
| 26 | 347 | Observation | `Observation.interpretation.coding` | 827068008.0 | Stage 1 hypertension | http://snomed.info/sct |
| 27 | 352 | Observation | `Observation.interpretation.coding` | OI000042 | Hipertensi Derajat 3 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 28 | 361 | Observation | `Observation.code.coding` | 268607006.0 | Hypertension risk level | http://snomed.info/sct |
| 29 | 373 | Observation | `Observation.interpretation.coding` | OI000040 | Tekanan Darah Optimal | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 30 | 374 | Observation | `Observation.interpretation.coding` | 2004005.0 | Normal blood pressure | http://snomed.info/sct |
| 31 | 375 | Observation | `Observation.interpretation.coding` | OI000041 | Tekanan Darah Normal Tinggi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 32 | 376 | Observation | `Observation.interpretation.coding` | 827069000.0 | Stage 1 hypertension | http://snomed.info/sct |
| 33 | 377 | Observation | `Observation.interpretation.coding` | 827068008.0 | Stage 2 hypertension | http://snomed.info/sct |
| 34 | 378 | Observation | `Observation.interpretation.coding` | OI000042 | Hipertensi Derajat 3 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 35 | 379 | Observation | `Observation.interpretation.coding` | 56218007.0 | Systolic hypertension | http://snomed.info/sct |
| 36 | 392 | ServiceRequest | `ServiceRequest.code` | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 37 | 400 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002.0 | Laboratory worker | http://snomed.info/sct |
| 38 | 403 | Specimen | `Specimen.type` | 119297000.0 | Blood specimen | http://snomed.info/sct |
| 39 | 412 | Observation | `Observation.code.coding` | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 40 | 420 | Observation | `Observation.interpretation.coding` | 302866003.0 | Hypoglycemia | http://snomed.info/sct |
| 41 | 423 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 42 | 428 | Observation | `Observation.interpretation.coding` | 714628002.0 | Prediabetes | http://snomed.info/sct |
| 43 | 433 | Observation | `Observation.interpretation.coding` | 80394007.0 | Hyperglycemia | http://snomed.info/sct |
| 44 | 438 | DiagnosticReport | `DiagnosticReport.code` | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 45 | 452 | Observation | `Observation.code.coding` | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 46 | 460 | Observation | `Observation.interpretation.coding` | 302866003.0 | Hypoglycemia | http://snomed.info/sct |
| 47 | 463 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 48 | 468 | Observation | `Observation.interpretation.coding` | 714628002.0 | Prediabetes | http://snomed.info/sct |
| 49 | 473 | Observation | `Observation.interpretation.coding` | 73211009.0 | Diabetes mellitus | http://snomed.info/sct |
| 50 | 480 | Observation | `Observation.code.coding` | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 51 | 488 | Observation | `Observation.interpretation.coding` | 302866003.0 | Hypoglycemia | http://snomed.info/sct |
| 52 | 491 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 53 | 496 | Observation | `Observation.interpretation.coding` | 714628002.0 | Prediabetes | http://snomed.info/sct |
| 54 | 501 | Observation | `Observation.interpretation.coding` | 73211009.0 | Diabetes mellitus | http://snomed.info/sct |
| 55 | 508 | Observation | `Observation.code.coding` | 1521-4 | Glucose [Mass/volume] in Serum or Plasma --2 hours post meal | http://loinc.org |
| 56 | 518 | Observation | `Observation.interpretation.coding` | 302866003.0 | Hypoglycemia | http://snomed.info/sct |
| 57 | 521 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 58 | 526 | Observation | `Observation.interpretation.coding` | 714628002.0 | Prediabetes | http://snomed.info/sct |
| 59 | 531 | Observation | `Observation.interpretation.coding` | 73211009.0 | Diabetes mellitus | http://snomed.info/sct |
| 60 | 538 | Observation | `Observation.code.coding` | 4548-4 | Hemoglobin A1c/Hemoglobin.total in Blood | http://loinc.org |
| 61 | 546 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 62 | 549 | Observation | `Observation.interpretation.coding` | 714628002.0 | Prediabetes | http://snomed.info/sct |
| 63 | 554 | Observation | `Observation.interpretation.coding` | 73211009.0 | Diabetes mellitus | http://snomed.info/sct |
| 64 | 563 | Observation | `Observation.code.coding` | 34534-8 | 12 lead EKG panel | http://loinc.org |
| 65 | 564 | Observation | `Observation.valueCodeableConcept.coding` | 17621005.0 | Normal | http://snomed.info/sct |
| 66 | 565 | Observation | `Observation.interpretation.coding` | 164854000 | Electrocardiogram normal | http://snomed.info/sct |
| 67 | 566 | Observation | `Observation.valueCodeableConcept.coding` | 263654008 | Abnormal | http://snomed.info/sct |
| 68 | 567 | Observation | `Observation.interpretation.coding` | 102594003.0 | Electrocardiogram abnormal | http://snomed.info/sct |
| 69 | 575 | Observation | `Observation.component.code.coding` | 164854000 | Electrocardiogram normal | http://snomed.info/sct |
| 70 | 578 | Observation | `Observation.component.code.coding` | 26141007 | ST segment depression | http://snomed.info/sct |
| 71 | 581 | Observation | `Observation.component.code.coding` | 59931005 | Electrocardiogram normal | http://snomed.info/sct |
| 72 | 584 | Observation | `Observation.component.code.coding` | 164873001 | Electrocardiographic left ventricle hypertrophy | http://snomed.info/sct |
| 73 | 587 | Observation | `Observation.component.code.coding` | 164889003 | Electrocardiographic atrial fibrillation | http://snomed.info/sct |
| 74 | 590 | Observation | `Observation.component.code.coding` | 164918000 | Pathological Q wave | http://snomed.info/sct |
| 75 | 593 | Observation | `Observation.component.code.coding` | 76388001 | ST segment elevation | http://snomed.info/sct |
| 76 | 596 | Observation | `Observation.component.code.coding` | 102594003.0 | Electrocardiogram abnormal | http://snomed.info/sct |
| 77 | 606 | Observation | `Observation.code.coding` | 2093-3 | Cholesterol [Mass/volume] in Serum or Plasma | http://loinc.org |
| 78 | 616 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 79 | 620 | Observation | `Observation.interpretation.coding` | H | High | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 80 | 628 | Observation | `Observation.code.coding` | 2085-9 | Cholesterol in HDL [Mass/volume] in Serum or Plasma | http://loinc.org |
| 81 | 631 | Observation | `Observation.interpretation.coding` | L | Low | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 82 | 635 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 83 | 650 | Observation | `Observation.code.coding` | 2085-9 | Cholesterol in HDL [Mass/volume] in Serum or Plasma | http://loinc.org |
| 84 | 653 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 85 | 657 | Observation | `Observation.interpretation.coding` | H | High | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 86 | 672 | Observation | `Observation.code.coding` | 2571-8 | Triglyceride [Mass/volume] in Serum or Plasma | http://loinc.org |
| 87 | 675 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 88 | 679 | Observation | `Observation.interpretation.coding` | H | High | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 89 | 694 | Observation | `Observation.code.coding` | 100898-6 | Lipid panel - Serum or Plasma | http://loinc.org |
| 90 | 695 | Observation | `Observation.valueCodeableConcept.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 91 | 696 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 92 | 697 | Observation | `Observation.valueCodeableConcept.coding` | 370992007.0 | Dyslipidemia | http://snomed.info/sct |
| 93 | 698 | Observation | `Observation.interpretation.coding` | 370992007.0 | Dyslipidemia | http://snomed.info/sct |
| 94 | 712 | Observation | `Observation.code.coding` | OC000173 | Prediksi Risiko PTM tanpa Pemeriksaan Laboratorium | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 95 | 713 | Observation | `Observation.interpretation.coding` | 723505004.0 | Low risk | http://snomed.info/sct |
| 96 | 716 | Observation | `Observation.interpretation.coding` | 25594002.0 | Moderate risk of | http://snomed.info/sct |
| 97 | 721 | Observation | `Observation.interpretation.coding` | 723509005.0 | High risk | http://snomed.info/sct |
| 98 | 737 | Observation | `Observation.code.coding` | 20977-5 | Urea [Mass/volume] in Blood | http://loinc.org |
| 99 | 738 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 100 | 743 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 101 | 757 | Observation | `Observation.code.coding` | 2160-0 | Creatinine [Mass/volume] in Serum or Plasma | http://loinc.org |
| 102 | 758 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 103 | 763 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 104 | 777 | Observation | `Observation.code.coding` | 62238-1 | Glomerular filtration rate/1.73 sq M.predicted [Volume Rate/Area] in Serum, Plasma or Blood by Creatinine-based formula (CKD-EPI) | http://loinc.org |
| 105 | 778 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 106 | 781 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 107 | 834 | Observation | `Observation.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 108 | 835 | Observation | `Observation.method.coding` | 391483001.0 | Microscopy (acid fast bacilli) | http://snomed.info/sct |
| 109 | 836 | Observation | `Observation.valueCodeableConcept.coding` | 10828004.0 | Positive | http://snomed.info/sct |
| 110 | 837 | Observation | `Observation.valueCodeableConcept.coding` | 260385009.0 | Negative | http://snomed.info/sct |
| 111 | 849 | Observation | `Observation.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 112 | 850 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 113 | 863 | Observation | `Observation.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 114 | 864 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 115 | 877 | Observation | `Observation.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 116 | 878 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 117 | 891 | Observation | `Observation.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 118 | 892 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 119 | 905 | Observation | `Observation.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 120 | 906 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 121 | 907 | Observation | `Observation.valueCodeableConcept.coding` | LA11883-8 | Not Detected | http://loinc.org |
| 122 | 908 | Observation | `Observation.interpretation.coding` | NEG | Negative | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 123 | 920 | Observation | `Observation.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 124 | 921 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 125 | 922 | Observation | `Observation.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 126 | 923 | Observation | `Observation.interpretation.coding` | NEG | Negative | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 127 | 935 | Observation | `Observation.code.coding` | 89372-7 | Mycobacterium tuberculosis complex rpoB gene rifAMPin resistance mutation [Presence] by Molecular method | http://loinc.org |
| 128 | 936 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 129 | 937 | Observation | `Observation.valueCodeableConcept.coding` | LA11883-8 | Not Detected | http://loinc.org |
| 130 | 938 | Observation | `Observation.interpretation.coding` | X099770 | Rifampisin sensitive | http://terminology.kemkes.go.id/CodeSystem/examination |
| 131 | 950 | Observation | `Observation.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 132 | 951 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 133 | 952 | Observation | `Observation.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 134 | 953 | Observation | `Observation.interpretation.coding` | NEG | Negative | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 135 | 965 | Observation | `Observation.code.coding` | 89372-7 | Mycobacterium tuberculosis complex rpoB gene rifAMPin resistance mutation [Presence] by Molecular method | http://loinc.org |
| 136 | 966 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 137 | 967 | Observation | `Observation.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 138 | 968 | Observation | `Observation.interpretation.coding` | X099771 | Rifampisin resistan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 139 | 980 | Observation | `Observation.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 140 | 981 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 141 | 982 | Observation | `Observation.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 142 | 983 | Observation | `Observation.interpretation.coding` | NEG | Negative | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 143 | 995 | Observation | `Observation.code.coding` | 89372-7 | Mycobacterium tuberculosis complex rpoB gene rifAMPin resistance mutation [Presence] by Molecular method | http://loinc.org |
| 144 | 996 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 145 | 997 | Observation | `Observation.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 146 | 998 | Observation | `Observation.interpretation.coding` | X099772 | Rifampisin indeterminate | http://terminology.kemkes.go.id/CodeSystem/examination |
| 147 | 1010 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | female | Female | http://hl7.org/fhir/administrative-gender |
| 148 | 1011 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | male | Male | http://hl7.org/fhir/administrative-gender |
| 149 | 1023 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | SP000435 | <20 bungkus per tahun | http://terminology.kemkes.go.id/sp |
| 150 | 1024 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | SP000436 | 20-30 bungkus per tahun | http://terminology.kemkes.go.id/sp |
| 151 | 1025 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | SP000437 | >30 bungkus per tahun | http://terminology.kemkes.go.id/sp |
| 152 | 1044 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | 723505004.0 | Low risk | http://snomed.info/sct |
| 153 | 1045 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | 723509005.0 | High risk | http://snomed.info/sct |
| 154 | 1146 | Observation | `Observation.code.coding` | 410007005.0 | Rectal examination | http://snomed.info/sct |
| 155 | 1154 | Observation | `Observation.valueCodeableConcept.coding` | 248523006.0 | Rectal mass | http://snomed.info/sct |
| 156 | 1155 | Observation | `Observation.valueCodeableConcept.coding` | 300870000.0 | No mass present | http://snomed.info/sct |
| 157 | 1162 | Observation | `Observation.code.coding` | 14563-1 | Hemoglobin.gastrointestinal [Presence] in Stool --1st specimen | http://loinc.org |
| 158 | 1170 | Observation | `Observation.valueCodeableConcept.coding` | 167667006.0 | Occult blood not detected in feces | http://snomed.info/sct |
| 159 | 1171 | Observation | `Observation.valueCodeableConcept.coding` | 59614000.0 | Occult blood detected in feces | http://snomed.info/sct |
| 160 | 1182 | Observation | `Observation.code.coding` | 247301006.0 | Finding of ability to hear whisper | http://snomed.info/sct |
| 161 | 1190 | Observation | `Observation.valueCodeableConcept.coding` | 275727004.0 | Hearing test normal | http://snomed.info/sct |
| 162 | 1191 | Observation | `Observation.valueCodeableConcept.coding` | 300221005.0 | Hearing for whisper impaired | http://snomed.info/sct |
| 163 | 1198 | Observation | `Observation.code.coding` | 76517002.0 | Otoscopy | http://snomed.info/sct |
| 164 | 1206 | Observation | `Observation.valueCodeableConcept.coding` | 275727004.0 | Hearing test normal | http://snomed.info/sct |
| 165 | 1207 | Observation | `Observation.valueCodeableConcept.coding` | 300221005.0 | Hearing for whisper impaired | http://snomed.info/sct |
| 166 | 1221 | Observation | `Observation.code.coding` | 400911007.0 | Tumbling E test | http://snomed.info/sct |
| 167 | 1223 | Observation | `Observation.valueCodeableConcept.coding` | 45089002.0 | Normal vision | http://snomed.info/sct |
| 168 | 1224 | Observation | `Observation.interpretation.coding` | 45089002.0 | Normal vision | http://snomed.info/sct |
| 169 | 1225 | Observation | `Observation.valueCodeableConcept.coding` | 397540003.0 | Visual impairment | http://snomed.info/sct |
| 170 | 1226 | Observation | `Observation.interpretation.coding` | 397540003.0 | Visual impairment | http://snomed.info/sct |
| 171 | 1237 | Observation | `Observation.code.coding` | 252973004.0 | Snellen chart assessment | http://snomed.info/sct |
| 172 | 1239 | Observation | `Observation.valueCodeableConcept.coding` | 45089002.0 | Normal vision | http://snomed.info/sct |
| 173 | 1240 | Observation | `Observation.interpretation.coding` | 45089002.0 | Normal vision | http://snomed.info/sct |
| 174 | 1241 | Observation | `Observation.valueCodeableConcept.coding` | 397540003.0 | Visual impairment | http://snomed.info/sct |
| 175 | 1242 | Observation | `Observation.interpretation.coding` | 397540003.0 | Visual impairment | http://snomed.info/sct |
| 176 | 1256 | Observation | `Observation.code.coding` | 441841000.0 | Pinhole visual acuity test | http://loinc.org |
| 177 | 1258 | Observation | `Observation.valueCodeableConcept.coding` | 39021009.0 | Disorder of refraction | http://snomed.info/sct |
| 178 | 1259 | Observation | `Observation.interpretation.coding` | 39021009.0 | Disorder of refraction | http://snomed.info/sct |
| 179 | 1260 | Observation | `Observation.valueCodeableConcept.coding` | OI000044 | Kelainan organik | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 180 | 1261 | Observation | `Observation.interpretation.coding` | OI000044 | Kelainan organik | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 181 | 1275 | Observation | `Observation.code.coding` | 40137007.0 | Pupil light reflex | http://snomed.info/sct |
| 182 | 1277 | Observation | `Observation.valueCodeableConcept.coding` | OV000393 | Suspek katarak | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 183 | 1278 | Observation | `Observation.valueCodeableConcept.coding` | 371405004.0 | Disorder of eye proper | http://snomed.info/sct |
| 184 | 1364 | Observation | `Observation.code.coding` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 185 | 1366 | Observation | `Observation.valueCodeableConcept.coding` | 11214006.0 | Reactive | http://snomed.info/sct |
| 186 | 1367 | Observation | `Observation.valueCodeableConcept.coding` | 131194007.0 | Non-Reactive | http://snomed.info/sct |
| 187 | 1380 | Observation | `Observation.code.coding` | 72376-7 | Hepatitis C virus Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 188 | 1382 | Observation | `Observation.valueCodeableConcept.coding` | 11214006.0 | Reactive | http://snomed.info/sct |
| 189 | 1383 | Observation | `Observation.valueCodeableConcept.coding` | 131194007.0 | Non-Reactive | http://snomed.info/sct |
| 190 | 1416 | Observation | `Observation.code.coding` | 1920-8 | Aspartate aminotransferase [Enzymatic activity/volume] in Serum or Plasma | http://loinc.org |
| 191 | 1433 | Observation | `Observation.code.coding[x]` | 26515-7 | Platelets [#/volume] in Blood | http://loinc.org |
| 192 | 1449 | Observation | `Observation.code.coding[x]` | 86465-2 | AST to platelet ratio index in Serum and Blood by calculation | http://loinc.org |
| 193 | 1471 | Observation | `Observation.code.coding` | TK000144 | Rencana menikah 1 tahun ke depan | http://terminology.kemkes.go.id |
| 194 | 1496 | Observation | `Observation.code.coding` | 30352-9 | Hemoglobin [Mass/volume] in Capillary blood | http://loinc.org |
| 195 | 1504 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 196 | 1507 | Observation | `Observation.interpretation.coding` | 271737000.0 | Anemia | http://snomed.info/sct |
| 197 | 1521 | Observation | `Observation.code.coding` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 198 | 1522 | Observation | `Observation.valueCodeableConcept.coding` | LA15255-5 | Reactive | http://loinc.org |
| 199 | 1523 | Observation | `Observation.valueCodeableConcept.coding` | LA15256-3 | Nonreactive | http://loinc.org |
| 200 | 1542 | Observation | `Observation.code.coding` | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 201 | 1543 | Observation | `Observation.valueCodeableConcept.coding` | LA15255-5 | Reactive | http://loinc.org |
| 202 | 1544 | Observation | `Observation.valueCodeableConcept.coding` | LA15256-3 | Nonreactive | http://loinc.org |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 98 |
| http://loinc.org | 53 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 27 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 13 |
| http://terminology.kemkes.go.id/CodeSystem/examination | 3 |
| http://terminology.kemkes.go.id/sp | 3 |
| http://terminology.kemkes.go.id | 2 |
| http://hl7.org/fhir/administrative-gender | 2 |
| http://hl7.org/fhir/sid/icd-10 | 1 |
| **Total** | **202** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 30 | – | ihs_organization | Organization | `Organization.id` |
| 32 | – | organization_name | Organization | `Organization.name` |
| 33 | – | kabkota_name | Organization | `Organization.address.city` |
| 36 | – | provinsi | Organization | `Organization.address.extension.extension.url` |
| 39 | – | kabkota | Organization | `Organization.address.extension.extension.url` |
| 603 | – | interpretasi_kolesterol_total | – | `` |
