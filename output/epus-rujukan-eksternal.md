# Output Form: ePuskesmas Rujukan Eksternal

Sumber: `mapping/phdt-data-dictionary-epus-rujukan-eksternal.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-epus-rujukan-eksternal.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 5 |
| Code (`jumlah code` = 1) | 0 |
| Code unik (code + CodeSystem) | 0 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 0 |
| Variabel BQ (unik) | 0 |
| Variabel raw (variabel dictionary; belum ada file mentah) | 23 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 3–4 | Encounter | – | – | _Tanggal_ → `Encounter.period.start` (3, tanpa BQ)<br>_Asal Faskes_ → `Encounter.serviceProvider.reference` (29, tanpa BQ)<br>_Poli Perujuk_ → `Enounter.location.reference` (43, tanpa BQ) |
| 2 | 5–28 | Patient | – | – | _Nama Pasien_ → `Patient.name` (5, tanpa BQ)<br>_No. eRM_ → `Patient.identifier.value` (8, tanpa BQ)<br>_NIK_ → `Patient.identifier.value` (11, tanpa BQ)<br>_No. RM Lama_ → `Patient.name` (12, tanpa BQ)<br>_No. Dokumen RM_ → `Patient.name` (15, tanpa BQ)<br>_Tempat & Tgl.Lahir_ → `Patient.extension:birthPlace` (18, tanpa BQ)<br>_Umur_ → `Patient.birthDate` (20, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (21, tanpa BQ)<br>_Alamat_ → `Patient.address.line` (23, tanpa BQ)<br>_RT_ → `Patient.address.line` (25, tanpa BQ)<br>_RW_ → `Patient.address.line` (26, tanpa BQ)<br>_Kelurahan_ → `Patient.address.extension:administrativeCode.extension:village` (27, tanpa BQ) |
| 3 | 31–37 | Coverage | – | – | _Asuransi_ → `Coverage.subsriberId` (31, tanpa BQ)<br>_No. Asuransi_ → `Coverage.identifier.system` (37, tanpa BQ) |
| 4 | 38–42 | Condition | – | – | _Diagnosa_ → `Condition.category.coding` (38, tanpa BQ) |
| 5 | 44–47 | ServiceRequest | – | – | _Dokter / Tenaga Medis Perujuk_ → `ServiceRequest.requester.reference` (44, tanpa BQ)<br>_RS Tujuan Rujukan_ → `ServiceRequest.performer.reference` (45, tanpa BQ)<br>_Poli Tujuan Rujukan_ → `ServiceRequest.performerType.coding` (46, tanpa BQ)<br>_No. Rujukan BPJS_ → `ServiceRequest.identifier` (47, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Encounter | 1 |
| Patient | 1 |
| Coverage | 1 |
| Condition | 1 |
| ServiceRequest | 1 |
| **Total** | **5** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| **Total** | **0** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 2 | – | No. | – | `` |
