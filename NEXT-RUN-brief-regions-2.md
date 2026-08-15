# Session brief — REGION REBUILDS, batch 4 onward. Start here.

Written 10 Aug 2026. Supersedes `NEXT-RUN-brief-regions.md` for the state of the work. That file's
traps and method warnings still hold except where **corrected below** — read this file's
corrections section before trusting it.

Paste the block below into a **new** chat with the `TJJM Projects` folder connected.

---

## The block to paste

> Continuing the TJJM BJJ directory. Read `NEXT-RUN-brief-regions-2.md` first, then `RULES-tjjm.md`,
> then `region-rebuild-batch3-findings.md`. RULES is canonical where they overlap **except** for the
> removed-index scoping correction, where the batch-3 findings are newer and proven.
>
> **Everything through region-rebuild batch 3 is DONE AND PUBLISHED.** Live theme is
> `Aug 9 BJJ Gyms FF` (`154774995116`), 4,825 records across 61 regions. Do not redo it.
>
> The work now is **region rebuilds for the 22 remaining never-curated regions**, in batches of
> 3–5. The method is proven three times; follow the RECIPE section exactly.
>
> Before anything: re-verify the live theme id and record count, and re-derive any buildId rather
> than trusting a written one.

---

## STATE — verified live 10 Aug 2026

**MAIN = `Aug 9 BJJ Gyms FF` (`gid://shopify/OnlineStoreTheme/154774995116`).**

| | count |
|---|---|
| corpus | **4,825** rendered / 61 regions |
| stored records | **5,302** (4,825 rendered + 477 region-scoped suppressions) |
| Iowa | 36 (was 15) · Kansas | 37 (was 13) |
| Manitoba | 21 (was 11) · South Dakota | 11 (was 9) |

Next data file is **`tjjm-gyms-data-40`**. Next theme letter is **GG**.

### File headroom — check before planning a batch
- `sections/tjjm-state-directory.liquid` — **12,657** B of ~24,576. Each new data file costs +34 B.
- `snippets/tjjm-gym-websites-2.liquid` — **20,046** B of ~24,576. **~4.5 KB left.** A batch with
  more than ~90 URL overrides needs a `tjjm-gym-websites-3` and a matching render tag in the
  section's `web_overrides` capture. Batch 3 needed only 2 overrides, so file 3 was **not** created —
  the previous brief's claim that "the next batch needs a file 3" was premature.
- `snippets/tjjm-removed-index.liquid` — 10,106 B. Now has 38 region rows.

### Theme stack
- **KEEP** MAIN `154774995116` (FF).
- **Rollback points:** `154717487276` (EE), `154712932524` (DD), `154697138348` (CC).
- **Disposable:** `154695565484` (BB), `154694877356` (AA), `154665025708` (ZZ),
  `154658242732` (YY), `154653950124` (XX), `154658209964`, `154661355692`.
- `154657063084` is the audit-dump harness. Keep. **Not** a valid "before" theme.

---

## ⚠️ CORRECTIONS to the previous brief — read before using it

**1. `tjjm-removed-index` suppression is REGION-SCOPED, not corpus-wide.**
The old brief and RULES both say all three name-keyed mechanisms match "on NAME ALONE, corpus-wide."
True for `tjjm-gym-websites` and `tjjm-gym-addresses`. **False for the removed-index.** The section
matches `rc == scan_code`, assigns that one row, and breaks — so a suppression only ever applies
inside its own region. Proved by reading the section and by arithmetic:
`5,202 − 434 region-scoped matches = 4,768`, the then-published total. The corpus-wide reading gives
436 and does not reconcile.

Consequence for the collision gate: **condition 4 is "every suppressed name appears exactly once in
its OWN region"**, not corpus-wide. Under the wrong reading, `IL|Aurora BJJ` and
`WA|Northwest Fighting Arts` look like live defects. They are not.

**2. The region counts in the old brief were internally inconsistent** — the header said 24 remaining
regions, the backlog said 28, and the batch table listed 25. The real figure now is **22** (below).

**3. The old batch table was numbered one behind the narrative** — its "batch 1: SK, ND, WY, UT" was
actually batch 2. Batches are renumbered correctly below.

**4. West Virginia was missing from the batch table entirely** despite being never-curated with 10
records and 5 city stubs. It is included below.

