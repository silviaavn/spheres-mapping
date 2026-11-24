"""Konsolidasi lintas form: frekuensi-payload.md, frekuensi-code.md, dan tabel di output.md.
Pemakaian: python3 -I consolidate.py <repo> <outdir> [jumlah_form]"""
import sys, importlib.util
from collections import OrderedDict, Counter
repo, outdir = sys.argv[1], sys.argv[2]
nform = int(sys.argv[3]) if len(sys.argv) > 3 else None
spec = importlib.util.spec_from_file_location('fo', repo + '/scripts/form_output.py'); fo = importlib.util.module_from_spec(spec); spec.loader.exec_module(fo)
FORMS = [("Maternal Outcome", "kobo-data-dictionary-maternal-outcome"), ("Raffle", "kobo-data-dictionary-raffle"),
         ("SiGizi ANC", "phdt-data-dictionary-sigizi-anc"), ("SITB TB 06", "phdt-data-dictionary-sitb-tb06"),
         ("SITB TB 03 SO", "phdt-data-dictionary-sitb-tb03-so"), ("SITB TB 03 RO", "phdt-data-dictionary-sitb-tb03-ro"),
         ("SITB TB 04", "phdt-data-dictionary-sitb-tb04"), ("SITB TB 16K", "phdt-data-dictionary-sitb-tb16k"),
         ("MPDN Kematian Bayi", "phdt-data-dictionary-mpdn-kematian-bayi"), ("MPDN Kematian Ibu", "phdt-data-dictionary-mpdn-kematian-ibu"),
         ("ePus Pelayanan Pasien", "phdt-data-dictionary-epus-pelayanan"),
         ("ePus Kunjungan Ibu Hamil", "phdt-data-dictionary-epus-kunjungan-ibu-hamil"),
         ("ePus Laboratorium", "phdt-data-dictionary-epus-lab"),
         ("ePus Rujukan Eksternal", "phdt-data-dictionary-epus-rujukan-eksternal"),
         ("ePus ANC", "phdt-data-dictionary-epus-anc"),
         ("ePus INC", "phdt-data-dictionary-epus-inc"),
         ("ePus PNC", "phdt-data-dictionary-epus-pnc"),
         ("ePus MTBS", "phdt-data-dictionary-epus-mtbs"),
         ("ePus MTBM", "phdt-data-dictionary-epus-mtbm"),
         ("ePus Tumbang Anak", "phdt-data-dictionary-epus-tumbang-anak"),
         ("ePus Tumbang DDTK", "phdt-data-dictionary-epus-tumbang-ddtk"),
         ("ePus Tumbang KPSP", "phdt-data-dictionary-epus-tumbang-kpsp"),
         ("ePus Tumbang TDD", "phdt-data-dictionary-epus-tumbang-tdd"),
         ("ePus Tumbang TDL", "phdt-data-dictionary-epus-tumbang-tdl"),
         ("ePus Tumbang KMPE", "phdt-data-dictionary-epus-tumbang-kmpe"),
         ("ePus Tumbang M-CHAT-R", "phdt-data-dictionary-epus-tumbang-mchat"),
         ("Dapodik PAUD", "phdt-data-dictionary-dapodik-paud"),
         ("ePus Tumbang GPPH", "phdt-data-dictionary-epus-tumbang-gpph"),
         ("SITB TB 01", "phdt-data-dictionary-sitb-tb01"),
         ("SITB TB 02", "phdt-data-dictionary-sitb-tb02"),
         ("ELSMIL Ibu Hamil", "phdt-data-dictionary-elsmil-ibu-hamil"),
         ("ELSMIL Pasca Persalinan", "phdt-data-dictionary-elsmil-pasca-persalinan"),
         ("ELSMIL Baduta", "phdt-data-dictionary-elsmil-baduta"),
         ("SIPTM", "phdt-data-dictionary-siptm"),
         ("ASIK Skrining PTM", "phdt-data-dictionary-asik-skrining-ptm"),
         ("ASIK CKG Bayi Baru Lahir (v2)", "phdt-data-dictionary-asik-ckg-bbl"),
         ("ASIK CKG Balita (v2)", "phdt-data-dictionary-asik-ckg-balita"),
         ("ASIK CKG Dewasa Laki-laki", "phdt-data-dictionary-asik-ckg-dewasa-laki"),
         ("ASIK CKG Dewasa Perempuan", "phdt-data-dictionary-asik-ckg-dewasa-perempuan"),
         ("ASIK CKG Lansia (27 Apr 2026)", "phdt-data-dictionary-asik-ckg-lansia"),
         ("Informed Consent", "phdt-data-dictionary-informed-consent"),
         ("SIHEPI Rekap 3e", "phdt-data-dictionary-sihepi-rekap-3e"),
         ("eKohort ANC", "phdt-data-dictionary-ekohort-anc"),
         ("eKohort INC", "phdt-data-dictionary-ekohort-inc"),
         ("SiGizi Balita BNBA", "phdt-data-dictionary-sigizi-balita-bnba"),
         ("SiGizi Balita Vitamin A", "phdt-data-dictionary-sigizi-balita-vitamin-a"),
         ("SiGizi Balita Mendapat PMT 2024", "phdt-data-dictionary-sigizi-balita-mendapat-pmt-2024"),
         ("SiGizi Balita Pemantauan PMT 2024", "phdt-data-dictionary-sigizi-balita-pemantauan-pmt-2024"),
         ("SiGizi Balita ASI Eksklusif", "phdt-data-dictionary-sigizi-balita-asi-eksklusif"),
         ("SiGizi Balita MPASI", "phdt-data-dictionary-sigizi-balita-mpasi"),
         ("SiGizi PMT 2025 BB Tidak Naik - Pantau", "phdt-data-dictionary-sigizi-pmt2025-bb-tidak-naik-pantau"),
         ("SiGizi PMT 2025 BB Tidak Naik - Riwayat", "phdt-data-dictionary-sigizi-pmt2025-bb-tidak-naik-riwayat"),
         ("SiGizi PMT 2025 BB Tidak Naik - Survey", "phdt-data-dictionary-sigizi-pmt2025-bb-tidak-naik-survey"),
         ("SiGizi PMT 2025 BB Kurang - Pantau", "phdt-data-dictionary-sigizi-pmt2025-bb-kurang-pantau"),
         ("SiGizi PMT 2025 BB Kurang - Riwayat", "phdt-data-dictionary-sigizi-pmt2025-bb-kurang-riwayat"),
         ("SiGizi PMT 2025 BB Kurang - Survey", "phdt-data-dictionary-sigizi-pmt2025-bb-kurang-survey"),
         ("SiGizi PMT 2025 Gizi Kurang - Pantau", "phdt-data-dictionary-sigizi-pmt2025-gizi-kurang-pantau"),
         ("SiGizi PMT 2025 Gizi Kurang - Riwayat", "phdt-data-dictionary-sigizi-pmt2025-gizi-kurang-riwayat"),
         ("SiGizi PMT 2025 Gizi Kurang - Survey", "phdt-data-dictionary-sigizi-pmt2025-gizi-kurang-survey"),
         ("SiGizi Ibu Nifas", "phdt-data-dictionary-sigizi-ibu-nifas"),
         ("SiGizi Kohort Ibu", "phdt-data-dictionary-sigizi-kohort-ibu"),
         ("SIM RS Tripat ANC", "phdt-data-dictionary-rs-tripat-anc"),
         ("SIM RS Tripat BBL (sheet 'INC BBL')", "phdt-data-dictionary-rs-tripat-bbl"),
         ("SIM RS Tripat PNC", "phdt-data-dictionary-rs-tripat-pnc"),
         ("SIM RS Narmada INC", "phdt-data-dictionary-rs-narmada-inc"),
         ("SIM RS Narmada KIA", "phdt-data-dictionary-rs-narmada-kia"),
         ("SIM RS Panti Nugroho ANC", "phdt-data-dictionary-rs-panti-nugroho-anc"),
         ("SIM RS Panti Nugroho INC", "phdt-data-dictionary-rs-panti-nugroho-inc"),
         ("SIM RS Panti Nugroho PNC", "phdt-data-dictionary-rs-panti-nugroho-pnc"),
         ("SIM RS Panti Nugroho BBL", "phdt-data-dictionary-rs-panti-nugroho-bbl"),
         ("SIM RS Panti Nugroho Diabetes Melitus", "phdt-data-dictionary-rs-panti-nugroho-dm"),
         ("SIM RS Panti Nugroho Hipertensi", "phdt-data-dictionary-rs-panti-nugroho-ht"),
         ("SIM RS Panti Nugroho Stroke", "phdt-data-dictionary-rs-panti-nugroho-stroke"),
         ("SIM RS Ummu Hani ANC", "phdt-data-dictionary-rs-ummu-hani-anc"),
         ("SIM RS Ummu Hani INC", "phdt-data-dictionary-rs-ummu-hani-inc"),
         ("SIM RS Ummu Hani PNC", "phdt-data-dictionary-rs-ummu-hani-pnc"),
         ("SIM RS Ummu Hani BBL", "phdt-data-dictionary-rs-ummu-hani-bbl"),
         ("SIM RS MPH ANC", "phdt-data-dictionary-rs-mph-anc"),
         ("SIM RS MPH INC", "phdt-data-dictionary-rs-mph-inc"),
         ("SIM RS MPH PNC", "phdt-data-dictionary-rs-mph-pnc"),
         ("SIM RS MPH BBL", "phdt-data-dictionary-rs-mph-bbl"),
         ("SIM RS MPH Diabetes Melitus", "phdt-data-dictionary-rs-mph-dm"),
         ("SIM RS MPH Hipertensi", "phdt-data-dictionary-rs-mph-ht"),
         ("SIM RS Siaga Medika ANC", "phdt-data-dictionary-rs-siaga-medika-anc"),
         ("SIM RS Siaga Medika INC", "phdt-data-dictionary-rs-siaga-medika-inc"),
         ("SIM RS Siaga Medika PNC", "phdt-data-dictionary-rs-siaga-medika-pnc"),
         ("SIM RS Siaga Medika BBL", "phdt-data-dictionary-rs-siaga-medika-bbl"),
         ("SIM RS PKU INC", "phdt-data-dictionary-rs-pku-inc"),
         ("SIM RS PKU PNC", "phdt-data-dictionary-rs-pku-pnc"),
         ("SIM RS Goetoeng ANC", "phdt-data-dictionary-rs-goetoeng-anc"),
         ("SIM RS Goetoeng INC", "phdt-data-dictionary-rs-goetoeng-inc"),
         ("SIM RS Goetoeng PNC", "phdt-data-dictionary-rs-goetoeng-pnc"),
         ("SIM RS Goetoeng BBL", "phdt-data-dictionary-rs-goetoeng-bbl"),
         ("SIM RS Goetoeng Diabetes Melitus", "phdt-data-dictionary-rs-goetoeng-dm"),
         ("SIM RS Goetoeng Hipertensi", "phdt-data-dictionary-rs-goetoeng-ht"),
         ("SISMAL Regmal 1", "phdt-data-dictionary-sismal-regmal1"),
         ("SISMAL Validasi Indigenous", "phdt-data-dictionary-sismal-validasi-indigenous"),
         ("SIM RS Harapan Ibu ANC", "phdt-data-dictionary-rs-harapan-ibu-anc"),
         ("SIM RS Harapan Ibu INC", "phdt-data-dictionary-rs-harapan-ibu-inc"),
         ("SIM RS Harapan Ibu PNC", "phdt-data-dictionary-rs-harapan-ibu-pnc"),
         ("SIM RS Harapan Ibu BBL", "phdt-data-dictionary-rs-harapan-ibu-bbl"),
         ("SIM RS At tin ANC", "phdt-data-dictionary-rs-attin-anc"),
         ("SIM RS At tin INC", "phdt-data-dictionary-rs-attin-inc"),
         ("SIM RS At tin PNC", "phdt-data-dictionary-rs-attin-pnc"),
         ("SIM RS At tin BBL", "phdt-data-dictionary-rs-attin-bbl"),
         ("SIM RS Nirmala ANC", "phdt-data-dictionary-rs-nirmala-anc"),
         ("SIM RS Nirmala INC", "phdt-data-dictionary-rs-nirmala-inc"),
         ("SIM RS Nirmala PNC", "phdt-data-dictionary-rs-nirmala-pnc"),
         ("SIM RS Nirmala BBL", "phdt-data-dictionary-rs-nirmala-bbl"),
         ("SIM RS PKU ANC", "phdt-data-dictionary-rs-pku-anc"),
         ("SIM RS PKU BBL", "phdt-data-dictionary-rs-pku-bbl"),
         ("SIM RS MPH Hepatitis", "phdt-data-dictionary-rs-mph-hepatitis"),
         ("SIM RS Ummu Hani Hepatitis", "phdt-data-dictionary-rs-ummu-hani-hepatitis"),
         ("SIM RS PKU Hepatitis", "phdt-data-dictionary-rs-pku-hepatitis"),
         ("SIM RS Siaga Medika Hepatitis", "phdt-data-dictionary-rs-siaga-medika-hepatitis"),
         ("Kobo Modul ANC", "phdt-data-dictionary-kobo-modul-anc"),
         ("Kobo Modul INC", "phdt-data-dictionary-kobo-modul-inc"),
         ("Kobo Modul Neonatus", "phdt-data-dictionary-kobo-modul-neonatus"),
         ("Kobo Modul PNC", "phdt-data-dictionary-kobo-modul-pnc"),
         ("Kobo Buku KIA 1 - ANC", "phdt-data-dictionary-kobo-kia1-anc"),
         ("Kobo Buku KIA 2 - Luaran Kehamilan", "phdt-data-dictionary-kobo-kia2-luaran"),
         ("Kobo Buku KIA 3 - PNC", "phdt-data-dictionary-kobo-kia3-pnc"),
         ("Kobo Buku KIA 4 - Cadre", "phdt-data-dictionary-kobo-kia4-cadre"),
         ("Kobo Buku KIA 5 - Vaksinatorku", "phdt-data-dictionary-kobo-kia5-vaksinator"),
         ("Kobo Neonatus Outcome", "phdt-data-dictionary-kobo-neonatus-outcome"),
         ("Kobo Neonatus Outcome v2", "phdt-data-dictionary-kobo-neonatus-outcome-v2"),
         ("Kobo DDTK", "phdt-data-dictionary-kobo-ddtk")]
