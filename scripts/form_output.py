"""Buat output per form dari data dictionary di mapping/.

Pemakaian:
    python3 scripts/form_output.py mapping/kobo-data-dictionary-<form>.csv "<Nama Form>" output/<form>.md

Payload = baris dengan `jumlah instance` = 1. Code = baris dengan `jumlah code` = 1.
Nomor baris = nomor baris fisik di file CSV (header multi-baris ikut dihitung).
"""
import csv
import sys
from collections import Counter, OrderedDict

PEMBEDA_RESOURCES = {"Condition", "EpisodeOfCare", "Observation"}


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
            current = dict(line=d["line"], res=d["res"], code="", disp="", vars=[], last=d["line"])
            payloads.append(current)
        if current and d["res"] == current["res"]:
            current["last"] = d["line"]
            if d["bq"] or d["var"]:
                current["vars"].append((d["line"], d["bq"], d["var"]))
            if (current["res"] in PEMBEDA_RESOURCES and not current["code"] and d["jc"] == "1"
                    and d["path"].endswith((".code.coding", ".type.coding"))):
                current["code"], current["disp"] = d["code"], d["disp"]
        elif d["res"]:
            current = None  # blok resource lain: berhenti mengumpulkan
    codes = [d for d in data if d["jc"] == "1"]
    in_payload = {v[0] for p in payloads for v in p["vars"]}
    other_vars = [d for d in data if (d["bq"] or d["var"]) and d["line"] not in in_payload]
    return payloads, codes, other_vars


def render(form, src, data, payloads, codes, other_vars):
    bq = OrderedDict((d["bq"], None) for d in data if d["bq"])
    out = [f"# Output Form: {form}", "",
           f"Sumber: `{src}`",
           "Dibuat otomatis oleh `scripts/form_output.py` dari kolom `jumlah instance` dan `jumlah code`.",
           "Kolom **Baris** = nomor baris di file CSV sumber, untuk ditelusuri.", "",
           "## Ringkasan", "",
           "| Item | Jumlah |", "|---|---|",
           f"| Payload (`jumlah instance` = 1) | {len(payloads)} |",
           f"| Code (`jumlah code` = 1) | {len(codes)} |",
           f"| Code unik (code + CodeSystem) | {len({(d['code'], d['cs']) for d in codes})} |",
           f"| Variabel BQ (unik) | {len(bq)} |", "",
           "## Payload", "",
           "| # | Baris | Resource | Code pembeda | Display | Variabel BQ (baris) |",
           "|---|---|---|---|---|---|"]
    for i, p in enumerate(payloads, 1):
        v = "<br>".join((f"`{b}` ({ln})" if b else f"_{k}_ ({ln}, tanpa BQ)") for ln, b, k in p["vars"]) or "–"
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
            "Variabel yang ada di dictionary tapi tidak masuk blok payload mana pun (mis. master data).", "",
            "| Baris | Variabel BQ | Variabel Kobo | Resource | Path |", "|---|---|---|---|---|"]
    for d in other_vars:
        out.append(f"| {d['line']} | {d['bq'] or '–'} | {d['var'] or '–'} | {d['res'] or '–'} | `{d['path']}` |")
    if not other_vars:
        out.append("| – | – | – | – | – |")
    out.append("")
    return "\n".join(out)


if __name__ == "__main__":
    src, form, dst = sys.argv[1], sys.argv[2], sys.argv[3]
    data = load(src)
    payloads, codes, other = build(data)
    open(dst, "w", encoding="utf-8").write(render(form, src, data, payloads, codes, other))
    print(f"{form}: {len(payloads)} payload, {len(codes)} code -> {dst}")
