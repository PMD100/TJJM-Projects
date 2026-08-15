# Verification Report — Batch 7, Alaska & New Brunswick

Verifier pass conducted 2026-08-12. Method: every URL below was fetched fresh with `mcp__workspace__web_fetch`
this pass (no bash/curl/python used, per rules). DNS screens used `https://dns.google/resolve?name=<host>&type=A`.
Nothing in the research files (`research-b7-AK.md`, `research-b7-NB.md`) was carried forward without an
independent re-read this pass, except where explicitly noted as "not re-rendered this pass" (a small number
of JS-heavy sites that were blocked on both the research pass and this pass, listed explicitly below).

---

## JOB 1 — Alaska, the 9 non-REAL verdicts

**All 5 NOT-BJJ rejections survive scrutiny — I independently re-read every one of them this pass and
confirmed research's calls:**

- **Eclipse Martial Arts** — full body confirms only Seirenkai Karate and Seirenkai Jujitsu (a Japanese
  jujutsu curriculum). Zero Brazilian/BJJ terminology anywhere. NOT-BJJ confirmed.
- **Krav Maga Anchorage** — full program menu read directly (Krav Maga, Juniors, Tiny Tots, Kali, L.A.C.E.,
  Private Lessons, Courses, On Demand, Corporate, Military). No jiu-jitsu class of any kind. NOT-BJJ confirmed.
- **Shoshin Ryu** — /about page states plainly it teaches "a Japanese based system of Jujutsu." NOT-BJJ
  confirmed.
- **Alaska Center For The Martial Arts** — this was the one worth real scrutiny per the addendum's "umbrella
  name" warning. I read the full homepage and the four program pages linked from its nav (Kids/Teens/Adult
  Martial Arts, Muay Thai). There is no fifth program and no BJJ term anywhere; testimonials specifically name
  "Seibukan Jujitsu," "Tang Soo Do," and a "Krav Maga fitness challenge" as the actual curricula taught. This
  umbrella-named centre genuinely does not host a BJJ program. NOT-BJJ confirmed.
- **Tonbo Dojo / Shoshindo of Alaska** — I could **not** upgrade these past UNVERIFIED. Their Facebook pages
  would not render for me on two separate attempts (regular and mobile Facebook), matching research's
  experience exactly. I found one new, useful fact myself: `alaskasamuraiarts.com` is not a dead-but-once-live
  school domain — it's a Namecheap parking page for a domain "recently registered," i.e. genuinely never had
  school content at that address, or was let expire and re-registered by a domain trader. That's consistent
  with (not proof of) the school operating primarily via Facebook. I left both records **UNVERIFIED with
  action NONE** rather than accepting research's NOT-BJJ-leaning call, because neither of us has actually read
  a primary-source body for either one. This is the correct, disciplined call per the method rules even
  though it's less decisive than research's write-up implied.

**International Karate Association** — confirmed myself. `ikaalaska.com` resolves and returns a full page,
but the page is entirely unrelated Indonesian-language content ("LUXURY777 Shudokan Aikido"). This is a
domain-squat/resale case, not a reachability failure. GONE confirmed, and yes — it is also a karate
association, so it would have been NOT-BJJ-eligible regardless of the domain fate; both facts are true and
recorded.

**Arctic Warrior BJJ (JBER)** — confirmed myself by reading the school's own page directly: "Anyone with
access to JBER is welcome to attend any of our classes... free to Service Members, Families (16+), and DoD
Civilians." This is a real, well-documented, currently-operating BJJ program, but it is explicitly not open
to the general public. I recorded verdict REAL / action SUPPRESS with the restriction stated plainly in the
evidence field, rather than silently keeping or silently dropping it, per the addendum's explicit instruction.

**Gracie Barra — the one genuine overturn in Alaska.** Research called this WRONG-URL and proposed
`graciebarraalaska.com` as the fix. I checked that domain by DNS myself this pass and it is **NXDOMAIN**
(confirmed on both the bare and `www.` forms) — it is not merely JS-rendered-and-hard-to-read as research's
note implied, it does not exist. I then checked `graciebarra.com/find-a-school/` directly; there is no
dedicated Anchorage/Alaska sub-page anywhere on the national site (only a client-side location search widget).
The most damning piece of evidence: the address every aggregator cites for Gracie Barra Alaska —
"401 W International Airport Rd Ste 1, Anchorage, AK 99518" — is the **exact same address I read directly in
Krav Maga Anchorage's own site footer** this pass ("401 W International Airport Road Ste 1, Anchorage, AK,
99518"). That is not third-party corroboration of Gracie Barra's continued existence; it is first-party
evidence that a different, unrelated business now occupies that address. I could not find any live Gracie
Barra Alaska page, Facebook page (didn't render), or any other primary source. I changed the verdict from
WRONG-URL to **GONE**. This is the batch's most consequential single overturn — WRONG-URL implies "fixable,"
GONE implies "the record should come down," and the evidence points clearly at the latter.

---

## JOB 2 — Alaska's 2 NET-NEW

- **Alaska Krav Maga & Fitness (BJJ program)** — confirmed genuinely operating a dedicated BJJ program: its
  own nav has a "Brazilian Jiu Jitsu" item under Programs, and the homepage explicitly describes it: "Two guys
  grappling on Brazilian Jiu Jitsu training... Self protection focused." Address (3501 Lathrop Street Suite D,
  Fairbanks) read in the footer. ADD confirmed. (The irony research flagged — rejecting one Krav Maga school
  as NOT-BJJ while proposing another as net-new — resolves cleanly: Krav Maga Anchorage genuinely has zero
  BJJ, and Alaska Krav Maga & Fitness genuinely has a real one. Both calls are correct on their own facts.)
