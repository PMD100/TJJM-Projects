# Session brief — POST-BATCH-7. Start here.

Written 13 Aug 2026. Supersedes `NEXT-RUN-brief-regions-5.md`.

**All 61 regions have now been curated at least once.** The region-rebuild programme is
finished. What remains is debt: held-back records, cross-region debts, second harvests and
the repointing pass.

Paste the block below into a **new** chat with the `TJJM Projects` folder connected.

---

## The block to paste

> Continuing the TJJM BJJ directory. Read `NEXT-RUN-brief-regions-6.md` first, then
> `RULES-tjjm.md`, then `region-rebuild-batch7-findings.md`. RULES is canonical where they
> overlap **except** for the removed-index scoping correction and the NE/NL split, where the
> batch-3-to-7 findings are newer and proven.
>
> **Everything through region-rebuild batch 7 is DONE.** All 61 regions are curated.
> Before anything: **confirm the Shopify connector is on thejiujitsumindset.com** (it has
> silently switched stores once), then re-verify the live theme id and record count against
> the STATE table below.
>
> ⚠️ **Check what has actually been published.** Two themes were staged and handed over, and
> `themePublish` is blocked so both may still be sitting unpublished.
> **`LL` (`154883129516`) is the tip and is the one to publish** — it contains batch 7 AND the
> duplicate-name disambiguation. Publishing LL alone is sufficient; KK then becomes a rollback.
> If nothing was published, the live corpus is still 5,205 and `metafieldsSet` has not been run.

---

## STATE

**Two unpublished themes are stacked. LL is the tip.**

| theme | id | contains | rendered |
|---|---|---|---|
| **LL** | `154883129516` | batch 7 **+ duplicate-name disambiguation** | **5,219** |
| KK | `154881523884` | batch 7 only | 5,219 |
| JJ | `154865860780` | pre-batch-7, currently MAIN unless published | 5,205 |

**After publishing LL:** 5,219 rendered / 61 regions, **5,911** stored, **692** suppressed
records (from **690** suppression *names* — see the C4 note below, these now differ).

`build-b7/` and `build-b8/` hold the exact files written, all MD5-verified against their themes.

Next data file is **`tjjm-gyms-data-46`**. Next theme letter is **MM**.

### Post-batch-7 region counts
TN 52 · NS 29 · AK 14 · NB 15 · NL 13 · PE 10 · DE 8 · DC 6 · **NE 21 (unchanged)**

### File headroom (as of LL)
- `sections/tjjm-state-directory.liquid` — **12,906** B of ~24,576. Each data file costs +34 B.
- `snippets/tjjm-gym-websites-2.liquid` — **20,524** B. **~4.0 KB left — treat as full.**
- `snippets/tjjm-gym-websites-3.liquid` — **826** B. New in batch 7. Put new overrides here.
- `snippets/tjjm-gym-addresses.liquid` — 8,455 B. Plenty.
- `snippets/tjjm-removed-index.liquid` — 13,749 B, **59** region rows.

### Theme stack
- **KEEP** LL `154883129516` (tip — batch 7 + disambiguation).
- **Rollback:** KK `154881523884`, JJ `154865860780`, II `154862780588`, HH `154860028076`.
- ⚠️ GG `154856816812`, FF `154774995116` and the audit-dump harness `154657063084`
  **no longer exist** — brief 5 still listed them.

---

## AFTER PUBLISHING LL — do this

1. `metafieldsSet` for the eight batch-7 regions. **Check the city lists, not just the
   numbers** — five cities dropped to zero records in batch 5 while still named in
   descriptions. Batch 7 changes city membership heavily: Alaska lost cities, Tennessee
   gained many, NS gained Windsor and Chéticamp, NL gained Flat Bay and lost Gander.
2. Re-verify live cookie-free with `fetch(url,{credentials:'omit'})`.
3. Confirm title = description = JSON-LD `numberOfItems` = card count = body count.

---

## THE COLLISION GATE — now NINE conditions

