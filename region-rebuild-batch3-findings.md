# Region rebuild batch 3 — IA, KS, MB, SD

Session of 9–10 Aug 2026. Built as theme **FF** (`154774995116`), verified, and **PUBLISHED**.
SEO metafields set after publish; verified live and cookie-free with `credentials:'omit'` —
on all four regions **title = description = JSON-LD `numberOfItems` = card count = body count**.
No inconsistency window was opened.

---

## Result

| region | was | suppressed | added | now |
|---|---|---|---|---|
| Iowa | 15 | 12 | 33 | **36** |
| Kansas | 13 | 12 | 36 | **37** |
| Manitoba | 11 | 10 | 20 | **21** |
| South Dakota | 9 | 9 | 11 | **11** |
| **total** | **48** | **43** | **100** | **105** |

Corpus **4,768 → 4,825** (net +57). Ratio **2.2x**, in line with every previous rebuild.

South Dakota is the outlier at 1.2x — but that understates the work. Eight of its nine existing
records were junk; the region went from 1 real record to 11.

---

## Verification

Sequential 61-region sweep, concurrency 1, `credentials:'include'`, explicit `preview_theme_id`
on **both** sides, unique cache-buster per fetch, comparison scoped to
`data-tjjm-statedir` → `</section>` with the region-nav block excised.

- total before **4,768**, after **4,825**, delta **+57** — matches prediction exactly
- exactly **4** regions differ, and they are the 4 intended ones
- the other **57** are byte-identical in the scoped section
- on all four changed pages, JSON-LD `numberOfItems` = `.tjjm-gym` card count = body paragraph count
- control run first: IA 15→36 and KS 13→37 under preview, proving the parameter was live before
  any conclusion was drawn from the sweep

Every one of the five file writes hit its predicted byte size exactly, and all five MD5s match
the local sources.

---

## The collision gate caught five real collisions

The gate was **seeded with four known-bad records and one bogus suppression first**, and confirmed
to fire on all five conditions, before its clean result on the real batch was believed. (The brief
records a run where the gate reported "no collisions" on a set that had two.)

| new record | collided with | resolution |
|---|---|---|
| `Ethos BJJ` (Wichita KS) | `Ethos BJJ` (Wilmington NC) — **carries a blank website override** | → `Ethos BJJ Wichita` |
| `Elite Academy of Martial Arts` (Junction City KS) | same name, Stone Mountain GA | → `Elite Academy of Martial Arts Junction City` |
| `Precision MMA` (Morden MB) | same name, Poughkeepsie | → `Precision MMA Morden` |
| `Breaking Point Jiu-Jitsu` (Bettendorf IA) | its own sibling below | → `Breaking Point Jiu-Jitsu Bettendorf` |
| `Breaking Point Jiu-Jitsu` (Davenport IA) | its own sibling above | → `Breaking Point Jiu-Jitsu Davenport` |

**The Ethos case is the dangerous one and is the third instance of this exact defect class.** The
Wilmington NC record carries an *empty* `tjjm-gym-websites-2` override, which blanks a link. Since
overrides match on name alone corpus-wide, a Wichita record sharing that name would have rendered
with **no website at all** — silently, with nothing in the build to indicate it. Identical in shape
to `Action & Reaction MMA` / Laval QC.

---

## ⚠️ Correction to RULES §, and to this brief's own collision section

Both documents state that all three name-keyed mechanisms — `tjjm-removed-index`,
`tjjm-gym-websites`, `tjjm-gym-addresses` — match **"on NAME ALONE, corpus-wide."**

**That is true for the two override files. It is false for `tjjm-removed-index`.**

Read the section source: it loops the removed-index rows, matches `rc == scan_code`, assigns that
one row to `removed`, and `break`s. Suppression therefore only ever applies **within the record's
own region**.

Proved arithmetically as well as by reading the code:

```
5,202 stored records  −  434 region-scoped suppression matches  =  4,768   ← the published total
```

A corpus-wide reading gives 436 and does not reconcile. Two entries only look like corpus-wide
defects and are in fact harmless because of the scoping:

- `IL|Aurora BJJ` also name-matches `Aurora BJJ` in Aurora **MO** — not suppressed, different region
- `WA|Northwest Fighting Arts` also name-matches the Portland **OR** record — not suppressed

This matters for gate condition 4: a suppressed name must appear exactly once **in its own region**,
not once corpus-wide. Under the corpus-wide reading those two entries are false positives that
would send a future run chasing defects that do not exist.

---

## Pre-existing defects found, not fixed

1. **`NJ|JC Projects` is a dead suppression entry** — it matches no record in NJ or anywhere else.
   Suppresses nothing. Harmless, but it is noise in a file that is read for correctness.
2. **`Precision MMA` is filed under `s:"NJ"` with `c:"Poughkeepsie"`.** Poughkeepsie is in New York.
   This is exactly the "name/city contradicting state" class RULES § lists as still-to-scan, and it
   is the first confirmed instance found by accident rather than by a scan.
