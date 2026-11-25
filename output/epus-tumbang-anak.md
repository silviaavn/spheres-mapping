# Output Form: ePuskesmas KIA Harian Tumbuh Kembang Anak

Sumber: `mapping/phdt-data-dictionary-epus-tumbang-anak.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-epus-tumbang-anak.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 19 |
| Code (`jumlah code` = 1) | 62 |
| Code unik (code + CodeSystem) | 45 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 8 |
| Variabel BQ (unik) | 0 |
| Variabel raw (variabel dictionary; belum ada file mentah) | 34 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–15 | Condition | 404684003 | Clinical finding | _Keluhan Utama_ → `Condition.code.text` (5, tanpa BQ)<br>_Dokter/Tenaga Medis_ → `Condition.recorder.display` (12, tanpa BQ)<br>_Perawat / Bidan / Nutrisionist / Sanitarian_ → `Condition.asserter.display` (14, tanpa BQ)<br>_Masalah Pada Anak_ → `Condition.note` (15, tanpa BQ) |
| 2 | 16–27 | Observation | 29463-7 | Body weight | _BB_ → `Observation.valueQuantity.value` (19, tanpa BQ) |
| 3 | 28–40 | Observation | 8308-9 | Body height --standing | _PB/TB_ → `Observation.valueQuantity.value` (32, tanpa BQ) |
| 4 | 41–52 | Observation | 50373000 | Body height measure | _Cara Ukur_ → `Observation.status` (41, tanpa BQ) |
| 5 | 53–71 | Observation | 1153600001 | Weight for height z-score | _BB/TB atau BB/PB_ → `Observation.valueQuantity.value` (57, tanpa BQ) |
| 6 | 72–83 | Observation | OC000012 | Kenaikan Berat Badan Adekuat | _Kenaikan Berat Badan Adekuat_ → `Observation.valueBoolean` (74, tanpa BQ) |
| 7 | 84–110 | Observation | 1153590000 | Length for age z-score | _PB/U atau TB/U_ → `Observation.valueRange.high.value` (88, tanpa BQ) |
| 8 | 111–126 | Observation | 1153593003 | Weight for age z-score | _BB/U_ → `Observation.valueQuantity.value` (114, tanpa BQ) |
| 9 | 127–138 | Observation | 9843-4 | Head Occipital-frontal circumference | _LKA_ → `Observation.valueQuantity.value` (130, tanpa BQ) |
| 10 | 139–159 | Observation | 1153594009 | Head circumference for age z-score | _LKA/U_ → `Observation.valueRange.high.value` (142, tanpa BQ) |
| 11 | 160–168 | Condition | 404684003 | Clinical finding | _Ada keluhan_ → `Condition.clinicalStatus.coding` (160, tanpa BQ)<br>_Detail Keluhan_ → `Condition.code.text` (164, tanpa BQ) |
| 12 | 169–235 | QuestionnaireResponse | – | – | _Perkembangan Anak Sesuai_ → `QuestionnaireResponse.item.text` (180, tanpa BQ)<br>_Perkembangan Anak Meragukan_ → `QuestionnaireResponse.item.text` (188, tanpa BQ)<br>_Perkembangan Anak Penyimpangan_ → `QuestionnaireResponse.item.text` (202, tanpa BQ)<br>_Daya Dengar_ → `QuestionnaireResponse.questionnaire` (215, tanpa BQ)<br>_Daya Lihat_ → `QuestionnaireResponse.questionnaire` (222, tanpa BQ)<br>_Perilaku dan Emosional_ → `QuestionnaireResponse.questionnaire` (229, tanpa BQ) |
| 13 | 247–258 | Observation | 1145307003 | Exclusively breastfed | _ASI Eksklusif_ → `Observation.valueBoolean` (250, tanpa BQ) |
| 14 | 259–270 | Observation | OC000009 | Makanan Pendamping ASI (MPASI) | _Mendapat Makanan Pendamping ASI_ → `Observation.valueBoolean` (262, tanpa BQ) |
| 15 | 271–291 | QuestionnaireResponse | – | – | _Autisme_ → `QuestionnaireResponse.questionnaire` (271, tanpa BQ)<br>_GPPH_ → `QuestionnaireResponse.questionnaire` (279, tanpa BQ)<br>_Kesimpulan_ → `QuestionnaireResponse.questionnaire` (286, tanpa BQ) |
| 16 | 292–302 | Procedure | 408429008 | Recommendation to caregiver regarding child's development program | _Konseling Stimulasi Bagi Ibu/Pengasuh_ → `Procedure.category.coding` (292, tanpa BQ) |
| 17 | 303–316 | Observation | SP000061 | Intervensi Dini Masalah Perkembangan Anak | _Intervensi Stimulasi Perkembangan_ → `Observation.valueCodeableConcept` (306, tanpa BQ) |
| 18 | 317–327 | Observation | SP000064 | Tindakan Pengobatan Lain | _Tindakan Pengobatan Lain_ → `Observation.valueString` (320, tanpa BQ) |
| 19 | 328–339 | Observation | OC000034 | Surat Pengantar Rujukan | _Dirujuk dengan Surat Rujukan ke_ → `Observation.valueBoolean` (331, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 14 |
| Condition | 2 |
| QuestionnaireResponse | 2 |
| Procedure | 1 |
| **Total** | **19** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 4 | Condition | `Condition.code.coding` | 404684003 | Clinical finding | http://snomed.info/sct |
| 2 | 18 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 3 | 30 | Observation | `Observation.code.coding` | 8308-9 | Body height --standing | http://loinc.org |
| 4 | 31 | Observation | `Observation.code.coding` | 8306-3 | Body height --lying | http://loinc.org |
| 5 | 43 | Observation | `Observation.code.coding` | 50373000 | Body height measure | http://loinc.org |
| 6 | 44 | Observation | `Observation.method.coding` | 10904000 | Standing position | http://snomed.info/sct |
| 7 | 45 | Observation | `Observation.method.coding` | 102538003 | Recumbent body position | http://snomed.info/sct |
| 8 | 55 | Observation | `Observation.code.coding` | 1153600001 | Weight for height z-score | http://snomed.info/sct |
| 9 | 56 | Observation | `Observation.code.coding` | 1153598007 | Weight for length z score | http://snomed.info/sct |
| 10 | 59 | Observation | `Observation.interpretation.coding` | 248324001 | Well nourished | http://snomed.info/sct |
| 11 | 60 | Observation | `Observation.interpretation.coding` | OI000001 | Gizi Buruk | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 12 | 61 | Observation | `Observation.interpretation.coding` | 248325000 | Undernourished | http://snomed.info/sct |
| 13 | 62 | Observation | `Observation.interpretation.coding` | 238131007 | Overweight | http://snomed.info/sct |
| 14 | 63 | Observation | `Observation.interpretation.coding` | 414915002 | Obese | http://snomed.info/sct |
| 15 | 64 | Observation | `Observation.interpretation.coding` | OI000004 | Risiko Gizi Lebih | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 16 | 73 | Observation | `Observation.code.coding` | OC000012 | Kenaikan Berat Badan Adekuat | http://terminology.kemkes.go.id/CodeSystem/ |
| 17 | 86 | Observation | `Observation.code.coding` | 1153590000 | Length for age z-score | http://snomed.info/sct |
| 18 | 87 | Observation | `Observation.code.coding` | 1153604005 | Body height for age z score | http://snomed.info/sct |
| 19 | 90 | Observation | `Observation.interpretation.coding` | OI000011 | Sangat Pendek | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 20 | 95 | Observation | `Observation.interpretation.coding` | 444000005 | Short stature for age | http://snomed.info/sct |
| 21 | 100 | Observation | `Observation.interpretation.coding` | 17489000 | Body height normal for age | http://snomed.info/sct |
| 22 | 103 | Observation | `Observation.interpretation.coding` | 83077003 | Tall for age | http://snomed.info/sct |
| 23 | 113 | Observation | `Observation.code.coding` | 1153593003 | Weight for age z-score | http://snomed.info/sct |
| 24 | 116 | Observation | `Observation.interpretation.coding` | 248342006 | Underweight | http://snomed.info/sct |
| 25 | 117 | Observation | `Observation.interpretation.coding` | 43664005 | Normal weight | http://snomed.info/sct |
| 26 | 118 | Observation | `Observation.interpretation.coding` | OI000010 | Risiko Berat Badan Lebih | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 27 | 119 | Observation | `Observation.interpretation.coding` | OI000007 | Berat Badan Sangat Kurang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 28 | 129 | Observation | `Observation.code.coding` | 9843-4 | Head Occipital-frontal circumference | http://loinc.org |
| 29 | 141 | Observation | `Observation.code.coding` | 1153594009 | Head circumference for age z-score | http://loinc.org |
| 30 | 144 | Observation | `Observation.interpretation.coding` | 1148757008 | Microcephaly | http://snomed.info/sct |
| 31 | 149 | Observation | `Observation.interpretation.coding` | 840673007 | Normal head | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 32 | 152 | Observation | `Observation.interpretation.coding` | 1145403003 | Macrocephaly | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 33 | 163 | Condition | `Condition.code.coding` | 404684003 | Clinical finding | http://snomed.info/sct |
| 34 | 197 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 170218003 | Child examination: gross motor development | http://snomed.info/sct |
| 35 | 198 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 170219006 | Child examination: fine motor development | http://snomed.info/sct |
| 36 | 199 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000062 | Pemeriksaan Anak: Bicara dan Bahasa | http://terminology.kemkes.go.id/sp |
| 37 | 200 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000155 | Pemeriksaan Anak: Sosialisasi dan Kemandirian | http://terminology.kemkes.go.id/sp |
| 38 | 211 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 170218003 | Child examination: gross motor development | http://snomed.info/sct |
| 39 | 212 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 170219006 | Child examination: fine motor development | http://snomed.info/sct |
| 40 | 213 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000062 | Pemeriksaan Anak: Bicara dan Bahasa | http://terminology.kemkes.go.id/sp |
| 41 | 214 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000155 | Pemeriksaan Anak: Sosialisasi dan Kemandirian | http://terminology.kemkes.go.id/sp |
| 42 | 220 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 17621005 | Normal | http://snomed.info/sct |
| 43 | 221 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 410519009 | At risk | http://snomed.info/sct |
| 44 | 227 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 17621005 | Normal | http://snomed.info/sct |
| 45 | 228 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 410519009 | At risk | http://snomed.info/sct |
| 46 | 234 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 17621005 | Normal | http://snomed.info/sct |
| 47 | 235 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 410519009 | At risk | http://snomed.info/sct |
| 48 | 249 | Observation | `Observation.code.coding` | 1145307003 | Exclusively breastfed | http://snomed.info/sct |
| 49 | 261 | Observation | `Observation.code.coding` | OC000009 | Makanan Pendamping ASI (MPASI) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 50 | 276 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 17621005 | Normal | http://snomed.info/sct |
| 51 | 277 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 410519009 | At risk | http://snomed.info/sct |
| 52 | 278 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 723509005 | High risk | http://snomed.info/sct |
| 53 | 284 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 17621005 | Normal | http://snomed.info/sct |
| 54 | 285 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 410519009 | At risk | http://snomed.info/sct |
| 55 | 293 | Procedure | `Procedure.code.coding` | 408429008 | Recommendation to caregiver regarding child's development program | http://snomed.info/sct |
| 56 | 305 | Observation | `Observation.code.coding` | SP000061 | Intervensi Dini Masalah Perkembangan Anak | http://terminology.kemkes.go.id/sp |
| 57 | 306 | Observation | `Observation.valueCodeableConcept` | 170218003 | Child examination: gross motor development | http://snomed.info/sct |
| 58 | 307 | Observation | `Observation.valueCodeableConcept` | 170219006 | Child examination: fine motor development | http://snomed.info/sct |
| 59 | 308 | Observation | `Observation.valueCodeableConcept` | SP000062 | Pemeriksaan Anak: Bicara dan Bahasa | http://terminology.kemkes.go.id/sp |
| 60 | 309 | Observation | `Observation.valueCodeableConcept` | SP000155 | Pemeriksaan Anak: Sosialisasi dan Kemandirian | http://terminology.kemkes.go.id/sp |
| 61 | 319 | Observation | `Observation.code.coding` | SP000064 | Tindakan Pengobatan Lain | http://terminology.kemkes.go.id/sp |
| 62 | 330 | Observation | `Observation.code.coding` | OC000034 | Surat Pengantar Rujukan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 38 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 9 |
| http://terminology.kemkes.go.id/sp | 8 |
| http://loinc.org | 6 |
| http://terminology.kemkes.go.id/CodeSystem/ | 1 |
| **Total** | **62** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 236 | – | Jenis Skrining | – | `` |
| 244 | – | Tanggal Skrining | – | `` |
| 245 | – | Nama Petugas | – | `` |
| 246 | – | Interpretasi | – | `` |
