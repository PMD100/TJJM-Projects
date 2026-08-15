# NY curation worksheet — run of 5 Aug 2026

Companion to `ny-legacy-64-raw.txt` and `ny-186-matmade.tsv`. Steps 1–2 done and the
**mechanical** half of step 4 done.

**UPDATED 5 Aug 2026 (later run): step 3 is now COMPLETE** — all 64 legacy domains navigated and
all 43 screen-passes body-read. Results are in `ny-step3-findings.md`, and the rows that step 3
bears on are annotated inline below. **Step 5 is still not started, so nothing below is a
keep/suppress verdict.** Step 3 settles the state of a *link* (and in four cases a *city*), never
of a *school*.

## Provenance of every number here

- **MatMade side:** full gym-sitemap crawl, 5 Aug 2026. buildId **`Rd7MR1U4ddxhWYs6pVmUV`**,
  **re-derived this run from `__NEXT_DATA__`, not assumed** — unchanged from the 5 Aug record.
  Sitemap `/sitemap/gym-sitemap.xml` via `/sitemap.xml`: 7,311 URLs, 1,859,884 B.
  Crawled 7,310 (skipped `triton-fight-center`, known permanent 404) at concurrency 12,
  **0 errors**. Measured: **186 records** with `state.title === 'New York'`.
- **Legacy side:** audit-dump harness `154657063084`, raw stored `w`.
  Measured: **64 records, 0 suppressed**.

To regenerate the MatMade side: crawl `/_next/data/<buildId>/gyms/<slug>.json` →
`pageProps.gymData`, taking `city`/`state`/`affiliation` through
`rel = v => (v && v.data && v.data.attributes) ? v.data.attributes : null`.

## Step 1 checks

- **`/^[A-Z]{2}$/` on `state.title`** — **10 records** carry a 2-letter code instead of a full
  state name: 6 TX, 2 TN, 1 NV, 1 AZ. All have a null `postalCode`. **None are NY**, so they do
  not affect this import. Measured, not inferred. *Owed to TN (unshipped, 34), TX, NV, AZ: these
  records will be invisible to a `state.title === '<Full Name>'` filter.*
- **NY ZIPs filed under another state** — the range scan (10001–14975, 00501, 00544, 06390)
  returned exactly one hit, `10th Planet Berlin` /Germany, ZIP 13587. That is a German postal
  code colliding with the NY numeric range, i.e. a **false positive**. **No genuine cases.**
- **`city` extracted through `rel()`** throughout. 70 distinct city strings across the 186.

## Step 2

BEFORE baseline duplicated from MAIN/YY **before any change**:
`gid://shopify/OnlineStoreTheme/154661355692`
("BEFORE baseline — MAIN/YY snapshot (pre-NY import)"). This is the honest "before" side for the
step-9 sweep. The audit-dump harness `154657063084` is **not** usable as a baseline (post-XX).

---

## Finding that contradicts a standing rule — the name check works here

RULES §4 and the handoff both record **"the name-only check found 0 of 40 domain collisions —
never run it alone."** That was measured across the **27 shipped** states.

Measured on NY, 5 Aug: **15 domain collisions and 10 name collisions**, and **4 of the 10 name
hits are invisible to the domain check** because the two records carry different domains:

| pair | MatMade domain | legacy domain |
|---|---|---|
| `Jungle Gym Martial Arts` /The Bronx vs /New Rochelle | junglegymbronx.com | junglegym.com |
| `Modern Martial Arts NYC` /Manhattan vs /New York | 4blackbelt.com | modernmartialarts.com |
| `Seven Tigers Martial Arts Academy` /Cheektowaga (both) | martialartsbuffalo.com | seventigersmartialarts.com |
| `The Dojo NYC` /Ridgewood vs /Brooklyn | thedojonyc.com | thedonycny.com |

**Bound to its method, so the method's limits are visible:** the 0-of-40 result was measured on
states where a curator had *already* imported MatMade and reconciled names. NY is unshipped, so
its legacy names have never been reconciled against MatMade's. **Inference, not measurement:** on
an unshipped region the name check should be expected to fire, and the "never run it alone"
instruction is about *sufficiency*, not about skipping it. Both were run here.

**Not checked:** whether the other 33 unshipped regions show the same pattern. n=1.

---

## Collision inventory — CANDIDATES ONLY, no verdicts

