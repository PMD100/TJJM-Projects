# Session brief — REGION REBUILDS, batch 6 onward. Start here.

Written 12 Aug 2026. Supersedes `NEXT-RUN-brief-regions-3.md`. Adds gate condition C7 and the
aggregator-fabrication warning.

Paste the block below into a **new** chat with the `TJJM Projects` folder connected.

---

## The block to paste

> Continuing the TJJM BJJ directory. Read `NEXT-RUN-brief-regions-4.md` first, then `RULES-tjjm.md`,
> then `region-rebuild-batch5-findings.md`. RULES is canonical where they overlap **except** for the
> removed-index scoping correction, where the batch-3/4/5 findings are newer and proven.
>
> **Everything through region-rebuild batch 5 is DONE AND PUBLISHED.** Live theme is
> `Aug 12 BJJ Gyms HH` (`154860028076`), 5,020 records across 61 regions. Do not redo it.
>
> The work now is **region rebuilds for the 12 remaining never-curated regions**, in batches of 4.
> The method is proven five times; follow the RECIPE exactly.
>
> Before anything: **confirm the Shopify connector is on thejiujitsumindset.com** (it has silently
> switched stores once), then re-verify the live theme id and record count.

---

## STATE — verified live 12 Aug 2026

**MAIN = `Aug 12 BJJ Gyms HH` (`gid://shopify/OnlineStoreTheme/154860028076`).**

| | count |
|---|---|
| corpus | **5,020** rendered / 61 regions |
| stored records | **5,600** (5,020 rendered + 580 region-scoped suppressions) |
| MN 52 · SC 34 · MS 27 · NE 21 · NH 33 | (were 18/14/14/12/10) |

Next data file is **`tjjm-gyms-data-42`**. Next theme letter is **II**.

### File headroom
- `sections/tjjm-state-directory.liquid` — **12,725** B of ~24,576. Each data file costs +34 B.
- `snippets/tjjm-gym-websites-2.liquid` — **20,256** B of ~24,576. **~4.3 KB left**, roughly 80 more
  override rows. A bigger batch needs `tjjm-gym-websites-3` plus a render tag in `web_overrides`.
- `snippets/tjjm-gym-addresses.liquid` — 8,104 B. Plenty.
- `snippets/tjjm-removed-index.liquid` — 11,718 B, 48 region rows.

### Theme stack
- **KEEP** MAIN `154860028076` (HH).
- **Rollback:** `154856816812` (GG), `154774995116` (FF), `154717487276` (EE).
- **Disposable:** DD `154712932524` and older.
- `154657063084` is the audit-dump harness. Keep. **Not** a valid "before" theme.

---

## THE COLLISION GATE — SEVEN conditions

`tjjm-gym-websites` and `tjjm-gym-addresses` match **on name alone, corpus-wide**.
`tjjm-removed-index` matches **on name within its own region row only**.

1. no new name equals any existing corpus name
2. no new name equals another new name
3. no new name equals a name in either overrides file
4. every suppressed name appears exactly once **in its own region**
5. no name anywhere contains `|` or `~`
6. **no name is both SUPPRESSED and ADDED in the same region** — makes the new record render nothing
7. **the Nebraska/Newfoundland rule** ← new, batch 5

### C7, and why it exists
Newfoundland records are stored as `s:"NE"` and separated from Nebraska only by a city list inside
the section. The section sets `scan_code = 'NE'` when rendering the **Newfoundland** page, so **both
pages read the same `NE` removed-index row**, and the suppression check runs *before* the city split.

- **C7a** — no new Nebraska record may use a city in `nl_cities`
  (St. John's, Corner Brook, Gander, Paradise, Conception Bay South, Labrador City,
  Grand Falls-Windsor, Clarenville, Mount Pearl, Torbay)
- **C7b** — no Nebraska suppression may match a Newfoundland record name. Newfoundland holds
  `Corner Brook BJJ`, `Gander BJJ`, `Labrador City BJJ`, `St. John's BJJ` — exactly the stub shape
  Nebraska also uses.

Batch 5 created the first NE suppression row. **If you ever touch NE or NL again, assert Newfoundland's
count is unchanged before and after.**

**Always seed the gate with known-bad input and confirm all seven fire before believing a clean run.**

