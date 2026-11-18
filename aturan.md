# Aturan Hitung Payload & Code — Form Kobo & PHDT

Terakhir diperbarui: 2026-11-17

## Sumber dictionary
- **Kobo**: `mapping/kobo-data-dictionary-<form>.csv` (Maternal Outcome, Raffle).
- **PHDT Data Dictionary** (mis. SiGizi): `mapping/phdt-data-dictionary-<form>.csv`. Jangan disebut Kobo.

## Sumber kebenaran: file mentah
- Kalau ada **file mentah** (mis. export Excel SiGizi), file itu sumber kebenaran. Kobo tidak punya file mentah.
- **Setiap kolom di file mentah wajib punya mapping**, termasuk kolom tampilan seperti `Aksi` (link halaman) → extension di Encounter.
- Cocokkan kolom mentah ↔ BQ ↔ dictionary berdasarkan **nama header**, bukan posisi kolom (urutan bisa beda, mis. SiGizi: NIK sebelum Nama).
- Lampirkan struktur kolomnya di `raw/<form>-kolom.md`: header bertingkat/merge cell, variabel BQ, jumlah terisi, dan nilai pilihan. **File asli tidak di-commit** dan kolom identitas pasien (nama, NIK, tanggal lahir, alamat) tidak ditampilkan.

