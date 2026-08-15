# NY step 3 — COMPLETE. All 64 legacy domains navigated (5 Aug 2026)

**Status: step 3 is DONE. Step 5 (school-level verdicts) is NOT started.**
**Nothing has been written to any theme this run.** Production untouched. The only store change
remains the inert duplicate `154661355692` (the BEFORE baseline), created last run.

Supersedes the partial version of this file. The previous run navigated 4 of 64; this run
navigated the remaining 60 and opened all 43 screen-passes.

---

## Carry-over state, re-verified rather than trusted

- **buildId `Rd7MR1U4ddxhWYs6pVmUV` — RE-DERIVED** from `__NEXT_DATA__` this run, per the brief's
  instruction not to trust the recorded value. Unchanged.
- **Sitemap re-crawled:** `/sitemap/gym-sitemap.xml` via `/sitemap.xml`, **7,311 URLs**, crawled
  **7,310** at concurrency 12, **0 errors** (skipped `triton-fight-center`, known permanent 404).
  **Measured: 186 records** with `state.title === 'New York'`. Reproduces the previous run exactly.
- **The BEFORE baseline is still valid.** MAIN/YY `154658242732` has `updatedAt`
  **2026-08-05T22:37:33Z**; baseline `154661355692` was created **2026-08-05T23:10:54Z**, i.e.
  *after* MAIN's last modification. Nothing has been written to MAIN since the snapshot, so the
  step-9 "before" side is honest. **Measured from the themes query, not assumed.**
- **The 186 MatMade records are now persisted** to `ny-186-matmade.tsv` (29,079 B, 11 columns,
  raw `websiteURL` per METHOD CORRECTION 3). They previously existed nowhere on disk — Oregon had
  `oregon-136-matmade.tsv`, NY had no equivalent, so steps 4–5 would have forced a third crawl.

### Independent re-measurement of the 186 — every defect count reproduces

Re-derived from the fresh crawl, not copied from the worksheet:

| class | worksheet | this run | agrees |
|---|---|---|---|
| records | 186 | 186 | ✓ |
| name contains `\|` | 2 | 2 (same two names) | ✓ |
| name contains `~` | 0 | 0 | ✓ |
| no website | 13 | 13 | ✓ |
| no address | 3 | 3 (same three records) | ✓ |
| scheme-less `w` | 2 | 2 (`www.716bjj.com`, `www.peakjj.com`) | ✓ |
| `w` carries a query string | 10 | 10 | ✓ |
| mixed-case host (raw string) | 0 | 0 | ✓ |
| en/em-dash in name | 3 | 3 | ✓ |
| distinct city strings | 70 | 70 | ✓ |
| 2-letter `state.title` (corpus-wide) | 10 | 10 | ✓ |

⚠️ **Bound to its method:** this is the *same method* re-run on the *same population*. It
validates the transcription and the crawl, **not the method**. Per RULES §8, a second application
of a method that was already wrong would agree with itself. It rules out transcription error only.

*New, incidental:* **`affiliation` is null on all 186 NY records**, as it was on all 136 Oregon
records. That takes the "STILL TRUE" note *`programs`/`affiliation` are dead as curation signals*
from n=136 / 1 state to **n=322 / 2 states**. Still both unshipped-import states, so it is not yet
evidence about shipped ones.

*New, incidental:* the 10 corpus-wide 2-letter-`state.title` records are **not randomly
distributed** — 8 of 10 are Renzo Gracie or Insight BJJ affiliate records
(`renzo-gracie-reno-reno-nv`, `renzo-gracie-sat-san-antonio-tx`, `renzo-gracie-spring-hill-…-tn`,
`insight-bjj-bastrop-…`, `insight-bjj-brenham-…`, `renzo-gracie-taylor-…`,
`insight-bjj-la-grange-…`, `renzo-gracie-columbia-…-tn`), plus `marcelo-garcia-dallas-dallas-tx`
and `sonoran-brazilian-jiu-jitsu-tucson-az`. All 10 have a null `postalCode`. **Inference, not
measurement:** this looks like one upstream import batch rather than ten independent slips, which
means the defect is likely to recur as a *block* in TX (352) and TN (34, unshipped).

---

## Headline: the no-cors screen was wrong 4 times in 21 — in the *other* direction

The previous run established that parked pages and directories score LIVE (false pass). This run
measured the opposite error on the whole failure set.

**Of the 21 domains that FAILED the no-cors screen, 4 were not dead:**

