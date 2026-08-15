# Maine region rebuild — PILOT. Findings, 7 Aug 2026.

Pilot for Piece 2 of the link audit: the 174 city-stub records across 31 never-curated regions.
Maine chosen because it is the smallest region on the board and the worst ratio — **11 listed,
11 flagged, 100%**.

Cost of this pass: one research agent, 73 tool calls, ~6 minutes. That is the calibration number
for the remaining 30 regions.

---

## Headline

**Maine currently lists 11 schools. Of those, 6 already had their dead links blanked, and the
remaining 5 all point at NXDOMAIN domains. Not one Maine listing carries a working link today.**

The research found **at least 20 BJJ schools actually operating in Maine**, of which **14 are
net-new** — never listed at all. Maine should be roughly **11 → 24 listings, every one with a
real URL and a street address.**

That is the same shape as the NY import (64 → 182) at a twentieth of the size.

---

## The 5 city-stub records — all 5 domains are NXDOMAIN

But the stub NAME pattern was, again, not a verdict. Three of the five towns do have a real school;
it is simply called something else.

| stub record | domain | is there a school in that town? |
|---|---|---|
| `Ellsworth BJJ` | dead | **YES, two** — Acadia Brazilian Jiu-Jitsu (385 High St STE H) and Rolls Jiu Jitsu (249 Bucksport Rd) |
| `Saco BJJ` | dead | **YES** — Evolution Athletix, 4 Cascade Rd, with a live Gi BJJ schedule |
| `Presque Isle BJJ` | dead | **PROBABLY** — GracieFighter Presque Isle, 497 Main St. ⚠️ evidence is a Nov 2022 local-news opening piece; the parent Caribou site's own body never mentions Presque Isle. Unconfirmed. |
| `Rumford BJJ` | dead | **NO standalone academy.** Jiu-jitsu appears only as a class inside DWFitness / Berserkers MMA at the Greater Rumford Community Center. Search-snippet only. |
| `Waterville BJJ` | dead | **NO — not in Waterville proper.** Nearest are Huard's Ju-Jitsu (Winslow, across the river) and Bearclan Jiujitsu (Oakland). Huard's markets to "Waterville and surrounding areas" but its own contact block says Winslow. |

**This is the third time the city-stub pattern has failed as a verdict** — after `Brooklyn
Brazilian Jiu Jitsu` and `Binghamton Brazilian Jiu Jitsu`, both real. Treat it as a
prioritisation signal only. Two of five here really were empty; three were not.

---

## The 14 net-new schools

Every one verified from its own site body unless noted.

| school | town | address | website |
|---|---|---|---|
| Rolls Jiu Jitsu | Ellsworth | 249 Bucksport Rd | rollsjiujitsumaine.com |
| Bar Harbor Brazilian Jiu Jitsu | Bar Harbor | 12 Bethany Lane | barharborbjj.com |
| Graciefighter Jiu Jitsu | Caribou | 118 Bennett Dr | graciefightercaribou.com |
| Huard's Ju-Jitsu & Karate | Winslow | 234 Clinton Ave | huardsmartialarts.com |
| Bearclan Jiujitsu | Oakland | 826 Kennedy Memorial Dr | bearclanjiujitsu.com |
| The Foundry Brazilian Jiu Jitsu | Farmington | 218 Fairbanks Rd | foundrybjj.com |
| Stonecoast Brazilian Jiu Jitsu | Portland | 131 Johnson Rd | stonecoastbjj.com |
| Gracie Barra South Portland | South Portland | 798 Main St Suite 9B | graciebarrasouthportland.com |
| Alexey Pickerell BJJ | Westbrook | 90 Bridge St #335 | alexeybjj.com |
| Gracie Gym Maine | Windham | Route 302 (no street number published) | graciegymmaine.com |
| Empire Brazilian Jiu Jitsu | Freeport | 15 Depot St | empirebjjmaine.com |
| Brunswick Martial Arts Academy | Topsham | 126 Main St Suite 5 | brunswickmartialarts.com |
| Flow Brazilian Jiu Jitsu | Rockland | 4 Cedar St | flowbrazilianjiujitsu.com |
| Port City BJJ | Kittery | 280 Route 1 | portcitybjj.com |

## Existing records that map to a real school under a different name

These need a rename, which no override reaches — so they want the same treatment as the NY
import: suppress the stub, add the real record.

| current record | is really | evidence |
|---|---|---|
| `Ellsworth BJJ` | Acadia Brazilian Jiu-Jitsu | own site, live schedule, 4 named instructors, © 2026 |
| `Saco BJJ` | Evolution Athletix | own BJJ program page, weekly Gi times, 2026 media |
| `Lewiston-Auburn BJJ` | Central Maine Brazilian Jiu Jitsu (cmbjj.com) | ⚠️ address from search snippet, site is JS-rendered |
| `Portland BJJ Maine` | The Academy, 18 Ashmont St (theacademymaine.com) | |
| `Augusta BJJ Maine` | probably Black Bear BJJ & Fitness, 126 Western Ave | |
| `Brunswick BJJ Maine` | probably First Class MMA, 14 Maine St Unit 102B | ⚠️ address is site metadata, not a rendered block |
| `Seacoast Brazilian Jiu-Jitsu` /Biddeford | probably Team Moreira BJJ Biddeford, 408 Alfred St | |
| `Maine BJJ` /Bangor | possibly Gracie Barra Bangor, 424 Odlin Rd | ⚠️ **aggregator only** — no live first-party site found |

---

## Explicitly NOT settled

- **GracieFighter Presque Isle** — cannot confirm it currently operates. One 2022 news piece; no
  site of its own; parent Caribou site silent on it.
- **Gracie Barra Bangor** — no live first-party site. graciebarra.com's find-a-school is
  JS-rendered and returned nothing to a plain fetch. The address is aggregator-derived.
- **Maine Jiu Jitsu Academy, Boothbay** and its claimed Manchester/Augusta and Brunswick
  affiliates — `mainejiujitsu.com` returns an empty body; `blakebjj.com` is JS-only with no
  published address. Existence likely, operation and addresses unsettled.
- **Southern Maine BJJ (South Portland)** and **The Outlet (Dexter)** — Facebook-only, omitted
  rather than padded.
- **Titan Athletics (Brewer)** — domain now parked/for-sale, no live gym site.
- The 11 existing records' stored URLs were not audited beyond the 5 suspects, so the "is really"
  mappings above are inference from town + discipline, **not confirmed record matches**.
- 10th Planet's own affiliate list shows **zero** Maine schools — worth knowing before chasing it.

---

## What this implies for the other 30 regions

Maine had 11 listings and ~20 real schools, i.e. the directory was carrying roughly **half** the
schools that exist, and none of the links worked. The 31 stub-bearing regions hold **513 records
between them**. If Maine's ratio is anywhere near typical, there are several hundred unlisted
schools across them — which is a far larger prize than the link cleanup that started this.

**Bound to its method / sample size:** n=1 region. Maine is small, rural and was 100% flagged;
it may be the worst case rather than the median. Ontario (40 records) and Arkansas (35) will test
that. Do not extrapolate the ratio until at least one larger region has been done.
