"""Siapkan dictionary Tumbuh Kembang (KPSP, TDD, TDL, KMPE, M-CHAT, GPPH) dari
Childhood_Development_Toolkit_Data_Dictionary.xlsx -> mapping/phdt-data-dictionary-epus-tumbang-<form>.csv
Pemakaian: python3 -I scripts/tumbang_prepare.py <xlsx> <repo_dir>
Memakai fungsi yang sama dengan scripts/epus_prepare.py (kolom standar, perapian sel, jumlah instance/code)."""
import importlib.util, json, os, sys
from collections import Counter, OrderedDict
import openpyxl

here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("ep", os.path.join(here, "epus_prepare.py"))
ep = importlib.util.module_from_spec(spec); spec.loader.exec_module(ep)

def F(slug, nama, sheet, ref, label):
    return dict(slug=slug, nama=nama, sheet=sheet, hdr=0, var="Variables", raw=None, bq=None, tracker=16, ref=ref, ref_label=label)

FORMS = [
    F("tumbang-kpsp", "ePuskesmas Tumbuh Kembang - KPSP", "KPSP", 140, "ePuskesmas | Tumbang - KPSP"),
    F("tumbang-tdd", "ePuskesmas Tumbuh Kembang - TDD", "TDD New", 48, "ePuskesmas | Tumbang - TDD"),
    F("tumbang-tdl", "ePuskesmas Tumbuh Kembang - TDL", "TDL New", 21, "ePuskesmas | Tumbang - TDL"),
    F("tumbang-kmpe", "ePuskesmas Tumbuh Kembang - KMPE", "KMPE", 14, "ePuskesmas | Tumbang - KMPE"),
    F("tumbang-mchat", "ePuskesmas Tumbuh Kembang - M-CHAT-R", "M-CHAT", 20, "ePuskesmas | Tumbang - M-CHAT-R"),
    F("tumbang-gpph", "ePuskesmas Tumbuh Kembang - GPPH", "GPPH", 10, "ePuskesmas | Tumbang - GPPH"),
]

def main(xlsx, repo):
    wb = openpyxl.load_workbook(xlsx, data_only=True)
    stats = OrderedDict()
    for cfg in FORMS:
        rows, log = ep.prepare(cfg, wb, None)
        blocks, payloads = ep.flag(rows)
        keep = [r for r in rows if any(r[c] for c in ep.OUT_COLS[:15])]
        ep.write_csv(f"{repo}/mapping/phdt-data-dictionary-epus-{cfg['slug']}.csv", keep)
        vars_ = [r["Variables"] for r in keep if r["Variables"]]
        stats[cfg["slug"]] = dict(
            nama=cfg["nama"], sheet=cfg["sheet"], tracker=16, ref=cfg["ref"], ref_label=cfg["ref_label"],
            baris_sheet=len(rows), baris_csv=len(keep), var_unik=len(set(vars_)), var_baris=len(vars_),
            payload=len(payloads), code=sum(1 for r in keep if r["jumlah code"] == "1"),
            payload_per_resource=dict(Counter(b["res"] for b in payloads)),
            tidak_dihitung_res=dict(Counter(f'{b["res"]}: {b["reason"]}' for b in blocks if b["reason"])),
            kode_tanggal=log["kode_tanggal"], resource_fix=Counter(map(tuple, log["resource_fix"])).most_common(10))
        s = stats[cfg["slug"]]
        print(f"{cfg['slug']:15s} baris {s['baris_sheet']:5d}->{s['baris_csv']:4d} var unik {s['var_unik']:3d} "
              f"(baris {s['var_baris']:3d}, ref {cfg['ref']}) payload {s['payload']:3d} code {s['code']:4d}", s["payload_per_resource"])
    os.makedirs("/home/claude/work", exist_ok=True)
    json.dump(stats, open("/home/claude/work/tumbang-stats.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
