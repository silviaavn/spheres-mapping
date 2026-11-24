"""Siapkan dictionary Dapodik PAUD dari sheet `Copy of DAPODIK` (Childhood_Development_Toolkit_Data_Dictionary.xlsx)
-> mapping/phdt-data-dictionary-dapodik-paud.csv. Pemakaian: python3 -I scripts/dapodik_prepare.py <xlsx> <repo_dir>
Variabel = kolom `Variabel PDF`; nama kolom raw = `Variables Excel Export`."""
import importlib.util, json, os, sys
from collections import Counter
import openpyxl
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("ep", os.path.join(here, "epus_prepare.py"))
ep = importlib.util.module_from_spec(spec); spec.loader.exec_module(ep)
cfg = dict(slug="dapodik-paud", nama="Dapodik PAUD", sheet="Copy of DAPODIK", hdr=0, var="Variabel PDF",
           raw="Variables Excel Export", bq=None, tracker=124, ref=93, ref_label="Dapodik | PAUD (semester)")
wb = openpyxl.load_workbook(sys.argv[1], data_only=True)
wb[cfg["sheet"]].cell(row=1, column=1).value = "Categories"   # header asli: "udah selesai semua"
rows, log = ep.prepare(cfg, wb, None)
blocks, payloads = ep.flag(rows)
keep = [r for r in rows if any(r[c] for c in ep.OUT_COLS[:15])]
ep.write_csv(f"{sys.argv[2]}/mapping/phdt-data-dictionary-dapodik-paud.csv", keep)
v = [r["Variables"] for r in keep if r["Variables"]]
raw = {r["Nama Column Raw"] for r in keep if r["Nama Column Raw"]}
st = {cfg["slug"]: dict(nama=cfg["nama"], sheet=cfg["sheet"], tracker=124, ref=93, ref_label=cfg["ref_label"],
      baris_sheet=len(rows), baris_csv=len(keep), var_unik=len(set(v)), var_baris=len(v), raw_unik=len(raw),
      payload=len(payloads), code=sum(1 for r in keep if r["jumlah code"] == "1"),
      payload_per_resource=dict(Counter(b["res"] for b in payloads)),
      tidak_dihitung_res=dict(Counter(f'{b["res"]}: {b["reason"]}' for b in blocks if b["reason"])),
      kode_tanggal=log["kode_tanggal"], resource_fix=Counter(map(tuple, log["resource_fix"])).most_common(10))}
print(st)
json.dump(st, open("/home/claude/work/dapodik-stats.json", "w"), ensure_ascii=False, indent=1)
