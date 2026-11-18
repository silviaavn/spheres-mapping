# Output Hitungan Payload & Code — Form Kobo & PHDT

Terakhir diperbarui: 2026-11-17
Aturan hitung: lihat `aturan.md`
Form yang sudah dihitung (detail per form, bisa ditelusuri per baris):
- **Maternal Outcome** → `output/maternal-outcome.md` (sumber: `mapping/kobo-data-dictionary-maternal-outcome.csv`)
- **Raffle** → `output/raffle.md` (sumber: `mapping/kobo-data-dictionary-raffle.csv`)
- **SiGizi ANC** → `output/sigizi-anc.md` (sumber: `mapping/phdt-data-dictionary-sigizi-anc.csv`, PHDT Data Dictionary; struktur file mentah: `raw/sigizi-anc-kolom.md`)
- **SITB TB 06** → `output/sitb-tb06.md` (sumber: `mapping/phdt-data-dictionary-sitb-tb06.csv`; file mentah: `raw/sitb-tb06-kolom.md`)
- **SITB TB 03 SO** → `output/sitb-tb03-so.md` (sumber: `mapping/phdt-data-dictionary-sitb-tb03-so.csv`; file mentah: `raw/sitb-tb03-so-kolom.md`)
- **SITB TB 03 RO** → `output/sitb-tb03-ro.md` (sumber: `mapping/phdt-data-dictionary-sitb-tb03-ro.csv`; file mentah: `raw/sitb-tb03-ro-kolom.md`)
- **SITB TB 04** (Fasyankes & Rujukan) → `output/sitb-tb04.md` (sumber: `mapping/phdt-data-dictionary-sitb-tb04.csv`; file mentah: `raw/sitb-tb04-kolom.md`)
- **SITB TB 16K** → `output/sitb-tb16k.md` (sumber: `mapping/phdt-data-dictionary-sitb-tb16k.csv`; file mentah: `raw/sitb-tb16k-kolom.md`)

File ini adalah **konsolidasi** lintas form. Angka per form di sini harus sama dengan file `output/<form>.md`.

Belum: PNC, SITB TB 13 SO/RO, form lain

---

## Ringkasan semua form

| Form | Payload | Code |
|---|---|---|
| Maternal Outcome | 12 | 14 |
| Raffle | 8 | 6 |
| SiGizi ANC | 61 | 142 |
| SITB TB 06 | 56 | 276 |
| SITB TB 03 SO | 62 | 329 |
| SITB TB 03 RO | 50 | 377 |
| SITB TB 04 | 69 | 579 |
| SITB TB 16K | 21 | 35 |
| **Total (non-unik)** | **339** | **1758** |
| **Total unik** | **148** | **434** |
| Selisih (dipakai ulang) | 191 | 1324 |

---

## Frekuensi payload (lintas form)

Frekuensi = di berapa form dipakai. Angka (Nx) = muncul N kali di form itu.

| # | Resource | Code pembeda | Display | Dipakai di form | Frekuensi |
|---|---|---|---|---|---|
| 1 | PractitionerRole | – | – | Maternal Outcome, SiGizi ANC | 2 |
| 2 | Practitioner | – | – | Maternal Outcome, Raffle (2x) | 2 |
| 3 | Patient | – | – | Maternal Outcome, Raffle, SiGizi ANC, SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 04, SITB TB 16K | 8 |
| 4 | Encounter | – | – | Maternal Outcome, Raffle, SiGizi ANC, SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 04, SITB TB 16K | 8 |
| 5 | Condition | SP000738 | Kunjungan pemantauan luaran maternal | Maternal Outcome | 1 |
| 6 | EpisodeOfCare | ANC | Antenatal Care | Maternal Outcome, Raffle, SiGizi ANC | 3 |
| 7 | EpisodeOfCare | PNC | Postnatal Care | Maternal Outcome | 1 |
| 8 | Observation | SP000389 | Keadaan Ibu | Maternal Outcome | 1 |
| 9 | Observation | 93857-1 | Date and time of obstetric delivery | Maternal Outcome | 1 |
| 10 | Observation | 81956-5 | Date and time of death [TimeStamp] | Maternal Outcome | 1 |
| 11 | Observation | LT000005 | Alamat Mati | Maternal Outcome | 1 |
| 12 | Observation | 79378-6 | Cause of death | Maternal Outcome | 1 |
| 13 | Location | – | – | Raffle, SITB TB 06 | 2 |
| 14 | Condition | SP001135 | Presensi Posyandu | Raffle | 1 |
| 15 | Observation | 385438008 | Source of information | Raffle | 1 |
| 16 | Condition | 134435003 | Routine antenatal care | SiGizi ANC | 1 |
| 17 | Observation | 424144002 | Current chronological age | SiGizi ANC, SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 04, SITB TB 16K (2x) | 6 |
| 18 | Observation | 8665-2 | Last menstrual period start date | SiGizi ANC | 1 |
| 19 | Observation | 18185-9 | Gestational age | SiGizi ANC | 1 |
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

Variabel dictionary / BQ per payload: lihat `output/<form>.md`.

## Frekuensi code (lintas form)

