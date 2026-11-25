# Output Form: SIM RS Nirmala PNC

Sumber: `mapping/phdt-data-dictionary-rs-nirmala-pnc.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-rs-nirmala-pnc.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 67 |
| Code (`jumlah code` = 1) | 147 |
| Code unik (code + CodeSystem) | 141 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 22 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–27 | Patient | – | – | _Nama Ibu_ → `Patient.name.text` (2, tanpa BQ)<br>_NIK_ → `Patient.identifier.value` (6, tanpa BQ)<br>_No HP_ → `Patient.telecom` (7, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (10, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (11, tanpa BQ)<br>_Alamat Domisili_ → `Patient.address.line` (13, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (18, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (21, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.extension.valueCode` (24, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.extension.valueCode` (27, tanpa BQ) |
| 2 | 66–72 | Practitioner | – | – | _NIK_ → `Practitioner.identifier.value` (68, tanpa BQ)<br>_Nama Tenaga Kesehatan_ → `Practitioner.name.text` (70, tanpa BQ)<br>_Jenis Kelamin Tenaga Kesehatan_ → `Practitioner.gender` (71, tanpa BQ) |
| 3 | 73–80 | PractitionerRole | – | – | _Tenaga Pemeriksa_ → `PractitionerRole.code.coding` (77, tanpa BQ) |
| 4 | 82–101 | Encounter | – | – | _Tanggal Kunjungan PNC_ → `Encounter.period.start` (89, tanpa BQ)<br>_Tempat Pelayanan PNC_ → `Encounter.location.location.display` (92, tanpa BQ)<br>_Cara Masuk_ → `Encounter.hospitalization.admitSource.coding` (93, tanpa BQ) |
| 5 | 102–110 | Condition | Z39.2 | Routine postpartum follow-up | _Kode ICD - Diagnosa_ → `Condition.clinicalStatus.coding` (102, tanpa BQ) |
| 6 | 113–133 | Condition | 404684003.0 | Clinical finding | _Keluhan_ → `Condition.clinicalStatus.coding` (113, tanpa BQ) |
| 7 | 144–152 | EpisodeOfCare | PNC | Postnatal Care | – |
| 8 | 153–164 | Observation | 93857-1 | Date and time of obstetric delivery | _Tanggal Persalinan_ → `Observation.valueDateTime` (156, tanpa BQ) |
| 9 | 165–176 | Observation | 11996-6 | [#] Pregnancies | _Gravida_ → `Observation.valueInteger` (169, tanpa BQ) |
| 10 | 177–188 | Observation | 11977-6 | [#] Parity | _Partus_ → `Observation.valueInteger` (181, tanpa BQ) |
| 11 | 189–200 | Observation | 69043-8 | Other pregnancy outcomes # | _Abortus_ → `Observation.valueInteger` (193, tanpa BQ) |
| 12 | 201–212 | Observation | 8480-6 | Systolic blood pressure | _Tekanan Darah Sistolik_ → `Observation.valueQuantity.value` (204, tanpa BQ) |
| 13 | 213–224 | Observation | 8462-4 | Diastolic blood pressure | _Tekanan Darah Diastolik_ → `Observation.valueQuantity.value` (216, tanpa BQ) |
| 14 | 225–237 | Observation | 8867-4 | Heart rate | _Nadi_ → `Observation.valueQuantity.value` (228, tanpa BQ) |
| 15 | 238–250 | Observation | – | – | _Suhu_ → `Observation.valueQuantity.value` (241, tanpa BQ) |
| 16 | 251–263 | Observation | 9279-1 | Respiratory rate | _Pernapasan_ → `Observation.valueQuantity.value` (254, tanpa BQ) |
| 17 | 264–274 | Observation | SP000683 | Tatalaksana Tindakan | _Tatalaksana (Tindakan)_ → `Observation.valueString` (267, tanpa BQ) |
| 18 | 275–285 | Observation | SP000684 | Tatalaksana Obat | _Tatalaksana Obat_ → `Observation.valueString` (278, tanpa BQ) |
| 19 | 286–294 | Condition | 199745000.0 | Complication occurring during labor and delivery | _Komplikasi_ → `Condition.clinicalStatus.coding` (286, tanpa BQ) |
| 20 | 296–302 | Condition | 289530006.0 | Vaginal bleeding | _Pendarahan Pervaginam_ → `Condition.clinicalStatus.coding` (296, tanpa BQ) |
| 21 | 303–314 | Observation | 81661-1 | Blood Loss [Volume] Measured | _Jumlah Pendarahan_ → `Observation.valueQuantity.value` (306, tanpa BQ) |
| 22 | 315–325 | Observation | 364297003.0 | Female perineum observable | _Kondisi Perineum_ → `Observation.valueString` (318, tanpa BQ) |
| 23 | 326–337 | Observation | OC000020 | Tanda Infeksi Perineum | _Tanda Infeksi Perineum_ → `Observation.valueBoolean` (329, tanpa BQ) |
| 24 | 338–349 | Observation | OC000025 | Tanda Infeksi Luka Jahitan Sectio Caesaria | _Tanda Infeksi Luka Jahitan Sectio Caesaria_ → `Observation.valueBoolean` (341, tanpa BQ) |
| 25 | 350–364 | Observation | 32422-8 | Physical findings of breast | _Kondisi Payudara_ → `Observation.valueCodeableConcept.coding` (353, tanpa BQ) |
| 26 | 365–376 | Observation | 289700000.0 | Uterine contractions present | _Kontraksi Uteri_ → `Observation.valueBoolean` (368, tanpa BQ) |
| 27 | 377–390 | Observation | 249214003.0 | Color of lochia | _Warna Lokhia_ → `Observation.valueCodeableConcept.coding` (380, tanpa BQ) |
| 28 | 391–402 | Observation | 249215002.0 | Odor of lochia | _Bau Lokhia_ → `Observation.valueBoolean` (394, tanpa BQ) |
| 29 | 403–415 | Observation | OC000017 | Produksi ASI | _Produksi ASI_ → `Observation.valueCodeableConcept.coding` (406, tanpa BQ) |
| 30 | 416–427 | Observation | 1145307003.0 | Exclusively breastfed | _ASI Eksklusif_ → `Observation.valueBoolean` (419, tanpa BQ) |
| 31 | 428–445 | Observation | 252041008.0 | Micturition finding | _Gangguan Buang Air Kecil_ → `Observation.valueBoolean` (431, tanpa BQ) |
| 32 | 446–457 | Observation | 300375001.0 | Able to defecate | _Gangguan Buang Air Besar_ → `Observation.valueBoolean` (449, tanpa BQ) |
| 33 | 458–468 | Procedure | 408988007.0 | Newborn care education | _Konseling Perawatan Bayi Baru Lahir_ → `Procedure.category.coding` (458, tanpa BQ) |
| 34 | 469–480 | Observation | 8345-1 | Body weight Measured --post partum | _Berat Badan_ → `Observation.valueQuantity.value` (472, tanpa BQ) |
| 35 | 481–492 | Observation | 8305-5 | Body height --post partum | _Tinggi Badan_ → `Observation.valueQuantity.value` (484, tanpa BQ) |
| 36 | 493–508 | Observation | 284473002.0 | Mid upper arm circumference | _LILA_ → `Observation.valueQuantity.value` (496, tanpa BQ)<br>_Status Gizi KEK/Tidak KEK_ → `Observation.interpretation` (505, tanpa BQ) |
| 37 | 509–521 | Observation | 11881-0 | Uterus Fundal height Tape measure | _TFU_ → `Observation.valueString` (512, tanpa BQ) |
| 38 | 522–539 | Condition | 47821001.0 | Postpartum hemorrhage | _Komplikasi Masa Nifas_ → `Condition.clinicalStatus.coding` (522, tanpa BQ) |
| 39 | 540–553 | Observation | 289084000.0 | Difficulty performing breastfeeding | _Apakah ada masalah memberikan ASI_ → `Observation.valueBoolean` (543, tanpa BQ)<br>_Catatan ASI_ → `Observation.note.text` (552, tanpa BQ)<br>_Catat dibuku KIA_ → `Observation.category.coding` (553, tanpa BQ) |
| 40 | 554–564 | Observation | SP000122 | Catat di Buku KIA | – |
| 41 | 565–566 | MedicationDispense | – | – | _Diberikan Tablet FE_ → `MedicationDispense.status` (565, tanpa BQ) |
| 42 | 567–581 | Medication | – | – | – |
| 43 | 582–587 | MedicationRequest | – | – | – |
| 44 | 588–602 | Medication | – | – | – |
| 45 | 603–608 | MedicationDispense | – | – | – |
| 46 | 609–642 | MedicationRequest | 92000653.0 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula | _Jumlah Tablet Fe yang didapatkan (butir)_ → `MedicationRequest.contained.resourceType` (609, tanpa BQ) |
| 47 | 643–674 | MedicationDispense | 93015491.0 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | – |
| 48 | 675–684 | Procedure | 767224000.0 | Administration of vitamin A | _Pemberian Vitamin A_ → `Procedure.category.coding` (675, tanpa BQ) |
| 49 | 685–695 | Procedure | 711029005.0 | Counseling about breastfeeding | _Konseling ASI_ → `Procedure.category.coding` (685, tanpa BQ) |
| 50 | 696–706 | Procedure | ED000008 | Edukasi Tanda Bahaya Kehamilan, Bersalin dan Nifas | _Tanda Bahaya Nifas_ → `Procedure.category.coding` (696, tanpa BQ) |
| 51 | 707–717 | Procedure | 72531000052105.0 | Counseling for contraception | _Konseling KB_ → `Procedure.category.coding` (707, tanpa BQ) |
| 52 | 718–728 | Procedure | SP000135 | Konseling Tanda Bahaya Bayi Baru Lahir | _Konseling Tanda Bahaya Bayi Baru Lahir_ → `Procedure.category.coding` (718, tanpa BQ) |
| 53 | 729–739 | Procedure | 441041000124100.0 | Counseling about nutrition | _Konseling Gizi_ → `Procedure.category.coding` (729, tanpa BQ) |
| 54 | 740–750 | Procedure | PC000001 | Perawatan Tali Pusat | _Konseling Perawatan Tali Pusar_ → `Procedure.category.coding` (740, tanpa BQ) |
| 55 | 751–761 | Procedure | ED000010 | Edukasi PHBS | _Konseling PHBS_ → `Procedure.category.coding` (751, tanpa BQ) |
| 56 | 762–772 | Procedure | ED000012 | Edukasi lainnya | _Konseling Jiwa Pascasalin_ → `Procedure.category.coding` (762, tanpa BQ) |
| 57 | 773–784 | Observation | SP000046 | Terapi Antiretroviral (ART) | _ART_ → `Observation.valueBoolean` (776, tanpa BQ) |
| 58 | 785–796 | Observation | 395264002.0 | Product containing tenofovir | _Obat Hepatitis (Tenofovir)_ → `Observation.valueBoolean` (788, tanpa BQ) |
| 59 | 797–817 | Observation | SP000124 | Obat anti malaria | _Obat Anti Malaria_ → `Observation.valueBoolean` (800, tanpa BQ) |
| 60 | 818–841 | Observation | SP000125 | Obat anti tuberkulosis | _Obat Anti Tuberkulosis (OAT)_ → `Observation.valueBoolean` (821, tanpa BQ) |
| 61 | 842–859 | Observation | PC000004 | KB Pasca Persalinan | _Metode Kontrasepsi KB Pasca Persalinan_ → `Observation.valueCodeableConcept.coding` (845, tanpa BQ) |
| 62 | 860–877 | Observation | SP000380 | Tatalaksana Komplikasi Pendarahan | _Tatalaksana Komplikasi Pendarahan_ → `Observation.valueBoolean` (863, tanpa BQ)<br>_Pemberian Tablet FE_ → `Observation.component.code.coding` (865, tanpa BQ)<br>_Transfusi Darah_ → `Observation.component.code.coding` (868, tanpa BQ) |
| 63 | 878–895 | Observation | 736286003 | Hypertension clinical management plan | _Tatalaksana Komplikasi Hipertensi_ → `Observation.valueBoolean` (881, tanpa BQ)<br>_Pantau Tekanan Darah_ → `Observation.component.code.coding` (883, tanpa BQ)<br>_Pantau Protein Urin_ → `Observation.component.code.coding` (886, tanpa BQ) |
| 64 | 896–922 | Observation | SP000138 | Tatalaksana Komplikasi Pre Eklampsia | _Tatalaksana Komplikasi Pre Eklampsia dan Eklampsia_ → `Observation.valueBoolean` (899, tanpa BQ)<br>_Pantau Tekanan Darah_ → `Observation.component.code.coding` (901, tanpa BQ)<br>_Pantau Protein Urin_ → `Observation.component.code.coding` (904, tanpa BQ)<br>_Pemberian Anti Hipertensi_ → `Observation.component.code` (907, tanpa BQ)<br>_Pemberian MgSO4_ → `Observation.component.code.coding` (910, tanpa BQ)<br>_Pemberian Diazepam Injeksi_ → `Observation.component.code.coding` (913, tanpa BQ) |
| 65 | 924–935 | Observation | SP000389 | Keadaan Ibu | – |
| 66 | 936–944 | Condition | 359746009.0 | Patient’s condition stable | _Keadaan Pulang_ → `Condition.clinicalStatus.coding` (936, tanpa BQ) |
| 67 | 945–965 | ServiceRequest | 409014006.0 | Delivery care management | _Tanggal Dirujuk_ → `ServiceRequest.occurrenceDateTime` (953, tanpa BQ)<br>_Faskes Rujukan_ → `ServiceRequest.locationCode.coding` (957, tanpa BQ)<br>_Nama Faskes Rujukan_ → `ServiceRequest.locationCode.text` (964, tanpa BQ)<br>_Tindak Lanjut_ → `ServiceRequest.patientInstruction` (965, tanpa BQ) |

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
| 14 | 117 | Condition | `Condition.code.coding` | 80313002.0 | Palpitations | http://snomed.info/sct |
| 15 | 118 | Condition | `Condition.code.coding` | 271939006.0 | Vaginal discharge | http://snomed.info/sct |
| 16 | 119 | Condition | `Condition.code.coding` | 267036007.0 | Dyspnea | http://snomed.info/sct |
| 17 | 120 | Condition | `Condition.code.coding` | 248858001.0 | Vulva finding | http://snomed.info/sct |
| 18 | 121 | Condition | `Condition.code.coding` | 274671002.0 | Pelvic and perineal pain | http://snomed.info/sct |
| 19 | 122 | Condition | `Condition.code.coding` | 47821001.0 | Postpartum hemorrhage | http://snomed.info/sct |
| 20 | 123 | Condition | `Condition.code.coding` | 289552002.0 | White vaginal discharge | http://snomed.info/sct |
| 21 | 124 | Condition | `Condition.code.coding` | 58703003.0 | Postpartum depression | http://snomed.info/sct |
| 22 | 125 | Condition | `Condition.code.coding` | 386661006.0 | Fever | http://snomed.info/sct |
| 23 | 126 | Condition | `Condition.code.coding` | 25064002.0 | Headache | http://snomed.info/sct |
| 24 | 127 | Condition | `Condition.code.coding` | 111516008.0 | Blurring of visual image | http://snomed.info/sct |
| 25 | 128 | Condition | `Condition.code.coding` | 79922009.0 | Epigastric pain | http://snomed.info/sct |
| 26 | 145 | EpisodeOfCare | `EpisodeOfCare.type.coding` | PNC | Postnatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 27 | 155 | Observation | `Observation.code.coding` | 93857-1 | Date and time of obstetric delivery | http://loinc.org |
| 28 | 167 | Observation | `Observation.code.coding` | 11996-6 | [#] Pregnancies | http://loinc.org |
| 29 | 168 | Observation | `Observation.code.coding` | ANC.B6.DE24 | Number of pregnancies (gravida) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 30 | 179 | Observation | `Observation.code.coding` | 11977-6 | [#] Parity | http://loinc.org |
| 31 | 180 | Observation | `Observation.code.coding` | ANC.B6.DE32 | Parity | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 32 | 191 | Observation | `Observation.code.coding` | 69043-8 | Other pregnancy outcomes # | http://loinc.org |
| 33 | 192 | Observation | `Observation.code.coding` | ANC.B6.DE25 | Number of miscarriages and/or abortions | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 34 | 203 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 35 | 215 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://loinc.org |
| 36 | 227 | Observation | `Observation.code.coding` | 8867-4 | Heart rate | http://loinc.org |
| 37 | 253 | Observation | `Observation.code.coding` | 9279-1 | Respiratory rate | http://loinc.org |
| 38 | 266 | Observation | `Observation.code.coding` | SP000683 | Tatalaksana Tindakan | http://terminology.kemkes.go.id/sp |
| 39 | 277 | Observation | `Observation.code.coding` | SP000684 | Tatalaksana Obat | http://terminology.kemkes.go.id/sp |
| 40 | 288 | Condition | `Condition.code.coding` | 199745000.0 | Complication occurring during labor and delivery | http://snomed.info/sct |
| 41 | 298 | Condition | `Condition.code.coding` | 289530006.0 | Vaginal bleeding | http://snomed.info/sct |
| 42 | 305 | Observation | `Observation.code.coding` | 81661-1 | Blood Loss [Volume] Measured | http://loinc.org |
| 43 | 317 | Observation | `Observation.code.coding` | 364297003.0 | Female perineum observable | http://loinc.org |
| 44 | 328 | Observation | `Observation.code.coding` | OC000020 | Tanda Infeksi Perineum | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 45 | 340 | Observation | `Observation.code.coding` | OC000025 | Tanda Infeksi Luka Jahitan Sectio Caesaria | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 46 | 352 | Observation | `Observation.code.coding` | 32422-8 | Physical findings of breast | http://loinc.org |
| 47 | 353 | Observation | `Observation.valueCodeableConcept.coding` | 300885006.0 | Swelling of breast | http://snomed.info/sct |
| 48 | 354 | Observation | `Observation.valueCodeableConcept.coding` | 290070001.0 | Red breast | http://snomed.info/sct |
| 49 | 355 | Observation | `Observation.valueCodeableConcept.coding` | 54302000.0 | Discharge from nipple | http://snomed.info/sct |
| 50 | 356 | Observation | `Observation.valueCodeableConcept.coding` | 53430007.0 | Pain of breast | http://snomed.info/sct |
| 51 | 357 | Observation | `Observation.valueCodeableConcept.coding` | 290084006.0 | Breast normal | http://snomed.info/sct |
| 52 | 367 | Observation | `Observation.code.coding` | 289700000.0 | Uterine contractions present | http://snomed.info/sct |
| 53 | 379 | Observation | `Observation.code.coding` | 249214003.0 | Color of lochia | http://snomed.info/sct |
| 54 | 380 | Observation | `Observation.valueCodeableConcept.coding` | 278072004.0 | Lochia rubra | http://snomed.info/sct |
| 55 | 381 | Observation | `Observation.valueCodeableConcept.coding` | 449828001.0 | Lochia serosa | http://snomed.info/sct |
| 56 | 382 | Observation | `Observation.valueCodeableConcept.coding` | 113291006.0 | Lochia sanguinolenta | http://snomed.info/sct |
| 57 | 383 | Observation | `Observation.valueCodeableConcept.coding` | 449827006.0 | Lochia alba | http://snomed.info/sct |
| 58 | 393 | Observation | `Observation.code.coding` | 249215002.0 | Odor of lochia | http://snomed.info/sct |
| 59 | 405 | Observation | `Observation.code.coding` | OC000017 | Produksi ASI | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 60 | 406 | Observation | `Observation.valueCodeableConcept.coding` | OV000016 | Produksi ASI ada | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 61 | 407 | Observation | `Observation.valueCodeableConcept.coding` | OV000017 | Produksi ASI ada tapi sedikit | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 62 | 408 | Observation | `Observation.valueCodeableConcept.coding` | OV000018 | Produksi ASI tidak ada | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 63 | 418 | Observation | `Observation.code.coding` | 1145307003.0 | Exclusively breastfed | http://snomed.info/sct |
| 64 | 430 | Observation | `Observation.code.coding` | 252041008.0 | Micturition finding | http://snomed.info/sct |
| 65 | 433 | Observation | `Observation.valueCodeableConcept.coding` | 49650001.0 | Dysuria | http://snomed.info/sct |
| 66 | 434 | Observation | `Observation.valueCodeableConcept.coding` | 249288007.0 | Incomplete emptying of urinary bladder | http://snomed.info/sct |
| 67 | 435 | Observation | `Observation.valueCodeableConcept.coding` | 162116003.0 | Increased frequency of urination | http://snomed.info/sct |
| 68 | 436 | Observation | `Observation.valueCodeableConcept.coding` | 42112009.0 | Enuresis | http://snomed.info/sct |
| 69 | 437 | Observation | `Observation.valueCodeableConcept.coding` | 102834005.0 | Normal micturition | http://snomed.info/sct |
| 70 | 438 | Observation | `Observation.valueCodeableConcept.coding` | 267064002.0 | Retention of urine | http://snomed.info/sct |
| 71 | 448 | Observation | `Observation.code.coding` | 300375001.0 | Able to defecate | http://snomed.info/sct |
| 72 | 459 | Procedure | `Procedure.code.coding` | 408988007.0 | Newborn care education | http://snomed.info/sct |
| 73 | 471 | Observation | `Observation.code.coding` | 8345-1 | Body weight Measured --post partum | http://loinc.org |
| 74 | 483 | Observation | `Observation.code.coding` | 8305-5 | Body height --post partum | http://loinc.org |
| 75 | 495 | Observation | `Observation.code.coding` | 284473002.0 | Mid upper arm circumference | http://snomed.info/sct |
| 76 | 505 | Observation | `Observation.interpretation` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 77 | 506 | Observation | `Observation.interpretation` | OI000018 | Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 78 | 507 | Observation | `Observation.interpretation` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 79 | 508 | Observation | `Observation.interpretation` | OI000035 | Risiko Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 80 | 511 | Observation | `Observation.code.coding` | 11881-0 | Uterus Fundal height Tape measure | http://loinc.org |
| 81 | 524 | Condition | `Condition.code.coding` | 47821001.0 | Postpartum hemorrhage | http://snomed.info/sct |
| 82 | 525 | Condition | `Condition.code.coding` | 198188007.0 | Chronic uterine inflammatory disease | http://snomed.info/sct |
| 83 | 526 | Condition | `Condition.code.coding` | 111367007.0 | Pelvic abscess | http://snomed.info/sct |
| 84 | 527 | Condition | `Condition.code.coding` | 211063003.0 | Infected abrasion of perineum | http://snomed.info/sct |
| 85 | 528 | Condition | `Condition.code.coding` | 76902006.0 | Tetanus | http://snomed.info/sct |
| 86 | 529 | Condition | `Condition.code.coding` | 266579006.0 | Inflammatory disorder of breast | http://snomed.info/sct |
| 87 | 530 | Condition | `Condition.code.coding` | 49746001.0 | Engorgement of breasts | http://snomed.info/sct |
| 88 | 531 | Condition | `Condition.code.coding` | 82231009.0 | Inversion of nipple | http://snomed.info/sct |
| 89 | 532 | Condition | `Condition.code.coding` | 58703003.0 | Postpartum depression | http://snomed.info/sct |
| 90 | 533 | Condition | `Condition.code.coding` | O13 | Gestational [pregnancy-induced] hypertension without signification proteinuria | http://hl7.org/fhir/sid/icd-10 |
| 91 | 534 | Condition | `Condition.code.coding` | O90.8 | Other complications of the puerperium, not elsewhere classified | http://hl7.org/fhir/sid/icd-10 |
| 92 | 542 | Observation | `Observation.code.coding` | 289084000.0 | Difficulty performing breastfeeding | http://snomed.info/sct |
| 93 | 554 | Observation | `Observation.code.coding` | SP000122 | Catat di Buku KIA | http://terminology.kemkes.go.id/sp |
| 94 | 568 | Medication | `Medication.code` | 92000653.0 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula | http://sys-ids.kemkes.go.id/kf |
| 95 | 589 | Medication | `Medication.code` | 93015491.0 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | http://sys-ids.kemkes.go.id/kf |
| 96 | 612 | MedicationRequest | `MedicationRequest.contained.code.coding` | 92000653.0 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula | http://sys-ids.kemkes.go.id/kf |
| 97 | 646 | MedicationDispense | `MedicationDispense.contained.code.coding` | 93015491.0 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | http://sys-ids.kemkes.go.id/kf |
| 98 | 676 | Procedure | `Procedure.code.coding` | 767224000.0 | Administration of vitamin A | http://snomed.info/sct |
| 99 | 686 | Procedure | `Procedure.code.coding` | 711029005.0 | Counseling about breastfeeding | http://snomed.info/sct |
| 100 | 697 | Procedure | `Procedure.code.coding` | ED000008 | Edukasi Tanda Bahaya Kehamilan, Bersalin dan Nifas | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 101 | 708 | Procedure | `Procedure.code.coding` | 72531000052105.0 | Counseling for contraception | http://snomed.info/sct |
| 102 | 719 | Procedure | `Procedure.code.coding` | SP000135 | Konseling Tanda Bahaya Bayi Baru Lahir | http://terminology.kemkes.go.id/sp |
| 103 | 730 | Procedure | `Procedure.code.coding` | 441041000124100.0 | Counseling about nutrition | http://snomed.info/sct |
| 104 | 741 | Procedure | `Procedure.code.coding` | PC000001 | Perawatan Tali Pusat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 105 | 752 | Procedure | `Procedure.code.coding` | ED000010 | Edukasi PHBS | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 106 | 763 | Procedure | `Procedure.code.coding` | ED000012 | Edukasi lainnya | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 107 | 775 | Observation | `Observation.code.coding` | SP000046 | Terapi Antiretroviral (ART) | http://terminology.kemkes.go.id/sp |
| 108 | 787 | Observation | `Observation.code.coding` | 395264002.0 | Product containing tenofovir | http://snomed.info/sct |
| 109 | 799 | Observation | `Observation.code.coding` | SP000124 | Obat anti malaria | http://terminology.kemkes.go.id/sp |
| 110 | 802 | Observation | `Observation.component.code.coding` | 432555000.0 | Product containing artesunate | http://snomed.info/sct |
| 111 | 805 | Observation | `Observation.component.code.coding` | 64115004.0 | Product containing amodiaquine | http://snomed.info/sct |
| 112 | 808 | Observation | `Observation.component.code.coding` | 324919005.0 | Product containing precisely quinine sulfate 200 milligram/1 each conventional release oral tablet | http://snomed.info/sct |
| 113 | 820 | Observation | `Observation.code.coding` | SP000125 | Obat anti tuberkulosis | http://terminology.kemkes.go.id/sp |
| 114 | 823 | Observation | `Observation.component.code.coding` | 29175007.0 | Product containing rifampicin | http://snomed.info/sct |
| 115 | 826 | Observation | `Observation.component.code.coding` | 81335000.0 | Product containing isoniazid | http://snomed.info/sct |
| 116 | 829 | Observation | `Observation.component.code.coding` | 13592004.0 | Product containing pyrazinamide | http://snomed.info/sct |
| 117 | 832 | Observation | `Observation.component.code.coding` | 24450004.0 | Product containing ethambutol | http://snomed.info/sct |
| 118 | 844 | Observation | `Observation.code.coding` | PC000004 | KB Pasca Persalinan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 119 | 845 | Observation | `Observation.valueCodeableConcept.coding` | LA6524-8 | Oral contraceptive pill | http://loinc.org |
| 120 | 846 | Observation | `Observation.valueCodeableConcept.coding` | 237122005.0 | Lactational amenorrhea | http://snomed.info/sct |
| 121 | 847 | Observation | `Observation.valueCodeableConcept.coding` | LA6525-5 | Injectable/implantable hormone | http://loinc.org |
| 122 | 848 | Observation | `Observation.valueCodeableConcept.coding` | LA6527-1 | Intrauterine device | http://loinc.org |
| 123 | 849 | Observation | `Observation.valueCodeableConcept.coding` | SP000097 | Implan | http://terminology.kemkes.go.id/sp |
| 124 | 850 | Observation | `Observation.valueCodeableConcept.coding` | LA6523-0 | Condom | http://loinc.org |
| 125 | 851 | Observation | `Observation.valueCodeableConcept.coding` | 22523008.0 | Vasectomy | http://snomed.info/sct |
| 126 | 852 | Observation | `Observation.valueCodeableConcept.coding` | 77543007.0 | Ligation of fallopian tube | http://snomed.info/sct |
| 127 | 862 | Observation | `Observation.code.coding` | SP000380 | Tatalaksana Komplikasi Pendarahan | http://terminology.kemkes.go.id/sp |
| 128 | 865 | Observation | `Observation.component.code.coding` | SP000008 | Pemberian Tablet Tambah Darah | http://terminology.kemkes.go.id/sp |
| 129 | 868 | Observation | `Observation.component.code.coding` | 116859006.0 | Transfusion of blood product | http://snomed.info/sct |
| 130 | 880 | Observation | `Observation.code.coding` | 736286003 | Hypertension clinical management plan | http://snomed.info/sct |
| 131 | 883 | Observation | `Observation.component.code.coding` | 135840009.0 | Blood pressure monitoring | http://snomed.info/sct |
| 132 | 886 | Observation | `Observation.component.code.coding` | SP000133 | Pemantauan Protein Urin | http://terminology.kemkes.go.id/sp |
| 133 | 898 | Observation | `Observation.code.coding` | SP000138 | Tatalaksana Komplikasi Pre Eklampsia | http://terminology.kemkes.go.id/sp |
| 134 | 901 | Observation | `Observation.component.code.coding` | 135840009 | Blood pressure monitoring | http://snomed.info/sct |
| 135 | 904 | Observation | `Observation.component.code.coding` | SP000133 | Pemantauan Protein Urin | http://terminology.kemkes.go.id/sp |
| 136 | 907 | Observation | `Observation.component.code` | 308116003.0 | Antihypertensive therapy | http://snomed.info/sct |
| 137 | 910 | Observation | `Observation.component.code.coding` | SP000136 | Pemberian MgSO4 | http://terminology.kemkes.go.id/sp |
| 138 | 913 | Observation | `Observation.component.code.coding` | SP000137 | Pemberian Diazepam Injeksi | http://terminology.kemkes.go.id/sp |
| 139 | 926 | Observation | `Observation.code.coding` | SP000389 | Keadaan Ibu | http://terminology.kemkes.go.id/sp |
| 140 | 927 | Observation | `Observation.valueCodeableConcept.coding` | 438949009.0 | Alive | http://snomed.info/sct |
| 141 | 928 | Observation | `Observation.valueCodeableConcept.coding` | 419099009.0 | Dead | http://snomed.info/sct |
| 142 | 938 | Condition | `Condition.code.coding` | 359746009.0 | Patient’s condition stable | http://snomed.info/sct |
| 143 | 939 | Condition | `Condition.code.coding` | 162668006.0 | Patient’s condition unstable | http://snomed.info/sct |
| 144 | 940 | Condition | `Condition.code.coding` | 268910001.0 | Patient’s condition improved | http://snomed.info/sct |
| 145 | 949 | ServiceRequest | `ServiceRequest.code.coding` | 409014006.0 | Delivery care management | http://snomed.info/sct |
| 146 | 957 | ServiceRequest | `ServiceRequest.locationCode.coding` | SP000129 | Puskesmas PONED | http://terminology.kemkes.go.id/sp |
| 147 | 961 | ServiceRequest | `ServiceRequest.locationCode.coding` | SP000128 | Rumah Sakit Ibu dan Anak | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 80 |
| http://terminology.kemkes.go.id/sp | 22 |
| http://loinc.org | 18 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 14 |
| http://sys-ids.kemkes.go.id/kf | 4 |
| http://hl7.org/fhir/sid/icd-10 | 3 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 3 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 2 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 1 |
| **Total** | **147** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 32 | – | Faskes yang Melayani PNC | Organization | `Organization.name` |
| 923 | – | Keadaan Ibu | – | `` |
