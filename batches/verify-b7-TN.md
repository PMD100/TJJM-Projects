# Batch 7 — Tennessee (TN) Verification

Verifying `research-b7-TN.md` against `METHOD-RULES-agent.md` and `METHOD-RULES-batch7-addendum.md`.
All DNS checks re-run myself via `https://dns.google/resolve?name=<host>&type=A`. All page reads are
my own `mcp__workspace__web_fetch` calls this pass — nothing carried forward from the research file
without independently re-reading it. No WebSearch synthesized answer was trusted without either a
direct page read confirming it or an explicit flag that it could not be confirmed (one synthesized
answer was caught being wrong outright — see Tri-Cities BJJ below).

Full row-level detail is in `verdict-b7-TN.tsv`. This file is the reasoning behind it.

---

## JOB 1 — the 9 non-REAL verdicts

**All 9 of the research pass's non-REAL verdicts are CONFIRMED. None were overturned.** However,
evidence was substantially strengthened or extended for several, and three of the dead/unreachable
stubs now have a genuine, differently-named replacement school found and added.

1. **Athens Brazilian Jiu-Jitsu (GONE)** — re-ran DNS myself: `Status: 3` NXDOMAIN, conclusive,
   confirmed. But per the task's specific instruction to check whether a real school exists in Athens
   under a different name: yes. **Athens Jiu Jitsu** (athensjiu-jitsu.com) is real, BJJ-specific, and
   its own page links to `facebook.com/AthensBrazilianJiuJitsu` — the *exact same Facebook page name*
   as the dead stub, which is about as clean a same-lineage/rebrand signal as this project gets without
   a direct statement on the page. Added as ADD.

2. **Knoxville BJJ (GONE)** — DNS re-confirmed NXDOMAIN. Knoxville already has 4 other REAL confirmed
   records on the corpus (Knoxville Martial Arts Academy, Lucas Lepri BJJ, Shield Systems Academy, and
   Gracie Barra Knoxville per the fix below), so no forced replacement was pursued for this specific stub.

3. **Upper Cumberland MMA (GONE)** — re-fetched myself, confirmed the domain now redirects to a
   HugeDomains "for sale" landing page. Conclusive. No replacement business found under any name in
   Cookeville specifically for this stub; Cookeville's two other real records stand.

4. **Kaze BJJ and Judo Institute (WRONG-ENTITY)** — **the Ontario finding is confirmed by me reading
   the page myself.** `kazebjj.com/location.html` states in its own body: "Kaze Brazilian Jiu Jitsu...
   1950 Ellesmere Rd unit #8, Scarborough, ON M1H 2V8, Canada." This is a real, active, unrelated
   business (confirmed via its own homepage too — logo, class schedule, "NEW UNIFORMS" post). This is
   a clean instance of the "a working link is not evidence the record is right" trap from the method
   file. I made a genuine attempt to reach a primary source for the real Clarksville, TN entity: no
   working own-domain exists, and Facebook/Instagram fetches returned empty in this sandbox (blocked).
   The best source I could reach was a **self-authored** Smoothcomp club profile (a first-person "About
   us" written by the club, not a third-party aggregator scrape) naming managers Eric Schwalm and
   Krystal Crocker and giving the address 99 Marion Street, Clarksville, TN — consistent with several
   independent aggregators and a Facebook post title I could see the title of but not the body of. This
   is stronger than pure aggregator noise but is *not* a strict "own page" read, so I am not stating the
   address as fully confirmed — recommending a blank URL with the corrected address, flagged accordingly.

5. **Chattanooga BJJ (UNVERIFIED)** — DNS re-confirmed resolving (Status 0). Re-fetched http, https,
   and www variants myself; all three return only a bare `<meta viewport>` tag and nothing else — this
   is genuinely a JS-only render this tool cannot execute, not a typo or a redirect I missed. Chattanooga
   already has two other real, own-page-confirmed schools, so this gap is low-stakes.

6. **Kingsport BJJ (UNVERIFIED)** — DNS re-confirmed resolving. Re-fetched http/www; totally empty
   response. Found and added a genuine replacement: **Kingsport JiuJitsu** (kingsportjiujitsu.com),
   run out of Duncan MMA, BJJ program under Steve Bongiorno (a Ricardo Almeida BJJ Black Belt) —
   own page read myself, address 1133 N Eastman Rd, Kingsport, TN 37664.

7. **Murfreesboro BJJ (UNVERIFIED)** — DNS re-confirmed resolving. Re-fetched; same empty-shell
   pattern. Independently re-confirmed the research file's proposed replacement (Tennessee BJJ Academy
   Murfreesboro / Asura Combat Sports, bestboromma.com) by reading its own page myself. Separately
   discovered that `graciebarramurfreesboro.com` — a domain that would be an obvious thing to check for
   this city — has been **hijacked and now redirects to an unrelated gambling/spam site** ("HOKI22").
   Flagging this so nobody downstream mistakes that domain for a live source.

