# Session brief — POST-BATCH-9. Start here.

Written 13 Aug 2026. **Supersedes `NEXT-RUN-brief-regions-6.md`, which is now substantially
wrong — see CORRECTIONS.** The region-rebuild programme is finished; all 61 regions are curated.
What remains is the **audit debt**, which is much larger than brief 6 implied.

Paste the block below into a **new** chat with the `TJJM Projects` folder connected.

---

## The block to paste

> Continuing the TJJM BJJ directory. Read `NEXT-RUN-brief-regions-7.md` first, then
> `RULES-tjjm.md`, then `region-rebuild-batch9-findings.md` and
> `POST-BATCH-8-audit-2026-08-13.md`. RULES is canonical where they overlap **except** for the
> removed-index scoping correction, the NE/NL split, and **the DNS/cache correction in batch 9**,
> where the later findings are newer and proven.
>
> **Everything through batch 9 is DONE and PUBLISHED.** Theme **MM** (`154892861612`) is MAIN.
> Before anything: **confirm the Shopify connector is on thejiujitsumindset.com** (it has
> silently switched stores once), then re-verify MAIN and the record count against STATE below.
>
> A complete **raw corpus already exists** — `scratch/raw-corpus-LL.json`, 5,911 records with
> true stored `w`. Do not rebuild it and do not re-fetch the data files; they are all in
> `scratch/raw-datafiles/`, MD5-verified. Regenerate only if the corpus changes.

---

## STATE

| theme | id | role |
|---|---|---|
| **MM** | `154892861612` | **MAIN** — batch 9, URL repointing |
| LL | `154883129516` | rollback — batch 7 + disambiguation |
| KK | `154881523884` | rollback |
| JJ | `154865860780` | rollback |

⚠️ **HH `154860028076` and II `154862780588` have been deleted** since brief 6. So have GG, FF
and the audit-dump harness `154657063084`. Assume any theme older than JJ is gone.

**Live corpus: 5,911 stored · 692 suppressed records (from 690 names) · 5,219 published ·
61 regions.** Verified cookie-free on the live site: the region nav sums to exactly 5,219.

**Links: 4,417 of 5,219 published records render a link. 802 render nothing.**

Next data file is **`tjjm-gyms-data-46`**. Next theme letter is **NN**.

### SEO metafields — correct as of 13 Aug
All 61 `title_tag` counts sum to 5,219 and match the live pages. Rollback strings for the last
change are in `batches/metafields-b8-rollback.md`. **No metafield work is outstanding.**

### File headroom (as of MM)
- `sections/tjjm-state-directory.liquid` — 12,906 B of ~24,576. Each data file costs +34 B.
- `snippets/tjjm-gym-websites-2.liquid` — **20,922 B. ~3.6 KB left — treat as full.**
- `snippets/tjjm-gym-websites-3.liquid` — **1,609 B. Put new overrides here.**
- `snippets/tjjm-gym-addresses.liquid` — 8,455 B. Plenty.
- `snippets/tjjm-removed-index.liquid` — 13,749 B, 60 region rows.

Override entries total **604** across the three files, **zero duplicate names**, 522 blank.

---

## ⚠️ CORRECTIONS TO BRIEF 6 — it is wrong on all of these

1. **LL was published, and MM is now MAIN.** Brief 6 says nothing may have been published.
2. **The raw-corpus prerequisite (its backlog item 2) is DONE.** All 45 data files are in
   `scratch/raw-datafiles/`, MD5-verified against the theme.
3. **`scratch/raw-G1-legacy.txt` IS the legacy blob**, byte-identical (MD5 `1ee054…`, 113,187 B).
   Brief 6 implies it is only a partial dump.
4. **Data files 39–42 were never missing** — they are in `build-b3/`, `build-b4/`, `build-b5/`,
   `build-b6a/`. Nor were 13, 21, 29, 33 (in `scratch/` as `raw-G1-*.txt`).
5. ⚠️ **`build-b4/tjjm-gyms-data.liquid` is a stale, 1-byte-truncated copy of the legacy blob.**
   It does NOT match the theme. Never use it.
6. **SIX data files fail strict JSON, not four**: `29, 30, 31, 32, 33, 34`. Identical structural
   cause in all six — objects concatenated as `}{` with no commas and no array wrapper. No
   individual record is malformed, which is why they render. Its backlog item 11 is otherwise
   retired.
7. **The residual latent-duplicate set is 15 names, not 4.** Full list in
   `POST-BATCH-8-audit-2026-08-13.md`.
8. **Brief 6's "all 61 regions curated" badly overstates coverage.** By *records*, only ~16% have
   had originals screened. See COVERAGE below — this is the single most important correction.

