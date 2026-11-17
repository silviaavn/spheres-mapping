# Output Form: SITB TB 16K

Sumber: `mapping/phdt-data-dictionary-sitb-tb16k.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 21 |
| Code (`jumlah code` = 1) | 35 |
| Code unik (code + CodeSystem) | 34 |
| Variabel BQ (unik) | 40 |
| Variabel di Excel export | 40 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 3–8 | Group | – | – | – |
| 2 | 11–22 | Observation | SP000373 | Kader Kesehatan | `petugas_yang_menginvestigasi_kontak_nama_kader_petugas_kesehatan` → `Observation.valueString` (14)<br>`petugas_yang_menginvestigasi_kontak_nama_fasyankesorganisasi_kader` → `Observation.performer.reference` (21) 🔎 lookup master data |
| 3 | 25–30 | RelatedPerson | – | – | `no_register_sitb` → `RelatedPerson.identifier` (25)<br>`nama_kasus_indeks` → `RelatedPerson.name.text` (27) |
| 4 | 32–44 | Observation | 424144002 | Current chronological age | `umur_kasus_indeks` → `Observation.valueQuantity.value` (35) |
| 5 | 46–58 | Observation | 106229004 | Qualifier for type of diagnosis | `tipe_diagnosis` → `Observation.valueCodeableConcept.coding` (49)<br>`tanggal_hasil_diagnosis` → `Observation.effectiveDateTime` (55) |
| 6 | 60–72 | Observation | 415759006 | Tuberculosis index case | `jenis_kasus_indeks` → `Observation.valueCodeableConcept.coding` (63) |
| 7 | 74–83 | Patient | – | – | _Nama_ → `Patient.active` (74, tanpa BQ)<br>`identitas_kontak_nama` → `Patient.name.text` (75)<br>`identitas_kontak_nik` → `Patient.identifier.value` (78)<br>`identitas_kontak_lp` → `Patient.gender` (79)<br>`identitas_kontak_alamat` → `Patient.address.line` (83) |
| 8 | 85–96 | Observation | 424144002 | Current chronological age | `identitas_kontak_umur` → `Observation.valueQuantity.value` (88) |
| 9 | 99–109 | ServiceRequest | 185389009 | Follow-up visit | `dirujukdikirim_oleh` → `ServiceRequest.category.coding` (99) |
| 10 | 111–125 | Encounter | – | – | `nama_fasyankes` → `Encounter.serviceProvider.reference` (145) 🔎 lookup master data |
| 11 | 127–133 | Condition | Z20.1 | Contact with and exposure to tuberculosis | – |
| 12 | 147–158 | Observation | 225368008 | Contact tracing | `identitas_kontak_metode_ik` → `Observation.valueCodeableConcept.coding` (150)<br>`tanggal_investigasi` → `Observation.effectiveDateTime` (155) |
| 13 | 160–171 | Observation | SP000369 | Kontak Dengan Penderita TBC | _Kontak Dengan Penderita TBC_ → `Observation.status` (160, tanpa BQ)<br>`identitas_kontak_kontak_serumah` → `Observation.valueCodeableConcept.coding` (163)<br>`identitas_kontak_kontak_erat` → `Observation.valueCodeableConcept.coding` (164) |
| 14 | 173–216 | QuestionnaireResponse | – | – | `hasil_skrining_batuk` → `QuestionnaireResponse.item.text` (184)<br>`hasil_skrining_gejala_lain_sesak_napas` → `QuestionnaireResponse.item.item.text` (189)<br>`hasil_skrining_gejala_lain_berkeringat_malam_hari_tanpa_kegiatan` → `QuestionnaireResponse.item.item.text` (192)<br>`hasil_skrining_gejala_lain_demam_meriang_1_bulan` → `QuestionnaireResponse.item.item.text` (195)<br>`hasil_skrining_faktor_risiko_dm` → `QuestionnaireResponse.item.item.text` (200)<br>`hasil_skrining_faktor_risiko_lansia_60_th` → `QuestionnaireResponse.item.item.text` (203)<br>`hasil_skrining_faktor_risiko_ibu_hamil` → `QuestionnaireResponse.item.item.text` (206)<br>`hasil_skrining_faktor_risiko_perokok` → `QuestionnaireResponse.item.item.text` (209)<br>`hasil_skrining_faktor_risiko_pernah_berobat_tbc_tapi_tidak_tuntas` → `QuestionnaireResponse.item.item.text` (212)<br>`memenuhi_syarat_rujukan_pemeriksaan_terduga` → `QuestionnaireResponse.item.text` (215) |
| 15 | 219–230 | Observation | SP000206 | Dirujuk Pemeriksaan Terduga TBC | `dirujuk_pemeriksaan_terduga_tbc` → `Observation.valueBoolean` (222) |
| 16 | 232–243 | Observation | 171400006 | Examination for suspected tuberculosis | `diperiksa_terduga_tbc` → `Observation.valueBoolean` (235) |
| 17 | 245–256 | Observation | SP000207 | Hasil Pemeriksaan Terduga | _Hasil Pemeriksaan Terduga_ → `Observation.status` (245, tanpa BQ)<br>`hasil_pemeriksaan_terduga_sakit_tbc` → `Observation.valueCodeableConcept.coding` (248)<br>`hasil_pemeriksaan_terduga_tidak_tbc` → `Observation.valueCodeableConcept.coding` (249) |
| 18 | 258–269 | Observation | SP000209 | Memenuhi syarat rujukan pemeriksaan Eligibilitas TPT | `memenuhi_syarat_rujukan_pemeriksaan_eligibilitas_tpt` → `Observation.valueBoolean` (261) |
| 19 | 271–282 | Observation | SP000210 | Kesimpulan Hasil Pemeriksaan Eligibilitas TPT | `kesimpulan_hasil_pemeriksaan_eligibilitas_tpt` → `Observation.status` (271)<br>`memenuhi_syarat_tpt` → `Observation.valueCodeableConcept.coding` (274) |
| 20 | 284–295 | Observation | SP000212 | Tanggal Pemberian TPT | _Tanggal Pemberian TPT_ → `Observation.status` (284, tanpa BQ)<br>`tanggal_pemberian_tpt__5_th` → `Observation.valueDateTime` (287)<br>`tanggal_pemberian_tpt__5_th_1` → `Observation.valueDateTime` (288) |
| 21 | 297–314 | Observation | SP000213 | Hasil Akhir TPT | _Hasil Akhir TPT_ → `Observation.valueString` (300, tanpa BQ)<br>`hasil_akhir_tpt__5_th` → `Observation.valueCodeableConcept.coding` (301)<br>`hasil_akhir_tpt__5_th_1` → `Observation.valueCodeableConcept.coding` (302) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 14 |
| Group | 1 |
| RelatedPerson | 1 |
| Patient | 1 |
| ServiceRequest | 1 |
| Encounter | 1 |
| Condition | 1 |
| QuestionnaireResponse | 1 |
| **Total** | **21** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 13 | Observation | `Observation.code.coding` | SP000373 | Kader Kesehatan | http://terminology.kemkes.go.id/sp |
| 2 | 34 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 3 | 48 | Observation | `Observation.code.coding` | 106229004 | Qualifier for type of diagnosis | http://snomed.info/sct |
| 4 | 49 | Observation | `Observation.valueCodeableConcept.coding` | tb-bac | Terkonfirmasi bakteriologis | http://terminology.kemkes.go.id/CodeSystem/tb-case-definition |
| 5 | 50 | Observation | `Observation.valueCodeableConcept.coding` | tb-clin | Terdiagnosis klinis | http://terminology.kemkes.go.id/CodeSystem/tb-case-definition |
| 6 | 62 | Observation | `Observation.code.coding` | 415759006 | Tuberculosis index case | http://snomed.info/sct |
| 7 | 63 | Observation | `Observation.valueCodeableConcept.coding` | TB-SO | Tuberkulosis Sensitif Obat | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 8 | 64 | Observation | `Observation.valueCodeableConcept.coding` | TB-RO | Tuberkulosis Resisten Obat | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 9 | 87 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 10 | 103 | ServiceRequest | `ServiceRequest.code.coding` | 185389009 | Follow-up visit | http://snomed.info/sct |
| 11 | 104 | ServiceRequest | `ServiceRequest.code.coding` | 737492002 | Outpatient care management | http://snomed.info/sct |
| 12 | 129 | Condition | `Condition.code.coding` | Z20.1 | Contact with and exposure to tuberculosis | http://hl7.org/fhir/sid/icd-10 |
| 13 | 149 | Observation | `Observation.code.coding` | 225368008 | Contact tracing | http://snomed.info/sct |
| 14 | 150 | Observation | `Observation.valueCodeableConcept.coding` | SP000200 | Invitasi kontak | http://terminology.kemkes.go.id/sp |
| 15 | 151 | Observation | `Observation.valueCodeableConcept.coding` | 439708006 | Home visit | http://snomed.info/sct |
| 16 | 162 | Observation | `Observation.code.coding` | SP000369 | Kontak Dengan Penderita TBC | http://terminology.kemkes.go.id/sp |
| 17 | 163 | Observation | `Observation.valueCodeableConcept.coding` | SP000201 | Kontak Serumah | http://terminology.kemkes.go.id/sp |
| 18 | 164 | Observation | `Observation.valueCodeableConcept.coding` | SP000202 | Kontak Erat | http://terminology.kemkes.go.id/sp |
| 19 | 221 | Observation | `Observation.code.coding` | SP000206 | Dirujuk Pemeriksaan Terduga TBC | http://terminology.kemkes.go.id/sp |
| 20 | 234 | Observation | `Observation.code.coding` | 171400006 | Examination for suspected tuberculosis | http://snomed.info/sct |
| 21 | 247 | Observation | `Observation.code.coding` | SP000207 | Hasil Pemeriksaan Terduga | http://terminology.kemkes.go.id/sp |
| 22 | 248 | Observation | `Observation.valueCodeableConcept.coding` | 56717001 | Tuberculosis | http://snomed.info/sct |
| 23 | 249 | Observation | `Observation.valueCodeableConcept.coding` | SP000208 | Tidak TBC | http://terminology.kemkes.go.id/sp |
| 24 | 260 | Observation | `Observation.code.coding` | SP000209 | Memenuhi syarat rujukan pemeriksaan Eligibilitas TPT | http://terminology.kemkes.go.id/sp |
| 25 | 273 | Observation | `Observation.code.coding` | SP000210 | Kesimpulan Hasil Pemeriksaan Eligibilitas TPT | http://terminology.kemkes.go.id/sp |
| 26 | 274 | Observation | `Observation.valueCodeableConcept.coding` | SP000211 | Memenuhi syarat TPT | http://terminology.kemkes.go.id/sp |
| 27 | 275 | Observation | `Observation.valueCodeableConcept.coding` | SP000374 | Tidak Memenuhi Syarat TPT | http://terminology.kemkes.go.id/sp |
| 28 | 286 | Observation | `Observation.code.coding` | SP000212 | Tanggal Pemberian TPT | http://terminology.kemkes.go.id/sp |
| 29 | 299 | Observation | `Observation.code.coding` | SP000213 | Hasil Akhir TPT | http://terminology.kemkes.go.id/sp |
| 30 | 301 | Observation | `Observation.valueCodeableConcept.coding` | 371001000 | Patient cured | http://snomed.info/sct |
| 31 | 303 | Observation | `Observation.valueCodeableConcept.coding` | 182992009 | Treatment completed | http://snomed.info/sct |
| 32 | 304 | Observation | `Observation.valueCodeableConcept.coding` | CP000094 | Pengobatan Gagal | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 33 | 305 | Observation | `Observation.valueCodeableConcept.coding` | 419099009 | Dead | http://snomed.info/sct |
| 34 | 306 | Observation | `Observation.valueCodeableConcept.coding` | 399307001 | Lost to follow-up | http://snomed.info/sct |
| 35 | 307 | Observation | `Observation.valueCodeableConcept.coding` | CP000096 | Tidak dievaluasi/pindah | http://terminology.kemkes.go.id/CodeSystem/clinical-term |

### Code per CodeSystem

| CodeSystem | Jumlah | Code |
|---|---|---|
| http://terminology.kemkes.go.id/sp | 14 | SP000373, SP000200, SP000369, SP000201, SP000202, SP000206, SP000207, SP000208, SP000209, SP000210, SP000211, SP000374, SP000212, SP000213 |
| http://snomed.info/sct | 14 | 424144002, 106229004, 415759006, 424144002, 185389009, 737492002, 225368008, 439708006, 171400006, 56717001, 371001000, 182992009, 419099009, 399307001 |
| http://terminology.kemkes.go.id/CodeSystem/tb-case-definition | 2 | tb-bac, tb-clin |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 2 | TB-SO, TB-RO |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 2 | CP000094, CP000096 |
| http://hl7.org/fhir/sid/icd-10 | 1 | Z20.1 |
| **Total** | **35** | |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
