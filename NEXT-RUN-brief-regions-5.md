# Session brief — REGION REBUILDS, batch 7 (the last one). Start here.

Written 12 Aug 2026. Supersedes `NEXT-RUN-brief-regions-4.md`.

Paste the block below into a **new** chat with the `TJJM Projects` folder connected.

---

## The block to paste

> Continuing the TJJM BJJ directory. Read `NEXT-RUN-brief-regions-5.md` first, then `RULES-tjjm.md`,
> then `region-rebuild-batch6-findings.md`. RULES is canonical where they overlap **except** for the
> removed-index scoping correction, where the batch-3/4/5/6 findings are newer and proven.
>
> **Everything through region-rebuild batch 6 is DONE AND PUBLISHED.** Live theme is
> `Aug 12 BJJ Gyms JJ` (`154865860780`), 5,205 records across 61 regions. Do not redo it.
>
> **Batch 7 is the last never-curated batch: TN, NS, NB, NL, PE, DE, DC, AK** — 151 records.
> ⚠️ It contains **NL**, so gate condition C7 applies. Read it before touching anything.
>
> Before anything: **confirm the Shopify connector is on thejiujitsumindset.com** (it has silently
> switched stores once), then re-verify the live theme id and record count.

---

## STATE — verified live 12 Aug 2026

**MAIN = `Aug 12 BJJ Gyms JJ` (`gid://shopify/OnlineStoreTheme/154865860780`).**

| | count |
|---|---|
| corpus | **5,205** rendered / 61 regions |
| stored records | **5,841** (5,205 + 636 region-scoped suppressions) |
| WV 28 · AB 72 · BC 101 · QC 63 | (were 10/22/26/21) |

Next data file is **`tjjm-gyms-data-44`**. Next theme letter is **KK**.

### File headroom
- `sections/tjjm-state-directory.liquid` — **12,793** B of ~24,576. Each data file costs +34 B.
- `snippets/tjjm-gym-websites-2.liquid` — **20,491** B of ~24,576. **~4.0 KB left, roughly 75 override
  rows.** Batch 7 has 151 records and heavy link rot — **plan for a `tjjm-gym-websites-3`** plus a
  render tag in the section's `web_overrides` capture.
- `snippets/tjjm-gym-addresses.liquid` — 8,507 B. Plenty.
- `snippets/tjjm-removed-index.liquid` — 12,593 B, 52 region rows.

### Theme stack
- **KEEP** MAIN `154865860780` (JJ).
- **Rollback:** `154862780588` (II), `154860028076` (HH), `154856816812` (GG).
- **Disposable:** FF `154774995116` and older.
- `154657063084` is the audit-dump harness. Keep. **Not** a valid "before" theme.

---

## THE COLLISION GATE — SEVEN conditions, plus a city-spelling check

`tjjm-gym-websites` and `tjjm-gym-addresses` match **on name alone, corpus-wide**.
`tjjm-removed-index` matches **on name within its own region row only**.

1. no new name equals any existing corpus name
2. no new name equals another new name
3. no new name equals a name in either overrides file
4. every suppressed name appears exactly once **in its own region**
5. no name anywhere contains `|` or `~`
6. **no name is both SUPPRESSED and ADDED in the same region** — the new record renders nothing
7. **the Nebraska/Newfoundland rule** — see below
8. **city-spelling fold check** — no new city string may fold (strip accents, lowercase, normalise
   hyphens) to an existing city string in that region. The section groups by exact city string, so a
   variant spelling silently creates a second heading for the same place. Quebec introduced 18 new
   city strings in batch 6 and this check cleared them all.

**Always seed the gate with known-bad input and confirm every condition fires before believing a
clean run.**

