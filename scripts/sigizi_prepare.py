"""Siapkan dictionary SiGizi (selain ANC) dari PHDT_SIGIZI.xlsx + bq_schema.xlsx
-> mapping/phdt-data-dictionary-sigizi-<slug>.csv

Pemakaian:
    python3 -I scripts/sigizi_prepare.py <PHDT_SIGIZI.xlsx> <bq_schema.xlsx> <repo_dir>

Yang dilakukan (otomatis, bisa diulang dari file asli; file asli tidak di-commit):
  1. Potong sheet "Copy of ..." per form (baris Excel, inklusif) dan rapikan lewat epus_prepare.prepare().
  2. Isi jumlah instance / jumlah code lewat epus_prepare.flag() (aturan.md).
  3. Isi kolom Nama Column BQ dari schema BQ: cocokkan nama raw header (schema) ke Nama Column Raw
     (tanpa kurung kurawal) atau Variables, berdasarkan nama, bukan posisi. BQ ditulis di baris pertama yang cocok.
     Kolom metadata pipeline dan `no` (data lokal, R2) tidak dihitung.
  4. Kolom `detail` (link halaman detail di web SiGizi): tambahkan baris Encounter.extension sigizi-detail
     (valueString) di blok Encounter (keputusan user 2026-11-24).
  5. Tulis ringkasan tally ke work/sigizi-stats.json.
"""
import importlib.util
import json
import os
import re
import sys
from collections import Counter, OrderedDict

import openpyxl

here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("ep", os.path.join(here, "epus_prepare.py"))
ep = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ep)

META = {"puskesmasname", "puskesmasid", "filename", "filedate", "ingestiontimestamp", "uuid", "hashcode", "sheetname",
        "no"}
# Kolom BQ yang bukan variabel form (tidak dimapping, dicatat di revisi.md)
AGG = "kolom rekap agregat per desa (ikut tercampur dari sheet rekap di file export), bukan data individu"
DERIVED = "kolom turunan pipeline (hasil konversi), bukan kolom file mentah"
EXCLUDE = {"desakelurahan": AGG, "jumlah_anak_diberi_vit_a": AGG, "jumlah_anak_asi_eksklusif": AGG,
           "zs_tbu_converted": DERIVED, "zs_tbu_awal": DERIVED}
# Schema `pemantauan pmt 2024`: raw header mulai "Tinggi Badan (cm) Awal" bergeser 1 baris terhadap field name,
# sehingga field tinggi_badan_cm_awal tampak tanpa raw. Kolom ini tetap kolom file mentah.
SHIFT_FIX = {"pemantauan pmt 2024": ["tinggi_badan_cm_awal"]}
DETAIL_URL = "http://terminology.kemkes.go.id/sp/sigizi-detail"
TINDAKAN_URL = "http://terminology.kemkes.go.id/sp/sigizi-tindakan"

