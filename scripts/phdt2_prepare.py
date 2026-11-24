"""Siapkan dictionary: ASIK CKG (xlsx, beberapa versi), Informed Consent, SIHEPI Rekap 3e, eKohort ANC/INC (CSV).
Pemakaian: python3 -I scripts/phdt2_prepare.py <dir_csv> <ckg.xlsx> <repo_dir>
Tiap entri FORMS menghasilkan mapping/phdt-data-dictionary-<slug>.csv. `main` = versi yang dipakai di konsolidasi."""
import csv, glob, importlib.util, json, os, sys, warnings
from collections import Counter
import openpyxl
warnings.filterwarnings("ignore")
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("ep", os.path.join(here, "epus_prepare.py"))
ep = importlib.util.module_from_spec(spec); spec.loader.exec_module(ep)
src, xlsx, repo = sys.argv[1], sys.argv[2], sys.argv[3]
ckg = openpyxl.load_workbook(xlsx, data_only=True)   # data_only: kolom 'Variabel v2' berisi rumus
def load(key):
    f = [x for x in glob.glob(f"{src}/*.csv") if key in x][0]
    return list(csv.reader(open(f, encoding="utf-8-sig", newline="")))
def book(header, rows):
    wb = openpyxl.Workbook(); ws = wb.active; ws.title = "s"
    ws.append(header)
    for r in rows: ws.append([c if c != "" else None for c in r])
    return wb
