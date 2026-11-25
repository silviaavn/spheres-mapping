# Output Form: SIM RS PKU PNC

Sumber: `mapping/phdt-data-dictionary-rs-pku-pnc.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-rs-pku-pnc.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 67 |
| Code (`jumlah code` = 1) | 133 |
| Code unik (code + CodeSystem) | 130 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 23 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–27 | Patient | – | – | _Nama Ibu_ → `Patient.name.text` (2, tanpa BQ)<br>_NIK_ → `Patient.identifier.value` (6, tanpa BQ)<br>_No HP_ → `Patient.telecom` (7, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (10, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (11, tanpa BQ)<br>_Alamat Domisili_ → `Patient.address.line` (13, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.city` (14, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (18, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (21, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.extension.valueCode` (24, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.extension.valueCode` (27, tanpa BQ) |
| 2 | 66–72 | Practitioner | – | – | _NIK_ → `Practitioner.identifier.value` (68, tanpa BQ)<br>_Nama Tenaga Kesehatan_ → `Practitioner.name.text` (70, tanpa BQ)<br>_Jenis Kelamin Tenaga Kesehatan_ → `Practitioner.gender` (71, tanpa BQ) |
| 3 | 73–80 | PractitionerRole | – | – | _Tenaga Pemeriksa_ → `PractitionerRole.code.coding` (77, tanpa BQ) |
| 4 | 82–101 | Encounter | – | – | _Tanggal Kunjungan PNC_ → `Encounter.period.start` (89, tanpa BQ)<br>_Tempat Pelayanan PNC_ → `Encounter.location.location.display` (92, tanpa BQ)<br>_Cara Masuk_ → `Encounter.hospitalization.admitSource.coding` (93, tanpa BQ) |
| 5 | 102–110 | Condition | Z39.2 | Routine postpartum follow-up | _Kode ICD - Diagnosa_ → `Condition.clinicalStatus.coding` (102, tanpa BQ) |
| 6 | 113–121 | Condition | 404684003.0 | Clinical finding | _Keluhan_ → `Condition.clinicalStatus.coding` (113, tanpa BQ) |
| 7 | 132–140 | EpisodeOfCare | PNC | Postnatal Care | – |
| 8 | 141–152 | Observation | 93857-1 | Date and time of obstetric delivery | _Tanggal Persalinan_ → `Observation.valueDateTime` (144, tanpa BQ) |
| 9 | 153–164 | Observation | 11996-6 | [#] Pregnancies | _Gravida_ → `Observation.valueInteger` (157, tanpa BQ) |
| 10 | 165–176 | Observation | 11977-6 | [#] Parity | _Partus_ → `Observation.valueInteger` (169, tanpa BQ) |
| 11 | 177–188 | Observation | 69043-8 | Other pregnancy outcomes # | _Abortus_ → `Observation.valueInteger` (181, tanpa BQ) |
| 12 | 189–200 | Observation | 8480-6 | Systolic blood pressure | _Tekanan Darah Sistolik_ → `Observation.valueQuantity.value` (192, tanpa BQ) |
| 13 | 201–212 | Observation | 8462-4 | Diastolic blood pressure | _Tekanan Darah Diastolik_ → `Observation.valueQuantity.value` (204, tanpa BQ) |
| 14 | 213–225 | Observation | 8867-4 | Heart rate | _Nadi_ → `Observation.valueQuantity.value` (216, tanpa BQ) |
| 15 | 226–238 | Observation | – | – | _Suhu_ → `Observation.valueQuantity.value` (229, tanpa BQ) |
| 16 | 239–251 | Observation | 9279-1 | Respiratory rate | _Pernapasan_ → `Observation.valueQuantity.value` (242, tanpa BQ) |
| 17 | 252–262 | Observation | SP000683 | Tatalaksana Tindakan | _Tatalaksana (Tindakan)_ → `Observation.valueString` (255, tanpa BQ) |
| 18 | 263–273 | Observation | SP000684 | Tatalaksana Obat | _Tatalaksana Obat_ → `Observation.valueString` (266, tanpa BQ) |
| 19 | 274–282 | Condition | 199745000.0 | Complication occurring during labor and delivery | _Komplikasi_ → `Condition.clinicalStatus.coding` (274, tanpa BQ) |
| 20 | 284–290 | Condition | 289530006.0 | Vaginal bleeding | _Pendarahan Pervaginam_ → `Condition.clinicalStatus.coding` (284, tanpa BQ) |
| 21 | 291–302 | Observation | 81661-1 | Blood Loss [Volume] Measured | _Jumlah Pendarahan_ → `Observation.valueQuantity.value` (294, tanpa BQ) |
| 22 | 303–313 | Observation | 364297003.0 | Female perineum observable | _Kondisi Perineum_ → `Observation.valueString` (306, tanpa BQ) |
| 23 | 314–325 | Observation | OC000020 | Tanda Infeksi Perineum | _Tanda Infeksi Perineum_ → `Observation.valueBoolean` (317, tanpa BQ) |
| 24 | 326–337 | Observation | OC000025 | Tanda Infeksi Luka Jahitan Sectio Caesaria | _Tanda Infeksi Luka Jahitan Sectio Caesaria_ → `Observation.valueBoolean` (329, tanpa BQ) |
| 25 | 338–352 | Observation | 32422-8 | Physical findings of breast | _Kondisi Payudara_ → `Observation.valueCodeableConcept.coding` (341, tanpa BQ) |
| 26 | 353–364 | Observation | 289700000.0 | Uterine contractions present | _Kontraksi Uteri_ → `Observation.valueBoolean` (356, tanpa BQ) |
| 27 | 365–378 | Observation | 249214003.0 | Color of lochia | _Warna Lokhia_ → `Observation.valueCodeableConcept.coding` (368, tanpa BQ) |
| 28 | 379–390 | Observation | 249215002.0 | Odor of lochia | _Bau Lokhia_ → `Observation.valueBoolean` (382, tanpa BQ) |
| 29 | 391–403 | Observation | OC000017 | Produksi ASI | _Produksi ASI_ → `Observation.valueCodeableConcept.coding` (394, tanpa BQ) |
| 30 | 404–415 | Observation | 1145307003.0 | Exclusively breastfed | _ASI Eksklusif_ → `Observation.valueBoolean` (407, tanpa BQ) |
| 31 | 416–433 | Observation | 252041008.0 | Micturition finding | _Gangguan Buang Air Kecil_ → `Observation.valueBoolean` (419, tanpa BQ) |
| 32 | 434–445 | Observation | 300375001.0 | Able to defecate | _Gangguan Buang Air Besar_ → `Observation.valueBoolean` (437, tanpa BQ) |
| 33 | 446–456 | Procedure | 408988007.0 | Newborn care education | _Konseling Perawatan Bayi Baru Lahir_ → `Procedure.category.coding` (446, tanpa BQ) |
| 34 | 457–468 | Observation | 8345-1 | Body weight Measured --post partum | _Berat Badan_ → `Observation.valueQuantity.value` (460, tanpa BQ) |
| 35 | 469–480 | Observation | 8305-5 | Body height --post partum | _Tinggi Badan_ → `Observation.valueQuantity.value` (472, tanpa BQ) |
| 36 | 481–494 | Observation | 284473002.0 | Mid upper arm circumference | _LILA_ → `Observation.valueQuantity.value` (484, tanpa BQ)<br>_Status Gizi KEK/Tidak KEK_ → `Observation.interpretation` (493, tanpa BQ) |
| 37 | 495–507 | Observation | 11881-0 | Uterus Fundal height Tape measure | _TFU_ → `Observation.valueString` (498, tanpa BQ) |
| 38 | 508–525 | Condition | 47821001.0 | Postpartum hemorrhage | _Komplikasi Masa Nifas_ → `Condition.clinicalStatus.coding` (508, tanpa BQ) |
| 39 | 526–539 | Observation | 289084000.0 | Difficulty performing breastfeeding | _Apakah ada masalah memberikan ASI_ → `Observation.valueBoolean` (529, tanpa BQ)<br>_Catatan ASI_ → `Observation.note.text` (538, tanpa BQ)<br>_Catat dibuku KIA_ → `Observation.category.coding` (539, tanpa BQ) |
| 40 | 540–550 | Observation | SP000122 | Catat di Buku KIA | – |
| 41 | 551–552 | MedicationDispense | – | – | _Diberikan Tablet FE_ → `MedicationDispense.status` (551, tanpa BQ) |
| 42 | 553–567 | Medication | – | – | – |
| 43 | 568–573 | MedicationRequest | – | – | – |
| 44 | 574–588 | Medication | – | – | – |
| 45 | 589–594 | MedicationDispense | – | – | – |
| 46 | 595–628 | MedicationRequest | 92000653.0 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula | _Jumlah Tablet Fe yang didapatkan (butir)_ → `MedicationRequest.contained.resourceType` (595, tanpa BQ) |
| 47 | 629–660 | MedicationDispense | 93015491.0 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | – |
| 48 | 661–670 | Procedure | 767224000.0 | Administration of vitamin A | _Pemberian Vitamin A_ → `Procedure.category.coding` (661, tanpa BQ) |
| 49 | 671–681 | Procedure | 711029005.0 | Counseling about breastfeeding | _Konseling ASI_ → `Procedure.category.coding` (671, tanpa BQ) |
| 50 | 682–692 | Procedure | ED000008 | Edukasi Tanda Bahaya Kehamilan, Bersalin dan Nifas | _Tanda Bahaya Nifas_ → `Procedure.category.coding` (682, tanpa BQ) |
| 51 | 693–703 | Procedure | 72531000052105.0 | Counseling for contraception | _Konseling KB_ → `Procedure.category.coding` (693, tanpa BQ) |
| 52 | 704–714 | Procedure | SP000135 | Konseling Tanda Bahaya Bayi Baru Lahir | _Konseling Tanda Bahaya Bayi Baru Lahir_ → `Procedure.category.coding` (704, tanpa BQ) |
| 53 | 715–725 | Procedure | 441041000124100.0 | Counseling about nutrition | _Konseling Gizi_ → `Procedure.category.coding` (715, tanpa BQ) |
| 54 | 726–736 | Procedure | PC000001 | Perawatan Tali Pusat | _Konseling Perawatan Tali Pusar_ → `Procedure.category.coding` (726, tanpa BQ) |
| 55 | 737–747 | Procedure | ED000010 | Edukasi PHBS | _Konseling PHBS_ → `Procedure.category.coding` (737, tanpa BQ) |
| 56 | 748–758 | Procedure | ED000012 | Edukasi lainnya | _Konseling Jiwa Pascasalin_ → `Procedure.category.coding` (748, tanpa BQ) |
| 57 | 759–770 | Observation | SP000046 | Terapi Antiretroviral (ART) | _ART_ → `Observation.valueBoolean` (762, tanpa BQ) |
| 58 | 771–782 | Observation | 395264002.0 | Product containing tenofovir | _Obat Hepatitis (Tenofovir)_ → `Observation.valueBoolean` (774, tanpa BQ) |
| 59 | 783–803 | Observation | SP000124 | Obat anti malaria | _Obat Anti Malaria_ → `Observation.valueBoolean` (786, tanpa BQ) |
| 60 | 804–827 | Observation | SP000125 | Obat anti tuberkulosis | _Obat Anti Tuberkulosis (OAT)_ → `Observation.valueBoolean` (807, tanpa BQ) |
| 61 | 828–845 | Observation | PC000004 | KB Pasca Persalinan | _Metode Kontrasepsi KB Pasca Persalinan_ → `Observation.valueCodeableConcept.coding` (831, tanpa BQ) |
| 62 | 846–863 | Observation | SP000380 | Tatalaksana Komplikasi Pendarahan | _Tatalaksana Komplikasi Pendarahan_ → `Observation.valueBoolean` (849, tanpa BQ)<br>_Pemberian Tablet FE_ → `Observation.component.code.coding` (851, tanpa BQ)<br>_Transfusi Darah_ → `Observation.component.code.coding` (854, tanpa BQ) |
| 63 | 864–881 | Observation | 736286003 | Hypertension clinical management plan | _Tatalaksana Komplikasi Hipertensi_ → `Observation.valueBoolean` (867, tanpa BQ)<br>_Pantau Tekanan Darah_ → `Observation.component.code.coding` (869, tanpa BQ)<br>_Pantau Protein Urin_ → `Observation.component.code.coding` (872, tanpa BQ) |
| 64 | 882–908 | Observation | SP000138 | Tatalaksana Komplikasi Pre Eklampsia | _Tatalaksana Komplikasi Pre Eklampsia dan Eklampsia_ → `Observation.valueBoolean` (885, tanpa BQ)<br>_Pantau Tekanan Darah_ → `Observation.component.code.coding` (887, tanpa BQ)<br>_Pantau Protein Urin_ → `Observation.component.code.coding` (890, tanpa BQ)<br>_Pemberian Anti Hipertensi_ → `Observation.component.code` (893, tanpa BQ)<br>_Pemberian MgSO4_ → `Observation.component.code.coding` (896, tanpa BQ)<br>_Pemberian Diazepam Injeksi_ → `Observation.component.code.coding` (899, tanpa BQ) |
| 65 | 910–921 | Observation | SP000389 | Keadaan Ibu | – |
| 66 | 922–930 | Condition | 359746009.0 | Patient’s condition stable | _Keadaan Pulang_ → `Condition.clinicalStatus.coding` (922, tanpa BQ) |
| 67 | 931–950 | ServiceRequest | 409014006.0 | Delivery care management | _Tanggal Dirujuk_ → `ServiceRequest.occurrenceDateTime` (939, tanpa BQ)<br>_Faskes Rujukan_ → `ServiceRequest.locationCode.coding` (943, tanpa BQ)<br>_Nama Faskes Rujukan_ → `ServiceRequest.locationCode.text` (950, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 38 |
| Procedure | 10 |
| Condition | 6 |
| MedicationDispense | 3 |
| Medication | 2 |
| MedicationRequest | 2 |
| Patient | 1 |
| Practitioner | 1 |
| PractitionerRole | 1 |
| Encounter | 1 |
| EpisodeOfCare | 1 |
| ServiceRequest | 1 |
| **Total** | **67** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 77 | PractitionerRole | `PractitionerRole.code.coding` | 309453006.0 | Registered midwife | http://snomed.info/sct |
| 2 | 78 | PractitionerRole | `PractitionerRole.code.coding` | 309367003.0 | Obstetrician and gynecologist | http://snomed.info/sct |
| 3 | 79 | PractitionerRole | `PractitionerRole.code.coding` | 309343006.0 | Physician | http://snomed.info/sct |
| 4 | 80 | PractitionerRole | `PractitionerRole.code.coding` | 224535009.0 | Registered nurse | http://snomed.info/sct |
| 5 | 93 | Encounter | `Encounter.hospitalization.admitSource.coding` | EHA000002 | Datang sendiri | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 6 | 94 | Encounter | `Encounter.hospitalization.admitSource.coding` | 305956004.0 | Referral by physician | http://snomed.info/sct |
| 7 | 95 | Encounter | `Encounter.hospitalization.admitSource.coding` | 306052007.0 | Referral by midwife | http://snomed.info/sct |
| 8 | 96 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000116 | Rujukan dari Puskesmas Pembantu | http://terminology.kemkes.go.id/sp |
| 9 | 97 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000117 | Rujukan dari Puskesmas | http://terminology.kemkes.go.id/sp |
| 10 | 98 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000118 | Rujukan dari Rumah Bersalin / Klinik | http://terminology.kemkes.go.id/sp |
| 11 | 99 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000119 | Rujukan dari Rumah Sakit | http://terminology.kemkes.go.id/sp |
| 12 | 105 | Condition | `Condition.code.coding` | Z39.2 | Routine postpartum follow-up | http://hl7.org/fhir/sid/icd-10 |
| 13 | 115 | Condition | `Condition.code.coding` | 404684003.0 | Clinical finding | http://snomed.info/sct |
| 14 | 133 | EpisodeOfCare | `EpisodeOfCare.type.coding` | PNC | Postnatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 15 | 143 | Observation | `Observation.code.coding` | 93857-1 | Date and time of obstetric delivery | http://loinc.org |
| 16 | 155 | Observation | `Observation.code.coding` | 11996-6 | [#] Pregnancies | http://loinc.org |
| 17 | 156 | Observation | `Observation.code.coding` | ANC.B6.DE24 | Number of pregnancies (gravida) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 18 | 167 | Observation | `Observation.code.coding` | 11977-6 | [#] Parity | http://loinc.org |
| 19 | 168 | Observation | `Observation.code.coding` | ANC.B6.DE32 | Parity | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 20 | 179 | Observation | `Observation.code.coding` | 69043-8 | Other pregnancy outcomes # | http://loinc.org |
| 21 | 180 | Observation | `Observation.code.coding` | ANC.B6.DE25 | Number of miscarriages and/or abortions | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 22 | 191 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 23 | 203 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://loinc.org |
| 24 | 215 | Observation | `Observation.code.coding` | 8867-4 | Heart rate | http://loinc.org |
| 25 | 241 | Observation | `Observation.code.coding` | 9279-1 | Respiratory rate | http://loinc.org |
| 26 | 254 | Observation | `Observation.code.coding` | SP000683 | Tatalaksana Tindakan | http://terminology.kemkes.go.id/sp |
| 27 | 265 | Observation | `Observation.code.coding` | SP000684 | Tatalaksana Obat | http://terminology.kemkes.go.id/sp |
| 28 | 276 | Condition | `Condition.code.coding` | 199745000.0 | Complication occurring during labor and delivery | http://snomed.info/sct |
| 29 | 286 | Condition | `Condition.code.coding` | 289530006.0 | Vaginal bleeding | http://snomed.info/sct |
| 30 | 293 | Observation | `Observation.code.coding` | 81661-1 | Blood Loss [Volume] Measured | http://loinc.org |
| 31 | 305 | Observation | `Observation.code.coding` | 364297003.0 | Female perineum observable | http://loinc.org |
| 32 | 316 | Observation | `Observation.code.coding` | OC000020 | Tanda Infeksi Perineum | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 33 | 328 | Observation | `Observation.code.coding` | OC000025 | Tanda Infeksi Luka Jahitan Sectio Caesaria | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 34 | 340 | Observation | `Observation.code.coding` | 32422-8 | Physical findings of breast | http://loinc.org |
| 35 | 341 | Observation | `Observation.valueCodeableConcept.coding` | 300885006.0 | Swelling of breast | http://snomed.info/sct |
| 36 | 342 | Observation | `Observation.valueCodeableConcept.coding` | 290070001.0 | Red breast | http://snomed.info/sct |
| 37 | 343 | Observation | `Observation.valueCodeableConcept.coding` | 54302000.0 | Discharge from nipple | http://snomed.info/sct |
| 38 | 344 | Observation | `Observation.valueCodeableConcept.coding` | 53430007.0 | Pain of breast | http://snomed.info/sct |
| 39 | 345 | Observation | `Observation.valueCodeableConcept.coding` | 290084006.0 | Breast normal | http://snomed.info/sct |
| 40 | 355 | Observation | `Observation.code.coding` | 289700000.0 | Uterine contractions present | http://snomed.info/sct |
| 41 | 367 | Observation | `Observation.code.coding` | 249214003.0 | Color of lochia | http://snomed.info/sct |
| 42 | 368 | Observation | `Observation.valueCodeableConcept.coding` | 278072004.0 | Lochia rubra | http://snomed.info/sct |
| 43 | 369 | Observation | `Observation.valueCodeableConcept.coding` | 449828001.0 | Lochia serosa | http://snomed.info/sct |
| 44 | 370 | Observation | `Observation.valueCodeableConcept.coding` | 113291006.0 | Lochia sanguinolenta | http://snomed.info/sct |
| 45 | 371 | Observation | `Observation.valueCodeableConcept.coding` | 449827006.0 | Lochia alba | http://snomed.info/sct |
| 46 | 381 | Observation | `Observation.code.coding` | 249215002.0 | Odor of lochia | http://snomed.info/sct |
| 47 | 393 | Observation | `Observation.code.coding` | OC000017 | Produksi ASI | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 48 | 394 | Observation | `Observation.valueCodeableConcept.coding` | OV000016 | Produksi ASI ada | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 49 | 395 | Observation | `Observation.valueCodeableConcept.coding` | OV000017 | Produksi ASI ada tapi sedikit | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 50 | 396 | Observation | `Observation.valueCodeableConcept.coding` | OV000018 | Produksi ASI tidak ada | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 51 | 406 | Observation | `Observation.code.coding` | 1145307003.0 | Exclusively breastfed | http://snomed.info/sct |
| 52 | 418 | Observation | `Observation.code.coding` | 252041008.0 | Micturition finding | http://snomed.info/sct |
| 53 | 421 | Observation | `Observation.valueCodeableConcept.coding` | 49650001.0 | Dysuria | http://snomed.info/sct |
| 54 | 422 | Observation | `Observation.valueCodeableConcept.coding` | 249288007.0 | Incomplete emptying of urinary bladder | http://snomed.info/sct |
| 55 | 423 | Observation | `Observation.valueCodeableConcept.coding` | 162116003.0 | Increased frequency of urination | http://snomed.info/sct |
| 56 | 424 | Observation | `Observation.valueCodeableConcept.coding` | 42112009.0 | Enuresis | http://snomed.info/sct |
| 57 | 425 | Observation | `Observation.valueCodeableConcept.coding` | 102834005.0 | Normal micturition | http://snomed.info/sct |
| 58 | 426 | Observation | `Observation.valueCodeableConcept.coding` | 267064002.0 | Retention of urine | http://snomed.info/sct |
| 59 | 436 | Observation | `Observation.code.coding` | 300375001.0 | Able to defecate | http://snomed.info/sct |
| 60 | 447 | Procedure | `Procedure.code.coding` | 408988007.0 | Newborn care education | http://snomed.info/sct |
| 61 | 459 | Observation | `Observation.code.coding` | 8345-1 | Body weight Measured --post partum | http://loinc.org |
| 62 | 471 | Observation | `Observation.code.coding` | 8305-5 | Body height --post partum | http://loinc.org |
| 63 | 483 | Observation | `Observation.code.coding` | 284473002.0 | Mid upper arm circumference | http://snomed.info/sct |
| 64 | 493 | Observation | `Observation.interpretation` | OI000018 | Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 65 | 494 | Observation | `Observation.interpretation` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 66 | 497 | Observation | `Observation.code.coding` | 11881-0 | Uterus Fundal height Tape measure | http://loinc.org |
| 67 | 510 | Condition | `Condition.code.coding` | 47821001.0 | Postpartum hemorrhage | http://snomed.info/sct |
| 68 | 511 | Condition | `Condition.code.coding` | 198188007.0 | Chronic uterine inflammatory disease | http://snomed.info/sct |
| 69 | 512 | Condition | `Condition.code.coding` | 111367007.0 | Pelvic abscess | http://snomed.info/sct |
| 70 | 513 | Condition | `Condition.code.coding` | 211063003.0 | Infected abrasion of perineum | http://snomed.info/sct |
| 71 | 514 | Condition | `Condition.code.coding` | 76902006.0 | Tetanus | http://snomed.info/sct |
| 72 | 515 | Condition | `Condition.code.coding` | 266579006.0 | Inflammatory disorder of breast | http://snomed.info/sct |
| 73 | 516 | Condition | `Condition.code.coding` | 49746001.0 | Engorgement of breasts | http://snomed.info/sct |
| 74 | 517 | Condition | `Condition.code.coding` | 82231009.0 | Inversion of nipple | http://snomed.info/sct |
| 75 | 518 | Condition | `Condition.code.coding` | 58703003.0 | Postpartum depression | http://snomed.info/sct |
| 76 | 519 | Condition | `Condition.code.coding` | O13 | Gestational [pregnancy-induced] hypertension without signification proteinuria | http://hl7.org/fhir/sid/icd-10 |
| 77 | 520 | Condition | `Condition.code.coding` | O90.8 | Other complications of the puerperium, not elsewhere classified | http://hl7.org/fhir/sid/icd-10 |
| 78 | 528 | Observation | `Observation.code.coding` | 289084000.0 | Difficulty performing breastfeeding | http://snomed.info/sct |
| 79 | 540 | Observation | `Observation.code.coding` | SP000122 | Catat di Buku KIA | http://terminology.kemkes.go.id/sp |
| 80 | 554 | Medication | `Medication.code` | 92000653.0 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula | http://sys-ids.kemkes.go.id/kf |
| 81 | 575 | Medication | `Medication.code` | 93015491.0 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | http://sys-ids.kemkes.go.id/kf |
| 82 | 598 | MedicationRequest | `MedicationRequest.contained.code.coding` | 92000653.0 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula | http://sys-ids.kemkes.go.id/kf |
| 83 | 632 | MedicationDispense | `MedicationDispense.contained.code.coding` | 93015491.0 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | http://sys-ids.kemkes.go.id/kf |
| 84 | 662 | Procedure | `Procedure.code.coding` | 767224000.0 | Administration of vitamin A | http://snomed.info/sct |
| 85 | 672 | Procedure | `Procedure.code.coding` | 711029005.0 | Counseling about breastfeeding | http://snomed.info/sct |
| 86 | 683 | Procedure | `Procedure.code.coding` | ED000008 | Edukasi Tanda Bahaya Kehamilan, Bersalin dan Nifas | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 87 | 694 | Procedure | `Procedure.code.coding` | 72531000052105.0 | Counseling for contraception | http://snomed.info/sct |
| 88 | 705 | Procedure | `Procedure.code.coding` | SP000135 | Konseling Tanda Bahaya Bayi Baru Lahir | http://terminology.kemkes.go.id/sp |
| 89 | 716 | Procedure | `Procedure.code.coding` | 441041000124100.0 | Counseling about nutrition | http://snomed.info/sct |
| 90 | 727 | Procedure | `Procedure.code.coding` | PC000001 | Perawatan Tali Pusat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 91 | 738 | Procedure | `Procedure.code.coding` | ED000010 | Edukasi PHBS | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 92 | 749 | Procedure | `Procedure.code.coding` | ED000012 | Edukasi lainnya | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 93 | 761 | Observation | `Observation.code.coding` | SP000046 | Terapi Antiretroviral (ART) | http://terminology.kemkes.go.id/sp |
| 94 | 773 | Observation | `Observation.code.coding` | 395264002.0 | Product containing tenofovir | http://snomed.info/sct |
| 95 | 785 | Observation | `Observation.code.coding` | SP000124 | Obat anti malaria | http://terminology.kemkes.go.id/sp |
| 96 | 788 | Observation | `Observation.component.code.coding` | 432555000.0 | Product containing artesunate | http://snomed.info/sct |
| 97 | 791 | Observation | `Observation.component.code.coding` | 64115004.0 | Product containing amodiaquine | http://snomed.info/sct |
| 98 | 794 | Observation | `Observation.component.code.coding` | 324919005.0 | Product containing precisely quinine sulfate 200 milligram/1 each conventional release oral tablet | http://snomed.info/sct |
| 99 | 806 | Observation | `Observation.code.coding` | SP000125 | Obat anti tuberkulosis | http://terminology.kemkes.go.id/sp |
| 100 | 809 | Observation | `Observation.component.code.coding` | 29175007.0 | Product containing rifampicin | http://snomed.info/sct |
| 101 | 812 | Observation | `Observation.component.code.coding` | 81335000.0 | Product containing isoniazid | http://snomed.info/sct |
| 102 | 815 | Observation | `Observation.component.code.coding` | 13592004.0 | Product containing pyrazinamide | http://snomed.info/sct |
| 103 | 818 | Observation | `Observation.component.code.coding` | 24450004.0 | Product containing ethambutol | http://snomed.info/sct |
| 104 | 830 | Observation | `Observation.code.coding` | PC000004 | KB Pasca Persalinan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 105 | 831 | Observation | `Observation.valueCodeableConcept.coding` | LA6524-8 | Oral contraceptive pill | http://loinc.org |
| 106 | 832 | Observation | `Observation.valueCodeableConcept.coding` | 237122005.0 | Lactational amenorrhea | http://snomed.info/sct |
| 107 | 833 | Observation | `Observation.valueCodeableConcept.coding` | LA6525-5 | Injectable/implantable hormone | http://loinc.org |
| 108 | 834 | Observation | `Observation.valueCodeableConcept.coding` | LA6527-1 | Intrauterine device | http://loinc.org |
| 109 | 835 | Observation | `Observation.valueCodeableConcept.coding` | SP000097 | Implan | http://terminology.kemkes.go.id/sp |
| 110 | 836 | Observation | `Observation.valueCodeableConcept.coding` | LA6523-0 | Condom | http://loinc.org |
| 111 | 837 | Observation | `Observation.valueCodeableConcept.coding` | 22523008.0 | Vasectomy | http://snomed.info/sct |
| 112 | 838 | Observation | `Observation.valueCodeableConcept.coding` | 77543007.0 | Ligation of fallopian tube | http://snomed.info/sct |
| 113 | 848 | Observation | `Observation.code.coding` | SP000380 | Tatalaksana Komplikasi Pendarahan | http://terminology.kemkes.go.id/sp |
| 114 | 851 | Observation | `Observation.component.code.coding` | SP000008 | Pemberian Tablet Tambah Darah | http://terminology.kemkes.go.id/sp |
| 115 | 854 | Observation | `Observation.component.code.coding` | 116859006.0 | Transfusion of blood product | http://snomed.info/sct |
| 116 | 866 | Observation | `Observation.code.coding` | 736286003 | Hypertension clinical management plan | http://snomed.info/sct |
| 117 | 869 | Observation | `Observation.component.code.coding` | 135840009.0 | Blood pressure monitoring | http://snomed.info/sct |
| 118 | 872 | Observation | `Observation.component.code.coding` | SP000133 | Pemantauan Protein Urin | http://terminology.kemkes.go.id/sp |
| 119 | 884 | Observation | `Observation.code.coding` | SP000138 | Tatalaksana Komplikasi Pre Eklampsia | http://terminology.kemkes.go.id/sp |
| 120 | 887 | Observation | `Observation.component.code.coding` | 135840009.0 | Blood pressure monitoring | http://terminology.kemkes.go.id/sp |
| 121 | 890 | Observation | `Observation.component.code.coding` | SP000133 | Pemantauan Protein Urin | http://terminology.kemkes.go.id/sp |
| 122 | 893 | Observation | `Observation.component.code` | 308116003.0 | Antihypertensive therapy | http://snomed.info/sct |
| 123 | 896 | Observation | `Observation.component.code.coding` | SP000136 | Pemberian MgSO4 | http://terminology.kemkes.go.id/sp |
| 124 | 899 | Observation | `Observation.component.code.coding` | SP000137 | Pemberian Diazepam Injeksi | http://terminology.kemkes.go.id/sp |
| 125 | 912 | Observation | `Observation.code.coding` | SP000389 | Keadaan Ibu | http://terminology.kemkes.go.id/sp |
| 126 | 913 | Observation | `Observation.valueCodeableConcept.coding` | 438949009.0 | Alive | http://snomed.info/sct |
| 127 | 914 | Observation | `Observation.valueCodeableConcept.coding` | 419099009.0 | Dead | http://snomed.info/sct |
| 128 | 924 | Condition | `Condition.code.coding` | 359746009.0 | Patient’s condition stable | http://snomed.info/sct |
| 129 | 925 | Condition | `Condition.code.coding` | 162668006.0 | Patient’s condition unstable | http://snomed.info/sct |
| 130 | 926 | Condition | `Condition.code.coding` | 268910001.0 | Patient’s condition improved | http://snomed.info/sct |
| 131 | 935 | ServiceRequest | `ServiceRequest.code.coding` | 409014006.0 | Delivery care management | http://snomed.info/sct |
| 132 | 943 | ServiceRequest | `ServiceRequest.locationCode.coding` | SP000129 | Puskesmas PONED | http://terminology.kemkes.go.id/sp |
| 133 | 947 | ServiceRequest | `ServiceRequest.locationCode.coding` | SP000128 | Rumah Sakit Ibu dan Anak | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 67 |
| http://terminology.kemkes.go.id/sp | 23 |
| http://loinc.org | 18 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 13 |
| http://sys-ids.kemkes.go.id/kf | 4 |
| http://hl7.org/fhir/sid/icd-10 | 3 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 3 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 1 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 1 |
| **Total** | **133** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 32 | – | Faskes yang Melayani PNC | Organization | `Organization.name` |
| 909 | – | Keadaan Ibu | – | `` |