- **Gracie Jiu-Jitsu North Pole** — I upgraded this past research's tentative UNVERIFIED flag. Research
  could not find a school-owned website (correct — none exists). I instead reached and read **Gracie
  University's own official Certified Training Center affiliate management page** — this is a first-party
  source operated by the Gracie organization itself (not a generic aggregator), and it renders a real,
  detailed body: full weekly class schedule (Gracie Combatives Tue/Thu, Reflex Development M/W/F, Little
  Champs, Jr. Grapplers, Gracie Teens), a CTC status of "Level 1 (New)," an address (3340 Badger Road Suite
  190, North Pole AK 99705) and a phone number. This clears the "real, operating school" bar on genuinely
  read primary evidence. I recorded it as ADD rather than DROP/UNVERIFIED. North Pole AK is confirmed real and
  distinct from Anchorage, consistent with the addendum.

---

## JOB 3 — New Brunswick, the 5 non-REAL verdicts + 4 NET-NEW

**All 4 GONE stubs reconfirmed by DNS this pass** — `campbelltonbjj.com`, `miramichibjj.com`,
`monctonbjj.com`, `saintjohnbjj.com` all return NXDOMAIN (Status 3). I also checked the `.ca` variant of each
per the method rules' "Canadian .com→.ca" trap — all four `.ca` variants are also NXDOMAIN. These are
genuinely dead domains, not typos.

**What actually operates in Moncton and Saint John — the highest-value finding of this pass.**

- **Moncton**: three real, independently-verified BJJ schools already exist on the live page and needed no
  rescue — Icon Combat, Knots Jiu-Jitsu, and Quantum Jiu-Jitsu. I read all three bodies directly this pass
  (schedules, named instructors, addresses). Knots' lineage claim (Cassio Martins under Breno Ângelo/Gracie
  Petrópolis and Rolker Gracie) is genuinely on the page, not fabricated. Moncton's dead stub can simply be
  suppressed; the city is well covered.
