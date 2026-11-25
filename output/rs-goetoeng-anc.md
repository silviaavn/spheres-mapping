# Output Form: SIM RS Goetoeng ANC

Sumber: `mapping/phdt-data-dictionary-rs-goetoeng-anc.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-rs-goetoeng-anc.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 106 |
| Code (`jumlah code` = 1) | 111 |
| Code unik (code + CodeSystem) | 91 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 22 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–24 | Patient | – | – | _Nama Ibu_ → `Patient.name.text` (2, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (7, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (8, tanpa BQ)<br>_Alamat Domisili_ → `Patient.address.use` (9, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (15, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (18, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.extension.valueCode` (21, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.extension.valueCode` (24, tanpa BQ) |
| 2 | 92–106 | Encounter | – | – | _DPJP_ → `Encounter.participant.individual.display` (100, tanpa BQ)<br>_Tanggal Kunjungan_ → `Encounter.period.start` (101, tanpa BQ)<br>_Unit Ruangan_ → `Encounter.location.location.display` (104, tanpa BQ)<br>_Asal Pasien_ → `Encounter.hospitalization.admitSource.coding` (114, tanpa BQ)<br>_Cara Pulang_ → `Encounter.hospitalization.dischargeDisposition.coding` (127, tanpa BQ) |
| 3 | 107–113 | Condition | 134435003.0 | Routine antenatal care | – |
| 4 | 132–144 | ServiceRequest | – | – | _Cara Pulang_ → `ServiceRequest.category` (132, tanpa BQ) |
| 5 | 145–152 | Coverage | – | – | _Cara Bayar_ → `Coverage.identifier` (145, tanpa BQ) |
| 6 | 153–170 | Observation | 424144002.0 | Current chronological age | _Umur_ → `Observation.valueQuantity.value` (156, tanpa BQ) |
| 7 | 171–179 | Condition | – | – | _Diagnosis_ → `Condition.clinicalStatus.coding` (171, tanpa BQ) |
| 8 | 180–199 | Procedure | – | – | _Prosedur_ → `Procedure.code.coding` (180, tanpa BQ)<br>_Tindakan_ → `Procedure.status` (190, tanpa BQ) |
| 9 | 200–202 | Procedure | SP000821 | Konsultasi Medis | – |
| 10 | 203–205 | Procedure | 88.78 | Diagnostic ultrasound of gravid uterus | – |
| 11 | 206–208 | Procedure | 34608000.0 | Alanine aminotransferase measurement | – |
| 12 | 209–211 | Procedure | 86228006.0 | Uric acid measurement | – |
| 13 | 212–213 | Procedure | 70901006.0 | Creatinine measurement | – |
| 14 | 214–216 | Procedure | 27171005.0 | Urinalysis | – |
| 15 | 217–218 | Procedure | 105010007.0 | Urea measurement | – |
| 16 | 219–221 | Procedure | 396550006.0 | Blood test | – |
| 17 | 222–223 | Procedure | 45896001.0 | Aspartate aminotransferase measurement | – |
| 18 | 224–226 | Procedure | 165566005.0 | Whole blood clotting time procedure | – |
| 19 | 227–228 | Procedure | 40675008.0 | Serologic test for syphilis | – |
| 20 | 229–230 | Procedure | 269826008.0 | ABO blood grouping | – |
| 21 | 231–233 | Procedure | 27171005.0 | Urinalysis | – |
| 22 | 234–236 | Procedure | 271061004.0 | Random blood glucose measurement | – |
| 23 | 237–238 | Procedure | 104176001.0 | HIV antibody test | – |
| 24 | 239–240 | Procedure | 72406003.0 | Bleeding time | – |
| 25 | 241–242 | Procedure | 47758006.0 | Hepatitis B surface antigen measurement | – |
| 26 | 243–244 | Procedure | 43396009.0 | Hemoglobin A1c measurement | – |
| 27 | 245–246 | Procedure | 14740000.0 | Triglycerides measurement | – |
| 28 | 247–248 | Procedure | 22644003.0 | Low density lipoprotein measurement | – |
| 29 | 249–250 | Procedure | 17888004.0 | High density lipoprotein measurement | – |
| 30 | 251–255 | Procedure | 121868005.0 | Total cholesterol measurement | – |
| 31 | 256–258 | Procedure | 410136007.0 | Nursing coordination management | – |
| 32 | 259–260 | Procedure | 410175003.0 | Dietary regime management | – |
| 33 | 261–263 | Procedure | SP000824 | Tindakan Non Operatif Non Medis | – |
| 34 | 264–266 | Procedure | SP000824 | Tindakan Non Operatif Non Medis | – |
| 35 | 267–269 | Procedure | 182810003.0 | Intensive care monitoring | – |
| 36 | 270–273 | Procedure | 424029000.0 | Personal hygiene case management | – |
| 37 | 274–275 | Procedure | 410188000.0 | Taking patient vital signs assessment | – |
| 38 | 276–277 | Procedure | 237433000.0 | Breast care procedure | – |
| 39 | 278–279 | Procedure | 386372009.0 | Nutrition management | – |
| 40 | 280–282 | Procedure | 18949003.0 | Change of dressing | – |
| 41 | 283–284 | Procedure | 57.94 | Insertion of indwelling urinary catheter | – |
| 42 | 285–286 | Procedure | 38.93 | Venous catheterization, not elsewhere classified | – |
| 43 | 287–288 | Procedure | 96.39 | Other transanal enema | – |
| 44 | 289–291 | Procedure | 99.1 | Injection or infusion of therapeutic or prophylactic substance | – |
| 45 | 292–293 | Procedure | 18949003.0 | Change of dressing | – |
| 46 | 294–295 | Procedure | SP000823 | Perawatan Luka Operasi | – |
| 47 | 296–297 | Procedure | 386761002.0 | Local anesthesia | – |
| 48 | 298–299 | Procedure | 69.7 | Insertion of intrauterine contraceptive device | – |
| 49 | 300–301 | Procedure | SP000819 | Pemberian Anastesi Operatif Besar Khusus | – |
| 50 | 302–303 | Procedure | SP000825 | Operatif Besar Khusus | – |
| 51 | 304–305 | Procedure | SP000820 | Pengawasan Pre-Eklampsia Berat | – |
| 52 | 306–308 | Procedure | 48403009.0 | Insertion of infusion pump | – |
| 53 | 309–310 | Procedure | 43060002.0 | Intravenous injection | – |
| 54 | 311–312 | Procedure | 313006001.0 | Doppler ultrasonography of fetal heart for heart sounds | – |
| 55 | 313–314 | Procedure | 765172009.0 | Doppler ultrasound | – |
| 56 | 315–317 | Procedure | 410188000.0 | Taking patient vital signs assessment | – |
| 57 | 318–320 | Procedure | 441689006.0 | Measurement of total hemoglobin concentration | – |
| 58 | 321–324 | Procedure | 424029000.0 | Personal hygiene case management | – |
| 59 | 325–326 | Procedure | 234083009.0 | Venous puncture | – |
| 60 | 327–329 | Procedure | 133858001.0 | Preoperative procedure | – |
| 61 | 330–331 | Procedure | 99.04 | Transfusion of packed cells | – |
| 62 | 332–333 | Procedure | 5447007.0 | Transfusion | – |
| 63 | 334–336 | Procedure | 424029000.0 | Personal hygiene case management | – |
| 64 | 337–338 | Procedure | 89.52 | Electrocardiogram | – |
| 65 | 339–340 | Procedure | 269826008.0 | ABO blood grouping | – |
| 66 | 341–342 | Procedure | 165745004.0 | Rhesus blood grouping | – |
| 67 | 343–344 | Procedure | 43060002.0 | Intravenous injection | – |
| 68 | 345–346 | Procedure | 386432004.0 | Shock management | – |
| 69 | 347–348 | Procedure | 386219007.0 | Control of hemorrhage in postpartum uterus | – |
| 70 | 349–351 | Procedure | 116859006.0 | Transfusion of blood product | – |
| 71 | 352–353 | Procedure | 99.1 | Injection or infusion of therapeutic or prophylactic substance | – |
| 72 | 354–355 | Procedure | 26758005.0 | Albumin measurement | – |
| 73 | 356–358 | Procedure | 99.60 | Cardiopulmonary resuscitation, not otherwise specified | – |
| 74 | 359–361 | Procedure | 278297009.0 | Blood gas analysis | – |
| 75 | 362–363 | Procedure | 96.07 | Insertion of other (naso-)gastric tube | – |
| 76 | 364–366 | Procedure | 38.93 | Venous catheterization, not elsewhere classified | – |
| 77 | 367–369 | Procedure | 96.6 | Enteral infusion of concentrated nutritional substances | – |
| 78 | 370–371 | Procedure | 173830003.0 | Gastric lavage | – |
| 79 | 372–373 | Procedure | 57931004.0 | Puncture of artery | – |
| 80 | 374–375 | Procedure | 234083009.0 | Venous puncture | – |
| 81 | 376–378 | Procedure | 51241000.0 | Control of hemorrhage | – |
| 82 | 379–381 | Procedure | 271061004.0 | Random blood glucose measurement | – |
| 83 | 382–383 | Procedure | 97.37 | Removal of tracheostomy tube | – |
| 84 | 384–386 | Procedure | SP000826 | Tindakan Non Medis | – |
| 85 | 387–388 | Procedure | 276026009.0 | Fluid balance regulation | – |
| 86 | 389–391 | Procedure | 182810003.0 | Intensive care monitoring | – |
| 87 | 392–393 | Procedure | 104177005.0 | Electrolyte measurement | – |
| 88 | 394–396 | Procedure | 87.44 | Routine chest x-ray, so described | – |
| 89 | 397–399 | Procedure | 96.04 | Insertion of endotracheal tube | – |
| 90 | 400–401 | Procedure | 226007004.0 | Post-surgical wound care | – |
| 91 | 402–404 | Procedure | 48403009.0 | Insertion of infusion pump | – |
| 92 | 405–407 | Procedure | SP000827 | Pemasangan dan Monitoring Syringe Pump | – |
| 93 | 408–412 | Procedure | 410136007.0 | Nursing coordination management | – |
| 94 | 413–417 | Procedure | 43060002.0 | Intravenous injection | – |
| 95 | 418–423 | Procedure | SP000822 | Konsultasi Non Medis | – |
| 96 | 424–425 | Procedure | 360362007.0 | Suture of laceration of perineum | – |
| 97 | 426–427 | Procedure | 73.1 | Other surgical induction of labor | – |
| 98 | 428–429 | Procedure | 309878003.0 | Exploration of uterine cavity | – |
| 99 | 430–431 | Procedure | SP000818 | Pemasangan IUD/ Implan | – |
| 100 | 432–436 | Procedure | SP000821 | Konsultasi Medis | – |
| 101 | 437–439 | Procedure | 387672006.0 | Cardiotochogram | – |
| 102 | 440–441 | Procedure | 89.52 | Electrocardiogram | – |
| 103 | 442–444 | Procedure | SP000821 | Konsultasi Medis | – |
| 104 | 445–446 | Procedure | SP000826 | Tindakan Non Medis | – |
| 105 | 448–459 | Observation | SP000815 | Jenis Kasus Pasien | _Jenis Kasus_ → `Observation.valueCodeableConcept.coding` (451, tanpa BQ) |
| 106 | 460–471 | Observation | 184061005.0 | Patient registration status | _Status Pasien_ → `Observation.valueCodeableConcept.coding` (463, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Procedure | 97 |
| Observation | 3 |
| Condition | 2 |
| Patient | 1 |
| Encounter | 1 |
| ServiceRequest | 1 |
| Coverage | 1 |
| **Total** | **106** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 109 | Condition | `Condition.code.coding` | 134435003.0 | Routine antenatal care | http://snomed.info/sct |
| 2 | 114 | Encounter | `Encounter.hospitalization.admitSource.coding` | 1991000124105.0 | Referred by self | http://snomed.info/sct |
| 3 | 115 | Encounter | `Encounter.hospitalization.admitSource.coding` | other | Other | http://terminology.hl7.org/CodeSystem/admit-source |
| 4 | 116 | Encounter | `Encounter.hospitalization.admitSource.coding` | SP000117 | Rujukan dari Puskesmas | http://terminology.kemkes.go.id/sp |
| 5 | 136 | ServiceRequest | `ServiceRequest.code` | 185389009.0 | Follow-up visit | http://snomed.info/sct |
| 6 | 137 | ServiceRequest | `ServiceRequest.code` | 737481003.0 | Inpatient care management | http://snomed.info/sct |
| 7 | 155 | Observation | `Observation.code.coding` | 424144002.0 | Current chronological age | http://snomed.info/sct |
| 8 | 158 | Observation | `Observation.component.code.coding` | SP000020 | Umur Bulan | http://terminology.kemkes.go.id/sp |
| 9 | 161 | Observation | `Observation.component.code.coding` | SP000021 | Umur Hari | http://terminology.kemkes.go.id/sp |
| 10 | 200 | Procedure | `Procedure.code.coding` | SP000821 | Konsultasi Medis | http://terminology.kemkes.go.id/sp |
| 11 | 203 | Procedure | `Procedure.code.coding` | 88.78 | Diagnostic ultrasound of gravid uterus | http://hl7.org/fhir/sid/icd-9-cm |
| 12 | 206 | Procedure | `Procedure.code.coding` | 34608000.0 | Alanine aminotransferase measurement | http://snomed.info/sct |
| 13 | 209 | Procedure | `Procedure.code.coding` | 86228006.0 | Uric acid measurement | http://snomed.info/sct |
| 14 | 212 | Procedure | `Procedure.code.coding` | 70901006.0 | Creatinine measurement | http://snomed.info/sct |
| 15 | 214 | Procedure | `Procedure.code.coding` | 27171005.0 | Urinalysis | http://snomed.info/sct |
| 16 | 217 | Procedure | `Procedure.code.coding` | 105010007.0 | Urea measurement | http://snomed.info/sct |
| 17 | 219 | Procedure | `Procedure.code.coding` | 396550006.0 | Blood test | http://snomed.info/sct |
| 18 | 222 | Procedure | `Procedure.code.coding` | 45896001.0 | Aspartate aminotransferase measurement | http://snomed.info/sct |
| 19 | 224 | Procedure | `Procedure.code.coding` | 165566005.0 | Whole blood clotting time procedure | http://snomed.info/sct |
| 20 | 227 | Procedure | `Procedure.code.coding` | 40675008.0 | Serologic test for syphilis | http://snomed.info/sct |
| 21 | 229 | Procedure | `Procedure.code.coding` | 269826008.0 | ABO blood grouping | http://snomed.info/sct |
| 22 | 231 | Procedure | `Procedure.code.coding` | 27171005.0 | Urinalysis | http://snomed.info/sct |
| 23 | 234 | Procedure | `Procedure.code.coding` | 271061004.0 | Random blood glucose measurement | http://snomed.info/sct |
| 24 | 237 | Procedure | `Procedure.code.coding` | 104176001.0 | HIV antibody test | http://snomed.info/sct |
| 25 | 239 | Procedure | `Procedure.code.coding` | 72406003.0 | Bleeding time | http://snomed.info/sct |
| 26 | 241 | Procedure | `Procedure.code.coding` | 47758006.0 | Hepatitis B surface antigen measurement | http://snomed.info/sct |
| 27 | 243 | Procedure | `Procedure.code.coding` | 43396009.0 | Hemoglobin A1c measurement | http://snomed.info/sct |
| 28 | 245 | Procedure | `Procedure.code.coding` | 14740000.0 | Triglycerides measurement | http://snomed.info/sct |
| 29 | 247 | Procedure | `Procedure.code.coding` | 22644003.0 | Low density lipoprotein measurement | http://snomed.info/sct |
| 30 | 249 | Procedure | `Procedure.code.coding` | 17888004.0 | High density lipoprotein measurement | http://snomed.info/sct |
| 31 | 251 | Procedure | `Procedure.code.coding` | 121868005.0 | Total cholesterol measurement | http://snomed.info/sct |
| 32 | 256 | Procedure | `Procedure.code.coding` | 410136007.0 | Nursing coordination management | http://snomed.info/sct |
| 33 | 259 | Procedure | `Procedure.code.coding` | 410175003.0 | Dietary regime management | http://snomed.info/sct |
| 34 | 261 | Procedure | `Procedure.code.coding` | SP000824 | Tindakan Non Operatif Non Medis | http://terminology.kemkes.go.id/sp |
| 35 | 264 | Procedure | `Procedure.code.coding` | SP000824 | Tindakan Non Operatif Non Medis | http://terminology.kemkes.go.id/sp |
| 36 | 267 | Procedure | `Procedure.code.coding` | 182810003.0 | Intensive care monitoring | http://snomed.info/sct |
| 37 | 270 | Procedure | `Procedure.code.coding` | 424029000.0 | Personal hygiene case management | http://snomed.info/sct |
| 38 | 274 | Procedure | `Procedure.code.coding` | 410188000.0 | Taking patient vital signs assessment | http://snomed.info/sct |
| 39 | 276 | Procedure | `Procedure.code.coding` | 237433000.0 | Breast care procedure | http://snomed.info/sct |
| 40 | 278 | Procedure | `Procedure.code.coding` | 386372009.0 | Nutrition management | http://snomed.info/sct |
| 41 | 280 | Procedure | `Procedure.code.coding` | 18949003.0 | Change of dressing | http://snomed.info/sct |
| 42 | 283 | Procedure | `Procedure.code.coding` | 57.94 | Insertion of indwelling urinary catheter | http://hl7.org/fhir/sid/icd-9-cm |
| 43 | 285 | Procedure | `Procedure.code.coding` | 38.93 | Venous catheterization, not elsewhere classified | http://hl7.org/fhir/sid/icd-9-cm |
| 44 | 287 | Procedure | `Procedure.code.coding` | 96.39 | Other transanal enema | http://hl7.org/fhir/sid/icd-9-cm |
| 45 | 289 | Procedure | `Procedure.code.coding` | 99.1 | Injection or infusion of therapeutic or prophylactic substance | http://hl7.org/fhir/sid/icd-9-cm |
| 46 | 292 | Procedure | `Procedure.code.coding` | 18949003.0 | Change of dressing | http://snomed.info/sct |
| 47 | 294 | Procedure | `Procedure.code.coding` | SP000823 | Perawatan Luka Operasi | http://terminology.kemkes.go.id/sp |
| 48 | 296 | Procedure | `Procedure.code.coding` | 386761002.0 | Local anesthesia | http://snomed.info/sct |
| 49 | 298 | Procedure | `Procedure.code.coding` | 69.7 | Insertion of intrauterine contraceptive device | http://hl7.org/fhir/sid/icd-9-cm |
| 50 | 300 | Procedure | `Procedure.code.coding` | SP000819 | Pemberian Anastesi Operatif Besar Khusus | http://terminology.kemkes.go.id/sp |
| 51 | 302 | Procedure | `Procedure.code.coding` | SP000825 | Operatif Besar Khusus | http://terminology.kemkes.go.id/sp |
| 52 | 304 | Procedure | `Procedure.code.coding` | SP000820 | Pengawasan Pre-Eklampsia Berat | http://terminology.kemkes.go.id/sp |
| 53 | 306 | Procedure | `Procedure.code.coding` | 48403009.0 | Insertion of infusion pump | http://snomed.info/sct |
| 54 | 309 | Procedure | `Procedure.code.coding` | 43060002.0 | Intravenous injection | http://snomed.info/sct |
| 55 | 311 | Procedure | `Procedure.code.coding` | 313006001.0 | Doppler ultrasonography of fetal heart for heart sounds | http://snomed.info/sct |
| 56 | 313 | Procedure | `Procedure.code.coding` | 765172009.0 | Doppler ultrasound | http://snomed.info/sct |
| 57 | 315 | Procedure | `Procedure.code.coding` | 410188000.0 | Taking patient vital signs assessment | http://snomed.info/sct |
| 58 | 318 | Procedure | `Procedure.code.coding` | 441689006.0 | Measurement of total hemoglobin concentration | http://snomed.info/sct |
| 59 | 321 | Procedure | `Procedure.code.coding` | 424029000.0 | Personal hygiene case management | http://snomed.info/sct |
| 60 | 325 | Procedure | `Procedure.code.coding` | 234083009.0 | Venous puncture | http://snomed.info/sct |
| 61 | 327 | Procedure | `Procedure.code.coding` | 133858001.0 | Preoperative procedure | http://snomed.info/sct |
| 62 | 330 | Procedure | `Procedure.code.coding` | 99.04 | Transfusion of packed cells | http://hl7.org/fhir/sid/icd-9-cm |
| 63 | 332 | Procedure | `Procedure.code.coding` | 5447007.0 | Transfusion | http://snomed.info/sct |
| 64 | 334 | Procedure | `Procedure.code.coding` | 424029000.0 | Personal hygiene case management | http://snomed.info/sct |
| 65 | 337 | Procedure | `Procedure.code.coding` | 89.52 | Electrocardiogram | http://hl7.org/fhir/sid/icd-9-cm |
| 66 | 339 | Procedure | `Procedure.code.coding` | 269826008.0 | ABO blood grouping | http://snomed.info/sct |
| 67 | 341 | Procedure | `Procedure.code.coding` | 165745004.0 | Rhesus blood grouping | http://snomed.info/sct |
| 68 | 343 | Procedure | `Procedure.code.coding` | 43060002.0 | Intravenous injection | http://snomed.info/sct |
| 69 | 345 | Procedure | `Procedure.code.coding` | 386432004.0 | Shock management | http://snomed.info/sct |
| 70 | 347 | Procedure | `Procedure.code.coding` | 386219007.0 | Control of hemorrhage in postpartum uterus | http://snomed.info/sct |
| 71 | 349 | Procedure | `Procedure.code.coding` | 116859006.0 | Transfusion of blood product | http://snomed.info/sct |
| 72 | 352 | Procedure | `Procedure.code.coding` | 99.1 | Injection or infusion of therapeutic or prophylactic substance | http://hl7.org/fhir/sid/icd-9-cm |
| 73 | 354 | Procedure | `Procedure.code.coding` | 26758005.0 | Albumin measurement | http://snomed.info/sct |
| 74 | 356 | Procedure | `Procedure.code.coding` | 99.60 | Cardiopulmonary resuscitation, not otherwise specified | http://hl7.org/fhir/sid/icd-9-cm |
| 75 | 359 | Procedure | `Procedure.code.coding` | 278297009.0 | Blood gas analysis | http://snomed.info/sct |
| 76 | 362 | Procedure | `Procedure.code.coding` | 96.07 | Insertion of other (naso-)gastric tube | http://hl7.org/fhir/sid/icd-9-cm |
| 77 | 364 | Procedure | `Procedure.code.coding` | 38.93 | Venous catheterization, not elsewhere classified | http://hl7.org/fhir/sid/icd-9-cm |
| 78 | 367 | Procedure | `Procedure.code.coding` | 96.6 | Enteral infusion of concentrated nutritional substances | http://hl7.org/fhir/sid/icd-9-cm |
| 79 | 370 | Procedure | `Procedure.code.coding` | 173830003.0 | Gastric lavage | http://snomed.info/sct |
| 80 | 372 | Procedure | `Procedure.code.coding` | 57931004.0 | Puncture of artery | http://snomed.info/sct |
| 81 | 374 | Procedure | `Procedure.code.coding` | 234083009.0 | Venous puncture | http://snomed.info/sct |
| 82 | 376 | Procedure | `Procedure.code.coding` | 51241000.0 | Control of hemorrhage | http://snomed.info/sct |
| 83 | 379 | Procedure | `Procedure.code.coding` | 271061004.0 | Random blood glucose measurement | http://snomed.info/sct |
| 84 | 382 | Procedure | `Procedure.code.coding` | 97.37 | Removal of tracheostomy tube | http://hl7.org/fhir/sid/icd-9-cm |
| 85 | 384 | Procedure | `Procedure.code.coding` | SP000826 | Tindakan Non Medis | http://terminology.kemkes.go.id/sp |
| 86 | 387 | Procedure | `Procedure.code.coding` | 276026009.0 | Fluid balance regulation | http://snomed.info/sct |
| 87 | 389 | Procedure | `Procedure.code.coding` | 182810003.0 | Intensive care monitoring | http://snomed.info/sct |
| 88 | 392 | Procedure | `Procedure.code.coding` | 104177005.0 | Electrolyte measurement | http://snomed.info/sct |
| 89 | 394 | Procedure | `Procedure.code.coding` | 87.44 | Routine chest x-ray, so described | http://hl7.org/fhir/sid/icd-9-cm |
| 90 | 397 | Procedure | `Procedure.code.coding` | 96.04 | Insertion of endotracheal tube | http://hl7.org/fhir/sid/icd-9-cm |
| 91 | 400 | Procedure | `Procedure.code.coding` | 226007004.0 | Post-surgical wound care | http://snomed.info/sct |
| 92 | 402 | Procedure | `Procedure.code.coding` | 48403009.0 | Insertion of infusion pump | http://snomed.info/sct |
| 93 | 405 | Procedure | `Procedure.code.coding` | SP000827 | Pemasangan dan Monitoring Syringe Pump | http://terminology.kemkes.go.id/sp |
| 94 | 408 | Procedure | `Procedure.code.coding` | 410136007.0 | Nursing coordination management | http://snomed.info/sct |
| 95 | 413 | Procedure | `Procedure.code.coding` | 43060002.0 | Intravenous injection | http://snomed.info/sct |
| 96 | 418 | Procedure | `Procedure.code.coding` | SP000822 | Konsultasi Non Medis | http://terminology.kemkes.go.id/sp |
| 97 | 424 | Procedure | `Procedure.code.coding` | 360362007.0 | Suture of laceration of perineum | http://snomed.info/sct |
| 98 | 426 | Procedure | `Procedure.code.coding` | 73.1 | Other surgical induction of labor | http://hl7.org/fhir/sid/icd-9-cm |
| 99 | 428 | Procedure | `Procedure.code.coding` | 309878003.0 | Exploration of uterine cavity | http://snomed.info/sct |
| 100 | 430 | Procedure | `Procedure.code.coding` | SP000818 | Pemasangan IUD/ Implan | http://terminology.kemkes.go.id/sp |
| 101 | 432 | Procedure | `Procedure.code.coding` | SP000821 | Konsultasi Medis | http://terminology.kemkes.go.id/sp |
| 102 | 437 | Procedure | `Procedure.code.coding` | 387672006.0 | Cardiotochogram | http://snomed.info/sct |
| 103 | 440 | Procedure | `Procedure.code.coding` | 89.52 | Electrocardiogram | http://hl7.org/fhir/sid/icd-9-cm |
| 104 | 442 | Procedure | `Procedure.code.coding` | SP000821 | Konsultasi Medis | http://terminology.kemkes.go.id/sp |
| 105 | 445 | Procedure | `Procedure.code.coding` | SP000826 | Tindakan Non Medis | http://terminology.kemkes.go.id/sp |
| 106 | 450 | Observation | `Observation.code.coding` | SP000815 | Jenis Kasus Pasien | http://terminology.kemkes.go.id/sp |
| 107 | 451 | Observation | `Observation.valueCodeableConcept.coding` | SP000816 | Kasus Baru | http://terminology.kemkes.go.id/sp |
| 108 | 452 | Observation | `Observation.valueCodeableConcept.coding` | SP000817 | Kasus Lama | http://terminology.kemkes.go.id/sp |
| 109 | 462 | Observation | `Observation.code.coding` | 184061005.0 | Patient registration status | http://snomed.info/sct |
| 110 | 463 | Observation | `Observation.valueCodeableConcept.coding` | SP000812 | Pasien Baru | http://terminology.kemkes.go.id/sp |
| 111 | 464 | Observation | `Observation.valueCodeableConcept.coding` | SP000813 | Pasien Lama | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 70 |
| http://terminology.kemkes.go.id/sp | 22 |
| http://hl7.org/fhir/sid/icd-9-cm | 18 |
| http://terminology.hl7.org/CodeSystem/admit-source | 1 |
| **Total** | **111** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 28 | – | Faskes yang melayani ANC | Organization | `Organization.name` |
| 68 | – | Unit Ruangan | Location | `Location.identifier` |
