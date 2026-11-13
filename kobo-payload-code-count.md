# Hitungan Payload & Code — Form Kobo (living file)

Terakhir diperbarui: 2026-11-13
Form yang sudah dihitung: **Maternal Outcome**
Belum: ANC, PNC, form lain (tambahkan di bawah)

---

## Aturan hitung

**Payload (instance)**
- 1 payload = 1 resource FHIR yang dibuat dari submission form.
- Identitas payload = resource + determining code (mis. `Observation | SP000389`, `EpisodeOfCare | ANC`). Resource tanpa determining code (Patient, Practitioner, Encounter) identitasnya cukup nama resource.
- Encounter yang muncul di 2 blok kamus (data utama + statusHistory) = **1 payload**.
- **Patient dihitung.**
- **Organization dan Location TIDAK dihitung**: keduanya diambil dari master data (lookup/reference), bukan dibuat dari form.

**Determining code**
- Code yang menentukan identitas payload: `PractitionerRole.code`, `Condition.code`, `EpisodeOfCare.type`, `Observation.code`.
- Ditambah pilihan jawaban coded (`Observation.valueCodeableConcept`) dan opsi role PractitionerRole.
- Code tetap HL7 (status, category, class, participant.type, diagnosis.use, clinicalStatus, organization-type, physicalType) **tidak dihitung**.
- Bedakan: **code di kamus** (semua opsi) vs **code per submission** (hanya opsi yang terpilih).

**Frekuensi**
- **Frekuensi payload** = di berapa form payload yang sama (resource + determining code) dipakai.
- **Frekuensi code** = di berapa form code yang sama (code + CodeSystem) dipakai.
- Contoh: kalau SP000389 nanti juga dipakai di form PNC, frekuensinya jadi 2.

**Kolom di data dictionary**
- `jumlah instance` = isi 1 di baris pertama setiap payload.
- `jumlah code` = isi 1 di setiap baris determining code / opsi coded.

---

## Ringkasan semua form

| Form | Payload | Jenis resource | Code di kamus | Code per submission |
|---|---|---|---|---|
| Maternal Outcome | 12 | 7 | 14 | 10 |
| **Total unik (semua form)** | **12** | **7** | **14** | – |

> Kalau form baru ditambahkan, hitung ulang baris "Total unik": payload/code yang sama di beberapa form hanya dihitung sekali, lalu naikkan frekuensinya di tabel di bawah.

---

## Frekuensi payload (lintas form)

| # | Payload (resource + pembeda) | Dipakai di form | Frekuensi |
|---|---|---|---|
| 1 | PractitionerRole | Maternal Outcome | 1 |
| 2 | Practitioner | Maternal Outcome | 1 |
| 3 | Patient | Maternal Outcome | 1 |
| 4 | Encounter | Maternal Outcome | 1 |
| 5 | Condition \| SP000738 | Maternal Outcome | 1 |
| 6 | EpisodeOfCare \| ANC | Maternal Outcome | 1 |
| 7 | EpisodeOfCare \| PNC | Maternal Outcome | 1 |
| 8 | Observation \| SP000389 (Keadaan Ibu) | Maternal Outcome | 1 |
| 9 | Observation \| 93857-1 (Tgl Persalinan) | Maternal Outcome | 1 |
| 10 | Observation \| 81956-5 (Tgl Meninggal) | Maternal Outcome | 1 |
| 11 | Observation \| LT000005 (Tempat Meninggal) | Maternal Outcome | 1 |
| 12 | Observation \| 79378-6 (Penyebab Meninggal) | Maternal Outcome | 1 |

## Frekuensi code (lintas form)

| # | Code | Display | CodeSystem | Dipakai di form | Frekuensi |
|---|---|---|---|---|---|
| 1 | 223366009 | Healthcare professional | snomed | Maternal Outcome | 1 |
| 2 | SP000396 | (cek display, lihat temuan #2) | kemkes sp | Maternal Outcome | 1 |
| 3 | SP000397 | (cek display, lihat temuan #2) | kemkes sp | Maternal Outcome | 1 |
| 4 | SP000738 | Kunjungan pemantauan luaran maternal | kemkes sp | Maternal Outcome | 1 |
| 5 | ANC | Antenatal Care | episodeofcare-type | Maternal Outcome | 1 |
| 6 | PNC | Postnatal Care | episodeofcare-type | Maternal Outcome | 1 |
| 7 | SP000389 | Keadaan Ibu | kemkes sp | Maternal Outcome | 1 |
| 8 | 102514002 | Well female adult | snomed | Maternal Outcome | 1 |
| 9 | 39104002 | Illness | snomed | Maternal Outcome | 1 |
| 10 | 419099009 | Dead | snomed | Maternal Outcome | 1 |
| 11 | 93857-1 | Date and time of obstetric delivery | loinc | Maternal Outcome | 1 |
| 12 | 81956-5 | Date and time of death | loinc | Maternal Outcome | 1 |
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

## Form: Maternal Outcome

### Payload per resource

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

### Koreksi kolom `jumlah instance` di dictionary

| Baris CSV | Sekarang | Seharusnya |
|---|---|---|
| 12 (baris kosong) | 1 | kosong (pindahkan ke baris Patient) |
| 13 (Patient.name.text) | kosong | 1 |
| Organization / Location | kosong | tetap kosong (master data) |

Setelah koreksi: total = 12.

### Temuan mapping (status: open)

| # | Temuan | Status |
|---|---|---|
| 1 | Keadaan Ibu: Value Name bergeser 1 baris (sehat→Illness, sakit→Dead). Seharusnya sehat→102514002, sakit→39104002, meninggal→419099009 | open |
| 2 | PractitionerRole: display SP000396 / SP000397 tertukar dengan value name | open |
| 3 | Typo `ofiicial` di Practitioner.identifier | open |
| 4 | Baris 45: path `Organization.address.extension.url` di blok Location | open |
| 5 | URL organization-type ada spasi di akhir | open |

---

## Log perubahan

- 2026-11-13: Frekuensi payload/code didefinisikan ulang jadi "dipakai di berapa form". Tabel frekuensi dipindah ke bagian lintas form.
- 2026-11-13: Dibuat. Maternal Outcome dihitung. Aturan: Patient masuk, Organization & Location tidak (master data). Repo dibersihkan; isi lama ada di commit `0aba562`.
