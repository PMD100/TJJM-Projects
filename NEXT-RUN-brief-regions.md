# Session brief — REGION REBUILDS. Start here.

Written 7 Aug 2026 at the end of a very long session. Supersedes `NEXT-RUN-brief-NY-3.md` for the
state of the work; that file's *method warnings* still hold and are folded in below.

Paste the block below into a **new** chat with the `TJJM Projects` folder connected.

---

## The block to paste

> Continuing the TJJM BJJ directory. Read `NEXT-RUN-brief-regions.md` first, then `RULES-tjjm.md`.
> RULES is canonical where the two overlap.
>
> **Everything through region-rebuild batch 2 is DONE AND PUBLISHED.** Live theme is
> `Aug 7 BJJ Gyms EE` (`154717487276`), 4,768 records across 61 regions. Do not redo it.
>
> The work now is **region rebuilds for the 24 remaining never-curated regions**, in batches of
> 3–4. The method is proven; follow the RECIPE section of the brief exactly.
>
> Before anything: re-verify the live theme id and record count, and re-derive any buildId rather
> than trusting a written one.

---

## STATE — what is live, verified 7 Aug 2026

**MAIN = `Aug 7 BJJ Gyms EE` (`gid://shopify/OnlineStoreTheme/154717487276`).**

| | count |
|---|---|
| corpus | **4,768** records / 61 regions |
| New York | 182 (was 64) |
| Maine | 23 (was 11) · Arkansas | 56 (was 35) |
| Ontario | 107 (was 40) |
| Utah | 46 (was 14) · Saskatchewan | 14 (was 11) |
| North Dakota | 11 (was 9) · Wyoming | 10 (was 9) |

Verified live, cookie-free: on all four regions **title tag = JSON-LD `numberOfItems` = body
count**. No inconsistency window open.

### What this session shipped

1. **New York import** — 64 → 182. 130 imported of 186 candidates, 12 legacy suppressed, 15 link
   fixes. Full evidence in `ny-step5-verdicts.md`.
2. **Corpus-wide link audit** — all 4,282 published outbound links screened, 899 flagged.
3. **544 links blanked** — 435 in the 27 curated states, 109 in never-curated regions. Every gym
   stayed listed; only the bad URL was removed.
4. **10 wrong-entity links removed** — lapsed gym domains now serving a Norwegian casino, an
   Indonesian gambling site, Chinese lottery spam, two Chinese manufacturers, a Japanese parenting
   blog, a credit-repair firm, a software consultancy, a parks authority, a bare payment page.
5. **Region rebuild batch 1** — Maine, Arkansas, Ontario. +117 schools, 17 stubs suppressed.
6. **Region rebuild batch 2** — Utah, Saskatchewan, North Dakota, Wyoming. +77 schools, 39 stubs
   suppressed. Utah alone went 14 -> 46. Metafields updated for all 7 rebuilt regions.

### Theme stack — keep or delete

- **KEEP** MAIN `154717487276` (EE).
- **Rollback points, keep for now:** `154712932524` (DD), `154697138348` (CC), `154695565484` (BB),
  `154694877356` (AA), `154665025708` (ZZ).
- **Disposable:** `154658242732` (YY), `154653950124` (XX), `154658209964`, `154661355692`
  (the pre-NY baseline — superseded).
- `154657063084` is the audit-dump harness. Keep. **Not** a valid "before" theme.

---

## THE RECIPE — this works, follow it

Three phases per batch of regions. Roughly two hours a batch. Each batch is independently
shippable.

### Phase 1 — research (one agent per region, ~6 min each)
Give the agent: the region's current listings (**have it fetch the live page itself** — see the
transcription warning below), the list of suspect records, and the METHOD RULES. Ask for the full
roster of schools actually operating in the region, marked ALREADY-IN or NET-NEW, plus a validation
of each suspect. Prioritise breadth of cities over exhaustiveness in the biggest city.

### Phase 2 — verification (one agent per ~23 candidates, ~7 min each)
**Do not skip this.** Research output is provisional: in Ontario only ~10 of 95 had been opened,
and when all 89 were checked, **3 were in the wrong country** and roughly a fifth had a wrong name,
city or address. Have each agent open every candidate and extract the name and street address from
the page **body**.

