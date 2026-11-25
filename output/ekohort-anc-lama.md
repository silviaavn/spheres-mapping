# Output Form: eKohort - Pelayanan Ibu ANC (file eKohort lama)

Sumber: `mapping/phdt-data-dictionary-ekohort-anc-lama.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-ekohort-anc-lama.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 140 |
| Code (`jumlah code` = 1) | 256 |
| Code unik (code + CodeSystem) | 150 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 0 |
| Variabel BQ (unik) | 0 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–14 | Patient | – | – | _Nama Ibu_ → `Patient.name` (2, tanpa BQ)<br>_Nama Provinsi_ → `Patient.address.extension.extension.valueCode` (5, tanpa BQ)<br>_Nama Kabupaten_ → `Patient.address.extension.extension.valueCode` (8, tanpa BQ)<br>_Nama Kecamatan_ → `Patient.address.extension.url` (9, tanpa BQ)<br>_Nama Desa_ → `Patient.address.extension.extension.valueCode` (14, tanpa BQ)<br>_No Ktp_ → `Patient.identifier.use` (17, tanpa BQ)<br>_Id Ibu_ → `Patient.identifier.use` (24, tanpa BQ) |
| 2 | 15–15 | Encounter | – | – | _Nama Pemeriksa_ → `Encounter.participant` (15, tanpa BQ)<br>_Id Anc_ → `Encounter.identifier` (20, tanpa BQ)<br>_Kunjungan K_ → `` (36, tanpa BQ)<br>_Tanggal Anc_ → `Encounter.period.start` (44, tanpa BQ)<br>_Dirujuk Ke_ → `Encounter.hospitalization.dischargeDisposition.coding` (364, tanpa BQ)<br>_Nakes_ → `Encounter.participant` (366, tanpa BQ) |
| 3 | 16–16 | Practitioner | – | – | – |
| 4 | 22–23 | EpisodeOfCare | – | – | – |
| 5 | 25–29 | Observation | 18185-9 | Gestational age | _Usia Kehamilan_ → `Observation.valueQuantity.value` (28, tanpa BQ) |
| 6 | 30–33 | Observation | 32418-6 | Obstetric trimester Stated | _Tribulan Ke_ → `Observation.valueInteger` (33, tanpa BQ) |
| 7 | 49–50 | Condition | – | – | _Diagnosis_ → `Condition.category.coding` (49, tanpa BQ) |
| 8 | 51–55 | Observation | 29463-7 | Body weight | _Berat Badan_ → `Observation.valueQuantity.value` (54, tanpa BQ) |
| 9 | 56–60 | Observation | 8302-2 | Body height | _Tinggibadan_ → `Observation.valueQuantity.value` (59, tanpa BQ) |
| 10 | 61–70 | Observation | OC000010 | Indeks Massa Tubuh Sebelum Hamil | _IMT_ → `Observation.valueQuantity.value` (64, tanpa BQ) |
| 11 | 71–75 | Observation | 8480-6 | Systolic blood pressure | _Tekanan Darah_ → `Observation.valueQuantity.value` (74, tanpa BQ) |
| 12 | 76–80 | Observation | 8462-4 | Diastolic blood pressure | _Tekanan Darah Di_ → `Observation.valueQuantity.value` (79, tanpa BQ) |
| 13 | 81–84 | Observation | 392570002 | Blood pressure finding | _TD >140/90_ → `Observation.valueCodeableConcept.coding` (83, tanpa BQ) |
| 14 | 85–93 | Observation | 284473002 | Mid upper arm circumference | _Lila_ → `Observation.valueQuantity.value` (88, tanpa BQ)<br>_Status Gizi_ → `` (90, tanpa BQ) |
| 15 | 94–98 | Observation | 11881-0 | Uterus Fundal height Tape measure | _Tinggi Fundus_ → `Observation.valueQuantity.value` (97, tanpa BQ) |
| 16 | 99–102 | Observation | 32392-3 | Deep tendon reflex of Patellar | _Refleks Patella_ → `Observation.valueCodeableConcept.coding` (101, tanpa BQ) |
| 17 | 103–107 | Observation | 11948-7 | Fetal Heart rate US | _Detak Jantung Janin_ → `Observation.valueQuantity.value` (106, tanpa BQ) |
| 18 | 108–111 | Observation | 289437007 | Finding of fetal heart rate | _Djj Kondisi_ → `Observation.valueCodeableConcept.coding` (110, tanpa BQ) |
| 19 | 112–116 | Observation | 249111004 | Engagement of head | _Kepala Janin_ → `Observation.valueCodeableConcept.coding` (115, tanpa BQ) |
| 20 | 117–121 | Observation | 89087-1 | Fetal Body weight Estimated | _Berat Janin_ → `Observation.valueQuantity.value` (120, tanpa BQ) |
| 21 | 122–129 | Observation | 72155-5 | Position in womb Fetus [RHEA] | _Posisi Janin_ → `Observation.valueCodeableConcept.coding` (124, tanpa BQ) |
| 22 | 130–135 | Observation | 246435002 | Number of fetuses | _Janin_ → `Observation.valueCodeableConcept.coding` (133, tanpa BQ) |
| 23 | 136–142 | Observation | 72155-5 | Position in womb Fetus [RHEA] | _Presentasi_ → `Observation.valueCodeableConcept.coding` (139, tanpa BQ) |
| 24 | 143–153 | Immunization | – | – | _Status Tt_ → `Immunization.status` (143, tanpa BQ) |
| 25 | 154–157 | Procedure | 99.38 | Administration of tetanus toxoid | _Tt_ → `Procedure.category.coding` (154, tanpa BQ) |
| 26 | 158–160 | Observation | – | – | _Catat Kia_ → `Observation.valueBoolean` (160, tanpa BQ) |
| 27 | 162–163 | MedicationDispense | – | – | – |
| 28 | 164–178 | Medication | – | – | – |
| 29 | 179–184 | MedicationRequest | – | – | – |
| 30 | 185–199 | Medication | – | – | – |
| 31 | 200–204 | MedicationDispense | – | – | _Fe_ → `MedicationDispense.quantity.code` (204, tanpa BQ) |
| 32 | 205–206 | ServiceRequest | – | – | _Periksa Hb_ → `ServiceRequest.category` (205, tanpa BQ) |
| 33 | 207–209 | Specimen | – | – | – |
| 34 | 210–220 | Observation | 718-7 | Hemoglobin [Mass/volume] in Blood | _Hemoglobin_ → `Observation.valueQuantity.code` (214, tanpa BQ) |
| 35 | 221–222 | DiagnosticReport | – | – | – |
| 36 | 223–224 | ServiceRequest | – | – | _Periksa Protein Urin_ → `ServiceRequest.category` (223, tanpa BQ) |
| 37 | 225–226 | Specimen | – | – | – |
| 38 | 227–235 | Observation | 2887-8 | Protein [Presence] in Urine | _Pro Urin_ → `Observation.valueCodeableConcept.coding` (231, tanpa BQ) |
| 39 | 236–237 | DiagnosticReport | – | – | – |
| 40 | 239–240 | ServiceRequest | – | – | _Reduksi Guladarah_ → `ServiceRequest.category` (239, tanpa BQ) |
| 41 | 241–242 | Specimen | – | – | – |
| 42 | 243–249 | Observation | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | _Reduksi Guladarah Hasil_ → `Observation.valueQuantity.value` (245, tanpa BQ)<br>_> 140_ → `Observation.interpretation.coding` (247, tanpa BQ)<br>_Reduksi_ → `Observation.dataAbsentReason` (249, tanpa BQ) |
| 43 | 250–251 | DiagnosticReport | – | – | – |
| 44 | 252–253 | ServiceRequest | – | – | _Thalasemia_ → `ServiceRequest.category` (252, tanpa BQ) |
| 45 | 254–255 | Specimen | – | – | – |
| 46 | 256–259 | Observation | 94537-8 | Hemoglobin panel - Blood by HPLC | – |
| 47 | 260–261 | DiagnosticReport | – | – | – |
| 48 | 262–263 | ServiceRequest | – | – | _Sifilis_ → `ServiceRequest.category` (262, tanpa BQ) |
| 49 | 264–266 | Specimen | – | – | – |
| 50 | 267–271 | Observation | 22464-2 | Reagin Ab [Presence] in Specimen | – |
| 51 | 272–273 | DiagnosticReport | – | – | – |
| 52 | 274–275 | ServiceRequest | – | – | _Hepb_ → `ServiceRequest.category` (274, tanpa BQ) |
| 53 | 276–278 | Specimen | – | – | – |
| 54 | 279–283 | Observation | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | – |
| 55 | 284–285 | DiagnosticReport | – | – | – |
| 56 | 286–287 | ServiceRequest | – | – | _Hiv_ → `ServiceRequest.category` (286, tanpa BQ) |
| 57 | 288–289 | Specimen | – | – | – |
| 58 | 290–293 | Observation | 7918-6 | HIV 1+2 Ab [Presence] in Serum | – |
| 59 | 294–295 | DiagnosticReport | – | – | – |
| 60 | 296–298 | Observation | 4241000179101 | Laboratory report | _Hasil Lab_ → `Observation.valueString` (298, tanpa BQ) |
| 61 | 300–301 | ServiceRequest | – | – | _Periksa Darah Malaria_ → `ServiceRequest.category` (300, tanpa BQ) |
| 62 | 302–303 | Specimen | – | – | – |
| 63 | 304–308 | Observation | 76772-3 | Plasmodium falciparum Ag [Presence] in Blood by Rapid immunoassay | _Malaria_ → `Observation.valueCodeableConcept.coding` (307, tanpa BQ) |
| 64 | 309–310 | DiagnosticReport | – | – | – |
| 65 | 313–314 | ServiceRequest | – | – | _Tbc_ → `ServiceRequest.category` (313, tanpa BQ) |
| 66 | 315–316 | Specimen | – | – | – |
| 67 | 317–320 | Observation | 11477-7 | Microscopic observation [Identifier] in Sputum by Acid fast stain | – |
| 68 | 321–322 | DiagnosticReport | – | – | – |
| 69 | 323–324 | ServiceRequest | – | – | – |
| 70 | 325–326 | Specimen | – | – | – |
| 71 | 327–332 | Observation | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | – |
| 72 | 333–334 | DiagnosticReport | – | – | – |
| 73 | 338–341 | Observation | CUSTOM | CUSTOM | _Vdlr_ → `Observation.valueBoolean` (340, tanpa BQ) |
| 74 | 342–345 | Procedure | 88.78 | Diagnostic ultrasound of gravid uterus | _Usg_ → `Procedure.category.coding` (342, tanpa BQ) |
| 75 | 348–350 | Observation | – | – | _Usia Hpht_ → `Observation.valueBoolean` (350, tanpa BQ) |
| 76 | 351–354 | Observation | 32418-6 | Obstetric trimester Stated | _Trimester_ → `Observation.valueInteger` (354, tanpa BQ) |
| 77 | 355–360 | Condition | O13 | Gestational [pregnancy-induced] hypertension without signification proteinuria | _Komplikasi_ → `Condition.category.coding` (355, tanpa BQ)<br>_Komplikasi Lain_ → `Condition.code.coding` (360, tanpa BQ) |
| 78 | 361–363 | Observation | – | – | _Tatalaksana Komplikasi_ → `Observation.valueBoolean` (363, tanpa BQ) |
| 79 | 365–365 | Practitioner | – | – | _Id Nakes_ → `Practitioner.id` (365, tanpa BQ) |
| 80 | 367–370 | PractitionerRole | – | – | – |
| 81 | 381–385 | Observation | 8867-4 | Heart rate | _Nadi_ → `Observation.category[i].coding[i]` (381, tanpa BQ) |
| 82 | 386–390 | Observation | 9279-1 | Respiratory rate | _Rr_ → `Observation.category[i].coding[i]` (386, tanpa BQ) |
| 83 | 391–394 | Observation | – | – | _Pmt_ → `Observation.category[i].coding[i]` (391, tanpa BQ)<br>_Keterangan Pmt_ → `Observation.note` (394, tanpa BQ) |
| 84 | 403–404 | Condition | – | – | _Keluhan Ibu_ → `Condition.category.coding` (403, tanpa BQ) |
| 85 | 407–408 | ServiceRequest | 5292-8 | Reagin Ab [Presence] in Serum by VDRL | _Hasil Vdlr_ → `ServiceRequest.category.coding` (407, tanpa BQ) |
| 86 | 409–412 | Observation | 5292-8 | Reagin Ab [Presence] in Serum by VDRL | – |
| 87 | 413–414 | DiagnosticReport | – | – | – |
| 88 | 415–421 | Immunization | – | – | _Imunisasi Tt_ → `Immunization.status` (415, tanpa BQ)<br>_Tanggal Imunisasi Tt_ → `Immunization.occurrenceDateTime` (421, tanpa BQ) |
| 89 | 422–425 | Observation | 8665-2 | Last menstrual period start date | _Hpht_ → `Observation.valueDateTime` (425, tanpa BQ) |
| 90 | 426–429 | Observation | 11778-8 | Delivery date Estimated | _Hpl_ → `Observation.valueDateTime` (429, tanpa BQ) |
| 91 | 432–436 | Observation | 11948-7 | Fetal Heart rate US | _Usg Djj_ → `Observation.valueQuantity.value` (435, tanpa BQ) |
| 92 | 437–441 | Observation | 11888-5 | Gestational age US composite estimate | _Usg Usia Kehamilan_ → `Observation.valueQuantity.value` (440, tanpa BQ) |
| 93 | 442–450 | Observation | 271692001 | Presentation of fetus | _Usg Letak Janin_ → `Observation.valueCodeableConcept.coding` (445, tanpa BQ) |
| 94 | 451–454 | Procedure | 88.78 | Diagnostic ultrasound of gravid uterus | _Usg Taksiran Kehamilan_ → `Procedure.category.coding` (451, tanpa BQ) |
| 95 | 455–462 | Observation | – | – | _Tatalaksana Anemia_ → `Observation.valueBoolean` (457, tanpa BQ)<br>_Tata Laksana Anemia Lain_ → `Observation.component.code` (461, tanpa BQ) |
| 96 | 463–473 | Observation | 736286003 | Hypertension clinical management plan | _Tatalaksana Hipertensi_ → `Observation.valueBoolean` (465, tanpa BQ)<br>_Pantau Tekanan Darah_ → `Observation.component.code` (466, tanpa BQ)<br>_Pantau Protein Urine_ → `Observation.component.code` (468, tanpa BQ)<br>_Pantau Kondisi Janin_ → `Observation.component.code` (470, tanpa BQ)<br>_Tata Laksana Hipertensi Lain_ → `Observation.component.code` (472, tanpa BQ) |
| 97 | 474–490 | Observation | – | – | _Tatalaksana Preeklampsia_ → `Observation.valueBoolean` (476, tanpa BQ)<br>_Pantau Tekanan Darah Preeklampsia_ → `Observation.component.code` (477, tanpa BQ)<br>_Pantau Protein Urine Preeklampsia_ → `Observation.component.code` (479, tanpa BQ)<br>_Pantau Kondisi Janin Preeklampsia_ → `Observation.component.code` (481, tanpa BQ)<br>_Pemberian Antihipertensi_ → `Observation.component.code` (483, tanpa BQ)<br>_Pemberian Mgso4_ → `Observation.component.code` (485, tanpa BQ)<br>_Pemberian Diazepam_ → `Observation.component.code` (487, tanpa BQ)<br>_Tata Laksana Preeklampsia Lain_ → `Observation.component.code` (489, tanpa BQ) |
| 98 | 491–495 | Observation | – | – | _Tatalaksana Kek_ → `Observation.valueBoolean` (493, tanpa BQ)<br>_Pemberian Mt_ → `Observation.component.code` (494, tanpa BQ) |
| 99 | 496–499 | Procedure | 11816003 | Diet education | _Edukasi Gizi_ → `Procedure.category.coding` (496, tanpa BQ) |
| 100 | 500–504 | Observation | – | – | _Tata Laksana Kek Lain_ → `Observation.component.code` (500, tanpa BQ)<br>_Tatalaksana Obesitas_ → `Observation.valueBoolean` (504, tanpa BQ) |
| 101 | 505–508 | Procedure | 171054004 | Pregnancy diet education | _Edukasi Gizi Ibu Hamil_ → `Procedure.category.coding` (505, tanpa BQ) |
| 102 | 509–519 | Observation | 385821000 | Infection control management | _Tata Laksana Obesitas Lain_ → `Observation.component.code` (509, tanpa BQ)<br>_Tatalaksana Infeksi_ → `Observation.valueBoolean` (513, tanpa BQ)<br>_Antipiretik_ → `Observation.component.code` (514, tanpa BQ)<br>_Antibiotik_ → `Observation.component.code` (516, tanpa BQ)<br>_Tata Laksana Infeksi Lain_ → `Observation.component.code` (518, tanpa BQ) |
| 103 | 520–522 | Observation | – | – | _Tatalaksana Jantung_ → `Observation.valueBoolean` (522, tanpa BQ) |
| 104 | 523–526 | Procedure | 363001008 | Cardiovascular education | _Edukasi Penyakit Jantung_ → `Procedure.category` (523, tanpa BQ) |
| 105 | 527–531 | Observation | 1284934003 | Human immunodeficiency virus management program | _Tata Laksana Jantung Lain_ → `Observation.component.code` (527, tanpa BQ)<br>_Tatalaksana Hiv_ → `Observation.valueBoolean` (531, tanpa BQ) |
| 106 | 532–534 | Observation | 1280002000 | Tuberculosis management program | _Tatalaksana Tb_ → `Observation.valueBoolean` (534, tanpa BQ) |
| 107 | 535–543 | Observation | – | – | _Tatalaksana Malaria_ → `Observation.valueBoolean` (537, tanpa BQ)<br>_Rujuk_ → `Observation.component.code` (542, tanpa BQ) |
| 108 | 545–549 | ServiceRequest | 737492002 | Outpatient care management | _Faskes Rujukan_ → `ServiceRequest.category.coding` (545, tanpa BQ)<br>_Nama Faskes Rujuk_ → `ServiceRequest.performer` (549, tanpa BQ) |
| 109 | 551–554 | Observation | – | – | _Jumlah Mt Diberikan_ → `Observation.category[i].coding[i]` (551, tanpa BQ) |
| 110 | 555–558 | Procedure | – | – | _Konseling Lainnya_ → `Procedure.category` (555, tanpa BQ) |
| 111 | 560–563 | Observation | 289437007 | Finding of fetal heart rate | _Djj Kondisi3_ → `Observation.valueCodeableConcept.coding` (562, tanpa BQ) |
| 112 | 565–572 | Observation | 72155-5 | Position in womb Fetus [RHEA] | _Posisi Janin3_ → `Observation.valueCodeableConcept.coding` (567, tanpa BQ) |
| 113 | 573–577 | Observation | 249111004 | Engagement of head | _Kepala Janin3_ → `Observation.valueCodeableConcept.coding` (576, tanpa BQ) |
| 114 | 578–582 | Observation | 89087-1 | Fetal Body weight Estimated | _Berat Janin3_ → `Observation.valueQuantity.value` (581, tanpa BQ) |
| 115 | 583–589 | Observation | 72155-5 | Position in womb Fetus [RHEA] | _Presentasi3_ → `Observation.valueCodeableConcept.coding` (586, tanpa BQ) |
| 116 | 590–593 | Observation | 289437007 | Finding of fetal heart rate | _Djj Kondisi2_ → `Observation.valueCodeableConcept.coding` (592, tanpa BQ) |
| 117 | 594–598 | Observation | 11948-7 | Fetal Heart rate US | _Detak Jantung Janin2_ → `Observation.valueQuantity.value` (597, tanpa BQ) |
| 118 | 599–606 | Observation | 72155-5 | Position in womb Fetus [RHEA] | _Posisi Janin2_ → `Observation.valueCodeableConcept.coding` (601, tanpa BQ) |
| 119 | 607–611 | Observation | 249111004 | Engagement of head | _Kepala Janin2_ → `Observation.valueCodeableConcept.coding` (610, tanpa BQ) |
| 120 | 612–616 | Observation | 89087-1 | Fetal Body weight Estimated | _Berat Janin2_ → `Observation.valueQuantity.value` (615, tanpa BQ) |
| 121 | 617–622 | Observation | 72155-5 | Position in womb Fetus [RHEA] | _Presentasi2_ → `Observation.valueCodeableConcept.coding` (620, tanpa BQ) |
| 122 | 635–638 | Observation | CUSTOM | CUSTOM | _Dilakukan Hiv_ → `Observation.valueBoolean` (637, tanpa BQ) |
| 123 | 639–642 | Observation | CUSTOM | CUSTOM | _Dilakukan Sifilis_ → `Observation.valueBoolean` (641, tanpa BQ) |
| 124 | 643–646 | Observation | CUSTOM | CUSTOM | _Dilakukan Hepb_ → `Observation.valueBoolean` (645, tanpa BQ) |
| 125 | 647–650 | Observation | CUSTOM | CUSTOM | _Dilakukan Thalasemia_ → `Observation.valueBoolean` (649, tanpa BQ) |
| 126 | 651–655 | Procedure | – | – | _Konseling Gizi Ibu Hamil_ → `Procedure.category` (651, tanpa BQ) |
| 127 | 658–662 | Observation | 11727-5 | Fetal Body weight estimated by US | _Usg Taksiran Br Janin_ → `Observation.valueCodeableConcept.coding` (660, tanpa BQ) |
| 128 | 663–668 | Observation | 72155-5 | Position in womb Fetus [RHEA] | _Usg Presentasi_ → `Observation.valueCodeableConcept.coding` (666, tanpa BQ) |
| 129 | 669–676 | Observation | 1285244000 | Mean arterial pressure | _Map_ → `Observation.category[i].coding[i]` (669, tanpa BQ)<br>_Hasil Map_ → `Observation.interpretation` (674, tanpa BQ)<br>_Nakes Pemeriksa_ → `Observation.performer` (676, tanpa BQ) |
| 130 | 677–678 | PractitionerRole | – | – | – |
| 131 | 681–683 | Observation | – | – | _Kia Lengkap_ → `Observation.category[i].coding[i]` (681, tanpa BQ) |
| 132 | 684–687 | Condition | – | – | _Infeksi_ → `Condition.category` (684, tanpa BQ) |
| 133 | 689–692 | Observation | CUSTOM | CUSTOM | _Lab Malaria_ → `Observation.valueBoolean` (691, tanpa BQ) |
| 134 | 694–696 | Procedure | – | – | _Parenteral_ → `Procedure.category` (694, tanpa BQ) |
| 135 | 697–701 | Procedure | – | – | _Transfusi Darah_ → `Procedure.category` (698, tanpa BQ) |
| 136 | 702–705 | Condition | 161445009 | H/O: diabetes mellitus | _Diabetes_ → `Condition.category.coding` (702, tanpa BQ) |
| 137 | 706–708 | Observation | 698472009 | Blood glucose monitoring | _Pantau Gula Darah_ → `Observation.valueBoolean` (708, tanpa BQ) |
| 138 | 710–713 | Observation | CUSTOM | CUSTOM | _Lab Tb_ → `Observation.valueBoolean` (712, tanpa BQ) |
| 139 | 714–719 | Observation | 1285318003 | Viral hepatitis disease management program | _Ttl Hepatitis_ → `Observation.valueBoolean` (716, tanpa BQ)<br>_Ttl Hepatitis Lain_ → `Observation.component.code` (718, tanpa BQ) |
| 140 | 720–725 | Observation | – | – | _Ttl Sifilis_ → `Observation.valueBoolean` (722, tanpa BQ)<br>_Ttl Sifilis Lain_ → `Observation.component.code` (724, tanpa BQ) |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 78 |
| ServiceRequest | 12 |
| DiagnosticReport | 11 |
| Procedure | 10 |
| Specimen | 10 |
| Condition | 5 |
| Practitioner | 2 |
| Immunization | 2 |
| MedicationDispense | 2 |
| Medication | 2 |
| PractitionerRole | 2 |
| Patient | 1 |
| Encounter | 1 |
| EpisodeOfCare | 1 |
| MedicationRequest | 1 |
| **Total** | **140** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 22 | EpisodeOfCare | `EpisodeOfCare.type` | ANC | Antenatal Care | http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type |
| 2 | 26 | Observation | `Observation.code.coding` | 18185-9 | Gestational age | http://loinc.org |
| 3 | 27 | Observation | `Observation.code.coding` | ANC.B6.DE17 | Gestational age | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 4 | 31 | Observation | `Observation.code.coding` | 32418-6 | Obstetric trimester Stated | http://loinc.org |
| 5 | 32 | Observation | `Observation.code.coding` | ANC.SS.DE13 | Trimester ke | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 6 | 37 | Encounter | `Encounter.identifier` | K1M | Tidak ada | http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC |
| 7 | 38 | Encounter | `Encounter.identifier` | K1A | Tidak ada | http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC |
| 8 | 39 | Encounter | `Encounter.identifier` | K2 | Tidak ada | http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC |
| 9 | 40 | Encounter | `Encounter.identifier` | K3 | Tidak ada | http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC |
| 10 | 41 | Encounter | `Encounter.identifier` | K4 | Tidak ada | http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC |
| 11 | 42 | Encounter | `Encounter.identifier` | K5 | Tidak ada | http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC |
| 12 | 43 | Encounter | `Encounter.identifier` | K6 | Tidak ada | http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC |
| 13 | 52 | Observation | `Observation.code.coding` | 29463-7 | Body weight | http://loinc.org |
| 14 | 53 | Observation | `Observation.code.coding` | ANC.B8.DE3 | Current weight | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 15 | 57 | Observation | `Observation.code.coding` | 8302-2 | Body height | http://loinc.org |
| 16 | 58 | Observation | `Observation.code.coding` | ANC.B8.DE1 | Height | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 17 | 62 | Observation | `Observation.code.coding` | OC000010 | Indeks Massa Tubuh Sebelum Hamil | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 18 | 63 | Observation | `Observation.code.coding` | ANC.SS.DE58 | IMT Sebelum Hamil | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 19 | 67 | Observation | `Observation.interpretation.coding` | 43664005 | Normal weight | http://snomed.info/sct |
| 20 | 68 | Observation | `Observation.interpretation.coding` | 414915002 | Obese | http://snomed.info/sct |
| 21 | 69 | Observation | `Observation.interpretation.coding` | 238131007 | Overweight | http://snomed.info/sct |
| 22 | 70 | Observation | `Observation.interpretation.coding` | 248342006 | Underweight | http://snomed.info/sct |
| 23 | 72 | Observation | `Observation.code.coding` | 8480-6 | Systolic blood pressure | http://loinc.org |
| 24 | 73 | Observation | `Observation.code.coding` | ANC.B8.DE17 | Systolic blood pressure | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 25 | 77 | Observation | `Observation.code.coding` | 8462-4 | Diastolic blood pressure | http://loinc.org |
| 26 | 78 | Observation | `Observation.code.coding` | ANC.B8.DE19 | Diastolic blood pressure | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 27 | 82 | Observation | `Observation.code.coding` | 392570002 | Blood pressure finding | http://snomed.info/sct |
| 28 | 83 | Observation | `Observation.valueCodeableConcept.coding` | 2004005 | Normal blood pressure | http://snomed.info/sct |
| 29 | 84 | Observation | `Observation.valueCodeableConcept.coding` | 38341003 | Hypertension | http://snomed.info/sct |
| 30 | 86 | Observation | `Observation.code.coding` | 284473002 | Mid upper arm circumference | http://snomed.info/sct |
| 31 | 87 | Observation | `Observation.code.coding` | ANC.SS.DE3 | Lingkar Lengan Atas (LILA) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 32 | 91 | Observation | `Observation.interpretation` | OI000018 | Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 33 | 92 | Observation | `Observation.interpretation` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 34 | 93 | Observation | `Observation.interpretation` | OI000035 | Risiko Kurang Energi Kronis (KEK) | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 35 | 95 | Observation | `Observation.code.coding` | 11881-0 | Uterus Fundal height Tape measure | http://loinc.org |
| 36 | 96 | Observation | `Observation.code.coding` | ANC.B8.DE105 | Symphysis-fundal height | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 37 | 100 | Observation | `Observation.code.coding` | 32392-3 | Deep tendon reflex of Patellar | http://loinc.org |
| 38 | 101 | Observation | `Observation.valueCodeableConcept.coding` | 10828004 | Positive | http://snomed.info/sct |
| 39 | 102 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 40 | 104 | Observation | `Observation.code.coding` | 11948-7 | Fetal Heart rate US | http://loinc.org |
| 41 | 105 | Observation | `Observation.code.coding` | ANC.SS.DE38 | Denyut Jantung Janin (DJJ) USG | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 42 | 109 | Observation | `Observation.code.coding` | 289437007 | Finding of fetal heart rate | http://snomed.info/sct |
| 43 | 110 | Observation | `Observation.valueCodeableConcept.coding` | 289439005 | Fetal heart rate absent | http://snomed.info/sct |
| 44 | 111 | Observation | `Observation.valueCodeableConcept.coding` | 289441006 | Normal fetal heart rate | http://snomed.info/sct |
| 45 | 113 | Observation | `Observation.code.coding` | 249111004 | Engagement of head | http://snomed.info/sct |
| 46 | 114 | Observation | `Observation.code.coding` | ANC.SS.DE46 | Kepala Terhadap PAP | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 47 | 115 | Observation | `Observation.valueCodeableConcept.coding` | 249112006 | Head engaged | http://snomed.info/sct |
| 48 | 116 | Observation | `Observation.valueCodeableConcept.coding` | 62098001 | Belum masuk panggul | http://snomed.info/sct |
| 49 | 118 | Observation | `Observation.code.coding` | 89087-1 | Fetal Body weight Estimated | http://loinc.org |
| 50 | 119 | Observation | `Observation.code.coding` | ANC.SS.DE1 | Taksiran Berat Janin (TBJ) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 51 | 123 | Observation | `Observation.code.coding` | 72155-5 | Position in womb Fetus [RHEA] | http://loinc.org |
| 52 | 125 | Observation | `Observation.valueCodeableConcept.coding` | 73161006 | Transverse lie | http://snomed.info/sct |
| 53 | 126 | Observation | `Observation.dataAbsentReason` | unknown | Unknown | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 54 | 128 | Observation | `Observation.valueCodeableConcept.coding` | 63750008 | Oblique lie | http://snomed.info/sct |
| 55 | 129 | Observation | `Observation.valueCodeableConcept.coding` | 6096002 | Breech presentation | http://snomed.info/sct |
| 56 | 131 | Observation | `Observation.code.coding` | 246435002 | Number of fetuses | http://snomed.info/sct |
| 57 | 132 | Observation | `Observation.code.coding` | ANC.B8.DE109 | Number of fetuses | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 58 | 133 | Observation | `Observation.valueCodeableConcept.coding` | 16356006 | Multiple pregnancy | http://snomed.info/sct |
| 59 | 134 | Observation | `Observation.dataAbsentReason` | unknown | Unknown | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 60 | 135 | Observation | `Observation.valueCodeableConcept.coding` | 237244005 | Single pregnancy | http://snomed.info/sct |
| 61 | 137 | Observation | `Observation.code.coding` | 72155-5 | Position in womb Fetus [RHEA] | http://loinc.org |
| 62 | 138 | Observation | `Observation.code.coding` | ANC.B8.DE111 | Fetal presentation | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 63 | 139 | Observation | `Observation.valueCodeableConcept.coding` | 1209182005 | Cephalic fetal presentation | http://snomed.info/sct |
| 64 | 140 | Observation | `Observation.valueCodeableConcept.coding` | 6096002 | Breech presentation | http://snomed.info/sct |
| 65 | 144 | Immunization | `Immunization.vaccineCode` | VG139 | Td | http://sys-ids.kemkes.go.id/kfa |
| 66 | 155 | Procedure | `Procedure.code.coding` | 99.38 | Administration of tetanus toxoid | http://hl7.org/fhir/sid/icd-9-cm |
| 67 | 165 | Medication | `Medication.code` | 92000653 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula | http://sys-ids.kemkes.go.id/kf |
| 68 | 186 | Medication | `Medication.code` | 93015491 | Ferrous Fumarate 60 mg / Folic Acid 0,4 mg Tablet Salut Gula (TABLET TAMBAH DARAH) | http://sys-ids.kemkes.go.id/kf |
| 69 | 206 | ServiceRequest | `ServiceRequest.code` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 70 | 207 | Specimen | `Specimen.type` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 71 | 211 | Observation | `Observation.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 72 | 212 | Observation | `Observation.code.coding` | ANC.B9.DE175 | Blood hemoglobin test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 73 | 213 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 74 | 217 | Observation | `Observation.interpretation.coding` | 860635002 | No anemia present | http://snomed.info/sct |
| 75 | 218 | Observation | `Observation.interpretation.coding` | OI000034 | Anemia berat | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 76 | 219 | Observation | `Observation.interpretation.coding` | OI000032 | Anemia ringan | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 77 | 220 | Observation | `Observation.interpretation.coding` | OI000033 | Anemia sedang | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 78 | 222 | DiagnosticReport | `DiagnosticReport.code` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 79 | 224 | ServiceRequest | `ServiceRequest.code` | 2887-8 | Protein [Presence] in Urine | http://loinc.org |
| 80 | 225 | Specimen | `Specimen.type` | 122575003 | Urine specimen | http://snomed.info/sct |
| 81 | 228 | Observation | `Observation.code.coding` | 2887-8 | Protein [Presence] in Urine | http://loinc.org |
| 82 | 229 | Observation | `Observation.code.coding` | ANC.B9.DE114 | Urine test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 83 | 230 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 84 | 231 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 85 | 232 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 86 | 234 | Observation | `Observation.valueCodeableConcept.coding` | LA11841-6 | 1+ | http://loinc.org |
| 87 | 235 | Observation | `Observation.valueCodeableConcept.coding` | LA11842-4 | 2+ | http://loinc.org |
| 88 | 237 | DiagnosticReport | `DiagnosticReport.code` | 2887-8 | Protein [Presence] in Urine | http://loinc.org |
| 89 | 240 | ServiceRequest | `ServiceRequest.code` | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 90 | 241 | Specimen | `Specimen.type` | 122592007 | Acellular blood (serum or plasma) specimen (specimen)​ | http://snomed.info/sct |
| 91 | 244 | Observation | `Observation.code.coding` | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 92 | 247 | Observation | `Observation.interpretation.coding` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 93 | 248 | Observation | `Observation.interpretation.coding` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 94 | 249 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 95 | 251 | DiagnosticReport | `DiagnosticReport.code` | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 96 | 253 | ServiceRequest | `ServiceRequest.code` | 94537-8 | Hemoglobin panel - Blood by HPLC | http://loinc.org |
| 97 | 254 | Specimen | `Specimen.type` | 122555007 | Whole Blood | http://snomed.info/sct |
| 98 | 257 | Observation | `Observation.code.coding` | 94537-8 | Hemoglobin panel - Blood by HPLC | http://loinc.org |
| 99 | 258 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 100 | 259 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 101 | 261 | DiagnosticReport | `DiagnosticReport.code` | 94537-8 | Hemoglobin panel - Blood by HPLC | http://loinc.org |
| 102 | 263 | ServiceRequest | `ServiceRequest.code` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 103 | 264 | Specimen | `Specimen.type` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 104 | 268 | Observation | `Observation.code.coding` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 105 | 269 | Observation | `Observation.code.coding` | ANC.B9.DE96 | Syphilis test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 106 | 270 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 107 | 271 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 108 | 273 | DiagnosticReport | `DiagnosticReport.code` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 109 | 275 | ServiceRequest | `ServiceRequest.code` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 110 | 276 | Specimen | `Specimen.type` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 111 | 280 | Observation | `Observation.code.coding` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 112 | 281 | Observation | `Observation.code.coding` | ANC.B9.DE60 | Hepatitis B test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 113 | 282 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 114 | 283 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 115 | 285 | DiagnosticReport | `DiagnosticReport.code` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 116 | 287 | ServiceRequest | `ServiceRequest.code` | 7918-6 | HIV 1+2 Ab [Presence] in Serum | http://loinc.org |
| 117 | 288 | Specimen | `Specimen.type` | 119364003 | Serum specimen (specimen) | http://snomed.info/sct |
| 118 | 291 | Observation | `Observation.code.coding` | 7918-6 | HIV 1+2 Ab [Presence] in Serum | http://loinc.org |
| 119 | 292 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 120 | 293 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 121 | 295 | DiagnosticReport | `DiagnosticReport.code` | 7918-6 | HIV 1+2 Ab [Presence] in Serum | http://loinc.org |
| 122 | 297 | Observation | `Observation.code.coding` | 4241000179101 | Laboratory report | http://snomed.info/sct |
| 123 | 301 | ServiceRequest | `ServiceRequest.code` | 76772-3 | Plasmodium falciparum Ag [Presence] in Blood by Rapid immunoassay | http://loinc.org |
| 124 | 302 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 125 | 305 | Observation | `Observation.code.coding` | 76772-3 | Plasmodium falciparum Ag [Presence] in Blood by Rapid immunoassay | http://loinc.org |
| 126 | 306 | Observation | `Observation.dataAbsentReason` | not-performed | Not Performed | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 127 | 307 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 128 | 308 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 129 | 310 | DiagnosticReport | `DiagnosticReport.code` | 76772-3 | Plasmodium falciparum Ag [Presence] in Blood by Rapid immunoassay | http://loinc.org |
| 130 | 314 | ServiceRequest | `ServiceRequest.code` | 11477-7 | Microscopic observation [Identifier] in Sputum by Acid fast stain | http://loinc.org |
| 131 | 315 | Specimen | `Specimen.type` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 132 | 318 | Observation | `Observation.code.coding` | 11477-7 | Microscopic observation [Identifier] in Sputum by Acid fast stain | http://loinc.org |
| 133 | 319 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 134 | 320 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 135 | 322 | DiagnosticReport | `DiagnosticReport.code` | 11477-7 | Microscopic observation [Identifier] in Sputum by Acid fast stain | http://loinc.org |
| 136 | 324 | ServiceRequest | `ServiceRequest.code` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 137 | 325 | Specimen | `Specimen.type` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 138 | 328 | Observation | `Observation.code.coding` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 139 | 329 | Observation | `Observation.valueCodeableConcept.coding` | LA11882-0 | Detected | http://loinc.org |
| 140 | 330 | Observation | `Observation.interpretation.coding` | POS | Positive | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 141 | 331 | Observation | `Observation.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://loinc.org |
| 142 | 332 | Observation | `Observation.interpretation.coding` | NEG | Negative | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 143 | 334 | DiagnosticReport | `DiagnosticReport.code` | 88874-3 | Mycobacterium tuberculosis complex DNA [Presence] in Isolate or Specimen by Molecular genetics method | http://loinc.org |
| 144 | 339 | Observation | `Observation.code.coding` | CUSTOM | CUSTOM | CUSTOM |
| 145 | 343 | Procedure | `Procedure.code.coding` | 88.78 | Diagnostic ultrasound of gravid uterus | http://hl7.org/fhir/sid/icd-9-cm |
| 146 | 352 | Observation | `Observation.code.coding` | 32418-6 | Obstetric trimester Stated | http://loinc.org |
| 147 | 353 | Observation | `Observation.code.coding` | ANC.SS.DE13 | Trimester ke | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 148 | 356 | Condition | `Condition.code.coding` | O13 | Gestational [pregnancy-induced] hypertension without signification proteinuria | http://hl7.org/fhir/sid/icd-10 |
| 149 | 357 | Condition | `Condition.code.coding` | O21.9 | Vomiting of pregnancy, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 150 | 358 | Condition | `Condition.code.coding` | O25 | Malnutrition in pregnancy | http://hl7.org/fhir/sid/icd-10 |
| 151 | 359 | Condition | `Condition.code.coding` | O14.9 | Pre-eclampsia, unspecified | http://hl7.org/fhir/sid/icd-10 |
| 152 | 367 | PractitionerRole | `PractitionerRole.code` | 309453006 | Registered midwife | http://snomed.info/sct |
| 153 | 368 | PractitionerRole | `PractitionerRole.code` | 309367003 | Obstetrician and gynecologist | http://snomed.info/sct |
| 154 | 369 | PractitionerRole | `PractitionerRole.code` | 309343006 | Physician | http://snomed.info/sct |
| 155 | 370 | PractitionerRole | `PractitionerRole.code` | 106292003 | Professional nurse | http://snomed.info/sct |
| 156 | 382 | Observation | `Observation.code.coding` | 8867-4 | Heart rate | http://loinc.org |
| 157 | 387 | Observation | `Observation.code.coding` | 9279-1 | Respiratory rate | http://loinc.org |
| 158 | 408 | ServiceRequest | `ServiceRequest.code.coding` | 5292-8 | Reagin Ab [Presence] in Serum by VDRL | http://loinc.org |
| 159 | 410 | Observation | `Observation.code.coding` | 5292-8 | Reagin Ab [Presence] in Serum by VDRL | http://loinc.org |
| 160 | 414 | DiagnosticReport | `DiagnosticReport.code` | 5292-8 | Reagin Ab [Presence] in Serum by VDRL | http://loinc.org |
| 161 | 416 | Immunization | `Immunization.vaccineCode` | VG139 | Td | http://sys-ids.kemkes.go.id/kfa |
| 162 | 423 | Observation | `Observation.code.coding` | 8665-2 | Last menstrual period start date | http://loinc.org |
| 163 | 424 | Observation | `Observation.code.coding` | ANC.B6.DE14 | Last menstrual period (LMP) date | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 164 | 427 | Observation | `Observation.code.coding` | 11778-8 | Delivery date Estimated | http://loinc.org |
| 165 | 428 | Observation | `Observation.code.coding` | ANC.B6.DE22 | Expected date of delivery (EDD) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 166 | 433 | Observation | `Observation.code.coding` | 11948-7 | Fetal Heart rate US | http://loinc.org |
| 167 | 434 | Observation | `Observation.code.coding` | ANC.SS.DE38 | Denyut Jantung Janin (DJJ) USG | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 168 | 438 | Observation | `Observation.code.coding` | 11888-5 | Gestational age US composite estimate | http://loinc.org |
| 169 | 439 | Observation | `Observation.code.coding` | ANC.B6.DE20 | Ultrasound | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 170 | 443 | Observation | `Observation.code.coding` | 271692001 | Presentation of fetus | http://snomed.info/sct |
| 171 | 444 | Observation | `Observation.code.coding` | ANC.SS.DE41 | Letak Janin USG | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 172 | 446 | Observation | `Observation.valueCodeableConcept.coding` | 6096002 | Breech presentation | http://snomed.info/sct |
| 173 | 447 | Observation | `Observation.valueCodeableConcept.coding` | 398236008 | Intrauterine | http://snomed.info/sct |
| 174 | 448 | Observation | `Observation.valueCodeableConcept.coding` | 1209182005 | Cephalic fetal presentation | http://snomed.info/sct |
| 175 | 449 | Observation | `Observation.valueCodeableConcept.coding` | 288203005 | Transverse/oblique lie | http://snomed.info/sct |
| 176 | 452 | Procedure | `Procedure.code.coding` | 88.78 | Diagnostic ultrasound of gravid uterus | http://hl7.org/fhir/sid/icd-9-cm |
| 177 | 461 | Observation | `Observation.component.code` | 74964007 | Other | http://snomed.info/sct |
| 178 | 464 | Observation | `Observation.code.coding` | 736286003 | Hypertension clinical management plan | http://snomed.info/sct |
| 179 | 466 | Observation | `Observation.component.code` | 135840009 | Blood pressure monitoring | http://snomed.info/sct |
| 180 | 470 | Observation | `Observation.component.code` | 387672006 | Fetal monitoring | http://snomed.info/sct |
| 181 | 472 | Observation | `Observation.component.code` | 74964007 | Other | http://snomed.info/sct |
| 182 | 477 | Observation | `Observation.component.code` | 135840009 | Blood pressure monitoring | http://snomed.info/sct |
| 183 | 481 | Observation | `Observation.component.code` | 387672006 | Fetal monitoring | http://snomed.info/sct |
| 184 | 483 | Observation | `Observation.component.code` | 308116003 | Antihypertensive therapy | http://snomed.info/sct |
| 185 | 489 | Observation | `Observation.component.code` | 74964007 | Other | http://snomed.info/sct |
| 186 | 497 | Procedure | `Procedure.code.coding` | 11816003 | Diet education | http://snomed.info/sct |
| 187 | 506 | Procedure | `Procedure.code.coding` | 171054004 | Pregnancy diet education | http://snomed.info/sct |
| 188 | 512 | Observation | `Observation.code.coding` | 385821000 | Infection control management | http://snomed.info/sct |
| 189 | 514 | Observation | `Observation.component.code` | 709541000 | Administration of antipyretic | http://snomed.info/sct |
| 190 | 516 | Observation | `Observation.component.code` | 281789004 | Antibiotic therapy | http://snomed.info/sct |
| 191 | 524 | Procedure | `Procedure.code.coding` | 363001008 | Cardiovascular education | http://snomed.info/sct |
| 192 | 530 | Observation | `Observation.code.coding` | 1284934003 | Human immunodeficiency virus management program | http://snomed.info/sct |
| 193 | 533 | Observation | `Observation.code.coding` | 1280002000 | Tuberculosis management program | http://snomed.info/sct |
| 194 | 542 | Observation | `Observation.component.code` | 3457005 | Patient referral | http://snomed.info/sct |
| 195 | 546 | ServiceRequest | `ServiceRequest.code.coding` | 737492002 | Outpatient care management | http://snomed.info/sct |
| 196 | 561 | Observation | `Observation.code.coding` | 289437007 | Finding of fetal heart rate | http://snomed.info/sct |
| 197 | 562 | Observation | `Observation.valueCodeableConcept.coding` | 289441006 | Normal fetal heart rate | http://snomed.info/sct |
| 198 | 563 | Observation | `Observation.valueCodeableConcept.coding` | 312668007 | Abnormal fetal heart rate | http://snomed.info/sct |
| 199 | 566 | Observation | `Observation.code.coding` | 72155-5 | Position in womb Fetus [RHEA] | http://loinc.org |
| 200 | 568 | Observation | `Observation.valueCodeableConcept.coding` | 73161006 | Transverse lie | http://snomed.info/sct |
| 201 | 569 | Observation | `Observation.dataAbsentReason` | unknown | Unknown | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 202 | 571 | Observation | `Observation.valueCodeableConcept.coding` | 63750008 | Oblique lie | http://snomed.info/sct |
| 203 | 572 | Observation | `Observation.valueCodeableConcept.coding` | 6096002 | Breech presentation | http://snomed.info/sct |
| 204 | 574 | Observation | `Observation.code.coding` | 249111004 | Engagement of head | http://loinc.org |
| 205 | 575 | Observation | `Observation.code.coding` | ANC.SS.DE46 | Kepala Terhadap PAP | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 206 | 576 | Observation | `Observation.valueCodeableConcept.coding` | 62098001 | Head not engaged | http://snomed.info/sct |
| 207 | 577 | Observation | `Observation.valueCodeableConcept.coding` | 249112006 | Head engaged | http://snomed.info/sct |
| 208 | 579 | Observation | `Observation.code.coding` | 89087-1 | Fetal Body weight Estimated | http://loinc.org |
| 209 | 580 | Observation | `Observation.code.coding` | ANC.SS.DE1 | Taksiran Berat Janin (TBJ) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 210 | 584 | Observation | `Observation.code.coding` | 72155-5 | Position in womb Fetus [RHEA] | http://loinc.org |
| 211 | 585 | Observation | `Observation.code.coding` | ANC.B8.DE111 | Fetal presentation | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 212 | 586 | Observation | `Observation.valueCodeableConcept.coding` | 1209182005 | Cephalic fetal presentation | http://snomed.info/sct |
| 213 | 587 | Observation | `Observation.valueCodeableConcept.coding` | 6096002 | Breech presentation | http://snomed.info/sct |
| 214 | 591 | Observation | `Observation.code.coding` | 289437007 | Finding of fetal heart rate | http://snomed.info/sct |
| 215 | 592 | Observation | `Observation.valueCodeableConcept.coding` | 289439005 | Fetal heart rate absent | http://snomed.info/sct |
| 216 | 593 | Observation | `Observation.valueCodeableConcept.coding` | 289441006 | Normal fetal heart rate | http://snomed.info/sct |
| 217 | 595 | Observation | `Observation.code.coding` | 11948-7 | Fetal Heart rate US | http://loinc.org |
| 218 | 596 | Observation | `Observation.code.coding` | ANC.SS.DE38 | Denyut Jantung Janin (DJJ) USG | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 219 | 600 | Observation | `Observation.code.coding` | 72155-5 | Position in womb Fetus [RHEA] | http://loinc.org |
| 220 | 602 | Observation | `Observation.valueCodeableConcept.coding` | 73161006 | Transverse lie | http://snomed.info/sct |
| 221 | 603 | Observation | `Observation.dataAbsentReason` | unknown | Unknown | http://terminology.hl7.org/CodeSystem/data-absent-reason |
| 222 | 605 | Observation | `Observation.valueCodeableConcept.coding` | 63750008 | Oblique lie | http://snomed.info/sct |
| 223 | 606 | Observation | `Observation.valueCodeableConcept.coding` | 6096002 | Breech presentation | http://snomed.info/sct |
| 224 | 608 | Observation | `Observation.code.coding` | 249111004 | Engagement of head | http://loinc.org |
| 225 | 609 | Observation | `Observation.code.coding` | ANC.SS.DE46 | Kepala Terhadap PAP | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 226 | 610 | Observation | `Observation.valueCodeableConcept.coding` | 62098001 | Head not engaged | http://snomed.info/sct |
| 227 | 611 | Observation | `Observation.valueCodeableConcept.coding` | 249112006 | Head engaged | http://snomed.info/sct |
| 228 | 613 | Observation | `Observation.code.coding` | 89087-1 | Fetal Body weight Estimated | http://loinc.org |
| 229 | 614 | Observation | `Observation.code.coding` | ANC.SS.DE1 | Taksiran Berat Janin (TBJ) | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 230 | 618 | Observation | `Observation.code.coding` | 72155-5 | Position in womb Fetus [RHEA] | http://loinc.org |
| 231 | 619 | Observation | `Observation.code.coding` | ANC.B8.DE111 | Fetal presentation | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 232 | 620 | Observation | `Observation.valueCodeableConcept.coding` | 1209182005 | Cephalic fetal presentation | http://snomed.info/sct |
| 233 | 636 | Observation | `Observation.code.coding` | CUSTOM | CUSTOM | http://snomed.info/sct |
| 234 | 640 | Observation | `Observation.code.coding` | CUSTOM | CUSTOM | http://snomed.info/sct |
| 235 | 644 | Observation | `Observation.code.coding` | CUSTOM | CUSTOM | http://snomed.info/sct |
| 236 | 648 | Observation | `Observation.code.coding` | CUSTOM | CUSTOM | http://snomed.info/sct |
| 237 | 652 | Procedure | `Procedure.code` | 441041000124100 | Counseling about nutrition | http://snomed.info/sct |
| 238 | 659 | Observation | `Observation.code.coding` | 11727-5 | Fetal Body weight estimated by US | http://loinc.org |
| 239 | 664 | Observation | `Observation.code.coding` | 72155-5 | Position in womb Fetus [RHEA] | http://loinc.org |
| 240 | 665 | Observation | `Observation.code.coding` | ANC.B8.DE111 | Fetal presentation | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 241 | 666 | Observation | `Observation.valueCodeableConcept.coding` | 1209182005 | Cephalic fetal presentation | http://snomed.info/sct |
| 242 | 667 | Observation | `Observation.valueCodeableConcept.coding` | 6096002 | Breech presentation | http://snomed.info/sct |
| 243 | 668 | Observation | `Observation.valueCodeableConcept.coding` | 6096002 | Breech presentation | http://snomed.info/sct |
| 244 | 670 | Observation | `Observation.code.coding` | 1285244000 | Mean arterial pressure | http://loinc.org |
| 245 | 674 | Observation | `Observation.interpretation` | N | Normal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 246 | 675 | Observation | `Observation.interpretation` | A | Abnormal | http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation |
| 247 | 677 | PractitionerRole | `PractitionerRole.code.coding` | doctor | Doctor | http://terminology.hl7.org/CodeSystem/practitioner-role |
| 248 | 678 | PractitionerRole | `PractitionerRole.code.coding` | 309367003 | Obstetrician and gynecologist | http://snomed.info/sct |
| 249 | 685 | Condition | `Condition.code` | 40733004 | Infectious disease | http://snomed.info/sct |
| 250 | 690 | Observation | `Observation.code.coding` | CUSTOM | CUSTOM | CUSTOM |
| 251 | 695 | Procedure | `Procedure.code` | 25156005 | Intravenous feeding of patient | http://snomed.info/sct |
| 252 | 699 | Procedure | `Procedure.code` | 161664006 | History of blood transfusion | http://snomed.info/sct |
| 253 | 703 | Condition | `Condition.code.coding` | 161445009 | H/O: diabetes mellitus | http://snomed.info/sct |
| 254 | 707 | Observation | `Observation.code.coding` | 698472009 | Blood glucose monitoring | http://snomed.info/sct |
| 255 | 711 | Observation | `Observation.code.coding` | CUSTOM | CUSTOM | CUSTOM |
| 256 | 715 | Observation | `Observation.code.coding` | 1285318003 | Viral hepatitis disease management program | http://snomed.info/sct |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 97 |
| http://loinc.org | 82 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 32 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 9 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC | 7 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 7 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 6 |
| http://hl7.org/fhir/sid/icd-10 | 4 |
| http://hl7.org/fhir/sid/icd-9-cm | 3 |
| CUSTOM | 3 |
| http://sys-ids.kemkes.go.id/kfa | 2 |
| http://sys-ids.kemkes.go.id/kf | 2 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 1 |
| http://terminology.hl7.org/CodeSystem/practitioner-role | 1 |
| **Total** | **256** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 46 | – | Kode Lembaga | Organization | `Organization.identifier` |
| 47 | – | Nama Lembaga | Organization | `Organization.name` |
| 48 | – | Resiko Lain | – | `` |
| 161 | – | Diberikan Fe | – | `` |
| 216 | – | Anemia | – | `` |
| 233 | – | Pro Urin Hasil | – | `` |
| 238 | – | Reduksi | – | `` |
| 299 | – | Serologi | – | `` |
| 311 | – | Obat Malaria | – | `` |
| 335 | – | Obat Tb | – | `` |
| 337 | – | Tbc Lain | – | `` |
| 346 | – | Dada | – | `` |
| 371 | – | Lokasi | – | `` |
| 395 | – | Tata Laksana | – | `` |
| 396 | – | Kedatangan | – | `` |
| 397 | – | Nama Faskes Perujuk | – | `` |
| 398 | – | Lokasi Screening Lain | – | `` |
| 399 | – | Status Lembaga | – | `` |
| 402 | – | Pemeriksaan Malaria | – | `` |
| 430 | – | Ki | – | `` |
| 458 | – | Tata Laksana Anemia Dosis | – | `` |
| 538 | – | Tatalaksana Lainnya | – | `` |
| 540 | – | Jenis Tatalaksana Lain | – | `` |
| 541 | – | Isian Tatalaksana Lain | – | `` |
| 550 | – | Hasil Serologi | – | `` |
| 559 | – | Pelayanan Lainnya | – | `` |
| 564 | – | Detak Jantung Janin3 | – | `` |
| 623 | – | Hiv Lain | – | `` |
| 624 | – | Rujuk Kab | – | `` |
| 625 | – | Fe Saatini | – | `` |
| 626 | – | Ket Positifhiv | – | `` |
| 627 | – | Tata Laksana Obat Malaria | – | `` |
| 628 | – | Lainnya Malaria | – | `` |
| 629 | – | Kabupaten Rujukan | – | `` |
| 630 | – | Profilaksis Lainnya | – | `` |
| 631 | – | Status Pindahan | – | `` |
| 633 | – | Tfu Terdeteksi | – | `` |
| 656 | – | Cek Pelayanan Lainnya | – | `` |
| 657 | – | Test | – | `` |
| 679 | – | Gula Darah Puasa | – | `` |
| 680 | – | Gula Darah Post Prandial | – | `` |
| 688 | – | Hasil Infeksi | – | `` |
| 693 | – | Hasil Malaria | – | `` |
| 709 | – | Faktor Preeklamsia | – | `` |
| 717 | – | Obat Ttl Hepatitis | – | `` |
| 723 | – | Obat Ttl Sifilis | – | `` |
