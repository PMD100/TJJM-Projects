# Batch 45 — 17 more out. Identity pass past halfway. The batch-7 notes keep being right.

Session of 16 Aug 2026. Built as theme **WWW** (`154983399596`), **staged and awaiting publish**.
Overrides only. **Record counts cannot have moved.**
**Publish WWW `154983399596`.** VVV `154982580396` becomes the rollback.

---

## Removed — 17

| reason | n |
|---|---|
| AGGREGATOR — booking platform, `business.site`, brand homepage | 9 |
| WRONG_BUSINESS | 3 |
| DEAD | 2 |
| HIJACK | 1 |
| STRIKING_ONLY | 1 |
| WRONG_CITY | 1 |

16 new rows in file 6, 1 in-place edit in file 2.
**Verified: 1,224 override rows, 1,224 distinct names, zero duplicates.**

Two worth naming. `Hess' Oriental Martial Arts` was serving a **Chinese gambling and pharma site**.
`Iron Sharpens Iron Brazilian Jiu Jitsu Academy` is recorded in **Virginia** and its link serves
**Winchester, England** — the classic same-name-different-continent trap.

Also caught: `Guelph BJJ` and `Hamilton Brazilian Jiu-Jitsu`, both Ontario, both redirecting to
genuinely different clubs (Kohbukan Judo and Bora BJJ respectively). Judo is in scope, so these were
judged on *identity*, not sport — a different club at a different address is still the wrong link.

## 50 of 98 fetch-flagged rows have now proved healthy

Third browser round: 8 of 16 were fine. Running total across all three rounds — **50 of 98, 51%.**

The rule that a fetch may flag but never remove has now preserved **50 working links.** It remains
the single most valuable rule added this programme.

---

## Two links deliberately kept, because the record is what's wrong

- **`Kioto Brazilian Jiu Jitsu`** — record says "New York", the school is in **Oakdale NY**
- **`Long Island MMA`** — record says "Lake Grove", the school is in **West Babylon**

Both are in the batch-7 notes sitting inside `tjjm-gym-websites.liquid`, written months ago:
*"Kioto is in Oakdale not New York … Long Island MMA is in West Babylon not Lake Grove."*

That is now **four** confirmed cases where an identity check flagged a link and the record turned
out to be the error — `AKF Lexington`, `Brian Beury`, and these two. In every case the earlier notes
had already spotted it and recorded that no override could reach the city field.

**The city-correction pass is no longer optional.** These records are actively misfiling schools
into the wrong town's page, and the only fix is editing the data snippets directly.

---

## Identity pass — 1,200 of 2,170 (55%)

| verdict | groups 1–3 | 4–6 | 7–8 | 9–10 |
|---|---|---|---|---|
| OK | 285 (79%) | 295 (82%) | 209 (87%) | **206 (86%)** |
| SUSPECT | 33 | 49 | 16 | 22 |
| AGGREGATOR | 17 | 9 | 10 | 9 |
| WRONG_CITY | 15 | 1 | 3 | 3 |
| NO_CITY | 10 | 6 | 2 | 0 |

Settled at roughly **86% OK**, so about one live link in seven has a problem of some kind.

### Pending
- **22 SUSPECT rows** awaiting a browser pass. Several look genuinely bad: `Impact Martial Arts
  Harrison` (Indonesian slot gambling), `Kaiten Mixed Martial Arts` (real Prince George school with
  casino spam injected), `Inspire Brazilian Jiu Jitsu` (domain expired, parked),
  `Kutting Edge Jiu-Jitsu` (redirects to an unrelated Patreon), `Lopez Martial Arts` (Hostinger
  placeholder), `Kings Combat` and `Kings Combat Fitness` (striking only).
- **970 links still never read.**
- **`Guardian Tactics`** still unresolved — one address lookup on 770 Davis St decides whether the
  link or the record is wrong.

---

## Where the directory stands

| | |
|---|---|
| records published | **5,215** across 61 regions |
| with a link | **4,148** |
| deliberately link-free | 1,067 |
| override rows | 1,224, all distinct names |
| **identity pass** | **1,200 of 2,170 (55%)** |
| removal audit | complete |

⚠️ Headroom: file 1 **339 B**, file 3 **738 B**, file 2 1,269 B, file 4 1,632 B, file 6 **13,194 B**.
All new work to file 6.

## Next

1. **Browser-check the 22 SUSPECT rows.**
2. **Continue the identity pass** — 970 left, about 8 agent groups.
3. **Start the city-correction pass.** Four confirmed record errors and counting; this needs the
   45 data snippets edited, which is a different and more delicate operation than an override.
