# Output Form: Kuapps Spheres - TB

Sumber: `mapping/phdt-data-dictionary-kuapps-spheres-tb.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-kuapps-spheres-tb.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 5 |
| Code (`jumlah code` = 1) | 47 |
| Code unik (code + CodeSystem) | 21 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 19 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 3–29 | Encounter | – | – | _Tanggal Kunjungan_ → `Encounter.period.start` (9, tanpa BQ)<br>_Nama Faskes_ → `Encounter.serviceProvider.display` (21, tanpa BQ)<br>_Apakah pengisian form real/latihan?_ → `Encounter.meta.tag` (24, tanpa BQ) |
| 2 | 30–44 | Condition | 390906007.0 | Follow-up encounter | – |
| 3 | 47–102 | Patient | – | – | – |
| 4 | 105–158 | QuestionnaireResponse | – | – | _Nomor HP Pasien/Kerabat yang terhubung ke Whatsapp_ → `QuestionnaireResponse.item.text` (116, tanpa BQ)<br>_Kepemilikan nomor HP yang terhubung dengan Whatsapp_ → `QuestionnaireResponse.item.text` (119, tanpa BQ)<br>_Sebutkan lainnya_ → `QuestionnaireResponse.item.item.text` (130, tanpa BQ)<br>_Status validasi nomor HP yang terhubung dengan Whatsapp_ → `QuestionnaireResponse.item.text` (133, tanpa BQ)<br>_Nomor HP Pasien/Kerabat yang terhubung ke jaringan selular_ → `QuestionnaireResponse.item.text` (138, tanpa BQ)<br>_Kepemilikan nomor HP yang terhubung dengan jaringan selular_ → `QuestionnaireResponse.item.text` (141, tanpa BQ)<br>_Sebutkan lainnya_ → `QuestionnaireResponse.item.item.text` (152, tanpa BQ)<br>_Status validasi nomor HP yang terhubung dengan jaringan selular_ → `QuestionnaireResponse.item.text` (155, tanpa BQ) |
| 5 | 160–241 | QuestionnaireResponse | – | – | _Apakah ada dahak yang dikumpulkan saat pasien datang ke puskesmas?_ → `QuestionnaireResponse.item.text` (171, tanpa BQ)<br>_Apa tahapan pengobatan yang sedang dijalani pasien?_ → `QuestionnaireResponse.item.text` (175, tanpa BQ)<br>_Apakah pasien mengambil obat untuk diri sendiri/diwakilkan?_ → `QuestionnaireResponse.item.text` (179, tanpa BQ)<br>_Siapa yang mewakili pasien mengambil obat?_ → `QuestionnaireResponse.item.text` (184, tanpa BQ)<br>_Sebutkan lainnya_ → `QuestionnaireResponse.item.item.text` (193, tanpa BQ)<br>_Nama orang yang mewakilkan_ → `QuestionnaireResponse.item.text` (196, tanpa BQ)<br>_Apakah pasien memiliki pengawas minum obat (PMO)?_ → `QuestionnaireResponse.item.text` (199, tanpa BQ)<br>_Siapa PMO pasien?_ → `QuestionnaireResponse.item.text` (203, tanpa BQ)<br>_Sebutkan lainnya_ → `QuestionnaireResponse.item.item.text` (212, tanpa BQ)<br>_Tanggal pengambilan obat_ → `QuestionnaireResponse.item.text` (215, tanpa BQ)<br>_Untuk berapa hari persediaan obat TB yang diberikan ke pasien?_ → `QuestionnaireResponse.item.text` (218, tanpa BQ)<br>_Apakah kunjungan ini merupakan pengambilan obat perdana?_ → `QuestionnaireResponse.item.text` (221, tanpa BQ)<br>_Berapa hari sisa obat yang dimiliki pasien sebelum mengambil obat ke puskesmas?_ → `QuestionnaireResponse.item.text` (225, tanpa BQ)<br>_Apakah selama ini OAT dikonsumsi setiap hari tanpa putus?_ → `QuestionnaireResponse.item.text` (228, tanpa BQ)<br>_Jika OAT tidak dikonsumsi setiap hari, seberapa sering pasien mengonsumsi OAT?_ → `QuestionnaireResponse.item.text` (232, tanpa BQ)<br>_Kapan tanggal pengambilan obat pasien selanjutnya?_ → `QuestionnaireResponse.item.text` (237, tanpa BQ)<br>_Jika ada catatan penting selama interaksi dengan pasien, silakan dijelaskan secara singkat di sini._ → `QuestionnaireResponse.item.text` (240, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| QuestionnaireResponse | 2 |
| Encounter | 1 |
| Condition | 1 |
| Patient | 1 |
| **Total** | **5** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 32 | Condition | `Condition.code.coding` | 390906007.0 | Follow-up encounter | http://snomed.info/sct |
| 2 | 120 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001109 | Pribadi | http://terminology.kemkes.go.id/sp |
| 3 | 121 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 127848009.0 | Spouse | http://snomed.info/sct |
| 4 | 122 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 40683002.0 | Parent | http://snomed.info/sct |
| 5 | 123 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 67822003.0 | Child | http://snomed.info/sct |
| 6 | 124 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001108 | Kader | http://terminology.kemkes.go.id/sp |
| 7 | 125 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 427568008.0 | Neighbor | http://snomed.info/sct |
| 8 | 126 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001110 | Tidak ada nomor HP pribadi/suami/istri/orang tua/anak/kader/tetangga | http://terminology.kemkes.go.id/sp |
| 9 | 127 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 86372007.0 | Grandchild | http://snomed.info/sct |
| 10 | 128 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 74964007.0 | Other | http://snomed.info/sct |
| 11 | 134 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001111 | Nomor HP tervalidasi dapat terhubung | http://terminology.kemkes.go.id/sp |
| 12 | 135 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001112 | Nomor HP tervalidasi tidak dapat terhubung | http://terminology.kemkes.go.id/sp |
| 13 | 136 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001113 | Tidak ada nomor HP yang terhubung | http://terminology.kemkes.go.id/sp |
| 14 | 142 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001109 | Pribadi | http://terminology.kemkes.go.id/sp |
| 15 | 143 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 127848009.0 | Spouse | http://snomed.info/sct |
| 16 | 144 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 40683002.0 | Parent | http://snomed.info/sct |
| 17 | 145 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 67822003.0 | Child | http://snomed.info/sct |
| 18 | 146 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001108 | Kader | http://terminology.kemkes.go.id/sp |
| 19 | 147 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 427568008.0 | Neighbor | http://snomed.info/sct |
| 20 | 148 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001110 | Tidak ada nomor HP pribadi/suami/istri/orang tua/anak/kader/tetangga | http://terminology.kemkes.go.id/sp |
| 21 | 149 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 86372007.0 | Grandchild | http://snomed.info/sct |
| 22 | 150 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 74964007.0 | Other | http://snomed.info/sct |
| 23 | 156 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001111 | Nomor HP tervalidasi dapat terhubung | http://terminology.kemkes.go.id/sp |
| 24 | 157 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001112 | Nomor HP tervalidasi tidak dapat terhubung | http://terminology.kemkes.go.id/sp |
| 25 | 158 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001113 | Tidak ada nomor HP yang terhubung | http://terminology.kemkes.go.id/sp |
| 26 | 176 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001114 | Tahap awal | http://terminology.kemkes.go.id/sp |
| 27 | 177 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001115 | Tahap lanjutan | http://terminology.kemkes.go.id/sp |
| 28 | 180 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001116 | Pasien dewasa mengambil obat sendiri | http://terminology.kemkes.go.id/sp |
| 29 | 181 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001117 | Pasien dewasa mengambil obat diwakilkan | http://terminology.kemkes.go.id/sp |
| 30 | 182 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001118 | Pasien anak diwakilkan | http://terminology.kemkes.go.id/sp |
| 31 | 185 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 127848009.0 | Spouse | http://snomed.info/sct |
| 32 | 186 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 40683002.0 | Parent | http://snomed.info/sct |
| 33 | 187 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 67822003.0 | Child | http://snomed.info/sct |
| 34 | 188 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 86372007.0 | Grandchild | http://snomed.info/sct |
| 35 | 189 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001108 | Kader | http://terminology.kemkes.go.id/sp |
| 36 | 190 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 427568008.0 | Neighbor | http://snomed.info/sct |
| 37 | 191 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 74964007.0 | Other | http://snomed.info/sct |
| 38 | 204 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 127848009.0 | Spouse | http://snomed.info/sct |
| 39 | 205 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 40683002.0 | Parent | http://snomed.info/sct |
| 40 | 206 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 67822003.0 | Child | http://snomed.info/sct |
| 41 | 207 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 86372007.0 | Grandchild | http://snomed.info/sct |
| 42 | 208 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001108 | Kader | http://terminology.kemkes.go.id/sp |
| 43 | 209 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 427568008.0 | Neighbor | http://snomed.info/sct |
| 44 | 210 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 74964007.0 | Other | http://snomed.info/sct |
| 45 | 233 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | LA13834-9 | 1-2 times per week | http://loinc.org |
| 46 | 234 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | LA13853-9 | 3-4 times per week | http://loinc.org |
| 47 | 235 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | LA13860-4 | 5-6 times per week | http://loinc.org |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 25 |
| http://terminology.kemkes.go.id/sp | 19 |
| http://loinc.org | 3 |
| **Total** | **47** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
