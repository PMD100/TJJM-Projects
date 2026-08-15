# Batch 12 — NJ, OK, CO, LA. **INTERIM — NOT STAGED, NOT PUBLISHED.**

Session of 13 Aug 2026. **No theme was created and nothing was written to the store for this
batch.** Live MAIN remains **OO `154896597164`** (batches 10 + 11).

This file exists so the verification work survives. Two agent failures stopped the batch partway:
a **sleep/API cutoff** lost group 7 entirely, and the independent recheck could not be started
because of repeated **529 Overloaded** errors.

---

## Where it stands

| stage | status |
|---|---|
| Tranche assembled (145 targets: NJ 43, OK 35, CO 34, LA 33) | ✅ `scratch/repoint-b12/tranche.tsv` |
| Groups 1–6 verified (97 targets) | ✅ `scratch/repoint-b12/verdicts-ALL.tsv` |
| Groups 7–9 (48 targets) | ❌ **not verified** |
| Independent recheck of the 33 confirms | ❌ **not run — blocked on 529** |
| Override build, theme, publish | ❌ not started |

### Verified so far — 97 targets

| verdict | n | share |
|---|---|---|
| DEAD | 34 | 35% |
| CONFIRMED | 33 | 34% |
| NEEDS_BROWSER | 25 | 26% |
| NOT_BJJ | 3 | 3% |
| UNRESOLVED | 2 | 2% |

**33 candidate links** are in `scratch/repoint-b12/confirmed-for-recheck.tsv`, gate-clean on
format (no verdict/action mismatches, no missing schemes, no duplicate ids).

⚠️ **Do not publish these 33 without the independent recheck.** That pass has rejected
1 of 32, 1 of 50 and 2 of 18 in the previous three batches — it is not ceremonial.

### Carried forward — 48 unverified ids
7, 8, 9, 16, 17, 18, 25, 26, 27, 34, 35, 36, 43, 44, 45, 52, 53, 54, 61, 62, 63, 70, 71, 72,
79, 80, 81, 88, 89, 90, 97, 98, 99, 106, 107, 108, 115, 116, 117, 124, 125, 126, 133, 134, 135,
142, 143, 144 — in `scratch/repoint-b12/tranche.tsv`. Groups 7–9 target files are already split
and ready to re-dispatch.

---

## ⚠️ NEW TRAP — the resurrected archive. Add this to the standard checks.

`thehqtraining.com` (id 15) resolved, and served a **complete, convincing school page with the
correct address and phone**. Its own footer read:

> "This is a free demo result from the Wayback Machine Downloader. It is not a complete website."

It is a **re-registered domain replaying a scrape of the dead original**. Nothing else on the page
gave it away — not the DNS, not the branding, not the contact details, which were all genuine
because they were the real school's, historically.

**Standing check from now on: search any page you are about to confirm for the strings
"Wayback Machine Downloader" and "free demo result".**

This is the third distinct way a live-looking page turns out not to be a school's site, alongside
the parked lander and the outright hijack. The category is now big enough to name: **a rendering
page with correct details is not evidence of a live business.**

---

## Other findings from groups 1–6

**Stored-URL death rate stays at ~100%** — 11/11, 13/13, 9/9, 14/14, 11/11, 11/11 across the six
groups. Two more non-NXDOMAIN death modes seen: `advancedbjj.com` and `teamclinch.com` return
REFUSED at their own nameservers; `rwmma.com` is registered on Cloudflare with no A/AAAA at either
apex or www.

**⚠️ Two more hijacked domains.** `cuttingedgebjj.com` is live on Cloudflare and redirects to an
Indonesian gambling SEO farm (`fortworthrvshow.com/arta189`). Never link it. Its genuine successor
is `chokelabacademy.com` — a real rebrand under the same instructor, address and phone, which was
confirmed separately.

**⚠️ Relocation is far more common in this corpus than assumed — seven in 97 targets.** Each is a
recoverable link *and* a city defect in the record:

| record | stored city | actual |
|---|---|---|
| Genesis Training Academy | Arvada CO | Wheat Ridge |
| Anaconda BJJ | Lyndhurst NJ | North Bergen |
| Camal Judo | Woodland Park NJ | Totowa |
| Team Impact | Broken Arrow OK | Coweta |
| Church BJJ | Muskogee OK | Tulsa |
| Renzo Gracie Denville | — | moved within Denville |
| 14ers Jiu Jitsu → Veritas | — | entity dissolved, members refounded |

Combined with batch 9's seven and batch 10's six, **the gazetteer scan (backlog item 4) now has
20+ seed cases.** This is no longer a suspected defect class; it is a measured one.

**Same-name-different-school claimed four more near-misses:** `cheyennebjj.com` is in Cheyenne
**WY** (record is Cheyenne Mountain, CO); `warriorscove.com` renders a convincing school that is a
**Minnesota** operation (record is Baton Rouge); `lucasmartialartsacademy.com` is in **Indiana**
(record is Duncan, OK); `misfitsclubbjj.com` is in **Tujunga CA** (record is Brick, NJ).

**Two exact-name domains now redirect to unrelated schools:** `rockymountainjiujitsu.com` → Six
Blades Littleton; `korebjj.com` → the KORE association HQ rather than the Poteau affiliate.

**BJJ surviving only in a stale meta description, twice more.** `Langston's` → Garrison's Martial
Arts is a genuine rebrand (same address, phone and Facebook page id) but now teaches
TKD/Filipino/Muay Thai/Silat; BJJ persists only in a meta description inherited from the old brand.
Marked NOT_BJJ, not published.

**The MatMade fabricated boilerplate appeared verbatim again** for a fourth unrelated school.

---

## Tooling failures worth recording

1. **An agent completed ~90 tool calls of verification and was cut off before writing its output
   file — all of it lost.** `SendMessage` was not available in the session, so the agent could not
   be resumed. **Instruct verification agents to write their output file incrementally, every few
   rows, rather than once at the end.** This is now in the recheck prompt.
2. **Repeated `529 Overloaded`** blocked the recheck agent twice in a row.

---

## RESUME FROM HERE

1. Run the independent recheck over `scratch/repoint-b12/confirmed-for-recheck.tsv` (33 rows).
   A ready prompt shape is in the batch-9/10/11 findings; add the Wayback-footer check and the
   incremental-write instruction.
2. Drop whatever fails, build with `build_b11.py` as the template (point SRC at `build-b11/`,
   output to `build-b12/`, read `batches/url-overrides-b12.tsv`).
3. Duplicate OO → **PP**, upsert the two override files, MD5-verify yourself.
4. Re-dispatch groups 7–9 (48 targets) either into this batch or the next.
5. ⚠️ **`tjjm-gym-websites-2` is at 21,913 B, ~2.7 KB from the ceiling.** New entries must go in
   file 3 (3,698 B). In-place edits of existing entries are still fine.

**Current live totals, unchanged by this batch: 5,219 published records, 4,480 rendering a link,
739 blank.**
