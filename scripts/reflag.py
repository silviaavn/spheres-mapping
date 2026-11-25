"""Tambah flag `jumlah code` = 1 di mapping/*.csv sesuai aturan hitung code (epus_prepare.is_counted).
HANYA menambah: flag yang sudah ada tidak dihapus, `jumlah instance` tidak diubah. Baris dihitung kalau
resource barisnya punya payload (minimal 1 baris `jumlah instance` = 1 di file itu); resource lookup tanpa payload dilewati.
Pemakaian: python3 -I scripts/reflag.py <repo> [--apply]"""
import csv, glob, importlib.util, os, sys, json
repo = sys.argv[1]; apply = "--apply" in sys.argv
spec = importlib.util.spec_from_file_location("ep", os.path.join(repo, "scripts/epus_prepare.py"))
ep = importlib.util.module_from_spec(spec); spec.loader.exec_module(ep)
tot = 0; per = {}; added = []
for f in sorted(glob.glob(repo + "/mapping/*.csv")):
    rows = list(csv.reader(open(f, encoding="utf-8", newline="")))
    if not rows: continue
    h = rows[0]
    need = ["Resource", "Path", "Code", "CodeSystem", "jumlah code", "jumlah instance"]
    if any(c not in h for c in need): continue
    ix = {c: h.index(c) for c in need}
    pay = {r[ix["Resource"]].strip().lower() for r in rows[1:] if len(r) > ix["jumlah instance"] and r[ix["jumlah instance"]].strip() == "1"}
    n = 0
    for ln, r in enumerate(rows[1:], 2):
        if len(r) < len(h): r += [""] * (len(h) - len(r))
        res = r[ix["Resource"]].strip()
        if not res or res.lower() not in pay or r[ix["jumlah code"]].strip() == "1": continue
        if ep.is_counted(ep.norm_path(r[ix["Path"]]), r[ix["Code"]].strip(), r[ix["CodeSystem"]]):
            r[ix["jumlah code"]] = "1"; n += 1
            added.append([os.path.basename(f), ln, r[ix["Path"]], r[ix["Code"]], r[ix["CodeSystem"]]])
    if n:
        per[os.path.basename(f)] = n; tot += n
        if apply:
            with open(f, "w", encoding="utf-8", newline="") as w:
                csv.writer(w, lineterminator="\n").writerows(rows)
json.dump(added, open("/tmp/spheres/reflag_added.json", "w"), ensure_ascii=False)
print("baris code ditambah:", tot, "di", len(per), "file")
for k, v in sorted(per.items(), key=lambda x: -x[1])[:25]: print(v, k)
