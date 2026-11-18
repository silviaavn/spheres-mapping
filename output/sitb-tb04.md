# Output Form: SITB TB 04 (Fasyankes & Rujukan)

Sumber: `mapping/phdt-data-dictionary-sitb-tb04.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-sitb-tb04.csv) · [struktur file mentah](../raw/sitb-tb04-kolom.md)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 69 |
| Code (`jumlah code` = 1) | 579 |
| Code unik (code + CodeSystem) | 85 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 24 |
| Variabel BQ (unik) | 99 |
| Variabel di Excel export | 114 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 5–30 | Patient | – | – | `no_rekam_medis` → `Patient.identifier.value` (8)<br>`nik_nomor_induk_kependudukan` → `Patient.identifier.value` (11)<br>`nama_lengkap_pasien` → `Patient.name.text` (12)<br>`jenis_kelamin` → `Patient.gender` (13)<br>_Provinsi_ → `Patient.address.extension.extension.valueCode` (19, tanpa BQ)<br>_Kabupaten/Kota_ → `Patient.address.extension.extension.valueCode` (22, tanpa BQ)<br>_Kecamatan_ → `Patient.address.extension.extension.valueCode` (25, tanpa BQ)<br>_Kelurahan_ → `Patient.address.extension.extension.valueCode` (28, tanpa BQ)<br>`alamat_lengkap` → `Patient.address.line` (29) |
| 2 | 33–55 | EpisodeOfCare | TB-SO | Tuberkulosis Sensitif Obat | – |
| 3 | 58–85 | Encounter | – | – | `nama_fasilitas_kesehatan_asal_contoh_uji` → `Encounter.hospitalization.origin.reference` (62) 🔎 lookup master data<br>_Nama Fasyankes_ → `Encounter.serviceProvider.reference` (85, tanpa BQ) 🔎 lookup master data |
| 4 | 87–93 | Condition | 171126009 | Tuberculosis screening | – |
| 5 | 96–107 | Observation | 424144002 | Current chronological age | `umur` → `Observation.valueQuantity.value` (99) |
| 6 | 112–140 | ServiceRequest | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | _Pemeriksaan Mikroskopis 1_ → `ServiceRequest.identifier` (112, tanpa BQ)<br>`pemeriksaan_mikroskopis_tgl_contoh_uji_diterima` → `ServiceRequest.occurrenceDateTime` (120)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (121) |
| 7 | 142–161 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (143)<br>`pemeriksaan_mikroskopis_jenis_contoh_uji` → `Specimen.type.coding` (145) |
| 8 | 163–179 | Observation | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | `pemeriksaan_mikroskopis_1_hasil_pemeriksaan` → `Observation.valueCodeableConcept.coding` (167)<br>`pemeriksaan_mikroskopis_1_tgl_hasil_dilaporkan` → `Observation.issued` (177) |
| 9 | 181–193 | DiagnosticReport | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | – |
| 10 | 195–223 | ServiceRequest | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | _Pemeriksaan Mikroskopis 2_ → `ServiceRequest.identifier` (195, tanpa BQ)<br>`pemeriksaan_mikroskopis_tgl_contoh_uji_diterima` → `ServiceRequest.occurrenceDateTime` (203)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (204) |
| 11 | 225–245 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (226)<br>`pemeriksaan_mikroskopis_jenis_contoh_uji` → `Specimen.type.coding` (228) |
| 12 | 247–263 | Observation | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | `pemeriksaan_mikroskopis_2_hasil_pemeriksaan` → `Observation.valueCodeableConcept.coding` (251)<br>`pemeriksaan_mikroskopis_2_tgl_hasil_dilaporkan` → `Observation.issued` (261) |
| 13 | 265–277 | DiagnosticReport | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | – |
| 14 | 282–310 | ServiceRequest | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | _Pemeriksaan Xpert MTB RIF (Xpert) 1_ → `ServiceRequest.identifier` (282, tanpa BQ)<br>`pemeriksaan_xpert_mtb_rif_xpert_tgl_contoh_uji_diterima` → `ServiceRequest.occurrenceDateTime` (290)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (291) |
| 15 | 312–333 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (313)<br>`pemeriksaan_xpert_mtb_rif_xpert_jenis_contoh_uji` → `Specimen.type.coding` (315) |
| 16 | 335–353 | Observation | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | `pemeriksaan_xpert_mtb_rif_xpert_1_hasil_pemeriksaan` → `Observation.valueCodeableConcept.coding` (339)<br>`pemeriksaan_xpert_mtb_rif_xpert_1_tgl_hasil_dilaporkan` → `Observation.issued` (351) |
| 17 | 355–367 | DiagnosticReport | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | – |
| 18 | 369–397 | ServiceRequest | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | _Pemeriksaan Xpert MTB RIF (Xpert) 2_ → `ServiceRequest.identifier` (369, tanpa BQ)<br>`pemeriksaan_xpert_mtb_rif_xpert_tgl_contoh_uji_diterima` → `ServiceRequest.occurrenceDateTime` (377)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (378) |
| 19 | 399–419 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (400)<br>`pemeriksaan_xpert_mtb_rif_xpert_jenis_contoh_uji` → `Specimen.type.coding` (402) |
| 20 | 421–439 | Observation | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | `pemeriksaan_xpert_mtb_rif_xpert_2_hasil_pemeriksaan` → `Observation.valueCodeableConcept.coding` (425)<br>`pemeriksaan_xpert_mtb_rif_xpert_2_tgl_hasil_dilaporkan` → `Observation.issued` (437) |
| 21 | 441–453 | DiagnosticReport | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | – |
| 22 | 458–486 | ServiceRequest | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | _Chip MTB Plus 1_ → `ServiceRequest.identifier` (458, tanpa BQ)<br>`pemeriksaan_xpert_mtb_rif_truenat_tgl_contoh_uji_diterima` → `ServiceRequest.occurrenceDateTime` (466)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (467) |
| 23 | 488–508 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (489)<br>`pemeriksaan_xpert_mtb_rif_truenat_jenis_contoh_uji` → `Specimen.type.coding` (491) |
| 24 | 510–521 | Observation | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | `pemeriksaan_xpert_mtb_rif_truenat_chip_mtb_plus_1_hasil_pemeriksaan` → `Observation.valueString` (514)<br>`pemeriksaan_xpert_mtb_rif_truenat_chip_mtb_plus_1_tgl_hasil_dilaporkan` → `Observation.issued` (519) |
| 25 | 523–535 | DiagnosticReport | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | – |
| 26 | 537–566 | ServiceRequest | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | _Chip MTB Plus 2_ → `ServiceRequest.identifier` (537, tanpa BQ)<br>`pemeriksaan_xpert_mtb_rif_truenat_tgl_contoh_uji_diterima` → `ServiceRequest.occurrenceDateTime` (545)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (546) |
| 27 | 568–588 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (569)<br>`pemeriksaan_xpert_mtb_rif_truenat_jenis_contoh_uji` → `Specimen.type.coding` (571) |
| 28 | 590–601 | Observation | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | `pemeriksaan_xpert_mtb_rif_truenat_chip_mtb_plus_2_hasil_pemeriksaan` → `Observation.valueString` (594)<br>`pemeriksaan_xpert_mtb_rif_truenat_chip_mtb_plus_2_tgl_hasil_dilaporkan` → `Observation.issued` (599) |
| 29 | 603–615 | DiagnosticReport | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | – |
| 30 | 617–646 | ServiceRequest | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | _Chip MTB Rif 1_ → `ServiceRequest.identifier` (617, tanpa BQ)<br>`pemeriksaan_xpert_mtb_rif_truenat_tgl_contoh_uji_diterima` → `ServiceRequest.occurrenceDateTime` (625)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (626) |
| 31 | 648–667 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (649)<br>`pemeriksaan_xpert_mtb_rif_truenat_jenis_contoh_uji` → `Specimen.type.coding` (651) |
| 32 | 669–680 | Observation | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | `pemeriksaan_xpert_mtb_rif_truenat_chip_mtb_rif_1_hasil_pemeriksaan` → `Observation.valueString` (673)<br>`pemeriksaan_xpert_mtb_rif_truenat_chip_mtb_rif_1_tgl_hasil_dilaporkan` → `Observation.issued` (678) |
| 33 | 682–694 | DiagnosticReport | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | – |
| 34 | 696–724 | ServiceRequest | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | _Chip MTB Rif 2_ → `ServiceRequest.identifier` (696, tanpa BQ)<br>`pemeriksaan_xpert_mtb_rif_truenat_tgl_contoh_uji_diterima` → `ServiceRequest.occurrenceDateTime` (704)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (705) |
| 35 | 726–746 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (727)<br>`pemeriksaan_xpert_mtb_rif_truenat_jenis_contoh_uji` → `Specimen.type.coding` (729) |
| 36 | 748–759 | Observation | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | `pemeriksaan_xpert_mtb_rif_truenat_chip_mtb_rif_2_hasil_pemeriksaan` → `Observation.valueString` (752)<br>`pemeriksaan_xpert_mtb_rif_truenat_chip_mtb_rif_2_tgl_hasil_dilaporkan` → `Observation.issued` (757) |
| 37 | 761–773 | DiagnosticReport | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | – |
| 38 | 778–806 | ServiceRequest | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | _Pemeriksaan TCM MTB RIF INH (BD MAX) 1_ → `ServiceRequest.identifier` (778, tanpa BQ)<br>`pemeriksaan_tcm_mtb_rif_inh_bd_max_tgl_contoh_uji_diterima` → `ServiceRequest.occurrenceDateTime` (786)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (787) |
| 39 | 808–828 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (809)<br>`pemeriksaan_tcm_mtb_rif_inh_bd_max_jenis_contoh_uji` → `Specimen.type.coding` (811) |
| 40 | 830–848 | Observation | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | `pemeriksaan_tcm_mtb_rif_inh_bd_max_1_hasil_pemeriksaan` → `Observation.valueCodeableConcept.coding` (834)<br>`pemeriksaan_tcm_mtb_rif_inh_bd_max_1_tgl_hasil_dilaporkan` → `Observation.issued` (846) |
| 41 | 850–862 | DiagnosticReport | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | – |
| 42 | 864–892 | ServiceRequest | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | _Pemeriksaan TCM MTB RIF INH (BD MAX) 2_ → `ServiceRequest.identifier` (864, tanpa BQ)<br>`pemeriksaan_tcm_mtb_rif_inh_bd_max_tgl_contoh_uji_diterima` → `ServiceRequest.occurrenceDateTime` (872)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (873) |
| 43 | 894–914 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (895)<br>`pemeriksaan_tcm_mtb_rif_inh_bd_max_jenis_contoh_uji` → `Specimen.type.coding` (897) |
| 44 | 916–934 | Observation | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | `pemeriksaan_tcm_mtb_rif_inh_bd_max_2_hasil_pemeriksaan` → `Observation.valueCodeableConcept.coding` (920)<br>`pemeriksaan_tcm_mtb_rif_inh_bd_max_2_tgl_hasil_dilaporkan` → `Observation.issued` (932) |
| 45 | 936–948 | DiagnosticReport | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | – |
| 46 | 954–982 | ServiceRequest | MK099927 | Pemeriksaan PCR Open System | _Pemeriksaan PCR Open System_ → `ServiceRequest.identifier` (954, tanpa BQ)<br>`pemeriksaan_pcr_open_system_tgl_contoh_uji_diterima` → `ServiceRequest.occurrenceDateTime` (962)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (963) |
| 47 | 984–1004 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (985)<br>`pemeriksaan_pcr_open_system_jenis_contoh_uji` → `Specimen.type.coding` (987) |
| 48 | 1006–1039 | Observation | MK099927 | Pemeriksaan PCR Open System | _MTB_ → `Observation.component.code.coding` (1010, tanpa BQ)<br>`pemeriksaan_pcr_open_system_hasil_pemeriksaan_mtb` → `Observation.component.valueCodeableConcept.coding` (1011)<br>_Rifampisin_ → `Observation.component.code.coding` (1016, tanpa BQ)<br>`pemeriksaan_pcr_open_system_hasil_pemeriksaan_rif` → `Observation.component.valueCodeableConcept.coding` (1017)<br>_Isoniazid_ → `Observation.component.code.coding` (1020, tanpa BQ)<br>`pemeriksaan_pcr_open_system_hasil_pemeriksaan_inh` → `Observation.component.valueCodeableConcept.coding` (1021)<br>_Mutasi Gen katG_ → `Observation.component.code.coding` (1024, tanpa BQ)<br>`pemeriksaan_pcr_open_system_hasil_pemeriksaan_katg` → `Observation.component.valueCodeableConcept.coding` (1025)<br>_Mutasi Gen inhApr_ → `Observation.component.code.coding` (1027, tanpa BQ)<br>`pemeriksaan_pcr_open_system_hasil_pemeriksaan_inhapr` → `Observation.component.valueCodeableConcept.coding` (1028)<br>_NTM_ → `Observation.component.code.coding` (1030, tanpa BQ)<br>`pemeriksaan_pcr_open_system_hasil_pemeriksaan_ntm` → `Observation.component.valueCodeableConcept.coding` (1031)<br>`pemeriksaan_pcr_open_system_tgl_hasil_dilaporkan` → `Observation.issued` (1037) |
| 49 | 1042–1054 | DiagnosticReport | MK099927 | Pemeriksaan PCR Open System | – |
| 50 | 1060–1088 | ServiceRequest | X099379 | Pemeriksaan TCM XDR | _Pemeriksaan Xpert (TCM) XDR_ → `ServiceRequest.identifier` (1060, tanpa BQ)<br>`pemeriksaan_xpert_tcm_xdr_tgl_contoh_uji_diterima` → `ServiceRequest.occurrenceDateTime` (1068)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (1069) |
| 51 | 1090–1111 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (1091)<br>`pemeriksaan_xpert_tcm_xdr_jenis_contoh_uji` → `Specimen.type.coding` (1093) |
| 52 | 1113–1171 | Observation | X099379 | Pemeriksaan TCM XDR | `pemeriksaan_xpert_tcm_xdr_hasil_pemeriksaan_validinvalidno_resulterror` → `Observation.valueCodeableConcept.coding` (1117)<br>_MTB_ → `Observation.component.code.coding` (1122, tanpa BQ)<br>`pemeriksaan_xpert_tcm_xdr_hasil_pemeriksaan_mtb` → `Observation.component.valueCodeableConcept.coding` (1123)<br>_H Dosis Rendah (Low)_ → `Observation.component.code.coding` (1126, tanpa BQ)<br>`pemeriksaan_xpert_tcm_xdr_hasil_pemeriksaan_h_dosis_rendah_low` → `Observation.component.valueCodeableConcept.coding` (1127)<br>_H_ → `Observation.component.code.coding` (1131, tanpa BQ)<br>`pemeriksaan_xpert_tcm_xdr_hasil_pemeriksaan_h` → `Observation.component.valueCodeableConcept.coding` (1132)<br>_Eto_ → `Observation.component.code.coding` (1136, tanpa BQ)<br>`pemeriksaan_xpert_tcm_xdr_hasil_pemeriksaan_eto` → `Observation.component.valueCodeableConcept.coding` (1137)<br>_FQ Dosis Rendah (Low)_ → `Observation.component.code.coding` (1140, tanpa BQ)<br>`pemeriksaan_xpert_tcm_xdr_hasil_pemeriksaan_fq_dosis_rendah_low` → `Observation.component.valueCodeableConcept.coding` (1141)<br>_FQ_ → `Observation.component.code.coding` (1145, tanpa BQ)<br>`pemeriksaan_xpert_tcm_xdr_hasil_pemeriksaan_fq` → `Observation.component.valueCodeableConcept.coding` (1146)<br>_Amk_ → `Observation.component.code.coding` (1150, tanpa BQ)<br>`pemeriksaan_xpert_tcm_xdr_hasil_pemeriksaan_amk` → `Observation.component.valueCodeableConcept.coding` (1151)<br>_Km_ → `Observation.component.code.coding` (1155, tanpa BQ)<br>`pemeriksaan_xpert_tcm_xdr_hasil_pemeriksaan_km` → `Observation.component.valueCodeableConcept.coding` (1156)<br>_Cm_ → `Observation.component.code.coding` (1160, tanpa BQ)<br>`pemeriksaan_xpert_tcm_xdr_hasil_pemeriksaan_cm` → `Observation.component.valueCodeableConcept.coding` (1161)<br>`pemeriksaan_xpert_tcm_xdr_tgl_hasil_dilaporkan` → `Observation.issued` (1169) |
| 53 | 1173–1185 | DiagnosticReport | X099379 | Pemeriksaan TCM XDR | – |
| 54 | 1191–1219 | ServiceRequest | X099380 | Line Probe Assay (LPA) Lini 1 | _Pemeriksaan LPA Lini 1_ → `ServiceRequest.identifier` (1191, tanpa BQ)<br>`pemeriksaan_lpa_lini_satu_tgl_contoh_uji_diterima` → `ServiceRequest.occurrenceDateTime` (1199)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (1200) |
| 55 | 1221–1241 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (1222)<br>`pemeriksaan_lpa_lini_satu_jenis_contoh_uji` → `Specimen.type.coding` (1224) |
| 56 | 1243–1290 | Observation | X099380 | Line Probe Assay (LPA) Lini 1 | _Valid/Invalid_ → `Observation.code.coding` (1246, tanpa BQ)<br>`pemeriksaan_lpa_lini_satu_hasil_pemeriksaan_validinvalid` → `Observation.valueCodeableConcept.coding` (1247)<br>_MTB_ → `Observation.component.code.coding` (1250, tanpa BQ)<br>`pemeriksaan_lpa_lini_satu_hasil_pemeriksaan_mtb` → `Observation.component.valueCodeableConcept.coding` (1251)<br>_R_ → `Observation.component.code.coding` (1254, tanpa BQ)<br>`pemeriksaan_lpa_lini_satu_hasil_pemeriksaan_r` → `Observation.component.valueCodeableConcept.coding` (1255)<br>_Isoniazid Dosis Rendah_ → `Observation.component.code.coding` (1260, tanpa BQ)<br>`pemeriksaan_lpa_lini_satu_hasil_pemeriksaan_h_low_dose` → `Observation.component.valueCodeableConcept.coding` (1261)<br>_Isoniazid Dosis Tinggi_ → `Observation.component.code.coding` (1266, tanpa BQ)<br>`pemeriksaan_lpa_lini_satu_hasil_pemeriksaan_h_high_dose` → `Observation.component.valueCodeableConcept.coding` (1267)<br>_Etionamid_ → `Observation.component.code.coding` (1272, tanpa BQ)<br>`pemeriksaan_lpa_lini_satu_hasil_pemeriksaan_eto` → `Observation.component.valueCodeableConcept.coding` (1273)<br>_Protionamid_ → `Observation.component.code.coding` (1278, tanpa BQ)<br>`pemeriksaan_lpa_lini_satu_hasil_pemeriksaan_pto` → `Observation.component.valueCodeableConcept.coding` (1279)<br>`pemeriksaan_lpa_lini_satu_tgl_hasil_dilaporkan` → `Observation.issued` (1288) |
| 57 | 1292–1304 | DiagnosticReport | X099380 | Line Probe Assay (LPA) Lini 1 | – |
| 58 | 1310–1338 | ServiceRequest | X099381 | Line Probe Assay (LPA) Lini 2 | _Pemeriksaan LPA Lini 2_ → `ServiceRequest.identifier` (1310, tanpa BQ)<br>`pemeriksaan_lpa_line_probe_assay_lini_2_tgl_contoh_uji_diterima` → `ServiceRequest.occurrenceDateTime` (1318)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (1319) |
| 59 | 1340–1359 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (1341)<br>`pemeriksaan_lpa_line_probe_assay_lini_2_jenis_contoh_uji` → `Specimen.type.coding` (1343) |
| 60 | 1361–1414 | Observation | X099381 | Line Probe Assay (LPA) Lini 2 | `pemeriksaan_lpa_line_probe_assay_lini_2_hasil_pemeriksaan_invalid` → `Observation.valueCodeableConcept.coding` (1365)<br>_MTB_ → `Observation.component.code.coding` (1368, tanpa BQ)<br>`pemeriksaan_lpa_line_probe_assay_lini_2_hasil_pemeriksaan_mtb` → `Observation.component.valueCodeableConcept.coding` (1369)<br>_Levofloksasin_ → `Observation.component.code.coding` (1372, tanpa BQ)<br>`pemeriksaan_lpa_line_probe_assay_lini_2_hasil_pemeriksaan_fq_lfx` → `Observation.component.valueCodeableConcept.coding` (1373)<br>_Moksifloksasin_ → `Observation.component.code.coding` (1378, tanpa BQ)<br>`pemeriksaan_lpa_line_probe_assay_lini_2_hasil_pemeriksaan_fq_mfx` → `Observation.component.valueCodeableConcept.coding` (1379)<br>_Moksifloksasin Dosis Tinggi_ → `Observation.component.code.coding` (1384, tanpa BQ)<br>`pemeriksaan_lpa_line_probe_assay_lini_2_hasil_pemeriksaan_fq_mfx_dosis_tinggi` → `Observation.component.valueCodeableConcept.coding` (1385)<br>_Kanamisin_ → `Observation.component.code.coding` (1390, tanpa BQ)<br>`pemeriksaan_lpa_line_probe_assay_lini_2_hasil_pemeriksaan_slid_km` → `Observation.component.valueCodeableConcept.coding` (1391)<br>_Amikasin_ → `Observation.component.code.coding` (1396, tanpa BQ)<br>`pemeriksaan_lpa_line_probe_assay_lini_2_hasil_pemeriksaan_slid_amk` → `Observation.component.valueCodeableConcept.coding` (1397)<br>_Kapreomisin_ → `Observation.component.code.coding` (1402, tanpa BQ)<br>`pemeriksaan_lpa_line_probe_assay_lini_2_hasil_pemeriksaan_slid_cm` → `Observation.component.valueCodeableConcept.coding` (1403)<br>`pemeriksaan_lpa_line_probe_assay_lini_2_tgl_hasil_dilaporkan` → `Observation.issued` (1412) |
| 61 | 1416–1428 | DiagnosticReport | X099381 | Line Probe Assay (LPA) Lini 2 | – |
| 62 | 1435–1464 | ServiceRequest | X099389 | Hasil Pemeriksaan Biakan TB (Metode: LJ) | _Pemeriksaan Biakan_ → `ServiceRequest.identifier` (1435, tanpa BQ)<br>`pemeriksaan_biakan_tgl_contoh_uji_diterima_untuk_pemeriksaan_biakan_dan_uji_kepekaan` → `ServiceRequest.occurrenceDateTime` (1444)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (1445) |
| 63 | 1466–1485 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (1467)<br>`pemeriksaan_biakan_jenis_contoh_uji` → `Specimen.type.coding` (1469) |
| 64 | 1487–1508 | Observation | X099389 | Hasil Pemeriksaan Biakan TB (Metode: LJ) | `pemeriksaan_biakan_metode_uji` → `Observation.method.coding` (1488)<br>`pemeriksaan_biakan_hasil_pemeriksaan` → `Observation.valueCodeableConcept.coding` (1494)<br>`pemeriksaan_biakan_tgl_hasil_dilaporkan` → `Observation.issued` (1506) |
| 65 | 1510–1523 | DiagnosticReport | X099389 | Hasil Pemeriksaan Biakan TB (Metode: LJ) | – |
| 66 | 1526–1554 | ServiceRequest | X099383 | Pemeriksaan Paket Standar Kepekaan | _Pemeriksaan Paket Standar Uji Kepekaan_ → `ServiceRequest.identifier` (1526, tanpa BQ)<br>`pemeriksaan_paket_standar_uji_kepekaan_tgl_hasil_dilaporkan` → `ServiceRequest.occurrenceDateTime` (1534)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (1535) |
| 67 | 1556–1575 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (1557)<br>_Jenis Contoh Uji_ → `Specimen.type.coding` (1559, tanpa BQ) |
| 68 | 1577–1649 | Observation | X099383 | Pemeriksaan Paket Standar Kepekaan | _Isoniazid_ → `Observation.component.code.coding` (1582, tanpa BQ)<br>`pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_h` → `Observation.component.valueCodeableConcept.coding` (1583)<br>_Isoniazid Dosis Tinggi_ → `Observation.component.code.coding` (1588, tanpa BQ)<br>`pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_h_dosis_tinggi` → `Observation.component.valueCodeableConcept.coding` (1589)<br>_Levofloksasin_ → `Observation.component.code.coding` (1594, tanpa BQ)<br>`pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_lfx` → `Observation.component.valueCodeableConcept.coding` (1595)<br>_Moksifloksasin_ → `Observation.component.code.coding` (1600, tanpa BQ)<br>`pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_mfx` → `Observation.component.valueCodeableConcept.coding` (1601)<br>_Moksifloksasin Dosis Tinggi_ → `Observation.component.code.coding` (1606, tanpa BQ)<br>`pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_mfx_dosis_tinggi` → `Observation.component.valueCodeableConcept.coding` (1607)<br>_Kanamisin_ → `Observation.component.code.coding` (1612, tanpa BQ)<br>`pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_km` → `Observation.component.valueCodeableConcept.coding` (1613)<br>_Amikasin_ → `Observation.component.code.coding` (1618, tanpa BQ)<br>_Hasil Pemeriksaan Amk_ → `Observation.component.valueCodeableConcept.coding` (1619, tanpa BQ)<br>_Kapreomisin_ → `Observation.component.code.coding` (1624, tanpa BQ)<br>`pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_cm` → `Observation.component.valueCodeableConcept.coding` (1625)<br>`pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan` → `Observation.component.code.coding` (1630)<br>`pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_1` → `Observation.component.code.coding` (1632)<br>`pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_2` → `Observation.component.code.coding` (1634)<br>`pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_3` → `Observation.component.code.coding` (1636)<br>`pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_4` → `Observation.component.code.coding` (1638)<br>`pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_5` → `Observation.component.code.coding` (1640) |
| 69 | 1651–1663 | DiagnosticReport | X099383 | Pemeriksaan Paket Standar Kepekaan | – |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 17 |
| ServiceRequest | 16 |
| Specimen | 16 |
| DiagnosticReport | 16 |
| Patient | 1 |
| EpisodeOfCare | 1 |
| Encounter | 1 |
| Condition | 1 |
| **Total** | **69** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 38 | EpisodeOfCare | `EpisodeOfCare.type.coding` | TB-SO | Tuberkulosis Sensitif Obat | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 2 | 39 | EpisodeOfCare | `EpisodeOfCare.type.coding` | TB-RO | Tuberkulosis Resisten Obat | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 3 | 60 | Encounter | `Encounter.hospitalization.admitSource.coding` | EHA000002 | Datang sendiri | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 4 | 61 | Encounter | `Encounter.hospitalization.admitSource.coding` | 257622000 | Healthcare facility | http://snomed.info/sct |
| 5 | 89 | Condition | `Condition.code.coding` | 171126009 | Tuberculosis screening | http://snomed.info/sct |
| 6 | 98 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 7 | 117 | ServiceRequest | `ServiceRequest.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 8 | 121 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 9 | 122 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 10 | 124 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 11 | 126 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 12 | 128 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 13 | 130 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 14 | 132 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 15 | 134 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 16 | 136 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 17 | 138 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 18 | 145 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 19 | 146 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 20 | 147 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 21 | 148 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 22 | 149 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 23 | 150 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 24 | 151 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 25 | 152 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 26 | 153 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 27 | 154 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 28 | 155 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 29 | 166 | Observation | `Observation.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 30 | 167 | Observation | `Observation.valueCodeableConcept.coding` | 260385009 | Negative | http://snomed.info/sct |
| 31 | 168 | Observation | `Observation.valueCodeableConcept.coding` | LA11841-6 | 1+ | http://loinc.org |
| 32 | 169 | Observation | `Observation.valueCodeableConcept.coding` | LA11842-4 | 2+ | http://loinc.org |
| 33 | 170 | Observation | `Observation.valueCodeableConcept.coding` | LA11843-2 | 3+ | http://loinc.org |
| 34 | 184 | DiagnosticReport | `DiagnosticReport.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 35 | 200 | ServiceRequest | `ServiceRequest.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 36 | 204 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 37 | 205 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 38 | 207 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 39 | 209 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 40 | 211 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 41 | 213 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 42 | 215 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 43 | 217 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 44 | 219 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 45 | 221 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 46 | 228 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 47 | 229 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 48 | 230 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 49 | 231 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 50 | 232 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 51 | 233 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 52 | 234 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 53 | 235 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 54 | 236 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 55 | 237 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 56 | 238 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 57 | 250 | Observation | `Observation.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 58 | 251 | Observation | `Observation.valueCodeableConcept.coding` | 260385009 | Negative | http://snomed.info/sct |
| 59 | 252 | Observation | `Observation.valueCodeableConcept.coding` | LA11841-6 | 1+ | http://loinc.org |
| 60 | 253 | Observation | `Observation.valueCodeableConcept.coding` | LA11842-4 | 2+ | http://loinc.org |
| 61 | 254 | Observation | `Observation.valueCodeableConcept.coding` | LA11843-2 | 3+ | http://loinc.org |
| 62 | 268 | DiagnosticReport | `DiagnosticReport.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 63 | 287 | ServiceRequest | `ServiceRequest.code.coding` | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | http://terminology.kemkes.go.id/sp |
| 64 | 291 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 65 | 292 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 66 | 294 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 67 | 296 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 68 | 298 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 69 | 300 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 70 | 302 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 71 | 304 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 72 | 306 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 73 | 308 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 74 | 315 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 75 | 316 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 76 | 317 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 77 | 318 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 78 | 319 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 79 | 320 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 80 | 321 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 81 | 322 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 82 | 323 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 83 | 324 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 84 | 325 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 85 | 338 | Observation | `Observation.code.coding` | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | http://terminology.kemkes.go.id/sp |
| 86 | 339 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 87 | 340 | Observation | `Observation.valueCodeableConcept.coding` | X099770 | Rifampisin sensitive | http://terminology.kemkes.go.id/CodeSystem/examination |
| 88 | 341 | Observation | `Observation.valueCodeableConcept.coding` | X099771 | Rifampisin resistan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 89 | 342 | Observation | `Observation.valueCodeableConcept.coding` | X099772 | Rifampisin indeterminate | http://terminology.kemkes.go.id/CodeSystem/examination |
| 90 | 358 | DiagnosticReport | `DiagnosticReport.code.coding` | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | http://terminology.kemkes.go.id/sp |
| 91 | 374 | ServiceRequest | `ServiceRequest.code.coding` | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | http://terminology.kemkes.go.id/sp |
| 92 | 378 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 93 | 379 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 94 | 381 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 95 | 383 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 96 | 385 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 97 | 387 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 98 | 389 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 99 | 391 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 100 | 393 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 101 | 395 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 102 | 402 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 103 | 403 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 104 | 404 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 105 | 405 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 106 | 406 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 107 | 407 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 108 | 408 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 109 | 409 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 110 | 410 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 111 | 411 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 112 | 412 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 113 | 424 | Observation | `Observation.code.coding` | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | http://terminology.kemkes.go.id/sp |
| 114 | 425 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 115 | 426 | Observation | `Observation.valueCodeableConcept.coding` | X099770 | Rifampisin sensitive | http://terminology.kemkes.go.id/CodeSystem/examination |
| 116 | 427 | Observation | `Observation.valueCodeableConcept.coding` | X099771 | Rifampisin resistan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 117 | 428 | Observation | `Observation.valueCodeableConcept.coding` | X099772 | Rifampisin indeterminate | http://terminology.kemkes.go.id/CodeSystem/examination |
| 118 | 444 | DiagnosticReport | `DiagnosticReport.code.coding` | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | http://terminology.kemkes.go.id/sp |
| 119 | 463 | ServiceRequest | `ServiceRequest.code.coding` | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | http://terminology.kemkes.go.id/sp |
| 120 | 467 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 121 | 468 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 122 | 470 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 123 | 472 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 124 | 474 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 125 | 476 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 126 | 478 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 127 | 480 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 128 | 482 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 129 | 484 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 130 | 491 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 131 | 492 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 132 | 493 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 133 | 494 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 134 | 495 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 135 | 496 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 136 | 497 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 137 | 498 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 138 | 499 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 139 | 500 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 140 | 501 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 141 | 513 | Observation | `Observation.code.coding` | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | http://terminology.kemkes.go.id/sp |
| 142 | 526 | DiagnosticReport | `DiagnosticReport.code.coding` | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | http://terminology.kemkes.go.id/sp |
| 143 | 542 | ServiceRequest | `ServiceRequest.code.coding` | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | http://terminology.kemkes.go.id/sp |
| 144 | 546 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 145 | 547 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 146 | 549 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 147 | 551 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 148 | 553 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 149 | 555 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 150 | 557 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 151 | 559 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 152 | 561 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 153 | 563 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 154 | 571 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 155 | 572 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 156 | 573 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 157 | 574 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 158 | 575 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 159 | 576 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 160 | 577 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 161 | 578 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 162 | 579 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 163 | 580 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 164 | 581 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 165 | 593 | Observation | `Observation.code.coding` | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | http://terminology.kemkes.go.id/sp |
| 166 | 606 | DiagnosticReport | `DiagnosticReport.code.coding` | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | http://terminology.kemkes.go.id/sp |
| 167 | 622 | ServiceRequest | `ServiceRequest.code.coding` | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | http://terminology.kemkes.go.id/sp |
| 168 | 626 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 169 | 627 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 170 | 629 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 171 | 631 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 172 | 633 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 173 | 635 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 174 | 637 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 175 | 639 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 176 | 641 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 177 | 643 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 178 | 651 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 179 | 652 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 180 | 653 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 181 | 654 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 182 | 655 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 183 | 656 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 184 | 657 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 185 | 658 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 186 | 659 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 187 | 660 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 188 | 661 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 189 | 672 | Observation | `Observation.code.coding` | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | http://terminology.kemkes.go.id/sp |
| 190 | 685 | DiagnosticReport | `DiagnosticReport.code.coding` | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | http://terminology.kemkes.go.id/sp |
| 191 | 701 | ServiceRequest | `ServiceRequest.code.coding` | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | http://terminology.kemkes.go.id/sp |
| 192 | 705 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 193 | 706 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 194 | 708 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 195 | 710 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 196 | 712 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 197 | 714 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 198 | 716 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 199 | 718 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 200 | 720 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 201 | 722 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 202 | 729 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 203 | 730 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 204 | 731 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 205 | 732 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 206 | 733 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 207 | 734 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 208 | 735 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 209 | 736 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 210 | 737 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 211 | 738 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 212 | 739 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 213 | 751 | Observation | `Observation.code.coding` | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | http://terminology.kemkes.go.id/sp |
| 214 | 764 | DiagnosticReport | `DiagnosticReport.code.coding` | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | http://terminology.kemkes.go.id/sp |
| 215 | 783 | ServiceRequest | `ServiceRequest.code.coding` | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 216 | 787 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 217 | 788 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 218 | 790 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 219 | 792 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 220 | 794 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 221 | 796 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 222 | 798 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 223 | 800 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 224 | 802 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 225 | 804 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 226 | 811 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 227 | 812 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 228 | 813 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 229 | 814 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 230 | 815 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 231 | 816 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 232 | 817 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 233 | 818 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 234 | 819 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 235 | 820 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 236 | 821 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 237 | 833 | Observation | `Observation.code.coding` | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 238 | 834 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 239 | 835 | Observation | `Observation.valueCodeableConcept.coding` | X099770 | Rifampisin sensitive | http://terminology.kemkes.go.id/CodeSystem/examination |
| 240 | 836 | Observation | `Observation.valueCodeableConcept.coding` | X099771 | Rifampisin resistan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 241 | 837 | Observation | `Observation.valueCodeableConcept.coding` | X099772 | Rifampisin indeterminate | http://terminology.kemkes.go.id/CodeSystem/examination |
| 242 | 853 | DiagnosticReport | `DiagnosticReport.code.coding` | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 243 | 869 | ServiceRequest | `ServiceRequest.code.coding` | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 244 | 873 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 245 | 874 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 246 | 876 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 247 | 878 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 248 | 880 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 249 | 882 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 250 | 884 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 251 | 886 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 252 | 888 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 253 | 890 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 254 | 897 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 255 | 898 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 256 | 899 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 257 | 900 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 258 | 901 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 259 | 902 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 260 | 903 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 261 | 904 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 262 | 905 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 263 | 906 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 264 | 907 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 265 | 919 | Observation | `Observation.code.coding` | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 266 | 920 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 267 | 921 | Observation | `Observation.valueCodeableConcept.coding` | X099770 | Rifampisin sensitive | http://terminology.kemkes.go.id/CodeSystem/examination |
| 268 | 922 | Observation | `Observation.valueCodeableConcept.coding` | X099771 | Rifampisin resistan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 269 | 923 | Observation | `Observation.valueCodeableConcept.coding` | X099772 | Rifampisin indeterminate | http://terminology.kemkes.go.id/CodeSystem/examination |
| 270 | 939 | DiagnosticReport | `DiagnosticReport.code.coding` | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 271 | 959 | ServiceRequest | `ServiceRequest.code.coding` | MK099927 | Pemeriksaan PCR Open System | http://terminology.kemkes.go.id/CodeSystem/examination |
| 272 | 963 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 273 | 964 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 274 | 966 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 275 | 968 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 276 | 970 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 277 | 972 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 278 | 974 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 279 | 976 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 280 | 978 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 281 | 980 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 282 | 987 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 283 | 988 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 284 | 989 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 285 | 990 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 286 | 991 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 287 | 992 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 288 | 993 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 289 | 994 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 290 | 995 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 291 | 996 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 292 | 997 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 293 | 1009 | Observation | `Observation.code.coding` | MK099927 | Pemeriksaan PCR Open System | http://terminology.kemkes.go.id/CodeSystem/examination |
| 294 | 1010 | Observation | `Observation.component.code.coding` | 13956-8 | Mycobacterium tuberculosis DNA [Presence] in Specimen by NAA with probe detection | http://loinc.org |
| 295 | 1011 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 296 | 1012 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 297 | 1016 | Observation | `Observation.component.code.coding` | 89489-9 | rifAMPin [Susceptibility] by Genotype method | http://loinc.org |
| 298 | 1017 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 299 | 1018 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 300 | 1020 | Observation | `Observation.component.code.coding` | 89488-1 | Isoniazid [Susceptibility] by Genotype method | http://loinc.org |
| 301 | 1021 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 302 | 1022 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 303 | 1024 | Observation | `Observation.component.code.coding` | 46246-5 | Mycobacterium tuberculosis katG gene isoniazid high level resistance mutation [Identifier] by Molecular method | http://loinc.org |
| 304 | 1025 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 305 | 1026 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 306 | 1027 | Observation | `Observation.component.code.coding` | 63072-3 | Mycobacterium tuberculosis inhA gene isoniazid low level resistance mutation [Presence] by Molecular method | http://loinc.org |
| 307 | 1028 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 308 | 1029 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 309 | 1030 | Observation | `Observation.component.code.coding` | 110379001 | Mycobacterium, non-tuberculosis (organism) | http://snomed.info/sct |
| 310 | 1031 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 311 | 1032 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 312 | 1045 | DiagnosticReport | `DiagnosticReport.code.coding` | MK099927 | Pemeriksaan PCR Open System | http://terminology.kemkes.go.id/CodeSystem/examination |
| 313 | 1065 | ServiceRequest | `ServiceRequest.code.coding` | X099379 | Pemeriksaan TCM XDR | http://terminology.kemkes.go.id/CodeSystem/examination |
| 314 | 1069 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 315 | 1070 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 316 | 1072 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 317 | 1074 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 318 | 1076 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 319 | 1078 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 320 | 1080 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 321 | 1082 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 322 | 1084 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 323 | 1086 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 324 | 1093 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 325 | 1094 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 326 | 1095 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 327 | 1096 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 328 | 1097 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 329 | 1098 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 330 | 1099 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 331 | 1100 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 332 | 1101 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 333 | 1102 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 334 | 1103 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 335 | 1116 | Observation | `Observation.code.coding` | X099379 | Pemeriksaan TCM XDR | http://terminology.kemkes.go.id/CodeSystem/examination |
| 336 | 1117 | Observation | `Observation.valueCodeableConcept.coding` | X099781 | Hasil Valid | http://terminology.kemkes.go.id/CodeSystem/examination |
| 337 | 1122 | Observation | `Observation.component.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 338 | 1123 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 339 | 1124 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 340 | 1126 | Observation | `Observation.component.code.coding` | X099391 | H Dosis Rendah (Low) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 341 | 1127 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 342 | 1128 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 343 | 1129 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 344 | 1131 | Observation | `Observation.component.code.coding` | 89488-1 | Isoniazid [Susceptibility] by Genotype method | http://loinc.org |
| 345 | 1132 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 346 | 1133 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 347 | 1134 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 348 | 1136 | Observation | `Observation.component.code.coding` | 96110-2 | Ethionamide [Susceptibility] by Genotype method | http://loinc.org |
| 349 | 1137 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 350 | 1138 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 351 | 1140 | Observation | `Observation.component.code.coding` | X099392 | FQ Dosis Rendah (Low) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 352 | 1141 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 353 | 1142 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 354 | 1143 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 355 | 1145 | Observation | `Observation.component.code.coding` | 89487-3 | Fluoroquinolone [Susceptibility] by Genotype method | http://loinc.org |
| 356 | 1146 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 357 | 1147 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 358 | 1148 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 359 | 1150 | Observation | `Observation.component.code.coding` | 89484-0 | Amikacin [Susceptibility] by Genotype method | http://loinc.org |
| 360 | 1151 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 361 | 1152 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 362 | 1153 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 363 | 1155 | Observation | `Observation.component.code.coding` | 89482-4 | Kanamycin [Susceptibility] by Genotype method | http://loinc.org |
| 364 | 1156 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 365 | 1157 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 366 | 1158 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 367 | 1160 | Observation | `Observation.component.code.coding` | 89483-2 | Capreomycin [Susceptibility] by Genotype method | http://loinc.org |
| 368 | 1161 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 369 | 1162 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 370 | 1163 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 371 | 1176 | DiagnosticReport | `DiagnosticReport.code.coding` | X099379 | Pemeriksaan TCM XDR | http://terminology.kemkes.go.id/CodeSystem/examination |
| 372 | 1196 | ServiceRequest | `ServiceRequest.code.coding` | X099380 | Line Probe Assay (LPA) Lini 1 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 373 | 1200 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 374 | 1201 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 375 | 1203 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 376 | 1205 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 377 | 1207 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 378 | 1209 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 379 | 1211 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 380 | 1213 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 381 | 1215 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 382 | 1217 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 383 | 1224 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 384 | 1225 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 385 | 1226 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 386 | 1227 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 387 | 1228 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 388 | 1229 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 389 | 1230 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 390 | 1231 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 391 | 1232 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 392 | 1233 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 393 | 1234 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 394 | 1246 | Observation | `Observation.code.coding` | X099380 | Line Probe Assay (LPA) Lini 1 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 395 | 1247 | Observation | `Observation.valueCodeableConcept.coding` | X099781 | Hasil Valid | http://terminology.kemkes.go.id/CodeSystem/examination |
| 396 | 1250 | Observation | `Observation.component.code.coding` | 13956-8 | Mycobacterium tuberculosis DNA [Presence] in Specimen by NAA with probe detection | http://loinc.org |
| 397 | 1251 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 398 | 1252 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 399 | 1254 | Observation | `Observation.component.code.coding` | 89489-9 | rifAMPin [Susceptibility] by Genotype method | http://loinc.org |
| 400 | 1255 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 401 | 1256 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 402 | 1257 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 403 | 1258 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 404 | 1260 | Observation | `Observation.component.code.coding` | X099391 | H Dosis Rendah (Low) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 405 | 1261 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 406 | 1262 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 407 | 1263 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 408 | 1264 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 409 | 1266 | Observation | `Observation.component.code.coding` | X099783 | H Dosis Tinggi (High) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 410 | 1267 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 411 | 1268 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 412 | 1269 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 413 | 1270 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 414 | 1272 | Observation | `Observation.component.code.coding` | 96110-2 | Ethionamide [Susceptibility] by Genotype method | http://loinc.org |
| 415 | 1273 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 416 | 1274 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 417 | 1275 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 418 | 1276 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 419 | 1278 | Observation | `Observation.component.code.coding` | 103960-1 | Prothionamide [Susceptibility] by Genotype method | http://loinc.org |
| 420 | 1279 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 421 | 1280 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 422 | 1281 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 423 | 1282 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 424 | 1295 | DiagnosticReport | `DiagnosticReport.code.coding` | X099380 | Line Probe Assay (LPA) Lini 1 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 425 | 1315 | ServiceRequest | `ServiceRequest.code.coding` | X099381 | Line Probe Assay (LPA) Lini 2 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 426 | 1319 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 427 | 1320 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 428 | 1322 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 429 | 1324 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 430 | 1326 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 431 | 1328 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 432 | 1330 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 433 | 1332 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 434 | 1334 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 435 | 1336 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 436 | 1343 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 437 | 1344 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 438 | 1345 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 439 | 1346 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 440 | 1347 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 441 | 1348 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 442 | 1349 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 443 | 1350 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 444 | 1351 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 445 | 1352 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 446 | 1353 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 447 | 1364 | Observation | `Observation.code.coding` | X099381 | Line Probe Assay (LPA) Lini 2 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 448 | 1365 | Observation | `Observation.valueCodeableConcept.coding` | X099781 | Hasil Valid | http://terminology.kemkes.go.id/CodeSystem/examination |
| 449 | 1368 | Observation | `Observation.component.code.coding` | 13956-8 | Mycobacterium tuberculosis DNA [Presence] in Specimen by NAA with probe detection | http://loinc.org |
| 450 | 1369 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 451 | 1370 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 452 | 1372 | Observation | `Observation.component.code.coding` | 20629-2 | levoFLOXacin [Susceptibility] | http://loinc.org |
| 453 | 1373 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 454 | 1374 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 455 | 1375 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 456 | 1376 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 457 | 1378 | Observation | `Observation.component.code.coding` | 96112-8 | Moxifloxacin [Susceptibility] by Genotype method | http://loinc.org |
| 458 | 1379 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 459 | 1380 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 460 | 1381 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 461 | 1382 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 462 | 1384 | Observation | `Observation.component.code.coding` | X099775 | Moxifloxacin DT (Mfx DT) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 463 | 1385 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 464 | 1386 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 465 | 1387 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 466 | 1388 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 467 | 1390 | Observation | `Observation.component.code.coding` | 89482-4 | Kanamycin [Susceptibility] by Genotype method | http://loinc.org |
| 468 | 1391 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 469 | 1392 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 470 | 1393 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 471 | 1394 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 472 | 1396 | Observation | `Observation.component.code.coding` | 89484-0 | Amikacin [Susceptibility] by Genotype method | http://loinc.org |
| 473 | 1397 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 474 | 1398 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 475 | 1399 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 476 | 1400 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 477 | 1402 | Observation | `Observation.component.code.coding` | 89483-2 | Capreomycin [Susceptibility] by Genotype method | http://loinc.org |
| 478 | 1403 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 479 | 1404 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 480 | 1405 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 481 | 1406 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 482 | 1419 | DiagnosticReport | `DiagnosticReport.code.coding` | X099381 | Line Probe Assay (LPA) Lini 2 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 483 | 1440 | ServiceRequest | `ServiceRequest.code.coding` | X099389 | Hasil Pemeriksaan Biakan TB (Metode: LJ) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 484 | 1441 | ServiceRequest | `ServiceRequest.code.coding` | X099390 | Hasil Pemeriksaan Biakan TB (Metode: MGIT) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 485 | 1445 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 486 | 1446 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 487 | 1448 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 488 | 1450 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 489 | 1452 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 490 | 1454 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 491 | 1456 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 492 | 1458 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 493 | 1460 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 494 | 1462 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 495 | 1469 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 496 | 1470 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 497 | 1471 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 498 | 1472 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 499 | 1473 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 500 | 1474 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 501 | 1475 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 502 | 1476 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 503 | 1477 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 504 | 1478 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 505 | 1479 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 506 | 1488 | Observation | `Observation.method.coding` | OM000001 | LJ | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 507 | 1489 | Observation | `Observation.method.coding` | OM000002 | MGIT | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 508 | 1492 | Observation | `Observation.code.coding` | X099389 | Hasil Pemeriksaan Biakan TB (Metode: LJ) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 509 | 1493 | Observation | `Observation.code.coding` | X099390 | Hasil Pemeriksaan Biakan TB (Metode: MGIT) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 510 | 1494 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 511 | 1495 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 512 | 1496 | Observation | `Observation.valueCodeableConcept.coding` | LA11841-6 | + | http://loinc.org |
| 513 | 1497 | Observation | `Observation.valueCodeableConcept.coding` | LA11842-4 | ++ | http://loinc.org |
| 514 | 1498 | Observation | `Observation.valueCodeableConcept.coding` | LA11843-2 | +++ | http://loinc.org |
| 515 | 1499 | Observation | `Observation.valueCodeableConcept.coding` | 110379001 | Mycobacterium, non-tuberculosis (organism) | http://snomed.info/sct |
| 516 | 1513 | DiagnosticReport | `DiagnosticReport.code.coding` | X099389 | Hasil Pemeriksaan Biakan TB (Metode: LJ) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 517 | 1514 | DiagnosticReport | `DiagnosticReport.code.coding` | X099390 | Hasil Pemeriksaan Biakan TB (Metode: MGIT) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 518 | 1531 | ServiceRequest | `ServiceRequest.code.coding` | X099383 | Pemeriksaan Paket Standar Kepekaan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 519 | 1535 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 520 | 1536 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 521 | 1538 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 522 | 1540 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 523 | 1542 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 524 | 1544 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 525 | 1546 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 526 | 1548 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 527 | 1550 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 528 | 1552 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 529 | 1559 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 530 | 1560 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 531 | 1561 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 532 | 1562 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 533 | 1563 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 534 | 1564 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 535 | 1565 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 536 | 1566 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 537 | 1567 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 538 | 1568 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 539 | 1569 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 540 | 1580 | Observation | `Observation.code.coding` | X099383 | Pemeriksaan Paket Standar Kepekaan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 541 | 1582 | Observation | `Observation.component.code.coding` | 20383-6 | Isoniazid [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 542 | 1583 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 543 | 1584 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 544 | 1585 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 545 | 1588 | Observation | `Observation.component.code.coding` | X099776 | H High Dosage [Susceptibility] by Method for Slow-growing mycobacteria | http://terminology.kemkes.go.id/CodeSystem/examination |
| 546 | 1589 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 547 | 1590 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 548 | 1591 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 549 | 1594 | Observation | `Observation.component.code.coding` | 53716-7 | levoFLOXacin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 550 | 1595 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 551 | 1596 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 552 | 1597 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 553 | 1600 | Observation | `Observation.component.code.coding` | 41502-6 | Moxifloxacin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 554 | 1601 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 555 | 1602 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 556 | 1603 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 557 | 1606 | Observation | `Observation.component.code.coding` | X099778 | Moxifloxacin High Dosage [Susceptibility] by Method for Slow-growing mycobacteria | http://terminology.kemkes.go.id/CodeSystem/examination |
| 558 | 1607 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 559 | 1608 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 560 | 1609 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 561 | 1612 | Observation | `Observation.component.code.coding` | 23609-1 | Kanamycin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 562 | 1613 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 563 | 1614 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 564 | 1615 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 565 | 1618 | Observation | `Observation.component.code.coding` | 20373-7 | Amikacin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 566 | 1619 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 567 | 1620 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 568 | 1621 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 569 | 1624 | Observation | `Observation.component.code.coding` | 23607-5 | Capreomycin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 570 | 1625 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 571 | 1626 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 572 | 1627 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 573 | 1630 | Observation | `Observation.component.code.coding` | SP000472 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya | http://terminology.kemkes.go.id/sp |
| 574 | 1632 | Observation | `Observation.component.code.coding` | SP000473 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 1 | http://terminology.kemkes.go.id/sp |
| 575 | 1634 | Observation | `Observation.component.code.coding` | SP000474 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 2 | http://terminology.kemkes.go.id/sp |
| 576 | 1636 | Observation | `Observation.component.code.coding` | SP000475 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 3 | http://terminology.kemkes.go.id/sp |
| 577 | 1638 | Observation | `Observation.component.code.coding` | SP000476 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 4 | http://terminology.kemkes.go.id/sp |
| 578 | 1640 | Observation | `Observation.component.code.coding` | SP000477 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 5 | http://terminology.kemkes.go.id/sp |
| 579 | 1654 | DiagnosticReport | `DiagnosticReport.code.coding` | X099383 | Pemeriksaan Paket Standar Kepekaan | http://terminology.kemkes.go.id/CodeSystem/examination |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 195 |
| http://snomed.info/sct | 151 |
| http://loinc.org | 147 |
| http://terminology.kemkes.go.id/CodeSystem/examination | 60 |
| http://terminology.kemkes.go.id/sp | 24 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 2 |
| **Total** | **579** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 110 | – | No.Reg Lab | – | `` |
| 280 | – | No.Reg Lab | – | `` |
| 456 | – | No.Reg Lab | – | `` |
| 776 | – | No.Reg Lab | – | `` |
| 952 | – | No.Reg Lab | – | `` |
| 1058 | – | No.Reg Lab | – | `` |
| 1189 | – | No.Reg Lab | – | `` |
| 1308 | – | No.Reg Lab | – | `` |
| 1431 | – | No.Reg Lab | – | `` |
| 1433 | – | Metode Uji | – | `` |
| 1666 | – | Tanda Tangan Petugas Pemeriksa | – | `` |
| 1667 | – | Keterangan | – | `` |
