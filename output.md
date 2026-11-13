# Output Hitungan Payload & Code — Form Kobo

Terakhir diperbarui: 2026-11-13
Aturan hitung: lihat `aturan.md`
Form yang sudah dihitung:
- **Maternal Outcome** (sumber: `mapping/kobo-data-dictionary-maternal-outcome.csv`)
- **Raffle** (sumber: `mapping/kobo-data-dictionary-raffle.csv`)

Belum: ANC, PNC, form lain

---

## Ringkasan semua form

| Form | Payload | Jenis resource | Code |
|---|---|---|---|
| Maternal Outcome | 12 | 7 | 14 |
| Raffle | 7 | 7 | 6 |
| **Total unik (semua form)** | **15** | **8** | **19** |

---

## Frekuensi payload (lintas form)

| # | Resource | Code pembeda | Display | Dipakai di form | Frekuensi |
|---|---|---|---|---|---|
| 1 | PractitionerRole | – | – | Maternal Outcome | 1 |
| 2 | Practitioner | – | – | Maternal Outcome, Raffle | 2 |
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

## Form: Maternal Outcome — payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 5 |
| EpisodeOfCare | 2 (status finished, penutup episode di hari ke-43) |
| PractitionerRole | 1 |
| Practitioner | 1 |
| Patient | 1 |
| Encounter | 1 |
| Condition | 1 |
| **Total** | **12** |
| ~~Organization~~ | master data, tidak dihitung |
| ~~Location~~ | master data, tidak dihitung |

## Form: Raffle — payload per resource

| Resource | Jumlah | Pembeda / catatan |
|---|---|---|
| Patient | 1 | Nama Ibu, NIK Ibu, Nomor Telepon |
| Location | 1 | Lokasi/Fasilitas Kesehatan + Kecamatan + Kelurahan (dibuat dari form) |
| Practitioner | 1 | Nama Bidan Desa |
| EpisodeOfCare | 1 | ANC (dicari dulu; kalau tidak ada baru dibuat) |
| Encounter | 1 | Tanggal Kunjungan Pelayanan; Nama Data Entry di participant ADM (2 blok kamus = 1 payload) |
| Condition | 1 | SP001135 Presensi Posyandu (+ Keterangan di `.note`) |
| Observation | 1 | 385438008 Source of information (Input Data) |
| **Total** | **7** | |
| ~~Organization~~ | – | master data, tidak dihitung |

Code Raffle (6): ANC, SP001135, 385438008, SP000776 / SP000777 / SP000778 (value Input Data).

---

## Log perubahan output
- 2026-11-13: Raffle direvisi: Location dibuat dari form (payload jadi 7), Condition.code jadi SP001135. Total unik lintas form jadi 15 payload, 8 jenis resource, 19 code.
- 2026-11-13: Tambah form Raffle (6 payload, 6 baris code). Total unik lintas form jadi 14 payload, 18 code. Frekuensi Practitioner, Patient, Encounter, EpisodeOfCare ANC, dan code ANC naik jadi 2.
- 2026-11-13: Kolom "Code per submission" dihapus (tidak dipakai).
- 2026-11-13: Tabel frekuensi payload diberi kolom Code pembeda, Display, dan Variabel Kobo.
- 2026-11-13: Dicek ulang dengan Kobo_3. Angka tidak berubah (12 payload, 14 code). Display SP000396/SP000397 dibetulkan.
- 2026-11-13: File dipisah jadi `aturan.md`, `revisi.md`, `output.md`.
- 2026-11-13: Maternal Outcome dihitung. Repo dibersihkan; isi lama ada di commit `0aba562`.
