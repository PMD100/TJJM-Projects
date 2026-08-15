# Region rebuild batch 7 — TN, NS, NB, NL, PE, DE, DC, AK

Session of 13 Aug 2026. The last never-curated batch. Built as theme **KK**
(`154881523884`), staged and swept, **awaiting publish** (`themePublish` is blocked).

Eight small regions rather than one or two large ones, which changed the character of the
work: the dominant failure mode was not link rot but **wrong region**, and the dominant
constraint was not research effort but a **tooling limit** (see "The Facebook wall").

---

## Result

| region | was | suppressed | added | now | ratio |
|---|---|---|---|---|---|
| Tennessee | 34 | 5 | 23 | **52** | 1.53x |
| Nova Scotia | 23 | 5 | 11 | **29** | 1.26x |
| Delaware | 7 | 7 | 8 | **8** | 1.14x |
| New Brunswick | 15 | 5 | 5 | **15** | 1.00x |
| Prince Edward Island | 10 | 3 | 3 | **10** | 1.00x |
| Newfoundland | 15 | 3 | 1 | **13** | 0.87x |
| Washington DC | 7 | 4 | 3 | **6** | 0.86x |
| Alaska | 22 | 10 | 2 | **14** | 0.64x |
| **total** | **133** | **42** | **56** | **147** | **1.11x** |

Corpus **5,205 → 5,219** (net +14). Stored 5,841 → 5,897, suppressions 636 → 678.
Nebraska held at 21 on both sides, as required.

**1.11x is by far the lowest ratio of any batch** (batch 6 was 3.3x) and three regions
shrank. The suppression rate of **32%** is the highest yet. Both facts are mostly real —
see below — but partly an artifact of the Facebook wall.

---

## ⚠️ The brief's record count was wrong, and the error was structural

`NEXT-RUN-brief-regions-5.md` scoped batch 7 as **151 records**. The true figure is **133**.

151 = the seven straightforward regions (118) **plus the entire unsplit `NE` row (33)**,
instead of just the 15 Newfoundland records inside it. This is precisely the double-count
`RULES-tjjm.md` §5 warns about: *"Any dump that skips the split double-counts NE and NL."*

The brief was internally inconsistent — its own "14 stubs" figure counts NL correctly and
excludes Nebraska. Had the 151 been worked to, batch 5's already-curated Nebraska would
have been dragged back into scope.

**Any future count over these regions must apply the NE/NL city split before counting.**

---

## ⚠️ C7c — a third Newfoundland condition, and it fired

The known C7 conditions were C7a (no Nebraska record may use an NL city) and C7b (the NE
suppression row applies to both pages). A third exists and had never been written down:

> **C7c — a Newfoundland record in a city outside the hardcoded `nl_cities` list renders on
> the NEBRASKA page.** It does not error and it does not vanish.

`nl_cities` was a hardcoded list of exactly ten strings. Batch 7 found **Golden Rule Jiu
Jitsu, Flat Bay NL** — a confirmed school with adult and kids BJJ programmes at 9 Rushy
Pond Lane — whose city was not on it. Added blind, it would have appeared under Nebraska.

Fixed by extending `nl_cities` to eleven entries **and** adding the record in the same
build. The sweep confirms Flat Bay renders on the NL page and does not appear on Nebraska's.

**The gate and the section's city list must stay in lockstep.** `gate_b7.py` carries a
comment saying so. Any future NL city needs both edits.

Still outside the list and therefore still blocked: Stephenville, Happy Valley-Goose Bay,
Carbonear, Bay Roberts, Marystown, Placentia, Deer Lake, Bonavista, Channel-Port aux
Basques, Springdale. Two Facebook-only NL leads (Port aux Basques, Blaketown) are pending.

---

## The Facebook wall — the batch's real constraint

**`web_fetch` cannot render Facebook or Instagram bodies at all.** Six test URLs, all empty.
This is not a per-site quirk; it is a hard limit of the tool. It blocked primary
verification of roughly 20 records, and it fell almost entirely on small towns, because
small clubs do not have websites — they have a Facebook page.

