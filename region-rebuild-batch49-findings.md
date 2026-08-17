# Batch 49 — the identity pass is finished. Every live link in the directory has now been read.

Session of 17 Aug 2026. Built as theme **AB3** (`155004502188`), **staged and awaiting publish**.
Overrides plus a structural change to both rendering surfaces. **Record counts cannot have moved.**
**Publish AB3 `155004502188`.** ZZ2 `154993066156` becomes the rollback.

---

## The milestone

**2,170 of 2,170 links read. The identity pass is complete.**

When this started, 4,335 links had passed a DNS check and nothing else — no one had ever looked at
what was on the other end. Every one has now been opened and judged: is this the right school's own
site, in the right town, still teaching grappling?

Final distribution across all 17 groups:

| verdict | total | share |
|---|---|---|
| OK | 1,866 | 86% |
| SUSPECT (sent to a browser round) | 182 | 8% |
| AGGREGATOR | 66 | 3% |
| WRONG_CITY | 33 | 2% |
| NO_CITY | 23 | 1% |

Roughly **one live link in seven had a problem of some kind**, and the rate held remarkably steady
from group 4 onwards once the wrong-city classifier stopped over-triggering.

---

## Applied — 45 rows

| reason | n |
|---|---|
| AGGREGATOR | 20 |
| DEAD | 6 |
| WRONG_BUSINESS | 6 |
| STRIKING_ONLY | 4 |
| WRONG_CITY | 4 |
| HIJACK | 2 |
| **REPOINT** | **3** |

42 appended to **file 7**, 3 edited in place in file 3.
**Verified: 1,326 override rows, 1,326 distinct names, C3/C5/C11/BYTES all pass, both written files'
API checksums matched local.**

### Two more injected-spam cases, and one is the largest yet
`Tennessee Brazilian Jiu-Jitsu Academy` is a real Spring Hill school whose site carries **92 hidden
German casino links, hosted as pages on its own domain**. Visible body text contains the word
"casino" zero times. `Tarpein's Dojo` in Davenport is the same pattern with a different payload.
That makes **eleven** cases of this class. Every one of them would read clean to any screen based on
rendered text.

### A crossed pair worth naming
`Vitor Shaolin BJJ NYC` (New York) pointed at `bjjnewyorkcity.com`, which now serves **Modern Martial
Arts / NYC BJJ Academy** in Times Square. Meanwhile `Yeti MMA` (New Jersey) pointed at
`shaolinbjj.com`, which serves **Vitor Shaolin's own school in Union County NJ**. Two records, two
wrong links, pointing past each other. Both blanked.

`Xtreme Couture MMA` was repointed rather than removed: the stored `.tv` domain is a Thai-language
content farm, `xtremecouture.com` is the apparel store, and the actual Las Vegas gym is at
`xcmma.com`.

---

## Structural: override file 7 exists, and both surfaces read it

File 6 had about two batches of headroom left. Rather than hit the ceiling mid-batch, file 7 was
created and wired **before** it was needed.

The risk here was the mistake that cost this project 28 batches: the directory renders on **two**
independent surfaces, and for a long time only one of them read the override snippets. So the wiring
was verified end to end rather than assumed —

- A temporary test row was added to file 7 for a school present in no other override file.
- Both the region page **and** the Schools Near You page were loaded through the theme preview and
  confirmed to render that test URL.
- The test row was removed and both surfaces re-checked to confirm it was gone, with the flat page
  still reporting 5,215 gyms, 61 regions and the full override island.

File 7 now holds 42 rows and **20,218 bytes of headroom — roughly eight more batches.**

⚠️ One gate could not be met as written and I want that on the record. The plan called for a diff
showing "exactly one added line." Both surfaces render the whole chain of `{%- render -%}` calls on a
**single line**, so the change is intra-line and `diff` reports one line replaced. The agent
substituted a stronger machine check — a single 36-character insertion at a known offset, every other
render present exactly once, line count unchanged — and verified the render order is 1→7. That is a
better check than the one I specified, but it is not the check I specified.

---

## The fetch-flag false-positive rate got worse, not better

56 rows went to the browser round. **36 came back healthy — 64%.**

Running total across all rounds: **108 of 202 fetch flags were wrong, 53%.** A fetch flag on this
corpus is now formally worse than a coin toss. The rule that a fetch may flag but never remove has
preserved **108 working links** and remains the most valuable rule in the programme.

### Drift is now confirmed as noise in both directions
Last batch I retracted the claim that browser substitutions always land on healthy gyms. This round
confirms the retraction from the other side. One agent caught a drift onto `/SouthernKarate/` while
requesting `/FlowstateJJ` — **same host, different path** — which would have produced a false
STRIKING_ONLY and cost a working link. Another drift landed on a BJJ-keyword-rich page that would
have falsely *cleared* a striking-only check. Both directions, same session.

The host-and-path assertion caught both. It should be treated as non-negotiable.

Two rows were deliberately left alone rather than removed: `Straight Blast Gym New Jersey` (never
resolved to its own host after repeated retries — unreadable, not proven bad) and
`Snake Pit U.S.A. MMA` (record says Galloway NJ, site says Hammonton NJ, ~18 miles — that is a
record-city question, not a link problem).

---

## Where the directory stands

| | |
|---|---|
| records published | **5,215** across 61 regions |
| with a link | **4,058** |
| deliberately link-free | 1,157 |
| override rows | 1,326, all distinct names |
| **identity pass** | **2,170 of 2,170 — COMPLETE** |
| removal audit | complete |
| unverified-OK spot-check | complete |
| hidden-spam re-screen | 200 of 1,202 |

Headroom: file 1 397 B, file 3 923 B, file 2 1,269 B, file 4 1,632 B, file 6 4,753 B,
**file 7 20,218 B.**

### Correction to a number I have been quoting
I said the corpus holds 17 duplicated names. It holds **16 duplicated names across 17 surplus
records** — `Capital MMA & Elite Fitness` appears three times, not twice. None of them were touched
by this batch, but gate C11 will fail on them whenever one comes up.

## Next

Now that every link has been read once, the remaining work is different in kind — it is about the
**records**, not the links:

1. **The city-correction pass.** This is now the biggest known accuracy defect and it cannot be fixed
   with overrides — city lives in the data snippets. Confirmed errors keep accumulating: the original
   six, plus Precision JJ Spring Mount, Ranieri Paiva, Renzo Gracie Harrison, Revive BJJ, Ricardo
   Almeida, Snake Pit, Teknica, The Dojang NOLA, Tiger Academy, Tutaj BJJ and several same-town
   address moves. These misfile schools onto the wrong town's page.
2. **Resolve the 16 duplicated names** before one lands in a batch and trips C11.
3. **Continue the hidden-spam re-screen** — 1,002 cleared links unscanned, and this batch found two
   more cases in the small sample it did look at. That changes my view: the first 200 coming back
   empty now looks like luck rather than evidence.
4. **Re-check the UNREACHABLE and UNSURE rows** accumulated across batches.
5. **The 162 unscreened social links** in `scratch/park-sweep/social-deferred.tsv`.