---

## ⚠️ NEW STANDING METHOD — DNS-check every candidate URL

**`web_fetch` serves cached copies of domains that no longer exist.** Eight domains in batch 9
returned long, convincing bodies — correct branding, addresses, named black belts, testimonials —
while being NXDOMAIN at the authoritative servers. Search indexes serve stale titles the same way.
On one, a researcher would have published a dead link **and** transcribed a named black belt's
credentials from a defunct site — the fabrication failure `METHOD-RULES-agent.md` forbids, reached
completely honestly.

**Before believing any URL:**

    web_fetch  https://dns.google/resolve?name=<hostname>&type=A

- `Status: 3` → NXDOMAIN → conclusively DEAD
- `Status: 0` **with an `Answer` array carrying A records** → alive
- `Status: 0` with no Answer → no A record → dead
- Registered but nameservers REFUSE (lame delegation) → dead. Seen on `usajujitsu.net`, `rtbjjai.com`

This supersedes RULES §4 in **both** directions: an empty body is not evidence of death (live JS
sites return empty), and a full body is not evidence of life (caches lie). **Run it even when the
page renders perfectly.** Known-poisoned in batch 9: `agogiac.com`, `gbwestpalm.com`,
`ironsidemartialarts.com`, `renatotavaresbjj.com`, `toddcutlerbjj.com`, `gradysmma.com`,
`tridentjiujitsu.com`, `westvolusiamma.com`.

### Also proven in batch 9
- **Aggregator boilerplate is fabricated.** The sentence *"passionate about Brazilian Jiu-Jitsu…
  strong fundamentals, technical precision, and a supportive training culture"* appeared
  **word-for-word for two unrelated schools**, both from MatMade. They invent *attributes*, from a
  template — not just schools. Any BJJ claim traceable to a directory template is worthless.
- **BJJ in the meta description only.** Two schools carried "Brazilian Jiu-Jitsu" in `<meta>` while
  their class grids contained no grappling at all. The discipline-side twin of "title tags lie".
- **Stored links are essentially all dead** — 11/11, 8/8, 7/7, 11/11 NXDOMAIN across the batch-9
  sub-batches. The historic blanking decisions were correct.
- **Rebrands are recoveries, not losses.** Five schools kept address, phone and head instructor
  while changing name. Confirm by matching address/phone/instructor, never by assumption.

---

## ⚠️ COVERAGE — what is actually audited

All 61 regions have been *touched*. By **records**:

| tier | regions | records | share | what was done |
|---|---|---|---|---|
| **A — fully rebuilt** | 26 | 835 | **16%** | batches 3–7: originals screened AND new research |
| **B — additive only** | 7 | 267 | **5%** | batches 1–2: **originals never screened** |
| **C — never region-rebuilt** | 28 | 4,117 | **79%** | corpus-wide mechanical screens only |

Tier B: **ME AR ON UT SK ND WY**
Tier C: CA 460 · TX 351 · FL 328 · NJ 210 · NY 182 · AZ 173 · CO 156 · GA 152 · PA 148 · MA 140 ·
OH 137 · VA 137 · IL 130 · NC 125 · WA 121 · NV 118 · OR 118 · MI 115 · LA 100 · MO 98 · OK 98 ·
MD 94 · CT 85 · WI 85 · IN 80 · AL 78 · KY 65 · MT 33

Tier C has had the 5 Aug domain-collision audit, the 6 Aug link/DNS audit, and import-time
curation; NY and OR were separately curated end-to-end. **So ~22% of the corpus has had a
school-by-school body-read audit and ~73% has had mechanical screening only.**

**Do not assume that 73% is clean.** Every time originals have been screened the defect rate was
high and rising with region size — 29% → 33% → 34% → 46% → **84%** across batches 3–6b, and
Delaware's stored records came in at **7 of 7 defective**. Batch 6's conclusion, "the larger and
less-curated the region, the worse," points straight at tier C, which is both the largest and the
least curated. RULES §2's four blind spots are all invisible to every screen tier C has had.

**Scale:** batches 3–7 audited 835 records across five sessions (~165/session). Tier C is 4,117
records ≈ **25 sessions**, and likely worse — CA + TX + FL alone are 1,139.

---

## BACKLOG, ordered

**1. Continue the repointing pass — highest value, method now proven and tooled.**
802 published records render no link. Batch 9 measured **one recovery per 2.8 attempts**, so
roughly **275 more links are recoverable**. Override-only, so no corpus risk and no count change.
- Worklist: `scratch/repoint-targets-LL.tsv` (regenerate after each batch).
- Remaining pool by region: CA 75 · TX 75 · FL 55 · NJ 43 · OK 35 · CO 34 · LA 33 · GA 32 ·
  IL 30 · NV 28 · OH 28 · PA 27 · WA 26 · MO 25 · MA 22. 15 regions have zero blanks.
