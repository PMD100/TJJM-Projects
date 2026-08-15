# Region rebuild batch 2 — RESEARCH COMPLETE, not yet verified or built.
## Utah, Saskatchewan, North Dakota, Wyoming. 7 Aug 2026.

**Status: phase 1 (research) only.** Phase 2 (verification body-reads) and phase 3 (build) are NOT
done. Nothing has been written to any theme. Do not build from this file without running phase 2 —
in Ontario, ~20% of unverified research rows had a wrong name, city or address, and 3 were in the
wrong country.

---

## Result

| region | listed | net-new found | would become | multiplier |
|---|---|---|---|---|
| **Utah** | 14 | **47** | ~52 | **3.7x** |
| Saskatchewan | 11 | 13 | ~22 | 2.0x |
| North Dakota | 9 | ~6 | ~14 | 1.6x |
| Wyoming | 9 | ~7 | ~15 | 1.7x |
| **batch total** | **43** | **~73** | **~103** | **2.4x** |

Running total across five regions rebuilt or researched (ME, AR, ON, + these four): the directory
consistently carries **roughly half to a third** of the schools that actually exist in a
never-curated region. Utah at 3.7x is the highest yet and it is a populous state — **13 of its 14
current listings are unverifiable or wrong.**

---

## THE BIG FINDING: the screen misses stubs whose domain resolves

This batch surfaced **three more bad records that never got flagged**, because a reachability
screen only asks "does the host answer", not "is this the right school":

| record | region | what the domain actually does |
|---|---|---|
| `Orem BJJ` | UT | **301s to oremkarate.com** = Bobby Lawrence Karate Orem, 976 S State St. A karate school that runs BJJ classes, not a school called "Orem BJJ". |
| `Gillette BJJ` | WY | **301s to westernplainsbrazilianjiujitsu.com** = Western Plains Brazilian Jiu Jitsu, 900 Ez Street, Gillette. Right city, wrong name. |
| `Cody BJJ` | WY | **Resolves to an empty parked Shopify host** (23.227.38.65). No content, no redirect. Real school is Potter Combat Academy, 1713 17th St. |

⚠️ **This means the 899-link audit systematically undercounted.** Ontario had 8 unflagged
`<city> BJJ` records for the same reason. **Every rebuild should re-screen ALL of a region's
records, not just the ones the audit flagged.**

## Typo'd domains — a fourth instance

`Grand Forks BJJ` /ND stores **grandforks`jj`.com** — missing the "b". The real school is
**Grand Forks Brazilian Jiu-jitsu Academy at grandforks`bjj`.com**, 2750 Gateway Dr. Joins
`Oshawa BJJ` (oshawa**w**bjj.com, extra w), `Cambridge BJJ` (.com vs .ca) and
`Prince Albert BJJ` (princealber**t** missing — though there both spellings are NXDOMAIN, so no
live site is hiding behind it). **Always try the obvious typo correction before declaring dead.**

## A possible class of records that were never real

Several listings have names that no school anywhere trades under, in cities that *do* have real
BJJ schools under entirely different names:

- `SLC BJJ Academy` /Salt Lake City — *"no school by that name exists in SLC that I can find under any source; likely fabricated"*
- `Alliance Jiu Jitsu St. George` /UT — no Alliance presence in St. George; Utah's only Alliance is Viotti in Bountiful, 300 mi north
- `Alliance Jiu Jitsu Utah` /SLC — probably a mis-citied reference to that same Bountiful school
- `Alliance Jiu Jitsu Wyoming` /Laramie — Laramie's real school is Third Way Jiu Jitsu, no Alliance affiliation on its site
- `Wyoming Martial Arts` /Jackson — Jackson's real school is Jackson Hole MMA
- `Prairie Jiu Jitsu` /Minot — no first-party trace; Minot's real school is Gracie Jiu-jitsu Minot

**This is a different defect from a stale link or a renamed school.** Worth a corpus-wide look at
records whose name contains an affiliation brand ("Alliance Jiu Jitsu <Place>") that the brand's
own roster does not list.

