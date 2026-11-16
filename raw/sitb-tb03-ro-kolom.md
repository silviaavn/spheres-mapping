# File mentah SITB TB 03 RO — struktur kolom

Sumber: export SITB `Kab_Purbalingga_Report_TB_03RO_spheres_Januari-Juni_2025.xlsx` (Register Pasien TBC RO, Kab. Purbalingga, Januari–Juni 2025).
File asli **tidak** disimpan di repo karena berisi data pasien. File ini berisi struktur kolom, jumlah terisi, dan nilai pilihan (kolom identitas & teks bebas tidak ditampilkan).

- `Kab_Purbalingga_Report_TB_03RO_spheres_Januari-Juni_2025.xlsx`: header sampai baris 17 (baris 17 = nomor kolom (1), (2), ...), 14 baris data.

| # | Kolom Excel | Header | Variabel BQ | Terisi (Kab_Purbalingga_Report_TB_03RO_spheres_Januari-Juni_2025.xlsx) | Nilai (frekuensi) |
|---|---|---|---|---|---|
| 1 | C | No. Urut | `no_urut` ⛔ tidak dimapping | 14/14 | `<angka>` (14) |
| 2 | D | No. Registrasi Fasyankes | `no_registrasi_fasyankes` ⛔ tidak dimapping | 14/14 | *(identitas / teks bebas, tidak ditampilkan)* |
| 3 | E | No. Registrasi TBC Kab/Kota | `no_registrasi_tbc_kabkota` ⛔ tidak dimapping | 14/14 | *(identitas / teks bebas, tidak ditampilkan)* |
| 4 | F | Tgl Pengisian Data Dasar Terduga TBC RO | `tgl_pengisian_data_dasar_terduga_tbc_ro` | 14/14 | `<tanggal>` (14) |
| 5 | G | No. Rekam Medis | `no_rekam_medis` | 11/14 | *(identitas / teks bebas, tidak ditampilkan)* |
| 6 | H | Tgl Mulai Pengobatan | `tgl_mulai_pengobatan` | 14/14 | `<tanggal>` (14) |
| 7 | I | Bulan | `bulan` ⛔ tidak dimapping | 14/14 | `Februari` (6), `September` (3), `Juni` (2), `Agustus` (2), `Juli` (1) |
| 8 | J | Nomor Identitas Kependudukan (NIK) | `nomor_identitas_kependudukan_nik` | 14/14 | *(identitas / teks bebas, tidak ditampilkan)* |
| 9 | K | Nomor Register SITB | `nomor_register_sitb` | 14/14 | *(identitas / teks bebas, tidak ditampilkan)* |
| 10 | L | Nomor Register Terduga | `nomor_register_terduga` | 14/14 | *(identitas / teks bebas, tidak ditampilkan)* |
| 11 | M | Nomor Register Pasien | `nomor_register_pasien` | 14/14 | *(identitas / teks bebas, tidak ditampilkan)* |
| 12 | N | Nomor BPJS | `nomor_bpjs` | 0/14 | *(identitas / teks bebas, tidak ditampilkan)* |
| 13 | O | Nama Lengkap Pasien | `nama_lengkap_pasien` | 14/14 | *(identitas / teks bebas, tidak ditampilkan)* |
| 14 | P | Umur (Tahun) | `umur_tahun` | 14/14 | `<angka>` (14) |
| 15 | Q | Jenis Kelamin | `jenis_kelamin` | 14/14 | `L` (13), `P` (1) |
| 16 | R | Pekerjaan/ Status | `pekerjaan_status` | 12/14 | `Buruh` (5), `Wiraswasta` (3), `Tidak Bekerja` (2), `Lain-lain:` (1), `IRT` (1) |
| 17 | S | Status Hamil | `status_hamil` | 1/14 | `Tidak Hamil` (1) |
| 18 | T | Alamat Lengkap Faskes / Provinsi | `alamat_lengkap_faskes_provinsi` | 14/14 | `Jawa Tengah` (14) |
| 19 | U | Alamat Lengkap Faskes / Kabupaten/Kota | `alamat_lengkap_faskes_kabupatenkota` | 14/14 | `Kab. Purbalingga` (14) |
| 20 | V | Alamat Lengkap Faskes / Jenis Fasyankes | `alamat_lengkap_faskes_jenis_fasyankes` | 14/14 | `Rumah Sakit` (12), `Puskesmas` (2) |
| 21 | W | Alamat Lengkap Faskes / Kepemilikan Fasyankes | `alamat_lengkap_faskes_kepemilikan_fasyankes` | 14/14 | `Pemda Kab./Kota` (13), `Organisasi Non Profit` (1) |
| 22 | X | Alamat Lengkap Faskes / Kode Fasyankes | `alamat_lengkap_faskes_kode_fasyankes` | 14/14 | `<angka>` (12), `P3303160101` (2) |
| 23 | Y | Alamat Lengkap Faskes / Nama Fasyankes | `alamat_lengkap_faskes_nama_fasyankes` | 14/14 | *(identitas / teks bebas, tidak ditampilkan)* |
| 24 | Z | Alamat Lengkap Pasien / Provinsi | `alamat_lengkap_pasien_provinsi` | 14/14 | `Jawa Tengah` (14) |
| 25 | AA | Alamat Lengkap Pasien / Kabupaten/Kota | `alamat_lengkap_pasien_kabupatenkota` | 14/14 | `Kab. Purbalingga` (14) |
| 26 | AB | Alamat Lengkap Pasien / Kecamatan | `alamat_lengkap_pasien_kecamatan` | 14/14 | `Rembang` (4), `Padamara` (2), `Bojongsari` (2), `Kutasari` (2), `Kejobong` (1), `Karangmoncol` (1), `Kemangkon` (1), `Bukateja` (1) |
| 27 | AC | Alamat Lengkap Pasien / Kelurahan | `alamat_lengkap_pasien_kelurahan` | 13/14 | `Bantarbarang` (2), `MIPIRAN` (2), `PAGEDANGAN` (2), `SUMINGKIR` (1), `Tamansari` (1), `SENON` (1), `KUTASARI` (1), `KARANGCENGIS` (1), `Sumampir` (1), `Karangbawang` (1) |
| 28 | AD | Alamat Lengkap Pasien / Alamat Lengkap | `alamat_lengkap_pasien_alamat_lengkap` | 14/14 | *(identitas / teks bebas, tidak ditampilkan)* |
| 29 | AE | Dilakukan Pemeriksaan Kontak | `dilakukan_pemeriksaan_kontak` | 14/14 | `Ya` (9), `Tidak` (5) |
| 30 | AF | Dirujuk/ dikirim Oleh | `dirujuk_dikirim_oleh` | 14/14 | `Fasyankes: RS PKU Muhammadiyah Purbalingga` (3), `Fasyankes: Puskesmas Rembang` (2), `Fasyankes: Puskesmas Padamara` (2), `Datang Sendiri` (2), `Fasyankes: Puskesmas Kejobong` (1), `Fasyankes: Puskesmas Kutasari` (1), `Fasyankes: Klinik Abmi Medika` (1), `Fasyankes: Puskesmas Kemangkon` (1), `Fasyankes: RS Umum Siaga Medika Purbalingga` (1) |
| 31 | AG | Nama Fasyankes Satelit TBC RO (Lanjutan Pengobatan) | `nama_fasyankes_satelit_tbc_ro_lanjutan_pengobatan` | 13/14 | *(identitas / teks bebas, tidak ditampilkan)* |
| 32 | AH | Klasifikasi Berdasarkan Lokasi Anatomi | `klasifikasi_berdasarkan_lokasi_anatomi` | 14/14 | `TBC Paru` (14) |
| 33 | AI | Klasifikasi Berdasarkan Riwayat Pengobatan Sebelumnya | `klasifikasi_berdasarkan_riwayat_pengobatan_sebelumnya` | 12/14 | `Baru` (6), `Kambuh` (5), `Diobati setelah putus berobat` (1) |
| 34 | AJ | Riwayat Pengobatan TBC Sebelumnya | `riwayat_pengobatan_tbc_sebelumnya` | 6/14 | `Pasien TB kasus kambuh setelah pengobatan OAT kategori 1 ataupun kategori 2` (3), `Pasien TB kasus kambuh (relaps), kategori 1 dan kategori 2` (1), `Pasien TB yang kembali setelah putus berobat` (1), `Pasien TB RO kasus kambuh` (1) |
| 35 | AK | Riwayat DM | `riwayat_dm` | 14/14 | `Tidak Diketahui` (8), `Tidak` (5), `Ya` (1) |
| 36 | AL | Status HIV | `status_hiv` | 14/14 | `Tidak Diketahui` (12), `Bukan ODHIV` (2) |
| 37 | AM | Dilakukan Pemeriksaan Tuberkulin/IGRA | `dilakukan_pemeriksaan_tuberkulinigra` | 0/14 |  |
| 38 | AN | Hasil Pemeriksaan Tuberkulin/IGRA | `hasil_pemeriksaan_tuberkulinigra` | 0/14 |  |
| 39 | AO | Hasil Foto Toraks | `hasil_foto_toraks` | 6/14 | `Kavitas` (6) |
| 40 | AP | Paduan Pengobatan | `paduan_pengobatan` | 14/14 | `Bdq Lzd Mfx Pa` (12), `Lfx RHZE` (2) |
| 41 | AQ | Paduan OAT | `paduan_oat` | 14/14 | `Paduan Jangka Pendek` (12), `Paduan Monoresistan INH` (2) |
| 42 | AR | Tanggal Pengambilan Dahak untuk Uji Kepekaan (hh/bb/tttt) | `tanggal_pengambilan_dahak_untuk_uji_kepekaan_hhbbtttt` | 7/14 | `<tanggal>` (7) |
| 43 | AS | Tanggal Hasil Uji Kepekaan Keluar (hh/bb/tttt) | `tanggal_hasil_uji_kepekaan_keluar_hhbbtttt` | 7/14 | `<tanggal>` (7) |
| 44 | AT | Tanggal Hasil Pemeriksaan Diagnosis TBC | `tanggal_hasil_pemeriksaan_diagnosis_tbc` | 14/14 | `<tanggal>` (14) |
| 45 | AU | Hasil Pemeriksaan Diagnosis TBC | `hasil_pemeriksaan_diagnosis_tbc` | 14/14 | `Rif Res` (12), `Rif Sen` (2) |
| 46 | AV | Jenis Pemeriksaan Diagnosis | `jenis_pemeriksaan_diagnosis` | 14/14 | `TCM Xpert` (14) |
| 47 | AW | Tanggal Hasil Pemeriksaan TCM-XDR | `tanggal_hasil_pemeriksaan_tcmxdr` | 14/14 | `<tanggal>` (14) |
| 48 | AX | Hasil Pemeriksaan Xpert (TCM) - XDR / Valid/ Invalid/ No Result/ Error | `hasil_pemeriksaan_xpert_tcm_xdr_valid_invalid_no_result_error` | 14/14 | `Valid` (14) |
| 49 | AY | Hasil Pemeriksaan Xpert (TCM) - XDR / MTB | `hasil_pemeriksaan_xpert_tcm_xdr_mtb` | 14/14 | `D` (10), `RD` (2), `ND` (2) |
| 50 | AZ | Hasil Pemeriksaan Xpert (TCM) - XDR / H Dosis Rendah (Low) | `hasil_pemeriksaan_xpert_tcm_xdr_h_dosis_rendah_low` | 12/14 | `RD` (8), `RND` (4) |
| 51 | BA | Hasil Pemeriksaan Xpert (TCM) - XDR / H | `hasil_pemeriksaan_xpert_tcm_xdr_h` | 12/14 | `RND` (10), `RD` (2) |
| 52 | BB | Hasil Pemeriksaan Xpert (TCM) - XDR / FQ Dosis Rendah (Low) | `hasil_pemeriksaan_xpert_tcm_xdr_fq_dosis_rendah_low` | 12/14 | `RND` (11), `RD` (1) |
| 53 | BC | Hasil Pemeriksaan Xpert (TCM) - XDR / FQ | `hasil_pemeriksaan_xpert_tcm_xdr_fq` | 12/14 | `RND` (11), `RD` (1) |
| 54 | BD | Hasil Pemeriksaan Xpert (TCM) - XDR / Amk | `hasil_pemeriksaan_xpert_tcm_xdr_amk` | 12/14 | `RND` (12) |
| 55 | BE | Hasil Pemeriksaan Xpert (TCM) - XDR / Km | `hasil_pemeriksaan_xpert_tcm_xdr_km` | 12/14 | `RND` (12) |
| 56 | BF | Hasil Pemeriksaan Xpert (TCM) - XDR / Cm | `hasil_pemeriksaan_xpert_tcm_xdr_cm` | 12/14 | `RND` (12) |
| 57 | BG | Hasil Pemeriksaan Xpert (TCM) - XDR / Eto | `hasil_pemeriksaan_xpert_tcm_xdr_eto` | 12/14 | `RND` (12) |
| 58 | BH | Hasil Pemeriksaan LPA (Line Probe Assay) Lini 1 / Valid/ Invalid | `hasil_pemeriksaan_lpa_line_probe_assay_lini_1_valid_invalid` | 0/14 |  |
| 59 | BI | Hasil Pemeriksaan LPA (Line Probe Assay) Lini 1 / MTB | `hasil_pemeriksaan_lpa_line_probe_assay_lini_1_mtb` | 0/14 |  |
| 60 | BJ | Hasil Pemeriksaan LPA (Line Probe Assay) Lini 1 / R | `hasil_pemeriksaan_lpa_line_probe_assay_lini_1_r` | 0/14 |  |
| 61 | BK | Hasil Pemeriksaan LPA (Line Probe Assay) Lini 1 / H | `hasil_pemeriksaan_lpa_line_probe_assay_lini_1_h` | 0/14 |  |
| 62 | BL | Hasil Pemeriksaan LPA lini 2 / Valid/ Invalid | `hasil_pemeriksaan_lpa_lini_2_valid_invalid` | 0/14 |  |
| 63 | BM | Hasil Pemeriksaan LPA lini 2 / MTB | `hasil_pemeriksaan_lpa_lini_2_mtb` | 0/14 |  |
| 64 | BN | Hasil Pemeriksaan LPA lini 2 / FQ / Lfx | `hasil_pemeriksaan_lpa_lini_2_fq_lfx` | 0/14 |  |
| 65 | BO | Hasil Pemeriksaan LPA lini 2 / FQ / Mfx | `hasil_pemeriksaan_lpa_lini_2_fq_mfx` | 0/14 |  |
| 66 | BP | Hasil Pemeriksaan LPA lini 2 / FQ / Mfx DT | `hasil_pemeriksaan_lpa_lini_2_fq_mfx_dt` | 0/14 |  |
| 67 | BQ | Hasil Pemeriksaan LPA lini 2 / SLID / Km | `hasil_pemeriksaan_lpa_lini_2_slid_km` | 0/14 |  |
| 68 | BR | Hasil Pemeriksaan LPA lini 2 / SLID / Amk | `hasil_pemeriksaan_lpa_lini_2_slid_amk` | 0/14 |  |
| 69 | BS | Hasil Pemeriksaan LPA lini 2 / SLID / Cm | `hasil_pemeriksaan_lpa_lini_2_slid_cm` | 0/14 |  |
| 70 | BT | Hasil Pemeriksaan Paket Standar Uji Kepekaan / H Dosis Tinggi | `hasil_pemeriksaan_paket_standar_uji_kepekaan_h_dosis_tinggi` | 7/14 | `R` (3), `S` (3), `TDL` (1) |
| 71 | BU | Hasil Pemeriksaan Paket Standar Uji Kepekaan / H | `hasil_pemeriksaan_paket_standar_uji_kepekaan_h` | 7/14 | `R` (3), `S` (3), `TDL` (1) |
| 72 | BV | Hasil Pemeriksaan Paket Standar Uji Kepekaan / Km | `hasil_pemeriksaan_paket_standar_uji_kepekaan_km` | 7/14 | `TDL` (7) |
| 73 | BW | Hasil Pemeriksaan Paket Standar Uji Kepekaan / Cm | `hasil_pemeriksaan_paket_standar_uji_kepekaan_cm` | 7/14 | `TDL` (7) |
| 74 | BX | Hasil Pemeriksaan Paket Standar Uji Kepekaan / Lfx | `hasil_pemeriksaan_paket_standar_uji_kepekaan_lfx` | 7/14 | `S` (6), `TDL` (1) |
| 75 | BY | Hasil Pemeriksaan Paket Standar Uji Kepekaan / Mfx Dosis Tinggi | `hasil_pemeriksaan_paket_standar_uji_kepekaan_mfx_dosis_tinggi` | 7/14 | `TDL` (7) |
| 76 | BZ | Hasil Pemeriksaan Paket Standar Uji Kepekaan / Mfx | `hasil_pemeriksaan_paket_standar_uji_kepekaan_mfx` | 7/14 | `S` (6), `TDL` (1) |
| 77 | CA | Hasil Pemeriksaan Paket Standar Uji Kepekaan / ... | `hasil_pemeriksaan_paket_standar_uji_kepekaan` | 7/14 | `Bdq= S` (7) |
| 78 | CB | Hasil Pemeriksaan Paket Standar Uji Kepekaan / ... | `hasil_pemeriksaan_paket_standar_uji_kepekaan_1` | 7/14 | `Cfz= S` (7) |
| 79 | CC | Hasil Pemeriksaan Paket Standar Uji Kepekaan / ... | `hasil_pemeriksaan_paket_standar_uji_kepekaan_2` | 7/14 | `Lzd= S` (7) |
| 80 | CD | Hasil Pemeriksaan Paket Standar Uji Kepekaan / ... | `hasil_pemeriksaan_paket_standar_uji_kepekaan_3` | 4/14 | `Z= TDL` (4) |
| 81 | CE | Hasil Pemeriksaan Paket Standar Uji Kepekaan / ... | `hasil_pemeriksaan_paket_standar_uji_kepekaan_4` | 0/14 |  |
| 82 | CF | Hasil Pemeriksaan Paket Standar Uji Kepekaan / ... | `hasil_pemeriksaan_paket_standar_uji_kepekaan_5` | 0/14 |  |
| 83 | CG | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 1 / BTA | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__1_bta` | 9/14 | `NEG` (9) |
| 84 | CH | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 1 / B | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__1_b` | 5/14 | `Pos` (5) |
| 85 | CI | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 2 / BTA | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__2_bta` | 7/14 | `NEG` (4), `<angka>` (2), `Neg` (1) |
| 86 | CJ | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 2 / B | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__2_b` | 4/14 | `Pos` (4) |
| 87 | CK | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 3 / BTA | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__3_bta` | 5/14 | `NEG` (3), `1+` (2) |
| 88 | CL | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 3 / B | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__3_b` | 2/14 | `Neg` (2) |
| 89 | CM | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 4 / BTA | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__4_bta` | 2/14 | `NEG` (2) |
| 90 | CN | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 4 / B | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__4_b` | 2/14 | `Neg` (2) |
| 91 | CO | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 4 / BTA 2 | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__4_bta_2` | 0/14 |  |
| 92 | CP | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 4 / B 2 | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__4_b_2` | 0/14 |  |
| 93 | CQ | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 5 / BTA | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__5_bta` | 3/14 | `NEG` (2), `Neg` (1) |
| 94 | CR | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 5 / B | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__5_b` | 2/14 | `Neg` (2) |
| 95 | CS | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 5 / BTA2 | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__5_bta2` | 1/14 | `Neg` (1) |
| 96 | CT | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 5 / B2 | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__5_b2` | 0/14 |  |
| 97 | CU | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 6 / BTA | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__6_bta` | 1/14 | `NEG` (1) |
| 98 | CV | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 6 / B | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__6_b` | 0/14 |  |
| 99 | CW | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 6 / BTA2 | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__6_bta2` | 0/14 |  |
| 100 | CX | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 6 / B2 | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__6_b2` | 0/14 |  |
| 101 | CY | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 7 / BTA | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__7_bta` | 0/14 |  |
| 102 | CZ | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 7 / B | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__7_b` | 0/14 |  |
| 103 | DA | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 8 / BTA | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__8_bta` | 0/14 |  |
| 104 | DB | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 8 / B | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__8_b` | 0/14 |  |
| 105 | DC | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 9 / BTA | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__9_bta` | 0/14 |  |
| 106 | DD | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 9 / B | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__9_b` | 0/14 |  |
| 107 | DE | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 10 / BTA | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__10_bta` | 0/14 |  |
| 108 | DF | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 10 / B | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__10_b` | 0/14 |  |
| 109 | DG | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 11 / BTA | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__11_bta` | 0/14 |  |
| 110 | DH | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 11 / B | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__11_b` | 0/14 |  |
| 111 | DI | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 12 / BTA | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__12_bta` | 0/14 |  |
| 112 | DJ | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 12 / B | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__12_b` | 0/14 |  |
| 113 | DK | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 13 / BTA | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__13_bta` | 0/14 |  |
| 114 | DL | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 13 / B | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__13_b` | 0/14 |  |
| 115 | DM | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 14 / BTA | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__14_bta` | 0/14 |  |
| 116 | DN | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 14 / B | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__14_b` | 0/14 |  |
| 117 | DO | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 15 / BTA | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__15_bta` | 0/14 |  |
| 118 | DP | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 15 / B | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__15_b` | 0/14 |  |
| 119 | DQ | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 16 / BTA | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__16_bta` | 0/14 |  |
| 120 | DR | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 16 / B | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__16_b` | 0/14 |  |
| 121 | DS | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 17 / BTA | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__17_bta` | 0/14 |  |
| 122 | DT | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 17 / B | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__17_b` | 0/14 |  |
| 123 | DU | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 18 / BTA | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__18_bta` | 0/14 |  |
| 124 | DV | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 18 / B | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__18_b` | 0/14 |  |
| 125 | DW | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 19 / BTA | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__19_bta` | 0/14 |  |
| 126 | DX | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 19 / B | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__19_b` | 0/14 |  |
| 127 | DY | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 20 / BTA | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__20_bta` | 0/14 |  |
| 128 | DZ | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 20 / B | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__20_b` | 0/14 |  |
| 129 | EA | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 21 / BTA | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__21_bta` | 0/14 |  |
| 130 | EB | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 21 / B | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__21_b` | 0/14 |  |
| 131 | EC | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 22 / BTA | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__22_bta` | 0/14 |  |
| 132 | ED | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 22 / B | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__22_b` | 0/14 |  |
| 133 | EE | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 23 / BTA | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__23_bta` | 0/14 |  |
| 134 | EF | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 23 / B | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__23_b` | 0/14 |  |
| 135 | EG | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 24 / BTA | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__24_bta` | 0/14 |  |
| 136 | EH | Pemeriksaan Dahak Follow Up BTA dan Biakan Pasien TBC RO Bulan ke - ... / 24 / B | `pemeriksaan_dahak_follow_up_bta_dan_biakan_pasien_tbc_ro_bulan_ke__24_b` | 0/14 |  |
| 137 | EI | Hasil Akhir Pengobatan / Tanggal (HH/BB/TTTT) | `hasil_akhir_pengobatan_tanggal_hhbbtttt` | 2/14 | `<tanggal>` (2) |
| 138 | EJ | Hasil Akhir Pengobatan / Hasil | `hasil_akhir_pengobatan_hasil` | 1/14 | `Pengobatan Lengkap` (1) |
| 139 | EK | Kegiatan TBC-HIV / Hasil Tes HIV | `kegiatan_tbchiv_hasil_tes_hiv` | 6/14 | `Bukan ODHIV` (6) |
| 140 | EL | Kegiatan TBC-HIV / Kotrimoksasol | `kegiatan_tbchiv_kotrimoksasol` | 0/14 |  |
| 141 | EM | Kegiatan TBC-HIV / ART | `kegiatan_tbchiv_art` | 0/14 |  |
| 142 | EN | Kegiatan TBC-DM / DM | `kegiatan_tbcdm_dm` | 14/14 | `Tidak` (13), `Ya` (1) |
| 143 | EO | Kegiatan TBC-DM / Terapi DM | `kegiatan_tbcdm_terapi_dm` | 0/14 |  |
| 144 | EP | Keterangan | `keterangan` | 0/14 |  |

Kolom BQ yang tidak ada di file mentah: `puskesmas_name`, `puskesmas_id`, `file_name`, `file_date`, `ingestion_timestamp`, `uuid`, `hash_code`