`gate_b7.py` in the project root implements all of them, is reusable, and takes `--seed`.
**Run `--seed` first every time and confirm every sub-condition fires independently.**

`tjjm-gym-websites*` and `tjjm-gym-addresses` match **on name alone, corpus-wide**.
`tjjm-removed-index` matches **on name within its own region row only**.

1. no new name equals any existing corpus name
2. no new name equals another new name
3. no new name equals a name in any overrides file — **now three files, not two**
4. every suppressed name matches **at least one** record in its own region — and any name
   matching **more than one** must be a declared, deliberate multi-match (see below)
5. no name anywhere contains `|` or `~`
6. no name is both SUPPRESSED and ADDED in the same region
7. **the Nebraska/Newfoundland rule — a, b and c**
8. **city-spelling fold check**
9. **no override may restate the stored value** — new in batch 7, see below

⚠️ **Report every sub-condition separately.** Batch 7's seeded run claimed "all fired" while
C7b and C7c were silently not being exercised, because the summary grouped C7a/b/c together.

### C7 — Newfoundland is stored under Nebraska's code
- **C7a** — no new Nebraska record may use a city in `nl_cities`.
- **C7b** — the suppression check runs *before* the city split, so **the `NE` removed-index row
  applies to both pages**. There is no NL row and there cannot be one. Suppressing an NL record
  means adding a name to the NE row.
- **C7c** — **an NL record in a city outside the hardcoded `nl_cities` list renders on the
  NEBRASKA page.** Silently. This fired for real in batch 7 (Golden Rule Jiu Jitsu, Flat Bay).
- `nl_cities` now has **eleven** entries: St. John's · Corner Brook · Gander · Paradise ·
  Conception Bay South · Labrador City · Grand Falls-Windsor · Clarenville · Mount Pearl ·
  Torbay · **Flat Bay**. Adding a twelfth requires editing the section AND `gate_b7.py`.
  Still blocked: Stephenville, Happy Valley-Goose Bay, Carbonear, Bay Roberts, Marystown,
  Placentia, Deer Lake, Bonavista, Channel-Port aux Basques, Springdale.
- **Assert Nebraska's count is 21 before and after any NL work.**

### ⚠️ C4 changed — suppressed NAMES and suppressed RECORDS now differ
Until the disambiguation session, every suppressed name matched exactly one record, so
`stored − suppression_names == published` held. It no longer does. Two entries deliberately
match two records each:

- `MD | Southern Maryland Martial Arts & Fitness` → kills 2 records
- `VA | Capital MMA & Elite Fitness` → kills 2 records

This is intended. **A same-region duplicate name cannot be half-renamed** — suppression matches
by name within a region, so one entry kills both copies and both must be re-added under new
names. **The true invariant is `stored − suppressed RECORDS == published`.** Counting names
now gives 690 where the record count is 692. Assert on records.

### C9 — never restate a stored value in an override
Building overrides from a verdict file's `url` column produced four no-op overrides in batch 7,
because agents disagreed about whether that column held the stored or the corrected URL.
**Read the stored `w` out of the legacy blob (`scratch/raw-G1-legacy.txt`) and assert
`new_w != stored_w`.** See `batches/url-overrides-b7.tsv` for the format that works.

### The silent-blank-override class — now SEVEN
`Jungle Gym Martial Arts` · `Action & Reaction MMA` · `Ethos BJJ` · `Alliance Jiu Jitsu Easley` ·
`Ironside Martial Arts` · **`Athens Jiu Jitsu`** · `Victory Jiu Jitsu Dieppe` (fixed in b7).
Plus one deliberate new blank: **`Kaze BJJ and Judo Institute`** — its domain serves an
unrelated Ontario business. When fixing an existing record's URL, **edit its existing override
entry rather than appending a duplicate**.

---

## METHOD CHANGES PROVEN IN BATCH 7 — adopt these

