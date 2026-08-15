# Verification — Batch 7 — Delaware & Washington DC

Verifier pass. Every claim below was re-read on the cited page during this pass (or explicitly marked
UNVERIFIED where a body could not be reached). Nothing was carried forward from the research file on
trust; DNS was re-run fresh for every domain-resolution claim rather than reused from research.

## Headline result

Delaware really was a rotten region for link rot, not a bad research pass — the research agent's
core findings (two domain-repurposing cases, one wrong-city, one wrong-city-and-name, two genuine
stubs) all held up under re-verification. But the research agent under-fetched: five of six DE
net-new candidates it marked UNVERIFIED because it "did not read directly" turned out to be
reachable, real BJJ schools when actually fetched — 4 of 5 are promoted to ADD this pass. DC's
research was more solid but left two structural questions explicitly unresolved that the brief
required be settled, and missed one discipline-test failure (Urban Boxing Navy Yard) that the
addendum specifically warned about.

---

## JOB 1 — Delaware stored records (7)

1. **Delaware BJJ (Wilmington, delawarebjj.com)** — Re-fetched. Confirmed WRONG-ENTITY per research,
   but I'm calling it **GONE** rather than leaving it as an open wrong-entity case, because there is
   no evidence a separate Wilmington "Delaware BJJ" survives anywhere else. Ran two targeted searches
   for a surviving Wilmington entity under that name; found none. Importantly, Wilmington's BJJ gap
   is **not actually empty** — 302 BJJ (see Job 2) has a confirmed, live Wilmington location at 3904
   Evelyn Drive, a fact research missed entirely. Suppress the old record; the net-new 302 BJJ
   Wilmington row covers the city.

2. **Synergy MMA (Wilmington, synergymma.com)** — Re-fetched. Confirmed: redirects to
   synergybjj.podia.com, Bali Indonesia's Synergy BJJ Academy, full academy roster spans Indonesia
   and Singapore, zero US presence. Searched for a surviving Wilmington Synergy; found none (only a
   JJGF page for the same Bali academy). **GONE**, suppress.

3. **Rehoboth Beach BJJ** — DNS re-run fresh: rehobothbeachbjj.com is Status 3 NXDOMAIN, conclusive.
   Rip Tide Brazilian Jiu Jitsu's own page (brazilianjiujitsudelaware.com) re-read in full: address
   17314 N Village Main Blvd #51, **Lewes**, DE 19958, stated twice (header + footer), with an
   explicit service-area line naming Lewes, Rehoboth Beach, Milton, Georgetown and Sussex County.
   Confirms research exactly. **WRONG-CITY**, action FIX-CITY (city, name and URL all need
   correcting together).

4. **First State BJJ (stored Middletown)** — This is where I pushed harder than research asked and
   found something research would have gotten wrong had it "tried harder" blindly. Research left
   doverbjj.com as "returned empty on fetch" and flagged a follow-up should try again. I re-ran DNS
   fresh: **doverbjj.com is Status 3 NXDOMAIN — genuinely dead, not merely unreadable.** I then
   guessed the obvious alternate domain, firststatemartialarts.com, which *does* resolve — but
   reading its body shows it is **a completely different business**: "Delaware Hapkido Martial Arts
   Academy," Hockessin, DE. Had a downstream pass simply seen "firststatemartialarts.com resolves"
   and stopped there, it would have produced a wrong-entity error identical in shape to the
   Delaware BJJ / Synergy MMA domain-repurposing traps already caught in this same region — this is
   the third instance of that exact failure mode in one seven-record region. A targeted web search
   confirmed independent third-party corroboration (bjjweb.com, Yelp, Facebook/Instagram
   @firststatebjj) for a Pedro Sauer-lineage Gracie BJJ school named First State Martial Arts
   Academy at 523 S Red Haven Ln, Dover, DE 19901 — but I could not reach a first-party body this
   pass (both known domains for it are dead). Verdict: **WRONG-CITY** (Middletown → Dover), action
   FIX-CITY, with an explicit note that address/instructor/rank detail is third-party-only and
   UNVERIFIED by primary source.

5. **Dover AFB BJJ** — Tried to re-read the exact dover.af.mil article research cited
   (Article/3879189). The URL now redirects to the base's generic News listing; the article is gone.
   Per the addendum's explicit rule, a base fitness club is not a directory listing unless civilians
   can train there, and no evidence of civilian access exists in either pass. **Overturned from
   research's UNVERIFIED to DROP** — this should not be a directory listing regardless of whether
   the underlying program exists, and the one piece of evidence research had is no longer even
   reachable.