8. **Alliance Jiu Jitsu Tennessee (UNVERIFIED)** — re-fetched `alliancetnbjj.com` myself, still empty.
   A search snippet shows the business's own Facebook page is literally titled "Alliance TN | Memphis
   TN," which is suggestive that this Nashville-stored record may actually belong in Memphis — but I
   could not read that Facebook page's body (fetch blocked in this sandbox), so per the "never state
   evidence you did not read yourself" rule this stays UNVERIFIED rather than being upgraded to
   WRONG-CITY. Flagging the suspicion explicitly rather than acting on it.

9. **Tri-Cities BJJ (UNVERIFIED)** — could not reach a working own page under this specific name.
   **Important catch:** a WebSearch synthesis handed me a confident-sounding answer — "located at 113
   Cherry Street, Johnson City... person in charge is Keith Olson" — for what it implied was this
   entity. I did not accept it. I found the actual most-plausible candidate business, Olson's Martial
   Arts Academy (olsonsma.com), fetched its own page, and it directly contradicts the search synthesis:
   the real address is 316 Marketplace Blvd Suite 15, and the owner is **Grand Master Amanda Olson**,
   not Keith Olson. This is exactly the "confident fabrication is worse than nothing" failure mode the
   method file warns about, except this time it came from the search tool's own summarization rather
   than from a prior research pass — and reading the actual page caught it. Olson's Martial Arts
   Academy does have a genuine, explicit "Brazilian Jiu-Jitsu program" (confirmed on its own /jiu-jitsu
   subpage: "Our Brazilian Jiu-Jitsu program is a great way to improve your fitness and conditioning")
   and is added separately below as its own record — not asserted to be "Tri-Cities BJJ."

**Bonus finding beyond the required 9:** while chasing the Knoxville stub I found that "Gracie Barra
Knoxville" (stored URL samuelbragabjj.com, verdict REAL in the research file) has a live, current own
page at a *different* domain, **jiujitsuknoxvilletn.com**, which I read myself. It confirms the same
person (Samuel Braga, Gracie Barra Black Belt, 3× IBJJF World Champion) but a different current
address (5710 Kingston Pike, Suite 2, Knoxville, TN 37919) than any aggregator claim. Recommending a
URL fix. This wasn't required by the task but was too good a find to leave out.

---

## JOB 2 — the 7 NET-NEW proposals

**All 7 are confirmed real, BJJ-teaching, and correctly located, by reading each school's own page
myself this pass.** Chattanooga Jiu-Jitsu Academy, Seymour Brazilian Jiu-Jitsu Academy, Tennessee BJJ
Academy Murfreesboro, Triangle Academy of Jiu-Jitsu, and Greeneville Jiu-Jitsu all pass the discipline
test cleanly — each has a dedicated, explicit adult (and usually kids) BJJ program, not a kids-only
add-on at a TKD school.

### The Progressive Martial Arts Academy duplicate name — resolved, not deferred

I fetched `pmaoakridge.com` directly. It is **genuinely one business with two locations**, and its own
page lists both under the literal identical name "Progressive Martial Arts Academy":

- Oak Ridge: 1375 Oak Ridge Turnpike, Oak Ridge, TN 37830 (the flagship — matches the domain name,
  matches the footer copyright address)
- Knoxville: 215 Center Park Drive Suite 550, Knoxville, TN 37922 (opened later; a 2022 Farragut Press
  article surfaced in search calls it "Progressive Martial Arts opens in West Knoxville")

