# Batch 7 Verification — Nova Scotia (NS)

Verifying `research-b7-NS.md` against method rules in `METHOD-RULES-agent.md` and
`METHOD-RULES-batch7-addendum.md`. Every claim below was re-read by me this pass unless
explicitly marked secondary/unread. DNS screens used `https://dns.google/resolve?name=<host>&type=A`.
All fetches used `mcp__workspace__web_fetch`; no bash/curl/python was used.

## Headline result

Research's work held up much better on this pass than the batch's 46%/84% defect rates would
suggest — **zero fabricated evidence was found** (no invented lineages, ranks, or quotes; every
quoted sentence I checked against a school's own page matched verbatim). The defects here are
of a different kind: **one real research error (a conflated three-way identity)**, **two
premature UNVERIFIED verdicts that should have been REAL**, and **a laundering risk on the 13
leads that the research agent itself flagged and mostly avoided**, but which needed one more
level of digging to resolve properly (the "two independent directories" claim turned out to be
false).

## JOB 1 — the 7 non-REAL verdicts

All 7 re-verified independently. **4 confirmed unchanged, 3 overturned.**

**Confirmed GONE (4):** Shelburne BJJ NS, Stellarton BJJ, Atlantic BJJ, Cape Breton BJJ. I
re-ran DNS on every plausible domain for each name (including `.ca` variants and, for Shelburne,
the `shelburnebjjns.com` variant matching the stub's own name) — every single one returned
`Status: 3` (NXDOMAIN), conclusive. I also independently re-searched each town and cross-checked
against both the Josh Presley Feb-2025 roster (37 clubs) and the Coastline BJJ Collective
directory (39 clubs), both of which I read directly — neither lists a business under any of
these four names in these towns. No real school appears to be hiding behind any of these
stub names under a different domain. These are stale/erroneous entries and should stay
suppressed.

**Confirmed WRONG-ENTITY (1):** Halifax BJJ. I independently fetched both `halifaxbjj.com` and
`halifaxbjj.ca` myself. `halifaxbjj.com` resolves and canonicalises straight to `halifaxbjj.ca`,
serving an identical body: same title ("Halifax Brazilian Jiu-Jitsu Society"), same H1 ("HFX BJJ
Society"), same phone (902-209-8324), same email. This is one business, listed twice under two
domains. The business's own branding on its own page is unambiguous — it calls itself "Halifax
Brazilian Jiu-Jitsu Society" / "HFX BJJ Society", never plain "Halifax BJJ". **Recommend
suppressing the "Halifax BJJ" record and keeping "Halifax BJJ Society."**

**Overturned to REAL (2): Team Fortitude NS and Yarmouth BJJ.**

- **Yarmouth BJJ** — the stored `yarmouthbjj.com` is dead (DNS NXDOMAIN, re-verified). But I
  found and read a live replacement, `yarmouthbjj.ca`, myself: a full, currently-populated class
  schedule (Gi BJJ, No-Gi BJJ, two age bands of Kids BJJ, Muay Thai Kickboxing, Open Roll),
  address "73C Starrs Road, Yarmouth, NS B5A 2T6", email `yarmouthbjj@gmail.com`. This is about
  as clean a REAL as exists in this file. Action: FIX-URL from `.com` to `.ca`.
- **Team Fortitude NS** — the domain research treated as the site, `teamfortitudemma.ca`, is
  **also actually dead** (DNS NXDOMAIN on both apex and `www`, verified twice). An earlier fetch
  to that URL had returned an empty-but-non-erroring response, which is misleading — DNS is the
  authority here, not fetch success/failure, and DNS says the domain does not exist. Despite
  that, I found strong evidence the club is real and current: **Halifax BJJ Society's own
  Affiliates page**, which I read directly, currently links `facebook.com/FortitudeJiujitsu` as
  an active affiliate. That is a primary source (the hub gym's own, actively-maintained partner
  list) confirming the spoke gym exists today — a materially different and stronger signal than
  "two directories agree." I could not read Team Fortitude's own Facebook body (the tool cannot
  render Facebook), so the address and instructor name remain secondary-sourced only. Action:
  FIX-URL — drop the dead `.ca` domain, point to the Facebook page.

## JOB 2 — the 13 secondary-source-only leads

**Zero of the 13 assigned leads were promoted to a clean ADD on their own evidence. One
(Bulldog Martial Arts) was promoted via an unusual, explicitly-flagged first-party corroboration
route (see below). One record (Marmac/Mountain/Porters Lake) was resolved as a research error,
not promoted or rejected as a single thing.**

### The corroboration problem is worse than research realized

Research treated "the Feb-2025 NS-clubs roster" (Josh Presley's Substack, `joshpresley.substack.com`)
and "the Coastline BJJ Collective directory" as two independent sources whose agreement was
meaningful corroboration. **I read Presley's post directly and it says, in its own text:**
*"(Thanks to Coastline BJJ blog for the help.)"* **— the two directories are not independent.**
One was compiled with the other's assistance. Every place in the research file (and in my own
work) where "both directories agree" was cited as support, that support is weaker than it
looked — it may be one underlying data source counted twice. This is the single most important
methodological finding of this pass, and it's why almost none of the 13 could be promoted:
Facebook and Instagram bodies never render through `mcp__workspace__web_fetch` (I tested this
against six distinct URLs across the pass — every single one returned empty), so directory
agreement, even if it were independent, was never going to be enough on its own per the
addendum's explicit rule against laundering directory listings.

### What happened to each of the 13

- **Woodshop Jiu-Jitsu (Antigonish)** — UNVERIFIED. Facebook only, unrenderable.
- **Shiretown Grappling Club (Pictou)** — UNVERIFIED. Instagram only, unrenderable.
- **Samson Martial Arts & Fitness (St. Peter's)** — UNVERIFIED, but notable: it has its own
  domain, `samsonmartialarts.com`, unlike most of the other 12. Every page I tried (home,
  about-us, programs, contact) returned an empty body — it's a JS-rendered site our fetch tool
  can't execute, not a dead domain. This is the strongest "try again with a better tool" candidate
  of the batch. Also worth flagging: Coastline's directory links a mismatched Facebook handle
  (`facebook.com/PIRATESWAYBJJ`) for this listing — a live example of exactly the kind of
  directory unreliability the task warned about.
- **SOB (Sprawl or Brawl) MMA (Glace Bay)** — UNVERIFIED. Instagram only, unrenderable, and the
  addendum's "MMA name needs a genuine-BJJ check" caution is unresolved.
- **Workhorse Mixed Martial Arts (Port Hawkesbury)** — DROP. This one is *not* even
  non-independently double-sourced — it appears only in the Coastline directory and is entirely
  absent from Presley's roster. Weakest evidence in the set of 13.
- **Marmac / Mountain / Porters Lake Brazilian Jiu-Jitsu** — **resolved as a research error, not
  a record.** See dedicated section below.
- **Manimal Athletics Training Center (Lucasville)** — UNVERIFIED. Has its own domain
  (`manimalathletics.com`) but, like Samson's, every page returned an empty JS-rendered body.
  Secondary description calls it a "private, members only" studio — a flag worth resolving before
  adding, since "members only" cuts against a walk-in-accessible directory listing.
- **True Leverage Alliance BJJ (Kingston/North Alton)** — UNVERIFIED. See dedicated section below.
- **The Tap Room Grappling Group (Middle Sackville)** — UNVERIFIED. Facebook only, unrenderable.
- **12 Wing Brazilian Jiu-Jitsu (Eastern Passage/Shearwater)** — UNVERIFIED. See dedicated
  section below; this is the best-evidenced "exists and operates" case of the 13, but it's gated
  on a different question entirely.
- **Bulldog Martial Arts (East Hants/Lantz)** — **ADD.** See dedicated section below.
- **Dragon Martial Arts Colchester (Kemptown)** — UNVERIFIED. Facebook group only, unrenderable.
- **Cheticamp Martial Arts (Petit Etang)** — UNVERIFIED. Instagram only, unrenderable.

### The Marmac / Mountain / Porters Lake identity, resolved

This was written up as one three-way-slash record with two cities, which the task correctly
flagged as an unresolved identity rather than a record. Having read both underlying directories
myself, this is **two completely separate, unrelated businesses that got merged by mistake**:

1. **Marmac Athletics (Truro)** — 36 Inglis Place, Truro. `facebook.com/marmacathletics`. This
   would be a *second* Truro-area school alongside the existing "Truro BJJ" record, if ever
   confirmed. Nothing to do with Porters Lake.
2. **Mountain Jiu-Jitsu / Porters Lake Brazilian Jiu-Jitsu** — one club, 5775 NS Trunk 7,
   Chezzetcook (the Porters Lake area), instructor Shaun Gillis (BJJ brown belt). Presley's roster
   names it "Mountain Jiu-Jitsu"; Coastline's directory names it "Porters Lake Brazilian Jiu
   Jitsu"; **both point to the exact same Facebook URL**, `facebook.com/averageday` — so it's
   genuinely one club with an unsettled trading name, not two clubs.

Neither could be primary-verified this pass (Facebook unrenderable). Both are recorded as
separate UNVERIFIED rows in the TSV, and the combined three-way name is explicitly marked DROP
so it cannot accidentally get entered into the corpus as written.

### True Leverage Alliance BJJ — Kingston trap, resolved; address, not resolved

The addendum specifically flags Kingston as a trap name (`kingstonbjj.com` and
`kingstonjiujitsu.com` are both Kingston-upon-Thames, England). This one is genuinely **Kingston,
Nova Scotia** — an Instagram bio search result tags the account "Kingston, NS," and a Coastline
"Club Spotlight" interview blog post (a richer secondary source than a plain directory row)
independently describes an Annapolis Valley founding story (Windermere and Millville, 2019),
which is consistent geography, not a coincidence. So the region trap is cleared.

What is *not* resolved: the street address conflicts between sources — "165 Bridge Street, North
Alton" (Presley/Coastline) versus "659 Victoria Rd, Aylesford" (an independent business
directory found via search). I did not pick one; both are reported so a future pass with FB/IG
access can settle it. The city-string question the task asked about (Kingston vs. North Alton)
is likewise unresolved without a primary read — the club brands itself "Kingston" per every
source, while its street address sits in North Alton or Aylesford depending on source. Given the
address conflict alone, this stays UNVERIFIED, not ADD.

### 12 Wing Brazilian Jiu-Jitsu — the best-confirmed existence, but gated on access, not evidence

This is the one lead in the batch where I found genuinely strong, non-directory, first-party-adjacent
evidence: **CFB Halifax's own base newspaper, the Trident** (`tridentnewspaper.com`), publishes
its own articles about this club, and I read one directly — it describes the club meeting
Monday–Thursday at 6 p.m. in the Shearwater Fitness and Sports Centre, names its team captain and
coach, and explicitly invites people to "give Jiu-Jitsu a try" by contacting the coach. Separately,
**Halifax BJJ Society's own current Affiliates page** — which I read directly — lists
`instagram.com/12wingbjj` as an active affiliate today, which independently confirms the club
still exists in 2026, not just in the 2019 article.

None of that resolves the actual gating question the addendum asks about: **can a civilian
without a base pass or DND sponsorship actually walk in and train?** CFB Shearwater is a working
military base. The Trident article's invitation is ambiguous on this point — it may mean "anyone
already able to access the base" rather than "anyone at all." I found no explicit statement
either way. Per the addendum's explicit instruction (modelled on the Alaska JBER case), that
ambiguity is disqualifying on its own regardless of how well the club's existence is confirmed.
**Verdict: UNVERIFIED, held back specifically on the access question, not the existence
question.** The same reasoning applies to Hero Grappling Club (CFB Halifax), carried forward from
the prior pass's held-back list though not one of the 13 assigned leads.

### Bulldog Martial Arts — the one promotion, and why it's different from the other 12

I'm promoting this one to **ADD**, and I want to be explicit about why it's treated differently
from the other 12 rather than silently applying a double standard.

The distinguishing fact: **Halifax BJJ Society's own current Affiliates page** (a primary source
I read directly, not a directory) links `facebook.com/groups/206127349417091` as an active
affiliate today — and that is the *exact same* Facebook group ID that both secondary directories
independently attach to "Bulldog Martial Arts (East Hants)." That's not two directories echoing
each other; it's the hub gym's own vetted, currently-maintained partner list independently
matching a unique identifier found elsewhere. I treat that as qualifying first-party
corroboration in the spirit of the rule (confirms an active, current relationship) even though I
could not read Bulldog's own Facebook body directly. I applied the identical logic to Team
Fortitude NS in Job 1 above, for consistency.

What I did *not* verify myself: the address (1076 Hwy 2, Lantz NS B2S 1M8, at the East Hants
Sportsplex) and the specific class mix (BJJ + Kickboxing + Uechi-Ryu Karate) come from a
secondary community-services directory (`cioc.ca`), not a primary page. I've flagged that
explicitly in the TSV. If a stricter reviewer disagrees with treating a hub gym's affiliate page
as sufficient, this row (and Team Fortitude's REAL verdict in Job 1) should both be downgraded
back to UNVERIFIED together, since they rest on the identical reasoning.

Recommended city string: **"Lantz"**, the specific town, not "East Hants" (the municipality) —
consistent with how Wellington, Greenwich, and other small-town NS records are already handled on
the live page.

### Leads outside the assigned 13 that surfaced along the way

Two things surfaced during this pass that are worth naming even though they weren't in scope:

- Halifax BJJ Society's own Affiliates page also links `quantumjj.com` and `terabjj.com` —
  locations unchecked this pass, flagged as leads for a future NS pass, not asserted as NS.
- The same page links `charlottetownbjj.com` (clearly PEI) and `frederictonbjj.com` (clearly NB).
  These were never NS candidates, so this is not cross-region debt in the strict sense of a
  misfiled NS record — it's just an informational note in case it's useful to the PE/NB verifiers
  working the same batch.
- **CROSS-REGION DEBT: none found.** Every NS record kept in this file, existing or new, has
  explicit NS region evidence I read myself (a `B*` postal code, a `902` area code, or explicit
  "Nova Scotia" text on the page). Windsor, Kingston, Sydney, Liverpool and Amherst were all
  specifically checked against their named collision risks and all resolved to Nova Scotia.

## JOB 3 — Abhaya Martial Arts Academy (Windsor)

**Verdict: ADD.** I read `abhaya.ca/windsor` directly. The page states plainly: "Abhaya Martial
Arts Academy (Abhaya Windsor) offer classes in Brazilian Jiu-Jitsu and Judo... located in the
Fort Edward Armory at 62 Ford Edward Street, Windsor, Nova Scotia." Instructor Chris Robinson
holds black belts in both Judo and BJJ; the class schedule includes a genuine adult BJJ class
(Monday and Wednesday evenings) alongside Judo and kids' classes — this clears the addendum's
"judo-only or kids-only-BJJ-at-a-TKD-school" rejection bar. Region is explicit and unambiguous:
"Windsor, Nova Scotia" in the page's own text, not Windsor ON or Windsor England.

**The spelling resolves in favour of the armoury's name, against Abhaya's own page.** Abhaya's
page reads "Fort Edward Armory" but then gives the street as "**Ford** Edward Street" — a
transposition. I checked this against Parks Canada's own contact page for Fort Edward National
Historic Site (an authoritative civic source, read directly): its official site address is
"**67 Fort Edward Street**, Windsor, Nova Scotia, Canada, B0N 2T0." So there are actually *two*
small errors on Abhaya's own page: "Ford" should be "Fort," and the house number "62" is very
likely a typo for "67" (Presley's independent roster also gives "67," while separately keeping
the same "Ford" spelling typo — consistent with the number being right and the street name being
copied from a source with the same spelling error). I've recorded what Abhaya's page literally
says as the read evidence and flagged the correction separately, per the method rule to record
what was actually read.

**Two genuinely separate Abhaya locations, confirmed.** Abhaya's own site navigation lists
"Abhaya Greenwich" and "Abhaya Windsor" as two distinct pages, each with its own address (38
Highway 358, Greenwich vs. 67 Fort Edward Street, Windsor — roughly 40 km apart), own class
schedule, own instructor, and own phone number, with a note that members can train at either
location on an unlimited membership. This is not a duplicate listing.

## Recommended Halifax-area city-string convention

Dartmouth, Bedford and Lower Sackville should each keep their **own** city heading, separate from
"Halifax." This is already how the live page and the existing REAL records in this file are
consistently treating them (Fit Plus, Grant's, and Tower 1 are all "Dartmouth, NS"; Clinch
Training Centre is "Lower Sackville, NS"), and it matches the addendum's own guidance that these
are "conventionally listed as their own cities" despite being inside HRM. I'd extend the same
logic explicitly to **Middle Sackville** (The Tap Room Grappling Group, unverified) as a further
distinct string from both "Lower Sackville" and New Brunswick's "Sackville" — three different
places that must never collapse into one heading. No Bedford candidates surfaced this pass, so
there was nothing to test that convention against directly, but the same rule should apply if one
appears.

## Budget / context statement

This was the largest job in the batch and I spent the bulk of my tool budget on it accordingly:
roughly 45 direct fetches (page bodies and DNS lookups) plus about a dozen targeted web searches,
concentrated on (a) re-reading every existing REAL record's own page rather than trusting the
prior pass's quotes, (b) DNS-verifying every GONE call and every plausible replacement domain,
and (c) attempting a first-party read on all 13 leads before falling back to secondary sources.

I did **not** run out of budget, but I am flagging two honest limitations:

1. **Facebook and Instagram never rendered through `mcp__workspace__web_fetch` this pass** — I
   tested this against six distinct URLs (`facebook.com/FortitudeJiujitsu`,
   `facebook.com/woodshopjits`, `instagram.com/shiretownbjj`, `facebook.com/averageday`,
   `instagram.com/cheticamp_martial_arts`, and one more) and every one returned an empty body.
   This is a tool limitation, not a shortcut, and it is the reason 10 of the 13 leads and both
   military-base clubs remain UNVERIFIED rather than ADD or DROP — I could not reach a first-party
   body for any of them no matter how I tried.
2. **Two domains that DO exist rendered empty anyway** (`samsonmartialarts.com` and
   `manimalathletics.com`) — these appear to be JS-rendered sites the fetch tool can't execute,
   distinct from the Facebook/Instagram limitation. Both are flagged as the best candidates to
   retry in a future pass with a JS-capable fetch tool, since they're independent domains, not
   directory listings.

Every row in the TSV is covered — all 7 Job 1 records, all 16 previously-REAL records I
re-checked, the Job 3 net-new, all 13 assigned Job 2 leads, plus 4 directly-relevant extra rows
(the Marmac split, Bulldog, Hero Grappling Club) carried over from the prior pass's held-back
list because they bear on the same questions the task asked about.
