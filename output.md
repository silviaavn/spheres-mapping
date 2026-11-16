# Output Hitungan Payload & Code — Form Kobo

Terakhir diperbarui: 2026-11-13
Aturan hitung: lihat `aturan.md`
Form yang sudah dihitung (detail per form, bisa ditelusuri per baris):
- **Maternal Outcome** → `output/maternal-outcome.md` (sumber: `mapping/kobo-data-dictionary-maternal-outcome.csv`)
- **Raffle** → `output/raffle.md` (sumber: `mapping/kobo-data-dictionary-raffle.csv`)

File ini adalah **konsolidasi** lintas form. Angka per form di sini harus sama dengan file `output/<form>.md`.

Belum: ANC, PNC, form lain

---

## Ringkasan semua form

| Form | Payload | Code |
|---|---|---|
| Maternal Outcome | 12 | 14 |
| Raffle | 8 | 6 |
| **Total (non-unik)** | **20** | **20** |
| **Total unik** | **15** | **19** |
| Selisih (dipakai ulang) | 5 | 1 |

---

## Frekuensi payload (lintas form)

| # | Resource | Code pembeda | Display | Dipakai di form | Frekuensi |
|---|---|---|---|---|---|
| 1 | PractitionerRole | – | – | Maternal Outcome | 1 |
| 2 | Practitioner | – | – | Maternal Outcome, Raffle (2x: bidan desa + data entry) | 2 |
| 3 | Patient | – | – | Maternal Outcome, Raffle | 2 |
| 4 | Encounter | – | – | Maternal Outcome, Raffle | 2 |
| 5 | Location | – | – | Raffle | 1 |
| 6 | Condition | SP000738 | Kunjungan pemantauan luaran maternal | Maternal Outcome | 1 |
| 7 | Condition | SP001135 | Presensi Posyandu | Raffle | 1 |
| 8 | EpisodeOfCare | ANC | Antenatal Care | Maternal Outcome, Raffle | 2 |
| 9 | EpisodeOfCare | PNC | Postnatal Care | Maternal Outcome | 1 |
| 10 | Observation | SP000389 | Keadaan Ibu | Maternal Outcome | 1 |
| 11 | Observation | 93857-1 | Date and time of obstetric delivery | Maternal Outcome | 1 |
| 12 | Observation | 81956-5 | Date and time of death [TimeStamp] | Maternal Outcome | 1 |
| 13 | Observation | LT000005 | Alamat Mati | Maternal Outcome | 1 |
| 14 | Observation | 79378-6 | Cause of death | Maternal Outcome | 1 |
| 15 | Observation | 385438008 | Source of information | Raffle | 1 |

Variabel Kobo / BQ per payload: lihat tabel tally BQ di `revisi.md`.

## Frekuensi code (lintas form)

| # | Code | Display | CodeSystem | Dipakai di form | Frekuensi |
|---|---|---|---|---|---|
| 1 | 223366009 | Healthcare professional | snomed | Maternal Outcome | 1 |
| 2 | SP000396 | Data entry staff | kemkes sp | Maternal Outcome | 1 |
| 3 | SP000397 | Field/call center staff | kemkes sp | Maternal Outcome | 1 |
| 4 | SP000738 | Kunjungan pemantauan luaran maternal | kemkes sp | Maternal Outcome | 1 |
| 5 | ANC | Antenatal Care | episodeofcare-type | Maternal Outcome, Raffle | 2 |
| 6 | PNC | Postnatal Care | episodeofcare-type | Maternal Outcome | 1 |
| 7 | SP000389 | Keadaan Ibu | kemkes sp | Maternal Outcome | 1 |
| 8 | 102514002 | Well female adult | snomed | Maternal Outcome | 1 |
| 9 | 39104002 | Illness | snomed | Maternal Outcome | 1 |
| 10 | 419099009 | Dead | snomed | Maternal Outcome | 1 |
| 11 | 93857-1 | Date and time of obstetric delivery | loinc | Maternal Outcome | 1 |
| 12 | 81956-5 | Date and time of death [TimeStamp] | loinc | Maternal Outcome | 1 |
| 13 | LT000005 | Alamat Mati | location-type | Maternal Outcome | 1 |
| 14 | 79378-6 | Cause of death | loinc | Maternal Outcome | 1 |
| 15 | SP001135 | Presensi Posyandu | kemkes sp | Raffle | 1 |
| 16 | 385438008 | Source of information | snomed | Raffle | 1 |
| 17 | SP000776 | Sigizi | kemkes sp | Raffle | 1 |
| 18 | SP000777 | E-pus PKD | kemkes sp | Raffle | 1 |
| 19 | SP000778 | E-pus | kemkes sp | Raffle | 1 |

## Jumlah per CodeSystem (code unik lintas form)

| CodeSystem | Jumlah | Code |
|---|---|---|
| http://terminology.kemkes.go.id/sp | 8 | SP000396, SP000397, SP000738, SP000389, SP001135, SP000776, SP000777, SP000778 |
| http://snomed.info/sct | 5 | 223366009, 102514002, 39104002, 419099009, 385438008 |
| http://loinc.org | 3 | 93857-1, 81956-5, 79378-6 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 2 | ANC, PNC |
| http://terminology.kemkes.go.id/CodeSystem/location-type | 1 | LT000005 |
| **Total** | **19** | |

---

## Payload per resource (semua form)

| Resource | Maternal Outcome | Raffle | Total (non-unik) | Total unik | Pembeda (unik) |
|---|---|---|---|---|---|
| Observation | 5 | 1 | 6 | 6 | SP000389, 93857-1, 81956-5, LT000005, 79378-6, 385438008 |
| EpisodeOfCare | 2 | 1 | 3 | 2 | ANC, PNC |
| Condition | 1 | 1 | 2 | 2 | SP000738, SP001135 |
| Patient | 1 | 1 | 2 | 1 | – |
| Practitioner | 1 | 2 | 3 | 1 | – (Raffle: bidan desa + data entry) |
| Encounter | 1 | 1 | 2 | 1 | – |
| PractitionerRole | 1 | – | 1 | 1 | – |
| Location | – | 1 | 1 | 1 | – |
| **Total** | **12** | **8** | **20** | **15** | |

Catatan:
- Organization tidak dihitung di semua form (lookup master data, bloknya tidak ditulis di dictionary). Location di Maternal Outcome juga lookup (tidak dihitung), tapi di Raffle dihitung karena dibuat dari form.
- EpisodeOfCare: Maternal Outcome = ANC & PNC ditutup (finished, hari ke-43); Raffle = ANC dicari dulu, kalau tidak ada baru dibuat.
- Encounter muncul di 2 blok kamus (data utama + statusHistory) = 1 payload.

---

## Log perubahan output
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
