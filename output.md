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
- **ASIK - CKG Bayi Baru Lahir** (versi 2 dipakai; v1 tersedia) → [`output/asik-ckg-bbl.md`](output/asik-ckg-bbl.md) · [v1](output/asik-ckg-bbl-v1.md) (sumber: [`mapping/phdt-data-dictionary-asik-ckg-bbl.csv`](mapping/phdt-data-dictionary-asik-ckg-bbl.csv), sheet `CKG Bayi Baru Lahir 2` di `PHDT_ASIK_CKG.xlsx`, ⚠️ belum comprehensive review)
- **ASIK - CKG Balita dan Anak Pra-Sekolah** (versi 2 dipakai; v1 tersedia) → [`output/asik-ckg-balita.md`](output/asik-ckg-balita.md) · [v1](output/asik-ckg-balita-v1.md) (sumber: [`mapping/phdt-data-dictionary-asik-ckg-balita.csv`](mapping/phdt-data-dictionary-asik-ckg-balita.csv), sheet `Sheet9`, ⚠️ belum comprehensive review)
- **ASIK - CKG Dewasa Laki-laki** → [`output/asik-ckg-dewasa-laki.md`](output/asik-ckg-dewasa-laki.md) (sumber: [`mapping/phdt-data-dictionary-asik-ckg-dewasa-laki.csv`](mapping/phdt-data-dictionary-asik-ckg-dewasa-laki.csv), ⚠️ belum comprehensive review)
- **ASIK - CKG Dewasa Perempuan** → [`output/asik-ckg-dewasa-perempuan.md`](output/asik-ckg-dewasa-perempuan.md) (sumber: [`mapping/phdt-data-dictionary-asik-ckg-dewasa-perempuan.csv`](mapping/phdt-data-dictionary-asik-ckg-dewasa-perempuan.csv), ⚠️ belum comprehensive review)
- **ASIK - CKG Lansia** (versi 27 April 2026 dipakai; 2026 dan 2025 tersedia) → [`output/asik-ckg-lansia.md`](output/asik-ckg-lansia.md) · [2026](output/asik-ckg-lansia-2026.md) · [2025](output/asik-ckg-lansia-2025.md) (sumber: [`mapping/phdt-data-dictionary-asik-ckg-lansia.csv`](mapping/phdt-data-dictionary-asik-ckg-lansia.csv), ⚠️ belum comprehensive review)
- **Informed Consent** → [`output/informed-consent.md`](output/informed-consent.md) (sumber: [`mapping/phdt-data-dictionary-informed-consent.csv`](mapping/phdt-data-dictionary-informed-consent.csv), ⚠️ belum comprehensive review)
- **SiHepi - Form Rekap 3e** → [`output/sihepi-rekap-3e.md`](output/sihepi-rekap-3e.md) (sumber: [`mapping/phdt-data-dictionary-sihepi-rekap-3e.csv`](mapping/phdt-data-dictionary-sihepi-rekap-3e.csv), ⚠️ belum comprehensive review)
- **eKohort - Pelayanan Ibu ANC** (Final Format dipakai; file eKohort lama tersedia) → [`output/ekohort-anc.md`](output/ekohort-anc.md) · [lama](output/ekohort-anc-lama.md) (sumber: [`mapping/phdt-data-dictionary-ekohort-anc.csv`](mapping/phdt-data-dictionary-ekohort-anc.csv), ⚠️ belum comprehensive review)
- **eKohort - Pelayanan Ibu Bersalin (INC)** → [`output/ekohort-inc.md`](output/ekohort-inc.md) (sumber: [`mapping/phdt-data-dictionary-ekohort-inc.csv`](mapping/phdt-data-dictionary-ekohort-inc.csv), ⚠️ belum comprehensive review)
- **SIM RS - Tripat ANC** (tracker #228) → [`output/rs-tripat-anc.md`](output/rs-tripat-anc.md) (sumber: [`mapping/phdt-data-dictionary-rs-tripat-anc.csv`](mapping/phdt-data-dictionary-rs-tripat-anc.csv), sheet `Mapping ANC Tripat` di `PHDT_Data_Rumah_Sakit.xlsx`, ⚠️ belum comprehensive review)
- **SIM RS - Tripat BBL (sheet 'INC BBL')** (tracker #231) → [`output/rs-tripat-bbl.md`](output/rs-tripat-bbl.md) (sumber: [`mapping/phdt-data-dictionary-rs-tripat-bbl.csv`](mapping/phdt-data-dictionary-rs-tripat-bbl.csv), sheet `Mapping INC BBL Tripat` di `PHDT_Data_Rumah_Sakit.xlsx`, ⚠️ belum comprehensive review)
- **SIM RS - Tripat PNC** (tracker #230) → [`output/rs-tripat-pnc.md`](output/rs-tripat-pnc.md) (sumber: [`mapping/phdt-data-dictionary-rs-tripat-pnc.csv`](mapping/phdt-data-dictionary-rs-tripat-pnc.csv), sheet `Mapping PNC Tripat` di `PHDT_Data_Rumah_Sakit.xlsx`, ⚠️ belum comprehensive review)
- **SIM RS - Narmada INC** (tracker #219) → [`output/rs-narmada-inc.md`](output/rs-narmada-inc.md) (sumber: [`mapping/phdt-data-dictionary-rs-narmada-inc.csv`](mapping/phdt-data-dictionary-rs-narmada-inc.csv), sheet `Mapping INC Narmada` di `PHDT_Data_Rumah_Sakit.xlsx`, ⚠️ belum comprehensive review)
- **SIM RS - Narmada KIA** (tracker #222) → [`output/rs-narmada-kia.md`](output/rs-narmada-kia.md) (sumber: [`mapping/phdt-data-dictionary-rs-narmada-kia.csv`](mapping/phdt-data-dictionary-rs-narmada-kia.csv), sheet `Mapping KIA Narmada` di `PHDT_Data_Rumah_Sakit.xlsx`, ⚠️ belum comprehensive review)
- **SIM RS - Panti Nugroho ANC** (tracker #200) → [`output/rs-panti-nugroho-anc.md`](output/rs-panti-nugroho-anc.md) (sumber: [`mapping/phdt-data-dictionary-rs-panti-nugroho-anc.csv`](mapping/phdt-data-dictionary-rs-panti-nugroho-anc.csv), sheet `Mapping ANC Panti Nugroho✅` di `PHDT_Data_Rumah_Sakit.xlsx`, ⚠️ belum comprehensive review)
- **SIM RS - Panti Nugroho INC** (tracker #201) → [`output/rs-panti-nugroho-inc.md`](output/rs-panti-nugroho-inc.md) (sumber: [`mapping/phdt-data-dictionary-rs-panti-nugroho-inc.csv`](mapping/phdt-data-dictionary-rs-panti-nugroho-inc.csv), sheet `Mapping INC RSUD Panti Nugroho` di `PHDT_Data_Rumah_Sakit.xlsx`, ⚠️ belum comprehensive review)
- **SIM RS - Panti Nugroho PNC** (tracker #202) → [`output/rs-panti-nugroho-pnc.md`](output/rs-panti-nugroho-pnc.md) (sumber: [`mapping/phdt-data-dictionary-rs-panti-nugroho-pnc.csv`](mapping/phdt-data-dictionary-rs-panti-nugroho-pnc.csv), sheet `Mapping PNC Panti Nugroho✅` di `PHDT_Data_Rumah_Sakit.xlsx`, ⚠️ belum comprehensive review)
- **SIM RS - Panti Nugroho BBL** (tracker #203) → [`output/rs-panti-nugroho-bbl.md`](output/rs-panti-nugroho-bbl.md) (sumber: [`mapping/phdt-data-dictionary-rs-panti-nugroho-bbl.csv`](mapping/phdt-data-dictionary-rs-panti-nugroho-bbl.csv), sheet `Mapping BBL Panti Nugroho✅` di `PHDT_Data_Rumah_Sakit.xlsx`, ⚠️ belum comprehensive review)
- **SIM RS - Panti Nugroho Diabetes Melitus** (tracker #205) → [`output/rs-panti-nugroho-dm.md`](output/rs-panti-nugroho-dm.md) (sumber: [`mapping/phdt-data-dictionary-rs-panti-nugroho-dm.csv`](mapping/phdt-data-dictionary-rs-panti-nugroho-dm.csv), sheet `DM Panti Nugroho` di `PHDT_Data_Rumah_Sakit.xlsx`, ⚠️ belum comprehensive review)
- **SIM RS - Panti Nugroho Hipertensi** (tracker #206) → [`output/rs-panti-nugroho-ht.md`](output/rs-panti-nugroho-ht.md) (sumber: [`mapping/phdt-data-dictionary-rs-panti-nugroho-ht.csv`](mapping/phdt-data-dictionary-rs-panti-nugroho-ht.csv), sheet `HT Panti Nugroho` di `PHDT_Data_Rumah_Sakit.xlsx`, ⚠️ belum comprehensive review)
- **SIM RS - Panti Nugroho Stroke** (tracker #207) → [`output/rs-panti-nugroho-stroke.md`](output/rs-panti-nugroho-stroke.md) (sumber: [`mapping/phdt-data-dictionary-rs-panti-nugroho-stroke.csv`](mapping/phdt-data-dictionary-rs-panti-nugroho-stroke.csv), sheet `Stroke Panti Nugroho (Template)` di `PHDT_Data_Rumah_Sakit.xlsx`, ⚠️ belum comprehensive review)
- **SIM RS - Ummu Hani ANC** (tracker #173) → [`output/rs-ummu-hani-anc.md`](output/rs-ummu-hani-anc.md) (sumber: [`mapping/phdt-data-dictionary-rs-ummu-hani-anc.csv`](mapping/phdt-data-dictionary-rs-ummu-hani-anc.csv), sheet `Mapping ANC RS Ummu Hani✅` di `PHDT_Data_Rumah_Sakit.xlsx`, ⚠️ belum comprehensive review)
- **SIM RS - Ummu Hani INC** (tracker #174) → [`output/rs-ummu-hani-inc.md`](output/rs-ummu-hani-inc.md) (sumber: [`mapping/phdt-data-dictionary-rs-ummu-hani-inc.csv`](mapping/phdt-data-dictionary-rs-ummu-hani-inc.csv), sheet `Mapping INC RS Ummu Hani ✅` di `PHDT_Data_Rumah_Sakit.xlsx`, ⚠️ belum comprehensive review)
- **SIM RS - Ummu Hani PNC** (tracker #175) → [`output/rs-ummu-hani-pnc.md`](output/rs-ummu-hani-pnc.md) (sumber: [`mapping/phdt-data-dictionary-rs-ummu-hani-pnc.csv`](mapping/phdt-data-dictionary-rs-ummu-hani-pnc.csv), sheet `Mapping PNC RS Ummu Hani ✅` di `PHDT_Data_Rumah_Sakit.xlsx`, ⚠️ belum comprehensive review)
- **SIM RS - Ummu Hani BBL** (tracker #176) → [`output/rs-ummu-hani-bbl.md`](output/rs-ummu-hani-bbl.md) (sumber: [`mapping/phdt-data-dictionary-rs-ummu-hani-bbl.csv`](mapping/phdt-data-dictionary-rs-ummu-hani-bbl.csv), sheet `Mapping BBL RS Ummu Hani` di `PHDT_Data_Rumah_Sakit.xlsx`, ⚠️ belum comprehensive review)
- **SIM RS - MPH ANC** (tracker #155) → [`output/rs-mph-anc.md`](output/rs-mph-anc.md) (sumber: [`mapping/phdt-data-dictionary-rs-mph-anc.csv`](mapping/phdt-data-dictionary-rs-mph-anc.csv), sheet `Mapping ANC RS MPH` di `PHDT_Data_Rumah_Sakit.xlsx`, ⚠️ belum comprehensive review)
- **SIM RS - MPH INC** (tracker #156) → [`output/rs-mph-inc.md`](output/rs-mph-inc.md) (sumber: [`mapping/phdt-data-dictionary-rs-mph-inc.csv`](mapping/phdt-data-dictionary-rs-mph-inc.csv), sheet `Mapping INC RS MPH` di `PHDT_Data_Rumah_Sakit.xlsx`, ⚠️ belum comprehensive review)
- **SIM RS - MPH PNC** (tracker #157) → [`output/rs-mph-pnc.md`](output/rs-mph-pnc.md) (sumber: [`mapping/phdt-data-dictionary-rs-mph-pnc.csv`](mapping/phdt-data-dictionary-rs-mph-pnc.csv), sheet `Mapping PNC RS MPH` di `PHDT_Data_Rumah_Sakit.xlsx`, ⚠️ belum comprehensive review)
- **SIM RS - MPH BBL** (tracker #158) → [`output/rs-mph-bbl.md`](output/rs-mph-bbl.md) (sumber: [`mapping/phdt-data-dictionary-rs-mph-bbl.csv`](mapping/phdt-data-dictionary-rs-mph-bbl.csv), sheet `Mapping BBL RS MPH` di `PHDT_Data_Rumah_Sakit.xlsx`, ⚠️ belum comprehensive review)
- **SIM RS - MPH Diabetes Melitus** (tracker #160) → [`output/rs-mph-dm.md`](output/rs-mph-dm.md) (sumber: [`mapping/phdt-data-dictionary-rs-mph-dm.csv`](mapping/phdt-data-dictionary-rs-mph-dm.csv), sheet `DM MPH (Template)` di `PHDT_Data_Rumah_Sakit.xlsx`, ⚠️ belum comprehensive review)
- **SIM RS - MPH Hipertensi** (tracker #161) → [`output/rs-mph-ht.md`](output/rs-mph-ht.md) (sumber: [`mapping/phdt-data-dictionary-rs-mph-ht.csv`](mapping/phdt-data-dictionary-rs-mph-ht.csv), sheet `HT MPH (Template)` di `PHDT_Data_Rumah_Sakit.xlsx`, ⚠️ belum comprehensive review)
- **SIM RS - Siaga Medika ANC** (tracker #146) → [`output/rs-siaga-medika-anc.md`](output/rs-siaga-medika-anc.md) (sumber: [`mapping/phdt-data-dictionary-rs-siaga-medika-anc.csv`](mapping/phdt-data-dictionary-rs-siaga-medika-anc.csv), sheet `Mapping ANC Siaga Medika ✅` di `PHDT_Data_Rumah_Sakit.xlsx`, ⚠️ belum comprehensive review)
- **SIM RS - Siaga Medika INC** (tracker #147) → [`output/rs-siaga-medika-inc.md`](output/rs-siaga-medika-inc.md) (sumber: [`mapping/phdt-data-dictionary-rs-siaga-medika-inc.csv`](mapping/phdt-data-dictionary-rs-siaga-medika-inc.csv), sheet `Mapping INC Siaga Medika✅` di `PHDT_Data_Rumah_Sakit.xlsx`, ⚠️ belum comprehensive review)
- **SIM RS - Siaga Medika PNC** (tracker #148) → [`output/rs-siaga-medika-pnc.md`](output/rs-siaga-medika-pnc.md) (sumber: [`mapping/phdt-data-dictionary-rs-siaga-medika-pnc.csv`](mapping/phdt-data-dictionary-rs-siaga-medika-pnc.csv), sheet `Mapping PNC Siaga Medika✅` di `PHDT_Data_Rumah_Sakit.xlsx`, ⚠️ belum comprehensive review)
- **SIM RS - Siaga Medika BBL** (tracker #149) → [`output/rs-siaga-medika-bbl.md`](output/rs-siaga-medika-bbl.md) (sumber: [`mapping/phdt-data-dictionary-rs-siaga-medika-bbl.csv`](mapping/phdt-data-dictionary-rs-siaga-medika-bbl.csv), sheet `Mapping BBL Siaga Medika✅` di `PHDT_Data_Rumah_Sakit.xlsx`, ⚠️ belum comprehensive review)
- **SIM RS - PKU INC** (tracker #183) → [`output/rs-pku-inc.md`](output/rs-pku-inc.md) (sumber: [`mapping/phdt-data-dictionary-rs-pku-inc.csv`](mapping/phdt-data-dictionary-rs-pku-inc.csv), sheet `Mapping INC PKU Muhammadiyah✅` di `PHDT_Data_Rumah_Sakit.xlsx`, ⚠️ belum comprehensive review)
- **SIM RS - PKU PNC** (tracker #184) → [`output/rs-pku-pnc.md`](output/rs-pku-pnc.md) (sumber: [`mapping/phdt-data-dictionary-rs-pku-pnc.csv`](mapping/phdt-data-dictionary-rs-pku-pnc.csv), sheet `Mapping PNC PKU Muhammadiyah✅` di `PHDT_Data_Rumah_Sakit.xlsx`, ⚠️ belum comprehensive review)
- **SIM RS - Goetoeng ANC** (tracker #191) → [`output/rs-goetoeng-anc.md`](output/rs-goetoeng-anc.md) (sumber: [`mapping/phdt-data-dictionary-rs-goetoeng-anc.csv`](mapping/phdt-data-dictionary-rs-goetoeng-anc.csv), sheet `Mapping ANC Goeteng` di `PHDT_Data_Rumah_Sakit.xlsx`, ⚠️ belum comprehensive review)
- **SIM RS - Goetoeng INC** (tracker #192) → [`output/rs-goetoeng-inc.md`](output/rs-goetoeng-inc.md) (sumber: [`mapping/phdt-data-dictionary-rs-goetoeng-inc.csv`](mapping/phdt-data-dictionary-rs-goetoeng-inc.csv), sheet `Mapping INC Goeteng` di `PHDT_Data_Rumah_Sakit.xlsx`, ⚠️ belum comprehensive review)
- **SIM RS - Goetoeng PNC** (tracker #193) → [`output/rs-goetoeng-pnc.md`](output/rs-goetoeng-pnc.md) (sumber: [`mapping/phdt-data-dictionary-rs-goetoeng-pnc.csv`](mapping/phdt-data-dictionary-rs-goetoeng-pnc.csv), sheet `Mapping PNC Goeteng` di `PHDT_Data_Rumah_Sakit.xlsx`, ⚠️ belum comprehensive review)
- **SIM RS - Goetoeng BBL** (tracker #194) → [`output/rs-goetoeng-bbl.md`](output/rs-goetoeng-bbl.md) (sumber: [`mapping/phdt-data-dictionary-rs-goetoeng-bbl.csv`](mapping/phdt-data-dictionary-rs-goetoeng-bbl.csv), sheet `Mapping BBL Goeteng` di `PHDT_Data_Rumah_Sakit.xlsx`, ⚠️ belum comprehensive review)
- **SIM RS - Goetoeng Diabetes Melitus** (tracker #196) → [`output/rs-goetoeng-dm.md`](output/rs-goetoeng-dm.md) (sumber: [`mapping/phdt-data-dictionary-rs-goetoeng-dm.csv`](mapping/phdt-data-dictionary-rs-goetoeng-dm.csv), sheet `Mapping DM Goeteng` di `PHDT_Data_Rumah_Sakit.xlsx`, ⚠️ belum comprehensive review)
- **SIM RS - Goetoeng Hipertensi** (tracker #197) → [`output/rs-goetoeng-ht.md`](output/rs-goetoeng-ht.md) (sumber: [`mapping/phdt-data-dictionary-rs-goetoeng-ht.csv`](mapping/phdt-data-dictionary-rs-goetoeng-ht.csv), sheet `Mapping HT Goeteng` di `PHDT_Data_Rumah_Sakit.xlsx`, ⚠️ belum comprehensive review)
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
4. [Versi ASIK CKG](#versi-asik-ckg)
5. [Catatan](#catatan)
6. [Log perubahan output](#log-perubahan-output)

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
| ASIK CKG Bayi Baru Lahir (v2) | 35 | 25 | 41 | 1 |
| ASIK CKG Balita (v2) | 57 | 32 | 102 | 10 |
| ASIK CKG Dewasa Laki-laki | 123 | 61 | 202 | 3 |
| ASIK CKG Dewasa Perempuan | 130 | 66 | 223 | 3 |
| ASIK CKG Lansia (27 Apr 2026) | 188 | 101 | 458 | 11 |
| Informed Consent | 27 | 3 | 8 | 8 |
| SIHEPI Rekap 3e | 93 | 65 | 118 | 49 |
| eKohort ANC | 34 | 43 | 78 | 0 |
| eKohort INC | 84 | 58 | 74 | 0 |
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
| SIM RS Tripat ANC | 31 | 20 | 28 | 0 |
| SIM RS Tripat BBL (sheet 'INC BBL') | 36 | 23 | 20 | 0 |
| SIM RS Tripat PNC | 36 | 24 | 28 | 0 |
| SIM RS Narmada INC | 225 | 86 | 262 | 2 |
| SIM RS Narmada KIA | 70 | 50 | 107 | 2 |
| SIM RS Panti Nugroho ANC | 43 | 31 | 68 | 11 |
| SIM RS Panti Nugroho INC | 55 | 37 | 118 | 8 |
| SIM RS Panti Nugroho PNC | 85 | 67 | 131 | 21 |
| SIM RS Panti Nugroho BBL | 49 | 31 | 55 | 2 |
| SIM RS Panti Nugroho Diabetes Melitus | 19 | 7 | 4 | 0 |
| SIM RS Panti Nugroho Hipertensi | 40 | 23 | 21 | 4 |
| SIM RS Panti Nugroho Stroke | 35 | 20 | 23 | 4 |
| SIM RS Ummu Hani ANC | 33 | 23 | 49 | 3 |
| SIM RS Ummu Hani INC | 54 | 41 | 94 | 6 |
| SIM RS Ummu Hani PNC | 65 | 53 | 110 | 6 |
| SIM RS Ummu Hani BBL | 45 | 30 | 51 | 2 |
| SIM RS MPH ANC | 43 | 33 | 87 | 12 |
| SIM RS MPH INC | 54 | 40 | 91 | 6 |
| SIM RS MPH PNC | 59 | 43 | 104 | 6 |
| SIM RS MPH BBL | 73 | 42 | 59 | 2 |
| SIM RS MPH Diabetes Melitus | 44 | 24 | 37 | 3 |
| SIM RS MPH Hipertensi | 35 | 20 | 22 | 3 |
| SIM RS Siaga Medika ANC | 61 | 100 | 181 | 12 |
| SIM RS Siaga Medika INC | 58 | 42 | 125 | 12 |
| SIM RS Siaga Medika PNC | 71 | 49 | 110 | 16 |
| SIM RS Siaga Medika BBL | 64 | 37 | 48 | 2 |
| SIM RS PKU INC | 81 | 66 | 175 | 16 |
| SIM RS PKU PNC | 85 | 67 | 131 | 21 |
| SIM RS Goetoeng ANC | 21 | 106 | 111 | 22 |
| SIM RS Goetoeng INC | 35 | 64 | 245 | 12 |
| SIM RS Goetoeng PNC | 27 | 9 | 21 | 11 |
| SIM RS Goetoeng BBL | 34 | 68 | 124 | 14 |
| SIM RS Goetoeng Diabetes Melitus | 12 | 6 | 4 | 0 |
| SIM RS Goetoeng Hipertensi | 13 | 5 | 3 | 0 |
| **Total (non-unik)** | **5136** | **3902** | **9735** | **1063** |
| **Total unik** | – | **996** | **2648** | **436** |
| Selisih (dipakai ulang) | – | 2906 | 7087 | 627 |

---

## Jumlah per CodeSystem (code unik lintas form)

Daftar code satu per baris: lihat [`frekuensi-code.md`](frekuensi-code.md).

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 1062 |
| http://terminology.kemkes.go.id/sp | 436 |
| http://loinc.org | 391 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 298 |
| http://hl7.org/fhir/sid/icd-10 | 116 |
|  | 51 |
| http://hl7.org/fhir/sid/icd-9-cm | 49 |
| http://terminology.kemkes.go.id | 48 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 29 |
| http://terminology.kemkes.go.id/CodeSystem/examination | 21 |
| http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes | 19 |
| http://terminology.kemkes.go.id/CodeSystem/organization-type | 18 |
| http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment | 17 |
| http://sys-ids.kemkes.go.id/kfa | 14 |
| http://hl7.org/fhir/sid/cvx | 10 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 9 |
| http://terminology.kemkes.go.id/CodeSystem/location-type | 7 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC | 7 |
| https://loinc.org | 7 |
| http://sys-ids.kemkes.go.id/kf | 7 |
| http://terminology.hl7.org/CodeSystem/admit-source | 6 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 5 |
| hhttp://terminology.kemkes.go.id/CodeSystem/organization-type | 4 |
| http://terminology.kemkes.go.id/CodeSystem/composition-type | 3 |
| http://terminology.kemkes.go.id/Codesystem/kpsp | 3 |
| http://terminology.kemkes.go.id/CodeSystem/tb-case-definition | 2 |
| http://hl7.org/fhir/administrative-gender | 2 |
| http://terminology.kemkes.go.id/CodeSystem/kptl | 1 |
| http://terminology.hl7. org/CodeSystem/admit -source | 1 |
| http://terminology.kemkes.go.id/CodeSystem/ | 1 |
| http://terminology.kemkes.go.id/CodeSystem/immunization-reason | 1 |
| http://terminology.hl7. org/CodeSystem/v3-Ob servationInterpretatio n | 1 |
| CUSTOM | 1 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term" | 1 |
| **Total** | **2648** |

---

## Payload per resource (semua form)

Baris = form, kolom = resource FHIR. Code pembeda tiap payload: lihat [`frekuensi-payload.md`](frekuensi-payload.md).

| Form | Observation | Procedure | ServiceRequest | DiagnosticReport | Condition | Specimen | Encounter | Patient | PractitionerRole | Immunization | EpisodeOfCare | QuestionnaireResponse | Practitioner | RelatedPerson | MedicationDispense | MedicationRequest | MedicationStatement | Coverage | CarePlan | Medication | Composition | AllergyIntolerance | Organization | FamilyMemberHistory | Goal | Location | Group | Account | ClinicalImpression | Consent | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maternal Outcome | 5 | – | – | – | 1 | – | 1 | 1 | 1 | – | 2 | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 12 |
| Raffle | 1 | – | – | – | 1 | – | 1 | 1 | – | – | 1 | – | 2 | – | – | – | – | – | – | – | – | – | – | – | – | 1 | – | – | – | – | 8 |
| SiGizi ANC | 30 | 3 | 6 | 6 | 1 | 6 | 1 | 1 | 1 | 1 | 1 | – | – | – | 2 | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 61 |
| SITB TB 06 | 17 | 2 | 9 | 9 | 2 | 8 | 1 | 1 | – | – | 3 | 1 | – | – | – | – | – | – | 1 | – | – | – | 1 | – | – | 1 | – | – | – | – | 56 |
| SITB TB 03 SO | 23 | 4 | 9 | 9 | 1 | 9 | 1 | 1 | – | – | 1 | 1 | – | – | – | – | – | 1 | 1 | – | – | – | 1 | – | – | – | – | – | – | – | 62 |
| SITB TB 03 RO | 18 | 3 | 7 | 7 | 1 | 7 | 1 | 1 | – | – | 1 | 1 | – | – | – | – | – | 1 | 1 | – | – | – | 1 | – | – | – | – | – | – | – | 50 |
| SITB TB 04 | 17 | – | 16 | 16 | 1 | 16 | 1 | 1 | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 69 |
| SITB TB 16K | 14 | – | 1 | – | 1 | – | 1 | 1 | – | – | – | 1 | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | 1 | – | – | – | 21 |
| MPDN Kematian Bayi | 16 | – | – | – | – | – | – | 2 | – | – | – | – | – | – | – | – | – | – | – | – | 1 | – | – | – | – | – | – | – | – | – | 19 |
| MPDN Kematian Ibu | 7 | – | – | – | 1 | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | 1 | – | – | – | – | – | – | – | – | – | 10 |
| ePus Pelayanan Pasien | 24 | 2 | 1 | – | 9 | – | 1 | 1 | – | – | – | – | 1 | – | 1 | 1 | – | 1 | 3 | – | – | 1 | – | 1 | – | – | – | – | – | – | 47 |
| ePus Kunjungan Ibu Hamil | 46 | 5 | 17 | 16 | 4 | 16 | 1 | 1 | – | 2 | 1 | – | – | – | 1 | 1 | 2 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | 114 |
| ePus Laboratorium | 92 | – | 74 | 73 | – | 65 | 1 | 1 | 2 | – | – | – | – | – | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | 309 |
| ePus Rujukan Eksternal | – | – | 1 | – | 1 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | 5 |
| ePus ANC | 82 | 3 | 19 | 19 | 3 | 6 | 1 | 1 | 14 | 3 | 1 | – | 1 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 155 |
| ePus INC | 49 | 9 | 1 | – | 3 | – | 1 | 1 | 1 | – | 1 | 1 | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 69 |
| ePus PNC | 50 | 9 | 3 | 2 | 4 | 1 | 1 | 1 | 2 | – | 1 | – | 1 | – | 2 | 2 | 1 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | 82 |
| ePus MTBS | 53 | 14 | 9 | 8 | 7 | 8 | 1 | 1 | – | 17 | – | 1 | 1 | 1 | 2 | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 125 |
| ePus MTBM | 35 | 8 | 1 | – | 4 | – | 1 | 1 | – | 3 | 1 | 1 | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 57 |
| ePus Tumbang Anak | 14 | 1 | – | – | 2 | – | – | – | – | – | – | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 19 |
| ePus Tumbang DDTK | 14 | 4 | 1 | – | 3 | – | 1 | 1 | – | – | – | 2 | 1 | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 29 |
| ePus Tumbang KPSP | – | – | – | – | – | – | – | – | – | – | – | 14 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 14 |
| ePus Tumbang TDD | – | – | – | – | – | – | – | – | – | – | – | 8 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 8 |
| ePus Tumbang TDL | 4 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 4 |
| ePus Tumbang KMPE | – | – | – | – | – | – | – | – | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 1 |
| ePus Tumbang M-CHAT-R | – | – | – | – | – | – | – | – | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 1 |
| Dapodik PAUD | 32 | – | – | – | 4 | – | 1 | 1 | – | – | – | – | – | 3 | – | – | – | – | – | – | – | – | – | – | – | – | – | 1 | – | – | 42 |
| ePus Tumbang GPPH | – | – | – | – | – | – | – | – | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 1 |
| SITB TB 01 | 25 | 1 | – | – | 1 | – | 1 | 1 | – | – | 2 | 1 | – | 2 | – | – | 2 | – | 1 | – | – | – | – | – | – | – | – | – | – | – | 37 |
| SITB TB 02 | 1 | – | 2 | – | 1 | – | 1 | 1 | – | – | – | 1 | – | – | 2 | 2 | – | – | 1 | – | – | – | – | – | – | – | – | – | 1 | – | 13 |
| ELSMIL Ibu Hamil | 28 | – | 2 | 1 | 2 | 1 | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 36 |
| ELSMIL Pasca Persalinan | 22 | – | – | – | 1 | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 24 |
| ELSMIL Baduta | 29 | – | – | – | – | – | – | 1 | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 31 |
| SIPTM | 31 | 2 | 3 | 1 | 7 | 1 | 1 | 1 | – | – | – | – | – | – | – | 1 | – | – | – | – | – | – | – | 1 | 3 | – | – | – | – | – | 52 |
| ASIK Skrining PTM | 41 | – | 20 | 20 | 1 | 14 | 1 | 1 | 6 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 104 |
| ASIK CKG Bayi Baru Lahir (v2) | 17 | 5 | – | – | 1 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 25 |
| ASIK CKG Balita (v2) | 17 | 3 | 2 | 2 | 1 | 2 | 1 | 1 | 2 | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 32 |
| ASIK CKG Dewasa Laki-laki | 53 | – | 1 | 1 | 1 | 1 | 1 | 1 | 1 | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 61 |
| ASIK CKG Dewasa Perempuan | 58 | – | 1 | 1 | 1 | 1 | 1 | 1 | 1 | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 66 |
| ASIK CKG Lansia (27 Apr 2026) | 90 | 1 | – | – | 1 | – | 1 | 1 | – | – | – | 7 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 101 |
| Informed Consent | – | – | – | – | – | – | – | 1 | – | – | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 1 | 3 |
| SIHEPI Rekap 3e | 44 | 1 | 4 | 3 | 1 | 3 | 1 | 1 | – | 5 | 1 | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 65 |
| eKohort ANC | 20 | 1 | 5 | 5 | 1 | 5 | 1 | 1 | – | 2 | 1 | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 43 |
| eKohort INC | 46 | 4 | 1 | – | 2 | – | 1 | 1 | – | – | – | – | 3 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 58 |
| SiGizi Balita BNBA | 14 | 1 | – | – | 1 | – | 1 | 1 | – | – | – | 1 | – | 1 | 2 | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 24 |
| SiGizi Balita Vitamin A | 13 | 1 | – | – | 1 | – | 1 | 1 | – | – | – | – | – | 1 | 2 | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 22 |
| SiGizi Balita Mendapat PMT 2024 | 12 | – | – | – | 1 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 15 |
| SiGizi Balita Pemantauan PMT 2024 | 6 | – | – | – | 1 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 9 |
| SiGizi Balita ASI Eksklusif | 7 | – | – | – | 1 | – | 1 | 1 | – | – | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 11 |
| SiGizi Balita MPASI | 6 | – | – | – | 1 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 9 |
| SiGizi PMT 2025 BB Tidak Naik - Pantau | 12 | – | – | – | 1 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 15 |
| SiGizi PMT 2025 BB Tidak Naik - Riwayat | 16 | – | – | – | 1 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 19 |
| SiGizi PMT 2025 BB Tidak Naik - Survey | 1 | – | – | – | 1 | – | 1 | 1 | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 5 |
| SiGizi PMT 2025 BB Kurang - Pantau | 18 | – | – | – | 1 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 21 |
| SiGizi PMT 2025 BB Kurang - Riwayat | 16 | – | – | – | 1 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 19 |
| SiGizi PMT 2025 BB Kurang - Survey | 1 | – | – | – | 1 | – | 1 | 1 | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 5 |
| SiGizi PMT 2025 Gizi Kurang - Pantau | 39 | – | – | – | 1 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 42 |
| SiGizi PMT 2025 Gizi Kurang - Riwayat | 16 | – | – | – | 1 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 19 |
| SiGizi PMT 2025 Gizi Kurang - Survey | 1 | – | – | – | 1 | – | 1 | 1 | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 5 |
| SiGizi Ibu Nifas | 3 | 3 | – | – | 1 | – | 1 | 1 | – | – | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 11 |
| SiGizi Kohort Ibu | 17 | 1 | 3 | 3 | 15 | 3 | 14 | 1 | 1 | 2 | 2 | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 63 |
| SIM RS Tripat ANC | 9 | 1 | – | – | 1 | – | 1 | 1 | 2 | 1 | 1 | – | 2 | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | 20 |
| SIM RS Tripat BBL (sheet 'INC BBL') | 11 | 2 | – | – | 1 | – | 1 | 1 | 2 | – | 1 | – | 2 | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 23 |
| SIM RS Tripat PNC | 13 | 1 | – | – | 2 | – | 1 | 1 | 2 | – | 1 | – | 2 | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | 24 |
| SIM RS Narmada INC | 57 | 5 | – | – | 10 | – | 1 | 1 | – | 4 | 3 | – | 1 | 1 | – | – | 1 | – | – | – | – | 1 | – | 1 | – | – | – | – | – | – | 86 |
| SIM RS Narmada KIA | 37 | 2 | – | – | 4 | – | 1 | 1 | – | 1 | 2 | – | 1 | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | 50 |
| SIM RS Panti Nugroho ANC | 17 | 2 | – | – | 2 | – | 1 | 1 | 1 | 3 | 1 | – | 1 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 31 |
| SIM RS Panti Nugroho INC | 23 | 3 | 1 | – | 2 | – | 1 | 1 | 1 | – | 2 | – | 2 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 37 |
| SIM RS Panti Nugroho PNC | 38 | 10 | 1 | – | 6 | – | 1 | 1 | 1 | – | 1 | – | 1 | – | 3 | 2 | – | – | – | 2 | – | – | – | – | – | – | – | – | – | – | 67 |
| SIM RS Panti Nugroho BBL | 14 | 7 | – | – | 1 | – | 1 | 1 | 1 | 2 | 1 | – | 1 | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 31 |
| SIM RS Panti Nugroho Diabetes Melitus | 3 | – | – | – | 1 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | 7 |
| SIM RS Panti Nugroho Hipertensi | 7 | 2 | 2 | 1 | 3 | 1 | 1 | 1 | 1 | – | – | – | 1 | – | – | – | 2 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | 23 |
| SIM RS Panti Nugroho Stroke | 5 | 2 | 2 | 1 | 3 | 1 | 1 | 1 | 1 | – | – | – | 1 | – | – | – | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | 20 |
| SIM RS Ummu Hani ANC | 11 | 1 | – | – | 3 | – | 1 | 1 | 2 | 1 | 1 | – | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 23 |
| SIM RS Ummu Hani INC | 23 | 4 | 1 | – | 2 | – | 1 | 1 | 3 | – | 2 | – | 3 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 41 |
| SIM RS Ummu Hani PNC | 28 | 5 | 1 | – | 4 | – | 1 | 1 | 2 | – | 1 | – | 2 | 1 | 3 | 2 | – | – | – | 2 | – | – | – | – | – | – | – | – | – | – | 53 |
| SIM RS Ummu Hani BBL | 13 | 7 | – | – | 1 | – | 1 | 1 | 1 | 2 | 1 | – | 1 | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 30 |
| SIM RS MPH ANC | 18 | 2 | – | – | 3 | – | 1 | 1 | 2 | 1 | 1 | – | 2 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 33 |
| SIM RS MPH INC | 24 | 4 | 1 | – | 2 | – | 1 | 1 | 2 | – | 2 | – | 2 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 40 |
| SIM RS MPH PNC | 27 | 2 | 2 | – | 4 | – | 1 | 1 | 2 | – | 1 | – | 2 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 43 |
| SIM RS MPH BBL | 25 | 4 | 1 | – | 1 | – | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 2 | – | – | – | – | – | – | – | 1 | – | – | – | – | – | – | – | – | 42 |
| SIM RS MPH Diabetes Melitus | 6 | 2 | 2 | 2 | 3 | 1 | 1 | 1 | 2 | – | – | – | 2 | – | – | – | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | 24 |
| SIM RS MPH Hipertensi | 5 | 2 | 2 | 1 | 3 | 1 | 1 | 1 | 1 | – | – | – | 1 | – | – | – | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | 20 |
| SIM RS Siaga Medika ANC | 36 | 2 | 15 | 15 | 1 | 6 | 1 | 1 | 16 | 3 | 1 | – | 1 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 100 |
| SIM RS Siaga Medika INC | 29 | 5 | – | – | 2 | – | 1 | 1 | – | – | 2 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 42 |
| SIM RS Siaga Medika PNC | 30 | 9 | – | – | 4 | – | 1 | 1 | 1 | – | 1 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 49 |
| SIM RS Siaga Medika BBL | 22 | 4 | 1 | – | 1 | – | 1 | 1 | – | 2 | 1 | 1 | – | 2 | – | – | – | – | – | – | – | 1 | – | – | – | – | – | – | – | – | 37 |
| SIM RS PKU INC | 46 | 8 | 1 | – | 5 | – | 1 | 1 | 1 | – | 2 | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 66 |
| SIM RS PKU PNC | 38 | 10 | 1 | – | 6 | – | 1 | 1 | 1 | – | 1 | – | 1 | – | 3 | 2 | – | – | – | 2 | – | – | – | – | – | – | – | – | – | – | 67 |
| SIM RS Goetoeng ANC | 3 | 97 | 1 | – | 2 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | 106 |
| SIM RS Goetoeng INC | 5 | 48 | 1 | – | 6 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | 1 | – | – | 1 | – | – | – | – | – | – | – | – | – | 64 |
| SIM RS Goetoeng PNC | 4 | – | – | – | 1 | – | 1 | 1 | – | – | – | – | 1 | – | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | 9 |
| SIM RS Goetoeng BBL | 5 | 52 | – | – | 6 | – | 1 | 1 | – | – | 1 | – | – | – | – | – | – | 1 | – | – | 1 | – | – | – | – | – | – | – | – | – | 68 |
| SIM RS Goetoeng Diabetes Melitus | 3 | – | – | – | 1 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 6 |
| SIM RS Goetoeng Hipertensi | 2 | – | – | – | 1 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 5 |
| **Total (non-unik)** | **2000** | **396** | **255** | **222** | **205** | **183** | **96** | **89** | **81** | **58** | **55** | **54** | **54** | **34** | **27** | **25** | **17** | **12** | **9** | **7** | **4** | **4** | **3** | **3** | **3** | **2** | **1** | **1** | **1** | **1** | **3902** |
| **Total unik** | **576** | **171** | **33** | **109** | **60** | **7** | **1** | **1** | **1** | **3** | **6** | **1** | **1** | **1** | **5** | **6** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **996** |

---

## Versi ASIK CKG

`PHDT_ASIK_CKG.xlsx` berisi beberapa versi dictionary untuk form CKG yang sama. **Versi terbaru** dipakai di Ringkasan dan total di atas; versi lain tetap dihitung (output per form tersedia) supaya perubahannya bisa dibandingkan, tapi **tidak masuk total** agar tidak dihitung dua kali. Sheet `CKG Lansia (tidak dipakai)`, `Pivot Table 1`, `All Variable`, `All Variable v2`, `Detail1-Lansia`, `variabel ckg dewasa`, `Hasil Check Tarikan Baru dan Lama`, `lansia` dilewati (bukan dictionary / ditandai tidak dipakai).

| Form | Versi | Sheet | Variabel unik | Payload | Code | Status |
|---|---|---|---|---|---|---|
| CKG Bayi Baru Lahir | v2 (tarikan baru) | `CKG Bayi Baru Lahir 2` | 35 (35 baris) | 25 | 41 | ✅ dipakai |
| CKG Bayi Baru Lahir | v1 | `CKG Bayi Baru Lahir` | 33 (33 baris) | 25 | 56 | tidak dihitung di total |
| CKG Balita dan Anak Pra-Sekolah | v2 (tarikan baru) | `Sheet9` | 57 (58 baris) | 32 | 102 | ✅ dipakai |
| CKG Balita dan Anak Pra-Sekolah | v1 | `CKG Balita dan Anak Pra-Sekolah` | 62 (63 baris) | 29 | 99 | tidak dihitung di total |
| CKG Dewasa Laki-laki | 1 versi | `CKG Dewasa Laki-laki` | 123 (132 baris) | 61 | 202 | ✅ dipakai |
| CKG Dewasa Perempuan | 1 versi | `CKG Dewasa Perempuan` | 130 (139 baris) | 66 | 223 | ✅ dipakai |
| CKG Lansia | 27 April 2026 (terbaru) | `CKG Lansia 27 April 2026` | 188 (204 baris) | 101 | 458 | ✅ dipakai |
| CKG Lansia | 2026 | `CKG Lansia 2026` | 188 (197 baris) | 82 | 366 | tidak dihitung di total |
| CKG Lansia | 2025 | `CKG Lansia 2025` | 186 (195 baris) | 80 | 361 | tidak dihitung di total |

Perbedaan antar versi:

- **BBL v1 → v2**: payload sama (25: Patient, Encounter, Condition, Observation 17, Procedure 5); code turun 56 → 41. Nama kolom raw pindah ke nama tarikan baru (mis. `nama_pasien` → `Nama Lengkap`, `nik` → `NIK`). Variabel 33 → 35.
- **Balita v1 → v2** (`Sheet9` = tarikan baru, contoh data `individu-bayi-2025-08.xlsx`; ini **asumsi saya** dari nama kolom raw dan sheet `Hasil Check Tarikan Baru dan Lama`, mohon dikonfirmasi): payload 29 → 32 (+3 Procedure), code 99 → 102. Variabel 62 → 57.
- **Lansia 2025 → 2026 → 27 April 2026**: payload 80 → 82 → 101, code 361 → 366 → 458. Observation 69 → 70 → 90. ⚠️ Di versi 27 April 2026 **blok lab (ServiceRequest, Specimen, DiagnosticReport, PractitionerRole) tidak ada lagi**, padahal ada di 2025 dan 2026. Sudah dikonfirmasi: **terlewat** (belum dimapping), jadi angka Lansia 27 April 2026 masih kurang blok lab.
- **Dewasa Laki-laki / Perempuan**: hanya 1 versi per form. Sheet punya kolom `Variabel v2` (nama variabel tarikan baru), tidak dijadikan versi terpisah.
- Angka variabel PHDT: BBL 33, Balita 59, Dewasa 132 / 132, Lansia 180. Selisih terhadap angka PHDT (variabel unik / baris): BBL v2 35 / 35, BBL v1 33 / 33, Balita v2 57 / 58, Dewasa Laki-laki 123 / 132, Dewasa Perempuan 130 / 139 (+7 baris), Lansia 188 / 204 (+24 baris). Angka output tetap dipakai.

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


- **ASIK CKG (5 form), Informed Consent, SiHepi Rekap 3e, eKohort ANC / INC**: dari `PHDT_ASIK_CKG.xlsx` dan 4 CSV PHDT (⚠️ belum comprehensive review, tanpa daftar BQ dan file mentah). Variabel raw = variabel unik di dictionary. Payload/code (versi yang dipakai): CKG BBL 25/41, Balita 32/102, Dewasa Laki-laki 61/202, Dewasa Perempuan 66/223, Lansia 101/458, Informed Consent 3/8, SiHepi 65/118, eKohort ANC 43/78, eKohort INC 58/74. Di form CKG, baris QuestionnaireResponse berselang-seling dengan blok Observation. Jumlah QR dihitung dari jumlah baris `QuestionnaireResponse.questionnaire`: 1 untuk BBL/Balita/Dewasa (= 1 payload), tetapi Lansia punya QR terpisah (27 April 2026 = 7, 2026 = 4, 2025 = 4). Informed Consent: kode klausul `Consent.provision.provision[n].code` (SP000840–SP000847) dihitung sebagai code (8); Consent = 1 payload. Sheet CKG Dewasa/Lansia memakai kolom `Variables` (nama variabel tarikan lama). eKohort ANC memakai `Final Format` (file `eKohort` lama berisi bagian ANC dengan 190 variabel / 140 payload / 247 code, tidak masuk total). Detail temuan: `revisi.md` (bagian CKG/IC/SiHepi/eKohort).


- **SIM RS (34 form)**: tiap sheet mapping di `PHDT_Data_Rumah_Sakit.xlsx` = 1 form di tracker (#128–#236). Sheet `Template` (ANC, INC, PNC, BBL neo, BBL INC, TB, HepB) generik, tidak dihitung di total. Beberapa hal yang perlu dicek: `Mapping PNC PKU` hasil hitungnya sama persis dengan `Mapping PNC Panti Nugroho` (67 / 131), kemungkinan salinan; `Goetoeng ANC` 106 payload dari hanya 21 variabel karena satu variabel tindakan dipetakan ke ±97 Procedure code berbeda; `Mapping INC BBL Tripat` dipakai sebagai BBL Tripat (#231). Tidak ada sheet untuk Hepatitis, TB, dan Tripat INC.

---

## Log perubahan output
- 2026-11-24 (2): Tambah 34 form SIM RS dari `PHDT_Data_Rumah_Sakit.xlsx` (ANC/INC/PNC/BBL/KIA/DM/HT/Stroke; RS Tripat, Narmada, Panti Nugroho, Ummu Hani, MPH, Siaga Medika, PKU, Goetoeng; ⚠️ belum comprehensive review). Variabel raw = variabel unik di dictionary. Sheet Template (ANC/INC/PNC/BBL/TB/HepB) dibuat dictionary-nya tapi tidak masuk total (belum terikat ke satu RS). Perbaikan QR Lansia: 1 QR per baris `QuestionnaireResponse.questionnaire` (27 Apr 2026: 7 QR, payload 101). Total non-unik lihat tabel di atas.
- 2026-11-24: Tambah 9 form: ASIK CKG BBL (v2) 25/41, Balita (v2) 32/102, Dewasa Laki-laki 61/202, Dewasa Perempuan 66/223, Lansia (27 Apr 2026) 95/458, Informed Consent 3/8, SiHepi Rekap 3e 65/118, eKohort ANC 43/78, eKohort INC 58/74 (⚠️ belum comprehensive review). Versi lain CKG (BBL v1, Balita v1, Lansia 2026/2025) dan eKohort ANC lama dihitung terpisah, tidak masuk total (bagian Versi ASIK CKG). Total non-unik **2509 payload / 6888 code** (variabel raw 3345), unik **771 / 2070** (sudah termasuk 17 form SiGizi dari commit `c4de31c`).
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