| domain | what navigation actually found |
|---|---|
| `binghamtonbjj.com` | **LIVE** — 301s to `broomecountymartialarts.com`, "Broome County Martial Arts — Binghamton NY \| BJJ, Muay Thai, Boxing". Real school, renamed. |
| `paxibellum.com` | **LIVE at the apex.** `www.paxibellum.com` fails TLS; `paxibellum.com` serves "Paxibellum Jiu Jitsu". The record stores the **www** form. |
| `rochesterfitnessmartialarts.com` | **LIVE** — 301s to `rochesterkungfu.com`, "Rochester Shaolin Kung Fu Training Academy \| Rochester Fitness Martial Arts". |
| `itcny.com` | **REACHABLE BUT BROKEN** — see the new sub-class below. |

**Measured false-negative rate of the screen on NY: 4 of 21 (19%).** Combined with the known
false-positive direction, the screen is unreliable both ways on this state. **Use it to order the
work; never to conclude.** That instruction is now backed by measurements in both directions
rather than one.

### NEW sub-class — "reachable but broken" is a third state, not a shade of dead

`location.host === 'chromewebdata'` is conclusive for **NXDOMAIN / connection failure**. It does
**not** cover two states found this run, and in both the browser tooling behaves differently:

1. **TLS interstitial.** `itcny.com` and `www.paxibellum.com` render Chrome's *"Privacy error"*
   page. **`javascript_tool` cannot attach to it** — the call fails with *"Cannot attach to this
   target"*. That error is a **signal, not a tool failure**: treat "cannot attach" + title
   "Privacy error" as a distinct outcome and re-probe the opposite scheme and the apex/www
   alternate before concluding anything.
2. **Server up, site broken.** `http://www.itcny.com` returns **IIS 8.5 error 500.19**. The domain
   resolves, a server answers, and there is no site. Dead as a *link*; says nothing about the
   *school*.

⚠️ **Put this next to the action:** a probe loop that only tests `host === 'chromewebdata'` will
score both of these as LIVE and move on. Test for the interstitial and for an empty/error body too.

### Final disposition of the 21 screen-failures

**DEAD by navigation (conclusive `chromewebdata`), n=17:**
`serrabjj.com` · `www.seventigersmartialarts.com` · `www.thedonycny.com` · `nextevolutionma.com`
(these four navigated last run) · `brianbeury.com` · `albanybjj.com` · `clobberbjj.com` ·
`elitefitnessmartialarts.com` · `fightsporttrainingcenter.com` · `bptwestchester.com` ·
`joncalestinebjj.com` · `jiulivrenyc.com` · `middletownbjjny.com` · `plattsburghbjj.com` ·
`watertownbjjny.com` · `precisionbjj.com` · `newburghbjj.com`

**NOT dead, n=4:** the four in the table above.

---

## All 43 screen-passes opened — 7 do not reach a usable school site

Step 3 exists for exactly this. **7 of 43 (16%) of the domains that PASSED the screen are not the
school's site.** Every one would have been scored LIVE by any probe that does not read the body.

| # | legacy record | stored domain | what the body actually says |
|---|---|---|---|
| 1 | **CNY MMA** /Baldwinsville | `cnymma.com` | ⚠️ **INDONESIAN ONLINE-GAMBLING SPAM.** Title *"MANCINGDUIT - Situs Slot Online Raja Slot Gacor…"*. The domain lapsed and was re-registered as an SEO gambling site. **The live directory currently links customers to this.** |
| 2 | **Ithaca BJJ** /Ithaca | `ithacabjj.com` | **PARKED.** Redirects to `/lander`; empty title, empty body. Classic domain-parking lander. |
| 3 | **Kings Combat** /Brooklyn | `kingscombat.com` | **FOR SALE.** Redirects to `forsale.godaddy.com/forsale/kingscombat.com` — "for sale! …$1,988, or Lease to Own". |
| 4 | **Jungle Gym Martial Arts** /New Rochelle | `junglegym.com` | **WRONG ENTITY.** A **UK wooden-playground-equipment retailer** — "climbing frames", prices in £. |
| 5 | **Modern Martial Arts NYC** /New York | `modernmartialarts.com` | **WRONG ENTITY.** A book-promo site: *"Modern Martial Arts Warrior Training is a unique book by James Dolmage"*. |
| 6 | **Savarese BJJ Academy** /Lynbrook | `savarese.com` | **WRONG ENTITY.** *"Savarese Software Research Corporation"* — a software company. |
| 7 | **Maxum BJJ Long Island** /Huntington | `maxumbjj.com` | **UNPUBLISHED.** *"Site not found — This site is not published or does not have a domain assigned to it."* Site-builder placeholder. |