| # | Code | Display | CodeSystem | Dipakai di form | Frekuensi |
|---|---|---|---|---|---|
| 1 | 223366009 | Healthcare professional | snomed | Maternal Outcome, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 2 | SP000396 | Data entry staff | kemkes sp | Maternal Outcome | 1 |
| 3 | SP000397 | Field/call center staff | kemkes sp | Maternal Outcome | 1 |
| 4 | SP000738 | Kunjungan pemantauan luaran maternal | kemkes sp | Maternal Outcome | 1 |
| 5 | ANC | Antenatal Care | episodeofcare-type | Maternal Outcome, Raffle, SiGizi ANC | 3 |
| 6 | PNC | Postnatal Care | episodeofcare-type | Maternal Outcome | 1 |
| 7 | SP000389 | Keadaan Ibu | kemkes sp | Maternal Outcome | 1 |
| 8 | 102514002 | Well female adult | snomed | Maternal Outcome | 1 |
| 9 | 39104002 | Illness | snomed | Maternal Outcome | 1 |
| 10 | 419099009 | Dead | snomed | Maternal Outcome, SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 16K | 5 |
| 11 | 93857-1 | Date and time of obstetric delivery | loinc | Maternal Outcome | 1 |
| 12 | 81956-5 | Date and time of death [TimeStamp] | loinc | Maternal Outcome | 1 |
| 13 | LT000005 | Alamat Mati | location-type | Maternal Outcome | 1 |
| 14 | 79378-6 | Cause of death | loinc | Maternal Outcome | 1 |
| 15 | SP001135 | Presensi Posyandu | kemkes sp | Raffle | 1 |
| 16 | 385438008 | Source of information | snomed | Raffle | 1 |
| 17 | SP000776 | Sigizi | kemkes sp | Raffle | 1 |
| 18 | SP000777 | E-pus PKD | kemkes sp | Raffle | 1 |
| 19 | SP000778 | E-pus | kemkes sp | Raffle | 1 |
| 20 | 309453006 | Registered midwife | snomed | SiGizi ANC | 1 |
| 21 | 309343006 | Physician | snomed | SiGizi ANC | 1 |
| 22 | 309367003 | Obstetrician and gynecologist | snomed | SiGizi ANC | 1 |
| 23 | 224535009 | Registered nurse | snomed | SiGizi ANC | 1 |
| 24 | K1M | Tidak ada | episodeofcare/ANC | SiGizi ANC | 1 |
| 25 | K1A | Tidak ada | episodeofcare/ANC | SiGizi ANC | 1 |
| 26 | 134435003 | Routine antenatal care | snomed | SiGizi ANC | 1 |
| 27 | 424144002 | Current chronological age | snomed | SiGizi ANC, SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 04, SITB TB 16K (2x) | 6 |
| 28 | 8665-2 | Last menstrual period start date | loinc | SiGizi ANC | 1 |
| 29 | ANC.B6.DE14 | Last menstrual period (LMP) date | WHO anc-custom-codes | SiGizi ANC | 1 |
| 30 | 18185-9 | Gestational age | loinc | SiGizi ANC | 1 |
| 31 | 11778-8 | Delivery date Estimated | loinc | SiGizi ANC | 1 |
| 32 | ANC.B6.DE22 | Expected date of delivery (EDD) | WHO anc-custom-codes | SiGizi ANC | 1 |
| 33 | 8302-2 | Body height | loinc | SiGizi ANC | 1 |
| 34 | ANC.B8.DE1 | Height | WHO anc-custom-codes | SiGizi ANC | 1 |
| 35 | OC000010 | Indeks Massa Tubuh Sebelum Hamil | kemkes clinical-term | SiGizi ANC | 1 |
| 36 | ANC.SS.DE58 | IMT Sebelum Hamil | kemkes anc-custom-codes | SiGizi ANC | 1 |
| 37 | VG139 | Td | kfa | SiGizi ANC | 1 |
| 38 | SP000001 | Skrining Imunisasi Tetanus Toksoid | kemkes sp | SiGizi ANC | 1 |
| 39 | SP000002 | Kunjungan Pertama Pemeriksaan Kehamilan | kemkes sp | SiGizi ANC | 1 |
| 40 | 29463-7 | Body weight | loinc | SiGizi ANC | 1 |
| 41 | ANC.B8.DE3 | Current weight | WHO anc-custom-codes | SiGizi ANC | 1 |
| 42 | 392570002 | Blood pressure finding | snomed | SiGizi ANC | 1 |
| 43 | 2004005 | Normal blood pressure | snomed | SiGizi ANC | 1 |
| 44 | 38341003 | Hypertension | snomed | SiGizi ANC | 1 |
| 45 | 45007003 | Hypotension | snomed | SiGizi ANC | 1 |
| 46 | 284473002 | Mid upper arm circumference | snomed | SiGizi ANC | 1 |
| 47 | ANC.SS.DE3 | Lingkar Lengan Atas (LILA) | kemkes anc-custom-codes | SiGizi ANC | 1 |
| 48 | OI000018 | Kurang Energi Kronis (KEK) | kemkes clinical-term | SiGizi ANC | 1 |
| 49 | N | Normal | v3-ObservationInterpretation | SiGizi ANC | 1 |
| 50 | OI000035 | Risiko Kurang Energi Kronis (KEK) | kemkes clinical-term | SiGizi ANC | 1 |
| 51 | 289625003 | Finding of fundal height of uterus | snomed | SiGizi ANC | 1 |
| 52 | SP000003 | Sesuai Usia Kehamilan | kemkes sp | SiGizi ANC | 1 |
| 53 | SP000004 | Tidak Sesuai Usia Kehamilan | kemkes sp | SiGizi ANC | 1 |
| 54 | 883-9 | ABO group [Type] in Blood | loinc | SiGizi ANC | 1 |
| 55 | ANC.B9.DE24 | Blood type | WHO anc-custom-codes | SiGizi ANC | 1 |
| 56 | LA19710-5 | Group A | loinc | SiGizi ANC | 1 |
| 57 | LA19709-7 | Group B | loinc | SiGizi ANC | 1 |
| 58 | LA19708-9 | Group O | loinc | SiGizi ANC | 1 |
| 59 | LA28449-9 | Group AB | loinc | SiGizi ANC | 1 |
| 60 | 10331-7 | Rh [Type] in Blood | loinc | SiGizi ANC | 1 |
| 61 | ANC.B9.DE29 | Rh factor | WHO anc-custom-codes | SiGizi ANC | 1 |
| 62 | LA6576-8 | Positive | loinc | SiGizi ANC (4x), SITB TB 06 (4x), SITB TB 03 SO (3x), SITB TB 03 RO (4x), SITB TB 04 (3x) | 5 |
| 63 | LA6577-6 | Negative | loinc | SiGizi ANC (4x), SITB TB 06 (5x), SITB TB 03 SO (4x), SITB TB 03 RO (5x), SITB TB 04 (7x) | 5 |
| 64 | 289437007 | Finding of fetal heart rate | snomed | SiGizi ANC | 1 |
| 65 | 289441006 | Normal fetal heart rate | snomed | SiGizi ANC | 1 |
| 66 | 289440007 | Fetal heart rate not observed | snomed | SiGizi ANC | 1 |
| 67 | 312668007 | Abnormal fetal heart rate | snomed | SiGizi ANC | 1 |
| 68 | 289439005 | Fetal heart rate absent | snomed | SiGizi ANC | 1 |
| 69 | 72155-5 | Position in womb Fetus [RHEA] | loinc | SiGizi ANC | 1 |
| 70 | ANC.B8.DE111 | Fetal presentation | WHO anc-custom-codes | SiGizi ANC | 1 |
| 71 | 1209182005 | Cephalic fetal presentation | snomed | SiGizi ANC | 1 |
| 72 | SP000005 | Letak Bokong/ Lintang | kemkes sp | SiGizi ANC | 1 |
| 73 | SP000006 | Organ Tubuh Lainnya | kemkes sp | SiGizi ANC | 1 |
| 74 | 88.78 | Diagnostic ultrasound of gravid uterus | icd-9-cm | SiGizi ANC | 1 |
| 75 | 268445003 | Ultrasound scan - obstetric | snomed | SiGizi ANC | 1 |
| 76 | 169221005 | Ultrasound obstetric scan normal | snomed | SiGizi ANC | 1 |
| 77 | 169255008 | Ultrasound scan abnormal | snomed | SiGizi ANC | 1 |
| 78 | 92000653 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula | kfa | SiGizi ANC | 1 |
| 79 | 93015491 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | kfa | SiGizi ANC | 1 |
| 80 | SP000370 | Multiple Micronutrient Supplement | kemkes sp | SiGizi ANC (2x) | 1 |
| 81 | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | loinc | SiGizi ANC (3x) | 1 |
| 82 | 122555007 | Venous blood specimen | snomed | SiGizi ANC (5x) | 1 |
| 83 | ANC.B9.DE32 | HIV test | WHO anc-custom-codes | SiGizi ANC | 1 |
| 84 | LA15255-5 | Reactive | loinc | SiGizi ANC | 1 |
| 85 | LA15256-3 | Nonreactive | loinc | SiGizi ANC | 1 |
| 86 | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | loinc | SiGizi ANC (3x) | 1 |
| 87 | ANC.B9.DE60 | Hepatitis B test conducted | WHO anc-custom-codes | SiGizi ANC | 1 |
| 88 | 22464-2 | Reagin Ab [Presence] in Specimen | loinc | SiGizi ANC (3x) | 1 |
| 89 | ANC.B9.DE96 | Syphilis test conducted | WHO anc-custom-codes | SiGizi ANC | 1 |
| 90 | 2887-8 | Protein [Presence] in Urine | loinc | SiGizi ANC (3x) | 1 |
| 91 | 122575003 | Urine specimen | snomed | SiGizi ANC | 1 |
| 92 | ANC.B9.DE114 | Urine test conducted | WHO anc-custom-codes | SiGizi ANC | 1 |
| 93 | 718-7 | Hemoglobin [Mass/volume] in Blood | loinc | SiGizi ANC (3x) | 1 |
| 94 | ANC.B9.DE175 | Blood hemoglobin test conducted | WHO anc-custom-codes | SiGizi ANC | 1 |
| 95 | 860635002 | No anemia present | snomed | SiGizi ANC | 1 |
| 96 | OI000032 | Anemia ringan | kemkes clinical-term | SiGizi ANC | 1 |
| 97 | OI000033 | Anemia sedang | kemkes clinical-term | SiGizi ANC | 1 |
| 98 | OI000034 | Anemia berat | kemkes clinical-term | SiGizi ANC | 1 |
| 99 | 74774-1 | Glucose [Mass/volume] in Serum, Plasma or Blood | loinc | SiGizi ANC (3x) | 1 |
| 100 | ANC.B9.DE159 | Blood glucose test conducted | WHO anc-custom-codes | SiGizi ANC | 1 |
| 101 | 166921001 | Blood glucose normal | snomed | SiGizi ANC | 1 |
| 102 | 166922008 | Blood glucose abnormal | snomed | SiGizi ANC | 1 |
| 103 | 15220000 | Laboratory test | snomed | SiGizi ANC | 1 |
| 104 | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | loinc | SiGizi ANC, SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 04 | 5 |
| 105 | 76772-3 | Plasmodium falciparum Ag [Presence] in Blood by Rapid immunoassay | loinc | SiGizi ANC | 1 |
| 106 | 104742-2 | Ova and parasites identified in Specimen | loinc | SiGizi ANC | 1 |
| 107 | 74964007 | Other | snomed | SiGizi ANC (4x), SITB TB 03 SO (3x), SITB TB 03 RO (2x) | 3 |
| 108 | SP000007 | Tatalaksana Anemia | kemkes sp | SiGizi ANC | 1 |
| 109 | SP000008 | Pemberian Tablet Tambah Darah | kemkes sp | SiGizi ANC | 1 |
| 110 | SP000009 | Pemberian Fe Parenteral | kemkes sp | SiGizi ANC | 1 |
| 111 | 116859006 | Transfusion of blood product | snomed | SiGizi ANC | 1 |
| 112 | 3457005 | Patient referral | snomed | SiGizi ANC (3x) | 1 |
| 113 | SP000010 | Skrining Hipertensi dalam Kehamilan | kemkes sp | SiGizi ANC | 1 |
| 114 | SP000011 | Tidak Pre Eklampsia/ Eklampsia | kemkes sp | SiGizi ANC | 1 |
| 115 | 48194001 | Pregnancy-induced hypertension | snomed | SiGizi ANC | 1 |
| 116 | 398254007 | Pre-eclampsia | snomed | SiGizi ANC | 1 |
| 117 | 15938005 | Eclampsia | snomed | SiGizi ANC | 1 |
| 118 | SP000012 | Tatalaksana Pre Eklampsia | kemkes sp | SiGizi ANC | 1 |
| 119 | 135840009 | Blood pressure monitoring | snomed | SiGizi ANC | 1 |
| 120 | 308116003 | Antihypertensive therapy | snomed | SiGizi ANC | 1 |
| 121 | SP000013 | Pemberian MgSO4 | kemkes sp | SiGizi ANC | 1 |
| 122 | SP000014 | Tatalaksana KEK | kemkes sp | SiGizi ANC | 1 |
| 123 | 435591000124104 | Nutrition supplement therapy | snomed | SiGizi ANC | 1 |
| 124 | SP000015 | Risiko Masalah Kesehatan | kemkes sp | SiGizi ANC | 1 |
| 125 | 40733004 | Infectious disease | snomed | SiGizi ANC | 1 |
| 126 | 73211009 | Diabetes mellitus | snomed | SiGizi ANC | 1 |
| 127 | 414916001 | Obesity | snomed | SiGizi ANC | 1 |
| 128 | 56717001 | Tuberculosis | snomed | SiGizi ANC, SITB TB 16K | 2 |
| 129 | 56265001 | Heart disease | snomed | SiGizi ANC | 1 |
| 130 | SP000016 | Tatalaksana Masalah Kesehatan | kemkes sp | SiGizi ANC | 1 |
| 131 | 1230101008 | Counseling for pregnancy | snomed | SiGizi ANC | 1 |
| 132 | 385892002 | Mental health screening | snomed | SiGizi ANC | 1 |
| 133 | TB-SO | Tuberkulosis Sensitif Obat | episodeofcare-type | SITB TB 06 (3x), SITB TB 03 SO, SITB TB 04, SITB TB 16K | 4 |
| 134 | TB-RO | Tuberkulosis Resisten Obat | episodeofcare-type | SITB TB 06 (3x), SITB TB 03 RO, SITB TB 04, SITB TB 16K | 4 |
| 135 | EHA000001 | Kader/ Komunitas | kemkes clinical-term | SITB TB 06 | 1 |
| 136 | EHA000002 | Datang sendiri | kemkes clinical-term | SITB TB 06, SITB TB 03 SO (2x), SITB TB 03 RO (2x), SITB TB 04 | 4 |
| 137 | EHA000003 | Kegiatan ACF | kemkes clinical-term | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 138 | 257622000 | Healthcare facility | snomed | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 04 | 4 |
| 139 | EHA000004 | Skrining TBC DM | kemkes clinical-term | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 140 | EHA000005 | Pemadanan Data BPJS | kemkes clinical-term | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 141 | Z03.0 | Observation for suspected tuberculosis | icd-10 | SITB TB 06 | 1 |
| 142 | A15.0 | Tuberculosis of lung, confirmed by sputum microscopy with or without culture | icd-10 | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 143 | A16.2 | Tuberculosis of lung, without mention of bacteriological or histological confirmation | icd-10 | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 144 | QRI000001 | Terduga TBC SO | kemkes clinical-term | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 145 | QRI000002 | Terduga TBC RO | kemkes clinical-term | SITB TB 06, SITB TB 03 RO | 2 |
| 146 | new | Kasus Baru | kemkes prev-tb-treatment | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 147 | relapse | Kasus Kambuh | kemkes prev-tb-treatment | SITB TB 06 (2x), SITB TB 03 SO, SITB TB 03 RO (2x) | 3 |
| 148 | failure-cat1 | Kasus Pengobatan Setelah Gagal Kategori 1 | kemkes prev-tb-treatment | SITB TB 06 (2x), SITB TB 03 SO, SITB TB 03 RO (2x) | 3 |
| 149 | failure-cat2 | Kasus Pengobatan Setelah Gagal Kategori 2 | kemkes prev-tb-treatment | SITB TB 06 (2x), SITB TB 03 SO, SITB TB 03 RO (2x) | 3 |
| 150 | loss-to-follow-up | Kasus Setelah Loss To Follow Up | kemkes prev-tb-treatment | SITB TB 06 (2x), SITB TB 03 SO, SITB TB 03 RO (2x) | 3 |
| 151 | failure-2line | Kasus Pengobatan Setelah Gagal lini 2 | kemkes prev-tb-treatment | SITB TB 06 (2x), SITB TB 03 SO, SITB TB 03 RO (2x) | 3 |
| 152 | not-eval | Pernah diobati tidak diketahui hasilnya | kemkes prev-tb-treatment | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 153 | unknown | Kasus dengan riwayat pengobatan tidak diketahui | kemkes prev-tb-treatment | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 154 | other | Kasus lain-lain | kemkes prev-tb-treatment | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 155 | failure | Kasus Pengobatan Setelah Gagal | kemkes prev-tb-treatment | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 156 | treatment-non-conversion-2 | Pasien TB pengobatan kategori 2 yang tidak konversi setelah 3 bulan pengobatan | kemkes prev-tb-treatment | SITB TB 06, SITB TB 03 RO | 2 |
| 157 | non-standard-treatment | Pasien TB yang mempunyai riwayat pengobatan TB yang tidak standar | kemkes prev-tb-treatment | SITB TB 06, SITB TB 03 RO | 2 |
| 158 | treatment-non-conversion-1 | Pasien TB pengobatan kategori 1 yang tidak konversi | kemkes prev-tb-treatment | SITB TB 06, SITB TB 03 RO | 2 |
| 159 | history-of-close-contact with-TB-DR | Terduga TB yang mempunyai riwayat kontak erat dengan pasien TB RO | kemkes prev-tb-treatment | SITB TB 06, SITB TB 03 RO | 2 |
| 160 | co-infected-TBHIV | Pasien ko-infeksi TB-HIV yang tidak respons secara klinis maupun bakteriologis terhadap pemberian OAT | kemkes prev-tb-treatment | SITB TB 06, SITB TB 03 RO | 2 |
| 161 | TB-DR-relapse | Pasien TB RO kasus kambuh | kemkes prev-tb-treatment | SITB TB 06, SITB TB 03 RO | 2 |
| 162 | TB-DR-returns | Pasien TB RO yang kembali setelah putus berobat | kemkes prev-tb-treatment | SITB TB 06, SITB TB 03 RO | 2 |
| 163 | 154283005 | Pulmonary tuberculosis | snomed | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 164 | 423997002 | Tuberculosis, extrapulmonary | snomed | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 165 | OC000191 | Jumlah Skoring TBC Anak | kemkes clinical-term | SITB TB 06, SITB TB 03 SO | 2 |
| 166 | 24648-8 | XR Chest PA upright | loinc | SITB TB 06 (3x), SITB TB 03 SO, SITB TB 03 RO | 3 |
| 167 | 707307002 | Tuberculosis screening chest X-ray abnormal | snomed | SITB TB 06, SITB TB 03 SO | 2 |
| 168 | 707308007 | Tuberculosis screening chest X-ray normal | snomed | SITB TB 06, SITB TB 03 SO | 2 |
| 169 | 424489006 | Mantoux test | snomed | SITB TB 06 (2x), SITB TB 03 SO (2x), SITB TB 03 RO (2x) | 3 |
| 170 | 35140007 | Interferon gamma assay | snomed | SITB TB 06 (2x), SITB TB 03 SO (2x), SITB TB 03 RO (2x) | 3 |
| 171 | 23539-0 | Tuberculosis reaction wheal [Diameter] --3 days post dose mammalian tuberculin intradermal | loinc | SITB TB 06 (2x), SITB TB 03 SO (2x), SITB TB 03 RO (2x) | 3 |
| 172 | 268376005 | Mantoux: positive | snomed | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 173 | 268375009 | Mantoux: negative | snomed | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 174 | 71773-6 | Mycobacterium tuberculosis stimulated gamma interferon [Interpretation] in Blood Qualitative | loinc | SITB TB 06 (2x), SITB TB 03 SO (2x), SITB TB 03 RO (2x) | 3 |
| 175 | 55277-8 | HIV status | loinc | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 176 | 10828004 | Positive | snomed | SITB TB 06 (3x), SITB TB 03 SO (3x), SITB TB 03 RO (3x) | 3 |
| 177 | 260385009 | Negative | snomed | SITB TB 06 (5x), SITB TB 03 SO (8x), SITB TB 03 RO (4x), SITB TB 04 (2x) | 4 |
| 178 | 261665006 | Unknown | snomed | SITB TB 06 (2x), SITB TB 03 SO (3x), SITB TB 03 RO (3x) | 3 |
| 179 | 33248-6 | Diabetes status | loinc | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 180 | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | loinc | SITB TB 06 (9x), SITB TB 03 SO (18x), SITB TB 03 RO (6x), SITB TB 04 (6x) | 4 |
| 181 | 119334006 | Sputum specimen | snomed | SITB TB 06 (8x), SITB TB 03 SO (9x), SITB TB 03 RO (7x), SITB TB 04 (32x) | 4 |
| 182 | LA11841-6 | 1+ | loinc | SITB TB 06 (3x), SITB TB 03 SO (6x), SITB TB 03 RO (2x), SITB TB 04 (3x) | 4 |
| 183 | LA11842-4 | 2+ | loinc | SITB TB 06 (3x), SITB TB 03 SO (6x), SITB TB 03 RO (2x), SITB TB 04 (3x) | 4 |
| 184 | LA11843-2 | 3+ | loinc | SITB TB 06 (3x), SITB TB 03 SO (6x), SITB TB 03 RO (2x), SITB TB 04 (3x) | 4 |
| 185 | 89371-9 | MTB complex DNA and rpoB RIF resistance mutation panel [Presence] | loinc | SITB TB 06 (3x), SITB TB 03 SO (3x), SITB TB 03 RO | 3 |
| 186 | X099379 | Pemeriksaan TCM XDR | kemkes examination | SITB TB 06 (6x), SITB TB 03 SO (6x), SITB TB 03 RO (4x), SITB TB 04 (3x) | 4 |
| 187 | X099380 | Line Probe Assay (LPA) Lini 1 | kemkes examination | SITB TB 06 (6x), SITB TB 03 SO (6x), SITB TB 03 RO (4x), SITB TB 04 (3x) | 4 |
| 188 | X099381 | Line Probe Assay (LPA) Lini 2 | kemkes examination | SITB TB 06 (6x), SITB TB 03 SO (3x), SITB TB 03 RO (4x), SITB TB 04 (3x) | 4 |
| 189 | X099388 | Biakan TB | kemkes examination | SITB TB 06 (6x), SITB TB 03 SO (6x), SITB TB 03 RO (4x) | 3 |
| 190 | X099383 | Pemeriksaan Paket Standar Kepekaan | kemkes examination | SITB TB 06 (6x), SITB TB 03 SO (3x), SITB TB 03 RO (4x), SITB TB 04 (3x) | 4 |
| 191 | MK099926 | Pemeriksaan TCM MTB Rif INH (BDMAX) | kemkes examination | SITB TB 06 (3x), SITB TB 03 SO (3x), SITB TB 03 RO, SITB TB 04 (6x) | 4 |
| 192 | MK099927 | Pemeriksaan PCR Open System | kemkes examination | SITB TB 06 (3x), SITB TB 03 SO (3x), SITB TB 03 RO, SITB TB 04 (3x) | 4 |
| 193 | X099770 | Rifampisin sensitive | kemkes examination | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 04 (4x) | 4 |
| 194 | X099771 | Rifampisin resistan | kemkes examination | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 04 (4x) | 4 |
| 195 | X099772 | Rifampisin indeterminate | kemkes examination | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 04 (4x) | 4 |
| 196 | X099781 | Hasil Valid | kemkes examination | SITB TB 06 (3x), SITB TB 03 SO (2x), SITB TB 03 RO (3x), SITB TB 04 (3x) | 4 |
| 197 | LA11882-0 | Detected | loinc | SITB TB 06 (17x), SITB TB 03 SO (11x), SITB TB 03 RO (18x), SITB TB 04 (26x) | 4 |
| 198 | LA11883-8 | Not detected | loinc | SITB TB 06 (17x), SITB TB 03 SO (11x), SITB TB 03 RO (17x), SITB TB 04 (26x) | 4 |
| 199 | X099391 | H Dosis Rendah (Low) | kemkes examination | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 04 (2x) | 4 |
| 200 | LA11884-6 | Indeterminate | loinc | SITB TB 06 (15x), SITB TB 03 SO (9x), SITB TB 03 RO (15x), SITB TB 04 (18x) | 4 |
| 201 | 89488-1 | Isoniazid [Susceptibility] by Genotype method | loinc | SITB TB 06 (2x), SITB TB 03 SO (2x), SITB TB 03 RO (2x), SITB TB 04 (2x) | 4 |
| 202 | 96110-2 | Ethionamide [Susceptibility] by Genotype method | loinc | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 04 (2x) | 4 |
| 203 | X099392 | FQ Dosis Rendah (Low) | kemkes examination | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 04 | 4 |
| 204 | 89487-3 | Fluoroquinolone [Susceptibility] by Genotype method | loinc | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 04 | 4 |
| 205 | 89484-0 | Amikacin [Susceptibility] by Genotype method | loinc | SITB TB 06 (2x), SITB TB 03 SO, SITB TB 03 RO (2x), SITB TB 04 (2x) | 4 |
| 206 | 89482-4 | Kanamycin [Susceptibility] by Genotype method | loinc | SITB TB 06 (2x), SITB TB 03 SO, SITB TB 03 RO (2x), SITB TB 04 (2x) | 4 |
| 207 | 89483-2 | Capreomycin [Susceptibility] by Genotype method | loinc | SITB TB 06 (2x), SITB TB 03 SO, SITB TB 03 RO (2x), SITB TB 04 (2x) | 4 |
| 208 | 13956-8 | Mycobacterium tuberculosis DNA [Presence] in Specimen by NAA with probe detection | loinc | SITB TB 06 (2x), SITB TB 03 SO, SITB TB 03 RO (2x), SITB TB 04 (3x) | 4 |
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
| 231 | 106229004 | Qualifier for type of diagnosis | snomed | SITB TB 06, SITB TB 03 SO, SITB TB 16K | 3 |
| 232 | tb-bac | Terkonfirmasi bakteriologis | kemkes tb-case-definition | SITB TB 06, SITB TB 03 SO, SITB TB 16K | 3 |
| 233 | tb-clin | Terdiagnosis klinis | kemkes tb-case-definition | SITB TB 06, SITB TB 03 SO, SITB TB 16K | 3 |
| 234 | TK000022 | Akan diobati/dirujuk | kemkes | SITB TB 06 | 1 |
| 235 | 699618001 | Administration of prophylactic antituberculosis agent | snomed | SITB TB 06 | 1 |
| 236 | 266714009 | Previous treatment continue | snomed | SITB TB 06 | 1 |
| 237 | SP001136 | Belum Mulai Pengobatan | kemkes sp | SITB TB 06 | 1 |
| 238 | 406149000 | Medication declined | snomed | SITB TB 06 | 1 |
| 239 | 399307001 | Lost to follow-up | snomed | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO, SITB TB 16K | 4 |
| 240 | 365866002 | Finding of human immunodeficiency virus status | snomed | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 241 | 165816005 | Human immunodeficiency virus detected | snomed | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 242 | 165815009 | Human immunodeficiency virus not detected | snomed | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 243 | SP000046 | Terapi Antiretroviral (ART) | kemkes sp | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 244 | SP000047 | Hasil Tes Diabetes Melitus | kemkes sp | SITB TB 06, SITB TB 03 SO, SITB TB 03 RO | 3 |
| 245 | 225368008 | Contact tracing | snomed | SITB TB 03 SO (2x), SITB TB 03 RO (2x), SITB TB 16K | 3 |
| 246 | 85658-3 | Occupation [Type] | loinc | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 247 | 106540006 | Laborer | snomed | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 248 | 106304008 | Teacher | snomed | SITB TB 03 SO (2x), SITB TB 03 RO (2x) | 2 |
| 249 | 106305009 | University/higher education teacher | snomed | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 250 | 444168002 | Homemaker | snomed | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 251 | OV000430 | Pegawai Swasta/ BUMN/ BUMD | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 252 | 65853000 | Student | snomed | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 253 | 106386007 | Agricultural animal husbandry/forestry worker, fisherman/hunter | snomed | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 254 | 106388008 | Farmer | snomed | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 255 | 36625000 | Livestock worker | snomed | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 256 | 77715000 | Fisherman | snomed | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 257 | 236297007 | Civil servant | snomed | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 258 | OV000431 | Siswa Berasrama | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 259 | 236320001 | Vehicle driver (occupation) | snomed | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 260 | OV000432 | Tenaga Profesional Nonmedis | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 261 | OV000433 | TNI/ Polri | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 262 | OV000434 | Warga Binaan Pemasyarakatan | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 263 | 160906004 | Self-employed | snomed | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 264 | 741062008 | Not in labor force | snomed | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 265 | 82810-3 | Pregnancy status | loinc | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 266 | LA15173-0 | Pregnant | loinc | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 267 | LA26683-5 | Not Pregnant | loinc | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 268 | CP000006 | Paduan OAT | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 269 | CP000007 | OAT Kategori 1 | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 270 | CP000008 | OAT Kategori 2 | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 271 | CP000009 | OAT Kategori Anak | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO | 2 |
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
| 355 | SP000795 | Sumber Obat | kemkes sp | SITB TB 03 SO | 1 |
| 356 | SP000791 | Program TBC | kemkes sp | SITB TB 03 SO | 1 |
| 357 | SP000792 | Asuransi | kemkes sp | SITB TB 03 SO | 1 |
| 358 | SP000793 | Bayar Sendiri | kemkes sp | SITB TB 03 SO | 1 |
| 359 | 371001000 | Patient cured | snomed | SITB TB 03 SO, SITB TB 03 RO, SITB TB 16K | 3 |
| 360 | 182992009 | Treatment completed | snomed | SITB TB 03 SO, SITB TB 03 RO, SITB TB 16K | 3 |
| 361 | CP000094 | Pengobatan Gagal | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO, SITB TB 16K | 3 |
| 362 | CP000096 | Tidak dievaluasi/pindah | kemkes clinical-term | SITB TB 03 SO, SITB TB 03 RO, SITB TB 16K | 3 |
| 363 | TK000016 | Edukasi Tes HIV | kemkes | SITB TB 03 SO | 1 |
| 364 | SP000371 | Cotrimoxazole | kemkes sp | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 365 | 1284985006 | Diabetes mellitus management program | snomed | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 366 | SP000372 | Obat Hipoglikemik Oral | kemkes sp | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 367 | 308755006 | Subcutaneous injection of insulin | snomed | SITB TB 03 SO, SITB TB 03 RO | 2 |
| 368 | SP000797 | Pindah Register Pasien TB RO | kemkes sp | SITB TB 03 SO | 1 |
| 369 | 17621005 | Normal | snomed | SITB TB 03 RO | 1 |
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
| 389 | SRR000013 | Pemeriksaan Diagnosis Baseline | kemkes clinical-term | SITB TB 04 (16x) | 1 |
| 390 | SRR000007 | Pemeriksaan Diagnosis | kemkes clinical-term | SITB TB 04 (32x) | 1 |
| 391 | SRR000009 | Pemeriksaan Ulang | kemkes clinical-term | SITB TB 04 (48x) | 1 |
| 392 | SRR000008 | Follow Up | kemkes clinical-term | SITB TB 04 (48x) | 1 |
| 393 | SRR000010 | Akhir Pengobatan | kemkes clinical-term | SITB TB 04 (16x) | 1 |
| 394 | 418564007 | Pleural fluid specimen | snomed | SITB TB 04 (16x) | 1 |
| 395 | 258450006 | Cerebrospinal fluid specimen | snomed | SITB TB 04 (16x) | 1 |
| 396 | 119376003 | Tissue specimen | snomed | SITB TB 04 (16x) | 1 |
| 397 | 309508006 | Soft tissue lesion fine needle aspirate specimen | snomed | SITB TB 04 (16x) | 1 |
| 398 | 168137004 | Gastric aspirate specimen | snomed | SITB TB 04 (16x) | 1 |
| 399 | 119303007 | Microbial isolate specimen | snomed | SITB TB 04 (16x) | 1 |
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
| 415 | SP000373 | Kader Kesehatan | kemkes sp | SITB TB 16K | 1 |
| 416 | 415759006 | Tuberculosis index case | snomed | SITB TB 16K | 1 |
| 417 | 185389009 | Follow-up visit | snomed | SITB TB 16K | 1 |
| 418 | 737492002 | Outpatient care management | snomed | SITB TB 16K | 1 |
| 419 | Z20.1 | Contact with and exposure to tuberculosis | icd-10 | SITB TB 16K | 1 |
| 420 | SP000200 | Invitasi kontak | kemkes sp | SITB TB 16K | 1 |
| 421 | 439708006 | Home visit | snomed | SITB TB 16K | 1 |
| 422 | SP000369 | Kontak Dengan Penderita TBC | kemkes sp | SITB TB 16K | 1 |
| 423 | SP000201 | Kontak Serumah | kemkes sp | SITB TB 16K | 1 |
| 424 | SP000202 | Kontak Erat | kemkes sp | SITB TB 16K | 1 |
| 425 | SP000206 | Dirujuk Pemeriksaan Terduga TBC | kemkes sp | SITB TB 16K | 1 |
| 426 | 171400006 | Examination for suspected tuberculosis | snomed | SITB TB 16K | 1 |
| 427 | SP000207 | Hasil Pemeriksaan Terduga | kemkes sp | SITB TB 16K | 1 |
| 428 | SP000208 | Tidak TBC | kemkes sp | SITB TB 16K | 1 |
| 429 | SP000209 | Memenuhi syarat rujukan pemeriksaan Eligibilitas TPT | kemkes sp | SITB TB 16K | 1 |
| 430 | SP000210 | Kesimpulan Hasil Pemeriksaan Eligibilitas TPT | kemkes sp | SITB TB 16K | 1 |
| 431 | SP000211 | Memenuhi syarat TPT | kemkes sp | SITB TB 16K | 1 |
| 432 | SP000374 | Tidak Memenuhi Syarat TPT | kemkes sp | SITB TB 16K | 1 |
| 433 | SP000212 | Tanggal Pemberian TPT | kemkes sp | SITB TB 16K | 1 |
| 434 | SP000213 | Hasil Akhir TPT | kemkes sp | SITB TB 16K | 1 |

