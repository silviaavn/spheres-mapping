# Revisi Data Dictionary — Form Kobo & PHDT

Terakhir diperbarui: 2026-11-24
File dictionary terbaru: Maternal Outcome → `mapping/kobo-data-dictionary-maternal-outcome.csv`; Raffle → `mapping/kobo-data-dictionary-raffle.csv`; SiGizi ANC → `mapping/phdt-data-dictionary-sigizi-anc.csv`; SITB TB 06 / TB 03 SO / TB 03 RO / TB 04 / TB 16K → `mapping/phdt-data-dictionary-sitb-<form>.csv`; MPDN Kematian Bayi / Kematian Ibu → `mapping/phdt-data-dictionary-mpdn-kematian-<bayi|ibu>.csv` (nomor baris di bawah mengikuti CSV asli; di `mapping/` nomor barisnya sudah berbeda karena ada baris tambahan/dihapus. Untuk nomor baris terbaru lihat `output/raffle.md`)

> Maternal Outcome: nomor baris di bawah mengikuti Kobo_3. Di file `mapping/`, baris setelah 11 bergeser +1 karena ada baris baru `Practitioner.identifier.value`.

Daftar hal yang perlu diperbaiki di data dictionary. Ubah status jadi `done` kalau sudah dibetulkan.

## Form: Maternal Outcome

### Koreksi kolom `jumlah instance`

| # | Baris CSV | Sebelumnya | Seharusnya | Status |
|---|---|---|---|---|
| 1 | 12 (baris kosong) | 1 | kosong (pindahkan ke baris Patient) | done |
| 2 | 13 (Patient.name.text) | kosong | 1 | done |
| 3 | Organization / Location | kosong | tetap kosong (master data) | ok |
| 4 | 71 (Condition.category) | 1 | pindah ke baris 70 (baris pertama Condition) supaya konsisten dengan aturan | done (mapping/) |

Hasil Kobo_3: jumlah instance = 12, jumlah code = 14 (sesuai).

### Temuan mapping

| # | Temuan | Status |
|---|---|---|
| 1 | Keadaan Ibu: Value Name bergeser 1 baris (sehat→Illness, sakit→Dead). Seharusnya sehat→102514002, sakit→39104002, meninggal→419099009 | done (Kobo_3) |
| 2 | PractitionerRole: display SP000396 / SP000397 tertukar dengan value name | done (Kobo_3): data_entry_staff→SP000396, field_or_call_center_staff→SP000397 |
| 3 | Typo `ofiicial` di Practitioner.identifier | done (Kobo_3) |
| 4 | Baris 45: path `Organization.address.extension.url` di blok Location | done (mapping/): jadi `Location.address.extension.url`, sama seperti baris 36, 39, 42 |
| 5 | URL organization-type ada spasi di akhir | done (Kobo_3) |
| 6 | Practitioner.identifier (baris 10–11) tidak konsisten. Input-nya NIK, tapi baris 10 pakai system `nakes-his-number`, sedangkan baris 11 `identifier.use` pakai system `nik`. Belum ada baris `.system` / `.value` seperti di Patient (baris 14–16) | done (mapping/): disamakan dengan Patient jadi 3 baris `.use` official, `.system` nik, `.value`. System `nakes-his-number` dihapus karena yang diinput NIK |
| 7 | Baris 13: Subcategory tertulis "Identitas Bayi", padahal isinya Nama Ibu / NIK Ibu | done (mapping/): jadi "Identitas Ibu" |

### Tally variabel BQ vs dictionary

Kolom **Nama Column BQ** sudah ditambahkan di `mapping/` (sebelum "Nama Column Raw"). Hasil: **12 variabel BQ = 12 variabel Kobo** ✅

