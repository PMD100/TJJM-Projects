# Batch 32 — the parked-and-dead sweep. A new, much cheaper screen.

Session of 15 Aug 2026. Built as theme **KKK** (`154959118508`), **staged and awaiting publish**.
Overrides only. **Record counts cannot have moved.**
**Publish KKK `154959118508`.** JJJ `154958987436` becomes the rollback.

⚠️ **Theme-naming note.** JJJ `154958987436` was created for this batch but ended up MAIN before the
write landed, so batch 32 went into a fresh duplicate, KKK. JJJ is content-identical to III
(websites-1 `27ce9ee8b60612cf2fe28b2e1d18441c`) — that is the batch-31 state you already approved.
Nothing was lost and nothing incorrect went live.

---

## The method — because it is reusable and roughly five times cheaper

You found a GoDaddy for-sale lander on `5th St. Gym`. Reading all 2,286 unscreened pages would take
several sessions. Instead this pass **resolves each hostname and matches the A records against
parking infrastructure**, fetching a page only when the IPs look like a lander.

Fingerprints were **calibrated against domains we already knew were landers**, not guessed:

| IPs | operator | control domain |
|---|---|---|
| `15.197.148.33` + `3.33.130.190` | Afternic / GoDaddy for-sale | `5thstreetgym.com` |
| `76.223.54.146` + `13.248.169.48` | GoDaddy for-sale | `cageworx.com` |
| `13.223.25.84` + `54.243.117.197` | HugeDomains | `compassjiujitsu.com` |
| `208.91.197.27` | Confluence / Sedo | serves nothing at all |

**Two calibrations that prevented false positives** — both look like GoDaddy but front real schools:

- `15.197.225.128` + `3.33.251.168` — GoDaddy **web forwarding**. Seven domains on it were live schools.
- `76.223.105.230` + `13.248.243.5` — GoDaddy **Website Builder hosting**. Four of four were live schools.

**The IP is a filter, never a verdict.** The page still has to be fetched to tell a lander from a
forward. That distinction is the difference between this sweep and a blunt IP blocklist.

---

## Result — 1,777 of 2,286 swept

| verdict | n |
|---|---|
| OK — resolves, not parked | 1,726 |
| **DEAD** | **39** |
| **PARKED** | **12** |

**50 blanked** (51 found + `5th St. Gym`, minus 2 rejected by a gate — see below). **2.9% bad**,
in a population that batch 25's sampling predicted would be the cleanest left.

### The per-location 404 cluster is real and bigger than expected
Gracie Barra runs every school as a WordPress subsite at `graciebarra.com/<slug>/`. **Those subsites
are alive** — I fetched `graciebarra.com/edmonton-alberta-canada/` and it serves a full page with
address, phone and timetable. The ones that 404 are schools that **closed or left the network**:

`GB Oro Valley` · `GB Ellijay` · `Gracie Barra Boise` · `Gracie Barra Des Plaines` ·
`GB Libertyville` · `GB New Lenox` · `GB Burton` · `GB McAllen` · `GB Las Vegas`

Plus `UFC GYM Costa Mesa`, `UFC GYM Arlington`, `UFC GYM Norfolk` and `Roninjitsu Martial Arts`.
**Thirteen links that every DNS screen we have ever run passed cleanly**, because the brand domain
is perfectly healthy. We hold **93 Gracie Barra**, 36 UFC GYM, 46 Tiger Schulmann's, 18 Arashi-Do
and 8 Easton records — the rest of those still need the same exact-URL check.

### Two candidates the gates refused
`Jaguar BJJ` (NXDOMAIN) and `Catch MMA` already carry rows in `tjjm-gym-websites-3`, so gate C3
rejected adding a second entry. Blanking them means **editing that file**, not appending. Carried to
the next batch. This is the gate working as designed — a duplicate would have made the record fall
back to its stored URL.

---

## What was written

| file | was | now |
|---|---|---|
| `snippets/tjjm-gym-websites.liquid` | 16,653 B | **24,032 B · `228dd90a98f1b6fc3c08c7dcb88a64a2`** |

Byte-identical to the local build in `build-b32/`. **965 override entries, 685 blanking, zero
duplicate names.** Gates C5, C3, C11 and no-duplicates: all 50 passed.

⚠️ **`tjjm-gym-websites.liquid` is now full** — 24,032 B against a ~24,576 B rewrite ceiling, 544 B
spare. **The next batch must go in `tjjm-gym-websites-3`**, which has roughly 9,100 B free.
`tjjm-gym-websites-2` is also nearly full at 21,249 B.

### Structural guarantee
Only one file changed. Every record-bearing file in KKK is inherited unchanged from JJJ, so the
5,215 published records across 61 regions cannot have moved. Blanking overrides never change counts.

---

## Where the directory stands

| | |
|---|---|
| records published | **5,215** across 61 regions |
| with a link | **4,323** |
| deliberately link-free | 892 |
| links read or swept | **4,099** |
| harmful links removed | **292** |
| links restored to a correct URL | 190 |

## Next, in priority order

1. **Finish the sweep — 509 rows left.** Groups 2 and 5 stopped early (one when the machine slept,
   one interrupted); their completed rows are on disk and already counted. Worklists are
   `scratch/park-sweep/sweep-2.tsv` rows 184-381 and `sweep-5.tsv` rows 71-381.
2. **The brand per-location audit.** Fetch the exact URL for all 93 Gracie Barra, 36 UFC GYM, 46
   Tiger Schulmann's, 18 Arashi-Do and 8 Easton records. Expect a further 20-40 dead links. This is
   the highest yield-per-fetch job left.
3. **Fix `Jaguar BJJ` and `Catch MMA`** by editing `tjjm-gym-websites-3`.
4. **The browser queue — 223 rows** (`scratch/hijack-screen/browser-queue-2026-08-15.tsv`). JS-rendered
   and bot-walled pages a fetch cannot read. ~40% historically convert to a good link, so ~90 recovered.
5. **162 social/aggregator links** deferred from this sweep (`scratch/park-sweep/social-deferred.tsv`)
   — Facebook, Instagram, business.site, wixsite, Zenplanner. They cannot be parked, but many are
   bare brand homepages rather than the school's page, which is a wrong-entity problem.
6. **892 link-free records.** The "largest directory" work rather than the "safest directory" work.
