# Batch 15 — suppress five defunct / not-BJJ records.

Session of 13 Aug 2026. Built as theme **SS** (`154919305388`), **staged and awaiting publish**.

## ⚠️ THIS BATCH CHANGES RECORD COUNTS

Unlike batches 9–14, this is **not** an overrides-only batch. The removed-index changed, so the
structural "counts cannot have moved" guarantee **does not apply** and a real verification is
required. Two things are owed after publish:

1. **`metafieldsSet` for CO, FL, NJ and OK** — their titles and descriptions will be one or two
   records stale the moment SS goes live. Exact new values below.
2. **A live count check** confirming the region nav sums to **5,214**.

---

## What was suppressed, and why

| region | record | city | reason |
|---|---|---|---|
| OK | `Mega Church Jiu Jitsu` | Muskogee | **CLOSED** — pinned Facebook post reads "CLOSED."; owner replied ~1 yr ago "On to the next chapter." |
| OK | `Empire Jiu-Jitsu Durant` | Durant | **CLOSED** — domain dead, Facebook page *and* Instagram both removed |
| CO | `14ers Jiu Jitsu` | Salida | **DISSOLVED** — entity wound up; former members founded Veritas Training Center as a new business. Not a rebrand |
| NJ | `AJW Martial Arts Academy & Fitness Center` | City Of Orange | **NOT BJJ** — live site verified (address + phone), but a Shito Ryu karate school with zero grappling named |
| FL | `Gladiator Sports Fitness MMA` | Hialeah | **NOT BJJ** — address and phone match, classes are Judo / kickboxing / MMA / Muay Thai, no BJJ |

**All five were discovered as a by-product of the repointing programme**, not by any scheduled audit.
Three of them — the two closures and the karate school — are invisible to DNS and HTTP checks: the
closures were only detectable by *rendering a social page*, and the karate school has a perfectly
healthy website. This is more evidence that link verification is doing the corpus's real defect
detection.

⚠️ **`AJW` is in NEW JERSEY**, not Oklahoma as the running notes implied. Checked before writing.

---

## Gate

- **C4** — every suppression name matches **exactly one published record** in its own region. All
  five verified; none matched zero or multiple.
- **C4 (duplicate guard)** — none of the five was already present in its removed-index row.
- **C5** — no name contains `|` or `~`.
- **C6** — none is both suppressed and added in this batch.
- **C7b** — none is a Newfoundland record, so no NE/NL row subtlety applies. Suppression rows were
  keyed on the **source state code**, not the display region, which is the correct behaviour.
- **Post-build recomputation** from the amended removed-index reproduces **5,214 published / 61
  regions / 697 suppressed records from 695 names** — the two-record gap being the declared C4
  multi-matches (`MD | Southern Maryland Martial Arts & Fitness`, `VA | Capital MMA & Elite Fitness`),
  unchanged.

## Housekeeping folded in

Two of the five carried a **blanking override** in `tjjm-gym-websites-2` that becomes dead weight
once the record stops rendering. Both removed — `Empire Jiu-Jitsu Durant` and `AJW Martial Arts
Academy & Fitness Center`. The build refuses to drop an override whose value is *not* blank, so a
real URL can never be silently discarded this way.

---

## What was written

| file | was | now | change |
|---|---|---|---|
| `snippets/tjjm-removed-index.liquid` | 13,749 B | **13,882 B** | +5 suppression names across 4 rows |
| `snippets/tjjm-gym-websites-2.liquid` | 21,899 B | **21,827 B** | 2 dead blanking entries removed |

MD5-verified against theme SS by the caller, not trusted from the write agent:
`07242e908d7b4b1a77a43581dae76244` / `88d63b7878a7f46da8140c8c3cc01e23`.
Unchanged and confirmed identical to RR: the legacy blob, all data files, the section,
region-index, addresses, websites-1 and websites-3.

`tjjm-gym-websites-2` is now **21,827 B — 2,749 B of headroom**, its best since batch 10.

---

## TO PUBLISH — then two required follow-ups

**1. Publish SS `154919305388`.** RR `154918781100` becomes the rollback.

**2. Run `metafieldsSet` on these four pages.** Rollback strings are the current live values.

| region | page id | title count | description count |
|---|---|---|---|
| CO | `gid://shopify/Page/121182748844` | 156 → **155** | 156 → **155** |
| FL | `gid://shopify/Page/121182847148` | 328 → **327** | 328 → **327** |
| NJ | `gid://shopify/Page/121183600812` | 210 → **209** | 210 → **209** |
| OK | `gid://shopify/Page/121183895724` | 98 → **96** | 98 → **96** |

⚠️ **NJ's description also states "across 137 towns" and OK's "across 45 cities".** Check whether
suppressing these records emptied a city before changing only the number — City Of Orange NJ and
Muskogee/Durant OK each need a city-count re-derivation. Muskogee in particular now loses one of
its records.

**3. Verify live cookie-free** that the region nav sums to **5,214**, and that CO/FL/NJ/OK read
155 / 327 / 209 / 96.

---

## Owed

1. The **4 UNRESOLVED** rows from batch 14, incl. `Ground Zero Combat Sports` (two sibling
   Leesville pages that could not be proven to be one entity).
2. Remaining blank pool: FL 52 · TX 48 · CA 41 · GA 32 · IL 30 · NV 28 · OH 28 · PA 27 · WA 26 ·
   MO 25 · MA 22 · AZ 20 · VA 20.
3. **`Louisiana Judo` and `Tulsa Judo`** — both published with links, both judo-only with no BJJ
   class. Kept because judo is grappling; **if the directory's bar is BJJ specifically they are the
   next two suppression candidates.** That is a policy call, not a research one.
