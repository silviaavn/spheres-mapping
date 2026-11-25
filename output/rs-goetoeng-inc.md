# Output Form: SIM RS Goetoeng INC

Sumber: `mapping/phdt-data-dictionary-rs-goetoeng-inc.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-rs-goetoeng-inc.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 64 |
| Code (`jumlah code` = 1) | 245 |
| Code unik (code + CodeSystem) | 131 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 12 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–26 | Patient | – | – | _Nama Ibu_ → `Patient.name.text` (2, tanpa BQ)<br>_No KTP_ → `Patient.identifier.value` (5, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (7, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (8, tanpa BQ)<br>_Alamat Domisili_ → `Patient.address.use` (9, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (15, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (18, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.extension.valueCode` (23, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.extension.valueCode` (26, tanpa BQ) |
| 2 | 94–108 | Encounter | – | – | _DPJP_ → `Encounter.participant.individual.display` (102, tanpa BQ)<br>_Tanggal Masuk_ → `Encounter.period.start` (103, tanpa BQ)<br>_Tanggal Keluar_ → `Encounter.period.end` (104, tanpa BQ)<br>_Ruang_ → `Encounter.location.location.display` (106, tanpa BQ)<br>_Keterangan Rujuk_ → `Encounter.hospitalization.admitSource.coding` (116, tanpa BQ)<br>_TINDAK LANJUT_ → `Encounter.hospitalization.dischargeDisposition.coding` (143, tanpa BQ) |
| 3 | 109–115 | Condition | 386337006.0 | Intrapartal care | – |
| 4 | 146–157 | ServiceRequest | – | – | _TINDAK LANJUT_ → `ServiceRequest.category` (146, tanpa BQ) |
| 5 | 158–174 | Coverage | – | – | _Cara Bayar_ → `Coverage.identifier` (158, tanpa BQ)<br>_KELAS_ → `Coverage.class.type.coding` (166, tanpa BQ) |
| 6 | 175–186 | Observation | 424144002.0 | Current chronological age | _Umur_ → `Observation.valueQuantity.value` (178, tanpa BQ) |
| 7 | 187–207 | Observation | 82589-3 | Highest level of education | _PENDIDIKAN_ → `Observation.valueCodeableConcept.coding` (190, tanpa BQ) |
| 8 | 208–249 | Condition | O61.0 | Failed medical induction of labour | _DX1_ → `Condition.clinicalStatus.coding` (208, tanpa BQ)<br>_KODE1_ → `Condition.clinicalStatus.coding` (242, tanpa BQ) |
| 9 | 250–283 | Condition | O61.0 | Failed medical induction of labour | _DX2_ → `Condition.clinicalStatus.coding` (276, tanpa BQ) |
| 10 | 284–331 | Condition | O42 | Premature rupture of membranes | _KODE2_ → `Condition.clinicalStatus.coding` (324, tanpa BQ) |
| 11 | 332–405 | Condition | O42 | Premature rupture of membranes | – |
| 12 | 406–416 | Procedure | 74.4 | Cesarean section of other specified type | _Tindakan_ → `Procedure.status` (406, tanpa BQ)<br>_KODE ICD9_ → `Procedure.category.coding` (415, tanpa BQ) |
| 13 | 417–418 | Procedure | 69.7 | Insertion of intrauterine contraceptive device | – |
| 14 | 419–420 | Procedure | 73.4 | Medical induction of labor | – |
| 15 | 421–422 | Procedure | 90.59 | Microscopic examination of blood, Other microscopic examination | – |
| 16 | 423–424 | Procedure | 88.78 | Diagnostic ultrasound of gravid uterus | – |
| 17 | 425–426 | Procedure | 75.32 | Fetal EKG (scalp) | – |
| 18 | 427–428 | Procedure | 91.39 | Microscopic examination of specimen from bladder, urethra, prostate,seminal vesicle, perivesical tissue, and of urine and semen, Other microscopic examination | – |
| 19 | 429–430 | Procedure | 89.52 | Electrocardiogram | – |
| 20 | 431–432 | Procedure | 66.39 | Other bilateral destruction or occlusion of fallopian tubes | – |
| 21 | 433–434 | Procedure | 99.04 | Transfusion of packed cells | – |
| 22 | 435–436 | Procedure | 69.7 | Insertion of intrauterine contraceptive device | – |
| 23 | 437–438 | Procedure | 90.52 | Microscopic examination of blood, Culture | – |
| 24 | 439–440 | Procedure | 88.09 | Other soft tissue x-ray of abdominal wall | – |
| 25 | 441–442 | Procedure | 97.71 | Removal of intrauterine contraceptive device | – |
| 26 | 443–444 | Procedure | 65.29 | Other local excision or destruction of ovary | – |
| 27 | 445–446 | Procedure | 69.02 | Dilation and curettage following delivery or abortion | – |
| 28 | 447–448 | Procedure | 57.94 | Insertion of indwelling urinary catheter | – |
| 29 | 449–450 | Procedure | 70.79 | Other repair of vagina | – |
| 30 | 451–452 | Procedure | 75.69 | Repair of other current obstetric laceration | – |
| 31 | 453–454 | Procedure | 73.59 | Other manually assisted delivery | – |
| 32 | 455–456 | Procedure | 73.59 | Other manually assisted delivery | – |
| 33 | 457–458 | Procedure | 75.51 | Repair of current obstetric laceration of cervix | – |
| 34 | 459–469 | Procedure | 75.69 | Repair of other current obstetric laceration | _Tindakan_ → `Procedure.status` (461, tanpa BQ) |
| 35 | 470–471 | Procedure | 74.4 | Cesarean section of other specified type | _PROSEDUR KLINIS_ → `Procedure.category.coding` (470, tanpa BQ) |
| 36 | 472–473 | Procedure | 69.7 | Insertion of intrauterine contraceptive device | – |
| 37 | 474–475 | Procedure | 73.4 | Medical induction of labor | – |
| 38 | 476–477 | Procedure | 90.59 | Microscopic examination of blood, Other microscopic examination | – |
| 39 | 478–479 | Procedure | 88.78 | Diagnostic ultrasound of gravid uterus | – |
| 40 | 480–481 | Procedure | 90.95 | Microscopic examination of specimen from lower gastrointestinal tract and of stool, Toxicology | – |
| 41 | 482–483 | Procedure | 75.32 | Fetal EKG (scalp) | – |
| 42 | 484–485 | Procedure | 89.52 | Electrocardiogram | – |
| 43 | 486–487 | Procedure | 91.3 | Microscopic examination of specimen from bladder, urethra, prostate,seminal vesicle, perivesical tissue, and of urine and semen | – |
| 44 | 488–489 | Procedure | 99.04 | Transfusion of packed cells | – |
| 45 | 490–491 | Procedure | 66.39 | Other bilateral destruction or occlusion of fallopian tubes | – |
| 46 | 492–493 | Procedure | 87.44 | Routine chest x-ray, so described | – |
| 47 | 494–495 | Procedure | 90.52 | Microscopic examination of blood, Culture | – |
| 48 | 496–497 | Procedure | 88.09 | Other soft tissue x-ray of abdominal wall | – |
| 49 | 498–499 | Procedure | 65.29 | Other local excision or destruction of ovary | – |
| 50 | 500–501 | Procedure | 97.71 | Removal of intrauterine contraceptive device | – |
| 51 | 502–503 | Procedure | 89.52 | Electrocardiogram | – |
| 52 | 504–505 | Procedure | 97.71 | Removal of intrauterine contraceptive device | – |
| 53 | 506–507 | Procedure | 73.59 | Other manually assisted delivery | – |
| 54 | 508–509 | Procedure | 69.02 | Dilation and curettage following delivery or abortion | – |
| 55 | 510–511 | Procedure | 75.51 | Repair of current obstetric laceration of cervix | – |
| 56 | 512–513 | Procedure | 73.6 | Episiotomy | – |
| 57 | 514–515 | Procedure | 75.69 | Repair of other current obstetric laceration | – |
| 58 | 516–517 | Procedure | 72.79 | Other vacuum extraction | – |
| 59 | 518–519 | Procedure | 75.92 | Evacuation of other hematoma of vulva or vagina | – |
| 60 | 520–529 | Condition | 268910001.0 | Patient's condition improved | _KEADAAN PASIEN_ → `Condition.clinicalStatus.coding` (520, tanpa BQ) |
| 61 | 530–541 | Observation | 183797002.0 | Duration of inpatient stay | _LAMA RAWAT (HARI)_ → `Observation.valueQuantity.value` (533, tanpa BQ) |
| 62 | 542–555 | Observation | SP000811 | Jalur Masuk Rawat Inap | _VIA_ → `Observation.valueCodeableConcept.coding` (545, tanpa BQ) |
| 63 | 556–567 | Observation | 184061005.0 | Patient registration status | _P.BARU_ → `Observation.valueCodeableConcept.coding` (559, tanpa BQ) |
| 64 | 568–578 | Composition | – | – | _DX RESUME PULANG_ → `Composition.status` (568, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Procedure | 48 |
| Condition | 6 |
| Observation | 5 |
| Patient | 1 |
| Encounter | 1 |
| ServiceRequest | 1 |
| Coverage | 1 |
| Composition | 1 |
| **Total** | **64** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 111 | Condition | `Condition.code.coding` | 386337006.0 | Intrapartal care | http://snomed.info/sct |
| 2 | 116 | Encounter | `Encounter.hospitalization.admitSource.coding` | 1991000124105.0 | Referred by self | http://snomed.info/sct |
| 3 | 117 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000814 | Rujukan dari Dokter Praktik Mandiri | http://terminology.kemkes.go.id/sp |
| 4 | 118 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000117 | Rujukan dari Puskesmas | http://terminology.kemkes.go.id/sp |
| 5 | 119 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000117 | Rujukan dari Puskesmas | http://terminology.kemkes.go.id/sp |
| 6 | 121 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000117 | Rujukan dari Puskesmas | http://terminology.kemkes.go.id/sp |
| 7 | 123 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000117 | Rujukan dari Puskesmas | http://terminology.kemkes.go.id/sp |
| 8 | 125 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000117 | Rujukan dari Puskesmas | http://terminology.kemkes.go.id/sp |
| 9 | 127 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000117 | Rujukan dari Puskesmas | http://terminology.kemkes.go.id/sp |
| 10 | 129 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000117 | Rujukan dari Puskesmas | http://terminology.kemkes.go.id/sp |
| 11 | 131 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000117 | Rujukan dari Puskesmas | http://terminology.kemkes.go.id/sp |
| 12 | 150 | ServiceRequest | `ServiceRequest.code` | 185389009.0 | Follow-up visit | http://snomed.info/sct |
| 13 | 177 | Observation | `Observation.code.coding` | 424144002.0 | Current chronological age | http://snomed.info/sct |
| 14 | 189 | Observation | `Observation.code.coding` | 82589-3 | Highest level of education | http://loinc.org |
| 15 | 190 | Observation | `Observation.valueCodeableConcept.coding` | 224294005.0 | No formal education | http://snomed.info/sct |
| 16 | 191 | Observation | `Observation.valueCodeableConcept.coding` | 473463000.0 | Received elementary school education | http://snomed.info/sct |
| 17 | 192 | Observation | `Observation.valueCodeableConcept.coding` | 603435002.0 | Educated to junior high school level | http://snomed.info/sct |
| 18 | 193 | Observation | `Observation.valueCodeableConcept.coding` | 603434003.0 | Educated to senior high school level | http://snomed.info/sct |
| 19 | 194 | Observation | `Observation.valueCodeableConcept.coding` | 38901000087109.0 | University diploma achieved | http://snomed.info/sct |
| 20 | 196 | Observation | `Observation.valueCodeableConcept.coding` | 38901000087109.0 | University diploma achieved | http://snomed.info/sct |
| 21 | 198 | Observation | `Observation.valueCodeableConcept.coding` | 38861000087100.0 | Bachelor's degree achieved | http://snomed.info/sct |
| 22 | 200 | Observation | `Observation.valueCodeableConcept.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 23 | 216 | Condition | `Condition.code.coding` | O61.0 | Failed medical induction of labour | http://hl7.org/fhir/sid/icd-10 |
| 24 | 217 | Condition | `Condition.code.coding` | O64.4 | Obstructed labour due to shoulder presentation | http://hl7.org/fhir/sid/icd-10 |
| 25 | 218 | Condition | `Condition.code.coding` | O42.0 | Premature rupture of membranes, onset of labour within 24 hours | http://hl7.org/fhir/sid/icd-10 |
| 26 | 219 | Condition | `Condition.code.coding` | O33.0 | Maternal care for disproportion due to deformity of maternal pelvic bones | http://hl7.org/fhir/sid/icd-10 |
| 27 | 220 | Condition | `Condition.code.coding` | O34.2 | Maternal care due to uterine scar from previous surgery | http://hl7.org/fhir/sid/icd-10 |
| 28 | 221 | Condition | `Condition.code.coding` | O45.0 | Premature separation of placenta with coagulation defect | http://hl7.org/fhir/sid/icd-10 |
| 29 | 222 | Condition | `Condition.code.coding` | O33.9 | Maternal care for disproportion, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 30 | 223 | Condition | `Condition.code.coding` | O63.1 | Prolonged second stage of labour | http://hl7.org/fhir/sid/icd-10 |
| 31 | 224 | Condition | `Condition.code.coding` | O64.1 | Obstructed labour due to breech presentation | http://hl7.org/fhir/sid/icd-10 |
| 32 | 225 | Condition | `Condition.code.coding` | O14.1 | Severe pre-eclampsia | http://hl7.org/fhir/sid/icd-10 |
| 33 | 226 | Condition | `Condition.code.coding` | O30.0 | Twin pregnancy | http://hl7.org/fhir/sid/icd-10 |
| 34 | 227 | Condition | `Condition.code.coding` | O68.9 | Labour and delivery complicated by fetal stress, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 35 | 228 | Condition | `Condition.code.coding` | O14.9 | Pre-eclampsia, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 36 | 229 | Condition | `Condition.code.coding` | O44.0 | Placenta praevia specified as without haemorrhage | http://hl7.org/fhir/sid/icd-10 |
| 37 | 230 | Condition | `Condition.code.coding` | O36.4 | Maternal care for intrauterine death | http://hl7.org/fhir/sid/icd-10 |
| 38 | 231 | Condition | `Condition.code.coding` | O13 | Gestational [pregnancy-induced] hypertension without signification proteinuria | http://hl7.org/fhir/sid/icd-10 |
| 39 | 232 | Condition | `Condition.code.coding` | O42.1 | Premature rupture of membranes, onset of labour after 24 hours | http://hl7.org/fhir/sid/icd-10 |
| 40 | 233 | Condition | `Condition.code.coding` | O48 | Prolonged pregnancy | http://hl7.org/fhir/sid/icd-10 |
| 41 | 234 | Condition | `Condition.code.coding` | O63.0 | Prolonged first stage of labour | http://hl7.org/fhir/sid/icd-10 |
| 42 | 235 | Condition | `Condition.code.coding` | O41.0 | Oligohydramnios | http://hl7.org/fhir/sid/icd-10 |
| 43 | 236 | Condition | `Condition.code.coding` | O70.9 | Perineal laceration during delivery, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 44 | 237 | Condition | `Condition.code.coding` | O36.5 | Maternal care for poor fetal growth | http://hl7.org/fhir/sid/icd-10 |
| 45 | 238 | Condition | `Condition.code.coding` | O99.4 | Diseases of the circulatory system complicating pregnancy, childbirth and the puerperium | http://hl7.org/fhir/sid/icd-10 |
| 46 | 239 | Condition | `Condition.code.coding` | O47.0 | False labour before 37 completed weeks of gestation | http://hl7.org/fhir/sid/icd-10 |
| 47 | 240 | Condition | `Condition.code.coding` | O60.1 | Preterm labour with preterm delivery | http://hl7.org/fhir/sid/icd-10 |
| 48 | 241 | Condition | `Condition.code.coding` | O14.0 | Moderate pre-eclampsia | http://hl7.org/fhir/sid/icd-10 |
| 49 | 250 | Condition | `Condition.code.coding` | O61.0 | Failed medical induction of labour | http://hl7.org/fhir/sid/icd-10 |
| 50 | 251 | Condition | `Condition.code.coding` | O64.4 | Obstructed labour due to shoulder presentation | http://hl7.org/fhir/sid/icd-10 |
| 51 | 252 | Condition | `Condition.code.coding` | O42.0 | Premature rupture of membranes, onset of labour within 24 hours | http://hl7.org/fhir/sid/icd-10 |
| 52 | 253 | Condition | `Condition.code.coding` | O33.0 | Maternal care for disproportion due to deformity of maternal pelvic bones | http://hl7.org/fhir/sid/icd-10 |
| 53 | 254 | Condition | `Condition.code.coding` | O34.2 | Maternal care due to uterine scar from previous surgery | http://hl7.org/fhir/sid/icd-10 |
| 54 | 255 | Condition | `Condition.code.coding` | O45.0 | Premature separation of placenta with coagulation defect | http://hl7.org/fhir/sid/icd-10 |
| 55 | 256 | Condition | `Condition.code.coding` | O33.9 | Maternal care for disproportion, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 56 | 257 | Condition | `Condition.code.coding` | O63.1 | Prolonged second stage of labour | http://hl7.org/fhir/sid/icd-10 |
| 57 | 258 | Condition | `Condition.code.coding` | O64.1 | Obstructed labour due to breech presentation | http://hl7.org/fhir/sid/icd-10 |
| 58 | 259 | Condition | `Condition.code.coding` | O14.1 | Severe pre-eclampsia | http://hl7.org/fhir/sid/icd-10 |
| 59 | 260 | Condition | `Condition.code.coding` | O30.0 | Twin pregnancy | http://hl7.org/fhir/sid/icd-10 |
| 60 | 261 | Condition | `Condition.code.coding` | O68.9 | Labour and delivery complicated by fetal stress, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 61 | 262 | Condition | `Condition.code.coding` | O14.9 | Pre-eclampsia, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 62 | 263 | Condition | `Condition.code.coding` | O44.0 | Placenta praevia specified as without haemorrhage | http://hl7.org/fhir/sid/icd-10 |
| 63 | 264 | Condition | `Condition.code.coding` | O36.4 | Maternal care for intrauterine death | http://hl7.org/fhir/sid/icd-10 |
| 64 | 265 | Condition | `Condition.code.coding` | O13 | Gestational [pregnancy-induced] hypertension without signification proteinuria | http://hl7.org/fhir/sid/icd-10 |
| 65 | 266 | Condition | `Condition.code.coding` | O42.1 | Premature rupture of membranes, onset of labour after 24 hours | http://hl7.org/fhir/sid/icd-10 |
| 66 | 267 | Condition | `Condition.code.coding` | O48 | Prolonged pregnancy | http://hl7.org/fhir/sid/icd-10 |
| 67 | 268 | Condition | `Condition.code.coding` | O63.0 | Prolonged first stage of labour | http://hl7.org/fhir/sid/icd-10 |
| 68 | 269 | Condition | `Condition.code.coding` | O41.0 | Oligohydramnios | http://hl7.org/fhir/sid/icd-10 |
| 69 | 270 | Condition | `Condition.code.coding` | O70.9 | Perineal laceration during delivery, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 70 | 271 | Condition | `Condition.code.coding` | O36.5 | Maternal care for poor fetal growth | http://hl7.org/fhir/sid/icd-10 |
| 71 | 272 | Condition | `Condition.code.coding` | O99.4 | Diseases of the circulatory system complicating pregnancy, childbirth and the puerperium | http://hl7.org/fhir/sid/icd-10 |
| 72 | 273 | Condition | `Condition.code.coding` | O47.0 | False labour before 37 completed weeks of gestation | http://hl7.org/fhir/sid/icd-10 |
| 73 | 274 | Condition | `Condition.code.coding` | O60.1 | Preterm labour with preterm delivery | http://hl7.org/fhir/sid/icd-10 |
| 74 | 275 | Condition | `Condition.code.coding` | O14.0 | Moderate pre-eclampsia | http://hl7.org/fhir/sid/icd-10 |
| 75 | 284 | Condition | `Condition.code.coding` | O42 | Premature rupture of membranes | http://hl7.org/fhir/sid/icd-10 |
| 76 | 285 | Condition | `Condition.code.coding` | O22.4 | Haemorrhoids in pregnancy | http://hl7.org/fhir/sid/icd-10 |
| 77 | 286 | Condition | `Condition.code.coding` | O33.0 | Maternal care for disproportion due to deformity of maternal pelvic bones | http://hl7.org/fhir/sid/icd-10 |
| 78 | 287 | Condition | `Condition.code.coding` | O48 | Prolonged pregnancy | http://hl7.org/fhir/sid/icd-10 |
| 79 | 288 | Condition | `Condition.code.coding` | O64.4 | Obstructed labour due to shoulder presentation | http://hl7.org/fhir/sid/icd-10 |
| 80 | 289 | Condition | `Condition.code.coding` | O82.0 | Delivery by elective caesarean section | http://hl7.org/fhir/sid/icd-10 |
| 81 | 290 | Condition | `Condition.code.coding` | O13 | Gestational [pregnancy-induced] hypertension without signification proteinuria | http://hl7.org/fhir/sid/icd-10 |
| 82 | 291 | Condition | `Condition.code.coding` | Z30.1 | Insertion of (intrauterine) contraceptive device | http://hl7.org/fhir/sid/icd-10 |
| 83 | 292 | Condition | `Condition.code.coding` | O82.9 | Delivery by caesarean section, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 84 | 293 | Condition | `Condition.code.coding` | Z37.0 | Single live birth | http://hl7.org/fhir/sid/icd-10 |
| 85 | 294 | Condition | `Condition.code.coding` | O41.0 | Oligohydramnios | http://hl7.org/fhir/sid/icd-10 |
| 86 | 295 | Condition | `Condition.code.coding` | O99.8 | Other specified diseases and conditions complicating pregnancy, childbirth and the puerperium | http://hl7.org/fhir/sid/icd-10 |
| 87 | 296 | Condition | `Condition.code.coding` | O64.1 | Obstructed labour due to breech presentation | http://hl7.org/fhir/sid/icd-10 |
| 88 | 297 | Condition | `Condition.code.coding` | O69.1 | Labour and delivery complicated cord around neck, with compression | http://hl7.org/fhir/sid/icd-10 |
| 89 | 298 | Condition | `Condition.code.coding` | O60.1 | Preterm labour with preterm delivery | http://hl7.org/fhir/sid/icd-10 |
| 90 | 299 | Condition | `Condition.code.coding` | O11 | Pre-existing hypertensive disorder with superimposed proteinuria | http://hl7.org/fhir/sid/icd-10 |
| 91 | 300 | Condition | `Condition.code.coding` | O14.1 | Severe pre-eclampsia | http://hl7.org/fhir/sid/icd-10 |
| 92 | 301 | Condition | `Condition.code.coding` | O99.0 | Anaemia complicating pregnancy, childbirth and the puerperium | http://hl7.org/fhir/sid/icd-10 |
| 93 | 302 | Condition | `Condition.code.coding` | O63.0 | Prolonged first stage of labour | http://hl7.org/fhir/sid/icd-10 |
| 94 | 303 | Condition | `Condition.code.coding` | H52.1 | Myopia | http://hl7.org/fhir/sid/icd-10 |
| 95 | 305 | Condition | `Condition.code.coding` | O83.9 | Assisted single delivery, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 96 | 306 | Condition | `Condition.code.coding` | Z30.8 | Other contraceptive management | http://hl7.org/fhir/sid/icd-10 |
| 97 | 307 | Condition | `Condition.code.coding` | O73.0 | Retained placenta without haemorrhage | http://hl7.org/fhir/sid/icd-10 |
| 98 | 308 | Condition | `Condition.code.coding` | O99.5 | Diseases of the respiratory system complicating pregnancy, childbirth and the puerperium | http://hl7.org/fhir/sid/icd-10 |
| 99 | 309 | Condition | `Condition.code.coding` | R33 | Retention of urine | http://hl7.org/fhir/sid/icd-10 |
| 100 | 310 | Condition | `Condition.code.coding` | Z86.4 | Personal history of psychoactive substance abuse | http://hl7.org/fhir/sid/icd-10 |
| 101 | 311 | Condition | `Condition.code.coding` | O16 | Unspecified maternal hypertension | http://hl7.org/fhir/sid/icd-10 |
| 102 | 312 | Condition | `Condition.code.coding` | O80.0 | Spontaneous vertex delivery | http://hl7.org/fhir/sid/icd-10 |
| 103 | 313 | Condition | `Condition.code.coding` | O98.0 | Tuberculosis complicating pregnancy, childbirth and the puerperium | http://hl7.org/fhir/sid/icd-10 |
| 104 | 314 | Condition | `Condition.code.coding` | Z87.5 | Personal history complications of pregnancy, childbirth and the puerperium | http://hl7.org/fhir/sid/icd-10 |
| 105 | 315 | Condition | `Condition.code.coding` | O36.5 | Maternal care for poor fetal growth | http://hl7.org/fhir/sid/icd-10 |
| 106 | 316 | Condition | `Condition.code.coding` | O00 | Ectopic pregnancy | http://hl7.org/fhir/sid/icd-10 |
| 107 | 317 | Condition | `Condition.code.coding` | I49.9 | Cardiac arrhythmia, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 108 | 318 | Condition | `Condition.code.coding` | I49.3 | Ventricular premature depolarization | http://hl7.org/fhir/sid/icd-10 |
| 109 | 319 | Condition | `Condition.code.coding` | O24 | Diabetes mellitus in pregnancy | http://hl7.org/fhir/sid/icd-10 |
| 110 | 320 | Condition | `Condition.code.coding` | O14.9 | Pre-eclampsia, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 111 | 322 | Condition | `Condition.code.coding` | O81.4 | Vacuum extractor delivery | http://hl7.org/fhir/sid/icd-10 |
| 112 | 323 | Condition | `Condition.code.coding` | O63.1 | Prolonged second stage of labour | http://hl7.org/fhir/sid/icd-10 |
| 113 | 332 | Condition | `Condition.code.coding` | O42 | Premature rupture of membranes | http://hl7.org/fhir/sid/icd-10 |
| 114 | 333 | Condition | `Condition.code.coding` | O82.9 | Delivery by caesarean section, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 115 | 334 | Condition | `Condition.code.coding` | Z30.1 | Insertion of (intrauterine) contraceptive device | http://hl7.org/fhir/sid/icd-10 |
| 116 | 335 | Condition | `Condition.code.coding` | Z37.0 | Single live birth | http://hl7.org/fhir/sid/icd-10 |
| 117 | 336 | Condition | `Condition.code.coding` | O22.4 | Haemorrhoids in pregnancy | http://hl7.org/fhir/sid/icd-10 |
| 118 | 337 | Condition | `Condition.code.coding` | O60.1 | Preterm labour with preterm delivery | http://hl7.org/fhir/sid/icd-10 |
| 119 | 338 | Condition | `Condition.code.coding` | Z30.1 | Insertion of (intrauterine) contraceptive device | http://hl7.org/fhir/sid/icd-10 |
| 120 | 339 | Condition | `Condition.code.coding` | O33.0 | Maternal care for disproportion due to deformity of maternal pelvic bones | http://hl7.org/fhir/sid/icd-10 |
| 121 | 340 | Condition | `Condition.code.coding` | O82.1 | Delivery by emergency caesarean section | http://hl7.org/fhir/sid/icd-10 |
| 122 | 341 | Condition | `Condition.code.coding` | O48 | Prolonged pregnancy | http://hl7.org/fhir/sid/icd-10 |
| 123 | 342 | Condition | `Condition.code.coding` | O98.1 | Syphilis complicating pregnancy, childbirth and the puerperium | http://hl7.org/fhir/sid/icd-10 |
| 124 | 343 | Condition | `Condition.code.coding` | A53.9 | Syphilis, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 125 | 344 | Condition | `Condition.code.coding` | O40 | Polyhydramnios | http://hl7.org/fhir/sid/icd-10 |
| 126 | 345 | Condition | `Condition.code.coding` | O64.4 | Obstructed labour due to shoulder presentation | http://hl7.org/fhir/sid/icd-10 |
| 127 | 346 | Condition | `Condition.code.coding` | O82.0 | Delivery by elective caesarean section | http://hl7.org/fhir/sid/icd-10 |
| 128 | 347 | Condition | `Condition.code.coding` | O34.2 | Maternal care due to uterine scar from previous surgery | http://hl7.org/fhir/sid/icd-10 |
| 129 | 348 | Condition | `Condition.code.coding` | O13 | Gestational [pregnancy-induced] hypertension without signification proteinuria | http://hl7.org/fhir/sid/icd-10 |
| 130 | 349 | Condition | `Condition.code.coding` | O99.0 | Anaemia complicating pregnancy, childbirth and the puerperium | http://hl7.org/fhir/sid/icd-10 |
| 131 | 350 | Condition | `Condition.code.coding` | D64.9 | Anaemia, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 132 | 351 | Condition | `Condition.code.coding` | Z30.2 | Sterilization | http://hl7.org/fhir/sid/icd-10 |
| 133 | 352 | Condition | `Condition.code.coding` | O44.0 | Placenta praevia specified as without haemorrhage | http://hl7.org/fhir/sid/icd-10 |
| 134 | 353 | Condition | `Condition.code.coding` | Z30.8 | Other contraceptive management | http://hl7.org/fhir/sid/icd-10 |
| 135 | 354 | Condition | `Condition.code.coding` | O30.0 | Twin pregnancy | http://hl7.org/fhir/sid/icd-10 |
| 136 | 355 | Condition | `Condition.code.coding` | Z37.2 | Twins, both liveborn | http://hl7.org/fhir/sid/icd-10 |
| 137 | 356 | Condition | `Condition.code.coding` | O14.1 | Severe pre-eclampsia | http://hl7.org/fhir/sid/icd-10 |
| 138 | 357 | Condition | `Condition.code.coding` | Z86.1 | Personal history of infectious and parasitic diseases | http://hl7.org/fhir/sid/icd-10 |
| 139 | 358 | Condition | `Condition.code.coding` | O41.0 | Oligohydramnios | http://hl7.org/fhir/sid/icd-10 |
| 140 | 359 | Condition | `Condition.code.coding` | K56.0 | Paralytic ileus | http://hl7.org/fhir/sid/icd-10 |
| 141 | 360 | Condition | `Condition.code.coding` | O99.6 | Diseases of the digestive system complicating pregnancy, childbirth and the puerperium | http://hl7.org/fhir/sid/icd-10 |
| 142 | 361 | Condition | `Condition.code.coding` | R00.0 | Tachycardia, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 143 | 362 | Condition | `Condition.code.coding` | O16 | Unspecified maternal hypertension | http://hl7.org/fhir/sid/icd-10 |
| 144 | 363 | Condition | `Condition.code.coding` | O31 | Complications specific to multiple gestation | http://hl7.org/fhir/sid/icd-10 |
| 145 | 364 | Condition | `Condition.code.coding` | O99.8 | Other specified diseases and conditions complicating pregnancy, childbirth and the puerperium | http://hl7.org/fhir/sid/icd-10 |
| 146 | 365 | Condition | `Condition.code.coding` | H52.1 | Myopia | http://hl7.org/fhir/sid/icd-10 |
| 147 | 366 | Condition | `Condition.code.coding` | O10.0 | Pre-existing essential hypertension complicating pregnancy, childbirth and the puerperium | http://hl7.org/fhir/sid/icd-10 |
| 148 | 367 | Condition | `Condition.code.coding` | O64.1 | Obstructed labour due to breech presentation | http://hl7.org/fhir/sid/icd-10 |
| 149 | 368 | Condition | `Condition.code.coding` | O98.4 | Viral hepatitis complicating pregnancy, childbirth and the puerperium | http://hl7.org/fhir/sid/icd-10 |
| 150 | 369 | Condition | `Condition.code.coding` | O63.0 | Prolonged first stage of labour | http://hl7.org/fhir/sid/icd-10 |
| 151 | 370 | Condition | `Condition.code.coding` | O69.1 | Labour and delivery complicated cord around neck, with compression | http://hl7.org/fhir/sid/icd-10 |
| 152 | 371 | Condition | `Condition.code.coding` | O11 | Pre-existing hypertensive disorder with superimposed proteinuria | http://hl7.org/fhir/sid/icd-10 |
| 153 | 372 | Condition | `Condition.code.coding` | O24.9 | Diabetes mellitus in pregnancy, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 154 | 373 | Condition | `Condition.code.coding` | O14.0 | Moderate pre-eclampsia | http://hl7.org/fhir/sid/icd-10 |
| 155 | 374 | Condition | `Condition.code.coding` | H44.2 | Degenerative myopia | http://hl7.org/fhir/sid/icd-10 |
| 156 | 375 | Condition | `Condition.code.coding` | N83.2 | Other and unspecified ovarian cysts | http://hl7.org/fhir/sid/icd-10 |
| 157 | 376 | Condition | `Condition.code.coding` | O82.1 | Delivery by emergency caesarean section | http://hl7.org/fhir/sid/icd-10 |
| 158 | 377 | Condition | `Condition.code.coding` | D56.9 | Thalassaemia, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 159 | 378 | Condition | `Condition.code.coding` | D56.9 | Thalassaemia, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 160 | 379 | Condition | `Condition.code.coding` | O42.1 | Premature rupture of membranes, onset of labour after 24 hours | http://hl7.org/fhir/sid/icd-10 |
| 161 | 380 | Condition | `Condition.code.coding` | O63.0 | Prolonged first stage of labour | http://hl7.org/fhir/sid/icd-10 |
| 162 | 381 | Condition | `Condition.code.coding` | O68.9 | Labour and delivery complicated by fetal stress, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 163 | 382 | Condition | `Condition.code.coding` | O83.9 | Assisted single delivery, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 164 | 383 | Condition | `Condition.code.coding` | O80.0 | Spontaneous vertex delivery | http://hl7.org/fhir/sid/icd-10 |
| 165 | 384 | Condition | `Condition.code.coding` | O73.0 | Retained placenta without haemorrhage | http://hl7.org/fhir/sid/icd-10 |
| 166 | 385 | Condition | `Condition.code.coding` | O63.1 | Prolonged second stage of labour | http://hl7.org/fhir/sid/icd-10 |
| 167 | 386 | Condition | `Condition.code.coding` | O99.5 | Diseases of the respiratory system complicating pregnancy, childbirth and the puerperium | http://hl7.org/fhir/sid/icd-10 |
| 168 | 387 | Condition | `Condition.code.coding` | J45.9 | Asthma, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 169 | 388 | Condition | `Condition.code.coding` | R33 | Retention of urine | http://hl7.org/fhir/sid/icd-10 |
| 170 | 389 | Condition | `Condition.code.coding` | Z86.4 | Personal history of psychoactive substance abuse | http://hl7.org/fhir/sid/icd-10 |
| 171 | 390 | Condition | `Condition.code.coding` | D69.6 | Thrombocytopenia, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 172 | 391 | Condition | `Condition.code.coding` | O99.1 | Other diseases of the blood and blood-forming organs and certain disorders involving the immune mechanism complicating pregnancy, childbirth and the puerperium | http://hl7.org/fhir/sid/icd-10 |
| 173 | 392 | Condition | `Condition.code.coding` | O98.0 | Tuberculosis complicating pregnancy, childbirth and the puerperium | http://hl7.org/fhir/sid/icd-10 |
| 174 | 393 | Condition | `Condition.code.coding` | A18.8 | Tuberculosis of other specified organs | http://hl7.org/fhir/sid/icd-10 |
| 175 | 394 | Condition | `Condition.code.coding` | Z87.5 | Personal history complications of pregnancy, childbirth and the puerperium | http://hl7.org/fhir/sid/icd-10 |
| 176 | 395 | Condition | `Condition.code.coding` | O72.1 | Other immediate postpartum haemorrhage | http://hl7.org/fhir/sid/icd-10 |
| 177 | 396 | Condition | `Condition.code.coding` | O71.7 | Obstetric haematoma of pelvis | http://hl7.org/fhir/sid/icd-10 |
| 178 | 397 | Condition | `Condition.code.coding` | O36.5 | Maternal care for poor fetal growth | http://hl7.org/fhir/sid/icd-10 |
| 179 | 398 | Condition | `Condition.code.coding` | O00.9 | Ectopic pregnancy, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 180 | 399 | Condition | `Condition.code.coding` | I49.9 | Cardiac arrhythmia, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 181 | 400 | Condition | `Condition.code.coding` | I49.3 | Ventricular premature depolarization | http://hl7.org/fhir/sid/icd-10 |
| 182 | 401 | Condition | `Condition.code.coding` | O99.4 | Diseases of the circulatory system complicating pregnancy, childbirth and the puerperium | http://hl7.org/fhir/sid/icd-10 |
| 183 | 402 | Condition | `Condition.code.coding` | I25.9 | Chronic ischaemic heart disease, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 184 | 403 | Condition | `Condition.code.coding` | O71.3 | Obstetric laceration of cervix | http://hl7.org/fhir/sid/icd-10 |
| 185 | 404 | Condition | `Condition.code.coding` | O81.4 | Vacuum extractor delivery | http://hl7.org/fhir/sid/icd-10 |
| 186 | 405 | Condition | `Condition.code.coding` | O46.8 | Other antepartum haemorrhage | http://hl7.org/fhir/sid/icd-10 |
| 187 | 416 | Procedure | `Procedure.code.coding` | 74.4 | Cesarean section of other specified type | http://hl7.org/fhir/sid/icd-9-cm |
| 188 | 418 | Procedure | `Procedure.code.coding` | 69.7 | Insertion of intrauterine contraceptive device | http://hl7.org/fhir/sid/icd-9-cm |
| 189 | 420 | Procedure | `Procedure.code.coding` | 73.4 | Medical induction of labor | http://hl7.org/fhir/sid/icd-9-cm |
| 190 | 422 | Procedure | `Procedure.code.coding` | 90.59 | Microscopic examination of blood, Other microscopic examination | http://hl7.org/fhir/sid/icd-9-cm |
| 191 | 424 | Procedure | `Procedure.code.coding` | 88.78 | Diagnostic ultrasound of gravid uterus | http://hl7.org/fhir/sid/icd-9-cm |
| 192 | 426 | Procedure | `Procedure.code.coding` | 75.32 | Fetal EKG (scalp) | http://hl7.org/fhir/sid/icd-9-cm |
| 193 | 428 | Procedure | `Procedure.code.coding` | 91.39 | Microscopic examination of specimen from bladder, urethra, prostate,seminal vesicle, perivesical tissue, and of urine and semen, Other microscopic examination | http://hl7.org/fhir/sid/icd-9-cm |
| 194 | 430 | Procedure | `Procedure.code.coding` | 89.52 | Electrocardiogram | http://hl7.org/fhir/sid/icd-9-cm |
| 195 | 432 | Procedure | `Procedure.code.coding` | 66.39 | Other bilateral destruction or occlusion of fallopian tubes | http://hl7.org/fhir/sid/icd-9-cm |
| 196 | 434 | Procedure | `Procedure.code.coding` | 99.04 | Transfusion of packed cells | http://hl7.org/fhir/sid/icd-9-cm |
| 197 | 436 | Procedure | `Procedure.code.coding` | 69.7 | Insertion of intrauterine contraceptive device | http://hl7.org/fhir/sid/icd-9-cm |
| 198 | 438 | Procedure | `Procedure.code.coding` | 90.52 | Microscopic examination of blood, Culture | http://hl7.org/fhir/sid/icd-9-cm |
| 199 | 440 | Procedure | `Procedure.code.coding` | 88.09 | Other soft tissue x-ray of abdominal wall | http://hl7.org/fhir/sid/icd-9-cm |
| 200 | 442 | Procedure | `Procedure.code.coding` | 97.71 | Removal of intrauterine contraceptive device | http://hl7.org/fhir/sid/icd-9-cm |
| 201 | 444 | Procedure | `Procedure.code.coding` | 65.29 | Other local excision or destruction of ovary | http://hl7.org/fhir/sid/icd-9-cm |
| 202 | 446 | Procedure | `Procedure.code.coding` | 69.02 | Dilation and curettage following delivery or abortion | http://hl7.org/fhir/sid/icd-9-cm |
| 203 | 448 | Procedure | `Procedure.code.coding` | 57.94 | Insertion of indwelling urinary catheter | http://hl7.org/fhir/sid/icd-9-cm |
| 204 | 450 | Procedure | `Procedure.code.coding` | 70.79 | Other repair of vagina | http://hl7.org/fhir/sid/icd-9-cm |
| 205 | 452 | Procedure | `Procedure.code.coding` | 75.69 | Repair of other current obstetric laceration | http://hl7.org/fhir/sid/icd-9-cm |
| 206 | 454 | Procedure | `Procedure.code.coding` | 73.59 | Other manually assisted delivery | http://hl7.org/fhir/sid/icd-9-cm |
| 207 | 456 | Procedure | `Procedure.code.coding` | 73.59 | Other manually assisted delivery | http://hl7.org/fhir/sid/icd-9-cm |
| 208 | 458 | Procedure | `Procedure.code.coding` | 75.51 | Repair of current obstetric laceration of cervix | http://hl7.org/fhir/sid/icd-9-cm |
| 209 | 460 | Procedure | `Procedure.code.coding` | 75.69 | Repair of other current obstetric laceration | http://hl7.org/fhir/sid/icd-9-cm |
| 210 | 471 | Procedure | `Procedure.code.coding` | 74.4 | Cesarean section of other specified type | http://hl7.org/fhir/sid/icd-9-cm |
| 211 | 473 | Procedure | `Procedure.code.coding` | 69.7 | Insertion of intrauterine contraceptive device | http://hl7.org/fhir/sid/icd-9-cm |
| 212 | 475 | Procedure | `Procedure.code.coding` | 73.4 | Medical induction of labor | http://hl7.org/fhir/sid/icd-9-cm |
| 213 | 477 | Procedure | `Procedure.code.coding` | 90.59 | Microscopic examination of blood, Other microscopic examination | http://hl7.org/fhir/sid/icd-9-cm |
| 214 | 479 | Procedure | `Procedure.code.coding` | 88.78 | Diagnostic ultrasound of gravid uterus | http://hl7.org/fhir/sid/icd-9-cm |
| 215 | 481 | Procedure | `Procedure.code.coding` | 90.95 | Microscopic examination of specimen from lower gastrointestinal tract and of stool, Toxicology | http://hl7.org/fhir/sid/icd-9-cm |
| 216 | 483 | Procedure | `Procedure.code.coding` | 75.32 | Fetal EKG (scalp) | http://hl7.org/fhir/sid/icd-9-cm |
| 217 | 485 | Procedure | `Procedure.code.coding` | 89.52 | Electrocardiogram | http://hl7.org/fhir/sid/icd-9-cm |
| 218 | 487 | Procedure | `Procedure.code.coding` | 91.3 | Microscopic examination of specimen from bladder, urethra, prostate,seminal vesicle, perivesical tissue, and of urine and semen | http://hl7.org/fhir/sid/icd-9-cm |
| 219 | 489 | Procedure | `Procedure.code.coding` | 99.04 | Transfusion of packed cells | http://hl7.org/fhir/sid/icd-9-cm |
| 220 | 491 | Procedure | `Procedure.code.coding` | 66.39 | Other bilateral destruction or occlusion of fallopian tubes | http://hl7.org/fhir/sid/icd-9-cm |
| 221 | 493 | Procedure | `Procedure.code.coding` | 87.44 | Routine chest x-ray, so described | http://hl7.org/fhir/sid/icd-9-cm |
| 222 | 495 | Procedure | `Procedure.code.coding` | 90.52 | Microscopic examination of blood, Culture | http://hl7.org/fhir/sid/icd-9-cm |
| 223 | 497 | Procedure | `Procedure.code.coding` | 88.09 | Other soft tissue x-ray of abdominal wall | http://hl7.org/fhir/sid/icd-9-cm |
| 224 | 499 | Procedure | `Procedure.code.coding` | 65.29 | Other local excision or destruction of ovary | http://hl7.org/fhir/sid/icd-9-cm |
| 225 | 501 | Procedure | `Procedure.code.coding` | 97.71 | Removal of intrauterine contraceptive device | http://hl7.org/fhir/sid/icd-9-cm |
| 226 | 503 | Procedure | `Procedure.code.coding` | 89.52 | Electrocardiogram | http://hl7.org/fhir/sid/icd-9-cm |
| 227 | 505 | Procedure | `Procedure.code.coding` | 97.71 | Removal of intrauterine contraceptive device | http://hl7.org/fhir/sid/icd-9-cm |
| 228 | 507 | Procedure | `Procedure.code.coding` | 73.59 | Other manually assisted delivery | http://hl7.org/fhir/sid/icd-9-cm |
| 229 | 509 | Procedure | `Procedure.code.coding` | 69.02 | Dilation and curettage following delivery or abortion | http://hl7.org/fhir/sid/icd-9-cm |
| 230 | 511 | Procedure | `Procedure.code.coding` | 75.51 | Repair of current obstetric laceration of cervix | http://hl7.org/fhir/sid/icd-9-cm |
| 231 | 513 | Procedure | `Procedure.code.coding` | 73.6 | Episiotomy | http://hl7.org/fhir/sid/icd-9-cm |
| 232 | 515 | Procedure | `Procedure.code.coding` | 75.69 | Repair of other current obstetric laceration | http://hl7.org/fhir/sid/icd-9-cm |
| 233 | 517 | Procedure | `Procedure.code.coding` | 72.79 | Other vacuum extraction | http://hl7.org/fhir/sid/icd-9-cm |
| 234 | 519 | Procedure | `Procedure.code.coding` | 75.92 | Evacuation of other hematoma of vulva or vagina | http://hl7.org/fhir/sid/icd-9-cm |
| 235 | 522 | Condition | `Condition.code.coding` | 268910001.0 | Patient's condition improved | http://snomed.info/sct |
| 236 | 523 | Condition | `Condition.code.coding` | 371001000.0 | Patient cured | http://snomed.info/sct |
| 237 | 532 | Observation | `Observation.code.coding` | 183797002.0 | Duration of inpatient stay | http://snomed.info/sct |
| 238 | 544 | Observation | `Observation.code.coding` | SP000811 | Jalur Masuk Rawat Inap | http://terminology.kemkes.go.id/sp |
| 239 | 545 | Observation | `Observation.valueCodeableConcept.coding` | 225728007.0 | Accident and Emergency department | http://snomed.info/sct |
| 240 | 546 | Observation | `Observation.valueCodeableConcept.coding` | 309942007.0 | Obstetrics and gynecology department | http://snomed.info/sct |
| 241 | 547 | Observation | `Observation.valueCodeableConcept.coding` | 1363029004.0 | Hospital observation unit | http://snomed.info/sct |
| 242 | 548 | Observation | `Observation.valueCodeableConcept.coding` | 405606005.0 | Labor and delivery unit | http://snomed.info/sct |
| 243 | 558 | Observation | `Observation.code.coding` | 184061005.0 | Patient registration status | http://snomed.info/sct |
| 244 | 559 | Observation | `Observation.valueCodeableConcept.coding` | SP000812 | Pasien Baru | http://terminology.kemkes.go.id/sp |
| 245 | 560 | Observation | `Observation.valueCodeableConcept.coding` | SP000813 | Pasien Lama | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://hl7.org/fhir/sid/icd-10 | 164 |
| http://hl7.org/fhir/sid/icd-9-cm | 48 |
| http://snomed.info/sct | 20 |
| http://terminology.kemkes.go.id/sp | 12 |
| http://loinc.org | 1 |
| **Total** | **245** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 30 | – | Faskes yang melayani INC | Organization | `Organization.name` |
| 70 | – | Ruang | Location | `Location.identifier` |
| 579 | – | NO | – | `` |
| 580 | – | TANGGAL | – | `` |
| 581 | – | NOMR | – | `` |