### ⚠️ C7 APPLIES TO BATCH 7 — Newfoundland is in it
Newfoundland records are stored as `s:"NE"` (Nebraska's code) and split only by a city list inside
the section. The section sets `scan_code = 'NE'` when rendering the **Newfoundland** page, so **both
pages read the same `NE` removed-index row**, and the suppression check runs *before* the city split.
Batch 5 created the first NE row, so that row now exists and is live.

- **C7a** — no new Nebraska record may use a city in `nl_cities`
- **C7b** — no Nebraska suppression may match a Newfoundland record name
- **New for batch 7:** the reverse also applies. Any **NL** work must not collide with Nebraska's
  existing 21 records, and there is no NL row in the removed-index — suppressing an NL record means
  **adding names to the NE row**, which will also apply to the Nebraska page.
- **Assert Nebraska's count is unchanged before and after any NL work, and vice versa.**

### The silent-blank-override class — five instances
`Jungle Gym Martial Arts` · `Action & Reaction MMA` · `Ethos BJJ` · `Alliance Jiu Jitsu Easley` ·
`Ironside Martial Arts`. A new record sharing a name with a record carrying a **blank** override
renders with no link at all. When fixing an existing record's URL, **edit its existing override entry
rather than appending a duplicate**. Budget roughly one collision per 20 new records.

---

## THE RECIPE

### Phase 0 — corpus
**Already done for you: `scratch/jj-corpus.json` is the theme JJ stored corpus, 5,841 records,
validated as `5,841 − 636 region-scoped suppressions = 5,205`, matching the live total.** Load it and
re-assert that identity before trusting it; if it does not hold, rebuild from
`scratch/ii-corpus.json` (5,693) + `build-b6b/tjjm-gyms-data-43.liquid` (148).

For future batches, reconstruct rather than re-dumping: `previous corpus + previous batch's data
files`, then assert `stored − region-scoped suppressions == published total`. Off by one means stop.

### Batch 7 starting counts (verified 12 Aug 2026)
TN 34 · AK 22 · NS 23 · NB 15 · NL 15 · PE 10 · DE 7 · DC 7 — **133 records**, not the 151 the older
brief estimated. Tennessee and Alaska are the two substantial ones.

### Phase 1 — research (one agent per region)
Point each at `METHOD-RULES-agent.md`; have it fetch the live page itself.
**Batch 7 is eight regions but only 151 records** — several are tiny (DE 7, DC 7, PE 10, NH-scale).
Consider two agents covering four small regions each rather than eight separate agents.

### Phase 2 — verification (one agent per ~24 candidates, **in waves of four**)
**Never skip.** Defect rates: 29% → 33% → 34% → 46% → **84%**. The trend is upward and the larger
the region, the worse. Waves of four protect the shared WebSearch budget, which has capped out twice.

⚠️ **Extract research verdicts with a leading-keyword regex, not a split on `:` or ` -`.** Agents
delimit inconsistently — batch 5's used a period, which silently produced "0 suppressions" for three
whole regions until the arithmetic looked wrong.

### Phase 2b — identity reconciliation
Researchers write **corrected** names, so joins back to stored stub names fail silently. Print the
fate of every stored record and read the table. Batch 4 had 8 unmatchable records; resolving them
refuted three earlier matches, one made from a meta-description.

### Phase 3 — build
1. Assemble `{n,c,s,w,a}`, key order exactly, sorted by `(s,c,n)`, `w`/`a` omitted when empty.
2. Eight-condition gate, **seeded**.
3. Data file — `[` line 1, one record per line, `]` last, trailing newline.
4. Suppressions → one new row per region in `tjjm-removed-index`.
5. In-place fixes → overrides. **Skip any override that restates the stored value.**
6. Section render tag (+34 B). Region index counts **and** the total in the comment.
7. **Predict every byte size before writing.** Six sessions, every write exact.
8. **Stage everything in `build-b<N>/` in the mounted folder — never `/tmp`, which is wiped between
   sessions.** A fully built batch was lost that way.
9. Duplicate MAIN → write there. `themeDuplicate` returns **`newTheme`**. Wait ~30 s.
10. **Verify writes by MD5** (`checksumMd5` on theme files), and **re-query after ANY agent failure** —
    a 6b write agent died mid-job having landed 4 of 6 files, one of them missing entirely while the
    section already referenced it.
11. Sweep with a control first, hand over to publish.
12. **After publish**, `metafieldsSet`. **Check the city lists, not just the numbers** — five cities
    dropped to zero records in batch 5 while still named in descriptions.
13. Re-verify live cookie-free with `fetch(url,{credentials:'omit'})`.

---

## TRAPS — running tally

**Wrong province/country records: 20+ found so far.** Batch 6 alone produced nine, including
Northern Ireland, Ontario ×3, Quebec ×2, Alberta, Maryland and New York. **Every one returns 200.**

**Aggregators fabricate.** MatMade invented a Manchester NH school and files Rochester **Indiana**
and Exeter **England** under New Hampshire. `westcoastbjj.ca`'s affiliate list is copyrighted **2014**
and three batch-6 rows rest on it alone.

**⚠️ AGENTS FABRICATE TOO.** A batch-6 researcher recorded a black-belt lineage that appears nowhere
on the school's site. `METHOD-RULES-agent.md` now has an explicit clause forbidding this — make sure
every agent reads it. Conversely, **reward honest self-flagging**: Alberta's researcher marked ~30
rows "body not individually read" and verifiers found two thirds defective.

**Title tags lie about discipline.** Schools advertising BJJ whose rendered class list sells karate,
TaeKwonDo, kickboxing or Japanese jujitsu. Batch 6 rejected **20** on this basis.

**Wrong-city errors** remain very common. Watch mailing-city footers and brand-vs-location mismatches
(a school branded "Omaha" in Papillion, "Greenville" in Greer, "Coeur d'Alene" in Dalton Gardens).

**DNS-first is the only sound screen.** `Status 3` NXDOMAIN is conclusive; Status 2 and blank bodies
are UNRESOLVED, not evidence. And a typo hypothesis does not always pay — `grandeprairiebjj.com` is
NXDOMAIN too.

---

## OPERATIONAL NOTES

- `themePublish` **blocked**; `themeFilesUpsert` **blocked on MAIN**.
- ⚠️ **The 113 KB legacy blob cannot be rewritten through this toolchain** — no streaming, ~65k tokens
  of transcription with no redundancy. Any fix needing a change to `n`, `c` or `s` inside it is
  blocked; overrides can fix `w` and backfill a blank `a` only. **Workaround that works:** suppress
  the record and re-add a corrected copy in the new data file (different name, or a different region).
  Used successfully for `Parkersburg BJJ` → `Parkersburg Martial Arts Center` in Vienna.
- **Sandbox has no outbound network**; `mcp__workspace__bash` cannot fetch. Use `web_fetch` or the browser.
- **`web_fetch` keeps no cookie jar** so it cannot preview a theme, and **dedupes within a session**.
- Sweeps: browser, sequential, `credentials:'include'`, explicit `preview_theme_id` on **both** sides,
  cache-buster, **control first**. `credentials:'omit'` renders the **live** theme.
- JS REPL times out at **45 s** — chunk 61 regions into groups of ~16, accumulate in `sessionStorage`.
- **The output filter blanks a whole tool result if you echo raw HTML containing URLs.** Extract fields.

---

## BACKLOG, ordered

**1. Batch 7 — the last never-curated regions: TN, NS, NB, NL, PE, DE, DC, AK.** 151 records, 14 stubs.
   Tennessee is the big one at 34. ⚠️ NL triggers C7.

**2. Held-back records: 32 from batch 6, 29 from batch 5, 15 from batch 4, 9 from batch 3 — 85 total.**
   Many would clear with a browser render (JS-only sites) rather than more research.

**3. Cross-region debts surfaced but never filed** — a substantial list now spanning WA, ON, MD, OH,
   NY, VA, ND, WI, ME, MA, MO, NC, GA, TX, TN, IA. Each batch's findings file has its own list. This
   is probably worth one dedicated session.

**4. Montreal second harvest** — ~20–25 aggregator-only candidates the QC researcher correctly
   declined to launder.

**5. The two blocked legacy-blob fixes** — Vermont BJJ's city, Precision MMA's state (the latter is
   already suppressed, so it is latent only).

**6. Ontario second harvest** and **re-screen the original records in ME, AR, ON, UT, SK, ND, WY** —
   never done; every batch that has done it found major defects.

**7. The 63 unresolved `EMPTY` links** and the **repointing pass** over 544 blanked links. Note batch
   6 recovered live URLs for 8 of 19 already-blanked records in its own regions — the repointing
   backlog is clearly productive.

**8. City/state gazetteer scan** — still unrun properly. **Seed it with `Precision MMA` and confirm it
   fires**; two heuristics were tried and both missed the one known case.

**9. `tjjm-gyms-data-30, -31, -32, -34` are not valid JSON** — render fine, break strict `JSON.parse`.

**10. Rebuild `tjjm-gyms.json`** — expired, ~1,200 records behind. Nothing is known to consume it.

---

## FILES

| file | what it is |
|---|---|
| `RULES-tjjm.md` | durable rules + evidence. Read first, with the scoping correction. |
| `NEXT-RUN-brief-regions-5.md` | this file |
| `METHOD-RULES-agent.md` | **agent-facing brief. Now includes the never-fabricate clause. Reusable as-is.** |
| `region-rebuild-batch6-findings.md` | WV/AB/BC/QC — the 84% defect rate, the fabrication, the half-landed write |
| `region-rebuild-batch5-findings.md` | MN/SC/MS/NE/NH — C7, the Wales/England links, MatMade fabrication |
| `region-rebuild-batch4-findings.md` | NM/HI/ID/VT/RI — C6, the identity pass, the blob limit |
| `region-rebuild-batch3-findings.md` | IA/KS/MB/SD — the region-scoping correction |
| `corpus-checks-2026-08-10.md` | cross-region diff, Savarese resolved, the gazetteer dead end |
| `build-b6b/` `build-b6a/` `build-b5/` `build-b4/` `build-b3/` | exact files written to each theme |
| `scratch/ii-corpus.json` | 5,693-record corpus as of theme II — reconstruct forward from here |
| `batches/verdict-b6{a,b}-*.tsv` | batch 6 verdicts with evidence and source URLs |
| `batches/B-stubs-ALL.tsv` | 174 city stubs; 109 now cleared, 65 remain |
