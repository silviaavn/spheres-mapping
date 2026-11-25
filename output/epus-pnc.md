# Output Form: ePuskesmas KIA Harian PNC

Sumber: `mapping/phdt-data-dictionary-epus-pnc.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-epus-pnc.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 82 |
| Code (`jumlah code` = 1) | 166 |
| Code unik (code + CodeSystem) | 147 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 29 |
| Variabel BQ (unik) | 0 |
| Variabel raw (variabel dictionary; belum ada file mentah) | 107 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–27 | Patient | – | – | _Nama_Pasien_ → `Patient.name.text` (2, tanpa BQ)<br>_NIK_ → `Patient.identifier.value` (5, tanpa BQ)<br>_Tanggal_Lahir_ → `Patient.birthDate` (8, tanpa BQ)<br>_No HP_ → `Patient.telecom` (9, tanpa BQ)<br>_Alamat Domisili_ → `Patient.address.use` (12, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (18, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (21, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.extension.valueCode` (24, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.extension.valueCode` (27, tanpa BQ) |
| 2 | 76–96 | Practitioner | – | – | _Dokter/Tenaga Medis_ → `Practitioner.identifier` (76, tanpa BQ) |
| 3 | 97–103 | PractitionerRole | – | – | _jenis_tenaga_kesehatan_ → `PractitionerRole.active` (97, tanpa BQ) |
| 4 | 104–112 | EpisodeOfCare | PNC | Postnatal Care | _Episode Of Care ID_ → `EpisodeOfCare.identifier` (104, tanpa BQ) |
| 5 | 113–131 | Encounter | – | – | _Kunjungan_KF_ → `Encounter.identifier` (114, tanpa BQ)<br>_Tanggal_PNC_ → `Encounter.period.start` (126, tanpa BQ)<br>_Cara Masuk_ → `Encounter.hospitalization.admitSource.coding` (142, tanpa BQ) |
| 6 | 132–141 | Condition | Z39.2 | Routine postpartum follow-up | _Diagnosis_ → `Condition.code.coding` (134, tanpa BQ) |
| 7 | 149–159 | Observation | 93857-1 | Date and time of obstetric delivery | _Tanggal_Bersalin_ → `Observation.valueDateTime` (152, tanpa BQ) |
| 8 | 160–170 | Observation | 11996-6 | [#] Pregnancies | _Gravida_ → `Observation.valueInteger` (163, tanpa BQ) |
| 9 | 171–181 | Observation | 11977-6 | [#] Parity | _Partus_ → `Observation.valueInteger` (174, tanpa BQ) |
| 10 | 182–192 | Observation | 69043-8 | Other pregnancy outcomes # | _Abortus_ → `Observation.valueInteger` (185, tanpa BQ) |
| 11 | 193–204 | Observation | SP000131 | Status Pindahan | _Status Pindahan_ → `Observation.valueBoolean` (196, tanpa BQ) |
| 12 | 205–226 | Observation | SP000134 | Jenis Lokasi Screening | _Lokasi Screening_ → `Observation.valueCodeableConcept.coding` (208, tanpa BQ)<br>_Nama Faskes Lokasi Screening_ → `Observation.note` (226, tanpa BQ) |
| 13 | 227–238 | Observation | 8480-6 | Systolic blood pressure | _Tekanan_Darah_ → `Observation.valueQuantity.value` (230, tanpa BQ) |
| 14 | 239–250 | Observation | 8462-4 | Diastolic blood pressure | _Tekanan_Darah_ → `Observation.valueQuantity.value` (242, tanpa BQ) |
| 15 | 251–262 | Observation | 8867-4 | Heart rate | _Nadi_ → `Observation.valueQuantity.value` (254, tanpa BQ) |
| 16 | 263–274 | Observation | 8310-5 | Body temperature | _Suhu_ → `Observation.valueQuantity.value` (266, tanpa BQ) |
| 17 | 275–286 | Observation | 9279-1 | Respiratory rate | _Respirasi_ → `Observation.valueQuantity.value` (278, tanpa BQ) |
| 18 | 287–293 | Condition | 289530006 | Vaginal bleeding | _Pendarahan_Pervaginam_ → `Condition.clinicalStatus.coding` (287, tanpa BQ) |
| 19 | 294–305 | Observation | 81661-1 | Blood Loss [Volume] Measured | _Jumlah_Pendarahan_Pervaginam_ → `Observation.valueQuantity.value` (297, tanpa BQ) |
| 20 | 306–316 | Observation | 364297003 | Female perineum observable | _Kondisi_Perineum_ → `Observation.valueString` (309, tanpa BQ) |
| 21 | 317–328 | Observation | OC000020 | Tanda Infeksi Perineum | _Tanda_Infeksi_Perineum_ → `Observation.valueBoolean` (320, tanpa BQ) |
| 22 | 329–340 | Observation | OC000025 | Tanda Infeksi Luka Jahitan Sectio Caesaria | _Tanda_Infeksi_Luka_Jahitan_ → `Observation.valueBoolean` (332, tanpa BQ) |
| 23 | 341–355 | Observation | 32422-8 | Physical findings of breast | _Pemeriksaan_Payudara_ → `Observation.valueCodeableConcept.coding` (344, tanpa BQ) |
| 24 | 356–367 | Observation | 289700000 | Uterine contractions present | _Kontraksi_Uteri_ → `Observation.valueBoolean` (359, tanpa BQ) |
| 25 | 368–380 | Observation | 249214003 | Color of lochia | _Warna_Lokia_ → `Observation.valueCodeableConcept.coding` (371, tanpa BQ) |
| 26 | 381–392 | Observation | 249215002 | Odor of lochia | _Bau_Lokia_ → `Observation.valueBoolean` (384, tanpa BQ) |
| 27 | 393–405 | Observation | OC000017 | Produksi ASI | _Produksi_Asi_ → `Observation.valueCodeableConcept.coding` (396, tanpa BQ) |
| 28 | 406–417 | Observation | 252041008 | Micturition finding | _BAK_ → `Observation.valueCodeableConcept.coding` (409, tanpa BQ) |
| 29 | 418–429 | Observation | 300375001 | Able to defecate | _BAB_ → `Observation.valueBoolean` (421, tanpa BQ) |
| 30 | 430–440 | Procedure | 408988007 | Newborn care education | _Konseling Perawatan Bayi Baru Lahir_ → `Procedure.category.coding` (430, tanpa BQ) |
| 31 | 441–452 | Observation | 8345-1 | Body weight Measured --post partum | _BB_ → `Observation.valueQuantity.value` (444, tanpa BQ) |
| 32 | 453–464 | Observation | 8305-5 | Body height --post partum | _TB_ → `Observation.valueQuantity.value` (456, tanpa BQ) |
| 33 | 465–477 | Observation | 284473002 | Mid upper arm circumference | _Lila_ → `Observation.status` (465, tanpa BQ)<br>_Status Gizi KEK/Tidak KEK_ → `Observation.interpretation` (476, tanpa BQ) |
| 34 | 478–489 | Condition | 47821001 | Postpartum hemorrhage | _Komplikasi_ → `Condition.clinicalStatus.coding` (478, tanpa BQ) |
| 35 | 490–503 | Observation | 289084000 | Difficulty performing breastfeeding | _Apakah ada masalah memberikan ASI_ → `Observation.valueBoolean` (493, tanpa BQ)<br>_Catatan ASI_ → `Observation.note.text` (502, tanpa BQ)<br>_Catat_Di_Buku_KIA_ → `Observation.category.coding` (503, tanpa BQ) |
| 36 | 504–514 | Observation | SP000122 | Catat di Buku KIA | – |
| 37 | 515–529 | Medication | 93015491 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | _Jumlah_Tablet_Fe_yang_Didapatkan_ → `Medication.id` (515, tanpa BQ) |
| 38 | 530–563 | MedicationRequest | 92000653 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula | – |
| 39 | 564–596 | MedicationDispense | 93015491 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | _Diberikan_Tablet_FE_ → `MedicationDispense.status` (584, tanpa BQ)<br>_{Jumlah_Tablet_Fe_yang_Didapatkan}_ → `MedicationDispense.quantity.value` (594, tanpa BQ) |
| 40 | 597–607 | MedicationStatement | – | – | _Jumlah_Tablet_Fe_yang_Sudah_Dikonsumsi_ → `MedicationStatement.category.coding` (597, tanpa BQ)<br>_{Jumlah_Tablet_Fe_yang_Sudah_Dikonsumsi}_ → `MedicationStatement.dosage.doseAndRate.doseQuantity` (607, tanpa BQ) |
| 41 | 608–618 | Procedure | 767224000 | Administration of vitamin A | _Pemberian_Vitamin_A_ → `Procedure.category.coding` (608, tanpa BQ)<br>_Catatan_Pemberian_Vit_A_ → `Procedure.note` (618, tanpa BQ) |
| 42 | 619–645 | MedicationRequest | 92000809 | Retinol Palmitate 200.000 IU Kapsul Lunak | _Dosis_Vit_A_ → `MedicationRequest.contained.resourceType` (619, tanpa BQ) |
| 43 | 646–671 | MedicationDispense | 93018284 | Retinol Palmitate 200.000 IU Kapsul Lunak (Umum) | – |
| 44 | 672–682 | Procedure | 711029005 | Counseling about breastfeeding | _Konseling ASI_ → `Procedure.category.coding` (672, tanpa BQ) |
| 45 | 683–693 | Procedure | ED000008 | Edukasi Tanda Bahaya Kehamilan, Bersalin dan Nifas | _Tanda Bahaya Nifas_ → `Procedure.category.coding` (683, tanpa BQ) |
| 46 | 694–704 | Procedure | 72531000052105 | Counseling for contraception | _Konseling KB_ → `Procedure.category.coding` (694, tanpa BQ) |
| 47 | 705–715 | Procedure | SP000135 | Konseling Tanda Bahaya Bayi Baru Lahir | _Konseling Tanda Bahaya Bayi Baru Lahir_ → `Procedure.category.coding` (705, tanpa BQ) |
| 48 | 716–726 | Procedure | 441041000124100 | Counseling about nutrition | _Konseling Gizi_ → `Procedure.category.coding` (716, tanpa BQ) |
| 49 | 727–737 | Procedure | PC000001 | Perawatan Tali Pusat | _Konseling Perawatan Tali Pusar_ → `Procedure.category.coding` (727, tanpa BQ) |
| 50 | 738–748 | Procedure | ED000010 | Edukasi PHBS | _Konseling PHBS_ → `Procedure.category.coding` (738, tanpa BQ) |
| 51 | 749–758 | ServiceRequest | – | – | _Tindak_Lanjut_CD4_ → `ServiceRequest.category` (749, tanpa BQ) |
| 52 | 762–769 | Specimen | – | – | – |
| 53 | 770–782 | Observation | 32515-9 | CD3+CD4+ (T4 helper) cells [#/volume] in Specimen | – |
| 54 | 783–794 | DiagnosticReport | 32515-9 | CD3+CD4+ (T4 helper) cells [#/volume] in Specimen | – |
| 55 | 795–806 | Observation | SP000046 | Terapi Antiretroviral (ART) | _Tindak_Lanjut_ART_ → `Observation.valueBoolean` (798, tanpa BQ) |
| 56 | 807–827 | Observation | SP000124 | Obat anti malaria | _Tindak_Lanjut_Obat_Anti_Malaria_ → `Observation.valueBoolean` (810, tanpa BQ) |
| 57 | 828–851 | Observation | SP000125 | Obat anti tuberkulosis | _Tindak_Lanjut_Obat_TB_ → `Observation.valueBoolean` (831, tanpa BQ) |
| 58 | 852–861 | ServiceRequest | – | – | _Foto_Thorax_ → `ServiceRequest.category` (852, tanpa BQ) |
| 59 | 862–865 | PractitionerRole | – | – | – |
| 60 | 866–878 | Observation | 24648-8 | XR Chest PA upright | – |
| 61 | 879–889 | DiagnosticReport | – | – | – |
| 62 | 890–907 | Observation | SP000139 | KB Pasca Plasenta | _Metode_Kontrasepsi_KB_Pasca_Plasenta_ → `Observation.valueCodeableConcept.coding` (893, tanpa BQ) |
| 63 | 908–919 | Observation | SP000139 | KB Pasca Plasenta | _KB_Pasca_Plasenta_ → `Observation.valueBoolean` (911, tanpa BQ)<br>_Tanggal Pelaksanaan KB Plasenta_ → `Observation.effectiveDateTime` (916, tanpa BQ) |
| 64 | 920–937 | Observation | PC000004 | KB Pasca Persalinan | _Metode_Kontrasepsi_KB_Pasca_Persalinan_ → `Observation.valueCodeableConcept.coding` (923, tanpa BQ) |
| 65 | 938–949 | Observation | PC000004 | KB Pasca Persalinan | _KB_Pasca_Persalinan_ → `Observation.valueBoolean` (941, tanpa BQ)<br>_Tanggal Pelaksanaan KB Pasca Persalinan_ → `Observation.effectiveDateTime` (946, tanpa BQ) |
| 66 | 950–959 | CarePlan | – | – | _Rencana KB Pasca Persalinan_ → `CarePlan.status` (950, tanpa BQ) |
| 67 | 960–979 | Observation | SP000380 | Tatalaksana Komplikasi Pendarahan | _Tatalaksana_Komplikasi_Pendarahan_ → `Observation.valueBoolean` (963, tanpa BQ)<br>_Tatalaksana_Pemberian_Tablet_Fe_ → `Observation.component.code.coding` (965, tanpa BQ)<br>_Tatalaksana_Transfusi_Darah_ → `Observation.component.code.coding` (968, tanpa BQ)<br>_Lain-lain_ → `Observation.component.code.coding` (971, tanpa BQ) |
| 68 | 980–998 | Observation | 736286003 | Hypertension clinical management plan | _Tatalaksana_Komplikasi_Hipertensi_ → `Observation.valueBoolean` (983, tanpa BQ)<br>_Tatalaksana_Pantau_Tekanan_Darah_Hipertensi_ → `Observation.component.code.coding` (985, tanpa BQ)<br>_Tatalaksana_Pantau_Urin_Hipertensi_ → `Observation.component.code.coding` (988, tanpa BQ) |
| 69 | 999–1026 | Observation | SP000138 | Tatalaksana Komplikasi Pre Eklampsia | _Tatalaksana_Eklampsia_ → `Observation.valueBoolean` (1002, tanpa BQ)<br>_Tatalaksana_Pantau_Tekanan_Darah_Eklampsia_ → `Observation.component.code.coding` (1004, tanpa BQ)<br>_Tatalaksana_Pantau_Urin_Eklampsia_ → `Observation.component.code.coding` (1007, tanpa BQ)<br>_Lain-lain_ → `Observation.component.code.coding` (1010, tanpa BQ)<br>_Pemberian_Anti_Hipertensi_ → `Observation.component.code` (1011, tanpa BQ)<br>_Pemberian_MgSO4_ → `Observation.component.code.coding` (1014, tanpa BQ)<br>_Pemberian_Diazepam_Injeksi_ → `Observation.component.code.coding` (1017, tanpa BQ) |
| 70 | 1028–1039 | Observation | SP000389 | Keadaan Ibu | – |
| 71 | 1040–1048 | Condition | 359746009 | Patient’s condition stable | _Keadaan_Pulang_ → `Condition.clinicalStatus.coding` (1040, tanpa BQ) |
| 72 | 1054–1074 | ServiceRequest | 409014006 | Delivery care management | _Apakah pasien dirujuk?_ → `ServiceRequest.status` (1054, tanpa BQ)<br>_Faskes Rujukan_ → `ServiceRequest.locationCode.coding` (1067, tanpa BQ)<br>_Nama Faskes Rujukan_ → `ServiceRequest.locationCode.text` (1074, tanpa BQ) |
| 73 | 1075–1084 | Observation | 35025007 | Manual pelvic examination | _Pemeriksaan_Jalan_Lahir_ → `Observation.valueString` (1078, tanpa BQ) |
| 74 | 1085–1095 | Observation | 81956-5 | Date and time of death [TimeStamp] | _Waktu_Kematian_ → `Observation.valueDateTime` (1088, tanpa BQ) |
| 75 | 1096–1106 | Observation | SP000666 | Hari setelah melahirkan | _Hari ke Sejak Melahirkan_ → `Observation.valueInteger` (1099, tanpa BQ) |
| 76 | 1107–1119 | Observation | 8665-2 | Last menstrual period start date | _Tanggal_HPHT_ → `Observation.valueDateTime` (1111, tanpa BQ) |
| 77 | 1120–1132 | Observation | 11778-8 | Delivery date Estimated | _Tanggal_Taksiran_Persalinan_ → `Observation.valueDateTime` (1124, tanpa BQ) |
| 78 | 1133–1146 | Observation | SP000050 | Riwayat Onset Persalinan | _Tanggal_Persalinan_Sebelumnya_ → `Observation.identifier` (1133, tanpa BQ) |
| 79 | 1147–1158 | Observation | SP000132 | Memiliki Buku KIA | _Memiliki_Buku_KIA_ → `Observation.valueBoolean` (1150, tanpa BQ) |
| 80 | 1159–1172 | Observation | 56077-1 | Body weight --pre current pregnancy | _BB_Sebelum_Hamil_ → `Observation.valueQuantity.value` (1163, tanpa BQ) |
| 81 | 1173–1185 | Observation | 11977-6 | [#] Parity | _Hidup_ → `Observation.valueInteger` (1177, tanpa BQ) |
| 82 | 1186–1196 | Observation | SP000667 | Penanganan Risiko Tinggi dan Komplikasi | _Penanganan_Resiko_Tinggi_Dan_Komplikasi_ → `Observation.valueString` (1189, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 50 |
| Procedure | 9 |
| Condition | 4 |
| ServiceRequest | 3 |
| PractitionerRole | 2 |
| MedicationRequest | 2 |
| MedicationDispense | 2 |
| DiagnosticReport | 2 |
| Patient | 1 |
| Practitioner | 1 |
| EpisodeOfCare | 1 |
| Encounter | 1 |
| Medication | 1 |
| MedicationStatement | 1 |
| Specimen | 1 |
| CarePlan | 1 |
| **Total** | **82** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 99 | PractitionerRole | `PractitionerRole.code.coding` | 309453006 | Registered midwife | http://snomed.info/sct |
| 2 | 100 | PractitionerRole | `PractitionerRole.code.coding` | 309343006 | Physician | http://snomed.info/sct |
| 3 | 101 | PractitionerRole | `PractitionerRole.code.coding` | 309367003 | Obstetrician and gynecologist | http://snomed.info/sct |
| 4 | 102 | PractitionerRole | `PractitionerRole.code.coding` | 224535009 | Registered nurse | http://snomed.info/sct |
| 5 | 108 | EpisodeOfCare | `EpisodeOfCare.type.coding` | PNC | Postnatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 6 | 134 | Condition | `Condition.code.coding` | Z39.2 | Routine postpartum follow-up | http://hl7.org/fhir/sid/icd-10 |
| 7 | 142 | Encounter | `Encounter.hospitalization.admitSource.coding` | EHA000002 | Datang sendiri | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 8 | 143 | Encounter | `Encounter.hospitalization.admitSource.coding` | 305956004 | Referral by physician | http://snomed.info/sct |
| 9 | 144 | Encounter | `Encounter.hospitalization.admitSource.coding` | 306052007 | Referral by midwife | http://snomed.info/sct |
| 10 | 145 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000116 | Rujukan dari Puskesmas Pembantu | http://terminology.kemkes.go.id/sp |
| 11 | 146 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000117 | Rujukan dari Puskesmas | http://terminology.kemkes.go.id/sp |
| 12 | 147 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000118 | Rujukan dari Rumah Bersalin / Klinik | http://terminology.kemkes.go.id/sp |
| 13 | 148 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000119 | Rujukan dari Rumah Sakit | http://terminology.kemkes.go.id/sp |
| 14 | 151 | Observation | `Observation.code.coding` | 93857-1 | Date and time of obstetric delivery | http://loinc.org |
| 15 | 162 | Observation | `Observation.code.coding` | 11996-6 | [#] Pregnancies | http://loinc.org |
| 16 | 173 | Observation | `Observation.code.coding` | 11977-6 | [#] Parity | http://loinc.org |
| 17 | 184 | Observation | `Observation.code.coding` | 69043-8 | Other pregnancy outcomes # | http://loinc.org |
| 18 | 195 | Observation | `Observation.code.coding` | SP000131 | Status Pindahan | http://terminology.kemkes.go.id/sp |
| 19 | 207 | Observation | `Observation.code.coding` | SP000134 | Jenis Lokasi Screening | http://terminology.kemkes.go.id/sp |
| 20 | 208 | Observation | `Observation.valueCodeableConcept.coding` | 264362003 | Home | http://snomed.info/sct |
| 21 | 209 | Observation | `Observation.valueCodeableConcept.coding` | OT000001 | Polindes | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 22 | 210 | Observation | `Observation.valueCodeableConcept.coding` | OT000002 | Pustu | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 23 | 211 | Observation | `Observation.valueCodeableConcept.coding` | 102 | Pusat Kesehatan Masyarakat | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 24 | 212 | Observation | `Observation.valueCodeableConcept.coding` | 103 | Klinik | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 25 | 213 | Observation | `Observation.valueCodeableConcept.coding` | OT000008 | Rumah Bersalin | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 26 | 214 | Observation | `Observation.valueCodeableConcept.coding` | 82242000 | Children’s hospital | http://snomed.info/sct |
| 27 | 215 | Observation | `Observation.valueCodeableConcept.coding` | 104 | Rumah Sakit | hhttp://terminology.kemkes.go.id/CodeSystem/organization-type |
| 28 | 216 | Observation | `Observation.valueCodeableConcept.coding` | OT000003 | RS ODHA | hhttp://terminology.kemkes.go.id/CodeSystem/organization-type |
| 29 | 217 | Observation | `Observation.valueCodeableConcept.coding` | OT000004 | Bidan Praktek Mandiri | hhttp://terminology.kemkes.go.id/CodeSystem/organization-type |
| 30 | 218 | Observation | `Observation.valueCodeableConcept.coding` | LT000008 | Dalam perjalanan dari rumah/masyarakat | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 31 | 229 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 32 | 241 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://loinc.org |
| 33 | 253 | Observation | `Observation.code.coding` | 8867-4 | Heart rate | http://loinc.org |
| 34 | 265 | Observation | `Observation.code.coding` | 8310-5 | Body temperature | http://loinc.org |
| 35 | 277 | Observation | `Observation.code.coding` | 9279-1 | Respiratory rate | http://loinc.org |
| 36 | 289 | Condition | `Condition.code.coding` | 289530006 | Vaginal bleeding | http://snomed.info/sct |
| 37 | 296 | Observation | `Observation.code.coding` | 81661-1 | Blood Loss [Volume] Measured | http://loinc.org |
| 38 | 308 | Observation | `Observation.code.coding` | 364297003 | Female perineum observable | http://loinc.org |
| 39 | 319 | Observation | `Observation.code.coding` | OC000020 | Tanda Infeksi Perineum | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 40 | 331 | Observation | `Observation.code.coding` | OC000025 | Tanda Infeksi Luka Jahitan Sectio Caesaria | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 41 | 343 | Observation | `Observation.code.coding` | 32422-8 | Physical findings of breast | http://loinc.org |
| 42 | 344 | Observation | `Observation.valueCodeableConcept.coding` | 300885006 | Swelling of breast | http://snomed.info/sct |
| 43 | 345 | Observation | `Observation.valueCodeableConcept.coding` | 290070001 | Red breast | http://snomed.info/sct |
| 44 | 346 | Observation | `Observation.valueCodeableConcept.coding` | 54302000 | Discharge from nipple | http://snomed.info/sct |
| 45 | 347 | Observation | `Observation.valueCodeableConcept.coding` | 53430007 | Pain of breast | http://snomed.info/sct |
| 46 | 348 | Observation | `Observation.valueCodeableConcept.coding` | 290084006 | Breast normal | http://snomed.info/sct |
| 47 | 358 | Observation | `Observation.code.coding` | 289700000 | Uterine contractions present | http://snomed.info/sct |
| 48 | 370 | Observation | `Observation.code.coding` | 249214003 | Color of lochia | http://snomed.info/sct |
| 49 | 371 | Observation | `Observation.valueCodeableConcept.coding` | 278072004 | Lochia rubra | http://snomed.info/sct |
| 50 | 372 | Observation | `Observation.valueCodeableConcept.coding` | 449828001 | Lochia serosa | http://snomed.info/sct |
| 51 | 373 | Observation | `Observation.valueCodeableConcept.coding` | 449827006 | Lochia alba | http://snomed.info/sct |
| 52 | 383 | Observation | `Observation.code.coding` | 249215002 | Odor of lochia | http://snomed.info/sct |
| 53 | 395 | Observation | `Observation.code.coding` | OC000017 | Produksi ASI | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 54 | 396 | Observation | `Observation.valueCodeableConcept.coding` | OV000016 | Produksi ASI ada | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 55 | 397 | Observation | `Observation.valueCodeableConcept.coding` | OV000017 | Produksi ASI ada tapi sedikit | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 56 | 398 | Observation | `Observation.valueCodeableConcept.coding` | OV000018 | Produksi ASI tidak ada | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 57 | 408 | Observation | `Observation.code.coding` | 252041008 | Micturition finding | http://snomed.info/sct |
| 58 | 409 | Observation | `Observation.valueCodeableConcept.coding` | 38671000119103 | Abnormal urination | http://snomed.info/sct |
| 59 | 410 | Observation | `Observation.valueCodeableConcept.coding` | 102834005 | Normal micturition | http://snomed.info/sct |
| 60 | 420 | Observation | `Observation.code.coding` | 300375001 | Able to defecate | http://snomed.info/sct |
| 61 | 431 | Procedure | `Procedure.code.coding` | 408988007 | Newborn care education | http://snomed.info/sct |
| 62 | 443 | Observation | `Observation.code.coding` | 8345-1 | Body weight Measured --post partum | http://loinc.org |
| 63 | 455 | Observation | `Observation.code.coding` | 8305-5 | Body height --post partum | http://loinc.org |
| 64 | 467 | Observation | `Observation.code.coding` | 284473002 | Mid upper arm circumference | http://snomed.info/sct |
| 65 | 476 | Observation | `Observation.interpretation` | OI000018 | Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 66 | 477 | Observation | `Observation.interpretation` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 67 | 480 | Condition | `Condition.code.coding` | 47821001 | Postpartum hemorrhage | http://snomed.info/sct |
| 68 | 481 | Condition | `Condition.code.coding` | O86.8 | Other specified puerperal infections | http://hl7.org/fhir/sid/icd-10 |
| 69 | 482 | Condition | `Condition.code.coding` | 58703003 | Postpartum depression | http://snomed.info/sct |
| 70 | 483 | Condition | `Condition.code.coding` | O13 | Gestational [pregnancy-induced] hypertension without signification proteinuria | http://hl7.org/fhir/sid/icd-10 |
| 71 | 484 | Condition | `Condition.code.coding` | O90.8 | Other complications of the puerperium, not elsewhere classified | http://hl7.org/fhir/sid/icd-10 |
| 72 | 492 | Observation | `Observation.code.coding` | 289084000 | Difficulty performing breastfeeding | http://snomed.info/sct |
| 73 | 504 | Observation | `Observation.code.coding` | SP000122 | Catat di Buku KIA | http://terminology.kemkes.go.id/sp |
| 74 | 516 | Medication | `Medication.code` | 93015491 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | http://sys-ids.kemkes.go.id/kf |
| 75 | 533 | MedicationRequest | `MedicationRequest.contained.code.coding` | 92000653 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula | http://sys-ids.kemkes.go.id/kf |
| 76 | 567 | MedicationDispense | `MedicationDispense.contained.code.coding` | 93015491 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | http://sys-ids.kemkes.go.id/kf |
| 77 | 609 | Procedure | `Procedure.code.coding` | 767224000 | Administration of vitamin A | http://snomed.info/sct |
| 78 | 622 | MedicationRequest | `MedicationRequest.contained.code.coding` | 92000809 | Retinol Palmitate 200.000 IU Kapsul Lunak | http://sys-ids.kemkes.go.id/kf |
| 79 | 649 | MedicationDispense | `MedicationDispense.contained.code.coding` | 93018284 | Retinol Palmitate 200.000 IU Kapsul Lunak (Umum) | http://sys-ids.kemkes.go.id/kf |
| 80 | 673 | Procedure | `Procedure.code.coding` | 711029005 | Counseling about breastfeeding | http://snomed.info/sct |
| 81 | 684 | Procedure | `Procedure.code.coding` | ED000008 | Edukasi Tanda Bahaya Kehamilan, Bersalin dan Nifas | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 82 | 695 | Procedure | `Procedure.code.coding` | 72531000052105 | Counseling for contraception | http://snomed.info/sct |
| 83 | 706 | Procedure | `Procedure.code.coding` | SP000135 | Konseling Tanda Bahaya Bayi Baru Lahir | http://terminology.kemkes.go.id/sp |
| 84 | 717 | Procedure | `Procedure.code.coding` | 441041000124100 | Counseling about nutrition | http://snomed.info/sct |
| 85 | 728 | Procedure | `Procedure.code.coding` | PC000001 | Perawatan Tali Pusat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 86 | 739 | Procedure | `Procedure.code.coding` | ED000010 | Edukasi PHBS | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 87 | 753 | ServiceRequest | `ServiceRequest.code` | 32515-9 | CD3+CD4+ (T4 helper) cells [#/volume] in Specimen | http://loinc.org |
| 88 | 760 | PractitionerRole | `PractitionerRole.code.coding` | 1290220002 | Laboratory worker | http://snomed.info/sct |
| 89 | 763 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 90 | 772 | Observation | `Observation.code.coding` | 32515-9 | CD3+CD4+ (T4 helper) cells [#/volume] in Specimen | http://loinc.org |
| 91 | 785 | DiagnosticReport | `DiagnosticReport.code.coding` | 32515-9 | CD3+CD4+ (T4 helper) cells [#/volume] in Specimen | http://loinc.org |
| 92 | 797 | Observation | `Observation.code.coding` | SP000046 | Terapi Antiretroviral (ART) | http://terminology.kemkes.go.id/sp |
| 93 | 809 | Observation | `Observation.code.coding` | SP000124 | Obat anti malaria | http://terminology.kemkes.go.id/sp |
| 94 | 812 | Observation | `Observation.component.code.coding` | 432555000 | Product containing artesunate | http://snomed.info/sct |
| 95 | 815 | Observation | `Observation.component.code.coding` | 64115004 | Product containing amodiaquine | http://snomed.info/sct |
| 96 | 818 | Observation | `Observation.component.code.coding` | 324919005 | Product containing precisely quinine sulfate 200 milligram/1 each conventional release oral tablet | http://snomed.info/sct |
| 97 | 830 | Observation | `Observation.code.coding` | SP000125 | Obat anti tuberkulosis | http://terminology.kemkes.go.id/sp |
| 98 | 833 | Observation | `Observation.component.code.coding` | 29175007 | Product containing rifampicin | http://snomed.info/sct |
| 99 | 836 | Observation | `Observation.component.code.coding` | 81335000 | Product containing isoniazid | http://snomed.info/sct |
| 100 | 839 | Observation | `Observation.component.code.coding` | 13592004 | Product containing pyrazinamide | http://snomed.info/sct |
| 101 | 842 | Observation | `Observation.component.code.coding` | 24450004 | Product containing ethambutol | http://snomed.info/sct |
| 102 | 856 | ServiceRequest | `ServiceRequest.code` | 24648-8 | XR Chest PA upright | http://loinc.org |
| 103 | 864 | PractitionerRole | `PractitionerRole.code.coding` | 159016003 | Medical radiographer | http://snomed.info/sct |
| 104 | 868 | Observation | `Observation.code.coding` | 24648-8 | XR Chest PA upright | http://loinc.org |
| 105 | 869 | Observation | `Observation.valueCodeableConcept.coding` | 707307002 | Tuberculosis screening chest X-ray abnormal | http://snomed.info/sct |
| 106 | 870 | Observation | `Observation.valueCodeableConcept.coding` | 707308007 | Tuberculosis screening chest X-ray normal | http://snomed.info/sct |
| 107 | 871 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed |  |
| 108 | 881 | DiagnosticReport | `DiagnosticReport.code` | 24648-8 | XR Chest PA upright | http://loinc.org |
| 109 | 892 | Observation | `Observation.code.coding` | SP000139 | KB Pasca Plasenta | http://terminology.kemkes.go.id/sp |
| 110 | 893 | Observation | `Observation.valueCodeableConcept.coding` | LA6524-8 | Oral contraceptive pill | http://loinc.org |
| 111 | 894 | Observation | `Observation.valueCodeableConcept.coding` | 237122005 | Lactational amenorrhea | http://snomed.info/sct |
| 112 | 895 | Observation | `Observation.valueCodeableConcept.coding` | LA6525-5 | Injectable/implantable hormone | http://loinc.org |
| 113 | 896 | Observation | `Observation.valueCodeableConcept.coding` | LA6527-1 | Intrauterine device | http://loinc.org |
| 114 | 897 | Observation | `Observation.valueCodeableConcept.coding` | SP000097 | Implan | http://terminology.kemkes.go.id/sp |
| 115 | 898 | Observation | `Observation.valueCodeableConcept.coding` | LA6523-0 | Condom | http://loinc.org |
| 116 | 899 | Observation | `Observation.valueCodeableConcept.coding` | 22523008 | Vasectomy | http://snomed.info/sct |
| 117 | 900 | Observation | `Observation.valueCodeableConcept.coding` | 77543007 | Ligation of fallopian tube | http://snomed.info/sct |
| 118 | 910 | Observation | `Observation.code.coding` | SP000139 | KB Pasca Plasenta | http://terminology.kemkes.go.id/sp |
| 119 | 922 | Observation | `Observation.code.coding` | PC000004 | KB Pasca Persalinan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 120 | 923 | Observation | `Observation.valueCodeableConcept.coding` | LA6524-8 | Oral contraceptive pill | http://loinc.org |
| 121 | 924 | Observation | `Observation.valueCodeableConcept.coding` | 237122005 | Lactational amenorrhea | http://snomed.info/sct |
| 122 | 925 | Observation | `Observation.valueCodeableConcept.coding` | LA6525-5 | Injectable/implantable hormone | http://loinc.org |
| 123 | 926 | Observation | `Observation.valueCodeableConcept.coding` | LA6527-1 | Intrauterine device | http://loinc.org |
| 124 | 927 | Observation | `Observation.valueCodeableConcept.coding` | SP000097 | Implan | http://terminology.kemkes.go.id/sp |
| 125 | 928 | Observation | `Observation.valueCodeableConcept.coding` | LA6523-0 | Condom | http://loinc.org |
| 126 | 929 | Observation | `Observation.valueCodeableConcept.coding` | 22523008 | Vasectomy | http://snomed.info/sct |
| 127 | 930 | Observation | `Observation.valueCodeableConcept.coding` | 77543007 | Ligation of fallopian tube | http://snomed.info/sct |
| 128 | 940 | Observation | `Observation.code.coding` | PC000004 | KB Pasca Persalinan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 129 | 962 | Observation | `Observation.code.coding` | SP000380 | Tatalaksana Komplikasi Pendarahan | http://terminology.kemkes.go.id/sp |
| 130 | 965 | Observation | `Observation.component.code.coding` | SP000008 | Pemberian Tablet Tambah Darah | http://terminology.kemkes.go.id/sp |
| 131 | 968 | Observation | `Observation.component.code.coding` | 116859006 | Transfusion of blood product | http://snomed.info/sct |
| 132 | 971 | Observation | `Observation.component.code.coding` | 74964007 | Other | http://snomed.info/sct |
| 133 | 982 | Observation | `Observation.code.coding` | 736286003 | Hypertension clinical management plan | http://snomed.info/sct |
| 134 | 985 | Observation | `Observation.component.code.coding` | 135840009 | Blood pressure monitoring | http://snomed.info/sct |
| 135 | 988 | Observation | `Observation.component.code.coding` | SP000133 | Pemantauan Protein Urin | http://terminology.kemkes.go.id/sp |
| 136 | 1001 | Observation | `Observation.code.coding` | SP000138 | Tatalaksana Komplikasi Pre Eklampsia | http://terminology.kemkes.go.id/sp |
| 137 | 1004 | Observation | `Observation.component.code.coding` | 135840009 | Blood pressure monitoring | http://snomed.info/sct |
| 138 | 1007 | Observation | `Observation.component.code.coding` | SP000133 | Pemantauan Protein Urin | http://terminology.kemkes.go.id/sp |
| 139 | 1010 | Observation | `Observation.component.code.coding` | 74964007 | Other | http://snomed.info/sct |
| 140 | 1011 | Observation | `Observation.component.code` | 308116003 | Antihypertensive therapy | http://snomed.info/sct |
| 141 | 1014 | Observation | `Observation.component.code.coding` | SP000136 | Pemberian MgSO4 | http://terminology.kemkes.go.id/sp |
| 142 | 1017 | Observation | `Observation.component.code.coding` | SP000137 | Pemberian Diazepam Injeksi | http://terminology.kemkes.go.id/sp |
| 143 | 1030 | Observation | `Observation.code.coding` | SP000389 | Keadaan Ibu | http://terminology.kemkes.go.id/sp |
| 144 | 1031 | Observation | `Observation.valueCodeableConcept.coding` | 438949009 | Alive | http://snomed.info/sct |
| 145 | 1032 | Observation | `Observation.valueCodeableConcept.coding` | 419099009 | Dead | http://snomed.info/sct |
| 146 | 1042 | Condition | `Condition.code.coding` | 359746009 | Patient’s condition stable | http://snomed.info/sct |
| 147 | 1043 | Condition | `Condition.code.coding` | 162668006 | Patient’s condition unstable | http://snomed.info/sct |
| 148 | 1044 | Condition | `Condition.code.coding` | 268910001 | Patient’s condition improved | http://snomed.info/sct |
| 149 | 1058 | ServiceRequest | `ServiceRequest.code.coding` | 409014006 | Delivery care management | http://snomed.info/sct |
| 150 | 1067 | ServiceRequest | `ServiceRequest.locationCode.coding` | SP000129 | Puskesmas PONED | http://terminology.kemkes.go.id/sp |
| 151 | 1071 | ServiceRequest | `ServiceRequest.locationCode.coding` | SP000128 | Rumah Sakit Ibu dan Anak | http://terminology.kemkes.go.id/sp |
| 152 | 1077 | Observation | `Observation.code.coding` | 35025007 | Manual pelvic examination | http://snomed.info/sct |
| 153 | 1087 | Observation | `Observation.code.coding` | 81956-5 | Date and time of death [TimeStamp] | http://loinc.org |
| 154 | 1098 | Observation | `Observation.code.coding` | SP000666 | Hari setelah melahirkan | http://terminology.kemkes.go.id/sp |
| 155 | 1109 | Observation | `Observation.code.coding` | 8665-2 | Last menstrual period start date | http://loinc.org |
| 156 | 1110 | Observation | `Observation.code.coding` | ANC.B6.DE14 | Last menstrual period (LMP) date | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 157 | 1122 | Observation | `Observation.code.coding` | 11778-8 | Delivery date Estimated | http://loinc.org |
| 158 | 1123 | Observation | `Observation.code.coding` | ANC.B6.DE22 | Expected date of delivery (EDD) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 159 | 1136 | Observation | `Observation.code.coding` | SP000050 | Riwayat Onset Persalinan | http://terminology.kemkes.go.id/sp |
| 160 | 1138 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 161 | 1149 | Observation | `Observation.code.coding` | SP000132 | Memiliki Buku KIA | http://terminology.kemkes.go.id/sp |
| 162 | 1161 | Observation | `Observation.code.coding` | 56077-1 | Body weight --pre current pregnancy | http://loinc.org |
| 163 | 1162 | Observation | `Observation.code.coding` | ANC.B8.DE2 | Pre-gestational weight | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 164 | 1175 | Observation | `Observation.code.coding` | 11977-6 | [#] Parity | http://loinc.org |
| 165 | 1176 | Observation | `Observation.code.coding` | ANC.B6.DE32 | Parity | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 166 | 1188 | Observation | `Observation.code.coding` | SP000667 | Penanganan Risiko Tinggi dan Komplikasi | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 65 |
| http://loinc.org | 33 |
| http://terminology.kemkes.go.id/sp | 29 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 13 |
| http://terminology.kemkes.go.id/CodeSystem/organization-type | 5 |
| http://sys-ids.kemkes.go.id/kf | 5 |
| http://hl7.org/fhir/sid/icd-10 | 4 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 4 |
| hhttp://terminology.kemkes.go.id/CodeSystem/organization-type | 3 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 1 |
| http://terminology.kemkes.go.id/CodeSystem/location-type | 1 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 1 |
|  | 1 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 1 |
| **Total** | **166** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 30 | – | Jenis Faskes | Organization | `Organization.type` |
| 34 | – | Nama Faskes | Organization | `Organization.name` |
| 41 | – | provinsi | Organization | `Organization.address.extension.extension.url` |
| 44 | – | kabupaten | Organization | `Organization.address.extension.extension.url` |
| 1027 | – | Keadaan_Tiba | – | `` |
