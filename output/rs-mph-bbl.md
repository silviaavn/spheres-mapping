# Output Form: SIM RS MPH BBL

Sumber: `mapping/phdt-data-dictionary-rs-mph-bbl.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-rs-mph-bbl.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 42 |
| Code (`jumlah code` = 1) | 59 |
| Code unik (code + CodeSystem) | 44 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 2 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–6 | Practitioner | – | – | _NIK_ → `Practitioner.identifier.value` (4, tanpa BQ)<br>_Nama Tenaga Kesehatan_ → `Practitioner.name.text` (6, tanpa BQ) |
| 2 | 7–16 | PractitionerRole | – | – | _Tenaga Pemeriksa_ → `PractitionerRole.code.coding` (11, tanpa BQ) |
| 3 | 17–26 | RelatedPerson | – | – | _Nama Ibu_ → `RelatedPerson.name.text` (17, tanpa BQ)<br>_NIK Ibu_ → `RelatedPerson.identifier` (18, tanpa BQ)<br>_No HP Ibu_ → `RelatedPerson.telecom` (24, tanpa BQ) |
| 4 | 27–33 | RelatedPerson | – | – | _Nama Ayah_ → `RelatedPerson.name.text` (27, tanpa BQ)<br>_NIK Ayah_ → `RelatedPerson.identifier` (28, tanpa BQ) |
| 5 | 36–65 | Patient | – | – | _Nama Bayi_ → `Patient.name.text` (36, tanpa BQ)<br>_NIK Bayi_ → `Patient.identifier.value` (40, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (41, tanpa BQ)<br>_No HP Orang Tua_ → `Patient.telecom` (43, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (46, tanpa BQ)<br>_Tempat Lahir_ → `Patient.extension.valueAddress.city` (48, tanpa BQ)<br>_Kembar_ → `Patient.multipleBirthBoolean` (49, tanpa BQ)<br>_Alamat Domisili_ → `Patient.address.line` (51, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (56, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (59, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.extension.valueCode` (62, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.extension.valueCode` (65, tanpa BQ) |
| 6 | 66–82 | Encounter | – | – | _Kunjungan Neonatus_ → `Encounter.identifier` (67, tanpa BQ)<br>_Tanggal Kunjungan_ → `Encounter.period.start` (77, tanpa BQ) |
| 7 | 83–90 | Condition | Z00.1 | Routine child health examination | – |
| 8 | 101–109 | EpisodeOfCare | Neonate | Neonate | – |
| 9 | 110–120 | Observation | 72150-6 | Delivery location | _Lokasi Kelahiran_ → `Observation.valueCodeableConcept.coding` (113, tanpa BQ) |
| 10 | 121–131 | Observation | 365475008.0 | Place in family order | _Anak ke_ → `Observation.valueInteger` (124, tanpa BQ) |
| 11 | 132–142 | Observation | 57715-5 | Birth time | _Jam Lahir_ → `Observation.valueTime` (135, tanpa BQ) |
| 12 | 143–184 | Observation | 76516-4 | Gestational age—​at birth | _Usia Gestasi Saat Lahir_ → `Observation.valueQuantity.value` (146, tanpa BQ)<br>_Golongan darah_ → `Observation` (158, tanpa BQ)<br>_Rhesus_ → `Observation` (172, tanpa BQ) |
| 13 | 185–196 | Observation | 8339-4 | Birth weight Measured | _Berat Badan Saat Lahir_ → `Observation.valueQuantity.value` (188, tanpa BQ) |
| 14 | 197–208 | Observation | 89269-5 | Body height Measured --at birth | _Panjang Badan Saat Lahir_ → `Observation.valueQuantity.value` (200, tanpa BQ) |
| 15 | 209–220 | Observation | 8290-9 | Head Occipital-frontal circumference --at birth- by Tape measure | _Lingkar Kepala Saat Lahir_ → `Observation.valueQuantity.value` (212, tanpa BQ) |
| 16 | 221–233 | Observation | 8867-4 | Heart rate | _Frekuensi Nadi_ → `Observation.valueQuantity.value` (224, tanpa BQ) |
| 17 | 234–246 | Observation | 8310-5 | Body temperature | _Suhu Badan_ → `Observation.valueQuantity.value` (237, tanpa BQ) |
| 18 | 247–259 | Observation | 9279-1 | Respiratory rate | _Respiratory Rate_ → `Observation.valueQuantity.value` (250, tanpa BQ) |
| 19 | 260–271 | Observation | 20564-1 | Oxygen saturation in Blood | _Saturasi Oksigen_ → `Observation.valueQuantity.value` (263, tanpa BQ) |
| 20 | 272–282 | Observation | 276654001.0 | Congenital malformation | _Kelainan Bawaan_ → `Observation.valueString` (275, tanpa BQ) |
| 21 | 283–294 | Observation | 1145307003.0 | Exclusively breastfed | _Apakah Diberikan ASI Eksklusi_ → `Observation.valueBoolean` (286, tanpa BQ) |
| 22 | 295–306 | Observation | 29463-7 | Body weight | _Berat Badan_ → `Observation.valueQuantity.value` (298, tanpa BQ) |
| 23 | 307–318 | Observation | 8306-3 | Body height --lying | _Tinggi Badan_ → `Observation.valueQuantity.value` (310, tanpa BQ) |
| 24 | 319–329 | Procedure | 400984005.0 | Congenital hypothyroidism screening test | _Apakah dilakukan SHK?_ → `Procedure.category.coding` (319, tanpa BQ) |
| 25 | 330–341 | Observation | 29575-8 | Thyrotropin [Units/volume] in DBS | _Hasil SHK_ → `Observation.valueQuantity.value` (333, tanpa BQ) |
| 26 | 342–352 | Procedure | SP000296 | Skrining Penyakit Jantung Bawaan | _Skrining PJB_ → `Procedure.category.coding` (342, tanpa BQ) |
| 27 | 353–363 | Procedure | 408989004.0 | Newborn care management | _Tatalaksana Bayi Neonatus_ → `Procedure.category.coding` (353, tanpa BQ) |
| 28 | 364–381 | Immunization | – | – | _Alasan Tidak Diberikan Vaksin HB0_ → `Immunization.status` (379, tanpa BQ) |
| 29 | 382–393 | QuestionnaireResponse | https://fhir.kemkes.go.id/Questionnaire/Q0004 | – | _Kelas Ibu Balita_ → `QuestionnaireResponse.questionnaire` (382, tanpa BQ) |
| 30 | 395–408 | ServiceRequest | 409014006.0 | Delivery care management | _Faskes Tujuan Rujukan_ → `ServiceRequest.performer.display` (407, tanpa BQ)<br>_Nama Faskes Rujukan_ → `ServiceRequest.locationCode.text` (408, tanpa BQ) |
| 31 | 409–421 | Observation | 10206-1 | Physical findings of Skin Narrative | _Pemeriksaan Kulit_ → `Observation.valueString` (412, tanpa BQ)<br>_Interpretasi Hasil Pemeriksaan Kulit_ → `Observation.interpretation.coding` (413, tanpa BQ) |
| 32 | 422–434 | Observation | 10199-8 | Physical findings of Head Narrative | _Pemeriksaan Kepala_ → `Observation.valueString` (425, tanpa BQ)<br>_Interpretasi Hasil Pemeriksaan Kepala_ → `Observation.interpretation.coding` (426, tanpa BQ) |
| 33 | 435–447 | Observation | 10197-2 | Physical findings of Eye Narrative | _Pemeriksaan Mata_ → `Observation.valueString` (438, tanpa BQ)<br>_Interpretasi Hasil Pemeriksaan Mata_ → `Observation.interpretation.coding` (439, tanpa BQ) |
| 34 | 448–460 | Observation | 32453-3 | Physical findings of Mouth | _Pemeriksaan Mulut_ → `Observation.valueString` (451, tanpa BQ)<br>_Interpretasi Hasil Pemeriksaan Mulut_ → `Observation.interpretation.coding` (452, tanpa BQ) |
| 35 | 461–473 | Observation | 10191-5 | Physical findings of Abdomen Narrative | _Pemeriksaan Perut_ → `Observation.valueString` (464, tanpa BQ)<br>_Interpretasi Hasil Pemeriksaan Perut_ → `Observation.interpretation.coding` (465, tanpa BQ) |
| 36 | 474–486 | Observation | 10192-3 | Physical findings of Back Narrative | _Pemeriksaan Punggung_ → `Observation.valueString` (477, tanpa BQ)<br>_Interpretasi Hasil Pemeriksaan Punggung_ → `Observation.interpretation.coding` (478, tanpa BQ) |
| 37 | 487–499 | Observation | 11388-6 | Physical findings of Buttocks Narrative | _Pemeriksaan Lubang Anus_ → `Observation.valueString` (490, tanpa BQ)<br>_Interpretasi Hasil Pemeriksaan Lubang Anus_ → `Observation.interpretation.coding` (491, tanpa BQ) |
| 38 | 500–512 | Observation | 11400-9 | Physical findings of Genitalia Narrative | _Pemeriksaan Alat Kelamin_ → `Observation.valueString` (503, tanpa BQ)<br>_Interpretasi Hasil Pemeriksaan Alat Kelamin_ → `Observation.interpretation.coding` (504, tanpa BQ) |
| 39 | 513–528 | AllergyIntolerance | – | – | _Apakah ada alergi obat saat ini?_ → `AllergyIntolerance.clinicalStatus.coding` (513, tanpa BQ)<br>_Jika Ya, jenis obat?_ → `AllergyIntolerance.code.coding` (515, tanpa BQ) |
| 40 | 529–539 | Procedure | 431868002.0 | Initiation of breastfeeding | _Inisiasi Menyusu Dini (IMD)_ → `Procedure.category.coding` (529, tanpa BQ) |
| 41 | 540–551 | Observation | OC000016 | Waktu Inisiasi Menyusui Dini | _Waktu Inisiasi Menyusu Dini (IMD)_ → `Observation.valueCodeableConcept.coding` (543, tanpa BQ) |
| 42 | 552–566 | Immunization | 787859002.0 | Vaccine product | _Tanggal Pemberian Vaksin_ → `Immunization.occurrenceDateTime` (552, tanpa BQ)<br>_Nomor Lot Vaksin_ → `Immunization.lotNumber` (557, tanpa BQ)<br>_Tanggal Kadaluarsa Vaksin_ → `Immunization.expirationDate` (558, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 25 |
| Procedure | 4 |
| RelatedPerson | 2 |
| Immunization | 2 |
| Practitioner | 1 |
| PractitionerRole | 1 |
| Patient | 1 |
| Encounter | 1 |
| Condition | 1 |
| EpisodeOfCare | 1 |
| QuestionnaireResponse | 1 |
| ServiceRequest | 1 |
| AllergyIntolerance | 1 |
| **Total** | **42** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 11 | PractitionerRole | `PractitionerRole.code.coding` | 309453006.0 | Registered midwife | http://snomed.info/sct |
| 2 | 12 | PractitionerRole | `PractitionerRole.code.coding` | 309367003.0 | Obstetrician and gynecologist | http://snomed.info/sct |
| 3 | 13 | PractitionerRole | `PractitionerRole.code.coding` | 309343006.0 | Physician | http://snomed.info/sct |
| 4 | 14 | PractitionerRole | `PractitionerRole.code.coding` | 224535009.0 | Registered nurse | http://snomed.info/sct |
| 5 | 15 | PractitionerRole | `PractitionerRole.code.coding` | 224535009.0 | Registered nurse | http://snomed.info/sct |
| 6 | 85 | Condition | `Condition.code.coding` | Z00.1 | Routine child health examination | http://hl7.org/fhir/sid/icd-10 |
| 7 | 102 | EpisodeOfCare | `EpisodeOfCare.type.coding` | Neonate | Neonate | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 8 | 112 | Observation | `Observation.code.coding` | 72150-6 | Delivery location | http://loinc.org |
| 9 | 113 | Observation | `Observation.valueCodeableConcept.coding` | 104.0 | Rumah Sakit | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 10 | 123 | Observation | `Observation.code.coding` | 365475008.0 | Place in family order | http://snomed.info/sct |
| 11 | 134 | Observation | `Observation.code.coding` | 57715-5 | Birth time | http://loinc.org |
| 12 | 145 | Observation | `Observation.code.coding` | 76516-4 | Gestational age—​at birth | http://loinc.org |
| 13 | 148 | Observation | `Observation.component.code.coding` | SP000398 | Usia Kehamilan Saat Persalinan (hari) | http://terminology.kemkes.go.id/sp |
| 14 | 187 | Observation | `Observation.code.coding` | 8339-4 | Birth weight Measured | http://loinc.org |
| 15 | 199 | Observation | `Observation.code.coding` | 89269-5 | Body height Measured --at birth | http://loinc.org |
| 16 | 211 | Observation | `Observation.code.coding` | 8290-9 | Head Occipital-frontal circumference --at birth- by Tape measure | http://loinc.org |
| 17 | 223 | Observation | `Observation.code.coding` | 8867-4 | Heart rate | http://loinc.org |
| 18 | 236 | Observation | `Observation.code.coding` | 8310-5 | Body temperature | http://loinc.org |
| 19 | 249 | Observation | `Observation.code.coding` | 9279-1 | Respiratory rate | http://loinc.org |
| 20 | 262 | Observation | `Observation.code.coding` | 20564-1 | Oxygen saturation in Blood | http://loinc.org |
| 21 | 274 | Observation | `Observation.code.coding` | 276654001.0 | Congenital malformation | http://snomed.info/sct |
| 22 | 285 | Observation | `Observation.code.coding` | 1145307003.0 | Exclusively breastfed | http://snomed.info/sct |
| 23 | 297 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 24 | 309 | Observation | `Observation.code.coding` | 8306-3 | Body height --lying | http://loinc.org |
| 25 | 320 | Procedure | `Procedure.code.coding` | 400984005.0 | Congenital hypothyroidism screening test | http://snomed.info/sct |
| 26 | 332 | Observation | `Observation.code.coding` | 29575-8 | Thyrotropin [Units/volume] in DBS | http://loinc.org |
| 27 | 345 | Procedure | `Procedure.code.coding` | SP000296 | Skrining Penyakit Jantung Bawaan | http://terminology.kemkes.go.id/sp |
| 28 | 354 | Procedure | `Procedure.code.coding` | 408989004.0 | Newborn care management | http://snomed.info/sct |
| 29 | 366 | Immunization | `Immunization.vaccineCode` | VG45 | HepB | http://sys-ids.kemkes.go.id/kfa |
| 30 | 399 | ServiceRequest | `ServiceRequest.code.coding` | 409014006.0 | Delivery care management | http://snomed.info/sct |
| 31 | 411 | Observation | `Observation.code.coding` | 10206-1 | Physical findings of Skin Narrative | http://loinc.org |
| 32 | 413 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 33 | 414 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 34 | 424 | Observation | `Observation.code.coding` | 10199-8 | Physical findings of Head Narrative | http://loinc.org |
| 35 | 426 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 36 | 427 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 37 | 437 | Observation | `Observation.code.coding` | 10197-2 | Physical findings of Eye Narrative | http://loinc.org |
| 38 | 439 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 39 | 440 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 40 | 450 | Observation | `Observation.code.coding` | 32453-3 | Physical findings of Mouth | http://loinc.org |
| 41 | 452 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 42 | 453 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 43 | 463 | Observation | `Observation.code.coding` | 10191-5 | Physical findings of Abdomen Narrative | http://loinc.org |
| 44 | 465 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 45 | 466 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 46 | 476 | Observation | `Observation.code.coding` | 10192-3 | Physical findings of Back Narrative | http://loinc.org |
| 47 | 478 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 48 | 479 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 49 | 489 | Observation | `Observation.code.coding` | 11388-6 | Physical findings of Buttocks Narrative | http://loinc.org |
| 50 | 491 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 51 | 492 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 52 | 502 | Observation | `Observation.code.coding` | 11400-9 | Physical findings of Genitalia Narrative | http://loinc.org |
| 53 | 504 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 54 | 505 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 55 | 532 | Procedure | `Procedure.code.coding` | 431868002.0 | Initiation of breastfeeding | http://snomed.info/sct |
| 56 | 542 | Observation | `Observation.code.coding` | OC000016 | Waktu Inisiasi Menyusui Dini | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 57 | 543 | Observation | `Observation.valueCodeableConcept.coding` | OV000014 | Kurang dari 1 Jam | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 58 | 544 | Observation | `Observation.valueCodeableConcept.coding` | OV000015 | Lebih dari 1 Jam | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 59 | 554 | Immunization | `Immunization.vaccineCode.coding` | 787859002.0 | Vaccine product | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://loinc.org | 21 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 16 |
| http://snomed.info/sct | 13 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 3 |
| http://terminology.kemkes.go.id/sp | 2 |
| http://hl7.org/fhir/sid/icd-10 | 1 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 1 |
| http://terminology.kemkes.go.id/CodeSystem/organization-type | 1 |
| http://sys-ids.kemkes.go.id/kfa | 1 |
| **Total** | **59** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 34 | – | Jenis Faskes | – | `` |
| 35 | – | Email Faskes | – | `` |
| 394 | – | Rujuk | – | `` |