**1. Mandate a strict TSV from Phase 1, not just verification.**
Columns `verdict region name city url action evidence source_url`, `verdict` FIRST, closed
vocabulary. Batch 7's research files used three different table layouts and one invented
keyword, and a position-based parser silently returned zero verdicts for all 34 Tennessee
records — the same failure batch 5 had. All eight verification TSVs parsed first time.

**2. Add a browser-render pass as a standing phase.**
`web_fetch` **cannot render Facebook or Instagram at all**, and small-town clubs mostly have
no website. This is not an edge case: it blocked ~20 records in batch 7 and would have made
Nova Scotia shrink. A Claude in Chrome pass resolved 24 of 30 targets and produced **17
records**. Also note three dead domains all served the identical GoDaddy parked template,
which is indistinguishable from a JS-rendered page through plain fetch.

**3. Check whether your second source cites your first.**
Nova Scotia's 13 leads rested on two directories "corroborating" each other. One explicitly
credits the other in its own text.

**4. A military-base club is not a directory listing unless civilians can train there.**
Three instances in batch 7 (JBER, CFB Shearwater, CFB Halifax).

**5. Expect one duplicate-name collision per ~20 net-new records.**
Multi-location brands are the source. Batch 7 had five.

---

## BACKLOG, ordered

**1. Publish LL (`154883129516`) and run the post-publish steps above.** Nothing else should
start first. LL is the tip and contains batch 7 plus the disambiguation — publishing it alone
is sufficient, and KK then becomes a rollback.

**2. ⚠️ PREREQUISITE for the repointing pass: assemble raw stored `w` values.**
Do this before starting item 3, not during it. To repoint a link you need the record's **raw
stored `w`**, and per RULES §3 the rendered page is not it (the section prepends `https://` and
substitutes overrides) and `tjjm-gyms.json` is not it either (it has overrides applied). Only a
raw dump carries true stored values — **and the audit-dump harness theme `154657063084` has been
deleted.**

What exists on disk: `scratch/raw-G1-legacy.txt` (the 113 KB legacy blob, 1,304 records), plus
data files 35–38 and 43–45 in the project root and `build-b*/`. **Missing: `tjjm-gyms-data-2`
through `-34`, and `-39` through `-42`.**

Pull those from the theme with `theme.files(filenames:[...])` and build a complete raw corpus
(`{n,c,s,w,a,src}`) into `scratch/`. It is ~500 KB total, so split it across several agents —
roughly ten files each — rather than one. This also retires backlog item 11 and gives every
later session the dump the deleted harness used to provide.

**3. The repointing / browser-render pass — the highest-value item.**
Batch 7 measured the yield: roughly one record recovered per 1.8 attempts. Targets:
   - the **16 records held back from batch 7** (listed in the batch-7 findings)
   - the **85 held back from batches 3–6** (32 from b6, 29 from b5, 15 from b4, 9 from b3)
   - the **63 unresolved `EMPTY` links** and the **544 blanked links**
   Batch 6 recovered live URLs for 8 of 19 already-blanked records in its own regions. With a
   browser this should do considerably better.

