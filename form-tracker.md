# Form Tracker — Sumber Data Mapping FHIR

Versi editable (sumber utama): Sheet [Daftar Sumber Data Puskesmas - Mapping FHIR](https://claude.ai/artifact/HRNvr5haWkiSyVHUVakRgj). File ini salinan dari Sheet. Status review di-update di Sheet **dan** di file ini setiap form selesai (lihat `aturan.md`, checklist langkah 6).

Angka code per form diperbarui 2026-11-25 (aturan hitung baru: code SP custom di path coded mana pun, dataAbsentReason, path QuestionnaireResponse valid; path disamakan ke FHIR R4). Angka payload tidak berubah. Total non-unik 7313 payload / 19299 code; unik 1420 / 4257.

Total: 251 laporan · Masih diperlukan: 232 · Dimapping ke FHIR: 224 · Sudah direview: 9

⚠️ = payload dan code sudah dihitung, tapi **belum ada comprehensive review** (belum ada daftar variabel BQ, file mentah, atau pembahasan dengan tim). Tidak dihitung di "Sudah direview". Kolom Catatan di Sheet (G73, G74) berisi catatan yang sama. Saat ini:

| # | Laporan | Payload / code |
|---|---|---|
| 1 | ePuskesmas - Pelayanan Pasien | 47 / 62 |
| 3 | ePuskesmas - Laporan Kunjungan Ibu Hamil (sheet lama) | 114 / 206 |
| 5 | ePuskesmas - Laboratorium | 309 / 500 |
| 8 | ePuskesmas - Rujukan Eksternal | 5 / 0 |
| 11 | KIA Harian - ANC | 155 / 346 |
| 12 | KIA Harian - INC | 69 / 210 |
| 13 | KIA Harian - PNC | 82 / 166 |
| 14 | KIA Harian - MTBS | 125 / 285 |
| 15 | KIA Harian - MTBM | 57 / 139 |
| 16 | Tumbuh Kembang (8 dictionary: Anak 19 / 62, DDTK 29 / 92, KPSP 14 / 0, TDD 8 / 0, TDL 4 / 8, KMPE 1 / 0, M-CHAT-R 1 / 0, GPPH 1 / 40) | 77 / 202 |
| 17 | SiGizi - Posyandu Balita BNBA (daftar status gizi) | 24 / 50 |
| 18 | SiGizi - Balita Vitamin A | 22 / 51 |
| 19 | SiGizi - Balita Mendapat PMT 2024 | 15 / 45 |
| 20 | SiGizi - Balita Pemantauan PMT 2024 | 9 / 15 |
| 21 | SiGizi - Asi Eksklusif | 11 / 36 |
| 22 | SiGizi - Balita Pemantauan MPASI | 9 / 32 |
| 24 | SIGIZI (Balita BB Tidak Naik) - Pantau PMT 2025 | 15 / 33 |
| 25 | SIGIZI (Balita BB Tidak Naik) - Riwayat PMT 2025 | 19 / 75 |
| 26 | SIGIZI (Balita BB Tidak Naik) - Survey PMT 2025 | 5 / 16 |
| 27 | SIGIZI (Balita BB Kurang) - Pantau PMT 2025 | 21 / 47 |
| 28 | SIGIZI (Balita BB Kurang) - Riwayat PMT 2025 | 19 / 75 |
| 29 | SIGIZI (Balita BB Kurang) - Survey PMT 2025 | 5 / 16 |
| 30 | SIGIZI (Balita Gizi Kurang) - Pantau PMT 2025 | 42 / 102 |
| 31 | SIGIZI (Balita Gizi Kurang) - Riwayat PMT 2025 | 19 / 75 |
| 32 | SIGIZI (Balita Gizi Kurang) - Survey PMT 2025 | 5 / 16 |
| 34 | SIGIZI IBU - Daftar Nifas | 11 / 12 |
| 35 | SIGIZI IBU - Pengukuran ANC Bumil | 61 / 154 |
| 36 | SIGIZI IBU - Kohort Ibu | 63 / 109 |
| 39 | ASIK - Data Individu Kohort Bayi (Imunisasi) | 19 / 27 |
| 40 | ASIK - Data Individu Kohort Baduta (Imunisasi) | 4 / 6 |
| 41 | ASIK - Data Individu Kohort WUS (Imunisasi) | 12 / 20 |
| 42 | ASIK - Data Skrining PTM | 104 / 215 |
| 43 | ASIK - CKG-Klaster BBL (versi 2; v1 25 / 56) | 25 / 41 |
| 44 | ASIK - CKG-Klaster Balita Pra Sekolah (versi 2; v1 29 / 99) | 32 / 102 |
| 46 | ASIK - CKG-Klaster Dewasa Laki-laki | 61 / 278 |
| 47 | ASIK - CKG-Klaster Dewasa Perempuan | 66 / 299 |
| 48 | ASIK - CKG-Klaster Lansia (versi 27 Apr 2026; 2026 82 / 366, 2025 80 / 361) | 101 / 567 |
| 49 | SiHepi - Form Rekap 3e | 65 / 118 |
| 50 | SITB - TB 01 (Kartu Pengobatan Pasien) | 37 / 101 |
| 51 | SITB - TB 02 (Kartu Identitas Pasien) | 13 / 15 |
| 52 | SITB - TB 03 SO (Sensitif Obat) | 62 / 358 |
| 53 | SITB - TB 03 RO (Resisten Obat) | 50 / 403 |
| 54 | SITB - TB 04 Fasyankes (pemeriksaan lab) (satu dictionary TB 04 bersama Rujukan) | 69 / 616 |
| 55 | SITB - TB 04 Rujukan (pemeriksaan lab) (satu dictionary TB 04 bersama Fasyankes, dihitung 1x di #54) | ikut #54 |
| 56 | SITB - TB 06 (terduga/suspek TB) | 56 / 301 |
| 60 | SITB - TB 15 (Pemeriksaan Eligibilitas TPT) | 13 / 113 |
| 61 | SITB - TB 15P (Penerima TPT) | 21 / 59 |
| 62 | SITB - TB 16K (IK) | 21 / 35 |
| 64 | SISMAL (Malaria) - Regmal 1 | 20 / 54 |
| 72 | MPDN - Laporan Kematian Bayi | 19 / 115 |
| 73 | MPDN - Laporan Kematian Ibu | 10 / 50 |
| 74 | eKohort - Pelayanan Ibu ANC (Final Format; file lama 140 / 247 tidak dipakai) | 43 / 78 |
| 77 | eKohort - Pelayanan Ibu Bersalin (INC) | 58 / 82 |
| 78 | Informed Consent | 3 / 8 |
| 79 | Buku KIA - Identitas dan ANC | 206 / 438 |
| 80 | Buku KIA - INC | 60 / 108 |
| 81 | Buku KIA - PNC | 14 / 32 |
| 82 | Buku KIA - Anak | 189 / 288 |
| 83 | Kobo Modul ANC | 86 / 189 |
| 84 | Kobo Modul INC | 80 / 248 |
| 85 | Kobo Modul Neonatus | 50 / 100 |
| 86 | Kobo Modul PNC | 98 / 228 |
| 88 | Kobo Buku KIA 1 - ANC | 167 / 733 |
| 89 | Kobo Buku KIA 2 - Luaran Kehamilan | 38 / 87 |
| 90 | Kobo Buku KIA 3 - PNC | 75 / 175 |
| 91 | Kobo Buku KIA 4 - Cadre | 44 / 51 |
| 92 | Kobo Buku KIA 5 - Vaksinatorku | 40 / 65 |
| 93 | Kobo Neonatus Outcome | 14 / 25 |
| 94 | Kobo Neonatus Outcome v2 | 89 / 276 |
| 101 | Kobo DDTK | 11 / 10 |
| 103 | Kobo - SDIDTK | 35 / 92 |
| 104 | Kobo - Maternal Outcome | 12 / 14 |
| 105 | Kobo - Raffle | 8 / 6 |
| 106 | KuApps BidanKu - ANC | 190 / 440 |
| 107 | KuApps BidanKu - PNC | 49 / 143 |
| 108 | KuApps BidanKu - BBL | 48 / 103 |
| 109 | KuApps BidanKu - Bayi | 101 / 242 |
| 110 | KuApps BidanKu - Anak | 81 / 157 |
| 111 | KuApps BidanKu - Anak Usia Sekolah dan Remaja | 31 / 83 |
| 112 | KuApps BidanKu - Dewasa | 39 / 122 |
| 113 | KuApps BidanKu - Lansia | 29 / 121 |
| 114 | Kuapps Spheres - HT | 10 / 243 |
| 115 | Kuapps Spheres - DM | 10 / 245 |
| 116 | Kuapps Spheres - TB | 5 / 49 |
| 118 | Genomics - TB | 8 / 43 |
| 119 | Genomics - Klebsiella | 10 / 31 |
| 120 | Genomics - Dengue | 12 / 22 |
| 121 | ELSMIL (BKKBN) - Ibu Hamil | 36 / 105 |
| 122 | ELSMIL (BKKBN) - Pasca Persalinan | 24 / 102 |
| 123 | ELSMIL (BKKBN) - Baduta | 31 / 84 |
| 124 | Dapodik - PAUD (semester) | 42 / 378 |
| 128 | SIM RS Data - At tin ANC (template Spheres) | 89 / 194 |
| 129 | SIM RS Data - At tin INC (template Spheres) | 67 / 164 |
| 130 | SIM RS Data - At tin PNC (template Spheres) | 67 / 147 |
| 131 | SIM RS Data - At tin BBL (template Spheres) | 82 / 126 |
| 137 | SIM RS Data - Harapan Ibu ANC (template Spheres) | 89 / 194 |
| 138 | SIM RS Data - Harapan Ibu INC (template Spheres) | 67 / 164 |
| 139 | SIM RS Data - Harapan Ibu PNC (template Spheres) | 67 / 147 |
| 140 | SIM RS Data - Harapan Ibu BBL (template Spheres) | 79 / 114 |
| 146 | SIM RS Data - Siaga Medika ANC | 100 / 193 |
| 147 | SIM RS Data - Siaga Medika INC | 42 / 125 |
| 148 | SIM RS Data - Siaga Medika PNC | 49 / 110 |
| 149 | SIM RS Data - Siaga Medika BBL | 37 / 48 |
| 150 | SIM RS Data - Siaga Medika Hepatitis (template Spheres) | 20 / 22 |
| 155 | SIM RS Data - MPH ANC | 33 / 90 |
| 156 | SIM RS Data - MPH INC | 40 / 94 |
| 157 | SIM RS Data - MPH PNC | 43 / 104 |
| 158 | SIM RS Data - MPH BBL | 42 / 59 |
| 159 | SIM RS Data - MPH Hepatitis (template Spheres) | 20 / 22 |
| 160 | SIM RS Data - MPH Diabetes Melitus | 24 / 37 |
| 161 | SIM RS Data - MPH Hipertensi | 20 / 22 |
| 164 | SIM RS Data - Nirmala ANC (template Spheres) | 89 / 194 |
| 165 | SIM RS Data - Nirmala INC (template Spheres) | 67 / 164 |
| 166 | SIM RS Data - Nirmala PNC (template Spheres) | 67 / 147 |
| 167 | SIM RS Data - Nirmala BBL (template Spheres) | 82 / 126 |
| 173 | SIM RS Data - Ummu Hani ANC | 23 / 49 |
| 174 | SIM RS Data - Ummu Hani INC | 41 / 97 |
| 175 | SIM RS Data - Ummu Hani PNC | 53 / 112 |
| 176 | SIM RS Data - Ummu Hani BBL | 30 / 55 |
| 177 | SIM RS Data - Ummu Hani Hepatitis (template Spheres) | 20 / 22 |
| 182 | SIM RS Data - PKU ANC (template Spheres) | 89 / 194 |
| 183 | SIM RS Data - PKU INC | 66 / 179 |
| 184 | SIM RS Data - PKU PNC | 67 / 133 |
| 185 | SIM RS Data - PKU BBL (template Spheres) | 82 / 126 |
| 186 | SIM RS Data - PKU Hepatitis (template Spheres) | 20 / 22 |
| 191 | SIM RS Data - Goetoeng ANC | 106 / 111 |
| 192 | SIM RS Data - Goetoeng INC | 64 / 245 |
| 193 | SIM RS Data - Goetoeng PNC | 9 / 21 |
| 194 | SIM RS Data - Goetoeng BBL | 68 / 124 |
| 196 | SIM RS Data - Goetoeng Diabetes Melitus | 6 / 4 |
| 197 | SIM RS Data - Goetoeng Hipertensi | 5 / 3 |
| 200 | SIM RS Data - Panti Nugroho ANC | 31 / 77 |
| 201 | SIM RS Data - Panti Nugroho INC | 37 / 121 |
| 202 | SIM RS Data - Panti Nugroho PNC | 67 / 133 |
| 203 | SIM RS Data - Panti Nugroho BBL | 31 / 55 |
| 205 | SIM RS Data - Panti Nugroho Diabetes Melitus | 7 / 4 |
| 206 | SIM RS Data - Panti Nugroho Hipertensi | 23 / 21 |
| 207 | SIM RS Data - Panti Nugroho Stroke | 20 / 23 |
| 219 | SIM RS Data - Narmada INC | 86 / 264 |
| 222 | SIM RS Data - Narmada KIA | 50 / 110 |
| 228 | SIM RS Data - Tripat ANC | 20 / 28 |
| 230 | SIM RS Data - Tripat PNC | 24 / 28 |
| 231 | SIM RS Data - Tripat BBL (sheet 'INC BBL') | 23 / 20 |
| 237 | SIPTM (baru ditambahkan) | 52 / 214 |
| 275 | SISMAL (Malaria) - Validasi Kasus Indigenous | 7 / 13 |
| 284 | KuApps New - BidanKu: Tambah Pasien | 11 / 33 |
| 285 | KuApps New - BidanKu: Daftar Kehamilan | 12 / 32 |
| 286 | KuApps New - BidanKu: Luaran Kehamilan | 31 / 156 |
| 287 | KuApps New - BidanKu: PHBS | 1 / 3 |
| 288 | KuApps New - BidanKu: Skrining Rumah Tangga | 2 / 9 |
| 289 | KuApps New - BidanKu: Imunisasi | 23 / 52 |
| 290 | KuApps New - BidanKu: Kumpulan Skrinning | 23 / 30 |
| 291 | MMS - Pemantauan Distribusi dan Konsumsi | 22 / 58 |
| 292 | MMS - Informed Consent | 8 / 7 |
| 293 | MMS - Master Database Responden | 16 / 48 |
| 294 | MMS - Survei Sosio Ekonomi | 22 / 229 |
| 295 | MMS - Survei Demografi (Listing Responden) | 12 / 20 |
| 296 | MMS - Konfirmasi Kelahiran dan Luaran Kehamilan | 50 / 193 |

Lihat `revisi.md` bagian ePuskesmas (asumsi EA1–EA10) dan bagian Tumbuh Kembang tambahan (EB1–EB6) dan MPDN (asumsi MA1–MA10, temuan MG/MB/MI), dan SiGizi (17 form, asumsi/temuan SG1–SG14). Kolom Status review di Sheet perlu disamakan (belum diubah di Sheet, termasuk #43, #44, #46–#49, #74, #77, #78 yang baru ⚠️).

### Versi ASIK CKG (PHDT_ASIK_CKG.xlsx)

Form CKG punya beberapa versi dictionary. **Versi terbaru dipakai** (di tabel ⚠️ di atas dan di `output.md`); versi lain dihitung terpisah, tidak masuk total. Detail dan perbedaan antar versi: `output.md` bagian "Versi ASIK CKG".

| # | Form | Versi | Sheet | Payload / code | Dipakai |
|---|---|---|---|---|---|
| 43 | CKG BBL | v2 (tarikan baru) | `CKG Bayi Baru Lahir 2` | 25 / 41 | ✅ |
| 43 | CKG BBL | v1 | `CKG Bayi Baru Lahir` | 25 / 56 |  |
| 44 | CKG Balita dan Anak Pra-Sekolah | v2 (tarikan baru, asumsi) | `Sheet9` | 32 / 102 | ✅ |
| 44 | CKG Balita dan Anak Pra-Sekolah | v1 | `CKG Balita dan Anak Pra-Sekolah` | 29 / 99 |  |
| 46 | CKG Dewasa Laki-laki | 1 versi | `CKG Dewasa Laki-laki` | 61 / 278 | ✅ |
| 47 | CKG Dewasa Perempuan | 1 versi | `CKG Dewasa Perempuan` | 66 / 299 | ✅ |
| 48 | CKG Lansia | 27 April 2026 (terbaru) | `CKG Lansia 27 April 2026` | 101 / 567 | ✅ |
| 48 | CKG Lansia | 2026 | `CKG Lansia 2026` | 82 / 366 |  |
| 48 | CKG Lansia | 2025 | `CKG Lansia 2025` | 80 / 361 |  |

SISMAL (Malaria): hanya form yang punya mapping yang dicatat di tracker (#64, #275); jenis form SISMAL lain tidak dimasukkan.

Baris #284–290 = sheet KuApps BidanKu di luar PYD (Tambah Pasien dst.), ditambahkan 2026-11-25 (nomor lanjut dari #283; di Google Sheet perlu ditambahkan manual).

SIM RS: 34 sheet sendiri + 18 baris yang memakai template Spheres = 52 dari 109 baris (#128–#236) sudah ada sheet mapping di `PHDT_Data_Rumah_Sakit.xlsx` (sheet Template generik tidak dihitung). Sisanya (Margono semua; Hepatitis Panti Nugroho/Nirmala/Harapan Ibu/Goetoeng/Tripat/Narmada/At tin; TB semua RS; DM/HT/Stroke yang tidak punya sheet; Tripat INC; Narmada ANC/PNC/BBL; dst.) belum ada file mapping. Kobo: 12 form dari `Kobo_-_Data_Dictionary.xlsx` dihitung (#83–86, #88–94, #101).

Catatan: Balita v2 = `Sheet9` adalah asumsi (perlu konfirmasi). Lansia 27 April 2026 belum punya blok lab (ServiceRequest / Specimen / DiagnosticReport / PractitionerRole) yang ada di 2025 dan 2026: terlewat, belum dimapping (konfirmasi 2026-11-24). Lansia punya QR terpisah (7 baris `QuestionnaireResponse.questionnaire`), jadi 7 QR dihitung. eKohort INC (#77) belum 100% termapping ke FHIR (konfirmasi 2026-11-24). Sheet `CKG Lansia (tidak dipakai)` tidak dihitung. Klaster Remaja (#45), eKohort PNC (#75), dan Laporan Kohort Ibu (#76) belum ada mapping. #43–#48 masih ada kolom Table BQ kosong.

| No | Sumber - Laporan | Masih diperlukan | Dimapping ke FHIR | Status review | Table BQ Purbalingga | Table BQ Lombok Barat |
|---|---|:-:|:-:|:-:|---|---|
| 1 | ePuskesmas - Pelayanan Pasien | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 2 | ePuskesmas - Pemeriksaan Medis (tidak dipakai lagi) | ❌ | ❌ | ❌ |  |  |
| 3 | ePuskesmas - Laporan Kunjungan Ibu Hamil | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 4 | ePuskesmas - Laporan Kohort KIA | ✅ | ❌ | ❌ |  |  |
| 5 | ePuskesmas - Laboratorium | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 6 | ePuskesmas - LPLPO (UKP6) | ✅ | ❌ | ❌ |  |  |
| 7 | ePuskesmas - Kinerja Puskesmas (tidak dipakai lagi) | ❌ | ❌ | ❌ |  |  |
| 8 | ePuskesmas - Rujukan Eksternal | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 9 | ePuskesmas - Kunjungan Pasien BPJS | ✅ | ✅ | ❌ |  |  |
| 10 | ePuskesmas - Kunjungan Pasien | ✅ | ✅ | ❌ |  |  |
| 11 | ePuskesmas (Laporan Pelayanan KIA Harian) - ANC | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 12 | ePuskesmas (Laporan Pelayanan KIA Harian) - INC | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 13 | ePuskesmas (Laporan Pelayanan KIA Harian) - PNC | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 14 | ePuskesmas (Laporan Pelayanan KIA Harian) - MTBS | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 15 | ePuskesmas (Laporan Pelayanan KIA Harian) - MTBM | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 16 | ePuskesmas (Laporan Pelayanan KIA Harian) - Tumbuh Kembang | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 17 | SiGizi - Posyandu Balita BNBA (daftar status gizi) | ✅ | ✅ | ⚠️ belum comprehensive review | `stellar-orb-451904-d9.raw_data.sigizi_balita_bnba` |  |
| 18 | SiGizi - Balita Vitamin A | ✅ | ✅ | ⚠️ belum comprehensive review | `stellar-orb-451904-d9.raw_data.sigizi_balita_vitamin_a` |  |
| 19 | SiGizi - Balita Mendapat PMT 2024 | ✅ | ✅ | ⚠️ belum comprehensive review | `stellar-orb-451904-d9.raw_data.sigizi_mendapat_pmt` |  |
| 20 | SiGizi - Balita Pemantauan PMT 2024 | ✅ | ✅ | ⚠️ belum comprehensive review | `stellar-orb-451904-d9.raw_data.sigizi_dipantau_pmt` |  |
| 21 | SiGizi - Asi Eksklusif | ✅ | ✅ | ⚠️ belum comprehensive review | `stellar-orb-451904-d9.raw_data.sigizi_asi_ekslusif` |  |
| 22 | SiGizi - Balita Pemantauan MPASI | ✅ | ✅ | ⚠️ belum comprehensive review | `stellar-orb-451904-d9.raw_data.sigizi_mpasi` |  |
| 23 | SiGizi - Daftar Balita | ✅ | ✅ | ❌ | `stellar-orb-451904-d9.raw_data.sigizi_daftar_balita` |  |
| 24 | SIGIZI (Balita BB Tidak Naik) - Pantau PMT 2025 | ✅ | ✅ | ⚠️ belum comprehensive review | `stellar-orb-451904-d9.raw_data.sigizi_balita_bb_tidak_naik_pantau_pmt_2025` |  |
| 25 | SIGIZI (Balita BB Tidak Naik) - Riwayat PMT 2025 | ✅ | ✅ | ⚠️ belum comprehensive review | `stellar-orb-451904-d9.raw_data.sigizi_balita_bb_tidak_naik_riwayat_pmt_2025` |  |
| 26 | SIGIZI (Balita BB Tidak Naik) - Survey PMT 2025 | ✅ | ✅ | ⚠️ belum comprehensive review | `stellar-orb-451904-d9.raw_data.sigizi_balita_bb_tidak_naik_survey_pmt_2025` |  |
| 27 | SIGIZI (Balita BB Kurang) - Pantau PMT 2025 | ✅ | ✅ | ⚠️ belum comprehensive review | `stellar-orb-451904-d9.raw_data.sigizi_balita_bb_kurang_pantau_pmt_2025` |  |
| 28 | SIGIZI (Balita BB Kurang) - Riwayat PMT 2025 | ✅ | ✅ | ⚠️ belum comprehensive review | `stellar-orb-451904-d9.raw_data.sigizi_balita_bb_kurang_riwayat_pmt_2025` |  |
| 29 | SIGIZI (Balita BB Kurang) - Survey PMT 2025 | ✅ | ✅ | ⚠️ belum comprehensive review | `stellar-orb-451904-d9.raw_data.sigizi_balita_bb_kurang_survey_pmt_2025` |  |
| 30 | SIGIZI (Balita Gizi Kurang) - Pantau PMT 2025 | ✅ | ✅ | ⚠️ belum comprehensive review | `stellar-orb-451904-d9.raw_data.sigizi_balita_gizi_kurang_pantau_pmt_2025` |  |
| 31 | SIGIZI (Balita Gizi Kurang) - Riwayat PMT 2025 | ✅ | ✅ | ⚠️ belum comprehensive review | `stellar-orb-451904-d9.raw_data.sigizi_balita_gizi_kurang_riwayat_pmt_2025` |  |
| 32 | SIGIZI (Balita Gizi Kurang) - Survey PMT 2025 | ✅ | ✅ | ⚠️ belum comprehensive review | `stellar-orb-451904-d9.raw_data.sigizi_balita_gizi_kurang_survey_pmt_2025` |  |
| 33 | SIGIZI IBU - Daftar Bumil | ✅ | ✅ | ❌ | `stellar-orb-451904-d9.raw_data.sigizi_daftar_bumil` |  |
| 34 | SIGIZI IBU - Daftar Nifas | ✅ | ✅ | ⚠️ belum comprehensive review | `stellar-orb-451904-d9.raw_data.sigizi_ibu_nifas` |  |
| 35 | SIGIZI IBU - Pengukuran ANC Bumil | ✅ | ✅ | ✅ | `stellar-orb-451904-d9.raw_data.sigizi_kesga_bumil_anc` |  |
| 36 | SIGIZI IBU - Kohort Ibu | ✅ | ✅ | ⚠️ belum comprehensive review | `stellar-orb-451904-d9.raw_data.sigizi_kohort_ibu` |  |
| 37 | SIGIZI IBU - Rekap 12T (tidak dipakai karena data agregat) | ❌ | ❌ | ❌ |  |  |
| 38 | SIGIZI IBU - Rekap PWS (hilang dari SIGIZI) | ❌ | ❌ | ❌ |  |  |
| 39 | ASIK - Data Individu Kohort Bayi | ✅ | ✅ | ⚠️ belum comprehensive review | `stellar-orb-451904-d9.raw_data.asik_laporan_layanan_imunisasi_test` |  |
| 40 | ASIK - Data Individu Kohort Baduta | ✅ | ✅ | ⚠️ belum comprehensive review | `stellar-orb-451904-d9.raw_data.asik_laporan_layanan_imunisasi_baduta` |  |
| 41 | ASIK - Data Individu Kohort WUS | ✅ | ✅ | ⚠️ belum comprehensive review | `stellar-orb-451904-d9.raw_data.asik_laporan_layanan_imunisasi_wus` |  |
| 42 | ASIK - Data Skrining PTM | ✅ | ✅ | ⚠️ belum comprehensive review | `stellar-orb-451904-d9.raw_data.asik_skrining_ptm` |  |
| 43 | ASIK - CKG-Klaster BBL | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 44 | ASIK - CKG-Klaster Balita Pra Sekolah | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 45 | ASIK - CKG-Klaster Remaja dan Usia Sekolah | ❌ | ✅ | ❌ |  |  |
| 46 | ASIK - CKG-Klaster Dewasa Laki-laki | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 47 | ASIK - CKG-Klaster Dewasa Perempuan | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 48 | ASIK - CKG-Klaster Lansia | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 49 | SiHepi - Form Rekap 3e | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 50 | SITB - TB 01 (Kartu Pengobatan Pasien) | ❌ | ✅ | ⚠️ belum comprehensive review |  |  |
| 51 | SITB - TB 02 (Kartu Identitas Pasien) | ❌ | ✅ | ⚠️ belum comprehensive review |  |  |
| 52 | SITB - TB 03 SO (Sensitif Obat) | ✅ | ✅ | ✅ | `stellar-orb-451904-d9.raw_data.sitb_tb_03` |  |
| 53 | SITB - TB 03 RO (Resisten Obat) | ✅ | ✅ | ✅ | `stellar-orb-451904-d9.raw_data.sitb_tb_03ro` |  |
| 54 | SITB - TB 04 Fasyankes (pemeriksaan lab) | ✅ | ✅ | ✅ | `stellar-orb-451904-d9.raw_data.sitb_tb_04_fasyankes` |  |
| 55 | SITB - TB 04 Rujukan (pemeriksaan lab) | ✅ | ✅ | ✅ | `stellar-orb-451904-d9.raw_data.sitb_tb_04_rujukan` |  |
| 56 | SITB - TB 06 (terduga/suspek TB) | ✅ | ✅ | ✅ | `stellar-orb-451904-d9.raw_data.sitb_tb_06` |  |
| 57 | SITB - TB 13 SO (Pemakaian Obat) | ✅ | ❌ | ❌ | `stellar-orb-451904-d9.raw_data.sitb_tb_13so` |  |
| 58 | SITB - TB 13 RO (Pemakaian Obat) | ✅ | ❌ | ❌ | `stellar-orb-451904-d9.raw_data.sitb_tb_13ro` |  |
| 59 | SITB - TB 14 Fasyankes (ketenagaan) | ✅ | ❌ | ❌ | `stellar-orb-451904-d9.raw_data.sitb_tb_14_fasyankes` |  |
| 60 | SITB - TB 15 (Pemeriksaan Eligibilitas TPT) | ❌ | ✅ | ⚠️ belum comprehensive review |  |  |
| 61 | SITB - TB 15P (Penerima TPT) | ❌ | ✅ | ⚠️ belum comprehensive review |  |  |
| 62 | SITB - TB 16K (IK) | ✅ | ✅ | ✅ | `stellar-orb-451904-d9.raw_data.sitb_tb_16k` |  |
| 63 | Data Absensi Pegawai - Dari tarikan fingerprint | ✅ | ❌ | ❌ |  |  |
| 64 | SISMAL (Malaria) - Regmal 1 | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 65 | ASPAK - Alat Kesehatan | ✅ | ❌ | ❌ |  |  |
| 66 | ASPAK - Sarana | ✅ | ❌ | ❌ |  |  |
| 67 | ASPAK - Prasarana | ✅ | ❌ | ❌ |  |  |
| 68 | ASPAK - Data Gedung | ✅ | ❌ | ❌ |  |  |
| 69 | ASPAK - Data Umum | ✅ | ❌ | ❌ |  |  |
| 70 | SMILE (oleh Dinkes) - Vaksinasi | ✅ | ❌ | ❌ | `stellar-orb-451904-d9.raw_data.smile_vaksinasi` |  |
| 71 | SMILE (oleh Dinkes) - ATM (HIV, AIDS, Malaria) | ✅ | ❌ | ❌ | `stellar-orb-451904-d9.raw_data.smile_atm` |  |
| 72 | MPDN (oleh Dinkes) - Laporan Kematian Bayi | ✅ | ✅ | ⚠️ belum comprehensive review | `stellar-orb-451904-d9.raw_data.mpdn_laporan_kematian_bayi` | `spheres-lombok-barat.raw_data.mpdn_laporan_kematian_bayi` |
| 73 | MPDN (oleh Dinkes) - Laporan Kematian Ibu | ✅ | ✅ | ⚠️ belum comprehensive review | `stellar-orb-451904-d9.raw_data.mpdn_laporan_kematian_ibu` | `spheres-lombok-barat.raw_data.mpdn_laporan_kematian_ibu` |
| 74 | eKohort (app sudah mati dari kemenkes) - Pelayanan Ibu ANC | ❌ | ✅ | ⚠️ belum comprehensive review |  |  |
| 75 | eKohort (app sudah mati dari kemenkes) - Pelayanan Ibu PNC | ❌ | ✅ | ❌ |  |  |
| 76 | eKohort (app sudah mati dari kemenkes) - Laporan Kohort Ibu | ❌ | ✅ | ❌ |  |  |
| 77 | eKohort (app sudah mati dari kemenkes) - Pelayanan Ibu Bersalin | ❌ | ✅ | ⚠️ belum comprehensive review |  |  |
| 78 | Informed Consent | ❌ | ✅ | ⚠️ belum comprehensive review |  |  |
| 79 | Buku KIA - Identitas dan ANC | ❌ | ✅ | ⚠️ belum comprehensive review |  |  |
| 80 | Buku KIA - INC | ❌ | ✅ | ⚠️ belum comprehensive review |  |  |
| 81 | Buku KIA - PNC | ❌ | ✅ | ⚠️ belum comprehensive review |  |  |
| 82 | Buku KIA - Anak | ❌ | ✅ | ⚠️ belum comprehensive review |  |  |
| 83 | Kobo - Modul ANC | ✅ | ✅ | ⚠️ belum comprehensive review | `stellar-orb-451904-d9.kobo_form.e-form_pencatatan_pelayanan_antenatal_care` |  |
| 84 | Kobo - Modul INC | ✅ | ✅ | ⚠️ belum comprehensive review | `stellar-orb-451904-d9.kobo_form.e-form_pencatatan_pelayanan_intranatal_care` |  |
| 85 | Kobo - Modul Neonatus | ✅ | ✅ | ⚠️ belum comprehensive review | `stellar-orb-451904-d9.kobo_form.e-form_pencatatan_bayi_neonatus` |  |
| 86 | Kobo - Modul PNC | ✅ | ✅ | ⚠️ belum comprehensive review | `stellar-orb-451904-d9.kobo_form.e-form_pencatatan_pelayanan_post_natal_care` |  |
| 87 | Kobo - Enumeration Form | ✅ | ❌ | ❌ |  |  |
| 88 | Kobo - Buku KIA 1 - ANC | ✅ | ✅ | ⚠️ belum comprehensive review | `stellar-orb-451904-d9.kobo_form.e-form_kia_anc` |  |
| 89 | Kobo - Buku KIA 2 - Luaran Kehamilan | ✅ | ✅ | ⚠️ belum comprehensive review | `stellar-orb-451904-d9.kobo_form.e-form_kia_luaran_kehamilan` |  |
| 90 | Kobo - Buku KIA 3 - PNC | ✅ | ✅ | ⚠️ belum comprehensive review | `stellar-orb-451904-d9.kobo_form.e-form_kia_pnc` |  |
| 91 | Kobo - Buku KIA 4 - Cadre | ✅ | ✅ | ⚠️ belum comprehensive review | `stellar-orb-451904-d9.kobo_form.e-form_kia_cadre` |  |
| 92 | Kobo - Buku KIA 5 - Vaksinatorku | ✅ | ✅ | ⚠️ belum comprehensive review | `stellar-orb-451904-d9.kobo_form.e-form_kia_vaccinator` |  |
| 93 | Kobo - Neonatus Outcome | ✅ | ✅ | ⚠️ belum comprehensive review | `stellar-orb-451904-d9.kobo_form.neonatus_outcome` |  |
| 94 | Kobo - Neonatus Outcome v2 | ✅ | ✅ | ⚠️ belum comprehensive review | `stellar-orb-451904-d9.kobo_form.neonatus_outcome_v2` |  |
| 95 | Kobo - PPIx Daily | ✅ | ❌ | ❌ | `stellar-orb-451904-d9.kobo_form.e-form_ppix_daily` |  |
| 96 | Kobo - PPIx Monthly | ✅ | ❌ | ❌ | `stellar-orb-451904-d9.kobo_form.e-form_ppix_monthly` |  |
| 97 | Kobo - POPIX | ✅ | ❌ | ❌ | `stellar-orb-451904-d9.kobo_form.e-form_popix` |  |
| 98 | Kobo - PrePOPIX | ✅ | ❌ | ❌ | `stellar-orb-451904-d9.kobo_form.e-form_prepopix` |  |
| 99 | Kobo - POPIX H 1 2 | ✅ | ❌ | ❌ | `stellar-orb-451904-d9.kobo_form.e-form_popix_H_1_2` |  |
| 100 | Kobo - SBPI | ✅ | ❌ | ❌ | `stellar-orb-451904-d9.kobo_form.e-form_sbpi` |  |
| 101 | Kobo - DDTK | ✅ | ✅ | ⚠️ belum comprehensive review | `stellar-orb-451904-d9.kobo_form.kobo-ddtk` |  |
| 102 | Kobo - Form Pendataan Kader | ✅ | ❌ | ❌ | `stellar-orb-451904-d9.kobo_form.e-form_data_kader` |  |
| 103 | Kobo - SDIDTK | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 104 | Kobo - Maternal Outcome | ✅ | ✅ | ✅ | `stellar-orb-451904-d9.kobo_form.e-form_maternal_outcome` |  |
| 105 | Kobo - Raffle | ❌ | ✅ | ✅ | `stellar-orb-451904-d9.kobo_form.e-form_kobo_raffle` |  |
| 106 | KuApps New - BidanKu: ANC | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 107 | KuApps New - BidanKu: PNC | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 108 | KuApps New - BidanKu: BBL | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 109 | KuApps New - BidanKu: Bayi | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 110 | KuApps New - BidanKu: Anak | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 111 | KuApps New - BidanKu: Anak Usia Sekolah dan Remaja | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 112 | KuApps New - BidanKu: Dewasa | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 113 | KuApps New - BidanKu: Lansia | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 114 | Kuapps Spheres - HT | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 115 | Kuapps Spheres - DM | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 116 | Kuapps Spheres - TB | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 117 | GSI Labs - Lab Test | ✅ | ✅ | ❌ |  |  |
| 118 | Genomics - TB | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 119 | Genomics - Klebsiella | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 120 | Genomics - Dengue | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 121 | ELSMIL (BKKBN) - Ibu Hamil | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 122 | ELSMIL (BKKBN) - Pasca Persalinan | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 123 | ELSMIL (BKKBN) - Baduta | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 124 | Dapodik - PAUD (semester) | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 125 | Dapodik - Antropometri DDTK (monthly) | ✅ | ✅ | ❌ |  |  |
| 126 | SIGA - Balita (BKB - K0) | ✅ | ❌ | ❌ |  |  |
| 127 | SIGA - Balita (BKB - R1) | ✅ | ❌ | ❌ |  |  |
| 128 | SIM RS Data - At tin ANC | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 129 | SIM RS Data - At tin INC | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 130 | SIM RS Data - At tin PNC | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 131 | SIM RS Data - At tin BBL | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 132 | SIM RS Data - At tin Hepatitis | ✅ | ✅ | ❌ |  |  |
| 133 | SIM RS Data - At tin Diabetes Melitus | ✅ | ✅ | ❌ |  |  |
| 134 | SIM RS Data - At tin Hipertensi | ✅ | ✅ | ❌ |  |  |
| 135 | SIM RS Data - At tin Stroke | ✅ | ✅ | ❌ |  |  |
| 136 | SIM RS Data - At tin TB | ✅ | ✅ | ❌ |  |  |
| 137 | SIM RS Data - Harapan Ibu ANC | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 138 | SIM RS Data - Harapan Ibu INC | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 139 | SIM RS Data - Harapan Ibu PNC | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 140 | SIM RS Data - Harapan Ibu BBL | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 141 | SIM RS Data - Harapan Ibu Hepatitis | ✅ | ✅ | ❌ |  |  |
| 142 | SIM RS Data - Harapan Ibu Diabetes Melitus | ✅ | ✅ | ❌ |  |  |
| 143 | SIM RS Data - Harapan Ibu Hipertensi | ✅ | ✅ | ❌ |  |  |
| 144 | SIM RS Data - Harapan Ibu Stroke | ✅ | ✅ | ❌ |  |  |
| 145 | SIM RS Data - Harapan Ibu TB | ✅ | ✅ | ❌ |  |  |
| 146 | SIM RS Data - Siaga Medika ANC | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 147 | SIM RS Data - Siaga Medika INC | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 148 | SIM RS Data - Siaga Medika PNC | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 149 | SIM RS Data - Siaga Medika BBL | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 150 | SIM RS Data - Siaga Medika Hepatitis | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 151 | SIM RS Data - Siaga Medika Diabetes Melitus | ✅ | ✅ | ❌ |  |  |
| 152 | SIM RS Data - Siaga Medika Hipertensi | ✅ | ✅ | ❌ |  |  |
| 153 | SIM RS Data - Siaga Medika Stroke | ✅ | ✅ | ❌ |  |  |
| 154 | SIM RS Data - Siaga Medika TB | ✅ | ✅ | ❌ |  |  |
| 155 | SIM RS Data - MPH ANC | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 156 | SIM RS Data - MPH INC | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 157 | SIM RS Data - MPH PNC | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 158 | SIM RS Data - MPH BBL | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 159 | SIM RS Data - MPH Hepatitis | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 160 | SIM RS Data - MPH Diabetes Melitus | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 161 | SIM RS Data - MPH Hipertensi | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 162 | SIM RS Data - MPH Stroke | ✅ | ✅ | ❌ |  |  |
| 163 | SIM RS Data - MPH TB | ✅ | ✅ | ❌ |  |  |
| 164 | SIM RS Data - Nirmala ANC | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 165 | SIM RS Data - Nirmala INC | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 166 | SIM RS Data - Nirmala PNC | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 167 | SIM RS Data - Nirmala BBL | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 168 | SIM RS Data - Nirmala Hepatitis | ✅ | ✅ | ❌ |  |  |
| 169 | SIM RS Data - Nirmala Diabetes Melitus | ✅ | ✅ | ❌ |  |  |
| 170 | SIM RS Data - Nirmala Hipertensi | ✅ | ✅ | ❌ |  |  |
| 171 | SIM RS Data - Nirmala Stroke | ✅ | ✅ | ❌ |  |  |
| 172 | SIM RS Data - Nirmala TB | ✅ | ✅ | ❌ |  |  |
| 173 | SIM RS Data - Ummu Hani ANC | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 174 | SIM RS Data - Ummu Hani INC | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 175 | SIM RS Data - Ummu Hani PNC | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 176 | SIM RS Data - Ummu Hani BBL | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 177 | SIM RS Data - Ummu Hani Hepatitis | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 178 | SIM RS Data - Ummu Hani Diabetes Melitus | ✅ | ✅ | ❌ |  |  |
| 179 | SIM RS Data - Ummu Hani Hipertensi | ✅ | ✅ | ❌ |  |  |
| 180 | SIM RS Data - Ummu Hani Stroke | ✅ | ✅ | ❌ |  |  |
| 181 | SIM RS Data - Ummu Hani TB | ✅ | ✅ | ❌ |  |  |
| 182 | SIM RS Data - PKU ANC | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 183 | SIM RS Data - PKU INC | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 184 | SIM RS Data - PKU PNC | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 185 | SIM RS Data - PKU BBL | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 186 | SIM RS Data - PKU Hepatitis | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 187 | SIM RS Data - PKU Diabetes Melitus | ✅ | ✅ | ❌ |  |  |
| 188 | SIM RS Data - PKU Hipertensi | ✅ | ✅ | ❌ |  |  |
| 189 | SIM RS Data - PKU Stroke | ✅ | ✅ | ❌ |  |  |
| 190 | SIM RS Data - PKU TB | ✅ | ✅ | ❌ |  |  |
| 191 | SIM RS Data - Goetoeng ANC | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 192 | SIM RS Data - Goetoeng INC | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 193 | SIM RS Data - Goetoeng PNC | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 194 | SIM RS Data - Goetoeng BBL | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 195 | SIM RS Data - Goetoeng Hepatitis | ✅ | ✅ | ❌ |  |  |
| 196 | SIM RS Data - Goetoeng Diabetes Melitus | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 197 | SIM RS Data - Goetoeng Hipertensi | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 198 | SIM RS Data - Goetoeng Stroke | ✅ | ✅ | ❌ |  |  |
| 199 | SIM RS Data - Goetoeng TB | ✅ | ✅ | ❌ |  |  |
| 200 | SIM RS Data - Panti Nugroho ANC | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 201 | SIM RS Data - Panti Nugroho INC | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 202 | SIM RS Data - Panti Nugroho PNC | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 203 | SIM RS Data - Panti Nugroho BBL | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 204 | SIM RS Data - Panti Nugroho Hepatitis | ✅ | ✅ | ❌ |  |  |
| 205 | SIM RS Data - Panti Nugroho Diabetes Melitus | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 206 | SIM RS Data - Panti Nugroho Hipertensi | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 207 | SIM RS Data - Panti Nugroho Stroke | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 208 | SIM RS Data - Panti Nugroho TB | ✅ | ✅ | ❌ |  |  |
| 209 | SIM RS Data - Margono ANC | ✅ | ✅ | ❌ |  |  |
| 210 | SIM RS Data - Margono INC | ✅ | ✅ | ❌ |  |  |
| 211 | SIM RS Data - Margono PNC | ✅ | ✅ | ❌ |  |  |
| 212 | SIM RS Data - Margono BBL | ✅ | ✅ | ❌ |  |  |
| 213 | SIM RS Data - Margono Hepatitis | ✅ | ✅ | ❌ |  |  |
| 214 | SIM RS Data - Margono Diabetes Melitus | ✅ | ✅ | ❌ |  |  |
| 215 | SIM RS Data - Margono Hipertensi | ✅ | ✅ | ❌ |  |  |
| 216 | SIM RS Data - Margono Stroke | ✅ | ✅ | ❌ |  |  |
| 217 | SIM RS Data - Margono TB | ✅ | ✅ | ❌ |  |  |
| 218 | SIM RS Data - Narmada ANC | ✅ | ✅ | ❌ |  |  |
| 219 | SIM RS Data - Narmada INC | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 220 | SIM RS Data - Narmada PNC | ✅ | ✅ | ❌ |  |  |
| 221 | SIM RS Data - Narmada BBL | ✅ | ✅ | ❌ |  |  |
| 222 | SIM RS Data - Narmada KIA | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 223 | SIM RS Data - Narmada Hepatitis | ✅ | ✅ | ❌ |  |  |
| 224 | SIM RS Data - Narmada Diabetes Melitus | ✅ | ✅ | ❌ |  |  |
| 225 | SIM RS Data - Narmada Hipertensi | ✅ | ✅ | ❌ |  |  |
| 226 | SIM RS Data - Narmada Stroke | ✅ | ✅ | ❌ |  |  |
| 227 | SIM RS Data - Narmada TB | ✅ | ✅ | ❌ |  |  |
| 228 | SIM RS Data - Tripat ANC | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 229 | SIM RS Data - Tripat INC | ✅ | ✅ | ❌ |  |  |
| 230 | SIM RS Data - Tripat PNC | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 231 | SIM RS Data - Tripat BBL | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 232 | SIM RS Data - Tripat Hepatitis | ✅ | ✅ | ❌ |  |  |
| 233 | SIM RS Data - Tripat Diabetes Melitus | ✅ | ✅ | ❌ |  |  |
| 234 | SIM RS Data - Tripat Hipertensi | ✅ | ✅ | ❌ |  |  |
| 235 | SIM RS Data - Tripat Stroke | ✅ | ✅ | ❌ |  |  |
| 236 | SIM RS Data - Tripat TB | ✅ | ✅ | ❌ |  |  |
| 237 | SIPTM | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 275 | SISMAL (Malaria) - Validasi Kasus Indigenous | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 284 | KuApps New - BidanKu: Tambah Pasien | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 285 | KuApps New - BidanKu: Daftar Kehamilan | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 286 | KuApps New - BidanKu: Luaran Kehamilan | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 287 | KuApps New - BidanKu: PHBS | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 288 | KuApps New - BidanKu: Skrining Rumah Tangga | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 289 | KuApps New - BidanKu: Imunisasi | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 290 | KuApps New - BidanKu: Kumpulan Skrinning | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 291 | MMS - Pemantauan Distribusi dan Konsumsi | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 292 | MMS - Informed Consent | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 293 | MMS - Master Database Responden | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 294 | MMS - Survei Sosio Ekonomi | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 295 | MMS - Survei Demografi (Listing Responden) | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
| 296 | MMS - Konfirmasi Kelahiran dan Luaran Kehamilan | ✅ | ✅ | ⚠️ belum comprehensive review |  |  |
