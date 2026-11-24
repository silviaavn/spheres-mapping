# Output Form: eKohort - Pelayanan Ibu Bersalin (INC)

Sumber: `mapping/phdt-data-dictionary-ekohort-inc.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-ekohort-inc.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 58 |
| Code (`jumlah code` = 1) | 74 |
| Code unik (code + CodeSystem) | 56 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 0 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–14 | Patient | – | – | _Nama Ibu_ → `Patient.name` (2, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (5, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (8, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.extension.valueCode` (11, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.extension.valueCode` (14, tanpa BQ)<br>_No Ktp_ → `Patient.identifier.use` (18, tanpa BQ)<br>_Id Ibu_ → `Patient.identifier.use` (22, tanpa BQ)<br>_Nama Ibu_ → `Patient.name` (25, tanpa BQ) |
| 2 | 17–17 | Practitioner | – | – | _Nama Pemeriksa_ → `Practitioner.name` (17, tanpa BQ) |
| 3 | 21–21 | Encounter | – | – | _Id Bersalinan_ → `Encounter.identifier` (21, tanpa BQ) |
| 4 | 26–28 | Observation | – | – | _Kala 1 Tgl_ → `Observation.category.coding` (26, tanpa BQ)<br>_Kala 1 Jam_ → `Observation.code.coding[x]` (27, tanpa BQ) |
| 5 | 29–31 | Observation | – | – | _Kala 2 Tgl_ → `Observation.category.coding` (29, tanpa BQ)<br>_Kala 2 Jam_ → `Observation.code.coding[x]` (30, tanpa BQ) |
| 6 | 32–34 | Observation | – | – | _By Lahir Tgl_ → `Observation.category.coding` (32, tanpa BQ)<br>_By Lahir Jam_ → `Observation.code.coding[x]` (33, tanpa BQ)<br>_Plasenta Lahir Tgl_ → `Observation.categoriy.coding` (34, tanpa BQ) |
| 7 | 35–37 | Observation | – | – | _Plasenta Lahir Jam_ → `Observation.valueDateTime` (36, tanpa BQ)<br>_Usia Kehamilan_ → `Observation.category.coding` (37, tanpa BQ) |
| 8 | 38–42 | Observation | – | – | _Usia Hpht_ → `Observation.category.coding` (42, tanpa BQ) |
| 9 | 43–47 | Observation | – | – | _Presentasi Persalinan_ → `Observation.category.coding` (47, tanpa BQ) |
| 10 | 48–51 | Observation | 72155-5 | Position in womb Fetus [RHEA] | _Berat Bayi Lahir_ → `Observation.category.coding` (51, tanpa BQ) |
| 11 | 52–57 | Observation | – | – | _Cara Persalinan_ → `Observation.category.coding` (57, tanpa BQ) |
| 12 | 58–61 | Observation | 57071-3 | Obstetric delivery method | _Tempat Persalinan_ → `Observation.category.coding` (61, tanpa BQ) |
| 13 | 62–63 | Observation | 85712-8 | Expected delivery location | – |
| 14 | 64–67 | Procedure | – | – | – |
| 15 | 70–74 | Observation | – | – | _Penolong Persalinan_ → `Observation.valueCodeableConcept.coding` (72, tanpa BQ) |
| 16 | 75–79 | Observation | – | – | _Kala 3_ → `Observation.valueCodeableConcept.coding` (77, tanpa BQ) |
| 17 | 80–81 | Condition | – | – | _Komplikasi_ → `Condition.category.coding` (80, tanpa BQ) |
| 18 | 87–89 | Procedure | – | – | _Pelayanan Imd_ → `Procedure.category.coding` (87, tanpa BQ) |
| 19 | 90–93 | Observation | – | – | – |
| 20 | 94–97 | Observation | – | – | _Keadaan Ibu_ → `Observation.valueCodeableConcept.coding` (96, tanpa BQ) |
| 21 | 98–101 | Observation | 64710-7 | Was your pregnancy a live birth, stillbirth, miscarriage, abortion, or ectopic pregnancy [PhenX] | _Keadaan Bayi_ → `Observation.valueCodeableConcept.coding` (100, tanpa BQ) |
| 22 | 108–108 | Practitioner | – | – | _Kode Nakes_ → `Practitioner.identifier` (108, tanpa BQ) |
| 23 | 109–112 | Procedure | – | – | _Nama Penolong_ → `Procedure.category` (109, tanpa BQ) |
| 24 | 113–113 | Practitioner | – | – | – |
| 25 | 114–118 | Observation | 93857-1 | Date and time of obstetric delivery | _Kehamilan Ke_ → `Observation.code[0].coding[0` (114, tanpa BQ)<br>_Kode Tempat Persalinan_ → `Observation.valueInteger[0]` (115, tanpa BQ)<br>_Tgl Persalinan_ → `Observation.category[i].coding[i]` (116, tanpa BQ) |
| 26 | 119–124 | Observation | 8480-6 | Systolic blood pressure | _Td_ → `Observation.category[i].coding[i]` (119, tanpa BQ) |
| 27 | 125–129 | Observation | 8867-4 | Heart rate | _Frekuensi Nadi_ → `Observation.category[i].coding[i]` (125, tanpa BQ) |
| 28 | 130–134 | Observation | 9279-1 | Respiratory rate | _Frekuensi Pernapasan_ → `Observation.category[i].coding[i]` (130, tanpa BQ) |
| 29 | 135–139 | Observation | 8310-5 | Body temperature | _Suhu_ → `Observation.valueQuantity.value` (137, tanpa BQ) |
| 30 | 140–144 | Observation | 11881-0 | Uterus Fundal height Tape measure | _Tinggi Fundus Uteri_ → `Observation.valueQuantity.value` (143, tanpa BQ) |
| 31 | 145–152 | Observation | – | – | _Kondisi Detak Jantung Janin_ → `Observation.valueCodeableConcept.coding` (148, tanpa BQ)<br>_Detak Jantung Janin_ → `Observation.valueQuantity.value` (150, tanpa BQ) |
| 32 | 153–157 | Observation | – | – | _Letak Janin_ → `Observation.valueCodeableConcept.coding` (156, tanpa BQ) |
| 33 | 158–163 | Observation | 72155-5 | Position in womb Fetus [RHEA] | _Presentasi_ → `Observation.valueCodeableConcept.coding` (161, tanpa BQ) |
| 34 | 164–169 | Observation | 249111004 | Engagement of head | _Posisi Kepala_ → `Observation.valueCodeableConcept.coding` (167, tanpa BQ) |
| 35 | 170–173 | Observation | 289282009 | Amniotic membrane finding | _Kondisi Ketuban_ → `Observation.valueCodeableConcept.coding` (172, tanpa BQ) |
| 36 | 174–178 | Observation | CUSTOM | – | _Riwayat Lab Anemia_ → `Observation.valueBoolean` (176, tanpa BQ) |
| 37 | 179–183 | Observation | CUSTOM | – | _Riwayat Lab Protein Urin_ → `Observation.valueBoolean` (181, tanpa BQ) |
| 38 | 184–188 | Observation | CUSTOM | – | _Riwayat Lab Diabetes_ → `Observation.valueBoolean` (186, tanpa BQ) |
| 39 | 189–193 | Observation | CUSTOM | – | _Riwayat Lab Hiv_ → `Observation.valueBoolean` (191, tanpa BQ) |
| 40 | 194–198 | Observation | CUSTOM | – | _Riwayat Lab Hepatitis B_ → `Observation.valueBoolean` (196, tanpa BQ) |
| 41 | 199–203 | Observation | CUSTOM | – | _Riwayat Lab Sifilis_ → `Observation.valueBoolean` (201, tanpa BQ) |
| 42 | 204–206 | Observation | CUSTOM | – | _Faktor Resiko Anemia_ → `Observation.valueString` (206, tanpa BQ) |
| 43 | 207–209 | Observation | CUSTOM | Faktor risiko eklampsia | _Faktor Resiko Pre Eklampsia_ → `Observation.valueString` (209, tanpa BQ) |
| 44 | 210–212 | Observation | CUSTOM | Faktor risiko diabetes | _Faktor Resiko Diabetes_ → `Observation.valueString` (212, tanpa BQ) |
| 45 | 213–215 | Observation | CUSTOM | Faktor risiko HIV | _Faktor Resiko Hiv_ → `Observation.valueString` (215, tanpa BQ) |
| 46 | 216–218 | Observation | CUSTOM | Faktor risiko Hepatitis B | _Faktor Resiko Hepatitis B_ → `Observation.valueString` (218, tanpa BQ) |
| 47 | 219–221 | Observation | CUSTOM | Faktor risiko Sifilis | _Faktor Resiko Sifilis_ → `Observation.valueString` (221, tanpa BQ) |
| 48 | 222–224 | Observation | CUSTOM | Faktor risiko Malaria | _Faktor Resiko Malaria_ → `Observation.valueString` (224, tanpa BQ) |
| 49 | 225–227 | Observation | CUSTOM | Faktor risiko Tb | _Faktor Resiko Tb_ → `Observation.valueString` (227, tanpa BQ) |
| 50 | 228–230 | Observation | CUSTOM | Faktor Resiko Lainnya | _Faktor Resiko Lainnya_ → `Observation.valueString` (230, tanpa BQ) |
| 51 | 231–235 | Observation | – | – | _Kondisi Kala4_ → `Observation.valueCodeableConcept.coding` (233, tanpa BQ) |
| 52 | 236–240 | Observation | 81661-1 | Blood Loss [Volume] Measured | _Jumlah Pendarahan_ → `Observation.valueQuantity.value` (238, tanpa BQ) |
| 53 | 241–243 | Observation | – | – | _Td Kala4_ → `Observation.valueDatetime` (243, tanpa BQ) |
| 54 | 244–247 | Observation | – | – | _Tindakan Kala4_ → `Observation.valueString` (246, tanpa BQ)<br>_Ket Kala4_ → `Observation.note` (247, tanpa BQ) |
| 55 | 248–249 | Condition | – | – | _Komplikasi Persalinan_ → `Condition.category.coding` (248, tanpa BQ) |
| 56 | 250–254 | Observation | – | – | _Tata Laksana Komplikasi Persalinan_ → `Observation.valueBoolean` (252, tanpa BQ)<br>_Rujuk_ → `Observation.component.code` (253, tanpa BQ) |
| 57 | 256–260 | ServiceRequest | 737492002 | Outpatient care management | _Faskes Rujukan_ → `ServiceRequest.category.coding` (256, tanpa BQ)<br>_Nama Faskes Rujuk_ → `ServiceRequest.performer` (260, tanpa BQ) |
| 58 | 261–264 | Procedure | – | – | _Konseling_ → `Procedure.category` (261, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 46 |
| Procedure | 4 |
| Practitioner | 3 |
| Condition | 2 |
| Patient | 1 |
| Encounter | 1 |
| ServiceRequest | 1 |
| **Total** | **58** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 27 | Observation | `Observation.code.coding[x]` | 249120008 | Onset of labor first stage | http://snomed.info/sct |
| 2 | 30 | Observation | `Observation.code.coding[x]` | 249160009 | Onset of labor second stage | http://snomed.info/sct |
| 3 | 33 | Observation | `Observation.code.coding[x]` | 93857-1 | Date and time of obstetric delivery | http://loinc.org |
| 4 | 38 | Observation | `Observation.code.coding[x]` | 76516-4 | Gestational age--at birth | http://loinc.org |
| 5 | 48 | Observation | `Observation.code.coding` | 72155-5 | Position in womb Fetus [RHEA] | http://loinc.org |
| 6 | 49 | Observation | `Observation.valueCodeableConcept.coding` | 70028003 | Vertex presentation | http://snomed.info/sct |
| 7 | 50 | Observation | `Observation.valueCodeableConcept.coding` | 288203005 | Transverse/oblique lie | http://snomed.info/sct |
| 8 | 52 | Observation | `Observation.code.coding[x]` | 8339-4 | Birth weight Measured | https://loinc.org |
| 9 | 58 | Observation | `Observation.code.coding` | 57071-3 | Obstetric delivery method | https://loinc.org |
| 10 | 59 | Observation | `Observation.valueCodeableConcept.coding` | 48782003 | Delivery normal | http://snomed.info/sct |
| 11 | 60 | Observation | `Observation.valueCodeableConcept.coding` | 200144004 | Deliveries by cesarean | http://snomed.info/sct |
| 12 | 62 | Observation | `Observation.code.coding` | 85712-8 | Expected delivery location | https://loinc.org |
| 13 | 65 | Procedure | `Procedure.code` | 73.59 | Other manually assisted delivery | http://hl7.org/fhir/sid/icd-9-cm |
| 14 | 66 | Procedure | `Procedure.code` | 74.0 | Classical cesarean section | http://hl7.org/fhir/sid/icd-9-cm |
| 15 | 71 | Observation | `Observation.code.coding[x]` | OC000013 | Penolong Persalinan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 16 | 72 | Observation | `Observation.valueCodeableConcept.coding` | 309453006 | Registered midwife | http://snomed.info/sct |
| 17 | 73 | Observation | `Observation.valueCodeableConcept.coding` | 309343006 | Physician Occupation | http://snomed.info/sct |
| 18 | 74 | Observation | `Observation.valueCodeableConcept.coding` | 11935004 | Obstetrician Occupation | http://snomed.info/sct |
| 19 | 78 | Observation | `Observation.valueCodeableConcept.coding` | 302384005 | Controlled cord traction of placenta | http://snomed.info/sct |
| 20 | 79 | Observation | `Observation.valueCodeableConcept.coding` | 236996005 | Abdominal uterine fundal massage | http://snomed.info/sct |
| 21 | 88 | Procedure | `Procedure.code.coding[x]` | 431868002 | Initiation of breastfeeding | http://snomed.info/sct |
| 22 | 91 | Observation | `Observation.code.coding[x]` | OC000016 | Waktu Inisiasi Menyusui Dini | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 23 | 92 | Observation | `Observation.valueCodeableConcept.coding` | OV000014 | Kurang dari 1 Jam | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 24 | 93 | Observation | `Observation.valueCodeableConcept.coding` | OV000015 | Lebih dari 1 Jam | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 25 | 97 | Observation | `Observation.valueCodeableConcept.coding` | 59283008 | Maternal death | http://snomed.info/sct |
| 26 | 99 | Observation | `Observation.code.coding` | 64710-7 | Was your pregnancy a live birth, stillbirth, miscarriage, abortion, or ectopic pregnancy [PhenX] | http://loinc.org |
| 27 | 100 | Observation | `Observation.valueCodeableConcept.coding` | 281050002 | Livebirth | http://snomed.info/sct |
| 28 | 101 | Observation | `Observation.valueCodeableConcept.coding` | 276506001 | Newborn death | http://snomed.info/sct |
| 29 | 110 | Procedure | `Procedure.code` | 73.59 | Other manually assisted delivery | http://hl7.org/fhir/sid/icd-9-cm |
| 30 | 111 | Procedure | `Procedure.code` | 74.0 | Classical cesarean section | http://hl7.org/fhir/sid/icd-9-cm |
| 31 | 117 | Observation | `Observation.code.coding` | 93857-1 | Date and time of obstetric delivery | http://loinc.org |
| 32 | 120 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 33 | 121 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://loinc.org |
| 34 | 126 | Observation | `Observation.code.coding` | 8867-4 | Heart rate | http://loinc.org |
| 35 | 131 | Observation | `Observation.code.coding` | 9279-1 | Respiratory rate | http://loinc.org |
| 36 | 136 | Observation | `Observation.code.coding` | 8310-5 | Body temperature | http://loinc.org |
| 37 | 141 | Observation | `Observation.code.coding` | 11881-0 | Uterus Fundal height Tape measure | http://loinc.org |
| 38 | 142 | Observation | `Observation.code.coding` | ANC.B8.DE105 | Symphysis-fundal height | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 39 | 146 | Observation | `Observation.code.coding[x]` | 289437007 | Finding of fetal heart rate | http://loinc.org |
| 40 | 147 | Observation | `Observation.code.coding[x]` | ANC.B8.DE107 | Fetal heart rate | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 41 | 148 | Observation | `Observation.valueCodeableConcept.coding` | 289441006 | Normal fetal heart rate | http://snomed.info/sct |
| 42 | 149 | Observation | `Observation.valueCodeableConcept.coding` | 312668007 | Abnormal fetal heart rate | http://snomed.info/sct |
| 43 | 154 | Observation | `Observation.code.coding[x]` | 271692001 | Presentation of fetus | http://snomed.info/sct |
| 44 | 155 | Observation | `Observation.code.coding[x]` | ANC.SS.DE41 | Letak Janin USG | http://snomed.info/sct |
| 45 | 159 | Observation | `Observation.code.coding` | 72155-5 | Position in womb Fetus [RHEA] | http://loinc.org |
| 46 | 160 | Observation | `Observation.code.coding` | ANC.B8.DE111 | Fetal presentation | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 47 | 161 | Observation | `Observation.valueCodeableConcept.coding` | 1209182005 | Cephalic fetal presentation | http://snomed.info/sct |
| 48 | 162 | Observation | `Observation.valueCodeableConcept.coding` | 6096002 | Breech presentation | http://snomed.info/sct |
| 49 | 165 | Observation | `Observation.code.coding` | 249111004 | Engagement of head | http://loinc.org |
| 50 | 166 | Observation | `Observation.code.coding` | ANC.SS.DE46 | Kepala Terhadap PAP | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 51 | 167 | Observation | `Observation.valueCodeableConcept.coding` | 62098001 | Head not engaged | http://snomed.info/sct |
| 52 | 168 | Observation | `Observation.valueCodeableConcept.coding` | 249112006 | Head engaged | http://snomed.info/sct |
| 53 | 171 | Observation | `Observation.code.coding` | 289282009 | Amniotic membrane finding | http://snomed.info/sct |
| 54 | 172 | Observation | `Observation.valueCodeableConcept.coding` | 249125003 | Intact membranes | http://snomed.info/sct |
| 55 | 173 | Observation | `Observation.valueCodeableConcept.coding` | CUSTOM | non intact membrane | http://snomed.info/sct |
| 56 | 175 | Observation | `Observation.code.coding` | CUSTOM |  |  |
| 57 | 180 | Observation | `Observation.code.coding` | CUSTOM |  |  |
| 58 | 185 | Observation | `Observation.code.coding` | CUSTOM |  |  |
| 59 | 190 | Observation | `Observation.code.coding` | CUSTOM |  |  |
| 60 | 195 | Observation | `Observation.code.coding` | CUSTOM |  |  |
| 61 | 200 | Observation | `Observation.code.coding` | CUSTOM |  |  |
| 62 | 205 | Observation | `Observation.code.coding` | CUSTOM |  |  |
| 63 | 208 | Observation | `Observation.code.coding` | CUSTOM | Faktor risiko eklampsia | CUSTOM |
| 64 | 211 | Observation | `Observation.code.coding` | CUSTOM | Faktor risiko diabetes | CUSTOM |
| 65 | 214 | Observation | `Observation.code.coding` | CUSTOM | Faktor risiko HIV | CUSTOM |
| 66 | 217 | Observation | `Observation.code.coding` | CUSTOM | Faktor risiko Hepatitis B | CUSTOM |
| 67 | 220 | Observation | `Observation.code.coding` | CUSTOM | Faktor risiko Sifilis | CUSTOM |
| 68 | 223 | Observation | `Observation.code.coding` | CUSTOM | Faktor risiko Malaria | CUSTOM |
| 69 | 226 | Observation | `Observation.code.coding` | CUSTOM | Faktor risiko Tb | CUSTOM |
| 70 | 229 | Observation | `Observation.code.coding` | CUSTOM | Faktor Resiko Lainnya |  |
| 71 | 237 | Observation | `Observation.code.coding` | 81661-1 | Blood Loss [Volume] Measured | http://loinc.org |
| 72 | 242 | Observation | `Observation.code.coding[x]` | 249160009 | Onset of labor second stage | http://snomed.info/sct |
| 73 | 253 | Observation | `Observation.component.code` | 3457005 | Patient referral | http://snomed.info/sct |
| 74 | 257 | ServiceRequest | `ServiceRequest.code.coding` | 737492002 | Outpatient care management | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 29 |
| http://loinc.org | 15 |
|  | 8 |
| CUSTOM | 7 |
| http://hl7.org/fhir/sid/icd-9-cm | 4 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 4 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 4 |
| https://loinc.org | 3 |
| **Total** | **74** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 15 | – | Nama Lembaga Kesehatan | Organization | `Organization.type` |
| 68 | – | Alamat Persalinan | Location | `Location.type.coding` |
| 82 | – | Fasilitas Kesehatan | – | `` |
| 83 | – | Keadaan | – | `` |
| 84 | – | Keadaan Jam | – | `` |
| 85 | – | Pelayanan | – | `` |
| 102 | – | Integrasi Arv | – | `` |
| 103 | – | Integrasi Anti Malaria | – | `` |
| 104 | – | Integrasi Anti Tb | – | `` |
| 105 | – | D | – | `` |
| 106 | – | T | – | `` |
| 107 | – | U | – | `` |
| 265 | – | Status Pindahan | – | `` |
