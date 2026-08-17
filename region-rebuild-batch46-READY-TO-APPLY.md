# Batch 46 — built and staged. Shopify connector is down; nothing was written.

Session of 16 Aug 2026. **WWW `154983399596` remains MAIN and correct.**
Theme **XXX2 `154985070764`** was created and is UNPUBLISHED and **unchanged** — it is a clean
duplicate of WWW, ready to receive this batch.

The Shopify MCP connector began returning `503` on every call, including `query { shop { name } }`,
and has stayed down through ~15 spaced retries. Confirmed independently from my side. This is a
connector outage, not a query problem. **Worth checking whether the Shopify connector needs
reconnecting at your end.**

---

## Ready to apply — 18 removals

Staged in `build-b46/`:
- **`batch46-file6-append.fragment`** (2,582 B) — the complete comment block plus 16 new blanking
  rows, ready to concatenate onto file 6. Projected file 6: 13,964 / 24,576 B.
- **`c3check.py`** — the gate C3 verifier.
- **`worklist.tsv`** — the 18 rows.
- Files 5 and 6 already pulled and MD5-verified against the theme.

| reason | n |
|---|---|
| AGGREGATOR | 6 |
| DEAD | 3 |
| PARKED | 3 |
| WRONG_CITY | 3 |
| HIJACK | 2 |
| STRIKING_ONLY | 1 |

Two in-place edits (`Kings Combat` in file 1, `Orient Jiu Jitsu` in file 3), 16 new rows in file 6.

### On resume
1. Fetch files 1–4 **one at a time** — a combined query for all six (111,353 chars) was rejected as
   too large, and 24 KB singles were already struggling before the outage. If they still fail,
   request `body { ... on OnlineStoreThemeFileBodyUrl { url } }` and download the content instead.
2. Run `c3check.py` over all six before adding rows.
3. Apply, upsert files 1, 3, 6, confirm MD5 both ends, re-run the duplicate check.

---

## Two methodological findings that matter more than the batch

### 1. The browser has been substituting pages, biased toward false OKs

While checking the 22 suspects, navigations repeatedly **reported success while the tab was showing
a different site**, and unrequested tabs kept spawning — `nordikfightclub.com`,
`northlegionacademie.ca`, `novajiujitsu.com`, `montanamma`, and others.

**Every substituted page was a healthy grappling gym, often matching the region of the row being
checked. Never once was it one of the parked or hijacked domains also being visited.** The bias runs
entirely toward recording a bad link as OK.

The agent caught this and discarded every read whose `location.hostname` did not match the requested
URL, re-fetching until it did, so all 22 verdicts in this round are host-verified. **But the three
earlier browser rounds did not verify hostname.** Their OK verdicts — 50 links we decided to keep —
may be contaminated.

**Action: every browser check from now on must assert `location.hostname` matches the requested URL
before reading the body. And the ~50 OK verdicts from suspect rounds 1–3 deserve a spot-check.**
There may also be an extension on that Chrome profile worth investigating.

### 2. Injected spam is invisible to a body-text scan

`Kaiten Mixed Martial Arts Academy` (`princegeorgemma.com`) reads **100% clean** in `innerText`. It
is a real Prince George BC school. The spam is a `position:absolute; visibility:hidden` block of
Polish casino links — **hosted as pages on the school's own domain**. It was found only by scanning
raw `outerHTML` and computed styles.

This is the **ninth** injected-spam case, and it means the previous eight were probably the visible
minority. **Every screen we have run reads `innerText`. None of them could have seen this class.**

**Action: the identity pass prompt needs a hidden-element check** — scan `outerHTML` for
`visibility:hidden`, `display:none`, `position:absolute` blocks containing outbound links, and for
casino/pharma keywords anywhere in the raw HTML rather than the rendered text.

### 3. The fetch pass was wrong on 3 of 5 specific claims
- `kingscombatfitness.com` is **not** striking-only — it lists a BJJ program. Kept.
- `samuraidetroit.com` is **not** karate-only — its Kudo programme combines striking and grappling,
  and it runs a separate MMA programme. Kept. Its `/free-lesson` path 404s while the root works, so
  it is a **repoint**, not a removal. Same for `magnessbjj.com/free-trial/`.
- Only `impactharrison`, `princegeorgemma` and `inspirebjj` were confirmed bad.

---

## Identity pass — 1,440 of 2,170 (66%)

| verdict | 1–3 | 4–6 | 7–8 | 9–10 | 11–12 |
|---|---|---|---|---|---|
| OK | 285 | 295 | 209 | 206 | **207 (86%)** |
| SUSPECT | 33 | 49 | 16 | 22 | 21 |
| AGGREGATOR | 17 | 9 | 10 | 9 | 6 |
| WRONG_CITY | 15 | 1 | 3 | 3 | 3 |
| NO_CITY | 10 | 6 | 2 | 0 | 3 |

**730 links still never read.** 21 new SUSPECT rows await a browser pass.

## Confirmed record-city errors — the city-correction backlog

`scratch/identity/city-errors-CONFIRMED.tsv`. Six so far, four high-confidence:
`Brian Beury` (Albany→Watervliet), `Kioto` (New York→Oakdale), `Long Island MMA`
(Lake Grove→West Babylon), `AKF Lexington` (Nicholasville→Lexington). Plus `Guardian Tactics`
unresolved and `Hero Fitness Academy` low-confidence.

⚠️ I also built a 749-row "city candidates" file from a regex over the verdict notes. **It was
garbage** — it matched street names and cities that agreed with the record. Renamed
`city-candidates.BAD-HEURISTIC-do-not-use.tsv`. The city list has to be built by reading the notes,
not pattern-matching them.
