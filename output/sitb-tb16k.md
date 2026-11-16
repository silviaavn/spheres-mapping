# Output Form: SITB TB 16K

Sumber: `mapping/phdt-data-dictionary-sitb-tb16k.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 24 |
| Code (`jumlah code` = 1) | 39 |
| Code unik (code + CodeSystem) | 36 |
| Variabel BQ (unik) | 40 |
| Variabel di Excel export | 40 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 3–8 | Group | – | – | – |
| 2 | 11–11 | Practitioner | – | – | `petugas_yang_menginvestigasi_kontak_nama_kader_petugas_kesehatan` → `Practitioner.name.text` (11) |
| 3 | 12–14 | PractitionerRole | – | – | `petugas_yang_menginvestigasi_kontak_nama_fasyankesorganisasi_kader` → `PractitionerRole.organization.reference` (14) 🔎 lookup master data |
| 4 | 16–26 | Observation | SP000373 | Kader Kesehatan | – |
| 5 | 29–34 | RelatedPerson | – | – | `no_register_sitb` → `RelatedPerson.identifier` (29)<br>`nama_kasus_indeks` → `RelatedPerson.name.text` (31) |
| 6 | 36–48 | Observation | 424144002 | Current chronological age | `umur_kasus_indeks` → `Observation.valueQuantity.value` (39) |
| 7 | 50–62 | Observation | 106229004 | Qualifier for type of diagnosis | `tipe_diagnosis` → `Observation.valueCodeableConcept.coding` (53)<br>`tanggal_hasil_diagnosis` → `Observation.effectiveDateTime` (59) |
| 8 | 64–76 | Observation | 415759006 | Tuberculosis index case | `jenis_kasus_indeks` → `Observation.valueCodeableConcept.coding` (67) |
| 9 | 78–99 | Patient | – | – | _Nama_ → `Patient.active` (78, tanpa BQ)<br>`identitas_kontak_nama` → `Patient.name.text` (79)<br>`identitas_kontak_nik` → `Patient.identifier.value` (82)<br>`identitas_kontak_lp` → `Patient.gender` (83)<br>_Provinsi_ → `Patient.address.extension.extension.valueCode` (89, tanpa BQ)<br>_Kabupaten/ Kota_ → `Patient.address.extension.extension.valueCode` (92, tanpa BQ)<br>_Kecamatan_ → `Patient.address.extension.extension.valueCode` (95, tanpa BQ)<br>_Kelurahan_ → `Patient.address.extension.extension.valueCode` (98, tanpa BQ)<br>`identitas_kontak_alamat` → `Patient.address.line` (99) |
| 10 | 101–112 | Observation | 424144002 | Current chronological age | `identitas_kontak_umur` → `Observation.valueQuantity.value` (104) |
| 11 | 115–125 | ServiceRequest | 185389009 | Follow-up visit | `dirujukdikirim_oleh` → `ServiceRequest.category.coding` (115) |
| 12 | 127–141 | Encounter | – | – | `nama_fasyankes` → `Encounter.serviceProvider.reference` (161) 🔎 lookup master data |
| 13 | 143–149 | Condition | Z20.1 | Contact with and exposure to tuberculosis | – |
| 14 | 163–174 | Observation | 225368008 | Contact tracing | `identitas_kontak_metode_ik` → `Observation.valueCodeableConcept.coding` (166)<br>`tanggal_investigasi` → `Observation.effectiveDateTime` (171) |
| 15 | 176–187 | Observation | SP000369 | Kontak Dengan Penderita TBC | _Kontak Dengan Penderita TBC_ → `Observation.status` (176, tanpa BQ)<br>`identitas_kontak_kontak_serumah` → `Observation.valueCodeableConcept.coding` (179)<br>`identitas_kontak_kontak_erat` → `Observation.valueCodeableConcept.coding` (180) |
| 16 | 189–232 | QuestionnaireResponse | – | – | `hasil_skrining_batuk` → `QuestionnaireResponse.item.text` (200)<br>`hasil_skrining_gejala_lain_sesak_napas` → `QuestionnaireResponse.item.item.text` (205)<br>`hasil_skrining_gejala_lain_berkeringat_malam_hari_tanpa_kegiatan` → `QuestionnaireResponse.item.item.text` (208)<br>`hasil_skrining_gejala_lain_demam_meriang_1_bulan` → `QuestionnaireResponse.item.item.text` (211)<br>`hasil_skrining_faktor_risiko_dm` → `QuestionnaireResponse.item.item.text` (216)<br>`hasil_skrining_faktor_risiko_lansia_60_th` → `QuestionnaireResponse.item.item.text` (219)<br>`hasil_skrining_faktor_risiko_ibu_hamil` → `QuestionnaireResponse.item.item.text` (222)<br>`hasil_skrining_faktor_risiko_perokok` → `QuestionnaireResponse.item.item.text` (225)<br>`hasil_skrining_faktor_risiko_pernah_berobat_tbc_tapi_tidak_tuntas` → `QuestionnaireResponse.item.item.text` (228)<br>`memenuhi_syarat_rujukan_pemeriksaan_terduga` → `QuestionnaireResponse.item.text` (231) |
| 17 | 235–246 | Observation | SP000206 | Dirujuk Pemeriksaan Terduga TBC | `dirujuk_pemeriksaan_terduga_tbc` → `Observation.valueBoolean` (238) |
| 18 | 248–259 | Observation | 171400006 | Examination for suspected tuberculosis | `diperiksa_terduga_tbc` → `Observation.valueBoolean` (251) |
| 19 | 261–272 | Observation | SP000207 | Hasil Pemeriksaan Terduga | _Hasil Pemeriksaan Terduga_ → `Observation.status` (261, tanpa BQ)<br>`hasil_pemeriksaan_terduga_sakit_tbc` → `Observation.valueCodeableConcept.coding` (264)<br>`hasil_pemeriksaan_terduga_tidak_tbc` → `Observation.valueCodeableConcept.coding` (265) |
| 20 | 274–285 | Observation | SP000209 | Memenuhi syarat rujukan pemeriksaan Eligibilitas TPT | `memenuhi_syarat_rujukan_pemeriksaan_eligibilitas_tpt` → `Observation.valueBoolean` (277) |
| 21 | 287–298 | Observation | SP000210 | Kesimpulan Hasil Pemeriksaan Eligibilitas TPT | `kesimpulan_hasil_pemeriksaan_eligibilitas_tpt` → `Observation.valueCodeableConcept.coding` (290) |
| 22 | 300–311 | Observation | SP000211 | Memenuhi syarat TPT | `memenuhi_syarat_tpt` → `Observation.valueCodeableConcept.coding` (303) |
| 23 | 313–324 | Observation | SP000212 | Tanggal Pemberian TPT | _Tanggal Pemberian TPT_ → `Observation.status` (313, tanpa BQ)<br>`tanggal_pemberian_tpt__5_th` → `Observation.valueDateTime` (316)<br>`tanggal_pemberian_tpt__5_th_1` → `Observation.valueDateTime` (317) |
| 24 | 326–343 | Observation | SP000213 | Hasil Akhir TPT | _Hasil Akhir TPT_ → `Observation.valueString` (329, tanpa BQ)<br>`hasil_akhir_tpt__5_th` → `Observation.valueCodeableConcept.coding` (330)<br>`hasil_akhir_tpt__5_th_1` → `Observation.valueCodeableConcept.coding` (331) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 15 |
| Group | 1 |
| Practitioner | 1 |
| PractitionerRole | 1 |
| RelatedPerson | 1 |
| Patient | 1 |
| ServiceRequest | 1 |
| Encounter | 1 |
| Condition | 1 |
| QuestionnaireResponse | 1 |
| **Total** | **24** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 12 | PractitionerRole | `PractitionerRole.code` | SP000373 | Kader Kesehatan | http://terminology.kemkes.go.id/sp |
| 2 | 18 | Observation | `Observation.code.coding` | SP000373 | Kader Kesehatan | http://terminology.kemkes.go.id/sp |
| 3 | 38 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 4 | 52 | Observation | `Observation.code.coding` | 106229004 | Qualifier for type of diagnosis | http://snomed.info/sct |
| 5 | 53 | Observation | `Observation.valueCodeableConcept.coding` | tb-bac | Terkonfirmasi bakteriologis | http://terminology.kemkes.go.id/CodeSystem/tb-case-definition |
| 6 | 54 | Observation | `Observation.valueCodeableConcept.coding` | tb-clin | Terdiagnosis klinis | http://terminology.kemkes.go.id/CodeSystem/tb-case-definition |
| 7 | 66 | Observation | `Observation.code.coding` | 415759006 | Tuberculosis index case | http://snomed.info/sct |
| 8 | 67 | Observation | `Observation.valueCodeableConcept.coding` | TB-SO | Tuberkulosis Sensitif Obat | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 9 | 68 | Observation | `Observation.valueCodeableConcept.coding` | TB-RO | Tuberkulosis Resisten Obat | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 10 | 103 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 11 | 119 | ServiceRequest | `ServiceRequest.code.coding` | 185389009 | Follow-up visit | http://snomed.info/sct |
| 12 | 120 | ServiceRequest | `ServiceRequest.code.coding` | 737492002 | Outpatient care management | http://snomed.info/sct |
| 13 | 145 | Condition | `Condition.code.coding` | Z20.1 | Contact with and exposure to tuberculosis | http://hl7.org/fhir/sid/icd-10 |
| 14 | 165 | Observation | `Observation.code.coding` | 225368008 | Contact tracing | http://snomed.info/sct |
| 15 | 166 | Observation | `Observation.valueCodeableConcept.coding` | SP000200 | Invitasi kontak | http://terminology.kemkes.go.id/sp |
| 16 | 167 | Observation | `Observation.valueCodeableConcept.coding` | 439708006 | Home visit | http://snomed.info/sct |
| 17 | 178 | Observation | `Observation.code.coding` | SP000369 | Kontak Dengan Penderita TBC | http://terminology.kemkes.go.id/sp |
| 18 | 179 | Observation | `Observation.valueCodeableConcept.coding` | SP000201 | Kontak Serumah | http://terminology.kemkes.go.id/sp |
| 19 | 180 | Observation | `Observation.valueCodeableConcept.coding` | SP000202 | Kontak Erat | http://terminology.kemkes.go.id/sp |
| 20 | 237 | Observation | `Observation.code.coding` | SP000206 | Dirujuk Pemeriksaan Terduga TBC | http://terminology.kemkes.go.id/sp |
| 21 | 250 | Observation | `Observation.code.coding` | 171400006 | Examination for suspected tuberculosis | http://snomed.info/sct |
| 22 | 263 | Observation | `Observation.code.coding` | SP000207 | Hasil Pemeriksaan Terduga | http://terminology.kemkes.go.id/sp |
| 23 | 264 | Observation | `Observation.valueCodeableConcept.coding` | 56717001 | Tuberculosis | http://snomed.info/sct |
| 24 | 265 | Observation | `Observation.valueCodeableConcept.coding` | SP000208 | Tidak TBC | http://terminology.kemkes.go.id/sp |
| 25 | 276 | Observation | `Observation.code.coding` | SP000209 | Memenuhi syarat rujukan pemeriksaan Eligibilitas TPT | http://terminology.kemkes.go.id/sp |
| 26 | 289 | Observation | `Observation.code.coding` | SP000210 | Kesimpulan Hasil Pemeriksaan Eligibilitas TPT | http://terminology.kemkes.go.id/sp |
| 27 | 290 | Observation | `Observation.valueCodeableConcept.coding` | SP000211 | Memenuhi syarat TPT | http://terminology.kemkes.go.id/sp |
| 28 | 291 | Observation | `Observation.valueCodeableConcept.coding` | SP000374 | Tidak Memenuhi Syarat TPT | http://terminology.kemkes.go.id/sp |
| 29 | 302 | Observation | `Observation.code.coding` | SP000211 | Memenuhi syarat TPT | http://terminology.kemkes.go.id/sp |
| 30 | 303 | Observation | `Observation.valueCodeableConcept.coding` | 373066001 | Yes | http://snomed.info/sct |
| 31 | 304 | Observation | `Observation.valueCodeableConcept.coding` | 373067005 | No | http://snomed.info/sct |
| 32 | 315 | Observation | `Observation.code.coding` | SP000212 | Tanggal Pemberian TPT | http://terminology.kemkes.go.id/sp |
| 33 | 328 | Observation | `Observation.code.coding` | SP000213 | Hasil Akhir TPT | http://terminology.kemkes.go.id/sp |
| 34 | 330 | Observation | `Observation.valueCodeableConcept.coding` | 371001000 | Patient cured | http://snomed.info/sct |
| 35 | 332 | Observation | `Observation.valueCodeableConcept.coding` | 182992009 | Treatment completed | http://snomed.info/sct |
| 36 | 333 | Observation | `Observation.valueCodeableConcept.coding` | CP000094 | Pengobatan Gagal | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 37 | 334 | Observation | `Observation.valueCodeableConcept.coding` | 419099009 | Dead | http://snomed.info/sct |
| 38 | 335 | Observation | `Observation.valueCodeableConcept.coding` | 399307001 | Lost to follow-up | http://snomed.info/sct |
| 39 | 336 | Observation | `Observation.valueCodeableConcept.coding` | CP000096 | Tidak dievaluasi/pindah | http://terminology.kemkes.go.id/CodeSystem/clinical-term |

### Code per CodeSystem

| CodeSystem | Jumlah | Code |
|---|---|---|
| http://terminology.kemkes.go.id/sp | 16 | SP000373, SP000373, SP000200, SP000369, SP000201, SP000202, SP000206, SP000207, SP000208, SP000209, SP000210, SP000211, SP000374, SP000211, SP000212, SP000213 |
| http://snomed.info/sct | 16 | 424144002, 106229004, 415759006, 424144002, 185389009, 737492002, 225368008, 439708006, 171400006, 56717001, 373066001, 373067005, 371001000, 182992009, 419099009, 399307001 |
| http://terminology.kemkes.go.id/CodeSystem/tb-case-definition | 2 | tb-bac, tb-clin |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 2 | TB-SO, TB-RO |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 2 | CP000094, CP000096 |
| http://hl7.org/fhir/sid/icd-10 | 1 | Z20.1 |
| **Total** | **39** | |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