if nform: FORMS = FORMS[:nform]
SHORT = {"http://snomed.info/sct": "snomed", "http://loinc.org": "loinc", "http://terminology.kemkes.go.id/sp": "kemkes sp",
         "http://terminology.kemkes.go.id": "kemkes", "http://fhir.org/guides/who/anc-cds/CodeSystem/anc-custom-codes": "WHO anc-custom-codes",
         "http://hl7.org/fhir/sid/icd-10": "icd-10", "http://hl7.org/fhir/sid/icd-9-cm": "icd-9-cm", "http://sys-ids.kemkes.go.id/kfa": "kfa",
         "http://terminology.kemkes.go.id/CodeSystem/episodeofcare-type": "episodeofcare-type", "http://terminology.kemkes.go.id/CodeSystem/location-type": "location-type",
         "http://terminology.kemkes.go.id/CodeSystem/episodeofcare/ANC": "episodeofcare/ANC", "http://terminology.kemkes.go.id/CodeSystem/organization-type": "organization-type",
         "http://terminology.kemkes.go.id/CodeSystem/composition-type": "composition-type",
         "http://terminology.hl7.org/CodeSystem/v3-ObservationInterpretation": "v3-ObservationInterpretation"}
# Variabel raw per form: kolom file mentah (raw/*.md) kalau ada; kalau tidak ada file mentah = jumlah variabel di dictionary
RAW = {"Maternal Outcome": 12, "Raffle": 12, "SiGizi ANC": "sigizi-anc", "SITB TB 06": "sitb-tb06", "SITB TB 03 SO": "sitb-tb03-so",
       "SITB TB 03 RO": "sitb-tb03-ro", "SITB TB 04": "sitb-tb04", "SITB TB 16K": "sitb-tb16k", "MPDN Kematian Bayi": 37, "MPDN Kematian Ibu": 24,
       "ePus Pelayanan Pasien": 81, "ePus Kunjungan Ibu Hamil": 68, "ePus Laboratorium": 22, "ePus Rujukan Eksternal": 23, "ePus ANC": 123, "ePus INC": 93, "ePus PNC": 107, "ePus MTBS": 187, "ePus MTBM": 105, "ePus Tumbang Anak": 34, "ePus Tumbang DDTK": 38, "ePus Tumbang KPSP": 123, "ePus Tumbang TDD": 37, "ePus Tumbang TDL": 6, "ePus Tumbang KMPE": 14, "ePus Tumbang M-CHAT-R": 20, "Dapodik PAUD": 75, "ePus Tumbang GPPH": 10, "SITB TB 01": 82, "SITB TB 02": 22, "ELSMIL Ibu Hamil": 36, "ELSMIL Pasca Persalinan": 29, "ELSMIL Baduta": 38, "SIPTM": 60, "ASIK Skrining PTM": 67, "SiGizi Balita BNBA": 33, "SiGizi Balita Vitamin A": 14, "SiGizi Balita Mendapat PMT 2024": 30, "SiGizi Balita Pemantauan PMT 2024": 18, "SiGizi Balita ASI Eksklusif": 22, "SiGizi Balita MPASI": 28, "SiGizi PMT 2025 BB Tidak Naik - Pantau": 24, "SiGizi PMT 2025 BB Tidak Naik - Riwayat": 34, "SiGizi PMT 2025 BB Tidak Naik - Survey": 20, "SiGizi PMT 2025 BB Kurang - Pantau": 24, "SiGizi PMT 2025 BB Kurang - Riwayat": 34, "SiGizi PMT 2025 BB Kurang - Survey": 20, "SiGizi PMT 2025 Gizi Kurang - Pantau": 51, "SiGizi PMT 2025 Gizi Kurang - Riwayat": 34, "SiGizi PMT 2025 Gizi Kurang - Survey": 20, "SiGizi Ibu Nifas": 14, "SiGizi Kohort Ibu": 42, "ASIK CKG Bayi Baru Lahir (v2)": 35, "ASIK CKG Balita (v2)": 57, "ASIK CKG Dewasa Laki-laki": 123, "ASIK CKG Dewasa Perempuan": 130, "ASIK CKG Lansia (27 Apr 2026)": 188, "Informed Consent": 27, "SIHEPI Rekap 3e": 93, "eKohort ANC": 34, "eKohort INC": 84, "SIM RS Tripat ANC": 31, "SIM RS Tripat BBL (sheet 'INC BBL')": 36, "SIM RS Tripat PNC": 36, "SIM RS Narmada INC": 225, "SIM RS Narmada KIA": 70, "SIM RS Panti Nugroho ANC": 43, "SIM RS Panti Nugroho INC": 55, "SIM RS Panti Nugroho PNC": 85, "SIM RS Panti Nugroho BBL": 49, "SIM RS Panti Nugroho Diabetes Melitus": 19, "SIM RS Panti Nugroho Hipertensi": 40, "SIM RS Panti Nugroho Stroke": 35, "SIM RS Ummu Hani ANC": 33, "SIM RS Ummu Hani INC": 54, "SIM RS Ummu Hani PNC": 65, "SIM RS Ummu Hani BBL": 45, "SIM RS MPH ANC": 43, "SIM RS MPH INC": 54, "SIM RS MPH PNC": 59, "SIM RS MPH BBL": 73, "SIM RS MPH Diabetes Melitus": 44, "SIM RS MPH Hipertensi": 35, "SIM RS Siaga Medika ANC": 61, "SIM RS Siaga Medika INC": 58, "SIM RS Siaga Medika PNC": 71, "SIM RS Siaga Medika BBL": 64, "SIM RS PKU INC": 81, "SIM RS PKU PNC": 85, "SIM RS Goetoeng ANC": 21, "SIM RS Goetoeng INC": 35, "SIM RS Goetoeng PNC": 27, "SIM RS Goetoeng BBL": 34, "SIM RS Goetoeng Diabetes Melitus": 12, "SIM RS Goetoeng Hipertensi": 13, "SISMAL Regmal 1": 49, "SISMAL Validasi Indigenous": 14, "SIM RS Harapan Ibu ANC": 76, "SIM RS Harapan Ibu INC": 81, "SIM RS Harapan Ibu PNC": 86, "SIM RS Harapan Ibu BBL": 105, "SIM RS At tin ANC": 76, "SIM RS At tin INC": 81, "SIM RS At tin PNC": 86, "SIM RS At tin BBL": 109, "SIM RS Nirmala ANC": 76, "SIM RS Nirmala INC": 81, "SIM RS Nirmala PNC": 86, "SIM RS Nirmala BBL": 109, "SIM RS PKU ANC": 76, "SIM RS PKU BBL": 109, "SIM RS MPH Hepatitis": 40, "SIM RS Ummu Hani Hepatitis": 40, "SIM RS PKU Hepatitis": 40, "SIM RS Siaga Medika Hepatitis": 40, "Kobo Modul ANC": 75, "Kobo Modul INC": 108, "Kobo Modul Neonatus": 89, "Kobo Modul PNC": 118, "Kobo Buku KIA 1 - ANC": 404, "Kobo Buku KIA 2 - Luaran Kehamilan": 48, "Kobo Buku KIA 3 - PNC": 145, "Kobo Buku KIA 4 - Cadre": 83, "Kobo Buku KIA 5 - Vaksinatorku": 100, "Kobo Neonatus Outcome": 25, "Kobo Neonatus Outcome v2": 208, "Kobo DDTK": 20}
