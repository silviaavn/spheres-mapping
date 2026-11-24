# Output Form: ePuskesmas Laboratorium

Sumber: `mapping/phdt-data-dictionary-epus-lab.csv`
Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.
Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.

File terkait: [`output.md`](../output.md) (konsolidasi semua form) · [`frekuensi-payload.md`](../frekuensi-payload.md) · [`frekuensi-code.md`](../frekuensi-code.md) · [dictionary](../mapping/phdt-data-dictionary-epus-lab.csv)

## Ringkasan

| Item | Jumlah |
|---|---|
| Payload (`jumlah instance` = 1) | 309 |
| Code (`jumlah code` = 1) | 429 |
| Code unik (code + CodeSystem) | 139 |
| Code SP (`http://terminology.kemkes.go.id/sp`) | 0 |
| Variabel BQ (unik) | 0 |
| Variabel raw (variabel dictionary; belum ada file mentah) | 22 |

## Payload

| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |
|---|---|---|---|---|---|
| 1 | 2–3 | Encounter | – | – | _No_ → `Encounter.identifier` (2, tanpa BQ)<br>_Ruangan Pengirim_ → `Encounter.hospitaliz ation.admitSource.co ding` (50, tanpa BQ) |
| 2 | 4–4 | ServiceRequest | – | – | _Tanggal order_ → `ServiceRequest.authoredOn` (4, tanpa BQ) |
| 3 | 5–23 | Specimen | 119361006 | Plasma | _Tanggal sample_ → `Specimen.collectedDateTime` (5, tanpa BQ) |
| 4 | 24–49 | Patient | – | – | _Nama Pasien_ → `Patient.name` (24, tanpa BQ)<br>_Tempat & Tgl Lahir_ → `Patient.extension:birthPlace` (25, tanpa BQ)<br>_ID KTP/Paspor_ → `Patient.identifier.value` (29, tanpa BQ)<br>_Alamat_ → `Patient.address.line` (33, tanpa BQ)<br>_Kelurahan_ → `Patient.address.extension:administrativeCode.extension:village` (35, tanpa BQ)<br>_No.eRM_ → `Patient.identifier.value` (38, tanpa BQ)<br>_No. RM Lama_ → `Patient.name` (39, tanpa BQ)<br>_No. Dokumen RM_ → `Patient.name` (42, tanpa BQ)<br>_Jenis Kelamin_ → `Patient.gender` (45, tanpa BQ)<br>_Umur_ → `Patient.birthDate` (47, tanpa BQ)<br>_Email_ → `Patient.telecom` (48, tanpa BQ)<br>_Nomor Telp/HP_ → `Patient.telecom` (49, tanpa BQ) |
| 5 | 52–59 | Coverage | – | – | _Asuransi_ → `Coverage.subsriberId` (52, tanpa BQ)<br>_Nomor Asuransi_ → `Coverage.identifier.system` (59, tanpa BQ) |
| 6 | 60–61 | Observation | – | – | _Penanggung jawab_ → `Observation.performer.reference` (60, tanpa BQ)<br>_Pemeriksa_ → `Observation.performer.reference` (61, tanpa BQ) |
| 7 | 69–71 | ServiceRequest | 89371-9 | MTB complex DNA and rpoB RIF resistance mutation panel [Presence] | – |
| 8 | 72–79 | Observation | – | – | – |
| 9 | 80–89 | DiagnosticReport | 89371-9 | MTB complex DNA and rpoB RIF resistance mutation panel [Presence] | – |
| 10 | 90–99 | ServiceRequest | – | – | – |
| 11 | 103–110 | Specimen | – | – | – |
| 12 | 111–122 | Observation | 94500-6 | SARS-CoV-2 (COVID-19) RNA [Presence] in Respiratory specimen by NAA with probe detection | – |
| 13 | 123–134 | DiagnosticReport | 94500-6 | SARS-CoV-2 (COVID-19) RNA [Presence] in Respiratory specimen by NAA with probe detection | – |
| 14 | 135–144 | ServiceRequest | – | – | – |
| 15 | 148–155 | Specimen | – | – | – |
| 16 | 156–167 | Observation | 23539-0 | Tuberculosis reaction wheal [Diameter] --3 days post dose mammalian tuberculin intradermal | – |
| 17 | 168–179 | DiagnosticReport | 23539-0 | Tuberculosis reaction wheal [Diameter] --3 days post dose mammalian tuberculin intradermal | – |
| 18 | 180–189 | ServiceRequest | – | – | – |
| 19 | 193–200 | Specimen | – | – | – |
| 20 | 201–214 | Observation | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | – |
| 21 | 215–226 | DiagnosticReport | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | – |
| 22 | 227–236 | ServiceRequest | – | – | – |
| 23 | 240–247 | Specimen | – | – | – |
| 24 | 248–260 | Observation | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | – |
| 25 | 261–272 | DiagnosticReport | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | – |
| 26 | 273–282 | ServiceRequest | – | – | – |
| 27 | 286–293 | Specimen | – | – | – |
| 28 | 294–306 | Observation | 2093-3 | Cholesterol [Mass/volume] in Serum or Plasma | – |
| 29 | 307–318 | DiagnosticReport | 2093-3 | Cholesterol [Mass/volume] in Serum or Plasma | – |
| 30 | 319–328 | ServiceRequest | – | – | – |
| 31 | 332–339 | Specimen | – | – | – |
| 32 | 340–352 | Observation | 3084-1 | Urate [Mass/volume] in Serum or Plasma | – |
| 33 | 353–364 | DiagnosticReport | 3084-1 | Urate [Mass/volume] in Serum or Plasma | – |
| 34 | 366–375 | ServiceRequest | – | – | – |
| 35 | 379–386 | Specimen | – | – | – |
| 36 | 387–399 | Observation | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | – |
| 37 | 400–411 | DiagnosticReport | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | – |
| 38 | 412–421 | ServiceRequest | – | – | – |
| 39 | 425–432 | Specimen | – | – | – |
| 40 | 433–445 | Observation | 41653-7 | Glucose [Mass/volume] in Capillary blood by Glucometer | – |
| 41 | 446–457 | DiagnosticReport | 41653-7 | Glucose [Mass/volume] in Capillary blood by Glucometer | – |
| 42 | 458–467 | ServiceRequest | – | – | – |
| 43 | 471–478 | Specimen | – | – | – |
| 44 | 479–491 | Observation | 2571-8 | Triglyceride [Mass/volume] in Serum or Plasma | – |
| 45 | 492–503 | DiagnosticReport | 2571-8 | Triglyceride [Mass/volume] in Serum or Plasma | – |
| 46 | 504–513 | ServiceRequest | – | – | – |
| 47 | 517–524 | Specimen | – | – | – |
| 48 | 525–537 | Observation | 2085-9 | Cholesterol in HDL [Mass/volume] in Serum or Plasma | – |
| 49 | 538–549 | DiagnosticReport | 2085-9 | Cholesterol in HDL [Mass/volume] in Serum or Plasma | – |
| 50 | 550–559 | ServiceRequest | – | – | – |
| 51 | 563–570 | Specimen | – | – | – |
| 52 | 571–583 | Observation | 2089-1 | Cholesterol in LDL [Mass/volume] in Serum or Plasma | – |
| 53 | 584–595 | DiagnosticReport | 2089-1 | Cholesterol in LDL [Mass/volume] in Serum or Plasma | – |
| 54 | 596–605 | ServiceRequest | – | – | – |
| 55 | 609–616 | Specimen | – | – | – |
| 56 | 617–629 | Observation | 1751-7 | Albumin [Mass/volume] in Serum or Plasma | – |
| 57 | 630–641 | DiagnosticReport | 1751-7 | Albumin [Mass/volume] in Serum or Plasma | – |
| 58 | 642–651 | ServiceRequest | – | – | – |
| 59 | 655–662 | Specimen | – | – | – |
| 60 | 663–675 | Observation | 2324-2 | Gamma glutamyl transferase [Enzymatic activity/volume] in Serum or Plasma | – |
| 61 | 676–687 | DiagnosticReport | 2324-2 | Gamma glutamyl transferase [Enzymatic activity/volume] in Serum or Plasma | – |
| 62 | 688–697 | ServiceRequest | – | – | – |
| 63 | 701–708 | Specimen | – | – | – |
| 64 | 709–721 | Observation | 4548-4 | Hemoglobin A1c/Hemoglobin.total in Blood | – |
| 65 | 722–733 | DiagnosticReport | 4548-4 | Hemoglobin A1c/Hemoglobin.total in Blood | – |
| 66 | 734–743 | ServiceRequest | – | – | – |
| 67 | 747–754 | Specimen | – | – | – |
| 68 | 755–767 | Observation | 1920-8 | Aspartate aminotransferase [Enzymatic activity/volume] in Serum or Plasma | – |
| 69 | 768–779 | DiagnosticReport | 1920-8 | Aspartate aminotransferase [Enzymatic activity/volume] in Serum or Plasma | – |
| 70 | 780–789 | ServiceRequest | – | – | – |
| 71 | 793–800 | Specimen | – | – | – |
| 72 | 801–813 | Observation | 1742-6 | Alanine aminotransferase [Enzymatic activity/volume] in Serum or Plasma | – |
| 73 | 814–825 | DiagnosticReport | 1742-6 | Alanine aminotransferase [Enzymatic activity/volume] in Serum or Plasma | – |
| 74 | 826–835 | ServiceRequest | – | – | – |
| 75 | 839–846 | Specimen | – | – | – |
| 76 | 847–859 | Observation | 2157-6 | Creatine kinase [Enzymatic activity/volume] in Serum or Plasma | – |
| 77 | 860–871 | DiagnosticReport | 2157-6 | Creatine kinase [Enzymatic activity/volume] in Serum or Plasma | – |
| 78 | 872–881 | ServiceRequest | – | – | – |
| 79 | 885–892 | Specimen | – | – | – |
| 80 | 893–905 | Observation | 20977-5 | Urea [Mass/volume] in Blood | – |
| 81 | 906–917 | DiagnosticReport | 20977-5 | Urea [Mass/volume] in Blood | – |
| 82 | 918–927 | ServiceRequest | – | – | – |
| 83 | 931–938 | Specimen | – | – | – |
| 84 | 939–951 | Observation | 2885-2 | Protein [Mass/volume] in Serum or Plasma | – |
| 85 | 952–963 | DiagnosticReport | 2885-2 | Protein [Mass/volume] in Serum or Plasma | – |
| 86 | 964–973 | ServiceRequest | – | – | – |
| 87 | 977–984 | Specimen | – | – | – |
| 88 | 985–997 | Observation | 1521-4 | Glucose [Mass/volume] in Serum or Plasma --2 hours post meal | – |
| 89 | 998–1009 | DiagnosticReport | 1521-4 | Glucose [Mass/volume] in Serum or Plasma --2 hours post meal | – |
| 90 | 1010–1019 | ServiceRequest | – | – | – |
| 91 | 1023–1030 | Specimen | – | – | – |
| 92 | 1031–1036 | Observation | – | – | – |
| 93 | 1037–1040 | Observation | – | – | – |
| 94 | 1041–1044 | Observation | – | – | – |
| 95 | 1045–1048 | Observation | – | – | – |
| 96 | 1049–1052 | Observation | – | – | – |
| 97 | 1053–1056 | Observation | – | – | – |
| 98 | 1057–1067 | Observation | – | – | – |
| 99 | 1068–1079 | DiagnosticReport | 58410-2 | CBC panel - Blood by Automated count | – |
| 100 | 1080–1089 | ServiceRequest | – | – | – |
| 101 | 1093–1100 | Specimen | – | – | – |
| 102 | 1101–1114 | Observation | 718-7 | Hemoglobin [Mass/volume] in Blood | – |
| 103 | 1115–1126 | DiagnosticReport | 718-7 | Hemoglobin [Mass/volume] in Blood | – |
| 104 | 1127–1136 | ServiceRequest | – | – | – |
| 105 | 1140–1147 | Specimen | – | – | – |
| 106 | 1148–1160 | Observation | – | – | – |
| 107 | 1161–1172 | DiagnosticReport | 26453-1 | Erythrocytes [#/volume] in Blood | – |
| 108 | 1173–1182 | ServiceRequest | – | – | – |
| 109 | 1186–1193 | Specimen | – | – | – |
| 110 | 1194–1206 | Observation | – | – | – |
| 111 | 1207–1218 | DiagnosticReport | 26464-8 | Leukocytes [#/volume] in Blood | – |
| 112 | 1219–1228 | ServiceRequest | – | – | – |
| 113 | 1232–1239 | Specimen | – | – | – |
| 114 | 1240–1252 | Observation | – | – | – |
| 115 | 1253–1264 | DiagnosticReport | 26515-7 | Platelets [#/volume] in Blood | – |
| 116 | 1265–1274 | ServiceRequest | – | – | – |
| 117 | 1278–1285 | Specimen | – | – | – |
| 118 | 1286–1298 | Observation | – | – | – |
| 119 | 1299–1310 | DiagnosticReport | 20570-8 | Hematocrit [Volume Fraction] of Blood | – |
| 120 | 1311–1320 | ServiceRequest | – | – | – |
| 121 | 1324–1331 | Specimen | – | – | – |
| 122 | 1332–1344 | Observation | – | – | – |
| 123 | 1345–1356 | DiagnosticReport | 11067-6 | Bleeding time | – |
| 124 | 1357–1366 | ServiceRequest | – | – | – |
| 125 | 1370–1377 | Specimen | – | – | – |
| 126 | 1378–1390 | Observation | – | – | – |
| 127 | 1391–1402 | DiagnosticReport | 30341-2 | Erythrocyte sedimentation rate [Velocity] in Red Blood Cells | – |
| 128 | 1403–1412 | ServiceRequest | – | – | – |
| 129 | 1416–1423 | Specimen | – | – | – |
| 130 | 1424–1435 | Observation | – | – | – |
| 131 | 1436–1447 | DiagnosticReport | 17009-2 | IgM [Presence] in Serum | – |
| 132 | 1448–1457 | ServiceRequest | – | – | – |
| 133 | 1461–1468 | Specimen | – | – | – |
| 134 | 1469–1481 | Observation | – | – | – |
| 135 | 1482–1493 | DiagnosticReport | 3183-1 | Clotting time of Blood by Lee White method | – |
| 136 | 1494–1503 | ServiceRequest | – | – | – |
| 137 | 1507–1514 | Specimen | – | – | – |
| 138 | 1515–1526 | Observation | – | – | – |
| 139 | 1527–1538 | DiagnosticReport | 17007-6 | IgG [Presence] in Serum | – |
| 140 | 1539–1548 | ServiceRequest | – | – | – |
| 141 | 1552–1559 | Specimen | – | – | – |
| 142 | 1560–1572 | Observation | – | – | – |
| 143 | 1573–1584 | DiagnosticReport | 30428-7 | MCV [Entitic volume] | – |
| 144 | 1585–1594 | ServiceRequest | – | – | – |
| 145 | 1598–1605 | Specimen | – | – | – |
| 146 | 1606–1618 | Observation | – | – | – |
| 147 | 1619–1630 | DiagnosticReport | 28539-5 | MCH [Entitic mass] | – |
| 148 | 1631–1640 | ServiceRequest | – | – | – |
| 149 | 1644–1651 | Specimen | – | – | – |
| 150 | 1652–1664 | Observation | – | – | – |
| 151 | 1665–1676 | DiagnosticReport | 28540-3 | MCHC [Mass/volume] | – |
| 152 | 1677–1686 | ServiceRequest | – | – | – |
| 153 | 1690–1697 | Specimen | – | – | – |
| 154 | 1698–1710 | Observation | – | – | – |
| 155 | 1711–1722 | DiagnosticReport | 26511-6 | Neutrophils/100 leukocytes in Blood | – |
| 156 | 1723–1725 | ServiceRequest | 26464-8 | Leukocytes [#/volume] in Blood | – |
| 157 | 1726–1730 | Observation | – | – | – |
| 158 | 1731–1734 | Observation | – | – | – |
| 159 | 1735–1737 | Observation | – | – | – |
| 160 | 1738–1738 | Observation | – | – | – |
| 161 | 1739–1742 | DiagnosticReport | 26464-8 | Leukocytes [#/volume] in Blood | – |
| 162 | 1743–1751 | ServiceRequest | 26511-6 | Neutrophils/100 leukocytes in Blood | – |
| 163 | 1752–1756 | Observation | – | – | – |
| 164 | 1757–1760 | Observation | – | – | – |
| 165 | 1761–1764 | Observation | – | – | – |
| 166 | 1765–1768 | Observation | – | – | – |
| 167 | 1769–1772 | Observation | – | – | – |
| 168 | 1773–1776 | Observation | – | – | – |
| 169 | 1777–1780 | Observation | – | – | – |
| 170 | 1781–1784 | Observation | – | – | – |
| 171 | 1785–1788 | Observation | – | – | – |
| 172 | 1789–1798 | DiagnosticReport | 26511-6 | Neutrophils/100 leukocytes in Blood | – |
| 173 | 1799–1808 | ServiceRequest | – | – | – |
| 174 | 1812–1819 | Specimen | – | – | – |
| 175 | 1820–1832 | Observation | – | – | – |
| 176 | 1833–1844 | DiagnosticReport | 26478-8 | Lymphocytes/100 leukocytes in Blood | – |
| 177 | 1845–1854 | ServiceRequest | – | – | – |
| 178 | 1858–1865 | Specimen | – | – | – |
| 179 | 1866–1883 | Observation | 882-1 | ABO and Rh group [Type] in Blood | – |
| 180 | 1884–1895 | DiagnosticReport | 882-1 | ABO and Rh group [Type] in Blood | – |
| 181 | 1896–1905 | ServiceRequest | – | – | – |
| 182 | 1909–1922 | Observation | 883-9 | ABO group [Type] in Blood | – |
| 183 | 1923–1934 | DiagnosticReport | 883-9 | ABO group [Type] in Blood | – |
| 184 | 1935–1944 | ServiceRequest | – | – | – |
| 185 | 1948–1955 | Specimen | – | – | – |
| 186 | 1956–1967 | Observation | 17566-1 | Salmonella typhi O Ab [Presence] in Serum | – |
| 187 | 1968–1979 | DiagnosticReport | 17566-1 | Salmonella typhi O Ab [Presence] in Serum | – |
| 188 | 1980–1989 | ServiceRequest | – | – | – |
| 189 | 1993–2000 | Specimen | – | – | – |
| 190 | 2001–2012 | Observation | 22529-2 | Salmonella typhi H Ab [Presence] in Serum | – |
| 191 | 2013–2024 | DiagnosticReport | 22529-2 | Salmonella typhi H Ab [Presence] in Serum | – |
| 192 | 2025–2034 | ServiceRequest | – | – | – |
| 193 | 2038–2045 | Specimen | – | – | – |
| 194 | 2046–2058 | Observation | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | – |
| 195 | 2059–2070 | DiagnosticReport | – | – | – |
| 196 | 2071–2077 | ServiceRequest | 743-5 | Monocytes [#/volume] in Blood by Manual count | – |
| 197 | 2078–2087 | Observation | – | – | – |
| 198 | 2088–2094 | DiagnosticReport | 743-5 | Monocytes [#/volume] in Blood by Manual count | – |
| 199 | 2095–2104 | ServiceRequest | – | – | – |
| 200 | 2108–2115 | Specimen | – | – | – |
| 201 | 2116–2128 | Observation | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | – |
| 202 | 2129–2140 | DiagnosticReport | – | – | – |
| 203 | 2141–2150 | ServiceRequest | – | – | – |
| 204 | 2155–2162 | Specimen | – | – | – |
| 205 | 2163–2176 | Observation | 22464-2 | Reagin Ab [Presence] in Specimen | – |
| 206 | 2177–2188 | DiagnosticReport | – | – | – |
| 207 | 2189–2198 | ServiceRequest | – | – | – |
| 208 | 2202–2209 | Specimen | – | – | – |
| 209 | 2210–2221 | Observation | – | – | – |
| 210 | 2222–2233 | Observation | – | – | – |
| 211 | 2234–2245 | DiagnosticReport | 87546-8 | Dengue virus IgG and IgM panel - Serum Qualitative | – |
| 212 | 2246–2255 | ServiceRequest | – | – | – |
| 213 | 2259–2270 | Observation | – | – | – |
| 214 | 2271–2282 | DiagnosticReport | 29676-4 | Dengue virus IgG Ab [Presence] in Serum | – |
| 215 | 2283–2292 | ServiceRequest | – | – | – |
| 216 | 2296–2307 | Observation | – | – | – |
| 217 | 2308–2319 | DiagnosticReport | 25338-5 | Dengue virus IgM Ab [Presence] in Serum | – |
| 218 | 2320–2329 | ServiceRequest | – | – | – |
| 219 | 2333–2340 | Specimen | – | – | – |
| 220 | 2341–2353 | Observation | – | – | – |
| 221 | 2354–2365 | DiagnosticReport | 91064-6 | Dengue virus NS1 Ag [Presence] in Serum or Plasma by Immunoassay | – |
| 222 | 2366–2375 | ServiceRequest | – | – | – |
| 223 | 2379–2386 | Specimen | – | – | – |
| 224 | 2387–2399 | Observation | – | – | – |
| 225 | 2400–2411 | DiagnosticReport | 47085-6 | Plasmodium sp DNA [Presence] in Blood by NAA with probe detection | – |
| 226 | 2412–2421 | ServiceRequest | – | – | – |
| 227 | 2422–2424 | PractitionerRole | – | – | – |
| 228 | 2425–2434 | Observation | – | – | – |
| 229 | 2435–2445 | DiagnosticReport | 34534-8 | 12 lead EKG panel | – |
| 230 | 2446–2455 | ServiceRequest | – | – | – |
| 231 | 2456–2458 | PractitionerRole | – | – | – |
| 232 | 2459–2468 | Observation | – | – | – |
| 233 | 2469–2479 | DiagnosticReport | 11525-3 | US for pregnancy | – |
| 234 | 2480–2489 | ServiceRequest | – | – | – |
| 235 | 2490–2497 | Specimen | – | – | – |
| 236 | 2498–2508 | Observation | – | – | – |
| 237 | 2509–2520 | DiagnosticReport | 5778-6 | Color of Urine | – |
| 238 | 2521–2530 | ServiceRequest | – | – | – |
| 239 | 2534–2541 | Specimen | – | – | – |
| 240 | 2542–2552 | Observation | – | – | – |
| 241 | 2553–2564 | DiagnosticReport | 32167-9 | Clarity of Urine | – |
| 242 | 2565–2574 | ServiceRequest | – | – | – |
| 243 | 2578–2585 | Specimen | – | – | – |
| 244 | 2586–2598 | Observation | – | – | – |
| 245 | 2599–2610 | DiagnosticReport | 2756-5 | pH of Urine | – |
| 246 | 2611–2620 | ServiceRequest | – | – | – |
| 247 | 2624–2631 | Specimen | – | – | – |
| 248 | 2632–2644 | Observation | – | – | – |
| 249 | 2645–2656 | DiagnosticReport | 2965-2 | Specific gravity of Urine | – |
| 250 | 2657–2666 | ServiceRequest | – | – | – |
| 251 | 2670–2677 | Specimen | – | – | – |
| 252 | 2678–2694 | Observation | 2887-8 | Protein [Presence] in Urine | – |
| 253 | 2695–2706 | DiagnosticReport | 2887-8 | Protein [Presence] in Urine | – |
| 254 | 2707–2716 | ServiceRequest | – | – | – |
| 255 | 2720–2727 | Specimen | – | – | – |
| 256 | 2728–2739 | Observation | – | – | – |
| 257 | 2740–2751 | DiagnosticReport | 2349-9 | Glucose [Presence] in Urine | – |
| 258 | 2752–2761 | ServiceRequest | – | – | – |
| 259 | 2765–2772 | Specimen | – | – | – |
| 260 | 2773–2784 | Observation | – | – | – |
| 261 | 2785–2796 | DiagnosticReport | 33903-6 | Ketones [Presence] in Urine | – |
| 262 | 2797–2806 | ServiceRequest | – | – | – |
| 263 | 2810–2817 | Specimen | – | – | – |
| 264 | 2818–2829 | Observation | – | – | – |
| 265 | 2830–2841 | DiagnosticReport | 1977-8 | Bilirubin.total [Presence] in Urine | – |
| 266 | 2842–2851 | ServiceRequest | – | – | – |
| 267 | 2855–2862 | Specimen | – | – | – |
| 268 | 2863–2875 | Observation | – | – | – |
| 269 | 2876–2887 | DiagnosticReport | 34927-4 | Urobilinogen [Moles/volume] in Urine | – |
| 270 | 2888–2897 | ServiceRequest | – | – | – |
| 271 | 2901–2908 | Specimen | – | – | – |
| 272 | 2909–2920 | Observation | 105906-2 | Blood [Presence] in Urine | – |
| 273 | 2921–2932 | DiagnosticReport | 105906-2 | Blood [Presence] in Urine | – |
| 274 | 2933–2942 | ServiceRequest | – | – | – |
| 275 | 2946–2953 | Specimen | – | – | – |
| 276 | 2954–2965 | Observation | 32710-6 | Nitrite [Presence] in Urine | – |
| 277 | 2966–2977 | DiagnosticReport | 32710-6 | Nitrite [Presence] in Urine | – |
| 278 | 2978–2987 | ServiceRequest | – | – | – |
| 279 | 2991–2998 | Specimen | – | – | – |
| 280 | 2999–3010 | Observation | 105087-1 | Epithelial cells.squamous [Presence] in Urine | – |
| 281 | 3011–3022 | DiagnosticReport | 105087-1 | Epithelial cells.squamous [Presence] in Urine | – |
| 282 | 3023–3032 | ServiceRequest | – | – | – |
| 283 | 3036–3043 | Specimen | – | – | – |
| 284 | 3044–3055 | Observation | 105089-7 | Epithelial cells.non-squamous [Presence] in Urine | – |
| 285 | 3056–3067 | DiagnosticReport | 105089-7 | Epithelial cells.non-squamous [Presence] in Urine | – |
| 286 | 3068–3077 | ServiceRequest | – | – | – |
| 287 | 3081–3088 | Specimen | – | – | – |
| 288 | 3089–3100 | Observation | 85093-3 | Crystal casts [Presence] in Urine sediment by Light microscopy | – |
| 289 | 3101–3112 | DiagnosticReport | 85093-3 | Crystal casts [Presence] in Urine sediment by Light microscopy | – |
| 290 | 3113–3122 | ServiceRequest | – | – | – |
| 291 | 3126–3133 | Specimen | – | – | – |
| 292 | 3134–3146 | Observation | 105107-7 | Erythrocytes [#/area] in Urine sediment | – |
| 293 | 3147–3158 | DiagnosticReport | 105107-7 | Erythrocytes [#/area] in Urine sediment | – |
| 294 | 3159–3168 | ServiceRequest | – | – | – |
| 295 | 3172–3179 | Specimen | – | – | – |
| 296 | 3180–3192 | Observation | 105104-4 | Leukocytes [#/area] in Urine sediment | – |
| 297 | 3193–3204 | DiagnosticReport | 105104-4 | Leukocytes [#/area] in Urine sediment | – |
| 298 | 3205–3214 | ServiceRequest | – | – | – |
| 299 | 3218–3225 | Specimen | – | – | – |
| 300 | 3226–3238 | Observation | 105908-8 | Bacteria [#/area] in Urine sediment | – |
| 301 | 3239–3250 | DiagnosticReport | 105908-8 | Bacteria [#/area] in Urine sediment | – |
| 302 | 3251–3260 | ServiceRequest | – | – | – |
| 303 | 3264–3271 | Specimen | – | – | – |
| 304 | 3272–3283 | Observation | 2106-3 | Choriogonadotropin [Presence] in Urine | – |
| 305 | 3284–3295 | DiagnosticReport | 2106-3 | Choriogonadotropin [Presence] in Urine | – |
| 306 | 3296–3305 | ServiceRequest | – | – | – |
| 307 | 3309–3316 | Specimen | – | – | – |
| 308 | 3317–3329 | Observation | 11258-1 | Hepatitis B virus DNA [Units/volume] in Serum | – |
| 309 | 3330–3341 | DiagnosticReport | 11258-1 | Hepatitis B virus DNA [Units/volume] in Serum | – |

### Payload per resource

| Resource | Jumlah |
|---|---|
| Observation | 92 |
| ServiceRequest | 74 |
| DiagnosticReport | 73 |
| Specimen | 65 |
| PractitionerRole | 2 |
| Encounter | 1 |
| Patient | 1 |
| Coverage | 1 |
| **Total** | **309** |

## Code

| # | Baris | Resource | Path | Code | Display | CodeSystem |
|---|---|---|---|---|---|---|
| 1 | 6 | Specimen | `Specimen.type.coding` | 119361006 | Plasma | http://snomed.info/sct |
| 2 | 7 | Specimen | `Specimen.type.coding` | 119364003 | Serum | http://snomed.info/sct |
| 3 | 8 | Specimen | `Specimen.type.coding` | 258580003 | Whole blood specimen | http://snomed.info/sct |
| 4 | 9 | Specimen | `Specimen.type.coding` | 119297000 | Blood specimen | http://snomed.info/sct |
| 5 | 10 | Specimen | `Specimen.type.coding` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 6 | 11 | Specimen | `Specimen.type.coding` | 258450006 | Cerebrospinal fluid specimen | http://snomed.info/sct |
| 7 | 12 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 8 | 13 | Specimen | `Specimen.type.coding` | 309508006 | Soft tissue lesion fine needle aspirate specimen | http://snomed.info/sct |
| 9 | 14 | Specimen | `Specimen.type.coding` | 168137004 | Gastric aspirate specimen | http://snomed.info/sct |
| 10 | 15 | Specimen | `Specimen.type.coding` | 119303007 | Microbial isolate specimen | http://snomed.info/sct |
| 11 | 16 | Specimen | `Specimen.type.coding` | ST000001 | Sputum Pagi | http://snomed.info/sct |
| 12 | 17 | Specimen | `Specimen.type.coding` | ST000002 | Sputum Sewaktu | http://snomed.info/sct |
| 13 | 18 | Specimen | `Specimen.type.coding` | 122575003 | Urine specimen | http://snomed.info/sct |
| 14 | 19 | Specimen | `Specimen.type.coding` | 119339001 | Stool specimen | http://snomed.info/sct |
| 15 | 20 | Specimen | `Specimen.type.coding` | 119376003 | Tissue specimen | http://snomed.info/sct |
| 16 | 21 | Specimen | `Specimen.type.coding` | 119297000 | Blood specimen | http://snomed.info/sct |
| 17 | 50 | Encounter | `Encounter.hospitaliz ation.admitSource.co ding` | emd | From accident/emergency department | http://terminology.hl7.org/CodeSystem/admit-source |
| 18 | 51 | Encounter | `Encounter.hospitaliz ation.admitSource.co ding` | outp | From outpatient department | http://terminology.hl7.org/CodeSystem/admit-source |
| 19 | 70 | ServiceRequest | `ServiceRequest.code.coding` | 89371-9 | MTB complex DNA and rpoB RIF resistance mutation panel [Presence] | http://loinc.org |
| 20 | 71 | ServiceRequest | `ServiceRequest.code.coding` | SRC000011 | Pemeriksaaan TCM XDR | http://terminology.kemkes.go.id/CodeSystem/clinical-term |
| 21 | 73 | Observation | `Observation.code.coding[x]` | 89371-9 | MTB complex DNA and rpoB RIF resistance mutation panel [Presence] | http://loinc.org |
| 22 | 74 | Observation | `Observation.valueCodeableConcept.coding` | LA11882-0 | Detected | http://snomed.info/sct |
| 23 | 75 | Observation | `Observation.valueCodeableConcept.coding` | LA11883-8 | Not detected | http://snomed.info/sct |
| 24 | 81 | DiagnosticReport | `DiagnosticReport.code.coding` | 89371-9 | MTB complex DNA and rpoB RIF resistance mutation panel [Presence] | http://loinc.org |
| 25 | 94 | ServiceRequest | `ServiceRequest.code` | 94500-6 | SARS-CoV-2 (COVID-19) RNA [Presence] in Respiratory specimen by NAA with probe detection | http://loinc.org |
| 26 | 104 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 27 | 113 | Observation | `Observation.code.coding` | 94500-6 | SARS-CoV-2 (COVID-19) RNA [Presence] in Respiratory specimen by NAA with probe detection | http://loinc.org |
| 28 | 114 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 29 | 115 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 30 | 125 | DiagnosticReport | `DiagnosticReport.code.coding` | 94500-6 | SARS-CoV-2 (COVID-19) RNA [Presence] in Respiratory specimen by NAA with probe detection | http://loinc.org |
| 31 | 139 | ServiceRequest | `ServiceRequest.code` | 23539-0 | Tuberculosis reaction wheal [Diameter] --3 days post dose mammalian tuberculin intradermal | http://loinc.org |
| 32 | 149 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 33 | 158 | Observation | `Observation.code.coding` | 23539-0 | Tuberculosis reaction wheal [Diameter] --3 days post dose mammalian tuberculin intradermal | http://loinc.org |
| 34 | 159 | Observation | `Observation.valueCodeableConcept.coding` | 268376005 | Mantoux: positive | http://snomed.info/sct |
| 35 | 160 | Observation | `Observation.valueCodeableConcept.coding` | 268375009 | Mantoux: negative | http://snomed.info/sct |
| 36 | 170 | DiagnosticReport | `DiagnosticReport.code.coding` | 23539-0 | Tuberculosis reaction wheal [Diameter] --3 days post dose mammalian tuberculin intradermal | http://loinc.org |
| 37 | 184 | ServiceRequest | `ServiceRequest.code` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 38 | 194 | Specimen | `Specimen.type` | 119334006 | Sputum specimen | http://snomed.info/sct |
| 39 | 203 | Observation | `Observation.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 40 | 204 | Observation | `Observation.valueCodeableConcept.coding` | 260385009 | Negative | http://snomed.info/sct |
| 41 | 205 | Observation | `Observation.valueCodeableConcept.coding` | LA11841-6 | 1+ | http://loinc.org |
| 42 | 206 | Observation | `Observation.valueCodeableConcept.coding` | LA11842-4 | 2+ | http://loinc.org |
| 43 | 207 | Observation | `Observation.valueCodeableConcept.coding` | LA11843-2 | 3+ | http://loinc.org |
| 44 | 217 | DiagnosticReport | `DiagnosticReport.code.coding` | 11545-1 | Microscopic observation [Identifier] in Specimen by Acid fast stain | http://loinc.org |
| 45 | 231 | ServiceRequest | `ServiceRequest.code` | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 46 | 241 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 47 | 250 | Observation | `Observation.code.coding` | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 48 | 263 | DiagnosticReport | `DiagnosticReport.code.coding` | 1558-6 | Fasting glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 49 | 277 | ServiceRequest | `ServiceRequest.code` | 2093-3 | Cholesterol [Mass/volume] in Serum or Plasma | http://loinc.org |
| 50 | 287 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 51 | 296 | Observation | `Observation.code.coding` | 2093-3 | Cholesterol [Mass/volume] in Serum or Plasma | http://loinc.org |
| 52 | 309 | DiagnosticReport | `DiagnosticReport.code.coding` | 2093-3 | Cholesterol [Mass/volume] in Serum or Plasma | http://loinc.org |
| 53 | 323 | ServiceRequest | `ServiceRequest.code` | 3084-1 | Urate [Mass/volume] in Serum or Plasma | http://loinc.org |
| 54 | 333 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 55 | 342 | Observation | `Observation.code.coding` | 3084-1 | Urate [Mass/volume] in Serum or Plasma | http://loinc.org |
| 56 | 355 | DiagnosticReport | `DiagnosticReport.code.coding` | 3084-1 | Urate [Mass/volume] in Serum or Plasma | http://loinc.org |
| 57 | 370 | ServiceRequest | `ServiceRequest.code` | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 58 | 380 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 59 | 389 | Observation | `Observation.code.coding` | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 60 | 402 | DiagnosticReport | `DiagnosticReport.code.coding` | 2345-7 | Glucose [Mass/volume] in Serum or Plasma | http://loinc.org |
| 61 | 416 | ServiceRequest | `ServiceRequest.code` | 41653-7 | Glucose [Mass/volume] in Capillary blood by Glucometer | http://loinc.org |
| 62 | 426 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 63 | 435 | Observation | `Observation.code.coding` | 41653-7 | Glucose [Mass/volume] in Capillary blood by Glucometer | http://loinc.org |
| 64 | 448 | DiagnosticReport | `DiagnosticReport.code.coding` | 41653-7 | Glucose [Mass/volume] in Capillary blood by Glucometer | http://loinc.org |
| 65 | 462 | ServiceRequest | `ServiceRequest.code` | 2571-8 | Triglyceride [Mass/volume] in Serum or Plasma | http://loinc.org |
| 66 | 472 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 67 | 481 | Observation | `Observation.code.coding` | 2571-8 | Triglyceride [Mass/volume] in Serum or Plasma | http://loinc.org |
| 68 | 494 | DiagnosticReport | `DiagnosticReport.code.coding` | 2571-8 | Triglyceride [Mass/volume] in Serum or Plasma | http://loinc.org |
| 69 | 508 | ServiceRequest | `ServiceRequest.code` | 2085-9 | Cholesterol in HDL [Mass/volume] in Serum or Plasma | http://loinc.org |
| 70 | 518 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 71 | 527 | Observation | `Observation.code.coding` | 2085-9 | Cholesterol in HDL [Mass/volume] in Serum or Plasma | http://loinc.org |
| 72 | 540 | DiagnosticReport | `DiagnosticReport.code.coding` | 2085-9 | Cholesterol in HDL [Mass/volume] in Serum or Plasma | http://loinc.org |
| 73 | 554 | ServiceRequest | `ServiceRequest.code` | 2089-1 | Cholesterol in LDL [Mass/volume] in Serum or Plasma | http://loinc.org |
| 74 | 564 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 75 | 573 | Observation | `Observation.code.coding` | 2089-1 | Cholesterol in LDL [Mass/volume] in Serum or Plasma | http://loinc.org |
| 76 | 586 | DiagnosticReport | `DiagnosticReport.code.coding` | 2089-1 | Cholesterol in LDL [Mass/volume] in Serum or Plasma | http://loinc.org |
| 77 | 600 | ServiceRequest | `ServiceRequest.code` | 1751-7 | Albumin [Mass/volume] in Serum or Plasma | http://loinc.org |
| 78 | 610 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 79 | 619 | Observation | `Observation.code.coding` | 1751-7 | Albumin [Mass/volume] in Serum or Plasma | http://loinc.org |
| 80 | 632 | DiagnosticReport | `DiagnosticReport.code.coding` | 1751-7 | Albumin [Mass/volume] in Serum or Plasma | http://loinc.org |
| 81 | 646 | ServiceRequest | `ServiceRequest.code` | 2324-2 | Gamma glutamyl transferase [Enzymatic activity/volume] in Serum or Plasma | http://loinc.org |
| 82 | 656 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 83 | 665 | Observation | `Observation.code.coding` | 2324-2 | Gamma glutamyl transferase [Enzymatic activity/volume] in Serum or Plasma | http://loinc.org |
| 84 | 678 | DiagnosticReport | `DiagnosticReport.code.coding` | 2324-2 | Gamma glutamyl transferase [Enzymatic activity/volume] in Serum or Plasma | http://loinc.org |
| 85 | 692 | ServiceRequest | `ServiceRequest.code` | 4548-4 | Hemoglobin A1c/Hemoglobin.total in Blood | http://loinc.org |
| 86 | 702 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 87 | 711 | Observation | `Observation.code.coding` | 4548-4 | Hemoglobin A1c/Hemoglobin.total in Blood | http://loinc.org |
| 88 | 724 | DiagnosticReport | `DiagnosticReport.code.coding` | 4548-4 | Hemoglobin A1c/Hemoglobin.total in Blood | http://loinc.org |
| 89 | 738 | ServiceRequest | `ServiceRequest.code` | 1920-8 | Aspartate aminotransferase [Enzymatic activity/volume] in Serum or Plasma | http://loinc.org |
| 90 | 748 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 91 | 757 | Observation | `Observation.code.coding` | 1920-8 | Aspartate aminotransferase [Enzymatic activity/volume] in Serum or Plasma | http://loinc.org |
| 92 | 770 | DiagnosticReport | `DiagnosticReport.code.coding` | 1920-8 | Aspartate aminotransferase [Enzymatic activity/volume] in Serum or Plasma | http://loinc.org |
| 93 | 784 | ServiceRequest | `ServiceRequest.code` | 1742-6 | Alanine aminotransferase [Enzymatic activity/volume] in Serum or Plasma | http://loinc.org |
| 94 | 794 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 95 | 803 | Observation | `Observation.code.coding` | 1742-6 | Alanine aminotransferase [Enzymatic activity/volume] in Serum or Plasma | http://loinc.org |
| 96 | 816 | DiagnosticReport | `DiagnosticReport.code.coding` | 1742-6 | Alanine aminotransferase [Enzymatic activity/volume] in Serum or Plasma | http://loinc.org |
| 97 | 830 | ServiceRequest | `ServiceRequest.code` | 2157-6 | Creatine kinase [Enzymatic activity/volume] in Serum or Plasma | http://loinc.org |
| 98 | 840 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 99 | 849 | Observation | `Observation.code.coding` | 2157-6 | Creatine kinase [Enzymatic activity/volume] in Serum or Plasma | http://loinc.org |
| 100 | 862 | DiagnosticReport | `DiagnosticReport.code.coding` | 2157-6 | Creatine kinase [Enzymatic activity/volume] in Serum or Plasma | http://loinc.org |
| 101 | 876 | ServiceRequest | `ServiceRequest.code` | 20977-5 | Urea [Mass/volume] in Blood | http://loinc.org |
| 102 | 886 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 103 | 895 | Observation | `Observation.code.coding` | 20977-5 | Urea [Mass/volume] in Blood | http://loinc.org |
| 104 | 908 | DiagnosticReport | `DiagnosticReport.code.coding` | 20977-5 | Urea [Mass/volume] in Blood | http://loinc.org |
| 105 | 922 | ServiceRequest | `ServiceRequest.code` | 2885-2 | Protein [Mass/volume] in Serum or Plasma | http://loinc.org |
| 106 | 932 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 107 | 941 | Observation | `Observation.code.coding` | 2885-2 | Protein [Mass/volume] in Serum or Plasma | http://loinc.org |
| 108 | 954 | DiagnosticReport | `DiagnosticReport.code.coding` | 2885-2 | Protein [Mass/volume] in Serum or Plasma | http://loinc.org |
| 109 | 968 | ServiceRequest | `ServiceRequest.code` | 1521-4 | Glucose [Mass/volume] in Serum or Plasma --2 hours post meal | http://loinc.org |
| 110 | 978 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 111 | 987 | Observation | `Observation.code.coding` | 1521-4 | Glucose [Mass/volume] in Serum or Plasma --2 hours post meal | http://loinc.org |
| 112 | 1000 | DiagnosticReport | `DiagnosticReport.code.coding` | 1521-4 | Glucose [Mass/volume] in Serum or Plasma --2 hours post meal | http://loinc.org |
| 113 | 1014 | ServiceRequest | `ServiceRequest.code` | 58410-2 | CBC panel - Blood by Automated count | http://loinc.org |
| 114 | 1024 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 115 | 1033 | Observation | `Observation.code.coding[x]` | 6690-2 | Leukocytes [#/volume] in Blood by Automated count | http://loinc.org |
| 116 | 1037 | Observation | `Observation.code.coding[x]` | 789-8 | Erythrocytes [#/volume] in Blood by Automated count | http://loinc.org |
| 117 | 1041 | Observation | `Observation.code.coding[x]` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 118 | 1045 | Observation | `Observation.code.coding[x]` | 4544-3 | Hematocrit [Volume Fraction] of Blood by Automated count | http://loinc.org |
| 119 | 1049 | Observation | `Observation.code.coding[x]` | 787-2 | MCV [Entitic mean volume] in Red Blood Cells by Automated count | http://loinc.org |
| 120 | 1053 | Observation | `Observation.code.coding[x]` | 785-6 | MCH [Entitic mass] by Automated count | http://loinc.org |
| 121 | 1057 | Observation | `Observation.code.coding[x]` | 786-4 | MCHC [Entitic Mass/volume] in Red Blood Cells by Automated count | http://loinc.org |
| 122 | 1070 | DiagnosticReport | `DiagnosticReport.code.coding` | 58410-2 | CBC panel - Blood by Automated count | http://loinc.org |
| 123 | 1084 | ServiceRequest | `ServiceRequest.code` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 124 | 1094 | Specimen | `Specimen.type` | 122555007 | Venous blood specimen | http://snomed.info/sct |
| 125 | 1103 | Observation | `Observation.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 126 | 1104 | Observation | `Observation.code.coding` | ANC.B9.DE175 | Blood hemoglobin test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 127 | 1117 | DiagnosticReport | `DiagnosticReport.code.coding` | 718-7 | Hemoglobin [Mass/volume] in Blood | http://loinc.org |
| 128 | 1131 | ServiceRequest | `ServiceRequest.code` | 26453-1 | Erythrocytes [#/volume] in Blood | http://loinc.org |
| 129 | 1141 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 130 | 1150 | Observation | `Observation.code.coding[x]` | 26453-1 | Erythrocytes [#/volume] in Blood | http://loinc.org |
| 131 | 1163 | DiagnosticReport | `DiagnosticReport.code.coding` | 26453-1 | Erythrocytes [#/volume] in Blood | http://loinc.org |
| 132 | 1177 | ServiceRequest | `ServiceRequest.code` | 26464-8 | Leukocytes [#/volume] in Blood | http://loinc.org |
| 133 | 1187 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 134 | 1196 | Observation | `Observation.code.coding[x]` | 26464-8 | Leukocytes [#/volume] in Blood | http://loinc.org |
| 135 | 1209 | DiagnosticReport | `DiagnosticReport.code.coding` | 26464-8 | Leukocytes [#/volume] in Blood | http://loinc.org |
| 136 | 1223 | ServiceRequest | `ServiceRequest.code` | 26515-7 | Platelets [#/volume] in Blood | http://loinc.org |
| 137 | 1233 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 138 | 1242 | Observation | `Observation.code.coding[x]` | 26515-7 | Platelets [#/volume] in Blood | http://loinc.org |
| 139 | 1255 | DiagnosticReport | `DiagnosticReport.code.coding` | 26515-7 | Platelets [#/volume] in Blood | http://loinc.org |
| 140 | 1269 | ServiceRequest | `ServiceRequest.code` | 20570-8 | Hematocrit [Volume Fraction] of Blood | http://loinc.org |
| 141 | 1279 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 142 | 1288 | Observation | `Observation.code.coding[x]` | 20570-8 | Hematocrit [Volume Fraction] of Blood | http://loinc.org |
| 143 | 1301 | DiagnosticReport | `DiagnosticReport.code.coding` | 20570-8 | Hematocrit [Volume Fraction] of Blood | http://loinc.org |
| 144 | 1315 | ServiceRequest | `ServiceRequest.code` | 11067-6 | Bleeding time | http://loinc.org |
| 145 | 1325 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 146 | 1334 | Observation | `Observation.code.coding[x]` | 11067-6 | Bleeding time | http://loinc.org |
| 147 | 1347 | DiagnosticReport | `DiagnosticReport.code.coding` | 11067-6 | Bleeding time | http://loinc.org |
| 148 | 1361 | ServiceRequest | `ServiceRequest.code` | 30341-2 | Erythrocyte sedimentation rate [Velocity] in Red Blood Cells | http://loinc.org |
| 149 | 1371 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 150 | 1380 | Observation | `Observation.code.coding[x]` | 30341-2 | Erythrocyte sedimentation rate [Velocity] in Red Blood Cells | http://loinc.org |
| 151 | 1393 | DiagnosticReport | `DiagnosticReport.code.coding` | 30341-2 | Erythrocyte sedimentation rate [Velocity] in Red Blood Cells | http://loinc.org |
| 152 | 1407 | ServiceRequest | `ServiceRequest.code` | 17009-2 | IgM [Presence] in Serum | http://loinc.org |
| 153 | 1417 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 154 | 1426 | Observation | `Observation.code.coding[x]` | 17009-2 | IgM [Presence] in Serum | http://loinc.org |
| 155 | 1427 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 156 | 1428 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 157 | 1438 | DiagnosticReport | `DiagnosticReport.code.coding` | 17009-2 | IgM [Presence] in Serum | http://loinc.org |
| 158 | 1452 | ServiceRequest | `ServiceRequest.code` | 3183-1 | Clotting time of Blood by Lee White method | http://loinc.org |
| 159 | 1462 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 160 | 1471 | Observation | `Observation.code.coding[x]` | 3183-1 | Clotting time of Blood by Lee White method | http://loinc.org |
| 161 | 1484 | DiagnosticReport | `DiagnosticReport.code.coding` | 3183-1 | Clotting time of Blood by Lee White method | http://loinc.org |
| 162 | 1498 | ServiceRequest | `ServiceRequest.code` | 17007-6 | IgG [Presence] in Serum | http://loinc.org |
| 163 | 1508 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 164 | 1517 | Observation | `Observation.code.coding[x]` | 17007-6 | IgG [Presence] in Serum | http://loinc.org |
| 165 | 1518 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 166 | 1519 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 167 | 1529 | DiagnosticReport | `DiagnosticReport.code.coding` | 17007-6 | IgG [Presence] in Serum | http://loinc.org |
| 168 | 1543 | ServiceRequest | `ServiceRequest.code` | 30428-7 | MCV [Entitic volume] | http://loinc.org |
| 169 | 1553 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 170 | 1562 | Observation | `Observation.code.coding[x]` | 30428-7 | MCV [Entitic volume] | http://loinc.org |
| 171 | 1575 | DiagnosticReport | `DiagnosticReport.code.coding` | 30428-7 | MCV [Entitic volume] | http://loinc.org |
| 172 | 1589 | ServiceRequest | `ServiceRequest.code` | 28539-5 | MCH [Entitic mass] | http://loinc.org |
| 173 | 1599 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 174 | 1608 | Observation | `Observation.code.coding[x]` | 28539-5 | MCH [Entitic mass] | http://loinc.org |
| 175 | 1621 | DiagnosticReport | `DiagnosticReport.code.coding` | 28539-5 | MCH [Entitic mass] | http://loinc.org |
| 176 | 1635 | ServiceRequest | `ServiceRequest.code` | 28540-3 | MCHC [Mass/volume] | http://loinc.org |
| 177 | 1645 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 178 | 1654 | Observation | `Observation.code.coding[x]` | 28540-3 | MCHC [Mass/volume] | http://loinc.org |
| 179 | 1667 | DiagnosticReport | `DiagnosticReport.code.coding` | 28540-3 | MCHC [Mass/volume] | http://loinc.org |
| 180 | 1681 | ServiceRequest | `ServiceRequest.code` | 26511-6 | Neutrophils/100 leukocytes in Blood | http://loinc.org |
| 181 | 1691 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 182 | 1700 | Observation | `Observation.code.coding[x]` | 26511-6 | Neutrophils/100 leukocytes in Blood | http://loinc.org |
| 183 | 1713 | DiagnosticReport | `DiagnosticReport.code.coding` | 26511-6 | Neutrophils/100 leukocytes in Blood | http://loinc.org |
| 184 | 1723 | ServiceRequest | `ServiceRequest.code.coding` | 26464-8 | Leukocytes [#/volume] in Blood | http://loinc.org |
| 185 | 1724 | ServiceRequest | `ServiceRequest.code.coding` | 804-5 | Leukocytes [#/volume] in Blood by Manual count | http://loinc.org |
| 186 | 1725 | ServiceRequest | `ServiceRequest.code.coding` | 6690-2 | Leukocytes [#/volume] in Blood by Automated count | http://loinc.org |
| 187 | 1727 | Observation | `Observation.code.coding[x]` | 26464-8 | Leukocytes [#/volume] in Blood | http://loinc.org |
| 188 | 1731 | Observation | `Observation.code.coding[x]` | 804-5 | Leukocytes [#/volume] in Blood by Manual count | http://loinc.org |
| 189 | 1735 | Observation | `Observation.code.coding[x]` | 6690-2 | Leukocytes [#/volume] in Blood by Automated count | http://loinc.org |
| 190 | 1738 | Observation | `Observation.code.coding[x]` | 6690-2 | Leukocytes [#/volume] in Blood by Automated count | http://loinc.org |
| 191 | 1740 | DiagnosticReport | `DiagnosticReport.code.coding` | 26464-8 | Leukocytes [#/volume] in Blood | http://loinc.org |
| 192 | 1741 | DiagnosticReport | `DiagnosticReport.code.coding` | 804-5 | Leukocytes [#/volume] in Blood by Manual count | http://loinc.org |
| 193 | 1742 | DiagnosticReport | `DiagnosticReport.code.coding` | 6690-2 | Leukocytes [#/volume] in Blood by Automated count | http://loinc.org |
| 194 | 1743 | ServiceRequest | `ServiceRequest.code.coding` | 26511-6 | Neutrophils/100 leukocytes in Blood | http://loinc.org |
| 195 | 1744 | ServiceRequest | `ServiceRequest.code.coding` | 23761-0 | Neutrophils/100 leukocytes in Blood by Manual count | http://loinc.org |
| 196 | 1745 | ServiceRequest | `ServiceRequest.code.coding` | 770-8 | Neutrophils/100 leukocytes in Blood by Automated count | http://loinc.org |
| 197 | 1746 | ServiceRequest | `ServiceRequest.code.coding` | 26505-8 | Segmented neutrophils/100 leukocytes in Blood | http://loinc.org |
| 198 | 1747 | ServiceRequest | `ServiceRequest.code.coding` | 769-0 | Segmented neutrophils/100 leukocytes in Blood by Manual count | http://loinc.org |
| 199 | 1748 | ServiceRequest | `ServiceRequest.code.coding` | 32200-8 | Segmented neutrophils/100 leukocytes in Blood by Automated count | http://loinc.org |
| 200 | 1749 | ServiceRequest | `ServiceRequest.code.coding` | 26508-2 | Band form neutrophils/100 leukocytes in Blood | http://loinc.org |
| 201 | 1750 | ServiceRequest | `ServiceRequest.code.coding` | 764-1 | Band form neutrophils/100 leukocytes in Blood by Manual count | http://loinc.org |
| 202 | 1751 | ServiceRequest | `ServiceRequest.code.coding` | 35332-6 | Band form neutrophils/100 leukocytes in Blood by Automated count | http://loinc.org |
| 203 | 1753 | Observation | `Observation.code.coding[x]` | 26511-6 | Neutrophils/100 leukocytes in Blood | http://loinc.org |
| 204 | 1757 | Observation | `Observation.code.coding[x]` | 23761-0 | Neutrophils/100 leukocytes in Blood by Manual count | http://loinc.org |
| 205 | 1761 | Observation | `Observation.code.coding[x]` | 770-8 | Neutrophils/100 leukocytes in Blood by Automated count | http://loinc.org |
| 206 | 1765 | Observation | `Observation.code.coding[x]` | 26505-8 | Segmented neutrophils/100 leukocytes in Blood | http://loinc.org |
| 207 | 1769 | Observation | `Observation.code.coding[x]` | 769-0 | Segmented neutrophils/100 leukocytes in Blood by Manual count | http://loinc.org |
| 208 | 1773 | Observation | `Observation.code.coding[x]` | 32200-8 | Segmented neutrophils/100 leukocytes in Blood by Automated count | http://loinc.org |
| 209 | 1777 | Observation | `Observation.code.coding[x]` | 26508-2 | Band form neutrophils/100 leukocytes in Blood | http://loinc.org |
| 210 | 1781 | Observation | `Observation.code.coding[x]` | 764-1 | Band form neutrophils/100 leukocytes in Blood by Manual count | http://loinc.org |
| 211 | 1785 | Observation | `Observation.code.coding[x]` | 35332-6 | Band form neutrophils/100 leukocytes in Blood by Automated count | http://loinc.org |
| 212 | 1790 | DiagnosticReport | `DiagnosticReport.code.coding` | 26511-6 | Neutrophils/100 leukocytes in Blood | http://loinc.org |
| 213 | 1791 | DiagnosticReport | `DiagnosticReport.code.coding` | 23761-0 | Neutrophils/100 leukocytes in Blood by Manual count | http://loinc.org |
| 214 | 1792 | DiagnosticReport | `DiagnosticReport.code.coding` | 770-8 | Neutrophils/100 leukocytes in Blood by Automated count | http://loinc.org |
| 215 | 1793 | DiagnosticReport | `DiagnosticReport.code.coding` | 26505-8 | Segmented neutrophils/100 leukocytes in Blood | http://loinc.org |
| 216 | 1794 | DiagnosticReport | `DiagnosticReport.code.coding` | 769-0 | Segmented neutrophils/100 leukocytes in Blood by Manual count | http://loinc.org |
| 217 | 1795 | DiagnosticReport | `DiagnosticReport.code.coding` | 32200-8 | Segmented neutrophils/100 leukocytes in Blood by Automated count | http://loinc.org |
| 218 | 1796 | DiagnosticReport | `DiagnosticReport.code.coding` | 26508-2 | Band form neutrophils/100 leukocytes in Blood | http://loinc.org |
| 219 | 1797 | DiagnosticReport | `DiagnosticReport.code.coding` | 764-1 | Band form neutrophils/100 leukocytes in Blood by Manual count | http://loinc.org |
| 220 | 1798 | DiagnosticReport | `DiagnosticReport.code.coding` | 35332-6 | Band form neutrophils/100 leukocytes in Blood by Automated count | http://loinc.org |
| 221 | 1803 | ServiceRequest | `ServiceRequest.code` | 26478-8 | Lymphocytes/100 leukocytes in Blood | http://loinc.org |
| 222 | 1813 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 223 | 1822 | Observation | `Observation.code.coding[x]` | 26478-8 | Lymphocytes/100 leukocytes in Blood | http://loinc.org |
| 224 | 1835 | DiagnosticReport | `DiagnosticReport.code.coding` | 26478-8 | Lymphocytes/100 leukocytes in Blood | http://loinc.org |
| 225 | 1849 | ServiceRequest | `ServiceRequest.code` | 882-1 | ABO and Rh group [Type] in Blood | http://loinc.org |
| 226 | 1859 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 227 | 1868 | Observation | `Observation.code.coding` | 882-1 | ABO and Rh group [Type] in Blood | http://loinc.org |
| 228 | 1869 | Observation | `Observation.valueCodeableConcept.coding` | LA21321-7 | O Pos | http://loinc.org |
| 229 | 1870 | Observation | `Observation.valueCodeableConcept.coding` | LA21322-5 | O Neg | http://loinc.org |
| 230 | 1871 | Observation | `Observation.valueCodeableConcept.coding` | LA21327-4 | B Pos | http://loinc.org |
| 231 | 1872 | Observation | `Observation.valueCodeableConcept.coding` | LA21328-2 | B Neg | http://loinc.org |
| 232 | 1873 | Observation | `Observation.valueCodeableConcept.coding` | LA21323-3 | AB Pos | http://loinc.org |
| 233 | 1874 | Observation | `Observation.valueCodeableConcept.coding` | LA21324-1 | AB Neg | http://loinc.org |
| 234 | 1875 | Observation | `Observation.valueCodeableConcept.coding` | LA21325-8 | A Pos | http://loinc.org |
| 235 | 1876 | Observation | `Observation.valueCodeableConcept.coding` | LA21326-6 | A Neg | http://loinc.org |
| 236 | 1886 | DiagnosticReport | `DiagnosticReport.code.coding` | 882-1 | ABO and Rh group [Type] in Blood | http://loinc.org |
| 237 | 1900 | ServiceRequest | `ServiceRequest.code` | 883-9 | ABO group [Type] in Blood | http://loinc.org |
| 238 | 1911 | Observation | `Observation.code.coding` | 883-9 | ABO group [Type] in Blood | http://loinc.org |
| 239 | 1912 | Observation | `Observation.valueCodeableConcept.coding` | LA19710-5 | Group A | http://loinc.org |
| 240 | 1913 | Observation | `Observation.valueCodeableConcept.coding` | LA19709-7 | Group B | http://loinc.org |
| 241 | 1914 | Observation | `Observation.valueCodeableConcept.coding` | LA19708-9 | Group O | http://loinc.org |
| 242 | 1915 | Observation | `Observation.valueCodeableConcept.coding` | LA28449-9 | Group AB | http://loinc.org |
| 243 | 1925 | DiagnosticReport | `DiagnosticReport.code.coding` | 883-9 | ABO group [Type] in Blood | http://loinc.org |
| 244 | 1939 | ServiceRequest | `ServiceRequest.code` | 17566-1 | Salmonella typhi O Ab [Presence] in Serum | http://loinc.org |
| 245 | 1949 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 246 | 1958 | Observation | `Observation.code.coding` | 17566-1 | Salmonella typhi O Ab [Presence] in Serum | http://loinc.org |
| 247 | 1959 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 248 | 1960 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 249 | 1970 | DiagnosticReport | `DiagnosticReport.code.coding` | 17566-1 | Salmonella typhi O Ab [Presence] in Serum | http://loinc.org |
| 250 | 1984 | ServiceRequest | `ServiceRequest.code` | 22529-2 | Salmonella typhi H Ab [Presence] in Serum | http://loinc.org |
| 251 | 1994 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 252 | 2003 | Observation | `Observation.code.coding` | 22529-2 | Salmonella typhi H Ab [Presence] in Serum | http://loinc.org |
| 253 | 2004 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 254 | 2005 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 255 | 2015 | DiagnosticReport | `DiagnosticReport.code.coding` | 22529-2 | Salmonella typhi H Ab [Presence] in Serum | http://loinc.org |
| 256 | 2029 | ServiceRequest | `ServiceRequest.code` | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 257 | 2039 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 258 | 2048 | Observation | `Observation.code.coding` | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 259 | 2049 | Observation | `Observation.code.coding` | ANC.B9.DE32 | HIV test | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 260 | 2050 | Observation | `Observation.valueCodeableConcept.coding` | LA15255-5 | Reactive | http://loinc.org |
| 261 | 2051 | Observation | `Observation.valueCodeableConcept.coding` | LA15256-3 | Nonreactive | http://loinc.org |
| 262 | 2061 | DiagnosticReport | `DiagnosticReport.code` | 68961-2 | HIV 1 Ab [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 263 | 2072 | ServiceRequest | `ServiceRequest.code.coding` | 743-5 | Monocytes [#/volume] in Blood by Manual count | http://loinc.org |
| 264 | 2073 | ServiceRequest | `ServiceRequest.code.coding` | 705-4 | Basophils [#/volume] in Blood by Manual count | http://loinc.org |
| 265 | 2074 | ServiceRequest | `ServiceRequest.code.coding` | 712-0 | Eosinophils [#/volume] in Blood by Manual count | http://loinc.org |
| 266 | 2075 | ServiceRequest | `ServiceRequest.code.coding` | 26484-6 | Monocytes [#/volume] in Blood | http://loinc.org |
| 267 | 2076 | ServiceRequest | `ServiceRequest.code.coding` | 26449-9 | Eosinophils [#/volume] in Blood | http://loinc.org |
| 268 | 2077 | ServiceRequest | `ServiceRequest.code.coding` | 26444-0 | Basophils [#/volume] in Blood | http://loinc.org |
| 269 | 2079 | Observation | `Observation.code.coding[x]` | 743-5 | Monocytes [#/volume] in Blood by Manual count | http://loinc.org |
| 270 | 2080 | Observation | `Observation.code.coding[x]` | 26484-6 | Monocytes [#/volume] in Blood | http://loinc.org |
| 271 | 2081 | Observation | `Observation.code.coding[x]` | 705-4 | Basophils [#/volume] in Blood by Manual count | http://loinc.org |
| 272 | 2082 | Observation | `Observation.code.coding[x]` | 26444-0 | Basophils [#/volume] in Blood | http://loinc.org |
| 273 | 2083 | Observation | `Observation.code.coding[x]` | 712-0 | Eosinophils [#/volume] in Blood by Manual count | http://loinc.org |
| 274 | 2084 | Observation | `Observation.code.coding[x]` | 26449-9 | Eosinophils [#/volume] in Blood | http://loinc.org |
| 275 | 2089 | DiagnosticReport | `DiagnosticReport.code.coding` | 743-5 | Monocytes [#/volume] in Blood by Manual count | http://loinc.org |
| 276 | 2090 | DiagnosticReport | `DiagnosticReport.code.coding` | 26484-6 | Monocytes [#/volume] in Blood | http://loinc.org |
| 277 | 2091 | DiagnosticReport | `DiagnosticReport.code.coding` | 705-4 | Basophils [#/volume] in Blood by Manual count | http://loinc.org |
| 278 | 2092 | DiagnosticReport | `DiagnosticReport.code.coding` | 26444-0 | Basophils [#/volume] in Blood | http://loinc.org |
| 279 | 2093 | DiagnosticReport | `DiagnosticReport.code.coding` | 712-0 | Eosinophils [#/volume] in Blood by Manual count | http://loinc.org |
| 280 | 2094 | DiagnosticReport | `DiagnosticReport.code.coding` | 26449-9 | Eosinophils [#/volume] in Blood | http://loinc.org |
| 281 | 2099 | ServiceRequest | `ServiceRequest.code` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 282 | 2109 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 283 | 2118 | Observation | `Observation.code.coding` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 284 | 2119 | Observation | `Observation.code.coding` | ANC.B9.DE60 | Hepatitis B test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 285 | 2120 | Observation | `Observation.valueCodeableConcept.coding` | LA15255-5 | Reactive | http://loinc.org |
| 286 | 2121 | Observation | `Observation.valueCodeableConcept.coding` | LA15256-3 | Nonreactive | http://loinc.org |
| 287 | 2131 | DiagnosticReport | `DiagnosticReport.code` | 75410-1 | Hepatitis B virus surface Ag [Presence] in Serum, Plasma or Blood by Rapid immunoassay | http://loinc.org |
| 288 | 2145 | ServiceRequest | `ServiceRequest.code` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 289 | 2156 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 290 | 2165 | Observation | `Observation.code.coding` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 291 | 2166 | Observation | `Observation.code.coding` | ANC.B9.DE96 | Syphilis test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 292 | 2167 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 293 | 2168 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 294 | 2179 | DiagnosticReport | `DiagnosticReport.code` | 22464-2 | Reagin Ab [Presence] in Specimen | http://loinc.org |
| 295 | 2193 | ServiceRequest | `ServiceRequest.code` | 87546-8 | Dengue virus IgG and IgM panel - Serum Qualitative | http://loinc.org |
| 296 | 2203 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 297 | 2212 | Observation | `Observation.code.coding[x]` | 29676-4 | Dengue virus IgG Ab [Presence] in Serum | http://loinc.org |
| 298 | 2213 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 299 | 2214 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 300 | 2224 | Observation | `Observation.code.coding[x]` | 25338-5 | Dengue virus IgM Ab [Presence] in Serum | http://loinc.org |
| 301 | 2225 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 302 | 2226 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 303 | 2236 | DiagnosticReport | `DiagnosticReport.code.coding` | 87546-8 | Dengue virus IgG and IgM panel - Serum Qualitative | http://loinc.org |
| 304 | 2250 | ServiceRequest | `ServiceRequest.code` | 29676-4 | Dengue virus IgG Ab [Presence] in Serum | http://loinc.org |
| 305 | 2261 | Observation | `Observation.code.coding[x]` | 29676-4 | Dengue virus IgG Ab [Presence] in Serum | http://loinc.org |
| 306 | 2262 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 307 | 2263 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 308 | 2273 | DiagnosticReport | `DiagnosticReport.code.coding` | 29676-4 | Dengue virus IgG Ab [Presence] in Serum | http://loinc.org |
| 309 | 2287 | ServiceRequest | `ServiceRequest.code` | 25338-5 | Dengue virus IgM Ab [Presence] in Serum | http://loinc.org |
| 310 | 2298 | Observation | `Observation.code.coding[x]` | 25338-5 | Dengue virus IgM Ab [Presence] in Serum | http://loinc.org |
| 311 | 2299 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 312 | 2300 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 313 | 2310 | DiagnosticReport | `DiagnosticReport.code.coding` | 25338-5 | Dengue virus IgM Ab [Presence] in Serum | http://loinc.org |
| 314 | 2324 | ServiceRequest | `ServiceRequest.code` | 91064-6 | Dengue virus NS1 Ag [Presence] in Serum or Plasma by Immunoassay | http://loinc.org |
| 315 | 2334 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 316 | 2343 | Observation | `Observation.code.coding[x]` | 91064-6 | Dengue virus NS1 Ag [Presence] in Serum or Plasma by Immunoassay | http://loinc.org |
| 317 | 2345 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 318 | 2346 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 319 | 2356 | DiagnosticReport | `DiagnosticReport.code.coding` | 91064-6 | Dengue virus NS1 Ag [Presence] in Serum or Plasma by Immunoassay | http://loinc.org |
| 320 | 2370 | ServiceRequest | `ServiceRequest.code` | 47085-6 | Plasmodium sp DNA [Presence] in Blood by NAA with probe detection | http://loinc.org |
| 321 | 2380 | Specimen | `Specimen.type` | 119297000 | Blood specimen | http://snomed.info/sct |
| 322 | 2389 | Observation | `Observation.code.coding[x]` | 47085-6 | Plasmodium sp DNA [Presence] in Blood by NAA with probe detection | http://loinc.org |
| 323 | 2391 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 324 | 2392 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 325 | 2402 | DiagnosticReport | `DiagnosticReport.code.coding` | 47085-6 | Plasmodium sp DNA [Presence] in Blood by NAA with probe detection | http://loinc.org |
| 326 | 2416 | ServiceRequest | `ServiceRequest.code` | 34534-8 | 12 lead EKG panel | http://loinc.org |
| 327 | 2423 | PractitionerRole | `PractitionerRole.code.coding` | 66862007 | Radiologist | http://snomed.info/sct |
| 328 | 2427 | Observation | `Observation.code.coding[x]` | 34534-8 | 12 lead EKG panel | http://loinc.org |
| 329 | 2437 | DiagnosticReport | `DiagnosticReport.code.coding` | 34534-8 | 12 lead EKG panel | http://loinc.org |
| 330 | 2450 | ServiceRequest | `ServiceRequest.code` | 11525-3 | US for pregnancy | http://loinc.org |
| 331 | 2457 | PractitionerRole | `PractitionerRole.code.coding` | 66862007 | Radiologist | http://snomed.info/sct |
| 332 | 2461 | Observation | `Observation.code.coding[x]` | 11525-3 | US for pregnancy | http://loinc.org |
| 333 | 2471 | DiagnosticReport | `DiagnosticReport.code.coding` | 11525-3 | US for pregnancy | http://loinc.org |
| 334 | 2484 | ServiceRequest | `ServiceRequest.code` | 5778-6 | Color of Urine | http://loinc.org |
| 335 | 2491 | Specimen | `Specimen.type` | 122575003 | Urine specimen | http://snomed.info/sct |
| 336 | 2500 | Observation | `Observation.code.coding[x]` | 5778-6 | Color of Urine | http://loinc.org |
| 337 | 2511 | DiagnosticReport | `DiagnosticReport.code.coding` | 5778-6 | Color of Urine | http://loinc.org |
| 338 | 2525 | ServiceRequest | `ServiceRequest.code` | 32167-9 | Clarity of Urine | http://loinc.org |
| 339 | 2535 | Specimen | `Specimen.type` | 122575003 | Urine specimen | http://snomed.info/sct |
| 340 | 2544 | Observation | `Observation.code.coding[x]` | 32167-9 | Clarity of Urine | http://loinc.org |
| 341 | 2555 | DiagnosticReport | `DiagnosticReport.code.coding` | 32167-9 | Clarity of Urine | http://loinc.org |
| 342 | 2569 | ServiceRequest | `ServiceRequest.code` | 2756-5 | pH of Urine | http://loinc.org |
| 343 | 2579 | Specimen | `Specimen.type` | 122575003 | Urine specimen | http://snomed.info/sct |
| 344 | 2588 | Observation | `Observation.code.coding[x]` | 2756-5 | pH of Urine | http://loinc.org |
| 345 | 2601 | DiagnosticReport | `DiagnosticReport.code.coding` | 2756-5 | pH of Urine | http://loinc.org |
| 346 | 2615 | ServiceRequest | `ServiceRequest.code` | 2965-2 | Specific gravity of Urine | http://loinc.org |
| 347 | 2625 | Specimen | `Specimen.type` | 122575003 | Urine specimen | http://snomed.info/sct |
| 348 | 2634 | Observation | `Observation.code.coding[x]` | 2965-2 | Specific gravity of Urine | http://loinc.org |
| 349 | 2647 | DiagnosticReport | `DiagnosticReport.code.coding` | 2965-2 | Specific gravity of Urine | http://loinc.org |
| 350 | 2661 | ServiceRequest | `ServiceRequest.code` | 2887-8 | Protein [Presence] in Urine | http://loinc.org |
| 351 | 2671 | Specimen | `Specimen.type` | 122575003 | Urine specimen | http://snomed.info/sct |
| 352 | 2680 | Observation | `Observation.code.coding` | 2887-8 | Protein [Presence] in Urine | http://loinc.org |
| 353 | 2681 | Observation | `Observation.code.coding` | ANC.B9.DE114 | Urine test conducted | http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes |
| 354 | 2682 | Observation | `Observation.valueCodeableConcept.coding` | LA11843-2 | 3+ | http://loinc.org |
| 355 | 2683 | Observation | `Observation.valueCodeableConcept.coding` | LA11842-4 | 2+ | http://loinc.org |
| 356 | 2684 | Observation | `Observation.valueCodeableConcept.coding` | LA11841-6 | 1+ | http://loinc.org |
| 357 | 2685 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 358 | 2697 | DiagnosticReport | `DiagnosticReport.code.coding` | 2887-8 | Protein [Presence] in Urine | http://loinc.org |
| 359 | 2711 | ServiceRequest | `ServiceRequest.code` | 2349-9 | Glucose [Presence] in Urine | http://loinc.org |
| 360 | 2721 | Specimen | `Specimen.type` | 122575003 | Urine specimen | http://snomed.info/sct |
| 361 | 2730 | Observation | `Observation.code.coding[x]` | 2349-9 | Glucose [Presence] in Urine | http://loinc.org |
| 362 | 2731 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 363 | 2732 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 364 | 2742 | DiagnosticReport | `DiagnosticReport.code.coding` | 2349-9 | Glucose [Presence] in Urine | http://loinc.org |
| 365 | 2756 | ServiceRequest | `ServiceRequest.code` | 33903-6 | Ketones [Presence] in Urine | http://loinc.org |
| 366 | 2766 | Specimen | `Specimen.type` | 122575003 | Urine specimen | http://snomed.info/sct |
| 367 | 2775 | Observation | `Observation.code.coding[x]` | 33903-6 | Ketones [Presence] in Urine | http://loinc.org |
| 368 | 2776 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 369 | 2777 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 370 | 2787 | DiagnosticReport | `DiagnosticReport.code.coding` | 33903-6 | Ketones [Presence] in Urine | http://loinc.org |
| 371 | 2801 | ServiceRequest | `ServiceRequest.code` | 1977-8 | Bilirubin.total [Presence] in Urine | http://loinc.org |
| 372 | 2811 | Specimen | `Specimen.type` | 122575003 | Urine specimen | http://snomed.info/sct |
| 373 | 2820 | Observation | `Observation.code.coding[x]` | 1977-8 | Bilirubin.total [Presence] in Urine | http://loinc.org |
| 374 | 2821 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 375 | 2822 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 376 | 2832 | DiagnosticReport | `DiagnosticReport.code.coding` | 1977-8 | Bilirubin.total [Presence] in Urine | http://loinc.org |
| 377 | 2846 | ServiceRequest | `ServiceRequest.code` | 34927-4 | Urobilinogen [Moles/volume] in Urine | http://loinc.org |
| 378 | 2856 | Specimen | `Specimen.type` | 122575003 | Urine specimen | http://snomed.info/sct |
| 379 | 2865 | Observation | `Observation.code.coding[x]` | 34927-4 | Urobilinogen [Moles/volume] in Urine | http://loinc.org |
| 380 | 2878 | DiagnosticReport | `DiagnosticReport.code.coding` | 34927-4 | Urobilinogen [Moles/volume] in Urine | http://loinc.org |
| 381 | 2892 | ServiceRequest | `ServiceRequest.code` | 105906-2 | Blood [Presence] in Urine | http://loinc.org |
| 382 | 2902 | Specimen | `Specimen.type` | 122575003 | Urine specimen | http://snomed.info/sct |
| 383 | 2911 | Observation | `Observation.code.coding` | 105906-2 | Blood [Presence] in Urine | http://loinc.org |
| 384 | 2912 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 385 | 2913 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 386 | 2923 | DiagnosticReport | `DiagnosticReport.code.coding` | 105906-2 | Blood [Presence] in Urine | http://loinc.org |
| 387 | 2937 | ServiceRequest | `ServiceRequest.code` | 32710-6 | Nitrite [Presence] in Urine | http://loinc.org |
| 388 | 2947 | Specimen | `Specimen.type` | 122575003 | Urine specimen | http://snomed.info/sct |
| 389 | 2956 | Observation | `Observation.code.coding` | 32710-6 | Nitrite [Presence] in Urine | http://loinc.org |
| 390 | 2957 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 391 | 2958 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 392 | 2968 | DiagnosticReport | `DiagnosticReport.code.coding` | 32710-6 | Nitrite [Presence] in Urine | http://loinc.org |
| 393 | 2982 | ServiceRequest | `ServiceRequest.code` | 105087-1 | Epithelial cells.squamous [Presence] in Urine | http://loinc.org |
| 394 | 2992 | Specimen | `Specimen.type` | 122575003 | Urine specimen | http://snomed.info/sct |
| 395 | 3001 | Observation | `Observation.code.coding` | 105087-1 | Epithelial cells.squamous [Presence] in Urine | http://loinc.org |
| 396 | 3002 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 397 | 3003 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 398 | 3013 | DiagnosticReport | `DiagnosticReport.code.coding` | 105087-1 | Epithelial cells.squamous [Presence] in Urine | http://loinc.org |
| 399 | 3027 | ServiceRequest | `ServiceRequest.code` | 105089-7 | Epithelial cells.non-squamous [Presence] in Urine | http://loinc.org |
| 400 | 3037 | Specimen | `Specimen.type` | 122575003 | Urine specimen | http://snomed.info/sct |
| 401 | 3046 | Observation | `Observation.code.coding` | 105089-7 | Epithelial cells.non-squamous [Presence] in Urine | http://loinc.org |
| 402 | 3047 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 403 | 3048 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 404 | 3058 | DiagnosticReport | `DiagnosticReport.code.coding` | 105089-7 | Epithelial cells.non-squamous [Presence] in Urine | http://loinc.org |
| 405 | 3072 | ServiceRequest | `ServiceRequest.code` | 85093-3 | Crystal casts [Presence] in Urine sediment by Light microscopy | http://loinc.org |
| 406 | 3082 | Specimen | `Specimen.type` | 122575003 | Urine specimen | http://snomed.info/sct |
| 407 | 3091 | Observation | `Observation.code.coding` | 85093-3 | Crystal casts [Presence] in Urine sediment by Light microscopy | http://loinc.org |
| 408 | 3092 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 409 | 3093 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 410 | 3103 | DiagnosticReport | `DiagnosticReport.code.coding` | 85093-3 | Crystal casts [Presence] in Urine sediment by Light microscopy | http://loinc.org |
| 411 | 3117 | ServiceRequest | `ServiceRequest.code` | 105107-7 | Erythrocytes [#/area] in Urine sediment | http://loinc.org |
| 412 | 3136 | Observation | `Observation.code.coding` | 105107-7 | Erythrocytes [#/area] in Urine sediment | http://loinc.org |
| 413 | 3149 | DiagnosticReport | `DiagnosticReport.code.coding` | 105107-7 | Erythrocytes [#/area] in Urine sediment | http://loinc.org |
| 414 | 3163 | ServiceRequest | `ServiceRequest.code` | 105104-4 | Leukocytes [#/area] in Urine sediment | http://loinc.org |
| 415 | 3182 | Observation | `Observation.code.coding` | 105104-4 | Leukocytes [#/area] in Urine sediment | http://loinc.org |
| 416 | 3195 | DiagnosticReport | `DiagnosticReport.code.coding` | 105104-4 | Leukocytes [#/area] in Urine sediment | http://loinc.org |
| 417 | 3209 | ServiceRequest | `ServiceRequest.code` | 105908-8 | Bacteria [#/area] in Urine sediment | http://loinc.org |
| 418 | 3228 | Observation | `Observation.code.coding` | 105908-8 | Bacteria [#/area] in Urine sediment | http://loinc.org |
| 419 | 3241 | DiagnosticReport | `DiagnosticReport.code.coding` | 105908-8 | Bacteria [#/area] in Urine sediment | http://loinc.org |
| 420 | 3255 | ServiceRequest | `ServiceRequest.code` | 2106-3 | Choriogonadotropin [Presence] in Urine | http://loinc.org |
| 421 | 3265 | Specimen | `Specimen.type` | 122575003 | Urine specimen | http://snomed.info/sct |
| 422 | 3274 | Observation | `Observation.code.coding` | 2106-3 | Choriogonadotropin [Presence] in Urine | http://loinc.org |
| 423 | 3275 | Observation | `Observation.valueCodeableConcept.coding` | LA6576-8 | Positive | http://loinc.org |
| 424 | 3276 | Observation | `Observation.valueCodeableConcept.coding` | LA6577-6 | Negative | http://loinc.org |
| 425 | 3286 | DiagnosticReport | `DiagnosticReport.code.coding` | 2106-3 | Choriogonadotropin [Presence] in Urine | http://loinc.org |
| 426 | 3300 | ServiceRequest | `ServiceRequest.code` | 11258-1 | Hepatitis B virus DNA [Units/volume] in Serum | http://loinc.org |
| 427 | 3310 | Specimen | `Specimen.type` | 119364003 | Serum | http://snomed.info/sct |
| 428 | 3319 | Observation | `Observation.code.coding` | 11258-1 | Hepatitis B virus DNA [Units/volume] in Serum | http://loinc.org |
| 429 | 3332 | DiagnosticReport | `DiagnosticReport.code.coding` | 11258-1 | Hepatitis B virus DNA [Units/volume] in Serum | http://loinc.org |

### Code per CodeSystem

| CodeSystem | Jumlah |
|---|---|
| http://loinc.org | 337 |
| http://snomed.info/sct | 84 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 5 |
| http://terminology.hl7.org/CodeSystem/admit-source | 2 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 1 |
| **Total** | **429** |

## Variabel di luar payload

Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.

| Baris | Variabel BQ | Variabel dictionary | Resource | Path |
|---|---|---|---|---|
| 62 | – | Pemeriksaan | ServiceRequest | `ServiceRequest.category.coding` |
| 66 | – | Hasil | Observation | `Observation.value[X]` |
