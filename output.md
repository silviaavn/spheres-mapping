# Output Hitungan Payload & Code — Form Kobo & PHDT

Terakhir diperbarui: 2026-11-25
Aturan hitung: lihat [`aturan.md`](aturan.md) · Temuan & catatan pipeline: [`revisi.md`](revisi.md)
Form yang sudah dihitung (detail per form, bisa ditelusuri per baris):
- **Master Data (Prerequisite)** → [`output/master-data-prerequisite.md`](output/master-data-prerequisite.md) (sumber: [`mapping/phdt-data-dictionary-master-data-prerequisite.csv`](mapping/phdt-data-dictionary-master-data-prerequisite.csv); 15 kode custom SP untuk Organization.type dan PractitionerRole.code/specialty dari master SPHERES Custom Value Set; tidak ada baris tracker)
- **Maternal Outcome** → [`output/maternal-outcome.md`](output/maternal-outcome.md) (sumber: [`mapping/kobo-data-dictionary-maternal-outcome.csv`](mapping/kobo-data-dictionary-maternal-outcome.csv))
- **Raffle** → [`output/raffle.md`](output/raffle.md) (sumber: [`mapping/kobo-data-dictionary-raffle.csv`](mapping/kobo-data-dictionary-raffle.csv))
- **SiGizi ANC** → [`output/sigizi-anc.md`](output/sigizi-anc.md) (sumber: [`mapping/phdt-data-dictionary-sigizi-anc.csv`](mapping/phdt-data-dictionary-sigizi-anc.csv), PHDT Data Dictionary; struktur file mentah: [`raw/sigizi-anc-kolom.md`](raw/sigizi-anc-kolom.md))
- **SITB TB 06** → [`output/sitb-tb06.md`](output/sitb-tb06.md) (sumber: [`mapping/phdt-data-dictionary-sitb-tb06.csv`](mapping/phdt-data-dictionary-sitb-tb06.csv); file mentah: [`raw/sitb-tb06-kolom.md`](raw/sitb-tb06-kolom.md))
- **SITB TB 03 SO** → [`output/sitb-tb03-so.md`](output/sitb-tb03-so.md) (sumber: [`mapping/phdt-data-dictionary-sitb-tb03-so.csv`](mapping/phdt-data-dictionary-sitb-tb03-so.csv); file mentah: [`raw/sitb-tb03-so-kolom.md`](raw/sitb-tb03-so-kolom.md))
- **SITB TB 03 RO** → [`output/sitb-tb03-ro.md`](output/sitb-tb03-ro.md) (sumber: [`mapping/phdt-data-dictionary-sitb-tb03-ro.csv`](mapping/phdt-data-dictionary-sitb-tb03-ro.csv); file mentah: [`raw/sitb-tb03-ro-kolom.md`](raw/sitb-tb03-ro-kolom.md))
- **SITB TB 04** (Fasyankes & Rujukan) → [`output/sitb-tb04.md`](output/sitb-tb04.md) (sumber: [`mapping/phdt-data-dictionary-sitb-tb04.csv`](mapping/phdt-data-dictionary-sitb-tb04.csv); file mentah: [`raw/sitb-tb04-kolom.md`](raw/sitb-tb04-kolom.md))
- **SITB TB 16K** (revised) → [`output/sitb-tb16k.md`](output/sitb-tb16k.md) (sumber: [`mapping/phdt-data-dictionary-sitb-tb16k.csv`](mapping/phdt-data-dictionary-sitb-tb16k.csv); file mentah: [`raw/sitb-tb16k-kolom.md`](raw/sitb-tb16k-kolom.md))
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
- **SiHepi - Form Rekap 3e** → [`output/sihepi-rekap-3e.md`](output/sihepi-rekap-3e.md) (sumber: [`mapping/phdt-data-dictionary-sihepi-rekap-3e.csv`](mapping/phdt-data-dictionary-sihepi-rekap-3e.csv), ⚠️ belum comprehensive review)
- **eKohort - Pelayanan Ibu ANC** (Final Format dipakai; file eKohort lama tersedia) → [`output/ekohort-anc.md`](output/ekohort-anc.md) · [lama](output/ekohort-anc-lama.md) (sumber: [`mapping/phdt-data-dictionary-ekohort-anc.csv`](mapping/phdt-data-dictionary-ekohort-anc.csv), ⚠️ belum comprehensive review)
- **eKohort - Pelayanan Ibu Bersalin (INC)** → [`output/ekohort-inc.md`](output/ekohort-inc.md) (sumber: [`mapping/phdt-data-dictionary-ekohort-inc.csv`](mapping/phdt-data-dictionary-ekohort-inc.csv), ⚠️ belum comprehensive review)
- **Buku KIA - Identitas dan ANC** (tracker #79) → [`output/buku-kia-anc.md`](output/buku-kia-anc.md) (sumber: [`mapping/phdt-data-dictionary-buku-kia-anc.csv`](mapping/phdt-data-dictionary-buku-kia-anc.csv), file `PHDT_Buku_KIA_-_Mapping_ANC_Buku_KIA_2024.csv`, ⚠️ belum comprehensive review)
- **Buku KIA - INC** (tracker #80) → [`output/buku-kia-inc.md`](output/buku-kia-inc.md) (sumber: [`mapping/phdt-data-dictionary-buku-kia-inc.csv`](mapping/phdt-data-dictionary-buku-kia-inc.csv), file `PHDT_Buku_KIA_-_Mapping_INC_Buku_KIA_2024.csv`, ⚠️ belum comprehensive review)
- **Buku KIA - PNC** (tracker #81) → [`output/buku-kia-pnc.md`](output/buku-kia-pnc.md) (sumber: [`mapping/phdt-data-dictionary-buku-kia-pnc.csv`](mapping/phdt-data-dictionary-buku-kia-pnc.csv), file `PHDT_Buku_KIA_-_Mapping_PNC_Buku_KIA_2024.csv`, ⚠️ belum comprehensive review)
- **Buku KIA - Anak** (tracker #82) → [`output/buku-kia-anak.md`](output/buku-kia-anak.md) (sumber: [`mapping/phdt-data-dictionary-buku-kia-anak.csv`](mapping/phdt-data-dictionary-buku-kia-anak.csv), file `PHDT_Buku_KIA_-_Mapping_Anak_Usia_0-6_Tahun_Buku_KIA_2024.csv`, ⚠️ belum comprehensive review)
- **SITB - TB 15 (Pemeriksaan Eligibilitas TPT)** (tracker #60) → [`output/sitb-tb15.md`](output/sitb-tb15.md) (sumber: [`mapping/phdt-data-dictionary-sitb-tb15.csv`](mapping/phdt-data-dictionary-sitb-tb15.csv), PHDT_SITB_-_TB_15.csv, ⚠️ belum comprehensive review)
- **SITB - TB 15P (Penerima TPT)** (tracker #61) → [`output/sitb-tb15p.md`](output/sitb-tb15p.md) (sumber: [`mapping/phdt-data-dictionary-sitb-tb15p.csv`](mapping/phdt-data-dictionary-sitb-tb15p.csv), PHDT_SITB_-_TB_15P.csv, ⚠️ belum comprehensive review)
- **ASIK - Data Individu Kohort Bayi (Imunisasi)** (tracker #39) → [`output/asik-kohort-bayi.md`](output/asik-kohort-bayi.md) (sumber: [`mapping/phdt-data-dictionary-asik-kohort-bayi.csv`](mapping/phdt-data-dictionary-asik-kohort-bayi.csv), PHDT_Data_Dictionary_-_ASIK.csv (baris 117–711), ⚠️ belum comprehensive review)
- **ASIK - Data Individu Kohort Baduta (Imunisasi)** (tracker #40) → [`output/asik-kohort-baduta.md`](output/asik-kohort-baduta.md) (sumber: [`mapping/phdt-data-dictionary-asik-kohort-baduta.csv`](mapping/phdt-data-dictionary-asik-kohort-baduta.csv), PHDT_Data_Dictionary_-_ASIK.csv (baris 2–116), ⚠️ belum comprehensive review)
- **ASIK - Data Individu Kohort WUS (Imunisasi)** (tracker #41) → [`output/asik-kohort-wus.md`](output/asik-kohort-wus.md) (sumber: [`mapping/phdt-data-dictionary-asik-kohort-wus.csv`](mapping/phdt-data-dictionary-asik-kohort-wus.csv), PHDT_Data_Dictionary_-_ASIK.csv (baris 712–akhir), ⚠️ belum comprehensive review)
- **KuApps BidanKu - ANC** (tracker #106) → [`output/kuapps-bidanku-anc.md`](output/kuapps-bidanku-anc.md) (sumber: [`mapping/phdt-data-dictionary-kuapps-bidanku-anc.csv`](mapping/phdt-data-dictionary-kuapps-bidanku-anc.csv), sheet `PYD-ANC`, ⚠️ belum comprehensive review)
- **KuApps BidanKu - PNC** (tracker #107) → [`output/kuapps-bidanku-pnc.md`](output/kuapps-bidanku-pnc.md) (sumber: [`mapping/phdt-data-dictionary-kuapps-bidanku-pnc.csv`](mapping/phdt-data-dictionary-kuapps-bidanku-pnc.csv), sheet `PYD-PNC`, ⚠️ belum comprehensive review)
- **KuApps BidanKu - BBL** (tracker #108) → [`output/kuapps-bidanku-bbl.md`](output/kuapps-bidanku-bbl.md) (sumber: [`mapping/phdt-data-dictionary-kuapps-bidanku-bbl.csv`](mapping/phdt-data-dictionary-kuapps-bidanku-bbl.csv), sheet `PYD-BBL`, ⚠️ belum comprehensive review)
- **KuApps BidanKu - Bayi** (tracker #109) → [`output/kuapps-bidanku-bayi.md`](output/kuapps-bidanku-bayi.md) (sumber: [`mapping/phdt-data-dictionary-kuapps-bidanku-bayi.csv`](mapping/phdt-data-dictionary-kuapps-bidanku-bayi.csv), sheet `PYD-Bayi`, ⚠️ belum comprehensive review)
- **KuApps BidanKu - Anak** (tracker #110) → [`output/kuapps-bidanku-anak.md`](output/kuapps-bidanku-anak.md) (sumber: [`mapping/phdt-data-dictionary-kuapps-bidanku-anak.csv`](mapping/phdt-data-dictionary-kuapps-bidanku-anak.csv), sheet `PYD-Anak`, ⚠️ belum comprehensive review)
- **KuApps BidanKu - Anak Usia Sekolah dan Remaja** (tracker #111) → [`output/kuapps-bidanku-usekre.md`](output/kuapps-bidanku-usekre.md) (sumber: [`mapping/phdt-data-dictionary-kuapps-bidanku-usekre.csv`](mapping/phdt-data-dictionary-kuapps-bidanku-usekre.csv), sheet `PYD-Anak Usekre (6-18 tahun)`, ⚠️ belum comprehensive review)
- **KuApps BidanKu - Dewasa** (tracker #112) → [`output/kuapps-bidanku-dewasa.md`](output/kuapps-bidanku-dewasa.md) (sumber: [`mapping/phdt-data-dictionary-kuapps-bidanku-dewasa.csv`](mapping/phdt-data-dictionary-kuapps-bidanku-dewasa.csv), sheet `PYD Dewasa`, ⚠️ belum comprehensive review)
- **KuApps BidanKu - Lansia** (tracker #113) → [`output/kuapps-bidanku-lansia.md`](output/kuapps-bidanku-lansia.md) (sumber: [`mapping/phdt-data-dictionary-kuapps-bidanku-lansia.csv`](mapping/phdt-data-dictionary-kuapps-bidanku-lansia.csv), sheet `PYD Lansia`, ⚠️ belum comprehensive review)
- **Kuapps Spheres - HT** (tracker #114) → [`output/kuapps-spheres-ht.md`](output/kuapps-spheres-ht.md) (sumber: [`mapping/phdt-data-dictionary-kuapps-spheres-ht.csv`](mapping/phdt-data-dictionary-kuapps-spheres-ht.csv), sheet `Form Caregap HT`, ⚠️ belum comprehensive review)
- **Kuapps Spheres - DM** (tracker #115) → [`output/kuapps-spheres-dm.md`](output/kuapps-spheres-dm.md) (sumber: [`mapping/phdt-data-dictionary-kuapps-spheres-dm.csv`](mapping/phdt-data-dictionary-kuapps-spheres-dm.csv), sheet `Form Caregap DM`, ⚠️ belum comprehensive review)
- **Kuapps Spheres - TB** (tracker #116) → [`output/kuapps-spheres-tb.md`](output/kuapps-spheres-tb.md) (sumber: [`mapping/phdt-data-dictionary-kuapps-spheres-tb.csv`](mapping/phdt-data-dictionary-kuapps-spheres-tb.csv), sheet `Form Caregap TB`, ⚠️ belum comprehensive review)
- **Genomics - TB** (tracker #118) → [`output/genomics-tb.md`](output/genomics-tb.md) (sumber: [`mapping/phdt-data-dictionary-genomics-tb.csv`](mapping/phdt-data-dictionary-genomics-tb.csv), sheet `TB Mapping`, ⚠️ belum comprehensive review)
- **Genomics - Klebsiella** (tracker #119) → [`output/genomics-klebsiella.md`](output/genomics-klebsiella.md) (sumber: [`mapping/phdt-data-dictionary-genomics-klebsiella.csv`](mapping/phdt-data-dictionary-genomics-klebsiella.csv), sheet `Klebsiella Mapping`, ⚠️ belum comprehensive review)
- **Genomics - Dengue** (tracker #120) → [`output/genomics-dengue.md`](output/genomics-dengue.md) (sumber: [`mapping/phdt-data-dictionary-genomics-dengue.csv`](mapping/phdt-data-dictionary-genomics-dengue.csv), sheet `Dengue Mapping`, ⚠️ belum comprehensive review)
- **KuApps BidanKu - Tambah Pasien** (tracker #284) → [`output/kuapps-bidanku-tambah-pasien.md`](output/kuapps-bidanku-tambah-pasien.md) (sumber: [`mapping/phdt-data-dictionary-kuapps-bidanku-tambah-pasien.csv`](mapping/phdt-data-dictionary-kuapps-bidanku-tambah-pasien.csv), sheet `Tambah Pasien`, ⚠️ belum comprehensive review)
- **KuApps BidanKu - Daftar Kehamilan** (tracker #285) → [`output/kuapps-bidanku-daftar-kehamilan.md`](output/kuapps-bidanku-daftar-kehamilan.md) (sumber: [`mapping/phdt-data-dictionary-kuapps-bidanku-daftar-kehamilan.csv`](mapping/phdt-data-dictionary-kuapps-bidanku-daftar-kehamilan.csv), sheet `Daftar Kehamilan`, ⚠️ belum comprehensive review)
- **KuApps BidanKu - Luaran Kehamilan** (tracker #286) → [`output/kuapps-bidanku-luaran-kehamilan.md`](output/kuapps-bidanku-luaran-kehamilan.md) (sumber: [`mapping/phdt-data-dictionary-kuapps-bidanku-luaran-kehamilan.csv`](mapping/phdt-data-dictionary-kuapps-bidanku-luaran-kehamilan.csv), sheet `Luaran Kehamilan`, ⚠️ belum comprehensive review)
- **KuApps BidanKu - PHBS** (tracker #287) → [`output/kuapps-bidanku-phbs.md`](output/kuapps-bidanku-phbs.md) (sumber: [`mapping/phdt-data-dictionary-kuapps-bidanku-phbs.csv`](mapping/phdt-data-dictionary-kuapps-bidanku-phbs.csv), sheet `PHBS`, ⚠️ belum comprehensive review)
- **KuApps BidanKu - Skrining Rumah Tangga** (tracker #288) → [`output/kuapps-bidanku-skrining-rt.md`](output/kuapps-bidanku-skrining-rt.md) (sumber: [`mapping/phdt-data-dictionary-kuapps-bidanku-skrining-rt.csv`](mapping/phdt-data-dictionary-kuapps-bidanku-skrining-rt.csv), sheet `Skrining Rumah Tangga`, ⚠️ belum comprehensive review)
- **KuApps BidanKu - Imunisasi** (tracker #289) → [`output/kuapps-bidanku-imunisasi.md`](output/kuapps-bidanku-imunisasi.md) (sumber: [`mapping/phdt-data-dictionary-kuapps-bidanku-imunisasi.csv`](mapping/phdt-data-dictionary-kuapps-bidanku-imunisasi.csv), sheet `Imunisasi`, ⚠️ belum comprehensive review)
- **KuApps BidanKu - Kumpulan Skrinning** (tracker #290) → [`output/kuapps-bidanku-kumpulan-skrining.md`](output/kuapps-bidanku-kumpulan-skrining.md) (sumber: [`mapping/phdt-data-dictionary-kuapps-bidanku-kumpulan-skrining.csv`](mapping/phdt-data-dictionary-kuapps-bidanku-kumpulan-skrining.csv), sheet `Kumpulan Skrinning`, ⚠️ belum comprehensive review)
- **Kobo SDIDTK** (tracker #103) → [`output/kobo-sdidtk.md`](output/kobo-sdidtk.md) (sumber: [`mapping/phdt-data-dictionary-kobo-sdidtk.csv`](mapping/phdt-data-dictionary-kobo-sdidtk.csv), ⚠️ belum comprehensive review)
- **MMS - Pemantauan Distribusi dan Konsumsi** (tracker #291) → [`output/mms-distribusi-konsumsi.md`](output/mms-distribusi-konsumsi.md) (sumber: [`mapping/phdt-data-dictionary-mms-distribusi-konsumsi.csv`](mapping/phdt-data-dictionary-mms-distribusi-konsumsi.csv), ⚠️ belum comprehensive review)
- **MMS - Informed Consent** (tracker #292) → [`output/mms-informed-consent.md`](output/mms-informed-consent.md) (sumber: [`mapping/phdt-data-dictionary-mms-informed-consent.csv`](mapping/phdt-data-dictionary-mms-informed-consent.csv), ⚠️ belum comprehensive review)
- **MMS - Master Database Responden** (tracker #293) → [`output/mms-master-responden.md`](output/mms-master-responden.md) (sumber: [`mapping/phdt-data-dictionary-mms-master-responden.csv`](mapping/phdt-data-dictionary-mms-master-responden.csv), ⚠️ belum comprehensive review)
- **MMS - Survei Sosio Ekonomi** (tracker #294) → [`output/mms-sosio-ekonomi.md`](output/mms-sosio-ekonomi.md) (sumber: [`mapping/phdt-data-dictionary-mms-sosio-ekonomi.csv`](mapping/phdt-data-dictionary-mms-sosio-ekonomi.csv), ⚠️ belum comprehensive review)
- **MMS - Survei Demografi (Listing Responden)** (tracker #295) → [`output/mms-demografi.md`](output/mms-demografi.md) (sumber: [`mapping/phdt-data-dictionary-mms-demografi.csv`](mapping/phdt-data-dictionary-mms-demografi.csv), ⚠️ belum comprehensive review)
- **MMS - Konfirmasi Kelahiran dan Luaran Kehamilan** (tracker #296) → [`output/mms-konfirmasi-kelahiran.md`](output/mms-konfirmasi-kelahiran.md) (sumber: [`mapping/phdt-data-dictionary-mms-konfirmasi-kelahiran.csv`](mapping/phdt-data-dictionary-mms-konfirmasi-kelahiran.csv), ⚠️ belum comprehensive review)
- **SKI - Sahabat Sehat Household Survey** (tracker #297) → [`output/ski-household-survey.md`](output/ski-household-survey.md) (sumber: [`mapping/phdt-data-dictionary-ski-household-survey.csv`](mapping/phdt-data-dictionary-ski-household-survey.csv), sheet `Sahabat Sehat Household Survey` di `PHDT_Data_SKI.xlsx`, ⚠️ belum comprehensive review)
- **SKI - Individu Bagian B (Penyakit)** (tracker #298) → [`output/ski-individu-penyakit.md`](output/ski-individu-penyakit.md) (sumber: [`mapping/phdt-data-dictionary-ski-individu-penyakit.csv`](mapping/phdt-data-dictionary-ski-individu-penyakit.csv), sheet `FIX_SKI Individu_Bagian B`, ⚠️ belum comprehensive review)
- **SKI - Kesehatan Bayi Balita** (tracker #299) → [`output/ski-bayi-balita.md`](output/ski-bayi-balita.md) (sumber: [`mapping/phdt-data-dictionary-ski-bayi-balita.csv`](mapping/phdt-data-dictionary-ski-bayi-balita.csv), sheet `Kesehatan Bayi Balita`, ⚠️ belum comprehensive review)
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
- **SIM RS - Harapan Ibu ANC** (tracker #137, memakai template Spheres `template-anc`) → [`output/rs-harapan-ibu-anc.md`](output/rs-harapan-ibu-anc.md) (⚠️ belum comprehensive review)
- **SIM RS - Harapan Ibu INC** (tracker #138, memakai template Spheres `template-inc`) → [`output/rs-harapan-ibu-inc.md`](output/rs-harapan-ibu-inc.md) (⚠️ belum comprehensive review)
- **SIM RS - Harapan Ibu PNC** (tracker #139, memakai template Spheres `template-pnc`) → [`output/rs-harapan-ibu-pnc.md`](output/rs-harapan-ibu-pnc.md) (⚠️ belum comprehensive review)
- **SIM RS - Harapan Ibu BBL** (tracker #140, memakai template Spheres `template-bbl-neo`) → [`output/rs-harapan-ibu-bbl.md`](output/rs-harapan-ibu-bbl.md) (⚠️ belum comprehensive review)
- **SIM RS - At tin ANC** (tracker #128, memakai template Spheres `template-anc`) → [`output/rs-attin-anc.md`](output/rs-attin-anc.md) (⚠️ belum comprehensive review)
- **SIM RS - At tin INC** (tracker #129, memakai template Spheres `template-inc`) → [`output/rs-attin-inc.md`](output/rs-attin-inc.md) (⚠️ belum comprehensive review)
- **SIM RS - At tin PNC** (tracker #130, memakai template Spheres `template-pnc`) → [`output/rs-attin-pnc.md`](output/rs-attin-pnc.md) (⚠️ belum comprehensive review)
- **SIM RS - At tin BBL** (tracker #131, memakai template Spheres `template-bbl-inc`) → [`output/rs-attin-bbl.md`](output/rs-attin-bbl.md) (⚠️ belum comprehensive review)
- **SIM RS - Nirmala ANC** (tracker #164, memakai template Spheres `template-anc`) → [`output/rs-nirmala-anc.md`](output/rs-nirmala-anc.md) (⚠️ belum comprehensive review)
- **SIM RS - Nirmala INC** (tracker #165, memakai template Spheres `template-inc`) → [`output/rs-nirmala-inc.md`](output/rs-nirmala-inc.md) (⚠️ belum comprehensive review)
- **SIM RS - Nirmala PNC** (tracker #166, memakai template Spheres `template-pnc`) → [`output/rs-nirmala-pnc.md`](output/rs-nirmala-pnc.md) (⚠️ belum comprehensive review)
- **SIM RS - Nirmala BBL** (tracker #167, memakai template Spheres `template-bbl-inc`) → [`output/rs-nirmala-bbl.md`](output/rs-nirmala-bbl.md) (⚠️ belum comprehensive review)
- **SIM RS - PKU ANC** (tracker #182, memakai template Spheres `template-anc`) → [`output/rs-pku-anc.md`](output/rs-pku-anc.md) (⚠️ belum comprehensive review)
- **SIM RS - PKU BBL** (tracker #185, memakai template Spheres `template-bbl-inc`) → [`output/rs-pku-bbl.md`](output/rs-pku-bbl.md) (⚠️ belum comprehensive review)
- **SIM RS - MPH Hepatitis** (tracker #159, memakai template Spheres `template-hepb`) → [`output/rs-mph-hepatitis.md`](output/rs-mph-hepatitis.md) (⚠️ belum comprehensive review)
- **SIM RS - Ummu Hani Hepatitis** (tracker #177, memakai template Spheres `template-hepb`) → [`output/rs-ummu-hani-hepatitis.md`](output/rs-ummu-hani-hepatitis.md) (⚠️ belum comprehensive review)
- **SIM RS - PKU Hepatitis** (tracker #186, memakai template Spheres `template-hepb`) → [`output/rs-pku-hepatitis.md`](output/rs-pku-hepatitis.md) (⚠️ belum comprehensive review)
- **SIM RS - Siaga Medika Hepatitis** (tracker #150, memakai template Spheres `template-hepb`) → [`output/rs-siaga-medika-hepatitis.md`](output/rs-siaga-medika-hepatitis.md) (⚠️ belum comprehensive review)
- **Kobo Modul ANC** (tracker #83) → [`output/kobo-modul-anc.md`](output/kobo-modul-anc.md) (sumber: [`mapping/phdt-data-dictionary-kobo-modul-anc.csv`](mapping/phdt-data-dictionary-kobo-modul-anc.csv), sheet `ANC Kobo` di `Kobo_-_Data_Dictionary.xlsx`, ⚠️ belum comprehensive review)
- **Kobo Modul INC** (tracker #84) → [`output/kobo-modul-inc.md`](output/kobo-modul-inc.md) (sumber: [`mapping/phdt-data-dictionary-kobo-modul-inc.csv`](mapping/phdt-data-dictionary-kobo-modul-inc.csv), sheet `INC Kobo` di `Kobo_-_Data_Dictionary.xlsx`, ⚠️ belum comprehensive review)
- **Kobo Modul Neonatus** (tracker #85) → [`output/kobo-modul-neonatus.md`](output/kobo-modul-neonatus.md) (sumber: [`mapping/phdt-data-dictionary-kobo-modul-neonatus.csv`](mapping/phdt-data-dictionary-kobo-modul-neonatus.csv), sheet `Neonatus Kobo` di `Kobo_-_Data_Dictionary.xlsx`, ⚠️ belum comprehensive review)
- **Kobo Modul PNC** (tracker #86) → [`output/kobo-modul-pnc.md`](output/kobo-modul-pnc.md) (sumber: [`mapping/phdt-data-dictionary-kobo-modul-pnc.csv`](mapping/phdt-data-dictionary-kobo-modul-pnc.csv), sheet `PNC Kobo` di `Kobo_-_Data_Dictionary.xlsx`, ⚠️ belum comprehensive review)
- **Kobo Buku KIA 1 - ANC** (tracker #88) → [`output/kobo-kia1-anc.md`](output/kobo-kia1-anc.md) (sumber: [`mapping/phdt-data-dictionary-kobo-kia1-anc.csv`](mapping/phdt-data-dictionary-kobo-kia1-anc.csv), sheet `Mapping Kobo Buku KIA 1 - ANC (` di `Kobo_-_Data_Dictionary.xlsx`, ⚠️ belum comprehensive review)
- **Kobo Buku KIA 2 - Luaran Kehamilan** (tracker #89) → [`output/kobo-kia2-luaran.md`](output/kobo-kia2-luaran.md) (sumber: [`mapping/phdt-data-dictionary-kobo-kia2-luaran.csv`](mapping/phdt-data-dictionary-kobo-kia2-luaran.csv), sheet `Mapping Variable Buku KIA Entry` di `Kobo_-_Data_Dictionary.xlsx`, ⚠️ belum comprehensive review)
- **Kobo Buku KIA 3 - PNC** (tracker #90) → [`output/kobo-kia3-pnc.md`](output/kobo-kia3-pnc.md) (sumber: [`mapping/phdt-data-dictionary-kobo-kia3-pnc.csv`](mapping/phdt-data-dictionary-kobo-kia3-pnc.csv), sheet `Mapping Kobo Buku KIA 3 - PNC` di `Kobo_-_Data_Dictionary.xlsx`, ⚠️ belum comprehensive review)
- **Kobo Buku KIA 4 - Cadre** (tracker #91) → [`output/kobo-kia4-cadre.md`](output/kobo-kia4-cadre.md) (sumber: [`mapping/phdt-data-dictionary-kobo-kia4-cadre.csv`](mapping/phdt-data-dictionary-kobo-kia4-cadre.csv), sheet `Mapping Variabel Kobo Buku KIA` di `Kobo_-_Data_Dictionary.xlsx`, ⚠️ belum comprehensive review)
- **Kobo Buku KIA 5 - Vaksinatorku** (tracker #92) → [`output/kobo-kia5-vaksinator.md`](output/kobo-kia5-vaksinator.md) (sumber: [`mapping/phdt-data-dictionary-kobo-kia5-vaksinator.csv`](mapping/phdt-data-dictionary-kobo-kia5-vaksinator.csv), sheet `Mapping Kobo Vaksinator (revise` di `Kobo_-_Data_Dictionary.xlsx`, ⚠️ belum comprehensive review)
- **Kobo Neonatus Outcome** (tracker #93) → [`output/kobo-neonatus-outcome.md`](output/kobo-neonatus-outcome.md) (sumber: [`mapping/phdt-data-dictionary-kobo-neonatus-outcome.csv`](mapping/phdt-data-dictionary-kobo-neonatus-outcome.csv), sheet `Neonatal Outcome Kobo` di `Kobo_-_Data_Dictionary.xlsx`, ⚠️ belum comprehensive review)
- **Kobo Neonatus Outcome v2** (tracker #94) → [`output/kobo-neonatus-outcome-v2.md`](output/kobo-neonatus-outcome-v2.md) (sumber: [`mapping/phdt-data-dictionary-kobo-neonatus-outcome-v2.csv`](mapping/phdt-data-dictionary-kobo-neonatus-outcome-v2.csv), sheet `Neonatal Outcome v2` di `Kobo_-_Data_Dictionary.xlsx`, ⚠️ belum comprehensive review)
- **Kobo DDTK** (tracker #101) → [`output/kobo-ddtk.md`](output/kobo-ddtk.md) (sumber: [`mapping/phdt-data-dictionary-kobo-ddtk.csv`](mapping/phdt-data-dictionary-kobo-ddtk.csv), sheet `DDTK Kobo` di `Kobo_-_Data_Dictionary.xlsx`, ⚠️ belum comprehensive review)
- **Kobo Data BBL** (tidak ada baris tracker, tidak masuk total) → [`output/kobo-data-bbl.md`](output/kobo-data-bbl.md) (38 payload / 124 code)
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
- **SISMAL Regmal 1** → [`output/sismal-regmal1.md`](output/sismal-regmal1.md) (sumber: [`mapping/phdt-data-dictionary-sismal-regmal1.csv`](mapping/phdt-data-dictionary-sismal-regmal1.csv), sheet `Mapping Regmal 1` di `PHDT_SISMAL.xlsx`; ⚠️ **belum comprehensive review**, belum ada file mentah dan daftar variabel BQ)
- **SISMAL Validasi Kasus Indigenous** → [`output/sismal-validasi-indigenous.md`](output/sismal-validasi-indigenous.md) (sumber: [`mapping/phdt-data-dictionary-sismal-validasi-indigenous.csv`](mapping/phdt-data-dictionary-sismal-validasi-indigenous.csv), sheet `Mapping Indigeneous`; ⚠️ **belum comprehensive review**)

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

Baris **ePus ...** = 11 form ePuskesmas dari `PHDT_ePus.xlsx` (⚠️ belum comprehensive review). Kolom **Variabel raw** = jumlah kolom di file mentah (kalau belum ada file mentah: jumlah variabel di dictionary; Maternal Outcome & Raffle = variabel Kobo, MPDN = variabel dictionary tanpa placeholder). Kolom **Code SP** = jumlah code dengan CodeSystem `http://terminology.kemkes.go.id/sp` atau `http://terminology.kemkes.go.id/sp`, `.../CodeSystem/organization-type/sp` (6 kode master PAUD), atau `.../CodeSystem/organization-ownership` (kepemilikan faskes; bukan sistem SatuSehat, tapi tetap dihitung custom SP); semuanya kode custom SP dan sudah termasuk di kolom Code.

| Form | Variabel raw | Payload | Code | Code SP |
|---|---|---|---|---|
| Maternal Outcome | 12 | 12 | 14 | 4 |
| Raffle | 12 | 8 | 6 | 4 |
| SiGizi ANC | 49 | 61 | 154 | 18 |
| SITB TB 06 | 96 | 56 | 301 | 11 |
| SITB TB 03 SO | 84 | 62 | 358 | 12 |
| SITB TB 03 RO | 144 | 50 | 403 | 13 |
| SITB TB 04 | 114 | 69 | 616 | 24 |
| SITB TB 16K | 40 | 24 | 38 | 15 |
| MPDN Kematian Bayi | 37 | 19 | 115 | 37 |
| MPDN Kematian Ibu | 24 | 10 | 50 | 17 |
| ePus Pelayanan Pasien | 81 | 47 | 62 | 2 |
| ePus Kunjungan Ibu Hamil | 68 | 114 | 206 | 11 |
| ePus Laboratorium | 22 | 309 | 500 | 0 |
| ePus Rujukan Eksternal | 23 | 5 | 0 | 0 |
| ePus ANC | 123 | 155 | 346 | 25 |
| ePus INC | 93 | 69 | 210 | 25 |
| ePus PNC | 107 | 82 | 166 | 29 |
| ePus MTBS | 187 | 125 | 285 | 20 |
| ePus MTBM | 105 | 57 | 139 | 20 |
| ePus Tumbang Anak | 34 | 19 | 62 | 8 |
| ePus Tumbang DDTK | 38 | 29 | 92 | 10 |
| ePus Tumbang KPSP | 123 | 14 | 0 | 0 |
| ePus Tumbang TDD | 37 | 8 | 0 | 0 |
| ePus Tumbang TDL | 6 | 4 | 8 | 0 |
| ePus Tumbang KMPE | 14 | 1 | 0 | 0 |
| ePus Tumbang M-CHAT-R | 20 | 1 | 0 | 0 |
| Dapodik PAUD | 75 | 42 | 378 | 161 |
| ePus Tumbang GPPH | 10 | 1 | 40 | 20 |
| SITB TB 01 | 82 | 37 | 101 | 15 |
| SITB TB 02 | 22 | 13 | 15 | 0 |
| ELSMIL Ibu Hamil | 36 | 36 | 105 | 33 |
| ELSMIL Pasca Persalinan | 29 | 24 | 102 | 35 |
| ELSMIL Baduta | 38 | 31 | 84 | 29 |
| SIPTM | 60 | 52 | 214 | 7 |
| ASIK Skrining PTM | 67 | 104 | 215 | 19 |
| ASIK CKG Bayi Baru Lahir (v2) | 35 | 25 | 41 | 1 |
| ASIK CKG Balita (v2) | 57 | 32 | 102 | 10 |
| ASIK CKG Dewasa Laki-laki | 123 | 61 | 278 | 9 |
| ASIK CKG Dewasa Perempuan | 130 | 66 | 299 | 9 |
| ASIK CKG Lansia (27 Apr 2026) | 188 | 101 | 567 | 18 |
| SIHEPI Rekap 3e | 93 | 65 | 118 | 49 |
| eKohort ANC | 34 | 43 | 78 | 0 |
| eKohort INC | 84 | 58 | 82 | 0 |
| Buku KIA Identitas dan ANC | 235 | 206 | 438 | 44 |
| Buku KIA INC | 79 | 60 | 108 | 4 |
| Buku KIA PNC | 26 | 14 | 32 | 3 |
| Buku KIA Anak | 266 | 189 | 288 | 8 |
| SITB TB 15 | 28 | 13 | 113 | 3 |
| SITB TB 15P | 32 | 21 | 59 | 15 |
| ASIK Kohort Bayi | 123 | 19 | 27 | 0 |
| ASIK Kohort Baduta | 27 | 4 | 6 | 0 |
| ASIK Kohort WUS | 37 | 12 | 20 | 0 |
| KuApps BidanKu ANC | 244 | 190 | 440 | 93 |
| KuApps BidanKu PNC | 52 | 49 | 143 | 2 |
| KuApps BidanKu BBL | 62 | 48 | 103 | 4 |
| KuApps BidanKu Bayi | 197 | 101 | 242 | 17 |
| KuApps BidanKu Anak | 199 | 81 | 157 | 9 |
| KuApps BidanKu Anak Usia Sekolah dan Remaja | 47 | 31 | 83 | 2 |
| KuApps BidanKu Dewasa | 72 | 39 | 122 | 25 |
| KuApps BidanKu Lansia | 84 | 29 | 121 | 11 |
| Kuapps Spheres HT | 132 | 10 | 243 | 231 |
| Kuapps Spheres DM | 133 | 10 | 245 | 233 |
| Kuapps Spheres TB | 25 | 5 | 49 | 21 |
| Genomics TB | 34 | 8 | 43 | 4 |
| Genomics Klebsiella | 33 | 10 | 31 | 9 |
| Genomics Dengue | 30 | 12 | 22 | 5 |
| KuApps BidanKu Tambah Pasien | 41 | 11 | 33 | 11 |
| KuApps BidanKu Daftar Kehamilan | 14 | 12 | 32 | 6 |
| KuApps BidanKu Luaran Kehamilan | 43 | 31 | 156 | 7 |
| KuApps BidanKu PHBS | 4 | 1 | 3 | 3 |
| KuApps BidanKu Skrining Rumah Tangga | 13 | 2 | 9 | 9 |
| KuApps BidanKu Imunisasi | 24 | 23 | 52 | 0 |
| KuApps BidanKu Kumpulan Skrinning | 81 | 23 | 30 | 15 |
| Kobo SDIDTK | 38 | 35 | 92 | 10 |
| MMS - Pemantauan Distribusi dan Konsumsi | 95 | 22 | 58 | 30 |
| MMS - Informed Consent | 35 | 8 | 7 | 2 |
| MMS - Master Database Responden | 38 | 16 | 48 | 21 |
| MMS - Survei Sosio Ekonomi | 101 | 22 | 229 | 147 |
| MMS - Survei Demografi (Listing Responden) | 30 | 12 | 20 | 14 |
| MMS - Konfirmasi Kelahiran dan Luaran Kehamilan | 72 | 50 | 193 | 18 |
| SKI - Sahabat Sehat Household Survey | 58 | 14 | 102 | 44 |
| SKI - Individu Bagian B (Penyakit) | 55 | 12 | 62 | 31 |
| SKI - Kesehatan Bayi Balita | 70 | 5 | 4 | 4 |
| SiGizi Balita BNBA | 33 | 24 | 50 | 10 |
| SiGizi Balita Vitamin A | 14 | 22 | 51 | 9 |
| SiGizi Balita Mendapat PMT 2024 | 30 | 15 | 45 | 14 |
| SiGizi Balita Pemantauan PMT 2024 | 18 | 9 | 15 | 5 |
| SiGizi Balita ASI Eksklusif | 22 | 11 | 36 | 28 |
| SiGizi Balita MPASI | 28 | 9 | 32 | 2 |
| SiGizi PMT 2025 BB Tidak Naik - Pantau | 24 | 15 | 33 | 17 |
| SiGizi PMT 2025 BB Tidak Naik - Riwayat | 34 | 19 | 75 | 23 |
| SiGizi PMT 2025 BB Tidak Naik - Survey | 20 | 5 | 16 | 4 |
| SiGizi PMT 2025 BB Kurang - Pantau | 24 | 21 | 47 | 21 |
| SiGizi PMT 2025 BB Kurang - Riwayat | 34 | 19 | 75 | 23 |
| SiGizi PMT 2025 BB Kurang - Survey | 20 | 5 | 16 | 4 |
| SiGizi PMT 2025 Gizi Kurang - Pantau | 51 | 42 | 102 | 29 |
| SiGizi PMT 2025 Gizi Kurang - Riwayat | 34 | 19 | 75 | 23 |
| SiGizi PMT 2025 Gizi Kurang - Survey | 20 | 5 | 16 | 4 |
| SiGizi Ibu Nifas | 14 | 11 | 12 | 3 |
| SiGizi Kohort Ibu | 42 | 63 | 109 | 3 |
| SIM RS Tripat ANC | 31 | 20 | 28 | 0 |
| SIM RS Tripat BBL (sheet 'INC BBL') | 36 | 23 | 20 | 0 |
| SIM RS Tripat PNC | 36 | 24 | 28 | 0 |
| SIM RS Narmada INC | 225 | 86 | 264 | 2 |
| SIM RS Narmada KIA | 70 | 50 | 110 | 2 |
| SIM RS Panti Nugroho ANC | 43 | 31 | 77 | 11 |
| SIM RS Panti Nugroho INC | 55 | 37 | 121 | 11 |
| SIM RS Panti Nugroho PNC | 85 | 67 | 133 | 22 |
| SIM RS Panti Nugroho BBL | 49 | 31 | 55 | 2 |
| SIM RS Panti Nugroho Diabetes Melitus | 19 | 7 | 4 | 0 |
| SIM RS Panti Nugroho Hipertensi | 40 | 23 | 21 | 4 |
| SIM RS Panti Nugroho Stroke | 35 | 20 | 23 | 4 |
| SIM RS Ummu Hani ANC | 33 | 23 | 49 | 2 |
| SIM RS Ummu Hani INC | 54 | 41 | 97 | 9 |
| SIM RS Ummu Hani PNC | 65 | 53 | 112 | 8 |
| SIM RS Ummu Hani BBL | 45 | 30 | 55 | 2 |
| SIM RS MPH ANC | 43 | 33 | 90 | 11 |
| SIM RS MPH INC | 54 | 40 | 94 | 9 |
| SIM RS MPH PNC | 59 | 43 | 104 | 6 |
| SIM RS MPH BBL | 73 | 42 | 59 | 2 |
| SIM RS MPH Diabetes Melitus | 44 | 24 | 37 | 3 |
| SIM RS MPH Hipertensi | 35 | 20 | 22 | 3 |
| SIM RS Siaga Medika ANC | 61 | 100 | 193 | 12 |
| SIM RS Siaga Medika INC | 58 | 42 | 125 | 13 |
| SIM RS Siaga Medika PNC | 71 | 49 | 110 | 15 |
| SIM RS Siaga Medika BBL | 64 | 37 | 48 | 2 |
| SIM RS PKU INC | 81 | 66 | 179 | 19 |
| SIM RS PKU PNC | 85 | 67 | 133 | 22 |
| SIM RS Goetoeng ANC | 21 | 106 | 111 | 22 |
| SIM RS Goetoeng INC | 35 | 64 | 245 | 12 |
| SIM RS Goetoeng PNC | 27 | 9 | 21 | 11 |
| SIM RS Goetoeng BBL | 34 | 68 | 124 | 14 |
| SIM RS Goetoeng Diabetes Melitus | 12 | 6 | 4 | 0 |
| SIM RS Goetoeng Hipertensi | 13 | 5 | 3 | 0 |
| SISMAL Regmal 1 | 49 | 20 | 54 | 15 |
| SISMAL Validasi Indigenous | 14 | 7 | 13 | 7 |
| SIM RS Harapan Ibu ANC | 76 | 89 | 194 | 21 |
| SIM RS Harapan Ibu INC | 81 | 67 | 164 | 19 |
| SIM RS Harapan Ibu PNC | 86 | 67 | 147 | 22 |
| SIM RS Harapan Ibu BBL | 105 | 79 | 114 | 2 |
| SIM RS At tin ANC | 76 | 89 | 194 | 21 |
| SIM RS At tin INC | 81 | 67 | 164 | 19 |
| SIM RS At tin PNC | 86 | 67 | 147 | 22 |
| SIM RS At tin BBL | 109 | 82 | 126 | 2 |
| SIM RS Nirmala ANC | 76 | 89 | 194 | 21 |
| SIM RS Nirmala INC | 81 | 67 | 164 | 19 |
| SIM RS Nirmala PNC | 86 | 67 | 147 | 22 |
| SIM RS Nirmala BBL | 109 | 82 | 126 | 2 |
| SIM RS PKU ANC | 76 | 89 | 194 | 21 |
| SIM RS PKU BBL | 109 | 82 | 126 | 2 |
| SIM RS MPH Hepatitis | 40 | 20 | 22 | 0 |
| SIM RS Ummu Hani Hepatitis | 40 | 20 | 22 | 0 |
| SIM RS PKU Hepatitis | 40 | 20 | 22 | 0 |
| SIM RS Siaga Medika Hepatitis | 40 | 20 | 22 | 0 |
| Kobo Modul ANC | 75 | 86 | 189 | 16 |
| Kobo Modul INC | 108 | 80 | 248 | 44 |
| Kobo Modul Neonatus | 89 | 50 | 100 | 4 |
| Kobo Modul PNC | 118 | 98 | 228 | 28 |
| Kobo Buku KIA 1 - ANC | 404 | 167 | 733 | 69 |
| Kobo Buku KIA 2 - Luaran Kehamilan | 48 | 38 | 87 | 3 |
| Kobo Buku KIA 3 - PNC | 145 | 75 | 175 | 26 |
| Kobo Buku KIA 4 - Cadre | 83 | 44 | 51 | 15 |
| Kobo Buku KIA 5 - Vaksinatorku | 100 | 40 | 65 | 13 |
| Kobo Neonatus Outcome | 25 | 14 | 25 | 5 |
| Kobo Neonatus Outcome v2 | 208 | 89 | 276 | 52 |
| Kobo DDTK | 20 | 11 | 10 | 0 |
| Master Data (Prerequisite) | 84 | 0 | 84 | 84 |
| **Total (non-unik)** | **11085** | **7344** | **19546** | **2908** |
| **Total unik** | – | **1430** | **4402** | **1082** |
| Selisih (dipakai ulang) | – | 5914 | 15144 | 1826 |

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 1866 |
| http://terminology.kemkes.go.id/sp | 1073 |
| http://loinc.org | 503 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 338 |
| http://hl7.org/fhir/sid/icd-10 | 120 |
|  | 83 |
| http://terminology.kemkes.go.id | 61 |
| http://hl7.org/fhir/sid/icd-9-cm | 53 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 37 |
| http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes | 27 |
| http://sys-ids.kemkes.go.id/kfa | 24 |
| http://terminology.kemkes.go.id/CodeSystem/examination | 22 |
| http://terminology.kemkes.go.id/CodeSystem/organization-type | 20 |
| http://hl7.org/fhir/sid/cvx | 20 |
| http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment | 17 |
| http://terminology.kemkes.go.id/CodeSystem/icd-10-mm | 15 |
| http://terminology.kemkes.go.id/CodeSystem/icd-10-pm | 13 |
| http://sys-ids.kemkes.go.id/kf | 11 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 10 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 10 |
| http://terminology.kemkes.go.id/CodeSystem/location-type | 7 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC | 7 |
| https://loinc.org | 7 |
| http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl | 7 |
| http://terminology.hl7.org/CodeSystem/admit-source | 6 |
| http://terminology.kemkes.go.id/CodeSystem/organization-type/sp | 6 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 5 |
| hhttp://terminology.kemkes.go.id/CodeSystem/organization-type | 4 |
| http://terminology.kemkes.go.id/CodeSystem/organization-ownership | 3 |
| http://terminology.kemkes.go.id/CodeSystem/composition-type | 3 |
| http://terminology.kemkes.go.id/Codesystem/kpsp | 3 |
| http://terminology.kemkes.go.id/CodeSystem/tb-case-definition | 2 |
| https://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 2 |
| http://hl7.org/fhir/administrative-gender | 2 |
| http://terminology.kemkes.go.id/CodeSystem/data-absent-reason | 1 |
| http://terminology.kemkes.go.id/CodeSystem/kptl | 1 |
| http://terminology.hl7. org/CodeSystem/admit -source | 1 |
| http://terminology.kemkes.go.id/CodeSystem/ | 1 |
| http://terminology.kemkes.go.id/CodeSystem/immunization-reason | 1 |
| http://termi nology.hl7. org/CodeSy stem/v3-Ob servationIn terpretation | 1 |
| http://terminology.hl7. org/CodeSystem/v3-Ob servationInterpretatio n | 1 |
| CUSTOM | 1 |
| 237244005 | 1 |
| 65147003 | 1 |
| 64254006 | 1 |
| OV000394 | 1 |
| https://www.ncbi.nlm.nih.gov/gene | 1 |
| Viral Consensus Genome Sequence | 1 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term" | 1 |
| **Total** | **4402** |

---

## Jumlah per CodeSystem (code unik lintas form)

Daftar code satu per baris: lihat [`frekuensi-code.md`](frekuensi-code.md).

| CodeSystem | Jumlah |
|---|---|
| http://snomed.info/sct | 1780 |
| http://terminology.kemkes.go.id/sp | 860 |
| http://loinc.org | 492 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term | 318 |
| http://hl7.org/fhir/sid/icd-10 | 120 |
|  | 86 |
| http://hl7.org/fhir/sid/icd-9-cm | 52 |
| http://terminology.kemkes.go.id | 48 |
| http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes | 37 |
| http://terminology.kemkes.go.id/CodeSystem/anc-custom-codes | 27 |
| http://sys-ids.kemkes.go.id/kfa | 24 |
| http://terminology.kemkes.go.id/CodeSystem/examination | 21 |
| http://terminology.kemkes.go.id/CodeSystem/organization-type | 20 |
| http://hl7.org/fhir/sid/cvx | 20 |
| http://terminology.kemkes.go.id/CodeSystem/prev-tb-treatment | 17 |
| http://terminology.kemkes.go.id/CodeSystem/icd-10-mm | 15 |
| http://terminology.kemkes.go.id/CodeSystem/icd-10-pm | 12 |
| http://sys-ids.kemkes.go.id/kf | 11 |
| http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation | 10 |
| http://terminology.kemkes.go.id/CodeSystem/location-type | 7 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC | 7 |
| https://loinc.org | 7 |
| http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl | 7 |
| http://terminology.hl7.org/CodeSystem/admit-source | 6 |
| http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 5 |
| hhttp://terminology.kemkes.go.id/CodeSystem/organization-type | 4 |
| http://terminology.kemkes.go.id/CodeSystem/composition-type | 3 |
| http://terminology.kemkes.go.id/Codesystem/kpsp | 3 |
| http://terminology.kemkes.go.id/CodeSystem/tb-case-definition | 2 |
| http://hl7.org/fhir/administrative-gender | 2 |
| https://terminology.kemkes.go.id/CodeSystem/episodeofcare-type | 2 |
| http://terminology.kemkes.go.id/CodeSystem/kptl | 1 |
| http://terminology.hl7. org/CodeSystem/admit -source | 1 |
| http://terminology.kemkes.go.id/CodeSystem/ | 1 |
| http://terminology.kemkes.go.id/CodeSystem/immunization-reason | 1 |
| http://terminology.hl7. org/CodeSystem/v3-Ob servationInterpretatio n | 1 |
| CUSTOM | 1 |
| 237244005 | 1 |
| 65147003 | 1 |
| 64254006 | 1 |
| OV000394 | 1 |
| https://www.ncbi.nlm.nih.gov/gene | 1 |
| Viral Consensus Genome Sequence | 1 |
| http://terminology.kemkes.go.id/CodeSystem/clinical-term" | 1 |
| http://terminology.kemkes.go.id/CodeSystem/organization-ownership | 1 |
| http://terminology.hl7.org/CodeSystem/data-absent-reason | 1 |
| **Total** | **4040** |

---

## Payload per resource (semua form)

Baris = form, kolom = resource FHIR. Code pembeda tiap payload: lihat [`frekuensi-payload.md`](frekuensi-payload.md).

| Form | Observation | Procedure | Condition | ServiceRequest | DiagnosticReport | Specimen | Immunization | QuestionnaireResponse | PractitionerRole | Encounter | Patient | Practitioner | EpisodeOfCare | RelatedPerson | MedicationDispense | MedicationRequest | MedicationStatement | CarePlan | Coverage | Medication | Composition | FamilyMemberHistory | AllergyIntolerance | Consent | DocumentReference | Organization | Location | Goal | Media | Group | Account | ClinicalImpression | BodyStructure | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Maternal Outcome | 5 | – | 1 | – | – | – | – | – | 1 | 1 | 1 | 1 | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 12 |
| Raffle | 1 | – | 1 | – | – | – | – | – | – | 1 | 1 | 2 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | 1 | – | – | – | – | – | – | 8 |
| SiGizi ANC | 30 | 3 | 1 | 6 | 6 | 6 | 1 | – | 1 | 1 | 1 | – | 1 | – | 2 | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 61 |
| SITB TB 06 | 17 | 2 | 2 | 9 | 9 | 8 | – | 1 | – | 1 | 1 | – | 3 | – | – | – | – | 1 | – | – | – | – | – | – | – | 1 | 1 | – | – | – | – | – | – | 56 |
| SITB TB 03 SO | 23 | 4 | 1 | 9 | 9 | 9 | – | 1 | – | 1 | 1 | – | 1 | – | – | – | – | 1 | 1 | – | – | – | – | – | – | 1 | – | – | – | – | – | – | – | 62 |
| SITB TB 03 RO | 18 | 3 | 1 | 7 | 7 | 7 | – | 1 | – | 1 | 1 | – | 1 | – | – | – | – | 1 | 1 | – | – | – | – | – | – | 1 | – | – | – | – | – | – | – | 50 |
| SITB TB 04 | 17 | – | 1 | 16 | 16 | 16 | – | – | – | 1 | 1 | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 69 |
| SITB TB 16K | 14 | – | 1 | 1 | – | – | – | 1 | 1 | 1 | 1 | 1 | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 1 | – | – | – | 24 |
| MPDN Kematian Bayi | 16 | – | – | – | – | – | – | – | – | – | 2 | – | – | – | – | – | – | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | 19 |
| MPDN Kematian Ibu | 7 | – | 1 | – | – | – | – | – | – | – | 1 | – | – | – | – | – | – | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | 10 |
| ePus Pelayanan Pasien | 24 | 2 | 9 | 1 | – | – | – | – | – | 1 | 1 | 1 | – | – | 1 | 1 | – | 3 | 1 | – | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | 47 |
| ePus Kunjungan Ibu Hamil | 46 | 5 | 4 | 17 | 16 | 16 | 2 | – | – | 1 | 1 | – | 1 | – | 1 | 1 | 2 | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 114 |
| ePus Laboratorium | 92 | – | – | 74 | 73 | 65 | – | – | 2 | 1 | 1 | – | – | – | – | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 309 |
| ePus Rujukan Eksternal | – | – | 1 | 1 | – | – | – | – | – | 1 | 1 | – | – | – | – | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 5 |
| ePus ANC | 82 | 3 | 3 | 19 | 19 | 6 | 3 | – | 14 | 1 | 1 | 1 | 1 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 155 |
| ePus INC | 49 | 9 | 3 | 1 | – | – | – | 1 | 1 | 1 | 1 | 1 | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 69 |
| ePus PNC | 50 | 9 | 4 | 3 | 2 | 1 | – | – | 2 | 1 | 1 | 1 | 1 | – | 2 | 2 | 1 | 1 | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | 82 |
| ePus MTBS | 53 | 14 | 7 | 9 | 8 | 8 | 17 | 1 | – | 1 | 1 | 1 | – | 1 | 2 | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 125 |
| ePus MTBM | 35 | 8 | 4 | 1 | – | – | 3 | 1 | – | 1 | 1 | 1 | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 57 |
| ePus Tumbang Anak | 14 | 1 | 2 | – | – | – | – | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 19 |
| ePus Tumbang DDTK | 14 | 4 | 3 | 1 | – | – | – | 2 | – | 1 | 1 | 1 | – | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 29 |
| ePus Tumbang KPSP | – | – | – | – | – | – | – | 14 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 14 |
| ePus Tumbang TDD | – | – | – | – | – | – | – | 8 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 8 |
| ePus Tumbang TDL | 4 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 4 |
| ePus Tumbang KMPE | – | – | – | – | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 1 |
| ePus Tumbang M-CHAT-R | – | – | – | – | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 1 |
| Dapodik PAUD | 32 | – | 4 | – | – | – | – | – | – | 1 | 1 | – | – | 3 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 1 | – | – | 42 |
| ePus Tumbang GPPH | – | – | – | – | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 1 |
| SITB TB 01 | 25 | 1 | 1 | – | – | – | – | 1 | – | 1 | 1 | – | 2 | 2 | – | – | 2 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 37 |
| SITB TB 02 | 1 | – | 1 | 2 | – | – | – | 1 | – | 1 | 1 | – | – | – | 2 | 2 | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | 1 | – | 13 |
| ELSMIL Ibu Hamil | 28 | – | 2 | 2 | 1 | 1 | – | – | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 36 |
| ELSMIL Pasca Persalinan | 22 | – | 1 | – | – | – | – | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 24 |
| ELSMIL Baduta | 29 | – | – | – | – | – | 1 | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 31 |
| SIPTM | 31 | 2 | 7 | 3 | 1 | 1 | – | – | – | 1 | 1 | – | – | – | – | 1 | – | – | – | – | – | 1 | – | – | – | – | – | 3 | – | – | – | – | – | 52 |
| ASIK Skrining PTM | 41 | – | 1 | 20 | 20 | 14 | – | – | 6 | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 104 |
| ASIK CKG Bayi Baru Lahir (v2) | 17 | 5 | 1 | – | – | – | – | – | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 25 |
| ASIK CKG Balita (v2) | 17 | 3 | 1 | 2 | 2 | 2 | – | 1 | 2 | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 32 |
| ASIK CKG Dewasa Laki-laki | 53 | – | 1 | 1 | 1 | 1 | – | 1 | 1 | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 61 |
| ASIK CKG Dewasa Perempuan | 58 | – | 1 | 1 | 1 | 1 | – | 1 | 1 | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 66 |
| ASIK CKG Lansia (27 Apr 2026) | 90 | 1 | 1 | – | – | – | – | 7 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 101 |
| SIHEPI Rekap 3e | 44 | 1 | 1 | 4 | 3 | 3 | 5 | – | – | 1 | 1 | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 65 |
| eKohort ANC | 20 | 1 | 1 | 5 | 5 | 5 | 2 | – | – | 1 | 1 | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 43 |
| eKohort INC | 46 | 4 | 2 | 1 | – | – | – | – | – | 1 | 1 | 3 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 58 |
| Buku KIA Identitas dan ANC | 158 | 9 | 3 | 4 | 3 | 3 | 3 | – | – | 1 | 1 | 2 | – | 9 | 1 | 1 | – | 3 | 5 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 206 |
| Buku KIA INC | 28 | 6 | 2 | 1 | – | – | 1 | – | – | 1 | 1 | 1 | 3 | 3 | – | – | – | 7 | 1 | – | 4 | – | – | – | – | – | – | – | – | – | – | – | 1 | 60 |
| Buku KIA PNC | 7 | 4 | 1 | – | – | – | – | – | – | 1 | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 14 |
| Buku KIA Anak | 90 | 44 | 5 | 4 | – | – | 22 | 22 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 189 |
| SITB TB 15 | 8 | – | 1 | – | – | – | – | 1 | – | 1 | 1 | – | – | – | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 13 |
| SITB TB 15P | 15 | – | 1 | 1 | – | – | – | 1 | – | 1 | 1 | – | – | – | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 21 |
| ASIK Kohort Bayi | – | – | – | – | – | – | 18 | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 19 |
| ASIK Kohort Baduta | – | – | – | – | – | – | 3 | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 4 |
| ASIK Kohort WUS | 5 | – | – | – | – | – | 6 | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 12 |
| KuApps BidanKu ANC | 113 | 6 | 5 | 10 | 10 | 9 | 3 | 9 | – | 1 | – | – | – | – | 13 | 3 | 4 | 1 | – | 2 | – | 1 | – | – | – | – | – | – | – | – | – | – | – | 190 |
| KuApps BidanKu PNC | 35 | 6 | 6 | – | – | – | – | – | – | 1 | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 49 |
| KuApps BidanKu BBL | 35 | 6 | 2 | – | – | – | – | 2 | – | 1 | – | – | 1 | – | – | – | – | – | – | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | 48 |
| KuApps BidanKu Bayi | 61 | 7 | 3 | 1 | – | – | – | 24 | – | 1 | – | – | – | – | 1 | 1 | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 101 |
| KuApps BidanKu Anak | 44 | 6 | 4 | 2 | – | – | – | 20 | – | 1 | – | – | – | – | 1 | 1 | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 81 |
| KuApps BidanKu Anak Usia Sekolah dan Remaja | 21 | 2 | 3 | – | – | – | – | 2 | – | – | – | – | – | – | 1 | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 31 |
| KuApps BidanKu Dewasa | 32 | 1 | 2 | – | – | – | 1 | 3 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 39 |
| KuApps BidanKu Lansia | 21 | 1 | 3 | – | – | – | – | 4 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 29 |
| Kuapps Spheres HT | 2 | – | 1 | – | – | – | – | 6 | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 10 |
| Kuapps Spheres DM | 2 | – | 1 | – | – | – | – | 6 | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 10 |
| Kuapps Spheres TB | – | – | 1 | – | – | – | – | 2 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 5 |
| Genomics TB | 1 | – | 1 | 1 | 1 | 1 | – | – | 1 | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 8 |
| Genomics Klebsiella | 2 | – | 1 | 1 | 2 | 1 | – | – | 1 | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 10 |
| Genomics Dengue | 4 | – | 1 | 1 | 2 | 1 | – | – | 1 | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 12 |
| KuApps BidanKu Tambah Pasien | 6 | – | – | 1 | – | – | – | – | – | – | 1 | – | – | 1 | – | – | – | – | 1 | – | – | – | – | 1 | – | – | – | – | – | – | – | – | – | 11 |
| KuApps BidanKu Daftar Kehamilan | 12 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 12 |
| KuApps BidanKu Luaran Kehamilan | 25 | 2 | 1 | 1 | – | – | – | – | – | 1 | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 31 |
| KuApps BidanKu PHBS | – | – | – | – | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 1 |
| KuApps BidanKu Skrining Rumah Tangga | – | – | – | – | – | – | – | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 2 |
| KuApps BidanKu Imunisasi | – | – | – | – | – | – | 23 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 23 |
| KuApps BidanKu Kumpulan Skrinning | 18 | – | – | – | – | – | – | 5 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 23 |
| Kobo SDIDTK | 14 | 4 | 3 | 1 | – | – | – | 8 | – | 1 | 1 | 1 | – | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 35 |
| MMS - Pemantauan Distribusi dan Konsumsi | 10 | – | – | – | – | – | – | – | 1 | – | 1 | 1 | – | 1 | 2 | 2 | 3 | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | 22 |
| MMS - Informed Consent | 2 | – | – | – | – | – | – | 1 | – | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | 3 | – | – | – | – | – | – | – | – | – | 8 |
| MMS - Master Database Responden | 10 | – | – | – | – | – | – | – | 1 | – | 1 | 1 | – | 2 | – | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 16 |
| MMS - Survei Sosio Ekonomi | 13 | – | – | – | – | – | – | 6 | – | – | 1 | 1 | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 22 |
| MMS - Survei Demografi (Listing Responden) | 5 | – | 1 | – | – | – | – | – | 1 | 1 | 1 | – | – | 2 | – | – | – | – | – | – | – | – | – | – | 1 | – | – | – | – | – | – | – | – | 12 |
| MMS - Konfirmasi Kelahiran dan Luaran Kehamilan | 42 | – | 2 | – | – | – | – | – | 1 | – | 1 | 1 | – | 1 | – | – | – | – | – | – | 2 | – | – | – | – | – | – | – | – | – | – | – | – | 50 |
| SKI - Sahabat Sehat Household Survey | 3 | 1 | 5 | – | – | – | – | 1 | – | 1 | 1 | 1 | – | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 14 |
| SKI - Individu Bagian B (Penyakit) | 1 | 3 | 3 | – | – | – | – | 1 | – | 1 | 1 | 1 | – | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 12 |
| SKI - Kesehatan Bayi Balita | – | – | 1 | – | – | – | – | 1 | – | 1 | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 5 |
| SiGizi Balita BNBA | 14 | 1 | 1 | – | – | – | – | 1 | – | 1 | 1 | – | – | 1 | 2 | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 24 |
| SiGizi Balita Vitamin A | 13 | 1 | 1 | – | – | – | – | – | – | 1 | 1 | – | – | 1 | 2 | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 22 |
| SiGizi Balita Mendapat PMT 2024 | 12 | – | 1 | – | – | – | – | – | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 15 |
| SiGizi Balita Pemantauan PMT 2024 | 6 | – | 1 | – | – | – | – | – | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 9 |
| SiGizi Balita ASI Eksklusif | 7 | – | 1 | – | – | – | – | – | – | 1 | 1 | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 11 |
| SiGizi Balita MPASI | 6 | – | 1 | – | – | – | – | – | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 9 |
| SiGizi PMT 2025 BB Tidak Naik - Pantau | 12 | – | 1 | – | – | – | – | – | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 15 |
| SiGizi PMT 2025 BB Tidak Naik - Riwayat | 16 | – | 1 | – | – | – | – | – | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 19 |
| SiGizi PMT 2025 BB Tidak Naik - Survey | 1 | – | 1 | – | – | – | – | 1 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 5 |
| SiGizi PMT 2025 BB Kurang - Pantau | 18 | – | 1 | – | – | – | – | – | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 21 |
| SiGizi PMT 2025 BB Kurang - Riwayat | 16 | – | 1 | – | – | – | – | – | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 19 |
| SiGizi PMT 2025 BB Kurang - Survey | 1 | – | 1 | – | – | – | – | 1 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 5 |
| SiGizi PMT 2025 Gizi Kurang - Pantau | 39 | – | 1 | – | – | – | – | – | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 42 |
| SiGizi PMT 2025 Gizi Kurang - Riwayat | 16 | – | 1 | – | – | – | – | – | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 19 |
| SiGizi PMT 2025 Gizi Kurang - Survey | 1 | – | 1 | – | – | – | – | 1 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 5 |
| SiGizi Ibu Nifas | 3 | 3 | 1 | – | – | – | – | – | – | 1 | 1 | – | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 11 |
| SiGizi Kohort Ibu | 17 | 1 | 15 | 3 | 3 | 3 | 2 | – | 1 | 14 | 1 | – | 2 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 63 |
| SIM RS Tripat ANC | 9 | 1 | 1 | – | – | – | 1 | – | 2 | 1 | 1 | 2 | 1 | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 20 |
| SIM RS Tripat BBL (sheet 'INC BBL') | 11 | 2 | 1 | – | – | – | – | – | 2 | 1 | 1 | 2 | 1 | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 23 |
| SIM RS Tripat PNC | 13 | 1 | 2 | – | – | – | – | – | 2 | 1 | 1 | 2 | 1 | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 24 |
| SIM RS Narmada INC | 57 | 5 | 10 | – | – | – | 4 | – | – | 1 | 1 | 1 | 3 | 1 | – | – | 1 | – | – | – | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | 86 |
| SIM RS Narmada KIA | 37 | 2 | 4 | – | – | – | 1 | – | – | 1 | 1 | 1 | 2 | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 50 |
| SIM RS Panti Nugroho ANC | 17 | 2 | 2 | – | – | – | 3 | – | 1 | 1 | 1 | 1 | 1 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 31 |
| SIM RS Panti Nugroho INC | 23 | 3 | 2 | 1 | – | – | – | – | 1 | 1 | 1 | 2 | 2 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 37 |
| SIM RS Panti Nugroho PNC | 38 | 10 | 6 | 1 | – | – | – | – | 1 | 1 | 1 | 1 | 1 | – | 3 | 2 | – | – | – | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | 67 |
| SIM RS Panti Nugroho BBL | 14 | 7 | 1 | – | – | – | 2 | – | 1 | 1 | 1 | 1 | 1 | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 31 |
| SIM RS Panti Nugroho Diabetes Melitus | 3 | – | 1 | – | – | – | – | – | – | 1 | 1 | – | – | – | – | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 7 |
| SIM RS Panti Nugroho Hipertensi | 7 | 2 | 3 | 2 | 1 | 1 | – | – | 1 | 1 | 1 | 1 | – | – | – | – | 2 | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 23 |
| SIM RS Panti Nugroho Stroke | 5 | 2 | 3 | 2 | 1 | 1 | – | – | 1 | 1 | 1 | 1 | – | – | – | – | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 20 |
| SIM RS Ummu Hani ANC | 11 | 1 | 3 | – | – | – | 1 | – | 2 | 1 | 1 | 2 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 23 |
| SIM RS Ummu Hani INC | 23 | 4 | 2 | 1 | – | – | – | – | 3 | 1 | 1 | 3 | 2 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 41 |
| SIM RS Ummu Hani PNC | 28 | 5 | 4 | 1 | – | – | – | – | 2 | 1 | 1 | 2 | 1 | 1 | 3 | 2 | – | – | – | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | 53 |
| SIM RS Ummu Hani BBL | 13 | 7 | 1 | – | – | – | 2 | – | 1 | 1 | 1 | 1 | 1 | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 30 |
| SIM RS MPH ANC | 18 | 2 | 3 | – | – | – | 1 | – | 2 | 1 | 1 | 2 | 1 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 33 |
| SIM RS MPH INC | 24 | 4 | 2 | 1 | – | – | – | – | 2 | 1 | 1 | 2 | 2 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 40 |
| SIM RS MPH PNC | 27 | 2 | 4 | 2 | – | – | – | – | 2 | 1 | 1 | 2 | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 43 |
| SIM RS MPH BBL | 25 | 4 | 1 | 1 | – | – | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | – | – | – | – | – | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | 42 |
| SIM RS MPH Diabetes Melitus | 6 | 2 | 3 | 2 | 2 | 1 | – | – | 2 | 1 | 1 | 2 | – | – | – | – | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 24 |
| SIM RS MPH Hipertensi | 5 | 2 | 3 | 2 | 1 | 1 | – | – | 1 | 1 | 1 | 1 | – | – | – | – | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 20 |
| SIM RS Siaga Medika ANC | 36 | 2 | 1 | 15 | 15 | 6 | 3 | – | 16 | 1 | 1 | 1 | 1 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 100 |
| SIM RS Siaga Medika INC | 29 | 5 | 2 | – | – | – | – | – | – | 1 | 1 | 1 | 2 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 42 |
| SIM RS Siaga Medika PNC | 30 | 9 | 4 | – | – | – | – | – | 1 | 1 | 1 | 1 | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 49 |
| SIM RS Siaga Medika BBL | 22 | 4 | 1 | 1 | – | – | 2 | 1 | – | 1 | 1 | – | 1 | 2 | – | – | – | – | – | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | 37 |
| SIM RS PKU INC | 46 | 8 | 5 | 1 | – | – | – | – | 1 | 1 | 1 | 1 | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 66 |
| SIM RS PKU PNC | 38 | 10 | 6 | 1 | – | – | – | – | 1 | 1 | 1 | 1 | 1 | – | 3 | 2 | – | – | – | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | 67 |
| SIM RS Goetoeng ANC | 3 | 97 | 2 | 1 | – | – | – | – | – | 1 | 1 | – | – | – | – | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 106 |
| SIM RS Goetoeng INC | 5 | 48 | 6 | 1 | – | – | – | – | – | 1 | 1 | – | – | – | – | – | – | – | 1 | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | 64 |
| SIM RS Goetoeng PNC | 4 | – | 1 | – | – | – | – | – | – | 1 | 1 | 1 | – | – | – | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 9 |
| SIM RS Goetoeng BBL | 5 | 52 | 6 | – | – | – | – | – | – | 1 | 1 | – | 1 | – | – | – | – | – | 1 | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | 68 |
| SIM RS Goetoeng Diabetes Melitus | 3 | – | 1 | – | – | – | – | – | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 6 |
| SIM RS Goetoeng Hipertensi | 2 | – | 1 | – | – | – | – | – | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 5 |
| SISMAL Regmal 1 | 14 | – | 1 | 1 | – | – | – | – | 1 | 1 | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 20 |
| SISMAL Validasi Indigenous | 2 | 1 | 1 | – | – | – | – | – | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 1 | – | – | – | – | – | – | 7 |
| SIM RS Harapan Ibu ANC | 52 | 2 | 3 | 6 | 6 | 6 | 3 | – | 7 | 1 | 1 | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 89 |
| SIM RS Harapan Ibu INC | 46 | 8 | 5 | 1 | – | – | – | 1 | 1 | 1 | 1 | 1 | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 67 |
| SIM RS Harapan Ibu PNC | 38 | 10 | 6 | 1 | – | – | – | – | 1 | 1 | 1 | 1 | 1 | – | 3 | 2 | – | – | – | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | 67 |
| SIM RS Harapan Ibu BBL | 59 | 7 | 4 | – | – | – | 2 | – | 1 | 1 | 1 | 1 | 1 | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 79 |
| SIM RS At tin ANC | 52 | 2 | 3 | 6 | 6 | 6 | 3 | – | 7 | 1 | 1 | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 89 |
| SIM RS At tin INC | 46 | 8 | 5 | 1 | – | – | – | 1 | 1 | 1 | 1 | 1 | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 67 |
| SIM RS At tin PNC | 38 | 10 | 6 | 1 | – | – | – | – | 1 | 1 | 1 | 1 | 1 | – | 3 | 2 | – | – | – | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | 67 |
| SIM RS At tin BBL | 62 | 7 | 4 | – | – | – | 2 | – | 1 | 1 | 1 | 1 | 1 | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 82 |
| SIM RS Nirmala ANC | 52 | 2 | 3 | 6 | 6 | 6 | 3 | – | 7 | 1 | 1 | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 89 |
| SIM RS Nirmala INC | 46 | 8 | 5 | 1 | – | – | – | 1 | 1 | 1 | 1 | 1 | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 67 |
| SIM RS Nirmala PNC | 38 | 10 | 6 | 1 | – | – | – | – | 1 | 1 | 1 | 1 | 1 | – | 3 | 2 | – | – | – | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | 67 |
| SIM RS Nirmala BBL | 62 | 7 | 4 | – | – | – | 2 | – | 1 | 1 | 1 | 1 | 1 | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 82 |
| SIM RS PKU ANC | 52 | 2 | 3 | 6 | 6 | 6 | 3 | – | 7 | 1 | 1 | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 89 |
| SIM RS PKU BBL | 62 | 7 | 4 | – | – | – | 2 | – | 1 | 1 | 1 | 1 | 1 | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 82 |
| SIM RS MPH Hepatitis | 3 | 2 | 3 | 2 | 1 | 1 | – | – | 2 | 1 | 1 | 2 | – | – | – | – | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 20 |
| SIM RS Ummu Hani Hepatitis | 3 | 2 | 3 | 2 | 1 | 1 | – | – | 2 | 1 | 1 | 2 | – | – | – | – | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 20 |
| SIM RS PKU Hepatitis | 3 | 2 | 3 | 2 | 1 | 1 | – | – | 2 | 1 | 1 | 2 | – | – | – | – | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 20 |
| SIM RS Siaga Medika Hepatitis | 3 | 2 | 3 | 2 | 1 | 1 | – | – | 2 | 1 | 1 | 2 | – | – | – | – | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 20 |
| Kobo Modul ANC | 47 | 3 | 2 | 6 | 6 | 6 | 3 | – | 7 | 1 | 1 | 1 | 1 | – | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 86 |
| Kobo Modul INC | 56 | 9 | 3 | 1 | – | – | – | 1 | 2 | 1 | 1 | 2 | 2 | 1 | – | – | – | – | – | – | – | – | – | – | 1 | – | – | – | – | – | – | – | – | 80 |
| Kobo Modul Neonatus | 29 | 9 | 1 | 1 | – | – | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | – | – | – | – | – | – | – | – | 1 | – | – | – | – | – | – | – | – | – | – | 50 |
| Kobo Modul PNC | 52 | 10 | 8 | 5 | 2 | 1 | – | 1 | 4 | 1 | 1 | 2 | 1 | – | 4 | 3 | – | 1 | – | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | 98 |
| Kobo Buku KIA 1 - ANC | 125 | 14 | 6 | 1 | – | – | 3 | – | 2 | 1 | 1 | 1 | – | – | 1 | 1 | 1 | 3 | 2 | – | – | 3 | 1 | – | 1 | – | – | – | – | – | – | – | – | 167 |
| Kobo Buku KIA 2 - Luaran Kehamilan | 29 | 1 | 2 | – | – | – | – | – | 2 | 1 | 1 | 1 | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 38 |
| Kobo Buku KIA 3 - PNC | 45 | 9 | 7 | 4 | – | – | 1 | – | 1 | 1 | 1 | 1 | 2 | – | 1 | 1 | – | – | 1 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 75 |
| Kobo Buku KIA 4 - Cadre | 16 | 1 | 1 | – | – | – | 15 | – | 2 | 1 | 1 | 3 | – | 4 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 44 |
| Kobo Buku KIA 5 - Vaksinatorku | 5 | – | 1 | – | – | – | 25 | – | 1 | 1 | 1 | 1 | – | 4 | – | – | – | – | – | – | – | – | – | – | 1 | – | – | – | – | – | – | – | – | 40 |
| Kobo Neonatus Outcome | 8 | – | – | – | – | – | – | – | 1 | – | 1 | 1 | 1 | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 14 |
| Kobo Neonatus Outcome v2 | 60 | 6 | 3 | – | – | – | 3 | 1 | 4 | 1 | 1 | 4 | – | 3 | – | – | – | – | – | – | – | – | – | 1 | – | – | – | – | 2 | – | – | – | – | 89 |
| Kobo DDTK | 4 | – | 1 | – | – | – | – | – | 1 | 1 | 1 | 1 | – | 2 | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 11 |
| Master Data (Prerequisite) | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | – | 0 |
| **Total (non-unik)** | **4054** | **665** | **378** | **341** | **276** | **233** | **209** | **189** | **164** | **150** | **143** | **109** | **89** | **81** | **62** | **46** | **40** | **26** | **23** | **18** | **10** | **7** | **7** | **5** | **4** | **3** | **3** | **3** | **2** | **1** | **1** | **1** | **1** | **7344** |
| **Total unik** | **914** | **201** | **98** | **34** | **109** | **7** | **17** | **1** | **1** | **1** | **1** | **1** | **6** | **1** | **10** | **11** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1430** |

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

- **SISMAL (2 form, ⚠️ belum comprehensive review)**: dari `PHDT_SISMAL.xlsx` (tanpa daftar BQ dan file mentah). Regmal 1 20 payload / 54 code, Validasi Indigenous 7 / 12. Organization lookup (tidak dihitung); Location "Alamat Asal Penularan" di Indigenous dihitung (dibuat dari isian form). Sheet `Verifikasi Uji Silang` **tidak dihitung**: isinya salinan template TB-TPT, bukan form malaria. Detail & asumsi: `revisi.md`.


- **KuApps BidanKu, Kuapps Spheres, Genomics, SITB TB 15 / 15P, ASIK Kohort (28 form, baru)**: dari `KuApps_Reborn_Variable_and_FHIR_Mapping.xlsx` (sheet PYD-ANC, PYD-PNC, PYD-BBL, PYD-Bayi, PYD-Anak, PYD-Anak Usekre, PYD Dewasa, PYD Lansia = #106–113), `Mapping_KuApps_SPHERES.xlsx` (Form Caregap HT / DM / TB = #114–116), `Genomics_SPHERES_Data_Dictionary_.xlsx` (TB / Klebsiella / Dengue = #118–120), CSV TB 15 (#60), TB 15P (#61), dan ASIK (Imunisasi Bayi #39, Baduta #40, WUS #41). ⚠️ belum comprehensive review, tanpa daftar variabel BQ. Dibuat dengan `scripts/kuapps_prepare.py` dan `scripts/phdt2_prepare.py`. Sheet IFIV, Summary, Gambar SDIDTK, List Skrining, dan `Notes untuk Robin` bukan dictionary dan dilewati. Sheet Tambah Pasien, Daftar Kehamilan, Luaran Kehamilan, PHBS, Skrining Rumah Tangga, Imunisasi, dan Kumpulan Skrinning (7 form) ditambahkan sebagai baris tracker baru #284–290 dan masuk total. Asumsi: (1) typo `valuableCodeableConcept` di TB 15 / TB 15P / ASIK dibaca `valueCodeableConcept`; (2) di PYD Bayi dan PYD Anak 24 baris kehilangan 1 kolom di kiri (Ya/Tidak masuk kolom Resource) dan digeser otomatis; (3) di ASIK Kohort, kode vaksin ada di path `Immunization.vaccineCode.coding.code`, dibaca sebagai `coding`; vaksin kombinasi (DPT-Hb-Hib, 4 kode) = 1 payload dengan 4 code; (4) di Form Caregap DM / HT kolom `Sub Variables` dipakai sebagai nama variabel.
- **Buku KIA 2024 (4 form, baru)**: dari 4 CSV `PHDT_Buku_KIA_-_Mapping_{ANC,INC,PNC,Anak_Usia_0-6_Tahun}_Buku_KIA_2024.csv` (⚠️ belum comprehensive review, tanpa daftar variabel BQ). Dibuat dengan `scripts/phdt2_prepare.py`. Angka: ANC 206 / 388, INC 60 / 108, PNC 14 / 32, Anak 189 / 284. Variabel unik vs `referensi-variabel-phdt.md` (Identitas+ANC 296, INC 58, PNC 17, Anak 267): ANC 235 (−61), INC 79 (+21), PNC 26 (+9), Anak 266 (−1). Angka output tetap dipakai. Variabel tanpa payload (perlu dicek): ANC 12, INC 4, PNC 9, Anak 34 (lihat bagian "Variabel di luar payload" di `output/buku-kia-*.md`). File ANC punya kolom tambahan (nama variabel OCR, Kobo ANC SID, JSON); kolom itu tidak dipakai di hitungan.
- **Kobo (12 form, baru)**: dari `Kobo_-_Data_Dictionary.xlsx`. Sheet `ANC Kobo`, `INC Kobo`, `Neonatus Kobo`, `PNC Kobo`, `Mapping Kobo Buku KIA 1 - ANC`, `Mapping Variable Buku KIA Entry Form 2`, `Mapping Kobo Buku KIA 3 - PNC`, `Mapping Variabel Kobo Buku KIA 4- Cadre`, `Mapping Kobo Vaksinator (revisedform)`, `Neonatal Outcome Kobo`, `Neonatal Outcome v2`, `DDTK Kobo`. Dilewati: `Variabel ...`, `tarikan ...`, `Copy of Neonatus Kobo`, `Deprecated PNC`, `epus pnc dan buku kia`, `rencana INC`, `Variabel ANC (sigizi lama)` (= SiGizi ANC yang sudah dihitung), `Mapping Kobo Buku KIA 5 - Vaksinator (tdk dipakai)`. `Maternal Outcome Kobo` dan `Kobo Raffle` tidak dihitung ulang (angka Maternal Outcome / Raffle yang sudah ada tetap). `Data BBL Kobo` dihitung terpisah karena tidak ada baris tracker yang cocok. Buku KIA 1 - ANC punya 404 variabel unik (kolom `Question/answer option` dipakai sebagai Variables).
- **SIM RS template Spheres**: sheet TRACKER di file RS mencatat RS yang memakai Excel template Spheres. RS tanpa sheet mapping sendiri memakai angka template: ANC/INC/PNC = template ANC/INC/PNC, BBL = template BBL (neo) untuk Harapan Ibu dan BBL (INC) untuk At tin, Nirmala, PKU, Hepatitis = template HepB. Panti Nugroho Hepatitis, Nirmala Hepatitis, dan Harapan Ibu Hepatitis tidak dihitung (notes: form SIHEPI baru). Margono dan Goetoeng (selain sheet yang sudah ada) belum kirim data.
- **Kobo SDIDTK (#103) dan MMS (6 form, #291–296, baru)**: SDIDTK dari `Kobo_-_Data_Dictionary_-_Copy_of_SDIDTK.csv` (35 payload, 68 code); MMS dari `MMS_Data_Dictionary.xlsx`, 6 sheet = 6 form (Distribusi dan Konsumsi 22/51, Informed Consent 8/5, Master Responden 16/33, Sosio Ekonomi 22/200, Demografi 12/20, Konfirmasi Kelahiran 50/193). ⚠️ belum comprehensive review, tanpa daftar variabel BQ (baris tanpa variabel BQ di "Variabel di luar payload" adalah isian kondisional/pendukung tanpa mapping, bukan variabel BQ). Nomor #291–296 saya pilih sendiri, melanjutkan #283. Dibuat dengan `scripts/kuapps_prepare.py` (MMS) dan `scripts/phdt2_prepare.py` (SDIDTK).
- **SKI (3 form, baru) dan SITB TB 16K revised**: SKI dari `PHDT_Data_SKI.xlsx` (Household Survey 14 payload / 102 code, Individu Bagian B 12 / 62, Bayi Balita 5 / 4), ⚠️ belum comprehensive review, tanpa daftar BQ dan file mentah. Sheet `FIX_SKI Ruta_Bagian 1_Identitas` (235 variabel) belum ada mapping FHIR, dilewati. Blok QuestionnaireResponse tanpa baris `questionnaire` dianggap lanjutan dari QR sebelumnya (tidak dihitung terpisah). TB 16K diganti dengan file revised: 24 payload / 38 code (sebelumnya 21 / 35). Nomor #297–299 saya pilih sendiri. Asumsi KS1–KS4: `revisi.md`.
- **Master Data (Prerequisite)**: 15 kode custom SP untuk data master (PractitionerRole 8: Pengelola SIK, Cleaning Service, Vaksinator, PJ SITB, PJ KIA, Kader Madya/Purwa/Utama; Organization.type 7: 6 jenis satuan PAUD + Kelurahan), diambil dari `SPHERES_Custom_Value_Set_FHIR`. Dihitung sebagai **code** (kode custom dihitung di path coded mana pun), **0 payload** karena Organization/PractitionerRole master data tidak dibuat dari form. Tidak ada baris tracker. Dibuat manual (`mapping/phdt-data-dictionary-master-data-prerequisite.csv`).

---

## Log perubahan output
- 2026-11-25 (6): 36 baris di 25 dictionary dibetulkan: kode SNOMED/LOINC yang salah diberi CodeSystem `kemkes.go.id/sp` dipindah ke SNOMED/LOINC, dan akhiran ".0" dihapus (mis. 718-7, 135840009, 49052-4, 276707008). `special-needs` (Dapodik PAUD) belum diputuskan. Code SP unik 1019 → 1004; total unik 1430 payload / 4341 code (non-unik tetap 7344 / 19477).
- 2026-11-25 (7): Code SP sekarang juga menghitung CodeSystem `organization-type/sp` (6 kode master PAUD: SP000385–388, SP000457, SP000458). `special-needs` (Dapodik PAUD) tetap kode bernama, dihitung sebagai Code SP. Code SP unik 1004 → 1010.
- 2026-11-25 (8): Master Data (Prerequisite) ditambah 69 kode SP master (dari daftar master Kemkes, frekuensi 0 di form; Resource/Path sesuai daftar, 5 kode frekuensi harian/MMS tanpa elemen). Master Data jadi 84 code / 0 payload. Total non-unik 19546 code; unik 4410 code, Code SP unik 1010 → 1079.
- 2026-11-25 (9): 32 baris di 21 dictionary: kode berformat SP000xxx yang CodeSystem-nya LOINC / SNOMED / organization-ownership / kosong diubah ke `http://terminology.kemkes.go.id/sp` (SP000050, SP000120, SP000208, SP000367, SP000368, SP000369, SP000380, SP000381, SP000382, SP000658, SP000761). Code SP unik 1079 → 1082; total unik 4402 code.
- 2026-11-25 (10): Kode SP000367, SP000368, SP000761 (kepemilikan faskes) memakai CodeSystem `http://terminology.kemkes.go.id/CodeSystem/organization-ownership` (14 baris di 6 dictionary), bukan `kemkes.go.id/sp` dan bukan varian `/sp`; seperti `organization-type/sp` (PAUD), beda sistem tapi tetap dihitung sebagai Code SP. 5 kode SP000895–898 dan SP000910 di Master Data diberi elemen Observation.code.coding (sebelumnya "Tanpa elemen").
- 2026-11-25 (5): Informed Consent (#78) dikeluarkan dari konsolidasi (bukan aplikasi tersendiri; file mapping/output tetap ada di repo). Total non-unik 7344 payload / 19477 code; unik 1431 / 4349.
- 2026-11-25 (4): Tambah 3 form SKI (#297–299) dan ganti SITB TB 16K dengan versi revised (21/35 → 24/38). Total non-unik 7347 payload / 19485 code; unik 1431 / 4357.
- 2026-11-25 (3): Tambah form Master Data (Prerequisite): 0 payload / 15 code. Total non-unik 7313 payload / 19314 code; unik 1420 / 4272.
- 2026-11-25: Tambah Kobo SDIDTK (#103) dan 6 form MMS (#291–296). Total non-unik 7313 payload / 17518 code; unik 1420 / 4040. ⚠️ belum comprehensive review.
- 2026-11-25: Tambah 7 sheet BidanKu (Tambah Pasien #284, Daftar Kehamilan #285, Luaran Kehamilan #286, PHBS #287, Skrining Rumah Tangga #288, Imunisasi #289, Kumpulan Skrinning #290) sebagai baris tracker baru. Total non-unik 7148 payload / 16948 code. ⚠️ belum comprehensive review.
- 2026-11-24 (5): Tambah 21 form: BidanKu 8 (#106–113), Spheres HT/DM/TB (#114–116), Genomics TB/Klebsiella/Dengue (#118–120), TB 15 (#60), TB 15P (#61), ASIK Kohort Bayi/Baduta/WUS (#39–41). ⚠️ belum comprehensive review.
- 2026-11-24 (4): Tambah 4 form Buku KIA 2024 (tracker #79–82): ANC 206 / 388, INC 60 / 108, PNC 14 / 32, Anak 189 / 284. ⚠️ belum comprehensive review.
- 2026-11-24 (3): Tambah 12 form Kobo dari `Kobo_-_Data_Dictionary.xlsx` (#83–86, #88–94, #101) dan 18 form SIM RS yang memakai template Spheres (berdasarkan notes sheet TRACKER di file RS: Harapan Ibu, At tin, Nirmala ANC/INC/PNC/BBL; PKU ANC/BBL; Hepatitis MPH, Ummu Hani, PKU, Siaga Medika). Tiap RS dihitung sebagai form sendiri dengan angka template (non-unik). ⚠️ belum comprehensive review.
- 2026-11-24 (3): Tambah 2 form SISMAL: Regmal 1 (20 payload / 54 code) dan Validasi Kasus Indigenous (7 / 12), ⚠️ belum comprehensive review. Total non-unik **3929 payload / 9801 code** (sebelumnya 3902 / 9735), unik **1004 / 2686** (sebelumnya 996 / 2648). Tabel frekuensi, CodeSystem, payload per resource dibuat ulang dengan `scripts/consolidate.py`.
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
