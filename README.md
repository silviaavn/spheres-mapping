# spheres-mapping

Cross-check pipeline for mapping survey/data-dictionary CSVs (Kobo now, more
sources later — e.g. Epus) against their FHIR SatuSehat mappings. Built to
scale to 100+ forms across multiple source platforms.

The output feeds the "Cross-Check Mapping" dashboard
(https://claude.ai/artifact/FvPoMiwoUewgPC9natz27M).

## Layout

```
scripts/parse_crosscheck.py          core parser (reusable across forms/sources)
data/<source>/<form-slug>/raw/       original data-dictionary CSV
data/<source>/<form-slug>/processed/ generated JSON (see below)
```

## Running it

```
python3 scripts/parse_crosscheck.py \
  --csv data/kobo/maternal-outcome/raw/Kobo_-_Data_Dictionary_-_Maternal_Outcome_Kobo.csv \
  --form "Maternal Outcome (Kobo)" \
  --form-slug maternal-outcome \
  --source Kobo \
  --out-dir data/kobo/maternal-outcome/processed \
  --confirm "maternal-outcome:Organization:4,maternal-outcome:Encounter:6"
```

`--confirm` takes a comma-separated list of `form-slug:resource:anchor_row_index`
entries — a human sign-off that a `needs_review` instance split/merge is
correct, after you've checked it in the dashboard.

Outputs six JSON files per form: `forms_summary`, `resource_breakdown`,
`instance_detail`, `code_detail`, `concept_consolidation`, `code_systems`.
Each is uploaded as a dataset in the dashboard artifact.

## What counts as an "instance" and what counts as a "meaningful code"

These rules came out of a back-and-forth refining the methodology; written
down here so the next form is processed the same way.

- **Variable blocks**: a non-empty "Nama Variabel di Kobo" cell starts a new
  variable's block; the block runs to the next such cell.
- **Resource instances**: consecutive rows sharing a "Resource" value form a
  segment. Segments of the same resource are merged into one instance unless
  a **shared discriminator Path** — a Path common to all the segments, whose
  *value* differs between them (e.g. `EpisodeOfCare.type.coding` = ANC vs
  PNC, or `Observation.category.coding` = vital-signs vs survey) — proves
  they're genuinely separate instances. Two anchor rows for the same resource
  is not automatically two instances.
- **Master-data resources are not counted as new instances.** `Organization`
  and `Location` are reference lookups — matched against existing master
  data (e.g. by Puskesmas name), not created fresh per submission. They still
  appear in the breakdown/instance tables (tagged `master_data`) for
  transparency, but are excluded from every instance/resource-type count.
- **Structural/boilerplate codes are excluded from the "meaningful codes"
  count.** `active`, `identifier`, `country`, `status`, `Observation.category`,
  and `Encounter.participant` are structural scaffolding, not information the
  variable is actually collecting — *unless* the row's own **Value Name**
  column is populated, which signals it's one of several genuine selectable
  answer options rather than a fixed constant (e.g. `Observation.status`
  rows that are literally the answer being recorded, not a hardcoded
  `"final"`). Excluded rows are kept in `code_detail` with `include: false`
  and an `exclude_reason`, never silently dropped.

## Dashboard

The dashboard (Claude Dashboard artifact) reads these JSON files as
datasets and is filterable by source and by form. It shows, live-computed
from the uploaded data (no hardcoded totals): per-row code/system detail
with an include/exclude filter and CSV download, a per-form summary, an
instance-level table + chart per FHIR resource type, a terminology-system
summary, and cross-form concept consolidation. Explanations and methodology
notes live in chat with Claude, not on the page itself.

## Adding a new form or source

1. Drop the raw CSV under `data/<source>/<form-slug>/raw/`.
2. If the sheet has no "Nama Column Raw" column, add the anchor-row → raw
   Kobo field name mapping to `RAW_NAME_OVERRIDES` in
   `scripts/parse_crosscheck.py`.
3. Run the script with `--source`/`--form`/`--form-slug` for the new form.
4. Upload the six resulting JSON files as datasets in the dashboard
   (same dataset ids, so the page doesn't need to change).
