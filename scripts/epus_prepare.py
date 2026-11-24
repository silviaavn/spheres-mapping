"""Siapkan dictionary ePuskesmas dari PHDT_ePus.xlsx -> mapping/phdt-data-dictionary-epus-<form>.csv

Pemakaian:
    python3 -I scripts/epus_prepare.py <PHDT_ePus.xlsx> <repo_dir>

Yang dilakukan (semua otomatis, bisa diulang dari file asli):
  1. Ambil kolom standar dari tiap sheet (kolom tracking Google Function / Validation dst. tidak dibawa).
  2. Rapikan sel: float kode (119361006.0 -> 119361006), kode LOINC yang jadi tanggal di Excel
     (8665-02-01 00:00:00 -> 8665-2), spasi/tab/newline di Code, Display, CodeSystem.
  3. Resource: perbaiki 'Careplan' -> 'CarePlan', Resource yang berisi path, Resource kosong dari awalan path.
  4. Isi `jumlah instance` (payload) dan `jumlah code` sesuai aturan.md. Blok Organization / Location
     (lookup master data), PractitionerRole petugas lab (lookup), dan blok template (kode "dapat merujuk ...")
     tidak dihitung. Baris tetap ada di dictionary.
  5. Tulis ringkasan ke work/epus-stats.json (angka variabel, perbaikan, payload per resource).
"""
import csv
import json
import os
import re
import sys
import datetime as dt
from collections import Counter, OrderedDict

import openpyxl

OUT_COLS = ["Categories", "Subcategories", "Nama Column BQ", "Nama Column Raw", "Variables", "Data Type",
            "Format/Value", "Value Name", "Definisi Operasional", "Agregat/Individu", "Resource", "Path", "Code",
            "Display", "CodeSystem", "Keterangan", "jumlah code", "jumlah instance"]

# slug, nama form, sheet, baris header (0-based), kolom variabel, kolom raw, kolom BQ, tracker #, referensi PHDT
FORMS = [
    dict(slug="pelayanan", nama="ePuskesmas Pelayanan Pasien", sheet="epus layanan", hdr=0, var="Original Variables",
         raw=None, bq="Nama Column BQ", tracker=1, ref=80, ref_label="ePuskesmas | Pelayanan"),
    dict(slug="kunjungan-ibu-hamil", nama="ePuskesmas Kunjungan Ibu Hamil", sheet="old epusk kunjungan ibu hamil ",
         hdr=0, var="Original Variables", raw=None, bq="Nama Column BQ", tracker=3, ref=97,
         ref_label="ePuskesmas | KIA"),
    dict(slug="lab", nama="ePuskesmas Laboratorium", sheet="epus lab", hdr=0, var="Original Variables", raw="Variable",
         bq=None, tracker=5, ref=23, ref_label="ePuskesmas | Laboratorium"),
    dict(slug="rujukan-eksternal", nama="ePuskesmas Rujukan Eksternal", sheet="epus rujukan eksternal", hdr=0,
         var="Original Variables", raw=None, bq="Nama Column BQ", tracker=8, ref=22, ref_label="ePuskesmas | Rujukan"),
    dict(slug="anc", nama="ePuskesmas ANC (KIA Harian)", sheet="epus ordal anc", hdr=1, var="Variables",
         raw="Nama Column Raw", bq="Nama Column BQ", tracker=11, ref=136, ref_label="ePuskesmas | ANC - Ibu Hamil"),
    dict(slug="inc", nama="ePuskesmas INC (KIA Harian)", sheet="epus ordal inc", hdr=1, var="Variables",
         raw="Nama Column Raw", bq="Nama Column BQ", tracker=12, ref=82, ref_label="ePuskesmas | INC - Persalinan"),
    dict(slug="pnc", nama="ePuskesmas PNC (KIA Harian)", sheet="epus ordal pnc", hdr=2, var="Variables", raw=None,
         bq=None, tracker=13, ref=96, ref_label="ePuskesmas | PNC - Ibu Nifas"),
    dict(slug="mtbs", nama="ePuskesmas MTBS (KIA Harian)", sheet="epus mtbs", hdr=0, var="Variables",
         raw="Nama Column Raw", bq=None, tracker=14, ref=187, ref_label="ePuskesmas | MTBS"),
    dict(slug="mtbm", nama="ePuskesmas MTBM (KIA Harian)", sheet="epus mbtm", hdr=0, var="Variables",
         raw="Nama Column Raw", bq=None, tracker=15, ref=115, ref_label="ePuskesmas | MTBM"),
    dict(slug="tumbang-anak", nama="ePuskesmas Tumbuh Kembang - Anak", sheet="epusk tumbang", hdr=0, var="Variables",
         raw=None, bq=None, tracker=16, ref=34, ref_label="ePuskesmas | Tumbang - Anak"),
    dict(slug="tumbang-ddtk", nama="ePuskesmas Tumbuh Kembang - DDTK/SDIDTK", sheet="epus DDTKSDIDTK", hdr=0,
         var="Variables", raw=None, bq=None, tracker=16, ref=38, ref_label="ePuskesmas | Tumbang - DDTK"),
]
NOTE_COLS = ["notes mas faris", "notes mas fariz", "personal notes", "internal review fhir", "mapping fhir status",
             "keterangan"]

