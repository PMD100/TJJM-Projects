# Batch 13 — carry-forward targets, and the fix for the websites-2 ceiling.

Session of 13 Aug 2026. Built as theme **QQ** (`154915864748`), **staged and awaiting publish**.
Overrides only. **Record counts cannot have moved.**

---

## Result

**48 targets (the batch-12 carry-forward) · 17 confirmed · 2 rejected on recheck · 15 published.**

| verdict | n |
|---|---|
| DEAD | 19 |
| CONFIRMED | 17 |
| NEEDS_BROWSER | 10 |
| NOT_BJJ | 1 |
| UNRESOLVED | 1 |

**One recovery per 3.2 attempts.** **Blank-rendering published records: 708 → 693.**

**The 145-target batch-12 tranche is now fully covered** — nothing from NJ/OK/CO/LA is outstanding
except the browser queue.

### Dropped on recheck
- **`Amorosi MMA`** — FAIL_BODY. Phone 973.533.9112 confirms the entity, but the site names only a
  PreK and an Adults program — no BJJ, jiu jitsu or grappling anywhere, and it never states
  Livingston.
- **`Tra Jiu Jitsu`** (claimed rename to "The Relentless Art") — the page never names Thiago Rela
  and carries no address. Continuity rested on the domain plus external listings. **Identity not
  pinned by address or phone → dropped**, consistent with the standard applied since batch 9.

---

## 🔧 THE FILE-2 CEILING IS SOLVED — move, don't edit

Batch 12 ended with `tjjm-gym-websites-2` at **22,547 B against a ~24,576 B ceiling — 2,029 B left**,
and recommended creating a `tjjm-gym-websites-4` plus a section change to add it to the render chain.

**That is not necessary.** There is a cheaper fix with no section edit:

> When a record already has a *blanking* entry in file 2 and you now have a real URL for it,
> **delete the entry from file 2 and write the URL into file 3** — rather than editing file 2
> in place.

The section renders file 1 → 2 → 3, later wins, so behaviour is identical. But the arithmetic
reverses: an in-place edit *grows* file 2 by the length of the URL, whereas a move *shrinks* it by
the whole line.

Measured this batch — 10 entries moved out:

| file | before | after | change |
|---|---|---|---|
| `tjjm-gym-websites-2.liquid` | 22,547 B | **22,251 B** | **−296** |
| `tjjm-gym-websites-3.liquid` | 4,433 B | **5,439 B** | +1,006 |

**websites-2 headroom went from 2,029 B to 2,325 B — it grew.** Name uniqueness is preserved (655
entries, zero duplicates), and no `tjjm-gym-websites-4` is needed for the foreseeable future. File 3
is at 5,439 B with ~19 KB of room.

**Adopt this as the standing rule for every future repointing batch.** `build_b13.py` logic is
inline in this session's history; the earlier `build_b9.py`–`build_b12.py` edit-in-place pattern
should be considered superseded.

---

## New traps

**⚠️ Hijacks are now actively hostile, not merely stale.** `pmatc.com` resolves and 302s to
`sireimplement.com/h5e8vxwdr0`, an ad/redirect farm. That is the third hijack class after the
Chinese streaming site and the Indonesian gambling SEO farm. **Follow redirects and read where you
actually land** — the landing page, not the requested URL, is what would be published.

**⚠️ Unclaimed booking stubs.** A WellnessLiving (or similar) page whose rows read
"Service Name" / "Instructor Name" is a placeholder, not a school site. Two hit this batch —
`Rising Crane` and `Yu'ki MMA`. It looks like a real booking system until you read the rows.

**Stored-URL death rate remains ~100%** — 12/12, 15/15 and 10/11 across the three groups, the sole
survivor being the hijacked `pmatc.com`. Across roughly 450 stored URLs tested in this corpus, the
historic blanking decisions have been vindicated essentially without exception.