---

## Per region

### UTAH — 14 listed, 47 net-new
All 9 suspects NXDOMAIN. **8 of 9 cities have a real school** under another name; only **Moab** has
none (the "Grand Valley BJJ" that surfaces is Grand Junction, **Colorado**).
Highlights: Gracie Barra has **10 Utah schools**, only 1 listed. Renzo Gracie SLC, 10th Planet SLC
and Pleasant Grove, Pedro Sauer (Fusion/Unified/Westside), Caique, Carlson Gracie, Caio Terra and
Gracie Humaita all present and all unlisted.
**Not settled:** Cedar City (only city where existence could not be confirmed or refuted —
mixedgrapplingarts.com returns an empty body, KALA/Carlson Gracie Cedar City is Facebook-only);
Estavel BJJ Layton (empty body, shares an address with GB Layton — one may have absorbed the
other); Westside BJJ Ogden (URL found, body not read); Uintah Basin JJ Roosevelt (booking listing
only). `10thplanetwestvalley.com` resolves but its content is entirely the SLC location — **no
separate West Valley school was counted.**

### SASKATCHEWAN — 11 listed, 13 net-new
All 10 suspects NXDOMAIN. **Only 1 of 11 existing records is correct** (Regina BJJ = Regina
Brazilian Jiu-Jitsu, 655 Henderson Dr). 8 of 10 stub cities have a real school under another name.
**Lloydminster belongs to ALBERTA** — the city straddles the border and The Gym 110 MMA's own
contact page says 5201A 63 St, Lloydminster **AB**. Aggregators wrongly place it in SK.
**Swift Current appears to have no BJJ at all** (judo and karate only).
**Not settled:** Melfort (chamber-of-commerce entry only, no business name recoverable); Green Dojo
North Battleford publishes **two conflicting addresses on its own site**; Midwest BJJ / GFTeam
Saskatoon is likely the predecessor of Valens (same coach) — **do not add without confirming, risk
of double-listing one school**; Rolls Academy, Momentum, and Modern Martial Arts Center all teach
BJJ but publish no first-party street address, so were left off rather than padded.
No Saskatchewan affiliate exists for any major network — real affiliations are GFTeam and Infight.

### NORTH DAKOTA — 9 listed, ~6 net-new
5 of 6 suspects NXDOMAIN; `Grand Forks BJJ` is the typo case above. **Mandan has no BJJ school** —
it trains 6 miles away in Bismarck. Fargo BJJ is the only ND listing with a live correct domain.
Net-new: Ice Dragon Academy and Bismarck MMA (Bismarck), Elite BJJ and Carlos Machado JJ
(Dickinson), Academy of Combat Arts (Fargo), Progressive Martial Arts and Gracie Jiu-jitsu Minot.
Several existing records need a **name/URL fix rather than suppression**: Grand Forks, Valley City,
Williston (= SBG Williston).
**Not settled:** Jamestown Academy of MMA (aggregator only); whether `Prairie Jiu Jitsu` ever
existed.

### WYOMING — 9 listed, ~7 net-new
2 of 4 suspects NXDOMAIN, 1 resolves-but-empty (Cody), plus the unflagged Gillette case.
Net-new: D's Jiu-Jitsu (Casper), Black Label BJJ (Cheyenne), Potter Combat (Cody), Duality BJJ
(Green River), Jackson Hole MMA, Third Way Jiu Jitsu (Laramie), **Wind River Dojo in LANDER** —
note Lander, not Riverton. Cheyenne BJJ is correct as listed.
**Not settled:** Riverton (Wyoming Shoot Fighting's own site returns an empty body — Riverton may
have no operating dedicated BJJ school; nearest confirmed is Lander, ~25 mi); Casper may have more
than the one confirmed gym; Sheridan's two gyms (Black Tooth, Grindhouse) have no first-party sites.

---

## Excluded as out-of-region — every one caught by reading the body

