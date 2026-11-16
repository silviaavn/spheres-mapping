# Output Form: SITB TB 06

Sumber: `mapping/phdt-data-dictionary-sitb-tb06.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 55 |
| Code (`jumlah code` = 1) | 275 |
| Code unik (code + CodeSystem) | 116 |
| Variabel BQ (unik) | 94 |
| Variabel di Excel export | 97 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–27 | Patient | – | – | `no_rekam_medis` → `Patient.identifier.value` (5)<br>`nik_nomor_identitas_kependudukan` → `Patient.identifier.value` (8)<br>`nama_lengkap_terduga_tbc` → `Patient.name.text` (9)<br>`jenis_kelamin` → `Patient.gender` (10)<br>`alamat_lengkap_terduga_tbc_provinsi` → `Patient.address.extension.extension.valueCode` (16)<br>`alamat_lengkap_terduga_tbc_kabupatenkota` → `Patient.address.extension.extension.valueCode` (19)<br>`alamat_lengkap_terduga_tbc_kecamatan` → `Patient.address.extension.extension.valueCode` (22)<br>`alamat_lengkap_terduga_tbc_kelurahan` → `Patient.address.extension.extension.valueCode` (25)<br>`alamat_lengkap_terduga_tbc_alamat_lengkap` → `Patient.address.line` (26) |
| 2 | 29–33 | Coverage | – | – | `no_bpjs` → `Coverage.identifier.value` (33) |
| 3 | 35–44 | EpisodeOfCare | TB-SO | Tuberkulosis Sensitif Obat | `no_register_terduga` → `EpisodeOfCare.identifier` (35)<br>`klasifikasi_terduga_tbc` → `EpisodeOfCare.type.coding` (37)<br>`tanggal_didaftar` → `EpisodeOfCare.period.start` (39) |
| 4 | 47–59 | EpisodeOfCare | TB-SO | Tuberkulosis Sensitif Obat | `hasil_diagnosis` → `EpisodeOfCare.type.coding` (48)<br>`terkonfirmasi_tbc` → `EpisodeOfCare.status` (51)<br>`tanggal_hasil_diagnosis` → `EpisodeOfCare.statusHistory.period.start` (53) |
| 5 | 62–74 | EpisodeOfCare | TB-SO | Tuberkulosis Sensitif Obat | _Terkonfirmasi TBC_ → `EpisodeOfCare.status` (66, tanpa BQ) |
| 6 | 75–114 | Encounter | – | – | `no_register_sitb` → `Encounter.identifier` (76)<br>`dirujukdikirim_oleh` → `Encounter.hospitalization.admitSource.coding` (78)<br>`alamat_lengkap_faskes_kode_fasyankes` → `Encounter.serviceProvider.reference` (109) 🔎 lookup master data<br>`alamat_lengkap_faskes_nama_fasyankes` → `Encounter.serviceProvider.reference` (110) 🔎 lookup master data<br>`alamat_lengkap_faskes_jenis_fasyankes` → `Encounter.serviceProvider.reference` (111) 🔎 lookup master data<br>`alamat_lengkap_faskes_kepemilikan_fasyankes` → `Encounter.serviceProvider.reference` (112) 🔎 lookup master data<br>`alamat_lengkap_faskes_provinsi` → `Encounter.serviceProvider.reference` (113) 🔎 lookup master data<br>`alamat_lengkap_faskes_kabupatenkota` → `Encounter.serviceProvider.reference` (114) 🔎 lookup master data |
| 7 | 116–122 | Condition | Z03.0 | Observation for suspected tuberculosis | – |
| 8 | 124–131 | Condition | A15.0 | Tuberculosis of lung, confirmed by sputum microscopy with or without culture | – |
| 9 | 134–145 | Observation | 424144002 | Current chronological age | `umur_tahun` → `Observation.valueQuantity.value` (137) |
| 10 | 148–192 | QuestionnaireResponse | – | – | `klasifikasi_berdasarkan_riwayat_pengobatan_sebelumnya` → `QuestionnaireResponse.item.item.linkId` (163)<br>`kriteria_terduga_tbc_ro` → `QuestionnaireResponse.item.item.linkId` (175)<br>`lokasi_anatomi_penyakit` → `QuestionnaireResponse.item.item.linkId` (189) |
| 11 | 195–206 | Observation | OC000191 | Jumlah Skoring TBC Anak | `total_skoring_tbc_anak` → `Observation.valueInteger` (198) |
| 12 | 209–218 | ServiceRequest | 24648-8 | XR Chest PA upright | – |
| 13 | 220–232 | Observation | 24648-8 | XR Chest PA upright | `hasil_pemeriksaan_foto_toraks` → `Observation.valueCodeableConcept.coding` (223) |
| 14 | 234–244 | DiagnosticReport | 24648-8 | XR Chest PA upright | – |
| 15 | 246–261 | Procedure | 424489006 | Mantoux test | `dilakukan_pemeriksaan_tuberkulinigra` → `Procedure.category.coding` (246) |
| 16 | 263–281 | Observation | 23539-0 | Tuberculosis reaction wheal [Diameter] --3 days post dose mammalian tuberculin intradermal | `hasil_pemeriksaan_tuberkulinigra` → `Observation.valueCodeableConcept.coding` (266) |
| 17 | 284–296 | Observation | 55277-8 | HIV status | `status_hiv` → `Observation.valueCodeableConcept.coding` (287) |
| 18 | 299–311 | Observation | 33248-6 | Diabetes status | `riwayat_diabetes_melitus` → `Observation.valueCodeableConcept.coding` (302) |
| 19 | 314–324 | ServiceRequest | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | – |
| 20 | 326–335 | Specimen | 119334006 | Sputum specimen | `no_identitas_sediaan` → `Specimen.identifier` (327) |
| 21 | 337–353 | Observation | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | `hasil_pemeriksaan_mikroskopis_hasil_pemeriksaan_1` → `Observation.valueCodeableConcept.coding` (341)<br>`hasil_pemeriksaan_mikroskopis_tanggal_pemeriksaan_1` → `Observation.issued` (351) |
| 22 | 355–367 | DiagnosticReport | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | – |
| 23 | 369–379 | ServiceRequest | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | – |
| 24 | 381–390 | Specimen | 119334006 | Sputum specimen | `no_identitas_sediaan` → `Specimen.identifier` (382) |
| 25 | 392–408 | Observation | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | `hasil_pemeriksaan_mikroskopis_hasil_pemeriksaan_2` → `Observation.valueCodeableConcept.coding` (396)<br>`hasil_pemeriksaan_mikroskopis_tanggal_pemeriksaan_2` → `Observation.issued` (406) |
| 26 | 410–422 | DiagnosticReport | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | – |
| 27 | 425–442 | ServiceRequest | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | `jenis_pemeriksaan_diagnosis` → `ServiceRequest.category.coding` (425) |
| 28 | 444–451 | Specimen | 119334006 | Sputum specimen | – |
| 29 | 453–479 | Observation | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | `hasil_pemeriksaan_diagnosis_tbc` → `Observation.valueCodeableConcept.coding` (464)<br>`tanggal_hasil_pemeriksaan_diagnosis_tbc` → `Observation.issued` (476)<br>`keterangan_diisi_tempat_pemeriksaan_selain_mikroskopis` → `Observation.note.text` (477) |
| 30 | 481–508 | DiagnosticReport | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | – |
| 31 | 511–520 | ServiceRequest | X099379 | Pemeriksaan TCM XDR | – |
| 32 | 522–529 | Specimen | 119334006 | Sputum specimen | – |
| 33 | 531–588 | Observation | X099379 | Pemeriksaan TCM XDR | `hasil_pemeriksaan_xpert_tcm_xdr_validinvaliderrorno_result` → `Observation.valueCodeableConcept.coding` (534)<br>`hasil_pemeriksaan_xpert_tcm_xdr_mtb` → `Observation.component.code.coding` (539)<br>`hasil_pemeriksaan_xpert_tcm_xdr_h_dosis_rendah_low` → `Observation.component.code.coding` (543)<br>`hasil_pemeriksaan_xpert_tcm_xdr_h` → `Observation.component.code.coding` (548)<br>`hasil_pemeriksaan_xpert_tcm_xdr_eto` → `Observation.component.code.coding` (553)<br>`hasil_pemeriksaan_xpert_tcm_xdr_fq_dosis_rendah_low` → `Observation.component.code.coding` (557)<br>`hasil_pemeriksaan_xpert_tcm_xdr_fq` → `Observation.component.code.coding` (562)<br>`hasil_pemeriksaan_xpert_tcm_xdr_amk` → `Observation.component.code.coding` (567)<br>`hasil_pemeriksaan_xpert_tcm_xdr_km` → `Observation.component.code.coding` (572)<br>`hasil_pemeriksaan_xpert_tcm_xdr_cm` → `Observation.component.code.coding` (577)<br>`tanggal_hasil_pemeriksaan_tcmxdr` → `Observation.issued` (586) |
| 34 | 590–601 | DiagnosticReport | X099379 | Pemeriksaan TCM XDR | – |
| 35 | 604–613 | ServiceRequest | X099380 | Line Probe Assay (LPA) Lini 1 | – |
| 36 | 615–622 | Specimen | 119334006 | Sputum specimen | – |
| 37 | 624–652 | Observation | X099380 | Line Probe Assay (LPA) Lini 1 | `hasil_pemeriksaan_lpa_line_probe_assay_lini_1_invalid` → `Observation.valueCodeableConcept.coding` (627)<br>`hasil_pemeriksaan_lpa_line_probe_assay_lini_1_mtb` → `Observation.component.code.coding` (630)<br>`hasil_pemeriksaan_lpa_line_probe_assay_lini_1_r` → `Observation.component.code.coding` (634)<br>`hasil_pemeriksaan_lpa_line_probe_assay_lini_1_h` → `Observation.component.code.coding` (640)<br>`tanggal_hasil_pemeriksaan_lpa_lini_1` → `Observation.effectiveDateTime` (649) |
| 38 | 654–665 | DiagnosticReport | X099380 | Line Probe Assay (LPA) Lini 1 | – |
| 39 | 668–677 | ServiceRequest | X099381 | Line Probe Assay (LPA) Lini 2 | – |
| 40 | 679–686 | Specimen | 119334006 | Sputum specimen | – |
| 41 | 688–740 | Observation | X099381 | Line Probe Assay (LPA) Lini 2 | `hasil_pemeriksaan_lpa_line_probe_assay_lini_2_invalid` → `Observation.valueCodeableConcept.coding` (691)<br>`hasil_pemeriksaan_lpa_line_probe_assay_lini_2_mtb` → `Observation.component.code.coding` (694)<br>`hasil_pemeriksaan_lpa_line_probe_assay_lini_2_lfx` → `Observation.component.code.coding` (698)<br>`hasil_pemeriksaan_lpa_line_probe_assay_lini_2_mfx` → `Observation.component.code.coding` (704)<br>`hasil_pemeriksaan_lpa_line_probe_assay_lini_2_mfx_dt` → `Observation.component.code.coding` (710)<br>`hasil_pemeriksaan_lpa_line_probe_assay_lini_2_km` → `Observation.component.code.coding` (716)<br>`hasil_pemeriksaan_lpa_line_probe_assay_lini_2_amk` → `Observation.component.code.coding` (722)<br>`hasil_pemeriksaan_lpa_line_probe_assay_lini_2_cm` → `Observation.component.code.coding` (728)<br>`tanggal_hasil_pemeriksaan_lpa_lini_2` → `Observation.effectiveDateTime` (737) |
| 42 | 742–753 | DiagnosticReport | X099381 | Line Probe Assay (LPA) Lini 2 | – |
| 43 | 756–765 | ServiceRequest | X099388 | Biakan TB | – |
| 44 | 767–774 | Specimen | 119334006 | Sputum specimen | – |
| 45 | 776–793 | Observation | X099388 | Biakan TB | `hasil_pemeriksaan_biakan` → `Observation.valueCodeableConcept.coding` (779)<br>`tanggal_hasil_pemeriksaan_biakan` → `Observation.effectiveDateTime` (790) |
| 46 | 795–806 | DiagnosticReport | X099388 | Biakan TB | – |
| 47 | 809–818 | ServiceRequest | X099383 | Pemeriksaan Paket Standar Kepekaan | – |
| 48 | 820–827 | Specimen | 119334006 | Sputum specimen | – |
| 49 | 829–896 | Observation | X099383 | Pemeriksaan Paket Standar Kepekaan | `hasil_pemeriksaan_paket_standar_uji_kepekaan_h_dosis_tinggi` → `Observation.component.code.coding` (834)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_h` → `Observation.component.code.coding` (840)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_km` → `Observation.component.code.coding` (846)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_cm` → `Observation.component.code.coding` (852)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_lfx` → `Observation.component.code.coding` (858)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_mfx_dosis_tinggi` → `Observation.component.code.coding` (864)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_mfx` → `Observation.component.code.coding` (870)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan` → `Observation.component.code.coding` (876)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_1` → `Observation.component.code.coding` (878)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_2` → `Observation.component.code.coding` (880)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_3` → `Observation.component.code.coding` (882)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_4` → `Observation.component.code.coding` (884)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_5` → `Observation.component.code.coding` (886)<br>`tanggal_hasil_pemeriksaan_uji_kepekaan` → `Observation.effectiveDateTime` (893) |
| 50 | 898–909 | DiagnosticReport | X099383 | Pemeriksaan Paket Standar Kepekaan | – |
| 51 | 912–923 | Observation | 106229004 | Qualifier for type of diagnosis | `tipe_diagnosis` → `Observation.valueCodeableConcept.coding` (915) |
| 52 | 926–951 | CarePlan | – | – | `tindak_lanjut` → `CarePlan.status` (926)<br>`tempat_pengobatan_dirujuk_ke_nama_fasyankes` → `CarePlan.activity.detail.performer.reference` (939) 🔎 lookup master data<br>`tempat_pengobatan_tidak_dirujuk` → `CarePlan.activity.detail.performer.reference` (940) 🔎 lookup master data<br>`tanggal_mulai_pengobatan_tbc_tglblnthn` → `CarePlan.activity.detail.scheduledPeriod.start` (942)<br>`tindak_lanjut_penambahan_resistansi` → `CarePlan.note.text` (950) |
| 53 | 953–964 | Observation | 365866002 | Finding of human immunodeficiency virus status | `hasil_tes_hiv` → `Observation.valueCodeableConcept.coding` (956)<br>`tanggal_tes_hiv` → `Observation.issued` (962) |
| 54 | 966–976 | Procedure | SP000046 | Terapi Antiretroviral (ART) | `art` → `Procedure.category.coding` (966) |
| 55 | 978–989 | Observation | SP000047 | Hasil Tes Diabetes Melitus | `hasil_tes_dm` → `Observation.valueCodeableConcept.coding` (981) |

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
| Patient | 1 |
| Coverage | 1 |
| Encounter | 1 |
| QuestionnaireResponse | 1 |
| CarePlan | 1 |
| **Total** | **55** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 37 | EpisodeOfCare | `EpisodeOfCare.type.coding` | TB-SO | Tuberkulosis Sensitif Obat | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 2 | 38 | EpisodeOfCare | `EpisodeOfCare.type.coding` | TB-RO | Tuberkulosis Resisten Obat | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 3 | 48 | EpisodeOfCare | `EpisodeOfCare.type.coding` | TB-SO | Tuberkulosis Sensitif Obat | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 4 | 49 | EpisodeOfCare | `EpisodeOfCare.type.coding` | TB-RO | Tuberkulosis Resisten Obat | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 5 | 63 | EpisodeOfCare | `EpisodeOfCare.type.coding` | TB-SO | Tuberkulosis Sensitif Obat | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 6 | 64 | EpisodeOfCare | `EpisodeOfCare.type.coding` | TB-RO | Tuberkulosis Resisten Obat | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 7 | 78 | Encounter | `Encounter.hospitalization.admitSource.coding` | EHA000001 | Kader/ Komunitas | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 8 | 79 | Encounter | `Encounter.hospitalization.admitSource.coding` | EHA000002 | Datang sendiri | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 9 | 80 | Encounter | `Encounter.hospitalization.admitSource.coding` | EHA000003 | Kegiatan ACF | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 10 | 81 | Encounter | `Encounter.hospitalization.admitSource.coding` | 257622000 | Healthcare facility | http://snomed.info/sct |
| 11 | 82 | Encounter | `Encounter.hospitalization.admitSource.coding` | EHA000004 | Skrining TBC DM | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 12 | 83 | Encounter | `Encounter.hospitalization.admitSource.coding` | EHA000005 | Pemadanan Data BPJS | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 13 | 118 | Condition | `Condition.code.coding` | Z03.0 | Observation for suspected tuberculosis | http://hl7.org/fhir/sid/icd-10 |
| 14 | 126 | Condition | `Condition.code.coding` | A15.0 | Tuberculosis of lung, confirmed by sputum microscopy with or without culture | http://hl7.org/fhir/sid/icd-10 |
| 15 | 127 | Condition | `Condition.code.coding` | A16.2 | Tuberculosis of lung, without mention of bacteriological or histological confirmation | http://hl7.org/fhir/sid/icd-10 |
| 16 | 136 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 17 | 161 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | QRI000001 | Terduga TBC SO | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 18 | 162 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | QRI000002 | Terduga TBC RO | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 19 | 165 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | new | Kasus Baru | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 20 | 166 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | relapse | Kasus Kambuh | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 21 | 167 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure-cat1 | Kasus Pengobatan Setelah Gagal Kategori 1 | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 22 | 168 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure-cat2 | Kasus Pengobatan Setelah Gagal Kategori 2 | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 23 | 169 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | loss-to-follow-up | Kasus Setelah Loss To Follow Up | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 24 | 170 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure-2line | Kasus Pengobatan Setelah Gagal lini 2 | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 25 | 171 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | not-eval | Pernah diobati tidak diketahui hasilnya | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 26 | 172 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | unknown | Kasus dengan riwayat pengobatan tidak diketahui | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 27 | 173 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | other | Kasus lain-lain | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 28 | 174 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure | Kasus Pengobatan Setelah Gagal | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 29 | 177 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure-cat2 | Kasus Pengobatan Setelah Gagal Kategori 2 | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 30 | 178 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | treatment-non-conversion-2 | Pasien TB pengobatan kategori 2 yang tidak konversi setelah 3 bulan pengobatan | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 31 | 179 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | non-standard-treatment | Pasien TB yang mempunyai riwayat pengobatan TB yang tidak standar | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 32 | 180 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure-cat1 | Kasus Pengobatan Setelah Gagal Kategori 1 | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 33 | 181 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | treatment-non-conversion-1 | Pasien TB pengobatan kategori 1 yang tidak konversi | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 34 | 182 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | relapse | Kasus Baru | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 35 | 183 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | loss-to-follow-up | Kasus Setelah Loss To Follow Up | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 36 | 184 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | history-of-close-contact with-TB-DR | Terduga TB yang mempunyai riwayat kontak erat dengan pasien TB RO | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 37 | 185 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | co-infected-TBHIV | Pasien ko-infeksi TB-HIV yang tidak respons secara klinis maupun bakteriologis terhadap pemberian OAT | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 38 | 186 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure-2line | Kasus Pengobatan Setelah Gagal lini 2 | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 39 | 187 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TB-DR-relapse | Pasien TB RO kasus kambuh | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 40 | 188 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TB-DR-returns | Pasien TB RO yang kembali setelah putus berobat | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 41 | 191 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 154283005 | Pulmonary tuberculosis | http://snomed.info/sct |
| 42 | 192 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 423997002 | Tuberculosis, extrapulmonary | http://snomed.info/sct |
| 43 | 197 | Observation | `Observation.code.coding` | OC000191 | Jumlah Skoring TBC Anak | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 44 | 213 | ServiceRequest | `ServiceRequest.code.coding` | 24648-8 | XR Chest PA upright | http://loinc.org |
| 45 | 222 | Observation | `Observation.code.coding` | 24648-8 | XR Chest PA upright | http://loinc.org |
| 46 | 223 | Observation | `Observation.valueCodeableConcept.coding` | 707307002 | Tuberculosis screening chest X-ray abnormal | http://snomed.info/sct |
| 47 | 224 | Observation | `Observation.valueCodeableConcept.coding` | 707308007 | Tuberculosis screening chest X-ray normal | http://snomed.info/sct |
| 48 | 236 | DiagnosticReport | `DiagnosticReport.code.coding` | 24648-8 | XR Chest PA upright | http://loinc.org |
| 49 | 247 | Procedure | `Procedure.code.coding` | 424489006 | Mantoux test | http://snomed.info/sct |
| 50 | 249 | Procedure | `Procedure.code.coding` | 35140007 | Interferon gamma assay | http://snomed.info/sct |
| 51 | 251 | Procedure | `Procedure.code.coding` | 424489006 | Mantoux test | http://snomed.info/sct |
| 52 | 253 | Procedure | `Procedure.code.coding` | 35140007 | Interferon gamma assay | http://snomed.info/sct |
| 53 | 265 | Observation | `Observation.code.coding` | 23539-0 | Tuberculosis reaction wheal [Diameter] --3 days post dose mammalian tuberculin intradermal | http://loinc.org |
| 54 | 266 | Observation | `Observation.valueCodeableConcept.coding` | 268376005 | Mantoux: positive | http://snomed.info/sct |
| 55 | 267 | Observation | `Observation.valueCodeableConcept.coding` | 268375009 | Mantoux: negative | http://snomed.info/sct |
| 56 | 268 | Observation | `Observation.code.coding` | 71773-6 | Mycobacterium tuberculosis stimulated gamma interferon [Interpretation] in Blood Qualitative | http://loinc.org |
| 57 | 269 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 58 | 270 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 59 | 271 | Observation | `Observation.code.coding` | 23539-0 | Tuberculosis reaction wheal [Diameter] --3 days post dose mammalian tuberculin intradermal | http://loinc.org |
| 60 | 273 | Observation | `Observation.code.coding` | 71773-6 | Mycobacterium tuberculosis stimulated gamma interferon [Interpretation] in Blood Qualitative | http://loinc.org |
| 61 | 286 | Observation | `Observation.code.coding` | 55277-8 | HIV status | http://loinc.org |
| 62 | 287 | Observation | `Observation.valueCodeableConcept.coding` | 10828004 | Positive | http://snomed.info/sct |
| 63 | 288 | Observation | `Observation.valueCodeableConcept.coding` | 260385009 | Negative | http://snomed.info/sct |
| 64 | 289 | Observation | `Observation.valueCodeableConcept.coding` | 261665006 | Unknown | http://snomed.info/sct |
| 65 | 301 | Observation | `Observation.code.coding` | 33248-6 | Diabetes status | http://loinc.org |
| 66 | 302 | Observation | `Observation.valueCodeableConcept.coding` | 10828004 | Positive | http://snomed.info/sct |
| 67 | 303 | Observation | `Observation.valueCodeableConcept.coding` | 260385009 | Negative | http://snomed.info/sct |
| 68 | 304 | Observation | `Observation.valueCodeableConcept.coding` | 261665006 | Unknown | http://snomed.info/sct |
| 69 | 319 | ServiceRequest | `ServiceRequest.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 70 | 329 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 71 | 340 | Observation | `Observation.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 72 | 341 | Observation | `Observation.valueCodeableConcept.coding` | 260385009 | Negative | http://snomed.info/sct |
| 73 | 342 | Observation | `Observation.valueCodeableConcept.coding` | LA11841-6 | 1+ | http://loinc.org |
| 74 | 343 | Observation | `Observation.valueCodeableConcept.coding` | LA11842-4 | 2+ | http://loinc.org |
| 75 | 344 | Observation | `Observation.valueCodeableConcept.coding` | LA11843-2 | 3+ | http://loinc.org |
| 76 | 358 | DiagnosticReport | `DiagnosticReport.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 77 | 374 | ServiceRequest | `ServiceRequest.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 78 | 384 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 79 | 395 | Observation | `Observation.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 80 | 396 | Observation | `Observation.valueCodeableConcept.coding` | 260385009 | Negative | http://snomed.info/sct |
| 81 | 397 | Observation | `Observation.valueCodeableConcept.coding` | LA11841-6 | 1+ | http://loinc.org |
| 82 | 398 | Observation | `Observation.valueCodeableConcept.coding` | LA11842-4 | 2+ | http://loinc.org |
| 83 | 399 | Observation | `Observation.valueCodeableConcept.coding` | LA11843-2 | 3+ | http://loinc.org |
| 84 | 413 | DiagnosticReport | `DiagnosticReport.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 85 | 429 | ServiceRequest | `ServiceRequest.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 86 | 430 | ServiceRequest | `ServiceRequest.code.coding` | 89371-9 | MTB complex DNA and rpoB RIF resistance mutation panel [Presence] | http://loinc.org |
| 87 | 431 | ServiceRequest | `ServiceRequest.code.coding` | X099379 | Pemeriksaan TCM XDR | http://terminology.kemkes.go.id/CodeSystem/examination |
| 88 | 432 | ServiceRequest | `ServiceRequest.code.coding` | X099380 | Line Probe Assay (LPA) Lini 1 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 89 | 433 | ServiceRequest | `ServiceRequest.code.coding` | X099381 | Line Probe Assay (LPA) Lini 2 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 90 | 434 | ServiceRequest | `ServiceRequest.code.coding` | X099388 | Biakan TB | http://terminology.kemkes.go.id/CodeSystem/examination |
| 91 | 435 | ServiceRequest | `ServiceRequest.code.coding` | X099383 | Pemeriksaan Paket Standar Kepekaan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 92 | 436 | ServiceRequest | `ServiceRequest.code.coding` | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 93 | 437 | ServiceRequest | `ServiceRequest.code.coding` | MK099927 | Pemeriksaan PCR Open System | http://terminology.kemkes.go.id/CodeSystem/examination |
| 94 | 445 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 95 | 455 | Observation | `Observation.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 96 | 456 | Observation | `Observation.code.coding` | 89371-9 | MTB complex DNA and rpoB RIF resistance mutation panel [Presence] | http://loinc.org |
| 97 | 457 | Observation | `Observation.code.coding` | X099379 | Pemeriksaan TCM XDR | http://terminology.kemkes.go.id/CodeSystem/examination |
| 98 | 458 | Observation | `Observation.code.coding` | X099380 | Line Probe Assay (LPA) Lini 1 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 99 | 459 | Observation | `Observation.code.coding` | X099381 | Line Probe Assay (LPA) Lini 2 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 100 | 460 | Observation | `Observation.code.coding` | X099388 | Biakan TB | http://terminology.kemkes.go.id/CodeSystem/examination |
| 101 | 461 | Observation | `Observation.code.coding` | X099383 | Pemeriksaan Paket Standar Kepekaan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 102 | 462 | Observation | `Observation.code.coding` | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 103 | 463 | Observation | `Observation.code.coding` | MK099927 | Pemeriksaan PCR Open System | http://terminology.kemkes.go.id/CodeSystem/examination |
| 104 | 464 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 105 | 465 | Observation | `Observation.valueCodeableConcept.coding` | X099770 | Rifampisin sensitive | http://terminology.kemkes.go.id/CodeSystem/examination |
| 106 | 466 | Observation | `Observation.valueCodeableConcept.coding` | X099771 | Rifampisin resistan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 107 | 467 | Observation | `Observation.valueCodeableConcept.coding` | X099772 | Rifampisin indeterminate | http://terminology.kemkes.go.id/CodeSystem/examination |
| 108 | 483 | DiagnosticReport | `DiagnosticReport.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 109 | 485 | DiagnosticReport | `DiagnosticReport.code.coding` | 89371-9 | MTB complex DNA and rpoB RIF resistance mutation panel [Presence] | http://loinc.org |
| 110 | 487 | DiagnosticReport | `DiagnosticReport.code.coding` | X099379 | Pemeriksaan TCM XDR | http://terminology.kemkes.go.id/CodeSystem/examination |
| 111 | 489 | DiagnosticReport | `DiagnosticReport.code.coding` | X099380 | Line Probe Assay (LPA) Lini 1 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 112 | 491 | DiagnosticReport | `DiagnosticReport.code.coding` | X099381 | Line Probe Assay (LPA) Lini 2 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 113 | 493 | DiagnosticReport | `DiagnosticReport.code.coding` | X099388 | Biakan TB | http://terminology.kemkes.go.id/CodeSystem/examination |
| 114 | 495 | DiagnosticReport | `DiagnosticReport.code.coding` | X099383 | Pemeriksaan Paket Standar Kepekaan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 115 | 497 | DiagnosticReport | `DiagnosticReport.code.coding` | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 116 | 499 | DiagnosticReport | `DiagnosticReport.code.coding` | MK099927 | Pemeriksaan PCR Open System | http://terminology.kemkes.go.id/CodeSystem/examination |
| 117 | 515 | ServiceRequest | `ServiceRequest.code.coding` | X099379 | Pemeriksaan TCM XDR | http://terminology.kemkes.go.id/CodeSystem/examination |
| 118 | 523 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 119 | 533 | Observation | `Observation.code.coding` | X099379 | Pemeriksaan TCM XDR | http://terminology.kemkes.go.id/CodeSystem/examination |
| 120 | 534 | Observation | `Observation.valueCodeableConcept.coding` | X099781 | Hasil Valid | http://terminology.kemkes.go.id/CodeSystem/examination |
| 121 | 539 | Observation | `Observation.component.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 122 | 540 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 123 | 541 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 124 | 543 | Observation | `Observation.component.code.coding` | X099391 | H Dosis Rendah (Low) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 125 | 544 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 126 | 545 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 127 | 546 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 128 | 548 | Observation | `Observation.component.code.coding` | 89488-1 | Isoniazid [Susceptibility] by Genotype method | http://loinc.org |
| 129 | 549 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 130 | 550 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 131 | 551 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 132 | 553 | Observation | `Observation.component.code.coding` | 96110-2 | Ethionamide [Susceptibility] by Genotype method | http://loinc.org |
| 133 | 554 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 134 | 555 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 135 | 557 | Observation | `Observation.component.code.coding` | X099392 | FQ Dosis Rendah (Low) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 136 | 558 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 137 | 559 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 138 | 560 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 139 | 562 | Observation | `Observation.component.code.coding` | 89487-3 | Fluoroquinolone [Susceptibility] by Genotype method | http://loinc.org |
| 140 | 563 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 141 | 564 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 142 | 565 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 143 | 567 | Observation | `Observation.component.code.coding` | 89484-0 | Amikacin [Susceptibility] by Genotype method | http://loinc.org |
| 144 | 568 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 145 | 569 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 146 | 570 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 147 | 572 | Observation | `Observation.component.code.coding` | 89482-4 | Kanamycin [Susceptibility] by Genotype method | http://loinc.org |
| 148 | 573 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 149 | 574 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 150 | 575 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 151 | 577 | Observation | `Observation.component.code.coding` | 89483-2 | Capreomycin [Susceptibility] by Genotype method | http://loinc.org |
| 152 | 578 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 153 | 579 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 154 | 580 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 155 | 592 | DiagnosticReport | `DiagnosticReport.code.coding` | X099379 | Pemeriksaan TCM XDR | http://terminology.kemkes.go.id/CodeSystem/examination |
| 156 | 608 | ServiceRequest | `ServiceRequest.code.coding` | X099380 | Line Probe Assay (LPA) Lini 1 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 157 | 616 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 158 | 626 | Observation | `Observation.code.coding` | X099380 | Line Probe Assay (LPA) Lini 1 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 159 | 627 | Observation | `Observation.valueCodeableConcept.coding` | X099781 | Hasil Valid | http://terminology.kemkes.go.id/CodeSystem/examination |
| 160 | 630 | Observation | `Observation.component.code.coding` | 13956-8 | Mycobacterium tuberculosis DNA [Presence] in Specimen by NAA with probe detection | http://loinc.org |
| 161 | 631 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 162 | 632 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 163 | 634 | Observation | `Observation.component.code.coding` | 89489-9 | rifAMPin [Susceptibility] by Genotype method | http://loinc.org |
| 164 | 635 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 165 | 636 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 166 | 637 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 167 | 638 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 168 | 640 | Observation | `Observation.component.code.coding` | 89488-1 | Isoniazid [Susceptibility] by Genotype method | http://loinc.org |
| 169 | 641 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 170 | 642 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 171 | 643 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 172 | 644 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 173 | 656 | DiagnosticReport | `DiagnosticReport.code.coding` | X099380 | Line Probe Assay (LPA) Lini 1 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 174 | 672 | ServiceRequest | `ServiceRequest.code.coding` | X099381 | Line Probe Assay (LPA) Lini 2 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 175 | 680 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 176 | 690 | Observation | `Observation.code.coding` | X099381 | Line Probe Assay (LPA) Lini 2 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 177 | 691 | Observation | `Observation.valueCodeableConcept.coding` | X099781 | Hasil Valid | http://terminology.kemkes.go.id/CodeSystem/examination |
| 178 | 694 | Observation | `Observation.component.code.coding` | 13956-8 | Mycobacterium tuberculosis DNA [Presence] in Specimen by NAA with probe detection | http://loinc.org |
| 179 | 695 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 180 | 696 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 181 | 698 | Observation | `Observation.component.code.coding` | 20629-2 | levoFLOXacin [Susceptibility] | http://loinc.org |
| 182 | 699 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 183 | 700 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 184 | 701 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 185 | 702 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 186 | 704 | Observation | `Observation.component.code.coding` | 96112-8 | Moxifloxacin [Susceptibility] by Genotype method | http://loinc.org |
| 187 | 705 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 188 | 706 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 189 | 707 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 190 | 708 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 191 | 710 | Observation | `Observation.component.code.coding` | X099775 | Moxifloxacin DT (Mfx DT) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 192 | 711 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 193 | 712 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 194 | 713 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 195 | 714 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 196 | 716 | Observation | `Observation.component.code.coding` | 89482-4 | Kanamycin [Susceptibility] by Genotype method | http://loinc.org |
| 197 | 717 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 198 | 718 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 199 | 719 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 200 | 720 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 201 | 722 | Observation | `Observation.component.code.coding` | 89484-0 | Amikacin [Susceptibility] by Genotype method | http://loinc.org |
| 202 | 723 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 203 | 724 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 204 | 725 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 205 | 726 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 206 | 728 | Observation | `Observation.component.code.coding` | 89483-2 | Capreomycin [Susceptibility] by Genotype method | http://loinc.org |
| 207 | 729 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 208 | 730 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 209 | 731 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 210 | 732 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 211 | 744 | DiagnosticReport | `DiagnosticReport.code.coding` | X099381 | Line Probe Assay (LPA) Lini 2 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 212 | 760 | ServiceRequest | `ServiceRequest.code.coding` | X099388 | Biakan TB | http://terminology.kemkes.go.id/CodeSystem/examination |
| 213 | 768 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 214 | 778 | Observation | `Observation.code.coding` | X099388 | Biakan TB | http://terminology.kemkes.go.id/CodeSystem/examination |
| 215 | 779 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 216 | 780 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 217 | 781 | Observation | `Observation.valueCodeableConcept.coding` | LA11841-6 | + | http://loinc.org |
| 218 | 782 | Observation | `Observation.valueCodeableConcept.coding` | LA11842-4 | ++ | http://loinc.org |
| 219 | 783 | Observation | `Observation.valueCodeableConcept.coding` | LA11843-2 | +++ | http://loinc.org |
| 220 | 784 | Observation | `Observation.valueCodeableConcept.coding` | 110379001 | Mycobacterium, non-tuberculosis (organism) | http://snomed.info/sct |
| 221 | 797 | DiagnosticReport | `DiagnosticReport.code.coding` | X099388 | Biakan TB | http://terminology.kemkes.go.id/CodeSystem/examination |
| 222 | 813 | ServiceRequest | `ServiceRequest.code.coding` | X099383 | Pemeriksaan Paket Standar Kepekaan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 223 | 821 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 224 | 831 | Observation | `Observation.code.coding` | X099383 | Pemeriksaan Paket Standar Kepekaan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 225 | 834 | Observation | `Observation.component.code.coding` | X099776 | H High Dosage [Susceptibility] by Method for Slow-growing mycobacteria | http://terminology.kemkes.go.id/CodeSystem/examination |
| 226 | 835 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 227 | 836 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 228 | 837 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 229 | 840 | Observation | `Observation.component.code.coding` | 20383-6 | Isoniazid [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 230 | 841 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 231 | 842 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 232 | 843 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 233 | 846 | Observation | `Observation.component.code.coding` | 23609-1 | Kanamycin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 234 | 847 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 235 | 848 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 236 | 849 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 237 | 852 | Observation | `Observation.component.code.coding` | 23607-5 | Capreomycin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 238 | 853 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 239 | 854 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 240 | 855 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 241 | 858 | Observation | `Observation.component.code.coding` | 53716-7 | levoFLOXacin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 242 | 859 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 243 | 860 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 244 | 861 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 245 | 864 | Observation | `Observation.component.code.coding` | X099778 | Moxifloxacin High Dosage [Susceptibility] by Method for Slow-growing mycobacteria | http://terminology.kemkes.go.id/CodeSystem/examination |
| 246 | 865 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 247 | 866 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 248 | 867 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 249 | 870 | Observation | `Observation.component.code.coding` | 41502-6 | Moxifloxacin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 250 | 871 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 251 | 872 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 252 | 873 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 253 | 876 | Observation | `Observation.component.code.coding` | SP000472 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya | http://terminology.kemkes.go.id/sp |
| 254 | 878 | Observation | `Observation.component.code.coding` | SP000473 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 1 | http://terminology.kemkes.go.id/sp |
| 255 | 880 | Observation | `Observation.component.code.coding` | SP000474 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 2 | http://terminology.kemkes.go.id/sp |
| 256 | 882 | Observation | `Observation.component.code.coding` | SP000475 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 3 | http://terminology.kemkes.go.id/sp |
| 257 | 884 | Observation | `Observation.component.code.coding` | SP000476 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 4 | http://terminology.kemkes.go.id/sp |
| 258 | 886 | Observation | `Observation.component.code.coding` | SP000477 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 5 | http://terminology.kemkes.go.id/sp |
| 259 | 900 | DiagnosticReport | `DiagnosticReport.code.coding` | X099383 | Pemeriksaan Paket Standar Kepekaan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 260 | 914 | Observation | `Observation.code.coding` | 106229004 | Qualifier for type of diagnosis | http://snomed.info/sct |
| 261 | 915 | Observation | `Observation.valueCodeableConcept.coding` | tb-bac | Terkonfirmasi bakteriologis | http://terminology.kemkes.go.id/CodeSystem/tb-case-definition |
| 262 | 916 | Observation | `Observation.valueCodeableConcept.coding` | tb-clin | Terdiagnosis klinis | http://terminology.kemkes.go.id/CodeSystem/tb-case-definition |
| 263 | 930 | CarePlan | `CarePlan.activity.detail.code.coding` | TK000022 | Akan diobati/dirujuk | http://terminology.kemkes.go.id |
| 264 | 931 | CarePlan | `CarePlan.activity.detail.code.coding` | 699618001 | Administration of prophylactic antituberculosis agent | http://snomed.info/sct |
| 265 | 932 | CarePlan | `CarePlan.activity.detail.code.coding` | 266714009 | Previous treatment continue | http://snomed.info/sct |
| 266 | 935 | CarePlan | `CarePlan.activity.detail.statusReason.coding` | 406149000 | Medication declined | http://snomed.info/sct |
| 267 | 936 | CarePlan | `CarePlan.activity.detail.statusReason.coding` | 419099009 | Dead | http://snomed.info/sct |
| 268 | 937 | CarePlan | `CarePlan.activity.detail.statusReason.coding` | 399307001 | Lost to follow-up | http://snomed.info/sct |
| 269 | 955 | Observation | `Observation.code.coding` | 365866002 | Finding of human immunodeficiency virus status | http://snomed.info/sct |
| 270 | 956 | Observation | `Observation.valueCodeableConcept.coding` | 165816005 | Human immunodeficiency virus detected | http://snomed.info/sct |
| 271 | 957 | Observation | `Observation.valueCodeableConcept.coding` | 165815009 | Human immunodeficiency virus not detected | http://snomed.info/sct |
| 272 | 967 | Procedure | `Procedure.code.coding` | SP000046 | Terapi Antiretroviral (ART) | http://terminology.kemkes.go.id/sp |
| 273 | 980 | Observation | `Observation.code.coding` | SP000047 | Hasil Tes Diabetes Melitus | http://terminology.kemkes.go.id/sp |
| 274 | 981 | Observation | `Observation.valueCodeableConcept.coding` | 10828004 | Positive | http://snomed.info/sct |
| 275 | 982 | Observation | `Observation.valueCodeableConcept.coding` | 260385009 | Negative | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah | Code |
|---|---|---|
| http://loinc.org | 130 | 24648-8, 24648-8, 24648-8, 23539-0, 71773-6, LA6576-8, LA6577-6, 23539-0, 71773-6, 55277-8, 33248-6, 11545-1, 11545-1, LA11841-6, LA11842-4, LA11843-2, 11545-1, 11545-1, 11545-1, LA11841-6, LA11842-4, LA11843-2, 11545-1, 11545-1, 89371-9, 11545-1, 89371-9, LA6577-6, 11545-1, 89371-9, 88874-3, LA11882-0, LA11883-8, LA11882-0, LA11883-8, LA11884-6, 89488-1, LA11882-0, LA11883-8, LA11884-6, 96110-2, LA11882-0, LA11883-8, LA11882-0, LA11883-8, LA11884-6, 89487-3, LA11882-0, LA11883-8, LA11884-6, 89484-0, LA11882-0, LA11883-8, LA11884-6, 89482-4, LA11882-0, LA11883-8, LA11884-6, 89483-2, LA11882-0, LA11883-8, LA11884-6, 13956-8, LA6576-8, LA6577-6, 89489-9, LA11882-0, LA11883-8, LA11884-6, 89488-1, LA11882-0, LA11883-8, LA11884-6, 13956-8, LA6576-8, LA6577-6, 20629-2, LA11882-0, LA11883-8, LA11884-6, 96112-8, LA11882-0, LA11883-8, LA11884-6, LA11882-0, LA11883-8, LA11884-6, 89482-4, LA11882-0, LA11883-8, LA11884-6, 89484-0, LA11882-0, LA11883-8, LA11884-6, 89483-2, LA11882-0, LA11883-8, LA11884-6, LA6577-6, LA6576-8, LA11841-6, LA11842-4, LA11843-2, LA24225-7, LA6676-6, LA16550-8, 20383-6, LA24225-7, LA6676-6, LA16550-8, 23609-1, LA24225-7, LA6676-6, LA16550-8, 23607-5, LA24225-7, LA6676-6, LA16550-8, 53716-7, LA24225-7, LA6676-6, LA16550-8, LA24225-7, LA6676-6, LA16550-8, 41502-6, LA24225-7, LA6676-6, LA16550-8 |
| http://terminology.kemkes.go.id/CodeSystem/examination | 55 | X099379, X099380, X099381, X099388, X099383, MK099926, MK099927, X099379, X099380, X099381, X099388, X099383, MK099926, MK099927, X099770, X099771, X099772, X099379, X099380, X099381, X099388, X099383, MK099926, MK099927, X099379, X099379, X099781, X099391, X099392, X099379, X099380, X099380, X099781, X099774, X099774, X099380, X099381, X099381, X099781, X099774, X099774, X099775, X099774, X099774, X099774, X099774, X099381, X099388, X099388, X099388, X099383, X099383, X099776, X099778, X099383 |
| http://snomed.info/sct | 40 | 257622000, 424144002, 154283005, 423997002, 707307002, 707308007, 424489006, 35140007, 424489006, 35140007, 268376005, 268375009, 10828004, 260385009, 261665006, 10828004, 260385009, 261665006, 119334006, 260385009, 119334006, 260385009, 119334006, 119334006, 119334006, 119334006, 119334006, 110379001, 119334006, 106229004, 699618001, 266714009, 406149000, 419099009, 399307001, 365866002, 165816005, 165815009, 10828004, 260385009 |
| http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment | 22 | new, relapse, failure-cat1, failure-cat2, loss-to-follow-up, failure-2line, not-eval, unknown, other, failure, failure-cat2, treatment-non-conversion-2, non-standard-treatment, failure-cat1, treatment-non-conversion-1, relapse, loss-to-follow-up, history-of-close-contact with-TB-DR, co-infected-TBHIV, failure-2line, TB-DR-relapse, TB-DR-returns |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 8 | EHA000001, EHA000002, EHA000003, EHA000004, EHA000005, QRI000001, QRI000002, OC000191 |
| http://terminology.kemkes.go.id/sp | 8 | SP000472, SP000473, SP000474, SP000475, SP000476, SP000477, SP000046, SP000047 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 6 | TB-SO, TB-RO, TB-SO, TB-RO, TB-SO, TB-RO |
| http://hl7.org/fhir/sid/icd-10 | 3 | Z03.0, A15.0, A16.2 |
| http://terminology.kemkes.go.id/CodeSystem/tb-case-definition | 2 | tb-bac, tb-clin |
| http://terminology.kemkes.go.id | 1 | TK000022 |
| **Total** | **275** | |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
