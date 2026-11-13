#!/usr/bin/env python3
"""
parse_crosscheck.py — Kobo/survey "data dictionary" -> FHIR SatuSehat cross-check datasets.

Turns one data-dictionary CSV (one row per FHIR mapping line, with a
"Nama Variabel di Kobo" cell marking the first row of each survey
variable's block) into the JSON datasets the "Cross-Check Mapping"
dashboard reads:

  - forms_summary.json        1 row  (this form's totals)
  - resource_breakdown.json   1 row per FHIR resource *type*
  - instance_detail.json      1 row per actual FHIR resource *instance*
  - code_detail.json          1 row per raw terminology code
  - concept_consolidation.json 1 row per survey variable/concept

Design notes (read before changing the heuristics):

- A "variable block" = all rows from a non-empty "Nama Variabel di
  Kobo" cell up to (not including) the next non-empty one. This is a
  block-detection parse of a merged-cell spreadsheet export, not a
  structured schema — it only works because each new variable starts
  a fresh anchor cell.
- A "segment" is a maximal run of consecutive rows with the same
  non-empty Resource, bounded by blank rows or a Resource change.
- Segments of the SAME resource that are NOT adjacent (something else
  sits between them) are merged into one instance when their anchor
  field (first row's Path) repeats the SAME code value across
  segments (looks like a duplicate/continuation of the same resource
  in the sheet) -> confidence "needs_review", since this is a guess.
  They are kept as SEPARATE instances when the anchor code value
  DIFFERS between segments (e.g. EpisodeOfCare.type.coding = "ANC" in
  one segment, "PNC" in another -> clearly two different episodes)
  -> confidence "auto".
- Within one segment, anchor rows that share the same Path but have
  different "Value Name" are alternative coded options of ONE field
  (e.g. 3 rows for 3 answer options of "who entered the data"), not 3
  separate instances.
- Placeholder codes ("Tidak ada" / "Tidak Ada", case-insensitive) and
  "Reference ke ..." rows are not real terminology codes and are
  excluded from code_detail / code_systems counts.
- Nothing here is auto-trusted into a final number without a flag:
  anything the heuristic can't decide confidently is marked
  needs_review for a human to confirm (see CLI --confirm below).

Usage:
    python3 parse_crosscheck.py \
        --csv path/to/dictionary.csv \
        --form "Maternal Outcome (Kobo)" \
        --form-slug maternal-outcome \
        --source Kobo \
        --out-dir data/kobo/maternal-outcome/processed \
        [--confirm instance_id1,instance_id2,...]   # mark needs_review instances as confirmed

--confirm takes instance_id values printed by a prior run under
"NEEDS REVIEW" and flips their confidence to "confirmed" with a note
that a human checked it — it never silently guesses.
"""
import argparse
import csv
import json
import re
import sys
from datetime import datetime, timezone

PLACEHOLDER_CODES = {"tidak ada"}
PLACEHOLDER_SYSTEMS = {"tidak ada"}
REFERENCE_PREFIX = "reference ke"

MASTER_DATA_RESOURCES = {"Organization", "Location"}
# These resources are looked up against existing master data (a puskesmas's
# Organization/Location record already exists) rather than created fresh per
# submission. They're still listed in resource_breakdown/instance_detail for
# transparency (so a reviewer can see they were found and why they're out),
# but they are excluded from n_resource_types/n_instances_total/n_path_rows_total
# and from code_detail's counted (include=True) rows: matching a name to a
# master-data record isn't "using" a new terminology code.

STRUCTURAL_PATH_RULES = [
    (lambda p: p.endswith(".active"), "Field struktural (flag active), bukan jawaban variabel."),
    (lambda p: ".identifier" in p, "Kode/sistem identifier struktural, bukan isi jawaban variabel."),
    (lambda p: p.endswith(".address.country"), "Kode negara default, bukan isi variabel."),
    (lambda p: p.endswith(".status") or ".statusHistory." in p, "Status administratif FHIR, bukan jawaban variabel."),
    (lambda p: p == "Observation.category.coding", "Kategori administratif Observation, bukan isi jawaban."),
    (lambda p: p.startswith("Encounter.participant"), "Kode partisipan/administratif Encounter, bukan isi jawaban."),
]


