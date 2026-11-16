# File mentah SiGizi ANC — struktur kolom

Sumber: `PUSKESMAS PADAMARA_SiGizi_Pengukuran_ANC_2026-11-16_13_00_41.980.xlsx` (export web SiGizi Kesga, 1 sheet, header 3 baris dengan merge cell, 57 baris data).
File asli **tidak** disimpan di repo karena berisi data pasien. File ini berisi struktur kolom dan nilai pilihan (kolom identitas tidak ditampilkan).

Merge cell header: A1:A3, AA2:AA3, AB2:AB3, AC2:AC3, AD2:AD3, AE2:AM2, AN2:AN3, AO2:AO3, AP2:AP3, AQ2:AQ3, AR2:AR3, AS2:AS3, AT2:AT3, AU2:AU3, AV2:AV3, AW2:AW3, AX2:AX3, B1:B3, C1:C3, D1:D3, E1:E3, F1:F3, G1:G3, H1:H3, I1:I3, J1:J3, K1:K3, L1:L3, M1:M3, N1:N3, O1:O3, P1:AX1, P2:P3, Q2:Q3, R2:R3, S2:S3, T2:T3, U2:U3, V2:V3, W2:W3, X2:X3, Y2:Y3, Z2:Z3

| # | Kolom Excel | Header (baris 1 / 2 / 3) | Variabel BQ | Terisi | Nilai (frekuensi) |
|---|---|---|---|---|---|
| 1 | B | NIK | `nik` ⚠️ | 57/57 | *(identitas, tidak ditampilkan)* |
| 2 | C | Nama | `nama` ⚠️ | 57/57 | *(identitas, tidak ditampilkan)* |
| 3 | D | Tanggal Lahir | `tanggal_lahir` | 57/57 | *(identitas, tidak ditampilkan)* |
| 4 | E | Umur | `umur` | 57/57 | `<angka>` (57) |
| 5 | F | Prov Domisili | `prov_domisili` | 57/57 | `JAWA TENGAH` (57) |
| 6 | G | Kab/Kota Domisili | `kabkota_domisili` | 57/57 | `KABUPATEN PURBALINGGA` (57) |
| 7 | H | Kec Domisili | `kec_domisili` | 57/57 | `PADAMARA` (57) |
| 8 | I | Puskesmas Domisili | `puskesmas_domisili` | 57/57 | `PADAMARA` (57) |
| 9 | J | Desa/Kel Domisili | `desakel_domisili` | 57/57 | `DAWUHAN` (8), `KARANGJAMBE` (8), `BOJANEGARA` (5), `KARANGPULE` (5), `MIPIRAN` (5), `KALITINGGAR KIDUL` (5), `KALITINGGAR` (4), `SOKAWERA` (4), `KARANGGAMBAS` (3), `PRIGI` (3), `PADAMARA` (2), `PURBAYASA` (2), `KARANGSENTUL` (2), `GEMURUH` (1) |
| 10 | K | Posyandu Domisili | `posyandu_domisili` | 54/57 | 25 nilai berbeda (teks bebas), contoh tidak ditampilkan |
| 11 | L | Alamat Domisili | `alamat_domisili` | 57/57 | *(identitas, tidak ditampilkan)* |
| 12 | M | Faskes yang melayani ANC | `faskes_yang_melayani_anc` | 57/57 | `ASIH SUBEKTI` (24), `Puskesmas Padamara` (10), `Ari Handayani` (7), `RSIA Ummu Hani Purbalingga` (5), `RSU Siaga Medika Purbalingga` (4), `Puskesmas Bojongsari` (2), `DSOG` (1), `RSU Harapan Ibu Purbalingga` (1), `Kunjungan rumah` (1), `PMB Ari Budiyanti` (1), `RSUD Goeteng Taroenadibrata Purbalingga` (1) |
| 13 | N | Pemeriksaan Pertama | `pemeriksaan_pertama` | 57/57 | `Tidak` (51), `Ya` (6) |
| 14 | O | Tanggal HPHT | `tanggal_hpht` | 57/57 | `<tanggal>` (57) |
| 15 | P | Pemeriksaan ANC / Tanggal ANC | `pemeriksaan_anc_tanggal_anc` | 57/57 | `<tanggal>` (57) |
| 16 | Q | Usia Kehamilan | `pemeriksaan_anc_usia_kehamilan` | 57/57 | 28 nilai berbeda (teks bebas), contoh tidak ditampilkan |
| 17 | R | Tenaga Pemeriksa | `pemeriksaan_anc_tenaga_pemeriksa` | 57/57 | `Bidan` (27), `Dokter Umum` (18), `SpOG` (12) |
| 18 | S | Riwayat Imun TT Terakhir | `pemeriksaan_anc_riwayat_imun_tt_terakhir` | 57/57 | `TT 5` (36), `Tidak dilakukan skrinning TT` (19), `TT 4` (1), `TT 3` (1) |
| 19 | T | Berat | `pemeriksaan_anc_berat` | 57/57 | 17 nilai berbeda (teks bebas), contoh tidak ditampilkan |
| 20 | U | Tinggi | `pemeriksaan_anc_tinggi` | 57/57 | `<angka>` (55), `150.5` (1), `153.5` (1) |
| 21 | V | LiLA | `pemeriksaan_anc_lila` | 0/57 |  |
| 22 | W | Tekanan Darah | `pemeriksaan_anc_tekanan_darah` | 57/57 | `Normal (<= 140)` (55), `Hipertensi (>= 140)` (2) |
| 23 | X | TFU | `pemeriksaan_anc_tfu` | 57/57 | `Sesuai usia kehamilan` (57) |
| 24 | Y | Presentasi Janin | `pemeriksaan_anc_presentasi_janin` | 57/57 | `Kepala` (28), `Organ tubuh lainnya` (22), `Letak Bokong/Lintang` (4), `Tidak Dilakukan Pemeriksaan Janin` (3) |
| 25 | Z | DJJ | `pemeriksaan_anc_djj` | 57/57 | `Terdengar, normal (110-160)` (53), `Tidak diperiksa DJJ` (4) |
| 26 | AA | Diperiksa USG | `pemeriksaan_anc_diperiksa_usg` | 57/57 | `Diperiksa, hasil normal` (28), `Tidak diperiksa` (28), `Diperiksa, kecurigaan hasil abnormal` (1) |
| 27 | AB | IMT Sebelum Hamil | `pemeriksaan_anc_imt_sebelum_hamil` | 57/57 | 42 nilai berbeda (teks bebas), contoh tidak ditampilkan — ⚠️ nilai `<tanggal>` = angka yang diubah Excel jadi tanggal (P12) |
| 28 | AC | Jumlah TTD Diterima | `pemeriksaan_anc_jumlah_ttd_diterima` | 57/57 | `0` (37), `30` (16), `10` (2), `15` (1), `14` (1) |
| 29 | AD | Jumlah MMS Diterima | `pemeriksaan_anc_jumlah_mms_diterima` | 57/57 | `0` (53), `180` (4) |
| 30 | AE | Pemeriksaan ANC / Lab / Golongan Darah | `pemeriksaan_anc_lab_golongan_darah` | 48/57 | `O` (16), `A` (13), `B` (12), `AB` (7) |
| 31 | AF | Pemeriksaan ANC / Lab / Rhesus | `pemeriksaan_anc_lab_rhesus` | 57/57 | `Positif` (23), `positif` (22), `--Pilih--` (12) |
| 32 | AG | Pemeriksaan ANC / Lab / HIV | `pemeriksaan_anc_lab_hiv` | 57/57 | `Tidak Diperiksa` (43), `Non reaktif` (14) |
| 33 | AH | Pemeriksaan ANC / Lab / Hepatitis | `pemeriksaan_anc_lab_hepatitis` | 57/57 | `Tidak Diperiksa` (43), `Negatif` (14) |
| 34 | AI | Pemeriksaan ANC / Lab / Siphilis | `pemeriksaan_anc_lab_siphilis` | 57/57 | `Tidak Diperiksa` (43), `Negatif` (14) |
| 35 | AJ | Pemeriksaan ANC / Lab / Protein Urine | `pemeriksaan_anc_lab_protein_urine` | 57/57 | `Tidak Diperiksa` (36), `Negatif` (20), `Positif` (1) |
| 36 | AK | Pemeriksaan ANC / Lab / Hb | `pemeriksaan_anc_lab_hb` | 57/57 | `Tidak diperiksa Hb` (35), `Tidak Anemia (>=11)` (19), `Anemia Ringan (10-10,9)` (2), `Anemia Sedang (7-9,9)` (1) |
| 37 | AL | Pemeriksaan ANC / Lab / Gula Sewaktu | `pemeriksaan_anc_lab_gula_sewaktu` | 57/57 | `Tidak Diperiksa` (34), `Normal < 200` (23) |
| 38 | AM | Pemeriksaan ANC / Lab / Lainnya | `pemeriksaan_anc_lab_lainnya` | 57/57 | `-` (57) |
| 39 | AN | Tatalaksana Anemia | `pemeriksaan_anc_tatalaksana_anemia` | 57/57 | `-` (54), `Pemberian tablet tambah darah` (2), `Pemberian Fe Parenteral` (1) |
| 40 | AO | Pre Eklampsia | `pemeriksaan_anc_pre_eklampsia` | 57/57 | `Tidak Pre eklampsia/Eklampsia` (32), `-` (23), `Hipertensi dalam Kehamilan` (2) |
| 41 | AP | Tatalaksana Pre Eklampsia | `pemeriksaan_anc_tatalaksana_pre_eklampsia` | 57/57 | `-` (55), `Rujuk` (1), `Pemberian obat anti hipertensi` (1) |
| 42 | AQ | Status Gizi KEK/Tidak KEK | `pemeriksaan_anc_status_gizi_kektidak_kek` | 57/57 | `Tidak KEK` (51), `KEK` (4), `Risiko KEK` (2) |
| 43 | AR | Tatalaksana KEK | `pemeriksaan_anc_tatalaksana_kek` | 57/57 | `-` (53), `Pemberian MT` (4) |
| 44 | AS | Risiko Masalah Kesehatan Lainnya | `pemeriksaan_anc_risiko_masalah_kesehatan_lainnya` | 57/57 | `-` (55), `Lainnya` (2) |
| 45 | AT | Diberikan Tatalaksana Masalah Kesehatan Lainnya | `pemeriksaan_anc_diberikan_tatalaksana_masalah_kesehatan_lainnya` | 57/57 | `-` (55), `Ya` (2) |
| 46 | AU | Konseling | `pemeriksaan_anc_konseling` | 57/57 | `Ya` (56), `Tidak` (1) |
| 47 | AV | Skrinning Keswa | `pemeriksaan_anc_skrinning_keswa` | 57/57 | `Tidak` (40), `Ya` (17) |
| 48 | AW | Tanggal Perkiraan Persalinan | `pemeriksaan_anc_tanggal_perkiraan_persalinan` | 57/57 | `<tanggal>` (57) |
| 49 | AX | Aksi | `pemeriksaan_anc_aksi` | 0/57 |  |

Kolom A (`No`) tidak masuk BQ.

⚠️ Urutan kolom B (NIK) dan C (Nama) di Excel terbalik dibanding urutan BQ (`nama`, `nik`). Ingestion harus memetakan berdasarkan nama header, bukan posisi kolom (P17).

Usia Kehamilan berformat `<angka> Minggu` (mis. `24 Minggu`). IMT Sebelum Hamil: 9 dari 57 nilai sudah berubah jadi tanggal oleh Excel (P12).
