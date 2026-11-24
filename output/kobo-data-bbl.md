# Output Form: Kobo Data BBL (belum ada baris tracker)

Sumber: `mapping/phdt-data-dictionary-kobo-data-bbl.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-kobo-data-bbl.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 38 |
| Code (`jumlah code` = 1) | 124 |
| Code unik (code + CodeSystem) | 86 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 2 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–14 | Patient | – | – | _Nama Bayi_ → `Patient.name.text` (2, tanpa BQ)<br>_NIK Bayi_ → `Patient.identifier.value` (5, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (10, tanpa BQ)<br>_Tanggal Lahir_ → `Patient.birthDate` (12, tanpa BQ)<br>_Tempat lahir_ → `Patient.extension:birthPlace` (13, tanpa BQ)<br>_Kembar_ → `Patient.multipleBirthBoolean` (14, tanpa BQ) |
| 2 | 15–25 | RelatedPerson | – | – | _Nama Ibu_ → `RelatedPerson.name.text` (16, tanpa BQ)<br>_No Hp Ibu_ → `RelatedPerson.telecom.value` (18, tanpa BQ)<br>_NIK Ibu_ → `RelatedPerson.identifier.value` (24, tanpa BQ) |
| 3 | 26–34 | RelatedPerson | – | – | _Nama Ayah_ → `RelatedPerson.name.text` (26, tanpa BQ)<br>_No Hp Ayah_ → `RelatedPerson.telecom.value` (28, tanpa BQ)<br>_NIK Ayah_ → `RelatedPerson.identifier.value` (34, tanpa BQ) |
| 4 | 35–43 | EpisodeOfCare | Neonate | Neonate | – |
| 5 | 44–58 | Encounter | – | – | _Tanggal Kunjungan_ → `Encounter.period.start` (488, tanpa BQ) |
| 6 | 59–66 | Condition | Z00.1 | Routine child health examination | – |
| 7 | 81–91 | Observation | 365475008.0 | Place in family order | _Anak ke_ → `Observation.valueInteger` (84, tanpa BQ) |
| 8 | 92–102 | Observation | 57715-5 | Birth time | _Jam Lahir_ → `Observation.valueTime` (95, tanpa BQ) |
| 9 | 103–117 | Observation | 76516-4 | Gestational age—​at birth | _Usia Gestasi Saat Lahir_ → `Observation.valueQuantity.value` (106, tanpa BQ) |
| 10 | 118–130 | Observation | 883-9 | ABO group [Type] in Blood | _Golongan darah_ → `Observation.valueCodeableConcept.coding` (121, tanpa BQ) |
| 11 | 131–142 | Observation | 10331-7 | Rh [Type] in Blood | _Rhesus_ → `Observation.valueCodeableConcept.coding` (134, tanpa BQ) |
| 12 | 143–154 | Observation | 8339-4 | Birth weight Measured | _Berat Badan Saat Lahir_ → `Observation.valueQuantity.value` (146, tanpa BQ) |
| 13 | 155–166 | Observation | 89269-5 | Body height Measured --at birth | _Panjang Badan Saat Lahir_ → `Observation.valueQuantity.value` (158, tanpa BQ) |
| 14 | 167–178 | Observation | 8290-9 | Head Occipital-frontal circumference --at birth- by Tape measure | _Lingkar Kepala Saat Lahir_ → `Observation.valueQuantity.value` (170, tanpa BQ) |
| 15 | 179–213 | Observation | 9272-6 | 1 minute Apgar Score | _APGAR menit ke-1_ → `Observation.valueQuantity.value` (182, tanpa BQ) |
| 16 | 214–248 | Observation | 9274-2 | 5 minute Apgar Score | _APGAR menit ke-5_ → `Observation.valueQuantity.value` (217, tanpa BQ) |
| 17 | 249–283 | Observation | 9271-8 | 10 minute Apgar Score | _APGAR menit ke-10_ → `Observation.valueQuantity.value` (252, tanpa BQ) |
| 18 | 284–305 | Observation | 276654001.0 | Congenital malformation | _Kelainan Bawaan_ → `Observation.valueCodeableConcept.coding` (287, tanpa BQ) |
| 19 | 306–317 | Observation | 8867-4 | Heart rate | _Frekuensi Denyut Jantung_ → `Observation.valueQuantity.value` (309, tanpa BQ) |
| 20 | 318–328 | Observation | 8310-5 | Body temperature | _Suhu_ → `Observation.valueQuantity.value` (321, tanpa BQ) |
| 21 | 329–339 | Observation | 9279-1 | Respiratory rate | _Pernapasan_ → `Observation.valueQuantity.value` (332, tanpa BQ) |
| 22 | 340–351 | Observation | 20564-1 | Oxygen saturation in Blood | _Saturasi Oksigen_ → `Observation.valueQuantity.value` (343, tanpa BQ) |
| 23 | 352–362 | Procedure | 386412000.0 | Resuscitation of neonate | _Apakah Diberikan Resusitasi_ → `Procedure.category.coding` (352, tanpa BQ) |
| 24 | 363–373 | Procedure | PC000003 | Manajemen Terpadu Bayi Muda (MTBM) | _Apakah dilakukan pemeriksaan kesehatan dengan pendekatan MTBM_ → `Procedure.category.coding` (363, tanpa BQ) |
| 25 | 374–384 | Procedure | SP000126 | ARV Profilaksis | _ARV Profilaksis pada bayi baru lahir_ → `Procedure.category.coding` (374, tanpa BQ) |
| 26 | 385–395 | Procedure | 448883004.0 | Injection of vitamin K1 | _Apakah diberikan vitamin K_ → `Procedure.category.coding` (385, tanpa BQ) |
| 27 | 396–406 | Procedure | PC000001 | Perawatan Tali Pusat | _Perawatan Tali Pusat_ → `Procedure.category.coding` (396, tanpa BQ) |
| 28 | 407–417 | Procedure | PC000002 | Pemberian Salep Antibiotik Mata | _Salep Antibiotik Mata_ → `Procedure.category.coding` (407, tanpa BQ) |
| 29 | 418–440 | Immunization | – | – | _Imunisasi Hepatitis B (HB0)_ → `Immunization.status` (418, tanpa BQ) |
| 30 | 441–451 | Procedure | 431868002.0 | Initiation of breastfeeding | _Inisiasi Menyusu Dini (IMD)_ → `Procedure.category.coding` (441, tanpa BQ) |
| 31 | 452–463 | Observation | OC000016 | Waktu Inisiasi Menyusui Dini | _Waktu Inisiasi Menyusu Dini (IMD)_ → `Observation.valueCodeableConcept.coding` (454, tanpa BQ) |
| 32 | 464–487 | Immunization | – | – | _Imunisasi HBIg_ → `Immunization.status` (464, tanpa BQ) |
| 33 | 494–500 | Condition | Z00.1 | Routine child health examination | – |
| 34 | 515–526 | Observation | 29463-7 | Body weight | _Berat Badan_ → `Observation.valueQuantity.value` (518, tanpa BQ) |
| 35 | 527–538 | Observation | 8306-3 | Body height --lying | _Tinggi Badan_ → `Observation.valueQuantity.value` (530, tanpa BQ) |
| 36 | 539–549 | Observation | 249278006.0 | Ability to pass urine | _Bayi sudah Buang Air Kecil 6 jam setelah kelahiran?_ → `Observation.valueBoolean` (542, tanpa BQ) |
| 37 | 550–560 | Observation | 276397000.0 | Has passed meconium | _Bayi sudah Buang Air Besar 6 jam setelah kelahiran?_ → `Observation.valueBoolean` (553, tanpa BQ) |
| 38 | 561–582 | ServiceRequest | 736282001.0 | Neonatal critical care plan | _Rujuk_ → `ServiceRequest.status` (561, tanpa BQ)<br>_Faskes Rujukan_ → `ServiceRequest.locationCode.coding` (574, tanpa BQ)<br>_Nama Faskes Rujukan_ → `ServiceRequest.locationCode.text` (582, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 21 |
| Procedure | 7 |
| RelatedPerson | 2 |
| Condition | 2 |
| Immunization | 2 |
| Patient | 1 |
| EpisodeOfCare | 1 |
| Encounter | 1 |
| ServiceRequest | 1 |
| **Total** | **38** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 39 | EpisodeOfCare | `EpisodeOfCare.type.coding` | Neonate | Neonate | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 2 | 61 | Condition | `Condition.code.coding` | Z00.1 | Routine child health examination | http://hl7.org/fhir/sid/icd-10 |
| 3 | 83 | Observation | `Observation.code.coding` | 365475008.0 | Place in family order | http://snomed.info/sct |
| 4 | 94 | Observation | `Observation.code.coding` | 57715-5 | Birth time | http://loinc.org |
| 5 | 105 | Observation | `Observation.code.coding` | 76516-4 | Gestational age—​at birth | http://loinc.org |
| 6 | 108 | Observation | `Observation.component.code.coding` | SP000398 | Usia Kehamilan Saat Persalinan (hari) | http://terminology.kemkes.go.id/sp |
| 7 | 120 | Observation | `Observation.code.coding` | 883-9 | ABO group [Type] in Blood | http://loinc.org |
| 8 | 121 | Observation | `Observation.valueCodeableConcept.coding` | LA19710-5 | Group A | http://loinc.org |
| 9 | 122 | Observation | `Observation.valueCodeableConcept.coding` | LA19709-7 | Group B | http://loinc.org |
| 10 | 123 | Observation | `Observation.valueCodeableConcept.coding` | LA19708-9 | Group O | http://loinc.org |
| 11 | 124 | Observation | `Observation.valueCodeableConcept.coding` | LA28449-9 | Group AB | http://loinc.org |
| 12 | 133 | Observation | `Observation.code.coding` | 10331-7 | Rh [Type] in Blood | http://loinc.org |
| 13 | 134 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 14 | 135 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 15 | 145 | Observation | `Observation.code.coding` | 8339-4 | Birth weight Measured | http://loinc.org |
| 16 | 157 | Observation | `Observation.code.coding` | 89269-5 | Body height Measured --at birth | http://loinc.org |
| 17 | 169 | Observation | `Observation.code.coding` | 8290-9 | Head Occipital-frontal circumference --at birth- by Tape measure | http://loinc.org |
| 18 | 181 | Observation | `Observation.code.coding` | 9272-6 | 1 minute Apgar Score | http://loinc.org |
| 19 | 191 | Observation | `Observation.interpretation.coding` | 57284007.0 | Severe birth asphyxia | http://snomed.info/sct |
| 20 | 192 | Observation | `Observation.interpretation.coding` | 77362009.0 | Mild to moderate birth asphyxia | http://snomed.info/sct |
| 21 | 193 | Observation | `Observation.interpretation.coding` | 275307002.0 | Apgar normal | http://snomed.info/sct |
| 22 | 194 | Observation | `Observation.component.code.coding` | 32406-1 | 1 minute Apgar Color | http://loinc.org |
| 23 | 195 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6722-8 | The baby's whole body is completely bluish-gray or pale | http://loinc.org |
| 24 | 196 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6723-6 | Good color in body with bluish hands or feet | http://loinc.org |
| 25 | 197 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6724-4 | Good color all over | http://loinc.org |
| 26 | 198 | Observation | `Observation.component.code.coding` | 32407-9 | 1 minute Apgar Heart rate | http://loinc.org |
| 27 | 199 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6716-0 | No heart rate | http://loinc.org |
| 28 | 200 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6717-8 | Fewer than 100 beats per minute | http://loinc.org |
| 29 | 201 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6718-6 | At least 100 beats per minute | http://loinc.org |
| 30 | 202 | Observation | `Observation.component.code.coding` | 32409-5 | 1 minute Apgar Reflex irritability | http://loinc.org |
| 31 | 203 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6719-4 | No response to airways being suctioned | http://loinc.org |
| 32 | 204 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6720-2 | Grimace during suctioning | http://loinc.org |
| 33 | 205 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6721-0 | Grimace and pulling away, cough, or sneeze during suctioning | http://loinc.org |
| 34 | 206 | Observation | `Observation.component.code.coding` | 32408-7 | 1 minute Apgar Muscle tone | http://loinc.org |
| 35 | 207 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6713-7 | Limp; no movement | http://loinc.org |
| 36 | 208 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6714-5 | Some flexion of arms and legs | http://loinc.org |
| 37 | 209 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6715-2 | Active motion | http://loinc.org |
| 38 | 210 | Observation | `Observation.component.code.coding` | 32410-3 | 1 minute Apgar Respiratory effort | http://loinc.org |
| 39 | 211 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6725-1 | Not breathing | http://loinc.org |
| 40 | 212 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6726-9 | Weak cry; may sound like whimpering, slow or irregular breathing | http://loinc.org |
| 41 | 213 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6727-7 | Good, strong cry; normal rate and effort of breathing | http://loinc.org |
| 42 | 216 | Observation | `Observation.code.coding` | 9274-2 | 5 minute Apgar Score | http://loinc.org |
| 43 | 226 | Observation | `Observation.interpretation.coding` | 57284007.0 | Severe birth asphyxia | http://snomed.info/sct |
| 44 | 227 | Observation | `Observation.interpretation.coding` | 77362009.0 | Mild to moderate birth asphyxia | http://snomed.info/sct |
| 45 | 228 | Observation | `Observation.interpretation.coding` | 275307002.0 | Apgar normal | http://snomed.info/sct |
| 46 | 229 | Observation | `Observation.component.code.coding` | 32411-1 | 5 minute Apgar Color | http://loinc.org |
| 47 | 230 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6722-8 | The baby's whole body is completely bluish-gray or pale | http://loinc.org |
| 48 | 231 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6723-6 | Good color in body with bluish hands or feet | http://loinc.org |
| 49 | 232 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6724-4 | Good color all over | http://loinc.org |
| 50 | 233 | Observation | `Observation.component.code.coding` | 32412-9 | 5 minute Apgar Heart rate | http://loinc.org |
| 51 | 234 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6716-0 | No heart rate | http://loinc.org |
| 52 | 235 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6717-8 | Fewer than 100 beats per minute | http://loinc.org |
| 53 | 236 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6718-6 | At least 100 beats per minute | http://loinc.org |
| 54 | 237 | Observation | `Observation.component.code.coding` | 32414-5 | 5 minute Apgar Reflex irritability | http://loinc.org |
| 55 | 238 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6719-4 | No response to airways being suctioned | http://loinc.org |
| 56 | 239 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6720-2 | Grimace during suctioning | http://loinc.org |
| 57 | 240 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6721-0 | Grimace and pulling away, cough, or sneeze during suctioning | http://loinc.org |
| 58 | 241 | Observation | `Observation.component.code.coding` | 32413-7 | 5 minute Apgar Muscle tone | http://loinc.org |
| 59 | 242 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6713-7 | Limp; no movement | http://loinc.org |
| 60 | 243 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6714-5 | Some flexion of arms and legs | http://loinc.org |
| 61 | 244 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6715-2 | Active motion | http://loinc.org |
| 62 | 245 | Observation | `Observation.component.code.coding` | 32415-2 | 5 minute Apgar Respiratory effort | http://loinc.org |
| 63 | 246 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6725-1 | Not breathing | http://loinc.org |
| 64 | 247 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6726-9 | Weak cry; may sound like whimpering, slow or irregular breathing | http://loinc.org |
| 65 | 248 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6727-7 | Good, strong cry; normal rate and effort of breathing | http://loinc.org |
| 66 | 251 | Observation | `Observation.code.coding` | 9271-8 | 10 minute Apgar Score | http://loinc.org |
| 67 | 261 | Observation | `Observation.interpretation.coding` | 57284007.0 | Severe birth asphyxia | http://snomed.info/sct |
| 68 | 262 | Observation | `Observation.interpretation.coding` | 77362009.0 | Mild to moderate birth asphyxia | http://snomed.info/sct |
| 69 | 263 | Observation | `Observation.interpretation.coding` | 275307002.0 | Apgar normal | http://snomed.info/sct |
| 70 | 264 | Observation | `Observation.component.code.coding` | 32401-2 | 10 minute Apgar Color | http://loinc.org |
| 71 | 265 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6722-8 | The baby's whole body is completely bluish-gray or pale | http://loinc.org |
| 72 | 266 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6723-6 | Good color in body with bluish hands or feet | http://loinc.org |
| 73 | 267 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6724-4 | Good color all over | http://loinc.org |
| 74 | 268 | Observation | `Observation.component.code.coding` | 32402-0 | 10 minute Apgar Heart rate | http://loinc.org |
| 75 | 269 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6716-0 | No heart rate | http://loinc.org |
| 76 | 270 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6717-8 | Fewer than 100 beats per minute | http://loinc.org |
| 77 | 271 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6718-6 | At least 100 beats per minute | http://loinc.org |
| 78 | 272 | Observation | `Observation.component.code.coding` | 32404-6 | 10 minute Apgar Reflex irritability | http://loinc.org |
| 79 | 273 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6719-4 | No response to airways being suctioned | http://loinc.org |
| 80 | 274 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6720-2 | Grimace during suctioning | http://loinc.org |
| 81 | 275 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6721-0 | Grimace and pulling away, cough, or sneeze during suctioning | http://loinc.org |
| 82 | 276 | Observation | `Observation.component.code.coding` | 32403-8 | 10 minute Apgar Muscle tone | http://loinc.org |
| 83 | 277 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6713-7 | Limp; no movement | http://loinc.org |
| 84 | 278 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6714-5 | Some flexion of arms and legs | http://loinc.org |
| 85 | 279 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6715-2 | Active motion | http://loinc.org |
| 86 | 280 | Observation | `Observation.component.code.coding` | 32405-3 | 10 minute Apgar Respiratory effort | http://loinc.org |
| 87 | 281 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6725-1 | Not breathing | http://loinc.org |
| 88 | 282 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6726-9 | Weak cry; may sound like whimpering, slow or irregular breathing | http://loinc.org |
| 89 | 283 | Observation | `Observation.component.valueCodeableConcept.coding` | LA6727-7 | Good, strong cry; normal rate and effort of breathing | http://loinc.org |
| 90 | 286 | Observation | `Observation.code.coding` | 276654001.0 | Congenital malformation | http://snomed.info/sct |
| 91 | 287 | Observation | `Observation.valueCodeableConcept.coding` | 74964007.0 | Other | http://snomed.info/sct |
| 92 | 289 | Observation | `Observation.valueCodeableConcept.coding` | 80281008.0 | Cleft lip | http://snomed.info/sct |
| 93 | 290 | Observation | `Observation.valueCodeableConcept.coding` | 13213009.0 | Congenital heart disease | http://snomed.info/sct |
| 94 | 291 | Observation | `Observation.valueCodeableConcept.coding` | 35045004.0 | Microtia | http://snomed.info/sct |
| 95 | 292 | Observation | `Observation.valueCodeableConcept.coding` | 22006008.0 | Hypertelorism | http://snomed.info/sct |
| 96 | 293 | Observation | `Observation.valueCodeableConcept.coding` | 367506006.0 | Polydactyly | http://snomed.info/sct |
| 97 | 294 | Observation | `Observation.valueCodeableConcept.coding` | 52781008.0 | Congenital hip dysplasia | http://snomed.info/sct |
| 98 | 295 | Observation | `Observation.valueCodeableConcept.coding` | 1156475005.0 | Congenital talipes equinovarus | http://snomed.info/sct |
| 99 | 296 | Observation | `Observation.valueCodeableConcept.coding` | 253098009.0 | Neural tube defect | http://snomed.info/sct |
| 100 | 297 | Observation | `Observation.valueCodeableConcept.coding` | 118928003.0 | Disorder of abdominal wall | http://snomed.info/sct |
| 101 | 298 | Observation | `Observation.valueCodeableConcept.coding` | 42030000.0 | Disorder of the genitourinary system | http://snomed.info/sct |
| 102 | 308 | Observation | `Observation.code.coding` | 8867-4 | Heart rate | http://loinc.org |
| 103 | 320 | Observation | `Observation.code.coding` | 8310-5 | Body temperature | http://loinc.org |
| 104 | 331 | Observation | `Observation.code.coding` | 9279-1 | Respiratory rate | http://loinc.org |
| 105 | 342 | Observation | `Observation.code.coding` | 20564-1 | Oxygen saturation in Blood | http://loinc.org |
| 106 | 355 | Procedure | `Procedure.code.coding` | 386412000.0 | Resuscitation of neonate | http://snomed.info/sct |
| 107 | 366 | Procedure | `Procedure.code.coding` | PC000003 | Manajemen Terpadu Bayi Muda (MTBM) | http://terminology.kemkes.go.id/CodeSystem/clinical-term" |
| 108 | 377 | Procedure | `Procedure.code.coding` | SP000126 | ARV Profilaksis | http://terminology.kemkes.go.id/sp |
| 109 | 388 | Procedure | `Procedure.code.coding` | 448883004.0 | Injection of vitamin K1 | http://snomed.info/sct |
| 110 | 399 | Procedure | `Procedure.code.coding` | PC000001 | Perawatan Tali Pusat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 111 | 410 | Procedure | `Procedure.code.coding` | PC000002 | Pemberian Salep Antibiotik Mata | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 112 | 421 | Immunization | `Immunization.vaccineCode` | VG45 | HepB | http://sys-ids.kemkes.go.id/kfa |
| 113 | 444 | Procedure | `Procedure.code.coding` | 431868002.0 | Initiation of breastfeeding | http://snomed.info/sct |
| 114 | 453 | Observation | `Observation.code.coding` | OC000016 | Waktu Inisiasi Menyusui Dini | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 115 | 454 | Observation | `Observation.valueCodeableConcept.coding` | OV000014 | Kurang dari 1 Jam | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 116 | 455 | Observation | `Observation.valueCodeableConcept.coding` | OV000015 | Lebih dari 1 Jam | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 117 | 467 | Immunization | `Immunization.vaccineCode` | VG45 | HepB | http://sys-ids.kemkes.go.id/kfa |
| 118 | 468 | Immunization | `Immunization.vaccineCode` | 30.0 | hepatitis B immune globulin | http://hl7.org/fhir/sid/cvx |
| 119 | 496 | Condition | `Condition.code.coding` | Z00.1 | Routine child health examination | http://hl7.org/fhir/sid/icd-10 |
| 120 | 517 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 121 | 529 | Observation | `Observation.code.coding` | 8306-3 | Body height --lying | http://loinc.org |
| 122 | 541 | Observation | `Observation.code.coding` | 249278006.0 | Ability to pass urine | http://snomed.info/sct |
| 123 | 552 | Observation | `Observation.code.coding` | 276397000.0 | Has passed meconium | http://snomed.info/sct |
| 124 | 565 | ServiceRequest | `ServiceRequest.code.coding` | 736282001.0 | Neonatal critical care plan | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://loinc.org | 82 |
| http://snomed.info/sct | 28 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 5 |
| http://hl7.org/fhir/sid/icd-10 | 2 |
| http://terminology.kemkes.go.id/sp | 2 |
| http://sys-ids.kemkes.go.id/kfa | 2 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 1 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term" | 1 |
| http://hl7.org/fhir/sid/cvx | 1 |
| **Total** | **124** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| – | – | – | – | – |