LOOKUP_RES = {"Organization", "Location"}          # master data: tidak dihitung (aturan.md)
SINGLETON = {"Patient", "Encounter"}               # 1 payload per form, blok lanjutan = payload yang sama
START_TAIL = (".identifier", ".status", ".clinicalStatus.coding", ".clinicalStatus", ".active")
SINGLE_SUFFIX = (".subject.reference", ".encounter.reference", ".effectiveDateTime", ".issued", ".name.text")
LAB_WORKER = "1290220002"
TEMPLATE_RE = re.compile(r"kode dapat merujuk|valuenya akan merujuk", re.I)
PLACEHOLDER_CODES = {"", "tidak ada", "true", "false", "none"}
CODE_OK = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._\-/]*$")

COUNT_PATHS = [re.compile(p) for p in [
    r"^(Condition|DiagnosticReport|Observation|Procedure|ServiceRequest|PractitionerRole)\.code(\.coding)?$",
    r"^Specimen\.type(\.coding)?$", r"^EpisodeOfCare\.type(\.coding)?$", r"^Immunization\.vaccineCode(\.coding)?$",
    r"^(MedicationRequest|MedicationDispense)\.contained\.code(\.coding)?$", r"^Medication\.code(\.coding)?$",
    r"^Observation\.(valueCodeableConcept|interpretation|method)(\.coding)?$",
    r"^Observation\.component\.(code|valueCodeableConcept)(\.coding)?$",
    r"^ServiceRequest\.reasonCode(\.coding)?$",
    r"^CarePlan\.activity\.detail\.(code|productCodeableConcept|statusReason)(\.coding)?$",
    r"^CarePlan\.activity\.outcomeCodeableConcept(\.coding)?$",
    r"^Encounter\.hospitalization\.admitSource(\.coding)?$",
    r"^QuestionnaireResponse\.item(\.item)*\.answer\.valueCoding$",
    r"^Encounter\.identifier$",
    r"^Consent\.provision(\.provision)?\.code(\.coding)?$",   # klausul IC (kode SP custom)
]]
DET_PATHS = [re.compile(p) for p in [   # code pembeda payload (baris pertama yang cocok)
    r"^(Condition|DiagnosticReport|Observation|Procedure|ServiceRequest|PractitionerRole)\.code(\.coding)?$",
    r"^Specimen\.type(\.coding)?$", r"^EpisodeOfCare\.type(\.coding)?$", r"^Immunization\.vaccineCode(\.coding)?$"]]


