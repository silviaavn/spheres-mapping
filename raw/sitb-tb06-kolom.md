# File mentah SITB TB 06 — struktur kolom

Sumber: export SITB `Kab_Purbalingga_Report_TB_06_spheres_Januari-Mei_2025.xlsx` (Register Terduga TBC, Kab. Purbalingga, Januari–Mei 2025, header bertingkat). File `TB_06SO` dan `TB_06RO` di folder Drive yang sama berisi format yang sama tanpa kolom AC "Klasifikasi Terduga TBC".
File asli **tidak** disimpan di repo karena berisi data pasien. File ini berisi struktur kolom, jumlah terisi, dan nilai pilihan (kolom identitas & teks bebas tidak ditampilkan).

- `Kab_Purbalingga_Report_TB_06_spheres_Januari-Mei_2025.xlsx`: header sampai baris 16 (baris 16 = nomor kolom (1), (2), ...), 6201 baris data.

| # | Kolom Excel | Header | Variabel BQ | Terisi (Kab_Purbalingga_Report_TB_06_spheres_Januari-Mei_2025.xlsx) | Nilai (frekuensi) |
|---|---|---|---|---|---|
| 1 | C | No. Urut | `no_urut` ⛔ tidak dimapping | 6201/6201 | `<angka>` (6201) |
| 2 | D | No. Identitas Sediaan | `no_identitas_sediaan` | 6201/6201 | *(identitas / teks bebas, tidak ditampilkan)* |
| 3 | E | No. Rekam Medis | `no_rekam_medis` | 1097/6201 | *(identitas / teks bebas, tidak ditampilkan)* |
| 4 | F | Tanggal Didaftar | `tanggal_didaftar` | 6201/6201 | `<tanggal>` (6201) |
| 5 | G | Bulan | `bulan` ⛔ tidak dimapping | 6201/6201 | `Maret` (1318), `Februari` (1295), `Januari` (1256), `April` (1173), `Mei` (1159) |
| 6 | H | NIK (Nomor Identitas Kependudukan) | `nik_nomor_identitas_kependudukan` | 6201/6201 | *(identitas / teks bebas, tidak ditampilkan)* |
| 7 | I | No Register SITB | `no_register_sitb` | 6201/6201 | *(identitas / teks bebas, tidak ditampilkan)* |
| 8 | J | No Register Terduga | `no_register_terduga` | 6201/6201 | *(identitas / teks bebas, tidak ditampilkan)* |
| 9 | K | No. BPJS | `no_bpjs` ⛔ tidak dimapping | 113/6201 | *(identitas / teks bebas, tidak ditampilkan)* |
| 10 | L | Status Diagnosis | `status_diagnosis` ⛔ tidak dimapping | 5424/6201 | `Sesuai standar` (5387), `Tidak sesuai standar` (37) |
| 11 | M | Nama Lengkap Terduga TBC | `nama_lengkap_terduga_tbc` | 6201/6201 | *(identitas / teks bebas, tidak ditampilkan)* |
| 12 | N | Umur (Tahun) | `umur_tahun` | 6201/6201 | `<angka>` (6201) |
| 13 | O | Jenis Kelamin | `jenis_kelamin` | 6201/6201 | `P` (3507), `L` (2694) |
| 14 | P | Alamat Lengkap Faskes / Provinsi | `alamat_lengkap_faskes_provinsi` | 6201/6201 | `Jawa Tengah` (6201) |
| 15 | Q | Alamat Lengkap Faskes / Kabupaten/Kota | `alamat_lengkap_faskes_kabupatenkota` | 6201/6201 | `Kab. Purbalingga` (6201) |
| 16 | R | Alamat Lengkap Faskes / Jenis Fasyankes | `alamat_lengkap_faskes_jenis_fasyankes` | 6201/6201 | `Puskesmas` (4632), `Rumah Sakit` (1464), `Klinik` (101), `Dokter Praktik Mandiri` (4) |
| 17 | S | Alamat Lengkap Faskes / Kepemilikan Fasyankes | `alamat_lengkap_faskes_kepemilikan_fasyankes` | 6201/6201 | `Kemenkes` (3507), `Pemda Kab./Kota` (1788), `Organisasi Non Profit` (512), `Perseorangan` (352), `Perusahaan` (35), `Polri` (7) |
| 18 | T | Alamat Lengkap Faskes / Kode Fasyankes | `alamat_lengkap_faskes_kode_fasyankes` | 6201/6201 | `<angka>` (1569), + 22 nilai lain |
| 19 | U | Alamat Lengkap Faskes / Nama Fasyankes | `alamat_lengkap_faskes_nama_fasyankes` | 6201/6201 | *(identitas / teks bebas, tidak ditampilkan)* |
| 20 | V | Alamat Lengkap Terduga TBC / Provinsi | `alamat_lengkap_terduga_tbc_provinsi` | 6201/6201 | `Jawa Tengah` (6160), `DKI Jakarta` (13), `Jawa Barat` (12), `Banten` (7), `Kepulauan Riau` (2), `Lampung` (2), `Riau` (2), `Papua Barat` (1), `Jawa Timur` (1), `DI Yogyakarta` (1) |
| 21 | W | Alamat Lengkap Terduga TBC / Kabupaten/Kota | `alamat_lengkap_terduga_tbc_kabupatenkota` | 6200/6201 | 41 nilai berbeda (teks bebas), contoh tidak ditampilkan |
| 22 | X | Alamat Lengkap Terduga TBC / Kecamatan | `alamat_lengkap_terduga_tbc_kecamatan` | 6135/6201 | 100 nilai berbeda (teks bebas), contoh tidak ditampilkan |
| 23 | Y | Alamat Lengkap Terduga TBC / Kelurahan | `alamat_lengkap_terduga_tbc_kelurahan` | 6010/6201 | 365 nilai berbeda (teks bebas), contoh tidak ditampilkan |
| 24 | Z | Alamat Lengkap Terduga TBC / Alamat Lengkap | `alamat_lengkap_terduga_tbc_alamat_lengkap` | 6201/6201 | *(identitas / teks bebas, tidak ditampilkan)* |
| 25 | AA | Dirujuk/Dikirim Oleh | `dirujukdikirim_oleh` | 6201/6201 | 19 nilai berbeda (teks bebas), contoh tidak ditampilkan |
| 26 | AB | Klasifikasi Berdasarkan Riwayat Pengobatan Sebelumnya | `klasifikasi_berdasarkan_riwayat_pengobatan_sebelumnya` | 6200/6201 | `Baru` (5079), `Tidak diketahui` (959), `Kambuh` (129), `Diobati setelah gagal kategori 1` (18), `Diobati setelah putus berobat` (15) |
| 27 | AC | Klasifikasi Terduga TBC | `klasifikasi_terduga_tbc` 🆕 belum ada di BQ | 11/6201 | `Terduga TBC SO` (10), `Terduga TBC RO` (1) |
| 28 | AD | Kriteria Terduga TBC RO | `kriteria_terduga_tbc_ro` | 161/6201 | `Pasien TB RO kasus kambuh` (52), `Pasien TB kasus kambuh setelah pengobatan OAT kategori 1 ataupun kategori 2` (45), `Pasien TB kasus kambuh (relaps), kategori 1 dan kategori 2` (24), `Pasien TB yang kembali setelah putus berobat` (15), `Pasien TB gagal pengobatan dengan OAT kategori 1` (11), `Pasien TB RO kasus kambuh (relaps)` (6), `Pasien TB pengobatan kategori 1 yang tidak konversi` (5), `Pasien TB pengobatan kategori 1 yang gagal` (2), `Pasien TB RO yang kembali setelahÂ putusÂ berobat` (1) |
| 29 | AE | Lokasi Anatomi Penyakit | `lokasi_anatomi_penyakit` | 6150/6201 | `TBC Paru` (6026), `TBC Ekstraparu` (124) |
| 30 | AF | Total Skoring TBC Anak | `total_skoring_tbc_anak` | 262/6201 | `<angka>` (262) |
| 31 | AG | Hasil Pemeriksaan Foto Toraks | `hasil_pemeriksaan_foto_toraks` | 5425/6201 | `TDL` (3852), `Neg` (1048), `Pos` (525) |
| 32 | AH | Dilakukan Pemeriksaan Tuberkulin/IGRA | `dilakukan_pemeriksaan_tuberkulinigra` | 380/6201 | `Tuberkulin` (223), `TDL` (141), `IGRA` (16) |
| 33 | AI | Hasil Pemeriksaan Tuberkulin/IGRA | `hasil_pemeriksaan_tuberkulinigra` | 379/6201 | `TDL` (141), `Negatif` (135), `Positif (>=10mm atau >=5mm)` (103) |
| 34 | AJ | Status HIV | `status_hiv` | 6201/6201 | `Tidak Diketahui` (5618), `Bukan ODHIV` (568), `ODHIV` (15) |
| 35 | AK | Riwayat Diabetes Melitus | `riwayat_diabetes_melitus` | 6201/6201 | `Tidak Diketahui` (5228), `Tidak` (858), `Ya` (115) |
| 36 | AL | Hasil Pemeriksaan Mikroskopis / Tanggal Pemeriksaan 1 | `hasil_pemeriksaan_mikroskopis_tanggal_pemeriksaan_1` | 2/6201 | `<tanggal>` (2) |
| 37 | AM | Hasil Pemeriksaan Mikroskopis / Hasil Pemeriksaan 1 | `hasil_pemeriksaan_mikroskopis_hasil_pemeriksaan_1` | 2/6201 | `2+` (2) |
| 38 | AN | Hasil Pemeriksaan Mikroskopis / Tanggal Pemeriksaan 2 | `hasil_pemeriksaan_mikroskopis_tanggal_pemeriksaan_2` | 1/6201 | `<tanggal>` (1) |
| 39 | AO | Hasil Pemeriksaan Mikroskopis / Hasil Pemeriksaan 2 | `hasil_pemeriksaan_mikroskopis_hasil_pemeriksaan_2` | 1/6201 | `2+` (1) |
| 40 | AP | Tanggal Hasil Pemeriksaan Diagnosis TBC | `tanggal_hasil_pemeriksaan_diagnosis_tbc` | 5757/6201 | `<tanggal>` (5757) |
| 41 | AQ | Hasil Pemeriksaan Diagnosis TBC | `hasil_pemeriksaan_diagnosis_tbc` | 5757/6201 | `Neg` (5136), `Rif Sen` (593), `ERROR` (21), `Rif Res` (4), `INVALID` (2), `NO RESULT` (1) |
| 42 | AR | Jenis Pemeriksaan Diagnosis | `jenis_pemeriksaan_diagnosis` | 5757/6201 | `TCM Xpert` (5757) |
| 43 | AS | Tanggal Hasil Pemeriksaan TCM-XDR | `tanggal_hasil_pemeriksaan_tcmxdr` | 14/6201 | `<tanggal>` (14) |
| 44 | AT | Hasil Pemeriksaan Xpert (TCM) - XDR / Valid/Invalid/Error/No Result | `hasil_pemeriksaan_xpert_tcm_xdr_validinvaliderrorno_result` | 14/6201 | `Valid` (14) |
| 45 | AU | Hasil Pemeriksaan Xpert (TCM) - XDR / MTB | `hasil_pemeriksaan_xpert_tcm_xdr_mtb` | 14/6201 | `D` (12), `ND` (1), `RD` (1) |
| 46 | AV | Hasil Pemeriksaan Xpert (TCM) - XDR / H Dosis Rendah (Low) | `hasil_pemeriksaan_xpert_tcm_xdr_h_dosis_rendah_low` | 13/6201 | `RND` (10), `RD` (3) |
| 47 | AW | Hasil Pemeriksaan Xpert (TCM) - XDR / H | `hasil_pemeriksaan_xpert_tcm_xdr_h` | 13/6201 | `RND` (13) |
| 48 | AX | Hasil Pemeriksaan Xpert (TCM) - XDR / Eto | `hasil_pemeriksaan_xpert_tcm_xdr_eto` | 13/6201 | `RND` (13) |
| 49 | AY | Hasil Pemeriksaan Xpert (TCM) - XDR / FQ Dosis Rendah (Low | `hasil_pemeriksaan_xpert_tcm_xdr_fq_dosis_rendah_low` | 13/6201 | `RND` (12), `IDT` (1) |
| 50 | AZ | Hasil Pemeriksaan Xpert (TCM) - XDR / FQ | `hasil_pemeriksaan_xpert_tcm_xdr_fq` | 13/6201 | `RND` (13) |
| 51 | BA | Hasil Pemeriksaan Xpert (TCM) - XDR / Amk | `hasil_pemeriksaan_xpert_tcm_xdr_amk` | 13/6201 | `RND` (12), `IDT` (1) |
| 52 | BB | Hasil Pemeriksaan Xpert (TCM) - XDR / Km | `hasil_pemeriksaan_xpert_tcm_xdr_km` | 13/6201 | `RND` (12), `IDT` (1) |
| 53 | BC | Hasil Pemeriksaan Xpert (TCM) - XDR / Cm | `hasil_pemeriksaan_xpert_tcm_xdr_cm` | 13/6201 | `RND` (12), `IDT` (1) |
| 54 | BD | Tanggal Hasil Pemeriksaan LPA Lini 1 | `tanggal_hasil_pemeriksaan_lpa_lini_1` | 0/6201 |  |
| 55 | BE | Hasil Pemeriksaan LPA (Line Probe Assay) Lini 1 / Invalid | `hasil_pemeriksaan_lpa_line_probe_assay_lini_1_invalid` | 0/6201 |  |
| 56 | BF | Hasil Pemeriksaan LPA (Line Probe Assay) Lini 1 / MTB | `hasil_pemeriksaan_lpa_line_probe_assay_lini_1_mtb` | 0/6201 |  |
| 57 | BG | Hasil Pemeriksaan LPA (Line Probe Assay) Lini 1 / R | `hasil_pemeriksaan_lpa_line_probe_assay_lini_1_r` | 0/6201 |  |
| 58 | BH | Hasil Pemeriksaan LPA (Line Probe Assay) Lini 1 / H | `hasil_pemeriksaan_lpa_line_probe_assay_lini_1_h` | 0/6201 |  |
| 59 | BI | Tanggal Hasil Pemeriksaan LPA Lini 2 | `tanggal_hasil_pemeriksaan_lpa_lini_2` | 0/6201 |  |
| 60 | BJ | Hasil Pemeriksaan LPA (Line Probe Assay) lini 2 / Invalid | `hasil_pemeriksaan_lpa_line_probe_assay_lini_2_invalid` | 0/6201 |  |
| 61 | BK | Hasil Pemeriksaan LPA (Line Probe Assay) lini 2 / MTB | `hasil_pemeriksaan_lpa_line_probe_assay_lini_2_mtb` | 0/6201 |  |
| 62 | BL | Hasil Pemeriksaan LPA (Line Probe Assay) lini 2 / Lfx | `hasil_pemeriksaan_lpa_line_probe_assay_lini_2_lfx` | 0/6201 |  |
| 63 | BM | Hasil Pemeriksaan LPA (Line Probe Assay) lini 2 / Mfx | `hasil_pemeriksaan_lpa_line_probe_assay_lini_2_mfx` | 0/6201 |  |
| 64 | BN | Hasil Pemeriksaan LPA (Line Probe Assay) lini 2 / Mfx DT | `hasil_pemeriksaan_lpa_line_probe_assay_lini_2_mfx_dt` | 0/6201 |  |
| 65 | BO | Hasil Pemeriksaan LPA (Line Probe Assay) lini 2 / Km | `hasil_pemeriksaan_lpa_line_probe_assay_lini_2_km` | 0/6201 |  |
| 66 | BP | Hasil Pemeriksaan LPA (Line Probe Assay) lini 2 / Amk | `hasil_pemeriksaan_lpa_line_probe_assay_lini_2_amk` | 0/6201 |  |
| 67 | BQ | Hasil Pemeriksaan LPA (Line Probe Assay) lini 2 / Cm | `hasil_pemeriksaan_lpa_line_probe_assay_lini_2_cm` | 0/6201 |  |
| 68 | BR | Tanggal Hasil Pemeriksaan Biakan | `tanggal_hasil_pemeriksaan_biakan` | 2/6201 | `<tanggal>` (2) |
| 69 | BS | Hasil Pemeriksaan Biakan | `hasil_pemeriksaan_biakan` | 2/6201 | `Pos` (2) |
| 70 | BT | Tanggal Hasil Pemeriksaan Uji Kepekaan | `tanggal_hasil_pemeriksaan_uji_kepekaan` | 2/6201 | `<tanggal>` (2) |
| 71 | BU | Hasil Pemeriksaan Paket Standar Uji Kepekaan / H Dosis Tinggi | `hasil_pemeriksaan_paket_standar_uji_kepekaan_h_dosis_tinggi` | 2/6201 | `R` (1), `S` (1) |
| 72 | BV | Hasil Pemeriksaan Paket Standar Uji Kepekaan / H | `hasil_pemeriksaan_paket_standar_uji_kepekaan_h` | 2/6201 | `R` (1), `S` (1) |
| 73 | BW | Hasil Pemeriksaan Paket Standar Uji Kepekaan / Km | `hasil_pemeriksaan_paket_standar_uji_kepekaan_km` | 2/6201 | `TDL` (2) |
| 74 | BX | Hasil Pemeriksaan Paket Standar Uji Kepekaan / Cm | `hasil_pemeriksaan_paket_standar_uji_kepekaan_cm` | 2/6201 | `TDL` (2) |
| 75 | BY | Hasil Pemeriksaan Paket Standar Uji Kepekaan / Lfx | `hasil_pemeriksaan_paket_standar_uji_kepekaan_lfx` | 2/6201 | `S` (2) |
| 76 | BZ | Hasil Pemeriksaan Paket Standar Uji Kepekaan / Mfx Dosis Tinggi | `hasil_pemeriksaan_paket_standar_uji_kepekaan_mfx_dosis_tinggi` | 2/6201 | `TDL` (2) |
| 77 | CA | Hasil Pemeriksaan Paket Standar Uji Kepekaan / Mfx | `hasil_pemeriksaan_paket_standar_uji_kepekaan_mfx` | 2/6201 | `S` (2) |
| 78 | CB | Hasil Pemeriksaan Paket Standar Uji Kepekaan / ... | `hasil_pemeriksaan_paket_standar_uji_kepekaan` | 2/6201 | `Bdq= S` (2) |
| 79 | CC | Hasil Pemeriksaan Paket Standar Uji Kepekaan / ... | `hasil_pemeriksaan_paket_standar_uji_kepekaan_1` | 2/6201 | `Cfz= S` (2) |
| 80 | CD | Hasil Pemeriksaan Paket Standar Uji Kepekaan / ... | `hasil_pemeriksaan_paket_standar_uji_kepekaan_2` | 2/6201 | `Lzd= S` (2) |
| 81 | CE | Hasil Pemeriksaan Paket Standar Uji Kepekaan / ... | `hasil_pemeriksaan_paket_standar_uji_kepekaan_3` | 2/6201 | `Z= TDL` (2) |
| 82 | CF | Hasil Pemeriksaan Paket Standar Uji Kepekaan / ... | `hasil_pemeriksaan_paket_standar_uji_kepekaan_4` | 0/6201 |  |
| 83 | CG | Hasil Pemeriksaan Paket Standar Uji Kepekaan / ... | `hasil_pemeriksaan_paket_standar_uji_kepekaan_5` | 0/6201 |  |
| 84 | CH | Terkonfirmasi TBC | `terkonfirmasi_tbc` | 1042/6201 | `TBC SO` (1037), `TBC RO` (5) |
| 85 | CI | Tanggal Hasil Diagnosis | `tanggal_hasil_diagnosis` | 5425/6201 | `<tanggal>` (5425) |
| 86 | CJ | Hasil Diagnosis | `hasil_diagnosis` | 5425/6201 | `Bukan TBC` (4429), `TBC SO` (992), `TBC RO` (4) |
| 87 | CK | Tipe Diagnosis | `tipe_diagnosis` | 996/6201 | `Terkonfirmasi bakteriologis` (550), `Terdiagnosis klinis` (446) |
| 88 | CL | Tindak Lanjut | `tindak_lanjut` | 996/6201 | `Akan Diobati/Dirujuk` (955), `Meninggal sebelum pengobatan` (19), `Belum Mulai Pengobatan` (14), `Melanjutkan Pengobatan Sebelumnya` (5), `Lost to follow up sebelum pengobatan` (1), `Menolak pengobatan` (1), `Melanjutkan pengobatan sebelumnya` (1) |
| 89 | CM | Tempat Pengobatan / Dirujuk ke (Nama fasyankes) | `tempat_pengobatan_dirujuk_ke_nama_fasyankes` | 124/6201 | *(identitas / teks bebas, tidak ditampilkan)* |
| 90 | CN | Tempat Pengobatan / Tidak Dirujuk | `tempat_pengobatan_tidak_dirujuk` | 833/6201 | `V` (833) |
| 91 | CO | Tanggal Mulai Pengobatan TBC (Tgl/Bln/Thn) | `tanggal_mulai_pengobatan_tbc_tglblnthn` | 901/6201 | `<tanggal>` (901) |
| 92 | CP | Tanggal Tes HIV | `tanggal_tes_hiv` | 463/6201 | `<tanggal>` (463) |
| 93 | CQ | Hasil Tes HIV | `hasil_tes_hiv` | 463/6201 | `Bukan ODHIV` (455), `ODHIV` (8) |
| 94 | CR | ART | `art` | 18/6201 | `Tidak` (16), `Ya` (2) |
| 95 | CS | Hasil Tes DM | `hasil_tes_dm` | 445/6201 | `Negatif` (421), `Positif` (24) |
| 96 | CT | Keterangan (Diisi tempat pemeriksaan selain Mikroskopis) | `keterangan_diisi_tempat_pemeriksaan_selain_mikroskopis` | 63/6201 | 44 nilai berbeda (teks bebas), contoh tidak ditampilkan |
| 97 | CU | Tindak lanjut penambahan resistansi | `tindak_lanjut_penambahan_resistansi` | 1/6201 | `Sudah didaftarkan menjadi terduga` (1) |

Kolom BQ yang tidak ada di file mentah: `puskesmas_name`, `puskesmas_id`, `file_name`, `file_date`, `ingestion_timestamp`, `uuid`, `hash_code`
