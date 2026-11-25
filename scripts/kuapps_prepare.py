"""Siapkan dictionary KuApps: BidanKu (KuApps_Reborn_Variable_and_FHIR_Mapping.xlsx) dan Kuapps Spheres (Mapping_KuApps_SPHERES.xlsx).
Pemakaian: python3 -I scripts/kuapps_prepare.py <reborn.xlsx> <spheres.xlsx> <repo_dir> [genomics.xlsx]
Sheet IFIV / Summary / Gambar / List Skrining bukan dictionary (testing / daftar) dan dilewati.
Sheet Tambah Pasien dst. = baris tracker #284–290 (ditambahkan 2026-11-25)."""
import importlib.util, json, os, sys, warnings
from collections import Counter
import openpyxl
warnings.filterwarnings("ignore")
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("ep", os.path.join(here, "epus_prepare.py"))
ep = importlib.util.module_from_spec(spec); spec.loader.exec_module(ep)
reborn, spheres, repo = sys.argv[1], sys.argv[2], sys.argv[3]
genomics = sys.argv[4] if len(sys.argv) > 4 else None   # Genomics_SPHERES_Data_Dictionary_.xlsx
REN = {"section": "Categories", "nama skrining": "Categories", "variable": "Variables", "value": "Value Name", "formula": "Format/Value",
       "system": "CodeSystem", "keterangan": "Definisi Operasional", "note": "Definisi Operasional",
       "categories (halaman)": "Categories", "data type (string, int, dsb)": "Data Type",
       "format/value (yyyy-mm-dd, dsb)": "Format/Value", "definisi operasional (logic)": "Definisi Operasional", "tanggaaaaa": "Categories"}
# (slug, workbook, sheet, nama, tracker#, baris header)
F = [("kuapps-bidanku-anc", "r", "PYD-ANC", "KuApps BidanKu - ANC", 106, 1),
     ("kuapps-bidanku-pnc", "r", "PYD-PNC", "KuApps BidanKu - PNC", 107, 1),
     ("kuapps-bidanku-bbl", "r", "PYD-BBL", "KuApps BidanKu - BBL", 108, 1),
     ("kuapps-bidanku-bayi", "r", "PYD-Bayi", "KuApps BidanKu - Bayi", 109, 1),
     ("kuapps-bidanku-anak", "r", "PYD-Anak", "KuApps BidanKu - Anak", 110, 1),
     ("kuapps-bidanku-usekre", "r", "PYD-Anak Usekre (6-18 tahun)", "KuApps BidanKu - Anak Usia Sekolah dan Remaja", 111, 1),
     ("kuapps-bidanku-dewasa", "r", "PYD Dewasa", "KuApps BidanKu - Dewasa", 112, 1),
     ("kuapps-bidanku-lansia", "r", "PYD Lansia", "KuApps BidanKu - Lansia", 113, 1),
     ("kuapps-spheres-ht", "s", "Form Caregap HT", "Kuapps Spheres - HT", 114, 1),
     ("kuapps-spheres-dm", "s", "Form Caregap DM", "Kuapps Spheres - DM", 115, 1),
     ("kuapps-spheres-tb", "s", "Form Caregap TB", "Kuapps Spheres - TB", 116, 1),
     ("genomics-tb", "g", "TB Mapping", "Genomics - TB", 118, 1),
     ("genomics-klebsiella", "g", "Klebsiella Mapping", "Genomics - Klebsiella", 119, 1),
     ("genomics-dengue", "g", "Dengue Mapping", "Genomics - Dengue", 120, 1),
     ("kuapps-bidanku-tambah-pasien", "r", "Tambah Pasien", "KuApps BidanKu - Tambah Pasien", 284, 1),
     ("kuapps-bidanku-daftar-kehamilan", "r", "Daftar Kehamilan", "KuApps BidanKu - Daftar Kehamilan", 285, 1),
     ("kuapps-bidanku-luaran-kehamilan", "r", "Luaran Kehamilan", "KuApps BidanKu - Luaran Kehamilan", 286, 1),
     ("kuapps-bidanku-phbs", "r", "PHBS", "KuApps BidanKu - PHBS", 287, 1),
     ("kuapps-bidanku-skrining-rt", "r", "Skrining Rumah Tangga", "KuApps BidanKu - Skrining Rumah Tangga", 288, 1),
     ("kuapps-bidanku-imunisasi", "r", "Imunisasi", "KuApps BidanKu - Imunisasi", 289, 3),
     ("kuapps-bidanku-kumpulan-skrining", "r", "Kumpulan Skrinning", "KuApps BidanKu - Kumpulan Skrinning", 290, 1)]
