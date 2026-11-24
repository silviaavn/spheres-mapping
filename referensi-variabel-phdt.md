# Referensi Jumlah Variabel per Form (PHDT Data Dictionary)

Terakhir diperbarui: 2026-11-24
Aturan pemakaian: lihat [`aturan.md`](aturan.md) bagian "Referensi jumlah variabel PHDT".

Daftar ini berasal dari **PHDT Data Dictionary** (kolom "Number of variables"). Dipakai sebagai **angka pembanding** untuk form yang akan dikerjakan: jumlah variabel di mapping/file mentah dibandingkan dengan angka di sini. Angka di output utama ([`output.md`](output.md)) tetap yang dipakai.

## Tally form yang sudah ada di output utama

Kolom **Variabel raw** = angka di `output.md`. Kolom **PHDT** = angka di daftar bawah.

| Form di output utama | Baris di daftar PHDT | Variabel raw | PHDT | Selisih | Status |
|---|---|---|---|---|---|
| Maternal Outcome | Kobo - Maternal Outcome | 12 | 12 | 0 | ✅ cocok |
| SITB TB 03 RO | SITB - TB 03 RO (register TB) | 144 | 144 | 0 | ✅ cocok |
| SITB TB 04 (Fasyankes & Rujukan) | SITB - TB 04 rujukan / TB 04 fasyankes | 114 | 114 / 114 | 0 | ✅ cocok |
| MPDN Kematian Bayi | MPDN - Kematian Bayi | 37 | 37 | 0 | ✅ cocok |
| MPDN Kematian Ibu | MPDN - Kematian Ibu | 24 | 24 | 0 | ✅ cocok |
| SiGizi ANC | SiGizi - Bumil Kesga | 49 | 45 | +4 | ⚠️ beda, penyebab belum diketahui |
| SITB TB 06 | SITB - TB 06 (suspect TB) | 96 | 69 | +27 | ⚠️ beda (dugaan: kolom SITB yang di-skip di PHDT) |
| SITB TB 03 SO | SITB - TB 03 SO (register TB) | 84 | 75 | +9 | ⚠️ beda (dugaan: kolom SITB yang di-skip di PHDT) |
| SITB TB 16K | SITB - TB 16K | 40 | 24 | +16 | ⚠️ beda (dugaan: kolom SITB yang di-skip di PHDT) |
| Raffle | (tidak ada di daftar) | 12 | – | – | ➖ belum bisa dibandingkan |
| ePus pelayanan | ePuskesmas - Pelayanan | 81 | 80 | +1 | ⚠️ beda (belum dijelaskan) |
| ePus kunjungan-ibu-hamil | ePuskesmas - KIA | 68 | 97 | -29 | ⚠️ beda (belum dijelaskan) |
| ePus lab | ePuskesmas - Laboratorium | 22 | 23 | -1 | ⚠️ beda (belum dijelaskan) |
| ePus rujukan-eksternal | ePuskesmas - Rujukan | 23 | 22 | +1 | ⚠️ beda (belum dijelaskan) |
| ePus anc | ePuskesmas - ANC - Ibu Hamil | 123 | 136 | -13 | ⚠️ beda (belum dijelaskan) |
| ePus inc | ePuskesmas - INC - Persalinan | 93 | 82 | +11 | ⚠️ beda (belum dijelaskan) |
| ePus pnc | ePuskesmas - PNC - Ibu Nifas | 107 | 96 | +11 | ⚠️ beda (belum dijelaskan) |
| ePus mtbs | ePuskesmas - MTBS | 187 | 187 | +0 | ✅ cocok |
| ePus mtbm | ePuskesmas - MTBM | 105 | 115 | -10 | ⚠️ beda (belum dijelaskan) |
| ePus tumbang-anak | ePuskesmas - Tumbang - Anak | 34 | 34 | +0 | ✅ cocok |
| ePus tumbang-ddtk | ePuskesmas - Tumbang - DDTK | 38 | 38 | +0 | ✅ cocok |
| ePus tumbang-kpsp | ePuskesmas - Tumbang - KPSP | 123 (baris 141) | 140 | +1 (baris) | ⚠️ baris +1 |
| ePus tumbang-tdd | ePuskesmas - Tumbang - TDD | 37 (baris 48) | 48 | +0 (baris) | ✅ baris cocok |
| ePus tumbang-tdl | ePuskesmas - Tumbang - TDL | 6 (baris 21) | 21 | +0 (baris) | ✅ baris cocok |
| ePus tumbang-kmpe | ePuskesmas - Tumbang - KMPE | 14 (baris 14) | 14 | +0 (baris) | ✅ baris cocok |
| ePus tumbang-mchat | ePuskesmas - Tumbang - M-CHAT-R | 20 (baris 20) | 20 | +0 (baris) | ✅ baris cocok |
| ePus tumbang-gpph | ePuskesmas - Tumbang - GPPH | 10 (baris 10) | 10 | +0 (baris) | ✅ baris cocok |
| dapodik-paud | Dapodik - PAUD (semester) | 75 (baris 87) | 93 | −6 (baris) | ⚠️ baris −6 |
| sitb-tb01 | SITB - TB 01 | 82 (baris 88) | 78 | 10 (baris) | ⚠️ belum review |
| sitb-tb02 | SITB - TB 02 | 22 (baris 22) | 22 | 0 (baris) | ⚠️ belum review |
| elsmil-ibu-hamil | ELSMIL - Ibu Hamil | 36 (baris 37) | 37 | 0 (baris) | ⚠️ belum review |
| elsmil-pasca-persalinan | ELSMIL - Pasca Persalinan | 29 (baris 29) | 29 | 0 (baris) | ⚠️ belum review |
| elsmil-baduta | ELSMIL - Baduta | 38 (baris 45) | 42 | 3 (baris) | ⚠️ belum review |
| siptm | SIPTM (baru, tidak ada di PHDT) | 60 (baris 60) | – | dihitung dari mapping | ⚠️ belum review |
| asik-skrining-ptm | ASIK - Data Skrining PTM | 67 (baris 89) | 64 | 25 (baris) | ⚠️ belum review |
| asik-ckg-bbl | ASIK - CKG - Bayi Baru Lahir (v2; v1: 33 / 33) | 35 (baris 35) | 33 | 2 (baris) | ⚠️ belum review |
| asik-ckg-balita | ASIK - CKG Balita dan Anak Pra-Sekolah (v2; v1: 62 / 63) | 57 (baris 58) | 59 | −1 (baris) | ⚠️ belum review |
| asik-ckg-dewasa-laki | ASIK - CKG - Dewasa Laki-laki | 123 (baris 132) | 132 | 0 (baris) | ⚠️ belum review |
| asik-ckg-dewasa-perempuan | ASIK - CKG - Dewasa Perempuan | 130 (baris 139) | 132 | 7 (baris) | ⚠️ belum review |
| asik-ckg-lansia | ASIK - CKG - Lansia (27 Apr 2026; 2026: 188 / 197, 2025: 186 / 195) | 188 (baris 204) | 180 | 24 (baris) | ⚠️ belum review |
| informed-consent | Informed Consent | 27 (baris 28) | 28 | 0 (baris) | ⚠️ belum review |
| sihepi-rekap-3e | SIHEPI - Rekap 3e | 93 (baris 115) | 115 | 0 (baris) | ⚠️ belum review |
| ekohort-anc | eKohort - ANC (Final Format) | 34 (baris 34) | 36 | −2 (baris) | ⚠️ belum review |
| ekohort-inc | eKohort - INC | 84 (baris 85) | 85 | 0 (baris) | ⚠️ belum review |

