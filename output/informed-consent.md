# Output Form: Informed Consent

Sumber: `mapping/phdt-data-dictionary-informed-consent.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-informed-consent.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 3 |
| Code (`jumlah code` = 1) | 8 |
| Code unik (code + CodeSystem) | 8 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 8 |
| Variabel BQ (unik) | 15 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 3–13 | Patient | – | – | `nama_responden, nama_pasien` → `Patient.name.text` (3)<br>`nik, nik_diwakilkan` → `Patient.identifier.value` (5)<br>`tgl_lahir_pasien` → `Patient.birthDate` (8)<br>`no_hp` → `Patient.telecom.value` (11)<br>`alamat` → `Patient.address.line` (13) |
| 2 | 15–63 | Consent | – | – | `menyetujui` → `Consent.status` (15)<br>`menyetujui` → `Consent.status` (16)<br>`nama_responden, nama_pasien` → `Consent.patient.reference` (19)<br>`tanggal_ic` → `Consent.dateTime` (20)<br>`status_responden` → `Consent.performer.reference` (21)<br>`status_responden` → `Consent.performer.reference` (22)<br>`faskes_id` → `Consent.organization.reference` (23)<br>`nama_faskes` → `Consent.organization.display` (24)<br>_Tanda Tangan Responden_ → `Consent.sourceAttachment[0].url` (26, tanpa BQ)<br>_Tanda Tangan Pemberi Penjelasan_ → `Consent.sourceAttachment[1].url` (28, tanpa BQ)<br>_Dokumen Pendukung 1_ → `Consent.sourceAttachment[2].url` (30, tanpa BQ)<br>_Dokumen Pendukung 2_ → `Consent.sourceAttachment[3].url` (32, tanpa BQ)<br>_Dokumen Pendukung 3_ → `Consent.sourceAttachment[4].url` (34, tanpa BQ)<br>_Dokumen Pendukung 4_ → `Consent.sourceAttachment[5].url` (36, tanpa BQ)<br>`nama_pemateri` → `Consent.provision.actor.display` (38)<br>_Klausul Persetujuan 1_ → `Consent.provision.provision[0].code.coding` (40, tanpa BQ)<br>_Klausul Persetujuan 2_ → `Consent.provision.provision[1].code.coding` (43, tanpa BQ)<br>_Klausul Persetujuan 3_ → `Consent.provision.provision[2].code.coding` (46, tanpa BQ)<br>_Klausul Persetujuan 4_ → `Consent.provision.provision[3].code.coding` (49, tanpa BQ)<br>_Klausul Persetujuan 5_ → `Consent.provision.provision[4].code.coding` (52, tanpa BQ)<br>_Klausul Persetujuan 6_ → `Consent.provision.provision[5].code.coding` (55, tanpa BQ)<br>_Klausul Persetujuan 7_ → `Consent.provision.provision[6].code.coding` (58, tanpa BQ)<br>_Klausul Persetujuan 8_ → `Consent.provision.provision[7].code.coding` (61, tanpa BQ) |
| 3 | 65–72 | RelatedPerson | – | – | `nama_responden` → `RelatedPerson.name.text` (67)<br>`nik` → `RelatedPerson.identifier.value` (68)<br>_Tanggal Lahir Wali_ → `RelatedPerson.birthDate` (71, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Patient | 1 |
| Consent | 1 |
| RelatedPerson | 1 |
| **Total** | **3** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 40 | Consent | `Consent.provision.provision[0].code.coding` | SP000840 | Persetujuan IC 1 | http://terminology.kemkes.go.id/sp |
| 2 | 43 | Consent | `Consent.provision.provision[1].code.coding` | SP000841 | Persetujuan IC 2 | http://terminology.kemkes.go.id/sp |
| 3 | 46 | Consent | `Consent.provision.provision[2].code.coding` | SP000842 | Persetujuan IC 3 | http://terminology.kemkes.go.id/sp |
| 4 | 49 | Consent | `Consent.provision.provision[3].code.coding` | SP000843 | Persetujuan IC 4 | http://terminology.kemkes.go.id/sp |
| 5 | 52 | Consent | `Consent.provision.provision[4].code.coding` | SP000844 | Persetujuan IC 5 | http://terminology.kemkes.go.id/sp |
| 6 | 55 | Consent | `Consent.provision.provision[5].code.coding` | SP000845 | Persetujuan IC 6 | http://terminology.kemkes.go.id/sp |
| 7 | 58 | Consent | `Consent.provision.provision[6].code.coding` | SP000846 | Persetujuan IC 7 | http://terminology.kemkes.go.id/sp |
| 8 | 61 | Consent | `Consent.provision.provision[7].code.coding` | SP000847 | Persetujuan IC 8 | http://terminology.kemkes.go.id/sp |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://terminology.kemkes.go.id/sp | 8 |
| **Total** | **8** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 14 | ⚠️ is_teen | Status Remaja (isTeen) | – | `` |
| 25 | ⚠️ kecamatan | – | – | `` |
| 64 | ⚠️ status_responden | Status Responden | – | `` |