Would all have passed a title-only screen:
`gbriverton.com` = Gracie Barra **Riverton UTAH** (surfaced on a Riverton WY search) ·
`kinetixcombat.com` = **Jamestown NEW YORK** · `serafinjiujitsu.com` = **Evanston ILLINOIS** ·
`sheridanbjj.com` = Sheridan/Oakville **ONTARIO** · `scjja.com` = Caringbah **NSW AUSTRALIA** ·
`fcjiujitsu.com` = Newark **NEW JERSEY** · Humboldt Jiu Jitsu = Arcata **CALIFORNIA** ·
SwiftKick MMA = **NASHVILLE** · Grand Valley BJJ = Grand Junction **COLORADO** ·
Fusion MMA Mesquite = **NEVADA** · Vanguard BJJ-Judo and Hadwin School = **ALBERTA**

Eleven out-of-region false positives in four regions. The country/state check is not optional.

---

## NEXT STEPS for this batch

1. **Phase 2 verification** — body-read every net-new candidate, extract name and street address
   from the page. ~73 candidates, so 3–4 agents of ~23. Utah alone is 47.
2. **Re-screen all 43 existing records** in these four regions, not just the 29 stubs — the Orem,
   Gillette and Cody cases prove the audit missed resolving-but-wrong records.
3. **Decide the fix type per existing record**: several want a name/URL correction rather than
   suppression (Grand Forks, Valley City, Williston, Gillette, Rock Springs, Sheridan, Cody).
   A name change is NOT overridable — it needs suppress + re-add, the NY pattern.
4. **Phase 3 build** — remember `tjjm-gym-websites-2` is at 19,998 B of a ~24 KB ceiling, so this
   batch needs a **file 3** plus its render tag.
5. Run the **collision gate** and seed it with a known duplicate to prove it fires.

---

# PHASE 2 COMPLETE — 7 Aug 2026. Verified, not yet built.

All 75 net-new candidates body-read across three agents.

| verdict | n | |
|---|---|---|
| CONFIRMED | 68 | 91% |
| CONFIRMED-NO-ADDR | 4 | Adapt Jiu-Jitsu (Herriman, "opening soon"), Estevan Combat Sports, Weyburn MMA Club, Fusion Academy SLC |
| DEAD | 2 | Estavel BJJ (NXDOMAIN on retry), Uintah Basin Jiu Jitsu (uintahbasinbjj.com NXDOMAIN) |
| EMPTY | 1 | Mixed Grappling Arts, Cedar City — resolves, serves nothing |

**72 importable**, 70 with a street address from the school's own page.
**Zero WRONG-PLACE, zero NOT-BJJ** — markedly cleaner than Ontario (3 wrong-country, ~20% errors).
Importable by region: **UT 45, SK 13, ND 7, WY 7**.

Traps checked and cleared:
- `Bobby Lawrence Karate Orem` has dedicated Kids/Teen/Adult BJJ pages — **stays in**, not cut as karate.
- The two St. George `Fusion MMA` rows are genuinely separate campuses; the site lists three, the
  third being **Mesquite NEVADA**, correctly excluded.
- `Green Dojo` address conflict resolved: the stale header says 9902 20 Ave, but Contact and
  Facilities both say **2202 101st, beside the Ford dealership** — that is current.
- `Alliance Training Center` Saskatoon is a **name collision**, not an Alliance affiliate. Teaches
  BJJ under its own brand. Import under its own name; do not treat as an Alliance school.
- `Wind River Dojo` (Lander WY) confirmed teaching **BJJ specifically** — two BJJ black belts on
  the instructors page — not judo alone.
- `Gracie Jiu-jitsu Minot` confirmed real: the only Gracie CTC in North Dakota.

Artifacts: `batches/verdict-b2-ALL.tsv` (all 75 verdicts), `batches/adds-batch2.json` (the 72).

## STILL TO DO for this batch — phase 3

**Suppression plan, decided but not yet built** (39 of 43 existing records go):
- **UT** suppress 13, keep 1 (Gracie Barra Salt Lake City — the only correct Utah listing)
- **SK** suppress 10, keep 1 (Regina BJJ)
- **ND** suppress 8, keep 1 (Fargo BJJ)
- **WY** suppress 8, keep 1 (Cheyenne BJJ)

