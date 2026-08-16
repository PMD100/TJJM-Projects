# Batch 33 — the brand per-location audit. 17 links recovered, 26 removed.

Session of 15 Aug 2026. Built as theme **LLL** (`154960298156`), **staged and awaiting publish**.
Overrides only. **Record counts cannot have moved.**
**Publish LLL `154960298156`.** KKK `154959118508` becomes the rollback.

*(Supersedes `region-rebuild-batch33-READY-TO-APPLY.md`, which described this batch before it was
written to a theme. That file can be deleted.)*

---

## The brand per-location audit — 194 URLs, 33 broken (17%)

Links that live on a **shared brand domain with a per-location path** —
`graciebarra.com/<slug>/`, `ufcgym.com/locations/<city>/`, `tsk.com/locations/...`,
`arashido.com/location/...`, `eastonbjj.com/...`, `checkmat.com/...`. The brand domain is always
healthy, so **DNS tells you nothing and every screen we had run passed all 194**.

| verdict | n |
|---|---|
| OK | 161 |
| **REPLACE — school moved to its own domain** | **17** |
| **DEAD** | **15** |
| **MOVED — page serves a different city** | **1** |

### Seventeen of the thirty-three were recoveries, not removals
Gracie Barra schools that left the brand site are alive under their own domains. Each replacement
was opened and the city confirmed against the record before it was written:

`GB Tacoma` · `GB Renton` · `GB Encinitas` · `GB Fullerton` · `GB HQ Irvine` · `GB Newport Beach` ·
`GB Oceanside` · `GB Santa Ana` · `GB Thousand Oaks` · `GB Fleming Island` · `GB Palmetto Bay` ·
`GB Windermere` · `GB Fulshear` · `10th Planet Denver` · `Checkmat Charlotte` ·
`UFC GYM Sunnyvale` · `Gracie Jiu-Jitsu North Pole`

`10th Planet Denver` is the sharpest example: its stored URL was a **HugeDomains lander asking
$13,495**, while the school trades happily at `10thplanetdenver.com`.

### UFC GYM is the opposite story — and a third named failure mode
**Eleven** UFC GYM location pages are broken and none had a replacement. Several do not 404 —
they **silently redirect to the generic find-a-gym index and return HTTP 200 with a real-looking
page**. A status-code check passes them. A "is this a martial arts site?" check passes them too,
because it *is* a martial arts site. Only reading the page and matching the city catches it.

Three failure modes are now named, and none is caught by DNS:

1. **Resolves-but-404** — domain healthy, root returns 404 (batch 30).
2. **Location-page 404** — brand domain healthy, the school's subpage is gone (batch 32).
3. **Redirect-to-index** — brand domain healthy, subpage redirects to a locations list, HTTP 200.

---

## The parked-and-dead sweep is complete

The last 509 rows returned **17 bad** — 8 parked, 9 dead. **All 2,286 previously unscreened links
have now been swept.**

One judgment call: `bellevillebjj.com` (Belleville BJJ, Ontario) resolves normally and is not
parked, but 301s to **Savarese BJJ in Lyndhurst, New Jersey**. Blanked as wrong-entity.

---

## What was written

| file | was | now |
|---|---|---|
| `snippets/tjjm-gym-websites-3.liquid` | 15,431 B | **21,665 B · `b5c6a33dda6253ea6382159161b2cd0f`** |

Byte-identical to the local build in `build-b33/`. **1,004 override entries, 711 blanking, zero
duplicate names.** 2,911 B of headroom left.

Contents: **17 repoints · 22 new blanking rows · 4 existing rows edited to blank.** The four edits
were required because gate C3 forbids a name appearing in two override files, and they finally clear
`Jaguar BJJ` and `Catch MMA`, which the gates blocked in batch 32:

| record | was | why |
|---|---|---|
| `GB La Crescenta` | `graciebarra.com/la-canada-ca/` | page serves La Cañada Flintridge |
| `Kingsnake Jiu-Jitsu` | `kingsnakebjj.com/` | NXDOMAIN |
| `Jaguar BJJ` | `jaguarbjj.com/` | NXDOMAIN |
| `Catch MMA` | `catchmma.com/` | dead |

### Verified live on the LLL preview
Re-ran the section's own merge in the browser:

```
records published   5,215   unchanged
with a link         4,297   was 4,323 — exactly minus 26 (22 blanks + 4 edits)
link-free             918   was 892  — exactly plus 26
override entries    1,004   was 965  — exactly plus 39 (17 repoints + 22 blanks)
blanking entries      711   was 685  — exactly plus 26
```

Spot checks: `GB Tacoma` → `graciebarratacoma.com/`, `GB HQ - Irvine` → `gbirvine.com/`,
`10th Planet Denver` → `10thplanetdenver.com`, `Checkmat Charlotte` → `realamericangrappling.com/`,
`UFC GYM Sunnyvale` → the working `/locations/sunnyvale` page. `UFC GYM Lancaster`,
`GB La Crescenta`, `Jaguar BJJ`, `Catch MMA`, `Kingsnake Jiu-Jitsu` and `Belleville BJJ` all render
with **no link**.

### Structural guarantee
Only one file changed. Every record-bearing file in LLL is inherited unchanged from KKK.

---

## Where the directory stands

| | |
|---|---|
| records published | **5,215** across 61 regions |
| with a link | **4,297** |
| deliberately link-free | 918 |
| links read or swept | **4,293** — every link in the corpus has now had at least a DNS+parking check |
| harmful or broken links removed | **318** |
| links repointed to a correct URL | **207** |

## Next — section 2 and section 3

**Section 2: the browser queue, 223 rows.** `scratch/hijack-screen/browser-queue-2026-08-15.tsv`.
JavaScript-rendered, Cloudflare-fronted and Facebook bot-walled pages a fetch physically cannot
read. Historically ~40% convert to a verified good link — roughly **90 recoveries**, the largest
remaining accuracy gain. Needs a browser session, not agents with fetch.

**Section 3: `tjjm-gym-websites-4`.** All three override files are nearly full — 544 B, 3,327 B and
2,911 B of headroom. Create the new snippet and add one `{%- render -%}` line to each of
`sections/tjjm-state-directory.liquid` and `sections/tjjm-gym-directory.liquid`. Do this **before**
the next batch that needs to write overrides.

Then: the 162 social/aggregator links (`scratch/park-sweep/social-deferred.tsv`), the identity pass,
and the 918 link-free records.
