# Post-batch-8 audit + raw-corpus assembly

Run of 13 Aug 2026. Supersedes parts of `NEXT-RUN-brief-regions-6.md` — see **CORRECTIONS** below.
**Nothing was written to any theme, snippet, metafield or page.** Store changes: none.

---

## STATE — verified, not assumed

- Shopify connector confirmed on **thejiujitsumindset.com** (`get-shop-info`).
- **LL `154883129516` is now MAIN.** It was published. JJ is back to UNPUBLISHED.
- Rollback stack intact and confirmed present: KK `154881523884`, JJ `154865860780`,
  II `154862780588`, HH `154860028076`. GG / FF / audit-harness confirmed **gone**.
- Live corpus: **5,911 stored / 692 suppressed records / 5,219 published / 61 regions.**
  All nine post-batch-7 region counts (TN 52 · NS 29 · AK 14 · NB 15 · NL 13 · PE 10 ·
  DE 8 · DC 6 · NE 21) reproduce **exactly** from the corpus. Nebraska is 21. ✔
- The C4 invariant `stored − suppressed RECORDS == published` holds: 5,911 − 692 = 5,219,
  from **690** suppression names. The two declared multi-match entries are the only ones:
  `MD | Southern Maryland Martial Arts & Fitness` and `VA | Capital MMA & Elite Fitness`. ✔

---

## ⚠️ POST-PUBLISH STEPS WERE NEVER RUN

`metafieldsSet` has **not** been run for batch 7. Proof: the 61 page-level `title_tag`
counts sum to **5,205** — exactly the pre-LL (theme JJ) total. Six of the eight batch-7
regions advertise a stale number in search results right now:

| region | metafield says | actually live | drift |
|---|---|---|---|
| TN | 34 | **52** | −18 |
| NS | 23 | **29** | −6 |
| AK | 22 | **14** | +8 |
| NL | 15 | **13** | +2 |
| DE | 7 | **8** | −1 |
| DC | 7 | **6** | +1 |
| NB | 15 | 15 | ✔ coincidence — NB was unchanged |
| PE | 10 | 10 | ✔ coincidence — PE was unchanged |

Every other region's count is correct, and **all 22 `across N cities` claims are correct**.

### The city-list check the brief demanded — five defects, three different kinds

Descriptions name example cities. Five name a city with **zero live records**:

| region | city named | stored | published | kind |
|---|---|---|---|---|
| AK | **Wasilla** | 2 | **0** | new in batch 7 — both records suppressed |
| CT | New Haven | 1 | **0** | pre-existing — sole record suppressed |
| GA | Columbus | 1 | **0** | pre-existing — sole record suppressed |
| NJ | Cherry Hill | **0** | **0** | never existed in the corpus at all |
| NY | New York City | 0 | 0 | cosmetic — filed as `New York` (40) + boroughs |

All five confirmed against a city-name **fold** (case/punctuation-insensitive), so none is a
spelling artefact. NY is defensible as SEO copy; the other four are not. **Do not simply
update the numbers — fix these city lists in the same pass**, which is exactly what the
brief's "check the city lists, not just the numbers" warned about.

---

## THE RAW CORPUS — backlog item 2 is DONE

**All 45 data files are on disk and MD5-verified against LL**, in `scratch/raw-datafiles/`
(676,240 B). Every checksum was re-verified by me after the agents returned; no agent report
was taken on trust.

Two corrections to the brief's inventory:

- **`scratch/raw-G1-legacy.txt` IS the legacy blob**, byte-for-byte —
  MD5 `1ee054115f5f2a4ab7b96a1a4395e342`, 113,187 B. It never needed fetching.
- **39–42 were already on disk** (in `build-b3/`, `build-b4/`, `build-b5/`, `build-b6a/`),
  and 13 / 21 / 29 / 33 were already in `scratch/` as `raw-G1-*.txt`, all MD5-clean.
  Only **2–12, 14–20, 22–28, 30–32, 34** genuinely had to be pulled — 29 files, not 33.
- ⚠️ `build-b4/tjjm-gyms-data.liquid` is a **stale, 1-byte-truncated** copy of the legacy
  blob (113,186 B, MD5 `c7ee895c…`). It does **not** match LL. Do not use it.

### Artifacts

