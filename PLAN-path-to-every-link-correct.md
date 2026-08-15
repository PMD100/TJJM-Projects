# The path to "every gym has a good link or no link"

Written 13 Aug 2026, after batch 18. **This supersedes the framing in earlier briefs**, which
measured progress by the count of blank records. That was the wrong denominator.

---

## The goal, stated precisely

> Every published record either carries a **verified, correct, live** link, or **no link at all**.
> A wrong link is worse than a blank one. A hijacked link is actively harmful.

## Where the corpus actually stands

**5,215 published records / 61 regions.**

| tier | records | status |
|---|---|---|
| **A. Verified links** | 243 | checked this session — identity, city, discipline, still-trading |
| **B. Unverified live links** | **4,335** | rendering their original stored URL. **Never individually checked.** |
| **C. Blank** | 637 | correct-by-default, but ~230 are recoverable |

**Tier B is the real work, and it is the part nobody had counted.** The repointing programme has
been working tier C — the safe half.

### Why tier B cannot be assumed good

- **Eight hostile hijacks found so far**, every one on a school's own expired domain: a Norwegian
  casino, a Chinese gambling site, a Chinese streaming/piracy site, an Indonesian gambling SEO
  farm, an ad-redirect farm, a motorsports content farm, a credit-repair site, and a WordPress farm
  carrying paid links to an escort directory. **All resolve, all return 200, and search engines
  still show the school's old title for them.**
- **Essentially 100% of the ~570 stored URLs tested so far were dead.** That sample is biased —
  they had been flagged — but the rot rate in this corpus is extreme.
- A reachability screen **cannot see a wrong-entity link.** A live site belonging to someone else
  passes it cleanly. That is exactly how the eight hijacks would have been missed.

---

## The good news — the known backlog is 80% cleared

The 6 Aug 2026 link audit flagged **899** candidates. Re-checked today against the live corpus:

| | n |
|---|---|
| already resolved — blanked or repointed by the batch-9-to-18 work | **482** |
| no longer a published record — suppressed or renamed | **233** |
| **still rendering the same unverified link** | **184** |

At that audit's own measured 61% true-positive rate, roughly **112 of the remaining 184 are
genuinely bad.** That is one batch, not a programme.

### Tier-1 progress (this session)
**46 of 184 checked** — `scratch/audit-recheck/verdict-1.tsv`, `verdict-2.tsv`.
Result so far: **20 KEEP, 26 requiring action** (10 dead, 4 wrong-entity, 3 parked, 2 not-grappling,
6 needs-browser, 1 unresolved). A **43% genuine-defect rate**, matching the audit's estimate.

Two that were live and wrong to real users:
- `Ronin Jiu-Jitsu` (North Las Vegas) → its site is a school in **Attleboro, Massachusetts**
- `Guerrero BJJ & MMA` (Caldwell NJ) → redirects to **a different academy** in West Orange

Groups 3–8 are pre-split and ready in `scratch/audit-recheck/targets-{3..8}.tsv`.

---

## The plan, in priority order

### 1. Finish tier 1 — the 184 known-suspect live links
138 remain. ~6 agent groups, one build. **Highest value per unit of effort in the project**: these
are the links most likely to be actively wrong, and they are already live to users.

### 2. Continue tier C — the 637 blanks
~230 recoverable at the established 1-per-2.7 yield. Remaining pool: FL 52 · TX 48 · CA 41 ·
OH 28 · PA 27 · WA 26 · MO 25 · NJ 25 · MA 22 · AZ 20 · VA 20 · MI 19.

### 3. Tier B proper — the ~4,151 links that passed the reachability screen
The long tail, and the last thing standing between here and the goal.

**A DNS screen will not help** — these resolve. They need a body check. But it can be made cheap:

- **Bulk hijack-signature screen.** Fetch each page and pattern-match for casino/gambling/pharma
  keywords, foreign-language content where none is expected, parking-lander boilerplate,
  "Wayback Machine Downloader", and redirects landing off-domain. That is mechanical, needs no
  judgement, and would surface the actively-harmful subset fast.
- **Prioritise by rot risk.** `http://`-only and scheme-less stored URLs are older and likelier
  rotted than `https://`. Sort the queue that way.
- Only the survivors need a human-equivalent body read.

At ~150 records per agent-group and 8 groups per batch, tier B is roughly **3–4 sessions for the
signature screen**, then a longer tail for body reads. Tractable, but it is the bulk of the
remaining work and should be scoped as a programme.

---

## Method notes that make this affordable

- **Verifying an existing link is far cheaper than finding a missing one** — no discovery step.
  Tier B records mostly need one DNS lookup and one page read.
- **Carry known-wrong candidates forward into each batch's prompt.** Batch 14 proved this works:
  three pre-warned traps were all avoided.
- **Write agent output incrementally.** Two agents were lost mid-task this session; one lost ~90
  tool calls of finished work.
- The full trap list is `RULES-tjjm.md` §11 — five ways a live-looking page is not the school's
  site, plus the identity tests.

---

## Definition of done

- Tier 1: 184 → 0 outstanding
- Tier B: every one of the 4,335 either verified live-and-correct, or repointed, or blanked
- Tier C: every blank record either has a verified link or is confirmed unrecoverable

At that point every record on the site carries a link that has been read by someone, or carries
none. That is the goal, and it is reachable — but it is roughly **six to ten more working sessions**,
not one or two.