def norm_path(p):
    p = re.sub(r"\[\w+\]", "", p.replace(" ", ""))
    return p


def clean(v):
    if v is None:
        return ""
    if isinstance(v, bool):
        return "True" if v else "False"
    if isinstance(v, (dt.datetime, dt.date)):
        return v.strftime("%Y-%m-%d %H:%M:%S")
    if isinstance(v, float) and v == int(v):
        return str(int(v))
    return str(v)


def fix_code(code, log):
    c = clean(code).replace("\t", " ").replace("\n", " ").strip()
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2}) 00:00:00$", c)
    if m:   # LOINC mis-baca jadi tanggal oleh Excel (8665-2 -> 8665-02-01)
        new = f"{m.group(1)}-{int(m.group(2))}" if m.group(3) == "01" else c
        if new != c:
            log["kode_tanggal"].append((c, new))
        return new
    return c


def ws_rows(ws, hdr):
    rows = list(ws.iter_rows(values_only=True))
    header = [" ".join(clean(h).split()).lower() for h in rows[hdr]]
    return header, rows[hdr + 1:], hdr + 2   # baris Excel pertama data = hdr+2


def find(header, *names, startswith=None):
    for n in names:
        if n and n.lower() in header:
            return header.index(n.lower())
    if startswith:
        for i, h in enumerate(header):
            if h.startswith(startswith):
                return i
    return None


def prepare(cfg, wb, revised_map):
    log = dict(kode_tanggal=[], resource_fix=[], resource_dari_path=0, float_fix=0)
    header, data, first_excel = ws_rows(wb[cfg["sheet"]], cfg["hdr"])
    ix = dict(
        cat=find(header, "categories"), sub=find(header, "subcategories"),
        bq=find(header, cfg["bq"]) if cfg["bq"] else None,
        raw=find(header, cfg["raw"]) if cfg["raw"] else None,
        var=find(header, cfg["var"]),
        dtype=find(header, startswith="data type"), fmt=find(header, startswith="format/value"),
        vname=find(header, "value name", "value raw"), df=find(header, startswith="definisi operasional"),
        agg=find(header, "agregat/individu", "menjawab indikator"),
        res=find(header, "resource"), path=find(header, "path"), code=find(header, "code"),
        disp=find(header, "display"), cs=find(header, "codesystem"),
    )
    notes = [header.index(n) for n in NOTE_COLS if n in header]
    g = lambda r, k: clean(r[ix[k]]) if ix[k] is not None and ix[k] < len(r) else ""
    out = []
    for r in data:
        row = OrderedDict((c, "") for c in OUT_COLS)
        row["Categories"], row["Subcategories"] = g(r, "cat").strip(), g(r, "sub").strip()
        row["Nama Column BQ"] = g(r, "bq").strip()
        row["Variables"] = " ".join(g(r, "var").split())
        row["Nama Column Raw"] = " ".join(g(r, "raw").split())
        row["Data Type"], row["Format/Value"] = g(r, "dtype").strip(), g(r, "fmt").strip()
        row["Value Name"] = " ".join(g(r, "vname").split())
        row["Definisi Operasional"] = g(r, "df").strip()
        row["Agregat/Individu"] = g(r, "agg").strip()
        res, path = g(r, "res").strip(), " ".join(g(r, "path").split())
        if "." in res and not path:
            path, res = res, res.split(".")[0]
            log["resource_fix"].append(("resource berisi path", path))
        elif "." in res:
            log["resource_fix"].append(("resource berisi path", res))
            res = res.split(".")[0]
        if res == "Practioner":
            log["resource_fix"].append(("Practioner", "Practitioner"))
            res = "Practitioner"
        if res == "Careplan":
            log["resource_fix"].append(("Careplan", "CarePlan"))
            res = "CarePlan"
        if not res and re.match(r"^[A-Z][A-Za-z]+\.", path):
            res = path.split(".")[0]
            log["resource_dari_path"] += 1
        row["Resource"], row["Path"] = res, path
        row["Code"] = fix_code(r[ix["code"]] if ix["code"] is not None else None, log)
        row["Display"] = " ".join(g(r, "disp").split())
        row["CodeSystem"] = " ".join(g(r, "cs").split())
        row["Keterangan"] = " | ".join(clean(r[i]).strip() for i in notes if i < len(r) and clean(r[i]).strip())
        row["_excel"] = first_excel + len(out)
        out.append(row)
    # --- nama raw dari sheet "revised" (khusus Pelayanan): cocokkan label variabel
    if revised_map and cfg["slug"] == "pelayanan":
        hit = 0
        for row in out:
            k = re.sub(r"[^a-z0-9]", "", row["Variables"].lower())
            if k and k in revised_map and not row["Nama Column Raw"]:
                row["Nama Column Raw"] = revised_map[k]
                hit += 1
        log["raw_dari_revised"] = hit
    return out, log