BAL, PMT = "Copy of SiGizi_Balita", "Copy of SiGizi_PMT_2025"
# slug, nama form, sheet, baris Excel awal-akhir (None = sampai akhir), tabel BQ, tracker #, referensi PHDT
FORMS = [
    ("balita-bnba", "SiGizi Balita BNBA", BAL, 2, 538, "balita bnba", 17, 34, "SiGizi | Balita Tumbang (BNBA)"),
    ("balita-vitamin-a", "SiGizi Balita Vitamin A", "Copy of Sigizi Balita Vitamin A", 2, None, "vitamin a", 18, 32,
     "SiGizi | Balita Vitamin A"),
    ("balita-mendapat-pmt-2024", "SiGizi Balita Mendapat PMT 2024", BAL, 539, 887, "mendapat pmt 2024", 19, 49,
     "SiGizi | Balita PMT (2024, gabungan Mendapat + Pemantauan)"),
    ("balita-pemantauan-pmt-2024", "SiGizi Balita Pemantauan PMT 2024", BAL, 888, 1142, "pemantauan pmt 2024", 20, 49,
     "SiGizi | Balita PMT (2024, gabungan Mendapat + Pemantauan)"),
    ("balita-asi-eksklusif", "SiGizi Balita ASI Eksklusif", "Copy of Sigizi Balita ASI Ekskl", 2, None, "asi eksklusif",
     21, 22, "SiGizi | Balita ASI Ekslusif"),
    ("balita-mpasi", "SiGizi Balita MPASI", "Copy of Sigizi Balita MPASI", 2, None, "mpasi", 22, 28,
     "SiGizi | Balita MPASI"),
    ("pmt2025-bb-tidak-naik-pantau", "SiGizi PMT 2025 BB Tidak Naik - Pantau", PMT, 2, 347,
     "bb tidak naik pantau pmt 2025", 24, 154, "SiGizi | Balita PMT 2025 (gabungan 9 tabel)"),
    ("pmt2025-bb-tidak-naik-riwayat", "SiGizi PMT 2025 BB Tidak Naik - Riwayat", PMT, 1568, 2013,
     "bb tidak naik riwayat pmt 2025", 25, 154, "SiGizi | Balita PMT 2025 (gabungan 9 tabel)"),
    ("pmt2025-bb-tidak-naik-survey", "SiGizi PMT 2025 BB Tidak Naik - Survey", PMT, 2014, None,
     "bb tidak naik survey pmt 2025", 26, 154, "SiGizi | Balita PMT 2025 (gabungan 9 tabel)"),
    ("pmt2025-bb-kurang-pantau", "SiGizi PMT 2025 BB Kurang - Pantau", PMT, 348, 786,
     "bb kurang pantau pmt 2025", 27, 154, "SiGizi | Balita PMT 2025 (gabungan 9 tabel)"),
    ("pmt2025-bb-kurang-riwayat", "SiGizi PMT 2025 BB Kurang - Riwayat", PMT, 1568, 2013,
     "bb kurang riwayat pmt 2025", 28, 154, "SiGizi | Balita PMT 2025 (gabungan 9 tabel)"),
    ("pmt2025-bb-kurang-survey", "SiGizi PMT 2025 BB Kurang - Survey", PMT, 2014, None,
     "bb kurang survey pmt 2025", 29, 154, "SiGizi | Balita PMT 2025 (gabungan 9 tabel)"),
    ("pmt2025-gizi-kurang-pantau", "SiGizi PMT 2025 Gizi Kurang - Pantau", PMT, 787, 1567,
     "gizi kurang pantau pmt 2025", 30, 154, "SiGizi | Balita PMT 2025 (gabungan 9 tabel)"),
    ("pmt2025-gizi-kurang-riwayat", "SiGizi PMT 2025 Gizi Kurang - Riwayat", PMT, 1568, 2013,
     "gizi kurang riwayat pmt 2025", 31, 154, "SiGizi | Balita PMT 2025 (gabungan 9 tabel)"),
    ("pmt2025-gizi-kurang-survey", "SiGizi PMT 2025 Gizi Kurang - Survey", PMT, 2014, None,
     "gizi kurang survey pmt 2025", 32, 154, "SiGizi | Balita PMT 2025 (gabungan 9 tabel)"),
    ("ibu-nifas", "SiGizi Ibu Nifas", "Copy of SiGizi Nifas", 2, None, "ibu nifas", 34, 57, "SiGizi | Ibu Nifas"),
    ("kohort-ibu", "SiGizi Kohort Ibu", "Copy of SiGizi Kohort Ibu", 2, None, "kohort ibu", 36, None,
     "SiGizi Kohort Ibu (tidak ada di PHDT)"),
]

K = lambda s: re.sub(r"[^a-z0-9]", "", (s or "").lower()).replace("pukesmas", "puskesmas")  # typo header SiGizi
N = lambda v: " ".join(str(v).split()) if v is not None else ""