def raw_n(name):
    r = RAW[name]
    return r if isinstance(r, int) else len(fo.load_raw(f"{repo}/raw/{r}-kolom.md"))
def short(cs):
    cs = cs.strip()
    if cs in SHORT: return SHORT[cs]
    if cs.startswith("http://terminology.kemkes.go.id/CodeSystem/"): return "kemkes " + cs.rsplit("/", 1)[1]
    return cs
SP = "http://terminology.kemkes.go.id/sp"
data = {}
for name, f in FORMS:
    d = fo.load(f"{repo}/mapping/{f}.csv"); p, c, o = fo.build(d); data[name] = (p, c)
def fmt_forms(cnt):  # cnt: OrderedDict form->n
    return ", ".join(f"{f} ({n}x)" if n > 1 else f for f, n in cnt.items())
# --- frekuensi payload
pay = OrderedDict()
for name, (p, c) in data.items():
    for x in p:
        k = (x["res"], x["code"]); e = pay.setdefault(k, dict(disp=x["disp"], forms=OrderedDict()))
        e["forms"][name] = e["forms"].get(name, 0) + 1
L = ["# Frekuensi Payload (lintas form)", "", "Bagian dari konsolidasi [`output.md`](output.md). Dibuat otomatis, jangan diedit manual. Lihat juga [`frekuensi-code.md`](frekuensi-code.md).", "",
     "Frekuensi = di berapa form dipakai. Angka (Nx) = muncul N kali di form itu.", "", "| # | Resource | Code pembeda | Display | Dipakai di form | Frekuensi |", "|---|---|---|---|---|---|"]
