"""Siapkan dictionary dari CSV PHDT (SITB TB 01/02, Elsmil x3, SIPTM, ASIK PTM) -> mapping/phdt-data-dictionary-<slug>.csv.
Pemakaian: python3 -I scripts/csvform_prepare.py <dir_csv> <repo_dir>
CSV dibungkus jadi workbook in-memory supaya bisa lewat epus_prepare.prepare()."""
import csv, glob, importlib.util, json, os, sys
from collections import Counter
import openpyxl
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("ep", os.path.join(here, "epus_prepare.py"))
ep = importlib.util.module_from_spec(spec); spec.loader.exec_module(ep)
src, repo = sys.argv[1], sys.argv[2]
def load(key):
    f = [x for x in glob.glob(f"{src}/*.csv") if key in x][0]
    return list(csv.reader(open(f, encoding="utf-8-sig", newline="")))
def book(header, rows):
    wb = openpyxl.Workbook(); ws = wb.active; ws.title = "s"
    ws.append(header)
    for r in rows: ws.append([c if c != "" else None for c in r])
    return wb
# (slug, nama, csv-key, baris awal, baris akhir (1-based, inklusif), tracker, ref, ref_label)
FORMS = [
 ("sitb-tb01", "SITB - TB 01 (Kartu Pengobatan Pasien)", "TB_01", 2, None, 50, 78, "SITB | TB 01"),
 ("sitb-tb02", "SITB - TB 02 (Kartu Identitas Pasien)", "TB_02", 2, None, 51, 22, "SITB | TB 02"),
 ("elsmil-ibu-hamil", "ELSMIL Ibu Hamil", "Elsmil", 2, 483, 121, 37, "ELSMIL | Ibu Hamil"),
 ("elsmil-pasca-persalinan", "ELSMIL Pasca Persalinan", "Elsmil", 484, 810, 122, 29, "ELSMIL | Pasca Persalinan"),
 ("elsmil-baduta", "ELSMIL Baduta", "Elsmil", 811, None, 123, 42, "ELSMIL | Baduta"),
 ("siptm", "SIPTM", "SIPTM", 2, None, 237, None, "SIPTM (baru, tidak ada di PHDT)"),
 ("asik-skrining-ptm", "ASIK - Data Skrining PTM", "ASIK_PTM", 2, None, 42, 64, "ASIK | Data Skrining PTM"),
]
stats = {}
for slug, nama, key, a, b, trk, ref, lab in FORMS:
    data = load(key); hdr = data[0]
    body = data[a - 1:(b or len(data))]
    cfg = dict(slug=slug, nama=nama, sheet="s", hdr=0, var="Variables", raw="Nama Column Raw",
               bq="Nama Column BQ" if "Nama Column BQ" in [h.strip() for h in hdr] else None,
               tracker=trk, ref=ref, ref_label=lab)
    rows, log = ep.prepare(cfg, book(hdr, body), None)
    blocks, payloads = ep.flag(rows)
    keep = [r for r in rows if any(r[c] for c in ep.OUT_COLS[:15])]
    ep.write_csv(f"{repo}/mapping/phdt-data-dictionary-{slug}.csv", keep)
    v = [r["Variables"] for r in keep if r["Variables"]]
    raw = {r["Nama Column Raw"] for r in keep if r["Nama Column Raw"]}
    stats[slug] = dict(nama=nama, tracker=trk, ref=ref, ref_label=lab, baris_csv_asal=f"{a}-{b or len(data)}",
        baris_csv=len(keep), var_unik=len(set(v)), var_baris=len(v), raw_unik=len(raw),
        payload=len(payloads), code=sum(1 for r in keep if r["jumlah code"] == "1"),
        payload_per_resource=dict(Counter(x["res"] for x in payloads)),
        tidak_dihitung_res=dict(Counter(f'{x["res"]}: {x["reason"]}' for x in blocks if x["reason"])),
        kode_tanggal=len(log["kode_tanggal"]), resource_fix=Counter(map(tuple, log["resource_fix"])).most_common(6),
        resource_dari_path=log["resource_dari_path"])
    s = stats[slug]
    print(f"{slug:24s} baris {s['baris_csv']:5d} var unik {s['var_unik']:4d} (baris {s['var_baris']:4d}, ref {ref}) "
          f"raw {s['raw_unik']:4d} payload {s['payload']:4d} code {s['code']:4d}")
json.dump(stats, open("/home/claude/work/csvform-stats.json", "w"), ensure_ascii=False, indent=1)
