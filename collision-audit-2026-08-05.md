# Domain collision re-audit — all 27 shipped states (5 Aug 2026)

Backlog item 5, run corpus-wide. **Nothing was changed.** Everything below is a decision queue.

## Method

A scratch theme (`SCRATCH — collision audit`, `154652311724`, duplicated from MAIN) carries a
dump section `sections/tjjm-audit-dump.liquid` + `templates/page.tjjmaudit.json`. It reuses the
state-directory's own code-resolution and record-parsing logic, but emits every record for the
region as `SRC|REMOVED|name|city|website` — **including suppressed records**, which no rendered
page shows. Fetched via `/pages/<handle>?view=tjjmaudit&preview_theme_id=154652311724`,
concurrency 6, all 61 regions. The intersection was computed in-browser; only findings were
read back.

Domains normalised as: add scheme if missing → `URL.hostname` → lowercase → strip leading `www.`.
Multi-tenant hosts (facebook, instagram, mindbody, squareup, linktr, site builders) excluded from
matching, or every Facebook-linked gym would false-positive against every other.

### Reconciliation (this is what makes the numbers trustworthy)

- Dump total across 61 regions: **4,547** live records.
- Minus **27** for the NE/NL double count — Newfoundland records are miscoded `NE`, and the dump
  deliberately does not apply the section's city-based split, so NE and NL each report the union
  of 12 + 15. Every other region matched `tjjm-region-index` exactly.
- **4,547 − 27 = 4,520.** Matches the published total.
- Oregon dumps 132 = 15 legacy + 117 imported; rendered page is 117 + `Ashland BJJ` = **118**,
  with 14 legacy suppressed. Consistent.

### Control check

The audit independently rediscovered **`oregonbjj.com`**. It did **not** surface `ashlandbjj.com`
— correctly: that MatMade duplicate was never imported, so only one record in the corpus carries
the domain and there is nothing to intersect. That is a true null, not a miss.

**Structural consequence:** wherever the standing rule was applied as written (keep legacy, never
import the MatMade duplicate), the collision is **invisible to this audit** — the second record
does not exist in the theme. This pass can only see collisions where both records were imported.
Those cases can only be found by re-diffing against MatMade source data, not against the theme.

## Headline

| | |
|---|---|
| Name collisions (`legacyNames ∩ keptNames`) | **0** |
| Domain collisions (`legacyDomains ∩ keptDomains`) | **40**, across 19 states |

The name-only check was blind to every single one. That is the handoff's hypothesis confirmed at
corpus scale.

Of the 40: **11 both-live**, **29 legacy-suppressed**. Zero MatMade-suppressed, for the structural
reason above.

---

## Group A — 11 both-live (same domain, two records currently rendering)

**8 of these are not collisions at all.** They are multi-location brands where each location links
to the brand root instead of its own location page:

| state | domain | locations sharing it |
|---|---|---|
| NJ | `tsk.com` | 18 Tiger Schulmann's |
| CO | `eastonbjj.com` | 8 Easton Training Center |
| AZ | `graciebarra.com` | 5 Gracie Barra |
| NV | `gracielasvegas.com` | 3 Gracie |
| FL | `americantopteam.com` | ATT Davie + ATT Coconut Creek |
| LA | `ufcgym.com` | New Orleans + Baton Rouge |
| TX | `revolutiondojo.com` | Houston + Cypress |
| TX | `cjjftx.com` | Caveirinha Prosper + CJJF West Frisco |

This is the **same defect class as backlog item 3**, not a duplication problem — 38 real, distinct
schools all pointing at a brand homepage. The handoff already fixed one instance of exactly this
(`Gracie Barra Sw Portland` → `graciebarra.com/sw-portland-or/`). Resolving each to its location
page is a link-quality task, not a curation decision, and needs no adjudication.

**3 need investigation** — these are genuine same-domain anomalies:

1. **TX `rodrigopinheirobjj.com`** — `Rodrigo Pinheiro BJJ` /San Antonio *vs*
   `Unconventional Performance & Training` /New Braunfels. Different entity names, different
   cities, shared domain, neither suppressed. **This is the exact shape of the Oregon
   `oregonbjj.com` case.** One of the two records has the wrong website. Highest priority.