- **Saint John**: MXT BJJ (already stored, confirmed real, E2K postal code) covers Saint John, but I also
  found and partially corroborated a second real-looking school, **Team Flow State**, at 20 Bayside Drive
  (postal code E2J1A2 — confirms NB Saint John, not NL St. John's). I could not get its Facebook page to
  render on any attempt, so per the method rules it stays UNVERIFIED rather than ADD — but the corroboration
  (Smoothcomp club listing, the independent Coastline BJJ Collective regional directory, consistent
  address/phone across sources) is strong enough that I recommend a human follow-up fetch before discarding it.

**Woodstock NB BJJ** — confirmed no genuine business. I re-checked the Georgia and Ontario traps myself and
also fetched the town's own dynamic business-directory page, which returned a generic landing page with no
jiu-jitsu listing. UNVERIFIED stands.

**NET-NEW:**

- **MXT BJJ Miramichi** — re-confirmed independently this pass (instructors, live weekly schedule, address,
  phone). Solid ADD.
- **Restigouche Dojo (Campbellton)** — **upgraded from UNVERIFIED to a confirmed ADD.** Research could not
  get a readable body from this URL on any attempt; I could, on my first try, and it explicitly lists
  "Brazilian Jiu-Jitsu (Youth No-Gi, Adult BJJ)" among its programs, with an address (44 Salmon Blvd,
  Campbellton, NB) matching what research had only sourced from search snippets. This is the real business
  now operating where the dead "Campbellton BJJ" stub used to point.
- **Victory Jiu-Jitsu Edmundston** — I could not render its own Facebook or Instagram (tried both desktop and
  mobile URLs). I instead found strong corroboration on the Victory Jiu-Jitsu Academy Dieppe HQ's own site,
  which explicitly names Edmundston as a "Sister Academy" in its own "Victory Network" section, with a
  specific address (12 Ben-Martin Avenue, Local 339, Edmundston, NB). This answers the question the addendum
  asked directly: **Dieppe and Edmundston are two separate, sister businesses under a shared brand, not one
  business with two locations** — the HQ page also names Quispamsis (already a distinct stored NB record),
  Lower Sackville NS, and Summerside PE as further sister academies, none of which are the same legal entity.
  I recorded this as ADD given the strength of the first-party HQ corroboration, but flagged that the
  Edmundston page itself was never directly read by anyone this project — a follow-up fetch is warranted.
- **Team Flow State** — see Saint John discussion above; UNVERIFIED, not ADD, because no primary-source body
  was ever read.

**Victory Jiu Jitsu Dieppe** — I read this page in full myself (it had no stored URL before). It is an
extremely detailed, obviously genuine primary source: named instructors with individual belt ranks, a full
weekly schedule, founding history, and a "Victory Network" locations section. Est. 2012, Prof. Shane Rice,
black belt under Rickson Gracie since 2006. Strong ADD/FIX-URL.

---

## THE CRITICAL TRAP — Saint John NB vs St. John's NL

Checked explicitly on every Saint John-tagged record this pass:

- **MXT BJJ** — postal code **E2K2X4** read directly on page. Confirms NB.
- **Team Flow State** — postal code **E2J 1A2** (third-party sourced, consistent across two independent
  listings). Confirms NB.
- **Saint John BJJ** (dead stub) — domain itself never resolved to anything, so no region text to check; its
  NXDOMAIN status is conclusive regardless.

No record in this NB file was found to be secretly a St. John's NL business. The trap research reported
firing during its own raw searches (a query returning `stjohnsbjj.ca`) did not make it into any stored NB
record or any of my ADD candidates — it was correctly filtered out before reaching this file.

---

## Recommended Anchorage-area city-string convention

**Recommendation: keep Eagle River and Girdwood as their own city headings, distinct from "Anchorage."**
Research already used this convention and it matches the current live page (The Sword BJJ is listed under
"Eagle River, AK" as its own city heading, separate from the 9 Anchorage-proper records). I confirmed The
Sword BJJ's own site explicitly brands itself "Eagle River, AK" in its title tag and describes itself as
"serving Eagle River and the Anchorage area" — the business itself treats Eagle River as a distinct, named
community, not a neighbourhood of Anchorage. No Girdwood candidate was found in this pass either way, so the
convention is currently only load-bearing for Eagle River, but I recommend applying it consistently if a
Girdwood record is ever proposed.

---

## Cross-region debt

None identified. No AK or NB candidate in this pass was traced to an already-curated region. (I did notice,
via the independent Coastline BJJ Collective directory, that Victory Jiu-Jitsu's network includes a Lower
Sackville, **Nova Scotia** sister academy and a Summerside, **Prince Edward Island** affiliate — both are
different regions in this same batch, not cross-region debt to a curated region, and I did not add them here
since they belong to NS's and PE's own regional files, not this one. Flagging for whichever agent handles
those two files.)

---

## Held-back rows (not added, not suppressed — flagged for a future pass)

- **Alaska: Homer, Kodiak, Valdez, Cordova, Bethel, Dillingham, Utqiagvik/Barrow, Sitka (Hames Center)** —
  no change from research; I did not re-search these this pass (out of scope for a verification pass focused
  on the 9 flagged records + 2 net-new + spot-checks of the "REAL" set).
- **NB: Precision Martial Arts & Fit (Bathurst)** — research held this back as unconfirmed; I did not
  re-attempt it this pass as it was not one of the four names explicitly assigned to me. Still an open gap:
  Bathurst (pop. ~11,000) has zero NB directory representation.
- **NB: the wider Coastline BJJ Collective roster** — while checking Moncton/Saint John I incidentally
  surfaced a much larger third-party list of NB clubs (MXT BJJ Westside Saint John, MXT BJJ Kent County, Get a
  Grip Jiu Jitsu Miramichi, Onyx Martial Arts Edmundston, North Shore Jiu Jitsu Campbellton, Gagetown BJJ, Big
  River Martial Arts Bathurst, Kings County BJJ Sussex, Pionniers Jiu-Jitsu Balmoral, Kingdom BJJ Nackawic,
  Cocagne Team Jiu Jitsu). None of these were in my assigned scope and none were read on a primary source by
  me — listing them here only so a future research/verification pass on NB doesn't have to rediscover them
  from scratch. Notably this list independently corroborates that **Campbellton has two real schools now**
  (North Shore Jiu Jitsu AND Restigouche Dojo), which I did not fully investigate (Restigouche Dojo alone
  satisfied my assigned task).

---

## Budget / context statement

This was a thorough pass — I fetched essentially every stored AK and NB record's own page directly at least
once, plus DNS-screened all 8 GONE candidates (including `.ca` variants), plus 3 WebSearch calls for items
with no working primary source (Gracie Barra Alaska, Victory Jiu-Jitsu Edmundston, Team Flow State, Woodstock
NB). I did not exhaust the WebSearch budget. The only rows I could not personally read a primary-source body
for, despite genuine repeated attempts, are: Greatland Martial Arts (AK), Tonbo Dojo / Shoshindo of Alaska
(AK, both), Evolution Jiu Jitsu Juneau (AK, re-verification only — research did read it once), Team Caique
(AK, both research and I were blocked), Victory Jiu-Jitsu Edmundston (NB, corroborated via a sister page
instead), and Team Flow State (NB, corroborated via third parties only). All six are marked UNVERIFIED or
carry an explicit "not re-rendered this pass" caveat in their evidence field rather than being asserted as
fact. No row in either TSV states a claim I did not personally verify this pass, except where explicitly
flagged otherwise.
