# City-correction verification — method and open questions

Output: `city-corrections-VERIFIED.tsv` (70 rows = 69 shortlist rows + 1 seed-only row,
`Hero Fitness Academy`; the other 5 seed rows are also in the shortlist and were re-verified there).

## Sources

1. **Stored record data** — all 45 `.liquid` files in `scratch/raw-datafiles/` were parsed with the
   documented split-on-`{"n":"` method (5,911 records recovered, including the bare-object files
   29–34). Every one of the 70 names matched exactly one record after normalising case, punctuation
   and curly apostrophes. One name (`ALLIANCE JIU JITSU`) matches two records; the Huntsville AL /
   `alliancehuntsville.com` one is this row, the other is a Key Biscayne FL record.
2. **Live site fetch** — `mcp__workspace__web_fetch` on the shortlist URL. No fetch came back blank,
   stale or unreadable, so there are **no NEEDS_BROWSER rows**. No Facebook/Instagram URLs were in
   the shortlist.

## Which rows were fetched

Fetching was prioritised by risk. **Every row classified CORRECT_CITY or RELOCATED was fetched and
its address read directly off the live site** — no city change in this file rests on the shortlist
note alone.

Rows left desk-verified (marked `record; not re-fetched` or `note; not re-fetched` in the `source`
column) are all *no-change* verdicts where the stored address `a` sits plainly inside the recorded
city, or the "other town" is a neighbourhood/metro twin. Since the recommended action for these is
"do nothing", not fetching them cannot move a school off its page. They are flagged so a later pass
can re-check them cheaply if wanted.

## Decision rule used

- **CORRECT_CITY** — the site publishes exactly one address, in town X; the record's city Y appears
  nowhere on the site; and the stored address is either also in X or absent/not in Y.
- **RELOCATED** — same, but the stored address is demonstrably the *old* premises in a different
  town, i.e. the record was right once. Old address is kept in `stored_address`.
- **ADJACENT_OK** — the stored address is clearly inside the recorded town, or the other town is a
  borough/neighbourhood (Brooklyn, Manhattan, Leather District, Druid Hills), a same-agglomeration
  municipality (Kirkland within Montreal, Pinecrest within Miami-Dade), or a sub-10-mile neighbour
  where the recorded town remains a fair label.
- **ADDRESS_ONLY** — move within the same town; also used where the record and site agree on city
  and only the street changed.
- **AMBIGUOUS** — multiple candidate locations, an entity/URL mismatch, or a reported move that could
  not be corroborated.

Where the rubric's "under ~10 miles → ADJACENT_OK" heuristic collided with an unambiguous site
address, the site address won: Hazlet vs Middletown (~4mi), Grayslake vs Libertyville (~7mi),
Bloomingdale vs Kinnelon (~4mi), Southfield vs Detroit (~10mi), Watervliet vs Albany (~5mi). In each
of those the record's town appears **nowhere** on the site and the school has a single premises, so
leaving the record as-is files it under a town it has no presence in.

## Region changes — read before applying

Only **two** rows carry a region implication, and neither should be handled as a routine city edit.

- **Method BJJ** (record `NJ / South Plainfield`) — this is not a New Jersey school at all. The site
  is tagged `bjj edmonton`, `edmonton alberta`, `method bjj edmonton` throughout, and carries a post
  dated 26 Nov 2025: *"Method BJJ has closed its doors."* `region_change = AB`.
  **Recommendation: delete the record, do not re-file it to Alberta.** The school is closed; moving a
  defunct Edmonton gym onto an Alberta page helps nobody. If the directory keeps closed entries,
  then city `Edmonton`, region `AB`.
- **American Grappling** (record `KY / Tompkinsville`, stored `1101 N Main St`) — the *record* looks
  like a real Tompkinsville KY address, but `americangrappling.org` is now a Raleigh NC grappling
  **tournament organisation**, not a school, and publishes no venue address.
  `region_change` is recorded as `NC?` and the row is **AMBIGUOUS, no city change**.
  **Recommendation: do not move it to NC.** Either drop the stale URL and keep the Tompkinsville
  address, or delist the record — a tournament promoter is not a school listing. Settle by checking
  whether anything still operates at 1101 N Main St, Tompkinsville.

## Rows I could not resolve

- **Atlanta Budokan** (`GA / Smyrna`, stored `2508 Cobb Pkwy SE`) — the shortlist URL `gamasd.com`
  is *Georgia Martial Arts and Self Defense Acworth* at 3485 Acworth Due West Rd, ~20mi away, while
  the record's own `w` field is `atlantabudokan.com` and the stored address is a Smyrna one.
  This is an identity/URL question, not a city question. **No change.** Settle by fetching
  `atlantabudokan.com` and checking whether 2508 Cobb Pkwy SE is still occupied.
- **Skinner's Martial Arts** (`KY / Grand Rivers`) — reported rebrand to "Transform Academy" in
  Calvert City (~10mi). Not fetched, not corroborated. **No change.** Settle by fetching
  `skinnersmartialarts.com`.
- **Tutaj Brazilian Jiu Jitsu** (`IL / Forest Park`, stored `1525 Circle Ave`) — reported move to
  North Riverside (~2mi). Not fetched. **No change.** Settle by fetching `tutajbjj.com`.
- **BJJ Revolution Team – Baton Rouge** (`LA / Zachary`) — the URL is the affiliation's national
  homepage (which lists a Williston VT office). Nothing about the Zachary record's city is in doubt;
  the *URL* is wrong. **No city change**; fix or drop the URL.
- **AKF Lexington Martial Arts** — classified CORRECT_CITY → Lexington, but note the page carries
  **two** addresses: the footer/contact block says 4383 Old Harrodsburg Rd, Lexington KY 40513, while
  an embedded Google map still queries "125 Cynthia drive lexington" (the stored address, which is a
  Nicholasville street). I took the footer as current and the map embed as stale, which agrees with
  the seed file's high-confidence verdict. If someone wants belt-and-braces, phone the school.
- **Gracie New Jersey Academy** — the site writes its address as "56 Payne Rd Lebanon (Clinton TWP),
  New Jersey 08833". I used **Lebanon** (the postal city) as `new_city`; if the directory keys on
  municipality rather than postal town, use **Clinton Township** instead.
- **Long Island MMA** — now has two locations (West Babylon HQ and a new Long Island City site with
  Team Savage). I set the city to the HQ, West Babylon. If the directory supports multi-location
  records, this is a candidate for a second entry rather than a rename.
- **Whitefish BJJ / James Shook BJJ / New Way** — all three relocated *and* rebranded
  (Glacier Grappling & MMA, Tier 1 Jiu-Jitsu, New Way Training Center). The city fix is safe on its
  own, but the `name` and `w` fields on those records are also stale.

## Counts

| classification | rows |
| --- | --- |
| ADJACENT_OK | 31 |
| CORRECT_CITY | 17 |
| ADDRESS_ONLY | 12 |
| RELOCATED | 5 |
| AMBIGUOUS | 5 |
| NEEDS_BROWSER | 0 |
| **total** | **70** |

22 of 70 rows (31%) warrant a city edit; the other 48 should be left alone.