| file | what it is |
|---|---|
| `scratch/raw-datafiles/` | all 45 data files, byte-exact, MD5-verified vs LL |
| `scratch/ll-datafile-manifest.tsv` | filename → checksumMd5 → size, straight from LL |
| `scratch/raw-corpus-LL.json` | **5,911 records, raw stored `{n,c,s,w,a,src}`, NO overrides applied** |
| `scratch/raw-corpus-LL.tsv` | same, flat, + override / effective / link-state columns |
| `scratch/repoint-targets-LL.tsv` | the 833 published records that render with no link |

`raw-corpus-LL.json` carries, per record: raw `w` **and** `w_present` (so "no `w` key" is
distinguishable from `w: ""`), raw `a`, the override value and which of the three files it
came from, `suppressed`, and `region` with the NE/NL city split already applied.

**Proof it is genuinely raw:** 51 records carry a stored `w` that differs from what the page
renders (e.g. `AB YYC Brazilian Jiu Jitsu` stores `yycbjj.com`, renders `www.yycbjj.ca`).
This is the artifact the deleted harness `154657063084` used to provide.

---

## GATE CHECKS RUN AGAINST THE LIVE CORPUS

- **C10 — no live duplicate names: PASSES.** Zero duplicate names among the 5,219 published
  records. The batch-8 disambiguation held.
- **C9 — no override restates a stored value: PASSES.** Zero no-op overrides.
- **C5 — no name contains `|` or `~`: PASSES.**
- **Orphan overrides: zero.** Every one of the 590 override names matches a real record.

### ⚠️ The residual latent-duplicate set is 15, not 4

The brief lists four names with a second suppressed copy. There are **fifteen**:

`Aurora BJJ` · `Capital MMA & Elite Fitness` (3 stored) · `Carlson Gracie Jiu Jitsu` ·
`Connection Rio Jiu-Jitsu Academy` · `Core Combat Sports` · `EchoValor Striking & MMA` ·
`Evolution Jiu Jitsu` · `Impact Martial Arts` · `Infinite Jiu-Jitsu` ·
`Integrity Martial Arts` · `Logic Jiu Jitsu` · `Midwest Training Center` ·
`Northwest Fighting Arts` · `Red River BJJ` · `Zombie Brazilian Jiu-Jitsu and MMA`

Safe today. Each would collide the moment a future batch un-suppressed the second copy.
Run C10 as a standing check, as the brief says — but against this list of 15.

### ⚠️ Three duplicate override entries — two are load-bearing

593 override lines collapse to 590 names. The three collisions resolve by file order, and
**two of them only work by accident**:

| name | earlier | later (wins) |
|---|---|---|
| `Stratford BJJ PEI` | w2: *blank* | w3: `https://www.peimma.com/stratford` |
| `Team Fortitude NS` | w2: *blank* | w3: `https://www.facebook.com/FortitudeJiujitsu` |
| `Fighting Gravity Jiu Jitsu` | w2: *blank* | w2: *blank* (harmless, redundant) |

Both PEI and NS links survive **only** because the section renders file 3 after file 2. Delete
the stale w2 blanks — this is precisely the "edit the existing entry rather than appending a
duplicate" rule, violated twice in batch 7.

### ⚠️ Backlog item 11 is wrong — SIX files fail strict JSON, not four

`29, 30, 31, 32, 33, 34` — the brief names only 30/31/32/34.
The fault is **identical and structural** in all six: objects are concatenated as `}{` with
no separating commas and no enclosing `[...]`. No individual record is malformed — every
`{…}` chunk parses cleanly on its own. That is why they render fine. Files 1–28 and 35–45
are all strict-valid. (`-44` re-confirmed clean.)

---

## LINK STATE OF THE PUBLISHED CORPUS — the repointing baseline

Of 5,219 published records, **4,386 render a link and 833 render none**:

| cause | n |
|---|---|
| blanked by an override | 471 |
| no `w` key at all | 252 |
| stored `w` is an empty string | 110 |

Concentration: FL 83 · TX 76 · CA 75 · NJ 43 · OK 35 · CO 34 · LA 33 · GA 32 · IL 30.

Effective-scheme spread across the 4,386 live links: **2,377** `https://`, **1,510**
`http://`, **499 scheme-less** (the section prepends `https://` at render time).

`scratch/repoint-targets-LL.tsv` is the worklist, with the raw stored `w` and the reason each
record is blank. At batch 7's measured yield of one recovery per 1.8 attempts, 833 targets is
the largest single pool of recoverable value left on the project.

---

## WHAT'S NOW UNBLOCKED

Backlog item 3 (repointing / browser-render pass) has its prerequisite. Item 11 is retired
apart from correcting its file list. The raw dump also stands in for the deleted harness for
every future session.

---

