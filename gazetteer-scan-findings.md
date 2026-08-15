# The city/state gazetteer scan — backlog item 10. **NEGATIVE RESULT.**

Run 13 Aug 2026, against theme PP's corpus (5,219 published / 5,911 stored).
**Nothing was written to the store. No records were changed.**

## Verdict, up front

**A corpus-derived gazetteer cannot detect this defect class, and no amount of tuning will fix
it.** Two heuristics were tried before and "both missed the one known case." This run reproduces
that failure, and — more usefully — **explains why**, so the third attempt does not get made on the
same basis.

Backlog item 10 should be **closed as attempted-and-refuted**, or re-scoped to use an external
authoritative gazetteer.

---

## What was built

Both tests use a gazetteer derived from the corpus itself (2,431 distinct cities, 2,378 in
vocabulary), because the sandbox has no outbound network.

- **Test A — name-vs-city.** Does the record's *name* contain a city different from its `c` field?
  Filtered by: city must have ≥3 corpus records; a 45-word generic blocklist (`Alliance`, `Phoenix`,
  `Summit`, `Union`, `Grove`, `Eagle`, …); and **a match contained within the record's own city is
  excluded** (`Vista` in `Bella Vista`, `Huntington` in `Huntington Beach`). That exclusion alone
  cut raw hits from 251 to 41.
- **Test B — city-vs-state.** Is the record's city dominated by a different state elsewhere in the
  corpus?

## Why both fail

### Test A finds brand-vs-location, which is normal, not a defect — 60 hits, ~0 defects
Martial arts schools brand themselves for the nearest metro and operate in a suburb. Every one of
these is *correct*:

`10th Planet Jiu Jitsu Denver` in Wheat Ridge · `Renzo Gracie Houston` in Sugar Land ·
`GB Tacoma` in Fircrest · `Brazilian Top Team Boston` in Everett · `Gracie Humaita Omaha` in
Papillion · `Checkmat Portland` in Gresham · `Atos Jiu-Jitsu Houston` in Deer Park

RULES already lists "a school branded Omaha in Papillion" as a **watch item**. This scan confirms
it is the *rule*, not the exception — 54 of the 60 trailing hits are same-state metro branding.
Test A is a brand-convention detector.

### Test B measures corpus imbalance, not error — 86 hits, ~0 defects
US city names repeat across states constantly. Every one of these is a **real place in the state it
is filed under**, flagged only because the corpus happens to hold more records for the same name
elsewhere:

Alexandria **AL** · Lincoln **CA** · Newark **CA** · Glendale **CA** · Jacksonville **AR** ·
Aurora **MO** · Springfield **MO** · Columbia **TN** · Cleveland **TN** · Charleston **WV** ·
Bridgeport **WV** · Vienna **WV** · Fresno **TX** · Victoria **TX** · Long Beach **MS**

A directory with 5,911 records across 61 regions is far too sparse to infer which state a city
"belongs" to.

### The decisive evidence — the one known defect cannot fire

`Precision MMA` is filed **city Poughkeepsie, state NJ**. Poughkeepsie is in New York; this is a
genuine, confirmed state error. Its corpus distribution is:

    Poughkeepsie -> {NJ: 1, NY: 1}

**A one-to-one split carries no signal whatsoever.** No threshold, no weighting and no
generic-blocklist tuning can extract a defect from that. The corpus contains exactly two
Poughkeepsie records and one of them *is* the error.

(It is also suppressed, so a published-only scan never sees it. But including suppressed records
does not help — the distribution is still 1:1.)

Seed results across both tests:

| seed | defect | Test A | Test B |
|---|---|---|---|
| `Precision MMA` | state wrong (Poughkeepsie → NJ) | no | **no — 1:1 split** |
| `Elite Martial Arts-Richmond` | name/city mismatch | **YES** | no |
| `GB Palm Coast` | filed Orlando, is Palm Coast | no — Palm Coast has <3 corpus records | no |
| `Church BJJ` | filed Muskogee, operates Tulsa | no — the name says neither | no |
| `10th Planet St. Louis` | filed Washington MO | no (suppressed) | no |
| `Vermont BJJ` | city wrong | no — "Vermont" is a state | no |

**One seed of six fires, and it is the least consequential one.**

---

## What actually detects this defect class

**Reading the school's own website.** The repointing passes have found **20+ confirmed city defects
as a side effect** of verifying links — including the two worst known cases:

- `GB Palm Coast` filed under **Orlando**, ~90 miles from its actual address
- `Church BJJ` filed under **Muskogee**, operating in **Tulsa**, ~50 miles away

Neither is visible to any string heuristic. Both were trivial to spot once a human-equivalent read
the contact page. **The repointing pass is the city-defect detector**; the gazetteer scan is not.

Score so far: **repointing 20+, heuristics 1.**

---

## If someone wants to try again, do it this way

1. **Fetch an authoritative gazetteer** — the US Census Bureau national places file and a Canadian
   equivalent — via `web_fetch` or the browser. The sandbox has no network, so this must come in
   from outside and be cached in `scratch/`.
2. Assert `(city, state)` exists in that gazetteer. That, and only that, catches `Precision MMA`.
3. **Do not use Test A at all.** Brand-vs-location is the industry norm; it will always be noise.
4. Expect the yield to be small. The genuinely wrong ones found so far were wrong about the
   *city within the right state* (Orlando vs Palm Coast), which a gazetteer also cannot catch —
   both are real Florida cities.

**Realistically, an external gazetteer would catch only the wrong-state subclass.** The
wrong-city-within-state subclass — which is most of what has actually been found — is only
detectable by reading the site.

---

## Salvage: one genuinely useful artifact

`batches/gazetteer-scan-b12.tsv` holds all 146 hits. The 60 Test-A rows are a **reference list of
legitimate brand-vs-location pairs**. Hand it to future verification agents so they do not flag
`10th Planet Denver` in Wheat Ridge as a wrong-city defect — that mistake would create false
positives in exactly the pass that is currently doing the real detection work.
