# Output Form: ELSMIL Pasca Persalinan

Sumber: `mapping/phdt-data-dictionary-elsmil-pasca-persalinan.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-elsmil-pasca-persalinan.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 24 |
| Code (`jumlah code` = 1) | 96 |
| Code unik (code + CodeSystem) | 90 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 35 |
| Variabel BQ (unik) | 0 |
| Variabel raw (variabel dictionary; belum ada file mentah) | 29 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–7 | Patient | – | – | _Nama_ → `Patient.name.text` (2, tanpa BQ)<br>_NIK_ → `Patient.identifier.use` (3, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (4, tanpa BQ)<br>_Usia_ → `Patient.birthDate` (5, tanpa BQ)<br>_No HP_ → `Patient.telecom` (6, tanpa BQ)<br>_Alamat_ → `Patient.address.use` (7, tanpa BQ) |
| 2 | 8–19 | Observation | 93857-1 | Date and time of obstetric delivery | _Tanggal Persalinan_ → `Observation.valueDateTime` (11, tanpa BQ) |
| 3 | 20–33 | Observation | 72150-6 | Delivery location | _Tempat Persalinan_ → `Observation.valueCodeableConcept.coding` (23, tanpa BQ) |
| 4 | 34–47 | Observation | OC000013 | Penolong Persalinan | _Penolong Persalinan_ → `Observation.valueCodeableConcept.coding` (37, tanpa BQ) |
| 5 | 48–60 | Observation | 57071-3 | Obstetric delivery method | _Cara Persalinan_ → `Observation.valueCodeableConcept.coding` (51, tanpa BQ) |
| 6 | 61–73 | Observation | 249222005 | Neonatal condition | _Keadaan Bayi_ → `Observation.valueCodeableConcept.coding` (64, tanpa BQ) |
| 7 | 74–84 | Observation | SP000147 | Komplikasi pasca persalinan | _Apakah ibu mengalami komplikasi pada masa nifas_ → `Observation.valueBoolean` (77, tanpa BQ) |
| 8 | 85–94 | Condition | 47821001 | Postpartum hemorrhage | _Jika ya pilih salah satu_ → `Condition.clinicalStatus.coding` (85, tanpa BQ) |
| 9 | 95–108 | Observation | PC000004 | KB Pasca Persalinan | _Penggunaan KB Pasca Persalinan_ → `Observation.valueBoolean` (101, tanpa BQ) |
| 10 | 109–126 | Observation | 8659-5 | Birth control method - Reported | _Jika Ya, sebutkan Jenis Metode/Alat/ Obat KBPP dan sebutkan Alasan Ber KB_ → `Observation.valueCodeableConcept.coding` (112, tanpa BQ) |
| 11 | 127–139 | Observation | SP000227 | Alasan menggunakan KB | _Alasan Ber KB_ → `Observation.valueCodeableConcept.coding` (130, tanpa BQ) |
| 12 | 140–165 | Observation | 736796006 | Reason for no contraception (observable entity) | _Jika Tidak, sebutkan alasan tidak ingin berKB_ → `Observation.valueCodeableConcept.coding` (143, tanpa BQ) |
| 13 | 166–176 | Observation | 72166-2 | Tobacco smoking status | _Apakah merokok/terpapar rokok_ → `Observation.valueBoolean` (169, tanpa BQ) |
| 14 | 177–197 | Observation | 63719-9 | What was the primary source of drinking water at your home [Next-of-kin] | _Akses air minum yang layak?_ → `Observation.valueCodeableConcept.coding` (180, tanpa BQ) |
| 15 | 198–211 | Observation | SP000093 | Tempat BAB Layak | _Buang Air Besar di tempat yang layak?_ → `Observation.valueCodeableConcept.coding` (201, tanpa BQ) |
| 16 | 212–222 | Observation | 385827001 | Health promotion education | _TPK memberikan penyuluhan/KIE_ → `Observation.valueBoolean` (215, tanpa BQ) |
| 17 | 223–234 | Observation | 171035004 | Health education given | _Jika Ya_ → `Observation.valueCodeableConcept.coding` (226, tanpa BQ) |
| 18 | 235–245 | Observation | SP000229 | Sudah mendapatkan tablet tambah darah | _Apakah Ibu Pascapersalinan sudah mendapatkan tablet tambah darah_ → `Observation.valueBoolean` (238, tanpa BQ) |
| 19 | 246–256 | Observation | SP000144 | Sudah mengonsumsi tablet tambah darah | _Apakah Ibu Pascapersalinan sudah meminum tablet tambah darah_ → `Observation.valueBoolean` (249, tanpa BQ) |
| 20 | 257–269 | Observation | 306206005 | Referral to service | _Memfasilitasi pelayanan rujukan_ → `Observation.valueCodeableConcept.coding` (260, tanpa BQ) |
| 21 | 270–283 | Observation | 405076007 | Social support status | _Memfasilitasi bantuan sosial_ → `Observation.valueCodeableConcept.coding` (273, tanpa BQ) |
| 22 | 284–298 | Observation | SP000145 | Bantuan sosial yang sedang dalam proses | _Sedang proses_ → `Observation.valueCodeableConcept.coding` (287, tanpa BQ) |
| 23 | 299–313 | Observation | SP000146 | Bantuan sosial yang sudah didapatkan | _Sudah mendapatkan bantuan sosial_ → `Observation.valueCodeableConcept.coding` (302, tanpa BQ) |
| 24 | 314–324 | Observation | SP000219 | Catatan TPK | _Catatan TPK_ → `Observation.valueString` (316, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 22 |
| Patient | 1 |
| Condition | 1 |
| **Total** | **24** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 10 | Observation | `Observation.code.coding` | 93857-1 | Date and time of obstetric delivery | https://loinc.org |
| 2 | 22 | Observation | `Observation.code.coding` | 72150-6 | Delivery location | https://loinc.org |
| 3 | 23 | Observation | `Observation.valueCodeableConcept.coding` | 102 | Pusat Kesehatan Masyarakat | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 4 | 24 | Observation | `Observation.valueCodeableConcept.coding` | 104 | Rumah Sakit | hhttp://terminology.kemkes.go.id/CodeSystem/organization-type |
| 5 | 25 | Observation | `Observation.valueCodeableConcept.coding` | OT000004 | Bidan Praktek Mandiri | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 6 | 36 | Observation | `Observation.code.coding` | OC000013 | Penolong Persalinan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 7 | 37 | Observation | `Observation.valueCodeableConcept.coding` | 11935004 | Obstetrician Occupation | http://snomed.info/sct |
| 8 | 38 | Observation | `Observation.valueCodeableConcept.coding` | 309343006 | Physician Occupation | http://snomed.info/sct |
| 9 | 39 | Observation | `Observation.valueCodeableConcept.coding` | 309453006 | Registered midwife | http://snomed.info/sct |
| 10 | 50 | Observation | `Observation.code.coding` | 57071-3 | Obstetric delivery method | https://loinc.org |
| 11 | 51 | Observation | `Observation.valueCodeableConcept.coding` | 48782003 | Delivery normal | http://snomed.info/sct |
| 12 | 52 | Observation | `Observation.valueCodeableConcept.coding` | 200144004 | Deliveries by cesarean | http://snomed.info/sct |
| 13 | 63 | Observation | `Observation.code.coding` | 249222005 | Neonatal condition | http://snomed.info/sct |
| 14 | 64 | Observation | `Observation.valueCodeableConcept.coding` | 438949009 | Alive | http://snomed.info/sct |
| 15 | 65 | Observation | `Observation.valueCodeableConcept.coding` | 419099009 | Dead |  |
| 16 | 76 | Observation | `Observation.code.coding` | SP000147 | Komplikasi pasca persalinan | http://terminology.kemkes.go.id/sp |
| 17 | 87 | Condition | `Condition.code.coding` | 47821001 | Postpartum hemorrhage | http://snomed.info/sct |
| 18 | 88 | Condition | `Condition.code.coding` | 178280004 | Postnatal infection | http://snomed.info/sct |
| 19 | 89 | Condition | `Condition.code.coding` | O13 | Gestational [pregnancy-induced] hypertension without signification proteinuria | http://hl7.org/fhir/sid/icd-10 |
| 20 | 90 | Condition | `Condition.code.coding` | O90.8 | Other complications of the puerperium, not elsewhere classified | http://hl7.org/fhir/sid/icd-10 |
| 21 | 100 | Observation | `Observation.code.coding` | PC000004 | KB Pasca Persalinan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 22 | 111 | Observation | `Observation.code.coding` | 8659-5 | Birth control method - Reported | http://loinc.org |
| 23 | 112 | Observation | `Observation.valueCodeableConcept.coding` | 77543007 | Ligation of fallopian tube | http://snomed.info/sct |
| 24 | 113 | Observation | `Observation.valueCodeableConcept.coding` | 22523008 | Vasectomy | http://snomed.info/sct |
| 25 | 114 | Observation | `Observation.valueCodeableConcept.coding` | LA6527-1 | Intrauterine device | http://loinc.org |
| 26 | 115 | Observation | `Observation.valueCodeableConcept.coding` | SP000097 | Implan | http://terminology.kemkes.go.id/sp |
| 27 | 116 | Observation | `Observation.valueCodeableConcept.coding` | LA6525-5 | Injectable/implantable hormone | http://loinc.org |
| 28 | 117 | Observation | `Observation.valueCodeableConcept.coding` | LA6524-8 | Oral contraceptive pill | http://loinc.org |
| 29 | 118 | Observation | `Observation.valueCodeableConcept.coding` | LA6523-0 | Condom | http://loinc.org |
| 30 | 119 | Observation | `Observation.valueCodeableConcept.coding` | 237122005 | Lactational amenorrhea | http://snomed.info/sct |
| 31 | 129 | Observation | `Observation.code.coding` | SP000227 | Alasan menggunakan KB | http://terminology.kemkes.go.id/sp |
| 32 | 130 | Observation | `Observation.valueCodeableConcept.coding` | SP000225 | Ingin anak di tunda | http://terminology.kemkes.go.id/sp |
| 33 | 131 | Observation | `Observation.valueCodeableConcept.coding` | SP000226 | Tidak ingin anak lagi | http://terminology.kemkes.go.id/sp |
| 34 | 142 | Observation | `Observation.code.coding` | 736796006 | Reason for no contraception (observable entity) | http://snomed.info/sct |
| 35 | 143 | Observation | `Observation.valueCodeableConcept.coding` | 276367008 | Wanted pregnancy (finding) | http://snomed.info/sct |
| 36 | 144 | Observation | `Observation.valueCodeableConcept.coding` | 423875000 | Deficient knowledge of family planning methods | http://snomed.info/sct |
| 37 | 145 | Observation | `Observation.valueCodeableConcept.coding` | 440552008 | Contraception need complicated by medical condition | http://snomed.info/sct |
| 38 | 146 | Observation | `Observation.valueCodeableConcept.coding` | SP000072 | Efek samping kontrasepsi | http://terminology.kemkes.go.id/sp |
| 39 | 147 | Observation | `Observation.valueCodeableConcept.coding` | 422704000 | Difficulty obtaining contraception | http://snomed.info/sct |
| 40 | 148 | Observation | `Observation.valueCodeableConcept.coding` | SP000091 | Alat/cara KB tidak tersedia | http://terminology.kemkes.go.id/sp |
| 41 | 149 | Observation | `Observation.valueCodeableConcept.coding` | SP000073 | Alat Kontrasepsi Mahal | http://terminology.kemkes.go.id/sp |
| 42 | 150 | Observation | `Observation.valueCodeableConcept.coding` | 424670002 | Dissatisfaction with contraception method (finding) | http://snomed.info/sct |
| 43 | 151 | Observation | `Observation.valueCodeableConcept.coding` | 724073007 | Declined by caregiver of subject (qualifier value) | http://snomed.info/sct |
| 44 | 152 | Observation | `Observation.valueCodeableConcept.coding` | 183945002 | Procedure declined for religious reason (situation) | http://snomed.info/sct |
| 45 | 153 | Observation | `Observation.valueCodeableConcept.coding` | SP000151 | Tidak ada petugas pelayanan KB | http://terminology.kemkes.go.id/sp |
| 46 | 154 | Observation | `Observation.valueCodeableConcept.coding` | SP000148 | Baru melahirkan | http://terminology.kemkes.go.id/sp |
| 47 | 155 | Observation | `Observation.valueCodeableConcept.coding` | SP000149 | 6 bulan terakhir tidak melakukan hubungan suami istri | http://terminology.kemkes.go.id/sp |
| 48 | 156 | Observation | `Observation.valueCodeableConcept.coding` | SP000150 | 6 bulan terakhir tidak menstruasi | http://terminology.kemkes.go.id/sp |
| 49 | 157 | Observation | `Observation.valueCodeableConcept.coding` | 297106006 | Primary infertility | http://snomed.info/sct |
| 50 | 158 | Observation | `Observation.valueCodeableConcept.coding` | 289903006 | Menopause present | http://snomed.info/sct |
| 51 | 168 | Observation | `Observation.code.coding` | 72166-2 | Tobacco smoking status | http://loinc.org |
| 52 | 179 | Observation | `Observation.code.coding` | 63719-9 | What was the primary source of drinking water at your home [Next-of-kin] | http://loinc.org |
| 53 | 180 | Observation | `Observation.valueCodeableConcept.coding` | LA14183-0 | Bottled water | http://loinc.org |
| 54 | 181 | Observation | `Observation.valueCodeableConcept.coding` | LA14182-2 | Community supply | http://loinc.org |
| 55 | 182 | Observation | `Observation.valueCodeableConcept.coding` | SP000066 | Sumur bor/pompa | http://terminology.kemkes.go.id/sp |
| 56 | 183 | Observation | `Observation.valueCodeableConcept.coding` | SP000067 | Sumur terlindungi | http://terminology.kemkes.go.id/sp |
| 57 | 184 | Observation | `Observation.valueCodeableConcept.coding` | SP000068 | Sumur tak terlindungi | http://terminology.kemkes.go.id/sp |
| 58 | 185 | Observation | `Observation.valueCodeableConcept.coding` | SP000069 | Mata air terlindungi | http://terminology.kemkes.go.id/sp |
| 59 | 186 | Observation | `Observation.valueCodeableConcept.coding` | SP000070 | Mata air tak terlindungi | http://terminology.kemkes.go.id/sp |
| 60 | 187 | Observation | `Observation.valueCodeableConcept.coding` | 421665008 | River water | http://snomed.info/sct |
| 61 | 188 | Observation | `Observation.valueCodeableConcept.coding` | 420492000 | Lake water | http://snomed.info/sct |
| 62 | 189 | Observation | `Observation.valueCodeableConcept.coding` | 421176006 | Pond water | http://snomed.info/sct |
| 63 | 190 | Observation | `Observation.valueCodeableConcept.coding` | SP000071 | Air hujan | http://terminology.kemkes.go.id/sp |
| 64 | 200 | Observation | `Observation.code.coding` | SP000093 | Tempat BAB Layak | http://terminology.kemkes.go.id/sp |
| 65 | 201 | Observation | `Observation.valueCodeableConcept.coding` | SP000094 | Jamban milik sendiri dengan leher angsa dan tangki septik/IPAL | http://terminology.kemkes.go.id/sp |
| 66 | 202 | Observation | `Observation.valueCodeableConcept.coding` | SP000095 | Jamban pada MCK komunal dengan leher angsa dan tangki septik/IPAL | http://terminology.kemkes.go.id/sp |
| 67 | 203 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 68 | 204 | Observation | `Observation.valueCodeableConcept.coding` | SP000096 | Tidak ada tempat BAB layak | http://terminology.kemkes.go.id/sp |
| 69 | 214 | Observation | `Observation.code.coding` | 385827001 | Health promotion education | http://loinc.org |
| 70 | 225 | Observation | `Observation.code.coding` | 171035004 | Health education given | http://snomed.info/sct |
| 71 | 226 | Observation | `Observation.valueCodeableConcept.coding` | 125676002 | Person | http://snomed.info/sct |
| 72 | 227 | Observation | `Observation.valueCodeableConcept.coding` | 389109008 | Group | http://snomed.info/sct |
| 73 | 237 | Observation | `Observation.code.coding` | SP000229 | Sudah mendapatkan tablet tambah darah | http://terminology.kemkes.go.id/sp |
| 74 | 248 | Observation | `Observation.code.coding` | SP000144 | Sudah mengonsumsi tablet tambah darah | http://terminology.kemkes.go.id/sp |
| 75 | 259 | Observation | `Observation.code.coding` | 306206005 | Referral to service | http://snomed.info/sct |
| 76 | 260 | Observation | `Observation.valueCodeableConcept.coding` | 385651009 | In progress | http://snomed.info/sct |
| 77 | 261 | Observation | `Observation.valueCodeableConcept.coding` | 385658003 | Done | http://snomed.info/sct |
| 78 | 262 | Observation | `Observation.valueCodeableConcept.coding` | 385660001 | Not done | http://snomed.info/sct |
| 79 | 272 | Observation | `Observation.code.coding` | 405076007 | Social support status | http://snomed.info/sct |
| 80 | 273 | Observation | `Observation.valueCodeableConcept.coding` | LA32661-3 | Applied and waiting to receive | http://loinc.org |
| 81 | 274 | Observation | `Observation.valueCodeableConcept.coding` | LA32660-5 | Received | http://loinc.org |
| 82 | 275 | Observation | `Observation.valueCodeableConcept.coding` | LA32662-1 | Tried but was not able to apply for, or was not eligible | http://loinc.org |
| 83 | 276 | Observation | `Observation.valueCodeableConcept.coding` | LA32663-9 | Did not apply for | http://loinc.org |
| 84 | 286 | Observation | `Observation.code.coding` | SP000145 | Bantuan sosial yang sedang dalam proses | http://terminology.kemkes.go.id/sp |
| 85 | 287 | Observation | `Observation.valueCodeableConcept.coding` | SP000140 | Program Keluarga Harapan | http://terminology.kemkes.go.id/sp |
| 86 | 288 | Observation | `Observation.valueCodeableConcept.coding` | SP000141 | Bantu Non Tunai | http://terminology.kemkes.go.id/sp |
| 87 | 289 | Observation | `Observation.valueCodeableConcept.coding` | SP000142 | Program Indonesia Pintar | http://terminology.kemkes.go.id/sp |
| 88 | 290 | Observation | `Observation.valueCodeableConcept.coding` | SP000143 | Kartu Indonesia Sehat | http://terminology.kemkes.go.id/sp |
| 89 | 291 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 90 | 301 | Observation | `Observation.code.coding` | SP000146 | Bantuan sosial yang sudah didapatkan | http://terminology.kemkes.go.id/sp |
| 91 | 302 | Observation | `Observation.valueCodeableConcept.coding` | SP000140 | Program Keluarga Harapan | http://terminology.kemkes.go.id/sp |
| 92 | 303 | Observation | `Observation.valueCodeableConcept.coding` | SP000141 | Bantu Non Tunai | http://terminology.kemkes.go.id/sp |
| 93 | 304 | Observation | `Observation.valueCodeableConcept.coding` | SP000142 | Program Indonesia Pintar | http://terminology.kemkes.go.id/sp |
| 94 | 305 | Observation | `Observation.valueCodeableConcept.coding` | SP000143 | Kartu Indonesia Sehat | http://terminology.kemkes.go.id/sp |
| 95 | 306 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 96 | 315 | Observation | `Observation.code.coding` | SP000219 | Catatan TPK | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 36 |
| http://terminology.kemkes.go.id/sp | 35 |
| http://loinc.org | 14 |
| https://loinc.org | 3 |
| http://terminology.kemkes.go.id/CodeSystem/organization-type | 2 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 2 |
| http://hl7.org/fhir/sid/icd-10 | 2 |
| hhttp://terminology.kemkes.go.id/CodeSystem/organization-type | 1 |
|  | 1 |
| **Total** | **96** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
