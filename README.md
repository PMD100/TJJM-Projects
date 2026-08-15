# TJJM Gym Directory — data, tooling and audit trail

Canonical data and build tooling for the Brazilian Jiu Jitsu school directory on
**thejiujitsumindset.com**. As of Aug 2026: **5,215 published records across 61 regions**.

**This repo does not contain the Shopify theme and is not connected to Shopify.** It is the
source of truth for the *data*, the *build scripts*, and the *audit trail*. Files are written to
Shopify separately via the Admin API and verified by MD5.

---

## Why this repo exists

Shopify caps a store at 20 themes. Themes were being deleted to stay under that cap, and the
themes were the only record of what had been published — HH, II, JJ and KK are already gone.

**Everything needed to reconstruct or roll back any batch now lives here instead**, so old themes
can be deleted freely.

---

## Layout

| path | what it is |
|---|---|
| `scratch/raw-corpus-LL.json` | **The canonical corpus.** 5,911 records, raw stored `{n,c,s,w,a,src}`, no overrides applied. All verification runs against this. |
| `scratch/raw-corpus-LL.tsv` | Same, flat, plus override / effective-URL / link-state columns. |
| `scratch/raw-datafiles/` | All 45 `tjjm-gyms-data*` snippets, **MD5-verified against the live theme**. |
| `scratch/ll-datafile-manifest.tsv` | filename → checksumMd5 → size, straight from Shopify. |
| `scratch/repoint-targets-LIVE.tsv` | Current worklist: published records that render no link. |
| `build-b3/` … `build-b18/` | **The exact files written to each theme**, one directory per batch. This is the deployment history. |
| `batches/` | Verdict TSVs, override manifests, corrections, metafield rollback strings. The audit trail. |
| `build_b*.py` | Per-batch gate + build scripts. `build_b9.py` onward are the reusable pattern. |
| `gate_b7.py` | The nine-condition collision gate, for batches that **add** records. `--seed` and `--dump`. |
| `RULES-tjjm.md` | **Read first.** Durable rules and the evidence behind them. |
| `NEXT-RUN-brief-regions-*.md` | Session briefs. Highest number wins. |
| `region-rebuild-batch*-findings.md` | Per-batch findings. |

---

## The data model in one page

Records live in Liquid snippets in the theme:

- `snippets/tjjm-gyms-data.liquid` — a 113 KB legacy blob, 1,304 records. **Cannot be rewritten
  through the Admin API toolchain.** Fixes needing a change to `n`, `c` or `s` inside it require
  suppress-plus-add.
- `snippets/tjjm-gyms-data-2` … `-45` — per-state imports. Record shape `{n,c,s,w,a}`.
  **Names must not contain `|` or `~`** — both are field separators.

Three override layers, rendered in order, later wins:

- `snippets/tjjm-gym-websites.liquid`, `-2`, `-3` — `~Name|URL~` overrides the stored `w`.
  **An empty value blanks the link.** Matches on name alone, corpus-wide.
- `snippets/tjjm-gym-addresses.liquid` — `~Name|Address~`, fills a blank `a` only.
- `snippets/tjjm-removed-index.liquid` — suppressed names, one row per region code.
  Suppression is a render-time filter; the record stays in the blob.

⚠️ **Counts live in three places.** See `RULES-tjjm.md` §10. Getting this wrong put three wrong
numbers on every region page in Aug 2026.

⚠️ **Newfoundland is stored under Nebraska's code** and re-filed by a hardcoded city list in the
section. See `RULES-tjjm.md` and the batch-7 findings before touching NE or NL.

---

## Working rules

- **Verify every theme write by MD5 yourself.** Never trust a write agent's report. Re-query after
  any agent failure — two agents were lost mid-write in one session.
- **An overrides-only batch cannot move record counts**, and you can prove it by checksumming every
  count-bearing file against the previous theme. That is stronger than a count sweep.
- **Move, don't edit.** When a record has a blanking entry in websites-1 or -2 and you now have a
  real URL, *delete* the old entry and write the URL into file 3. Editing in place grows the file
  toward the ~24 KB Admin API ceiling; moving shrinks it.
- **`themePublish` is blocked** — the owner publishes. `themeFilesUpsert` is blocked on MAIN, so
  duplicate first.

## Gates

`build_b*.py` enforce, and refuse to write on failure:

- **C3** no name in more than one override file, none twice in one file
- **C5** no name contains `|` or `~`
- **C9 / C9b** a new URL must differ from the stored value *and* from the current override
- **C11** every target name matches exactly one published record
- **BYTES** every file asserted under the ~24,576 B ceiling before writing
- post-build re-parse: every URL present and correct, zero duplicate names corpus-wide

---

## Status, Aug 2026

- 5,215 published records / 61 regions. 4,548 render a link; 637 render none.
- Link-repointing programme: **522 targets checked, 190 links restored**, blank records down from
  833 — a 24% reduction. Steady yield of one recovery per 2.7 attempts.
- Audit coverage: ~28.5% of records individually examined; ~66% have had mechanical screening only.
  See `POST-BATCH-8-audit-2026-08-13.md`.