---

## THE RECIPE — proven three times, follow it

Three phases per batch. Roughly two hours. Each batch is independently shippable.

### Phase 0 — corpus dump (do this first, in parallel with Phase 1)
The collision gate needs every stored name, including suppressed ones. Rendered pages are not
enough. Split `snippets/tjjm-gyms-data*.liquid` (~600 KB, 39 files) across 4 subagents; each reads
its files via the Shopify connector and writes `name<TAB>city<TAB>state<TAB>sourcefile` to disk,
returning **counts only**. Do not let the names into the main context.

Then assert `stored − region-scoped suppressions == the published total`. If that identity does not
hold exactly, your dump is incomplete — stop and fix it before building anything.

### Phase 1 — research (one agent per region, ~6 min each)
Point each agent at `METHOD-RULES-agent.md` (already written, reusable). Give it the region's stub
list and have it **fetch the live page itself**. Ask for the full roster marked ALREADY-IN or
NET-NEW, plus a verdict on each suspect. Prioritise breadth of cities over depth in the largest metro.

### Phase 2 — verification (one agent per ~22 candidates, ~8 min each)
**Do not skip this.** Batch 3 ran a **29% defect rate** on research output — 31 corrections and 9
unverifiable out of 108 — worse than Ontario's ~20%. One sub-batch hit 48%. Have each agent open
every candidate and read the **body** for name, city, state, address, whether it is actually BJJ,
and whether it is still open.

### Phase 3 — build
1. Assemble `{n,c,s,w,a}`, key order exactly that, sorted by `(s,c,n)`. `w`/`a` omitted when empty.
2. **Run the collision gate, and seed it first** (below).
3. Generate `tjjm-gyms-data-<N>.liquid` — compact JSON, `[` on line 1, one record per line,
   `]` last, trailing newline.
4. Suppressions → one new row per region in `tjjm-removed-index`, format `CODE|Name|Name|...`.
5. URL blanking/fixes → `tjjm-gym-websites-2` if it fits, else create file 3 + render tag.
6. Section: add `{%- render 'tjjm-gyms-data-<N>' -%}` to the `gym_json` capture. +34 bytes.
7. Region index: update each changed count **and** the total in the header comment.
8. **Predict every byte size before writing.** Every write across three sessions has hit exactly.
9. Duplicate MAIN → write there (writes are blocked on MAIN). Wait ~30 s. `themeDuplicate` returns
   **`newTheme`**, not `theme`.
10. Verify by sweep (below), then hand to the user to publish. `themePublish` is blocked.
11. **After they publish, `metafieldsSet` the changed regions' `title_tag` and `description_tag`.**
    They are global, not theme-scoped, so setting them early opens an inconsistency window in the
    other direction. Only change the number; check the city lists still name listed cities.
12. Re-verify live and **cookie-free**: `fetch(url, {credentials:'omit'})` bypasses any preview
    cookie and renders the live theme. Assert title = description = JSON-LD = cards = body.

---

## THE COLLISION GATE — and the seed test that makes it trustworthy

`tjjm-gym-websites` and `tjjm-gym-addresses` match on **name alone, corpus-wide**. A shared name
silently applies one record's correction — or its *blank* — to another.

Assert, before writing:
1. no new name equals any existing corpus name
2. no new name equals another new name
3. no new name equals a name in either overrides file
4. every name being suppressed appears exactly once **in its own region**
5. no name anywhere contains `|` or `~`

**Always seed the gate with known-bad input and confirm it fires on all five conditions before
believing a clean result.** The gate once reported "no collisions" on a set that had two, because
a `slice(2)` prefix-strip left a stray character on every corpus name so nothing could ever match.

### Three instances of the same defect class so far
- `Jungle Gym Martial Arts` — New Rochelle vs a real Bronx school. → `... - Bronx`
- `Action & Reaction MMA` — new Pickering ON school vs a Laval QC record carrying a **blank**
  override; the new school would have rendered with no link. → `Action & Reaction MMA Pickering`
- `Ethos BJJ` — new Wichita KS school vs a Wilmington NC record carrying a **blank** override.
  Same silent-blanking failure. → `Ethos BJJ Wichita`

Batch 3 caught five collisions in 100 records. Assume roughly one per 20 new records.

---

## TRAPS — updated counts