Because the directory's storage format matches records by **name alone, corpus-wide**, adding both
locations under the identical string would silently corrupt both records — exactly the failure mode
the task called out. My resolution: add the Oak Ridge location under the canonical name **"Progressive
Martial Arts Academy"**, and add the Knoxville location under the disambiguated name **"Progressive
Martial Arts Academy - Knoxville."** That suffix is not something I read on PMA's own page (the shared
domain doesn't distinguish the two locations by name) — it's taken from the business's own Facebook
page name as it appeared in a search snippet ("Progressive Martial Arts Academy - Knoxville," at
`facebook.com/knoxvillepma`), which I could not fetch directly (Facebook is blocked in this sandbox).
I'm flagging that the disambiguation suffix itself is a recommendation, not a page-verified trade name,
but the underlying facts (one business, two real locations, two real addresses, genuine BJJ taught at
both per the Felipe Costa endorsement on the shared page) are confirmed.

---

## JOB 3 — coverage sweep

The research file explicitly flagged that it skipped a systematic sweep of TN's small/mid towns for
budget reasons, naming Dyersburg, Tullahoma, Shelbyville, Morristown, Gatlinburg, Paris, Milan, and the
Memphis suburbs. I swept most of that list plus several more (McMinnville, Dover, Collierville,
Dickson, Gallatin, Sevierville, Johnson City) and confirmed **14 new ADD rows** by reading each
school's own page myself:

- **Shelbyville** — Shelbyville BJJ (bjjshelbyville.com)
- **Dyersburg** — Dogwood MMA (dogwoodmma.com) — Dyersburg location only, see below
- **Tullahoma** — Station 6 Fitness and Martial Arts (station6fitness.com)
- **Morristown** — Victory Brazilian Jiu-Jitsu (teamvictorybjj.com)
- **McMinnville** — McMinnville Jiu-Jitsu Academy (mcminnvillejiujitsu.com)
- **Dover** — Renzo Gracie of Stewart County (renzogracieofstewartcounty.com) — see the Dover TN/DE
  trap note below
- **Collierville** — Border Martial Arts Academy (colliervillemartialarts.com)
- **Dickson** — Vigilance Martial Arts (vigilancemartialarts.com) — Dickson location only, see below
- **Johnson City** — Olson's Martial Arts Academy (olsonsma.com)
- **Gallatin** — Global Martial Arts USA (globalmartialartsusa.com)
- **Sevierville** — Fit Factory Fitness and Jiu Jitsu (fitfactoryonline.com)
- **Memphis** — Brazilian Jiu-Jitsu Centers of Memphis (bjjmemphis.com) — lower priority, city already covered
- Plus the two Job-1 stub replacements counted above (Athens Jiu Jitsu, Kingsport JiuJitsu)

### Dover TN vs Dover DE — the addendum's named trap, checked and passed correctly

Renzo Gracie of Stewart County's own page states "Proudly serving Stewart County, TN" and gives the
address 959 US-79, Dover, TN 37058. Stewart County, TN is unambiguous and does not exist in Delaware —
this is correctly a Tennessee record, not a Delaware one.

### Paris, TN — found, not added, because I could not read the page

Paris Gracie Jiu Jitsu Academy (312 Tyson Ave, Paris, TN 38242) has strong circumstantial support —
Yelp, WellnessLiving, matmade, and its own domain all point to a real, currently-operating Gracie
Jiu-Jitsu school. But `parisgraciejiujitsuacademy.com` and its `/contact` page both returned completely
empty responses on two separate fetch attempts. Per the method rules I am **not** adding this as ADD —
it is left UNVERIFIED with a plain statement of what I could and could not read. It is a strong
candidate for a follow-up pass.

### Milan, TN — genuinely not found

I did not find a specific Brazilian Jiu-Jitsu school operating in Milan, TN itself this pass (search
results were dominated by Milan, Italy and Milan, Michigan). Not adding anything for Milan; not
claiming it has no BJJ school either — just honestly came up empty.

### Gatlinburg — not conclusively resolved

