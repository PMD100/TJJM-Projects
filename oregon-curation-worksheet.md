# Oregon curation worksheet — run of 5 Aug 2026

Source set: `oregon-136-matmade.tsv` (136 records, verified against browser byte-for-byte
except line 99, where the Portland CTC `utm_*`/`y_source` tail was deliberately stripped).

Crawl reproduced the previous run exactly: 7,311 slugs, 1 permanent error
(`triton-fight-center` 404), 136 Oregon. No two-letter `OR` variant (only NV×1, TX×6, TN×2,
AZ×1). Zero `97xxx` ZIPs filed outside Oregon. City null on 0 of 136.

---

## CUT — decided on evidence

| # | Name | Reason | Evidence |
|---|---|---|---|
| 99 | Portland CTC | Not a gym | Own URL is `ctcprograms.com/location/downtown-portland-comprehensive-treatment-center/`. Self-proving. Missing postalCode. |
| 49 | Eugene CTC | Not a gym | `ccceugene.org` opened directly = **Center for Community Counseling**, sliding-scale mental-health nonprofit, 1465 Coburg Rd. Site phone `541.344.0620` matches the record exactly. Missing postalCode. |
| 122 | Müv Fitness /Beaverton | Health club, no grappling | Chain (OR/WA/SC). Only martial-arts content is "MUV Force", a karate/boxing-*inspired* cardio class. 2,760 reviews = foot traffic, not jiu-jitsu. |
| 63 | Ballistic Box /Wood Village | Boxing only | USA Boxing registered club. |
| 124 | Next Level Barbell /Milwaukie | Powerlifting only | Strength/powerlifting; since rebranded **Strength Union**. |
| 37 | Taft Athletic Club /Lincoln City | No grappling | 24hr gym housing "Sidekicks Gym" = kickboxing fitness, TaeKwonDo, MMA *conditioning*. |
| 112 | Victory Gym /Albany | Striking only | USA Boxing + MMA **striking**. (Also address conflict: Yelp lists 251 Pacific Blvd SW.) |
| 35 | Budo Fights COM /Bend | Not a gym | 51 NW Greenwood Ave is **Midtown Music Hall / Midtown Ballroom**, a concert venue. "Budo Fights" is a fight *promotion* that stages events there. |
| 66 | Martial Masters Academy /Hillsboro | No grappling | Muay Thai + Boxing + Boot Camp. |
| 54 | Rogue Valley Martial Arts /Phoenix | No grappling | Tang Soo Do (Korean striking). Twice weekly. |
| 94 | Team Quest /Tualatin | Closed location | Yelp: **CLOSED** as of Mar 2026. Phone field is literal `n/a`. Portland Team Quest (#103) survives. |

## KEEP — checked and confirmed, despite looking cuttable

| # | Name | Why it stays |
|---|---|---|
| 13 | CrossFit Tigard - PAW | Jiu jitsu is one of its specialty classes. |
| 36 | Recreate Fitness /Portland | Group fitness **and** jiu jitsu; Mindbody lists a Jiu-Jitsu-at-Recreate class. |
| 135 | GIRLS Gym /Portland | Women's MMA school specialising in kickboxing, **Brazilian jiu jitsu**, self-defence. |
| 55 | Impact Next Generation /Gresham | Youth MMA, **wrestling and jiu jitsu** academy. |
| 132 | Jujitsu-Do Martial Art Center /Eugene | Real AJJF-affiliated Japanese jujitsu school, site live. |
| 8 | Full Force Mma /Aloha | Real MMA gym (Tapology page). **Address stale** — listings show 20125 SW TV Hwy #17, record says 20795. |
| 18 | Courthouse Fit … Salem OR | Genuine Impact JJ location (Lancaster). See name fix below. |
| 108 | Industrial Strength Gym BJJ | Genuine Impact JJ Portland location. |

## RESOLVED in this run

- **111 Oregon's Elite Training Academy /Eugene — CUT.** Yelp marks it CLOSED, and it also
  surfaces on Oregon Higher Ed's "CLOSED PRIVATE CAREER SCHOOLS (2022–2026)" list. Zero reviews.
- **`Gracie Barra Sw Portland` bare host RESOLVED → `graciebarra.com/sw-portland-or/`.**
  Address also gains a suite: 9975 SW Frewing St **Suite 120**. Closes the new instance of
  backlog item 4/3.

---

## Impact Jiu Jitsu sister-site pass — `impactjj.com/locations/`

**Net-new academies: ZERO.** All 12 Oregon Impact locations were already in the MatMade set.
The value came out as corrections instead:

- **#18 name resolved.** "Courthouse Fit Impact JJ South River Lancaster Salem OR" is a mashup
  of all three Salem-area site names. This record is specifically the **Lancaster** location,
  4132 Devonshire Ct NE. (South River Rd = #19, Keizer = #81.)
- **#134 Mountain Warrior** — official site is `mwama.com`, not the stored `facebook.com/MWAMA`.
- **#108 Industrial Strength** — official phone 971-571-5725; record has 971-242-8471 (stale).
- **#45 McMinnville** — official address form "1290 NE HWY 99W"; record has "1290 OR-99W".
- PCC (Cascade / Rock Creek / Sylvania campuses) run classes "powered by Impact JJ". These are
  college gymnasium programmes, not standalone academies — **not added**.

---

## Shared-address pairs — 10 (suffix-normalised)

Resolved by shared host / same org:

| address | records | call |
|---|---|---|
| 9844 SE Empire Ct, Clackamas | Brazilian Top Team Happy Valley · MMA Hiit Fitness | MMA Hiit's URL is `btthappyvalley.com/courses/mma-hiit-fitness/` — **a course page of the former. Cut the course.** |
| 729 Welch St, Medford | Spartan Team BJJ · Spartan Boxing Club | Both on `spartanboxinggym.com`, one org |
| 5280 NE Shell World, Newport | 10th Planet Newport · Tsunami Training Center | Both on `tsunamitc.com`, one facility |
| 14935 SW 72nd Ave, Tigard | River City Warriors · Portland Jiu Jitsu | Both on `rivercitywarrior.com` |

Closure checks now done — **no pair was a succession; none collapse as duplicates except the
same-org cases below.** Shared address in Oregon was overwhelmingly *shared buildings*:

| address | records | call |
|---|---|---|
| 1287 Oak St, Ashland | Ashland Jiu-jitsu Academy · Ashland Mixed Martial Art | **Keep both.** Two distinct active schools, separate sites. AJJA = adult/kids BJJ + kickboxing; Ashland Hero Academy = jiu jitsu/kickboxing/tai chi, founded 2016. |
| 1465 Grand Ave, Astoria | Men's JIUJITSU School · White Panther TKD/Boxing/FMA | Address is **Star of the Sea School**, a rented hall. Men's Jiujitsu = Carlson Gracie affiliate, Thursdays 5pm. The two are **affiliated** (`facebook.com/WPJiujitsu` = "White Panther Men's Jiujitsu"). **Keep both — White Panther is a soft call**, see below. |
| 2101 Bailey Hill Rd, Eugene | Atos Jiu Jitsu Northwest (Ste A3) · Empire Boxing and Fitness | Separate suites, separate businesses. Atos = BJJ under world champion Lucas Barbosa. **Empire Boxing = boxing only → CUT.** |
| 125 Silver Ln, Eugene | Gracie Jiu Jitsu Eugene (Ste B) · RISE Mixed Martial Arts | Building is **McKenzie Martial Arts** — which is why #76's facebook link points there. GJJ Eugene = Gracie University CTC; RISE is in the jiujitsu.com gym directory. **Keep both.** |
| 17761 Dunn Rd NE, Hubbard | Animals MMA Oregon · Counter Point Martial Arts | Both real and active. Counter Point teaches **Jiu-Jitsu** alongside Arnis/Hapkido/JKD/Karate. **Keep both.** (Counter Point's real phone is 503-981-8276; record has 503-201-9368.) |
| 3220 S Troutdale Rd | Choi's Taekwondo Academy · Gracie Technics Jiu-Jitsu (Unit 1) | Different units, different businesses. Gracie Technics = BJJ. **Choi's = TKD only → CUT.** |

### Same-org duplicates — keep one, cut the other

| keep | cut | why |
|---|---|---|
| Brazilian Top Team Happy Valley | **MMA Hiit Fitness** | Cut record's URL is a *course page* of the keeper. |
| Spartan Team Brazilian Jiu-Jitsu | **Spartan Boxing Club** | One org on `spartanboxinggym.com`; keep the grappling arm. |
| Tsunami Training Center | **10th Planet Newport** | One facility on `tsunamitc.com`. Keeper has 120 reviews, a valid URL and full socials; the cut record has 16 reviews and a scheme-less URL. |
| River City Warriors | **Portland Jiu Jitsu** | One org on `rivercitywarrior.com`, same address and phone. Keeper matches the brand/domain. |

### Soft calls — reversible, recorded for the squeeze list

- **White Panther Tae Kwon Do Boxing and Filipino Martial Arts /Astoria.** Its own name
  enumerates only striking arts, which would normally be a cut — but the org demonstrably runs
  jiujitsu via the affiliated Men's Jiujitsu class at the same hall. **Kept.**
- **Full Force Mma /Aloha** — kept on merit, but the address is stale and listings disagree
  (20125 SW TV Hwy #17 vs a Hillsboro Cornelius Pass address). Resolve before trusting.
- **Victory Gym /Albany** — cut as striking-only, but note Yelp lists it at 251 Pacific Blvd SW,
  not the record's 1526 NW Laurel Oaks. If reinstated, fix the address too.

---

## Defects found (supersedes the handoff's list where they differ)

Confirmed from the handoff:
- Lowercase cities: `portland`×17, `salem`×6, `ashland`×2. Title-case before counting.
- Curly apostrophe U+2019: `Men’s JIUJITSU School…`, `Oregon’s Elite Training Academy`.
- Trailing space: `Southwest Portland Martial Arts and CrossFit Hillsdale `.
- SEO tails: `Men’s JIUJITSU School, Astoria Oregon` (comma tail), `Courthouse Fit … Salem OR`.
- Zero pipes, zero emoji, zero quotes/®/NBSP, zero double-spaces.
- Missing postalCode on exactly 2 of 136 — **both are the CTCs. Signal is 2-for-2 in Oregon.**
- `Gracie Barra Sw Portland` stores bare `graciebarra.com`.

**NEW this run — not in the handoff:**
1. **En-dash U+2013** in `RISE Mixed Martial Arts – Eugene`. The sanitiser covers curly quotes;
   it must also cover en/em dashes.
2. **`phoneNumber` is the literal string `n/a`** on `Dynamic MMA` and `Team Quest`. Grep for a
   phone field with no digits.
3. **Three URLs have no scheme at all** — `Combat Sports Center` (`www.combatsportscenters.com`),
   `10th Planet Newport` (`Tsunamitc.com`), `Grappletown` (`grappletown.com`). The handoff filed
   `Tsunamitc.com` under "mixed-case hosts"; it is actually *scheme-less*. Two separate classes:
   scheme-less ×3, mixed-case-with-scheme ×2 (`Canbyjiujitsu.com`, `Impactnextgeneration.com`).
4. **Cross-city phone collision.** `Eugene Jiu Jitsu Club` (122 reviews, 577 River Rd, Eugene)
   carries `541-606-4789` — the **Newport** number, shared with both 10th Planet Newport and
   Tsunami Training Center. An address-only duplicate scan cannot see this. **Add a shared-phone
   scan to the import sequence.**
5. **Wrong-entity social links.** `Kilian's Martial Arts Center` carries four **TeePublic**
   social URLs (twitter/instagram/facebook/tiktok). `Gracie Jiu Jitsu Eugene`'s facebook link
   points at "McKenzie Martial Arts and Family Fitness Center".
6. **ZIP/city mismatch.** `Combat Sports Center` is city `salem`, address "156 Lancaster Dr SE"
   (Salem), but ZIP **97417** = Days Creek, ~150 mi south. One of the three is wrong.
7. `https://www.facebook.com/login` appears as a junk social link on 8 records.
8. Trailing `%20` in Grit MMA's facebook URL.

## Final cut list — 18 of 136

Not a gym (4): Portland CTC · Eugene CTC · Budo Fights COM · Team Quest /Tualatin (closed)
Closed (1): Oregon's Elite Training Academy
No grappling (8): Müv Fitness · Ballistic Box · Next Level Barbell · Taft Athletic Club ·
Victory Gym · Martial Masters Academy · Rogue Valley Martial Arts · Choi's Taekwondo Academy ·
Empire Boxing and Fitness  *(9 with Empire — see table)*
Same-org duplicate (4): MMA Hiit Fitness · Spartan Boxing Club · 10th Planet Newport ·
Portland Jiu Jitsu

**136 − 18 = 118 keeps.** Against the ×0.50–0.85 band on 136 (~68–116), 118 lands **just above
the top of the band** — consistent with Oregon being a genuinely dense BJJ state, and with the
zero-review records splitting 50/50 here rather than Washington's 3-for-3 cut rate.

Oregon's page is at **15** today, so this is +103.

## Collision check vs the live legacy page — A NEW FAILURE MODE

Live `bjj-schools-oregon` = 15 records, all generic SEO-style names on matching generic domains
(`Albany BJJ Oregon` / `albanybjjor.com`, `Bend BJJ` / `bendbjj.com`, …).

- **Name collisions: 0.** `legacyNames.filter(n => keptNames.has(n))` returns empty.
- **Domain collisions: 2.** And the name check *cannot see them*:

| legacy | MatMade record | same domain | verdict |
|---|---|---|---|
| `Ashland BJJ` /Ashland | `Ashland Jiu-jitsu Academy` /Ashland | `ashlandbjj.com` | **Same school.** Same domain, same city. One of them must go. |
| `Oregon BJJ` /**Eugene** | `CTA Hillsboro Jiu Jitsu and Boxing` /**Hillsboro** | `oregonbjj.com` | **The legacy record is mislocated.** The domain belongs to a Hillsboro school; the legacy entry files it under Eugene. |

> **This is a new backlog item.** The standing collision check is name-only, so every past state
> may carry legacy/MatMade duplicates that share a domain under different names. It is the same
> root cause as backlog item 13 (name-only dedupe in `tjjm-gym-directory.liquid`). The re-audit
> in backlog item 5 should be **`legacyDomains ∩ keptDomains`, not just names.**

The `Oregon BJJ` case also breaks the standing rule "keep the legacy record, drop the MatMade
duplicate". Here the legacy record is the wrong one — wrong city, generic name. Applying the
rule blindly would keep a mislocated entry and drop a real Hillsboro school.

## Legacy domain probe — 15 records, only 2 are real schools

`https://` probe (no mixed-content false negatives):

**DEAD ×11** — albanybjjor · coosbaybjj · corvallisbjj · grantspassbjj · klamathfallsbjj ·
medfordbjj · newportbjjor · pendletonbjj · roseburgbjj · alliancejiujitsuportland ·
alliancejiujitsusalem

**LIVE ×4, but only 2 are schools:**

| domain | what it actually is |
|---|---|
| `ashlandbjj.com` | Ashland Jiu-jitsu Academy — real school (collision case) |
| `oregonbjj.com` | CTA Hillsboro Jiu Jitsu and Boxing — real school (collision case) |
| `bendbjj.com` | **Parked on HugeDomains, "for sale".** The Wisconsin pattern. |
| `portlandbjj.com` | **A directory site**, not a gym — "your resource for everything jiu jitsu in Portland". |

So of 15 legacy Oregon records, **zero are independently real** — the two live school domains
are both duplicates of MatMade records, one is parked, one is a link directory, and eleven are
dead. This is the third state running with essentially no true legacy survivors (backlog item 6).

### Net-new leads from `portlandbjj.com` — 6 schools MatMade missed

The junk-looking legacy record turned out to be the best net-new source of the run. Its Portland
school list diffs against the MatMade set as follows — 9 already present, **6 not**:

- American Top Team
- Black Dog Jiu Jitsu Company
- Black Wolf Academy
- Eastside Grappling  *(`eastsidegrappling.com`)*
- Oregon Grappling Arts  *(`oregongrapplingarts.com`)*
- 10th Planet Portland

**Not yet verified or added** — each needs an address and a liveness check before wiring.
Generalisable lesson: **a dead-looking legacy domain may be a directory; open it before
discarding it.**

## Fixes to apply at write time

| record | fix |
|---|---|
| Gracie Barra Sw Portland | URL → `graciebarra.com/sw-portland-or/`; address → 9975 SW Frewing St **Suite 120** |
| Courthouse Fit … Salem OR | name → the Lancaster Impact JJ location; strip the SEO tail |
| Men's JIUJITSU School, Astoria Oregon | strip trailing `, Astoria Oregon`; straighten U+2019 |
| Oregon's Elite Training Academy | *(cut — no fix needed)* |
| RISE Mixed Martial Arts – Eugene | normalise en-dash U+2013 |
| Southwest Portland Martial Arts and CrossFit Hillsdale | strip trailing space |
| Mountain Warrior Academy | URL → `mwama.com` |
| Industrial Strength Gym BJJ | phone → 971-571-5725 |
| Impact Jiu Jitsu Mcminnville | address → 1290 NE HWY 99W; title-case "McMinnville" |
| Combat Sports Center | add scheme; **ZIP 97417 contradicts Salem — verify** |
| Grappletown / 10th Planet Newport | add scheme *(latter is cut)* |
| Sunshine Athletics, Impact Next Generation | lowercase the host |
| Dynamic MMA, Team Quest | phone `n/a` → blank *(latter is cut)* |
| Kilian's Martial Arts Center | drop the four TeePublic social links |
| Wayne Owen Fighting Arts, Portland CTC | strip query strings *(latter is cut)* |
| Grit MMA | strip trailing `%20` from the facebook URL |
| 8 records | drop `facebook.com/login` junk social link |
| portland ×17, salem ×6, ashland ×2 | title-case city |
