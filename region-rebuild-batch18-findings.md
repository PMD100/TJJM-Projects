# Batch 18 — Georgia, Illinois, Nevada. And the hijack problem gets serious.

Session of 13 Aug 2026. Built as theme **VV** (`154923991212`), **staged and awaiting publish**.
Overrides only. **Record counts cannot have moved.**

---

## Result

**90 targets · 34 confirmed · 4 rejected on recheck · 30 published.**

| verdict | n | share |
|---|---|---|
| DEAD | 41 | 46% |
| CONFIRMED | 34 | 38% |
| NEEDS_BROWSER | 12 | 13% |
| NOT_BJJ / UNRESOLVED / WRONG_ENTITY | 3 | 3% |

**One recovery per 3.0 attempts.** **Blank-rendering records: 667 → 637.**
The 46% DEAD rate is the highest of the programme — these three regions had rotted harder than any
previous tranche.

### Rejected on independent recheck
- **`Atlanta Kyusho and Jujitsu` → Evolution X** — every path renders only "EVX" and a logo. No
  address, phone or classes anywhere.
- **`Victory Martial Arts Northbrook`** — the site's only Northbrook content is a 2018 opening
  announcement; Northbrook is absent from its own nav and 8-school footer, and the named instructor
  is now listed at Arlington Heights.
- **`Wand Fight Team`** — a bare PerfectMind storefront with zero class content whose only product
  is a uniform kit.
- **`Fredson Paixao Academy`** — UNVERIFIABLE. Yelp marks the location closed as of Dec 2025 and the
  page was last modified in 2024. Not confirmable in either direction.

Four better URLs adopted: `Gracie Jiu-Jitsu Geneva` → the school homepage rather than a programme
subpath; `Orient Jiu Jitsu` → `/book` rather than a login stub; plus contact/locations pages for
`Full Throttle Fitness` and `LCCT`.

---

## ⚠️ HOSTILE HIJACKS ARE NOW A MAJOR CLASS — eight found, four in this batch alone

A school's expired domain gets re-registered and repointed at something else. **The domain resolves,
returns 200, and search engines still serve the OLD school's title and description for it.** Four
new ones here:

| former school domain | now serves |
|---|---|
| `jamesshookbjj.com` | a Norwegian online-casino site |
| `redlinemma.com` | a Chinese gambling / quartz-materials site |
| `rmnurockton.org` | a WordPress content farm with paid links to an escort directory |
| `fredsonpaixaobjj.com` | a credit-repair site |

Plus `tapoutlasvegas.com` now 301s to the Tapout apparel brand, and `kenshamrock.com` — a real site —
carries **injected Indonesian gambling spam in its footer**, which disqualifies it too.

Running total: **eight hostile hijacks**, spanning casinos, gambling SEO farms, streaming piracy,
ad farms, a motorsports content farm, an escort-link farm and a credit-repair site.

**This changes the risk profile of the whole programme.** A stale link is merely useless; a hijacked
link actively sends the directory's users to gambling and adult content under a jiu-jitsu school's
name. **Following redirects and reading the landing page is now mandatory, not best practice.**

---

## A defect the gate caught — and why it mattered

The first build attempt appended `James Shook Brazilian Jiu-Jitsu` to file 3 while its blanking entry
sat in **`tjjm-gym-websites`, file 1** — not file 2, where every previous batch's blanks had been.
That produced a **cross-file duplicate name**, which the post-build assertion caught and refused.

That mattered more than usual: the fix is to *remove* the file-1 blank, and had it been removed
without the file-3 replacement landing, the record would have fallen back to its stored URL —
`jamesshookbjj.com`, the Norwegian casino. **The no-duplicate-names invariant prevented publishing a
link to a casino.**

The move-not-edit rule now applies to **files 1 and 2 both**, not just file 2.

### A write agent was cut off mid-batch, leaving VV inconsistent
File 1 had been written (blank removed) but files 2 and 3 had not. Re-querying the theme after the
failure — rather than trusting the agent's last message — found exactly that. A second agent was
sent with the current state spelled out and instructed to **write file 3 first** to close the unsafe
window, verifying each file before starting the next. Both landed first attempt.

