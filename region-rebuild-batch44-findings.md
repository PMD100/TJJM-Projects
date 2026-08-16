# Batch 44 — 40 more links out, 31 saved. Identity pass at 960 of 2,170.

Session of 16 Aug 2026. Built as theme **VVV** (`154982580396`), **staged and awaiting publish**.
Overrides only. **Record counts cannot have moved.**
**Publish VVV `154982580396`.** UUU `154980188332` becomes the rollback.

---

## Removed — 40

| reason | n |
|---|---|
| **AGGREGATOR** — booking platform, `business.site`, brand homepage | **19** |
| DEAD | 9 |
| STRIKING_ONLY | 4 |
| PARKED | 3 |
| WRONG_BUSINESS | 2 |
| WRONG_CITY | 2 |
| HIJACK | 1 |

38 new rows in file 6, 2 in-place edits in file 3.
**Verified: 1,208 override rows, 1,208 distinct names, zero duplicates.**

Notable: `Gracie Barra Trinity` was serving **injected gambling and adult links**;
`GB Sorrento Valley` redirects to an expireddomains.com for-sale lander; `GB Boynton Beach` points
at **SBG Boynton Beach — a different school**; `DualForces 001` is now an LA branding agency;
`Elite Jiu-Jitsu Academy` is recorded in Boise, Idaho and serves **Newark, Delaware**.

## The number that matters: 31 of 49 were healthy

The fetch pass flagged 49 rows as suspicious. Loaded in a real browser, **31 were fine.** Acting on
the fetch verdicts would have removed 31 working links from live schools.

Combined with the previous round, **42 of 82 fetch-flagged rows have now turned out healthy — 51%.**
A fetch flag is barely better than a coin toss on this corpus. §11 of the rules now says a fetch may
flag but never remove; that rule has saved 42 links in two batches.

Most of the false alarms are one class: **Facebook and Instagram pages, which the fetcher returns
blank for every time.** A browser renders them normally.

---

## Identity pass — 960 of 2,170 (44%)

| verdict | groups 1–3 | groups 4–6 | groups 7–8 |
|---|---|---|---|
| OK | 285 (79%) | 295 (82%) | **209 (87%)** |
| SUSPECT | 33 | 49 | 16 |
| AGGREGATOR | 17 | 9 | 10 |
| WRONG_CITY | 15 | 1 | 3 |
| NO_CITY | 10 | 6 | 2 |

The OK rate is climbing as the classifier calibrates, not because the data is improving — groups 1–3
over-flagged wrong-city badly and that has been corrected.

### Two wrong-city rows deliberately NOT blanked
Under the rule that the record's city may be the error rather than the link:

- **`Guardian Tactics`** — recorded Plymouth MI, site says Holland MI, ~150 miles apart. But the
  record's stored address is **770 Davis St**, and Holland MI has a Davis St. If the address belongs
  to Holland then the record's city is wrong and the link is right. **Needs the address resolved
  before anything is done.**
- **`Hero Fitness Academy`** — recorded Calhoun LA, site says West Monroe LA. Both sit on US-80 about
  10 miles apart, and the record's address is 985 US-80. Adjacent — left alone.

### Still pending
- **16 SUSPECT rows** from groups 7–8 awaiting a browser pass. Nine are Facebook blanks and probably
  fine; `hessma.com` (`Hess' Oriental Martial Arts`) looks hijacked to a gambling/pharma site but
  was fetch-only, so it has not been touched.
- **1,210 links still never read.**

---

## Where the directory stands

| | |
|---|---|
| records published | **5,215** across 61 regions |
| with a link | **4,165** |
| deliberately link-free | 1,050 |
| override rows | 1,208, all distinct names |
| **identity pass** | **960 of 2,170 (44%)** |
| removal audit | complete |

⚠️ File 3 is down to **738 bytes** and file 1 to **339**. File 6 has 15,800. All new work goes to
file 6; when it fills, add file 7 and wire one `{%- render -%}` into each of the two sections.

## Next

1. **Browser-check the 16 SUSPECT rows** from groups 7–8.
2. **Continue the identity pass** — 1,210 links left, about 10 agent groups.
3. **Resolve `Guardian Tactics`** — one address lookup decides whether the link or the record is wrong.
4. **The city-correction pass**, once the identity pass has finished surfacing candidates. Confirmed
   so far: `AKF Lexington`, `Brian Beury`, probably `Guardian Tactics`, plus seven relocations noted
   in group 6. City is not overridable — this needs the data snippets edited.
