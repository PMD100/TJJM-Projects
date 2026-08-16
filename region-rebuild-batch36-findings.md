# Batch 36 — link recovery begins. 46 schools found, 12 applied, 34 ready.

Session of 15 Aug 2026. Built as theme **OOO** (`154963017900`), **staged and awaiting publish**.
Overrides only. **Record counts cannot have moved.**
**Publish OOO `154963017900`.** NNN `154962034860` becomes the rollback.

The programme has turned a corner. The harm work is essentially done — every link in the corpus has
been screened. This batch is the first of the **recovery** work: finding where the schools we
un-linked actually live now.

---

## The pass: 240 researched, 46 recovered — a 19% hit rate

Four agents took 240 of the 770 records we had blanked in earlier batches and searched for each
school's current home.

| verdict | n | meaning |
|---|---|---|
| **FOUND** | **46** | opened the page, matched the city or street address |
| UNSURE | 75 | plausible candidate, could not confirm — **not published** |
| NOT_FOUND | 103 | no credible current site |
| CLOSED | 16 | positive evidence the school has shut |

**19% recovery is a good rate** and it means roughly **150 more links are recoverable** across the
remaining 530 blanked records — plus whatever the 275 records that never had a URL yield.

### Two tooling limits that make NOT_FOUND an undercount
Both worth knowing before anyone treats 103 as final:

1. **The web-search budget ran out in all four agents**, between rows 22 and 45. Everything after
   that was researched by direct URL guessing only. Those NOT_FOUNDs are low-confidence and worth
   re-running.
2. **Facebook and Instagram return empty bodies to a fetcher.** Every social-only candidate was
   therefore filed UNSURE rather than FOUND — which is most of the 75. A browser pass over just
   those would likely convert a large share of them.

So the true recoverable share is meaningfully higher than 19%.

### A finding that needs following up
Several UNSURE notes say things like *"old domain still resolves and serves live class pages"* —
`Fortitude Jiu Jitsu`, `Gunnison Jiu-Jitsu`, `OC Carlson Gracie Jiu Jitsu`, `Rocknroll BJJ`,
`Catch MMA`, `Hayastan MMA`. **These may be false positives from our own screens** — for example
`OC Carlson Gracie` was blanked in batch 32 on a SERVFAIL, which can be transient. Worth a
deliberate recheck of every record we blanked on a DNS-level failure rather than on page content.

---

## What was written

| file | was | now |
|---|---|---|
| `snippets/tjjm-gym-websites-4.liquid` | 19,136 B | **20,986 B · `fac9197367b65eb90334f78ac2288f8e`** |

Byte-identical to the local build in `build-b36/`. **12 rows changed from blank to a live URL.**

These are **edits in place, not new rows.** Every recovered name already carried a blanking entry,
so gate C3 — one name, one file — requires changing the value where it lives rather than shadowing
it from a later file. That is why the 46 recoveries split across four files by where their blank was
written, and why only 12 could be applied in this batch.

### Verified
```
cross-file duplicate names   none
records published            5,215   unchanged
with a link                  4,182   was 4,170 — exactly plus 12
link-free                    1,033   was 1,045 — exactly minus 12
blanking entries               826   was   838 — exactly minus 12
```

---

## Carried forward — 34 recoveries, verified and waiting

| file to edit | recoveries | why not now |
|---|---|---|
| `tjjm-gym-websites-3.liquid` | **18** | built and gated at `build-b36/`, 24,226 B, 350 B headroom |
| `tjjm-gym-websites.liquid` (file 1) | **7** | needs a full 24 KB rewrite |
| `tjjm-gym-websites-2.liquid` | **9** | needs a full 21 KB rewrite; never yet read into this project |

All 46 URLs, with the evidence read off each page, are in
`scratch/recover/verdict-recover-{1,2,3,4}.tsv`. **File 3's patched version is already built and
byte-verified** — applying it is a single upsert.

Note `tjjm-gym-websites-2.liquid` has never been read in this project; it will need to be pulled
from the theme before it can be edited. Worth doing anyway — it is the last override file with no
local copy in the repo.

---

## Where the directory stands

| | |
|---|---|
| records published | **5,215** across 61 regions |
| with a link | **4,182** |
| deliberately link-free | 1,033 |
| harmful or broken links removed | 445 |
| links repointed to a correct URL | **227** |

## Next, in order

1. **Apply the remaining 34 recoveries** — file 3 first (already built), then files 1 and 2.
2. **A browser pass over the 75 UNSURE rows.** Mostly Facebook and Instagram pages a fetcher cannot
   read. High expected conversion.
3. **Recheck the DNS-failure blanks.** Any record blanked on NXDOMAIN/SERVFAIL/REFUSED rather than
   on page content, in case the failure was transient. This is a correctness issue, not a
   completeness one, so it outranks new recovery work.
4. **Recovery tranche 2** — the remaining 530 blanked records, with a fresh search budget.
5. **The 275 records that never had a URL** — pure gain, no prior link to lose.
6. The identity pass, and the 187 social/aggregator links never screened.