def load_schema(path):
    wb = openpyxl.load_workbook(path, read_only=True)
    out = {}
    for ws in wb.worksheets:
        rows = list(ws.iter_rows(values_only=True))
        h = [N(x).lower() for x in rows[0]]
        fi = h.index("field name")
        ri = 0 if fi == 1 else None
        fields = []
        for r in rows[1:]:
            f = N(r[fi]) if fi < len(r) else ""
            if not f or K(f) in META:
                continue
            fields.append((f, N(r[ri]) if ri is not None and ri < len(r) else ""))
        if ws.title in SHIFT_FIX:            # raw header di schema bergeser: kolom ini tetap kolom file mentah
            fields = [(f, raw or (f if f in SHIFT_FIX[ws.title] else "")) for f, raw in fields]
        has_raw = any(raw for _, raw in fields)
        ex = lambda f, raw: f in EXCLUDE and has_raw and not raw   # hanya kalau memang tidak ada di file mentah
        out[ws.title] = dict(fields=[x for x in fields if not ex(*x)],
                             excluded=[(f, EXCLUDE[f]) for f, raw in fields if ex(f, raw)],
                             tanpa_raw=[f for f, raw in fields if has_raw and not raw and f not in EXCLUDE])
    return out


def section_book(wb, sheet, a, b):
    """Workbook 1-sheet: header (baris 1) + baris a..b, supaya bisa lewat ep.prepare()."""
    rows = list(wb[sheet].iter_rows(values_only=True))
    header = list(rows[0])
    if not N(header[0]):
        header[0] = "Categories"
    body = [list(r) for r in rows[a - 1:(b or len(rows))]]
    section_book.shifted = 0
    for r in body:   # blok yang bergeser 1 kolom ke kiri (Resource di kolom Agregat/Individu, Path di kolom Resource)
        r += [None] * (16 - len(r))
        if re.match(r"^[A-Z][A-Za-z]+$", N(r[9])) and N(r[10]).startswith(N(r[9]) + "."):
            r.insert(9, None)
            section_book.shifted += 1
    nb = openpyxl.Workbook()
    ws = nb.active
    ws.title = "s"
    ws.append(header)
    for r in body:
        ws.append(list(r))
    return nb


def fill_bq(rows, fields, field_only=False):
    """Isi Nama Column BQ. Return (cocok {field: baris}, tidak ketemu [field])."""
    keys = []
    for i, r in enumerate(rows):
        raw = K(r["Nama Column Raw"])
        var = K(r["Variables"])
        keys.append((i, raw, var))
    hit, miss = OrderedDict(), []
    used = set()
    for f, raw in fields:
        cands = [k for k in ((K(f),) if field_only else (K(f), K(raw))) if k]   # field name dulu: raw di schema bisa bergeser
        idx = None
        for c in cands:                      # 1) nama sama persis (raw lalu Variables)
            for i, kr, kv in keys:
                if c in (kr, kv) and i not in used:
                    idx = i
                    break
            if idx is not None:
                break
        if idx is None:                      # 2) nama BQ hierarkis, berakhiran nama variabel dictionary
            best = None
            for i, kr, kv in keys:
                for k in (kr, kv):
                    if len(k) >= 3 and any(c.endswith(k) for c in cands) and i not in used:
                        if best is None or len(k) > best[1]:
                            best = (i, len(k))
            idx = best[0] if best else None
        if idx is None:
            miss.append(f)
            continue
        used.add(idx)
        if rows[idx]["Nama Column BQ"] and rows[idx]["Nama Column BQ"] != f:
            # baris sudah dipakai field lain: tulis di baris yang sama tidak bisa
            miss.append(f)
            continue
        rows[idx]["Nama Column BQ"] = f
        hit[f] = idx
    return hit, miss


