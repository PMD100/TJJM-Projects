# Region rebuild batch 6 — WV, AB (6a) and BC, QC (6b)

Session of 12 Aug 2026. Split into two shippable halves because the research pass returned 302
candidates — far more than any previous batch.

- **6a** = theme **II** (`154862780588`) — WV, AB. Published.
- **6b** = theme **JJ** (`154865860780`) — BC, QC. Published.

Metafields set after each publish and verified live cookie-free: **title = description = JSON-LD
`numberOfItems` = card count = body count** on all four regions. Region-nav sums to 5,205.

---

## Result

| region | was | suppressed | added | now |
|---|---|---|---|---|
| West Virginia | 10 | 10 | 28 | **28** |
| Alberta | 22 | 15 | 65 | **72** |
| British Columbia | 26 | 24 | 99 | **101** |
| Quebec | 21 | 10 | 52 | **63** |
| **total** | **79** | **59** | **244** | **264** |

Corpus **5,020 → 5,205** (net +185). Ratio **3.3x** — the highest of any batch.

British Columbia went **3.9x** and Alberta **3.3x**. Metro Vancouver went from ~8 records to ~50;
Edmonton from 2 to 23; Calgary from 6 to 25.

---

## ⚠️ THE DEFECT RATE KEEPS CLIMBING

| batch | defect rate |
|---|---|
| 3 (IA KS MB SD) | 29% |
| 4 (NM HI ID VT RI) | 33% |
| 5 (MN SC MS NE NH) | 34% |
| **6a (WV AB)** | **46%** |
| **6b (BC QC)** | **84%** |

6b's worst sub-batch had **2 of 24 rows survive untouched**. Much of 6b is missing-field enrichment
rather than wrong entities — but 20 records were rejected outright as not-BJJ, and the pattern is
clear: **the larger and less-curated the region, the worse the research output.**

### A research agent fabricated evidence

A verifier found the research pass had attributed **"Prof. Jay Zeballos, 3rd degree black belt under
Jean Jacques Machado"** to a school whose page body contains no such text. The attribution was
invented, not merely mis-sourced.

Wave 2 of 6b was given an explicit instruction: *do not carry forward any lineage, instructor or
affiliation claim you have not read yourself.* Every wave-2 agent confirmed compliance and several
independently caught further mismatches (e.g. GB Cloverdale's owner is Prof. Andar Lin on the body,
not the "Prof. Eddy Jovel" researched).

**This should become a permanent METHOD-RULES clause.** The existing rules cover trusting the wrong
*source*; they did not anticipate an agent inventing a source.

### Alberta's researcher ran out of context and said so

It flagged ~30 rows "body not individually read - lower confidence". Verifiers opened nearly all of
them; one reported **4 of 6** such rows were defective. The honesty was useful — the flag was a
genuine defect signal, not noise. Worth encouraging explicitly in future research prompts.

---

## The write that half-landed

The 6b write agent was terminated mid-job by an API error (the machine slept). **Four of six files
had landed; `tjjm-gyms-data-43.liquid` was missing entirely and `tjjm-gym-websites-2.liquid` still
held the 6a version.**

The project's own rule — *always re-query file sizes after a failed agent* — caught it. Had it gone
unchecked and been published, `sections/tjjm-state-directory.liquid` would have referenced a snippet
that did not exist. A second agent wrote the two remaining files; all six then MD5-verified.

---

## Gate results

Seven conditions, seeded and confirmed firing before every run.

**6a — 5 collisions:** `Dynamic MMA` (new Calgary vs existing Roseburg OR); `Ironside Martial Arts`
(new St. Albert vs **Bedford TX carrying a blank override** — the fifth silent-blanking instance);
plus three C6 cases converted to in-place override fixes (`Elite Martial Arts Calgary`,
`YYC Brazilian Jiu Jitsu`, `Phoenix Martial Arts Club`).

**6b — 11 collisions:** three C6 in-place conversions (`Lions MMA`, `Van Isle BJJ`,
`Alliance Jiu Jitsu Montreal` — the latter two needed **blank overrides edited**, not appended);
three renames (`Elite Jiu Jitsu` vs Livonia MI, `Delta BJJ` vs Biloxi MS,
`Pinnacle Martial Arts Academy` vs Monroe LA).

### A new check: C8, city-spelling folding
Quebec introduced **18 new city strings**. Because the section groups by exact city string, a variant
spelling would silently create a second heading for the same place. A fold-to-ASCII comparison
confirmed every new string is a genuinely distinct place, and the live page renders **30 Quebec city
headings with zero mojibake** — `Lévis`, `Rosemère`, `Saint-Jérôme`, `Sept-Îles`, `Trois-Rivières`
all correct.

---

## Records filed in the wrong province or country — nine this batch