### The silent-blank-override class — four instances
`Jungle Gym Martial Arts` · `Action & Reaction MMA` · `Ethos BJJ` · `Alliance Jiu Jitsu Easley`.
A new record sharing a name with a record carrying a **blank** override renders with no link at all.
When fixing an existing record's URL, **edit its existing override entry rather than appending a
duplicate**. Budget roughly one collision per 20 new records.

---

## THE RECIPE

### Phase 0 — corpus
Reconstruct rather than re-dump: `previous dump + previous batch's data files`, then assert
`stored − region-scoped suppressions == published total`. Off by one means stop.
Current base: `scratch/gg-corpus.json` (5,444) + `build-b5/tjjm-gyms-data-41.liquid` (156) = 5,600.

### Phase 1 — research (one agent per region)
Point each at `METHOD-RULES-agent.md`; have it fetch the live page itself.

### Phase 2 — verification (one agent per ~24 candidates)
**Never skip.** Defect rates: batch 3 **29%**, batch 4 **33%**, batch 5 **34%**.
⚠️ **Run in waves of four, not eight at once.** The shared WebSearch budget caps per session and has
blown out twice. Tell agents to screen with DNS and go straight to the school's own site; batch 5's
first wave used only 18 searches across four agents doing that.

### Phase 2b — identity reconciliation
Researchers write schools' **corrected** names, so joins back to stored stub names fail silently.
⚠️ **Extract the verdict with a regex on the leading keyword, not a split on `:` or ` -`.** Different
agents delimit differently — batch 5's MS/NE/NH/SC agents used a **period**, which silently produced
"0 suppressions" for three whole regions until caught.
Print the fate of every stored record and read the table.

### Phase 3 — build
1. Assemble `{n,c,s,w,a}`, key order exactly, sorted by `(s,c,n)`, `w`/`a` omitted when empty.
2. Seven-condition gate, **seeded**.
3. Generate the data file — `[` line 1, one record per line, `]` last, trailing newline.
4. Suppressions → one new row per region in `tjjm-removed-index`.
5. In-place fixes → overrides. **Skip any override that restates the stored value.**
6. Section render tag (+34 B). Region index counts **and** the total in the comment.
7. **Predict every byte size before writing.** Five sessions, every write exact.
8. **Stage everything in `build-b<N>/` in the mounted folder — never `/tmp`, which is wiped between
   sessions.** A fully built batch was lost that way.
9. Duplicate MAIN → write there. `themeDuplicate` returns **`newTheme`**. Wait ~30 s.
10. **Verify writes by MD5** — Shopify exposes `checksumMd5` on theme files.
11. Sweep with a control first, hand over to publish.
12. **After publish**, `metafieldsSet`. **Check the city lists, not just the numbers** — batch 5 had
    five cities drop to zero records (Moorhead, Gulfport, Corinth, Norfolk, Columbus NE) that were
    still named in descriptions.
13. Re-verify live cookie-free with `fetch(url,{credentials:'omit'})`.

---

## TRAPS — running tally

**Working links serving the wrong business — now the single largest defect class.** Batch 5 alone:
Cardiff **Wales**, Oxfordshire **England**, Lincoln **England**, plus California ×2, Missouri,
Maryland, Alabama, North Carolina and South Carolina. **Every one returns 200.**

**Aggregators fabricate.** MatMade appears to have **invented** a Manchester NH school, and files
Rochester **Indiana**, Portsmouth **Virginia** and Exeter **England** under New Hampshire towns.
Treat any row whose only source is MatMade as UNVERIFIED.

**SEO doorway pages.** `fightworksacademy.com` publishes ~15 SC city pages that are one gym. A city
page is not a location — but verify both ways: Renzo Gracie NH's three sites *are* genuinely separate.

**Title tags lie about discipline.** Two batch-5 schools advertised BJJ in the title while the body
sold karate and TaeKwonDo respectively. Judge on the rendered class list.

**Wrong-city errors** remain the most common single defect. Watch footers printing a **mailing city**
(two MN schools print "Minneapolis" for ZIPs that are Coon Rapids and Plymouth).

**Brands filed in the wrong state.** `Roufusport MMA Academy` sat under Minneapolis; it is a
Milwaukee brand with zero Minnesota locations.

**DNS-first is still the only sound screen.** `Status 3` NXDOMAIN is conclusive; Status 2 and blank
bodies are UNRESOLVED, not evidence.

---

## OPERATIONAL NOTES

