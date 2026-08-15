# Region rebuild batch 5 — MN, SC, MS, NE, NH

Session of 12 Aug 2026. Built as theme **HH** (`154860028076`), verified, **PUBLISHED**.
Metafields set after publish and verified live cookie-free — on all five regions
**title = description = JSON-LD `numberOfItems` = card count = body count**.

---

## Result

| region | was | suppressed | added | now |
|---|---|---|---|---|
| Minnesota | 18 | 15 | 49 | **52** |
| South Carolina | 14 | 10 | 30 | **34** |
| Mississippi | 14 | 13 | 26 | **27** |
| Nebraska | 12 | 12 | 21 | **21** |
| New Hampshire | 10 | 7 | 30 | **33** |
| **total** | **68** | **57** | **156** | **171** |

Corpus **4,921 → 5,020** (net +99). Ratio **2.5x**. Five records were handled as in-place override
fixes rather than suppress-and-re-add, so they appear in neither column.

New Hampshire came in at **3.3x** and Minnesota at **2.9x**. Mississippi lost 13 of its 14 existing
records — not one survived verification intact.

## Verification

Sequential 61-region sweep, control first, `credentials:'include'`, explicit `preview_theme_id` on
both sides, scoped comparison with the region-nav excised.

- total 4,921 → 5,020, delta **+99**, exactly as predicted
- exactly **5** regions differ; the other **56** byte-identical
- all six theme files verified by **MD5**
- **Newfoundland verified at 15 before and after, and again live cookie-free** (see below)

---

## ⚠️ NEW GATE CONDITION — C7, the Nebraska/Newfoundland collision

**Newfoundland records are stored under Nebraska's region code (`s:"NE"`) and separated only by a
city list inside the section.** Critically, the section computes `scan_code = 'NE'` when rendering
the Newfoundland page — so **both pages load the same `NE` row of `tjjm-removed-index`**, and the
suppression check runs *before* the city split.

Batch 5 created the **first ever NE suppression row**. Any Nebraska suppression whose name matched a
Newfoundland school would have silently deleted that school from the Newfoundland page. Newfoundland
holds several generic names — `Corner Brook BJJ`, `Gander BJJ`, `Labrador City BJJ`, `St. John's BJJ` —
exactly the shape Nebraska's stubs also take.

C7 has two halves:
- **C7a** — no new Nebraska record may use a city in `nl_cities` (it would surface on the
  Newfoundland page)
- **C7b** — no Nebraska suppression may match a Newfoundland record name

Both were seeded and confirmed to fire before the clean result was believed. Neither triggered on the
real batch, and Newfoundland was independently confirmed at 15 records under preview and again live.

**The gate now has seven conditions.**

## C6 fired five more times

Same class as batch 4 — suppress-and-re-add in one region renders **nothing**. Converted to in-place
override fixes: `Bemidji BJJ` (MN), `Aiken Jiu-Jitsu`, `Alliance Jiu Jitsu Anderson`,
`Alliance Jiu Jitsu Easley`, `Rock Hill BJJ` (SC).

`Alliance Jiu Jitsu Easley` carried a **blank** website override, so it needed its existing entry
*edited* rather than a duplicate appended — the fourth instance of the silent-blanking class.

Two of the five needed **no website override at all** (stored URL already correct). Per RULES, an
entry that restates a value pins it as a second source of truth, so those were skipped.

Two further collisions: `MKG Martial Arts` (new, Minneapolis) against an existing Ferndale **MI**
record → renamed `MKG Martial Arts Minneapolis`.

---

## The worst link rot yet

**Five Mississippi records had resolving links serving entirely different businesses:**

| stored record | what the domain actually serves |
|---|---|
| `Meridian BJJ` | a school in **Culverhouse Cross, Cardiff, WALES** |
| `Oxford BJJ` | Jiu-Jitsu Republic, **Oxfordshire, ENGLAND** |
| `Delta BJJ` | **Culver City, California** |
| `Coast BJJ` | Coast Jiu-Jitsu, **Myrtle Beach, South Carolina** |
| `Laurel BJJ` | 2nd Gear BJJ, **Laurel, MARYLAND** |

Plus, elsewhere in the batch: `fremontbjj.com` → Fremont **California**; `kearneybjj.com` →
Pleasant Valley **Missouri**; `claremontbjj.com` → Claremont **California**; `concordbjj.com` →
Harrisburg **North Carolina**; `florencebjj.com` → Florence **Alabama**; and a
"Lincoln Grappling Coalition" ranking top for Lincoln NE that is in **Lincoln, ENGLAND**.

**Every one of these passes a reachability screen.** The count of wrong-country/wrong-state records
found in the corpus is now well into double figures.

