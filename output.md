# Output Hitungan Payload & Code — Form Kobo

Terakhir diperbarui: 2026-11-16
Aturan hitung: lihat `aturan.md`
Form yang sudah dihitung (detail per form, bisa ditelusuri per baris):
- **Maternal Outcome** → `output/maternal-outcome.md` (sumber: `mapping/kobo-data-dictionary-maternal-outcome.csv`)
- **Raffle** → `output/raffle.md` (sumber: `mapping/kobo-data-dictionary-raffle.csv`)
- **SiGizi ANC** → `output/sigizi-anc.md` (sumber: `mapping/kobo-data-dictionary-sigizi-anc.csv`; struktur file mentah: `raw/sigizi-anc-kolom.md`)

File ini adalah **konsolidasi** lintas form. Angka per form di sini harus sama dengan file `output/<form>.md`.

Belum: PNC, form lain

---

## Ringkasan semua form

| Form | Payload | Code |
|---|---|---|
| Maternal Outcome | 12 | 14 |
| Raffle | 8 | 6 |
| SiGizi ANC | 61 | 142 |
| **Total (non-unik)** | **81** | **162** |
| **Total unik** | **68** | **132** |
| Selisih (dipakai ulang) | 13 | 30 |

---

## Frekuensi payload (lintas form)

Frekuensi = di berapa form dipakai. Angka (Nx) = muncul N kali di form itu.

| # | Resource | Code pembeda | Display | Dipakai di form | Frekuensi |
|---|---|---|---|---|---|
| 1 | PractitionerRole | – | – | Maternal Outcome, SiGizi ANC | 2 |
| 2 | Practitioner | – | – | Maternal Outcome, Raffle (2x) | 2 |
| 3 | Patient | – | – | Maternal Outcome, Raffle, SiGizi ANC | 3 |
| 4 | Encounter | – | – | Maternal Outcome, Raffle, SiGizi ANC | 3 |
| 5 | Condition | SP000738 | Kunjungan pemantauan luaran maternal | Maternal Outcome | 1 |
| 6 | EpisodeOfCare | ANC | Antenatal Care | Maternal Outcome, Raffle, SiGizi ANC | 3 |
| 7 | EpisodeOfCare | PNC | Postnatal Care | Maternal Outcome | 1 |
| 8 | Observation | SP000389 | Keadaan Ibu | Maternal Outcome | 1 |
| 9 | Observation | 93857-1 | Date and time of obstetric delivery | Maternal Outcome | 1 |
| 10 | Observation | 81956-5 | Date and time of death [TimeStamp] | Maternal Outcome | 1 |
| 11 | Observation | LT000005 | Alamat Mati | Maternal Outcome | 1 |
| 12 | Observation | 79378-6 | Cause of death | Maternal Outcome | 1 |
| 13 | Location | – | – | Raffle | 1 |
| 14 | Condition | SP001135 | Presensi Posyandu | Raffle | 1 |
| 15 | Observation | 385438008 | Source of information | Raffle | 1 |
| 16 | Condition | 134435003 | Routine antenatal care | SiGizi ANC | 1 |
| 17 | Observation | 424144002 | Current chronological age | SiGizi ANC | 1 |
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

Variabel Kobo / BQ per payload: lihat `output/<form>.md`.

## Frekuensi code (lintas form)

| # | Code | Display | CodeSystem | Dipakai di form | Frekuensi |
|---|---|---|---|---|---|
| 1 | 223366009 | Healthcare professional | snomed | Maternal Outcome | 1 |
| 2 | SP000396 | Data entry staff | kemkes sp | Maternal Outcome | 1 |
| 3 | SP000397 | Field/call center staff | kemkes sp | Maternal Outcome | 1 |
| 4 | SP000738 | Kunjungan pemantauan luaran maternal | kemkes sp | Maternal Outcome | 1 |
| 5 | ANC | Antenatal Care | episodeofcare-type | Maternal Outcome, Raffle, SiGizi ANC | 3 |
| 6 | PNC | Postnatal Care | episodeofcare-type | Maternal Outcome | 1 |
| 7 | SP000389 | Keadaan Ibu | kemkes sp | Maternal Outcome | 1 |
| 8 | 102514002 | Well female adult | snomed | Maternal Outcome | 1 |
| 9 | 39104002 | Illness | snomed | Maternal Outcome | 1 |
| 10 | 419099009 | Dead | snomed | Maternal Outcome | 1 |
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
| 27 | 424144002 | Current chronological age | snomed | SiGizi ANC | 1 |
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
| 62 | LA6576-8 | Positive | loinc | SiGizi ANC (4x) | 1 |
| 63 | LA6577-6 | Negative | loinc | SiGizi ANC (4x) | 1 |
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
| 104 | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | loinc | SiGizi ANC | 1 |
| 105 | 76772-3 | Plasmodium falciparum Ag [Presence] in Blood by Rapid immunoassay | loinc | SiGizi ANC | 1 |
| 106 | 104742-2 | Ova and parasites identified in Specimen | loinc | SiGizi ANC | 1 |
| 107 | 74964007 | Other | snomed | SiGizi ANC (4x) | 1 |
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
| 128 | 56717001 | Tuberculosis | snomed | SiGizi ANC | 1 |
| 129 | 56265001 | Heart disease | snomed | SiGizi ANC | 1 |
| 130 | SP000016 | Tatalaksana Masalah Kesehatan | kemkes sp | SiGizi ANC | 1 |
| 131 | 1230101008 | Counseling for pregnancy | snomed | SiGizi ANC | 1 |
| 132 | 385892002 | Mental health screening | snomed | SiGizi ANC | 1 |

## Jumlah per CodeSystem (code unik lintas form)

