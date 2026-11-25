# Output Form: Master Data (Prerequisite)

Sumber: `mapping/phdt-data-dictionary-master-data-prerequisite.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-master-data-prerequisite.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 0 |
| Code (`jumlah code` = 1) | 84 |
| Code unik (code + CodeSystem) | 84 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 84 |
| Variabel BQ (unik) | 0 |
| Variabel raw (variabel dictionary; belum ada file mentah) | 15 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|

### Payload per resource

| Resource | Jumlah |
|---|---|
| **Total** | **0** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 2 | PractitionerRole | `PractitionerRole.code.coding` | SP000048 | Pengelola Sistem Informasi dan Basis Data (Database) | http://terminology.kemkes.go.id/sp |
| 2 | 3 | PractitionerRole | `PractitionerRole.code.coding` | SP000049 | Cleaning Service | http://terminology.kemkes.go.id/sp |
| 3 | 4 | PractitionerRole | `PractitionerRole.code.coding` | SP000434 | Vaksinator | http://terminology.kemkes.go.id/sp |
| 4 | 5 | PractitionerRole | `PractitionerRole.code.coding` | SP000677 | PJ SITB | http://terminology.kemkes.go.id/sp |
| 5 | 6 | PractitionerRole | `PractitionerRole.code.coding` | SP000714 | PJ KIA | http://terminology.kemkes.go.id/sp |
| 6 | 7 | PractitionerRole | `PractitionerRole.specialty.coding` | SP001124 | Kader Madya | http://terminology.kemkes.go.id/sp |
| 7 | 8 | PractitionerRole | `PractitionerRole.specialty.coding` | SP001125 | Kader Purwa | http://terminology.kemkes.go.id/sp |
| 8 | 9 | PractitionerRole | `PractitionerRole.specialty.coding` | SP001126 | Kader Utama | http://terminology.kemkes.go.id/sp |
| 9 | 10 | Organization | `Organization.type.coding` | SP000385 | Taman Kanak-Kanak | http://terminology.kemkes.go.id/CodeSystem/organization-type/sp |
| 10 | 11 | Organization | `Organization.type.coding` | SP000386 | Kelompok Bermain | http://terminology.kemkes.go.id/CodeSystem/organization-type/sp |
| 11 | 12 | Organization | `Organization.type.coding` | SP000387 | Taman Penitipan Anak | http://terminology.kemkes.go.id/CodeSystem/organization-type/sp |
| 12 | 13 | Organization | `Organization.type.coding` | SP000388 | Satuan PAUD Sejenis | http://terminology.kemkes.go.id/CodeSystem/organization-type/sp |
| 13 | 14 | Organization | `Organization.type.coding` | SP000457 | Pendidikan Anak Usia Dini Al-Quran | http://terminology.kemkes.go.id/CodeSystem/organization-type/sp |
| 14 | 15 | Organization | `Organization.type.coding` | SP000458 | Raudhatul Athfal | http://terminology.kemkes.go.id/CodeSystem/organization-type/sp |
| 15 | 16 | Organization | `Organization.type.coding` | SP000753 | Kelurahan | http://terminology.kemkes.go.id/sp |
| 16 | 17 | Observation | `Observation.code.coding` | SP000050 | Riwayat Onset Persalinan | http://terminology.kemkes.go.id/sp |
| 17 | 18 | Observation | `Observation.code.coding` | SP000051 | Riwayat Berat Badan Lahir Anak | http://terminology.kemkes.go.id/sp |
| 18 | 19 | Observation | `Observation.code.coding` | SP000052 | Riwayat Penolong Persalinan | http://terminology.kemkes.go.id/sp |
| 19 | 20 | Observation | `Observation.code.coding` | SP000053 | Riwayat Perilaku Berisiko 1 Bulan Sebelum Hamil | http://terminology.kemkes.go.id/sp |
| 20 | 21 | Observation | `Observation.valueCodeableConcept.coding` | SP000054 | Pola makan beresiko | http://terminology.kemkes.go.id/sp |
| 21 | 22 | Observation | `Observation.valueCodeableConcept.coding` | SP000055 | Obat teratogenik | http://terminology.kemkes.go.id/sp |
| 22 | 23 | Observation | `Observation.valueCodeableConcept.coding` | SP000056 | Kosmetik berbahaya | http://terminology.kemkes.go.id/sp |
| 23 | 24 | Condition | `Condition.code.coding` | SP000203 | Berkeringat malam hari tanpa kegiatan | http://terminology.kemkes.go.id/sp |
| 24 | 25 | Observation | `Observation.category.coding` | SP000204 | Pernah berobat TBC tapi tidak tuntas | http://terminology.kemkes.go.id/sp |
| 25 | 26 | Observation | `Observation.category.coding` | SP000205 | Memenuhi syarat rujukan pemeriksaan Terduga | http://terminology.kemkes.go.id/sp |
| 26 | 27 | Observation | `Observation.code.coding` | SP000231 | Berkebutuhan Khusus | http://terminology.kemkes.go.id/sp |
| 27 | 28 | Observation | `Observation.valueCodeableConcept.coding` | SP000246 | Pekerjaan Wali | http://terminology.kemkes.go.id/sp |
| 28 | 29 | Observation | `Observation.code.coding` | SP000369 | Kontak Dengan Penderita TBC | http://terminology.kemkes.go.id/sp |
| 29 | 30 | Observation | `Observation.code.coding` | SP000381 | Tatalaksana Komplikasi Infeksi | http://terminology.kemkes.go.id/sp |
| 30 | 31 | Observation | `Observation.code.coding` | SP000382 | Tatalaksana Komplikasi Mastitis | http://terminology.kemkes.go.id/sp |
| 31 | 32 | Condition | `Condition.code.coding` | SP000421 | Riwayat Penyakit Jiwa | http://terminology.kemkes.go.id/sp |
| 32 | 33 | Observation | `Observation.valueCodeableConcept.coding` | SP000468 | Tidak ada penolong persalinan | http://terminology.kemkes.go.id/sp |
| 33 | 34 | Observation | `Observation.code.coding` | SP000506 | Ibu diresepkan tenofovir 300 mg setiap hari untuk pencegahan penularan vertikal Hepatitis B | http://terminology.kemkes.go.id/sp |
| 34 | 35 | Observation | `Observation.code.coding` | SP000641 | Konsumsi MMS setiap hari | http://terminology.kemkes.go.id/sp |
| 35 | 36 | Observation | `Observation.code.coding` | SP000643 | Alasan tidak mengonsumsi MMS | http://terminology.kemkes.go.id/sp |
| 36 | 37 | Observation | `Observation.code.coding` | SP000646 | Mendapatkan vitamin A | http://terminology.kemkes.go.id/sp |
| 37 | 38 | Observation | `Observation.code.coding` | SP000662 | Kontak erat dengan Pasien TBC | http://terminology.kemkes.go.id/sp |
| 38 | 39 | Observation | `Observation.code.coding` | SP000663 | Skor skrining TBC | http://terminology.kemkes.go.id/sp |
| 39 | 40 | Observation | `Observation.code.coding` | SP000731 | MPASI Protein Hewani | http://terminology.kemkes.go.id/sp |
| 40 | 41 | Observation | `Observation.code.coding` | SP000733 | Isi piringku Ibu menyusui | http://terminology.kemkes.go.id/sp |
| 41 | 42 | Observation | `Observation.code.coding` | SP000734 | Tanda bahaya nifas | http://terminology.kemkes.go.id/sp |
| 42 | 43 | Observation | `Observation.code.coding` | SP000735 | Isi piringku Anak Usia Sekolah dan Remaja | http://terminology.kemkes.go.id/sp |
| 43 | 44 | Observation | `Observation.code.coding` | SP000736 | Isi piringku Usia Produktif | http://terminology.kemkes.go.id/sp |
| 44 | 45 | Condition | `Condition.code.coding` | SP000737 | Kunjungan pemantauan luaran neonatal | http://terminology.kemkes.go.id/sp |
| 45 | 46 | Observation | `Observation.code.coding` | SP000756 | Apakah pemeriksaan kehamilan sebelumnya dilakukan di kota ini? | http://terminology.kemkes.go.id/sp |
| 46 | 47 | Observation | `Observation.code.coding` | SP000762 | Tanda bahaya bayi | http://terminology.kemkes.go.id/sp |
| 47 | 48 | Observation | `Observation.code.coding` | SP000763 | Isi piringku Ibu hamil | http://terminology.kemkes.go.id/sp |
| 48 | 49 | Observation | `Observation.code.coding` | SP000765 | PMT Ibu Hamil | http://terminology.kemkes.go.id/sp |
| 49 | 50 | Observation | `Observation.code.coding` | SP000766 | Demam lebih dari 2 hari | http://terminology.kemkes.go.id/sp |
| 50 | 51 | Observation | `Observation.code.coding` | SP000767 | Jumlah anggota keluarga lansia | http://terminology.kemkes.go.id/sp |
| 51 | 52 | Observation | `Observation.code.coding` | SP000768 | Jumlah anggota keluarga usia dewasa | http://terminology.kemkes.go.id/sp |
| 52 | 53 | Observation | `Observation.code.coding` | SP000769 | Jumlah anggota keluarga usia sekolah dan remaja | http://terminology.kemkes.go.id/sp |
| 53 | 54 | Observation | `Observation.code.coding` | SP000770 | Jumlah anggota keluarga balita | http://terminology.kemkes.go.id/sp |
| 54 | 55 | Observation | `Observation.code.coding` | SP000771 | Jumlah anggota keluarga bayi | http://terminology.kemkes.go.id/sp |
| 55 | 56 | Observation | `Observation.code.coding` | SP000772 | Jumlah anggota keluarga ibu bersalin dan nifas | http://terminology.kemkes.go.id/sp |
| 56 | 57 | Observation | `Observation.code.coding` | SP000773 | Jumlah anggota keluarga ibu hamil | http://terminology.kemkes.go.id/sp |
| 57 | 58 | Observation | `Observation.code.coding` | SP000774 | Jenis Jamban Saniter | http://terminology.kemkes.go.id/sp |
| 58 | 59 | Observation | `Observation.code.coding` | SP000794 | Skrining Kekerasan Pada Perempuan | http://terminology.kemkes.go.id/sp |
| 59 | 60 | Observation | `Observation.code.coding` | SP000800 | Deeplex Myc-TB codon change | http://terminology.kemkes.go.id/sp |
| 60 | 61 | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` | SP000861 | Sudah Sembuh | http://terminology.kemkes.go.id/sp |
| 61 | 62 | Observation | `Observation.code.coding` | SP000891 | Isi piringku lansia | http://terminology.kemkes.go.id/sp |
| 62 | 63 |  | `` | SP000895 | 1 kali sehari | http://terminology.kemkes.go.id/sp |
| 63 | 64 |  | `` | SP000896 | 2 kali sehari | http://terminology.kemkes.go.id/sp |
| 64 | 65 |  | `` | SP000897 | 3 kali sehari | http://terminology.kemkes.go.id/sp |
| 65 | 66 |  | `` | SP000898 | > 3 kali sehari | http://terminology.kemkes.go.id/sp |
| 66 | 67 |  | `` | SP000910 | Ibu mengonsumsi MMS setiap hari | http://terminology.kemkes.go.id/sp |
| 67 | 68 | Observation | `Observation.valueCodeableConcept.coding` | SP000960 | 1-6 Bulan yang lalu | http://terminology.kemkes.go.id/sp |
| 68 | 69 | Observation | `Observation.valueCodeableConcept.coding` | SP000961 | 1-3 tahun yang lalu | http://terminology.kemkes.go.id/sp |
| 69 | 70 | Observation | `Observation.valueCodeableConcept.coding` | SP000962 | 4-5 Tahun yang lalu | http://terminology.kemkes.go.id/sp |
| 70 | 71 | Observation | `Observation.valueCodeableConcept.coding` | SP000963 | Lebih dari  5 tahun yang lalu | http://terminology.kemkes.go.id/sp |
| 71 | 72 | Observation | `Observation.code.coding` | SP000964 | Orang yang mengawasi minum obat | http://terminology.kemkes.go.id/sp |
| 72 | 73 | Observation | `Observation.code.coding` | SP000965 | Memiliki obat TBC | http://terminology.kemkes.go.id/sp |
| 73 | 74 | Observation | `Observation.valueCodeableConcept.coding` | SP000966 | 1-3 Bulan Terakhir | http://terminology.kemkes.go.id/sp |
| 74 | 75 | Observation | `Observation.valueCodeableConcept.coding` | SP000967 | 4-6 Bulan Terakhir | http://terminology.kemkes.go.id/sp |
| 75 | 76 | Observation | `Observation.valueCodeableConcept.coding` | SP000968 | 7 - 12 Bulan Terakhir | http://terminology.kemkes.go.id/sp |
| 76 | 77 | Observation | `Observation.valueCodeableConcept.coding` | SP000969 | >12 Bulan | http://terminology.kemkes.go.id/sp |
| 77 | 78 | Observation | `Observation.code.coding` | SP000970 | Waktu dilakukannya skrining kesehatan jiwa | http://terminology.kemkes.go.id/sp |
| 78 | 79 | Observation | `Observation.code.coding` | SP001106 | Jumlah Gestasional Sac | http://terminology.kemkes.go.id/sp |
| 79 | 80 | Observation | `Observation.code.coding` | SP001128 | Tanggal lahir diketahui | http://terminology.kemkes.go.id/sp |
| 80 | 81 | Observation | `Observation.code.coding` | SP001129 | Perkiraan umur diketahui | http://terminology.kemkes.go.id/sp |
| 81 | 82 | Observation | `Observation.component.code.coding` | SP001130 | Belum melakukan imunisasi Hb0 dan BCG | http://terminology.kemkes.go.id/sp |
| 82 | 83 | Procedure | `Procedure.code.coding` | SP001131 | Skrining Lansia Sederhana | http://terminology.kemkes.go.id/sp |
| 83 | 84 | Procedure | `Procedure.code.coding` | SP001132 | Skrining AKS | http://terminology.kemkes.go.id/sp |
| 84 | 85 | Observation | `Observation.code.coding` | SP001134 | Menggunakan Buku KIA | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://terminology.kemkes.go.id/sp | 78 |
| http://terminology.kemkes.go.id/CodeSystem/organization-type/sp | 6 |
| **Total** | **84** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 2 | – | Pengelola Sistem Informasi dan Basis Data (Database) | PractitionerRole | `PractitionerRole.code.coding` |
| 3 | – | Cleaning Service | PractitionerRole | `PractitionerRole.code.coding` |
| 4 | – | Vaksinator | PractitionerRole | `PractitionerRole.code.coding` |
| 5 | – | PJ SITB | PractitionerRole | `PractitionerRole.code.coding` |
| 6 | – | PJ KIA | PractitionerRole | `PractitionerRole.code.coding` |
| 7 | – | Kader Madya | PractitionerRole | `PractitionerRole.specialty.coding` |
| 8 | – | Kader Purwa | PractitionerRole | `PractitionerRole.specialty.coding` |
| 9 | – | Kader Utama | PractitionerRole | `PractitionerRole.specialty.coding` |
| 10 | – | Taman Kanak-Kanak | Organization | `Organization.type.coding` |
| 11 | – | Kelompok Bermain | Organization | `Organization.type.coding` |
| 12 | – | Taman Penitipan Anak | Organization | `Organization.type.coding` |
| 13 | – | Satuan PAUD Sejenis | Organization | `Organization.type.coding` |
| 14 | – | Pendidikan Anak Usia Dini Al-Quran | Organization | `Organization.type.coding` |
| 15 | – | Raudhatul Athfal | Organization | `Organization.type.coding` |
| 16 | – | Kelurahan | Organization | `Organization.type.coding` |
| 17 | – | Riwayat Onset Persalinan | Observation | `Observation.code.coding` |
| 18 | – | Riwayat Berat Badan Lahir Anak | Observation | `Observation.code.coding` |
| 19 | – | Riwayat Penolong Persalinan | Observation | `Observation.code.coding` |
| 20 | – | Riwayat Perilaku Berisiko 1 Bulan Sebelum Hamil | Observation | `Observation.code.coding` |
| 21 | – | Pola makan beresiko | Observation | `Observation.valueCodeableConcept.coding` |
| 22 | – | Obat teratogenik | Observation | `Observation.valueCodeableConcept.coding` |
| 23 | – | Kosmetik berbahaya | Observation | `Observation.valueCodeableConcept.coding` |
| 24 | – | Berkeringat malam hari tanpa kegiatan | Condition | `Condition.code.coding` |
| 25 | – | Pernah berobat TBC tapi tidak tuntas | Observation | `Observation.category.coding` |
| 26 | – | Memenuhi syarat rujukan pemeriksaan Terduga | Observation | `Observation.category.coding` |
| 27 | – | Berkebutuhan Khusus | Observation | `Observation.code.coding` |
| 28 | – | Pekerjaan Wali | Observation | `Observation.valueCodeableConcept.coding` |
| 29 | – | Kontak Dengan Penderita TBC | Observation | `Observation.code.coding` |
| 30 | – | Tatalaksana Komplikasi Infeksi | Observation | `Observation.code.coding` |
| 31 | – | Tatalaksana Komplikasi Mastitis | Observation | `Observation.code.coding` |
| 32 | – | Riwayat Penyakit Jiwa | Condition | `Condition.code.coding` |
| 33 | – | Tidak ada penolong persalinan | Observation | `Observation.valueCodeableConcept.coding` |
| 34 | – | Ibu diresepkan tenofovir 300 mg setiap hari untuk pencegahan penularan vertikal Hepatitis B | Observation | `Observation.code.coding` |
| 35 | – | Konsumsi MMS setiap hari | Observation | `Observation.code.coding` |
| 36 | – | Alasan tidak mengonsumsi MMS | Observation | `Observation.code.coding` |
| 37 | – | Mendapatkan vitamin A | Observation | `Observation.code.coding` |
| 38 | – | Kontak erat dengan Pasien TBC | Observation | `Observation.code.coding` |
| 39 | – | Skor skrining TBC | Observation | `Observation.code.coding` |
| 40 | – | MPASI Protein Hewani | Observation | `Observation.code.coding` |
| 41 | – | Isi piringku Ibu menyusui | Observation | `Observation.code.coding` |
| 42 | – | Tanda bahaya nifas | Observation | `Observation.code.coding` |
| 43 | – | Isi piringku Anak Usia Sekolah dan Remaja | Observation | `Observation.code.coding` |
| 44 | – | Isi piringku Usia Produktif | Observation | `Observation.code.coding` |
| 45 | – | Kunjungan pemantauan luaran neonatal | Condition | `Condition.code.coding` |
| 46 | – | Apakah pemeriksaan kehamilan sebelumnya dilakukan di kota ini? | Observation | `Observation.code.coding` |
| 47 | – | Tanda bahaya bayi | Observation | `Observation.code.coding` |
| 48 | – | Isi piringku Ibu hamil | Observation | `Observation.code.coding` |
| 49 | – | PMT Ibu Hamil | Observation | `Observation.code.coding` |
| 50 | – | Demam lebih dari 2 hari | Observation | `Observation.code.coding` |
| 51 | – | Jumlah anggota keluarga lansia | Observation | `Observation.code.coding` |
| 52 | – | Jumlah anggota keluarga usia dewasa | Observation | `Observation.code.coding` |
| 53 | – | Jumlah anggota keluarga usia sekolah dan remaja | Observation | `Observation.code.coding` |
| 54 | – | Jumlah anggota keluarga balita | Observation | `Observation.code.coding` |
| 55 | – | Jumlah anggota keluarga bayi | Observation | `Observation.code.coding` |
| 56 | – | Jumlah anggota keluarga ibu bersalin dan nifas | Observation | `Observation.code.coding` |
| 57 | – | Jumlah anggota keluarga ibu hamil | Observation | `Observation.code.coding` |
| 58 | – | Jenis Jamban Saniter | Observation | `Observation.code.coding` |
| 59 | – | Skrining Kekerasan Pada Perempuan | Observation | `Observation.code.coding` |
| 60 | – | Deeplex Myc-TB codon change | Observation | `Observation.code.coding` |
| 61 | – | Sudah Sembuh | QuestionnaireResponse | `QuestionnaireResponse.item.item.answer.valueCoding` |
| 62 | – | Isi piringku lansia | Observation | `Observation.code.coding` |
| 63 | – | 1 kali sehari | – | `` |
| 64 | – | 2 kali sehari | – | `` |
| 65 | – | 3 kali sehari | – | `` |
| 66 | – | > 3 kali sehari | – | `` |
| 67 | – | Ibu mengonsumsi MMS setiap hari | – | `` |
| 68 | – | 1-6 Bulan yang lalu | Observation | `Observation.valueCodeableConcept.coding` |
| 69 | – | 1-3 tahun yang lalu | Observation | `Observation.valueCodeableConcept.coding` |
| 70 | – | 4-5 Tahun yang lalu | Observation | `Observation.valueCodeableConcept.coding` |
| 71 | – | Lebih dari  5 tahun yang lalu | Observation | `Observation.valueCodeableConcept.coding` |
| 72 | – | Orang yang mengawasi minum obat | Observation | `Observation.code.coding` |
| 73 | – | Memiliki obat TBC | Observation | `Observation.code.coding` |
| 74 | – | 1-3 Bulan Terakhir | Observation | `Observation.valueCodeableConcept.coding` |
| 75 | – | 4-6 Bulan Terakhir | Observation | `Observation.valueCodeableConcept.coding` |
| 76 | – | 7 - 12 Bulan Terakhir | Observation | `Observation.valueCodeableConcept.coding` |
| 77 | – | >12 Bulan | Observation | `Observation.valueCodeableConcept.coding` |
| 78 | – | Waktu dilakukannya skrining kesehatan jiwa | Observation | `Observation.code.coding` |
| 79 | – | Jumlah Gestasional Sac | Observation | `Observation.code.coding` |
| 80 | – | Tanggal lahir diketahui | Observation | `Observation.code.coding` |
| 81 | – | Perkiraan umur diketahui | Observation | `Observation.code.coding` |
| 82 | – | Belum melakukan imunisasi Hb0 dan BCG | Observation | `Observation.component.code.coding` |
| 83 | – | Skrining Lansia Sederhana | Procedure | `Procedure.code.coding` |
| 84 | – | Skrining AKS | Procedure | `Procedure.code.coding` |
| 85 | – | Menggunakan Buku KIA | Observation | `Observation.code.coding` |
