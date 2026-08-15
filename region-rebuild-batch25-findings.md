# Batch 25 — the bucket sampling. The remaining work just got much smaller.

Session of 13 Aug 2026. Built as theme **CCC** (`154950467756`), **staged and awaiting publish**.
Overrides only. **Record counts cannot have moved.**

**Publish CCC `154950467756`.** BBB `154949288108` becomes the rollback.

---

## The finding: rot is concentrated, not uniform

Batch 24 flagged that all 840 links screened so far came from a single bucket — `http://`-only
stored URLs — and that projecting from it was unsafe. This batch tested that by taking a **random
sample of 120 from each of the two unmeasured buckets.**

| bucket | pool | sampled | actively bad | bad rate | hijacked | hijack rate |
|---|---|---|---|---|---|---|
| `http://`-only | 1,455 | 840 | 56 | **6.7%** | 16 | 1.9% |
| scheme-less | 491 | 120 | 6 | **5.0%** | 4 | **3.3%** |
| `https://` | 2,294 | 120 | 2 | **1.7%** | 0 | **0.0%** |

**The `https://` bucket — the largest, at 2,294 records — is nearly clean.** Zero hijacks, zero
parked, zero dead in a random 120. Its only two defects were wrong-business links.

### What that changes

| | previous flat estimate | bucket-weighted estimate |
|---|---|---|
| actively bad across 4,240 | ~284 | **~160** |
| hijacked | ~80 | **~44** |

**And it reprioritises the remaining work sharply.** 3,400 links are unscreened, but the harm is
not evenly spread:

- **615 remaining `http://`-only** → ~41 bad expected
- **371 remaining scheme-less** → ~19 bad expected
- **2,174 remaining `https://`** → ~37 bad expected, and **essentially no hijacks**

**Screening the 986 remaining non-`https` links captures roughly 60% of the remaining harm for
29% of the effort** — and all of the remaining hijack risk. That is one more session, not three.

The `https://` tail is still worth doing eventually, but it is a low-yield sweep for wrong-business
and wrong-location links, not an urgent safety problem.

⚠️ **One caution on the scheme-less figure:** its hijack rate (3.3%) is the *highest* of the three
and rests on a single sample of 120 with 4 hits. The confidence interval is wide. It is enough to
justify prioritising that bucket; it is not enough to claim scheme-less is worse than `http://`.

---

## Four more hijacks — twenty-eight total

| record | what its domain now serves |
|---|---|
| `Peak MMA & Fitness` | **HUBET** — a Vietnamese casino / sportsbook |
| `Defense Combatives DEFCOM` | an **Aviator crash-game** casino affiliate (1Win / Mostbet / 4rabet) |
| `College Park MMA` | `syairtogel.info` — Indonesian togel gambling |
| `Crazy Monkey USA` | a Chinese-language **九游** gaming/gambling portal |

All four came from the scheme-less sample. **None came from `https://`.**

## Four wrong-business links
A bare **Mindbody sign-in page** · a **Pilates and massage studio** · a real martial arts academy
**250 miles** from the listed city · and **Goshin & Kudo Academy in Barry, Wales, UK** standing in
for a school in Shelby Township, Michigan.

---

## What was written

| file | was | now | change |
|---|---|---|---|
| `snippets/tjjm-gym-websites-3.liquid` | 14,242 B | **14,462 B** | 8 blanking entries added |

Files 1 and 2 unchanged. MD5-verified against theme CCC by the caller:
`bf38e01f663a8debc0c32937e218821b`. **832 override entries, zero duplicate names.**

### Structural guarantee
Every count-bearing file in CCC is byte-identical to BBB — legacy blob `1ee054…`, removed-index
`98ee61…`, section `633ec8…`, region-index `8f4faa…`, websites-1 `16a715…`, websites-2 `08c171…`.
**5,215 published / 61 regions preserved by construction.**

---

## Running total of the harmful-link programme

| batch | audited / screened | links removed or fixed |
|---|---|---|
| 19–20 (the 6 Aug flagged set) | 184 | 95 |
| 21–24 (screen groups 1–7) | 720 | 56 |
| 25 (bucket samples A + B) | 240 | 8 |
| **total** | **1,144** | **159** |

Plus **190 links restored** in batches 9–18. **349 link changes in one day.**

---

## Next session — a concrete, short plan

1. **Finish the two dirty buckets first: 986 links** (615 `http://`-only + 371 scheme-less), about
   8 agent groups. Expect ~60 bad and essentially all the remaining hijacks. **One session.**
2. **Then the `https://` tail** — 2,174 links, low yield, no urgency. Can be spread out or sampled
   further rather than swept exhaustively.
3. **~110 EMPTY rows** across all batches need a browser session.
4. **The identity pass** — wrong-location and wrong-school links — is the final tier. Note that
   *every* defect found in the clean `https://` bucket was of this type, which suggests the
   identity pass, not the harm screen, is what the `https://` population actually needs.