### A. Domain collisions, MatMade × NY legacy (15)

Multi-tenant hosts excluded from matching per RULES §2 blind spot 3.

| # | domain | MatMade record | NY legacy record | shape |
|---|---|---|---|---|
| A1 | andersonsmartialarts.com | Anderson's Martial Arts Academy /New York @ 12 E 14th St | Anderson's Martial Arts Academy /New York | same name, same city |
| A2 | buffalobjj.com | Buffalo Brazilian Jiu-Jitsu Academy /West Seneca @ 22 French Lea Drive | Buffalo Brazilian Jiu Jitsu Academy /Buffalo | cross-city |
| A3 | clockworkbjj.com | Clockwork Jiu Jitsu /New York @ 650 Broadway | Clockwork Brazilian Jiu-Jitsu /New York | same city |
| A4 | studiox.nyc | Fabio Clemente StudioX BJJ /New York @ 6 St Marks Pl | Studio X /New York | same city |
| A5 | gentleartstudio.com | Gentle Art Studio – Lotus Club BJJ & Wellness Center /New York @ 23-17 Broadway | Gentle Art Studio Lotus Club /Astoria | **MatMade city looks wrong** — ZIP 11106 is Astoria |
| A6 | kiotobjj.com | Kioto Brazilian Jiu-Jitsu /Sayville @ 205 West Main St | Kioto Brazilian Jiu Jitsu /New York | cross-city |
| A7 | limixedmartialarts.com | Long Island MMA & Fitness Center /Lindenhurst @ 1 Gear Ave | Long Island MMA /Lake Grove | cross-city |
| A8 | marcelogarciajj.com | Marcelo Garcia Jiu Jitsu /New York @ 250 W 26th St | Marcelo Garcia Academy /New York | same city |
| A9 | renzograciebayside.com | Renzo Gracie Bayside /Bayside @ 45-58 Bell Blvd | Renzo Gracie Bayside /Bayside | same name, same city |
| A10 | renzograciebrooklynnyc.com | Renzo Gracie Fight Academy /Brooklyn @ 100 Bayard St | Renzo Gracie Brooklyn /Brooklyn | same city, name differs |
| A11 | marloncoloradobjjnyc.com | Rocian Gracie Jr. Prof Marlon Colorado /Queens @ 47-10 32nd Pl | Marlon Colorado BJJ NYC /Sunnyside | Sunnyside **is** in Queens |
| A12 | roninathletics.com | Ronin Athletics /New York @ 265 Madison Ave | Ronin Athletics /New York | same name, same city |
| A13 | serrabjj.com | Serra Brazilian Jiu-Jitsu Academy - Huntington /Huntington, **no address** | Serra BJJ Academy /Levittown | see B/C |
| A14 | serrabjj.com | Serra Brazilian Jiu-Jitsu Academy - Levittown /Levittown, **no address** | Serra BJJ Academy /Levittown | see B/C |
| A15 | synthesisbjj.com | Synthesis Brazilian JiuJitsu \| BJJ Rochester NY 14610 /Rochester | Synthesis Brazilian Jiu-Jitsu /Rochester | same city; **MatMade name is keyword-stuffed and its address ZIP (14623) contradicts its own ZIP field (14610)** |

### B. Name collisions not caught by domain (4)

Listed in the table above.

### C. MatMade-internal shared domain (5 groups)

- `serrabjj.com` — **Huntington and Levittown stubs**: no address, no ZIP, and **identical**
  phone and identical rating/review counts (4.6 / 36) to each other. Strong stub signal; the
  addressed record `Serra BJJ Academy` /Levittown (serrabjjacademy.com, 2949 Hempstead Tpke) is
  a separate MatMade record. **Candidate, not a verdict** — read the body.
- `bkwingtsun.com` — `Brooklyn BJJ` /157 Columbia St and `Brooklyn Wing Tsun` /808 Union St.
  Different addresses, different phones. Smells like a wrong-entity link on one of them
  (RULES §4: a wrong URL can resolve perfectly and belong to someone else).
- `mmanewyorkcity.com` — Modern Martial Arts NYC Upper Eastside and Upper West Side. Note the
  **UWS record's URL path says `brazilian-jiu-jitsu-east-side`** — link/record mismatch.
