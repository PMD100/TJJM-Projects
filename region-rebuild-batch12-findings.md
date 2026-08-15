# Batch 12 — URL repointing: New Jersey, Oklahoma, Colorado, Louisiana.

Session of 13 Aug 2026. Built as theme **PP** (`154911932588`), **staged and awaiting publish**.
Overrides only. **Record counts cannot have moved.**
Supersedes `region-rebuild-batch12-INTERIM.md`, which was written while the batch was blocked.

---

## Result

**145 targets planned · 97 verified · 33 confirmed · 2 rejected on recheck · 31 published.**

| verdict | n | share of 97 |
|---|---|---|
| DEAD | 34 | 35% |
| CONFIRMED | 33 | 34% |
| NEEDS_BROWSER | 25 | 26% |
| NOT_BJJ | 3 | 3% |
| UNRESOLVED | 2 | 2% |

**One recovery per 3.1 attempts.** Slightly worse than b9 (2.8), b10 (2.6) and b11 (2.75) — the
DEAD rate in these four regions was the highest yet at 35%.

**Blank-rendering published records: 739 → 708.**

**48 targets carried forward** (groups 7–9) — see "Interrupted" below. Ids and split files are in
`scratch/repoint-b12/`.

### The independent recheck — no hard failures, two dropped on judgement
All 33 passed DNS and body checks: **21 clean PASS, 12 PASS_WITH_CAVEAT, 0 FAIL**. No parked page,
no hijack, no Wayback-archive replay got through. Two were pulled anyway:

- **`14ers Jiu Jitsu` → Veritas Training Center** — REMOVED. 14ers **dissolved**; former members
  founded Veritas as a new entity. The only link is an owner-controlled 301 from the old domain.
  That is a **new business, not a rebrand** — the record should probably be suppressed, not
  repointed.
- **`Team Impact`** — REMOVED. Group 1 reported the site's own text documented a relocation from
  Broken Arrow to Coweta; the verifier found no such documentation. **Two agents directly
  contradicting each other on the evidence is the same signal that sank `Hayward BJJ` in batch 11.**
  When that happens, drop it.

---

## ⚠️ NEW TRAP — the resurrected archive. Add to standard checks.

`thehqtraining.com` resolved and served a **complete, convincing school page with the correct
address and phone**. Its own footer read:

> "This is a free demo result from the Wayback Machine Downloader. It is not a complete website."

A **re-registered domain replaying a scrape of the dead original**. Nothing else gave it away — the
DNS was live, the branding right, the contact details genuine, because they were the real school's
historically.

**Standing check: search any page you are about to confirm for "Wayback Machine Downloader" and
"free demo result".** The recheck ran this against all 33 and found none, so the check is cheap.

This is the **third** distinct way a live-looking page is not a school's site, alongside the parked
lander and the outright hijack. The category deserves a name in RULES: **a rendering page with
correct details is not evidence of a live business.**

---

## ⚠️ RELOCATION IS A MEASURED DEFECT CLASS NOW — 7 in 97 targets

Every one is both a recoverable link and a wrong-city record:

| record | stored city | actual | evidence |
|---|---|---|---|
| Genesis Training Academy | Arvada CO | Wheat Ridge | adjacent |
| Anaconda BJJ | Lyndhurst NJ | North Bergen | instructor + lineage; **move not documented on-site** |
| Camal Judo | Woodland Park NJ | Totowa | matched phone; site says "since 1996", never mentions Woodland Park |
| Church BJJ | Muskogee OK | **Tulsa, ~50 mi** | matched name, owner surname and phone 918-428-9152 |
| Renzo Gracie Denville | Denville NJ | Denville, new address | matched phone 973-625-9444 |
| The Dojang | New Orleans LA | Kenner | adjacent |
| Pellegrino MMA | Wall Twp NJ | Manasquan | adjacent |

With batch 9's seven and batch 10's six, **backlog item 4's gazetteer scan now has 20+ seed
cases.** Church BJJ at 50 miles is the standout — that is not adjacency, it is a wrong record.

---

## Other findings

**Stored-URL death rate holds at ~100%** — 11/11, 13/13, 9/9, 14/14, 11/11, 11/11 across the six
groups. Two more non-NXDOMAIN death modes: `advancedbjj.com` and `teamclinch.com` return REFUSED at
their own nameservers; `rwmma.com` is registered on Cloudflare with no A/AAAA at apex or www.

**⚠️ Two more hijacked domains.** `cuttingedgebjj.com` is live on Cloudflare and redirects to an
Indonesian gambling SEO farm (`fortworthrvshow.com/arta189`). Never link it. Its genuine successor
`chokelabacademy.com` — same instructor, address and phone — was confirmed separately and published.