wbs = {"r": openpyxl.load_workbook(reborn, data_only=True), "s": openpyxl.load_workbook(spheres, data_only=True)}
if genomics: wbs["g"] = openpyxl.load_workbook(genomics, data_only=True)
else: F = [f for f in F if f[1] != "g"]
stats = {}
for slug, w, sheet, nama, trk, hrow in F:
    name = next(n for n in wbs[w].sheetnames if n.strip() == sheet.strip())
    data = [["" if c is None else str(c) for c in r] for r in wbs[w][name].iter_rows(values_only=True)]
    hdr = [" ".join(h.split()) for h in data[hrow - 1]]
    hdr = [REN.get(h.lower(), h) for h in hdr]
    sub = next((i for i, h in enumerate(hdr) if h.lower().startswith("sub variables")), None)
    vi = hdr.index("Variables"); ri = hdr.index("Resource")
    body = [r + [""] * (len(hdr) - len(r)) for r in data[hrow:] if any(c.strip() for c in r)]
    if sub is not None:                       # DM / HT: anak pertanyaan matriks dipakai sebagai nama variabel
        for r in body:
            if r[sub].strip(): r[vi] = r[sub]
    for r in body:                            # typo di sumber
        pi = hdr.index("Path")
        r[pi] = r[pi].replace(".valuableCodeableConcept", ".valueCodeableConcept")
    shifted = 0
    for r in body:                            # baris yang kehilangan 1 kolom di kiri (Ya/Tidak masuk kolom Resource)
        if r[ri + 1].strip() and r[ri + 2].startswith(r[ri + 1].strip() + ".") and not r[ri].strip().startswith(r[ri + 1].strip()) and not r[ri - 1].strip():
            r[ri - 1], r[ri:] = r[ri], r[ri + 1:] + [""]
            shifted += 1
    if shifted: print("  baris digeser:", slug, shifted)
    body = [r for r in body if not (r[vi].strip().replace(".", "", 1).isdigit() and not any(c.strip() for c in r[ri:ri + 3]))]
    wb = openpyxl.Workbook(); ws = wb.active; ws.title = "s"; ws.append(hdr)
    for r in body: ws.append([c if c != "" else None for c in r])
    cfg = dict(slug=slug, nama=nama, sheet="s", hdr=0, var="Variables", raw=None, bq=None, tracker=trk, ref=None, ref_label=nama)
    rows, log = ep.prepare(cfg, wb, None)
    ep.SINGLETON = {"Patient", "Encounter"}
    blocks, payloads = ep.flag(rows)
    keep = [r for r in rows if any(r[c] for c in ep.OUT_COLS[:15])]
    ep.write_csv(f"{repo}/mapping/phdt-data-dictionary-{slug}.csv", keep)
    v = [r["Variables"] for r in keep if r["Variables"]]
    stats[slug] = dict(nama=nama, sheet=name, tracker=trk, baris_csv=len(keep), var_unik=len(set(v)), var_baris=len(v), payload=len(payloads),
        code=sum(1 for r in keep if r["jumlah code"] == "1"), payload_per_resource=dict(Counter(x["res"] for x in payloads)),
        tidak_dihitung=dict(Counter(f'{x["res"]}: {x["reason"]}' for x in blocks if x["reason"])), resource_fix=Counter(map(tuple, log["resource_fix"])).most_common(4))
    s = stats[slug]
    print(f"{slug:34s} #{str(trk):4s} baris {s['baris_csv']:5d} var {s['var_unik']:4d}/{s['var_baris']:4d} payload {s['payload']:4d} code {s['code']:4d}")
json.dump(stats, open("/home/claude/work/kuapps-stats.json", "w"), ensure_ascii=False, indent=1)