- `tsk.com` — **23 Tiger Schulmann's NY locations**, every one with a per-location URL. The NJ
  precedent (METHOD CORRECTION 3) is that per-location URLs are usually correct — 17 of 18 NJ
  records were fine. **Zero of these 23 are in the NY legacy set.** Largest single block of
  net-new.
- `ufcgym.com` — UFC GYM Long Island (per-location URL) and UFC GYM Park Slope (**brand root** —
  the RULES §2 blind-spot-4 defect class).

### D. MatMade-internal shared name (1)

`Bronx Martial Arts Academy` appears **twice**, both /The Bronx, at 1051 Allerton Ave
(bronxmartialarts.com) and 1621 Crosby Ave (bronxjiujitsu.com). Two sites, two addresses, one
name. Read both bodies.

### E. Same address statewide (1) — **and this scan has a known false negative**

`Modern Martial Arts NYC` /Manhattan @ 103 West 73th St [10023] and
`Modern Martial Arts NYC Upper West Side` /New York @ 103 W 73rd St [10023].

⚠️ **Do not read "n=1" as "there is one."** The first pass of this scan returned **0** because it
keyed on city, and NYC boroughs appear as Manhattan / New York / Queens / The Bronx
interchangeably; the second returned 0 until directionals (W↔West) were folded. The scan is
**one normalisation bug away from silence** and has been wrong twice already in this session.
Treat E as a lower bound.

---

## Defect classes measured on the 186 MatMade records

| class | n | note |
|---|---|---|
| **name contains `\|`** | **2** | **BLOCKING** — `\|` is a field separator (RULES §5). `Sas Jiu Jitsu Syracuse \| BJJ Syracuse NY 13206`, `Synthesis Brazilian JiuJitsu \| BJJ Rochester NY 14610`. Both must be renamed before they can be written at all. |
| name contains `~` | 0 | |
| no website | 13 | |
| no address | 3 | Serra Huntington, Serra Levittown, Victor CTC |
| scheme-less `w` | 2 | `www.716bjj.com`, `www.peakjj.com` |
| mixed-case host (raw string) | 0 | tested on the raw string, not `URL.hostname` (METHOD CORRECTION 4) |
| URL carries a query string | 10 | includes tracking tokens and booking-widget deep links |
| multi-tenant / non-site host | 16 | see below |
| en/em-dash in name | 3 | |

### The 16 multi-tenant / non-site hosts

`app.squarespacescheduling.com` · `facebook.com` · **`safebrowse.io`** · `sparkpages.io` ·
`icsportsmassage.com` · `youtube.com` · `form.123formbuilder.com` · `sites.google.com` (bare
root) · `kravmaga.fithit.com` · `places.singleplatform.com` ×2 · `mindbodyonline.com` ×3 ·
`bigappleguide.wixsite.com` · `instagram.com`

**`Igor Gracie Academy` is the notable one:** its stored `websiteURL` is a **safebrowse.io
interstitial wrapper** with the real target (`igorgraciejiujitsu.com`) as a query parameter and a
token attached. That is a defect class not previously recorded in this project. The NY legacy
record already carries the clean `https://igorgraciejiujitsu.com` (A-list domain collision would
have missed this pair, because the wrapper host is not the school's host — **it only surfaced via
the name check**).

### Non-gym tell — third CTC data point

`Victor CTC` /Victoria: **no address, no postalCode**, `ctconline.com`, rating 3.2. The handoff's
"STILL TRUE" records *missing `postalCode` is a non-gym tell — 2-for-2 in Oregon, both CTCs*.
This is a **third** CTC with the same signature. Still needs the body read before it is a verdict,
but the prior is strong and it would take the tell to 3-for-3.

Also note the slug is `victor-ctc-victor-new-york` while `city` resolves to **"Victoria"** — the
city relation is wrong, not just lowercase.

### City-string hygiene on the MatMade side

Four records carry a lowercase/underscored city from the relation: `point_lookout`,
`poughkeepsie`, `sayville`, `victor`. One is ALL CAPS: `SYRACUSE`. Boroughs are inconsistent
(`Manhattan`, `New York`, `Queens`, `The Bronx`, `Astoria`, `Ridgewood`, `Forest Hills`,
`Williamsburg`). **A city-normalisation pass is required before the snippet is generated**, and
the choice of borough convention has to match what the existing 64 legacy records use
(they use `New York`, `Brooklyn`, `Astoria`, `Long Island City`, `Bayside`, `Sunnyside`).

---

