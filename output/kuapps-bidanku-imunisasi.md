# Output Form: KuApps BidanKu - Imunisasi

Sumber: `mapping/phdt-data-dictionary-kuapps-bidanku-imunisasi.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-kuapps-bidanku-imunisasi.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 23 |
| Code (`jumlah code` = 1) | 52 |
| Code unik (code + CodeSystem) | 16 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 0 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–18 | Immunization | – | – | _Hepatitis B 0 (HepB 0)_ → `Immunization.status` (2, tanpa BQ)<br>_Tempat imunisasi dilakukan_ → `Immunization.location.display` (15, tanpa BQ)<br>_BCG_ → `Immunization.status` (16, tanpa BQ) |
| 2 | 19–32 | Immunization | – | – | _Tempat imunisasi dilakukan_ → `Immunization.location.display` (29, tanpa BQ)<br>_Polio Tetes 1 (OPV 1)_ → `Immunization.status` (30, tanpa BQ) |
| 3 | 33–47 | Immunization | – | – | _Tempat imunisasi dilakukan_ → `Immunization.location.display` (44, tanpa BQ)<br>_Dpt-Hb-Hib 1_ → `Immunization.status` (45, tanpa BQ) |
| 4 | 48–64 | Immunization | – | – | _Tempat imunisasi dilakukan_ → `Immunization.location.display` (61, tanpa BQ)<br>_Polio tetes 2 (OPV 2)_ → `Immunization.status` (62, tanpa BQ) |
| 5 | 65–79 | Immunization | – | – | _Tempat imunisasi dilakukan_ → `Immunization.location.display` (76, tanpa BQ)<br>_PCV 1_ → `Immunization.status` (77, tanpa BQ) |
| 6 | 80–94 | Immunization | – | – | _Tempat imunisasi dilakukan_ → `Immunization.location.display` (91, tanpa BQ)<br>_Rotavirus 1_ → `Immunization.status` (92, tanpa BQ) |
| 7 | 95–109 | Immunization | – | – | _Tempat imunisasi dilakukan_ → `Immunization.location.display` (106, tanpa BQ)<br>_Dpt-Hb-Hib 2_ → `Immunization.status` (107, tanpa BQ) |
| 8 | 110–126 | Immunization | – | – | _Tempat imunisasi dilakukan_ → `Immunization.location.display` (123, tanpa BQ)<br>_Polio tetes 3 (OPV 3)_ → `Immunization.status` (124, tanpa BQ) |
| 9 | 127–141 | Immunization | – | – | _Tempat imunisasi dilakukan_ → `Immunization.location.display` (138, tanpa BQ)<br>_PCV 2_ → `Immunization.status` (139, tanpa BQ) |
| 10 | 142–156 | Immunization | – | – | _Tempat imunisasi dilakukan_ → `Immunization.location.display` (153, tanpa BQ)<br>_Rotavirus 2_ → `Immunization.status` (154, tanpa BQ) |
| 11 | 157–170 | Immunization | – | – | _Dpt-Hb-Hib 3_ → `Immunization.status` (168, tanpa BQ) |
| 12 | 171–186 | Immunization | – | – | _Polio tetes 4 (OPV 4)_ → `Immunization.status` (184, tanpa BQ) |
| 13 | 187–200 | Immunization | – | – | _Polio injeksi (IPV 1)_ → `Immunization.status` (198, tanpa BQ) |
| 14 | 201–214 | Immunization | – | – | _Rotavirus 3 (Booster)_ → `Immunization.status` (212, tanpa BQ) |
| 15 | 215–227 | Immunization | – | – | _Polio injeksi (IPV 2)_ → `Immunization.status` (225, tanpa BQ) |
| 16 | 228–241 | Immunization | – | – | _Campak Rubella (MR 1)_ → `Immunization.status` (239, tanpa BQ) |
| 17 | 242–254 | Immunization | – | – | _Japanese Enchepalitis (JE) 1_ → `Immunization.status` (252, tanpa BQ) |
| 18 | 255–267 | Immunization | – | – | _PCV 3_ → `Immunization.status` (265, tanpa BQ) |
| 19 | 268–281 | Immunization | – | – | _PCV 4 (Booster)_ → `Immunization.status` (279, tanpa BQ) |
| 20 | 282–294 | Immunization | – | – | _Dpt-Hb-Hib 4_ → `Immunization.status` (292, tanpa BQ) |
| 21 | 295–310 | Immunization | – | – | _Campak Rubella (MR 2)_ → `Immunization.status` (308, tanpa BQ) |
| 22 | 311–323 | Immunization | – | – | _Japanese Enchepalitis (JE) 2_ → `Immunization.status` (321, tanpa BQ) |
| 23 | 324–333 | Immunization | – | – | – |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Immunization | 23 |
| **Total** | **23** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 5 | Immunization | `Immunization.vaccineCode` | VG45 | HepB | http://sys-ids.kemkes.go.id/kfa |
| 2 | 19 | Immunization | `Immunization.vaccineCode` | VG19 | BCG | http://sys-ids.kemkes.go.id/kfa |
| 3 | 33 | Immunization | `Immunization.vaccineCode` | VG89 | POLIO | http://sys-ids.kemkes.go.id/kfa |
| 4 | 34 | Immunization | `Immunization.vaccineCode` | 178 | OPV | http://hl7.org/fhir/sid/cvx |
| 5 | 48 | Immunization | `Immunization.vaccineCode` | VG45 | HepB | http://sys-ids.kemkes.go.id/kfa |
| 6 | 49 | Immunization | `Immunization.vaccineCode` | VG17 | HIB | http://sys-ids.kemkes.go.id/kfa |
| 7 | 50 | Immunization | `Immunization.vaccineCode` | VG107 | DTAP | http://sys-ids.kemkes.go.id/kfa |
| 8 | 51 | Immunization | `Immunization.vaccineCode` | 198 | DTP-hepB-Hib Pentavalent Non-US | http://hl7.org/fhir/sid/cvx |
| 9 | 65 | Immunization | `Immunization.vaccineCode` | VG89 | POLIO | http://sys-ids.kemkes.go.id/kfa |
| 10 | 66 | Immunization | `Immunization.vaccineCode` | 178 | OPV | http://hl7.org/fhir/sid/cvx |
| 11 | 80 | Immunization | `Immunization.vaccineCode` | VG152 | PneumoPCV | http://sys-ids.kemkes.go.id/kfa |
| 12 | 81 | Immunization | `Immunization.vaccineCode` | 152 | Pneumococcal Conjugate, unspecified formulation | http://hl7.org/fhir/sid/cvx |
| 13 | 95 | Immunization | `Immunization.vaccineCode` | VG122 | ROTAVIRUS | http://sys-ids.kemkes.go.id/kfa |
| 14 | 96 | Immunization | `Immunization.vaccineCode` | 119 | rotavirus, monovalent | http://hl7.org/fhir/sid/cvx |
| 15 | 110 | Immunization | `Immunization.vaccineCode` | VG45 | HepB | http://sys-ids.kemkes.go.id/kfa |
| 16 | 111 | Immunization | `Immunization.vaccineCode` | VG17 | HIB | http://sys-ids.kemkes.go.id/kfa |
| 17 | 112 | Immunization | `Immunization.vaccineCode` | VG107 | DTAP | http://sys-ids.kemkes.go.id/kfa |
| 18 | 113 | Immunization | `Immunization.vaccineCode` | 198 | DTP-hepB-Hib Pentavalent Non-US | http://hl7.org/fhir/sid/cvx |
| 19 | 127 | Immunization | `Immunization.vaccineCode` | VG89 | POLIO | http://sys-ids.kemkes.go.id/kfa |
| 20 | 128 | Immunization | `Immunization.vaccineCode` | 178 | OPV | http://hl7.org/fhir/sid/cvx |
| 21 | 142 | Immunization | `Immunization.vaccineCode` | VG152 | PneumoPCV | http://sys-ids.kemkes.go.id/kfa |
| 22 | 143 | Immunization | `Immunization.vaccineCode` | 152 | Pneumococcal Conjugate, unspecified formulation | http://hl7.org/fhir/sid/cvx |
| 23 | 157 | Immunization | `Immunization.vaccineCode` | VG122 | ROTAVIRUS | http://sys-ids.kemkes.go.id/kfa |
| 24 | 158 | Immunization | `Immunization.vaccineCode` | 119 | rotavirus, monovalent | http://hl7.org/fhir/sid/cvx |
| 25 | 171 | Immunization | `Immunization.vaccineCode` | VG45 | HepB | http://sys-ids.kemkes.go.id/kfa |
| 26 | 172 | Immunization | `Immunization.vaccineCode` | VG17 | HIB | http://sys-ids.kemkes.go.id/kfa |
| 27 | 173 | Immunization | `Immunization.vaccineCode` | VG107 | DTAP | http://sys-ids.kemkes.go.id/kfa |
| 28 | 174 | Immunization | `Immunization.vaccineCode` | 198 | DTP-hepB-Hib Pentavalent Non-US | http://hl7.org/fhir/sid/cvx |
| 29 | 187 | Immunization | `Immunization.vaccineCode` | VG89 | POLIO | http://sys-ids.kemkes.go.id/kfa |
| 30 | 188 | Immunization | `Immunization.vaccineCode` | 178 | OPV | http://hl7.org/fhir/sid/cvx |
| 31 | 201 | Immunization | `Immunization.vaccineCode` | VG89 | POLIO | http://sys-ids.kemkes.go.id/kfa |
| 32 | 202 | Immunization | `Immunization.vaccineCode` | 10 | IPV | http://hl7.org/fhir/sid/cvx |
| 33 | 215 | Immunization | `Immunization.vaccineCode` | VG122 | ROTAVIRUS | http://sys-ids.kemkes.go.id/kfa |
| 34 | 216 | Immunization | `Immunization.vaccineCode` | 119 | rotavirus, monovalent | http://hl7.org/fhir/sid/cvx |
| 35 | 228 | Immunization | `Immunization.vaccineCode` | VG89 | POLIO | http://sys-ids.kemkes.go.id/kfa |
| 36 | 229 | Immunization | `Immunization.vaccineCode` | 10 | IPV | http://hl7.org/fhir/sid/cvx |
| 37 | 242 | Immunization | `Immunization.vaccineCode` | VG03 | MMR | http://sys-ids.kemkes.go.id/kfa |
| 38 | 243 | Immunization | `Immunization.vaccineCode` | 04 | M/R | http://hl7.org/fhir/sid/cvx |
| 39 | 255 | Immunization | `Immunization.vaccineCode` | VG129 | Japanese encephalitis | http://sys-ids.kemkes.go.id/kfa |
| 40 | 256 | Immunization | `Immunization.vaccineCode` | 134 | Japanese Encephalitis IM | http://hl7.org/fhir/sid/cvx |
| 41 | 268 | Immunization | `Immunization.vaccineCode` | VG152 | PneumoPCV | http://sys-ids.kemkes.go.id/kfa |
| 42 | 269 | Immunization | `Immunization.vaccineCode` | 152 | Pneumococcal Conjugate, unspecified formulation | http://hl7.org/fhir/sid/cvx |
| 43 | 282 | Immunization | `Immunization.vaccineCode` | VG152 | PneumoPCV | http://sys-ids.kemkes.go.id/kfa |
| 44 | 283 | Immunization | `Immunization.vaccineCode` | 152 | Pneumococcal Conjugate, unspecified formulation | http://hl7.org/fhir/sid/cvx |
| 45 | 295 | Immunization | `Immunization.vaccineCode` | VG45 | HepB | http://sys-ids.kemkes.go.id/kfa |
| 46 | 296 | Immunization | `Immunization.vaccineCode` | VG17 | HIB | http://sys-ids.kemkes.go.id/kfa |
| 47 | 297 | Immunization | `Immunization.vaccineCode` | VG107 | DTAP | http://sys-ids.kemkes.go.id/kfa |
| 48 | 298 | Immunization | `Immunization.vaccineCode` | 198 | DTP-hepB-Hib Pentavalent Non-US | http://hl7.org/fhir/sid/cvx |
| 49 | 311 | Immunization | `Immunization.vaccineCode` | VG03 | MMR | http://sys-ids.kemkes.go.id/kfa |
| 50 | 312 | Immunization | `Immunization.vaccineCode` | 04 | M/R | http://hl7.org/fhir/sid/cvx |
| 51 | 324 | Immunization | `Immunization.vaccineCode` | VG129 | Japanese encephalitis | http://sys-ids.kemkes.go.id/kfa |
| 52 | 325 | Immunization | `Immunization.vaccineCode` | 134 | Japanese Encephalitis IM | http://hl7.org/fhir/sid/cvx |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://sys-ids.kemkes.go.id/kfa | 31 |
| http://hl7.org/fhir/sid/cvx | 21 |
| **Total** | **52** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
