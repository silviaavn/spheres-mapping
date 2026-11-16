# File mentah SITB TB 04 (Fasyankes & Rujukan) — struktur kolom

Sumber: export SITB `Kab_Purbalingga_Report_TB_04_Fasyankes_spheres_Januari-Juni_2025.xlsx` dan `Kab_Purbalingga_Report_TB_04_Rujukan_spheres_Januari-Juni_2025.xlsx`. Header kedua file sama persis (114 kolom), jadi memakai 1 dictionary. Tabel BQ: `sitb_tb_04_fasyankes` dan `sitb_tb_04_rujukan` (kolom sama).
File asli **tidak** disimpan di repo karena berisi data pasien. File ini berisi struktur kolom, jumlah terisi, dan nilai pilihan (kolom identitas & teks bebas tidak ditampilkan).

- `TB_04_Fasyankes`: header sampai baris 17 (baris 17 = nomor kolom (1), (2), ...), 2039 baris data.
- `TB_04_Rujukan`: header sampai baris 17 (baris 17 = nomor kolom (1), (2), ...), 4403 baris data.

| # | Kolom Excel | Header | Variabel BQ | Terisi (TB_04_Fasyankes) | Terisi (TB_04_Rujukan) | Nilai (frekuensi) |
|---|---|---|---|---|---|---|
| 1 | C | No. Urut | `no_urut` ⛔ tidak dimapping | 2039/2039 | 4403/4403 | `<angka>` (6442) |
| 2 | D | No. Identitas Sediaan | `no_identitas_sediaan` | 2039/2039 | 4403/4403 | *(identitas / teks bebas, tidak ditampilkan)* |
| 3 | E | No. Rekam Medis | `no_rekam_medis` | 561/2039 | 593/4403 | *(identitas / teks bebas, tidak ditampilkan)* |
| 4 | F | Nama Lengkap Pasien | `nama_lengkap_pasien` | 2039/2039 | 4403/4403 | *(identitas / teks bebas, tidak ditampilkan)* |
| 5 | G | NIK (Nomor Induk Kependudukan) | `nik_nomor_induk_kependudukan` | 2039/2039 | 4403/4403 | *(identitas / teks bebas, tidak ditampilkan)* |
| 6 | H | Umur | `umur` | 2039/2039 | 4403/4403 | `<angka>` (6442) |
| 7 | I | Jenis Kelamin | `jenis_kelamin` | 2039/2039 | 4403/4403 | `P` (3609), `L` (2833) |
| 8 | J | Alamat Lengkap | `alamat_lengkap` | 2039/2039 | 4403/4403 | *(identitas / teks bebas, tidak ditampilkan)* |
| 9 | K | Nama Fasilitas Kesehatan Asal Contoh Uji | `nama_fasilitas_kesehatan_asal_contoh_uji` | 2039/2039 | 4403/4403 | *(identitas / teks bebas, tidak ditampilkan)* |
| 10 | L | Alasan Pemeriksaan | `alasan_pemeriksaan` | 2039/2039 | 4403/4403 | `Diagnosis TB SO` (5681), `Akhir Pengobatan` (295), `Diagnosis TB RO` (155), `Follow Up Bulan ke 2` (137), `Follow Up Bulan ke 5` (125), `Follow Up Bulan ke 6` (21), `Pemeriksaan Diagnosis Baseline` (13), `Pemeriksaan Ulang Ke 2` (10), `Pemeriksaan Ulang Ke 5` (4), `Pemeriksaan Ulang Ke 6` (1) |
| 11 | M | Pemeriksaan Mikroskopis / No.Reg Lab | `pemeriksaan_mikroskopis_noreg_lab` ⛔ tidak dimapping | 590/2039 | 4/4403 | `<angka>` (534), + 51 nilai lain |
| 12 | N | Pemeriksaan Mikroskopis / Jenis Contoh Uji | `pemeriksaan_mikroskopis_jenis_contoh_uji` | 590/2039 | 4/4403 | `Dahak` (572), `dahak` (21), `SPUTUM/DAHAK` (1) |
| 13 | O | Pemeriksaan Mikroskopis / Tgl Contoh Uji Diterima | `pemeriksaan_mikroskopis_tgl_contoh_uji_diterima` | 590/2039 | 4/4403 | `<tanggal>` (594) |
| 14 | P | Pemeriksaan Mikroskopis / 1 / Tgl Hasil Dilaporkan | `pemeriksaan_mikroskopis_1_tgl_hasil_dilaporkan` | 590/2039 | 4/4403 | `<tanggal>` (594) |
| 15 | Q | Pemeriksaan Mikroskopis / 1 / Hasil Pemeriksaan | `pemeriksaan_mikroskopis_1_hasil_pemeriksaan` | 590/2039 | 4/4403 | `Neg` (579), `1+` (6), `<angka>` (5), `2+` (3), `TDL` (1) |
| 16 | R | Pemeriksaan Mikroskopis / 2 / Tgl Hasil Dilaporkan | `pemeriksaan_mikroskopis_2_tgl_hasil_dilaporkan` | 480/2039 | 4/4403 | `<tanggal>` (484) |
| 17 | S | Pemeriksaan Mikroskopis / 2 / Hasil Pemeriksaan | `pemeriksaan_mikroskopis_2_hasil_pemeriksaan` | 480/2039 | 4/4403 | `Neg` (472), `1+` (7), `<angka>` (2), `2+` (2), `TDL` (1) |
| 18 | T | Pemeriksaan Xpert MTB RIF (Xpert) / No.Reg Lab | `pemeriksaan_xpert_mtb_rif_xpert_noreg_lab` ⛔ tidak dimapping | 1447/2039 | 4388/4403 | `<angka>` (5296), + 520 nilai lain |
| 19 | U | Pemeriksaan Xpert MTB RIF (Xpert) / Jenis Contoh Uji | `pemeriksaan_xpert_mtb_rif_xpert_jenis_contoh_uji` | 1447/2039 | 4388/4403 | `Dahak` (5833), `Cairan Pleura` (1), `LCS` (1) |
| 20 | V | Pemeriksaan Xpert MTB RIF (Xpert) / Tgl Contoh Uji Diterima | `pemeriksaan_xpert_mtb_rif_xpert_tgl_contoh_uji_diterima` | 1447/2039 | 4388/4403 | `<tanggal>` (5835) |
| 21 | W | Pemeriksaan Xpert MTB RIF (Xpert) / 1 / Tgl Hasil Dilaporkan | `pemeriksaan_xpert_mtb_rif_xpert_1_tgl_hasil_dilaporkan` | 1447/2039 | 4388/4403 | `<tanggal>` (5835) |
| 22 | X | Pemeriksaan Xpert MTB RIF (Xpert) / 1 / Hasil Pemeriksaan | `pemeriksaan_xpert_mtb_rif_xpert_1_hasil_pemeriksaan` | 1447/2039 | 4388/4403 | `Neg` (5146), `Rif Sen` (577), `ERROR` (83), `Rif Res` (11), `INVALID` (9), `NO RESULT` (8), `TDL` (1) |
| 23 | Y | Pemeriksaan Xpert MTB RIF (Xpert) / 2 / Tgl Hasil Dilaporkan | `pemeriksaan_xpert_mtb_rif_xpert_2_tgl_hasil_dilaporkan` | 18/2039 | 67/4403 | `<tanggal>` (85) |
| 24 | Z | Pemeriksaan Xpert MTB RIF (Xpert) / 2 / Hasil Pemeriksaan | `pemeriksaan_xpert_mtb_rif_xpert_2_hasil_pemeriksaan` | 18/2039 | 67/4403 | `Neg` (65), `Rif Sen` (14), `Rif Indet` (2), `Rif Res` (2), `ERROR` (1), `NO RESULT` (1) |
| 25 | AA | Pemeriksaan Xpert MTB RIF (Truenat) / No.Reg Lab | `pemeriksaan_xpert_mtb_rif_truenat_noreg_lab` ⛔ tidak dimapping | 0/2039 | 0/4403 |  |
| 26 | AB | Pemeriksaan Xpert MTB RIF (Truenat) / Jenis Contoh Uji | `pemeriksaan_xpert_mtb_rif_truenat_jenis_contoh_uji` | 0/2039 | 0/4403 |  |
| 27 | AC | Pemeriksaan Xpert MTB RIF (Truenat) / Tgl Contoh Uji Diterima | `pemeriksaan_xpert_mtb_rif_truenat_tgl_contoh_uji_diterima` | 0/2039 | 0/4403 |  |
| 28 | AD | Pemeriksaan Xpert MTB RIF (Truenat) / Chip MTB Plus / 1 / Tgl Hasil Dilaporkan | `pemeriksaan_xpert_mtb_rif_truenat_chip_mtb_plus_1_tgl_hasil_dilaporkan` | 0/2039 | 0/4403 |  |
| 29 | AE | Pemeriksaan Xpert MTB RIF (Truenat) / Chip MTB Plus / 1 / Hasil Pemeriksaan | `pemeriksaan_xpert_mtb_rif_truenat_chip_mtb_plus_1_hasil_pemeriksaan` | 0/2039 | 0/4403 |  |
| 30 | AF | Pemeriksaan Xpert MTB RIF (Truenat) / Chip MTB Plus / 2 / Tgl Hasil Dilaporkan | `pemeriksaan_xpert_mtb_rif_truenat_chip_mtb_plus_2_tgl_hasil_dilaporkan` | 0/2039 | 0/4403 |  |
| 31 | AG | Pemeriksaan Xpert MTB RIF (Truenat) / Chip MTB Plus / 2 / Hasil Pemeriksaan | `pemeriksaan_xpert_mtb_rif_truenat_chip_mtb_plus_2_hasil_pemeriksaan` | 0/2039 | 0/4403 |  |
| 32 | AH | Pemeriksaan Xpert MTB RIF (Truenat) / Chip MTB Rif / 1 / Tgl Hasil Dilaporkan | `pemeriksaan_xpert_mtb_rif_truenat_chip_mtb_rif_1_tgl_hasil_dilaporkan` | 0/2039 | 0/4403 |  |
| 33 | AI | Pemeriksaan Xpert MTB RIF (Truenat) / Chip MTB Rif / 1 / Hasil Pemeriksaan | `pemeriksaan_xpert_mtb_rif_truenat_chip_mtb_rif_1_hasil_pemeriksaan` | 0/2039 | 0/4403 |  |
| 34 | AJ | Pemeriksaan Xpert MTB RIF (Truenat) / Chip MTB Rif / 2 / Tgl Hasil Dilaporkan | `pemeriksaan_xpert_mtb_rif_truenat_chip_mtb_rif_2_tgl_hasil_dilaporkan` | 0/2039 | 0/4403 |  |
| 35 | AK | Pemeriksaan Xpert MTB RIF (Truenat) / Chip MTB Rif / 2 / Hasil Pemeriksaan | `pemeriksaan_xpert_mtb_rif_truenat_chip_mtb_rif_2_hasil_pemeriksaan` | 0/2039 | 0/4403 |  |
| 36 | AL | Pemeriksaan TCM MTB RIF INH (BD MAX) / No.Reg Lab | `pemeriksaan_tcm_mtb_rif_inh_bd_max_noreg_lab` ⛔ tidak dimapping | 0/2039 | 0/4403 |  |
| 37 | AM | Pemeriksaan TCM MTB RIF INH (BD MAX) / Jenis Contoh Uji | `pemeriksaan_tcm_mtb_rif_inh_bd_max_jenis_contoh_uji` | 0/2039 | 0/4403 |  |
| 38 | AN | Pemeriksaan TCM MTB RIF INH (BD MAX) / Tgl Contoh Uji Diterima | `pemeriksaan_tcm_mtb_rif_inh_bd_max_tgl_contoh_uji_diterima` | 0/2039 | 0/4403 |  |
| 39 | AO | Pemeriksaan TCM MTB RIF INH (BD MAX) / 1 / Tgl Hasil Dilaporkan | `pemeriksaan_tcm_mtb_rif_inh_bd_max_1_tgl_hasil_dilaporkan` | 0/2039 | 0/4403 |  |
| 40 | AP | Pemeriksaan TCM MTB RIF INH (BD MAX) / 1 / Hasil Pemeriksaan | `pemeriksaan_tcm_mtb_rif_inh_bd_max_1_hasil_pemeriksaan` | 0/2039 | 0/4403 |  |
| 41 | AQ | Pemeriksaan TCM MTB RIF INH (BD MAX) / 2 / Tgl Hasil Dilaporkan | `pemeriksaan_tcm_mtb_rif_inh_bd_max_2_tgl_hasil_dilaporkan` | 0/2039 | 0/4403 |  |
| 42 | AR | Pemeriksaan TCM MTB RIF INH (BD MAX) / 2 / Hasil Pemeriksaan | `pemeriksaan_tcm_mtb_rif_inh_bd_max_2_hasil_pemeriksaan` | 0/2039 | 0/4403 |  |
| 43 | AS | Pemeriksaan PCR Open System / No.Reg Lab | `pemeriksaan_pcr_open_system_noreg_lab` ⛔ tidak dimapping | 0/2039 | 0/4403 |  |
| 44 | AT | Pemeriksaan PCR Open System / Jenis Contoh Uji | `pemeriksaan_pcr_open_system_jenis_contoh_uji` | 0/2039 | 0/4403 |  |
| 45 | AU | Pemeriksaan PCR Open System / Tgl Contoh Uji Diterima | `pemeriksaan_pcr_open_system_tgl_contoh_uji_diterima` | 0/2039 | 0/4403 |  |
| 46 | AV | Pemeriksaan PCR Open System / Tgl Hasil Dilaporkan | `pemeriksaan_pcr_open_system_tgl_hasil_dilaporkan` | 0/2039 | 0/4403 |  |
| 47 | AW | Pemeriksaan PCR Open System / Hasil Pemeriksaan / MTB | `pemeriksaan_pcr_open_system_hasil_pemeriksaan_mtb` | 0/2039 | 0/4403 |  |
| 48 | AX | Pemeriksaan PCR Open System / Hasil Pemeriksaan / RIF | `pemeriksaan_pcr_open_system_hasil_pemeriksaan_rif` | 0/2039 | 0/4403 |  |
| 49 | AY | Pemeriksaan PCR Open System / Hasil Pemeriksaan / INH | `pemeriksaan_pcr_open_system_hasil_pemeriksaan_inh` | 0/2039 | 0/4403 |  |
| 50 | AZ | Pemeriksaan PCR Open System / Hasil Pemeriksaan / katG | `pemeriksaan_pcr_open_system_hasil_pemeriksaan_katg` | 0/2039 | 0/4403 |  |
| 51 | BA | Pemeriksaan PCR Open System / Hasil Pemeriksaan / inhApr | `pemeriksaan_pcr_open_system_hasil_pemeriksaan_inhapr` | 0/2039 | 0/4403 |  |
| 52 | BB | Pemeriksaan PCR Open System / Hasil Pemeriksaan / NTM | `pemeriksaan_pcr_open_system_hasil_pemeriksaan_ntm` | 0/2039 | 0/4403 |  |
| 53 | BC | Pemeriksaan Xpert (TCM) XDR / No.Reg Lab | `pemeriksaan_xpert_tcm_xdr_noreg_lab` ⛔ tidak dimapping | 2/2039 | 11/4403 | `<angka>` (13) |
| 54 | BD | Pemeriksaan Xpert (TCM) XDR / Jenis Contoh Uji | `pemeriksaan_xpert_tcm_xdr_jenis_contoh_uji` | 2/2039 | 11/4403 | `Dahak` (13) |
| 55 | BE | Pemeriksaan Xpert (TCM) XDR / Tgl Contoh Uji Diterima | `pemeriksaan_xpert_tcm_xdr_tgl_contoh_uji_diterima` | 2/2039 | 11/4403 | `<tanggal>` (13) |
| 56 | BF | Pemeriksaan Xpert (TCM) XDR / Tgl Hasil Dilaporkan | `pemeriksaan_xpert_tcm_xdr_tgl_hasil_dilaporkan` | 2/2039 | 11/4403 | `<tanggal>` (13) |
| 57 | BG | Pemeriksaan Xpert (TCM) XDR / Hasil Pemeriksaan / Valid/Invalid/No Result/Error | `pemeriksaan_xpert_tcm_xdr_hasil_pemeriksaan_validinvalidno_resulterror` | 2/2039 | 11/4403 | `Valid` (13) |
| 58 | BH | Pemeriksaan Xpert (TCM) XDR / Hasil Pemeriksaan / MTB | `pemeriksaan_xpert_tcm_xdr_hasil_pemeriksaan_mtb` | 2/2039 | 11/4403 | `D` (12), `ND` (1) |
| 59 | BI | Pemeriksaan Xpert (TCM) XDR / Hasil Pemeriksaan / H Dosis Rendah (Low) | `pemeriksaan_xpert_tcm_xdr_hasil_pemeriksaan_h_dosis_rendah_low` | 2/2039 | 10/4403 | `RND` (10), `RD` (2) |
| 60 | BJ | Pemeriksaan Xpert (TCM) XDR / Hasil Pemeriksaan / H | `pemeriksaan_xpert_tcm_xdr_hasil_pemeriksaan_h` | 2/2039 | 10/4403 | `RND` (12) |
| 61 | BK | Pemeriksaan Xpert (TCM) XDR / Hasil Pemeriksaan / FQ Dosis Rendah (Low) | `pemeriksaan_xpert_tcm_xdr_hasil_pemeriksaan_fq_dosis_rendah_low` | 2/2039 | 10/4403 | `RND` (11), `IDT` (1) |
| 62 | BL | Pemeriksaan Xpert (TCM) XDR / Hasil Pemeriksaan / FQ | `pemeriksaan_xpert_tcm_xdr_hasil_pemeriksaan_fq` | 2/2039 | 10/4403 | `RND` (12) |
| 63 | BM | Pemeriksaan Xpert (TCM) XDR / Hasil Pemeriksaan / Amk | `pemeriksaan_xpert_tcm_xdr_hasil_pemeriksaan_amk` | 2/2039 | 10/4403 | `RND` (11), `IDT` (1) |
| 64 | BN | Pemeriksaan Xpert (TCM) XDR / Hasil Pemeriksaan / Km | `pemeriksaan_xpert_tcm_xdr_hasil_pemeriksaan_km` | 2/2039 | 10/4403 | `RND` (11), `IDT` (1) |
| 65 | BO | Pemeriksaan Xpert (TCM) XDR / Hasil Pemeriksaan / Cm | `pemeriksaan_xpert_tcm_xdr_hasil_pemeriksaan_cm` | 2/2039 | 10/4403 | `RND` (11), `IDT` (1) |
| 66 | BP | Pemeriksaan Xpert (TCM) XDR / Hasil Pemeriksaan / Eto | `pemeriksaan_xpert_tcm_xdr_hasil_pemeriksaan_eto` | 2/2039 | 10/4403 | `RND` (12) |
| 67 | BQ | Pemeriksaan LPA Lini Satu / No.Reg Lab | `pemeriksaan_lpa_lini_satu_noreg_lab` ⛔ tidak dimapping | 0/2039 | 0/4403 |  |
| 68 | BR | Pemeriksaan LPA Lini Satu / Jenis Contoh Uji | `pemeriksaan_lpa_lini_satu_jenis_contoh_uji` | 0/2039 | 0/4403 |  |
| 69 | BS | Pemeriksaan LPA Lini Satu / Tgl Contoh Uji Diterima | `pemeriksaan_lpa_lini_satu_tgl_contoh_uji_diterima` | 0/2039 | 0/4403 |  |
| 70 | BT | Pemeriksaan LPA Lini Satu / Tgl Hasil Dilaporkan | `pemeriksaan_lpa_lini_satu_tgl_hasil_dilaporkan` | 0/2039 | 0/4403 |  |
| 71 | BU | Pemeriksaan LPA Lini Satu / Hasil Pemeriksaan / Valid/Invalid | `pemeriksaan_lpa_lini_satu_hasil_pemeriksaan_validinvalid` | 0/2039 | 0/4403 |  |
| 72 | BV | Pemeriksaan LPA Lini Satu / Hasil Pemeriksaan / MTB | `pemeriksaan_lpa_lini_satu_hasil_pemeriksaan_mtb` | 0/2039 | 0/4403 |  |
| 73 | BW | Pemeriksaan LPA Lini Satu / Hasil Pemeriksaan / R | `pemeriksaan_lpa_lini_satu_hasil_pemeriksaan_r` | 0/2039 | 0/4403 |  |
| 74 | BX | Pemeriksaan LPA Lini Satu / Hasil Pemeriksaan / H Low Dose | `pemeriksaan_lpa_lini_satu_hasil_pemeriksaan_h_low_dose` | 0/2039 | 0/4403 |  |
| 75 | BY | Pemeriksaan LPA Lini Satu / Hasil Pemeriksaan / H High Dose | `pemeriksaan_lpa_lini_satu_hasil_pemeriksaan_h_high_dose` | 0/2039 | 0/4403 |  |
| 76 | BZ | Pemeriksaan LPA Lini Satu / Hasil Pemeriksaan / Eto | `pemeriksaan_lpa_lini_satu_hasil_pemeriksaan_eto` | 0/2039 | 0/4403 |  |
| 77 | CA | Pemeriksaan LPA Lini Satu / Hasil Pemeriksaan / Pto | `pemeriksaan_lpa_lini_satu_hasil_pemeriksaan_pto` | 0/2039 | 0/4403 |  |
| 78 | CB | Pemeriksaan LPA (Line Probe Assay) lini 2 / No.Reg Lab | `pemeriksaan_lpa_line_probe_assay_lini_2_noreg_lab` ⛔ tidak dimapping | 0/2039 | 0/4403 |  |
| 79 | CC | Pemeriksaan LPA (Line Probe Assay) lini 2 / Jenis Contoh Uji | `pemeriksaan_lpa_line_probe_assay_lini_2_jenis_contoh_uji` | 0/2039 | 0/4403 |  |
| 80 | CD | Pemeriksaan LPA (Line Probe Assay) lini 2 / Tgl Contoh Uji Diterima | `pemeriksaan_lpa_line_probe_assay_lini_2_tgl_contoh_uji_diterima` | 0/2039 | 0/4403 |  |
| 81 | CE | Pemeriksaan LPA (Line Probe Assay) lini 2 / Tgl Hasil Dilaporkan | `pemeriksaan_lpa_line_probe_assay_lini_2_tgl_hasil_dilaporkan` | 0/2039 | 0/4403 |  |
| 82 | CF | Pemeriksaan LPA (Line Probe Assay) lini 2 / Hasil Pemeriksaan / Invalid | `pemeriksaan_lpa_line_probe_assay_lini_2_hasil_pemeriksaan_invalid` | 0/2039 | 0/4403 |  |
| 83 | CG | Pemeriksaan LPA (Line Probe Assay) lini 2 / Hasil Pemeriksaan / MTB | `pemeriksaan_lpa_line_probe_assay_lini_2_hasil_pemeriksaan_mtb` | 0/2039 | 0/4403 |  |
| 84 | CH | Pemeriksaan LPA (Line Probe Assay) lini 2 / Hasil Pemeriksaan / FQ / Lfx | `pemeriksaan_lpa_line_probe_assay_lini_2_hasil_pemeriksaan_fq_lfx` | 0/2039 | 0/4403 |  |
| 85 | CI | Pemeriksaan LPA (Line Probe Assay) lini 2 / Hasil Pemeriksaan / FQ / Mfx | `pemeriksaan_lpa_line_probe_assay_lini_2_hasil_pemeriksaan_fq_mfx` | 0/2039 | 0/4403 |  |
| 86 | CJ | Pemeriksaan LPA (Line Probe Assay) lini 2 / Hasil Pemeriksaan / FQ / Mfx Dosis Tinggi | `pemeriksaan_lpa_line_probe_assay_lini_2_hasil_pemeriksaan_fq_mfx_dosis_tinggi` | 0/2039 | 0/4403 |  |
| 87 | CK | Pemeriksaan LPA (Line Probe Assay) lini 2 / Hasil Pemeriksaan / SLID / Km | `pemeriksaan_lpa_line_probe_assay_lini_2_hasil_pemeriksaan_slid_km` | 0/2039 | 0/4403 |  |
| 88 | CL | Pemeriksaan LPA (Line Probe Assay) lini 2 / Hasil Pemeriksaan / SLID / Amk | `pemeriksaan_lpa_line_probe_assay_lini_2_hasil_pemeriksaan_slid_amk` | 0/2039 | 0/4403 |  |
| 89 | CM | Pemeriksaan LPA (Line Probe Assay) lini 2 / Hasil Pemeriksaan / SLID / Cm | `pemeriksaan_lpa_line_probe_assay_lini_2_hasil_pemeriksaan_slid_cm` | 0/2039 | 0/4403 |  |
| 90 | CN | Pemeriksaan Biakan / No.Reg Lab | `pemeriksaan_biakan_noreg_lab` ⛔ tidak dimapping | 0/2039 | 0/4403 |  |
| 91 | CO | Pemeriksaan Biakan / Jenis Contoh Uji | `pemeriksaan_biakan_jenis_contoh_uji` | 0/2039 | 0/4403 |  |
| 92 | CP | Pemeriksaan Biakan / Tgl Contoh Uji Diterima untuk Pemeriksaan Biakan dan Uji Kepekaan | `pemeriksaan_biakan_tgl_contoh_uji_diterima_untuk_pemeriksaan_biakan_dan_uji_kepekaan` | 0/2039 | 0/4403 |  |
| 93 | CQ | Pemeriksaan Biakan / Metode Uji | `pemeriksaan_biakan_metode_uji` | 0/2039 | 0/4403 |  |
| 94 | CR | Pemeriksaan Biakan / Tgl Hasil Dilaporkan | `pemeriksaan_biakan_tgl_hasil_dilaporkan` | 0/2039 | 0/4403 |  |
| 95 | CS | Pemeriksaan Biakan / Hasil Pemeriksaan | `pemeriksaan_biakan_hasil_pemeriksaan` | 0/2039 | 0/4403 |  |
| 96 | CT | Pemeriksaan Paket Standar Uji Kepekaan / Tgl Hasil Dilaporkan | `pemeriksaan_paket_standar_uji_kepekaan_tgl_hasil_dilaporkan` | 0/2039 | 0/4403 |  |
| 97 | CU | Pemeriksaan Paket Standar Uji Kepekaan / Hasil Pemeriksaan / H Dosis Tinggi | `pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_h_dosis_tinggi` | 0/2039 | 0/4403 |  |
| 98 | CV | Pemeriksaan Paket Standar Uji Kepekaan / Hasil Pemeriksaan / H | `pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_h` | 0/2039 | 0/4403 |  |
| 99 | CW | Pemeriksaan Paket Standar Uji Kepekaan / Hasil Pemeriksaan / Km | `pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_km` | 0/2039 | 0/4403 |  |
| 100 | CX | Pemeriksaan Paket Standar Uji Kepekaan / Hasil Pemeriksaan / Cm | `pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_cm` | 0/2039 | 0/4403 |  |
| 101 | CY | Pemeriksaan Paket Standar Uji Kepekaan / Hasil Pemeriksaan / Lfx | `pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_lfx` | 0/2039 | 0/4403 |  |
| 102 | CZ | Pemeriksaan Paket Standar Uji Kepekaan / Hasil Pemeriksaan / Mfx Dosis Tinggi | `pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_mfx_dosis_tinggi` | 0/2039 | 0/4403 |  |
| 103 | DA | Pemeriksaan Paket Standar Uji Kepekaan / Hasil Pemeriksaan / Mfx | `pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_mfx` | 0/2039 | 0/4403 |  |
| 104 | DB | Pemeriksaan Paket Standar Uji Kepekaan / Hasil Pemeriksaan / ... | `pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan` | 0/2039 | 0/4403 |  |
| 105 | DC | Pemeriksaan Paket Standar Uji Kepekaan / Hasil Pemeriksaan / ... | `pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_1` | 0/2039 | 0/4403 |  |
| 106 | DD | Pemeriksaan Paket Standar Uji Kepekaan / Hasil Pemeriksaan / ... | `pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_2` | 0/2039 | 0/4403 |  |
| 107 | DE | Pemeriksaan Paket Standar Uji Kepekaan / Hasil Pemeriksaan / ... | `pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_3` | 0/2039 | 0/4403 |  |
| 108 | DF | Pemeriksaan Paket Standar Uji Kepekaan / Hasil Pemeriksaan / ... | `pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_4` | 0/2039 | 0/4403 |  |
| 109 | DG | Pemeriksaan Paket Standar Uji Kepekaan / Hasil Pemeriksaan / ... | `pemeriksaan_paket_standar_uji_kepekaan_hasil_pemeriksaan_5` | 0/2039 | 0/4403 |  |
| 110 | DH | Tanda Tangan Petugas Pemeriksa | `tanda_tangan_petugas_pemeriksa` ⛔ tidak dimapping | 0/2039 | 0/4403 | *(identitas / teks bebas, tidak ditampilkan)* |
| 111 | DI | Keterangan | `keterangan` ⛔ tidak dimapping | 0/2039 | 0/4403 |  |
| 112 | DJ | Nama Fasyankes | `nama_fasyankes` 🆕 belum ada di BQ | 2039/2039 | 4403/4403 | *(identitas / teks bebas, tidak ditampilkan)* |
| 113 | DK | Kabupaten Fasyankes | `kabupaten_fasyankes` 🆕 belum ada di BQ | 2039/2039 | 4403/4403 | `Kab. Purbalingga` (6442) |
| 114 | DL | Provinsi Fasyankes | `provinsi_fasyankes` 🆕 belum ada di BQ | 2039/2039 | 4403/4403 | `Jawa Tengah` (6442) |

Kolom BQ yang tidak ada di file mentah: `puskesmas_name`, `puskesmas_id`, `file_name`, `file_date`, `ingestion_timestamp`, `uuid`, `hash_code`