## Yield

Oregon, the single prior observation: 136 MatMade candidates → 117 imported → **×0.86**, which
falls **outside** the recorded band of ×0.50–0.85.

NY has **186** candidates. The band predicts 93–158; the Oregon point predicts ~160. This run is
the **second** data point and the band should be rewritten from n=2 with both values stated, not
smoothed.

## Step 3 outcomes that bear directly on the rows above

Added 5 Aug 2026 (later run). Full detail and method in `ny-step3-findings.md`.

- **A2 `buffalobjj.com`** — LIVE and real (Prof. Chuck Anzalone). Also the **only `http://`
  record in the NY legacy 64**, and it upgrades to `https://`. The cross-city question
  (legacy /Buffalo vs MatMade /West Seneca) is **still open** — the site was not read for its
  street address.
- **A6 `kiotobjj.com`** — LIVE. Body says **96 Biltmore Ave, Oakdale, NY**. So the **legacy city
  `/New York` is wrong**, and MatMade's `/Sayville` @ 205 West Main St **contradicts the site's own
  address**. One of the two addresses is stale; unresolved.
- **A13 / A14 `serrabjj.com`** — DEAD, but the two stubs are **not** the same case. Serra's own
  site lists **two** academies: Huntington (365 West Jericho Tpke, 11743) and Levittown (2949
  Hempstead Tpke). So **Huntington is a real school missing an address**, while **Levittown
  duplicates** the addressed `Serra BJJ Academy`. The identical phone/rating/review pair was a
  *stub signal that pointed the wrong way on one of the two* — a caution for reading that signal.
- **B-list `Jungle Gym Martial Arts`** — the legacy link `junglegym.com` is a **UK playground
  equipment retailer**. MatMade's per-location domains (`junglegymnewroc.com`,
  `junglegymbronx.com`) are the real ones. Resolves as a **link fix**, not a suppression.
- **B-list `Modern Martial Arts NYC`** — the legacy link `modernmartialarts.com` is a **book
  promo site**. Worse, the separate legacy record `Vitor Shaolin BJJ NYC` points at
  `bjjnewyorkcity.com`, which is **Modern Martial Arts, Times Square**. The cluster now has two
  broken legacy links, five MatMade records and the E same-address pair in one knot —
  **adjudicate it as a whole, never row by row.**
- **B-list `Seven Tigers Martial Arts Academy`** — both links still unusable. Aggregators say
  open, at the MatMade address and phone, offering **Karate / Praying Mantis Kung Fu, not BJJ**.
  Aggregator evidence only, so a **prior, not a result**.
- **`Igor Gracie` safebrowse.io wrapper** — the wrapped target `igorgraciejiujitsu.com` opens live
  and real, and the **legacy record already stores it clean**. Keep legacy's URL, discard the
  wrapper.
- **Two live sites may not be BJJ schools at all:** `Swan's Martial Arts Academy` /Cheektowaga
  (Family Kempo Karate) and `Rochester Fitness Martial Arts` /Rochester (Shaolin Kung Fu, now at
  `rochesterkungfu.com`). Landing pages only; not verified.

## What has NOT been done

- ~~**Step 3 not started.**~~ **DONE 5 Aug 2026 (later run)** — 64 of 64 navigated, 43 of 43
  screen-passes opened. See `ny-step3-findings.md`. *Struck rather than deleted: the numbers below
  were all generated before any domain had been opened, which is why none of them is a verdict.*
- **Step 5 not started.** No **school** has been adjudicated. **Every row above is a candidate
  generated by a string signal, and the acronym pass went 1-for-3 on 6 Aug.** Nothing here is
  evidence about any school.
- **The 186 MatMade domains have never been probed or opened.** Step 3 covered the legacy side
  only. The 16 multi-tenant hosts, the 5 shared-domain groups and the 23 `tsk.com` per-location
  URLs are all unverified.
- **7 school searches are owed** — the 7 legacy records whose domains passed the screen but reach
  no usable site (CNY MMA, Ithaca BJJ, Kings Combat, Jungle Gym, Modern Martial Arts NYC,
  Savarese, Maxum). A dead link is not a dead gym; backlog item 2 got that wrong in 2 of 6 cases.
- **Blind spot 1 (never-imported duplicates) is untouched** and unreachable by any diff above.
- No check yet on whether any of the 186 is already in the directory **under a different region**.