for i, ((r, cd), e) in enumerate(pay.items(), 1):
    L.append(f"| {i} | {r} | {cd or '–'} | {e['disp'] or '–'} | {fmt_forms(e['forms'])} | {len(e['forms'])} |")
L += ["", "Variabel dictionary / BQ per payload: lihat `output/<form>.md` (link di [`output.md`](output.md)).", ""]
open(f"{outdir}/frekuensi-payload.md", "w", encoding="utf-8").write("\n".join(L))
# --- frekuensi code
cod = OrderedDict()
for name, (p, c) in data.items():
    for d in c:
        k = (d["code"], d["cs"].strip()); e = cod.setdefault(k, dict(disp=d["disp"], forms=OrderedDict()))
        e["forms"][name] = e["forms"].get(name, 0) + 1
L = ["# Frekuensi Code (lintas form)", "", "Bagian dari konsolidasi [`output.md`](output.md). Dibuat otomatis, jangan diedit manual. Lihat juga [`frekuensi-payload.md`](frekuensi-payload.md).", "",
     "Frekuensi = di berapa form code (code + CodeSystem) dipakai; angka (Nx) = muncul N kali di form itu.", "", "| # | Code | Display | CodeSystem | Dipakai di form | Frekuensi |", "|---|---|---|---|---|---|"]
