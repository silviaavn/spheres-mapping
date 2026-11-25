# Output Form: SITB TB 04 (Fasyankes & Rujukan)

Sumber: `mapping/phdt-data-dictionary-sitb-tb04.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-sitb-tb04.csv) · [struktur file mentah](../raw/sitb-tb04-kolom.md)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 69 |
| Code (`jumlah code` = 1) | 616 |
| Code unik (code + CodeSystem) | 92 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 24 |
| Variabel BQ (unik) | 99 |
| Variabel raw (kolom Excel export) | 114 |

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
| 34 | 172 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 35 | 184 | DiagnosticReport | `DiagnosticReport.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 36 | 200 | ServiceRequest | `ServiceRequest.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 37 | 204 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 38 | 205 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 39 | 207 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 40 | 209 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 41 | 211 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 42 | 213 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 43 | 215 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 44 | 217 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 45 | 219 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 46 | 221 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 47 | 228 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 48 | 229 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 49 | 230 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 50 | 231 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 51 | 232 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 52 | 233 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 53 | 234 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 54 | 235 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 55 | 236 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 56 | 237 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 57 | 238 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 58 | 250 | Observation | `Observation.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 59 | 251 | Observation | `Observation.valueCodeableConcept.coding` | 260385009 | Negative | http://snomed.info/sct |
| 60 | 252 | Observation | `Observation.valueCodeableConcept.coding` | LA11841-6 | 1+ | http://loinc.org |
| 61 | 253 | Observation | `Observation.valueCodeableConcept.coding` | LA11842-4 | 2+ | http://loinc.org |
| 62 | 254 | Observation | `Observation.valueCodeableConcept.coding` | LA11843-2 | 3+ | http://loinc.org |
| 63 | 256 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 64 | 268 | DiagnosticReport | `DiagnosticReport.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 65 | 287 | ServiceRequest | `ServiceRequest.code.coding` | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | http://terminology.kemkes.go.id/sp |
| 66 | 291 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 67 | 292 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 68 | 294 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 69 | 296 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 70 | 298 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 71 | 300 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 72 | 302 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 73 | 304 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 74 | 306 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 75 | 308 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 76 | 315 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 77 | 316 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 78 | 317 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 79 | 318 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 80 | 319 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 81 | 320 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 82 | 321 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 83 | 322 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 84 | 323 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 85 | 324 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 86 | 325 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 87 | 338 | Observation | `Observation.code.coding` | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | http://terminology.kemkes.go.id/sp |
| 88 | 339 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 89 | 340 | Observation | `Observation.valueCodeableConcept.coding` | X099770 | Rifampisin sensitive | http://terminology.kemkes.go.id/CodeSystem/examination |
| 90 | 341 | Observation | `Observation.valueCodeableConcept.coding` | X099771 | Rifampisin resistan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 91 | 342 | Observation | `Observation.valueCodeableConcept.coding` | X099772 | Rifampisin indeterminate | http://terminology.kemkes.go.id/CodeSystem/examination |
| 92 | 343 | Observation | `Observation.dataAbsentReason.coding` | LA15841-2 | Invalid result | http://loinc.org |
| 93 | 344 | Observation | `Observation.dataAbsentReason.coding` | error | Error | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 94 | 345 | Observation | `Observation.dataAbsentReason.coding` | OD000001 | Tidak ada hasil | http://terminology.kemkes.go.id/CodeSystem/data-absent-reason |
| 95 | 346 | Observation | `Observation.dataAbsentReason.coding` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 96 | 358 | DiagnosticReport | `DiagnosticReport.code.coding` | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | http://terminology.kemkes.go.id/sp |
| 97 | 374 | ServiceRequest | `ServiceRequest.code.coding` | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | http://terminology.kemkes.go.id/sp |
| 98 | 378 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 99 | 379 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 100 | 381 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 101 | 383 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 102 | 385 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 103 | 387 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 104 | 389 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 105 | 391 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 106 | 393 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 107 | 395 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 108 | 402 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 109 | 403 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 110 | 404 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 111 | 405 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 112 | 406 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 113 | 407 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 114 | 408 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 115 | 409 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 116 | 410 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 117 | 411 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 118 | 412 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 119 | 424 | Observation | `Observation.code.coding` | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | http://terminology.kemkes.go.id/sp |
| 120 | 425 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 121 | 426 | Observation | `Observation.valueCodeableConcept.coding` | X099770 | Rifampisin sensitive | http://terminology.kemkes.go.id/CodeSystem/examination |
| 122 | 427 | Observation | `Observation.valueCodeableConcept.coding` | X099771 | Rifampisin resistan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 123 | 428 | Observation | `Observation.valueCodeableConcept.coding` | X099772 | Rifampisin indeterminate | http://terminology.kemkes.go.id/CodeSystem/examination |
| 124 | 429 | Observation | `Observation.dataAbsentReason.coding` | LA15841-2 | Invalid result | http://loinc.org |
| 125 | 430 | Observation | `Observation.dataAbsentReason.coding` | error | Error | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 126 | 431 | Observation | `Observation.dataAbsentReason.coding` | OD000001 | Tidak ada hasil | http://terminology.kemkes.go.id/CodeSystem/data-absent-reason |
| 127 | 432 | Observation | `Observation.dataAbsentReason.coding` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 128 | 444 | DiagnosticReport | `DiagnosticReport.code.coding` | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | http://terminology.kemkes.go.id/sp |
| 129 | 463 | ServiceRequest | `ServiceRequest.code.coding` | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | http://terminology.kemkes.go.id/sp |
| 130 | 467 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 131 | 468 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 132 | 470 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 133 | 472 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 134 | 474 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 135 | 476 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 136 | 478 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 137 | 480 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 138 | 482 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 139 | 484 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 140 | 491 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 141 | 492 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 142 | 493 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 143 | 494 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 144 | 495 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 145 | 496 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 146 | 497 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 147 | 498 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 148 | 499 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 149 | 500 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 150 | 501 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 151 | 513 | Observation | `Observation.code.coding` | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | http://terminology.kemkes.go.id/sp |
| 152 | 526 | DiagnosticReport | `DiagnosticReport.code.coding` | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | http://terminology.kemkes.go.id/sp |
| 153 | 542 | ServiceRequest | `ServiceRequest.code.coding` | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | http://terminology.kemkes.go.id/sp |
| 154 | 546 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 155 | 547 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 156 | 549 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 157 | 551 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 158 | 553 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 159 | 555 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 160 | 557 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 161 | 559 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 162 | 561 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 163 | 563 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 164 | 571 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 165 | 572 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 166 | 573 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 167 | 574 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 168 | 575 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 169 | 576 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 170 | 577 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 171 | 578 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 172 | 579 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 173 | 580 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 174 | 581 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 175 | 593 | Observation | `Observation.code.coding` | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | http://terminology.kemkes.go.id/sp |
| 176 | 606 | DiagnosticReport | `DiagnosticReport.code.coding` | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | http://terminology.kemkes.go.id/sp |
| 177 | 622 | ServiceRequest | `ServiceRequest.code.coding` | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | http://terminology.kemkes.go.id/sp |
| 178 | 626 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 179 | 627 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 180 | 629 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 181 | 631 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 182 | 633 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 183 | 635 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 184 | 637 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 185 | 639 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 186 | 641 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 187 | 643 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 188 | 651 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 189 | 652 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 190 | 653 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 191 | 654 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 192 | 655 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 193 | 656 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 194 | 657 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 195 | 658 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 196 | 659 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 197 | 660 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 198 | 661 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 199 | 672 | Observation | `Observation.code.coding` | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | http://terminology.kemkes.go.id/sp |
| 200 | 685 | DiagnosticReport | `DiagnosticReport.code.coding` | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | http://terminology.kemkes.go.id/sp |
| 201 | 701 | ServiceRequest | `ServiceRequest.code.coding` | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | http://terminology.kemkes.go.id/sp |
| 202 | 705 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 203 | 706 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 204 | 708 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 205 | 710 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 206 | 712 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 207 | 714 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 208 | 716 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 209 | 718 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 210 | 720 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 211 | 722 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 212 | 729 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 213 | 730 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 214 | 731 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 215 | 732 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 216 | 733 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 217 | 734 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 218 | 735 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 219 | 736 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 220 | 737 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 221 | 738 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 222 | 739 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 223 | 751 | Observation | `Observation.code.coding` | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | http://terminology.kemkes.go.id/sp |
| 224 | 764 | DiagnosticReport | `DiagnosticReport.code.coding` | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | http://terminology.kemkes.go.id/sp |
| 225 | 783 | ServiceRequest | `ServiceRequest.code.coding` | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 226 | 787 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 227 | 788 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 228 | 790 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 229 | 792 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 230 | 794 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 231 | 796 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 232 | 798 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 233 | 800 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 234 | 802 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 235 | 804 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 236 | 811 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 237 | 812 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 238 | 813 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 239 | 814 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 240 | 815 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 241 | 816 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 242 | 817 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 243 | 818 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 244 | 819 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 245 | 820 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 246 | 821 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 247 | 833 | Observation | `Observation.code.coding` | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 248 | 834 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 249 | 835 | Observation | `Observation.valueCodeableConcept.coding` | X099770 | Rifampisin sensitive | http://terminology.kemkes.go.id/CodeSystem/examination |
| 250 | 836 | Observation | `Observation.valueCodeableConcept.coding` | X099771 | Rifampisin resistan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 251 | 837 | Observation | `Observation.valueCodeableConcept.coding` | X099772 | Rifampisin indeterminate | http://terminology.kemkes.go.id/CodeSystem/examination |
| 252 | 838 | Observation | `Observation.dataAbsentReason.coding` | LA15841-2 | Invalid result | http://loinc.org |
| 253 | 839 | Observation | `Observation.dataAbsentReason.coding` | error | Error | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 254 | 840 | Observation | `Observation.dataAbsentReason.coding` | OD000001 | Tidak ada hasil | http://terminology.kemkes.go.id/CodeSystem/data-absent-reason |
| 255 | 841 | Observation | `Observation.dataAbsentReason.coding` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 256 | 853 | DiagnosticReport | `DiagnosticReport.code.coding` | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 257 | 869 | ServiceRequest | `ServiceRequest.code.coding` | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 258 | 873 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 259 | 874 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 260 | 876 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 261 | 878 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 262 | 880 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 263 | 882 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 264 | 884 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 265 | 886 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 266 | 888 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 267 | 890 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 268 | 897 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 269 | 898 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 270 | 899 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 271 | 900 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 272 | 901 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 273 | 902 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 274 | 903 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 275 | 904 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 276 | 905 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 277 | 906 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 278 | 907 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 279 | 919 | Observation | `Observation.code.coding` | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 280 | 920 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 281 | 921 | Observation | `Observation.valueCodeableConcept.coding` | X099770 | Rifampisin sensitive | http://terminology.kemkes.go.id/CodeSystem/examination |
| 282 | 922 | Observation | `Observation.valueCodeableConcept.coding` | X099771 | Rifampisin resistan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 283 | 923 | Observation | `Observation.valueCodeableConcept.coding` | X099772 | Rifampisin indeterminate | http://terminology.kemkes.go.id/CodeSystem/examination |
| 284 | 924 | Observation | `Observation.dataAbsentReason.coding` | LA15841-2 | Invalid result | http://loinc.org |
| 285 | 925 | Observation | `Observation.dataAbsentReason.coding` | error | Error | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 286 | 926 | Observation | `Observation.dataAbsentReason.coding` | OD000001 | Tidak ada hasil | http://terminology.kemkes.go.id/CodeSystem/data-absent-reason |
| 287 | 927 | Observation | `Observation.dataAbsentReason.coding` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 288 | 939 | DiagnosticReport | `DiagnosticReport.code.coding` | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 289 | 959 | ServiceRequest | `ServiceRequest.code.coding` | MK099927 | Pemeriksaan PCR Open System | http://terminology.kemkes.go.id/CodeSystem/examination |
| 290 | 963 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 291 | 964 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 292 | 966 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 293 | 968 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 294 | 970 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 295 | 972 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 296 | 974 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 297 | 976 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 298 | 978 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 299 | 980 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 300 | 987 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 301 | 988 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 302 | 989 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 303 | 990 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 304 | 991 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 305 | 992 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 306 | 993 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 307 | 994 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 308 | 995 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 309 | 996 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 310 | 997 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 311 | 1009 | Observation | `Observation.code.coding` | MK099927 | Pemeriksaan PCR Open System | http://terminology.kemkes.go.id/CodeSystem/examination |
| 312 | 1010 | Observation | `Observation.component.code.coding` | 13956-8 | Mycobacterium tuberculosis DNA [Presence] in Specimen by NAA with probe detection | http://loinc.org |
| 313 | 1011 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 314 | 1012 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 315 | 1013 | Observation | `Observation.component.dataAbsentReason.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 316 | 1014 | Observation | `Observation.component.dataAbsentReason.coding` | 263921008 | Unresolved | http://snomed.info/sct |
| 317 | 1015 | Observation | `Observation.component.dataAbsentReason.coding` | LA7341-6 | Incomplete | http://loinc.org |
| 318 | 1016 | Observation | `Observation.component.code.coding` | 89489-9 | rifAMPin [Susceptibility] by Genotype method | http://loinc.org |
| 319 | 1017 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 320 | 1018 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 321 | 1019 | Observation | `Observation.component.dataAbsentReason.coding` | J099384 | Unreportable | http://terminology.kemkes.go.id/CodeSystem/examination |
| 322 | 1020 | Observation | `Observation.component.code.coding` | 89488-1 | Isoniazid [Susceptibility] by Genotype method | http://loinc.org |
| 323 | 1021 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 324 | 1022 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 325 | 1023 | Observation | `Observation.component.dataAbsentReason.coding` | J099384 | Unreportable | http://terminology.kemkes.go.id/CodeSystem/examination |
| 326 | 1024 | Observation | `Observation.component.code.coding` | 46246-5 | Mycobacterium tuberculosis katG gene isoniazid high level resistance mutation [Identifier] by Molecular method | http://loinc.org |
| 327 | 1025 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 328 | 1026 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 329 | 1027 | Observation | `Observation.component.code.coding` | 63072-3 | Mycobacterium tuberculosis inhA gene isoniazid low level resistance mutation [Presence] by Molecular method | http://loinc.org |
| 330 | 1028 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 331 | 1029 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 332 | 1030 | Observation | `Observation.component.code.coding` | 110379001 | Mycobacterium, non-tuberculosis (organism) | http://snomed.info/sct |
| 333 | 1031 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 334 | 1032 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 335 | 1045 | DiagnosticReport | `DiagnosticReport.code.coding` | MK099927 | Pemeriksaan PCR Open System | http://terminology.kemkes.go.id/CodeSystem/examination |
| 336 | 1065 | ServiceRequest | `ServiceRequest.code.coding` | X099379 | Pemeriksaan TCM XDR | http://terminology.kemkes.go.id/CodeSystem/examination |
| 337 | 1069 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 338 | 1070 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 339 | 1072 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 340 | 1074 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 341 | 1076 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 342 | 1078 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 343 | 1080 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 344 | 1082 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 345 | 1084 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 346 | 1086 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 347 | 1093 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 348 | 1094 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 349 | 1095 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 350 | 1096 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 351 | 1097 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 352 | 1098 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 353 | 1099 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 354 | 1100 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 355 | 1101 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 356 | 1102 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 357 | 1103 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 358 | 1116 | Observation | `Observation.code.coding` | X099379 | Pemeriksaan TCM XDR | http://terminology.kemkes.go.id/CodeSystem/examination |
| 359 | 1117 | Observation | `Observation.valueCodeableConcept.coding` | X099781 | Hasil Valid | http://terminology.kemkes.go.id/CodeSystem/examination |
| 360 | 1118 | Observation | `Observation.dataAbsentReason.coding` | LA15841-2 | Invalid result | http://loinc.org |
| 361 | 1119 | Observation | `Observation.dataAbsentReason.coding` | error | Error | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 362 | 1120 | Observation | `Observation.dataAbsentReason.coding` | OD000001 | Tidak ada hasil | http://terminology.kemkes.go.id/CodeSystem/data-absent-reason |
| 363 | 1122 | Observation | `Observation.component.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 364 | 1123 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 365 | 1124 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 366 | 1126 | Observation | `Observation.component.code.coding` | X099391 | H Dosis Rendah (Low) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 367 | 1127 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 368 | 1128 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 369 | 1129 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 370 | 1131 | Observation | `Observation.component.code.coding` | 89488-1 | Isoniazid [Susceptibility] by Genotype method | http://loinc.org |
| 371 | 1132 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 372 | 1133 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 373 | 1134 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 374 | 1136 | Observation | `Observation.component.code.coding` | 96110-2 | Ethionamide [Susceptibility] by Genotype method | http://loinc.org |
| 375 | 1137 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 376 | 1138 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 377 | 1140 | Observation | `Observation.component.code.coding` | X099392 | FQ Dosis Rendah (Low) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 378 | 1141 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 379 | 1142 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 380 | 1143 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 381 | 1145 | Observation | `Observation.component.code.coding` | 89487-3 | Fluoroquinolone [Susceptibility] by Genotype method | http://loinc.org |
| 382 | 1146 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 383 | 1147 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 384 | 1148 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 385 | 1150 | Observation | `Observation.component.code.coding` | 89484-0 | Amikacin [Susceptibility] by Genotype method | http://loinc.org |
| 386 | 1151 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 387 | 1152 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 388 | 1153 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 389 | 1155 | Observation | `Observation.component.code.coding` | 89482-4 | Kanamycin [Susceptibility] by Genotype method | http://loinc.org |
| 390 | 1156 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 391 | 1157 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 392 | 1158 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 393 | 1160 | Observation | `Observation.component.code.coding` | 89483-2 | Capreomycin [Susceptibility] by Genotype method | http://loinc.org |
| 394 | 1161 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 395 | 1162 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 396 | 1163 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 397 | 1176 | DiagnosticReport | `DiagnosticReport.code.coding` | X099379 | Pemeriksaan TCM XDR | http://terminology.kemkes.go.id/CodeSystem/examination |
| 398 | 1196 | ServiceRequest | `ServiceRequest.code.coding` | X099380 | Line Probe Assay (LPA) Lini 1 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 399 | 1200 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 400 | 1201 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 401 | 1203 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 402 | 1205 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 403 | 1207 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 404 | 1209 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 405 | 1211 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 406 | 1213 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 407 | 1215 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 408 | 1217 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 409 | 1224 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 410 | 1225 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 411 | 1226 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 412 | 1227 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 413 | 1228 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 414 | 1229 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 415 | 1230 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 416 | 1231 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 417 | 1232 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 418 | 1233 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 419 | 1234 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 420 | 1246 | Observation | `Observation.code.coding` | X099380 | Line Probe Assay (LPA) Lini 1 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 421 | 1247 | Observation | `Observation.valueCodeableConcept.coding` | X099781 | Hasil Valid | http://terminology.kemkes.go.id/CodeSystem/examination |
| 422 | 1248 | Observation | `Observation.dataAbsentReason.coding` | LA15841-2 | Invalid result | http://loinc.org |
| 423 | 1250 | Observation | `Observation.component.code.coding` | 13956-8 | Mycobacterium tuberculosis DNA [Presence] in Specimen by NAA with probe detection | http://loinc.org |
| 424 | 1251 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 425 | 1252 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 426 | 1254 | Observation | `Observation.component.code.coding` | 89489-9 | rifAMPin [Susceptibility] by Genotype method | http://loinc.org |
| 427 | 1255 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 428 | 1256 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 429 | 1257 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 430 | 1258 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 431 | 1260 | Observation | `Observation.component.code.coding` | X099391 | H Dosis Rendah (Low) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 432 | 1261 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 433 | 1262 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 434 | 1263 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 435 | 1264 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 436 | 1266 | Observation | `Observation.component.code.coding` | X099783 | H Dosis Tinggi (High) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 437 | 1267 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 438 | 1268 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 439 | 1269 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 440 | 1270 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 441 | 1272 | Observation | `Observation.component.code.coding` | 96110-2 | Ethionamide [Susceptibility] by Genotype method | http://loinc.org |
| 442 | 1273 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 443 | 1274 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 444 | 1275 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 445 | 1276 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 446 | 1278 | Observation | `Observation.component.code.coding` | 103960-1 | Prothionamide [Susceptibility] by Genotype method | http://loinc.org |
| 447 | 1279 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 448 | 1280 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 449 | 1281 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 450 | 1282 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 451 | 1295 | DiagnosticReport | `DiagnosticReport.code.coding` | X099380 | Line Probe Assay (LPA) Lini 1 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 452 | 1315 | ServiceRequest | `ServiceRequest.code.coding` | X099381 | Line Probe Assay (LPA) Lini 2 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 453 | 1319 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 454 | 1320 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 455 | 1322 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 456 | 1324 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 457 | 1326 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 458 | 1328 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 459 | 1330 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 460 | 1332 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 461 | 1334 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 462 | 1336 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 463 | 1343 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 464 | 1344 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 465 | 1345 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 466 | 1346 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 467 | 1347 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 468 | 1348 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 469 | 1349 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 470 | 1350 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 471 | 1351 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 472 | 1352 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 473 | 1353 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 474 | 1364 | Observation | `Observation.code.coding` | X099381 | Line Probe Assay (LPA) Lini 2 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 475 | 1365 | Observation | `Observation.valueCodeableConcept.coding` | X099781 | Hasil Valid | http://terminology.kemkes.go.id/CodeSystem/examination |
| 476 | 1366 | Observation | `Observation.dataAbsentReason.coding` | LA15841-2 | Invalid result | http://loinc.org |
| 477 | 1368 | Observation | `Observation.component.code.coding` | 13956-8 | Mycobacterium tuberculosis DNA [Presence] in Specimen by NAA with probe detection | http://loinc.org |
| 478 | 1369 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 479 | 1370 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 480 | 1372 | Observation | `Observation.component.code.coding` | 20629-2 | levoFLOXacin [Susceptibility] | http://loinc.org |
| 481 | 1373 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 482 | 1374 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 483 | 1375 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 484 | 1376 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 485 | 1378 | Observation | `Observation.component.code.coding` | 96112-8 | Moxifloxacin [Susceptibility] by Genotype method | http://loinc.org |
| 486 | 1379 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 487 | 1380 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 488 | 1381 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 489 | 1382 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 490 | 1384 | Observation | `Observation.component.code.coding` | X099775 | Moxifloxacin DT (Mfx DT) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 491 | 1385 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 492 | 1386 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 493 | 1387 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 494 | 1388 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 495 | 1390 | Observation | `Observation.component.code.coding` | 89482-4 | Kanamycin [Susceptibility] by Genotype method | http://loinc.org |
| 496 | 1391 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 497 | 1392 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 498 | 1393 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 499 | 1394 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 500 | 1396 | Observation | `Observation.component.code.coding` | 89484-0 | Amikacin [Susceptibility] by Genotype method | http://loinc.org |
| 501 | 1397 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 502 | 1398 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 503 | 1399 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 504 | 1400 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 505 | 1402 | Observation | `Observation.component.code.coding` | 89483-2 | Capreomycin [Susceptibility] by Genotype method | http://loinc.org |
| 506 | 1403 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 507 | 1404 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 508 | 1405 | Observation | `Observation.component.valueCodeableConcept.coding` | LA11884-6 | Indeterminate | http://loinc.org |
| 509 | 1406 | Observation | `Observation.component.valueCodeableConcept.coding` | X099774 | Ress Inffered (RI) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 510 | 1419 | DiagnosticReport | `DiagnosticReport.code.coding` | X099381 | Line Probe Assay (LPA) Lini 2 | http://terminology.kemkes.go.id/CodeSystem/examination |
| 511 | 1440 | ServiceRequest | `ServiceRequest.code.coding` | X099389 | Hasil Pemeriksaan Biakan TB (Metode: LJ) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 512 | 1441 | ServiceRequest | `ServiceRequest.code.coding` | X099390 | Hasil Pemeriksaan Biakan TB (Metode: MGIT) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 513 | 1445 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 514 | 1446 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 515 | 1448 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 516 | 1450 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 517 | 1452 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 518 | 1454 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 519 | 1456 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 520 | 1458 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 521 | 1460 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 522 | 1462 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 523 | 1469 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 524 | 1470 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 525 | 1471 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 526 | 1472 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 527 | 1473 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 528 | 1474 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 529 | 1475 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 530 | 1476 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 531 | 1477 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 532 | 1478 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 533 | 1479 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 534 | 1488 | Observation | `Observation.method.coding` | OM000001 | LJ | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 535 | 1489 | Observation | `Observation.method.coding` | OM000002 | MGIT | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 536 | 1492 | Observation | `Observation.code.coding` | X099389 | Hasil Pemeriksaan Biakan TB (Metode: LJ) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 537 | 1493 | Observation | `Observation.code.coding` | X099390 | Hasil Pemeriksaan Biakan TB (Metode: MGIT) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 538 | 1494 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 539 | 1495 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 540 | 1496 | Observation | `Observation.valueCodeableConcept.coding` | LA11841-6 | + | http://loinc.org |
| 541 | 1497 | Observation | `Observation.valueCodeableConcept.coding` | LA11842-4 | ++ | http://loinc.org |
| 542 | 1498 | Observation | `Observation.valueCodeableConcept.coding` | LA11843-2 | +++ | http://loinc.org |
| 543 | 1499 | Observation | `Observation.valueCodeableConcept.coding` | 110379001 | Mycobacterium, non-tuberculosis (organism) | http://snomed.info/sct |
| 544 | 1500 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 545 | 1513 | DiagnosticReport | `DiagnosticReport.code.coding` | X099389 | Hasil Pemeriksaan Biakan TB (Metode: LJ) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 546 | 1514 | DiagnosticReport | `DiagnosticReport.code.coding` | X099390 | Hasil Pemeriksaan Biakan TB (Metode: MGIT) | http://terminology.kemkes.go.id/CodeSystem/examination |
| 547 | 1531 | ServiceRequest | `ServiceRequest.code.coding` | X099383 | Pemeriksaan Paket Standar Kepekaan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 548 | 1535 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000013 | Pemeriksaan Diagnosis Baseline | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 549 | 1536 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 550 | 1538 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000007 | Pemeriksaan Diagnosis | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 551 | 1540 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 552 | 1542 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 553 | 1544 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000009 | Pemeriksaan Ulang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 554 | 1546 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 555 | 1548 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 556 | 1550 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000008 | Follow Up | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 557 | 1552 | ServiceRequest | `ServiceRequest.reasonCode.coding` | SRR000010 | Akhir Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 558 | 1559 | Specimen | `Specimen.type.coding` | 418564007 | Pleural fluid specimen | http://snomed.info/sct |
| 559 | 1560 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 560 | 1561 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 561 | 1562 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 562 | 1563 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 563 | 1564 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 564 | 1565 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 565 | 1566 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 566 | 1567 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 567 | 1568 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 568 | 1569 | Specimen | `Specimen.type.coding` | 123038009 | Specimen | http://snomed.info/sct |
| 569 | 1580 | Observation | `Observation.code.coding` | X099383 | Pemeriksaan Paket Standar Kepekaan | http://terminology.kemkes.go.id/CodeSystem/examination |
| 570 | 1582 | Observation | `Observation.component.code.coding` | 20383-6 | Isoniazid [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 571 | 1583 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 572 | 1584 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 573 | 1585 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 574 | 1586 | Observation | `Observation.component.dataAbsentReason.coding` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 575 | 1588 | Observation | `Observation.component.code.coding` | X099776 | H High Dosage [Susceptibility] by Method for Slow-growing mycobacteria | http://terminology.kemkes.go.id/CodeSystem/examination |
| 576 | 1589 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 577 | 1590 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 578 | 1591 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 579 | 1592 | Observation | `Observation.component.dataAbsentReason.coding` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 580 | 1594 | Observation | `Observation.component.code.coding` | 53716-7 | levoFLOXacin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 581 | 1595 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 582 | 1596 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 583 | 1597 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 584 | 1598 | Observation | `Observation.component.dataAbsentReason.coding` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 585 | 1600 | Observation | `Observation.component.code.coding` | 41502-6 | Moxifloxacin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 586 | 1601 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 587 | 1602 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 588 | 1603 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 589 | 1604 | Observation | `Observation.component.dataAbsentReason.coding` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 590 | 1606 | Observation | `Observation.component.code.coding` | X099778 | Moxifloxacin High Dosage [Susceptibility] by Method for Slow-growing mycobacteria | http://terminology.kemkes.go.id/CodeSystem/examination |
| 591 | 1607 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 592 | 1608 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 593 | 1609 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 594 | 1610 | Observation | `Observation.component.dataAbsentReason.coding` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 595 | 1612 | Observation | `Observation.component.code.coding` | 23609-1 | Kanamycin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 596 | 1613 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 597 | 1614 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 598 | 1615 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 599 | 1616 | Observation | `Observation.component.dataAbsentReason.coding` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 600 | 1618 | Observation | `Observation.component.code.coding` | 20373-7 | Amikacin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 601 | 1619 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 602 | 1620 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 603 | 1621 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 604 | 1622 | Observation | `Observation.component.dataAbsentReason.coding` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 605 | 1624 | Observation | `Observation.component.code.coding` | 23607-5 | Capreomycin [Susceptibility] by Method for Slow-growing mycobacteria | http://loinc.org |
| 606 | 1625 | Observation | `Observation.component.valueCodeableConcept.coding` | LA24225-7 | Susceptible | http://loinc.org |
| 607 | 1626 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6676-6 | Resistant | http://loinc.org |
| 608 | 1627 | Observation | `Observation.component.valueCodeableConcept.coding` | LA16550-8 | Intermediate | http://loinc.org |
| 609 | 1628 | Observation | `Observation.component.dataAbsentReason.coding` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 610 | 1630 | Observation | `Observation.component.code.coding` | SP000472 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya | http://terminology.kemkes.go.id/sp |
| 611 | 1632 | Observation | `Observation.component.code.coding` | SP000473 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 1 | http://terminology.kemkes.go.id/sp |
| 612 | 1634 | Observation | `Observation.component.code.coding` | SP000474 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 2 | http://terminology.kemkes.go.id/sp |
| 613 | 1636 | Observation | `Observation.component.code.coding` | SP000475 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 3 | http://terminology.kemkes.go.id/sp |
| 614 | 1638 | Observation | `Observation.component.code.coding` | SP000476 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 4 | http://terminology.kemkes.go.id/sp |
| 615 | 1640 | Observation | `Observation.component.code.coding` | SP000477 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 5 | http://terminology.kemkes.go.id/sp |
| 616 | 1654 | DiagnosticReport | `DiagnosticReport.code.coding` | X099383 | Pemeriksaan Paket Standar Kepekaan | http://terminology.kemkes.go.id/CodeSystem/examination |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 195 |
| http://loinc.org | 156 |
| http://snomed.info/sct | 152 |
| http://terminology.kemkes.go.id/CodeSystem/examination | 62 |
| http://terminology.kemkes.go.id/sp | 24 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 20 |
| http://terminology.kemkes.go.id/CodeSystem/data-absent-reason | 5 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 2 |
| **Total** | **616** |

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