Keputusan (2026-11-24): selisih di SITB dianggap wajar karena sebelumnya banyak kolom SITB yang di-skip di PHDT Data Dictionary (dugaan, belum dicek per kolom). **Angka output utama tidak diubah.** Selisih SiGizi ANC (+4) belum dijelaskan.

## Daftar lengkap (PHDT Data Dictionary)

Sel kosong = jumlah variabel belum diisi di sumber. Angka 0 = sumber mencatat 0 variabel. Kolom Sumber diisi ulang ke bawah (di daftar asli hanya baris pertama tiap sumber yang terisi). Baris kosong di daftar asli dibuang. Baris `Tumbang - KPSP` sampai `GPPH` menjorok di daftar asli (sub-form).

| Sumber | Form / kategori | Jumlah variabel |
|---|---|---|
| Dinas Kesehatan |  |  |
| ePuskesmas | Pelayanan | 80 |
| ePuskesmas | Laboratorium | 23 |
| ePuskesmas | KIA | 97 |
| ePuskesmas | Rujukan | 22 |
| ePuskesmas | MTBS and MTBM | 261 |
| ePuskesmas | Tumbang - Anak | 34 |
| ePuskesmas | Tumbang - DDTK | 38 |
| ePuskesmas | Tumbang - KPSP | 140 |
| ePuskesmas | Tumbang - TDD | 48 |
| ePuskesmas | Tumbang - TDL | 21 |
| ePuskesmas | Tumbang - KMPE | 14 |
| ePuskesmas | Tumbang - M-CHAT-R | 20 |
| ePuskesmas | Tumbang - GPPH | 10 |
| ePuskesmas | Manual Dump Export |  |
| ePuskesmas | ANC - Ibu Hamil | 136 |
| ePuskesmas | INC - Persalinan | 82 |
| ePuskesmas | PNC - Ibu Nifas | 96 |
| ePuskesmas | MTBM | 115 |
| ePuskesmas | MTBS | 187 |
| SiGizi | Bumil Kesga | 45 |
| SiGizi | Balita Tumbang (BNBA) | 34 |
| SiGizi | Balita ASI Ekslusif | 22 |
| SiGizi | Balita MPASI | 28 |
| SiGizi | Balita PMT | 49 |
| SiGizi | Balita PMT 2025 | 154 |
| SiGizi | Balita Vitamin A | 32 |
| SiGizi | Ibu Nifas | 57 |
| Format XLS | Bumil |  |
| Format XLS | Bayi/ Balita - Antropometri | 43 |
| Hospital XLS | ANC | 76 |
| Hospital XLS | INC - Ibu | 81 |
| Hospital XLS | INC - Bayi | 47 |
| Hospital XLS | PNC | 87 |
| Hospital XLS | Neonatus | 45 |
| eKohort | ANC | 36 |
| eKohort | INC | 85 |
| MPDN | Kematian Ibu | 24 |
| MPDN | Kematian Bayi | 37 |
| ASIK | Imunisasi Bayi | 117 |
| ASIK | Imunisasi Baduta | 26 |
| ASIK | Imunisasi WUS | 41 |
| ASIK | Skrining PTM | 64 |
| ASIK | CKG - Lansia | 180 |
| ASIK | CKG - Dewasa Laki-laki | 132 |
| ASIK | CKG - Dewasa Perempuan | 132 |
| ASIK | CKG Balita dan Anak Pra-Sekolah | 59 |
| ASIK | CKG - Bayi Baru Lahir | 33 |
| Informed Consent | Informed Consent | 28 |
| Master Data | Organization | 40 |
| (MSI, MNI, SISDMK, MIcrosite) | Location | 26 |
| (MSI, MNI, SISDMK, MIcrosite) | Practitioner | 10 |
| (MSI, MNI, SISDMK, MIcrosite) | PractitionerRole | 18 |
| Buku KIA | Evaluasi Kehamilan | 80 |
| Buku KIA | Identitas+ANC | 296 |
| Buku KIA | INC | 58 |
| Buku KIA | PNC | 17 |
| Buku KIA | Anak | 267 |
| SITB | TB 06 (suspect TB) | 69 |
| SITB | TB 03 SO (register TB) | 75 |
| SITB | TB 03 RO (register TB) | 144 |
| SITB | TB 16K | 24 |
| SITB | TB 04 rujukan | 114 |
| SITB | TB 04 fasyankes | 114 |
| SITB | TB 15 | 28 |
| SITB | TB 15P | 37 |
| SITB | TB 01 (Kartu Pasien) | 78 |
| SITB | TB 02 | 22 |
| Kobo | Modul ANC | 82 |
| Kobo | Modul INC | 67 |
| Kobo | Modul Neonatus | 37 |
| Kobo | Modul PNC | 132 |
| Kobo | Enumeration Form | 24 |
| Kobo | Buku KIA 1 - ANC | 418 |
| Kobo | Buku KIA 2 - Luaran Kehamilan | 50 |
| Kobo | Buku KIA 3 - PNC | 161 |
| Kobo | Buku KIA 4 - Cadre | 84 |
| Kobo | Buku KIA 5 - Vaksinatorku | 77 |
| Kobo | Neonatus Outcome | 31 |
| Kobo | PPIx Daily | 31 |
| Kobo | PPIx Monthly | 189 |
| Kobo | POPIX | 487 |
| Kobo | DDTK | 20 |
| Kobo | Form Pendataan Kader | 74 |
| Kobo | SDIDTK |  |
| Kobo | Maternal Outcome | 12 |
| SIHEPI | Rekap 3e | 115 |
| KuApps - BidanKu | ANC | 404 |
| KuApps - BidanKu | PNC | 128 |
| KuApps - BidanKu | INC - Ibu | 79 |
| KuApps - BidanKu | INC - Bayi Baru Lahir | 40 |
| KuApps - BidanKu | Neonatus | 128 |
| KuApps - BidanKu | Neonatus Outcome | 34 |
| KuApps - ILP (Posyandu) |  |  |
| KuApps - ILP (Kunjungan Rumah) |  |  |
| GSI Labs | Lab Test | 492 |
| Genomics | TB use case | 127 |
| Genomics | Klebsiella | 38 |
| Genomics | Dengue | 58 |
| Intersectoral |  |  |
| ELSMIL (BKKBN) | Ibu Hamil | 37 |
| ELSMIL (BKKBN) | Pasca Persalinan | 29 |
| ELSMIL (BKKBN) | Baduta | 42 |
| Dapodik | PAUD (semester) | 93 |
| Dapodik | Antropometri DDTK (monthly) | 37 |
| SIPTM |  | (dihitung dari mapping: 60 unik / 60 baris; belum ada angka PHDT) |
| SIGA | Balita (BKB - K0) | 0 |
| SIGA | Balita (BKB - R1) | 0 |
| SIM RS Data | At tin ANC | 76 |
| SIM RS Data | At tin INC | 81 |
| SIM RS Data | At tin PNC | 47 |
| SIM RS Data | At tin BBL | 87 |
| SIM RS Data | At tin Hepatitis | 0 |
| SIM RS Data | At tin Diabetes Melitus | 0 |
| SIM RS Data | At tin Hipertensi | 0 |
| SIM RS Data | At tin Stroke | 0 |
| SIM RS Data | At tin TB |  |
| SIM RS Data | Harapan Ibu ANC | 76 |
| SIM RS Data | Harapan Ibu INC | 81 |
| SIM RS Data | Harapan Ibu PNC | 47 |
| SIM RS Data | Harapan Ibu BBL | 87 |
| SIM RS Data | Harapan Ibu Hepatitis | 0 |
| SIM RS Data | Harapan Ibu Diabetes Melitus | 36 |
| SIM RS Data | Harapan Ibu Hipertensi | 36 |
| SIM RS Data | Harapan Ibu Stroke | 36 |
| SIM RS Data | Harapan Ibu TB | 16 |
| SIM RS Data | Siaga Medika ANC | 75 |
| SIM RS Data | Siaga Medika INC | 67 |
| SIM RS Data | Siaga Medika PNC | 49 |
| SIM RS Data | Siaga Medika BBL | 72 |
| SIM RS Data | Siaga Medika Hepatitis | 0 |
| SIM RS Data | Siaga Medika Diabetes Melitus | 0 |
| SIM RS Data | Siaga Medika Hipertensi | 0 |
| SIM RS Data | Siaga Medika Stroke | 0 |
| SIM RS Data | Siaga Medika TB |  |
| SIM RS Data | MPH ANC | 45 |
| SIM RS Data | MPH INC | 55 |
| SIM RS Data | MPH PNC | 60 |
| SIM RS Data | MPH BBL | 73 |
| SIM RS Data | MPH Hepatitis | 0 |
| SIM RS Data | MPH Diabetes Melitus | 52 |
| SIM RS Data | MPH Hipertensi | 34 |
| SIM RS Data | MPH Stroke | 0 |
| SIM RS Data | MPH TB | 0 |
| SIM RS Data | Nirmala ANC | 76 |
| SIM RS Data | Nirmala INC | 81 |
| SIM RS Data | Nirmala PNC | 47 |
| SIM RS Data | Nirmala BBL | 87 |
| SIM RS Data | Nirmala Hepatitis | 0 |
| SIM RS Data | Nirmala Diabetes Melitus | 0 |
| SIM RS Data | Nirmala Hipertensi | 0 |
| SIM RS Data | Nirmala Stroke | 0 |
| SIM RS Data | Nirmala TB |  |
| SIM RS Data | Ummu Hani ANC | 35 |
| SIM RS Data | Ummu Hani INC | 53 |
| SIM RS Data | Ummu Hani PNC | 67 |
| SIM RS Data | Ummu Hani BBL | 0 |
| SIM RS Data | Ummu Hani Hepatitis | 0 |
| SIM RS Data | Ummu Hani Diabetes Melitus | 0 |
| SIM RS Data | Ummu Hani Hipertensi | 0 |
| SIM RS Data | Ummu Hani Stroke | 0 |
| SIM RS Data | Ummu Hani TB |  |
| SIM RS Data | PKU ANC | 76 |
| SIM RS Data | PKU INC | 81 |
| SIM RS Data | PKU PNC | 47 |
| SIM RS Data | PKU BBL | 87 |
| SIM RS Data | PKU Hepatitis | 0 |
| SIM RS Data | PKU Diabetes Melitus | 0 |
| SIM RS Data | PKU Hipertensi | 0 |
| SIM RS Data | PKU Stroke | 0 |
| SIM RS Data | PKU TB |  |
| SIM RS Data | Goetoeng ANC | 23 |
| SIM RS Data | Goetoeng INC | 35 |
| SIM RS Data | Goetoeng PNC | 27 |
| SIM RS Data | Goetoeng BBL | 35 |
| SIM RS Data | Goetoeng Hepatitis | 0 |
| SIM RS Data | Goetoeng Diabetes Melitus | 11 |
| SIM RS Data | Goetoeng Hipertensi | 12 |
| SIM RS Data | Goetoeng Stroke | 0 |
| SIM RS Data | Goetoeng TB | 0 |
| SIM RS Data | Panti Nugroho ANC | 56 |
| SIM RS Data | Panti Nugroho INC | 56 |
| SIM RS Data | Panti Nugroho PNC | 89 |
| SIM RS Data | Panti Nugroho BBL | 50 |
| SIM RS Data | Panti Nugroho Hepatitis | 0 |
| SIM RS Data | Panti Nugroho Diabetes Melitus | 19 |
| SIM RS Data | Panti Nugroho Hipertensi | 41 |
| SIM RS Data | Panti Nugroho Stroke | 35 |
| SIM RS Data | Panti Nugroho TB | 17 |
| SIM RS Data | Margono ANC | 0 |
| SIM RS Data | Margono INC | 0 |
| SIM RS Data | Margono PNC | 0 |
| SIM RS Data | Margono BBL | 0 |
| SIM RS Data | Margono Hepatitis | 0 |
| SIM RS Data | Margono Diabetes Melitus | 0 |
| SIM RS Data | Margono Hipertensi | 0 |
| SIM RS Data | Margono Stroke | 0 |
| SIM RS Data | Margono TB |  |
| SIM RS Data | Narmada ANC |  |
| SIM RS Data | Narmada INC |  |
| SIM RS Data | Narmada PNC |  |
| SIM RS Data | Narmada BBL |  |
| SIM RS Data | Narmada KIA |  |
| SIM RS Data | Narmada Hepatitis |  |
| SIM RS Data | Narmada Diabetes Melitus |  |
| SIM RS Data | Narmada Hipertensi |  |
| SIM RS Data | Narmada Stroke |  |
| SIM RS Data | Narmada TB |  |
| SIM RS Data | Tripat ANC | 31 |
| SIM RS Data | Tripat INC |  |
| SIM RS Data | Tripat PNC | 36 |
| SIM RS Data | Tripat BBL | 36 |
| SIM RS Data | Tripat Hepatitis |  |
| SIM RS Data | Tripat Diabetes Melitus |  |
| SIM RS Data | Tripat Hipertensi |  |
| SIM RS Data | Tripat Stroke |  |
| SIM RS Data | Tripat TB |  |