**This is the second agent lost to a mid-response cutoff this session.** The standing mitigations —
write incrementally, re-query after any agent failure, never trust a write report — all earned their
keep here.

---

## Other findings

**`Fight to Win Lake Norman` / `GB Lake Norman` style duplicates keep surfacing.** This batch found
**ids 43 and 44 are the same school** — 432 Green Bay Rd, listed as Highland Park by Yelp and
Highwood by the site, under two records. Both were published with the same URL, as with the two
Austin pairs from batch 10. **Duplicate-record queue is now five pairs.**

**Rebrands confirmed only by hard identifiers, five more:** Carlos Machado North Atlanta → Campeão
United (same address *and* phone, though lineage changed); James Shook → Tier 1 Jiu-Jitsu (same
owner and phone, moved to Dallas GA); Atlanta Budokan → GAMASD; Hamby → Laviano (same unit, new
owners); Norse Academy → Uniphi MMA (identical address, phone and Facebook page). **`aejiujitsu.com`
301-redirecting to `aeujj.com` was the single most decisive piece of evidence in the batch** — an
owner-controlled redirect is worth more than any amount of name matching.

**`web_fetch` returns an empty body for every Cloudflare-fronted site.** That accounted for most of
the 12 NEEDS_BROWSER rows. Worth adding to the standing notes: Cloudflare + empty body ≠ dead.

---

## What was written

| file | was | now | change |
|---|---|---|---|
| `snippets/tjjm-gym-websites.liquid` | 7,698 B | **7,663 B** | 1 entry moved out |
| `snippets/tjjm-gym-websites-2.liquid` | 21,827 B | **21,249 B** | 20 entries moved out |
| `snippets/tjjm-gym-websites-3.liquid` | 6,951 B | **8,687 B** | 30 entries added |

MD5-verified against theme VV by the caller: `16a7151096dc7212cd927271173d3474` /
`08c1715d3cca873f38de48940978ec6c` / `a7209883177445d1b4a52ae567dbb5d6`.
**673 override entries, zero duplicate names, 430 blank.**

**websites-2 headroom is now 3,327 B** — up from 2,029 B at its worst, while 65 links were added
across batches 13–18. The move-not-edit rule has fully solved that ceiling.

### Structural guarantee
Every count-bearing file in VV is byte-identical to UU — legacy blob `1ee054…`, removed-index
`98ee61…`, section `633ec8…`, region-index `8f4faa…`, addresses `031ea9…`.
**5,215 published / 61 regions preserved by construction.**

---

## TO PUBLISH

**Publish VV `154923991212`.** UU `154921402540` becomes the rollback.
No `metafieldsSet` needed — counts unchanged.

---

## Programme total after seven repointing batches

| batch | targets | published |
|---|---|---|
| 9 FL + debts | 88 | 31 |
| 10 CA, TX | 120 | 47 |
| 11 browser | 44 | 16 |
| 12 NJ OK CO LA | 97 | 31 |
| 13 carry-forward | 48 | 15 |
| 14 browser | 35 | 20 |
| 18 GA IL NV | 90 | 30 |
| **total** | **522** | **190** |

**190 links restored. Blank records 833 → 637, a 24% reduction.** Yield steady at 1 per 2.7.

## Owed

1. **12 NEEDS_BROWSER** from this batch — mostly Cloudflare-fronted. Add to the browser queue with
   batch 14's 4 UNRESOLVED.
2. **Five duplicate-record pairs** now queued: two Austin, Highland Park/Highwood IL, plus
   `theacademyofmma.com` and `usajujitsu.net` from batch 10.
3. **`Las Vegas Fight Club`** — live site, matching address and phone, but boxing only with no named
   grappling class. Suppression candidate under the §9 scope rule.
4. Remaining blank pool: FL 52 · TX 48 · CA 41 · OH 28 · PA 27 · WA 26 · MO 25 · NJ 25 · MA 22 ·
   AZ 20 · VA 20 · MI 19.