**4. Cross-region debts — now a substantial standalone session.**
Spanning WA, ON, MD, OH, NY, VA, ND, WI, ME, MA, MO, NC, GA, TX, TN, IA, and new from batch 7:
**Ontario** (Kaze BJJ Scarborough), **Oklahoma** (Tribal Jiu-Jitsu Ardmore), **Maryland**
(WDC BJJ Takoma Park), **Virginia** (Capital MMA's five locations, Ashburn Jiu Jitsu),
**Alabama** (`Athens Jiu Jitsu` renders with no link). Each batch's findings file has its list.

**5. Second harvests** — Montreal (~20–25 aggregator-only candidates the QC researcher
declined to launder), Ontario, and now **Nova Scotia** (the b7 browser pass cleared the known
leads but never swept for new ones).

**6. Re-screen the original records in ME, AR, ON, UT, SK, ND, WY** — never done; every batch
that has done it found major defects.

**7. `Labrador City BJJ`** needs a working URL or a deliberate blank — stored domain is
NXDOMAIN, the candidate replacement returns a blank body through every route tried.

**8. ~~Disambiguate the duplicate names~~ — DONE, staged in theme LL.** 14 records renamed via
suppress-plus-add; no live duplicate name remains. Net corpus change zero, all 61 counts
unchanged. See `batches/disambiguation-b8.tsv` and `batches/sweep-b8.md`.
   **Residual:** four names still have two stored copies, but only one renders because the
   other is already suppressed — `Aurora BJJ`, `Midwest Training Center`,
   `Northwest Fighting Arts`, `Red River BJJ`. Safe today; they would collide again if a future
   batch un-suppressed the second copy. `build_b8.py`'s **C10** check ("no live duplicate names
   remain") is worth running as a standing corpus-health check.

**9. The two blocked legacy-blob fixes** — Vermont BJJ's city, Precision MMA's state (already
suppressed, so latent only).

**10. City/state gazetteer scan** — still unrun properly. **Seed it with `Precision MMA` and
confirm it fires**; two heuristics were tried and both missed the one known case.

**11. `tjjm-gyms-data-30, -31, -32, -34` are not valid JSON** — they render fine but break
strict `JSON.parse`. (`-44` was checked and parses cleanly.)

**12. Rebuild `tjjm-gyms.json`** — expired, now ~1,200+ records behind. Nothing is known to
consume it.

---

## TRAPS — running tally

**Wrong province/country/state records: 28+ found so far.** Batch 7 added eight, including
Ontario, Oklahoma, Bali Indonesia, and Maryland. **Every one returns 200.** Four of batch 7's
were **domain repurposing** — the domain outlived the business and now serves someone else.

**Delaware returned a 100% defect rate** — 7 of 7 stored records wrong. The worst region
measured on this project. Small, long-neglected regions are not necessarily clean.

**Aggregators fabricate**, and now: **aggregators cite each other**. MatMade invented a
Manchester NH school and files Rochester **Indiana** under New Hampshire. `westcoastbjj.ca`'s
affiliate list is copyrighted **2014**.

**⚠️ AGENTS FABRICATE TOO.** A batch-6 researcher recorded a black-belt lineage appearing
nowhere on the school's site. `METHOD-RULES-agent.md` has an explicit clause forbidding this —
make sure every agent reads it. **Reward honest self-flagging**: Tennessee's researcher
declared its own coverage gap and the verifier's sweep of the towns it named found 14 more
schools.

**Search summaries are not sources.** WebSearch asserted a Tri-Cities BJJ owner and address
that the business's own page contradicts on both counts.

**Title tags lie about discipline.** Batch 6 rejected 20 on this basis; batch 7 rejected 8 in
Alaska alone. `374 MMA`'s meta keywords say "Windsor Ontario" while its body says Halifax NS.

**Branding can contradict the body within one page.** `johnsoncityjiujitsu.com` shows
"Tri-Cities Premier Jiu Jitsu Academy" branding over body text describing a business in
Ashburn, **Virginia**.

**Wrong-city errors** remain common. Watch mailing-city footers and brand-vs-location
mismatches (a school branded "Omaha" in Papillion, "Rehoboth Beach" in Lewes).

**DNS-first is the only sound screen.** `Status 3` NXDOMAIN is conclusive; Status 2 and blank
bodies are UNRESOLVED, not evidence. A typo hypothesis does not always pay.

---

## OPERATIONAL NOTES

- `themePublish` **blocked**; `themeFilesUpsert` **blocked on MAIN**. Duplicate first;
  `themeDuplicate` returns **`newTheme`**. Wait ~30 s.
- **Verify writes by MD5** (`checksumMd5`) **yourself** — do not trust a write agent's report —
  and **re-query after ANY agent failure**. A 6b write agent died mid-job having landed 4 of 6.
  Splitting the write one file per agent worked well in b7: six files, six exact MD5s.
- **The 113 KB legacy blob cannot be rewritten through this toolchain.** Any fix needing a
  change to `n`, `c` or `s` inside it is blocked; overrides can fix `w` and backfill a blank `a`
  only. **Workaround:** suppress the record and re-add a corrected copy under a different name.
  Used four times in batch 7 (Rip Tide, First State MAA, Alliance TN, B7 Jiu Jitsu).
- **Sandbox has no outbound network**; `mcp__workspace__bash` cannot fetch. Use `web_fetch` or
  the browser. **Deletes in the mounted folder are also not permitted** — overwrite instead.
- **`web_fetch` keeps no cookie jar** so it cannot preview a theme, **dedupes within a session**,
  and **cannot render Facebook or Instagram at all**.
- Sweeps: browser, sequential, `credentials:'include'`, explicit `preview_theme_id` on **both**
  sides, cache-buster, **control first**. `credentials:'omit'` renders the **live** theme.
  A sweep where every region differs, or none does, is reporting a defect not a result.
  ⚠️ Do not regex the whole HTML for `(\d+) BJJ gyms and academies` — that matches the stale
  meta description in `<head>`. Use the JSON-LD `numberOfItems` or the `tjjm-p` body paragraph.
- JS REPL times out at **45 s** — chunk 61 regions into groups of ~16, accumulate in
  `sessionStorage`. `javascript_tool` truncates at ~1–1.3 KB; write into the page and use
  `get_page_text` to read ~11 KB back.
- **The output filter blanks a whole tool result if you echo raw HTML containing URLs.**

---

## FILES

| file | what it is |
|---|---|
| `RULES-tjjm.md` | durable rules + evidence. Read first, with the scoping correction. |
| `NEXT-RUN-brief-regions-6.md` | this file |
| `METHOD-RULES-agent.md` | agent-facing brief with the never-fabricate clause. ⚠️ Still contains batch-3-specific inserts (Iowa Waterloo, Manitoba Brandon, Flin Flon) — strip or override them. |
| `METHOD-RULES-batch7-addendum.md` | the batch-7 trap list. A good template for a per-batch addendum. |
| `region-rebuild-batch7-findings.md` | TN/NS/NB/NL/PE/DE/DC/AK — C7c, the Facebook wall, the 100% Delaware defect rate |
| `region-rebuild-batch6-findings.md` | WV/AB/BC/QC — the 84% defect rate, the fabrication, the half-landed write |
| `region-rebuild-batch5-findings.md` | MN/SC/MS/NE/NH — C7, the Wales/England links, MatMade fabrication |
| `region-rebuild-batch4-findings.md` | NM/HI/ID/VT/RI — C6, the identity pass, the blob limit |
| `region-rebuild-batch3-findings.md` | IA/KS/MB/SD — the region-scoping correction |
| `gate_b7.py` | **the nine-condition gate, reusable, `--seed` and `--dump`** |
| `build_b7.py` | batch-7 build with byte prediction. Reusable pattern. |
| `build_b8.py` | disambiguation gate+build. Adds **C10, "no live duplicate names remain"** — run this as a standing corpus-health check. |
| `batches/disambiguation-b8.tsv` | the 14 renames, with stored w/a preserved and rationale |
| `batches/sweep-b8.md` | LL vs KK: all 61 counts identical, name-level diff on 11 regions |
| `batches/duplicate-names-rendered.tsv` | the raw rendered data behind the disambiguation |
| `batches/url-overrides-b7.tsv` | the audited override format that prevents C9 violations |
| `batches/corrections-b7.tsv` | every gate-driven decision and its rationale |
| `batches/sweep-b7.md` | the 61-region before/after sweep |
| `batches/verdict-b7-*.tsv` | batch-7 verdicts, strict TSV. **Use this format from Phase 1.** |
| `batches/research-b7-*.md` `verify-b7-*.md` | batch-7 research and verification detail |
| `build-b7/` … `build-b3/` | exact files written to each theme |
| `scratch/jj-corpus.json` | 5,841-record corpus as of theme JJ — reconstruct forward from here |
| `batches/B-stubs-ALL.tsv` | 174 city stubs; 123 now cleared, 51 remain |