Nova Scotia was hit hardest: its research pass produced 13 small-town leads and its
verification pass promoted **zero** of them, not because they were bad but because they
were unreadable.

**A browser-render pass fixed this.** Running the same URLs through Claude in Chrome, which
executes JavaScript, resolved 24 of 30 targets and produced **17 additional records**.
Nova Scotia went from 20 to 29 on the strength of that pass alone; without it batch 7 would
have shrunk NS below its starting count.

**This should be a standing phase, not a rescue.** Any region whose leads are Facebook-based
is under-counted until it has had a browser pass. The existing backlog item — *"many would
clear with a browser render"* — is now measured: it is worth roughly one record for every
1.8 attempted.

Separately, the browser pass exposed a failure mode plain fetch cannot distinguish:
**three domains (chattanoogabjj.com, murfreesborobjj.com, tribalbjj.com) all resolve to the
identical GoDaddy parked-domain template.** Through `web_fetch` these look like empty
bodies — indistinguishable from a JS-rendered site. Rendered, they are obviously dead.

---

## ⚠️ Two "independent" sources that were not independent

Nova Scotia's 13 leads rested on two directories "corroborating" each other: a Feb-2025
NS-clubs roster and the Coastline BJJ Collective directory. **Josh Presley's roster
explicitly credits Coastline BJJ Collective for help compiling it.** They are one source
wearing two hats.

This is a new shape of the aggregator trap. The existing rule warns against trusting a
directory; it did not anticipate two directories being treated as mutual corroboration.
**Check whether your second source cites your first.**

---

## The verdict-extraction problem, twice

The brief warns to extract verdicts with a leading-keyword regex rather than a delimiter
split. That was necessary but not sufficient — batch 7 hit two further variants:

1. **Column position is not stable.** The TN researcher used a numbered-row layout, so a
   parser reading "column 4" got zero verdicts for all 34 Tennessee records — the same
   silent-zero failure batch 5 suffered. Fixed by locating columns from the header row.
2. **One agent coined a keyword nobody specified** (`WRONG-CITY`).

The durable fix, applied from the verification phase onward: **mandate a strict TSV with
`verdict` as the first column and a closed vocabulary.** All eight verification files came
back conforming and parsed on the first attempt. Do this from Phase 1 next time.

### And a third: the `url` column was ambiguous
Some verifiers recorded the **stored** URL in the `url` column, others the **corrected** one.
Building overrides straight from that column produced **four overrides that merely restated
the stored value** — including `St. John's BJJ|stjohnsbjj.com` when the whole finding was
that the real domain is `.ca`, and `Kaze BJJ|kazebjj.com` which points at the wrong business
entirely. RULES §5 explicitly forbids restating a stored value.

Caught by diffing every proposed override against the stored `w` read out of the legacy blob.
Overrides are now driven by `batches/url-overrides-b7.tsv`, which records `stored_w`,
`new_w` and a rationale for each, and the build **asserts `new_w != stored_w`**.

---

## The gate

Eight conditions, seeded before every run. It **blocked twice** and caught nine real defects.

**Round 1 — six violations:**
- `Underworld BJJ` (DC) collides corpus-wide with a stored `Underworld BJJ` in Millersville
  **MD** — two real, unrelated businesses. Renamed `Underworld BJJ DC`.
- `Athens Jiu Jitsu` (TN) collides with `Athens Jiu Jitsu` in Athens **ALABAMA**, which also
  carries a **blank override** — so the new record would have rendered with no link at all.
  This is exactly the Athens TN/AL collision the batch-7 addendum predicted. Renamed
  `Athens Jiu Jitsu Tennessee`.
- `302 BJJ` proposed twice (Middletown and Wilmington) — one business, two real locations.
  Suffixed by city.
- `Victory Jiu Jitsu Dieppe` proposed as new when it is **already stored** and **already
  carries a blank override**. Converted to an in-place override edit.