## Log perubahan
- 2026-11-24: Tally ditambah 9 form (ASIK CKG BBL, Balita, Dewasa Laki-laki, Dewasa Perempuan, Lansia; Informed Consent; SIHEPI Rekap 3e; eKohort ANC, INC). Selisih baris: BBL +2, Balita −1, Dewasa Perempuan +7, Lansia +24, eKohort ANC −2; lainnya cocok. Versi lama CKG tidak ditambahkan. Angka output utama tidak diubah.
- 2026-11-24: Tally ditambah 6 form Tumbuh Kembang (KPSP, TDD, TDL, KMPE, M-CHAT-R, GPPH): jumlah baris variabel cocok dengan PHDT (KPSP +1), variabel unik lebih kecil karena pertanyaan berulang antar kelompok umur. Belum comprehensive review.
- 2026-11-24: Tally ditambah 11 form ePuskesmas (belum comprehensive review): cocok = MTBS, Tumbang Anak, Tumbang DDTK; beda = Pelayanan +1, Kunjungan Ibu Hamil −29, Lab −1, Rujukan +1, ANC −13 (baris 136 = PHDT), INC +11, PNC +11, MTBM −10. Angka output utama tidak diubah.
- 2026-11-24: Dibuat dari daftar PHDT Data Dictionary (216 baris berisi). Tally 9 form di output utama: 5 cocok, 4 beda (SiGizi ANC, TB 06, TB 03 SO, TB 16K), Raffle tidak ada di daftar.
- 2026-11-24: Tally ditambah Dapodik PAUD (sheet `Copy of DAPODIK`, dipilih user): 75 variabel unik / 87 baris vs PHDT 93 (−6 baris), angka output utama tidak diubah.
- 2026-11-24: Tally ditambah 7 form dari 5 CSV (TB 01, TB 02, Elsmil x3, SIPTM, ASIK PTM). SIPTM tidak ada di daftar PHDT: ditambahkan baris baru, jumlah variabel dihitung dari mapping (60). Angka output utama tidak diubah.