# (slug, nama, jenis, sumber, baris awal, baris akhir, tracker#, ref, ref_label, main, versi)
FORMS = [
 ("asik-ckg-bbl", "ASIK - CKG Bayi Baru Lahir (versi 2, tarikan baru)", "xlsx", "CKG Bayi Baru Lahir 2", 2, None, 43, 33, "ASIK | CKG - Bayi Baru Lahir", True, "v2"),
 ("asik-ckg-bbl-v1", "ASIK - CKG Bayi Baru Lahir (versi 1)", "xlsx", "CKG Bayi Baru Lahir", 2, None, 43, 33, "ASIK | CKG - Bayi Baru Lahir", False, "v1"),
 ("asik-ckg-balita", "ASIK - CKG Balita dan Anak Pra-Sekolah (versi 2, tarikan baru)", "xlsx", "Sheet9", 4, None, 44, 59, "ASIK | CKG Balita dan Anak Pra-Sekolah", True, "v2"),
 ("asik-ckg-balita-v1", "ASIK - CKG Balita dan Anak Pra-Sekolah (versi 1)", "xlsx", "CKG Balita dan Anak Pra-Sekolah", 4, None, 44, 59, "ASIK | CKG Balita dan Anak Pra-Sekolah", False, "v1"),
 ("asik-ckg-dewasa-laki", "ASIK - CKG Dewasa Laki-laki", "xlsx", "CKG Dewasa Laki-laki", 2, None, 46, 132, "ASIK | CKG - Dewasa Laki-laki", True, "1 versi"),
 ("asik-ckg-dewasa-perempuan", "ASIK - CKG Dewasa Perempuan", "xlsx", "CKG Dewasa Perempuan", 2, None, 47, 132, "ASIK | CKG - Dewasa Perempuan", True, "1 versi"),
 ("asik-ckg-lansia", "ASIK - CKG Lansia (versi 27 April 2026)", "xlsx", "CKG Lansia 27 April 2026", 2, None, 48, 180, "ASIK | CKG - Lansia", True, "27 Apr 2026"),
 ("asik-ckg-lansia-2026", "ASIK - CKG Lansia (versi 2026)", "xlsx", "CKG Lansia 2026", 2, None, 48, 180, "ASIK | CKG - Lansia", False, "2026"),
 ("asik-ckg-lansia-2025", "ASIK - CKG Lansia (versi 2025)", "xlsx", "CKG Lansia 2025", 2, None, 48, 180, "ASIK | CKG - Lansia", False, "2025"),
 ("informed-consent", "Informed Consent", "csv", "IC_1", 2, None, 78, 28, "Informed Consent | Informed Consent", True, ""),
 ("sihepi-rekap-3e", "SiHepi - Form Rekap 3e (Registrasi Ibu Hamil Triple Eliminasi)", "csv", "SIHEPI", 2, None, 49, 115, "SIHEPI | Rekap 3e", True, ""),
 ("ekohort-anc", "eKohort - Pelayanan Ibu ANC (Final Format)", "csv", "ANC_Final", 2, None, 74, 36, "eKohort | ANC", True, "Final Format"),
 ("ekohort-anc-lama", "eKohort - Pelayanan Ibu ANC (file eKohort lama)", "csv", "eKohort.csv", 2, 725, 74, 36, "eKohort | ANC", False, "file lama"),
 ("ekohort-inc", "eKohort - Pelayanan Ibu Bersalin (INC)", "csv", "eKohort.csv", 726, None, 77, 85, "eKohort | INC", True, ""),
]
stats = {}
shifted = []
for slug, nama, kind, key, a, b, trk, ref, lab, main, ver in FORMS:
    if kind == "xlsx":
        ws = ckg[key]; data = [["" if c is None else str(c) for c in r] for r in ws.iter_rows(values_only=True)]
    else:
        data = load(key)
    hdr = [h.strip() for h in data[0]]
    body = data[a - 1:(b or len(data))]
    body = [r for r in body if not (r and r[0].startswith("Contoh Data"))]    # baris "Contoh Data: <url>" bukan variabel
    # baris ujung sheet yang hanya berisi angka (jumlah variabel, mis. "58") bukan variabel
    vi = hdr.index("Variables")
    assert "Resource" in hdr
    body = [r for r in body if not (len(r) > vi and r[vi].strip().replace(".", "", 1).isdigit() and not any(c.strip() for j, c in enumerate(r) if hdr.index("Resource") <= j <= hdr.index("Resource") + 2))]
    # file eKohort ANC Final Format: beberapa baris kehilangan 2 kolom (Definisi Operasional, Agregat/Individu) -> geser kanan
    ri = hdr.index("Resource") if "Resource" in hdr else None
    if ri:
        fixed = []
        for r in body:
            r = list(r) + [""] * (ri + 2 - len(r))
            if r[ri - 2] and r[ri - 1].startswith(r[ri - 2] + ".") and not (r[ri] and r[ri + 1].startswith(r[ri] + ".")):
                r = r[:ri - 2] + ["", ""] + r[ri - 2:]
                shifted.append(slug)
            fixed.append(r)
        body = fixed
    cfg = dict(slug=slug, nama=nama, sheet="s", hdr=0, var="Variables", raw="Nama Column Raw" if ("Nama Column Raw" in hdr and not slug.startswith(("asik-ckg-dewasa", "asik-ckg-lansia"))) else None,
               bq="Nama Column BQ" if "Nama Column BQ" in hdr else None, tracker=trk, ref=ref, ref_label=lab)
    rows, log = ep.prepare(cfg, book(data[0], body), None)
    # CKG: baris QuestionnaireResponse berselang-seling dengan blok Observation, tetapi hanya 1 QR per form
    # Lansia: QR terpisah per bagian -> 1 QR per header QuestionnaireResponse.questionnaire (blok QR tanpa header = lanjutan)
    lansia = slug.startswith("asik-ckg-lansia")
    ep.SINGLETON = {"Patient", "Encounter", "QuestionnaireResponse"} if slug.startswith("asik-ckg") and not lansia else {"Patient", "Encounter"}
    blocks, payloads = ep.flag(rows)
    if lansia:
        for b in blocks:
            if b["res"] == "QuestionnaireResponse" and not b["reason"] and not any(r["Path"].startswith("QuestionnaireResponse.questionnaire") for r in b["rows"]):
                b["first"]["jumlah instance"] = ""
                b["reason"] = "lanjutan QR"
        payloads = [b for b in payloads if not b["reason"]]
    keep = [r for r in rows if any(r[c] for c in ep.OUT_COLS[:15])]
    ep.write_csv(f"{repo}/mapping/phdt-data-dictionary-{slug}.csv", keep)
    v = [r["Variables"] for r in keep if r["Variables"]]
    stats[slug] = dict(nama=nama, tracker=trk, ref=ref, main=main, versi=ver, sumber=key, baris_csv=len(keep),
        var_unik=len(set(v)), var_baris=len(v), payload=len(payloads), code=sum(1 for r in keep if r["jumlah code"] == "1"),
        payload_per_resource=dict(Counter(x["res"] for x in payloads)),
        tidak_dihitung=dict(Counter(f'{x["res"]}: {x["reason"]}' for x in blocks if x["reason"])),
        kode_tanggal=len(log["kode_tanggal"]), resource_dari_path=log["resource_dari_path"],
        resource_fix=Counter(map(tuple, log["resource_fix"])).most_common(6))
    s = stats[slug]
    print(f"{slug:26s} baris {s['baris_csv']:5d} var unik {s['var_unik']:4d} (baris {s['var_baris']:4d}, ref {ref}) payload {s['payload']:4d} code {s['code']:4d} {'MAIN' if main else ''}")
print("baris digeser (kolom hilang):", Counter(shifted))
json.dump(stats, open("/home/claude/work/phdt2-stats.json", "w"), ensure_ascii=False, indent=1)