HEADER_LIKE = re.compile(r"\.(identifier|status|category(\.coding)?|clinicalStatus(\.coding)?|verificationStatus(\.coding)?"
                         r"|intent|priority|active)$")
CODED = {"Observation", "Condition", "Procedure", "ServiceRequest", "DiagnosticReport", "Specimen", "PractitionerRole",
         "EpisodeOfCare", "Immunization"}


def is_det(res, path):
    return any(rx.match(path) for rx in DET_PATHS) and path.split(".")[0] == res


def flag(rows):
    """Isi jumlah instance / jumlah code. Mengembalikan (semua blok, blok yang dihitung sebagai payload).

    Awal blok baru: (1) resource berganti (Patient & Encounter = 1 payload per form, blok lanjutan ikut payload
    pertama); (2) resource ber-code (Observation, Condition, dst.): baris code pembeda muncul lagi setelah ada
    baris isi (value / subject / dst.), baris header (status, category, identifier) sebelumnya ikut pindah ke blok baru;
    (3) resource tanpa code: path nilai-tunggal (name.text, subject.reference, ...) muncul lagi."""
    blocks, cur, last_res = [], None, None
    singleton_block = {}
    for row in rows:
        res, path = row["Resource"], norm_path(row["Path"])
        if not res or not path:
            continue
        start, backup = False, 0
        if cur is None or res != last_res:
            if res in SINGLETON and res in singleton_block:
                cur = singleton_block[res]
            else:
                start = True
        elif res in SINGLETON:
            pass
        elif res in CODED:
            if is_det(res, path) and cur["after_code"]:
                start = True
                # baris header (status/category/identifier) di ujung blok lama yang merupakan pengulangan path
                # (sudah muncul lebih awal di blok itu) adalah awal blok baru: ikut dipindah
                for k in range(len(cur["rows"]) - 1, -1, -1):
                    pp = norm_path(cur["rows"][k]["Path"])
                    earlier = {norm_path(x["Path"]) for x in cur["rows"][:k]}
                    if HEADER_LIKE.search(pp) and not is_det(res, pp) and (pp in earlier or pp.endswith(".identifier")):
                        backup += 1
                    else:
                        break
                backup = min(backup, len(cur["rows"]) - 1)
        elif path in cur["seen"] and path.endswith(SINGLE_SUFFIX):
            start = True
        if start:
            moved = []
            if backup:
                moved = cur["rows"][-backup:]
                cur["rows"] = cur["rows"][:-backup]
            cur = dict(res=res, rows=list(moved), seen=set(), after_code=False, first=(moved[0] if moved else row))
            blocks.append(cur)
            if res in SINGLETON:
                singleton_block[res] = cur
        cur["rows"].append(row)
        cur["seen"].add(path)
        if res in CODED:
            if is_det(res, path):
                cur["after_code"] = False
                cur["det_seen"] = True
            elif cur.get("det_seen") and not path.startswith(res + ".code") and not path.startswith(res + ".type"):
                cur["after_code"] = True
        last_res = res
    payloads = []
    for b in blocks:
        res = b["res"]
        reason = ""
        if res in LOOKUP_RES:
            reason = "lookup master data"
        elif res == "PractitionerRole" and any(r["Code"] == LAB_WORKER for r in b["rows"]):
            reason = "PractitionerRole lab = lookup"
        elif any(TEMPLATE_RE.search(r["Code"] + " " + r["Display"]) for r in b["rows"]):
            reason = "template (kode merujuk ke masing-masing)"
        b["reason"] = reason
        b["first"] = b["rows"][0]
        if reason:
            continue
        b["first"]["jumlah instance"] = "1"
        payloads.append(b)
        for r in b["rows"]:
            p = norm_path(r["Path"])
            code = r["Code"]
            if not any(rx.match(p) for rx in COUNT_PATHS):
                continue
            if code.lower() in PLACEHOLDER_CODES or code.startswith("Reference") or not CODE_OK.match(code) \
                    or len(code) > 40:
                continue
            if p == "Encounter.identifier" and not re.match(r"^K\d", code):
                continue
            r["jumlah code"] = "1"
    return blocks, payloads


