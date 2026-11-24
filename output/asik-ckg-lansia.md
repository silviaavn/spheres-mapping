# Output Form: ASIK - CKG Lansia (versi 27 April 2026)

Sumber: `mapping/phdt-data-dictionary-asik-ckg-lansia.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-asik-ckg-lansia.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 95 |
| Code (`jumlah code` = 1) | 458 |
| Code unik (code + CodeSystem) | 278 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 11 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–39 | Patient | – | – | _pasien_name_ → `Patient.name.text` (2, tanpa BQ)<br>_nik_ → `Patient.identifier.value` (5, tanpa BQ)<br>_pasien_id_ → `Patient.identifier.value` (8, tanpa BQ)<br>_jenis_kelamin_ → `Patient.gender` (10, tanpa BQ)<br>_tgl_lahir_ → `Patient.birthDate` (12, tanpa BQ)<br>_no_handphone_ → `Patient.telecom` (13, tanpa BQ)<br>_status_perkawinan_ → `Patient.maritalStatus.coding` (16, tanpa BQ)<br>_kabkota_name_ → `Patient.address.city` (26, tanpa BQ)<br>_provinsi_ → `Patient.address.extension.extension.valueCode` (30, tanpa BQ)<br>_kabkota_ → `Patient.address.extension.extension.valueCode` (33, tanpa BQ)<br>_kecamatan_ → `Patient.address.extension.extension.valueCode` (36, tanpa BQ)<br>_kelurahan_ → `Patient.address.extension.extension.valueCode` (39, tanpa BQ) |
| 2 | 78–98 | Encounter | – | – | _tgl_pelayanan_ → `Encounter.identifier` (78, tanpa BQ) |
| 3 | 99–106 | Condition | Z01.8 | Other specified special examinations | – |
| 4 | 117–128 | Observation | 424144002.0 | Current chronological age | _age_now_ → `Observation.valueQuantity.value` (120, tanpa BQ) |
| 5 | 129–140 | Observation | TK000144 | Rencana menikah 1 tahun ke depan | _rencana_menikah_dalam_kurun_waktu_1_tahun_ → `Observation.valueBoolean` (132, tanpa BQ) |
| 6 | 141–212 | QuestionnaireResponse | – | – | _apakah_merokok_dalam_setahun_terakhir_ → `QuestionnaireResponse.item.item.text` (153, tanpa BQ)<br>_sudah_berapa_tahun_merokok_ → `QuestionnaireResponse.item.item.answer.item.text` (159, tanpa BQ)<br>_berapa_batang_rokok_yang_dihisap_dalam_sehari_ → `QuestionnaireResponse.item.item.answer.item.text` (163, tanpa BQ)<br>_apakah_pernah_merokok_sebelumnya_ → `QuestionnaireResponse.item.item.text` (178, tanpa BQ)<br>_berapa_lama_merokok_sebelumnya_ → `QuestionnaireResponse.item.item.answer.item.text` (182, tanpa BQ)<br>_kapan_anda_berhenti_merokok_ → `QuestionnaireResponse.item.item.answer.item.text` (186, tanpa BQ)<br>_apakah_terpapar_asap_rokok_sebulan_terakhir_ → `QuestionnaireResponse.item.item.text` (190, tanpa BQ)<br>_apakah_rutin_melakukan_olahraga_ → `QuestionnaireResponse.item.item.text` (194, tanpa BQ)<br>_berapa_kali_berolahraga_dalam_seminggu_ → `QuestionnaireResponse.item.item.answer.item.text` (198, tanpa BQ)<br>_berapa_menit_berolahraga_ → `QuestionnaireResponse.item.item.answer.item.text` (201, tanpa BQ)<br>_tingkat_aktivitas_fisik_ → `QuestionnaireResponse.item.item.answer.item.linkId` (203, tanpa BQ)<br>_berat_badan_kg_ → `QuestionnaireResponse.item.item.item.text` (210, tanpa BQ)<br>_tinggi_badan_cm_ → `QuestionnaireResponse.item.item.item.text` (226, tanpa BQ)<br>_index_massa_tubuh_ → `QuestionnaireResponse.item.item.item.text` (242, tanpa BQ)<br>_lingkar_perut_ → `QuestionnaireResponse.item.item.item.text` (273, tanpa BQ)<br>_apakah_pernah_dinyatakan_tekanan_darah_tinggi_ → `QuestionnaireResponse.item.item.linkId` (296, tanpa BQ)<br>_sistolik_ → `QuestionnaireResponse.item.item.item.answer.valueReference.reference` (302, tanpa BQ)<br>_diastolik_ → `QuestionnaireResponse.item.item.item.answer.valueReference.reference` (360, tanpa BQ)<br>_tekanan_darah_ → `QuestionnaireResponse.item.item.item.answer.valueReference.reference` (418, tanpa BQ)<br>_apakah_pernah_dinyatakan_diabetes_kencing_manis_ → `QuestionnaireResponse.item.item.text` (471, tanpa BQ)<br>_gula_darah_sewaktu_ → `QuestionnaireResponse.item.item.item.answer.valueReference.display` (477, tanpa BQ)<br>_gula_darah_puasa_ → `QuestionnaireResponse.item.item.item.answer.valueReference.display` (507, tanpa BQ)<br>_gula_darah_puasa_lanjutan_ → `QuestionnaireResponse.item.item.item.answer.valueReference.display` (521, tanpa BQ)<br>_gula_darah_2_jam_pp_ → `QuestionnaireResponse.item.item.item.answer.valueReference.reference` (548, tanpa BQ)<br>_pemeriksaan_hb1ac_ → `QuestionnaireResponse.item.item.item.answer.valueReference.display` (563, tanpa BQ)<br>_hasil_pemeriksaan_ekg_ → `QuestionnaireResponse.item.item.text` (604, tanpa BQ)<br>_hasil_interpretasi_dislipidemia_ → `QuestionnaireResponse.item.item.answer.valueReference.reference` (735, tanpa BQ)<br>_prediksi_risiko_penyakit_kardiovaskular_ → `QuestionnaireResponse.item.item.linkId` (751, tanpa BQ)<br>_hasil_pemeriksaan_ureum_ → `QuestionnaireResponse.item.item.answer.valueReference.reference` (778, tanpa BQ)<br>_hasil_pemeriksaan_kreatinin_ → `QuestionnaireResponse.item.item.answer.valueReference.reference` (810, tanpa BQ)<br>_hasil_pemeriksaan_elfg_ckd_epi_ → `QuestionnaireResponse.item.item.answer.valueReference.reference` (842, tanpa BQ)<br>_hasil_pemeriksaan_gigi_karies_ → `QuestionnaireResponse.item.item.item.text` (882, tanpa BQ)<br>_hasil_pemeriksaan_gigi_hilang_dicabut_ → `QuestionnaireResponse.item.item.item.text` (886, tanpa BQ)<br>_hasil_pemeriksaan_pocket_periodontal_ → `QuestionnaireResponse.item.item.answer.item.text` (893, tanpa BQ)<br>_hasil_pemeriksaan_gigi_goyang_ → `QuestionnaireResponse.item.item.answer.item.text` (897, tanpa BQ)<br>_apakah_mengalami_batuk_lebih_dari_2_minggu_ → `QuestionnaireResponse.item.item.item.linkId` (906, tanpa BQ)<br>_apakah_sering_bertemu_dengan_penderita_tbc_ → `QuestionnaireResponse.item.item.item.linkId` (910, tanpa BQ)<br>_riwayat_kontak_tuberkulosis_ → `QuestionnaireResponse.item.item.item.linkId` (914, tanpa BQ)<br>_hasil_pemeriksaan_bta_ → `QuestionnaireResponse.item.item.answer.valueReference.display` (954, tanpa BQ)<br>_hasil_pemeriksaan_tb_tcm_ → `QuestionnaireResponse.item.item.answer.valueReference.display` (984, tanpa BQ)<br>_hasil_pemeriksaan_tb_tcm_ → `QuestionnaireResponse.item.item.answer.valueReference.display` (998, tanpa BQ)<br>_hasil_pemeriksaan_tb_tcm_ → `QuestionnaireResponse.item.item.answer.valueReference.display` (1012, tanpa BQ)<br>_hasil_pemeriksaan_tb_tcm_ → `QuestionnaireResponse.item.item.answer.valueReference.display` (1026, tanpa BQ)<br>_hasil_pemeriksaan_tb_tcm_ → `QuestionnaireResponse.item.item.answer.valueReference.display` (1040, tanpa BQ)<br>_hasil_pemeriksaan_tb_tcm_ → `QuestionnaireResponse.item.item.answer.valueReference.display` (1055, tanpa BQ)<br>_hasil_pemeriksaan_tb_tcm_ → `QuestionnaireResponse.item.item.answer.valueReference.display` (1070, tanpa BQ)<br>_hasil_pemeriksaan_tb_tcm_ → `QuestionnaireResponse.item.item.answer.valueReference.display` (1085, tanpa BQ)<br>_hasil_pemeriksaan_tb_tcm_ → `QuestionnaireResponse.item.item.answer.valueReference.display` (1100, tanpa BQ)<br>_hasil_pemeriksaan_tb_tcm_ → `QuestionnaireResponse.item.item.answer.valueReference.display` (1115, tanpa BQ)<br>_hasil_pemeriksaan_tb_tcm_ → `QuestionnaireResponse.item.item.answer.valueReference.display` (1130, tanpa BQ)<br>_metode_pemeriksaan_ → `QuestionnaireResponse.item.item.item.text` (1145, tanpa BQ)<br>_usia_puma_ → `QuestionnaireResponse.item.item.item.linkId` (1156, tanpa BQ)<br>_apakah_mempunyai_riwayat_merokok_ → `QuestionnaireResponse.item.item.item.linkId` (1161, tanpa BQ)<br>_berapa_bungkus_rokok_dalam_1_tahun_ → `QuestionnaireResponse.item.item.item.linkId` (1165, tanpa BQ)<br>_apakah_pernah_merasa_napas_pendek_saat_jalan_cepat_ → `QuestionnaireResponse.item.item.item.linkId` (1170, tanpa BQ)<br>_apakah_mempunyai_dahak_atau_kesulitan_mengeluarkan_dahak_ → `QuestionnaireResponse.item.item.item.linkId` (1174, tanpa BQ)<br>_apakah_biasanya_batuk_ketika_tidak_menderita_flu_ → `QuestionnaireResponse.item.item.item.linkId` (1178, tanpa BQ)<br>_apakah_pernah_melakukan_spirometri_ → `QuestionnaireResponse.item.item.item.linkId` (1182, tanpa BQ)<br>_hasil_skor_puma_ → `QuestionnaireResponse.item.item.item.linkId` (1186, tanpa BQ)<br>_jenis_pemeriksaan_ → `QuestionnaireResponse.item.item.answer.item.text` (1197, tanpa BQ)<br>_hasil_pemeriksaan_sadanis_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1206, tanpa BQ)<br>_hasil_pemeriksaan_usg_payudara_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1223, tanpa BQ)<br>_apakah_pernah_melakukan_hubungan_intim_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1244, tanpa BQ)<br>_hasil_pemeriksaan_inspekulo_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1248, tanpa BQ)<br>_hasil_pemeriksaan_iva_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1264, tanpa BQ)<br>_hasil_pemeriksaan_hpv_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1280, tanpa BQ)<br>_jenis_kelamin_1_ → `QuestionnaireResponse.item.item.answer.item.text` (1366, tanpa BQ)<br>_usia_ → `QuestionnaireResponse.item.item.item.linkId` (1369, tanpa BQ)<br>_apakah_pernah_didiagnosa_menderita_kanker_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1374, tanpa BQ)<br>_apakah_ada_keluarga_yang_didiagnosa_menderita_kanker_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1379, tanpa BQ)<br>_riwayat_merokok_atau_paparan_asap_rokok_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1384, tanpa BQ)<br>_riwayat_tempat_kerja_mengandung_zat_karsinogenik_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1390, tanpa BQ)<br>_lingkungan_tempat_tinggal_berpotensi_tinggi_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1395, tanpa BQ)<br>_lingkungan_tempat_tinggal_berpotensi_tinggi_1_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1400, tanpa BQ)<br>_apakah_pernah_didiagnosis_penyakit_paru_kronik_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1405, tanpa BQ)<br>_apakah_pernah_didiagnosis_penyakit_paru_kronik_1_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1410, tanpa BQ)<br>_hasil_skrining_kanker_paru_ → `QuestionnaireResponse.item.item.answer.item.text` (1416, tanpa BQ)<br>_jenis_kelamin_apcs_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1423, tanpa BQ)<br>_usia_skor_apcs_ → `QuestionnaireResponse.item.item.item.linkId` (1427, tanpa BQ)<br>_kankes_usus_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1432, tanpa BQ)<br>_riwayat_merokok_apcs_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1436, tanpa BQ)<br>_skor_apcs_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1440, tanpa BQ)<br>_kesediaan_colok_dubur_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1449, tanpa BQ)<br>_hasil_colok_dubur_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1453, tanpa BQ)<br>_hasil_darah_samar_ → `QuestionnaireResponse.item.item.answer.item.linkId` (1469, tanpa BQ)<br>_hasil_pemeriksaan_tajam_pendengaran_ → `QuestionnaireResponse.item.answer.item.linkId` (1489, tanpa BQ)<br>_hasil_pemeriksaan_otoskop_penala_ → `QuestionnaireResponse.item.answer.item.linkId` (1506, tanpa BQ)<br>_hasil_pemeriksaan_pinhole_ → `QuestionnaireResponse.item.answer.item.linkId` (1611, tanpa BQ)<br>_hasil_pemeriksaan_pupil_ → `QuestionnaireResponse.item.answer.item.text` (1631, tanpa BQ)<br>_seberapa_sering_tidak_bersemangat_dalam_2_minggu_ → `QuestionnaireResponse.item.answer.item.text` (1670, tanpa BQ)<br>_seberapa_sering_merasa_murung_tertekan_putus_asa_dalam_2_minggu_ → `QuestionnaireResponse.item.answer.item.text` (1676, tanpa BQ)<br>_seberapa_sering_merasa_gugup_cemas_gelisah_dalam_2_minggu_ → `QuestionnaireResponse.item.answer.item.text` (1682, tanpa BQ)<br>_seberapa_sering_merasa_khawatir_dalam_2_minggu_ → `QuestionnaireResponse.item.answer.item.text` (1688, tanpa BQ)<br>_gejala_depresi_ → `QuestionnaireResponse.item.answer.item.text` (1694, tanpa BQ)<br>_gejala_kecemasan_ → `QuestionnaireResponse.item.answer.item.text` (1698, tanpa BQ)<br>_apakah_hasil_hepatitis_b_mendapat_positif_ → `QuestionnaireResponse.item.answer.item.linkId` (1714, tanpa BQ)<br>_apakah_memiliki_keluarga_yang_menderita_hepatitis_b_ → `QuestionnaireResponse.item.answer.item.linkId` (1718, tanpa BQ)<br>_apakah_pernah_melakukan_hubungan_intim_dengan_bebas_ → `QuestionnaireResponse.item.answer.item.linkId` (1722, tanpa BQ)<br>_apakah_pernah_menerima_transfusi_darah_ → `QuestionnaireResponse.item.answer.item.linkId` (1726, tanpa BQ)<br>_apakah_pernah_menjalani_cuci_darah_ → `QuestionnaireResponse.item.answer.item.linkId` (1730, tanpa BQ)<br>_apakah_pernah_menggunakan_narkoba_ → `QuestionnaireResponse.item.answer.item.linkId` (1734, tanpa BQ)<br>_apakah_anda_menderita_hiv_ → `QuestionnaireResponse.item.answer.item.linkId` (1738, tanpa BQ)<br>_apakah_anda_mendapat_pengobatan_hepatitis_c_dan_tidak_sembuh_ → `QuestionnaireResponse.item.answer.item.linkId` (1742, tanpa BQ)<br>_hasil_rapid_test_hepatitis_b_ → `QuestionnaireResponse.item.answer.item.linkId` (1746, tanpa BQ)<br>_hasil_rapid_test_hepatitis_c_ → `QuestionnaireResponse.item.answer.item.linkId` (1763, tanpa BQ)<br>_faktor_risiko_hepatitis_b_ → `QuestionnaireResponse.item.answer.item.linkId` (1779, tanpa BQ)<br>_faktor_risiko_hepatitis_c_ → `QuestionnaireResponse.item.answer.item.linkId` (1783, tanpa BQ)<br>_faktor_risiko_hepatitis_ → `QuestionnaireResponse.item.answer.item.linkId` (1787, tanpa BQ)<br>_apakah_hasil_kolestrol_tinggi_ → `QuestionnaireResponse.item.answer.item.linkId` (1822, tanpa BQ)<br>_nilai_sgot_ → `QuestionnaireResponse.item.answer.item.linkId` (1826, tanpa BQ)<br>_pemeriksaan_trombosit_ → `QuestionnaireResponse.item.answer.item.linkId` (1843, tanpa BQ)<br>_hasil_apri_score_ → `QuestionnaireResponse.item.answer.item.linkId` (1859, tanpa BQ)<br>_rencana_menikah_dalam_kurun_waktu_1_tahun_ → `QuestionnaireResponse.item.answer.valueBoolean` (1898, tanpa BQ)<br>_rencana_menikah_dalam_kurun_waktu_1_tahun_ → `QuestionnaireResponse.item.answer.valueBoolean` (1899, tanpa BQ)<br>_hasil_pemeriksaan_rapid_test_hb_ → `QuestionnaireResponse.item.answer.item.item.text` (1907, tanpa BQ)<br>_hasil_pemeriksaan_rapid_test_sifilis_ → `QuestionnaireResponse.item.answer.item.item.text` (1932, tanpa BQ)<br>_hasil_pemeriksaan_rapid_test_hiv_ → `QuestionnaireResponse.item.answer.item.item.text` (1953, tanpa BQ)<br>_apakah_dapat_mengingat_tiga_kata_ → `QuestionnaireResponse.item.item.text` (2038, tanpa BQ)<br>_tanggal_berapa_hari_ini_dimana_saat_ini_ → `QuestionnaireResponse.item.item.text` (2042, tanpa BQ)<br>_apakah_dapat_mengingat_tiga_kata_sebelumnya_ → `QuestionnaireResponse.item.item.text` (2047, tanpa BQ)<br>_hasil_interpretasi_skilas_penurunan_kognitif_ → `QuestionnaireResponse.item.item.text` (2051, tanpa BQ)<br>_apakah_dapat_berdiri_dari_kursi_skilas_ → `QuestionnaireResponse.item.item.text` (2057, tanpa BQ)<br>_apakah_berat_badan_berkurang_ → `QuestionnaireResponse.item.item.text` (2063, tanpa BQ)<br>_apakah_nafsu_makan_hilang_ → `QuestionnaireResponse.item.item.text` (2067, tanpa BQ)<br>_apakah_lila_kurang_dari_21_cm_ → `QuestionnaireResponse.item.item.text` (2071, tanpa BQ)<br>_hasil_interpretasi_skilas_malnutrisi_ → `QuestionnaireResponse.item.item.text` (2077, tanpa BQ)<br>_apakah_merasa_sedih_dalam_2_minggu_terakhir_ → `QuestionnaireResponse.item.item.text` (2083, tanpa BQ)<br>_apakah_minat_berkurang_dalam_berkegiatan_dalam_2_minggu_terakhir_ → `QuestionnaireResponse.item.item.text` (2087, tanpa BQ)<br>_hasil_interpretasi_gejala_depresi_ → `QuestionnaireResponse.item.item.text` (2091, tanpa BQ)<br>_apakah_sulit_membuat_keputusan_ → `QuestionnaireResponse.item.linkId` (2255, tanpa BQ)<br>_apakah_sudah_tidak_menekuni_hobi_ → `QuestionnaireResponse.item.linkId` (2261, tanpa BQ)<br>_apakah_keluar_mengulang_pertanyaan_cerita_pernyataan_yang_sama_ → `QuestionnaireResponse.item.linkId` (2266, tanpa BQ)<br>_apakah_kesulitan_belajar_menggunakan_perkakas_dan_peralatan_ → `QuestionnaireResponse.item.linkId` (2271, tanpa BQ)<br>_apakah_lupa_nama_bulan_atau_tahun_ → `QuestionnaireResponse.item.linkId` (2276, tanpa BQ)<br>_apakah_kesulitan_mengatur_keuangan_ → `QuestionnaireResponse.item.linkId` (2281, tanpa BQ)<br>_apakah_sulit_mengingat_janji_ → `QuestionnaireResponse.item.linkId` (2286, tanpa BQ)<br>_apakah_mengalami_gangguan_memori_dan_pemikiran_yang_konsisten_ → `QuestionnaireResponse.item.linkId` (2291, tanpa BQ)<br>_hasil_interpretasi_ad_8_ → `QuestionnaireResponse.item.linkId` (2296, tanpa BQ)<br>_apakah_asupan_makan_turun_dalam_3_bulan_terakhir_ → `QuestionnaireResponse.item.text` (2372, tanpa BQ)<br>_apakah_berat_badan_turun_dalam_3_bulan_terakhir_ → `QuestionnaireResponse.item.item.linkId` (2378, tanpa BQ)<br>_kemampuan_melakukan_mobilitas_ → `QuestionnaireResponse.item.item.linkId` (2384, tanpa BQ)<br>_apakah_menderita_stress_atau_penyakit_akut_dalam_3_bulan_terakhir_ → `QuestionnaireResponse.item.item.linkId` (2389, tanpa BQ)<br>_apakah_mengalami_masalah_neuropsikologis_ → `QuestionnaireResponse.item.item.linkId` (2393, tanpa BQ)<br>_nilai_imt_ → `QuestionnaireResponse.item.item.linkId` (2398, tanpa BQ)<br>_lingkar_betis_ → `QuestionnaireResponse.item.item.linkId` (2425, tanpa BQ)<br>_hasil_interpretasi_mnasf_ → `QuestionnaireResponse.item.item.linkId` (2445, tanpa BQ) |
| 7 | 213–224 | Observation | 29463-7 | Body weight | – |
| 8 | 229–240 | Observation | 8302-2 | Body height | – |
| 9 | 245–271 | Observation | 39156-5 | Body mass index (BMI) [Ratio] | – |
| 10 | 276–295 | Observation | vital-signs | Abdominal circumference | – |
| 11 | 304–347 | Observation | 8480-6 | Systolic blood pressure | – |
| 12 | 348–359 | Observation | 8480-6 | – | – |
| 13 | 362–405 | Observation | 8462-4 | Diastolic blood pressure | – |
| 14 | 406–417 | Observation | 8462-4 | Diastolic blood pressure | – |
| 15 | 420–445 | Observation | 268607006.0 | Hypertension risk level | – |
| 16 | 446–469 | Observation | 268607006.0 | Hypertension risk level | – |
| 17 | 478–490 | Observation | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | – |
| 18 | 493–505 | Observation | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | – |
| 19 | 508–519 | Observation | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | – |
| 20 | 522–547 | Observation | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | – |
| 21 | 550–561 | Observation | 1521-4 | Glucose [Mass/volume] in Serum or Plasma --2 hours post meal | – |
| 22 | 564–584 | Observation | 4548-4 | Hemoglobin A1c/Hemoglobin.total in Blood | – |
| 23 | 607–644 | Observation | 34534-8 | 12 lead EKG panel | _hasil_detail_pemeriksaan_ekg_ → `Observation.component.code.coding` (621, tanpa BQ) |
| 24 | 649–668 | Observation | 2093-3 | Cholesterol [Mass/volume] in Serum or Plasma | _kolesterol_total_ → `Observation.valueQuantity.value` (652, tanpa BQ)<br>_interpretasi_kolesterol_total_ → `Observation.interpretation.coding` (661, tanpa BQ) |
| 25 | 671–690 | Observation | 2085-9 | Cholesterol in HDL [Mass/volume] in Serum or Plasma | _masukkan_nilai_hdl_ → `Observation.valueQuantity.value` (674, tanpa BQ)<br>_interpretasi_hdl_ → `Observation.interpretation.coding` (676, tanpa BQ) |
| 26 | 693–712 | Observation | 2085-9 | Cholesterol in HDL [Mass/volume] in Serum or Plasma | _masukkan_nilai_ldl_ → `Observation.valueQuantity.value` (696, tanpa BQ)<br>_interpretasi_ldl_ → `Observation.interpretation.coding` (698, tanpa BQ) |
| 27 | 715–734 | Observation | 2571-8 | Triglyceride [Mass/volume] in Serum or Plasma | _masukkan_nilai_trigliserida_ → `Observation.valueQuantity.value` (718, tanpa BQ)<br>_hasil_interpretasi_trigliserida_ → `Observation.interpretation.coding` (720, tanpa BQ) |
| 28 | 737–750 | Observation | 100898-6 | Lipid panel - Serum or Plasma | – |
| 29 | 755–775 | Observation | OC000173 | Prediksi Risiko PTM tanpa Pemeriksaan Laboratorium | – |
| 30 | 780–793 | Observation | 20977-5 | Urea [Mass/volume] in Blood | – |
| 31 | 796–809 | Observation | 1754-1 | Albumin [Mass/volume] in Urine | – |
| 32 | 812–825 | Observation | 2160-0 | Creatinine [Mass/volume] in Serum or Plasma | – |
| 33 | 828–841 | Observation | 2149-3 | Creatine [Mass/volume] in Urine | – |
| 34 | 844–861 | Observation | 62238-1 | Glomerular filtration rate/1.73 sq M.predicted [Volume Rate/Area] in Serum, Plasma or Blood by Creatinine-based formula (CKD-EPI) | – |
| 35 | 864–878 | Observation | 32294-1 | Albumin/Creatinine [Ratio] in Urine | – |
| 36 | 921–930 | Procedure | 424489006.0 | Mantoux test | – |
| 37 | 932–943 | Observation | 23539-0 | Tuberculosis reaction wheal [Diameter] --3 days post dose mammalian tuberculin intradermal | – |
| 38 | 955–967 | Observation | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | – |
| 39 | 970–982 | Observation | 13956-8 | Mycobacterium tuberculosis DNA [Presence] in Specimen by NAA with probe detection | – |
| 40 | 985–996 | Observation | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | – |
| 41 | 999–1010 | Observation | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | – |
| 42 | 1013–1024 | Observation | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | – |
| 43 | 1027–1038 | Observation | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | – |
| 44 | 1041–1053 | Observation | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | – |
| 45 | 1056–1068 | Observation | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | – |
| 46 | 1071–1083 | Observation | 89372-7 | Mycobacterium tuberculosis complex rpoB gene rifAMPin resistance mutation [Presence] by Molecular method | – |
| 47 | 1086–1098 | Observation | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | – |
| 48 | 1101–1113 | Observation | 89372-7 | Mycobacterium tuberculosis complex rpoB gene rifAMPin resistance mutation [Presence] by Molecular method | – |
| 49 | 1116–1128 | Observation | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | – |
| 50 | 1131–1143 | Observation | 89372-7 | Mycobacterium tuberculosis complex rpoB gene rifAMPin resistance mutation [Presence] by Molecular method | – |
| 51 | 1210–1222 | Observation | 13607009.0 | Manual examination of breast | – |
| 52 | 1227–1239 | Observation | 24601-7 | US Breast | – |
| 53 | 1252–1263 | Observation | 451024007.0 | Inspection of vagina using vaginal speculum | – |
| 54 | 1268–1279 | Observation | X099241 | Tes IVA | – |
| 55 | 1284–1300 | Observation | 44550-2 | Human papilloma virus DNA [Presence] in Cervix by Probe | – |
| 56 | 1303–1315 | Observation | 77399-4 | Human papilloma virus 16 DNA [Presence] in Cervix by NAA with probe detection | – |
| 57 | 1318–1330 | Observation | 77400-0 | Human papilloma virus 18 DNA [Presence] in Cervix by NAA with probe detection | – |
| 58 | 1333–1345 | Observation | 95534-4 | Human papilloma virus 52 DNA [Presence] in Cervix by NAA with probe detection | – |
| 59 | 1348–1360 | Observation | OV000351 | Positif (HPV tipe onkogenik lain) | – |
| 60 | 1457–1468 | Observation | 410007005.0 | Rectal examination | – |
| 61 | 1473–1484 | Observation | 14563-1 | Hemoglobin.gastrointestinal [Presence] in Stool --1st specimen | – |
| 62 | 1493–1505 | Observation | 247301006.0 | Finding of ability to hear whisper | – |
| 63 | 1510–1521 | Observation | 76517002.0 | Otoscopy | – |
| 64 | 1524–1535 | Observation | 18070006.0 | Impacted cerumen | – |
| 65 | 1538–1549 | Observation | 129127001.0 | Infection of ear | – |
| 66 | 1552–1563 | Observation | SP000828 | Tes Penala | – |
| 67 | 1575–1592 | Observation | 400911007.0 | Tumbling E test | _pemeriksaan_visus_e_tumbling_ → `Observation.valueCodeableConcept.coding` (1579, tanpa BQ) |
| 68 | 1593–1610 | Observation | 252973004.0 | Snellen chart assessment | _pemeriksaan_visus_snellen_chart_ → `Observation.valueCodeableConcept.coding` (1597, tanpa BQ) |
| 69 | 1614–1629 | Observation | 441841000.0 | Pinhole visual acuity test | – |
| 70 | 1633–1647 | Observation | 40137007.0 | Pupil light reflex | – |
| 71 | 1651–1664 | Observation | 53524009.0 | Ophthalmoscopy | – |
| 72 | 1749–1762 | Observation | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | – |
| 73 | 1766–1778 | Observation | 72376-7 | Hepatitis C virus Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | – |
| 74 | 1794–1805 | Observation | 395197008.0 | Hepatitis C viral load | – |
| 75 | 1829–1842 | Observation | 1920-8 | Aspartate aminotransferase [Enzymatic activity/volume] in Serum or Plasma | – |
| 76 | 1846–1858 | Observation | – | – | – |
| 77 | 1862–1883 | Observation | – | – | – |
| 78 | 1884–1895 | Observation | TK000144 | Rencana menikah 1 tahun ke depan | _rencana_menikah_dalam_kurun_waktu_1_tahun_ → `Observation.valueBoolean` (1887, tanpa BQ) |
| 79 | 1909–1924 | Observation | 30352-9 | Hemoglobin [Mass/volume] in Capillary blood | – |
| 80 | 1934–1945 | Observation | 22464-2 | Reagin Ab [Presence] in Specimen | – |
| 81 | 1955–1966 | Observation | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | – |
| 82 | 1981–1994 | Observation | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | – |
| 83 | 2012–2024 | Observation | 106936-8 | Treponema pallidum IgG+IgM Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | – |
| 84 | 2094–2126 | Observation | 48542-5 | Geriatric depression scale (GDS) panel | _hasil_interpretasi_gejala_depresi_1_ → `Observation.valueQuantity.value` (2098, tanpa BQ)<br>_apakah_merasa_puas_dengan_kehidupan_ → `Observation.component.code.coding` (2115, tanpa BQ)<br>_apakah_sering_merasa_bosan_ → `Observation.component.code.coding` (2118, tanpa BQ)<br>_apakah_sering_merasa_tidak_berdaya_ → `Observation.component.code.coding` (2121, tanpa BQ)<br>_apakah_merasa_tidak_berharga_ → `Observation.component.code.coding` (2124, tanpa BQ) |
| 85 | 2127–2199 | Observation | 96762-0 | Barthel index panel | _hasil_intrepretasi_adl_ → `Observation.valueRange.low.value` (2131, tanpa BQ)<br>_apakah_dapat_mengendalikan_rangsang_bab_ → `Observation.component.code.coding` (2160, tanpa BQ)<br>_apakah_dapat_mengendalikan_rangsang_bak_ → `Observation.component.code.coding` (2164, tanpa BQ)<br>_apakah_dapat_membersihkan_diri_sendiri_ → `Observation.component.code.coding` (2168, tanpa BQ)<br>_apakah_dapat_menggunakan_jamban_sendiri_ → `Observation.component.code.coding` (2171, tanpa BQ)<br>_apakah_dapat_makan_sendiri_ → `Observation.component.code.coding` (2175, tanpa BQ)<br>_apakah_dapat_merubah_sikap_dari_berbaring_ke_duduk_sendiri_ → `Observation.component.code.coding` (2179, tanpa BQ)<br>_apakah_dapat_berjalan_sendiri_ → `Observation.component.code.coding` (2184, tanpa BQ)<br>_apakah_dapat_berpakaian_sendiri_ → `Observation.component.code.coding` (2189, tanpa BQ)<br>_apakah_dapat_turun_naik_tangga_sendiri_ → `Observation.component.code.coding` (2193, tanpa BQ)<br>_apakah_dapat_mandi_sendiri_ → `Observation.component.code.coding` (2197, tanpa BQ) |
| 86 | 2200–2214 | Observation | 72234-8 | Mini-Cog | _hasil_mengingat_3_versi_kata_ → `Observation.valueCodeableConcept.coding` (2203, tanpa BQ)<br>_sudah_mendengarkan_dan_mengingat_3_versi_kata_ → `Observation.note` (2214, tanpa BQ) |
| 87 | 2215–2231 | Observation | 79150-9 | Clock drawing panel [GPCOG] | _apakah_dapat_menggambar_sesuai_perintah_ → `Observation.component.valueBoolean` (2220, tanpa BQ) |
| 88 | 2232–2245 | Observation | 72233-0 | Total score [Mini-Cog] | _hasil_interpretasi_mini_cog_ → `Observation.valueQuantity` (2236, tanpa BQ) |
| 89 | 2299–2311 | Observation | 71722-3 | Total score [AD8] | – |
| 90 | 2312–2335 | Observation | 66248-6 | Balance test [PhenX] | _tes_keseimbangan_berdiri_berdampingan_ → `Observation.component.code.coding` (2315, tanpa BQ)<br>_tes_keseimbangan_berdiri_semi_tandem_ → `Observation.component.code.coding` (2319, tanpa BQ)<br>_tes_keseimbangan_berdiri_tandem_ → `Observation.component.code.coding` (2323, tanpa BQ) |
| 91 | 2336–2361 | Observation | 714283000.0 | Short Physical Performance Battery | _tes_kecepatan_berjalan_ → `Observation.component.code.coding` (2340, tanpa BQ)<br>_tes_berdiri_dari_kursi_ → `Observation.component.code.coding` (2346, tanpa BQ)<br>_hasil_interpretasi_spbb_ → `Observation.valueQuantity` (2352, tanpa BQ) |
| 92 | 2407–2424 | Observation | 39156-5 | Body mass index (BMI) [Ratio] | – |
| 93 | 2432–2444 | Observation | 8283-4 | Calf - right Maximum circumference | – |
| 94 | 2448–2465 | Observation | TK000195 | Mini Nutritional Assessment (MNA) SF | – |
| 95 | 2466–2481 | Observation | TK000195 | Mini Nutritional Assessment (MNA) SF | – |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 90 |
| Patient | 1 |
| Encounter | 1 |
| Condition | 1 |
| QuestionnaireResponse | 1 |
| Procedure | 1 |
| **Total** | **95** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 101 | Condition | `Condition.code.coding` | Z01.8 | Other specified special examinations | http://hl7.org/fhir/sid/icd-10 |
| 2 | 119 | Observation | `Observation.code.coding` | 424144002.0 | Current chronological age | http://snomed.info/sct |
| 3 | 131 | Observation | `Observation.code.coding` | TK000144 | Rencana menikah 1 tahun ke depan | http://terminology.kemkes.go.id |
| 4 | 215 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 5 | 231 | Observation | `Observation.code.coding` | 8302-2 | Body height | http://loinc.org |
| 6 | 247 | Observation | `Observation.code.coding` | 39156-5 | Body mass index (BMI) [Ratio] | http://loinc.org |
| 7 | 248 | Observation | `Observation.interpretation.coding` | 248342006.0 | Underweight | http://snomed.info/sct |
| 8 | 251 | Observation | `Observation.interpretation.coding` | 43664005.0 | Normal weight | http://snomed.info/sct |
| 9 | 256 | Observation | `Observation.interpretation.coding` | 238131007.0 | Overweight | http://snomed.info/sct |
| 10 | 261 | Observation | `Observation.interpretation.coding` | 414915002.0 | Obese | http://snomed.info/sct |
| 11 | 278 | Observation | `Observation.code.coding` | vital-signs | Abdominal circumference | http://snomed.info/sct |
| 12 | 288 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 13 | 292 | Observation | `Observation.interpretation.coding` | 248311001.0 | Central obesity | http://snomed.info/sct |
| 14 | 307 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 15 | 317 | Observation | `Observation.interpretation.coding` | OI000040 | Tekanan Darah Optimal | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 16 | 322 | Observation | `Observation.interpretation.coding` | 2004005.0 | Normal blood pressure | http://snomed.info/sct |
| 17 | 327 | Observation | `Observation.interpretation.coding` | OI000041 | Tekanan Darah Normal Tinggi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 18 | 332 | Observation | `Observation.interpretation.coding` | 827069000.0 | Stage 1 hypertension | http://snomed.info/sct |
| 19 | 337 | Observation | `Observation.interpretation.coding` | 827068008.0 | Stage 1 hypertension | http://snomed.info/sct |
| 20 | 342 | Observation | `Observation.interpretation.coding` | OI000042 | Hipertensi Derajat 3 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 21 | 350 | Observation | `Observation.code.coding` | 8480-6 |  |  |
| 22 | 365 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://snomed.info/sct |
| 23 | 375 | Observation | `Observation.interpretation.coding` | OI000040 | Tekanan Darah Optimal | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 24 | 380 | Observation | `Observation.interpretation.coding` | 2004005.0 | Normal blood pressure | http://snomed.info/sct |
| 25 | 385 | Observation | `Observation.interpretation.coding` | OI000041 | Tekanan Darah Normal Tinggi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 26 | 390 | Observation | `Observation.interpretation.coding` | 827069000.0 | Stage 1 hypertension | http://snomed.info/sct |
| 27 | 395 | Observation | `Observation.interpretation.coding` | 827068008.0 | Stage 1 hypertension | http://snomed.info/sct |
| 28 | 400 | Observation | `Observation.interpretation.coding` | OI000042 | Hipertensi Derajat 3 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 29 | 408 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure |  |
| 30 | 423 | Observation | `Observation.code.coding` | 268607006.0 | Hypertension risk level | http://snomed.info/sct |
| 31 | 435 | Observation | `Observation.interpretation.coding` | OI000040 | Tekanan Darah Optimal | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 32 | 436 | Observation | `Observation.interpretation.coding` | 2004005.0 | Normal blood pressure | http://snomed.info/sct |
| 33 | 437 | Observation | `Observation.interpretation.coding` | OI000041 | Tekanan Darah Normal Tinggi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 34 | 438 | Observation | `Observation.interpretation.coding` | 827069000.0 | Stage 1 hypertension | http://snomed.info/sct |
| 35 | 439 | Observation | `Observation.interpretation.coding` | 827068008.0 | Stage 2 hypertension | http://snomed.info/sct |
| 36 | 440 | Observation | `Observation.interpretation.coding` | OI000042 | Hipertensi Derajat 3 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 37 | 441 | Observation | `Observation.interpretation.coding` | 56218007.0 | Systolic hypertension | http://snomed.info/sct |
| 38 | 442 | Observation | `Observation.interpretation.coding` | 2004005.0 | Normal blood pressure | http://snomed.info/sct |
| 39 | 443 | Observation | `Observation.interpretation.coding` | 702817009.0 | Prehypertension | http://snomed.info/sct |
| 40 | 444 | Observation | `Observation.interpretation.coding` | 24184005.0 | Blood pressure above reference range | http://snomed.info/sct |
| 41 | 448 | Observation | `Observation.code.coding` | 268607006.0 | Hypertension risk level | http://snomed.info/sct |
| 42 | 460 | Observation | `Observation.interpretation.coding` | OI000040 | Tekanan Darah Optimal | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 43 | 461 | Observation | `Observation.interpretation.coding` | 2004005.0 | Normal blood pressure | http://snomed.info/sct |
| 44 | 462 | Observation | `Observation.interpretation.coding` | OI000041 | Tekanan Darah Normal Tinggi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 45 | 463 | Observation | `Observation.interpretation.coding` | 827069000.0 | Stage 1 hypertension | http://snomed.info/sct |
| 46 | 464 | Observation | `Observation.interpretation.coding` | 827068008.0 | Stage 2 hypertension | http://snomed.info/sct |
| 47 | 465 | Observation | `Observation.interpretation.coding` | OI000042 | Hipertensi Derajat 3 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 48 | 466 | Observation | `Observation.interpretation.coding` | 56218007.0 | Systolic hypertension | http://snomed.info/sct |
| 49 | 467 | Observation | `Observation.interpretation.coding` | 2004005.0 | Normal blood pressure | http://snomed.info/sct |
| 50 | 468 | Observation | `Observation.interpretation.coding` | 702817009.0 | Prehypertension | http://snomed.info/sct |
| 51 | 469 | Observation | `Observation.interpretation.coding` | 24184005.0 | Blood pressure above reference range | http://snomed.info/sct |
| 52 | 481 | Observation | `Observation.code.coding` | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 53 | 496 | Observation | `Observation.code.coding` | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 54 | 510 | Observation | `Observation.code.coding` | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 55 | 524 | Observation | `Observation.code.coding` | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 56 | 532 | Observation | `Observation.interpretation.coding` | 302866003.0 | Hypoglycemia | http://snomed.info/sct |
| 57 | 535 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 58 | 540 | Observation | `Observation.interpretation.coding` | 714628002.0 | Prediabetes | http://snomed.info/sct |
| 59 | 545 | Observation | `Observation.interpretation.coding` | 73211009.0 | Diabetes mellitus | http://snomed.info/sct |
| 60 | 552 | Observation | `Observation.code.coding` | 1521-4 | Glucose [Mass/volume] in Serum or Plasma --2 hours post meal | http://loinc.org |
| 61 | 566 | Observation | `Observation.code.coding` | 4548-4 | Hemoglobin A1c/Hemoglobin.total in Blood | http://loinc.org |
| 62 | 574 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 63 | 577 | Observation | `Observation.interpretation.coding` | 714628002.0 | Prediabetes | http://snomed.info/sct |
| 64 | 582 | Observation | `Observation.interpretation.coding` | 73211009.0 | Diabetes mellitus | http://snomed.info/sct |
| 65 | 590 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | 162650008.0 | Examination not done on subject of record | http://snomed.info/sct |
| 66 | 591 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | 714628002.0 | Prediabetes | http://snomed.info/sct |
| 67 | 592 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | 73211009.0 | Diabetes mellitus | http://snomed.info/sct |
| 68 | 593 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | 80394007.0 | Hyperglycemia | http://snomed.info/sct |
| 69 | 594 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | 302866003.0 | Hypoglycemia | http://snomed.info/sct |
| 70 | 597 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | 162650008.0 | Examination not done on subject of record | http://snomed.info/sct |
| 71 | 598 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | 714628002.0 | Prediabetes | http://snomed.info/sct |
| 72 | 599 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | 73211009.0 | Diabetes mellitus | http://snomed.info/sct |
| 73 | 600 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | 80394007.0 | Hyperglycemia | http://snomed.info/sct |
| 74 | 601 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | 302866003.0 | Hypoglycemia | http://snomed.info/sct |
| 75 | 602 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | 261665006.0 | Unknown | http://snomed.info/sct |
| 76 | 609 | Observation | `Observation.code.coding` | 34534-8 | 12 lead EKG panel | http://loinc.org |
| 77 | 610 | Observation | `Observation.valueCodeableConcept.coding` | 17621005.0 | Normal | http://snomed.info/sct |
| 78 | 611 | Observation | `Observation.interpretation.coding` | 164854000 | Electrocardiogram normal | http://snomed.info/sct |
| 79 | 612 | Observation | `Observation.valueCodeableConcept.coding` | 263654008 | Abnormal | http://snomed.info/sct |
| 80 | 613 | Observation | `Observation.interpretation.coding` | 102594003.0 | Electrocardiogram abnormal | http://snomed.info/sct |
| 81 | 621 | Observation | `Observation.component.code.coding` | 164854000 | Electrocardiogram normal | http://snomed.info/sct |
| 82 | 624 | Observation | `Observation.component.code.coding` | 26141007 | ST segment depression | http://snomed.info/sct |
| 83 | 627 | Observation | `Observation.component.code.coding` | 59931005 | Electrocardiogram normal | http://snomed.info/sct |
| 84 | 630 | Observation | `Observation.component.code.coding` | 164873001 | Electrocardiographic left ventricle hypertrophy | http://snomed.info/sct |
| 85 | 633 | Observation | `Observation.component.code.coding` | 164889003 | Electrocardiographic atrial fibrillation | http://snomed.info/sct |
| 86 | 636 | Observation | `Observation.component.code.coding` | 164918000 | Pathological Q wave | http://snomed.info/sct |
| 87 | 639 | Observation | `Observation.component.code.coding` | 76388001 | ST segment elevation | http://snomed.info/sct |
| 88 | 642 | Observation | `Observation.component.code.coding` | 102594003.0 | Electrocardiogram abnormal | http://snomed.info/sct |
| 89 | 651 | Observation | `Observation.code.coding` | 2093-3 | Cholesterol [Mass/volume] in Serum or Plasma | http://loinc.org |
| 90 | 661 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 91 | 665 | Observation | `Observation.interpretation.coding` | H | High | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 92 | 673 | Observation | `Observation.code.coding` | 2085-9 | Cholesterol in HDL [Mass/volume] in Serum or Plasma | http://loinc.org |
| 93 | 676 | Observation | `Observation.interpretation.coding` | L | Low | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 94 | 680 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 95 | 695 | Observation | `Observation.code.coding` | 2085-9 | Cholesterol in HDL [Mass/volume] in Serum or Plasma | http://loinc.org |
| 96 | 698 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 97 | 702 | Observation | `Observation.interpretation.coding` | H | High | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 98 | 717 | Observation | `Observation.code.coding` | 2571-8 | Triglyceride [Mass/volume] in Serum or Plasma | http://loinc.org |
| 99 | 720 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 100 | 724 | Observation | `Observation.interpretation.coding` | H | High | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 101 | 739 | Observation | `Observation.code.coding` | 100898-6 | Lipid panel - Serum or Plasma | http://loinc.org |
| 102 | 740 | Observation | `Observation.valueCodeableConcept.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 103 | 741 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 104 | 742 | Observation | `Observation.valueCodeableConcept.coding` | 370992007.0 | Dyslipidemia | http://snomed.info/sct |
| 105 | 743 | Observation | `Observation.interpretation.coding` | 370992007.0 | Dyslipidemia | http://snomed.info/sct |
| 106 | 757 | Observation | `Observation.code.coding` | OC000173 | Prediksi Risiko PTM tanpa Pemeriksaan Laboratorium | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 107 | 758 | Observation | `Observation.interpretation.coding` | 723505004.0 | Low risk | http://snomed.info/sct |
| 108 | 761 | Observation | `Observation.interpretation.coding` | 25594002.0 | Moderate risk of | http://snomed.info/sct |
| 109 | 766 | Observation | `Observation.interpretation.coding` | 723509005.0 | High risk | http://snomed.info/sct |
| 110 | 782 | Observation | `Observation.code.coding` | 20977-5 | Urea [Mass/volume] in Blood | http://loinc.org |
| 111 | 785 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 112 | 786 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 113 | 798 | Observation | `Observation.code.coding` | 1754-1 | Albumin [Mass/volume] in Urine | http://loinc.org |
| 114 | 801 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 115 | 802 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 116 | 814 | Observation | `Observation.code.coding` | 2160-0 | Creatinine [Mass/volume] in Serum or Plasma | http://loinc.org |
| 117 | 817 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 118 | 818 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 119 | 830 | Observation | `Observation.code.coding` | 2149-3 | Creatine [Mass/volume] in Urine | http://loinc.org |
| 120 | 833 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 121 | 834 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 122 | 846 | Observation | `Observation.code.coding` | 62238-1 | Glomerular filtration rate/1.73 sq M.predicted [Volume Rate/Area] in Serum, Plasma or Blood by Creatinine-based formula (CKD-EPI) | http://loinc.org |
| 123 | 849 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 124 | 852 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 125 | 866 | Observation | `Observation.code.coding` | 32294-1 | Albumin/Creatinine [Ratio] in Urine | http://loinc.org |
| 126 | 869 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 127 | 870 | Observation | `Observation.interpretation.coding` | 735623008.0 | Grade A2 albuminuria | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 128 | 871 | Observation | `Observation.interpretation.coding` | 735624002.0 | Grade A3 albuminuria | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 129 | 922 | Procedure | `Procedure.code.coding` | 424489006.0 | Mantoux test | http://snomed.info/sct |
| 130 | 934 | Observation | `Observation.code.coding` | 23539-0 | Tuberculosis reaction wheal [Diameter] --3 days post dose mammalian tuberculin intradermal | http://loinc.org |
| 131 | 935 | Observation | `Observation.valueCodeableConcept.coding` | 268376005.0 | Mantoux: positive | http://snomed.info/sct |
| 132 | 936 | Observation | `Observation.valueCodeableConcept.coding` | 268375009.0 | Mantoux: negative | http://snomed.info/sct |
| 133 | 946 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | TK000161 | Dugaan Tuberkulosis klinis | http://terminology.kemkes.go.id |
| 134 | 957 | Observation | `Observation.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 135 | 958 | Observation | `Observation.method.coding` | 391483001.0 | Microscopy (acid fast bacilli) | http://snomed.info/sct |
| 136 | 959 | Observation | `Observation.valueCodeableConcept.coding` | 10828004.0 | Positive | http://snomed.info/sct |
| 137 | 960 | Observation | `Observation.valueCodeableConcept.coding` | 260385009.0 | Negative | http://snomed.info/sct |
| 138 | 972 | Observation | `Observation.code.coding` | 13956-8 | Mycobacterium tuberculosis DNA [Presence] in Specimen by NAA with probe detection | http://loinc.org |
| 139 | 973 | Observation | `Observation.method.coding` | 405262001.0 | Point of care testing | http://snomed.info/sct |
| 140 | 974 | Observation | `Observation.valueCodeableConcept.coding` | 10828004.0 | Positive | http://snomed.info/sct |
| 141 | 975 | Observation | `Observation.valueCodeableConcept.coding` | 260385009.0 | Negative | http://snomed.info/sct |
| 142 | 987 | Observation | `Observation.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 143 | 988 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 144 | 1001 | Observation | `Observation.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 145 | 1002 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 146 | 1015 | Observation | `Observation.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 147 | 1016 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 148 | 1029 | Observation | `Observation.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 149 | 1030 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 150 | 1043 | Observation | `Observation.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 151 | 1044 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 152 | 1045 | Observation | `Observation.valueCodeableConcept.coding` | LA11883-8 | Not Detected | http://loinc.org |
| 153 | 1046 | Observation | `Observation.interpretation.coding` | NEG | Negative | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 154 | 1058 | Observation | `Observation.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 155 | 1059 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 156 | 1060 | Observation | `Observation.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 157 | 1061 | Observation | `Observation.interpretation.coding` | NEG | Negative | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 158 | 1073 | Observation | `Observation.code.coding` | 89372-7 | Mycobacterium tuberculosis complex rpoB gene rifAMPin resistance mutation [Presence] by Molecular method | http://loinc.org |
| 159 | 1074 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 160 | 1075 | Observation | `Observation.valueCodeableConcept.coding` | LA11883-8 | Not Detected | http://loinc.org |
| 161 | 1076 | Observation | `Observation.interpretation.coding` | X099770 | Rifampisin sensitive | http://terminology.kemkes.go.id/CodeSystem/examination |
| 162 | 1088 | Observation | `Observation.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 163 | 1089 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 164 | 1090 | Observation | `Observation.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 165 | 1091 | Observation | `Observation.interpretation.coding` | NEG | Negative | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 166 | 1103 | Observation | `Observation.code.coding` | 89372-7 | Mycobacterium tuberculosis complex rpoB gene rifAMPin resistance mutation [Presence] by Molecular method | http://loinc.org |
| 167 | 1104 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 168 | 1105 | Observation | `Observation.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 169 | 1106 | Observation | `Observation.interpretation.coding` | X099771 | Rifampisin resistan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 170 | 1118 | Observation | `Observation.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 171 | 1119 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 172 | 1120 | Observation | `Observation.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 173 | 1121 | Observation | `Observation.interpretation.coding` | NEG | Negative | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 174 | 1133 | Observation | `Observation.code.coding` | 89372-7 | Mycobacterium tuberculosis complex rpoB gene rifAMPin resistance mutation [Presence] by Molecular method | http://loinc.org |
| 175 | 1134 | Observation | `Observation.method.coding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 176 | 1135 | Observation | `Observation.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 177 | 1136 | Observation | `Observation.interpretation.coding` | X099772 | Rifampisin indeterminate | http://terminology.kemkes.go.id/CodeSystem/examination |
| 178 | 1146 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | 258066000.0 | Polymerase chain reaction technique | http://snomed.info/sct |
| 179 | 1147 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | 391483001.0 | Microscopy (acid fast bacilli) | http://snomed.info/sct |
| 180 | 1148 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | 405262001.0 | Point of care testing | http://snomed.info/sct |
| 181 | 1149 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | 162650008.0 | Examination not done on subject of record | http://snomed.info/sct |
| 182 | 1154 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | female | Female | http://hl7.org/fhir/administrative-gender |
| 183 | 1155 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | male | Male | http://hl7.org/fhir/administrative-gender |
| 184 | 1167 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | SP000435 | <20 bungkus per tahun | http://terminology.kemkes.go.id/sp |
| 185 | 1168 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | SP000436 | 20-30 bungkus per tahun | http://terminology.kemkes.go.id/sp |
| 186 | 1169 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | SP000437 | >30 bungkus per tahun | http://terminology.kemkes.go.id/sp |
| 187 | 1188 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | 723505004.0 | Low risk | http://snomed.info/sct |
| 188 | 1189 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | 723509005.0 | High risk | http://snomed.info/sct |
| 189 | 1212 | Observation | `Observation.code.coding` | 13607009.0 | Manual examination of breast | http://snomed.info/sct |
| 190 | 1220 | Observation | `Observation.valueCodeableConcept.coding` | 290084006.0 | Breast normal | http://snomed.info/sct |
| 191 | 1221 | Observation | `Observation.valueCodeableConcept.coding` | 89164003.0 | Breast lump | http://snomed.info/sct |
| 192 | 1222 | Observation | `Observation.valueCodeableConcept.coding` | 134405005.0 | Suspected breast cancer | http://snomed.info/sct |
| 193 | 1229 | Observation | `Observation.code.coding` | 24601-7 | US Breast | http://loinc.org |
| 194 | 1237 | Observation | `Observation.valueCodeableConcept.coding` | 290084006.0 | Breast normal | http://snomed.info/sct |
| 195 | 1238 | Observation | `Observation.valueCodeableConcept.coding` | 367644007.0 | Simple cyst | http://snomed.info/sct |
| 196 | 1239 | Observation | `Observation.valueCodeableConcept.coding` | 449837001.0 | Complex cyst of breast | http://snomed.info/sct |
| 197 | 1254 | Observation | `Observation.code.coding` | 451024007.0 | Inspection of vagina using vaginal speculum | http://snomed.info/sct |
| 198 | 1262 | Observation | `Observation.valueCodeableConcept.coding` | 395100000.0 | No evidence of cancer found | http://snomed.info/sct |
| 199 | 1263 | Observation | `Observation.valueCodeableConcept.coding` | 315266007.0 | Suspected cervical cancer | http://snomed.info/sct |
| 200 | 1270 | Observation | `Observation.code.coding` | X099241 | Tes IVA | http://terminology.kemkes.go.id/CodeSystem/examination |
| 201 | 1278 | Observation | `Observation.valueCodeableConcept.coding` | 300557001.0 | Aceto-white reaction positive | http://snomed.info/sct |
| 202 | 1279 | Observation | `Observation.valueCodeableConcept.coding` | 300558006.0 | Aceto-white reaction negative | http://snomed.info/sct |
| 203 | 1287 | Observation | `Observation.code.coding` | 44550-2 | Human papilloma virus DNA [Presence] in Cervix by Probe | http://loinc.org |
| 204 | 1295 | Observation | `Observation.valueCodeableConcept.coding` | 787724008.0 | Human papillomavirus deoxyribonucleic acid not detected | http://snomed.info/sct |
| 205 | 1296 | Observation | `Observation.valueCodeableConcept.coding` | 787723002.0 | Human papillomavirus deoxyribonucleic acid detected | http://snomed.info/sct |
| 206 | 1297 | Observation | `Observation.valueCodeableConcept.coding` | OV000351 | Positif (HPV tipe onkogenik lain) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 207 | 1298 | Observation | `Observation.valueCodeableConcept.coding` | 708311006.0 | Deoxyribonucleic acid of Human papillomavirus 52 | http://snomed.info/sct |
| 208 | 1299 | Observation | `Observation.valueCodeableConcept.coding` | 708299006.0 | Deoxyribonucleic acid of Human papillomavirus 18 | http://snomed.info/sct |
| 209 | 1300 | Observation | `Observation.valueCodeableConcept.coding` | 708298003.0 | Deoxyribonucleic acid of Human papillomavirus 16 | http://snomed.info/sct |
| 210 | 1306 | Observation | `Observation.code.coding` | 77399-4 | Human papilloma virus 16 DNA [Presence] in Cervix by NAA with probe detection | http://loinc.org |
| 211 | 1321 | Observation | `Observation.code.coding` | 77400-0 | Human papilloma virus 18 DNA [Presence] in Cervix by NAA with probe detection | http://loinc.org |
| 212 | 1336 | Observation | `Observation.code.coding` | 95534-4 | Human papilloma virus 52 DNA [Presence] in Cervix by NAA with probe detection | http://loinc.org |
| 213 | 1351 | Observation | `Observation.code.coding` | OV000351 | Positif (HPV tipe onkogenik lain) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 214 | 1459 | Observation | `Observation.code.coding` | 410007005.0 | Rectal examination | http://snomed.info/sct |
| 215 | 1467 | Observation | `Observation.valueCodeableConcept.coding` | 248523006.0 | Rectal mass | http://snomed.info/sct |
| 216 | 1468 | Observation | `Observation.valueCodeableConcept.coding` | 300870000.0 | No mass present | http://snomed.info/sct |
| 217 | 1475 | Observation | `Observation.code.coding` | 14563-1 | Hemoglobin.gastrointestinal [Presence] in Stool --1st specimen | http://loinc.org |
| 218 | 1483 | Observation | `Observation.valueCodeableConcept.coding` | 167667006.0 | Occult blood not detected in feces | http://snomed.info/sct |
| 219 | 1484 | Observation | `Observation.valueCodeableConcept.coding` | 59614000.0 | Occult blood detected in feces | http://snomed.info/sct |
| 220 | 1495 | Observation | `Observation.code.coding` | 247301006.0 | Finding of ability to hear whisper | http://snomed.info/sct |
| 221 | 1503 | Observation | `Observation.valueCodeableConcept.coding` | 275727004.0 | Hearing test normal | http://snomed.info/sct |
| 222 | 1504 | Observation | `Observation.valueCodeableConcept.coding` | 300221005.0 | Hearing for whisper impaired | http://snomed.info/sct |
| 223 | 1512 | Observation | `Observation.code.coding` | 76517002.0 | Otoscopy | http://snomed.info/sct |
| 224 | 1520 | Observation | `Observation.valueCodeableConcept.coding` | 164178007.0 | Ear examination normal | http://snomed.info/sct |
| 225 | 1521 | Observation | `Observation.valueCodeableConcept.coding` | 699116001.0 | Ear examination abnormal | http://snomed.info/sct |
| 226 | 1526 | Observation | `Observation.code.coding` | 18070006.0 | Impacted cerumen | http://terminology.kemkes.go.id/sp |
| 227 | 1540 | Observation | `Observation.code.coding` | 129127001.0 | Infection of ear | http://terminology.kemkes.go.id/sp |
| 228 | 1554 | Observation | `Observation.code.coding` | SP000828 | Tes Penala | http://terminology.kemkes.go.id/sp |
| 229 | 1562 | Observation | `Observation.valueCodeableConcept.coding` | 164178007.0 | Ear examination normal | http://snomed.info/sct |
| 230 | 1563 | Observation | `Observation.valueCodeableConcept.coding` | 699116001.0 | Ear examination abnormal | http://snomed.info/sct |
| 231 | 1577 | Observation | `Observation.code.coding` | 400911007.0 | Tumbling E test | http://snomed.info/sct |
| 232 | 1579 | Observation | `Observation.valueCodeableConcept.coding` | 45089002.0 | Normal vision | http://snomed.info/sct |
| 233 | 1580 | Observation | `Observation.interpretation.coding` | 45089002.0 | Normal vision | http://snomed.info/sct |
| 234 | 1581 | Observation | `Observation.valueCodeableConcept.coding` | 397540003.0 | Visual impairment | http://snomed.info/sct |
| 235 | 1582 | Observation | `Observation.interpretation.coding` | 397540003.0 | Visual impairment | http://snomed.info/sct |
| 236 | 1583 | Observation | `Observation.valueCodeableConcept.coding` | 164728001.0 | Visual testing abnormal | http://snomed.info/sct |
| 237 | 1584 | Observation | `Observation.interpretation.coding` | 164728001.0 | Visual testing abnormal | http://snomed.info/sct |
| 238 | 1595 | Observation | `Observation.code.coding` | 252973004.0 | Snellen chart assessment | http://snomed.info/sct |
| 239 | 1597 | Observation | `Observation.valueCodeableConcept.coding` | 45089002.0 | Normal vision | http://snomed.info/sct |
| 240 | 1598 | Observation | `Observation.valueCodeableConcept.coding` | 397543001.0 | Mild visual impairment | http://snomed.info/sct |
| 241 | 1599 | Observation | `Observation.valueCodeableConcept.coding` | 397542006.0 | Moderate visual impairment | http://snomed.info/sct |
| 242 | 1600 | Observation | `Observation.valueCodeableConcept.coding` | 397541004.0 | Severe visual impairment | http://snomed.info/sct |
| 243 | 1601 | Observation | `Observation.interpretation.coding` | 45089002.0 | Normal vision | http://snomed.info/sct |
| 244 | 1602 | Observation | `Observation.interpretation.coding` | 397540003.0 | Visual impairment | http://snomed.info/sct |
| 245 | 1616 | Observation | `Observation.code.coding` | 441841000.0 | Pinhole visual acuity test | http://loinc.org |
| 246 | 1618 | Observation | `Observation.valueCodeableConcept.coding` | 39021009.0 | Disorder of refraction | http://snomed.info/sct |
| 247 | 1619 | Observation | `Observation.interpretation.coding` | 39021009.0 | Disorder of refraction | http://snomed.info/sct |
| 248 | 1620 | Observation | `Observation.valueCodeableConcept.coding` | OI000044 | Kelainan organik | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 249 | 1621 | Observation | `Observation.interpretation.coding` | OI000044 | Kelainan organik | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 250 | 1635 | Observation | `Observation.code.coding` | 40137007.0 | Pupil light reflex | http://snomed.info/sct |
| 251 | 1637 | Observation | `Observation.valueCodeableConcept.coding` | 301950001.0 | Pupil normal | http://snomed.info/sct |
| 252 | 1638 | Observation | `Observation.valueCodeableConcept.coding` | OV000393 | Suspek katarak | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 253 | 1639 | Observation | `Observation.valueCodeableConcept.coding` | 371405004.0 | Disorder of eye proper | http://snomed.info/sct |
| 254 | 1653 | Observation | `Observation.code.coding` | 53524009.0 | Ophthalmoscopy | http://snomed.info/sct |
| 255 | 1655 | Observation | `Observation.valueCodeableConcept.coding` | 164734008.0 | Fundoscopy normal | http://snomed.info/sct |
| 256 | 1656 | Observation | `Observation.valueCodeableConcept.coding` | 164735009.0 | Fundoscopy abnormal | http://snomed.info/sct |
| 257 | 1751 | Observation | `Observation.code.coding` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 258 | 1753 | Observation | `Observation.valueCodeableConcept.coding` | 11214006.0 | Reactive | http://snomed.info/sct |
| 259 | 1754 | Observation | `Observation.valueCodeableConcept.coding` | 131194007.0 | Non-Reactive | http://snomed.info/sct |
| 260 | 1768 | Observation | `Observation.code.coding` | 72376-7 | Hepatitis C virus Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 261 | 1770 | Observation | `Observation.valueCodeableConcept.coding` | 11214006.0 | Reactive | http://snomed.info/sct |
| 262 | 1771 | Observation | `Observation.valueCodeableConcept.coding` | 131194007.0 | Non-Reactive | http://snomed.info/sct |
| 263 | 1796 | Observation | `Observation.code.coding` | 395197008.0 | Hepatitis C viral load | http://snomed.info/sct |
| 264 | 1797 | Observation | `Observation.valueCodeableConcept.coding` | 10828004.0 | Positive | http://snomed.info/sct |
| 265 | 1798 | Observation | `Observation.valueCodeableConcept.coding` | 260385009.0 | Negative | http://snomed.info/sct |
| 266 | 1831 | Observation | `Observation.code.coding` | 1920-8 | Aspartate aminotransferase [Enzymatic activity/volume] in Serum or Plasma | http://loinc.org |
| 267 | 1848 | Observation | `Observation.code.coding[x]` | 26515-7 | Platelets [#/volume] in Blood | http://loinc.org |
| 268 | 1864 | Observation | `Observation.code.coding[x]` | 86465-2 | AST to platelet ratio index in Serum and Blood by calculation | http://loinc.org |
| 269 | 1886 | Observation | `Observation.code.coding` | TK000144 | Rencana menikah 1 tahun ke depan | http://terminology.kemkes.go.id |
| 270 | 1911 | Observation | `Observation.code.coding` | 30352-9 | Hemoglobin [Mass/volume] in Capillary blood | http://loinc.org |
| 271 | 1919 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 272 | 1922 | Observation | `Observation.interpretation.coding` | 271737000.0 | Anemia | http://snomed.info/sct |
| 273 | 1936 | Observation | `Observation.code.coding` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 274 | 1937 | Observation | `Observation.valueCodeableConcept.coding` | LA15255-5 | Reactive | http://loinc.org |
| 275 | 1938 | Observation | `Observation.valueCodeableConcept.coding` | LA15256-3 | Nonreactive | http://loinc.org |
| 276 | 1957 | Observation | `Observation.code.coding` | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 277 | 1958 | Observation | `Observation.valueCodeableConcept.coding` | LA15255-5 | Reactive | http://loinc.org |
| 278 | 1959 | Observation | `Observation.valueCodeableConcept.coding` | LA15256-3 | Nonreactive | http://loinc.org |
| 279 | 1973 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | 10828004.0 | Positive | http://snomed.info/sct |
| 280 | 1974 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | 260385009.0 | Negative | http://snomed.info/sct |
| 281 | 1975 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | 82334004.0 | Indeterminate | http://snomed.info/sct |
| 282 | 1976 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | 260413007.0 | None | http://snomed.info/sct |
| 283 | 1984 | Observation | `Observation.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 284 | 1985 | Observation | `Observation.valueCodeableConcept.coding` | 10828004.0 | Positive | http://snomed.info/sct |
| 285 | 1986 | Observation | `Observation.valueCodeableConcept.coding` | 260385009.0 | Negative | http://snomed.info/sct |
| 286 | 1987 | Observation | `Observation.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 287 | 1999 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | 10828004.0 | Positive | http://snomed.info/sct |
| 288 | 2000 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | 260385009.0 | Negative | http://snomed.info/sct |
| 289 | 2001 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | 82334004.0 | Indeterminate | http://snomed.info/sct |
| 290 | 2002 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | 260413007.0 | None | http://snomed.info/sct |
| 291 | 2007 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | 302814007.0 | Early yaws skin lesion | http://snomed.info/sct |
| 292 | 2008 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | 260385009.0 | Negative | http://snomed.info/sct |
| 293 | 2009 | QuestionnaireResponse | `QuestionnaireResponse.item.item.item.answer.valueCoding` | 260413007.0 | None | http://snomed.info/sct |
| 294 | 2015 | Observation | `Observation.code.coding` | 106936-8 | Treponema pallidum IgG+IgM Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay |  |
| 295 | 2016 | Observation | `Observation.valueCodeableConcept.coding` | LA15255-5 | Reactive | http://loinc.org |
| 296 | 2017 | Observation | `Observation.valueCodeableConcept.coding` | LA15256-3 | Nonreactive | http://loinc.org |
| 297 | 2043 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000169 | Benar semua kata | http://terminology.kemkes.go.id |
| 298 | 2044 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000444 | Salah satu/Dua | http://terminology.kemkes.go.id/sp |
| 299 | 2045 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000170 | Tidak dapat mengingat/mengulang kata | http://terminology.kemkes.go.id |
| 300 | 2052 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 38369006.0 | At increased risk for cognitive impairment | http://snomed.info/sct |
| 301 | 2053 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000173 | Kemungkinan tidak ada gangguan kognitif | http://terminology.kemkes.go.id |
| 302 | 2078 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 129845004.0 | At risk for malnutrition | http://snomed.info/sct |
| 303 | 2079 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 248324001.0 | Well nourished | http://snomed.info/sct |
| 304 | 2092 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000197 | Kemungkinan depresi | http://terminology.kemkes.go.id |
| 305 | 2093 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000196 | Tidak depresi | http://terminology.kemkes.go.id |
| 306 | 2096 | Observation | `Observation.code.coding` | 48542-5 | Geriatric depression scale (GDS) panel | http://loinc.org |
| 307 | 2097 | Observation | `Observation.interpretation.coding` | TK000196 | Tidak depresi | http://terminology.kemkes.go.id |
| 308 | 2100 | Observation | `Observation.interpretation.coding` | TK000197 | Kemungkinan depresi | http://terminology.kemkes.go.id |
| 309 | 2103 | Observation | `Observation.interpretation.coding` | 35489007.0 | Depression | http://snomed.info/sct |
| 310 | 2115 | Observation | `Observation.component.code.coding` | 48512-8 | Are you basically satisfied with your life [GDS] | http://loinc.org |
| 311 | 2118 | Observation | `Observation.component.code.coding` | 48515-1 | Do you often get bored [GDS] | http://loinc.org |
| 312 | 2121 | Observation | `Observation.component.code.coding` | 48521-9 | Do you often feel helpless [GDS] | http://loinc.org |
| 313 | 2124 | Observation | `Observation.component.code.coding` | 48528-4 | Do you feel pretty worthless the way you are now [GDS] | http://loinc.org |
| 314 | 2129 | Observation | `Observation.code.coding` | 96762-0 | Barthel index panel | http://loinc.org |
| 315 | 2130 | Observation | `Observation.interpretation.coding` | OI000048 | Ketergantungan total | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 316 | 2135 | Observation | `Observation.interpretation.coding` | OI000047 | Ketergantungan berat | http://snomed.info/sct |
| 317 | 2140 | Observation | `Observation.interpretation.coding` | OI000046 | Ketergantungan sedang | http://snomed.info/sct |
| 318 | 2145 | Observation | `Observation.interpretation.coding` | OI000045 | Ketergantungan ringan | http://snomed.info/sct |
| 319 | 2150 | Observation | `Observation.interpretation.coding` | 371153006.0 | Independent | http://snomed.info/sct |
| 320 | 2160 | Observation | `Observation.component.code.coding` | 96759-6 | Bowels | http://loinc.org |
| 321 | 2161 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31627-5 | Incontinent (or needs to be given enemas) | http://loinc.org |
| 322 | 2162 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31626-7 | Occasional accident | http://loinc.org |
| 323 | 2163 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31625-9 | Continent | http://loinc.org |
| 324 | 2164 | Observation | `Observation.component.code.coding` | 96760-4 | Bladder | http://loinc.org |
| 325 | 2165 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31628-3 | Incontinent, or catheterized and unable to manage alone | http://loinc.org |
| 326 | 2166 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31626-7 | Occasional accident | http://loinc.org |
| 327 | 2167 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31625-9 | Continent | http://loinc.org |
| 328 | 2168 | Observation | `Observation.component.code.coding` | 96767-9 | Grooming | http://loinc.org |
| 329 | 2169 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31643-2 | Needs help with personal care | http://loinc.org |
| 330 | 2170 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31644-0 | Independent face/hair/teeth/shaving (implements provided) | http://loinc.org |
| 331 | 2171 | Observation | `Observation.component.code.coding` | 83183-4 | Toilet Use | http://loinc.org |
| 332 | 2172 | Observation | `Observation.component.valueCodeableConcept.coding` | LA12304-4 | Dependent | http://loinc.org |
| 333 | 2173 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31631-7 | Needs some help, but can do something alone | http://loinc.org |
| 334 | 2174 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31632-5 | Independent (on and off, dressing, wiping) | http://loinc.org |
| 335 | 2175 | Observation | `Observation.component.code.coding` | 83184-2 | Feeding | http://loinc.org |
| 336 | 2176 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24937-7 | Unable | http://loinc.org |
| 337 | 2177 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31630-9 | Needs help cutting, spreading butter, etc., or requires modified diet | http://loinc.org |
| 338 | 2178 | Observation | `Observation.component.valueCodeableConcept.coding` | LA12302-8 | Independent | http://loinc.org |
| 339 | 2179 | Observation | `Observation.component.code.coding` | 83185-9 | Transfer | http://loinc.org |
| 340 | 2180 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31633-3 | Unable, no sitting balance | http://loinc.org |
| 341 | 2181 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31634-1 | Major help (one or two people, physical), can sit | http://loinc.org |
| 342 | 2182 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31635-8 | Minor help (verbal or physical) | http://loinc.org |
| 343 | 2183 | Observation | `Observation.component.valueCodeableConcept.coding` | LA12302-8 | Independent | http://loinc.org |
| 344 | 2184 | Observation | `Observation.component.code.coding` | 83186-7 | Mobility | http://loinc.org |
| 345 | 2185 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31639-0 | Immobile or <50 yards | http://loinc.org |
| 346 | 2186 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31640-8 | Wheelchair independent, including corners, >50 yards | http://loinc.org |
| 347 | 2187 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31641-6 | Walks with help of one person (verbal or physical) >50 yards | http://loinc.org |
| 348 | 2188 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31642-4 | Independent (but may use any aid; for example, stick) >50 yards | http://loinc.org |
| 349 | 2189 | Observation | `Observation.component.code.coding` | 83182-6 | Dressing | http://loinc.org |
| 350 | 2190 | Observation | `Observation.component.valueCodeableConcept.coding` | LA12304-4 | Dependent | http://loinc.org |
| 351 | 2191 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31637-4 | Needs help but can do about half unaided | http://loinc.org |
| 352 | 2192 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31638-2 | Independent (including buttons, zips, laces, etc.) | http://loinc.org |
| 353 | 2193 | Observation | `Observation.component.code.coding` | 96758-8 | Stairs | http://loinc.org |
| 354 | 2194 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24937-7 | Unable | http://loinc.org |
| 355 | 2195 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31629-1 | Needs help (verbal, physical, carrying aid) | http://loinc.org |
| 356 | 2196 | Observation | `Observation.component.valueCodeableConcept.coding` | LA12302-8 | Independent | http://loinc.org |
| 357 | 2197 | Observation | `Observation.component.code.coding` | 83181-8 | Bathing | http://loinc.org |
| 358 | 2198 | Observation | `Observation.component.valueCodeableConcept.coding` | LA12304-4 | Dependent | http://loinc.org |
| 359 | 2199 | Observation | `Observation.component.valueCodeableConcept.coding` | LA31636-6 | Independent (or in shower) | http://loinc.org |
| 360 | 2202 | Observation | `Observation.code.coding` | 72234-8 | Mini-Cog | http://loinc.org |
| 361 | 2203 | Observation | `Observation.valueCodeableConcept.coding` | TK000167 | Benar 1 kata | http://terminology.kemkes.go.id |
| 362 | 2204 | Observation | `Observation.valueCodeableConcept.coding` | TK000168 | Benar 2 kata | http://terminology.kemkes.go.id |
| 363 | 2205 | Observation | `Observation.valueCodeableConcept.coding` | TK000169 | Benar semua kata | http://terminology.kemkes.go.id |
| 364 | 2206 | Observation | `Observation.valueCodeableConcept.coding` | TK000170 | Tidak dapat mengingat/mengulang kata | http://terminology.kemkes.go.id |
| 365 | 2217 | Observation | `Observation.code.coding` | 79150-9 | Clock drawing panel [GPCOG] | http://loinc.org |
| 366 | 2218 | Observation | `Observation.component.code.coding` | 79106-1 | Please mark in all the numbers to indicate the hours of a clock | http://loinc.org |
| 367 | 2219 | Observation | `Observation.component.code.coding` | 79107-9 | Please mark in hands to show 10 minutes past eleven o'clock (11:10) | http://loinc.org |
| 368 | 2223 | Observation | `Observation.interpretation.coding` | TK000171 | Gambar jam benar/tepat | http://terminology.kemkes.go.id |
| 369 | 2224 | Observation | `Observation.interpretation.coding` | TK000172 | Gambar jam salah/tidak tepat | http://terminology.kemkes.go.id |
| 370 | 2234 | Observation | `Observation.code.coding` | 72233-0 | Total score [Mini-Cog] | http://loinc.org |
| 371 | 2237 | Observation | `Observation.interpretation.coding` | 38369006.0 | At increased risk for cognitive impairment | http://snomed.info/sct |
| 372 | 2238 | Observation | `Observation.interpretation.coding` | TK000173 | Kemungkinan tidak ada gangguan kognitif | http://terminology.kemkes.go.id |
| 373 | 2257 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 263703002.0 | Changed | http://snomed.info/sct |
| 374 | 2258 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 260388006.0 | Unchanged | http://snomed.info/sct |
| 375 | 2259 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 260388006.0 | Unchanged | http://snomed.info/sct |
| 376 | 2260 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 261665006.0 | Unknown | http://snomed.info/sct |
| 377 | 2263 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 263703002.0 | Changed | http://snomed.info/sct |
| 378 | 2264 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 260388006.0 | Unchanged | http://snomed.info/sct |
| 379 | 2265 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 261665006.0 | Unknown | http://snomed.info/sct |
| 380 | 2268 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 263703002.0 | Changed | http://snomed.info/sct |
| 381 | 2269 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 260388006.0 | Unchanged | http://snomed.info/sct |
| 382 | 2270 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 261665006.0 | Unknown | http://snomed.info/sct |
| 383 | 2273 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 263703002.0 | Changed | http://snomed.info/sct |
| 384 | 2274 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 260388006.0 | Unchanged | http://snomed.info/sct |
| 385 | 2275 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 261665006.0 | Unknown | http://snomed.info/sct |
| 386 | 2278 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 263703002.0 | Changed | http://snomed.info/sct |
| 387 | 2279 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 260388006.0 | Unchanged | http://snomed.info/sct |
| 388 | 2280 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 261665006.0 | Unknown | http://snomed.info/sct |
| 389 | 2283 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 263703002.0 | Changed | http://snomed.info/sct |
| 390 | 2284 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 260388006.0 | Unchanged | http://snomed.info/sct |
| 391 | 2285 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 261665006.0 | Unknown | http://snomed.info/sct |
| 392 | 2288 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 263703002.0 | Changed | http://snomed.info/sct |
| 393 | 2289 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 260388006.0 | Unchanged | http://snomed.info/sct |
| 394 | 2290 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 261665006.0 | Unknown | http://snomed.info/sct |
| 395 | 2293 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 263703002.0 | Changed | http://snomed.info/sct |
| 396 | 2294 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 260388006.0 | Unchanged | http://snomed.info/sct |
| 397 | 2295 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 261665006.0 | Unknown | http://snomed.info/sct |
| 398 | 2301 | Observation | `Observation.code.coding` | 71722-3 | Total score [AD8] | http://loinc.org |
| 399 | 2303 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7. org/CodeSystem/v3-Ob servationInterpretatio n |
| 400 | 2304 | Observation | `Observation.interpretation.coding` | 698464007.0 | At risk of dementia | http://snomed.info/sct |
| 401 | 2314 | Observation | `Observation.code.coding` | 66248-6 | Balance test [PhenX] | http://loinc.org |
| 402 | 2315 | Observation | `Observation.component.code.coding` | LA18188-5 | Side by side stand | http://loinc.org |
| 403 | 2319 | Observation | `Observation.component.code.coding` | LA18189-3 | Semi tandem stand | http://loinc.org |
| 404 | 2323 | Observation | `Observation.component.code.coding` | LA18190-1 | Tandem stand | http://loinc.org |
| 405 | 2338 | Observation | `Observation.code.coding` | 714283000.0 | Short Physical Performance Battery | http://snomed.info/sct |
| 406 | 2340 | Observation | `Observation.component.code.coding` | 66258-5 | For 4-Meter Walk | http://loinc.org |
| 407 | 2346 | Observation | `Observation.component.code.coding` | 66264-3 | Safe to stand five times | http://loinc.org |
| 408 | 2360 | Observation | `Observation.interpretation.coding` | 160697000.0 | Mobilitas fair | http://snomed.info/sct |
| 409 | 2361 | Observation | `Observation.interpretation.coding` | 82971005.0 | Limited mobility | http://snomed.info/sct |
| 410 | 2375 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 64379006.0 | Decrease in appetite | http://snomed.info/sct |
| 411 | 2376 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 79890006.0 | Loss of appetite | http://snomed.info/sct |
| 412 | 2377 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 161825005.0 | Appetite normal | http://snomed.info/sct |
| 413 | 2380 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000180 | Penurunan BB > 3 kg | http://terminology.kemkes.go.id |
| 414 | 2381 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 261665006.0 | Unknown | http://snomed.info/sct |
| 415 | 2382 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000181 | Penurunan BB antara 1-3 kg | http://terminology.kemkes.go.id |
| 416 | 2383 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000181 | Tidak ada penurunan BB | http://terminology.kemkes.go.id |
| 417 | 2386 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000183 | Harus berbaring di tempat tidur atau menggunakan kursi roda | http://terminology.kemkes.go.id |
| 418 | 2387 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000184 | Bisa bangun dari tempat tidur atau kursi roda, tetapi tidak bisa keluar rumah | http://terminology.kemkes.go.id |
| 419 | 2388 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000185 | Bisa bepergian keluar rumah | http://terminology.kemkes.go.id |
| 420 | 2395 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000186 | Demensia atau depresi berat | http://terminology.kemkes.go.id |
| 421 | 2396 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000187 | Demensia atau kepikunan ringan | http://terminology.kemkes.go.id |
| 422 | 2397 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000188 | Tidak ada masalah psikologis | http://terminology.kemkes.go.id |
| 423 | 2400 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000189 | IMT <19 | http://terminology.kemkes.go.id |
| 424 | 2401 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000190 | IMT 19 -<21 | http://terminology.kemkes.go.id |
| 425 | 2402 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000191 | IMT 21 -<23 | http://terminology.kemkes.go.id |
| 426 | 2403 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000192 | IMT >= 23 | http://terminology.kemkes.go.id |
| 427 | 2409 | Observation | `Observation.code.coding` | 39156-5 | Body mass index (BMI) [Ratio] | http://loinc.org |
| 428 | 2420 | Observation | `Observation.interpretation.coding` | 43664005.0 | Normal weight | http://snomed.info/sct |
| 429 | 2421 | Observation | `Observation.interpretation.coding` | 238131007.0 | Overweight | http://snomed.info/sct |
| 430 | 2422 | Observation | `Observation.interpretation.coding` | 443371000124107.0 | Obese class I | http://snomed.info/sct |
| 431 | 2423 | Observation | `Observation.interpretation.coding` | 443381000124105.0 | Obese class II | http://snomed.info/sct |
| 432 | 2424 | Observation | `Observation.interpretation.coding` | 248342006 | Underweight | http://snomed.info/sct |
| 433 | 2427 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000193 | <31 cm | http://terminology.kemkes.go.id |
| 434 | 2428 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TK000194 | >= 31 cm | http://terminology.kemkes.go.id |
| 435 | 2434 | Observation | `Observation.code.coding` | 8283-4 | Calf - right Maximum circumference | http://loinc.org |
| 436 | 2435 | Observation | `Observation.code.coding` | 8282-6 | Calf - left Maximum circumference | http://loinc.org |
| 437 | 2451 | Observation | `Observation.code.coding` | TK000195 | Mini Nutritional Assessment (MNA) SF | http://terminology.kemkes.go.id |
| 438 | 2454 | Observation | `Observation.interpretation.coding` | 248324001.0 | Well nourished | http://snomed.info/sct |
| 439 | 2455 | Observation | `Observation.interpretation.coding` | 129845004.0 | At risk for malnutrition | http://snomed.info/sct |
| 440 | 2456 | Observation | `Observation.interpretation.coding` | 2492009.0 | Malnutrition | http://snomed.info/sct |
| 441 | 2457 | Observation | `Observation.interpretation.coding` | 860635002.0 | No anemia present | http://snomed.info/sct |
| 442 | 2468 | Observation | `Observation.code.coding` | TK000195 | Mini Nutritional Assessment (MNA) SF | http://terminology.kemkes.go.id |
| 443 | 2471 | Observation | `Observation.interpretation.coding` | 248324001.0 | Well nourished | http://snomed.info/sct |
| 444 | 2472 | Observation | `Observation.interpretation.coding` | 129845004.0 | At risk for malnutrition | http://snomed.info/sct |
| 445 | 2473 | Observation | `Observation.interpretation.coding` | 2492009.0 | Malnutrition | http://snomed.info/sct |
| 446 | 2474 | Observation | `Observation.interpretation.coding` | 860635002.0 | No anemia present | http://snomed.info/sct |
| 447 | 2517 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 723505004.0 | Low risk | http://snomed.info/sct |
| 448 | 2518 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 723509005.0 | High risk | http://snomed.info/sct |
| 449 | 2602 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 424805008.0 | Exercise above recommended level | http://snomed.info/sct |
| 450 | 2603 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 413300002.0 | Exercise below recommended level | http://snomed.info/sct |
| 451 | 2615 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP000831 | Tidak batuk | http://terminology.kemkes.go.id/sp |
| 452 | 2616 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP000832 | Ya, lebih dari 2 minggu | http://terminology.kemkes.go.id/sp |
| 453 | 2617 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP000833 | Ya, kurang dari 2 minggu | http://terminology.kemkes.go.id/sp |
| 454 | 2636 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 260413007.0 | None | http://snomed.info/sct |
| 455 | 2637 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 261665006.0 | Unknown | http://snomed.info/sct |
| 456 | 2638 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP000201 | Kontak serumah | http://terminology.kemkes.go.id/sp |
| 457 | 2641 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | tb-bac | Terkonfirmasi bakteriologis | http://terminology.kemkes.go.id/CodeSystem/tb-case-definition |
| 458 | 2642 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | tb-clin | Terdiagnosis klinis | http://terminology.kemkes.go.id/CodeSystem/tb-case-definition |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 223 |
| http://loinc.org | 127 |
| http://terminology.kemkes.go.id | 34 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 31 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 19 |
| http://terminology.kemkes.go.id/sp | 11 |
| http://terminology.kemkes.go.id/CodeSystem/examination | 4 |
|  | 3 |
| http://hl7.org/fhir/administrative-gender | 2 |
| http://terminology.kemkes.go.id/CodeSystem/tb-case-definition | 2 |
| http://hl7.org/fhir/sid/icd-10 | 1 |
| http://terminology.hl7. org/CodeSystem/v3-Ob servationInterpretatio n | 1 |
| **Total** | **458** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 42 | – | ihs_organization | Organization | `Organization.id` |
| 44 | – | organization_name | Organization | `Organization.name` |
| 45 | – | kabkota_name | Organization | `Organization.address.city` |
| 48 | – | provinsi | Organization | `Organization.address.extension.extension.url` |
| 51 | – | kabkota | Organization | `Organization.address.extension.extension.url` |
