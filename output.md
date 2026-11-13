# Output Hitungan Payload & Code — Form Kobo

Terakhir diperbarui: 2026-11-13 (sumber: `mapping/kobo-data-dictionary-maternal-outcome.csv`)
Aturan hitung: lihat `aturan.md`
Form yang sudah dihitung: **Maternal Outcome**
Belum: ANC, PNC, form lain

---

## Ringkasan semua form

| Form | Payload | Jenis resource | Code |
|---|---|---|---|
| Maternal Outcome | 12 | 7 | 14 |
| **Total unik (semua form)** | **12** | **7** | **14** |

---

## Frekuensi payload (lintas form)

| # | Resource | Code pembeda | Display | Variabel Kobo | Dipakai di form | Frekuensi |
|---|---|---|---|---|---|---|
| 1 | PractitionerRole | – | – | Siapa yang melakukan entry data? | Maternal Outcome | 1 |
| 2 | Practitioner | – | – | Nama / NIK yang melakukan entry data | Maternal Outcome | 1 |
| 3 | Patient | – | – | Nama Ibu / NIK Ibu | Maternal Outcome | 1 |
| 4 | Encounter | – | – | Tanggal Pencatatan | Maternal Outcome | 1 |
| 5 | Condition | SP000738 | Kunjungan pemantauan luaran maternal | – | Maternal Outcome | 1 |
| 6 | EpisodeOfCare | ANC | Antenatal Care | – | Maternal Outcome | 1 |
| 7 | EpisodeOfCare | PNC | Postnatal Care | – | Maternal Outcome | 1 |
| 8 | Observation | SP000389 | Keadaan Ibu | Keadaan Ibu | Maternal Outcome | 1 |
| 9 | Observation | 93857-1 | Date and time of obstetric delivery | Tanggal Persalinan | Maternal Outcome | 1 |
| 10 | Observation | 81956-5 | Date and time of death [TimeStamp] | Tanggal Meninggal | Maternal Outcome | 1 |
| 11 | Observation | LT000005 | Alamat Mati | Tempat Meninggal | Maternal Outcome | 1 |
| 12 | Observation | 79378-6 | Cause of death | Penyebab Meninggal | Maternal Outcome | 1 |

## Frekuensi code (lintas form)

| # | Code | Display | CodeSystem | Dipakai di form | Frekuensi |
|---|---|---|---|---|---|
| 1 | 223366009 | Healthcare professional | snomed | Maternal Outcome | 1 |
| 2 | SP000396 | Data entry staff | kemkes sp | Maternal Outcome | 1 |
| 3 | SP000397 | Field/call center staff | kemkes sp | Maternal Outcome | 1 |
| 4 | SP000738 | Kunjungan pemantauan luaran maternal | kemkes sp | Maternal Outcome | 1 |
| 5 | ANC | Antenatal Care | episodeofcare-type | Maternal Outcome | 1 |
| 6 | PNC | Postnatal Care | episodeofcare-type | Maternal Outcome | 1 |
| 7 | SP000389 | Keadaan Ibu | kemkes sp | Maternal Outcome | 1 |
| 8 | 102514002 | Well female adult | snomed | Maternal Outcome | 1 |
| 9 | 39104002 | Illness | snomed | Maternal Outcome | 1 |
| 10 | 419099009 | Dead | snomed | Maternal Outcome | 1 |
| 11 | 93857-1 | Date and time of obstetric delivery | loinc | Maternal Outcome | 1 |
| 12 | 81956-5 | Date and time of death [TimeStamp] | loinc | Maternal Outcome | 1 |
| 13 | LT000005 | Alamat Mati | location-type | Maternal Outcome | 1 |
| 14 | 79378-6 | Cause of death | loinc | Maternal Outcome | 1 |

## Jumlah per CodeSystem (code unik lintas form)

| CodeSystem | Jumlah | Code |
|---|---|---|
| http://snomed.info/sct | 4 | 223366009, 102514002, 39104002, 419099009 |
| http://terminology.kemkes.go.id/sp | 4 | SP000396, SP000397, SP000738, SP000389 |
| http://loinc.org | 3 | 93857-1, 81956-5, 79378-6 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 2 | ANC, PNC |
| http://terminology.kemkes.go.id/CodeSystem/location-type | 1 | LT000005 |
| **Total** | **14** | |

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

---

## Log perubahan output
- 2026-11-13: Kolom "Code per submission" dihapus (tidak dipakai).
- 2026-11-13: Tabel frekuensi payload diberi kolom Code pembeda, Display, dan Variabel Kobo.
- 2026-11-13: Dicek ulang dengan Kobo_3. Angka tidak berubah (12 payload, 14 code). Display SP000396/SP000397 dibetulkan.
- 2026-11-13: File dipisah jadi `aturan.md`, `revisi.md`, `output.md`.
- 2026-11-13: Maternal Outcome dihitung. Repo dibersihkan; isi lama ada di commit `0aba562`.