def classify_structural(path):
    """Return an exclude_reason if `path` matches a known structural/
    boilerplate FHIR field (not the actual content of a survey answer), or
    None if it isn't one of those. The caller exempts a row that has its own
    non-empty "Value Name" -- a populated Value Name is the sheet's own
    signal that this row is one of several real, selectable answer options
    (not a fixed constant), so even a field that happens to match one of
    these patterns (e.g. a variable that genuinely asks for a status) is
    still counted when it carries a Value Name."""
    for pred, reason in STRUCTURAL_PATH_RULES:
        if pred(path):
            return reason
    return None


SYSTEM_CATEGORY_RULES = [
    ("snomed.info/sct", "SNOMED CT"),
    ("loinc.org", "LOINC"),
    ("terminology.hl7.org", "HL7 Terminology"),
    ("terminology.kemkes.go.id", "SatuSehat/Kemenkes"),
    ("fhir.kemkes.go.id", "SatuSehat/Kemenkes"),
    ("sys-ids.kemkes.go.id", "SatuSehat/Kemenkes"),
]

# Manual override for forms whose sheet leaves "Nama Column Raw" empty, so the
# dashboard can still show the real Kobo field name instead of the Indonesian
# label. Keyed by form_slug -> {row index of the variable's first row: raw_name}.
# Add overrides here when a sheet has no raw-name column; leave empty to fall
# back to slugifying the label.
RAW_NAME_OVERRIDES = {
    "maternal-outcome": {
        0: "data_entry_clerk_type",
        3: "data_entry_clerk_staff_id",
        4: "nik_yang_melakukan_entry_data",
        7: "nama_ibu",
        8: "nik_ibu",
        19: "puskesmas_name",
        56: "tanggal_pencatatan",
        94: "outcome_001",
        108: "delivery_date",
        120: "tanggal_meninggal",
        133: "tempat_meninggal",
        146: "sebab_meninggal",
    }
}


def slugify(text):
    s = re.sub(r"[^a-z0-9]+", "_", text.strip().lower()).strip("_")
    return s or "var"


def is_placeholder_code(code):
    return (code or "").strip().lower() in PLACEHOLDER_CODES


def is_placeholder_system(system):
    return (system or "").strip().lower() in PLACEHOLDER_SYSTEMS


def is_reference_row(code):
    return (code or "").strip().lower().startswith(REFERENCE_PREFIX)


def categorize_system(url):
    low = (url or "").lower()
    for needle, label in SYSTEM_CATEGORY_RULES:
        if needle in low:
            return label
    if not url or url.strip() == "":
        return "(tidak ada)"
    return "Lainnya"


