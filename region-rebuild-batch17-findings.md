# Batch 17 — a defect I introduced, found on live verification.

Session of 13 Aug 2026. Built as theme **UU** (`154921402540`), **staged and awaiting publish**.

---

## ⚠️ WHAT WENT WRONG

**Batches 15 and 16 changed record counts but never updated
`snippets/tjjm-region-index.liquid`, which carries a HARDCODED count per region.**

That file feeds the "Find schools in another state or province" nav that appears at the bottom of
**every one of the 61 region pages**. After SS and TT published, the live nav still read:

| region | nav said | actual |
|---|---|---|
| Colorado | 156 | **155** |
| Oklahoma | 98 | **96** |
| New Jersey | 210 | **209** |

Florida was correct at 328 only by accident — batch 15 took it to 327 and batch 16 put it back.

**Every region page was displaying three wrong numbers**, on the live site, for as long as SS and
TT were published.

### How it was caught
A cookie-free fetch of a small region page after publishing TT. The page's *own* body count was
right — that is computed dynamically from the data — but the nav list at the foot of the page was
not. **Checking a page's own count would never have found this**; the defect only shows in the nav,
which is data from a different file.

### Why I missed it
Every batch from 9 to 14 was overrides-only, so I leaned on the structural argument: *no
count-bearing file changed, therefore counts are preserved.* When batch 15 finally did change
counts, I correctly identified the removed-index and the SEO metafields as needing updates — and
**did not realise there was a third place counts live.** `tjjm-region-index.liquid` was on my
verified-unchanged list all session, which made it look safe rather than overlooked.

**The lesson: "counts live in three places, not two."** The data files and removed-index determine
the truth; `tjjm-region-index.liquid` and the page metafields are two independent hand-maintained
copies of it. Any batch that moves a count must update all three, and the file's own comment block
carries a fourth copy — an asserted grand total.

---

## The fix

`snippets/tjjm-region-index.liquid` regenerated from the batch-16 removed-index:

| row | was | now |
|---|---|---|
| Colorado | 156 | **155** |
| New Jersey | 210 | **209** |
| Oklahoma | 98 | **96** |
| *comment block* — "Verified total across all 61 regions" | 5,219 | **5,215** |

The build asserts that the 61 hardcoded counts **sum to the corpus-derived total (5,215)** and that
every corpus region code appears exactly once in the file. That assertion is the check that was
missing; it should run in every future count-changing batch.

Size is unchanged at **3,446 B** — the digit substitutions happened to balance exactly, which is a
neat illustration of why byte size is not a proxy for correctness.

MD5-verified against theme UU by the caller: `8f4faa309ace35a8f6d2738476c47b35`.
Everything else in UU is byte-identical to TT.

---

## State after publishing UU

**5,215 published records / 61 regions.** All three copies of the counts agree:

- **data + removed-index** → 5,215 (authoritative)
- **`tjjm-region-index.liquid`** → 5,215 ✔ fixed here
- **page metafields** → CO 155, NJ 209, OK 96, FL 328 ✔ set in batch 16

---

## TO PUBLISH

**Publish UU `154921402540`.** TT `154919895212` becomes the rollback.
Then re-fetch any region page cookie-free and confirm the nav reads Colorado **155**,
New Jersey **209**, Oklahoma **96**, Florida **328**, and that the 61 entries sum to **5,215**.

---

## For `RULES-tjjm.md`

Two additions this batch argues for:

> **Counts live in three places.** `tjjm-gyms-data*` + `tjjm-removed-index` are the truth.
> `tjjm-region-index.liquid` holds a hand-maintained display count per region **plus an asserted
> grand total in its comment block**, and each region page has `title_tag` / `description_tag`
> metafields with a third copy. **A batch that changes any count must update all three.**
> Assert that the region-index counts sum to the corpus total before writing.

> **Verifying a page's own count does not verify the nav.** The page body count is computed from
> the data and is always right. The nav list is not. Check both.
