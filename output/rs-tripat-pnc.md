# Output Form: SIM RS Tripat PNC

Sumber: `mapping/phdt-data-dictionary-rs-tripat-pnc.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-rs-tripat-pnc.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 24 |
| Code (`jumlah code` = 1) | 28 |
| Code unik (code + CodeSystem) | 27 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 0 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–26 | Patient | – | – | _Nama Ibu_ → `Patient.name.text` (2, tanpa BQ)<br>_NIK_ → `Patient.identifier.value` (5, tanpa BQ)<br>_No HP_ → `Patient.telecom.value` (8, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (11, tanpa BQ)<br>_Alamat Domisili_ → `Patient.address.line` (13, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (15, tanpa BQ)<br>_Nama Kabupaten/Kota_ → `Patient.address.extension.extension.valueCode` (18, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.extension.valueCode` (21, tanpa BQ)<br>_Nama Kelurahan/Desa_ → `Patient.address.extension.extension.valueCode` (24, tanpa BQ) |
| 2 | 39–40 | Practitioner | – | – | _Nama Tenaga Pemeriksa_ → `Practitioner.name.text` (39, tanpa BQ) |
| 3 | 41–47 | PractitionerRole | – | – | _Tenaga Pemeriksa (Role)_ → `PractitionerRole.code.coding` (41, tanpa BQ) |
| 4 | 48–54 | Practitioner | – | – | _NIK DPJP_ → `Practitioner.identifier.value` (48, tanpa BQ)<br>_Nama DPJP_ → `Practitioner.name.text` (51, tanpa BQ)<br>_Jenis Kelamin DPJP_ → `Practitioner.gender` (52, tanpa BQ) |
| 5 | 55–57 | PractitionerRole | – | – | – |
| 6 | 58–66 | EpisodeOfCare | PNC | Postnatal Care | – |
| 7 | 67–96 | Encounter | – | – | _Nomor Pendaftaran_ → `Encounter.identifier.value` (67, tanpa BQ)<br>_Tanggal Kunjungan PNC_ → `Encounter.period.start` (71, tanpa BQ)<br>_Cara Masuk_ → `Encounter.hospitalization.admitSource.coding` (81, tanpa BQ) |
| 8 | 97–106 | Condition | Z39.2 | Routine postpartum follow-up | _Diagnosa ICD-X_ → `Condition.code.coding` (97, tanpa BQ) |
| 9 | 107–115 | Condition | 404684003 | Clinical finding | _Keluhan Utama_ → `Condition.code.coding` (107, tanpa BQ) |
| 10 | 116–126 | Observation | 93857-1 | Date and time of obstetric delivery | _Tanggal Persalinan_ → `Observation.valueDateTime` (118, tanpa BQ) |
| 11 | 127–138 | Observation | 11996-6 | [#] Pregnancies | _Gravida_ → `Observation.valueInteger` (130, tanpa BQ) |
| 12 | 139–150 | Observation | 11977-6 | [#] Parity | _Partus_ → `Observation.valueInteger` (142, tanpa BQ) |
| 13 | 151–162 | Observation | 69043-8 | Other pregnancy outcomes # | _Abortus_ → `Observation.valueInteger` (154, tanpa BQ) |
| 14 | 163–174 | Observation | 8480-6 | Systolic blood pressure | _Tekanan Darah Sistolik_ → `Observation.valueQuantity.value` (165, tanpa BQ) |
| 15 | 175–186 | Observation | 8462-4 | Diastolic blood pressure | _Tekanan Darah Diastolik_ → `Observation.valueQuantity.value` (177, tanpa BQ) |
| 16 | 187–198 | Observation | 8867-4 | Heart rate | _Nadi_ → `Observation.valueQuantity.value` (189, tanpa BQ) |
| 17 | 199–210 | Observation | 9279-1 | Respiratory rate | _Pernapasan_ → `Observation.valueQuantity.value` (201, tanpa BQ) |
| 18 | 211–222 | Observation | 8310-5 | Body temperature | _Suhu_ → `Observation.valueQuantity.value` (213, tanpa BQ) |
| 19 | 223–234 | Observation | 8345-1 | Body weight Measured --post partum | _Berat Badan_ → `Observation.valueQuantity.value` (225, tanpa BQ) |
| 20 | 235–246 | Observation | 8305-5 | Body height --post partum | _Tinggi Badan_ → `Observation.valueQuantity.value` (237, tanpa BQ) |
| 21 | 247–259 | Observation | 11881-0 | Uterus Fundal height Tape measure | _Tinggi Fundus Uteri (TFU)_ → `Observation.valueQuantity.value` (249, tanpa BQ) |
| 22 | 260–271 | Observation | 116859006 | Transfusion of blood product | _Status Transfusi_ → `Observation.valueBoolean` (262, tanpa BQ) |
| 23 | 272–279 | MedicationStatement | – | – | _Obat_ → `MedicationStatement.medicationCodeableConcept.text` (272, tanpa BQ) |
| 24 | 280–289 | Procedure | 71388002 | Procedure | _Tindakan_ → `Procedure.code.coding` (280, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 13 |
| Practitioner | 2 |
| PractitionerRole | 2 |
| Condition | 2 |
| Patient | 1 |
| EpisodeOfCare | 1 |
| Encounter | 1 |
| MedicationStatement | 1 |
| Procedure | 1 |
| **Total** | **24** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 41 | PractitionerRole | `PractitionerRole.code.coding` | 309453006 | Registered midwife | http://snomed.info/sct |
| 2 | 42 | PractitionerRole | `PractitionerRole.code.coding` | 309367003 | Obstetrician and gynecologist | http://snomed.info/sct |
| 3 | 43 | PractitionerRole | `PractitionerRole.code.coding` | 224535009 | Registered nurse | http://snomed.info/sct |
| 4 | 44 | PractitionerRole | `PractitionerRole.code.coding` | 768827000 | Nutritionist | http://snomed.info/sct |
| 5 | 45 | PractitionerRole | `PractitionerRole.code.coding` | 36682004 | Physiotherapist | http://snomed.info/sct |
| 6 | 55 | PractitionerRole | `PractitionerRole.code.coding` | 309367003 | Obstetrician and gynecologist | http://snomed.info/sct |
| 7 | 58 | EpisodeOfCare | `EpisodeOfCare.type.coding` | PNC | Postnatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 8 | 81 | Encounter | `Encounter.hospitalization.admitSource.coding` | EHA000002 | Datang sendiri | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 9 | 82 | Encounter | `Encounter.hospitalization.admitSource.coding` | 305956004 | Referral by physician | http://snomed.info/sct |
| 10 | 98 | Condition | `Condition.code.coding` | Z39.2 | Routine postpartum follow-up | http://hl7.org/fhir/sid/icd-10 |
| 11 | 107 | Condition | `Condition.code.coding` | 404684003 | Clinical finding | http://snomed.info/sct |
| 12 | 116 | Observation | `Observation.code.coding` | 93857-1 | Date and time of obstetric delivery | http://loinc.org |
| 13 | 127 | Observation | `Observation.code.coding` | 11996-6 | [#] Pregnancies | http://loinc.org |
| 14 | 128 | Observation | `Observation.code.coding` | ANC.B6.DE24 | Number of pregnancies (gravida) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 15 | 139 | Observation | `Observation.code.coding` | 11977-6 | [#] Parity | http://loinc.org |
| 16 | 140 | Observation | `Observation.code.coding` | ANC.B6.DE32 | Parity | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 17 | 151 | Observation | `Observation.code.coding` | 69043-8 | Other pregnancy outcomes # | http://loinc.org |
| 18 | 152 | Observation | `Observation.code.coding` | ANC.B6.DE25 | Number of miscarriages and/or abortions | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 19 | 163 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 20 | 175 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://loinc.org |
| 21 | 187 | Observation | `Observation.code.coding` | 8867-4 | Heart rate | http://loinc.org |
| 22 | 199 | Observation | `Observation.code.coding` | 9279-1 | Respiratory rate | http://loinc.org |
| 23 | 211 | Observation | `Observation.code.coding` | 8310-5 | Body temperature | http://loinc.org |
| 24 | 223 | Observation | `Observation.code.coding` | 8345-1 | Body weight Measured --post partum | http://loinc.org |
| 25 | 235 | Observation | `Observation.code.coding` | 8305-5 | Body height --post partum | http://loinc.org |
| 26 | 247 | Observation | `Observation.code.coding` | 11881-0 | Uterus Fundal height Tape measure | http://loinc.org |
| 27 | 260 | Observation | `Observation.code.coding` | 116859006 | Transfusion of blood product | http://snomed.info/sct |
| 28 | 280 | Procedure | `Procedure.code.coding` | 71388002 | Procedure | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://loinc.org | 12 |
| http://snomed.info/sct | 10 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 3 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 1 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 1 |
| http://hl7.org/fhir/sid/icd-10 | 1 |
| **Total** | **28** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 27 | – | Faskes yang Melayani PNC | Organization | `Organization.name` |
| 33 | – | Tempat Pelayanan PNC | Location | `Location.name` |