3. **Four data snippets are not valid JSON.** `tjjm-gyms-data-30`, `-31`, `-32` and `-34` have no
   enclosing `[ ]` and no newlines — they are bare concatenated `}{` objects. They parse fine by
   object boundary and render correctly, but any consumer doing a strict `JSON.parse` will fail on
   these four and succeed on the other 34. Worth normalising before anything is built on top of them.
4. **The researcher's claim that `Fighting Gravity Jiu Jitsu` has "no website on record" was wrong** —
   it stores `fightinggravityjiujitsu.com`. Independently DNS-checked: NXDOMAIN. Link blanked.

---

## Held back — 9 records, not published

Per the Maine/Arkansas precedent. Each has corroborating sources but **no readable page body**.

| region | name | why |
|---|---|---|
| IA | 10th Planet Jiu Jitsu Des Moines (Altoona) | FB/Yelp empty bodies; newest signal 2020 |
| IA | Erebus Jiu Jitsu (Grinnell) | JS-only, empty body on every path |
| KS | Emporia BJJ *(existing record, left in place)* | site resolves but body never says "jiu-jitsu"; no address anywhere |
| KS | Jiu Jitsu Warehouse (Liberal) | only source is a Facebook scraper; may not be BJJ; one listing says "Opening Soon" |
| KS | Louisburg Jiu Jitsu | domain resolves, every path returns an empty body |
| KS | Abilene Jiu Jitsu | `abilenejiujitsu.com` **and** `abilenebjj.com` both NXDOMAIN; research had cited a stale `<title>` |
| MB | WAMMA Swan River | body self-dates "Last updated 28 Jun 2017"; nothing after Mar 2017 |
| MB | AR Training Centre (Brandon) | own site JS-only; the URL on file is a **capoeira** group, wrong entity |
| MB | Top Knotch MMA Fitness (Winnipeg) | **parked domain** on Above.com/Trellian; returns 200, passes any reachability screen |

`Swan River BJJ` and `Fighting Gravity Jiu Jitsu` were therefore **kept listed with their links
blanked**, rather than suppressed — the schools are probably real, only the domains are dead.

---

## Method notes worth carrying forward

**The verification pass earned its keep again, harder than expected.** 108 candidates were checked;
**31 were corrected and 9 could not be verified — a 29% defect rate in research output**, above the
~20% the brief predicted from Ontario. One verifier's own batch ran at 48%. Research output is
provisional. It is not close to publishable.

**`<city>bjj.com` is a dead domain family.** Of 27 stubs, 24 were NXDOMAIN. But — consistent with
the Oshawa precedent — **15 of them were real schools trading under a different name**, not dead
listings. Only 9 were genuinely gone. Blanking them all would have been wrong 15 times.

**Rule 4 fired hard in Kansas.** Two of the three KS records whose links *resolved* were bad anyway:
`kansasbjj.com` is a GoDaddy for-sale page, `midwesttrainingcenter.com` is a Squarespace
placeholder. A working link remains no evidence at all.

**Two more wrong-country records found already in the corpus**, both live before this run:
`Red River BJJ` filed under Manitoba is in **Wichita Falls, Texas**; `Huron BJJ` filed under South
Dakota is in **Goderich, Ontario**. Both suppressed. That makes seven instances of this class.

**The typo hypothesis did not pay out this time.** `flinflobbjj.com` looked like a certain
transposition of `flinflonbjj.com` — both are NXDOMAIN. But the school is real and operating, as
WAMMA Flin Flon. Checking the typo was still right; the school just lives elsewhere.

**WAMMA is the spine of rural Manitoba BJJ.** Five of the eight MB stubs resolved to WAMMA
affiliates. When a region is rural and thinly covered, find the network before searching city by city.

---

## Owed from this batch

1. **The 9 held-back records above** — one readable body each would clear most of them.
2. **Garden City and Leavenworth, KS** — suppressed with no replacement found. The researcher flagged
   both as the verdicts most wanting a second pass.
3. **`Alliance Jiu Jitsu Lawrence`** — suppressed on absence of evidence. No Alliance affiliate found
   in Lawrence, but nothing positively disproves it.
4. **Elite Edge Gym** has seven Iowa sites; only Ankeny was listed, because it is unclear which run
   mat classes. Its own site also contradicts itself on the Ankeny address.
5. **Mason City may be one school or two** — Tsunami Flow Jiu Jitsu and The Flow Institute share a
   coach and a name root. Both listed.
6. **Two net-new KS leads surfaced too late to verify**: Northwest KS Jiu Jitsu **Goodland**
   (602 Caldwell Ave) and **Colby** (1035 Taylor Ave), both read out of the Hays page body.
7. **Missouri owes 9 records.** The KS research found and correctly excluded nine Kansas City **MO**
   schools. MO is a curated state at 98 records; these may or may not already be in it. Worth a diff.
