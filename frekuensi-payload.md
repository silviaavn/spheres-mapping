# Frekuensi Payload (lintas form)

Bagian dari konsolidasi [`output.md`](output.md). Dibuat otomatis, jangan diedit manual. Lihat juga [`frekuensi-code.md`](frekuensi-code.md).

Frekuensi = di berapa form dipakai. Angka (Nx) = muncul N kali di form itu.

| # | Resource | Code pembeda | Display | Dipakai di form | Frekuensi |
|---|---|---|---|---|---|
| 1 | PractitionerRole | – | – | Maternal Outcome, SiGizi ANC | 2 |
| 2 | Practitioner | – | – | Maternal Outcome, Raffle (2x) | 2 |
| 3 | Patient | – | – | Maternal Outcome, Raffle, SiGizi ANC, SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 04, SITB TB 16K, MPDN Kematian Bayi (2x), MPDN Kematian Ibu | 10 |
| 4 | Encounter | – | – | Maternal Outcome, Raffle, SiGizi ANC, SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 04, SITB TB 16K | 8 |
| 5 | Condition | SP000738 | Kunjungan pemantauan luaran maternal | Maternal Outcome | 1 |
| 6 | EpisodeOfCare | ANC | Antenatal Care | Maternal Outcome, Raffle, SiGizi ANC | 3 |
| 7 | EpisodeOfCare | PNC | Postnatal Care | Maternal Outcome | 1 |
| 8 | Observation | SP000389 | Keadaan Ibu | Maternal Outcome | 1 |
| 9 | Observation | 93857-1 | Date and time of obstetric delivery | Maternal Outcome | 1 |
| 10 | Observation | 81956-5 | Date and time of death [TimeStamp] | Maternal Outcome, MPDN Kematian Bayi, MPDN Kematian Ibu | 3 |
| 11 | Observation | LT000005 | Alamat Mati | Maternal Outcome | 1 |
| 12 | Observation | 79378-6 | Cause of death | Maternal Outcome, MPDN Kematian Bayi, MPDN Kematian Ibu | 3 |
| 13 | Location | – | – | Raffle, SITB TB 06 | 2 |
| 14 | Condition | SP001135 | Presensi Posyandu | Raffle | 1 |
| 15 | Observation | 385438008 | Source of information | Raffle | 1 |
| 16 | Condition | 134435003 | Routine antenatal care | SiGizi ANC | 1 |
| 17 | Observation | 424144002 | Current chronological age | SiGizi ANC, SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 04, SITB TB 16K (2x) | 6 |
| 18 | Observation | 8665-2 | Last menstrual period start date | SiGizi ANC | 1 |
| 19 | Observation | 18185-9 | Gestational age | SiGizi ANC, MPDN Kematian Bayi | 2 |
| 20 | Observation | 11778-8 | Delivery date Estimated | SiGizi ANC | 1 |
| 21 | Observation | 8302-2 | Body height | SiGizi ANC | 1 |
| 22 | Observation | OC000010 | Indeks Massa Tubuh Sebelum Hamil | SiGizi ANC | 1 |
| 23 | Immunization | VG139 | Td | SiGizi ANC | 1 |
| 24 | Observation | SP000001 | Skrining Imunisasi Tetanus Toksoid | SiGizi ANC | 1 |
| 25 | Observation | SP000002 | Kunjungan Pertama Pemeriksaan Kehamilan | SiGizi ANC | 1 |
| 26 | Observation | 29463-7 | Body weight | SiGizi ANC | 1 |
| 27 | Observation | 392570002 | Blood pressure finding | SiGizi ANC | 1 |
| 28 | Observation | 284473002 | Mid upper arm circumference | SiGizi ANC | 1 |
| 29 | Observation | 289625003 | Finding of fundal height of uterus | SiGizi ANC | 1 |
| 30 | Observation | 883-9 | ABO group [Type] in Blood | SiGizi ANC | 1 |
| 31 | Observation | 10331-7 | Rh [Type] in Blood | SiGizi ANC | 1 |
| 32 | Observation | 289437007 | Finding of fetal heart rate | SiGizi ANC | 1 |
| 33 | Observation | 72155-5 | Position in womb Fetus [RHEA] | SiGizi ANC | 1 |
| 34 | Procedure | 88.78 | Diagnostic ultrasound of gravid uterus | SiGizi ANC | 1 |
| 35 | Observation | 268445003 | Ultrasound scan - obstetric | SiGizi ANC | 1 |
| 36 | MedicationRequest | 92000653 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula | SiGizi ANC | 1 |
| 37 | MedicationDispense | 93015491 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | SiGizi ANC | 1 |
| 38 | MedicationRequest | SP000370 | Multiple Micronutrient Supplement | SiGizi ANC | 1 |
| 39 | MedicationDispense | SP000370 | Multiple Micronutrient Supplement | SiGizi ANC | 1 |
| 40 | ServiceRequest | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | SiGizi ANC | 1 |
| 41 | Specimen | 122555007 | Venous blood specimen | SiGizi ANC (5x) | 1 |
| 42 | Observation | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | SiGizi ANC | 1 |
| 43 | DiagnosticReport | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | SiGizi ANC | 1 |
| 44 | ServiceRequest | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | SiGizi ANC | 1 |
| 45 | Observation | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | SiGizi ANC | 1 |
| 46 | DiagnosticReport | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | SiGizi ANC | 1 |
| 47 | ServiceRequest | 22464-2 | Reagin Ab [Presence] in Specimen | SiGizi ANC | 1 |
| 48 | Observation | 22464-2 | Reagin Ab [Presence] in Specimen | SiGizi ANC | 1 |
| 49 | DiagnosticReport | 22464-2 | Reagin Ab [Presence] in Specimen | SiGizi ANC | 1 |
| 50 | ServiceRequest | 2887-8 | Protein [Presence] in Urine | SiGizi ANC | 1 |
| 51 | Specimen | 122575003 | Urine specimen | SiGizi ANC | 1 |
| 52 | Observation | 2887-8 | Protein [Presence] in Urine | SiGizi ANC | 1 |
| 53 | DiagnosticReport | 2887-8 | Protein [Presence] in Urine | SiGizi ANC | 1 |
| 54 | ServiceRequest | 718-7 | Hemoglobin [Mass/volume] in Blood | SiGizi ANC | 1 |
| 55 | Observation | 718-7 | Hemoglobin [Mass/volume] in Blood | SiGizi ANC | 1 |
| 56 | DiagnosticReport | 718-7 | Hemoglobin [Mass/volume] in Blood | SiGizi ANC | 1 |
| 57 | ServiceRequest | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | SiGizi ANC | 1 |
| 58 | Observation | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | SiGizi ANC | 1 |
| 59 | DiagnosticReport | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | SiGizi ANC | 1 |
| 60 | Observation | 15220000 | Laboratory test | SiGizi ANC | 1 |
| 61 | Observation | SP000007 | Tatalaksana Anemia | SiGizi ANC | 1 |
| 62 | Observation | SP000010 | Skrining Hipertensi dalam Kehamilan | SiGizi ANC | 1 |
| 63 | Observation | SP000012 | Tatalaksana Pre Eklampsia | SiGizi ANC | 1 |
| 64 | Observation | SP000014 | Tatalaksana KEK | SiGizi ANC | 1 |
| 65 | Observation | SP000015 | Risiko Masalah Kesehatan | SiGizi ANC | 1 |
| 66 | Observation | SP000016 | Tatalaksana Masalah Kesehatan | SiGizi ANC | 1 |
| 67 | Procedure | 1230101008 | Counseling for pregnancy | SiGizi ANC | 1 |
| 68 | Procedure | 385892002 | Mental health screening | SiGizi ANC | 1 |
| 69 | Organization | – | – | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 70 | EpisodeOfCare | TB-SO | Tuberkulosis Sensitif Obat | SITB TB 06 (3x), SITB TB 03 SO, SITB TB 04 | 3 |
| 71 | Condition | Z03.0 | Observation for suspected tuberculosis | SITB TB 06 | 1 |
| 72 | Condition | A15.0 | Tuberculosis of lung, confirmed by sputum microscopy with or without culture | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 73 | QuestionnaireResponse | – | – | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 16K | 4 |
| 74 | Observation | OC000191 | Jumlah Skoring TBC Anak | SITB TB 06, SITB TB 03 SO | 2 |
| 75 | ServiceRequest | 24648-8 | XR Chest PA upright | SITB TB 06 | 1 |
| 76 | Observation | 24648-8 | XR Chest PA upright | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 77 | DiagnosticReport | 24648-8 | XR Chest PA upright | SITB TB 06 | 1 |
| 78 | Procedure | 424489006 | Mantoux test | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 79 | Observation | 23539-0 | Tuberculosis reaction wheal [Diameter] --3 days post dose mammalian tuberculin intradermal | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 80 | Observation | 55277-8 | HIV status | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 81 | Observation | 33248-6 | Diabetes status | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 82 | ServiceRequest | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | SITB TB 06 (3x), SITB TB 03 SO (6x), SITB TB 03 RO (2x), SITB TB 04 (2x) | 4 |
| 83 | Specimen | 119334006 | Sputum specimen | SITB TB 06 (8x), SITB TB 03 SO (9x), SITB TB 03 RO (7x) | 3 |
| 84 | Observation | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | SITB TB 06 (3x), SITB TB 03 SO (6x), SITB TB 03 RO (2x), SITB TB 04 (2x) | 4 |
| 85 | DiagnosticReport | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | SITB TB 06 (3x), SITB TB 03 SO (6x), SITB TB 03 RO (2x), SITB TB 04 (2x) | 4 |
| 86 | ServiceRequest | X099379 | Pemeriksaan TCM XDR | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 04 | 4 |
| 87 | Observation | X099379 | Pemeriksaan TCM XDR | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 04 | 4 |
| 88 | DiagnosticReport | X099379 | Pemeriksaan TCM XDR | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 04 | 4 |
| 89 | ServiceRequest | X099380 | Line Probe Assay (LPA) Lini 1 | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 04 | 4 |
| 90 | Observation | X099380 | Line Probe Assay (LPA) Lini 1 | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 04 | 4 |
| 91 | DiagnosticReport | X099380 | Line Probe Assay (LPA) Lini 1 | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 04 | 4 |
| 92 | ServiceRequest | X099381 | Line Probe Assay (LPA) Lini 2 | SITB TB 06, SITB TB 03 RO, SITB TB 04 | 3 |
| 93 | Observation | X099381 | Line Probe Assay (LPA) Lini 2 | SITB TB 06, SITB TB 03 RO, SITB TB 04 | 3 |
| 94 | DiagnosticReport | X099381 | Line Probe Assay (LPA) Lini 2 | SITB TB 06, SITB TB 03 RO, SITB TB 04 | 3 |
| 95 | ServiceRequest | X099388 | Biakan TB | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 96 | Observation | X099388 | Biakan TB | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 97 | DiagnosticReport | X099388 | Biakan TB | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 98 | ServiceRequest | X099383 | Pemeriksaan Paket Standar Kepekaan | SITB TB 06, SITB TB 03 RO, SITB TB 04 | 3 |
| 99 | Observation | X099383 | Pemeriksaan Paket Standar Kepekaan | SITB TB 06, SITB TB 03 RO, SITB TB 04 | 3 |
| 100 | DiagnosticReport | X099383 | Pemeriksaan Paket Standar Kepekaan | SITB TB 06, SITB TB 03 RO, SITB TB 04 | 3 |
| 101 | Observation | 106229004 | Qualifier for type of diagnosis | SITB TB 06, SITB TB 03 SO, SITB TB 16K | 3 |
| 102 | CarePlan | – | – | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 103 | Observation | 365866002 | Finding of human immunodeficiency virus status | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 104 | Procedure | SP000046 | Terapi Antiretroviral (ART) | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 105 | Observation | SP000047 | Hasil Tes Diabetes Melitus | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 106 | Coverage | – | – | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 107 | Observation | 85658-3 | Occupation [Type] | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 108 | Observation | 82810-3 | Pregnancy status | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 109 | Observation | 225368008 | Contact tracing | SITB TB 03 SO, SITB TB 03 RO, SITB TB 16K | 3 |
| 110 | Procedure | TK000016 | Edukasi Tes HIV | SITB TB 03 SO | 1 |
| 111 | Procedure | SP000371 | Cotrimoxazole | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 112 | Observation | 1284985006 | Diabetes mellitus management program | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 113 | Observation | SP000797 | Pindah Register Pasien TB RO | SITB TB 03 SO | 1 |
| 114 | EpisodeOfCare | TB-RO | Tuberkulosis Resisten Obat | SITB TB 03 RO | 1 |
| 115 | Condition | 171126009 | Tuberculosis screening | SITB TB 04 | 1 |
| 116 | Specimen | 418564007 | Pleural fluid specimen | SITB TB 04 (16x) | 1 |
| 117 | ServiceRequest | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | SITB TB 04 (2x) | 1 |
| 118 | Observation | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | SITB TB 04 (2x) | 1 |
| 119 | DiagnosticReport | SP000720 | Pemeriksaan Xpert MTB RIF (Xpert) | SITB TB 04 (2x) | 1 |
| 120 | ServiceRequest | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | SITB TB 04 (2x) | 1 |
| 121 | Observation | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | SITB TB 04 (2x) | 1 |
| 122 | DiagnosticReport | SP000721 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Plus | SITB TB 04 (2x) | 1 |
| 123 | ServiceRequest | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | SITB TB 04 (2x) | 1 |
| 124 | Observation | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | SITB TB 04 (2x) | 1 |
| 125 | DiagnosticReport | SP000722 | Pemeriksaan Xpert MTB RIF (Truenat) Chip MTB Rif | SITB TB 04 (2x) | 1 |
| 126 | ServiceRequest | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | SITB TB 04 (2x) | 1 |
| 127 | Observation | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | SITB TB 04 (2x) | 1 |
| 128 | DiagnosticReport | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | SITB TB 04 (2x) | 1 |
| 129 | ServiceRequest | MK099927 | Pemeriksaan PCR Open System | SITB TB 04 | 1 |
| 130 | Observation | MK099927 | Pemeriksaan PCR Open System | SITB TB 04 | 1 |
| 131 | DiagnosticReport | MK099927 | Pemeriksaan PCR Open System | SITB TB 04 | 1 |
| 132 | ServiceRequest | X099389 | Hasil Pemeriksaan Biakan TB (Metode: LJ) | SITB TB 04 | 1 |
| 133 | Observation | X099389 | Hasil Pemeriksaan Biakan TB (Metode: LJ) | SITB TB 04 | 1 |
| 134 | DiagnosticReport | X099389 | Hasil Pemeriksaan Biakan TB (Metode: LJ) | SITB TB 04 | 1 |
| 135 | Group | – | – | SITB TB 16K | 1 |
| 136 | Observation | SP000373 | Kader Kesehatan | SITB TB 16K | 1 |
| 137 | RelatedPerson | – | – | SITB TB 16K | 1 |
| 138 | Observation | 415759006 | Tuberculosis index case | SITB TB 16K | 1 |
| 139 | ServiceRequest | 185389009 | Follow-up visit | SITB TB 16K | 1 |
| 140 | Condition | Z20.1 | Contact with and exposure to tuberculosis | SITB TB 16K | 1 |
| 141 | Observation | SP000369 | Kontak Dengan Penderita TBC | SITB TB 16K | 1 |
| 142 | Observation | SP000206 | Dirujuk Pemeriksaan Terduga TBC | SITB TB 16K | 1 |
| 143 | Observation | 171400006 | Examination for suspected tuberculosis | SITB TB 16K | 1 |
| 144 | Observation | SP000207 | Hasil Pemeriksaan Terduga | SITB TB 16K | 1 |
| 145 | Observation | SP000209 | Memenuhi syarat rujukan pemeriksaan Eligibilitas TPT | SITB TB 16K | 1 |
| 146 | Observation | SP000210 | Kesimpulan Hasil Pemeriksaan Eligibilitas TPT | SITB TB 16K | 1 |
| 147 | Observation | SP000212 | Tanggal Pemberian TPT | SITB TB 16K | 1 |
| 148 | Observation | SP000213 | Hasil Akhir TPT | SITB TB 16K | 1 |
| 149 | Observation | 64710-7 | Was your pregnancy a live birth, stillbirth, miscarriage, abortion, or ectopic pregnancy [PhenX] | MPDN Kematian Bayi | 1 |
| 150 | Observation | 39016-1 | Age at death | MPDN Kematian Bayi, MPDN Kematian Ibu | 2 |
| 151 | Observation | OC000028 | Jenis Tempat Meninggal | MPDN Kematian Bayi, MPDN Kematian Ibu | 2 |
| 152 | Observation | SP000098 | Tipe Penyelenggara Faskes Meninggal | MPDN Kematian Bayi, MPDN Kematian Ibu | 2 |
| 153 | Observation | 72150-6 | Delivery location | MPDN Kematian Bayi | 1 |
| 154 | Observation | 57071-3 | Obstetric delivery method | MPDN Kematian Bayi | 1 |
| 155 | Observation | OC000013 | Penolong Persalinan | MPDN Kematian Bayi | 1 |
| 156 | Observation | SP000075 | Tipe Penyelenggara Faskes Lahir | MPDN Kematian Bayi | 1 |
| 157 | Observation | 57715-5 | Birth time | MPDN Kematian Bayi | 1 |
| 158 | Observation | 8339-4 | Birth weight Measured | MPDN Kematian Bayi | 1 |
| 159 | Observation | 11996-6 | [#] Pregnancies | MPDN Kematian Bayi, MPDN Kematian Ibu | 2 |
| 160 | Observation | 57722-1 | Birth plurality of Pregnancy | MPDN Kematian Bayi | 1 |
| 161 | Observation | 30525-0 | Age | MPDN Kematian Bayi | 1 |
| 162 | Composition | – | – | MPDN Kematian Bayi, MPDN Kematian Ibu | 2 |
| 163 | Condition | – | – | MPDN Kematian Ibu | 1 |
| 164 | Observation | OC000026 | Masa terjadi Kematian Ibu | MPDN Kematian Ibu | 1 |

Variabel dictionary / BQ per payload: lihat `output/<form>.md` (link di [`output.md`](output.md)).