### Phase 3 — build
1. Assemble records `{n,c,s,w,a}`, key order exactly that, sorted by `(s,c,n)`.
2. **Run the collision gate** (below). It is the step most likely to be got wrong.
3. Generate `tjjm-gyms-data-<N>.liquid` — compact JSON, one record per line, `[` first line,
   `]` last, trailing newline.
4. Suppressions → a new row per region in `tjjm-removed-index`, format `CODE|Name|Name|...`.
5. URL fixes → `tjjm-gym-websites-2` (**file 1 is nearly full**; file 2 is at 19,998 B of a
   ~24 KB ceiling, so **the next batch needs a file 3** and a matching render tag).
6. Section: add `{%- render 'tjjm-gyms-data-<N>' -%}` to the `gym_json` capture. +34 bytes.
7. Region index: update each changed count **and** the total in the comment.
8. **Predict every byte size before writing.** Every write this session hit its prediction exactly.
9. Duplicate MAIN → write there (writes are blocked on MAIN). Wait ~30 s before files are readable.
10. Verify by sweep (below), then hand to the user to publish. `themePublish` is blocked.
11. **`metafieldsSet` the changed regions' `title_tag` and `description_tag`** — they are global,
    not theme-scoped, so they hit the live site immediately. Only change the number; the city lists
    stay accurate. **This was nearly forgotten this session** — the pages shipped correct while
    search results understated by 100 schools.

---

## THE COLLISION GATE — run it, and check that it actually ran

Every name-keyed mechanism in this theme — `tjjm-removed-index` suppression, `tjjm-gym-websites`
overrides, `tjjm-gym-addresses` backfill — **matches on NAME ALONE, corpus-wide**. A shared name
silently applies one record's correction to another.

Before writing any batch, assert:

1. no new name equals any existing corpus name
2. no new name equals another new name
3. no new name equals a name already present in either overrides file
4. every name being suppressed appears **exactly once** in the corpus
5. no name anywhere contains `|` or `~`

**Both times this gate was skipped or broken, it cost a defect:**
- `Jungle Gym Martial Arts` — a New Rochelle record and a genuinely separate Bronx location shared
  a name. The New Rochelle website override would have silently repointed the Bronx record.
  Imported as `Jungle Gym Martial Arts - Bronx`.
- `Action & Reaction MMA` — a new Pickering ON school collided with a Laval QC record carrying a
  **blank** override, so the new school would have rendered with no link. Renamed
  `Action & Reaction MMA Pickering`. A second collision in the same check,
  `Brampton Brazilian Jiu Jitsu Academy`, was already listed and was dropped as a duplicate.

⚠️ **THE GATE ITSELF FAILED SILENTLY ONCE.** The corpus name set was built by stripping a 2-char
region prefix with `slice(2)` from strings joined by a 1-char separator, so every entry kept a
stray leading character and **nothing could ever match**. It reported "no collisions" on a set that
had two. **Always assert the gate found the collisions you already know about** — seed it with a
known-duplicate name and confirm it fires.

---

## TRAPS THAT HAVE ACTUALLY FIRED

**Place-name collisions across countries — five instances.** Ontario and UK/NZ city names overlap
badly. `kingstonbjj.com` and `kingstonjiujitsu.com` are both real BJJ clubs in **Kingston upon
Thames, England**. `peterboroughjudo.com` is **Peterborough, England** (postcode PE3 8AF).
`resolvebjjacademy.com` is **Cambridge, NEW ZEALAND**. `strongholdjiujitsu.co.uk` likewise.
Everything looks right except the country. **Check the country on every candidate**, especially
London, Hamilton, Cambridge, Kingston, Peterborough, Windsor, Waterloo, Guelph, Whitby.

**A `<City> BJJ` name does NOT mean the record is fake — failed three times as a verdict.**
`Brooklyn Brazilian Jiu Jitsu`, `Binghamton Brazilian Jiu Jitsu`, `Ellsworth BJJ`, `Saco BJJ`,
`Fort Smith BJJ` and `Springdale BJJ` are all real schools. It is a prioritisation signal only.

