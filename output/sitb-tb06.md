# Output Form: SITB TB 06

Sumber: `mapping/phdt-data-dictionary-sitb-tb06.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 54 |
| Code (`jumlah code` = 1) | 276 |
| Code unik (code + CodeSystem) | 117 |
| Variabel BQ (unik) | 93 |
| Variabel di Excel export | 97 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–27 | Patient | – | – | `no_rekam_medis` → `Patient.identifier.value` (5)<br>`nik_nomor_identitas_kependudukan` → `Patient.identifier.value` (8)<br>`nama_lengkap_terduga_tbc` → `Patient.name.text` (9)<br>`jenis_kelamin` → `Patient.gender` (10)<br>`alamat_lengkap_terduga_tbc_provinsi` → `Patient.address.extension.extension.valueCode` (16)<br>`alamat_lengkap_terduga_tbc_kabupatenkota` → `Patient.address.extension.extension.valueCode` (19)<br>`alamat_lengkap_terduga_tbc_kecamatan` → `Patient.address.extension.extension.valueCode` (22)<br>`alamat_lengkap_terduga_tbc_kelurahan` → `Patient.address.extension.extension.valueCode` (25)<br>`alamat_lengkap_terduga_tbc_alamat_lengkap` → `Patient.address.line` (26) |
| 2 | 29–38 | EpisodeOfCare | TB-SO | Tuberkulosis Sensitif Obat | `no_register_terduga` → `EpisodeOfCare.identifier` (29)<br>`klasifikasi_terduga_tbc` → `EpisodeOfCare.type.coding` (31)<br>`tanggal_didaftar` → `EpisodeOfCare.period.start` (33) |
| 3 | 41–53 | EpisodeOfCare | TB-SO | Tuberkulosis Sensitif Obat | `hasil_diagnosis` → `EpisodeOfCare.type.coding` (42)<br>`terkonfirmasi_tbc` → `EpisodeOfCare.status` (45)<br>`tanggal_hasil_diagnosis` → `EpisodeOfCare.statusHistory.period.start` (47) |
| 4 | 56–68 | EpisodeOfCare | TB-SO | Tuberkulosis Sensitif Obat | _Terkonfirmasi TBC_ → `EpisodeOfCare.status` (60, tanpa BQ) |
| 5 | 69–108 | Encounter | – | – | `no_register_sitb` → `Encounter.identifier` (70)<br>`dirujukdikirim_oleh` → `Encounter.hospitalization.admitSource.coding` (72)<br>`alamat_lengkap_faskes_kode_fasyankes` → `Encounter.serviceProvider.reference` (103) 🔎 lookup master data<br>`alamat_lengkap_faskes_nama_fasyankes` → `Encounter.serviceProvider.reference` (104) 🔎 lookup master data<br>`alamat_lengkap_faskes_jenis_fasyankes` → `Encounter.serviceProvider.reference` (105) 🔎 lookup master data<br>`alamat_lengkap_faskes_kepemilikan_fasyankes` → `Encounter.serviceProvider.reference` (106) 🔎 lookup master data<br>`alamat_lengkap_faskes_provinsi` → `Encounter.serviceProvider.reference` (107) 🔎 lookup master data<br>`alamat_lengkap_faskes_kabupatenkota` → `Encounter.serviceProvider.reference` (108) 🔎 lookup master data |
| 6 | 110–116 | Condition | Z03.0 | Observation for suspected tuberculosis | – |
| 7 | 118–125 | Condition | A15.0 | Tuberculosis of lung, confirmed by sputum microscopy with or without culture | – |
| 8 | 128–139 | Observation | 424144002 | Current chronological age | `umur_tahun` → `Observation.valueQuantity.value` (131) |
| 9 | 142–186 | QuestionnaireResponse | – | – | `klasifikasi_berdasarkan_riwayat_pengobatan_sebelumnya` → `QuestionnaireResponse.item.item.linkId` (157)<br>`kriteria_terduga_tbc_ro` → `QuestionnaireResponse.item.item.linkId` (169)<br>`lokasi_anatomi_penyakit` → `QuestionnaireResponse.item.item.linkId` (183) |
| 10 | 189–200 | Observation | OC000191 | Jumlah Skoring TBC Anak | `total_skoring_tbc_anak` → `Observation.valueInteger` (192) |
| 11 | 203–212 | ServiceRequest | 24648-8 | XR Chest PA upright | – |
| 12 | 214–226 | Observation | 24648-8 | XR Chest PA upright | `hasil_pemeriksaan_foto_toraks` → `Observation.valueCodeableConcept.coding` (217) |
| 13 | 228–238 | DiagnosticReport | 24648-8 | XR Chest PA upright | – |
| 14 | 240–255 | Procedure | 424489006 | Mantoux test | `dilakukan_pemeriksaan_tuberkulinigra` → `Procedure.category.coding` (240) |
| 15 | 257–275 | Observation | 23539-0 | Tuberculosis reaction wheal [Diameter] --3 days post dose mammalian tuberculin intradermal | `hasil_pemeriksaan_tuberkulinigra` → `Observation.valueCodeableConcept.coding` (260) |
| 16 | 278–290 | Observation | 55277-8 | HIV status | `status_hiv` → `Observation.valueCodeableConcept.coding` (281) |
| 17 | 293–305 | Observation | 33248-6 | Diabetes status | `riwayat_diabetes_melitus` → `Observation.valueCodeableConcept.coding` (296) |
| 18 | 308–318 | ServiceRequest | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | – |
| 19 | 320–329 | Specimen | 119334006 | Sputum specimen | `no_identitas_sediaan` → `Specimen.identifier` (321) |
| 20 | 331–347 | Observation | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | `hasil_pemeriksaan_mikroskopis_hasil_pemeriksaan_1` → `Observation.valueCodeableConcept.coding` (335)<br>`hasil_pemeriksaan_mikroskopis_tanggal_pemeriksaan_1` → `Observation.issued` (345) |
| 21 | 349–361 | DiagnosticReport | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | – |
| 22 | 363–373 | ServiceRequest | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | – |
| 23 | 375–384 | Specimen | 119334006 | Sputum specimen | `no_identitas_sediaan` → `Specimen.identifier` (376) |
| 24 | 386–402 | Observation | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | `hasil_pemeriksaan_mikroskopis_hasil_pemeriksaan_2` → `Observation.valueCodeableConcept.coding` (390)<br>`hasil_pemeriksaan_mikroskopis_tanggal_pemeriksaan_2` → `Observation.issued` (400) |
| 25 | 404–416 | DiagnosticReport | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | – |
| 26 | 419–436 | ServiceRequest | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | `jenis_pemeriksaan_diagnosis` → `ServiceRequest.category.coding` (419) |
| 27 | 438–445 | Specimen | 119334006 | Sputum specimen | – |
| 28 | 447–473 | Observation | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | `hasil_pemeriksaan_diagnosis_tbc` → `Observation.valueCodeableConcept.coding` (458)<br>`tanggal_hasil_pemeriksaan_diagnosis_tbc` → `Observation.issued` (470)<br>`keterangan_diisi_tempat_pemeriksaan_selain_mikroskopis` → `Observation.note.text` (471) |
| 29 | 475–502 | DiagnosticReport | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | – |
| 30 | 505–514 | ServiceRequest | X099379 | Pemeriksaan TCM XDR | – |
| 31 | 516–523 | Specimen | 119334006 | Sputum specimen | – |
| 32 | 525–582 | Observation | X099379 | Pemeriksaan TCM XDR | `hasil_pemeriksaan_xpert_tcm_xdr_validinvaliderrorno_result` → `Observation.valueCodeableConcept.coding` (528)<br>`hasil_pemeriksaan_xpert_tcm_xdr_mtb` → `Observation.component.code.coding` (533)<br>`hasil_pemeriksaan_xpert_tcm_xdr_h_dosis_rendah_low` → `Observation.component.code.coding` (537)<br>`hasil_pemeriksaan_xpert_tcm_xdr_h` → `Observation.component.code.coding` (542)<br>`hasil_pemeriksaan_xpert_tcm_xdr_eto` → `Observation.component.code.coding` (547)<br>`hasil_pemeriksaan_xpert_tcm_xdr_fq_dosis_rendah_low` → `Observation.component.code.coding` (551)<br>`hasil_pemeriksaan_xpert_tcm_xdr_fq` → `Observation.component.code.coding` (556)<br>`hasil_pemeriksaan_xpert_tcm_xdr_amk` → `Observation.component.code.coding` (561)<br>`hasil_pemeriksaan_xpert_tcm_xdr_km` → `Observation.component.code.coding` (566)<br>`hasil_pemeriksaan_xpert_tcm_xdr_cm` → `Observation.component.code.coding` (571)<br>`tanggal_hasil_pemeriksaan_tcmxdr` → `Observation.issued` (580) |
| 33 | 584–595 | DiagnosticReport | X099379 | Pemeriksaan TCM XDR | – |
| 34 | 598–607 | ServiceRequest | X099380 | Line Probe Assay (LPA) Lini 1 | – |
| 35 | 609–616 | Specimen | 119334006 | Sputum specimen | – |
| 36 | 618–646 | Observation | X099380 | Line Probe Assay (LPA) Lini 1 | `hasil_pemeriksaan_lpa_line_probe_assay_lini_1_invalid` → `Observation.valueCodeableConcept.coding` (621)<br>`hasil_pemeriksaan_lpa_line_probe_assay_lini_1_mtb` → `Observation.component.code.coding` (624)<br>`hasil_pemeriksaan_lpa_line_probe_assay_lini_1_r` → `Observation.component.code.coding` (628)<br>`hasil_pemeriksaan_lpa_line_probe_assay_lini_1_h` → `Observation.component.code.coding` (634)<br>`tanggal_hasil_pemeriksaan_lpa_lini_1` → `Observation.effectiveDateTime` (643) |
| 37 | 648–659 | DiagnosticReport | X099380 | Line Probe Assay (LPA) Lini 1 | – |
| 38 | 662–671 | ServiceRequest | X099381 | Line Probe Assay (LPA) Lini 2 | – |
| 39 | 673–680 | Specimen | 119334006 | Sputum specimen | – |
| 40 | 682–734 | Observation | X099381 | Line Probe Assay (LPA) Lini 2 | `hasil_pemeriksaan_lpa_line_probe_assay_lini_2_invalid` → `Observation.valueCodeableConcept.coding` (685)<br>`hasil_pemeriksaan_lpa_line_probe_assay_lini_2_mtb` → `Observation.component.code.coding` (688)<br>`hasil_pemeriksaan_lpa_line_probe_assay_lini_2_lfx` → `Observation.component.code.coding` (692)<br>`hasil_pemeriksaan_lpa_line_probe_assay_lini_2_mfx` → `Observation.component.code.coding` (698)<br>`hasil_pemeriksaan_lpa_line_probe_assay_lini_2_mfx_dt` → `Observation.component.code.coding` (704)<br>`hasil_pemeriksaan_lpa_line_probe_assay_lini_2_km` → `Observation.component.code.coding` (710)<br>`hasil_pemeriksaan_lpa_line_probe_assay_lini_2_amk` → `Observation.component.code.coding` (716)<br>`hasil_pemeriksaan_lpa_line_probe_assay_lini_2_cm` → `Observation.component.code.coding` (722)<br>`tanggal_hasil_pemeriksaan_lpa_lini_2` → `Observation.effectiveDateTime` (731) |
| 41 | 736–747 | DiagnosticReport | X099381 | Line Probe Assay (LPA) Lini 2 | – |
| 42 | 750–759 | ServiceRequest | X099388 | Biakan TB | – |
| 43 | 761–768 | Specimen | 119334006 | Sputum specimen | – |
| 44 | 770–787 | Observation | X099388 | Biakan TB | `hasil_pemeriksaan_biakan` → `Observation.valueCodeableConcept.coding` (773)<br>`tanggal_hasil_pemeriksaan_biakan` → `Observation.effectiveDateTime` (784) |
| 45 | 789–800 | DiagnosticReport | X099388 | Biakan TB | – |
| 46 | 803–812 | ServiceRequest | X099383 | Pemeriksaan Paket Standar Kepekaan | – |
| 47 | 814–821 | Specimen | 119334006 | Sputum specimen | – |
| 48 | 823–890 | Observation | X099383 | Pemeriksaan Paket Standar Kepekaan | `hasil_pemeriksaan_paket_standar_uji_kepekaan_h_dosis_tinggi` → `Observation.component.code.coding` (828)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_h` → `Observation.component.code.coding` (834)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_km` → `Observation.component.code.coding` (840)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_cm` → `Observation.component.code.coding` (846)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_lfx` → `Observation.component.code.coding` (852)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_mfx_dosis_tinggi` → `Observation.component.code.coding` (858)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_mfx` → `Observation.component.code.coding` (864)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan` → `Observation.component.code.coding` (870)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_1` → `Observation.component.code.coding` (872)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_2` → `Observation.component.code.coding` (874)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_3` → `Observation.component.code.coding` (876)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_4` → `Observation.component.code.coding` (878)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_5` → `Observation.component.code.coding` (880)<br>`tanggal_hasil_pemeriksaan_uji_kepekaan` → `Observation.effectiveDateTime` (887) |
| 49 | 892–903 | DiagnosticReport | X099383 | Pemeriksaan Paket Standar Kepekaan | – |
| 50 | 906–917 | Observation | 106229004 | Qualifier for type of diagnosis | `tipe_diagnosis` → `Observation.valueCodeableConcept.coding` (909) |
| 51 | 920–946 | CarePlan | – | – | `tindak_lanjut` → `CarePlan.status` (920)<br>`tempat_pengobatan_dirujuk_ke_nama_fasyankes` → `CarePlan.activity.detail.performer.reference` (934) 🔎 lookup master data<br>`tempat_pengobatan_tidak_dirujuk` → `CarePlan.activity.detail.performer.reference` (935) 🔎 lookup master data<br>`tanggal_mulai_pengobatan_tbc_tglblnthn` → `CarePlan.activity.detail.scheduledPeriod.start` (937)<br>`tindak_lanjut_penambahan_resistansi` → `CarePlan.note.text` (945) |
| 52 | 948–959 | Observation | 365866002 | Finding of human immunodeficiency virus status | `hasil_tes_hiv` → `Observation.valueCodeableConcept.coding` (951)<br>`tanggal_tes_hiv` → `Observation.issued` (957) |
| 53 | 961–971 | Procedure | SP000046 | Terapi Antiretroviral (ART) | `art` → `Procedure.category.coding` (961) |
| 54 | 973–984 | Observation | SP000047 | Hasil Tes Diabetes Melitus | `hasil_tes_dm` → `Observation.valueCodeableConcept.coding` (976) |

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
| Encounter | 1 |
| QuestionnaireResponse | 1 |
| CarePlan | 1 |
| **Total** | **54** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 31 | EpisodeOfCare | `EpisodeOfCare.type.coding` | TB-SO | Tuberkulosis Sensitif Obat | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 2 | 32 | EpisodeOfCare | `EpisodeOfCare.type.coding` | TB-RO | Tuberkulosis Resisten Obat | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 3 | 42 | EpisodeOfCare | `EpisodeOfCare.type.coding` | TB-SO | Tuberkulosis Sensitif Obat | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 4 | 43 | EpisodeOfCare | `EpisodeOfCare.type.coding` | TB-RO | Tuberkulosis Resisten Obat | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 5 | 57 | EpisodeOfCare | `EpisodeOfCare.type.coding` | TB-SO | Tuberkulosis Sensitif Obat | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 6 | 58 | EpisodeOfCare | `EpisodeOfCare.type.coding` | TB-RO | Tuberkulosis Resisten Obat | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 7 | 72 | Encounter | `Encounter.hospitalization.admitSource.coding` | EHA000001 | Kader/ Komunitas | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 8 | 73 | Encounter | `Encounter.hospitalization.admitSource.coding` | EHA000002 | Datang sendiri | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 9 | 74 | Encounter | `Encounter.hospitalization.admitSource.coding` | EHA000003 | Kegiatan ACF | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 10 | 75 | Encounter | `Encounter.hospitalization.admitSource.coding` | 257622000 | Healthcare facility | http://snomed.info/sct |
| 11 | 76 | Encounter | `Encounter.hospitalization.admitSource.coding` | EHA000004 | Skrining TBC DM | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 12 | 77 | Encounter | `Encounter.hospitalization.admitSource.coding` | EHA000005 | Pemadanan Data BPJS | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 13 | 112 | Condition | `Condition.code.coding` | Z03.0 | Observation for suspected tuberculosis | http://hl7.org/fhir/sid/icd-10 |
| 14 | 120 | Condition | `Condition.code.coding` | A15.0 | Tuberculosis of lung, confirmed by sputum microscopy with or without culture | http://hl7.org/fhir/sid/icd-10 |
| 15 | 121 | Condition | `Condition.code.coding` | A16.2 | Tuberculosis of lung, without mention of bacteriological or histological confirmation | http://hl7.org/fhir/sid/icd-10 |
| 16 | 130 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 17 | 155 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | QRI000001 | Terduga TBC SO | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 18 | 156 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | QRI000002 | Terduga TBC RO | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 19 | 159 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | new | Kasus Baru | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 20 | 160 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | relapse | Kasus Kambuh | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 21 | 161 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure-cat1 | Kasus Pengobatan Setelah Gagal Kategori 1 | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 22 | 162 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure-cat2 | Kasus Pengobatan Setelah Gagal Kategori 2 | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 23 | 163 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | loss-to-follow-up | Kasus Setelah Loss To Follow Up | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 24 | 164 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure-2line | Kasus Pengobatan Setelah Gagal lini 2 | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 25 | 165 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | not-eval | Pernah diobati tidak diketahui hasilnya | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 26 | 166 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | unknown | Kasus dengan riwayat pengobatan tidak diketahui | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 27 | 167 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | other | Kasus lain-lain | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 28 | 168 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure | Kasus Pengobatan Setelah Gagal | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 29 | 171 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure-cat2 | Kasus Pengobatan Setelah Gagal Kategori 2 | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 30 | 172 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | treatment-non-conversion-2 | Pasien TB pengobatan kategori 2 yang tidak konversi setelah 3 bulan pengobatan | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 31 | 173 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | non-standard-treatment | Pasien TB yang mempunyai riwayat pengobatan TB yang tidak standar | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 32 | 174 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure-cat1 | Kasus Pengobatan Setelah Gagal Kategori 1 | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 33 | 175 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | treatment-non-conversion-1 | Pasien TB pengobatan kategori 1 yang tidak konversi | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 34 | 176 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | relapse | Kasus Baru | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 35 | 177 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | loss-to-follow-up | Kasus Setelah Loss To Follow Up | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 36 | 178 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | history-of-close-contact with-TB-DR | Terduga TB yang mempunyai riwayat kontak erat dengan pasien TB RO | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 37 | 179 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | co-infected-TBHIV | Pasien ko-infeksi TB-HIV yang tidak respons secara klinis maupun bakteriologis terhadap pemberian OAT | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 38 | 180 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure-2line | Kasus Pengobatan Setelah Gagal lini 2 | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 39 | 181 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TB-DR-relapse | Pasien TB RO kasus kambuh | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 40 | 182 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TB-DR-returns | Pasien TB RO yang kembali setelah putus berobat | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 41 | 185 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 154283005 | Pulmonary tuberculosis | http://snomed.info/sct |
| 42 | 186 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 423997002 | Tuberculosis, extrapulmonary | http://snomed.info/sct |
| 43 | 191 | Observation | `Observation.code.coding` | OC000191 | Jumlah Skoring TBC Anak | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 44 | 207 | ServiceRequest | `ServiceRequest.code.coding` | 24648-8 | XR Chest PA upright | http://loinc.org |
| 45 | 216 | Observation | `Observation.code.coding` | 24648-8 | XR Chest PA upright | http://loinc.org |
| 46 | 217 | Observation | `Observation.valueCodeableConcept.coding` | 707307002 | Tuberculosis screening chest X-ray abnormal | http://snomed.info/sct |
| 47 | 218 | Observation | `Observation.valueCodeableConcept.coding` | 707308007 | Tuberculosis screening chest X-ray normal | http://snomed.info/sct |
| 48 | 230 | DiagnosticReport | `DiagnosticReport.code.coding` | 24648-8 | XR Chest PA upright | http://loinc.org |
| 49 | 241 | Procedure | `Procedure.code.coding` | 424489006 | Mantoux test | http://snomed.info/sct |
| 50 | 243 | Procedure | `Procedure.code.coding` | 35140007 | Interferon gamma assay | http://snomed.info/sct |
| 51 | 245 | Procedure | `Procedure.code.coding` | 424489006 | Mantoux test | http://snomed.info/sct |
| 52 | 247 | Procedure | `Procedure.code.coding` | 35140007 | Interferon gamma assay | http://snomed.info/sct |
| 53 | 259 | Observation | `Observation.code.coding` | 23539-0 | Tuberculosis reaction wheal [Diameter] --3 days post dose mammalian tuberculin intradermal | http://loinc.org |
| 54 | 260 | Observation | `Observation.valueCodeableConcept.coding` | 268376005 | Mantoux: positive | http://snomed.info/sct |
| 55 | 261 | Observation | `Observation.valueCodeableConcept.coding` | 268375009 | Mantoux: negative | http://snomed.info/sct |
| 56 | 262 | Observation | `Observation.code.coding` | 71773-6 | Mycobacterium tuberculosis stimulated gamma interferon [Interpretation] in Blood Qualitative | http://loinc.org |
| 57 | 263 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 58 | 264 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 59 | 265 | Observation | `Observation.code.coding` | 23539-0 | Tuberculosis reaction wheal [Diameter] --3 days post dose mammalian tuberculin intradermal | http://loinc.org |
| 60 | 267 | Observation | `Observation.code.coding` | 71773-6 | Mycobacterium tuberculosis stimulated gamma interferon [Interpretation] in Blood Qualitative | http://loinc.org |
| 61 | 280 | Observation | `Observation.code.coding` | 55277-8 | HIV status | http://loinc.org |
| 62 | 281 | Observation | `Observation.valueCodeableConcept.coding` | 10828004 | Positive | http://snomed.info/sct |
| 63 | 282 | Observation | `Observation.valueCodeableConcept.coding` | 260385009 | Negative | http://snomed.info/sct |
| 64 | 283 | Observation | `Observation.valueCodeableConcept.coding` | 261665006 | Unknown | http://snomed.info/sct |
| 65 | 295 | Observation | `Observation.code.coding` | 33248-6 | Diabetes status | http://loinc.org |
| 66 | 296 | Observation | `Observation.valueCodeableConcept.coding` | 10828004 | Positive | http://snomed.info/sct |
| 67 | 297 | Observation | `Observation.valueCodeableConcept.coding` | 260385009 | Negative | http://snomed.info/sct |
| 68 | 298 | Observation | `Observation.valueCodeableConcept.coding` | 261665006 | Unknown | http://snomed.info/sct |
| 69 | 313 | ServiceRequest | `ServiceRequest.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 70 | 323 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 71 | 334 | Observation | `Observation.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 72 | 335 | Observation | `Observation.valueCodeableConcept.coding` | 260385009 | Negative | http://snomed.info/sct |
| 73 | 336 | Observation | `Observation.valueCodeableConcept.coding` | LA11841-6 | 1+ | http://loinc.org |
| 74 | 337 | Observation | `Observation.valueCodeableConcept.coding` | LA11842-4 | 2+ | http://loinc.org |
| 75 | 338 | Observation | `Observation.valueCodeableConcept.coding` | LA11843-2 | 3+ | http://loinc.org |
| 76 | 352 | DiagnosticReport | `DiagnosticReport.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 77 | 368 | ServiceRequest | `ServiceRequest.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 78 | 378 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 79 | 389 | Observation | `Observation.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 80 | 390 | Observation | `Observation.valueCodeableConcept.coding` | 260385009 | Negative | http://snomed.info/sct |
| 81 | 391 | Observation | `Observation.valueCodeableConcept.coding` | LA11841-6 | 1+ | http://loinc.org |
| 82 | 392 | Observation | `Observation.valueCodeableConcept.coding` | LA11842-4 | 2+ | http://loinc.org |
| 83 | 393 | Observation | `Observation.valueCodeableConcept.coding` | LA11843-2 | 3+ | http://loinc.org |
| 84 | 407 | DiagnosticReport | `DiagnosticReport.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 85 | 423 | ServiceRequest | `ServiceRequest.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 86 | 424 | ServiceRequest | `ServiceRequest.code.coding` | 89371-9 | MTB complex DNA and rpoB RIF resistance mutation panel [Presence] | http://loinc.org |
| 87 | 425 | ServiceRequest | `ServiceRequest.code.coding` | X099379 | Pemeriksaan TCM XDR | http://terminology.kemkes.go.id/CodeSystem/examination |
| 88 | 426 | ServiceRequest | `ServiceRequest.code.coding` | X099380 | Line Probe Assay (LPA) Lini 1 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 89 | 427 | ServiceRequest | `ServiceRequest.code.coding` | X099381 | Line Probe Assay (LPA) Lini 2 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 90 | 428 | ServiceRequest | `ServiceRequest.code.coding` | X099388 | Biakan TB | http://terminology.kemkes.go.id/CodeSystem/examination |
| 91 | 429 | ServiceRequest | `ServiceRequest.code.coding` | X099383 | Pemeriksaan Paket Standar Kepekaan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 92 | 430 | ServiceRequest | `ServiceRequest.code.coding` | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 93 | 431 | ServiceRequest | `ServiceRequest.code.coding` | MK099927 | Pemeriksaan PCR Open System | http://terminology.kemkes.go.id/CodeSystem/examination |
| 94 | 439 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 95 | 449 | Observation | `Observation.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 96 | 450 | Observation | `Observation.code.coding` | 89371-9 | MTB complex DNA and rpoB RIF resistance mutation panel [Presence] | http://loinc.org |
| 97 | 451 | Observation | `Observation.code.coding` | X099379 | Pemeriksaan TCM XDR | http://terminology.kemkes.go.id/CodeSystem/examination |
| 98 | 452 | Observation | `Observation.code.coding` | X099380 | Line Probe Assay (LPA) Lini 1 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 99 | 453 | Observation | `Observation.code.coding` | X099381 | Line Probe Assay (LPA) Lini 2 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 100 | 454 | Observation | `Observation.code.coding` | X099388 | Biakan TB | http://terminology.kemkes.go.id/CodeSystem/examination |
| 101 | 455 | Observation | `Observation.code.coding` | X099383 | Pemeriksaan Paket Standar Kepekaan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 102 | 456 | Observation | `Observation.code.coding` | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 103 | 457 | Observation | `Observation.code.coding` | MK099927 | Pemeriksaan PCR Open System | http://terminology.kemkes.go.id/CodeSystem/examination |
| 104 | 458 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 105 | 459 | Observation | `Observation.valueCodeableConcept.coding` | X099770 | Rifampisin sensitive | http://terminology.kemkes.go.id/CodeSystem/examination |
| 106 | 460 | Observation | `Observation.valueCodeableConcept.coding` | X099771 | Rifampisin resistan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 107 | 461 | Observation | `Observation.valueCodeableConcept.coding` | X099772 | Rifampisin indeterminate | http://terminology.kemkes.go.id/CodeSystem/examination |
| 108 | 477 | DiagnosticReport | `DiagnosticReport.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 109 | 479 | DiagnosticReport | `DiagnosticReport.code.coding` | 89371-9 | MTB complex DNA and rpoB RIF resistance mutation panel [Presence] | http://loinc.org |
| 110 | 481 | DiagnosticReport | `DiagnosticReport.code.coding` | X099379 | Pemeriksaan TCM XDR | http://terminology.kemkes.go.id/CodeSystem/examination |
| 111 | 483 | DiagnosticReport | `DiagnosticReport.code.coding` | X099380 | Line Probe Assay (LPA) Lini 1 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 112 | 485 | DiagnosticReport | `DiagnosticReport.code.coding` | X099381 | Line Probe Assay (LPA) Lini 2 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 113 | 487 | DiagnosticReport | `DiagnosticReport.code.coding` | X099388 | Biakan TB | http://terminology.kemkes.go.id/CodeSystem/examination |
| 114 | 489 | DiagnosticReport | `DiagnosticReport.code.coding` | X099383 | Pemeriksaan Paket Standar Kepekaan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 115 | 491 | DiagnosticReport | `DiagnosticReport.code.coding` | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 116 | 493 | DiagnosticReport | `DiagnosticReport.code.coding` | MK099927 | Pemeriksaan PCR Open System | http://terminology.kemkes.go.id/CodeSystem/examination |
| 117 | 509 | ServiceRequest | `ServiceRequest.code.coding` | X099379 | Pemeriksaan TCM XDR | http://terminology.kemkes.go.id/CodeSystem/examination |
| 118 | 517 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 119 | 527 | Observation | `Observation.code.coding` | X099379 | Pemeriksaan TCM XDR | http://terminology.kemkes.go.id/CodeSystem/examination |
| 120 | 528 | Observation | `Observation.valueCodeableConcept.coding` | X099781 | Hasil Valid | http://terminology.kemkes.go.id/CodeSystem/examination |
| 121 | 533 | Observation | `Observation.component.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 122 | 534 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 123 | 535 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 124 | 537 | Observation | `Observation.component.code.coding` | X099391 | H Dosis Rendah (Low) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 125 | 538 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 126 | 539 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 127 | 540 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 128 | 542 | Observation | `Observation.component.code.coding` | 89488-1 | Isoniazid [Susceptibility] by Genotype method | http://loinc.org |
| 129 | 543 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 130 | 544 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 131 | 545 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 132 | 547 | Observation | `Observation.component.code.coding` | 96110-2 | Ethionamide [Susceptibility] by Genotype method | http://loinc.org |
| 133 | 548 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 134 | 549 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 135 | 551 | Observation | `Observation.component.code.coding` | X099392 | FQ Dosis Rendah (Low) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 136 | 552 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 137 | 553 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 138 | 554 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 139 | 556 | Observation | `Observation.component.code.coding` | 89487-3 | Fluoroquinolone [Susceptibility] by Genotype method | http://loinc.org |
| 140 | 557 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 141 | 558 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 142 | 559 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 143 | 561 | Observation | `Observation.component.code.coding` | 89484-0 | Amikacin [Susceptibility] by Genotype method | http://loinc.org |
| 144 | 562 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 145 | 563 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 146 | 564 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 147 | 566 | Observation | `Observation.component.code.coding` | 89482-4 | Kanamycin [Susceptibility] by Genotype method | http://loinc.org |
| 148 | 567 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 149 | 568 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 150 | 569 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 151 | 571 | Observation | `Observation.component.code.coding` | 89483-2 | Capreomycin [Susceptibility] by Genotype method | http://loinc.org |
| 152 | 572 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 153 | 573 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 154 | 574 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 155 | 586 | DiagnosticReport | `DiagnosticReport.code.coding` | X099379 | Pemeriksaan TCM XDR | http://terminology.kemkes.go.id/CodeSystem/examination |
| 156 | 602 | ServiceRequest | `ServiceRequest.code.coding` | X099380 | Line Probe Assay (LPA) Lini 1 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 157 | 610 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 158 | 620 | Observation | `Observation.code.coding` | X099380 | Line Probe Assay (LPA) Lini 1 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 159 | 621 | Observation | `Observation.valueCodeableConcept.coding` | X099781 | Hasil Valid | http://terminology.kemkes.go.id/CodeSystem/examination |
| 160 | 624 | Observation | `Observation.component.code.coding` | 13956-8 | Mycobacterium tuberculosis DNA [Presence] in Specimen by NAA with probe detection | http://loinc.org |
| 161 | 625 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 162 | 626 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 163 | 628 | Observation | `Observation.component.code.coding` | 89489-9 | rifAMPin [Susceptibility] by Genotype method | http://loinc.org |
| 164 | 629 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 165 | 630 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 166 | 631 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 167 | 632 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 168 | 634 | Observation | `Observation.component.code.coding` | 89488-1 | Isoniazid [Susceptibility] by Genotype method | http://loinc.org |
| 169 | 635 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 170 | 636 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 171 | 637 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 172 | 638 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 173 | 650 | DiagnosticReport | `DiagnosticReport.code.coding` | X099380 | Line Probe Assay (LPA) Lini 1 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 174 | 666 | ServiceRequest | `ServiceRequest.code.coding` | X099381 | Line Probe Assay (LPA) Lini 2 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 175 | 674 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 176 | 684 | Observation | `Observation.code.coding` | X099381 | Line Probe Assay (LPA) Lini 2 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 177 | 685 | Observation | `Observation.valueCodeableConcept.coding` | X099781 | Hasil Valid | http://terminology.kemkes.go.id/CodeSystem/examination |
| 178 | 688 | Observation | `Observation.component.code.coding` | 13956-8 | Mycobacterium tuberculosis DNA [Presence] in Specimen by NAA with probe detection | http://loinc.org |
| 179 | 689 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 180 | 690 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 181 | 692 | Observation | `Observation.component.code.coding` | 20629-2 | levoFLOXacin [Susceptibility] | http://loinc.org |
| 182 | 693 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 183 | 694 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 184 | 695 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 185 | 696 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 186 | 698 | Observation | `Observation.component.code.coding` | 96112-8 | Moxifloxacin [Susceptibility] by Genotype method | http://loinc.org |
| 187 | 699 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 188 | 700 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 189 | 701 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 190 | 702 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 191 | 704 | Observation | `Observation.component.code.coding` | X099775 | Moxifloxacin DT (Mfx DT) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 192 | 705 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 193 | 706 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 194 | 707 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 195 | 708 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 196 | 710 | Observation | `Observation.component.code.coding` | 89482-4 | Kanamycin [Susceptibility] by Genotype method | http://loinc.org |
| 197 | 711 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 198 | 712 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 199 | 713 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 200 | 714 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 201 | 716 | Observation | `Observation.component.code.coding` | 89484-0 | Amikacin [Susceptibility] by Genotype method | http://loinc.org |
| 202 | 717 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 203 | 718 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 204 | 719 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 205 | 720 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 206 | 722 | Observation | `Observation.component.code.coding` | 89483-2 | Capreomycin [Susceptibility] by Genotype method | http://loinc.org |
| 207 | 723 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 208 | 724 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 209 | 725 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 210 | 726 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 211 | 738 | DiagnosticReport | `DiagnosticReport.code.coding` | X099381 | Line Probe Assay (LPA) Lini 2 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 212 | 754 | ServiceRequest | `ServiceRequest.code.coding` | X099388 | Biakan TB | http://terminology.kemkes.go.id/CodeSystem/examination |
| 213 | 762 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 214 | 772 | Observation | `Observation.code.coding` | X099388 | Biakan TB | http://terminology.kemkes.go.id/CodeSystem/examination |
| 215 | 773 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 216 | 774 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 217 | 775 | Observation | `Observation.valueCodeableConcept.coding` | LA11841-6 | + | http://loinc.org |
| 218 | 776 | Observation | `Observation.valueCodeableConcept.coding` | LA11842-4 | ++ | http://loinc.org |
| 219 | 777 | Observation | `Observation.valueCodeableConcept.coding` | LA11843-2 | +++ | http://loinc.org |
| 220 | 778 | Observation | `Observation.valueCodeableConcept.coding` | 110379001 | Mycobacterium, non-tuberculosis (organism) | http://snomed.info/sct |
| 221 | 791 | DiagnosticReport | `DiagnosticReport.code.coding` | X099388 | Biakan TB | http://terminology.kemkes.go.id/CodeSystem/examination |
| 222 | 807 | ServiceRequest | `ServiceRequest.code.coding` | X099383 | Pemeriksaan Paket Standar Kepekaan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 223 | 815 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 224 | 825 | Observation | `Observation.code.coding` | X099383 | Pemeriksaan Paket Standar Kepekaan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 225 | 828 | Observation | `Observation.component.code.coding` | X099776 | H High Dosage [Susceptibility] by Method for Slow-growing mycobacteria | http://terminology.kemkes.go.id/CodeSystem/examination |
| 226 | 829 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 227 | 830 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 228 | 831 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 229 | 834 | Observation | `Observation.component.code.coding` | 20383-6 | Isoniazid [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 230 | 835 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 231 | 836 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 232 | 837 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 233 | 840 | Observation | `Observation.component.code.coding` | 23609-1 | Kanamycin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 234 | 841 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 235 | 842 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 236 | 843 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 237 | 846 | Observation | `Observation.component.code.coding` | 23607-5 | Capreomycin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 238 | 847 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 239 | 848 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 240 | 849 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 241 | 852 | Observation | `Observation.component.code.coding` | 53716-7 | levoFLOXacin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 242 | 853 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 243 | 854 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 244 | 855 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 245 | 858 | Observation | `Observation.component.code.coding` | X099778 | Moxifloxacin High Dosage [Susceptibility] by Method for Slow-growing mycobacteria | http://terminology.kemkes.go.id/CodeSystem/examination |
| 246 | 859 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 247 | 860 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 248 | 861 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 249 | 864 | Observation | `Observation.component.code.coding` | 41502-6 | Moxifloxacin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 250 | 865 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 251 | 866 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 252 | 867 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 253 | 870 | Observation | `Observation.component.code.coding` | SP000472 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya | http://terminology.kemkes.go.id/sp |
| 254 | 872 | Observation | `Observation.component.code.coding` | SP000473 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 1 | http://terminology.kemkes.go.id/sp |
| 255 | 874 | Observation | `Observation.component.code.coding` | SP000474 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 2 | http://terminology.kemkes.go.id/sp |
| 256 | 876 | Observation | `Observation.component.code.coding` | SP000475 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 3 | http://terminology.kemkes.go.id/sp |
| 257 | 878 | Observation | `Observation.component.code.coding` | SP000476 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 4 | http://terminology.kemkes.go.id/sp |
| 258 | 880 | Observation | `Observation.component.code.coding` | SP000477 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 5 | http://terminology.kemkes.go.id/sp |
| 259 | 894 | DiagnosticReport | `DiagnosticReport.code.coding` | X099383 | Pemeriksaan Paket Standar Kepekaan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 260 | 908 | Observation | `Observation.code.coding` | 106229004 | Qualifier for type of diagnosis | http://snomed.info/sct |
| 261 | 909 | Observation | `Observation.valueCodeableConcept.coding` | tb-bac | Terkonfirmasi bakteriologis | http://terminology.kemkes.go.id/CodeSystem/tb-case-definition |
| 262 | 910 | Observation | `Observation.valueCodeableConcept.coding` | tb-clin | Terdiagnosis klinis | http://terminology.kemkes.go.id/CodeSystem/tb-case-definition |
| 263 | 924 | CarePlan | `CarePlan.activity.detail.code.coding` | TK000022 | Akan diobati/dirujuk | http://terminology.kemkes.go.id |
| 264 | 925 | CarePlan | `CarePlan.activity.detail.code.coding` | 699618001 | Administration of prophylactic antituberculosis agent | http://snomed.info/sct |
| 265 | 926 | CarePlan | `CarePlan.activity.detail.code.coding` | 266714009 | Previous treatment continue | http://snomed.info/sct |
| 266 | 927 | CarePlan | `CarePlan.activity.detail.code.coding` | SP001136 | Belum Mulai Pengobatan | http://terminology.kemkes.go.id/sp |
| 267 | 930 | CarePlan | `CarePlan.activity.detail.statusReason.coding` | 406149000 | Medication declined | http://snomed.info/sct |
| 268 | 931 | CarePlan | `CarePlan.activity.detail.statusReason.coding` | 419099009 | Dead | http://snomed.info/sct |
| 269 | 932 | CarePlan | `CarePlan.activity.detail.statusReason.coding` | 399307001 | Lost to follow-up | http://snomed.info/sct |
| 270 | 950 | Observation | `Observation.code.coding` | 365866002 | Finding of human immunodeficiency virus status | http://snomed.info/sct |
| 271 | 951 | Observation | `Observation.valueCodeableConcept.coding` | 165816005 | Human immunodeficiency virus detected | http://snomed.info/sct |
| 272 | 952 | Observation | `Observation.valueCodeableConcept.coding` | 165815009 | Human immunodeficiency virus not detected | http://snomed.info/sct |
| 273 | 962 | Procedure | `Procedure.code.coding` | SP000046 | Terapi Antiretroviral (ART) | http://terminology.kemkes.go.id/sp |
| 274 | 975 | Observation | `Observation.code.coding` | SP000047 | Hasil Tes Diabetes Melitus | http://terminology.kemkes.go.id/sp |
| 275 | 976 | Observation | `Observation.valueCodeableConcept.coding` | 10828004 | Positive | http://snomed.info/sct |
| 276 | 977 | Observation | `Observation.valueCodeableConcept.coding` | 260385009 | Negative | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah | Code |
|---|---|---|
| http://loinc.org | 130 | 24648-8, 24648-8, 24648-8, 23539-0, 71773-6, LA6576-8, LA6577-6, 23539-0, 71773-6, 55277-8, 33248-6, 11545-1, 11545-1, LA11841-6, LA11842-4, LA11843-2, 11545-1, 11545-1, 11545-1, LA11841-6, LA11842-4, LA11843-2, 11545-1, 11545-1, 89371-9, 11545-1, 89371-9, LA6577-6, 11545-1, 89371-9, 88874-3, LA11882-0, LA11883-8, LA11882-0, LA11883-8, LA11884-6, 89488-1, LA11882-0, LA11883-8, LA11884-6, 96110-2, LA11882-0, LA11883-8, LA11882-0, LA11883-8, LA11884-6, 89487-3, LA11882-0, LA11883-8, LA11884-6, 89484-0, LA11882-0, LA11883-8, LA11884-6, 89482-4, LA11882-0, LA11883-8, LA11884-6, 89483-2, LA11882-0, LA11883-8, LA11884-6, 13956-8, LA6576-8, LA6577-6, 89489-9, LA11882-0, LA11883-8, LA11884-6, 89488-1, LA11882-0, LA11883-8, LA11884-6, 13956-8, LA6576-8, LA6577-6, 20629-2, LA11882-0, LA11883-8, LA11884-6, 96112-8, LA11882-0, LA11883-8, LA11884-6, LA11882-0, LA11883-8, LA11884-6, 89482-4, LA11882-0, LA11883-8, LA11884-6, 89484-0, LA11882-0, LA11883-8, LA11884-6, 89483-2, LA11882-0, LA11883-8, LA11884-6, LA6577-6, LA6576-8, LA11841-6, LA11842-4, LA11843-2, LA24225-7, LA6676-6, LA16550-8, 20383-6, LA24225-7, LA6676-6, LA16550-8, 23609-1, LA24225-7, LA6676-6, LA16550-8, 23607-5, LA24225-7, LA6676-6, LA16550-8, 53716-7, LA24225-7, LA6676-6, LA16550-8, LA24225-7, LA6676-6, LA16550-8, 41502-6, LA24225-7, LA6676-6, LA16550-8 |
| http://terminology.kemkes.go.id/CodeSystem/examination | 55 | X099379, X099380, X099381, X099388, X099383, MK099926, MK099927, X099379, X099380, X099381, X099388, X099383, MK099926, MK099927, X099770, X099771, X099772, X099379, X099380, X099381, X099388, X099383, MK099926, MK099927, X099379, X099379, X099781, X099391, X099392, X099379, X099380, X099380, X099781, X099774, X099774, X099380, X099381, X099381, X099781, X099774, X099774, X099775, X099774, X099774, X099774, X099774, X099381, X099388, X099388, X099388, X099383, X099383, X099776, X099778, X099383 |
| http://snomed.info/sct | 40 | 257622000, 424144002, 154283005, 423997002, 707307002, 707308007, 424489006, 35140007, 424489006, 35140007, 268376005, 268375009, 10828004, 260385009, 261665006, 10828004, 260385009, 261665006, 119334006, 260385009, 119334006, 260385009, 119334006, 119334006, 119334006, 119334006, 119334006, 110379001, 119334006, 106229004, 699618001, 266714009, 406149000, 419099009, 399307001, 365866002, 165816005, 165815009, 10828004, 260385009 |
| http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment | 22 | new, relapse, failure-cat1, failure-cat2, loss-to-follow-up, failure-2line, not-eval, unknown, other, failure, failure-cat2, treatment-non-conversion-2, non-standard-treatment, failure-cat1, treatment-non-conversion-1, relapse, loss-to-follow-up, history-of-close-contact with-TB-DR, co-infected-TBHIV, failure-2line, TB-DR-relapse, TB-DR-returns |
| http://terminology.kemkes.go.id/sp | 9 | SP000472, SP000473, SP000474, SP000475, SP000476, SP000477, SP001136, SP000046, SP000047 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 8 | EHA000001, EHA000002, EHA000003, EHA000004, EHA000005, QRI000001, QRI000002, OC000191 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 6 | TB-SO, TB-RO, TB-SO, TB-RO, TB-SO, TB-RO |
| http://hl7.org/fhir/sid/icd-10 | 3 | Z03.0, A15.0, A16.2 |
| http://terminology.kemkes.go.id/CodeSystem/tb-case-definition | 2 | tb-bac, tb-clin |
| http://terminology.kemkes.go.id | 1 | TK000022 |
| **Total** | **276** | |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