## Jumlah per CodeSystem (code unik lintas form)

Daftar code satu per baris: lihat tabel Frekuensi code di atas (kolom CodeSystem).

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 120 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 116 |
| http://loinc.org | 67 |
| http://terminology.kemkes.go.id/sp | 59 |
| http://terminology.kemkes.go.id/CodeSystem/examination | 20 |
| http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment | 17 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 13 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 4 |
| http://hl7.org/fhir/sid/icd-10 | 4 |
| http://sys-ids.kemkes.go.id/kfa | 3 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC | 2 |
| http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes | 2 |
| http://terminology.kemkes.go.id/CodeSystem/tb-case-definition | 2 |
| http://terminology.kemkes.go.id | 2 |
| http://terminology.kemkes.go.id/CodeSystem/location-type | 1 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 1 |
| http://hl7.org/fhir/sid/icd-9-cm | 1 |
| **Total** | **434** |

---

## Payload per resource (semua form)

Baris = form, kolom = resource FHIR. Code pembeda tiap payload: lihat tabel Frekuensi payload.

| Form | Observation | ServiceRequest | DiagnosticReport | Specimen | Procedure | EpisodeOfCare | Condition | Encounter | Patient | QuestionnaireResponse | CarePlan | Organization | Practitioner | Coverage | Location | MedicationDispense | MedicationRequest | PractitionerRole | Group | Immunization | RelatedPerson | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maternal Outcome | 5 | – | – | – | – | 2 | 1 | 1 | 1 | – | – | – | 1 | – | – | – | – | 1 | – | – | – | 12 |
| Raffle | 1 | – | – | – | – | 1 | 1 | 1 | 1 | – | – | – | 2 | – | 1 | – | – | – | – | – | – | 8 |
| SiGizi ANC | 30 | 6 | 6 | 6 | 3 | 1 | 1 | 1 | 1 | – | – | – | – | – | – | 2 | 2 | 1 | – | 1 | – | 61 |
| SITB TB 06 | 17 | 9 | 9 | 8 | 2 | 3 | 2 | 1 | 1 | 1 | 1 | 1 | – | – | 1 | – | – | – | – | – | – | 56 |
| SITB TB 03 SO | 23 | 9 | 9 | 9 | 4 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | – | 1 | – | – | – | – | – | – | – | 62 |
| SITB TB 03 RO | 18 | 7 | 7 | 7 | 3 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | – | 1 | – | – | – | – | – | – | – | 50 |
| SITB TB 04 | 17 | 16 | 16 | 16 | – | 1 | 1 | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | 69 |
| SITB TB 16K | 14 | 1 | – | – | – | – | 1 | 1 | 1 | 1 | – | – | – | – | – | – | – | – | 1 | – | 1 | 21 |
| **Total (non-unik)** | **125** | **48** | **47** | **46** | **12** | **10** | **9** | **8** | **8** | **4** | **3** | **3** | **3** | **2** | **2** | **2** | **2** | **2** | **1** | **1** | **1** | **339** |
| **Total unik** | **71** | **20** | **19** | **4** | **7** | **4** | **7** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **2** | **2** | **1** | **1** | **1** | **1** | **148** |

