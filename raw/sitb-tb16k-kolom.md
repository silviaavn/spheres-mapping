# File mentah SITB TB 16K — struktur kolom

Sumber: export SITB `Puskesmas_Serayu_Larangan_Report_TB_16K_FASYANKES_spheres_Januari-Juni_2025.xlsx` (Register Investigasi Kontak, 1 puskesmas). File `Daftar Laporan TBC 16K - SITK.xlsx` di folder yang sama adalah export SITK dengan format berbeda (35 kolom datar) dan tidak cocok dengan tabel BQ `sitb_tb_16k`.
File asli **tidak** disimpan di repo karena berisi data pasien. File ini berisi struktur kolom, jumlah terisi, dan nilai pilihan (kolom identitas & teks bebas tidak ditampilkan).

- `Puskesmas_Serayu_Larangan_Report_TB_16K_FASYANKES`: header sampai baris 14 (baris 14 = nomor kolom (1), (2), ...), 3 baris data.

| # | Kolom Excel | Header | Variabel BQ | Terisi (Puskesmas_Serayu_Larangan_Report_TB_16K_FASYANKES) | Nilai (frekuensi) |
|---|---|---|---|---|---|
| 1 | C | No. | `no` ⛔ tidak dimapping | 3/3 | `<angka>` (3) |
| 2 | D | Petugas yang menginvestigasi kontak / Nama Kader / Petugas Kesehatan | `petugas_yang_menginvestigasi_kontak_nama_kader_petugas_kesehatan` | 3/3 | *(identitas / teks bebas, tidak ditampilkan)* |
| 3 | E | Petugas yang menginvestigasi kontak / Nama Fasyankes/Organisasi Kader | `petugas_yang_menginvestigasi_kontak_nama_fasyankesorganisasi_kader` | 3/3 | *(identitas / teks bebas, tidak ditampilkan)* |
| 4 | F | Dirujuk/dikirim oleh | `dirujukdikirim_oleh` | 3/3 | `Internal` (3) |
| 5 | G | No Register SITB | `no_register_sitb` | 3/3 | *(identitas / teks bebas, tidak ditampilkan)* |
| 6 | H | Nama Kasus Indeks | `nama_kasus_indeks` | 3/3 | *(identitas / teks bebas, tidak ditampilkan)* |
| 7 | I | Umur Kasus Indeks | `umur_kasus_indeks` | 3/3 | `<angka>` (3) |
| 8 | J | Tipe Diagnosis | `tipe_diagnosis` | 3/3 | `Terkonfirmasi bakteriologis` (3) |
| 9 | K | Tanggal Hasil Diagnosis | `tanggal_hasil_diagnosis` | 3/3 | `<tanggal>` (3) |
| 10 | L | Jenis Kasus Indeks | `jenis_kasus_indeks` | 3/3 | `TBC SO` (3) |
| 11 | M | Identitas Kontak / Nama | `identitas_kontak_nama` | 3/3 | *(identitas / teks bebas, tidak ditampilkan)* |
| 12 | N | Identitas Kontak / NIK | `identitas_kontak_nik` | 3/3 | *(identitas / teks bebas, tidak ditampilkan)* |
| 13 | O | Identitas Kontak / Umur | `identitas_kontak_umur` | 3/3 | `<angka>` (3) |
| 14 | P | Identitas Kontak / L/P | `identitas_kontak_lp` | 3/3 | `P` (2), `L` (1) |
| 15 | Q | Identitas Kontak / Alamat | `identitas_kontak_alamat` | 3/3 | *(identitas / teks bebas, tidak ditampilkan)* |
| 16 | R | Identitas Kontak / Metode IK | `identitas_kontak_metode_ik` | 3/3 | `Kunjungan Rumah` (3) |
| 17 | S | Identitas Kontak / Kontak Serumah | `identitas_kontak_kontak_serumah` | 2/3 | `V` (2) |
| 18 | T | Identitas Kontak / Kontak Erat | `identitas_kontak_kontak_erat` | 1/3 | `V` (1) |
| 19 | U | Tanggal Investigasi | `tanggal_investigasi` | 3/3 | `<tanggal>` (3) |
| 20 | V | Hasil Skrining / Batuk | `hasil_skrining_batuk` | 0/3 |  |
| 21 | W | Hasil Skrining / Gejala Lain / Sesak napas | `hasil_skrining_gejala_lain_sesak_napas` | 0/3 |  |
| 22 | X | Hasil Skrining / Gejala Lain / Berkeringat malam hari tanpa kegiatan | `hasil_skrining_gejala_lain_berkeringat_malam_hari_tanpa_kegiatan` | 0/3 |  |
| 23 | Y | Hasil Skrining / Gejala Lain / Demam meriang >1 bulan | `hasil_skrining_gejala_lain_demam_meriang_1_bulan` | 0/3 |  |
| 24 | Z | Hasil Skrining / Faktor Risiko / DM | `hasil_skrining_faktor_risiko_dm` | 0/3 |  |
| 25 | AA | Hasil Skrining / Faktor Risiko / Lansia >60 th | `hasil_skrining_faktor_risiko_lansia_60_th` | 0/3 |  |
| 26 | AB | Hasil Skrining / Faktor Risiko / Ibu Hamil | `hasil_skrining_faktor_risiko_ibu_hamil` | 0/3 |  |
| 27 | AC | Hasil Skrining / Faktor Risiko / Perokok | `hasil_skrining_faktor_risiko_perokok` | 0/3 |  |
| 28 | AD | Hasil Skrining / Faktor Risiko / Pernah berobat TBC tapi tidak tuntas | `hasil_skrining_faktor_risiko_pernah_berobat_tbc_tapi_tidak_tuntas` | 0/3 |  |
| 29 | AE | Memenuhi syarat rujukan pemeriksaan Terduga | `memenuhi_syarat_rujukan_pemeriksaan_terduga` | 0/3 |  |
| 30 | AF | Dirujuk Pemeriksaan Terduga TBC | `dirujuk_pemeriksaan_terduga_tbc` | 0/3 |  |
| 31 | AG | Diperiksa Terduga TBC | `diperiksa_terduga_tbc` | 0/3 |  |
| 32 | AH | Hasil Pemeriksaan Terduga / Sakit TBC | `hasil_pemeriksaan_terduga_sakit_tbc` | 0/3 |  |
| 33 | AI | Hasil Pemeriksaan Terduga / Tidak TBC | `hasil_pemeriksaan_terduga_tidak_tbc` | 0/3 |  |
| 34 | AJ | Memenuhi syarat rujukan pemeriksaan Eligibilitas TPT | `memenuhi_syarat_rujukan_pemeriksaan_eligibilitas_tpt` | 2/3 | `V` (2) |
| 35 | AK | Kesimpulan Hasil Pemeriksaan Eligibilitas TPT | `kesimpulan_hasil_pemeriksaan_eligibilitas_tpt` | 0/3 |  |
| 36 | AL | Memenuhi syarat TPT | `memenuhi_syarat_tpt` | 0/3 |  |
| 37 | AM | Tanggal Pemberian TPT / < 5 th | `tanggal_pemberian_tpt__5_th` | 0/3 |  |
| 38 | AN | Tanggal Pemberian TPT / ≥ 5 th | `tanggal_pemberian_tpt__5_th_1` | 0/3 |  |
| 39 | AO | Hasil Akhir TPT / < 5 th | `hasil_akhir_tpt__5_th` | 0/3 |  |
| 40 | AP | Hasil Akhir TPT / ≥ 5 th | `hasil_akhir_tpt__5_th_1` | 0/3 |  |

Kolom BQ yang tidak ada di file mentah: `puskesmas_name`, `puskesmas_id`, `file_name`, `file_date`, `ingestion_timestamp`, `uuid`, `hash_code`, `nama_fasyankes`
