# Aturan Hitung Payload & Code — Form Kobo

Terakhir diperbarui: 2026-11-13

## Payload (instance)
- 1 payload = 1 resource FHIR yang dibuat dari submission form.
- Identitas payload = resource + determining code (mis. `Observation | SP000389`, `EpisodeOfCare | ANC`). Resource tanpa determining code (Patient, Practitioner, Encounter) identitasnya cukup nama resource.
- Di tabel output, payload selalu ditulis dengan code pembeda **dan display-nya**.
- Encounter yang muncul di 2 blok kamus (data utama + statusHistory) = **1 payload**.
- **Patient dihitung.**
- **Organization dan Location TIDAK dihitung**: keduanya diambil dari master data (lookup/reference), bukan dibuat dari form.

## Determining code
- Code yang menentukan identitas payload: `PractitionerRole.code`, `Condition.code`, `EpisodeOfCare.type`, `Observation.code`.
- Ditambah pilihan jawaban coded (`Observation.valueCodeableConcept`) dan opsi role PractitionerRole.
- Code tetap HL7 (status, category, class, participant.type, diagnosis.use, clinicalStatus, organization-type, physicalType) **tidak dihitung**.
- Bedakan: **code di kamus** (semua opsi) vs **code per submission** (hanya opsi yang terpilih).

## Frekuensi
- **Frekuensi payload** = di berapa form payload yang sama (resource + determining code) dipakai.
- **Frekuensi code** = di berapa form code yang sama (code + CodeSystem) dipakai.
- Contoh: kalau SP000389 nanti juga dipakai di form PNC, frekuensinya jadi 2.

## Total unik lintas form
- Payload/code yang sama di beberapa form hanya dihitung sekali.
- Setiap form baru masuk: tambahkan nama form di kolom "Dipakai di form" di `output.md`, naikkan frekuensinya, lalu hitung ulang baris "Total unik".

## Checklist setiap form baru
1. **Minta daftar variabel BQ dari form** (nama kolom di BigQuery). Jangan mulai hitung sebelum daftar ini ada.
2. Cek tally: jumlah variabel BQ = jumlah baris yang punya "Nama Variabel di Kobo". Cek juga isinya cocok satu-satu (mis. `staff_id` jangan dipasang ke baris nama).
3. Isi kolom **Nama Column BQ** (letaknya sebelum "Nama Column Raw") di dictionary.
4. Baru hitung payload & code, lalu update `output.md` dan `revisi.md`.

## Kolom di data dictionary
- `jumlah instance` = isi 1 di baris pertama setiap payload.
- `jumlah code` = isi 1 di setiap baris determining code / opsi coded.

## Log perubahan aturan
- 2026-11-13: Tambah checklist form baru (minta daftar variabel BQ, cek tally, isi kolom Nama Column BQ).
- 2026-11-13: Payload di output wajib ditulis lengkap dengan display.
- 2026-11-13: Frekuensi didefinisikan ulang jadi "dipakai di berapa form".
- 2026-11-13: Dibuat. Patient masuk hitungan; Organization & Location tidak (master data).
