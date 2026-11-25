# Output Form: ASIK - CKG Dewasa Perempuan

Sumber: `mapping/phdt-data-dictionary-asik-ckg-dewasa-perempuan.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-asik-ckg-dewasa-perempuan.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 66 |
| Code (`jumlah code` = 1) | 299 |
| Code unik (code + CodeSystem) | 174 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 9 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–27 | Patient | – | – | _pasien_name_ → `Patient.name.text` (2, tanpa BQ)<br>_nik_ → `Patient.identifier.value` (5, tanpa BQ)<br>_pasien_id_ → `Patient.identifier.value` (8, tanpa BQ)<br>_jenis_kelamin_ → `Patient.gender` (10, tanpa BQ)<br>_tgl_lahir_ → `Patient.birthDate` (12, tanpa BQ)<br>_no_handphone_ → `Patient.telecom` (13, tanpa BQ)<br>_status_perkawinan_ → `Patient.maritalStatus.coding` (16, tanpa BQ)<br>_kabkota_name_ → `Patient.address.city` (20, tanpa BQ)<br>_provinsi_ → `Patient.address.extension.extension.valueCode` (24, tanpa BQ)<br>_kabkota_ → `Patient.address.extension.extension.valueCode` (27, tanpa BQ) |
| 2 | 66–79 | Encounter | – | – | _tgl_pelayanan_ → `Encounter.identifier` (66, tanpa BQ) |
| 3 | 80–87 | Condition | Z01.8 | Other specified special examinations | – |
| 4 | 98–109 | Observation | 424144002 | Current chronological age | _age_now_ → `Observation.valueQuantity.value` (101, tanpa BQ) |
| 5 | 110–121 | Observation | TK000144 | Rencana menikah 1 tahun ke depan | _rencana_menikah_dalam_kurun_waktu_1_tahun_ → `Observation.valueBoolean` (113, tanpa BQ) |
| 6 | 122–179 | QuestionnaireResponse | https://fhir.kemkes.go.id/Questionnaire/Q0051 | – | _apakah_merokok_dalam_setahun_terakhir_ → `QuestionnaireResponse.item.item.text` (134, tanpa BQ)<br>_sudah_berapa_tahun_merokok_ → `QuestionnaireResponse.item.item.answer.item.text` (138, tanpa BQ)<br>_berapa_batang_rokok_yang_dihisap_dalam_sehari_ → `QuestionnaireResponse.item.item.answer.item.text` (142, tanpa BQ)<br>_apakah_pernah_merokok_sebelumnya_ → `QuestionnaireResponse.item.item.text` (145, tanpa BQ)<br>_berapa_lama_merokok_sebelumnya_ → `QuestionnaireResponse.item.item.answer.item.text` (149, tanpa BQ)<br>_kapan_anda_berhenti_merokok_ → `QuestionnaireResponse.item.item.answer.item.text` (153, tanpa BQ)<br>_apakah_terpapar_asap_rokok_sebulan_terakhir_ → `QuestionnaireResponse.item.item.text` (157, tanpa BQ)<br>_apakah_rutin_melakukan_olahraga_ → `QuestionnaireResponse.item.item.text` (161, tanpa BQ)<br>_berapa_kali_berolahraga_dalam_seminggu_ → `QuestionnaireResponse.item.item.answer.item.text` (165, tanpa BQ)<br>_berapa_menit_berolahraga_ → `QuestionnaireResponse.item.item.answer.item.text` (168, tanpa BQ)<br>_tingkat_aktivitas_fisik_ → `QuestionnaireResponse.item.item.answer.item.linkId` (170, tanpa BQ)<br>_berat_badan_kg_ → `QuestionnaireResponse.item.item.item.text` (177, tanpa BQ)<br>_tinggi_badan_cm_ → `QuestionnaireResponse.item.item.item.text` (193, tanpa BQ)<br>_index_massa_tubuh_ → `QuestionnaireResponse.item.item.item.text` (209, tanpa BQ)<br>_lingkar_perut_ → `QuestionnaireResponse.item.item.item.text` (240, tanpa BQ)<br>_apakah_pernah_dinyatakan_tekanan_darah_tinggi_ → `QuestionnaireResponse.item.item.linkId` (263, tanpa BQ)<br>_sistolik_ → `QuestionnaireResponse.item.item.item.answer.valueReference.reference` (269, tanpa BQ)<br>_diastolik_ → `QuestionnaireResponse.item.item.item.answer.valueReference.reference` (313, tanpa BQ)<br>_tekanan_darah_ → `QuestionnaireResponse.item.item.item.answer.valueReference.reference` (357, tanpa BQ)<br>_apakah_pernah_dinyatakan_diabetes_kencing_manis_ → `QuestionnaireResponse.item.item.text` (381, tanpa BQ)<br>_gula_darah_sewaktu_ → `QuestionnaireResponse.item.item.item.answer.valueReference.display` (387, tanpa BQ)<br>_gula_darah_puasa_ → `QuestionnaireResponse.item.item.item.answer.valueReference.display` (449, tanpa BQ)<br>_gula_darah_puasa_lanjutan_ → `QuestionnaireResponse.item.item.item.answer.valueReference.display` (477, tanpa BQ)<br>_gula_darah_2_jam_pp_ → `QuestionnaireResponse.item.item.item.answer.valueReference.reference` (504, tanpa BQ)<br>_pemeriksaan_hb1ac_ → `QuestionnaireResponse.item.item.item.answer.valueReference.display` (535, tanpa BQ)<br>_hasil_pemeriksaan_ekg_ → `QuestionnaireResponse.item.item.text` (558, tanpa BQ)<br>_kolesterol_total_ → `QuestionnaireResponse.item.item.answer.valueReference.display` (602, tanpa BQ)<br>_masukkan_nilai_hdl_ → `QuestionnaireResponse.item.item.answer.valueReference.reference` (624, tanpa BQ)<br>_interpretasi_hdl_ → `QuestionnaireResponse.item.item.answer.valueReference.display` (625, tanpa BQ)<br>_masukkan_nilai_ldl_ → `QuestionnaireResponse.item.item.answer.valueReference.reference` (646, tanpa BQ)<br>_interpretasi_ldl_ → `QuestionnaireResponse.item.item.answer.valueReference.display` (647, tanpa BQ)<br>_masukkan_nilai_trigliserida_ → `QuestionnaireResponse.item.item.answer.valueReference.reference` (668, tanpa BQ)<br>_interpretasi_trigliserida_ → `QuestionnaireResponse.item.item.answer.valueReference.display` (669, tanpa BQ)<br>_interpretasi_dislipidemia_ → `QuestionnaireResponse.item.item.answer.valueReference.reference` (690, tanpa BQ)<br>_prediksi_risiko_penyakit_kardiovaskular_ → `QuestionnaireResponse.item.item.linkId` (706, tanpa BQ)<br>_hasil_ureum_ → `QuestionnaireResponse.item.item.answer.valueReference.reference` (733, tanpa BQ)<br>_hasil_kreatinin_ → `QuestionnaireResponse.item.item.answer.valueReference.reference` (753, tanpa BQ)<br>_hasil_elfg_ckd_epi_ → `QuestionnaireResponse.item.item.answer.valueReference.reference` (773, tanpa BQ)<br>_hasil_pemeriksaan_gigi_karies_ → `QuestionnaireResponse.item.item.item.text` (794, tanpa BQ)<br>_hasil_pemeriksaan_gigi_hilang_dicabut_ → `QuestionnaireResponse.item.item.item.text` (798, tanpa BQ)<br>_hasil_pemeriksaan_pocket_periodontal_ → `QuestionnaireResponse.item.item.answer.item.text` (805, tanpa BQ)<br>_hasil_pemeriksaan_gigi_goyang_ → `QuestionnaireResponse.item.item.answer.item.text` (809, tanpa BQ)<br>_apakah_mengalami_batuk_lebih_dari_2_minggu_ → `QuestionnaireResponse.item.item.item.linkId` (816, tanpa BQ)<br>_apakah_sering_bertemu_dengan_penderita_tbc_ → `QuestionnaireResponse.item.item.item.linkId` (820, tanpa BQ)<br>_riwayat_kontak_tuberkulosis_ → `QuestionnaireResponse.item.item.item.linkId` (824, tanpa BQ)<br>_metode_pemeriksaan_ → `QuestionnaireResponse.item.item.text` (829, tanpa BQ)<br>_hasil_pemeriksaan_bta_ → `QuestionnaireResponse.item.item.answer.valueReference.display` (831, tanpa BQ)<br>_hasil_pemeriksaan_tb_tcm_ → `QuestionnaireResponse.item.item.answer.valueReference.display` (846, tanpa BQ)<br>_hasil_pemeriksaan_tb_tcm_ → `QuestionnaireResponse.item.item.answer.valueReference.display` (860, tanpa BQ)<br>_hasil_pemeriksaan_tb_tcm_ → `QuestionnaireResponse.item.item.answer.valueReference.display` (874, tanpa BQ)<br>_hasil_pemeriksaan_tb_tcm_ → `QuestionnaireResponse.item.item.answer.valueReference.display` (888, tanpa BQ)<br>_usia_puma_ → `QuestionnaireResponse.item.item.item.linkId` (1012, tanpa BQ)<br>_apakah_mempunyai_riwayat_merokok_ → `QuestionnaireResponse.item.item.item.linkId` (1017, tanpa BQ)<br>_berapa_bungkus_rokok_dalam_1_tahun_ → `QuestionnaireResponse.item.item.item.linkId` (1021, tanpa BQ)<br>_apakah_pernah_merasa_napas_pendek_saat_jalan_cepat_ → `QuestionnaireResponse.item.item.item.linkId` (1026, tanpa BQ)<br>_apakah_mempunyai_dahak_atau_kesulitan_mengeluarkan_dahak_ → `QuestionnaireResponse.item.item.item.linkId` (1030, tanpa BQ)<br>_apakah_biasanya_batuk_ketika_tidak_menderita_flu_ → `QuestionnaireResponse.item.item.item.linkId` (1034, tanpa BQ)<br>_apakah_pernah_melakukan_spirometri_ → `QuestionnaireResponse.item.item.item.linkId` (1038, tanpa BQ)<br>_hasil_skor_puma_ → `QuestionnaireResponse.item.item.item.linkId` (1042, tanpa BQ)<br>_jenis_pemeriksaan_ → `QuestionnaireResponse.item.item.answer.item.text` (1053, tanpa BQ)<br>_hasil_pemeriksaan_sadanis_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1062, tanpa BQ)<br>_hasil_pemeriksaan_usg_payudara_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1079, tanpa BQ)<br>_apakah_pernah_melakukan_hubungan_intim_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1100, tanpa BQ)<br>_hasil_pemeriksaan_inspekulo_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1104, tanpa BQ)<br>_hasil_pemeriksaan_iva_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1120, tanpa BQ)<br>_hasil_pemeriksaan_hpv_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1136, tanpa BQ)<br>_jenis_kelamin_paru_ → `QuestionnaireResponse.item.item.answer.item.text` (1161, tanpa BQ)<br>_usia_paru_ → `QuestionnaireResponse.item.item.item.linkId` (1164, tanpa BQ)<br>_apakah_pernah_didiagnosa_menderita_kanker_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1169, tanpa BQ)<br>_apakah_ada_keluarga_yang_didiagnosa_menderita_kanker_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1174, tanpa BQ)<br>_riwayat_merokok_atau_paparan_asap_rokok_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1179, tanpa BQ)<br>_riwayat_tempat_kerja_mengandung_zat_karsinogenik_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1185, tanpa BQ)<br>_lingkungan_tempat_tinggal_berpotensi_tinggi_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1190, tanpa BQ)<br>_lingkungan_tempat_tinggal_berpotensi_tinggi_1_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1195, tanpa BQ)<br>_apakah_pernah_didiagnosis_penyakit_paru_kronik_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1200, tanpa BQ)<br>_apakah_pernah_didiagnosis_penyakit_paru_kronik_1_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1205, tanpa BQ)<br>_hasil_skrining_kanker_paru_ → `QuestionnaireResponse.item.item.answer.item.text` (1211, tanpa BQ)<br>_jenis_kelamin_apcs_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1218, tanpa BQ)<br>_usia_skor_apcs_ → `QuestionnaireResponse.item.item.item.linkId` (1222, tanpa BQ)<br>_kankes_usus_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1227, tanpa BQ)<br>_riwayat_merokok_apcs_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1231, tanpa BQ)<br>_skor_apcs_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1235, tanpa BQ)<br>_kesediaan_colok_dubur_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1244, tanpa BQ)<br>_hasil_colok_dubur_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1248, tanpa BQ)<br>_hasil_darah_samar_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1264, tanpa BQ)<br>_hasil_pemeriksaan_tajam_pendengaran_ → `QuestionnaireResponse.item.answer.item.linkId` (1284, tanpa BQ)<br>_hasil_pemeriksaan_pinhole_ → `QuestionnaireResponse.item.answer.item.linkId` (1359, tanpa BQ)<br>_hasil_pemeriksaan_pupil_ → `QuestionnaireResponse.item.answer.item.text` (1379, tanpa BQ)<br>_seberapa_sering_tidak_bersemangat_dalam_2_minggu_ → `QuestionnaireResponse.item.answer.item.text` (1400, tanpa BQ)<br>_seberapa_sering_merasa_murung_tertekan_putus_asa_dalam_2_minggu_ → `QuestionnaireResponse.item.answer.item.text` (1406, tanpa BQ)<br>_seberapa_sering_merasa_gugup_cemas_gelisah_dalam_2_minggu_ → `QuestionnaireResponse.item.answer.item.text` (1412, tanpa BQ)<br>_seberapa_sering_merasa_khawatir_dalam_2_minggu_ → `QuestionnaireResponse.item.answer.item.text` (1418, tanpa BQ)<br>_gejala_depresi_ → `QuestionnaireResponse.item.answer.item.text` (1424, tanpa BQ)<br>_gejala_kecemasan_ → `QuestionnaireResponse.item.answer.item.text` (1428, tanpa BQ)<br>_apakah_hasil_hepatitis_b_mendapat_positif_ → `QuestionnaireResponse.item.answer.item.linkId` (1435, tanpa BQ)<br>_apakah_memiliki_keluarga_yang_menderita_hepatitis_b_ → `QuestionnaireResponse.item.answer.item.linkId` (1439, tanpa BQ)<br>_apakah_pernah_melakukan_hubungan_intim_dengan_bebas_ → `QuestionnaireResponse.item.answer.item.linkId` (1443, tanpa BQ)<br>_apakah_pernah_menerima_transfusi_darah_ → `QuestionnaireResponse.item.answer.item.linkId` (1447, tanpa BQ)<br>_apakah_pernah_menjalani_cuci_darah_ → `QuestionnaireResponse.item.answer.item.linkId` (1451, tanpa BQ)<br>_apakah_pernah_menggunakan_narkoba_ → `QuestionnaireResponse.item.answer.item.linkId` (1455, tanpa BQ)<br>_apakah_anda_menderita_hiv_ → `QuestionnaireResponse.item.answer.item.linkId` (1459, tanpa BQ)<br>_apakah_anda_mendapat_pengobatan_hepatitis_c_dan_tidak_sembuh_ → `QuestionnaireResponse.item.answer.item.linkId` (1463, tanpa BQ)<br>_hasil_rapid_test_hepatitis_b_ → `QuestionnaireResponse.item.answer.item.linkId` (1467, tanpa BQ)<br>_hasil_rapid_test_hepatitis_c_ → `QuestionnaireResponse.item.answer.item.linkId` (1484, tanpa BQ)<br>_faktor_risiko_hepatitis_b_ → `QuestionnaireResponse.item.answer.item.linkId` (1499, tanpa BQ)<br>_faktor_risiko_hepatitis_c_ → `QuestionnaireResponse.item.answer.item.linkId` (1503, tanpa BQ)<br>_faktor_risiko_hepatitis_ → `QuestionnaireResponse.item.answer.item.linkId` (1507, tanpa BQ)<br>_apakah_hasil_kolestrol_tinggi_ → `QuestionnaireResponse.item.answer.item.linkId` (1515, tanpa BQ)<br>_nilai_sgot_ → `QuestionnaireResponse.item.answer.item.linkId` (1519, tanpa BQ)<br>_pemeriksaan_trombosit_ → `QuestionnaireResponse.item.answer.item.linkId` (1536, tanpa BQ)<br>_hasil_apri_score_ → `QuestionnaireResponse.item.answer.item.linkId` (1552, tanpa BQ)<br>_rencana_menikah_dalam_kurun_waktu_1_tahun_ → `QuestionnaireResponse.item.answer.valueBoolean` (1591, tanpa BQ)<br>_rencana_menikah_dalam_kurun_waktu_1_tahun_ → `QuestionnaireResponse.item.answer.valueBoolean` (1592, tanpa BQ)<br>_hasil_pemeriksaan_rapid_test_hb_ → `QuestionnaireResponse.item.answer.item.item.text` (1600, tanpa BQ)<br>_hasil_pemeriksaan_rapid_test_sifilis_ → `QuestionnaireResponse.item.answer.item.item.text` (1625, tanpa BQ)<br>_hasil_pemeriksaan_rapid_test_hiv_ → `QuestionnaireResponse.item.answer.item.item.text` (1646, tanpa BQ) |
| 7 | 180–191 | Observation | 29463-7 | Body weight | – |
| 8 | 196–207 | Observation | 8302-2 | Body height | – |
| 9 | 212–238 | Observation | 39156-5 | Body mass index (BMI) [Ratio] | – |
| 10 | 243–262 | Observation | vital-signs | Abdominal circumference | – |
| 11 | 271–312 | Observation | 8480-6 | Systolic blood pressure | – |
| 12 | 315–356 | Observation | 8462-4 | Diastolic blood pressure | – |
| 13 | 359–379 | Observation | 268607006 | Hypertension risk level | – |
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
| 45 | 1066–1078 | Observation | 13607009 | Manual examination of breast | – |
| 46 | 1083–1095 | Observation | 24601-7 | US Breast | – |
| 47 | 1108–1119 | Observation | 451024007 | Inspection of vagina using vaginal speculum | – |
| 48 | 1124–1135 | Observation | X099241 | Tes IVA | – |
| 49 | 1140–1155 | Observation | 44550-2 | Human papilloma virus DNA [Presence] in Cervix by Probe | – |
| 50 | 1252–1263 | Observation | 410007005 | Rectal examination | – |
| 51 | 1268–1279 | Observation | 14563-1 | Hemoglobin.gastrointestinal [Presence] in Stool --1st specimen | – |
| 52 | 1288–1299 | Observation | 247301006 | Finding of ability to hear whisper | – |
| 53 | 1304–1315 | Observation | 76517002 | Otoscopy | – |
| 54 | 1327–1342 | Observation | 400911007 | Tumbling E test | _pemeriksaan_visus_e_tumbling_ → `Observation.valueCodeableConcept.coding` (1331, tanpa BQ) |
| 55 | 1343–1358 | Observation | 252973004 | Snellen chart assessment | _pemeriksaan_visus_snellen_chart_ → `Observation.valueCodeableConcept.coding` (1347, tanpa BQ) |
| 56 | 1362–1377 | Observation | 441841000 | Pinhole visual acuity test | – |
| 57 | 1381–1394 | Observation | 40137007 | Pupil light reflex | – |
| 58 | 1470–1483 | Observation | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | – |
| 59 | 1486–1498 | Observation | 72376-7 | Hepatitis C virus Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | – |
| 60 | 1522–1535 | Observation | 1920-8 | Aspartate aminotransferase [Enzymatic activity/volume] in Serum or Plasma | – |
| 61 | 1539–1551 | Observation | – | – | – |
| 62 | 1555–1576 | Observation | – | – | – |
| 63 | 1577–1588 | Observation | TK000144 | Rencana menikah 1 tahun ke depan | _rencana_menikah_dalam_kurun_waktu_1_tahun_ → `Observation.valueBoolean` (1580, tanpa BQ) |
| 64 | 1602–1617 | Observation | 30352-9 | Hemoglobin [Mass/volume] in Capillary blood | – |
| 65 | 1627–1638 | Observation | 22464-2 | Reagin Ab [Presence] in Specimen | – |
| 66 | 1648–1659 | Observation | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | – |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 58 |
| Patient | 1 |
| Encounter | 1 |
| Condition | 1 |
| QuestionnaireResponse | 1 |
| ServiceRequest | 1 |
| PractitionerRole | 1 |
| Specimen | 1 |
| DiagnosticReport | 1 |
| **Total** | **66** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 82 | Condition | `Condition.code.coding` | Z01.8 | Other specified special examinations | http://hl7.org/fhir/sid/icd-10 |
| 2 | 100 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 3 | 112 | Observation | `Observation.code.coding` | TK000144 | Rencana menikah 1 tahun ke depan | http://terminology.kemkes.go.id |
| 4 | 154 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | TK000145 | 1 tahun yang lalu | http://terminology.kemkes.go.id |
| 5 | 155 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | TK000146 | Lebih dari 1 tahun yang lalu | http://terminology.kemkes.go.id |
| 6 | 172 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 424805008 | Exercise above recommended level | http://snomed.info/sct |
| 7 | 173 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 413300002 | Exercise below recommended level | http://snomed.info/sct |
| 8 | 182 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 9 | 198 | Observation | `Observation.code.coding` | 8302-2 | Body height | http://loinc.org |
| 10 | 214 | Observation | `Observation.code.coding` | 39156-5 | Body mass index (BMI) [Ratio] | http://loinc.org |
| 11 | 215 | Observation | `Observation.interpretation.coding` | 248342006 | Underweight | http://snomed.info/sct |
| 12 | 218 | Observation | `Observation.interpretation.coding` | 43664005 | Normal weight | http://snomed.info/sct |
| 13 | 223 | Observation | `Observation.interpretation.coding` | 238131007 | Overweight | http://snomed.info/sct |
| 14 | 228 | Observation | `Observation.interpretation.coding` | 414915002 | Obese | http://snomed.info/sct |
| 15 | 245 | Observation | `Observation.code.coding` | vital-signs | Abdominal circumference | http://snomed.info/sct |
| 16 | 255 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 17 | 259 | Observation | `Observation.interpretation.coding` | 248311001 | Central obesity | http://snomed.info/sct |
| 18 | 273 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 19 | 283 | Observation | `Observation.interpretation.coding` | OI000040 | Tekanan Darah Optimal | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 20 | 288 | Observation | `Observation.interpretation.coding` | 2004005 | Normal blood pressure | http://snomed.info/sct |
| 21 | 293 | Observation | `Observation.interpretation.coding` | OI000041 | Tekanan Darah Normal Tinggi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 22 | 298 | Observation | `Observation.interpretation.coding` | 827069000 | Stage 1 hypertension | http://snomed.info/sct |
| 23 | 303 | Observation | `Observation.interpretation.coding` | 827068008 | Stage 1 hypertension | http://snomed.info/sct |
| 24 | 308 | Observation | `Observation.interpretation.coding` | OI000042 | Hipertensi Derajat 3 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 25 | 317 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://snomed.info/sct |
| 26 | 327 | Observation | `Observation.interpretation.coding` | OI000040 | Tekanan Darah Optimal | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 27 | 332 | Observation | `Observation.interpretation.coding` | 2004005 | Normal blood pressure | http://snomed.info/sct |
| 28 | 337 | Observation | `Observation.interpretation.coding` | OI000041 | Tekanan Darah Normal Tinggi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 29 | 342 | Observation | `Observation.interpretation.coding` | 827069000 | Stage 1 hypertension | http://snomed.info/sct |
| 30 | 347 | Observation | `Observation.interpretation.coding` | 827068008 | Stage 1 hypertension | http://snomed.info/sct |
| 31 | 352 | Observation | `Observation.interpretation.coding` | OI000042 | Hipertensi Derajat 3 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 32 | 361 | Observation | `Observation.code.coding` | 268607006 | Hypertension risk level | http://snomed.info/sct |
| 33 | 373 | Observation | `Observation.interpretation.coding` | OI000040 | Tekanan Darah Optimal | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 34 | 374 | Observation | `Observation.interpretation.coding` | 2004005 | Normal blood pressure | http://snomed.info/sct |
| 35 | 375 | Observation | `Observation.interpretation.coding` | OI000041 | Tekanan Darah Normal Tinggi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 36 | 376 | Observation | `Observation.interpretation.coding` | 827069000 | Stage 1 hypertension | http://snomed.info/sct |
| 37 | 377 | Observation | `Observation.interpretation.coding` | 827068008 | Stage 2 hypertension | http://snomed.info/sct |
| 38 | 378 | Observation | `Observation.interpretation.coding` | OI000042 | Hipertensi Derajat 3 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 39 | 379 | Observation | `Observation.interpretation.coding` | 56218007 | Systolic hypertension | http://snomed.info/sct |
| 40 | 392 | ServiceRequest | `ServiceRequest.code` | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 41 | 400 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002 | Laboratory worker | http://snomed.info/sct |
| 42 | 403 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 43 | 412 | Observation | `Observation.code.coding` | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 44 | 420 | Observation | `Observation.interpretation.coding` | 302866003 | Hypoglycemia | http://snomed.info/sct |
| 45 | 423 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 46 | 428 | Observation | `Observation.interpretation.coding` | 714628002 | Prediabetes | http://snomed.info/sct |
| 47 | 433 | Observation | `Observation.interpretation.coding` | 80394007 | Hyperglycemia | http://snomed.info/sct |
| 48 | 438 | DiagnosticReport | `DiagnosticReport.code` | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 49 | 452 | Observation | `Observation.code.coding` | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 50 | 460 | Observation | `Observation.interpretation.coding` | 302866003 | Hypoglycemia | http://snomed.info/sct |
| 51 | 463 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 52 | 468 | Observation | `Observation.interpretation.coding` | 714628002 | Prediabetes | http://snomed.info/sct |
| 53 | 473 | Observation | `Observation.interpretation.coding` | 73211009 | Diabetes mellitus | http://snomed.info/sct |
| 54 | 480 | Observation | `Observation.code.coding` | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 55 | 488 | Observation | `Observation.interpretation.coding` | 302866003 | Hypoglycemia | http://snomed.info/sct |
| 56 | 491 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 57 | 496 | Observation | `Observation.interpretation.coding` | 714628002 | Prediabetes | http://snomed.info/sct |
| 58 | 501 | Observation | `Observation.interpretation.coding` | 73211009 | Diabetes mellitus | http://snomed.info/sct |
| 59 | 508 | Observation | `Observation.code.coding` | 1521-4 | Glucose [Mass/volume] in Serum or Plasma --2 hours post meal | http://loinc.org |
| 60 | 518 | Observation | `Observation.interpretation.coding` | 302866003 | Hypoglycemia | http://snomed.info/sct |
| 61 | 521 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 62 | 526 | Observation | `Observation.interpretation.coding` | 714628002 | Prediabetes | http://snomed.info/sct |
| 63 | 531 | Observation | `Observation.interpretation.coding` | 73211009 | Diabetes mellitus | http://snomed.info/sct |
| 64 | 538 | Observation | `Observation.code.coding` | 4548-4 | Hemoglobin A1c/Hemoglobin.total in Blood | http://loinc.org |
| 65 | 546 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 66 | 549 | Observation | `Observation.interpretation.coding` | 714628002 | Prediabetes | http://snomed.info/sct |
| 67 | 554 | Observation | `Observation.interpretation.coding` | 73211009 | Diabetes mellitus | http://snomed.info/sct |
| 68 | 563 | Observation | `Observation.code.coding` | 34534-8 | 12 lead EKG panel | http://loinc.org |
| 69 | 564 | Observation | `Observation.valueCodeableConcept.coding` | 17621005 | Normal | http://snomed.info/sct |
| 70 | 565 | Observation | `Observation.interpretation.coding` | 164854000 | Electrocardiogram normal | http://snomed.info/sct |
| 71 | 566 | Observation | `Observation.valueCodeableConcept.coding` | 263654008 | Abnormal | http://snomed.info/sct |
| 72 | 567 | Observation | `Observation.interpretation.coding` | 102594003 | Electrocardiogram abnormal | http://snomed.info/sct |
| 73 | 575 | Observation | `Observation.component.code.coding` | 164854000 | Electrocardiogram normal | http://snomed.info/sct |
| 74 | 578 | Observation | `Observation.component.code.coding` | 26141007 | ST segment depression | http://snomed.info/sct |
| 75 | 581 | Observation | `Observation.component.code.coding` | 59931005 | Electrocardiogram normal | http://snomed.info/sct |
| 76 | 584 | Observation | `Observation.component.code.coding` | 164873001 | Electrocardiographic left ventricle hypertrophy | http://snomed.info/sct |
| 77 | 587 | Observation | `Observation.component.code.coding` | 164889003 | Electrocardiographic atrial fibrillation | http://snomed.info/sct |
| 78 | 590 | Observation | `Observation.component.code.coding` | 164918000 | Pathological Q wave | http://snomed.info/sct |
| 79 | 593 | Observation | `Observation.component.code.coding` | 76388001 | ST segment elevation | http://snomed.info/sct |
| 80 | 596 | Observation | `Observation.component.code.coding` | 102594003 | Electrocardiogram abnormal | http://snomed.info/sct |
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
| 96 | 697 | Observation | `Observation.valueCodeableConcept.coding` | 370992007 | Dyslipidemia | http://snomed.info/sct |
| 97 | 698 | Observation | `Observation.interpretation.coding` | 370992007 | Dyslipidemia | http://snomed.info/sct |
| 98 | 712 | Observation | `Observation.code.coding` | OC000173 | Prediksi Risiko PTM tanpa Pemeriksaan Laboratorium | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 99 | 713 | Observation | `Observation.interpretation.coding` | 723505004 | Low risk | http://snomed.info/sct |
| 100 | 716 | Observation | `Observation.interpretation.coding` | 25594002 | Moderate risk of | http://snomed.info/sct |
| 101 | 721 | Observation | `Observation.interpretation.coding` | 723509005 | High risk | http://snomed.info/sct |
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
| 112 | 835 | Observation | `Observation.method.coding` | 391483001 | Microscopy (acid fast bacilli) | http://snomed.info/sct |
| 113 | 836 | Observation | `Observation.valueCodeableConcept.coding` | 10828004 | Positive | http://snomed.info/sct |
| 114 | 837 | Observation | `Observation.valueCodeableConcept.coding` | 260385009 | Negative | http://snomed.info/sct |
| 115 | 849 | Observation | `Observation.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 116 | 850 | Observation | `Observation.method.coding` | 258066000 | Polymerase chain reaction technique | http://snomed.info/sct |
| 117 | 851 | Observation | `Observation.dataAbsentReason.coding` | OD000001 | Tidak ada hasil | http://terminology.kemkes.go.id/CodeSystem/data-absent-reason |
| 118 | 863 | Observation | `Observation.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 119 | 864 | Observation | `Observation.method.coding` | 258066000 | Polymerase chain reaction technique | http://snomed.info/sct |
| 120 | 865 | Observation | `Observation.dataAbsentReason.coding` | LA15841-2 | Invalid | http://loinc.org |
| 121 | 877 | Observation | `Observation.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 122 | 878 | Observation | `Observation.method.coding` | 258066000 | Polymerase chain reaction technique | http://snomed.info/sct |
| 123 | 879 | Observation | `Observation.dataAbsentReason.coding` | error | Error | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 124 | 891 | Observation | `Observation.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 125 | 892 | Observation | `Observation.method.coding` | 258066000 | Polymerase chain reaction technique | http://snomed.info/sct |
| 126 | 893 | Observation | `Observation.dataAbsentReason.coding` | OD000001 | Tidak ada hasil | http://terminology.kemkes.go.id/CodeSystem/data-absent-reason |
| 127 | 905 | Observation | `Observation.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 128 | 906 | Observation | `Observation.method.coding` | 258066000 | Polymerase chain reaction technique | http://snomed.info/sct |
| 129 | 907 | Observation | `Observation.valueCodeableConcept.coding` | LA11883-8 | Not Detected | http://loinc.org |
| 130 | 908 | Observation | `Observation.interpretation.coding` | NEG | Negative | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 131 | 920 | Observation | `Observation.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 132 | 921 | Observation | `Observation.method.coding` | 258066000 | Polymerase chain reaction technique | http://snomed.info/sct |
| 133 | 922 | Observation | `Observation.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 134 | 923 | Observation | `Observation.interpretation.coding` | NEG | Negative | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 135 | 935 | Observation | `Observation.code.coding` | 89372-7 | Mycobacterium tuberculosis complex rpoB gene rifAMPin resistance mutation [Presence] by Molecular method | http://loinc.org |
| 136 | 936 | Observation | `Observation.method.coding` | 258066000 | Polymerase chain reaction technique | http://snomed.info/sct |
| 137 | 937 | Observation | `Observation.valueCodeableConcept.coding` | LA11883-8 | Not Detected | http://loinc.org |
| 138 | 938 | Observation | `Observation.interpretation.coding` | X099770 | Rifampisin sensitive | http://terminology.kemkes.go.id/CodeSystem/examination |
| 139 | 950 | Observation | `Observation.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 140 | 951 | Observation | `Observation.method.coding` | 258066000 | Polymerase chain reaction technique | http://snomed.info/sct |
| 141 | 952 | Observation | `Observation.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 142 | 953 | Observation | `Observation.interpretation.coding` | NEG | Negative | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 143 | 965 | Observation | `Observation.code.coding` | 89372-7 | Mycobacterium tuberculosis complex rpoB gene rifAMPin resistance mutation [Presence] by Molecular method | http://loinc.org |
| 144 | 966 | Observation | `Observation.method.coding` | 258066000 | Polymerase chain reaction technique | http://snomed.info/sct |
| 145 | 967 | Observation | `Observation.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 146 | 968 | Observation | `Observation.interpretation.coding` | X099771 | Rifampisin resistan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 147 | 980 | Observation | `Observation.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 148 | 981 | Observation | `Observation.method.coding` | 258066000 | Polymerase chain reaction technique | http://snomed.info/sct |
| 149 | 982 | Observation | `Observation.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 150 | 983 | Observation | `Observation.interpretation.coding` | NEG | Negative | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 151 | 995 | Observation | `Observation.code.coding` | 89372-7 | Mycobacterium tuberculosis complex rpoB gene rifAMPin resistance mutation [Presence] by Molecular method | http://loinc.org |
| 152 | 996 | Observation | `Observation.method.coding` | 258066000 | Polymerase chain reaction technique | http://snomed.info/sct |
| 153 | 997 | Observation | `Observation.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 154 | 998 | Observation | `Observation.interpretation.coding` | X099772 | Rifampisin indeterminate | http://terminology.kemkes.go.id/CodeSystem/examination |
| 155 | 1010 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | female | Female | http://hl7.org/fhir/administrative-gender |
| 156 | 1011 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | male | Male | http://hl7.org/fhir/administrative-gender |
| 157 | 1023 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | SP000435 | <20 bungkus per tahun | http://terminology.kemkes.go.id/sp |
| 158 | 1024 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | SP000436 | 20-30 bungkus per tahun | http://terminology.kemkes.go.id/sp |
| 159 | 1025 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | SP000437 | >30 bungkus per tahun | http://terminology.kemkes.go.id/sp |
| 160 | 1044 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | 723505004 | Low risk | http://snomed.info/sct |
| 161 | 1045 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | 723509005 | High risk | http://snomed.info/sct |
| 162 | 1068 | Observation | `Observation.code.coding` | 13607009 | Manual examination of breast | http://snomed.info/sct |
| 163 | 1076 | Observation | `Observation.valueCodeableConcept.coding` | 290084006 | Breast normal | http://snomed.info/sct |
| 164 | 1077 | Observation | `Observation.valueCodeableConcept.coding` | 89164003 | Breast lump | http://snomed.info/sct |
| 165 | 1078 | Observation | `Observation.valueCodeableConcept.coding` | 134405005 | Suspected breast cancer | http://snomed.info/sct |
| 166 | 1085 | Observation | `Observation.code.coding` | 24601-7 | US Breast | http://loinc.org |
| 167 | 1093 | Observation | `Observation.valueCodeableConcept.coding` | 290084006 | Breast normal | http://snomed.info/sct |
| 168 | 1094 | Observation | `Observation.valueCodeableConcept.coding` | 367644007 | Simple cyst | http://snomed.info/sct |
| 169 | 1095 | Observation | `Observation.valueCodeableConcept.coding` | 449837001 | Complex cyst of breast | http://snomed.info/sct |
| 170 | 1110 | Observation | `Observation.code.coding` | 451024007 | Inspection of vagina using vaginal speculum | http://snomed.info/sct |
| 171 | 1118 | Observation | `Observation.valueCodeableConcept.coding` | 395100000 | No evidence of cancer found | http://snomed.info/sct |
| 172 | 1119 | Observation | `Observation.valueCodeableConcept.coding` | 315266007 | Suspected cervical cancer | http://snomed.info/sct |
| 173 | 1126 | Observation | `Observation.code.coding` | X099241 | Tes IVA | http://terminology.kemkes.go.id/CodeSystem/examination |
| 174 | 1134 | Observation | `Observation.valueCodeableConcept.coding` | 300557001 | Aceto-white reaction positive | http://snomed.info/sct |
| 175 | 1135 | Observation | `Observation.valueCodeableConcept.coding` | 300558006 | Aceto-white reaction negative | http://snomed.info/sct |
| 176 | 1142 | Observation | `Observation.code.coding` | 44550-2 | Human papilloma virus DNA [Presence] in Cervix by Probe | http://loinc.org |
| 177 | 1150 | Observation | `Observation.valueCodeableConcept.coding` | 787724008 | Human papillomavirus deoxyribonucleic acid not detected | http://snomed.info/sct |
| 178 | 1151 | Observation | `Observation.valueCodeableConcept.coding` | 787723002 | Human papillomavirus deoxyribonucleic acid detected | http://snomed.info/sct |
| 179 | 1152 | Observation | `Observation.valueCodeableConcept.coding` | OV000351 | Positif (HPV tipe onkogenik lain) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 180 | 1153 | Observation | `Observation.valueCodeableConcept.coding` | 708311006 | Deoxyribonucleic acid of Human papillomavirus 52 | http://snomed.info/sct |
| 181 | 1154 | Observation | `Observation.valueCodeableConcept.coding` | 708299006 | Deoxyribonucleic acid of Human papillomavirus 18 | http://snomed.info/sct |
| 182 | 1155 | Observation | `Observation.valueCodeableConcept.coding` | 708298003 | Deoxyribonucleic acid of Human papillomavirus 16 | http://snomed.info/sct |
| 183 | 1162 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | female | Female | http://hl7.org/fhir/administrative-gender |
| 184 | 1163 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | male | Male | http://hl7.org/fhir/administrative-gender |
| 185 | 1166 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | SP000438 | <45 thn | http://terminology.kemkes.go.id/sp |
| 186 | 1167 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | SP000439 | 45-65 thn | http://terminology.kemkes.go.id/sp |
| 187 | 1168 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | SP000440 | >65 tahun | http://terminology.kemkes.go.id/sp |
| 188 | 1171 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | QRI000032 | Memiliki diagnosis kanker >5 tahun yang lalu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 189 | 1172 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | QRI000033 | Memiliki diagnosis kanker <5 tahun yang lalu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 190 | 1173 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | QRI000034 | Tidak pernah didiagnosis menderita kanker | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 191 | 1176 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | QRI000036 | Tidak ada keluarga yang terdiagnosis kanker | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 192 | 1177 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 429011007 | Family history of malignant neoplasm of lung | http://snomed.info/sct |
| 193 | 1178 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | QRI000035 | Memiliki keluarga yang terdiagnosis kanker lain | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 194 | 1181 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | QRI000023 | Perokok/bekas perokok berhenti <10 tahun lalu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 195 | 1182 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | QRI000022 | Perokok aktif (dalam 1 tahun ini masih merokok) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 196 | 1183 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 266919005 | Never smoked tobacco | http://snomed.info/sct |
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
| 207 | 1202 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 161414005 | History of tuberculosis | http://snomed.info/sct |
| 208 | 1203 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 414415007 | History of chronic lung disease | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 209 | 1204 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 160258000 | No history of respiratory system disease | http://snomed.info/sct |
| 210 | 1207 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 723505004 | Low risk | http://snomed.info/sct |
| 211 | 1208 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 25594002 | Moderate risk of | http://snomed.info/sct |
| 212 | 1209 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 723509005 | High risk | http://snomed.info/sct |
| 213 | 1212 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 17621005 | Normal | http://snomed.info/sct |
| 214 | 1213 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 263654008 | Abnormal | http://snomed.info/sct |
| 215 | 1220 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | female | Female | http://hl7.org/fhir/administrative-gender |
| 216 | 1221 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | male | Male | http://hl7.org/fhir/administrative-gender |
| 217 | 1224 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | SP000441 | <50 tahun | http://terminology.kemkes.go.id/sp |
| 218 | 1225 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | SP000442 | 50 - 69 tahun | http://terminology.kemkes.go.id/sp |
| 219 | 1226 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | SP000443 | >= 70 tahun | http://terminology.kemkes.go.id/sp |
| 220 | 1237 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 723505004 | Low risk | http://snomed.info/sct |
| 221 | 1238 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 25594002 | Moderate risk of | http://snomed.info/sct |
| 222 | 1239 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.item.answer.valueCoding` | 723509005 | High risk | http://snomed.info/sct |
| 223 | 1254 | Observation | `Observation.code.coding` | 410007005 | Rectal examination | http://snomed.info/sct |
| 224 | 1262 | Observation | `Observation.valueCodeableConcept.coding` | 248523006 | Rectal mass | http://snomed.info/sct |
| 225 | 1263 | Observation | `Observation.valueCodeableConcept.coding` | 300870000 | No mass present | http://snomed.info/sct |
| 226 | 1270 | Observation | `Observation.code.coding` | 14563-1 | Hemoglobin.gastrointestinal [Presence] in Stool --1st specimen | http://loinc.org |
| 227 | 1278 | Observation | `Observation.valueCodeableConcept.coding` | 167667006 | Occult blood not detected in feces | http://snomed.info/sct |
| 228 | 1279 | Observation | `Observation.valueCodeableConcept.coding` | 59614000 | Occult blood detected in feces | http://snomed.info/sct |
| 229 | 1290 | Observation | `Observation.code.coding` | 247301006 | Finding of ability to hear whisper | http://snomed.info/sct |
| 230 | 1298 | Observation | `Observation.valueCodeableConcept.coding` | 275727004 | Hearing test normal | http://snomed.info/sct |
| 231 | 1299 | Observation | `Observation.valueCodeableConcept.coding` | 300221005 | Hearing for whisper impaired | http://snomed.info/sct |
| 232 | 1306 | Observation | `Observation.code.coding` | 76517002 | Otoscopy | http://snomed.info/sct |
| 233 | 1314 | Observation | `Observation.valueCodeableConcept.coding` | 275727004 | Hearing test normal | http://snomed.info/sct |
| 234 | 1315 | Observation | `Observation.valueCodeableConcept.coding` | 300221005 | Hearing for whisper impaired | http://snomed.info/sct |
| 235 | 1322 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.answer.valueCoding` | 400911007 | Tumbling E test | http://snomed.info/sct |
| 236 | 1323 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.answer.valueCoding` | 252973004 | Snellen chart assessment | http://snomed.info/sct |
| 237 | 1329 | Observation | `Observation.code.coding` | 400911007 | Tumbling E test | http://snomed.info/sct |
| 238 | 1330 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 239 | 1331 | Observation | `Observation.valueCodeableConcept.coding` | 45089002 | Normal vision | http://snomed.info/sct |
| 240 | 1332 | Observation | `Observation.interpretation.coding` | 45089002 | Normal vision | http://snomed.info/sct |
| 241 | 1333 | Observation | `Observation.valueCodeableConcept.coding` | 397540003 | Visual impairment | http://snomed.info/sct |
| 242 | 1334 | Observation | `Observation.interpretation.coding` | 397540003 | Visual impairment | http://snomed.info/sct |
| 243 | 1345 | Observation | `Observation.code.coding` | 252973004 | Snellen chart assessment | http://snomed.info/sct |
| 244 | 1346 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 245 | 1347 | Observation | `Observation.valueCodeableConcept.coding` | 45089002 | Normal vision | http://snomed.info/sct |
| 246 | 1348 | Observation | `Observation.interpretation.coding` | 45089002 | Normal vision | http://snomed.info/sct |
| 247 | 1349 | Observation | `Observation.valueCodeableConcept.coding` | 397540003 | Visual impairment | http://snomed.info/sct |
| 248 | 1350 | Observation | `Observation.interpretation.coding` | 397540003 | Visual impairment | http://snomed.info/sct |
| 249 | 1364 | Observation | `Observation.code.coding` | 441841000 | Pinhole visual acuity test | http://loinc.org |
| 250 | 1365 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 251 | 1366 | Observation | `Observation.valueCodeableConcept.coding` | 39021009 | Disorder of refraction | http://snomed.info/sct |
| 252 | 1367 | Observation | `Observation.interpretation.coding` | 39021009 | Disorder of refraction | http://snomed.info/sct |
| 253 | 1368 | Observation | `Observation.valueCodeableConcept.coding` | OI000044 | Kelainan organik | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 254 | 1369 | Observation | `Observation.interpretation.coding` | OI000044 | Kelainan organik | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 255 | 1383 | Observation | `Observation.code.coding` | 40137007 | Pupil light reflex | http://snomed.info/sct |
| 256 | 1384 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 257 | 1385 | Observation | `Observation.valueCodeableConcept.coding` | OV000393 | Suspek katarak | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 258 | 1386 | Observation | `Observation.valueCodeableConcept.coding` | 371405004 | Disorder of eye proper | http://snomed.info/sct |
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
| 277 | 1474 | Observation | `Observation.valueCodeableConcept.coding` | 11214006 | Reactive | http://snomed.info/sct |
| 278 | 1475 | Observation | `Observation.valueCodeableConcept.coding` | 131194007 | Non-Reactive | http://snomed.info/sct |
| 279 | 1488 | Observation | `Observation.code.coding` | 72376-7 | Hepatitis C virus Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 280 | 1489 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 281 | 1490 | Observation | `Observation.valueCodeableConcept.coding` | 11214006 | Reactive | http://snomed.info/sct |
| 282 | 1491 | Observation | `Observation.valueCodeableConcept.coding` | 131194007 | Non-Reactive | http://snomed.info/sct |
| 283 | 1524 | Observation | `Observation.code.coding` | 1920-8 | Aspartate aminotransferase [Enzymatic activity/volume] in Serum or Plasma | http://loinc.org |
| 284 | 1525 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 285 | 1541 | Observation | `Observation.code.coding[x]` | 26515-7 | Platelets [#/volume] in Blood | http://loinc.org |
| 286 | 1557 | Observation | `Observation.code.coding[x]` | 86465-2 | AST to platelet ratio index in Serum and Blood by calculation | http://loinc.org |
| 287 | 1561 | Observation | `Observation.interpretation.coding` | N | Normal | http://termi nology.hl7. org/CodeSy stem/v3-Ob servationIn terpretation |
| 288 | 1566 | Observation | `Observation.interpretation.coding` | 112674009 | Fibrosis | http://snomed.info/sct |
| 289 | 1569 | Observation | `Observation.interpretation.coding` | 19943007 | Cirrhosis of liver | http://snomed.info/sct |
| 290 | 1579 | Observation | `Observation.code.coding` | TK000144 | Rencana menikah 1 tahun ke depan | http://terminology.kemkes.go.id |
| 291 | 1604 | Observation | `Observation.code.coding` | 30352-9 | Hemoglobin [Mass/volume] in Capillary blood | http://loinc.org |
| 292 | 1612 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 293 | 1615 | Observation | `Observation.interpretation.coding` | 271737000 | Anemia | http://snomed.info/sct |
| 294 | 1629 | Observation | `Observation.code.coding` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 295 | 1630 | Observation | `Observation.valueCodeableConcept.coding` | LA15255-5 | Reactive | http://loinc.org |
| 296 | 1631 | Observation | `Observation.valueCodeableConcept.coding` | LA15256-3 | Nonreactive | http://loinc.org |
| 297 | 1650 | Observation | `Observation.code.coding` | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 298 | 1651 | Observation | `Observation.valueCodeableConcept.coding` | LA15255-5 | Reactive | http://loinc.org |
| 299 | 1652 | Observation | `Observation.valueCodeableConcept.coding` | LA15256-3 | Nonreactive | http://loinc.org |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 134 |
| http://loinc.org | 56 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 31 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 27 |
| http://terminology.kemkes.go.id | 20 |
| http://terminology.kemkes.go.id/sp | 9 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 8 |
| http://hl7.org/fhir/administrative-gender | 6 |
| http://terminology.kemkes.go.id/CodeSystem/examination | 4 |
| http://terminology.kemkes.go.id/CodeSystem/data-absent-reason | 2 |
| http://hl7.org/fhir/sid/icd-10 | 1 |
| http://termi nology.hl7. org/CodeSy stem/v3-Ob servationIn terpretation | 1 |
| **Total** | **299** |

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
