# File mentah SITB TB 03 SO — struktur kolom

Sumber: export SITB `Kab_Purbalingga_Report_TB_03SO_spheres_Januari-Juni_2025.xlsx` (Register Pasien TBC SO, Kab. Purbalingga, Januari–Juni 2025).
File asli **tidak** disimpan di repo karena berisi data pasien. File ini berisi struktur kolom, jumlah terisi, dan nilai pilihan (kolom identitas & teks bebas tidak ditampilkan).

- `Kab_Purbalingga_Report_TB_03SO_spheres_Januari-Juni_2025.xlsx`: header sampai baris 17 (baris 17 = nomor kolom (1), (2), ...), 953 baris data.

| # | Kolom Excel | Header | Variabel BQ | Terisi (Kab_Purbalingga_Report_TB_03SO_spheres_Januari-Juni_2025.xlsx) | Nilai (frekuensi) |
|---|---|---|---|---|---|
| 1 | C | No. Urut | `no_urut` ⛔ tidak dimapping | 953/953 | `<angka>` (953) |
| 2 | D | No. Registrasi Fasyankes | `no_registrasi_fasyankes` ⛔ tidak dimapping | 953/953 | *(identitas / teks bebas, tidak ditampilkan)* |
| 3 | E | No.Registrasi TBC Kab/Kota | `noregistrasi_tbc_kabkota` ⛔ tidak dimapping | 953/953 | *(identitas / teks bebas, tidak ditampilkan)* |
| 4 | F | Bulan | `bulan` ⛔ tidak dimapping | 953/953 | `Januari` (229), `Maret` (206), `April` (189), `Februari` (176), `Mei` (147), `Juni` (6) |
| 5 | G | No. Rekam Medis | `no_rekam_medis` | 371/953 | *(identitas / teks bebas, tidak ditampilkan)* |
| 6 | H | Nomor Identitas Kependudukan (NIK) | `nomor_identitas_kependudukan_nik` | 953/953 | *(identitas / teks bebas, tidak ditampilkan)* |
| 7 | I | Nomor Register SITB | `nomor_register_sitb` | 953/953 | *(identitas / teks bebas, tidak ditampilkan)* |
| 8 | J | Nomor Register Terduga | `nomor_register_terduga` | 953/953 | *(identitas / teks bebas, tidak ditampilkan)* |
| 9 | K | Nomor Register Pasien | `nomor_register_pasien` | 953/953 | *(identitas / teks bebas, tidak ditampilkan)* |
| 10 | L | Nomor BPJS | `nomor_bpjs` | 10/953 | *(identitas / teks bebas, tidak ditampilkan)* |
| 11 | M | Status Pengobatan | `status_pengobatan` | 953/953 | `Sesuai standar` (943), `Tidak sesuai standar` (10) |
| 12 | N | Nama Lengkap Pasien | `nama_lengkap_pasien` | 953/953 | *(identitas / teks bebas, tidak ditampilkan)* |
| 13 | O | Umur (Tahun) | `umur_tahun` | 953/953 | `<angka>` (953) |
| 14 | P | Jenis Kelamin | `jenis_kelamin` | 953/953 | `L` (515), `P` (438) |
| 15 | Q | Pekerjaan/ Status | `pekerjaan_status` | 860/953 | 17 nilai berbeda (teks bebas), contoh tidak ditampilkan |
| 16 | R | Status Hamil | `status_hamil` | 328/953 | `Tidak Hamil` (317), `Tidak Tahu` (8), `Hamil` (3) |
| 17 | S | Alamat Lengkap Faskes / Provinsi | `alamat_lengkap_faskes_provinsi` | 953/953 | `Jawa Tengah` (953) |
| 18 | T | Alamat Lengkap Faskes / Kabupaten/Kota | `alamat_lengkap_faskes_kabupatenkota` | 953/953 | `Kab. Purbalingga` (953) |
| 19 | U | Alamat Lengkap Faskes / Jenis Fasyankes | `alamat_lengkap_faskes_jenis_fasyankes` | 953/953 | `Rumah Sakit` (528), `Puskesmas` (417), `Klinik` (7), `Dokter Praktik Mandiri` (1) |
| 20 | V | Alamat Lengkap Faskes / Kepemilikan Fasyankes | `alamat_lengkap_faskes_kepemilikan_fasyankes` | 953/953 | `Pemda Kab./Kota` (341), `Kemenkes` (278), `Organisasi Non Profit` (231), `Perseorangan` (99), `Perusahaan` (3), `Polri` (1) |
| 21 | W | Alamat Lengkap Faskes / Kode Fasyankes | `alamat_lengkap_faskes_kode_fasyankes` | 953/953 | `<angka>` (536), + 22 nilai lain |
| 22 | X | Alamat Lengkap Faskes / Nama Fasyankes | `alamat_lengkap_faskes_nama_fasyankes` | 953/953 | *(identitas / teks bebas, tidak ditampilkan)* |
| 23 | Y | Alamat Lengkap Pasien / Provinsi | `alamat_lengkap_pasien_provinsi` | 953/953 | `Jawa Tengah` (943), `Jawa Barat` (5), `DKI Jakarta` (2), `DI Yogyakarta` (1), `Kepulauan Riau` (1), `Kalimantan Timur` (1) |
| 24 | Z | Alamat Lengkap Pasien / Kabupaten/Kota | `alamat_lengkap_pasien_kabupatenkota` | 953/953 | 21 nilai berbeda (teks bebas), contoh tidak ditampilkan |
| 25 | AA | Alamat Lengkap Pasien / Kecamatan | `alamat_lengkap_pasien_kecamatan` | 935/953 | 49 nilai berbeda (teks bebas), contoh tidak ditampilkan |
| 26 | AB | Alamat Lengkap Pasien / Kelurahan | `alamat_lengkap_pasien_kelurahan` | 908/953 | 271 nilai berbeda (teks bebas), contoh tidak ditampilkan |
| 27 | AC | Alamat Lengkap Pasien / Alamat Lengkap | `alamat_lengkap_pasien_alamat_lengkap` | 953/953 | *(identitas / teks bebas, tidak ditampilkan)* |
| 28 | AD | Dilakukan Pemeriksaan kontak | `dilakukan_pemeriksaan_kontak` | 953/953 | `Tidak` (674), `Ya` (279) |
| 29 | AE | Dirujuk/ dikirim Oleh | `dirujuk_dikirim_oleh` | 953/953 | 45 nilai berbeda (teks bebas), contoh tidak ditampilkan |
| 30 | AF | Tipe Diagnosis TBC | `tipe_diagnosis_tbc` | 953/953 | `Terkonfirmasi bakteriologis` (502), `Terdiagnosis klinis` (451) |
| 31 | AG | Klasifikasi Berdasarkan Lokasi Anatomi | `klasifikasi_berdasarkan_lokasi_anatomi` | 953/953 | `TBC Paru` (834), `TBC Ekstraparu` (119) |
| 32 | AH | Klasifikasi Berdasarkan Riwayat Pengobatan Sebelumnya | `klasifikasi_berdasarkan_riwayat_pengobatan_sebelumnya` | 953/953 | `Baru` (755), `Tidak diketahui` (155), `Kambuh` (31), `Diobati setelah putus berobat` (7), `Diobati setelah gagal kategori 1` (5) |
| 33 | AI | Riwayat DM | `riwayat_dm` | 953/953 | `Tidak Diketahui` (705), `Tidak` (231), `Ya` (17) |
| 34 | AJ | Status HIV | `status_hiv` | 953/953 | `Tidak Diketahui` (790), `Bukan ODHIV` (154), `ODHIV` (9) |
| 35 | AK | Skoring TBC Anak (0-13) | `skoring_tbc_anak_013` | 139/953 | `<angka>` (139) |
| 36 | AL | Dilakukan Pemeriksaan Tuberkulin/IGRA | `dilakukan_pemeriksaan_tuberkulinigra` | 132/953 | `Tuberkulin` (125), `TDL` (7) |
| 37 | AM | Hasil Pemeriksaan Tuberkulin/IGRA | `hasil_pemeriksaan_tuberkulinigra` | 131/953 | `Positif (>=10mm atau >=5mm)` (98), `Negatif` (26), `TDL` (7) |
| 38 | AN | Hasil Pemeriksaan Foto Toraks | `hasil_pemeriksaan_foto_toraks` | 953/953 | `Pos` (494), `TDL` (327), `Neg` (132) |
| 39 | AO | Tanggal Mulai Pengobatan | `tanggal_mulai_pengobatan` | 953/953 | `<tanggal>` (953) |
| 40 | AP | Paduan OAT | `paduan_oat` | 953/953 | `Kategori 1` (826), `Kategori Anak` (126), `Paduan tidak standar TB SO` (1) |
| 41 | AQ | Paduan Pengobatan | `paduan_pengobatan` | 953/953 | `2(HRZE)/4(HR) - KDT Dosis Harian` (818), `2(HRZ)/4(HR)` (125), `2(HRZE)/4(HR)3` (4), `Kategori 1 + levo 4 tablet` (1), `Pro TB 3` (1), `2HRZE/4HR` (1), `RHE` (1), `INH 1X300 MG, RIFAMPICIN 1X450 MG, PIRAZINAMID 1500 MG (3X/MG SELAIN HD),ETAMBUTOL (3X/MG SELAIN HD)` (1), `INH 1X100MG,RIF 1X450 MG, ETAM 1X1500 MG` (1) |
| 42 | AR | Sumber Obat | `sumber_obat` | 953/953 | `Program TBC` (953) |
| 43 | AS | Pemeriksaan Contoh Uji / Sebelum Pengobatan / Tanggal Hasil Pemeriksaan Mikroskopis | `pemeriksaan_contoh_uji_sebelum_pengobatan_tanggal_hasil_pemeriksaan_mikroskopis` | 0/953 |  |
| 44 | AT | Pemeriksaan Contoh Uji / Sebelum Pengobatan / Hasil Mikroskopis | `pemeriksaan_contoh_uji_sebelum_pengobatan_hasil_mikroskopis` | 0/953 |  |
| 45 | AU | Pemeriksaan Contoh Uji / Sebelum Pengobatan / Tanggal Hasil Pemeriksaan Diagnosis TBC | `pemeriksaan_contoh_uji_sebelum_pengobatan_tanggal_hasil_pemeriksaan_diagnosis_tbc` | 709/953 | `<tanggal>` (709) |
| 46 | AV | Pemeriksaan Contoh Uji / Sebelum Pengobatan / Hasil Pemeriksaan Diagnosis TBC | `pemeriksaan_contoh_uji_sebelum_pengobatan_hasil_pemeriksaan_diagnosis_tbc` | 709/953 | `Rif Sen` (501), `Neg` (207), `Rif Indet` (1) |
| 47 | AW | Pemeriksaan Contoh Uji / Sebelum Pengobatan / Jenis Pemeriksaan Diagnosis | `pemeriksaan_contoh_uji_sebelum_pengobatan_jenis_pemeriksaan_diagnosis` | 709/953 | `TCM Xpert` (709) |
| 48 | AX | Pemeriksaan Contoh Uji / Hasil Pemeriksaan Xpert (TCM) - XDR / Tanggal Hasil Pemeriksaan TCM-XDR | `pemeriksaan_contoh_uji_hasil_pemeriksaan_xpert_tcm_xdr_tanggal_hasil_pemeriksaan_tcmxdr` | 8/953 | `<tanggal>` (8) |
| 49 | AY | Pemeriksaan Contoh Uji / Hasil Pemeriksaan Xpert (TCM) - XDR / Valid/Invalid/Error/No Result | `pemeriksaan_contoh_uji_hasil_pemeriksaan_xpert_tcm_xdr_validinvaliderrorno_result` | 8/953 | `Valid` (8) |
| 50 | AZ | Pemeriksaan Contoh Uji / Hasil Pemeriksaan Xpert (TCM) - XDR / MTB | `pemeriksaan_contoh_uji_hasil_pemeriksaan_xpert_tcm_xdr_mtb` | 8/953 | `D` (8) |
| 51 | BA | Pemeriksaan Contoh Uji / Hasil Pemeriksaan Xpert (TCM) - XDR / H Dosis Rendah (Low) | `pemeriksaan_contoh_uji_hasil_pemeriksaan_xpert_tcm_xdr_h_dosis_rendah_low` | 8/953 | `RND` (7), `RD` (1) |
| 52 | BB | Pemeriksaan Contoh Uji / Hasil Pemeriksaan Xpert (TCM) - XDR / H | `pemeriksaan_contoh_uji_hasil_pemeriksaan_xpert_tcm_xdr_h` | 8/953 | `RND` (8) |
| 53 | BC | Pemeriksaan Contoh Uji / Hasil Pemeriksaan Xpert (TCM) - XDR / Eto | `pemeriksaan_contoh_uji_hasil_pemeriksaan_xpert_tcm_xdr_eto` | 8/953 | `RND` (8) |
| 54 | BD | Pemeriksaan Contoh Uji / Hasil Pemeriksaan Xpert (TCM) - XDR / FQ Dosis Rendah (Low) | `pemeriksaan_contoh_uji_hasil_pemeriksaan_xpert_tcm_xdr_fq_dosis_rendah_low` | 8/953 | `RND` (7), `IDT` (1) |
| 55 | BE | Pemeriksaan Contoh Uji / Hasil Pemeriksaan Xpert (TCM) - XDR / FQ | `pemeriksaan_contoh_uji_hasil_pemeriksaan_xpert_tcm_xdr_fq` | 8/953 | `RND` (8) |
| 56 | BF | Pemeriksaan Contoh Uji / Hasil Pemeriksaan Xpert (TCM) - XDR / Amk | `pemeriksaan_contoh_uji_hasil_pemeriksaan_xpert_tcm_xdr_amk` | 8/953 | `RND` (8) |
| 57 | BG | Pemeriksaan Contoh Uji / Hasil Pemeriksaan Xpert (TCM) - XDR / Km | `pemeriksaan_contoh_uji_hasil_pemeriksaan_xpert_tcm_xdr_km` | 8/953 | `RND` (8) |
| 58 | BH | Pemeriksaan Contoh Uji / Hasil Pemeriksaan Xpert (TCM) - XDR / Cm | `pemeriksaan_contoh_uji_hasil_pemeriksaan_xpert_tcm_xdr_cm` | 8/953 | `RND` (8) |
| 59 | BI | Pemeriksaan Contoh Uji / Hasil Pemeriksaan Biakan / Tanggal Hasil Biakan | `pemeriksaan_contoh_uji_hasil_pemeriksaan_biakan_tanggal_hasil_biakan` | 0/953 |  |
| 60 | BJ | Pemeriksaan Contoh Uji / Hasil Pemeriksaan Biakan / Hasil Biakan | `pemeriksaan_contoh_uji_hasil_pemeriksaan_biakan_hasil_biakan` | 0/953 |  |
| 61 | BK | Pemeriksaan Contoh Uji / Hasil Pemeriksaan LPA (Line Probe Assay) Lini 1 / Tanggal Hasil LPA Lini 1 | `pemeriksaan_contoh_uji_hasil_pemeriksaan_lpa_line_probe_assay_lini_1_tanggal_hasil_lpa_lini_1` | 0/953 |  |
| 62 | BL | Pemeriksaan Contoh Uji / Hasil Pemeriksaan LPA (Line Probe Assay) Lini 1 / Valid/ Invalid | `pemeriksaan_contoh_uji_hasil_pemeriksaan_lpa_line_probe_assay_lini_1_valid_invalid` | 0/953 |  |
| 63 | BM | Pemeriksaan Contoh Uji / Hasil Pemeriksaan LPA (Line Probe Assay) Lini 1 / MTB | `pemeriksaan_contoh_uji_hasil_pemeriksaan_lpa_line_probe_assay_lini_1_mtb` | 0/953 |  |
| 64 | BN | Pemeriksaan Contoh Uji / Hasil Pemeriksaan LPA (Line Probe Assay) Lini 1 / R | `pemeriksaan_contoh_uji_hasil_pemeriksaan_lpa_line_probe_assay_lini_1_r` | 0/953 |  |
| 65 | BO | Pemeriksaan Contoh Uji / Hasil Pemeriksaan LPA (Line Probe Assay) Lini 1 / H | `pemeriksaan_contoh_uji_hasil_pemeriksaan_lpa_line_probe_assay_lini_1_h` | 0/953 |  |
| 66 | BP | Pemeriksaan Contoh Uji / Akhir Bulan ke 2 / No Reg Lab | `pemeriksaan_contoh_uji_akhir_bulan_ke_2_no_reg_lab` ⛔ tidak dimapping | 58/953 | `<angka>` (53), `25/1233251/1/0001` (1), `0151F` (1), `0212F` (1), `0005R` (1), `0014R` (1) |
| 67 | BQ | Pemeriksaan Contoh Uji / Akhir Bulan ke 2 / Hasil Mikroskopis | `pemeriksaan_contoh_uji_akhir_bulan_ke_2_hasil_mikroskopis` | 58/953 | `Neg` (54), `1+` (4) |
| 68 | BR | Pemeriksaan Contoh Uji / Akhir Bulan ke 3 / No Reg Lab | `pemeriksaan_contoh_uji_akhir_bulan_ke_3_no_reg_lab` ⛔ tidak dimapping | 0/953 |  |
| 69 | BS | Pemeriksaan Contoh Uji / Akhir Bulan ke 3 / Hasil Mikroskopis | `pemeriksaan_contoh_uji_akhir_bulan_ke_3_hasil_mikroskopis` | 0/953 |  |
| 70 | BT | Pemeriksaan Contoh Uji / Akhir Bulan ke 5 / No Reg Lab | `pemeriksaan_contoh_uji_akhir_bulan_ke_5_no_reg_lab` ⛔ tidak dimapping | 1/953 | `<angka>` (1) |
| 71 | BU | Pemeriksaan Contoh Uji / Akhir Bulan ke 5 / Hasil Mikroskopis | `pemeriksaan_contoh_uji_akhir_bulan_ke_5_hasil_mikroskopis` | 1/953 | `Neg` (1) |
| 72 | BV | Pemeriksaan Contoh Uji / Akhir Pengobatan / No Reg Lab | `pemeriksaan_contoh_uji_akhir_pengobatan_no_reg_lab` ⛔ tidak dimapping | 0/953 |  |
| 73 | BW | Pemeriksaan Contoh Uji / Akhir Pengobatan / Hasil Mikroskopis | `pemeriksaan_contoh_uji_akhir_pengobatan_hasil_mikroskopis` | 0/953 |  |
| 74 | BX | Hasil Akhir Pengobatan / Tanggal (hh/bb/tttt) | `hasil_akhir_pengobatan_tanggal_hhbbtttt` | 32/953 | `<tanggal>` (32) |
| 75 | BY | Hasil Akhir Pengobatan / Hasil | `hasil_akhir_pengobatan_hasil` | 32/953 | `Tidak dievaluasi/pindah` (18), `Meninggal` (13), `Gagal` (1) |
| 76 | BZ | Kolaborasi Kegiatan TBC-HIV / Layanan Tes dan Konseling HIV / Tanggal Dianjurkan | `kolaborasi_kegiatan_tbchiv_layanan_tes_dan_konseling_hiv_tanggal_dianjurkan` | 512/953 | `<tanggal>` (512) |
| 77 | CA | Kolaborasi Kegiatan TBC-HIV / Layanan Tes dan Konseling HIV / Tanggal Tes HIV | `kolaborasi_kegiatan_tbchiv_layanan_tes_dan_konseling_hiv_tanggal_tes_hiv` | 504/953 | `<tanggal>` (504) |
| 78 | CB | Kolaborasi Kegiatan TBC-HIV / Layanan Tes dan Konseling HIV / Hasil Tes | `kolaborasi_kegiatan_tbchiv_layanan_tes_dan_konseling_hiv_hasil_tes` | 512/953 | `Bukan ODHIV` (496), `Tidak Diketahui` (8), `ODHIV` (8) |
| 79 | CC | Kolaborasi Kegiatan TBC-HIV / Layanan PDP / Kotrimoksasol | `kolaborasi_kegiatan_tbchiv_layanan_pdp_kotrimoksasol` | 22/953 | `Tidak` (21), `Ya` (1) |
| 80 | CD | Kolaborasi Kegiatan TBC-HIV / Layanan PDP / ART | `kolaborasi_kegiatan_tbchiv_layanan_pdp_art` | 22/953 | `Tidak` (20), `Ya` (2) |
| 81 | CE | Kegiatan TBC-DM / DM | `kegiatan_tbcdm_dm` | 480/953 | `Negatif` (451), `Positif` (29) |
| 82 | CF | Kegiatan TBC-DM / Terapi DM | `kegiatan_tbcdm_terapi_dm` | 25/953 | `OHO` (23), `Inj Insulin` (2) |
| 83 | CG | Dipindah ke TBC.03 RO | `dipindah_ke_tbc03_ro` | 1/953 | `Ya` (1) |
| 84 | CH | Keterangan | `keterangan` | 2/953 | `Perubahan Diagnosis menjadi TB RO` (2) |

Kolom BQ yang tidak ada di file mentah: `puskesmas_name`, `puskesmas_id`, `file_name`, `file_date`, `ingestion_timestamp`, `uuid`, `hash_code`
