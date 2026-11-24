# Output Hitungan Payload & Code — Form Kobo & PHDT

Terakhir diperbarui: 2026-11-24
Aturan hitung: lihat [`aturan.md`](aturan.md) · Temuan & catatan pipeline: [`revisi.md`](revisi.md)
Form yang sudah dihitung (detail per form, bisa ditelusuri per baris):
- **Maternal Outcome** → [`output/maternal-outcome.md`](output/maternal-outcome.md) (sumber: [`mapping/kobo-data-dictionary-maternal-outcome.csv`](mapping/kobo-data-dictionary-maternal-outcome.csv))
- **Raffle** → [`output/raffle.md`](output/raffle.md) (sumber: [`mapping/kobo-data-dictionary-raffle.csv`](mapping/kobo-data-dictionary-raffle.csv))
- **SiGizi ANC** → [`output/sigizi-anc.md`](output/sigizi-anc.md) (sumber: [`mapping/phdt-data-dictionary-sigizi-anc.csv`](mapping/phdt-data-dictionary-sigizi-anc.csv), PHDT Data Dictionary; struktur file mentah: [`raw/sigizi-anc-kolom.md`](raw/sigizi-anc-kolom.md))
- **SITB TB 06** → [`output/sitb-tb06.md`](output/sitb-tb06.md) (sumber: [`mapping/phdt-data-dictionary-sitb-tb06.csv`](mapping/phdt-data-dictionary-sitb-tb06.csv); file mentah: [`raw/sitb-tb06-kolom.md`](raw/sitb-tb06-kolom.md))
- **SITB TB 03 SO** → [`output/sitb-tb03-so.md`](output/sitb-tb03-so.md) (sumber: [`mapping/phdt-data-dictionary-sitb-tb03-so.csv`](mapping/phdt-data-dictionary-sitb-tb03-so.csv); file mentah: [`raw/sitb-tb03-so-kolom.md`](raw/sitb-tb03-so-kolom.md))
- **SITB TB 03 RO** → [`output/sitb-tb03-ro.md`](output/sitb-tb03-ro.md) (sumber: [`mapping/phdt-data-dictionary-sitb-tb03-ro.csv`](mapping/phdt-data-dictionary-sitb-tb03-ro.csv); file mentah: [`raw/sitb-tb03-ro-kolom.md`](raw/sitb-tb03-ro-kolom.md))
- **SITB TB 04** (Fasyankes & Rujukan) → [`output/sitb-tb04.md`](output/sitb-tb04.md) (sumber: [`mapping/phdt-data-dictionary-sitb-tb04.csv`](mapping/phdt-data-dictionary-sitb-tb04.csv); file mentah: [`raw/sitb-tb04-kolom.md`](raw/sitb-tb04-kolom.md))
- **SITB TB 16K** → [`output/sitb-tb16k.md`](output/sitb-tb16k.md) (sumber: [`mapping/phdt-data-dictionary-sitb-tb16k.csv`](mapping/phdt-data-dictionary-sitb-tb16k.csv); file mentah: [`raw/sitb-tb16k-kolom.md`](raw/sitb-tb16k-kolom.md))
- **MPDN Kematian Bayi** → [`output/mpdn-kematian-bayi.md`](output/mpdn-kematian-bayi.md) (sumber: [`mapping/phdt-data-dictionary-mpdn-kematian-bayi.csv`](mapping/phdt-data-dictionary-mpdn-kematian-bayi.csv), PHDT Data Dictionary; **belum ada file mentah dan daftar variabel BQ**, belum ada comprehensive review)
- **MPDN Kematian Ibu** → [`output/mpdn-kematian-ibu.md`](output/mpdn-kematian-ibu.md) (sumber: [`mapping/phdt-data-dictionary-mpdn-kematian-ibu.csv`](mapping/phdt-data-dictionary-mpdn-kematian-ibu.csv), PHDT Data Dictionary; **belum ada file mentah dan daftar variabel BQ**, belum ada comprehensive review)
- **ePuskesmas Pelayanan Pasien** → [`output/epus-pelayanan.md`](output/epus-pelayanan.md) (sumber: [`mapping/phdt-data-dictionary-epus-pelayanan.csv`](mapping/phdt-data-dictionary-epus-pelayanan.csv), sheet `epus layanan`; ⚠️ **belum comprehensive review**, belum ada file mentah dan daftar variabel BQ)
- **ePuskesmas Kunjungan Ibu Hamil** → [`output/epus-kunjungan-ibu-hamil.md`](output/epus-kunjungan-ibu-hamil.md) (sumber: [`mapping/phdt-data-dictionary-epus-kunjungan-ibu-hamil.csv`](mapping/phdt-data-dictionary-epus-kunjungan-ibu-hamil.csv), sheet `old epusk kunjungan ibu hamil`; ⚠️ **belum comprehensive review**, belum ada file mentah dan daftar variabel BQ)
- **ePuskesmas Laboratorium** → [`output/epus-lab.md`](output/epus-lab.md) (sumber: [`mapping/phdt-data-dictionary-epus-lab.csv`](mapping/phdt-data-dictionary-epus-lab.csv), sheet `epus lab`; ⚠️ **belum comprehensive review**, belum ada file mentah dan daftar variabel BQ)
- **ePuskesmas Rujukan Eksternal** → [`output/epus-rujukan-eksternal.md`](output/epus-rujukan-eksternal.md) (sumber: [`mapping/phdt-data-dictionary-epus-rujukan-eksternal.csv`](mapping/phdt-data-dictionary-epus-rujukan-eksternal.csv), sheet `epus rujukan eksternal`; ⚠️ **belum comprehensive review**, belum ada file mentah dan daftar variabel BQ)
- **ePuskesmas KIA Harian ANC** → [`output/epus-anc.md`](output/epus-anc.md) (sumber: [`mapping/phdt-data-dictionary-epus-anc.csv`](mapping/phdt-data-dictionary-epus-anc.csv), sheet `epus ordal anc`; ⚠️ **belum comprehensive review**, belum ada file mentah dan daftar variabel BQ)
- **ePuskesmas KIA Harian INC** → [`output/epus-inc.md`](output/epus-inc.md) (sumber: [`mapping/phdt-data-dictionary-epus-inc.csv`](mapping/phdt-data-dictionary-epus-inc.csv), sheet `epus ordal inc`; ⚠️ **belum comprehensive review**, belum ada file mentah dan daftar variabel BQ)
- **ePuskesmas KIA Harian PNC** → [`output/epus-pnc.md`](output/epus-pnc.md) (sumber: [`mapping/phdt-data-dictionary-epus-pnc.csv`](mapping/phdt-data-dictionary-epus-pnc.csv), sheet `epus ordal pnc`; ⚠️ **belum comprehensive review**, belum ada file mentah dan daftar variabel BQ)
- **ePuskesmas KIA Harian MTBS** → [`output/epus-mtbs.md`](output/epus-mtbs.md) (sumber: [`mapping/phdt-data-dictionary-epus-mtbs.csv`](mapping/phdt-data-dictionary-epus-mtbs.csv), sheet `epus mtbs`; ⚠️ **belum comprehensive review**, belum ada file mentah dan daftar variabel BQ)
- **ePuskesmas KIA Harian MTBM** → [`output/epus-mtbm.md`](output/epus-mtbm.md) (sumber: [`mapping/phdt-data-dictionary-epus-mtbm.csv`](mapping/phdt-data-dictionary-epus-mtbm.csv), sheet `epus mbtm`; ⚠️ **belum comprehensive review**, belum ada file mentah dan daftar variabel BQ)
- **ePuskesmas KIA Harian Tumbuh Kembang Anak** → [`output/epus-tumbang-anak.md`](output/epus-tumbang-anak.md) (sumber: [`mapping/phdt-data-dictionary-epus-tumbang-anak.csv`](mapping/phdt-data-dictionary-epus-tumbang-anak.csv), sheet `epusk tumbang`; ⚠️ **belum comprehensive review**, belum ada file mentah dan daftar variabel BQ)
- **ePuskesmas KIA Harian Tumbuh Kembang DDTK** → [`output/epus-tumbang-ddtk.md`](output/epus-tumbang-ddtk.md) (sumber: [`mapping/phdt-data-dictionary-epus-tumbang-ddtk.csv`](mapping/phdt-data-dictionary-epus-tumbang-ddtk.csv), sheet `epus DDTKSDIDTK`; ⚠️ **belum comprehensive review**, belum ada file mentah dan daftar variabel BQ)
- **ePuskesmas Tumbuh Kembang - KPSP** → [`output/epus-tumbang-kpsp.md`](output/epus-tumbang-kpsp.md) (sumber: [`mapping/phdt-data-dictionary-epus-tumbang-kpsp.csv`](mapping/phdt-data-dictionary-epus-tumbang-kpsp.csv), sheet `KPSP` di `Childhood_Development_Toolkit_Data_Dictionary.xlsx`; ⚠️ **belum comprehensive review**, belum ada file mentah dan daftar variabel BQ)
- **ePuskesmas Tumbuh Kembang - TDD** → [`output/epus-tumbang-tdd.md`](output/epus-tumbang-tdd.md) (sumber: [`mapping/phdt-data-dictionary-epus-tumbang-tdd.csv`](mapping/phdt-data-dictionary-epus-tumbang-tdd.csv), sheet `TDD New` di `Childhood_Development_Toolkit_Data_Dictionary.xlsx`; ⚠️ **belum comprehensive review**, belum ada file mentah dan daftar variabel BQ)
- **ePuskesmas Tumbuh Kembang - TDL** → [`output/epus-tumbang-tdl.md`](output/epus-tumbang-tdl.md) (sumber: [`mapping/phdt-data-dictionary-epus-tumbang-tdl.csv`](mapping/phdt-data-dictionary-epus-tumbang-tdl.csv), sheet `TDL New` di `Childhood_Development_Toolkit_Data_Dictionary.xlsx`; ⚠️ **belum comprehensive review**, belum ada file mentah dan daftar variabel BQ)
- **ePuskesmas Tumbuh Kembang - KMPE** → [`output/epus-tumbang-kmpe.md`](output/epus-tumbang-kmpe.md) (sumber: [`mapping/phdt-data-dictionary-epus-tumbang-kmpe.csv`](mapping/phdt-data-dictionary-epus-tumbang-kmpe.csv), sheet `KMPE` di `Childhood_Development_Toolkit_Data_Dictionary.xlsx`; ⚠️ **belum comprehensive review**, belum ada file mentah dan daftar variabel BQ)
- **ePuskesmas Tumbuh Kembang - M-CHAT-R** → [`output/epus-tumbang-mchat.md`](output/epus-tumbang-mchat.md) (sumber: [`mapping/phdt-data-dictionary-epus-tumbang-mchat.csv`](mapping/phdt-data-dictionary-epus-tumbang-mchat.csv), sheet `M-CHAT` di `Childhood_Development_Toolkit_Data_Dictionary.xlsx`; ⚠️ **belum comprehensive review**, belum ada file mentah dan daftar variabel BQ)
- **Dapodik PAUD** → [`output/dapodik-paud.md`](output/dapodik-paud.md) (sumber: [`mapping/phdt-data-dictionary-dapodik-paud.csv`](mapping/phdt-data-dictionary-dapodik-paud.csv), sheet `Copy of DAPODIK` di `Childhood_Development_Toolkit_Data_Dictionary.xlsx`, ⚠️ belum comprehensive review)
- **SITB - TB 01 (Kartu Pengobatan Pasien)** → [`output/sitb-tb01.md`](output/sitb-tb01.md) (sumber: [`mapping/phdt-data-dictionary-sitb-tb01.csv`](mapping/phdt-data-dictionary-sitb-tb01.csv), ⚠️ belum comprehensive review)
- **SITB - TB 02 (Kartu Identitas Pasien)** → [`output/sitb-tb02.md`](output/sitb-tb02.md) (sumber: [`mapping/phdt-data-dictionary-sitb-tb02.csv`](mapping/phdt-data-dictionary-sitb-tb02.csv), ⚠️ belum comprehensive review)
- **ELSMIL Ibu Hamil** → [`output/elsmil-ibu-hamil.md`](output/elsmil-ibu-hamil.md) (sumber: [`mapping/phdt-data-dictionary-elsmil-ibu-hamil.csv`](mapping/phdt-data-dictionary-elsmil-ibu-hamil.csv), ⚠️ belum comprehensive review)
- **ELSMIL Pasca Persalinan** → [`output/elsmil-pasca-persalinan.md`](output/elsmil-pasca-persalinan.md) (sumber: [`mapping/phdt-data-dictionary-elsmil-pasca-persalinan.csv`](mapping/phdt-data-dictionary-elsmil-pasca-persalinan.csv), ⚠️ belum comprehensive review)
- **ELSMIL Baduta** → [`output/elsmil-baduta.md`](output/elsmil-baduta.md) (sumber: [`mapping/phdt-data-dictionary-elsmil-baduta.csv`](mapping/phdt-data-dictionary-elsmil-baduta.csv), ⚠️ belum comprehensive review)
- **SIPTM** → [`output/siptm.md`](output/siptm.md) (sumber: [`mapping/phdt-data-dictionary-siptm.csv`](mapping/phdt-data-dictionary-siptm.csv), ⚠️ belum comprehensive review)
- **ASIK - Data Skrining PTM** → [`output/asik-skrining-ptm.md`](output/asik-skrining-ptm.md) (sumber: [`mapping/phdt-data-dictionary-asik-skrining-ptm.csv`](mapping/phdt-data-dictionary-asik-skrining-ptm.csv), ⚠️ belum comprehensive review)
- **ePuskesmas Tumbuh Kembang - GPPH** → [`output/epus-tumbang-gpph.md`](output/epus-tumbang-gpph.md) (sumber: [`mapping/phdt-data-dictionary-epus-tumbang-gpph.csv`](mapping/phdt-data-dictionary-epus-tumbang-gpph.csv), sheet `GPPH` di `Childhood_Development_Toolkit_Data_Dictionary.xlsx`; ⚠️ **belum comprehensive review**, belum ada file mentah dan daftar variabel BQ)
- **SiGizi Balita BNBA** → [`output/sigizi-balita-bnba.md`](output/sigizi-balita-bnba.md) (sumber: [`mapping/phdt-data-dictionary-sigizi-balita-bnba.csv`](mapping/phdt-data-dictionary-sigizi-balita-bnba.csv), sheet `Copy of SiGizi_Balita` baris 2-538 di `PHDT_SIGIZI.xlsx`; BQ: `balita bnba`; ⚠️ belum comprehensive review)
- **SiGizi Balita Vitamin A** → [`output/sigizi-balita-vitamin-a.md`](output/sigizi-balita-vitamin-a.md) (sumber: [`mapping/phdt-data-dictionary-sigizi-balita-vitamin-a.csv`](mapping/phdt-data-dictionary-sigizi-balita-vitamin-a.csv), sheet `Copy of Sigizi Balita Vitamin A` baris 2-akhir di `PHDT_SIGIZI.xlsx`; BQ: `vitamin a`; ⚠️ belum comprehensive review)
- **SiGizi Balita Mendapat PMT 2024** → [`output/sigizi-balita-mendapat-pmt-2024.md`](output/sigizi-balita-mendapat-pmt-2024.md) (sumber: [`mapping/phdt-data-dictionary-sigizi-balita-mendapat-pmt-2024.csv`](mapping/phdt-data-dictionary-sigizi-balita-mendapat-pmt-2024.csv), sheet `Copy of SiGizi_Balita` baris 539-887 di `PHDT_SIGIZI.xlsx`; BQ: `mendapat pmt 2024`; ⚠️ belum comprehensive review)
- **SiGizi Balita Pemantauan PMT 2024** → [`output/sigizi-balita-pemantauan-pmt-2024.md`](output/sigizi-balita-pemantauan-pmt-2024.md) (sumber: [`mapping/phdt-data-dictionary-sigizi-balita-pemantauan-pmt-2024.csv`](mapping/phdt-data-dictionary-sigizi-balita-pemantauan-pmt-2024.csv), sheet `Copy of SiGizi_Balita` baris 888-1142 di `PHDT_SIGIZI.xlsx`; BQ: `pemantauan pmt 2024`; ⚠️ belum comprehensive review)
- **SiGizi Balita ASI Eksklusif** → [`output/sigizi-balita-asi-eksklusif.md`](output/sigizi-balita-asi-eksklusif.md) (sumber: [`mapping/phdt-data-dictionary-sigizi-balita-asi-eksklusif.csv`](mapping/phdt-data-dictionary-sigizi-balita-asi-eksklusif.csv), sheet `Copy of Sigizi Balita ASI Ekskl` baris 2-akhir di `PHDT_SIGIZI.xlsx`; BQ: `asi eksklusif`; ⚠️ belum comprehensive review)
- **SiGizi Balita MPASI** → [`output/sigizi-balita-mpasi.md`](output/sigizi-balita-mpasi.md) (sumber: [`mapping/phdt-data-dictionary-sigizi-balita-mpasi.csv`](mapping/phdt-data-dictionary-sigizi-balita-mpasi.csv), sheet `Copy of Sigizi Balita MPASI` baris 2-akhir di `PHDT_SIGIZI.xlsx`; BQ: `mpasi`; ⚠️ belum comprehensive review)
- **SiGizi PMT 2025 BB Tidak Naik - Pantau** → [`output/sigizi-pmt2025-bb-tidak-naik-pantau.md`](output/sigizi-pmt2025-bb-tidak-naik-pantau.md) (sumber: [`mapping/phdt-data-dictionary-sigizi-pmt2025-bb-tidak-naik-pantau.csv`](mapping/phdt-data-dictionary-sigizi-pmt2025-bb-tidak-naik-pantau.csv), sheet `Copy of SiGizi_PMT_2025` baris 2-347 di `PHDT_SIGIZI.xlsx`; BQ: `bb tidak naik pantau pmt 2025`; ⚠️ belum comprehensive review)
- **SiGizi PMT 2025 BB Tidak Naik - Riwayat** → [`output/sigizi-pmt2025-bb-tidak-naik-riwayat.md`](output/sigizi-pmt2025-bb-tidak-naik-riwayat.md) (sumber: [`mapping/phdt-data-dictionary-sigizi-pmt2025-bb-tidak-naik-riwayat.csv`](mapping/phdt-data-dictionary-sigizi-pmt2025-bb-tidak-naik-riwayat.csv), sheet `Copy of SiGizi_PMT_2025` baris 1568-2013 di `PHDT_SIGIZI.xlsx`; BQ: `bb tidak naik riwayat pmt 2025`; ⚠️ belum comprehensive review)
- **SiGizi PMT 2025 BB Tidak Naik - Survey** → [`output/sigizi-pmt2025-bb-tidak-naik-survey.md`](output/sigizi-pmt2025-bb-tidak-naik-survey.md) (sumber: [`mapping/phdt-data-dictionary-sigizi-pmt2025-bb-tidak-naik-survey.csv`](mapping/phdt-data-dictionary-sigizi-pmt2025-bb-tidak-naik-survey.csv), sheet `Copy of SiGizi_PMT_2025` baris 2014-akhir di `PHDT_SIGIZI.xlsx`; BQ: `bb tidak naik survey pmt 2025`; ⚠️ belum comprehensive review)
- **SiGizi PMT 2025 BB Kurang - Pantau** → [`output/sigizi-pmt2025-bb-kurang-pantau.md`](output/sigizi-pmt2025-bb-kurang-pantau.md) (sumber: [`mapping/phdt-data-dictionary-sigizi-pmt2025-bb-kurang-pantau.csv`](mapping/phdt-data-dictionary-sigizi-pmt2025-bb-kurang-pantau.csv), sheet `Copy of SiGizi_PMT_2025` baris 348-786 di `PHDT_SIGIZI.xlsx`; BQ: `bb kurang pantau pmt 2025`; ⚠️ belum comprehensive review)
- **SiGizi PMT 2025 BB Kurang - Riwayat** → [`output/sigizi-pmt2025-bb-kurang-riwayat.md`](output/sigizi-pmt2025-bb-kurang-riwayat.md) (sumber: [`mapping/phdt-data-dictionary-sigizi-pmt2025-bb-kurang-riwayat.csv`](mapping/phdt-data-dictionary-sigizi-pmt2025-bb-kurang-riwayat.csv), sheet `Copy of SiGizi_PMT_2025` baris 1568-2013 di `PHDT_SIGIZI.xlsx`; BQ: `bb kurang riwayat pmt 2025`; ⚠️ belum comprehensive review)
- **SiGizi PMT 2025 BB Kurang - Survey** → [`output/sigizi-pmt2025-bb-kurang-survey.md`](output/sigizi-pmt2025-bb-kurang-survey.md) (sumber: [`mapping/phdt-data-dictionary-sigizi-pmt2025-bb-kurang-survey.csv`](mapping/phdt-data-dictionary-sigizi-pmt2025-bb-kurang-survey.csv), sheet `Copy of SiGizi_PMT_2025` baris 2014-akhir di `PHDT_SIGIZI.xlsx`; BQ: `bb kurang survey pmt 2025`; ⚠️ belum comprehensive review)
- **SiGizi PMT 2025 Gizi Kurang - Pantau** → [`output/sigizi-pmt2025-gizi-kurang-pantau.md`](output/sigizi-pmt2025-gizi-kurang-pantau.md) (sumber: [`mapping/phdt-data-dictionary-sigizi-pmt2025-gizi-kurang-pantau.csv`](mapping/phdt-data-dictionary-sigizi-pmt2025-gizi-kurang-pantau.csv), sheet `Copy of SiGizi_PMT_2025` baris 787-1567 di `PHDT_SIGIZI.xlsx`; BQ: `gizi kurang pantau pmt 2025`; ⚠️ belum comprehensive review)
- **SiGizi PMT 2025 Gizi Kurang - Riwayat** → [`output/sigizi-pmt2025-gizi-kurang-riwayat.md`](output/sigizi-pmt2025-gizi-kurang-riwayat.md) (sumber: [`mapping/phdt-data-dictionary-sigizi-pmt2025-gizi-kurang-riwayat.csv`](mapping/phdt-data-dictionary-sigizi-pmt2025-gizi-kurang-riwayat.csv), sheet `Copy of SiGizi_PMT_2025` baris 1568-2013 di `PHDT_SIGIZI.xlsx`; BQ: `gizi kurang riwayat pmt 2025`; ⚠️ belum comprehensive review)
- **SiGizi PMT 2025 Gizi Kurang - Survey** → [`output/sigizi-pmt2025-gizi-kurang-survey.md`](output/sigizi-pmt2025-gizi-kurang-survey.md) (sumber: [`mapping/phdt-data-dictionary-sigizi-pmt2025-gizi-kurang-survey.csv`](mapping/phdt-data-dictionary-sigizi-pmt2025-gizi-kurang-survey.csv), sheet `Copy of SiGizi_PMT_2025` baris 2014-akhir di `PHDT_SIGIZI.xlsx`; BQ: `gizi kurang survey pmt 2025`; ⚠️ belum comprehensive review)
- **SiGizi Ibu Nifas** → [`output/sigizi-ibu-nifas.md`](output/sigizi-ibu-nifas.md) (sumber: [`mapping/phdt-data-dictionary-sigizi-ibu-nifas.csv`](mapping/phdt-data-dictionary-sigizi-ibu-nifas.csv), sheet `Copy of SiGizi Nifas` baris 2-akhir di `PHDT_SIGIZI.xlsx`; BQ: `ibu nifas`; ⚠️ belum comprehensive review)
- **SiGizi Kohort Ibu** → [`output/sigizi-kohort-ibu.md`](output/sigizi-kohort-ibu.md) (sumber: [`mapping/phdt-data-dictionary-sigizi-kohort-ibu.csv`](mapping/phdt-data-dictionary-sigizi-kohort-ibu.csv), sheet `Copy of SiGizi Kohort Ibu` baris 2-akhir di `PHDT_SIGIZI.xlsx`; BQ: `kohort ibu`; ⚠️ belum comprehensive review)