**Wrong-country / wrong-state records: seven instances, two of them already live in the corpus.**
`Red River BJJ` filed under Manitoba is in **Wichita Falls, Texas**. `Huron BJJ` filed under South
Dakota is in **Goderich, Ontario**. Plus the five Ontario/UK/NZ cases. Check the state or country on
every candidate via a street address, ZIP/postal code, or area code — never via the school's name.

**A `<City> BJJ` name does not mean the record is fake — now failed as a verdict many times over.**
In batch 3, 24 of 27 stubs were NXDOMAIN, but **15 of them were real schools trading under a
different name.** Only 9 were genuinely gone. Blanking on the domain alone would have been wrong 15 times.

**A working link is not evidence.** Two of the three Kansas records whose links resolved were bad
anyway: `kansasbjj.com` is a GoDaddy for-sale page, `midwesttrainingcenter.com` a Squarespace
placeholder. Also seen: a NamesPro.ca registrar placeholder, and a parked Above.com/Trellian domain
returning 200. **Every one of these passes a reachability screen.**

**DNS-first is still the screen that works.** `https://dns.google/resolve?name=<host>&type=A`;
`"Status": 3` is NXDOMAIN and conclusive. A blank body is not — record it as UNRESOLVED. Note
Status 2 (REFUSED) also occurs and is likewise not evidence.

**Rural regions often run on one network.** Five of eight Manitoba stubs resolved to WAMMA
affiliates. Find the network before sweeping city by city.

**Whole-page byte comparison between two themes can never pass** — assets are served per-theme from
`/cdn/shop/t/<n>/`. Scope to `data-tjjm-statedir` → `</section>` and excise the region-nav block when
`tjjm-region-index` changed. Scoped correctly, batch 3 got **57 of 57** non-target regions identical.

---

## OPERATIONAL NOTES

- `themePublish` **blocked** — the user publishes. `themeFilesUpsert` **blocked on MAIN**.
- `themeDuplicate` returns **`newTheme`**. Wait ~30 s before files are readable.
- **Sandbox has no outbound network.** Use `web_fetch` or the browser.
- **`web_fetch` truncates at ~75 KB and keeps no cookie jar**, so it cannot preview a theme at all —
  `preview_theme_id` sets a cookie and redirects to the clean URL, so an unparameterised fetch
  renders the live theme. Sweeps must run in the browser.
- Sweeps: sequential (concurrency 1), `credentials:'include'`, explicit `preview_theme_id` on
  **both** sides, unique cache-buster per fetch. **Run a control first** — confirm one known region
  actually changes under preview before believing any result.
- `credentials:'omit'` deliberately renders the **live** theme. Useful for the final cookie-free check.
- The JS REPL takes top-level `await`. Keep returns under ~1 KB. It **times out at 45 s**, so chunk
  a 61-region sweep into groups of ~16 and accumulate in `sessionStorage` (`window.*` dies on reload).
- The output filter blocks query-string/token-like data. Strip `?...` from any URL you echo.
- **Re-query file sizes after any failed agent** before assuming a write did or did not land.

---

## BACKLOG, ordered

**1. The 22 remaining never-curated regions.** Every rebuilt region has come in at roughly **2x**
its listed count — batch 3 averaged 2.2x. Plausibly **350–600 more schools** left.

~~batch 1: ME, AR, ON~~ · ~~batch 2: UT, SK, ND, WY~~ · ~~batch 3: IA, KS, MB, SD~~ **all published**

| batch | regions | listed | stubs |
|---|---|---|---|
| 4 | NM, HI, ID, VT, RI | 56 | 22 |
| 5 | MN, SC, MS, NE, NH | 68 | 28 |
| 6 | WV, BC, AB, QC | 79 | 34 |
| 7 | TN, NS, NB, NL, PE, DE, DC, AK | 151 | 14 |

**2. The 9 records held back in batch 3** and the 7 other owed items — see
`region-rebuild-batch3-findings.md`, "Owed from this batch".

**3. Ontario second harvest.** Toronto reportedly has 100+ academies; only ~8 net-new surfaced.
Never swept: Milton, Newmarket, Aurora, Brantford, Woodstock, Stratford, Chatham-Kent, Timmins,
Cornwall, Brockville, Owen Sound, Kenora, Orangeville, Bradford.