**Same-name-different-school, four more:** `cheyennebjj.com` is Cheyenne **WY** (record: Cheyenne
Mountain CO) · `warriorscove.com` renders a convincing school that is a **Minnesota** operation
(record: Baton Rouge) · `lucasmartialartsacademy.com` is **Indiana** (record: Duncan OK) ·
`misfitsclubbjj.com` is **Tujunga CA** (record: Brick NJ).

**Two exact-name domains now redirect to unrelated schools:** `rockymountainjiujitsu.com` → Six
Blades Littleton; `korebjj.com` → the KORE association HQ rather than the Poteau affiliate.

**BJJ surviving only in a stale meta description, twice more.** `Langston's` → Garrison's Martial
Arts is a genuine rebrand (same address, phone, Facebook page id) but now teaches
TKD/Filipino/Muay Thai/Silat; BJJ persists only in inherited meta. NOT_BJJ, not published.

**The MatMade fabricated boilerplate appeared verbatim for a fourth unrelated school.**

---

## Caveats recorded on published links

Twelve carry a caveat; the ones to revisit first:

- **`Rebellion Martial Arts`** — the site names Ada and Duncan in its own posts but publishes **no
  address or phone anywhere**; the contact page renders empty.
- **`David Branch Jiu Jitsu`** — live site with the Hoboken address and a working Wodify signup,
  but **Yelp marks it CLOSED** and there is no phone to cross-check.
- **`Genesis Training Academy`** — BJJ appears only in a kids-class blurb and stale about-us copy;
  no adult BJJ class is listed.
- **`CE Jiu Jitsu` → Chokelab** — address and phone match, but the page never says "Cutting Edge".

---

## What was written

| file | was | now | change |
|---|---|---|---|
| `snippets/tjjm-gym-websites-2.liquid` | 21,913 B | **22,547 B** | 20 in-place edits |
| `snippets/tjjm-gym-websites-3.liquid` | 3,698 B | **4,433 B** | 11 new entries appended |

MD5-verified against theme PP by the caller, not trusted from the write agent:
`977c159ebca087605ffe4c2cf2ec66cc` / `0fe252ca2372fa138c68c23e72ea19ff`.

Override entries now **650** across three files, **zero duplicate names**, 474 blank.

### 🚨 `tjjm-gym-websites-2` is nearly full — 22,547 B against a ~24,576 B ceiling, ~2.0 KB left
**Stop adding new entries to file 2 entirely.** In-place edits of existing entries are still fine
but each one grows the file. **The next batch should create `tjjm-gym-websites-4`** and add it to
the render chain in `sections/tjjm-state-directory.liquid`, before file 2 blocks a write. File 3 is
at 4,433 B with room.

### Structural guarantee that counts did not move
Every count-bearing file in PP is byte-identical to OO — verified by checksum: legacy blob
`1ee054…`, `tjjm-removed-index` `c6069b…`, `sections/tjjm-state-directory` `633ec8…`,
`tjjm-region-index` `3df967…`, `tjjm-gym-addresses` `031ea9…`, `tjjm-gym-websites` file 1
`065db8…`. Only the two override files differ. **5,219 published / 61 regions preserved by
construction.**

---

## Interrupted — what stopped and what it cost

1. **An agent completed ~90 tool calls of verification and was cut off before writing its output
   file. All of it was lost**, and `SendMessage` was unavailable in the session, so it could not be
   resumed. That is group 7 (16 targets).
   → **Fix applied: verification agents are now told to write their output file incrementally,
   every 5 rows, rather than once at the end.** The recheck agent did this and it worked.
2. **Repeated `529 Overloaded`** blocked the recheck twice; it succeeded on a later retry.
3. Groups 8 and 9 were never dispatched.

**48 targets carried forward**, split files ready in `scratch/repoint-b12/targets-{7,8,9}.tsv`.

---

## TO PUBLISH

**Publish PP `154911932588`.** OO `154896597164` becomes the rollback, behind it NN, MM, LL.
No `metafieldsSet` needed — counts unchanged.

---

## Owed

1. **Create `tjjm-gym-websites-4`** before the next repointing batch. File 2 is nearly full.
2. The **48 carried-forward targets** (groups 7–9).
3. **25 NEEDS_BROWSER** rows from this batch — add to the browser queue.
4. **`14ers Jiu Jitsu`** — entity dissolved. Suppression candidate, not a repoint.
5. The gazetteer scan, now with **20+ seed cases**.
