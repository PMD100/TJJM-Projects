# Region rebuild batch 4 — NM, HI, ID, VT, RI

Session of 10–12 Aug 2026. Built as theme **GG** (`154856816812`), verified, **PUBLISHED**.
Metafields set after publish and verified live cookie-free with `credentials:'omit'` — on all five
regions **title = description = JSON-LD `numberOfItems` = card count = body count**.

---

## Result

| region | was | suppressed | added | now |
|---|---|---|---|---|
| New Mexico | 12 | 12 | 34 | **34** |
| Hawaii | 11 | 11 | 38 | **38** |
| Idaho | 11 | 9 | 43 | **45** |
| Vermont | 11 | 9 | 10 | **12** |
| Rhode Island | 11 | 10 | 22 | **23** |
| **total** | **56** | **46** | **142** | **152** |

Corpus **4,825 → 4,921** (net +96). Ratio **2.7x**.

Idaho was the standout: 11 → 45, roughly **4x**. The Boise metro alone went from 4 records to 21
across Boise, Garden City, Meridian, Eagle, Kuna, Nampa, Caldwell and Star. Gracie Barra had five
Idaho schools and the directory carried none.

## Verification

Sequential 61-region sweep, concurrency 1, `credentials:'include'`, explicit `preview_theme_id` on
both sides, unique cache-buster, scoped to `data-tjjm-statedir` → `</section>` with the region-nav
excised. Control run first (VT 11→12, ID 11→45 under preview) before any conclusion was drawn.

- total 4,825 → 4,921, delta **+96**, exactly as predicted
- exactly **5** regions differ; the other **56** are byte-identical
- all seven theme files verified by **MD5**, not merely by length

---

## ⚠️ NEW GATE CONDITION — C6

**A name that is suppressed in a region must not also be ADDED in that same region.**

Suppression is region-scoped and matches on name alone within the region, so suppressing `X` in
region `R` and adding a new record named `X` in `R` suppresses the new record too. It would have
rendered **nothing at all**, silently, with no error anywhere in the build.

**Five records hit this**: `Alliance Jiu Jitsu Twin Falls` (ID), `Vermont BJJ` (VT), `Cortes BJJ`,
`Coventry Brazilian Jiu Jitsu` and `Providence BJJ` (RI). All five were "existing record, corrected
by verification" cases — exactly the shape that invites suppress-and-re-add.

They were converted to **in-place corrections via overrides** instead: website fixes into
`tjjm-gym-websites-2`, addresses into `tjjm-gym-addresses`. No suppression, no re-add.

The gate now has six conditions and was seeded and confirmed to fire on all six before its clean
result was believed.

## Other collisions caught

Three disambiguating renames, all C1/C2:

- `Vital Brothers Brazilian Jiu Jitsu` (Mountain Home ID) collided with a North Miami FL record
  → `Vital Brothers Brazilian Jiu Jitsu Mountain Home`
- `Sindalu Brazilian Jiu-Jitsu` appeared twice in the batch (Albuquerque and Portales, one brand,
  one website) → suffixed with each city

---

## The identity pass — and three errors it caught

Eight stored records could not be matched to a research row, because the researchers wrote the
schools' **corrected** names rather than the stored stub names. Publishing on that basis would have
double-listed schools. A dedicated identity pass resolved all eight, and **refuted three earlier
matches**:

| stored record | earlier claim | actual |
|---|---|---|
| `Meridian BJJ Idaho` | matched to Team Rhino | **refuted** — inference only, no body support |
| `Authentic BJJ Idaho` | matched to West Idaho BJJ | **refuted** — the match came from a **meta-description**, which METHOD-RULES explicitly forbids |
| `Middletown BJJ RI` | matched to Two Swords | **refuted** — no body citation |

Confirmed by body read: `Idaho Falls BJJ` → SOMA Idaho Falls, `Rexburg BJJ` → SOMA Rexburg,
`Gracie Vermont` → Gracie Jiu Jitsu Vermont (Essex Junction, not Montpelier), and
`Mission First BJJ` (Newport) → Mission First Jiu-Jitsu (Middletown). The Middletown/Newport tangle
was **three entries representing one school**.

`Two Swords BJJ` remains UNRESOLVED. Its old domain `2swordsjiujitsu.com` now serves **scraped
recipe content** on an AFRINIC-allocated IP — a working link owned by someone else. `research-RI.tsv`
still publishes that URL and it must never be shipped.

---

## Traps that fired

**Wrong entity behind a working link, again.** Idaho's `Elite Jiu-Jitsu Academy` pointed at
`elitejiujitsu.com`, which resolves perfectly and serves a school at **280 East Main Street, Newark,
DELAWARE**. The real Elite Jiu-Jitsu Academy is at `idahobjj.com` and is in **Pocatello**, not Boise.
Wrong on two axes at once.

**Burlington, again — the fourth time.** Vermont's `Burlington Brazilian Jiu Jitsu` redirects to
`burlingtonbjj.ca`: Tristar Burlington, **1167 Pettit Road, Burlington ONTARIO**. Two further
Burlington Ontario schools surfaced during the same search.

**Two phantom records in Hawaii.** `Fighting Arts Academy Hawaii` (city stored as "Maui", an island)
does not exist anywhere in the state. `Hawaii Academy of Brazilian Jiu-Jitsu` is an **alias domain**
of Gracie Technics resolving to the same IP — a duplicate, not a school. `Purebred Jiu-Jitsu` is a
Japan/Guam network with no Honolulu location.

