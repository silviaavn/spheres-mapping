# Output Hitungan Payload & Code — Form Kobo & PHDT

Terakhir diperbarui: 2026-11-24
Aturan hitung: lihat [`aturan.md`](aturan.md) · Temuan & catatan pipeline: [`revisi.md`](revisi.md)
Form yang sudah dihitung (detail per form, bisa ditelusuri per baris):
- **Maternal Outcome** → [`output/maternal-outcome.md`](output/maternal-outcome.md) (sumber: [`mapping/kobo-data-dictionary-maternal-outcome.csv`](mapping/kobo-data-dictionary-maternal-outcome.csv))
- **Raffle** → [`output/raffle.md`](output/raffle.md) (sumber: [`mapping/kobo-data-dictionary-raffle.csv`](mapping/kobo-data-dictionary-raffle.csv))
- **SiGizi ANC** → [`output/sigizi-anc.md`](output/sigizi-anc.md) (sumber: [`mapping/phdt-data-dictionary-sigizi-anc.csv`](mapping/phdt-data-dictionary-sigizi-anc.csv), PHDT Data Dictionary; struktur file mentah: [`raw/sigizi-anc-kolom.md`](raw/sigizi-anc-kolom.md))
- **SITB TB 06** → [`output/sitb-tb06.md`](output/sitb-tb06.md) (sumber: [`mapping/phdt-data-dictionary-sitb-tb06.csv`](mapping/phdt-data-dictionary-sitb-tb06.csv); file mentah: [`raw/sitb-tb06-kolom.md`](raw/sitb-tb06-kolom.md))
- **SITB TB 03 SO** → [`output/sitb-tb03-so.md`](output/sitb-tb03-so.md) (sumber: [`mapping/phdt-data-dictionary-sitb-tb03-so.csv`](mapping/phdt-data-dictionary-sitb-tb03-so.csv); file mentah: [`raw/sitb-tb03-so-kolom.md`](raw/sitb-tb03-so-kolom.md))
- **SITB TB 03 RO** → [`output/sitb-tb03-ro.md`](output/sitb-tb03-ro.md) (sumber: [`mapping/phdt-data-dictionary-sitb-tb03-ro.csv`](mapping/phdt-data-dictionary-sitb-tb03-ro.csv); file mentah: [`raw/sitb-tb03-ro-kolom.md`](raw/sitb-tb03-ro-kolom.md))
- **SITB TB 04** (Fasyankes & Rujukan) → [`output/sitb-tb04.md`](output/sitb-tb04.md) (sumber: [`mapping/phdt-data-dictionary-sitb-tb04.csv`](mapping/phdt-data-dictionary-sitb-tb04.csv); file mentah: [`raw/sitb-tb04-kolom.md`](raw/sitb-tb04-kolom.md))
- **SITB TB 16K** → [`output/sitb-tb16k.md`](output/sitb-tb16k.md) (sumber: [`mapping/phdt-data-dictionary-sitb-tb16k.csv`](mapping/phdt-data-dictionary-sitb-tb16k.csv); file mentah: [`raw/sitb-tb16k-kolom.md`](raw/sitb-tb16k-kolom.md))
- **MPDN Kematian Bayi** → [`output/mpdn-kematian-bayi.md`](output/mpdn-kematian-bayi.md) (sumber: [`mapping/phdt-data-dictionary-mpdn-kematian-bayi.csv`](mapping/phdt-data-dictionary-mpdn-kematian-bayi.csv), PHDT Data Dictionary; **belum ada file mentah dan daftar variabel BQ**, belum ada comprehensive review)
- **MPDN Kematian Ibu** → [`output/mpdn-kematian-ibu.md`](output/mpdn-kematian-ibu.md) (sumber: [`mapping/phdt-data-dictionary-mpdn-kematian-ibu.csv`](mapping/phdt-data-dictionary-mpdn-kematian-ibu.csv), PHDT Data Dictionary; **belum ada file mentah dan daftar variabel BQ**, belum ada comprehensive review)

File ini adalah **konsolidasi** lintas form. Angka per form di sini harus sama dengan file `output/<form>.md`.