**The remaining 36 resolved to a live, real martial-arts site.** Three of those 36 carry a defect
that is about the *record*, not the domain:

- **`Vitor Shaolin BJJ NYC` /New York → `bjjnewyorkcity.com`** — the site is live and real but it
  is **Modern Martial Arts**, "in the heart of Times Square", Manhattan. **Zero mentions of Vitor
  Shaolin anywhere in the body.** This is a name/entity mismatch, not a dead link, and it collides
  with the Modern Martial Arts cluster below.
- **`Bellmore Kickboxing Academy` /Bellmore** — `bellmorekickboxing.com` 301s to
  **`bellmorekickboxingmma.com`** (2551 Merrick Road, Bellmore 11710). Link fix.
- **`Buffalo Brazilian Jiu Jitsu Academy` /Buffalo** — `http://www.buffalobjj.com` upgrades to
  **`https://`** and is live and real (Prof. Chuck Anzalone). This is the **only `http://` record
  in the NY legacy 64**; the scheme should be corrected in the same pass.

### Two live sites that may not belong in a BJJ directory

Recorded as candidates, **not verdicts** — neither has been checked for a BJJ program beyond the
landing page, and RULES §4 forbids concluding from a landing page alone:

- **`Swan's Martial Arts Academy` /Cheektowaga** → live, but the body is **Family Kempo Karate**.
  No BJJ or grappling seen on the home page.
- **`Rochester Fitness Martial Arts` /Rochester** → live at `rochesterkungfu.com`, **Shaolin Kung
  Fu**. Same question.

*(The MatMade side has the same issue at least once — `Kim's TaeKwonDo` /Warren, and
`Iaido Kendo Club`, `Westchester Judo Club`, `Church Street Boxing Gym`, `Krav Maga Academy`,
`Evolution Muay Thai`, `Jiu Jitsu Massage` are all in the 186. **Not scanned systematically.**)*

---

## The four named step-3 debts — all four closed

**1. `kiotobjj.com` opened — it resolves the Kioto tangle and contradicts the legacy city.**

Body: **"Brazilian Jiu-Jitsu Oakdale | #1 BJJ Gym Long Island"**, **96 Biltmore Ave, Oakdale, NY**,
631-319-8479, Professor Milton Regis / Professor Melissa Regis.

- Legacy `Kioto Brazilian Jiu Jitsu` **/New York** on `kiotobjj.com` — **the city is wrong.** The
  school is on Long Island, not in New York City.
- MatMade `Kioto Brazilian Jiu-Jitsu` **/Sayville** @ 205 West Main St on `kiotobjj.com` — right
  region, **but the site's own address is Oakdale, 96 Biltmore Ave.** Sayville and Oakdale are
  adjacent; one of the two addresses is stale. **Not resolved — needs the school's contact page.**
- MatMade `Kioto Brazilian Jiu Jitsu / NEMMAA` /New York @ 1786 3rd Ave is a **different school**
  (Next Evolution, confirmed last run) that runs a Kioto-affiliated *program*.

**2. Serra Huntington — RESOLVED, and it is a real second academy.**

Read from the school's own site body (`serrajitsu.com/contact-us.html`), not an aggregator:
**"Huntington Academy — 365 West Jericho Tpke., Huntington, NY 11743"** and **"Levittown Academy —
2949 Hempstead Tpke."** Two academies.

- MatMade `Serra Brazilian Jiu-Jitsu Academy - Huntington` is a **real school** whose record is
  merely missing its address. **Do not treat it as a stub to drop.**
- MatMade `Serra Brazilian Jiu-Jitsu Academy - Levittown` **duplicates** the addressed
  `Serra BJJ Academy` /Levittown (2949 Hempstead Tpke). That is the one that is redundant.
- Both stubs carry the dead `serrabjj.com`. Live domains are `serrabjjacademy.com` and
  `serrajitsu.com`.
- *Loose thread:* aggregators also mention a Serra **Bayside**. Unverified, and the legacy set
  already has a *Renzo Gracie* Bayside. Not the same thing; not chased.

**3. Igor Gracie safebrowse.io wrapper — target confirmed clean.**

`igorgraciejiujitsu.com` opens live and real ("Igor Gracie Jiu Jitsu Academy"). The **legacy
record already stores this clean URL**; the MatMade record stores a `safebrowse.io/warn.html`
interstitial wrapper carrying it as a query parameter plus a token. **Keep the legacy URL, discard
the wrapper.** No new lookup needed.

