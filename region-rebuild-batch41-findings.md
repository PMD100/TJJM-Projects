# Batch 41 — the never-read half of the directory opens up. Three live hijacks out.

Session of 16 Aug 2026. Built as theme **TTT** (`154977206444`), **staged and awaiting publish**.
Overrides only. **Record counts cannot have moved.**
**Publish TTT `154977206444`.** SSS `154975109292` becomes the rollback.

---

## Three live hijacks, confirmed in a real browser, removed

Found in the first tranche of the identity pass. All three were live on the directory as of today.

| record | what the link actually served |
|---|---|
| `10th Planet North Dallas` | **slotdemoonline.com** — Indonesian slot gambling |
| `Baker's MMA & Fitness LLC` | **Fixbet Türkiye** — Turkish online casino |
| `Applied MMA Austin` | **欢乐派影院** — Chinese film piracy portal |

Each was loaded in Chrome and read, not fetched. Blanked; the schools stay listed with name, city
and map link. Gate C3 verified clean afterwards: **1,140 rows, 1,140 distinct names, zero duplicates.**

These had passed every earlier screen because **their pages had never been opened.** They sat in the
47% of the directory that had only ever had a DNS and parking-IP check.

---

## The identity pass — first 360 of 2,170, and it changes the estimate

| verdict | n | share |
|---|---|---|
| OK — right school, right city | 285 | 79% |
| **SUSPECT** — parked, hijacked, dead, empty, or striking-only | **33** | **9.2%** |
| **AGGREGATOR** — Facebook/Mindbody/Yelp/booking page, not the school's site | **17** | **4.7%** |
| **WRONG_CITY** — a real school, but the wrong one | **15** | **4.2%** |
| NO_CITY — real school, no address to confirm against | 10 | 2.8% |

**About 21% of never-read links have a problem.** My earlier estimate in
`AUDIT-COVERAGE-where-we-actually-are.md` was ~60 bad links hiding in this population. **Extrapolated
from this sample it is closer to 350** — roughly 90 wrong-city, 100 aggregator and 200 suspect.
That estimate was wrong by about 6×, because it assumed this population resembled the `https://`
tail we had sampled. It does not: it is the part nobody ever looked at.

### WRONG_CITY is the find that nothing else could have caught
Fifteen links point at a real, healthy martial arts school — in the wrong place. No DNS check, no
parking check, and no "is this a martial arts site" check can see it. Examples:

- `B Team Jiu Jitsu` (NJ) → redirects to Craig Jones' B-Team in **Austin, Texas**
- `10th Planet Miami` (FL) → the site serves **Miramar**, not Miami
- `Brian Beury Jiu Jitsu` (NY) → **Watervliet**, not Albany — which the batch-7 notes had already
  flagged as an uncorrectable city error, now confirmed from the school's own page
- `Bitterroot Warrior Arts Corvallis` (MT) → the page lists **Hamilton and Stevensville**
- `303 Training Center` (CO) → **Arvada**, `925 Jiu Jitsu` (CA) → **Martinez**,
  `Anaconda BJJ` (NJ) → **North Bergen**

### AGGREGATOR is a quality problem rather than a safety one
Seventeen links go to a Facebook page, a Mindbody or MyStudio booking screen, a Vagaro page, or a
Google `business.site` placeholder rather than the school's own site. They resolve and they are not
harmful, but they are poor directory links.

### The SUSPECT rows are not verdicts
By design. The fetcher caches, so agents were told to flag anything that looked bad rather than
conclude from a fetch. **The three hijacks above came out of that pile after a browser check — the
other 30 still need one.**

---

## A correction to my own accounting

The agent finishing the removal audit found my worklist script was reading the wrong directories,
and corrected the numbers:

- The untested-removal set was **67, not the ~102** I reported. The "445 removals" figure in
  `AUDIT-COVERAGE-where-we-actually-are.md` counts `REPLACE` actions — links swapped, not removed —
  and duplicate rows. **445 is not the number of removals.**
- Those 67 came back **0 false positives**, and the agent was right to say that is *not* comparable
  to the 10.8% from earlier batches: 36 of the 67 are hard NXDOMAIN, and the population was already
  judged with DNS-plus-evidence rather than by the cache-prone fetcher.
- It also refused to score DNS failures caused by the sandbox having no egress, and ran DNS through
  the browser instead. That is exactly right — recording those as dead would have manufactured a
  clean sweep.

**The removal audit is now complete.** Every removal that could be re-tested has been.

---

## Where the directory stands

| | |
|---|---|
| records published | **5,215** across 61 regions |
| with a link | **4,237** |
| deliberately link-free | 978 |
| override rows | 1,140, all distinct names |
| identity pass | **360 of 2,170 done (17%)** |
| removal audit | **complete** |

⚠️ Headroom is tight again: file 1 has 984 bytes, file 4 has 1,632. The next batch touching either
should use the move-to-file-6 pattern rather than appending in place.

## Next

1. **Browser-check the 30 remaining SUSPECT rows**, then blank what they confirm.
2. **Decide the policy on WRONG_CITY.** A link to a real school in the wrong town is a wrong-entity
   link and should probably be blanked — but some may be a school that moved, in which case the
   *record's* city is what is stale. Worth your call before 90 of them get actioned.
3. **Decide the policy on AGGREGATOR.** Facebook pages are the only web presence many small gyms
   have; a Mindbody booking screen is not.
4. **Continue the identity pass** — 1,810 links still never read, about 15 agent groups.
