"""Siapkan dictionary SISMAL (Malaria) dari PHDT_SISMAL.xlsx -> mapping/phdt-data-dictionary-<slug>.csv
Pemakaian: python3 -I scripts/sismal_prepare.py <PHDT_SISMAL.xlsx> <repo_dir>
Memakai epus_prepare.prepare()/flag() (aturan sama dengan form PHDT lain). Sheet dibaca dengan data_only=True
karena kolom Resource di Mapping Regmal 1 berisi rumus (cache nilai dipakai).

Perbaikan otomatis (semua dicatat di revisi.md bagian SISMAL, bisa diulang dari file asli):
  - Regmal 1: blok ServiceRequest (sheet baris 427-446) bergeser 1 kolom ke kanan (kolom K-P) -> digeser balik.
  - Typo path: valuecodeableConcept -> valueCodeableConcept, valueinteger -> valueInteger;
    typo code: 'ofiicial' -> official, 'social history' -> social-history;
    path 'Organization.address.extension.url' di dalam blok Location -> 'Location.address.extension.url'.
  - Validasi Indigenous: Location "Alamat Asal Penularan" dibuat dari isian form -> dihitung 1 payload (aturan Location).
Tidak diproses:
  - Mapping Verif Uji Silang: isinya masih salinan template TB-TPT (tidak ada variabel uji silang malaria).
  - Knowlesi Fasyankes dan Knowlesi Lab: baru ada daftar variabel, belum ada sheet mapping."""
import importlib.util, json, os, re, sys, warnings
from collections import Counter
import openpyxl
warnings.filterwarnings("ignore")
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("ep", os.path.join(here, "epus_prepare.py"))
ep = importlib.util.module_from_spec(spec); spec.loader.exec_module(ep)
xlsx, repo = sys.argv[1], sys.argv[2]
wb = openpyxl.load_workbook(xlsx, data_only=True)
# (slug, nama, sheet mapping, tracker #)
FORMS = [
    ("sismal-regmal1", "SISMAL - Regmal 1", "Mapping Regmal 1", 64),
    ("sismal-validasi-indigenous", "SISMAL - Validasi Kasus Indigenous", "Mapping Indigeneous", None),
]
PATH_FIX = [("valuecodeableConcept", "valueCodeableConcept"), ("valueinteger", "valueInteger")]
CODE_FIX = {"ofiicial": "official", "social history": "social-history"}


def unshift(ws):
    """Geser balik baris yang kolom K-P-nya bergeser 1 ke kanan (J kosong, K = nama resource, L = path resource itu)."""
    n = []
    for r in range(2, ws.max_row + 1):
        j, k, l = (ws.cell(r, c).value for c in (10, 11, 12))
        if j in (None, "") and isinstance(k, str) and re.match(r"^[A-Z][A-Za-z]+$", k) and isinstance(l, str) \
                and l.startswith(k + "."):
            for c in range(10, 16):
                ws.cell(r, c).value = ws.cell(r, c + 1).value
            ws.cell(r, 16).value = None
            n.append(r)
    return n


stats = {}
for slug, nama, sheet, trk in FORMS:
    ws = wb[sheet]
    shifted = unshift(ws)
    cfg = dict(slug=slug, nama=nama, sheet=sheet, hdr=0, var="Variables", raw="Nama Column Raw",
               bq="Nama Column BQ", tracker=trk, ref=None, ref_label="SISMAL")
    rows, log = ep.prepare(cfg, wb, None)
    fixes = Counter()
    for r in rows:
        # sisa template blok Berat badan: kata tipe data (number/string/date) nyasar di kolom Variables -> pindah ke Data Type
        if r["Variables"] in ("number", "string", "date") and r["Resource"] == "Observation":
            if not r["Data Type"]:
                r["Data Type"] = r["Variables"]
            r["Variables"] = ""; fixes["sisa tipe data di kolom Variables dibersihkan"] += 1
        for a, b in PATH_FIX:
            if a in r["Path"]:
                r["Path"] = r["Path"].replace(a, b); fixes[f"path {a} -> {b}"] += 1
        if r["Code"] in CODE_FIX:
            fixes[f"code {r['Code']} -> {CODE_FIX[r['Code']]}"] += 1; r["Code"] = CODE_FIX[r["Code"]]
        if r["Resource"] == "Location" and r["Path"].startswith("Organization."):
            r["Path"] = "Location." + r["Path"].split(".", 1)[1]; fixes["path Organization.* di blok Location -> Location.*"] += 1
    blocks, payloads = ep.flag(rows)
    # Location yang dibuat dari isian form (bukan lookup master data) dihitung 1 payload
    for b in blocks:
        if b["res"] == "Location" and any(x["Path"] == "Location.type.coding" for x in b["rows"]):
            b["rows"][0]["jumlah instance"] = "1"; b["reason"] = ""; payloads.append(b)
            fixes["Location dari isian form dihitung payload"] += 1
    keep = [r for r in rows if any(r[c] for c in ep.OUT_COLS[:15])]
    ep.write_csv(f"{repo}/mapping/phdt-data-dictionary-{slug}.csv", keep)
    v = [r["Variables"] for r in keep if r["Variables"]]
    stats[slug] = dict(nama=nama, sheet=sheet, baris_csv=len(keep), var_unik=len(set(v)), var_baris=len(v),
                       payload=sum(1 for r in keep if r["jumlah instance"] == "1"),
                       code=sum(1 for r in keep if r["jumlah code"] == "1"),
                       payload_per_resource=dict(Counter(r["Resource"] for r in keep if r["jumlah instance"] == "1")),
                       tidak_dihitung=dict(Counter(f'{b["res"]}: {b["reason"]}' for b in blocks if b["reason"])),
                       baris_digeser=shifted, perbaikan=dict(fixes))
    s = stats[slug]
    print(f"{slug:28s} baris {s['baris_csv']:4d} var unik {s['var_unik']:3d} (baris {s['var_baris']:3d}) "
          f"payload {s['payload']:3d} code {s['code']:3d}  {s['payload_per_resource']}")
    print("   perbaikan:", dict(fixes), "| baris digeser:", (shifted[0], shifted[-1], len(shifted)) if shifted else "-")
os.makedirs("/home/claude/work", exist_ok=True)
json.dump(stats, open("/home/claude/work/sismal-stats.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