**Round 2 — three violations,** all the same shape: the browser pass proposed `ADD` for
records that already exist (`Foley's Martial Arts`, `Montague BJJ`, `Chattanooga BJJ`).
The first two simply stay; the third is a dead stub superseded by `Chattanooga Jiu-Jitsu
Academy`, so it was suppressed instead — otherwise one school would have appeared twice.

### The seeding itself was defective and the reporting hid it
The seeded run reported "all conditions fired" while **C7b and C7c were not actually being
exercised** — C7b's seed had no matching ADD row, and C7c's seed city was one I had just
added to the permitted list. The summary masked both by grouping C7a/b/c into a single "C7".

**Report every sub-condition independently.** A grouped pass is not a pass. Fixed; all ten
sub-conditions now fire separately under `--seed`.

---

## The silent-blank-override list grows from five to seven

New instances found this batch:
- **`Athens Jiu Jitsu`** (Athens, AL)
- **`Victory Jiu Jitsu Dieppe`** (Dieppe, NB) — now fixed in place

Full list is now: `Jungle Gym Martial Arts` · `Action & Reaction MMA` · `Ethos BJJ` ·
`Alliance Jiu Jitsu Easley` · `Ironside Martial Arts` · `Athens Jiu Jitsu` ·
`Victory Jiu Jitsu Dieppe` (resolved).

**One deliberate new blank was created:** `Kaze BJJ and Judo Institute`. Its stored domain
serves a different business in Scarborough Ontario, and no first-party page for the real
Clarksville TN school could be reached. Sending users to an unrelated gym is worse than no
link. Logged here so a future batch does not treat it as an accident.

---

## Duplicate-name traps — five in one batch

The storage format matches on name alone, corpus-wide, so two records sharing a name is a
hard failure that renders both wrong. Batch 7 produced an unusual cluster:

| name | situation | resolution |
|---|---|---|
| `Progressive Martial Arts Academy` | one business, Oak Ridge + Knoxville | second suffixed `- Knoxville` |
| `302 BJJ` | one business, Middletown + Wilmington | both suffixed by city |
| `Dogwood MMA` | Dyersburg + Union City | Union City dropped |
| `Vigilance Martial Arts` | Dickson + Fairview | Fairview dropped |
| `Underworld BJJ` | DC vs existing Millersville MD | DC suffixed |

The TN verifier caught three of these itself and pre-empted them. **Multi-location brands
are the standing source of this defect** — expect roughly one per twenty net-new records.

---

## Wrong-region records — the batch's signature defect

| stored as | actually |
|---|---|
| `Kaze BJJ and Judo Institute` — Clarksville **TN** | Scarborough, **ONTARIO** |
| `Tribal BJJ` — Dover **DE** | Ardmore, **OKLAHOMA** |
| `Synergy MMA` — Wilmington **DE** | **BALI, INDONESIA** |
| `Delaware BJJ` — Wilmington **DE** | Dauntless BJJ, **Newark DE** (right state, wrong city and name) |
| `International Karate Association` — **AK** | domain now Indonesian-language spam |
| `WDC BJJ` — marketed as **DC** | Takoma Park, **MARYLAND** |
| `First State BJJ` — Middletown **DE** | Dover **DE** |
| `Rehoboth Beach BJJ` — Rehoboth Beach **DE** | Lewes **DE** |

**All of them return HTTP 200.** Four are domain-repurposing cases: the domain outlived the
business and now serves someone else entirely. A resolving link remains no evidence at all.

Delaware is the standout: **7 of 7 stored records were defective** — a 100% defect rate,
the worst region ever measured on this project.

---

## Alaska shrank by a third, and it is correct

Alaska went 22 → 14, driven by **eight not-BJJ suppressions**. Five were found by research
and survived independent re-reading; three more (`Greatland Martial Arts`, `Tonbo Dojo -
Alaska Samurai Arts`, `Shoshindo of Alaska`) were settled only by the browser pass after two
earlier passes could not read them.

Two military-base clubs were dropped for lack of public access: `Arctic Warrior BJJ` (JBER)
and, in Nova Scotia, `12 Wing BJJ` (CFB Shearwater) and `Hero Grappling Club` (CFB Halifax).
**A base club is not a directory listing unless civilians can train there** — worth making a
standing rule; three instances appeared in one batch.

