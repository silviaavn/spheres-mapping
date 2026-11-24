"""Siapkan dictionary form Kobo dari Kobo_-_Data_Dictionary.xlsx (satu sheet mapping = satu form tracker).
Pemakaian: python3 -I scripts/kobo_prepare.py <kobo.xlsx> <repo_dir>
Sheet 'Variabel ...' / 'tarikan ...' / 'Copy of ...' / 'Deprecated' / 'rencana INC' bukan dictionary final, dilewati."""
import importlib.util, json, os, sys, warnings
from collections import Counter
import openpyxl
warnings.filterwarnings("ignore")
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("ep", os.path.join(here, "epus_prepare.py"))
ep = importlib.util.module_from_spec(spec); spec.loader.exec_module(ep)
xlsx, repo = sys.argv[1], sys.argv[2]
wbk = openpyxl.load_workbook(xlsx, data_only=True)
# (slug, awalan sheet, nama form, tracker#, rename kolom)
F = [("kobo-modul-anc", "ANC Kobo", "Kobo Modul ANC", 83, {}),
     ("kobo-modul-inc", "INC Kobo", "Kobo Modul INC", 84, {}),
     ("kobo-modul-neonatus", "Neonatus Kobo", "Kobo Modul Neonatus", 85, {}),
     ("kobo-modul-pnc", "PNC Kobo", "Kobo Modul PNC", 86, {}),
     ("kobo-kia1-anc", "Mapping Kobo Buku KIA 1 - ANC", "Kobo Buku KIA 1 - ANC", 88, {"question/answer option": "Variables", "kobo xml value (answer option)": "Value Name", "kobo data column name": "Nama Column Raw"}),
     ("kobo-kia2-luaran", "Mapping Variable Buku KIA Entry", "Kobo Buku KIA 2 - Luaran Kehamilan", 89, {}),
     ("kobo-kia3-pnc", "Mapping Kobo Buku KIA 3 - PNC", "Kobo Buku KIA 3 - PNC", 90, {}),
     ("kobo-kia4-cadre", "Mapping Variabel Kobo Buku KIA", "Kobo Buku KIA 4 - Cadre", 91, {}),
     ("kobo-kia5-vaksinator", "Mapping Kobo Vaksinator", "Kobo Buku KIA 5 - Vaksinatorku", 92, {}),
     ("kobo-neonatus-outcome", "Neonatal Outcome Kobo", "Kobo Neonatus Outcome", 93, {}),
     ("kobo-neonatus-outcome-v2", "Neonatal Outcome v2", "Kobo Neonatus Outcome v2", 94, {"kategori": "Categories", "format": "Format/Value", "value": "Value Name"}),
     ("kobo-ddtk", "DDTK Kobo", "Kobo DDTK", 101, {}),
     ("kobo-data-bbl", "Data BBL Kobo", "Kobo Data BBL (belum ada baris tracker)", None, {})]
stats = {}
for slug, pre, nama, trk, ren in F:
    name = next(n for n in wbk.sheetnames if n.startswith(pre) and "tidak dipakai" not in n and not n.startswith(("Copy of", "Variab", "tarikan")) and "Vaksi" not in n.replace("Vaksinator (revised", "") or n.startswith(pre) and pre == "Mapping Kobo Vaksinator")
    ws = wbk[name]
    data = [["" if c is None else str(c) for c in r] for r in ws.iter_rows(values_only=True)]
    hdr = [ren.get(" ".join(h.split()).lower(), h).strip() for h in data[0]]
    ri, vi = hdr.index("Resource"), hdr.index("Variables")
    body = [r for r in data[1:] if any(c.strip() for c in r)]
    body = [r for r in body if not (len(r) > vi and r[vi].strip().replace(".", "", 1).isdigit() and not any(c.strip() for c in r[ri:ri + 3]))]
    wb = openpyxl.Workbook(); w = wb.active; w.title = "s"; w.append(hdr)
    for r in body: w.append([c if c != "" else None for c in r])
    cfg = dict(slug=slug, nama=nama, sheet="s", hdr=0, var="Variables", raw="Nama Column Raw" if "Nama Column Raw" in hdr else None,
               bq="Nama Column BQ" if "Nama Column BQ" in hdr else None, tracker=trk, ref=None, ref_label=nama)
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
    print(f"{slug:26s} #{str(trk):4s} {name[:30]:30s} baris {s['baris_csv']:5d} var {s['var_unik']:4d}/{s['var_baris']:4d} payload {s['payload']:4d} code {s['code']:4d}")
json.dump(stats, open("/home/claude/work/kobo-stats.json", "w"), ensure_ascii=False, indent=1)