**Three more same-name-different-school traps**, all of which directories actively cite as correct:
`combatathletic.com` = Bermuda Run **NC** · `lionheartbjj.com` = Brighton **CO** ·
`ryanbjj.com` = Roseburg **OR** (Ryan Cunningham, not Tulsa's Joseph Todd Ryan).
`martialartsnorman.com` is a different Norman OK school than the record.

**Two rebrands resolved only by cross-checking a named person** — Carlson Gracie Castle Rock →
The Rock Jiu Jitsu Team (owner Jared Leblanc, same 488 Crystal Valley Pkwy) and Low Summit →
Rebellion Self Defense and GJJ (both phones match, relocated Denver → Westminster). Neither was
resolvable from names or addresses alone. **Naming the instructor is the strongest continuity
evidence available.**

**Lapsed affiliations are a distinct class.** Atos HQ's live directory has **zero** Colorado
affiliates and Rolles Gracie's locations page no longer lists West Long Branch. Successors exist at
both addresses but neither succession could be verified from a primary page, so neither was
repointed. Records whose *name* encodes a lapsed affiliation are a future cleanup class of their own.

---

## Caveats on published links

- **`Tulsa Judo`** — judo is grappling and the named classes are real, but there is **no separate BJJ
  class**. Kept on that basis; flag if the directory's bar is BJJ specifically.
- **`GJ MMA`** — published via a Square booking page because its own domain `gjmma.com` is NXDOMAIN.
  Address and phone verify; grappling is named only inside a class blurb.
- **`Champion Factory Amite`** — the subpage is genuine and location-specific (102 Central Ave, full
  BJJ schedule) but branded **Gracie United**, not Gracie Barra as the record implies.
- **`Cohesion Training Academy`** — the location page gives **Tulsa**, not Broken Arrow. Adjacent
  metro, acceptable, but the record's city looks stale.

---

## What was written

| file | was | now | change |
|---|---|---|---|
| `snippets/tjjm-gym-websites-2.liquid` | 22,547 B | **22,251 B** | 10 entries **removed** (moved to file 3) |
| `snippets/tjjm-gym-websites-3.liquid` | 4,433 B | **5,439 B** | 15 entries added (10 moved + 5 new) |

MD5-verified against theme QQ by the caller, not trusted from the write agent:
`9ef9fa998acae471714b198705c216e2` / `de4875896d1c7878fc05f23f36532fed`.

Override entries **655** across three files, **zero duplicate names**, 464 blank.

### Structural guarantee that counts did not move
Every count-bearing file in QQ is byte-identical to PP — legacy blob `1ee054…`,
`tjjm-removed-index` `c6069b…`, `sections/tjjm-state-directory` `633ec8…`, `tjjm-region-index`
`3df967…`, `tjjm-gym-addresses` `031ea9…`, `tjjm-gym-websites` file 1 `065db8…`. Only the two
override files differ. **5,219 published / 61 regions preserved by construction.**

---

## TO PUBLISH

**Publish QQ `154915864748`.** PP `154911932588` becomes the rollback.
No `metafieldsSet` needed — counts unchanged.

---

## Cumulative progress of the repointing programme

| batch | targets | published | blank after |
|---|---|---|---|
| 9 (FL + debts) | 88 | 31 | 802 |
| 10 (CA, TX) | 120 of 150 | 47 | 755 |
| 11 (browser) | 44 | 16 | 739 |
| 12 (NJ OK CO LA) | 97 of 145 | 31 | 708 |
| 13 (carry-forward) | 48 | 15 | **693** |
| **total** | **397** | **140** | |

**140 links restored, blank records down from 833 to 693 — a 17% reduction.** Overall yield is one
recovery per 2.8 attempts, stable across five batches.

## Owed

1. **35 NEEDS_BROWSER rows** from batches 12–13 — add to the browser queue, which also still holds
   the 15 UNRESOLVED and 10 DEAD from batch 11.
2. `14ers Jiu Jitsu` (dissolved) and `AJW` (karate-only) — **suppression candidates, not repoints**.
3. Records whose names encode a **lapsed affiliation** — a new cleanup class.
4. Remaining blank pool by region: FL 53 · TX 48 · CA 41 · GA 32 · IL 30 · NV 28 · OH 28 · PA 27 ·
   WA 26 · MO 25 · MA 22.
