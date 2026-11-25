# Output Form: SITB TB 06

Sumber: `mapping/phdt-data-dictionary-sitb-tb06.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-sitb-tb06.csv) · [struktur file mentah](../raw/sitb-tb06-kolom.md)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 56 |
| Code (`jumlah code` = 1) | 301 |
| Code unik (code + CodeSystem) | 124 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 9 |
| Variabel BQ (unik) | 92 |
| Variabel raw (kolom Excel export) | 96 |

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
| 1 | 20 | Organization | `Organization.type` | SP000367 | Kementerian Kesehatan | http://terminology.kemkes.go.id/CodeSystem/organization-ownership |
| 2 | 21 | Organization | `Organization.type` | SP000368 | Pemerintah Daerah Kabupaten/Kota | http://terminology.kemkes.go.id/CodeSystem/organization-ownership |
| 3 | 79 | EpisodeOfCare | `EpisodeOfCare.type.coding` | TB-SO | Tuberkulosis Sensitif Obat | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 4 | 80 | EpisodeOfCare | `EpisodeOfCare.type.coding` | TB-RO | Tuberkulosis Resisten Obat | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 5 | 90 | EpisodeOfCare | `EpisodeOfCare.type.coding` | TB-SO | Tuberkulosis Sensitif Obat | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 6 | 91 | EpisodeOfCare | `EpisodeOfCare.type.coding` | TB-RO | Tuberkulosis Resisten Obat | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 7 | 105 | EpisodeOfCare | `EpisodeOfCare.type.coding` | TB-SO | Tuberkulosis Sensitif Obat | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 8 | 106 | EpisodeOfCare | `EpisodeOfCare.type.coding` | TB-RO | Tuberkulosis Resisten Obat | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 9 | 120 | Encounter | `Encounter.hospitalization.admitSource.coding` | EHA000001 | Kader/ Komunitas | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 10 | 121 | Encounter | `Encounter.hospitalization.admitSource.coding` | EHA000002 | Datang sendiri | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 11 | 122 | Encounter | `Encounter.hospitalization.admitSource.coding` | EHA000003 | Kegiatan ACF | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 12 | 123 | Encounter | `Encounter.hospitalization.admitSource.coding` | 257622000 | Healthcare facility | http://snomed.info/sct |
| 13 | 124 | Encounter | `Encounter.hospitalization.admitSource.coding` | EHA000004 | Skrining TBC DM | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 14 | 125 | Encounter | `Encounter.hospitalization.admitSource.coding` | EHA000005 | Pemadanan Data BPJS | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 15 | 154 | Condition | `Condition.code.coding` | Z03.0 | Observation for suspected tuberculosis | http://hl7.org/fhir/sid/icd-10 |
| 16 | 162 | Condition | `Condition.code.coding` | A15.0 | Tuberculosis of lung, confirmed by sputum microscopy with or without culture | http://hl7.org/fhir/sid/icd-10 |
| 17 | 163 | Condition | `Condition.code.coding` | A16.2 | Tuberculosis of lung, without mention of bacteriological or histological confirmation | http://hl7.org/fhir/sid/icd-10 |
| 18 | 172 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 19 | 197 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | QRI000001 | Terduga TBC SO | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 20 | 198 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | QRI000002 | Terduga TBC RO | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 21 | 201 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | new | Kasus Baru | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 22 | 202 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | relapse | Kasus Kambuh | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 23 | 203 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure-cat1 | Kasus Pengobatan Setelah Gagal Kategori 1 | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 24 | 204 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure-cat2 | Kasus Pengobatan Setelah Gagal Kategori 2 | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 25 | 205 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | loss-to-follow-up | Kasus Setelah Loss To Follow Up | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 26 | 206 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure-2line | Kasus Pengobatan Setelah Gagal lini 2 | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 27 | 207 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | not-eval | Pernah diobati tidak diketahui hasilnya | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 28 | 208 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | unknown | Kasus dengan riwayat pengobatan tidak diketahui | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 29 | 209 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | other | Kasus lain-lain | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 30 | 210 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure | Kasus Pengobatan Setelah Gagal | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 31 | 213 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure-cat2 | Kasus Pengobatan Setelah Gagal Kategori 2 | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 32 | 214 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | treatment-non-conversion-2 | Pasien TB pengobatan kategori 2 yang tidak konversi setelah 3 bulan pengobatan | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 33 | 215 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | non-standard-treatment | Pasien TB yang mempunyai riwayat pengobatan TB yang tidak standar | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 34 | 216 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure-cat1 | Kasus Pengobatan Setelah Gagal Kategori 1 | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 35 | 217 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | treatment-non-conversion-1 | Pasien TB pengobatan kategori 1 yang tidak konversi | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 36 | 218 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | relapse | Kasus Baru | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 37 | 219 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | loss-to-follow-up | Kasus Setelah Loss To Follow Up | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 38 | 220 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | history-of-close-contact with-TB-DR | Terduga TB yang mempunyai riwayat kontak erat dengan pasien TB RO | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 39 | 221 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | co-infected-TBHIV | Pasien ko-infeksi TB-HIV yang tidak respons secara klinis maupun bakteriologis terhadap pemberian OAT | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 40 | 222 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure-2line | Kasus Pengobatan Setelah Gagal lini 2 | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 41 | 223 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TB-DR-relapse | Pasien TB RO kasus kambuh | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 42 | 224 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TB-DR-returns | Pasien TB RO yang kembali setelah putus berobat | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 43 | 227 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 154283005 | Pulmonary tuberculosis | http://snomed.info/sct |
| 44 | 228 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 423997002 | Tuberculosis, extrapulmonary | http://snomed.info/sct |
| 45 | 233 | Observation | `Observation.code.coding` | OC000191 | Jumlah Skoring TBC Anak | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 46 | 235 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 47 | 249 | ServiceRequest | `ServiceRequest.code.coding` | 24648-8 | XR Chest PA upright | http://loinc.org |
| 48 | 258 | Observation | `Observation.code.coding` | 24648-8 | XR Chest PA upright | http://loinc.org |
| 49 | 259 | Observation | `Observation.valueCodeableConcept.coding` | 707307002 | Tuberculosis screening chest X-ray abnormal | http://snomed.info/sct |
| 50 | 260 | Observation | `Observation.valueCodeableConcept.coding` | 707308007 | Tuberculosis screening chest X-ray normal | http://snomed.info/sct |
| 51 | 261 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed |  |
| 52 | 272 | DiagnosticReport | `DiagnosticReport.code.coding` | 24648-8 | XR Chest PA upright | http://loinc.org |
| 53 | 283 | Procedure | `Procedure.code.coding` | 424489006 | Mantoux test | http://snomed.info/sct |
| 54 | 285 | Procedure | `Procedure.code.coding` | 35140007 | Interferon gamma assay | http://snomed.info/sct |
| 55 | 287 | Procedure | `Procedure.code.coding` | 424489006 | Mantoux test | http://snomed.info/sct |
| 56 | 289 | Procedure | `Procedure.code.coding` | 35140007 | Interferon gamma assay | http://snomed.info/sct |
| 57 | 301 | Observation | `Observation.code.coding` | 23539-0 | Tuberculosis reaction wheal [Diameter] --3 days post dose mammalian tuberculin intradermal | http://loinc.org |
| 58 | 302 | Observation | `Observation.valueCodeableConcept.coding` | 268376005 | Mantoux: positive | http://snomed.info/sct |
| 59 | 303 | Observation | `Observation.valueCodeableConcept.coding` | 268375009 | Mantoux: negative | http://snomed.info/sct |
| 60 | 304 | Observation | `Observation.code.coding` | 71773-6 | Mycobacterium tuberculosis stimulated gamma interferon [Interpretation] in Blood Qualitative | http://loinc.org |
| 61 | 305 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 62 | 306 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 63 | 307 | Observation | `Observation.code.coding` | 23539-0 | Tuberculosis reaction wheal [Diameter] --3 days post dose mammalian tuberculin intradermal | http://loinc.org |
| 64 | 308 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 65 | 309 | Observation | `Observation.code.coding` | 71773-6 | Mycobacterium tuberculosis stimulated gamma interferon [Interpretation] in Blood Qualitative | http://loinc.org |
| 66 | 310 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 67 | 322 | Observation | `Observation.code.coding` | 55277-8 | HIV status | http://loinc.org |
| 68 | 323 | Observation | `Observation.valueCodeableConcept.coding` | 10828004 | Positive | http://snomed.info/sct |
| 69 | 324 | Observation | `Observation.valueCodeableConcept.coding` | 260385009 | Negative | http://snomed.info/sct |
| 70 | 325 | Observation | `Observation.valueCodeableConcept.coding` | 261665006 | Unknown | http://snomed.info/sct |
| 71 | 337 | Observation | `Observation.code.coding` | 33248-6 | Diabetes status | http://loinc.org |
| 72 | 338 | Observation | `Observation.valueCodeableConcept.coding` | 10828004 | Positive | http://snomed.info/sct |
| 73 | 339 | Observation | `Observation.valueCodeableConcept.coding` | 260385009 | Negative | http://snomed.info/sct |
| 74 | 340 | Observation | `Observation.valueCodeableConcept.coding` | 261665006 | Unknown | http://snomed.info/sct |
| 75 | 355 | ServiceRequest | `ServiceRequest.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 76 | 365 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 77 | 376 | Observation | `Observation.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 78 | 377 | Observation | `Observation.valueCodeableConcept.coding` | 260385009 | Negative | http://snomed.info/sct |
| 79 | 378 | Observation | `Observation.valueCodeableConcept.coding` | LA11841-6 | 1+ | http://loinc.org |
| 80 | 379 | Observation | `Observation.valueCodeableConcept.coding` | LA11842-4 | 2+ | http://loinc.org |
| 81 | 380 | Observation | `Observation.valueCodeableConcept.coding` | LA11843-2 | 3+ | http://loinc.org |
| 82 | 382 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 83 | 394 | DiagnosticReport | `DiagnosticReport.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 84 | 410 | ServiceRequest | `ServiceRequest.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 85 | 420 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 86 | 431 | Observation | `Observation.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 87 | 432 | Observation | `Observation.valueCodeableConcept.coding` | 260385009 | Negative | http://snomed.info/sct |
| 88 | 433 | Observation | `Observation.valueCodeableConcept.coding` | LA11841-6 | 1+ | http://loinc.org |
| 89 | 434 | Observation | `Observation.valueCodeableConcept.coding` | LA11842-4 | 2+ | http://loinc.org |
| 90 | 435 | Observation | `Observation.valueCodeableConcept.coding` | LA11843-2 | 3+ | http://loinc.org |
| 91 | 437 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 92 | 449 | DiagnosticReport | `DiagnosticReport.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 93 | 465 | ServiceRequest | `ServiceRequest.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 94 | 466 | ServiceRequest | `ServiceRequest.code.coding` | 89371-9 | MTB complex DNA and rpoB RIF resistance mutation panel [Presence] | http://loinc.org |
| 95 | 467 | ServiceRequest | `ServiceRequest.code.coding` | X099379 | Pemeriksaan TCM XDR | http://terminology.kemkes.go.id/CodeSystem/examination |
| 96 | 468 | ServiceRequest | `ServiceRequest.code.coding` | X099380 | Line Probe Assay (LPA) Lini 1 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 97 | 469 | ServiceRequest | `ServiceRequest.code.coding` | X099381 | Line Probe Assay (LPA) Lini 2 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 98 | 470 | ServiceRequest | `ServiceRequest.code.coding` | X099388 | Biakan TB | http://terminology.kemkes.go.id/CodeSystem/examination |
| 99 | 471 | ServiceRequest | `ServiceRequest.code.coding` | X099383 | Pemeriksaan Paket Standar Kepekaan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 100 | 472 | ServiceRequest | `ServiceRequest.code.coding` | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 101 | 473 | ServiceRequest | `ServiceRequest.code.coding` | MK099927 | Pemeriksaan PCR Open System | http://terminology.kemkes.go.id/CodeSystem/examination |
| 102 | 481 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 103 | 491 | Observation | `Observation.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 104 | 492 | Observation | `Observation.code.coding` | 89371-9 | MTB complex DNA and rpoB RIF resistance mutation panel [Presence] | http://loinc.org |
| 105 | 493 | Observation | `Observation.code.coding` | X099379 | Pemeriksaan TCM XDR | http://terminology.kemkes.go.id/CodeSystem/examination |
| 106 | 494 | Observation | `Observation.code.coding` | X099380 | Line Probe Assay (LPA) Lini 1 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 107 | 495 | Observation | `Observation.code.coding` | X099381 | Line Probe Assay (LPA) Lini 2 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 108 | 496 | Observation | `Observation.code.coding` | X099388 | Biakan TB | http://terminology.kemkes.go.id/CodeSystem/examination |
| 109 | 497 | Observation | `Observation.code.coding` | X099383 | Pemeriksaan Paket Standar Kepekaan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 110 | 498 | Observation | `Observation.code.coding` | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 111 | 499 | Observation | `Observation.code.coding` | MK099927 | Pemeriksaan PCR Open System | http://terminology.kemkes.go.id/CodeSystem/examination |
| 112 | 500 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 113 | 501 | Observation | `Observation.valueCodeableConcept.coding` | X099770 | Rifampisin sensitive | http://terminology.kemkes.go.id/CodeSystem/examination |
| 114 | 502 | Observation | `Observation.valueCodeableConcept.coding` | X099771 | Rifampisin resistan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 115 | 503 | Observation | `Observation.valueCodeableConcept.coding` | X099772 | Rifampisin indeterminate | http://terminology.kemkes.go.id/CodeSystem/examination |
| 116 | 504 | Observation | `Observation.dataAbsentReason.coding` | LA15841-2 | Invalid result | http://loinc.org |
| 117 | 505 | Observation | `Observation.dataAbsentReason.coding` | error | Error | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 118 | 506 | Observation | `Observation.dataAbsentReason.coding` | OD000001 | Tidak ada hasil | http://terminology.kemkes.go.id/CodeSystem/data-absent-reason |
| 119 | 507 | Observation | `Observation.dataAbsentReason.coding` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 120 | 519 | DiagnosticReport | `DiagnosticReport.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 121 | 521 | DiagnosticReport | `DiagnosticReport.code.coding` | 89371-9 | MTB complex DNA and rpoB RIF resistance mutation panel [Presence] | http://loinc.org |
| 122 | 523 | DiagnosticReport | `DiagnosticReport.code.coding` | X099379 | Pemeriksaan TCM XDR | http://terminology.kemkes.go.id/CodeSystem/examination |
| 123 | 525 | DiagnosticReport | `DiagnosticReport.code.coding` | X099380 | Line Probe Assay (LPA) Lini 1 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 124 | 527 | DiagnosticReport | `DiagnosticReport.code.coding` | X099381 | Line Probe Assay (LPA) Lini 2 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 125 | 529 | DiagnosticReport | `DiagnosticReport.code.coding` | X099388 | Biakan TB | http://terminology.kemkes.go.id/CodeSystem/examination |
| 126 | 531 | DiagnosticReport | `DiagnosticReport.code.coding` | X099383 | Pemeriksaan Paket Standar Kepekaan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 127 | 533 | DiagnosticReport | `DiagnosticReport.code.coding` | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 128 | 535 | DiagnosticReport | `DiagnosticReport.code.coding` | MK099927 | Pemeriksaan PCR Open System | http://terminology.kemkes.go.id/CodeSystem/examination |
| 129 | 551 | ServiceRequest | `ServiceRequest.code.coding` | X099379 | Pemeriksaan TCM XDR | http://terminology.kemkes.go.id/CodeSystem/examination |
| 130 | 559 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 131 | 569 | Observation | `Observation.code.coding` | X099379 | Pemeriksaan TCM XDR | http://terminology.kemkes.go.id/CodeSystem/examination |
| 132 | 570 | Observation | `Observation.valueCodeableConcept.coding` | X099781 | Hasil Valid | http://terminology.kemkes.go.id/CodeSystem/examination |
| 133 | 571 | Observation | `Observation.dataAbsentReason.coding` | LA15841-2 | Invalid result | http://loinc.org |
| 134 | 572 | Observation | `Observation.dataAbsentReason.coding` | error | Error | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 135 | 573 | Observation | `Observation.dataAbsentReason.coding` | OD000001 | Tidak ada hasil | http://terminology.kemkes.go.id/CodeSystem/data-absent-reason |
| 136 | 575 | Observation | `Observation.component.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 137 | 576 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 138 | 577 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 139 | 579 | Observation | `Observation.component.code.coding` | X099391 | H Dosis Rendah (Low) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 140 | 580 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 141 | 581 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 142 | 582 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 143 | 584 | Observation | `Observation.component.code.coding` | 89488-1 | Isoniazid [Susceptibility] by Genotype method | http://loinc.org |
| 144 | 585 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 145 | 586 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 146 | 587 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 147 | 589 | Observation | `Observation.component.code.coding` | 96110-2 | Ethionamide [Susceptibility] by Genotype method | http://loinc.org |
| 148 | 590 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 149 | 591 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 150 | 593 | Observation | `Observation.component.code.coding` | X099392 | FQ Dosis Rendah (Low) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 151 | 594 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 152 | 595 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 153 | 596 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 154 | 598 | Observation | `Observation.component.code.coding` | 89487-3 | Fluoroquinolone [Susceptibility] by Genotype method | http://loinc.org |
| 155 | 599 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 156 | 600 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 157 | 601 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 158 | 603 | Observation | `Observation.component.code.coding` | 89484-0 | Amikacin [Susceptibility] by Genotype method | http://loinc.org |
| 159 | 604 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 160 | 605 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 161 | 606 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 162 | 608 | Observation | `Observation.component.code.coding` | 89482-4 | Kanamycin [Susceptibility] by Genotype method | http://loinc.org |
| 163 | 609 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 164 | 610 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 165 | 611 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 166 | 613 | Observation | `Observation.component.code.coding` | 89483-2 | Capreomycin [Susceptibility] by Genotype method | http://loinc.org |
| 167 | 614 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 168 | 615 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 169 | 616 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 170 | 628 | DiagnosticReport | `DiagnosticReport.code.coding` | X099379 | Pemeriksaan TCM XDR | http://terminology.kemkes.go.id/CodeSystem/examination |
| 171 | 644 | ServiceRequest | `ServiceRequest.code.coding` | X099380 | Line Probe Assay (LPA) Lini 1 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 172 | 652 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 173 | 662 | Observation | `Observation.code.coding` | X099380 | Line Probe Assay (LPA) Lini 1 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 174 | 663 | Observation | `Observation.valueCodeableConcept.coding` | X099781 | Hasil Valid | http://terminology.kemkes.go.id/CodeSystem/examination |
| 175 | 664 | Observation | `Observation.dataAbsentReason.coding` | LA15841-2 | Invalid result | http://loinc.org |
| 176 | 666 | Observation | `Observation.component.code.coding` | 13956-8 | Mycobacterium tuberculosis DNA [Presence] in Specimen by NAA with probe detection | http://loinc.org |
| 177 | 667 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 178 | 668 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 179 | 670 | Observation | `Observation.component.code.coding` | 89489-9 | rifAMPin [Susceptibility] by Genotype method | http://loinc.org |
| 180 | 671 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 181 | 672 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 182 | 673 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 183 | 674 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 184 | 676 | Observation | `Observation.component.code.coding` | 89488-1 | Isoniazid [Susceptibility] by Genotype method | http://loinc.org |
| 185 | 677 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 186 | 678 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 187 | 679 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 188 | 680 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 189 | 692 | DiagnosticReport | `DiagnosticReport.code.coding` | X099380 | Line Probe Assay (LPA) Lini 1 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 190 | 708 | ServiceRequest | `ServiceRequest.code.coding` | X099381 | Line Probe Assay (LPA) Lini 2 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 191 | 716 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 192 | 726 | Observation | `Observation.code.coding` | X099381 | Line Probe Assay (LPA) Lini 2 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 193 | 727 | Observation | `Observation.valueCodeableConcept.coding` | X099781 | Hasil Valid | http://terminology.kemkes.go.id/CodeSystem/examination |
| 194 | 728 | Observation | `Observation.dataAbsentReason.coding` | LA15841-2 | Invalid result | http://loinc.org |
| 195 | 730 | Observation | `Observation.component.code.coding` | 13956-8 | Mycobacterium tuberculosis DNA [Presence] in Specimen by NAA with probe detection | http://loinc.org |
| 196 | 731 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 197 | 732 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 198 | 734 | Observation | `Observation.component.code.coding` | 20629-2 | levoFLOXacin [Susceptibility] | http://loinc.org |
| 199 | 735 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 200 | 736 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 201 | 737 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 202 | 738 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 203 | 740 | Observation | `Observation.component.code.coding` | 96112-8 | Moxifloxacin [Susceptibility] by Genotype method | http://loinc.org |
| 204 | 741 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 205 | 742 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 206 | 743 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 207 | 744 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 208 | 746 | Observation | `Observation.component.code.coding` | X099775 | Moxifloxacin DT (Mfx DT) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 209 | 747 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 210 | 748 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 211 | 749 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 212 | 750 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 213 | 752 | Observation | `Observation.component.code.coding` | 89482-4 | Kanamycin [Susceptibility] by Genotype method | http://loinc.org |
| 214 | 753 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 215 | 754 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 216 | 755 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 217 | 756 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 218 | 758 | Observation | `Observation.component.code.coding` | 89484-0 | Amikacin [Susceptibility] by Genotype method | http://loinc.org |
| 219 | 759 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 220 | 760 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 221 | 761 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 222 | 762 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 223 | 764 | Observation | `Observation.component.code.coding` | 89483-2 | Capreomycin [Susceptibility] by Genotype method | http://loinc.org |
| 224 | 765 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 225 | 766 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 226 | 767 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 227 | 768 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 228 | 780 | DiagnosticReport | `DiagnosticReport.code.coding` | X099381 | Line Probe Assay (LPA) Lini 2 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 229 | 796 | ServiceRequest | `ServiceRequest.code.coding` | X099388 | Biakan TB | http://terminology.kemkes.go.id/CodeSystem/examination |
| 230 | 804 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 231 | 814 | Observation | `Observation.code.coding` | X099388 | Biakan TB | http://terminology.kemkes.go.id/CodeSystem/examination |
| 232 | 815 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 233 | 816 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 234 | 817 | Observation | `Observation.valueCodeableConcept.coding` | LA11841-6 | + | http://loinc.org |
| 235 | 818 | Observation | `Observation.valueCodeableConcept.coding` | LA11842-4 | ++ | http://loinc.org |
| 236 | 819 | Observation | `Observation.valueCodeableConcept.coding` | LA11843-2 | +++ | http://loinc.org |
| 237 | 820 | Observation | `Observation.valueCodeableConcept.coding` | 110379001 | Mycobacterium, non-tuberculosis (organism) | http://snomed.info/sct |
| 238 | 821 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 239 | 833 | DiagnosticReport | `DiagnosticReport.code.coding` | X099388 | Biakan TB | http://terminology.kemkes.go.id/CodeSystem/examination |
| 240 | 849 | ServiceRequest | `ServiceRequest.code.coding` | X099383 | Pemeriksaan Paket Standar Kepekaan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 241 | 857 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 242 | 867 | Observation | `Observation.code.coding` | X099383 | Pemeriksaan Paket Standar Kepekaan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 243 | 870 | Observation | `Observation.component.code.coding` | X099776 | H High Dosage [Susceptibility] by Method for Slow-growing mycobacteria | http://terminology.kemkes.go.id/CodeSystem/examination |
| 244 | 871 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 245 | 872 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 246 | 873 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 247 | 874 | Observation | `Observation.component.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 248 | 876 | Observation | `Observation.component.code.coding` | 20383-6 | Isoniazid [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 249 | 877 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 250 | 878 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 251 | 879 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 252 | 880 | Observation | `Observation.component.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 253 | 882 | Observation | `Observation.component.code.coding` | 23609-1 | Kanamycin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 254 | 883 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 255 | 884 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 256 | 885 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 257 | 886 | Observation | `Observation.component.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 258 | 888 | Observation | `Observation.component.code.coding` | 23607-5 | Capreomycin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 259 | 889 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 260 | 890 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 261 | 891 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 262 | 892 | Observation | `Observation.component.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 263 | 894 | Observation | `Observation.component.code.coding` | 53716-7 | levoFLOXacin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 264 | 895 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 265 | 896 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 266 | 897 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 267 | 898 | Observation | `Observation.component.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 268 | 900 | Observation | `Observation.component.code.coding` | X099778 | Moxifloxacin High Dosage [Susceptibility] by Method for Slow-growing mycobacteria | http://terminology.kemkes.go.id/CodeSystem/examination |
| 269 | 901 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 270 | 902 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 271 | 903 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 272 | 904 | Observation | `Observation.component.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 273 | 906 | Observation | `Observation.component.code.coding` | 41502-6 | Moxifloxacin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 274 | 907 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 275 | 908 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 276 | 909 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 277 | 910 | Observation | `Observation.component.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 278 | 912 | Observation | `Observation.component.code.coding` | SP000472 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya | http://terminology.kemkes.go.id/sp |
| 279 | 914 | Observation | `Observation.component.code.coding` | SP000473 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 1 | http://terminology.kemkes.go.id/sp |
| 280 | 916 | Observation | `Observation.component.code.coding` | SP000474 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 2 | http://terminology.kemkes.go.id/sp |
| 281 | 918 | Observation | `Observation.component.code.coding` | SP000475 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 3 | http://terminology.kemkes.go.id/sp |
| 282 | 920 | Observation | `Observation.component.code.coding` | SP000476 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 4 | http://terminology.kemkes.go.id/sp |
| 283 | 922 | Observation | `Observation.component.code.coding` | SP000477 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 5 | http://terminology.kemkes.go.id/sp |
| 284 | 936 | DiagnosticReport | `DiagnosticReport.code.coding` | X099383 | Pemeriksaan Paket Standar Kepekaan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 285 | 950 | Observation | `Observation.code.coding` | 106229004 | Qualifier for type of diagnosis | http://snomed.info/sct |
| 286 | 951 | Observation | `Observation.valueCodeableConcept.coding` | tb-bac | Terkonfirmasi bakteriologis | http://terminology.kemkes.go.id/CodeSystem/tb-case-definition |
| 287 | 952 | Observation | `Observation.valueCodeableConcept.coding` | tb-clin | Terdiagnosis klinis | http://terminology.kemkes.go.id/CodeSystem/tb-case-definition |
| 288 | 966 | CarePlan | `CarePlan.activity.detail.code.coding` | TK000022 | Akan diobati/dirujuk | http://terminology.kemkes.go.id |
| 289 | 967 | CarePlan | `CarePlan.activity.detail.code.coding` | 699618001 | Administration of prophylactic antituberculosis agent | http://snomed.info/sct |
| 290 | 968 | CarePlan | `CarePlan.activity.detail.code.coding` | 266714009 | Previous treatment continue | http://snomed.info/sct |
| 291 | 969 | CarePlan | `CarePlan.activity.detail.code.coding` | SP001136 | Belum Mulai Pengobatan | http://terminology.kemkes.go.id/sp |
| 292 | 972 | CarePlan | `CarePlan.activity.detail.statusReason.coding` | 406149000 | Medication declined | http://snomed.info/sct |
| 293 | 973 | CarePlan | `CarePlan.activity.detail.statusReason.coding` | 419099009 | Dead | http://snomed.info/sct |
| 294 | 974 | CarePlan | `CarePlan.activity.detail.statusReason.coding` | 399307001 | Lost to follow-up | http://snomed.info/sct |
| 295 | 992 | Observation | `Observation.code.coding` | 365866002 | Finding of human immunodeficiency virus status | http://snomed.info/sct |
| 296 | 993 | Observation | `Observation.valueCodeableConcept.coding` | 165816005 | Human immunodeficiency virus detected | http://snomed.info/sct |
| 297 | 994 | Observation | `Observation.valueCodeableConcept.coding` | 165815009 | Human immunodeficiency virus not detected | http://snomed.info/sct |
| 298 | 1004 | Procedure | `Procedure.code.coding` | SP000046 | Terapi Antiretroviral (ART) | http://terminology.kemkes.go.id/sp |
| 299 | 1017 | Observation | `Observation.code.coding` | SP000047 | Hasil Tes Diabetes Melitus | http://terminology.kemkes.go.id/sp |
| 300 | 1018 | Observation | `Observation.valueCodeableConcept.coding` | 10828004 | Positive | http://snomed.info/sct |
| 301 | 1019 | Observation | `Observation.valueCodeableConcept.coding` | 260385009 | Negative | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://loinc.org | 134 |
| http://terminology.kemkes.go.id/CodeSystem/examination | 55 |
| http://snomed.info/sct | 40 |
| http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment | 22 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 16 |
| http://terminology.kemkes.go.id/sp | 9 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 8 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 6 |
| http://hl7.org/fhir/sid/icd-10 | 3 |
| http://terminology.kemkes.go.id/CodeSystem/organization-ownership | 2 |
| http://terminology.kemkes.go.id/CodeSystem/data-absent-reason | 2 |
| http://terminology.kemkes.go.id/CodeSystem/tb-case-definition | 2 |
|  | 1 |
| http://terminology.kemkes.go.id | 1 |
| **Total** | **301** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