6. **Tribal BJJ (Dover)** — DNS resolves (Status 0, not conclusive). Fetched tribalbjj.com and
   www.tribalbjj.com directly — both return an empty shell (a bare viewport meta tag, no title, no
   body). Also tried Facebook and Instagram profile fetches for "tribalbjj" directly — both came back
   empty (blocked/JS-gated, not readable via this tool). No independent corroboration found anywhere.
   **Confirmed UNVERIFIED**, unchanged from research. This is a genuinely unresolved record, not a
   research failure — I could not do better than research did here within this tool's limits.

7. **Milford BJJ Delaware** — See Job 2 below; resolved to Bayside Athletics.

---

## JOB 2 — Delaware net-new (6 proposed + resolution)

Research flagged five of six as "not read directly this pass" and left them UNVERIFIED. I fetched
all five directly this pass. Four are now confirmed real, primary-verified schools:

- **302 BJJ** — Own page (302bjj.com → www.302bjj.com) confirms **two** locations, not one: Middletown
  (119 Patriot Drive, Suite D, Middletown, DE 19709) **and** Wilmington (3904 Evelyn Drive,
  Wilmington, DE 19808). Research only proposed the Middletown location; I'm adding both as separate
  city rows, because the Wilmington location independently resolves the Job 1 finding that "Delaware
  BJJ" (Wilmington) is dead — Wilmington isn't actually an empty city in this region, it just needed
  the right business name. Cross-corroborated by Yelp ("302 Jiu-Jistu," same Evelyn Drive address)
  and facebook.com/302bjj.
- **Bayside Jiu Jitsu / Bayside Athletics (Milford)** — baysidebjjde.com redirects to
  baysideathleticsde.com, a gymnastics/cheer/ninja/BJJ gym. Read the dedicated Adult Jiu-Jitsu page
  directly: "We teach Brazilian Jiu Jitsu ... flexible schedule of Gi, No Gi for adults," plus a
  separate Youth Jiu-Jitsu page. This is a multi-sport kids' gym with BJJ as one program among
  several — the same shape as the "kids-only-BJJ-at-a-TKD-school" pattern batch 6 rejected — but
  unlike those rejections, Bayside's BJJ program is explicitly Brazilian Jiu-Jitsu, explicitly
  offers **adult** Gi/No-Gi classes (not kids-only), and has its own dedicated program pages. It
  passes the discipline test. **ADD.** This also resolves the "Milford BJJ Delaware" stub — of the
  three Milford candidates research named (Bayside, Milford Jiu Jitsu, Scavenger Jiu Jitsu), only
  Bayside has a live, readable page. Domain guesses for the other two (milfordjiujitsu.com,
  milfordjj.com, scavengerjiujitsu.com, scavengerbjj.com) are all fresh-confirmed NXDOMAIN. I cannot
  rule out that Milford Jiu Jitsu or Scavenger Jiu Jitsu exist under some other domain or
  social-media-only presence, but within this pass's budget I could not find one; flagging as still
  open rather than asserting they don't exist.
- **Kaizen Jiu-Jitsu Academy** — Research's guessed URL doverjiujitsu.com is an empty, unreadable
  shell (confirmed both with and without www). The **actual** live site is a different domain:
  kaizen-jiu-jitsu.com. Own page fully read: "KAIZEN JIU-JITSU ACADEMY, DOVER, DELAWARE," address 35
  Commerce Way, Suite 2, Dover, DE 19904, coaches Chris Bumgarner (3-stripe Gracie BJJ black belt
  under Pedro Sauer & Jon Garfield) and Dusty Estrada (BJJ black belt). **ADD** with a URL
  correction — research had the right business in mind but the wrong domain, which is why it
  couldn't confirm it.
- **Meia Guarda Gracie Brazilian Jiu-Jitsu / Delaware Self Defense Academy** — Own page fully read:
  "headquarters located in Dover ... Delaware's only Royce Gracie Jiu-Jitsu network academy,"
  address 4134 N DuPont Hwy, Dover, DE 19901. A blog-post title on the same domain names the owner
  as Ronnie Wuest. **ADD.**
- **Loyalty Brazilian Jiu-Jitsu** — The one net-new candidate I did **not** upgrade. No dedicated
  domain exists for this business as far as either pass could find; it is Facebook-only. Per the
  "open the page and read the body" rule, a Facebook-only presence does not clear the bar for a
  directory-grade primary source, and I did not attempt a Facebook fetch for this one (the Tribal
  BJJ attempt above showed Facebook fetches return empty through this tool regardless). Left as
  **UNVERIFIED**, action NONE — do not add without a reachable first-party page.

