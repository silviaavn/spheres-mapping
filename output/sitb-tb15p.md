# Output Form: SITB - TB 15P (Penerima TPT)

Sumber: `mapping/phdt-data-dictionary-sitb-tb15p.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-sitb-tb15p.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 21 |
| Code (`jumlah code` = 1) | 59 |
| Code unik (code + CodeSystem) | 32 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 15 |
| Variabel BQ (unik) | 6 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–8 | Patient | – | – | _NIK (Nomor Induk Kependudukan)_ → `Patient.identifier.value` (5, tanpa BQ)<br>_Nama Lengkap Pasien_ → `Patient.name.text` (6, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (7, tanpa BQ)<br>_Provinsi_ → `Patient.address.extension.url` (23, tanpa BQ)<br>_Kabupaten/Kota_ → `Patient.address.extension.url` (26, tanpa BQ)<br>_Kecamatan_ → `Patient.address.extension.url` (29, tanpa BQ)<br>_Kelurahan_ → `Patient.address.extension.url` (32, tanpa BQ)<br>_Alamat Lengkap Penerima TPT_ → `Patient.address.line` (35, tanpa BQ) |
| 2 | 9–20 | Observation | 424144002 | Current chronological age | _Umur (Tahun)_ → `Observation.valueQuantity.value` (12, tanpa BQ) |
| 3 | 83–95 | Observation | SP000450 | Faktor Risiko Tuberkulosis | _Faktor risiko_ → `Observation.valueCodeableConcept.coding` (86, tanpa BQ) |
| 4 | 96–108 | Observation | 415759006 | Tuberculosis index case | _Tipe TBC Kasus Indeks_ → `Observation.valueCodeableConcept.coding` (99, tanpa BQ) |
| 5 | 109–121 | Observation | 106229004 | Qualifier for type of diagnosis | `{tipe_diagnosis_tbc}` → `Observation.valueCodeableConcept.coding` (112)<br>`{tipe_diagnosis_tbc}` → `Observation.valueCodeableConcept.coding` (113)<br>`{nama_lengkap_pasien}` → `Observation.subject.display` (116)<br>`{tanggal_mulai_pengobatan}` → `Observation.effectiveDateTime` (118)<br>`{nama_lengkap_pasien}` → `Observation.issued` (119) |
| 6 | 122–134 | QuestionnaireResponse | https://fhir.kemkes.go.id/Questionnaire/Q0001 | – | _Lokasi Anatomi TBC Kasus Indeks_ → `QuestionnaireResponse.questionnaire` (122, tanpa BQ) |
| 7 | 136–149 | Observation | 23539-0 | Tuberculosis reaction wheal [Diameter] --3 days post dose mammalian tuberculin intradermal | _Hasil Uji Tuberkulin_ → `Observation.status` (136, tanpa BQ)<br>`{hasil_pemeriksaan_tuberkulin}` → `Observation.valueCodeableConcept.coding` (140)<br>`{hasil_pemeriksaan_tuberkulin}` → `Observation.valueCodeableConcept.coding` (141)<br>`{nama_lengkap_pasien}` → `Observation.subject.display` (144)<br>`{tanggal_mulai_pengobatan}` → `Observation.effectiveDateTime` (146)<br>`{tanggal_mulai_pengobatan}` → `Observation.issued` (147) |
| 8 | 150–163 | Observation | 71773-6 | Mycobacterium tuberculosis stimulated gamma interferon [Interpretation] in Blood Qualitative | _Hasil Uji IGRA_ → `Observation.status` (150, tanpa BQ)<br>`{hasil_pemeriksaan_igra}` → `Observation.valueCodeableConcept.coding` (154)<br>`{hasil_pemeriksaan_igra}` → `Observation.valueCodeableConcept.coding` (155)<br>`{nama_lengkap_pasien}` → `Observation.subject.display` (158)<br>`{tanggal_mulai_pengobatan}` → `Observation.effectiveDateTime` (160)<br>`{tanggal_mulai_pengobatan}` → `Observation.issued` (161) |
| 9 | 165–178 | Observation | SP000723 | Pemeriksaan TBST | _Hasil Uji TBST_ → `Observation.valueCodeableConcept.coding` (169, tanpa BQ)<br>_Tanggal Pemeriksaan_ → `Observation.effectiveDateTime` (175, tanpa BQ) |
| 10 | 179–192 | Observation | 24648-8 | XR Chest PA upright | _Hasil Foto Toraks_ → `Observation.status` (179, tanpa BQ)<br>`{hasil_pemeriksaan_foto_toraks}` → `Observation.valueCodeableConcept.coding` (183)<br>`{hasil_pemeriksaan_foto_toraks}` → `Observation.valueCodeableConcept.coding` (184)<br>`{hasil_pemeriksaan_foto_toraks}` → `Observation.dataAbsentReason` (185)<br>`{nama_lengkap_pasien}` → `Observation.subject.display` (187)<br>`{tanggal_mulai_pengobatan}` → `Observation.effectiveDateTime` (189)<br>`{tanggal_mulai_pengobatan}` → `Observation.issued` (190) |
| 11 | 193–205 | Observation | SP000210 | Kesimpulan Hasil Pemeriksaan Eligibilitas TPT | _Hasil Pemeriksaan Eligibilitas TPT ke-1_ → `Observation.valueCodeableConcept.coding` (197, tanpa BQ) |
| 12 | 206–219 | Observation | 23539-0 | Tuberculosis reaction wheal [Diameter] --3 days post dose mammalian tuberculin intradermal | _Hasil Uji Tuberkulin_ → `Observation.status` (206, tanpa BQ)<br>`{hasil_pemeriksaan_tuberkulin}` → `Observation.valueCodeableConcept.coding` (210)<br>`{hasil_pemeriksaan_tuberkulin}` → `Observation.valueCodeableConcept.coding` (211)<br>`{nama_lengkap_pasien}` → `Observation.subject.display` (214)<br>`{tanggal_mulai_pengobatan}` → `Observation.effectiveDateTime` (216)<br>`{tanggal_mulai_pengobatan}` → `Observation.issued` (217) |
| 13 | 220–233 | Observation | 71773-6 | Mycobacterium tuberculosis stimulated gamma interferon [Interpretation] in Blood Qualitative | _Hasil Uji IGRA_ → `Observation.status` (220, tanpa BQ)<br>`{hasil_pemeriksaan_igra}` → `Observation.valueCodeableConcept.coding` (224)<br>`{hasil_pemeriksaan_igra}` → `Observation.valueCodeableConcept.coding` (225)<br>`{nama_lengkap_pasien}` → `Observation.subject.display` (228)<br>`{tanggal_mulai_pengobatan}` → `Observation.effectiveDateTime` (230)<br>`{tanggal_mulai_pengobatan}` → `Observation.issued` (231) |
| 14 | 234–247 | Observation | SP000723 | Pemeriksaan TBST | _Hasil Uji TBST_ → `Observation.valueCodeableConcept.coding` (238, tanpa BQ)<br>_Tanggal Pemeriksaan_ → `Observation.effectiveDateTime` (244, tanpa BQ) |
| 15 | 248–261 | Observation | 24648-8 | XR Chest PA upright | _Hasil Foto Toraks_ → `Observation.status` (248, tanpa BQ)<br>`{hasil_pemeriksaan_foto_toraks}` → `Observation.valueCodeableConcept.coding` (252)<br>`{hasil_pemeriksaan_foto_toraks}` → `Observation.valueCodeableConcept.coding` (253)<br>`{hasil_pemeriksaan_foto_toraks}` → `Observation.dataAbsentReason` (254)<br>`{nama_lengkap_pasien}` → `Observation.subject.display` (256)<br>`{tanggal_mulai_pengobatan}` → `Observation.effectiveDateTime` (258)<br>`{tanggal_mulai_pengobatan}` → `Observation.issued` (259) |
| 16 | 262–274 | Observation | SP000210 | Kesimpulan Hasil Pemeriksaan Eligibilitas TPT | _Hasil Pemeriksaan Eligibilitas TPT ke-2_ → `Observation.valueCodeableConcept.coding` (266, tanpa BQ) |
| 17 | 275–286 | Observation | SP000210 | Kesimpulan Hasil Pemeriksaan Eligibilitas TPT | _Kesimpulan Hasil Pemeriksaan Eligibilitas TPT_ → `Observation.valueCodeableConcept.coding` (278, tanpa BQ) |
| 18 | 287–307 | ServiceRequest | 409014006 | Delivery care management | _Tempat Pemberian TPT_ → `ServiceRequest.status` (287, tanpa BQ)<br>_Dirujuk ke (Nama Fasyankes)_ → `ServiceRequest.locationCode.text` (307, tanpa BQ) |
| 19 | 308–320 | CarePlan | CP000005 | Paduan Pengobatan | _Tindak Lanjut_ → `CarePlan.intent` (310, tanpa BQ)<br>_Tanggal Mulai TPT_ → `CarePlan.period.start` (314, tanpa BQ) |
| 20 | 321–342 | Encounter | – | – | _//id puskesmas_ → `Encounter.serviceProvider.reference` (342, tanpa BQ) |
| 21 | 343–349 | Condition | 1237025001 | At increased risk of exposure to Mycobacterium tuberculosis complex | – |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 15 |
| Patient | 1 |
| QuestionnaireResponse | 1 |
| ServiceRequest | 1 |
| CarePlan | 1 |
| Encounter | 1 |
| Condition | 1 |
| **Total** | **21** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 11 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 2 | 85 | Observation | `Observation.code.coding` | SP000450 | Faktor Risiko Tuberkulosis | http://terminology.kemkes.go.id/sp |
| 3 | 86 | Observation | `Observation.valueCodeableConcept.coding` | SP000201 | Kontak serumah | http://terminology.kemkes.go.id/sp |
| 4 | 87 | Observation | `Observation.valueCodeableConcept.coding` | OV000431 | Siswa Berasrama | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 5 | 88 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 6 | 98 | Observation | `Observation.code.coding` | 415759006 | Tuberculosis index case | http://snomed.info/sct |
| 7 | 99 | Observation | `Observation.valueCodeableConcept.coding` | TB-SO | Tuberkulosis Sensitif Obat | https://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 8 | 100 | Observation | `Observation.valueCodeableConcept.coding` | TB-RO | Tuberkulosis Resisten Obat | https://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 9 | 111 | Observation | `Observation.code.coding` | 106229004 | Qualifier for type of diagnosis | http://snomed.info/sct |
| 10 | 112 | Observation | `Observation.valueCodeableConcept.coding` | tb-bac | Terkonfirmasi bakteriologis | http://terminology.kemkes.go.id/CodeSystem/tb-case-definition |
| 11 | 113 | Observation | `Observation.valueCodeableConcept.coding` | tb-clin | Terdiagnosis klinis | http://terminology.kemkes.go.id/CodeSystem/tb-case-definition |
| 12 | 133 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 154283005 | Pulmonary tuberculosis | http://snomed.info/sct |
| 13 | 134 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 423997002 | Tuberculosis, extrapulmonary | http://snomed.info/sct |
| 14 | 139 | Observation | `Observation.code.coding` | 23539-0 | Tuberculosis reaction wheal [Diameter] --3 days post dose mammalian tuberculin intradermal | http://loinc.org |
| 15 | 140 | Observation | `Observation.valueCodeableConcept.coding` | 268376005 | Mantoux: positive | http://snomed.info/sct |
| 16 | 141 | Observation | `Observation.valueCodeableConcept.coding` | 268375009 | Mantoux: negative | http://snomed.info/sct |
| 17 | 142 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 18 | 153 | Observation | `Observation.code.coding` | 71773-6 | Mycobacterium tuberculosis stimulated gamma interferon [Interpretation] in Blood Qualitative | http://loinc.org |
| 19 | 154 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 20 | 155 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 21 | 156 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 22 | 168 | Observation | `Observation.code.coding` | SP000723 | Pemeriksaan TBST | http://terminology.kemkes.go.id/sp |
| 23 | 169 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 24 | 170 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 25 | 171 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 26 | 182 | Observation | `Observation.code.coding` | 24648-8 | XR Chest PA upright | http://loinc.org |
| 27 | 183 | Observation | `Observation.valueCodeableConcept.coding` | 707307002 | Tuberculosis screening chest X-ray abnormal | http://snomed.info/sct |
| 28 | 184 | Observation | `Observation.valueCodeableConcept.coding` | 707308007 | Tuberculosis screening chest X-ray normal | http://snomed.info/sct |
| 29 | 185 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 30 | 196 | Observation | `Observation.code.coding` | SP000210 | Kesimpulan Hasil Pemeriksaan Eligibilitas TPT | http://terminology.kemkes.go.id/sp |
| 31 | 197 | Observation | `Observation.valueCodeableConcept.coding` | SP000211 | Memenuhi syarat TPT | http://terminology.kemkes.go.id/sp |
| 32 | 198 | Observation | `Observation.valueCodeableConcept.coding` | SP000374 | Tidak Memenuhi Syarat TPT | http://terminology.kemkes.go.id/sp |
| 33 | 209 | Observation | `Observation.code.coding` | 23539-0 | Tuberculosis reaction wheal [Diameter] --3 days post dose mammalian tuberculin intradermal | http://loinc.org |
| 34 | 210 | Observation | `Observation.valueCodeableConcept.coding` | 268376005 | Mantoux: positive | http://snomed.info/sct |
| 35 | 211 | Observation | `Observation.valueCodeableConcept.coding` | 268375009 | Mantoux: negative | http://snomed.info/sct |
| 36 | 212 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 37 | 223 | Observation | `Observation.code.coding` | 71773-6 | Mycobacterium tuberculosis stimulated gamma interferon [Interpretation] in Blood Qualitative | http://loinc.org |
| 38 | 224 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 39 | 225 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 40 | 226 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 41 | 237 | Observation | `Observation.code.coding` | SP000723 | Pemeriksaan TBST | http://terminology.kemkes.go.id/sp |
| 42 | 238 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 43 | 239 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 44 | 240 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 45 | 251 | Observation | `Observation.code.coding` | 24648-8 | XR Chest PA upright | http://loinc.org |
| 46 | 252 | Observation | `Observation.valueCodeableConcept.coding` | 707307002 | Tuberculosis screening chest X-ray abnormal | http://snomed.info/sct |
| 47 | 253 | Observation | `Observation.valueCodeableConcept.coding` | 707308007 | Tuberculosis screening chest X-ray normal | http://snomed.info/sct |
| 48 | 254 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 49 | 265 | Observation | `Observation.code.coding` | SP000210 | Kesimpulan Hasil Pemeriksaan Eligibilitas TPT | http://terminology.kemkes.go.id/sp |
| 50 | 266 | Observation | `Observation.valueCodeableConcept.coding` | SP000211 | Memenuhi syarat TPT | http://terminology.kemkes.go.id/sp |
| 51 | 267 | Observation | `Observation.valueCodeableConcept.coding` | SP000374 | Tidak Memenuhi Syarat TPT | http://terminology.kemkes.go.id/sp |
| 52 | 277 | Observation | `Observation.code.coding` | SP000210 | Kesimpulan Hasil Pemeriksaan Eligibilitas TPT | http://terminology.kemkes.go.id/sp |
| 53 | 278 | Observation | `Observation.valueCodeableConcept.coding` | SP000211 | Memenuhi syarat TPT | http://terminology.kemkes.go.id/sp |
| 54 | 279 | Observation | `Observation.valueCodeableConcept.coding` | SP000374 | Tidak Memenuhi Syarat TPT | http://terminology.kemkes.go.id/sp |
| 55 | 291 | ServiceRequest | `ServiceRequest.code.coding` | 409014006 | Delivery care management | http://snomed.info/sct |
| 56 | 300 | ServiceRequest | `ServiceRequest.locationCode.coding` | SP000129 | Puskesmas PONED | http://terminology.kemkes.go.id/sp |
| 57 | 304 | ServiceRequest | `ServiceRequest.locationCode.coding` | SP000128 | Rumah Sakit Ibu dan Anak | http://terminology.kemkes.go.id/sp |
| 58 | 320 | CarePlan | `CarePlan.activity.detail.code.coding` | CP000005 | Paduan Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 59 | 345 | Condition | `Condition.code.coding` | 1237025001 | At increased risk of exposure to Mycobacterium tuberculosis complex | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 16 |
| http://terminology.kemkes.go.id/sp | 15 |
| http://loinc.org | 14 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 8 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 2 |
| https://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 2 |
| http://terminology.kemkes.go.id/CodeSystem/tb-case-definition | 2 |
| **Total** | **59** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 38 | – | Kode Fasyankes | Organization | `Organization.identifier` |
| 39 | – | Jenis Fasyankes | Organization | `Organization.type` |
| 42 | – | Kepemilikan Fasyankes | Organization | `Organization.type` |
| 44 | – | Nama Fasyankes | Organization | `Organization.name` |
| 49 | – | Provinsi Fasyankes | Organization | `Organization.address.extension.extension.valueCode` |
| 52 | – | Kabupaten Fasyankes | Organization | `Organization.address.extension.extension.valueCode` |
