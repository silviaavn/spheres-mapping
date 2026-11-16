"""Buat output per form dari data dictionary di mapping/.

Pemakaian:
    python3 scripts/form_output.py mapping/kobo-data-dictionary-<form>.csv "<Nama Form>" output/<form>.md

Payload = baris dengan `jumlah instance` = 1. Code = baris dengan `jumlah code` = 1.
Nomor baris = nomor baris fisik di file CSV (header multi-baris ikut dihitung).
"""
import csv
import re
import sys
from collections import Counter, OrderedDict

PEMBEDA_RESOURCES = {"Condition", "EpisodeOfCare", "Observation", "Procedure", "ServiceRequest", "DiagnosticReport",
                     "Specimen", "Immunization", "MedicationRequest", "MedicationDispense"}
PEMBEDA_PATHS = (".code.coding", ".type.coding", ".vaccineCode.coding")
# Baris label yang bukan tempat nilai disimpan: cari baris nilai sesudahnya di blok yang sama.
STRUCTURAL = re.compile(r"(\.status|\.use|\.system|\.url|\.category\.coding)$|^Observation\.code\.coding$")
VALUE = re.compile(r"\.value([A-Z]\w*)?(\.coding)?$")


def norm(h):
    return " ".join(h.split()).lower()


def load(path):
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = []
        for r in reader:
            rows.append((reader.line_num, r))
    header = [norm(h) for h in rows[0][1]]

    def col(*names):
        for n in names:
            if n in header:
                return header.index(n)
        return None

    c = dict(
        bq=col("nama column bq"),
        var=col("nama variabel di kobo", "variables"),
        res=col("resource"), path=col("path"), code=col("code"),
        df=col("definisi operasional", "definisi operasional (logic)"),
        disp=col("display"), cs=col("codesystem"),
        jc=col("jumlah code"), ji=col("jumlah instance"),
    )
    data = []
    for line, r in rows[1:]:
        r = r + [""] * (len(header) - len(r))
        g = lambda k: (r[c[k]].strip() if c[k] is not None else "")
        data.append(dict(line=line, **{k: g(k) for k in c}))
    return data


def build(data):
    payloads, current = [], None
    for d in data:
        if d["ji"] == "1":
            current = dict(line=d["line"], res=d["res"], code="", disp="", vars=[], last=d["line"], rows=[])
            payloads.append(current)
        if current and d["res"] == current["res"]:
            current["last"] = d["line"]
            current["rows"].append(d)
            if d["bq"] or d["var"]:
                current["vars"].append((d["line"], d["bq"], d["var"], d["path"], d["df"]))
            if (current["res"] in PEMBEDA_RESOURCES and not current["code"] and d["jc"] == "1"
                    and d["path"].endswith(PEMBEDA_PATHS)):
                current["code"], current["disp"] = d["code"], d["disp"]
        elif d["res"]:
            current = None  # blok resource lain: berhenti mengumpulkan
    # Variabel di blok lanjutan resource yang sama (mis. Encounter.serviceProvider di blok statusHistory)
    # ikut ke payload itu, asal resource tersebut hanya punya 1 payload di form ini.
    seen = {d["line"] for p in payloads for d in p["rows"]}
    by_res = {}
    for p in payloads:
        by_res.setdefault(p["res"], []).append(p)
    for d in data:
        if d["line"] in seen or not (d["bq"] or d["var"]) or len(by_res.get(d["res"], [])) != 1:
            continue
        p = by_res[d["res"]][0]
        p["vars"].append((d["line"], d["bq"], d["var"], d["path"], d["df"]))
        p["rows"].append(d)
    for p in payloads:
        p["rows"].sort(key=lambda d: d["line"])
        var_lines = {v[0] for v in p["vars"]}
        resolved = []
        for ln, b, k, pa, df in p["vars"]:
            vln, vpa = ln, pa
            if STRUCTURAL.search(pa):
                for d in p["rows"]:
                    if d["line"] <= ln:
                        continue
                    if d["line"] in var_lines:
                        break
                    if VALUE.search(d["path"]):
                        vln, vpa = d["line"], d["path"]
                        break
            resolved.append((vln, b, k, vpa, "master data" in df.lower()))
        p["vars"] = resolved
    codes = [d for d in data if d["jc"] == "1"]
    in_payload = {d["line"] for p in payloads for d in p["rows"] if d["bq"] or d["var"]}
    other_vars = [d for d in data if (d["bq"] or d["var"]) and d["line"] not in in_payload]
    return payloads, codes, other_vars


