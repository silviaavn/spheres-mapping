# Output Form: SITB - TB 16K (Investigasi Kontak)

Sumber: `mapping/phdt-data-dictionary-sitb-tb16k.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-sitb-tb16k.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 24 |
| Code (`jumlah code` = 1) | 38 |
| Code unik (code + CodeSystem) | 36 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 15 |
| Variabel BQ (unik) | 36 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–7 | Group | – | – | – |
| 2 | 9–9 | Practitioner | – | – | `petugas_yang_menginvestigasi_kontak_nama_kader_petugas_kesehatan` → `Practitioner.name` (9) |
| 3 | 10–10 | PractitionerRole | – | – | – |
| 4 | 11–21 | Observation | SP000373 | Kader Kesehatan | – |
| 5 | 47–51 | RelatedPerson | – | – | `no_register_sitb` → `RelatedPerson.identifier` (47)<br>`nama_kasus_indeks` → `RelatedPerson.name.text` (48) |
| 6 | 52–64 | Observation | 424144002 | Current chronological age | `umur_kasus_indeks` → `Observation.valueQuantity.value` (55) |
| 7 | 65–77 | Observation | 106229004 | Qualifier for type of diagnosis | `tipe_diagnosis` → `Observation.valueCodeableConcept.coding` (68)<br>`tanggal_hasil_diagnosis` → `Observation.effectiveDateTime` (74) |
| 8 | 78–79 | EpisodeOfCare | TB-SO | Tuberkulosis Sensitif Obat | `jenis_kasus_indeks` → `EpisodeOfCare.type.coding` (78) |
| 9 | 80–92 | Observation | 415759006 | Tuberculosis index case | – |
| 10 | 93–114 | Patient | – | – | `identitas_kontak_nama` → `Patient.active` (93)<br>`identitas_kontak_nik` → `Patient.identifier.value` (97)<br>`identitas_kontak_lp` → `Patient.gender` (98)<br>_Provinsi_ → `Patient.address.extension.extension.valueCode` (104, tanpa BQ)<br>_Kabupaten/ Kota_ → `Patient.address.extension.extension.valueCode` (107, tanpa BQ)<br>_Kecamatan_ → `Patient.address.extension.extension.valueCode` (110, tanpa BQ)<br>_Kelurahan_ → `Patient.address.extension.extension.valueCode` (113, tanpa BQ)<br>`identitas_kontak_alamat` → `Patient.address.line` (114) |
| 11 | 115–126 | Observation | 424144002 | Current chronological age | `identitas_kontak_umur` → `Observation.valueQuantity.value` (118) |
| 12 | 127–137 | ServiceRequest | – | – | `dirujukdikirim_oleh` → `ServiceRequest.category` (127) |
| 13 | 138–152 | Encounter | – | – | `petugas_yang_menginvestigasi_kontak_nama_fasyankesorganisasi_kader` → `Encounter.serviceProvider.reference` (169) 🔎 lookup master data |
| 14 | 153–159 | Condition | Z20.1 | Contact with and exposure to tuberculosis | – |
| 15 | 170–181 | Observation | 225368008 | Contact tracing | `identitas_kontak_metode_ik` → `Observation.valueCodeableConcept.coding` (173)<br>`tanggal_investigasi` → `Observation.effectiveDateTime` (178) |
| 16 | 182–193 | Observation | SP000369 | Kontak Dengan Penderita TBC | `identitas_kontak_kontak_serumah` → `Observation.valueCodeableConcept.coding` (185)<br>`identitas_kontak_kontak_erat` → `Observation.valueCodeableConcept.coding` (186) |
| 17 | 194–237 | QuestionnaireResponse | – | – | `hasil_skrining_batuk` → `QuestionnaireResponse.item.text` (205)<br>`hasil_skrining_gejala_lain_sesak_napas` → `QuestionnaireResponse.item.item.text` (210)<br>`hasil_skrining_gejala_lain_berkeringat_malam_hari_tanpa_kegiatan` → `QuestionnaireResponse.item.item.text` (213)<br>`hasil_skrining_gejala_lain_demam_meriang_1_bulan` → `QuestionnaireResponse.item.item.text` (216)<br>`hasil_skrining_faktor_risiko_dm` → `QuestionnaireResponse.item.item.text` (221)<br>`hasil_skrining_faktor_risiko_lansia_60_th` → `QuestionnaireResponse.item.item.text` (224)<br>`hasil_skrining_faktor_risiko_ibu_hamil` → `QuestionnaireResponse.item.item.text` (227)<br>`hasil_skrining_faktor_risiko_perokok` → `QuestionnaireResponse.item.item.text` (230)<br>`hasil_skrining_faktor_risiko_pernah_berobat_tbc_tapi_tidak_tuntas` → `QuestionnaireResponse.item.item.text` (233)<br>`memenuhi_syarat_rujukan_pemeriksaan_terduga` → `QuestionnaireResponse.item.text` (236) |
| 18 | 238–249 | Observation | SP000206 | Dirujuk Pemeriksaan Terduga TBC | `dirujuk_pemeriksaan_terduga_tbc` → `Observation.valueBoolean` (241) |
| 19 | 250–261 | Observation | 171400006 | Examination for suspected tuberculosis | `diperiksa_terduga_tbc` → `Observation.valueBoolean` (253) |
| 20 | 262–273 | Observation | SP000207 | Hasil Pemeriksaan Terduga | `hasil_pemeriksaan_terduga_sakit_tbc` → `Observation.valueCodeableConcept.coding` (265)<br>`hasil_pemeriksaan_terduga_tidak_tbc` → `Observation.valueCodeableConcept.coding` (266) |
| 21 | 274–285 | Observation | SP000209 | Memenuhi syarat rujukan pemeriksaan Eligibilitas TPT | `memenuhi_syarat_rujukan_pemeriksaan_eligibilitas_tpt` → `Observation.valueBoolean` (277) |
| 22 | 286–297 | Observation | SP000210 | Kesimpulan Hasil Pemeriksaan Eligibilitas TPT | `kesimpulan_hasil_pemeriksaan_eligibilitas_tpt` → `Observation.valueCodeableConcept.coding` (289) |
| 23 | 298–308 | Observation | SP000212 | Tanggal Pemberian TPT | `tanggal_pemberian_tpt__5_th_1` → `Observation.valueDateTime` (301) |
| 24 | 309–325 | Observation | SP000213 | Hasil Akhir TPT | `hasil_akhir_tpt__5_th_1` → `Observation.valueString` (312) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 14 |
| Group | 1 |
| Practitioner | 1 |
| PractitionerRole | 1 |
| RelatedPerson | 1 |
| EpisodeOfCare | 1 |
| Patient | 1 |
| ServiceRequest | 1 |
| Encounter | 1 |
| Condition | 1 |
| QuestionnaireResponse | 1 |
| **Total** | **24** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 10 | PractitionerRole | `PractitionerRole.code` | SP000373 | Kader Kesehatan | http://terminology.kemkes.go.id/sp |
| 2 | 13 | Observation | `Observation.code.coding` | SP000373 | Kader Kesehatan | http://terminology.kemkes.go.id/sp |
| 3 | 54 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 4 | 67 | Observation | `Observation.code.coding` | 106229004 | Qualifier for type of diagnosis | http://snomed.info/sct |
| 5 | 68 | Observation | `Observation.valueCodeableConcept.coding` | tb-bac | Terkonfirmasi bakteriologis | http://terminology.kemkes.go.id/CodeSystem/tb-case-definition |
| 6 | 69 | Observation | `Observation.valueCodeableConcept.coding` | tb-clin | Terdiagnosis klinis | http://terminology.kemkes.go.id/CodeSystem/tb-case-definition |
| 7 | 78 | EpisodeOfCare | `EpisodeOfCare.type.coding` | TB-SO | Tuberkulosis Sensitif Obat | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 8 | 79 | EpisodeOfCare | `EpisodeOfCare.type.coding` | TB-RO | Tuberkulosis Resisten Obat | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 9 | 82 | Observation | `Observation.code.coding` | 415759006 | Tuberculosis index case | http://snomed.info/sct |
| 10 | 83 | Observation | `Observation.valueCodeableConcept.coding` | TB-SO | Tuberkulosis Sensitif Obat | https://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 11 | 84 | Observation | `Observation.valueCodeableConcept.coding` | TB-RO | Tuberkulosis Resisten Obat | https://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 12 | 117 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 13 | 131 | ServiceRequest | `ServiceRequest.code` | 185389009 | Follow-up visit | http://snomed.info/sct |
| 14 | 132 | ServiceRequest | `ServiceRequest.code` | 737492002 | Outpatient care management | http://snomed.info/sct |
| 15 | 155 | Condition | `Condition.code.coding` | Z20.1 | Contact with and exposure to tuberculosis | http://hl7.org/fhir/sid/icd-10 |
| 16 | 172 | Observation | `Observation.code.coding` | 225368008 | Contact tracing | http://snomed.info/sct |
| 17 | 173 | Observation | `Observation.valueCodeableConcept.coding` | SP000200 | Invitasi kontak | http://terminology.kemkes.go.id/sp |
| 18 | 174 | Observation | `Observation.valueCodeableConcept.coding` | 439708006 | Home visit | http://snomed.info/sct |
| 19 | 184 | Observation | `Observation.code.coding` | SP000369 | Kontak Dengan Penderita TBC | http://terminology.kemkes.go.id/sp |
| 20 | 185 | Observation | `Observation.valueCodeableConcept.coding` | SP000201 | Kontak Serumah | http://terminology.kemkes.go.id/sp |
| 21 | 186 | Observation | `Observation.valueCodeableConcept.coding` | SP000202 | Kontak Erat | http://terminology.kemkes.go.id/sp |
| 22 | 240 | Observation | `Observation.code.coding` | SP000206 | Dirujuk Pemeriksaan Terduga TBC | http://terminology.kemkes.go.id/sp |
| 23 | 252 | Observation | `Observation.code.coding` | 171400006 | Examination for suspected tuberculosis | http://snomed.info/sct |
| 24 | 264 | Observation | `Observation.code.coding` | SP000207 | Hasil Pemeriksaan Terduga | http://terminology.kemkes.go.id/sp |
| 25 | 265 | Observation | `Observation.valueCodeableConcept.coding` | 56717001 | Tuberculosis | http://snomed.info/sct |
| 26 | 266 | Observation | `Observation.valueCodeableConcept.coding` | SP000208 | Tidak TBC | http://terminology.kemkes.go.id/sp |
| 27 | 276 | Observation | `Observation.code.coding` | SP000209 | Memenuhi syarat rujukan pemeriksaan Eligibilitas TPT | http://terminology.kemkes.go.id/sp |
| 28 | 288 | Observation | `Observation.code.coding` | SP000210 | Kesimpulan Hasil Pemeriksaan Eligibilitas TPT | http://terminology.kemkes.go.id/sp |
| 29 | 289 | Observation | `Observation.valueCodeableConcept.coding` | SP000211 | Memenuhi syarat TPT | http://terminology.kemkes.go.id/sp |
| 30 | 290 | Observation | `Observation.valueCodeableConcept.coding` | SP000374 | Tidak Memenuhi Syarat TPT | http://terminology.kemkes.go.id/sp |
| 31 | 300 | Observation | `Observation.code.coding` | SP000212 | Tanggal Pemberian TPT | http://terminology.kemkes.go.id/sp |
| 32 | 311 | Observation | `Observation.code.coding` | SP000213 | Hasil Akhir TPT | http://terminology.kemkes.go.id/sp |
| 33 | 313 | Observation | `Observation.valueCodeableConcept.coding` | 371001000 | Patient cured | http://snomed.info/sct |
| 34 | 314 | Observation | `Observation.valueCodeableConcept.coding` | 182992009 | Treatment completed | http://snomed.info/sct |
| 35 | 315 | Observation | `Observation.valueCodeableConcept.coding` | CP000094 | Pengobatan Gagal | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 36 | 316 | Observation | `Observation.valueCodeableConcept.coding` | 419099009 | Dead | http://snomed.info/sct |
| 37 | 317 | Observation | `Observation.valueCodeableConcept.coding` | 399307001 | Lost to follow-up | http://snomed.info/sct |
| 38 | 318 | Observation | `Observation.valueCodeableConcept.coding` | CP000096 | Tidak dievaluasi/pindah | http://terminology.kemkes.go.id/CodeSystem/clinical-term |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://terminology.kemkes.go.id/sp | 15 |
| http://snomed.info/sct | 14 |
| http://terminology.kemkes.go.id/CodeSystem/tb-case-definition | 2 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 2 |
| https://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 2 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 2 |
| http://hl7.org/fhir/sid/icd-10 | 1 |
| **Total** | **38** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