**4. Re-screen the original records in every rebuilt region**, not just the stubs — see the
"working link" trap. Batch 3 did this for its four regions and it paid off; ME, AR, ON, UT, SK, ND,
WY have not had it.

**5. The 63 unresolved `EMPTY` links** (55 curated + 8 Ontario). One body read each.

**6. Repointing pass** over the 544 blanked links. `Four-Eleven Brazilian Jiu Jitsu` was blanked as
dead but is live at fourelevenbjj.ca. Batch 3 found 15 more of this shape in 27 stubs, so the
fraction is probably high.

**7. Newly found, not yet actioned** (all from batch 3):
   - `NJ|JC Projects` is a **dead suppression entry** matching nothing anywhere.
   - `Precision MMA` is stored as `c:"Poughkeepsie", s:"NJ"` — Poughkeepsie is in **New York**.
     First confirmed instance of the name/city-contradicting-state class RULES lists as unscanned.
   - `tjjm-gyms-data-30, -31, -32, -34` are **not valid JSON** — no enclosing `[ ]`, no newlines,
     bare concatenated `}{`. They render fine but break any strict `JSON.parse`.
   - **Missouri may owe up to 9 records** — the KS research found and correctly excluded nine Kansas
     City MO schools. MO is curated at 98; diff them.

**8. Rebuild `tjjm-gyms.json`.** The staged upload expired and must be rebuilt from scratch; it is
now ~760 records behind. See `STEP-11-BLOCKED-recovery.md`. **Lowest priority: nothing is known to
consume this file.**

**9. Carried from the NY run, untouched:** backlog item 0c, six owed `tjjm-statedir-notes-<code>`
files (FL, LA, MO, NJ, TX, NV), item 2b (UFC GYM Sherwood), item 1b-follow-up (Alliance San Diego).

**10. Never-imported duplicates (RULES §2 blind spot 1)** — still untouched, still unreachable by
any diff run so far.

---

## WHAT WAS NOT CHECKED

- **No corpus-wide cross-region diff has ever been completed.** Still unknown whether any imported
  record already exists under another region. Specifically unresolved: whether **Savarese BJJ**
  (suppressed from NY as being in Lyndhurst NJ) already exists under NJ.
  *Note: this is now cheap.* The Phase 0 corpus dump produces exactly the artifact needed — a
  complete `name/city/state` table. Run the diff on it next session.
- The 96 curated-state links the screen flagged that are live and correct were left alone —
  correctly. Not a to-do.
- Ontario's `Hamilton BJJ` vs `Hamilton Brazilian Jiu-Jitsu`: probably one school on two domains,
  unconfirmed. Hamilton BJJ is actually in **Stoney Creek**.
- Batch 1/2 holdbacks: 3 Maine records, 6 Arkansas records. Still owed.

---

## FILES IN THIS FOLDER

| file | what it is |
|---|---|
| `RULES-tjjm.md` | durable decision rules + evidence. **Read first**, with the correction above. |
| `NEXT-RUN-brief-regions-2.md` | this file |
| `METHOD-RULES-agent.md` | **the agent-facing brief. Reusable as-is for Phase 1 and 2.** |
| `region-rebuild-batch3-findings.md` | IA/KS/MB/SD — the 29% defect rate, the Ethos collision, the scoping correction |
| `region-rebuild-batch2-findings.md` | UT/SK/ND/WY |
| `region-rebuild-batch1-findings.md` | ME/AR/ON, the 2x ratio finding |
| `ny-step5-verdicts.md` | the NY import, full evidence base |
| `STEP-11-BLOCKED-recovery.md` | Files JSON rebuild procedure |
| `scratch/corpus-names-G1..G4.tsv` | **the 5,202-name corpus dump as of theme EE.** Regenerate for FF. |
| `scratch/live-*.liquid` | verbatim copies of the theme files as of EE |
| `build-b3/` | the exact five files written to FF |
| `batches/research-{IA,KS,MB,SD}.tsv` | batch 3 Phase 1 output |
| `batches/verdict-b3-0{1..5}.tsv` | batch 3 Phase 2 verdicts, with evidence and source URLs |
| `batches/B-stubs-ALL.tsv` | the 174 city-stub records; 27 now cleared, 147 remain |
| `HANDOFF-next-states.md` | older handoff; backlog items 0c–17 still live there |
