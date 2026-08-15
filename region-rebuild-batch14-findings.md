# Batch 14 — browser pass over the accumulated queue. Best yield of the programme.

Session of 13 Aug 2026. Built as theme **RR** (`154918781100`), **staged and awaiting publish**.
Overrides only. **Record counts cannot have moved.**

---

## Result

**35 targets · 24 confirmed · 4 dropped on the BJJ test · 20 published.**

| verdict | n |
|---|---|
| CONFIRMED | 24 (69%) |
| DEAD | 7 |
| UNRESOLVED | 4 |

**One recovery per 1.75 attempts — by far the best rate of the programme** (b9 2.8 · b10 2.6 ·
b11 2.75 · b12 3.1 · b13 3.2). **Blank-rendering published records: 693 → 673.**

**15 of the 20 published links are Facebook or Instagram pages.** That is the entire justification
for the browser phase: `web_fetch` cannot render those at all, so these records were not difficult,
they were *invisible*. Combined with batch 11, the browser pass has now produced **36 links from 79
targets (46%)** against **~34% for the fetch-based passes** — on records the fetch passes had
already given up on.

### Dropped before recheck — the BJJ test
Four rows the original agent **self-flagged honestly**: confirmed on address or phone, but no live
page names a BJJ or grappling class. One (`F-5 Grappling`) is explicitly wrestling. Removed on the
same standard as `Paladin MMA` (b9), `Gladiator Sports` (b11) and `Amorosi MMA` (b13).

### The independent recheck — no failures, two better URLs
**15 clean PASS, 5 PASS_WITH_CAVEAT, zero FAIL.** It also found two cases where a **real website
beats the proposed social page**, which is a straight upgrade:

- `Kingsnake Jiu-Jitsu` → `kingsnakebjj.com` instead of a Facebook page
- `Jaguar BJJ` → `jaguarbjj.com` instead of a **3-post Instagram** — and the live site carries the
  matching address (518 Old Post Rd, Edison) and phone

**Lesson: when a social page is the candidate, check for a real site anyway.** Two of twenty had
one, and the browser agent had settled for the social page.

---

## Findings

**⚠️ Two schools are closed, and the corpus still lists them.**
- **`Mega Church Jiu Jitsu`** — its pinned Facebook post reads "CLOSED.", and the owner replied
  about a year ago "On to the next chapter."
- **`Empire Jiu-Jitsu Durant`** — domain dead, **Facebook page and Instagram both removed**.

Both are **suppression candidates**, not repoints. Neither is detectable without rendering a social
page — no DNS or HTTP check would have found them.

**Six more parked/expired landers on exact-name domains**, invisible to any check short of
rendering: `guetho.com` (Hostinger), `usfamilymartialarts.com` (GoDaddy), `gatorpitbjj.com`
(expired-domain ad lander), `clinchmartialarts.com` (`/lander`), `jbmjiujitsu.com` (Squarespace
"Website Expired"), `kudosjiujitsu.com` (Google 404). Running total: **fifteen** exact-name domains
that looked like JS-rendered school sites and were landers.

**Two more live-site rebrands, both confirmed by owner and phone:**
- `Fight to Win Lafayette` → **Royce Gracie Academy of Broussard**, same Facebook page,
  817 Albertson Pkwy
- `Rolles Gracie Long Branch` → **RR Martial Arts**, 167 Locust Ave, same phone, same owner
  Rodolfo Rocha

**Two same-name candidates correctly rejected:** `empirebjjok.com` is Empire Jiu-Jitsu of **Moore
OK** (Dustin Brooks), with no Durant location; `criterionbjj.com` is Criterion Jiu-Jitsu of
**Louisville KY**.

**All three pre-warned traps held.** The agent was told `lucasmartialartsacademy.com` is a Bedford
**Indiana** school, `ryanbjj.com` is Roseburg **Oregon**, and `rockymountainjiujitsu.com` redirects
to Six Blades Littleton. It avoided all three and found correct social pages instead — and the
verifier independently confirmed the replacements. **Carrying known-wrong candidates forward into
the next batch's prompt works.**

---

## Caveats on published links

- **`Louisiana Judo`** and **`Tulsa Judo`** (b13) — judo is grappling and the classes are real, but
  neither names a BJJ class. Kept on that basis. **If the directory's bar is BJJ specifically, both
  are record-level suppression candidates** — that is a corpus decision, not a link decision.
- **`Criterion Jiu Jitsu`** — the address is on the page, but the Facebook page has **15 followers**
  and `criterionjiujitsu.com` is dead. Thin.
- **`Ground Zero Roaring Fork`** — relocated to 413 9th St, **Glenwood Springs**; the record says
  New Castle. Same operator, within Garfield County.
- **`Kingsnake Jiu-Jitsu`** — appointment-only private lessons rather than a public class schedule.

---

## What was written

| file | was | now | change |
|---|---|---|---|
| `snippets/tjjm-gym-websites-2.liquid` | 22,251 B | **21,899 B** | 11 entries **moved out** |
| `snippets/tjjm-gym-websites-3.liquid` | 5,439 B | **6,814 B** | 20 entries added |

MD5-verified against theme RR by the caller: `eee253e6630fe70d4638ccda6f232daa` /
`eb513bb80a0ca910302ea11953c0a5e6`. Override entries **664**, zero duplicate names, 453 blank.

**The move-not-edit rule keeps working: websites-2 headroom is now 2,677 B, up from 2,029 B two
batches ago**, while 35 links were added across those batches. File 3 is at 6,814 B with ~18 KB
free.

### Structural guarantee
Every count-bearing file in RR is byte-identical to QQ — legacy blob `1ee054…`, removed-index
`c6069b…`, section `633ec8…`, region-index `3df967…`, addresses `031ea9…`, websites-1 `065db8…`.
**5,219 published / 61 regions preserved by construction.**

---

## TO PUBLISH

**Publish RR `154918781100`.** QQ `154915864748` becomes the rollback.
No `metafieldsSet` needed — counts unchanged.

---

## Programme total after six batches

| batch | targets | published |
|---|---|---|
| 9 FL + cross-region debts | 88 | 31 |
| 10 CA, TX | 120 | 47 |
| 11 browser | 44 | 16 |
| 12 NJ OK CO LA | 97 | 31 |
| 13 carry-forward | 48 | 15 |
| 14 browser | 35 | 20 |
| **total** | **432** | **160** |

**160 links restored. Blank records 833 → 673, a 19% reduction.** Overall yield 1 per 2.7.

## Owed

1. **Suppression candidates, not repoints:** `Mega Church Jiu Jitsu` (closed), `Empire Jiu-Jitsu
   Durant` (closed), `14ers Jiu Jitsu` (dissolved), `AJW` (karate only), `Gladiator Sports Fitness
   MMA` (no BJJ). A single corpus batch could clear all five.
2. **4 UNRESOLVED** from this batch, incl. `Ground Zero Combat Sports` — two sibling Leesville pages
   that could not be proven to be one entity.
3. Remaining blank pool: FL 53 · TX 48 · CA 41 · GA 32 · IL 30 · NV 28 · OH 28 · PA 27 · WA 26 ·
   MO 25 · MA 22 · AZ 20 · VA 20.
4. **When a social page is the only candidate, still check for a real site** — two of twenty had one.
