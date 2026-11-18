# Output Form: SITB TB 06

Sumber: `mapping/phdt-data-dictionary-sitb-tb06.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 56 |
| Code (`jumlah code` = 1) | 276 |
| Code unik (code + CodeSystem) | 117 |
| Variabel BQ (unik) | 92 |
| Variabel di Excel export | 96 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–21 | Organization | – | – | `alamat_lengkap_faskes_kode_fasyankes` → `Organization.identifier` (3)<br>`alamat_lengkap_faskes_jenis_fasyankes` → `Organization.type` (4)<br>`alamat_lengkap_faskes_nama_fasyankes` → `Organization.name` (5)<br>`alamat_lengkap_faskes_kabupatenkota` → `Organization.address.city` (6)<br>`alamat_lengkap_faskes_provinsi` → `Organization.address.extension.extension.valueCode` (10)<br>`alamat_lengkap_faskes_kepemilikan_fasyankes` → `Organization.type` (20) |
| 2 | 24–47 | Location | – | – | – |
| 3 | 50–75 | Patient | – | – | `no_rekam_medis` → `Patient.identifier.value` (53)<br>`nik_nomor_identitas_kependudukan` → `Patient.identifier.value` (56)<br>`nama_lengkap_terduga_tbc` → `Patient.name.text` (57)<br>`jenis_kelamin` → `Patient.gender` (58)<br>`alamat_lengkap_terduga_tbc_provinsi` → `Patient.address.extension.extension.valueCode` (64)<br>`alamat_lengkap_terduga_tbc_kabupatenkota` → `Patient.address.extension.extension.valueCode` (67)<br>`alamat_lengkap_terduga_tbc_kecamatan` → `Patient.address.extension.extension.valueCode` (70)<br>`alamat_lengkap_terduga_tbc_kelurahan` → `Patient.address.extension.extension.valueCode` (73)<br>`alamat_lengkap_terduga_tbc_alamat_lengkap` → `Patient.address.line` (74) |
| 4 | 77–86 | EpisodeOfCare | TB-SO | Tuberkulosis Sensitif Obat | `no_register_terduga` → `EpisodeOfCare.identifier` (77)<br>_Klasifikasi Kasus Terduga TB_ → `EpisodeOfCare.type.coding` (79, tanpa BQ)<br>`tanggal_didaftar` → `EpisodeOfCare.period.start` (81) |
| 5 | 89–101 | EpisodeOfCare | TB-SO | Tuberkulosis Sensitif Obat | `hasil_diagnosis` → `EpisodeOfCare.type.coding` (90)<br>`terkonfirmasi_tbc` → `EpisodeOfCare.status` (93)<br>`tanggal_hasil_diagnosis` → `EpisodeOfCare.statusHistory.period.start` (95) |
| 6 | 104–116 | EpisodeOfCare | TB-SO | Tuberkulosis Sensitif Obat | _Terkonfirmasi TBC_ → `EpisodeOfCare.status` (108, tanpa BQ) |
| 7 | 117–150 | Encounter | – | – | `no_register_sitb` → `Encounter.identifier` (118)<br>`dirujukdikirim_oleh` → `Encounter.hospitalization.admitSource.coding` (120) |
| 8 | 152–158 | Condition | Z03.0 | Observation for suspected tuberculosis | – |
| 9 | 160–167 | Condition | A15.0 | Tuberculosis of lung, confirmed by sputum microscopy with or without culture | – |
| 10 | 170–181 | Observation | 424144002 | Current chronological age | `umur_tahun` → `Observation.valueQuantity.value` (173) |
| 11 | 184–228 | QuestionnaireResponse | – | – | `klasifikasi_berdasarkan_riwayat_pengobatan_sebelumnya` → `QuestionnaireResponse.item.item.linkId` (199)<br>`kriteria_terduga_tbc_ro` → `QuestionnaireResponse.item.item.linkId` (211)<br>`lokasi_anatomi_penyakit` → `QuestionnaireResponse.item.item.linkId` (225) |
| 12 | 231–242 | Observation | OC000191 | Jumlah Skoring TBC Anak | `total_skoring_tbc_anak` → `Observation.valueInteger` (234) |
| 13 | 245–254 | ServiceRequest | 24648-8 | XR Chest PA upright | – |
| 14 | 256–268 | Observation | 24648-8 | XR Chest PA upright | `hasil_pemeriksaan_foto_toraks` → `Observation.valueCodeableConcept.coding` (259) |
| 15 | 270–280 | DiagnosticReport | 24648-8 | XR Chest PA upright | – |
| 16 | 282–297 | Procedure | 424489006 | Mantoux test | `dilakukan_pemeriksaan_tuberkulinigra` → `Procedure.category.coding` (282) |
| 17 | 299–317 | Observation | 23539-0 | Tuberculosis reaction wheal [Diameter] --3 days post dose mammalian tuberculin intradermal | `hasil_pemeriksaan_tuberkulinigra` → `Observation.valueCodeableConcept.coding` (302) |
| 18 | 320–332 | Observation | 55277-8 | HIV status | `status_hiv` → `Observation.valueCodeableConcept.coding` (323) |
| 19 | 335–347 | Observation | 33248-6 | Diabetes status | `riwayat_diabetes_melitus` → `Observation.valueCodeableConcept.coding` (338) |
| 20 | 350–360 | ServiceRequest | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | – |
| 21 | 362–371 | Specimen | 119334006 | Sputum specimen | `no_identitas_sediaan` → `Specimen.identifier` (363) |
| 22 | 373–389 | Observation | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | `hasil_pemeriksaan_mikroskopis_hasil_pemeriksaan_1` → `Observation.valueCodeableConcept.coding` (377)<br>`hasil_pemeriksaan_mikroskopis_tanggal_pemeriksaan_1` → `Observation.issued` (387) |
| 23 | 391–403 | DiagnosticReport | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | – |
| 24 | 405–415 | ServiceRequest | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | – |
| 25 | 417–426 | Specimen | 119334006 | Sputum specimen | `no_identitas_sediaan` → `Specimen.identifier` (418) |
| 26 | 428–444 | Observation | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | `hasil_pemeriksaan_mikroskopis_hasil_pemeriksaan_2` → `Observation.valueCodeableConcept.coding` (432)<br>`hasil_pemeriksaan_mikroskopis_tanggal_pemeriksaan_2` → `Observation.issued` (442) |
| 27 | 446–458 | DiagnosticReport | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | – |
| 28 | 461–478 | ServiceRequest | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | `jenis_pemeriksaan_diagnosis` → `ServiceRequest.category.coding` (461) |
| 29 | 480–487 | Specimen | 119334006 | Sputum specimen | – |
| 30 | 489–515 | Observation | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | `hasil_pemeriksaan_diagnosis_tbc` → `Observation.valueCodeableConcept.coding` (500)<br>`tanggal_hasil_pemeriksaan_diagnosis_tbc` → `Observation.issued` (512)<br>`keterangan_diisi_tempat_pemeriksaan_selain_mikroskopis` → `Observation.note.text` (513) |
| 31 | 517–544 | DiagnosticReport | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | – |
| 32 | 547–556 | ServiceRequest | X099379 | Pemeriksaan TCM XDR | – |
| 33 | 558–565 | Specimen | 119334006 | Sputum specimen | – |
| 34 | 567–624 | Observation | X099379 | Pemeriksaan TCM XDR | `hasil_pemeriksaan_xpert_tcm_xdr_validinvaliderrorno_result` → `Observation.valueCodeableConcept.coding` (570)<br>`hasil_pemeriksaan_xpert_tcm_xdr_mtb` → `Observation.component.code.coding` (575)<br>`hasil_pemeriksaan_xpert_tcm_xdr_h_dosis_rendah_low` → `Observation.component.code.coding` (579)<br>`hasil_pemeriksaan_xpert_tcm_xdr_h` → `Observation.component.code.coding` (584)<br>`hasil_pemeriksaan_xpert_tcm_xdr_eto` → `Observation.component.code.coding` (589)<br>`hasil_pemeriksaan_xpert_tcm_xdr_fq_dosis_rendah_low` → `Observation.component.code.coding` (593)<br>`hasil_pemeriksaan_xpert_tcm_xdr_fq` → `Observation.component.code.coding` (598)<br>`hasil_pemeriksaan_xpert_tcm_xdr_amk` → `Observation.component.code.coding` (603)<br>`hasil_pemeriksaan_xpert_tcm_xdr_km` → `Observation.component.code.coding` (608)<br>`hasil_pemeriksaan_xpert_tcm_xdr_cm` → `Observation.component.code.coding` (613)<br>`tanggal_hasil_pemeriksaan_tcmxdr` → `Observation.issued` (622) |
| 35 | 626–637 | DiagnosticReport | X099379 | Pemeriksaan TCM XDR | – |
| 36 | 640–649 | ServiceRequest | X099380 | Line Probe Assay (LPA) Lini 1 | – |
| 37 | 651–658 | Specimen | 119334006 | Sputum specimen | – |
| 38 | 660–688 | Observation | X099380 | Line Probe Assay (LPA) Lini 1 | `hasil_pemeriksaan_lpa_line_probe_assay_lini_1_invalid` → `Observation.valueCodeableConcept.coding` (663)<br>`hasil_pemeriksaan_lpa_line_probe_assay_lini_1_mtb` → `Observation.component.code.coding` (666)<br>`hasil_pemeriksaan_lpa_line_probe_assay_lini_1_r` → `Observation.component.code.coding` (670)<br>`hasil_pemeriksaan_lpa_line_probe_assay_lini_1_h` → `Observation.component.code.coding` (676)<br>`tanggal_hasil_pemeriksaan_lpa_lini_1` → `Observation.effectiveDateTime` (685) |
| 39 | 690–701 | DiagnosticReport | X099380 | Line Probe Assay (LPA) Lini 1 | – |
| 40 | 704–713 | ServiceRequest | X099381 | Line Probe Assay (LPA) Lini 2 | – |
| 41 | 715–722 | Specimen | 119334006 | Sputum specimen | – |
| 42 | 724–776 | Observation | X099381 | Line Probe Assay (LPA) Lini 2 | `hasil_pemeriksaan_lpa_line_probe_assay_lini_2_invalid` → `Observation.valueCodeableConcept.coding` (727)<br>`hasil_pemeriksaan_lpa_line_probe_assay_lini_2_mtb` → `Observation.component.code.coding` (730)<br>`hasil_pemeriksaan_lpa_line_probe_assay_lini_2_lfx` → `Observation.component.code.coding` (734)<br>`hasil_pemeriksaan_lpa_line_probe_assay_lini_2_mfx` → `Observation.component.code.coding` (740)<br>`hasil_pemeriksaan_lpa_line_probe_assay_lini_2_mfx_dt` → `Observation.component.code.coding` (746)<br>`hasil_pemeriksaan_lpa_line_probe_assay_lini_2_km` → `Observation.component.code.coding` (752)<br>`hasil_pemeriksaan_lpa_line_probe_assay_lini_2_amk` → `Observation.component.code.coding` (758)<br>`hasil_pemeriksaan_lpa_line_probe_assay_lini_2_cm` → `Observation.component.code.coding` (764)<br>`tanggal_hasil_pemeriksaan_lpa_lini_2` → `Observation.effectiveDateTime` (773) |
| 43 | 778–789 | DiagnosticReport | X099381 | Line Probe Assay (LPA) Lini 2 | – |
| 44 | 792–801 | ServiceRequest | X099388 | Biakan TB | – |
| 45 | 803–810 | Specimen | 119334006 | Sputum specimen | – |
| 46 | 812–829 | Observation | X099388 | Biakan TB | `hasil_pemeriksaan_biakan` → `Observation.valueCodeableConcept.coding` (815)<br>`tanggal_hasil_pemeriksaan_biakan` → `Observation.effectiveDateTime` (826) |
| 47 | 831–842 | DiagnosticReport | X099388 | Biakan TB | – |
| 48 | 845–854 | ServiceRequest | X099383 | Pemeriksaan Paket Standar Kepekaan | – |
| 49 | 856–863 | Specimen | 119334006 | Sputum specimen | – |
| 50 | 865–932 | Observation | X099383 | Pemeriksaan Paket Standar Kepekaan | `hasil_pemeriksaan_paket_standar_uji_kepekaan_h_dosis_tinggi` → `Observation.component.code.coding` (870)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_h` → `Observation.component.code.coding` (876)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_km` → `Observation.component.code.coding` (882)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_cm` → `Observation.component.code.coding` (888)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_lfx` → `Observation.component.code.coding` (894)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_mfx_dosis_tinggi` → `Observation.component.code.coding` (900)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_mfx` → `Observation.component.code.coding` (906)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan` → `Observation.component.code.coding` (912)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_1` → `Observation.component.code.coding` (914)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_2` → `Observation.component.code.coding` (916)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_3` → `Observation.component.code.coding` (918)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_4` → `Observation.component.code.coding` (920)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_5` → `Observation.component.code.coding` (922)<br>`tanggal_hasil_pemeriksaan_uji_kepekaan` → `Observation.effectiveDateTime` (929) |
| 51 | 934–945 | DiagnosticReport | X099383 | Pemeriksaan Paket Standar Kepekaan | – |
| 52 | 948–959 | Observation | 106229004 | Qualifier for type of diagnosis | `tipe_diagnosis` → `Observation.valueCodeableConcept.coding` (951) |
| 53 | 962–988 | CarePlan | – | – | `tindak_lanjut` → `CarePlan.status` (962)<br>`tempat_pengobatan_dirujuk_ke_nama_fasyankes` → `CarePlan.activity.detail.performer.reference` (976) 🔎 lookup master data<br>`tempat_pengobatan_tidak_dirujuk` → `CarePlan.activity.detail.performer.reference` (977) 🔎 lookup master data<br>`tanggal_mulai_pengobatan_tbc_tglblnthn` → `CarePlan.activity.detail.scheduledPeriod.start` (979)<br>`tindak_lanjut_penambahan_resistansi` → `CarePlan.note.text` (987) |
| 54 | 990–1001 | Observation | 365866002 | Finding of human immunodeficiency virus status | `hasil_tes_hiv` → `Observation.valueCodeableConcept.coding` (993)<br>`tanggal_tes_hiv` → `Observation.issued` (999) |
| 55 | 1003–1013 | Procedure | SP000046 | Terapi Antiretroviral (ART) | `art` → `Procedure.category.coding` (1003) |
| 56 | 1015–1026 | Observation | SP000047 | Hasil Tes Diabetes Melitus | `hasil_tes_dm` → `Observation.valueCodeableConcept.coding` (1018) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 17 |
| ServiceRequest | 9 |
| DiagnosticReport | 9 |
| Specimen | 8 |
| EpisodeOfCare | 3 |
| Condition | 2 |
| Procedure | 2 |
| Organization | 1 |
| Location | 1 |
| Patient | 1 |
| Encounter | 1 |
| QuestionnaireResponse | 1 |
| CarePlan | 1 |
| **Total** | **56** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 79 | EpisodeOfCare | `EpisodeOfCare.type.coding` | TB-SO | Tuberkulosis Sensitif Obat | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 2 | 80 | EpisodeOfCare | `EpisodeOfCare.type.coding` | TB-RO | Tuberkulosis Resisten Obat | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 3 | 90 | EpisodeOfCare | `EpisodeOfCare.type.coding` | TB-SO | Tuberkulosis Sensitif Obat | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 4 | 91 | EpisodeOfCare | `EpisodeOfCare.type.coding` | TB-RO | Tuberkulosis Resisten Obat | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 5 | 105 | EpisodeOfCare | `EpisodeOfCare.type.coding` | TB-SO | Tuberkulosis Sensitif Obat | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 6 | 106 | EpisodeOfCare | `EpisodeOfCare.type.coding` | TB-RO | Tuberkulosis Resisten Obat | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 7 | 120 | Encounter | `Encounter.hospitalization.admitSource.coding` | EHA000001 | Kader/ Komunitas | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 8 | 121 | Encounter | `Encounter.hospitalization.admitSource.coding` | EHA000002 | Datang sendiri | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 9 | 122 | Encounter | `Encounter.hospitalization.admitSource.coding` | EHA000003 | Kegiatan ACF | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 10 | 123 | Encounter | `Encounter.hospitalization.admitSource.coding` | 257622000 | Healthcare facility | http://snomed.info/sct |
| 11 | 124 | Encounter | `Encounter.hospitalization.admitSource.coding` | EHA000004 | Skrining TBC DM | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 12 | 125 | Encounter | `Encounter.hospitalization.admitSource.coding` | EHA000005 | Pemadanan Data BPJS | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 13 | 154 | Condition | `Condition.code.coding` | Z03.0 | Observation for suspected tuberculosis | http://hl7.org/fhir/sid/icd-10 |
| 14 | 162 | Condition | `Condition.code.coding` | A15.0 | Tuberculosis of lung, confirmed by sputum microscopy with or without culture | http://hl7.org/fhir/sid/icd-10 |
| 15 | 163 | Condition | `Condition.code.coding` | A16.2 | Tuberculosis of lung, without mention of bacteriological or histological confirmation | http://hl7.org/fhir/sid/icd-10 |
| 16 | 172 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 17 | 197 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | QRI000001 | Terduga TBC SO | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 18 | 198 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | QRI000002 | Terduga TBC RO | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 19 | 201 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | new | Kasus Baru | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 20 | 202 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | relapse | Kasus Kambuh | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 21 | 203 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure-cat1 | Kasus Pengobatan Setelah Gagal Kategori 1 | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 22 | 204 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure-cat2 | Kasus Pengobatan Setelah Gagal Kategori 2 | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 23 | 205 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | loss-to-follow-up | Kasus Setelah Loss To Follow Up | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 24 | 206 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure-2line | Kasus Pengobatan Setelah Gagal lini 2 | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 25 | 207 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | not-eval | Pernah diobati tidak diketahui hasilnya | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 26 | 208 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | unknown | Kasus dengan riwayat pengobatan tidak diketahui | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 27 | 209 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | other | Kasus lain-lain | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 28 | 210 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure | Kasus Pengobatan Setelah Gagal | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 29 | 213 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure-cat2 | Kasus Pengobatan Setelah Gagal Kategori 2 | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 30 | 214 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | treatment-non-conversion-2 | Pasien TB pengobatan kategori 2 yang tidak konversi setelah 3 bulan pengobatan | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 31 | 215 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | non-standard-treatment | Pasien TB yang mempunyai riwayat pengobatan TB yang tidak standar | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 32 | 216 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure-cat1 | Kasus Pengobatan Setelah Gagal Kategori 1 | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 33 | 217 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | treatment-non-conversion-1 | Pasien TB pengobatan kategori 1 yang tidak konversi | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 34 | 218 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | relapse | Kasus Baru | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 35 | 219 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | loss-to-follow-up | Kasus Setelah Loss To Follow Up | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 36 | 220 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | history-of-close-contact with-TB-DR | Terduga TB yang mempunyai riwayat kontak erat dengan pasien TB RO | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 37 | 221 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | co-infected-TBHIV | Pasien ko-infeksi TB-HIV yang tidak respons secara klinis maupun bakteriologis terhadap pemberian OAT | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 38 | 222 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure-2line | Kasus Pengobatan Setelah Gagal lini 2 | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 39 | 223 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TB-DR-relapse | Pasien TB RO kasus kambuh | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 40 | 224 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TB-DR-returns | Pasien TB RO yang kembali setelah putus berobat | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 41 | 227 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 154283005 | Pulmonary tuberculosis | http://snomed.info/sct |
| 42 | 228 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 423997002 | Tuberculosis, extrapulmonary | http://snomed.info/sct |
| 43 | 233 | Observation | `Observation.code.coding` | OC000191 | Jumlah Skoring TBC Anak | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 44 | 249 | ServiceRequest | `ServiceRequest.code.coding` | 24648-8 | XR Chest PA upright | http://loinc.org |
| 45 | 258 | Observation | `Observation.code.coding` | 24648-8 | XR Chest PA upright | http://loinc.org |
| 46 | 259 | Observation | `Observation.valueCodeableConcept.coding` | 707307002 | Tuberculosis screening chest X-ray abnormal | http://snomed.info/sct |
| 47 | 260 | Observation | `Observation.valueCodeableConcept.coding` | 707308007 | Tuberculosis screening chest X-ray normal | http://snomed.info/sct |
| 48 | 272 | DiagnosticReport | `DiagnosticReport.code.coding` | 24648-8 | XR Chest PA upright | http://loinc.org |
| 49 | 283 | Procedure | `Procedure.code.coding` | 424489006 | Mantoux test | http://snomed.info/sct |
| 50 | 285 | Procedure | `Procedure.code.coding` | 35140007 | Interferon gamma assay | http://snomed.info/sct |
| 51 | 287 | Procedure | `Procedure.code.coding` | 424489006 | Mantoux test | http://snomed.info/sct |
| 52 | 289 | Procedure | `Procedure.code.coding` | 35140007 | Interferon gamma assay | http://snomed.info/sct |
| 53 | 301 | Observation | `Observation.code.coding` | 23539-0 | Tuberculosis reaction wheal [Diameter] --3 days post dose mammalian tuberculin intradermal | http://loinc.org |
| 54 | 302 | Observation | `Observation.valueCodeableConcept.coding` | 268376005 | Mantoux: positive | http://snomed.info/sct |
| 55 | 303 | Observation | `Observation.valueCodeableConcept.coding` | 268375009 | Mantoux: negative | http://snomed.info/sct |
| 56 | 304 | Observation | `Observation.code.coding` | 71773-6 | Mycobacterium tuberculosis stimulated gamma interferon [Interpretation] in Blood Qualitative | http://loinc.org |
| 57 | 305 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 58 | 306 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 59 | 307 | Observation | `Observation.code.coding` | 23539-0 | Tuberculosis reaction wheal [Diameter] --3 days post dose mammalian tuberculin intradermal | http://loinc.org |
| 60 | 309 | Observation | `Observation.code.coding` | 71773-6 | Mycobacterium tuberculosis stimulated gamma interferon [Interpretation] in Blood Qualitative | http://loinc.org |
| 61 | 322 | Observation | `Observation.code.coding` | 55277-8 | HIV status | http://loinc.org |
| 62 | 323 | Observation | `Observation.valueCodeableConcept.coding` | 10828004 | Positive | http://snomed.info/sct |
| 63 | 324 | Observation | `Observation.valueCodeableConcept.coding` | 260385009 | Negative | http://snomed.info/sct |
| 64 | 325 | Observation | `Observation.valueCodeableConcept.coding` | 261665006 | Unknown | http://snomed.info/sct |
| 65 | 337 | Observation | `Observation.code.coding` | 33248-6 | Diabetes status | http://loinc.org |
| 66 | 338 | Observation | `Observation.valueCodeableConcept.coding` | 10828004 | Positive | http://snomed.info/sct |
| 67 | 339 | Observation | `Observation.valueCodeableConcept.coding` | 260385009 | Negative | http://snomed.info/sct |
| 68 | 340 | Observation | `Observation.valueCodeableConcept.coding` | 261665006 | Unknown | http://snomed.info/sct |
| 69 | 355 | ServiceRequest | `ServiceRequest.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 70 | 365 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 71 | 376 | Observation | `Observation.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 72 | 377 | Observation | `Observation.valueCodeableConcept.coding` | 260385009 | Negative | http://snomed.info/sct |
| 73 | 378 | Observation | `Observation.valueCodeableConcept.coding` | LA11841-6 | 1+ | http://loinc.org |
| 74 | 379 | Observation | `Observation.valueCodeableConcept.coding` | LA11842-4 | 2+ | http://loinc.org |
| 75 | 380 | Observation | `Observation.valueCodeableConcept.coding` | LA11843-2 | 3+ | http://loinc.org |
| 76 | 394 | DiagnosticReport | `DiagnosticReport.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 77 | 410 | ServiceRequest | `ServiceRequest.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 78 | 420 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 79 | 431 | Observation | `Observation.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 80 | 432 | Observation | `Observation.valueCodeableConcept.coding` | 260385009 | Negative | http://snomed.info/sct |
| 81 | 433 | Observation | `Observation.valueCodeableConcept.coding` | LA11841-6 | 1+ | http://loinc.org |
| 82 | 434 | Observation | `Observation.valueCodeableConcept.coding` | LA11842-4 | 2+ | http://loinc.org |
| 83 | 435 | Observation | `Observation.valueCodeableConcept.coding` | LA11843-2 | 3+ | http://loinc.org |
| 84 | 449 | DiagnosticReport | `DiagnosticReport.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 85 | 465 | ServiceRequest | `ServiceRequest.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 86 | 466 | ServiceRequest | `ServiceRequest.code.coding` | 89371-9 | MTB complex DNA and rpoB RIF resistance mutation panel [Presence] | http://loinc.org |
| 87 | 467 | ServiceRequest | `ServiceRequest.code.coding` | X099379 | Pemeriksaan TCM XDR | http://terminology.kemkes.go.id/CodeSystem/examination |
| 88 | 468 | ServiceRequest | `ServiceRequest.code.coding` | X099380 | Line Probe Assay (LPA) Lini 1 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 89 | 469 | ServiceRequest | `ServiceRequest.code.coding` | X099381 | Line Probe Assay (LPA) Lini 2 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 90 | 470 | ServiceRequest | `ServiceRequest.code.coding` | X099388 | Biakan TB | http://terminology.kemkes.go.id/CodeSystem/examination |
| 91 | 471 | ServiceRequest | `ServiceRequest.code.coding` | X099383 | Pemeriksaan Paket Standar Kepekaan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 92 | 472 | ServiceRequest | `ServiceRequest.code.coding` | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 93 | 473 | ServiceRequest | `ServiceRequest.code.coding` | MK099927 | Pemeriksaan PCR Open System | http://terminology.kemkes.go.id/CodeSystem/examination |
| 94 | 481 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 95 | 491 | Observation | `Observation.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 96 | 492 | Observation | `Observation.code.coding` | 89371-9 | MTB complex DNA and rpoB RIF resistance mutation panel [Presence] | http://loinc.org |
| 97 | 493 | Observation | `Observation.code.coding` | X099379 | Pemeriksaan TCM XDR | http://terminology.kemkes.go.id/CodeSystem/examination |
| 98 | 494 | Observation | `Observation.code.coding` | X099380 | Line Probe Assay (LPA) Lini 1 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 99 | 495 | Observation | `Observation.code.coding` | X099381 | Line Probe Assay (LPA) Lini 2 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 100 | 496 | Observation | `Observation.code.coding` | X099388 | Biakan TB | http://terminology.kemkes.go.id/CodeSystem/examination |
| 101 | 497 | Observation | `Observation.code.coding` | X099383 | Pemeriksaan Paket Standar Kepekaan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 102 | 498 | Observation | `Observation.code.coding` | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 103 | 499 | Observation | `Observation.code.coding` | MK099927 | Pemeriksaan PCR Open System | http://terminology.kemkes.go.id/CodeSystem/examination |
| 104 | 500 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 105 | 501 | Observation | `Observation.valueCodeableConcept.coding` | X099770 | Rifampisin sensitive | http://terminology.kemkes.go.id/CodeSystem/examination |
| 106 | 502 | Observation | `Observation.valueCodeableConcept.coding` | X099771 | Rifampisin resistan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 107 | 503 | Observation | `Observation.valueCodeableConcept.coding` | X099772 | Rifampisin indeterminate | http://terminology.kemkes.go.id/CodeSystem/examination |
| 108 | 519 | DiagnosticReport | `DiagnosticReport.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 109 | 521 | DiagnosticReport | `DiagnosticReport.code.coding` | 89371-9 | MTB complex DNA and rpoB RIF resistance mutation panel [Presence] | http://loinc.org |
| 110 | 523 | DiagnosticReport | `DiagnosticReport.code.coding` | X099379 | Pemeriksaan TCM XDR | http://terminology.kemkes.go.id/CodeSystem/examination |
| 111 | 525 | DiagnosticReport | `DiagnosticReport.code.coding` | X099380 | Line Probe Assay (LPA) Lini 1 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 112 | 527 | DiagnosticReport | `DiagnosticReport.code.coding` | X099381 | Line Probe Assay (LPA) Lini 2 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 113 | 529 | DiagnosticReport | `DiagnosticReport.code.coding` | X099388 | Biakan TB | http://terminology.kemkes.go.id/CodeSystem/examination |
| 114 | 531 | DiagnosticReport | `DiagnosticReport.code.coding` | X099383 | Pemeriksaan Paket Standar Kepekaan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 115 | 533 | DiagnosticReport | `DiagnosticReport.code.coding` | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 116 | 535 | DiagnosticReport | `DiagnosticReport.code.coding` | MK099927 | Pemeriksaan PCR Open System | http://terminology.kemkes.go.id/CodeSystem/examination |
| 117 | 551 | ServiceRequest | `ServiceRequest.code.coding` | X099379 | Pemeriksaan TCM XDR | http://terminology.kemkes.go.id/CodeSystem/examination |
| 118 | 559 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 119 | 569 | Observation | `Observation.code.coding` | X099379 | Pemeriksaan TCM XDR | http://terminology.kemkes.go.id/CodeSystem/examination |
| 120 | 570 | Observation | `Observation.valueCodeableConcept.coding` | X099781 | Hasil Valid | http://terminology.kemkes.go.id/CodeSystem/examination |
| 121 | 575 | Observation | `Observation.component.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 122 | 576 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 123 | 577 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 124 | 579 | Observation | `Observation.component.code.coding` | X099391 | H Dosis Rendah (Low) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 125 | 580 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 126 | 581 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 127 | 582 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 128 | 584 | Observation | `Observation.component.code.coding` | 89488-1 | Isoniazid [Susceptibility] by Genotype method | http://loinc.org |
| 129 | 585 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 130 | 586 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 131 | 587 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 132 | 589 | Observation | `Observation.component.code.coding` | 96110-2 | Ethionamide [Susceptibility] by Genotype method | http://loinc.org |
| 133 | 590 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 134 | 591 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 135 | 593 | Observation | `Observation.component.code.coding` | X099392 | FQ Dosis Rendah (Low) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 136 | 594 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 137 | 595 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 138 | 596 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 139 | 598 | Observation | `Observation.component.code.coding` | 89487-3 | Fluoroquinolone [Susceptibility] by Genotype method | http://loinc.org |
| 140 | 599 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 141 | 600 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 142 | 601 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 143 | 603 | Observation | `Observation.component.code.coding` | 89484-0 | Amikacin [Susceptibility] by Genotype method | http://loinc.org |
| 144 | 604 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 145 | 605 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 146 | 606 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 147 | 608 | Observation | `Observation.component.code.coding` | 89482-4 | Kanamycin [Susceptibility] by Genotype method | http://loinc.org |
| 148 | 609 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 149 | 610 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 150 | 611 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 151 | 613 | Observation | `Observation.component.code.coding` | 89483-2 | Capreomycin [Susceptibility] by Genotype method | http://loinc.org |
| 152 | 614 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 153 | 615 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 154 | 616 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 155 | 628 | DiagnosticReport | `DiagnosticReport.code.coding` | X099379 | Pemeriksaan TCM XDR | http://terminology.kemkes.go.id/CodeSystem/examination |
| 156 | 644 | ServiceRequest | `ServiceRequest.code.coding` | X099380 | Line Probe Assay (LPA) Lini 1 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 157 | 652 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 158 | 662 | Observation | `Observation.code.coding` | X099380 | Line Probe Assay (LPA) Lini 1 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 159 | 663 | Observation | `Observation.valueCodeableConcept.coding` | X099781 | Hasil Valid | http://terminology.kemkes.go.id/CodeSystem/examination |
| 160 | 666 | Observation | `Observation.component.code.coding` | 13956-8 | Mycobacterium tuberculosis DNA [Presence] in Specimen by NAA with probe detection | http://loinc.org |
| 161 | 667 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 162 | 668 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 163 | 670 | Observation | `Observation.component.code.coding` | 89489-9 | rifAMPin [Susceptibility] by Genotype method | http://loinc.org |
| 164 | 671 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 165 | 672 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 166 | 673 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 167 | 674 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 168 | 676 | Observation | `Observation.component.code.coding` | 89488-1 | Isoniazid [Susceptibility] by Genotype method | http://loinc.org |
| 169 | 677 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 170 | 678 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 171 | 679 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 172 | 680 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 173 | 692 | DiagnosticReport | `DiagnosticReport.code.coding` | X099380 | Line Probe Assay (LPA) Lini 1 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 174 | 708 | ServiceRequest | `ServiceRequest.code.coding` | X099381 | Line Probe Assay (LPA) Lini 2 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 175 | 716 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 176 | 726 | Observation | `Observation.code.coding` | X099381 | Line Probe Assay (LPA) Lini 2 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 177 | 727 | Observation | `Observation.valueCodeableConcept.coding` | X099781 | Hasil Valid | http://terminology.kemkes.go.id/CodeSystem/examination |
| 178 | 730 | Observation | `Observation.component.code.coding` | 13956-8 | Mycobacterium tuberculosis DNA [Presence] in Specimen by NAA with probe detection | http://loinc.org |
| 179 | 731 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 180 | 732 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 181 | 734 | Observation | `Observation.component.code.coding` | 20629-2 | levoFLOXacin [Susceptibility] | http://loinc.org |
| 182 | 735 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 183 | 736 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 184 | 737 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 185 | 738 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 186 | 740 | Observation | `Observation.component.code.coding` | 96112-8 | Moxifloxacin [Susceptibility] by Genotype method | http://loinc.org |
| 187 | 741 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 188 | 742 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 189 | 743 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 190 | 744 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 191 | 746 | Observation | `Observation.component.code.coding` | X099775 | Moxifloxacin DT (Mfx DT) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 192 | 747 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 193 | 748 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 194 | 749 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 195 | 750 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 196 | 752 | Observation | `Observation.component.code.coding` | 89482-4 | Kanamycin [Susceptibility] by Genotype method | http://loinc.org |
| 197 | 753 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 198 | 754 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 199 | 755 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 200 | 756 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 201 | 758 | Observation | `Observation.component.code.coding` | 89484-0 | Amikacin [Susceptibility] by Genotype method | http://loinc.org |
| 202 | 759 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 203 | 760 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 204 | 761 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 205 | 762 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 206 | 764 | Observation | `Observation.component.code.coding` | 89483-2 | Capreomycin [Susceptibility] by Genotype method | http://loinc.org |
| 207 | 765 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 208 | 766 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 209 | 767 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 210 | 768 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 211 | 780 | DiagnosticReport | `DiagnosticReport.code.coding` | X099381 | Line Probe Assay (LPA) Lini 2 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 212 | 796 | ServiceRequest | `ServiceRequest.code.coding` | X099388 | Biakan TB | http://terminology.kemkes.go.id/CodeSystem/examination |
| 213 | 804 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 214 | 814 | Observation | `Observation.code.coding` | X099388 | Biakan TB | http://terminology.kemkes.go.id/CodeSystem/examination |
| 215 | 815 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 216 | 816 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 217 | 817 | Observation | `Observation.valueCodeableConcept.coding` | LA11841-6 | + | http://loinc.org |
| 218 | 818 | Observation | `Observation.valueCodeableConcept.coding` | LA11842-4 | ++ | http://loinc.org |
| 219 | 819 | Observation | `Observation.valueCodeableConcept.coding` | LA11843-2 | +++ | http://loinc.org |
| 220 | 820 | Observation | `Observation.valueCodeableConcept.coding` | 110379001 | Mycobacterium, non-tuberculosis (organism) | http://snomed.info/sct |
| 221 | 833 | DiagnosticReport | `DiagnosticReport.code.coding` | X099388 | Biakan TB | http://terminology.kemkes.go.id/CodeSystem/examination |
| 222 | 849 | ServiceRequest | `ServiceRequest.code.coding` | X099383 | Pemeriksaan Paket Standar Kepekaan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 223 | 857 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 224 | 867 | Observation | `Observation.code.coding` | X099383 | Pemeriksaan Paket Standar Kepekaan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 225 | 870 | Observation | `Observation.component.code.coding` | X099776 | H High Dosage [Susceptibility] by Method for Slow-growing mycobacteria | http://terminology.kemkes.go.id/CodeSystem/examination |
| 226 | 871 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 227 | 872 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 228 | 873 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 229 | 876 | Observation | `Observation.component.code.coding` | 20383-6 | Isoniazid [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 230 | 877 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 231 | 878 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 232 | 879 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 233 | 882 | Observation | `Observation.component.code.coding` | 23609-1 | Kanamycin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 234 | 883 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 235 | 884 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 236 | 885 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 237 | 888 | Observation | `Observation.component.code.coding` | 23607-5 | Capreomycin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 238 | 889 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 239 | 890 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 240 | 891 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 241 | 894 | Observation | `Observation.component.code.coding` | 53716-7 | levoFLOXacin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 242 | 895 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 243 | 896 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 244 | 897 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 245 | 900 | Observation | `Observation.component.code.coding` | X099778 | Moxifloxacin High Dosage [Susceptibility] by Method for Slow-growing mycobacteria | http://terminology.kemkes.go.id/CodeSystem/examination |
| 246 | 901 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 247 | 902 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 248 | 903 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 249 | 906 | Observation | `Observation.component.code.coding` | 41502-6 | Moxifloxacin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 250 | 907 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 251 | 908 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 252 | 909 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 253 | 912 | Observation | `Observation.component.code.coding` | SP000472 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya | http://terminology.kemkes.go.id/sp |
| 254 | 914 | Observation | `Observation.component.code.coding` | SP000473 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 1 | http://terminology.kemkes.go.id/sp |
| 255 | 916 | Observation | `Observation.component.code.coding` | SP000474 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 2 | http://terminology.kemkes.go.id/sp |
| 256 | 918 | Observation | `Observation.component.code.coding` | SP000475 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 3 | http://terminology.kemkes.go.id/sp |
| 257 | 920 | Observation | `Observation.component.code.coding` | SP000476 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 4 | http://terminology.kemkes.go.id/sp |
| 258 | 922 | Observation | `Observation.component.code.coding` | SP000477 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 5 | http://terminology.kemkes.go.id/sp |
| 259 | 936 | DiagnosticReport | `DiagnosticReport.code.coding` | X099383 | Pemeriksaan Paket Standar Kepekaan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 260 | 950 | Observation | `Observation.code.coding` | 106229004 | Qualifier for type of diagnosis | http://snomed.info/sct |
| 261 | 951 | Observation | `Observation.valueCodeableConcept.coding` | tb-bac | Terkonfirmasi bakteriologis | http://terminology.kemkes.go.id/CodeSystem/tb-case-definition |
| 262 | 952 | Observation | `Observation.valueCodeableConcept.coding` | tb-clin | Terdiagnosis klinis | http://terminology.kemkes.go.id/CodeSystem/tb-case-definition |
| 263 | 966 | CarePlan | `CarePlan.activity.detail.code.coding` | TK000022 | Akan diobati/dirujuk | http://terminology.kemkes.go.id |
| 264 | 967 | CarePlan | `CarePlan.activity.detail.code.coding` | 699618001 | Administration of prophylactic antituberculosis agent | http://snomed.info/sct |
| 265 | 968 | CarePlan | `CarePlan.activity.detail.code.coding` | 266714009 | Previous treatment continue | http://snomed.info/sct |
| 266 | 969 | CarePlan | `CarePlan.activity.detail.code.coding` | SP001136 | Belum Mulai Pengobatan | http://terminology.kemkes.go.id/sp |
| 267 | 972 | CarePlan | `CarePlan.activity.detail.statusReason.coding` | 406149000 | Medication declined | http://snomed.info/sct |
| 268 | 973 | CarePlan | `CarePlan.activity.detail.statusReason.coding` | 419099009 | Dead | http://snomed.info/sct |
| 269 | 974 | CarePlan | `CarePlan.activity.detail.statusReason.coding` | 399307001 | Lost to follow-up | http://snomed.info/sct |
| 270 | 992 | Observation | `Observation.code.coding` | 365866002 | Finding of human immunodeficiency virus status | http://snomed.info/sct |
| 271 | 993 | Observation | `Observation.valueCodeableConcept.coding` | 165816005 | Human immunodeficiency virus detected | http://snomed.info/sct |
| 272 | 994 | Observation | `Observation.valueCodeableConcept.coding` | 165815009 | Human immunodeficiency virus not detected | http://snomed.info/sct |
| 273 | 1004 | Procedure | `Procedure.code.coding` | SP000046 | Terapi Antiretroviral (ART) | http://terminology.kemkes.go.id/sp |
| 274 | 1017 | Observation | `Observation.code.coding` | SP000047 | Hasil Tes Diabetes Melitus | http://terminology.kemkes.go.id/sp |
| 275 | 1018 | Observation | `Observation.valueCodeableConcept.coding` | 10828004 | Positive | http://snomed.info/sct |
| 276 | 1019 | Observation | `Observation.valueCodeableConcept.coding` | 260385009 | Negative | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://loinc.org | 130 |
| http://terminology.kemkes.go.id/CodeSystem/examination | 55 |
| http://snomed.info/sct | 40 |
| http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment | 22 |
| http://terminology.kemkes.go.id/sp | 9 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 8 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 6 |
| http://hl7.org/fhir/sid/icd-10 | 3 |
| http://terminology.kemkes.go.id/CodeSystem/tb-case-definition | 2 |
| http://terminology.kemkes.go.id | 1 |
| **Total** | **276** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
