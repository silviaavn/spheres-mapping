# Output Form: SIM RS Tripat BBL (sheet 'INC BBL')

Sumber: `mapping/phdt-data-dictionary-rs-tripat-bbl.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-rs-tripat-bbl.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 23 |
| Code (`jumlah code` = 1) | 20 |
| Code unik (code + CodeSystem) | 19 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 0 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–29 | Patient | – | – | _Nama Bayi_ → `Patient.name.text` (2, tanpa BQ)<br>_NIK Ibu_ → `Patient.identifier.value` (5, tanpa BQ)<br>_No HP Orang Tua_ → `Patient.telecom.value` (8, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (11, tanpa BQ)<br>_Tempat Lahir_ → `Patient.extension.valueAddress.city` (12, tanpa BQ)<br>_Kehamilan (Tunggal/Kembar)_ → `Patient.multipleBirthBoolean` (14, tanpa BQ)<br>_Alamat Domisili_ → `Patient.address.line` (16, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (18, tanpa BQ)<br>_Nama Kabupaten/Kota_ → `Patient.address.extension.extension.valueCode` (21, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.extension.valueCode` (24, tanpa BQ)<br>_Nama Kelurahan/Desa_ → `Patient.address.extension.extension.valueCode` (27, tanpa BQ) |
| 2 | 30–36 | RelatedPerson | – | – | _Nama Ibu_ → `RelatedPerson.name.text` (30, tanpa BQ) |
| 3 | 37–40 | RelatedPerson | – | – | _Nama Ayah_ → `RelatedPerson.name.text` (37, tanpa BQ) |
| 4 | 53–59 | Practitioner | – | – | _NIK Pemeriksa_ → `Practitioner.identifier.value` (53, tanpa BQ)<br>_Nama Tenaga Pemeriksa_ → `Practitioner.name.text` (56, tanpa BQ)<br>_Jenis Kelamin Pemeriksa_ → `Practitioner.gender` (57, tanpa BQ) |
| 5 | 60–65 | PractitionerRole | – | – | _Tenaga Pemeriksa (Role)_ → `PractitionerRole.code.coding` (60, tanpa BQ) |
| 6 | 66–67 | Practitioner | – | – | _Nama Dokter DPJP_ → `Practitioner.name.text` (66, tanpa BQ) |
| 7 | 68–70 | PractitionerRole | – | – | – |
| 8 | 71–79 | EpisodeOfCare | Neonate | Neonate | – |
| 9 | 80–105 | Encounter | – | – | _Nomor Pendaftaran_ → `Encounter.identifier.value` (80, tanpa BQ)<br>_Tanggal & Waktu INC (Bersalin)_ → `Encounter.period.start` (84, tanpa BQ) |
| 10 | 106–115 | Condition | Z00.1 | Routine child health examination | _Diagnosa ICD-X_ → `Condition.code.coding` (106, tanpa BQ) |
| 11 | 116–126 | Observation | 365475008 | Place in family order | _Kelahiran Ke_ → `Observation.valueInteger` (118, tanpa BQ) |
| 12 | 127–137 | Observation | 57715-5 | Birth time | _Jam Lahir_ → `Observation.valueTime` (129, tanpa BQ) |
| 13 | 138–149 | Observation | 76516-4 | Gestational age--at birth | _Usia Gestasi Saat Lahir_ → `Observation.valueQuantity.value` (140, tanpa BQ) |
| 14 | 150–161 | Observation | 8339-4 | Birth weight Measured | _Berat Badan Saat Lahir_ → `Observation.valueQuantity.value` (152, tanpa BQ) |
| 15 | 162–173 | Observation | 89269-5 | Body height Measured --at birth | _Panjang Badan Saat Lahir_ → `Observation.valueQuantity.value` (164, tanpa BQ) |
| 16 | 174–185 | Observation | 8290-9 | Head Occipital-frontal circumference --at birth- by Tape measure | _Lingkar Kepala Saat Lahir_ → `Observation.valueQuantity.value` (176, tanpa BQ) |
| 17 | 186–196 | Observation | 302083008 | Finding of Apgar score | _APGAR Score_ → `Observation.valueString` (188, tanpa BQ) |
| 18 | 197–208 | Observation | 276654001 | Congenital malformation | _Kelainan Bawaan_ → `Observation.valueBoolean` (199, tanpa BQ) |
| 19 | 209–220 | Observation | 8310-5 | Body temperature | _Suhu_ → `Observation.valueQuantity.value` (211, tanpa BQ) |
| 20 | 221–232 | Observation | 9279-1 | Respiratory rate | _Pernapasan_ → `Observation.valueQuantity.value` (223, tanpa BQ) |
| 21 | 233–244 | Observation | 8867-4 | Heart rate | _Frekuensi Denyut Jantung_ → `Observation.valueQuantity.value` (235, tanpa BQ) |
| 22 | 245–255 | Procedure | 386412000 | Resuscitation of neonate | _Riwayat Resusitasi_ → `Procedure.code.coding` (245, tanpa BQ) |
| 23 | 256–266 | Procedure | 431868002 | Initiation of breastfeeding | _Inisiasi Menyusu Dini (IMD)_ → `Procedure.code.coding` (256, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 11 |
| RelatedPerson | 2 |
| Practitioner | 2 |
| PractitionerRole | 2 |
| Procedure | 2 |
| Patient | 1 |
| EpisodeOfCare | 1 |
| Encounter | 1 |
| Condition | 1 |
| **Total** | **23** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 60 | PractitionerRole | `PractitionerRole.code.coding` | 309453006 | Registered midwife | http://snomed.info/sct |
| 2 | 61 | PractitionerRole | `PractitionerRole.code.coding` | 82296001 | Pediatrician | http://snomed.info/sct |
| 3 | 62 | PractitionerRole | `PractitionerRole.code.coding` | 224535009 | Registered nurse | http://snomed.info/sct |
| 4 | 63 | PractitionerRole | `PractitionerRole.code.coding` | 768827000 | Nutritionist | http://snomed.info/sct |
| 5 | 68 | PractitionerRole | `PractitionerRole.code.coding` | 82296001 | Pediatrician | http://snomed.info/sct |
| 6 | 71 | EpisodeOfCare | `EpisodeOfCare.type.coding` | Neonate | Neonate | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 7 | 107 | Condition | `Condition.code.coding` | Z00.1 | Routine child health examination | http://hl7.org/fhir/sid/icd-10 |
| 8 | 116 | Observation | `Observation.code.coding` | 365475008 | Place in family order | http://snomed.info/sct |
| 9 | 127 | Observation | `Observation.code.coding` | 57715-5 | Birth time | http://loinc.org |
| 10 | 138 | Observation | `Observation.code.coding` | 76516-4 | Gestational age--at birth | http://loinc.org |
| 11 | 150 | Observation | `Observation.code.coding` | 8339-4 | Birth weight Measured | http://loinc.org |
| 12 | 162 | Observation | `Observation.code.coding` | 89269-5 | Body height Measured --at birth | http://loinc.org |
| 13 | 174 | Observation | `Observation.code.coding` | 8290-9 | Head Occipital-frontal circumference --at birth- by Tape measure | http://loinc.org |
| 14 | 186 | Observation | `Observation.code.coding` | 302083008 | Finding of Apgar score | http://snomed.info/sct |
| 15 | 197 | Observation | `Observation.code.coding` | 276654001 | Congenital malformation | http://snomed.info/sct |
| 16 | 209 | Observation | `Observation.code.coding` | 8310-5 | Body temperature | http://loinc.org |
| 17 | 221 | Observation | `Observation.code.coding` | 9279-1 | Respiratory rate | http://loinc.org |
| 18 | 233 | Observation | `Observation.code.coding` | 8867-4 | Heart rate | http://loinc.org |
| 19 | 245 | Procedure | `Procedure.code.coding` | 386412000 | Resuscitation of neonate | http://snomed.info/sct |
| 20 | 256 | Procedure | `Procedure.code.coding` | 431868002 | Initiation of breastfeeding | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 10 |
| http://loinc.org | 8 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 1 |
| http://hl7.org/fhir/sid/icd-10 | 1 |
| **Total** | **20** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 41 | – | Faskes yang Melayani INC | Organization | `Organization.name` |
| 47 | – | Tempat Pelayanan INC | Location | `Location.name` |
