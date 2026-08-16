# Batch 42 — the identity pass starts paying. 32 links removed, 11 saved from removal.

Session of 16 Aug 2026. Built as theme **UUU** (`154980188332`), **staged and awaiting publish**.
Overrides only. **Record counts cannot have moved.**
**Publish UUU `154980188332`.** TTT `154977206444` becomes the rollback.

---

## Your two policy calls, now in force

- **Wrong city → blank the link, keep the record.**
- **Aggregators → keep a school's own Facebook or Instagram page; blank booking platforms
  (Mindbody, Vagaro, MyStudio), Google `business.site` pages, brand homepages, and third-party
  directories.**

Both are written into the file headers so future batches inherit them.

## What was removed — 32

| reason | n |
|---|---|
| DEAD | 10 |
| AGGREGATOR — booking platform, `business.site`, or brand homepage | 8 |
| STRIKING_ONLY — no grappling taught | 7 |
| WRONG_CITY | 5 |
| PARKED | 1 |
| WRONG_BUSINESS | 1 |

30 were new blanking rows in file 6; 2 were in-place edits (`Atlanta Budokan` in file 3,
`Bellmore Kickboxing Academy` in file 1).

**Verified: 1,170 override rows, 1,170 distinct names, zero duplicates.** Every one of the 32 is
blank-valued in exactly one file.

---

## The part that matters more: 11 links were saved from removal

33 links had been flagged SUSPECT by the fetch-based pass. Loaded in a real browser, **11 were
perfectly fine.** Had we acted on the fetch verdicts, we would have removed 11 working links from
live schools.

That is the stale-cache flaw caught in the act, and it is why the pass was designed to flag rather
than conclude. The rule is earning its keep: **a fetch may not remove a link. Only a browser may.**

## And the wrong-city classifier over-triggered — badly

The pass returned 15 WRONG_CITY rows. Checking each against the record's stored city and street
address, **only 5 were genuine.** The other 10 were adjacent suburbs:

| record | site says | apart |
|---|---|---|
| `303 Training Center` Westminster CO | Arvada CO | ~4 mi |
| `Bataille Jiu Jitsu` Kinnelon NJ | Bloomingdale NJ | ~4 mi |
| `Bayshore BJJ` Middletown NJ | Hazlet NJ | ~5 mi |
| `Anaconda BJJ` Lyndhurst NJ | North Bergen NJ | ~6 mi |
| `Black Tiger` Libertyville IL | Grayslake IL | ~7 mi |
| `925 Jiu Jitsu` Concord CA | Martinez CA | ~8 mi |
| `Academy Of Striking & Grappling` Riverside CA | Moreno Valley CA | ~8 mi |
| `AE Brazilian Jiu Jitsu` Las Vegas NV | Henderson NV | city line |
| `AKF Lexington` Nicholasville KY | **Lexington KY** | the record's own city is the suburb |
| `Brian Beury Jiu Jitsu` Albany NY | **Watervliet NY** | already documented in batch 7 as a *record* error |

**None of these was blanked.** In every case the link is fine and it is the record's city that is
imprecise or stale. `Brian Beury` is the clearest: our own batch-7 notes flagged years ago that the
record says Albany and the school is in Watervliet — the link was right all along.

**This is a data-quality finding about the records, not the links,** and city is not overridable
through this system — it needs a data-snippet edit. Worth its own pass.

The 5 genuine removals: `B Team Jiu Jitsu` (Edison NJ → Craig Jones' B-Team in **Austin TX**),
`BlackSmith Jiu Jitsu` (Tallahassee → Niceville, ~150 mi), `Atlanta Budokan` (Smyrna → Acworth, and
trading as Georgia Martial Arts), `10th Planet Miami` (→ Miramar), `Bitterroot Warrior Arts
Corvallis` (page lists Hamilton and Stevensville, not Corvallis).

---

## Where the directory stands

| | |
|---|---|
| records published | **5,215** across 61 regions |
| with a link | **4,205** |
| deliberately link-free | 1,010 |
| override rows | 1,170, all distinct names |
| **identity pass** | **360 of 2,170 read (17%)** |
| removal audit | complete |

⚠️ Headroom is now genuinely tight: **file 1 has 339 bytes, file 3 has 838.** Files 2, 4 and 5 have
room and file 6 has 18 KB. Future batches should use file 6 or add file 7.

## Next

1. **Continue the identity pass — 1,810 links still never read.** Worklists `id-4` … `id-6` are
   built and ready; about 15 agent groups in total.
2. **A city-correction pass on the records.** The 10 adjacent-suburb cases are the visible tip;
   there are likely many more, and fixing them needs the data snippets edited, not overrides.
3. Re-check the 10 NO_CITY rows — real schools whose pages carry no address at all.