**Five records need a NAME change, not a link fix** — names are not overridable, so each is a
suppress-and-re-add. **These five were NOT in the phase-2 verification pass** and need checking
before build:
| current record | should be | url | address |
|---|---|---|---|
| `Grand Forks BJJ` /ND | Grand Forks Brazilian Jiu-jitsu Academy | grandforksbjj.com | 2750 Gateway Dr |
| `Valley City BJJ` /ND | Valley City Jiu-Jitsu and Self Defense Academy | jiujitsuvc.wixsite.com/valley-city-jiujitsu | 200 Co Hwy 21 |
| `Williston BJJ` /ND | SBG Williston | sbgwilliston.com | 1135 2nd Ave W Ste 206 |
| `Gillette BJJ` /WY | Western Plains Brazilian Jiu Jitsu | westernplainsbrazilianjiujitsu.com | 900 Ez Street |
| `Rock Springs BJJ` /WY | Wyo Faction | wyofaction.com | 1248 Dewar Dr ⚠️ aggregator-only address |

**Build notes:** needs `tjjm-gyms-data-38`, a **new `tjjm-gym-websites-3`** (file 2 is at 19,998 B
of ~24 KB), two render tags in the section, removed-index rows for UT SK ND WY, and region-index
updates. Run the collision gate **seeded with a known duplicate to prove it fires.**

---

# PHASE 3 COMPLETE — theme EE built and verified, 7 Aug 2026.

**Theme `Aug 7 BJJ Gyms EE` = `gid://shopify/OnlineStoreTheme/154717487276`. NOT YET PUBLISHED.**

Sweep of all 61 regions, live (DD) vs EE — every assertion exact:

| | live | EE |
|---|---|---|
| records | 4,730 | **4,768** |
| Utah | 14 | **46** |
| Saskatchewan | 11 | **14** |
| North Dakota | 9 | **11** |
| Wyoming | 9 | **10** |

- **77 added** (UT 45, SK 13, ND 10, WY 9), **39 suppressed** (UT 13, SK 10, ND 8, WY 8)
- only those four regions touched
- **0 records lost a link unexpectedly, 0 gained one**

Files: `tjjm-gyms-data-38.liquid` 9,776 B (new) · `tjjm-removed-index` 8,822 → 9,422 ·
section 12,589 → 12,623 · `tjjm-region-index` 3,442 → 3,444. Every write hit its predicted size.
**No `tjjm-gym-websites` change** — all five rename cases became suppress-and-re-add, so no
file 3 was needed after all. File 2 remains at 19,998 B; the NEXT batch that needs an override
will still need a file 3.

## The collision gate fired again — and this time it was proven trustworthy first

Seeded with three names known to exist (`Fargo BJJ`, `Regina BJJ`, `Gracie Barra Salt Lake City`).
All three flagged, so a "no collisions" verdict from it means something. It then found **two real
collisions**:

| new record | collided with | fix |
|---|---|---|
| `Progressive Martial Arts` /Grand Forks ND | an existing record in **Fresh Meadows NY** | renamed `Progressive Martial Arts Grand Forks` |
| `Valens Jiu Jitsu Academy` /Saskatoon SK | an existing record in **Hamilton ON** that carries a **blank override** | renamed `Valens Jiu Jitsu Academy Saskatoon` |

The Valens case is the third instance of the same hazard (after `Jungle Gym Martial Arts` and
`Action & Reaction MMA`): an existing blank override would have silently stripped the new school's
link. **Always seed the gate before trusting it.**

## A stale local mirror nearly caused a regression

While doing the read-modify-writes, the agent diffed each fetched body against the pre-existing
local scratch mirrors and found `scratch/w5-regionindex-NEW.txt` was **stale** — it held
`Ontario|108` and total `4,731`, the pre-correction values. Using it as an edit base would have
silently reverted batch 1's Ontario fix. It has been deleted.
**Rule: always fetch the current body from the theme. Never edit from a local mirror.**