2. **CA `reddingselfdefense.com`** — `Combat Base Shasta/ Mendes Brazilian Jiu-Jitsu` *vs*
   `MZ Brazilian Jiu-Jitsu`, both /Palo Cedro. Same city, same domain, unrelated names — likely
   one school listed under both a former and current name. Note the domain says Redding while
   both records say Palo Cedro.
3. **FL `bjjorlando.com`** — `Fabin Rosa BJJ Altamonte Springs` *vs*
   `Fabin Rosa Brazilian Jiu Jitsu Academy` /Orlando. Two locations, or one relocated school
   listed twice.

---

## Group B — 29 legacy-suppressed, needing directional review

In all 29 the legacy record was suppressed and the MatMade record kept — i.e. the standing rule
was **not** applied. In most cases that produced the right outcome anyway, because the legacy
record was a generic `<City> BJJ` stub. But the Oregon lesson is that the direction has to be
checked, not assumed.

### B1 — 9 high risk: the surviving record is in a DIFFERENT city

These are the cases where suppressing the legacy record may have deleted a real school and kept
one that is somewhere else entirely. **This is the Oregon `oregonbjj.com` failure mode.**

| state | domain | suppressed | kept | note |
|---|---|---|---|---|
| VA | `topgamebjj.com` | Top Game BJJ /**Fairfax** | Top Game BJJ Academy /**Richmond** | ~100 mi apart |
| WI | `fluidmotionbjj.com` | Fluid Motion BJJ /**Appleton** | Fluid Motion JJ /**Monroe** | ~150 mi apart |
| MD | `topflightmma.com` | Top Flight MMA /**Fort Washington** | Top Flight MMA /**Belcamp** | opposite ends of MD |
| GA | `ascensionmma.com` | Ascension MMA /**Kennesaw** | Ascension MMA /**Cumming** | both plausible real |
| MA | `fenixbjj.com` | Fenix BJJ /**Lowell** | Fenix /Tewksbury + /Woburn | Lowell location now absent |
| MA | `evolutionlowell.com` | Evolution BJJ /**Lowell** | "Evolution BJJ **Lowell**" /**Tewksbury** | kept record's name and city disagree |
| PA | `lancasterbjj.com` | Lancaster BJJ /**Lancaster** | Lancaster BJJ /**Ephrata** | |
| GA | `sbgatlanta.com` | SBG Atlanta /**Norcross** | SBG Atlanta /Atlanta + /Buford | Norcross now absent |
| GA | `sakurabjj.com` | Sakura BJJ /Woodstock | KODA Academy /Woodstock | same city, total name change — rename or two schools? |

`evolutionlowell.com` is worth flagging twice: the surviving record is *named* "Evolution BJJ
Lowell" but filed under Tewksbury, while the record actually filed under Lowell was the one
suppressed. That is a ZIP/city-contradiction of the kind the handoff already catalogued.

### B2 — 20 low risk: same city, same school, cosmetic name difference

Suppression looks correct; the MatMade record is the better one. Listed for completeness, no
action proposed:

`CA modestobjj.com` · `GA` (none) · `IN munciebjj.com` · `MA alliancebjjframingham.com` ·
`MA bbjjoff.com` · `MA bernardofariaacademy.com` · `MA redlinefightsports.com` ·
`MA sonecabjj.com` · `MD hagerstownbjj.com` · `MI lansingbjj.com` · `OK edmondbjj.com` ·
`OR oregonbjj.com` *(already adjudicated)* · `PA eriebjj.com` · `PA yorkbjj.com` ·
`TX amarillobjj.com` · `VA richmondbjj.com` · `VA winchesterbjj.com` · `WA bjjolympia.com` ·
`WA everettbjj.com` · `WI alliancebjjmadison.com` · `WI sheboyganbjj.com`

Worth noting: several of these (Bernardo Faria, Redline, Soneca, Alliance Framingham, BBJJ
Framingham) are MA records whose legacy twin was suppressed — the **inverse** of backlog item 8,
where three MA legacy records were kept and their MatMade twins dropped. MA was clearly curated
in both directions. Worth one consistency pass over MA specifically.

---

## Incidental findings (measured, not requested)

Same dump, same pass:

- **Backlog item 3 is now fully scoped and is smaller than feared.** Truly bare multi-tenant
  hosts across all 27 shipped states: **exactly 4 records, all in Massachusetts** —
  `clients.mindbodyonline.com`, `squareup.com`, `facebook.com`, `m.facebook.com`. These are
  precisely the four the handoff named. **No other shipped state has one.** Item 3 can be closed
  with a four-record fix.
- 41 further records use a site-builder homepage (`business.site`, `gymdesk`, `weebly`,
  `wordpress`). These are legitimate homepages, not defects.
- **1,712 live records still use `http://`.** That is the true scope of backlog item 2's
  mixed-content re-probe — substantially larger than the "~700 bad links" working estimate, and
  it means the `no-cors` false-negative affects roughly 40% of the corpus, not a tail.
- **516 live records have scheme-less URLs.** They render fine (the section prepends `https://`),
  so this is cosmetic in output but it means the step-3 gate was only ever enforced on Oregon.
- **0 mixed-case hostnames** anywhere. That defect class is clean and can be dropped from the
  scan.

---

## The remaining-states list the handoff never had

The handoff header is a **top-25 leaderboard, not a done-list**: those 25 counts sum to 3,845
against a total of 4,520, leaving 675 records in smaller regions.

**27 states shipped** (have a MatMade import):
AL AZ CA CO CT FL GA IL IN KY LA MD MA MI MO MT NV NJ NC OH OK OR PA TX VA WA WI

**34 regions still legacy-only**, with current legacy counts:
NY (64) · ON (40) · AR (35) · TN (34) · BC (26) · NS (23) · AK (22) · AB (22) · QC (21) ·
MN (18) · IA (15) · NB (15) · NL (15) · MS (14) · SC (14) · UT (14) · KS (13) · NE (12) ·
NM (12) · HI (11) · ID (11) · ME (11) · MB (11) · RI (11) · SK (11) · VT (11) · NH (10) ·
PE (10) · WV (10) · ND (9) · SD (9) · WY (9) · DE (7) · DC (7)

**New York at 64 legacy records is by far the largest unshipped region** and the obvious next
state — no other unshipped region exceeds 40.

---

---

# ADJUDICATION OF THE 9 B1 CASES — COMPLETE (5 Aug 2026)

**Result: 9 of 9 suppressions were correct. No real school was deleted anywhere.**
One surviving record carries a name defect. Nothing was changed.

In all nine, the legacy record was the mislocated one — the shared domain provably belongs to
the school the MatMade record describes. This is a meaningful update to the standing rule:
across a 27-state corpus, **every** cross-city domain collision resolved the same way Oregon
did. The rule's premise — that the legacy record is real — held zero times out of nine.

| # | state / domain | suppressed legacy | evidence | verdict |
|---|---|---|---|---|
| 1 | VA `topgamebjj.com` | Top Game BJJ /Fairfax | Richmond-only academy, est. 2003, 8324 Staples Mill Rd; serves Richmond/Mechanicsville/Ashland/Short Pump. No Fairfax site. | correct |
| 2 | WI `fluidmotionbjj.com` | Fluid Motion BJJ /Appleton | Domain is the Monroe school (1313 16th St) + Brodhead; instructors Ben & Dave Dodd. No Appleton site. | correct |
| 3 | MD `topflightmma.com` | Top Flight MMA /Fort Washington | Harford County school, 1371 Brass Mill Rd Belcamp; serves Aberdeen/Bel Air/Havre de Grace. Fort Washington is Prince George's County. | correct |
| 4 | GA `ascensionmma.com` | Ascension MMA /Kennesaw | Single site, 2 Tri-County Plaza Cumming; site's own page is "Cumming Schedule". Head instructor Junior Assuncao. | correct |
| 5 | MA `fenixbjj.com` | Fenix BJJ /Lowell | Two sites only — Woburn (911 Main St, founded 2007) and Tewksbury (1830 Main St). Brands itself "Woburn & Tewksbury". Both kept. | correct |
| 6 | MA `evolutionlowell.com` | Evolution BJJ /Lowell | **See below — resolved, but with a defect in the surviving record.** | correct |
| 7 | PA `lancasterbjj.com` | Lancaster BJJ /Lancaster | Single site, 342 N Reading Rd, Ephrata PA 17522, opened 2008. Named for the *county*; physically in Ephrata. | correct |
| 8 | GA `sbgatlanta.com` | SBG Atlanta /Norcross | SBG states two locations: Druid Hills (1799 Briarcliff Rd NE) and Buford (4989 Lanier Islands Pkwy). Both kept. No Norcross. | correct |
| 9 | GA `sakurabjj.com` | Sakura BJJ /Woodstock | **Rename, not a collision.** Sakura BJJ → KODA Academy of Martial Arts, same address (1105 Parkside Ln, Woodstock), same domain. Suppression prevented a double listing. | correct |

## Case 6 in detail — and a caution worth recording

Directory aggregators (businessyab, beakid, bjjweb) still list **910 Andover St, Lowell**
with a separate phone, `978-996-1873`, and the site's `<title>` still reads
**"HOME | Evolution - Gym in Lowell and Tewksbury"**. On that evidence the Lowell school looks
live, and the suppression looks like a real deletion.

Opening the site settles it. The rendered page body mentions **Lowell zero times**, and carries
exactly one address — **540 Main St, Tewksbury, MA 01876** — and one phone, `978-450-0006`.
The Lowell site has consolidated into Tewksbury; the page title is a stale SEO artifact.

This is the same trap `snippets/tjjm-region-index`'s own header warns about — never trust a
`<title>` or meta description, they go stale. Extend that rule: **it applies to third-party
sites too, and aggregator listings lag by years.** Three separate directories agreed on a
location that no longer exists.

### The one thing that does need fixing

The surviving MatMade record is named **`Evolution BJJ Lowell`** but filed under **Tewksbury**.
The name is now wrong — the school is not in Lowell. Proposed: rename to
`Evolution Performance Center` (its current trading name) or `Evolution BJJ Tewksbury`, city
Tewksbury, address 540 Main St. **Awaiting approval — not applied.**

## What this changes about the standing rule

The handoff says "keep the legacy record" is conditional. This pass suggests it should be
inverted for one specific shape: **when a legacy record and a MatMade record share a domain but
sit in different cities, the legacy record has been wrong 10 times out of 10** (9 here + Oregon).
The legacy corpus's cross-city entries are SEO stubs or years-stale locations, not schools.

That does not license blind suppression — case 6 needed the site opened to distinguish
"consolidated" from "still open", and the answer was not visible in search results. But it does
mean the default should flip, with verification as the check rather than the decision.

---

---

# GROUP A ANOMALIES — INVESTIGATED (5 Aug 2026)

Three verdicts, all different. **One duplicate, one wrong-entity link, one link fix that turned
up net-new leads.** Nothing applied.

## A1 · TX `rodrigopinheirobjj.com` — wrong-entity link, NOT a duplicate

Both records are real, unrelated schools.

- `rodrigopinheirobjj.com` is a **single San Antonio academy** — 4523 N Loop 1604 W Ste 103,
  San Antonio TX 78249, (210) 404-9955, operating since 2008 (a second RPBJJ site on Potranco Rd
  has its own domain, `rpbjjpotranco.com`).
- On the whole site, "New Braunfels" appears **once**, in catchment marketing copy
  ("welcomes everyone in San Antonio and the surrounding area, including Austin, Boerne, and
  New Braunfels"). "Unconventional" and "Walnut" appear **zero** times.
- `Unconventional Performance & Training` is a real, separate gym at **1117 N Walnut Ave,
  New Braunfels TX 78130**, (830) 310-2568.

**Proposed:** blank or replace the website on the MatMade record
`Unconventional Performance & Training`. Keep both records. **No suppression.**

**Worth noting:** the same wrong URL appears on `gyms.jiujitsu.com` for the same gym. Two
independent directories carrying the identical error points at a shared upstream source rather
than a MatMade-specific mistake — so this defect class is probably not rare, and cannot be found
by checking whether a URL *resolves*. It resolves perfectly; it just belongs to someone else.

## A2 · CA `reddingselfdefense.com` — genuine duplicate

The site's own `/locations` page lists **Mendes Jiu-Jitsu Headquarters, 9481 Deschutes Road,
Ste. 5&7, Palo Cedro, CA 96073**, plus three affiliates elsewhere (Lost Boys /Arcata,
Ka'eo Athletics /Kailua-Kona HI, Los Mo Dojo /Los Molinos). **"MZ" appears zero times**, and
the organisation occupies suites **5&7** — not the Ste 3 on the MZ listing. Instagram is
`@mendesbjjhq`.

`MZ Brazilian Jiu-Jitsu` /Palo Cedro is a stale listing of the same school under a former name.

**Proposed:** suppress the MatMade record `MZ Brazilian Jiu-Jitsu`, keep the legacy
`Combat Base Shasta/ Mendes Brazilian Jiu-Jitsu`. **CA 461 → 460.** Awaiting approval.

**This is the only case in the entire audit where the standing rule — keep the legacy record,
drop the MatMade duplicate — is the correct call.** Ten cross-city cases went the other way;
this same-address, same-domain case goes the original way. That is the actual discriminator:
**not legacy-vs-MatMade, but same-location-vs-different-location.**

## A3 · FL `bjjorlando.com` — two real locations, plus 2 net-new leads

Fabin Rosa BJJ Academy runs **four** locations, each with its own page:

| location | address | phone | page |
|---|---|---|---|
| Orlando | 4085 L B McLeod Rd, Ste F, 32811 | (407) 649-6762 | `/orlando` |
| Altamonte Springs | 477 E Altamonte Dr, 32701 | (407) 960-7646 | `/altamonte` |
| **Belle Isle** | 119 Gatlin Ave, 32809 | (407) 730-4060 | `/belle-isle` |
| **Casselberry** | 232 FL-436, 32707 | (407) 360-5669 | `/casselberry` |

Both existing records are real and distinct. **Proposed:** repoint them to `/altamonte` and
`/orlando` respectively. No suppression.

**Belle Isle and Casselberry are absent from the FL set** — verified against the dump, which
returns only the two Fabin Rosa records (`Mata Leao BJJ/MMA Academy` /Casselberry is a different
school). **2 net-new FL leads.**

## The generalisation this produces

A3 was chased as a *link defect* and produced *net-new schools*. That reframes the 8 brand-root
clusters in Group A: when every location of a brand points at the brand homepage, the data
cannot tell you which locations exist — so a brand-root cluster is simultaneously a link defect
**and** a hidden coverage gap.

The 8 clusters are worth a sister-site pass each, exactly like the handoff's `impactjj.com`
pass. That one yielded fixes but no net-new; this one yielded 2 net-new from a 4-location brand.
Tiger Schulmann's (18 records), Easton (8) and Gracie Barra (5) are the largest and should be
checked against their own locations pages before assuming coverage is complete.

---

---

# BRAND-CLUSTER SISTER-SITE PASS (5 Aug 2026)

Each brand's own locations page, diffed against the full in-state set — not just against the
records in the collision cluster. That distinction matters: several brand locations are already
in the directory under **different names**, and a cluster-only diff would have reported them as
missing.

## Net-new leads: 18

| state | brand | missing locations |
|---|---|---|
| AZ | Gracie Barra (19 schools; 10 in directory) | **Arcadia** /Phoenix · **Ahwatukee** /Phoenix · **McCormick Ranch** /Scottsdale · **Scottsdale** · **North Phoenix** · **Maricopa** · **Anthem** /Phoenix · **Marana** · **Vail** /Tucson |
| NJ | Tiger Schulmann's (20; 18 in directory) | **Cherry Hill** · **Marlton** · **East Hanover** |
| TX | CJJF / Caveirinha (5; 2 in directory) | **Melissa** · **McKinney** · **Celina** |
| FL | American Top Team (11 FL facilities; 16 ATT records incl. affiliates) | **Coral Springs** |
| FL | Fabin Rosa (4; 2 in directory) | **Belle Isle** · **Casselberry** |

Arizona is the standout: **9 Gracie Barra schools missing from a state that already has 173
records.** Only 5 of AZ's 10 GB records were in the collision cluster — the other 5 use their own
domains (`graciebarrapeoria.com`, `gborovalley.com`), which is why the cluster undercounted.

## Zero net-new — and two averted false positives

- **CO Easton** — 9 locations, 8 in the cluster. Castle Rock looked missing, but the directory
  already lists it as **`Matrix Martial Arts` /Castle Rock**, matching Easton's own
  `/matrix-castle-rock/` page. Not net-new; the record just needs repointing and arguably a
  clearer name.
- **TX Revolution Dojo** — 3 locations (Houston, Katy, Cypress), 2 in the cluster. Katy is almost
  certainly the existing **`Katy Brazilian Jiu Jitsu Revolution Team` /Katy**. Confirm before
  treating as net-new.
- **NV Gracie Las Vegas** — the site has no `/locations` page (404) and its contact page lists
  exactly two sites: Charleston (5243 W Charleston Blvd) and Henderson (11165 S Eastern Ave).
  Both are in the directory. Nothing missing.

**Lesson: diff the brand roster against the whole state, never against the cluster.** Two of the
eight clusters would have produced phantom leads otherwise.

## Stale or wrong records this pass exposed

| state | record | problem |
|---|---|---|
| LA | `UFC Gym New Orleans` | UFC GYM's national list has **exactly one Louisiana location** — Sherwood, Baton Rouge. There is no New Orleans gym. Suppression candidate. |
| LA | `UFC GYM Acadian, Baton Rouge` | The Baton Rouge site is **Sherwood** (4520 S Sherwood Forest Blvd). "Acadian" is not on the brand list — stale name/address. |
| NJ | `Tiger Schulmann's Clifton` | Not on TSK's 20-location list. Likely closed. Verify before suppressing. |
| NV | `Gracie Jiu - Jitsu Summerlin` | Carries `gracielasvegas.com`, but "Summerlin" appears **zero** times on that site. Wrong-entity link. |
| TX | `CJJF Academy - North Texas` /Prosper **and** `Caveirinha Jiu-Jitsu Family Texas` /Prosper | Two records, same city, same brand — probable duplicate. The domain audit missed it because only one carries `cjjftx.com`. |
| FL | `American Top Team Aventura` | Filed under **Miami Beach**; Aventura is a separate city. |

The CJJF pair is worth noting structurally: it is a **same-city duplicate that the domain
intersection could not see**, because duplicates only collide when *both* records carry the
domain. That is a second blind spot alongside the never-imported one, and it argues for a
name-similarity pass within each city as a separate check.

## Link fixes ready to apply

All 38 brand-cluster records get location-specific URLs (`eastonbjj.com/boulder/`,
`tsk.com/locations/nj/hoboken/`, `graciebarra.com/avondale-az/`, `bjjorlando.com/altamonte`,
etc.), except the NV pair, whose brand site has no per-location pages — those stay on the root
legitimately.

---

---

# BUILD: "Aug 5 BJJ Gyms XX — collision fixes + brand links" (5 Aug 2026)

Theme **`gid://shopify/OnlineStoreTheme/154653950124`**, duplicated from MAIN.
**READY TO PUBLISH — the connector blocks `themePublish`, so you publish.**

## What changed

| file | before | after | change |
|---|---|---|---|
| `sections/tjjm-state-directory.liquid` | 12,028 | **12,485** | website-override lookup |
| `snippets/tjjm-gym-websites.liquid` | — | **2,226** | NEW — 11 link corrections |
| `snippets/tjjm-removed-index.liquid` | 7,699 | **8,078** | + `MZ Brazilian Jiu-Jitsu` on CA row |
| `snippets/tjjm-gyms-data-32.liquid` | 13,802 | **13,814** | Evolution record rewritten |
| `snippets/tjjm-region-index.liquid` | 3,440 | **3,440** | CA 461→460, total 4,520→4,519 |

`tjjm-gyms-data-32` came back at **exactly** the predicted 13,814 (name +8, domain +11,
address −7). Region index unchanged in size, as predicted (both edits same-length).

**New mechanism:** website corrections now live in `snippets/tjjm-gym-websites` using the same
`~Name|Value~` idiom as `tjjm-gym-addresses`. An override beats the record's own `w`, and an
empty value blanks the link. This exists because 10 of the affected records live in the 113 KB
legacy blob, which the Admin API can only write whole.

## Verification

- **Double sweep, all 61 regions**, explicit `preview_theme_id` on both sides, cache-busted:
  total **4,520 → 4,519**, exactly **6 regions changed** — AZ (URL), CO (URL), FL (URL),
  TX (URL), MA (NAME+URL), CA (461→460, NAME+URL). The other 55 byte-identical.
- **One count change only:** CA 461 → 460.
- JSON-LD `numberOfItems` == `class="tjjm-gym"` card count on **all 61** regions.
- CA: 460 gyms / 227 cities / `.tjjm-city-h` 228 (= cities + 1). `MZ` absent,
  `Combat Base Shasta/ Mendes` present.
- MA: still 140. `Evolution Performance Center` present with `540 Main St`;
  `Evolution BJJ Lowell` and `910 Andover` both gone.
- Metafields set: CA `title_tag` + `description_tag` now say 460.

## NOT DONE — Files JSON

The rebuilt 4,519-record `tjjm-gyms.json` (490,829 B) was generated and **uploaded to Shopify
staging successfully (HTTP 201)**, but the `fileUpdate` mutation that attaches it to the
existing file record was **blocked by the permission classifier**.

The staged upload expires **2026-08-06T17:56:48Z**.

**Consequence: after you publish, the theme will report 4,519 while the Files JSON still says
4,520.** Either re-run `fileUpdate` with permission granted, or replace the file from Shopify
admin. The rebuild method was validated first by reconstructing NJ from rendered JSON-LD and
confirming all 211 records matched the existing file byte-for-byte.

---

# METHOD CORRECTIONS FROM THIS BUILD

Four things that invalidate earlier assumptions. All were caught by verification, which is the
argument for keeping it.

1. **`?preview_theme_id=` SETS A COOKIE.** The handoff says it "works as a fetch query param,
   so a 61-page sweep needs no cookie juggling". True, but incomplete: the param also sets a
   preview cookie, so any *unparameterised* fetch afterwards renders the last previewed theme.
   My first sweep compared the build against itself and reported "0 changed regions, total
   4,519" — a completely clean false negative. **Always put an explicit `preview_theme_id` on
   BOTH sides of a comparison.** Use a pre-change duplicate as the "before".
2. **Storefront responses are cached; sweeps need a cache-buster.** With explicit params but no
   `&cb=`, the sweep reported TX unchanged when TX had in fact changed correctly. Append a
   unique param to every fetch.
3. **Domain-normalised collision detection overstates brand-root defects.** The audit
   normalises URLs to hostnames, so `tsk.com/locations/nj/hoboken/` and `tsk.com/` both become
   `tsk.com`. That made the NJ cluster look like 18 records pointing at a homepage when **17
   already had correct per-location URLs** — only the legacy Clifton record was on the root.
   The earlier "38 brand-root records" figure is wrong; the true number needing correction was
   **11**. Always inspect raw `w`, never the normalised domain.
4. **Mixed-case hosts DO exist.** The earlier scan reported zero because it read
   `URL.hostname`, which lowercases automatically. `Gracie Jiu - Jitsu Summerlin` carries
   `http://GracieLasVegas.com`. Test the raw string, not a parsed hostname.

Also corrected: `GB Oro Valley` already had `graciebarra.com/oro-valley-az/` — it was never
missing a deep link.

---

## Proposed next actions

0. **Publish theme `154653950124`**, then resolve the Files JSON above.
1. ~~Adjudicate the 9 B1 cases~~ — **done, 9/9 correct.** `Evolution BJJ Lowell` rename
   **applied**.
2. ~~Investigate the 3 Group A anomalies~~ — **done.** CA `MZ Brazilian Jiu-Jitsu` suppression
   **approved**; two link fixes; 2 net-new FL leads.
3. ~~Sister-site pass on the 8 brand clusters~~ — **done.** 18 net-new leads, 6 stale records,
   38 link fixes.
4. **Decide scope of the next theme build** — the approved edits are small; the 18 leads and 6
   stale records are a much larger piece of work and would normally be a state-sized run.
5. Verify the 6 stale records before any suppression (each ~1 search).
6. Name-similarity pass within city, to catch same-city duplicates the domain check cannot see.
3. Close **backlog item 3** — 4 MA records.
4. Fix the **38 brand-root links** in Group A (mechanical, no adjudication).
5. Re-scope **backlog item 2** around the real figure of 1,712 `http://` records.

## Scratch theme

`SCRATCH — collision audit`, id `154652311724`. Contains two added files
(`sections/tjjm-audit-dump.liquid`, `templates/page.tjjmaudit.json`) and nothing else changed.
It is the reusable harness for this audit — re-running after the next state import is one fetch
loop. Delete it if you would rather not keep a scratch theme around; recreating it is ~5 minutes.
