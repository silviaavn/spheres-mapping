# Output Form: MMS - Survei Sosio Ekonomi

Sumber: `mapping/phdt-data-dictionary-mms-sosio-ekonomi.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-mms-sosio-ekonomi.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 22 |
| Code (`jumlah code` = 1) | 229 |
| Code unik (code + CodeSystem) | 168 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 147 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–2 | Practitioner | – | – | _ID SID field staff yang melakukan survei sosio ekonomi_ → `Practitioner.identifier` (2, tanpa BQ) |
| 2 | 4–6 | Patient | – | – | _Nomor SID ID_ → `Patient.identifier.value` (4, tanpa BQ)<br>_Nama Lengkap Ibu_ → `Patient.name.text` (6, tanpa BQ)<br>_Tanggal lahir_ → `Patient.birthDate` (11, tanpa BQ)<br>_Asal Provinsi_ → `Patient.address.extension.url` (24, tanpa BQ)<br>_Asal Kabupaten_ → `Patient.address.extension.url` (27, tanpa BQ)<br>_Asal Kecamatan_ → `Patient.address.extension.url` (30, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.url` (37, tanpa BQ)<br>_Nama Dusun_ → `Patient.address.extension.url` (40, tanpa BQ) |
| 3 | 7–8 | RelatedPerson | – | – | _Nama Lengkap Suami_ → `RelatedPerson.patient.reference` (7, tanpa BQ) |
| 4 | 12–23 | Observation | 424144002 | Current chronological age | _Usia_ → `Observation.valueQuantity.value` (15, tanpa BQ) |
| 5 | 47–60 | Observation | SP000519 | Tipe Intervensi Puskesmas | _Tipe Intervensi Puskesmas_ → `Observation.valueCodeableConcept.coding` (50, tanpa BQ) |
| 6 | 61–72 | Observation | SP000524 | Umur pada saat perkawinan pertama | _Umur pada saat perkawinan pertama_ → `Observation.valueQuantity.value` (64, tanpa BQ) |
| 7 | 73–84 | Observation | SP000525 | Jumlah tahun dalam ikatan perkawinan | _Jumlah tahun dalam ikatan perkawinan_ → `Observation.valueQuantity.value` (76, tanpa BQ) |
| 8 | 85–96 | Observation | 423925001 | Family planning observable | _Rencana Penggunaan KB_ → `Observation.valueBoolean` (88, tanpa BQ) |
| 9 | 97–115 | Observation | 8659-5 | Birth control method - Reported | _Alat KB yang ingin digunakan_ → `Observation.valueCodeableConcept.coding` (100, tanpa BQ) |
| 10 | 116–135 | Observation | 85658-3 | Occupation [Type] | _Pekerjaan ibu (Responden)_ → `Observation.valueCodeableConcept.coding` (119, tanpa BQ) |
| 11 | 136–146 | Observation | 365552003 | Finding of income details | _Pemasukan ibu dari pekerjaan_ → `Observation.valueInteger` (139, tanpa BQ) |
| 12 | 147–165 | Observation | 85658-3 | Occupation [Type] | _Pekerjaan ayah (suami)_ → `Observation.valueCodeableConcept.coding` (150, tanpa BQ) |
| 13 | 166–177 | Observation | 365552003 | Finding of income details | _Pemasukan ayah (suami) dari pekerjaan_ → `Observation.valueInteger` (169, tanpa BQ) |
| 14 | 178–189 | Observation | 224525003 | Number in household | _Jumlah anggota keluarga dalam satu rumah_ → `Observation.valueInteger` (181, tanpa BQ) |
| 15 | 190–204 | Observation | 82589-3 | Highest level of education | _Pendidikan terakhir ibu (responden)_ → `Observation.valueCodeableConcept.coding` (193, tanpa BQ) |
| 16 | 205–219 | Observation | 82589-3 | Highest level of education | _Pendidikan terakhir ayah (suami)_ → `Observation.valueCodeableConcept.coding` (208, tanpa BQ) |
| 17 | 220–268 | QuestionnaireResponse | https://fhir.kemkes.go.id/sp/Questionnaire/Q0009 | – | _Apakah Anda bisa membaca sebagian dari kalimat ini untuk saya?_ → `QuestionnaireResponse.questionnaire` (220, tanpa BQ)<br>_Membaca koran atau majalah_ → `QuestionnaireResponse.item.linkId` (236, tanpa BQ)<br>_Mendengarkan radio_ → `QuestionnaireResponse.item.linkId` (242, tanpa BQ)<br>_Menonton televisi_ → `QuestionnaireResponse.item.linkId` (248, tanpa BQ)<br>_Kepemilikan telepon selular_ → `QuestionnaireResponse.item.linkId` (254, tanpa BQ)<br>_Penggunaan internet (pencarian, facebook, twitter, WhatsApp, BBM, online games, Instagram, tiktok, dll)_ → `QuestionnaireResponse.item.linkId` (257, tanpa BQ)<br>_Selama satu bulan, seberapa sering menggunakan internet_ → `QuestionnaireResponse.item.linkId` (263, tanpa BQ) |
| 18 | 269–400 | QuestionnaireResponse | https://fhir.kemkes.go.id/sp/Questionnaire/Q00010 | – | _Status kepemilikan bangunan tempat tinggal yang ditempati_ → `QuestionnaireResponse.questionnaire` (269, tanpa BQ)<br>_Jumlah anggota keluarga yang tidur dalam satu kamar tidur_ → `QuestionnaireResponse.item.linkId` (287, tanpa BQ)<br>_Jenis atap terluas_ → `QuestionnaireResponse.item.linkId` (290, tanpa BQ)<br>_Jenis dinding terluas_ → `QuestionnaireResponse.item.linkId` (303, tanpa BQ)<br>_Jenis lantai terluas_ → `QuestionnaireResponse.item.linkId` (320, tanpa BQ)<br>_Sumber air minum_ → `QuestionnaireResponse.item.linkId` (332, tanpa BQ)<br>_Apa yang biasa dilakukan untuk membuat air minum aman diminum?_ → `QuestionnaireResponse.item.linkId` (349, tanpa BQ)<br>_Penggunaan fasilitas tempat buang air besar_ → `QuestionnaireResponse.item.linkId` (359, tanpa BQ)<br>_Sumber penerangan_ → `QuestionnaireResponse.item.linkId` (370, tanpa BQ)<br>_Tempat kegiatan memasak_ → `QuestionnaireResponse.item.linkId` (377, tanpa BQ)<br>_Bahan bakar/energi utama untuk memasak_ → `QuestionnaireResponse.item.linkId` (383, tanpa BQ)<br>_Luas Bangunan_ → `QuestionnaireResponse.item.linkId` (395, tanpa BQ)<br>_Luas Tanah_ → `QuestionnaireResponse.item.linkId` (398, tanpa BQ) |
| 19 | 402–480 | QuestionnaireResponse | https://fhir.kemkes.go.id/sp/Questionnaire/Q00011 | – | _Makanan pokok: Beras_ → `QuestionnaireResponse.item.linkId` (412, tanpa BQ)<br>_Makanan pokok lainnya: jagung, terigu, tepung beras, tepung jagung,dll)_ → `QuestionnaireResponse.item.linkId` (415, tanpa BQ)<br>_Makanan pokok umbi-umbian (ketela pohon, ketela rambat, kentang, gaplek, talas, sagu,dll)_ → `QuestionnaireResponse.item.linkId` (418, tanpa BQ)<br>_Ikan/udang/cumi/ kerang yang segar/basah_ → `QuestionnaireResponse.item.linkId` (421, tanpa BQ)<br>_Ikan/udang/cumi/ kerang yang asin/diawetkan_ → `QuestionnaireResponse.item.linkId` (424, tanpa BQ)<br>_Daging (daging sapi, kerbau, kambing, domba, babi, ayam, jeroan, hati, limpa, abon, dendeng, dll)_ → `QuestionnaireResponse.item.linkId` (427, tanpa BQ)<br>_Telur ayam/itik/puyuh_ → `QuestionnaireResponse.item.linkId` (430, tanpa BQ)<br>_Susu murni, susu kental, susu bubuk, dll_ → `QuestionnaireResponse.item.linkId` (433, tanpa BQ)<br>_Sayur-sayuran (bayam, kangkung, ketimun, wortel, kacang panjang, buncis, bawang, cabe, tomat, dll)_ → `QuestionnaireResponse.item.linkId` (436, tanpa BQ)<br>_Kacang-kacangan (kacang tanah, hijau, kedele, merah, tunggak, mete, tahu, tempe, tauco, oncom, dll)_ → `QuestionnaireResponse.item.linkId` (439, tanpa BQ)<br>_Buah-buahan (jeruk, mangga, apel, durian, rambutan, salak, duku, nanas, semangka pisang, pepaya, dll)_ → `QuestionnaireResponse.item.linkId` (442, tanpa BQ)<br>_Minyak dan lemak (minyak kelapa/goreng, mentega, dll)_ → `QuestionnaireResponse.item.linkId` (445, tanpa BQ)<br>_Bahan minuman (gula pasir, gula merah, teh, kopi, coklat, sirup, dll)_ → `QuestionnaireResponse.item.linkId` (448, tanpa BQ)<br>_Bumbu-bumbuan (garam, kemiri, ketumbar, merica, terasi, kecap, vetsin, dll)_ → `QuestionnaireResponse.item.linkId` (451, tanpa BQ)<br>_Konsumsi lainnya (mie instant, mie basar, bihun, makaroni, mie kering)_ → `QuestionnaireResponse.item.linkId` (454, tanpa BQ)<br>_Konsumsi lainnya (kerupuk, emping, dll)_ → `QuestionnaireResponse.item.linkId` (457, tanpa BQ)<br>_Makanan jadi (roti, biskuit, kue basah, bubur, bakso, gado-gado, nasi rames, dll)_ → `QuestionnaireResponse.item.linkId` (460, tanpa BQ)<br>_Minuman non alkohol (soft drink, es sirop, limun, air mineral, dll)_ → `QuestionnaireResponse.item.linkId` (463, tanpa BQ)<br>_Minuman mengandung alkohol (bir, anggur, dan minuman keras lainnya)_ → `QuestionnaireResponse.item.linkId` (466, tanpa BQ)<br>_Rokok (rokok kretek, rokok putih, cerutu)_ → `QuestionnaireResponse.item.linkId` (469, tanpa BQ)<br>_Sirih/pinang/tembakau/lainnya_ → `QuestionnaireResponse.item.linkId` (472, tanpa BQ)<br>_Jumlah pengeluaran makanan_ → `QuestionnaireResponse.item.linkId` (475, tanpa BQ)<br>_Rata-rata pengeluaran makanan per bulan_ → `QuestionnaireResponse.item.linkId` (478, tanpa BQ) |
| 20 | 481–564 | QuestionnaireResponse | https://fhir.kemkes.go.id/sp/Questionnaire/Q00012 | – | _Perkiraan biaya sewa rumah_ → `QuestionnaireResponse.item.linkId` (491, tanpa BQ)<br>_Pemeliharaan rumah dan perbaikan ringan_ → `QuestionnaireResponse.item.linkId` (494, tanpa BQ)<br>_Rekening listrik, air, gas, minyak tanah, kayu bakar, dll_ → `QuestionnaireResponse.item.linkId` (497, tanpa BQ)<br>_Rekening telepon, rumah, pulsa HP, telepon umum, wartel, benda pos, dll)_ → `QuestionnaireResponse.item.linkId` (500, tanpa BQ)<br>_Sabun mandi/cuci, kosmetik, perawatan rambut/muka, tissue dll_ → `QuestionnaireResponse.item.linkId` (503, tanpa BQ)<br>_Biaya kesehatan (rumah sakit, puskesmas, dokter praktek, dukun,obat-obatan, dan lainnya)_ → `QuestionnaireResponse.item.linkId` (506, tanpa BQ)<br>_Biaya pendidikan (uang pendaftaran, SPP, POMG/BP3, uang pangkal/daftar uang, pramuka, prakarya, kursus, dan lainnya)_ → `QuestionnaireResponse.item.linkId` (509, tanpa BQ)<br>_Transportasi, pengangkutan, bensin, solar, minyak pelumas_ → `QuestionnaireResponse.item.linkId` (512, tanpa BQ)<br>_Jasa lainnya (gaji sopir, pembantu rumah tangga, hotel, dll)_ → `QuestionnaireResponse.item.linkId` (515, tanpa BQ)<br>_Pakaian, alas kaki, dan tutup kepala (pakaian jadi, bahan pakaian, sepatu, topi, dan lainnya)_ → `QuestionnaireResponse.item.linkId` (518, tanpa BQ)<br>_Barang tahan lama (alat rumah tangga, perkakas, alat dapur, alat hiburan (elektronik), alat olahraga, perhiasan, kendaraan, payung, arloji, kamera, HP, pasang telepon, pasang listrik, barang elektronik, dll)_ → `QuestionnaireResponse.item.linkId` (521, tanpa BQ)<br>_Pajak (PBB, pajak kendaraan)_ → `QuestionnaireResponse.item.linkId` (524, tanpa BQ)<br>_Pungutan/retribusi_ → `QuestionnaireResponse.item.linkId` (527, tanpa BQ)<br>_Asuransi kesehatan_ → `QuestionnaireResponse.item.linkId` (530, tanpa BQ)<br>_Lainnya (asuransi lainnya, tilang, PPh, dll)_ → `QuestionnaireResponse.item.linkId` (533, tanpa BQ)<br>_Keperluan pesta dan upacara/kenduri tidak termasuk makaanan (perkawinan, ulang tahum khitanan, upacara keagamaan, upacara adat, dan lainnya)_ → `QuestionnaireResponse.item.linkId` (536, tanpa BQ)<br>_Jumlah pengeluaran bukan makanan_ → `QuestionnaireResponse.item.linkId` (539, tanpa BQ)<br>_Rata-rata pengeluaran bukan makanan per bulan_ → `QuestionnaireResponse.item.linkId` (542, tanpa BQ)<br>_Sumber penghasilan terbesar rumah tangga (anggota rumah tangga dengan penghasilan terbesar) Lapangan usaha_ → `QuestionnaireResponse.item.linkId` (545, tanpa BQ) |
| 21 | 565–601 | QuestionnaireResponse | https://fhir.kemkes.go.id/sp/Questionnaire/Q00013 | – | _Daftar aset atau kepemilikan barang_ → `QuestionnaireResponse.item.linkId` (575, tanpa BQ)<br>_Apakah rumah tangga ini memiliki akses ke internet selama sebulan terakhir_ → `QuestionnaireResponse.item.linkId` (588, tanpa BQ)<br>_Kepemillikan kendaraan_ → `QuestionnaireResponse.item.linkId` (591, tanpa BQ)<br>_Rekening bank_ → `QuestionnaireResponse.item.linkId` (599, tanpa BQ) |
| 22 | 602–650 | QuestionnaireResponse | https://fhir.kemkes.go.id/sp/Questionnaire/Q00014 | – | _Kepemilikan lahan pertanian?_ → `QuestionnaireResponse.item.linkId` (612, tanpa BQ)<br>_Sapi jantan/betina_ → `QuestionnaireResponse.item.linkId` (615, tanpa BQ)<br>_Kerbau_ → `QuestionnaireResponse.item.linkId` (621, tanpa BQ)<br>_Kuda/keledai/bagul_ → `QuestionnaireResponse.item.linkId` (627, tanpa BQ)<br>_Kambing/domba_ → `QuestionnaireResponse.item.linkId` (633, tanpa BQ)<br>_Babi_ → `QuestionnaireResponse.item.linkId` (639, tanpa BQ)<br>_Ayam/unggas_ → `QuestionnaireResponse.item.linkId` (645, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 13 |
| QuestionnaireResponse | 6 |
| Practitioner | 1 |
| Patient | 1 |
| RelatedPerson | 1 |
| **Total** | **22** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 14 | Observation | `Observation.code.coding` | 424144002 | Current chronological age | http://snomed.info/sct |
| 2 | 49 | Observation | `Observation.code.coding` | SP000519 | Tipe Intervensi Puskesmas | http://terminology.kemkes.go.id/sp |
| 3 | 50 | Observation | `Observation.valueCodeableConcept.coding` | SP000520 | Blister Digital | http://terminology.kemkes.go.id/sp |
| 4 | 51 | Observation | `Observation.valueCodeableConcept.coding` | SP000521 | Blister Non Digital | http://terminology.kemkes.go.id/sp |
| 5 | 52 | Observation | `Observation.valueCodeableConcept.coding` | SP000522 | Botol Digital | http://terminology.kemkes.go.id/sp |
| 6 | 53 | Observation | `Observation.valueCodeableConcept.coding` | SP000523 | Botol Non Digital | http://terminology.kemkes.go.id/sp |
| 7 | 63 | Observation | `Observation.code.coding` | SP000524 | Umur pada saat perkawinan pertama | http://terminology.kemkes.go.id/sp |
| 8 | 75 | Observation | `Observation.code.coding` | SP000525 | Jumlah tahun dalam ikatan perkawinan | http://terminology.kemkes.go.id/sp |
| 9 | 87 | Observation | `Observation.code.coding` | 423925001 | Family planning observable | http://snomed.info/sct |
| 10 | 99 | Observation | `Observation.code.coding` | 8659-5 | Birth control method - Reported | http://loinc.org |
| 11 | 100 | Observation | `Observation.valueCodeableConcept.coding` | 77543007 | Ligation of fallopian tube | http://snomed.info/sct |
| 12 | 101 | Observation | `Observation.valueCodeableConcept.coding` | 22523008 | Vasectomy | http://snomed.info/sct |
| 13 | 102 | Observation | `Observation.valueCodeableConcept.coding` | LA6527-1 | Intrauterine device | http://loinc.org |
| 14 | 103 | Observation | `Observation.valueCodeableConcept.coding` | LA6525-5 | Injectable/implantable hormone | http://loinc.org |
| 15 | 104 | Observation | `Observation.valueCodeableConcept.coding` | SP000097 | Implan | http://terminology.kemkes.go.id/sp |
| 16 | 105 | Observation | `Observation.valueCodeableConcept.coding` | LA6524-8 | Oral contraceptive pill | http://loinc.org |
| 17 | 106 | Observation | `Observation.valueCodeableConcept.coding` | LA6523-0 | Condom | http://loinc.org |
| 18 | 107 | Observation | `Observation.valueCodeableConcept.coding` | 442288006 | Female condom, device | http://snomed.info/sct |
| 19 | 108 | Observation | `Observation.valueCodeableConcept.coding` | 225371000 | Uses natural method of contraception | http://snomed.info/sct |
| 20 | 118 | Observation | `Observation.code.coding` | 85658-3 | Occupation [Type] | http://loinc.org |
| 21 | 119 | Observation | `Observation.valueCodeableConcept.coding` | 741062008 | Not in labor force | http://snomed.info/sct |
| 22 | 120 | Observation | `Observation.valueCodeableConcept.coding` | 65853000 | Student | http://snomed.info/sct |
| 23 | 121 | Observation | `Observation.valueCodeableConcept.coding` | 236297007 | Civil servant | http://snomed.info/sct |
| 24 | 122 | Observation | `Observation.valueCodeableConcept.coding` | SP000218 | Karyawan Swasta | http://terminology.kemkes.go.id/sp |
| 25 | 123 | Observation | `Observation.valueCodeableConcept.coding` | 160906004 | Self-employed | http://snomed.info/sct |
| 26 | 124 | Observation | `Observation.valueCodeableConcept.coding` | 444168002 | Homemaker | http://snomed.info/sct |
| 27 | 125 | Observation | `Observation.valueCodeableConcept.coding` | 702479006 | At high risk of sexually transmitted infection | http://snomed.info/sct |
| 28 | 126 | Observation | `Observation.valueCodeableConcept.coding` | 106540006 | Laborer | http://snomed.info/sct |
| 29 | 127 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 30 | 138 | Observation | `Observation.code.coding` | 365552003 | Finding of income details | http://snomed.info/sct |
| 31 | 149 | Observation | `Observation.code.coding` | 85658-3 | Occupation [Type] | http://loinc.org |
| 32 | 150 | Observation | `Observation.valueCodeableConcept.coding` | 741062008 | Not in labor force | http://snomed.info/sct |
| 33 | 151 | Observation | `Observation.valueCodeableConcept.coding` | 65853000 | Student | http://snomed.info/sct |
| 34 | 152 | Observation | `Observation.valueCodeableConcept.coding` | 236297007 | Civil servant | http://snomed.info/sct |
| 35 | 153 | Observation | `Observation.valueCodeableConcept.coding` | SP000218 | Karyawan Swasta | http://terminology.kemkes.go.id/sp |
| 36 | 154 | Observation | `Observation.valueCodeableConcept.coding` | 160906004 | Self-employed | http://snomed.info/sct |
| 37 | 155 | Observation | `Observation.valueCodeableConcept.coding` | 702479006 | At high risk of sexually transmitted infection | http://snomed.info/sct |
| 38 | 156 | Observation | `Observation.valueCodeableConcept.coding` | 106540006 | Laborer | http://snomed.info/sct |
| 39 | 157 | Observation | `Observation.valueCodeableConcept.coding` | 74964007 | Other | http://snomed.info/sct |
| 40 | 168 | Observation | `Observation.code.coding` | 365552003 | Finding of income details | http://snomed.info/sct |
| 41 | 180 | Observation | `Observation.code.coding` | 224525003 | Number in household | http://snomed.info/sct |
| 42 | 192 | Observation | `Observation.code.coding` | 82589-3 | Highest level of education | http://loinc.org |
| 43 | 193 | Observation | `Observation.valueCodeableConcept.coding` | 224294005 | No formal education | http://snomed.info/sct |
| 44 | 194 | Observation | `Observation.dataAbsentReason.coding` | unknown | Unknown | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 45 | 195 | Observation | `Observation.valueCodeableConcept.coding` | 473463000 | Received elementary school education | http://snomed.info/sct |
| 46 | 196 | Observation | `Observation.valueCodeableConcept.coding` | 603435002 | Educated to junior high school level | http://snomed.info/sct |
| 47 | 197 | Observation | `Observation.valueCodeableConcept.coding` | 603434003 | Educated to senior high school level | http://snomed.info/sct |
| 48 | 198 | Observation | `Observation.valueCodeableConcept.coding` | 38861000087100 | Bachelor's degree achieved | http://snomed.info/sct |
| 49 | 207 | Observation | `Observation.code.coding` | 82589-3 | Highest level of education | http://loinc.org |
| 50 | 208 | Observation | `Observation.valueCodeableConcept.coding` | 224294005 | No formal education | http://snomed.info/sct |
| 51 | 209 | Observation | `Observation.dataAbsentReason.coding` | unknown | Unknown | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 52 | 210 | Observation | `Observation.valueCodeableConcept.coding` | 473463000 | Received elementary school education | http://snomed.info/sct |
| 53 | 211 | Observation | `Observation.valueCodeableConcept.coding` | 603435002 | Educated to junior high school level | http://snomed.info/sct |
| 54 | 212 | Observation | `Observation.valueCodeableConcept.coding` | 603434003 | Educated to senior high school level | http://snomed.info/sct |
| 55 | 213 | Observation | `Observation.valueCodeableConcept.coding` | 38861000087100 | Bachelor's degree achieved | http://snomed.info/sct |
| 56 | 232 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000526 | Tidak bisa membaca sama sekali | http://terminology.kemkes.go.id/sp |
| 57 | 233 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000527 | Hanya bisa membaca sebagian kalimat | http://terminology.kemkes.go.id/sp |
| 58 | 234 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000528 | Bisa membaca seluruh kalimat | http://terminology.kemkes.go.id/sp |
| 59 | 235 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 193699007 | Blindness - both eyes | http://snomed.info/sct |
| 60 | 238 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000529 | Hampir setiap hari | http://terminology.kemkes.go.id/sp |
| 61 | 239 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000530 | 1 minggu sekali | http://terminology.kemkes.go.id/sp |
| 62 | 240 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000531 | kurang dari 1 kali seminggu | http://terminology.kemkes.go.id/sp |
| 63 | 241 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000532 | tidak sama sekali | http://terminology.kemkes.go.id/sp |
| 64 | 244 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000529 | Hampir setiap hari | http://terminology.kemkes.go.id/sp |
| 65 | 245 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000530 | 1 minggu sekali | http://terminology.kemkes.go.id/sp |
| 66 | 246 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000531 | kurang dari 1 kali seminggu | http://terminology.kemkes.go.id/sp |
| 67 | 247 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000532 | tidak sama sekali | http://terminology.kemkes.go.id/sp |
| 68 | 250 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000529 | Hampir setiap hari | http://terminology.kemkes.go.id/sp |
| 69 | 251 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000530 | 1 minggu sekali | http://terminology.kemkes.go.id/sp |
| 70 | 252 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000531 | kurang dari 1 kali seminggu | http://terminology.kemkes.go.id/sp |
| 71 | 253 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000532 | tidak sama sekali | http://terminology.kemkes.go.id/sp |
| 72 | 259 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000529 | Hampir setiap hari | http://terminology.kemkes.go.id/sp |
| 73 | 260 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000530 | 1 minggu sekali | http://terminology.kemkes.go.id/sp |
| 74 | 261 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000531 | kurang dari 1 kali seminggu | http://terminology.kemkes.go.id/sp |
| 75 | 262 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000532 | tidak sama sekali | http://terminology.kemkes.go.id/sp |
| 76 | 265 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000529 | Hampir setiap hari | http://terminology.kemkes.go.id/sp |
| 77 | 266 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000530 | 1 minggu sekali | http://terminology.kemkes.go.id/sp |
| 78 | 267 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000531 | kurang dari 1 kali seminggu | http://terminology.kemkes.go.id/sp |
| 79 | 268 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000532 | tidak sama sekali | http://terminology.kemkes.go.id/sp |
| 80 | 281 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 160943002 | Lives in own home | http://snomed.info/sct |
| 81 | 282 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 224213000 | Lives in rented accommodation | http://snomed.info/sct |
| 82 | 283 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000533 | Bebas Sewa | http://terminology.kemkes.go.id/sp |
| 83 | 284 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000534 | Rumah Dinas | http://terminology.kemkes.go.id/sp |
| 84 | 285 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000535 | Rumah Keluarga | http://terminology.kemkes.go.id/sp |
| 85 | 286 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 74964007 | Other | http://snomed.info/sct |
| 86 | 292 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000536 | Jerami/daun kelapa | http://terminology.kemkes.go.id/sp |
| 87 | 293 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000537 | Rumput tanah | http://terminology.kemkes.go.id/sp |
| 88 | 294 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000538 | Anyaman kasar | http://terminology.kemkes.go.id/sp |
| 89 | 295 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 698018008 | Bamboo | http://snomed.info/sct |
| 90 | 296 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000539 | Seng/atap loga | http://terminology.kemkes.go.id/sp |
| 91 | 297 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 16369005 | Asbestos | http://snomed.info/sct |
| 92 | 298 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000540 | Genteng | http://terminology.kemkes.go.id/sp |
| 93 | 299 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000541 | Beton | http://terminology.kemkes.go.id/sp |
| 94 | 300 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000542 | Seng | http://terminology.kemkes.go.id/sp |
| 95 | 301 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000543 | Sirap atap | http://terminology.kemkes.go.id/sp |
| 96 | 302 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 74964007 | Other | http://snomed.info/sct |
| 97 | 305 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000544 | Tebu/daun kelapa/batang pohon | http://terminology.kemkes.go.id/sp |
| 98 | 306 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000545 | Bambu dengan lumpur/tanah | http://terminology.kemkes.go.id/sp |
| 99 | 307 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000546 | Batu dengan lumpur | http://terminology.kemkes.go.id/sp |
| 100 | 308 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000547 | Bata tanah tanpa pelapis | http://terminology.kemkes.go.id/sp |
| 101 | 309 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000548 | Kayu lapis (plywood) | http://terminology.kemkes.go.id/sp |
| 102 | 310 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000549 | Kardus | http://terminology.kemkes.go.id/sp |
| 103 | 311 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000550 | Kayu bekas | http://terminology.kemkes.go.id/sp |
| 104 | 312 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000551 | Anyaman Bambu | http://terminology.kemkes.go.id/sp |
| 105 | 313 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000552 | Batu dengan kapur/semen | http://terminology.kemkes.go.id/sp |
| 106 | 314 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000553 | Batako semen | http://terminology.kemkes.go.id/sp |
| 107 | 315 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000554 | Bata tanah berlapis semen | http://terminology.kemkes.go.id/sp |
| 108 | 316 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000555 | Papan kayu/sirap | http://terminology.kemkes.go.id/sp |
| 109 | 317 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000556 | Kawat Plester | http://terminology.kemkes.go.id/sp |
| 110 | 318 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000557 | GRC/Gypsum/Asbes | http://terminology.kemkes.go.id/sp |
| 111 | 319 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 74964007 | Other | http://snomed.info/sct |
| 112 | 322 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000558 | Tanah/pasir/kotoran | http://terminology.kemkes.go.id/sp |
| 113 | 323 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000559 | Papan kayu | http://terminology.kemkes.go.id/sp |
| 114 | 324 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000560 | Anyaman daun kelapa/bambu | http://terminology.kemkes.go.id/sp |
| 115 | 325 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000561 | Parket atau kayu yang dipoles | http://terminology.kemkes.go.id/sp |
| 116 | 326 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000562 | Vinyl atau aspal lembaran | http://terminology.kemkes.go.id/sp |
| 117 | 327 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000563 | Keramik atau marmer | http://terminology.kemkes.go.id/sp |
| 118 | 328 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000564 | Ubin keramik | http://terminology.kemkes.go.id/sp |
| 119 | 329 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000565 | Semen/Bata merah | http://terminology.kemkes.go.id/sp |
| 120 | 330 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000566 | Karpet | http://terminology.kemkes.go.id/sp |
| 121 | 331 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 74964007 | Other | http://snomed.info/sct |
| 122 | 334 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000567 | Air ledeng - masuk ke dalam rumah | http://terminology.kemkes.go.id/sp |
| 123 | 335 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000568 | Air ledeng - ke halaman atau lahan | http://terminology.kemkes.go.id/sp |
| 124 | 336 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000569 | Air ledeng - ke rumah tetangga | http://terminology.kemkes.go.id/sp |
| 125 | 337 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000570 | Sumur bor atau pompa tangan | http://terminology.kemkes.go.id/sp |
| 126 | 338 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000571 | Sumur gali - terlindung | http://terminology.kemkes.go.id/sp |
| 127 | 339 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000572 | Sumur gali - tidak terlindung | http://terminology.kemkes.go.id/sp |
| 128 | 340 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000573 | Mata air - terlindung | http://terminology.kemkes.go.id/sp |
| 129 | 341 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000574 | Mata air - tidak terlindung | http://terminology.kemkes.go.id/sp |
| 130 | 342 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000575 | Air hujan | http://terminology.kemkes.go.id/sp |
| 131 | 343 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000576 | Mobil tangki | http://terminology.kemkes.go.id/sp |
| 132 | 344 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000577 | Gerobak air dengan tangki kecil | http://terminology.kemkes.go.id/sp |
| 133 | 345 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000578 | Air permukaan (sungai/bendungan/danau/kolam/selokan/saluran irigasi) | http://terminology.kemkes.go.id/sp |
| 134 | 346 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000579 | Air kemasan botol | http://terminology.kemkes.go.id/sp |
| 135 | 347 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000580 | Air isi ulang | http://terminology.kemkes.go.id/sp |
| 136 | 348 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 74964007 | Other | http://snomed.info/sct |
| 137 | 351 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000581 | Dimasak/Didihkan | http://terminology.kemkes.go.id/sp |
| 138 | 352 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000582 | Tambahkan pemutih/klorin | http://terminology.kemkes.go.id/sp |
| 139 | 353 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000583 | Saring dengan kain | http://terminology.kemkes.go.id/sp |
| 140 | 354 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000584 | Gunakan saringan air (keramik/pasir/komposit, dll) | http://terminology.kemkes.go.id/sp |
| 141 | 355 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000585 | Disinfeksi dengan sinar matahari | http://terminology.kemkes.go.id/sp |
| 142 | 356 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000586 | Diamkan hingga mengendap | http://terminology.kemkes.go.id/sp |
| 143 | 358 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 74964007 | Other | http://snomed.info/sct |
| 144 | 361 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000587 | Milik pribadi dengan tangki septik | http://terminology.kemkes.go.id/sp |
| 145 | 362 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000588 | Milik pribadi tanpa tangki septik | http://terminology.kemkes.go.id/sp |
| 146 | 363 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000589 | Bersama/umum | http://terminology.kemkes.go.id/sp |
| 147 | 364 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000590 | Sungai/aliran air/parit | http://terminology.kemkes.go.id/sp |
| 148 | 365 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000591 | Pantai | http://terminology.kemkes.go.id/sp |
| 149 | 366 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000592 | Kolam/telaga | http://terminology.kemkes.go.id/sp |
| 150 | 367 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000593 | Lubang tanah | http://terminology.kemkes.go.id/sp |
| 151 | 368 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000594 | Halaman/semak/hutan | http://terminology.kemkes.go.id/sp |
| 152 | 369 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 74964007 | Other | http://snomed.info/sct |
| 153 | 372 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000595 | Listrik PLN | http://terminology.kemkes.go.id/sp |
| 154 | 373 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000596 | Listrik non PLN | http://terminology.kemkes.go.id/sp |
| 155 | 374 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000597 | Petromak/aladin | http://terminology.kemkes.go.id/sp |
| 156 | 375 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000598 | Pelita/sentir/obor | http://terminology.kemkes.go.id/sp |
| 157 | 379 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000599 | Dalam rumah | http://terminology.kemkes.go.id/sp |
| 158 | 380 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000600 | Di bangunan terpisah | http://terminology.kemkes.go.id/sp |
| 159 | 381 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000601 | Di luar ruangan | http://terminology.kemkes.go.id/sp |
| 160 | 382 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 74964007 | Other | http://snomed.info/sct |
| 161 | 385 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000602 | Listrik | http://terminology.kemkes.go.id/sp |
| 162 | 386 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000603 | LPG | http://terminology.kemkes.go.id/sp |
| 163 | 387 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000604 | Gas Alam (City Gas/CNG/LNG) | http://terminology.kemkes.go.id/sp |
| 164 | 388 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000605 | Biogas (Gas dari limbah organik) | http://terminology.kemkes.go.id/sp |
| 165 | 389 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000606 | Minyak tanah | http://terminology.kemkes.go.id/sp |
| 166 | 390 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000607 | Batu bara/lignit | http://terminology.kemkes.go.id/sp |
| 167 | 391 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000608 | Arang | http://terminology.kemkes.go.id/sp |
| 168 | 392 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000609 | Kayu bakar | http://terminology.kemkes.go.id/sp |
| 169 | 393 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000536 | Jerami/daun kelapa | http://terminology.kemkes.go.id/sp |
| 170 | 394 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 74964007 | Other | http://snomed.info/sct |
| 171 | 547 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000610 | Pertanian, perburuan, dan kehutanan | http://terminology.kemkes.go.id/sp |
| 172 | 548 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000611 | Perikanan | http://terminology.kemkes.go.id/sp |
| 173 | 549 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000612 | Pertambangan dan penggalian | http://terminology.kemkes.go.id/sp |
| 174 | 550 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000613 | Industri pengolahan | http://terminology.kemkes.go.id/sp |
| 175 | 551 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000614 | Litrik, gas, dan air | http://terminology.kemkes.go.id/sp |
| 176 | 552 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000615 | Konstruksi | http://terminology.kemkes.go.id/sp |
| 177 | 553 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000616 | Perdagangan besar dan eceran | http://terminology.kemkes.go.id/sp |
| 178 | 554 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000617 | Penyediaan akomodasi & penyediaan makan dan minum | http://terminology.kemkes.go.id/sp |
| 179 | 555 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000618 | Transportasi, pergudangan, dan komunikasi | http://terminology.kemkes.go.id/sp |
| 180 | 556 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000619 | Perantara keuangan | http://terminology.kemkes.go.id/sp |
| 181 | 557 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000620 | Real estate, usaha persewaan dan jasa perusahaan | http://terminology.kemkes.go.id/sp |
| 182 | 558 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000621 | Administrasi pemerintahan, pertahanan, dan jaminan sosial wajib | http://terminology.kemkes.go.id/sp |
| 183 | 559 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000622 | Jasa pendidikan | http://terminology.kemkes.go.id/sp |
| 184 | 560 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000623 | Jasa kesehatan dan kegiatan sosial | http://terminology.kemkes.go.id/sp |
| 185 | 561 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000624 | Jasa kemasyarakatan, sosial, budaya, dan perorangan | http://terminology.kemkes.go.id/sp |
| 186 | 562 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000625 | Jasa perorangan yang melayanani rumah tangga | http://terminology.kemkes.go.id/sp |
| 187 | 563 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000626 | Badan internasional dan badan ekstra internasional lainnya | http://terminology.kemkes.go.id/sp |
| 188 | 564 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 74964007 | Other | http://snomed.info/sct |
| 189 | 577 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 18213006 | Electricity | http://snomed.info/sct |
| 190 | 578 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 360004001 | Radio | http://snomed.info/sct |
| 191 | 579 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 255712000 | Television | http://snomed.info/sct |
| 192 | 580 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 160941000 | Telephone in house | http://snomed.info/sct |
| 193 | 581 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 706692004 | Computer | http://snomed.info/sct |
| 194 | 582 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 21546008 | Refrigerator, device | http://snomed.info/sct |
| 195 | 583 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 261259003 | Fan | http://snomed.info/sct |
| 196 | 584 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 470667006 | Laundry washing machine | http://snomed.info/sct |
| 197 | 585 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 15000008 | Air-conditioner | http://snomed.info/sct |
| 198 | 586 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000627 | Jam tangan | http://terminology.kemkes.go.id/sp |
| 199 | 587 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 1187059002 | Smartphone | http://snomed.info/sct |
| 200 | 593 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 260413007 | None | http://snomed.info/sct |
| 201 | 594 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 70224005 | Bicycle, device | http://snomed.info/sct |
| 202 | 595 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 90748009 | Motorcycle, device | http://snomed.info/sct |
| 203 | 596 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 90963000 | Animal drawn vehicle, device | http://snomed.info/sct |
| 204 | 597 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 71783008 | Automobile, device | http://snomed.info/sct |
| 205 | 598 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 49623006 | Powered watercraft, device | http://snomed.info/sct |
| 206 | 617 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 276727009 | Null | http://snomed.info/sct |
| 207 | 618 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000628 | 1 hingga 4 | http://terminology.kemkes.go.id/sp |
| 208 | 619 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000629 | 5 hingga 9 | http://terminology.kemkes.go.id/sp |
| 209 | 620 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000630 | 10+ | http://terminology.kemkes.go.id/sp |
| 210 | 623 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 276727009 | Null | http://snomed.info/sct |
| 211 | 624 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000628 | 1 hingga 4 | http://terminology.kemkes.go.id/sp |
| 212 | 625 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000629 | 5 hingga 9 | http://terminology.kemkes.go.id/sp |
| 213 | 626 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000630 | 10+ | http://terminology.kemkes.go.id/sp |
| 214 | 629 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 276727009 | Null | http://snomed.info/sct |
| 215 | 630 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000628 | 1 hingga 4 | http://terminology.kemkes.go.id/sp |
| 216 | 631 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000629 | 5 hingga 9 | http://terminology.kemkes.go.id/sp |
| 217 | 632 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000630 | 10+ | http://terminology.kemkes.go.id/sp |
| 218 | 635 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 276727009 | Null | http://snomed.info/sct |
| 219 | 636 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000628 | 1 hingga 4 | http://terminology.kemkes.go.id/sp |
| 220 | 637 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000629 | 5 hingga 9 | http://terminology.kemkes.go.id/sp |
| 221 | 638 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000630 | 10+ | http://terminology.kemkes.go.id/sp |
| 222 | 641 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 276727009 | Null | http://snomed.info/sct |
| 223 | 642 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000628 | 1 hingga 4 | http://terminology.kemkes.go.id/sp |
| 224 | 643 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000629 | 5 hingga 9 | http://terminology.kemkes.go.id/sp |
| 225 | 644 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000630 | 10+ | http://terminology.kemkes.go.id/sp |
| 226 | 647 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | 276727009 | Null | http://snomed.info/sct |
| 227 | 648 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000631 | 1 hingga 9 | http://terminology.kemkes.go.id/sp |
| 228 | 649 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000632 | 10 hingga 29 | http://terminology.kemkes.go.id/sp |
| 229 | 650 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000633 | 30+ | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://terminology.kemkes.go.id/sp | 147 |
| http://snomed.info/sct | 71 |
| http://loinc.org | 9 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 2 |
| **Total** | **229** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 3 | – | Tanggal entry | – | `` |
| 9 | – | Tanggal lahir ibu diketahui? | – | `` |
| 33 | – | Asal Puskesmas | Organization | `Organization.active` |
| 43 | – | Posyandu | Organization | `Organization.active` |
| 401 | – | Konversi luas tanah dari satuan are ke satuan meter persegi | – | `` |