for i, ((cd, cs), e) in enumerate(cod.items(), 1):
    L.append(f"| {i} | {cd} | {e['disp']} | {short(cs)} | {fmt_forms(e['forms'])} | {len(e['forms'])} |")
L.append("")
open(f"{outdir}/frekuensi-code.md", "w", encoding="utf-8").write("\n".join(L))
# --- tabel output.md
T = ["| Form | Variabel raw | Payload | Code | Code SP |", "|---|---|---|---|---|"]
tp = tc = ts = tr = 0
for name, (p, c) in data.items():
    sp = sum(1 for d in c if d["cs"].strip().rstrip("/") == SP); tp += len(p); tc += len(c); ts += sp; rn = raw_n(name); tr += rn
    T.append(f"| {name} | {rn} | {len(p)} | {len(c)} | {sp} |")
usp = sum(1 for (cd, cs) in cod if cs.rstrip("/") == SP)
T += [f"| **Total (non-unik)** | **{tr}** | **{tp}** | **{tc}** | **{ts}** |", f"| **Total unik** | – | **{len(pay)}** | **{len(cod)}** | **{usp}** |",
      f"| Selisih (dipakai ulang) | – | {tp-len(pay)} | {tc-len(cod)} | {ts-usp} |", ""]
bycs = OrderedDict()
for (cd, cs) in cod: bycs[cs] = bycs.get(cs, 0) + 1
T += ["| CodeSystem | Jumlah |", "|---|---|"] + [f"| {cs} | {n} |" for cs, n in sorted(bycs.items(), key=lambda x: -x[1])] + [f"| **Total** | **{len(cod)}** |", ""]
open(f"{outdir}/tabel.md", "w", encoding="utf-8").write("\n".join(T))
# payload per resource
tot = Counter(); 
for name, (p, c) in data.items(): tot.update(x["res"] for x in p)
uniq = Counter(r for (r, cd) in pay)
print(dict(tot)); print(dict(uniq))
print("form:", {n: (len(p), len(c)) for n, (p, c) in data.items()})
# --- payload per resource (kolom urut: total desc, seri sama ikut urutan lama)
OLD = ["Observation","ServiceRequest","DiagnosticReport","Specimen","Procedure","EpisodeOfCare","Condition","Encounter","Patient","QuestionnaireResponse","CarePlan","Organization","Practitioner","Coverage","Location","MedicationDispense","MedicationRequest","PractitionerRole","Group","Immunization","RelatedPerson"]
cols = sorted(tot, key=lambda r: (-tot[r], OLD.index(r) if r in OLD else 99))
M = ["| Form | " + " | ".join(cols) + " | Total |", "|---|" + "---|" * (len(cols) + 1)]
for name, (p, c) in data.items():
    cn = Counter(x["res"] for x in p)
    M.append(f"| {name} | " + " | ".join(str(cn[r]) if cn[r] else "–" for r in cols) + f" | {len(p)} |")
M.append("| **Total (non-unik)** | " + " | ".join(f"**{tot[r]}**" for r in cols) + f" | **{sum(tot.values())}** |")
M.append("| **Total unik** | " + " | ".join(f"**{uniq[r]}**" for r in cols) + f" | **{sum(uniq.values())}** |")
open(f"{outdir}/payload-per-resource.md", "w", encoding="utf-8").write("\n".join(M) + "\n")
