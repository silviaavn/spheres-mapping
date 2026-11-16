# Output Form: SITB TB 04 (Fasyankes & Rujukan)

Sumber: `mapping/phdt-data-dictionary-sitb-tb04.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 69 |
| Code (`jumlah code` = 1) | 579 |
| Code unik (code + CodeSystem) | 85 |
| Variabel BQ (unik) | 102 |
| Variabel di Excel export | 114 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 5–30 | Patient | – | – | `no_rekam_medis` → `Patient.identifier.value` (8)<br>`nik_nomor_induk_kependudukan` → `Patient.identifier.value` (11)<br>`nama_lengkap_pasien` → `Patient.name.text` (12)<br>`jenis_kelamin` → `Patient.gender` (13)<br>_Provinsi_ → `Patient.address.extension.extension.valueCode` (19, tanpa BQ)<br>_Kabupaten/Kota_ → `Patient.address.extension.extension.valueCode` (22, tanpa BQ)<br>_Kecamatan_ → `Patient.address.extension.extension.valueCode` (25, tanpa BQ)<br>_Kelurahan_ → `Patient.address.extension.extension.valueCode` (28, tanpa BQ)<br>`alamat_lengkap` → `Patient.address.line` (29) |
| 2 | 33–55 | EpisodeOfCare | TB-SO | Tuberkulosis Sensitif Obat | – |
| 3 | 58–87 | Encounter | – | – | `nama_fasilitas_kesehatan_asal_contoh_uji` → `Encounter.hospitalization.origin.reference` (62) 🔎 lookup master data<br>`nama_fasyankes` → `Encounter.serviceProvider.reference` (85) 🔎 lookup master data<br>`kabupaten_fasyankes` → `Encounter.serviceProvider.reference` (86) 🔎 lookup master data<br>`provinsi_fasyankes` → `Encounter.serviceProvider.reference` (87) 🔎 lookup master data |
| 4 | 89–95 | Condition | 171126009 | Tuberculosis screening | – |
| 5 | 98–109 | Observation | 424144002 | Current chronological age | `umur` → `Observation.valueQuantity.value` (101) |
| 6 | 114–142 | ServiceRequest | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | _Pemeriksaan Mikroskopis 1_ → `ServiceRequest.identifier` (114, tanpa BQ)<br>`pemeriksaan_mikroskopis_tgl_contoh_uji_diterima` → `ServiceRequest.occurrenceDateTime` (122)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (123) |
| 7 | 144–163 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (145)<br>`pemeriksaan_mikroskopis_jenis_contoh_uji` → `Specimen.type.coding` (147) |
| 8 | 165–181 | Observation | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | `pemeriksaan_mikroskopis_1_hasil_pemeriksaan` → `Observation.valueCodeableConcept.coding` (169)<br>`pemeriksaan_mikroskopis_1_tgl_hasil_dilaporkan` → `Observation.issued` (179) |
| 9 | 183–195 | DiagnosticReport | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | – |
| 10 | 197–225 | ServiceRequest | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | _Pemeriksaan Mikroskopis 2_ → `ServiceRequest.identifier` (197, tanpa BQ)<br>`pemeriksaan_mikroskopis_tgl_contoh_uji_diterima` → `ServiceRequest.occurrenceDateTime` (205)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (206) |
| 11 | 227–247 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (228)<br>`pemeriksaan_mikroskopis_jenis_contoh_uji` → `Specimen.type.coding` (230) |
| 12 | 249–265 | Observation | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | `pemeriksaan_mikroskopis_2_hasil_pemeriksaan` → `Observation.valueCodeableConcept.coding` (253)<br>`pemeriksaan_mikroskopis_2_tgl_hasil_dilaporkan` → `Observation.issued` (263) |
| 13 | 267–279 | DiagnosticReport | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | – |
| 14 | 284–312 | ServiceRequest | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | _Pemeriksaan Xpert MTB RIF (Xpert) 1_ → `ServiceRequest.identifier` (284, tanpa BQ)<br>`pemeriksaan_xpert_mtb_rif_xpert_tgl_contoh_uji_diterima` → `ServiceRequest.occurrenceDateTime` (292)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (293) |
| 15 | 314–335 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (315)<br>`pemeriksaan_xpert_mtb_rif_xpert_jenis_contoh_uji` → `Specimen.type.coding` (317) |
| 16 | 337–355 | Observation | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | `pemeriksaan_xpert_mtb_rif_xpert_1_hasil_pemeriksaan` → `Observation.valueCodeableConcept.coding` (341)<br>`pemeriksaan_xpert_mtb_rif_xpert_1_tgl_hasil_dilaporkan` → `Observation.issued` (353) |
| 17 | 357–369 | DiagnosticReport | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | – |
| 18 | 371–399 | ServiceRequest | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | _Pemeriksaan Xpert MTB RIF (Xpert) 2_ → `ServiceRequest.identifier` (371, tanpa BQ)<br>`pemeriksaan_xpert_mtb_rif_xpert_tgl_contoh_uji_diterima` → `ServiceRequest.occurrenceDateTime` (379)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (380) |
| 19 | 401–421 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (402)<br>`pemeriksaan_xpert_mtb_rif_xpert_jenis_contoh_uji` → `Specimen.type.coding` (404) |
| 20 | 423–441 | Observation | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | `pemeriksaan_xpert_mtb_rif_xpert_2_hasil_pemeriksaan` → `Observation.valueCodeableConcept.coding` (427)<br>`pemeriksaan_xpert_mtb_rif_xpert_2_tgl_hasil_dilaporkan` → `Observation.issued` (439) |
| 21 | 443–455 | DiagnosticReport | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | – |
| 22 | 460–488 | ServiceRequest | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | _Chip MTB Plus 1_ → `ServiceRequest.identifier` (460, tanpa BQ)<br>`pemeriksaan_xpert_mtb_rif_truenat_tgl_contoh_uji_diterima` → `ServiceRequest.occurrenceDateTime` (468)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (469) |
| 23 | 490–510 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (491)<br>`pemeriksaan_xpert_mtb_rif_truenat_jenis_contoh_uji` → `Specimen.type.coding` (493) |
| 24 | 512–523 | Observation | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | `pemeriksaan_xpert_mtb_rif_truenat_chip_mtb_plus_1_hasil_pemeriksaan` → `Observation.valueString` (516)<br>`pemeriksaan_xpert_mtb_rif_truenat_chip_mtb_plus_1_tgl_hasil_dilaporkan` → `Observation.issued` (521) |
| 25 | 525–537 | DiagnosticReport | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | – |
| 26 | 539–568 | ServiceRequest | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | _Chip MTB Plus 2_ → `ServiceRequest.identifier` (539, tanpa BQ)<br>`pemeriksaan_xpert_mtb_rif_truenat_tgl_contoh_uji_diterima` → `ServiceRequest.occurrenceDateTime` (547)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (548) |
| 27 | 570–590 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (571)<br>`pemeriksaan_xpert_mtb_rif_truenat_jenis_contoh_uji` → `Specimen.type.coding` (573) |
| 28 | 592–603 | Observation | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | `pemeriksaan_xpert_mtb_rif_truenat_chip_mtb_plus_2_hasil_pemeriksaan` → `Observation.valueString` (596)<br>`pemeriksaan_xpert_mtb_rif_truenat_chip_mtb_plus_2_tgl_hasil_dilaporkan` → `Observation.issued` (601) |
| 29 | 605–617 | DiagnosticReport | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | – |
| 30 | 619–648 | ServiceRequest | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | _Chip MTB Rif 1_ → `ServiceRequest.identifier` (619, tanpa BQ)<br>`pemeriksaan_xpert_mtb_rif_truenat_tgl_contoh_uji_diterima` → `ServiceRequest.occurrenceDateTime` (627)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (628) |
| 31 | 650–669 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (651)<br>`pemeriksaan_xpert_mtb_rif_truenat_jenis_contoh_uji` → `Specimen.type.coding` (653) |
| 32 | 671–682 | Observation | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | `pemeriksaan_xpert_mtb_rif_truenat_chip_mtb_rif_1_hasil_pemeriksaan` → `Observation.valueString` (675)<br>`pemeriksaan_xpert_mtb_rif_truenat_chip_mtb_rif_1_tgl_hasil_dilaporkan` → `Observation.issued` (680) |
| 33 | 684–696 | DiagnosticReport | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | – |
| 34 | 698–726 | ServiceRequest | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | _Chip MTB Rif 2_ → `ServiceRequest.identifier` (698, tanpa BQ)<br>`pemeriksaan_xpert_mtb_rif_truenat_tgl_contoh_uji_diterima` → `ServiceRequest.occurrenceDateTime` (706)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (707) |
| 35 | 728–748 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (729)<br>`pemeriksaan_xpert_mtb_rif_truenat_jenis_contoh_uji` → `Specimen.type.coding` (731) |
| 36 | 750–761 | Observation | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | `pemeriksaan_xpert_mtb_rif_truenat_chip_mtb_rif_2_hasil_pemeriksaan` → `Observation.valueString` (754)<br>`pemeriksaan_xpert_mtb_rif_truenat_chip_mtb_rif_2_tgl_hasil_dilaporkan` → `Observation.issued` (759) |
| 37 | 763–775 | DiagnosticReport | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | – |
| 38 | 780–808 | ServiceRequest | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | _Pemeriksaan TCM MTB RIF INH (BD MAX) 1_ → `ServiceRequest.identifier` (780, tanpa BQ)<br>`pemeriksaan_tcm_mtb_rif_inh_bd_max_tgl_contoh_uji_diterima` → `ServiceRequest.occurrenceDateTime` (788)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (789) |
| 39 | 810–830 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (811)<br>`pemeriksaan_tcm_mtb_rif_inh_bd_max_jenis_contoh_uji` → `Specimen.type.coding` (813) |
| 40 | 832–850 | Observation | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | `pemeriksaan_tcm_mtb_rif_inh_bd_max_1_hasil_pemeriksaan` → `Observation.valueCodeableConcept.coding` (836)<br>`pemeriksaan_tcm_mtb_rif_inh_bd_max_1_tgl_hasil_dilaporkan` → `Observation.issued` (848) |
| 41 | 852–864 | DiagnosticReport | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | – |
| 42 | 866–894 | ServiceRequest | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | _Pemeriksaan TCM MTB RIF INH (BD MAX) 2_ → `ServiceRequest.identifier` (866, tanpa BQ)<br>`pemeriksaan_tcm_mtb_rif_inh_bd_max_tgl_contoh_uji_diterima` → `ServiceRequest.occurrenceDateTime` (874)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (875) |
| 43 | 896–916 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (897)<br>`pemeriksaan_tcm_mtb_rif_inh_bd_max_jenis_contoh_uji` → `Specimen.type.coding` (899) |
| 44 | 918–936 | Observation | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | `pemeriksaan_tcm_mtb_rif_inh_bd_max_2_hasil_pemeriksaan` → `Observation.valueCodeableConcept.coding` (922)<br>`pemeriksaan_tcm_mtb_rif_inh_bd_max_2_tgl_hasil_dilaporkan` → `Observation.issued` (934) |
| 45 | 938–950 | DiagnosticReport | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | – |
| 46 | 956–984 | ServiceRequest | MK099927 | Pemeriksaan PCR Open System | _Pemeriksaan PCR Open System_ → `ServiceRequest.identifier` (956, tanpa BQ)<br>`pemeriksaan_pcr_open_system_tgl_contoh_uji_diterima` → `ServiceRequest.occurrenceDateTime` (964)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (965) |
| 47 | 986–1006 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (987)<br>`pemeriksaan_pcr_open_system_jenis_contoh_uji` → `Specimen.type.coding` (989) |
| 48 | 1008–1041 | Observation | MK099927 | Pemeriksaan PCR Open System | _MTB_ → `Observation.component.code.coding` (1012, tanpa BQ)<br>`pemeriksaan_pcr_open_system_hasil_pemeriksaan_mtb` → `Observation.component.valueCodeableConcept.coding` (1013)<br>_Rifampisin_ → `Observation.component.code.coding` (1018, tanpa BQ)<br>`pemeriksaan_pcr_open_system_hasil_pemeriksaan_rif` → `Observation.component.valueCodeableConcept.coding` (1019)<br>_Isoniazid_ → `Observation.component.code.coding` (1022, tanpa BQ)<br>`pemeriksaan_pcr_open_system_hasil_pemeriksaan_inh` → `Observation.component.valueCodeableConcept.coding` (1023)<br>_Mutasi Gen katG_ → `Observation.component.code.coding` (1026, tanpa BQ)<br>`pemeriksaan_pcr_open_system_hasil_pemeriksaan_katg` → `Observation.component.valueCodeableConcept.coding` (1027)<br>_Mutasi Gen inhApr_ → `Observation.component.code.coding` (1029, tanpa BQ)<br>`pemeriksaan_pcr_open_system_hasil_pemeriksaan_inhapr` → `Observation.component.valueCodeableConcept.coding` (1030)<br>_NTM_ → `Observation.component.code.coding` (1032, tanpa BQ)<br>`pemeriksaan_pcr_open_system_hasil_pemeriksaan_ntm` → `Observation.component.valueCodeableConcept.coding` (1033)<br>`pemeriksaan_pcr_open_system_tgl_hasil_dilaporkan` → `Observation.issued` (1039) |
| 49 | 1044–1056 | DiagnosticReport | MK099927 | Pemeriksaan PCR Open System | – |
| 50 | 1062–1090 | ServiceRequest | X099379 | Pemeriksaan TCM XDR | _Pemeriksaan Xpert (TCM) XDR_ → `ServiceRequest.identifier` (1062, tanpa BQ)<br>`pemeriksaan_xpert_tcm_xdr_tgl_contoh_uji_diterima` → `ServiceRequest.occurrenceDateTime` (1070)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (1071) |
| 51 | 1092–1113 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (1093)<br>`pemeriksaan_xpert_tcm_xdr_jenis_contoh_uji` → `Specimen.type.coding` (1095) |
| 52 | 1115–1173 | Observation | X099379 | Pemeriksaan TCM XDR | `pemeriksaan_xpert_tcm_xdr_hasil_pemeriksaan_validinvalidno_resulterror` → `Observation.valueCodeableConcept.coding` (1119)<br>_MTB_ → `Observation.component.code.coding` (1124, tanpa BQ)<br>`pemeriksaan_xpert_tcm_xdr_hasil_pemeriksaan_mtb` → `Observation.component.valueCodeableConcept.coding` (1125)<br>_H Dosis Rendah (Low)_ → `Observation.component.code.coding` (1128, tanpa BQ)<br>`pemeriksaan_xpert_tcm_xdr_hasil_pemeriksaan_h_dosis_rendah_low` → `Observation.component.valueCodeableConcept.coding` (1129)<br>_H_ → `Observation.component.code.coding` (1133, tanpa BQ)<br>`pemeriksaan_xpert_tcm_xdr_hasil_pemeriksaan_h` → `Observation.component.valueCodeableConcept.coding` (1134)<br>_Eto_ → `Observation.component.code.coding` (1138, tanpa BQ)<br>`pemeriksaan_xpert_tcm_xdr_hasil_pemeriksaan_eto` → `Observation.component.valueCodeableConcept.coding` (1139)<br>_FQ Dosis Rendah (Low)_ → `Observation.component.code.coding` (1142, tanpa BQ)<br>`pemeriksaan_xpert_tcm_xdr_hasil_pemeriksaan_fq_dosis_rendah_low` → `Observation.component.valueCodeableConcept.coding` (1143)<br>_FQ_ → `Observation.component.code.coding` (1147, tanpa BQ)<br>`pemeriksaan_xpert_tcm_xdr_hasil_pemeriksaan_fq` → `Observation.component.valueCodeableConcept.coding` (1148)<br>_Amk_ → `Observation.component.code.coding` (1152, tanpa BQ)<br>`pemeriksaan_xpert_tcm_xdr_hasil_pemeriksaan_amk` → `Observation.component.valueCodeableConcept.coding` (1153)<br>_Km_ → `Observation.component.code.coding` (1157, tanpa BQ)<br>`pemeriksaan_xpert_tcm_xdr_hasil_pemeriksaan_km` → `Observation.component.valueCodeableConcept.coding` (1158)<br>_Cm_ → `Observation.component.code.coding` (1162, tanpa BQ)<br>`pemeriksaan_xpert_tcm_xdr_hasil_pemeriksaan_cm` → `Observation.component.valueCodeableConcept.coding` (1163)<br>`pemeriksaan_xpert_tcm_xdr_tgl_hasil_dilaporkan` → `Observation.issued` (1171) |
| 53 | 1175–1187 | DiagnosticReport | X099379 | Pemeriksaan TCM XDR | – |
| 54 | 1193–1221 | ServiceRequest | X099380 | Line Probe Assay (LPA) Lini 1 | _Pemeriksaan LPA Lini 1_ → `ServiceRequest.identifier` (1193, tanpa BQ)<br>`pemeriksaan_lpa_lini_satu_tgl_contoh_uji_diterima` → `ServiceRequest.occurrenceDateTime` (1201)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (1202) |
| 55 | 1223–1243 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (1224)<br>`pemeriksaan_lpa_lini_satu_jenis_contoh_uji` → `Specimen.type.coding` (1226) |
| 56 | 1245–1292 | Observation | X099380 | Line Probe Assay (LPA) Lini 1 | _Valid/Invalid_ → `Observation.code.coding` (1248, tanpa BQ)<br>`pemeriksaan_lpa_lini_satu_hasil_pemeriksaan_validinvalid` → `Observation.valueCodeableConcept.coding` (1249)<br>_MTB_ → `Observation.component.code.coding` (1252, tanpa BQ)<br>`pemeriksaan_lpa_lini_satu_hasil_pemeriksaan_mtb` → `Observation.component.valueCodeableConcept.coding` (1253)<br>_R_ → `Observation.component.code.coding` (1256, tanpa BQ)<br>`pemeriksaan_lpa_lini_satu_hasil_pemeriksaan_r` → `Observation.component.valueCodeableConcept.coding` (1257)<br>_Isoniazid Dosis Rendah_ → `Observation.component.code.coding` (1262, tanpa BQ)<br>`pemeriksaan_lpa_lini_satu_hasil_pemeriksaan_h_low_dose` → `Observation.component.valueCodeableConcept.coding` (1263)<br>_Isoniazid Dosis Tinggi_ → `Observation.component.code.coding` (1268, tanpa BQ)<br>`pemeriksaan_lpa_lini_satu_hasil_pemeriksaan_h_high_dose` → `Observation.component.valueCodeableConcept.coding` (1269)<br>_Etionamid_ → `Observation.component.code.coding` (1274, tanpa BQ)<br>`pemeriksaan_lpa_lini_satu_hasil_pemeriksaan_eto` → `Observation.component.valueCodeableConcept.coding` (1275)<br>_Protionamid_ → `Observation.component.code.coding` (1280, tanpa BQ)<br>`pemeriksaan_lpa_lini_satu_hasil_pemeriksaan_pto` → `Observation.component.valueCodeableConcept.coding` (1281)<br>`pemeriksaan_lpa_lini_satu_tgl_hasil_dilaporkan` → `Observation.issued` (1290) |
| 57 | 1294–1306 | DiagnosticReport | X099380 | Line Probe Assay (LPA) Lini 1 | – |
| 58 | 1312–1340 | ServiceRequest | X099381 | Line Probe Assay (LPA) Lini 2 | _Pemeriksaan LPA Lini 2_ → `ServiceRequest.identifier` (1312, tanpa BQ)<br>`pemeriksaan_lpa_line_probe_assay_lini_2_tgl_contoh_uji_diterima` → `ServiceRequest.occurrenceDateTime` (1320)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (1321) |
| 59 | 1342–1361 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (1343)<br>`pemeriksaan_lpa_line_probe_assay_lini_2_jenis_contoh_uji` → `Specimen.type.coding` (1345) |
| 60 | 1363–1416 | Observation | X099381 | Line Probe Assay (LPA) Lini 2 | `pemeriksaan_lpa_line_probe_assay_lini_2_hasil_pemeriksaan_invalid` → `Observation.valueCodeableConcept.coding` (1367)<br>_MTB_ → `Observation.component.code.coding` (1370, tanpa BQ)<br>`pemeriksaan_lpa_line_probe_assay_lini_2_hasil_pemeriksaan_mtb` → `Observation.component.valueCodeableConcept.coding` (1371)<br>_Levofloksasin_ → `Observation.component.code.coding` (1374, tanpa BQ)<br>`pemeriksaan_lpa_line_probe_assay_lini_2_hasil_pemeriksaan_fq_lfx` → `Observation.component.valueCodeableConcept.coding` (1375)<br>_Moksifloksasin_ → `Observation.component.code.coding` (1380, tanpa BQ)<br>`pemeriksaan_lpa_line_probe_assay_lini_2_hasil_pemeriksaan_fq_mfx` → `Observation.component.valueCodeableConcept.coding` (1381)<br>_Moksifloksasin Dosis Tinggi_ → `Observation.component.code.coding` (1386, tanpa BQ)<br>`pemeriksaan_lpa_line_probe_assay_lini_2_hasil_pemeriksaan_fq_mfx_dosis_tinggi` → `Observation.component.valueCodeableConcept.coding` (1387)<br>_Kanamisin_ → `Observation.component.code.coding` (1392, tanpa BQ)<br>`pemeriksaan_lpa_line_probe_assay_lini_2_hasil_pemeriksaan_slid_km` → `Observation.component.valueCodeableConcept.coding` (1393)<br>_Amikasin_ → `Observation.component.code.coding` (1398, tanpa BQ)<br>`pemeriksaan_lpa_line_probe_assay_lini_2_hasil_pemeriksaan_slid_amk` → `Observation.component.valueCodeableConcept.coding` (1399)<br>_Kapreomisin_ → `Observation.component.code.coding` (1404, tanpa BQ)<br>`pemeriksaan_lpa_line_probe_assay_lini_2_hasil_pemeriksaan_slid_cm` → `Observation.component.valueCodeableConcept.coding` (1405)<br>`pemeriksaan_lpa_line_probe_assay_lini_2_tgl_hasil_dilaporkan` → `Observation.issued` (1414) |
| 61 | 1418–1430 | DiagnosticReport | X099381 | Line Probe Assay (LPA) Lini 2 | – |
| 62 | 1437–1466 | ServiceRequest | X099389 | Hasil Pemeriksaan Biakan TB (Metode: LJ) | _Pemeriksaan Biakan_ → `ServiceRequest.identifier` (1437, tanpa BQ)<br>`pemeriksaan_biakan_tgl_contoh_uji_diterima_untuk_pemeriksaan_biakan_dan_uji_kepekaan` → `ServiceRequest.occurrenceDateTime` (1446)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (1447) |
| 63 | 1468–1487 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (1469)<br>`pemeriksaan_biakan_jenis_contoh_uji` → `Specimen.type.coding` (1471) |
| 64 | 1489–1510 | Observation | X099389 | Hasil Pemeriksaan Biakan TB (Metode: LJ) | `pemeriksaan_biakan_metode_uji` → `Observation.method.coding` (1490)<br>`pemeriksaan_biakan_hasil_pemeriksaan` → `Observation.valueCodeableConcept.coding` (1496)<br>`pemeriksaan_biakan_tgl_hasil_dilaporkan` → `Observation.issued` (1508) |
| 65 | 1512–1525 | DiagnosticReport | X099389 | Hasil Pemeriksaan Biakan TB (Metode: LJ) | – |
| 66 | 1528–1556 | ServiceRequest | X099383 | Pemeriksaan Paket Standar Kepekaan | _Pemeriksaan Paket Standar Uji Kepekaan_ → `ServiceRequest.identifier` (1528, tanpa BQ)<br>`pemeriksaan_paket_standar_uji_kepekaan_tgl_hasil_dilaporkan` → `ServiceRequest.occurrenceDateTime` (1536)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (1537) |
| 67 | 1558–1577 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (1559)<br>_Jenis Contoh Uji_ → `Specimen.type.coding` (1561, tanpa BQ) |
| 68 | 1579–1651 | Observation | X099383 | Pemeriksaan Paket Standar Kepekaan | _Isoniazid_ → `Observation.component.code.coding` (1584, tanpa BQ)<br>`pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_h` → `Observation.component.valueCodeableConcept.coding` (1585)<br>_Isoniazid Dosis Tinggi_ → `Observation.component.code.coding` (1590, tanpa BQ)<br>`pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_h_dosis_tinggi` → `Observation.component.valueCodeableConcept.coding` (1591)<br>_Levofloksasin_ → `Observation.component.code.coding` (1596, tanpa BQ)<br>`pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_lfx` → `Observation.component.valueCodeableConcept.coding` (1597)<br>_Moksifloksasin_ → `Observation.component.code.coding` (1602, tanpa BQ)<br>`pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_mfx` → `Observation.component.valueCodeableConcept.coding` (1603)<br>_Moksifloksasin Dosis Tinggi_ → `Observation.component.code.coding` (1608, tanpa BQ)<br>`pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_mfx_dosis_tinggi` → `Observation.component.valueCodeableConcept.coding` (1609)<br>_Kanamisin_ → `Observation.component.code.coding` (1614, tanpa BQ)<br>`pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_km` → `Observation.component.valueCodeableConcept.coding` (1615)<br>_Amikasin_ → `Observation.component.code.coding` (1620, tanpa BQ)<br>_Hasil Pemeriksaan Amk_ → `Observation.component.valueCodeableConcept.coding` (1621, tanpa BQ)<br>_Kapreomisin_ → `Observation.component.code.coding` (1626, tanpa BQ)<br>`pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_cm` → `Observation.component.valueCodeableConcept.coding` (1627)<br>`pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan` → `Observation.component.code.coding` (1632)<br>`pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_1` → `Observation.component.code.coding` (1634)<br>`pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_2` → `Observation.component.code.coding` (1636)<br>`pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_3` → `Observation.component.code.coding` (1638)<br>`pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_4` → `Observation.component.code.coding` (1640)<br>`pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_5` → `Observation.component.code.coding` (1642) |
| 69 | 1653–1665 | DiagnosticReport | X099383 | Pemeriksaan Paket Standar Kepekaan | – |

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
| 5 | 91 | Condition | `Condition.code.coding` | 171126009 | Tuberculosis screening | http://snomed.info/sct |
| 6 | 100 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 7 | 119 | ServiceRequest | `ServiceRequest.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 8 | 123 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 9 | 124 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 10 | 126 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 11 | 128 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 12 | 130 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 13 | 132 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 14 | 134 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 15 | 136 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 16 | 138 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 17 | 140 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 18 | 147 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 19 | 148 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 20 | 149 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 21 | 150 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 22 | 151 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 23 | 152 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 24 | 153 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 25 | 154 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 26 | 155 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 27 | 156 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 28 | 157 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 29 | 168 | Observation | `Observation.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 30 | 169 | Observation | `Observation.valueCodeableConcept.coding` | 260385009 | Negative | http://snomed.info/sct |
| 31 | 170 | Observation | `Observation.valueCodeableConcept.coding` | LA11841-6 | 1+ | http://loinc.org |
| 32 | 171 | Observation | `Observation.valueCodeableConcept.coding` | LA11842-4 | 2+ | http://loinc.org |
| 33 | 172 | Observation | `Observation.valueCodeableConcept.coding` | LA11843-2 | 3+ | http://loinc.org |
| 34 | 186 | DiagnosticReport | `DiagnosticReport.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 35 | 202 | ServiceRequest | `ServiceRequest.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 36 | 206 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 37 | 207 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 38 | 209 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 39 | 211 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 40 | 213 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 41 | 215 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 42 | 217 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 43 | 219 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 44 | 221 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 45 | 223 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 46 | 230 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 47 | 231 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 48 | 232 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 49 | 233 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 50 | 234 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 51 | 235 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 52 | 236 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 53 | 237 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 54 | 238 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 55 | 239 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 56 | 240 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 57 | 252 | Observation | `Observation.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 58 | 253 | Observation | `Observation.valueCodeableConcept.coding` | 260385009 | Negative | http://snomed.info/sct |
| 59 | 254 | Observation | `Observation.valueCodeableConcept.coding` | LA11841-6 | 1+ | http://loinc.org |
| 60 | 255 | Observation | `Observation.valueCodeableConcept.coding` | LA11842-4 | 2+ | http://loinc.org |
| 61 | 256 | Observation | `Observation.valueCodeableConcept.coding` | LA11843-2 | 3+ | http://loinc.org |
| 62 | 270 | DiagnosticReport | `DiagnosticReport.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 63 | 289 | ServiceRequest | `ServiceRequest.code.coding` | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | http://terminology.kemkes.go.id/sp |
| 64 | 293 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 65 | 294 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 66 | 296 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 67 | 298 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 68 | 300 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 69 | 302 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 70 | 304 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 71 | 306 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 72 | 308 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 73 | 310 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 74 | 317 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 75 | 318 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 76 | 319 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 77 | 320 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 78 | 321 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 79 | 322 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 80 | 323 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 81 | 324 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 82 | 325 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 83 | 326 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 84 | 327 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 85 | 340 | Observation | `Observation.code.coding` | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | http://terminology.kemkes.go.id/sp |
| 86 | 341 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 87 | 342 | Observation | `Observation.valueCodeableConcept.coding` | X099770 | Rifampisin sensitive | http://terminology.kemkes.go.id/CodeSystem/examination |
| 88 | 343 | Observation | `Observation.valueCodeableConcept.coding` | X099771 | Rifampisin resistan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 89 | 344 | Observation | `Observation.valueCodeableConcept.coding` | X099772 | Rifampisin indeterminate | http://terminology.kemkes.go.id/CodeSystem/examination |
| 90 | 360 | DiagnosticReport | `DiagnosticReport.code.coding` | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | http://terminology.kemkes.go.id/sp |
| 91 | 376 | ServiceRequest | `ServiceRequest.code.coding` | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | http://terminology.kemkes.go.id/sp |
| 92 | 380 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 93 | 381 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 94 | 383 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 95 | 385 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 96 | 387 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 97 | 389 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 98 | 391 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 99 | 393 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 100 | 395 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 101 | 397 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 102 | 404 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 103 | 405 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 104 | 406 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 105 | 407 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 106 | 408 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 107 | 409 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 108 | 410 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 109 | 411 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 110 | 412 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 111 | 413 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 112 | 414 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 113 | 426 | Observation | `Observation.code.coding` | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | http://terminology.kemkes.go.id/sp |
| 114 | 427 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 115 | 428 | Observation | `Observation.valueCodeableConcept.coding` | X099770 | Rifampisin sensitive | http://terminology.kemkes.go.id/CodeSystem/examination |
| 116 | 429 | Observation | `Observation.valueCodeableConcept.coding` | X099771 | Rifampisin resistan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 117 | 430 | Observation | `Observation.valueCodeableConcept.coding` | X099772 | Rifampisin indeterminate | http://terminology.kemkes.go.id/CodeSystem/examination |
| 118 | 446 | DiagnosticReport | `DiagnosticReport.code.coding` | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | http://terminology.kemkes.go.id/sp |
| 119 | 465 | ServiceRequest | `ServiceRequest.code.coding` | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | http://terminology.kemkes.go.id/sp |
| 120 | 469 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 121 | 470 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 122 | 472 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 123 | 474 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 124 | 476 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 125 | 478 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 126 | 480 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 127 | 482 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 128 | 484 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 129 | 486 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 130 | 493 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 131 | 494 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 132 | 495 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 133 | 496 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 134 | 497 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 135 | 498 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 136 | 499 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 137 | 500 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 138 | 501 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 139 | 502 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 140 | 503 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 141 | 515 | Observation | `Observation.code.coding` | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | http://terminology.kemkes.go.id/sp |
| 142 | 528 | DiagnosticReport | `DiagnosticReport.code.coding` | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | http://terminology.kemkes.go.id/sp |
| 143 | 544 | ServiceRequest | `ServiceRequest.code.coding` | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | http://terminology.kemkes.go.id/sp |
| 144 | 548 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 145 | 549 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 146 | 551 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 147 | 553 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 148 | 555 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 149 | 557 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 150 | 559 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 151 | 561 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 152 | 563 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 153 | 565 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 154 | 573 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 155 | 574 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 156 | 575 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 157 | 576 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 158 | 577 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 159 | 578 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 160 | 579 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 161 | 580 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 162 | 581 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 163 | 582 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 164 | 583 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 165 | 595 | Observation | `Observation.code.coding` | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | http://terminology.kemkes.go.id/sp |
| 166 | 608 | DiagnosticReport | `DiagnosticReport.code.coding` | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | http://terminology.kemkes.go.id/sp |
| 167 | 624 | ServiceRequest | `ServiceRequest.code.coding` | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | http://terminology.kemkes.go.id/sp |
| 168 | 628 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 169 | 629 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 170 | 631 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 171 | 633 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 172 | 635 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 173 | 637 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 174 | 639 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 175 | 641 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 176 | 643 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 177 | 645 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 178 | 653 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 179 | 654 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 180 | 655 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 181 | 656 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 182 | 657 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 183 | 658 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 184 | 659 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 185 | 660 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 186 | 661 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 187 | 662 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 188 | 663 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 189 | 674 | Observation | `Observation.code.coding` | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | http://terminology.kemkes.go.id/sp |
| 190 | 687 | DiagnosticReport | `DiagnosticReport.code.coding` | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | http://terminology.kemkes.go.id/sp |
| 191 | 703 | ServiceRequest | `ServiceRequest.code.coding` | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | http://terminology.kemkes.go.id/sp |
| 192 | 707 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 193 | 708 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 194 | 710 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 195 | 712 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 196 | 714 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 197 | 716 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 198 | 718 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 199 | 720 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 200 | 722 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 201 | 724 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 202 | 731 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 203 | 732 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 204 | 733 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 205 | 734 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 206 | 735 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 207 | 736 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 208 | 737 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 209 | 738 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 210 | 739 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 211 | 740 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 212 | 741 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 213 | 753 | Observation | `Observation.code.coding` | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | http://terminology.kemkes.go.id/sp |
| 214 | 766 | DiagnosticReport | `DiagnosticReport.code.coding` | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | http://terminology.kemkes.go.id/sp |
| 215 | 785 | ServiceRequest | `ServiceRequest.code.coding` | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 216 | 789 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 217 | 790 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 218 | 792 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 219 | 794 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 220 | 796 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 221 | 798 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 222 | 800 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 223 | 802 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 224 | 804 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 225 | 806 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 226 | 813 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 227 | 814 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 228 | 815 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 229 | 816 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 230 | 817 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 231 | 818 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 232 | 819 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 233 | 820 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 234 | 821 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 235 | 822 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 236 | 823 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 237 | 835 | Observation | `Observation.code.coding` | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 238 | 836 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 239 | 837 | Observation | `Observation.valueCodeableConcept.coding` | X099770 | Rifampisin sensitive | http://terminology.kemkes.go.id/CodeSystem/examination |
| 240 | 838 | Observation | `Observation.valueCodeableConcept.coding` | X099771 | Rifampisin resistan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 241 | 839 | Observation | `Observation.valueCodeableConcept.coding` | X099772 | Rifampisin indeterminate | http://terminology.kemkes.go.id/CodeSystem/examination |
| 242 | 855 | DiagnosticReport | `DiagnosticReport.code.coding` | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 243 | 871 | ServiceRequest | `ServiceRequest.code.coding` | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 244 | 875 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 245 | 876 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 246 | 878 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 247 | 880 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 248 | 882 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 249 | 884 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 250 | 886 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 251 | 888 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 252 | 890 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 253 | 892 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 254 | 899 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 255 | 900 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 256 | 901 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 257 | 902 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 258 | 903 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 259 | 904 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 260 | 905 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 261 | 906 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 262 | 907 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 263 | 908 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 264 | 909 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 265 | 921 | Observation | `Observation.code.coding` | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 266 | 922 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 267 | 923 | Observation | `Observation.valueCodeableConcept.coding` | X099770 | Rifampisin sensitive | http://terminology.kemkes.go.id/CodeSystem/examination |
| 268 | 924 | Observation | `Observation.valueCodeableConcept.coding` | X099771 | Rifampisin resistan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 269 | 925 | Observation | `Observation.valueCodeableConcept.coding` | X099772 | Rifampisin indeterminate | http://terminology.kemkes.go.id/CodeSystem/examination |
| 270 | 941 | DiagnosticReport | `DiagnosticReport.code.coding` | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 271 | 961 | ServiceRequest | `ServiceRequest.code.coding` | MK099927 | Pemeriksaan PCR Open System | http://terminology.kemkes.go.id/CodeSystem/examination |
| 272 | 965 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 273 | 966 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 274 | 968 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 275 | 970 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 276 | 972 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 277 | 974 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 278 | 976 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 279 | 978 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 280 | 980 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 281 | 982 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 282 | 989 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 283 | 990 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 284 | 991 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 285 | 992 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 286 | 993 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 287 | 994 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 288 | 995 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 289 | 996 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 290 | 997 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 291 | 998 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 292 | 999 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 293 | 1011 | Observation | `Observation.code.coding` | MK099927 | Pemeriksaan PCR Open System | http://terminology.kemkes.go.id/CodeSystem/examination |
| 294 | 1012 | Observation | `Observation.component.code.coding` | 13956-8 | Mycobacterium tuberculosis DNA [Presence] in Specimen by NAA with probe detection | http://loinc.org |
| 295 | 1013 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 296 | 1014 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 297 | 1018 | Observation | `Observation.component.code.coding` | 89489-9 | rifAMPin [Susceptibility] by Genotype method | http://loinc.org |
| 298 | 1019 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 299 | 1020 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 300 | 1022 | Observation | `Observation.component.code.coding` | 89488-1 | Isoniazid [Susceptibility] by Genotype method | http://loinc.org |
| 301 | 1023 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 302 | 1024 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 303 | 1026 | Observation | `Observation.component.code.coding` | 46246-5 | Mycobacterium tuberculosis katG gene isoniazid high level resistance mutation [Identifier] by Molecular method | http://loinc.org |
| 304 | 1027 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 305 | 1028 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 306 | 1029 | Observation | `Observation.component.code.coding` | 63072-3 | Mycobacterium tuberculosis inhA gene isoniazid low level resistance mutation [Presence] by Molecular method | http://loinc.org |
| 307 | 1030 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 308 | 1031 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 309 | 1032 | Observation | `Observation.component.code.coding` | 110379001 | Mycobacterium, non-tuberculosis (organism) | http://snomed.info/sct |
| 310 | 1033 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 311 | 1034 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 312 | 1047 | DiagnosticReport | `DiagnosticReport.code.coding` | MK099927 | Pemeriksaan PCR Open System | http://terminology.kemkes.go.id/CodeSystem/examination |
| 313 | 1067 | ServiceRequest | `ServiceRequest.code.coding` | X099379 | Pemeriksaan TCM XDR | http://terminology.kemkes.go.id/CodeSystem/examination |
| 314 | 1071 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 315 | 1072 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 316 | 1074 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 317 | 1076 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 318 | 1078 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 319 | 1080 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 320 | 1082 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 321 | 1084 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 322 | 1086 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 323 | 1088 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 324 | 1095 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 325 | 1096 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 326 | 1097 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 327 | 1098 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 328 | 1099 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 329 | 1100 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 330 | 1101 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 331 | 1102 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 332 | 1103 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 333 | 1104 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 334 | 1105 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 335 | 1118 | Observation | `Observation.code.coding` | X099379 | Pemeriksaan TCM XDR | http://terminology.kemkes.go.id/CodeSystem/examination |
| 336 | 1119 | Observation | `Observation.valueCodeableConcept.coding` | X099781 | Hasil Valid | http://terminology.kemkes.go.id/CodeSystem/examination |
| 337 | 1124 | Observation | `Observation.component.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 338 | 1125 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 339 | 1126 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 340 | 1128 | Observation | `Observation.component.code.coding` | X099391 | H Dosis Rendah (Low) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 341 | 1129 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 342 | 1130 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 343 | 1131 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 344 | 1133 | Observation | `Observation.component.code.coding` | 89488-1 | Isoniazid [Susceptibility] by Genotype method | http://loinc.org |
| 345 | 1134 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 346 | 1135 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 347 | 1136 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 348 | 1138 | Observation | `Observation.component.code.coding` | 96110-2 | Ethionamide [Susceptibility] by Genotype method | http://loinc.org |
| 349 | 1139 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 350 | 1140 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 351 | 1142 | Observation | `Observation.component.code.coding` | X099392 | FQ Dosis Rendah (Low) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 352 | 1143 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 353 | 1144 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 354 | 1145 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 355 | 1147 | Observation | `Observation.component.code.coding` | 89487-3 | Fluoroquinolone [Susceptibility] by Genotype method | http://loinc.org |
| 356 | 1148 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 357 | 1149 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 358 | 1150 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 359 | 1152 | Observation | `Observation.component.code.coding` | 89484-0 | Amikacin [Susceptibility] by Genotype method | http://loinc.org |
| 360 | 1153 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 361 | 1154 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 362 | 1155 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 363 | 1157 | Observation | `Observation.component.code.coding` | 89482-4 | Kanamycin [Susceptibility] by Genotype method | http://loinc.org |
| 364 | 1158 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 365 | 1159 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 366 | 1160 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 367 | 1162 | Observation | `Observation.component.code.coding` | 89483-2 | Capreomycin [Susceptibility] by Genotype method | http://loinc.org |
| 368 | 1163 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 369 | 1164 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 370 | 1165 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 371 | 1178 | DiagnosticReport | `DiagnosticReport.code.coding` | X099379 | Pemeriksaan TCM XDR | http://terminology.kemkes.go.id/CodeSystem/examination |
| 372 | 1198 | ServiceRequest | `ServiceRequest.code.coding` | X099380 | Line Probe Assay (LPA) Lini 1 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 373 | 1202 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 374 | 1203 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 375 | 1205 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 376 | 1207 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 377 | 1209 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 378 | 1211 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 379 | 1213 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 380 | 1215 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 381 | 1217 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 382 | 1219 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 383 | 1226 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 384 | 1227 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 385 | 1228 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 386 | 1229 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 387 | 1230 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 388 | 1231 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 389 | 1232 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 390 | 1233 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 391 | 1234 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 392 | 1235 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 393 | 1236 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 394 | 1248 | Observation | `Observation.code.coding` | X099380 | Line Probe Assay (LPA) Lini 1 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 395 | 1249 | Observation | `Observation.valueCodeableConcept.coding` | X099781 | Hasil Valid | http://terminology.kemkes.go.id/CodeSystem/examination |
| 396 | 1252 | Observation | `Observation.component.code.coding` | 13956-8 | Mycobacterium tuberculosis DNA [Presence] in Specimen by NAA with probe detection | http://loinc.org |
| 397 | 1253 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 398 | 1254 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 399 | 1256 | Observation | `Observation.component.code.coding` | 89489-9 | rifAMPin [Susceptibility] by Genotype method | http://loinc.org |
| 400 | 1257 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 401 | 1258 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 402 | 1259 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 403 | 1260 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 404 | 1262 | Observation | `Observation.component.code.coding` | X099391 | H Dosis Rendah (Low) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 405 | 1263 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 406 | 1264 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 407 | 1265 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 408 | 1266 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 409 | 1268 | Observation | `Observation.component.code.coding` | X099783 | H Dosis Tinggi (High) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 410 | 1269 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 411 | 1270 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 412 | 1271 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 413 | 1272 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 414 | 1274 | Observation | `Observation.component.code.coding` | 96110-2 | Ethionamide [Susceptibility] by Genotype method | http://loinc.org |
| 415 | 1275 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 416 | 1276 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 417 | 1277 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 418 | 1278 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 419 | 1280 | Observation | `Observation.component.code.coding` | 103960-1 | Prothionamide [Susceptibility] by Genotype method | http://loinc.org |
| 420 | 1281 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 421 | 1282 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 422 | 1283 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 423 | 1284 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 424 | 1297 | DiagnosticReport | `DiagnosticReport.code.coding` | X099380 | Line Probe Assay (LPA) Lini 1 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 425 | 1317 | ServiceRequest | `ServiceRequest.code.coding` | X099381 | Line Probe Assay (LPA) Lini 2 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 426 | 1321 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 427 | 1322 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 428 | 1324 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 429 | 1326 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 430 | 1328 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 431 | 1330 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 432 | 1332 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 433 | 1334 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 434 | 1336 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 435 | 1338 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 436 | 1345 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 437 | 1346 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 438 | 1347 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 439 | 1348 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 440 | 1349 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 441 | 1350 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 442 | 1351 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 443 | 1352 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 444 | 1353 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 445 | 1354 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 446 | 1355 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 447 | 1366 | Observation | `Observation.code.coding` | X099381 | Line Probe Assay (LPA) Lini 2 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 448 | 1367 | Observation | `Observation.valueCodeableConcept.coding` | X099781 | Hasil Valid | http://terminology.kemkes.go.id/CodeSystem/examination |
| 449 | 1370 | Observation | `Observation.component.code.coding` | 13956-8 | Mycobacterium tuberculosis DNA [Presence] in Specimen by NAA with probe detection | http://loinc.org |
| 450 | 1371 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 451 | 1372 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 452 | 1374 | Observation | `Observation.component.code.coding` | 20629-2 | levoFLOXacin [Susceptibility] | http://loinc.org |
| 453 | 1375 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 454 | 1376 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 455 | 1377 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 456 | 1378 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 457 | 1380 | Observation | `Observation.component.code.coding` | 96112-8 | Moxifloxacin [Susceptibility] by Genotype method | http://loinc.org |
| 458 | 1381 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 459 | 1382 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 460 | 1383 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 461 | 1384 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 462 | 1386 | Observation | `Observation.component.code.coding` | X099775 | Moxifloxacin DT (Mfx DT) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 463 | 1387 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 464 | 1388 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 465 | 1389 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 466 | 1390 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 467 | 1392 | Observation | `Observation.component.code.coding` | 89482-4 | Kanamycin [Susceptibility] by Genotype method | http://loinc.org |
| 468 | 1393 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 469 | 1394 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 470 | 1395 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 471 | 1396 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 472 | 1398 | Observation | `Observation.component.code.coding` | 89484-0 | Amikacin [Susceptibility] by Genotype method | http://loinc.org |
| 473 | 1399 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 474 | 1400 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 475 | 1401 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 476 | 1402 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 477 | 1404 | Observation | `Observation.component.code.coding` | 89483-2 | Capreomycin [Susceptibility] by Genotype method | http://loinc.org |
| 478 | 1405 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 479 | 1406 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 480 | 1407 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 481 | 1408 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 482 | 1421 | DiagnosticReport | `DiagnosticReport.code.coding` | X099381 | Line Probe Assay (LPA) Lini 2 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 483 | 1442 | ServiceRequest | `ServiceRequest.code.coding` | X099389 | Hasil Pemeriksaan Biakan TB (Metode: LJ) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 484 | 1443 | ServiceRequest | `ServiceRequest.code.coding` | X099390 | Hasil Pemeriksaan Biakan TB (Metode: MGIT) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 485 | 1447 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 486 | 1448 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 487 | 1450 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 488 | 1452 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 489 | 1454 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 490 | 1456 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 491 | 1458 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 492 | 1460 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 493 | 1462 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 494 | 1464 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 495 | 1471 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 496 | 1472 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 497 | 1473 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 498 | 1474 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 499 | 1475 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 500 | 1476 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 501 | 1477 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 502 | 1478 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 503 | 1479 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 504 | 1480 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 505 | 1481 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 506 | 1490 | Observation | `Observation.method.coding` | OM000001 | LJ | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 507 | 1491 | Observation | `Observation.method.coding` | OM000002 | MGIT | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 508 | 1494 | Observation | `Observation.code.coding` | X099389 | Hasil Pemeriksaan Biakan TB (Metode: LJ) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 509 | 1495 | Observation | `Observation.code.coding` | X099390 | Hasil Pemeriksaan Biakan TB (Metode: MGIT) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 510 | 1496 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 511 | 1497 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 512 | 1498 | Observation | `Observation.valueCodeableConcept.coding` | LA11841-6 | + | http://loinc.org |
| 513 | 1499 | Observation | `Observation.valueCodeableConcept.coding` | LA11842-4 | ++ | http://loinc.org |
| 514 | 1500 | Observation | `Observation.valueCodeableConcept.coding` | LA11843-2 | +++ | http://loinc.org |
| 515 | 1501 | Observation | `Observation.valueCodeableConcept.coding` | 110379001 | Mycobacterium, non-tuberculosis (organism) | http://snomed.info/sct |
| 516 | 1515 | DiagnosticReport | `DiagnosticReport.code.coding` | X099389 | Hasil Pemeriksaan Biakan TB (Metode: LJ) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 517 | 1516 | DiagnosticReport | `DiagnosticReport.code.coding` | X099390 | Hasil Pemeriksaan Biakan TB (Metode: MGIT) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 518 | 1533 | ServiceRequest | `ServiceRequest.code.coding` | X099383 | Pemeriksaan Paket Standar Kepekaan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 519 | 1537 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 520 | 1538 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 521 | 1540 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 522 | 1542 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 523 | 1544 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 524 | 1546 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 525 | 1548 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 526 | 1550 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 527 | 1552 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 528 | 1554 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 529 | 1561 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 530 | 1562 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 531 | 1563 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 532 | 1564 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 533 | 1565 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 534 | 1566 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 535 | 1567 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 536 | 1568 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 537 | 1569 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 538 | 1570 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 539 | 1571 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 540 | 1582 | Observation | `Observation.code.coding` | X099383 | Pemeriksaan Paket Standar Kepekaan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 541 | 1584 | Observation | `Observation.component.code.coding` | 20383-6 | Isoniazid [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 542 | 1585 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 543 | 1586 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 544 | 1587 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 545 | 1590 | Observation | `Observation.component.code.coding` | X099776 | H High Dosage [Susceptibility] by Method for Slow-growing mycobacteria | http://terminology.kemkes.go.id/CodeSystem/examination |
| 546 | 1591 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 547 | 1592 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 548 | 1593 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 549 | 1596 | Observation | `Observation.component.code.coding` | 53716-7 | levoFLOXacin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 550 | 1597 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 551 | 1598 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 552 | 1599 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 553 | 1602 | Observation | `Observation.component.code.coding` | 41502-6 | Moxifloxacin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 554 | 1603 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 555 | 1604 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 556 | 1605 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 557 | 1608 | Observation | `Observation.component.code.coding` | X099778 | Moxifloxacin High Dosage [Susceptibility] by Method for Slow-growing mycobacteria | http://terminology.kemkes.go.id/CodeSystem/examination |
| 558 | 1609 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 559 | 1610 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 560 | 1611 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 561 | 1614 | Observation | `Observation.component.code.coding` | 23609-1 | Kanamycin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 562 | 1615 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 563 | 1616 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 564 | 1617 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 565 | 1620 | Observation | `Observation.component.code.coding` | 20373-7 | Amikacin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 566 | 1621 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 567 | 1622 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 568 | 1623 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 569 | 1626 | Observation | `Observation.component.code.coding` | 23607-5 | Capreomycin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 570 | 1627 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 571 | 1628 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 572 | 1629 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 573 | 1632 | Observation | `Observation.component.code.coding` | SP000472 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya | http://terminology.kemkes.go.id/sp |
| 574 | 1634 | Observation | `Observation.component.code.coding` | SP000473 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 1 | http://terminology.kemkes.go.id/sp |
| 575 | 1636 | Observation | `Observation.component.code.coding` | SP000474 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 2 | http://terminology.kemkes.go.id/sp |
| 576 | 1638 | Observation | `Observation.component.code.coding` | SP000475 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 3 | http://terminology.kemkes.go.id/sp |
| 577 | 1640 | Observation | `Observation.component.code.coding` | SP000476 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 4 | http://terminology.kemkes.go.id/sp |
| 578 | 1642 | Observation | `Observation.component.code.coding` | SP000477 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 5 | http://terminology.kemkes.go.id/sp |
| 579 | 1656 | DiagnosticReport | `DiagnosticReport.code.coding` | X099383 | Pemeriksaan Paket Standar Kepekaan | http://terminology.kemkes.go.id/CodeSystem/examination |

### Code per CodeSystem

| CodeSystem | Jumlah | Code |
|---|---|---|
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 195 | EHA000002, SRR000013, SRR000007, SRR000007, SRR000009, SRR000009, SRR000009, SRR000008, SRR000008, SRR000008, SRR000010, ST000001, ST000002, SRR000013, SRR000007, SRR000007, SRR000009, SRR000009, SRR000009, SRR000008, SRR000008, SRR000008, SRR000010, ST000001, ST000002, SRR000013, SRR000007, SRR000007, SRR000009, SRR000009, SRR000009, SRR000008, SRR000008, SRR000008, SRR000010, ST000001, ST000002, SRR000013, SRR000007, SRR000007, SRR000009, SRR000009, SRR000009, SRR000008, SRR000008, SRR000008, SRR000010, ST000001, ST000002, SRR000013, SRR000007, SRR000007, SRR000009, SRR000009, SRR000009, SRR000008, SRR000008, SRR000008, SRR000010, ST000001, ST000002, SRR000013, SRR000007, SRR000007, SRR000009, SRR000009, SRR000009, SRR000008, SRR000008, SRR000008, SRR000010, ST000001, ST000002, SRR000013, SRR000007, SRR000007, SRR000009, SRR000009, SRR000009, SRR000008, SRR000008, SRR000008, SRR000010, ST000001, ST000002, SRR000013, SRR000007, SRR000007, SRR000009, SRR000009, SRR000009, SRR000008, SRR000008, SRR000008, SRR000010, ST000001, ST000002, SRR000013, SRR000007, SRR000007, SRR000009, SRR000009, SRR000009, SRR000008, SRR000008, SRR000008, SRR000010, ST000001, ST000002, SRR000013, SRR000007, SRR000007, SRR000009, SRR000009, SRR000009, SRR000008, SRR000008, SRR000008, SRR000010, ST000001, ST000002, SRR000013, SRR000007, SRR000007, SRR000009, SRR000009, SRR000009, SRR000008, SRR000008, SRR000008, SRR000010, ST000001, ST000002, SRR000013, SRR000007, SRR000007, SRR000009, SRR000009, SRR000009, SRR000008, SRR000008, SRR000008, SRR000010, ST000001, ST000002, SRR000013, SRR000007, SRR000007, SRR000009, SRR000009, SRR000009, SRR000008, SRR000008, SRR000008, SRR000010, ST000001, ST000002, SRR000013, SRR000007, SRR000007, SRR000009, SRR000009, SRR000009, SRR000008, SRR000008, SRR000008, SRR000010, ST000001, ST000002, SRR000013, SRR000007, SRR000007, SRR000009, SRR000009, SRR000009, SRR000008, SRR000008, SRR000008, SRR000010, ST000001, ST000002, OM000001, OM000002, SRR000013, SRR000007, SRR000007, SRR000009, SRR000009, SRR000009, SRR000008, SRR000008, SRR000008, SRR000010, ST000001, ST000002 |
| http://snomed.info/sct | 151 | 257622000, 171126009, 424144002, 418564007, 119334006, 119334006, 258450006, 119376003, 309508006, 168137004, 119303007, 123038009, 260385009, 418564007, 119334006, 119334006, 258450006, 119376003, 309508006, 168137004, 119303007, 123038009, 260385009, 418564007, 119334006, 119334006, 258450006, 119376003, 309508006, 168137004, 119303007, 123038009, 418564007, 119334006, 119334006, 258450006, 119376003, 309508006, 168137004, 119303007, 123038009, 418564007, 119334006, 119334006, 258450006, 119376003, 309508006, 168137004, 119303007, 123038009, 418564007, 119334006, 119334006, 258450006, 119376003, 309508006, 168137004, 119303007, 123038009, 418564007, 119334006, 119334006, 258450006, 119376003, 309508006, 168137004, 119303007, 123038009, 418564007, 119334006, 119334006, 258450006, 119376003, 309508006, 168137004, 119303007, 123038009, 418564007, 119334006, 119334006, 258450006, 119376003, 309508006, 168137004, 119303007, 123038009, 418564007, 119334006, 119334006, 258450006, 119376003, 309508006, 168137004, 119303007, 123038009, 418564007, 119334006, 119334006, 258450006, 119376003, 309508006, 168137004, 119303007, 123038009, 110379001, 418564007, 119334006, 119334006, 258450006, 119376003, 309508006, 168137004, 119303007, 123038009, 418564007, 119334006, 119334006, 258450006, 119376003, 309508006, 168137004, 119303007, 123038009, 418564007, 119334006, 119334006, 258450006, 119376003, 309508006, 168137004, 119303007, 123038009, 418564007, 119334006, 119334006, 258450006, 119376003, 309508006, 168137004, 119303007, 123038009, 110379001, 418564007, 119334006, 119334006, 258450006, 119376003, 309508006, 168137004, 119303007, 123038009 |
| http://loinc.org | 147 | 11545-1, 11545-1, LA11841-6, LA11842-4, LA11843-2, 11545-1, 11545-1, 11545-1, LA11841-6, LA11842-4, LA11843-2, 11545-1, LA6577-6, LA6577-6, LA6577-6, LA6577-6, 13956-8, LA11882-0, LA11883-8, 89489-9, LA11882-0, LA11883-8, 89488-1, LA11882-0, LA11883-8, 46246-5, LA11882-0, LA11883-8, 63072-3, LA11882-0, LA11883-8, LA11882-0, LA11883-8, 88874-3, LA11882-0, LA11883-8, LA11882-0, LA11883-8, LA11884-6, 89488-1, LA11882-0, LA11883-8, LA11884-6, 96110-2, LA11882-0, LA11883-8, LA11882-0, LA11883-8, LA11884-6, 89487-3, LA11882-0, LA11883-8, LA11884-6, 89484-0, LA11882-0, LA11883-8, LA11884-6, 89482-4, LA11882-0, LA11883-8, LA11884-6, 89483-2, LA11882-0, LA11883-8, LA11884-6, 13956-8, LA6576-8, LA6577-6, 89489-9, LA11882-0, LA11883-8, LA11884-6, LA11882-0, LA11883-8, LA11884-6, LA11882-0, LA11883-8, LA11884-6, 96110-2, LA11882-0, LA11883-8, LA11884-6, 103960-1, LA11882-0, LA11883-8, LA11884-6, 13956-8, LA6576-8, LA6577-6, 20629-2, LA11882-0, LA11883-8, LA11884-6, 96112-8, LA11882-0, LA11883-8, LA11884-6, LA11882-0, LA11883-8, LA11884-6, 89482-4, LA11882-0, LA11883-8, LA11884-6, 89484-0, LA11882-0, LA11883-8, LA11884-6, 89483-2, LA11882-0, LA11883-8, LA11884-6, LA6577-6, LA6576-8, LA11841-6, LA11842-4, LA11843-2, 20383-6, LA24225-7, LA6676-6, LA16550-8, LA24225-7, LA6676-6, LA16550-8, 53716-7, LA24225-7, LA6676-6, LA16550-8, 41502-6, LA24225-7, LA6676-6, LA16550-8, LA24225-7, LA6676-6, LA16550-8, 23609-1, LA24225-7, LA6676-6, LA16550-8, 20373-7, LA24225-7, LA6676-6, LA16550-8, 23607-5, LA24225-7, LA6676-6, LA16550-8 |
| http://terminology.kemkes.go.id/CodeSystem/examination | 60 | X099770, X099771, X099772, X099770, X099771, X099772, MK099926, MK099926, X099770, X099771, X099772, MK099926, MK099926, MK099926, X099770, X099771, X099772, MK099926, MK099927, MK099927, MK099927, X099379, X099379, X099781, X099391, X099392, X099379, X099380, X099380, X099781, X099774, X099391, X099774, X099783, X099774, X099774, X099774, X099380, X099381, X099381, X099781, X099774, X099774, X099775, X099774, X099774, X099774, X099774, X099381, X099389, X099390, X099389, X099390, X099389, X099390, X099383, X099383, X099776, X099778, X099383 |
| http://terminology.kemkes.go.id/sp | 24 | SP000720, SP000720, SP000720, SP000720, SP000720, SP000720, SP000721, SP000721, SP000721, SP000721, SP000721, SP000721, SP000722, SP000722, SP000722, SP000722, SP000722, SP000722, SP000472, SP000473, SP000474, SP000475, SP000476, SP000477 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 2 | TB-SO, TB-RO |
| **Total** | **579** | |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 112 | – | No.Reg Lab | – | `` |
| 282 | – | No.Reg Lab | – | `` |
| 458 | – | No.Reg Lab | – | `` |
| 778 | – | No.Reg Lab | – | `` |
| 954 | – | No.Reg Lab | – | `` |
| 1060 | – | No.Reg Lab | – | `` |
| 1191 | – | No.Reg Lab | – | `` |
| 1310 | – | No.Reg Lab | – | `` |
| 1433 | – | No.Reg Lab | – | `` |
| 1435 | – | Metode Uji | – | `` |
| 1668 | – | Tanda Tangan Petugas Pemeriksa | – | `` |
| 1669 | – | Keterangan | – | `` |
