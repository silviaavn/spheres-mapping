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
         ("ePus Tumbang DDTK", "phdt-data-dictionary-epus-tumbang-ddtk")]
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
       "ePus Pelayanan Pasien": 81, "ePus Kunjungan Ibu Hamil": 68, "ePus Laboratorium": 22, "ePus Rujukan Eksternal": 23, "ePus ANC": 123, "ePus INC": 93, "ePus PNC": 107, "ePus MTBS": 187, "ePus MTBM": 105, "ePus Tumbang Anak": 34, "ePus Tumbang DDTK": 38}
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
