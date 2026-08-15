# Batch 24 — hijack screen, groups 6–7.

Session of 13 Aug 2026. Built as theme **BBB** (`154949288108`), **staged and awaiting publish**.
Overrides only. **Record counts cannot have moved.**

**Publish BBB `154949288108`.** AAA `154948108460` becomes the rollback.

---

## Cumulative screen — 840 of 4,240 unread links

| verdict | n | share |
|---|---|---|
| OK — a martial arts site | 688 | 81.9% |
| EMPTY — JS-rendered, needs a browser | 92 | 11.0% |
| **PARKED** | **28** | **3.3%** |
| **HIJACK** | **16** | **1.9%** |
| DEAD | 6 | 0.7% |
| **WRONG_BUSINESS** | **6** | **0.7%** |
| UNSURE | 4 | 0.5% |

**56 blanked — 6.7% actively bad.** **11 blanked in this batch.**

### ⚠️ A correction to the previous batch's inference
Batch 23 suggested the hijack rate was falling because the screen was "moving out of the `http://`
bucket into scheme-less URLs." **That was wrong.** All 840 links screened so far are still in the
`http://`-only bucket — it holds 1,455 records and we have not reached the end of it.

The per-group hijack counts (3, 3, 4, 2, 1, 0, 3) are **within-bucket variance, not a trend.** The
scheme-less and `https://` buckets remain entirely unmeasured, so no claim can yet be made about
whether rot correlates with scheme. Worth stating plainly because it is exactly the kind of
one-sample generalisation `RULES-tjjm.md` §8 warns about, and I made it.

### Projection, unchanged in substance
Applying 6.7% to all 4,240 unread links: **~284 actively bad, ~80 hijacked.** Treat as an estimate
for the `http://` population only until the other buckets are sampled.

---

## Three more hijacks — twenty-four total

| record | what its domain now serves |
|---|---|
| `Hahn MMA` | a Chinese **Kaiyun (开元)** gambling-branded page fronting a rigging-equipment site |
| `Cornerstone BJJ` | **LOGOTOTO** — Indonesian slots/togel gambling |
| `ECF Martial Arts / BTT Charlotte` | **SportHiatus**, a generic sports/nutrition content farm |

## Seven parked
GoDaddy for-sale ×3 (one at $3,799), HugeDomains, ExpiredDomains.com at $195, and two "Coming Soon"
placeholders.

## Group 6 was clean
Zero hijacks, zero wrong-business, only 3 bad in 120. **It also produced a useful negative:** several
redirects landed on legitimately **rebranded or merged schools at the same address** — still martial
arts, correctly marked OK. That instruction was added to group 7's prompt to prevent over-flagging,
and is worth keeping in future prompts.

---

## What was written

| file | was | now | change |
|---|---|---|---|
| `snippets/tjjm-gym-websites-3.liquid` | 13,887 B | **14,242 B** | 11 blanking entries added |

Files 1 and 2 unchanged. MD5-verified against theme BBB by the caller:
`a2c40fa732f412b44a7e3846e4b1869d`. **824 override entries, zero duplicate names.**

### Structural guarantee
Every count-bearing file in BBB is byte-identical to AAA — legacy blob `1ee054…`, removed-index
`98ee61…`, section `633ec8…`, region-index `8f4faa…`, websites-1 `16a715…`, websites-2 `08c171…`.
**5,215 published / 61 regions preserved by construction.**

---

## Running total of the harmful-link programme

| batch | audited / screened | links removed or fixed |
|---|---|---|
| 19–20 (the 6 Aug flagged set) | 184 | 95 |
| 21 (groups 1–2) | 240 | 17 |
| 22 (groups 3–4) | 240 | 16 |
| 23 (group 5) | 120 | 12 |
| 24 (groups 6–7) | 240 | 11 |
| **total** | **1,024** | **151** |

Plus **190 links restored** in batches 9–18. **341 link changes in one day.**

---

## Next

1. **3,400 unread links remain.** Worklist 8 is pre-built; beyond that, regenerate from
   `scratch/hijack-screen/all-targets.tsv`, which holds all 4,240 ranked by rot risk.
   **Sample the scheme-less and `https://` buckets early next session** rather than working
   straight through — that tests whether the 6.7% rate generalises or is specific to `http://`.
2. **92 EMPTY rows** — the browser queue now holds roughly 110 across all batches. Large enough to
   deserve its own session.
3. **The identity pass** — wrong-location and wrong-school links a content screen passes cleanly —
   remains the final tier.