- **Reuse `build_b9.py`** — it gates C3/C5/C9/C9b/C11 and predicts bytes. Copy the agent prompt
  shape from batch 9; six agents at ~15 targets each worked well.
- ⚠️ `tjjm-gym-websites-2` has only ~3.6 KB left. **Put new entries in file 3.** When file 3
  approaches ~20 KB, create `tjjm-gym-websites-4` and add it to the section's render chain.

**2. The 18 browser-only carryovers from batch 9.** They resolve but return empty JS bodies, or
bottom out at Facebook/Instagram, which `web_fetch` cannot render at all. Listed in
`region-rebuild-batch9-findings.md`. Best bets: `Gracie Jiu-Jitsu Ocoee` (exact-name domain
resolves, JS-only) and `Gainesville BJJ Florida`. Includes **`Labrador City BJJ`** (was backlog 7).

**3. Tier B re-screen — the cheapest genuine audit left.** ME AR ON UT SK ND WY, 267 records,
~2 sessions, and known-defective by construction. Edits the corpus, so it needs the full collision
gate; anything needing a change to `n`, `c` or `s` inside the legacy blob must be
suppress-plus-add.

**4. City/state gazetteer scan — now has a real seed set.** Batch 9 found seven records pointing at
the right school in the wrong city, including **`GB Palm Coast` filed under Orlando** (~90 mi).
Seed with those seven plus `Precision MMA` and confirm it fires; two earlier heuristics both
missed the one known case.

**5. Duplicate-record leads from batch 9.**
- `theacademyofmma.com` backs both `West Volusia Academy Of MMA` (DeLand) and `Orange City Academy
  Of MMA` — Orange City is the likely stale duplicate.
- `usajujitsu.net` backs both `Robson Moura Jiu-Jitsu` (Oxford) and `USA Jiu-Jitsu` (Wildwood);
  Robson Moura's own affiliate list names no Oxford school.
- `BJJ Academy Of Sarasota (wbjja)` shares 6170 N Lockwood Ridge Rd with **Six Blades Jiu Jitsu**.
- `Gracie Jiu-Jitsu North Miami Beach` — that address is **Valente Brothers**.