## Payload (instance)
- 1 payload = 1 resource FHIR yang dibuat dari submission form.
- Identitas payload = resource + determining code (mis. `Observation | SP000389`, `EpisodeOfCare | ANC`). Resource tanpa determining code (Patient, Practitioner, Encounter) identitasnya cukup nama resource.
- Di tabel output, payload selalu ditulis dengan code pembeda **dan display-nya**.
- Dalam 1 form, resource yang sama tanpa code pembeda bisa muncul lebih dari 1x dan **dihitung masing-masing** (mis. Raffle: Practitioner bidan desa + Practitioner data entry = 2 payload). Di total unik tetap dihitung 1.
- Encounter yang muncul di 2 blok kamus (data utama + statusHistory) = **1 payload**.
- **Patient dihitung.**
- **Organization TIDAK dihitung**: diambil dari master data (lookup/reference), bukan dibuat dari form. Variabel BQ puskesmas dipetakan ke `Encounter.serviceProvider.reference` dengan keterangan "Lookup ke master data Organization" di kolom Definisi Operasional. Kalau isian puskesmas dipilih dari list yang sudah ada, blok Organization tidak perlu ditulis di dictionary.
- Pengecualian (SITB): kalau form punya variabel faskes pelapor (kode, nama, jenis, kepemilikan, alamat), blok Organization + Location faskes **tetap dimapping dan dihitung payload**: cari di master data, kalau match di-update dari form (TB 06, TB 03 SO/RO). Kalau tidak ada variabel faskes (TB 04, TB 16K), cukup lookup seperti MO & Raffle.
- Kolom tambahan buatan user di export (tidak punya nomor kolom SITB) bukan variabel: tidak dihitung di tally.
- **Location**: tidak dihitung kalau hanya lookup ke master data (mis. Maternal Outcome). **Dihitung** kalau dibuat dari isian form (mis. Raffle: lokasi faskes + kecamatan + kelurahan).
- Isian berupa **string bebas** yang menunjuk faskes/posyandu (mis. SiGizi: Faskes yang melayani ANC, Posyandu Domisili) tetap **lookup**: cocokkan string ke master data. Organization/Location tidak ditulis dan tidak dihitung. Kolom lain yang membantu pencocokan (mis. desa, puskesmas domisili) ditulis sebagai baris "Kunci lookup" di resource yang mereferensi.
- **PractitionerRole petugas lab** tidak dibuat dari form: lookup ke master data PractitionerRole default lab milik Organization faskes. Tidak dihitung.
- Jawaban alternatif yang masih resource sama (mis. Immunization completed / not-done) = **1 payload**.
- Resource yang hanya dibuat kalau ada nilai (mis. lab "Tidak Diperiksa", jumlah obat 0) tetap dihitung sebagai payload; syaratnya ditulis di Definisi Operasional.
- Nama orang yang meng-input data (data entry) dimasukkan ke `Encounter.participant` dengan type `ADM` (admitter, http://terminology.hl7.org/CodeSystem/v3-ParticipationType). Tidak menambah payload karena masih di dalam Encounter.

## Determining code
- Code yang menentukan identitas payload: `PractitionerRole.code`, `Condition.code`, `EpisodeOfCare.type`, `Observation.code`, `Procedure.code`, `ServiceRequest.code`, `DiagnosticReport.code`, `Specimen.type`, `Immunization.vaccineCode`, code Medication (`contained.code`).
- Observation dengan 2 coding di `code` (mis. LOINC + ANC custom): **keduanya dihitung**; code pembeda = coding pertama.
- Ditambah pilihan jawaban coded (`Observation.valueCodeableConcept`, `Observation.interpretation`), opsi role PractitionerRole, dan opsi code lain yang mengikuti jawaban (mis. `Encounter.identifier` K1M/K1A, kesepakatan SatuSehat).
- Opsi coded yang mengikuti jawaban **juga dihitung** di: `ServiceRequest.reasonCode`, `CarePlan.activity.detail.code` / `productCodeableConcept` / `statusReason`, `CarePlan.activity.outcomeCodeableConcept`, `Encounter.hospitalization.admitSource`, `QuestionnaireResponse...answer.valueCoding`, `Observation.component.code` / `component.valueCodeableConcept`, `Observation.method` (mis. metode biakan LJ/MGIT).
- **Tidak dihitung** juga: category (termasuk yang SNOMED / v2-0074), `Specimen.collection.method`, `Immunization.reasonCode`, form / ingredient / extension Medication, unit (UCUM, v3-orderableDrugForm), `dataAbsentReason`.
- Code tetap HL7 (status, category, class, participant.type, diagnosis.use, clinicalStatus, organization-type, physicalType) **tidak dihitung**.
- Semua opsi coded di kamus dihitung (bukan hanya yang terpilih saat submission).

## Frekuensi
- **Frekuensi payload** = di berapa form payload yang sama (resource + determining code) dipakai.
- **Frekuensi code** = di berapa form code yang sama (code + CodeSystem) dipakai.
- Contoh: kalau SP000389 nanti juga dipakai di form PNC, frekuensinya jadi 2.

## Total unik lintas form
- Payload/code yang sama di beberapa form hanya dihitung sekali.
- Setiap form baru masuk: tambahkan nama form di kolom "Dipakai di form" di `frekuensi-payload.md` / `frekuensi-code.md` (dibuat ulang otomatis bersama `output.md`), naikkan frekuensinya, lalu hitung ulang baris "Total unik".

## Checklist setiap form baru
1. **Minta daftar variabel BQ dari form** (nama kolom di BigQuery). Jangan mulai hitung sebelum daftar ini ada. Kalau ada file mentah, cocokkan juga kolom mentah ↔ BQ (lihat "Sumber kebenaran: file mentah") dan buat `raw/<form>-kolom.md`.
2. Cek tally: jumlah variabel BQ = jumlah baris yang punya "Nama Variabel di Kobo". Cek juga isinya cocok satu-satu (mis. `staff_id` jangan dipasang ke baris nama).
   **Semua variabel BQ harus masuk ke salah satu payload.** Cek bagian "Variabel di luar payload" di `output/<form>.md` harus kosong.
   Pengecualian: kolom data lokal sistem sumber yang tidak perlu dikirim (SITB: No. Urut, Bulan, No. Registrasi Fasyankes / Kab/Kota) dan baris yang **dicoret** (strikethrough) di sheet dictionary. Keduanya dicatat di `revisi.md` sebagai "tidak dimapping".
3. Isi kolom **Nama Column BQ** (letaknya sebelum "Nama Column Raw") di dictionary.
4. Isi kolom `jumlah instance` dan `jumlah code` di dictionary `mapping/`, lalu buat output per form:
   `python3 scripts/form_output.py mapping/kobo-data-dictionary-<form>.csv "<Nama Form>" output/<form>.md [raw/<form>-kolom.md]`
   Kalau ada file mentah, tambahkan argumen ke-4 `raw/<form>-kolom.md`.
5. Update konsolidasi `output.md`, `frekuensi-payload.md`, `frekuensi-code.md` (angka per form harus sama dengan `output/<form>.md`) dan `revisi.md`.

## Kolom di data dictionary
- `jumlah instance` = isi 1 di baris pertama setiap payload.
- `jumlah code` = isi 1 di setiap baris determining code / opsi coded.

## Ringkasan di output per form
- Baris: Payload, Code, Code unik, Variabel BQ (unik).
- Kalau ada file mentah, tambah baris **Variabel di Excel export** = jumlah kolom di file mentah (angka saja, tanpa keterangan tambahan).
- "Variabel BQ di luar payload" **tidak dicantumkan** di ringkasan. Pengecekannya tetap lewat bagian "Variabel di luar payload" di bawah (harus kosong) dan peringatan dari script kalau ada kolom Excel export yang belum masuk payload.

## Log perubahan aturan
- 2026-11-18: `output.md` hanya berisi ringkasan, jumlah per CodeSystem, payload per resource, catatan; frekuensi payload & code di `frekuensi-payload.md` / `frekuensi-code.md`. Format output: tabel per CodeSystem hanya jumlah; tabel Payload per resource di `output.md` = baris form × kolom resource FHIR.
- 2026-11-17: (SITB) Blok faskes dengan variabel dari form tetap dimapping dan dihitung (match + update).
- 2026-11-17: (SITB) Opsi coded reasonCode, CarePlan activity, admitSource, jawaban QuestionnaireResponse, component lab, Observation.method ikut dihitung sebagai code. Baris dicoret di sheet dan kolom data lokal SITB (No. Urut, Bulan, No. Reg Fasyankes) tidak dimapping.
- 2026-11-16: Nama file dictionary dibedakan per sumber: `kobo-` untuk Kobo, `phdt-` untuk PHDT Data Dictionary.
- 2026-11-16: Ringkasan output per form: "Variabel BQ di luar payload" tidak dicantumkan; kalau ada file mentah, tampilkan "Variabel di Excel export" (angka saja). `form_output.py` menerima argumen ke-4 `raw/<form>-kolom.md`.
- 2026-11-16: (SiGizi ANC) File mentah = sumber kebenaran, semua kolom wajib punya mapping, lampiran `raw/<form>-kolom.md`. String faskes/posyandu → lookup master data. PractitionerRole petugas lab → lookup. Determining code diperluas untuk Procedure, ServiceRequest, DiagnosticReport, Specimen, Immunization, Medication, interpretation; daftar code yang tidak dihitung diperjelas (dipakai sejak SiGizi ANC).
- 2026-11-16: Semua variabel BQ wajib masuk payload. Puskesmas → Encounter.serviceProvider.reference (lookup master data).
- 2026-11-16: Output per form wajib dibuat dengan `scripts/form_output.py`. Resource sama dalam 1 form dihitung masing-masing.
- 2026-11-13: Location dihitung kalau dibuat dari form. Nama data entry → Encounter.participant ADM.
- 2026-11-13: Konsep "code per submission" dihapus; yang dihitung hanya code di kamus.
- 2026-11-13: Tambah checklist form baru (minta daftar variabel BQ, cek tally, isi kolom Nama Column BQ).
- 2026-11-13: Payload di output wajib ditulis lengkap dengan display.
- 2026-11-13: Frekuensi didefinisikan ulang jadi "dipakai di berapa form".
- 2026-11-13: Dibuat. Patient masuk hitungan; Organization & Location tidak (master data).
