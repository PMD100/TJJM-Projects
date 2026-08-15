# Session brief — REGION REBUILDS, batch 5 onward. Start here.

Written 12 Aug 2026. Supersedes `NEXT-RUN-brief-regions-2.md`. That file's traps and method still
hold; this one adds gate condition C6, the store-switch hazard, and the legacy-blob write limit.

Paste the block below into a **new** chat with the `TJJM Projects` folder connected.

---

## The block to paste

> Continuing the TJJM BJJ directory. Read `NEXT-RUN-brief-regions-3.md` first, then `RULES-tjjm.md`,
> then `region-rebuild-batch4-findings.md`. RULES is canonical where they overlap **except** for the
> removed-index scoping correction, where the batch-3/4 findings are newer and proven.
>
> **Everything through region-rebuild batch 4 is DONE AND PUBLISHED.** Live theme is
> `Aug 12 BJJ Gyms GG` (`154856816812`), 4,921 records across 61 regions. Do not redo it.
>
> The work now is **region rebuilds for the 17 remaining never-curated regions**, in batches of 4–5.
> The method is proven four times; follow the RECIPE exactly.
>
> Before anything: **confirm the Shopify connector is on thejiujitsumindset.com** (it has silently
> switched stores once), then re-verify the live theme id and record count, and re-derive any
> buildId rather than trusting a written one.

---

## STATE — verified live 12 Aug 2026

**MAIN = `Aug 12 BJJ Gyms GG` (`gid://shopify/OnlineStoreTheme/154856816812`).**

| | count |
|---|---|
| corpus | **4,921** rendered / 61 regions |
| stored records | **5,444** (4,921 rendered + 523 region-scoped suppressions) |
| NM 34 · HI 38 · ID 45 · VT 12 · RI 23 | (were 12/11/11/11/11) |

Next data file is **`tjjm-gyms-data-41`**. Next theme letter is **HH**.

### File headroom
- `sections/tjjm-state-directory.liquid` — **12,691** B of ~24,576. Each new data file costs +34 B.
- `snippets/tjjm-gym-websites-2.liquid` — **20,139** B of ~24,576. **~4.4 KB left.** A batch needing
  more than ~85 URL overrides requires a `tjjm-gym-websites-3` plus a render tag in the section's
  `web_overrides` capture.
- `snippets/tjjm-gym-addresses.liquid` — 7,843 B. Plenty of room.
- `snippets/tjjm-removed-index.liquid` — 10,853 B, 43 region rows.

### Theme stack
- **KEEP** MAIN `154856816812` (GG).
- **Rollback:** `154774995116` (FF), `154717487276` (EE), `154712932524` (DD).
- **Disposable:** CC `154697138348` and everything older.
- `154657063084` is the audit-dump harness. Keep. **Not** a valid "before" theme.

---

## ⚠️ THREE HAZARDS THAT COST TIME THIS SESSION

**1. The Shopify connector silently switched stores.** Mid-build it was pointed at
**Submission Coffee** (`submission-coffee.myshopify.com`). Querying theme FF returned
"Theme does not exist" and MAIN came back as "Horizon". Nothing was written to the wrong store only
because a read caught it first.
→ **Call `get-shop-info` and confirm `thejiujitsumindset.com` before any write, and put the same
check in every write-agent's prompt.** Reconnecting may land on the wrong store again; you may have
to switch twice.

**2. The sandbox `/tmp` is wiped between sessions.** A fully built batch was lost that way.
→ **Stage every build artifact in the mounted folder** (`build-b<N>/`), never in `/tmp`. Everything
is reconstructible from the surviving TSVs, but only if those are in the folder too.

**3. The 113 KB legacy blob cannot be rewritten through this toolchain.** `themeFilesUpsert` takes
the whole body as a mutation argument — no streaming, no file handle. That is ~65k tokens of
transcription over a dense single-line JSON array of 1,304 records, with no redundancy to catch a
dropped record. The `URL` body type exists but the sandbox has no network egress, so the bytes
cannot be staged where Shopify could fetch them.
→ **Any fix that requires editing a record's `n`, `c` or `s` inside the legacy blob is blocked.**
Overrides can fix `w` and backfill a blank `a`; they cannot change city or state. Landing blob edits
needs Shopify CLI or the Assets REST endpoint from a machine with the file and network access.

---

## THE COLLISION GATE — now SIX conditions

`tjjm-gym-websites` and `tjjm-gym-addresses` match **on name alone, corpus-wide**.
`tjjm-removed-index` matches **on name within its own region row only**.

Assert before writing:

1. no new name equals any existing corpus name
2. no new name equals another new name
3. no new name equals a name in either overrides file
4. every suppressed name appears exactly once **in its own region**
5. no name anywhere contains `|` or `~`
6. **no name is both SUPPRESSED and ADDED in the same region** ← new, batch 4

**C6 is the dangerous one.** Suppression is name-keyed within a region, so suppress-and-re-add makes
the new record render **nothing at all**, silently. Five records hit this in batch 4 — all of them
"existing record corrected by verification", which is exactly the shape that invites it. Convert
those to **in-place override fixes** instead of suppress-and-re-add.

**Always seed the gate with known-bad input and confirm it fires on all six before believing a clean
result.** The gate once reported "no collisions" on a set that had two.

### Four instances of the silent-blank-override class so far
`Jungle Gym Martial Arts` · `Action & Reaction MMA` · `Ethos BJJ` · plus batch 4's five C6 cases.
Budget roughly **one collision per 20 new records**.

---

## THE RECIPE

### Phase 0 — corpus dump
Split `snippets/tjjm-gyms-data*.liquid` across 4 subagents; each writes
`name<TAB>city<TAB>state<TAB>sourcefile` to disk and returns **counts only**. Then assert
`stored − region-scoped suppressions == published total`. If that identity is off by even one, the
dump is incomplete — stop.
*Shortcut:* if the previous batch's dump is still in `scratch/`, reconstruct instead —
`previous dump + previous batch's data file` — and validate with the same identity. Batch 4 did this
in seconds rather than re-dumping 600 KB.

### Phase 1 — research (one agent per region)
Point each at `METHOD-RULES-agent.md` and have it **fetch the live page itself**.

### Phase 2 — verification (one agent per ~22 candidates)
**Never skip.** Batch 3 ran 29% defects; batch 4 ran **33%**, with two sub-batches at 41%.

⚠️ **Watch the shared WebSearch budget.** It capped at 200/200 partway through batch 4's Phase 2 and
directly caused several of the 15 held-back rows. Budget it, or stagger the passes.

### Phase 2b — identity reconciliation ← new, batch 4
Researchers write schools' **corrected** names, not the stored stub names, so the join back to
stored records silently fails. Batch 4 had 8 unmatchable records; publishing blind would have
double-listed schools. A dedicated identity pass resolved them and **refuted three earlier matches**,
one of which had been made from a **meta-description**.
→ **Reconcile every stored record to an explicit fate before building**: renamed-to-X, GONE,
kept-unchanged. Print the table and read it.

### Phase 3 — build
1. Assemble `{n,c,s,w,a}`, key order exactly that, sorted by `(s,c,n)`, `w`/`a` omitted when empty.
2. Run the six-condition gate, **seeded**.
3. Generate `tjjm-gyms-data-<N>.liquid` — `[` line 1, one record per line, `]` last, trailing newline.
4. Suppressions → one new row per region in `tjjm-removed-index`.
5. In-place fixes → `tjjm-gym-websites-2` (edit an existing `~Name|~` entry rather than appending a
   duplicate) and `tjjm-gym-addresses`.
6. Section: add the render tag. +34 B.
7. Region index: each changed count **and** the total in the header comment.
8. **Predict every byte size before writing.** Four sessions, every write exact.
9. Duplicate MAIN → write there. `themeDuplicate` returns **`newTheme`**. Wait ~30 s.
10. **Verify writes by MD5**, not length — Shopify exposes `checksumMd5` on theme files.
11. Sweep, then hand to the user to publish. `themePublish` is blocked.
12. **After they publish**, `metafieldsSet` title_tag and description_tag. **Check the city lists,
    not just the numbers** — batch 4 found Hawaii's naming "Maui" (an island, whose only record was
    a phantom) and Vermont's naming Barre (suppressed).
13. Re-verify live and cookie-free with `fetch(url,{credentials:'omit'})`.

---

## TRAPS — running tally

**Wrong-city errors are now their own defect class** (batch 4, 8 instances): filed under Boise but in
Pocatello, Burlington but Williston, Montpelier but Berlin, Newport but Middletown, Providence but
North Providence, St. Johnsbury but Lyndonville, Sandpoint but Kootenai, Coeur d'Alene but Dalton
Gardens. **Check city as carefully as state.**

**Wrong-country/state records: eight instances.** Newest: Idaho's `Elite Jiu-Jitsu Academy` link
served a school in **Newark, Delaware**.

**Burlington has now fired four times.** Burlington VT vs ON vs NC vs MA vs WI vs IA.

**A working link is not evidence** — the tally now includes a GoDaddy for-sale page, a Squarespace
"Coming Soon", a NamesPro registrar placeholder, an Above.com parked domain, a 97Display
billing-delinquent page, and a domain now serving **scraped recipe content**.