| stored as | actually |
|---|---|
| `Wise Warrior Gym` — Langley **BC** | Edmonton, **ALBERTA** (and not BJJ — a ClickFunnels self-defence seminar) |
| `Poderoso Jiu Jitsu` — Abbotsford **BC** | Montréal, **QUEBEC** |
| `Angry Monkey MMA` — Calgary **AB** | Verdun, Montreal, **QUEBEC** |
| `Brooks BJJ` — Brooks **AB** | Dungannon, **NORTHERN IRELAND** |
| `Clarksburg BJJ` — **WV** | Clarksburg, **MARYLAND** |
| `Nitro BJJ` — **WV** | Altus BJJ, Brewster, **NEW YORK** |
| `Santos Brothers BJJ Montreal` — **QC** | Toronto, **ONTARIO** |
| `Action & Reaction MMA` — Laval **QC** | North York, **ONTARIO** |
| `Fearless MMA` — Laval **QC** | Aurora, **ONTARIO** |

Also caught before filing: `SBG Vancouver` is **Vancouver WASHINGTON**; `princetonbjj.com` is
Princeton **NEW JERSEY**; `Lincoln Grappling Coalition` (from batch 5) is Lincoln **ENGLAND**.

**`Action & Reaction MMA` is notable** — it is the record whose blank override caused the Pickering
collision back in batch 1. It turns out not to be a Quebec school at all.

---

## Twenty not-BJJ rejections

The largest cull yet. Rejected for teaching something else entirely: **Morganti Ju-Jitsu**
(Power3 Academy), **Can-Ryu** (Faulks), **Sogobudo Jujutsu** (Académie Martiale Laval),
**Goshinkan** (Edmonton Jujitsu), judo-only (Praxis — its stated venue is a judo club),
catch wrestling (FKP MMA), kickboxing-only (Victoria Martial Arts, Martial Arts Unlimited,
Richmond Martial Arts, Personal Best), Kung-Fu (Patenaude Gatineau), and a **bouldering gym with a
café and pizzeria** (Klimat). One — Posener's Pankration — says on its own page that it *stopped*
offering no-gi and refers students elsewhere.

Plus kids-only BJJ at TKD schools (Bowman's, Tsawwassen) and title-tag lies where the BJJ claim
existed only in meta tags.

---

## Other findings

**Arashi-Do had 18 Alberta locations and the directory listed none.** Its own BJJ programme page
names 18 of 19 sites. That single roster opened up Penhold, Olds, Edson, Hinton, Sylvan Lake and Leduc.

**`Parkersburg BJJ` is Parkersburg Martial Arts Center — in Vienna, not Parkersburg.** Wrong name and
wrong city. Fixed by suppress-plus-add, since the legacy blob remains unwritable.

**`West Virginia BJJ` was filed under Morgantown** but its domain redirects to a **Lewisburg** school
(Stellar Jiu Jitsu). Morgantown actually has four academies, none of them listed.

**Charleston, the WV state capital, had no record.** It has five schools in the Kanawha–Putnam corridor.

**`grandeprairebjj.com` was NOT a recoverable typo** — unlike the Oshawa case, the corrected spelling
`grandeprairiebjj.com` is also NXDOMAIN. Grande Prairie has BJJ under other names.

**`Method BJJ` (Edmonton) closed 26 Nov 2025** — its site is still live and directories still list it.
Only reading the body catches this.

---

## Held back — 32 records (9 from 6a, 23 from 6b)

Mostly JS-only sites returning empty bodies, plus rows resting on a single non-independent source.
Notable:
- **`Ultraforce MMA`, `Deep Cove BJJ`, `West Coast BJJ`** — all rest solely on `westcoastbjj.ca`'s
  affiliate list, a page copyrighted **2014**. Recommend deletion rather than holding.
- **`Eke Academy`** (Victoria) — the fabricated-lineage row; strongest candidate for a not-BJJ reject.
- **`KTB Brazilian Jiujitsu Academy`** — probably **New Westminster**, not Vancouver as stored.
- **`Definitive Jiu-Jitsu`** — probably **North Vancouver**, not Vancouver.
- **`Sept-Iles BJJ`**, **`Levis BJJ`**, **`Tomari Martial Arts`** — no evidence the entity exists.

## Owed from this batch

1. The 32 held-back records.
2. **Cross-region debts**: Washington (SBG Vancouver WA), Ontario (Santos Brothers, Action & Reaction,
   Fearless MMA, Therien, Ottawa Jiu Jitsu, several Marcus Soares affiliates), Maryland (MMA & Sport
   Damascus), Ohio (Steubenville BJJ), New York (Altus Brewster), Virginia (Bluefield VA),
   North Dakota (Fargo BJJ, Academy of Combat Arts), Wisconsin (Flow La Crosse, Roufusport affiliates).
3. **Montreal second harvest** — the QC researcher held back ~20–25 aggregator-only Montreal
   candidates rather than launder them. A disciplined call, and a high-yield follow-up.
4. **NET-NEW leads seen in bodies**: Champion's Creed South and Bravé South Edmonton; Bairro Central
   and South; Renzo Gracie's third NH academy; Nomad Coaticook QC; Alliance Rosemère and
   Saint-Eustache; Affinity Varsity; MKG Edina.
5. **`Gracie Barra West Vancouver`'s site is a recycled California template** — banner reads
   "CLASSES IN WALNUT CREEK ARE ON!" and the instructor card contradicts the roster. Instructor data
   from that page is unreliable.