File ini adalah **konsolidasi** lintas form. Angka per form di sini harus sama dengan file `output/<form>.md`.

Belum: SITB TB 13 SO/RO, form lain. Form ePuskesmas lain (Kunjungan Pasien BPJS, Kunjungan Pasien, Kohort KIA, LPLPO, Dapodik Antropometri DDTK) belum ada mapping yang bisa dicocokkan, tidak dihitung. SITB TB 01/TB 02, ELSMIL (3 form), SIPTM, ASIK Skrining PTM, dan 17 form SiGizi sudah dihitung (lihat catatan di bawah). SiGizi Daftar Balita dan Daftar Bumil belum (draft mapping ditunda).

---

## Daftar isi

Di file ini:
1. [Ringkasan semua form](#ringkasan-semua-form)
2. [Jumlah per CodeSystem](#jumlah-per-codesystem-code-unik-lintas-form)
3. [Payload per resource](#payload-per-resource-semua-form)
4. [Catatan](#catatan)
5. [Log perubahan output](#log-perubahan-output)

File terpisah (detail):
- [`frekuensi-payload.md`](frekuensi-payload.md): setiap payload unik (resource + code pembeda + display) dan form yang memakainya
- [`frekuensi-code.md`](frekuensi-code.md): setiap code unik (1 code per baris, dengan CodeSystem) dan form yang memakainya
- `output/<form>.md`: output per form dengan nomor baris dictionary (lihat daftar form di atas)

---

## Ringkasan semua form

Baris **ePus ...** = 11 form ePuskesmas dari `PHDT_ePus.xlsx` (⚠️ belum comprehensive review). Kolom **Variabel raw** = jumlah kolom di file mentah (kalau belum ada file mentah: jumlah variabel di dictionary; Maternal Outcome & Raffle = variabel Kobo, MPDN = variabel dictionary tanpa placeholder). Kolom **Code SP** = jumlah code dengan CodeSystem `http://terminology.kemkes.go.id/sp` (sudah termasuk di kolom Code).

| Form | Variabel raw | Payload | Code | Code SP |
|---|---|---|---|---|
| Maternal Outcome | 12 | 12 | 14 | 4 |
| Raffle | 12 | 8 | 6 | 4 |
| SiGizi ANC | 49 | 61 | 142 | 18 |
| SITB TB 06 | 96 | 56 | 276 | 9 |
| SITB TB 03 SO | 84 | 62 | 329 | 10 |
| SITB TB 03 RO | 144 | 50 | 377 | 11 |
| SITB TB 04 | 114 | 69 | 579 | 24 |
| SITB TB 16K | 40 | 21 | 35 | 14 |
| MPDN Kematian Bayi | 37 | 19 | 112 | 37 |
| MPDN Kematian Ibu | 24 | 10 | 50 | 17 |
| ePus Pelayanan Pasien | 81 | 47 | 62 | 2 |
| ePus Kunjungan Ibu Hamil | 68 | 114 | 198 | 11 |
| ePus Laboratorium | 22 | 309 | 429 | 0 |
| ePus Rujukan Eksternal | 23 | 5 | 0 | 0 |
| ePus ANC | 123 | 155 | 321 | 24 |
| ePus INC | 93 | 69 | 206 | 22 |
| ePus PNC | 107 | 82 | 161 | 27 |
| ePus MTBS | 187 | 125 | 268 | 19 |
| ePus MTBM | 105 | 57 | 139 | 20 |
| ePus Tumbang Anak | 34 | 19 | 55 | 8 |
| ePus Tumbang DDTK | 38 | 29 | 68 | 10 |
| ePus Tumbang KPSP | 123 | 14 | 0 | 0 |
| ePus Tumbang TDD | 37 | 8 | 0 | 0 |
| ePus Tumbang TDL | 6 | 4 | 8 | 0 |
| ePus Tumbang KMPE | 14 | 1 | 0 | 0 |
| ePus Tumbang M-CHAT-R | 20 | 1 | 0 | 0 |
| Dapodik PAUD | 75 | 42 | 190 | 75 |
| ePus Tumbang GPPH | 10 | 1 | 40 | 20 |
| SITB TB 01 | 82 | 37 | 94 | 15 |
| SITB TB 02 | 22 | 13 | 15 | 0 |
| ELSMIL Ibu Hamil | 36 | 36 | 104 | 33 |
| ELSMIL Pasca Persalinan | 29 | 24 | 96 | 35 |
| ELSMIL Baduta | 38 | 31 | 78 | 29 |
| SIPTM | 60 | 52 | 214 | 7 |
| ASIK Skrining PTM | 67 | 104 | 146 | 10 |
| SiGizi Balita BNBA | 33 | 24 | 48 | 10 |
| SiGizi Balita Vitamin A | 14 | 22 | 47 | 9 |
| SiGizi Balita Mendapat PMT 2024 | 30 | 15 | 44 | 14 |
| SiGizi Balita Pemantauan PMT 2024 | 18 | 9 | 12 | 5 |
| SiGizi Balita ASI Eksklusif | 22 | 11 | 36 | 28 |
| SiGizi Balita MPASI | 28 | 9 | 30 | 2 |
| SiGizi PMT 2025 BB Tidak Naik - Pantau | 24 | 15 | 32 | 17 |
| SiGizi PMT 2025 BB Tidak Naik - Riwayat | 34 | 19 | 74 | 23 |
| SiGizi PMT 2025 BB Tidak Naik - Survey | 20 | 5 | 16 | 4 |
| SiGizi PMT 2025 BB Kurang - Pantau | 24 | 21 | 46 | 21 |
| SiGizi PMT 2025 BB Kurang - Riwayat | 34 | 19 | 74 | 23 |
| SiGizi PMT 2025 BB Kurang - Survey | 20 | 5 | 16 | 4 |
| SiGizi PMT 2025 Gizi Kurang - Pantau | 51 | 42 | 101 | 29 |
| SiGizi PMT 2025 Gizi Kurang - Riwayat | 34 | 19 | 74 | 23 |
| SiGizi PMT 2025 Gizi Kurang - Survey | 20 | 5 | 16 | 4 |
| SiGizi Ibu Nifas | 14 | 11 | 12 | 3 |
| SiGizi Kohort Ibu | 42 | 63 | 94 | 3 |
| **Total (non-unik)** | **2574** | **2061** | **5584** | **737** |
| **Total unik** | – | **668** | **1717** | **335** |
| Selisih (dipakai ulang) | – | 1393 | 3867 | 402 |

---

## Jumlah per CodeSystem (code unik lintas form)

Daftar code satu per baris: lihat [`frekuensi-code.md`](frekuensi-code.md).

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 573 |
| http://terminology.kemkes.go.id/sp | 335 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 288 |
| http://loinc.org | 272 |
|  | 43 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 26 |
| http://terminology.kemkes.go.id/CodeSystem/examination | 21 |
| http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes | 19 |
| http://hl7.org/fhir/sid/icd-10 | 17 |
| http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment | 17 |
| http://sys-ids.kemkes.go.id/kfa | 14 |
| http://terminology.kemkes.go.id/CodeSystem/organization-type | 13 |
| http://terminology.kemkes.go.id | 11 |
| http://hl7.org/fhir/sid/cvx | 8 |
| http://terminology.kemkes.go.id/CodeSystem/location-type | 7 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC | 7 |
| http://hl7.org/fhir/sid/icd-9-cm | 7 |
| https://loinc.org | 6 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 5 |
| http://terminology.hl7.org/CodeSystem/admit-source | 5 |
| http://sys-ids.kemkes.go.id/kf | 5 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 3 |
| http://terminology.kemkes.go.id/CodeSystem/composition-type | 3 |
| hhttp://terminology.kemkes.go.id/CodeSystem/organization-type | 3 |
| http://terminology.kemkes.go.id/Codesystem/kpsp | 3 |
| http://terminology.kemkes.go.id/CodeSystem/tb-case-definition | 2 |
| http://terminology.kemkes.go.id/CodeSystem/kptl | 1 |
| http://terminology.hl7. org/CodeSystem/admit -source | 1 |
| http://terminology.kemkes.go.id/CodeSystem/ | 1 |
| http://terminology.kemkes.go.id/CodeSystem/immunization-reason | 1 |
| **Total** | **1717** |

---

## Payload per resource (semua form)

Baris = form, kolom = resource FHIR. Code pembeda tiap payload: lihat [`frekuensi-payload.md`](frekuensi-payload.md).

| Form | Observation | ServiceRequest | DiagnosticReport | Specimen | Condition | Procedure | Encounter | Patient | QuestionnaireResponse | Immunization | PractitionerRole | EpisodeOfCare | MedicationRequest | MedicationDispense | RelatedPerson | Practitioner | CarePlan | Coverage | MedicationStatement | Organization | Goal | Location | Composition | FamilyMemberHistory | Group | AllergyIntolerance | Medication | Account | ClinicalImpression | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maternal Outcome | 5 | – | – | – | 1 | – | 1 | 1 | – | – | 1 | 2 | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | 12 |
| Raffle | 1 | – | – | – | 1 | – | 1 | 1 | – | – | – | 1 | – | – | – | 2 | – | – | – | – | – | 1 | – | – | – | – | – | – | – | 8 |
| SiGizi ANC | 30 | 6 | 6 | 6 | 1 | 3 | 1 | 1 | – | 1 | 1 | 1 | 2 | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 61 |
| SITB TB 06 | 17 | 9 | 9 | 8 | 2 | 2 | 1 | 1 | 1 | – | – | 3 | – | – | – | – | 1 | – | – | 1 | – | 1 | – | – | – | – | – | – | – | 56 |
| SITB TB 03 SO | 23 | 9 | 9 | 9 | 1 | 4 | 1 | 1 | 1 | – | – | 1 | – | – | – | – | 1 | 1 | – | 1 | – | – | – | – | – | – | – | – | – | 62 |
| SITB TB 03 RO | 18 | 7 | 7 | 7 | 1 | 3 | 1 | 1 | 1 | – | – | 1 | – | – | – | – | 1 | 1 | – | 1 | – | – | – | – | – | – | – | – | – | 50 |
| SITB TB 04 | 17 | 16 | 16 | 16 | 1 | – | 1 | 1 | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 69 |
| SITB TB 16K | 14 | 1 | – | – | 1 | – | 1 | 1 | 1 | – | – | – | – | – | 1 | – | – | – | – | – | – | – | – | – | 1 | – | – | – | – | 21 |
| MPDN Kematian Bayi | 16 | – | – | – | – | – | – | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 1 | – | – | – | – | – | – | 19 |
| MPDN Kematian Ibu | 7 | – | – | – | 1 | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 1 | – | – | – | – | – | – | 10 |
| ePus Pelayanan Pasien | 24 | 1 | – | – | 9 | 2 | 1 | 1 | – | – | – | – | 1 | 1 | – | 1 | 3 | 1 | – | – | – | – | – | 1 | – | 1 | – | – | – | 47 |
| ePus Kunjungan Ibu Hamil | 46 | 17 | 16 | 16 | 4 | 5 | 1 | 1 | – | 2 | – | 1 | 1 | 1 | – | – | – | 1 | 2 | – | – | – | – | – | – | – | – | – | – | 114 |
| ePus Laboratorium | 92 | 74 | 73 | 65 | – | – | 1 | 1 | – | – | 2 | – | – | – | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | 309 |
| ePus Rujukan Eksternal | – | 1 | – | – | 1 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | 5 |
| ePus ANC | 82 | 19 | 19 | 6 | 3 | 3 | 1 | 1 | – | 3 | 14 | 1 | 1 | 1 | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | 155 |
| ePus INC | 49 | 1 | – | – | 3 | 9 | 1 | 1 | 1 | – | 1 | 1 | – | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | 69 |
| ePus PNC | 50 | 3 | 2 | 1 | 4 | 9 | 1 | 1 | – | – | 2 | 1 | 2 | 2 | – | 1 | 1 | – | 1 | – | – | – | – | – | – | – | 1 | – | – | 82 |
| ePus MTBS | 53 | 9 | 8 | 8 | 7 | 14 | 1 | 1 | 1 | 17 | – | – | 2 | 2 | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | 125 |
| ePus MTBM | 35 | 1 | – | – | 4 | 8 | 1 | 1 | 1 | 3 | – | 1 | – | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | 57 |
| ePus Tumbang Anak | 14 | – | – | – | 2 | 1 | – | – | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 19 |
| ePus Tumbang DDTK | 14 | 1 | – | – | 3 | 4 | 1 | 1 | 2 | – | – | – | – | – | 2 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | 29 |
| ePus Tumbang KPSP | – | – | – | – | – | – | – | – | 14 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 14 |
| ePus Tumbang TDD | – | – | – | – | – | – | – | – | 8 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 8 |
| ePus Tumbang TDL | 4 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 4 |
| ePus Tumbang KMPE | – | – | – | – | – | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 1 |
| ePus Tumbang M-CHAT-R | – | – | – | – | – | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 1 |
| Dapodik PAUD | 32 | – | – | – | 4 | – | 1 | 1 | – | – | – | – | – | – | 3 | – | – | – | – | – | – | – | – | – | – | – | – | 1 | – | 42 |
| ePus Tumbang GPPH | – | – | – | – | – | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 1 |
| SITB TB 01 | 25 | – | – | – | 1 | 1 | 1 | 1 | 1 | – | – | 2 | – | – | 2 | – | 1 | – | 2 | – | – | – | – | – | – | – | – | – | – | 37 |
| SITB TB 02 | 1 | 2 | – | – | 1 | – | 1 | 1 | 1 | – | – | – | 2 | 2 | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | 1 | 13 |
| ELSMIL Ibu Hamil | 28 | 2 | 1 | 1 | 2 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 36 |
| ELSMIL Pasca Persalinan | 22 | – | – | – | 1 | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 24 |
| ELSMIL Baduta | 29 | – | – | – | – | – | – | 1 | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 31 |
| SIPTM | 31 | 3 | 1 | 1 | 7 | 2 | 1 | 1 | – | – | – | – | 1 | – | – | – | – | – | – | – | 3 | – | – | 1 | – | – | – | – | – | 52 |
| ASIK Skrining PTM | 41 | 20 | 20 | 14 | 1 | – | 1 | 1 | – | – | 6 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 104 |
| SiGizi Balita BNBA | 14 | – | – | – | 1 | 1 | 1 | 1 | 1 | – | – | – | 2 | 2 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 24 |
| SiGizi Balita Vitamin A | 13 | – | – | – | 1 | 1 | 1 | 1 | – | – | – | – | 2 | 2 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 22 |
| SiGizi Balita Mendapat PMT 2024 | 12 | – | – | – | 1 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 15 |
| SiGizi Balita Pemantauan PMT 2024 | 6 | – | – | – | 1 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 9 |
| SiGizi Balita ASI Eksklusif | 7 | – | – | – | 1 | – | 1 | 1 | – | – | – | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 11 |
| SiGizi Balita MPASI | 6 | – | – | – | 1 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 9 |
| SiGizi PMT 2025 BB Tidak Naik - Pantau | 12 | – | – | – | 1 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 15 |
| SiGizi PMT 2025 BB Tidak Naik - Riwayat | 16 | – | – | – | 1 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 19 |
| SiGizi PMT 2025 BB Tidak Naik - Survey | 1 | – | – | – | 1 | – | 1 | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 5 |
| SiGizi PMT 2025 BB Kurang - Pantau | 18 | – | – | – | 1 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 21 |
| SiGizi PMT 2025 BB Kurang - Riwayat | 16 | – | – | – | 1 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 19 |
| SiGizi PMT 2025 BB Kurang - Survey | 1 | – | – | – | 1 | – | 1 | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 5 |
| SiGizi PMT 2025 Gizi Kurang - Pantau | 39 | – | – | – | 1 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 42 |
| SiGizi PMT 2025 Gizi Kurang - Riwayat | 16 | – | – | – | 1 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 19 |
| SiGizi PMT 2025 Gizi Kurang - Survey | 1 | – | – | – | 1 | – | 1 | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 5 |
| SiGizi Ibu Nifas | 3 | – | – | – | 1 | 3 | 1 | 1 | – | – | – | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 11 |
| SiGizi Kohort Ibu | 17 | 3 | 3 | 3 | 15 | 1 | 14 | 1 | – | 2 | 1 | 2 | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 63 |
| **Total (non-unik)** | **1018** | **205** | **190** | **161** | **98** | **76** | **54** | **46** | **42** | **29** | **28** | **21** | **16** | **15** | **15** | **10** | **9** | **6** | **5** | **3** | **3** | **2** | **2** | **2** | **1** | **1** | **1** | **1** | **1** | **2061** |
| **Total unik** | **418** | **27** | **108** | **6** | **33** | **40** | **1** | **1** | **1** | **2** | **1** | **6** | **5** | **4** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **668** |

---

## Catatan

- Organization tidak dihitung di Kobo, SiGizi, TB 04, dan TB 16K (lookup master data, bloknya tidak ditulis di dictionary). Location di Maternal Outcome dan SiGizi ANC juga lookup (tidak dihitung), tapi di Raffle dihitung karena dibuat dari form.
- SiGizi ANC: faskes & posyandu berupa string → lookup master data. PractitionerRole petugas lab → lookup (tidak dihitung). 6 Specimen di SiGizi ANC hanya 2 jenis (darah vena ×5, urine ×1). Code Observation dengan 2 coding (LOINC + ANC custom) dihitung dua-duanya.
- PractitionerRole tenaga pemeriksa SiGizi ANC dan PractitionerRole MO sama-sama tanpa code pembeda tetap (code-nya opsi), jadi dihitung sebagai payload yang sama.
- EpisodeOfCare: Maternal Outcome = ANC & PNC ditutup (finished, hari ke-43); Raffle = ANC dicari dulu, kalau tidak ada baru dibuat.
- Encounter muncul di 2 blok kamus (data utama + statusHistory) = 1 payload.
- SITB TB 06, TB 03 SO, TB 03 RO: blok faskes (Organization + Location) **dihitung** karena dimapping dari variabel faskes di form (match + update). TB 04 dan TB 16K: faskes lookup (TB 04 lewat metadata `puskesmas_id` / `puskesmas_name`). PractitionerRole petugas lab/radiografer dan Practitioner PJ SITB = lookup master data (tidak dihitung). Baris yang dicoret di sheet tidak dipakai. Lihat asumsi A1–A12 di `revisi.md`.
- SITB: opsi coded yang mengikuti jawaban ikut dihitung sebagai code (reasonCode ServiceRequest, CarePlan activity, admitSource, jawaban QuestionnaireResponse, component lab, metode biakan) — disetujui, lihat `aturan.md`. Karena itu jumlah code SITB besar (mis. TB 04: 16 ServiceRequest × 9 alasan pemeriksaan, 16 Specimen × 11 jenis contoh uji).
- SITB TB 04: 1 dictionary untuk TB 04 Fasyankes dan TB 04 Rujukan (header sama). TB 03 RO: follow up 24 bulan = 1 template BTA + 1 template Biakan (asumsi A7); setiap pemeriksaan lab punya ServiceRequest + Specimen + Observation + DiagnosticReport (T03R-4).
- SITB: EpisodeOfCare TB-SO / TB-RO, Patient, Encounter, Condition A15.0, Observation umur (424144002), HIV/DM, lab (11545-1, X0993xx) dipakai ulang di beberapa form SITB → total unik jauh lebih kecil dari non-unik.

- MPDN Kematian Bayi / Ibu: **belum ada comprehensive review**, file mentah, dan daftar variabel BQ (tally BQ belum bisa dicek; kolom Nama Column BQ kosong). Satu payload Composition per laporan; Location di `Composition.contained` ikut di dalam Composition (tidak dihitung terpisah). Dua Patient (ibu + bayi) di Bayi dihitung 2 payload. Tidak ada Encounter, dan Practitioner PJ MPDN tidak dibuat (lookup). `Composition.type` (COM000001/2/3) dihitung sebagai code; ICD-PM / ICD-MM (daftar eksternal) dan kode ICD dinamis di Condition tidak dihitung. Asumsi dan temuan: `revisi.md` bagian MPDN.
- **ePuskesmas (11 form, ⚠️ belum comprehensive review)**: dictionary dari `PHDT_ePus.xlsx`, tidak ada file mentah dan daftar BQ. Pemisahan blok payload otomatis (heuristik), belum dicek manual per blok; blok Condition yang `clinicalStatus`-nya setelah `code` bisa menyatu, dan Laboratorium (banyak baris alias), Kunjungan Ibu Hamil, ANC, MTBS kemungkinan perlu dicek ulang. Organization/Location dianggap lookup (tidak dihitung). Code dihitung dari path determining/opsi coded saja; `conclusionCode` tidak dihitung; kode dinamis (`{kode ...}`) = payload tanpa code. Detail asumsi EA1–EA10: `revisi.md`.

- **Tumbuh Kembang tambahan (KPSP, TDD, TDL, KMPE, M-CHAT-R, GPPH)**: dari `Childhood_Development_Toolkit_Data_Dictionary.xlsx`, ⚠️ belum comprehensive review. 1 QuestionnaireResponse per kelompok umur/kuesioner (KPSP 14, TDD 8, KMPE/M-CHAT-R/GPPH 1). Jawaban Ya/Tidak (`valueBoolean`) bukan code, jadi code hanya di GPPH (opsi `valueCoding`, 40) dan TDL (Observation tajam penglihatan, 8). Tidak ada blok Patient/Encounter di sheet (hanya reference), jadi tidak dihitung. Sheet `TDD Deprecated`, `TDL Deprecated`, `SDIDTK` (sama persis dengan DDTK yang sudah ada), `PAUD`, dan `Copy of DAPODIK` tidak dihitung. Detail EB1–EB6: `revisi.md`.

- **Dapodik PAUD**: sheet `Copy of DAPODIK` (dipilih user karena jumlah variabel paling dekat dengan PHDT: 75 unik / 87 baris vs 93), ⚠️ belum comprehensive review. 42 payload (Observation 32, Condition 4, RelatedPerson 3, Patient, Encounter, Account), 190 code (Condition 55, Observation 135). Pemisahan blok otomatis (heuristik), belum dicek manual.

- **SITB TB 01 / TB 02, ELSMIL (Ibu Hamil, Pasca Persalinan, Baduta), SIPTM, ASIK Skrining PTM**: dari 5 file CSV PHDT (⚠️ belum comprehensive review, tanpa daftar BQ dan file mentah). Variabel raw = variabel unik di dictionary. Payload/code: TB 01 37/94, TB 02 13/15, Elsmil Ibu Hamil 36/104, Pasca Persalinan 24/96, Baduta 31/78, SIPTM 52/214, ASIK PTM 104/146. Elsmil 1 file dipecah 3 form menurut kolom Categories (baris 2–483 / 484–810 / 811–akhir). SIPTM tidak ada di tracker maupun daftar PHDT: ditambahkan sebagai #237, jumlah variabel dihitung dari mapping (60 unik). Blok payload otomatis (heuristik), belum dicek manual.

- **SiGizi 17 form (Balita BNBA, Vitamin A, Mendapat/Pemantauan PMT 2024, ASI, MPASI, PMT 2025 ×9, Ibu Nifas, Kohort Ibu)**: dari `PHDT_SIGIZI.xlsx` + schema BQ user (⚠️ belum comprehensive review, belum ada file mentah). Nama Column BQ diisi dari schema; tally cocok kecuali MPASI `pengukuran`. `puskesmas`/`posyandu` = lookup (Organization/Location tidak dihitung), `detail` → extension `sigizi-detail`. Kohort Ibu: 14 Encounter (12 kunjungan bulanan + utama + persalinan) dihitung masing-masing. PMT 2025: Riwayat & Survey 1 dictionary untuk 3 kategori (dihitung 3 form). Asumsi/temuan SG1–SG14: `revisi.md`.

---

## Log perubahan output
- 2026-11-24: Tambah 17 form SiGizi (314 payload / 772 code; Kohort Ibu 63/94, PMT 2025 Pantau Gizi Kurang 42/101, BNBA 24/48, …), ⚠️ belum comprehensive review. Total non-unik **2061 payload / 5584 code** (sebelumnya 1747 / 4812), unik **668 / 1717** (sebelumnya 635 / 1631).
- 2026-11-24: Tambah 7 form dari 5 CSV (SITB TB 01 37/94, TB 02 13/15, ELSMIL Ibu Hamil 36/104, Pasca Persalinan 24/96, Baduta 31/78, SIPTM 52/214, ASIK Skrining PTM 104/146), ⚠️ belum comprehensive review. Total non-unik **1747 payload / 4812 code**, unik **635 / 1631** (sebelumnya 1450 / 4065 dan 552 / 1393).
- 2026-11-24: Ringkasan semua form: tambah kolom **Variabel raw** (total 612). Di `output/<form>.md` baris "Variabel di Excel export" diganti "Variabel raw" dan ditambahkan juga untuk Maternal Outcome (12), Raffle (12), MPDN Kematian Bayi (37), MPDN Kematian Ibu (24). Angka payload/code tidak berubah.
- 2026-11-24: Tambah 2 form MPDN dari `PHDT_Data_Dictionary_-_MPDN.csv`: Kematian Bayi (19 payload / 112 code) dan Kematian Ibu (10 / 50). Belum ada daftar variabel BQ dan belum ada comprehensive review. Total non-unik 339 / 1758 → **368 / 1920**, unik 148 / 434 → **164 / 510**. Resource baru: Composition. Tabel di file ini dan `frekuensi-*.md` dibuat ulang untuk 10 form dengan `scripts/consolidate.py` (hasilnya identik dengan versi lama untuk 8 form sebelumnya).
- 2026-11-18: Ringkasan semua form: tambah kolom **Code SP** (CodeSystem `http://terminology.kemkes.go.id/sp`). Daftar form diberi link. Output per form diberi baris File terkait (link ke `output.md`, frekuensi, dictionary, file mentah) dan baris Code SP di Ringkasan.
- 2026-11-18: `output.md` dirampingkan: tambah Daftar isi; tabel Frekuensi payload dan Frekuensi code dipindah ke file terpisah `frekuensi-payload.md` dan `frekuensi-code.md`. Angka tidak berubah.
- 2026-11-18: Format tabel: "Jumlah per CodeSystem" hanya CodeSystem + jumlah (daftar code per baris ada di tabel Frekuensi code). "Payload per resource" ditranspos: baris = form, kolom = resource FHIR, tanpa kolom pembeda; ditambah baris Total unik. Bagian Catatan dikembalikan (sempat terhapus 17 Nov) dan diperbarui. Angka tidak berubah. Format yang sama dipakai di `output/<form>.md` (Code per CodeSystem tanpa daftar code).
- 2026-11-17: TB 04 lookup faskes saja (blok Org/Location dihapus, 71 → **69** payload). TB 03 RO: ServiceRequest + Specimen + DiagnosticReport untuk 7 pemeriksaan lab (30 → **50** payload, 357 → **377** code). TB 06 kolom AC (tambahan user) tidak dihitung. Total non-unik 339 / 1758, unik 148 / 434.
- 2026-11-17: Blok faskes dikembalikan (A3): +2 payload di TB 06 (56), TB 04 (71); +1 di TB 03 SO (62), TB 03 RO (30). Code tidak berubah.
- 2026-11-17: SP001138–SP001140 dibatalkan; SP001137 jadi "Paduan lainnya" (TB 03 SO & RO). Varian teks paduan ditambah sebagai baris alias (code lama, tidak dihitung ulang). TB 03 SO 332 → **329** code, TB 03 RO 356 → **357** code. Total non-unik 315 / 1738, unik 147 / 434.
- 2026-11-17: Code lokal baru: TB 06 SP001136 Belum Mulai Pengobatan (code 275 → **276**); TB 03 SO SP001137–SP001140 paduan pengobatan (code 328 → **332**). Hasil Tes HIV "Tidak Diketahui" → dataAbsentReason unknown (tidak dihitung). Total non-unik 315 / 1740, unik 147 / 437.
- 2026-11-17: Jawaban user diterapkan. TB 06: 55 → **54 payload** (Coverage dihapus karena No. BPJS dicoret di sheet), code tetap 275. TB 03 SO: tetap 61 / 328 (Status Pengobatan masuk CarePlan sebagai teks). TB 16K: 24/39 → **21 payload / 35 code** (Practitioner, PractitionerRole kader, dan Observation SP000211 dicoret di sheet). Total non-unik 315 / 1735, unik 147 / 432.
- 2026-11-17: Tambah 5 form SITB: TB 06 (55 payload / 275 code), TB 03 SO (61 / 328), TB 03 RO (29 / 356), TB 04 (69 / 579), TB 16K (24 / 39). Total non-unik jadi 319 payload / 1739 code, unik 148 / 434. Semua tabel di file ini sekarang dibuat ulang dari 8 dictionary di `mapping/` (angka 3 form lama tidak berubah; urutan baris yang frekuensinya sama di tabel Payload per resource bisa bergeser).
- 2026-11-16: Dictionary SiGizi ANC diganti nama jadi `mapping/phdt-data-dictionary-sigizi-anc.csv` (sumbernya PHDT Data Dictionary, bukan Kobo). Angka tidak berubah.
- 2026-11-16: Ringkasan `output/sigizi-anc.md`: baris "Variabel BQ di luar payload" diganti "Variabel di Excel export" (SiGizi ANC: 49, angka saja). Baris ini tidak muncul di form Kobo (tidak ada file mentah). Angka tidak berubah.
- 2026-11-16: SiGizi ANC final setelah jawaban R1–R14: **61 payload, 142 code** (−6 PractitionerRole lab, +1 Observation usia kehamilan 18185-9; code −6 Laboratory worker, +1 18185-9). Tabel frekuensi, CodeSystem, dan payload per resource diperbarui untuk 3 form. Total non-unik 81 payload / 162 code, unik 68 / 132.
- 2026-11-16: Tambah SiGizi ANC sebagai angka sementara (66 payload, 147 code; total non-unik 86/167, unik 67/132). Tabel frekuensi belum diubah sampai R1–R14 dijawab. `scripts/form_output.py` mengenali code pembeda untuk Procedure, ServiceRequest, DiagnosticReport, Specimen, Immunization, MedicationRequest, MedicationDispense (output MO & Raffle tidak berubah).
- 2026-11-16: Revisi reference & path di kedua dictionary (lihat `revisi.md`). Angka tidak berubah.
- 2026-11-16: MO: blok Organization & Location dihapus dari dictionary (lookup master data). Angka tidak berubah.
- 2026-11-16: Output per form menampilkan path tiap variabel BQ dan tanda 🔎 untuk lookup master data. Semua variabel BQ sudah masuk payload (0 di luar payload). Angka tidak berubah.
- 2026-11-16: Tambah output per form (`output/maternal-outcome.md`, `output/raffle.md`), dibuat dengan `scripts/form_output.py`. Raffle jadi 8 payload (Practitioner data entry ditambahkan user di commit `9da6c8d`). Total non-unik 20, unik 15.
- 2026-11-13: Ringkasan diberi Total non-unik vs unik; kolom Jenis resource dihapus. Section payload per form diganti jadi satu tabel "Payload per resource (semua form)".
- 2026-11-13: Raffle direvisi: Location dibuat dari form (payload jadi 7), Condition.code jadi SP001135. Total unik lintas form jadi 15 payload, 8 jenis resource, 19 code.
- 2026-11-13: Tambah form Raffle (6 payload, 6 baris code). Total unik lintas form jadi 14 payload, 18 code. Frekuensi Practitioner, Patient, Encounter, EpisodeOfCare ANC, dan code ANC naik jadi 2.
- 2026-11-13: Kolom "Code per submission" dihapus (tidak dipakai).
- 2026-11-13: Tabel frekuensi payload diberi kolom Code pembeda, Display, dan Variabel Kobo.
- 2026-11-13: Dicek ulang dengan Kobo_3. Angka tidak berubah (12 payload, 14 code). Display SP000396/SP000397 dibetulkan.
- 2026-11-13: File dipisah jadi `aturan.md`, `revisi.md`, `output.md`.
- 2026-11-13: Maternal Outcome dihitung. Repo dibersihkan; isi lama ada di commit `0aba562`.
- 2026-11-24: Tambah Dapodik PAUD (42 payload, 190 code, ⚠️ belum comprehensive review). Total non-unik 1450 payload / 4065 code; unik 552 / 1393.
