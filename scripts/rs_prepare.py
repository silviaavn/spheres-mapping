"""Siapkan dictionary SIM RS (PHDT_Data_Rumah_Sakit.xlsx): satu sheet mapping = satu form di tracker (#128-#236).
Pemakaian: python3 -I scripts/rs_prepare.py <rs.xlsx> <repo_dir>
Sheet 'Template' generik (tidak terikat RS) tetap dibuat dictionary-nya tetapi tidak masuk konsolidasi (tracker=None)."""
import importlib.util, json, os, sys, warnings
from collections import Counter
import openpyxl
warnings.filterwarnings("ignore")
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("ep", os.path.join(here, "epus_prepare.py"))
ep = importlib.util.module_from_spec(spec); spec.loader.exec_module(ep)
xlsx, repo = sys.argv[1], sys.argv[2]
wbk = openpyxl.load_workbook(xlsx, data_only=True)
# (slug, awalan nama sheet, nama form, tracker#)
F = [("tripat-anc", "Mapping ANC Tripat", "Tripat ANC", 228), ("tripat-bbl", "Mapping INC BBL Tripat", "Tripat BBL (sheet 'INC BBL')", 231),
 ("tripat-pnc", "Mapping PNC Tripat", "Tripat PNC", 230),
 ("narmada-inc", "Mapping INC Narmada", "Narmada INC", 219), ("narmada-kia", "Mapping KIA Narmada", "Narmada KIA", 222),
 ("panti-nugroho-anc", "Mapping ANC Panti Nugroho", "Panti Nugroho ANC", 200), ("panti-nugroho-inc", "Mapping INC RSUD Panti Nugroho", "Panti Nugroho INC", 201),
 ("panti-nugroho-pnc", "Mapping PNC Panti Nugroho", "Panti Nugroho PNC", 202), ("panti-nugroho-bbl", "Mapping BBL Panti Nugroho", "Panti Nugroho BBL", 203),
 ("panti-nugroho-dm", "DM Panti Nugroho", "Panti Nugroho Diabetes Melitus", 205), ("panti-nugroho-ht", "HT Panti Nugroho", "Panti Nugroho Hipertensi", 206),
 ("panti-nugroho-stroke", "Stroke Panti Nugroho", "Panti Nugroho Stroke", 207),
 ("ummu-hani-anc", "Mapping ANC RS Ummu Hani", "Ummu Hani ANC", 173), ("ummu-hani-inc", "Mapping INC RS Ummu Hani", "Ummu Hani INC", 174),
 ("ummu-hani-pnc", "Mapping PNC RS Ummu Hani", "Ummu Hani PNC", 175), ("ummu-hani-bbl", "Mapping BBL RS Ummu Hani", "Ummu Hani BBL", 176),
 ("mph-anc", "Mapping ANC RS MPH", "MPH ANC", 155), ("mph-inc", "Mapping INC RS MPH", "MPH INC", 156), ("mph-pnc", "Mapping PNC RS MPH", "MPH PNC", 157),
 ("mph-bbl", "Mapping BBL RS MPH", "MPH BBL", 158), ("mph-dm", "DM MPH", "MPH Diabetes Melitus", 160), ("mph-ht", "HT MPH", "MPH Hipertensi", 161),
 ("siaga-medika-anc", "Mapping ANC Siaga Medika", "Siaga Medika ANC", 146), ("siaga-medika-inc", "Mapping INC Siaga Medika", "Siaga Medika INC", 147),
 ("siaga-medika-pnc", "Mapping PNC Siaga Medika", "Siaga Medika PNC", 148), ("siaga-medika-bbl", "Mapping BBL Siaga Medika", "Siaga Medika BBL", 149),
 ("pku-inc", "Mapping INC PKU", "PKU INC", 183), ("pku-pnc", "Mapping PNC PKU", "PKU PNC", 184),
 ("goetoeng-anc", "Mapping ANC Goeteng", "Goetoeng ANC", 191), ("goetoeng-inc", "Mapping INC Goeteng", "Goetoeng INC", 192),
 ("goetoeng-pnc", "Mapping PNC Goeteng", "Goetoeng PNC", 193), ("goetoeng-bbl", "Mapping BBL Goeteng", "Goetoeng BBL", 194),
 ("goetoeng-dm", "Mapping DM Goeteng", "Goetoeng Diabetes Melitus", 196), ("goetoeng-ht", "Mapping HT Goeteng", "Goetoeng Hipertensi", 197),
 ("template-anc", "Mapping ANC Template", "Template ANC", None), ("template-inc", "Mapping INC Template", "Template INC", None),
 ("template-pnc", "Mapping PNC Template", "Template PNC", None), ("template-bbl-neo", "Mapping BBL (neo) Template", "Template BBL (neo)", None),
 ("template-bbl-inc", "Mapping BBL (INC) Template", "Template BBL (INC)", None), ("template-tb", "TB Template", "Template TB", None),
 ("template-hepb", "HepB (Template)", "Template Hepatitis B", None)]
stats = {}
for slug, pre, nama, trk in F:
    name = next(n for n in wbk.sheetnames if n.strip().replace("✅", "").strip().startswith(pre) and not n.lower().startswith("variab"))
    ws = wbk[name]
    data = [["" if c is None else str(c) for c in r] for r in ws.iter_rows(values_only=True)]
    hdr = [h.strip() for h in data[0]]
    ri, vi = hdr.index("Resource"), hdr.index("Variables")
    body = [r for r in data[1:] if any(c.strip() for c in r)]
    body = [r for r in body if not (len(r) > vi and r[vi].strip().replace(".", "", 1).isdigit() and not any(c.strip() for c in r[ri:ri + 3]))]
    wb = openpyxl.Workbook(); w = wb.active; w.title = "s"; w.append(hdr[:max(ri + 6, 16)] if False else hdr)
    for r in body: w.append([c if c != "" else None for c in r])
    cfg = dict(slug=slug, nama=nama, sheet="s", hdr=0, var="Variables", raw="Nama Column Raw" if "Nama Column Raw" in hdr else None,
               bq="Nama Column BQ" if "Nama Column BQ" in hdr else None, tracker=trk, ref=None, ref_label=nama)
    rows, log = ep.prepare(cfg, wb, None)
    ep.SINGLETON = {"Patient", "Encounter"}
    blocks, payloads = ep.flag(rows)
    keep = [r for r in rows if any(r[c] for c in ep.OUT_COLS[:15])]
    ep.write_csv(f"{repo}/mapping/phdt-data-dictionary-rs-{slug}.csv", keep)
    v = [r["Variables"] for r in keep if r["Variables"]]
    stats[slug] = dict(nama=nama, sheet=name, tracker=trk, baris_csv=len(keep), var_unik=len(set(v)), var_baris=len(v), payload=len(payloads),
        code=sum(1 for r in keep if r["jumlah code"] == "1"), payload_per_resource=dict(Counter(x["res"] for x in payloads)),
        tidak_dihitung=dict(Counter(f'{x["res"]}: {x["reason"]}' for x in blocks if x["reason"])), resource_fix=Counter(map(tuple, log["resource_fix"])).most_common(4))
    s = stats[slug]
    print(f"{slug:22s} #{str(trk):4s} baris {s['baris_csv']:5d} var {s['var_unik']:4d}/{s['var_baris']:4d} payload {s['payload']:4d} code {s['code']:4d}")
json.dump(stats, open("/home/claude/work/rs-stats.json", "w"), ensure_ascii=False, indent=1)