**Non-BJJ schools, the Hawaii problem.** Hawaii is the birthplace of Danzan-Ryu jujitsu and
Kajukenbo. A dozen schools were correctly rejected for teaching Danzan-Ryu, Kodenkan, Kajukenbo,
Kenpo, Aikido or TKD rather than BJJ. Vermont's `Green Mountain BJJ` teaches only Krabi Krabong,
Kali, Thai Boxing and Filipino Dirty Boxing — MatMade files it as a BJJ gym; it is not one.

**`Jackson-Wink MMA` suppressed.** New Mexico's most famous gym, but across home, programs and
schedule the words jiu-jitsu, BJJ, gi, no-gi, grappling and open mat appear **zero times**; the
roster is MMA plus a wrestling club. Albuquerque still gains 10 verified BJJ records.

**Wrong-city errors were unusually common** — a new defect class. Filed under Boise but in Pocatello;
Burlington but in Williston; Montpelier but in Berlin; Newport but in Middletown; Providence but in
North Providence; St. Johnsbury but in Lyndonville; Sandpoint but in Kootenai; Coeur d'Alene but in
Dalton Gardens. Check the city as carefully as the state.

**Defect rate 33%** — 37 corrections, 15 unverifiable, 2 rejections out of 164. Above batch 3's 29%.
Two sub-batches ran at 41%.

---

## Deferred, and why

**The 113 KB legacy blob was not rewritten.** `themeFilesUpsert` has no streaming or file-handle
path — the only way in is to type the entire body into a mutation argument. For a dense single-line
JSON array of 1,304 records that is ~65k tokens of transcription with no redundancy to catch a
dropped record. The `URL` body type exists but the sandbox has no network egress, so the bytes
cannot be staged anywhere Shopify could fetch them.

Two intended fixes are therefore **still owed**:

1. **`Vermont BJJ` city is wrong** — the record says Burlington; the school is at 55 Leroy Road,
   **Williston**. Its address override was deliberately *removed* rather than kept, because the
   section builds its map link as `{{ g_addr }}, {{ g_city }}, {{ code }}` — keeping it would have
   produced the malformed query "55 Leroy Road, Williston, VT 05495, Burlington, VT".
2. **`Precision MMA`** is stored as `c:"Poughkeepsie", s:"NJ"`. Poughkeepsie is in New York.

⚠️ **Correction to `corpus-checks-2026-08-10.md`:** that file calls the Precision MMA defect live.
**It is not.** The record is *already suppressed* in the NJ removed-index row, so it renders nowhere.
This also explains why the gazetteer scan missed it — the record was filtered out as suppressed, not
absent from the list. It was deliberately not resurrected: someone suppressed it for a reason nobody
has recovered.

**To land the blob edits, a route that streams bytes from disk is needed** — Shopify CLI
(`shopify theme push --only snippets/tjjm-gyms-data.liquid`) or the Assets REST endpoint from a
machine with both the file and network access.

---

## Held back — 15 records, not published

The shared **WebSearch budget hit its session cap (200/200)** partway through Phase 2, and several
verifiers said explicitly that this, not the evidence, was why they could not close their rows. The
holdback list is therefore larger than batch 3's and unusually likely to clear on a re-run.

| region | name | why |
|---|---|---|
| NM | Cavern City BJJ (Carlsbad) | no site; search unavailable |
| NM | Three Crosses BJJ (Las Cruces) | one source only |
| NM | Soria Martial Arts Club (Artesia) | no source retrievable |
| NM | Gracie Barra Los Lunas | GB's own index returns empty for this school; page removed in 2024 |
| HI | Hawaii Jiu Jitsu Academy (Kailua-Kona) | location solid, **BJJ unproven** |
| HI | Alliance Jiu-Jitsu Hawaii (Waipahu) | JS-only, empty body |
| HI | Egan Inoue Jiu Jitsu (Honolulu) | domain now an expired-domain park |
| ID | Sidekicks MMA / Snake River JJ (Nampa) | no page mentions jiu jitsu at all |
| VT | Montpelier BJJ *(existing, kept)* | JS-only, body unreadable |
| VT | Northeast Kingdom BJJ *(existing, kept)* | `nekjiujitsu.com` now serves a **Sarasota, Florida** school |
| VT | Team Jucao Vermont BJJ (Londonderry) | empty body, one source |
| VT | United Fighting Arts Institute (S. Burlington) | no website; all domains dead |
| RI | Two Swords BJJ *(existing, kept)* | old domain serves recipe spam |
| RI | Bristol BJJ *(existing, kept)* | `bttbristol.com` has **zero Wayback snapshots ever** |
| RI | Brausa Carlson Gracie (Westerly) | all four candidate domains NXDOMAIN |

---

## Owed from this batch

1. **The 15 held-back records** — most should clear with working search.
2. **The two legacy-blob fixes** (Vermont BJJ city, Precision MMA state).
3. **Massachusetts may owe 6 records** — the RI research found and correctly excluded Danny Savery
   (Somerset, Fairhaven) and Terrinha BJJ (Milford, Hopedale, Lowell, Nantucket). MA is curated at
   140; diff them.
4. **Missouri may owe 6** — carried from the corpus checks, still unverified.
5. **Net-new leads found in passing**, not yet verified: Alliance Jiu Jitsu East Boise
   (880 S Vista Ave), Northwest KS Jiu Jitsu Goodland and Colby, Rutland American JJ's Middlebury
   second location.
6. **Amend `research-ID.tsv` and `research-RI.tsv`** — they still carry the three refuted identity
   claims as `ALREADY-IN`, and research-RI publishes the recipe-spam URL for Two Swords.
7. **Sites contradicting themselves** — worth a pass: Alliance Eagle prints an invalid ZIP 83161 and
   the wrong city in its footer; The PIT Idaho prints 93709 (not an Idaho ZIP); Gracie Barra Meridian
   gives two different addresses; `graciebarra.com/boise-id` prints a Boise ZIP for a Garden City
   street.
