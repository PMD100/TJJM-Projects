# Batch 7 Verification — Newfoundland & Labrador and Prince Edward Island

Verifier pass. Every stored record in both regions was independently re-read this pass — I did not
carry forward a single claim from `research-b7-NL.md` or `research-b7-PE.md` without re-confirming
it myself against a primary source (or, where the tool could not reach a primary source, an
independently-run DNS check). Method: `mcp__workspace__web_fetch` for all page reads and
`https://dns.google/resolve` for all DNS screens, per `METHOD-RULES-agent.md`. No bash/curl/python
was used.

## Headline result

**Research's work holds up well on this batch.** Of the 13 non-REAL verdicts across both regions
(7 in NL, 6 in PE), I independently reproduced the same verdict category in all 13 cases. I did
**not** overturn a single verdict category. What I did do:

- Confirmed the `nlbjj.com` WRONG-ENTITY call myself, first-hand, including reading its full
  affiliates list.
- Independently re-confirmed all 4 Foley-family addresses are distinct (3 by direct address read,
  1 — Foley's Martial Arts, Paradise — still genuinely unreadable, same as research found).
- Independently confirmed, by reading `peimma.com`'s own location pages myself, that "Stratford BJJ
  PEI," "Summerside BJJ PEI," and the O'Leary location all really are one business (PEI Martial
  Arts Academy) trading at three physical addresses — and worked out the naming-convention fix
  needed to avoid a corpus-wide name collision.
- Found one thing research missed: a genuine, currently-operating BJJ school (**Golden Rule Jiu
  Jitsu**, Flat Bay, NL) in a city outside the ten permitted NL strings. Not added — flagged below,
  per C7c.
- Found a second thing research missed that turned out to be a non-issue on inspection: a listing
  called "St. John's Martial Arts Centre" that looked like a possible new St. John's BJJ record, but
  reading its own `/jiu-jitsu/` page shows it is word-for-word the *same* club as the already-stored
  "St. John's BJJ" (same Jeff Joslin / Jacaré Cavalcanti lineage text) — it's the shared facility
  page for the same club, not a second school.

## Newfoundland and Labrador — confirmed vs overturned

**15 stored records. 7 non-REAL verdicts from research. All 7 independently reproduced; 0
overturned.**

| Record | Research verdict | My verdict | Changed? |
|---|---|---|---|
| Corner Brook BJJ | GONE | GONE | No — DNS re-verified NXDOMAIN myself |
| Gander BJJ | GONE | GONE | No — DNS re-verified NXDOMAIN myself |
| NL BJJ Academy (nlbjj.com) | WRONG-ENTITY | WRONG-ENTITY | No — read the site and its full affiliates list myself |
| Labrador City BJJ | WRONG-URL | WRONG-URL | No — old domain re-confirmed NXDOMAIN, new domain re-confirmed unreadable |
| Foley's Martial Arts (Paradise) | UNVERIFIED | UNVERIFIED | No — reproduced the same blank-body result across every path I tried |
| Evolution Martial Arts NL | WRONG-URL | WRONG-URL | No — read the correct evolutionmartialartsnl.com myself, confirmed live |
| St. John's BJJ | WRONG-URL | WRONG-URL | No — read stjohnsbjj.ca myself, and found independent corroboration on a second site |

The other 8 NL records (Velocity, Jason Foley, Anchor Combat Academy, New Found TAO BJJ, Alex
Foley's, Michael Foley's, Republic BJJ, Tera BJJ) were all independently re-read by me this pass
and are confirmed REAL, genuine BJJ, correct city. No changes.

### Does the `nlbjj.com` removal hold?

**Yes, confirmed independently.** I fetched `nlbjj.com` and `nlbjj.com/affiliates.html` myself. The
site is "Next Level Brazilian Jiu-Jitsu Association" (NLBJJA), founded by Tony Eduardo Hoerhann
(5th degree black belt), headquartered in Sherman, TX. I read its complete 15-academy, 9-country
affiliate list: Brazil (x3), USA-Texas, USA-Nebraska (Omaha), USA-California, UK, France, UAE,
China (x4), Singapore, Australia, India. **There is no Newfoundland listing, no Atlantic Canada
listing, and no Canadian listing outside the Omaha, NE affiliate.** "NL" here stands for "Next
Level," not Newfoundland & Labrador — a coincidental abbreviation collision, exactly the kind of
trap the method rules warn about.