def load_raw(path):
    """Daftar variabel BQ dari tabel kolom file mentah (raw/<form>-kolom.md), urut kolom Excel."""
    cols = []
    for line in open(path, encoding="utf-8"):
        m = re.match(r"\|\s*\d+\s*\|\s*([A-Z]+)\s*\|[^|]*\|\s*`([^`]+)`", line)
        if m:
            cols.append((m.group(1), m.group(2)))
    return cols


def render(form, src, data, payloads, codes, other_vars, raw=None, raw_path=None):
    bq = OrderedDict((d["bq"], None) for d in data if d["bq"])
    bq_in = {b for p in payloads for _, b, _, _, _ in p["vars"] if b}
    bq_out = [b for b in bq if b not in bq_in]
    out = [f"# Output Form: {form}", "",
           f"Sumber: `{src}`",
           "Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.",
           "Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.", "",
           "## Ringkasan", "",
           "| Item | Jumlah |", "|---|---|",
           f"| Payload (`jumlah instance` = 1) | {len(payloads)} |",
           f"| Code (`jumlah code` = 1) | {len(codes)} |",
           f"| Code unik (code + CodeSystem) | {len({(d['code'], d['cs']) for d in codes})} |",
           f"| Variabel BQ (unik) | {len(bq)} |"]
    if raw is not None:
        out.append(f"| Variabel di Excel export | {len(raw)} |")
    out += ["",
           "## Payload", "",
           "| # | Baris | Resource | Code pembeda | Display | Variabel BQ → Path (baris) |",
           "|---|---|---|---|---|---|"]
    for i, p in enumerate(payloads, 1):
        v = "<br>".join((f"`{b}` → `{pa}` ({ln})" if b else f"_{k}_ → `{pa}` ({ln}, tanpa BQ)")
                        + (" 🔎 lookup master data" if md else "") for ln, b, k, pa, md in p["vars"]) or "–"
        out.append(f"| {i} | {p['line']}–{p['last']} | {p['res']} | {p['code'] or '–'} | {p['disp'] or '–'} | {v} |")
    out += ["", "### Payload per resource", "", "| Resource | Jumlah |", "|---|---|"]
    for r, n in Counter(p["res"] for p in payloads).most_common():
        out.append(f"| {r} | {n} |")
    out += [f"| **Total** | **{len(payloads)}** |", "",
            "## Code", "",
            "| # | Baris | Resource | Path | Code | Display | CodeSystem |",
            "|---|---|---|---|---|---|---|"]
    for i, d in enumerate(codes, 1):
        out.append(f"| {i} | {d['line']} | {d['res']} | `{d['path']}` | {d['code']} | {d['disp']} | {d['cs']} |")
    out += ["", "### Code per CodeSystem", "", "| CodeSystem | Jumlah | Code |", "|---|---|---|"]
    by_cs = OrderedDict()
    for d in codes:
        by_cs.setdefault(d["cs"], []).append(d["code"])
    for cs, cl in sorted(by_cs.items(), key=lambda x: -len(x[1])):
        out.append(f"| {cs} | {len(cl)} | {', '.join(cl)} |")
    out += [f"| **Total** | **{len(codes)}** | |", "",
            "## Variabel di luar payload", "",
            "Semua variabel BQ harus masuk ke salah satu payload. Baris dengan variabel BQ di sini = ⚠️ perlu dicek.", "",
            "| Baris | Variabel BQ | Variabel dictionary | Resource | Path |", "|---|---|---|---|---|"]
    for d in other_vars:
        flag = "⚠️ " if d["bq"] else ""
        out.append(f"| {d['line']} | {flag}{d['bq'] or '–'} | {d['var'] or '–'} | {d['res'] or '–'} | `{d['path']}` |")
    if not other_vars:
        out.append("| – | – | – | – | – |")
    out.append("")
    return "\n".join(out)


if __name__ == "__main__":
    src, form, dst = sys.argv[1], sys.argv[2], sys.argv[3]
    raw_path = sys.argv[4] if len(sys.argv) > 4 else None  # opsional: raw/<form>-kolom.md (file mentah, mis. Excel export)
    data = load(src)
    payloads, codes, other = build(data)
    raw = load_raw(raw_path) if raw_path else None
    open(dst, "w", encoding="utf-8").write(render(form, src, data, payloads, codes, other, raw, raw_path))
    print(f"{form}: {len(payloads)} payload, {len(codes)} code -> {dst}")
    bq_in = {b for p in payloads for _, b, _, _, _ in p["vars"] if b}
    if raw is not None:
        miss = [f"{c} {b}" for c, b in raw if b not in bq_in]
        if miss:
            print("PERINGATAN: kolom Excel export belum masuk payload:", ", ".join(miss))