- `themePublish` **blocked**; `themeFilesUpsert` **blocked on MAIN**.
- ⚠️ **The 113 KB legacy blob cannot be rewritten through this toolchain** — `themeFilesUpsert` takes
  the whole body as a mutation argument, ~65k tokens of transcription over a dense JSON array with no
  redundancy. Any fix needing a change to `n`, `c` or `s` inside it is blocked. Overrides can fix `w`
  and backfill a blank `a` only. Landing blob edits needs Shopify CLI or the Assets REST endpoint.
- **Sandbox has no outbound network**; `mcp__workspace__bash` cannot fetch. Use `web_fetch` or the browser.
- **`web_fetch` keeps no cookie jar** so it cannot preview a theme, and **dedupes within a session** —
  an "already fetched" with no content means request a subpage or the other host form.
- Sweeps: browser, sequential, `credentials:'include'`, explicit `preview_theme_id` on **both** sides,
  cache-buster, **control first**. `credentials:'omit'` renders the **live** theme.
- JS REPL times out at **45 s** — chunk 61 regions into groups of ~16, accumulate in `sessionStorage`.
- **The output filter blanks a whole tool result if you echo raw HTML containing URLs.** Extract fields.

---

## BACKLOG, ordered

**1. The 12 remaining never-curated regions.**

~~b1 ME AR ON~~ · ~~b2 UT SK ND WY~~ · ~~b3 IA KS MB SD~~ · ~~b4 NM HI ID VT RI~~ ·
~~b5 MN SC MS NE NH~~ **all published**

| batch | regions | listed | stubs |
|---|---|---|---|
| 6 | WV, BC, AB, QC | 79 | 34 |
| 7 | TN, NS, NB, NL, PE, DE, DC, AK | 151 | 14 |

⚠️ **Batch 7 contains NL.** Re-read C7 before touching it.
⚠️ **Batch 6 is the first with three Canadian regions** — BC, AB and QC total 69 records. Quebec will
need French-language handling and Montreal is a major BJJ city.

**2. Held-back records: 29 from batch 5, 15 from batch 4, plus batch 3's 9.**
**3. Cross-region debts surfaced but not filed** — ND 2, WI 2, ME 1 (Port City has moved to Kittery),
   MA 6, MO 6, plus NC/GA/TX/TN/IA singles. See each batch's findings file.
**4. Three unresolved identity questions** from batch 5: TC Martial Arts, Winona BJJ, Seacoast BJJ NH.
**5. The two blocked legacy-blob fixes** — Vermont BJJ's city, Precision MMA's state.
**6. Ontario second harvest** and **re-screen the original records in ME, AR, ON, UT, SK, ND, WY.**
**7. The 63 unresolved `EMPTY` links** and the **repointing pass** over 544 blanked links.
**8. City/state gazetteer scan** — still unrun properly. **Seed it with `Precision MMA` and confirm
   it fires**; two heuristics were tried and both missed the one known case.
**9. `tjjm-gyms-data-30, -31, -32, -34` are not valid JSON** — render fine, break strict `JSON.parse`.
**10. Rebuild `tjjm-gyms.json`** — expired, ~1,000 records behind. Nothing is known to consume it.

---

## FILES

| file | what it is |
|---|---|
| `RULES-tjjm.md` | durable rules + evidence. Read first, with the scoping correction. |
| `NEXT-RUN-brief-regions-4.md` | this file |
| `METHOD-RULES-agent.md` | **agent-facing brief. Reusable as-is for Phase 1 and 2.** |
| `region-rebuild-batch5-findings.md` | MN/SC/MS/NE/NH — C7, the Wales/England links, MatMade fabrication |
| `region-rebuild-batch4-findings.md` | NM/HI/ID/VT/RI — C6, the identity pass, the blob limit |
| `region-rebuild-batch3-findings.md` | IA/KS/MB/SD — the region-scoping correction |
| `corpus-checks-2026-08-10.md` | cross-region diff, Savarese resolved, the gazetteer dead end |
| `build-b5/` `build-b4/` `build-b3/` | the exact files written to HH, GG and FF |
| `scratch/gg-corpus.json` | 5,444-record corpus as of GG — reconstruct forward from here |
| `batches/verdict-b5-0{1..8}.tsv` | batch 5 verdicts with evidence and source URLs |
| `batches/B-stubs-ALL.tsv` | 174 city stubs; 75 now cleared, 99 remain |