| CodeSystem | Jumlah | Code |
|---|---|---|
| http://snomed.info/sct | 48 | 223366009, 102514002, 39104002, 419099009, 385438008, 309453006, 309343006, 309367003, 224535009, 134435003, 424144002, 392570002, 2004005, 38341003, 45007003, 284473002, 289625003, 289437007, 289441006, 289440007, 312668007, 289439005, 1209182005, 268445003, 169221005, 169255008, 122555007, 122575003, 860635002, 166921001, 166922008, 15220000, 74964007, 116859006, 3457005, 48194001, 398254007, 15938005, 135840009, 308116003, 435591000124104, 40733004, 73211009, 414916001, 56717001, 56265001, 1230101008, 385892002 |
| http://loinc.org | 28 | 93857-1, 81956-5, 79378-6, 8665-2, 18185-9, 11778-8, 8302-2, 29463-7, 883-9, LA19710-5, LA19709-7, LA19708-9, LA28449-9, 10331-7, LA6576-8, LA6577-6, 72155-5, 68961-2, LA15255-5, LA15256-3, 75410-1, 22464-2, 2887-8, 718-7, 74774-1, 88874-3, 76772-3, 104742-2 |
| http://terminology.kemkes.go.id/sp | 25 | SP000396, SP000397, SP000738, SP000389, SP001135, SP000776, SP000777, SP000778, SP000001, SP000002, SP000003, SP000004, SP000005, SP000006, SP000370, SP000007, SP000008, SP000009, SP000010, SP000011, SP000012, SP000013, SP000014, SP000015, SP000016 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 13 | ANC.B6.DE14, ANC.B6.DE22, ANC.B8.DE1, ANC.B8.DE3, ANC.B9.DE24, ANC.B9.DE29, ANC.B8.DE111, ANC.B9.DE32, ANC.B9.DE60, ANC.B9.DE96, ANC.B9.DE114, ANC.B9.DE175, ANC.B9.DE159 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 6 | OC000010, OI000018, OI000035, OI000032, OI000033, OI000034 |
| http://sys-ids.kemkes.go.id/kfa | 3 | VG139, 92000653, 93015491 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 2 | ANC, PNC |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC | 2 | K1M, K1A |
| http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes | 2 | ANC.SS.DE58, ANC.SS.DE3 |
| http://terminology.kemkes.go.id/CodeSystem/location-type | 1 | LT000005 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 1 | N |
| http://hl7.org/fhir/sid/icd-9-cm | 1 | 88.78 |
| **Total** | **132** | |

---

## Payload per resource (semua form)

| Resource | Maternal Outcome | Raffle | SiGizi ANC | Total (non-unik) | Total unik | Pembeda (unik) |
|---|---|---|---|---|---|---|
| Observation | 5 | 1 | 30 | 36 | 36 | SP000389, 93857-1, 81956-5, LT000005, 79378-6, 385438008, 424144002, 8665-2, 18185-9, 11778-8, 8302-2, OC000010, SP000001, SP000002, 29463-7, 392570002, 284473002, 289625003, 883-9, 10331-7, 289437007, 72155-5, 268445003, 68961-2, 75410-1, 22464-2, 2887-8, 718-7, 74774-1, 15220000, SP000007, SP000010, SP000012, SP000014, SP000015, SP000016 |
| ServiceRequest | – | – | 6 | 6 | 6 | 68961-2, 75410-1, 22464-2, 2887-8, 718-7, 74774-1 |
| Specimen | – | – | 6 | 6 | 2 | 122555007, 122575003 |
| DiagnosticReport | – | – | 6 | 6 | 6 | 68961-2, 75410-1, 22464-2, 2887-8, 718-7, 74774-1 |
| EpisodeOfCare | 2 | 1 | 1 | 4 | 2 | ANC, PNC |
| Practitioner | 1 | 2 | – | 3 | 1 | – |
| Patient | 1 | 1 | 1 | 3 | 1 | – |
| Encounter | 1 | 1 | 1 | 3 | 1 | – |
| Condition | 1 | 1 | 1 | 3 | 3 | SP000738, SP001135, 134435003 |
| Procedure | – | – | 3 | 3 | 3 | 88.78, 1230101008, 385892002 |
| PractitionerRole | 1 | – | 1 | 2 | 1 | – |
| MedicationRequest | – | – | 2 | 2 | 2 | 92000653, SP000370 |
| MedicationDispense | – | – | 2 | 2 | 2 | 93015491, SP000370 |
| Location | – | 1 | – | 1 | 1 | – |
| Immunization | – | – | 1 | 1 | 1 | VG139 |
| **Total** | **12** | **8** | **61** | **81** | **68** | |

Catatan:
- Organization tidak dihitung di semua form (lookup master data, bloknya tidak ditulis di dictionary). Location di Maternal Outcome dan SiGizi ANC juga lookup (tidak dihitung), tapi di Raffle dihitung karena dibuat dari form.
- SiGizi ANC: faskes & posyandu berupa string → lookup master data. PractitionerRole petugas lab → lookup (tidak dihitung). 6 Specimen di SiGizi ANC hanya 2 jenis (darah vena ×5, urine ×1). Code Observation dengan 2 coding (LOINC + ANC custom) dihitung dua-duanya.
- PractitionerRole tenaga pemeriksa SiGizi ANC dan PractitionerRole MO sama-sama tanpa code pembeda tetap (code-nya opsi), jadi dihitung sebagai payload yang sama.
- EpisodeOfCare: Maternal Outcome = ANC & PNC ditutup (finished, hari ke-43); Raffle = ANC dicari dulu, kalau tidak ada baru dibuat.
- Encounter muncul di 2 blok kamus (data utama + statusHistory) = 1 payload.

---

## Log perubahan output
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
