# Batch 19 — the link audit. Removing bad links rather than filling blanks.

Session of 13 Aug 2026. Built as theme **WW** (`154932805804`), **staged and awaiting publish**.
Overrides only. **Record counts cannot have moved.**

**This is the first batch aimed at links that were already live and wrong**, rather than at records
with no link. It is the shape of the work required to reach the owner's standard: *a good accurate
link, or no link at all.*

---

## Result

**138 of 184 known-suspect live links checked. 72 changed — 44 blanked, 28 replaced.**

| verdict | n | share |
|---|---|---|
| KEEP | 65 | 47% |
| DEAD | 33 | 24% |
| NEEDS_BROWSER | 17 | 12% |
| PARKED | 9 | 7% |
| **WRONG_ENTITY** | **8** | 6% |
| NOT_GRAPPLING | 4 | 3% |
| **HIJACKED** | **1** | 1% |
| UNRESOLVED | 1 | 1% |

**A 53% defect rate** among links the 6 Aug screen had flagged — close to its own 61% estimate.

46 targets remain, pre-split in `scratch/audit-recheck/targets-{7,8}.tsv`.

---

## ⚠️ NINE HIJACKS NOW. One was live on the site today.

**`The Dojo LLC` (Fort Collins CO)** — `thedojofc.com` now serves a **Chinese sports-gambling SEO
farm** (开云·体育 / Kaiyun Sports), fronted as a Guangzhou IT company, with a footer link farm to a
dozen other gambling brands. No martial-arts content at all. **Blanked.**

That brings the running total to nine hijacked former school domains: a Norwegian casino, two
Chinese gambling sites, a Chinese streaming/piracy site, an Indonesian gambling SEO farm, an
ad-redirect farm, a motorsports content farm, a credit-repair site, and a WordPress farm carrying
paid links to an escort directory.

**Every one resolves, returns 200, and still shows the school's old title in search results.** No
reachability screen can see them. Only reading the landing page can.

## Eight wrong-entity links, all live to users until now

| record | pointed at |
|---|---|
| `Bridge City Combat` (AZ) | **a firearms retailer / gunsmith** |
| `Ronin Jiu-Jitsu North Las Vegas` (NV) | a school in **Attleboro, Massachusetts** |
| `Michigan Sports Camps` (MI) | a fitness business in **Middleville**, ~65 mi away |
| `Gracie Gym Richardson` (TX) | **a gym in Windham, Maine** — see the scheme note below |
| `Guerrero BJJ & MMA` (NJ) | a different academy in West Orange |
| `Team Carvalho Treasure Coast` (FL) | the Dunnellon / Paterson academy, not Fort Pierce |
| `Aloisio Silva BJJ` (TX) | the Silva association HQ, not the Arlington academy |
| `Valente Brothers Pembroke Pines` (FL) | the North Miami headquarters site |

**⚠️ New trap — the scheme changes the destination.** `Gracie Gym Richardson`'s stored `http://`
URL redirects to a **Maine** gym, while `https://` on the *same host* serves the correct Texas
school. **Always try both schemes before condemning a link.**

---

## ⚠️ The gate caught a silent-failure class — curly apostrophes

The build refused to write because `Eric Nolan's Xtreme Training Center` matched **zero** published
records. The corpus spells it `Eric Nolan’s` with a **curly apostrophe (U+2019)**; the 6 Aug audit
file used a straight `'` (U+0027).

**Overrides match on exact name.** Had that been written as-is, the override would have applied to
nothing, the hijacked-or-dead link would have stayed live, and *nothing would have reported a
failure* — the write would have succeeded and the count of entries would have looked right.

The build now resolves every incoming name against the corpus by a normalised form (curly/straight
quotes, en/em dashes) and **fails loudly if it cannot land on exactly one published record.** Any
future batch that joins on names from an external file needs this. It should go in `RULES-tjjm.md`
alongside the "a mismatch just misses silently" warning already in the addresses-file header.

---

## Other patterns

**Host normalisation was the most common fix** — apex renders while `www` serves an empty body, or
the reverse. Roughly a third of the 28 replacements were this, not a genuine domain change.

**Four schools failed the grappling test outright**, including a self-described "MMA studio" whose
class pages are headed *STRIKING* and list only kickboxing, boxing, muay thai and sanshou, and one
listing only Jeet Kune Do, Filipino weapons arts and Silat.

**Two live 404s at redirect targets** where the owner had merely relocated — repointed to the
working homepage rather than blanked.

**Agents flagged their own weak evidence honestly** throughout: several noted that an address came
from a third-party listing rather than the school's own page, and left `source_url` empty rather
than cite something unread. One declined to condemn a domain on suspicious hosting alone — a
Chinese IP block that turned out to serve the genuine school.

---

## What was written

| file | was | now | change |
|---|---|---|---|
| `snippets/tjjm-gym-websites-3.liquid` | 8,687 B | **11,593 B** | 72 entries added |

Files 1 and 2 unchanged. MD5-verified against theme WW by the caller:
`d590ef8910cde1cde730b2a602af1a7a`.
**745 override entries, zero duplicate names, 474 blank.**

### Structural guarantee
Every count-bearing file in WW is byte-identical to VV — legacy blob `1ee054…`, removed-index
`98ee61…`, section `633ec8…`, region-index `8f4faa…`, addresses `031ea9…`, websites-1 `16a715…`,
websites-2 `08c171…`. **5,215 published / 61 regions preserved by construction.**

---

## TO PUBLISH

**Publish WW `154932805804`.** VV `154923991212` becomes the rollback.
No `metafieldsSet` needed — counts unchanged. Blanking a link does not remove the record.

---

## Owed

1. **46 remaining targets** — `scratch/audit-recheck/targets-{7,8}.tsv`.
2. **17 NEEDS_BROWSER** rows from this batch, mostly Cloudflare-fronted or JS-rendered.
3. Two rows needing an owner decision, both flagged in `batches/link-audit-fixes-b19.tsv`:
   `Team Reno` (the URL is Momentum Martial Arts; the name matches a different school's site) and
   `D'Arce BJJ` (the replacement domain states **Shirley**, not Patchogue).
4. **Tier B proper — ~4,151 links that passed the 6 Aug screen and have never been read.** See
   `PLAN-path-to-every-link-correct.md`. Nine hijacks have surfaced from incidental checking alone;
   a mechanical hijack-signature screen across that population is the next big win.
