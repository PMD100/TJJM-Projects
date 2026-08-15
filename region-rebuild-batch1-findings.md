# Region rebuild — batch 1 research. Maine, Arkansas, Ontario. 7 Aug 2026.

Three research passes, ~6 minutes each. Purpose: decide whether the never-curated regions are
worth rebuilding, and calibrate the cost before committing to the remaining 28.

---

## The answer: yes, and by more than the link audit suggested

| region | currently listed | net-new schools found | would become | multiplier |
|---|---|---|---|---|
| Maine | 11 | 14 | ~24 | **2.2x** |
| Arkansas | 35 | ~30 | ~62 | **1.8x** |
| Ontario | 40 | ~95 | ~130 | **3.3x** |

**The ratio survived the test it was set.** Maine was the worst case — tiny, rural, 100% of links
broken — so its "half the schools are missing" result could have been an artifact of link rot.
**Arkansas disproves that**: only 5 of its 35 links were flagged, i.e. its links were largely
healthy, and it was *still* missing ~30 schools. Coverage and link rot are independent problems.
Ontario, the largest never-curated region, is the worst of the three.

Extrapolating from n=3 across the 513 records in the 31 stub-bearing regions, there are plausibly
**500–900 unlisted schools**. That is a far larger prize than the link cleanup that started this,
and it argues for treating region rebuilds as the main workstream rather than a follow-up.

---

## Findings that change how the stubs should be handled

**3 of Ontario's 11 stubs are real schools with a broken URL — not fake listings.**

| record | stored domain | actually |
|---|---|---|
| `Cambridge BJJ` | cambridgebjj**.com** — NXDOMAIN | real school at **cambridgebjj.ca**, 55 Raglin Pl. Wrong TLD. |
| `Oshawa BJJ` | oshawa**w**bjj.com — NXDOMAIN | real school at **oshawabjj.com**, 1160 Simcoe St S. **A literal typo — an extra "w" in the stored domain.** |
| `Windsor BJJ` | windsorbjj.com — NXDOMAIN | real school, JJ Machado affiliate, at **windsorbrazilianjiujitsu.com**, 4471 Tecumseh Rd E |

These want a URL fix and to keep the record. Blanking them would have been wrong.

**No Ontario suspect city was empty.** All 11 have live BJJ. Compare Maine, where Rumford and
Waterville genuinely had none, and Arkansas, where Pine Bluff had none. Region size predicts this.

**`kingstonbjj.com` resolves — to a BJJ club in Kingston upon Thames, ENGLAND** (Diccon Lynes BJJ
Ltd, UK company 12258505, classes at the British Legion near Surbiton). A name-matching domain
serving a real BJJ school on the wrong continent. Do not repoint to it. This is the wrong-entity
trap in its most seductive form — everything about it looks right except the country.

**The stub pattern is wider than the screen found.** Ontario has 8 further `<city> BJJ` records
that were NOT flagged, because their links happen to resolve: Barrie, Belleville, Brantford,
Burlington, Guelph, Sudbury, St. Catharines, Niagara. Two look suspect on other grounds —
`Guelph BJJ`/guelphbjj.com (no Guelph school trades under that name; Guelph has Royal City BJJ,
Omerta BJJ, Guelph MMA) and `Barrie BJJ`/barriebjj.com (a school does trade as Barrie BJJ, but its
site is **705bjj.com**). **A working link is not evidence the record is right.**

**One blanked link has a findable replacement.** `Four-Eleven Brazilian Jiu Jitsu` /Whitby was
blanked in Piece 1 as dead — correctly, the old domain is gone — but the school is live at
**fourelevenbjj.ca**. Generalises: some fraction of the 544 links blanked so far have discoverable
replacements. Blanking was the safe action; repointing is the better one. Worth a later pass.

---

## Confidence, per region — this determines what is safe to build

**Maine — mostly body-verified.** Ready to build, excluding: Gracie Barra Bangor (aggregator only,
no first-party site), GracieFighter Presque Isle (one 2022 news piece), Maine Jiu Jitsu Academy
Boothbay (JS-only site, no address), Southern Maine BJJ and The Outlet (Facebook only).

**Arkansas — mostly body-verified.** Ready to build, excluding the entries the researcher marked
weak: Fort Smith Dark Arts and Omega BJJ (no first-party site), Ru-Jitsu and Spa City (JS-only,
addresses aggregator-only), Kokoro (primarily Kenpo, instructor is a BJJ purple belt), Gracie Barra
Batesville (could not confirm operating). Also note **Gracie Jiu-Jitsu Springdale states on its own
page "This club is no longer active"** — do not add. Pine Bluff has no BJJ school at all.

**Ontario — NOT ready to build.** The researcher was explicit: only ~10 of the ~95 were opened and
body-read; the rest are search-derived, "mostly quoting the school's own site copy, but I did not
open each page." Those addresses are provisional. Ontario needs a verification pass before any of
it is written. It is also incomplete by admission — Toronto alone is claimed to have 100+ academies
and only ~8 net-new surfaced; Milton, Newmarket, Aurora, Brantford, Woodstock, Stratford,
Chatham-Kent, Timmins, Cornwall, Brockville, Owen Sound, Kenora, Orangeville and Bradford were not
swept at all.

---

## Recommended build order

1. **Maine + Arkansas together** — one snippet, one theme, one publish. ~44 net-new records.
2. **Ontario verification pass**, then build separately. It is worth ~95 records and deserves the
   extra pass rather than shipping provisional addresses.
3. **Re-screen all 40 Ontario records**, not just the 11 — the Guelph and Barrie cases show a
   working link does not mean a correct record.

## Method note for the remaining 28 regions

Two errors in my own briefs this batch, both caught by the researchers:
- I told the Arkansas agent the stubs were Conway, Fort Smith, Pine Bluff, **Jonesboro, Hot
  Springs**. The real ones are Conway, Fort Smith, Pine Bluff, **Russellville, Springdale**. I
  typed from memory instead of reading `B-stubs-ALL.tsv`. The agent validated all seven towns
  anyway, which turned out useful — Jonesboro and Hot Springs both have net-new schools.
- I asked for "AK" meaning Arkansas when AK is Alaska.

**Read the source file into the brief. Do not type region contents from memory.**