def add_detail(rows, name="Detail", url=DETAIL_URL, note="ditambahkan 2026-11-24 (keputusan user)"):
    """Tambahkan 2 baris Encounter.extension sigizi-detail sesudah baris Encounter.serviceProvider (atau baris
    Encounter terakhir pada blok pertama)."""
    enc = [i for i, r in enumerate(rows) if r["Resource"] == "Encounter"]
    if not enc:
        return None
    sp = [i for i in enc if r_path(rows[i]).startswith("Encounter.serviceProvider")]
    pos = (sp[0] if sp else enc[-1]) + 1
    base = OrderedDict((c, "") for c in ep.OUT_COLS)
    url = dict(base, Resource="Encounter", Path="Encounter.extension.url", Code="Tidak ada", Display="Tidak ada",
               CodeSystem=url,
               **{"Definisi Operasional": f'Extension custom kolom "{name}" di tabel web SiGizi (awalan URL '
                                         'http://terminology.kemkes.go.id/sp/)'})
    val = dict(base, Resource="Encounter", Path="Encounter.extension.valueString", Code="Tidak ada",
               Display="Tidak ada", CodeSystem="Tidak ada", **{"Nama Column Raw": "{%s}" % name, "Variables": name,
                                                              "Data Type": "string",
                                                              "Definisi Operasional": f"Isi kolom {name} apa adanya (valueString)",
                                                              "Keterangan": note})
    url["_excel"] = val["_excel"] = None
    rows[pos:pos] = [url, val]
    return pos


def new_row(**kw):
    r = OrderedDict((c, "") for c in ep.OUT_COLS)
    for k, v in kw.items():
        r[k] = v
    r["_excel"] = None
    return r


def fix_rows(rows):
    """Perbaikan otomatis yang jelas (dicatat di revisi.md)."""
    out = []
    for r in rows:
        if r["Path"] == "Patient.line":
            r["Path"] = "Patient.address.line"
            out.append("Patient.line -> Patient.address.line")
        if r["Resource"] == "Location" and r["Path"].startswith("Organization.address"):
            r["Path"] = "Location" + r["Path"][len("Organization"):]
            out.append("Location: Organization.address... -> Location.address...")
        m = re.match(r"^(ServiceRequest|Observation|Condition|Procedure|DiagnosticReport|PractitionerRole)\.code$|"
                     r"^Specimen\.type$|^EpisodeOfCare\.type$", r["Path"])
        if m and r["Code"] and not r["Code"].lower().startswith(("tidak", "reference")):
            r["Path"] += ".coding"
            out.append(f"{r['Resource']}: path code tanpa .coding -> .coding")
    return sorted(set(out))


def vita_extra(rows):
    """Vitamin A: kolom export Nama Ortu & Tanggal Pemberian belum ada di dictionary (dictionary disalin dari BNBA)."""
    out = []
    enc = next(i for i, r in enumerate(rows) if r["Resource"] == "Encounter")
    rp = [new_row(Subcategories="Data Keluarga Pasien", Variables="Nama Ortu", **{"Data Type": "string"},
                  Resource="RelatedPerson", Path="RelatedPerson.patient", Code="Reference ke resources Patient",
                  Keterangan="ditambahkan 2026-11-24 (pola BNBA): kolom export Nama Ortu"),
          new_row(Resource="RelatedPerson", Path="RelatedPerson.active", Code="true", Display="Tidak ada",
                  CodeSystem="Tidak ada"),
          new_row(Resource="RelatedPerson", Path="RelatedPerson.relationship.coding", Code="PRN", Display="parent",
                  CodeSystem="http://terminology.hl7.org/CodeSystem/v3-RoleCode"),
          new_row(Resource="RelatedPerson", Path="RelatedPerson.name.text", Code="Tidak ada", Display="Tidak ada",
                  CodeSystem="Tidak ada", **{"Nama Column Raw": "{Nama Ortu}",
                                             "Definisi Operasional": "Hanya dibuat kalau {Nama Ortu} terisi"})]
    rows[enc:enc] = rp
    out.append("tambah blok RelatedPerson (Nama Ortu)")
    pr = [i for i, r in enumerate(rows) if r["Path"] == "Procedure.performedPeriod.start"]
    if pr:
        rows.insert(pr[0], new_row(Resource="Procedure", Path="Procedure.performedPeriod.start", Code="Tidak Ada",
                                   Display="Tidak Ada", CodeSystem="Tidak Ada", Variables="Tanggal Pemberian",
                                   **{"Nama Column Raw": "{Tanggal Pemberian}", "Data Type": "date",
                                      "Definisi Operasional": "Format export 14 kolom: tanggal pemberian vitamin A. "
                                      "Dipakai juga untuk Encounter.period, MedicationDispense.whenHandedOver kalau "
                                      "{Tanggal Pengukuran} (format export lama) kosong",
                                      "Keterangan": "ditambahkan 2026-11-24"}))
        out.append("tambah baris Tanggal Pemberian (Procedure.performedPeriod.start)")
    return out