**Does removing it displace a real St. John's school? No.** St. John's already has six other
confirmed-real, independently-verified BJJ businesses on this pass: Republic BJJ, Tera BJJ,
Michael Foley's Academy, Alex Foley's Academy, Evolution Martial Arts NL (URL-corrected), and
St. John's BJJ (URL-corrected, and independently corroborated a second time via
`stjohnsmartialartscentre.com/jiu-jitsu/`, the shared facility page for the same club). Suppressing
`nlbjj.com` removes a phantom listing, not a real business.

### The Foley cluster — independently re-verified, four real schools confirmed at three distinct addresses (Foley's Martial Arts, Paradise, remains unread)

I read each Foley site myself, separately, this pass:

- **Jason Foley Martial Arts** (Conception Bay South) — 16 Hops St. Unit 104, A1W 0E8, Conception
  Bay South. Read directly on the site's own `/location` page. Postal code A1W confirms NL and
  confirms this is a distinct address from every other Foley location.
- **Michael Foley's Academy of Martial Arts** (St. John's) — 117 Ropewalk Lane, St. John's, NL A1E
  4H6. Read directly on the site footer. Explicit BJJ program taught by "Pedro Sauer BJJ black
  belt, Michael Foley," with a full Gi/No-Gi BJJ class schedule distinct from its separate Kenpo
  Karate/Kickboxing classes — passes the "read the class list, not the title" test.
  Independent history note read on the same page: "Since 1976, the Foley name has been synonymous
  with martial arts in the province."
