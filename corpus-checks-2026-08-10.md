# Corpus-wide checks, 10 Aug 2026

Run against theme **FF** (`154774995116`), 5,302 stored / 4,825 rendered. All local — no research,
no fetching except one live confirmation. These are the checks the previous brief listed under
"WHAT WAS NOT CHECKED", now cheap because the Phase 0 corpus dump exists.

**Reconstruction validated first:** FF stored = EE dump (5,202) + the 100 batch-3 adds = 5,302.
`5,302 − 477 region-scoped suppressions = 4,825` — exactly the published total. Missouri
independently checks out too (103 stored, 98 rendering, page says 98).

---

## 1. Cross-region diff — COMPLETE, first time on this project

**15 names appear in 2+ regions.** Nearly all are genuinely different schools with generic names
(`Evolution Jiu Jitsu`, `Impact Martial Arts`, `Core Combat Sports`, `Logic Jiu Jitsu`…).

That is not the interesting question. The interesting question is which of them carry a
**corpus-wide name-keyed override**, because those apply one school's URL or address to every record
sharing the name.

**Result: exactly one candidate, and it does not manifest.**

`Infinite Jiu-Jitsu` exists in Phoenix AZ and Rocklin CA, and carries an address override
(`4220 W Opportunity Way Ste 103` — the Phoenix address). Because `tjjm-gym-addresses` only fills a
**blank** `a`, it can only leak onto a record with no stored address. Confirmed live and cookie-free:
`Opportunity Way` appears **0 times** on the California page and 2 times on the Arizona page. The
Rocklin record stores its own address, so the override cannot reach it.

**No live override-collision defect exists in the corpus.** It is, however, a latent one: if the
Rocklin record's address were ever cleared, it would silently inherit a Phoenix street.

## 2. Savarese BJJ — RESOLVED, no NJ add is owed

The brief asks whether `Savarese BJJ` "(suppressed from NY as being in Lyndhurst NJ) already exists
under NJ — if not, a net-new NJ add is owed."

Both records exist and are listed:

- `Savarese BJJ Academy - Jersey City` — Jersey City, **NJ**
- `Savarese BJJ Academy` — Lynbrook, **NY**

**Nothing is owed.** Note the brief's "Lyndhurst NJ" appears to be a garbling of **Lynbrook NY**,
which is where the surviving NY record actually is. Lyndhurst NJ does exist in the corpus but holds
two unrelated schools (Anaconda BJJ & MMA, Subforce BJJ).

## 3. Missouri — likely owes 6 records, all unverified

The Kansas research correctly excluded nine Kansas City **Missouri** schools. Checked against MO's
98 rendering records:

| candidate | status |
|---|---|
| Gracie Humaita Kansas City | **already listed** (under city "Kansas City", researcher said North Kansas City — minor city-field discrepancy) |
| Sharkbait's MMA | **already listed** as `Sharkbait's MMA & Jiu Jitsu Academy`, Blue Springs. Researcher cited "Kansas City and Blue Springs" — a second site may be owed |
| 10th Planet KC / Lone Wolf MMA | `10th Planet Kansas City` is listed, but the researcher's address is **Platte City** — different location, possibly a second site or a move |
| Rilion Gracie Kansas City | no match — **owed** |
| Warriors Academy KC | no match — **owed** |
| Alive BJJ | no match — **owed** |
| Gracie Jiu-Jitsu Kansas City | no match — **owed** |
| Wildfire BJJ | no match — **owed** |
| Ignite Jiu Jitsu and MMA (Gladstone) | no match — **owed** |

**6 net-new, 3 needing adjudication.** All nine came from a researcher who was *not* verifying
Missouri — they are leads, not publishable. They need a Phase 2 body-verification pass first.

## 4. City/state contradiction scan — INCONCLUSIVE, needs a gazetteer

Two heuristics were tried and **neither is fit for purpose**. Recording this so the next run does
not repeat the attempt.

- **"City appears under 2+ states, one side a singleton"** → 78 candidates, overwhelmingly
  legitimate (Springfield, Aurora, Columbus, Hamilton all genuinely exist in several states).
- **A hand-built gazetteer of ~90 distinctive cities** → 48 flags, again dominated by real places:
  Vancouver WA, Portland ME, Salem MA, Richmond TX, Newark OH, Wilmington NC, Manhattan KS,
  Jackson WY are all correct as filed.

⚠️ **Both scans missed the one confirmed defect.** The first missed it because it required the
correct side to hold ≥3 records and NY-Poughkeepsie holds exactly one; the second because
Poughkeepsie was not in the hand-built list. A scan that misses the only case you already know about
is not a scan — **this is the same failure shape as the collision gate that reported "no collisions"
on a set that had two.** Seed any future version with `Precision MMA` and confirm it fires.

**The real fix is a proper place gazetteer** (US Census place file + Statistics Canada equivalent),
loaded once and checked exhaustively. Until then this class remains unscanned.

---

## Confirmed defects, not yet fixed

**1. `Precision MMA` is filed under the wrong state.**

```
"Precision MMA"                 Poughkeepsie   NJ    <-- wrong, Poughkeepsie is in New York
"Gracie Jiu-Jitsu Poughkeepsie" Poughkeepsie   NY    <-- correct, same city
```

In `snippets/tjjm-gyms-data.liquid` (the 113 KB legacy blob).

⚠️ **CORRECTED 12 Aug 2026 — this is NOT a live defect.** The record is **already suppressed** in the
NJ row of `tjjm-removed-index`, so it renders nowhere on the site. It is a latent *stored* defect
only. Two consequences:

- Fixing it does **not** move NJ 210 → 209 or NY 182 → 183, because the record is not currently
  counted in either. Any earlier plan to edit `tjjm-region-index` and the NJ/NY metafields was wrong
  and was reverted before publication.
- This is also why the gazetteer scan in §4 missed it: the scan ran over *live* records, and this
  one was filtered out as suppressed. The stated reason ("Poughkeepsie was not in the hand-built
  list") was itself wrong — Poughkeepsie **was** in the list.

Nobody has recovered *why* it was suppressed, so it was deliberately not resurrected. Resolving it
means answering that question first, not just flipping the state field.

**2. `NJ|JC Projects` is a dead suppression entry** in `tjjm-removed-index` — matches no record in
NJ or anywhere else. Suppresses nothing. Removing it is cosmetic and has zero render impact.

**3. Four data snippets are not valid JSON** — `tjjm-gyms-data-30`, `-31`, `-32`, `-34` have no
enclosing `[ ]` and no newlines, just concatenated `}{`. They render correctly and are only a
problem for a strict `JSON.parse` consumer. Low priority; rewriting four files carries more risk
than the defect does.

**Recommendation:** fold fixes 1 and 2 into the next batch's theme write rather than doing a
separate duplicate-verify-publish cycle for them. Fix 3 can wait indefinitely.
