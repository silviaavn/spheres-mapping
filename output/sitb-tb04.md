# Output Form: SITB TB 04 (Fasyankes & Rujukan)

Sumber: `mapping/phdt-data-dictionary-sitb-tb04.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 71 |
| Code (`jumlah code` = 1) | 579 |
| Code unik (code + CodeSystem) | 85 |
| Variabel BQ (unik) | 99 |
| Variabel di Excel export | 114 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 5–30 | Patient | – | – | `no_rekam_medis` → `Patient.identifier.value` (8)<br>`nik_nomor_induk_kependudukan` → `Patient.identifier.value` (11)<br>`nama_lengkap_pasien` → `Patient.name.text` (12)<br>`jenis_kelamin` → `Patient.gender` (13)<br>_Provinsi_ → `Patient.address.extension.extension.valueCode` (19, tanpa BQ)<br>_Kabupaten/Kota_ → `Patient.address.extension.extension.valueCode` (22, tanpa BQ)<br>_Kecamatan_ → `Patient.address.extension.extension.valueCode` (25, tanpa BQ)<br>_Kelurahan_ → `Patient.address.extension.extension.valueCode` (28, tanpa BQ)<br>`alamat_lengkap` → `Patient.address.line` (29) |
| 2 | 33–51 | Organization | – | – | _Nama Fasyankes_ → `Organization.name` (37, tanpa BQ)<br>_Provinsi Fasyankes_ → `Organization.address.extension.extension.valueCode` (42, tanpa BQ)<br>_Kabupaten Fasyankes_ → `Organization.address.extension.extension.valueCode` (45, tanpa BQ) |
| 3 | 53–76 | Location | – | – | – |
| 4 | 79–101 | EpisodeOfCare | TB-SO | Tuberkulosis Sensitif Obat | – |
| 5 | 104–131 | Encounter | – | – | `nama_fasilitas_kesehatan_asal_contoh_uji` → `Encounter.hospitalization.origin.reference` (108) 🔎 lookup master data<br>_Nama Fasyankes_ → `Encounter.serviceProvider.reference` (131, tanpa BQ) |
| 6 | 133–139 | Condition | 171126009 | Tuberculosis screening | – |
| 7 | 142–153 | Observation | 424144002 | Current chronological age | `umur` → `Observation.valueQuantity.value` (145) |
| 8 | 158–186 | ServiceRequest | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | _Pemeriksaan Mikroskopis 1_ → `ServiceRequest.identifier` (158, tanpa BQ)<br>`pemeriksaan_mikroskopis_tgl_contoh_uji_diterima` → `ServiceRequest.occurrenceDateTime` (166)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (167) |
| 9 | 188–207 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (189)<br>`pemeriksaan_mikroskopis_jenis_contoh_uji` → `Specimen.type.coding` (191) |
| 10 | 209–225 | Observation | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | `pemeriksaan_mikroskopis_1_hasil_pemeriksaan` → `Observation.valueCodeableConcept.coding` (213)<br>`pemeriksaan_mikroskopis_1_tgl_hasil_dilaporkan` → `Observation.issued` (223) |
| 11 | 227–239 | DiagnosticReport | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | – |
| 12 | 241–269 | ServiceRequest | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | _Pemeriksaan Mikroskopis 2_ → `ServiceRequest.identifier` (241, tanpa BQ)<br>`pemeriksaan_mikroskopis_tgl_contoh_uji_diterima` → `ServiceRequest.occurrenceDateTime` (249)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (250) |
| 13 | 271–291 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (272)<br>`pemeriksaan_mikroskopis_jenis_contoh_uji` → `Specimen.type.coding` (274) |
| 14 | 293–309 | Observation | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | `pemeriksaan_mikroskopis_2_hasil_pemeriksaan` → `Observation.valueCodeableConcept.coding` (297)<br>`pemeriksaan_mikroskopis_2_tgl_hasil_dilaporkan` → `Observation.issued` (307) |
| 15 | 311–323 | DiagnosticReport | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | – |
| 16 | 328–356 | ServiceRequest | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | _Pemeriksaan Xpert MTB RIF (Xpert) 1_ → `ServiceRequest.identifier` (328, tanpa BQ)<br>`pemeriksaan_xpert_mtb_rif_xpert_tgl_contoh_uji_diterima` → `ServiceRequest.occurrenceDateTime` (336)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (337) |
| 17 | 358–379 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (359)<br>`pemeriksaan_xpert_mtb_rif_xpert_jenis_contoh_uji` → `Specimen.type.coding` (361) |
| 18 | 381–399 | Observation | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | `pemeriksaan_xpert_mtb_rif_xpert_1_hasil_pemeriksaan` → `Observation.valueCodeableConcept.coding` (385)<br>`pemeriksaan_xpert_mtb_rif_xpert_1_tgl_hasil_dilaporkan` → `Observation.issued` (397) |
| 19 | 401–413 | DiagnosticReport | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | – |
| 20 | 415–443 | ServiceRequest | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | _Pemeriksaan Xpert MTB RIF (Xpert) 2_ → `ServiceRequest.identifier` (415, tanpa BQ)<br>`pemeriksaan_xpert_mtb_rif_xpert_tgl_contoh_uji_diterima` → `ServiceRequest.occurrenceDateTime` (423)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (424) |
| 21 | 445–465 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (446)<br>`pemeriksaan_xpert_mtb_rif_xpert_jenis_contoh_uji` → `Specimen.type.coding` (448) |
| 22 | 467–485 | Observation | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | `pemeriksaan_xpert_mtb_rif_xpert_2_hasil_pemeriksaan` → `Observation.valueCodeableConcept.coding` (471)<br>`pemeriksaan_xpert_mtb_rif_xpert_2_tgl_hasil_dilaporkan` → `Observation.issued` (483) |
| 23 | 487–499 | DiagnosticReport | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | – |
| 24 | 504–532 | ServiceRequest | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | _Chip MTB Plus 1_ → `ServiceRequest.identifier` (504, tanpa BQ)<br>`pemeriksaan_xpert_mtb_rif_truenat_tgl_contoh_uji_diterima` → `ServiceRequest.occurrenceDateTime` (512)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (513) |
| 25 | 534–554 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (535)<br>`pemeriksaan_xpert_mtb_rif_truenat_jenis_contoh_uji` → `Specimen.type.coding` (537) |
| 26 | 556–567 | Observation | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | `pemeriksaan_xpert_mtb_rif_truenat_chip_mtb_plus_1_hasil_pemeriksaan` → `Observation.valueString` (560)<br>`pemeriksaan_xpert_mtb_rif_truenat_chip_mtb_plus_1_tgl_hasil_dilaporkan` → `Observation.issued` (565) |
| 27 | 569–581 | DiagnosticReport | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | – |
| 28 | 583–612 | ServiceRequest | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | _Chip MTB Plus 2_ → `ServiceRequest.identifier` (583, tanpa BQ)<br>`pemeriksaan_xpert_mtb_rif_truenat_tgl_contoh_uji_diterima` → `ServiceRequest.occurrenceDateTime` (591)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (592) |
| 29 | 614–634 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (615)<br>`pemeriksaan_xpert_mtb_rif_truenat_jenis_contoh_uji` → `Specimen.type.coding` (617) |
| 30 | 636–647 | Observation | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | `pemeriksaan_xpert_mtb_rif_truenat_chip_mtb_plus_2_hasil_pemeriksaan` → `Observation.valueString` (640)<br>`pemeriksaan_xpert_mtb_rif_truenat_chip_mtb_plus_2_tgl_hasil_dilaporkan` → `Observation.issued` (645) |
| 31 | 649–661 | DiagnosticReport | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | – |
| 32 | 663–692 | ServiceRequest | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | _Chip MTB Rif 1_ → `ServiceRequest.identifier` (663, tanpa BQ)<br>`pemeriksaan_xpert_mtb_rif_truenat_tgl_contoh_uji_diterima` → `ServiceRequest.occurrenceDateTime` (671)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (672) |
| 33 | 694–713 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (695)<br>`pemeriksaan_xpert_mtb_rif_truenat_jenis_contoh_uji` → `Specimen.type.coding` (697) |
| 34 | 715–726 | Observation | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | `pemeriksaan_xpert_mtb_rif_truenat_chip_mtb_rif_1_hasil_pemeriksaan` → `Observation.valueString` (719)<br>`pemeriksaan_xpert_mtb_rif_truenat_chip_mtb_rif_1_tgl_hasil_dilaporkan` → `Observation.issued` (724) |
| 35 | 728–740 | DiagnosticReport | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | – |
| 36 | 742–770 | ServiceRequest | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | _Chip MTB Rif 2_ → `ServiceRequest.identifier` (742, tanpa BQ)<br>`pemeriksaan_xpert_mtb_rif_truenat_tgl_contoh_uji_diterima` → `ServiceRequest.occurrenceDateTime` (750)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (751) |
| 37 | 772–792 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (773)<br>`pemeriksaan_xpert_mtb_rif_truenat_jenis_contoh_uji` → `Specimen.type.coding` (775) |
| 38 | 794–805 | Observation | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | `pemeriksaan_xpert_mtb_rif_truenat_chip_mtb_rif_2_hasil_pemeriksaan` → `Observation.valueString` (798)<br>`pemeriksaan_xpert_mtb_rif_truenat_chip_mtb_rif_2_tgl_hasil_dilaporkan` → `Observation.issued` (803) |
| 39 | 807–819 | DiagnosticReport | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | – |
| 40 | 824–852 | ServiceRequest | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | _Pemeriksaan TCM MTB RIF INH (BD MAX) 1_ → `ServiceRequest.identifier` (824, tanpa BQ)<br>`pemeriksaan_tcm_mtb_rif_inh_bd_max_tgl_contoh_uji_diterima` → `ServiceRequest.occurrenceDateTime` (832)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (833) |
| 41 | 854–874 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (855)<br>`pemeriksaan_tcm_mtb_rif_inh_bd_max_jenis_contoh_uji` → `Specimen.type.coding` (857) |
| 42 | 876–894 | Observation | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | `pemeriksaan_tcm_mtb_rif_inh_bd_max_1_hasil_pemeriksaan` → `Observation.valueCodeableConcept.coding` (880)<br>`pemeriksaan_tcm_mtb_rif_inh_bd_max_1_tgl_hasil_dilaporkan` → `Observation.issued` (892) |
| 43 | 896–908 | DiagnosticReport | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | – |
| 44 | 910–938 | ServiceRequest | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | _Pemeriksaan TCM MTB RIF INH (BD MAX) 2_ → `ServiceRequest.identifier` (910, tanpa BQ)<br>`pemeriksaan_tcm_mtb_rif_inh_bd_max_tgl_contoh_uji_diterima` → `ServiceRequest.occurrenceDateTime` (918)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (919) |
| 45 | 940–960 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (941)<br>`pemeriksaan_tcm_mtb_rif_inh_bd_max_jenis_contoh_uji` → `Specimen.type.coding` (943) |
| 46 | 962–980 | Observation | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | `pemeriksaan_tcm_mtb_rif_inh_bd_max_2_hasil_pemeriksaan` → `Observation.valueCodeableConcept.coding` (966)<br>`pemeriksaan_tcm_mtb_rif_inh_bd_max_2_tgl_hasil_dilaporkan` → `Observation.issued` (978) |
| 47 | 982–994 | DiagnosticReport | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | – |
| 48 | 1000–1028 | ServiceRequest | MK099927 | Pemeriksaan PCR Open System | _Pemeriksaan PCR Open System_ → `ServiceRequest.identifier` (1000, tanpa BQ)<br>`pemeriksaan_pcr_open_system_tgl_contoh_uji_diterima` → `ServiceRequest.occurrenceDateTime` (1008)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (1009) |
| 49 | 1030–1050 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (1031)<br>`pemeriksaan_pcr_open_system_jenis_contoh_uji` → `Specimen.type.coding` (1033) |
| 50 | 1052–1085 | Observation | MK099927 | Pemeriksaan PCR Open System | _MTB_ → `Observation.component.code.coding` (1056, tanpa BQ)<br>`pemeriksaan_pcr_open_system_hasil_pemeriksaan_mtb` → `Observation.component.valueCodeableConcept.coding` (1057)<br>_Rifampisin_ → `Observation.component.code.coding` (1062, tanpa BQ)<br>`pemeriksaan_pcr_open_system_hasil_pemeriksaan_rif` → `Observation.component.valueCodeableConcept.coding` (1063)<br>_Isoniazid_ → `Observation.component.code.coding` (1066, tanpa BQ)<br>`pemeriksaan_pcr_open_system_hasil_pemeriksaan_inh` → `Observation.component.valueCodeableConcept.coding` (1067)<br>_Mutasi Gen katG_ → `Observation.component.code.coding` (1070, tanpa BQ)<br>`pemeriksaan_pcr_open_system_hasil_pemeriksaan_katg` → `Observation.component.valueCodeableConcept.coding` (1071)<br>_Mutasi Gen inhApr_ → `Observation.component.code.coding` (1073, tanpa BQ)<br>`pemeriksaan_pcr_open_system_hasil_pemeriksaan_inhapr` → `Observation.component.valueCodeableConcept.coding` (1074)<br>_NTM_ → `Observation.component.code.coding` (1076, tanpa BQ)<br>`pemeriksaan_pcr_open_system_hasil_pemeriksaan_ntm` → `Observation.component.valueCodeableConcept.coding` (1077)<br>`pemeriksaan_pcr_open_system_tgl_hasil_dilaporkan` → `Observation.issued` (1083) |
| 51 | 1088–1100 | DiagnosticReport | MK099927 | Pemeriksaan PCR Open System | – |
| 52 | 1106–1134 | ServiceRequest | X099379 | Pemeriksaan TCM XDR | _Pemeriksaan Xpert (TCM) XDR_ → `ServiceRequest.identifier` (1106, tanpa BQ)<br>`pemeriksaan_xpert_tcm_xdr_tgl_contoh_uji_diterima` → `ServiceRequest.occurrenceDateTime` (1114)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (1115) |
| 53 | 1136–1157 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (1137)<br>`pemeriksaan_xpert_tcm_xdr_jenis_contoh_uji` → `Specimen.type.coding` (1139) |
| 54 | 1159–1217 | Observation | X099379 | Pemeriksaan TCM XDR | `pemeriksaan_xpert_tcm_xdr_hasil_pemeriksaan_validinvalidno_resulterror` → `Observation.valueCodeableConcept.coding` (1163)<br>_MTB_ → `Observation.component.code.coding` (1168, tanpa BQ)<br>`pemeriksaan_xpert_tcm_xdr_hasil_pemeriksaan_mtb` → `Observation.component.valueCodeableConcept.coding` (1169)<br>_H Dosis Rendah (Low)_ → `Observation.component.code.coding` (1172, tanpa BQ)<br>`pemeriksaan_xpert_tcm_xdr_hasil_pemeriksaan_h_dosis_rendah_low` → `Observation.component.valueCodeableConcept.coding` (1173)<br>_H_ → `Observation.component.code.coding` (1177, tanpa BQ)<br>`pemeriksaan_xpert_tcm_xdr_hasil_pemeriksaan_h` → `Observation.component.valueCodeableConcept.coding` (1178)<br>_Eto_ → `Observation.component.code.coding` (1182, tanpa BQ)<br>`pemeriksaan_xpert_tcm_xdr_hasil_pemeriksaan_eto` → `Observation.component.valueCodeableConcept.coding` (1183)<br>_FQ Dosis Rendah (Low)_ → `Observation.component.code.coding` (1186, tanpa BQ)<br>`pemeriksaan_xpert_tcm_xdr_hasil_pemeriksaan_fq_dosis_rendah_low` → `Observation.component.valueCodeableConcept.coding` (1187)<br>_FQ_ → `Observation.component.code.coding` (1191, tanpa BQ)<br>`pemeriksaan_xpert_tcm_xdr_hasil_pemeriksaan_fq` → `Observation.component.valueCodeableConcept.coding` (1192)<br>_Amk_ → `Observation.component.code.coding` (1196, tanpa BQ)<br>`pemeriksaan_xpert_tcm_xdr_hasil_pemeriksaan_amk` → `Observation.component.valueCodeableConcept.coding` (1197)<br>_Km_ → `Observation.component.code.coding` (1201, tanpa BQ)<br>`pemeriksaan_xpert_tcm_xdr_hasil_pemeriksaan_km` → `Observation.component.valueCodeableConcept.coding` (1202)<br>_Cm_ → `Observation.component.code.coding` (1206, tanpa BQ)<br>`pemeriksaan_xpert_tcm_xdr_hasil_pemeriksaan_cm` → `Observation.component.valueCodeableConcept.coding` (1207)<br>`pemeriksaan_xpert_tcm_xdr_tgl_hasil_dilaporkan` → `Observation.issued` (1215) |
| 55 | 1219–1231 | DiagnosticReport | X099379 | Pemeriksaan TCM XDR | – |
| 56 | 1237–1265 | ServiceRequest | X099380 | Line Probe Assay (LPA) Lini 1 | _Pemeriksaan LPA Lini 1_ → `ServiceRequest.identifier` (1237, tanpa BQ)<br>`pemeriksaan_lpa_lini_satu_tgl_contoh_uji_diterima` → `ServiceRequest.occurrenceDateTime` (1245)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (1246) |
| 57 | 1267–1287 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (1268)<br>`pemeriksaan_lpa_lini_satu_jenis_contoh_uji` → `Specimen.type.coding` (1270) |
| 58 | 1289–1336 | Observation | X099380 | Line Probe Assay (LPA) Lini 1 | _Valid/Invalid_ → `Observation.code.coding` (1292, tanpa BQ)<br>`pemeriksaan_lpa_lini_satu_hasil_pemeriksaan_validinvalid` → `Observation.valueCodeableConcept.coding` (1293)<br>_MTB_ → `Observation.component.code.coding` (1296, tanpa BQ)<br>`pemeriksaan_lpa_lini_satu_hasil_pemeriksaan_mtb` → `Observation.component.valueCodeableConcept.coding` (1297)<br>_R_ → `Observation.component.code.coding` (1300, tanpa BQ)<br>`pemeriksaan_lpa_lini_satu_hasil_pemeriksaan_r` → `Observation.component.valueCodeableConcept.coding` (1301)<br>_Isoniazid Dosis Rendah_ → `Observation.component.code.coding` (1306, tanpa BQ)<br>`pemeriksaan_lpa_lini_satu_hasil_pemeriksaan_h_low_dose` → `Observation.component.valueCodeableConcept.coding` (1307)<br>_Isoniazid Dosis Tinggi_ → `Observation.component.code.coding` (1312, tanpa BQ)<br>`pemeriksaan_lpa_lini_satu_hasil_pemeriksaan_h_high_dose` → `Observation.component.valueCodeableConcept.coding` (1313)<br>_Etionamid_ → `Observation.component.code.coding` (1318, tanpa BQ)<br>`pemeriksaan_lpa_lini_satu_hasil_pemeriksaan_eto` → `Observation.component.valueCodeableConcept.coding` (1319)<br>_Protionamid_ → `Observation.component.code.coding` (1324, tanpa BQ)<br>`pemeriksaan_lpa_lini_satu_hasil_pemeriksaan_pto` → `Observation.component.valueCodeableConcept.coding` (1325)<br>`pemeriksaan_lpa_lini_satu_tgl_hasil_dilaporkan` → `Observation.issued` (1334) |
| 59 | 1338–1350 | DiagnosticReport | X099380 | Line Probe Assay (LPA) Lini 1 | – |
| 60 | 1356–1384 | ServiceRequest | X099381 | Line Probe Assay (LPA) Lini 2 | _Pemeriksaan LPA Lini 2_ → `ServiceRequest.identifier` (1356, tanpa BQ)<br>`pemeriksaan_lpa_line_probe_assay_lini_2_tgl_contoh_uji_diterima` → `ServiceRequest.occurrenceDateTime` (1364)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (1365) |
| 61 | 1386–1405 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (1387)<br>`pemeriksaan_lpa_line_probe_assay_lini_2_jenis_contoh_uji` → `Specimen.type.coding` (1389) |
| 62 | 1407–1460 | Observation | X099381 | Line Probe Assay (LPA) Lini 2 | `pemeriksaan_lpa_line_probe_assay_lini_2_hasil_pemeriksaan_invalid` → `Observation.valueCodeableConcept.coding` (1411)<br>_MTB_ → `Observation.component.code.coding` (1414, tanpa BQ)<br>`pemeriksaan_lpa_line_probe_assay_lini_2_hasil_pemeriksaan_mtb` → `Observation.component.valueCodeableConcept.coding` (1415)<br>_Levofloksasin_ → `Observation.component.code.coding` (1418, tanpa BQ)<br>`pemeriksaan_lpa_line_probe_assay_lini_2_hasil_pemeriksaan_fq_lfx` → `Observation.component.valueCodeableConcept.coding` (1419)<br>_Moksifloksasin_ → `Observation.component.code.coding` (1424, tanpa BQ)<br>`pemeriksaan_lpa_line_probe_assay_lini_2_hasil_pemeriksaan_fq_mfx` → `Observation.component.valueCodeableConcept.coding` (1425)<br>_Moksifloksasin Dosis Tinggi_ → `Observation.component.code.coding` (1430, tanpa BQ)<br>`pemeriksaan_lpa_line_probe_assay_lini_2_hasil_pemeriksaan_fq_mfx_dosis_tinggi` → `Observation.component.valueCodeableConcept.coding` (1431)<br>_Kanamisin_ → `Observation.component.code.coding` (1436, tanpa BQ)<br>`pemeriksaan_lpa_line_probe_assay_lini_2_hasil_pemeriksaan_slid_km` → `Observation.component.valueCodeableConcept.coding` (1437)<br>_Amikasin_ → `Observation.component.code.coding` (1442, tanpa BQ)<br>`pemeriksaan_lpa_line_probe_assay_lini_2_hasil_pemeriksaan_slid_amk` → `Observation.component.valueCodeableConcept.coding` (1443)<br>_Kapreomisin_ → `Observation.component.code.coding` (1448, tanpa BQ)<br>`pemeriksaan_lpa_line_probe_assay_lini_2_hasil_pemeriksaan_slid_cm` → `Observation.component.valueCodeableConcept.coding` (1449)<br>`pemeriksaan_lpa_line_probe_assay_lini_2_tgl_hasil_dilaporkan` → `Observation.issued` (1458) |
| 63 | 1462–1474 | DiagnosticReport | X099381 | Line Probe Assay (LPA) Lini 2 | – |
| 64 | 1481–1510 | ServiceRequest | X099389 | Hasil Pemeriksaan Biakan TB (Metode: LJ) | _Pemeriksaan Biakan_ → `ServiceRequest.identifier` (1481, tanpa BQ)<br>`pemeriksaan_biakan_tgl_contoh_uji_diterima_untuk_pemeriksaan_biakan_dan_uji_kepekaan` → `ServiceRequest.occurrenceDateTime` (1490)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (1491) |
| 65 | 1512–1531 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (1513)<br>`pemeriksaan_biakan_jenis_contoh_uji` → `Specimen.type.coding` (1515) |
| 66 | 1533–1554 | Observation | X099389 | Hasil Pemeriksaan Biakan TB (Metode: LJ) | `pemeriksaan_biakan_metode_uji` → `Observation.method.coding` (1534)<br>`pemeriksaan_biakan_hasil_pemeriksaan` → `Observation.valueCodeableConcept.coding` (1540)<br>`pemeriksaan_biakan_tgl_hasil_dilaporkan` → `Observation.issued` (1552) |
| 67 | 1556–1569 | DiagnosticReport | X099389 | Hasil Pemeriksaan Biakan TB (Metode: LJ) | – |
| 68 | 1572–1600 | ServiceRequest | X099383 | Pemeriksaan Paket Standar Kepekaan | _Pemeriksaan Paket Standar Uji Kepekaan_ → `ServiceRequest.identifier` (1572, tanpa BQ)<br>`pemeriksaan_paket_standar_uji_kepekaan_tgl_hasil_dilaporkan` → `ServiceRequest.occurrenceDateTime` (1580)<br>`alasan_pemeriksaan` → `ServiceRequest.reasonCode.coding` (1581) |
| 69 | 1602–1621 | Specimen | 418564007 | Pleural fluid specimen | `no_identitas_sediaan` → `Specimen.identifier` (1603)<br>_Jenis Contoh Uji_ → `Specimen.type.coding` (1605, tanpa BQ) |
| 70 | 1623–1695 | Observation | X099383 | Pemeriksaan Paket Standar Kepekaan | _Isoniazid_ → `Observation.component.code.coding` (1628, tanpa BQ)<br>`pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_h` → `Observation.component.valueCodeableConcept.coding` (1629)<br>_Isoniazid Dosis Tinggi_ → `Observation.component.code.coding` (1634, tanpa BQ)<br>`pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_h_dosis_tinggi` → `Observation.component.valueCodeableConcept.coding` (1635)<br>_Levofloksasin_ → `Observation.component.code.coding` (1640, tanpa BQ)<br>`pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_lfx` → `Observation.component.valueCodeableConcept.coding` (1641)<br>_Moksifloksasin_ → `Observation.component.code.coding` (1646, tanpa BQ)<br>`pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_mfx` → `Observation.component.valueCodeableConcept.coding` (1647)<br>_Moksifloksasin Dosis Tinggi_ → `Observation.component.code.coding` (1652, tanpa BQ)<br>`pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_mfx_dosis_tinggi` → `Observation.component.valueCodeableConcept.coding` (1653)<br>_Kanamisin_ → `Observation.component.code.coding` (1658, tanpa BQ)<br>`pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_km` → `Observation.component.valueCodeableConcept.coding` (1659)<br>_Amikasin_ → `Observation.component.code.coding` (1664, tanpa BQ)<br>_Hasil Pemeriksaan Amk_ → `Observation.component.valueCodeableConcept.coding` (1665, tanpa BQ)<br>_Kapreomisin_ → `Observation.component.code.coding` (1670, tanpa BQ)<br>`pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_cm` → `Observation.component.valueCodeableConcept.coding` (1671)<br>`pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan` → `Observation.component.code.coding` (1676)<br>`pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_1` → `Observation.component.code.coding` (1678)<br>`pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_2` → `Observation.component.code.coding` (1680)<br>`pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_3` → `Observation.component.code.coding` (1682)<br>`pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_4` → `Observation.component.code.coding` (1684)<br>`pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_5` → `Observation.component.code.coding` (1686) |
| 71 | 1697–1709 | DiagnosticReport | X099383 | Pemeriksaan Paket Standar Kepekaan | – |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 17 |
| ServiceRequest | 16 |
| Specimen | 16 |
| DiagnosticReport | 16 |
| Patient | 1 |
| Organization | 1 |
| Location | 1 |
| EpisodeOfCare | 1 |
| Encounter | 1 |
| Condition | 1 |
| **Total** | **71** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 84 | EpisodeOfCare | `EpisodeOfCare.type.coding` | TB-SO | Tuberkulosis Sensitif Obat | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 2 | 85 | EpisodeOfCare | `EpisodeOfCare.type.coding` | TB-RO | Tuberkulosis Resisten Obat | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 3 | 106 | Encounter | `Encounter.hospitalization.admitSource.coding` | EHA000002 | Datang sendiri | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 4 | 107 | Encounter | `Encounter.hospitalization.admitSource.coding` | 257622000 | Healthcare facility | http://snomed.info/sct |
| 5 | 135 | Condition | `Condition.code.coding` | 171126009 | Tuberculosis screening | http://snomed.info/sct |
| 6 | 144 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 7 | 163 | ServiceRequest | `ServiceRequest.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 8 | 167 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 9 | 168 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 10 | 170 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 11 | 172 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 12 | 174 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 13 | 176 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 14 | 178 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 15 | 180 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 16 | 182 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 17 | 184 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 18 | 191 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 19 | 192 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 20 | 193 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 21 | 194 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 22 | 195 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 23 | 196 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 24 | 197 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 25 | 198 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 26 | 199 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 27 | 200 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 28 | 201 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 29 | 212 | Observation | `Observation.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 30 | 213 | Observation | `Observation.valueCodeableConcept.coding` | 260385009 | Negative | http://snomed.info/sct |
| 31 | 214 | Observation | `Observation.valueCodeableConcept.coding` | LA11841-6 | 1+ | http://loinc.org |
| 32 | 215 | Observation | `Observation.valueCodeableConcept.coding` | LA11842-4 | 2+ | http://loinc.org |
| 33 | 216 | Observation | `Observation.valueCodeableConcept.coding` | LA11843-2 | 3+ | http://loinc.org |
| 34 | 230 | DiagnosticReport | `DiagnosticReport.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 35 | 246 | ServiceRequest | `ServiceRequest.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 36 | 250 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 37 | 251 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 38 | 253 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 39 | 255 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 40 | 257 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 41 | 259 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 42 | 261 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 43 | 263 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 44 | 265 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 45 | 267 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 46 | 274 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 47 | 275 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 48 | 276 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 49 | 277 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 50 | 278 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 51 | 279 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 52 | 280 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 53 | 281 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 54 | 282 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 55 | 283 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 56 | 284 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 57 | 296 | Observation | `Observation.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 58 | 297 | Observation | `Observation.valueCodeableConcept.coding` | 260385009 | Negative | http://snomed.info/sct |
| 59 | 298 | Observation | `Observation.valueCodeableConcept.coding` | LA11841-6 | 1+ | http://loinc.org |
| 60 | 299 | Observation | `Observation.valueCodeableConcept.coding` | LA11842-4 | 2+ | http://loinc.org |
| 61 | 300 | Observation | `Observation.valueCodeableConcept.coding` | LA11843-2 | 3+ | http://loinc.org |
| 62 | 314 | DiagnosticReport | `DiagnosticReport.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 63 | 333 | ServiceRequest | `ServiceRequest.code.coding` | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | http://terminology.kemkes.go.id/sp |
| 64 | 337 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 65 | 338 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 66 | 340 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 67 | 342 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 68 | 344 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 69 | 346 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 70 | 348 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 71 | 350 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 72 | 352 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 73 | 354 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 74 | 361 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 75 | 362 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 76 | 363 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 77 | 364 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 78 | 365 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 79 | 366 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 80 | 367 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 81 | 368 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 82 | 369 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 83 | 370 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 84 | 371 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 85 | 384 | Observation | `Observation.code.coding` | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | http://terminology.kemkes.go.id/sp |
| 86 | 385 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 87 | 386 | Observation | `Observation.valueCodeableConcept.coding` | X099770 | Rifampisin sensitive | http://terminology.kemkes.go.id/CodeSystem/examination |
| 88 | 387 | Observation | `Observation.valueCodeableConcept.coding` | X099771 | Rifampisin resistan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 89 | 388 | Observation | `Observation.valueCodeableConcept.coding` | X099772 | Rifampisin indeterminate | http://terminology.kemkes.go.id/CodeSystem/examination |
| 90 | 404 | DiagnosticReport | `DiagnosticReport.code.coding` | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | http://terminology.kemkes.go.id/sp |
| 91 | 420 | ServiceRequest | `ServiceRequest.code.coding` | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | http://terminology.kemkes.go.id/sp |
| 92 | 424 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 93 | 425 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 94 | 427 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 95 | 429 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 96 | 431 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 97 | 433 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 98 | 435 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 99 | 437 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 100 | 439 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 101 | 441 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 102 | 448 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 103 | 449 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 104 | 450 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 105 | 451 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 106 | 452 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 107 | 453 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 108 | 454 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 109 | 455 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 110 | 456 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 111 | 457 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 112 | 458 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 113 | 470 | Observation | `Observation.code.coding` | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | http://terminology.kemkes.go.id/sp |
| 114 | 471 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 115 | 472 | Observation | `Observation.valueCodeableConcept.coding` | X099770 | Rifampisin sensitive | http://terminology.kemkes.go.id/CodeSystem/examination |
| 116 | 473 | Observation | `Observation.valueCodeableConcept.coding` | X099771 | Rifampisin resistan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 117 | 474 | Observation | `Observation.valueCodeableConcept.coding` | X099772 | Rifampisin indeterminate | http://terminology.kemkes.go.id/CodeSystem/examination |
| 118 | 490 | DiagnosticReport | `DiagnosticReport.code.coding` | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | http://terminology.kemkes.go.id/sp |
| 119 | 509 | ServiceRequest | `ServiceRequest.code.coding` | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | http://terminology.kemkes.go.id/sp |
| 120 | 513 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 121 | 514 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 122 | 516 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 123 | 518 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 124 | 520 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 125 | 522 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 126 | 524 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 127 | 526 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 128 | 528 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 129 | 530 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 130 | 537 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 131 | 538 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 132 | 539 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 133 | 540 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 134 | 541 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 135 | 542 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 136 | 543 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 137 | 544 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 138 | 545 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 139 | 546 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 140 | 547 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 141 | 559 | Observation | `Observation.code.coding` | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | http://terminology.kemkes.go.id/sp |
| 142 | 572 | DiagnosticReport | `DiagnosticReport.code.coding` | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | http://terminology.kemkes.go.id/sp |
| 143 | 588 | ServiceRequest | `ServiceRequest.code.coding` | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | http://terminology.kemkes.go.id/sp |
| 144 | 592 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 145 | 593 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 146 | 595 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 147 | 597 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 148 | 599 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 149 | 601 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 150 | 603 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 151 | 605 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 152 | 607 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 153 | 609 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 154 | 617 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 155 | 618 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 156 | 619 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 157 | 620 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 158 | 621 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 159 | 622 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 160 | 623 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 161 | 624 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 162 | 625 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 163 | 626 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 164 | 627 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 165 | 639 | Observation | `Observation.code.coding` | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | http://terminology.kemkes.go.id/sp |
| 166 | 652 | DiagnosticReport | `DiagnosticReport.code.coding` | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | http://terminology.kemkes.go.id/sp |
| 167 | 668 | ServiceRequest | `ServiceRequest.code.coding` | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | http://terminology.kemkes.go.id/sp |
| 168 | 672 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 169 | 673 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 170 | 675 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 171 | 677 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 172 | 679 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 173 | 681 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 174 | 683 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 175 | 685 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 176 | 687 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 177 | 689 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 178 | 697 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 179 | 698 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 180 | 699 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 181 | 700 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 182 | 701 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 183 | 702 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 184 | 703 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 185 | 704 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 186 | 705 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 187 | 706 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 188 | 707 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 189 | 718 | Observation | `Observation.code.coding` | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | http://terminology.kemkes.go.id/sp |
| 190 | 731 | DiagnosticReport | `DiagnosticReport.code.coding` | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | http://terminology.kemkes.go.id/sp |
| 191 | 747 | ServiceRequest | `ServiceRequest.code.coding` | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | http://terminology.kemkes.go.id/sp |
| 192 | 751 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 193 | 752 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 194 | 754 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 195 | 756 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 196 | 758 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 197 | 760 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 198 | 762 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 199 | 764 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 200 | 766 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 201 | 768 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 202 | 775 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 203 | 776 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 204 | 777 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 205 | 778 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 206 | 779 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 207 | 780 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 208 | 781 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 209 | 782 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 210 | 783 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 211 | 784 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 212 | 785 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 213 | 797 | Observation | `Observation.code.coding` | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | http://terminology.kemkes.go.id/sp |
| 214 | 810 | DiagnosticReport | `DiagnosticReport.code.coding` | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | http://terminology.kemkes.go.id/sp |
| 215 | 829 | ServiceRequest | `ServiceRequest.code.coding` | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 216 | 833 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 217 | 834 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 218 | 836 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 219 | 838 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 220 | 840 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 221 | 842 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 222 | 844 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 223 | 846 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 224 | 848 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 225 | 850 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 226 | 857 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 227 | 858 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 228 | 859 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 229 | 860 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 230 | 861 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 231 | 862 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 232 | 863 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 233 | 864 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 234 | 865 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 235 | 866 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 236 | 867 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 237 | 879 | Observation | `Observation.code.coding` | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 238 | 880 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 239 | 881 | Observation | `Observation.valueCodeableConcept.coding` | X099770 | Rifampisin sensitive | http://terminology.kemkes.go.id/CodeSystem/examination |
| 240 | 882 | Observation | `Observation.valueCodeableConcept.coding` | X099771 | Rifampisin resistan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 241 | 883 | Observation | `Observation.valueCodeableConcept.coding` | X099772 | Rifampisin indeterminate | http://terminology.kemkes.go.id/CodeSystem/examination |
| 242 | 899 | DiagnosticReport | `DiagnosticReport.code.coding` | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 243 | 915 | ServiceRequest | `ServiceRequest.code.coding` | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 244 | 919 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 245 | 920 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 246 | 922 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 247 | 924 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 248 | 926 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 249 | 928 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 250 | 930 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 251 | 932 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 252 | 934 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 253 | 936 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 254 | 943 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 255 | 944 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 256 | 945 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 257 | 946 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 258 | 947 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 259 | 948 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 260 | 949 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 261 | 950 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 262 | 951 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 263 | 952 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 264 | 953 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 265 | 965 | Observation | `Observation.code.coding` | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 266 | 966 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 267 | 967 | Observation | `Observation.valueCodeableConcept.coding` | X099770 | Rifampisin sensitive | http://terminology.kemkes.go.id/CodeSystem/examination |
| 268 | 968 | Observation | `Observation.valueCodeableConcept.coding` | X099771 | Rifampisin resistan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 269 | 969 | Observation | `Observation.valueCodeableConcept.coding` | X099772 | Rifampisin indeterminate | http://terminology.kemkes.go.id/CodeSystem/examination |
| 270 | 985 | DiagnosticReport | `DiagnosticReport.code.coding` | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 271 | 1005 | ServiceRequest | `ServiceRequest.code.coding` | MK099927 | Pemeriksaan PCR Open System | http://terminology.kemkes.go.id/CodeSystem/examination |
| 272 | 1009 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 273 | 1010 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 274 | 1012 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 275 | 1014 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 276 | 1016 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 277 | 1018 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 278 | 1020 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 279 | 1022 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 280 | 1024 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 281 | 1026 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 282 | 1033 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 283 | 1034 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 284 | 1035 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 285 | 1036 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 286 | 1037 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 287 | 1038 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 288 | 1039 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 289 | 1040 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 290 | 1041 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 291 | 1042 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 292 | 1043 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 293 | 1055 | Observation | `Observation.code.coding` | MK099927 | Pemeriksaan PCR Open System | http://terminology.kemkes.go.id/CodeSystem/examination |
| 294 | 1056 | Observation | `Observation.component.code.coding` | 13956-8 | Mycobacterium tuberculosis DNA [Presence] in Specimen by NAA with probe detection | http://loinc.org |
| 295 | 1057 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 296 | 1058 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 297 | 1062 | Observation | `Observation.component.code.coding` | 89489-9 | rifAMPin [Susceptibility] by Genotype method | http://loinc.org |
| 298 | 1063 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 299 | 1064 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 300 | 1066 | Observation | `Observation.component.code.coding` | 89488-1 | Isoniazid [Susceptibility] by Genotype method | http://loinc.org |
| 301 | 1067 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 302 | 1068 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 303 | 1070 | Observation | `Observation.component.code.coding` | 46246-5 | Mycobacterium tuberculosis katG gene isoniazid high level resistance mutation [Identifier] by Molecular method | http://loinc.org |
| 304 | 1071 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 305 | 1072 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 306 | 1073 | Observation | `Observation.component.code.coding` | 63072-3 | Mycobacterium tuberculosis inhA gene isoniazid low level resistance mutation [Presence] by Molecular method | http://loinc.org |
| 307 | 1074 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 308 | 1075 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 309 | 1076 | Observation | `Observation.component.code.coding` | 110379001 | Mycobacterium, non-tuberculosis (organism) | http://snomed.info/sct |
| 310 | 1077 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 311 | 1078 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 312 | 1091 | DiagnosticReport | `DiagnosticReport.code.coding` | MK099927 | Pemeriksaan PCR Open System | http://terminology.kemkes.go.id/CodeSystem/examination |
| 313 | 1111 | ServiceRequest | `ServiceRequest.code.coding` | X099379 | Pemeriksaan TCM XDR | http://terminology.kemkes.go.id/CodeSystem/examination |
| 314 | 1115 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 315 | 1116 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 316 | 1118 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 317 | 1120 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 318 | 1122 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 319 | 1124 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 320 | 1126 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 321 | 1128 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 322 | 1130 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 323 | 1132 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 324 | 1139 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 325 | 1140 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 326 | 1141 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 327 | 1142 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 328 | 1143 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 329 | 1144 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 330 | 1145 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 331 | 1146 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 332 | 1147 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 333 | 1148 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 334 | 1149 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 335 | 1162 | Observation | `Observation.code.coding` | X099379 | Pemeriksaan TCM XDR | http://terminology.kemkes.go.id/CodeSystem/examination |
| 336 | 1163 | Observation | `Observation.valueCodeableConcept.coding` | X099781 | Hasil Valid | http://terminology.kemkes.go.id/CodeSystem/examination |
| 337 | 1168 | Observation | `Observation.component.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 338 | 1169 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 339 | 1170 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 340 | 1172 | Observation | `Observation.component.code.coding` | X099391 | H Dosis Rendah (Low) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 341 | 1173 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 342 | 1174 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 343 | 1175 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 344 | 1177 | Observation | `Observation.component.code.coding` | 89488-1 | Isoniazid [Susceptibility] by Genotype method | http://loinc.org |
| 345 | 1178 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 346 | 1179 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 347 | 1180 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 348 | 1182 | Observation | `Observation.component.code.coding` | 96110-2 | Ethionamide [Susceptibility] by Genotype method | http://loinc.org |
| 349 | 1183 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 350 | 1184 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 351 | 1186 | Observation | `Observation.component.code.coding` | X099392 | FQ Dosis Rendah (Low) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 352 | 1187 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 353 | 1188 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 354 | 1189 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 355 | 1191 | Observation | `Observation.component.code.coding` | 89487-3 | Fluoroquinolone [Susceptibility] by Genotype method | http://loinc.org |
| 356 | 1192 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 357 | 1193 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 358 | 1194 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 359 | 1196 | Observation | `Observation.component.code.coding` | 89484-0 | Amikacin [Susceptibility] by Genotype method | http://loinc.org |
| 360 | 1197 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 361 | 1198 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 362 | 1199 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 363 | 1201 | Observation | `Observation.component.code.coding` | 89482-4 | Kanamycin [Susceptibility] by Genotype method | http://loinc.org |
| 364 | 1202 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 365 | 1203 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 366 | 1204 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 367 | 1206 | Observation | `Observation.component.code.coding` | 89483-2 | Capreomycin [Susceptibility] by Genotype method | http://loinc.org |
| 368 | 1207 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 369 | 1208 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 370 | 1209 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 371 | 1222 | DiagnosticReport | `DiagnosticReport.code.coding` | X099379 | Pemeriksaan TCM XDR | http://terminology.kemkes.go.id/CodeSystem/examination |
| 372 | 1242 | ServiceRequest | `ServiceRequest.code.coding` | X099380 | Line Probe Assay (LPA) Lini 1 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 373 | 1246 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 374 | 1247 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 375 | 1249 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 376 | 1251 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 377 | 1253 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 378 | 1255 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 379 | 1257 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 380 | 1259 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 381 | 1261 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 382 | 1263 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 383 | 1270 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 384 | 1271 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 385 | 1272 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 386 | 1273 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 387 | 1274 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 388 | 1275 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 389 | 1276 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 390 | 1277 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 391 | 1278 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 392 | 1279 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 393 | 1280 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 394 | 1292 | Observation | `Observation.code.coding` | X099380 | Line Probe Assay (LPA) Lini 1 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 395 | 1293 | Observation | `Observation.valueCodeableConcept.coding` | X099781 | Hasil Valid | http://terminology.kemkes.go.id/CodeSystem/examination |
| 396 | 1296 | Observation | `Observation.component.code.coding` | 13956-8 | Mycobacterium tuberculosis DNA [Presence] in Specimen by NAA with probe detection | http://loinc.org |
| 397 | 1297 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 398 | 1298 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 399 | 1300 | Observation | `Observation.component.code.coding` | 89489-9 | rifAMPin [Susceptibility] by Genotype method | http://loinc.org |
| 400 | 1301 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 401 | 1302 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 402 | 1303 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 403 | 1304 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 404 | 1306 | Observation | `Observation.component.code.coding` | X099391 | H Dosis Rendah (Low) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 405 | 1307 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 406 | 1308 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 407 | 1309 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 408 | 1310 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 409 | 1312 | Observation | `Observation.component.code.coding` | X099783 | H Dosis Tinggi (High) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 410 | 1313 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 411 | 1314 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 412 | 1315 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 413 | 1316 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 414 | 1318 | Observation | `Observation.component.code.coding` | 96110-2 | Ethionamide [Susceptibility] by Genotype method | http://loinc.org |
| 415 | 1319 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 416 | 1320 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 417 | 1321 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 418 | 1322 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 419 | 1324 | Observation | `Observation.component.code.coding` | 103960-1 | Prothionamide [Susceptibility] by Genotype method | http://loinc.org |
| 420 | 1325 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 421 | 1326 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 422 | 1327 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 423 | 1328 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 424 | 1341 | DiagnosticReport | `DiagnosticReport.code.coding` | X099380 | Line Probe Assay (LPA) Lini 1 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 425 | 1361 | ServiceRequest | `ServiceRequest.code.coding` | X099381 | Line Probe Assay (LPA) Lini 2 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 426 | 1365 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 427 | 1366 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 428 | 1368 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 429 | 1370 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 430 | 1372 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 431 | 1374 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 432 | 1376 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 433 | 1378 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 434 | 1380 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 435 | 1382 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 436 | 1389 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 437 | 1390 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 438 | 1391 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 439 | 1392 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 440 | 1393 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 441 | 1394 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 442 | 1395 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 443 | 1396 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 444 | 1397 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 445 | 1398 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 446 | 1399 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 447 | 1410 | Observation | `Observation.code.coding` | X099381 | Line Probe Assay (LPA) Lini 2 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 448 | 1411 | Observation | `Observation.valueCodeableConcept.coding` | X099781 | Hasil Valid | http://terminology.kemkes.go.id/CodeSystem/examination |
| 449 | 1414 | Observation | `Observation.component.code.coding` | 13956-8 | Mycobacterium tuberculosis DNA [Presence] in Specimen by NAA with probe detection | http://loinc.org |
| 450 | 1415 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 451 | 1416 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 452 | 1418 | Observation | `Observation.component.code.coding` | 20629-2 | levoFLOXacin [Susceptibility] | http://loinc.org |
| 453 | 1419 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 454 | 1420 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 455 | 1421 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 456 | 1422 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 457 | 1424 | Observation | `Observation.component.code.coding` | 96112-8 | Moxifloxacin [Susceptibility] by Genotype method | http://loinc.org |
| 458 | 1425 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 459 | 1426 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 460 | 1427 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 461 | 1428 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 462 | 1430 | Observation | `Observation.component.code.coding` | X099775 | Moxifloxacin DT (Mfx DT) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 463 | 1431 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 464 | 1432 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 465 | 1433 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 466 | 1434 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 467 | 1436 | Observation | `Observation.component.code.coding` | 89482-4 | Kanamycin [Susceptibility] by Genotype method | http://loinc.org |
| 468 | 1437 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 469 | 1438 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 470 | 1439 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 471 | 1440 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 472 | 1442 | Observation | `Observation.component.code.coding` | 89484-0 | Amikacin [Susceptibility] by Genotype method | http://loinc.org |
| 473 | 1443 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 474 | 1444 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 475 | 1445 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 476 | 1446 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 477 | 1448 | Observation | `Observation.component.code.coding` | 89483-2 | Capreomycin [Susceptibility] by Genotype method | http://loinc.org |
| 478 | 1449 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 479 | 1450 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 480 | 1451 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 481 | 1452 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 482 | 1465 | DiagnosticReport | `DiagnosticReport.code.coding` | X099381 | Line Probe Assay (LPA) Lini 2 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 483 | 1486 | ServiceRequest | `ServiceRequest.code.coding` | X099389 | Hasil Pemeriksaan Biakan TB (Metode: LJ) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 484 | 1487 | ServiceRequest | `ServiceRequest.code.coding` | X099390 | Hasil Pemeriksaan Biakan TB (Metode: MGIT) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 485 | 1491 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 486 | 1492 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 487 | 1494 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 488 | 1496 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 489 | 1498 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 490 | 1500 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 491 | 1502 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 492 | 1504 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 493 | 1506 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 494 | 1508 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 495 | 1515 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 496 | 1516 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 497 | 1517 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 498 | 1518 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 499 | 1519 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 500 | 1520 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 501 | 1521 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 502 | 1522 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 503 | 1523 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 504 | 1524 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 505 | 1525 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 506 | 1534 | Observation | `Observation.method.coding` | OM000001 | LJ | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 507 | 1535 | Observation | `Observation.method.coding` | OM000002 | MGIT | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 508 | 1538 | Observation | `Observation.code.coding` | X099389 | Hasil Pemeriksaan Biakan TB (Metode: LJ) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 509 | 1539 | Observation | `Observation.code.coding` | X099390 | Hasil Pemeriksaan Biakan TB (Metode: MGIT) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 510 | 1540 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 511 | 1541 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 512 | 1542 | Observation | `Observation.valueCodeableConcept.coding` | LA11841-6 | + | http://loinc.org |
| 513 | 1543 | Observation | `Observation.valueCodeableConcept.coding` | LA11842-4 | ++ | http://loinc.org |
| 514 | 1544 | Observation | `Observation.valueCodeableConcept.coding` | LA11843-2 | +++ | http://loinc.org |
| 515 | 1545 | Observation | `Observation.valueCodeableConcept.coding` | 110379001 | Mycobacterium, non-tuberculosis (organism) | http://snomed.info/sct |
| 516 | 1559 | DiagnosticReport | `DiagnosticReport.code.coding` | X099389 | Hasil Pemeriksaan Biakan TB (Metode: LJ) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 517 | 1560 | DiagnosticReport | `DiagnosticReport.code.coding` | X099390 | Hasil Pemeriksaan Biakan TB (Metode: MGIT) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 518 | 1577 | ServiceRequest | `ServiceRequest.code.coding` | X099383 | Pemeriksaan Paket Standar Kepekaan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 519 | 1581 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 520 | 1582 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 521 | 1584 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 522 | 1586 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 523 | 1588 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 524 | 1590 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 525 | 1592 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 526 | 1594 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 527 | 1596 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 528 | 1598 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 529 | 1605 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 530 | 1606 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 531 | 1607 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 532 | 1608 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 533 | 1609 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 534 | 1610 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 535 | 1611 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 536 | 1612 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 537 | 1613 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 538 | 1614 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 539 | 1615 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 540 | 1626 | Observation | `Observation.code.coding` | X099383 | Pemeriksaan Paket Standar Kepekaan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 541 | 1628 | Observation | `Observation.component.code.coding` | 20383-6 | Isoniazid [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 542 | 1629 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 543 | 1630 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 544 | 1631 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 545 | 1634 | Observation | `Observation.component.code.coding` | X099776 | H High Dosage [Susceptibility] by Method for Slow-growing mycobacteria | http://terminology.kemkes.go.id/CodeSystem/examination |
| 546 | 1635 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 547 | 1636 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 548 | 1637 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 549 | 1640 | Observation | `Observation.component.code.coding` | 53716-7 | levoFLOXacin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 550 | 1641 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 551 | 1642 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 552 | 1643 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 553 | 1646 | Observation | `Observation.component.code.coding` | 41502-6 | Moxifloxacin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 554 | 1647 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 555 | 1648 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 556 | 1649 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 557 | 1652 | Observation | `Observation.component.code.coding` | X099778 | Moxifloxacin High Dosage [Susceptibility] by Method for Slow-growing mycobacteria | http://terminology.kemkes.go.id/CodeSystem/examination |
| 558 | 1653 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 559 | 1654 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 560 | 1655 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 561 | 1658 | Observation | `Observation.component.code.coding` | 23609-1 | Kanamycin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 562 | 1659 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 563 | 1660 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 564 | 1661 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 565 | 1664 | Observation | `Observation.component.code.coding` | 20373-7 | Amikacin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 566 | 1665 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 567 | 1666 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 568 | 1667 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 569 | 1670 | Observation | `Observation.component.code.coding` | 23607-5 | Capreomycin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 570 | 1671 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 571 | 1672 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 572 | 1673 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 573 | 1676 | Observation | `Observation.component.code.coding` | SP000472 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya | http://terminology.kemkes.go.id/sp |
| 574 | 1678 | Observation | `Observation.component.code.coding` | SP000473 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 1 | http://terminology.kemkes.go.id/sp |
| 575 | 1680 | Observation | `Observation.component.code.coding` | SP000474 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 2 | http://terminology.kemkes.go.id/sp |
| 576 | 1682 | Observation | `Observation.component.code.coding` | SP000475 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 3 | http://terminology.kemkes.go.id/sp |
| 577 | 1684 | Observation | `Observation.component.code.coding` | SP000476 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 4 | http://terminology.kemkes.go.id/sp |
| 578 | 1686 | Observation | `Observation.component.code.coding` | SP000477 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 5 | http://terminology.kemkes.go.id/sp |
| 579 | 1700 | DiagnosticReport | `DiagnosticReport.code.coding` | X099383 | Pemeriksaan Paket Standar Kepekaan | http://terminology.kemkes.go.id/CodeSystem/examination |

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
| 156 | – | No.Reg Lab | – | `` |
| 326 | – | No.Reg Lab | – | `` |
| 502 | – | No.Reg Lab | – | `` |
| 822 | – | No.Reg Lab | – | `` |
| 998 | – | No.Reg Lab | – | `` |
| 1104 | – | No.Reg Lab | – | `` |
| 1235 | – | No.Reg Lab | – | `` |
| 1354 | – | No.Reg Lab | – | `` |
| 1477 | – | No.Reg Lab | – | `` |
| 1479 | – | Metode Uji | – | `` |
| 1712 | – | Tanda Tangan Petugas Pemeriksa | – | `` |
| 1713 | – | Keterangan | – | `` |
