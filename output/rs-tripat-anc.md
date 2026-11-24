# Output Form: SIM RS Tripat ANC

Sumber: `mapping/phdt-data-dictionary-rs-tripat-anc.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-rs-tripat-anc.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 20 |
| Code (`jumlah code` = 1) | 28 |
| Code unik (code + CodeSystem) | 27 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 0 |
| Variabel BQ (unik) | 31 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–26 | Patient | – | – | `nama` → `Patient.name.text` (2)<br>`nomor_identitas` → `Patient.identifier.value` (5)<br>`nomor_telepon` → `Patient.telecom.value` (8)<br>`tgl_lahir` → `Patient.birthDate` (11)<br>`alamat` → `Patient.address.line` (13)<br>`nama_propinsi` → `Patient.address.extension.extension.valueCode` (15)<br>`keterangan_kota_kabupaten` → `Patient.address.extension.extension.valueCode` (18)<br>`keterangan_kecamatan` → `Patient.address.extension.extension.valueCode` (21)<br>`keterangan_kelurahan` → `Patient.address.extension.extension.valueCode` (24) |
| 2 | 39–40 | Practitioner | – | – | `nama_tenaga_pemeriksa` → `Practitioner.name.text` (39) |
| 3 | 41–46 | PractitionerRole | – | – | `tenaga_pemeriksa` → `PractitionerRole.code.coding` (41)<br>`tenaga_pemeriksa` → `PractitionerRole.code.coding` (42)<br>`tenaga_pemeriksa` → `PractitionerRole.code.coding` (43)<br>`tenaga_pemeriksa` → `PractitionerRole.code.coding` (44)<br>`nama_tenaga_pemeriksa` → `PractitionerRole.practitioner.reference` (45)<br>`faskes` → `PractitionerRole.organization.reference` (46) |
| 4 | 47–53 | Practitioner | – | – | `nik_dpjp` → `Practitioner.identifier.value` (47)<br>`employee_name_dpjp` → `Practitioner.name.text` (50)<br>`jenis_kelamin_dpjp` → `Practitioner.gender` (51)<br>`jenis_kelamin_dpjp` → `Practitioner.gender` (52) |
| 5 | 54–56 | PractitionerRole | – | – | `employee_name_dpjp` → `PractitionerRole.practitioner.reference` (55)<br>`faskes` → `PractitionerRole.organization.reference` (56) |
| 6 | 57–65 | EpisodeOfCare | ANC | Antenatal Care | `hpht` → `EpisodeOfCare.period.start` (60)<br>`hpht` → `EpisodeOfCare.statusHistory.period.start` (62)<br>`nama` → `EpisodeOfCare.patient.reference` (63)<br>`nama` → `EpisodeOfCare.patient.display` (64)<br>`faskes` → `EpisodeOfCare.managingOrganization.reference` (65) |
| 7 | 66–91 | Encounter | – | – | `no_pendaftaran` → `Encounter.identifier.value` (66)<br>`tgl_pendaftaran, tgl_entri` → `Encounter.period.start` (70)<br>`tgl_pendaftaran, tgl_entri` → `Encounter.period.end` (71)<br>`nama` → `Encounter.subject.reference` (73)<br>`nama` → `Encounter.subject.display` (74)<br>`nama_tenaga_pemeriksa` → `Encounter.participant.individual.reference` (76)<br>`nama_tenaga_pemeriksa` → `Encounter.participant.individual.display` (77)<br>`tempat_anc` → `Encounter.location.location.reference` (78)<br>`tempat_anc` → `Encounter.location.location.display` (79)<br>`tgl_pendaftaran, tgl_entri` → `Encounter.statusHistory.period.start` (81)<br>`tgl_pendaftaran, tgl_entri` → `Encounter.statusHistory.period.end` (82)<br>`tgl_pendaftaran, tgl_entri` → `Encounter.statusHistory.period.start` (84)<br>`tgl_pendaftaran, tgl_entri` → `Encounter.statusHistory.period.end` (85)<br>`tgl_pendaftaran, tgl_entri` → `Encounter.statusHistory.period.start` (87)<br>`tgl_pendaftaran, tgl_entri` → `Encounter.statusHistory.period.end` (88)<br>`faskes` → `Encounter.serviceProvider.reference` (91) |
| 8 | 92–101 | Condition | 134435003.0 | Routine antenatal care | `nama_icdx` → `Condition.code.coding` (92)<br>`nama_icdx` → `Condition.code.text` (94)<br>`nama` → `Condition.subject.reference` (97)<br>`nama` → `Condition.subject.display` (98)<br>`no_pendaftaran` → `Condition.encounter.reference` (99)<br>`tgl_pendaftaran, tgl_entri` → `Condition.recordedDate` (100)<br>`tgl_pendaftaran, tgl_entri` → `Condition.onsetDateTime` (101) |
| 9 | 102–113 | Observation | 8665-2 | Last menstrual period start date | `hpht` → `Observation.code.coding` (102)<br>`hpht` → `Observation.valueDateTime` (105)<br>`nama` → `Observation.subject.reference` (107)<br>`nama` → `Observation.subject.display` (108)<br>`no_pendaftaran` → `Observation.encounter.reference` (109)<br>`tgl_pendaftaran, tgl_entri` → `Observation.effectiveDateTime` (110)<br>`tgl_pendaftaran, tgl_entri` → `Observation.issued` (111)<br>`nama_tenaga_pemeriksa` → `Observation.performer.reference` (112)<br>`nama_tenaga_pemeriksa` → `Observation.performer.display` (113) |
| 10 | 114–125 | Observation | 11778-8 | Delivery date Estimated | `hpl` → `Observation.code.coding` (114)<br>`hpl` → `Observation.valueDateTime` (117)<br>`nama` → `Observation.subject.reference` (119)<br>`nama` → `Observation.subject.display` (120)<br>`no_pendaftaran` → `Observation.encounter.reference` (121)<br>`tgl_pendaftaran, tgl_entri` → `Observation.effectiveDateTime` (122)<br>`tgl_pendaftaran, tgl_entri` → `Observation.issued` (123)<br>`nama_tenaga_pemeriksa` → `Observation.performer.reference` (124)<br>`nama_tenaga_pemeriksa` → `Observation.performer.display` (125) |
| 11 | 126–138 | Observation | 18185-9 | Gestational age | `usia_kehamilan` → `Observation.code.coding` (126)<br>`usia_kehamilan` → `Observation.valueQuantity.value` (129)<br>`nama` → `Observation.subject.reference` (132)<br>`nama` → `Observation.subject.display` (133)<br>`no_pendaftaran` → `Observation.encounter.reference` (134)<br>`tgl_pendaftaran, tgl_entri` → `Observation.effectiveDateTime` (135)<br>`tgl_pendaftaran, tgl_entri` → `Observation.issued` (136)<br>`nama_tenaga_pemeriksa` → `Observation.performer.reference` (137)<br>`nama_tenaga_pemeriksa` → `Observation.performer.display` (138) |
| 12 | 139–151 | Observation | 29463-7 | Body weight | `berat_badan` → `Observation.code.coding` (139)<br>`berat_badan` → `Observation.valueQuantity.value` (142)<br>`nama` → `Observation.subject.reference` (145)<br>`nama` → `Observation.subject.display` (146)<br>`no_pendaftaran` → `Observation.encounter.reference` (147)<br>`tgl_pendaftaran, tgl_entri` → `Observation.effectiveDateTime` (148)<br>`tgl_pendaftaran, tgl_entri` → `Observation.issued` (149)<br>`nama_tenaga_pemeriksa` → `Observation.performer.reference` (150)<br>`nama_tenaga_pemeriksa` → `Observation.performer.display` (151) |
| 13 | 152–164 | Observation | 8302-2 | Body height | `tinggi_badan` → `Observation.code.coding` (152)<br>`tinggi_badan` → `Observation.valueQuantity.value` (155)<br>`nama` → `Observation.subject.reference` (158)<br>`nama` → `Observation.subject.display` (159)<br>`no_pendaftaran` → `Observation.encounter.reference` (160)<br>`tgl_pendaftaran, tgl_entri` → `Observation.effectiveDateTime` (161)<br>`tgl_pendaftaran, tgl_entri` → `Observation.issued` (162)<br>`nama_tenaga_pemeriksa` → `Observation.performer.reference` (163)<br>`nama_tenaga_pemeriksa` → `Observation.performer.display` (164) |
| 14 | 165–176 | Observation | 8480-6 | Systolic blood pressure | `tekanan_darah` → `Observation.code.coding` (165)<br>`tekanan_darah` → `Observation.valueQuantity.value` (167)<br>`nama` → `Observation.subject.reference` (170)<br>`nama` → `Observation.subject.display` (171)<br>`no_pendaftaran` → `Observation.encounter.reference` (172)<br>`tgl_pendaftaran, tgl_entri` → `Observation.effectiveDateTime` (173)<br>`tgl_pendaftaran, tgl_entri` → `Observation.issued` (174)<br>`nama_tenaga_pemeriksa` → `Observation.performer.reference` (175)<br>`nama_tenaga_pemeriksa` → `Observation.performer.display` (176) |
| 15 | 177–188 | Observation | 8462-4 | Diastolic blood pressure | `tekanan_darah` → `Observation.code.coding` (177)<br>`tekanan_darah` → `Observation.valueQuantity.value` (179)<br>`nama` → `Observation.subject.reference` (182)<br>`nama` → `Observation.subject.display` (183)<br>`no_pendaftaran` → `Observation.encounter.reference` (184)<br>`tgl_pendaftaran, tgl_entri` → `Observation.effectiveDateTime` (185)<br>`tgl_pendaftaran, tgl_entri` → `Observation.issued` (186)<br>`nama_tenaga_pemeriksa` → `Observation.performer.reference` (187)<br>`nama_tenaga_pemeriksa` → `Observation.performer.display` (188) |
| 16 | 189–199 | Observation | 103975-9 | Previous delivery date | `kehamilan_terakhir` → `Observation.code.coding` (189)<br>`kehamilan_terakhir` → `Observation.valueDateTime` (191)<br>`nama` → `Observation.subject.reference` (193)<br>`nama` → `Observation.subject.display` (194)<br>`no_pendaftaran` → `Observation.encounter.reference` (195)<br>`tgl_pendaftaran, tgl_entri` → `Observation.effectiveDateTime` (196)<br>`tgl_pendaftaran, tgl_entri` → `Observation.issued` (197)<br>`nama_tenaga_pemeriksa` → `Observation.performer.reference` (198)<br>`nama_tenaga_pemeriksa` → `Observation.performer.display` (199) |
| 17 | 200–215 | Observation | 72155-5 | Position in womb Fetus [RHEA] | `letak_presentasi` → `Observation.code.coding` (200)<br>`letak_presentasi` → `Observation.valueCodeableConcept.coding` (203)<br>`letak_presentasi` → `Observation.valueCodeableConcept.coding` (204)<br>`letak_presentasi` → `Observation.valueCodeableConcept.coding` (205)<br>`letak_presentasi` → `Observation.valueCodeableConcept.coding` (206)<br>`letak_presentasi` → `Observation.valueCodeableConcept.text` (207)<br>`nama` → `Observation.subject.reference` (209)<br>`nama` → `Observation.subject.display` (210)<br>`no_pendaftaran` → `Observation.encounter.reference` (211)<br>`tgl_pendaftaran, tgl_entri` → `Observation.effectiveDateTime` (212)<br>`tgl_pendaftaran, tgl_entri` → `Observation.issued` (213)<br>`nama_tenaga_pemeriksa` → `Observation.performer.reference` (214)<br>`nama_tenaga_pemeriksa` → `Observation.performer.display` (215) |
| 18 | 216–229 | Immunization | VG139 | Td | `imunisasi_tt` → `Immunization.status` (216)<br>`imunisasi_tt` → `Immunization.status` (217)<br>`imunisasi_tt_kali` → `Immunization.protocolApplied.doseNumberPositiveInt` (221)<br>`nama` → `Immunization.patient.reference` (223)<br>`nama` → `Immunization.patient.display` (224)<br>`no_pendaftaran` → `Immunization.encounter.reference` (225)<br>`tgl_pendaftaran, tgl_entri` → `Immunization.recorded` (226)<br>`nama_tenaga_pemeriksa` → `Immunization.performer.actor.reference` (228)<br>`nama_tenaga_pemeriksa` → `Immunization.performer.actor.display` (229) |
| 19 | 230–237 | MedicationStatement | – | – | `obat` → `MedicationStatement.medicationCodeableConcept.text` (230)<br>`nama` → `MedicationStatement.subject.reference` (233)<br>`nama` → `MedicationStatement.subject.display` (234)<br>`tgl_pendaftaran, tgl_entri` → `MedicationStatement.effectiveDateTime` (235)<br>`nama_tenaga_pemeriksa` → `MedicationStatement.informationSource.reference` (236)<br>`no_pendaftaran` → `MedicationStatement.context.reference` (237) |
| 20 | 238–247 | Procedure | 71388002.0 | Procedure | `tindakan` → `Procedure.code.coding` (238)<br>`tindakan` → `Procedure.code.text` (239)<br>`nama` → `Procedure.subject.reference` (242)<br>`nama` → `Procedure.subject.display` (243)<br>`no_pendaftaran` → `Procedure.encounter.reference` (244)<br>`tgl_pendaftaran, tgl_entri` → `Procedure.performedDateTime` (245)<br>`nama_tenaga_pemeriksa` → `Procedure.performer.actor.reference` (246)<br>`nama_tenaga_pemeriksa` → `Procedure.performer.actor.display` (247) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 9 |
| Practitioner | 2 |
| PractitionerRole | 2 |
| Patient | 1 |
| EpisodeOfCare | 1 |
| Encounter | 1 |
| Condition | 1 |
| Immunization | 1 |
| MedicationStatement | 1 |
| Procedure | 1 |
| **Total** | **20** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 41 | PractitionerRole | `PractitionerRole.code.coding` | 309453006.0 | Registered midwife | http://snomed.info/sct |
| 2 | 42 | PractitionerRole | `PractitionerRole.code.coding` | 309367003.0 | Obstetrician and gynecologist | http://snomed.info/sct |
| 3 | 43 | PractitionerRole | `PractitionerRole.code.coding` | 224535009.0 | Registered nurse | http://snomed.info/sct |
| 4 | 44 | PractitionerRole | `PractitionerRole.code.coding` | 768827000.0 | Nutritionist | http://snomed.info/sct |
| 5 | 54 | PractitionerRole | `PractitionerRole.code.coding` | 309367003.0 | Obstetrician and gynecologist | http://snomed.info/sct |
| 6 | 57 | EpisodeOfCare | `EpisodeOfCare.type.coding` | ANC | Antenatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 7 | 93 | Condition | `Condition.code.coding` | 134435003.0 | Routine antenatal care | http://snomed.info/sct |
| 8 | 102 | Observation | `Observation.code.coding` | 8665-2 | Last menstrual period start date | http://loinc.org |
| 9 | 103 | Observation | `Observation.code.coding` | ANC.B6.DE14 | Last menstrual period (LMP) date | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 10 | 114 | Observation | `Observation.code.coding` | 11778-8 | Delivery date Estimated | http://loinc.org |
| 11 | 115 | Observation | `Observation.code.coding` | ANC.B6.DE22 | Expected date of delivery (EDD) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 12 | 126 | Observation | `Observation.code.coding` | 18185-9 | Gestational age | http://loinc.org |
| 13 | 127 | Observation | `Observation.code.coding` | ANC.B6.DE17 | Gestational age | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 14 | 139 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 15 | 140 | Observation | `Observation.code.coding` | ANC.B8.DE3 | Current weight | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 16 | 152 | Observation | `Observation.code.coding` | 8302-2 | Body height | http://loinc.org |
| 17 | 153 | Observation | `Observation.code.coding` | ANC.B8.DE1 | Height | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 18 | 165 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 19 | 177 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://loinc.org |
| 20 | 189 | Observation | `Observation.code.coding` | 103975-9 | Previous delivery date | http://loinc.org |
| 21 | 200 | Observation | `Observation.code.coding` | 72155-5 | Position in womb Fetus [RHEA] | http://loinc.org |
| 22 | 201 | Observation | `Observation.code.coding` | ANC.B8.DE111 | Fetal presentation | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 23 | 203 | Observation | `Observation.valueCodeableConcept.coding` | 1209182005.0 | Cephalic fetal presentation | http://snomed.info/sct |
| 24 | 204 | Observation | `Observation.valueCodeableConcept.coding` | 6096002.0 | Breech presentation | http://snomed.info/sct |
| 25 | 205 | Observation | `Observation.valueCodeableConcept.coding` | 73161006.0 | Transverse lie | http://snomed.info/sct |
| 26 | 206 | Observation | `Observation.valueCodeableConcept.coding` | 63750008.0 | Oblique lie | http://snomed.info/sct |
| 27 | 218 | Immunization | `Immunization.vaccineCode.coding` | VG139 | Td | http://sys-ids.kemkes.go.id/kfa |
| 28 | 238 | Procedure | `Procedure.code.coding` | 71388002.0 | Procedure | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 11 |
| http://loinc.org | 9 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 6 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 1 |
| http://sys-ids.kemkes.go.id/kfa | 1 |
| **Total** | **28** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 27 | ⚠️ faskes | Faskes yang Melayani ANC | Organization | `Organization.name` |
| 33 | ⚠️ tempat_anc | Tempat ANC | Location | `Location.name` |