Search surfaced "Grapplingburg" (grapplingburg.com) as a plausible Gatlinburg-area candidate, but the
page returned empty on fetch and I did not pursue a second source given budget. Sevierville's Fit
Factory (added) already gives that immediate area some coverage. Leaving Gatlinburg itself unconfirmed
rather than guessing.

### Two more duplicate-name situations, caught and resolved the same way as PMA

- **Dogwood MMA** trades under one name at two locations (Dyersburg and Union City), exactly like PMA.
  Only Dyersburg is added as ADD; Union City is logged as DROP with the same reasoning as PMA — do not
  duplicate the name, and I am not going to guess at a disambiguation suffix the business hasn't shown
  me on its own page.
- **Vigilance Martial Arts** likewise has Fairview and Dickson locations under one name. Dickson's
  location page is explicitly headed "Brazilian Jiu-Jitsu" (cleaner discipline-test pass); Fairview is
  billed as combined "Taekwondo and Brazilian Jiu-Jitsu." Only Dickson is added; Fairview is DROP for
  the same name-collision reason.

This pattern (one real business, two locations, one name, directory matches by name alone) appears to
be a structural risk worth flagging to whoever maintains the storage format, not just a one-off with PMA.

---

## Cross-region debt

- **Kaze Brazilian Jiu Jitsu** (kazebjj.com) — genuinely a real business, but in Scarborough, ON,
  Canada, not Tennessee. Ontario is already curated and out of scope for batch 7. Logged as
  WRONG-REGION in the TSV for the record; no action taken against Ontario's corpus.

No other record checked this pass — existing or NET-NEW — was found to actually belong to VA, MS, AR,
KY, GA, AL, or NC. I specifically re-checked Absolute Jiu-Jitsu Academy Bristol's own page for the
Bristol TN/VA trap: it reads "107 Cox ST Bristol, TN 37620," area code 423 — correctly TN-side.

---

## Held-back rows

| Row | Reason |
|---|---|
| Paris Gracie Jiu Jitsu Academy | Own page and /contact page both returned empty on fetch; strong secondary evidence but no primary read achieved. UNVERIFIED. |
| Dogwood MMA — Union City | Same business/name as the added Dyersburg record; not duplicated to avoid the name-collision hard failure. DROP. |
| Vigilance Martial Arts — Fairview | Same business/name as the added Dickson record; not duplicated for the same reason, and weaker on the discipline test (blended TKD/BJJ vs. Dickson's dedicated BJJ page). DROP. |
| Alliance Jiu Jitsu Tennessee | Suspected actually-Memphis entity per a Facebook page title, but I could not read that page's body, so left UNVERIFIED rather than reclassified. |
| Tri-Cities BJJ | No working own page found under this specific name; Olson's Martial Arts Academy (a different, confirmed entity) added separately for Johnson City instead. |
| Gatlinburg (Grapplingburg) | Page returned empty on fetch; not pursued further given budget. No row added. |
| Milan, TN | No specific school found; genuinely came up empty, not claimed as "no school exists." No row added. |

---

## Budget / context statement

This pass used roughly 20 WebSearch calls (Kaze BJJ primary-source attempt, the four empty-body-domain
chases, and the town-by-town coverage sweep across ~15 towns) plus on the order of 50 direct
`mcp__workspace__web_fetch` calls (DNS checks and own-page reads). I did not exhaustively sweep every
remaining unswept TN town named in the research file's own NOTES section (e.g., Winchester, Fayetteville,
Pulaski, Portland, White House, Mount Juliet, La Vergne, Rogersville, Newport, Sweetwater, Dayton,
Elizabethton, Pigeon Forge/Gatlinburg beyond the one attempt, or the remaining Memphis suburbs Arlington/
Cordova/Millington individually) — the sweep here prioritized breadth (hitting ~15 distinct towns) over
exhausting the full list, consistent with the task's explicit "prioritise breadth across many towns"
instruction. Every row in the TSV reflects a fetch I performed and read myself this pass; nothing was
carried forward from the research file's text without independent re-verification. Rows I could not
independently confirm are explicitly marked UNVERIFIED rather than guessed at (Paris Gracie Jiu Jitsu
Academy, Alliance Jiu Jitsu Tennessee, Tri-Cities BJJ, Chattanooga/Kingsport/Murfreesboro BJJ stubs).