**Three Ontario stubs were real schools with a broken URL, not fake listings.** `Cambridge BJJ`
stored the `.com` when the school is on the `.ca`. `Windsor BJJ` trades at
windsorbrazilianjiujitsu.com. **`Oshawa BJJ` stored `oshawawbjj.com` — a literal typo, an extra
"w".** Blanking any of them would have been wrong.

**A working link is not evidence the record is right.** Ontario has 8 further `<city> BJJ` records
the screen never flagged *because their links resolve*, and at least two look wrong anyway —
no Guelph school trades as "Guelph BJJ", and Barrie BJJ's real site is 705bjj.com.

**A reachability screen orders work; it never concludes.** The browser no-cors screen had a
**measured 39% false-positive rate** (n=18, with a known-live control) and is structurally blind to
a working link owned by someone else. **DNS-first is the method that works:**
`https://dns.google/resolve?name=<host>&type=A`, `"Status": 3` is NXDOMAIN and conclusive. A blank
body is **not** — record it as unresolved. One batch that skipped DNS returned 70 useless "EMPTY"
verdicts and had to be redone.

**Whole-page byte comparison between two themes can never pass.** Shopify serves each theme's
assets from `/cdn/shop/t/<n>/`, so every page differs on every region. Scope the comparison to the
section's own output (`data-tjjm-statedir` → `</section>`) and excise the region-nav block
separately when `tjjm-region-index` changed. ⚠️ The 6 Aug record's claim of "55 of 61
byte-identical" is not reachable on raw HTML — do not cite it as precedent.

**Some blanked links have findable replacements.** `Four-Eleven Brazilian Jiu Jitsu` was blanked as
dead — correctly, the old domain is gone — but the school is live at fourelevenbjj.ca. Of the 544
links blanked, an unknown fraction are like this. Blanking was the safe action; repointing is the
better one.

**Do not transcribe region contents from memory — read the source file into the brief.** Two errors
this session: the Arkansas stub list was typed as Jonesboro and Hot Springs when the real ones are
Russellville and Springdale, and "AK" was written meaning Arkansas when AK is Alaska.

---

## OPERATIONAL NOTES

- `themePublish` is **blocked** — the user publishes.
- `themeFilesUpsert` is **blocked on MAIN** — always duplicate first, wait ~30 s.
- `fileUpdate` is **situational** — blocked twice this session after succeeding on two prior runs.
  Retry once, then report; do not work around it.
- **The sandbox has no outbound network** (proxy 403s everything). Use `web_fetch` or the browser.
- **`web_fetch` truncates at ~75 KB** — it cannot read `tjjm-gyms.json` (488 KB). Use the browser.
- The JS REPL takes **top-level `await`**; an `(async()=>{})()` IIFE returns `{}`.
- **The output filter blocks query-string/token-like data.** Strip `?...` from any URL you echo.
- Browser page state (`window.__*`) is lost on reload — it happened three times this session.
  Re-derive rather than assume, and keep sweeps self-contained.
- A subagent died mid-write once. **Always re-query file sizes after a failed agent** before
  assuming a write did or did not land.

---

## BACKLOG, ordered

**1. The 28 remaining never-curated regions.** The prize. All three rebuilt regions came in at
roughly **double** their listed count — and that held across a tiny rural region whose links were
100% broken (Maine), a mid-size one whose links were basically healthy (Arkansas), and the largest
(Ontario). Coverage and link rot are independent problems. Plausibly **400–700 more schools**.

Suggested batches, worst ratio first:
~~batch 1: SK, ND, WY, UT~~ **DONE 7 Aug, published as theme EE.**

| batch | regions | listed | flagged |
|---|---|---|---|
| 2 | IA, MB, SD, KS | 48 | 37 |
| 3 | NM, HI, ID, VT, RI | 56 | 40 |
| 4 | MN, SC, MS, NE, NH | 68 | 46 |
| 5 | BC, AB, QC | 69 | 49 |
| 6 | TN, NS, NB, NL, PE, DE, DC, AK | 151 | 40 |

