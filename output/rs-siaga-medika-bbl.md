# Output Form: SIM RS Siaga Medika BBL

Sumber: `mapping/phdt-data-dictionary-rs-siaga-medika-bbl.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-rs-siaga-medika-bbl.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 37 |
| Code (`jumlah code` = 1) | 48 |
| Code unik (code + CodeSystem) | 34 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 2 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–11 | RelatedPerson | – | – | _Nama Ibu_ → `RelatedPerson.name.text` (2, tanpa BQ)<br>_NIK Ibu_ → `RelatedPerson.identifier` (3, tanpa BQ)<br>_No HP Ibu_ → `RelatedPerson.telecom` (9, tanpa BQ) |
| 2 | 12–18 | RelatedPerson | – | – | _Nama Ayah_ → `RelatedPerson.name.text` (12, tanpa BQ)<br>_NIK Ayah_ → `RelatedPerson.identifier` (13, tanpa BQ) |
| 3 | 19–45 | Patient | – | – | _Nama Bayi_ → `Patient.name.text` (19, tanpa BQ)<br>_NIK Bayi_ → `Patient.identifier.value` (23, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (24, tanpa BQ)<br>_Alamat Domisili_ → `Patient.address.line` (26, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (31, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (34, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.extension.valueCode` (37, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.extension.valueCode` (40, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (41, tanpa BQ)<br>_Tempat Lahir_ → `Patient.extension.valueAddress.city` (43, tanpa BQ)<br>_Kembar_ → `Patient.multipleBirthBoolean` (44, tanpa BQ) |
| 4 | 46–61 | Encounter | – | – | _Kunjungan Neonatus_ → `Encounter.identifier` (46, tanpa BQ)<br>_Tanggal Kunjungan_ → `Encounter.period.start` (56, tanpa BQ) |
| 5 | 62–69 | Condition | Z00.1 | Routine child health examination | – |
| 6 | 80–88 | EpisodeOfCare | Neonate | Neonate | – |
| 7 | 89–99 | Observation | 365475008.0 | Place in family order | _Anak ke_ → `Observation.valueInteger` (92, tanpa BQ) |
| 8 | 100–110 | Observation | 57715-5 | Birth time | _Jam Lahir_ → `Observation.valueTime` (103, tanpa BQ) |
| 9 | 111–152 | Observation | 76516-4 | Gestational age—​at birth | _Usia Gestasi Saat Lahir_ → `Observation.valueQuantity.value` (114, tanpa BQ)<br>_Golongan darah_ → `Observation` (126, tanpa BQ)<br>_Rhesus_ → `Observation` (140, tanpa BQ) |
| 10 | 153–164 | Observation | 8339-4 | Birth weight Measured | _Berat Badan Saat Lahir_ → `Observation.valueQuantity.value` (156, tanpa BQ) |
| 11 | 165–176 | Observation | 89269-5 | Body height Measured --at birth | _Panjang Badan Saat Lahir_ → `Observation.valueQuantity.value` (168, tanpa BQ) |
| 12 | 177–188 | Observation | 8290-9 | Head Occipital-frontal circumference --at birth- by Tape measure | _Lingkar Kepala Saat Lahir_ → `Observation.valueQuantity.value` (180, tanpa BQ) |
| 13 | 189–201 | Observation | 8867-4 | Heart rate | _Frekuensi Nadi_ → `Observation.valueQuantity.value` (192, tanpa BQ) |
| 14 | 202–214 | Observation | 8310-5 | Body temperature | _Suhu Badan_ → `Observation.valueQuantity.value` (205, tanpa BQ) |
| 15 | 215–227 | Observation | 9279-1 | Respiratory rate | _Respiratory Rate_ → `Observation.valueQuantity.value` (218, tanpa BQ) |
| 16 | 228–239 | Observation | 20564-1 | Oxygen saturation in Blood | _Saturasi Oksigen_ → `Observation.valueQuantity.value` (231, tanpa BQ) |
| 17 | 240–250 | Observation | 276654001.0 | Congenital malformation | _Kelainan Bawaan_ → `Observation.valueString` (243, tanpa BQ) |
| 18 | 251–262 | Observation | 1145307003.0 | Exclusively breastfed | _Apakah Diberikan ASI Eksklusi_ → `Observation.valueBoolean` (254, tanpa BQ) |
| 19 | 263–274 | Observation | 29463-7 | Body weight | _Berat Badan_ → `Observation.valueQuantity.value` (266, tanpa BQ) |
| 20 | 275–286 | Observation | 8306-3 | Body height --lying | _Tinggi Badan_ → `Observation.valueQuantity.value` (278, tanpa BQ) |
| 21 | 287–297 | Procedure | 400984005.0 | Congenital hypothyroidism screening test | _Apakah dilakukan SHK?_ → `Procedure.category.coding` (287, tanpa BQ) |
| 22 | 298–308 | Procedure | SP000296 | Skrining Penyakit Jantung Bawaan | _Skrining PJB_ → `Procedure.category.coding` (298, tanpa BQ) |
| 23 | 309–319 | Procedure | 408989004.0 | Newborn care management | _Tatalaksana Bayi Neonatus_ → `Procedure.category.coding` (309, tanpa BQ) |
| 24 | 320–337 | Immunization | – | – | _Alasan Tidak Diberikan Vaksin HB0_ → `Immunization.status` (335, tanpa BQ) |
| 25 | 338–349 | QuestionnaireResponse | – | – | _Kelas Ibu Balita_ → `QuestionnaireResponse.questionnaire` (338, tanpa BQ) |
| 26 | 351–363 | ServiceRequest | 409014006.0 | Delivery care management | _Faskes Tujuan Rujukan_ → `ServiceRequest.performer.display` (362, tanpa BQ)<br>_Nama Faskes Rujukan_ → `ServiceRequest.locationCode.text` (363, tanpa BQ) |
| 27 | 364–376 | Observation | 10206-1 | Physical findings of Skin Narrative | _Pemeriksaan Kulit_ → `Observation.valueString` (367, tanpa BQ)<br>_Interpretasi Hasil Pemeriksaan Kulit_ → `Observation.interpretation.coding` (368, tanpa BQ) |
| 28 | 377–389 | Observation | 10199-8 | Physical findings of Head Narrative | _Pemeriksaan Kepala_ → `Observation.valueString` (380, tanpa BQ)<br>_Interpretasi Hasil Pemeriksaan Kepala_ → `Observation.interpretation.coding` (381, tanpa BQ) |
| 29 | 390–402 | Observation | 10197-2 | Physical findings of Eye Narrative | _Pemeriksaan Mata_ → `Observation.valueString` (393, tanpa BQ)<br>_Interpretasi Hasil Pemeriksaan Mata_ → `Observation.interpretation.coding` (394, tanpa BQ) |
| 30 | 403–415 | Observation | 32453-3 | Physical findings of Mouth | _Pemeriksaan Mulut_ → `Observation.valueString` (406, tanpa BQ)<br>_Interpretasi Hasil Pemeriksaan Mulut_ → `Observation.interpretation.coding` (407, tanpa BQ) |
| 31 | 416–428 | Observation | 10191-5 | Physical findings of Abdomen Narrative | _Pemeriksaan Perut_ → `Observation.valueString` (419, tanpa BQ)<br>_Interpretasi Hasil Pemeriksaan Perut_ → `Observation.interpretation.coding` (420, tanpa BQ) |
| 32 | 429–441 | Observation | 10192-3 | Physical findings of Back Narrative | _Pemeriksaan Punggung_ → `Observation.valueString` (432, tanpa BQ)<br>_Interpretasi Hasil Pemeriksaan Punggung_ → `Observation.interpretation.coding` (433, tanpa BQ) |
| 33 | 442–454 | Observation | 11388-6 | Physical findings of Buttocks Narrative | _Pemeriksaan Lubang Anus_ → `Observation.valueString` (445, tanpa BQ)<br>_Interpretasi Hasil Pemeriksaan Lubang Anus_ → `Observation.interpretation.coding` (446, tanpa BQ) |
| 34 | 455–467 | Observation | 11400-9 | Physical findings of Genitalia Narrative | _Pemeriksaan Alat Kelamin_ → `Observation.valueString` (458, tanpa BQ)<br>_Interpretasi Hasil Pemeriksaan Alat Kelamin_ → `Observation.interpretation.coding` (459, tanpa BQ) |
| 35 | 468–483 | AllergyIntolerance | – | – | _Apakah ada alergi obat saat ini?_ → `AllergyIntolerance.clinicalStatus.coding` (468, tanpa BQ)<br>_Jika Ya, jenis obat?_ → `AllergyIntolerance.code.coding` (470, tanpa BQ) |
| 36 | 484–494 | Procedure | 431868002.0 | Initiation of breastfeeding | _Inisiasi Menyusu Dini (IMD)_ → `Procedure.category.coding` (484, tanpa BQ) |
| 37 | 495–509 | Immunization | 787859002.0 | Vaccine product | _Tanggal Pemberian Vaksin_ → `Immunization.occurrenceDateTime` (495, tanpa BQ)<br>_Nomor Lot Vaksin_ → `Immunization.lotNumber` (500, tanpa BQ)<br>_Tanggal Kadaluarsa Vaksin_ → `Immunization.expirationDate` (501, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 22 |
| Procedure | 4 |
| RelatedPerson | 2 |
| Immunization | 2 |
| Patient | 1 |
| Encounter | 1 |
| Condition | 1 |
| EpisodeOfCare | 1 |
| QuestionnaireResponse | 1 |
| ServiceRequest | 1 |
| AllergyIntolerance | 1 |
| **Total** | **37** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 64 | Condition | `Condition.code.coding` | Z00.1 | Routine child health examination | http://hl7.org/fhir/sid/icd-10 |
| 2 | 81 | EpisodeOfCare | `EpisodeOfCare.type.coding` | Neonate | Neonate | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 3 | 91 | Observation | `Observation.code.coding` | 365475008.0 | Place in family order | http://snomed.info/sct |
| 4 | 102 | Observation | `Observation.code.coding` | 57715-5 | Birth time | http://loinc.org |
| 5 | 113 | Observation | `Observation.code.coding` | 76516-4 | Gestational age—​at birth | http://loinc.org |
| 6 | 116 | Observation | `Observation.component.code.coding` | SP000398 | Usia Kehamilan Saat Persalinan (hari) | http://terminology.kemkes.go.id/sp |
| 7 | 155 | Observation | `Observation.code.coding` | 8339-4 | Birth weight Measured | http://loinc.org |
| 8 | 167 | Observation | `Observation.code.coding` | 89269-5 | Body height Measured --at birth | http://loinc.org |
| 9 | 179 | Observation | `Observation.code.coding` | 8290-9 | Head Occipital-frontal circumference --at birth- by Tape measure | http://loinc.org |
| 10 | 191 | Observation | `Observation.code.coding` | 8867-4 | Heart rate | http://loinc.org |
| 11 | 204 | Observation | `Observation.code.coding` | 8310-5 | Body temperature | http://loinc.org |
| 12 | 217 | Observation | `Observation.code.coding` | 9279-1 | Respiratory rate | http://loinc.org |
| 13 | 230 | Observation | `Observation.code.coding` | 20564-1 | Oxygen saturation in Blood | http://loinc.org |
| 14 | 242 | Observation | `Observation.code.coding` | 276654001.0 | Congenital malformation | http://snomed.info/sct |
| 15 | 253 | Observation | `Observation.code.coding` | 1145307003.0 | Exclusively breastfed | http://snomed.info/sct |
| 16 | 265 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 17 | 277 | Observation | `Observation.code.coding` | 8306-3 | Body height --lying | http://loinc.org |
| 18 | 288 | Procedure | `Procedure.code.coding` | 400984005.0 | Congenital hypothyroidism screening test | http://snomed.info/sct |
| 19 | 301 | Procedure | `Procedure.code.coding` | SP000296 | Skrining Penyakit Jantung Bawaan | http://terminology.kemkes.go.id/sp |
| 20 | 310 | Procedure | `Procedure.code.coding` | 408989004.0 | Newborn care management | http://snomed.info/sct |
| 21 | 322 | Immunization | `Immunization.vaccineCode` | VG45 | HepB | http://sys-ids.kemkes.go.id/kfa |
| 22 | 355 | ServiceRequest | `ServiceRequest.code.coding` | 409014006.0 | Delivery care management | http://snomed.info/sct |
| 23 | 366 | Observation | `Observation.code.coding` | 10206-1 | Physical findings of Skin Narrative | http://loinc.org |
| 24 | 368 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 25 | 369 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 26 | 379 | Observation | `Observation.code.coding` | 10199-8 | Physical findings of Head Narrative | http://loinc.org |
| 27 | 381 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 28 | 382 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 29 | 392 | Observation | `Observation.code.coding` | 10197-2 | Physical findings of Eye Narrative | http://loinc.org |
| 30 | 394 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 31 | 395 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 32 | 405 | Observation | `Observation.code.coding` | 32453-3 | Physical findings of Mouth | http://loinc.org |
| 33 | 407 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 34 | 408 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 35 | 418 | Observation | `Observation.code.coding` | 10191-5 | Physical findings of Abdomen Narrative | http://loinc.org |
| 36 | 420 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 37 | 421 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 38 | 431 | Observation | `Observation.code.coding` | 10192-3 | Physical findings of Back Narrative | http://loinc.org |
| 39 | 433 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 40 | 434 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 41 | 444 | Observation | `Observation.code.coding` | 11388-6 | Physical findings of Buttocks Narrative | http://loinc.org |
| 42 | 446 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 43 | 447 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 44 | 457 | Observation | `Observation.code.coding` | 11400-9 | Physical findings of Genitalia Narrative | http://loinc.org |
| 45 | 459 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 46 | 460 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 47 | 487 | Procedure | `Procedure.code.coding` | 431868002.0 | Initiation of breastfeeding | http://snomed.info/sct |
| 48 | 497 | Immunization | `Immunization.vaccineCode.coding` | 787859002.0 | Vaccine product | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://loinc.org | 19 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 16 |
| http://snomed.info/sct | 8 |
| http://terminology.kemkes.go.id/sp | 2 |
| http://hl7.org/fhir/sid/icd-10 | 1 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 1 |
| http://sys-ids.kemkes.go.id/kfa | 1 |
| **Total** | **48** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 350 | – | Rujuk | – | `` |