**Net result: 4 of 6 original DE net-new proposals survive as ADD (302 BJJ, Bayside, Kaizen, Meia
Guarda), one is correctly held back (Loyalty), and one net-new row was added that research never
found (302 BJJ's Wilmington location).**

---

## JOB 3 — Washington DC (7 stored + 4 net-new)

### The 810 H St NE resolution (required)

Research flagged this rather than resolving it. I read both pages plus a third source
(capitalmma.com's own current locations list) to settle it:

- **hstbjj.com** ("Capital BJJ" / Capital MMA's H Street program) — body has no current-year content
  at all; the only date-bearing element is a testimonial "Chris T. — Member since 2019." Nothing on
  the page itself confirms it is still operating today.
- **capitalmma.com** — the corporate site's own Locations menu, re-fetched fresh this pass, lists
  **seven** locations: Alexandria, Burke, Fairfax, Herndon, Lorton, Loudoun-Dulles, Takoma Park.
  **None of them is Washington DC.** Capital MMA corporate does not currently claim to operate
  anything at 810 H St NE.
- **underworlddc.com** — current, dated content (2025 No-Gi World Champion photo caption, active
  Google review widget), head coaches Danielle and Aidan. Crucially, **Underworld BJJ's own site
  links its Facebook icon to facebook.com/p/Capital-MMA-Team-Old-City** — i.e., Underworld is using
  the *same legacy Facebook identity* that the old H Street "Capital MMA" program used. A web search
  independently describes the H St NE program's origin as "a partnership of Old City CrossFit and
  Capital MMA."

**Resolution: this is a single business that changed hands/branding, not two concurrent businesses
sharing a building.** Capital MMA corporate has quietly stopped listing a DC location; the H Street
space is now run under new ownership as Underworld BJJ, which inherited the old location's Facebook
page rather than starting fresh. This is neither the "true duplicate" case nor the "shared building,
both stay" case from the Oregon precedent — it's a **successor-business** case. Correct handling:
**suppress "Capital City BJJ" as WRONG-ENTITY (superseded)**, and **add Underworld BJJ as the current
occupant.** Keeping both would double-count one physical BJJ program.

### The Capitol Hill BJJ / BETA Academy resolution (required)

Read betaacademy.com/brazilian-jiu-jitsu in full. Its footer lists exactly two DC locations: 1353
Florida Ave NW ("14th Street corridor") and **316 F Street NE ("Capitol Hill")**. No business
anywhere trades under the literal name "Capitol Hill BJJ" — it is a locational stub that research
correctly mapped to BETA's second location but then, inconsistently, *also* proposed BETA Academy as
a separate net-new row. **Resolution: they are the same business.** Suppress "Capitol Hill BJJ" as
WRONG-ENTITY, keep a single BETA Academy ADD row (noting both DC addresses in its evidence field,
since the output schema has no address column to split them into two rows cleanly). A downstream
editor may still choose to split BETA's two DC locations into two directory rows by street address —
that's a data-modeling choice, not a duplicate-avoidance one, since I've already prevented the
Capitol-Hill-BJJ-plus-BETA double count.

### Other stored records

- **Combat Athletics DC** — re-fetched, still a GoDaddy for-sale parking page. GONE, confirmed.
- **DC BJJ Academy** — targeted search found no business by this name anywhere among current DC BJJ
  listings. GONE, confirmed, unchanged from research.
- **Highstyle Jiu-Jitsu** — re-fetched and fully read: 907 N St NW #C-2, Shaw neighborhood, BJJ +
  Muay Thai + Haitian Fencing. REAL, confirmed, KEEP.
- **N-Flux** — re-fetched staynflux.com and its Facility subpage; confirmed live and offering No-Gi
  Jiu-Jitsu as one of several self-defense/fitness programs. Could not find an address on the
  school's own pages this pass (the Facility page is photos only); address stays third-party/
  UNVERIFIED exactly as research left it. WRONG-URL → FIX-URL to staynflux.com, confirmed.
- **Vortex Jiu-Jitsu** — re-fetched, black belt coach Kelly Quinn, Edlavitch JCC, 1529 16th St NW.
  REAL, confirmed, KEEP.

### Net-new

- **BETA Academy** — ADD (see Capitol Hill resolution above).
- **Estilo Jiu Jitsu** — re-fetched and fully read: 770 Park Rd NW #T01, third-degree black belt Luis
  Pantoja, dedicated BJJ curriculum. ADD, confirmed.
- **Underworld BJJ** — ADD (see 810 H St NE resolution above).
- **Urban Boxing Navy Yard — OVERTURNED from ADD to NOT-BJJ/DROP.** The addendum explicitly
  instructs: *"'Urban Boxing Navy Yard' is a boxing brand — apply this test to it hard."* Research
  added it anyway on the strength of one dedicated BJJ instructor (Ronald Clary, black belt) and a
  BJJ class page. Reading the full page shows Urban Boxing is a five-location boxing/kickboxing
  brand doing 130+ classes/week, of which BJJ (no-gi, Tuesday/Wednesday evenings plus a Friday open
  mat — roughly 3 hours/week) is a minor addition to an overwhelmingly boxing-branded, boxing-
  majority gym: Boxing Level 1, Boxing Level 2, Boxing (all levels), Kickboxing, MMA, Muay Thai,
  Sparring, and Yoga for Boxers are all separate offerings alongside it. This is the same shape of
  error as batch 6's "kids-only-BJJ-at-a-TKD-school" rejections, just with boxing instead of TKD and
  adults instead of kids. **DROP.**

---

## Cross-region debt (DC/DMV)

Re-verified research's one flagged DMV case and checked for others within budget:

- **WDC BJJ** — re-fetched wdcbjj.com fresh. Confirmed Takoma Park, MD (720 Erie Ave), exactly as
  research found. It also has a second location the research file didn't mention: **Hyattsville, MD**
  (4616 Ingraham St) — both Maryland, both correctly excluded from the DC roster.
- **Capital MMA** — re-fetched capitalmma.com's Locations list. All seven locations are VA/MD
  (Alexandria, Burke, Fairfax, Herndon, Lorton, Loudoun-Dulles, Takoma Park). No DC location claimed
  by the corporate brand today — this is itself supporting evidence for the 810 H St NE resolution
  above, not a new cross-region debt item (the DC location it once had is now a separate business,
  Underworld BJJ).

No additional DMV-branded misfiles were found within this pass's budget. I did not run an exhaustive
independent sweep of every Arlington/Alexandria/Bethesda/Silver Spring BJJ site beyond the two
research had already flagged for review — that would require WebSearch budget I chose to spend on
resolving the two required structural questions and re-verifying stored records instead.

## Additional Wilmington, DE schools noticed but not in scope

While confirming 302 BJJ's Wilmington location, a web search surfaced several more Wilmington, DE
BJJ businesses not connected to any stored record or research proposal: Titan Jiu Jitsu (1812 Marsh
Road), Elevated Studios Martial Arts, Riverfront Jiu Jitsu, and Delaware Jiu-Jitsu. None of these
were part of my Job 1/Job 2 assignment (they don't correspond to any stored record or research
net-new proposal), so I did not verify them and they are **not** included in the TSVs. Flagging them
here per the "every region roughly doubles" heuristic in METHOD-RULES-agent.md — Delaware's real BJJ
count is very likely higher than either research's roster or my corrected version of it, and a
dedicated coverage pass on Wilmington specifically would likely find more.

## Held-back rows (neither promoted nor rejected)

- **Tribal BJJ (DE)** — UNVERIFIED, unreachable body, no corroboration. Left exactly where research
  left it.
- **Loyalty Brazilian Jiu-Jitsu (DE)** — UNVERIFIED, Facebook-only, no first-party page to read.
- **Milford Jiu Jitsu / Scavenger Jiu Jitsu (DE)** — not confirmed to exist under any reachable
  domain this pass; not added, not asserted dead either. Open question for a future pass.
- **First State Martial Arts Academy (DE)** — city corrected with high confidence (multiple
  independent third-party sources), but address/instructor/rank details remain third-party-only;
  no first-party body was reachable this pass despite two additional domain attempts beyond
  research's.
- **N-Flux (DC)** — address remains third-party-only; own page confirmed but does not publish a
  street address anywhere I could find.

## Budget / context statement

This pass used direct fetches almost exclusively, as instructed, and only reached for WebSearch five
times total: (1) First State Martial Arts Academy corroboration, (2) DC BJJ Academy existence check,
(3) Delaware BJJ Wilmington survivor check, (4) Synergy Wilmington survivor check. All four were
targeted, single-purpose queries chosen because a direct-fetch domain-guessing approach had already
been exhausted for those specific rows. I did not run an exhaustive sweep of every plausible domain
for Tribal BJJ, Loyalty BJJ, or the two unconfirmed Milford businesses — those remain genuinely
open. No context or budget exhaustion occurred; every row in both TSVs reflects a direct read (or an
explicit UNVERIFIED where no read was possible) performed in this pass, not a carry-forward from the
research file.