| Variabel BQ | Variabel Kobo | Path FHIR | Cocok? |
|---|---|---|---|
| data_entry_clerk_type | Siapa yang melakukan entry data? | PractitionerRole.code | ✅ |
| data_entry_clerk_staff_id | Nama yang melakukan entry data | Practitioner.name.text + Encounter.participant ADM display | ✅ (isinya nama, lihat #8) |
| nik_yang_melakukan_entry_data | NIK yang melakukan entry data | Practitioner.identifier (nik) | ✅ |
| nama_ibu | Nama Ibu | Patient.name.text | ✅ |
| nik_ibu | NIK Ibu | Patient.identifier (nik) | ✅ |
| puskesmas_name | Puskesmas | Encounter.serviceProvider.reference (lookup master data Organization) | ✅ |
| tanggal_pencatatan | Tanggal Pencatatan | Encounter.period.start | ✅ |
| outcome_001 | Keadaan Ibu | Observation SP000389 | ✅ |
| delivery_date | Tanggal Persalinan | Observation 93857-1 | ✅ |
| tanggal_meninggal | Tanggal Meninggal | Observation 81956-5 | ✅ |
| tempat_meninggal | Tempat Meninggal | Observation LT000005 | ✅ |
| sebab_meninggal | Penyebab Meninggal | Observation 79378-6 | ✅ |

| # | Temuan | Status |
|---|---|---|
| 11 | Puskesmas dipilih dari list, jadi Organization & Location cukup lookup ke master data | done (mapping/): blok Organization dan Location dihapus. `Encounter.location.reference` diberi keterangan lookup master data Location |
| 12 | Observation Tanggal Meninggal (81956-5), Tempat Meninggal (LT000005), Penyebab Meninggal (79378-6) tidak punya `Observation.encounter.reference`, padahal 2 Observation lain punya. Ketiganya malah pakai `focus.reference` = Patient, yang sama dengan `subject` | done (mapping/): `focus.reference` diganti jadi `encounter.reference`, `focus.display` dihapus |
| 13 | PractitionerRole tidak direferensi oleh resource mana pun dan tidak punya `PractitionerRole.practitioner.reference`, jadi tidak tersambung ke Practitioner data entry | done (mapping/): tambah `PractitionerRole.practitioner.reference` → Practitioner data entry (Nama yang melakukan entry data) |
| 14 | EpisodeOfCare ANC & PNC hanya berisi `type` + `status` finished. Tidak ada `patient.reference` dan tidak ada keterangan cara mencari episode yang mau ditutup | done (mapping/): Definisi Operasional ANC & PNC diisi cara mencari episode, dan `patient.reference` ditambahkan di keduanya |
| 15 | Keadaan Ibu pakai category `vital-signs`, sedangkan Observation lain `survey` | done (mapping/): category diganti jadi `survey` |
| 10 | `puskesmas_name` dipindah dari `Organization.name` ke `Encounter.serviceProvider.reference` (keterangan: lookup master data Organization). Definisi lama "spheres? puskesmas?" diganti. Blok Organization masih ada di dictionary | done (mapping/) |
| 9 | Nama data entry juga masuk ke `Encounter.participant` (type ADM admitter). Kolom Variables di baris `Encounter.participant.individual.display` diisi "Nama yang melakukan entry data" | done (mapping/) |
| 8 | `data_entry_clerk_staff_id` kelihatannya ID, bukan nama | done: dikonfirmasi isinya **nama**. Mapping ke `Practitioner.name.text` sudah benar, dan kolom yang sama juga dipakai untuk `Encounter.participant.individual.display` (ADM) |

## Form: Raffle

Sumber: Kobo - Data Dictionary - Kobo Raffle (nomor baris = baris CSV asli, header 7 baris). Versi revisi: `mapping/kobo-data-dictionary-raffle.csv` (kolom BQ terisi, kolom `jumlah code` = 6 dan `jumlah instance` = 7 ditambahkan).

### Tally variabel BQ vs dictionary

**12 variabel BQ = 12 variabel Kobo** ✅ (setelah revisi R1, R2, R12).

| Variabel BQ | Variabel Kobo (baris) | Path FHIR | Cocok? |
|---|---|---|---|
| nama_data_entry | Nama Data Entry (baris baru) | Encounter.participant.individual.display (type ADM) | ✅ |
| puskesmas | Puskesmas Pengampu | Encounter.serviceProvider.reference (lookup master data Organization) | ✅ |
| kecamatan | Kecamatan (57) | Location.address district | ✅ |
| kelurahan | Kelurahan (60) | Location.address village | ✅ |
| lokasi_faskes | Lokasi/Fasilitas Kesehatan (43) | Location (dibuat dari form) | ✅ |
| nama_bidan_desa | Nama Bidan Desa (69) | Practitioner.name.text | ✅ |
| nik_ibu | NIK Ibu (10) | Patient.identifier (nik) | ✅ |
| nama_ibu | Nama Ibu (8) | Patient.name.text | ✅ |
| nomor_telepon | Nomor Telepon (18) | Patient.telecom | ✅ |
| tanggal_kunjungan | Tanggal Kunjungan Pelayanan (92) | Encounter.period.start | ✅ |
| keterangan | Keterangan (106) | Condition.note | ✅ |
| input_data 🆕 | Input Data (122) | Observation 385438008 | ✅ (kolom BQ baru, lihat Catatan pipeline) |

Provinsi dan Kabupaten/Kota (31, 34, 51, 54) tidak perlu kolom BQ karena di-hardcode sesuai deployment.

### Temuan

| # | Temuan | Status |
|---|---|---|
| R1 | `nama_data_entry` (BQ) tidak ada di dictionary, sedangkan "Input Data" (Observation 385438008, nilai Sigizi / E-pus PKD / E-pus) tidak ada di BQ. Kemungkinan keduanya pasangan yang sama, yaitu sistem tempat data di-input. Kalau ternyata `nama_data_entry` adalah nama orang yang meng-input, berarti perlu payload Practitioner/PractitionerRole tambahan dan Input Data belum punya kolom BQ | done (mapping/): `nama_data_entry` masuk ke `Encounter.participant` type ADM admitter, `individual.display`. Ditambah 2 baris baru setelah baris 91 |
| R2 | Kecamatan dan Kelurahan muncul 2x (blok Organization dan blok Location), tapi di BQ hanya ada 1 kolom masing-masing. Perlu ditentukan kolom BQ dipakai untuk resource yang mana, atau keduanya diisi dari kolom yang sama | done (mapping/): Kecamatan & Kelurahan hanya untuk Location. Variabel di blok Organization (37, 40) dikosongkan. Location sekarang dibuat dari form dan dihitung sebagai payload |
| R3 | **SP000776 dipakai dengan 2 arti berbeda**: Condition.code = "Presensi Posyandu" (101) dan value Input Data = "Sigizi" (123). Satu code hanya boleh punya 1 arti, jadi salah satunya harus diganti | done (mapping/): Condition.code jadi SP001135 Presensi Posyandu. SP000776 tetap untuk Sigizi |
| R4 | Variabel "Puskesmas Pengampu" ditaruh di baris Organization.type (26). Seharusnya di baris Organization.name (27), karena yang diisi adalah nama puskesmas | done (mapping/) |
| R5 | Baris 59: path `Organization.address.extension.url` di blok Location. Seharusnya `Location.address.extension.url` (sama dengan temuan Maternal Outcome #4) | done (mapping/) |
| R6 | Baris 18–20 Patient.telecom: "phone" ditaruh di kolom CodeSystem baris `Patient.telecom`. Seharusnya ada baris `Patient.telecom.system` = phone. Baris 19–20 kolom Resource kosong | done (mapping/): baris 18 jadi `Patient.telecom.system` = phone; Resource baris 19–20 diisi Patient |
| R7 | Baris 85: Encounter.class `FLD` tapi display "ambulatory". FLD = field, ambulatory = AMB. Pilih salah satu sesuai jenis kunjungan | done (mapping/): FLD dipertahankan (kunjungan posyandu = lapangan), display jadi "field". **Disetujui** |
| R8 | Baris 72: typo `EpisodeOfCare.Identifer` → `EpisodeOfCare.identifier` | done (mapping/) |
| R9 | Baris 90: Encounter.participant mereferensi PractitionerRole, tapi tidak ada blok PractitionerRole di dictionary (yang ada hanya Practitioner) | done (mapping/): reference diganti ke Practitioner (bidan desa). **Disetujui** |
| R10 | Baris 43, 45: placeholder "Gedung {Tempat yang melayani ANC}" ditaruh di kolom Display. Seharusnya di kolom Definisi Operasional | done (mapping/) |
| R11 | Dictionary Raffle belum punya kolom `jumlah code` dan `jumlah instance` | done (mapping/) |
| R12 | "Input Data" (Observation 385438008: Sigizi / E-pus PKD / E-pus) tidak punya kolom BQ | done: lupa ditambahkan. Kolom BQ `input_data` dibuat (nama sementara, ganti kalau nama di pipeline beda). Lihat Catatan pipeline |
| R14 | Variabel puskesmas belum masuk payload (hanya di blok Organization). Isian puskesmas dipilih dari list yang sudah ada, jadi Organization cukup di-lookup dari master data | done (mapping/): blok Organization dihapus. `puskesmas` dipindah ke `Encounter.serviceProvider.reference` dengan keterangan lookup master data. `Location.managingOrganization` dan `EpisodeOfCare.managingOrganization` diberi keterangan memakai Organization hasil lookup yang sama |
| R15 | Baris `Observation.encounter.reference` dobel di blok Observation Input Data | done (mapping/): baris kedua dihapus |
| R16 | Ada 2 Practitioner (bidan desa & data entry), tapi `Observation.performer.reference` hanya ditulis "Reference ke resources Practitioner". Belum jelas yang mana | done (mapping/): performer = Practitioner **data entry** |
| R17 | `lokasi_faskes` ditaruh di `Location.identifier`, sedangkan `Location.name` hanya berisi placeholder. Kalau isian lokasi_faskes berupa nama (bukan kode), seharusnya ke `Location.name` | done (mapping/): `lokasi_faskes` dipindah ke `Location.name` |
| R13 | Practitioner data entry sudah ditambahkan (baris 70 di `mapping/`), tapi `Encounter.participant` ADM baru punya `individual.display` (baris 94). Belum ada `individual.reference` ke Practitioner data entry, padahal ATND (bidan) punya | done (mapping/): tambah `Encounter.participant.individual.reference` → Practitioner data entry. Reference ATND diberi keterangan Practitioner bidan desa |

## Form: SiGizi ANC (PHDT Data Dictionary)

Sumber: PHDT Data Dictionary - SiGiziANC (nomor baris = baris CSV asli, header 7 baris). Contoh data mentah: PUSKESMAS PADAMARA SiGizi Pengukuran ANC (57 baris, 2026-11-16). Versi revisi: `mapping/phdt-data-dictionary-sigizi-anc.csv` (ada 1 baris sisipan setelah baris 268 dan 2 sel multi-baris jadi 1 baris, jadi nomor baris bergeser; untuk nomor baris terbaru lihat `output/sigizi-anc.md`).

### Tally variabel BQ vs dictionary

**49 variabel BQ = 49 variabel di dictionary = 49 kolom di file mentah** ✅ (setelah S16, S17, S19). Semua masuk payload. Struktur kolom file mentah: `raw/sigizi-anc-kolom.md`. Catatan: di Excel kolom NIK ada sebelum Nama (S29).

| Variabel BQ | Variabel di dictionary (baris asli) | Path FHIR | Cocok? |
|---|---|---|---|
| nama | Nama Ibu (8) | Patient.name.text | ✅ (Excel kolom C, S29) |
| nik | No Ktp (10) | Patient.identifier (nik) | ✅ (Excel kolom B, S29) |
| tanggal_lahir | Tanggal Lahir (18) | Patient.birthDate | ✅ |
| umur | Umur (150) | Observation 424144002 | ✅ |
| prov_domisili | Nama Provinsi (26) | Patient.address.extension province | ✅ (isi nama → lookup kode, P14) |
| kabkota_domisili | Nama Kabupaten (29), Kab/Kota (23) | Patient.address.city + extension city | ✅ |
| kec_domisili | Nama Kecamatan (32) | Patient.address.extension district | ✅ |
| puskesmas_domisili | Puskesmas Domisili (baris baru) | Patient.managingOrganization (kunci lookup posyandu) | ✅ (S19) |
| desakel_domisili | Nama Desa (35) | Patient.address.extension village | ✅ |
| posyandu_domisili | Posyandu Domisili (1027) | Patient.managingOrganization.reference (lookup master data) | ✅ (S19) |
| alamat_domisili | Alamat Domisili (20 → 21) | Patient.address.line | ✅ (S1) |
| faskes_yang_melayani_anc | Faskes yang melayani ANC | Encounter.serviceProvider.reference (lookup master data) + Encounter.location.display | ✅ (S18) |
| pemeriksaan_pertama | Pemeriksaan Pertama (264) | Observation SP000002 + Encounter.identifier K1M/K1A | ✅ (S20) |
| tanggal_hpht | HPHT (164) | Observation 8665-2 + EpisodeOfCare.period.start | ✅ |
| pemeriksaan_anc_tanggal_anc | Tanggal ANC (122) | Encounter.period.start | ✅ |
| pemeriksaan_anc_usia_kehamilan | Usia Kehamilan (baris baru) | Observation 18185-9 Gestational age | ✅ (S16) |
| pemeriksaan_anc_tenaga_pemeriksa | Tenaga Pemeriksa (85 → 87) | PractitionerRole.code | ✅ |
| pemeriksaan_anc_riwayat_imun_tt_terakhir | Riwayat Imun TT Terakhir (218 → 230) | Immunization VG139 / Observation SP000001 | ✅ |
| pemeriksaan_anc_berat | Berat Badan (277) | Observation 29463-7 | ✅ |
| pemeriksaan_anc_tinggi | Tinggi (190) | Observation 8302-2 | ✅ |
| pemeriksaan_anc_lila | LILA (305) | Observation 284473002 | ✅ (S6) |
| pemeriksaan_anc_tekanan_darah | Tekanan Darah (291) | Observation 392570002 | ✅ |
| pemeriksaan_anc_tfu | TFU (322) | Observation 289625003 | ✅ |
| pemeriksaan_anc_presentasi_janin | Presentasi Janin (381) | Observation 72155-5 | ✅ |
| pemeriksaan_anc_djj | DJJ (366) | Observation 289437007 | ✅ |
| pemeriksaan_anc_diperiksa_usg | USG (397 → 399), Diperiksa USG (409) | Procedure 88.78 + Observation 268445003 | ✅ |
| pemeriksaan_anc_imt_sebelum_hamil | IMT Sebelum Hamil (204) | Observation OC000010 | ✅ (data P12) |
| pemeriksaan_anc_jumlah_ttd_diterima | Jumlah TTD Diterima (424 → 457) | MedicationRequest + MedicationDispense TTD | ✅ |
| pemeriksaan_anc_jumlah_mms_diterima | Jumlah MMS Diterima (494 → 515) | MedicationRequest + MedicationDispense MMS | ✅ |
| pemeriksaan_anc_lab_golongan_darah | Lab : Golongan Darah (335) | Observation 883-9 | ✅ |
| pemeriksaan_anc_lab_rhesus | Lab : Rhesus (351) | Observation 10331-7 | ✅ |
| pemeriksaan_anc_lab_hiv | Lab : HIV (542 → 546) | ServiceRequest/Specimen/Observation/DiagnosticReport 68961-2 | ✅ |
| pemeriksaan_anc_lab_hepatitis | Lab : Hepatitis (595 → 599) | ... 75410-1 | ✅ |
| pemeriksaan_anc_lab_siphilis | Lab : Siphilis (648 → 652) | ... 22464-2 | ✅ |
| pemeriksaan_anc_lab_protein_urine | Lab : Protein Urine (701 → 705) | ... 2887-8 | ✅ |
| pemeriksaan_anc_lab_hb | Lab : Hb (754 → 758) | ... 718-7 | ✅ (S15) |
| pemeriksaan_anc_lab_gula_sewaktu | Lab : Gula Sewaktu (827 → 831) | ... 74774-1 | ✅ |
| pemeriksaan_anc_lab_lainnya | Lab : Lainnya (888) | Observation 15220000 | ✅ |
| pemeriksaan_anc_tatalaksana_anemia | Tatalaksana Anemia (904) | Observation SP000007 | ✅ |
| pemeriksaan_anc_pre_eklampsia | Pre Eklampsia (922) | Observation SP000010 | ✅ |
| pemeriksaan_anc_tatalaksana_pre_eklampsia | Tatalaksana Pre Eklampsia (938) | Observation SP000012 | ✅ |
| pemeriksaan_anc_status_gizi_kektidak_kek | Status Gizi KEK/Tidak KEK (318) | Observation LILA `interpretation` | ✅ |
| pemeriksaan_anc_tatalaksana_kek | Tatalaksana KEK (957) | Observation SP000014 | ✅ |
| pemeriksaan_anc_risiko_masalah_kesehatan_lainnya | Risiko Masalah Kesehatan Lainnya (971) | Observation SP000015 | ✅ |
| pemeriksaan_anc_diberikan_tatalaksana_masalah_kesehatan_lainnya | Diberikan Tatalaksana ... (988) | Observation SP000016 | ✅ |
| pemeriksaan_anc_konseling | Konseling (1001 → 1003) | Procedure 1230101008 | ✅ |
| pemeriksaan_anc_skrinning_keswa | Skrinning Keswa (1013 → 1015) | Procedure 385892002 | ✅ |
| pemeriksaan_anc_tanggal_perkiraan_persalinan | Tanggal Perkiraan Persalinan (177) | Observation 11778-8 | ✅ |
| pemeriksaan_anc_aksi | Aksi (baris baru) | Encounter.extension sigizi-aksi (valueUrl) | ✅ (S17) |

### Temuan

| # | Temuan | Status |
|---|---|---|
| S1 | Baris 21: path `Patient.line`, label "Alamat Domisili" di baris `.use` (20) | done (mapping/): jadi `Patient.address.line`, label pindah ke baris 21 |
| S2 | Baris 75: path `Organization.address.extension.url` di blok Location (sama dengan MO #4, Raffle R5) | done (mapping/) |
| S3 | Baris 94: typo `EpisodeOfCare.Identifer` | done (mapping/) |
| S4 | Placeholder pakai kurung campur `(X}` / `(X)` (baris 106–107, 294–296, 891–894, 907–911, 925–929, 941–945, 960–961, 974–979, 991–992) | done (mapping/): jadi `{X}` |
| S5 | Observation Pemeriksaan Pertama (SP000002) tidak punya `Observation.subject.reference` | done (mapping/): baris baru setelah baris 268 |
| S6 | Baris 309 `Observation.valueQuantity.value` LILA tidak punya placeholder `{LILA}` | done (mapping/) |
| S7 | Immunization: typo `occurenceDateTime` (224, 243), `vaccineCode` tanpa `.coding` (220, 239) | done (mapping/) |
| S8 | Typo `medicataionReference` (449, 483, 507, 529) | done (mapping/): `medicationReference` |
| S9 | `MedicationDispense.subject.display` (485, 531) tanpa `{Nama}` | done (mapping/) |
| S10 | `Observation.Interpretation.coding` huruf besar (786, 792, 798, 802, 859, 863); KEK (318–320) tanpa `.coding` | done (mapping/): `Observation.interpretation.coding` |
| S11 | `ServiceRequest.category/code`, `DiagnosticReport.category/code` (HIV, Hepatitis, Sifilis) dan `Specimen.type` tanpa `.coding`, padahal lab lain pakai | done (mapping/): semua pakai `.coding` |
| S12 | Spasi/tab/newline di sel Code & CodeSystem (`\t\nother-hcf` di 912/946, URL berakhiran spasi, `false `) | done (mapping/) |
| S13 | Value Name beda dengan label di SiGizi: TD `Normal (< 140)` vs `Normal (<= 140)`, `Hipertensi (≥140)` vs `(>= 140)`, USG `hasil tidak normal` vs `kecurigaan hasil abnormal`, typo `eklmapsia`, `skrining TT` vs `skrinning TT`, `SPOG` vs `SpOG`, `letak bokong/ lintang`, `Normal <200` | done (mapping/): disamakan dengan label SiGizi. Catatan: di form sumber batas TD 140 masuk ke 2 pilihan (P16) |
| S14 | Label variabel ada di baris pembuka blok (`.active`, `.category`, `contained.resourceType`), bukan di baris nilai | done (mapping/): label + kolom BQ pindah ke baris nilai (PractitionerRole.code, Procedure.status, quantity.value, ServiceRequest.code, protocolApplied) |
| S15 | Baris 802: code Anemia Berat berisi `what do yo eeeee` | done (mapping/): **OI000034** |
| S16 | `pemeriksaan_anc_usia_kehamilan` (file mentah: "24 Minggu") tidak ada di dictionary | done (mapping/): Observation baru LOINC **18185-9** Gestational age, valueQuantity satuan `wk`, setelah blok HPHT |
| S17 | `pemeriksaan_anc_aksi` = kolom "Aksi" di export web (link halaman perkembangan bumil SiGizi) | done (mapping/): `Encounter.extension` url `http://terminology.kemkes.go.id/sp/sigizi-aksi` (S31), `valueUrl` = isi Aksi. Di file Padamara kolom ini kosong 57/57 (S30) |
| S18 | Faskes yang melayani ANC: blok Organization (40–57) + Location (59–82) dibuat dari nama faskes. Isinya campur: puskesmas, RS, nama bidan (PMB), "Kunjungan rumah", "DSOG" | done (mapping/): isian string → **lookup** master data. Blok Organization & Location dihapus. `Encounter.serviceProvider` = lookup Organization, `Encounter.location` = lookup Location. Reference Organization/Location lain diberi keterangan yang sama |
| S19 | Posyandu domisili: blok Organization posyandu (1030–1048) + `puskesmas_domisili` hanya di `Organization.partOf`, jadi di luar payload | done (mapping/): string posyandu → **lookup** master data (type 131) dengan kunci posyandu + desa + puskesmas domisili. Blok Organization posyandu dihapus; `puskesmas_domisili` jadi baris "Kunci lookup" di Patient |
| S20 | Pemeriksaan Pertama → `Encounter.identifier` K1M/K1A dengan system terminology (`.../CodeSystem/episodeofcare/ANC`) | ok: **kesepakatan SatuSehat**, tetap. K1M/K1A dihitung sebagai opsi code |
| S21 | 6 PractitionerRole "Laboratory worker" (1 per lab) tanpa data dari form. Reference `performer` jadi ambigu dengan PractitionerRole tenaga pemeriksa | done (mapping/): 6 blok dihapus. `performer` ServiceRequest/Observation lab/DiagnosticReport = **lookup** PractitionerRole default lab milik Organization faskes. `ServiceRequest.requester` = PractitionerRole tenaga pemeriksa |
| S22 | Lab "Tidak Diperiksa" (mayoritas di Padamara): ServiceRequest/Specimen/DiagnosticReport tetap dibuat? | done (mapping/): **tidak dibuat**; cukup Observation dengan dataAbsentReason not-performed (Definisi Operasional di baris pertama SR/Specimen/DR) |
| S23 | TTD: code KFA MedicationRequest `92000653` ≠ MedicationDispense `93015491`. Jumlah 0 (banyak di Padamara) belum ada aturannya | done (mapping/): beda code KFA **ok**. Jumlah 0 → MedicationRequest/Dispense **tidak dibuat** (SatuSehat tidak menerima 0). Cara mencatat "0, bukan kosong" masih open (S32) |
| S24 | Condition `134435003` belum di-allow SatuSehat (catatan di kolom Keterangan dictionary) | ok: tetap 134435003 |
| S25 | Encounter.class AMB/FLD/HH tidak punya sumber variabel | ok: Definisi Operasional sudah ada (Faskes → AMB, luar faskes mis. Posyandu → FLD, kediaman pasien mis. Kunjungan rumah → HH). Diturunkan dari `faskes_yang_melayani_anc` (P21) |
| S26 | EpisodeOfCare: belum ada keterangan cara mencari episode ANC aktif | done (mapping/): cari EpisodeOfCare ANC active milik pasien, kalau tidak ada buat baru |
| S27 | Immunization riwayat TT: `occurrenceDateTime` = Tanggal ANC, padahal tanggal suntik sebenarnya tidak diketahui | ok: tetap Tanggal ANC; `primarySource` = false menandakan ini pernyataan. Ditulis di Definisi Operasional |
| S28 | DiagnosticReport HIV/Hepatitis/Sifilis category `MB` (Microbiology), lebih tepat `SR` (Serology). MedicationDispense.category pakai CodeSystem `medicationrequest-category` | done (mapping/): `SR` Serology; CodeSystem jadi `http://terminology.hl7.org/fhir/CodeSystem/medicationdispense-category` |
| S29 | Di file mentah kolom B = NIK, C = Nama, sedangkan urutan BQ `nama`, `nik` | open (pipeline P17): pastikan ingestion memetakan berdasarkan nama header |
| S30 | Kolom Aksi di file Padamara kosong 57/57 (tidak ada hyperlink juga). Isi seperti `https://sigizikesga.kemkes.go.id/ppgbm/bumil/perkembangan/<id>.html` terlihat di sumber lain | info: mapping tetap dibuat |
| S31 | URL extension `sigizi-aksi` masih sementara. Perlu dicek juga apakah SatuSehat menerima extension custom di Encounter | URL done: pakai awalan `http://terminology.kemkes.go.id/sp/` → `http://terminology.kemkes.go.id/sp/sigizi-aksi`. Penerimaan di SatuSehat masih open (P22) |
| S32 | Jumlah TTD/MMS = 0: cara mencatat "diberikan 0" (bukan kosong) belum ditentukan | open (lihat opsi di laporan chat 2026-11-16) |

## Form SITB (PHDT Data Dictionary): TB 06, TB 03 SO, TB 03 RO, TB 04, TB 16K

Sumber dictionary: `PHDT_SITB_2.xlsx` (sheet `TB06`, `TB 03 SO`, `TB 03 RO`, `TB 04`, `TB16K (revised)`; sheet `variabel TB 03 SO`, `variabel TB 03 RO`, `Variabel TB 04` = keputusan tim per variabel). Nomor baris di bawah = baris CSV hasil export sheet (baris 1 = header; sel multi-baris digabung jadi 1 baris). Versi revisi: `mapping/phdt-data-dictionary-sitb-<form>.csv`; nomor baris terbaru lihat `output/sitb-<form>.md`.
Variabel BQ: `bq_schema_sitb.xlsx` (tabel `stellar-orb-451904-d9.raw_data.sitb_tb_06`, `sitb_tb_03`, `sitb_tb_03ro`, `sitb_tb_04_fasyankes`, `sitb_tb_04_rujukan`, `sitb_tb_16k`). File mentah: folder Drive SPHERES (export SITB Kab. Purbalingga / PKM Serayu Larangan, Jan–Jun 2025); struktur kolom di `raw/sitb-<form>-kolom.md`. TB 13 SO/RO **tidak dianalisis** (permintaan user).
Kolom dictionary yang diambil: Categories s.d. CodeSystem, Personal Notes, plus `Definisi Operasional`, `jumlah code`, `jumlah instance`. Kolom tracking (status review, postman, dst.) tidak dibawa.

> Sesi 2026-11-17 dijalankan tanpa tanya-jawab (permintaan user). Keputusan yang diambil sendiri ditandai **asumsi** (A1–A12). Jawaban user 2026-11-17 siang sudah diterapkan (lihat kolom status asumsi).
> Baris yang **dicoret** di sheet tidak dipakai: TB06 baris 116–119; TB16K baris 14–15, 116–127, 328–339 (G13).

### Tally variabel BQ vs file mentah vs dictionary

| Form | Kolom file mentah | Variabel BQ (total / isi form) | Dipetakan ke payload | Tidak dimapping (keputusan tim) | Kolom baru (belum ada di BQ) |
|---|---|---|---|---|---|
| TB 06 | 96 | 103 / 96 | 92 | 4: `no_urut`, `bulan` (lokal SITB); `status_diagnosis`, `no_bpjs` (dicoret di sheet) | – (kolom AC "Klasifikasi Terduga TBC" = tambahan user, tidak dihitung) |
| TB 03 SO | 84 | 91 / 84 | 76 | 8: `no_urut`, `no_registrasi_fasyankes`, `noregistrasi_tbc_kabkota`, `bulan` (lokal SITB); 4× `..._no_reg_lab` (keputusan tim) | – |
| TB 03 RO | 144 | 151 / 144 | 140 | 4: `no_urut`, `no_registrasi_fasyankes`, `no_registrasi_tbc_kabkota`, `bulan` (lokal SITB) | – |
| TB 04 | 114 | 118 / 111 | 102 | 12: `no_urut` (lokal SITB); 9× `..._noreg_lab`, `tanda_tangan_petugas_pemeriksa`, `keterangan` (keputusan tim) | `nama_fasyankes`, `kabupaten_fasyankes`, `provinsi_fasyankes` (T04-1) |
| TB 16K | 40 | 48 / 41 | 40 | 1: `no` (lokal SITB) | – |

- "Isi form" = kolom BQ tanpa 7 kolom metadata pipeline (`puskesmas_name`, `puskesmas_id`, `file_name`, `file_date`, `ingestion_timestamp`, `uuid`, `hash_code`). Ketujuhnya tidak ada di file mentah dan tidak dimapping (A1).
- Semua variabel BQ yang dipetakan sudah masuk payload: bagian "Variabel di luar payload" di setiap `output/sitb-*.md` kosong dari ⚠️.
- Daftar lengkap variabel BQ → path FHIR per payload: lihat `output/sitb-<form>.md`.

### Asumsi yang diambil

| # | Asumsi | Berlaku di | Status |
|---|---|---|---|
| A1 | 7 kolom metadata pipeline BQ tidak dihitung di tally dan tidak dimapping | semua | **disetujui**: metadata tidak perlu dicek di tally |
| A2 | Variabel yang ditandai "tidak dimapping" oleh tim (sheet variabel) tetap tidak dimapping, walaupun `aturan.md` bilang semua variabel BQ wajib masuk payload. Perlu keputusan: ikuti tim atau petakan | semua | **diputuskan**: No. Urut, Bulan, No. Reg Fasyankes/Kab = data lokal SITB, tidak perlu. Keputusan lama tim lain tetap. `status_pengobatan` → CarePlan (T03S-6) |
| A3 | Faskes pelapor (Kode/Nama/Jenis/Kepemilikan/Provinsi/Kab) = **lookup** master data. Blok Organization & Location dihapus, kolomnya jadi baris "Kunci lookup" di `Encounter.serviceProvider.reference` | semua | **diubah**: blok Data Faskes (Organization + Location) **tetap dimapping** dan dihitung payload di TB 06, TB 03 SO, TB 03 RO (ada variabel faskes di form): cari di master data (Kode Fasyankes), kalau match di-update. **TB 04 dan TB 16K: lookup saja** (seperti MO & Raffle), blok dihapus |
| A4 | PractitionerRole petugas lab / radiografer = lookup PractitionerRole default lab (sama dengan SiGizi S21). Bloknya dihapus | TB 06, TB 03 SO, TB 04 | **disetujui** |
| A5 | Practitioner "PJ SITB" yang direferensi banyak resource tidak dibuat dari form → lookup master data Practitioner PJ SITB faskes | TB 06, TB 03, TB 04 | **disetujui** |
| A6 | Opsi coded berikut dihitung sebagai code: `ServiceRequest.reasonCode`, `CarePlan.activity.detail.code/productCodeableConcept/statusReason`, `CarePlan.activity.outcomeCodeableConcept`, `Encounter.hospitalization.admitSource`, `QuestionnaireResponse...answer.valueCoding`, `Observation.component.code/valueCodeableConcept`, `Observation.method` (LJ/MGIT). `Specimen.collection.method`, category, dataAbsentReason, unit tetap tidak dihitung | semua | **disetujui** → masuk `aturan.md` |
| A7 | Blok template (1 blok untuk banyak kolom, mis. follow up BTA/Biakan bulan ke-1 s.d. 24) dihitung 1 payload sesuai yang tertulis di dictionary | TB 03 RO | **disetujui** |
| A8 | `EpisodeOfCare.type` di register TB 03 tetap per register: TB 03 SO = TB-SO, TB 03 RO = TB-RO (opsi lainnya dihapus) | TB 03 SO, TB 03 RO | **disetujui** |
| A9 | No. BPJS di TB 06 dipetakan ke Coverage (struktur sama dengan TB 03 SO) | TB 06 | **dibatalkan**: No. BPJS dicoret di sheet TB06 (baris 119); blok Coverage dihapus |
| A10 | Teks bebas "Keterangan (tempat pemeriksaan selain mikroskopis)" → `Observation.note.text` (Observation Hasil Pemeriksaan Diagnosis TBC); "Tindak lanjut penambahan resistansi" → `CarePlan.note.text` | TB 06 | **disetujui** |
| A11 | Kolom BQ `nama_fasyankes` di TB 16K (tidak ada di export) diduga dari header laporan → kunci lookup Organization di Encounter | TB 16K | **diubah**: `nama_fasyankes` adalah kolom terakhir tabel BQ `sitb_tb_16k` (setelah `hash_code`) dan tidak ada di export → diperlakukan sebagai metadata pipeline, tidak dimapping |
| A12 | Kolom file mentah yang belum ada di BQ diberi nama BQ sementara (T06-1, T04-1) | TB 06, TB 04 | **dibatalkan**: TB 06 kolom AC tambahan user (bukan kolom asli SITB); TB 04 DJ–DL tidak ada di format baru |

### Temuan umum (semua form SITB)

| # | Temuan | Status |
|---|---|---|
| G1 | Blok Organization faskes (+ Location gedung faskes) ditulis lengkap di dictionary padahal faskes dipilih dari kode SITB | **diubah** (A3): blok faskes dikembalikan dan dihitung di TB 06, TB 03 SO, TB 03 RO; TB 04 & TB 16K lookup. Path `Organization.address.extension.url` di blok Location TB 06 diperbaiki jadi `Location.…` |
| G2 | PractitionerRole "Laboratory worker"/"Medical radiographer" tanpa data form, 1 blok per pemeriksaan (TB 06: 9, TB 03 SO: 9, TB 04: 16) | done (mapping/): dihapus; `performer` = lookup (A4) |
| G3 | Banyak reference ke "Practitioner" (PJ SITB) dan Organization/Location tanpa blok resource-nya | done (mapping/): Definisi Operasional diisi keterangan lookup (A5) |
| G4 | Path tanpa `.coding`: `ServiceRequest.code/category`, `DiagnosticReport.code/category`, `Observation.code/category/valueCodeableConcept`, `Specimen.type` | done (mapping/): ditambah `.coding` (TB 06: 40 baris, TB 03 SO: 37, TB 03 RO: 9, TB 04: 38, TB 16K: 3) |
| G5 | Typo path: `valuecodeableConcept` (46), `valuableCodeableConcept` (2), `CarePlan.author.refence`, index `[0]` di `admitSource.coding[0]`, resource `Careplan` | done (mapping/) |
| G6 | Biakan: code `Neg` / `Pos` dengan CodeSystem LOINC (bukan code LOINC) | done (mapping/): `LA6577-6` Negative / `LA6576-8` Positive |
| G7 | CodeSystem salah: `X0993xx` di DiagnosticReport LPA pakai LOINC; `20383-6` pakai CodeSystem examination; 18 code foto toraks TB 03 RO tanpa CodeSystem | done (mapping/): examination / loinc / snomed |
| G8 | Kolom "Nama Column BQ" berisi `{...}`, catatan ("gunakan tanggal paling awal…"), atau `True/False` (TB 16K) | done (mapping/): diganti nama kolom BQ; catatan dipindah ke Definisi Operasional |
| G9 | Isi file mentah memakai singkatan yang tidak sama dengan Value Name: `D/ND/RD/RND/IDT`, `S/R`, `L/P`, `Neg/Pos`, `ODHIV/Bukan ODHIV`, `V` (centang), prefix `Fasyankes: <nama>` | open (pipeline P24) |
| G10 | Kolom "tidak dimapping" (keputusan tim) bertentangan dengan aturan "semua variabel BQ wajib masuk payload" | done: pengecualian dicatat di `aturan.md` (data lokal SITB, baris dicoret) |
| G11 | CodeSystem `http://terminology.kemkes.go.id` (tanpa `/CodeSystem/...`) untuk `TK000022` (TB 06) dan `TK000016` (TB 03 SO) | ok: **benar**, code TKxxx memang memakai `http://terminology.kemkes.go.id` (SPxxx memakai `/sp`) |
| G12 | Baris hitungan di akhir sheet (mis. "97", "75", "39") dan spasi di akhir Code/CodeSystem | done (mapping/): dihapus/dirapikan |
| G13 | Baris yang dicoret di sheet sempat ikut dipetakan di analisis pertama (TB06 No. BPJS → Coverage; TB16K Practitioner/PractitionerRole kader, ekstensi alamat kontak, Observation SP000211) | done (mapping/): baris dicoret dihapus dari dictionary revisi |

### TB 06 (Register Terduga TBC)

| # | Temuan | Status |
|---|---|---|
| T06-1 | Kolom AC "Klasifikasi Terduga TBC" ada di export (11 terisi) dan di dictionary (EoC terduga `type`), tapi tidak ada di BQ | **ditutup**: kolom AC adalah kolom tambahan dari user (tidak punya nomor kolom di baris 16 export), bukan kolom asli SITB → tidak dihitung sebagai variabel. Baris 78 dictionary diberi keterangan |
| T06-2 | Keterangan, Tindak lanjut penambahan resistansi hanya label tanpa resource | done (mapping/): note.text (A10). No. BPJS dicoret di sheet, tidak dimapping |
| T06-3 | Tanggal Hasil Pemeriksaan TCM-XDR tidak punya baris | done (mapping/): `Observation.issued` di Observation TCM XDR |
| T06-4 | Tindak Lanjut "Belum Mulai Pengobatan" tidak ada di opsi. Dictionary: sheet `TB06` baris 1020 (label Tindak Lanjut), opsi di baris 1024–1031. Export: `TB_06` kolom CL, 14 baris (baris Excel 1702, 2067, 2105, 2116, 2495, 2592, 4957, 5523, 5580, 5586, 5603, 6072, 6125, 6131) | done (mapping/): code baru **SP001136** Belum Mulai Pengobatan di `CarePlan.activity.detail.code.coding` (kelompok CarePlan active / not-started) |
| T06-5 | Hasil Diagnosis "Bukan TBC" (4.429 baris) diproses lewat blok EoC "bukan TB" (cancelled); opsi type hanya TBC SO/RO | info |
| T06-6 | File `TB_06SO` dan `TB_06RO` di Drive = format TB 06 tanpa kolom AC. Analisis memakai file `TB_06` gabungan | info |

### TB 03 SO (Register Pasien TBC SO)

| # | Temuan | Status |
|---|---|---|
| T03S-1 | `EpisodeOfCare.type` berisi TB-SO dan TB-RO padahal register SO | done (mapping/): opsi TB-RO dihapus (A8) |
| T03S-2 | Pekerjaan berisi `Lain-lain:<teks>` | open (pipeline P26) |
| T03S-3 | Hasil Tes HIV "Tidak Diketahui" tidak ada di opsi. Dictionary: sheet `TB 03 SO` baris 1077–1078 (ODHIV 165816005 / Bukan ODHIV 165815009). Export: `TB_03SO` kolom CB, 8 baris (baris Excel 122, 199, 353, 467, 716, 725, 728, 963) | done (mapping/): `Observation.dataAbsentReason.coding` = `unknown` (data-absent-reason), Value Name "Tidak Diketahui" |
| T03S-4 | Paduan Pengobatan berisi teks bebas di luar daftar code. Dictionary: sheet `TB 03 SO` baris 362 (CP000005) dan opsi baris 363–438. Export: `TB_03SO` kolom AQ, 4 baris: "Kategori 1 + levo 4 tablet" (baris Excel 408), "RHE" (776), "INH 1X300 MG, RIFAMPICIN …" (940), "INH 1X100MG, RIF …" (951) | done (mapping/): **SP001137 Paduan lainnya** untuk teks yang tidak cocok; SP001138–SP001140 dibatalkan. Teks asli selalu di `productCodeableConcept.text`. Varian mirip (Dosis Baru/Lama, `{}`, singkatan BPaLM, `2RHZE 4RH`) = baris alias dengan code lama. Hasil cek BQ 17 Nov: 13 dari 136 nilai cocok langsung |
| T03S-6 | Status Pengobatan (Sesuai standar 943 / Tidak sesuai standar 10) sebelumnya tidak dimapping | done (mapping/): `CarePlan.activity.detail.description` (string, tidak perlu code). Path ini sudah dipakai di sheet `TB 02` baris 95 ("Paduan OAT yang diberikan", activity status in-progress). Di sheet SITB lain hanya ada `CarePlan.description` (teks tetap, TB 01 baris 404, TB 03 SO baris 338, TB 03 RO baris 343) |
| T03S-5 | Terapi DM "OHO" vs Value Name "Obat Hipoglikemik Oral (OHO)" | open (P24) |

### TB 03 RO (Register Pasien TBC RO)

| # | Temuan | Status |
|---|---|---|
| T03R-1 | `EpisodeOfCare.type` berisi TB-SO dan TB-RO | done (mapping/): opsi TB-SO dihapus (A8) |
| T03R-2 | 54 kolom follow up (bulan ke-1 s.d. 24, BTA & Biakan, plus kolom kedua bulan 4–6) hanya punya 1 blok template dengan BQ `BTA` / `B` | done (mapping/): 1 baris per kolom BQ di dalam template (A7, P27) |
| T03R-3 | Baris Observation setengah jadi (identifier/status/category/code tanpa nilai) di antara template BTA dan Biakan | done (mapping/): dihapus |
| T03R-4 | Hasil lab hanya Observation; tidak ada ServiceRequest/Specimen/DiagnosticReport seperti TB 03 SO | done (mapping/): ServiceRequest + Specimen + DiagnosticReport ditambahkan untuk 7 pemeriksaan (Diagnosis 11545-1, TCM-XDR X099379, LPA Lini 1 X099380, LPA Lini 2 X099381, Uji Kepekaan X099383 [Specimen sudah ada], template follow up BTA 11545-1 dan Biakan X099388). Observation diberi `basedOn` + `specimen`. +20 payload |
| T03R-5 | Paduan Pengobatan di export pakai singkatan. Export: `TB_03RO` kolom AP: "Bdq Lzd Mfx Pa" 12 baris (baris Excel 19–20, 22–31), "Lfx RHZE" 2 baris (18, 21). Code-nya **ada** di sheet `TB 03 RO`: baris 441 CP000086 (Bedaquline Pretomanid Linezolid Moxifloxacin) dan baris 439 CP000084 (RHZE + Levofloxacin) | done (mapping/): baris alias `Bdq Lzd Mfx Pa` → CP000086, `Lfx RHZE` → CP000084; varian Dosis Baru → CP000016; selain itu SP001137 Paduan lainnya |
| T03R-6 | Riwayat Pengobatan di export tanpa nomor ("Pasien TB …") vs Value Name "1. Pasien TB …"; DM "Ya/Tidak" vs "positif/negatif" | open (P24) |
| T03R-7 | File contoh hanya 14 baris | info |

### TB 04 (Fasyankes & Rujukan)

| # | Temuan | Status |
|---|---|---|
| T04-1 | Kolom DJ–DL (Nama/Kabupaten/Provinsi Fasyankes) ada di export dan dictionary, tapi tidak ada di BQ | **ditutup**: format export/BQ TB 04 sudah berubah, kolom Nama/Kabupaten/Provinsi Fasyankes tidak ada lagi. Baris dictionary blok Organization tetap ada tanpa kolom BQ (lihat T04-6) |
| T04-2 | Header TB 04 Fasyankes dan TB 04 Rujukan sama (114 kolom) | ok: 1 dictionary `phdt-data-dictionary-sitb-tb04.csv` |
| T04-3 | Observation LPA Lini 2 memakai code `X099380` (LPA Lini 1) | done (mapping/): `X099381` |
| T04-4 | Opsi pertama `Specimen.type` = Pleural fluid (418564007), jadi identitas payload Specimen di output ikut opsi pertama | ok: converter memilih code sesuai Value Name, urutan opsi tidak berpengaruh ke data |
| T04-5 | "No. Identitas Sediaan" dan "Alasan Pemeriksaan" dipakai di 16 Specimen / 16 ServiceRequest | ok (keputusan tim) |
| T04-6 | Blok Data Faskes TB 04 dikembalikan (A3), tapi kolom BQ untuk Nama/Kabupaten/Provinsi Fasyankes tidak ada di format baru. Faskes hanya bisa dicocokkan dari metadata `puskesmas_id` / `puskesmas_name` | done (mapping/): TB 04 hanya pencarian faskes (seperti MO & Raffle). Blok Organization & Location dihapus; `Encounter.serviceProvider.reference` = lookup memakai metadata `puskesmas_id` / `puskesmas_name` |

### TB 16K (Investigasi Kontak)

| # | Temuan | Status |
|---|---|---|
| T16-1 | Tabel BQ `sitb_tb_16k` cocok dengan export SITB "TB 16K Fasyankes" (40 kolom). File `Daftar Laporan TBC 16K - SITK` formatnya lain (35 kolom datar) | info |
| T16-2 | `RelatedPerson.patient` → `.patient.reference` | done (mapping/) |
| T16-3 | EpisodeOfCare 2 baris (hanya `type`) tanpa status/patient; jenis kasus indeks juga ada di Observation 415759006 | done (mapping/): EoC dihapus, Jenis Kasus Indeks di Observation |
| T16-4 | Value Name bergeser 1 baris di Observation kasus indeks (TB SO di baris code) | done (mapping/) |
| T16-5 | `SP000208` Tidak TBC pakai CodeSystem SNOMED; `SP000369` tanpa CodeSystem; `https://` di episodeofcare-type | done (mapping/) |
| T16-6 | Practitioner & PractitionerRole kader dicoret di sheet (baris 14–15); yang berlaku Observation "Kader Kesehatan" SP000373 dengan `valueString` | done (mapping/): nama kader → `Observation.valueString` (koreksi: temuan awal salah) |
| T16-7 | Organisasi kader (Nama Fasyankes/Organisasi Kader) di blok Organization (baris 29) | **disetujui**: lookup Organization di `Observation.performer.reference`; tidak ada blok Organization/Location terpisah di TB 16K |
| T16-8 | Encounter terpotong oleh Condition (statusHistory di blok kedua) | ok: dihitung 1 payload |
| T16-9 | Kolom TPT "< 5 th" dan "≥ 5 th" | done (mapping/): keduanya ke Observation yang sama |
| T16-10 | Observation "Memenuhi syarat TPT" (SP000211) dicoret di sheet (baris 328–339), tapi kolom BQ `memenuhi_syarat_tpt` ada | done (mapping/): dipetakan ke opsi SP000211 di Observation Kesimpulan Eligibilitas TPT (baris 318) |
| T16-11 | Ekstensi kode wilayah alamat kontak dicoret di sheet (baris 116–127) | done (mapping/): dihapus |

## Form MPDN (PHDT Data Dictionary): Kematian Bayi, Kematian Ibu

Sumber dictionary: `PHDT_Data_Dictionary_-_MPDN.csv` (1 file berisi 2 bagian, "LAPORAN KEMATIAN BAYI" dan "LAPORAN KEMATIAN IBU"), dipecah jadi `mapping/phdt-data-dictionary-mpdn-kematian-bayi.csv` dan `mapping/phdt-data-dictionary-mpdn-kematian-ibu.csv`. Nomor baris di bawah mengikuti file di `mapping/` (header = baris 1–3). Output: `output/mpdn-kematian-bayi.md`, `output/mpdn-kematian-ibu.md`. Tabel BQ di form tracker: `raw_data.mpdn_laporan_kematian_bayi` dan `raw_data.mpdn_laporan_kematian_ibu`.

> **Belum ada comprehensive review.** Sesi 2026-11-24 dijalankan tanpa cross-check (permintaan user): tidak ada daftar variabel BQ, tidak ada file mentah, dan belum dibahas dengan tim MPDN. Angka payload/code dan temuan di bawah hanya hasil membaca dictionary. Keputusan yang diambil sendiri ditandai **asumsi** (MA1–MA10), semuanya masih menunggu konfirmasi.

### Hasil hitung

| Form | Payload | Code | Code unik | Code SP |
|---|---|---|---|---|
| MPDN Kematian Bayi | 19 (Patient 2, Observation 16, Composition 1) | 112 | 76 | 37 |
| MPDN Kematian Ibu | 10 (Patient 1, Condition 1, Observation 7, Composition 1) | 50 | 50 | 17 |

### Perubahan pada file (dibuat otomatis, bisa diulang dari file asli)

| # | Perubahan | Status |
|---|---|---|
| F1 | Baris judul bagian dan 8 baris kosong di ujung bagian Ibu dibuang (file dipecah jadi 2) | done (mapping/) |
| F2 | Kolom `Nama Column BQ` dan `Nama Column Raw` ditambahkan (**kosong**), plus `jumlah code` dan `jumlah instance` | done (mapping/) |
| F3 | Angka `24` nyasar di kolom Subcategories (Ibu baris 164, di samping Status Data) dihapus. Isinya hitungan variabel, bukan data | done (mapping/) |
| F4 | Spasi/tab/newline di kolom Code, Display, CodeSystem dirapikan (Bayi 16 sel, Ibu 1 sel). CodeSystem `https://loinc.org` di Cara Persalinan (57071-3) jadi `http://loinc.org` | done (mapping/) |
| F5 | 26 baris `Composition.entry.display/reference` di Bayi jadi `Composition.section.entry.display/reference` (Composition tidak punya `entry` di level atas; 10 baris lain di Bayi dan semua di Ibu sudah memakai `section.entry`) | done (mapping/) |

### Tally variabel (tanpa BQ)

Daftar kolom BQ belum ada, jadi tally BQ ↔ dictionary belum bisa dicek. Sebagai pengganti: jumlah nama variabel unik di kolom `Original Variables`.

| Form | Nama unik di dictionary | Bukan variabel (dikeluarkan) | Variabel | Rekap user | Cocok? |
|---|---|---|---|---|---|
| Kematian Bayi | 43 | `//PJ MPDN` + 5 placeholder nama (`nama pasien 1`, `nama pasien 2 (hanya lahir mati)`, `nama pasien 2 (hanya lahir hidup)`, `nama pasien bayi (hanya lahir hidup)`, `nama bayi (generated)`) = 6 | **37** | 37 | ✅ |
| Kematian Ibu | 25 | `//PJ MPDN` = 1 | **24** | 24 | ✅ |

- Semua variabel di dictionary masuk ke payload: bagian "Variabel di luar payload" di kedua `output/mpdn-*.md` kosong. Karena kolom BQ kosong, baris "Variabel BQ (unik)" di output = 0.
- Cocok dengan rekap tim hanya kalau 6 nama di atas (Bayi) dan `//PJ MPDN` (Ibu) memang bukan kolom BQ. Perlu dicek begitu daftar BQ ada.

### Asumsi yang diambil

| # | Asumsi | Berlaku di | Status |
|---|---|---|---|
| MA1 | 1 `Composition` per laporan = 1 payload. Blok Location di `Composition.contained` (Faskes Lahir, Faskes Meninggal) adalah bagian dari Composition, **tidak** dihitung payload terpisah | Bayi, Ibu | open |
| MA2 | Bayi punya 2 Patient (ibu dan bayi) = 2 payload (resource sama tanpa code pembeda dihitung masing-masing, seperti Practitioner di Raffle) | Bayi | open |
| MA3 | `Composition.type.coding` (COM000001/2/3) dihitung sebagai code karena membedakan jenis formulir. `Composition.section.code` (LOINC penanda bagian) dan `Composition.contained.type` (LT000001, LT000005) tidak dihitung | Bayi, Ibu | open |
| MA4 | Opsi `Observation.valueCodeableConcept` dan `Observation.component.code` dihitung (aturan A6 SITB). Component Usia Meninggal (SP000716–718) dan Dugaan Sebab (TK000019–21) ikut dihitung | Bayi, Ibu | open |
| MA5 | Isian `ICD-PM.xlsx` / `[PUBLIC] ICD-MM (Maternal Mortality)` adalah penunjuk ke daftar kode eksternal, bukan satu code → tidak dihitung | Bayi, Ibu | open |
| MA6 | Condition Diagnosis Kematian (Ibu) memakai `{Kode ICD}` dinamis → 1 payload, 0 code | Ibu | open |
| MA7 | `Patient.gender`, `Patient.maritalStatus` (code tetap HL7) tidak dihitung sebagai code | Bayi, Ibu | open |
| MA8 | `//PJ MPDN` bukan variabel; Practitioner PJ MPDN = lookup master data (seperti PJ SITB, A5), tidak dibuat dari form dan tidak dihitung payload | Bayi, Ibu | open |
| MA9 | 5 placeholder nama pasien (`nama pasien 1`, dst.) bukan variabel, hanya isian referensi `subject.display` / `focus.display` | Bayi | open |
| MA10 | Tidak ada file mentah dan daftar BQ → kolom `Nama Column BQ` / `Nama Column Raw` dibiarkan kosong, tidak ada nama BQ sementara | Bayi, Ibu | open |

### Temuan

| # | Form | Temuan | Status |
|---|---|---|---|
| MG1 | Bayi, Ibu | `//PJ MPDN` (awalan `//`) dipakai sebagai `performer.display` di 16 Observation Bayi, 7 Observation Ibu, dan `Composition.author.display`, tapi tidak ada blok Practitioner di dictionary. Perlu dipastikan asalnya (kolom BQ apa, atau lookup) | open |
| MG2 | Bayi, Ibu | Tidak ada Encounter. Semua Observation/Condition hanya mereferensi Patient (form lain memakai `Observation.encounter.reference`). Perlu keputusan: laporan kematian tanpa Encounter, atau buat Encounter | open |
| MG3 | Bayi, Ibu | `Observation.effectiveDateTime` = Tgl. Meninggal dan `issued` = Wkt. Lapor dipakai di semua Observation, termasuk data persalinan dan kehamilan (Jam Lahir, Berat Lahir, Gravida, Usia Kehamilan, Jenis Kehamilan, Umur Ibu). Tanggal meninggal sebagai waktu efektif berat lahir kurang tepat | open |
| MG4 | Bayi | Variabel ditaruh di baris struktural, bukan baris nilai (mis. `Tgl. Meninggal` di `Observation.status`, baris 76). Hanya rapi di dictionary, tidak mengubah hitungan | open |
| MG5 | Bayi, Ibu | Kode ICD-PM (Bayi) dan ICD-MM (Ibu) belum berupa daftar code. Butuh value set (`icd-10-pm`, `icd-10-mm`) supaya bisa dihitung dan divalidasi | open |
| MG6 | Bayi, Ibu | Variabel status Composition bernama `Pelapor` di Bayi (baris 359; opsi `VALID TANPA NIK`, `... VERIFIED`, `... FINAL`) dan `Status Data` di Ibu (baris 164; opsi `VERIFIED`). Nama berbeda untuk data yang sama, dan isi `Pelapor` sebenarnya status verifikasi | open |
| MB1 | Bayi | Component Umur Jam / Menit / Detik (SP000716–718, baris 61–68) tidak punya variabel. Hanya `Usia Meninggal (Hari)` yang ada. Dari mana nilai jam/menit/detik? | open |
| MB2 | Bayi | Label "hanya lahir mati / hidup" tidak konsisten. `focus.display` berlabel "lahir mati" di 9 blok (baris 51, 83, 101, 133, 159, 191, 247, 259, 273), termasuk data persalinan yang ada di kedua jenis (Tempat Lahir, Tipe Faskes Lahir, Jam Lahir, Berat Lahir). Blok persalinan lain (Cara Persalinan, Penolong, Gravida, Usia Kehamilan, Jenis Kehamilan, Umur Ibu) berlabel "lahir hidup" | open |
| MB3 | Bayi | Typo `Faskese Lahir` di kolom Original Variables (baris 335). Tidak diubah karena bisa jadi nama kolom asli | open |
| MB4 | Bayi | Kode `OV000394` (Kehamilan Ganda Empat atau Lebih, baris 310) ber-CodeSystem SNOMED, padahal awalan `OV` = clinical-term Kemkes | open |
| MB5 | Bayi, Ibu | Display kode 264362003 tidak sama: `Home` (Bayi baris 126) vs `Home (environment)` (Bayi baris 184, Ibu baris 113) | open |
| MB6 | Bayi | `Composition.section` "Riwayat Kehamilan" yang kedua (isi: Umur Ibu, baris 413) memakai LOINC 45970-1 "Demographic information section", judul dan code tidak cocok | open |
| MI1 | Ibu | `Condition.code.coding` = `{Kode ICD}` dengan CodeSystem `http://snomed.info/sct` (baris 30). Isinya kode ICD, seharusnya `http://hl7.org/fhir/sid/icd-10` (seperti Condition TB) | open |
| MI2 | Ibu | Masa Terjadi Kematian Ibu memakai path `Observation.valueCodeableConcept` tanpa `.coding` (baris 71–73), berbeda dengan blok lain | open |

## Form ePuskesmas (PHDT_ePus.xlsx): 11 dictionary

Sumber: `PHDT_ePus.xlsx` (19 sheet), dipecah per form jadi `mapping/phdt-data-dictionary-epus-<form>.csv` oleh `scripts/epus_prepare.py` (bisa diulang dari file asli).

> **Belum comprehensive review.** Dikerjakan tanpa daftar variabel BQ, tanpa file mentah, dan belum dibahas dengan tim. Pemisahan blok payload dan penentuan code dilakukan otomatis (heuristik) dan **belum dicek manual per blok**. Angka di bawah = hasil hitung dictionary, bukan angka final. Semua asumsi ditandai EA.

### Sheet → form

| Sheet | Form di tracker | Dictionary | Baris sheet → CSV |
|---|---|---|---|
| `epus layanan` | #1 Pelayanan Pasien | `mapping/phdt-data-dictionary-epus-pelayanan.csv` | 978 → 317 |
| `old epusk kunjungan ibu hamil` | #3 Kunjungan Ibu Hamil | `mapping/phdt-data-dictionary-epus-kunjungan-ibu-hamil.csv` | 1344 → 1245 |
| `epus lab` | #5 Laboratorium | `mapping/phdt-data-dictionary-epus-lab.csv` | 4606 → 3340 |
| `epus rujukan eksternal` | #8 Rujukan Eksternal | `mapping/phdt-data-dictionary-epus-rujukan-eksternal.csv` | 46 → 46 |
| `epus ordal anc` | #11 ANC | `mapping/phdt-data-dictionary-epus-anc.csv` | 2383 → 2053 |
| `epus ordal inc` | #12 INC | `mapping/phdt-data-dictionary-epus-inc.csv` | 1242 → 1134 |
| `epus ordal pnc` | #13 PNC | `mapping/phdt-data-dictionary-epus-pnc.csv` | 2200 → 1195 |
| `epus mtbs` | #14 MTBS | `mapping/phdt-data-dictionary-epus-mtbs.csv` | 3193 → 2260 |
| `epus mbtm` | #15 MTBM | `mapping/phdt-data-dictionary-epus-mtbm.csv` | 3517 → 1140 |
| `epusk tumbang` | #16 Tumbuh Kembang (Anak) | `mapping/phdt-data-dictionary-epus-tumbang-anak.csv` | 1281 → 338 |
| `epus DDTKSDIDTK` | #16 Tumbuh Kembang (DDTK) | `mapping/phdt-data-dictionary-epus-tumbang-ddtk.csv` | 1389 → 475 |

Sheet yang **tidak dipakai**: `Daftar Isi`; `epus layanan (revised)` (parsial, hanya dipakai untuk mengisi nama kolom raw Pelayanan); `var epus bumil (KIA)`, `var epus mtbs`, `tracker variable anc/inc/pnc` (daftar variabel/tracker, bukan mapping FHIR); `Epusk Data Pasien` (tidak ada di tracker maupun daftar PHDT, belum ada keputusan).
Form tracker yang belum ada mapping di file ini, diabaikan: #4 Kohort KIA, #6 LPLPO, #9 Kunjungan BPJS, #10 Kunjungan Pasien, dan Dapodik Antropometri DDTK. (Tumbuh Kembang KPSP/TDD/TDL/KMPE/M-CHAT-R/GPPH dan Dapodik PAUD sudah dihitung, lihat bagian masing-masing.)

### Hasil hitung dan perbandingan variabel dengan PHDT

Variabel = nama variabel unik di dictionary. "Baris" = jumlah baris variabel (nama yang sama di beberapa blok dihitung tiap baris). Angka yang dipakai di output utama = variabel unik.

| Form | Payload | Code | Variabel (unik) | Variabel (baris) | PHDT (referensi) | Selisih unik vs PHDT |
|---|---|---|---|---|---|---|
| ePuskesmas Pelayanan Pasien | 47 | 62 | 81 | 81 | 80 (ePuskesmas | Pelayanan) | +1 |
| ePuskesmas Kunjungan Ibu Hamil | 114 | 198 | 68 | 75 | 97 (ePuskesmas | KIA) | -29 |
| ePuskesmas Laboratorium | 309 | 429 | 22 | 22 | 23 (ePuskesmas | Laboratorium) | -1 |
| ePuskesmas Rujukan Eksternal | 5 | 0 | 23 | 23 | 22 (ePuskesmas | Rujukan) | +1 |
| ePuskesmas ANC (KIA Harian) | 155 | 321 | 123 | 136 | 136 (ePuskesmas | ANC - Ibu Hamil) | -13 |
| ePuskesmas INC (KIA Harian) | 69 | 206 | 93 | 93 | 82 (ePuskesmas | INC - Persalinan) | +11 |
| ePuskesmas PNC (KIA Harian) | 82 | 161 | 107 | 109 | 96 (ePuskesmas | PNC - Ibu Nifas) | +11 |
| ePuskesmas MTBS (KIA Harian) | 125 | 268 | 187 | 199 | 187 (ePuskesmas | MTBS) | +0 |
| ePuskesmas MTBM (KIA Harian) | 57 | 139 | 105 | 121 | 115 (ePuskesmas | MTBM) | -10 |
| ePuskesmas Tumbuh Kembang - Anak | 19 | 55 | 34 | 34 | 34 (ePuskesmas | Tumbang - Anak) | +0 |
| ePuskesmas Tumbuh Kembang - DDTK/SDIDTK | 29 | 68 | 38 | 38 | 38 (ePuskesmas | Tumbang - DDTK) | +0 |

Selisih tidak mengubah angka output. Catatan: ANC baris = 136 = PHDT, unik 123 (13 nama muncul di >1 blok); MTBS 187 cocok; Tumbang Anak/DDTK cocok; Kunjungan Ibu Hamil memakai sheet lama (`old epusk kunjungan ibu hamil`) dibanding PHDT "KIA" 97; selisih INC/PNC (+11) dan MTBM (−10) belum dijelaskan.

### Asumsi yang diambil

| # | Asumsi | Berlaku di | Status |
|---|---|---|---|
| EA1 | Sheet dipetakan ke form berdasarkan nama sheet dan kecocokan jumlah variabel dengan PHDT (tabel di atas) | semua | open |
| EA2 | Organization dan Location = lookup master data, tidak dihitung payload (sama seperti form lain) | semua | open |
| EA3 | Pemisahan blok payload otomatis: tiap resource baru / pengulangan code pembeda = payload baru. Patient dan Encounter dihitung sekali per form. Blok Condition yang `clinicalStatus`-nya di bawah `code` (mis. RPS/RPD di Pelayanan) bisa menyatu. Lab (banyak baris alias), Kunjungan Ibu Hamil, ANC, MTBS perlu dicek ulang | semua | open |
| EA4 | Code dihitung hanya dari path determining/opsi coded (Observation/Condition/Procedure/ServiceRequest/DiagnosticReport .code, Specimen.type, EpisodeOfCare.type, Immunization.vaccineCode, valueCodeableConcept, interpretation, method, component, reasonCode, CarePlan activity, QuestionnaireResponse answer). `conclusionCode` dan code HL7 tetap tidak dihitung | semua | open |
| EA5 | Kode dinamis (`kode dapat merujuk ...`, `{kode ...}`) = 1 payload, 0 code (Lab: template ServiceRequest/Observation/DiagnosticReport tidak dihitung, hanya baris per-pemeriksaan) | Lab, Pelayanan | open |
| EA6 | Kode LOINC yang rusak jadi tanggal di Excel (mis. `8302-02-01` → `8302-2`) dipulihkan otomatis. Jumlahnya 3–13 sel per form (kecuali Rujukan Eksternal: 0); dibuat ulang oleh `scripts/epus_prepare.py` | semua | done |
| EA7 | Kolom catatan di sheet digabung ke `Keterangan`. Resource salah ketik `Careplan` → `CarePlan` (Pelayanan 4 baris); resource kosong diisi dari path (Pelayanan 12 baris) | Pelayanan | done |
| EA8 | Nama kolom raw Pelayanan diambil dari sheet `epus layanan (revised)` (64 baris) kalau cocok; form lain kolom `Nama Column BQ` / `Nama Column Raw` dibiarkan kosong | Pelayanan, lainnya | open |
| EA9 | Tumbuh Kembang = 1 baris tracker (#16) tapi 2 dictionary (Anak, DDTK), dihitung sebagai 2 form | #16 | open |
| EA10 | Praktisi lab (PractitionerRole kode 1290220002) = lookup, tidak dihitung (seperti SiGizi ANC) | Lab, ANC, PNC, MTBS, Kunjungan | open |

### Temuan awal (otomatis)

| # | Temuan | Status |
|---|---|---|
| EF1 | Tidak ada daftar BQ / file mentah, tally BQ belum bisa dicek. Pelayanan 64 dari 81 variabel dapat nama raw dari sheet revised | open |
| EF2 | Kunjungan Ibu Hamil: 1 baris `resource` berisi path (`Observation.dataAbsentReason`) dibetulkan; sheet bernama "old", perlu dikonfirmasi apakah ini versi yang dipakai | open |
| EF3 | Rujukan Eksternal: 23 variabel tapi 5 payload dan 0 code (isian bebas / lookup); referensi PHDT 22 | open |
| EF4 | Angka Lab (309 payload) sangat bergantung pada jumlah baris alias per pemeriksaan; perlu dipastikan satu pemeriksaan = satu set ServiceRequest/Specimen/Observation/DiagnosticReport | open |

## Tumbuh Kembang tambahan (Childhood Development Toolkit): KPSP, TDD, TDL, KMPE, M-CHAT-R, GPPH

Sumber: `Childhood_Development_Toolkit_Data_Dictionary.xlsx` (12 sheet), dipecah per form oleh `scripts/tumbang_prepare.py` ke `mapping/phdt-data-dictionary-epus-tumbang-<form>.csv` (pakai logika yang sama dengan `epus_prepare.py`). Form ini melengkapi baris #16 (Tumbuh Kembang) di tracker.

> **Belum comprehensive review.** Tanpa daftar BQ dan file mentah, belum dibahas dengan tim. Angka = hasil hitung otomatis dari dictionary.

### Sheet → form

| Form | Sheet | Payload | Code | Variabel (unik) | Variabel (baris) | PHDT | Selisih baris vs PHDT |
|---|---|---|---|---|---|---|---|
| KPSP | `KPSP` | 14 | 0 | 123 | 141 | 140 | +1 |
| TDD | `TDD New` | 8 | 0 | 37 | 48 | 48 | +0 |
| TDL | `TDL New` | 4 | 8 | 6 | 21 | 21 | +0 |
| KMPE | `KMPE` | 1 | 0 | 14 | 14 | 14 | +0 |
| M-CHAT-R | `M-CHAT` | 1 | 0 | 20 | 20 | 20 | +0 |
| GPPH | `GPPH` | 1 | 40 | 10 | 10 | 10 | +0 |

Variabel unik lebih kecil dari baris karena pertanyaan yang sama muncul di beberapa kelompok umur (KPSP 14 kelompok, TDD 8). Jumlah **baris** cocok dengan PHDT (KPSP +1; lainnya 0). Angka output memakai variabel unik, sama seperti form lain.

Sheet yang **tidak dihitung**: `Tracker` (tabel status, isinya rumus), `TDD Deprecated` dan `TDL Deprecated` (versi lama; PHDT 48 dan 21 cocok dengan versi New), `SDIDTK` (475 baris path **identik** dengan dictionary ePus DDTK yang sudah dihitung, tidak dihitung ulang), `PAUD` (daftar kolom export Dapodik tanpa mapping FHIR), `Copy of DAPODIK` (ada mapping, tapi belum jelas form mana: variabel PDF 75 unik / 87, Excel export 52 unik / 70, tidak cocok dengan PHDT Dapodik PAUD 93 maupun Antropometri DDTK 37), `WB Toolkit` (kosong).

### Asumsi

| # | Asumsi | Status |
|---|---|---|
| EB1 | 1 QuestionnaireResponse per kelompok umur / kuesioner = 1 payload (KPSP 14, TDD 8, KMPE 1, M-CHAT-R 1, GPPH 1) | open |
| EB2 | Jawaban Ya/Tidak (`answer.valueBoolean`) bukan code; hanya opsi `answer.valueCoding` yang dihitung (GPPH 40) | open |
| EB3 | Sheet tidak punya blok Patient/Encounter (hanya reference ke resource dari kunjungan), jadi tidak dihitung di form ini | open |
| EB4 | TDL: 4 Observation (Kartu E 6/60 dan 6/12 × mata kiri/kanan), code SNOMED tajam penglihatan + method (8 code) | open |
| EB5 | TDD dan TDL memakai sheet `New`; `Deprecated` diabaikan | open |
| EB6 | `QuestionnaireResponse.questionnaire` berisi "Tidak Ada" (belum ada canonical Questionnaire), jadi QR tidak punya code pembeda | open |

## Dapodik PAUD (Childhood Development Toolkit, sheet `Copy of DAPODIK`)

Sumber: sheet `Copy of DAPODIK` di `Childhood_Development_Toolkit_Data_Dictionary.xlsx`, diproses `scripts/dapodik_prepare.py` ke `mapping/phdt-data-dictionary-dapodik-paud.csv` (logika sama dengan `epus_prepare.py`).

> **Belum comprehensive review.** Tanpa daftar BQ dan file mentah, belum dibahas dengan tim. Angka = hasil hitung otomatis dari dictionary.

| Form | Sheet | Payload | Code | Variabel (unik) | Variabel (baris) | PHDT | Selisih baris vs PHDT |
|---|---|---|---|---|---|---|---|
| Dapodik PAUD | `Copy of DAPODIK` | 42 | 190 | 75 | 87 | 93 | −6 |

Payload: Observation 32, Condition 4, RelatedPerson 3, Patient 1, Encounter 1, Account 1. Code: Condition.code 55, Observation 135.

| # | Asumsi | Status |
|---|---|---|
| DA1 | Sheet `Copy of DAPODIK` = form Dapodik PAUD (semester), dipilih user karena jumlahnya paling dekat dengan PHDT (93). Sebelumnya baris Dapodik belum dicocokkan | open |
| DA2 | Header kolom A di sheet bertulis "udah selesai semua"; dibaca sebagai kolom Categories | open |
| DA3 | Pemisahan blok payload otomatis (heuristik), belum dicek manual per blok | open |
| DA4 | Selisih −6 baris vs PHDT belum dijelaskan; angka output memakai variabel unik (75) | open |

## 5 CSV PHDT tambahan: SITB TB 01, TB 02, ELSMIL (3 form), SIPTM, ASIK Skrining PTM

Sumber: `PHDT_SITB_-_TB_01.csv`, `PHDT_SITB_-_TB_02.csv`, `PHDT_Data_Dictionary_-_Elsmil.csv`, `PHDT_Data_Dictionary_-_SIPTM.csv`, `PHDT_Data_Dictionary_-_ASIK_PTM.csv`. Diproses `scripts/csvform_prepare.py` ke `mapping/phdt-data-dictionary-<form>.csv` (logika sama dengan `epus_prepare.py`).

> **Belum comprehensive review.** Tanpa daftar BQ dan file mentah, belum dibahas dengan tim. Angka = hasil hitung otomatis dari dictionary.

| Form | Slug | Payload | Code | Variabel (unik) | Variabel (baris) | PHDT | Selisih vs PHDT |
|---|---|---|---|---|---|---|---|
| SITB - TB 01 (Kartu Pengobatan Pasien) | `sitb-tb01` | 37 | 94 | 82 | 88 | 78 | +10 (baris) / +4 (unik) |
| SITB - TB 02 (Kartu Identitas Pasien) | `sitb-tb02` | 13 | 15 | 22 | 22 | 22 | +0 (baris) / +0 (unik) |
| ELSMIL Ibu Hamil | `elsmil-ibu-hamil` | 36 | 104 | 36 | 37 | 37 | +0 (baris) / -1 (unik) |
| ELSMIL Pasca Persalinan | `elsmil-pasca-persalinan` | 24 | 96 | 29 | 29 | 29 | +0 (baris) / +0 (unik) |
| ELSMIL Baduta | `elsmil-baduta` | 31 | 78 | 38 | 45 | 42 | +3 (baris) / -4 (unik) |
| SIPTM | `siptm` | 52 | 214 | 60 | 60 | – (tidak ada) | dihitung dari mapping |
| ASIK - Data Skrining PTM | `asik-skrining-ptm` | 104 | 146 | 67 | 89 | 64 | +25 (baris) / +3 (unik) |

Payload per resource:

- SITB - TB 01 (Kartu Pengobatan Pasien): Observation 25, EpisodeOfCare 2, RelatedPerson 2, MedicationStatement 2, Patient 1, Encounter 1, Condition 1, QuestionnaireResponse 1, CarePlan 1, Procedure 1
- SITB - TB 02 (Kartu Identitas Pasien): MedicationRequest 2, MedicationDispense 2, ServiceRequest 2, Patient 1, Observation 1, Encounter 1, Condition 1, QuestionnaireResponse 1, CarePlan 1, ClinicalImpression 1
- ELSMIL Ibu Hamil: Observation 28, Condition 2, ServiceRequest 2, Patient 1, Encounter 1, Specimen 1, DiagnosticReport 1
- ELSMIL Pasca Persalinan: Observation 22, Patient 1, Condition 1
- ELSMIL Baduta: Observation 29, Patient 1, Immunization 1
- SIPTM: Observation 31, Condition 7, ServiceRequest 3, Goal 3, Procedure 2, Patient 1, Encounter 1, Specimen 1, DiagnosticReport 1, FamilyMemberHistory 1, MedicationRequest 1
- ASIK - Data Skrining PTM: Observation 41, ServiceRequest 20, DiagnosticReport 20, Specimen 14, PractitionerRole 6, Patient 1, Encounter 1, Condition 1

| # | Asumsi / temuan | Status |
|---|---|---|
| CS1 | Satu file Elsmil dipecah 3 form menurut kolom Categories: baris CSV 2–483 = Ibu Hamil, 484–810 = Pasca Persalinan, 811–akhir = Baduta (termasuk sub-bagian berulang, Bayi Baru Lahir 0–28 hari, Baduta >28 hari–23 bulan, Pendampingan Bulanan) | open |
| CS2 | SIPTM belum ada di tracker dan daftar PHDT → ditambahkan sebagai #237 di tracker; jumlah variabel dihitung dari mapping (60 unik), tidak ada angka PHDT | open |
| CS3 | TB 01 dan TB 02 berstatus "Masih diperlukan ❌" di tracker, tetap dihitung karena sudah ada mapping | open |
| CS4 | TB 01: resource `Careplan` (6 baris) diperbaiki otomatis jadi `CarePlan`; 2 blok Organization (faskes asal & faskes) = lookup, tidak dihitung; baris No. Reg TBC.03 / Tahun / No. Urut Kontak tidak punya Resource di dictionary (variabel di luar payload) | open |
| CS5 | TB 02: 5 variabel di luar payload (Organization lookup: Nama UPK, Telp UPK, Provinsi; No. Reg. TBC UPK & Kab/Kota tanpa Resource) | open |
| CS6 | Elsmil Baduta: 4 sel Resource berisi path (mis. `Observation.valueQuantity.value`), diubah otomatis jadi Resource + Path | open |
| CS7 | SIPTM: 1 variabel tanpa Resource (baris 305, "Rujuk RS" curiga tuli kongenital) → di luar payload, perlu dilengkapi | open |
| CS8 | ASIK PTM: 109 baris kosong dibuang; sel Resource berisi path diperbaiki otomatis; PractitionerRole petugas lab (14 blok) dan Organization/Location puskesmas = lookup, tidak dihitung; 6 baris "//Petugas Lab" tetap di luar payload | open |
| CS9 | Pemisahan blok payload otomatis (heuristik), belum dicek manual per blok; blok Condition yang `clinicalStatus`-nya setelah `code` bisa menyatu | open |

- 2026-11-24: Tambah 7 form dari 5 CSV (asumsi CS1–CS9), ⚠️ belum comprehensive review. Sebelumnya TB 01/TB 02/Elsmil/ASIK PTM belum dicocokkan; SIPTM baru.

## ASIK CKG (PHDT_ASIK_CKG.xlsx, banyak versi), Informed Consent, SiHepi Rekap 3e, eKohort ANC / INC

Sumber: `PHDT_ASIK_CKG.xlsx` + 4 CSV PHDT (`IC_1`, `SIHEPI`, `eKohort`, `eKohort_ANC_Final_Format`). Dibuat dengan `scripts/phdt2_prepare.py`. ⚠️ **belum comprehensive review** (tanpa daftar BQ dan file mentah). Hasil (versi yang dipakai; payload / code; variabel unik / baris; PHDT):

| Form | Sumber | Payload / code | Var unik / baris | PHDT | Selisih baris |
|---|---|---|---|---|---|
| ASIK CKG BBL (v2) | sheet `CKG Bayi Baru Lahir 2` | 25 / 41 | 35 / 35 | 33 | +2 |
| ASIK CKG Balita (v2) | sheet `Sheet9` | 32 / 102 | 57 / 58 | 59 | −1 |
| ASIK CKG Dewasa Laki-laki | sheet `CKG Dewasa Laki-laki` | 61 / 202 | 123 / 132 | 132 | 0 |
| ASIK CKG Dewasa Perempuan | sheet `CKG Dewasa Perempuan` | 66 / 223 | 130 / 139 | 132 | +7 |
| ASIK CKG Lansia (27 Apr 2026) | sheet `CKG Lansia 27 April 2026` | 101 / 458 | 188 / 204 | 180 | +24 |
| Informed Consent | `IC_1` | 3 / 8 | 27 / 28 | 28 | 0 |
| SiHepi Rekap 3e | `SIHEPI` | 65 / 118 | 93 / 115 | 115 | 0 |
| eKohort ANC (Final Format) | `eKohort_ANC_Final_Format` | 43 / 78 | 34 / 34 | 36 | −2 |
| eKohort INC (Bersalin) | `eKohort`, baris 726–akhir | 58 / 74 | 84 / 85 | 85 | 0 |

Versi lain (tidak masuk total, output per form tersedia): BBL v1 25 / 56, Balita v1 29 / 99, Lansia 2026 82 / 366, Lansia 2025 80 / 361, eKohort ANC lama 140 / 247 (190 variabel). Tabel perbandingan versi: `output.md` bagian "Versi ASIK CKG".

**Asumsi**
- CK1: untuk form yang punya beberapa versi, versi terbaru dipakai di total konsolidasi (BBL v2, Balita v2, Lansia 27 April 2026); versi lain dihitung terpisah.
- CK2: `Sheet9` = Balita versi 2 (tarikan baru). Dasarnya nama kolom raw (`Nama Lengkap`, `NIK`) sama dengan BBL v2 dan sheet `Hasil Check Tarikan Baru dan Lama`, contoh data `individu-bayi-2025-08.xlsx`. **Perlu konfirmasi user.**
- CK3: di sheet CKG, baris QuestionnaireResponse berselang-seling dengan blok Observation. Jumlah QR dihitung dari jumlah baris `QuestionnaireResponse.questionnaire` (konfirmasi user 2026-11-24: sebagian form punya QR terpisah): BBL 0 (tanpa QR), Balita 1, Dewasa Laki-laki 1, Dewasa Perempuan 1 (= 1 payload), **Lansia 27 April 2026 = 7, Lansia 2026 = 4, Lansia 2025 = 4**. Tanpa aturan ini hasil heuristik membengkak (Lansia 174, Dewasa Laki-laki 109).
- CK4: baris "Contoh Data: ..." dan baris angka di ujung sheet (jumlah variabel, mis. 35, 58) dibuang. Di sheet Dewasa/Lansia kolom `Nama Column Raw` berisi nomor urut, jadi tidak dipakai; variabel = kolom `Variables` (nama variabel lama), bukan `Variabel v2`/`v2025`/`v2026`/`v27April2026`.
- CK5: sheet `CKG Lansia (tidak dipakai)`, `Pivot Table 1`, `All Variable`, `All Variable v2`, `Detail1-Lansia`, `variabel ckg dewasa`, `Hasil Check Tarikan Baru dan Lama`, `lansia` bukan dictionary, tidak dihitung. Klaster Remaja (#45) tidak ada mapping, dilewati.
- IC1: Informed Consent: Patient, Consent, RelatedPerson (hanya kalau `status_responden` = wali responden) = 3 payload. Kode klausul `Consent.provision.provision[n].code.coding` (SP000840–SP000847) dihitung sebagai code (8). Ditambah ke `COUNT_PATHS` di `epus_prepare.py`. Category/scope/status/type Consent (HL7) tidak dihitung. `faskes_id` pada form ini pakai ID database berbeda dengan ID Organization SatuSehat (lookup).
- EK1: eKohort ANC memakai file `Final Format` (34 variabel, mendekati PHDT 36). Bagian ANC di file `eKohort` lama (baris 2–725) dihitung terpisah sebagai versi lama (190 variabel, 140 payload, 247 code), tidak masuk total. eKohort INC hanya ada di file `eKohort` (baris 726–akhir). Baris 725 (sel `#NAME?`) ikut ANC lama.
- EK2: 14 baris di `eKohort_ANC_Final_Format` (baris sumber 572–586, blok ServiceRequest Hepb + PractitionerRole lab) kehilangan 2 kolom (Definisi Operasional dan Agregat/Individu), sehingga Resource bergeser ke kolom Value Name. Digeser otomatis di skrip (tanpa mengubah file asli). Tanpa ini ANC terhitung 51 payload dengan "resource" palsu (`active`, `routine`, `75410-1`, dst.).
- SH1: SiHepi: 93 variabel unik / 115 baris (nama yang sama muncul di beberapa blok); PractitionerRole lab (3) = lookup, tidak dihitung.

**Temuan terbuka (belum ditanyakan ke tim)**
- CK-1: **Lansia 27 April 2026 belum punya blok lab** (ServiceRequest, Specimen, DiagnosticReport, PractitionerRole) yang ada di Lansia 2025 dan 2026. Konfirmasi user 2026-11-24: **terlewat**, belum dimapping. Payload/code Lansia akan naik setelah blok lab ditambahkan.
- CK-2: `interpretasi_kolesterol_total` (baris 603 di Dewasa Laki-laki dan Perempuan) tanpa Resource/Path.
- CK-3: BBL v2 baris 342 dan 374 (Tanggal Pemeriksaan Skrining Kelainan Saluran Empedu 14–28 hari / 2–4 bulan) tanpa mapping. `Kode Faskes` (BBL dan Balita, baris akhir) tanpa mapping.
- CK-4: Di semua sheet CKG, 1 baris `Organization.address.extension` dengan Resource `Location` (baris 58–70 tergantung sheet): Resource/Path tidak cocok. Organization/Location = lookup (tidak dihitung).
- IC-1: Informed Consent: `is_teen` (Tidak dimapping), `kecamatan` (tidak dimapping), `status_responden` (kontrol pembuatan RelatedPerson, tanpa resource sendiri) tidak masuk payload.
- EK-1: eKohort ANC Final: baris 368–369 punya Resource `Procedure` tetapi path `Observation.performer.actor...` (salah resource atau path); baris 466 `Reduksi Guladarah` tanpa Resource; `nama_lembaga` dipetakan ke Organization / Location (lookup).
- EK-2: eKohort INC variabel tanpa Resource: Fasilitas Kesehatan, Keadaan, Keadaan Jam, Pelayanan (baris 82–85), Integrasi Arv, Integrasi Anti Malaria, Integrasi Anti Tb, D, T, U (102–107), Status Pindahan (265).
- EK-3: eKohort ANC lama: typo Resource `Practioner` (diperbaiki otomatis jadi `Practitioner`).
- SH-1: SiHepi baris 907: variabel `Keterangan` dengan BQ `TRUE` (kemungkinan sisa sel), tanpa Resource.

**Catatan pipeline**: Consent baru (`Consent`, klausul SP000840–SP000847) perlu ditambahkan di converter. `FamilyMemberHistory`/`Consent` belum ada di form lain. Versi CKG: ingestion perlu tahu versi tarikan (nama kolom raw berubah antar versi).

---
## SiGizi (PHDT_SIGIZI.xlsx): 17 form Balita, PMT 2024/2025, Ibu Nifas, Kohort Ibu

Sumber: `PHDT_SIGIZI.xlsx` (sheet "Copy of ...", sama dengan sumber SiGizi ANC) + schema BQ dari user (`bq_schema.xlsx`, kolom raw header + field name). Diproses `scripts/sigizi_prepare.py` ke `mapping/phdt-data-dictionary-sigizi-<form>.csv` (logika blok/payload sama dengan `epus_prepare.py`). File asli tidak di-commit. SiGizi ANC tidak diulang. Daftar Balita dan Daftar Bumil **ditunda** (draft mapping belum dimasukkan, menunggu keputusan user).

> ⚠️ **Belum comprehensive review.** Sudah ada daftar BQ (tally dicek), belum ada file mentah dan belum dibahas dengan tim. Pemisahan blok payload otomatis (heuristik).

| Form | Slug | Sheet / baris Excel | Tabel BQ | Kolom BQ | BQ cocok | Variabel raw | Payload | Code |
|---|---|---|---|---|---|---|---|---|
| SiGizi Balita BNBA | `balita-bnba` | `Copy of SiGizi_Balita` 2-538 | `balita bnba` | 35 | 35 | 33 | 24 | 48 |
| SiGizi Balita Vitamin A | `balita-vitamin-a` | `Copy of Sigizi Balita Vitamin A` 2-akhir | `vitamin a` | 34 | 34 | 14 | 22 | 47 |
| SiGizi Balita Mendapat PMT 2024 | `balita-mendapat-pmt-2024` | `Copy of SiGizi_Balita` 539-887 | `mendapat pmt 2024` | 30 | 30 | 30 | 15 | 44 |
| SiGizi Balita Pemantauan PMT 2024 | `balita-pemantauan-pmt-2024` | `Copy of SiGizi_Balita` 888-1142 | `pemantauan pmt 2024` | 18 | 18 | 18 | 9 | 12 |
| SiGizi Balita ASI Eksklusif | `balita-asi-eksklusif` | `Copy of Sigizi Balita ASI Ekskl` 2-akhir | `asi eksklusif` | 22 | 22 | 22 | 11 | 36 |
| SiGizi Balita MPASI | `balita-mpasi` | `Copy of Sigizi Balita MPASI` 2-akhir | `mpasi` | 28 | 27 | 28 | 9 | 30 |
| SiGizi PMT 2025 BB Tidak Naik - Pantau | `pmt2025-bb-tidak-naik-pantau` | `Copy of SiGizi_PMT_2025` 2-347 | `bb tidak naik pantau pmt 2025` | 24 | 24 | 24 | 15 | 32 |
| SiGizi PMT 2025 BB Tidak Naik - Riwayat | `pmt2025-bb-tidak-naik-riwayat` | `Copy of SiGizi_PMT_2025` 1568-2013 | `bb tidak naik riwayat pmt 2025` | 34 | 34 | 34 | 19 | 74 |
| SiGizi PMT 2025 BB Tidak Naik - Survey | `pmt2025-bb-tidak-naik-survey` | `Copy of SiGizi_PMT_2025` 2014-akhir | `bb tidak naik survey pmt 2025` | 20 | 20 | 20 | 5 | 16 |
| SiGizi PMT 2025 BB Kurang - Pantau | `pmt2025-bb-kurang-pantau` | `Copy of SiGizi_PMT_2025` 348-786 | `bb kurang pantau pmt 2025` | 24 | 24 | 24 | 21 | 46 |
| SiGizi PMT 2025 BB Kurang - Riwayat | `pmt2025-bb-kurang-riwayat` | `Copy of SiGizi_PMT_2025` 1568-2013 | `bb kurang riwayat pmt 2025` | 34 | 34 | 34 | 19 | 74 |
| SiGizi PMT 2025 BB Kurang - Survey | `pmt2025-bb-kurang-survey` | `Copy of SiGizi_PMT_2025` 2014-akhir | `bb kurang survey pmt 2025` | 20 | 20 | 20 | 5 | 16 |
| SiGizi PMT 2025 Gizi Kurang - Pantau | `pmt2025-gizi-kurang-pantau` | `Copy of SiGizi_PMT_2025` 787-1567 | `gizi kurang pantau pmt 2025` | 51 | 51 | 51 | 42 | 101 |
| SiGizi PMT 2025 Gizi Kurang - Riwayat | `pmt2025-gizi-kurang-riwayat` | `Copy of SiGizi_PMT_2025` 1568-2013 | `gizi kurang riwayat pmt 2025` | 34 | 34 | 34 | 19 | 74 |
| SiGizi PMT 2025 Gizi Kurang - Survey | `pmt2025-gizi-kurang-survey` | `Copy of SiGizi_PMT_2025` 2014-akhir | `gizi kurang survey pmt 2025` | 20 | 20 | 20 | 5 | 16 |
| SiGizi Ibu Nifas | `ibu-nifas` | `Copy of SiGizi Nifas` 2-akhir | `ibu nifas` | 14 | 14 | 14 | 11 | 12 |
| SiGizi Kohort Ibu | `kohort-ibu` | `Copy of SiGizi Kohort Ibu` 2-akhir | `kohort ibu` | 42 | 42 | 42 | 63 | 94 |

Kolom BQ = field di schema tanpa metadata pipeline (`puskesmas_name/_id`, `file_*`, `uuid`, `hash_code`, `sheet_name`, `ingestion_timestamp`), tanpa `no` (data lokal, keputusan user R2), dan tanpa kolom di SG3. Variabel raw = kolom yang punya raw header di schema (PMT 2025 tidak punya raw header → jumlah kolom BQ).

Payload per resource:

- SiGizi Balita BNBA: Observation 14, MedicationRequest 2, MedicationDispense 2, Patient 1, RelatedPerson 1, Encounter 1, Condition 1, Procedure 1, QuestionnaireResponse 1
- SiGizi Balita Vitamin A: Observation 13, MedicationRequest 2, MedicationDispense 2, Patient 1, RelatedPerson 1, Encounter 1, Condition 1, Procedure 1
- SiGizi Balita Mendapat PMT 2024: Observation 12, Patient 1, Encounter 1, Condition 1
- SiGizi Balita Pemantauan PMT 2024: Observation 6, Patient 1, Encounter 1, Condition 1
- SiGizi Balita ASI Eksklusif: Observation 7, Patient 1, RelatedPerson 1, Encounter 1, Condition 1
- SiGizi Balita MPASI: Observation 6, Patient 1, Encounter 1, Condition 1
- SiGizi PMT 2025 BB Tidak Naik - Pantau: Observation 12, Patient 1, Encounter 1, Condition 1
- SiGizi PMT 2025 BB Tidak Naik - Riwayat: Observation 16, Patient 1, Encounter 1, Condition 1
- SiGizi PMT 2025 BB Tidak Naik - Survey: Patient 1, Encounter 1, Condition 1, Observation 1, QuestionnaireResponse 1
- SiGizi PMT 2025 BB Kurang - Pantau: Observation 18, Patient 1, Encounter 1, Condition 1
- SiGizi PMT 2025 BB Kurang - Riwayat: Observation 16, Patient 1, Encounter 1, Condition 1
- SiGizi PMT 2025 BB Kurang - Survey: Patient 1, Encounter 1, Condition 1, Observation 1, QuestionnaireResponse 1
- SiGizi PMT 2025 Gizi Kurang - Pantau: Observation 39, Patient 1, Encounter 1, Condition 1
- SiGizi PMT 2025 Gizi Kurang - Riwayat: Observation 16, Patient 1, Encounter 1, Condition 1
- SiGizi PMT 2025 Gizi Kurang - Survey: Patient 1, Encounter 1, Condition 1, Observation 1, QuestionnaireResponse 1
- SiGizi Ibu Nifas: Observation 3, Procedure 3, EpisodeOfCare 2, Patient 1, Encounter 1, Condition 1
- SiGizi Kohort Ibu: Observation 17, Condition 15, Encounter 14, ServiceRequest 3, Specimen 3, DiagnosticReport 3, EpisodeOfCare 2, Immunization 2, Patient 1, RelatedPerson 1, PractitionerRole 1, Procedure 1

| # | Asumsi / temuan | Status |
|---|---|---|
| SG1 | Potongan sheet per form: `Copy of SiGizi_Balita` 2–538 BNBA, 539–887 Mendapat PMT 2024, 888–1142 Pemantauan PMT 2024; `Copy of SiGizi_PMT_2025` 2–347 Pantau BB Tidak Naik, 348–786 Pantau BB Kurang, 787–1567 Pantau Gizi Kurang, 1568–2013 Riwayat, 2014–akhir Survey. PMT 2025 = **9 form** (keputusan user R1): Riwayat dan Survey memakai dictionary yang sama untuk 3 kategori | open |
| SG2 | Nama Column BQ diisi otomatis dari schema: cocokkan field name dulu, lalu raw header (berdasarkan nama, bukan posisi). Semua kolom BQ cocok **kecuali MPASI `pengukuran`** (kolom export, belum ada di dictionary) | open |
| SG3 | Kolom BQ **tanpa raw header** yang tidak dimapping: `desakelurahan`, `jumlah_anak_diberi_vit_a` (Vitamin A), `jumlah_anak_asi_eksklusif` (ASI) = rekap agregat per desa yang ikut tercampur ke tabel individu; `zs_tbu_awal` (Mendapat PMT 2024), `zs_tbu_converted` (Pemantauan PMT 2024) = kolom turunan pipeline | open |
| SG4 | Schema `pemantauan pmt 2024`: raw header mulai "Tinggi Badan (cm) Awal" **bergeser 1 baris** terhadap field name (mis. raw "Tinggi Badan (cm) Awal" tertulis di field `status_pertumbuhan`). Pencocokan pakai field name saja; `tinggi_badan_cm_awal` tetap dianggap kolom file mentah | open (cek schema) |
| SG5 | Vitamin A: dictionary = salinan BNBA (format export lama, 34 kolom BQ termasuk berat, tinggi, BB/U, KPSP, KIA, `jml_vit_a`); raw header export sekarang hanya 14 kolom. Ditambahkan: blok RelatedPerson **Nama Ortu** (+1 payload, pola BNBA) dan baris **Tanggal Pemberian** (`Procedure.performedPeriod.start`, dipakai juga untuk tanggal lain kalau `Tanggal Pengukuran` kosong). Angka PHDT 32 mendekati format lama | open (konfirmasi) |
| SG6 | `puskesmas` / `posyandu`: di sheet dipasang ke `Organization.name` (master data). Dipindah ke `Encounter.serviceProvider.reference` / `Encounter.location.reference` dengan keterangan lookup (aturan.md). Blok Organization/Location tetap di dictionary tapi tidak dihitung, label variabelnya dipindah ke Keterangan. Header file export Vitamin A & ASI memang "Pukesmas" (typo asli) | done (otomatis) |
| SG7 | `detail` (5 form: BNBA, Vitamin A, Mendapat PMT 2024, ASI, MPASI) → `Encounter.extension` url `http://terminology.kemkes.go.id/sp/sigizi-detail`, `valueString` (keputusan user). Tidak menambah payload/code | done |
| SG8 | `tindakan` tanpa mapping di Pemantauan PMT 2024 dan 9 form PMT 2025 → **asumsi** pola sama dengan Detail: `Encounter.extension` `sigizi-tindakan` `valueString`. Ibu Nifas sudah punya mapping Tindakan (Procedure SP000683 Tatalaksana Tindakan) dan dibiarkan | open (konfirmasi) |
| SG9 | Kohort Ibu: kunjungan bulanan Januari–Desember (kolom `tahun_<bulan>`) dan kunjungan persalinan = **14 Encounter** dihitung masing-masing (+13 payload), sama seperti 13 Condition 134435003 per kunjungan. EpisodeOfCare ANC muncul 2x (dibuat + diperbarui saat persalinan) | open |
| SG10 | Baris bergeser 1 kolom ke kiri (Resource di kolom Agregat/Individu, Path di kolom Resource): 52 baris Kohort Ibu (blok lab Hb/protein urin/gula darah) dan 13 baris Pantau Gizi Kurang 2025 → dikembalikan otomatis | done (otomatis) |
| SG11 | Perbaikan path otomatis: `Patient.line` → `Patient.address.line` (Vitamin A, Nifas, Kohort); `Organization.address...` di blok Location → `Location.address...`; `ServiceRequest.code` / `Specimen.type` tanpa `.coding` → `.coding` (Kohort) | done (otomatis) |
| SG12 | BNBA & Vitamin A: MedicationDispense Vitamin A 200.000 IU dan 100.000 IU memakai KFA **93018284** yang sama (MedicationRequest beda: 92000809 / 92000354). Kemungkinan salah salin | open |
| SG13 | Pantau BB Tidak Naik (15 payload) dan Pantau BB Kurang (21 payload) punya 24 kolom BQ yang sama, tapi jumlah blok pemantauan di sheet beda (BB/U, berat, naik BB berulang 3x vs 5x). Perlu dicek apakah jumlah pemantauan memang beda per kategori | open |
| SG14 | BNBA: `kelas_ibu_balita` dan `mbg` ada di dictionary dan BQ tapi tidak punya raw header di schema (kolom baru di export?). Ibu Nifas: PHDT 57 variabel vs 14 kolom BQ (selisih −43, penyebab belum diketahui). Vitamin A: PHDT 32 vs raw 14 (lihat SG5) | open |

- 2026-11-24: Tambah 17 form SiGizi (asumsi/temuan SG1–SG14, catatan pipeline P39–P43), ⚠️ belum comprehensive review. Total 314 payload / 772 code.

## SISMAL (PHDT_SISMAL.xlsx): Regmal 1, Validasi Kasus Indigenous

Sumber: `PHDT_SISMAL.xlsx` (sheet `Mapping Regmal 1`, `Mapping Indigeneous`). ⚠️ belum comprehensive review (tanpa daftar BQ dan file mentah). Dictionary dibuat otomatis dengan `scripts/sismal_prepare.py`.

### Hasil hitung

| Form | Variabel | Payload | Code | Code SP |
|---|---|---|---|---|
| SISMAL Regmal 1 | 49 | 20 | 54 | 14 |
| SISMAL Validasi Indigenous | 14 | 7 | 12 | 6 |

Regmal 1: Observation 14, Patient 1, PractitionerRole 1, Practitioner 1, Encounter 1, Condition 1, ServiceRequest 1. Indigenous: Observation 2, Patient, Encounter, Condition, Location, Procedure masing-masing 1.

### Sheet → form

| Sheet | Status |
|---|---|
| Mapping Regmal 1 | dihitung |
| Mapping Indigeneous | dihitung |
| Verifikasi Uji Silang | **tidak dihitung**: isinya salinan template TB-TPT (bukan form malaria), perlu dikirim ulang oleh tim |
| Sheet laporan lain (Rekap dst.) | bukan form input per pasien, tidak dihitung |

### Asumsi yang diambil

| No | Asumsi | Status |
|---|---|---|
| SM1 | Organization (faskes) = lookup master data, tidak dihitung (sesuai aturan) | perlu konfirmasi |
| SM2 | Location "Alamat Asal Penularan" di Indigenous dibuat dari isian form, jadi dihitung | perlu konfirmasi |
| SM3 | Opsi `valueCodeableConcept` dihitung sebagai code (54 code Regmal 1) | sesuai aturan |
| SM4 | Baris Observation yang hanya tipe data (`number`, `string`, `date`) di kolom Variables dipindah ke kolom Data Type | done |

### Perbaikan otomatis pada file

| Perbaikan | Jumlah |
|---|---|
| Path `valuecodeableConcept` → `valueCodeableConcept` | 31 |
| Path `valueinteger` → `valueInteger` | 1 |
| Code `ofiicial` → `official`, `social history` → `social-history` | 1 + 1 |
| `Organization.*` di blok Location → `Location.*` | 1 blok |
| Blok ServiceRequest yang kolomnya bergeser 1 kolom dirapikan (`unshift`) | 19 baris |
| Sisa tipe data di kolom Variables dibersihkan | 5 |

### Temuan

| No | Temuan | Status |
|---|---|---|
| SM-1 | Regmal 1 punya 88 variabel di laporan, tapi hanya 49 ada di dictionary (sisanya `parkir` / `tidak dimapping` di sheet Variable Regmal 1) | open |
| SM-2 | `Condition.code` di Regmal 1 kosong (jenis malaria tidak punya code penentu); Knowlesi belum dimapping | open |
| SM-3 | Status Validasi (Indigenous) belum punya path FHIR | open |
| SM-4 | `Location.type` di Indigenous: code belum pasti | open |
| SM-5 | Verifikasi Uji Silang belum ada mapping malaria | open |

## Perbandingan jumlah variabel dengan PHDT Data Dictionary (2026-11-24)

Sumber angka pembanding: [`referensi-variabel-phdt.md`](referensi-variabel-phdt.md). Hasil: 5 form cocok, 4 form beda, Raffle tidak ada di daftar PHDT.

| Form | Variabel raw | PHDT | Selisih | Penyebab | Status |
|---|---|---|---|---|---|
| SiGizi ANC | 49 | 45 | +4 | belum diketahui | open |
| SITB TB 06 | 96 | 69 | +27 | dugaan: banyak kolom SITB yang sebelumnya di-skip di PHDT (belum dicek per kolom) | angka output utama dipakai |
| SITB TB 03 SO | 84 | 75 | +9 | dugaan sama dengan TB 06 | angka output utama dipakai |
| SITB TB 16K | 40 | 24 | +16 | dugaan sama dengan TB 06 | angka output utama dipakai |

Maternal Outcome, SITB TB 03 RO, SITB TB 04, MPDN Kematian Bayi, dan MPDN Kematian Ibu cocok (selisih 0).

## Catatan pipeline (perlu update)

Perubahan di dictionary yang harus diikuti di pipeline (ingestion BQ / FHIR converter).

| # | Form | Perubahan | Yang perlu di-update | Status |
|---|---|---|---|---|
| P1 | Raffle | Kolom BQ baru `input_data` → Observation 385438008 Source of information, value SP000776 Sigizi / SP000777 E-pus PKD / SP000778 E-pus | Ingestion: tambah kolom `input_data`. Converter: buat Observation dari kolom ini | open |
| P2 | Raffle | `nama_data_entry` → `Encounter.participant` type ADM admitter, `individual.display`, **dan** Practitioner baru (`Practitioner.name.text`) | Converter: buat 2 Practitioner (bidan desa + data entry) | open |
| P3 | Raffle | Location dibuat dari form (`lokasi_faskes`, `kecamatan`, `kelurahan`), bukan lookup | Converter | open |
| P4 | Raffle | Condition.code SP000776 → **SP001135** Presensi Posyandu | Converter | open |
| P5 | Raffle | Encounter.class display "field"; participant ATND reference ke Practitioner (bidan desa) | Converter | open |
| P6 | Maternal Outcome | `data_entry_clerk_staff_id` (isinya nama) juga dipakai untuk `Encounter.participant` ADM `individual.display` | Converter | open |
| P8 | Maternal Outcome, Raffle | `puskesmas_name` / `puskesmas` → lookup Organization di master data berdasarkan nama, lalu isi `Encounter.serviceProvider.reference`. Raffle: Organization yang sama dipakai untuk `Location.managingOrganization` dan `EpisodeOfCare.managingOrganization` | Converter | open |
| P10 | Raffle | `lokasi_faskes` → `Location.name`. `Encounter.participant` ADM dan `Observation.performer` → reference ke Practitioner data entry | Converter | open |
| P11 | Maternal Outcome | Observation meninggal: `focus` dihapus, diganti `encounter.reference`. Keadaan Ibu category `survey`. PractitionerRole.practitioner → Practitioner data entry. EpisodeOfCare ANC/PNC: cari episode aktif pasien lalu ubah ke finished, isi `patient.reference` | Converter | open |
| P9 | Maternal Outcome | Organization & Location tidak dibuat lagi: lookup master data untuk `Encounter.serviceProvider` dan `Encounter.location` | Converter | open |
| P7 | Maternal Outcome | Practitioner.identifier pakai system nik (use / system / value), `nakes-his-number` dihapus | Converter | open |
| P12 | SiGizi ANC | IMT Sebelum Hamil: 9 dari 57 nilai di file Padamara sudah berubah jadi tanggal oleh Excel (mis. 21.9 → 21-09-2026) | Ingestion: baca kolom sebagai teks, tandai nilai bertipe tanggal sebagai error | open |
| P13 | SiGizi ANC | Label pilihan beda huruf besar/kecil & spasi (`positif`/`Positif`, `SpOG`, `Normal < 200`). `-`, `--Pilih--` (Rhesus, 12 baris), dan kosong = tidak diisi | Converter: cocokkan Value Name tanpa beda huruf/spasi; `-`/`--Pilih--`/kosong → tidak buat resource | open |
| P14 | SiGizi ANC | Prov/Kab/Kec/Desa domisili berisi **nama** (mis. JAWA TENGAH), sedangkan `valueCode` butuh kode Kemendagri | Converter: lookup nama → kode wilayah | open |
| P15 | SiGizi ANC | Usia kehamilan (teks "24 Minggu") → Observation 18185-9, valueQuantity satuan `wk` | Ingestion: kolom `pemeriksaan_anc_usia_kehamilan`. Converter: ambil angkanya, buat Observation | open |
| P17 | SiGizi ANC | Urutan kolom Excel: NIK (B) sebelum Nama (C), beda dengan urutan BQ | Ingestion: petakan berdasarkan nama header, bukan posisi | open |
| P18 | SiGizi ANC | `faskes_yang_melayani_anc` dan `posyandu_domisili` berupa string → cocokkan ke master data Organization/Location (posyandu: + desa + puskesmas domisili). Blok Organization/Location tidak dibuat | Converter: fungsi pencocokan string (normalisasi huruf, spasi, singkatan "PKM"/"Puskesmas") + daftar yang tidak cocok untuk dicek manual | open |
| P19 | SiGizi ANC | PractitionerRole petugas lab tidak dibuat; performer lab = PractitionerRole default lab milik Organization faskes (master data) | Converter + master data (setiap faskes perlu PractitionerRole default lab) | open |
| P20 | SiGizi ANC | Lab "Tidak Diperiksa"/`-`/kosong → hanya Observation dataAbsentReason, tanpa ServiceRequest/Specimen/DiagnosticReport. TTD/MMS = 0 → MedicationRequest/Dispense tidak dibuat | Converter | open |
| P21 | SiGizi ANC | Encounter.class diturunkan dari faskes: faskes → AMB, luar faskes (posyandu) → FLD, "Kunjungan rumah" → HH | Converter | open |
| P22 | SiGizi ANC | Kolom `pemeriksaan_anc_aksi` → `Encounter.extension` url `http://terminology.kemkes.go.id/sp/sigizi-aksi` (valueUrl) | Ingestion: pastikan link ikut terambil (di export Padamara kosong). Converter: cek apakah SatuSehat menerima extension ini; kalau tidak, buang sebelum kirim ke SatuSehat | open |
| P23 | SiGizi ANC | Hb Anemia Berat → OI000034; DiagnosticReport HIV/Hepatitis/Sifilis category SR; EpisodeOfCare ANC dicari dulu (active) sebelum buat baru | Converter | open |
| P16 | SiGizi ANC | Pilihan TD di form sumber `Normal (<= 140)` dan `Hipertensi (>= 140)` sama-sama memuat 140 | Info ke pemilik form SiGizi | open |
| P24 | SITB (semua) | Isi export memakai singkatan/format lain dari Value Name: `D/ND/RD/RND/IDT`, `S/R/I`, `L/P`, `Neg/Pos`, `ODHIV/Bukan ODHIV`, `Ya/Tidak` vs `positif/negatif`, centang `V`, `Fasyankes: <nama faskes>` (Dirujuk/dikirim oleh), singkatan paduan pengobatan (`Bdq Lzd Mfx Pa` → CP000086, `Lfx RHZE` → CP000084) | Converter: tabel normalisasi nilai → Value Name; `Fasyankes: <nama>` → opsi Fasyankes + lookup Organization asal | open |
| P25 | TB 06, TB 04 | (dibatalkan) Kolom AC TB 06 adalah tambahan user; TB 04 DJ–DL tidak ada di format baru | – | ditutup |
| P26 | TB 03 SO | Pekerjaan `Lain-lain:<teks>` | Converter: pecah jadi opsi Lain-lain + teks | open |
| P27 | TB 03 RO | Follow up BTA & Biakan bulan ke-1 s.d. 24 (54 kolom) memakai 1 template Observation | Converter: buat 1 Observation BTA dan/atau Biakan per bulan yang terisi | open |
| P28 | SITB (semua) | Faskes pelapor: TB 06, TB 03 SO, TB 03 RO → cari Organization di master data (Kode Fasyankes), kalau match **update** Organization + Location dari form. TB 04 → lookup dari metadata `puskesmas_id`/`puskesmas_name`. TB 16K → lookup. Practitioner PJ SITB & PractitionerRole default lab tetap lookup master data | Converter + master data | open |
| P29 | TB 16K | Kolom centang `V` (Kontak serumah/erat, Memenuhi syarat rujukan eligibilitas) dan TPT `< 5 th` / `≥ 5 th` | Converter: `V` = pilih opsi itu; ambil kolom TPT yang terisi | open |
| P30 | TB 03 SO, TB 03 RO | `EpisodeOfCare.type` tetap per register (SO = TB-SO, RO = TB-RO) | Converter | open |
| P31 | TB 03 SO | `status_pengobatan` (Sesuai standar / Tidak sesuai standar) → `CarePlan.activity.detail.description` di CarePlan Pengobatan (sementara, teks) | Converter | open |
| P32 | TB 16K | Nama kader → `Observation.valueString` (Observation SP000373), organisasi kader → lookup Organization di `Observation.performer.reference`. Practitioner/PractitionerRole kader tidak dibuat | Converter | open |
| P33 | TB 06, TB 03 SO, TB 03 RO | Code lokal baru: SP001136 Belum Mulai Pengobatan (TB 06 Tindak Lanjut); SP001137 Paduan lainnya (TB 03 SO & RO, menggantikan SP001137–SP001140 versi awal). Hasil Tes HIV "Tidak Diketahui" → dataAbsentReason unknown | Converter + daftar local code | open |
| P34 | TB 03 SO, TB 03 RO | Paduan pengobatan: cocokkan teks ke Value Name tanpa beda huruf besar/kecil (termasuk baris alias); tidak cocok → SP001137 Paduan lainnya; nilai salah input (mis. `(40)`, `-41`) → tidak dibuat. `productCodeableConcept.text` selalu diisi teks asli | Converter | open |
| P35 | TB 03 RO | Pemeriksaan lab sekarang ServiceRequest + Specimen + Observation + DiagnosticReport (7 pemeriksaan, 2 di antaranya template follow up per bulan). Tanggal permintaan/pengambilan tidak ada di export (kecuali Uji Kepekaan) → pakai tanggal hasil. Path `Specimen.collectedDateTime` diperbaiki jadi `Specimen.collection.collectedDateTime` (TB 03 SO & RO) | Converter | open |
| P36 | MPDN Bayi, Ibu | Dua form baru tanpa Encounter: Patient (Bayi: ibu + bayi, nama bayi = `By Ny {Nama Ibu Hamil}`), Observation (Bayi 16, Ibu 7), Condition (Ibu), dan 1 Composition per laporan dengan `contained` Location (tipe lahir/meninggal) | Ingestion: tabel `mpdn_laporan_kematian_bayi` / `_ibu`. Converter: buat bundle Composition + Observation + Patient. **Daftar kolom BQ belum dicek** | open |
| P37 | MPDN Bayi | Urutan pasien tergantung lahir mati / hidup: lahir mati → pasien 1 = ibu, pasien 2 = anak; lahir hidup → pasien 1 = bayi, pasien 2 = ibu (`subject` / `focus`, baris 41–43 dictionary asli). `Composition.type`: COM000002 (lahir mati) / COM000003 (lahir hidup) | Converter: logika pasien 1/2 dan `Composition.type` | open |
| P38 | MPDN Bayi, Ibu | Dugaan sebab kematian = component kode group / subgroup / detail dari daftar ICD-PM (Bayi) dan ICD-MM (Ibu). Practitioner PJ MPDN = lookup (MA8) | Converter: pemetaan ICD-PM / ICD-MM ke code. Master data Practitioner PJ MPDN | open |
| P39 | SiGizi Balita (BNBA, Vitamin A, Mendapat PMT 2024, ASI, MPASI) | Kolom `detail` → `Encounter.extension` `http://terminology.kemkes.go.id/sp/sigizi-detail` (`valueString`). `tindakan` (Pemantauan PMT 2024, PMT 2025 ×9) → `Encounter.extension` `sigizi-tindakan` (`valueString`, asumsi SG8) | Converter | open |
| P40 | SiGizi Vitamin A, ASI, PMT 2024, Daftar Balita | Tabel BQ tercampur: kolom rekap agregat (`desakelurahan`, `jumlah_anak_*`), kolom format export lama (Vitamin A: berat, tinggi, BB/U, KPSP, KIA), kolom MPASI di `sigizi_daftar_balita`, kolom turunan `zs_tbu_awal` / `zs_tbu_converted` | Ingestion: pisahkan sheet rekap dari sheet individu; catat versi format export | open |
| P41 | SiGizi (17 form) | `puskesmas` / `pukesmas` → lookup `Encounter.serviceProvider.reference`; `posyandu` → lookup `Encounter.location.reference` (bukan Organization baru) | Converter: lookup master data Organization/Location | open |
| P42 | SiGizi Vitamin A | Kolom export baru `nama_ortu` → RelatedPerson (PRN); `tanggal_pemberian` → `Procedure.performedPeriod.start` dan fallback tanggal Encounter / MedicationDispense kalau `tanggal_pengukuran` kosong | Converter | open |
| P43 | SiGizi Kohort Ibu | 14 Encounter per pasien (12 kunjungan bulanan dari kolom `tahun_<bulan>` + 1 kunjungan utama + 1 persalinan), masing-masing dengan Condition sendiri; Encounter hanya dibuat kalau tanggal bulan itu terisi | Converter | open |
| P44 | SISMAL Regmal 1, Validasi Indigenous | Kolom `Variables` kadang berisi tipe data (`number`/`string`/`date`) bukan nama variabel; ServiceRequest Regmal 1 kolomnya bergeser 1 kolom (sudah dirapikan). Path salah ketik (`valuecodeableConcept`, `valueinteger`) sudah dibetulkan di CSV | Converter: pakai CSV hasil perbaikan, bukan sheet asli |
| P45 | SISMAL Indigenous | Location "Alamat Asal Penularan" dibuat dari form (bukan lookup), `Location.type.coding` menjadi penentu | Converter: buat Location baru; kode `Location.type` menunggu SM-4 |

## SIM RS (PHDT_Data_Rumah_Sakit.xlsx)

⚠️ belum comprehensive review (tanpa daftar BQ dan file mentah). Tiap sheet mapping = 1 form tracker (#128–#236). Variabel = kolom `Variables`; header kolom berbeda-beda antar sheet (ada `API SIMRS Name`, `Logic`, atau tanpa `Nama Column Raw`), dibaca per nama kolom.

**Asumsi**
- RS1: `Mapping INC BBL Tripat` dipakai sebagai BBL Tripat (#231). `Mapping KIA Narmada` = #222, `Stroke/DM/HT ... (Template)` yang bernama RS tertentu (Panti Nugroho, MPH) dipakai sebagai form RS itu.
- RS2: sheet `Mapping ANC/INC/PNC/BBL (neo)/BBL (INC) Template`, `TB Template`, `HepB (Template)` generik, dictionary dibuat (`mapping/phdt-data-dictionary-rs-template-*.csv`) tapi **tidak masuk total**.
- RS3: sheet `Variable ...`, `Variabel INC/KIA Narmada`, `Sheet6`, `TRACKER`, `Daftar Isi` bukan dictionary, dilewati.

**Temuan terbuka**
- RS-1: `Mapping PNC PKU` hasilnya sama persis dengan `Mapping PNC Panti Nugroho` (67 payload / 131 code): kemungkinan salinan.
- RS-2: `Goetoeng ANC` 106 payload dari 21 variabel: satu variabel tindakan dipetakan ke ±97 Procedure code berbeda (tiap code = 1 payload sesuai aturan). Mohon dicek apakah memang maksudnya.
- RS-3: Belum ada sheet untuk Hepatitis, TB, Tripat INC, dan RS At tin, Harapan Ibu, Nirmala, Margono.

| Form | Variabel unik / baris | Angka PHDT | Payload / code |
|---|---|---|---|
| #228 Tripat ANC | 31 / 31 | 31 | 20 / 28 |
| #231 Tripat BBL (sheet 'INC BBL') | 36 / 36 | – | 23 / 20 |
| #230 Tripat PNC | 36 / 36 | 36 | 24 / 28 |
| #219 Narmada INC | 225 / 227 | – | 86 / 262 |
| #222 Narmada KIA | 70 / 70 | – | 50 / 107 |
| #200 Panti Nugroho ANC | 43 / 56 | 56 | 31 / 68 |
| #201 Panti Nugroho INC | 55 / 56 | 56 | 37 / 118 |
| #202 Panti Nugroho PNC | 85 / 89 | 89 | 67 / 131 |
| #203 Panti Nugroho BBL | 49 / 50 | 50 | 31 / 55 |
| #205 Panti Nugroho Diabetes Melitus | 19 / 19 | 19 | 7 / 4 |
| #206 Panti Nugroho Hipertensi | 40 / 40 | 41 | 23 / 21 |
| #207 Panti Nugroho Stroke | 35 / 35 | 35 | 20 / 23 |
| #173 Ummu Hani ANC | 33 / 34 | 35 | 23 / 49 |
| #174 Ummu Hani INC | 54 / 58 | 53 | 41 / 94 |
| #175 Ummu Hani PNC | 65 / 66 | 67 | 53 / 110 |
| #176 Ummu Hani BBL | 45 / 45 | 0 | 30 / 51 |
| #155 MPH ANC | 43 / 44 | 45 | 33 / 87 |
| #156 MPH INC | 54 / 55 | 55 | 40 / 91 |
| #157 MPH PNC | 59 / 60 | 60 | 43 / 104 |
| #158 MPH BBL | 73 / 73 | 73 | 42 / 59 |
| #160 MPH Diabetes Melitus | 44 / 55 | 52 | 24 / 37 |
| #161 MPH Hipertensi | 35 / 35 | 34 | 20 / 22 |
| #146 Siaga Medika ANC | 61 / 74 | 75 | 100 / 181 |
| #147 Siaga Medika INC | 58 / 67 | 67 | 42 / 125 |
| #148 Siaga Medika PNC | 71 / 72 | 49 | 49 / 110 |
| #149 Siaga Medika BBL | 64 / 64 | 72 | 37 / 48 |
| #183 PKU INC | 81 / 90 | 81 | 66 / 175 |
| #184 PKU PNC | 85 / 89 | 47 | 67 / 131 |
| #191 Goetoeng ANC | 21 / 23 | 23 | 106 / 111 |
| #192 Goetoeng INC | 35 / 38 | 35 | 64 / 245 |
| #193 Goetoeng PNC | 27 / 27 | 27 | 9 / 21 |
| #194 Goetoeng BBL | 34 / 37 | 35 | 68 / 124 |
| #196 Goetoeng Diabetes Melitus | 12 / 12 | 11 | 6 / 4 |
| #197 Goetoeng Hipertensi | 13 / 13 | 12 | 5 / 3 |

## Log perubahan revisi
- 2026-11-24: Tambah bagian SISMAL (Regmal 1 20/54, Validasi Indigenous 7/12): asumsi SM1–SM4, temuan SM-1–SM-5, catatan pipeline P44–P45. Verifikasi Uji Silang tidak dihitung (isi salinan TB-TPT). ⚠️ belum comprehensive review.
- 2026-11-24: Tambah bagian ASIK CKG (5 form, banyak versi), Informed Consent, SiHepi Rekap 3e, eKohort ANC / INC: 9 form dipakai + 5 versi lain (asumsi CK1–CK5, IC1, EK1–EK2, SH1; temuan CK-1–CK-4, IC-1, EK-1–EK-3, SH-1). ⚠️ belum comprehensive review.
- 2026-11-24: Tambah bagian SiGizi 17 form (SG1–SG14) dan catatan pipeline P39–P43. Keputusan user: PMT 2025 = 9 form, `no` tidak dimapping, `detail` → extension `sigizi-detail` valueString.
- 2026-11-24: Tambah bagian perbandingan jumlah variabel dengan PHDT Data Dictionary (4 form beda: SiGizi ANC, TB 06, TB 03 SO, TB 16K). Angka output utama tidak berubah.
- 2026-11-24: Tambah jumlah **Variabel raw** di semua output form dan ringkasan `output.md` (MPDN Bayi 37, Ibu 24 = variabel dictionary tanpa placeholder; belum ada file mentah).
- 2026-11-24: Tambah review MPDN Kematian Bayi dan Kematian Ibu (dictionary dipecah jadi 2 file): hasil hitung 19/112 dan 10/50, tally variabel 37 dan 24 (cocok rekap user, tanpa BQ), asumsi MA1–MA10, temuan MG1–MG6, MB1–MB6, MI1–MI2, perubahan file F1–F5, catatan pipeline P36–P38. **Belum ada comprehensive review**, file mentah, dan daftar BQ.
- 2026-11-18: Tally TB 06: variabel BQ yang dipetakan 93 → 92 (kolom AC tambahan user tidak dihitung).
- 2026-11-17: P25/T06-1 ditutup (kolom AC = tambahan user). T03S-6: path sudah dipakai di TB 02 baris 95. T04-6: TB 04 lookup saja. T03R-4: SR/Specimen/DR ditambah di TB 03 RO (+20 payload). Tambah P35.
- 2026-11-17: Jawaban user: A1, A4, A5, A7, A8, A10, T16-7 disetujui. A3 diubah (blok faskes tetap dimapping & update). A11: `nama_fasyankes` = metadata pipeline. T03S-6 tanpa code. T04-1 ditutup (format baru), tambah T04-6. P25, P28 diperbarui.
- 2026-11-17: Paduan pengobatan: SP001138–SP001140 dibatalkan, SP001137 = Paduan lainnya; baris alias + `productCodeableConcept.text` (TB 03 SO & RO). T03R-5 done. P33 diperbarui, tambah P34.
- 2026-11-17: T06-4 (SP001136), T03S-3 (dataAbsentReason unknown), T03S-4 (SP001137–SP001140) done. Tambah P33.
- 2026-11-17: Jawaban user diterapkan: A2 (data lokal SITB tidak perlu; Status Pengobatan → CarePlan), A6 disetujui (masuk aturan), A9 batal (No. BPJS dicoret), G11 & T04-4 ok, T16-6 dikoreksi. Baris dicoret di sheet sekarang dihapus (G13). Lokasi baris T06-4, T03S-3, T03S-4, T03R-5 ditambahkan; T03R-5 ternyata hanya singkatan (code ada).
- 2026-11-17: Tambah 5 form SITB (TB 06, TB 03 SO, TB 03 RO, TB 04 Fasyankes & Rujukan, TB 16K) dari PHDT_SITB_2.xlsx + schema BQ + export SITB di Drive. TB 13 SO/RO tidak dianalisis. Dijalankan tanpa tanya-jawab: asumsi A1–A12, temuan G1–G12, T06, T03S, T03R, T04, T16; catatan pipeline P24–P30.
- 2026-11-16: Dictionary SiGizi ANC diganti nama jadi `mapping/phdt-data-dictionary-sigizi-anc.csv` (sumber PHDT, bukan Kobo).
- 2026-11-16: URL extension Aksi jadi `http://terminology.kemkes.go.id/sp/sigizi-aksi` (S31, P22).
- 2026-11-16: SiGizi ANC: jawaban R1–R14 diterapkan. S15–S19, S21–S23, S26, S28 done; S20, S24, S25, S27 ok (tetap). Tambah S29–S32 dan P17–P23. Tally 49 = 49 = 49 kolom file mentah. Struktur kolom file mentah di `raw/sigizi-anc-kolom.md`.
- 2026-11-16: Tambah review form SiGizi ANC: tally BQ (49 vs 47), temuan S1–S28 (S1–S14 done di `mapping/`, S15–S28 open menunggu jawaban R1–R14), catatan pipeline P12–P16.
- 2026-11-16: Semua temuan dictionary MO (#12–#15) dan Raffle (R13, R16, R17) done sesuai jawaban user. Tambah P10, P11. Tidak ada temuan dictionary yang open.
- 2026-11-16: MO: blok Organization & Location dihapus (#11), tambah #12–#15. Raffle: hapus baris dobel (R15), tambah R16–R17. Tambah P9.
- 2026-11-16: Semua variabel BQ sekarang masuk payload. Raffle: blok Organization dihapus (R14). MO: puskesmas_name ke serviceProvider (#10). Tambah P8.
- 2026-11-16: User menambah Practitioner data entry di Raffle (commit `9da6c8d`). P2 diperbarui. Tambah R13.
- 2026-11-13: R12 done (kolom BQ `input_data`). MO #8 done (staff_id = nama). R7, R9 disetujui. Tambah bagian Catatan pipeline (P1–P7).
- 2026-11-13: Raffle R1–R11 done di `mapping/kobo-data-dictionary-raffle.csv`. Tambah R12. Maternal Outcome: nama data entry diisi di Encounter.participant ADM (#9).
- 2026-11-13: Tambah review form Raffle: tally BQ dan temuan R1–R11.
- 2026-11-13: Tambah kolom Nama Column BQ dan tally variabel BQ (12 = 12). Tambah temuan #8.
- 2026-11-13: Semua item open dibetulkan langsung di `mapping/kobo-data-dictionary-maternal-outcome.csv`. Tidak ada item open tersisa.
- 2026-11-13: Cek Kobo_3. #1, #2, #3, #5 dan koreksi instance done. #4 masih salah (path berubah tapi belum benar). Tambah #6, #7, dan koreksi instance #4.
- 2026-11-13: Dibuat dari review Maternal Outcome.
- 2026-11-24: Tambah bagian ePuskesmas (11 form dari `PHDT_ePus.xlsx`): sheet→form, hasil hitung, perbandingan variabel dengan PHDT, asumsi EA1–EA10, temuan EF1–EF4. ⚠️ belum comprehensive review.
- 2026-11-24: Tambah bagian Tumbuh Kembang tambahan (KPSP, TDD, TDL, KMPE, M-CHAT-R, GPPH) dari `Childhood_Development_Toolkit_Data_Dictionary.xlsx`: asumsi EB1–EB6. SDIDTK = DDTK yang sudah ada. Dapodik belum dicocokkan.
- 2026-11-24: Tambah bagian Dapodik PAUD (42 payload, 190 code, asumsi DA1–DA4). Sheet dipilih user. Dapodik Antropometri DDTK tetap belum ada mapping.
- 2026-11-24: Tambah bagian 5 CSV PHDT (SITB TB 01, TB 02, ELSMIL x3, SIPTM, ASIK Skrining PTM): 7 form, asumsi CS1–CS9. ⚠️ belum comprehensive review.
- 2026-11-24 (2): Tambah bagian SIM RS (34 form). Perbaikan CK3 (QR Lansia terpisah) dan CK-1 (blok lab Lansia terlewat).
