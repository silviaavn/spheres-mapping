# Output Form: SITB TB 03 RO

Sumber: `mapping/phdt-data-dictionary-sitb-tb03-ro.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 29 |
| Code (`jumlah code` = 1) | 357 |
| Code unik (code + CodeSystem) | 242 |
| Variabel BQ (unik) | 140 |
| Variabel di Excel export | 144 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–27 | Patient | – | – | `no_rekam_medis` → `Patient.identifier.value` (5)<br>`nomor_identitas_kependudukan_nik` → `Patient.identifier.value` (8)<br>`nama_lengkap_pasien` → `Patient.name.text` (9)<br>`jenis_kelamin` → `Patient.gender` (10)<br>`alamat_lengkap_pasien_kabupatenkota` → `Patient.address.city` (12)<br>`alamat_lengkap_pasien_provinsi` → `Patient.address.extension.extension.valueCode` (16)<br>`alamat_lengkap_pasien_kabupatenkota` → `Patient.address.extension.extension.valueCode` (19)<br>`alamat_lengkap_pasien_kecamatan` → `Patient.address.extension.extension.valueCode` (22)<br>`alamat_lengkap_pasien_kelurahan` → `Patient.address.extension.extension.valueCode` (25)<br>`alamat_lengkap_pasien_alamat_lengkap` → `Patient.address.line` (26) |
| 2 | 29–50 | EpisodeOfCare | TB-RO | Tuberkulosis Resisten Obat | `nomor_register_sitb` → `EpisodeOfCare.identifier.value` (29)<br>`nomor_register_terduga` → `EpisodeOfCare.identifier.value` (31)<br>`nomor_register_pasien` → `EpisodeOfCare.identifier.value` (33)<br>`tgl_pengisian_data_dasar_terduga_tbc_ro` → `EpisodeOfCare.period.start` (36)<br>`nama_lengkap_pasien` → `EpisodeOfCare.patient.display` (49) |
| 3 | 52–56 | Coverage | – | – | `nomor_bpjs` → `Coverage.identifier.value` (56) |
| 4 | 58–97 | Encounter | – | – | `nomor_register_sitb` → `Encounter.identifier` (59)<br>`dirujuk_dikirim_oleh` → `Encounter.hospitalization.admitSource.coding` (61)<br>`nama_lengkap_pasien` → `Encounter.subject.display` (71)<br>`tgl_mulai_pengobatan` → `Encounter.period.start` (75)<br>`tgl_mulai_pengobatan` → `Encounter.period.end` (76)<br>`alamat_lengkap_faskes_nama_fasyankes` → `Encounter.location.display` (78)<br>`tgl_mulai_pengobatan` → `Encounter.statusHistory.period.start` (84)<br>`tgl_mulai_pengobatan` → `Encounter.statusHistory.period.end` (85)<br>`tgl_mulai_pengobatan` → `Encounter.statusHistory.period.start` (87)<br>`tgl_mulai_pengobatan` → `Encounter.statusHistory.period.end` (88)<br>`tgl_mulai_pengobatan` → `Encounter.statusHistory.period.start` (90)<br>`tgl_mulai_pengobatan` → `Encounter.statusHistory.period.end` (91)<br>`alamat_lengkap_faskes_kode_fasyankes` → `Encounter.serviceProvider.reference` (93) 🔎 lookup master data<br>`alamat_lengkap_faskes_jenis_fasyankes` → `Encounter.serviceProvider.reference` (94) 🔎 lookup master data<br>`alamat_lengkap_faskes_kepemilikan_fasyankes` → `Encounter.serviceProvider.reference` (95) 🔎 lookup master data<br>`alamat_lengkap_faskes_provinsi` → `Encounter.serviceProvider.reference` (96) 🔎 lookup master data<br>`alamat_lengkap_faskes_kabupatenkota` → `Encounter.serviceProvider.reference` (97) 🔎 lookup master data |
| 5 | 99–106 | Condition | A15.0 | Tuberculosis of lung, confirmed by sputum microscopy with or without culture | – |
| 6 | 108–119 | Observation | 424144002 | Current chronological age | `umur_tahun` → `Observation.valueQuantity.value` (111)<br>`nama_lengkap_pasien` → `Observation.subject.display` (114)<br>`tgl_mulai_pengobatan` → `Observation.effectiveDateTime` (116)<br>`nama_lengkap_pasien` → `Observation.issued` (117) |
| 7 | 121–154 | Observation | 85658-3 | Occupation [Type] | `pekerjaan_status` → `Observation.valueCodeableConcept.coding` (124)<br>`nama_lengkap_pasien` → `Observation.subject.display` (148)<br>`tgl_mulai_pengobatan` → `Observation.encounter.reference` (150)<br>`nama_lengkap_pasien` → `Observation.effectiveDateTime` (151) |
| 8 | 156–168 | Observation | 82810-3 | Pregnancy status | _Status Hamil_ → `Observation.status` (156, tanpa BQ)<br>`status_hamil` → `Observation.valueCodeableConcept.coding` (159)<br>`nama_lengkap_pasien` → `Observation.subject.display` (163)<br>`tgl_mulai_pengobatan` → `Observation.effectiveDateTime` (165)<br>`nama_lengkap_pasien` → `Observation.issued` (166) |
| 9 | 170–181 | Observation | 225368008 | Contact tracing | `dilakukan_pemeriksaan_kontak` → `Observation.valueBoolean` (173)<br>`nama_lengkap_pasien` → `Observation.subject.display` (176)<br>`tgl_mulai_pengobatan` → `Observation.effectiveDateTime` (178)<br>`nama_lengkap_pasien` → `Observation.issued` (179) |
| 10 | 184–228 | QuestionnaireResponse | – | – | `nama_lengkap_pasien` → `QuestionnaireResponse.subject.display` (187)<br>`tgl_pengisian_data_dasar_terduga_tbc_ro` → `QuestionnaireResponse.authoredOn` (189)<br>`klasifikasi_berdasarkan_riwayat_pengobatan_sebelumnya` → `QuestionnaireResponse.item.item.linkId` (199)<br>`riwayat_pengobatan_tbc_sebelumnya` → `QuestionnaireResponse.item.item.linkId` (211)<br>`klasifikasi_berdasarkan_lokasi_anatomi` → `QuestionnaireResponse.item.item.linkId` (225) |
| 11 | 230–242 | Observation | 33248-6 | Diabetes status | `riwayat_dm` → `Observation.valueCodeableConcept.coding` (233)<br>`nama_lengkap_pasien` → `Observation.subject.display` (237)<br>`tgl_mulai_pengobatan` → `Observation.effectiveDateTime` (239)<br>`tgl_mulai_pengobatan` → `Observation.issued` (240) |
| 12 | 244–256 | Observation | 55277-8 | HIV status | `status_hiv` → `Observation.valueCodeableConcept.coding` (247)<br>`nama_lengkap_pasien` → `Observation.subject.display` (251)<br>`tgl_mulai_pengobatan` → `Observation.effectiveDateTime` (253)<br>`tgl_mulai_pengobatan` → `Observation.issued` (254) |
| 13 | 258–273 | Procedure | 424489006 | Mantoux test | `dilakukan_pemeriksaan_tuberkulinigra` → `Procedure.category.coding` (258)<br>`nama_lengkap_pasien` → `Procedure.subject.display` (268)<br>`tgl_mulai_pengobatan` → `Procedure.performedPeriod.start` (270)<br>`tgl_mulai_pengobatan` → `Procedure.performedPeriod.end` (271) |
| 14 | 275–293 | Observation | 23539-0 | Tuberculosis reaction wheal [Diameter] --3 days post dose mammalian tuberculin intradermal | `hasil_pemeriksaan_tuberkulinigra` → `Observation.valueCodeableConcept.coding` (278)<br>`nama_lengkap_pasien` → `Observation.subject.display` (288)<br>`tgl_mulai_pengobatan` → `Observation.effectiveDateTime` (290)<br>`tgl_mulai_pengobatan` → `Observation.issued` (291) |
| 15 | 295–323 | Observation | 24648-8 | XR Chest PA upright | `hasil_foto_toraks` → `Observation.valueCodeableConcept.coding` (298)<br>`nama_lengkap_pasien` → `Observation.subject.display` (318)<br>`tgl_mulai_pengobatan` → `Observation.effectiveDateTime` (320)<br>`tgl_mulai_pengobatan` → `Observation.issued` (321) |
| 16 | 325–440 | CarePlan | – | – | `nama_lengkap_pasien` → `CarePlan.subject.display` (331)<br>`tgl_mulai_pengobatan` → `CarePlan.period.start` (333)<br>`hasil_akhir_pengobatan_tanggal_hhbbtttt` → `CarePlan.period.end` (334)<br>`nama_fasyankes_satelit_tbc_ro_lanjutan_pengobatan` → `CarePlan.contributor.reference` (338) 🔎 lookup master data<br>`paduan_oat` → `CarePlan.activity.detail.code.coding` (341)<br>`paduan_pengobatan` → `CarePlan.activity.detail.status` (351)<br>`paduan_pengobatan` → `CarePlan.activity.detail.productCodeableConcept.coding` (429)<br>`paduan_pengobatan` → `CarePlan.activity.detail.productCodeableConcept.coding` (430)<br>`paduan_pengobatan` → `CarePlan.activity.detail.productCodeableConcept.coding` (431)<br>`paduan_pengobatan` → `CarePlan.activity.detail.productCodeableConcept.coding` (432)<br>`paduan_pengobatan` → `CarePlan.activity.detail.productCodeableConcept.text` (433)<br>`hasil_akhir_pengobatan_hasil` → `CarePlan.activity.outcomeCodeableConcept.coding` (434)<br>`keterangan` → `CarePlan.note` (440) |
| 17 | 443–468 | Observation | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | `jenis_pemeriksaan_diagnosis` → `Observation.status` (443)<br>`hasil_pemeriksaan_diagnosis_tbc` → `Observation.valueCodeableConcept.coding` (454)<br>`nama_lengkap_pasien` → `Observation.subject.display` (463)<br>`tgl_mulai_pengobatan` → `Observation.effectiveDateTime` (465)<br>`tanggal_hasil_pemeriksaan_diagnosis_tbc` → `Observation.issued` (466) |
| 18 | 471–531 | Observation | X099379 | Pemeriksaan TCM XDR | `hasil_pemeriksaan_xpert_tcm_xdr_valid_invalid_no_result_error` → `Observation.valueCodeableConcept.coding` (474)<br>`hasil_pemeriksaan_xpert_tcm_xdr_mtb` → `Observation.component.code.coding` (479)<br>`hasil_pemeriksaan_xpert_tcm_xdr_h_dosis_rendah_low` → `Observation.component.code.coding` (486)<br>`hasil_pemeriksaan_xpert_tcm_xdr_h` → `Observation.component.code.coding` (491)<br>`hasil_pemeriksaan_xpert_tcm_xdr_eto` → `Observation.component.code.coding` (496)<br>`hasil_pemeriksaan_xpert_tcm_xdr_fq_dosis_rendah_low` → `Observation.component.code.coding` (500)<br>`hasil_pemeriksaan_xpert_tcm_xdr_fq` → `Observation.component.code.coding` (505)<br>`hasil_pemeriksaan_xpert_tcm_xdr_amk` → `Observation.component.code.coding` (510)<br>`hasil_pemeriksaan_xpert_tcm_xdr_km` → `Observation.component.code.coding` (515)<br>`hasil_pemeriksaan_xpert_tcm_xdr_cm` → `Observation.component.code.coding` (520)<br>`nama_lengkap_pasien` → `Observation.subject.display` (526)<br>`tgl_mulai_pengobatan` → `Observation.effectiveDateTime` (528)<br>`tanggal_hasil_pemeriksaan_tcmxdr` → `Observation.issued` (529) |
| 19 | 534–562 | Observation | X099380 | Line Probe Assay (LPA) Lini 1 | `hasil_pemeriksaan_lpa_line_probe_assay_lini_1_valid_invalid` → `Observation.valueCodeableConcept.coding` (537)<br>_MTB_ → `Observation.component.code.coding` (540, tanpa BQ)<br>`hasil_pemeriksaan_lpa_line_probe_assay_lini_1_mtb` → `Observation.component.valueCodeableConcept.coding` (541)<br>_R_ → `Observation.component.code.coding` (544, tanpa BQ)<br>`hasil_pemeriksaan_lpa_line_probe_assay_lini_1_r` → `Observation.component.valueCodeableConcept.coding` (545)<br>_H_ → `Observation.component.code.coding` (550, tanpa BQ)<br>`hasil_pemeriksaan_lpa_line_probe_assay_lini_1_h` → `Observation.component.valueCodeableConcept.coding` (551)<br>`nama_lengkap_pasien` → `Observation.subject.display` (557)<br>`tgl_mulai_pengobatan` → `Observation.effectiveDateTime` (559)<br>`tgl_mulai_pengobatan` → `Observation.issued` (560) |
| 20 | 564–616 | Observation | X099381 | Line Probe Assay (LPA) Lini 2 | `hasil_pemeriksaan_lpa_lini_2_valid_invalid` → `Observation.valueCodeableConcept.coding` (567)<br>`hasil_pemeriksaan_lpa_lini_2_mtb` → `Observation.component.code.coding` (570)<br>`hasil_pemeriksaan_lpa_lini_2_fq_lfx` → `Observation.component.code.coding` (574)<br>`hasil_pemeriksaan_lpa_lini_2_fq_mfx` → `Observation.component.code.coding` (580)<br>`hasil_pemeriksaan_lpa_lini_2_fq_mfx_dt` → `Observation.component.code.coding` (586)<br>`hasil_pemeriksaan_lpa_lini_2_slid_km` → `Observation.component.code.coding` (592)<br>`hasil_pemeriksaan_lpa_lini_2_slid_amk` → `Observation.component.code.coding` (598)<br>`hasil_pemeriksaan_lpa_lini_2_slid_cm` → `Observation.component.code.coding` (604)<br>`nama_lengkap_pasien` → `Observation.subject.display` (611)<br>`tgl_mulai_pengobatan` → `Observation.effectiveDateTime` (613)<br>`tgl_mulai_pengobatan` → `Observation.issued` (614) |
| 21 | 618–624 | Specimen | 119334006 | Sputum specimen | `tanggal_pengambilan_dahak_untuk_uji_kepekaan_hhbbtttt` → `Specimen.collectedDateTime` (621)<br>`nama_lengkap_pasien` → `Specimen.subject.display` (623)<br>`tanggal_pengambilan_dahak_untuk_uji_kepekaan_hhbbtttt` → `Specimen.receivedTime` (624) |
| 22 | 626–693 | Observation | X099383 | Pemeriksaan Paket Standar Kepekaan | `hasil_pemeriksaan_paket_standar_uji_kepekaan_h_dosis_tinggi` → `Observation.component.code.coding` (631)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_h` → `Observation.component.code.coding` (637)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_km` → `Observation.component.code.coding` (643)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_cm` → `Observation.component.code.coding` (649)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_lfx` → `Observation.component.code.coding` (655)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_mfx_dosis_tinggi` → `Observation.component.code.coding` (661)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_mfx` → `Observation.component.code.coding` (667)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan` → `Observation.component.code.coding` (673)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_1` → `Observation.component.code.coding` (675)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_2` → `Observation.component.code.coding` (677)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_3` → `Observation.component.code.coding` (679)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_4` → `Observation.component.code.coding` (681)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_5` → `Observation.component.code.coding` (683)<br>`nama_lengkap_pasien` → `Observation.subject.display` (688)<br>`tgl_mulai_pengobatan` → `Observation.effectiveDateTime` (690)<br>`tanggal_hasil_uji_kepekaan_keluar_hhbbtttt` → `Observation.issued` (691) |
| 23 | 695–738 | Observation | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | _BTA_ → `Observation.valueCodeableConcept.coding` (699, tanpa BQ)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__1_bta` → `Observation.valueCodeableConcept.coding` (705)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__2_bta` → `Observation.valueCodeableConcept.coding` (706)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__3_bta` → `Observation.valueCodeableConcept.coding` (707)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__4_bta` → `Observation.valueCodeableConcept.coding` (708)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__4_bta_2` → `Observation.valueCodeableConcept.coding` (709)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__5_bta` → `Observation.valueCodeableConcept.coding` (710)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__5_bta2` → `Observation.valueCodeableConcept.coding` (711)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__6_bta` → `Observation.valueCodeableConcept.coding` (712)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__6_bta2` → `Observation.valueCodeableConcept.coding` (713)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__7_bta` → `Observation.valueCodeableConcept.coding` (714)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__8_bta` → `Observation.valueCodeableConcept.coding` (715)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__9_bta` → `Observation.valueCodeableConcept.coding` (716)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__10_bta` → `Observation.valueCodeableConcept.coding` (717)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__11_bta` → `Observation.valueCodeableConcept.coding` (718)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__12_bta` → `Observation.valueCodeableConcept.coding` (719)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__13_bta` → `Observation.valueCodeableConcept.coding` (720)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__14_bta` → `Observation.valueCodeableConcept.coding` (721)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__15_bta` → `Observation.valueCodeableConcept.coding` (722)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__16_bta` → `Observation.valueCodeableConcept.coding` (723)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__17_bta` → `Observation.valueCodeableConcept.coding` (724)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__18_bta` → `Observation.valueCodeableConcept.coding` (725)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__19_bta` → `Observation.valueCodeableConcept.coding` (726)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__20_bta` → `Observation.valueCodeableConcept.coding` (727)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__21_bta` → `Observation.valueCodeableConcept.coding` (728)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__22_bta` → `Observation.valueCodeableConcept.coding` (729)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__23_bta` → `Observation.valueCodeableConcept.coding` (730)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__24_bta` → `Observation.valueCodeableConcept.coding` (731)<br>`nama_lengkap_pasien` → `Observation.subject.display` (733)<br>`tgl_mulai_pengobatan` → `Observation.effectiveDateTime` (735) |
| 24 | 740–784 | Observation | X099388 | Biakan TB | _Biakan_ → `Observation.identifier` (740, tanpa BQ)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__1_b` → `Observation.valueCodeableConcept.coding` (751)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__2_b` → `Observation.valueCodeableConcept.coding` (752)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__3_b` → `Observation.valueCodeableConcept.coding` (753)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__4_b` → `Observation.valueCodeableConcept.coding` (754)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__4_b_2` → `Observation.valueCodeableConcept.coding` (755)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__5_b` → `Observation.valueCodeableConcept.coding` (756)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__5_b2` → `Observation.valueCodeableConcept.coding` (757)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__6_b` → `Observation.valueCodeableConcept.coding` (758)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__6_b2` → `Observation.valueCodeableConcept.coding` (759)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__7_b` → `Observation.valueCodeableConcept.coding` (760)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__8_b` → `Observation.valueCodeableConcept.coding` (761)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__9_b` → `Observation.valueCodeableConcept.coding` (762)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__10_b` → `Observation.valueCodeableConcept.coding` (763)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__11_b` → `Observation.valueCodeableConcept.coding` (764)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__12_b` → `Observation.valueCodeableConcept.coding` (765)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__13_b` → `Observation.valueCodeableConcept.coding` (766)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__14_b` → `Observation.valueCodeableConcept.coding` (767)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__15_b` → `Observation.valueCodeableConcept.coding` (768)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__16_b` → `Observation.valueCodeableConcept.coding` (769)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__17_b` → `Observation.valueCodeableConcept.coding` (770)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__18_b` → `Observation.valueCodeableConcept.coding` (771)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__19_b` → `Observation.valueCodeableConcept.coding` (772)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__20_b` → `Observation.valueCodeableConcept.coding` (773)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__21_b` → `Observation.valueCodeableConcept.coding` (774)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__22_b` → `Observation.valueCodeableConcept.coding` (775)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__23_b` → `Observation.valueCodeableConcept.coding` (776)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__24_b` → `Observation.valueCodeableConcept.coding` (777)<br>`tgl_mulai_pengobatan` → `Observation.effectiveDateTime` (781)<br>`tgl_mulai_pengobatan` → `Observation.issued` (782) |
| 25 | 787–798 | Observation | 365866002 | Finding of human immunodeficiency virus status | `kegiatan_tbchiv_hasil_tes_hiv` → `Observation.valueCodeableConcept.coding` (790)<br>`nama_lengkap_pasien` → `Observation.subject.display` (793)<br>`tgl_mulai_pengobatan` → `Observation.effectiveDateTime` (795) |
| 26 | 800–810 | Procedure | SP000371 | Cotrimoxazole | `kegiatan_tbchiv_kotrimoksasol` → `Procedure.category.coding` (800)<br>`nama_lengkap_pasien` → `Procedure.subject.display` (805)<br>`tgl_mulai_pengobatan` → `Procedure.performedPeriod.start` (807)<br>`tgl_mulai_pengobatan` → `Procedure.performedPeriod.end` (808) |
| 27 | 812–822 | Procedure | SP000046 | Terapi Antiretroviral (ART) | `kegiatan_tbchiv_art` → `Procedure.category.coding` (812)<br>`nama_lengkap_pasien` → `Procedure.subject.display` (817)<br>`tgl_mulai_pengobatan` → `Procedure.performedPeriod.start` (819)<br>`tgl_mulai_pengobatan` → `Procedure.performedPeriod.end` (820) |
| 28 | 824–835 | Observation | SP000047 | Hasil Tes Diabetes Melitus | `kegiatan_tbcdm_dm` → `Observation.valueCodeableConcept.coding` (827)<br>`nama_lengkap_pasien` → `Observation.subject.display` (830)<br>`tgl_mulai_pengobatan` → `Observation.effectiveDateTime` (832)<br>`tgl_mulai_pengobatan` → `Observation.issued` (833) |
| 29 | 837–848 | Observation | 1284985006 | Diabetes mellitus management program | `kegiatan_tbcdm_terapi_dm` → `Observation.valueCodeableConcept.coding` (840)<br>`nama_lengkap_pasien` → `Observation.subject.display` (843)<br>`tgl_mulai_pengobatan` → `Observation.effectiveDateTime` (845)<br>`tgl_mulai_pengobatan` → `Observation.issued` (846) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 18 |
| Procedure | 3 |
| Patient | 1 |
| EpisodeOfCare | 1 |
| Coverage | 1 |
| Encounter | 1 |
| Condition | 1 |
| QuestionnaireResponse | 1 |
| CarePlan | 1 |
| Specimen | 1 |
| **Total** | **29** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 35 | EpisodeOfCare | `EpisodeOfCare.type.coding` | TB-RO | Tuberkulosis Resisten Obat | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 2 | 61 | Encounter | `Encounter.hospitalization.admitSource.coding` | EHA000002 | Datang sendiri | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 3 | 62 | Encounter | `Encounter.hospitalization.admitSource.coding` | EHA000003 | Kegiatan ACF | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 4 | 63 | Encounter | `Encounter.hospitalization.admitSource.coding` | 257622000 | Healthcare facility | http://snomed.info/sct |
| 5 | 64 | Encounter | `Encounter.hospitalization.admitSource.coding` | EHA000004 | Skrining TBC DM | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 6 | 65 | Encounter | `Encounter.hospitalization.admitSource.coding` | EHA000005 | Pemadanan Data BPJS | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 7 | 66 | Encounter | `Encounter.hospitalization.admitSource.coding` | 225368008 | Contact tracing | http://snomed.info/sct |
| 8 | 67 | Encounter | `Encounter.hospitalization.admitSource.coding` | EHA000002 | Datang sendiri | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 9 | 101 | Condition | `Condition.code.coding` | A15.0 | Tuberculosis of lung, confirmed by sputum microscopy with or without culture | http://hl7.org/fhir/sid/icd-10 |
| 10 | 102 | Condition | `Condition.code.coding` | A16.2 | Tuberculosis of lung, without mention of bacteriological or histological confirmation | http://hl7.org/fhir/sid/icd-10 |
| 11 | 110 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 12 | 123 | Observation | `Observation.code.coding` | 85658-3 | Occupation [Type] | http://loinc.org |
| 13 | 124 | Observation | `Observation.valueCodeableConcept.coding` | 106540006 | Laborer | http://snomed.info/sct |
| 14 | 125 | Observation | `Observation.valueCodeableConcept.coding` | 106304008 | Teacher | http://snomed.info/sct |
| 15 | 126 | Observation | `Observation.valueCodeableConcept.coding` | 106304008 | Teacher | http://snomed.info/sct |
| 16 | 127 | Observation | `Observation.valueCodeableConcept.coding` | 106305009 | University/higher education teacher | http://snomed.info/sct |
| 17 | 128 | Observation | `Observation.valueCodeableConcept.coding` | 444168002 | Homemaker | http://snomed.info/sct |
| 18 | 129 | Observation | `Observation.valueCodeableConcept.coding` | OV000430 | Pegawai Swasta/ BUMN/ BUMD | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 19 | 130 | Observation | `Observation.valueCodeableConcept.coding` | 65853000 | Student | http://snomed.info/sct |
| 20 | 131 | Observation | `Observation.valueCodeableConcept.coding` | 106386007 | Agricultural animal husbandry/forestry worker, fisherman/hunter | http://snomed.info/sct |
| 21 | 132 | Observation | `Observation.valueCodeableConcept.coding` | 106388008 | Farmer | http://snomed.info/sct |
| 22 | 133 | Observation | `Observation.valueCodeableConcept.coding` | 36625000 | Livestock worker | http://snomed.info/sct |
| 23 | 134 | Observation | `Observation.valueCodeableConcept.coding` | 77715000 | Fisherman | http://snomed.info/sct |
| 24 | 135 | Observation | `Observation.valueCodeableConcept.coding` | 236297007 | Civil servant | http://snomed.info/sct |
| 25 | 136 | Observation | `Observation.valueCodeableConcept.coding` | OV000431 | Siswa Berasrama | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 26 | 137 | Observation | `Observation.valueCodeableConcept.coding` | 236320001 | Vehicle driver (occupation) | http://snomed.info/sct |
| 27 | 138 | Observation | `Observation.valueCodeableConcept.coding` | 223366009 | Healthcare professional (occupation) | http://snomed.info/sct |
| 28 | 139 | Observation | `Observation.valueCodeableConcept.coding` | OV000432 | Tenaga Profesional Nonmedis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 29 | 140 | Observation | `Observation.valueCodeableConcept.coding` | OV000433 | TNI/ Polri | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 30 | 141 | Observation | `Observation.valueCodeableConcept.coding` | OV000434 | Warga Binaan Pemasyarakatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 31 | 142 | Observation | `Observation.valueCodeableConcept.coding` | 160906004 | Self-employed | http://snomed.info/sct |
| 32 | 143 | Observation | `Observation.valueCodeableConcept.coding` | 741062008 | Not in labor force | http://snomed.info/sct |
| 33 | 144 | Observation | `Observation.valueCodeableConcept.coding` | 261665006 | Unknown | http://snomed.info/sct |
| 34 | 145 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 35 | 146 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 36 | 158 | Observation | `Observation.code.coding` | 82810-3 | Pregnancy status | http://loinc.org |
| 37 | 159 | Observation | `Observation.valueCodeableConcept.coding` | LA15173-0 | Pregnant | http://loinc.org |
| 38 | 160 | Observation | `Observation.valueCodeableConcept.coding` | LA26683-5 | Not Pregnant | http://loinc.org |
| 39 | 172 | Observation | `Observation.code.coding` | 225368008 | Contact tracing | http://snomed.info/sct |
| 40 | 197 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | QRI000001 | Terduga TBC SO | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 41 | 198 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | QRI000002 | Terduga TBC RO | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 42 | 201 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | new | Kasus Baru | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 43 | 202 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | relapse | Kasus Kambuh | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 44 | 203 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure-cat1 | Kasus Pengobatan Setelah Gagal Kategori 1 | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 45 | 204 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure-cat2 | Kasus Pengobatan Setelah Gagal Kategori 2 | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 46 | 205 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | loss-to-follow-up | Kasus Setelah Loss To Follow Up | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 47 | 206 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure-2line | Kasus Pengobatan Setelah Gagal lini 2 | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 48 | 207 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | not-eval | Pernah diobati tidak diketahui hasilnya | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 49 | 208 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | unknown | Kasus dengan riwayat pengobatan tidak diketahui | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 50 | 209 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | other | Kasus lain-lain | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 51 | 210 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure | Kasus Pengobatan Setelah Gagal | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 52 | 213 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure-cat2 | Kasus Pengobatan Setelah Gagal Kategori 2 | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 53 | 214 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | treatment-non-conversion-2 | Pasien TB pengobatan kategori 2 yang tidak konversi setelah 3 bulan pengobatan | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 54 | 215 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | non-standard-treatment | Pasien TB yang mempunyai riwayat pengobatan TB yang tidak standar | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 55 | 216 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure-cat1 | Kasus Pengobatan Setelah Gagal Kategori 1 | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 56 | 217 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | treatment-non-conversion-1 | Pasien TB pengobatan kategori 1 yang tidak konversi | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 57 | 218 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | relapse | Kasus Baru | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 58 | 219 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | loss-to-follow-up | Kasus Setelah Loss To Follow Up | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 59 | 220 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | history-of-close-contact with-TB-DR | Terduga TB yang mempunyai riwayat kontak erat dengan pasien TB RO | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 60 | 221 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | co-infected-TBHIV | Pasien ko-infeksi TB-HIV yang tidak respons secara klinis maupun bakteriologis terhadap pemberian OAT | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 61 | 222 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure-2line | Kasus Pengobatan Setelah Gagal lini 2 | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 62 | 223 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TB-DR-relapse | Pasien TB RO kasus kambuh | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 63 | 224 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TB-DR-returns | Pasien TB RO yang kembali setelah putus berobat | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 64 | 227 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 154283005 | Pulmonary tuberculosis | http://snomed.info/sct |
| 65 | 228 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 423997002 | Tuberculosis, extrapulmonary | http://snomed.info/sct |
| 66 | 232 | Observation | `Observation.code.coding` | 33248-6 | Diabetes status | http://loinc.org |
| 67 | 233 | Observation | `Observation.valueCodeableConcept.coding` | 10828004 | Positive | http://snomed.info/sct |
| 68 | 234 | Observation | `Observation.valueCodeableConcept.coding` | 260385009 | Negative | http://snomed.info/sct |
| 69 | 235 | Observation | `Observation.valueCodeableConcept.coding` | 261665006 | Unknown | http://snomed.info/sct |
| 70 | 246 | Observation | `Observation.code.coding` | 55277-8 | HIV status | http://loinc.org |
| 71 | 247 | Observation | `Observation.valueCodeableConcept.coding` | 10828004 | Positive | http://snomed.info/sct |
| 72 | 248 | Observation | `Observation.valueCodeableConcept.coding` | 260385009 | Negative | http://snomed.info/sct |
| 73 | 249 | Observation | `Observation.valueCodeableConcept.coding` | 261665006 | Unknown | http://snomed.info/sct |
| 74 | 259 | Procedure | `Procedure.code.coding` | 424489006 | Mantoux test | http://snomed.info/sct |
| 75 | 261 | Procedure | `Procedure.code.coding` | 35140007 | Interferon gamma assay | http://snomed.info/sct |
| 76 | 263 | Procedure | `Procedure.code.coding` | 424489006 | Mantoux test | http://snomed.info/sct |
| 77 | 265 | Procedure | `Procedure.code.coding` | 35140007 | Interferon gamma assay | http://snomed.info/sct |
| 78 | 277 | Observation | `Observation.code.coding` | 23539-0 | Tuberculosis reaction wheal [Diameter] --3 days post dose mammalian tuberculin intradermal | http://loinc.org |
| 79 | 278 | Observation | `Observation.valueCodeableConcept.coding` | 268376005 | Mantoux: positive | http://snomed.info/sct |
| 80 | 279 | Observation | `Observation.valueCodeableConcept.coding` | 268375009 | Mantoux: negative | http://snomed.info/sct |
| 81 | 280 | Observation | `Observation.code.coding` | 71773-6 | Mycobacterium tuberculosis stimulated gamma interferon [Interpretation] in Blood Qualitative | http://loinc.org |
| 82 | 281 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 83 | 282 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 84 | 283 | Observation | `Observation.code.coding` | 23539-0 | Tuberculosis reaction wheal [Diameter] --3 days post dose mammalian tuberculin intradermal | http://loinc.org |
| 85 | 285 | Observation | `Observation.code.coding` | 71773-6 | Mycobacterium tuberculosis stimulated gamma interferon [Interpretation] in Blood Qualitative | http://loinc.org |
| 86 | 297 | Observation | `Observation.code.coding` | 24648-8 | XR Chest PA upright | http://loinc.org |
| 87 | 298 | Observation | `Observation.valueCodeableConcept.coding` | 17621005 | Normal | http://snomed.info/sct |
| 88 | 299 | Observation | `Observation.valueCodeableConcept.coding` | 2483006 | Cavity | http://snomed.info/sct |
| 89 | 300 | Observation | `Observation.valueCodeableConcept.coding` | 27925004 | Nodule | http://snomed.info/sct |
| 90 | 301 | Observation | `Observation.valueCodeableConcept.coding` | 1255665007 | Moderate | http://snomed.info/sct |
| 91 | 302 | Observation | `Observation.valueCodeableConcept.coding` | 47604008 | Miliary tuberculosis | http://snomed.info/sct |
| 92 | 303 | Observation | `Observation.valueCodeableConcept.coding` | 30746006 | Lymphadenopathy | http://snomed.info/sct |
| 93 | 304 | Observation | `Observation.valueCodeableConcept.coding` | 260544000 | Endobronchial (qualifier value) | http://snomed.info/sct |
| 94 | 305 | Observation | `Observation.valueCodeableConcept.coding` | 112674009 | Fibrosis | http://snomed.info/sct |
| 95 | 306 | Observation | `Observation.valueCodeableConcept.coding` | 442110002 | Fibrosis of pleura | http://snomed.info/sct |
| 96 | 307 | Observation | `Observation.valueCodeableConcept.coding` | 1303092009 | Pulmonary bulla | http://snomed.info/sct |
| 97 | 308 | Observation | `Observation.valueCodeableConcept.coding` | 60046008 | Pleural effusion | http://snomed.info/sct |
| 98 | 309 | Observation | `Observation.valueCodeableConcept.coding` | 36118008 | Pneumothorax | http://snomed.info/sct |
| 99 | 310 | Observation | `Observation.valueCodeableConcept.coding` | 12295008 | Bronchiectasis | http://snomed.info/sct |
| 100 | 311 | Observation | `Observation.valueCodeableConcept.coding` | 46621007 | Atelectasis | http://snomed.info/sct |
| 101 | 312 | Observation | `Observation.valueCodeableConcept.coding` | 9656002 | Consolidation | http://snomed.info/sct |
| 102 | 313 | Observation | `Observation.valueCodeableConcept.coding` | 309529002 | Lung mass | http://snomed.info/sct |
| 103 | 314 | Observation | `Observation.valueCodeableConcept.coding` | 385633008 | Improving | http://snomed.info/sct |
| 104 | 315 | Observation | `Observation.valueCodeableConcept.coding` | 230993007 | Worsening | http://snomed.info/sct |
| 105 | 316 | Observation | `Observation.valueCodeableConcept.coding` | 58158008 | Stable | http://snomed.info/sct |
| 106 | 341 | CarePlan | `CarePlan.activity.detail.code.coding` | CP000006 | Paduan OAT | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 107 | 342 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000007 | OAT Kategori 1 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 108 | 343 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000008 | OAT Kategori 2 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 109 | 344 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000009 | OAT Kategori Anak | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 110 | 345 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000010 | OAT Paduan tidak standar TB SO | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 111 | 346 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000011 | OAT Paduan Jangka Pendek | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 112 | 347 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000012 | OAT Paduan Jangka Panjang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 113 | 348 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000013 | OAT Paduan Individual | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 114 | 349 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000014 | OAT Paduan Monoresistan INH | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 115 | 352 | CarePlan | `CarePlan.activity.detail.code.coding` | CP000005 | Paduan Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 116 | 353 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000015 | 2(HRZE)/4(HR)3 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 117 | 354 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000016 | 2(HRZE)/4(HR) - KDT Dosis Harian | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 118 | 355 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000017 | 2(HRZE)S/(HRZE)/5(HRE) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 119 | 356 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000018 | 2(HRZE)S/(HRZE)/5((HR)3E3) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 120 | 357 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000019 | 2HRZE/4HR | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 121 | 358 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000020 | 2HRZES/HRZE/ 5H3R3E3 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 122 | 359 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000021 | 2(HRZ)/4(HR) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 123 | 360 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000022 | 2(HRZ)/4(HR) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 124 | 361 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000023 | Km Cs Eto Lfx Z VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 125 | 362 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000024 | Km Cs Eto Lfx PAS E Z VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 126 | 363 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000025 | Km Cs Eto Lfx E Z VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 127 | 364 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000026 | Km Cs Eto Mfx PAS Z VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 128 | 365 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000027 | Km Cs Eto Mfx PAS E VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 129 | 366 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000028 | Cm Cs Eto Lfx E Z Vit B6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 130 | 367 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000029 | Cm Cs Eto Lfx PAS Z VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 131 | 368 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000030 | Cm Cs Eto Mfx Z VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 132 | 369 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000031 | Cm Cs Eto Mfx PAS Z VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 133 | 370 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000032 | Km Eto Cs PAS Z Bdq | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 134 | 371 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000033 | Lfx Eto Cs PAS Z Bdq | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 135 | 372 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000034 | Eto Cs PAS Z Bdq Lnz Clf | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 136 | 373 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000035 | Km Lfx (Eto/CS/PAS) Z Bdq (Lnz/Clf) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 137 | 374 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000036 | 5 Km Mfx(h) Eto Cfz Z H(h) E/ 5Mfx(h) Cfz Z E | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 138 | 375 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000037 | 6 Dlm Lfx Eto Cs ZE B6/ 18 Lfx Eto Cs ZE B6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 139 | 376 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000038 | 10 Cm Dlm Lzd Eto Cs Z E B6/14 Lzd Eto Cs Z E B6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 140 | 377 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000039 | 6 Dlm Lzd Cfz Eto Cs PAS ZE B6/ 18 lzd Cfz Eto Cs PAS Z E B6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 141 | 378 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000040 | Etambutol | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 142 | 379 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000041 | Paduan TPT 6Lfx 250 mg + E 400 mg Dewasa | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 143 | 380 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000042 | 6 Bdq-Lfx-Lzd-Cfz-Cs-VitB6 / 14 Lfx-Cfz-Cs-VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 144 | 381 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000043 | 6 Bdq-Lfx-Cfz-Cs-E -VitB6/ 14 Lfx-Cfz-Cs-E-VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 145 | 382 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000044 | 6 Bdq-Lfx-Lzd-Cfz-E / 14 Lfx-Cfz-E | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 146 | 383 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000045 | 6 Bdq-Mfx-Lzd-Cfz-E / 14 Mfx-Cfz-E | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 147 | 384 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000046 | 6 Bdq-Lzd-Cfz-Cs-E-VitB6 / 14 Lzd-Cfz-Cs-E -VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 148 | 385 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000047 | 6 Bdq-Lzd-Cfz-Cs-Eto / 14 Lzd-Cfz-Cs-Eto- Vit B6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 149 | 386 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000048 | 6 Dlm-Lfx-Lzd-Clz-Cs / 14 Lfx-Lzd-Clz-Cs -VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 150 | 387 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000049 | 20 Lfx-Lzd-Cfz-Cs-Eto -VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 151 | 388 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000050 | 20 Mfx-Lzd-Cfz-Cs-E -VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 152 | 389 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000051 | 20 Mfx-Lzd-Cfz-Cs-Z -VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 153 | 390 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000052 | 6 Lfx-Lzd-Cfz-Cs-Amk-VitB6 / 14 Lfx-Lzd-Clz-Cs-VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 154 | 391 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000053 | 6 Lfx-Lzd-Cfz-Cs-S-VitB6 / 14 Lfx-Lzd-Clz-Cs-VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 155 | 392 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000054 | 6 Lfx-Lzd-Cfz-Eto-PAS / 14 Lfx-Lzd-Clz-Eto | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 156 | 393 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000055 | 6 Dlm-Lzd-Cfz-Cs-E / 14 Lzd-Clz-Cs-E-Vit B6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 157 | 394 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000056 | Pro TB 3 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 158 | 395 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000057 | 6 Bdq-Lfx-Lzd-Cfz-H(Hdose)-Z-E/5 Lfx-Cfz-Z-E | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 159 | 396 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000058 | 6 Dlm-Lzd-Cfz-Cs-E / 14 Lzd-Clz-Cs-E-Vit B6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 160 | 397 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000059 | 6 Dlm-Lfx-Lzd-Clz-Cs / 14 Lfx-Lzd-Clz-Cs -VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 161 | 398 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000060 | 6 Bdq-Lfx-Eto-E-Z-Hh-Cfz/ 5 Lfx)-Cfz-Z-E (STR Non Inj) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 162 | 399 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000061 | 6 Bdq-Mfx-Eto-E-Z-Hh-Cfz/ 5-Mfx-Cfz-Z-E (STR Non Inj) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 163 | 400 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000062 | Paduan TPT 6H 100 mg (INH) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 164 | 401 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000063 | Paduan TPT 3HP Lepasan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 165 | 402 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000064 | Paduan TPT 6H 300 mg (INH) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 166 | 403 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000065 | Paduan TPT 6Lfx 250mg | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 167 | 404 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000066 | Paduan TPT 3HR KDT | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 168 | 405 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000067 | Paduan TPT 3HR KDT | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 169 | 406 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000068 | 5 Lfx-Lzd-Cfz-Cs / 5 Lfx-Cfz-Cs | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 170 | 407 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000069 | 6 Lfx-Lzd-Cfz-Cs-Eto / 12 Lfx-Cfz-Cs-Eto | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 171 | 408 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000070 | 6 Lzd-Cfz-Cs-Eto / 5 Cfz-Cs-Eto | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 172 | 409 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000071 | 6 Lzd-Cfz-Cs-Eto / 12 Cfz-Cs-Eto | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 173 | 410 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000072 | 5 Lfx-Lzd-Cfz-Cs-Dlm / 5 Lfx-Cfz-Cs | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 174 | 411 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000073 | 6 Lfx-Lzd-Cfz-Cs-Dlm / 12 Lfx-Cfz-Cs | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 175 | 412 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000074 | 5 Lzd-Cfz-Cs-Dlm-Eto/5 Cfz-Cs-Eto | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 176 | 413 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000075 | 6 Lzd-Cfz-Cs-Dlm-Eto/ 12 Cfz-Cs-Eto | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 177 | 414 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000076 | 6 Bdq-Lfx-Lzd-Cfz-Cs / 5 Lfx-Cfz- Cs | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 178 | 415 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000077 | 6 Bdq-Lfx-Lzd-Cfz-Cs / 12 Lfx-Cfz-Cs | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 179 | 416 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000078 | 6 Bdq-Lzd-Cfz-Cs-PAS / 5 Cfz-Cs-PAS | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 180 | 417 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000079 | 6 Bdq-Lzd-Cfz-Cs- PAS / 12 Cfz-Cs-PAS | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 181 | 418 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000080 | Paduan TPT 6Lfx 100 mg + E 100 mg | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 182 | 419 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000081 | Paduan TPT 6Lfx 100mg | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 183 | 420 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000082 | Paduan TPT 3HR 300mg/450mg Lepasan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 184 | 421 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000083 | Paduan TPT 3HR 300mg/600mg Lepasan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 185 | 422 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000084 | RHZE (150/75/400/275) + Levofloxacin | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 186 | 423 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000085 | Bedaquline Pretomanid Linezolid (BPAL) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 187 | 424 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000086 | Bedaquline Pretomanid Linezolid Moxifloxacin (BPALM) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 188 | 425 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000087 | Paduan TPT 1HP 300mg/300mg Lepasan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 189 | 426 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000088 | Paduan TPT 1HP 300mg/150mg Lepasan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 190 | 427 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000089 | 6 BDQ-Lfx-Cfz-Hdt-Z-E-Lzd(2 bulan)/ 5 Lfx-Cfz-Z-E | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 191 | 428 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000090 | 2HPMZ/2HPM | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 192 | 432 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | SP001137 | Paduan lainnya | http://terminology.kemkes.go.id/sp |
| 193 | 434 | CarePlan | `CarePlan.activity.outcomeCodeableConcept.coding` | 371001000 | Patient cured | http://snomed.info/sct |
| 194 | 435 | CarePlan | `CarePlan.activity.outcomeCodeableConcept.coding` | 182992009 | Treatment completed | http://snomed.info/sct |
| 195 | 436 | CarePlan | `CarePlan.activity.outcomeCodeableConcept.coding` | CP000094 | Pengobatan Gagal | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 196 | 437 | CarePlan | `CarePlan.activity.outcomeCodeableConcept.coding` | 419099009 | Dead | http://snomed.info/sct |
| 197 | 438 | CarePlan | `CarePlan.activity.outcomeCodeableConcept.coding` | 399307001 | Lost to follow-up | http://snomed.info/sct |
| 198 | 439 | CarePlan | `CarePlan.activity.outcomeCodeableConcept.coding` | CP000096 | Tidak dievaluasi/pindah | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 199 | 445 | Observation | `Observation.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 200 | 446 | Observation | `Observation.code.coding` | 89371-9 | MTB complex DNA and rpoB RIF resistance mutation panel [Presence] | http://loinc.org |
| 201 | 447 | Observation | `Observation.code.coding` | X099379 | Pemeriksaan TCM XDR | http://terminology.kemkes.go.id/CodeSystem/examination |
| 202 | 448 | Observation | `Observation.code.coding` | X099380 | Line Probe Assay (LPA) Lini 1 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 203 | 449 | Observation | `Observation.code.coding` | X099381 | Line Probe Assay (LPA) Lini 2 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 204 | 450 | Observation | `Observation.code.coding` | X099388 | Biakan TB | http://terminology.kemkes.go.id/CodeSystem/examination |
| 205 | 451 | Observation | `Observation.code.coding` | X099383 | Pemeriksaan Paket Standar Kepekaan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 206 | 452 | Observation | `Observation.code.coding` | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 207 | 453 | Observation | `Observation.code.coding` | MK099927 | Pemeriksaan PCR Open System | http://terminology.kemkes.go.id/CodeSystem/examination |
| 208 | 454 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 209 | 455 | Observation | `Observation.valueCodeableConcept.coding` | X099770 | Rifampisin sensitive | http://terminology.kemkes.go.id/CodeSystem/examination |
| 210 | 456 | Observation | `Observation.valueCodeableConcept.coding` | X099771 | Rifampisin resistan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 211 | 457 | Observation | `Observation.valueCodeableConcept.coding` | X099772 | Rifampisin indeterminate | http://terminology.kemkes.go.id/CodeSystem/examination |
| 212 | 473 | Observation | `Observation.code.coding` | X099379 | Pemeriksaan TCM XDR | http://terminology.kemkes.go.id/CodeSystem/examination |
| 213 | 474 | Observation | `Observation.valueCodeableConcept.coding` | X099781 | Hasil Valid | http://terminology.kemkes.go.id/CodeSystem/examination |
| 214 | 479 | Observation | `Observation.component.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 215 | 480 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 216 | 482 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 217 | 484 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 218 | 486 | Observation | `Observation.component.code.coding` | X099391 | H Dosis Rendah (Low) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 219 | 487 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 220 | 488 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 221 | 489 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 222 | 491 | Observation | `Observation.component.code.coding` | 89488-1 | Isoniazid [Susceptibility] by Genotype method | http://loinc.org |
| 223 | 492 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 224 | 493 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 225 | 494 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 226 | 496 | Observation | `Observation.component.code.coding` | 96110-2 | Ethionamide [Susceptibility] by Genotype method | http://loinc.org |
| 227 | 497 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 228 | 498 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 229 | 500 | Observation | `Observation.component.code.coding` | X099392 | FQ Dosis Rendah (Low) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 230 | 501 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 231 | 502 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 232 | 503 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 233 | 505 | Observation | `Observation.component.code.coding` | 89487-3 | Fluoroquinolone [Susceptibility] by Genotype method | http://loinc.org |
| 234 | 506 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 235 | 507 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 236 | 508 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 237 | 510 | Observation | `Observation.component.code.coding` | 89484-0 | Amikacin [Susceptibility] by Genotype method | http://loinc.org |
| 238 | 511 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 239 | 512 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 240 | 513 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 241 | 515 | Observation | `Observation.component.code.coding` | 89482-4 | Kanamycin [Susceptibility] by Genotype method | http://loinc.org |
| 242 | 516 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 243 | 517 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 244 | 518 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 245 | 520 | Observation | `Observation.component.code.coding` | 89483-2 | Capreomycin [Susceptibility] by Genotype method | http://loinc.org |
| 246 | 521 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 247 | 522 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 248 | 523 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 249 | 536 | Observation | `Observation.code.coding` | X099380 | Line Probe Assay (LPA) Lini 1 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 250 | 537 | Observation | `Observation.valueCodeableConcept.coding` | X099781 | Hasil Valid | http://terminology.kemkes.go.id/CodeSystem/examination |
| 251 | 540 | Observation | `Observation.component.code.coding` | 13956-8 | Mycobacterium tuberculosis DNA [Presence] in Specimen by NAA with probe detection | http://loinc.org |
| 252 | 541 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 253 | 542 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 254 | 544 | Observation | `Observation.component.code.coding` | 89489-9 | rifAMPin [Susceptibility] by Genotype method | http://loinc.org |
| 255 | 545 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 256 | 546 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 257 | 547 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 258 | 548 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 259 | 550 | Observation | `Observation.component.code.coding` | 89488-1 | Isoniazid [Susceptibility] by Genotype method | http://loinc.org |
| 260 | 551 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 261 | 552 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 262 | 553 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 263 | 554 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 264 | 566 | Observation | `Observation.code.coding` | X099381 | Line Probe Assay (LPA) Lini 2 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 265 | 567 | Observation | `Observation.valueCodeableConcept.coding` | X099781 | Hasil Valid | http://terminology.kemkes.go.id/CodeSystem/examination |
| 266 | 570 | Observation | `Observation.component.code.coding` | 13956-8 | Mycobacterium tuberculosis DNA [Presence] in Specimen by NAA with probe detection | http://loinc.org |
| 267 | 571 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 268 | 572 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 269 | 574 | Observation | `Observation.component.code.coding` | 20629-2 | levoFLOXacin [Susceptibility] | http://loinc.org |
| 270 | 575 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 271 | 576 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 272 | 577 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 273 | 578 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 274 | 580 | Observation | `Observation.component.code.coding` | 96112-8 | Moxifloxacin [Susceptibility] by Genotype method | http://loinc.org |
| 275 | 581 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 276 | 582 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 277 | 583 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 278 | 584 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 279 | 586 | Observation | `Observation.component.code.coding` | X099775 | Moxifloxacin DT (Mfx DT) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 280 | 587 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 281 | 588 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 282 | 589 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 283 | 590 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 284 | 592 | Observation | `Observation.component.code.coding` | 89482-4 | Kanamycin [Susceptibility] by Genotype method | http://loinc.org |
| 285 | 593 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 286 | 594 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 287 | 595 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 288 | 596 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 289 | 598 | Observation | `Observation.component.code.coding` | 89484-0 | Amikacin [Susceptibility] by Genotype method | http://loinc.org |
| 290 | 599 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 291 | 600 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 292 | 601 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 293 | 602 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 294 | 604 | Observation | `Observation.component.code.coding` | 89483-2 | Capreomycin [Susceptibility] by Genotype method | http://loinc.org |
| 295 | 605 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 296 | 606 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 297 | 607 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 298 | 608 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 299 | 619 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 300 | 628 | Observation | `Observation.code.coding` | X099383 | Pemeriksaan Paket Standar Kepekaan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 301 | 631 | Observation | `Observation.component.code.coding` | X099776 | H High Dosage [Susceptibility] by Method for Slow-growing mycobacteria | http://terminology.kemkes.go.id/CodeSystem/examination |
| 302 | 632 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 303 | 633 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 304 | 634 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 305 | 637 | Observation | `Observation.component.code.coding` | 20383-6 | Isoniazid [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 306 | 638 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 307 | 639 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 308 | 640 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 309 | 643 | Observation | `Observation.component.code.coding` | 23609-1 | Kanamycin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 310 | 644 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 311 | 645 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 312 | 646 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 313 | 649 | Observation | `Observation.component.code.coding` | 23607-5 | Capreomycin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 314 | 650 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 315 | 651 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 316 | 652 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 317 | 655 | Observation | `Observation.component.code.coding` | 53716-7 | levoFLOXacin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 318 | 656 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 319 | 657 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 320 | 658 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 321 | 661 | Observation | `Observation.component.code.coding` | X099778 | Moxifloxacin High Dosage [Susceptibility] by Method for Slow-growing mycobacteria | http://terminology.kemkes.go.id/CodeSystem/examination |
| 322 | 662 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 323 | 663 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 324 | 664 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 325 | 667 | Observation | `Observation.component.code.coding` | 41502-6 | Moxifloxacin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 326 | 668 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 327 | 669 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 328 | 670 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 329 | 673 | Observation | `Observation.component.code.coding` | SP000472 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya | http://terminology.kemkes.go.id/sp |
| 330 | 675 | Observation | `Observation.component.code.coding` | SP000473 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 1 | http://terminology.kemkes.go.id/sp |
| 331 | 677 | Observation | `Observation.component.code.coding` | SP000474 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 2 | http://terminology.kemkes.go.id/sp |
| 332 | 679 | Observation | `Observation.component.code.coding` | SP000475 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 3 | http://terminology.kemkes.go.id/sp |
| 333 | 681 | Observation | `Observation.component.code.coding` | SP000476 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 4 | http://terminology.kemkes.go.id/sp |
| 334 | 683 | Observation | `Observation.component.code.coding` | SP000477 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 5 | http://terminology.kemkes.go.id/sp |
| 335 | 698 | Observation | `Observation.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 336 | 699 | Observation | `Observation.valueCodeableConcept.coding` | 260385009 | Negative | http://snomed.info/sct |
| 337 | 700 | Observation | `Observation.valueCodeableConcept.coding` | LA11841-6 | 1+ | http://loinc.org |
| 338 | 701 | Observation | `Observation.valueCodeableConcept.coding` | LA11842-4 | 2+ | http://loinc.org |
| 339 | 702 | Observation | `Observation.valueCodeableConcept.coding` | LA11843-2 | 3+ | http://loinc.org |
| 340 | 743 | Observation | `Observation.code.coding` | X099388 | Biakan TB | http://terminology.kemkes.go.id/CodeSystem/examination |
| 341 | 744 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 342 | 745 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 343 | 746 | Observation | `Observation.valueCodeableConcept.coding` | LA11841-6 | + | http://loinc.org |
| 344 | 747 | Observation | `Observation.valueCodeableConcept.coding` | LA11842-4 | ++ | http://loinc.org |
| 345 | 748 | Observation | `Observation.valueCodeableConcept.coding` | LA11843-2 | +++ | http://loinc.org |
| 346 | 749 | Observation | `Observation.valueCodeableConcept.coding` | 110379001 | Mycobacterium, non-tuberculosis (organism) | http://snomed.info/sct |
| 347 | 789 | Observation | `Observation.code.coding` | 365866002 | Finding of human immunodeficiency virus status | http://snomed.info/sct |
| 348 | 790 | Observation | `Observation.valueCodeableConcept.coding` | 165816005 | Human immunodeficiency virus detected | http://snomed.info/sct |
| 349 | 791 | Observation | `Observation.valueCodeableConcept.coding` | 165815009 | Human immunodeficiency virus not detected | http://snomed.info/sct |
| 350 | 801 | Procedure | `Procedure.code.coding` | SP000371 | Cotrimoxazole | http://terminology.kemkes.go.id/sp |
| 351 | 813 | Procedure | `Procedure.code.coding` | SP000046 | Terapi Antiretroviral (ART) | http://terminology.kemkes.go.id/sp |
| 352 | 826 | Observation | `Observation.code.coding` | SP000047 | Hasil Tes Diabetes Melitus | http://terminology.kemkes.go.id/sp |
| 353 | 827 | Observation | `Observation.valueCodeableConcept.coding` | 10828004 | Positive | http://snomed.info/sct |
| 354 | 828 | Observation | `Observation.valueCodeableConcept.coding` | 260385009 | Negative | http://snomed.info/sct |
| 355 | 839 | Observation | `Observation.code.coding` | 1284985006 | Diabetes mellitus management program | http://snomed.info/sct |
| 356 | 840 | Observation | `Observation.valueCodeableConcept.coding` | SP000372 | Obat Hipoglikemik Oral | http://terminology.kemkes.go.id/sp |
| 357 | 841 | Observation | `Observation.valueCodeableConcept.coding` | 308755006 | Subcutaneous injection of insulin | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah | Code |
|---|---|---|
| http://loinc.org | 121 | 85658-3, 82810-3, LA15173-0, LA26683-5, 33248-6, 55277-8, 23539-0, 71773-6, LA6576-8, LA6577-6, 23539-0, 71773-6, 24648-8, 11545-1, 89371-9, LA6577-6, 88874-3, LA11882-0, LA11882-0, LA11883-8, LA11882-0, LA11883-8, LA11884-6, 89488-1, LA11882-0, LA11883-8, LA11884-6, 96110-2, LA11882-0, LA11883-8, LA11882-0, LA11883-8, LA11884-6, 89487-3, LA11882-0, LA11883-8, LA11884-6, 89484-0, LA11882-0, LA11883-8, LA11884-6, 89482-4, LA11882-0, LA11883-8, LA11884-6, 89483-2, LA11882-0, LA11883-8, LA11884-6, 13956-8, LA6576-8, LA6577-6, 89489-9, LA11882-0, LA11883-8, LA11884-6, 89488-1, LA11882-0, LA11883-8, LA11884-6, 13956-8, LA6576-8, LA6577-6, 20629-2, LA11882-0, LA11883-8, LA11884-6, 96112-8, LA11882-0, LA11883-8, LA11884-6, LA11882-0, LA11883-8, LA11884-6, 89482-4, LA11882-0, LA11883-8, LA11884-6, 89484-0, LA11882-0, LA11883-8, LA11884-6, 89483-2, LA11882-0, LA11883-8, LA11884-6, LA24225-7, LA6676-6, LA16550-8, 20383-6, LA24225-7, LA6676-6, LA16550-8, 23609-1, LA24225-7, LA6676-6, LA16550-8, 23607-5, LA24225-7, LA6676-6, LA16550-8, 53716-7, LA24225-7, LA6676-6, LA16550-8, LA24225-7, LA6676-6, LA16550-8, 41502-6, LA24225-7, LA6676-6, LA16550-8, 11545-1, LA11841-6, LA11842-4, LA11843-2, LA6577-6, LA6576-8, LA11841-6, LA11842-4, LA11843-2 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 100 | EHA000002, EHA000003, EHA000004, EHA000005, EHA000002, OV000430, OV000431, OV000432, OV000433, OV000434, QRI000001, QRI000002, CP000006, CP000007, CP000008, CP000009, CP000010, CP000011, CP000012, CP000013, CP000014, CP000005, CP000015, CP000016, CP000017, CP000018, CP000019, CP000020, CP000021, CP000022, CP000023, CP000024, CP000025, CP000026, CP000027, CP000028, CP000029, CP000030, CP000031, CP000032, CP000033, CP000034, CP000035, CP000036, CP000037, CP000038, CP000039, CP000040, CP000041, CP000042, CP000043, CP000044, CP000045, CP000046, CP000047, CP000048, CP000049, CP000050, CP000051, CP000052, CP000053, CP000054, CP000055, CP000056, CP000057, CP000058, CP000059, CP000060, CP000061, CP000062, CP000063, CP000064, CP000065, CP000066, CP000067, CP000068, CP000069, CP000070, CP000071, CP000072, CP000073, CP000074, CP000075, CP000076, CP000077, CP000078, CP000079, CP000080, CP000081, CP000082, CP000083, CP000084, CP000085, CP000086, CP000087, CP000088, CP000089, CP000090, CP000094, CP000096 |
| http://snomed.info/sct | 69 | 257622000, 225368008, 424144002, 106540006, 106304008, 106304008, 106305009, 444168002, 65853000, 106386007, 106388008, 36625000, 77715000, 236297007, 236320001, 223366009, 160906004, 741062008, 261665006, 74964007, 74964007, 225368008, 154283005, 423997002, 10828004, 260385009, 261665006, 10828004, 260385009, 261665006, 424489006, 35140007, 424489006, 35140007, 268376005, 268375009, 17621005, 2483006, 27925004, 1255665007, 47604008, 30746006, 260544000, 112674009, 442110002, 1303092009, 60046008, 36118008, 12295008, 46621007, 9656002, 309529002, 385633008, 230993007, 58158008, 371001000, 182992009, 419099009, 399307001, 119334006, 260385009, 110379001, 365866002, 165816005, 165815009, 10828004, 260385009, 1284985006, 308755006 |
| http://terminology.kemkes.go.id/CodeSystem/examination | 31 | X099379, X099380, X099381, X099388, X099383, MK099926, MK099927, X099770, X099771, X099772, X099379, X099781, X099391, X099392, X099380, X099781, X099774, X099774, X099381, X099781, X099774, X099774, X099775, X099774, X099774, X099774, X099774, X099383, X099776, X099778, X099388 |
| http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment | 22 | new, relapse, failure-cat1, failure-cat2, loss-to-follow-up, failure-2line, not-eval, unknown, other, failure, failure-cat2, treatment-non-conversion-2, non-standard-treatment, failure-cat1, treatment-non-conversion-1, relapse, loss-to-follow-up, history-of-close-contact with-TB-DR, co-infected-TBHIV, failure-2line, TB-DR-relapse, TB-DR-returns |
| http://terminology.kemkes.go.id/sp | 11 | SP001137, SP000472, SP000473, SP000474, SP000475, SP000476, SP000477, SP000371, SP000046, SP000047, SP000372 |
| http://hl7.org/fhir/sid/icd-10 | 2 | A15.0, A16.2 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 1 | TB-RO |
| **Total** | **357** | |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
