# Frekuensi Code (lintas form)

Bagian dari konsolidasi [`output.md`](output.md). Dibuat otomatis, jangan diedit manual. Lihat juga [`frekuensi-payload.md`](frekuensi-payload.md).

Frekuensi = di berapa form code (code + CodeSystem) dipakai; angka (Nx) = muncul N kali di form itu.

| # | Code | Display | CodeSystem | Dipakai di form | Frekuensi |
|---|---|---|---|---|---|
| 1 | 223366009 | Healthcare professional | snomed | Maternal Outcome, SITB TB 03 SO, SITB TB 03 RO, SISMAL Regmal 1 | 4 |
| 2 | SP000396 | Data entry staff | kemkes sp | Maternal Outcome | 1 |
| 3 | SP000397 | Field/call center staff | kemkes sp | Maternal Outcome | 1 |
| 4 | SP000738 | Kunjungan pemantauan luaran maternal | kemkes sp | Maternal Outcome | 1 |
| 5 | ANC | Antenatal Care | episodeofcare-type | Maternal Outcome, Raffle, SiGizi ANC, ePus Kunjungan Ibu Hamil, ePus INC, SIHEPI Rekap 3e, eKohort ANC, SiGizi Ibu Nifas, SiGizi Kohort Ibu (2x), SIM RS Tripat ANC, SIM RS Narmada INC, SIM RS Narmada KIA, SIM RS Panti Nugroho ANC, SIM RS Panti Nugroho INC, SIM RS Ummu Hani ANC, SIM RS Ummu Hani INC, SIM RS MPH ANC, SIM RS MPH INC, SIM RS Siaga Medika ANC, SIM RS Siaga Medika INC, SIM RS PKU INC | 21 |
| 6 | PNC | Postnatal Care | episodeofcare-type | Maternal Outcome, ePus PNC, SiGizi Ibu Nifas, SIM RS Tripat PNC, SIM RS Narmada INC, SIM RS Narmada KIA, SIM RS Panti Nugroho INC, SIM RS Panti Nugroho PNC, SIM RS Ummu Hani INC, SIM RS Ummu Hani PNC, SIM RS MPH INC, SIM RS MPH PNC, SIM RS Siaga Medika INC, SIM RS Siaga Medika PNC, SIM RS PKU INC, SIM RS PKU PNC | 16 |
| 7 | SP000389 | Keadaan Ibu | kemkes sp | Maternal Outcome, ePus PNC, SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 7 |
| 8 | 102514002 | Well female adult | snomed | Maternal Outcome, ePus INC | 2 |
| 9 | 39104002 | Illness | snomed | Maternal Outcome, ePus INC, SiGizi PMT 2025 BB Tidak Naik - Survey, SiGizi PMT 2025 BB Kurang - Survey, SiGizi PMT 2025 Gizi Kurang - Survey | 5 |
| 10 | 419099009 | Dead | snomed | Maternal Outcome, SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 16K, ePus INC (3x), ePus PNC, SITB TB 01 | 8 |
| 11 | 93857-1 | Date and time of obstetric delivery | loinc | Maternal Outcome, ePus INC, ePus PNC, SIHEPI Rekap 3e, eKohort INC (2x), SiGizi Ibu Nifas, SiGizi Kohort Ibu, SIM RS Tripat PNC, SIM RS Narmada INC, SIM RS Panti Nugroho INC, SIM RS Panti Nugroho PNC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika INC, SIM RS Siaga Medika PNC, SIM RS PKU INC, SIM RS PKU PNC | 17 |
| 12 | 81956-5 | Date and time of death [TimeStamp] | loinc | Maternal Outcome, MPDN Kematian Bayi, MPDN Kematian Ibu, ePus INC, ePus PNC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika INC | 8 |
| 13 | LT000005 | Alamat Mati | location-type | Maternal Outcome | 1 |
| 14 | 79378-6 | Cause of death | loinc | Maternal Outcome, MPDN Kematian Bayi, MPDN Kematian Ibu, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika INC | 6 |
| 15 | SP001135 | Presensi Posyandu | kemkes sp | Raffle | 1 |
| 16 | 385438008 | Source of information | snomed | Raffle, SISMAL Regmal 1 | 2 |
| 17 | SP000776 | Sigizi | kemkes sp | Raffle | 1 |
| 18 | SP000777 | E-pus PKD | kemkes sp | Raffle | 1 |
| 19 | SP000778 | E-pus | kemkes sp | Raffle | 1 |
| 20 | 309453006 | Registered midwife | snomed | SiGizi ANC, MPDN Kematian Bayi, ePus Kunjungan Ibu Hamil, ePus ANC, ePus INC (2x), ePus PNC, ELSMIL Pasca Persalinan, SIPTM, eKohort INC, SiGizi Kohort Ibu | 10 |
| 21 | 309343006 | Physician | snomed | SiGizi ANC, MPDN Kematian Bayi, ePus Kunjungan Ibu Hamil, ePus ANC, ePus INC (2x), ePus PNC, ELSMIL Pasca Persalinan, eKohort INC, SiGizi Kohort Ibu | 9 |
| 22 | 309367003 | Obstetrician and gynecologist | snomed | SiGizi ANC, ePus ANC, ePus INC, ePus PNC, SiGizi Kohort Ibu | 5 |
| 23 | 224535009 | Registered nurse | snomed | SiGizi ANC, ePus ANC, ePus INC, ePus PNC, SiGizi Kohort Ibu | 5 |
| 24 | K1M | Tidak ada | episodeofcare/ANC | SiGizi ANC, ePus ANC, eKohort ANC | 3 |
| 25 | K1A | Tidak ada | episodeofcare/ANC | SiGizi ANC, ePus ANC, eKohort ANC | 3 |
| 26 | 134435003 | Routine antenatal care | snomed | SiGizi ANC, ePus Kunjungan Ibu Hamil (2x), ePus ANC, ELSMIL Ibu Hamil, SIHEPI Rekap 3e, eKohort ANC, SiGizi Kohort Ibu (13x) | 7 |
| 27 | 424144002 | Current chronological age | snomed | SiGizi ANC, SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 04, SITB TB 16K (2x), ePus Kunjungan Ibu Hamil, ePus MTBS, ePus MTBM, ePus Tumbang DDTK, SITB TB 01 (2x), SITB TB 02, ASIK Skrining PTM, SIHEPI Rekap 3e, SiGizi Balita BNBA, SiGizi Balita Vitamin A, SiGizi Kohort Ibu, SISMAL Regmal 1 (2x) | 18 |
| 28 | 8665-2 | Last menstrual period start date | loinc | SiGizi ANC, ePus Kunjungan Ibu Hamil, ePus ANC, ePus PNC, eKohort ANC, SiGizi Ibu Nifas, SiGizi Kohort Ibu, SIM RS Tripat ANC, SIM RS Narmada INC, SIM RS Narmada KIA, SIM RS Panti Nugroho ANC, SIM RS Ummu Hani ANC, SIM RS MPH ANC, SIM RS Siaga Medika ANC, SIM RS Siaga Medika INC | 15 |
| 29 | ANC.B6.DE14 | Last menstrual period (LMP) date | WHO anc-custom-codes | SiGizi ANC, ePus Kunjungan Ibu Hamil, ePus ANC, ePus PNC, eKohort ANC, SiGizi Kohort Ibu, SIM RS Tripat ANC, SIM RS Narmada INC, SIM RS Narmada KIA, SIM RS Panti Nugroho ANC, SIM RS Ummu Hani ANC, SIM RS MPH ANC, SIM RS Siaga Medika ANC | 13 |
| 30 | 18185-9 | Gestational age | loinc | SiGizi ANC, MPDN Kematian Bayi, ePus Kunjungan Ibu Hamil, ePus ANC, ePus INC, ELSMIL Ibu Hamil, SIHEPI Rekap 3e, eKohort ANC, SIM RS Tripat ANC, SIM RS Narmada INC, SIM RS Narmada KIA, SIM RS Ummu Hani ANC, SIM RS MPH ANC, SIM RS Siaga Medika INC | 14 |
| 31 | 11778-8 | Delivery date Estimated | loinc | SiGizi ANC, ePus Kunjungan Ibu Hamil, ePus ANC, ePus PNC, SIHEPI Rekap 3e, eKohort ANC, SIM RS Tripat ANC, SIM RS Narmada INC, SIM RS Narmada KIA, SIM RS Siaga Medika INC | 10 |
| 32 | ANC.B6.DE22 | Expected date of delivery (EDD) | WHO anc-custom-codes | SiGizi ANC, ePus Kunjungan Ibu Hamil, ePus ANC, ePus PNC, SIHEPI Rekap 3e, eKohort ANC, SIM RS Tripat ANC, SIM RS Narmada INC, SIM RS Narmada KIA | 9 |
| 33 | 8302-2 | Body height | loinc | SiGizi ANC, ePus Pelayanan Pasien, ePus Kunjungan Ibu Hamil, ePus ANC, ePus INC, Dapodik PAUD, SITB TB 01, ELSMIL Ibu Hamil, SIPTM, ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026), eKohort ANC, SiGizi Kohort Ibu, SIM RS Tripat ANC, SIM RS Narmada INC, SIM RS Narmada KIA, SIM RS Panti Nugroho ANC, SIM RS Ummu Hani ANC, SIM RS MPH ANC, SIM RS Siaga Medika ANC, SIM RS PKU INC | 22 |
| 34 | ANC.B8.DE1 | Height | WHO anc-custom-codes | SiGizi ANC, ePus ANC, ELSMIL Ibu Hamil, eKohort ANC, SiGizi Kohort Ibu, SIM RS Tripat ANC, SIM RS Narmada INC, SIM RS Narmada KIA, SIM RS Panti Nugroho ANC, SIM RS Ummu Hani ANC, SIM RS MPH ANC, SIM RS Siaga Medika ANC | 12 |
| 35 | OC000010 | Indeks Massa Tubuh Sebelum Hamil | kemkes clinical-term | SiGizi ANC, ELSMIL Ibu Hamil, SiGizi Kohort Ibu | 3 |
| 36 | ANC.SS.DE58 | IMT Sebelum Hamil | kemkes anc-custom-codes | SiGizi ANC, ELSMIL Ibu Hamil, SiGizi Kohort Ibu | 3 |
| 37 | VG139 | Td | kfa | SiGizi ANC, ePus Kunjungan Ibu Hamil (2x), ePus ANC (3x), eKohort ANC (2x), SiGizi Kohort Ibu (2x), SIM RS Tripat ANC, SIM RS Narmada INC (2x), SIM RS Narmada KIA, SIM RS Panti Nugroho ANC (3x), SIM RS Ummu Hani ANC, SIM RS MPH ANC, SIM RS Siaga Medika ANC (3x) | 12 |
| 38 | SP000001 | Skrining Imunisasi Tetanus Toksoid | kemkes sp | SiGizi ANC, ePus ANC, SiGizi Kohort Ibu, SIM RS Panti Nugroho ANC, SIM RS Siaga Medika ANC | 5 |
| 39 | SP000002 | Kunjungan Pertama Pemeriksaan Kehamilan | kemkes sp | SiGizi ANC, ePus ANC | 2 |
| 40 | 29463-7 | Body weight | loinc | SiGizi ANC, ePus Pelayanan Pasien, ePus Kunjungan Ibu Hamil, ePus ANC, ePus INC, ePus Tumbang Anak, ePus Tumbang DDTK, Dapodik PAUD, SITB TB 01 (3x), ELSMIL Ibu Hamil, SIPTM, ASIK CKG Bayi Baru Lahir (v2), ASIK CKG Balita (v2), ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026), eKohort ANC, SiGizi Balita BNBA, SiGizi Balita Vitamin A, SiGizi Balita Mendapat PMT 2024, SiGizi Balita Pemantauan PMT 2024, SiGizi PMT 2025 BB Tidak Naik - Pantau (3x), SiGizi PMT 2025 BB Tidak Naik - Riwayat (2x), SiGizi PMT 2025 BB Kurang - Pantau (5x), SiGizi PMT 2025 BB Kurang - Riwayat (2x), SiGizi PMT 2025 Gizi Kurang - Pantau (9x), SiGizi PMT 2025 Gizi Kurang - Riwayat (2x), SiGizi Kohort Ibu, SIM RS Tripat ANC, SIM RS Narmada INC, SIM RS Narmada KIA, SIM RS Panti Nugroho ANC, SIM RS Ummu Hani ANC, SIM RS MPH ANC, SIM RS MPH BBL, SIM RS Siaga Medika BBL, SIM RS PKU INC, SISMAL Regmal 1 | 38 |
| 41 | ANC.B8.DE3 | Current weight | WHO anc-custom-codes | SiGizi ANC, ePus ANC, SITB TB 01 (2x), ELSMIL Ibu Hamil, eKohort ANC, SiGizi Kohort Ibu, SIM RS Tripat ANC, SIM RS Narmada INC, SIM RS Narmada KIA, SIM RS Panti Nugroho ANC, SIM RS Ummu Hani ANC, SIM RS MPH ANC, SISMAL Regmal 1 | 13 |
| 42 | 392570002 | Blood pressure finding | snomed | SiGizi ANC | 1 |
| 43 | 2004005 | Normal blood pressure | snomed | SiGizi ANC | 1 |
| 44 | 38341003 | Hypertension | snomed | SiGizi ANC, ePus INC | 2 |
| 45 | 45007003 | Hypotension | snomed | SiGizi ANC | 1 |
| 46 | 284473002 | Mid upper arm circumference | snomed | SiGizi ANC, ePus Kunjungan Ibu Hamil, ePus ANC, ePus INC, ePus PNC, ePus MTBS (2x), ePus Tumbang DDTK, ELSMIL Ibu Hamil, eKohort ANC, SiGizi Balita BNBA, SiGizi Balita Vitamin A, SiGizi Kohort Ibu | 12 |
| 47 | ANC.SS.DE3 | Lingkar Lengan Atas (LILA) | kemkes anc-custom-codes | SiGizi ANC, ePus Kunjungan Ibu Hamil, ELSMIL Ibu Hamil, eKohort ANC, SiGizi Kohort Ibu, SIM RS Narmada INC, SIM RS Narmada KIA, SIM RS Ummu Hani ANC, SIM RS MPH ANC, SIM RS Siaga Medika ANC | 10 |
| 48 | OI000018 | Kurang Energi Kronis (KEK) | kemkes clinical-term | SiGizi ANC, ePus Kunjungan Ibu Hamil, ePus ANC, ePus PNC, eKohort ANC, SiGizi Kohort Ibu, SIM RS Narmada INC, SIM RS Narmada KIA, SIM RS Panti Nugroho ANC, SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH ANC, SIM RS MPH PNC, SIM RS Siaga Medika ANC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 16 |
| 49 | N | Normal | v3-ObservationInterpretation | SiGizi ANC, ePus ANC (13x), ePus PNC, ASIK CKG Balita (v2) (3x), ASIK CKG Dewasa Laki-laki (16x), ASIK CKG Dewasa Perempuan (16x), ASIK CKG Lansia (27 Apr 2026) (16x), eKohort ANC, SiGizi Kohort Ibu, SIM RS Narmada INC, SIM RS Narmada KIA, SIM RS Panti Nugroho ANC, SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH ANC, SIM RS MPH PNC, SIM RS MPH BBL (8x), SIM RS Siaga Medika ANC, SIM RS Siaga Medika PNC, SIM RS Siaga Medika BBL (8x), SIM RS PKU PNC | 21 |
| 50 | OI000035 | Risiko Kurang Energi Kronis (KEK) | kemkes clinical-term | SiGizi ANC, ePus Kunjungan Ibu Hamil, ePus ANC, eKohort ANC, SiGizi Kohort Ibu, SIM RS Narmada INC, SIM RS Narmada KIA, SIM RS Panti Nugroho ANC, SIM RS MPH ANC, SIM RS Siaga Medika ANC | 10 |
| 51 | 289625003 | Finding of fundal height of uterus | snomed | SiGizi ANC | 1 |
| 52 | SP000003 | Sesuai Usia Kehamilan | kemkes sp | SiGizi ANC | 1 |
| 53 | SP000004 | Tidak Sesuai Usia Kehamilan | kemkes sp | SiGizi ANC | 1 |
| 54 | 883-9 | ABO group [Type] in Blood | loinc | SiGizi ANC, ePus Laboratorium (3x), ePus ANC, ePus INC, SIPTM, SIM RS Ummu Hani ANC, SIM RS Ummu Hani BBL, SIM RS MPH ANC, SIM RS Siaga Medika ANC | 9 |
| 55 | ANC.B9.DE24 | Blood type | WHO anc-custom-codes | SiGizi ANC, ePus ANC, SIM RS Ummu Hani ANC, SIM RS MPH ANC, SIM RS Siaga Medika ANC | 5 |
| 56 | LA19710-5 | Group A | loinc | SiGizi ANC, ePus Laboratorium, ePus ANC, ePus INC, SIPTM, SIM RS Ummu Hani ANC, SIM RS Ummu Hani BBL, SIM RS MPH ANC, SIM RS Siaga Medika ANC | 9 |
| 57 | LA19709-7 | Group B | loinc | SiGizi ANC, ePus Laboratorium, ePus ANC, ePus INC, SIPTM, SIM RS Ummu Hani ANC, SIM RS Ummu Hani BBL, SIM RS MPH ANC, SIM RS Siaga Medika ANC | 9 |
| 58 | LA19708-9 | Group O | loinc | SiGizi ANC, ePus Laboratorium, ePus ANC, ePus INC, SIPTM, SIM RS Ummu Hani ANC, SIM RS Ummu Hani BBL, SIM RS MPH ANC, SIM RS Siaga Medika ANC | 9 |
| 59 | LA28449-9 | Group AB | loinc | SiGizi ANC, ePus Laboratorium, ePus ANC, ePus INC, SIPTM, SIM RS Ummu Hani ANC, SIM RS Ummu Hani BBL, SIM RS MPH ANC, SIM RS Siaga Medika ANC | 9 |
| 60 | 10331-7 | Rh [Type] in Blood | loinc | SiGizi ANC, ePus ANC, SIM RS Ummu Hani BBL, SIM RS Siaga Medika ANC | 4 |
| 61 | ANC.B9.DE29 | Rh factor | WHO anc-custom-codes | SiGizi ANC, ePus ANC, SIM RS Siaga Medika ANC | 3 |
| 62 | LA6576-8 | Positive | loinc | SiGizi ANC (4x), SITB TB 06 (4x), SITB TB 03 SO (3x), SITB TB 03 RO (4x), SITB TB 04 (3x), ePus Kunjungan Ibu Hamil (9x), ePus Laboratorium (21x), ePus ANC (4x), ePus MTBS (3x), SIHEPI Rekap 3e (2x), eKohort ANC (2x), SiGizi Kohort Ibu, SIM RS Ummu Hani BBL, SIM RS Siaga Medika ANC (4x) | 14 |
| 63 | LA6577-6 | Negative | loinc | SiGizi ANC (4x), SITB TB 06 (5x), SITB TB 03 SO (4x), SITB TB 03 RO (5x), SITB TB 04 (7x), ePus Kunjungan Ibu Hamil (10x), ePus Laboratorium (22x), ePus ANC (4x), ePus MTBS (3x), SIHEPI Rekap 3e (2x), eKohort ANC (3x), SiGizi Kohort Ibu, SIM RS Ummu Hani BBL, SIM RS Siaga Medika ANC (4x) | 14 |
| 64 | 289437007 | Finding of fetal heart rate | snomed | SiGizi ANC, ePus INC | 2 |
| 65 | 289441006 | Normal fetal heart rate | snomed | SiGizi ANC, ePus ANC, ePus INC, eKohort INC | 4 |
| 66 | 289440007 | Fetal heart rate not observed | snomed | SiGizi ANC, ePus ANC, ePus INC | 3 |
| 67 | 312668007 | Abnormal fetal heart rate | snomed | SiGizi ANC, ePus ANC, ePus INC, eKohort INC | 4 |
| 68 | 289439005 | Fetal heart rate absent | snomed | SiGizi ANC, ePus ANC, ePus INC | 3 |
| 69 | 72155-5 | Position in womb Fetus [RHEA] | loinc | SiGizi ANC, ePus Kunjungan Ibu Hamil (2x), ePus ANC, ePus INC, eKohort INC (2x), SIM RS Tripat ANC, SIM RS Narmada INC, SIM RS Narmada KIA, SIM RS Panti Nugroho ANC, SIM RS Panti Nugroho INC, SIM RS Ummu Hani ANC, SIM RS Ummu Hani INC, SIM RS MPH ANC, SIM RS MPH INC, SIM RS Siaga Medika ANC, SIM RS Siaga Medika INC, SIM RS PKU INC | 17 |
| 70 | ANC.B8.DE111 | Fetal presentation | WHO anc-custom-codes | SiGizi ANC, ePus Kunjungan Ibu Hamil (2x), ePus ANC (2x), eKohort INC, SIM RS Tripat ANC, SIM RS Panti Nugroho ANC, SIM RS Ummu Hani ANC, SIM RS MPH ANC, SIM RS Siaga Medika ANC (2x) | 9 |
| 71 | 1209182005 | Cephalic fetal presentation | snomed | SiGizi ANC, ePus Kunjungan Ibu Hamil (2x), ePus ANC (2x), ePus INC, eKohort INC | 5 |
| 72 | SP000005 | Letak Bokong/ Lintang | kemkes sp | SiGizi ANC, ePus ANC | 2 |
| 73 | SP000006 | Organ Tubuh Lainnya | kemkes sp | SiGizi ANC, ePus Kunjungan Ibu Hamil, ePus ANC (2x), SIM RS Ummu Hani ANC, SIM RS MPH ANC, SIM RS Siaga Medika ANC | 6 |
| 74 | 88.78 | Diagnostic ultrasound of gravid uterus | icd-9-cm | SiGizi ANC, ePus ANC, eKohort ANC, SIM RS Narmada KIA, SIM RS Panti Nugroho ANC, SIM RS Ummu Hani ANC, SIM RS MPH ANC, SIM RS Siaga Medika ANC, SIM RS Goetoeng ANC, SIM RS Goetoeng INC (2x) | 10 |
| 75 | 268445003 | Ultrasound scan - obstetric | snomed | SiGizi ANC, ePus ANC | 2 |
| 76 | 169221005 | Ultrasound obstetric scan normal | snomed | SiGizi ANC, ePus ANC | 2 |
| 77 | 169255008 | Ultrasound scan abnormal | snomed | SiGizi ANC, ePus ANC | 2 |
| 78 | 92000653 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula | kfa | SiGizi ANC, ePus Kunjungan Ibu Hamil | 2 |
| 79 | 93015491 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | kfa | SiGizi ANC, ePus Kunjungan Ibu Hamil, ePus ANC | 3 |
| 80 | SP000370 | Multiple Micronutrient Supplement | kemkes sp | SiGizi ANC (2x), ePus Pelayanan Pasien (2x) | 2 |
| 81 | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | loinc | SiGizi ANC (3x), ePus Kunjungan Ibu Hamil (3x), ePus Laboratorium (3x), ePus ANC (3x), SITB TB 01, ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026), SIHEPI Rekap 3e (3x), eKohort ANC (3x), SIM RS Siaga Medika ANC (2x) | 11 |
| 82 | 122555007 | Venous blood specimen | snomed | SiGizi ANC (5x), ePus Kunjungan Ibu Hamil (9x), ePus Laboratorium, ePus ANC (5x), ELSMIL Ibu Hamil, SIHEPI Rekap 3e (3x), eKohort ANC (4x), SiGizi Kohort Ibu (2x) | 8 |
| 83 | ANC.B9.DE32 | HIV test | WHO anc-custom-codes | SiGizi ANC, ePus Kunjungan Ibu Hamil, ePus Laboratorium, ePus ANC, SIHEPI Rekap 3e, eKohort ANC, SIM RS Siaga Medika ANC | 7 |
| 84 | LA15255-5 | Reactive | loinc | SiGizi ANC, ePus Kunjungan Ibu Hamil (3x), ePus Laboratorium (2x), ePus ANC, ePus MTBS (4x), ePus MTBM (3x), SITB TB 01, ASIK CKG Dewasa Laki-laki (2x), ASIK CKG Dewasa Perempuan (2x), ASIK CKG Lansia (27 Apr 2026) (3x), SIHEPI Rekap 3e (7x), eKohort ANC, SIM RS Siaga Medika ANC | 13 |
| 85 | LA15256-3 | Nonreactive | loinc | SiGizi ANC, ePus Kunjungan Ibu Hamil (3x), ePus Laboratorium (2x), ePus ANC, ePus MTBS (4x), ePus MTBM (3x), SITB TB 01, ASIK CKG Dewasa Laki-laki (2x), ASIK CKG Dewasa Perempuan (2x), ASIK CKG Lansia (27 Apr 2026) (3x), SIHEPI Rekap 3e (7x), eKohort ANC, SIM RS Siaga Medika ANC | 13 |
| 86 | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | loinc | SiGizi ANC (3x), ePus Kunjungan Ibu Hamil (6x), ePus Laboratorium (3x), ePus ANC (3x), ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026), SIHEPI Rekap 3e (3x), eKohort ANC (3x), SIM RS Siaga Medika ANC (3x) | 10 |
| 87 | ANC.B9.DE60 | Hepatitis B test conducted | WHO anc-custom-codes | SiGizi ANC, ePus Kunjungan Ibu Hamil (2x), ePus Laboratorium, ePus ANC, SIHEPI Rekap 3e, eKohort ANC, SIM RS Siaga Medika ANC | 7 |
| 88 | 22464-2 | Reagin Ab [Presence] in Specimen | loinc | SiGizi ANC (3x), ePus Kunjungan Ibu Hamil (6x), ePus Laboratorium (3x), ePus ANC (3x), ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026), SIHEPI Rekap 3e (3x), eKohort ANC (3x), SIM RS Siaga Medika ANC (3x) | 10 |
| 89 | ANC.B9.DE96 | Syphilis test conducted | WHO anc-custom-codes | SiGizi ANC, ePus Kunjungan Ibu Hamil (2x), ePus Laboratorium, ePus ANC, SIHEPI Rekap 3e, eKohort ANC, SIM RS Siaga Medika ANC | 7 |
| 90 | 2887-8 | Protein [Presence] in Urine | loinc | SiGizi ANC (3x), ePus Kunjungan Ibu Hamil (3x), ePus Laboratorium (3x), ePus ANC (3x), eKohort ANC (3x), SiGizi Kohort Ibu (3x), SIM RS Siaga Medika ANC (3x) | 7 |
| 91 | 122575003 | Urine specimen | snomed | SiGizi ANC, ePus Kunjungan Ibu Hamil, ePus Laboratorium (16x), ePus ANC, eKohort ANC, SiGizi Kohort Ibu | 6 |
| 92 | ANC.B9.DE114 | Urine test conducted | WHO anc-custom-codes | SiGizi ANC, ePus Kunjungan Ibu Hamil, ePus Laboratorium, ePus ANC, eKohort ANC, SiGizi Kohort Ibu, SIM RS Siaga Medika ANC | 7 |
| 93 | 718-7 | Hemoglobin [Mass/volume] in Blood | loinc | SiGizi ANC (3x), ePus Kunjungan Ibu Hamil (4x), ePus Laboratorium (4x), ePus ANC (3x), ePus MTBS (6x), ELSMIL Ibu Hamil (3x), ASIK CKG Balita (v2), eKohort ANC (3x), SiGizi Kohort Ibu (3x), SIM RS Siaga Medika ANC (3x) | 10 |
| 94 | ANC.B9.DE175 | Blood hemoglobin test conducted | WHO anc-custom-codes | SiGizi ANC, ePus Kunjungan Ibu Hamil, ePus Laboratorium, ePus ANC, ELSMIL Ibu Hamil, eKohort ANC, SiGizi Kohort Ibu, SIM RS Siaga Medika ANC | 8 |
| 95 | 860635002 | No anemia present | snomed | SiGizi ANC, ePus MTBS | 2 |
| 96 | OI000032 | Anemia ringan | kemkes clinical-term | SiGizi ANC | 1 |
| 97 | OI000033 | Anemia sedang | kemkes clinical-term | SiGizi ANC | 1 |
| 98 | OI000034 | Anemia berat | kemkes clinical-term | SiGizi ANC | 1 |
| 99 | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | loinc | SiGizi ANC (3x), ePus Kunjungan Ibu Hamil (3x), ePus ANC (3x), SIPTM (3x), ASIK Skrining PTM (3x), SiGizi Kohort Ibu (3x), SIM RS Siaga Medika ANC (3x) | 7 |
| 100 | ANC.B9.DE159 | Blood glucose test conducted | WHO anc-custom-codes | SiGizi ANC, ePus Kunjungan Ibu Hamil, ePus ANC, SiGizi Kohort Ibu, SIM RS Siaga Medika ANC | 5 |
| 101 | 166921001 | Blood glucose normal | snomed | SiGizi ANC | 1 |
| 102 | 166922008 | Blood glucose abnormal | snomed | SiGizi ANC | 1 |
| 103 | 15220000 | Laboratory test | snomed | SiGizi ANC, ePus ANC | 2 |
| 104 | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | loinc | SiGizi ANC, SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 04, ePus ANC, SITB TB 01, ASIK CKG Dewasa Laki-laki (8x), ASIK CKG Dewasa Perempuan (8x), ASIK CKG Lansia (27 Apr 2026) (8x), SIM RS Siaga Medika ANC | 11 |
| 105 | 76772-3 | Plasmodium falciparum Ag [Presence] in Blood by Rapid immunoassay | loinc | SiGizi ANC, ePus ANC, ePus MTBS (3x), SIM RS Siaga Medika ANC | 4 |
| 106 | 104742-2 | Ova and parasites identified in Specimen | loinc | SiGizi ANC, ePus ANC, SIM RS Siaga Medika ANC | 3 |
| 107 | 74964007 | Other | snomed | SiGizi ANC (4x), SITB TB 03 SO (3x), SITB TB 03 RO (2x), ePus ANC (5x), ePus INC (3x), ePus PNC (2x), Dapodik PAUD (4x), SITB TB 01, ELSMIL Ibu Hamil (4x), ELSMIL Pasca Persalinan (3x), ELSMIL Baduta (3x), SIPTM, SIHEPI Rekap 3e, SiGizi PMT 2025 BB Tidak Naik - Survey (2x), SiGizi PMT 2025 BB Kurang - Survey (2x), SiGizi PMT 2025 Gizi Kurang - Survey (2x), SISMAL Regmal 1 (2x) | 17 |
| 108 | SP000007 | Tatalaksana Anemia | kemkes sp | SiGizi ANC, ePus ANC, SIM RS Panti Nugroho ANC, SIM RS MPH ANC, SIM RS Siaga Medika ANC | 5 |
| 109 | SP000008 | Pemberian Tablet Tambah Darah | kemkes sp | SiGizi ANC, ePus ANC, ePus PNC, SIM RS Panti Nugroho ANC, SIM RS Panti Nugroho PNC, SIM RS MPH ANC, SIM RS Siaga Medika ANC, SIM RS PKU PNC | 8 |
| 110 | SP000009 | Pemberian Fe Parenteral | kemkes sp | SiGizi ANC, ePus ANC, SIM RS Panti Nugroho ANC, SIM RS MPH ANC, SIM RS Siaga Medika ANC | 5 |
| 111 | 116859006 | Transfusion of blood product | snomed | SiGizi ANC, ePus ANC, ePus PNC | 3 |
| 112 | 3457005 | Patient referral | snomed | SiGizi ANC (3x), ePus ANC (3x), SIPTM (2x), eKohort INC | 4 |
| 113 | SP000010 | Skrining Hipertensi dalam Kehamilan | kemkes sp | SiGizi ANC, ePus ANC, SIM RS Panti Nugroho ANC, SIM RS MPH ANC, SIM RS Siaga Medika ANC | 5 |
| 114 | SP000011 | Tidak Pre Eklampsia/ Eklampsia | kemkes sp | SiGizi ANC, ePus ANC, SIM RS Panti Nugroho ANC, SIM RS MPH ANC, SIM RS Siaga Medika ANC | 5 |
| 115 | 48194001 | Pregnancy-induced hypertension | snomed | SiGizi ANC, ePus ANC, ePus INC (2x) | 3 |
| 116 | 398254007 | Pre-eclampsia | snomed | SiGizi ANC, ePus ANC (2x), ePus INC | 3 |
| 117 | 15938005 | Eclampsia | snomed | SiGizi ANC, ePus ANC (2x), ePus INC | 3 |
| 118 | SP000012 | Tatalaksana Pre Eklampsia | kemkes sp | SiGizi ANC, ePus ANC, SIM RS Panti Nugroho ANC, SIM RS MPH ANC, SIM RS Siaga Medika ANC | 5 |
| 119 | 135840009 | Blood pressure monitoring | snomed | SiGizi ANC, ePus ANC, ePus PNC | 3 |
| 120 | 308116003 | Antihypertensive therapy | snomed | SiGizi ANC, ePus ANC, ePus PNC | 3 |
| 121 | SP000013 | Pemberian MgSO4 | kemkes sp | SiGizi ANC, ePus ANC, SIM RS Panti Nugroho ANC, SIM RS Panti Nugroho INC, SIM RS MPH ANC, SIM RS Siaga Medika ANC, SIM RS Siaga Medika INC, SIM RS PKU INC | 8 |
| 122 | SP000014 | Tatalaksana KEK | kemkes sp | SiGizi ANC, ePus ANC, SIM RS Panti Nugroho ANC, SIM RS MPH ANC, SIM RS Siaga Medika ANC | 5 |
| 123 | 435591000124104 | Nutrition supplement therapy | snomed | SiGizi ANC, ePus ANC | 2 |
| 124 | SP000015 | Risiko Masalah Kesehatan | kemkes sp | SiGizi ANC, ePus ANC, SIM RS Panti Nugroho ANC, SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH ANC, SIM RS MPH INC, SIM RS Siaga Medika ANC, SIM RS PKU INC | 9 |
| 125 | 40733004 | Infectious disease | snomed | SiGizi ANC, ePus ANC (2x), ePus INC | 3 |
| 126 | 73211009 | Diabetes mellitus | snomed | SiGizi ANC, ePus ANC (2x) | 2 |
| 127 | 414916001 | Obesity | snomed | SiGizi ANC, ePus ANC | 2 |
| 128 | 56717001 | Tuberculosis | snomed | SiGizi ANC, SITB TB 16K, ePus ANC (2x), SITB TB 01 | 4 |
| 129 | 56265001 | Heart disease | snomed | SiGizi ANC, ePus ANC | 2 |
| 130 | SP000016 | Tatalaksana Masalah Kesehatan | kemkes sp | SiGizi ANC, ePus ANC | 2 |
| 131 | 1230101008 | Counseling for pregnancy | snomed | SiGizi ANC, ePus Kunjungan Ibu Hamil, ePus ANC | 3 |
| 132 | 385892002 | Mental health screening | snomed | SiGizi ANC, ePus ANC | 2 |
| 133 | TB-SO | Tuberkulosis Sensitif Obat | episodeofcare-type | SITB TB 06 (3x), SITB TB 03 SO, SITB TB 04, SITB TB 16K, SITB TB 01 | 5 |
| 134 | TB-RO | Tuberkulosis Resisten Obat | episodeofcare-type | SITB TB 06 (3x), SITB TB 03 RO, SITB TB 04, SITB TB 16K, SITB TB 01 | 5 |
| 135 | EHA000001 | Kader/ Komunitas | kemkes clinical-term | SITB TB 06, SITB TB 01 | 2 |
| 136 | EHA000002 | Datang sendiri | kemkes clinical-term | SITB TB 06, SITB TB 03 SO (2x), SITB TB 03 RO (2x), SITB TB 04, ePus ANC, ePus INC, ePus PNC, SITB TB 01, SIM RS Tripat PNC, SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika INC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 15 |
| 137 | EHA000003 | Kegiatan ACF | kemkes clinical-term | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 138 | 257622000 | Healthcare facility | snomed | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 04, SITB TB 01 | 5 |
| 139 | EHA000004 | Skrining TBC DM | kemkes clinical-term | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 140 | EHA000005 | Pemadanan Data BPJS | kemkes clinical-term | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 141 | Z03.0 | Observation for suspected tuberculosis | icd-10 | SITB TB 06 | 1 |
| 142 | A15.0 | Tuberculosis of lung, confirmed by sputum microscopy with or without culture | icd-10 | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, ePus Tumbang DDTK | 4 |
| 143 | A16.2 | Tuberculosis of lung, without mention of bacteriological or histological confirmation | icd-10 | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 01, SITB TB 02 | 5 |
| 144 | QRI000001 | Terduga TBC SO | kemkes clinical-term | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 145 | QRI000002 | Terduga TBC RO | kemkes clinical-term | SITB TB 06, SITB TB 03 RO | 2 |
| 146 | new | Kasus Baru | kemkes prev-tb-treatment | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 01, SITB TB 02 | 5 |
| 147 | relapse | Kasus Kambuh | kemkes prev-tb-treatment | SITB TB 06 (2x), SITB TB 03 SO, SITB TB 03 RO (2x), SITB TB 01, SITB TB 02 | 5 |
| 148 | failure-cat1 | Kasus Pengobatan Setelah Gagal Kategori 1 | kemkes prev-tb-treatment | SITB TB 06 (2x), SITB TB 03 SO, SITB TB 03 RO (2x) | 3 |
| 149 | failure-cat2 | Kasus Pengobatan Setelah Gagal Kategori 2 | kemkes prev-tb-treatment | SITB TB 06 (2x), SITB TB 03 SO, SITB TB 03 RO (2x) | 3 |
| 150 | loss-to-follow-up | Kasus Setelah Loss To Follow Up | kemkes prev-tb-treatment | SITB TB 06 (2x), SITB TB 03 SO, SITB TB 03 RO (2x), SITB TB 01, SITB TB 02 | 5 |
| 151 | failure-2line | Kasus Pengobatan Setelah Gagal lini 2 | kemkes prev-tb-treatment | SITB TB 06 (2x), SITB TB 03 SO, SITB TB 03 RO (2x) | 3 |
| 152 | not-eval | Pernah diobati tidak diketahui hasilnya | kemkes prev-tb-treatment | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 01, SITB TB 02 (2x) | 5 |
| 153 | unknown | Kasus dengan riwayat pengobatan tidak diketahui | kemkes prev-tb-treatment | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 154 | other | Kasus lain-lain | kemkes prev-tb-treatment | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 01, SITB TB 02 | 5 |
| 155 | failure | Kasus Pengobatan Setelah Gagal | kemkes prev-tb-treatment | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 01, SITB TB 02 | 5 |
| 156 | treatment-non-conversion-2 | Pasien TB pengobatan kategori 2 yang tidak konversi setelah 3 bulan pengobatan | kemkes prev-tb-treatment | SITB TB 06, SITB TB 03 RO | 2 |
| 157 | non-standard-treatment | Pasien TB yang mempunyai riwayat pengobatan TB yang tidak standar | kemkes prev-tb-treatment | SITB TB 06, SITB TB 03 RO | 2 |
| 158 | treatment-non-conversion-1 | Pasien TB pengobatan kategori 1 yang tidak konversi | kemkes prev-tb-treatment | SITB TB 06, SITB TB 03 RO | 2 |
| 159 | history-of-close-contact with-TB-DR | Terduga TB yang mempunyai riwayat kontak erat dengan pasien TB RO | kemkes prev-tb-treatment | SITB TB 06, SITB TB 03 RO | 2 |
| 160 | co-infected-TBHIV | Pasien ko-infeksi TB-HIV yang tidak respons secara klinis maupun bakteriologis terhadap pemberian OAT | kemkes prev-tb-treatment | SITB TB 06, SITB TB 03 RO | 2 |
| 161 | TB-DR-relapse | Pasien TB RO kasus kambuh | kemkes prev-tb-treatment | SITB TB 06, SITB TB 03 RO | 2 |
| 162 | TB-DR-returns | Pasien TB RO yang kembali setelah putus berobat | kemkes prev-tb-treatment | SITB TB 06, SITB TB 03 RO | 2 |
| 163 | 154283005 | Pulmonary tuberculosis | snomed | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 164 | 423997002 | Tuberculosis, extrapulmonary | snomed | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 165 | OC000191 | Jumlah Skoring TBC Anak | kemkes clinical-term | SITB TB 06, SITB TB 03 SO, SITB TB 01 | 3 |
| 166 | 24648-8 | XR Chest PA upright | loinc | SITB TB 06 (3x), SITB TB 03 SO, SITB TB 03 RO, ePus PNC (3x), SITB TB 01 | 5 |
| 167 | 707307002 | Tuberculosis screening chest X-ray abnormal | snomed | SITB TB 06, SITB TB 03 SO, ePus PNC | 3 |
| 168 | 707308007 | Tuberculosis screening chest X-ray normal | snomed | SITB TB 06, SITB TB 03 SO, ePus PNC | 3 |
| 169 | 424489006 | Mantoux test | snomed | SITB TB 06 (2x), SITB TB 03 SO (2x), SITB TB 03 RO (2x) | 3 |
| 170 | 35140007 | Interferon gamma assay | snomed | SITB TB 06 (2x), SITB TB 03 SO (2x), SITB TB 03 RO (2x) | 3 |
| 171 | 23539-0 | Tuberculosis reaction wheal [Diameter] --3 days post dose mammalian tuberculin intradermal | loinc | SITB TB 06 (2x), SITB TB 03 SO (2x), SITB TB 03 RO (2x), ePus Laboratorium (3x), SITB TB 01, ASIK CKG Lansia (27 Apr 2026) | 6 |
| 172 | 268376005 | Mantoux: positive | snomed | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, ePus Laboratorium | 4 |
| 173 | 268375009 | Mantoux: negative | snomed | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, ePus Laboratorium | 4 |
| 174 | 71773-6 | Mycobacterium tuberculosis stimulated gamma interferon [Interpretation] in Blood Qualitative | loinc | SITB TB 06 (2x), SITB TB 03 SO (2x), SITB TB 03 RO (2x) | 3 |
| 175 | 55277-8 | HIV status | loinc | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 176 | 10828004 | Positive | snomed | SITB TB 06 (3x), SITB TB 03 SO (3x), SITB TB 03 RO (3x), SITB TB 01 (2x) | 4 |
| 177 | 260385009 | Negative | snomed | SITB TB 06 (5x), SITB TB 03 SO (8x), SITB TB 03 RO (4x), SITB TB 04 (2x), ePus Kunjungan Ibu Hamil, ePus Laboratorium, SITB TB 01 (3x) | 7 |
| 178 | 261665006 | Unknown | snomed | SITB TB 06 (2x), SITB TB 03 SO (3x), SITB TB 03 RO (3x) | 3 |
| 179 | 33248-6 | Diabetes status | loinc | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 01 | 4 |
| 180 | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | loinc | SITB TB 06 (9x), SITB TB 03 SO (18x), SITB TB 03 RO (6x), SITB TB 04 (6x), ePus Kunjungan Ibu Hamil (3x), ePus Laboratorium (3x), SITB TB 01, ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) (2x) | 10 |
| 181 | 119334006 | Sputum specimen | snomed | SITB TB 06 (8x), SITB TB 03 SO (9x), SITB TB 03 RO (7x), SITB TB 04 (32x), ePus Kunjungan Ibu Hamil, ePus Laboratorium (2x) | 6 |
| 182 | LA11841-6 | 1+ | loinc | SITB TB 06 (3x), SITB TB 03 SO (6x), SITB TB 03 RO (2x), SITB TB 04 (3x), ePus Kunjungan Ibu Hamil (2x), ePus Laboratorium (2x), SITB TB 01, eKohort ANC | 8 |
| 183 | LA11842-4 | 2+ | loinc | SITB TB 06 (3x), SITB TB 03 SO (6x), SITB TB 03 RO (2x), SITB TB 04 (3x), ePus Kunjungan Ibu Hamil (2x), ePus Laboratorium (2x), SITB TB 01, eKohort ANC | 8 |
| 184 | LA11843-2 | 3+ | loinc | SITB TB 06 (3x), SITB TB 03 SO (6x), SITB TB 03 RO (2x), SITB TB 04 (3x), ePus Kunjungan Ibu Hamil (2x), ePus Laboratorium (2x), SITB TB 01, eKohort ANC | 8 |
| 185 | 89371-9 | MTB complex DNA and rpoB RIF resistance mutation panel [Presence] | loinc | SITB TB 06 (3x), SITB TB 03 SO (3x), SITB TB 03 RO, ePus Laboratorium (3x) | 4 |
| 186 | X099379 | Pemeriksaan TCM XDR | kemkes examination | SITB TB 06 (6x), SITB TB 03 SO (6x), SITB TB 03 RO (4x), SITB TB 04 (3x) | 4 |
| 187 | X099380 | Line Probe Assay (LPA) Lini 1 | kemkes examination | SITB TB 06 (6x), SITB TB 03 SO (6x), SITB TB 03 RO (4x), SITB TB 04 (3x) | 4 |
| 188 | X099381 | Line Probe Assay (LPA) Lini 2 | kemkes examination | SITB TB 06 (6x), SITB TB 03 SO (3x), SITB TB 03 RO (4x), SITB TB 04 (3x) | 4 |
| 189 | X099388 | Biakan TB | kemkes examination | SITB TB 06 (6x), SITB TB 03 SO (6x), SITB TB 03 RO (4x), SITB TB 01 (2x) | 4 |
| 190 | X099383 | Pemeriksaan Paket Standar Kepekaan | kemkes examination | SITB TB 06 (6x), SITB TB 03 SO (3x), SITB TB 03 RO (4x), SITB TB 04 (3x) | 4 |
| 191 | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | kemkes examination | SITB TB 06 (3x), SITB TB 03 SO (3x), SITB TB 03 RO, SITB TB 04 (6x) | 4 |
| 192 | MK099927 | Pemeriksaan PCR Open System | kemkes examination | SITB TB 06 (3x), SITB TB 03 SO (3x), SITB TB 03 RO, SITB TB 04 (3x) | 4 |
| 193 | X099770 | Rifampisin sensitive | kemkes examination | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 04 (4x), ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 7 |
| 194 | X099771 | Rifampisin resistan | kemkes examination | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 04 (4x), ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 7 |
| 195 | X099772 | Rifampisin indeterminate | kemkes examination | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 04 (4x), ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 7 |
| 196 | X099781 | Hasil Valid | kemkes examination | SITB TB 06 (3x), SITB TB 03 SO (2x), SITB TB 03 RO (3x), SITB TB 04 (3x) | 4 |
| 197 | LA11882-0 | Detected | loinc | SITB TB 06 (17x), SITB TB 03 SO (11x), SITB TB 03 RO (18x), SITB TB 04 (26x), SITB TB 01, ASIK CKG Dewasa Laki-laki (4x), ASIK CKG Dewasa Perempuan (4x), ASIK CKG Lansia (27 Apr 2026) (4x) | 8 |
| 198 | LA11883-8 | Not detected | loinc | SITB TB 06 (17x), SITB TB 03 SO (11x), SITB TB 03 RO (17x), SITB TB 04 (26x), SITB TB 01, ASIK CKG Dewasa Laki-laki (2x), ASIK CKG Dewasa Perempuan (2x), ASIK CKG Lansia (27 Apr 2026) (2x) | 8 |
| 199 | X099391 | H Dosis Rendah (Low) | kemkes examination | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 04 (2x) | 4 |
| 200 | LA11884-6 | Indeterminate | loinc | SITB TB 06 (15x), SITB TB 03 SO (9x), SITB TB 03 RO (15x), SITB TB 04 (18x), ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) (2x) | 7 |
| 201 | 89488-1 | Isoniazid [Susceptibility] by Genotype method | loinc | SITB TB 06 (2x), SITB TB 03 SO (2x), SITB TB 03 RO (2x), SITB TB 04 (2x) | 4 |
| 202 | 96110-2 | Ethionamide [Susceptibility] by Genotype method | loinc | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 04 (2x) | 4 |
| 203 | X099392 | FQ Dosis Rendah (Low) | kemkes examination | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 04 | 4 |
| 204 | 89487-3 | Fluoroquinolone [Susceptibility] by Genotype method | loinc | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 04 | 4 |
| 205 | 89484-0 | Amikacin [Susceptibility] by Genotype method | loinc | SITB TB 06 (2x), SITB TB 03 SO, SITB TB 03 RO (2x), SITB TB 04 (2x) | 4 |
| 206 | 89482-4 | Kanamycin [Susceptibility] by Genotype method | loinc | SITB TB 06 (2x), SITB TB 03 SO, SITB TB 03 RO (2x), SITB TB 04 (2x) | 4 |
| 207 | 89483-2 | Capreomycin [Susceptibility] by Genotype method | loinc | SITB TB 06 (2x), SITB TB 03 SO, SITB TB 03 RO (2x), SITB TB 04 (2x) | 4 |
| 208 | 13956-8 | Mycobacterium tuberculosis DNA [Presence] in Specimen by NAA with probe detection | loinc | SITB TB 06 (2x), SITB TB 03 SO, SITB TB 03 RO (2x), SITB TB 04 (3x), ASIK CKG Lansia (27 Apr 2026) | 5 |
| 209 | 89489-9 | rifAMPin [Susceptibility] by Genotype method | loinc | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 04 (2x) | 4 |
| 210 | X099774 | Ress Inffered (RI) | kemkes examination | SITB TB 06 (8x), SITB TB 03 SO (2x), SITB TB 03 RO (8x), SITB TB 04 (11x) | 4 |
| 211 | 20629-2 | levoFLOXacin [Susceptibility] | loinc | SITB TB 06, SITB TB 03 RO, SITB TB 04 | 3 |
| 212 | 96112-8 | Moxifloxacin [Susceptibility] by Genotype method | loinc | SITB TB 06, SITB TB 03 RO, SITB TB 04 | 3 |
| 213 | X099775 | Moxifloxacin DT (Mfx DT) | kemkes examination | SITB TB 06, SITB TB 03 RO, SITB TB 04 | 3 |
| 214 | 110379001 | Mycobacterium, non-tuberculosis (organism) | snomed | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 04 (2x) | 4 |
| 215 | X099776 | H High Dosage [Susceptibility] by Method for Slow-growing mycobacteria | kemkes examination | SITB TB 06, SITB TB 03 RO, SITB TB 04 | 3 |
| 216 | LA24225-7 | Susceptible | loinc | SITB TB 06 (7x), SITB TB 03 RO (7x), SITB TB 04 (8x) | 3 |
| 217 | LA6676-6 | Resistant | loinc | SITB TB 06 (7x), SITB TB 03 RO (7x), SITB TB 04 (8x) | 3 |
| 218 | LA16550-8 | Intermediate | loinc | SITB TB 06 (7x), SITB TB 03 RO (7x), SITB TB 04 (8x) | 3 |
| 219 | 20383-6 | Isoniazid [Susceptibility] by Method for Slow-growing mycobacteria | loinc | SITB TB 06, SITB TB 03 RO, SITB TB 04 | 3 |
| 220 | 23609-1 | Kanamycin [Susceptibility] by Method for Slow-growing mycobacteria | loinc | SITB TB 06, SITB TB 03 RO, SITB TB 04 | 3 |
| 221 | 23607-5 | Capreomycin [Susceptibility] by Method for Slow-growing mycobacteria | loinc | SITB TB 06, SITB TB 03 RO, SITB TB 04 | 3 |
| 222 | 53716-7 | levoFLOXacin [Susceptibility] by Method for Slow-growing mycobacteria | loinc | SITB TB 06, SITB TB 03 RO, SITB TB 04 | 3 |
| 223 | X099778 | Moxifloxacin High Dosage [Susceptibility] by Method for Slow-growing mycobacteria | kemkes examination | SITB TB 06, SITB TB 03 RO, SITB TB 04 | 3 |
| 224 | 41502-6 | Moxifloxacin [Susceptibility] by Method for Slow-growing mycobacteria | loinc | SITB TB 06, SITB TB 03 RO, SITB TB 04 | 3 |
| 225 | SP000472 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya | kemkes sp | SITB TB 06, SITB TB 03 RO, SITB TB 04 | 3 |
| 226 | SP000473 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 1 | kemkes sp | SITB TB 06, SITB TB 03 RO, SITB TB 04 | 3 |
| 227 | SP000474 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 2 | kemkes sp | SITB TB 06, SITB TB 03 RO, SITB TB 04 | 3 |
| 228 | SP000475 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 3 | kemkes sp | SITB TB 06, SITB TB 03 RO, SITB TB 04 | 3 |
| 229 | SP000476 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 4 | kemkes sp | SITB TB 06, SITB TB 03 RO, SITB TB 04 | 3 |
| 230 | SP000477 | Hasil Pemeriksaan Paket Standar Uji Kepekaan Lainnya 5 | kemkes sp | SITB TB 06, SITB TB 03 RO, SITB TB 04 | 3 |
| 231 | 106229004 | Qualifier for type of diagnosis | snomed | SITB TB 06, SITB TB 03 SO, SITB TB 16K, SITB TB 01 | 4 |
| 232 | tb-bac | Terkonfirmasi bakteriologis | kemkes tb-case-definition | SITB TB 06, SITB TB 03 SO, SITB TB 16K, SITB TB 01, ASIK CKG Lansia (27 Apr 2026) | 5 |
| 233 | tb-clin | Terdiagnosis klinis | kemkes tb-case-definition | SITB TB 06, SITB TB 03 SO, SITB TB 16K, SITB TB 01, ASIK CKG Lansia (27 Apr 2026) | 5 |
| 234 | TK000022 | Akan diobati/dirujuk | kemkes | SITB TB 06, SITB TB 02 | 2 |
| 235 | 699618001 | Administration of prophylactic antituberculosis agent | snomed | SITB TB 06 | 1 |
| 236 | 266714009 | Previous treatment continue | snomed | SITB TB 06 | 1 |
| 237 | SP001136 | Belum Mulai Pengobatan | kemkes sp | SITB TB 06 | 1 |
| 238 | 406149000 | Medication declined | snomed | SITB TB 06 | 1 |
| 239 | 399307001 | Lost to follow-up | snomed | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 16K, SITB TB 01 | 5 |
| 240 | 365866002 | Finding of human immunodeficiency virus status | snomed | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 01 | 4 |
| 241 | 165816005 | Human immunodeficiency virus detected | snomed | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, ePus Kunjungan Ibu Hamil, ePus ANC, ePus MTBS, ePus MTBM, SITB TB 01 | 8 |
| 242 | 165815009 | Human immunodeficiency virus not detected | snomed | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, ePus Kunjungan Ibu Hamil, ePus ANC, SITB TB 01 | 6 |
| 243 | SP000046 | Terapi Antiretroviral (ART) | kemkes sp | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, ePus Kunjungan Ibu Hamil, ePus INC, ePus PNC, SITB TB 01, SIM RS Panti Nugroho PNC, SIM RS PKU INC, SIM RS PKU PNC | 10 |
| 244 | SP000047 | Hasil Tes Diabetes Melitus | kemkes sp | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 01 | 4 |
| 245 | 225368008 | Contact tracing | snomed | SITB TB 03 SO (2x), SITB TB 03 RO (2x), SITB TB 16K, SISMAL Regmal 1, SISMAL Validasi Indigenous | 5 |
| 246 | 85658-3 | Occupation [Type] | loinc | SITB TB 03 SO, SITB TB 03 RO, ePus Pelayanan Pasien, SIPTM, SIHEPI Rekap 3e, SISMAL Regmal 1 | 6 |
| 247 | 106540006 | Laborer | snomed | SITB TB 03 SO, SITB TB 03 RO, SIPTM | 3 |
| 248 | 106304008 | Teacher | snomed | SITB TB 03 SO (2x), SITB TB 03 RO (2x), SIPTM | 3 |
| 249 | 106305009 | University/higher education teacher | snomed | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 250 | 444168002 | Homemaker | snomed | SITB TB 03 SO, SITB TB 03 RO, SIPTM, SISMAL Regmal 1 | 4 |
| 251 | OV000430 | Pegawai Swasta/ BUMN/ BUMD | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 252 | 65853000 | Student | snomed | SITB TB 03 SO, SITB TB 03 RO, SIPTM, SISMAL Regmal 1 | 4 |
| 253 | 106386007 | Agricultural animal husbandry/forestry worker, fisherman/hunter | snomed | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 254 | 106388008 | Farmer | snomed | SITB TB 03 SO, SITB TB 03 RO, SIPTM, SISMAL Regmal 1 | 4 |
| 255 | 36625000 | Livestock worker | snomed | SITB TB 03 SO, SITB TB 03 RO, SIPTM | 3 |
| 256 | 77715000 | Fisherman | snomed | SITB TB 03 SO, SITB TB 03 RO, SIPTM, SISMAL Regmal 1 | 4 |
| 257 | 236297007 | Civil servant | snomed | SITB TB 03 SO, SITB TB 03 RO, Dapodik PAUD, SIPTM | 4 |
| 258 | OV000431 | Siswa Berasrama | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 259 | 236320001 | Vehicle driver (occupation) | snomed | SITB TB 03 SO, SITB TB 03 RO, SIPTM | 3 |
| 260 | OV000432 | Tenaga Profesional Nonmedis | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 261 | OV000433 | TNI/ Polri | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO, Dapodik PAUD | 3 |
| 262 | OV000434 | Warga Binaan Pemasyarakatan | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 263 | 160906004 | Self-employed | snomed | SITB TB 03 SO, SITB TB 03 RO, Dapodik PAUD, SIPTM, SIHEPI Rekap 3e | 5 |
| 264 | 741062008 | Not in labor force | snomed | SITB TB 03 SO, SITB TB 03 RO, SIHEPI Rekap 3e | 3 |
| 265 | 82810-3 | Pregnancy status | loinc | SITB TB 03 SO, SITB TB 03 RO, SITB TB 01, SIM RS Panti Nugroho Stroke, SIM RS MPH Diabetes Melitus, SIM RS MPH Hipertensi, SISMAL Regmal 1 | 7 |
| 266 | LA15173-0 | Pregnant | loinc | SITB TB 03 SO, SITB TB 03 RO, SITB TB 01, SIM RS Panti Nugroho Stroke, SIM RS MPH Diabetes Melitus, SIM RS MPH Hipertensi, SISMAL Regmal 1 | 7 |
| 267 | LA26683-5 | Not Pregnant | loinc | SITB TB 03 SO, SITB TB 03 RO, SITB TB 01, SIM RS Panti Nugroho Stroke, SIM RS MPH Diabetes Melitus, SIM RS MPH Hipertensi, SISMAL Regmal 1 | 7 |
| 268 | CP000006 | Paduan OAT | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO, SITB TB 01, SITB TB 02 | 4 |
| 269 | CP000007 | OAT Kategori 1 | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO, SITB TB 01 | 3 |
| 270 | CP000008 | OAT Kategori 2 | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO, SITB TB 01 | 3 |
| 271 | CP000009 | OAT Kategori Anak | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO, SITB TB 01 | 3 |
| 272 | CP000010 | OAT Paduan tidak standar TB SO | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 273 | CP000011 | OAT Paduan Jangka Pendek | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 274 | CP000012 | OAT Paduan Jangka Panjang | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 275 | CP000013 | OAT Paduan Individual | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 276 | CP000014 | OAT Paduan Monoresistan INH | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 277 | CP000005 | Paduan Pengobatan | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 278 | CP000015 | 2(HRZE)/4(HR)3 | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 279 | CP000016 | 2(HRZE)/4(HR) - KDT Dosis Harian | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 280 | CP000017 | 2(HRZE)S/(HRZE)/5(HRE) | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 281 | CP000018 | 2(HRZE)S/(HRZE)/5((HR)3E3) | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 282 | CP000019 | 2HRZE/4HR | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 283 | CP000020 | 2HRZES/HRZE/ 5H3R3E3 | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 284 | CP000021 | 2(HRZ)/4(HR) | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 285 | CP000022 | 2(HRZ)/4(HR) | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 286 | CP000023 | Km Cs Eto Lfx Z VitB6 | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 287 | CP000024 | Km Cs Eto Lfx PAS E Z VitB6 | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 288 | CP000025 | Km Cs Eto Lfx E Z VitB6 | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 289 | CP000026 | Km Cs Eto Mfx PAS Z VitB6 | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 290 | CP000027 | Km Cs Eto Mfx PAS E VitB6 | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 291 | CP000028 | Cm Cs Eto Lfx E Z Vit B6 | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 292 | CP000029 | Cm Cs Eto Lfx PAS Z VitB6 | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 293 | CP000030 | Cm Cs Eto Mfx Z VitB6 | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 294 | CP000031 | Cm Cs Eto Mfx PAS Z VitB6 | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 295 | CP000032 | Km Eto Cs PAS Z Bdq | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 296 | CP000033 | Lfx Eto Cs PAS Z Bdq | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 297 | CP000034 | Eto Cs PAS Z Bdq Lnz Clf | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 298 | CP000035 | Km Lfx (Eto/CS/PAS) Z Bdq (Lnz/Clf) | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 299 | CP000036 | 5 Km Mfx(h) Eto Cfz Z H(h) E/ 5Mfx(h) Cfz Z E | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 300 | CP000037 | 6 Dlm Lfx Eto Cs ZE B6/ 18 Lfx Eto Cs ZE B6 | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 301 | CP000038 | 10 Cm Dlm Lzd Eto Cs Z E B6/14 Lzd Eto Cs Z E B6 | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 302 | CP000039 | 6 Dlm Lzd Cfz Eto Cs PAS ZE B6/ 18 lzd Cfz Eto Cs PAS Z E B6 | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 303 | CP000040 | Etambutol | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 304 | CP000041 | Paduan TPT 6Lfx 250 mg + E 400 mg Dewasa | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 305 | CP000042 | 6 Bdq-Lfx-Lzd-Cfz-Cs-VitB6 / 14 Lfx-Cfz-Cs-VitB6 | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 306 | CP000043 | 6 Bdq-Lfx-Cfz-Cs-E -VitB6/ 14 Lfx-Cfz-Cs-E-VitB6 | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 307 | CP000044 | 6 Bdq-Lfx-Lzd-Cfz-E / 14 Lfx-Cfz-E | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 308 | CP000045 | 6 Bdq-Mfx-Lzd-Cfz-E / 14 Mfx-Cfz-E | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 309 | CP000046 | 6 Bdq-Lzd-Cfz-Cs-E-VitB6 / 14 Lzd-Cfz-Cs-E -VitB6 | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 310 | CP000047 | 6 Bdq-Lzd-Cfz-Cs-Eto / 14 Lzd-Cfz-Cs-Eto- Vit B6 | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 311 | CP000048 | 6 Dlm-Lfx-Lzd-Clz-Cs / 14 Lfx-Lzd-Clz-Cs -VitB6 | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 312 | CP000049 | 20 Lfx-Lzd-Cfz-Cs-Eto -VitB6 | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 313 | CP000050 | 20 Mfx-Lzd-Cfz-Cs-E -VitB6 | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 314 | CP000051 | 20 Mfx-Lzd-Cfz-Cs-Z -VitB6 | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 315 | CP000052 | 6 Lfx-Lzd-Cfz-Cs-Amk-VitB6 / 14 Lfx-Lzd-Clz-Cs-VitB6 | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 316 | CP000053 | 6 Lfx-Lzd-Cfz-Cs-S-VitB6 / 14 Lfx-Lzd-Clz-Cs-VitB6 | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 317 | CP000054 | 6 Lfx-Lzd-Cfz-Eto-PAS / 14 Lfx-Lzd-Clz-Eto | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 318 | CP000055 | 6 Dlm-Lzd-Cfz-Cs-E / 14 Lzd-Clz-Cs-E-Vit B6 | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 319 | CP000056 | Pro TB 3 | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 320 | CP000057 | 6 Bdq-Lfx-Lzd-Cfz-H(Hdose)-Z-E/5 Lfx-Cfz-Z-E | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 321 | CP000058 | 6 Dlm-Lzd-Cfz-Cs-E / 14 Lzd-Clz-Cs-E-Vit B6 | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 322 | CP000059 | 6 Dlm-Lfx-Lzd-Clz-Cs / 14 Lfx-Lzd-Clz-Cs -VitB6 | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 323 | CP000060 | 6 Bdq-Lfx-Eto-E-Z-Hh-Cfz/ 5 Lfx)-Cfz-Z-E (STR Non Inj) | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 324 | CP000061 | 6 Bdq-Mfx-Eto-E-Z-Hh-Cfz/ 5-Mfx-Cfz-Z-E (STR Non Inj) | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 325 | CP000062 | Paduan TPT 6H 100 mg (INH) | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 326 | CP000063 | Paduan TPT 3HP Lepasan | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 327 | CP000064 | Paduan TPT 6H 300 mg (INH) | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 328 | CP000065 | Paduan TPT 6Lfx 250mg | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 329 | CP000066 | Paduan TPT 3HR KDT | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 330 | CP000067 | Paduan TPT 3HR KDT | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 331 | CP000068 | 5 Lfx-Lzd-Cfz-Cs / 5 Lfx-Cfz-Cs | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 332 | CP000069 | 6 Lfx-Lzd-Cfz-Cs-Eto / 12 Lfx-Cfz-Cs-Eto | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 333 | CP000070 | 6 Lzd-Cfz-Cs-Eto / 5 Cfz-Cs-Eto | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 334 | CP000071 | 6 Lzd-Cfz-Cs-Eto / 12 Cfz-Cs-Eto | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 335 | CP000072 | 5 Lfx-Lzd-Cfz-Cs-Dlm / 5 Lfx-Cfz-Cs | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 336 | CP000073 | 6 Lfx-Lzd-Cfz-Cs-Dlm / 12 Lfx-Cfz-Cs | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 337 | CP000074 | 5 Lzd-Cfz-Cs-Dlm-Eto/5 Cfz-Cs-Eto | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 338 | CP000075 | 6 Lzd-Cfz-Cs-Dlm-Eto/ 12 Cfz-Cs-Eto | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 339 | CP000076 | 6 Bdq-Lfx-Lzd-Cfz-Cs / 5 Lfx-Cfz- Cs | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 340 | CP000077 | 6 Bdq-Lfx-Lzd-Cfz-Cs / 12 Lfx-Cfz-Cs | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 341 | CP000078 | 6 Bdq-Lzd-Cfz-Cs-PAS / 5 Cfz-Cs-PAS | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 342 | CP000079 | 6 Bdq-Lzd-Cfz-Cs- PAS / 12 Cfz-Cs-PAS | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 343 | CP000080 | Paduan TPT 6Lfx 100 mg + E 100 mg | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 344 | CP000081 | Paduan TPT 6Lfx 100mg | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 345 | CP000082 | Paduan TPT 3HR 300mg/450mg Lepasan | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 346 | CP000083 | Paduan TPT 3HR 300mg/600mg Lepasan | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 347 | CP000084 | RHZE (150/75/400/275) + Levofloxacin | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 348 | CP000085 | Bedaquline Pretomanid Linezolid (BPAL) | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 349 | CP000086 | Bedaquline Pretomanid Linezolid Moxifloxacin (BPALM) | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 350 | CP000087 | Paduan TPT 1HP 300mg/300mg Lepasan | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 351 | CP000088 | Paduan TPT 1HP 300mg/150mg Lepasan | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 352 | CP000089 | 6 BDQ-Lfx-Cfz-Hdt-Z-E-Lzd(2 bulan)/ 5 Lfx-Cfz-Z-E | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 353 | CP000090 | 2HPMZ/2HPM | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 354 | SP001137 | Paduan lainnya | kemkes sp | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 355 | SP000795 | Sumber Obat | kemkes sp | SITB TB 03 SO, SITB TB 01 | 2 |
| 356 | SP000791 | Program TBC | kemkes sp | SITB TB 03 SO, SITB TB 01 | 2 |
| 357 | SP000792 | Asuransi | kemkes sp | SITB TB 03 SO, SITB TB 01 | 2 |
| 358 | SP000793 | Bayar Sendiri | kemkes sp | SITB TB 03 SO, SITB TB 01 | 2 |
| 359 | 371001000 | Patient cured | snomed | SITB TB 03 SO, SITB TB 03 RO, SITB TB 16K, SITB TB 01 | 4 |
| 360 | 182992009 | Treatment completed | snomed | SITB TB 03 SO, SITB TB 03 RO, SITB TB 16K, SITB TB 01 | 4 |
| 361 | CP000094 | Pengobatan Gagal | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO, SITB TB 16K, SITB TB 01 | 4 |
| 362 | CP000096 | Tidak dievaluasi/pindah | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO, SITB TB 16K, SITB TB 01 | 4 |
| 363 | TK000016 | Edukasi Tes HIV | kemkes | SITB TB 03 SO, ePus Kunjungan Ibu Hamil, SITB TB 01 | 3 |
| 364 | SP000371 | Cotrimoxazole | kemkes sp | SITB TB 03 SO, SITB TB 03 RO, SITB TB 01 | 3 |
| 365 | 1284985006 | Diabetes mellitus management program | snomed | SITB TB 03 SO, SITB TB 03 RO, SITB TB 01 | 3 |
| 366 | SP000372 | Obat Hipoglikemik Oral | kemkes sp | SITB TB 03 SO, SITB TB 03 RO, SITB TB 01 | 3 |
| 367 | 308755006 | Subcutaneous injection of insulin | snomed | SITB TB 03 SO, SITB TB 03 RO, SITB TB 01 | 3 |
| 368 | SP000797 | Pindah Register Pasien TB RO | kemkes sp | SITB TB 03 SO, SITB TB 01 | 2 |
| 369 | 17621005 | Normal | snomed | SITB TB 03 RO, ePus Tumbang Anak (5x), ePus Tumbang DDTK (6x) | 3 |
| 370 | 2483006 | Cavity | snomed | SITB TB 03 RO | 1 |
| 371 | 27925004 | Nodule | snomed | SITB TB 03 RO | 1 |
| 372 | 1255665007 | Moderate | snomed | SITB TB 03 RO | 1 |
| 373 | 47604008 | Miliary tuberculosis | snomed | SITB TB 03 RO | 1 |
| 374 | 30746006 | Lymphadenopathy | snomed | SITB TB 03 RO | 1 |
| 375 | 260544000 | Endobronchial (qualifier value) | snomed | SITB TB 03 RO | 1 |
| 376 | 112674009 | Fibrosis | snomed | SITB TB 03 RO | 1 |
| 377 | 442110002 | Fibrosis of pleura | snomed | SITB TB 03 RO | 1 |
| 378 | 1303092009 | Pulmonary bulla | snomed | SITB TB 03 RO | 1 |
| 379 | 60046008 | Pleural effusion | snomed | SITB TB 03 RO | 1 |
| 380 | 36118008 | Pneumothorax | snomed | SITB TB 03 RO | 1 |
| 381 | 12295008 | Bronchiectasis | snomed | SITB TB 03 RO | 1 |
| 382 | 46621007 | Atelectasis | snomed | SITB TB 03 RO | 1 |
| 383 | 9656002 | Consolidation | snomed | SITB TB 03 RO | 1 |
| 384 | 309529002 | Lung mass | snomed | SITB TB 03 RO | 1 |
| 385 | 385633008 | Improving | snomed | SITB TB 03 RO | 1 |
| 386 | 230993007 | Worsening | snomed | SITB TB 03 RO | 1 |
| 387 | 58158008 | Stable | snomed | SITB TB 03 RO | 1 |
| 388 | 171126009 | Tuberculosis screening | snomed | SITB TB 04 | 1 |
| 389 | SRR000013 | Pemeriksaan Diagnosis Baseline | kemkes clinical-term | SITB TB 04 (16x), ePus Tumbang DDTK | 2 |
| 390 | SRR000007 | Pemeriksaan Diagnosis | kemkes clinical-term | SITB TB 04 (32x), ePus Tumbang DDTK | 2 |
| 391 | SRR000009 | Pemeriksaan Ulang | kemkes clinical-term | SITB TB 04 (48x), ePus Tumbang DDTK, SITB TB 02 | 3 |
| 392 | SRR000008 | Follow Up | kemkes clinical-term | SITB TB 04 (48x), ePus Tumbang DDTK | 2 |
| 393 | SRR000010 | Akhir Pengobatan | kemkes clinical-term | SITB TB 04 (16x), ePus Tumbang DDTK | 2 |
| 394 | 418564007 | Pleural fluid specimen | snomed | SITB TB 04 (16x) | 1 |
| 395 | 258450006 | Cerebrospinal fluid specimen | snomed | SITB TB 04 (16x), ePus Laboratorium | 2 |
| 396 | 119376003 | Tissue specimen | snomed | SITB TB 04 (16x), ePus Laboratorium (2x) | 2 |
| 397 | 309508006 | Soft tissue lesion fine needle aspirate specimen | snomed | SITB TB 04 (16x), ePus Laboratorium | 2 |
| 398 | 168137004 | Gastric aspirate specimen | snomed | SITB TB 04 (16x), ePus Laboratorium | 2 |
| 399 | 119303007 | Microbial isolate specimen | snomed | SITB TB 04 (16x), ePus Laboratorium | 2 |
| 400 | ST000001 | Sputum Pagi | kemkes clinical-term | SITB TB 04 (16x) | 1 |
| 401 | ST000002 | Sputum Sewaktu | kemkes clinical-term | SITB TB 04 (16x) | 1 |
| 402 | 123038009 | Specimen | snomed | SITB TB 04 (16x) | 1 |
| 403 | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | kemkes sp | SITB TB 04 (6x) | 1 |
| 404 | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | kemkes sp | SITB TB 04 (6x) | 1 |
| 405 | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | kemkes sp | SITB TB 04 (6x) | 1 |
| 406 | 46246-5 | Mycobacterium tuberculosis katG gene isoniazid high level resistance mutation [Identifier] by Molecular method | loinc | SITB TB 04 | 1 |
| 407 | 63072-3 | Mycobacterium tuberculosis inhA gene isoniazid low level resistance mutation [Presence] by Molecular method | loinc | SITB TB 04 | 1 |
| 408 | X099783 | H Dosis Tinggi (High) | kemkes examination | SITB TB 04 | 1 |
| 409 | 103960-1 | Prothionamide [Susceptibility] by Genotype method | loinc | SITB TB 04 | 1 |
| 410 | X099389 | Hasil Pemeriksaan Biakan TB (Metode: LJ) | kemkes examination | SITB TB 04 (3x) | 1 |
| 411 | X099390 | Hasil Pemeriksaan Biakan TB (Metode: MGIT) | kemkes examination | SITB TB 04 (3x) | 1 |
| 412 | OM000001 | LJ | kemkes clinical-term | SITB TB 04 | 1 |
| 413 | OM000002 | MGIT | kemkes clinical-term | SITB TB 04 | 1 |
| 414 | 20373-7 | Amikacin [Susceptibility] by Method for Slow-growing mycobacteria | loinc | SITB TB 04 | 1 |
| 415 | SP000373 | Kader Kesehatan | kemkes sp | SITB TB 16K, ePus Kunjungan Ibu Hamil, SISMAL Regmal 1 | 3 |
| 416 | 415759006 | Tuberculosis index case | snomed | SITB TB 16K | 1 |
| 417 | 185389009 | Follow-up visit | snomed | SITB TB 16K, ePus INC, ePus MTBS, ePus MTBM, SITB TB 02, ELSMIL Ibu Hamil, SISMAL Regmal 1 | 7 |
| 418 | 737492002 | Outpatient care management | snomed | SITB TB 16K, ePus Kunjungan Ibu Hamil, ePus Tumbang DDTK, SIPTM (2x), SIHEPI Rekap 3e, eKohort INC | 6 |
| 419 | Z20.1 | Contact with and exposure to tuberculosis | icd-10 | SITB TB 16K | 1 |
| 420 | SP000200 | Invitasi kontak | kemkes sp | SITB TB 16K | 1 |
| 421 | 439708006 | Home visit | snomed | SITB TB 16K, SISMAL Regmal 1 | 2 |
| 422 | SP000369 | Kontak Dengan Penderita TBC | kemkes sp | SITB TB 16K | 1 |
| 423 | SP000201 | Kontak Serumah | kemkes sp | SITB TB 16K, ASIK CKG Lansia (27 Apr 2026) | 2 |
| 424 | SP000202 | Kontak Erat | kemkes sp | SITB TB 16K | 1 |
| 425 | SP000206 | Dirujuk Pemeriksaan Terduga TBC | kemkes sp | SITB TB 16K | 1 |
| 426 | 171400006 | Examination for suspected tuberculosis | snomed | SITB TB 16K | 1 |
| 427 | SP000207 | Hasil Pemeriksaan Terduga | kemkes sp | SITB TB 16K | 1 |
| 428 | SP000208 | Tidak TBC | kemkes sp | SITB TB 16K, SITB TB 01 | 2 |
| 429 | SP000209 | Memenuhi syarat rujukan pemeriksaan Eligibilitas TPT | kemkes sp | SITB TB 16K | 1 |
| 430 | SP000210 | Kesimpulan Hasil Pemeriksaan Eligibilitas TPT | kemkes sp | SITB TB 16K | 1 |
| 431 | SP000211 | Memenuhi syarat TPT | kemkes sp | SITB TB 16K | 1 |
| 432 | SP000374 | Tidak Memenuhi Syarat TPT | kemkes sp | SITB TB 16K | 1 |
| 433 | SP000212 | Tanggal Pemberian TPT | kemkes sp | SITB TB 16K | 1 |
| 434 | SP000213 | Hasil Akhir TPT | kemkes sp | SITB TB 16K | 1 |
| 435 | 64710-7 | Was your pregnancy a live birth, stillbirth, miscarriage, abortion, or ectopic pregnancy [PhenX] | loinc | MPDN Kematian Bayi, eKohort INC | 2 |
| 436 | 276507005 | Fetal death | snomed | MPDN Kematian Bayi | 1 |
| 437 | 276506001 | Newborn death | snomed | MPDN Kematian Bayi, eKohort INC | 2 |
| 438 | 39016-1 | Age at death | loinc | MPDN Kematian Bayi, MPDN Kematian Ibu | 2 |
| 439 | SP000716 | Umur Jam (saat meninggal) | kemkes sp | MPDN Kematian Bayi | 1 |
| 440 | SP000717 | Umur Menit (saat meninggal) | kemkes sp | MPDN Kematian Bayi | 1 |
| 441 | SP000718 | Umur Detik (saat meninggal) | kemkes sp | MPDN Kematian Bayi | 1 |
| 442 | TK000019 | Kode group | kemkes | MPDN Kematian Bayi, MPDN Kematian Ibu | 2 |
| 443 | TK000020 | Kode subgroup | kemkes | MPDN Kematian Bayi | 1 |
| 444 | TK000021 | Kode detail | kemkes | MPDN Kematian Bayi, MPDN Kematian Ibu | 2 |
| 445 | OC000028 | Jenis Tempat Meninggal | kemkes clinical-term | MPDN Kematian Bayi, MPDN Kematian Ibu | 2 |
| 446 | LT000008 | Dalam perjalanan dari rumah/masyarakat | location-type | MPDN Kematian Bayi (2x), MPDN Kematian Ibu, ePus ANC, ePus INC, ePus PNC, SiGizi Kohort Ibu, SIM RS Panti Nugroho INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 9 |
| 447 | LT000009 | Dalam perjalanan ke faskes lain | location-type | MPDN Kematian Bayi (2x), MPDN Kematian Ibu, ePus INC, SiGizi Kohort Ibu, SIM RS Panti Nugroho INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 7 |
| 448 | SP000099 | FASKES | kemkes sp | MPDN Kematian Bayi (2x), MPDN Kematian Ibu | 2 |
| 449 | 102 | Pusat Kesehatan Masyarakat | organization-type | MPDN Kematian Bayi (2x), MPDN Kematian Ibu, ePus ANC, ePus INC, ePus PNC, ELSMIL Pasca Persalinan, SIHEPI Rekap 3e, SiGizi Kohort Ibu | 8 |
| 450 | OT000006 | Rumah Sakit Pemerintah | organization-type | MPDN Kematian Bayi (2x), MPDN Kematian Ibu, ePus INC, SIM RS Panti Nugroho INC, SIM RS PKU INC | 5 |
| 451 | OT000007 | Rumah Sakit Swasta | organization-type | MPDN Kematian Bayi (2x), MPDN Kematian Ibu, ePus INC, SIM RS Panti Nugroho INC, SIM RS PKU INC | 5 |
| 452 | LT000006 | Rumah Ibu | location-type | MPDN Kematian Bayi (2x), MPDN Kematian Ibu, ePus INC, SIM RS Panti Nugroho INC, SIM RS PKU INC | 5 |
| 453 | 104 | Rumah Sakit | organization-type | MPDN Kematian Bayi (2x), MPDN Kematian Ibu, SIHEPI Rekap 3e, SiGizi Kohort Ibu | 4 |
| 454 | OT000002 | Pustu | organization-type | MPDN Kematian Bayi (2x), MPDN Kematian Ibu, ePus ANC, ePus INC, ePus PNC, SIHEPI Rekap 3e, SiGizi Kohort Ibu, SIM RS Panti Nugroho INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 10 |
| 455 | OT000010 | Klinik Medis Utama | organization-type | MPDN Kematian Bayi (2x), MPDN Kematian Ibu, ePus INC, SIM RS Panti Nugroho INC, SIM RS PKU INC | 5 |
| 456 | OT000011 | Klinik Medis Pratama | organization-type | MPDN Kematian Bayi (2x), MPDN Kematian Ibu, ePus INC, SIM RS Panti Nugroho INC, SIM RS PKU INC | 5 |
| 457 | 103 | Klinik | organization-type | MPDN Kematian Bayi (2x), MPDN Kematian Ibu, ePus ANC, ePus INC, ePus PNC, SIHEPI Rekap 3e, SiGizi Kohort Ibu | 7 |
| 458 | 101 | Tempat Praktik Mandiri Tenaga Kesehatan | organization-type | MPDN Kematian Bayi (2x), MPDN Kematian Ibu, ePus INC, SISMAL Regmal 1 | 4 |
| 459 | OT000004 | Bidan Praktek Mandiri | organization-type | MPDN Kematian Bayi (2x), MPDN Kematian Ibu, ELSMIL Pasca Persalinan, SIHEPI Rekap 3e, SiGizi Kohort Ibu | 5 |
| 460 | OT000008 | Rumah Bersalin | organization-type | MPDN Kematian Bayi (2x), MPDN Kematian Ibu, ePus ANC, ePus INC, ePus PNC, SIHEPI Rekap 3e, SiGizi Kohort Ibu, SIM RS Panti Nugroho INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 10 |
| 461 | 394573001 | Maternity clinic | snomed | MPDN Kematian Bayi (2x), MPDN Kematian Ibu, ePus INC | 3 |
| 462 | OT000001 | Polindes | organization-type | MPDN Kematian Bayi (2x), MPDN Kematian Ibu, ePus ANC, ePus INC, ePus PNC, SIHEPI Rekap 3e, SiGizi Kohort Ibu, SIM RS Panti Nugroho INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 10 |
| 463 | 264362003 | Home | snomed | MPDN Kematian Bayi (2x), MPDN Kematian Ibu, ePus ANC, ePus INC, ePus PNC, SIHEPI Rekap 3e, SiGizi PMT 2025 BB Tidak Naik - Survey, SiGizi PMT 2025 BB Kurang - Survey, SiGizi PMT 2025 Gizi Kurang - Survey, SiGizi Kohort Ibu | 10 |
| 464 | LT000007 | Rumah Dukun | location-type | MPDN Kematian Bayi (2x), MPDN Kematian Ibu, ePus INC, SiGizi Kohort Ibu, SIM RS Panti Nugroho INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 7 |
| 465 | LT000010 | Lainnya | location-type | MPDN Kematian Bayi (2x), MPDN Kematian Ibu, ePus INC, SIM RS Panti Nugroho INC, SIM RS PKU INC | 5 |
| 466 | LT000011 | Belum Tahu | location-type | MPDN Kematian Bayi (2x), MPDN Kematian Ibu, ePus INC, SIM RS Panti Nugroho INC, SIM RS PKU INC | 5 |
| 467 | SP000098 | Tipe Penyelenggara Faskes Meninggal | kemkes sp | MPDN Kematian Bayi, MPDN Kematian Ibu | 2 |
| 468 | SP000076 | RSU - Pemprop | kemkes sp | MPDN Kematian Bayi (2x), MPDN Kematian Ibu | 2 |
| 469 | SP000077 | PUSKESMAS - Pemkab | kemkes sp | MPDN Kematian Bayi (2x), MPDN Kematian Ibu | 2 |
| 470 | SP000078 | RSU - Pemkot | kemkes sp | MPDN Kematian Bayi (2x), MPDN Kematian Ibu | 2 |
| 471 | SP000079 | RSU - Pemkab | kemkes sp | MPDN Kematian Bayi (2x), MPDN Kematian Ibu | 2 |
| 472 | SP000080 | RSIA - Perusahaan | kemkes sp | MPDN Kematian Bayi (2x), MPDN Kematian Ibu | 2 |
| 473 | SP000081 | RSU - TNI AD | kemkes sp | MPDN Kematian Bayi (2x), MPDN Kematian Ibu | 2 |
| 474 | SP000082 | RS Bersalin - Swasta/Lainnya | kemkes sp | MPDN Kematian Bayi (2x), MPDN Kematian Ibu | 2 |
| 475 | SP000083 | RS - Organisasi Islam | kemkes sp | MPDN Kematian Bayi (2x), MPDN Kematian Ibu | 2 |
| 476 | SP000084 | RS Bersalin - Pemkab | kemkes sp | MPDN Kematian Bayi (2x), MPDN Kematian Ibu | 2 |
| 477 | SP000085 | RSU - Swasta/Lainnya | kemkes sp | MPDN Kematian Bayi (2x), MPDN Kematian Ibu | 2 |
| 478 | SP000086 | RSU - KEMENKES | kemkes sp | MPDN Kematian Bayi (2x), MPDN Kematian Ibu | 2 |
| 479 | SP000087 | RSU - Perusahaan | kemkes sp | MPDN Kematian Bayi (2x), MPDN Kematian Ibu | 2 |
| 480 | SP000088 | RSU - Organisasi Islam | kemkes sp | MPDN Kematian Bayi (2x), MPDN Kematian Ibu | 2 |
| 481 | SP000089 | RSU - Organisasi Sosial | kemkes sp | MPDN Kematian Bayi (2x), MPDN Kematian Ibu | 2 |
| 482 | SP000090 | RS - Swasta/Lainnya | kemkes sp | MPDN Kematian Bayi (2x), MPDN Kematian Ibu | 2 |
| 483 | 72150-6 | Delivery location | loinc | MPDN Kematian Bayi, ePus INC, SIHEPI Rekap 3e, SiGizi Kohort Ibu, SIM RS Panti Nugroho INC, SIM RS MPH BBL, SIM RS Siaga Medika INC, SIM RS PKU INC | 8 |
| 484 | 57071-3 | Obstetric delivery method | loinc | MPDN Kematian Bayi, ePus INC, SiGizi Kohort Ibu, SIM RS Narmada INC, SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 9 |
| 485 | 289259007 | Vaginal delivery | snomed | MPDN Kematian Bayi | 1 |
| 486 | 200144004 | Deliveries by cesarean | snomed | MPDN Kematian Bayi, ePus Kunjungan Ibu Hamil, ePus INC, ELSMIL Pasca Persalinan, eKohort INC, SiGizi Kohort Ibu | 6 |
| 487 | 48782003 | Delivery normal | snomed | MPDN Kematian Bayi, ePus Kunjungan Ibu Hamil, ePus INC, ELSMIL Pasca Persalinan, eKohort INC, SiGizi Kohort Ibu | 6 |
| 488 | OC000013 | Penolong Persalinan | kemkes clinical-term | MPDN Kematian Bayi, ePus INC, ELSMIL Pasca Persalinan, eKohort INC, SIM RS Panti Nugroho INC, SIM RS MPH INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 8 |
| 489 | 303071001 | Person in the family | snomed | MPDN Kematian Bayi, ePus Kunjungan Ibu Hamil, ePus INC | 3 |
| 490 | OV000012 | Dukun | kemkes clinical-term | MPDN Kematian Bayi, ePus Kunjungan Ibu Hamil, ePus INC, SIM RS Siaga Medika INC | 4 |
| 491 | 11935004 | Obstetrician Occupation | snomed | MPDN Kematian Bayi, ePus Kunjungan Ibu Hamil, ePus INC, ELSMIL Pasca Persalinan, eKohort INC | 5 |
| 492 | SP000075 | Tipe Penyelenggara Faskes Lahir | kemkes sp | MPDN Kematian Bayi | 1 |
| 493 | 57715-5 | Birth time | loinc | MPDN Kematian Bayi, ePus INC, SIM RS Tripat BBL (sheet 'INC BBL'), SIM RS Panti Nugroho BBL, SIM RS Ummu Hani BBL, SIM RS MPH BBL, SIM RS Siaga Medika BBL | 7 |
| 494 | 8339-4 | Birth weight Measured | loinc | MPDN Kematian Bayi, ePus INC, ASIK CKG Bayi Baru Lahir (v2), SiGizi Balita BNBA, SiGizi Balita Vitamin A, SIM RS Tripat BBL (sheet 'INC BBL'), SIM RS Narmada INC, SIM RS Panti Nugroho BBL, SIM RS Ummu Hani BBL, SIM RS MPH BBL, SIM RS Siaga Medika BBL | 11 |
| 495 | 11996-6 | [#] Pregnancies | loinc | MPDN Kematian Bayi, MPDN Kematian Ibu, ePus ANC, ePus PNC, SIHEPI Rekap 3e, SiGizi Kohort Ibu, SIM RS Tripat PNC, SIM RS Narmada INC (2x), SIM RS Narmada KIA, SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika INC, SIM RS Siaga Medika PNC, SIM RS PKU INC, SIM RS PKU PNC | 16 |
| 496 | ANC.B6.DE24 | Number of pregnancies (gravida) | WHO anc-custom-codes | MPDN Kematian Bayi, MPDN Kematian Ibu, SIHEPI Rekap 3e, SiGizi Kohort Ibu, SIM RS Tripat PNC, SIM RS Narmada INC (2x), SIM RS Narmada KIA, SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU INC, SIM RS PKU PNC | 13 |
| 497 | ANC.B6.DE17 | Gestational age | WHO anc-custom-codes | MPDN Kematian Bayi, ePus Kunjungan Ibu Hamil, ePus ANC, ELSMIL Ibu Hamil, SIHEPI Rekap 3e, eKohort ANC, SIM RS Tripat ANC, SIM RS Narmada INC, SIM RS Narmada KIA, SIM RS Ummu Hani ANC, SIM RS MPH ANC | 11 |
| 498 | 57722-1 | Birth plurality of Pregnancy | loinc | MPDN Kematian Bayi | 1 |
| 499 | 237244005 | Single pregnancy | snomed | MPDN Kematian Bayi | 1 |
| 500 | 65147003 | Twin pregnancy | snomed | MPDN Kematian Bayi | 1 |
| 501 | 64254006 | Triplet pregnancy | snomed | MPDN Kematian Bayi | 1 |
| 502 | OV000394 | Kehamilan Ganda Empat atau Lebih | snomed | MPDN Kematian Bayi | 1 |
| 503 | 30525-0 | Age | loinc | MPDN Kematian Bayi, ePus INC | 2 |
| 504 | COM000002 | Formulir Informasi Kematian Perinatal Lahir Mati | composition-type | MPDN Kematian Bayi | 1 |
| 505 | COM000003 | Formulir Informasi Kematian Perinatal Lahir Hidup | composition-type | MPDN Kematian Bayi | 1 |
| 506 | OC000026 | Masa terjadi Kematian Ibu | kemkes clinical-term | MPDN Kematian Ibu | 1 |
| 507 | 1156679005 | Maternal antenatal period | snomed | MPDN Kematian Ibu | 1 |
| 508 | 1156682000 | Maternal intrapartum period | snomed | MPDN Kematian Ibu | 1 |
| 509 | 255410009 | Maternal postpartum | snomed | MPDN Kematian Ibu | 1 |
| 510 | COM000001 | Formulir Informasi Kematian Maternal | composition-type | MPDN Kematian Ibu | 1 |
| 511 | 161572004 | History of congenital anomaly | snomed | ePus Pelayanan Pasien | 1 |
| 512 | 51848-0 | Evaluation note | loinc | ePus Pelayanan Pasien | 1 |
| 513 | 61150-9 | Subjective Narrative | loinc | ePus Pelayanan Pasien | 1 |
| 514 | 72225-6 | Objective Narrative | loinc | ePus Pelayanan Pasien | 1 |
| 515 | 77977-7 | Illness duration | loinc | ePus Pelayanan Pasien | 1 |
| 516 | 72166-2 | Tobacco smoking status | loinc | ePus Pelayanan Pasien, ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan, SIM RS Narmada INC, SIM RS Narmada KIA | 5 |
| 517 | 77176002 | Smoker | snomed | ePus Pelayanan Pasien | 1 |
| 518 | 8392000 | Non-smoker | snomed | ePus Pelayanan Pasien | 1 |
| 519 | 11331-6 | History of Alcohol use | loinc | ePus Pelayanan Pasien, SIM RS Narmada INC, SIM RS Narmada KIA | 3 |
| 520 | 219006 | Current drinker | snomed | ePus Pelayanan Pasien, SIPTM | 2 |
| 521 | 105542008 | Non - drinker | snomed | ePus Pelayanan Pasien | 1 |
| 522 | 878899005 | Inadequate intake of plant fiber | loinc | ePus Pelayanan Pasien | 1 |
| 523 | 84635008 | Disease process or condition education | snomed | ePus Pelayanan Pasien | 1 |
| 524 | 10913 | Edukasi Kesehatan Individu | kemkes kptl | ePus Pelayanan Pasien | 1 |
| 525 | 67775-7 | Level of responsiveness | loinc | ePus Pelayanan Pasien, SIM RS Narmada INC | 2 |
| 526 | 248234008 | Mentally alert | snomed | ePus Pelayanan Pasien | 1 |
| 527 | LA9340-6 | Alert | loinc | ePus Pelayanan Pasien | 1 |
| 528 | 20602000 | Apathy | snomed | ePus Pelayanan Pasien | 1 |
| 529 | 2776000 | Delirium | snomed | ePus Pelayanan Pasien | 1 |
| 530 | 271782001 | Somnolence | snomed | ePus Pelayanan Pasien | 1 |
| 531 | LA25163-9 | Stuporous | loinc | ePus Pelayanan Pasien | 1 |
| 532 | 274659008 | Semicoma | snomed | ePus Pelayanan Pasien | 1 |
| 533 | 371632003 | Coma | snomed | ePus Pelayanan Pasien | 1 |
| 534 | LA9343-0 | Unresponsive | loinc | ePus Pelayanan Pasien | 1 |
| 535 | 75910-0 | Canadian triage and acuity scale [CTAS] | loinc | ePus Pelayanan Pasien, SIM RS Narmada INC | 2 |
| 536 | LA6113-0 | 2 | loinc | ePus Pelayanan Pasien | 1 |
| 537 | LA6114-8 | 3 | loinc | ePus Pelayanan Pasien | 1 |
| 538 | LA10137-0 | 5 | loinc | ePus Pelayanan Pasien, SIM RS Narmada INC | 2 |
| 539 | 276361009 | Waist circumference | snomed | ePus Pelayanan Pasien | 1 |
| 540 | 39156-5 | Body mass index (BMI) [Ratio] | loinc | ePus Pelayanan Pasien, ASIK Skrining PTM, ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) (2x), SIM RS Narmada KIA | 6 |
| 541 | 59575-1 | Body mass index (BMI) [Percentile] Per age | loinc | ePus Pelayanan Pasien | 1 |
| 542 | 248324001 | Well nourished | snomed | ePus Pelayanan Pasien, ePus MTBS, ePus Tumbang Anak, ePus Tumbang DDTK, SiGizi Balita BNBA, SiGizi Balita Vitamin A, SiGizi Balita Mendapat PMT 2024, SiGizi Balita MPASI, SiGizi PMT 2025 BB Tidak Naik - Riwayat (2x), SiGizi PMT 2025 BB Kurang - Riwayat (2x), SiGizi PMT 2025 Gizi Kurang - Riwayat (2x) | 11 |
| 543 | 248325000 | Undernourished | snomed | ePus Pelayanan Pasien, ePus MTBS, ePus Tumbang Anak, ePus Tumbang DDTK, SiGizi Balita BNBA, SiGizi Balita Vitamin A, SiGizi Balita Mendapat PMT 2024, SiGizi Balita MPASI, SiGizi PMT 2025 BB Tidak Naik - Riwayat (2x), SiGizi PMT 2025 BB Kurang - Riwayat (2x), SiGizi PMT 2025 Gizi Kurang - Riwayat (2x) | 11 |
| 544 | OI000001 | Gizi Buruk | kemkes clinical-term | ePus Pelayanan Pasien, ePus Tumbang Anak, ePus Tumbang DDTK, ASIK CKG Balita (v2) (3x), SiGizi Balita BNBA, SiGizi Balita Vitamin A, SiGizi Balita Mendapat PMT 2024, SiGizi Balita MPASI, SiGizi PMT 2025 BB Tidak Naik - Riwayat (2x), SiGizi PMT 2025 BB Kurang - Riwayat (2x), SiGizi PMT 2025 Gizi Kurang - Riwayat (2x) | 11 |
| 545 | 248342006 | Underweight | snomed | ePus Pelayanan Pasien, ePus Tumbang Anak, ASIK CKG Lansia (27 Apr 2026), SiGizi Balita BNBA, SiGizi Balita Vitamin A, SiGizi Balita Mendapat PMT 2024 (2x), SiGizi Balita MPASI, SiGizi PMT 2025 BB Tidak Naik - Riwayat (2x), SiGizi PMT 2025 BB Kurang - Riwayat (2x), SiGizi PMT 2025 Gizi Kurang - Riwayat (2x), SiGizi Kohort Ibu | 11 |
| 546 | 43664005 | Normal weight | snomed | ePus Pelayanan Pasien, ePus Tumbang Anak, SiGizi Balita BNBA, SiGizi Balita Vitamin A, SiGizi Balita Mendapat PMT 2024, SiGizi Balita MPASI, SiGizi PMT 2025 BB Tidak Naik - Riwayat (2x), SiGizi PMT 2025 BB Kurang - Riwayat (2x), SiGizi PMT 2025 Gizi Kurang - Riwayat (2x), SiGizi Kohort Ibu | 10 |
| 547 | 238131007 | Overweight | snomed | ePus Pelayanan Pasien, ePus MTBS, ePus Tumbang Anak, SiGizi Balita BNBA, SiGizi Balita Vitamin A, SiGizi Balita Mendapat PMT 2024, SiGizi Balita MPASI, SiGizi PMT 2025 BB Tidak Naik - Riwayat (2x), SiGizi PMT 2025 BB Kurang - Riwayat (2x), SiGizi PMT 2025 Gizi Kurang - Riwayat (2x), SiGizi Kohort Ibu | 11 |
| 548 | 414915002 | Obese | snomed | ePus Pelayanan Pasien, ePus MTBS, ePus Tumbang Anak, SiGizi Balita BNBA, SiGizi Balita Vitamin A, SiGizi Balita Mendapat PMT 2024, SiGizi Balita MPASI, SiGizi PMT 2025 BB Tidak Naik - Riwayat (2x), SiGizi PMT 2025 BB Kurang - Riwayat (2x), SiGizi PMT 2025 Gizi Kurang - Riwayat (2x), SiGizi Kohort Ibu | 11 |
| 549 | 8480-6 | Systolic blood pressure | loinc | ePus Pelayanan Pasien, ePus Kunjungan Ibu Hamil, ePus ANC, ePus INC, ePus PNC, SIPTM, ASIK Skrining PTM, ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026), eKohort ANC, eKohort INC, SIM RS Tripat ANC, SIM RS Tripat PNC, SIM RS Narmada INC, SIM RS Narmada KIA, SIM RS Panti Nugroho ANC, SIM RS Panti Nugroho INC, SIM RS Panti Nugroho PNC, SIM RS Panti Nugroho Stroke, SIM RS Ummu Hani ANC, SIM RS Ummu Hani INC, SIM RS Ummu Hani PNC, SIM RS MPH ANC, SIM RS MPH INC, SIM RS MPH PNC, SIM RS Siaga Medika ANC, SIM RS Siaga Medika INC, SIM RS PKU INC (2x), SIM RS PKU PNC | 30 |
| 550 | 8462-4 | Diastolic blood pressure | loinc | ePus Pelayanan Pasien, ePus Kunjungan Ibu Hamil, ePus ANC, ePus INC, ePus PNC, SIPTM, ASIK Skrining PTM, eKohort ANC, eKohort INC, SIM RS Tripat ANC, SIM RS Tripat PNC, SIM RS Narmada INC, SIM RS Narmada KIA, SIM RS Panti Nugroho ANC, SIM RS Panti Nugroho INC, SIM RS Panti Nugroho PNC, SIM RS Panti Nugroho Stroke, SIM RS Ummu Hani ANC, SIM RS Ummu Hani INC, SIM RS Ummu Hani PNC, SIM RS MPH ANC, SIM RS MPH INC, SIM RS MPH PNC, SIM RS Siaga Medika ANC, SIM RS Siaga Medika INC, SIM RS Siaga Medika PNC, SIM RS PKU INC, SIM RS PKU PNC | 28 |
| 551 | 9279-1 | Respiratory rate | loinc | ePus Pelayanan Pasien, ePus ANC, ePus INC, ePus PNC, ePus MTBS, ePus MTBM (2x), eKohort ANC, eKohort INC, SIM RS Tripat BBL (sheet 'INC BBL'), SIM RS Tripat PNC, SIM RS Narmada INC, SIM RS Narmada KIA, SIM RS Panti Nugroho INC, SIM RS Panti Nugroho PNC, SIM RS Panti Nugroho BBL, SIM RS Ummu Hani INC, SIM RS Ummu Hani PNC, SIM RS Ummu Hani BBL, SIM RS MPH INC, SIM RS MPH PNC, SIM RS MPH BBL, SIM RS Siaga Medika INC, SIM RS Siaga Medika PNC, SIM RS Siaga Medika BBL, SIM RS PKU INC, SIM RS PKU PNC | 26 |
| 552 | 8867-4 | Heart rate | loinc | ePus Pelayanan Pasien, ePus ANC, ePus INC, ePus PNC, eKohort ANC, eKohort INC, SIM RS Tripat BBL (sheet 'INC BBL'), SIM RS Tripat PNC, SIM RS Narmada INC, SIM RS Narmada KIA, SIM RS Panti Nugroho INC, SIM RS Panti Nugroho PNC, SIM RS Panti Nugroho BBL, SIM RS Ummu Hani INC, SIM RS Ummu Hani PNC, SIM RS Ummu Hani BBL, SIM RS MPH INC, SIM RS MPH PNC, SIM RS MPH BBL, SIM RS Siaga Medika INC, SIM RS Siaga Medika PNC, SIM RS Siaga Medika BBL, SIM RS PKU INC, SIM RS PKU PNC | 24 |
| 553 | 8884-9 | Heart rate rythm | loinc | ePus Pelayanan Pasien | 1 |
| 554 | 271636001 | Pulse regular | snomed | ePus Pelayanan Pasien | 1 |
| 555 | 61086009 | Pulse irregular | snomed | ePus Pelayanan Pasien | 1 |
| 556 | 8310-5 | Body temperature | loinc | ePus Pelayanan Pasien, ePus ANC, ePus PNC, ePus MTBS, ePus MTBM (2x), eKohort INC, SIM RS Tripat BBL (sheet 'INC BBL'), SIM RS Tripat PNC, SIM RS Narmada INC, SIM RS Narmada KIA, SIM RS Panti Nugroho BBL, SIM RS Ummu Hani BBL, SIM RS MPH BBL, SIM RS Siaga Medika INC, SIM RS Siaga Medika BBL, SISMAL Regmal 1 | 16 |
| 557 | 129861002 | Physical activity finding | snomed | ePus Pelayanan Pasien | 1 |
| 558 | 80316-3 | Pain scale [Type] | loinc | ePus Pelayanan Pasien | 1 |
| 559 | 81765008 | No pain | snomed | ePus Pelayanan Pasien | 1 |
| 560 | 40196000 | Mild pain | snomed | ePus Pelayanan Pasien (2x) | 1 |
| 561 | 50415004 | Moderate pain | snomed | ePus Pelayanan Pasien (2x) | 1 |
| 562 | 76948002 | Severe pain | snomed | ePus Pelayanan Pasien (2x) | 1 |
| 563 | 1991000124105 | Referred by self | snomed | ePus Pelayanan Pasien | 1 |
| 564 | outp | From outpatient department | http://terminology.hl7. org/CodeSystem/admit -source | ePus Pelayanan Pasien | 1 |
| 565 | SP000020 | Umur Bulan | kemkes sp | ePus Kunjungan Ibu Hamil, ePus MTBS, ePus MTBM, ePus Tumbang DDTK, SITB TB 01, SiGizi Balita BNBA, SiGizi Balita Vitamin A, SIM RS Panti Nugroho Hipertensi, SIM RS Panti Nugroho Stroke, SIM RS Goetoeng ANC, SIM RS Goetoeng PNC | 11 |
| 566 | SP000021 | Umur Hari | kemkes sp | ePus Kunjungan Ibu Hamil, ePus MTBS, ePus MTBM, ePus Tumbang DDTK, SiGizi Balita BNBA, SiGizi Balita Vitamin A, SIM RS Panti Nugroho Hipertensi, SIM RS Panti Nugroho Stroke, SIM RS Goetoeng ANC, SIM RS Goetoeng PNC | 10 |
| 567 | 32418-6 | Obstetric trimester Stated | loinc | ePus Kunjungan Ibu Hamil, ePus ANC, eKohort ANC | 3 |
| 568 | ANC.SS.DE13 | Trimester ke | kemkes anc-custom-codes | ePus Kunjungan Ibu Hamil, ePus ANC, eKohort ANC | 3 |
| 569 | hosp-trans | Transferred from other hospital | http://terminology.hl7.org/CodeSystem/admit-source | ePus Kunjungan Ibu Hamil, ePus ANC | 2 |
| 570 | 11881-0 | Uterus Fundal height Tape measure | loinc | ePus Kunjungan Ibu Hamil, ePus ANC, ePus INC, ELSMIL Ibu Hamil, eKohort ANC, eKohort INC, SIM RS Tripat PNC, SIM RS Narmada INC, SIM RS Narmada KIA, SIM RS Panti Nugroho ANC, SIM RS Panti Nugroho INC, SIM RS Panti Nugroho PNC, SIM RS Ummu Hani INC, SIM RS Ummu Hani PNC, SIM RS MPH ANC, SIM RS MPH INC, SIM RS MPH PNC, SIM RS Siaga Medika INC, SIM RS Siaga Medika PNC, SIM RS PKU INC, SIM RS PKU PNC | 21 |
| 571 | ANC.B8.DE105 | Symphysis-fundal height | WHO anc-custom-codes | ePus Kunjungan Ibu Hamil, ELSMIL Ibu Hamil, eKohort ANC, eKohort INC, SIM RS Narmada INC, SIM RS Narmada KIA, SIM RS MPH ANC | 7 |
| 572 | 32392-3 | Deep tendon reflex of Patellar | loinc | ePus Kunjungan Ibu Hamil | 1 |
| 573 | 55283-6 | Fetal Heart rate | loinc | ePus Kunjungan Ibu Hamil (2x), ePus ANC, ePus INC, eKohort ANC, SIM RS Narmada INC, SIM RS Narmada KIA, SIM RS Panti Nugroho ANC, SIM RS Panti Nugroho INC, SIM RS Ummu Hani ANC, SIM RS Ummu Hani INC, SIM RS MPH ANC, SIM RS MPH INC, SIM RS Siaga Medika ANC, SIM RS Siaga Medika INC, SIM RS PKU INC | 15 |
| 574 | ANC.B8.DE107 | Fetal heart rate | WHO anc-custom-codes | ePus Kunjungan Ibu Hamil (2x), ePus ANC, eKohort ANC, eKohort INC, SIM RS Narmada INC, SIM RS Narmada KIA, SIM RS Panti Nugroho ANC, SIM RS Ummu Hani ANC, SIM RS MPH ANC, SIM RS Siaga Medika ANC | 10 |
| 575 | 249111004 | Engagement of head | loinc | ePus Kunjungan Ibu Hamil (2x), eKohort INC | 2 |
| 576 | ANC.SS.DE46 | Kepala Terhadap PAP | WHO anc-custom-codes | ePus Kunjungan Ibu Hamil (2x), eKohort INC | 2 |
| 577 | 62098001 | Head not engaged | snomed | ePus Kunjungan Ibu Hamil (2x), ePus ANC, ePus INC, eKohort INC | 4 |
| 578 | 249112006 | Head engaged | snomed | ePus Kunjungan Ibu Hamil (2x), ePus ANC, ePus INC, eKohort INC | 4 |
| 579 | 89087-1 | Fetal Body weight Estimated | loinc | ePus Kunjungan Ibu Hamil (2x), ePus ANC, ELSMIL Ibu Hamil, eKohort ANC, SIM RS Narmada INC, SIM RS Narmada KIA | 6 |
| 580 | ANC.SS.DE1 | Taksiran Berat Janin (TBJ) | WHO anc-custom-codes | ePus Kunjungan Ibu Hamil (2x) | 1 |
| 581 | 6096002 | Breech presentation | snomed | ePus Kunjungan Ibu Hamil (2x), ePus ANC, ePus INC (2x), eKohort INC | 4 |
| 582 | 260415000 | Not detected | snomed | ePus Kunjungan Ibu Hamil, ePus ANC | 2 |
| 583 | 246435002 | Number of fetuses | snomed | ePus Kunjungan Ibu Hamil (2x) | 1 |
| 584 | ANC.B8.DE109 | Number of fetuses | WHO anc-custom-codes | ePus Kunjungan Ibu Hamil (2x), ePus ANC, SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika ANC | 6 |
| 585 | 99.38 | Administration of tetanus toxoid | icd-9-cm | ePus Kunjungan Ibu Hamil | 1 |
| 586 | SP000122 | Catat di Buku KIA | kemkes sp | ePus Kunjungan Ibu Hamil, ePus INC, ePus PNC, SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU INC, SIM RS PKU PNC | 9 |
| 587 | SP000115 | Pemeriksaan Laboratorium Thalassemia | kemkes sp | ePus Kunjungan Ibu Hamil (2x) | 1 |
| 588 | 94537-8 | Hemoglobin panel - Blood by HPLC | loinc | ePus Kunjungan Ibu Hamil | 1 |
| 589 | 718-7 | Hemoglobin [Mass/volume] in Blood | kemkes sp | ePus Kunjungan Ibu Hamil (2x) | 1 |
| 590 | 278977008 | Human immunodeficiency virus status | snomed | ePus Kunjungan Ibu Hamil, ePus ANC | 2 |
| 591 | 57071-3 | Obstetric delivery method | https://loinc.org | ePus Kunjungan Ibu Hamil, ELSMIL Pasca Persalinan, eKohort INC | 3 |
| 592 | 72178-7 | Given a mosquito net [RHEA] | loinc | ePus Kunjungan Ibu Hamil | 1 |
| 593 | 70569-9 | Plasmodium sp Ag [Identifier] in Blood by Rapid immunoassay | loinc | ePus Kunjungan Ibu Hamil (6x) | 1 |
| 594 | 119297000 | Blood specimen | snomed | ePus Kunjungan Ibu Hamil (5x), ePus Laboratorium (45x), ePus PNC, ePus MTBS (8x), SIPTM, ASIK Skrining PTM (14x) | 6 |
| 595 | 32700-7 | Microscopic observation [Identifier] in Blood by Malaria smear | loinc | ePus Kunjungan Ibu Hamil (6x), ePus MTBS (3x) | 2 |
| 596 | 50687-3 | Plasmodium sp Ag [Presence] in Blood | loinc | ePus Kunjungan Ibu Hamil | 1 |
| 597 | 5045-0 | Ancylostoma sp Ab [Units/volume] in Serum | loinc | ePus Kunjungan Ibu Hamil (3x) | 1 |
| 598 | 830039004 | Genitourinary medicine service | snomed | ePus Kunjungan Ibu Hamil | 1 |
| 599 | 386413005 | Risk identification | snomed | ePus Kunjungan Ibu Hamil | 1 |
| 600 | 1156040003 | Self reported | snomed | ePus Kunjungan Ibu Hamil | 1 |
| 601 | 257514003 | Member of public involved incidentally | snomed | ePus Kunjungan Ibu Hamil, ePus INC | 2 |
| 602 | 106292003 | Professional nurse | snomed | ePus Kunjungan Ibu Hamil, ePus INC, Dapodik PAUD | 3 |
| 603 | O13 | Gestational [pregnancy-induced] hypertension without significant proteinuria | icd-10 | ePus Kunjungan Ibu Hamil, ePus PNC, ELSMIL Pasca Persalinan, SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC, SIM RS Goetoeng INC (4x) | 9 |
| 604 | O06.9 | Unspecified abortion Complete or unspecified, without complication | icd-10 | ePus Kunjungan Ibu Hamil | 1 |
| 605 | O20.9 | Haemorrhage in early pregnancy, unspecified | icd-10 | ePus Kunjungan Ibu Hamil | 1 |
| 606 | O98.9 | Unspecified maternal infectious or parasitic disease complicating pregnancy, childbirth and the puerperium | icd-10 | ePus Kunjungan Ibu Hamil | 1 |
| 607 | O42.9 | Premature rupture of membranes, unspecified | icd-10 | ePus Kunjungan Ibu Hamil | 1 |
| 608 | O99.8 | Other specified diseases and conditions complicating pregnancy, childbirth and the puerperium | icd-10 | ePus Kunjungan Ibu Hamil, SIM RS Goetoeng INC (2x) | 2 |
| 609 | SP000383 | Keadaan Ibu Saat Tiba | kemkes sp | ePus Kunjungan Ibu Hamil, ePus INC, SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 7 |
| 610 | 63238001 | Dead on arrival at hospital | snomed | ePus Kunjungan Ibu Hamil | 1 |
| 611 | 438949009 | Alive | snomed | ePus Kunjungan Ibu Hamil, ePus INC (3x), ePus PNC, ELSMIL Pasca Persalinan | 4 |
| 612 | 119361006 | Plasma | snomed | ePus Laboratorium | 1 |
| 613 | 119364003 | Serum | snomed | ePus Laboratorium (2x) | 1 |
| 614 | 258580003 | Whole blood specimen | snomed | ePus Laboratorium | 1 |
| 615 | ST000001 | Sputum Pagi | snomed | ePus Laboratorium | 1 |
| 616 | ST000002 | Sputum Sewaktu | snomed | ePus Laboratorium | 1 |
| 617 | 119339001 | Stool specimen | snomed | ePus Laboratorium | 1 |
| 618 | emd | From accident/emergency department | http://terminology.hl7.org/CodeSystem/admit-source | ePus Laboratorium, SIM RS Narmada INC | 2 |
| 619 | outp | From outpatient department | http://terminology.hl7.org/CodeSystem/admit-source | ePus Laboratorium, SIM RS Narmada INC | 2 |
| 620 | SRC000011 | Pemeriksaaan TCM XDR | kemkes clinical-term | ePus Laboratorium | 1 |
| 621 | LA11882-0 | Detected | snomed | ePus Laboratorium | 1 |
| 622 | LA11883-8 | Not detected | snomed | ePus Laboratorium | 1 |
| 623 | 94500-6 | SARS-CoV-2 (COVID-19) RNA [Presence] in Respiratory specimen by NAA with probe detection | loinc | ePus Laboratorium (3x) | 1 |
| 624 | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | loinc | ePus Laboratorium (3x), ASIK Skrining PTM (3x), ASIK CKG Dewasa Laki-laki (2x), ASIK CKG Dewasa Perempuan (2x), ASIK CKG Lansia (27 Apr 2026) (2x), SIM RS Panti Nugroho Diabetes Melitus, SIM RS Panti Nugroho Hipertensi, SIM RS MPH Diabetes Melitus (3x), SIM RS Goetoeng Diabetes Melitus | 9 |
| 625 | 2093-3 | Cholesterol [Mass/volume] in Serum or Plasma | loinc | ePus Laboratorium (3x), ASIK Skrining PTM (3x), ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 5 |
| 626 | 3084-1 | Urate [Mass/volume] in Serum or Plasma | loinc | ePus Laboratorium (3x) | 1 |
| 627 | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | loinc | ePus Laboratorium (3x), ASIK CKG Balita (v2) (3x), ASIK CKG Dewasa Laki-laki (3x), ASIK CKG Dewasa Perempuan (3x), ASIK CKG Lansia (27 Apr 2026) (2x), SIM RS Panti Nugroho Diabetes Melitus, SIM RS Panti Nugroho Hipertensi, SIM RS MPH Diabetes Melitus (3x), SIM RS Goetoeng Diabetes Melitus | 9 |
| 628 | 41653-7 | Glucose [Mass/volume] in Capillary blood by Glucometer | loinc | ePus Laboratorium (3x) | 1 |
| 629 | 2571-8 | Triglyceride [Mass/volume] in Serum or Plasma | loinc | ePus Laboratorium (3x), ASIK Skrining PTM (3x), ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 5 |
| 630 | 2085-9 | Cholesterol in HDL [Mass/volume] in Serum or Plasma | loinc | ePus Laboratorium (3x), ASIK Skrining PTM (3x), ASIK CKG Dewasa Laki-laki (2x), ASIK CKG Dewasa Perempuan (2x), ASIK CKG Lansia (27 Apr 2026) (2x) | 5 |
| 631 | 2089-1 | Cholesterol in LDL [Mass/volume] in Serum or Plasma | loinc | ePus Laboratorium (3x), ASIK Skrining PTM (3x) | 2 |
| 632 | 1751-7 | Albumin [Mass/volume] in Serum or Plasma | loinc | ePus Laboratorium (3x) | 1 |
| 633 | 2324-2 | Gamma glutamyl transferase [Enzymatic activity/volume] in Serum or Plasma | loinc | ePus Laboratorium (3x) | 1 |
| 634 | 4548-4 | Hemoglobin A1c/Hemoglobin.total in Blood | loinc | ePus Laboratorium (3x), ASIK Skrining PTM (3x), ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026), SIM RS Panti Nugroho Diabetes Melitus, SIM RS Panti Nugroho Hipertensi, SIM RS MPH Diabetes Melitus (3x), SIM RS Goetoeng Diabetes Melitus | 9 |
| 635 | 1920-8 | Aspartate aminotransferase [Enzymatic activity/volume] in Serum or Plasma | loinc | ePus Laboratorium (3x), ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 4 |
| 636 | 1742-6 | Alanine aminotransferase [Enzymatic activity/volume] in Serum or Plasma | loinc | ePus Laboratorium (3x) | 1 |
| 637 | 2157-6 | Creatine kinase [Enzymatic activity/volume] in Serum or Plasma | loinc | ePus Laboratorium (3x) | 1 |
| 638 | 20977-5 | Urea [Mass/volume] in Blood | loinc | ePus Laboratorium (3x), ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 4 |
| 639 | 2885-2 | Protein [Mass/volume] in Serum or Plasma | loinc | ePus Laboratorium (3x) | 1 |
| 640 | 1521-4 | Glucose [Mass/volume] in Serum or Plasma --2 hours post meal | loinc | ePus Laboratorium (3x), ASIK Skrining PTM (3x), ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 5 |
| 641 | 58410-2 | CBC panel - Blood by Automated count | loinc | ePus Laboratorium (2x), ASIK CKG Balita (v2) (2x) | 2 |
| 642 | 6690-2 | Leukocytes [#/volume] in Blood by Automated count | loinc | ePus Laboratorium (5x) | 1 |
| 643 | 789-8 | Erythrocytes [#/volume] in Blood by Automated count | loinc | ePus Laboratorium, ASIK CKG Balita (v2) | 2 |
| 644 | 4544-3 | Hematocrit [Volume Fraction] of Blood by Automated count | loinc | ePus Laboratorium | 1 |
| 645 | 787-2 | MCV [Entitic mean volume] in Red Blood Cells by Automated count | loinc | ePus Laboratorium | 1 |
| 646 | 785-6 | MCH [Entitic mass] by Automated count | loinc | ePus Laboratorium | 1 |
| 647 | 786-4 | MCHC [Entitic Mass/volume] in Red Blood Cells by Automated count | loinc | ePus Laboratorium | 1 |
| 648 | 26453-1 | Erythrocytes [#/volume] in Blood | loinc | ePus Laboratorium (3x) | 1 |
| 649 | 26464-8 | Leukocytes [#/volume] in Blood | loinc | ePus Laboratorium (6x), ePus MTBS (3x) | 2 |
| 650 | 26515-7 | Platelets [#/volume] in Blood | loinc | ePus Laboratorium (3x), ePus MTBS (3x), ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 5 |
| 651 | 20570-8 | Hematocrit [Volume Fraction] of Blood | loinc | ePus Laboratorium (3x), ePus MTBS (3x) | 2 |
| 652 | 11067-6 | Bleeding time | loinc | ePus Laboratorium (3x) | 1 |
| 653 | 30341-2 | Erythrocyte sedimentation rate [Velocity] in Red Blood Cells | loinc | ePus Laboratorium (3x) | 1 |
| 654 | 17009-2 | IgM [Presence] in Serum | loinc | ePus Laboratorium (3x) | 1 |
| 655 | 3183-1 | Clotting time of Blood by Lee White method | loinc | ePus Laboratorium (3x) | 1 |
| 656 | 17007-6 | IgG [Presence] in Serum | loinc | ePus Laboratorium (3x) | 1 |
| 657 | 30428-7 | MCV [Entitic volume] | loinc | ePus Laboratorium (3x), ASIK CKG Balita (v2) | 2 |
| 658 | 28539-5 | MCH [Entitic mass] | loinc | ePus Laboratorium (3x), ASIK CKG Balita (v2) | 2 |
| 659 | 28540-3 | MCHC [Mass/volume] | loinc | ePus Laboratorium (3x) | 1 |
| 660 | 26511-6 | Neutrophils/100 leukocytes in Blood | loinc | ePus Laboratorium (6x) | 1 |
| 661 | 804-5 | Leukocytes [#/volume] in Blood by Manual count | loinc | ePus Laboratorium (3x) | 1 |
| 662 | 23761-0 | Neutrophils/100 leukocytes in Blood by Manual count | loinc | ePus Laboratorium (3x) | 1 |
| 663 | 770-8 | Neutrophils/100 leukocytes in Blood by Automated count | loinc | ePus Laboratorium (3x) | 1 |
| 664 | 26505-8 | Segmented neutrophils/100 leukocytes in Blood | loinc | ePus Laboratorium (3x) | 1 |
| 665 | 769-0 | Segmented neutrophils/100 leukocytes in Blood by Manual count | loinc | ePus Laboratorium (3x) | 1 |
| 666 | 32200-8 | Segmented neutrophils/100 leukocytes in Blood by Automated count | loinc | ePus Laboratorium (3x) | 1 |
| 667 | 26508-2 | Band form neutrophils/100 leukocytes in Blood | loinc | ePus Laboratorium (3x) | 1 |
| 668 | 764-1 | Band form neutrophils/100 leukocytes in Blood by Manual count | loinc | ePus Laboratorium (3x) | 1 |
| 669 | 35332-6 | Band form neutrophils/100 leukocytes in Blood by Automated count | loinc | ePus Laboratorium (3x) | 1 |
| 670 | 26478-8 | Lymphocytes/100 leukocytes in Blood | loinc | ePus Laboratorium (3x) | 1 |
| 671 | 882-1 | ABO and Rh group [Type] in Blood | loinc | ePus Laboratorium (3x) | 1 |
| 672 | LA21321-7 | O Pos | loinc | ePus Laboratorium | 1 |
| 673 | LA21322-5 | O Neg | loinc | ePus Laboratorium | 1 |
| 674 | LA21327-4 | B Pos | loinc | ePus Laboratorium | 1 |
| 675 | LA21328-2 | B Neg | loinc | ePus Laboratorium | 1 |
| 676 | LA21323-3 | AB Pos | loinc | ePus Laboratorium | 1 |
| 677 | LA21324-1 | AB Neg | loinc | ePus Laboratorium | 1 |
| 678 | LA21325-8 | A Pos | loinc | ePus Laboratorium | 1 |
| 679 | LA21326-6 | A Neg | loinc | ePus Laboratorium | 1 |
| 680 | 17566-1 | Salmonella typhi O Ab [Presence] in Serum | loinc | ePus Laboratorium (3x) | 1 |
| 681 | 22529-2 | Salmonella typhi H Ab [Presence] in Serum | loinc | ePus Laboratorium (3x) | 1 |
| 682 | 743-5 | Monocytes [#/volume] in Blood by Manual count | loinc | ePus Laboratorium (3x) | 1 |
| 683 | 705-4 | Basophils [#/volume] in Blood by Manual count | loinc | ePus Laboratorium (3x) | 1 |
| 684 | 712-0 | Eosinophils [#/volume] in Blood by Manual count | loinc | ePus Laboratorium (3x) | 1 |
| 685 | 26484-6 | Monocytes [#/volume] in Blood | loinc | ePus Laboratorium (3x) | 1 |
| 686 | 26449-9 | Eosinophils [#/volume] in Blood | loinc | ePus Laboratorium (3x) | 1 |
| 687 | 26444-0 | Basophils [#/volume] in Blood | loinc | ePus Laboratorium (3x) | 1 |
| 688 | 87546-8 | Dengue virus IgG and IgM panel - Serum Qualitative | loinc | ePus Laboratorium (2x) | 1 |
| 689 | 29676-4 | Dengue virus IgG Ab [Presence] in Serum | loinc | ePus Laboratorium (4x) | 1 |
| 690 | 25338-5 | Dengue virus IgM Ab [Presence] in Serum | loinc | ePus Laboratorium (4x) | 1 |
| 691 | 91064-6 | Dengue virus NS1 Ag [Presence] in Serum or Plasma by Immunoassay | loinc | ePus Laboratorium (3x) | 1 |
| 692 | 47085-6 | Plasmodium sp DNA [Presence] in Blood by NAA with probe detection | loinc | ePus Laboratorium (3x) | 1 |
| 693 | 34534-8 | 12 lead EKG panel | loinc | ePus Laboratorium (3x), ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 4 |
| 694 | 66862007 | Radiologist | snomed | ePus Laboratorium (2x), ePus ANC (13x), ASIK Skrining PTM (6x) | 3 |
| 695 | 11525-3 | US for pregnancy | loinc | ePus Laboratorium (3x), ePus ANC (11x), SIM RS Narmada KIA, SIM RS Siaga Medika ANC (6x) | 4 |
| 696 | 5778-6 | Color of Urine | loinc | ePus Laboratorium (3x) | 1 |
| 697 | 32167-9 | Clarity of Urine | loinc | ePus Laboratorium (3x) | 1 |
| 698 | 2756-5 | pH of Urine | loinc | ePus Laboratorium (3x) | 1 |
| 699 | 2965-2 | Specific gravity of Urine | loinc | ePus Laboratorium (3x) | 1 |
| 700 | 2349-9 | Glucose [Presence] in Urine | loinc | ePus Laboratorium (3x) | 1 |
| 701 | 33903-6 | Ketones [Presence] in Urine | loinc | ePus Laboratorium (3x) | 1 |
| 702 | 1977-8 | Bilirubin.total [Presence] in Urine | loinc | ePus Laboratorium (3x) | 1 |
| 703 | 34927-4 | Urobilinogen [Moles/volume] in Urine | loinc | ePus Laboratorium (3x) | 1 |
| 704 | 105906-2 | Blood [Presence] in Urine | loinc | ePus Laboratorium (3x) | 1 |
| 705 | 32710-6 | Nitrite [Presence] in Urine | loinc | ePus Laboratorium (3x) | 1 |
| 706 | 105087-1 | Epithelial cells.squamous [Presence] in Urine | loinc | ePus Laboratorium (3x) | 1 |
| 707 | 105089-7 | Epithelial cells.non-squamous [Presence] in Urine | loinc | ePus Laboratorium (3x) | 1 |
| 708 | 85093-3 | Crystal casts [Presence] in Urine sediment by Light microscopy | loinc | ePus Laboratorium (3x) | 1 |
| 709 | 105107-7 | Erythrocytes [#/area] in Urine sediment | loinc | ePus Laboratorium (3x) | 1 |
| 710 | 105104-4 | Leukocytes [#/area] in Urine sediment | loinc | ePus Laboratorium (3x) | 1 |
| 711 | 105908-8 | Bacteria [#/area] in Urine sediment | loinc | ePus Laboratorium (3x) | 1 |
| 712 | 2106-3 | Choriogonadotropin [Presence] in Urine | loinc | ePus Laboratorium (3x) | 1 |
| 713 | 11258-1 | Hepatitis B virus DNA [Units/volume] in Serum | loinc | ePus Laboratorium (3x) | 1 |
| 714 | K2 | Tidak ada | episodeofcare/ANC | ePus ANC, eKohort ANC | 2 |
| 715 | K3 | Tidak ada | episodeofcare/ANC | ePus ANC, eKohort ANC | 2 |
| 716 | K4 | Tidak ada | episodeofcare/ANC | ePus ANC, eKohort ANC | 2 |
| 717 | K5 | Tidak ada | episodeofcare/ANC | ePus ANC, eKohort ANC | 2 |
| 718 | K6 | Tidak ada | episodeofcare/ANC | ePus ANC, eKohort ANC | 2 |
| 719 | 305956004 | Referral by physician | snomed | ePus ANC, ePus INC, ePus PNC | 3 |
| 720 | 306052007 | Referral by midwife | snomed | ePus ANC, ePus INC, ePus PNC | 3 |
| 721 | SP000116 | Rujukan dari Puskesmas Pembantu | kemkes sp | ePus ANC, ePus INC, ePus PNC, SIM RS Panti Nugroho PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 6 |
| 722 | SP000117 | Rujukan dari Puskesmas | kemkes sp | ePus ANC, ePus INC, ePus PNC, SIM RS Panti Nugroho PNC, SIM RS Panti Nugroho Hipertensi, SIM RS Panti Nugroho Stroke, SIM RS MPH Diabetes Melitus, SIM RS MPH Hipertensi, SIM RS Siaga Medika INC, SIM RS Siaga Medika PNC, SIM RS PKU PNC, SIM RS Goetoeng ANC, SIM RS Goetoeng INC (8x), SIM RS Goetoeng PNC, SIM RS Goetoeng BBL (9x) | 15 |
| 723 | SP000118 | Rujukan dari Rumah Bersalin / Klinik | kemkes sp | ePus ANC, ePus INC, ePus PNC, SIM RS Panti Nugroho PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 6 |
| 724 | SP000119 | Rujukan dari Rumah Sakit | kemkes sp | ePus ANC, ePus INC, ePus PNC, SIM RS Panti Nugroho PNC, SIM RS MPH Diabetes Melitus, SIM RS MPH Hipertensi, SIM RS Siaga Medika PNC, SIM RS PKU PNC, SIM RS Goetoeng BBL | 9 |
| 725 | 11977-6 | [#] Parity | loinc | ePus ANC (2x), ePus PNC (2x), SIHEPI Rekap 3e, SIM RS Tripat PNC, SIM RS Narmada INC (2x), SIM RS Narmada KIA, SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika INC, SIM RS Siaga Medika PNC, SIM RS PKU INC, SIM RS PKU PNC | 13 |
| 726 | 69043-8 | Other pregnancy outcomes # | loinc | ePus ANC, ePus PNC, SIHEPI Rekap 3e, SIM RS Tripat PNC, SIM RS Narmada INC (2x), SIM RS Narmada KIA, SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika INC, SIM RS Siaga Medika PNC, SIM RS PKU INC, SIM RS PKU PNC | 13 |
| 727 | ANC.B6.DE32 | Parity | WHO anc-custom-codes | ePus ANC, ePus PNC, SIHEPI Rekap 3e, SIM RS Tripat PNC, SIM RS Narmada INC (2x), SIM RS Narmada KIA, SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU INC, SIM RS PKU PNC | 12 |
| 728 | SP000050 | Riwayat Onset Persalinan | loinc | ePus ANC, ePus PNC | 2 |
| 729 | SP000132 | Memiliki Buku KIA | kemkes sp | ePus ANC, ePus PNC, SIM RS Panti Nugroho ANC, SIM RS Ummu Hani ANC, SIM RS MPH ANC, SIM RS Siaga Medika ANC | 6 |
| 730 | 56077-1 | Body weight --pre current pregnancy | loinc | ePus ANC, ePus PNC, ELSMIL Ibu Hamil | 3 |
| 731 | ANC.B8.DE2 | Pre-gestational weight | WHO anc-custom-codes | ePus ANC, ePus PNC, ELSMIL Ibu Hamil | 3 |
| 732 | 404684003 | Clinical finding | snomed | ePus ANC, ePus Tumbang Anak (2x) | 2 |
| 733 | 3401000175105 | Total number of prenatal care visits | snomed | ePus ANC, eKohort ANC | 2 |
| 734 | SP000134 | Jenis Lokasi Screening | kemkes sp | ePus ANC, ePus PNC | 2 |
| 735 | 82242000 | Children’s hospital | snomed | ePus ANC, ePus INC, ePus PNC, SIHEPI Rekap 3e, SiGizi Kohort Ibu | 5 |
| 736 | 104 | Rumah Sakit | hhttp://terminology.kemkes.go.id/CodeSystem/organization-type | ePus ANC, ePus INC, ePus PNC, ELSMIL Pasca Persalinan | 4 |
| 737 | OT000003 | RS ODHA | hhttp://terminology.kemkes.go.id/CodeSystem/organization-type | ePus ANC, ePus INC, ePus PNC, SIM RS Panti Nugroho INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 6 |
| 738 | OT000004 | Bidan Praktek Mandiri | hhttp://terminology.kemkes.go.id/CodeSystem/organization-type | ePus ANC, ePus INC, ePus PNC, SIM RS Panti Nugroho INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 6 |
| 739 | SP000131 | Status Pindahan | kemkes sp | ePus ANC, ePus INC, ePus PNC | 3 |
| 740 | 10197-2 | Physical findings of Eye Narrative | loinc | ePus ANC (2x), SIM RS MPH BBL, SIM RS Siaga Medika BBL | 3 |
| 741 | ANC.SS.DE26 | Pemeriksaan Fisik Konjungtiva | kemkes anc-custom-codes | ePus ANC | 1 |
| 742 | A | Abnormal | v3-ObservationInterpretation | ePus ANC (13x), ASIK CKG Dewasa Laki-laki (3x), ASIK CKG Dewasa Perempuan (3x), ASIK CKG Lansia (27 Apr 2026) (5x), SIM RS MPH BBL (8x), SIM RS Siaga Medika BBL (8x) | 6 |
| 743 | ANC.SS.DE27 | Pemeriksaan Fisik Sklera | kemkes anc-custom-codes | ePus ANC | 1 |
| 744 | 10206-1 | Physical findings of Skin Narrative | loinc | ePus ANC, SIM RS MPH BBL, SIM RS Siaga Medika BBL | 3 |
| 745 | 11411-6 | Physical findings of Neck Narrative | loinc | ePus ANC | 1 |
| 746 | ANC.SS.DE28 | Pemeriksaan Fisik Leher | kemkes anc-custom-codes | ePus ANC | 1 |
| 747 | N | Normal | kemkes anc-custom-codes | ePus ANC | 1 |
| 748 | 32453-3 | Physical findings of Mouth | loinc | ePus ANC, SIM RS MPH BBL, SIM RS Siaga Medika BBL | 3 |
| 749 | ANC.SS.DE29 | Pemeriksaan Fisik Area Mulut | v3-ObservationInterpretation | ePus ANC | 1 |
| 750 | 297268004 | Ear, nose and throat finding | snomed | ePus ANC | 1 |
| 751 | ANC.SS.DE30 | Pemeriksaan Fisik Telinga Hidung dan Tenggorokan (THT) | kemkes anc-custom-codes | ePus ANC | 1 |
| 752 | 10200-4 | Physical findings of Heart Narrative | loinc | ePus ANC | 1 |
| 753 | ANC.SS.DE31 | Pemeriksaan Fisik Dada (Auskultasi Jantung) | kemkes anc-custom-codes | ePus ANC | 1 |
| 754 | 301230006 | Lung finding | snomed | ePus ANC | 1 |
| 755 | ANC.SS.DE32 | Pemeriksaan Fisik Dada (Auskultasi Paru) | kemkes anc-custom-codes | ePus ANC | 1 |
| 756 | 10191-5 | Physical findings of Abdomen Narrative | loinc | ePus ANC, SIM RS MPH BBL, SIM RS Siaga Medika BBL | 3 |
| 757 | ANC.SS.DE33 | Pemeriksaan Fisik Perut | kemkes anc-custom-codes | ePus ANC | 1 |
| 758 | 116307009 | Finding of upper limb | snomed | ePus ANC | 1 |
| 759 | ANC.SS.DE34 | Pemeriksaan Fisik Tungkai | kemkes anc-custom-codes | ePus ANC (4x) | 1 |
| 760 | 116312005 | Finding of lower limb | snomed | ePus ANC | 1 |
| 761 | 102572006 | Edema of lower extremity (finding) | snomed | ePus ANC | 1 |
| 762 | 299412000 | Finding of patella structure | snomed | ePus ANC | 1 |
| 763 | ANC.B8.DE17 | Systolic blood pressure | WHO anc-custom-codes | ePus ANC, eKohort ANC, SIM RS Narmada INC, SIM RS Narmada KIA, SIM RS Panti Nugroho ANC, SIM RS Siaga Medika ANC | 6 |
| 764 | ANC.B8.DE19 | Diastolic blood pressure | WHO anc-custom-codes | ePus ANC, eKohort ANC, SIM RS Narmada INC, SIM RS Narmada KIA, SIM RS Panti Nugroho ANC, SIM RS Siaga Medika ANC | 6 |
| 765 | ANC.SS.DE2 | Pernapasan | kemkes anc-custom-codes | ePus ANC, eKohort ANC, SIM RS Narmada INC, SIM RS Narmada KIA | 4 |
| 766 | 8478-0 | Mean blood pressure | loinc | ePus ANC | 1 |
| 767 | SP000634 | Tinggi fundus terdeteksi | kemkes sp | ePus ANC | 1 |
| 768 | SP000635 | Tinggi fundus jari | kemkes sp | ePus ANC | 1 |
| 769 | 11850-5 | Gestational sac Mean diameter US | loinc | ePus ANC (2x), SIM RS Siaga Medika ANC (3x) | 2 |
| 770 | ANC.SS.DE36 | Gestational sac (GS) USG | kemkes anc-custom-codes | ePus ANC, SIM RS Siaga Medika ANC | 2 |
| 771 | 11957-8 | Fetal Crown Rump length US | loinc | ePus ANC (2x), SIM RS Siaga Medika ANC (2x) | 2 |
| 772 | ANC.SS.DE37 | Fetal Crown Rump Length (CRL) USG | kemkes anc-custom-codes | ePus ANC, SIM RS Siaga Medika ANC | 2 |
| 773 | 11948-7 | Fetal Heart rate US | loinc | ePus ANC (2x), SIM RS Siaga Medika ANC (2x) | 2 |
| 774 | ANC.SS.DE38 | Denyut Jantung Janin (DJJ) USG | kemkes anc-custom-codes | ePus ANC | 1 |
| 775 | 11820-8 | Fetal Head Diameter.biparietal US | loinc | ePus ANC (2x), SIM RS Siaga Medika ANC (2x) | 2 |
| 776 | 11984-2 | Fetal Head Circumference US | loinc | ePus ANC (2x), SIM RS Siaga Medika ANC (2x) | 2 |
| 777 | 11979-2 | Fetal Abdomen Circumference US | loinc | ePus ANC (2x) | 1 |
| 778 | 11963-6 | Fetal Femur diaphysis [Length] US | loinc | ePus ANC (2x) | 1 |
| 779 | 11832-3 | Fetal Amniotic fluid space Maximum diameter largest pocket US | loinc | ePus ANC (2x), SIM RS Siaga Medika ANC (2x) | 2 |
| 780 | 365662002 | Finding of amniotic fluid appearance | snomed | ePus ANC, ePus INC | 2 |
| 781 | 168090003 | Amniotic fluid clear | snomed | ePus ANC, ePus INC | 2 |
| 782 | 408781009 | Straw colored amniotic fluid | snomed | ePus ANC, ePus INC | 2 |
| 783 | 249134008 | Bloodstained liquor | snomed | ePus ANC, ePus INC | 2 |
| 784 | 168092006 | Amniotic fluid -meconium stain | snomed | ePus ANC, ePus INC | 2 |
| 785 | 11525-3 | US for pregnancy | snomed | ePus ANC (2x), SIM RS Siaga Medika ANC (2x) | 2 |
| 786 | 271692001 | Presentation of fetus | snomed | ePus ANC, ePus INC, eKohort INC | 3 |
| 787 | ANC.SS.DE41 | Letak Janin USG | WHO anc-custom-codes | ePus ANC, SIM RS Siaga Medika ANC | 2 |
| 788 | 398236008 | Intrauterine | snomed | ePus ANC, ePus INC | 2 |
| 789 | 298109001 | Ectopic | snomed | ePus ANC, ePus INC | 2 |
| 790 | 72155-5 | Position in womb Fetus [RHEA] | snomed | ePus ANC, SIM RS Siaga Medika ANC | 2 |
| 791 | 11877-8 | Fetal presentation US | loinc | ePus ANC (2x), SIM RS Siaga Medika ANC (2x) | 2 |
| 792 | 11878-6 | Number of fetuses by US | loinc | ePus ANC (2x), SIM RS Siaga Medika ANC (2x) | 2 |
| 793 | 249111004 | Engagement of head | snomed | ePus ANC, ePus INC | 2 |
| 794 | ANC.SS.DE1 | Taksiran Berat Janin (TBJ) | kemkes anc-custom-codes | ePus ANC, ELSMIL Ibu Hamil, eKohort ANC, SIM RS Narmada INC, SIM RS Narmada KIA | 5 |
| 795 | 11888-5 | Gestational age US composite estimate | loinc | ePus ANC (2x) | 1 |
| 796 | ANC.B6.DE20 | Ultrasound | WHO anc-custom-codes | ePus ANC | 1 |
| 797 | 11781-2 | Delivery date US composite estimate | loinc | ePus ANC (2x) | 1 |
| 798 | ANC.SS.DE40 | Hari Perkiraan Lahir (HPL) USG | kemkes anc-custom-codes | ePus ANC | 1 |
| 799 | 34842007 | Antepartum hemorrhage | snomed | ePus ANC | 1 |
| 800 | 386639001 | Termination of pregnancy | snomed | ePus ANC, ePus INC, SiGizi Ibu Nifas | 3 |
| 801 | 91302008 | Sepsis | snomed | ePus ANC | 1 |
| 802 | 92000653 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula | http://sys-ids.kemkes.go.id/kf | ePus ANC, ePus PNC | 2 |
| 803 | OC000001 | Jarak kehamilan | kemkes clinical-term | ePus ANC, ePus INC, SiGizi Kohort Ibu, SIM RS PKU INC | 4 |
| 804 | ANC.SS.DE53 | Jarak kehamilan | kemkes anc-custom-codes | ePus ANC, ePus INC, SiGizi Kohort Ibu, SIM RS PKU INC | 4 |
| 805 | 66071002 | Viral hepatitis type B | snomed | ePus ANC | 1 |
| 806 | 76272004 | Syphilis | snomed | ePus ANC | 1 |
| 807 | 61462000 | Malaria | snomed | ePus ANC, ePus MTBS | 2 |
| 808 | 386337006 | Intrapartal care | snomed | ePus INC, SiGizi Ibu Nifas, SiGizi Kohort Ibu | 3 |
| 809 | 288203005 | Transverse/oblique lie | snomed | ePus INC (2x), eKohort INC | 2 |
| 810 | 70028003 | Vertex presentation | snomed | ePus INC, eKohort INC | 2 |
| 811 | 249083005 | Posterior fontanelle presenting | snomed | ePus INC | 1 |
| 812 | 23954006 | Acromion presentation | snomed | ePus INC | 1 |
| 813 | 8014007 | Brow presentation of fetus | snomed | ePus INC | 1 |
| 814 | 8017000 | Face presentation | snomed | ePus INC | 1 |
| 815 | 249097002 | Footling breech presentation | snomed | ePus INC | 1 |
| 816 | 124736009 | Compound presentation | snomed | ePus INC | 1 |
| 817 | 289282009 | Amniotic membrane finding | snomed | ePus INC, eKohort INC | 2 |
| 818 | 249125003 | Intact membranes | snomed | ePus INC, eKohort INC | 2 |
| 819 | SP000120 | Non-intact membrane | snomed | ePus INC, SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 6 |
| 820 | SP000123 | Integrasi Program | kemkes sp | ePus INC, SITB TB 01, SIM RS PKU INC | 3 |
| 821 | SP000124 | Obat anti malaria | kemkes sp | ePus INC, ePus PNC, SIM RS Panti Nugroho PNC, SIM RS PKU INC, SIM RS PKU PNC | 5 |
| 822 | SP000125 | Obar anti hepatitis B | kemkes sp | ePus INC, ePus PNC, SIM RS Panti Nugroho PNC, SIM RS PKU INC, SIM RS PKU PNC | 5 |
| 823 | 76516-4 | Gestational age—​at birth | loinc | ePus INC, ELSMIL Baduta, eKohort INC, SIM RS Tripat BBL (sheet 'INC BBL'), SIM RS Panti Nugroho INC, SIM RS Panti Nugroho BBL, SIM RS Ummu Hani INC, SIM RS Ummu Hani BBL, SIM RS MPH INC, SIM RS MPH BBL, SIM RS Siaga Medika BBL, SIM RS PKU INC | 12 |
| 824 | 118215003 | Delivery finding | snomed | ePus INC | 1 |
| 825 | 125677006 | Relative | snomed | ePus INC | 1 |
| 826 | 200138003 | Vacuum extractor delivery - delivered | snomed | ePus INC, SiGizi Kohort Ibu | 2 |
| 827 | 200130005 | Forceps delivery - delivered | snomed | ePus INC, SiGizi Kohort Ibu | 2 |
| 828 | 405195003 | Intrapartum maternal status | snomed | ePus INC | 1 |
| 829 | 131148009 | Bleeding | snomed | ePus INC | 1 |
| 830 | 386661006 | Fever | snomed | ePus INC, ePus MTBS | 2 |
| 831 | 91175000 | Seizure | snomed | ePus INC, ePus MTBS, ePus MTBM | 3 |
| 832 | 249215002 | Odor of lochia | snomed | ePus INC, ePus PNC | 2 |
| 833 | 59283008 | Maternal death | snomed | ePus INC, eKohort INC | 2 |
| 834 | 387700009 | Prolonged latent phase of labor | snomed | ePus INC | 1 |
| 835 | 398143009 | Uterine contraction monitoring | snomed | ePus INC (2x) | 1 |
| 836 | 289708007 | Regular uterine contractions | snomed | ePus INC (2x) | 1 |
| 837 | 289739009 | Uterine contractions problem | snomed | ePus INC (2x) | 1 |
| 838 | 364270005 | Frequency of uterine contraction | snomed | ePus INC (2x) | 1 |
| 839 | 364274001 | Duration of uterine contraction | snomed | ePus INC (2x) | 1 |
| 840 | SP000399 | <20 detik | kemkes sp | ePus INC (2x) | 1 |
| 841 | SP000400 | 20-40 detik | kemkes sp | ePus INC (2x) | 1 |
| 842 | SP000401 | >40 detik | kemkes sp | ePus INC (2x) | 1 |
| 843 | 249120008 | Onset of labor first stage | snomed | ePus INC, eKohort INC | 2 |
| 844 | 249160009 | Onset of labor second stage | snomed | ePus INC, eKohort INC (2x) | 2 |
| 845 | OC000018 | Onset Kala III | kemkes clinical-term | ePus INC, SIM RS PKU INC | 2 |
| 846 | 236994008 | Placental delivery procedure | kemkes clinical-term | ePus INC | 1 |
| 847 | 289267004 | Finding of completeness of placenta | snomed | ePus INC | 1 |
| 848 | 249170006 | Complete placenta at delivery | snomed | ePus INC | 1 |
| 849 | 268479002 | Incomplete placenta at delivery | snomed | ePus INC | 1 |
| 850 | SP000127 | Injeksi Oksitosin | kemkes sp | ePus INC, SIM RS PKU INC | 2 |
| 851 | 302384005 | Controlled cord traction of placenta | snomed | ePus INC, eKohort INC | 2 |
| 852 | 236996005 | Abdominal uterine fundal massage | snomed | ePus INC, eKohort INC | 2 |
| 853 | OC000019 | Onset Kala IV | kemkes clinical-term | ePus INC, SIM RS PKU INC | 2 |
| 854 | 9293002 | Atony of uterus | snomed | ePus INC (2x) | 1 |
| 855 | 1148943004 | Retention of placenta and uterine membrane | snomed | ePus INC | 1 |
| 856 | 283380005 | Laceration of perineum | snomed | ePus INC | 1 |
| 857 | 84007008 | Shock during AND/OR following labor AND/OR delivery | snomed | ePus INC | 1 |
| 858 | 118216002 | Labor finding | snomed | ePus INC | 1 |
| 859 | 719051004 | Quantity of postpartum maternal blood loss | snomed | ePus INC | 1 |
| 860 | 717809003 | Immediate postpartum care | snomed | ePus INC (2x) | 1 |
| 861 | 8462-4 | Diastolic blood pressure | snomed | ePus INC, ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026), SIM RS Panti Nugroho Hipertensi, SIM RS MPH Diabetes Melitus, SIM RS MPH Hipertensi, SIM RS PKU INC, SIM RS Goetoeng Hipertensi | 9 |
| 862 | 199746004 | Obstructed labor | snomed | ePus INC | 1 |
| 863 | 38010008 | Intrapartum hemorrhage | snomed | ePus INC (2x) | 1 |
| 864 | 44223004 | Premature rupture of membranes | snomed | ePus INC | 1 |
| 865 | 199745000 | Complication occurring during labor and delivery | snomed | ePus INC (2x) | 1 |
| 866 | SP000379 | Tatalaksana Komplikasi Persalinan | kemkes sp | ePus INC, SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 6 |
| 867 | 63893-2 | Outcome of pregnancy | loinc | ePus INC, SiGizi Kohort Ibu, SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika INC, SIM RS PKU INC (2x) | 7 |
| 868 | LA14270-5 | Live birth | loinc | ePus INC (2x), SiGizi Kohort Ibu, SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika INC, SIM RS PKU INC (2x) | 7 |
| 869 | LA14271-3 | Stillborn | loinc | ePus INC (2x), SiGizi Kohort Ibu, SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika INC, SIM RS PKU INC (2x) | 7 |
| 870 | LA14272-1 | Miscarriage | loinc | ePus INC, SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika INC, SIM RS PKU INC (2x) | 6 |
| 871 | LA14273-9 | Induced abortion | loinc | ePus INC, SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika INC, SIM RS PKU INC (2x) | 6 |
| 872 | 409014006 | Delivery care management | snomed | ePus INC, ePus PNC | 2 |
| 873 | SP000130 | Menggunakan Partograf | kemkes sp | ePus INC, SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 6 |
| 874 | 431868002 | Initiation of breastfeeding | snomed | ePus INC, eKohort INC | 2 |
| 875 | OC000016 | Waktu Inisiasi Menyusui Dini | kemkes clinical-term | ePus INC, eKohort INC, SIM RS Panti Nugroho BBL, SIM RS Ummu Hani BBL, SIM RS MPH BBL, SIM RS PKU INC | 6 |
| 876 | OV000014 | Kurang dari 1 Jam | kemkes clinical-term | ePus INC, eKohort INC, SIM RS Panti Nugroho BBL, SIM RS Ummu Hani BBL, SIM RS MPH BBL, SIM RS PKU INC | 6 |
| 877 | OV000015 | Lebih dari 1 Jam | kemkes clinical-term | ePus INC, eKohort INC, SIM RS Panti Nugroho BBL, SIM RS Ummu Hani BBL, SIM RS MPH BBL, SIM RS PKU INC | 6 |
| 878 | 409063005 | Counselling | snomed | ePus INC (2x) | 1 |
| 879 | ED000008 | Edukasi Tanda Bahaya Kehamilan, Bersalin dan Nifas | kemkes clinical-term | ePus INC, ePus PNC, SIM RS Panti Nugroho INC, SIM RS Panti Nugroho PNC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika INC, SIM RS Siaga Medika PNC, SIM RS PKU INC, SIM RS PKU PNC | 10 |
| 880 | SP000121 | Edukasi Tanda Bahaya Baru Lahir | kemkes sp | ePus INC, SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 6 |
| 881 | ED000009 | Edukasi IMD dan ASI Eksklusif | kemkes clinical-term | ePus INC, SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 6 |
| 882 | ED000005 | Edukasi Gizi | kemkes clinical-term | ePus INC, SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 6 |
| 883 | PC000001 | Perawatan Tali Pusat | kemkes clinical-term | ePus INC, ePus PNC, SIM RS Panti Nugroho INC, SIM RS Panti Nugroho PNC, SIM RS Panti Nugroho BBL, SIM RS Ummu Hani INC, SIM RS Ummu Hani BBL, SIM RS MPH INC, SIM RS Siaga Medika INC, SIM RS Siaga Medika PNC, SIM RS PKU INC, SIM RS PKU PNC | 12 |
| 884 | ED000010 | Edukasi PHBS | kemkes clinical-term | ePus INC, ePus PNC, SIM RS Panti Nugroho INC, SIM RS Panti Nugroho PNC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika INC, SIM RS Siaga Medika PNC, SIM RS PKU INC, SIM RS PKU PNC | 10 |
| 885 | SP000126 | ARV Profilaksis | kemkes sp | ePus INC, SIHEPI Rekap 3e, SIM RS Panti Nugroho BBL, SIM RS Ummu Hani BBL | 4 |
| 886 | 249222005 | Neonatal condition | snomed | ePus INC, ELSMIL Pasca Persalinan | 2 |
| 887 | Z39.2 | Routine postpartum follow-up | icd-10 | ePus PNC, SIM RS Tripat PNC, SIM RS Narmada KIA, SIM RS Panti Nugroho PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 6 |
| 888 | 289530006 | Vaginal bleeding | snomed | ePus PNC | 1 |
| 889 | 81661-1 | Blood Loss [Volume] Measured | loinc | ePus PNC, eKohort INC, SIM RS Panti Nugroho PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 5 |
| 890 | 364297003 | Female perineum observable | loinc | ePus PNC | 1 |
| 891 | OC000020 | Tanda Infeksi Perineum | kemkes clinical-term | ePus PNC, SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 6 |
| 892 | OC000025 | Tanda Infeksi Luka Jahitan Sectio Caesaria | kemkes clinical-term | ePus PNC, SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 6 |
| 893 | 32422-8 | Physical findings of breast | loinc | ePus PNC, SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 6 |
| 894 | 300885006 | Swelling of breast | snomed | ePus PNC | 1 |
| 895 | 290070001 | Red breast | snomed | ePus PNC | 1 |
| 896 | 54302000 | Discharge from nipple | snomed | ePus PNC | 1 |
| 897 | 53430007 | Pain of breast | snomed | ePus PNC | 1 |
| 898 | 290084006 | Breast normal | snomed | ePus PNC, SIPTM, ASIK Skrining PTM (3x) | 3 |
| 899 | 289700000 | Uterine contractions present | snomed | ePus PNC | 1 |
| 900 | 249214003 | Color of lochia | snomed | ePus PNC | 1 |
| 901 | 278072004 | Lochia rubra | snomed | ePus PNC | 1 |
| 902 | 449828001 | Lochia serosa | snomed | ePus PNC | 1 |
| 903 | 449827006 | Lochia alba | snomed | ePus PNC | 1 |
| 904 | OC000017 | Produksi ASI | kemkes clinical-term | ePus PNC, SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 6 |
| 905 | OV000016 | Produksi ASI ada | kemkes clinical-term | ePus PNC, SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 6 |
| 906 | OV000017 | Produksi ASI ada tapi sedikit | kemkes clinical-term | ePus PNC, SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 6 |
| 907 | OV000018 | Produksi ASI tidak ada | kemkes clinical-term | ePus PNC, SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 6 |
| 908 | 252041008 | Micturition finding | snomed | ePus PNC | 1 |
| 909 | 38671000119103 | Abnormal urination | snomed | ePus PNC | 1 |
| 910 | 102834005 | Normal micturition | snomed | ePus PNC | 1 |
| 911 | 300375001 | Able to defecate | snomed | ePus PNC | 1 |
| 912 | 408988007 | Newborn care education | snomed | ePus PNC | 1 |
| 913 | 8345-1 | Body weight Measured --post partum | loinc | ePus PNC, SIM RS Tripat PNC, SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 7 |
| 914 | 8305-5 | Body height --post partum | loinc | ePus PNC, SIM RS Tripat PNC, SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 7 |
| 915 | 47821001 | Postpartum hemorrhage | snomed | ePus PNC, ELSMIL Pasca Persalinan | 2 |
| 916 | O86.8 | Other specified puerperal infections | icd-10 | ePus PNC | 1 |
| 917 | 58703003 | Postpartum depression | snomed | ePus PNC | 1 |
| 918 | O90.8 | Other complications of the puerperium, not elsewhere classified | icd-10 | ePus PNC, ELSMIL Pasca Persalinan, SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 7 |
| 919 | 289084000 | Difficulty performing breastfeeding | snomed | ePus PNC | 1 |
| 920 | 93015491 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | http://sys-ids.kemkes.go.id/kf | ePus PNC (2x) | 1 |
| 921 | 767224000 | Administration of vitamin A | snomed | ePus PNC, ePus MTBS, SiGizi Balita BNBA, SiGizi Balita Vitamin A | 4 |
| 922 | 92000809 | Retinol Palmitate 200.000 IU Kapsul Lunak | http://sys-ids.kemkes.go.id/kf | ePus PNC, ePus MTBS, SiGizi Balita Vitamin A | 3 |
| 923 | 93018284 | Retinol Palmitate 200.000 IU Kapsul Lunak (Umum) | http://sys-ids.kemkes.go.id/kf | ePus PNC, ePus MTBS (2x), SiGizi Balita Vitamin A | 3 |
| 924 | 711029005 | Counseling about breastfeeding | snomed | ePus PNC | 1 |
| 925 | 72531000052105 | Counseling for contraception | snomed | ePus PNC | 1 |
| 926 | SP000135 | Konseling Tanda Bahaya Bayi Baru Lahir | kemkes sp | ePus PNC, SIM RS Panti Nugroho PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 4 |
| 927 | 441041000124100 | Counseling about nutrition | snomed | ePus PNC | 1 |
| 928 | 32515-9 | CD3+CD4+ (T4 helper) cells [#/volume] in Specimen | loinc | ePus PNC (3x) | 1 |
| 929 | 432555000 | Product containing artesunate | snomed | ePus PNC | 1 |
| 930 | 64115004 | Product containing amodiaquine | snomed | ePus PNC | 1 |
| 931 | 324919005 | Product containing precisely quinine sulfate 200 milligram/1 each conventional release oral tablet | snomed | ePus PNC | 1 |
| 932 | 29175007 | Product containing rifampicin | snomed | ePus PNC | 1 |
| 933 | 81335000 | Product containing isoniazid | snomed | ePus PNC | 1 |
| 934 | 13592004 | Product containing pyrazinamide | snomed | ePus PNC | 1 |
| 935 | 24450004 | Product containing ethambutol | snomed | ePus PNC | 1 |
| 936 | 159016003 | Medical radiographer | snomed | ePus PNC | 1 |
| 937 | SP000139 | KB Pasca Plasenta | kemkes sp | ePus PNC (2x), SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC | 4 |
| 938 | LA6524-8 | Oral contraceptive pill | loinc | ePus PNC (2x), ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan, ELSMIL Baduta, SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC (2x), SIM RS MPH PNC (2x), SIM RS Siaga Medika PNC (2x), SIM RS PKU PNC | 9 |
| 939 | 237122005 | Lactational amenorrhea | snomed | ePus PNC (2x), ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan, ELSMIL Baduta | 4 |
| 940 | LA6525-5 | Injectable/implantable hormone | loinc | ePus PNC (2x), ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan, ELSMIL Baduta, SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC (2x), SIM RS MPH PNC (2x), SIM RS Siaga Medika PNC (2x), SIM RS PKU PNC | 9 |
| 941 | LA6527-1 | Intrauterine device | loinc | ePus PNC (2x), ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan, ELSMIL Baduta, SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC (2x), SIM RS MPH PNC (2x), SIM RS Siaga Medika PNC (2x), SIM RS PKU PNC | 9 |
| 942 | SP000097 | Implan | kemkes sp | ePus PNC (2x), ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan, ELSMIL Baduta, SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC (2x), SIM RS MPH PNC (2x), SIM RS Siaga Medika PNC (2x), SIM RS PKU PNC | 9 |
| 943 | LA6523-0 | Condom | loinc | ePus PNC (2x), ELSMIL Pasca Persalinan, ELSMIL Baduta, SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC (2x), SIM RS MPH PNC (2x), SIM RS Siaga Medika PNC (2x), SIM RS PKU PNC | 8 |
| 944 | 22523008 | Vasectomy | snomed | ePus PNC (2x), ELSMIL Pasca Persalinan, ELSMIL Baduta | 3 |
| 945 | 77543007 | Ligation of fallopian tube | snomed | ePus PNC (2x), ELSMIL Pasca Persalinan, ELSMIL Baduta | 3 |
| 946 | PC000004 | KB Pasca Persalinan | kemkes clinical-term | ePus PNC (2x), ELSMIL Pasca Persalinan, SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 7 |
| 947 | SP000380 | Tatalaksana Komplikasi Pendarahan | kemkes sp | ePus PNC, SIM RS Panti Nugroho PNC, SIM RS PKU PNC | 3 |
| 948 | 736286003 | Hypertension clinical management plan | snomed | ePus PNC, SIM RS Panti Nugroho PNC, SIM RS PKU PNC | 3 |
| 949 | SP000133 | Pemantauan Protein Urin | kemkes sp | ePus PNC (2x), SIM RS Panti Nugroho PNC (2x), SIM RS Siaga Medika PNC, SIM RS PKU PNC (2x) | 4 |
| 950 | SP000138 | Tatalaksana Komplikasi Pre Eklampsia | kemkes sp | ePus PNC, SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 6 |
| 951 | 135840009 | Blood pressure monitoring | kemkes sp | ePus PNC | 1 |
| 952 | SP000136 | Pemberian MgSO4 | kemkes sp | ePus PNC, SIM RS Panti Nugroho PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 4 |
| 953 | SP000137 | Pemberian Diazepam Injeksi | kemkes sp | ePus PNC, SIM RS Panti Nugroho PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 4 |
| 954 | 359746009 | Patient’s condition stable | snomed | ePus PNC, ePus MTBS | 2 |
| 955 | 162668006 | Patient’s condition unstable | snomed | ePus PNC | 1 |
| 956 | 268910001 | Patient’s condition improved | snomed | ePus PNC | 1 |
| 957 | 35025007 | Manual pelvic examination | snomed | ePus PNC | 1 |
| 958 | SP000666 | Hari setelah melahirkan | kemkes sp | ePus PNC | 1 |
| 959 | SP000667 | Penanganan Risiko Tinggi dan Komplikasi | kemkes sp | ePus PNC | 1 |
| 960 | SP000273 | Integrated management of childhood illness | kemkes sp | ePus MTBS | 1 |
| 961 | 9843-4 | Head Occipital-frontal circumference | loinc | ePus MTBS, ePus MTBM, ePus Tumbang Anak, ePus Tumbang DDTK, Dapodik PAUD | 5 |
| 962 | SP000261 | Tipe Kunjungan | kemkes sp | ePus MTBS, ePus MTBM | 2 |
| 963 | SP000262 | Kunjungan Pertama | kemkes sp | ePus MTBS, ePus MTBM | 2 |
| 964 | SP000263 | Kunjungan Ulang | kemkes sp | ePus MTBS, ePus MTBM | 2 |
| 965 | OC000099 | Status daerah endemis malaria tempat tinggal | kemkes clinical-term | ePus MTBS (2x) | 1 |
| 966 | OV000221 | Daerah non endemis | kemkes clinical-term | ePus MTBS (2x) | 1 |
| 967 | OV000321 | Sangat pucat | kemkes clinical-term | ePus MTBS | 1 |
| 968 | 1237486008 | Pale discoloration of entire skin of body | snomed | ePus MTBS (2x) | 1 |
| 969 | OV000322 | Tidak pucat | kemkes clinical-term | ePus MTBS | 1 |
| 970 | OC000088 | Pemeriksaan tanda bahaya umum | kemkes clinical-term | ePus MTBS | 1 |
| 971 | 288853006 | Able to drink | snomed | ePus MTBS | 1 |
| 972 | OV000207 | Anak memuntahkan semua makanan dan minuman | kemkes clinical-term | ePus MTBS | 1 |
| 973 | SP000260 | Riwayat Kejang Selama Sakit | kemkes sp | ePus MTBS | 1 |
| 974 | 422768004 | Unresponsive | snomed | ePus MTBS | 1 |
| 975 | 130987000 | Acute confusion | snomed | ePus MTBS | 1 |
| 976 | OV000171 | Rewel | kemkes clinical-term | ePus MTBS | 1 |
| 977 | OV000208 | Anak tidak dapat ditenangkan | kemkes clinical-term | ePus MTBS | 1 |
| 978 | SP000259 | Pandangan Kosong atau Mata Tidak Membuka | kemkes sp | ePus MTBS | 1 |
| 979 | SP000258 | Anak Tidak Bersuara atau Menangis Melengking | kemkes sp | ePus MTBS | 1 |
| 980 | 67909005 | Chest wall retraction | snomed | ePus MTBS (2x) | 1 |
| 981 | 70407001 | Stridor | snomed | ePus MTBS | 1 |
| 982 | 248568003 | Nasal flaring | snomed | ePus MTBS | 1 |
| 983 | OV000211 | Anak mencari posisi paling nyaman dan menolak berbaring | kemkes clinical-term | ePus MTBS | 1 |
| 984 | 3415004 | Cyanosis | snomed | ePus MTBS, ePus MTBM | 2 |
| 985 | 26825009 | Cutis marmorata | snomed | ePus MTBS | 1 |
| 986 | OC000089 | Klasifikasi status kegawatan | kemkes clinical-term | ePus MTBS | 1 |
| 987 | 410429000 | Cardiac arrest | snomed | ePus MTBS | 1 |
| 988 | OV000137 | Penyakit sangat berat | kemkes clinical-term | ePus MTBS | 1 |
| 989 | 103228002 | Hemoglobin saturation with oxygen | snomed | ePus MTBS, ePus MTBM (2x) | 2 |
| 990 | OC000090 | Pemeriksaan tanda dan gejala sukar bernafas | kemkes clinical-term | ePus MTBS | 1 |
| 991 | 56018004 | Wheezing | snomed | ePus MTBS | 1 |
| 992 | OC000091 | Klasifikasi batuk dan/atau sukar bernapas | kemkes clinical-term | ePus MTBS | 1 |
| 993 | OV000287 | Pneumonia berat | kemkes clinical-term | ePus MTBS | 1 |
| 994 | 233604007 | Pneumonia | snomed | ePus MTBS | 1 |
| 995 | OV000288 | Batuk bukan pneumonia | kemkes clinical-term | ePus MTBS | 1 |
| 996 | 62315008 | Diarrhea | snomed | ePus MTBS, ePus MTBM | 2 |
| 997 | OC000113 | Durasi diare | kemkes clinical-term | ePus MTBS, ePus MTBM | 2 |
| 998 | 405729008 | Hematochezia | snomed | ePus MTBS | 1 |
| 999 | OC000097 | Pemeriksaan tanda dan gejala diare | kemkes clinical-term | ePus MTBS, ePus MTBM | 2 |
| 1000 | 214264003 | Lethargy | snomed | ePus MTBS (2x) | 1 |
| 1001 | SP000257 | Rewel atau Mudah Marah | kemkes sp | ePus MTBS | 1 |
| 1002 | 246923005 | Sunken eyes | snomed | ePus MTBS, ePus MTBM | 2 |
| 1003 | SP000256 | Tidak Bisa Minum atau Malas Minum | kemkes sp | ePus MTBS | 1 |
| 1004 | 17173007 | Excessive thirst | snomed | ePus MTBS | 1 |
| 1005 | SP000255 | Turgor Kulit Perut | kemkes sp | ePus MTBS, ePus MTBM | 2 |
| 1006 | OV000181 | Cubitan kulit perut kembalinya sangat lambat | kemkes clinical-term | ePus MTBS, ePus MTBM | 2 |
| 1007 | OV000182 | Cubitan kulit perut kembalinya lambat | kemkes clinical-term | ePus MTBS, ePus MTBM | 2 |
| 1008 | OC000098 | Klasifikasi diare | kemkes clinical-term | ePus MTBS, ePus MTBM | 2 |
| 1009 | OV000217 | Diare persisten berat | kemkes clinical-term | ePus MTBS | 1 |
| 1010 | OV000218 | Diare persisten | kemkes clinical-term | ePus MTBS | 1 |
| 1011 | 46799006 | Dysenteric diarrhea | snomed | ePus MTBS | 1 |
| 1012 | OV000214 | Diare dehidrasi berat | kemkes clinical-term | ePus MTBS | 1 |
| 1013 | OV000215 | Diare dehidrasi ringan/sedang | kemkes clinical-term | ePus MTBS | 1 |
| 1014 | OV000186 | Diare tanpa dehidrasi | kemkes clinical-term | ePus MTBS, ePus MTBM | 2 |
| 1015 | OV000219 | Daerah endemis tinggi | kemkes clinical-term | ePus MTBS | 1 |
| 1016 | OV000220 | Daerah endemis rendah | kemkes clinical-term | ePus MTBS | 1 |
| 1017 | 81264-4 | Fever duration | loinc | ePus MTBS | 1 |
| 1018 | OC000121 | Pemeriksaan tanda dan gejala demam | kemkes clinical-term | ePus MTBS | 1 |
| 1019 | 405947006 | Nuchal rigidity | snomed | ePus MTBS | 1 |
| 1020 | OV000222 | Ada penyebab lain dari demam | kemkes clinical-term | ePus MTBS | 1 |
| 1021 | OC000100 | Klasifikasi demam | kemkes clinical-term | ePus MTBS | 1 |
| 1022 | OV000223 | Penyakit berat dengan demam | kemkes clinical-term | ePus MTBS | 1 |
| 1023 | OV000224 | Demam mungkin bukan malaria | kemkes clinical-term | ePus MTBS | 1 |
| 1024 | OV000225 | Penyakit berat dengan demam | kemkes clinical-term | ePus MTBS | 1 |
| 1025 | OV000226 | Demam bukan malaria | kemkes clinical-term | ePus MTBS | 1 |
| 1026 | 14189004 | Measles | snomed | ePus MTBS (2x) | 1 |
| 1027 | OC000101 | Pemeriksaan tanda dan gejala campak | kemkes clinical-term | ePus MTBS | 1 |
| 1028 | 271807003 | Eruption of skin | snomed | ePus MTBS (2x) | 1 |
| 1029 | SP000253 | Batuk atau Pilek atau Mata Merah | kemkes sp | ePus MTBS | 1 |
| 1030 | 1071000119107 | Oral lesion | snomed | ePus MTBS | 1 |
| 1031 | OV000228 | Ada luka di mulut dalam atau luas | kemkes clinical-term | ePus MTBS | 1 |
| 1032 | 246679005 | Discharge from eye | snomed | ePus MTBS | 1 |
| 1033 | 64634000 | Corneal opacity | snomed | ePus MTBS | 1 |
| 1034 | OC000102 | Klasifikasi campak | kemkes clinical-term | ePus MTBS | 1 |
| 1035 | OV000229 | Campak dengan komplikasi berat | kemkes clinical-term | ePus MTBS | 1 |
| 1036 | SP000252 | Campak Dengan Komplikasi Pada Mata Dan/Atau Mulut | kemkes sp | ePus MTBS | 1 |
| 1037 | OC000104 | Pemeriksaan infeksi dengue | kemkes clinical-term | ePus MTBS | 1 |
| 1038 | OV000273 | Demam tinggi terus menerus | kemkes clinical-term | ePus MTBS | 1 |
| 1039 | OV000274 | Badan teraba dingin | kemkes clinical-term | ePus MTBS | 1 |
| 1040 | SP000251 | Lemas atau Gelisah | kemkes sp | ePus MTBS | 1 |
| 1041 | 422587007 | Nausea | snomed | ePus MTBS | 1 |
| 1042 | 422400008 | Vomiting | snomed | ePus MTBS | 1 |
| 1043 | OV000275 | Muntah terus menerus | kemkes clinical-term | ePus MTBS | 1 |
| 1044 | 21522001 | Abdominal pain | snomed | ePus MTBS | 1 |
| 1045 | SP000250 | Perdarahan Berupa Mimisan atau Muntah Darah (Coklat Seperti Kopi) atau BAB Berdarah (Berwarna Hitam) | kemkes sp | ePus MTBS | 1 |
| 1046 | 279001004 | Pain finding at anatomical site | snomed | ePus MTBS | 1 |
| 1047 | OV000276 | BAK terakhir ≥6 jam | kemkes clinical-term | ePus MTBS | 1 |
| 1048 | OV000233 | Kaki/ tangan tampak pucat | kemkes clinical-term | ePus MTBS | 1 |
| 1049 | OV000234 | Waktu pengisian kapiler >2 detik | kemkes clinical-term | ePus MTBS | 1 |
| 1050 | 771542000 | Cold extremity | snomed | ePus MTBS | 1 |
| 1051 | 64661000 | Thready pulse | snomed | ePus MTBS | 1 |
| 1052 | 86651002 | Pulse fast | snomed | ePus MTBS | 1 |
| 1053 | OV000235 | Nyeri tekan perut kanan atas | kemkes clinical-term | ePus MTBS | 1 |
| 1054 | 17672001 | Accumulation of fluid | snomed | ePus MTBS | 1 |
| 1055 | 271813007 | Petechiae | snomed | ePus MTBS | 1 |
| 1056 | 249366005 | Bleeding from nose | snomed | ePus MTBS | 1 |
| 1057 | 18165001 | Jaundice | snomed | ePus MTBS, ePus MTBM (2x) | 2 |
| 1058 | 17077006 | Abnormal respiratory rate | snomed | ePus MTBS | 1 |
| 1059 | OV000236 | Ada pembesaran hepar >2 cm | kemkes clinical-term | ePus MTBS | 1 |
| 1060 | 38520-3 | Capillary fragility | loinc | ePus MTBS | 1 |
| 1061 | 846603004 | Positive capillary fragility test | snomed | ePus MTBS | 1 |
| 1062 | 829990003 | Negative capillary fragility test | snomed | ePus MTBS | 1 |
| 1063 | 75377-2 | Dengue virus NS1 Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | loinc | ePus MTBS (3x) | 1 |
| 1064 | OC000105 | Klasifikasi infeksi dengue | kemkes clinical-term | ePus MTBS | 1 |
| 1065 | 20927009 | Dengue hemorrhagic fever | snomed | ePus MTBS | 1 |
| 1066 | 722863008 | Dengue with warning signs | snomed | ePus MTBS | 1 |
| 1067 | 722862003 | Dengue without warning signs | snomed | ePus MTBS | 1 |
| 1068 | OV000129 | Demam mungkin bukan dengue | kemkes clinical-term | ePus MTBS | 1 |
| 1069 | 300197009 | Ear problem | snomed | ePus MTBS (2x) | 1 |
| 1070 | OC000106 | Pemeriksaan tanda dan gejala masalah telinga | kemkes clinical-term | ePus MTBS | 1 |
| 1071 | 301354004 | Pain of ear | snomed | ePus MTBS | 1 |
| 1072 | OV000278 | Ada rasa penuh di telinga | kemkes clinical-term | ePus MTBS | 1 |
| 1073 | 300132001 | Ear discharge | snomed | ePus MTBS | 1 |
| 1074 | 162364004 | Ear discharge present | snomed | ePus MTBS | 1 |
| 1075 | 300874009 | Swelling of ear | snomed | ePus MTBS | 1 |
| 1076 | OC000107 | Klasifikasi masalah telinga | kemkes clinical-term | ePus MTBS | 1 |
| 1077 | 52404001 | Mastoiditis | snomed | ePus MTBS | 1 |
| 1078 | OV000241 | Infeksi telinga akut | kemkes clinical-term | ePus MTBS | 1 |
| 1079 | OV000289 | Infeksi telinga kronis | kemkes clinical-term | ePus MTBS | 1 |
| 1080 | OV000242 | Tidak ada infeksi telinga | kemkes clinical-term | ePus MTBS | 1 |
| 1081 | 284521000 | Pitting edema | snomed | ePus MTBS | 1 |
| 1082 | 420829009 | 1+ pitting edema | snomed | ePus MTBS | 1 |
| 1083 | 421605005 | 2+ pitting edema | snomed | ePus MTBS | 1 |
| 1084 | 421346005 | 3+ pitting edema | snomed | ePus MTBS | 1 |
| 1085 | 1153600001 | Weight for height z-score | snomed | ePus MTBS, ePus Tumbang Anak, ePus Tumbang DDTK, SiGizi Balita BNBA, SiGizi Balita Vitamin A, SiGizi Balita Mendapat PMT 2024, SiGizi Balita MPASI, SiGizi PMT 2025 BB Tidak Naik - Riwayat (2x), SiGizi PMT 2025 BB Kurang - Riwayat (2x), SiGizi PMT 2025 Gizi Kurang - Pantau (9x), SiGizi PMT 2025 Gizi Kurang - Riwayat (2x) | 11 |
| 1086 | 1153598007 | Weight for length z score | snomed | ePus MTBS (2x), ePus Tumbang Anak, ePus Tumbang DDTK, SiGizi Balita BNBA, SiGizi Balita Vitamin A, SiGizi Balita Mendapat PMT 2024, SiGizi Balita MPASI, SiGizi PMT 2025 BB Tidak Naik - Riwayat (2x), SiGizi PMT 2025 BB Kurang - Riwayat (2x), SiGizi PMT 2025 Gizi Kurang - Pantau (9x), SiGizi PMT 2025 Gizi Kurang - Riwayat (2x) | 11 |
| 1087 | OV000253 | Terlalu lemah untuk menyusu | kemkes clinical-term | ePus MTBS | 1 |
| 1088 | 271398006 | Weight steady | snomed | ePus MTBS | 1 |
| 1089 | OC000108 | Klasifikasi status gizi | kemkes clinical-term | ePus MTBS | 1 |
| 1090 | OI000004 | Risiko Gizi Lebih | kemkes clinical-term | ePus MTBS, ePus Tumbang Anak, ASIK CKG Balita (v2) (2x), SiGizi Balita BNBA, SiGizi Balita Vitamin A, SiGizi Balita Mendapat PMT 2024, SiGizi Balita MPASI, SiGizi PMT 2025 BB Tidak Naik - Riwayat (2x), SiGizi PMT 2025 BB Kurang - Riwayat (2x), SiGizi PMT 2025 Gizi Kurang - Riwayat (2x) | 10 |
| 1091 | OV000254 | Gizi buruk dengan komplikasi berat | kemkes clinical-term | ePus MTBS | 1 |
| 1092 | OV000255 | Gizi buruk tanpa komplikasi | kemkes clinical-term | ePus MTBS | 1 |
| 1093 | 1153604005 | Body height for age z-score | snomed | ePus MTBS, ePus Tumbang Anak, ePus Tumbang DDTK, SiGizi Balita BNBA, SiGizi Balita Vitamin A, SiGizi Balita Mendapat PMT 2024, SiGizi Balita MPASI, SiGizi PMT 2025 BB Tidak Naik - Riwayat (2x), SiGizi PMT 2025 BB Kurang - Riwayat (2x), SiGizi PMT 2025 Gizi Kurang - Riwayat (2x) | 10 |
| 1094 | 1153594009 | Head circumference for age z-score | snomed | ePus MTBS | 1 |
| 1095 | OC000111 | Klasifikasi anemia | kemkes clinical-term | ePus MTBS | 1 |
| 1096 | OV000272 | Anemia berat | kemkes clinical-term | ePus MTBS | 1 |
| 1097 | 271737000 | Anemia | snomed | ePus MTBS | 1 |
| 1098 | PC000013 | Riwayat tes HIV ibu | kemkes clinical-term | ePus MTBS, ePus MTBM | 2 |
| 1099 | SP000247 | Hasil Tes HIV Ibu | kemkes sp | ePus MTBS | 1 |
| 1100 | PC000014 | Riwayat tes HIV anak | kemkes clinical-term | ePus MTBS, ePus MTBM | 2 |
| 1101 | SP000248 | Hasil Tes HIV Anak | kemkes sp | ePus MTBS | 1 |
| 1102 | OC000084 | Tes virologis HIV anak | kemkes clinical-term | ePus MTBS, ePus MTBM | 2 |
| 1103 | OC000083 | Tes serologis HIV anak | kemkes clinical-term | ePus MTBS, ePus MTBM | 2 |
| 1104 | 63895-7 | Breastfeeding status | loinc | ePus MTBS, ePus MTBM (2x), SiGizi Balita MPASI | 3 |
| 1105 | 254387007 | Human immunodeficiency virus infection classification systems | snomed | ePus MTBS, ePus MTBM | 2 |
| 1106 | OV000187 | Terpajan HIV: mungkin infeksi HIV | kemkes clinical-term | ePus MTBS, ePus MTBM | 2 |
| 1107 | SP000249 | Mungkin Bukan Infeksi HIV | kemkes sp | ePus MTBS | 1 |
| 1108 | 8 | Hep B, adolescent or pediatric | http://hl7.org/fhir/sid/cvx | ePus MTBS, ePus MTBM | 2 |
| 1109 | VG45 | HepB | kfa | ePus MTBS (5x), ePus MTBM, ELSMIL Baduta, SIHEPI Rekap 3e, SIM RS Narmada INC (2x), SIM RS Panti Nugroho BBL (2x), SIM RS Ummu Hani BBL (2x), SIM RS MPH BBL, SIM RS Siaga Medika BBL | 9 |
| 1110 | 198 | DTP-hepB-Hib Pentavalent Non-US | http://hl7.org/fhir/sid/cvx | ePus MTBS (4x) | 1 |
| 1111 | VG107 | DTAP | kfa | ePus MTBS (4x) | 1 |
| 1112 | VG17 | HIB | kfa | ePus MTBS (4x) | 1 |
| 1113 | 129 | Japanese Encephalitis, unspecified formulation | http://hl7.org/fhir/sid/cvx | ePus MTBS | 1 |
| 1114 | VG129 | Japanese encephalitis | kfa | ePus MTBS | 1 |
| 1115 | 19 | BCG | http://hl7.org/fhir/sid/cvx | ePus MTBS, ePus MTBM | 2 |
| 1116 | VG19 | BCG | kfa | ePus MTBS, ePus MTBM | 2 |
| 1117 | 02 | OPV | http://hl7.org/fhir/sid/cvx | ePus MTBS (4x), ePus MTBM | 2 |
| 1118 | VG89 | POLIO | kfa | ePus MTBS (5x), ePus MTBM | 2 |
| 1119 | 152 | Pneumococcal Conjugate, unspecified formulation | http://hl7.org/fhir/sid/cvx | ePus MTBS (3x) | 1 |
| 1120 | VG152 | PneumoPCV | kfa | ePus MTBS (3x) | 1 |
| 1121 | 04 | M/R | http://hl7.org/fhir/sid/cvx | ePus MTBS (2x) | 1 |
| 1122 | VG03 | MMR | kfa | ePus MTBS (2x) | 1 |
| 1123 | 10 | IPV | http://hl7.org/fhir/sid/cvx | ePus MTBS | 1 |
| 1124 | OC000114 | Membutuhkan suplemen vitamin A | kemkes clinical-term | ePus MTBS | 1 |
| 1125 | 92000354 | Retinol Palmitate 100.000 IU Kapsul Lunak | http://sys-ids.kemkes.go.id/kf | ePus MTBS, SiGizi Balita Vitamin A | 2 |
| 1126 | Neonate | Neonate | episodeofcare-type | ePus MTBM, SIM RS Tripat BBL (sheet 'INC BBL'), SIM RS Narmada INC, SIM RS Panti Nugroho BBL, SIM RS Ummu Hani BBL, SIM RS MPH BBL, SIM RS Siaga Medika BBL, SIM RS Goetoeng BBL | 8 |
| 1127 | PC000003 | Manajemen Terpadu Bayi Muda (MTBM) | kemkes clinical-term | ePus MTBM | 1 |
| 1128 | 68276009 | Bottle, device | snomed | ePus MTBM (2x) | 1 |
| 1129 | 468332001 | Drinking cup | snomed | ePus MTBM (2x) | 1 |
| 1130 | 394841004 | Other category | snomed | ePus MTBM | 1 |
| 1131 | OC000078 | Pemeriksaan tanda dan gejala infeksi | kemkes clinical-term | ePus MTBM | 1 |
| 1132 | OV000167 | Bayi tidak BAB 48 jam setelah lahir | kemkes clinical-term | ePus MTBM | 1 |
| 1133 | SP000264 | Muntah Berisi Susu atau Cairan Berwarna Hijau | kemkes sp | ePus MTBM (3x) | 1 |
| 1134 | 116289008 | Abdominal bloating | snomed | ePus MTBM (2x) | 1 |
| 1135 | 230145002 | Difficulty breathing | snomed | ePus MTBM (2x) | 1 |
| 1136 | SP000265 | Bayi Tampak Lemah atau Tidak Mau Menghisap | kemkes sp | ePus MTBM | 1 |
| 1137 | SP000266 | Ada Tanda Biru di Sekitar Mulut Saat Menangis atau Menghisap | kemkes sp | ePus MTBM | 1 |
| 1138 | 267036007 | Dyspnea | snomed | ePus MTBM | 1 |
| 1139 | 260407003 | Weak | snomed | ePus MTBM | 1 |
| 1140 | 284511008 | Difficulty in initiating movement | snomed | ePus MTBM | 1 |
| 1141 | OV000124 | Bayi tidak mau mengisap | kemkes clinical-term | ePus MTBM | 1 |
| 1142 | SP000267 | Ada Gerakan Kejang | kemkes sp | ePus MTBM | 1 |
| 1143 | OV000125 | Suhu tubuh >37,5°C | kemkes clinical-term | ePus MTBM | 1 |
| 1144 | SP000268 | Suhu tubuh <37,5°C | kemkes sp | ePus MTBM | 1 |
| 1145 | 204712000 | Anal atresia | snomed | ePus MTBM | 1 |
| 1146 | SP000269 | Kondisi Mata Bernanah | kemkes sp | ePus MTBM | 1 |
| 1147 | OV000130 | Mata bernanah banyak | kemkes clinical-term | ePus MTBM | 1 |
| 1148 | OV000131 | Mata bernanah sedikit | kemkes clinical-term | ePus MTBM | 1 |
| 1149 | OV000132 | Pusar kemerahan | kemkes clinical-term | ePus MTBM | 1 |
| 1150 | OV000282 | Pusar kemerahan meluas sampai dinding perut >1 cm | kemkes clinical-term | ePus MTBM | 1 |
| 1151 | 35745008 | Umbilical discharge | snomed | ePus MTBM | 1 |
| 1152 | 271760008 | Pustule | snomed | ePus MTBM | 1 |
| 1153 | 62085005 | Grunting respiration | snomed | ePus MTBM | 1 |
| 1154 | OV000133 | Perbedaan saturasi oksigen >3% | kemkes clinical-term | ePus MTBM | 1 |
| 1155 | 301283003 | Finding of rate of respiration | snomed | ePus MTBM | 1 |
| 1156 | 271823003 | Tachypnea | snomed | ePus MTBM | 1 |
| 1157 | 86684002 | Bradypnea | snomed | ePus MTBM | 1 |
| 1158 | OC000126 | Klasifikasi infeksi | kemkes clinical-term | ePus MTBM | 1 |
| 1159 | OV000134 | Infeksi bakteri berat | kemkes clinical-term | ePus MTBM | 1 |
| 1160 | OV000135 | Infeksi bakteri lokal | kemkes clinical-term | ePus MTBM | 1 |
| 1161 | OV000136 | Mungkin bukan infeksi | kemkes clinical-term | ePus MTBM | 1 |
| 1162 | OC000128 | Umur pertama kali timbul kuning | kemkes clinical-term | ePus MTBM | 1 |
| 1163 | OV000174 | Timbul kuning pada hari pertama (<24 jam) setelah lahir | kemkes clinical-term | ePus MTBM | 1 |
| 1164 | OV000175 | Timbul kuning pada umur >24 jam sampai dengan umur 14 hari | kemkes clinical-term | ePus MTBM | 1 |
| 1165 | OV000176 | Timbul kuning pada umur >14 hari | kemkes clinical-term | ePus MTBM | 1 |
| 1166 | SP000214 | Pemeriksaan Kondisi Ikterus | kemkes sp | ePus MTBM | 1 |
| 1167 | SP000215 | Kuning Pada Mata atau Kulit | kemkes sp | ePus MTBM | 1 |
| 1168 | SP000216 | Kuning Pada Telapak Tangan dan Telapak Kaki | kemkes sp | ePus MTBM | 1 |
| 1169 | OC000129 | Klasifikasi ikterus | kemkes clinical-term | ePus MTBM | 1 |
| 1170 | OV000179 | Ikterus berat | kemkes clinical-term | ePus MTBM | 1 |
| 1171 | OV000180 | Tidak ada ikterus | kemkes clinical-term | ePus MTBM | 1 |
| 1172 | OV000127 | Bayi bergerak atas kemauan sendiri | kemkes clinical-term | ePus MTBM | 1 |
| 1173 | OV000128 | Bayi bergerak hanya ketika dirangsang | kemkes clinical-term | ePus MTBM | 1 |
| 1174 | 302001007 | Does not move | snomed | ePus MTBM | 1 |
| 1175 | SP000270 | Gelisah atau Rewel | kemkes sp | ePus MTBM | 1 |
| 1176 | OV000183 | Cubitan kulit perut kembali segera | kemkes clinical-term | ePus MTBM | 1 |
| 1177 | OV000184 | Diare dehidrasi berat | kemkes clinical-term | ePus MTBM | 1 |
| 1178 | OV000185 | Diare dehidrasi ringan/sedang | kemkes clinical-term | ePus MTBM | 1 |
| 1179 | OC000079 | Tes serologis HIV ibu | kemkes clinical-term | ePus MTBM | 1 |
| 1180 | OV000188 | Infeksi HIV tidak diketahui | kemkes clinical-term | ePus MTBM | 1 |
| 1181 | OV000189 | Bukan infeksi HIV | kemkes clinical-term | ePus MTBM | 1 |
| 1182 | 1153593003 | Weight for age z-score | snomed | ePus MTBM (2x), ePus Tumbang Anak, SiGizi Balita BNBA, SiGizi Balita Vitamin A, SiGizi Balita Mendapat PMT 2024, SiGizi Balita MPASI, SiGizi PMT 2025 BB Tidak Naik - Pantau (3x), SiGizi PMT 2025 BB Tidak Naik - Riwayat (2x), SiGizi PMT 2025 BB Kurang - Pantau (5x), SiGizi PMT 2025 BB Kurang - Riwayat (2x), SiGizi PMT 2025 Gizi Kurang - Riwayat (2x) | 11 |
| 1183 | OV000190 | < 2 kg (umur < 7 hari) | kemkes clinical-term | ePus MTBM (2x) | 1 |
| 1184 | 79740000 | Candidiasis of mouth | snomed | ePus MTBM (2x) | 1 |
| 1185 | SP000271 | Terdapat Celah Bibir atau Langit-Langit | kemkes sp | ePus MTBM (2x) | 1 |
| 1186 | OC000082 | Posisi menyusu bayi | kemkes clinical-term | ePus MTBM | 1 |
| 1187 | OV000193 | Posisi menyusu bayi benar | kemkes clinical-term | ePus MTBM | 1 |
| 1188 | OV000194 | Posisi menyusu bayi salah | kemkes clinical-term | ePus MTBM | 1 |
| 1189 | OC000081 | Posisi pelekatan bayi pada puting | kemkes clinical-term | ePus MTBM | 1 |
| 1190 | OV000195 | Tidak melekat sama sekali | kemkes clinical-term | ePus MTBM | 1 |
| 1191 | OV000196 | Tidak melekat dengan baik | kemkes clinical-term | ePus MTBM | 1 |
| 1192 | OV000197 | Melekat dengan baik | kemkes clinical-term | ePus MTBM | 1 |
| 1193 | OC000080 | Efektifitas hisapan bayi | kemkes clinical-term | ePus MTBM | 1 |
| 1194 | OV000198 | Tidak mengisap sama sekali | kemkes clinical-term | ePus MTBM | 1 |
| 1195 | OV000199 | Tidak mengisap dengan efektif | kemkes clinical-term | ePus MTBM | 1 |
| 1196 | OV000200 | Mengisap dengan efektif | kemkes clinical-term | ePus MTBM | 1 |
| 1197 | OC000085 | Klasifikasi berat badan menurut umur dan/atau masalah pemberian ASI | kemkes clinical-term | ePus MTBM | 1 |
| 1198 | OV000201 | Berat badan sangat rendah menurut umur | kemkes clinical-term | ePus MTBM (2x) | 1 |
| 1199 | OV000202 | Berat badan rendah menurut umur dan/atau masalah pemberian ASI | kemkes clinical-term | ePus MTBM | 1 |
| 1200 | OV000203 | Berat badan tidak rendah menurut umur dan tidak ada masalah pemberian ASI | kemkes clinical-term | ePus MTBM | 1 |
| 1201 | OC000086 | Klasifikasi Berat Badan Menurut Umur dan/atau Masalah Pemberian Minum | kemkes clinical-term | ePus MTBM | 1 |
| 1202 | OV000204 | Berat badan rendah menurut umur dan/atau masalah pemberian minum | kemkes clinical-term | ePus MTBM | 1 |
| 1203 | OV000205 | Berat badan tidak rendah menurut umur dan tidak ada masalah pemberian minum | kemkes clinical-term | ePus MTBM | 1 |
| 1204 | OC000087 | Pemberian Vitamin K pada Bayi Baru Lahir | kemkes clinical-term | ePus MTBM | 1 |
| 1205 | 448883004 | Injection of vitamin K1 | snomed | ePus MTBM | 1 |
| 1206 | 8308-9 | Body height --standing | loinc | ePus Tumbang Anak, ePus Tumbang DDTK, ASIK CKG Balita (v2), SiGizi Balita BNBA, SiGizi Balita Vitamin A, SiGizi Balita Mendapat PMT 2024, SiGizi Balita Pemantauan PMT 2024, SiGizi PMT 2025 BB Tidak Naik - Riwayat (2x), SiGizi PMT 2025 BB Kurang - Riwayat (2x), SiGizi PMT 2025 Gizi Kurang - Pantau (9x), SiGizi PMT 2025 Gizi Kurang - Riwayat (2x) | 11 |
| 1207 | 8306-3 | Body height --lying | loinc | ePus Tumbang Anak, ePus Tumbang DDTK, ASIK CKG Balita (v2), SiGizi Balita BNBA, SiGizi Balita Vitamin A, SiGizi Balita Mendapat PMT 2024, SiGizi Balita Pemantauan PMT 2024, SiGizi PMT 2025 BB Tidak Naik - Riwayat (2x), SiGizi PMT 2025 BB Kurang - Riwayat (2x), SiGizi PMT 2025 Gizi Kurang - Pantau (9x), SiGizi PMT 2025 Gizi Kurang - Riwayat (2x), SIM RS MPH BBL, SIM RS Siaga Medika BBL | 13 |
| 1208 | 50373000 | Body height measure | loinc | ePus Tumbang Anak, SiGizi Balita BNBA, SiGizi Balita Vitamin A | 3 |
| 1209 | 10904000 | Standing position | snomed | ePus Tumbang Anak, SiGizi Balita BNBA, SiGizi Balita Vitamin A | 3 |
| 1210 | 102538003 | Recumbent body position | snomed | ePus Tumbang Anak, SiGizi Balita BNBA, SiGizi Balita Vitamin A | 3 |
| 1211 | OC000012 | Kenaikan Berat Badan Adekuat | kemkes  | ePus Tumbang Anak | 1 |
| 1212 | 1153590000 | Length for age z-score | snomed | ePus Tumbang Anak, ePus Tumbang DDTK, SiGizi Balita BNBA, SiGizi Balita Vitamin A, SiGizi Balita Mendapat PMT 2024, SiGizi Balita MPASI, SiGizi PMT 2025 BB Tidak Naik - Riwayat (2x), SiGizi PMT 2025 BB Kurang - Riwayat (2x), SiGizi PMT 2025 Gizi Kurang - Riwayat (2x) | 9 |
| 1213 | OI000010 | Risiko Berat Badan Lebih | kemkes clinical-term | ePus Tumbang Anak, ASIK CKG Balita (v2), SiGizi Balita BNBA, SiGizi Balita Vitamin A, SiGizi Balita Mendapat PMT 2024, SiGizi Balita MPASI, SiGizi PMT 2025 BB Tidak Naik - Riwayat (2x), SiGizi PMT 2025 BB Kurang - Riwayat (2x), SiGizi PMT 2025 Gizi Kurang - Riwayat (2x) | 9 |
| 1214 | OI000007 | Berat Badan Sangat Kurang | kemkes clinical-term | ePus Tumbang Anak, ASIK CKG Balita (v2), SiGizi Balita BNBA, SiGizi Balita Vitamin A, SiGizi Balita Mendapat PMT 2024, SiGizi PMT 2025 BB Tidak Naik - Riwayat (2x), SiGizi PMT 2025 BB Kurang - Riwayat (2x), SiGizi PMT 2025 Gizi Kurang - Riwayat (2x) | 8 |
| 1215 | 1153594009 | Head circumference for age z-score | loinc | ePus Tumbang Anak, ePus Tumbang DDTK | 2 |
| 1216 | 170218003 | Child examination: gross motor development | snomed | ePus Tumbang Anak (3x), ePus Tumbang DDTK | 2 |
| 1217 | 170219006 | Child examination: fine motor development | snomed | ePus Tumbang Anak (3x), ePus Tumbang DDTK | 2 |
| 1218 | SP000062 | Pemeriksaan Anak: Bicara dan Bahasa | kemkes sp | ePus Tumbang Anak (3x), ePus Tumbang DDTK | 2 |
| 1219 | SP000155 | Pemeriksaan Anak: Sosialisasi dan Kemandirian | kemkes sp | ePus Tumbang Anak (3x) | 1 |
| 1220 | 410519009 | At risk | snomed | ePus Tumbang Anak (5x), ePus Tumbang DDTK (6x) | 2 |
| 1221 | 1145307003 | Exclusively breastfed | snomed | ePus Tumbang Anak, ELSMIL Baduta, SiGizi Balita ASI Eksklusif (7x) | 3 |
| 1222 | OC000009 | Makanan Pendamping ASI (MPASI) | kemkes clinical-term | ePus Tumbang Anak | 1 |
| 1223 | 723509005 | High risk | snomed | ePus Tumbang Anak, ASIK Skrining PTM (2x) | 2 |
| 1224 | 408429008 | Recommendation to caregiver regarding child's development program | snomed | ePus Tumbang Anak | 1 |
| 1225 | SP000061 | Intervensi Dini Masalah Perkembangan Anak | kemkes sp | ePus Tumbang Anak, ePus Tumbang DDTK | 2 |
| 1226 | SP000064 | Tindakan Pengobatan Lain | kemkes sp | ePus Tumbang Anak, ePus Tumbang DDTK | 2 |
| 1227 | OC000034 | Surat Pengantar Rujukan | kemkes clinical-term | ePus Tumbang Anak, ePus Tumbang DDTK | 2 |
| 1228 | 1153596006 | Body mass index for age z-score | snomed | ePus Tumbang DDTK (2x) | 1 |
| 1229 | SP000059 | Tren Pertumbuhan Anak | kemkes sp | ePus Tumbang DDTK | 1 |
| 1230 | 58236001 | Normal growth | snomed | ePus Tumbang DDTK | 1 |
| 1231 | 440301000124106 | Below expected growth rate | snomed | ePus Tumbang DDTK | 1 |
| 1232 | 704352005 | At increased risk of delayed growth | snomed | ePus Tumbang DDTK | 1 |
| 1233 | SP000057 | Perlambatan Pertumbuhan Linear | kemkes sp | ePus Tumbang DDTK | 1 |
| 1234 | SP000058 | Early Adiposity Rebound | kemkes sp | ePus Tumbang DDTK | 1 |
| 1235 | Ds | Perkembangan sesuai usia | http://terminology.kemkes.go.id/Codesystem/kpsp | ePus Tumbang DDTK, ASIK CKG Balita (v2) | 2 |
| 1236 | Dm | Perkembangan meragukan | http://terminology.kemkes.go.id/Codesystem/kpsp | ePus Tumbang DDTK, ASIK CKG Balita (v2) | 2 |
| 1237 | Dp | Perkembangan curiga adanya penyimpangan | http://terminology.kemkes.go.id/Codesystem/kpsp | ePus Tumbang DDTK, ASIK CKG Balita (v2) | 2 |
| 1238 | 64957009 | Uncertain | snomed | ePus Tumbang DDTK (2x) | 1 |
| 1239 | 441041000124100 | Counseling about nutrition | icd-9-cm | ePus Tumbang DDTK | 1 |
| 1240 | 410295000 | Growth/development education, guidance, and counseling | icd-9-cm | ePus Tumbang DDTK | 1 |
| 1241 | SP000060 | Intervensi Dini Masalah Pertumbuhan Anak | kemkes sp | ePus Tumbang DDTK | 1 |
| 1242 | SP000063 | Intervensi Dini Masalah Perilaku & Emosi | kemkes sp | ePus Tumbang DDTK | 1 |
| 1243 | SRR000011 | Monitoring rutin | kemkes clinical-term | ePus Tumbang DDTK | 1 |
| 1244 | SRR000012 | PPIA | kemkes clinical-term | ePus Tumbang DDTK | 1 |
| 1245 | SR000001 | Penanganan / perawatan lanjut pasien (medik) | kemkes clinical-term | ePus Tumbang DDTK | 1 |
| 1246 | SR000002 | Sarana dan prasarana (Ruang Perawatan Biasa) | kemkes clinical-term | ePus Tumbang DDTK | 1 |
| 1247 | SR000003 | Sarana dan prasarana (Ruang intensive (ICU, CVCU/ICCU, NICU, PICU, HCU)) | kemkes clinical-term | ePus Tumbang DDTK | 1 |
| 1248 | SR000004 | Sarana dan prasarana (Ruang Isolasi) | kemkes clinical-term | ePus Tumbang DDTK | 1 |
| 1249 | SR000005 | Dokter spesialis / sub spesialis tidak tersedia | kemkes clinical-term | ePus Tumbang DDTK | 1 |
| 1250 | SR000006 | Tindakan Khusus | kemkes clinical-term | ePus Tumbang DDTK | 1 |
| 1251 | SR000007 | Rujuk balik | kemkes clinical-term | ePus Tumbang DDTK | 1 |
| 1252 | 171128005 | Venereal disease screening | snomed | ePus Tumbang DDTK | 1 |
| 1253 | 863888006 | 6/60 visual acuity of left eye | snomed | ePus Tumbang TDL | 1 |
| 1254 | 400911007 | Tumbling E test | snomed | ePus Tumbang TDL (4x) | 1 |
| 1255 | 863887001 | 6/60 visual acuity of right eye | snomed | ePus Tumbang TDL | 1 |
| 1256 | 836333004 | 6/12 visual acuity of left eye | snomed | ePus Tumbang TDL | 1 |
| 1257 | 836332009 | 6/12 visual acuity of right eye | snomed | ePus Tumbang TDL | 1 |
| 1258 | 104890-9 | Nationality Person Narrative | loinc | Dapodik PAUD | 1 |
| 1259 | 170245002 | Child examination: school screening | snomed | Dapodik PAUD | 1 |
| 1260 | 365481000 | Finding of household composition | snomed | Dapodik PAUD | 1 |
| 1261 | SP000241 | Moda Transportasi yang digunakan untuk bersekolah | kemkes sp | Dapodik PAUD | 1 |
| 1262 | SP000239 | Kartu Perlindungan Sosial | kemkes sp | Dapodik PAUD (2x) | 1 |
| 1263 | 82589-3 | Highest level of education | loinc | Dapodik PAUD (3x), SIPTM, SIM RS Goetoeng INC, SIM RS Goetoeng PNC, SIM RS Goetoeng BBL | 5 |
| 1264 | OC000149 | Pekerjaan orang tua | kemkes clinical-term | Dapodik PAUD (4x) | 1 |
| 1265 | 81323004 | Normal general body function | snomed | Dapodik PAUD (3x) | 1 |
| 1266 | 397540003 | Visual impairment | snomed | Dapodik PAUD (3x) | 1 |
| 1267 | 15188001 | Hearing loss | snomed | Dapodik PAUD (3x) | 1 |
| 1268 | 86765009 | Mild intellectual disability | snomed | Dapodik PAUD (3x) | 1 |
| 1269 | 61152003 | Moderate intellectual disability | snomed | Dapodik PAUD (3x) | 1 |
| 1270 | 8510008 | Reduced mobility | snomed | Dapodik PAUD (3x) | 1 |
| 1271 | 160693001 | Mobility poor | snomed | Dapodik PAUD (3x) | 1 |
| 1272 | 5793009 | Mixed behavior and emotional disorder | snomed | Dapodik PAUD (3x) | 1 |
| 1273 | 29164008 | Disturbance in speech | snomed | Dapodik PAUD (3x) | 1 |
| 1274 | 406134008 | Multiple disability | snomed | Dapodik PAUD (3x) | 1 |
| 1275 | 44548000 | Hyperactive behavior | snomed | Dapodik PAUD (3x) | 1 |
| 1276 | 8273004 | Intelligence quotient high | snomed | Dapodik PAUD (3x) | 1 |
| 1277 | 367358004 | Above average intellect | snomed | Dapodik PAUD (3x) | 1 |
| 1278 | 1855002 | Developmental academic disorder | snomed | Dapodik PAUD (3x) | 1 |
| 1279 | 70545002 | Narcotic drug user | snomed | Dapodik PAUD (3x) | 1 |
| 1280 | 247701008 | Abnormal perception | snomed | Dapodik PAUD (3x) | 1 |
| 1281 | 41040004 | Complete trisomy 21 syndrome | snomed | Dapodik PAUD (3x) | 1 |
| 1282 | 35919005 | Pervasive developmental disorder | snomed | Dapodik PAUD (3x) | 1 |
| 1283 | 365552003 | Finding of income details | snomed | Dapodik PAUD (3x) | 1 |
| 1284 | SP000232 | Kartu Indonesia Pintar | kemkes sp | Dapodik PAUD | 1 |
| 1285 | SP000327 | Tetap akan menerima KIP | kemkes sp | Dapodik PAUD | 1 |
| 1286 | SP000243 | Program Indonesia Pintar | kemkes sp | Dapodik PAUD (2x) | 1 |
| 1287 | SP000317 | Layak menerima PIP | kemkes sp | Dapodik PAUD | 1 |
| 1288 | SP000318 | Alasan Layak PIP | kemkes sp | Dapodik PAUD | 1 |
| 1289 | SP000319 | Daerah konflik | kemkes sp | Dapodik PAUD | 1 |
| 1290 | SP000320 | Dampak bencana | kemkes sp | Dapodik PAUD | 1 |
| 1291 | SP000321 | Kelainan fisik | kemkes sp | Dapodik PAUD | 1 |
| 1292 | SP000322 | Keluarga narapidana | kemkes sp | Dapodik PAUD | 1 |
| 1293 | SP000323 | Pemegang PKH/KPS/KKS | kemkes sp | Dapodik PAUD | 1 |
| 1294 | SP000324 | Pernah Dropout | kemkes sp | Dapodik PAUD | 1 |
| 1295 | SP000325 | Siswa miskin/rentan miskin | kemkes sp | Dapodik PAUD | 1 |
| 1296 | SP000326 | Yatim Piatu/Panti Asuhan/Panti Sosial | kemkes sp | Dapodik PAUD | 1 |
| 1297 | 365475008 | Place in family order | snomed | Dapodik PAUD, ELSMIL Baduta (2x) | 2 |
| 1298 | 224095004 | Number of siblings | snomed | Dapodik PAUD | 1 |
| 1299 | SP000230 | Jarak dari rumah ke sekolah | kemkes sp | Dapodik PAUD | 1 |
| 1300 | SP000290 | Kurang dari 1 km | kemkes sp | Dapodik PAUD | 1 |
| 1301 | SP000291 | Lebih dari 1 km | kemkes sp | Dapodik PAUD | 1 |
| 1302 | SP000292 | Jarak dari rumah ke sekolah (km) | kemkes sp | Dapodik PAUD | 1 |
| 1303 | SP000293 | Waktu tempuh dari rumah ke sekolah | kemkes sp | Dapodik PAUD | 1 |
| 1304 | 105421008 | Educational achievement | snomed | Dapodik PAUD | 1 |
| 1305 | SP000294 | Jenis Prestasi | kemkes sp | Dapodik PAUD | 1 |
| 1306 | SP000300 | Sains | kemkes sp | Dapodik PAUD | 1 |
| 1307 | SP000301 | Seni | kemkes sp | Dapodik PAUD | 1 |
| 1308 | SP000302 | Olahraga | kemkes sp | Dapodik PAUD | 1 |
| 1309 | SP000295 | Tingkatan Prestasi | kemkes sp | Dapodik PAUD | 1 |
| 1310 | SP000303 | Tingkat Sekolah | kemkes sp | Dapodik PAUD | 1 |
| 1311 | SP000304 | Tingkat Kecamatan | kemkes sp | Dapodik PAUD | 1 |
| 1312 | SP000305 | Tingkat Kabupaten | kemkes sp | Dapodik PAUD | 1 |
| 1313 | SP000306 | Tingkat Provinsi | kemkes sp | Dapodik PAUD | 1 |
| 1314 | SP000307 | Tingkat Nasional | kemkes sp | Dapodik PAUD | 1 |
| 1315 | SP000308 | Tingkat Internasional | kemkes sp | Dapodik PAUD | 1 |
| 1316 | SP000297 | Nama Prestasi | kemkes sp | Dapodik PAUD | 1 |
| 1317 | SP000298 | Tahun Prestasi | kemkes sp | Dapodik PAUD | 1 |
| 1318 | SP000299 | Penyelenggara | kemkes sp | Dapodik PAUD | 1 |
| 1319 | SP000309 | Beasiswa | kemkes sp | Dapodik PAUD | 1 |
| 1320 | SP000310 | Jenis Beasiswa | kemkes sp | Dapodik PAUD | 1 |
| 1321 | SP000311 | Beasiswa Anak berprestasi | kemkes sp | Dapodik PAUD | 1 |
| 1322 | SP000312 | Beasiswa Anak miskin/kemiskinan | kemkes sp | Dapodik PAUD | 1 |
| 1323 | SP000313 | Beasiswa Pendidikan | kemkes sp | Dapodik PAUD | 1 |
| 1324 | SP000314 | Beasiswa Unggulan | kemkes sp | Dapodik PAUD | 1 |
| 1325 | SP000315 | Keterangan Beasiswa | kemkes sp | Dapodik PAUD | 1 |
| 1326 | SP000316 | Periode Beasiswa | kemkes sp | Dapodik PAUD | 1 |
| 1327 | SP000328 | Asuransi Kesejahteraan | kemkes sp | Dapodik PAUD | 1 |
| 1328 | SP000329 | Dana Pensiun | kemkes sp | Dapodik PAUD | 1 |
| 1329 | SP000330 | Jamkesmas | kemkes sp | Dapodik PAUD | 1 |
| 1330 | SP000331 | Jamsostek | kemkes sp | Dapodik PAUD | 1 |
| 1331 | SP000332 | BPJS | kemkes sp | Dapodik PAUD | 1 |
| 1332 | SP000333 | Kartu Keluarga Sejahtera | kemkes sp | Dapodik PAUD | 1 |
| 1333 | SP000334 | Kartu Indonesia Sehat | kemkes sp | Dapodik PAUD | 1 |
| 1334 | SP000335 | Otonomi Khusus Papua | kemkes sp | Dapodik PAUD | 1 |
| 1335 | SP000336 | Program Keluarga Harapan | kemkes sp | Dapodik PAUD | 1 |
| 1336 | 276031006 | Details of education | snomed | Dapodik PAUD | 1 |
| 1337 | SP000337 | Kompetensi Keahlian (SMK) | kemkes sp | Dapodik PAUD | 1 |
| 1338 | SP000338 | Jenis Pendaftaran | kemkes sp | Dapodik PAUD | 1 |
| 1339 | SP000339 | Siswa baru | kemkes sp | Dapodik PAUD | 1 |
| 1340 | SP000340 | Siswa Pindahan | kemkes sp | Dapodik PAUD | 1 |
| 1341 | SP000341 | Kembali bersekolah | kemkes sp | Dapodik PAUD | 1 |
| 1342 | 224293004 | Education received in the past | snomed | Dapodik PAUD | 1 |
| 1343 | SP000342 | Jenis Lembaga Pendidikan | kemkes sp | Dapodik PAUD | 1 |
| 1344 | SP000343 | Formal | kemkes sp | Dapodik PAUD | 1 |
| 1345 | SP000344 | Informal | kemkes sp | Dapodik PAUD | 1 |
| 1346 | SP000345 | Tanggal masuk sekolah | kemkes sp | Dapodik PAUD | 1 |
| 1347 | SP000346 | Rombongan Belajar | kemkes sp | Dapodik PAUD | 1 |
| 1348 | SP000347 | No Peserta Ujian Nasional | kemkes sp | Dapodik PAUD | 1 |
| 1349 | SP000348 | No Seri Ijazah | kemkes sp | Dapodik PAUD | 1 |
| 1350 | SP000349 | No SKHUN/SHUN | kemkes sp | Dapodik PAUD | 1 |
| 1351 | SP000350 | Alasan utama keluar sekolah | kemkes sp | Dapodik PAUD | 1 |
| 1352 | SP000351 | Mutasi | kemkes sp | Dapodik PAUD | 1 |
| 1353 | 228137002 | Excluded from school permanently |  | Dapodik PAUD | 1 |
| 1354 | 161131005 | Left school free will |  | Dapodik PAUD | 1 |
| 1355 | SP000352 | Putus sekolah | kemkes sp | Dapodik PAUD | 1 |
| 1356 | 419099009 | Dead |  | Dapodik PAUD, ELSMIL Pasca Persalinan | 2 |
| 1357 | SP000353 | Hilang | kemkes sp | Dapodik PAUD | 1 |
| 1358 | SP000354 | Lulus | kemkes sp | Dapodik PAUD | 1 |
| 1359 | SP000355 | Tanggal keluar sekolah | kemkes sp | Dapodik PAUD | 1 |
| 1360 | SP000356 | Alasan khusus keluar sekolah | kemkes sp | Dapodik PAUD | 1 |
| 1361 | 63764-5 | Hobby [LIBCSP] | loinc | Dapodik PAUD (2x) | 1 |
| 1362 | SP000357 | Cita-cita | kemkes sp | Dapodik PAUD (2x) | 1 |
| 1363 | 129011005 | Shopping | snomed | Dapodik PAUD | 1 |
| 1364 | 10496000 | Camping | snomed | Dapodik PAUD | 1 |
| 1365 | 418060005 | Running | snomed | Dapodik PAUD | 1 |
| 1366 | 88289009 | Soccer | snomed | Dapodik PAUD | 1 |
| 1367 | 26550000 | Tennis | snomed | Dapodik PAUD | 1 |
| 1368 | 84096006 | Surfing | snomed | Dapodik PAUD | 1 |
| 1369 | 1968006 | Jogging | snomed | Dapodik PAUD | 1 |
| 1370 | 48263008 | Eating | snomed | Dapodik PAUD | 1 |
| 1371 | 1137717005 | Fishing | snomed | Dapodik PAUD | 1 |
| 1372 | 50360004 | Reading | snomed | Dapodik PAUD | 1 |
| 1373 | 111055000 | Mountain climbing | snomed | Dapodik PAUD | 1 |
| 1374 | 14468000 | Sports activity | snomed | Dapodik PAUD | 1 |
| 1375 | 129018004 | Traveling | snomed | Dapodik PAUD | 1 |
| 1376 | 308047006 | Architect | snomed | Dapodik PAUD | 1 |
| 1377 | 106325008 | Athlete, sportsman/related worker | snomed | Dapodik PAUD | 1 |
| 1378 | 75271001 | Professional midwife | snomed | Dapodik PAUD | 1 |
| 1379 | 158965000 | Medical practitioner | snomed | Dapodik PAUD, SIPTM | 2 |
| 1380 | 265945005 | Performer (entertainment) | snomed | Dapodik PAUD | 1 |
| 1381 | 308207007 | Chef | snomed | Dapodik PAUD | 1 |
| 1382 | 12877000 | Lawyer | snomed | Dapodik PAUD | 1 |
| 1383 | 308004006 | Writer | snomed | Dapodik PAUD | 1 |
| 1384 | 78705009 | Radio and television announcer | snomed | Dapodik PAUD | 1 |
| 1385 | 308040008 | Pilot - aircraft | snomed | Dapodik PAUD | 1 |
| 1386 | 14406004 | Policeman | snomed | Dapodik PAUD, SIPTM, SISMAL Regmal 1 | 3 |
| 1387 | 159062006 | Artist | snomed | Dapodik PAUD | 1 |
| 1388 | 80409005 | Translator | snomed | Dapodik PAUD | 1 |
| 1389 | 29536009 | Journalist | snomed | Dapodik PAUD | 1 |
| 1390 | 373067005 | No | snomed | ePus Tumbang GPPH (10x) | 1 |
| 1391 | SP000363 | Kadang-Kadang | kemkes sp | ePus Tumbang GPPH (10x) | 1 |
| 1392 | 70232002 | Frequent | snomed | ePus Tumbang GPPH (10x) | 1 |
| 1393 | SP000366 | Selalu | kemkes sp | ePus Tumbang GPPH (10x) | 1 |
| 1394 | gp | General Practitioner referral | http://terminology.hl7.org/CodeSystem/admit-source | SITB TB 01 | 1 |
| 1395 | TK000031 | Rujukan Poli | kemkes | SITB TB 01 | 1 |
| 1396 | other | Other | http://terminology.hl7.org/CodeSystem/admit-source | SITB TB 01, SIM RS Narmada INC, SIM RS Goetoeng ANC | 3 |
| 1397 | A18 | Tuberculosis of other organs | icd-10 | SITB TB 01, SITB TB 02 | 2 |
| 1398 | 827034002 | Scar of skin following Bacillus Calmette-Guerin immunization | snomed | SITB TB 01 | 1 |
| 1399 | 2667000 | Absent | snomed | SITB TB 01 | 1 |
| 1400 | 52101004 | Present | snomed | SITB TB 01 | 1 |
| 1401 | 89372-7 | MTB complex DNA and rpoB RIF resistance mutation panel [Presence] | loinc | SITB TB 01, ASIK CKG Dewasa Laki-laki (3x), ASIK CKG Dewasa Perempuan (3x), ASIK CKG Lansia (27 Apr 2026) (3x) | 4 |
| 1402 | 48635004 | Fine needle biopsy | snomed | SITB TB 01 | 1 |
| 1403 | SP000790 | Hasil Pemeriksaan Kontak TBC | kemkes sp | SITB TB 01 | 1 |
| 1404 | 11999007 | Inactive tuberculosis | snomed | SITB TB 01 | 1 |
| 1405 | CP000004 | Bentuk OAT | kemkes clinical-term | SITB TB 01 | 1 |
| 1406 | CP000091 | KDT | kemkes clinical-term | SITB TB 01 | 1 |
| 1407 | CP000092 | Kombipak | kemkes clinical-term | SITB TB 01 | 1 |
| 1408 | CP000093 | Obat Lepas | kemkes clinical-term | SITB TB 01 | 1 |
| 1409 | SP000796 | Jumlah OAT | kemkes sp | SITB TB 01 (2x) | 1 |
| 1410 | 269911007 | Sputum examination | snomed | SITB TB 02 | 1 |
| 1411 | 1362035007 | Number of biological children | snomed | ELSMIL Ibu Hamil | 1 |
| 1412 | SP000065 | Tanggal Lahir Anak Terakhir | kemkes sp | ELSMIL Ibu Hamil | 1 |
| 1413 | 161501007 | H/O: hypertension | snomed | ELSMIL Ibu Hamil, SIPTM (3x) | 2 |
| 1414 | 161445009 | H/O: diabetes mellitus | snomed | ELSMIL Ibu Hamil, SIPTM (3x) | 2 |
| 1415 | 275536003 | H/O: thyroid disorder | snomed | ELSMIL Ibu Hamil | 1 |
| 1416 | 266995000 | H/O: cardiovascular disease | snomed | ELSMIL Ibu Hamil, SIPTM (3x) | 2 |
| 1417 | 161414005 | H/O: tuberculosis | snomed | ELSMIL Ibu Hamil | 1 |
| 1418 | 161527007 | H/O: asthma | snomed | ELSMIL Ibu Hamil, SIPTM (3x) | 2 |
| 1419 | SP000223 | Alasan tidak diperiksa HB | kemkes sp | ELSMIL Ibu Hamil | 1 |
| 1420 | SP000220 | Tidak terdapat sarana pemeriksaan HB | kemkes sp | ELSMIL Ibu Hamil | 1 |
| 1421 | SP000221 | Kesulitan akses menuju Fasilitas Kesehatan | kemkes sp | ELSMIL Ibu Hamil | 1 |
| 1422 | SP000222 | Ibu Hamil tidak mampu melakukan pemeriksaan | kemkes sp | ELSMIL Ibu Hamil | 1 |
| 1423 | 63719-9 | What was the primary source of drinking water at your home [Next-of-kin] | loinc | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan, ELSMIL Baduta | 3 |
| 1424 | LA14183-0 | Bottled water | loinc | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan, ELSMIL Baduta | 3 |
| 1425 | LA14182-2 | Community supply | loinc | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan, ELSMIL Baduta | 3 |
| 1426 | SP000066 | Sumur bor/pompa | kemkes sp | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan, ELSMIL Baduta | 3 |
| 1427 | SP000067 | Sumur terlindungi | kemkes sp | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan, ELSMIL Baduta | 3 |
| 1428 | SP000068 | Sumur tak terlindungi | kemkes sp | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan, ELSMIL Baduta | 3 |
| 1429 | SP000069 | Mata air terlindungi | kemkes sp | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan, ELSMIL Baduta | 3 |
| 1430 | SP000070 | Mata air tak terlindungi | kemkes sp | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan, ELSMIL Baduta | 3 |
| 1431 | 421665008 | River water | snomed | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan, ELSMIL Baduta | 3 |
| 1432 | 420492000 | Lake water | snomed | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan, ELSMIL Baduta | 3 |
| 1433 | 421176006 | Pond water | snomed | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan, ELSMIL Baduta | 3 |
| 1434 | SP000071 | Air hujan | kemkes sp | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan, ELSMIL Baduta | 3 |
| 1435 | SP000093 | Tempat BAB Layak | kemkes sp | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan, ELSMIL Baduta | 3 |
| 1436 | SP000094 | Jamban milik sendiri dengan leher angsa dan tangki septik/IPAL | kemkes sp | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan, ELSMIL Baduta | 3 |
| 1437 | SP000095 | Jamban pada MCK komunal dengan leher angsa dan tangki septik/IPAL | kemkes sp | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan, ELSMIL Baduta | 3 |
| 1438 | SP000096 | Tidak ada tempat BAB layak | kemkes sp | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan, ELSMIL Baduta | 3 |
| 1439 | 398780007 | Contraception education | snomed | ELSMIL Ibu Hamil | 1 |
| 1440 | 423925001 | Family planning observable | snomed | ELSMIL Ibu Hamil | 1 |
| 1441 | 8659-5 | Birth control method - Reported | loinc | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan, ELSMIL Baduta | 3 |
| 1442 | LA6528-9 | Vasectomy/tubal ligation/hysterectomy | loinc | ELSMIL Ibu Hamil | 1 |
| 1443 | 736796006 | Reason for no contraception (observable entity) | snomed | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan | 2 |
| 1444 | 276367008 | Wanted pregnancy (finding) | snomed | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan | 2 |
| 1445 | 440552008 | Contraception need complicated by medical condition | snomed | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan | 2 |
| 1446 | SP000072 | Efek samping kontrasepsi | kemkes sp | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan | 2 |
| 1447 | 724073007 | Declined by caregiver of subject (qualifier value) | snomed | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan | 2 |
| 1448 | SP000074 | Suami jauh | kemkes sp | ELSMIL Ibu Hamil | 1 |
| 1449 | 424670002 | Dissatisfaction with contraception method (finding) | snomed | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan | 2 |
| 1450 | 183945002 | Procedure declined for religious reason (situation) | snomed | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan | 2 |
| 1451 | 423875000 | Deficient knowledge of family planning methods | snomed | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan | 2 |
| 1452 | 422704000 | Difficulty obtaining contraception | snomed | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan | 2 |
| 1453 | SP000073 | Alat Kontrasepsi Mahal | kemkes sp | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan | 2 |
| 1454 | SP000091 | Alat/cara KB tidak tersedia | kemkes sp | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan | 2 |
| 1455 | SP000092 | Belum dapat informasi dari petugas pelayanan KB | kemkes sp | ELSMIL Ibu Hamil | 1 |
| 1456 | 385827001 | Health promotion education | loinc | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan, ELSMIL Baduta | 3 |
| 1457 | 171035004 | Health education given | snomed | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan, ELSMIL Baduta | 3 |
| 1458 | 125676002 | Person | snomed | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan, ELSMIL Baduta | 3 |
| 1459 | 389109008 | Group | snomed | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan, ELSMIL Baduta | 3 |
| 1460 | 182947002 | Administration of prophylactic iron during pregnancy (procedure) | loinc | ELSMIL Ibu Hamil | 1 |
| 1461 | SP000144 | Sudah mengonsumsi tablet tambah darah | kemkes sp | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan | 2 |
| 1462 | 306206005 | Referral to service | snomed | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan, ELSMIL Baduta | 3 |
| 1463 | 385651009 | In progress | snomed | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan, ELSMIL Baduta, SiGizi PMT 2025 BB Tidak Naik - Pantau, SiGizi PMT 2025 BB Kurang - Pantau, SiGizi PMT 2025 Gizi Kurang - Pantau | 6 |
| 1464 | 385658003 | Done | snomed | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan, ELSMIL Baduta, SiGizi PMT 2025 BB Tidak Naik - Pantau, SiGizi PMT 2025 BB Kurang - Pantau, SiGizi PMT 2025 Gizi Kurang - Pantau | 6 |
| 1465 | 385660001 | Not done | snomed | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan, ELSMIL Baduta | 3 |
| 1466 | 405076007 | Social support status | snomed | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan, ELSMIL Baduta | 3 |
| 1467 | LA32661-3 | Applied and waiting to receive | loinc | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan, ELSMIL Baduta | 3 |
| 1468 | LA32660-5 | Received | loinc | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan, ELSMIL Baduta | 3 |
| 1469 | LA32662-1 | Tried but was not able to apply for, or was not eligible | loinc | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan, ELSMIL Baduta | 3 |
| 1470 | LA32663-9 | Did not apply for | loinc | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan, ELSMIL Baduta | 3 |
| 1471 | SP000145 | Bantuan sosial yang sedang dalam proses | kemkes sp | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan, ELSMIL Baduta | 3 |
| 1472 | SP000140 | Program Keluarga Harapan | kemkes sp | ELSMIL Ibu Hamil (2x), ELSMIL Pasca Persalinan (2x), ELSMIL Baduta (2x) | 3 |
| 1473 | SP000141 | Bantu Non Tunai | kemkes sp | ELSMIL Ibu Hamil (2x), ELSMIL Pasca Persalinan (2x), ELSMIL Baduta (2x) | 3 |
| 1474 | SP000142 | Program Indonesia Pintar | kemkes sp | ELSMIL Ibu Hamil (2x), ELSMIL Pasca Persalinan (2x), ELSMIL Baduta (2x) | 3 |
| 1475 | SP000143 | Kartu Indonesia Sehat | kemkes sp | ELSMIL Ibu Hamil (2x), ELSMIL Pasca Persalinan (2x), ELSMIL Baduta (2x) | 3 |
| 1476 | SP000146 | Bantuan sosial yang sudah didapatkan | kemkes sp | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan, ELSMIL Baduta | 3 |
| 1477 | SP000219 | Catatan TPK | kemkes sp | ELSMIL Ibu Hamil, ELSMIL Pasca Persalinan, ELSMIL Baduta | 3 |
| 1478 | 93857-1 | Date and time of obstetric delivery | https://loinc.org | ELSMIL Pasca Persalinan | 1 |
| 1479 | 72150-6 | Delivery location | https://loinc.org | ELSMIL Pasca Persalinan | 1 |
| 1480 | SP000147 | Komplikasi pasca persalinan | kemkes sp | ELSMIL Pasca Persalinan | 1 |
| 1481 | 178280004 | Postnatal infection | snomed | ELSMIL Pasca Persalinan | 1 |
| 1482 | SP000227 | Alasan menggunakan KB | kemkes sp | ELSMIL Pasca Persalinan | 1 |
| 1483 | SP000225 | Ingin anak di tunda | kemkes sp | ELSMIL Pasca Persalinan | 1 |
| 1484 | SP000226 | Tidak ingin anak lagi | kemkes sp | ELSMIL Pasca Persalinan | 1 |
| 1485 | SP000151 | Tidak ada petugas pelayanan KB | kemkes sp | ELSMIL Pasca Persalinan | 1 |
| 1486 | SP000148 | Baru melahirkan | kemkes sp | ELSMIL Pasca Persalinan | 1 |
| 1487 | SP000149 | 6 bulan terakhir tidak melakukan hubungan suami istri | kemkes sp | ELSMIL Pasca Persalinan | 1 |
| 1488 | SP000150 | 6 bulan terakhir tidak menstruasi | kemkes sp | ELSMIL Pasca Persalinan | 1 |
| 1489 | 297106006 | Primary infertility | snomed | ELSMIL Pasca Persalinan | 1 |
| 1490 | 289903006 | Menopause present | snomed | ELSMIL Pasca Persalinan | 1 |
| 1491 | SP000229 | Sudah mendapatkan tablet tambah darah | kemkes sp | ELSMIL Pasca Persalinan | 1 |
| 1492 | 103975-9 | Previous delivery date | loinc | ELSMIL Baduta, SIM RS Tripat ANC | 2 |
| 1493 | 243816001 | Contraception status | loinc | ELSMIL Baduta | 1 |
| 1494 | 718701005 | Natural family planning method | snomed | ELSMIL Baduta | 1 |
| 1495 | SP000224 | Cukup atau Lebih Bulan: Umur kehamilan saat lahir >= 37 minggu | kemkes sp | ELSMIL Baduta | 1 |
| 1496 | 10761241000119104 | Preterm labor with preterm delivery (finding) |  | ELSMIL Baduta | 1 |
| 1497 | 89269-5 | Body height Measured --at birth | https://loinc.org | ELSMIL Baduta | 1 |
| 1498 | 8339-4 | Birth weight Measured | https://loinc.org | ELSMIL Baduta (2x), eKohort INC | 2 |
| 1499 | SP000024 | Monitoring ASI Eksklusif Bulan 0 | kemkes sp | ELSMIL Baduta, SiGizi Balita ASI Eksklusif | 2 |
| 1500 | SP000029 | Tidak ASI Eksklusif | kemkes sp | ELSMIL Baduta, SiGizi Balita ASI Eksklusif (7x) | 2 |
| 1501 | 16090371000119103 | Exposure to second hand tobacco smoke | loinc | ELSMIL Baduta (2x) | 1 |
| 1502 | 8306-3 | Body height --lying | https://loinc.org | ELSMIL Baduta | 1 |
| 1503 | SP000152 | Baduta hanya diberikan ASI saja kecuali vitamin dan oralit | kemkes sp | ELSMIL Baduta | 1 |
| 1504 | SP000153 | Baduta>= 6 bulan diberikan ASI | kemkes sp | ELSMIL Baduta | 1 |
| 1505 | IM-Baduta | Imunisasi Program Rutin Baduta | kemkes immunization-reason | ELSMIL Baduta | 1 |
| 1506 | 255599008 | Incomplete | snomed | ELSMIL Baduta | 1 |
| 1507 | 255594003 | Complete | snomed | ELSMIL Baduta | 1 |
| 1508 | SP000154 | Pengisian Kartu Kembang Anak (KKA) | kemkes sp | ELSMIL Baduta | 1 |
| 1509 | 1148955005 | Normal childhood development | snomed | ELSMIL Baduta | 1 |
| 1510 | SP000228 | Kehadiran pada Posyandu/BKB bulan ini | kemkes sp | ELSMIL Baduta | 1 |
| 1511 | 473463000 | Received elementary school education | snomed | SIPTM | 1 |
| 1512 | 603435002 | Educated to junior high school level | snomed | SIPTM | 1 |
| 1513 | 603434003 | Educated to senior high school level | snomed | SIPTM | 1 |
| 1514 | 38861000087100 | Bachelor's degree achieved | snomed | SIPTM | 1 |
| 1515 | 440344006 | Received postgraduate education | snomed | SIPTM | 1 |
| 1516 | 224294005 | No formal education | snomed | SIPTM | 1 |
| 1517 | 38901000087109 | University diploma achieved | snomed | SIPTM | 1 |
| 1518 | SP000244 | Pedagang kecil | kemkes sp | SIPTM | 1 |
| 1519 | 302314004 | Military personnel | snomed | SIPTM, SISMAL Regmal 1 | 2 |
| 1520 | TK000041 | Pegawai/karyawan swasta | kemkes | SIPTM, SISMAL Regmal 1 | 2 |
| 1521 | 73438004 | Unemployed | snomed | SIPTM, SISMAL Regmal 1 | 2 |
| 1522 | 105493001 | Retired, life even | snomed | SIPTM | 1 |
| 1523 | SP000288 | Tenaga Kerja Indonesia | kemkes sp | SIPTM | 1 |
| 1524 | 158891000 | University lecturer | snomed | SIPTM | 1 |
| 1525 | Z00.8 | Other general exemination | icd-10 | SIPTM, ASIK Skrining PTM | 2 |
| 1526 | 396552003 | Abdominal circumference | snomed | SIPTM, ASIK Skrining PTM | 2 |
| 1527 | 21324001 | Refraction of eye, function (observable entity) | snomed | SIPTM (2x) | 1 |
| 1528 | 816120008 | Cataract of right eye | snomed | SIPTM | 1 |
| 1529 | 816119002 | Cataract of left eye | snomed | SIPTM | 1 |
| 1530 | OC000150 | Suspek tuli kongenital | kemkes clinical-term | SIPTM (2x) | 1 |
| 1531 | 18070006 | Impacted cerumen | snomed | SIPTM (2x) | 1 |
| 1532 | 1091181000119108 | Chronic suppurative otitis media of right middle ear | snomed | SIPTM | 1 |
| 1533 | 1088571000119107 | Chronic suppurative otitis media of left middle ear | snomed | SIPTM | 1 |
| 1534 | X099241 | Tes IVA | kemkes examination | SIPTM, ASIK Skrining PTM (2x), ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 4 |
| 1535 | 300558006 | Aceto-white reaction negative | snomed | SIPTM, ASIK Skrining PTM (2x) | 2 |
| 1536 | 300557001 | Aceto-white reaction positive | snomed | SIPTM, ASIK Skrining PTM (2x) | 2 |
| 1537 | 37610005 | Inflammation of cervix | snomed | SIPTM | 1 |
| 1538 | 315266007 | Suspected cervical cancer | snomed | SIPTM, ASIK Skrining PTM (2x) | 2 |
| 1539 | 26782000 | Cryotherapy | snomed | SIPTM | 1 |
| 1540 | 13607009 | Manual examination of breast | snomed | SIPTM, ASIK Skrining PTM (2x) | 2 |
| 1541 | 89164003 | Breast lump | snomed | SIPTM, ASIK Skrining PTM (2x) | 2 |
| 1542 | 134405005 | Suspected breast cancer | snomed | SIPTM, ASIK Skrining PTM (2x) | 2 |
| 1543 | 275526006 | History of cerebrovascular accident | snomed | SIPTM (3x) | 1 |
| 1544 | 266987004 | History of malignant neoplasm | snomed | SIPTM (3x) | 1 |
| 1545 | 414416008 | History of hypercholesterolemia | snomed | SIPTM (3x) | 1 |
| 1546 | 110483000 | Tobacco user | snomed | SIPTM | 1 |
| 1547 | 43994002 | Lack of physical activity | snomed | SIPTM | 1 |
| 1548 | 412744006 | High sugar diet | snomed | SIPTM | 1 |
| 1549 | 440921000124100 | Excessive sodium intake | snomed | SIPTM | 1 |
| 1550 | 846619006 | Excessive intake of fat and oil | snomed | SIPTM | 1 |
| 1551 | SP000650 | Pola Makan Kurang Makan Buah dan Sayur | kemkes sp | SIPTM | 1 |
| 1552 | E11.9 | Non-insulin-dependent diabetes mellitus | icd-10 | SIPTM (3x) | 1 |
| 1553 | J45.9 | Asthma, unspecified |  | SIPTM (3x) | 1 |
| 1554 | E78.0 | Pure hypercholesterolaemia |  | SIPTM (3x) | 1 |
| 1555 | O24.4 | Diabetes mellitus arising in pregnancy |  | SIPTM (3x) | 1 |
| 1556 | E10.9 | Insulin-dependent diabetes mellitus |  | SIPTM (3x) | 1 |
| 1557 | SP000648 | Diabetes Mellitus dengan Tuberkulosis | kemkes sp | SIPTM (3x) | 1 |
| 1558 | I50.9 | Heart failure, unspecified |  | SIPTM (3x) | 1 |
| 1559 | H52.7 | Disorder of refraction, unspecified |  | SIPTM (3x) | 1 |
| 1560 | N18.9 | Chronic kidney disease, unspecified |  | SIPTM (3x) | 1 |
| 1561 | H40.9 | Glaucoma, unspecified |  | SIPTM (3x) | 1 |
| 1562 | I10 | Essential (primary) hypertension |  | SIPTM (3x) | 1 |
| 1563 | E05.9 | Thyrotoxicosis, unspecified |  | SIPTM (3x) | 1 |
| 1564 | N40 | Hyperplasia of prostate |  | SIPTM (3x) | 1 |
| 1565 | E03.9 | Hypothyroidism, unspecified |  | SIPTM (3x) | 1 |
| 1566 | I25.1 | Atherosclerotic heart disease |  | SIPTM (3x) | 1 |
| 1567 | C19 | Malignant neoplasm of rectosigmoid junction |  | SIPTM (3x) | 1 |
| 1568 | C50.9 | Breast, unspecified |  | SIPTM (3x) | 1 |
| 1569 | C53.9 | Cervix uteri, unspecified |  | SIPTM (3x) | 1 |
| 1570 | H26.9 | Cataract, unspecified |  | SIPTM (3x) | 1 |
| 1571 | C95.9 | Leukaemia, unspecified |  | SIPTM (3x) | 1 |
| 1572 | M32.9 | Systemic lupus erythematosus, unspecified |  | SIPTM (3x) | 1 |
| 1573 | H83.3 | Noise effects on inner ear |  | SIPTM (3x) | 1 |
| 1574 | E66.9 | Obesity, unspecified |  | SIPTM (3x) | 1 |
| 1575 | H66.3 | Other chronic suppurative otitis media |  | SIPTM (3x) | 1 |
| 1576 | M81.9 | Osteoporosis, unspecified |  | SIPTM (3x) | 1 |
| 1577 | J44.9 | Chronic obstructive pulmonary disease, unspecified |  | SIPTM (3x) | 1 |
| 1578 | H91.1 | Presbycusis |  | SIPTM (3x) | 1 |
| 1579 | L40.0 | Psoriasis vulgaris |  | SIPTM (3x) | 1 |
| 1580 | M06.9 | Rheumatoid arthritis, unspecified |  | SIPTM (3x) | 1 |
| 1581 | C69.2 | Retina |  | SIPTM (3x) | 1 |
| 1582 | H61.2 | Impacted cerumen |  | SIPTM (3x) | 1 |
| 1583 | I64 | Stroke, not specified as haemorrhage or infarction |  | SIPTM (3x) | 1 |
| 1584 | D56.9 | Thalassaemia, unspecified |  | SIPTM (3x) | 1 |
| 1585 | E07.9 | Disorder of thyroid, unspecified |  | SIPTM (3x) | 1 |
| 1586 | H90.5 | Sensorineural hearing loss, unspecified |  | SIPTM (3x) | 1 |
| 1587 | N87.0 | Mild cervical dysplasia |  | SIPTM (3x) | 1 |
| 1588 | 61310001 | Nutrition education | snomed | SIPTM | 1 |
| 1589 | 304507003 | Exercise education | snomed | SIPTM | 1 |
| 1590 | 94.4 | Other psychotherapy and counselling | icd-9-cm | SIPTM | 1 |
| 1591 | SP000649 | Status CAR saat dirujuk | kemkes sp | SIPTM | 1 |
| 1592 | TK000108 | CAR 3 | kemkes | SIPTM | 1 |
| 1593 | TK000109 | CAR 6 | kemkes | SIPTM | 1 |
| 1594 | TK000110 | CAR 9 | kemkes | SIPTM | 1 |
| 1595 | TK000111 | CAR 12 | kemkes | SIPTM | 1 |
| 1596 | Z72.0 | Tobacco Use | icd-10 | SIPTM | 1 |
| 1597 | 268607006 | Hypertension risk level | snomed | ASIK Skrining PTM | 1 |
| 1598 | 260246004 | Visual acuity finding | snomed | ASIK Skrining PTM | 1 |
| 1599 | 45089002 | Normal visual acuity | snomed | ASIK Skrining PTM | 1 |
| 1600 | 397543001 | Mild visual impairment | snomed | ASIK Skrining PTM | 1 |
| 1601 | 397542006 | Moderate visual impairment | snomed | ASIK Skrining PTM | 1 |
| 1602 | 397541004 | Severe visual impairment | snomed | ASIK Skrining PTM | 1 |
| 1603 | SP000100 | Buta | kemkes sp | ASIK Skrining PTM | 1 |
| 1604 | 247300007 | Finding of ability to hear voice | snomed | ASIK Skrining PTM | 1 |
| 1605 | 300226000 | Normal ability to hear voice | snomed | ASIK Skrining PTM | 1 |
| 1606 | 300227009 | Hearing for voice impaired | snomed | ASIK Skrining PTM | 1 |
| 1607 | OC000151 | Suspek Presbikusis | kemkes clinical-term | ASIK Skrining PTM | 1 |
| 1608 | 38394007 | Chronic purulent otitis media | snomed | ASIK Skrining PTM | 1 |
| 1609 | SP000101 | Suspek Katarak | kemkes sp | ASIK Skrining PTM | 1 |
| 1610 | SP000111 | Hasil Kuesioner PUMA | kemkes sp | ASIK Skrining PTM | 1 |
| 1611 | 2569-2 | Lipids [Mass/volume] in Serum | loinc | ASIK Skrining PTM (15x) | 1 |
| 1612 | 271921002 | Electrocardiogram finding | snomed | ASIK Skrining PTM (15x) | 1 |
| 1613 | 164854000 | Electrocardiogram normal | snomed | ASIK Skrining PTM (5x), ASIK CKG Dewasa Laki-laki (2x), ASIK CKG Dewasa Perempuan (2x), ASIK CKG Lansia (27 Apr 2026) (2x) | 4 |
| 1614 | 102594003 | Electrocardiogram abnormal | snomed | ASIK Skrining PTM (5x) | 1 |
| 1615 | 24601-7 | US Breast | loinc | ASIK Skrining PTM (3x), ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 3 |
| 1616 | 367644007 | Simple cyst | snomed | ASIK Skrining PTM | 1 |
| 1617 | 449837001 | Complex cyst of breast | snomed | ASIK Skrining PTM | 1 |
| 1618 | 44550-2 | Human papillomavirus DNA [Presence] in Cervix by Probe | loinc | ASIK Skrining PTM (3x), ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 3 |
| 1619 | 787724008 | Human papillomavirus deoxyribonucleic acid not detected | snomed | ASIK Skrining PTM | 1 |
| 1620 | SP000106 | HPV DNA Tipe 16/18 | kemkes sp | ASIK Skrining PTM | 1 |
| 1621 | OV000351 | Positif (HPV tipe onkogenik lain) | kemkes clinical-term | ASIK Skrining PTM, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) (2x) | 3 |
| 1622 | 275981009 | Screening for malignant neoplasm of lung | snomed | ASIK Skrining PTM | 1 |
| 1623 | 723505004 | Low risk | snomed | ASIK Skrining PTM (2x) | 1 |
| 1624 | 25594002 | Moderate risk of | snomed | ASIK Skrining PTM (2x) | 1 |
| 1625 | SP000107 | Hasil Kuesioner Kanker Kolorektal | kemkes sp | ASIK Skrining PTM | 1 |
| 1626 | SP000112 | Hasil Kuesioner Kanker Kolorektal dengan Risiko Tinggi | kemkes sp | ASIK Skrining PTM | 1 |
| 1627 | SP000108 | Tidak Curiga Kanker Kolorektal | kemkes sp | ASIK Skrining PTM | 1 |
| 1628 | SP000109 | Curiga Tumor Jinak Kolorektal | kemkes sp | ASIK Skrining PTM | 1 |
| 1629 | SP000110 | Curiga Kanker Kolorektal | kemkes sp | ASIK Skrining PTM | 1 |
| 1630 | 162572001 | Suspected malignancy | snomed | ASIK Skrining PTM | 1 |
| 1631 | SP000114 | Suspek Thalassemia | kemkes sp | ASIK Skrining PTM | 1 |
| 1632 | Z01.8 | Other specified special examinations | icd-10 | ASIK CKG Bayi Baru Lahir (v2), ASIK CKG Balita (v2), ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 5 |
| 1633 | 424144002.0 | Current chronological age | snomed | ASIK CKG Bayi Baru Lahir (v2), ASIK CKG Balita (v2), ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026), SIM RS Panti Nugroho Hipertensi, SIM RS Panti Nugroho Stroke, SIM RS MPH Diabetes Melitus, SIM RS MPH Hipertensi, SIM RS Goetoeng ANC, SIM RS Goetoeng INC, SIM RS Goetoeng PNC, SIM RS Goetoeng BBL | 13 |
| 1634 | 89269-5 | Body height Measured --at birth | loinc | ASIK CKG Bayi Baru Lahir (v2), SiGizi Balita BNBA, SiGizi Balita Vitamin A, SIM RS Tripat BBL (sheet 'INC BBL'), SIM RS Narmada INC, SIM RS Panti Nugroho BBL, SIM RS Ummu Hani BBL, SIM RS MPH BBL, SIM RS Siaga Medika BBL | 9 |
| 1635 | 103228002.0 | Hemoglobin saturation with oxygen | snomed | ASIK CKG Bayi Baru Lahir (v2) (2x) | 1 |
| 1636 | SP000449 | Hasil Pemeriksaan Skrining Penyakit Jantung Bawaan | kemkes sp | ASIK CKG Bayi Baru Lahir (v2) | 1 |
| 1637 | 410519009.0 | At risk | snomed | ASIK CKG Bayi Baru Lahir (v2), ASIK CKG Balita (v2) (3x) | 2 |
| 1638 | 260385009.0 | Negative | snomed | ASIK CKG Bayi Baru Lahir (v2), ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) (7x) | 4 |
| 1639 | 29575-8 | Thyrotropin [Units/volume] in DBS | loinc | ASIK CKG Bayi Baru Lahir (v2), SIM RS MPH BBL | 2 |
| 1640 | POS | Positve | v3-ObservationInterpretation | ASIK CKG Bayi Baru Lahir (v2) (6x) | 1 |
| 1641 | NEG | Negative | v3-ObservationInterpretation | ASIK CKG Bayi Baru Lahir (v2) (6x), ASIK CKG Dewasa Laki-laki (4x), ASIK CKG Dewasa Perempuan (4x), ASIK CKG Lansia (27 Apr 2026) (4x) | 4 |
| 1642 | 32546-4 | Glucose-6-Phosphate dehydrogenase [Enzymatic activity/mass] in Red Blood Cells | loinc | ASIK CKG Bayi Baru Lahir (v2) (2x) | 1 |
| 1643 | 57086-1 | Congenital adrenal hyperplasia newborn screening panel | loinc | ASIK CKG Bayi Baru Lahir (v2) (2x) | 1 |
| 1644 | 25179006.0 | Blood unit collection | snomed | ASIK CKG Bayi Baru Lahir (v2) | 1 |
| 1645 | 400984005.0 | Congenital hypothyroidism screening test | snomed | ASIK CKG Bayi Baru Lahir (v2), SIM RS MPH BBL, SIM RS Siaga Medika BBL | 3 |
| 1646 | 3016-3 | Thyrotropin [Units/volume] in Serum or Plasma | loinc | ASIK CKG Bayi Baru Lahir (v2) | 1 |
| 1647 | 252298007.0 | Glucose-6-phosphate dehydrogenase deficiency spot test | snomed | ASIK CKG Bayi Baru Lahir (v2) | 1 |
| 1648 | 431420002.0 | Screening for congenital adrenal hyperplasia | snomed | ASIK CKG Bayi Baru Lahir (v2) | 1 |
| 1649 | TK000151 | Edukasi skrining hiperbilirubinemia dan kelainan saluran empedu | kemkes | ASIK CKG Bayi Baru Lahir (v2) | 1 |
| 1650 | 267030001.0 | Yellow or jaundiced color | snomed | ASIK CKG Bayi Baru Lahir (v2) (2x) | 1 |
| 1651 | 225592001.0 | Finding of color of stool | snomed | ASIK CKG Bayi Baru Lahir (v2) (2x) | 1 |
| 1652 | 271863002.0 | Stool color abnormal | snomed | ASIK CKG Bayi Baru Lahir (v2) (2x) | 1 |
| 1653 | 167605001.0 | Stool color normal | snomed | ASIK CKG Bayi Baru Lahir (v2) (2x) | 1 |
| 1654 | 1145403003.0 | Macrocephaly | snomed | ASIK CKG Balita (v2) (2x) | 1 |
| 1655 | 840673007.0 | Normal Head | snomed | ASIK CKG Balita (v2) (2x) | 1 |
| 1656 | 1148757008.0 | Microcephaly | snomed | ASIK CKG Balita (v2) (2x) | 1 |
| 1657 | 17621005.0 | Normal | snomed | ASIK CKG Balita (v2) (4x), ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 4 |
| 1658 | 723509005.0 | High risk | snomed | ASIK CKG Balita (v2), ASIK CKG Dewasa Laki-laki (2x), ASIK CKG Dewasa Perempuan (2x), ASIK CKG Lansia (27 Apr 2026) (3x) | 4 |
| 1659 | TK000154 | ≥1 cm, lebih dari 1 KGB, tidak nyeri | kemkes | ASIK CKG Balita (v2) | 1 |
| 1660 | TK000155 | <1 cm, lebih dari 1 KGB, tidak nyeri | kemkes | ASIK CKG Balita (v2) | 1 |
| 1661 | TK000156 | <1 cm, tidak nyeri | kemkes | ASIK CKG Balita (v2) | 1 |
| 1662 | TK000157 | Negatif <10 mm | kemkes | ASIK CKG Balita (v2) | 1 |
| 1663 | TK000158 | Negatif <5 mm pada imunokompromais | kemkes | ASIK CKG Balita (v2) | 1 |
| 1664 | TK000159 | Positif ≥10 mm | kemkes | ASIK CKG Balita (v2) | 1 |
| 1665 | TK000160 | Positif ≥5 mm pada imunokompromais | kemkes | ASIK CKG Balita (v2) | 1 |
| 1666 | TK000162 | Dugaan bukan Tuberkulosis klinis | kemkes | ASIK CKG Balita (v2) | 1 |
| 1667 | TK000161 | Dugaan Tuberkulosis klinis | kemkes | ASIK CKG Balita (v2), ASIK CKG Lansia (27 Apr 2026) | 2 |
| 1668 | TK000163 | Curiga kelainan pupil putih pada anak | kemkes | ASIK CKG Balita (v2) | 1 |
| 1669 | 45089002.0 | Normal vision | snomed | ASIK CKG Balita (v2), ASIK CKG Dewasa Laki-laki (4x), ASIK CKG Dewasa Perempuan (4x), ASIK CKG Lansia (27 Apr 2026) (4x) | 4 |
| 1670 | 7973008.0 | Abnormal vision | snomed | ASIK CKG Balita (v2) | 1 |
| 1671 | 1153593003.0 | Weight for age z-score | snomed | ASIK CKG Balita (v2) | 1 |
| 1672 | 248342006.0 | Underweight | snomed | ASIK CKG Balita (v2), ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 4 |
| 1673 | 43664005.0 | Normal weight | snomed | ASIK CKG Balita (v2), ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) (2x) | 4 |
| 1674 | 1153604005.0 | Body height for age z-score | snomed | ASIK CKG Balita (v2) | 1 |
| 1675 | 1153590000.0 | Length for age z score | snomed | ASIK CKG Balita (v2) | 1 |
| 1676 | 17489000.0 | Body height normal for age | snomed | ASIK CKG Balita (v2) | 1 |
| 1677 | 444000005.0 | Short stature for age | snomed | ASIK CKG Balita (v2) | 1 |
| 1678 | OI000011 | Sangat Pendek | kemkes clinical-term | ASIK CKG Balita (v2), SiGizi Balita BNBA, SiGizi Balita Vitamin A, SiGizi Balita Mendapat PMT 2024, SiGizi Balita MPASI, SiGizi PMT 2025 BB Tidak Naik - Riwayat (2x), SiGizi PMT 2025 BB Kurang - Riwayat (2x), SiGizi PMT 2025 Gizi Kurang - Riwayat (2x) | 8 |
| 1679 | 83077003.0 | Tall for age | snomed | ASIK CKG Balita (v2) | 1 |
| 1680 | 1153600001.0 | Weight for height z-score | snomed | ASIK CKG Balita (v2) | 1 |
| 1681 | 1153598007.0 | Weight for length z score | snomed | ASIK CKG Balita (v2) | 1 |
| 1682 | 248324001.0 | Well nourished | snomed | ASIK CKG Balita (v2) (3x), ASIK CKG Lansia (27 Apr 2026) (3x) | 2 |
| 1683 | 248325000.0 | Undernourished | snomed | ASIK CKG Balita (v2) (3x) | 1 |
| 1684 | 238131007.0 | Overweight | snomed | ASIK CKG Balita (v2) (3x), ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) (2x) | 4 |
| 1685 | 414915002.0 | Obese | snomed | ASIK CKG Balita (v2) (3x), ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 4 |
| 1686 | 1153596006.0 | Body mass index for age z-score | snomed | ASIK CKG Balita (v2) | 1 |
| 1687 | 1153594009.0 | Head circumference for age z-score | snomed | ASIK CKG Balita (v2) | 1 |
| 1688 | SP000450 | Faktor Risiko Tuberkulosis | kemkes sp | ASIK CKG Balita (v2) | 1 |
| 1689 | SP000455 | Ada Risiko | kemkes sp | ASIK CKG Balita (v2) (2x) | 1 |
| 1690 | SP000456 | Tidak Ada Risiko | kemkes sp | ASIK CKG Balita (v2) (2x) | 1 |
| 1691 | SP000451 | Faktor Risiko Talasemia | kemkes sp | ASIK CKG Balita (v2) | 1 |
| 1692 | SP000452 | Keluhan dan Gejala Diabetes Melitus Pada Bayi dan Anak Prasekolah | kemkes sp | ASIK CKG Balita (v2) | 1 |
| 1693 | SP000453 | Tidak Ada Keluhan dan Gejala Diabetes | kemkes sp | ASIK CKG Balita (v2) | 1 |
| 1694 | SP000454 | Ada Keluhan dan Gejala Diabetes | kemkes sp | ASIK CKG Balita (v2) | 1 |
| 1695 | 1290220002.0 | Laboratory worker | snomed | ASIK CKG Balita (v2) (2x), ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, SIM RS MPH Diabetes Melitus, SIM RS Siaga Medika ANC (6x) | 5 |
| 1696 | 119297000.0 | Blood specimen | snomed | ASIK CKG Balita (v2) (2x), ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan | 3 |
| 1697 | 714628002.0 | Prediabetes | snomed | ASIK CKG Balita (v2), ASIK CKG Dewasa Laki-laki (5x), ASIK CKG Dewasa Perempuan (5x), ASIK CKG Lansia (27 Apr 2026) (4x) | 4 |
| 1698 | 302866003.0 | Hypoglycemia | snomed | ASIK CKG Balita (v2), ASIK CKG Dewasa Laki-laki (4x), ASIK CKG Dewasa Perempuan (4x), ASIK CKG Lansia (27 Apr 2026) (3x) | 4 |
| 1699 | 80394007.0 | Hyperglycemia | snomed | ASIK CKG Balita (v2), ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) (2x) | 4 |
| 1700 | 271737000.0 | Anemia | snomed | ASIK CKG Balita (v2), ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 4 |
| 1701 | 860635002.0 | No anemia present | snomed | ASIK CKG Balita (v2), ASIK CKG Lansia (27 Apr 2026) (2x) | 2 |
| 1702 | L | Low | v3-ObservationInterpretation | ASIK CKG Balita (v2) (2x), ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 4 |
| 1703 | 788-0 | Erythrocyte distribution width [Ratio] by Automated count | loinc | ASIK CKG Balita (v2) | 1 |
| 1704 | SP000496 | Skrining Gangguan Pemusatan Perhatian dan Hiperaktivitas (GPPH) | kemkes sp | ASIK CKG Balita (v2) | 1 |
| 1705 | 710075007.0 | Screening for child development | snomed | ASIK CKG Balita (v2) | 1 |
| 1706 | 866042005.0 | Screening for autistic disorder | snomed | ASIK CKG Balita (v2) | 1 |
| 1707 | TK000144 | Rencana menikah 1 tahun ke depan | kemkes | ASIK CKG Dewasa Laki-laki (2x), ASIK CKG Dewasa Perempuan (2x), ASIK CKG Lansia (27 Apr 2026) (2x) | 3 |
| 1708 | vital-signs | Abdominal circumference | snomed | ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 3 |
| 1709 | 248311001.0 | Central obesity | snomed | ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 3 |
| 1710 | OI000040 | Tekanan Darah Optimal | kemkes clinical-term | ASIK CKG Dewasa Laki-laki (3x), ASIK CKG Dewasa Perempuan (3x), ASIK CKG Lansia (27 Apr 2026) (4x) | 3 |
| 1711 | 2004005.0 | Normal blood pressure | snomed | ASIK CKG Dewasa Laki-laki (3x), ASIK CKG Dewasa Perempuan (3x), ASIK CKG Lansia (27 Apr 2026) (6x) | 3 |
| 1712 | OI000041 | Tekanan Darah Normal Tinggi | kemkes clinical-term | ASIK CKG Dewasa Laki-laki (3x), ASIK CKG Dewasa Perempuan (3x), ASIK CKG Lansia (27 Apr 2026) (4x) | 3 |
| 1713 | 827069000.0 | Stage 1 hypertension | snomed | ASIK CKG Dewasa Laki-laki (3x), ASIK CKG Dewasa Perempuan (3x), ASIK CKG Lansia (27 Apr 2026) (4x) | 3 |
| 1714 | 827068008.0 | Stage 1 hypertension | snomed | ASIK CKG Dewasa Laki-laki (3x), ASIK CKG Dewasa Perempuan (3x), ASIK CKG Lansia (27 Apr 2026) (4x) | 3 |
| 1715 | OI000042 | Hipertensi Derajat 3 | kemkes clinical-term | ASIK CKG Dewasa Laki-laki (3x), ASIK CKG Dewasa Perempuan (3x), ASIK CKG Lansia (27 Apr 2026) (4x) | 3 |
| 1716 | 268607006.0 | Hypertension risk level | snomed | ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) (2x) | 3 |
| 1717 | 56218007.0 | Systolic hypertension | snomed | ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) (2x) | 3 |
| 1718 | 73211009.0 | Diabetes mellitus | snomed | ASIK CKG Dewasa Laki-laki (4x), ASIK CKG Dewasa Perempuan (4x), ASIK CKG Lansia (27 Apr 2026) (4x), SIM RS Panti Nugroho ANC, SIM RS MPH ANC, SIM RS Siaga Medika ANC | 6 |
| 1719 | 263654008 | Abnormal | snomed | ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 3 |
| 1720 | 102594003.0 | Electrocardiogram abnormal | snomed | ASIK CKG Dewasa Laki-laki (2x), ASIK CKG Dewasa Perempuan (2x), ASIK CKG Lansia (27 Apr 2026) (2x) | 3 |
| 1721 | 26141007 | ST segment depression | snomed | ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 3 |
| 1722 | 59931005 | Electrocardiogram normal | snomed | ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 3 |
| 1723 | 164873001 | Electrocardiographic left ventricle hypertrophy | snomed | ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 3 |
| 1724 | 164889003 | Electrocardiographic atrial fibrillation | snomed | ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 3 |
| 1725 | 164918000 | Pathological Q wave | snomed | ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 3 |
| 1726 | 76388001 | ST segment elevation | snomed | ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 3 |
| 1727 | H | High | v3-ObservationInterpretation | ASIK CKG Dewasa Laki-laki (3x), ASIK CKG Dewasa Perempuan (3x), ASIK CKG Lansia (27 Apr 2026) (3x) | 3 |
| 1728 | 100898-6 | Lipid panel - Serum or Plasma | loinc | ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 3 |
| 1729 | 370992007.0 | Dyslipidemia | snomed | ASIK CKG Dewasa Laki-laki (2x), ASIK CKG Dewasa Perempuan (2x), ASIK CKG Lansia (27 Apr 2026) (2x) | 3 |
| 1730 | OC000173 | Prediksi Risiko PTM tanpa Pemeriksaan Laboratorium | kemkes clinical-term | ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 3 |
| 1731 | 723505004.0 | Low risk | snomed | ASIK CKG Dewasa Laki-laki (2x), ASIK CKG Dewasa Perempuan (2x), ASIK CKG Lansia (27 Apr 2026) (3x) | 3 |
| 1732 | 25594002.0 | Moderate risk of | snomed | ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 3 |
| 1733 | 2160-0 | Creatinine [Mass/volume] in Serum or Plasma | loinc | ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 3 |
| 1734 | 62238-1 | Glomerular filtration rate/1.73 sq M.predicted [Volume Rate/Area] in Serum, Plasma or Blood by Creatinine-based formula (CKD-EPI) | loinc | ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 3 |
| 1735 | 391483001.0 | Microscopy (acid fast bacilli) | snomed | ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) (2x) | 3 |
| 1736 | 10828004.0 | Positive | snomed | ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) (6x) | 3 |
| 1737 | 258066000.0 | Polymerase chain reaction technique | snomed | ASIK CKG Dewasa Laki-laki (11x), ASIK CKG Dewasa Perempuan (11x), ASIK CKG Lansia (27 Apr 2026) (12x) | 3 |
| 1738 | female | Female | http://hl7.org/fhir/administrative-gender | ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 3 |
| 1739 | male | Male | http://hl7.org/fhir/administrative-gender | ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 3 |
| 1740 | SP000435 | <20 bungkus per tahun | kemkes sp | ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 3 |
| 1741 | SP000436 | 20-30 bungkus per tahun | kemkes sp | ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 3 |
| 1742 | SP000437 | >30 bungkus per tahun | kemkes sp | ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 3 |
| 1743 | 410007005.0 | Rectal examination | snomed | ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 3 |
| 1744 | 248523006.0 | Rectal mass | snomed | ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 3 |
| 1745 | 300870000.0 | No mass present | snomed | ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 3 |
| 1746 | 14563-1 | Hemoglobin.gastrointestinal [Presence] in Stool --1st specimen | loinc | ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 3 |
| 1747 | 167667006.0 | Occult blood not detected in feces | snomed | ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 3 |
| 1748 | 59614000.0 | Occult blood detected in feces | snomed | ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 3 |
| 1749 | 247301006.0 | Finding of ability to hear whisper | snomed | ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 3 |
| 1750 | 275727004.0 | Hearing test normal | snomed | ASIK CKG Dewasa Laki-laki (2x), ASIK CKG Dewasa Perempuan (2x), ASIK CKG Lansia (27 Apr 2026) | 3 |
| 1751 | 300221005.0 | Hearing for whisper impaired | snomed | ASIK CKG Dewasa Laki-laki (2x), ASIK CKG Dewasa Perempuan (2x), ASIK CKG Lansia (27 Apr 2026) | 3 |
| 1752 | 76517002.0 | Otoscopy | snomed | ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 3 |
| 1753 | 400911007.0 | Tumbling E test | snomed | ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 3 |
| 1754 | 397540003.0 | Visual impairment | snomed | ASIK CKG Dewasa Laki-laki (4x), ASIK CKG Dewasa Perempuan (4x), ASIK CKG Lansia (27 Apr 2026) (3x) | 3 |
| 1755 | 252973004.0 | Snellen chart assessment | snomed | ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 3 |
| 1756 | 441841000.0 | Pinhole visual acuity test | loinc | ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 3 |
| 1757 | 39021009.0 | Disorder of refraction | snomed | ASIK CKG Dewasa Laki-laki (2x), ASIK CKG Dewasa Perempuan (2x), ASIK CKG Lansia (27 Apr 2026) (2x) | 3 |
| 1758 | OI000044 | Kelainan organik | kemkes clinical-term | ASIK CKG Dewasa Laki-laki (2x), ASIK CKG Dewasa Perempuan (2x), ASIK CKG Lansia (27 Apr 2026) (2x) | 3 |
| 1759 | 40137007.0 | Pupil light reflex | snomed | ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 3 |
| 1760 | OV000393 | Suspek katarak | kemkes clinical-term | ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 3 |
| 1761 | 371405004.0 | Disorder of eye proper | snomed | ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 3 |
| 1762 | 11214006.0 | Reactive | snomed | ASIK CKG Dewasa Laki-laki (2x), ASIK CKG Dewasa Perempuan (2x), ASIK CKG Lansia (27 Apr 2026) (2x) | 3 |
| 1763 | 131194007.0 | Non-Reactive | snomed | ASIK CKG Dewasa Laki-laki (2x), ASIK CKG Dewasa Perempuan (2x), ASIK CKG Lansia (27 Apr 2026) (2x) | 3 |
| 1764 | 72376-7 | Hepatitis C virus Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | loinc | ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 3 |
| 1765 | 86465-2 | AST to platelet ratio index in Serum and Blood by calculation | loinc | ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 3 |
| 1766 | 30352-9 | Hemoglobin [Mass/volume] in Capillary blood | loinc | ASIK CKG Dewasa Laki-laki, ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 3 |
| 1767 | 13607009.0 | Manual examination of breast | snomed | ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 2 |
| 1768 | 290084006.0 | Breast normal | snomed | ASIK CKG Dewasa Perempuan (2x), ASIK CKG Lansia (27 Apr 2026) (2x), SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 7 |
| 1769 | 89164003.0 | Breast lump | snomed | ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 2 |
| 1770 | 134405005.0 | Suspected breast cancer | snomed | ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 2 |
| 1771 | 367644007.0 | Simple cyst | snomed | ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 2 |
| 1772 | 449837001.0 | Complex cyst of breast | snomed | ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 2 |
| 1773 | 451024007.0 | Inspection of vagina using vaginal speculum | snomed | ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 2 |
| 1774 | 395100000.0 | No evidence of cancer found | snomed | ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 2 |
| 1775 | 315266007.0 | Suspected cervical cancer | snomed | ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 2 |
| 1776 | 300557001.0 | Aceto-white reaction positive | snomed | ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 2 |
| 1777 | 300558006.0 | Aceto-white reaction negative | snomed | ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 2 |
| 1778 | 787724008.0 | Human papillomavirus deoxyribonucleic acid not detected | snomed | ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 2 |
| 1779 | 787723002.0 | Human papillomavirus deoxyribonucleic acid detected | snomed | ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 2 |
| 1780 | 708311006.0 | Deoxyribonucleic acid of Human papillomavirus 52 | snomed | ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 2 |
| 1781 | 708299006.0 | Deoxyribonucleic acid of Human papillomavirus 18 | snomed | ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 2 |
| 1782 | 708298003.0 | Deoxyribonucleic acid of Human papillomavirus 16 | snomed | ASIK CKG Dewasa Perempuan, ASIK CKG Lansia (27 Apr 2026) | 2 |
| 1783 | 8480-6 |  |  | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1784 | 8462-4 | Diastolic blood pressure |  | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1785 | 702817009.0 | Prehypertension | snomed | ASIK CKG Lansia (27 Apr 2026) (2x) | 1 |
| 1786 | 24184005.0 | Blood pressure above reference range | snomed | ASIK CKG Lansia (27 Apr 2026) (2x) | 1 |
| 1787 | 162650008.0 | Examination not done on subject of record | snomed | ASIK CKG Lansia (27 Apr 2026) (3x) | 1 |
| 1788 | 261665006.0 | Unknown | snomed | ASIK CKG Lansia (27 Apr 2026) (11x) | 1 |
| 1789 | 1754-1 | Albumin [Mass/volume] in Urine | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1790 | 2149-3 | Creatine [Mass/volume] in Urine | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1791 | 32294-1 | Albumin/Creatinine [Ratio] in Urine | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1792 | 735623008.0 | Grade A2 albuminuria | v3-ObservationInterpretation | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1793 | 735624002.0 | Grade A3 albuminuria | v3-ObservationInterpretation | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1794 | 424489006.0 | Mantoux test | snomed | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1795 | 268376005.0 | Mantoux: positive | snomed | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1796 | 268375009.0 | Mantoux: negative | snomed | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1797 | 405262001.0 | Point of care testing | snomed | ASIK CKG Lansia (27 Apr 2026) (2x) | 1 |
| 1798 | 77399-4 | Human papilloma virus 16 DNA [Presence] in Cervix by NAA with probe detection | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1799 | 77400-0 | Human papilloma virus 18 DNA [Presence] in Cervix by NAA with probe detection | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1800 | 95534-4 | Human papilloma virus 52 DNA [Presence] in Cervix by NAA with probe detection | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1801 | 164178007.0 | Ear examination normal | snomed | ASIK CKG Lansia (27 Apr 2026) (2x) | 1 |
| 1802 | 699116001.0 | Ear examination abnormal | snomed | ASIK CKG Lansia (27 Apr 2026) (2x) | 1 |
| 1803 | 18070006.0 | Impacted cerumen | kemkes sp | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1804 | 129127001.0 | Infection of ear | kemkes sp | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1805 | SP000828 | Tes Penala | kemkes sp | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1806 | 164728001.0 | Visual testing abnormal | snomed | ASIK CKG Lansia (27 Apr 2026) (2x) | 1 |
| 1807 | 397543001.0 | Mild visual impairment | snomed | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1808 | 397542006.0 | Moderate visual impairment | snomed | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1809 | 397541004.0 | Severe visual impairment | snomed | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1810 | 301950001.0 | Pupil normal | snomed | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1811 | 53524009.0 | Ophthalmoscopy | snomed | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1812 | 164734008.0 | Fundoscopy normal | snomed | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1813 | 164735009.0 | Fundoscopy abnormal | snomed | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1814 | 395197008.0 | Hepatitis C viral load | snomed | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1815 | 82334004.0 | Indeterminate | snomed | ASIK CKG Lansia (27 Apr 2026) (2x) | 1 |
| 1816 | 260413007.0 | None | snomed | ASIK CKG Lansia (27 Apr 2026) (4x) | 1 |
| 1817 | 302814007.0 | Early yaws skin lesion | snomed | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1818 | 106936-8 | Treponema pallidum IgG+IgM Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay |  | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1819 | TK000169 | Benar semua kata | kemkes | ASIK CKG Lansia (27 Apr 2026) (2x) | 1 |
| 1820 | SP000444 | Salah satu/Dua | kemkes sp | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1821 | TK000170 | Tidak dapat mengingat/mengulang kata | kemkes | ASIK CKG Lansia (27 Apr 2026) (2x) | 1 |
| 1822 | 38369006.0 | At increased risk for cognitive impairment | snomed | ASIK CKG Lansia (27 Apr 2026) (2x) | 1 |
| 1823 | TK000173 | Kemungkinan tidak ada gangguan kognitif | kemkes | ASIK CKG Lansia (27 Apr 2026) (2x) | 1 |
| 1824 | 129845004.0 | At risk for malnutrition | snomed | ASIK CKG Lansia (27 Apr 2026) (3x) | 1 |
| 1825 | TK000197 | Kemungkinan depresi | kemkes | ASIK CKG Lansia (27 Apr 2026) (2x) | 1 |
| 1826 | TK000196 | Tidak depresi | kemkes | ASIK CKG Lansia (27 Apr 2026) (2x) | 1 |
| 1827 | 48542-5 | Geriatric depression scale (GDS) panel | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1828 | 35489007.0 | Depression | snomed | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1829 | 48512-8 | Are you basically satisfied with your life [GDS] | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1830 | 48515-1 | Do you often get bored [GDS] | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1831 | 48521-9 | Do you often feel helpless [GDS] | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1832 | 48528-4 | Do you feel pretty worthless the way you are now [GDS] | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1833 | 96762-0 | Barthel index panel | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1834 | OI000048 | Ketergantungan total | kemkes clinical-term | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1835 | OI000047 | Ketergantungan berat | snomed | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1836 | OI000046 | Ketergantungan sedang | snomed | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1837 | OI000045 | Ketergantungan ringan | snomed | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1838 | 371153006.0 | Independent | snomed | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1839 | 96759-6 | Bowels | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1840 | LA31627-5 | Incontinent (or needs to be given enemas) | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1841 | LA31626-7 | Occasional accident | loinc | ASIK CKG Lansia (27 Apr 2026) (2x) | 1 |
| 1842 | LA31625-9 | Continent | loinc | ASIK CKG Lansia (27 Apr 2026) (2x) | 1 |
| 1843 | 96760-4 | Bladder | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1844 | LA31628-3 | Incontinent, or catheterized and unable to manage alone | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1845 | 96767-9 | Grooming | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1846 | LA31643-2 | Needs help with personal care | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1847 | LA31644-0 | Independent face/hair/teeth/shaving (implements provided) | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1848 | 83183-4 | Toilet Use | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1849 | LA12304-4 | Dependent | loinc | ASIK CKG Lansia (27 Apr 2026) (3x) | 1 |
| 1850 | LA31631-7 | Needs some help, but can do something alone | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1851 | LA31632-5 | Independent (on and off, dressing, wiping) | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1852 | 83184-2 | Feeding | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1853 | LA24937-7 | Unable | loinc | ASIK CKG Lansia (27 Apr 2026) (2x) | 1 |
| 1854 | LA31630-9 | Needs help cutting, spreading butter, etc., or requires modified diet | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1855 | LA12302-8 | Independent | loinc | ASIK CKG Lansia (27 Apr 2026) (3x) | 1 |
| 1856 | 83185-9 | Transfer | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1857 | LA31633-3 | Unable, no sitting balance | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1858 | LA31634-1 | Major help (one or two people, physical), can sit | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1859 | LA31635-8 | Minor help (verbal or physical) | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1860 | 83186-7 | Mobility | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1861 | LA31639-0 | Immobile or <50 yards | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1862 | LA31640-8 | Wheelchair independent, including corners, >50 yards | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1863 | LA31641-6 | Walks with help of one person (verbal or physical) >50 yards | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1864 | LA31642-4 | Independent (but may use any aid; for example, stick) >50 yards | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1865 | 83182-6 | Dressing | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1866 | LA31637-4 | Needs help but can do about half unaided | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1867 | LA31638-2 | Independent (including buttons, zips, laces, etc.) | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1868 | 96758-8 | Stairs | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1869 | LA31629-1 | Needs help (verbal, physical, carrying aid) | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1870 | 83181-8 | Bathing | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1871 | LA31636-6 | Independent (or in shower) | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1872 | 72234-8 | Mini-Cog | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1873 | TK000167 | Benar 1 kata | kemkes | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1874 | TK000168 | Benar 2 kata | kemkes | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1875 | 79150-9 | Clock drawing panel [GPCOG] | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1876 | 79106-1 | Please mark in all the numbers to indicate the hours of a clock | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1877 | 79107-9 | Please mark in hands to show 10 minutes past eleven o'clock (11:10) | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1878 | TK000171 | Gambar jam benar/tepat | kemkes | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1879 | TK000172 | Gambar jam salah/tidak tepat | kemkes | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1880 | 72233-0 | Total score [Mini-Cog] | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1881 | 263703002.0 | Changed | snomed | ASIK CKG Lansia (27 Apr 2026) (8x) | 1 |
| 1882 | 260388006.0 | Unchanged | snomed | ASIK CKG Lansia (27 Apr 2026) (9x) | 1 |
| 1883 | 71722-3 | Total score [AD8] | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1884 | N | Normal | http://terminology.hl7. org/CodeSystem/v3-Ob servationInterpretatio n | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1885 | 698464007.0 | At risk of dementia | snomed | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1886 | 66248-6 | Balance test [PhenX] | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1887 | LA18188-5 | Side by side stand | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1888 | LA18189-3 | Semi tandem stand | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1889 | LA18190-1 | Tandem stand | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1890 | 714283000.0 | Short Physical Performance Battery | snomed | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1891 | 66258-5 | For 4-Meter Walk | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1892 | 66264-3 | Safe to stand five times | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1893 | 160697000.0 | Mobilitas fair | snomed | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1894 | 82971005.0 | Limited mobility | snomed | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1895 | 64379006.0 | Decrease in appetite | snomed | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1896 | 79890006.0 | Loss of appetite | snomed | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1897 | 161825005.0 | Appetite normal | snomed | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1898 | TK000180 | Penurunan BB > 3 kg | kemkes | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1899 | TK000181 | Penurunan BB antara 1-3 kg | kemkes | ASIK CKG Lansia (27 Apr 2026) (2x) | 1 |
| 1900 | TK000183 | Harus berbaring di tempat tidur atau menggunakan kursi roda | kemkes | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1901 | TK000184 | Bisa bangun dari tempat tidur atau kursi roda, tetapi tidak bisa keluar rumah | kemkes | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1902 | TK000185 | Bisa bepergian keluar rumah | kemkes | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1903 | TK000186 | Demensia atau depresi berat | kemkes | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1904 | TK000187 | Demensia atau kepikunan ringan | kemkes | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1905 | TK000188 | Tidak ada masalah psikologis | kemkes | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1906 | TK000189 | IMT <19 | kemkes | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1907 | TK000190 | IMT 19 -<21 | kemkes | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1908 | TK000191 | IMT 21 -<23 | kemkes | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1909 | TK000192 | IMT >= 23 | kemkes | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1910 | 443371000124107.0 | Obese class I | snomed | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1911 | 443381000124105.0 | Obese class II | snomed | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1912 | TK000193 | <31 cm | kemkes | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1913 | TK000194 | >= 31 cm | kemkes | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1914 | 8283-4 | Calf - right Maximum circumference | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1915 | 8282-6 | Calf - left Maximum circumference | loinc | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1916 | TK000195 | Mini Nutritional Assessment (MNA) SF | kemkes | ASIK CKG Lansia (27 Apr 2026) (2x) | 1 |
| 1917 | 2492009.0 | Malnutrition | snomed | ASIK CKG Lansia (27 Apr 2026) (2x) | 1 |
| 1918 | 424805008.0 | Exercise above recommended level | snomed | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1919 | 413300002.0 | Exercise below recommended level | snomed | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1920 | SP000831 | Tidak batuk | kemkes sp | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1921 | SP000832 | Ya, lebih dari 2 minggu | kemkes sp | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1922 | SP000833 | Ya, kurang dari 2 minggu | kemkes sp | ASIK CKG Lansia (27 Apr 2026) | 1 |
| 1923 | SP000840 | Persetujuan IC 1 | kemkes sp | Informed Consent | 1 |
| 1924 | SP000841 | Persetujuan IC 2 | kemkes sp | Informed Consent | 1 |
| 1925 | SP000842 | Persetujuan IC 3 | kemkes sp | Informed Consent | 1 |
| 1926 | SP000843 | Persetujuan IC 4 | kemkes sp | Informed Consent | 1 |
| 1927 | SP000844 | Persetujuan IC 5 | kemkes sp | Informed Consent | 1 |
| 1928 | SP000845 | Persetujuan IC 6 | kemkes sp | Informed Consent | 1 |
| 1929 | SP000846 | Persetujuan IC 7 | kemkes sp | Informed Consent | 1 |
| 1930 | SP000847 | Persetujuan IC 8 | kemkes sp | Informed Consent | 1 |
| 1931 | SP000217 | PNS/BUMN/TNI/POLRI | kemkes sp | SIHEPI Rekap 3e | 1 |
| 1932 | SP000218 | Karyawan Swasta | kemkes sp | SIHEPI Rekap 3e | 1 |
| 1933 | 159812002 | Farming/fishing occupation | snomed | SIHEPI Rekap 3e | 1 |
| 1934 | ANC.B6.DE25 | Number of miscarriages and/or abortions | WHO anc-custom-codes | SIHEPI Rekap 3e, SIM RS Tripat PNC, SIM RS Narmada INC (2x), SIM RS Narmada KIA, SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU INC, SIM RS PKU PNC | 10 |
| 1935 | SP000160 | Tanggal Masuk Perawatan, Dukungan, dan Pengobatan (PDP) HIV | kemkes sp | SIHEPI Rekap 3e | 1 |
| 1936 | SP000161 | Tanggal Mendapat atau Memulai ARV | kemkes sp | SIHEPI Rekap 3e | 1 |
| 1937 | SP000162 | Sifilis Ditangani | kemkes sp | SIHEPI Rekap 3e | 1 |
| 1938 | SP000163 | Sifilis Diobati Adekuat | kemkes sp | SIHEPI Rekap 3e | 1 |
| 1939 | SP000164 | Hepatitis B Ditangani atau Dirujuk | kemkes sp | SIHEPI Rekap 3e | 1 |
| 1940 | 72181-1 | HIV results shared with partner [RHEA] | loinc | SIHEPI Rekap 3e | 1 |
| 1941 | SP000165 | Pasangan Diperiksa Sifilis | kemkes sp | SIHEPI Rekap 3e | 1 |
| 1942 | SP000166 | Jumlah Anak Dilahirkan | kemkes sp | SIHEPI Rekap 3e | 1 |
| 1943 | OT000003 | RS ODHA | organization-type | SIHEPI Rekap 3e | 1 |
| 1944 | SP000169 | Pemantauan Anak dari Ibu HIV | kemkes sp | SIHEPI Rekap 3e | 1 |
| 1945 | SP000170 | Tanggal ARV Profilaksis | kemkes sp | SIHEPI Rekap 3e | 1 |
| 1946 | SP000171 | Tanggal Dry Blood Spot Early Infant Diagnosis Pada Usia 6-8 Minggu | kemkes sp | SIHEPI Rekap 3e | 1 |
| 1947 | SP000167 | Hasil Dry Blood Spot Early Infant Diagnosis Pada Usia 6-8 Minggu | kemkes sp | SIHEPI Rekap 3e (2x) | 1 |
| 1948 | SP000172 | Tanggal Konfirmasi Dry Blood Spot Early Infant Diagnosis dalam 12 Bulan | kemkes sp | SIHEPI Rekap 3e | 1 |
| 1949 | SP000168 | Hasil Konfirmasi Dry Blood Spot Early Infant Diagnosis dalam 12 Bulan | kemkes sp | SIHEPI Rekap 3e (2x) | 1 |
| 1950 | SP000173 | Tanggal Deteksi Serologis HIV Usia > 9 Bulan | kemkes sp | SIHEPI Rekap 3e | 1 |
| 1951 | SP000174 | Hasil Deteksi Serologis HIV Usia > 9 Bulan | kemkes sp | SIHEPI Rekap 3e | 1 |
| 1952 | SP000175 | Tanggal Dirawat di Perawatan, Dukungan, dan Pengobatan (PDP) Saat Balita | kemkes sp | SIHEPI Rekap 3e | 1 |
| 1953 | SP000176 | Tanggal Mendapat ARV Profilaksis Saat Balita | kemkes sp | SIHEPI Rekap 3e | 1 |
| 1954 | SP000177 | Pemantauan Anak dari Ibu Sifilis | kemkes sp | SIHEPI Rekap 3e | 1 |
| 1955 | SP000178 | Bayi Ditangani atau Dirujuk | kemkes sp | SIHEPI Rekap 3e | 1 |
| 1956 | SP000179 | Tanggal Screening Sifilis Pada Usia < 2 Tahun | kemkes sp | SIHEPI Rekap 3e | 1 |
| 1957 | SP000180 | Hasil Pemeriksaan Sifilis Pada Usia < 2 Tahun | kemkes sp | SIHEPI Rekap 3e | 1 |
| 1958 | SP000181 | Pemantauan Anak dari Ibu Hepatitis | kemkes sp | SIHEPI Rekap 3e | 1 |
| 1959 | SP000182 | Tanggal atau Jam Imunisasi HB 0 | kemkes sp | SIHEPI Rekap 3e | 1 |
| 1960 | SP000183 | < 24 jam | kemkes sp | SIHEPI Rekap 3e (2x) | 1 |
| 1961 | SP000184 | ≥ 24 jam | kemkes sp | SIHEPI Rekap 3e (2x) | 1 |
| 1962 | SP000185 | Tanggal atau Jam Imunisasi HBIg | kemkes sp | SIHEPI Rekap 3e | 1 |
| 1963 | SP000186 | Tanggal Imunisasi DPT/HB 1 | kemkes sp | SIHEPI Rekap 3e | 1 |
| 1964 | SP000187 | Tanggal Imunisasi DPT/HB 2 | kemkes sp | SIHEPI Rekap 3e | 1 |
| 1965 | SP000188 | Tanggal Imunisasi DPT/HB 3 | kemkes sp | SIHEPI Rekap 3e | 1 |
| 1966 | SP000189 | Tanggal Screening HBsAg Pada Usia 9-12 Bulan | kemkes sp | SIHEPI Rekap 3e | 1 |
| 1967 | SP000190 | Hasil Pemeriksaan HBsAg Pada Usia 9-12 Bulan | kemkes sp | SIHEPI Rekap 3e | 1 |
| 1968 | SP000191 | Tanggal Screening Anti HBs Pada Usia 9 - 12 Bulan | kemkes sp | SIHEPI Rekap 3e | 1 |
| 1969 | SP000192 | Hasil Pemeriksaan Anti HBs Pada Usia 9 - 12 Bulan | kemkes sp | SIHEPI Rekap 3e | 1 |
| 1970 | 121912002 | Hepatitis B virus deoxyribonucleic acid assay | snomed | SIHEPI Rekap 3e | 1 |
| 1971 | 313476009 | Hepatitis B e antigen test | snomed | SIHEPI Rekap 3e | 1 |
| 1972 | 34608000 | Alanine aminotransferase measurement | snomed | SIHEPI Rekap 3e | 1 |
| 1973 | SP000193 | Memenuhi Kriteria Pengobatan Pencegahan Hepatitis B | kemkes sp | SIHEPI Rekap 3e | 1 |
| 1974 | SP000194 | Metode Pemeriksaan Sirosis | kemkes sp | SIHEPI Rekap 3e | 1 |
| 1975 | SP000195 | Status Sirosis | kemkes sp | SIHEPI Rekap 3e | 1 |
| 1976 | SP000196 | Status Pengobatan Pencegahan Hepatitis B | kemkes sp | SIHEPI Rekap 3e | 1 |
| 1977 | SP000197 | Tanggal Pengambilan Obat Pencegahan Hepatitis B | kemkes sp | SIHEPI Rekap 3e (4x) | 1 |
| 1978 | SP000198 | Status Akhir Pengobatan Pencegahan Hepatitis B | kemkes sp | SIHEPI Rekap 3e | 1 |
| 1979 | 85712-8 | Expected delivery location | https://loinc.org | eKohort INC | 1 |
| 1980 | 73.59 | Other manually assisted delivery | icd-9-cm | eKohort INC (2x), SiGizi Ibu Nifas, SIM RS Siaga Medika INC, SIM RS Goetoeng INC (3x) | 4 |
| 1981 | 74.0 | Classical cesarean section | icd-9-cm | eKohort INC (2x) | 1 |
| 1982 | 281050002 | Livebirth | snomed | eKohort INC | 1 |
| 1983 | 289437007 | Finding of fetal heart rate | loinc | eKohort INC | 1 |
| 1984 | ANC.SS.DE41 | Letak Janin USG | snomed | eKohort INC | 1 |
| 1985 | CUSTOM | non intact membrane | snomed | eKohort INC | 1 |
| 1986 | CUSTOM |  |  | eKohort INC (8x) | 1 |
| 1987 | CUSTOM | Faktor risiko eklampsia | CUSTOM | eKohort INC (7x) | 1 |
| 1988 | 385984007 | Growth and development treatments and procedures | snomed | SiGizi Balita BNBA, SiGizi Balita Vitamin A, SiGizi Balita Mendapat PMT 2024, SiGizi Balita Pemantauan PMT 2024, SiGizi Balita ASI Eksklusif, SiGizi Balita MPASI, SiGizi PMT 2025 BB Tidak Naik - Pantau, SiGizi PMT 2025 BB Tidak Naik - Riwayat, SiGizi PMT 2025 BB Tidak Naik - Survey, SiGizi PMT 2025 BB Kurang - Pantau, SiGizi PMT 2025 BB Kurang - Riwayat, SiGizi PMT 2025 BB Kurang - Survey, SiGizi PMT 2025 Gizi Kurang - Pantau, SiGizi PMT 2025 Gizi Kurang - Riwayat, SiGizi PMT 2025 Gizi Kurang - Survey | 15 |
| 1989 | 365910001 | Weight trend finding | snomed | SiGizi Balita BNBA, SiGizi Balita Vitamin A, SiGizi Balita Mendapat PMT 2024, SiGizi Balita Pemantauan PMT 2024, SiGizi PMT 2025 BB Tidak Naik - Pantau (2x), SiGizi PMT 2025 BB Tidak Naik - Riwayat (2x), SiGizi PMT 2025 BB Kurang - Pantau (4x), SiGizi PMT 2025 BB Kurang - Riwayat (2x), SiGizi PMT 2025 Gizi Kurang - Pantau (8x), SiGizi PMT 2025 Gizi Kurang - Riwayat (2x) | 10 |
| 1990 | SP000018 | Baru Pertama Kali Ditimbang | kemkes sp | SiGizi Balita BNBA, SiGizi Balita Vitamin A, SiGizi Balita Mendapat PMT 2024, SiGizi Balita Pemantauan PMT 2024, SiGizi PMT 2025 BB Tidak Naik - Pantau (2x), SiGizi PMT 2025 BB Tidak Naik - Riwayat (2x), SiGizi PMT 2025 BB Kurang - Pantau (4x), SiGizi PMT 2025 BB Kurang - Riwayat (2x), SiGizi PMT 2025 Gizi Kurang - Pantau (8x), SiGizi PMT 2025 Gizi Kurang - Riwayat (2x) | 10 |
| 1991 | 8943002 | Weight gain | snomed | SiGizi Balita BNBA, SiGizi Balita Vitamin A, SiGizi Balita Mendapat PMT 2024, SiGizi Balita Pemantauan PMT 2024, SiGizi PMT 2025 BB Tidak Naik - Pantau (2x), SiGizi PMT 2025 BB Tidak Naik - Riwayat (2x), SiGizi PMT 2025 BB Kurang - Pantau (4x), SiGizi PMT 2025 BB Kurang - Riwayat (2x), SiGizi PMT 2025 Gizi Kurang - Pantau (8x), SiGizi PMT 2025 Gizi Kurang - Riwayat (2x) | 10 |
| 1992 | SP000019 | Tidak Ditimbang Bulan Lalu | kemkes sp | SiGizi Balita BNBA, SiGizi Balita Vitamin A, SiGizi Balita Mendapat PMT 2024, SiGizi Balita Pemantauan PMT 2024, SiGizi PMT 2025 BB Tidak Naik - Pantau (2x), SiGizi PMT 2025 BB Tidak Naik - Riwayat (2x), SiGizi PMT 2025 BB Kurang - Pantau (4x), SiGizi PMT 2025 BB Kurang - Riwayat (2x), SiGizi PMT 2025 Gizi Kurang - Pantau (8x), SiGizi PMT 2025 Gizi Kurang - Riwayat (2x) | 10 |
| 1993 | 36440009 | Failure to gain weight | snomed | SiGizi Balita BNBA, SiGizi Balita Vitamin A, SiGizi Balita Mendapat PMT 2024 (2x), SiGizi Balita Pemantauan PMT 2024, SiGizi PMT 2025 BB Tidak Naik - Pantau (2x), SiGizi PMT 2025 BB Tidak Naik - Riwayat (2x), SiGizi PMT 2025 BB Kurang - Pantau (4x), SiGizi PMT 2025 BB Kurang - Riwayat (2x), SiGizi PMT 2025 Gizi Kurang - Pantau (8x), SiGizi PMT 2025 Gizi Kurang - Riwayat (2x) | 10 |
| 1994 | SP000017 | Outlier | kemkes sp | SiGizi Balita BNBA (3x), SiGizi Balita Vitamin A (3x), SiGizi Balita Mendapat PMT 2024 (3x), SiGizi PMT 2025 BB Tidak Naik - Riwayat (6x), SiGizi PMT 2025 BB Kurang - Riwayat (6x), SiGizi PMT 2025 Gizi Kurang - Riwayat (6x) | 6 |
| 1995 | 17489000 | Body height normal for age | snomed | SiGizi Balita BNBA, SiGizi Balita Vitamin A, SiGizi Balita Mendapat PMT 2024, SiGizi Balita MPASI, SiGizi PMT 2025 BB Tidak Naik - Riwayat (2x), SiGizi PMT 2025 BB Kurang - Riwayat (2x), SiGizi PMT 2025 Gizi Kurang - Riwayat (2x) | 7 |
| 1996 | 444000005 | Short stature for age | snomed | SiGizi Balita BNBA, SiGizi Balita Vitamin A, SiGizi Balita Mendapat PMT 2024, SiGizi Balita MPASI, SiGizi PMT 2025 BB Tidak Naik - Riwayat (2x), SiGizi PMT 2025 BB Kurang - Riwayat (2x), SiGizi PMT 2025 Gizi Kurang - Riwayat (2x) | 7 |
| 1997 | 83077003 | Tall for age | snomed | SiGizi Balita BNBA, SiGizi Balita Vitamin A, SiGizi Balita Mendapat PMT 2024, SiGizi Balita MPASI, SiGizi PMT 2025 BB Tidak Naik - Riwayat (2x), SiGizi PMT 2025 BB Kurang - Riwayat (2x), SiGizi PMT 2025 Gizi Kurang - Riwayat (2x) | 7 |
| 1998 | 92000809 | Retinol Palmitate 200.000 IU Kapsul Lunak | kfa | SiGizi Balita BNBA | 1 |
| 1999 | 93018284 | Retinol Palmitate 200.000 IU Kapsul Lunak (Umum) | kfa | SiGizi Balita BNBA (2x), SiGizi Balita Vitamin A | 2 |
| 2000 | 92000354 | Retinol Palmitate 100.000 IU Kapsul Lunak | kfa | SiGizi Balita BNBA | 1 |
| 2001 | SP000022 | KPSP | kemkes sp | SiGizi Balita BNBA, SiGizi Balita Vitamin A | 2 |
| 2002 | SP000023 | KIA | kemkes sp | SiGizi Balita BNBA, SiGizi Balita Vitamin A | 2 |
| 2003 | SP000510 | Mendapat Makanan Bergizi Gratis (MBG) bulan ini | kemkes sp | SiGizi Balita BNBA | 1 |
| 2004 | SP000036 | Jenis PMT | kemkes sp | SiGizi Balita Mendapat PMT 2024, SiGizi PMT 2025 BB Tidak Naik - Survey, SiGizi PMT 2025 BB Kurang - Survey, SiGizi PMT 2025 Gizi Kurang - Survey | 4 |
| 2005 | FO000001 | MT Lokal | kemkes clinical-term | SiGizi Balita Mendapat PMT 2024 | 1 |
| 2006 | FO000002 | MT Pabrikan | kemkes clinical-term | SiGizi Balita Mendapat PMT 2024 | 1 |
| 2007 | SP000037 | Pemberian MT ke- | kemkes sp | SiGizi Balita Mendapat PMT 2024 | 1 |
| 2008 | SP000038 | Tahun Produksi MT | kemkes sp | SiGizi Balita Mendapat PMT 2024 | 1 |
| 2009 | SP000039 | Jumlah Pemberian MT | kemkes sp | SiGizi Balita Mendapat PMT 2024 | 1 |
| 2010 | SP000040 | Alasan Pemberian MT | kemkes sp | SiGizi Balita Mendapat PMT 2024 | 1 |
| 2011 | SP000041 | Sumber Anggaran PMT | kemkes sp | SiGizi Balita Mendapat PMT 2024, SiGizi PMT 2025 BB Tidak Naik - Pantau, SiGizi PMT 2025 BB Tidak Naik - Riwayat, SiGizi PMT 2025 BB Kurang - Pantau, SiGizi PMT 2025 BB Kurang - Riwayat, SiGizi PMT 2025 Gizi Kurang - Pantau, SiGizi PMT 2025 Gizi Kurang - Riwayat | 7 |
| 2012 | SP000042 | APBD | kemkes sp | SiGizi Balita Mendapat PMT 2024, SiGizi PMT 2025 BB Tidak Naik - Pantau, SiGizi PMT 2025 BB Tidak Naik - Riwayat, SiGizi PMT 2025 BB Kurang - Pantau, SiGizi PMT 2025 BB Kurang - Riwayat, SiGizi PMT 2025 Gizi Kurang - Pantau, SiGizi PMT 2025 Gizi Kurang - Riwayat | 7 |
| 2013 | SP000159 | Mitra | kemkes sp | SiGizi Balita Mendapat PMT 2024, SiGizi PMT 2025 BB Tidak Naik - Pantau, SiGizi PMT 2025 BB Tidak Naik - Riwayat, SiGizi PMT 2025 BB Kurang - Pantau, SiGizi PMT 2025 BB Kurang - Riwayat, SiGizi PMT 2025 Gizi Kurang - Pantau, SiGizi PMT 2025 Gizi Kurang - Riwayat | 7 |
| 2014 | SP000158 | DAK (Dana Alokasi Khusus) | kemkes sp | SiGizi Balita Mendapat PMT 2024, SiGizi PMT 2025 BB Tidak Naik - Pantau, SiGizi PMT 2025 BB Tidak Naik - Riwayat, SiGizi PMT 2025 BB Kurang - Pantau, SiGizi PMT 2025 BB Kurang - Riwayat, SiGizi PMT 2025 Gizi Kurang - Pantau, SiGizi PMT 2025 Gizi Kurang - Riwayat | 7 |
| 2015 | SP000043 | Pemantauan PMT ke- | kemkes sp | SiGizi Balita Pemantauan PMT 2024 | 1 |
| 2016 | SP000044 | Tanggal Pemantauan PMT Awal | kemkes sp | SiGizi Balita Pemantauan PMT 2024 | 1 |
| 2017 | SP000045 | Tanggal Pemantauan PMT Akhir | kemkes sp | SiGizi Balita Pemantauan PMT 2024 | 1 |
| 2018 | SP000030 | Belum Diukur | kemkes sp | SiGizi Balita ASI Eksklusif (7x) | 1 |
| 2019 | SP000031 | Tidak Direcall | kemkes sp | SiGizi Balita ASI Eksklusif (7x) | 1 |
| 2020 | SP000025 | Monitoring ASI Eksklusif Bulan 1 | kemkes sp | SiGizi Balita ASI Eksklusif | 1 |
| 2021 | SP000026 | Monitoring ASI Eksklusif Bulan 2 | kemkes sp | SiGizi Balita ASI Eksklusif | 1 |
| 2022 | SP000027 | Monitoring ASI Eksklusif Bulan 3 | kemkes sp | SiGizi Balita ASI Eksklusif | 1 |
| 2023 | SP000028 | Monitoring ASI Eksklusif Bulan 4 | kemkes sp | SiGizi Balita ASI Eksklusif | 1 |
| 2024 | SP000032 | Monitoring ASI Eksklusif Bulan 5 | kemkes sp | SiGizi Balita ASI Eksklusif | 1 |
| 2025 | SP000033 | Monitoring ASI Eksklusif Bulan 6 | kemkes sp | SiGizi Balita ASI Eksklusif | 1 |
| 2026 | OI000007 | Berat Badan Sangat Kurang |  | SiGizi Balita MPASI | 1 |
| 2027 | SP000034 | Jenis MPASI | kemkes sp | SiGizi Balita MPASI | 1 |
| 2028 | 23182003 | Cereal | snomed | SiGizi Balita MPASI | 1 |
| 2029 | 13577000 | Nut | snomed | SiGizi Balita MPASI | 1 |
| 2030 | QRI000007 | Susu dan produk olahannya | kemkes clinical-term | SiGizi Balita MPASI | 1 |
| 2031 | QRI000008 | Daging dan/atau ikan | kemkes clinical-term | SiGizi Balita MPASI | 1 |
| 2032 | 102263004 | Eggs | snomed | SiGizi Balita MPASI | 1 |
| 2033 | QRI000010 | Buah dan sayur sumber vitamin A | kemkes clinical-term | SiGizi Balita MPASI | 1 |
| 2034 | QRI000011 | Buah dan sayur lainnya | kemkes clinical-term | SiGizi Balita MPASI | 1 |
| 2035 | SP000035 | Kualitas MPASI | kemkes sp | SiGizi Balita MPASI | 1 |
| 2036 | SP000491 | Mitra Pemberi MT | kemkes sp | SiGizi PMT 2025 BB Tidak Naik - Pantau, SiGizi PMT 2025 BB Tidak Naik - Riwayat, SiGizi PMT 2025 BB Kurang - Pantau, SiGizi PMT 2025 BB Kurang - Riwayat, SiGizi PMT 2025 Gizi Kurang - Pantau, SiGizi PMT 2025 Gizi Kurang - Riwayat | 6 |
| 2037 | SP000483 | Benih Baik | kemkes sp | SiGizi PMT 2025 BB Tidak Naik - Pantau, SiGizi PMT 2025 BB Tidak Naik - Riwayat, SiGizi PMT 2025 BB Kurang - Pantau, SiGizi PMT 2025 BB Kurang - Riwayat, SiGizi PMT 2025 Gizi Kurang - Pantau, SiGizi PMT 2025 Gizi Kurang - Riwayat | 6 |
| 2038 | SP000484 | Astra | kemkes sp | SiGizi PMT 2025 BB Tidak Naik - Pantau, SiGizi PMT 2025 BB Tidak Naik - Riwayat, SiGizi PMT 2025 BB Kurang - Pantau, SiGizi PMT 2025 BB Kurang - Riwayat, SiGizi PMT 2025 Gizi Kurang - Pantau, SiGizi PMT 2025 Gizi Kurang - Riwayat | 6 |
| 2039 | SP000485 | Kadin | kemkes sp | SiGizi PMT 2025 BB Tidak Naik - Pantau, SiGizi PMT 2025 BB Tidak Naik - Riwayat, SiGizi PMT 2025 BB Kurang - Pantau, SiGizi PMT 2025 BB Kurang - Riwayat, SiGizi PMT 2025 Gizi Kurang - Pantau, SiGizi PMT 2025 Gizi Kurang - Riwayat | 6 |
| 2040 | SP000486 | APINDO | kemkes sp | SiGizi PMT 2025 BB Tidak Naik - Pantau, SiGizi PMT 2025 BB Tidak Naik - Riwayat, SiGizi PMT 2025 BB Kurang - Pantau, SiGizi PMT 2025 BB Kurang - Riwayat, SiGizi PMT 2025 Gizi Kurang - Pantau, SiGizi PMT 2025 Gizi Kurang - Riwayat | 6 |
| 2041 | SP000487 | Seruni | kemkes sp | SiGizi PMT 2025 BB Tidak Naik - Pantau, SiGizi PMT 2025 BB Tidak Naik - Riwayat, SiGizi PMT 2025 BB Kurang - Pantau, SiGizi PMT 2025 BB Kurang - Riwayat, SiGizi PMT 2025 Gizi Kurang - Pantau, SiGizi PMT 2025 Gizi Kurang - Riwayat | 6 |
| 2042 | SP000488 | Mitra Lain | kemkes sp | SiGizi PMT 2025 BB Tidak Naik - Pantau, SiGizi PMT 2025 BB Tidak Naik - Riwayat, SiGizi PMT 2025 BB Kurang - Pantau, SiGizi PMT 2025 BB Kurang - Riwayat, SiGizi PMT 2025 Gizi Kurang - Pantau, SiGizi PMT 2025 Gizi Kurang - Riwayat | 6 |
| 2043 | SP000489 | Status Pemantauan Pemberian Makanan Tambahan | kemkes sp | SiGizi PMT 2025 BB Tidak Naik - Pantau, SiGizi PMT 2025 BB Kurang - Pantau, SiGizi PMT 2025 Gizi Kurang - Pantau | 3 |
| 2044 | SP000490 | Siklus Pemberian Makanan Tambahan | kemkes sp | SiGizi PMT 2025 BB Tidak Naik - Pantau, SiGizi PMT 2025 BB Tidak Naik - Riwayat, SiGizi PMT 2025 BB Kurang - Pantau, SiGizi PMT 2025 BB Kurang - Riwayat, SiGizi PMT 2025 Gizi Kurang - Pantau, SiGizi PMT 2025 Gizi Kurang - Riwayat | 6 |
| 2045 | SP000492 | Jumlah Pemantauan PMT | kemkes sp | SiGizi PMT 2025 BB Tidak Naik - Riwayat, SiGizi PMT 2025 BB Kurang - Riwayat, SiGizi PMT 2025 Gizi Kurang - Riwayat | 3 |
| 2046 | SP000493 | Makanan Lengkap | kemkes sp | SiGizi PMT 2025 BB Tidak Naik - Survey, SiGizi PMT 2025 BB Kurang - Survey, SiGizi PMT 2025 Gizi Kurang - Survey | 3 |
| 2047 | 228070005 | Snack food | snomed | SiGizi PMT 2025 BB Tidak Naik - Survey, SiGizi PMT 2025 BB Kurang - Survey, SiGizi PMT 2025 Gizi Kurang - Survey | 3 |
| 2048 | SP000494 | Makanan Lengkap dan Makanan Kudapan | kemkes sp | SiGizi PMT 2025 BB Tidak Naik - Survey, SiGizi PMT 2025 BB Kurang - Survey, SiGizi PMT 2025 Gizi Kurang - Survey | 3 |
| 2049 | 131 | Posyandu | organization-type | SiGizi PMT 2025 BB Tidak Naik - Survey, SiGizi PMT 2025 BB Kurang - Survey, SiGizi PMT 2025 Gizi Kurang - Survey, SISMAL Regmal 1 | 4 |
| 2050 | SP000495 | Kelas Ibu Hamil | kemkes sp | SiGizi PMT 2025 BB Tidak Naik - Survey, SiGizi PMT 2025 BB Kurang - Survey, SiGizi PMT 2025 Gizi Kurang - Survey | 3 |
| 2051 | QRI000016 | Ya, setiap hari | kemkes clinical-term | SiGizi PMT 2025 BB Tidak Naik - Survey, SiGizi PMT 2025 BB Kurang - Survey, SiGizi PMT 2025 Gizi Kurang - Survey | 3 |
| 2052 | QRI000015 | Ya, tidak setiap hari | kemkes clinical-term | SiGizi PMT 2025 BB Tidak Naik - Survey, SiGizi PMT 2025 BB Kurang - Survey, SiGizi PMT 2025 Gizi Kurang - Survey | 3 |
| 2053 | 248134002 | Aversion to food or drink | snomed | SiGizi PMT 2025 BB Tidak Naik - Survey, SiGizi PMT 2025 BB Kurang - Survey, SiGizi PMT 2025 Gizi Kurang - Survey | 3 |
| 2054 | 79890006 | Loss of appetite | snomed | SiGizi PMT 2025 BB Tidak Naik - Survey, SiGizi PMT 2025 BB Kurang - Survey, SiGizi PMT 2025 Gizi Kurang - Survey | 3 |
| 2055 | 261015003 | Full | snomed | SiGizi PMT 2025 BB Tidak Naik - Survey, SiGizi PMT 2025 BB Kurang - Survey, SiGizi PMT 2025 Gizi Kurang - Survey | 3 |
| 2056 | SP000725 | Abortus | kemkes sp | SiGizi Ibu Nifas | 1 |
| 2057 | 236973005 | Delivery procedure | snomed | SiGizi Ibu Nifas | 1 |
| 2058 | SP000724 | Tanggal Abortus | kemkes sp | SiGizi Ibu Nifas | 1 |
| 2059 | 69.51 | Aspiration curettage of uterus for termination of pregnancy | icd-9-cm | SiGizi Ibu Nifas | 1 |
| 2060 | SP000683 | Tatalaksana Tindakan | kemkes sp | SiGizi Ibu Nifas, SIM RS Panti Nugroho PNC, SIM RS Siaga Medika PNC, SIM RS PKU INC, SIM RS PKU PNC | 5 |
| 2061 | SP000651 | Sumber Pembiayaan Pelayanan Kesehatan | kemkes sp | SiGizi Kohort Ibu | 1 |
| 2062 | SP000652 | Jaminan Kesehatan Nasional (JKN) | kemkes sp | SiGizi Kohort Ibu | 1 |
| 2063 | 73.59 | Other manually assisted delivery |  | SiGizi Kohort Ibu | 1 |
| 2064 | 72.7 | Vacuum extraction |  | SiGizi Kohort Ibu | 1 |
| 2065 | 72 | Low forceps delivery |  | SiGizi Kohort Ibu | 1 |
| 2066 | 74.1 | Classical cesarean section |  | SiGizi Kohort Ibu | 1 |
| 2067 | 161805006 | Past pregnancy history of cesarean section | snomed | SiGizi Kohort Ibu | 1 |
| 2068 | 16356006 | Multiple pregnancy | snomed | SiGizi Kohort Ibu | 1 |
| 2069 | 109894007 | Retained placenta | snomed | SiGizi Kohort Ibu | 1 |
| 2070 | 237361005 | Antepartum fetal death | snomed | SiGizi Kohort Ibu | 1 |
| 2071 | 309453006.0 | Registered midwife | snomed | SIM RS Tripat ANC, SIM RS Tripat BBL (sheet 'INC BBL'), SIM RS Tripat PNC, SIM RS Panti Nugroho ANC, SIM RS Panti Nugroho INC, SIM RS Panti Nugroho PNC, SIM RS Panti Nugroho BBL, SIM RS Panti Nugroho Stroke, SIM RS Ummu Hani ANC (2x), SIM RS Ummu Hani INC (3x), SIM RS Ummu Hani PNC (2x), SIM RS Ummu Hani BBL, SIM RS MPH ANC (2x), SIM RS MPH INC (2x), SIM RS MPH PNC (2x), SIM RS MPH BBL, SIM RS MPH Diabetes Melitus, SIM RS MPH Hipertensi, SIM RS Siaga Medika ANC, SIM RS Siaga Medika INC, SIM RS Siaga Medika PNC, SIM RS PKU INC, SIM RS PKU PNC | 23 |
| 2072 | 309367003.0 | Obstetrician and gynecologist | snomed | SIM RS Tripat ANC (2x), SIM RS Tripat PNC (2x), SIM RS Panti Nugroho ANC, SIM RS Panti Nugroho INC, SIM RS Panti Nugroho PNC, SIM RS Panti Nugroho BBL, SIM RS Ummu Hani ANC (2x), SIM RS Ummu Hani INC (3x), SIM RS Ummu Hani PNC (2x), SIM RS Ummu Hani BBL, SIM RS MPH ANC (2x), SIM RS MPH INC (2x), SIM RS MPH PNC (2x), SIM RS MPH BBL, SIM RS Siaga Medika PNC, SIM RS PKU INC, SIM RS PKU PNC | 17 |
| 2073 | 224535009.0 | Registered nurse | snomed | SIM RS Tripat ANC, SIM RS Tripat BBL (sheet 'INC BBL'), SIM RS Tripat PNC, SIM RS Panti Nugroho ANC, SIM RS Panti Nugroho INC, SIM RS Panti Nugroho PNC, SIM RS Panti Nugroho BBL, SIM RS Panti Nugroho Stroke, SIM RS Ummu Hani ANC (2x), SIM RS Ummu Hani INC (5x), SIM RS Ummu Hani PNC (3x), SIM RS Ummu Hani BBL, SIM RS MPH ANC (3x), SIM RS MPH INC (3x), SIM RS MPH PNC (3x), SIM RS MPH BBL (2x), SIM RS MPH Diabetes Melitus, SIM RS MPH Hipertensi, SIM RS Siaga Medika PNC, SIM RS PKU INC, SIM RS PKU PNC | 21 |
| 2074 | 768827000.0 | Nutritionist | snomed | SIM RS Tripat ANC, SIM RS Tripat BBL (sheet 'INC BBL'), SIM RS Tripat PNC | 3 |
| 2075 | 134435003.0 | Routine antenatal care | snomed | SIM RS Tripat ANC, SIM RS Narmada KIA, SIM RS Ummu Hani ANC, SIM RS MPH ANC, SIM RS Goetoeng ANC | 5 |
| 2076 | 1209182005.0 | Cephalic fetal presentation | snomed | SIM RS Tripat ANC, SIM RS Narmada INC (3x), SIM RS Narmada KIA, SIM RS Panti Nugroho ANC, SIM RS Ummu Hani ANC, SIM RS Ummu Hani INC, SIM RS MPH ANC, SIM RS MPH INC, SIM RS Siaga Medika ANC (2x), SIM RS Siaga Medika INC | 10 |
| 2077 | 6096002.0 | Breech presentation | snomed | SIM RS Tripat ANC, SIM RS Narmada KIA, SIM RS Panti Nugroho ANC, SIM RS Panti Nugroho INC, SIM RS Ummu Hani ANC, SIM RS Ummu Hani INC, SIM RS MPH ANC, SIM RS MPH INC, SIM RS Siaga Medika ANC (2x), SIM RS Siaga Medika INC, SIM RS PKU INC | 11 |
| 2078 | 73161006.0 | Transverse lie | snomed | SIM RS Tripat ANC, SIM RS Ummu Hani ANC, SIM RS MPH ANC | 3 |
| 2079 | 63750008.0 | Oblique lie | snomed | SIM RS Tripat ANC, SIM RS Ummu Hani ANC, SIM RS MPH ANC | 3 |
| 2080 | 71388002.0 | Procedure | snomed | SIM RS Tripat ANC, SIM RS Tripat PNC | 2 |
| 2081 | 82296001.0 | Pediatrician | snomed | SIM RS Tripat BBL (sheet 'INC BBL') (2x), SIM RS Panti Nugroho BBL, SIM RS Ummu Hani BBL | 3 |
| 2082 | Z00.1 | Routine child health examination | icd-10 | SIM RS Tripat BBL (sheet 'INC BBL'), SIM RS Narmada INC, SIM RS Panti Nugroho BBL, SIM RS Ummu Hani BBL, SIM RS MPH BBL, SIM RS Siaga Medika BBL, SIM RS Goetoeng BBL | 7 |
| 2083 | 365475008.0 | Place in family order | snomed | SIM RS Tripat BBL (sheet 'INC BBL'), SIM RS Narmada INC, SIM RS Panti Nugroho BBL, SIM RS Ummu Hani BBL, SIM RS MPH BBL, SIM RS Siaga Medika BBL | 6 |
| 2084 | 8290-9 | Head Occipital-frontal circumference --at birth- by Tape measure | loinc | SIM RS Tripat BBL (sheet 'INC BBL'), SIM RS Panti Nugroho BBL, SIM RS Ummu Hani BBL, SIM RS MPH BBL, SIM RS Siaga Medika BBL | 5 |
| 2085 | 302083008.0 | Finding of Apgar score | snomed | SIM RS Tripat BBL (sheet 'INC BBL') | 1 |
| 2086 | 276654001.0 | Congenital malformation | snomed | SIM RS Tripat BBL (sheet 'INC BBL'), SIM RS Panti Nugroho BBL, SIM RS Ummu Hani BBL, SIM RS MPH BBL, SIM RS Siaga Medika BBL | 5 |
| 2087 | 386412000.0 | Resuscitation of neonate | snomed | SIM RS Tripat BBL (sheet 'INC BBL'), SIM RS Narmada INC, SIM RS Panti Nugroho BBL, SIM RS Ummu Hani BBL | 4 |
| 2088 | 431868002.0 | Initiation of breastfeeding | snomed | SIM RS Tripat BBL (sheet 'INC BBL'), SIM RS Panti Nugroho BBL, SIM RS Ummu Hani INC, SIM RS Ummu Hani BBL, SIM RS MPH INC, SIM RS MPH BBL, SIM RS Siaga Medika INC, SIM RS Siaga Medika BBL, SIM RS PKU INC | 9 |
| 2089 | 36682004.0 | Physiotherapist | snomed | SIM RS Tripat PNC | 1 |
| 2090 | 305956004.0 | Referral by physician | snomed | SIM RS Tripat PNC, SIM RS Panti Nugroho PNC, SIM RS Panti Nugroho Hipertensi, SIM RS Panti Nugroho Stroke, SIM RS MPH Diabetes Melitus, SIM RS MPH Hipertensi, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 8 |
| 2091 | 404684003.0 | Clinical finding | snomed | SIM RS Tripat PNC, SIM RS Narmada INC (3x), SIM RS Narmada KIA (2x), SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 8 |
| 2092 | 116859006.0 | Transfusion of blood product | snomed | SIM RS Tripat PNC, SIM RS Panti Nugroho ANC, SIM RS Panti Nugroho PNC, SIM RS MPH ANC, SIM RS Siaga Medika ANC, SIM RS PKU PNC, SIM RS Goetoeng ANC | 7 |
| 2093 | 417662000.0 | History of clinical finding in subject | snomed | SIM RS Narmada INC | 1 |
| 2094 | 450891000124109.0 | Past pregnancy history of complication of pregnancy, childbirth and/or puerperium | snomed | SIM RS Narmada INC | 1 |
| 2095 | 161809000.0 | Past pregnancy history of postpartum hemorrhage | snomed | SIM RS Narmada INC | 1 |
| 2096 | 161806007.0 | Past pregnancy history of eclampsia | snomed | SIM RS Narmada INC | 1 |
| 2097 | 74964007.0 | Other | snomed | SIM RS Narmada INC, SIM RS Panti Nugroho ANC (4x), SIM RS Panti Nugroho INC (2x), SIM RS Panti Nugroho BBL, SIM RS Ummu Hani INC, SIM RS Ummu Hani BBL, SIM RS MPH ANC (3x), SIM RS MPH INC, SIM RS Siaga Medika ANC (5x), SIM RS Siaga Medika INC, SIM RS PKU INC (2x), SIM RS Goetoeng INC, SIM RS Goetoeng PNC | 13 |
| 2098 | 726001007.0 | Past pregnancy history of live birth | snomed | SIM RS Narmada INC, SIM RS Narmada KIA | 2 |
| 2099 | 3401000175105.0 | Total number of prenatal care visits | snomed | SIM RS Narmada INC, SIM RS Panti Nugroho ANC | 2 |
| 2100 | 243826008.0 | Antenatal care status | snomed | SIM RS Narmada INC | 1 |
| 2101 | 17854005.0 | Regular | snomed | SIM RS Narmada INC | 1 |
| 2102 | 49608001.0 | Irregular | snomed | SIM RS Narmada INC | 1 |
| 2103 | 422587007.0 | Nausea | snomed | SIM RS Narmada INC (2x) | 1 |
| 2104 | 422400008.0 | Vomiting | snomed | SIM RS Narmada INC | 1 |
| 2105 | 289530006.0 | Vaginal bleeding | snomed | SIM RS Narmada INC, SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 6 |
| 2106 | 413320001.0 | Physical health problem | snomed | SIM RS Narmada INC (2x) | 1 |
| 2107 | 161805006.0 | Past pregnancy history of cesarean section | snomed | SIM RS Narmada INC (2x) | 1 |
| 2108 | 10741751000119100 | Anemia in mother complicating childbirth | snomed | SIM RS Narmada INC | 1 |
| 2109 | 199746004.0 | Obstructed labor | snomed | SIM RS Narmada INC, SIM RS Panti Nugroho INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 4 |
| 2110 | 48194001.0 | Pregnancy-induced hypertension | snomed | SIM RS Narmada INC, SIM RS Panti Nugroho ANC, SIM RS Panti Nugroho INC, SIM RS MPH ANC, SIM RS Siaga Medika ANC, SIM RS Siaga Medika INC, SIM RS PKU INC (2x) | 7 |
| 2111 | 38010008.0 | Intrapartum hemorrhage | snomed | SIM RS Narmada INC, SIM RS Panti Nugroho INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 4 |
| 2112 | 40733004.0 | Infectious disease | snomed | SIM RS Narmada INC, SIM RS Panti Nugroho ANC (2x), SIM RS Panti Nugroho INC, SIM RS Ummu Hani ANC, SIM RS MPH ANC (2x), SIM RS Siaga Medika ANC (2x), SIM RS Siaga Medika INC, SIM RS PKU INC | 8 |
| 2113 | 386639001.0 | Termination of pregnancy | snomed | SIM RS Narmada INC, SIM RS Panti Nugroho ANC, SIM RS Panti Nugroho INC, SIM RS Ummu Hani ANC, SIM RS MPH ANC, SIM RS Siaga Medika ANC, SIM RS Siaga Medika INC, SIM RS PKU INC | 8 |
| 2114 | 44223004.0 | Premature rupture of membranes | snomed | SIM RS Narmada INC, SIM RS Panti Nugroho INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 4 |
| 2115 | 38341003.0 | Hypertensive disorder, systemic arterial | snomed | SIM RS Narmada INC, SIM RS Panti Nugroho INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 4 |
| 2116 | 398254007.0 | Pre-eclampsia | snomed | SIM RS Narmada INC, SIM RS Panti Nugroho ANC, SIM RS Panti Nugroho INC, SIM RS Ummu Hani ANC, SIM RS MPH ANC (2x), SIM RS Siaga Medika ANC (2x), SIM RS Siaga Medika INC, SIM RS PKU INC | 8 |
| 2117 | 15938005.0 | Eclampsia | snomed | SIM RS Narmada INC, SIM RS Panti Nugroho ANC, SIM RS Panti Nugroho INC, SIM RS Ummu Hani ANC, SIM RS MPH ANC (2x), SIM RS Siaga Medika ANC (2x), SIM RS Siaga Medika INC, SIM RS PKU INC | 8 |
| 2118 | 9293002.0 | Atony of uterus | snomed | SIM RS Narmada INC, SIM RS Panti Nugroho INC, SIM RS Siaga Medika INC, SIM RS PKU INC (2x) | 4 |
| 2119 | 283380005.0 | Laceration of perineum | snomed | SIM RS Narmada INC, SIM RS Panti Nugroho INC, SIM RS Siaga Medika INC, SIM RS PKU INC (2x) | 4 |
| 2120 | 199745000.0 | Complication occurring during labor and delivery | snomed | SIM RS Narmada INC, SIM RS Panti Nugroho INC, SIM RS Panti Nugroho PNC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika INC, SIM RS PKU INC (2x), SIM RS PKU PNC | 8 |
| 2121 | 59566000.0 | Oligohydramnios | snomed | SIM RS Narmada INC | 1 |
| 2122 | 53443007.0 | Prolonged labor | snomed | SIM RS Narmada INC | 1 |
| 2123 | 1365934004.0 | Failed attempted induction of labor | snomed | SIM RS Narmada INC | 1 |
| 2124 | 130955003.0 | Fetal distress | snomed | SIM RS Narmada INC | 1 |
| 2125 | 199747008.0 | Obstructed labor due to fetal malposition | snomed | SIM RS Narmada INC | 1 |
| 2126 | 199397009.0 | Cephalopelvic disproportion | snomed | SIM RS Narmada INC | 1 |
| 2127 | 371380006.0 | Amniotic fluid leaking | snomed | SIM RS Narmada INC | 1 |
| 2128 | 433068007.0 | Aneurysm of thoracic aorta | snomed | SIM RS Narmada INC | 1 |
| 2129 | 38206000.0 | Exceptionally large at birth | snomed | SIM RS Narmada INC | 1 |
| 2130 | 740597009.0 | Umbilical cord complication during labor and delivery | snomed | SIM RS Narmada INC | 1 |
| 2131 | 420209000.0 | History of contraceptive usage | snomed | SIM RS Narmada INC, SIM RS Narmada KIA | 2 |
| 2132 | 161772002.0 | History of oral contraceptive usage | snomed | SIM RS Narmada INC, SIM RS Narmada KIA | 2 |
| 2133 | 473093002.0 | History of use of depot contraception | snomed | SIM RS Narmada INC, SIM RS Narmada KIA | 2 |
| 2134 | 161773007.0 | History of intrauterine contraceptive device usage | snomed | SIM RS Narmada INC, SIM RS Narmada KIA | 2 |
| 2135 | 267020005.0 | History of tubal ligation | snomed | SIM RS Narmada INC, SIM RS Narmada KIA | 2 |
| 2136 | 473387004.0 | Never used contraception | snomed | SIM RS Narmada INC, SIM RS Narmada KIA | 2 |
| 2137 | SP000644 | Komplikasi KB Sebelumnya | kemkes sp | SIM RS Narmada INC, SIM RS Narmada KIA | 2 |
| 2138 | SP000645 | Alasan Berhenti KB | kemkes sp | SIM RS Narmada INC, SIM RS Narmada KIA | 2 |
| 2139 | 56728002.0 | Chronic cervicitis | snomed | SIM RS Narmada INC, SIM RS Narmada KIA | 2 |
| 2140 | 129103003.0 | Endometriosis | snomed | SIM RS Narmada INC, SIM RS Narmada KIA | 2 |
| 2141 | 6738008.0 | Female infertility | snomed | SIM RS Narmada INC, SIM RS Narmada KIA | 2 |
| 2142 | 371973000.0 | Malignant neoplasm of uterus | snomed | SIM RS Narmada INC, SIM RS Narmada KIA | 2 |
| 2143 | 1156875002.0 | Myoma | snomed | SIM RS Narmada INC, SIM RS Narmada KIA | 2 |
| 2144 | 8098009.0 | Sexually transmitted infectious disease | snomed | SIM RS Narmada INC, SIM RS Narmada KIA | 2 |
| 2145 | 65576009.0 | Polyp of cervix | snomed | SIM RS Narmada INC, SIM RS Narmada KIA | 2 |
| 2146 | 267011001.0 | Gynecological history | snomed | SIM RS Narmada INC, SIM RS Narmada KIA | 2 |
| 2147 | 8392000.0 | Non-smoker | snomed | SIM RS Narmada INC, SIM RS Narmada KIA | 2 |
| 2148 | 43381005.0 | Passive smoker | snomed | SIM RS Narmada INC, SIM RS Narmada KIA | 2 |
| 2149 | 77176002.0 | Smoker | snomed | SIM RS Narmada INC, SIM RS Narmada KIA | 2 |
| 2150 | 105542008.0 | Non - drinker | snomed | SIM RS Narmada INC, SIM RS Narmada KIA | 2 |
| 2151 | 219006.0 | Current drinker | snomed | SIM RS Narmada INC, SIM RS Narmada KIA | 2 |
| 2152 | 248234008.0 | Mentally alert | snomed | SIM RS Narmada INC | 1 |
| 2153 | 300202002.0 | Response to voice | snomed | SIM RS Narmada INC | 1 |
| 2154 | 450847001.0 | Response to pain | snomed | SIM RS Narmada INC | 1 |
| 2155 | 422768004.0 | Unresponsive | snomed | SIM RS Narmada INC | 1 |
| 2156 | 130987000.0 | Acute confusion | snomed | SIM RS Narmada INC | 1 |
| 2157 | 2776000.0 | Delirium | snomed | SIM RS Narmada INC | 1 |
| 2158 | LA6115-5 | 4.0 | loinc | SIM RS Narmada INC | 1 |
| 2159 | 9269-2 | Glasgow coma score total | loinc | SIM RS Narmada INC, SIM RS Narmada KIA | 2 |
| 2160 | ANC.B8.DE36 | Pulse rate | WHO anc-custom-codes | SIM RS Narmada INC, SIM RS Narmada KIA | 2 |
| 2161 | ANC.B8.DE34 | Body temperature | WHO anc-custom-codes | SIM RS Narmada INC, SIM RS Narmada KIA | 2 |
| 2162 | 250554003.0 | Measurement of oxygen saturation at periphery | snomed | SIM RS Narmada INC | 1 |
| 2163 | 284473002.0 | Mid upper arm circumference | snomed | SIM RS Narmada INC, SIM RS Narmada KIA, SIM RS Panti Nugroho PNC, SIM RS Ummu Hani ANC, SIM RS Ummu Hani PNC, SIM RS MPH ANC, SIM RS MPH PNC, SIM RS Siaga Medika ANC, SIM RS Siaga Medika PNC, SIM RS PKU INC, SIM RS PKU PNC | 11 |
| 2164 | 8017000.0 | Face presentation | snomed | SIM RS Narmada INC, SIM RS Narmada KIA, SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 7 |
| 2165 | 249097002.0 | Footling breech presentation | snomed | SIM RS Narmada INC, SIM RS Narmada KIA, SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 7 |
| 2166 | 124736009.0 | Compound presentation | snomed | SIM RS Narmada INC, SIM RS Narmada KIA, SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 7 |
| 2167 | 48782003.0 | Delivery normal | snomed | SIM RS Narmada INC, SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 6 |
| 2168 | 200138003.0 | Vacuum extractor delivery - delivered | snomed | SIM RS Narmada INC, SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 6 |
| 2169 | 200130005.0 | Forceps delivery - delivered | snomed | SIM RS Narmada INC, SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 6 |
| 2170 | 200144004.0 | Deliveries by cesarean | snomed | SIM RS Narmada INC, SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 6 |
| 2171 | 249111004.0 | Engagement of head | snomed | SIM RS Narmada INC (2x), SIM RS Narmada KIA (2x), SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 7 |
| 2172 | 249112006.0 | Head engaged | snomed | SIM RS Narmada INC (2x), SIM RS Narmada KIA (2x), SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 7 |
| 2173 | 62098001.0 | Head not engaged | snomed | SIM RS Narmada INC (2x), SIM RS Narmada KIA (2x), SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 7 |
| 2174 | 249120008.0 | Onset of labor first stage | snomed | SIM RS Narmada INC, SIM RS Narmada KIA, SIM RS PKU INC | 3 |
| 2175 | 364270005.0 | Frequency of uterine contraction | snomed | SIM RS Narmada INC, SIM RS Narmada KIA | 2 |
| 2176 | 398143009.0 | Uterine contraction monitoring | snomed | SIM RS Narmada INC, SIM RS Narmada KIA | 2 |
| 2177 | 289719005.0 | Strong uterine contractions | snomed | SIM RS Narmada INC, SIM RS Narmada KIA | 2 |
| 2178 | 289716003.0 | Moderate uterine contractions | snomed | SIM RS Narmada INC, SIM RS Narmada KIA | 2 |
| 2179 | 289715004.0 | Mild uterine contractions | snomed | SIM RS Narmada INC, SIM RS Narmada KIA | 2 |
| 2180 | 364274001.0 | Duration of uterine contraction | snomed | SIM RS Narmada INC, SIM RS Narmada KIA | 2 |
| 2181 | 289437007.0 | Finding of fetal heart rate | snomed | SIM RS Narmada INC, SIM RS Narmada KIA, SIM RS PKU INC | 3 |
| 2182 | 289441006.0 | Normal fetal heart rate | snomed | SIM RS Narmada INC, SIM RS Narmada KIA, SIM RS PKU INC | 3 |
| 2183 | 312668007.0 | Abnormal fetal heart rate | snomed | SIM RS Narmada INC, SIM RS Narmada KIA, SIM RS PKU INC | 3 |
| 2184 | 248910006.0 | Uterine cervix finding | loinc | SIM RS Narmada INC, SIM RS Narmada KIA | 2 |
| 2185 | 365662002.0 | Finding of amniotic fluid appearance | snomed | SIM RS Narmada INC (2x), SIM RS Narmada KIA, SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika ANC, SIM RS Siaga Medika INC, SIM RS PKU INC | 8 |
| 2186 | 168090003.0 | Amniotic fluid clear | snomed | SIM RS Narmada INC (2x), SIM RS Narmada KIA, SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika ANC, SIM RS Siaga Medika INC, SIM RS PKU INC | 8 |
| 2187 | 408781009.0 | Straw colored amniotic fluid | snomed | SIM RS Narmada INC (2x), SIM RS Narmada KIA, SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika ANC, SIM RS Siaga Medika INC, SIM RS PKU INC | 8 |
| 2188 | 249134008.0 | Bloodstained liquor | snomed | SIM RS Narmada INC (2x), SIM RS Narmada KIA, SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika ANC, SIM RS Siaga Medika INC, SIM RS PKU INC | 8 |
| 2189 | 168092006.0 | Amniotic fluid -meconium stain | snomed | SIM RS Narmada INC (2x), SIM RS Narmada KIA, SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika ANC, SIM RS Siaga Medika INC, SIM RS PKU INC | 8 |
| 2190 | 32750006.0 | Inspection | snomed | SIM RS Narmada INC, SIM RS Narmada KIA | 2 |
| 2191 | 424679001.0 | pH measurement, vaginal fluid | snomed | SIM RS Narmada INC, SIM RS Narmada KIA | 2 |
| 2192 | 387672006.0 | Cardiotochogram | snomed | SIM RS Narmada INC, SIM RS Narmada KIA, SIM RS Goetoeng ANC | 3 |
| 2193 | 251666009.0 | Cardiotochogram finding | snomed | SIM RS Narmada INC, SIM RS Narmada KIA | 2 |
| 2194 | born | Born in hospital | http://terminology.hl7.org/CodeSystem/admit-source | SIM RS Narmada INC | 1 |
| 2195 | 169876006.0 | Birth head circumference | snomed | SIM RS Narmada INC | 1 |
| 2196 | 3941000175104.0 | Birth abdominal circumference | snomed | SIM RS Narmada INC | 1 |
| 2197 | 3931000175105.0 | Birth chest circumference | snomed | SIM RS Narmada INC | 1 |
| 2198 | 9272-6 | 1 minute Apgar Score | loinc | SIM RS Narmada INC, SIM RS Panti Nugroho BBL | 2 |
| 2199 | 57284007.0 | Severe birth asphyxia | snomed | SIM RS Narmada INC (3x), SIM RS Panti Nugroho BBL (3x) | 2 |
| 2200 | 77362009.0 | Mild to moderate birth asphyxia | snomed | SIM RS Narmada INC (3x), SIM RS Panti Nugroho BBL (3x) | 2 |
| 2201 | 275307002.0 | Apgar normal | snomed | SIM RS Narmada INC (3x), SIM RS Panti Nugroho BBL (3x) | 2 |
| 2202 | 32406-1 | 1 minute Apgar Color | loinc | SIM RS Narmada INC | 1 |
| 2203 | LA6722-8 | The baby's whole body is completely bluish-gray or pale | loinc | SIM RS Narmada INC (3x) | 1 |
| 2204 | LA6723-6 | Good color in body with bluish hands or feet | loinc | SIM RS Narmada INC (3x) | 1 |
| 2205 | LA6724-4 | Good color all over | loinc | SIM RS Narmada INC (3x) | 1 |
| 2206 | 32407-9 | 1 minute Apgar Heart rate | loinc | SIM RS Narmada INC | 1 |
| 2207 | LA6716-0 | No heart rate | loinc | SIM RS Narmada INC (3x) | 1 |
| 2208 | LA6717-8 | Fewer than 100 beats per minute | loinc | SIM RS Narmada INC (3x) | 1 |
| 2209 | LA6718-6 | At least 100 beats per minute | loinc | SIM RS Narmada INC (3x) | 1 |
| 2210 | 32409-5 | 1 minute Apgar Reflex irritability | loinc | SIM RS Narmada INC | 1 |
| 2211 | LA6719-4 | No response to airways being suctioned | loinc | SIM RS Narmada INC (3x) | 1 |
| 2212 | LA6720-2 | Grimace during suctioning | loinc | SIM RS Narmada INC (3x) | 1 |
| 2213 | LA6721-0 | Grimace and pulling away, cough, or sneeze during suctioning | loinc | SIM RS Narmada INC (3x) | 1 |
| 2214 | 32408-7 | 1 minute Apgar Muscle tone | loinc | SIM RS Narmada INC | 1 |
| 2215 | LA6713-7 | Limp; no movement | loinc | SIM RS Narmada INC (3x) | 1 |
| 2216 | LA6714-5 | Some flexion of arms and legs | loinc | SIM RS Narmada INC (3x) | 1 |
| 2217 | LA6715-2 | Active motion | loinc | SIM RS Narmada INC (3x) | 1 |
| 2218 | 32410-3 | 1 minute Apgar Respiratory effort | loinc | SIM RS Narmada INC | 1 |
| 2219 | LA6725-1 | Not breathing | loinc | SIM RS Narmada INC (3x) | 1 |
| 2220 | LA6726-9 | Weak cry; may sound like whimpering, slow or irregular breathing | loinc | SIM RS Narmada INC (3x) | 1 |
| 2221 | LA6727-7 | Good, strong cry; normal rate and effort of breathing | loinc | SIM RS Narmada INC (3x) | 1 |
| 2222 | 9274-2 | 5 minute Apgar Score | loinc | SIM RS Narmada INC, SIM RS Panti Nugroho BBL | 2 |
| 2223 | 32411-1 | 5 minute Apgar Color | loinc | SIM RS Narmada INC | 1 |
| 2224 | 32412-9 | 5 minute Apgar Heart rate | loinc | SIM RS Narmada INC | 1 |
| 2225 | 32414-5 | 5 minute Apgar Reflex irritability | loinc | SIM RS Narmada INC | 1 |
| 2226 | 32413-7 | 5 minute Apgar Muscle tone | loinc | SIM RS Narmada INC | 1 |
| 2227 | 32415-2 | 5 minute Apgar Respiratory effort | loinc | SIM RS Narmada INC | 1 |
| 2228 | 9271-8 | 10 minute Apgar Score | loinc | SIM RS Narmada INC, SIM RS Panti Nugroho BBL | 2 |
| 2229 | 32401-2 | 10 minute Apgar Color | loinc | SIM RS Narmada INC | 1 |
| 2230 | 32402-0 | 10 minute Apgar Heart rate | loinc | SIM RS Narmada INC | 1 |
| 2231 | 32404-6 | 10 minute Apgar Reflex irritability | loinc | SIM RS Narmada INC | 1 |
| 2232 | 32403-8 | 10 minute Apgar Muscle tone | loinc | SIM RS Narmada INC | 1 |
| 2233 | 32405-3 | 10 minute Apgar Respiratory effort | loinc | SIM RS Narmada INC | 1 |
| 2234 | 448883004.0 | Injection of vitamin K1 | snomed | SIM RS Narmada INC, SIM RS Panti Nugroho BBL, SIM RS Ummu Hani BBL | 3 |
| 2235 | PC000002 | Pemberian Salep Antibiotik Mata | kemkes clinical-term | SIM RS Narmada INC, SIM RS Panti Nugroho BBL, SIM RS Ummu Hani BBL | 3 |
| 2236 | 30.0 | hepatitis B immune globulin | http://hl7.org/fhir/sid/cvx | SIM RS Narmada INC, SIM RS Panti Nugroho BBL, SIM RS Ummu Hani BBL | 3 |
| 2237 | 249278006.0 | Ability to pass urine | snomed | SIM RS Narmada INC | 1 |
| 2238 | 276397000.0 | Has passed meconium | snomed | SIM RS Narmada INC | 1 |
| 2239 | 1255917009.0 | Maternal perinatal care | snomed | SIM RS Narmada KIA | 1 |
| 2240 | 288203005.0 | Transverse/oblique lie | snomed | SIM RS Narmada KIA, SIM RS Panti Nugroho ANC, SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika ANC, SIM RS Siaga Medika INC, SIM RS PKU INC | 8 |
| 2241 | 243787009 | Antenatal screening | loinc | SIM RS Narmada KIA | 1 |
| 2242 | 34842007.0 | Antepartum hemorrhage | snomed | SIM RS Panti Nugroho ANC, SIM RS Ummu Hani ANC, SIM RS MPH ANC, SIM RS Siaga Medika ANC | 4 |
| 2243 | 91302008.0 | Sepsis | snomed | SIM RS Panti Nugroho ANC, SIM RS Ummu Hani ANC, SIM RS MPH ANC, SIM RS Siaga Medika ANC | 4 |
| 2244 | 92000653.0 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula | http://sys-ids.kemkes.go.id/kf | SIM RS Panti Nugroho ANC, SIM RS Panti Nugroho PNC (2x), SIM RS Ummu Hani PNC (2x), SIM RS MPH ANC, SIM RS Siaga Medika ANC, SIM RS PKU PNC (2x) | 6 |
| 2245 | 93015491.0 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | http://sys-ids.kemkes.go.id/kf | SIM RS Panti Nugroho ANC, SIM RS Panti Nugroho PNC (2x), SIM RS Ummu Hani PNC (2x), SIM RS MPH ANC, SIM RS Siaga Medika ANC, SIM RS PKU PNC (2x) | 6 |
| 2246 | 3457005.0 | Patient referral | snomed | SIM RS Panti Nugroho ANC (3x), SIM RS Ummu Hani PNC, SIM RS MPH ANC (3x), SIM RS MPH PNC, SIM RS Siaga Medika ANC (3x) | 5 |
| 2247 | 12763006.0 | Blood pressure below reference range (finding) | snomed | SIM RS Panti Nugroho ANC | 1 |
| 2248 | 135840009.0 | Blood pressure monitoring | snomed | SIM RS Panti Nugroho ANC, SIM RS Panti Nugroho PNC, SIM RS MPH ANC, SIM RS Siaga Medika ANC, SIM RS PKU PNC | 5 |
| 2249 | 308116003.0 | Antihypertensive therapy | snomed | SIM RS Panti Nugroho ANC, SIM RS Panti Nugroho INC, SIM RS Panti Nugroho PNC, SIM RS MPH ANC, SIM RS Siaga Medika ANC, SIM RS Siaga Medika INC, SIM RS Siaga Medika PNC, SIM RS PKU INC, SIM RS PKU PNC | 9 |
| 2250 | 435591000124104.0 | Nutrition supplement therapy | snomed | SIM RS Panti Nugroho ANC, SIM RS MPH ANC, SIM RS Siaga Medika ANC | 3 |
| 2251 | 414916001.0 | Obesity | snomed | SIM RS Panti Nugroho ANC, SIM RS MPH ANC, SIM RS Siaga Medika ANC | 3 |
| 2252 | 56717001.0 | Tuberculosis | snomed | SIM RS Panti Nugroho ANC, SIM RS MPH ANC, SIM RS Siaga Medika ANC | 3 |
| 2253 | 56265001.0 | Heart disease | snomed | SIM RS Panti Nugroho ANC, SIM RS MPH ANC, SIM RS Siaga Medika ANC | 3 |
| 2254 | 385892002.0 | Mental health screening | snomed | SIM RS Panti Nugroho ANC, SIM RS MPH ANC, SIM RS Siaga Medika ANC | 3 |
| 2255 | 309343006.0 | Physician | snomed | SIM RS Panti Nugroho INC, SIM RS Panti Nugroho PNC, SIM RS Panti Nugroho BBL, SIM RS Ummu Hani ANC (2x), SIM RS Ummu Hani INC (3x), SIM RS Ummu Hani PNC (2x), SIM RS Ummu Hani BBL, SIM RS MPH ANC (2x), SIM RS MPH INC (2x), SIM RS MPH PNC (2x), SIM RS MPH BBL, SIM RS MPH Diabetes Melitus, SIM RS Siaga Medika INC, SIM RS Siaga Medika PNC, SIM RS PKU INC, SIM RS PKU PNC | 16 |
| 2256 | 386337006.0 | Intrapartal care | snomed | SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS Ummu Hani PNC, SIM RS MPH INC, SIM RS MPH PNC, SIM RS Siaga Medika INC, SIM RS PKU INC, SIM RS Goetoeng INC | 8 |
| 2257 | 438949009.0 | Alive | snomed | SIM RS Panti Nugroho INC, SIM RS Panti Nugroho PNC, SIM RS Ummu Hani INC (2x), SIM RS Ummu Hani PNC, SIM RS MPH INC (2x), SIM RS MPH PNC, SIM RS Siaga Medika INC, SIM RS Siaga Medika PNC, SIM RS PKU INC (2x), SIM RS PKU PNC | 10 |
| 2258 | 419099009.0 | Dead | snomed | SIM RS Panti Nugroho INC, SIM RS Panti Nugroho PNC, SIM RS Ummu Hani INC, SIM RS Ummu Hani PNC, SIM RS MPH INC, SIM RS MPH PNC, SIM RS Siaga Medika INC, SIM RS Siaga Medika PNC, SIM RS PKU INC, SIM RS PKU PNC | 10 |
| 2259 | 246435002.0 | Number of fetuses | snomed | SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC | 3 |
| 2260 | 271692001.0 | Presentation of fetus | snomed | SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika ANC, SIM RS Siaga Medika INC, SIM RS PKU INC | 6 |
| 2261 | 398236008.0 | Intrauterine | snomed | SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika ANC, SIM RS Siaga Medika INC, SIM RS PKU INC | 6 |
| 2262 | 298109001.0 | Ectopic | snomed | SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika ANC, SIM RS Siaga Medika INC, SIM RS PKU INC | 6 |
| 2263 | 70028003.0 | Vertex presentation | snomed | SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS PKU INC | 4 |
| 2264 | 249083005.0 | Posterior fontanelle presenting | snomed | SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS PKU INC | 4 |
| 2265 | 8014007.0 | Brow presentation of fetus | snomed | SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 5 |
| 2266 | 289282009.0 | Amniotic membrane finding | snomed | SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 5 |
| 2267 | 249125003.0 | Intact membranes | snomed | SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 5 |
| 2268 | 264362003.0 | Home | snomed | SIM RS Panti Nugroho INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 3 |
| 2269 | 102.0 | Pusat Kesehatan Masyarakat | organization-type | SIM RS Panti Nugroho INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 3 |
| 2270 | 103.0 | Klinik | organization-type | SIM RS Panti Nugroho INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 3 |
| 2271 | 82242000.0 | Children’s hospital | snomed | SIM RS Panti Nugroho INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 3 |
| 2272 | 104.0 | Rumah Sakit | hhttp://terminology.kemkes.go.id/CodeSystem/organization-type | SIM RS Panti Nugroho INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 3 |
| 2273 | 101.0 | Tempat Praktik Mandiri Tenaga Kesehatan | organization-type | SIM RS Panti Nugroho INC, SIM RS PKU INC | 2 |
| 2274 | 394573001.0 | Maternity clinic | snomed | SIM RS Panti Nugroho INC, SIM RS PKU INC | 2 |
| 2275 | SP000398 | Usia Kehamilan Saat Persalinan (hari) | kemkes sp | SIM RS Panti Nugroho INC, SIM RS Panti Nugroho BBL, SIM RS Ummu Hani INC, SIM RS Ummu Hani BBL, SIM RS MPH INC, SIM RS MPH BBL, SIM RS Siaga Medika BBL, SIM RS PKU INC | 8 |
| 2276 | 405195003.0 | Intrapartum maternal status | snomed | SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 5 |
| 2277 | 102514002.0 | Well female adult | snomed | SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 5 |
| 2278 | 39104002.0 | Illness | snomed | SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 5 |
| 2279 | 131148009.0 | Bleeding | snomed | SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 5 |
| 2280 | 386661006.0 | Fever | snomed | SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 5 |
| 2281 | 91175000.0 | Seizure | snomed | SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 5 |
| 2282 | 249215002.0 | Odor of lochia | snomed | SIM RS Panti Nugroho INC, SIM RS Panti Nugroho PNC, SIM RS Ummu Hani INC, SIM RS Ummu Hani PNC, SIM RS MPH INC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU INC, SIM RS PKU PNC | 9 |
| 2283 | 59283008.0 | Maternal death | snomed | SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 5 |
| 2284 | 430701006.0 | Resuscitation using intravenous fluid | snomed | SIM RS Panti Nugroho INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 3 |
| 2285 | SP000156 | Pemberian Obat Uterotonik | kemkes sp | SIM RS Panti Nugroho INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 3 |
| 2286 | 236998006.0 | Bimanual uterine massage | snomed | SIM RS Panti Nugroho INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 3 |
| 2287 | 360362007.0 | Suture of laceration of perineum | snomed | SIM RS Panti Nugroho INC, SIM RS Siaga Medika INC, SIM RS PKU INC, SIM RS Goetoeng ANC | 4 |
| 2288 | 28233006.0 | Manual removal of retained placenta | snomed | SIM RS Panti Nugroho INC, SIM RS Siaga Medika INC, SIM RS PKU INC | 3 |
| 2289 | 409014006.0 | Delivery care management | snomed | SIM RS Panti Nugroho INC, SIM RS Panti Nugroho PNC, SIM RS Ummu Hani INC, SIM RS Ummu Hani PNC, SIM RS MPH INC, SIM RS MPH PNC, SIM RS MPH BBL, SIM RS Siaga Medika BBL, SIM RS PKU INC, SIM RS PKU PNC | 10 |
| 2290 | 409063005.0 | Counselling | snomed | SIM RS Panti Nugroho INC, SIM RS Ummu Hani INC (2x), SIM RS MPH INC (2x), SIM RS Siaga Medika INC, SIM RS PKU INC (2x) | 5 |
| 2291 | 306052007.0 | Referral by midwife | snomed | SIM RS Panti Nugroho PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 3 |
| 2292 | SP000684 | Tatalaksana Obat | kemkes sp | SIM RS Panti Nugroho PNC, SIM RS PKU INC, SIM RS PKU PNC | 3 |
| 2293 | 364297003.0 | Female perineum observable | loinc | SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 5 |
| 2294 | 300885006.0 | Swelling of breast | snomed | SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 5 |
| 2295 | 290070001.0 | Red breast | snomed | SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 5 |
| 2296 | 54302000.0 | Discharge from nipple | snomed | SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 5 |
| 2297 | 53430007.0 | Pain of breast | snomed | SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 5 |
| 2298 | 289700000.0 | Uterine contractions present | snomed | SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 5 |
| 2299 | 249214003.0 | Color of lochia | snomed | SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 5 |
| 2300 | 278072004.0 | Lochia rubra | snomed | SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 5 |
| 2301 | 449828001.0 | Lochia serosa | snomed | SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 5 |
| 2302 | 113291006.0 | Lochia sanguinolenta | snomed | SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 5 |
| 2303 | 449827006.0 | Lochia alba | snomed | SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 5 |
| 2304 | 1145307003.0 | Exclusively breastfed | snomed | SIM RS Panti Nugroho PNC, SIM RS MPH BBL, SIM RS Siaga Medika BBL, SIM RS PKU PNC | 4 |
| 2305 | 252041008.0 | Micturition finding | snomed | SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 5 |
| 2306 | 49650001.0 | Dysuria | snomed | SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 5 |
| 2307 | 249288007.0 | Incomplete emptying of urinary bladder | snomed | SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 5 |
| 2308 | 162116003.0 | Increased frequency of urination | snomed | SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 5 |
| 2309 | 42112009.0 | Enuresis | snomed | SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 5 |
| 2310 | 102834005.0 | Normal micturition | snomed | SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 5 |
| 2311 | 267064002.0 | Retention of urine | snomed | SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 5 |
| 2312 | 300375001.0 | Able to defecate | snomed | SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 5 |
| 2313 | 408988007.0 | Newborn care education | snomed | SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 5 |
| 2314 | 47821001.0 | Postpartum hemorrhage | snomed | SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 5 |
| 2315 | 198188007.0 | Chronic uterine inflammatory disease | snomed | SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 5 |
| 2316 | 111367007.0 | Pelvic abscess | snomed | SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 5 |
| 2317 | 211063003.0 | Infected abrasion of perineum | snomed | SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 5 |
| 2318 | 76902006.0 | Tetanus | snomed | SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 5 |
| 2319 | 266579006.0 | Inflammatory disorder of breast | snomed | SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 5 |
| 2320 | 49746001.0 | Engorgement of breasts | snomed | SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 5 |
| 2321 | 82231009.0 | Inversion of nipple | snomed | SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 5 |
| 2322 | 58703003.0 | Postpartum depression | snomed | SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 5 |
| 2323 | 289084000.0 | Difficulty performing breastfeeding | snomed | SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS MPH PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 5 |
| 2324 | 767224000.0 | Administration of vitamin A | snomed | SIM RS Panti Nugroho PNC, SIM RS PKU PNC | 2 |
| 2325 | 711029005.0 | Counseling about breastfeeding | snomed | SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 4 |
| 2326 | 72531000052105.0 | Counseling for contraception | snomed | SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 4 |
| 2327 | 441041000124100.0 | Counseling about nutrition | snomed | SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 4 |
| 2328 | ED000012 | Edukasi lainnya | kemkes clinical-term | SIM RS Panti Nugroho PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 3 |
| 2329 | 395264002.0 | Product containing tenofovir | snomed | SIM RS Panti Nugroho PNC, SIM RS PKU PNC | 2 |
| 2330 | 432555000.0 | Product containing artesunate | snomed | SIM RS Panti Nugroho PNC, SIM RS PKU PNC | 2 |
| 2331 | 64115004.0 | Product containing amodiaquine | snomed | SIM RS Panti Nugroho PNC, SIM RS PKU PNC | 2 |
| 2332 | 324919005.0 | Product containing precisely quinine sulfate 200 milligram/1 each conventional release oral tablet | snomed | SIM RS Panti Nugroho PNC, SIM RS PKU PNC | 2 |
| 2333 | 29175007.0 | Product containing rifampicin | snomed | SIM RS Panti Nugroho PNC, SIM RS PKU PNC | 2 |
| 2334 | 81335000.0 | Product containing isoniazid | snomed | SIM RS Panti Nugroho PNC, SIM RS PKU PNC | 2 |
| 2335 | 13592004.0 | Product containing pyrazinamide | snomed | SIM RS Panti Nugroho PNC, SIM RS PKU PNC | 2 |
| 2336 | 24450004.0 | Product containing ethambutol | snomed | SIM RS Panti Nugroho PNC, SIM RS PKU PNC | 2 |
| 2337 | 237122005.0 | Lactational amenorrhea | snomed | SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC (2x), SIM RS MPH PNC (2x), SIM RS Siaga Medika PNC (2x), SIM RS PKU PNC | 5 |
| 2338 | 22523008.0 | Vasectomy | snomed | SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC (2x), SIM RS MPH PNC (2x), SIM RS Siaga Medika PNC (2x), SIM RS PKU PNC | 5 |
| 2339 | 77543007.0 | Ligation of fallopian tube | snomed | SIM RS Panti Nugroho PNC, SIM RS Ummu Hani PNC (2x), SIM RS MPH PNC (2x), SIM RS Siaga Medika PNC (2x), SIM RS PKU PNC | 5 |
| 2340 | 135840009.0 | Blood pressure monitoring | kemkes sp | SIM RS Panti Nugroho PNC, SIM RS Siaga Medika PNC, SIM RS PKU PNC | 3 |
| 2341 | 359746009.0 | Patient’s condition stable | snomed | SIM RS Panti Nugroho PNC, SIM RS PKU PNC | 2 |
| 2342 | 162668006.0 | Patient’s condition unstable | snomed | SIM RS Panti Nugroho PNC, SIM RS PKU PNC | 2 |
| 2343 | 268910001.0 | Patient’s condition improved | snomed | SIM RS Panti Nugroho PNC, SIM RS PKU PNC, SIM RS Goetoeng INC, SIM RS Goetoeng BBL | 4 |
| 2344 | 80281008.0 | Cleft lip | snomed | SIM RS Panti Nugroho BBL, SIM RS Ummu Hani BBL | 2 |
| 2345 | 13213009.0 | Congenital heart disease | snomed | SIM RS Panti Nugroho BBL, SIM RS Ummu Hani BBL | 2 |
| 2346 | 35045004.0 | Microtia | snomed | SIM RS Panti Nugroho BBL, SIM RS Ummu Hani BBL | 2 |
| 2347 | 22006008.0 | Hypertelorism | snomed | SIM RS Panti Nugroho BBL, SIM RS Ummu Hani BBL | 2 |
| 2348 | 367506006.0 | Polydactyly | snomed | SIM RS Panti Nugroho BBL, SIM RS Ummu Hani BBL | 2 |
| 2349 | 52781008.0 | Congenital hip dysplasia | snomed | SIM RS Panti Nugroho BBL, SIM RS Ummu Hani BBL | 2 |
| 2350 | 1156475005.0 | Congenital talipes equinovarus | snomed | SIM RS Panti Nugroho BBL, SIM RS Ummu Hani BBL | 2 |
| 2351 | 253098009.0 | Neural tube defect | snomed | SIM RS Panti Nugroho BBL, SIM RS Ummu Hani BBL | 2 |
| 2352 | 118928003.0 | Disorder of abdominal wall | snomed | SIM RS Panti Nugroho BBL, SIM RS Ummu Hani BBL | 2 |
| 2353 | 42030000.0 | Disorder of the genitourinary system | snomed | SIM RS Panti Nugroho BBL, SIM RS Ummu Hani BBL | 2 |
| 2354 | PC000003 | Manajemen Terpadu Bayi Muda (MTBM) | kemkes clinical-term" | SIM RS Panti Nugroho BBL, SIM RS Ummu Hani BBL | 2 |
| 2355 | 8.0 | Hep B, adolescent or pediatric | http://hl7.org/fhir/sid/cvx | SIM RS Panti Nugroho BBL, SIM RS Ummu Hani BBL | 2 |
| 2356 | E14 | Unspecified diabetes mellitus | icd-10 | SIM RS Panti Nugroho Diabetes Melitus, SIM RS MPH Diabetes Melitus, SIM RS Goetoeng Diabetes Melitus | 3 |
| 2357 | 69280009.0 | Specialized physician | snomed | SIM RS Panti Nugroho Hipertensi, SIM RS Panti Nugroho Stroke, SIM RS MPH Diabetes Melitus (2x), SIM RS MPH Hipertensi | 4 |
| 2358 | 59058001.0 | General physician | snomed | SIM RS Panti Nugroho Hipertensi, SIM RS Panti Nugroho Stroke, SIM RS MPH Diabetes Melitus, SIM RS MPH Hipertensi | 4 |
| 2359 | SP000925 | Rujukan dari Klinik | kemkes sp | SIM RS Panti Nugroho Hipertensi, SIM RS Panti Nugroho Stroke, SIM RS MPH Diabetes Melitus, SIM RS MPH Hipertensi | 4 |
| 2360 | I10 | Essential (primary) hypertension | icd-10 | SIM RS Panti Nugroho Hipertensi, SIM RS MPH Hipertensi, SIM RS Goetoeng Hipertensi | 3 |
| 2361 | 8480-6 | Systolic blood pressure | snomed | SIM RS Panti Nugroho Hipertensi, SIM RS MPH Diabetes Melitus, SIM RS MPH Hipertensi, SIM RS Goetoeng Hipertensi | 4 |
| 2362 | 15220000.0 | Laboratory test | snomed | SIM RS Panti Nugroho Hipertensi (3x), SIM RS Panti Nugroho Stroke (3x), SIM RS MPH Diabetes Melitus (3x), SIM RS MPH Hipertensi (3x), SIM RS Siaga Medika ANC | 5 |
| 2363 | 123038009.0 | Specimen | snomed | SIM RS Panti Nugroho Hipertensi, SIM RS Panti Nugroho Stroke, SIM RS MPH Diabetes Melitus, SIM RS MPH Hipertensi | 4 |
| 2364 | TK000028 | Diagnostic procedure | kemkes | SIM RS Panti Nugroho Hipertensi, SIM RS MPH Diabetes Melitus, SIM RS MPH Hipertensi | 3 |
| 2365 | 277132007.0 | Therapeutic procedure | snomed | SIM RS Panti Nugroho Hipertensi, SIM RS Panti Nugroho Stroke, SIM RS MPH Diabetes Melitus, SIM RS MPH Hipertensi | 4 |
| 2366 | 736286003.0 | Hypertension clinical management plan | snomed | SIM RS Panti Nugroho Hipertensi, SIM RS MPH Hipertensi | 2 |
| 2367 | I64 | Stroke, not specified as haemorrhage or infarction | icd-10 | SIM RS Panti Nugroho Stroke | 1 |
| 2368 | 80051000119107.0 | Stroke care management | snomed | SIM RS Panti Nugroho Stroke | 1 |
| 2369 | 736251000.0 | Stroke care plan | snomed | SIM RS Panti Nugroho Stroke | 1 |
| 2370 | 609496007.0 | Complication occurring during pregnancy | snomed | SIM RS Ummu Hani ANC (2x), SIM RS MPH ANC (2x) | 2 |
| 2371 | 49052-4 | Gestational age in days | kemkes sp | SIM RS Ummu Hani ANC, SIM RS MPH ANC | 2 |
| 2372 | 56542007.0 | Medical record administrator | snomed | SIM RS Ummu Hani INC, SIM RS Ummu Hani PNC, SIM RS MPH ANC, SIM RS MPH INC, SIM RS MPH PNC | 5 |
| 2373 | 23954006.0 | Acromion presentation | snomed | SIM RS Ummu Hani INC, SIM RS MPH INC, SIM RS PKU INC | 3 |
| 2374 | 289259007.0 | Vaginal delivery | snomed | SIM RS Ummu Hani INC, SIM RS MPH INC | 2 |
| 2375 | 289854007.0 | Perineum intact | snomed | SIM RS Ummu Hani PNC, SIM RS MPH PNC | 2 |
| 2376 | 57759005.0 | First degree perineal laceration | snomed | SIM RS Ummu Hani PNC, SIM RS MPH PNC | 2 |
| 2377 | 6234006.0 | Second degree perineal laceration | snomed | SIM RS Ummu Hani PNC, SIM RS MPH PNC | 2 |
| 2378 | 10217006.0 | Third degree perineal laceration | snomed | SIM RS Ummu Hani PNC, SIM RS MPH PNC | 2 |
| 2379 | 399031001.0 | Fourth degree perineal laceration | snomed | SIM RS Ummu Hani PNC, SIM RS MPH PNC | 2 |
| 2380 | 409019001.0 | Postpartum care management | snomed | SIM RS Ummu Hani PNC, SIM RS MPH PNC | 2 |
| 2381 | 243787009.0 | Antenatal screening | loinc | SIM RS MPH ANC | 1 |
| 2382 | 11935004.0 | Obstetrician | snomed | SIM RS MPH INC, SIM RS Siaga Medika INC | 2 |
| 2383 | 185389009.0 | Follow-up visit | snomed | SIM RS MPH PNC, SIM RS Goetoeng ANC, SIM RS Goetoeng INC | 3 |
| 2384 | 104.0 | Rumah Sakit | organization-type | SIM RS MPH BBL | 1 |
| 2385 | 20564-1 | Oxygen saturation in Blood | loinc | SIM RS MPH BBL, SIM RS Siaga Medika BBL | 2 |
| 2386 | SP000296 | Skrining Penyakit Jantung Bawaan | kemkes sp | SIM RS MPH BBL, SIM RS Siaga Medika BBL | 2 |
| 2387 | 408989004.0 | Newborn care management | snomed | SIM RS MPH BBL, SIM RS Siaga Medika BBL | 2 |
| 2388 | 10199-8 | Physical findings of Head Narrative | loinc | SIM RS MPH BBL, SIM RS Siaga Medika BBL | 2 |
| 2389 | 10192-3 | Physical findings of Back Narrative | loinc | SIM RS MPH BBL, SIM RS Siaga Medika BBL | 2 |
| 2390 | 11388-6 | Physical findings of Buttocks Narrative | loinc | SIM RS MPH BBL, SIM RS Siaga Medika BBL | 2 |
| 2391 | 11400-9 | Physical findings of Genitalia Narrative | loinc | SIM RS MPH BBL, SIM RS Siaga Medika BBL | 2 |
| 2392 | 787859002.0 | Vaccine product | snomed | SIM RS MPH BBL, SIM RS Siaga Medika BBL | 2 |
| 2393 | 113076002.0 | Glucose tolerance test | snomed | SIM RS MPH Diabetes Melitus (3x) | 1 |
| 2394 | 736284000.0 | Diabetes clinical management plan | snomed | SIM RS MPH Diabetes Melitus | 1 |
| 2395 | 29463-7 | Body weight |  | SIM RS Siaga Medika ANC | 1 |
| 2396 | ANC.B8.DE3 | Current weight |  | SIM RS Siaga Medika ANC | 1 |
| 2397 | 289625003.0 | Finding of fundal height of uterus | snomed | SIM RS Siaga Medika ANC | 1 |
| 2398 | 66862007.0 | Radiologist | snomed | SIM RS Siaga Medika ANC (9x) | 1 |
| 2399 | ANC.SS.DE38 | Denyut Jantung Janin (DJJ) USG |  | SIM RS Siaga Medika ANC | 1 |
| 2400 | 260415000.0 | Not detected | snomed | SIM RS Siaga Medika ANC | 1 |
| 2401 | 122555007.0 | Venous blood specimen | snomed | SIM RS Siaga Medika ANC (5x) | 1 |
| 2402 | 68961-2 |  |  | SIM RS Siaga Medika ANC | 1 |
| 2403 | 122575003.0 | Urine specimen | snomed | SIM RS Siaga Medika ANC | 1 |
| 2404 | 438791000124102.0 | Vitamin C supplement therapy | snomed | SIM RS Siaga Medika ANC | 1 |
| 2405 | SP000685 | Rujukan dari Bidan Praktik Mandiri (BPM) | kemkes sp | SIM RS Siaga Medika INC | 1 |
| 2406 | SP000461 | Usia Kehamilan (Hari) | kemkes sp | SIM RS Siaga Medika INC | 1 |
| 2407 | SP000686 | Faktor Risiko Persalinan | kemkes sp | SIM RS Siaga Medika INC | 1 |
| 2408 | SP000687 | Tidak Ada Faktor Risiko Persalinan | kemkes sp | SIM RS Siaga Medika INC | 1 |
| 2409 | SP000688 | Ada Faktor Risiko Persalinan | kemkes sp | SIM RS Siaga Medika INC | 1 |
| 2410 | 106292003.0 | Professional nurse | snomed | SIM RS Siaga Medika INC | 1 |
| 2411 | 303071001.0 | Person in the family | snomed | SIM RS Siaga Medika INC | 1 |
| 2412 | 125677006.0 | Relative | snomed | SIM RS Siaga Medika INC | 1 |
| 2413 | 257514003.0 | Member of public involved incidentally | snomed | SIM RS Siaga Medika INC | 1 |
| 2414 | 74.1 | Classical cesarean section | icd-9-cm | SIM RS Siaga Medika INC | 1 |
| 2415 | 72.7 | Vacuum extraction | icd-9-cm | SIM RS Siaga Medika INC | 1 |
| 2416 | 72.0 | Low forceps delivery | icd-9-cm | SIM RS Siaga Medika INC | 1 |
| 2417 | 289440007.0 | Fetal heart rate not observed | snomed | SIM RS PKU INC | 1 |
| 2418 | 289439005.0 | Fetal heart rate absent | snomed | SIM RS PKU INC | 1 |
| 2419 | 387700009.0 | Prolonged latent phase of labor | snomed | SIM RS PKU INC | 1 |
| 2420 | 249160009.0 | Onset of labor second stage | snomed | SIM RS PKU INC | 1 |
| 2421 | 236994008.0 | Placental delivery procedure | kemkes clinical-term | SIM RS PKU INC | 1 |
| 2422 | 289267004.0 | Finding of completeness of placenta | snomed | SIM RS PKU INC | 1 |
| 2423 | 249170006.0 | Complete placenta at delivery | snomed | SIM RS PKU INC | 1 |
| 2424 | 268479002.0 | Incomplete placenta at delivery | snomed | SIM RS PKU INC | 1 |
| 2425 | 302384005.0 | Controlled cord traction of placenta | snomed | SIM RS PKU INC | 1 |
| 2426 | 236996005.0 | Abdominal uterine fundal massage | snomed | SIM RS PKU INC | 1 |
| 2427 | 1148943004.0 | Retention of placenta and uterine membrane | snomed | SIM RS PKU INC | 1 |
| 2428 | 84007008.0 | Shock during AND/OR following labor AND/OR delivery | snomed | SIM RS PKU INC | 1 |
| 2429 | 118216002.0 | Labor finding | snomed | SIM RS PKU INC | 1 |
| 2430 | 10756061000119109 | Pain during postpartum period due to and following cesarean section | snomed | SIM RS PKU INC | 1 |
| 2431 | 719051004.0 | Quantity of postpartum maternal blood loss | snomed | SIM RS PKU INC | 1 |
| 2432 | 717809003.0 | Immediate postpartum care | snomed | SIM RS PKU INC | 1 |
| 2433 | 1991000124105.0 | Referred by self | snomed | SIM RS Goetoeng ANC, SIM RS Goetoeng INC, SIM RS Goetoeng PNC, SIM RS Goetoeng BBL | 4 |
| 2434 | 737481003.0 | Inpatient care management | snomed | SIM RS Goetoeng ANC | 1 |
| 2435 | SP000821 | Konsultasi Medis | kemkes sp | SIM RS Goetoeng ANC (3x) | 1 |
| 2436 | 34608000.0 | Alanine aminotransferase measurement | snomed | SIM RS Goetoeng ANC | 1 |
| 2437 | 86228006.0 | Uric acid measurement | snomed | SIM RS Goetoeng ANC | 1 |
| 2438 | 70901006.0 | Creatinine measurement | snomed | SIM RS Goetoeng ANC | 1 |
| 2439 | 27171005.0 | Urinalysis | snomed | SIM RS Goetoeng ANC (2x) | 1 |
| 2440 | 105010007.0 | Urea measurement | snomed | SIM RS Goetoeng ANC | 1 |
| 2441 | 396550006.0 | Blood test | snomed | SIM RS Goetoeng ANC | 1 |
| 2442 | 45896001.0 | Aspartate aminotransferase measurement | snomed | SIM RS Goetoeng ANC | 1 |
| 2443 | 165566005.0 | Whole blood clotting time procedure | snomed | SIM RS Goetoeng ANC | 1 |
| 2444 | 40675008.0 | Serologic test for syphilis | snomed | SIM RS Goetoeng ANC | 1 |
| 2445 | 269826008.0 | ABO blood grouping | snomed | SIM RS Goetoeng ANC (2x) | 1 |
| 2446 | 271061004.0 | Random blood glucose measurement | snomed | SIM RS Goetoeng ANC (2x) | 1 |
| 2447 | 104176001.0 | HIV antibody test | snomed | SIM RS Goetoeng ANC | 1 |
| 2448 | 72406003.0 | Bleeding time | snomed | SIM RS Goetoeng ANC | 1 |
| 2449 | 47758006.0 | Hepatitis B surface antigen measurement | snomed | SIM RS Goetoeng ANC | 1 |
| 2450 | 43396009.0 | Hemoglobin A1c measurement | snomed | SIM RS Goetoeng ANC | 1 |
| 2451 | 14740000.0 | Triglycerides measurement | snomed | SIM RS Goetoeng ANC | 1 |
| 2452 | 22644003.0 | Low density lipoprotein measurement | snomed | SIM RS Goetoeng ANC | 1 |
| 2453 | 17888004.0 | High density lipoprotein measurement | snomed | SIM RS Goetoeng ANC | 1 |
| 2454 | 121868005.0 | Total cholesterol measurement | snomed | SIM RS Goetoeng ANC | 1 |
| 2455 | 410136007.0 | Nursing coordination management | snomed | SIM RS Goetoeng ANC (2x) | 1 |
| 2456 | 410175003.0 | Dietary regime management | snomed | SIM RS Goetoeng ANC | 1 |
| 2457 | SP000824 | Tindakan Non Operatif Non Medis | kemkes sp | SIM RS Goetoeng ANC (2x) | 1 |
| 2458 | 182810003.0 | Intensive care monitoring | snomed | SIM RS Goetoeng ANC (2x) | 1 |
| 2459 | 424029000.0 | Personal hygiene case management | snomed | SIM RS Goetoeng ANC (3x) | 1 |
| 2460 | 410188000.0 | Taking patient vital signs assessment | snomed | SIM RS Goetoeng ANC (2x) | 1 |
| 2461 | 237433000.0 | Breast care procedure | snomed | SIM RS Goetoeng ANC | 1 |
| 2462 | 386372009.0 | Nutrition management | snomed | SIM RS Goetoeng ANC | 1 |
| 2463 | 18949003.0 | Change of dressing | snomed | SIM RS Goetoeng ANC (2x) | 1 |
| 2464 | 57.94 | Insertion of indwelling urinary catheter | icd-9-cm | SIM RS Goetoeng ANC, SIM RS Goetoeng INC | 2 |
| 2465 | 38.93 | Venous catheterization, not elsewhere classified | icd-9-cm | SIM RS Goetoeng ANC (2x) | 1 |
| 2466 | 96.39 | Other transanal enema | icd-9-cm | SIM RS Goetoeng ANC | 1 |
| 2467 | 99.1 | Injection or infusion of therapeutic or prophylactic substance | icd-9-cm | SIM RS Goetoeng ANC (2x) | 1 |
| 2468 | SP000823 | Perawatan Luka Operasi | kemkes sp | SIM RS Goetoeng ANC | 1 |
| 2469 | 386761002.0 | Local anesthesia | snomed | SIM RS Goetoeng ANC | 1 |
| 2470 | 69.7 | Insertion of intrauterine contraceptive device | icd-9-cm | SIM RS Goetoeng ANC, SIM RS Goetoeng INC (3x) | 2 |
| 2471 | SP000819 | Pemberian Anastesi Operatif Besar Khusus | kemkes sp | SIM RS Goetoeng ANC | 1 |
| 2472 | SP000825 | Operatif Besar Khusus | kemkes sp | SIM RS Goetoeng ANC | 1 |
| 2473 | SP000820 | Pengawasan Pre-Eklampsia Berat | kemkes sp | SIM RS Goetoeng ANC | 1 |
| 2474 | 48403009.0 | Insertion of infusion pump | snomed | SIM RS Goetoeng ANC (2x) | 1 |
| 2475 | 43060002.0 | Intravenous injection | snomed | SIM RS Goetoeng ANC (3x) | 1 |
| 2476 | 313006001.0 | Doppler ultrasonography of fetal heart for heart sounds | snomed | SIM RS Goetoeng ANC | 1 |
| 2477 | 765172009.0 | Doppler ultrasound | snomed | SIM RS Goetoeng ANC | 1 |
| 2478 | 441689006.0 | Measurement of total hemoglobin concentration | snomed | SIM RS Goetoeng ANC | 1 |
| 2479 | 234083009.0 | Venous puncture | snomed | SIM RS Goetoeng ANC (2x) | 1 |
| 2480 | 133858001.0 | Preoperative procedure | snomed | SIM RS Goetoeng ANC | 1 |
| 2481 | 99.04 | Transfusion of packed cells | icd-9-cm | SIM RS Goetoeng ANC, SIM RS Goetoeng INC (2x), SIM RS Goetoeng BBL (2x) | 3 |
| 2482 | 5447007.0 | Transfusion | snomed | SIM RS Goetoeng ANC | 1 |
| 2483 | 89.52 | Electrocardiogram | icd-9-cm | SIM RS Goetoeng ANC (2x), SIM RS Goetoeng INC (3x), SIM RS Goetoeng BBL (2x) | 3 |
| 2484 | 165745004.0 | Rhesus blood grouping | snomed | SIM RS Goetoeng ANC | 1 |
| 2485 | 386432004.0 | Shock management | snomed | SIM RS Goetoeng ANC | 1 |
| 2486 | 386219007.0 | Control of hemorrhage in postpartum uterus | snomed | SIM RS Goetoeng ANC | 1 |
| 2487 | 26758005.0 | Albumin measurement | snomed | SIM RS Goetoeng ANC | 1 |
| 2488 | 99.60 | Cardiopulmonary resuscitation, not otherwise specified | icd-9-cm | SIM RS Goetoeng ANC, SIM RS Goetoeng BBL (4x) | 2 |
| 2489 | 278297009.0 | Blood gas analysis | snomed | SIM RS Goetoeng ANC | 1 |
| 2490 | 96.07 | Insertion of other (naso-)gastric tube | icd-9-cm | SIM RS Goetoeng ANC | 1 |
| 2491 | 96.6 | Enteral infusion of concentrated nutritional substances | icd-9-cm | SIM RS Goetoeng ANC | 1 |
| 2492 | 173830003.0 | Gastric lavage | snomed | SIM RS Goetoeng ANC | 1 |
| 2493 | 57931004.0 | Puncture of artery | snomed | SIM RS Goetoeng ANC | 1 |
| 2494 | 51241000.0 | Control of hemorrhage | snomed | SIM RS Goetoeng ANC | 1 |
| 2495 | 97.37 | Removal of tracheostomy tube | icd-9-cm | SIM RS Goetoeng ANC | 1 |
| 2496 | SP000826 | Tindakan Non Medis | kemkes sp | SIM RS Goetoeng ANC (2x) | 1 |
| 2497 | 276026009.0 | Fluid balance regulation | snomed | SIM RS Goetoeng ANC | 1 |
| 2498 | 104177005.0 | Electrolyte measurement | snomed | SIM RS Goetoeng ANC | 1 |
| 2499 | 87.44 | Routine chest x-ray, so described | icd-9-cm | SIM RS Goetoeng ANC, SIM RS Goetoeng INC, SIM RS Goetoeng BBL (13x) | 3 |
| 2500 | 96.04 | Insertion of endotracheal tube | icd-9-cm | SIM RS Goetoeng ANC, SIM RS Goetoeng BBL (5x) | 2 |
| 2501 | 226007004.0 | Post-surgical wound care | snomed | SIM RS Goetoeng ANC | 1 |
| 2502 | SP000827 | Pemasangan dan Monitoring Syringe Pump | kemkes sp | SIM RS Goetoeng ANC | 1 |
| 2503 | SP000822 | Konsultasi Non Medis | kemkes sp | SIM RS Goetoeng ANC | 1 |
| 2504 | 73.1 | Other surgical induction of labor | icd-9-cm | SIM RS Goetoeng ANC | 1 |
| 2505 | 309878003.0 | Exploration of uterine cavity | snomed | SIM RS Goetoeng ANC | 1 |
| 2506 | SP000818 | Pemasangan IUD/ Implan | kemkes sp | SIM RS Goetoeng ANC | 1 |
| 2507 | SP000815 | Jenis Kasus Pasien | kemkes sp | SIM RS Goetoeng ANC, SIM RS Goetoeng PNC | 2 |
| 2508 | SP000816 | Kasus Baru | kemkes sp | SIM RS Goetoeng ANC, SIM RS Goetoeng PNC | 2 |
| 2509 | SP000817 | Kasus Lama | kemkes sp | SIM RS Goetoeng ANC, SIM RS Goetoeng PNC | 2 |
| 2510 | 184061005.0 | Patient registration status | snomed | SIM RS Goetoeng ANC, SIM RS Goetoeng INC, SIM RS Goetoeng PNC, SIM RS Goetoeng BBL | 4 |
| 2511 | SP000812 | Pasien Baru | kemkes sp | SIM RS Goetoeng ANC, SIM RS Goetoeng INC, SIM RS Goetoeng PNC, SIM RS Goetoeng BBL | 4 |
| 2512 | SP000813 | Pasien Lama | kemkes sp | SIM RS Goetoeng ANC, SIM RS Goetoeng INC, SIM RS Goetoeng PNC, SIM RS Goetoeng BBL | 4 |
| 2513 | SP000814 | Rujukan dari Dokter Praktik Mandiri | kemkes sp | SIM RS Goetoeng INC, SIM RS Goetoeng PNC, SIM RS Goetoeng BBL | 3 |
| 2514 | 224294005.0 | No formal education | snomed | SIM RS Goetoeng INC, SIM RS Goetoeng BBL | 2 |
| 2515 | 473463000.0 | Received elementary school education | snomed | SIM RS Goetoeng INC, SIM RS Goetoeng PNC | 2 |
| 2516 | 603435002.0 | Educated to junior high school level | snomed | SIM RS Goetoeng INC, SIM RS Goetoeng PNC | 2 |
| 2517 | 603434003.0 | Educated to senior high school level | snomed | SIM RS Goetoeng INC, SIM RS Goetoeng PNC | 2 |
| 2518 | 38901000087109.0 | University diploma achieved | snomed | SIM RS Goetoeng INC (2x) | 1 |
| 2519 | 38861000087100.0 | Bachelor's degree achieved | snomed | SIM RS Goetoeng INC, SIM RS Goetoeng PNC | 2 |
| 2520 | O61.0 | Failed medical induction of labour | icd-10 | SIM RS Goetoeng INC (2x) | 1 |
| 2521 | O64.4 | Obstructed labour due to shoulder presentation | icd-10 | SIM RS Goetoeng INC (4x) | 1 |
| 2522 | O42.0 | Premature rupture of membranes, onset of labour within 24 hours | icd-10 | SIM RS Goetoeng INC (2x) | 1 |
| 2523 | O33.0 | Maternal care for disproportion due to deformity of maternal pelvic bones | icd-10 | SIM RS Goetoeng INC (4x) | 1 |
| 2524 | O34.2 | Maternal care due to uterine scar from previous surgery | icd-10 | SIM RS Goetoeng INC (3x) | 1 |
| 2525 | O45.0 | Premature separation of placenta with coagulation defect | icd-10 | SIM RS Goetoeng INC (2x) | 1 |
| 2526 | O33.9 | Maternal care for disproportion, unspecified | icd-10 | SIM RS Goetoeng INC (2x) | 1 |
| 2527 | O63.1 | Prolonged second stage of labour | icd-10 | SIM RS Goetoeng INC (4x) | 1 |
| 2528 | O64.1 | Obstructed labour due to breech presentation | icd-10 | SIM RS Goetoeng INC (4x) | 1 |
| 2529 | O14.1 | Severe pre-eclampsia | icd-10 | SIM RS Goetoeng INC (4x) | 1 |
| 2530 | O30.0 | Twin pregnancy | icd-10 | SIM RS Goetoeng INC (3x) | 1 |
| 2531 | O68.9 | Labour and delivery complicated by fetal stress, unspecified | icd-10 | SIM RS Goetoeng INC (3x) | 1 |
| 2532 | O14.9 | Pre-eclampsia, unspecified | icd-10 | SIM RS Goetoeng INC (3x) | 1 |
| 2533 | O44.0 | Placenta praevia specified as without haemorrhage | icd-10 | SIM RS Goetoeng INC (3x) | 1 |
| 2534 | O36.4 | Maternal care for intrauterine death | icd-10 | SIM RS Goetoeng INC (2x) | 1 |
| 2535 | O42.1 | Premature rupture of membranes, onset of labour after 24 hours | icd-10 | SIM RS Goetoeng INC (3x) | 1 |
| 2536 | O48 | Prolonged pregnancy | icd-10 | SIM RS Goetoeng INC (4x) | 1 |
| 2537 | O63.0 | Prolonged first stage of labour | icd-10 | SIM RS Goetoeng INC (5x) | 1 |
| 2538 | O41.0 | Oligohydramnios | icd-10 | SIM RS Goetoeng INC (4x) | 1 |
| 2539 | O70.9 | Perineal laceration during delivery, unspecified | icd-10 | SIM RS Goetoeng INC (2x) | 1 |
| 2540 | O36.5 | Maternal care for poor fetal growth | icd-10 | SIM RS Goetoeng INC (4x) | 1 |
| 2541 | O99.4 | Diseases of the circulatory system complicating pregnancy, childbirth and the puerperium | icd-10 | SIM RS Goetoeng INC (3x) | 1 |
| 2542 | O47.0 | False labour before 37 completed weeks of gestation | icd-10 | SIM RS Goetoeng INC (2x) | 1 |
| 2543 | O60.1 | Preterm labour with preterm delivery | icd-10 | SIM RS Goetoeng INC (4x) | 1 |
| 2544 | O14.0 | Moderate pre-eclampsia | icd-10 | SIM RS Goetoeng INC (3x) | 1 |
| 2545 | O42 | Premature rupture of membranes | icd-10 | SIM RS Goetoeng INC (2x) | 1 |
| 2546 | O22.4 | Haemorrhoids in pregnancy | icd-10 | SIM RS Goetoeng INC (2x) | 1 |
| 2547 | O82.0 | Delivery by elective caesarean section | icd-10 | SIM RS Goetoeng INC (2x) | 1 |
| 2548 | Z30.1 | Insertion of (intrauterine) contraceptive device | icd-10 | SIM RS Goetoeng INC (3x) | 1 |
| 2549 | O82.9 | Delivery by caesarean section, unspecified | icd-10 | SIM RS Goetoeng INC (2x) | 1 |
| 2550 | Z37.0 | Single live birth | icd-10 | SIM RS Goetoeng INC (2x) | 1 |
| 2551 | O69.1 | Labour and delivery complicated cord around neck, with compression | icd-10 | SIM RS Goetoeng INC (2x) | 1 |
| 2552 | O11 | Pre-existing hypertensive disorder with superimposed proteinuria | icd-10 | SIM RS Goetoeng INC (2x) | 1 |
| 2553 | O99.0 | Anaemia complicating pregnancy, childbirth and the puerperium | icd-10 | SIM RS Goetoeng INC (2x) | 1 |
| 2554 | H52.1 | Myopia | icd-10 | SIM RS Goetoeng INC (2x) | 1 |
| 2555 | O83.9 | Assisted single delivery, unspecified | icd-10 | SIM RS Goetoeng INC (2x) | 1 |
| 2556 | Z30.8 | Other contraceptive management | icd-10 | SIM RS Goetoeng INC (2x) | 1 |
| 2557 | O73.0 | Retained placenta without haemorrhage | icd-10 | SIM RS Goetoeng INC (2x) | 1 |
| 2558 | O99.5 | Diseases of the respiratory system complicating pregnancy, childbirth and the puerperium | icd-10 | SIM RS Goetoeng INC (2x) | 1 |
| 2559 | R33 | Retention of urine | icd-10 | SIM RS Goetoeng INC (2x) | 1 |
| 2560 | Z86.4 | Personal history of psychoactive substance abuse | icd-10 | SIM RS Goetoeng INC (2x) | 1 |
| 2561 | O16 | Unspecified maternal hypertension | icd-10 | SIM RS Goetoeng INC (2x) | 1 |
| 2562 | O80.0 | Spontaneous vertex delivery | icd-10 | SIM RS Goetoeng INC (2x) | 1 |
| 2563 | O98.0 | Tuberculosis complicating pregnancy, childbirth and the puerperium | icd-10 | SIM RS Goetoeng INC (2x) | 1 |
| 2564 | Z87.5 | Personal history complications of pregnancy, childbirth and the puerperium | icd-10 | SIM RS Goetoeng INC (2x) | 1 |
| 2565 | O00 | Ectopic pregnancy | icd-10 | SIM RS Goetoeng INC | 1 |
| 2566 | I49.9 | Cardiac arrhythmia, unspecified | icd-10 | SIM RS Goetoeng INC (2x) | 1 |
| 2567 | I49.3 | Ventricular premature depolarization | icd-10 | SIM RS Goetoeng INC (2x) | 1 |
| 2568 | O24 | Diabetes mellitus in pregnancy | icd-10 | SIM RS Goetoeng INC | 1 |
| 2569 | O81.4 | Vacuum extractor delivery | icd-10 | SIM RS Goetoeng INC (2x) | 1 |
| 2570 | O82.1 | Delivery by emergency caesarean section | icd-10 | SIM RS Goetoeng INC (2x) | 1 |
| 2571 | O98.1 | Syphilis complicating pregnancy, childbirth and the puerperium | icd-10 | SIM RS Goetoeng INC | 1 |
| 2572 | A53.9 | Syphilis, unspecified | icd-10 | SIM RS Goetoeng INC | 1 |
| 2573 | O40 | Polyhydramnios | icd-10 | SIM RS Goetoeng INC | 1 |
| 2574 | D64.9 | Anaemia, unspecified | icd-10 | SIM RS Goetoeng INC | 1 |
| 2575 | Z30.2 | Sterilization | icd-10 | SIM RS Goetoeng INC | 1 |
| 2576 | Z37.2 | Twins, both liveborn | icd-10 | SIM RS Goetoeng INC | 1 |
| 2577 | Z86.1 | Personal history of infectious and parasitic diseases | icd-10 | SIM RS Goetoeng INC | 1 |
| 2578 | K56.0 | Paralytic ileus | icd-10 | SIM RS Goetoeng INC | 1 |
| 2579 | O99.6 | Diseases of the digestive system complicating pregnancy, childbirth and the puerperium | icd-10 | SIM RS Goetoeng INC | 1 |
| 2580 | R00.0 | Tachycardia, unspecified | icd-10 | SIM RS Goetoeng INC | 1 |
| 2581 | O31 | Complications specific to multiple gestation | icd-10 | SIM RS Goetoeng INC | 1 |
| 2582 | O10.0 | Pre-existing essential hypertension complicating pregnancy, childbirth and the puerperium | icd-10 | SIM RS Goetoeng INC | 1 |
| 2583 | O98.4 | Viral hepatitis complicating pregnancy, childbirth and the puerperium | icd-10 | SIM RS Goetoeng INC | 1 |
| 2584 | O24.9 | Diabetes mellitus in pregnancy, unspecified | icd-10 | SIM RS Goetoeng INC | 1 |
| 2585 | H44.2 | Degenerative myopia | icd-10 | SIM RS Goetoeng INC | 1 |
| 2586 | N83.2 | Other and unspecified ovarian cysts | icd-10 | SIM RS Goetoeng INC | 1 |
| 2587 | D56.9 | Thalassaemia, unspecified | icd-10 | SIM RS Goetoeng INC (2x) | 1 |
| 2588 | J45.9 | Asthma, unspecified | icd-10 | SIM RS Goetoeng INC | 1 |
| 2589 | D69.6 | Thrombocytopenia, unspecified | icd-10 | SIM RS Goetoeng INC | 1 |
| 2590 | O99.1 | Other diseases of the blood and blood-forming organs and certain disorders involving the immune mechanism complicating pregnancy, childbirth and the puerperium | icd-10 | SIM RS Goetoeng INC | 1 |
| 2591 | A18.8 | Tuberculosis of other specified organs | icd-10 | SIM RS Goetoeng INC | 1 |
| 2592 | O72.1 | Other immediate postpartum haemorrhage | icd-10 | SIM RS Goetoeng INC | 1 |
| 2593 | O71.7 | Obstetric haematoma of pelvis | icd-10 | SIM RS Goetoeng INC | 1 |
| 2594 | O00.9 | Ectopic pregnancy, unspecified | icd-10 | SIM RS Goetoeng INC | 1 |
| 2595 | I25.9 | Chronic ischaemic heart disease, unspecified | icd-10 | SIM RS Goetoeng INC | 1 |
| 2596 | O71.3 | Obstetric laceration of cervix | icd-10 | SIM RS Goetoeng INC | 1 |
| 2597 | O46.8 | Other antepartum haemorrhage | icd-10 | SIM RS Goetoeng INC | 1 |
| 2598 | 74.4 | Cesarean section of other specified type | icd-9-cm | SIM RS Goetoeng INC (2x) | 1 |
| 2599 | 73.4 | Medical induction of labor | icd-9-cm | SIM RS Goetoeng INC (2x) | 1 |
| 2600 | 90.59 | Microscopic examination of blood, Other microscopic examination | icd-9-cm | SIM RS Goetoeng INC (2x), SIM RS Goetoeng BBL (4x) | 2 |
| 2601 | 75.32 | Fetal EKG (scalp) | icd-9-cm | SIM RS Goetoeng INC (2x) | 1 |
| 2602 | 91.39 | Microscopic examination of specimen from bladder, urethra, prostate,seminal vesicle, perivesical tissue, and of urine and semen, Other microscopic examination | icd-9-cm | SIM RS Goetoeng INC | 1 |
| 2603 | 66.39 | Other bilateral destruction or occlusion of fallopian tubes | icd-9-cm | SIM RS Goetoeng INC (2x) | 1 |
| 2604 | 90.52 | Microscopic examination of blood, Culture | icd-9-cm | SIM RS Goetoeng INC (2x) | 1 |
| 2605 | 88.09 | Other soft tissue x-ray of abdominal wall | icd-9-cm | SIM RS Goetoeng INC (2x), SIM RS Goetoeng BBL (8x) | 2 |
| 2606 | 97.71 | Removal of intrauterine contraceptive device | icd-9-cm | SIM RS Goetoeng INC (3x) | 1 |
| 2607 | 65.29 | Other local excision or destruction of ovary | icd-9-cm | SIM RS Goetoeng INC (2x) | 1 |
| 2608 | 69.02 | Dilation and curettage following delivery or abortion | icd-9-cm | SIM RS Goetoeng INC (2x) | 1 |
| 2609 | 70.79 | Other repair of vagina | icd-9-cm | SIM RS Goetoeng INC | 1 |
| 2610 | 75.69 | Repair of other current obstetric laceration | icd-9-cm | SIM RS Goetoeng INC (3x) | 1 |
| 2611 | 75.51 | Repair of current obstetric laceration of cervix | icd-9-cm | SIM RS Goetoeng INC (2x) | 1 |
| 2612 | 90.95 | Microscopic examination of specimen from lower gastrointestinal tract and of stool, Toxicology | icd-9-cm | SIM RS Goetoeng INC | 1 |
| 2613 | 91.3 | Microscopic examination of specimen from bladder, urethra, prostate,seminal vesicle, perivesical tissue, and of urine and semen | icd-9-cm | SIM RS Goetoeng INC | 1 |
| 2614 | 73.6 | Episiotomy | icd-9-cm | SIM RS Goetoeng INC | 1 |
| 2615 | 72.79 | Other vacuum extraction | icd-9-cm | SIM RS Goetoeng INC | 1 |
| 2616 | 75.92 | Evacuation of other hematoma of vulva or vagina | icd-9-cm | SIM RS Goetoeng INC | 1 |
| 2617 | 371001000.0 | Patient cured | snomed | SIM RS Goetoeng INC, SIM RS Goetoeng BBL | 2 |
| 2618 | 183797002.0 | Duration of inpatient stay | snomed | SIM RS Goetoeng INC, SIM RS Goetoeng BBL | 2 |
| 2619 | SP000811 | Jalur Masuk Rawat Inap | kemkes sp | SIM RS Goetoeng INC, SIM RS Goetoeng BBL | 2 |
| 2620 | 225728007.0 | Accident and Emergency department | snomed | SIM RS Goetoeng INC, SIM RS Goetoeng BBL | 2 |
| 2621 | 309942007.0 | Obstetrics and gynecology department | snomed | SIM RS Goetoeng INC | 1 |
| 2622 | 1363029004.0 | Hospital observation unit | snomed | SIM RS Goetoeng INC | 1 |
| 2623 | 405606005.0 | Labor and delivery unit | snomed | SIM RS Goetoeng INC, SIM RS Goetoeng BBL | 2 |
| 2624 | 741725004.0 | Primary school started but not finished | snomed | SIM RS Goetoeng PNC | 1 |
| 2625 | SP000277 | D3 | kemkes sp | SIM RS Goetoeng PNC | 1 |
| 2626 | SP000834 | D1/D2 | kemkes sp | SIM RS Goetoeng PNC | 1 |
| 2627 | 50849002.0 | Emergency room admission | snomed | SIM RS Goetoeng BBL | 1 |
| 2628 | P22.0 | Respiratory distress syndrome of newborn | icd-10 | SIM RS Goetoeng BBL (5x) | 1 |
| 2629 | E46 | Unspecified protein-energy malnutrition | icd-10 | SIM RS Goetoeng BBL (2x) | 1 |
| 2630 | P21.0 | Severe birth asphyxia | icd-10 | SIM RS Goetoeng BBL (7x) | 1 |
| 2631 | G41.9 | Status epilepticus, unspecified | icd-10 | SIM RS Goetoeng BBL (2x) | 1 |
| 2632 | R56.0 | Febrile convulsions | icd-10 | SIM RS Goetoeng BBL (2x) | 1 |
| 2633 | P21.1 | Mild and moderate birth asphyxia | icd-10 | SIM RS Goetoeng BBL (4x) | 1 |
| 2634 | P23.9 | Congenital pneumonia, unspecified | icd-10 | SIM RS Goetoeng BBL (3x) | 1 |
| 2635 | P07.1 | Other low birth weight | icd-10 | SIM RS Goetoeng BBL (2x) | 1 |
| 2636 | R40.2 | Coma, unspecified | icd-10 | SIM RS Goetoeng BBL (4x) | 1 |
| 2637 | P70.4 | Other neonatal hypoglycaemia | icd-10 | SIM RS Goetoeng BBL (2x) | 1 |
| 2638 | P59.9 | Neonatal jaundice, unspecified | icd-10 | SIM RS Goetoeng BBL (2x) | 1 |
| 2639 | P90 | Convulsions of newborn | icd-10 | SIM RS Goetoeng BBL (2x) | 1 |
| 2640 | J96.9 | Respiratory failure, unspecified | icd-10 | SIM RS Goetoeng BBL (2x) | 1 |
| 2641 | P03.4 | Fetus and newborn affected by caesarean delivery | icd-10 | SIM RS Goetoeng BBL (2x) | 1 |
| 2642 | P80.9 | Hypothermia of newborn, unspecified | icd-10 | SIM RS Goetoeng BBL (2x) | 1 |
| 2643 | P39.9 | Infection specific to the perinatal period, unspecified | icd-10 | SIM RS Goetoeng BBL (2x) | 1 |
| 2644 | 96.05 | Other intubation of respiratory tract | icd-9-cm | SIM RS Goetoeng BBL (2x) | 1 |
| 2645 | 90.41 | Microscopic examination of specimen from trachea, bronchus, pleura,lung,and other thoracic specimen, and of sputum, Bacterial smear | icd-9-cm | SIM RS Goetoeng BBL (2x) | 1 |
| 2646 | 93.90 | Non-invasive mechanical ventilation | icd-9-cm | SIM RS Goetoeng BBL (5x) | 1 |
| 2647 | 96.71 | Continuous invasive mechanical ventilation for less than 96 consecutive hours | icd-9-cm | SIM RS Goetoeng BBL (3x) | 1 |
| 2648 | 96.72 | Continuous invasive mechanical ventilation for 96 consecutive hours or more | icd-9-cm | SIM RS Goetoeng BBL (2x) | 1 |
| 2649 | SP000757 | Status Kependudukan (Khusus Papua) | kemkes sp | SISMAL Regmal 1 | 1 |
| 2650 | SP000758 | Orang Asli Papua (OAP) | kemkes sp | SISMAL Regmal 1 | 1 |
| 2651 | SP000759 | Bukan Orang Asli Papua | kemkes sp | SISMAL Regmal 1 | 1 |
| 2652 | SP000760 | Pasien Beralamat (KTP) Diluar Wilayah | kemkes sp | SISMAL Regmal 1 | 1 |
| 2653 | 67630004 | Miner | snomed | SISMAL Regmal 1 | 1 |
| 2654 | SP000754 | Pedagang | kemkes sp | SISMAL Regmal 1 | 1 |
| 2655 | 34484007 | Forestry worker | snomed | SISMAL Regmal 1 | 1 |
| 2656 | 34024003 | Gardener | snomed | SISMAL Regmal 1 | 1 |
| 2657 | SP000803 | Fasyankes Pencatat | kemkes sp | SISMAL Regmal 1 | 1 |
| 2658 | 138 | Puskesmas Pembantu | organization-type | SISMAL Regmal 1 | 1 |
| 2659 | SP000761 | Faskes Swasta | kemkes organization-ownership | SISMAL Regmal 1 | 1 |
| 2660 | SP000804 | Kantor Kesehatan Pelabuhan | kemkes sp | SISMAL Regmal 1 | 1 |
| 2661 | SP000805 | Perdhaki | kemkes sp | SISMAL Regmal 1 | 1 |
| 2662 | SP000806 | Pos Kesehatan TNI | kemkes sp | SISMAL Regmal 1 | 1 |
| 2663 | 418775008 | Finding method | snomed | SISMAL Regmal 1 | 1 |
| 2664 | SP000807 | Passive Case Detection | kemkes sp | SISMAL Regmal 1 | 1 |
| 2665 | SP000808 | Mass Blood Survey | kemkes sp | SISMAL Regmal 1 | 1 |
| 2666 | SP000809 | Survei Non PE | kemkes sp | SISMAL Regmal 1 | 1 |
| 2667 | SP000810 | Surveilans Migrasi | kemkes sp | SISMAL Regmal 1 | 1 |
| 2668 | 702705002 | Mobile clinic | snomed | SISMAL Regmal 1 | 1 |
| 2669 | 365690003 | Finding of presence of organism | snomed | SISMAL Regmal 1 | 1 |
| 2670 | 30020004 | Plasmodium falciparum | snomed | SISMAL Regmal 1 | 1 |
| 2671 | 56395006 | Plasmodium malariae | snomed | SISMAL Regmal 1 | 1 |
| 2672 | 49918008 | Plasmodium knowlesi | snomed | SISMAL Regmal 1 | 1 |
| 2673 | 74746009 | Plasmodium vivax | snomed | SISMAL Regmal 1 | 1 |
| 2674 | 18508006 | Plasmodium ovale | snomed | SISMAL Regmal 1 | 1 |
| 2675 | 21070001 | Mixed malaria | snomed | SISMAL Regmal 1 | 1 |
| 2676 | B54 | Unspecified malaria | icd-10 | SISMAL Validasi Indigenous | 1 |
| 2677 | 409496000 | Mode of transmission | snomed | SISMAL Validasi Indigenous | 1 |
| 2678 | 418427004 | Vector-borne transmission | snomed | SISMAL Validasi Indigenous | 1 |
| 2679 | 418912005 | Transfusion transmission | snomed | SISMAL Validasi Indigenous | 1 |
| 2680 | 417409004 | Transplacental transmission | snomed | SISMAL Validasi Indigenous | 1 |
| 2681 | SP000740 | Kategori Wilayah Penularan | kemkes sp | SISMAL Validasi Indigenous | 1 |
| 2682 | SP000741 | Dalam Wilayah Puskesmas | kemkes sp | SISMAL Validasi Indigenous | 1 |
| 2683 | SP000742 | Luar Wilayah Puskesmas | kemkes sp | SISMAL Validasi Indigenous | 1 |
| 2684 | SP000743 | Luar Wilayah Kabupaten/Kota | kemkes sp | SISMAL Validasi Indigenous | 1 |
| 2685 | SP000744 | Luar Wilayah Provinsi | kemkes sp | SISMAL Validasi Indigenous | 1 |
| 2686 | SP000745 | Luar Wilayah Negara | kemkes sp | SISMAL Validasi Indigenous | 1 |
