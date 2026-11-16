# Revisi Data Dictionary — Form Kobo

Terakhir diperbarui: 2026-11-16
File dictionary terbaru: Maternal Outcome → `mapping/kobo-data-dictionary-maternal-outcome.csv`; Raffle → `mapping/kobo-data-dictionary-raffle.csv`; SiGizi ANC → `mapping/kobo-data-dictionary-sigizi-anc.csv` (nomor baris di bawah mengikuti CSV asli; di `mapping/` nomor barisnya sudah berbeda karena ada baris tambahan/dihapus. Untuk nomor baris terbaru lihat `output/raffle.md`)

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

## Form: SiGizi ANC

Sumber: PHDT Data Dictionary - SiGiziANC (nomor baris = baris CSV asli, header 7 baris). Contoh data mentah: PUSKESMAS PADAMARA SiGizi Pengukuran ANC (57 baris, 2026-11-16). Versi revisi: `mapping/kobo-data-dictionary-sigizi-anc.csv` (ada 1 baris sisipan setelah baris 268 dan 2 sel multi-baris jadi 1 baris, jadi nomor baris bergeser; untuk nomor baris terbaru lihat `output/sigizi-anc.md`).

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
| S17 | `pemeriksaan_anc_aksi` = kolom "Aksi" di export web (link halaman perkembangan bumil SiGizi) | done (mapping/): `Encounter.extension` url `https://github.com/silviaavn/spheres-mapping/StructureDefinition/sigizi-aksi` (sementara, S31), `valueUrl` = isi Aksi. Di file Padamara kolom ini kosong 57/57 (S30) |
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
| S31 | URL extension `sigizi-aksi` masih sementara (belum ada canonical resmi). Perlu dicek juga apakah SatuSehat menerima extension custom di Encounter | open |
| S32 | Jumlah TTD/MMS = 0: cara mencatat "diberikan 0" (bukan kosong) belum ditentukan | open (lihat opsi di laporan chat 2026-11-16) |

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
| P22 | SiGizi ANC | Kolom `pemeriksaan_anc_aksi` → `Encounter.extension` sigizi-aksi (valueUrl) | Ingestion: pastikan link ikut terambil (di export Padamara kosong). Converter: cek apakah SatuSehat menerima extension ini; kalau tidak, buang sebelum kirim ke SatuSehat | open |
| P23 | SiGizi ANC | Hb Anemia Berat → OI000034; DiagnosticReport HIV/Hepatitis/Sifilis category SR; EpisodeOfCare ANC dicari dulu (active) sebelum buat baru | Converter | open |
| P16 | SiGizi ANC | Pilihan TD di form sumber `Normal (<= 140)` dan `Hipertensi (>= 140)` sama-sama memuat 140 | Info ke pemilik form SiGizi | open |

## Log perubahan revisi
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