Also: **Gracie Barra Alaska is GONE, not merely wrong-URL** — the replacement domain research
proposed is itself NXDOMAIN, and the address is now occupied by Krav Maga Anchorage, confirmed
by reading Krav Maga's own footer.

---

## Other findings

**Tennessee's coverage gap was self-reported and real.** The TN researcher flagged that it had
skipped the small and mid-size towns for budget reasons. The verifier swept them and found
**14 further schools** across Shelbyville, Dyersburg, Tullahoma, Morristown, McMinnville,
Dover, Collierville, Dickson, Johnson City, Gallatin, Sevierville and Memphis. Honest
self-flagging paid off again — this is the third batch running where it has.

**A synthesized search answer was flatly wrong.** WebSearch asserted `Tri-Cities BJJ` was run
by "Keith Olson" at "113 Cherry Street"; the business's own page shows Grand Master Amanda
Olson at a different address. Search summaries are not sources.

**`johnsoncityjiujitsu.com` displays "Tri-Cities Premier Jiu Jitsu Academy" branding while its
body text and contact block describe Ashburn Jiu Jitsu in Ashburn, VIRGINIA.** A branding-vs-body
mismatch inside a single page.

**`374 MMA`'s title tag and meta keywords say "Windsor Ontario"** while its body clearly places
it in Halifax NS — a clean live demonstration of the "title tags lie" rule.

**`nlbjj.com` is not Newfoundland.** "NL BJJ Academy" is Next Level Brazilian Jiu-Jitsu
Association, a Texas-founded lineage brand with 15 academies across 9 countries and zero
Canadian affiliates outside Omaha. It merely abbreviates to "NL BJJ". Suppressed.

