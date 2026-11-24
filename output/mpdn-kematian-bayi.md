# Output Form: MPDN Kematian Bayi

Sumber: `mapping/phdt-data-dictionary-mpdn-kematian-bayi.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-mpdn-kematian-bayi.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 19 |
| Code (`jumlah code` = 1) | 112 |
| Code unik (code + CodeSystem) | 76 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 37 |
| Variabel BQ (unik) | 0 |
| Variabel raw (variabel dictionary; belum ada file mentah) | 37 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 4–22 | Patient | – | – | _Nama Ibu Hamil_ → `Patient.name` (4, tanpa BQ)<br>_KTP/NIK Ibu_ → `Patient.identifier.value` (9, tanpa BQ)<br>_Nomor Hp/Kontak Keluarga_ → `Patient.telecom.value` (12, tanpa BQ)<br>_Kabupaten/Kota KTP_ → `Patient.address.city` (13, tanpa BQ)<br>_Provinsi KTP_ → `Patient.address.extension:administrativeCode.extension:province` (16, tanpa BQ)<br>_Kabupaten/Kota KTP_ → `Patient.address.extension:administrativeCode.extension:city` (17, tanpa BQ)<br>_Provinsi Domisili_ → `Patient.address.extension:administrativeCode.extension:province` (19, tanpa BQ)<br>_Kabupaten/Kota Domisili_ → `Patient.address.extension:administrativeCode.extension:city` (20, tanpa BQ)<br>_Kecamatan Domisili_ → `Patient.address.extension:administrativeCode.extension:district` (21, tanpa BQ)<br>_Desa/Kelurahan Domisili_ → `Patient.address.extension:administrativeCode.extension:village` (22, tanpa BQ) |
| 2 | 23–39 | Patient | – | – | _nama bayi (generated)_ → `Patient.name` (23, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (26, tanpa BQ)<br>_KTP/NIK Ibu_ → `Patient.identifier.value` (30, tanpa BQ)<br>_Tgl. Lahir_ → `Patient.birthDate` (31, tanpa BQ)<br>_Nama Ibu Hamil_ → `Patient.contact.name.text` (34, tanpa BQ)<br>_Nomor Hp/Kontak Keluarga_ → `Patient.contact.telecom.value` (37, tanpa BQ)<br>_Kembar_ → `Patient.multipleBirthBoolean` (38, tanpa BQ) |
| 3 | 43–55 | Observation | 64710-7 | Was your pregnancy a live birth, stillbirth, miscarriage, abortion, or ectopic pregnancy [PhenX] | _Lahir Mati_ → `Observation.valueCodeableConcept.coding` (46, tanpa BQ)<br>_nama pasien 1_ → `Observation.subject.display` (49, tanpa BQ)<br>_nama pasien 2 (hanya lahir mati)_ → `Observation.focus.display` (51, tanpa BQ)<br>_Tgl. Meninggal_ → `Observation.effectiveDateTime` (52, tanpa BQ)<br>_Wkt. Lapor_ → `Observation.issued` (53, tanpa BQ)<br>_//PJ MPDN_ → `Observation.performer.display` (55, tanpa BQ) |
| 4 | 56–75 | Observation | 39016-1 | Age at death | _Usia Meninggal (Hari)_ → `Observation.valueQuantity.value` (59, tanpa BQ)<br>_nama pasien bayi (hanya lahir hidup)_ → `Observation.subject.display` (71, tanpa BQ)<br>_Tgl. Meninggal_ → `Observation.effectiveDateTime` (72, tanpa BQ)<br>_Wkt. Lapor_ → `Observation.issued` (73, tanpa BQ)<br>_//PJ MPDN_ → `Observation.performer.display` (75, tanpa BQ) |
| 5 | 76–87 | Observation | 81956-5 | Date and time of death [TimeStamp] | _Tgl. Meninggal_ → `Observation.status` (76, tanpa BQ)<br>_Jam Meninggal_ → `Observation.valueDateTime` (79, tanpa BQ)<br>_nama pasien 1_ → `Observation.subject.display` (81, tanpa BQ)<br>_nama pasien 2 (hanya lahir mati)_ → `Observation.focus.display` (83, tanpa BQ)<br>_Tgl. Meninggal_ → `Observation.effectiveDateTime` (84, tanpa BQ)<br>_Wkt. Lapor_ → `Observation.issued` (85, tanpa BQ)<br>_//PJ MPDN_ → `Observation.performer.display` (87, tanpa BQ) |
| 6 | 88–105 | Observation | 79378-6 | Cause of death | _Dugaan Sebab_ → `Observation.component.valueCodeableConcept.coding` (91, tanpa BQ)<br>_Diagnosis_ → `Observation.note` (96, tanpa BQ)<br>_nama pasien 1_ → `Observation.subject.display` (99, tanpa BQ)<br>_nama pasien 2 (hanya lahir mati)_ → `Observation.focus.display` (101, tanpa BQ)<br>_Tgl. Meninggal_ → `Observation.effectiveDateTime` (102, tanpa BQ)<br>_Wkt. Lapor_ → `Observation.issued` (103, tanpa BQ)<br>_//PJ MPDN_ → `Observation.performer.display` (105, tanpa BQ) |
| 7 | 106–137 | Observation | OC000028 | Jenis Tempat Meninggal | _Tempat Meninggal_ → `Observation.valueCodeableConcept.coding` (109, tanpa BQ)<br>_nama pasien 1_ → `Observation.subject.display` (131, tanpa BQ)<br>_nama pasien 2 (hanya lahir mati)_ → `Observation.focus.display` (133, tanpa BQ)<br>_Tgl. Meninggal_ → `Observation.effectiveDateTime` (134, tanpa BQ)<br>_Wkt. Lapor_ → `Observation.issued` (135, tanpa BQ)<br>_//PJ MPDN_ → `Observation.performer.display` (137, tanpa BQ) |
| 8 | 138–163 | Observation | SP000098 | Tipe Penyelenggara Faskes Meninggal | _Tipe - Penyelenggara Faskes (DATA KEMATIAN)_ → `Observation.valueCodeableConcept.coding` (141, tanpa BQ)<br>_nama pasien 1_ → `Observation.subject.display` (157, tanpa BQ)<br>_nama pasien 2 (hanya lahir mati)_ → `Observation.focus.display` (159, tanpa BQ)<br>_Tgl. Meninggal_ → `Observation.effectiveDateTime` (160, tanpa BQ)<br>_Wkt. Lapor_ → `Observation.issued` (161, tanpa BQ)<br>_//PJ MPDN_ → `Observation.performer.display` (163, tanpa BQ) |
| 9 | 164–195 | Observation | 72150-6 | Delivery location | _Tempat Lahir_ → `Observation.valueCodeableConcept.coding` (167, tanpa BQ)<br>_nama pasien 1_ → `Observation.subject.display` (189, tanpa BQ)<br>_nama pasien 2 (hanya lahir mati)_ → `Observation.focus.display` (191, tanpa BQ)<br>_Tgl. Meninggal_ → `Observation.effectiveDateTime` (192, tanpa BQ)<br>_Wkt. Lapor_ → `Observation.issued` (193, tanpa BQ)<br>_//PJ MPDN_ → `Observation.performer.display` (195, tanpa BQ) |
| 10 | 196–209 | Observation | 57071-3 | Obstetric delivery method | _Cara Persalinan_ → `Observation.valueCodeableConcept.coding` (199, tanpa BQ)<br>_nama pasien 1_ → `Observation.subject.display` (203, tanpa BQ)<br>_nama pasien 2 (hanya lahir hidup)_ → `Observation.focus.display` (205, tanpa BQ)<br>_Tgl. Meninggal_ → `Observation.effectiveDateTime` (206, tanpa BQ)<br>_Wkt. Lapor_ → `Observation.issued` (207, tanpa BQ)<br>_//PJ MPDN_ → `Observation.performer.display` (209, tanpa BQ) |
| 11 | 210–225 | Observation | OC000013 | Penolong Persalinan | _Penolong_ → `Observation.valueCodeableConcept.coding` (213, tanpa BQ)<br>_nama pasien 1_ → `Observation.subject.display` (219, tanpa BQ)<br>_nama pasien 2 (hanya lahir hidup)_ → `Observation.focus.display` (221, tanpa BQ)<br>_Tgl. Meninggal_ → `Observation.effectiveDateTime` (222, tanpa BQ)<br>_Wkt. Lapor_ → `Observation.issued` (223, tanpa BQ)<br>_//PJ MPDN_ → `Observation.performer.display` (225, tanpa BQ) |
| 12 | 226–251 | Observation | SP000075 | Tipe Penyelenggara Faskes Lahir | _Tipe - Penyelenggara Faskes (IDENTITAS ANAK)_ → `Observation.valueCodeableConcept.coding` (229, tanpa BQ)<br>_nama pasien 1_ → `Observation.subject.display` (245, tanpa BQ)<br>_nama pasien 2 (hanya lahir mati)_ → `Observation.focus.display` (247, tanpa BQ)<br>_Tgl. Meninggal_ → `Observation.effectiveDateTime` (248, tanpa BQ)<br>_Wkt. Lapor_ → `Observation.issued` (249, tanpa BQ)<br>_//PJ MPDN_ → `Observation.performer.display` (251, tanpa BQ) |
| 13 | 252–263 | Observation | 57715-5 | Birth time | _Jam Lahir_ → `Observation.valueTime` (255, tanpa BQ)<br>_nama pasien 1_ → `Observation.subject.display` (257, tanpa BQ)<br>_nama pasien 2 (hanya lahir mati)_ → `Observation.focus.display` (259, tanpa BQ)<br>_Tgl. Meninggal_ → `Observation.effectiveDateTime` (260, tanpa BQ)<br>_Wkt. Lapor_ → `Observation.issued` (261, tanpa BQ)<br>_//PJ MPDN_ → `Observation.performer.display` (263, tanpa BQ) |
| 14 | 264–277 | Observation | 8339-4 | Birth weight Measured | _Berat Lahir_ → `Observation.valueQuantity.value` (267, tanpa BQ)<br>_nama pasien 1_ → `Observation.subject.display` (271, tanpa BQ)<br>_nama pasien 2 (hanya lahir mati)_ → `Observation.focus.display` (273, tanpa BQ)<br>_Tgl. Meninggal_ → `Observation.effectiveDateTime` (274, tanpa BQ)<br>_Wkt. Lapor_ → `Observation.issued` (275, tanpa BQ)<br>_//PJ MPDN_ → `Observation.performer.display` (277, tanpa BQ) |
| 15 | 278–290 | Observation | 11996-6 | [#] Pregnancies | _Hamil ke_ → `Observation.status` (278, tanpa BQ)<br>_nama pasien 1_ → `Observation.subject.display` (284, tanpa BQ)<br>_nama pasien 2 (hanya lahir hidup)_ → `Observation.focus.display` (286, tanpa BQ)<br>_Tgl. Meninggal_ → `Observation.effectiveDateTime` (287, tanpa BQ)<br>_Wkt. Lapor_ → `Observation.issued` (288, tanpa BQ)<br>_//PJ MPDN_ → `Observation.performer.display` (290, tanpa BQ) |
| 16 | 291–303 | Observation | 18185-9 | Gestational age | _Usia Kehamilan (Minggu)_ → `Observation.valueQuantity.value` (295, tanpa BQ)<br>_nama pasien 1_ → `Observation.subject.display` (297, tanpa BQ)<br>_nama pasien 2 (hanya lahir hidup)_ → `Observation.focus.display` (299, tanpa BQ)<br>_Tgl. Meninggal_ → `Observation.effectiveDateTime` (300, tanpa BQ)<br>_Wkt. Lapor_ → `Observation.issued` (301, tanpa BQ)<br>_//PJ MPDN_ → `Observation.performer.display` (303, tanpa BQ) |
| 17 | 304–318 | Observation | 57722-1 | Birth plurality of Pregnancy | _Kembar_ → `Observation.valueCodeableConcept.coding` (307, tanpa BQ)<br>_nama pasien 1_ → `Observation.subject.display` (312, tanpa BQ)<br>_nama pasien 2 (hanya lahir hidup)_ → `Observation.focus.display` (314, tanpa BQ)<br>_Tgl. Meninggal_ → `Observation.effectiveDateTime` (315, tanpa BQ)<br>_Wkt. Lapor_ → `Observation.issued` (316, tanpa BQ)<br>_//PJ MPDN_ → `Observation.performer.display` (318, tanpa BQ) |
| 18 | 319–332 | Observation | 30525-0 | Age | _Umur_ → `Observation.valueQuantity.value` (322, tanpa BQ)<br>_nama pasien 1_ → `Observation.subject.display` (326, tanpa BQ)<br>_nama pasien 2 (hanya lahir hidup)_ → `Observation.focus.display` (328, tanpa BQ)<br>_Tgl. Meninggal_ → `Observation.effectiveDateTime` (329, tanpa BQ)<br>_Wkt. Lapor_ → `Observation.issued` (330, tanpa BQ)<br>_//PJ MPDN_ → `Observation.performer.display` (332, tanpa BQ) |
| 19 | 333–417 | Composition | – | – | _Faskese Lahir_ → `Composition.contained.name` (335, tanpa BQ)<br>_Kabupaten/Kota Lahir_ → `Composition.contained.address.city` (338, tanpa BQ)<br>_Provinsi Lahir_ → `Composition.contained.address.extension:administrativeCode.extension:province` (340, tanpa BQ)<br>_Kabupaten/Kota Lahir_ → `Composition.contained.address.extension:administrativeCode.extension:city` (341, tanpa BQ)<br>_Faskes Meninggal_ → `Composition.contained.name` (344, tanpa BQ)<br>_Kabupaten/Kota Meninggal_ → `Composition.contained.address.city` (347, tanpa BQ)<br>_Provinsi Meninggal_ → `Composition.contained.address.extension:administrativeCode.extension:province` (349, tanpa BQ)<br>_Kabupaten/Kota Meninggal_ → `Composition.contained.address.extension:administrativeCode.extension:city` (350, tanpa BQ)<br>_nama pasien 1_ → `Composition.subject.reference` (353, tanpa BQ)<br>_//PJ MPDN_ → `Composition.author.display` (356, tanpa BQ)<br>_Wkt. Lapor_ → `Composition.date` (358, tanpa BQ)<br>_Pelapor_ → `Composition.status` (359, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 16 |
| Patient | 2 |
| Composition | 1 |
| **Total** | **19** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 45 | Observation | `Observation.code.coding` | 64710-7 | Was your pregnancy a live birth, stillbirth, miscarriage, abortion, or ectopic pregnancy [PhenX] | http://loinc.org |
| 2 | 46 | Observation | `Observation.valueCodeableConcept.coding` | 276507005 | Fetal death | http://snomed.info/sct |
| 3 | 47 | Observation | `Observation.valueCodeableConcept.coding` | 276506001 | Newborn death | http://snomed.info/sct |
| 4 | 58 | Observation | `Observation.code.coding` | 39016-1 | Age at death | http://loinc.org |
| 5 | 61 | Observation | `Observation.component.code.coding` | SP000716 | Umur Jam (saat meninggal) | http://terminology.kemkes.go.id/sp |
| 6 | 64 | Observation | `Observation.component.code.coding` | SP000717 | Umur Menit (saat meninggal) | http://terminology.kemkes.go.id/sp |
| 7 | 67 | Observation | `Observation.component.code.coding` | SP000718 | Umur Detik (saat meninggal) | http://terminology.kemkes.go.id/sp |
| 8 | 78 | Observation | `Observation.code.coding` | 81956-5 | Date and time of death [TimeStamp] | http://loinc.org |
| 9 | 89 | Observation | `Observation.code.coding` | 79378-6 | Cause of death | http://loinc.org |
| 10 | 90 | Observation | `Observation.component.code.coding` | TK000019 | Kode group | http://terminology.kemkes.go.id |
| 11 | 92 | Observation | `Observation.component.code.coding` | TK000020 | Kode subgroup | http://terminology.kemkes.go.id |
| 12 | 94 | Observation | `Observation.component.code.coding` | TK000021 | Kode detail | http://terminology.kemkes.go.id |
| 13 | 108 | Observation | `Observation.code.coding` | OC000028 | Jenis Tempat Meninggal | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 14 | 109 | Observation | `Observation.valueCodeableConcept.coding` | LT000008 | Dalam perjalanan dari rumah/masyarakat | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 15 | 110 | Observation | `Observation.valueCodeableConcept.coding` | LT000009 | Dalam perjalanan ke faskes lain | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 16 | 111 | Observation | `Observation.valueCodeableConcept.coding` | SP000099 | FASKES | http://terminology.kemkes.go.id/sp |
| 17 | 112 | Observation | `Observation.valueCodeableConcept.coding` | 102 | Pusat Kesehatan Masyarakat | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 18 | 113 | Observation | `Observation.valueCodeableConcept.coding` | OT000006 | Rumah Sakit Pemerintah | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 19 | 114 | Observation | `Observation.valueCodeableConcept.coding` | OT000007 | Rumah Sakit Swasta | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 20 | 115 | Observation | `Observation.valueCodeableConcept.coding` | LT000006 | Rumah Ibu | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 21 | 116 | Observation | `Observation.valueCodeableConcept.coding` | 104 | Rumah Sakit | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 22 | 117 | Observation | `Observation.valueCodeableConcept.coding` | OT000002 | Pustu | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 23 | 118 | Observation | `Observation.valueCodeableConcept.coding` | OT000010 | Klinik Medis Utama | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 24 | 119 | Observation | `Observation.valueCodeableConcept.coding` | OT000011 | Klinik Medis Pratama | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 25 | 120 | Observation | `Observation.valueCodeableConcept.coding` | 103 | Klinik | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 26 | 121 | Observation | `Observation.valueCodeableConcept.coding` | 101 | Tempat Praktik Mandiri Tenaga Kesehatan | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 27 | 122 | Observation | `Observation.valueCodeableConcept.coding` | OT000004 | Bidan Praktek Mandiri | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 28 | 123 | Observation | `Observation.valueCodeableConcept.coding` | OT000008 | Rumah Bersalin | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 29 | 124 | Observation | `Observation.valueCodeableConcept.coding` | 394573001 | Maternity clinic | http://snomed.info/sct |
| 30 | 125 | Observation | `Observation.valueCodeableConcept.coding` | OT000001 | Polindes | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 31 | 126 | Observation | `Observation.valueCodeableConcept.coding` | 264362003 | Home | http://snomed.info/sct |
| 32 | 127 | Observation | `Observation.valueCodeableConcept.coding` | LT000007 | Rumah Dukun | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 33 | 128 | Observation | `Observation.valueCodeableConcept.coding` | LT000010 | Lainnya | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 34 | 129 | Observation | `Observation.valueCodeableConcept.coding` | LT000011 | Belum Tahu | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 35 | 140 | Observation | `Observation.code.coding` | SP000098 | Tipe Penyelenggara Faskes Meninggal | http://terminology.kemkes.go.id/sp |
| 36 | 141 | Observation | `Observation.valueCodeableConcept.coding` | SP000076 | RSU - Pemprop | http://terminology.kemkes.go.id/sp |
| 37 | 142 | Observation | `Observation.valueCodeableConcept.coding` | SP000077 | PUSKESMAS - Pemkab | http://terminology.kemkes.go.id/sp |
| 38 | 143 | Observation | `Observation.valueCodeableConcept.coding` | SP000078 | RSU - Pemkot | http://terminology.kemkes.go.id/sp |
| 39 | 144 | Observation | `Observation.valueCodeableConcept.coding` | SP000079 | RSU - Pemkab | http://terminology.kemkes.go.id/sp |
| 40 | 145 | Observation | `Observation.valueCodeableConcept.coding` | SP000080 | RSIA - Perusahaan | http://terminology.kemkes.go.id/sp |
| 41 | 146 | Observation | `Observation.valueCodeableConcept.coding` | SP000081 | RSU - TNI AD | http://terminology.kemkes.go.id/sp |
| 42 | 147 | Observation | `Observation.valueCodeableConcept.coding` | SP000082 | RS Bersalin - Swasta/Lainnya | http://terminology.kemkes.go.id/sp |
| 43 | 148 | Observation | `Observation.valueCodeableConcept.coding` | SP000083 | RS - Organisasi Islam | http://terminology.kemkes.go.id/sp |
| 44 | 149 | Observation | `Observation.valueCodeableConcept.coding` | SP000084 | RS Bersalin - Pemkab | http://terminology.kemkes.go.id/sp |
| 45 | 150 | Observation | `Observation.valueCodeableConcept.coding` | SP000085 | RSU - Swasta/Lainnya | http://terminology.kemkes.go.id/sp |
| 46 | 151 | Observation | `Observation.valueCodeableConcept.coding` | SP000086 | RSU - KEMENKES | http://terminology.kemkes.go.id/sp |
| 47 | 152 | Observation | `Observation.valueCodeableConcept.coding` | SP000087 | RSU - Perusahaan | http://terminology.kemkes.go.id/sp |
| 48 | 153 | Observation | `Observation.valueCodeableConcept.coding` | SP000088 | RSU - Organisasi Islam | http://terminology.kemkes.go.id/sp |
| 49 | 154 | Observation | `Observation.valueCodeableConcept.coding` | SP000089 | RSU - Organisasi Sosial | http://terminology.kemkes.go.id/sp |
| 50 | 155 | Observation | `Observation.valueCodeableConcept.coding` | SP000090 | RS - Swasta/Lainnya | http://terminology.kemkes.go.id/sp |
| 51 | 166 | Observation | `Observation.code.coding` | 72150-6 | Delivery location | http://loinc.org |
| 52 | 167 | Observation | `Observation.valueCodeableConcept.coding` | LT000008 | Dalam perjalanan dari rumah/masyarakat | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 53 | 168 | Observation | `Observation.valueCodeableConcept.coding` | LT000009 | Dalam perjalanan ke faskes lain | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 54 | 169 | Observation | `Observation.valueCodeableConcept.coding` | SP000099 | FASKES | http://terminology.kemkes.go.id/sp |
| 55 | 170 | Observation | `Observation.valueCodeableConcept.coding` | 102 | Pusat Kesehatan Masyarakat | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 56 | 171 | Observation | `Observation.valueCodeableConcept.coding` | OT000006 | Rumah Sakit Pemerintah | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 57 | 172 | Observation | `Observation.valueCodeableConcept.coding` | OT000007 | Rumah Sakit Swasta | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 58 | 173 | Observation | `Observation.valueCodeableConcept.coding` | LT000006 | Rumah Ibu | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 59 | 174 | Observation | `Observation.valueCodeableConcept.coding` | 104 | Rumah Sakit | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 60 | 175 | Observation | `Observation.valueCodeableConcept.coding` | OT000002 | Pustu | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 61 | 176 | Observation | `Observation.valueCodeableConcept.coding` | OT000010 | Klinik Medis Utama | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 62 | 177 | Observation | `Observation.valueCodeableConcept.coding` | OT000011 | Klinik Medis Pratama | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 63 | 178 | Observation | `Observation.valueCodeableConcept.coding` | 103 | Klinik | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 64 | 179 | Observation | `Observation.valueCodeableConcept.coding` | 101 | Tempat Praktik Mandiri Tenaga Kesehatan | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 65 | 180 | Observation | `Observation.valueCodeableConcept.coding` | OT000004 | Bidan Praktek Mandiri | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 66 | 181 | Observation | `Observation.valueCodeableConcept.coding` | OT000008 | Rumah Bersalin | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 67 | 182 | Observation | `Observation.valueCodeableConcept.coding` | 394573001 | Maternity clinic | http://snomed.info/sct |
| 68 | 183 | Observation | `Observation.valueCodeableConcept.coding` | OT000001 | Polindes | http://terminology.kemkes.go.id/CodeSystem/organization-type |
| 69 | 184 | Observation | `Observation.valueCodeableConcept.coding` | 264362003 | Home (environment) | http://snomed.info/sct |
| 70 | 185 | Observation | `Observation.valueCodeableConcept.coding` | LT000007 | Rumah Dukun | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 71 | 186 | Observation | `Observation.valueCodeableConcept.coding` | LT000010 | Lainnya | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 72 | 187 | Observation | `Observation.valueCodeableConcept.coding` | LT000011 | Belum Tahu | http://terminology.kemkes.go.id/CodeSystem/location-type |
| 73 | 198 | Observation | `Observation.code.coding` | 57071-3 | Obstetric delivery method | http://loinc.org |
| 74 | 199 | Observation | `Observation.valueCodeableConcept.coding` | 289259007 | Vaginal delivery | http://snomed.info/sct |
| 75 | 200 | Observation | `Observation.valueCodeableConcept.coding` | 200144004 | Deliveries by cesarean | http://snomed.info/sct |
| 76 | 201 | Observation | `Observation.valueCodeableConcept.coding` | 48782003 | Delivery normal | http://snomed.info/sct |
| 77 | 212 | Observation | `Observation.code.coding` | OC000013 | Penolong Persalinan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 78 | 213 | Observation | `Observation.valueCodeableConcept.coding` | 303071001 | Person in the family | http://snomed.info/sct |
| 79 | 214 | Observation | `Observation.valueCodeableConcept.coding` | OV000012 | Dukun | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 80 | 215 | Observation | `Observation.valueCodeableConcept.coding` | 309453006 | Registered midwife | http://snomed.info/sct |
| 81 | 216 | Observation | `Observation.valueCodeableConcept.coding` | 309343006 | Physician Occupation | http://snomed.info/sct |
| 82 | 217 | Observation | `Observation.valueCodeableConcept.coding` | 11935004 | Obstetrician Occupation | http://snomed.info/sct |
| 83 | 228 | Observation | `Observation.code.coding` | SP000075 | Tipe Penyelenggara Faskes Lahir | http://terminology.kemkes.go.id/sp |
| 84 | 229 | Observation | `Observation.valueCodeableConcept.coding` | SP000076 | RSU - Pemprop | http://terminology.kemkes.go.id/sp |
| 85 | 230 | Observation | `Observation.valueCodeableConcept.coding` | SP000077 | PUSKESMAS - Pemkab | http://terminology.kemkes.go.id/sp |
| 86 | 231 | Observation | `Observation.valueCodeableConcept.coding` | SP000078 | RSU - Pemkot | http://terminology.kemkes.go.id/sp |
| 87 | 232 | Observation | `Observation.valueCodeableConcept.coding` | SP000079 | RSU - Pemkab | http://terminology.kemkes.go.id/sp |
| 88 | 233 | Observation | `Observation.valueCodeableConcept.coding` | SP000080 | RSIA - Perusahaan | http://terminology.kemkes.go.id/sp |
| 89 | 234 | Observation | `Observation.valueCodeableConcept.coding` | SP000081 | RSU - TNI AD | http://terminology.kemkes.go.id/sp |
| 90 | 235 | Observation | `Observation.valueCodeableConcept.coding` | SP000082 | RS Bersalin - Swasta/Lainnya | http://terminology.kemkes.go.id/sp |
| 91 | 236 | Observation | `Observation.valueCodeableConcept.coding` | SP000083 | RS - Organisasi Islam | http://terminology.kemkes.go.id/sp |
| 92 | 237 | Observation | `Observation.valueCodeableConcept.coding` | SP000084 | RS Bersalin - Pemkab | http://terminology.kemkes.go.id/sp |
| 93 | 238 | Observation | `Observation.valueCodeableConcept.coding` | SP000085 | RSU - Swasta/Lainnya | http://terminology.kemkes.go.id/sp |
| 94 | 239 | Observation | `Observation.valueCodeableConcept.coding` | SP000086 | RSU - KEMENKES | http://terminology.kemkes.go.id/sp |
| 95 | 240 | Observation | `Observation.valueCodeableConcept.coding` | SP000087 | RSU - Perusahaan | http://terminology.kemkes.go.id/sp |
| 96 | 241 | Observation | `Observation.valueCodeableConcept.coding` | SP000088 | RSU - Organisasi Islam | http://terminology.kemkes.go.id/sp |
| 97 | 242 | Observation | `Observation.valueCodeableConcept.coding` | SP000089 | RSU - Organisasi Sosial | http://terminology.kemkes.go.id/sp |
| 98 | 243 | Observation | `Observation.valueCodeableConcept.coding` | SP000090 | RS - Swasta/Lainnya | http://terminology.kemkes.go.id/sp |
| 99 | 254 | Observation | `Observation.code.coding` | 57715-5 | Birth time | http://loinc.org |
| 100 | 266 | Observation | `Observation.code.coding` | 8339-4 | Birth weight Measured | http://loinc.org |
| 101 | 280 | Observation | `Observation.code.coding` | 11996-6 | [#] Pregnancies | http://loinc.org |
| 102 | 281 | Observation | `Observation.code.coding` | ANC.B6.DE24 | Number of pregnancies (gravida) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 103 | 293 | Observation | `Observation.code.coding` | 18185-9 | Gestational age | http://loinc.org |
| 104 | 294 | Observation | `Observation.code.coding` | ANC.B6.DE17 | Gestational age | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 105 | 306 | Observation | `Observation.code.coding` | 57722-1 | Birth plurality of Pregnancy | http://loinc.org |
| 106 | 307 | Observation | `Observation.valueCodeableConcept.coding` | 237244005 | Single pregnancy | http://snomed.info/sct |
| 107 | 308 | Observation | `Observation.valueCodeableConcept.coding` | 65147003 | Twin pregnancy | http://snomed.info/sct |
| 108 | 309 | Observation | `Observation.valueCodeableConcept.coding` | 64254006 | Triplet pregnancy | http://snomed.info/sct |
| 109 | 310 | Observation | `Observation.valueCodeableConcept.coding` | OV000394 | Kehamilan Ganda Empat atau Lebih | http://snomed.info/sct |
| 110 | 321 | Observation | `Observation.code.coding` | 30525-0 | Age | http://loinc.org |
| 111 | 351 | Composition | `Composition.type.coding` | COM000002 | Formulir Informasi Kematian Perinatal Lahir Mati | http://terminology.kemkes.go.id/CodeSystem/composition-type |
| 112 | 352 | Composition | `Composition.type.coding` | COM000003 | Formulir Informasi Kematian Perinatal Lahir Hidup | http://terminology.kemkes.go.id/CodeSystem/composition-type |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://terminology.kemkes.go.id/sp | 37 |
| http://terminology.kemkes.go.id/CodeSystem/organization-type | 24 |
| http://snomed.info/sct | 17 |
| http://loinc.org | 12 |
| http://terminology.kemkes.go.id/CodeSystem/location-type | 12 |
| http://terminology.kemkes.go.id | 3 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 3 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 2 |
| http://terminology.kemkes.go.id/CodeSystem/composition-type | 2 |
| **Total** | **112** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