Catatan:
- Organization tidak dihitung di Kobo, SiGizi, TB 04, dan TB 16K (lookup master data, bloknya tidak ditulis di dictionary). Location di Maternal Outcome dan SiGizi ANC juga lookup (tidak dihitung), tapi di Raffle dihitung karena dibuat dari form.
- SiGizi ANC: faskes & posyandu berupa string → lookup master data. PractitionerRole petugas lab → lookup (tidak dihitung). 6 Specimen di SiGizi ANC hanya 2 jenis (darah vena ×5, urine ×1). Code Observation dengan 2 coding (LOINC + ANC custom) dihitung dua-duanya.
- PractitionerRole tenaga pemeriksa SiGizi ANC dan PractitionerRole MO sama-sama tanpa code pembeda tetap (code-nya opsi), jadi dihitung sebagai payload yang sama.
- EpisodeOfCare: Maternal Outcome = ANC & PNC ditutup (finished, hari ke-43); Raffle = ANC dicari dulu, kalau tidak ada baru dibuat.
- Encounter muncul di 2 blok kamus (data utama + statusHistory) = 1 payload.
- SITB TB 06, TB 03 SO, TB 03 RO: blok faskes (Organization + Location) **dihitung** karena dimapping dari variabel faskes di form (match + update). TB 04 dan TB 16K: faskes lookup (TB 04 lewat metadata `puskesmas_id` / `puskesmas_name`). PractitionerRole petugas lab/radiografer dan Practitioner PJ SITB = lookup master data (tidak dihitung). Baris yang dicoret di sheet tidak dipakai. Lihat asumsi A1–A12 di `revisi.md`.
- SITB: opsi coded yang mengikuti jawaban ikut dihitung sebagai code (reasonCode ServiceRequest, CarePlan activity, admitSource, jawaban QuestionnaireResponse, component lab, metode biakan) — disetujui, lihat `aturan.md`. Karena itu jumlah code SITB besar (mis. TB 04: 16 ServiceRequest × 9 alasan pemeriksaan, 16 Specimen × 11 jenis contoh uji).
- SITB TB 04: 1 dictionary untuk TB 04 Fasyankes dan TB 04 Rujukan (header sama). TB 03 RO: follow up 24 bulan = 1 template BTA + 1 template Biakan (asumsi A7); setiap pemeriksaan lab punya ServiceRequest + Specimen + Observation + DiagnosticReport (T03R-4).
- SITB: EpisodeOfCare TB-SO / TB-RO, Patient, Encounter, Condition A15.0, Observation umur (424144002), HIV/DM, lab (11545-1, X0993xx) dipakai ulang di beberapa form SITB → total unik jauh lebih kecil dari non-unik.