**6. Cross-region debts.** WA, ON, MD, OH, NY, VA, ND, WI, ME, MA, MO, NC, GA, TX, TN, IA, plus
batch 7's: Ontario (Kaze BJJ Scarborough), Oklahoma (Tribal Jiu-Jitsu Ardmore), Maryland (WDC BJJ
Takoma Park), Virginia (Capital MMA's five locations, Ashburn Jiu Jitsu). **Alabama's
`Athens Jiu Jitsu` is now FIXED** — it renders `ajjathens.com`.

**7. Second harvests** — Montreal (~20–25 aggregator-only candidates), Ontario, Nova Scotia.

**8. Tier C audit.** Scope as a programme, not a session. ~25 sessions.

**9. The 15 latent duplicate names** — safe today, would collide if a future batch un-suppressed
the second copy. `build_b8.py`'s C10 is the standing check. Full list in the post-batch-8 audit.

**10. Held, needing a human call.**
- `Renato Tavares Assoc HQ` (Vero Beach) — only confirming page is a WordPress blog last posted
  **Feb 2011**. Publish a 15-year-stale link or leave blank?
- `Master Lowell's MMA` (Melbourne) — same shape, blog last posted Aug 2011.
- `Refit Academy - Coral Gables` — operator has a live site, but only for the former Wynwood site.

**11. The two blocked legacy-blob fixes** — Vermont BJJ's city, Precision MMA's state.

**12. Rebuild `tjjm-gyms.json`** — expired, ~1,200+ records behind. Nothing is known to consume it.

---

## TRAPS — running tally

Everything in brief 6's trap list still holds. Additions from batches 8–9:

**⚠️ Caches and search indexes resurrect dead domains.** See the DNS section above. This is the
most dangerous trap found to date because the false evidence is *detailed and plausible*.

**⚠️ Aggregators invent attributes, not just schools** — identical fabricated BJJ boilerplate for
two unrelated businesses.

**Wrong province/country/state records: 28+.** Every one returns 200. Four of batch 7's were
domain repurposing; batch 9 found two more.

**Delaware returned a 100% defect rate** — 7 of 7 stored records wrong.

**⚠️ AGENTS FABRICATE.** A batch-6 researcher recorded a black-belt lineage appearing nowhere on
the school's site. `METHOD-RULES-agent.md` forbids this explicitly — make sure every agent reads
it. **Reward honest self-flagging**: batch 9's agents left `source_url` empty rather than cite a
page they had not fetched, and that is exactly right.

**The `city` field is unreliable** — seven measured cases in batch 9 alone.

**DNS-first is the only sound screen.** `Status 3` is conclusive; a blank body is UNRESOLVED, not
evidence. **And a rendered body is not evidence either.**

---

## OPERATIONAL NOTES

- `themePublish` **blocked**; `themeFilesUpsert` **blocked on MAIN**. Duplicate first;
  `themeDuplicate` returns **`newTheme`**. Wait ~30 s.
- **Verify writes by MD5** (`checksumMd5`) **yourself** — do not trust a write agent's report.
  One file per agent works well. Batch 9: two files, two exact MD5s, first attempt.
- **An override-only batch cannot move record counts**, and you can prove it by checksumming every
  count-bearing file against the previous theme — stronger than a count sweep and not subject to
  the sweep's own failure modes. Use this whenever no data file, removed-index or section changed.
- **The 113 KB legacy blob cannot be rewritten through this toolchain.** Fixes needing a change to
  `n`, `c` or `s` inside it are blocked; overrides fix `w` and backfill a blank `a` only.
  **Workaround:** suppress and re-add a corrected copy under a different name.
- **Sandbox has no outbound network**; `mcp__workspace__bash` cannot fetch. Use `web_fetch` or the
  browser. **Deletes in the mounted folder are not permitted** — overwrite instead.
- **`web_fetch` dedupes within a session** — bust it with a `?v=1` / `&cb=` parameter, or you will
  silently reuse an earlier agent's fetch. It **cannot render Facebook or Instagram at all**.
- Sweeps: browser, sequential, `credentials:'include'`, explicit `preview_theme_id` on **both**
  sides, cache-buster, control first. `credentials:'omit'` renders the **live** theme — which is
  the right tool for verifying what is published.
  ⚠️ Do not regex the whole HTML for `(\d+) BJJ gyms and academies` — that matches the stale meta
  description in `<head>`. Use JSON-LD `numberOfItems` or the `tjjm-p` body paragraph.
- JS REPL times out at **45 s**; `javascript_tool` truncates at ~1–1.3 KB — write into the page and
  read back with `get_page_text`.
- **The output filter blanks a whole tool result if you echo raw HTML containing URLs.**

---

## FILES

| file | what it is |
|---|---|
| `RULES-tjjm.md` | durable rules + evidence. Read first, with the scoping and DNS corrections. |
| `NEXT-RUN-brief-regions-7.md` | this file |
| `POST-BATCH-8-audit-2026-08-13.md` | **coverage analysis, raw-corpus build, gate results** |
| `region-rebuild-batch9-findings.md` | **the repointing pass, the DNS/cache trap, city defects** |
| `METHOD-RULES-agent.md` | agent-facing brief with the never-fabricate clause. ⚠️ Still contains batch-3-specific inserts — strip or override them. |
| `METHOD-RULES-batch7-addendum.md` | batch-7 trap list. Good template for a per-batch addendum. |
| `region-rebuild-batch3..7-findings.md` | per-batch findings |
| `scratch/raw-corpus-LL.json` | **5,911 records, raw stored `{n,c,s,w,a,src}`, NO overrides applied** |
| `scratch/raw-corpus-LL.tsv` | same, flat, + override / effective / link-state columns |
| `scratch/repoint-targets-LL.tsv` | the blank-rendering worklist (regenerate after each batch) |
| `scratch/raw-datafiles/` | all 45 data files, MD5-verified vs the theme |
| `scratch/ll-datafile-manifest.tsv` | filename → checksumMd5 → size |
| `scratch/repoint-work/verdicts-ALL.tsv` | batch-9's 88 verdicts, strict TSV. **Use this format from Phase 1.** |
| `scratch/repoint-work/recheck.tsv` | the independent falsification pass over batch 9's 32 confirms |
| `batches/url-overrides-b9.tsv` | the 31 published overrides, with caveats |
| `batches/metafields-b8-rollback.md` | SEO metafield rollback strings |
| `gate_b7.py` | the nine-condition gate for **record adds**, `--seed` and `--dump` |
| `build_b9.py` | **override-only gate + build. Reuse this for repointing batches.** |
| `build_b8.py` | disambiguation gate+build. C10 "no live duplicate names" — standing check. |
| `build-b9/` … `build-b3/` | exact files written to each theme |
