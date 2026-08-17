# Batch 46 — applied after the outage. 18 out. Two method failures found that matter more.

Session of 16 Aug 2026. Built as theme **XXX2** (`154985070764`), **staged and awaiting publish**.
Overrides only. **Record counts cannot have moved.**
**Publish XXX2 `154985070764`.** WWW `154983399596` becomes the rollback.

⚠️ **The earlier "XXX2 is published" did not take** — WWW was still MAIN when the connector came
back, and XXX2 was still empty. No harm done: XXX2 was a byte-identical copy of WWW at that point,
so publishing it would have changed nothing. The batch has now actually been written to it.

---

## Removed — 18

| reason | n |
|---|---|
| AGGREGATOR | 6 |
| DEAD | 3 |
| PARKED | 3 |
| WRONG_CITY | 3 |
| HIJACK | 2 |
| STRIKING_ONLY | 1 |

All six pre-edit checksums matched the table this batch was built against, so nothing had drifted
during the outage. **Verified after: 1,240 override rows, 1,240 distinct names, zero duplicates.**

The three wrong-city rows are materially distant, not adjacent suburbs: `Peak Performance MMA`
(record Yonkers NY, site serves **Keller, Texas**), `NovaGym` (Montreal → Quebec City, ~250 km),
`Peak Performance` (North Richland Hills → Cedar Park, ~200 mi).

---

## The two findings that matter more than the batch

### 1. The browser was substituting pages, biased toward false OKs

While checking the 22 suspects, navigations repeatedly **reported success while the tab was showing
a different site**, and unrequested tabs kept spawning — `nordikfightclub.com`,
`northlegionacademie.ca`, `novajiujitsu.com`, `montanamma` and others.

**Every substituted page was a healthy grappling gym, often matching the region of the row being
checked. Never once was it one of the parked or hijacked domains also being visited.** The bias runs
entirely toward recording a bad link as good.

The agent caught it and discarded every read whose `location.hostname` did not match the requested
URL, so this round's 22 verdicts are host-verified and sound. **But browser rounds 1–3 did not
verify hostname** — and those produced the ~50 OK verdicts we used to *keep* links.

**Rules added:** every browser check must assert `location.hostname` matches the requested URL
before reading the body. The ~50 OK verdicts from suspect rounds 1–3 need a spot-check. There may
also be an extension on that Chrome profile worth investigating.

### 2. Injected spam is invisible to every screen we have run

`Kaiten Mixed Martial Arts Academy` (`princegeorgemma.com`) reads **100% clean** in `innerText`. It
is a real Prince George BC school. The spam is a `position:absolute; visibility:hidden` block of
Polish casino links — **hosted as pages on the school's own domain**. Found only by scanning raw
`outerHTML` and computed styles.

This is the **ninth** case of this class. **Every screen in this programme reads rendered text.**
None of them could have seen it, which means the eight found earlier were the visible minority and
there are almost certainly more sitting in the 1,240 links already marked OK.

**Rule added:** screens must check hidden elements — scan `outerHTML` for `visibility:hidden`,
`display:none` and `position:absolute` blocks containing outbound links, and for casino/pharma
keywords anywhere in the raw HTML rather than the rendered text.

### 3. A fetch pass was wrong on 3 of 5 specific claims
`kingscombatfitness.com` does list a BJJ programme — kept. `samuraidetroit.com` teaches Kudo, which
combines striking and grappling, plus a separate MMA programme — kept. Both `samuraidetroit.com/free-lesson`
and `magnessbjj.com/free-trial/` 404 while their roots work: those are **repoints**, not removals.

---

## Identity pass — 1,440 of 2,170 (66%)

| verdict | 1–3 | 4–6 | 7–8 | 9–10 | 11–12 |
|---|---|---|---|---|---|
| OK | 285 | 295 | 209 | 206 | 207 (86%) |
| SUSPECT | 33 | 49 | 16 | 22 | 21 |
| AGGREGATOR | 17 | 9 | 10 | 9 | 6 |
| WRONG_CITY | 15 | 1 | 3 | 3 | 3 |
| NO_CITY | 10 | 6 | 2 | 0 | 3 |

**730 links still never read.** 21 SUSPECT rows await a browser pass.

## Where the directory stands

| | |
|---|---|
| records published | **5,215** across 61 regions |
| with a link | **4,130** |
| deliberately link-free | 1,085 |
| override rows | 1,240, all distinct names |
| identity pass | **1,440 of 2,170 (66%)** |

⚠️ Headroom: file 1 **369 B**, file 3 **783 B**, file 2 1,269 B, file 4 1,632 B, file 6 **10,612 B**.

## Next

1. **Browser-check the 21 SUSPECT rows** — with hostname assertion this time.
2. **Spot-check the ~50 OK verdicts from suspect rounds 1–3**, which were taken without it.
3. **Re-screen for hidden injected spam.** This is the one that worries me: it is a fresh sweep over
   links already marked OK, using raw HTML rather than rendered text.
4. **Finish the identity pass** — 730 left, about 6 agent groups.
5. **The city-correction pass** — six confirmed record errors in
   `scratch/identity/city-errors-CONFIRMED.tsv`, four high-confidence.

*(Minor: the batch-46 comment block says `Peak Performance MMA` is recorded in "Yonkers NY" while
the worklist says "New York". Both agree the site serves Keller TX, so the verdict is unaffected.)*