**2. Ontario second harvest.** Toronto reportedly has 100+ academies; only ~8 net-new surfaced.
Never swept: Milton, Newmarket, Aurora, Brantford, Woodstock, Stratford, Chatham-Kent, Timmins,
Cornwall, Brockville, Owen Sound, Kenora, Orangeville, Bradford.

**3. Re-screen all 40 original Ontario records**, not just the 11 stubs — see the "working link"
trap. Same for other rebuilt regions.

**4. The 63 unresolved `EMPTY` links** (55 curated + 8 Ontario). A fetch failure is not evidence
about a school. One body read each.

**5. Repointing pass** over the 544 blanked links, per the Four-Eleven case.

**6. Rebuild `tjjm-gyms.json`.** ⚠️ **The staged upload expired — it must be rebuilt from scratch**,
and it is now ~660 records behind. Procedure and the reason the record ORDER is not reproducible
are in `STEP-11-BLOCKED-recovery.md`. **Lowest priority: nothing is known to consume this file.**

**7. Carried from the NY run, untouched:** backlog item 0c (3 records needing a field no override
reaches), six owed `tjjm-statedir-notes-<code>` files (FL, LA, MO, NJ, TX, NV), item 2b (UFC GYM
Sherwood, one-record add), item 1b-follow-up (Alliance San Diego pair).

**8. Never-imported duplicates (RULES §2 blind spot 1)** — still untouched, still unreachable by
any diff run so far.

---

## WHAT WAS NOT CHECKED

- **No corpus-wide cross-region diff has ever been completed.** `web_fetch`'s 75 KB ceiling blocked
  it. So it is still unknown whether any imported record already exists under another region.
  Specifically unresolved: whether **Savarese BJJ** (suppressed from NY as being in Lyndhurst NJ)
  already exists under NJ — if not, a net-new NJ add is owed.
- **The 96 curated-state links the screen flagged that are live and correct were left alone** —
  correctly. They are not a to-do.
- Ontario's `Hamilton BJJ` vs the listed `Hamilton Brazilian Jiu-Jitsu`: probably one school on two
  domains, unconfirmed because hamiltonbjj.com is a JS shell. Both currently render. Hamilton BJJ
  is actually in **Stoney Creek**.
- The 3 Maine records held back as unverified: Gracie Barra Bangor (aggregator only), GracieFighter
  Presque Isle (one 2022 news piece), Maine Jiu Jitsu Academy Boothbay (JS-only, no address).
- Arkansas records held back as weak: Fort Smith Dark Arts, Omega BJJ, Ru-Jitsu, Spa City, Kokoro,
  Gracie Barra Batesville. Note **Gracie Jiu-Jitsu Springdale's own page says "This club is no
  longer active"** — do not add it.
- Pine Bluff AR, Rumford ME and Waterville ME appear to have **no BJJ school at all**. Suppressed.

---

## FILES IN THIS FOLDER

| file | what it is |
|---|---|
| `RULES-tjjm.md` | durable decision rules + evidence. **Read first.** |
| `NEXT-RUN-brief-regions.md` | this file |
| `ny-step5-verdicts.md` | the NY import, full evidence base and method corrections |
| `region-rebuild-maine.md` | the Maine pilot |
| `region-rebuild-batch1-findings.md` | ME/AR/ON research, the 2x ratio finding |
| `STEP-11-BLOCKED-recovery.md` | Files JSON rebuild procedure |
| `link-audit-flagged.tsv` | all 899 flagged links |
| `batches/verdict-TIER-A-ALL.tsv` | 586 curated-state verdicts |
| `batches/verdict-ON-ALL.tsv` | 89 Ontario verification verdicts |
| `batches/B-stubs-ALL.tsv` | the 174 city-stub records, 165 still unrebuilt |
| `batches/adds-ALL.json` | the 117 records shipped in batch 1 |
| `build_ny.py`, `build_ny_step7.py` | worked build scripts to model new ones on |
| `HANDOFF-next-states.md` | older handoff; backlog items 0c–17 still live there |
