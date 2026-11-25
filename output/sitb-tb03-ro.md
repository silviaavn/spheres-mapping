# Output Form: SITB TB 03 RO

Sumber: `mapping/phdt-data-dictionary-sitb-tb03-ro.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-sitb-tb03-ro.csv) · [struktur file mentah](../raw/sitb-tb03-ro-kolom.md)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 50 |
| Code (`jumlah code` = 1) | 403 |
| Code unik (code + CodeSystem) | 249 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 13 |
| Variabel BQ (unik) | 140 |
| Variabel raw (kolom Excel export) | 144 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–21 | Organization | – | – | `alamat_lengkap_faskes_kode_fasyankes` → `Organization.identifier` (3)<br>`alamat_lengkap_faskes_jenis_fasyankes` → `Organization.type` (4)<br>`alamat_lengkap_faskes_kepemilikan_fasyankes` → `Organization.type` (5)<br>`alamat_lengkap_faskes_nama_fasyankes` → `Organization.name` (7)<br>`alamat_lengkap_faskes_kabupatenkota` → `Organization.address.city` (8)<br>`alamat_lengkap_faskes_provinsi` → `Organization.address.extension.extension.valueCode` (12) |
| 2 | 23–48 | Patient | – | – | `no_rekam_medis` → `Patient.identifier.value` (26)<br>`nomor_identitas_kependudukan_nik` → `Patient.identifier.value` (29)<br>`nama_lengkap_pasien` → `Patient.name.text` (30)<br>`jenis_kelamin` → `Patient.gender` (31)<br>`alamat_lengkap_pasien_kabupatenkota` → `Patient.address.city` (33)<br>`alamat_lengkap_pasien_provinsi` → `Patient.address.extension.extension.valueCode` (37)<br>`alamat_lengkap_pasien_kabupatenkota` → `Patient.address.extension.extension.valueCode` (40)<br>`alamat_lengkap_pasien_kecamatan` → `Patient.address.extension.extension.valueCode` (43)<br>`alamat_lengkap_pasien_kelurahan` → `Patient.address.extension.extension.valueCode` (46)<br>`alamat_lengkap_pasien_alamat_lengkap` → `Patient.address.line` (47) |
| 3 | 50–71 | EpisodeOfCare | TB-RO | Tuberkulosis Resisten Obat | `nomor_register_sitb` → `EpisodeOfCare.identifier.value` (50)<br>`nomor_register_terduga` → `EpisodeOfCare.identifier.value` (52)<br>`nomor_register_pasien` → `EpisodeOfCare.identifier.value` (54)<br>`tgl_pengisian_data_dasar_terduga_tbc_ro` → `EpisodeOfCare.period.start` (57)<br>`nama_lengkap_pasien` → `EpisodeOfCare.patient.display` (70) |
| 4 | 73–77 | Coverage | – | – | `nomor_bpjs` → `Coverage.identifier.value` (77) |
| 5 | 79–113 | Encounter | – | – | `nomor_register_sitb` → `Encounter.identifier` (80)<br>`dirujuk_dikirim_oleh` → `Encounter.hospitalization.admitSource.coding` (82)<br>`nama_lengkap_pasien` → `Encounter.subject.display` (92)<br>`tgl_mulai_pengobatan` → `Encounter.period.start` (96)<br>`tgl_mulai_pengobatan` → `Encounter.period.end` (97)<br>`alamat_lengkap_faskes_nama_fasyankes` → `Encounter.location.location.display` (99)<br>`tgl_mulai_pengobatan` → `Encounter.statusHistory.period.start` (105)<br>`tgl_mulai_pengobatan` → `Encounter.statusHistory.period.end` (106)<br>`tgl_mulai_pengobatan` → `Encounter.statusHistory.period.start` (108)<br>`tgl_mulai_pengobatan` → `Encounter.statusHistory.period.end` (109)<br>`tgl_mulai_pengobatan` → `Encounter.statusHistory.period.start` (111)<br>`tgl_mulai_pengobatan` → `Encounter.statusHistory.period.end` (112) |
| 6 | 115–122 | Condition | A15.0 | Tuberculosis of lung, confirmed by sputum microscopy with or without culture | – |
| 7 | 124–135 | Observation | 424144002 | Current chronological age | `umur_tahun` → `Observation.valueQuantity.value` (127)<br>`nama_lengkap_pasien` → `Observation.subject.display` (130)<br>`tgl_mulai_pengobatan` → `Observation.effectiveDateTime` (132)<br>`nama_lengkap_pasien` → `Observation.issued` (133) |
| 8 | 137–170 | Observation | 85658-3 | Occupation [Type] | `pekerjaan_status` → `Observation.valueCodeableConcept.coding` (140)<br>`nama_lengkap_pasien` → `Observation.subject.display` (164)<br>`tgl_mulai_pengobatan` → `Observation.encounter.reference` (166)<br>`nama_lengkap_pasien` → `Observation.effectiveDateTime` (167) |
| 9 | 172–184 | Observation | 82810-3 | Pregnancy status | _Status Hamil_ → `Observation.status` (172, tanpa BQ)<br>`status_hamil` → `Observation.valueCodeableConcept.coding` (175)<br>`nama_lengkap_pasien` → `Observation.subject.display` (179)<br>`tgl_mulai_pengobatan` → `Observation.effectiveDateTime` (181)<br>`nama_lengkap_pasien` → `Observation.issued` (182) |
| 10 | 186–197 | Observation | 225368008 | Contact tracing | `dilakukan_pemeriksaan_kontak` → `Observation.valueBoolean` (189)<br>`nama_lengkap_pasien` → `Observation.subject.display` (192)<br>`tgl_mulai_pengobatan` → `Observation.effectiveDateTime` (194)<br>`nama_lengkap_pasien` → `Observation.issued` (195) |
| 11 | 200–244 | QuestionnaireResponse | https://fhir.kemkes.go.id/Questionnaire/Q0001 | – | `nama_lengkap_pasien` → `QuestionnaireResponse.subject.display` (203)<br>`tgl_pengisian_data_dasar_terduga_tbc_ro` → `QuestionnaireResponse.authored` (205)<br>`klasifikasi_berdasarkan_riwayat_pengobatan_sebelumnya` → `QuestionnaireResponse.item.item.linkId` (215)<br>`riwayat_pengobatan_tbc_sebelumnya` → `QuestionnaireResponse.item.item.linkId` (227)<br>`klasifikasi_berdasarkan_lokasi_anatomi` → `QuestionnaireResponse.item.item.linkId` (241) |
| 12 | 246–258 | Observation | 33248-6 | Diabetes status | `riwayat_dm` → `Observation.valueCodeableConcept.coding` (249)<br>`nama_lengkap_pasien` → `Observation.subject.display` (253)<br>`tgl_mulai_pengobatan` → `Observation.effectiveDateTime` (255)<br>`tgl_mulai_pengobatan` → `Observation.issued` (256) |
| 13 | 260–272 | Observation | 55277-8 | HIV status | `status_hiv` → `Observation.valueCodeableConcept.coding` (263)<br>`nama_lengkap_pasien` → `Observation.subject.display` (267)<br>`tgl_mulai_pengobatan` → `Observation.effectiveDateTime` (269)<br>`tgl_mulai_pengobatan` → `Observation.issued` (270) |
| 14 | 274–289 | Procedure | 424489006 | Mantoux test | `dilakukan_pemeriksaan_tuberkulinigra` → `Procedure.category.coding` (274)<br>`nama_lengkap_pasien` → `Procedure.subject.display` (284)<br>`tgl_mulai_pengobatan` → `Procedure.performedPeriod.start` (286)<br>`tgl_mulai_pengobatan` → `Procedure.performedPeriod.end` (287) |
| 15 | 291–309 | Observation | 23539-0 | Tuberculosis reaction wheal [Diameter] --3 days post dose mammalian tuberculin intradermal | `hasil_pemeriksaan_tuberkulinigra` → `Observation.valueCodeableConcept.coding` (294)<br>`nama_lengkap_pasien` → `Observation.subject.display` (304)<br>`tgl_mulai_pengobatan` → `Observation.effectiveDateTime` (306)<br>`tgl_mulai_pengobatan` → `Observation.issued` (307) |
| 16 | 311–339 | Observation | 24648-8 | XR Chest PA upright | `hasil_foto_toraks` → `Observation.valueCodeableConcept.coding` (314)<br>`nama_lengkap_pasien` → `Observation.subject.display` (334)<br>`tgl_mulai_pengobatan` → `Observation.effectiveDateTime` (336)<br>`tgl_mulai_pengobatan` → `Observation.issued` (337) |
| 17 | 341–456 | CarePlan | TB-RO | Tuberkulosis Resisten Obat | `nama_lengkap_pasien` → `CarePlan.subject.display` (347)<br>`tgl_mulai_pengobatan` → `CarePlan.period.start` (349)<br>`hasil_akhir_pengobatan_tanggal_hhbbtttt` → `CarePlan.period.end` (350)<br>`nama_fasyankes_satelit_tbc_ro_lanjutan_pengobatan` → `CarePlan.contributor.reference` (354) 🔎 lookup master data<br>`paduan_oat` → `CarePlan.activity.detail.code.coding` (357)<br>`paduan_pengobatan` → `CarePlan.activity.detail.status` (367)<br>`paduan_pengobatan` → `CarePlan.activity.detail.productCodeableConcept.coding` (445)<br>`paduan_pengobatan` → `CarePlan.activity.detail.productCodeableConcept.coding` (446)<br>`paduan_pengobatan` → `CarePlan.activity.detail.productCodeableConcept.coding` (447)<br>`paduan_pengobatan` → `CarePlan.activity.detail.productCodeableConcept.coding` (448)<br>`paduan_pengobatan` → `CarePlan.activity.detail.productCodeableConcept.text` (449)<br>`hasil_akhir_pengobatan_hasil` → `CarePlan.activity.outcomeCodeableConcept.coding` (450)<br>`keterangan` → `CarePlan.note` (456) |
| 18 | 459–468 | ServiceRequest | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | `tanggal_hasil_pemeriksaan_diagnosis_tbc` → `ServiceRequest.occurrenceDateTime` (466) |
| 19 | 470–475 | Specimen | 119334006 | Sputum specimen | – |
| 20 | 477–504 | Observation | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | `jenis_pemeriksaan_diagnosis` → `Observation.status` (477)<br>`hasil_pemeriksaan_diagnosis_tbc` → `Observation.valueCodeableConcept.coding` (488)<br>`nama_lengkap_pasien` → `Observation.subject.display` (497)<br>`tgl_mulai_pengobatan` → `Observation.effectiveDateTime` (499)<br>`tanggal_hasil_pemeriksaan_diagnosis_tbc` → `Observation.issued` (500) |
| 21 | 506–515 | DiagnosticReport | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | `tanggal_hasil_pemeriksaan_diagnosis_tbc` → `DiagnosticReport.issued` (511) |
| 22 | 518–527 | ServiceRequest | X099379 | Pemeriksaan TCM XDR | `tanggal_hasil_pemeriksaan_tcmxdr` → `ServiceRequest.occurrenceDateTime` (525) |
| 23 | 529–534 | Specimen | 119334006 | Sputum specimen | – |
| 24 | 536–598 | Observation | X099379 | Pemeriksaan TCM XDR | `hasil_pemeriksaan_xpert_tcm_xdr_valid_invalid_no_result_error` → `Observation.valueCodeableConcept.coding` (539)<br>`hasil_pemeriksaan_xpert_tcm_xdr_mtb` → `Observation.component.code.coding` (544)<br>`hasil_pemeriksaan_xpert_tcm_xdr_h_dosis_rendah_low` → `Observation.component.code.coding` (551)<br>`hasil_pemeriksaan_xpert_tcm_xdr_h` → `Observation.component.code.coding` (556)<br>`hasil_pemeriksaan_xpert_tcm_xdr_eto` → `Observation.component.code.coding` (561)<br>`hasil_pemeriksaan_xpert_tcm_xdr_fq_dosis_rendah_low` → `Observation.component.code.coding` (565)<br>`hasil_pemeriksaan_xpert_tcm_xdr_fq` → `Observation.component.code.coding` (570)<br>`hasil_pemeriksaan_xpert_tcm_xdr_amk` → `Observation.component.code.coding` (575)<br>`hasil_pemeriksaan_xpert_tcm_xdr_km` → `Observation.component.code.coding` (580)<br>`hasil_pemeriksaan_xpert_tcm_xdr_cm` → `Observation.component.code.coding` (585)<br>`nama_lengkap_pasien` → `Observation.subject.display` (591)<br>`tgl_mulai_pengobatan` → `Observation.effectiveDateTime` (593)<br>`tanggal_hasil_pemeriksaan_tcmxdr` → `Observation.issued` (594) |
| 25 | 600–609 | DiagnosticReport | X099379 | Pemeriksaan TCM XDR | `tanggal_hasil_pemeriksaan_tcmxdr` → `DiagnosticReport.issued` (605) |
| 26 | 612–621 | ServiceRequest | X099380 | Line Probe Assay (LPA) Lini 1 | – |
| 27 | 623–628 | Specimen | 119334006 | Sputum specimen | – |
| 28 | 630–660 | Observation | X099380 | Line Probe Assay (LPA) Lini 1 | `hasil_pemeriksaan_lpa_line_probe_assay_lini_1_valid_invalid` → `Observation.valueCodeableConcept.coding` (633)<br>_MTB_ → `Observation.component.code.coding` (636, tanpa BQ)<br>`hasil_pemeriksaan_lpa_line_probe_assay_lini_1_mtb` → `Observation.component.valueCodeableConcept.coding` (637)<br>_R_ → `Observation.component.code.coding` (640, tanpa BQ)<br>`hasil_pemeriksaan_lpa_line_probe_assay_lini_1_r` → `Observation.component.valueCodeableConcept.coding` (641)<br>_H_ → `Observation.component.code.coding` (646, tanpa BQ)<br>`hasil_pemeriksaan_lpa_line_probe_assay_lini_1_h` → `Observation.component.valueCodeableConcept.coding` (647)<br>`nama_lengkap_pasien` → `Observation.subject.display` (653)<br>`tgl_mulai_pengobatan` → `Observation.effectiveDateTime` (655)<br>`tgl_mulai_pengobatan` → `Observation.issued` (656) |
| 29 | 662–671 | DiagnosticReport | X099380 | Line Probe Assay (LPA) Lini 1 | – |
| 30 | 673–682 | ServiceRequest | X099381 | Line Probe Assay (LPA) Lini 2 | – |
| 31 | 684–689 | Specimen | 119334006 | Sputum specimen | – |
| 32 | 691–745 | Observation | X099381 | Line Probe Assay (LPA) Lini 2 | `hasil_pemeriksaan_lpa_lini_2_valid_invalid` → `Observation.valueCodeableConcept.coding` (694)<br>`hasil_pemeriksaan_lpa_lini_2_mtb` → `Observation.component.code.coding` (697)<br>`hasil_pemeriksaan_lpa_lini_2_fq_lfx` → `Observation.component.code.coding` (701)<br>`hasil_pemeriksaan_lpa_lini_2_fq_mfx` → `Observation.component.code.coding` (707)<br>`hasil_pemeriksaan_lpa_lini_2_fq_mfx_dt` → `Observation.component.code.coding` (713)<br>`hasil_pemeriksaan_lpa_lini_2_slid_km` → `Observation.component.code.coding` (719)<br>`hasil_pemeriksaan_lpa_lini_2_slid_amk` → `Observation.component.code.coding` (725)<br>`hasil_pemeriksaan_lpa_lini_2_slid_cm` → `Observation.component.code.coding` (731)<br>`nama_lengkap_pasien` → `Observation.subject.display` (738)<br>`tgl_mulai_pengobatan` → `Observation.effectiveDateTime` (740)<br>`tgl_mulai_pengobatan` → `Observation.issued` (741) |
| 33 | 747–756 | DiagnosticReport | X099381 | Line Probe Assay (LPA) Lini 2 | – |
| 34 | 758–767 | ServiceRequest | X099383 | Pemeriksaan Paket Standar Kepekaan | `tanggal_pengambilan_dahak_untuk_uji_kepekaan_hhbbtttt` → `ServiceRequest.occurrenceDateTime` (765) |
| 35 | 769–775 | Specimen | 119334006 | Sputum specimen | `tanggal_pengambilan_dahak_untuk_uji_kepekaan_hhbbtttt` → `Specimen.collection.collectedDateTime` (772)<br>`nama_lengkap_pasien` → `Specimen.subject.display` (774)<br>`tanggal_pengambilan_dahak_untuk_uji_kepekaan_hhbbtttt` → `Specimen.receivedTime` (775) |
| 36 | 777–846 | Observation | X099383 | Pemeriksaan Paket Standar Kepekaan | `hasil_pemeriksaan_paket_standar_uji_kepekaan_h_dosis_tinggi` → `Observation.component.code.coding` (782)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_h` → `Observation.component.code.coding` (788)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_km` → `Observation.component.code.coding` (794)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_cm` → `Observation.component.code.coding` (800)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_lfx` → `Observation.component.code.coding` (806)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_mfx_dosis_tinggi` → `Observation.component.code.coding` (812)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_mfx` → `Observation.component.code.coding` (818)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan` → `Observation.component.code.coding` (824)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_1` → `Observation.component.code.coding` (826)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_2` → `Observation.component.code.coding` (828)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_3` → `Observation.component.code.coding` (830)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_4` → `Observation.component.code.coding` (832)<br>`hasil_pemeriksaan_paket_standar_uji_kepekaan_5` → `Observation.component.code.coding` (834)<br>`nama_lengkap_pasien` → `Observation.subject.display` (839)<br>`tgl_mulai_pengobatan` → `Observation.effectiveDateTime` (841)<br>`tanggal_hasil_uji_kepekaan_keluar_hhbbtttt` → `Observation.issued` (842) |
| 37 | 848–857 | DiagnosticReport | X099383 | Pemeriksaan Paket Standar Kepekaan | `tanggal_hasil_uji_kepekaan_keluar_hhbbtttt` → `DiagnosticReport.issued` (853) |
| 38 | 859–868 | ServiceRequest | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | – |
| 39 | 870–875 | Specimen | 119334006 | Sputum specimen | – |
| 40 | 877–922 | Observation | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | _BTA_ → `Observation.valueCodeableConcept.coding` (881, tanpa BQ)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__1_bta` → `Observation.valueCodeableConcept.coding` (887)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__2_bta` → `Observation.valueCodeableConcept.coding` (888)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__3_bta` → `Observation.valueCodeableConcept.coding` (889)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__4_bta` → `Observation.valueCodeableConcept.coding` (890)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__4_bta_2` → `Observation.valueCodeableConcept.coding` (891)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__5_bta` → `Observation.valueCodeableConcept.coding` (892)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__5_bta2` → `Observation.valueCodeableConcept.coding` (893)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__6_bta` → `Observation.valueCodeableConcept.coding` (894)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__6_bta2` → `Observation.valueCodeableConcept.coding` (895)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__7_bta` → `Observation.valueCodeableConcept.coding` (896)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__8_bta` → `Observation.valueCodeableConcept.coding` (897)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__9_bta` → `Observation.valueCodeableConcept.coding` (898)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__10_bta` → `Observation.valueCodeableConcept.coding` (899)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__11_bta` → `Observation.valueCodeableConcept.coding` (900)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__12_bta` → `Observation.valueCodeableConcept.coding` (901)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__13_bta` → `Observation.valueCodeableConcept.coding` (902)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__14_bta` → `Observation.valueCodeableConcept.coding` (903)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__15_bta` → `Observation.valueCodeableConcept.coding` (904)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__16_bta` → `Observation.valueCodeableConcept.coding` (905)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__17_bta` → `Observation.valueCodeableConcept.coding` (906)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__18_bta` → `Observation.valueCodeableConcept.coding` (907)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__19_bta` → `Observation.valueCodeableConcept.coding` (908)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__20_bta` → `Observation.valueCodeableConcept.coding` (909)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__21_bta` → `Observation.valueCodeableConcept.coding` (910)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__22_bta` → `Observation.valueCodeableConcept.coding` (911)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__23_bta` → `Observation.valueCodeableConcept.coding` (912)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__24_bta` → `Observation.valueCodeableConcept.coding` (913)<br>`nama_lengkap_pasien` → `Observation.subject.display` (915)<br>`tgl_mulai_pengobatan` → `Observation.effectiveDateTime` (917) |
| 41 | 924–933 | DiagnosticReport | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | – |
| 42 | 935–944 | ServiceRequest | X099388 | Biakan TB | – |
| 43 | 946–951 | Specimen | 119334006 | Sputum specimen | – |
| 44 | 953–999 | Observation | X099388 | Biakan TB | _Biakan_ → `Observation.identifier` (953, tanpa BQ)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__1_b` → `Observation.valueCodeableConcept.coding` (964)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__2_b` → `Observation.valueCodeableConcept.coding` (965)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__3_b` → `Observation.valueCodeableConcept.coding` (966)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__4_b` → `Observation.valueCodeableConcept.coding` (967)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__4_b_2` → `Observation.valueCodeableConcept.coding` (968)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__5_b` → `Observation.valueCodeableConcept.coding` (969)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__5_b2` → `Observation.valueCodeableConcept.coding` (970)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__6_b` → `Observation.valueCodeableConcept.coding` (971)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__6_b2` → `Observation.valueCodeableConcept.coding` (972)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__7_b` → `Observation.valueCodeableConcept.coding` (973)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__8_b` → `Observation.valueCodeableConcept.coding` (974)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__9_b` → `Observation.valueCodeableConcept.coding` (975)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__10_b` → `Observation.valueCodeableConcept.coding` (976)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__11_b` → `Observation.valueCodeableConcept.coding` (977)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__12_b` → `Observation.valueCodeableConcept.coding` (978)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__13_b` → `Observation.valueCodeableConcept.coding` (979)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__14_b` → `Observation.valueCodeableConcept.coding` (980)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__15_b` → `Observation.valueCodeableConcept.coding` (981)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__16_b` → `Observation.valueCodeableConcept.coding` (982)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__17_b` → `Observation.valueCodeableConcept.coding` (983)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__18_b` → `Observation.valueCodeableConcept.coding` (984)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__19_b` → `Observation.valueCodeableConcept.coding` (985)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__20_b` → `Observation.valueCodeableConcept.coding` (986)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__21_b` → `Observation.valueCodeableConcept.coding` (987)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__22_b` → `Observation.valueCodeableConcept.coding` (988)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__23_b` → `Observation.valueCodeableConcept.coding` (989)<br>`pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__24_b` → `Observation.valueCodeableConcept.coding` (990)<br>`tgl_mulai_pengobatan` → `Observation.effectiveDateTime` (994)<br>`tgl_mulai_pengobatan` → `Observation.issued` (995) |
| 45 | 1001–1010 | DiagnosticReport | X099388 | Biakan TB | – |
| 46 | 1013–1024 | Observation | 365866002 | Finding of human immunodeficiency virus status | `kegiatan_tbchiv_hasil_tes_hiv` → `Observation.valueCodeableConcept.coding` (1016)<br>`nama_lengkap_pasien` → `Observation.subject.display` (1019)<br>`tgl_mulai_pengobatan` → `Observation.effectiveDateTime` (1021) |
| 47 | 1026–1036 | Procedure | SP000371 | Cotrimoxazole | `kegiatan_tbchiv_kotrimoksasol` → `Procedure.category.coding` (1026)<br>`nama_lengkap_pasien` → `Procedure.subject.display` (1031)<br>`tgl_mulai_pengobatan` → `Procedure.performedPeriod.start` (1033)<br>`tgl_mulai_pengobatan` → `Procedure.performedPeriod.end` (1034) |
| 48 | 1038–1048 | Procedure | SP000046 | Terapi Antiretroviral (ART) | `kegiatan_tbchiv_art` → `Procedure.category.coding` (1038)<br>`nama_lengkap_pasien` → `Procedure.subject.display` (1043)<br>`tgl_mulai_pengobatan` → `Procedure.performedPeriod.start` (1045)<br>`tgl_mulai_pengobatan` → `Procedure.performedPeriod.end` (1046) |
| 49 | 1050–1061 | Observation | SP000047 | Hasil Tes Diabetes Melitus | `kegiatan_tbcdm_dm` → `Observation.valueCodeableConcept.coding` (1053)<br>`nama_lengkap_pasien` → `Observation.subject.display` (1056)<br>`tgl_mulai_pengobatan` → `Observation.effectiveDateTime` (1058)<br>`tgl_mulai_pengobatan` → `Observation.issued` (1059) |
| 50 | 1063–1074 | Observation | 1284985006 | Diabetes mellitus management program | `kegiatan_tbcdm_terapi_dm` → `Observation.valueCodeableConcept.coding` (1066)<br>`nama_lengkap_pasien` → `Observation.subject.display` (1069)<br>`tgl_mulai_pengobatan` → `Observation.effectiveDateTime` (1071)<br>`tgl_mulai_pengobatan` → `Observation.issued` (1072) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 18 |
| ServiceRequest | 7 |
| Specimen | 7 |
| DiagnosticReport | 7 |
| Procedure | 3 |
| Organization | 1 |
| Patient | 1 |
| EpisodeOfCare | 1 |
| Coverage | 1 |
| Encounter | 1 |
| Condition | 1 |
| QuestionnaireResponse | 1 |
| CarePlan | 1 |
| **Total** | **50** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 5 | Organization | `Organization.type` | SP000367 | Kementerian Kesehatan | http://terminology.kemkes.go.id/CodeSystem/organization-ownership |
| 2 | 6 | Organization | `Organization.type` | SP000368 | Pemerintah Daerah Kabupaten/Kota | http://terminology.kemkes.go.id/CodeSystem/organization-ownership |
| 3 | 56 | EpisodeOfCare | `EpisodeOfCare.type.coding` | TB-RO | Tuberkulosis Resisten Obat | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 4 | 82 | Encounter | `Encounter.hospitalization.admitSource.coding` | EHA000002 | Datang sendiri | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 5 | 83 | Encounter | `Encounter.hospitalization.admitSource.coding` | EHA000003 | Kegiatan ACF | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 6 | 84 | Encounter | `Encounter.hospitalization.admitSource.coding` | 257622000 | Healthcare facility | http://snomed.info/sct |
| 7 | 85 | Encounter | `Encounter.hospitalization.admitSource.coding` | EHA000004 | Skrining TBC DM | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 8 | 86 | Encounter | `Encounter.hospitalization.admitSource.coding` | EHA000005 | Pemadanan Data BPJS | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 9 | 87 | Encounter | `Encounter.hospitalization.admitSource.coding` | 225368008 | Contact tracing | http://snomed.info/sct |
| 10 | 88 | Encounter | `Encounter.hospitalization.admitSource.coding` | EHA000002 | Datang sendiri | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 11 | 117 | Condition | `Condition.code.coding` | A15.0 | Tuberculosis of lung, confirmed by sputum microscopy with or without culture | http://hl7.org/fhir/sid/icd-10 |
| 12 | 118 | Condition | `Condition.code.coding` | A16.2 | Tuberculosis of lung, without mention of bacteriological or histological confirmation | http://hl7.org/fhir/sid/icd-10 |
| 13 | 126 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 14 | 139 | Observation | `Observation.code.coding` | 85658-3 | Occupation [Type] | http://loinc.org |
| 15 | 140 | Observation | `Observation.valueCodeableConcept.coding` | 106540006 | Laborer | http://snomed.info/sct |
| 16 | 141 | Observation | `Observation.valueCodeableConcept.coding` | 106304008 | Teacher | http://snomed.info/sct |
| 17 | 142 | Observation | `Observation.valueCodeableConcept.coding` | 106304008 | Teacher | http://snomed.info/sct |
| 18 | 143 | Observation | `Observation.valueCodeableConcept.coding` | 106305009 | University/higher education teacher | http://snomed.info/sct |
| 19 | 144 | Observation | `Observation.valueCodeableConcept.coding` | 444168002 | Homemaker | http://snomed.info/sct |
| 20 | 145 | Observation | `Observation.valueCodeableConcept.coding` | OV000430 | Pegawai Swasta/ BUMN/ BUMD | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 21 | 146 | Observation | `Observation.valueCodeableConcept.coding` | 65853000 | Student | http://snomed.info/sct |
| 22 | 147 | Observation | `Observation.valueCodeableConcept.coding` | 106386007 | Agricultural animal husbandry/forestry worker, fisherman/hunter | http://snomed.info/sct |
| 23 | 148 | Observation | `Observation.valueCodeableConcept.coding` | 106388008 | Farmer | http://snomed.info/sct |
| 24 | 149 | Observation | `Observation.valueCodeableConcept.coding` | 36625000 | Livestock worker | http://snomed.info/sct |
| 25 | 150 | Observation | `Observation.valueCodeableConcept.coding` | 77715000 | Fisherman | http://snomed.info/sct |
| 26 | 151 | Observation | `Observation.valueCodeableConcept.coding` | 236297007 | Civil servant | http://snomed.info/sct |
| 27 | 152 | Observation | `Observation.valueCodeableConcept.coding` | OV000431 | Siswa Berasrama | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 28 | 153 | Observation | `Observation.valueCodeableConcept.coding` | 236320001 | Vehicle driver (occupation) | http://snomed.info/sct |
| 29 | 154 | Observation | `Observation.valueCodeableConcept.coding` | 223366009 | Healthcare professional (occupation) | http://snomed.info/sct |
| 30 | 155 | Observation | `Observation.valueCodeableConcept.coding` | OV000432 | Tenaga Profesional Nonmedis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 31 | 156 | Observation | `Observation.valueCodeableConcept.coding` | OV000433 | TNI/ Polri | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 32 | 157 | Observation | `Observation.valueCodeableConcept.coding` | OV000434 | Warga Binaan Pemasyarakatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 33 | 158 | Observation | `Observation.valueCodeableConcept.coding` | 160906004 | Self-employed | http://snomed.info/sct |
| 34 | 159 | Observation | `Observation.valueCodeableConcept.coding` | 741062008 | Not in labor force | http://snomed.info/sct |
| 35 | 160 | Observation | `Observation.valueCodeableConcept.coding` | 261665006 | Unknown | http://snomed.info/sct |
| 36 | 161 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 37 | 162 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 38 | 174 | Observation | `Observation.code.coding` | 82810-3 | Pregnancy status | http://loinc.org |
| 39 | 175 | Observation | `Observation.valueCodeableConcept.coding` | LA15173-0 | Pregnant | http://loinc.org |
| 40 | 176 | Observation | `Observation.valueCodeableConcept.coding` | LA26683-5 | Not Pregnant | http://loinc.org |
| 41 | 177 | Observation | `Observation.dataAbsentReason.coding` | unknown | Unknown | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 42 | 188 | Observation | `Observation.code.coding` | 225368008 | Contact tracing | http://snomed.info/sct |
| 43 | 213 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | QRI000001 | Terduga TBC SO | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 44 | 214 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | QRI000002 | Terduga TBC RO | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 45 | 217 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | new | Kasus Baru | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 46 | 218 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | relapse | Kasus Kambuh | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 47 | 219 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure-cat1 | Kasus Pengobatan Setelah Gagal Kategori 1 | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 48 | 220 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure-cat2 | Kasus Pengobatan Setelah Gagal Kategori 2 | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 49 | 221 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | loss-to-follow-up | Kasus Setelah Loss To Follow Up | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 50 | 222 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure-2line | Kasus Pengobatan Setelah Gagal lini 2 | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 51 | 223 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | not-eval | Pernah diobati tidak diketahui hasilnya | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 52 | 224 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | unknown | Kasus dengan riwayat pengobatan tidak diketahui | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 53 | 225 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | other | Kasus lain-lain | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 54 | 226 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure | Kasus Pengobatan Setelah Gagal | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 55 | 229 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure-cat2 | Kasus Pengobatan Setelah Gagal Kategori 2 | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 56 | 230 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | treatment-non-conversion-2 | Pasien TB pengobatan kategori 2 yang tidak konversi setelah 3 bulan pengobatan | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 57 | 231 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | non-standard-treatment | Pasien TB yang mempunyai riwayat pengobatan TB yang tidak standar | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 58 | 232 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure-cat1 | Kasus Pengobatan Setelah Gagal Kategori 1 | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 59 | 233 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | treatment-non-conversion-1 | Pasien TB pengobatan kategori 1 yang tidak konversi | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 60 | 234 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | relapse | Kasus Baru | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 61 | 235 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | loss-to-follow-up | Kasus Setelah Loss To Follow Up | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 62 | 236 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | history-of-close-contact with-TB-DR | Terduga TB yang mempunyai riwayat kontak erat dengan pasien TB RO | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 63 | 237 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | co-infected-TBHIV | Pasien ko-infeksi TB-HIV yang tidak respons secara klinis maupun bakteriologis terhadap pemberian OAT | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 64 | 238 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | failure-2line | Kasus Pengobatan Setelah Gagal lini 2 | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 65 | 239 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TB-DR-relapse | Pasien TB RO kasus kambuh | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 66 | 240 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | TB-DR-returns | Pasien TB RO yang kembali setelah putus berobat | http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment |
| 67 | 243 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 154283005 | Pulmonary tuberculosis | http://snomed.info/sct |
| 68 | 244 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 423997002 | Tuberculosis, extrapulmonary | http://snomed.info/sct |
| 69 | 248 | Observation | `Observation.code.coding` | 33248-6 | Diabetes status | http://loinc.org |
| 70 | 249 | Observation | `Observation.valueCodeableConcept.coding` | 10828004 | Positive | http://snomed.info/sct |
| 71 | 250 | Observation | `Observation.valueCodeableConcept.coding` | 260385009 | Negative | http://snomed.info/sct |
| 72 | 251 | Observation | `Observation.valueCodeableConcept.coding` | 261665006 | Unknown | http://snomed.info/sct |
| 73 | 262 | Observation | `Observation.code.coding` | 55277-8 | HIV status | http://loinc.org |
| 74 | 263 | Observation | `Observation.valueCodeableConcept.coding` | 10828004 | Positive | http://snomed.info/sct |
| 75 | 264 | Observation | `Observation.valueCodeableConcept.coding` | 260385009 | Negative | http://snomed.info/sct |
| 76 | 265 | Observation | `Observation.valueCodeableConcept.coding` | 261665006 | Unknown | http://snomed.info/sct |
| 77 | 275 | Procedure | `Procedure.code.coding` | 424489006 | Mantoux test | http://snomed.info/sct |
| 78 | 277 | Procedure | `Procedure.code.coding` | 35140007 | Interferon gamma assay | http://snomed.info/sct |
| 79 | 279 | Procedure | `Procedure.code.coding` | 424489006 | Mantoux test | http://snomed.info/sct |
| 80 | 281 | Procedure | `Procedure.code.coding` | 35140007 | Interferon gamma assay | http://snomed.info/sct |
| 81 | 293 | Observation | `Observation.code.coding` | 23539-0 | Tuberculosis reaction wheal [Diameter] --3 days post dose mammalian tuberculin intradermal | http://loinc.org |
| 82 | 294 | Observation | `Observation.valueCodeableConcept.coding` | 268376005 | Mantoux: positive | http://snomed.info/sct |
| 83 | 295 | Observation | `Observation.valueCodeableConcept.coding` | 268375009 | Mantoux: negative | http://snomed.info/sct |
| 84 | 296 | Observation | `Observation.code.coding` | 71773-6 | Mycobacterium tuberculosis stimulated gamma interferon [Interpretation] in Blood Qualitative | http://loinc.org |
| 85 | 297 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 86 | 298 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 87 | 299 | Observation | `Observation.code.coding` | 23539-0 | Tuberculosis reaction wheal [Diameter] --3 days post dose mammalian tuberculin intradermal | http://loinc.org |
| 88 | 300 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 89 | 301 | Observation | `Observation.code.coding` | 71773-6 | Mycobacterium tuberculosis stimulated gamma interferon [Interpretation] in Blood Qualitative | http://loinc.org |
| 90 | 302 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 91 | 313 | Observation | `Observation.code.coding` | 24648-8 | XR Chest PA upright | http://loinc.org |
| 92 | 314 | Observation | `Observation.valueCodeableConcept.coding` | 17621005 | Normal | http://snomed.info/sct |
| 93 | 315 | Observation | `Observation.valueCodeableConcept.coding` | 2483006 | Cavity | http://snomed.info/sct |
| 94 | 316 | Observation | `Observation.valueCodeableConcept.coding` | 27925004 | Nodule | http://snomed.info/sct |
| 95 | 317 | Observation | `Observation.valueCodeableConcept.coding` | 1255665007 | Moderate | http://snomed.info/sct |
| 96 | 318 | Observation | `Observation.valueCodeableConcept.coding` | 47604008 | Miliary tuberculosis | http://snomed.info/sct |
| 97 | 319 | Observation | `Observation.valueCodeableConcept.coding` | 30746006 | Lymphadenopathy | http://snomed.info/sct |
| 98 | 320 | Observation | `Observation.valueCodeableConcept.coding` | 260544000 | Endobronchial (qualifier value) | http://snomed.info/sct |
| 99 | 321 | Observation | `Observation.valueCodeableConcept.coding` | 112674009 | Fibrosis | http://snomed.info/sct |
| 100 | 322 | Observation | `Observation.valueCodeableConcept.coding` | 442110002 | Fibrosis of pleura | http://snomed.info/sct |
| 101 | 323 | Observation | `Observation.valueCodeableConcept.coding` | 1303092009 | Pulmonary bulla | http://snomed.info/sct |
| 102 | 324 | Observation | `Observation.valueCodeableConcept.coding` | 60046008 | Pleural effusion | http://snomed.info/sct |
| 103 | 325 | Observation | `Observation.valueCodeableConcept.coding` | 36118008 | Pneumothorax | http://snomed.info/sct |
| 104 | 326 | Observation | `Observation.valueCodeableConcept.coding` | 12295008 | Bronchiectasis | http://snomed.info/sct |
| 105 | 327 | Observation | `Observation.valueCodeableConcept.coding` | 46621007 | Atelectasis | http://snomed.info/sct |
| 106 | 328 | Observation | `Observation.valueCodeableConcept.coding` | 9656002 | Consolidation | http://snomed.info/sct |
| 107 | 329 | Observation | `Observation.valueCodeableConcept.coding` | 309529002 | Lung mass | http://snomed.info/sct |
| 108 | 330 | Observation | `Observation.valueCodeableConcept.coding` | 385633008 | Improving | http://snomed.info/sct |
| 109 | 331 | Observation | `Observation.valueCodeableConcept.coding` | 230993007 | Worsening | http://snomed.info/sct |
| 110 | 332 | Observation | `Observation.valueCodeableConcept.coding` | 58158008 | Stable | http://snomed.info/sct |
| 111 | 357 | CarePlan | `CarePlan.activity.detail.code.coding` | CP000006 | Paduan OAT | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 112 | 358 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000007 | OAT Kategori 1 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 113 | 359 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000008 | OAT Kategori 2 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 114 | 360 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000009 | OAT Kategori Anak | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 115 | 361 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000010 | OAT Paduan tidak standar TB SO | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 116 | 362 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000011 | OAT Paduan Jangka Pendek | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 117 | 363 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000012 | OAT Paduan Jangka Panjang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 118 | 364 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000013 | OAT Paduan Individual | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 119 | 365 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000014 | OAT Paduan Monoresistan INH | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 120 | 368 | CarePlan | `CarePlan.activity.detail.code.coding` | CP000005 | Paduan Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 121 | 369 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000015 | 2(HRZE)/4(HR)3 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 122 | 370 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000016 | 2(HRZE)/4(HR) - KDT Dosis Harian | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 123 | 371 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000017 | 2(HRZE)S/(HRZE)/5(HRE) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 124 | 372 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000018 | 2(HRZE)S/(HRZE)/5((HR)3E3) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 125 | 373 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000019 | 2HRZE/4HR | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 126 | 374 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000020 | 2HRZES/HRZE/ 5H3R3E3 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 127 | 375 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000021 | 2(HRZ)/4(HR) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 128 | 376 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000022 | 2(HRZ)/4(HR) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 129 | 377 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000023 | Km Cs Eto Lfx Z VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 130 | 378 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000024 | Km Cs Eto Lfx PAS E Z VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 131 | 379 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000025 | Km Cs Eto Lfx E Z VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 132 | 380 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000026 | Km Cs Eto Mfx PAS Z VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 133 | 381 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000027 | Km Cs Eto Mfx PAS E VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 134 | 382 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000028 | Cm Cs Eto Lfx E Z Vit B6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 135 | 383 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000029 | Cm Cs Eto Lfx PAS Z VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 136 | 384 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000030 | Cm Cs Eto Mfx Z VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 137 | 385 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000031 | Cm Cs Eto Mfx PAS Z VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 138 | 386 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000032 | Km Eto Cs PAS Z Bdq | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 139 | 387 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000033 | Lfx Eto Cs PAS Z Bdq | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 140 | 388 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000034 | Eto Cs PAS Z Bdq Lnz Clf | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 141 | 389 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000035 | Km Lfx (Eto/CS/PAS) Z Bdq (Lnz/Clf) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 142 | 390 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000036 | 5 Km Mfx(h) Eto Cfz Z H(h) E/ 5Mfx(h) Cfz Z E | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 143 | 391 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000037 | 6 Dlm Lfx Eto Cs ZE B6/ 18 Lfx Eto Cs ZE B6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 144 | 392 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000038 | 10 Cm Dlm Lzd Eto Cs Z E B6/14 Lzd Eto Cs Z E B6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 145 | 393 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000039 | 6 Dlm Lzd Cfz Eto Cs PAS ZE B6/ 18 lzd Cfz Eto Cs PAS Z E B6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 146 | 394 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000040 | Etambutol | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 147 | 395 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000041 | Paduan TPT 6Lfx 250 mg + E 400 mg Dewasa | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 148 | 396 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000042 | 6 Bdq-Lfx-Lzd-Cfz-Cs-VitB6 / 14 Lfx-Cfz-Cs-VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 149 | 397 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000043 | 6 Bdq-Lfx-Cfz-Cs-E -VitB6/ 14 Lfx-Cfz-Cs-E-VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 150 | 398 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000044 | 6 Bdq-Lfx-Lzd-Cfz-E / 14 Lfx-Cfz-E | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 151 | 399 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000045 | 6 Bdq-Mfx-Lzd-Cfz-E / 14 Mfx-Cfz-E | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 152 | 400 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000046 | 6 Bdq-Lzd-Cfz-Cs-E-VitB6 / 14 Lzd-Cfz-Cs-E -VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 153 | 401 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000047 | 6 Bdq-Lzd-Cfz-Cs-Eto / 14 Lzd-Cfz-Cs-Eto- Vit B6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 154 | 402 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000048 | 6 Dlm-Lfx-Lzd-Clz-Cs / 14 Lfx-Lzd-Clz-Cs -VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 155 | 403 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000049 | 20 Lfx-Lzd-Cfz-Cs-Eto -VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 156 | 404 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000050 | 20 Mfx-Lzd-Cfz-Cs-E -VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 157 | 405 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000051 | 20 Mfx-Lzd-Cfz-Cs-Z -VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 158 | 406 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000052 | 6 Lfx-Lzd-Cfz-Cs-Amk-VitB6 / 14 Lfx-Lzd-Clz-Cs-VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 159 | 407 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000053 | 6 Lfx-Lzd-Cfz-Cs-S-VitB6 / 14 Lfx-Lzd-Clz-Cs-VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 160 | 408 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000054 | 6 Lfx-Lzd-Cfz-Eto-PAS / 14 Lfx-Lzd-Clz-Eto | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 161 | 409 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000055 | 6 Dlm-Lzd-Cfz-Cs-E / 14 Lzd-Clz-Cs-E-Vit B6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 162 | 410 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000056 | Pro TB 3 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 163 | 411 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000057 | 6 Bdq-Lfx-Lzd-Cfz-H(Hdose)-Z-E/5 Lfx-Cfz-Z-E | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 164 | 412 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000058 | 6 Dlm-Lzd-Cfz-Cs-E / 14 Lzd-Clz-Cs-E-Vit B6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 165 | 413 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000059 | 6 Dlm-Lfx-Lzd-Clz-Cs / 14 Lfx-Lzd-Clz-Cs -VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 166 | 414 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000060 | 6 Bdq-Lfx-Eto-E-Z-Hh-Cfz/ 5 Lfx)-Cfz-Z-E (STR Non Inj) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 167 | 415 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000061 | 6 Bdq-Mfx-Eto-E-Z-Hh-Cfz/ 5-Mfx-Cfz-Z-E (STR Non Inj) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 168 | 416 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000062 | Paduan TPT 6H 100 mg (INH) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 169 | 417 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000063 | Paduan TPT 3HP Lepasan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 170 | 418 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000064 | Paduan TPT 6H 300 mg (INH) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 171 | 419 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000065 | Paduan TPT 6Lfx 250mg | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 172 | 420 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000066 | Paduan TPT 3HR KDT | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 173 | 421 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000067 | Paduan TPT 3HR KDT | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 174 | 422 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000068 | 5 Lfx-Lzd-Cfz-Cs / 5 Lfx-Cfz-Cs | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 175 | 423 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000069 | 6 Lfx-Lzd-Cfz-Cs-Eto / 12 Lfx-Cfz-Cs-Eto | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 176 | 424 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000070 | 6 Lzd-Cfz-Cs-Eto / 5 Cfz-Cs-Eto | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 177 | 425 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000071 | 6 Lzd-Cfz-Cs-Eto / 12 Cfz-Cs-Eto | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 178 | 426 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000072 | 5 Lfx-Lzd-Cfz-Cs-Dlm / 5 Lfx-Cfz-Cs | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 179 | 427 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000073 | 6 Lfx-Lzd-Cfz-Cs-Dlm / 12 Lfx-Cfz-Cs | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 180 | 428 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000074 | 5 Lzd-Cfz-Cs-Dlm-Eto/5 Cfz-Cs-Eto | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 181 | 429 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000075 | 6 Lzd-Cfz-Cs-Dlm-Eto/ 12 Cfz-Cs-Eto | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 182 | 430 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000076 | 6 Bdq-Lfx-Lzd-Cfz-Cs / 5 Lfx-Cfz- Cs | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 183 | 431 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000077 | 6 Bdq-Lfx-Lzd-Cfz-Cs / 12 Lfx-Cfz-Cs | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 184 | 432 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000078 | 6 Bdq-Lzd-Cfz-Cs-PAS / 5 Cfz-Cs-PAS | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 185 | 433 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000079 | 6 Bdq-Lzd-Cfz-Cs- PAS / 12 Cfz-Cs-PAS | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 186 | 434 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000080 | Paduan TPT 6Lfx 100 mg + E 100 mg | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 187 | 435 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000081 | Paduan TPT 6Lfx 100mg | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 188 | 436 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000082 | Paduan TPT 3HR 300mg/450mg Lepasan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 189 | 437 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000083 | Paduan TPT 3HR 300mg/600mg Lepasan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 190 | 438 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000084 | RHZE (150/75/400/275) + Levofloxacin | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 191 | 439 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000085 | Bedaquline Pretomanid Linezolid (BPAL) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 192 | 440 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000086 | Bedaquline Pretomanid Linezolid Moxifloxacin (BPALM) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 193 | 441 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000087 | Paduan TPT 1HP 300mg/300mg Lepasan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 194 | 442 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000088 | Paduan TPT 1HP 300mg/150mg Lepasan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 195 | 443 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000089 | 6 BDQ-Lfx-Cfz-Hdt-Z-E-Lzd(2 bulan)/ 5 Lfx-Cfz-Z-E | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 196 | 444 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000090 | 2HPMZ/2HPM | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 197 | 445 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000016 | 2(HRZE)/4(HR) - KDT Dosis Harian | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 198 | 446 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000086 | Bedaquline Pretomanid Linezolid Moxifloxacin (BPALM) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 199 | 447 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000084 | RHZE (150/75/400/275) + Levofloxacin | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 200 | 448 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | SP001137 | Paduan lainnya | http://terminology.kemkes.go.id/sp |
| 201 | 450 | CarePlan | `CarePlan.activity.outcomeCodeableConcept.coding` | 371001000 | Patient cured | http://snomed.info/sct |
| 202 | 451 | CarePlan | `CarePlan.activity.outcomeCodeableConcept.coding` | 182992009 | Treatment completed | http://snomed.info/sct |
| 203 | 452 | CarePlan | `CarePlan.activity.outcomeCodeableConcept.coding` | CP000094 | Pengobatan Gagal | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 204 | 453 | CarePlan | `CarePlan.activity.outcomeCodeableConcept.coding` | 419099009 | Dead | http://snomed.info/sct |
| 205 | 454 | CarePlan | `CarePlan.activity.outcomeCodeableConcept.coding` | 399307001 | Lost to follow-up | http://snomed.info/sct |
| 206 | 455 | CarePlan | `CarePlan.activity.outcomeCodeableConcept.coding` | CP000096 | Tidak dievaluasi/pindah | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 207 | 463 | ServiceRequest | `ServiceRequest.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 208 | 471 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 209 | 479 | Observation | `Observation.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 210 | 480 | Observation | `Observation.code.coding` | 89371-9 | MTB complex DNA and rpoB RIF resistance mutation panel [Presence] | http://loinc.org |
| 211 | 481 | Observation | `Observation.code.coding` | X099379 | Pemeriksaan TCM XDR | http://terminology.kemkes.go.id/CodeSystem/examination |
| 212 | 482 | Observation | `Observation.code.coding` | X099380 | Line Probe Assay (LPA) Lini 1 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 213 | 483 | Observation | `Observation.code.coding` | X099381 | Line Probe Assay (LPA) Lini 2 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 214 | 484 | Observation | `Observation.code.coding` | X099388 | Biakan TB | http://terminology.kemkes.go.id/CodeSystem/examination |
| 215 | 485 | Observation | `Observation.code.coding` | X099383 | Pemeriksaan Paket Standar Kepekaan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 216 | 486 | Observation | `Observation.code.coding` | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 217 | 487 | Observation | `Observation.code.coding` | MK099927 | Pemeriksaan PCR Open System | http://terminology.kemkes.go.id/CodeSystem/examination |
| 218 | 488 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 219 | 489 | Observation | `Observation.valueCodeableConcept.coding` | X099770 | Rifampisin sensitive | http://terminology.kemkes.go.id/CodeSystem/examination |
| 220 | 490 | Observation | `Observation.valueCodeableConcept.coding` | X099771 | Rifampisin resistan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 221 | 491 | Observation | `Observation.valueCodeableConcept.coding` | X099772 | Rifampisin indeterminate | http://terminology.kemkes.go.id/CodeSystem/examination |
| 222 | 492 | Observation | `Observation.dataAbsentReason.coding` | LA15841-2 | Invalid result | http://loinc.org |
| 223 | 493 | Observation | `Observation.dataAbsentReason.coding` | error | Error | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 224 | 494 | Observation | `Observation.dataAbsentReason.coding` | OD000001 | Tidak ada hasil | http://terminology.kemkes.go.id/CodeSystem/data-absent-reason |
| 225 | 495 | Observation | `Observation.dataAbsentReason.coding` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 226 | 508 | DiagnosticReport | `DiagnosticReport.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 227 | 522 | ServiceRequest | `ServiceRequest.code.coding` | X099379 | Pemeriksaan TCM XDR | http://terminology.kemkes.go.id/CodeSystem/examination |
| 228 | 530 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 229 | 538 | Observation | `Observation.code.coding` | X099379 | Pemeriksaan TCM XDR | http://terminology.kemkes.go.id/CodeSystem/examination |
| 230 | 539 | Observation | `Observation.valueCodeableConcept.coding` | X099781 | Hasil Valid | http://terminology.kemkes.go.id/CodeSystem/examination |
| 231 | 540 | Observation | `Observation.dataAbsentReason.coding` | LA15841-2 | Invalid result | http://loinc.org |
| 232 | 541 | Observation | `Observation.dataAbsentReason.coding` | error | Error | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 233 | 542 | Observation | `Observation.dataAbsentReason.coding` | OD000001 | Tidak ada hasil | http://terminology.kemkes.go.id/CodeSystem/data-absent-reason |
| 234 | 544 | Observation | `Observation.component.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 235 | 545 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 236 | 547 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 237 | 549 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 238 | 551 | Observation | `Observation.component.code.coding` | X099391 | H Dosis Rendah (Low) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 239 | 552 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 240 | 553 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 241 | 554 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 242 | 556 | Observation | `Observation.component.code.coding` | 89488-1 | Isoniazid [Susceptibility] by Genotype method | http://loinc.org |
| 243 | 557 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 244 | 558 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 245 | 559 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 246 | 561 | Observation | `Observation.component.code.coding` | 96110-2 | Ethionamide [Susceptibility] by Genotype method | http://loinc.org |
| 247 | 562 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 248 | 563 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 249 | 565 | Observation | `Observation.component.code.coding` | X099392 | FQ Dosis Rendah (Low) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 250 | 566 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 251 | 567 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 252 | 568 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 253 | 570 | Observation | `Observation.component.code.coding` | 89487-3 | Fluoroquinolone [Susceptibility] by Genotype method | http://loinc.org |
| 254 | 571 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 255 | 572 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 256 | 573 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 257 | 575 | Observation | `Observation.component.code.coding` | 89484-0 | Amikacin [Susceptibility] by Genotype method | http://loinc.org |
| 258 | 576 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 259 | 577 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 260 | 578 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 261 | 580 | Observation | `Observation.component.code.coding` | 89482-4 | Kanamycin [Susceptibility] by Genotype method | http://loinc.org |
| 262 | 581 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 263 | 582 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 264 | 583 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 265 | 585 | Observation | `Observation.component.code.coding` | 89483-2 | Capreomycin [Susceptibility] by Genotype method | http://loinc.org |
| 266 | 586 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 267 | 587 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 268 | 588 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 269 | 602 | DiagnosticReport | `DiagnosticReport.code.coding` | X099379 | Pemeriksaan TCM XDR | http://terminology.kemkes.go.id/CodeSystem/examination |
| 270 | 616 | ServiceRequest | `ServiceRequest.code.coding` | X099380 | Line Probe Assay (LPA) Lini 1 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 271 | 624 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 272 | 632 | Observation | `Observation.code.coding` | X099380 | Line Probe Assay (LPA) Lini 1 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 273 | 633 | Observation | `Observation.valueCodeableConcept.coding` | X099781 | Hasil Valid | http://terminology.kemkes.go.id/CodeSystem/examination |
| 274 | 634 | Observation | `Observation.dataAbsentReason.coding` | LA15841-2 | Invalid result | http://loinc.org |
| 275 | 636 | Observation | `Observation.component.code.coding` | 13956-8 | Mycobacterium tuberculosis DNA [Presence] in Specimen by NAA with probe detection | http://loinc.org |
| 276 | 637 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 277 | 638 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 278 | 640 | Observation | `Observation.component.code.coding` | 89489-9 | rifAMPin [Susceptibility] by Genotype method | http://loinc.org |
| 279 | 641 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 280 | 642 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 281 | 643 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 282 | 644 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 283 | 646 | Observation | `Observation.component.code.coding` | 89488-1 | Isoniazid [Susceptibility] by Genotype method | http://loinc.org |
| 284 | 647 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 285 | 648 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 286 | 649 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 287 | 650 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 288 | 664 | DiagnosticReport | `DiagnosticReport.code.coding` | X099380 | Line Probe Assay (LPA) Lini 1 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 289 | 677 | ServiceRequest | `ServiceRequest.code.coding` | X099381 | Line Probe Assay (LPA) Lini 2 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 290 | 685 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 291 | 693 | Observation | `Observation.code.coding` | X099381 | Line Probe Assay (LPA) Lini 2 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 292 | 694 | Observation | `Observation.valueCodeableConcept.coding` | X099781 | Hasil Valid | http://terminology.kemkes.go.id/CodeSystem/examination |
| 293 | 695 | Observation | `Observation.dataAbsentReason.coding` | LA15841-2 | Invalid result | http://loinc.org |
| 294 | 697 | Observation | `Observation.component.code.coding` | 13956-8 | Mycobacterium tuberculosis DNA [Presence] in Specimen by NAA with probe detection | http://loinc.org |
| 295 | 698 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 296 | 699 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 297 | 701 | Observation | `Observation.component.code.coding` | 20629-2 | levoFLOXacin [Susceptibility] | http://loinc.org |
| 298 | 702 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 299 | 703 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 300 | 704 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 301 | 705 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 302 | 707 | Observation | `Observation.component.code.coding` | 96112-8 | Moxifloxacin [Susceptibility] by Genotype method | http://loinc.org |
| 303 | 708 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 304 | 709 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 305 | 710 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 306 | 711 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 307 | 713 | Observation | `Observation.component.code.coding` | X099775 | Moxifloxacin DT (Mfx DT) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 308 | 714 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 309 | 715 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 310 | 716 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 311 | 717 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 312 | 719 | Observation | `Observation.component.code.coding` | 89482-4 | Kanamycin [Susceptibility] by Genotype method | http://loinc.org |
| 313 | 720 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 314 | 721 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 315 | 722 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 316 | 723 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 317 | 725 | Observation | `Observation.component.code.coding` | 89484-0 | Amikacin [Susceptibility] by Genotype method | http://loinc.org |
| 318 | 726 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 319 | 727 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 320 | 728 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 321 | 729 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 322 | 731 | Observation | `Observation.component.code.coding` | 89483-2 | Capreomycin [Susceptibility] by Genotype method | http://loinc.org |
| 323 | 732 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 324 | 733 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 325 | 734 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 326 | 735 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 327 | 749 | DiagnosticReport | `DiagnosticReport.code.coding` | X099381 | Line Probe Assay (LPA) Lini 2 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 328 | 762 | ServiceRequest | `ServiceRequest.code.coding` | X099383 | Pemeriksaan Paket Standar Kepekaan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 329 | 770 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 330 | 779 | Observation | `Observation.code.coding` | X099383 | Pemeriksaan Paket Standar Kepekaan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 331 | 782 | Observation | `Observation.component.code.coding` | X099776 | H High Dosage [Susceptibility] by Method for Slow-growing mycobacteria | http://terminology.kemkes.go.id/CodeSystem/examination |
| 332 | 783 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 333 | 784 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 334 | 785 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 335 | 786 | Observation | `Observation.component.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 336 | 788 | Observation | `Observation.component.code.coding` | 20383-6 | Isoniazid [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 337 | 789 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 338 | 790 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 339 | 791 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 340 | 792 | Observation | `Observation.component.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 341 | 794 | Observation | `Observation.component.code.coding` | 23609-1 | Kanamycin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 342 | 795 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 343 | 796 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 344 | 797 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 345 | 798 | Observation | `Observation.component.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 346 | 800 | Observation | `Observation.component.code.coding` | 23607-5 | Capreomycin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 347 | 801 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 348 | 802 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 349 | 803 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 350 | 804 | Observation | `Observation.component.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 351 | 806 | Observation | `Observation.component.code.coding` | 53716-7 | levoFLOXacin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 352 | 807 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 353 | 808 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 354 | 809 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 355 | 810 | Observation | `Observation.component.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 356 | 812 | Observation | `Observation.component.code.coding` | X099778 | Moxifloxacin High Dosage [Susceptibility] by Method for Slow-growing mycobacteria | http://terminology.kemkes.go.id/CodeSystem/examination |
| 357 | 813 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 358 | 814 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 359 | 815 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 360 | 816 | Observation | `Observation.component.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 361 | 818 | Observation | `Observation.component.code.coding` | 41502-6 | Moxifloxacin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 362 | 819 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 363 | 820 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 364 | 821 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 365 | 822 | Observation | `Observation.component.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 366 | 824 | Observation | `Observation.component.code.coding` | SP000472 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya | http://terminology.kemkes.go.id/sp |
| 367 | 826 | Observation | `Observation.component.code.coding` | SP000473 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 1 | http://terminology.kemkes.go.id/sp |
| 368 | 828 | Observation | `Observation.component.code.coding` | SP000474 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 2 | http://terminology.kemkes.go.id/sp |
| 369 | 830 | Observation | `Observation.component.code.coding` | SP000475 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 3 | http://terminology.kemkes.go.id/sp |
| 370 | 832 | Observation | `Observation.component.code.coding` | SP000476 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 4 | http://terminology.kemkes.go.id/sp |
| 371 | 834 | Observation | `Observation.component.code.coding` | SP000477 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 5 | http://terminology.kemkes.go.id/sp |
| 372 | 850 | DiagnosticReport | `DiagnosticReport.code.coding` | X099383 | Pemeriksaan Paket Standar Kepekaan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 373 | 863 | ServiceRequest | `ServiceRequest.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 374 | 871 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 375 | 880 | Observation | `Observation.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 376 | 881 | Observation | `Observation.valueCodeableConcept.coding` | 260385009 | Negative | http://snomed.info/sct |
| 377 | 882 | Observation | `Observation.valueCodeableConcept.coding` | LA11841-6 | 1+ | http://loinc.org |
| 378 | 883 | Observation | `Observation.valueCodeableConcept.coding` | LA11842-4 | 2+ | http://loinc.org |
| 379 | 884 | Observation | `Observation.valueCodeableConcept.coding` | LA11843-2 | 3+ | http://loinc.org |
| 380 | 886 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 381 | 926 | DiagnosticReport | `DiagnosticReport.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 382 | 939 | ServiceRequest | `ServiceRequest.code.coding` | X099388 | Biakan TB | http://terminology.kemkes.go.id/CodeSystem/examination |
| 383 | 947 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 384 | 956 | Observation | `Observation.code.coding` | X099388 | Biakan TB | http://terminology.kemkes.go.id/CodeSystem/examination |
| 385 | 957 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 386 | 958 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 387 | 959 | Observation | `Observation.valueCodeableConcept.coding` | LA11841-6 | + | http://loinc.org |
| 388 | 960 | Observation | `Observation.valueCodeableConcept.coding` | LA11842-4 | ++ | http://loinc.org |
| 389 | 961 | Observation | `Observation.valueCodeableConcept.coding` | LA11843-2 | +++ | http://loinc.org |
| 390 | 962 | Observation | `Observation.valueCodeableConcept.coding` | 110379001 | Mycobacterium, non-tuberculosis (organism) | http://snomed.info/sct |
| 391 | 963 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 392 | 1003 | DiagnosticReport | `DiagnosticReport.code.coding` | X099388 | Biakan TB | http://terminology.kemkes.go.id/CodeSystem/examination |
| 393 | 1015 | Observation | `Observation.code.coding` | 365866002 | Finding of human immunodeficiency virus status | http://snomed.info/sct |
| 394 | 1016 | Observation | `Observation.valueCodeableConcept.coding` | 165816005 | Human immunodeficiency virus detected | http://snomed.info/sct |
| 395 | 1017 | Observation | `Observation.valueCodeableConcept.coding` | 165815009 | Human immunodeficiency virus not detected | http://snomed.info/sct |
| 396 | 1027 | Procedure | `Procedure.code.coding` | SP000371 | Cotrimoxazole | http://terminology.kemkes.go.id/sp |
| 397 | 1039 | Procedure | `Procedure.code.coding` | SP000046 | Terapi Antiretroviral (ART) | http://terminology.kemkes.go.id/sp |
| 398 | 1052 | Observation | `Observation.code.coding` | SP000047 | Hasil Tes Diabetes Melitus | http://terminology.kemkes.go.id/sp |
| 399 | 1053 | Observation | `Observation.valueCodeableConcept.coding` | 10828004 | Positive | http://snomed.info/sct |
| 400 | 1054 | Observation | `Observation.valueCodeableConcept.coding` | 260385009 | Negative | http://snomed.info/sct |
| 401 | 1065 | Observation | `Observation.code.coding` | 1284985006 | Diabetes mellitus management program | http://snomed.info/sct |
| 402 | 1066 | Observation | `Observation.valueCodeableConcept.coding` | SP000372 | Obat Hipoglikemik Oral | http://terminology.kemkes.go.id/sp |
| 403 | 1067 | Observation | `Observation.valueCodeableConcept.coding` | 308755006 | Subcutaneous injection of insulin | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://loinc.org | 129 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 103 |
| http://snomed.info/sct | 75 |
| http://terminology.kemkes.go.id/CodeSystem/examination | 41 |
| http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment | 22 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 15 |
| http://terminology.kemkes.go.id/sp | 11 |
| http://terminology.kemkes.go.id/CodeSystem/organization-ownership | 2 |
| http://hl7.org/fhir/sid/icd-10 | 2 |
| http://terminology.kemkes.go.id/CodeSystem/data-absent-reason | 2 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 1 |
| **Total** | **403** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