---

---

## Log perubahan output
- 2026-11-18: Format tabel: "Jumlah per CodeSystem" hanya CodeSystem + jumlah (daftar code per baris ada di tabel Frekuensi code). "Payload per resource" ditranspos: baris = form, kolom = resource FHIR, tanpa kolom pembeda; ditambah baris Total unik. Bagian Catatan dikembalikan (sempat terhapus 17 Nov) dan diperbarui. Angka tidak berubah. Format yang sama dipakai di `output/<form>.md` (Code per CodeSystem tanpa daftar code).
- 2026-11-17: TB 04 lookup faskes saja (blok Org/Location dihapus, 71 → **69** payload). TB 03 RO: ServiceRequest + Specimen + DiagnosticReport untuk 7 pemeriksaan lab (30 → **50** payload, 357 → **377** code). TB 06 kolom AC (tambahan user) tidak dihitung. Total non-unik 339 / 1758, unik 148 / 434.
- 2026-11-17: Blok faskes dikembalikan (A3): +2 payload di TB 06 (56), TB 04 (71); +1 di TB 03 SO (62), TB 03 RO (30). Code tidak berubah.
- 2026-11-17: SP001138–SP001140 dibatalkan; SP001137 jadi "Paduan lainnya" (TB 03 SO & RO). Varian teks paduan ditambah sebagai baris alias (code lama, tidak dihitung ulang). TB 03 SO 332 → **329** code, TB 03 RO 356 → **357** code. Total non-unik 315 / 1738, unik 147 / 434.
- 2026-11-17: Code lokal baru: TB 06 SP001136 Belum Mulai Pengobatan (code 275 → **276**); TB 03 SO SP001137–SP001140 paduan pengobatan (code 328 → **332**). Hasil Tes HIV "Tidak Diketahui" → dataAbsentReason unknown (tidak dihitung). Total non-unik 315 / 1740, unik 147 / 437.
- 2026-11-17: Jawaban user diterapkan. TB 06: 55 → **54 payload** (Coverage dihapus karena No. BPJS dicoret di sheet), code tetap 275. TB 03 SO: tetap 61 / 328 (Status Pengobatan masuk CarePlan sebagai teks). TB 16K: 24/39 → **21 payload / 35 code** (Practitioner, PractitionerRole kader, dan Observation SP000211 dicoret di sheet). Total non-unik 315 / 1735, unik 147 / 432.
- 2026-11-17: Tambah 5 form SITB: TB 06 (55 payload / 275 code), TB 03 SO (61 / 328), TB 03 RO (29 / 356), TB 04 (69 / 579), TB 16K (24 / 39). Total non-unik jadi 319 payload / 1739 code, unik 148 / 434. Semua tabel di file ini sekarang dibuat ulang dari 8 dictionary di `mapping/` (angka 3 form lama tidak berubah; urutan baris yang frekuensinya sama di tabel Payload per resource bisa bergeser).
- 2026-11-16: Dictionary SiGizi ANC diganti nama jadi `mapping/phdt-data-dictionary-sigizi-anc.csv` (sumbernya PHDT Data Dictionary, bukan Kobo). Angka tidak berubah.
- 2026-11-16: Ringkasan `output/sigizi-anc.md`: baris "Variabel BQ di luar payload" diganti "Variabel di Excel export" (SiGizi ANC: 49, angka saja). Baris ini tidak muncul di form Kobo (tidak ada file mentah). Angka tidak berubah.
- 2026-11-16: SiGizi ANC final setelah jawaban R1–R14: **61 payload, 142 code** (−6 PractitionerRole lab, +1 Observation usia kehamilan 18185-9; code −6 Laboratory worker, +1 18185-9). Tabel frekuensi, CodeSystem, dan payload per resource diperbarui untuk 3 form. Total non-unik 81 payload / 162 code, unik 68 / 132.
- 2026-11-16: Tambah SiGizi ANC sebagai angka sementara (66 payload, 147 code; total non-unik 86/167, unik 67/132). Tabel frekuensi belum diubah sampai R1–R14 dijawab. `scripts/form_output.py` mengenali code pembeda untuk Procedure, ServiceRequest, DiagnosticReport, Specimen, Immunization, MedicationRequest, MedicationDispense (output MO & Raffle tidak berubah).
- 2026-11-16: Revisi reference & path di kedua dictionary (lihat `revisi.md`). Angka tidak berubah.
- 2026-11-16: MO: blok Organization & Location dihapus dari dictionary (lookup master data). Angka tidak berubah.
- 2026-11-16: Output per form menampilkan path tiap variabel BQ dan tanda 🔎 untuk lookup master data. Semua variabel BQ sudah masuk payload (0 di luar payload). Angka tidak berubah.
- 2026-11-16: Tambah output per form (`output/maternal-outcome.md`, `output/raffle.md`), dibuat dengan `scripts/form_output.py`. Raffle jadi 8 payload (Practitioner data entry ditambahkan user di commit `9da6c8d`). Total non-unik 20, unik 15.
- 2026-11-13: Ringkasan diberi Total non-unik vs unik; kolom Jenis resource dihapus. Section payload per form diganti jadi satu tabel "Payload per resource (semua form)".
- 2026-11-13: Raffle direvisi: Location dibuat dari form (payload jadi 7), Condition.code jadi SP001135. Total unik lintas form jadi 15 payload, 8 jenis resource, 19 code.
- 2026-11-13: Tambah form Raffle (6 payload, 6 baris code). Total unik lintas form jadi 14 payload, 18 code. Frekuensi Practitioner, Patient, Encounter, EpisodeOfCare ANC, dan code ANC naik jadi 2.
- 2026-11-13: Kolom "Code per submission" dihapus (tidak dipakai).
- 2026-11-13: Tabel frekuensi payload diberi kolom Code pembeda, Display, dan Variabel Kobo.
- 2026-11-13: Dicek ulang dengan Kobo_3. Angka tidak berubah (12 payload, 14 code). Display SP000396/SP000397 dibetulkan.
- 2026-11-13: File dipisah jadi `aturan.md`, `revisi.md`, `output.md`.
- 2026-11-13: Maternal Outcome dihitung. Repo dibersihkan; isi lama ada di commit `0aba562`.