**4. Seven Tigers as a *school* — searched, still NOT settled. Be careful with this one.**

Both of its stored links remain unusable (legacy domain dead; MatMade domain is the Buffalo
Niagara Martial Arts Festival event site). Searching found **no page owned by the school**.

- Multiple aggregators (Yelp, superpages, wellnessliving, dojos.info, Zaubee) list it as **open**
  at 3015 Genesee St, Cheektowaga 14225, phone 716-893-4942 — which **matches the MatMade record
  exactly** — and describe the offering as **Karate and Praying Mantis Kung Fu**, not BJJ.
- ⚠️ **This is aggregator evidence, which RULES §4 says never to trust** — `evolutionlowell.com`
  had three directories agreeing on an address that no longer existed. So: **prior, not result.**
- `7tigers-jidokwan.com` surfaced in search and is **NOT this school** — it is "7 Tigers Taekwondo
  and Hapkido" in **Charlottesville, Virginia**. Checked and rejected; a name-shaped false
  positive of exactly the kind the acronym pass produced at 1-for-3 on 6 Aug.

---

## New for the collision inventory: the Modern Martial Arts cluster is worse than recorded

The worksheet lists `Modern Martial Arts NYC` as one name-only collision pair. Step 3 shows the
cluster has **two independently broken legacy links** pointing into it:

| record | side | stored link | state |
|---|---|---|---|
| `Modern Martial Arts NYC` /New York | legacy | `modernmartialarts.com` | **wrong entity** (a book) |
| `Vitor Shaolin BJJ NYC` /New York | legacy | `bjjnewyorkcity.com` | **live, but it is Modern Martial Arts Times Square** |
| `Modern Martial Arts NYC` /Manhattan @ 103 West 73th St | MatMade | `4blackbelt.com` | untested |
| `Modern Martial Arts NYC Upper West Side` /New York @ 103 W 73rd St | MatMade | `mmanewyorkcity.com/…-east-side` | path/record mismatch (already noted) |
| `Modern Martial Arts NYC Upper Eastside` | MatMade | `mmanewyorkcity.com/locations/upper-eastside` | untested |
| `Modern Martial Arts Astoria` | MatMade | mindbodyonline wrapper | untested |
| `Modern Martial Arts Tribeca` | MatMade | mindbodyonline wrapper | untested |

**Do not adjudicate any one of these in isolation.** Two legacy records, five MatMade records, at
least three distinct domains and one same-address pair (E in the worksheet) all sit in one knot.
**Not resolved this run** — it needs the whole cluster read together in step 5.

---

## Running tally — step 3 owes nothing further

- 64 of 64 legacy domains navigated. ✓
- 43 of 43 screen-passes opened and body-read. ✓
- All four named debts closed (one closed as *unresolvable from links alone*). ✓

## What this run did NOT check

Stated explicitly, because silence reads as absence of a problem.

- **No keep/suppress verdict was made on any record.** Step 5 is untouched. Everything above
  settles the state of a **link** (and in four cases a **city**), never of a **school**.
- **None of the 186 MatMade domains was probed or opened.** Step 3 covered the legacy side only.
  The 16 multi-tenant hosts, the 5 shared-domain groups and the 23 `tsk.com` per-location URLs are
  all still unverified.
- **The 7 unusable screen-pass domains have NOT been converted into school searches.** Per the
  backlog item-2 warning, a dead link is not a dead gym: CNY MMA, Ithaca BJJ, Kings Combat, Jungle
  Gym, Modern Martial Arts NYC, Savarese and Maxum each still need the school looked for
  independently. **7 searches owed.** Note `cnyjiujitsu.com` (Haven Jiu Jitsu /Syracuse) advertises
  **"Syracuse & Baldwinsville"** — CNY MMA's city — so that pair should be read together.
- **Swan's and Rochester Kung Fu were not checked for a BJJ program**, only seen on the landing
  page. No systematic non-BJJ scan was run over either side.
- **The Modern Martial Arts / Vitor Shaolin cluster was not adjudicated.**
- **Kioto's Oakdale-vs-Sayville address conflict was not resolved.**
- **Blind spot 1 (never-imported duplicates) remains untouched** and is unreachable by anything
  done here.
- **No check yet on whether any of the 186 is already in the directory under a different region.**
- **Nothing was written to any theme, snippet, metafield or file** other than this folder's
  working files.