LOOKUP_DO = {
    "puskesmas": ("Encounter.serviceProvider.reference", "Reference ke resources Organization",
                  "Lookup ke master data Organization Puskesmas: cocokkan string {Puskesmas}. Blok Organization/"
                  "Location di dictionary = master data, tidak dihitung"),
    "posyandu": ("Encounter.location.reference", "Reference ke resources Location",
                 "Lookup ke master data Location/Organization Posyandu (type 131): cocokkan string {Posyandu} + "
                 "{Desa/Kel} + {Puskesmas}. Tidak dihitung"),
}


def relocate_lookup(rows):
    """BQ puskesmas/posyandu yang jatuh di blok Organization/Location (master data, tidak dihitung) dipindah ke
    baris reference di Encounter pertama (aturan.md: lookup)."""
    out = []
    for i, r in enumerate(rows):
        f = K(r["Nama Column BQ"])
        if r["Resource"] not in ("Organization", "Location") or f not in LOOKUP_DO:
            continue
        path, code, do = LOOKUP_DO[f]
        e0 = next(j for j, x in enumerate(rows) if x["Resource"] == "Encounter")
        e1 = e0
        while e1 + 1 < len(rows) and rows[e1 + 1]["Resource"] in ("Encounter", ""):
            e1 += 1
        tgt = next((j for j in range(e0, e1 + 1) if rows[j]["Path"] == path), None)   # di blok Encounter pertama
        bq, raw = r["Nama Column BQ"], r["Nama Column Raw"]
        r["Nama Column BQ"] = ""
        if tgt is None:
            while not rows[e1]["Resource"]:
                e1 -= 1
            rows.insert(e1 + 1, new_row(Resource="Encounter", Path=path, Code=code))
            tgt = e1 + 1
        t = rows[tgt]
        t["Nama Column BQ"] = bq
        t["Nama Column Raw"] = t["Nama Column Raw"] or raw
        if "master data" not in t["Definisi Operasional"].lower():
            t["Definisi Operasional"] = (t["Definisi Operasional"] + " " + do).strip()
        out.append(f"{bq}: Organization/Location -> {path} (lookup)")
    return out


def has_mapped(rows, name):
    """Variabel sudah punya baris ber-Resource di dictionary?"""
    return any(K(r["Variables"]) == name or K(r["Nama Column Raw"]) == name for r in rows if r["Resource"] and r["Path"])


def drop_orphans(rows):
    """Baris yang hanya berisi label variabel tanpa Resource/Path (mis. catatan, Tindakan tanpa mapping) dan label
    variabel di blok Organization/Location (master data): label dipindah ke Keterangan supaya tidak terbaca sebagai
    variabel di luar payload."""
    out = []
    for r in rows:
        lab = r["Variables"] or r["Nama Column Raw"]
        if not lab or r["Nama Column BQ"]:
            continue
        if not r["Resource"] and not r["Path"]:
            r["Keterangan"] = (r["Keterangan"] + " | label tanpa mapping: " + lab).strip(" |")
            r["Variables"] = r["Nama Column Raw"] = ""
            out.append(f"label tanpa Resource dipindah ke Keterangan: {lab[:40]}")
        elif r["Resource"] in ("Organization", "Location") and r["Variables"]:
            r["Keterangan"] = (r["Keterangan"] + " | master data (lookup), tidak dihitung").strip(" |")
            r["Variables"] = ""
            out.append("label variabel di blok Organization/Location dihapus (lookup)")
    return sorted(set(out))


def r_path(r):
    return ep.norm_path(r["Path"])


