# Batch 26 — dirty-bucket screen, groups 1–2. Plus the Alberta region check.

Session of 13 Aug 2026. Built as theme **DDD** (`154951614636`), **staged and awaiting publish**.
Overrides only. **Record counts cannot have moved.**

**Publish DDD `154951614636`.** CCC `154950467756` becomes the rollback.

---

## Cumulative screen — 1,328 of 4,240 unread links

| verdict | n | share |
|---|---|---|
| OK — a martial arts site | 1,093 | 82.3% |
| EMPTY — JS-rendered, needs a browser | 151 | 11.4% |
| **PARKED** | **33** | **2.5%** |
| **HIJACK** | **24** | **1.8%** |
| **WRONG_BUSINESS** | **15** | **1.1%** |
| DEAD | 7 | 0.5% |
| UNSURE | 5 | 0.4% |

**79 blanked — 5.9% actively bad.** **15 blanked in this batch.**

## Four more hijacks — thirty-two total
| record | what its domain now serves |
|---|---|
| `Cutting Edge Brazilian Jiu Jitsu` | **Arta189** — Indonesian slots, via `fortworthrvshow.com` |
| `Ryoku Judo Club` | **Remipoker** — Indonesian slots/poker |
| `LifeStyle BJJ` | **DAX69** — Indonesian slot gambling |
| `JAO Martial Arts / Caio Terra NY` | a Chinese **"AG"** gambling-branded SEO site |

## Five wrong-business links
A **Spanish language school in Gran Canaria** · a martial arts **apparel retailer** · a
**barbell/powerlifting club** with no martial arts · a school that has moved to **Babcock Ranch,
Florida** · and a strength gym whose BJJ page is gone.

---

## ⚠️ THE ALBERTA CHECK — the owner's report was not reproduced

The owner reported that **nearly all Alberta gyms resolved to Chrome's
`DNS_PROBE_FINISHED_NXDOMAIN` page**, with a screenshot showing `firststatebjj.com`. Alberta was
screened in full — all 72 published records, every one of which renders a link.

**Result: 0 of 72 are dead.**

All 52 unique hostnames returned DNS `Status: 0` with populated `Answer` arrays. Not one NXDOMAIN,
not one REFUSED, not one empty answer. Every one then served a live martial-arts page. **70 OK, 2
EMPTY** (`graciebarracalgary.ca` and `thekomodoacademy.com` — both alive, JavaScript-rendered).
Zero parked, zero hijacked, zero dead.

Hosting is ordinarily scattered — Squarespace, Wix, Cloudflare, WP Engine, Shopify, Azure, one
Brazilian host. 18 of the 72 are Arashi-Do location pages on a single healthy host. **No shared
infrastructure to cluster on, because nothing failed.**

**And `firststatebjj.com` is not Alberta.** It is `First State BJJ`, Middletown **Delaware** — a
genuinely dead domain that was **suppressed in batch 7** and renders nothing on the live site today.

### Most likely explanation
A local resolver problem on the reporting machine — VPN, DNS filtering, or a poisoned OS cache —
would produce that exact page across many domains that are in fact healthy. **Unresolved**: the
owner has been asked for two or three specific gym names so those exact records can be re-checked.

### The methodological lesson, which is real regardless
Batch 25 concluded from a random sample of 120 that the `https://` bucket was "nearly clean."
**Alberta is 72 records, 100% `https://`, and only 3 had ever been screened.** A corpus-wide random
sample measures the *mean* and is blind to *regional concentration*. Even though Alberta turned out
fine, the criticism stands: **that sample could not have detected a bad region, and nothing in the
method would have flagged it.** Future sampling should stratify by region as well as by rot risk.

Full evidence: `scratch/region-check/verdict-AB.tsv`.

---

## What was written

| file | was | now | change |
|---|---|---|---|
| `snippets/tjjm-gym-websites-3.liquid` | 14,462 B | **14,978 B** | 15 blanking entries added |

Files 1 and 2 unchanged. MD5-verified against theme DDD by the caller:
`56bdc1517ed98dabbb0870c2972e5b00`. **847 override entries, zero duplicate names.**

### Structural guarantee
Every count-bearing file in DDD is byte-identical to CCC — legacy blob `1ee054…`, removed-index
`98ee61…`, section `633ec8…`, region-index `8f4faa…`, websites-1 `16a715…`, websites-2 `08c171…`.
**5,215 published / 61 regions preserved by construction.**

---

## Running total

| programme | audited / screened | links removed or fixed |
|---|---|---|
| 6 Aug flagged set (batches 19–20) | 184 | 95 |
| hijack screen (batches 21–26) | 1,328 | 79 |
| Alberta region check | 72 | 0 |
| **total** | **1,584** | **174** |

Plus **190 links restored** in batches 9–18. **364 link changes.**

---

## Next

1. **862 dirty-bucket links remain** — worklists `dirty-3.tsv` … `dirty-8.tsv` are pre-split.
   About 7 agent groups. Expect ~50 more bad links and most of the remaining hijacks.
2. **Then the `https://` tail**, 2,174 links — low yield for harm, but **stratify by region this
   time**, one sample per region rather than corpus-wide.
3. **151 EMPTY rows** now queued for a browser session — this is becoming the largest single
   backlog and deserves its own pass.
4. **The identity pass** remains the final tier.
