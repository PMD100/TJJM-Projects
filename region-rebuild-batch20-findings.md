# Batch 20 — the 6 Aug audit backlog is cleared.

Session of 13 Aug 2026. Built as theme **XX** (`154934083756`), **staged and awaiting publish**.
Overrides only. **Record counts cannot have moved.**

---

## Result — the backlog is finished

**All 184 known-suspect live links have now been checked.** Batch 19 did 138; this batch did the
last 46.

### Batch 20 (groups 7–8, 46 targets)
| verdict | n |
|---|---|
| KEEP | 27 |
| DEAD | 9 |
| NEEDS_BROWSER | 4 |
| WRONG_ENTITY | 2 |
| NOT_GRAPPLING | 2 |
| **HIJACKED** | **1** |
| UNRESOLVED | 1 |

**23 changes — 14 blanked, 9 replaced.**

### The 184 in total, across batches 19 and 20
| outcome | n | share |
|---|---|---|
| kept as correct | 92 | 50% |
| **blanked** (dead, parked, hijacked, wrong school, not grappling) | **58** | 32% |
| **replaced** with a working URL | **37** | 20% |
| carried forward, needs a browser | 21 | 11% |

**95 bad links removed or corrected.** Half of everything that screen flagged back in August was
genuinely broken.

---

## ⚠️ THE TENTH HIJACK — live on the site until now

**`ACS Mixed Martial Arts` (La Marque, TX)** — `acsmmatx.com` 301-redirects to a Chinese gambling
page titled "Bewei必威精装版下载" (a Betway app download) wrapped around cloned content from an
unrelated Beijing environmental company. No martial-arts content whatsoever.

**Running total: ten hijacked former school domains**, all found on this project:
a Norwegian online casino · three Chinese gambling sites (one a Betway clone) · a Chinese
streaming/piracy site · an Indonesian gambling SEO farm · an ad-redirect farm · a motorsports
content farm · a credit-repair site · a WordPress farm carrying paid links to an escort directory.

**Every one of them resolved, returned 200, and still carried the school's old title in search
results.** This is now the defining risk of the corpus: a rotted link is merely useless, but an
expired martial-arts domain is a *valuable* thing to re-register, and the directory was pointing
real users at ten of them.

## Two more wrong-entity links
- **`Advantage BJJ`** (Houston TX) → now serves **Lockhart Jiu Jitsu**, ~150 miles away. A real BJJ
  school, but not this one, and nothing on the site mentions Houston or Advantage.
- **`Hartford Dojo`** (Wethersfield CT) → pointed at `gracieacademy.com`, the Gracie University
  **corporate domain in Torrance, California**. Never the school's own site.

---

## Method notes

**Host and scheme normalisation was the single most common fix across the whole audit** — roughly a
third of the 37 replacements. The apex renders while `www` returns an empty body, or the reverse.
Several links that looked dead on the stored URL were perfectly alive one character away.

**Agents flagged their own weak evidence consistently**, and it mattered. Five rows in the final
group carry an explicit note that an address came from a third-party listing rather than the
school's own page. One agent declined to condemn a domain purely for sitting on a Chinese IP block
— and was right: it served the genuine school.

**One judgement left open:** `Kifaru Jitsu` (North Las Vegas) was called NOT_GRAPPLING — its own
curriculum is Kenpo/karate striking with no named grappling class — but the founder's history page
describes a judo background. Flagged as overrideable rather than decided unilaterally.

---

## What was written

| file | was | now | change |
|---|---|---|---|
| `snippets/tjjm-gym-websites-3.liquid` | 11,593 B | **12,559 B** | 23 entries added |

Files 1 and 2 unchanged. MD5-verified against theme XX by the caller:
`6ec5f2c4cc9388eb598deb89a81aede8`.
**768 override entries, zero duplicate names, 488 blank.**

### Structural guarantee
Every count-bearing file in XX is byte-identical to WW — legacy blob `1ee054…`, removed-index
`98ee61…`, section `633ec8…`, region-index `8f4faa…`, websites-1 `16a715…`, websites-2 `08c171…`.
**5,215 published / 61 regions preserved by construction.**

---

## TO PUBLISH

**Publish XX `154934083756`.** WW `154932805804` becomes the rollback.
No `metafieldsSet` needed — counts unchanged. Blanking a link does not remove a record.

---

## Where the goal stands after this

| tier | records | status |
|---|---|---|
| verified links | ~280 | checked and correct |
| **the 184 flagged set** | **184** | ✅ **complete** |
| blank | ~695 | correct-by-default; ~230 recoverable |
| **unread live links** | **~4,050** | **the remaining work** |

### Next, in priority order
1. **The hijack-signature screen across the ~4,050 unread live links.** Ten hijacks surfaced from
   incidental checking of a few hundred records. That rate, extrapolated, implies dozens more live
   right now. A mechanical pattern-match for gambling/casino/pharma keywords, unexpected CJK or
   Indonesian content, off-domain redirects and parking boilerplate would find them fast and needs
   no judgement. **This is the highest-value work left in the project.**
2. **21 NEEDS_BROWSER** rows carried from batches 19–20.
3. Continue the blank-filling programme, ~230 recoverable.