## Aggregators actively fabricating data

**MatMade appears to have invented a school.** `Northeast Jiu-Jitsu Academy`, Manchester NH — MatMade
is the sole source and no other source finds any business of that name in Manchester. The only
martial arts addresses on that street are a different gym (listed CLOSED) and a karate studio.

MatMade also filed Rochester **Indiana** under Rochester NH, Portsmouth **Virginia** under Portsmouth
NH, and Exeter **England** under Exeter NH. Twelve NH rows rested on MatMade alone and were flagged.

**`fightworksacademy.com` publishes ~15 South Carolina city landing pages** — Aiken, Sumter, Camden,
Orangeburg, Newberry, Greenwood, Clemson, Florence and more — that are all SEO doorways for a single
Greenville gym. Any directory built naively off that site over-counts South Carolina badly.

## Title tags lying about the discipline

Two schools advertise BJJ in the `<title>` while the rendered body sells something else entirely:
`Manchester Gracie Jiu Jitsu` is **Manchester Karate Studio** (whole syllabus is karate), and
`Nebraska Academy of Martial Arts` prices exactly one programme — **TaeKwonDo, $79 for 5 weeks**.
Four records were rejected as not-BJJ in total, including a judo-only school in Ladson SC whose
schedule lists only Junior Judo and Adult Judo.

---

## Other findings

**`Roufusport MMA Academy` was filed under Minneapolis and is a Milwaukee, Wisconsin brand.** Its own
worldwide affiliate roster lists 15 locations across 12 regions and **zero** in Minnesota.

**Moorhead MN dropped to zero.** Both its records were wrong: `Fargo BJJ MN side` is a Fargo **North
Dakota** school, and `moorheadbjj.com` is NXDOMAIN with no Moorhead academy under any name.

**Norfolk NE dropped to zero.** Both `Norfolk BJJ` and `Norfolk NE BJJ` are the same phantom — the
town's three martial arts schools teach Taekwondo, Hapkido, Gumdo and Kenpo, no BJJ.

**Jackson, Mississippi — the state capital — had no record at all.** Eight academies exist in the
metro, none of them listed.

**Defect rate 34%** — 32 corrections, 4 rejections, 29 unverifiable out of 194.

---

## Held back — 29 records

Larger than batch 4's 15. The shared **WebSearch budget hit its session cap again** during wave 2;
agents compensated with direct fetches and DNS, but several rows needed a search to close. Most of
the 29 are JS-only sites returning empty bodies rather than doubtful schools.

Notable among them:
- **`Gracie United Picayune` (MS)** — the network's own roster lists only Diamondhead, Hancock,
  Hattiesburg and Wiggins. **No Picayune.** Zero primary evidence for this record.
- **`Ogallala Brazilian Jiu Jitsu` (NE)** — recommend **drop**; the venue's own pages list no
  martial arts programme at all.
- **`Checkmate Martial Arts` (NH)**, **`Gracie Barra Charleston` (SC)**, **`Akagi Jiu-Jitsu` (MN)** —
  live domains, entirely empty bodies. Need a browser render, not another fetch.

## Owed from this batch

1. **The 29 held-back records** — most would clear with working search or a browser render.
2. **Three unresolved identity questions**, kept unchanged rather than guessed:
   `TC Martial Arts` (St. Paul — research found no business of that name),
   `Winona BJJ` (MN), `Seacoast BJJ NH` (Portsmouth — verification returned an empty body).
3. **North Dakota may owe 2**: Fargo Brazilian Jiu-Jitsu Academy and Academy of Combat Arts, both
   Fargo ND, both surfaced during the Minnesota sweep.
4. **Wisconsin may owe 2**: Flow Jiu-Jitsu La Crosse and the Roufusport Sheboygan/Green Bay affiliates.
5. **Maine may owe 1**: **Port City BJJ has left New Hampshire** — its own site now reads
   "NEW LOCATION! 280 Route 1, Kittery ME 03904".
6. **NC, GA, TX, TN, MO, IA may owe records** surfaced and correctly excluded during this batch —
   Lucas Lepri Charlotte, Frontline/North Augusta GA, Soul Fighters Georgetown TX, Jackson
   Brazilian Jiu-Jitsu Academy TN, Cast Iron BJJ MO, One Combat Academy Sioux City IA.
7. **Louisiana brand diff owed** — Gracie United reportedly has ~21 Louisiana locations; LA is
   curated at 100.
8. **Net-new leads found in passing**: Renzo Gracie's third NH academy (590 Second Street,
   Manchester), Gracie United Diamondhead MS, MKG Edina MN, Alliance East Boise (carried from batch 4).
