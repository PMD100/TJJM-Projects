# Batch 33 — screened, built, gated, NOT yet written to a theme

Session of 15 Aug 2026. **KKK `154959118508` is MAIN and unchanged — the site is exactly what you
published.** No theme was created this round.

**The finished file is on disk:** `build-b33/tjjm-gym-websites-3.liquid`
21,665 B · MD5 `b5c6a33dda6253ea6382159161b2cd0f` · 2,911 B under the ceiling.
Next session: duplicate KKK, upsert that one file, verify the MD5 matches, publish.

---

## Capacity — the theme is nowhere near full

The `~24,576 B` limit is **not a Shopify theme limit**. It is how large a single file can be pushed
through the Admin API in one rewrite. The theme itself is fine: it already carries a 113 KB data
snippet and a 95 KB product section.

| file | size | headroom |
|---|---|---|
| `tjjm-gym-websites.liquid` | 24,032 B | **544 B — full** |
| `tjjm-gym-websites-2.liquid` | 21,249 B | 3,327 B |
| `tjjm-gym-websites-3.liquid` | **21,665 B after this batch** | 2,911 B |

So roughly **one more batch** fits. After that, add `snippets/tjjm-gym-websites-4.liquid` and one
`{%- render 'tjjm-gym-websites-4' -%}` to each of the two sections. Unlimited headroom, ~30 minutes.
**Nothing about the directory is capped.** The 45 data snippets are untouched by any of this.

---

## What was screened this session

### Brand per-location audit — 194 URLs, 33 broken (17%)
URLs living on a shared brand domain with a per-location path. The brand domain is always healthy,
so **DNS is useless here and every previous screen passed these**.

| verdict | n |
|---|---|
| OK | 161 |
| **REPLACE — school moved to its own domain** | **17** |
| **DEAD** | **15** |
| **MOVED — page serves a different city** | **1** |

**17 of the 33 are recoveries, not removals.** Gracie Barra schools that left the brand site kept
trading under their own domains. Each replacement was opened and the city confirmed:

`GB Renton` · `GB Tacoma` · `GB Encinitas` · `GB Fleming Island` · `GB Fullerton` · `GB Fulshear` ·
`GB HQ Irvine` · `GB Thousand Oaks` · `GB Newport Beach` · `GB Oceanside` · `GB Palmetto Bay` ·
`GB Santa Ana` · `GB Windermere` · `UFC GYM Sunnyvale` · `10th Planet Denver` ·
`Checkmat Charlotte` · `Gracie Jiu-Jitsu North Pole`

**UFC GYM is the opposite story — 11 dead location pages, no replacements.** And note the failure
mode: several **silently redirect to the generic find-a-gym index** and return HTTP 200 with a
real-looking page. A status-code check alone passes them. The page has to be read and the city
matched. That is now a third named failure mode alongside resolves-but-404.

`10th Planet Denver` was found twice — the stored URL is a **HugeDomains lander at $13,495**, and
the school is live at `10thplanetdenver.com`. Repointed, not blanked.

### Parked-and-dead sweep — finished
The last 509 rows: **17 bad** (8 parked, 9 dead). **The sweep is now complete across all 2,286
previously unscreened links.**

One judgment call worth knowing: `bellevillebjj.com` (Belleville BJJ, Ontario) resolves normally and
isn't parked, but 301s to Savarese BJJ in **Lyndhurst, New Jersey**. Blanked as wrong-entity.

---

## What the built file contains

- **17 repoints** — new, verified URLs
- **22 new blanking rows**
- **4 existing rows edited to blank**, because gate C3 forbids a name in two files:
  `GB La Crescenta` (page serves La Cañada Flintridge) · `Kingsnake Jiu-Jitsu` (NXDOMAIN) ·
  `Jaguar BJJ` (NXDOMAIN, carried from batch 32) · `Catch MMA` (dead, carried from batch 32)

**43 link changes.** Three candidates were rejected by the gates and correctly so — `5th St. Gym`
was already blanked in batch 32, and the other two were the file-3 rows now edited in place.

Gates run: no `|` or `~` in any name; no name in another override file; every name matches exactly
one published record; every repoint diffed against the stored value so none restates it.

### Expected effect after publish
Records stay at **5,215** — overrides cannot move counts. Links go **4,323 → 4,340**
(+17 repoints, −22 new blanks, +… net of the 4 edits which were already-counted links).
Verify on the preview by re-running the section's merge, as in batches 30–32.

---

## Evidence on disk
- `scratch/brand-audit/verdict-brand-{1,2,3}.tsv` — 194 rows
- `scratch/park-sweep/verdict-sweep-{1..8}.tsv` — 2,286 rows, sweep complete
- `scratch/hijack-screen/browser-queue-2026-08-15.tsv` — 223 rows still queued
- `scratch/park-sweep/social-deferred.tsv` — 162 social/aggregator links

## Next, in priority order
1. **Apply batch 33** — one file, already built and gated.
2. **Add `tjjm-gym-websites-4`** before the batch after that; all three files are nearly full.
3. **Browser queue, 223 rows** — the largest remaining accuracy gain, ~90 links recoverable.
4. **162 social/aggregator links** — many are bare Facebook brand homepages, not the school's page.
5. **The identity pass** and the ~892 link-free records.