def load_rows(csv_path):
    with open(csv_path, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def detect_variable_blocks(rows):
    """Return list of (start_idx, end_idx_exclusive, nv_label) for each
    'Nama Variabel di Kobo' block."""
    anchors = [i for i, r in enumerate(rows) if (r.get("Nama Variabel di Kobo") or "").strip()]
    blocks = []
    for n, start in enumerate(anchors):
        end = anchors[n + 1] if n + 1 < len(anchors) else len(rows)
        blocks.append((start, end, rows[start]["Nama Variabel di Kobo"].strip()))
    return blocks


def detect_resource_segments(rows):
    """Maximal runs of consecutive rows sharing the same non-empty Resource."""
    segments = []
    cur_res, cur_start = None, None
    for i, r in enumerate(rows):
        res = (r.get("Resource") or "").strip()
        if res != cur_res or res == "":
            if cur_res:
                segments.append((cur_start, i, cur_res))
            cur_res, cur_start = (res, i) if res else (None, None)
    if cur_res:
        segments.append((cur_start, len(rows), cur_res))
    return segments


def row_in_range(idx, start, end):
    return start <= idx < end


def segment_path_codes(rows, start, end):
    """Map Path -> set of Code values seen within one segment's rows."""
    m = {}
    for i in range(start, end):
        p = (rows[i].get("Path") or "").strip()
        c = (rows[i].get("Code") or "").strip()
        if p and c:
            m.setdefault(p, set()).add(c)
    return m


def build_instances(rows, segments):
    """Group segments into instances per the module docstring's heuristic.

    For a resource with more than one segment, look for a Path that
    appears in at least two segments ("shared path"). If some shared
    path has DIFFERENT code values across segments, that path is a
    real discriminator (e.g. EpisodeOfCare.type.coding = ANC vs PNC)
    -> segments are distinct instances, confidence "auto". If every
    shared path has the SAME value everywhere it appears (or there is
    no shared path at all), the segments look like separate row-ranges
    of the same instance's definition (e.g. a field list split by a
    stray block in the sheet) -> merge into one instance, confidence
    "needs_review" pending a human's --confirm.
    """
    by_resource = {}
    for seg in segments:
        by_resource.setdefault(seg[2], []).append(seg)

    instances = []  # each: {resource, row_indices:[...], confidence, note}
    for resource, segs in by_resource.items():
        if len(segs) == 1:
            start, end, _ = segs[0]
            instances.append({
                "resource": resource,
                "row_indices": list(range(start, end)),
                "confidence": "auto",
                "note": "",
            })
            continue

        seg_path_codes = [segment_path_codes(rows, s, e) for s, e, _ in segs]
        shared_paths = set(seg_path_codes[0])
        for m in seg_path_codes[1:]:
            shared_paths &= set(m)

        discriminator = None
        for p in sorted(shared_paths):
            values_per_seg = [m[p] for m in seg_path_codes]
            all_values = set().union(*values_per_seg)
            if len(all_values) > 1:
                discriminator = p
                break

        if discriminator:
            for (start, end, _), m in zip(segs, seg_path_codes):
                codes_here = ", ".join(sorted(m.get(discriminator, set())))
                instances.append({
                    "resource": resource,
                    "row_indices": list(range(start, end)),
                    "confidence": "auto",
                    "note": f"Instance terpisah (dibedakan oleh {discriminator} = {codes_here}).",
                })
        else:
            all_idx = []
            for start, end, _ in segs:
                all_idx.extend(range(start, end))
            instances.append({
                "resource": resource,
                "row_indices": all_idx,
                "confidence": "needs_review",
                "note": (f"{len(segs)} blok anchor terpisah untuk resource ini di sheet, "
                         "tidak ada field yang membedakan nilainya -> digabung jadi 1 instance, "
                         "tapi ini tebakan heuristik, perlu konfirmasi manual."),
            })
    return instances


def attribute_instance_to_concepts(instance, var_blocks):
    """Partition an instance's rows among the concept(s) whose OWN anchor
    row ("Nama Variabel di Kobo" cell) falls inside this instance.

    A concept's block runs from its anchor to the next anchor GLOBALLY, so
    intersecting that span with this instance's own row set gives exactly
    the rows of this instance that belong to that concept (blocks never
    overlap, so this partitions cleanly even when 2+ concepts land in one
    instance, e.g. "nama" + "NIK" both feeding one Practitioner).

    Rows in the instance that precede any concept's anchor (or when the
    instance has no anchor inside it at all) are left over: those are
    returned under owned_rows=None and the caller buckets them as
    'derived / no specific Kobo variable' rather than silently dropping
    them or mis-attributing them to the wrong concept.
    """
    idx_set = set(instance["row_indices"])
    hits = []
    claimed = set()
    for start, end, label in var_blocks:
        if start in idx_set:
            owned = sorted(idx_set & set(range(start, end)))
            hits.append((start, label, owned))
            claimed.update(owned)
    leftover = sorted(idx_set - claimed)
    return hits, leftover


def extract_code_rows(rows, row_indices, concept_id, concept_label, resource, form, source, form_slug,
                       master_data=False):
    out = []
    for idx in sorted(row_indices):
        r = rows[idx]
        code = (r.get("Code") or "").strip()
        system = (r.get("CodeSystem") or "").strip()
        if not code or is_placeholder_code(code) or is_reference_row(code):
            continue
        path = (r.get("Path") or "").strip()
        has_value_name = bool((r.get("Value Name") or "").strip())

        include, exclude_reason = True, ""
        if master_data:
            include, exclude_reason = False, "Resource ini master data (dicocokkan ke record existing), bukan instance baru per submission."
        elif not has_value_name:
            reason = classify_structural(path)
            if reason:
                include, exclude_reason = False, reason

        out.append({
            "form": form,
            "source": source,
            "concept_id": concept_id,
            "canonical_label": concept_label,
            "resource": resource,
            "path": path,
            "code": code,
            "display": (r.get("Display") or "").strip(),
            "system": system if not is_placeholder_system(system) else "",
            "category": categorize_system(system) if not is_placeholder_system(system) else "(tidak ada)",
            "include": include,
            "exclude_reason": exclude_reason,
            "row_id": f"{form_slug}:{idx}",
        })
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--csv", required=True)
    ap.add_argument("--form", required=True, help='Display name, e.g. "Maternal Outcome (Kobo)"')
    ap.add_argument("--form-slug", required=True, help="Slug used for raw-name overrides and ids")
    ap.add_argument("--source", required=True, help="Originating platform, e.g. Kobo, Epus")
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--confirm", default="", help="Comma-separated instance_ids to mark confirmed")
    args = ap.parse_args()

    rows = load_rows(args.csv)
    var_blocks = detect_variable_blocks(rows)
    segments = detect_resource_segments(rows)
    instances = build_instances(rows, segments)

    overrides = RAW_NAME_OVERRIDES.get(args.form_slug, {})
    # concept_id per variable block, keyed by its start row index
    block_concept_id = {}
    for start, end, label in var_blocks:
        block_concept_id[start] = overrides.get(start, slugify(label))

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    confirm_ids = {s for s in args.confirm.split(",") if s}

    instance_rows = []
    code_detail_rows = []
    concept_map = {}  # concept_id -> consolidated row
    resource_agg = {}  # resource -> {n_path_rows, n_instances, confidence(any needs_review), notes:[]}

    needs_review_report = []

    for i, inst in enumerate(instances):
        resource = inst["resource"]
        hits, leftover = attribute_instance_to_concepts(inst, var_blocks)
        concept_ids = [block_concept_id[start] for start, _, _ in hits]
        concept_labels = [label for _, label, _ in hits]
        instance_id = f"{args.form_slug}:{resource}:{i+1}"

        confidence = inst["confidence"]
        note = inst["note"]
        if instance_id in confirm_ids and confidence == "needs_review":
            confidence = "confirmed"
            note = note + " [Dikonfirmasi manual: dianggap 1 instance.]"
        elif confidence == "needs_review":
            needs_review_report.append(instance_id)

        is_master = resource in MASTER_DATA_RESOURCES
        display_confidence = "master_data" if is_master else confidence
        display_note = ("Master data (dicocokkan ke record existing berdasarkan nama/identitas), "
                         "tidak dihitung sebagai instance baru per submission.") if is_master else note

        instance_rows.append({
            "instance_id": instance_id,
            "form": args.form,
            "source": args.source,
            "resource": resource,
            "concept_ids": concept_ids,
            "concept_labels_display": ", ".join(concept_labels) if concept_labels else "(tidak terhubung ke variabel Kobo spesifik)",
            "n_path_rows": len(inst["row_indices"]),
            "confidence": display_confidence,
            "note": display_note,
            "counted": not is_master,
        })

        agg = resource_agg.setdefault(resource, {"n_path_rows": 0, "n_instances": 0, "needs_review": False, "notes": []})
        agg["n_path_rows"] += len(inst["row_indices"])
        agg["n_instances"] += 1
        if confidence == "needs_review":
            agg["needs_review"] = True
        if note:
            agg["notes"].append(note)

        attributions = [(start, label, owned) for start, label, owned in hits]
        if leftover:
            derived_cid = f"_derived_{slugify(resource)}"
            attributions.append((None, "(derived, tidak ada variabel Kobo langsung)", leftover))
            block_concept_id.setdefault(None, derived_cid)  # harmless; not read back by key None elsewhere

        for start, label, owned in attributions:
            cid = f"_derived_{slugify(resource)}" if start is None else block_concept_id[start]
            crows = extract_code_rows(rows, owned, cid, label, resource, args.form, args.source, args.form_slug,
                                       master_data=is_master)
            code_detail_rows.extend(crows)
            entry = concept_map.setdefault(cid, {
                "concept_id": cid, "canonical_label": label, "forms": [], "sources": [],
                "variants": [], "unique_codes": set(),
            })
            if args.form not in entry["forms"]:
                entry["forms"].append(args.form)
            if args.source not in entry["sources"]:
                entry["sources"].append(args.source)
            entry["variants"].append({"form": args.form, "source": args.source, "resource": resource, "n_path_rows": len(owned)})
            for cr in crows:
                if cr["include"]:
                    entry["unique_codes"].add(cr["code"])

    # resource_breakdown.json
    resource_breakdown_rows = []
    for resource, agg in resource_agg.items():
        is_master = resource in MASTER_DATA_RESOURCES
        if is_master:
            confidence, note = "master_data", ("Master data (referensi ke record existing), tidak dihitung sebagai "
                                                "resource/instance baru dalam total.")
        else:
            confidence = "needs_review" if agg["needs_review"] else "auto"
            note = " / ".join(n for n in agg["notes"] if n)
        resource_breakdown_rows.append({
            "resource": resource,
            "form": args.form,
            "source": args.source,
            "n_path_rows": agg["n_path_rows"],
            "n_instances": agg["n_instances"],
            "confidence": confidence,
            "note": note,
            "counted": not is_master,
        })

    # concept_consolidation.json
    concept_rows = []
    for cid, entry in concept_map.items():
        codes_sorted = sorted(entry["unique_codes"])
        resources_used = sorted(set(v["resource"] for v in entry["variants"]))
        is_master = any(r in MASTER_DATA_RESOURCES for r in resources_used)
        multi_resource = len(resources_used) > 1
        if is_master:
            review_flag, review_reason = "MASTER DATA", "Dicocokkan ke master data existing, kodenya tidak dihitung."
        elif multi_resource:
            review_flag, review_reason = "PERLU REVIEW", "Konsep sama dipetakan ke resource FHIR berbeda di form berbeda."
        else:
            review_flag, review_reason = "OK", ""
        concept_rows.append({
            "concept_id": cid,
            "canonical_label": entry["canonical_label"],
            "n_forms": len(entry["forms"]),
            "forms": entry["forms"],
            "sources": entry["sources"],
            "variants": entry["variants"],
            "n_path_rows": sum(v["n_path_rows"] for v in entry["variants"]),
            "unique_codes": codes_sorted,
            "needs_review": multi_resource and not is_master,
            "review_reason": review_reason,
            "resources_used": ", ".join(resources_used),
            "unique_codes_display": ", ".join(codes_sorted) if codes_sorted else "–",
            "n_unique_codes": len(codes_sorted),
            "forms_display": ", ".join(entry["forms"]),
            "sources_display": ", ".join(entry["sources"]),
            "review_flag": review_flag,
        })

    total_unique_codes = len({c["code"] for c in code_detail_rows if c["include"]})
    total_systems = len({c["system"] for c in code_detail_rows if c["include"] and c["system"]})

    # code_systems.json: one row per distinct system URL actually in use (not
    # the coarser category bucket), for a human-readable reference snapshot.
    # The live dashboard recomputes this itself from code_detail so it always
    # reflects the current include/exclude_reason flags; this file is just a
    # point-in-time copy for the repo.
    sysmap = {}
    for c in code_detail_rows:
        if not c["include"] or not c["system"]:
            continue
        e = sysmap.setdefault(c["system"], {"system": c["system"], "category": c["category"], "n_uses": 0})
        e["n_uses"] += 1
    code_systems_rows = sorted(sysmap.values(), key=lambda r: (-r["n_uses"], r["system"]))

    counted_breakdown = [r for r in resource_breakdown_rows if r["counted"]]
    forms_summary_row = {
        "form": args.form,
        "source": args.source,
        "n_variables": len(var_blocks),
        "n_resource_types": len(counted_breakdown),
        "n_instances_total": sum(r["n_instances"] for r in counted_breakdown),
        "n_path_rows_total": sum(r["n_path_rows"] for r in counted_breakdown),
        "n_unique_codes": total_unique_codes,
        "n_systems": total_systems,
        "n_master_data_resources": len(resource_breakdown_rows) - len(counted_breakdown),
        "status": "needs_review" if any(r["confidence"] == "needs_review" for r in resource_breakdown_rows) else "ok",
        "n_flags": sum(1 for r in resource_breakdown_rows if r["confidence"] == "needs_review"),
    }

    def write_json(name, rows_, meta):
        path = f"{args.out_dir}/{name}"
        with open(path, "w", encoding="utf-8") as f:
            json.dump({"rows": rows_, "meta": meta}, f, ensure_ascii=False, indent=2)
        print(f"wrote {path} ({len(rows_)} rows)")

    edit_meta = [{"label": "Dihasilkan oleh", "value": "scripts/parse_crosscheck.py", "type": "code"},
                 {"label": "Diproses (UTC)", "value": now}]

    write_json("forms_summary.json", [forms_summary_row], edit_meta)
    write_json("resource_breakdown.json", resource_breakdown_rows, edit_meta)
    write_json("instance_detail.json", instance_rows, edit_meta)
    write_json("code_detail.json", code_detail_rows, edit_meta)
    write_json("concept_consolidation.json", concept_rows, edit_meta)
    write_json("code_systems.json", code_systems_rows, edit_meta)

    if needs_review_report:
        print("\nNEEDS REVIEW (not auto-counted as confirmed, re-run with --confirm id1,id2 once a human checks):")
        for iid in needs_review_report:
            print(" -", iid)
    else:
        print("\nNo needs_review instances.")


if __name__ == "__main__":
    main()