- **Alex Foley's Academy of Martial Arts (AFAMA)** (St. John's, and also Paradise, Goulds, Witless
  Bay, Whitbourne) — read directly. Genuine adult BJJ program confirmed via two instructor bios
  read on the page (Don Sinnott: "started training in our Adult Brazilian Jiu-Jitsu program in
  2015"; Ivan Burt: "started training in our Adult Brazilian Jiu-Jitsu program when we opened our
  first location in the Goulds in 2010"). This is a multi-location operation, not a single street
  address — consistent with the "40+ years, Foley family" framing on its own About text.
- **Foley's Martial Arts** (Paradise) — I could **not** read this school's own page this pass,
  despite trying every combination the method rules suggest: `foleysmartialarts.com` root,
  `/contact`, `/about`, `/schedule`, `/index.html`, with and without `www`, `http` and `https`, plus
  a reader-proxy workaround (`r.jina.ai`) as an extra attempt beyond what research tried. All
  returned a completely blank body. DNS confirms the domain resolves (Status 0), so this is a tool
  limitation, not evidence the school is closed. I *did* independently read a secondary
  business-directory page (canpages.ca) myself, which lists address 1483 Topsail Rd, Paradise, NL
  A1L 1P9, phone 709-747-7077 — a genuinely different address from the other three Foley locations
  — but per the "never state evidence you didn't read on the school's own page" rule, I am not
  promoting this to a confirmed fact. **UNVERIFIED stands.**

**Conclusion: the Foley cluster is not a duplication error.** Three of the four are independently
confirmed at three distinct addresses with distinct genuine BJJ programs (one of the three,
AFAMA, is itself a legitimate multi-location operation, which is different from being duplicated
under four names). The fourth (Foley's Martial Arts, Paradise) has a plausible, differently-located
address from secondary sources but remains genuinely unconfirmed on a primary source — this is
appropriately conservative, not a red flag.

### NL CITY NOT PERMITTED

**Golden Rule Jiu Jitsu — Flat Bay, NL.** This is a new finding, not present in the research file.
Found via the secondary Coastline BJJ Collective directory (which listed it as "Golden Rule Jiu
Jitsu, Stephenville Crossing") and independently confirmed by reading the school's own page
(`golden-rule-jiu-jitsu-ltd.gymdesk.com`) directly myself: genuine "Adult BJJ" and "Brazilian Jiu
Jitsu Kids" classes, instructors listed by belt rank (including a black belt), address "9 Rushy
Pond Lane, Box 7, Site 12, Flat Bay, NL A0N1Z0" — read directly in the page footer, not from the
directory. **Flat Bay is not one of the ten permitted NL city strings** (St. John's, Corner Brook,
Gander, Paradise, Conception Bay South, Labrador City, Grand Falls-Windsor, Clarenville, Mount
Pearl, Torbay). Per C7c, a record in this city would silently render on the Nebraska page instead
of Newfoundland's. **Not recommended for addition.** Flagging only, per the addendum's instruction.

Two further, weaker leads surfaced in the same secondary directory but were **not** independently
confirmed on a primary source this pass (both Facebook-only): "Trigon Jiu Jitsu" (Port aux Basques
— itself one of the explicitly non-permitted cities named in the addendum) and "BTTT Blaketown Top
Team Jiu Jitsu" (Blaketown — also not a permitted city). Neither is asserted as real; both are
noted here only so a future pass knows to check them, and knows in advance that neither city is on
the permitted list even if confirmed.

No other candidate NL school in any other non-permitted city (Stephenville proper,
Happy Valley-Goose Bay, Carbonear, Bay Roberts, Marystown, Placentia, Deer Lake, Bonavista,
Springdale, Channel-Port aux Basques) was found by me this pass, consistent with research's own
negative search result.

### NL vs NEBRASKA NAME CHECK

Checked every name I am recommending for ADD or FIX-URL in Newfoundland against the twelve
Nebraska-suppressed names: Columbus NE BJJ, Fremont BJJ, Grand Island BJJ, Hastings BJJ, Husker
Combat Club, Kearney BJJ, Lincoln BJJ, Nebraska BJJ, Norfolk BJJ, Norfolk NE BJJ, North Platte BJJ,
Scottsbluff BJJ.

- Evolution Martial Arts NL — no collision
- St. John's BJJ — no collision
- Labrador City BJJ — no collision
- Golden Rule Jiu Jitsu (flagged, not recommended for addition) — no collision

**No NL recommendation collides with the Nebraska suppression list.**

### Nebraska — unchanged

Not researched, not touched, per the addendum. No proposal in this file affects any of Nebraska's
21 curated records.

## Prince Edward Island — confirmed vs overturned

**10 stored records. 6 non-REAL verdicts from research (4 REAL, 2 UNVERIFIED, 2 WRONG-URL/
WRONG-ENTITY, 1 GONE, 1 WRONG-ENTITY). All 6 independently reproduced; 0 overturned in verdict
category**, though I refined the recommended fix for "Stratford BJJ PEI" (see below) and confirmed
the O'Leary/Stratford/Summerside multi-location structure by reading `peimma.com` myself, location
by location.

| Record | Research verdict | My verdict | Changed? |
|---|---|---|---|
| PEI Brazilian Jiu Jitsu | UNVERIFIED | UNVERIFIED | No |
| Montague BJJ | UNVERIFIED | UNVERIFIED | No — DNS independently confirms it resolves; body still unreadable |
| Souris Brazilian Jiu-Jitsu | WRONG-URL | WRONG-URL | No — DNS independently confirms both .com and .ca dead |
| Stratford BJJ PEI | WRONG-URL | WRONG-ENTITY (refined) | Verdict label refined, same underlying fact and fix |
| Island Grappling Club | GONE | GONE | No |
| Summerside BJJ PEI | WRONG-ENTITY | WRONG-ENTITY | No |

The other 4 PE records (West River Jiu Jitsu, Charlottetown BJJ Academy, PEI Martial Arts Academy
Summerside, Wulfrun Martial Arts) were all independently re-read by me and confirmed REAL. No
changes.

### The PEI Martial Arts Academy multi-location resolution

I read `peimma.com`'s own home page and all three of its location sub-pages myself
(`/summmerside`, `/stratford`, `/oleary`) — note the home page itself has a typo, "summmerside"
with three m's, which is the *actual* live path.

**Confirmed: one business (PEI Martial Arts Academy, founded 2018 by Jason Saggo) trades at three
physical locations**, each with its own address, its own local schedule, and its own Facebook/
Instagram handle:

- **Summerside** — 50 Ashwood Ave, Slemon Park, C0B 2A0. Own schedule names "BJJ-GI," "BJJ NO-GI,"
  "KIDS BJJ" explicitly. Already correctly stored as "PEI Martial Arts Academy Summerside" — KEEP.
- **Stratford** — 41 Hollis Ave, Stratford, PE C1B 2S6. Own schedule names "KIDS NO-GI BRAZILIAN
  JIU-JITSU (10-15)" and "ADULT BRAZILIAN JIU-JITSU" explicitly. This is what "Stratford BJJ PEI"
  actually is.
- **O'Leary** — 424 Main St, O'Leary, PE C0B 1V0. Own schedule names "KIDS BRAZILIAN JIU-JITSU
  (8-15)" and "ADULT BJJ" explicitly. This location is not currently on the live PEI page at all —
  genuine NET-NEW.

**This confirms the task's structural warning was correct to raise, and the correct fix is a
naming-convention fix, not a bare rename.** The storage format matches on name alone, corpus-wide.
The existing live record is named **"PEI Martial Arts Academy Summerside"** — i.e., the location
name is baked into the record's own name field, not left to the city field alone. Given that
established convention:

- "Stratford BJJ PEI" should become **"PEI Martial Arts Academy Stratford"** (not a bare "PEI
  Martial Arts Academy," which would collide by name with the Summerside record).
- The new O'Leary record should be added as **"PEI Martial Arts Academy O'Leary"**, same
  convention.

Doing it this way produces three uniquely-named, uniquely-addressed records for one real business
with three real locations — which is the correct outcome, not a duplication error and not a
collapse into one record.

"Summerside BJJ PEI" (the second, URL-less Summerside stub) is a different problem: it does **not**
represent a fourth location. I found no business anywhere trading under that literal name; it is a
redundant placeholder duplicating the already-correct "PEI Martial Arts Academy Summerside" record.
Recommended action is SUPPRESS, not a URL fix.

### PEI NET-NEW — all three checked

- **JM Brazilian Jiu-Jitsu (Charlottetown)** — CONFIRMED REAL. Read `jmbjj.ca` directly: "Juliano
  Macário | Brazilian Jiu-Jitsu Charlottetown." Black belt, "World Championship in Brazil,"
  teaching in Canada since 2015. Address 21 Macaleer Dr, Charlottetown PEI — a genuinely distinct
  address from Charlottetown BJJ Academy's 152 Kent St. **ADD.**
- **PEI Martial Arts Academy O'Leary** — CONFIRMED REAL, see above. **ADD**, new city heading
  "O'Leary, PE." Note PEI carries no hardcoded-city-list constraint (that mechanism, C7, is
  specific to the NL/Nebraska entanglement) — O'Leary can be added as a normal new city.
- **West Prince BJJ (Alberton)** — **NOT independently confirmed.** Facebook-group-only presence
  (`facebook.com/groups/347453136338820`); the fetch aborted/returned nothing usable, reproducing
  the same Facebook-body limitation research reported. A secondary directory (Coastline BJJ
  Collective) and a competition-registration site (Smoothcomp, not opened by me) both name it, but
  I could not reach a primary source. **Held back — not added to the TSV as an ADD row.** This
  matches research's own caution; I am not overturning it to ADD without a primary read.

### PEI collision names — checked, none found

Cornwall PE, Stratford PE (aside from the resolved PEI MMA location above), Georgetown PE: I
specifically re-checked all three. No BJJ business was found in Cornwall PE or Georgetown PE, real
or otherwise — nothing to misfile, matching research's own negative result. Stratford PE correctly
resolves to the PEI Martial Arts Academy Stratford location, not to Stratford ON, Georgetown DE, or
Georgetown DC.

### CROSS-REGION DEBT

None found in either region this pass. No NL or PE candidate school was found to actually belong to
an already-curated region (VA, MD, ON, NJ, NC, MS, AR, WA, NH, SC, PA, OH). Saint John NB vs
St. John's NL was checked explicitly on every St. John's record — every address/postal code read
this pass was `A1*`/709, never `E2*`/506.

### PEI roster completeness

Per the addendum's explicit warning, PEI's roster was **not** inflated to hit a doubling ratio. Net
change from this pass: 10 stored records confirmed/corrected, plus 2 confirmed NET-NEW additions
(JM Brazilian Jiu-Jitsu, PEI Martial Arts Academy O'Leary), for a resulting roster of 12 records —
a modest, evidence-driven increase consistent with "a short honest roster is the correct output"
for this region.

## Held-back rows (both regions)

- **Foley's Martial Arts (Paradise, NL)** — UNVERIFIED, unread body despite exhausting every
  fetch variant I could try. Do not promote to REAL or attach an address without a future
  successful read.
- **Labrador City BJJ (NL)** — WRONG-URL confirmed (old domain dead), but the new candidate URL's
  content remains genuinely unread by any tool available this pass. Recommend the URL fix on strong
  circumstantial grounds (identical `/lab-city` subpath, matching secondary-directory citation) but
  flag that the business details (instructor name, lineage) are not independently confirmed.
- **PEI Brazilian Jiu Jitsu (Charlottetown)** and **Montague BJJ (Montague)** — both UNVERIFIED,
  unread bodies, held exactly as research left them.
- **Souris Brazilian Jiu-Jitsu (PE)** — WRONG-URL confirmed dead on both TLDs; strong but
  secondary-only evidence of ongoing operation; no live corrected URL found to recommend.
- **West Prince BJJ (Alberton, PE)** — held back from ADD; Facebook-only, unreadable this pass.
- **Trigon Jiu Jitsu (Port aux Basques, NL)** and **BTTT Blaketown Top Team Jiu Jitsu (Blaketown,
  NL)** — new leads surfaced via a secondary directory only, Facebook-only, unreadable this pass.
  Not asserted as real. Flagged for a future pass; note both cities are outside the ten permitted
  NL strings regardless of confirmation status.

## Budget / context statement

This pass used a moderate number of tool calls: roughly 45 direct page/DNS fetches and 6 WebSearch
calls across both regions (well under any budget cap I hit). I did not run out of context or
budget. The one recurring, genuine tool limitation — reproduced independently on this pass, not
just carried forward from the research file — is that Facebook and Instagram bodies, and a small
number of specific third-party domains (`foleysmartialarts.com`, `novauniaocanada.com`), return
completely blank content through the fetch tool regardless of path, protocol, or www variant tried,
including a reader-proxy workaround. Every row affected by this is explicitly marked UNVERIFIED or
carries an explicit caveat in the `evidence` column above — nothing from a blank-body fetch was
promoted to a confirmed fact. `archive.org` is confirmed blocklisted for this session (tested
directly, got an explicit permission-denied response), consistent with what research reported.

## NL CITY NOT PERMITTED

Golden Rule Jiu Jitsu — Flat Bay, NL (confirmed real, not recommended for addition; see detail
above). Trigon Jiu Jitsu (Port aux Basques) and BTTT Blaketown Top Team Jiu Jitsu (Blaketown) are
unconfirmed leads in likewise-non-permitted cities, flagged for a future pass only.

## NL vs NEBRASKA NAME CHECK

Checked all NL names recommended for ADD/FIX-URL (Evolution Martial Arts NL, St. John's BJJ,
Labrador City BJJ, Golden Rule Jiu Jitsu) against the twelve suppressed Nebraska names (Columbus NE
BJJ, Fremont BJJ, Grand Island BJJ, Hastings BJJ, Husker Combat Club, Kearney BJJ, Lincoln BJJ,
Nebraska BJJ, Norfolk BJJ, Norfolk NE BJJ, North Platte BJJ, Scottsbluff BJJ). **No collision found
with any of the twelve.**
