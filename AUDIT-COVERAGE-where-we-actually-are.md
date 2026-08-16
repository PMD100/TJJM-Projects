# How close are we to 100%? Honestly: about half, not nearly done.

16 Aug 2026, after publishing PPP. This measures what evidence actually sits behind each live link,
rather than counting how many links we have touched.

---

## The directory today

| | |
|---|---|
| records published | **5,215** across 61 regions |
| showing a link | **4,204** |
| deliberately link-free | **1,011** |

## What is behind each of those 4,204 links

| evidence | links | share |
|---|---|---|
| **Browser-rendered** — a real Chrome load, page read | **277** | **6%** |
| Page body read by the **fetcher** | 1,757 | 41% |
| **DNS + parking-IP only — the page was never read** | **1,994** | **47%** |
| No record of any check | 176 | 4% |

**So: 96% of live links have had at least a DNS check. Only 48% have had anyone look at the page.
Only 6% have been seen by a real browser.**

### Why half the corpus was never read
That was a deliberate trade I made in batch 32. The parked-and-dead sweep resolved every hostname
and matched the A records against parking infrastructure, but **only fetched the page when the IPs
looked like a lander** — the instruction was literally "if the IPs match nothing → OK, do not fetch
the page. That keeps this sweep fast." It bought a complete DNS pass over 2,286 links cheaply, and
it found 51 dead or parked domains. But it cannot see a hijack, a wrong business, or a school that
moved city, because it never read a word of those pages.

### And the 41% that were read were read by a fetcher we no longer fully trust
Batch 37's audit found the fetcher serves **stale cached page bodies**, not just cached copies of
dead domains. Six domains returned live-looking school content to a fetch that a real browser showed
were dead. So the 1,757 fetch-read links are real evidence, but weaker than they looked when they
were recorded.

---

## The two known error pools, sized

**1. Unread live links — roughly 60 bad hiding in the 1,994.**
Content screens measured the `https://` population at 1.7–3% actively bad with near-zero hijacks.
Applying that gives ~40–60 bad links, mostly wrong-business and wrong-location rather than casinos.

**2. Wrongly-removed links — roughly 50 more, on top of the 22 already restored.**
Of 445 removals, only 131 have been re-tested and **21 of those were wrong — a 16% error rate**.
The other ~314 (parked, hijacked, wrong-business) have never been re-tested, and they were judged by
the same fetcher. If the error rate holds, that is ~50 live schools still wrongly un-linked.

**Best estimate of remaining defects: about 110 links, split roughly evenly between links that
should be removed and links that should be restored.**

---

## What "100%" would actually require

| pass | scope | why |
|---|---|---|
| **A. Read the 1,994 unread pages** | 1,994 links | the single biggest gap; turns 47% of the corpus from "resolves" into "verified" |
| **B. Re-test the 314 untested removals** | 314 records | 16% measured error rate; restores good schools |
| **C. Browser-check the fetch-read tier** | 1,757 links | the fetcher caches; ideally sampled rather than swept |
| **D. The identity pass** | all 4,204 | does the page belong to *this* school in *this* city — never systematically done |
| **E. Recovery** | 1,011 blank | 19% hit rate measured; ~190 more links findable |

A and B are correctness. C is confidence. D is the last quality tier. E is growth.

**Realistic sequencing:** B first — it is only 314 records, it restores real schools, and the error
rate is known and high. Then A, which is large but mechanical and can run at ~500 links per session.
Then E. C and D last, and C is better sampled than swept.

At roughly 500 links per session for A, and one session each for B and the first half of E, **the
remaining correctness work is about six to eight sessions.** D is open-ended.

---

## What is genuinely finished

- **Every link has had a DNS and parking check.** No NXDOMAIN, no for-sale lander, no dead
  registration is knowingly live. That was the original harm.
- **61 hijacks removed** — casinos, slots, togel, pharma, and six compromised real school sites
  carrying injected spam.
- **The structural work is done.** One source of truth, both directory surfaces rendering from the
  same snippets, override capacity for ~1,900 more rows, and a repo holding every batch.
- **Counts are provably stable.** 5,215 records across 61 regions, reconciled region-by-region
  against the region index on every batch since 30.

## What I would not claim

That the directory is accurate. It is **safe** — the actively harmful links are gone — and it is
**comprehensive**. Accuracy is at about half, and the honest headline is that **a link in this
directory has a 48% chance anyone has ever looked at the page behind it.**