def main(xlsx, schema_xlsx, repo):
    wb = openpyxl.load_workbook(xlsx, data_only=True)
    schema = load_schema(schema_xlsx)
    stats = OrderedDict()
    for slug, nama, sheet, a, b, table, trk, ref, ref_label in FORMS:
        book = section_book(wb, sheet, a, b)
        rows, log = ep.prepare(dict(slug=slug, nama=nama, sheet="s", hdr=0, var="Variables", raw="Nama Column Raw",
                                    bq="Nama Column BQ", tracker=trk, ref=ref, ref_label=ref_label),
                               book, None)
        for r in rows:          # nomor baris Excel asal
            r["_excel"] = r["_excel"] - 2 + a
            r["Nama Column BQ"] = ""   # kosong di sheet; diisi dari schema
        fields = schema[table]["fields"]
        fixes = fix_rows(rows)
        if section_book.shifted:
            fixes.append(f"{section_book.shifted} baris bergeser 1 kolom ke kiri (Resource di kolom Agregat/Individu) "
                         "dikembalikan")
        if slug == "balita-vitamin-a":
            fixes += vita_extra(rows)
        detail_pos = None
        if any(K(f) == "detail" for f, _ in fields):
            detail_pos = add_detail(rows)
        if any(K(f) == "tindakan" for f, _ in fields) and not has_mapped(rows, "tindakan"):
            add_detail(rows, name="Tindakan", url=TINDAKAN_URL,
                       note="asumsi 2026-11-24: pola sama dengan Detail (kolom aksi di tabel web SiGizi), perlu konfirmasi")
            fixes.append("tambah Encounter.extension sigizi-tindakan (asumsi)")
        fixes += drop_orphans(rows)
        blocks, payloads = ep.flag(rows)
        hit, miss = fill_bq(rows, fields, field_only=table in SHIFT_FIX)
        fixes += relocate_lookup(rows)
        if slug == "kohort-ibu":   # kunjungan bulanan = Encounter terpisah (kolom tanggal per bulan)
            n = 0
            for r in rows:
                if r["Path"] == "Encounter.identifier" and r["jumlah instance"] != "1":
                    r["jumlah instance"] = "1"
                    n += 1
            fixes.append(f"{n} Encounter tambahan (kunjungan bulanan Januari-Desember + kunjungan persalinan) "
                         "dihitung masing-masing")
        keep = [r for r in rows if any(r[c] for c in ep.OUT_COLS[:15])]
        ep.write_csv(f"{repo}/mapping/phdt-data-dictionary-sigizi-{slug}.csv", keep)
        vars_ = [r["Variables"] for r in keep if r["Variables"]]
        raw_unik = {K(r["Nama Column Raw"]) for r in keep if r["Nama Column Raw"]}
        stats[slug] = dict(
            nama=nama, sheet=sheet, baris_excel=f"{a}-{b or 'akhir'}", tabel_bq=table, tracker=trk, ref=ref,
            ref_label=ref_label, bq=len(fields), bq_cocok=len(hit), bq_tidak_ketemu=miss, bq_tanpa_raw=schema[table]["tanpa_raw"], bq_excluded=schema[table]["excluded"], fix=fixes,
            raw_header=sum(1 for f, raw in fields if raw), detail_ditambah=detail_pos is not None,
            var_unik=len(set(vars_)), raw_unik=len(raw_unik), baris_csv=len(keep),
            payload=sum(1 for r in keep if r["jumlah instance"] == "1"), code=sum(1 for r in keep if r["jumlah code"] == "1"),
            payload_per_resource=dict(Counter(x["res"] for x in payloads)),
            tidak_dihitung_res=dict(Counter(f'{x["res"]}: {x["reason"]}' for x in blocks if x["reason"])),
            kode_tanggal=len(log["kode_tanggal"]), resource_fix=Counter(map(tuple, log["resource_fix"])).most_common(6),
            resource_dari_path=log["resource_dari_path"])
        s = stats[slug]
        print(f"{slug:32s} BQ {s['bq']:3d} cocok {s['bq_cocok']:3d}  payload {s['payload']:4d} code {s['code']:4d}"
              f"  miss {miss}")
    os.makedirs("/home/claude/work", exist_ok=True)
    json.dump(stats, open("/home/claude/work/sigizi-stats.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