Belum: PNC, SITB TB 13 SO/RO, form lain

---

## Daftar isi

Di file ini:
1. [Ringkasan semua form](#ringkasan-semua-form)
2. [Jumlah per CodeSystem](#jumlah-per-codesystem-code-unik-lintas-form)
3. [Payload per resource](#payload-per-resource-semua-form)
4. [Catatan](#catatan)
5. [Log perubahan output](#log-perubahan-output)

File terpisah (detail):
- [`frekuensi-payload.md`](frekuensi-payload.md): setiap payload unik (resource + code pembeda + display) dan form yang memakainya
- [`frekuensi-code.md`](frekuensi-code.md): setiap code unik (1 code per baris, dengan CodeSystem) dan form yang memakainya
- `output/<form>.md`: output per form dengan nomor baris dictionary (lihat daftar form di atas)

---

## Ringkasan semua form

Kolom **Code SP** = jumlah code dengan CodeSystem `http://terminology.kemkes.go.id/sp` (sudah termasuk di kolom Code).

| Form | Payload | Code | Code SP |
|---|---|---|---|
| Maternal Outcome | 12 | 14 | 4 |
| Raffle | 8 | 6 | 4 |
| SiGizi ANC | 61 | 142 | 18 |
| SITB TB 06 | 56 | 276 | 9 |
| SITB TB 03 SO | 62 | 329 | 10 |
| SITB TB 03 RO | 50 | 377 | 11 |
| SITB TB 04 | 69 | 579 | 24 |
| SITB TB 16K | 21 | 35 | 14 |
| MPDN Kematian Bayi | 19 | 112 | 37 |
| MPDN Kematian Ibu | 10 | 50 | 17 |
| **Total (non-unik)** | **368** | **1920** | **148** |
| **Total unik** | **164** | **510** | **80** |
| Selisih (dipakai ulang) | 204 | 1410 | 68 |

---

## Jumlah per CodeSystem (code unik lintas form)

Daftar code satu per baris: lihat [`frekuensi-code.md`](frekuensi-code.md).

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 136 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 120 |
| http://terminology.kemkes.go.id/sp | 80 |
| http://loinc.org | 76 |
| http://terminology.kemkes.go.id/CodeSystem/examination | 20 |
| http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment | 17 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 15 |
| http://terminology.kemkes.go.id/CodeSystem/organization-type | 12 |
| http://terminology.kemkes.go.id/CodeSystem/location-type | 7 |
| http://terminology.kemkes.go.id | 5 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 4 |
| http://hl7.org/fhir/sid/icd-10 | 4 |
| http://sys-ids.kemkes.go.id/kfa | 3 |
| http://terminology.kemkes.go.id/CodeSystem/composition-type | 3 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC | 2 |
| http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes | 2 |
| http://terminology.kemkes.go.id/CodeSystem/tb-case-definition | 2 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 1 |
| http://hl7.org/fhir/sid/icd-9-cm | 1 |
| **Total** | **510** |

---

## Payload per resource (semua form)

Baris = form, kolom = resource FHIR. Code pembeda tiap payload: lihat [`frekuensi-payload.md`](frekuensi-payload.md).

| Form | Observation | ServiceRequest | DiagnosticReport | Specimen | Procedure | Patient | EpisodeOfCare | Condition | Encounter | QuestionnaireResponse | CarePlan | Organization | Practitioner | Coverage | Location | MedicationDispense | MedicationRequest | PractitionerRole | Composition | Group | Immunization | RelatedPerson | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maternal Outcome | 5 | – | – | – | – | 1 | 2 | 1 | 1 | – | – | – | 1 | – | – | – | – | 1 | – | – | – | – | 12 |
| Raffle | 1 | – | – | – | – | 1 | 1 | 1 | 1 | – | – | – | 2 | – | 1 | – | – | – | – | – | – | – | 8 |
| SiGizi ANC | 30 | 6 | 6 | 6 | 3 | 1 | 1 | 1 | 1 | – | – | – | – | – | – | 2 | 2 | 1 | – | – | 1 | – | 61 |
| SITB TB 06 | 17 | 9 | 9 | 8 | 2 | 1 | 3 | 2 | 1 | 1 | 1 | 1 | – | – | 1 | – | – | – | – | – | – | – | 56 |
| SITB TB 03 SO | 23 | 9 | 9 | 9 | 4 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | – | 1 | – | – | – | – | – | – | – | – | 62 |
| SITB TB 03 RO | 18 | 7 | 7 | 7 | 3 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | – | 1 | – | – | – | – | – | – | – | – | 50 |
| SITB TB 04 | 17 | 16 | 16 | 16 | – | 1 | 1 | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | 69 |
| SITB TB 16K | 14 | 1 | – | – | – | 1 | – | 1 | 1 | 1 | – | – | – | – | – | – | – | – | – | 1 | – | 1 | 21 |
| MPDN Kematian Bayi | 16 | – | – | – | – | 2 | – | – | – | – | – | – | – | – | – | – | – | – | 1 | – | – | – | 19 |
| MPDN Kematian Ibu | 7 | – | – | – | – | 1 | – | 1 | – | – | – | – | – | – | – | – | – | – | 1 | – | – | – | 10 |
| **Total (non-unik)** | **148** | **48** | **47** | **46** | **12** | **11** | **10** | **10** | **8** | **4** | **3** | **3** | **3** | **2** | **2** | **2** | **2** | **2** | **2** | **1** | **1** | **1** | **368** |
| **Total unik** | **85** | **20** | **19** | **4** | **7** | **1** | **4** | **8** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **2** | **2** | **1** | **1** | **1** | **1** | **1** | **164** |

---

## Catatan

- Organization tidak dihitung di Kobo, SiGizi, TB 04, dan TB 16K (lookup master data, bloknya tidak ditulis di dictionary). Location di Maternal Outcome dan SiGizi ANC juga lookup (tidak dihitung), tapi di Raffle dihitung karena dibuat dari form.
- SiGizi ANC: faskes & posyandu berupa string → lookup master data. PractitionerRole petugas lab → lookup (tidak dihitung). 6 Specimen di SiGizi ANC hanya 2 jenis (darah vena ×5, urine ×1). Code Observation dengan 2 coding (LOINC + ANC custom) dihitung dua-duanya.
- PractitionerRole tenaga pemeriksa SiGizi ANC dan PractitionerRole MO sama-sama tanpa code pembeda tetap (code-nya opsi), jadi dihitung sebagai payload yang sama.
- EpisodeOfCare: Maternal Outcome = ANC & PNC ditutup (finished, hari ke-43); Raffle = ANC dicari dulu, kalau tidak ada baru dibuat.
- Encounter muncul di 2 blok kamus (data utama + statusHistory) = 1 payload.
- SITB TB 06, TB 03 SO, TB 03 RO: blok faskes (Organization + Location) **dihitung** karena dimapping dari variabel faskes di form (match + update). TB 04 dan TB 16K: faskes lookup (TB 04 lewat metadata `puskesmas_id` / `puskesmas_name`). PractitionerRole petugas lab/radiografer dan Practitioner PJ SITB = lookup master data (tidak dihitung). Baris yang dicoret di sheet tidak dipakai. Lihat asumsi A1–A12 di `revisi.md`.
- SITB: opsi coded yang mengikuti jawaban ikut dihitung sebagai code (reasonCode ServiceRequest, CarePlan activity, admitSource, jawaban QuestionnaireResponse, component lab, metode biakan) — disetujui, lihat `aturan.md`. Karena itu jumlah code SITB besar (mis. TB 04: 16 ServiceRequest × 9 alasan pemeriksaan, 16 Specimen × 11 jenis contoh uji).
- SITB TB 04: 1 dictionary untuk TB 04 Fasyankes dan TB 04 Rujukan (header sama). TB 03 RO: follow up 24 bulan = 1 template BTA + 1 template Biakan (asumsi A7); setiap pemeriksaan lab punya ServiceRequest + Specimen + Observation + DiagnosticReport (T03R-4).
- SITB: EpisodeOfCare TB-SO / TB-RO, Patient, Encounter, Condition A15.0, Observation umur (424144002), HIV/DM, lab (11545-1, X0993xx) dipakai ulang di beberapa form SITB → total unik jauh lebih kecil dari non-unik.

- MPDN Kematian Bayi / Ibu: **belum ada comprehensive review**, file mentah, dan daftar variabel BQ (tally BQ belum bisa dicek; kolom Nama Column BQ kosong). Satu payload Composition per laporan; Location di `Composition.contained` ikut di dalam Composition (tidak dihitung terpisah). Dua Patient (ibu + bayi) di Bayi dihitung 2 payload. Tidak ada Encounter, dan Practitioner PJ MPDN tidak dibuat (lookup). `Composition.type` (COM000001/2/3) dihitung sebagai code; ICD-PM / ICD-MM (daftar eksternal) dan kode ICD dinamis di Condition tidak dihitung. Asumsi dan temuan: `revisi.md` bagian MPDN.
---

## Log perubahan output
- 2026-11-24: Tambah 2 form MPDN dari `PHDT_Data_Dictionary_-_MPDN.csv`: Kematian Bayi (19 payload / 112 code) dan Kematian Ibu (10 / 50). Belum ada daftar variabel BQ dan belum ada comprehensive review. Total non-unik 339 / 1758 → **368 / 1920**, unik 148 / 434 → **164 / 510**. Resource baru: Composition. Tabel di file ini dan `frekuensi-*.md` dibuat ulang untuk 10 form dengan `scripts/consolidate.py` (hasilnya identik dengan versi lama untuk 8 form sebelumnya).
- 2026-11-18: Ringkasan semua form: tambah kolom **Code SP** (CodeSystem `http://terminology.kemkes.go.id/sp`). Daftar form diberi link. Output per form diberi baris File terkait (link ke `output.md`, frekuensi, dictionary, file mentah) dan baris Code SP di Ringkasan.
- 2026-11-18: `output.md` dirampingkan: tambah Daftar isi; tabel Frekuensi payload dan Frekuensi code dipindah ke file terpisah `frekuensi-payload.md` dan `frekuensi-code.md`. Angka tidak berubah.
- 2026-11-18: Format tabel: "Jumlah per CodeSystem" hanya CodeSystem + jumlah (daftar code per baris ada di tabel Frekuensi code). "Payload per resource" ditranspos: baris = form, kolom = resource FHIR, tanpa kolom pembeda; ditambah baris Total unik. Bagian Catatan dikembalikan (sempat terhapus 17 Nov) dan diperbarui. Angka tidak berubah. Format yang sama dipakai di `output/<form>.md` (Code per CodeSystem tanpa daftar code).
- 2026-11-17: TB 04 lookup faskes saja (blok Org/Location dihapus, 71 → **69** payload). TB 03 RO: ServiceRequest + Specimen + DiagnosticReport untuk 7 pemeriksaan lab (30 → **50** payload, 357 → **377** code). TB 06 kolom AC (tambahan user) tidak dihitung. Total non-unik 339 / 1758, unik 148 / 434.
- 2026-11-17: Blok faskes dikembalikan (A3): +2 payload di TB 06 (56), TB 04 (71); +1 di TB 03 SO (62), TB 03 RO (30). Code tidak berubah.
- 2026-11-17: SP001138–SP001140 dibatalkan; SP001137 jadi "Paduan lainnya" (TB 03 SO & RO). Varian teks paduan ditambah sebagai baris alias (code lama, tidak dihitung ulang). TB 03 SO 332 → **329** code, TB 03 RO 356 → **357** code. Total non-unik 315 / 1738, unik 147 / 434.
- 2026-11-17: Code lokal baru: TB 06 SP001136 Belum Mulai Pengobatan (code 275 → **276**); TB 03 SO SP001137–SP001140 paduan pengobatan (code 328 → **332**). Hasil Tes HIV "Tidak Diketahui" → dataAbsentReason unknown (tidak dihitung). Total non-unik 315 / 1740, unik 147 / 437.
- 2026-11-17: Jawaban user diterapkan. TB 06: 55 → **54 payload** (Coverage dihapus karena No. BPJS dicoret di sheet), code tetap 275. TB 03 SO: tetap 61 / 328 (Status Pengobatan masuk CarePlan sebagai teks). TB 16K: 24/39 → **21 payload / 35 code** (Practitioner, PractitionerRole kader, dan Observation SP000211 dicoret di sheet). Total non-unik 315 / 1735, unik 147 / 432.
- 2026-11-17: Tambah 5 form SITB: TB 06 (55 payload / 275 code), TB 03 SO (61 / 328), TB 03 RO (29 / 356), TB 04 (69 / 579), TB 16K (24 / 39). Total non-unik jadi 319 payload / 1739 code, unik 148 / 434. Semua tabel di file ini sekarang dibuat ulang dari 8 dictionary di `mapping/` (angka 3 form lama tidak berubah; urutan baris yang frekuensinya sama di tabel Payload per resource bisa bergeser).
- 2026-11-16: Dictionary SiGizi ANC diganti nama jadi `mapping/phdt-data-dictionary-sigizi-anc.csv` (sumbernya PHDT Data Dictionary, bukan Kobo). Angka tidak berubah.
- 2026-11-16: Ringkasan `output/sigizi-anc.md`: baris "Variabel BQ di luar payload" diganti "Variabel di Excel export" (SiGizi ANC: 49, angka saja). Baris ini tidak muncul di form Kobo (tidak ada file mentah). Angka tidak berubah.
- 2026-11-16: SiGizi ANC final setelah jawaban R1–R14: **61 payload, 142 code** (−6 PractitionerRole lab, +1 Observation usia kehamilan 18185-9; code −6 Laboratory worker, +1 18185-9). Tabel frekuensi, CodeSystem, dan payload per resource diperbarui untuk 3 form. Total non-unik 81 payload / 162 code, unik 68 / 132.
- 2026-11-16: Tambah SiGizi ANC sebagai angka sementara (66 payload, 147 code; total non-unik 86/167, unik 67/132). Tabel frekuensi belum diubah sampai R1–R14 dijawab. `scripts/form_output.py` mengenali code pembeda untuk Procedure, ServiceRequest, DiagnosticReport, Specimen, Immunization, MedicationRequest, MedicationDispense (output MO & Raffle tidak berubah).
- 2026-11-16: Revisi reference & path di kedua dictionary (lihat `revisi.md`). Angka tidak berubah.
- 2026-11-16: MO: blok Organization & Location dihapus dari dictionary (lookup master data). Angka tidak berubah.
- 2026-11-16: Output per form menampilkan path tiap variabel BQ dan tanda 🔎 untuk lookup master data. Semua variabel BQ sudah masuk payload (0 di luar payload). Angka tidak berubah.
- 2026-11-16: Tambah output per form (`output/maternal-outcome.md`, `output/raffle.md`), dibuat dengan `scripts/form_output.py`. Raffle jadi 8 payload (Practitioner data entry ditambahkan user di commit `9da6c8d`). Total non-unik 20, unik 15.
- 2026-11-13: Ringkasan diberi Total non-unik vs unik; kolom Jenis resource dihapus. Section payload per form diganti jadi satu tabel "Payload per resource (semua form)".
- 2026-11-13: Raffle direvisi: Location dibuat dari form (payload jadi 7), Condition.code jadi SP001135. Total unik lintas form jadi 15 payload, 8 jenis resource, 19 code.
- 2026-11-13: Tambah form Raffle (6 payload, 6 baris code). Total unik lintas form jadi 14 payload, 18 code. Frekuensi Practitioner, Patient, Encounter, EpisodeOfCare ANC, dan code ANC naik jadi 2.
- 2026-11-13: Kolom "Code per submission" dihapus (tidak dipakai).
- 2026-11-13: Tabel frekuensi payload diberi kolom Code pembeda, Display, dan Variabel Kobo.
- 2026-11-13: Dicek ulang dengan Kobo_3. Angka tidak berubah (12 payload, 14 code). Display SP000396/SP000397 dibetulkan.
- 2026-11-13: File dipisah jadi `aturan.md`, `revisi.md`, `output.md`.
- 2026-11-13: Maternal Outcome dihitung. Repo dibersihkan; isi lama ada di commit `0aba562`.
