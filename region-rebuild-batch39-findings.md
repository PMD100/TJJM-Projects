# Batch 39 — partial. And a process problem I need to stop repeating.

Session of 16 Aug 2026. Built as theme **RRR** (`154974847148`), **staged**.
**Publish RRR `154974847148`** — it is strictly better than QQQ. QQQ `154974617772` is the rollback.

---

## What this batch was meant to do

Rewrite `tjjm-gym-websites-3.liquid` to delete the 25 blanking rows that batch 38 had superseded
with live URLs in file 6, restoring gate C3 (one name, one file).

## What actually happened

**14 of the 25 were deleted. 11 remain.** The rewrite was transmitted by hand from memory rather
than from the built artifact, and it was incomplete.

| | |
|---|---|
| local build, byte-verified | 21,444 B · `5f6c65eb7f1b44cb38740eab0330a636` |
| what reached the theme | 21,726 B · `00461c4f83cd71e9b20edb907348e861` |

### Still duplicated (file 3 blank, shadowed by file 6 URL)
`Knockout Fitness` · `GB Clermont` · `Gracie Barra Blue Ridge` · `Active Martial Arts` ·
`Combat CFMA - Functional Martial Arts` · `Elementum Jiu-jitsu` ·
`Gracie Jiu-Jitsu Altamonte Springs` · `Gracie Jiu-Jitsu Balance Academy` · `Hayastan MMA` ·
`School of Combat Arts` · `Wolfpack Brazilian Jiu Jitsu - Martial Arts`

### No correctness regression — this was checked properly
The risk of deleting a blanking row is that the record falls back to its stored URL, which may be
the dead or hijacked one we removed. That did not happen:

- All 14 deleted names are present in file 6 **with a live URL**
- File 6 contains **zero empty values**, so no name in it can fall back to anything
- Spot checks render correctly: `Hayastan MMA` → `gokor.com`, `GB Clermont` → `bjjclermont.com`,
  `Active Martial Arts` → `herogonzales.com`, `Stamford Judo` → `stamfordjudo.com`

Live state: **5,215 records, 4,230 links, 985 blank.** One link higher than the 4,229 predicted —
a small unexplained delta, not attributable to any file-6 row, worth reconciling next session.

`Odyssey MMA` and `Cascade Jiu-Jitsu` still show blank, which is **correct**: their restorations
belong to the file 1 group that has not been applied yet.

---

## ⚠️ The process problem

This is the **third** time a file has drifted from its built artifact — file 1 in batch 37, and now
file 3 twice over. The cause is the same every time: **I reconstructed the file by hand inside the
mutation instead of transmitting the artifact I had already built and MD5-verified.**

Batches 30 through 36 did this correctly and every one matched to the byte. The discipline broke
when files got large and I started economising.

**The rule, restated: never hand-edit during transmission. Build the file, verify its MD5 locally,
then send exactly that.** If a file is too large to send, that is a reason to split the batch, not
a reason to improvise.

### Repo state — three files now out of sync
| file | status |
|---|---|
| `tjjm-gym-websites.liquid` | theme `2e92d97a…`, repo copy renamed `.NOT-BYTE-EXACT-pull-from-theme` |
| `tjjm-gym-websites-2.liquid` | **never had a local copy at all** |
| `tjjm-gym-websites-3.liquid` | theme `00461c4f…`, local build is a different, cleaner file |

Files 4, 5 and 6 are byte-exact and verified.

---

## Next session — do these in this order

1. **Pull all three files down from the theme** and make the repo authoritative again. Nothing else
   should be written until this is done.
2. **Finish the file 3 cleanup** — delete the remaining 11 duplicate rows, from the pulled copy.
3. **Apply the 6 batch-38 file 1 restorations**: `Cascade Jiu-Jitsu` → `everettbjj.com`,
   `Disciple MMA Academy` → `disciplemmaacademy.com`, `Mid Shore Martial Arts` →
   `fitnessrxworkout.com`, `Miller's Martial Arts Academy` → `mmaa.com`, `Odyssey MMA` →
   `odysseymma.com`, `Team Reno` → `momentumreno.com`.
4. **Apply the 9 batch-36 file 2 recoveries.**
5. **Reconcile the +1 link delta.**
6. Then the remaining ~102 untested removals, and the 1,994 never-read live links.

---

## Where the directory stands

| | |
|---|---|
| records published | **5,215** across 61 regions |
| with a link | **4,230** |
| deliberately link-free | 985 |
| links repointed or restored | **275** |
| of which restored after being wrongly removed | 38 |
| removals re-tested | 343 of 445 |
