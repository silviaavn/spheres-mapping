# Hitungan Payload & Code — Form Kobo (living file)

Terakhir diperbarui: 2026-11-13
Form yang sudah dihitung: **Maternal Outcome**
Belum: ANC, PNC, form lain (tambahkan di bawah)

---

## Aturan hitung

**Payload (instance)**
- 1 payload = 1 resource FHIR yang dibuat dari submission form.
- Resource yang sama tapi beda pembeda (mis. EpisodeOfCare ANC vs PNC, Observation beda `code`) = payload berbeda.
- Encounter yang muncul di 2 blok kamus (data utama + statusHistory) = **1 payload**.
- **Patient dihitung.**
- **Organization dan Location TIDAK dihitung**: keduanya diambil dari master data (lookup/reference), bukan dibuat dari form.

**Determining code**
- Code yang menentukan identitas payload: `PractitionerRole.code`, `Condition.code`, `EpisodeOfCare.type`, `Observation.code`.
- Ditambah pilihan jawaban coded (`Observation.valueCodeableConcept`) dan opsi role PractitionerRole.
- Code tetap HL7 (status, category, class, participant.type, diagnosis.use, clinicalStatus, organization-type, physicalType) **tidak dihitung**.
- Bedakan: **code di kamus** (semua opsi) vs **code per submission** (hanya opsi yang terpilih).

**Kolom di data dictionary**
- `jumlah instance` = isi 1 di baris pertama setiap payload.
- `jumlah code` = isi 1 di setiap baris determining code / opsi coded.

---

## Ringkasan semua form

| Form | Payload | Jenis resource | Code di kamus | Code per submission |
|---|---|---|---|---|
| Maternal Outcome | 12 | 7 | 14 | 10 |
| **Total unik (semua form)** | **12** | **7** | **14** | – |

> Kalau form baru ditambahkan, hitung ulang baris "Total unik": payload/code yang sama di beberapa form hanya dihitung sekali.

---

## Form: Maternal Outcome

### Frekuensi payload

| Resource | Jumlah | Pembeda |
|---|---|---|
| Observation | 5 | Keadaan Ibu (SP000389), Tgl Persalinan (93857-1), Tgl Meninggal (81956-5), Tempat Meninggal (LT000005), Penyebab Meninggal (79378-6) |
| EpisodeOfCare | 2 | ANC, PNC (status finished — penutup episode di hari ke-43) |
| PractitionerRole | 1 | |
| Practitioner | 1 | |
| Patient | 1 | |
| Encounter | 1 | |
| Condition | 1 | SP000738 |
| **Total** | **12** | |
| ~~Organization~~ | – | master data, tidak dihitung |
| ~~Location~~ | – | master data, tidak dihitung |

### Frekuensi code (semua muncul 1x)

| Resource | Code |
|---|---|
| PractitionerRole | 223366009, SP000396, SP000397 (pilih 1) |
| Condition | SP000738 |
| EpisodeOfCare | ANC, PNC |
| Observation (code) | SP000389, 93857-1, 81956-5, LT000005, 79378-6 |
| Observation (value Keadaan Ibu) | 102514002, 39104002, 419099009 (pilih 1) |

### Jumlah per CodeSystem

| CodeSystem | Jumlah | Code |
|---|---|---|
| http://snomed.info/sct | 4 | 223366009, 102514002, 39104002, 419099009 |
| http://terminology.kemkes.go.id/sp | 4 | SP000396, SP000397, SP000738, SP000389 |
| http://loinc.org | 3 | 93857-1, 81956-5, 79378-6 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 2 | ANC, PNC |
| http://terminology.kemkes.go.id/CodeSystem/location-type | 1 | LT000005 |
| **Total** | **14** | |

### Koreksi kolom `jumlah instance` di dictionary

| Baris CSV | Sekarang | Seharusnya |
|---|---|---|
| 12 (baris kosong) | 1 | kosong — pindahkan ke baris Patient |
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

- 2026-11-13 — Dibuat. Maternal Outcome dihitung. Aturan: Patient masuk, Organization & Location tidak (master data). Repo dibersihkan; isi lama ada di commit `0aba562`.