## METAFIELD FIX — DONE, 13 Aug 2026

15 metafields across 9 pages via `metafieldsSet`, `userErrors: []`, all verified by
independent read-back. Rollback strings: `batches/metafields-b8-rollback.md`.

- Counts corrected on **TN 34→52 · NS 23→29 · AK 22→14 · NL 15→13 · DE 7→8 · DC 7→6**.
- Dead cities replaced: **AK** Wasilla→Juneau · **CT** New Haven→Norwalk ·
  **GA** Columbus→Lawrenceville · **NJ** Cherry Hill→Toms River.
- CT / GA / NJ titles left untouched — their counts were already right.
- **NY left alone deliberately** (see rollback file).

**The 61 metafield counts now sum to 5,219 — equal to the live corpus.** No inconsistency
window is open: LL is already MAIN, so the metafields and the rendered pages agree.

---

## HOW MUCH OF THE CORPUS IS ACTUALLY AUDITED?

All 61 regions have been *touched*. By **records**, the picture is very different:

| tier | regions | records | share | what was done |
|---|---|---|---|---|
| **A — fully rebuilt** | 26 | 835 | **16%** | batches 3–7: stored originals screened one by one AND new research added |
| **B — additive only** | 7 | 267 | **5%** | batches 1–2 (ME AR ON UT SK ND WY): new schools added, **stored originals never screened** — this is backlog item 6 |
| **C — never region-rebuilt** | 28 | 4,117 | **79%** | corpus-wide mechanical screens only |

Tier A: BC AB QC MN TN ID HI KS IA NM SC NH NS WV MS RI MB NE NB AK NL VT SD PE DE DC
Tier B: ON AR UT ME SK ND WY
Tier C: CA 460 · TX 351 · FL 328 · NJ 210 · NY 182 · AZ 173 · CO 156 · GA 152 · PA 148 ·
MA 140 · OH 137 · VA 137 · IL 130 · NC 125 · WA 121 · NV 118 · OR 118 · MI 115 · LA 100 ·
MO 98 · OK 98 · MD 94 · CT 85 · WI 85 · IN 80 · AL 78 · KY 65 · MT 33

**Tier C is not untouched** — it has had the 5 Aug corpus-wide domain-collision audit, the
6 Aug link/DNS audit (all 61 pages, 4,282 linked records, 905 flagged), and per-state
curation at MatMade import time. **NY (182) and OR (118) were additionally curated
end-to-end** in their own sessions.

So: **roughly 1,135 records (~22%) have had a school-by-school body-read audit. ~73% have
had mechanical screening only.**

### Why that 73% should not be assumed clean

Every time stored originals *have* been screened, the defect rate was high and **rising with
region size**:

| batch | research-output defect rate |
|---|---|
| 3 (IA KS MB SD) | 29% |
| 4 (NM HI ID VT RI) | 33% |
| 5 (MN SC MS NE NH) | 34% |
| 6a (WV AB) | 46% |
| 6b (BC QC) | **84%** |

And on *stored records*, Delaware came in at **7 of 7 defective**. Batch 6's own conclusion —
"the larger and less-curated the region, the worse" — points directly at tier C, which is
both the largest and the least curated. RULES §2 makes the same point structurally: the
collision check is blind to never-imported duplicates, same-city duplicates on different
domains, multi-tenant hosts and single-record brand roots. None of those are visible to any
screen tier C has had.

### Scale of the remaining work

Batches 3–7 audited 835 records across five working sessions — about **165 records per
session**. Tier C is 4,117 records. At the same rate that is **~25 sessions**, and the rate
will likely be worse, since tier C regions are 5–10× larger than the small regions batches
3–7 handled (CA + TX + FL alone are 1,139 records — more than tiers A and B combined).

Tier B is much cheaper: 267 records, ~2 sessions, and it is the highest-yield remaining
audit because those regions are *known* to have unscreened originals.

---

## RECOMMENDED NEXT ACTIONS, in order

1. ~~Run `metafieldsSet`~~ — **DONE 13 Aug 2026.**
2. **Delete the two stale w2 blank entries** for `Stratford BJJ PEI` and `Team Fortitude NS`.
   Currently correct only by file-render order.
3. **Item 3, the repointing pass**, against `scratch/repoint-targets-LL.tsv` — 833 targets,
   now fully unblocked.
4. **Item 6, tier B re-screen** (ME AR ON UT SK ND WY, 267 records). Cheapest real audit left.
5. **Tier C**, largest first or smallest first — but scope it as a programme, not a session.
