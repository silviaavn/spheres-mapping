# Output Form: SITB - TB 15 (Pemeriksaan Eligibilitas TPT)

Sumber: `mapping/phdt-data-dictionary-sitb-tb15.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-sitb-tb15.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 13 |
| Code (`jumlah code` = 1) | 109 |
| Code unik (code + CodeSystem) | 107 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 3 |
| Variabel BQ (unik) | 6 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–8 | Patient | – | – | _NIK (Nomor Induk Kependudukan)_ → `Patient.identifier.value` (5, tanpa BQ)<br>_Nama Lengkap Pasien_ → `Patient.name.text` (6, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (7, tanpa BQ)<br>_Provinsi_ → `Patient.address.extension.url` (23, tanpa BQ)<br>_Kabupaten/Kota_ → `Patient.address.extension.url` (26, tanpa BQ)<br>_Kecamatan_ → `Patient.address.extension.url` (29, tanpa BQ)<br>_Kelurahan_ → `Patient.address.extension.url` (32, tanpa BQ)<br>_Alamat Lengkap Penerima TPT_ → `Patient.address.line` (35, tanpa BQ) |
| 2 | 9–20 | Observation | 424144002 | Current chronological age | _Umur (Tahun)_ → `Observation.valueQuantity.value` (12, tanpa BQ) |
| 3 | 82–94 | Observation | SP000450 | Faktor Risiko Tuberkulosis | _Faktor risiko_ → `Observation.valueCodeableConcept.coding` (85, tanpa BQ) |
| 4 | 95–107 | Observation | 415759006 | Tuberculosis index case | _Tipe TBC Kasus Indeks_ → `Observation.valueCodeableConcept.coding` (98, tanpa BQ) |
| 5 | 108–120 | Observation | 106229004 | Qualifier for type of diagnosis | `{tipe_diagnosis_tbc}` → `Observation.valueCodeableConcept.coding` (111)<br>`{tipe_diagnosis_tbc}` → `Observation.valueCodeableConcept.coding` (112)<br>`{nama_lengkap_pasien}` → `Observation.subject.display` (115)<br>`{tanggal_mulai_pengobatan}` → `Observation.effectiveDateTime` (117)<br>`{nama_lengkap_pasien}` → `Observation.issued` (118) |
| 6 | 121–133 | QuestionnaireResponse | – | – | _Lokasi Anatomi TBC Kasus Indeks_ → `QuestionnaireResponse.questionnaire` (121, tanpa BQ) |
| 7 | 134–146 | Observation | 23539-0 | Tuberculosis reaction wheal [Diameter] --3 days post dose mammalian tuberculin intradermal | _Hasil Uji Tuberkulin_ → `Observation.status` (134, tanpa BQ)<br>`{hasil_pemeriksaan_tuberkulin}` → `Observation.valueCodeableConcept.coding` (137)<br>`{hasil_pemeriksaan_tuberkulin}` → `Observation.valueCodeableConcept.coding` (138)<br>`{nama_lengkap_pasien}` → `Observation.subject.display` (141)<br>`{tanggal_mulai_pengobatan}` → `Observation.effectiveDateTime` (143)<br>`{tanggal_mulai_pengobatan}` → `Observation.issued` (144) |
| 8 | 147–159 | Observation | 71773-6 | Mycobacterium tuberculosis stimulated gamma interferon [Interpretation] in Blood Qualitative | _Hasil Uji IGRA_ → `Observation.status` (147, tanpa BQ)<br>`{hasil_pemeriksaan_igra}` → `Observation.valueCodeableConcept.coding` (150)<br>`{hasil_pemeriksaan_igra}` → `Observation.valueCodeableConcept.coding` (151)<br>`{nama_lengkap_pasien}` → `Observation.subject.display` (154)<br>`{tanggal_mulai_pengobatan}` → `Observation.effectiveDateTime` (156)<br>`{tanggal_mulai_pengobatan}` → `Observation.issued` (157) |
| 9 | 161–173 | Observation | SP000723 | Pemeriksaan TBST | _Hasil Uji TBST_ → `Observation.valueCodeableConcept.coding` (164, tanpa BQ) |
| 10 | 174–186 | Observation | 24648-8 | XR Chest PA upright | _Hasil Foto Toraks_ → `Observation.status` (174, tanpa BQ)<br>`{hasil_pemeriksaan_foto_toraks}` → `Observation.valueCodeableConcept.coding` (177)<br>`{hasil_pemeriksaan_foto_toraks}` → `Observation.valueCodeableConcept.coding` (178)<br>`{hasil_pemeriksaan_foto_toraks}` → `Observation.dataAbsentReason` (179)<br>`{nama_lengkap_pasien}` → `Observation.subject.display` (181)<br>`{tanggal_mulai_pengobatan}` → `Observation.effectiveDateTime` (183)<br>`{tanggal_mulai_pengobatan}` → `Observation.issued` (184) |
| 11 | 187–281 | CarePlan | – | – | _Tanggal mulai TPT_ → `CarePlan.period.start` (193, tanpa BQ)<br>_Hasil Akhir TPT - Tanggal_ → `CarePlan.period.end` (194, tanpa BQ)<br>_Paduan TPT_ → `CarePlan.activity.detail.code.coding` (199, tanpa BQ)<br>_Hasil Akhir TPT - Hasil_ → `CarePlan.activity.outcomeCodeableConcept.coding` (276, tanpa BQ) |
| 12 | 282–303 | Encounter | – | – | _//id puskesmas_ → `Encounter.serviceProvider.reference` (303, tanpa BQ) |
| 13 | 304–310 | Condition | 1237025001 | At increased risk of exposure to Mycobacterium tuberculosis complex | – |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 8 |
| Patient | 1 |
| QuestionnaireResponse | 1 |
| CarePlan | 1 |
| Encounter | 1 |
| Condition | 1 |
| **Total** | **13** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 11 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 2 | 84 | Observation | `Observation.code.coding` | SP000450 | Faktor Risiko Tuberkulosis | http://terminology.kemkes.go.id/sp |
| 3 | 85 | Observation | `Observation.valueCodeableConcept.coding` | SP000201 | Kontak serumah | http://terminology.kemkes.go.id/sp |
| 4 | 86 | Observation | `Observation.valueCodeableConcept.coding` | OV000431 | Siswa Berasrama | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 5 | 87 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 6 | 97 | Observation | `Observation.code.coding` | 415759006 | Tuberculosis index case | http://snomed.info/sct |
| 7 | 98 | Observation | `Observation.valueCodeableConcept.coding` | TB-SO | Tuberkulosis Sensitif Obat | https://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 8 | 99 | Observation | `Observation.valueCodeableConcept.coding` | TB-RO | Tuberkulosis Resisten Obat | https://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 9 | 110 | Observation | `Observation.code.coding` | 106229004 | Qualifier for type of diagnosis | http://snomed.info/sct |
| 10 | 111 | Observation | `Observation.valueCodeableConcept.coding` | tb-bac | Terkonfirmasi bakteriologis | http://terminology.kemkes.go.id/CodeSystem/tb-case-definition |
| 11 | 112 | Observation | `Observation.valueCodeableConcept.coding` | tb-clin | Terdiagnosis klinis | http://terminology.kemkes.go.id/CodeSystem/tb-case-definition |
| 12 | 132 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 154283005 | Pulmonary tuberculosis | http://snomed.info/sct |
| 13 | 133 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 423997002 | Tuberculosis, extrapulmonary | http://snomed.info/sct |
| 14 | 136 | Observation | `Observation.code.coding` | 23539-0 | Tuberculosis reaction wheal [Diameter] --3 days post dose mammalian tuberculin intradermal | http://loinc.org |
| 15 | 137 | Observation | `Observation.valueCodeableConcept.coding` | 268376005 | Mantoux: positive | http://snomed.info/sct |
| 16 | 138 | Observation | `Observation.valueCodeableConcept.coding` | 268375009 | Mantoux: negative | http://snomed.info/sct |
| 17 | 149 | Observation | `Observation.code.coding` | 71773-6 | Mycobacterium tuberculosis stimulated gamma interferon [Interpretation] in Blood Qualitative | http://loinc.org |
| 18 | 150 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 19 | 151 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 20 | 163 | Observation | `Observation.code.coding` | SP000723 | Pemeriksaan TBST | http://terminology.kemkes.go.id/sp |
| 21 | 164 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 22 | 165 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 23 | 176 | Observation | `Observation.code.coding` | 24648-8 | XR Chest PA upright | http://loinc.org |
| 24 | 177 | Observation | `Observation.valueCodeableConcept.coding` | 707307002 | Tuberculosis screening chest X-ray abnormal | http://snomed.info/sct |
| 25 | 178 | Observation | `Observation.valueCodeableConcept.coding` | 707308007 | Tuberculosis screening chest X-ray normal | http://snomed.info/sct |
| 26 | 199 | CarePlan | `CarePlan.activity.detail.code.coding` | CP000005 | Paduan Pengobatan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 27 | 200 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000015 | 2(HRZE)/4(HR)3 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 28 | 201 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000016 | 2(HRZE)/4(HR) - KDT Dosis Harian | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 29 | 202 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000017 | 2(HRZE)S/(HRZE)/5(HRE) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 30 | 203 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000018 | 2(HRZE)S/(HRZE)/5((HR)3E3) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 31 | 204 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000019 | 2HRZE/4HR | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 32 | 205 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000020 | 2HRZES/HRZE/ 5H3R3E3 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 33 | 206 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000021 | 2(HRZ)/4(HR) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 34 | 207 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000022 | 2(HRZ)/4(HR) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 35 | 208 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000023 | Km Cs Eto Lfx Z VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 36 | 209 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000024 | Km Cs Eto Lfx PAS E Z VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 37 | 210 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000025 | Km Cs Eto Lfx E Z VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 38 | 211 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000026 | Km Cs Eto Mfx PAS Z VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 39 | 212 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000027 | Km Cs Eto Mfx PAS E VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 40 | 213 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000028 | Cm Cs Eto Lfx E Z Vit B6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 41 | 214 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000029 | Cm Cs Eto Lfx PAS Z VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 42 | 215 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000030 | Cm Cs Eto Mfx Z VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 43 | 216 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000031 | Cm Cs Eto Mfx PAS Z VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 44 | 217 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000032 | Km Eto Cs PAS Z Bdq | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 45 | 218 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000033 | Lfx Eto Cs PAS Z Bdq | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 46 | 219 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000034 | Eto Cs PAS Z Bdq Lnz Clf | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 47 | 220 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000035 | Km Lfx (Eto/CS/PAS) Z Bdq (Lnz/Clf) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 48 | 221 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000036 | 5 Km Mfx(h) Eto Cfz Z H(h) E/ 5Mfx(h) Cfz Z E | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 49 | 222 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000037 | 6 Dlm Lfx Eto Cs ZE B6/ 18 Lfx Eto Cs ZE B6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 50 | 223 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000038 | 10 Cm Dlm Lzd Eto Cs Z E B6/14 Lzd Eto Cs Z E B6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 51 | 224 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000039 | 6 Dlm Lzd Cfz Eto Cs PAS ZE B6/ 18 lzd Cfz Eto Cs PAS Z E B6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 52 | 225 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000040 | Etambutol | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 53 | 226 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000041 | Paduan TPT 6Lfx 250 mg + E 400 mg Dewasa | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 54 | 227 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000042 | 6 Bdq-Lfx-Lzd-Cfz-Cs-VitB6 / 14 Lfx-Cfz-Cs-VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 55 | 228 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000043 | 6 Bdq-Lfx-Cfz-Cs-E -VitB6/ 14 Lfx-Cfz-Cs-E-VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 56 | 229 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000044 | 6 Bdq-Lfx-Lzd-Cfz-E / 14 Lfx-Cfz-E | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 57 | 230 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000045 | 6 Bdq-Mfx-Lzd-Cfz-E / 14 Mfx-Cfz-E | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 58 | 231 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000046 | 6 Bdq-Lzd-Cfz-Cs-E-VitB6 / 14 Lzd-Cfz-Cs-E -VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 59 | 232 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000047 | 6 Bdq-Lzd-Cfz-Cs-Eto / 14 Lzd-Cfz-Cs-Eto- Vit B6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 60 | 233 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000048 | 6 Dlm-Lfx-Lzd-Clz-Cs / 14 Lfx-Lzd-Clz-Cs -VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 61 | 234 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000049 | 20 Lfx-Lzd-Cfz-Cs-Eto -VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 62 | 235 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000050 | 20 Mfx-Lzd-Cfz-Cs-E -VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 63 | 236 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000051 | 20 Mfx-Lzd-Cfz-Cs-Z -VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 64 | 237 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000052 | 6 Lfx-Lzd-Cfz-Cs-Amk-VitB6 / 14 Lfx-Lzd-Clz-Cs-VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 65 | 238 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000053 | 6 Lfx-Lzd-Cfz-Cs-S-VitB6 / 14 Lfx-Lzd-Clz-Cs-VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 66 | 239 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000054 | 6 Lfx-Lzd-Cfz-Eto-PAS / 14 Lfx-Lzd-Clz-Eto | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 67 | 240 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000055 | 6 Dlm-Lzd-Cfz-Cs-E / 14 Lzd-Clz-Cs-E-Vit B6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 68 | 241 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000056 | Pro TB 3 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 69 | 242 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000057 | 6 Bdq-Lfx-Lzd-Cfz-H(Hdose)-Z-E/5 Lfx-Cfz-Z-E | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 70 | 243 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000058 | 6 Dlm-Lzd-Cfz-Cs-E / 14 Lzd-Clz-Cs-E-Vit B6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 71 | 244 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000059 | 6 Dlm-Lfx-Lzd-Clz-Cs / 14 Lfx-Lzd-Clz-Cs -VitB6 | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 72 | 245 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000060 | 6 Bdq-Lfx-Eto-E-Z-Hh-Cfz/ 5 Lfx)-Cfz-Z-E (STR Non Inj) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 73 | 246 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000061 | 6 Bdq-Mfx-Eto-E-Z-Hh-Cfz/ 5-Mfx-Cfz-Z-E (STR Non Inj) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 74 | 247 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000062 | Paduan TPT 6H 100 mg (INH) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 75 | 248 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000063 | Paduan TPT 3HP Lepasan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 76 | 249 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000064 | Paduan TPT 6H 300 mg (INH) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 77 | 250 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000065 | Paduan TPT 6Lfx 250mg | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 78 | 251 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000066 | Paduan TPT 3HR KDT | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 79 | 252 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000067 | Paduan TPT 3HR KDT | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 80 | 253 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000068 | 5 Lfx-Lzd-Cfz-Cs / 5 Lfx-Cfz-Cs | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 81 | 254 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000069 | 6 Lfx-Lzd-Cfz-Cs-Eto / 12 Lfx-Cfz-Cs-Eto | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 82 | 255 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000070 | 6 Lzd-Cfz-Cs-Eto / 5 Cfz-Cs-Eto | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 83 | 256 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000071 | 6 Lzd-Cfz-Cs-Eto / 12 Cfz-Cs-Eto | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 84 | 257 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000072 | 5 Lfx-Lzd-Cfz-Cs-Dlm / 5 Lfx-Cfz-Cs | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 85 | 258 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000073 | 6 Lfx-Lzd-Cfz-Cs-Dlm / 12 Lfx-Cfz-Cs | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 86 | 259 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000074 | 5 Lzd-Cfz-Cs-Dlm-Eto/5 Cfz-Cs-Eto | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 87 | 260 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000075 | 6 Lzd-Cfz-Cs-Dlm-Eto/ 12 Cfz-Cs-Eto | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 88 | 261 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000076 | 6 Bdq-Lfx-Lzd-Cfz-Cs / 5 Lfx-Cfz- Cs | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 89 | 262 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000077 | 6 Bdq-Lfx-Lzd-Cfz-Cs / 12 Lfx-Cfz-Cs | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 90 | 263 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000078 | 6 Bdq-Lzd-Cfz-Cs-PAS / 5 Cfz-Cs-PAS | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 91 | 264 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000079 | 6 Bdq-Lzd-Cfz-Cs- PAS / 12 Cfz-Cs-PAS | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 92 | 265 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000080 | Paduan TPT 6Lfx 100 mg + E 100 mg | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 93 | 266 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000081 | Paduan TPT 6Lfx 100mg | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 94 | 267 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000082 | Paduan TPT 3HR 300mg/450mg Lepasan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 95 | 268 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000083 | Paduan TPT 3HR 300mg/600mg Lepasan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 96 | 269 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000084 | RHZE (150/75/400/275) + Levofloxacin | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 97 | 270 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000085 | Bedaquline Pretomanid Linezolid (BPAL) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 98 | 271 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000086 | Bedaquline Pretomanid Linezolid Moxifloxacin (BPALM) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 99 | 272 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000087 | Paduan TPT 1HP 300mg/300mg Lepasan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 100 | 273 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000088 | Paduan TPT 1HP 300mg/150mg Lepasan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 101 | 274 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000089 | 6 BDQ-Lfx-Cfz-Hdt-Z-E-Lzd(2 bulan)/ 5 Lfx-Cfz-Z-E | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 102 | 275 | CarePlan | `CarePlan.activity.detail.productCodeableConcept.coding` | CP000090 | 2HPMZ/2HPM | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 103 | 276 | CarePlan | `CarePlan.activity.outcomeCodeableConcept.coding` | 371001000 | Patient cured | http://snomed.info/sct |
| 104 | 277 | CarePlan | `CarePlan.activity.outcomeCodeableConcept.coding` | 182992009 | Treatment completed | http://snomed.info/sct |
| 105 | 278 | CarePlan | `CarePlan.activity.outcomeCodeableConcept.coding` | CP000094 | Pengobatan Gagal | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 106 | 279 | CarePlan | `CarePlan.activity.outcomeCodeableConcept.coding` | 419099009 | Dead | http://snomed.info/sct |
| 107 | 280 | CarePlan | `CarePlan.activity.outcomeCodeableConcept.coding` | 399307001 | Lost to follow-up | http://snomed.info/sct |
| 108 | 281 | CarePlan | `CarePlan.activity.outcomeCodeableConcept.coding` | CP000096 | Tidak dievaluasi/pindah | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 109 | 306 | Condition | `Condition.code.coding` | 1237025001 | At increased risk of exposure to Mycobacterium tuberculosis complex | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 80 |
| http://snomed.info/sct | 15 |
| http://loinc.org | 7 |
| http://terminology.kemkes.go.id/sp | 3 |
| https://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 2 |
| http://terminology.kemkes.go.id/CodeSystem/tb-case-definition | 2 |
| **Total** | **109** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 38 | – | Kode Fasyankes | Organization | `Organization.identifier` |
| 39 | – | Jenis Fasyankes | Organization | `Organization.type` |
| 41 | – | Kepemilikan Fasyankes | Organization | `Organization.type` |
| 43 | – | Nama Fasyankes | Organization | `Organization.name` |
| 48 | – | Provinsi Fasyankes | Organization | `Organization.address.extension.extension.valueCode` |
| 51 | – | Kabupaten Fasyankes | Organization | `Organization.address.extension.extension.valueCode` |
