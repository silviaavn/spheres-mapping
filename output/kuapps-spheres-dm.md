# Output Form: Kuapps Spheres - DM

Sumber: `mapping/phdt-data-dictionary-kuapps-spheres-dm.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-kuapps-spheres-dm.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 10 |
| Code (`jumlah code` = 1) | 245 |
| Code unik (code + CodeSystem) | 100 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 233 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 3–30 | Encounter | – | – | _TaskID_ → `Encounter.identifier.value` (3, tanpa BQ)<br>_Tanggal Kunjungan_ → `Encounter.period.start` (11, tanpa BQ)<br>_Puskesmas Pengampu_ → `Encounter.serviceProvider.display` (23, tanpa BQ)<br>_Desa Ampuan_ → `Encounter.location.location.display` (26, tanpa BQ)<br>_Posyandu Ampuan_ → `Encounter.location.location.display` (27, tanpa BQ) |
| 2 | 31–45 | Condition | 390906007 | Follow-up encounter | _Jenis Survei_ → `Condition.code.coding` (33, tanpa BQ) |
| 3 | 46–56 | Observation | 418138009 | Patient condition finding | _Kondisi Responden_ → `Observation.valueCodeableConcept.coding` (48, tanpa BQ) |
| 4 | 57–65 | Observation | 79378-6 | Cause of death | _Penyebab kematian_ → `Observation.valueString` (59, tanpa BQ)<br>_Tanggal Meninggal_ → `Observation.effectiveDateTime` (63, tanpa BQ) |
| 5 | 67–98 | QuestionnaireResponse | https://fhir.kemkes.go.id/sp/Questionnaire/Q00060 | – | _Hasil pengecekan BPJS dari web: https://pasti.bpjs-kesehatan.go.id/cek?_ → `QuestionnaireResponse.item.text` (78, tanpa BQ)<br>_Screenshot hasil pencarian web: https://pasti.bpjs-kesehatan.go.id/cek?_ → `QuestionnaireResponse.item.text` (82, tanpa BQ)<br>_Apakah responden memiliki BPJS Aktif?_ → `QuestionnaireResponse.item.text` (85, tanpa BQ)<br>_Jenis Faskes Tingkat 1 BPJS_ → `QuestionnaireResponse.item.text` (89, tanpa BQ)<br>_Nama Puskesmas Faskes Tingkat 1_ → `QuestionnaireResponse.item.text` (94, tanpa BQ)<br>_Nama Klinik atau Praktik Dokter Mandiri_ → `QuestionnaireResponse.item.text` (97, tanpa BQ) |
| 6 | 100–188 | QuestionnaireResponse | https://fhir.kemkes.go.id/sp/Questionnaire/Q00057 | – | _DMF 01. Apakah benar responden pernah didiagnosis Diabetes Mellitus (DM) sebelumnya?_ → `QuestionnaireResponse.item.text` (111, tanpa BQ)<br>_DMF 02. Apa yang membuat responden tidak rutin ke Puskesmas untuk kontrol DM sebulan sekali?_ → `QuestionnaireResponse.item.text` (115, tanpa BQ)<br>_Merasa sudah sehat_ → `QuestionnaireResponse.item.item.text` (117, tanpa BQ)<br>_Puskesmas jauh dari rumah_ → `QuestionnaireResponse.item.item.text` (121, tanpa BQ)<br>_Tidak ada yang mengantar_ → `QuestionnaireResponse.item.item.text` (125, tanpa BQ)<br>_Tidak ada kendaraan_ → `QuestionnaireResponse.item.item.text` (129, tanpa BQ)<br>_Kerja, tidak bisa izin_ → `QuestionnaireResponse.item.item.text` (133, tanpa BQ)<br>_Antrian Puskesmas terlalu lama_ → `QuestionnaireResponse.item.item.text` (137, tanpa BQ)<br>_Lupa harus kontrol_ → `QuestionnaireResponse.item.item.text` (141, tanpa BQ)<br>_Tidak ada BPJS aktif_ → `QuestionnaireResponse.item.item.text` (145, tanpa BQ)<br>_Biaya berobat mahal_ → `QuestionnaireResponse.item.item.text` (149, tanpa BQ)<br>_Efek samping obat_ → `QuestionnaireResponse.item.item.text` (153, tanpa BQ)<br>_DMF 03. Apakah responden tahu kalau DM yang tidak terkendali (gula darah tinggi) bisa menyebabkan komplikasi seperti gagal ginjal kronis, stroke,dll?_ → `QuestionnaireResponse.item.text` (157, tanpa BQ)<br>_Walau tidak ke Puskesmas, apakah responden rutin kontrol ke fasilitas kesehatan lain? (Minimal sebulan sekali)_ → `QuestionnaireResponse.item.text` (161, tanpa BQ)<br>_Nama Puskesmas yang sering didatangi pasien atau mengadakan kegiatan Prolanis_ → `QuestionnaireResponse.item.text` (169, tanpa BQ)<br>_Tulis nama Posbindu, Klinik, atau RS tempat biasa kontrol._ → `QuestionnaireResponse.item.text` (172, tanpa BQ)<br>_FG. Kondisi responden terhadap kepemilikian/konsumsi obat_ → `QuestionnaireResponse.item.text` (175, tanpa BQ)<br>_FG. Kondisi untuk memfoto obat yang responden punya & konsumsi_ → `QuestionnaireResponse.item.text` (179, tanpa BQ)<br>_FG. Bukti foto obat yang dimiliki_ → `QuestionnaireResponse.item.text` (187, tanpa BQ) |
| 7 | 190–288 | QuestionnaireResponse | https://fhir.kemkes.go.id/sp/Questionnaire/Q00058 | – | _DMA 01. Apakah setelah skrining (pengukuran) gula darah, Anda mengetahui bahwa kadar gula darah Anda tidak normal (tinggi)?_ → `QuestionnaireResponse.item.text` (201, tanpa BQ)<br>_DMA 02. Apakah setelah skrining (pengukuran) gula darah, Anda diinformasikan bahwa kadar gula darah Anda tidak normal (tinggi)?_ → `QuestionnaireResponse.item.text` (205, tanpa BQ)<br>_DMA 03. Apakah petugas yang memeriksa saat itu meminta Anda untuk pergi ke fasilitas kesehatan (Puskesmas) untuk melakukan pemeriksaan konfirmasi, penegakan diagnosis dan mendapatkan obat jika diperlukan?_ → `QuestionnaireResponse.item.text` (209, tanpa BQ)<br>_DMA 04. Pilihlah alasan mana saja dibawah ini yang membuat Anda tidak pergi ke fasilitas kesehatan (Puskesmas) untuk pemeriksaan konfirmasi dan penegakan diagnosis._ → `QuestionnaireResponse.item.text` (213, tanpa BQ)<br>_Menjawab tidak pada 3 pertanyaan sebelumnya_ → `QuestionnaireResponse.item.item.text` (215, tanpa BQ)<br>_Tidak tahu jika hasil pemeriksaan (skrining) abnormal (tinggi)_ → `QuestionnaireResponse.item.item.text` (219, tanpa BQ)<br>_Jarak rumah ke puskesmas terlalu jauh_ → `QuestionnaireResponse.item.item.text` (223, tanpa BQ)<br>_Merasa sehat atau baik-baik saja_ → `QuestionnaireResponse.item.item.text` (227, tanpa BQ)<br>_Merasa takut mengetahui punya penyakit (menderita diabetes mellitus)_ → `QuestionnaireResponse.item.item.text` (231, tanpa BQ)<br>_Merasa bahwa hasil pemeriksaan skrining CKG salah_ → `QuestionnaireResponse.item.item.text` (235, tanpa BQ)<br>_Transportasi sulit_ → `QuestionnaireResponse.item.item.text` (239, tanpa BQ)<br>_Pernah mengalami pelayanan tidak menyenangkan di puskesmas_ → `QuestionnaireResponse.item.item.text` (243, tanpa BQ)<br>_Antrian panjang dan pelayanan lambat_ → `QuestionnaireResponse.item.item.text` (247, tanpa BQ)<br>_Tidak mendapatkan dukungan dari keluarga_ → `QuestionnaireResponse.item.item.text` (251, tanpa BQ)<br>_Ingin mencoba pengobatan alternatif_ → `QuestionnaireResponse.item.item.text` (255, tanpa BQ)<br>_Tidak punya biaya ataupun asuransi BPJS_ → `QuestionnaireResponse.item.item.text` (259, tanpa BQ)<br>_Tidak punya waktu luang_ → `QuestionnaireResponse.item.item.text` (263, tanpa BQ)<br>_Lebih memilih kontrol ke RS atau klinik swasta_ → `QuestionnaireResponse.item.item.text` (267, tanpa BQ)<br>_DMA 05. Apakah anda mengetahui bahwa diabetes mellitus yang tidak diobati dapat menyebabkan komplikasi yang berat seperti stroke atau gagal ginjal?_ → `QuestionnaireResponse.item.text` (271, tanpa BQ)<br>_DG. Kondisi suspek terhadap kepemilikian/konsumsi obat_ → `QuestionnaireResponse.item.text` (275, tanpa BQ)<br>_DG. Kondisi untuk memfoto obat yang suspek punya & konsumsi_ → `QuestionnaireResponse.item.text` (279, tanpa BQ)<br>_DG. Bukti foto obat yang dimiliki_ → `QuestionnaireResponse.item.text` (287, tanpa BQ) |
| 8 | 290–459 | QuestionnaireResponse | https://fhir.kemkes.go.id/sp/Questionnaire/Q00059 | – | _Pilih sesuai kondisi pasien:_ → `QuestionnaireResponse.item.text` (301, tanpa BQ)<br>_TG01. Di rumah sakit mana pasien dirujuk_ → `QuestionnaireResponse.item.answer.item.item.text` (309, tanpa BQ)<br>_TG01. Apakah bukti surat rujukan RS bisa difoto?_ → `QuestionnaireResponse.item.answer.item.item.text` (312, tanpa BQ)<br>_TG01. Alasan surat rujukan tidak bisa difoto_ → `QuestionnaireResponse.item.answer.item.item.text` (316, tanpa BQ)<br>_TG01. Bukti Surat Rujukan_ → `QuestionnaireResponse.item.answer.item.item.text` (321, tanpa BQ)<br>_TG01. Apakah pasien mendapatkan obat dari rumah sakit_ → `QuestionnaireResponse.item.answer.item.item.text` (324, tanpa BQ)<br>_TG01. Kondisi untuk memfoto obat pasien dari rumah sakit_ → `QuestionnaireResponse.item.answer.item.item.text` (328, tanpa BQ)<br>_TG01. Apa alasan pasien tidak mendapat obat dari rumah sakit?_ → `QuestionnaireResponse.item.answer.item.item.text` (336, tanpa BQ)<br>_TG01. Bukti foto obat yang dimiliki_ → `QuestionnaireResponse.item.answer.item.item.text` (348, tanpa BQ)<br>_TG02. Puskesmas mana tempat pasien biasanya berobat, khususnya untuk DM?_ → `QuestionnaireResponse.item.answer.item.item.text` (353, tanpa BQ)<br>_TG02. Apakah pasien sebenarnya mendapat obat dari Puskesmas?_ → `QuestionnaireResponse.item.answer.item.item.text` (356, tanpa BQ)<br>_TG02. Kondisi untuk memfoto obat pasien dari Puskesmas_ → `QuestionnaireResponse.item.answer.item.item.text` (360, tanpa BQ)<br>_TG02. Apa alasan pasien tidak mendapat obat dari Puskesmas?_ → `QuestionnaireResponse.item.answer.item.item.text` (368, tanpa BQ)<br>_TG02. Bukti foto obat yang dimiliki_ → `QuestionnaireResponse.item.answer.item.item.text` (380, tanpa BQ)<br>_TG03. Di Klinik/Praktik Dokter Mandiri mana pasien biasanya berobat_ → `QuestionnaireResponse.item.answer.item.item.text` (385, tanpa BQ)<br>_TG03. Apakah pasien sebenarnya mendapat obat dari Klinik atau Praktik Dokter Mandiri?_ → `QuestionnaireResponse.item.answer.item.item.text` (388, tanpa BQ)<br>_TG03. Kondisi untuk memfoto obat pasien dari Klinik atau Praktik Dokter Mandiri_ → `QuestionnaireResponse.item.answer.item.item.text` (392, tanpa BQ)<br>_TG03. Apa alasan pasien tidak mendapat obat dari Klinik atau Praktik Dokter Mandiri?_ → `QuestionnaireResponse.item.answer.item.item.text` (400, tanpa BQ)<br>_TG03. Bukti foto obat yang dimiliki_ → `QuestionnaireResponse.item.answer.item.item.text` (412, tanpa BQ)<br>_TG04. Dari rumah sakit mana pasien dirujuk balik_ → `QuestionnaireResponse.item.answer.item.item.text` (417, tanpa BQ)<br>_TG04. Apakah bukti surat rujukan balik bisa difoto?_ → `QuestionnaireResponse.item.answer.item.item.text` (420, tanpa BQ)<br>_TG04. Alasan surat rujukan balik tidak bisa difoto_ → `QuestionnaireResponse.item.answer.item.item.text` (424, tanpa BQ)<br>_TG04. Bukti Surat Rujukan Balik_ → `QuestionnaireResponse.item.answer.item.item.text` (429, tanpa BQ)<br>_TG04. Kondisi pasien PRB terhadap obat_ → `QuestionnaireResponse.item.answer.item.item.text` (432, tanpa BQ)<br>_TG04. Kondisi untuk memfoto obat pasien PRB_ → `QuestionnaireResponse.item.answer.item.item.text` (438, tanpa BQ)<br>_TG04. Apa alasan pasien PRB tidak mendapat obat?_ → `QuestionnaireResponse.item.answer.item.item.text` (446, tanpa BQ)<br>_TG04. Bukti foto obat yang dimiliki_ → `QuestionnaireResponse.item.answer.item.item.text` (458, tanpa BQ) |
| 9 | 461–757 | QuestionnaireResponse | https://fhir.kemkes.go.id/sp/Questionnaire/Q00061 | – | _Obat apa saja yang dimiliki pasien?_ → `QuestionnaireResponse.item.text` (472, tanpa BQ)<br>_JO1. Obat yang ada: Metformin_ → `QuestionnaireResponse.item.answer.item.item.text` (484, tanpa BQ)<br>_JO1. Jumlah (butir) metformin yang didapat/ada_ → `QuestionnaireResponse.item.answer.item.item.text` (488, tanpa BQ)<br>_JO1. Signa Metformin_ → `QuestionnaireResponse.item.answer.item.item.text` (494, tanpa BQ)<br>_JO1. Total butir Metformin dalam sehari_ → `QuestionnaireResponse.item.answer.item.item.text` (508, tanpa BQ)<br>_JO1. Tanggal menerima metformin_ → `QuestionnaireResponse.item.answer.item.item.text` (514, tanpa BQ)<br>_JO2. Obat yang ada: Glimepiride_ → `QuestionnaireResponse.item.answer.item.item.text` (519, tanpa BQ)<br>_JO2. Jumlah (butir) Glimepiride yang didapat/ada_ → `QuestionnaireResponse.item.answer.item.item.text` (525, tanpa BQ)<br>_JO2. Signa Glimepiride_ → `QuestionnaireResponse.item.answer.item.item.text` (531, tanpa BQ)<br>_JO2. Total butir Glimepiride dalam sehari_ → `QuestionnaireResponse.item.answer.item.item.text` (545, tanpa BQ)<br>_JO2. Tanggal menerima Glimepiride_ → `QuestionnaireResponse.item.answer.item.item.text` (551, tanpa BQ)<br>_JO3. Obat yang ada: Injeksi Insulin_ → `QuestionnaireResponse.item.answer.item.item.text` (556, tanpa BQ)<br>_JO3. Jumlah pen injeksi yang didapat/ada_ → `QuestionnaireResponse.item.answer.item.item.text` (559, tanpa BQ)<br>_JO3. Jumlah injeksi dalam sehari_ → `QuestionnaireResponse.item.answer.item.item.text` (565, tanpa BQ)<br>_JO3. Dosis per suntik_ → `QuestionnaireResponse.item.answer.item.item.text` (573, tanpa BQ)<br>_JO3. Tanggal menerima injeksi insulin_ → `QuestionnaireResponse.item.answer.item.item.text` (576, tanpa BQ)<br>_JO4. Obat yang ada: Amlodipine_ → `QuestionnaireResponse.item.answer.item.item.text` (581, tanpa BQ)<br>_JO4. Jumlah (butir) Amlodipine yang didapat/ada_ → `QuestionnaireResponse.item.answer.item.item.text` (585, tanpa BQ)<br>_JO4. Signa Amlodipine_ → `QuestionnaireResponse.item.answer.item.item.text` (591, tanpa BQ)<br>_JO4. Total butir Amlodipine dalam sehari_ → `QuestionnaireResponse.item.answer.item.item.text` (605, tanpa BQ)<br>_JO4. Tanggal menerima Amlodipine_ → `QuestionnaireResponse.item.answer.item.item.text` (611, tanpa BQ)<br>_JO5. Obat yang ada: Captopril_ → `QuestionnaireResponse.item.answer.item.item.text` (616, tanpa BQ)<br>_JO5. Jumlah (butir) Captopril yang didapat/ada_ → `QuestionnaireResponse.item.answer.item.item.text` (621, tanpa BQ)<br>_JO5. Signa Captopril_ → `QuestionnaireResponse.item.answer.item.item.text` (627, tanpa BQ)<br>_JO5. Total butir Captopril dalam sehari_ → `QuestionnaireResponse.item.answer.item.item.text` (641, tanpa BQ)<br>_JO5. Tanggal menerima Captopril_ → `QuestionnaireResponse.item.answer.item.item.text` (647, tanpa BQ)<br>_JO6. Obat yang ada: Cadesartan_ → `QuestionnaireResponse.item.answer.item.item.text` (652, tanpa BQ)<br>_JO6. Jumlah (butir) Cadesartan yang didapat/ada_ → `QuestionnaireResponse.item.answer.item.item.text` (658, tanpa BQ)<br>_JO6. Signa Cadesartan_ → `QuestionnaireResponse.item.answer.item.item.text` (664, tanpa BQ)<br>_JO6. Total butir Cadesartan dalam sehari_ → `QuestionnaireResponse.item.answer.item.item.text` (678, tanpa BQ)<br>_JO6. Tanggal menerima Cadesartan_ → `QuestionnaireResponse.item.answer.item.item.text` (684, tanpa BQ)<br>_JO7. Obat yang ada: Bisoprolol_ → `QuestionnaireResponse.item.answer.item.item.text` (689, tanpa BQ)<br>_JO7. Jumlah (butir) Bisoprolol yang didapat/ada_ → `QuestionnaireResponse.item.answer.item.item.text` (694, tanpa BQ)<br>_JO7. Signa Bisoprolol_ → `QuestionnaireResponse.item.answer.item.item.text` (700, tanpa BQ)<br>_JO7. Total butir Bisoprolol dalam sehari_ → `QuestionnaireResponse.item.answer.item.item.text` (714, tanpa BQ)<br>_JO7. Tanggal menerima Bisoprolol_ → `QuestionnaireResponse.item.answer.item.item.text` (720, tanpa BQ)<br>_JO8. Obat yang ada: Spironolakton_ → `QuestionnaireResponse.item.answer.item.item.text` (725, tanpa BQ)<br>_JO8. Jumlah (butir) Spironolakton yang didapat/ada_ → `QuestionnaireResponse.item.answer.item.item.text` (730, tanpa BQ)<br>_JO8. Signa Spironolakton_ → `QuestionnaireResponse.item.answer.item.item.text` (736, tanpa BQ)<br>_JO8. Total butir Spironolakton dalam sehari_ → `QuestionnaireResponse.item.answer.item.item.text` (750, tanpa BQ)<br>_JO8. Tanggal menerima Spironolakton_ → `QuestionnaireResponse.item.answer.item.item.text` (756, tanpa BQ) |
| 10 | 759–804 | QuestionnaireResponse | https://fhir.kemkes.go.id/sp/Questionnaire/Q00062 | – | _Apakah kondisi responden bisa dijadwalkan untuk ke Puskesmas?_ → `QuestionnaireResponse.item.text` (770, tanpa BQ)<br>_Tanggal rencana pemeriksaan ke faskes_ → `QuestionnaireResponse.item.text` (778, tanpa BQ)<br>_Edukasi responden untuk:- Puasa dari jam 12 malam. Bangun tidur tidak makan dan minum yang berasa dan berwarna. - Berlaku bagi kedua kasus, diagnosis atau treatment gap. Minta responden untuk mengulang instruksi untuk memastikan mereka paham._ → `QuestionnaireResponse.item.text` (781, tanpa BQ)<br>_Edukasi responden bahwa:Hasil pemeriksaan di Puskesmas ada 2 kemungkinan. Sakit & sehat. Jelaskan bahwa diajak ke Puskesmas/faskes untuk memastikan keadaan mereka. Jika hasil bagus (sehat), suspek seharusnya lega dan jangan marah kepada pihak faskes. Minta suspek untuk mengulang instruksi untuk memastikan mereka paham._ → `QuestionnaireResponse.item.text` (785, tanpa BQ)<br>_Faskes tujuan untuk kontrol, pemeriksaan dan/atau pengambilan obat_ → `QuestionnaireResponse.item.text` (789, tanpa BQ)<br>_Puskesmas untuk kontrol, pemeriksaan dan/atau pengambilan obat_ → `QuestionnaireResponse.item.text` (795, tanpa BQ)<br>_Nama Rumah Sakit untuk kontrol, pemeriksaan dan/atau pengambilan obat_ → `QuestionnaireResponse.item.text` (798, tanpa BQ)<br>_Nama Klinik atau Praktik Dokter Mandiri untuk kontrol, pemeriksaan dan/atau pengambilan obat_ → `QuestionnaireResponse.item.text` (801, tanpa BQ)<br>_Unique QR Code_ → `QuestionnaireResponse.identifier.value` (803, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| QuestionnaireResponse | 6 |
| Observation | 2 |
| Encounter | 1 |
| Condition | 1 |
| **Total** | **10** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 33 | Condition | `Condition.code.coding` | 390906007 | Follow-up encounter | http://snomed.info/sct |
| 2 | 46 | Observation | `Observation.code.coding` | 418138009 | Patient condition finding | http://snomed.info/sct |
| 3 | 48 | Observation | `Observation.valueCodeableConcept.coding` | 438949009 | Alive | http://snomed.info/sct |
| 4 | 49 | Observation | `Observation.valueCodeableConcept.coding` | 419099009 | Dead | http://snomed.info/sct |
| 5 | 50 | Observation | `Observation.valueCodeableConcept.coding` | SP001004 | Pindah keluar kabupaten | http://terminology.kemkes.go.id/sp |
| 6 | 57 | Observation | `Observation.code.coding` | 79378-6 | Cause of death | http://loinc.org |
| 7 | 79 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001005 | Data ditemukan | http://terminology.kemkes.go.id/sp |
| 8 | 80 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001006 | Tidak ditemukan | http://terminology.kemkes.go.id/sp |
| 9 | 90 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 102 | Pusat Kesehatan Masyarakat | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 10 | 91 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 103 | Klinik | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 11 | 92 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 101 | Praktek mandiri | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 12 | 162 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001007 | Ya, ke Posbindu | http://terminology.kemkes.go.id/sp |
| 13 | 163 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001008 | Ya, ke Klinik Swasta | http://terminology.kemkes.go.id/sp |
| 14 | 164 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001009 | Ya, ke Rumah Sakit | http://terminology.kemkes.go.id/sp |
| 15 | 165 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001010 | Ya, di kegiatan Prolanis | http://terminology.kemkes.go.id/sp |
| 16 | 166 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001011 | Pasien ternyata rutin kontrol ke PKM | http://terminology.kemkes.go.id/sp |
| 17 | 167 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001012 | Tidak | http://terminology.kemkes.go.id/sp |
| 18 | 176 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001013 | Responden punya dan minum obat | http://terminology.kemkes.go.id/sp |
| 19 | 177 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001014 | Responden tidak pernah atau tidak lagi minum obat | http://terminology.kemkes.go.id/sp |
| 20 | 180 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001015 | Obat bisa difoto seluruhnya | http://terminology.kemkes.go.id/sp |
| 21 | 181 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001016 | Obat bisa difoto sebagian | http://terminology.kemkes.go.id/sp |
| 22 | 182 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001017 | Obat disimpan oleh anggota keluarga lain | http://terminology.kemkes.go.id/sp |
| 23 | 183 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001018 | Obat hilang | http://terminology.kemkes.go.id/sp |
| 24 | 184 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001019 | Obat habis | http://terminology.kemkes.go.id/sp |
| 25 | 185 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001020 | Lupa menyimpan dimana | http://terminology.kemkes.go.id/sp |
| 26 | 276 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001021 | Suspek punya dan minum obat | http://terminology.kemkes.go.id/sp |
| 27 | 277 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001022 | Suspek tidak pernah atau tidak lagi minum obat | http://terminology.kemkes.go.id/sp |
| 28 | 280 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001015 | Obat bisa difoto seluruhnya | http://terminology.kemkes.go.id/sp |
| 29 | 281 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001016 | Obat bisa difoto sebagian | http://terminology.kemkes.go.id/sp |
| 30 | 282 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001017 | Obat disimpan oleh anggota keluarga lain | http://terminology.kemkes.go.id/sp |
| 31 | 283 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001018 | Obat hilang | http://terminology.kemkes.go.id/sp |
| 32 | 284 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001019 | Obat habis | http://terminology.kemkes.go.id/sp |
| 33 | 285 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001020 | Lupa menyimpan dimana | http://terminology.kemkes.go.id/sp |
| 34 | 302 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001023 | Pasien dirujuk ke Rumah Sakit | http://terminology.kemkes.go.id/sp |
| 35 | 303 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001024 | Berobat di Puskesmas (tidak pernah rujuk) | http://terminology.kemkes.go.id/sp |
| 36 | 304 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001025 | Periksa di klinik mandiri | http://terminology.kemkes.go.id/sp |
| 37 | 305 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001026 | Rujuk balik ke Puskesmas dari RS (PRB) | http://terminology.kemkes.go.id/sp |
| 38 | 317 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001027 | Surat rujukan hilang | http://terminology.kemkes.go.id/sp |
| 39 | 318 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001028 | Surat rujukan disimpan oleh anggota keluarga | http://terminology.kemkes.go.id/sp |
| 40 | 319 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP000407 | Privasi | http://terminology.kemkes.go.id/sp |
| 41 | 329 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001015 | Obat bisa difoto seluruhnya | http://terminology.kemkes.go.id/sp |
| 42 | 330 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001016 | Obat bisa difoto sebagian | http://terminology.kemkes.go.id/sp |
| 43 | 331 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001017 | Obat disimpan oleh anggota keluarga lain | http://terminology.kemkes.go.id/sp |
| 44 | 332 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001018 | Obat hilang | http://terminology.kemkes.go.id/sp |
| 45 | 333 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001019 | Obat habis | http://terminology.kemkes.go.id/sp |
| 46 | 334 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001020 | Lupa menyimpan dimana | http://terminology.kemkes.go.id/sp |
| 47 | 337 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001029 | Beli obat sendiri | http://terminology.kemkes.go.id/sp |
| 48 | 338 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001030 | Punya obat di rumah | http://terminology.kemkes.go.id/sp |
| 49 | 339 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001031 | Obat tidak tersedia di RS | http://terminology.kemkes.go.id/sp |
| 50 | 340 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001032 | Mengambil obat di apotek luar RS | http://terminology.kemkes.go.id/sp |
| 51 | 341 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001033 | Terapi belum membutuhkan obat | http://terminology.kemkes.go.id/sp |
| 52 | 342 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001034 | Obat dihentikan | http://terminology.kemkes.go.id/sp |
| 53 | 343 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001035 | Obat diganti | http://terminology.kemkes.go.id/sp |
| 54 | 344 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001036 | Sengaja tidak mengambil obat | http://terminology.kemkes.go.id/sp |
| 55 | 345 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001037 | Kendala administrasi | http://terminology.kemkes.go.id/sp |
| 56 | 346 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001038 | Tidak tahu | http://terminology.kemkes.go.id/sp |
| 57 | 361 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001015 | Obat bisa difoto seluruhnya | http://terminology.kemkes.go.id/sp |
| 58 | 362 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001016 | Obat bisa difoto sebagian | http://terminology.kemkes.go.id/sp |
| 59 | 363 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001017 | Obat disimpan oleh anggota keluarga lain | http://terminology.kemkes.go.id/sp |
| 60 | 364 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001018 | Obat hilang | http://terminology.kemkes.go.id/sp |
| 61 | 365 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001019 | Obat habis | http://terminology.kemkes.go.id/sp |
| 62 | 366 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001020 | Lupa menyimpan dimana | http://terminology.kemkes.go.id/sp |
| 63 | 369 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001029 | Beli obat sendiri | http://terminology.kemkes.go.id/sp |
| 64 | 370 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001030 | Punya obat di rumah | http://terminology.kemkes.go.id/sp |
| 65 | 371 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001031 | Obat tidak tersedia di RS | http://terminology.kemkes.go.id/sp |
| 66 | 372 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001032 | Mengambil obat di apotek luar RS | http://terminology.kemkes.go.id/sp |
| 67 | 373 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001033 | Terapi belum membutuhkan obat | http://terminology.kemkes.go.id/sp |
| 68 | 374 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001034 | Obat dihentikan | http://terminology.kemkes.go.id/sp |
| 69 | 375 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001035 | Obat diganti | http://terminology.kemkes.go.id/sp |
| 70 | 376 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001036 | Sengaja tidak mengambil obat | http://terminology.kemkes.go.id/sp |
| 71 | 377 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001037 | Kendala administrasi | http://terminology.kemkes.go.id/sp |
| 72 | 378 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001038 | Tidak tahu | http://terminology.kemkes.go.id/sp |
| 73 | 393 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001015 | Obat bisa difoto seluruhnya | http://terminology.kemkes.go.id/sp |
| 74 | 394 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001016 | Obat bisa difoto sebagian | http://terminology.kemkes.go.id/sp |
| 75 | 395 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001017 | Obat disimpan oleh anggota keluarga lain | http://terminology.kemkes.go.id/sp |
| 76 | 396 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001018 | Obat hilang | http://terminology.kemkes.go.id/sp |
| 77 | 397 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001019 | Obat habis | http://terminology.kemkes.go.id/sp |
| 78 | 398 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001020 | Lupa menyimpan dimana | http://terminology.kemkes.go.id/sp |
| 79 | 401 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001029 | Beli obat sendiri | http://terminology.kemkes.go.id/sp |
| 80 | 402 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001030 | Punya obat di rumah | http://terminology.kemkes.go.id/sp |
| 81 | 403 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001031 | Obat tidak tersedia di RS | http://terminology.kemkes.go.id/sp |
| 82 | 404 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001032 | Mengambil obat di apotek luar RS | http://terminology.kemkes.go.id/sp |
| 83 | 405 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001033 | Terapi belum membutuhkan obat | http://terminology.kemkes.go.id/sp |
| 84 | 406 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001034 | Obat dihentikan | http://terminology.kemkes.go.id/sp |
| 85 | 407 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001035 | Obat diganti | http://terminology.kemkes.go.id/sp |
| 86 | 408 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001036 | Sengaja tidak mengambil obat | http://terminology.kemkes.go.id/sp |
| 87 | 409 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001037 | Kendala administrasi | http://terminology.kemkes.go.id/sp |
| 88 | 410 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001038 | Tidak tahu | http://terminology.kemkes.go.id/sp |
| 89 | 425 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001027 | Surat rujukan hilang | http://terminology.kemkes.go.id/sp |
| 90 | 426 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001028 | Surat rujukan disimpan oleh anggota keluarga | http://terminology.kemkes.go.id/sp |
| 91 | 427 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP000407 | Privasi | http://terminology.kemkes.go.id/sp |
| 92 | 433 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001039 | Seluruh obat dari Puskesmas | http://terminology.kemkes.go.id/sp |
| 93 | 434 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001040 | Sebagian obat dari Puskesmas, sebagian apotek luar | http://terminology.kemkes.go.id/sp |
| 94 | 435 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001041 | Seluruh obat dari apotek luar | http://terminology.kemkes.go.id/sp |
| 95 | 436 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001042 | Tidak mendapat obat | http://terminology.kemkes.go.id/sp |
| 96 | 439 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001015 | Obat bisa difoto seluruhnya | http://terminology.kemkes.go.id/sp |
| 97 | 440 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001016 | Obat bisa difoto sebagian | http://terminology.kemkes.go.id/sp |
| 98 | 441 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001017 | Obat disimpan oleh anggota keluarga lain | http://terminology.kemkes.go.id/sp |
| 99 | 442 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001018 | Obat hilang | http://terminology.kemkes.go.id/sp |
| 100 | 443 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001019 | Obat habis | http://terminology.kemkes.go.id/sp |
| 101 | 444 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001020 | Lupa menyimpan dimana | http://terminology.kemkes.go.id/sp |
| 102 | 447 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001029 | Beli obat sendiri | http://terminology.kemkes.go.id/sp |
| 103 | 448 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001030 | Punya obat di rumah | http://terminology.kemkes.go.id/sp |
| 104 | 449 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001031 | Obat tidak tersedia di RS | http://terminology.kemkes.go.id/sp |
| 105 | 450 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001032 | Mengambil obat di apotek luar RS | http://terminology.kemkes.go.id/sp |
| 106 | 451 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001033 | Terapi belum membutuhkan obat | http://terminology.kemkes.go.id/sp |
| 107 | 452 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001034 | Obat dihentikan | http://terminology.kemkes.go.id/sp |
| 108 | 453 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001035 | Obat diganti | http://terminology.kemkes.go.id/sp |
| 109 | 454 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001036 | Sengaja tidak mengambil obat | http://terminology.kemkes.go.id/sp |
| 110 | 455 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001037 | Kendala administrasi | http://terminology.kemkes.go.id/sp |
| 111 | 456 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001038 | Tidak tahu | http://terminology.kemkes.go.id/sp |
| 112 | 473 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001043 | Metformin | http://terminology.kemkes.go.id/sp |
| 113 | 474 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001044 | Glimepiride | http://terminology.kemkes.go.id/sp |
| 114 | 475 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001045 | Injeksi Insulin | http://terminology.kemkes.go.id/sp |
| 115 | 476 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001046 | Amlodipine | http://terminology.kemkes.go.id/sp |
| 116 | 477 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001047 | Captopril | http://terminology.kemkes.go.id/sp |
| 117 | 478 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001048 | Cadesartan | http://terminology.kemkes.go.id/sp |
| 118 | 479 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001049 | Bisoprolol | http://terminology.kemkes.go.id/sp |
| 119 | 480 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001050 | Spironolakton | http://terminology.kemkes.go.id/sp |
| 120 | 485 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001051 | 500 mg | http://terminology.kemkes.go.id/sp |
| 121 | 486 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001052 | 850 mg | http://terminology.kemkes.go.id/sp |
| 122 | 495 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001053 | 0.5 tablet 1 kali sehari | http://terminology.kemkes.go.id/sp |
| 123 | 496 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001054 | 1 tablet 1 kali sehari | http://terminology.kemkes.go.id/sp |
| 124 | 497 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001055 | 1.5 tablet 1 kali sehari | http://terminology.kemkes.go.id/sp |
| 125 | 498 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001056 | 2 tablet 1 kali sehari | http://terminology.kemkes.go.id/sp |
| 126 | 499 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001057 | 0.5 tablet 2 kali sehari | http://terminology.kemkes.go.id/sp |
| 127 | 500 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001058 | 1 tablet 2 kali sehari | http://terminology.kemkes.go.id/sp |
| 128 | 501 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001059 | 1.5 tablet 2 kali | http://terminology.kemkes.go.id/sp |
| 129 | 502 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001060 | 2 tablet 2 kali sehari | http://terminology.kemkes.go.id/sp |
| 130 | 503 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001061 | 0.5 tablet 3 kali | http://terminology.kemkes.go.id/sp |
| 131 | 504 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001062 | 1 tablet 3 kali sehari | http://terminology.kemkes.go.id/sp |
| 132 | 505 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001063 | 1.5 tablet 3 kali sehari | http://terminology.kemkes.go.id/sp |
| 133 | 506 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001064 | 2 tablet 3 kali sehari | http://terminology.kemkes.go.id/sp |
| 134 | 520 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001065 | 1 mg | http://terminology.kemkes.go.id/sp |
| 135 | 521 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001066 | 2 mg | http://terminology.kemkes.go.id/sp |
| 136 | 522 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001067 | 3 mg | http://terminology.kemkes.go.id/sp |
| 137 | 523 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001068 | 4 mg | http://terminology.kemkes.go.id/sp |
| 138 | 532 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001053 | 0.5 tablet 1 kali sehari | http://terminology.kemkes.go.id/sp |
| 139 | 533 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001054 | 1 tablet 1 kali sehari | http://terminology.kemkes.go.id/sp |
| 140 | 534 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001055 | 1.5 tablet 1 kali sehari | http://terminology.kemkes.go.id/sp |
| 141 | 535 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001056 | 2 tablet 1 kali sehari | http://terminology.kemkes.go.id/sp |
| 142 | 536 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001057 | 0.5 tablet 2 kali sehari | http://terminology.kemkes.go.id/sp |
| 143 | 537 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001058 | 1 tablet 2 kali sehari | http://terminology.kemkes.go.id/sp |
| 144 | 538 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001059 | 1.5 tablet 2 kali | http://terminology.kemkes.go.id/sp |
| 145 | 539 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001060 | 2 tablet 2 kali sehari | http://terminology.kemkes.go.id/sp |
| 146 | 540 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001061 | 0.5 tablet 3 kali | http://terminology.kemkes.go.id/sp |
| 147 | 541 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001062 | 1 tablet 3 kali sehari | http://terminology.kemkes.go.id/sp |
| 148 | 542 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001063 | 1.5 tablet 3 kali sehari | http://terminology.kemkes.go.id/sp |
| 149 | 543 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001064 | 2 tablet 3 kali sehari | http://terminology.kemkes.go.id/sp |
| 150 | 557 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001069 | 100 unit/mL, 3 mL | http://terminology.kemkes.go.id/sp |
| 151 | 566 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001070 | 1 kali suntik | http://terminology.kemkes.go.id/sp |
| 152 | 567 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001071 | 2 kali suntik | http://terminology.kemkes.go.id/sp |
| 153 | 568 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001072 | 3 kali suntik | http://terminology.kemkes.go.id/sp |
| 154 | 569 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001073 | 4 kali suntik | http://terminology.kemkes.go.id/sp |
| 155 | 570 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001074 | 5 kali suntik | http://terminology.kemkes.go.id/sp |
| 156 | 571 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001075 | 6 kali suntik | http://terminology.kemkes.go.id/sp |
| 157 | 582 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001076 | 5 mg | http://terminology.kemkes.go.id/sp |
| 158 | 583 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001077 | 10 mg | http://terminology.kemkes.go.id/sp |
| 159 | 592 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001053 | 0.5 tablet 1 kali sehari | http://terminology.kemkes.go.id/sp |
| 160 | 593 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001054 | 1 tablet 1 kali sehari | http://terminology.kemkes.go.id/sp |
| 161 | 594 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001055 | 1.5 tablet 1 kali sehari | http://terminology.kemkes.go.id/sp |
| 162 | 595 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001056 | 2 tablet 1 kali sehari | http://terminology.kemkes.go.id/sp |
| 163 | 596 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001057 | 0.5 tablet 2 kali sehari | http://terminology.kemkes.go.id/sp |
| 164 | 597 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001058 | 1 tablet 2 kali sehari | http://terminology.kemkes.go.id/sp |
| 165 | 598 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001059 | 1.5 tablet 2 kali | http://terminology.kemkes.go.id/sp |
| 166 | 599 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001060 | 2 tablet 2 kali sehari | http://terminology.kemkes.go.id/sp |
| 167 | 600 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001061 | 0.5 tablet 3 kali | http://terminology.kemkes.go.id/sp |
| 168 | 601 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001062 | 1 tablet 3 kali sehari | http://terminology.kemkes.go.id/sp |
| 169 | 602 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001063 | 1.5 tablet 3 kali sehari | http://terminology.kemkes.go.id/sp |
| 170 | 603 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001064 | 2 tablet 3 kali sehari | http://terminology.kemkes.go.id/sp |
| 171 | 617 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001078 | 12.5 mg | http://terminology.kemkes.go.id/sp |
| 172 | 618 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001079 | 25 mg | http://terminology.kemkes.go.id/sp |
| 173 | 619 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001080 | 50 mg | http://terminology.kemkes.go.id/sp |
| 174 | 628 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001053 | 0.5 tablet 1 kali sehari | http://terminology.kemkes.go.id/sp |
| 175 | 629 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001054 | 1 tablet 1 kali sehari | http://terminology.kemkes.go.id/sp |
| 176 | 630 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001055 | 1.5 tablet 1 kali sehari | http://terminology.kemkes.go.id/sp |
| 177 | 631 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001056 | 2 tablet 1 kali sehari | http://terminology.kemkes.go.id/sp |
| 178 | 632 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001057 | 0.5 tablet 2 kali sehari | http://terminology.kemkes.go.id/sp |
| 179 | 633 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001058 | 1 tablet 2 kali sehari | http://terminology.kemkes.go.id/sp |
| 180 | 634 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001059 | 1.5 tablet 2 kali | http://terminology.kemkes.go.id/sp |
| 181 | 635 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001060 | 2 tablet 2 kali sehari | http://terminology.kemkes.go.id/sp |
| 182 | 636 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001061 | 0.5 tablet 3 kali | http://terminology.kemkes.go.id/sp |
| 183 | 637 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001062 | 1 tablet 3 kali sehari | http://terminology.kemkes.go.id/sp |
| 184 | 638 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001063 | 1.5 tablet 3 kali sehari | http://terminology.kemkes.go.id/sp |
| 185 | 639 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001064 | 2 tablet 3 kali sehari | http://terminology.kemkes.go.id/sp |
| 186 | 653 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001068 | 4 mg | http://terminology.kemkes.go.id/sp |
| 187 | 654 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001081 | 8 mg | http://terminology.kemkes.go.id/sp |
| 188 | 655 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001082 | 16 mg | http://terminology.kemkes.go.id/sp |
| 189 | 656 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001083 | 32 mg | http://terminology.kemkes.go.id/sp |
| 190 | 665 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001053 | 0.5 tablet 1 kali sehari | http://terminology.kemkes.go.id/sp |
| 191 | 666 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001054 | 1 tablet 1 kali sehari | http://terminology.kemkes.go.id/sp |
| 192 | 667 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001055 | 1.5 tablet 1 kali sehari | http://terminology.kemkes.go.id/sp |
| 193 | 668 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001056 | 2 tablet 1 kali sehari | http://terminology.kemkes.go.id/sp |
| 194 | 669 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001057 | 0.5 tablet 2 kali sehari | http://terminology.kemkes.go.id/sp |
| 195 | 670 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001058 | 1 tablet 2 kali sehari | http://terminology.kemkes.go.id/sp |
| 196 | 671 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001059 | 1.5 tablet 2 kali | http://terminology.kemkes.go.id/sp |
| 197 | 672 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001060 | 2 tablet 2 kali sehari | http://terminology.kemkes.go.id/sp |
| 198 | 673 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001061 | 0.5 tablet 3 kali | http://terminology.kemkes.go.id/sp |
| 199 | 674 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001062 | 1 tablet 3 kali sehari | http://terminology.kemkes.go.id/sp |
| 200 | 675 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001063 | 1.5 tablet 3 kali sehari | http://terminology.kemkes.go.id/sp |
| 201 | 676 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001064 | 2 tablet 3 kali sehari | http://terminology.kemkes.go.id/sp |
| 202 | 690 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001084 | 2.5 mg | http://terminology.kemkes.go.id/sp |
| 203 | 691 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001076 | 5 mg | http://terminology.kemkes.go.id/sp |
| 204 | 692 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001077 | 10 mg | http://terminology.kemkes.go.id/sp |
| 205 | 701 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001053 | 0.5 tablet 1 kali sehari | http://terminology.kemkes.go.id/sp |
| 206 | 702 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001054 | 1 tablet 1 kali sehari | http://terminology.kemkes.go.id/sp |
| 207 | 703 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001055 | 1.5 tablet 1 kali sehari | http://terminology.kemkes.go.id/sp |
| 208 | 704 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001056 | 2 tablet 1 kali sehari | http://terminology.kemkes.go.id/sp |
| 209 | 705 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001057 | 0.5 tablet 2 kali sehari | http://terminology.kemkes.go.id/sp |
| 210 | 706 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001058 | 1 tablet 2 kali sehari | http://terminology.kemkes.go.id/sp |
| 211 | 707 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001059 | 1.5 tablet 2 kali | http://terminology.kemkes.go.id/sp |
| 212 | 708 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001060 | 2 tablet 2 kali sehari | http://terminology.kemkes.go.id/sp |
| 213 | 709 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001061 | 0.5 tablet 3 kali | http://terminology.kemkes.go.id/sp |
| 214 | 710 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001062 | 1 tablet 3 kali sehari | http://terminology.kemkes.go.id/sp |
| 215 | 711 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001063 | 1.5 tablet 3 kali sehari | http://terminology.kemkes.go.id/sp |
| 216 | 712 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001064 | 2 tablet 3 kali sehari | http://terminology.kemkes.go.id/sp |
| 217 | 726 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001079 | 25 mg | http://terminology.kemkes.go.id/sp |
| 218 | 727 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001080 | 50 mg | http://terminology.kemkes.go.id/sp |
| 219 | 728 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001085 | 100 mg | http://terminology.kemkes.go.id/sp |
| 220 | 737 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001053 | 0.5 tablet 1 kali sehari | http://terminology.kemkes.go.id/sp |
| 221 | 738 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001054 | 1 tablet 1 kali sehari | http://terminology.kemkes.go.id/sp |
| 222 | 739 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001055 | 1.5 tablet 1 kali sehari | http://terminology.kemkes.go.id/sp |
| 223 | 740 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001056 | 2 tablet 1 kali sehari | http://terminology.kemkes.go.id/sp |
| 224 | 741 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001057 | 0.5 tablet 2 kali sehari | http://terminology.kemkes.go.id/sp |
| 225 | 742 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001058 | 1 tablet 2 kali sehari | http://terminology.kemkes.go.id/sp |
| 226 | 743 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001059 | 1.5 tablet 2 kali | http://terminology.kemkes.go.id/sp |
| 227 | 744 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001060 | 2 tablet 2 kali sehari | http://terminology.kemkes.go.id/sp |
| 228 | 745 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001061 | 0.5 tablet 3 kali | http://terminology.kemkes.go.id/sp |
| 229 | 746 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001062 | 1 tablet 3 kali sehari | http://terminology.kemkes.go.id/sp |
| 230 | 747 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001063 | 1.5 tablet 3 kali sehari | http://terminology.kemkes.go.id/sp |
| 231 | 748 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.item.item.answer.valueCoding` | SP001064 | 2 tablet 3 kali sehari | http://terminology.kemkes.go.id/sp |
| 232 | 771 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001086 | Bisa | http://terminology.kemkes.go.id/sp |
| 233 | 772 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001087 | Tidak, responden stroke | http://terminology.kemkes.go.id/sp |
| 234 | 773 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001088 | Tidak, responden lansia | http://terminology.kemkes.go.id/sp |
| 235 | 774 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001089 | Tidak, responden memiliki gangguan penglihatan | http://terminology.kemkes.go.id/sp |
| 236 | 775 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001090 | Tidak, respondedn ODGJ | http://terminology.kemkes.go.id/sp |
| 237 | 776 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001091 | Tidak, responden memiliki gangguan kognitif (contoh: Demensia) | http://terminology.kemkes.go.id/sp |
| 238 | 782 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001092 | Responden paham | http://terminology.kemkes.go.id/sp |
| 239 | 783 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001093 | Responden memiliki pertanyaan lanjutan | http://terminology.kemkes.go.id/sp |
| 240 | 786 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001092 | Responden paham | http://terminology.kemkes.go.id/sp |
| 241 | 787 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | SP001093 | Responden memiliki pertanyaan lanjutan | http://terminology.kemkes.go.id/sp |
| 242 | 790 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 102 | Pusat Kesehatan Masyarakat | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 243 | 791 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 103 | Klinik | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 244 | 792 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 101 | Praktek mandiri | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 245 | 793 | QuestionnaireResponse | `QuestionnaireResponse.item.answer.valueCoding` | 104 | Rumah Sakit | http://terminology.kemkes.go.id/CodeSystem/organization-type |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://terminology.kemkes.go.id/sp | 233 |
| http://terminology.kemkes.go.id/CodeSystem/organization-type | 7 |
| http://snomed.info/sct | 4 |
| http://loinc.org | 1 |
| **Total** | **245** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