def write_csv(path, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(OUT_COLS)
        for r in rows:
            w.writerow([r[c] for c in OUT_COLS])


def main(xlsx, repo):
    wb = openpyxl.load_workbook(xlsx, data_only=True)
    # peta label Pelayanan -> nama variabel scraping (sheet "epus layanan (revised)")
    rv = list(wb["epus layanan (revised)"].iter_rows(values_only=True))
    revised_map = {}
    for r in rv[1:]:
        if r[3] and r[4]:
            revised_map[re.sub(r"[^a-z0-9]", "", str(r[4]).lower())] = str(r[3]).strip()
    stats = OrderedDict()
    for cfg in FORMS:
        rows, log = prepare(cfg, wb, revised_map)
        # buang baris kosong total, simpan nomor baris Excel asal di stats saja
        keep = [r for r in rows if any(r[c] for c in OUT_COLS[:15])]
        blocks, payloads = flag(rows)
        keep = [r for r in rows if any(r[c] for c in OUT_COLS[:15])]
        dst = f"{repo}/mapping/phdt-data-dictionary-epus-{cfg['slug']}.csv"
        write_csv(dst, keep)
        vars_ = [r["Variables"] for r in keep if r["Variables"]]
        res_cnt = Counter(b["res"] for b in payloads)
        stats[cfg["slug"]] = dict(
            nama=cfg["nama"], sheet=cfg["sheet"], tracker=cfg["tracker"], ref=cfg["ref"], ref_label=cfg["ref_label"],
            baris_sheet=len(rows), baris_csv=len(keep), var_unik=len(set(vars_)), var_baris=len(vars_),
            payload=len(payloads), code=sum(1 for r in keep if r["jumlah code"] == "1"),
            payload_per_resource=dict(res_cnt),
            tidak_dihitung=dict(Counter(b["reason"] for b in blocks if b["reason"])),
            tidak_dihitung_res=dict(Counter(f'{b["res"]}: {b["reason"]}' for b in blocks if b["reason"])),
            kode_tanggal=log["kode_tanggal"], resource_fix=Counter(map(tuple, log["resource_fix"])).most_common(10),
            resource_dari_path=log["resource_dari_path"], raw_dari_revised=log.get("raw_dari_revised"),
        )
        print(f"{cfg['slug']:22s} baris {len(rows):5d}->{len(keep):5d}  var unik {len(set(vars_)):3d} "
              f"(baris {len(vars_):3d}, ref {cfg['ref']})  payload {len(payloads):4d}  code "
              f"{stats[cfg['slug']]['code']:4d}")
    os.makedirs("/home/claude/work", exist_ok=True)
    json.dump(stats, open("/home/claude/work/epus-stats.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