**The Foley cluster is genuine.** Four near-identically-named Newfoundland schools (Jason,
Michael, Alex, and Foley's Martial Arts) are four distinct businesses at four distinct
addresses, not a duplication error. Three confirmed by direct address read; the fourth
(Paradise) only by browser render.

**PEI was genuinely near-complete**, exactly as predicted. Ten records in, ten out, with three
swapped. The "every region roughly doubles" heuristic does not hold for very small regions and
the PE researcher was right to refuse to pad the roster.

**Halifax BJJ and Halifax BJJ Society are one business** — halifaxbjj.com canonicalises to
halifaxbjj.ca with identical content, phone and email. One suppressed.

**810 H St NE, Washington DC** was claimed by two current-looking businesses. Resolved as
succession, not co-tenancy: Underworld BJJ is the same programme under new ownership, and
Capital City BJJ's site is stale 2019 content. Likewise `Capitol Hill BJJ` was never a
business name — it is BETA Academy's second location.

---

## ⚠️ NEW: 12 pre-existing duplicate names are already live in the corpus

A corpus-wide name-uniqueness check run as a final verification found **16 names carried by
two or more stored records, 12 of them with both copies LIVE.** These are pre-existing, not
introduced by batch 7 — but nobody had measured them.

Because `tjjm-gym-websites*` and `tjjm-gym-addresses` match **on name alone, corpus-wide**, an
override written for any of these applies to *every* copy. And where two copies sit in the same
region, a single suppression deletes both.

| name | live copies |
|---|---|
| `Capital MMA & Elite Fitness` | Takoma Park MD · **Fairfax VA · Sterling VA** |
| `Southern Maryland Martial Arts & Fitness` | **Bryans Road MD · La Plata MD** |
| `Carlson Gracie Jiu Jitsu` | Gainesville FL · Yuma AZ |
| `Connection Rio Jiu-Jitsu Academy` | College Place WA · Bend OR |
| `Core Combat Sports` | Louisville KY · Rockford IL |
| `EchoValor Striking & MMA` | Centralia WA · Beaverton OR |
| `Evolution Jiu Jitsu` | Juneau AK · Burlington WI |
| `Impact Martial Arts` | Harrison AR · Oshkosh WI |
| `Infinite Jiu-Jitsu` | Phoenix AZ · Rocklin CA |
| `Integrity Martial Arts` | Sydney NS · Moore OK |
| `Logic Jiu Jitsu` | Sacramento CA · Spanaway WA |
| `Zombie Brazilian Jiu-Jitsu and MMA` | Allentown PA · Abilene TX |

**The two bolded rows are the dangerous ones** — same name, same region, both live. Suppressing
either would silently remove both records while the counts still looked consistent, which is
exactly the failure mode the removed-index header warns about.

`Capital MMA & Elite Fitness` is also already implicated as Virginia cross-region debt from the
DC pass. `Evolution Jiu Jitsu` (Juneau AK) is one of batch 7's own held-back rows.

**This is a standing hazard, not a batch-7 defect.** It belongs in the gate as a corpus-health
check, and the twelve should be disambiguated before anyone writes an override touching them.

### RESOLVED — staged in theme LL (`154883129516`)

All twelve were disambiguated in a follow-on build the same session: **14 records renamed via
suppress-plus-add**, net corpus change zero, all 61 region counts unchanged, swept clean.

Two structural findings came out of it:

- **A same-region duplicate cannot be half-renamed.** Suppression matches by name *within* a
  region, so suppressing `Southern Maryland Martial Arts & Fitness` in MD kills *both* copies.
  Both must be renamed and re-added. Same for Capital MMA's two Virginia sites.
- **Consequently, suppressed NAMES and suppressed RECORDS now diverge** — two entries match two
  records each, so 690 names suppress 692 records. The documented assertion
  `stored − suppressions == published` only holds if you count **records**.

Also cleaned up: `Infinite Jiu-Jitsu`'s Phoenix record had **no stored `a` at all** — its address
came entirely from the name-keyed override. The address is now stored on the record directly and
the orphaned override entry was removed.

Four names still carry two stored copies but only one renders, because the other is already
suppressed: `Aurora BJJ`, `Midwest Training Center`, `Northwest Fighting Arts`, `Red River BJJ`.
Safe today, would collide again if a future batch un-suppressed the second copy.

---

## Held back — 16 records

Down from 33 before the browser pass.

- **6 still unreadable after browser render:** `Samson Martial Arts & Fitness` (St. Peter's),
  `SOB / Sprawl or Brawl MMA` (Glace Bay), `Loyalty BJJ` (Dover DE), `Kingsport BJJ`,
  `Murfreesboro BJJ`, `Tri-Cities BJJ` (Johnson City).
- **1 login wall:** `Dragon Martial Arts Colchester` — a Facebook *group*, gated despite being
  labelled Public.
- **`Labrador City BJJ`** — stored domain NXDOMAIN; candidate `novauniaocanada.com` resolves but
  returns a blank body through every route tried. No override written rather than guess.
- **`Golden Rule Jiu Jitsu`** is now added, but two further NL Facebook-only leads
  (Port aux Basques, Blaketown) remain unconfirmed.
- Plus the residual UNVERIFIED rows named in each `batches/verify-b7-*.md`.

## Cross-region debts owed from this batch

**Ontario** — Kaze Brazilian Jiu Jitsu, Scarborough (1950 Ellesmere Rd).
**Oklahoma** — Tribal Jiu-Jitsu, Ardmore.
**Maryland** — WDC BJJ, Takoma Park (720 Erie Ave).
**Virginia** — Capital MMA's Alexandria/Burke/Fairfax/Herndon/Lorton locations; Ashburn Jiu Jitsu.
**Alabama** — `Athens Jiu Jitsu` carries a blank override and so currently renders with no link.

## Owed from this batch

1. The 16 held-back records above.
2. A **browser-render pass as a standing phase** for any region whose leads are Facebook-based.
   Measured yield this batch: 17 records from 30 attempts.
3. **`Labrador City BJJ`** needs either a working URL or a deliberate blank.
4. The two NL Facebook-only leads, and the ten NL cities still outside `nl_cities`.
5. **Nova Scotia second harvest** — the browser pass covered the 13 known leads but did not
   sweep for new ones. NS at 29 across 21 cities is plausibly still short.
