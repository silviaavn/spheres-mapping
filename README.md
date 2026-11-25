# spheres-mapping

Konsolidasi mapping FHIR (SatuSehat) dari data dictionary form SPHERES: form **Kobo** dan **PHDT Data Dictionary** (SiGizi, SITB, dll). Untuk setiap form dihitung payload (resource FHIR) dan code-nya, lalu digabung jadi angka lintas form.

## Mulai dari mana

| File | Isi |
|---|---|
| [`form-tracker.md`](form-tracker.md) | Daftar semua sumber data/laporan + status: masih diperlukan, dimapping ke FHIR, sudah direview. Versi editable: [Sheet](https://claude.ai/artifact/HRNvr5haWkiSyVHUVakRgj) |
| [`aturan.md`](aturan.md) | Aturan hitung payload & code, checklist setiap form baru, log perubahan aturan |
| [`output.md`](output.md) | Konsolidasi semua form: ringkasan, jumlah per CodeSystem, payload per resource |
| [`frekuensi-payload.md`](frekuensi-payload.md) | Setiap payload unik dan form yang memakainya |
| [`frekuensi-code.md`](frekuensi-code.md) | Setiap code unik (dengan CodeSystem) dan form yang memakainya |
| [`revisi.md`](revisi.md) | Temuan yang perlu diperbaiki di data dictionary dan catatan pipeline |

## Struktur folder

```
mapping/   data dictionary per form (CSV)
           kobo-data-dictionary-<form>.csv   → form Kobo
           phdt-data-dictionary-<form>.csv   → PHDT Data Dictionary (SiGizi, SITB)
output/    output per form: payload, code, nomor baris dictionary
raw/       struktur kolom file mentah (header, variabel BQ, jumlah terisi)
           file asli tidak di-commit, kolom identitas pasien tidak ditampilkan
scripts/   form_output.py: membuat output/<form>.md dari dictionary
           epus_prepare.py: memecah PHDT_ePus.xlsx jadi dictionary per form (mapping/phdt-data-dictionary-epus-*.csv)
           tumbang_prepare.py: sama, untuk Childhood_Development_Toolkit_Data_Dictionary.xlsx (KPSP, TDD, TDL, KMPE, M-CHAT-R, GPPH)
           dapodik_prepare.py: sama, untuk sheet `Copy of DAPODIK` (Dapodik PAUD)
           csvform_prepare.py: sama, untuk CSV PHDT (SITB TB 01/TB 02, ELSMIL x3, SIPTM, ASIK Skrining PTM)
           phdt2_prepare.py: sama, untuk PHDT_ASIK_CKG.xlsx (5 form CKG, beberapa versi) + CSV Informed Consent, SiHepi Rekap 3e, eKohort ANC/INC, Buku KIA 2024 (ANC/INC/PNC/Anak), SITB TB 15/15P, ASIK Kohort. kuapps_prepare.py: KuApps BidanKu / Spheres / Genomics / MMS (xlsx); phdt2_prepare.py juga untuk Kobo SDIDTK
           sigizi_prepare.py: sama, untuk PHDT_SIGIZI.xlsx + schema BQ (17 form SiGizi selain ANC), sekaligus isi Nama Column BQ
           sismal_prepare.py: sama, untuk PHDT_SISMAL.xlsx (SISMAL Regmal 1, Validasi Kasus Indigenous)
```

## Form yang sudah dihitung

Maternal Outcome, Raffle (Kobo) · SiGizi ANC · SITB TB 06, TB 03 SO, TB 03 RO, TB 04 (Fasyankes & Rujukan), TB 16K · MPDN Kematian Bayi, Kematian Ibu · 11 form ePuskesmas (Pelayanan, Kunjungan Ibu Hamil, Laboratorium, Rujukan Eksternal, ANC, INC, PNC, MTBS, MTBM, Tumbang Anak, DDTK, KPSP, TDD, TDL, KMPE, M-CHAT-R, GPPH; ⚠️ belum comprehensive review) · Dapodik PAUD (⚠️ belum comprehensive review). Angka terbaru ada di [`output.md`](output.md), status per form di [`form-tracker.md`](form-tracker.md). · SITB TB 01, TB 02, ELSMIL (Ibu Hamil, Pasca Persalinan, Baduta), SIPTM, ASIK Skrining PTM (⚠️ belum comprehensive review) · SISMAL Regmal 1 dan Validasi Kasus Indigenous (⚠️ belum comprehensive review) · ASIK CKG (BBL, Balita, Dewasa Laki-laki, Dewasa Perempuan, Lansia; versi terbaru dipakai, versi lain di `output.md`), Informed Consent, SiHepi Rekap 3e, eKohort ANC dan INC (⚠️ belum comprehensive review)

## Menambah form baru

Ikuti checklist di [`aturan.md`](aturan.md#checklist-setiap-form-baru). Singkatnya:

1. Minta daftar variabel BQ form tersebut. Kalau ada file mentah, buat `raw/<form>-kolom.md`.
2. Cek tally: semua variabel BQ harus masuk ke salah satu payload.
3. Isi kolom `Nama Column BQ`, `jumlah instance`, dan `jumlah code` di dictionary `mapping/`.
4. Buat output per form:
   ```
   python3 scripts/form_output.py mapping/<sumber>-data-dictionary-<form>.csv "<Nama Form>" output/<form>.md [raw/<form>-kolom.md]
   ```
5. Update `output.md`, `frekuensi-payload.md`, `frekuensi-code.md`, dan `revisi.md`.
6. Ubah **Status review** form itu jadi ✅ di `form-tracker.md` dan di Sheet.

## Konvensi

- Payload = 1 resource FHIR yang dibuat dari submission form, identitasnya resource + determining code.
- Organization, Location, dan PractitionerRole yang hanya di-lookup ke master data tidak dihitung (detail dan pengecualian di `aturan.md`).
- Extension custom memakai prefix `http://terminology.kemkes.go.id/sp/`. Code `SPxxx` memakai CodeSystem `http://terminology.kemkes.go.id/sp`, code `TKxxx` memakai `http://terminology.kemkes.go.id`.

- 2026-11-24: Tambah 34 form SIM RS (`scripts/rs_prepare.py`, `mapping/phdt-data-dictionary-rs-*.csv`, `output/rs-*.md`) dari `PHDT_Data_Rumah_Sakit.xlsx`. ⚠️ belum comprehensive review.