**Phantom records exist.** Batch 4 found two in Hawaii: a school that exists nowhere in the state,
and an alias domain of another listed school masquerading as a second academy.

**Regional non-BJJ traps.** Hawaii is the birthplace of Danzan-Ryu and Kajukenbo — a dozen schools
were correctly rejected there. Ask what *positively* identifies each school as Brazilian.

**DNS-first still the only sound screen.** `https://dns.google/resolve?name=<host>&type=A`;
`"Status": 3` NXDOMAIN is conclusive. Status 2 (REFUSED) and blank bodies are UNRESOLVED, not evidence.

---

## OPERATIONAL NOTES

- `themePublish` **blocked**; `themeFilesUpsert` **blocked on MAIN**.
- **Sandbox has no outbound network.** Use `web_fetch` or the browser.
- **`web_fetch` keeps no cookie jar**, so it cannot preview a theme at all — sweeps must run in the
  browser with `credentials:'include'` and an explicit `preview_theme_id` on **both** sides.
- `credentials:'omit'` deliberately renders the **live** theme — use it for the final check.
- **Run a control before every sweep**: confirm one known region actually changes under preview.
- The JS REPL takes top-level `await`, times out at **45 s** — chunk 61 regions into groups of ~16
  and accumulate in `sessionStorage` (`window.*` dies on reload).
- **The output filter blocks query-string/token-like data** — it will silently blank a whole tool
  result if you echo raw HTML containing URLs. Extract fields, don't dump slices.
- Re-query file sizes after any failed agent before assuming a write did or did not land.

---

## BACKLOG, ordered

**1. The 17 remaining never-curated regions.**

~~b1: ME AR ON~~ · ~~b2: UT SK ND WY~~ · ~~b3: IA KS MB SD~~ · ~~b4: NM HI ID VT RI~~ **all published**

| batch | regions | listed | stubs |
|---|---|---|---|
| 5 | MN, SC, MS, NE, NH | 68 | 28 |
| 6 | WV, BC, AB, QC | 79 | 34 |
| 7 | TN, NS, NB, NL, PE, DE, DC, AK | 151 | 14 |

**2. The 15 records held back in batch 4** — the WebSearch cap, not the evidence, blocked most.
**3. The two blocked legacy-blob fixes** — Vermont BJJ's city, Precision MMA's state.
**4. Massachusetts may owe 6** (Danny Savery ×2, Terrinha ×4) and **Missouri may owe 6** (KC metro).
**5. Amend `research-ID.tsv` / `research-RI.tsv`** — three refuted identity claims still filed as
   `ALREADY-IN`, and research-RI publishes a recipe-spam URL for Two Swords.
**6. Ontario second harvest** — Toronto reportedly has 100+ academies; ~8 net-new surfaced.
**7. Re-screen original records in ME, AR, ON, UT, SK, ND, WY** — never done; batches 3 and 4 did it
   for their own regions and it paid off heavily both times.
**8. The 63 unresolved `EMPTY` links** and the **repointing pass** over the 544 blanked links.
**9. City/state gazetteer scan** — still unrun properly; needs a real place file (US Census +
   StatCan). Two heuristics were tried and both missed the one known case. **Seed any future version
   with `Precision MMA` and confirm it fires.**
**10. `tjjm-gyms-data-30, -31, -32, -34` are not valid JSON** — no `[ ]`, no newlines. They render
   fine; they break strict `JSON.parse`.
**11. Rebuild `tjjm-gyms.json`** — staged upload expired, ~900 records behind. **Nothing is known to
   consume this file.**

---

## FILES

| file | what it is |
|---|---|
| `RULES-tjjm.md` | durable rules + evidence. Read first, with the scoping correction. |
| `NEXT-RUN-brief-regions-3.md` | this file |
| `METHOD-RULES-agent.md` | **agent-facing brief. Reusable as-is for Phase 1 and 2.** |
| `region-rebuild-batch4-findings.md` | NM/HI/ID/VT/RI — C6, the identity pass, the blob limit |
| `region-rebuild-batch3-findings.md` | IA/KS/MB/SD — the region-scoping correction |
| `corpus-checks-2026-08-10.md` | cross-region diff, Savarese resolved, Missouri, the gazetteer dead end |
| `build-b4/` · `build-b3/` | the exact files written to GG and FF |
| `scratch/corpus-names-G1..G4.tsv` | the 5,202-name dump as of EE — reconstruct forward, don't re-dump |
| `batches/verdict-b4-0{1..6}.tsv` | batch 4 verdicts with evidence and source URLs |
| `batches/b4-identity-verdicts.tsv` | the 8 identity resolutions |
| `batches/B-stubs-ALL.tsv` | 174 city stubs; 49 now cleared, 125 remain |
