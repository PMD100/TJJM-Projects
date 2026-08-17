# Batch 48 — 22 out, 8 repointed. And the browser-drift theory was wrong in a way that matters.

Session of 16 Aug 2026. Built as theme **ZZ2** (`154993066156`), **staged and awaiting publish**.
Overrides only. **Record counts cannot have moved.**
**Publish ZZ2 `154993066156`.** YYY2 `154989691052` becomes the rollback.

---

## Applied — 30 rows

| action | n |
|---|---|
| DEAD | 10 |
| STRIKING_ONLY | 4 |
| AGGREGATOR | 5 |
| WRONG_CITY | 3 |
| HIJACK | 1 |
| **REPOINT** (link fixed, not removed) | **8** |

28 appended to file 6, 2 edited in place (`Ryan Brazilian Jiu Jitsu` in file 3, `Serra BJJ Academy`
in file 1). **Verified: 1,284 override rows, 1,284 distinct names, C3 clean, every written file's
API checksum matched local.**

All 30 names matched **exactly one** published record. Worth noting in passing: the corpus contains
**5,894 distinct names across 5,911 records — 17 duplicated names.** None of ours, but that is a
latent C11 hazard for a future batch and should be resolved.

### The eight repoints
This is the first batch where fixing links outnumbered removing them in any meaningful proportion.
Seven were schools whose site is perfectly healthy and whose *stored deep path* had 404'd —
`/schedule`, `/about-us/`, `/try-a-drop-in-class/`, `/facilities-pembroke-pines/`. The eighth,
`Ric Centron BJJ`, has rebranded to **Generational Grappling Club** at the same Chandler AZ address.

Under the old procedure every one of those would have been blanked as DEAD. Eight working schools
keep a link because the browser round was asked to look for a working root before concluding.

---

## ⚠️ Correction: the drift substitutions are NOT always healthy gyms

Batches 46 and 47 both recorded that when the browser landed on the wrong host, the substituted page
was **always a healthy grappling gym, never a bad one** — and concluded the failure was biased purely
toward false *clean* results. **That is now falsified.** This round's substitutions included a Wix
"ConnectYourDomain Error" page and a gambling-spam restaurant site. The drift is **noise in both
directions**, not a one-way bias, which means it can also produce a false *bad* verdict and cost a
working link.

### Worse: hostname alone is not sufficient
One read kept `host` = `www.facebook.com` while silently swapping the **path** to a different
school's page. A hostname-only assertion — the rule made mandatory in batch 47 — would have passed
that read.

**Rules updated:**
1. Assert `location.hostname` **and `location.pathname`**, both returned from inside the same JS
   evaluation as the body read.
2. **Never read page content in a follow-up call after the probe.** The tab moved between calls twice
   this round. Host, path and body must be captured in one atomic evaluation.
3. Stop describing the drift as biased-toward-clean. Treat every mismatch as a discarded read.

---

## The spot-check of the unverified OK verdicts came back mostly clean

50 links marked OK in browser rounds 1–3 — taken **before** any hostname assertion existed, and
therefore the population most exposed to substitution — were re-checked with the full probe.

**43 confirmed OK. 7 disagreed, and not one of them was a hijack, a parked domain or a wrong
business.** Six were broken deep links whose root still works (now repointed above) and one was a
school that has permanently closed. Page substitution was observed and rejected four times during the
re-check, so the mechanism is real — it just did not, on this sample, cause us to keep anything
genuinely bad.

That is the reassuring answer to the batch-46 worry. The contaminated rounds did not leave dangerous
links in the directory.

---

## Identity pass — 1,680 of 2,170 (77%)

| verdict | 1–3 | 4–6 | 7–8 | 9–10 | 11–12 | **13–14** |
|---|---|---|---|---|---|---|
| OK | 285 | 295 | 209 | 206 | 207 | **206 (86%)** |
| SUSPECT | 33 | 49 | 16 | 22 | 21 | 25 |
| AGGREGATOR | 17 | 9 | 10 | 9 | 6 | 5 |
| WRONG_CITY | 15 | 1 | 3 | 3 | 3 | 3 |
| NO_CITY | 10 | 6 | 2 | 0 | 3 | 1 |

Steady at 86% OK. **370 links still never read** — roughly three more agent groups.

### The fetch-flag false-positive rate held
26 rows the fetch pass flagged went to the browser. **9 came back healthy — 35%.** Running total
across all rounds: **72 of 146 fetch flags were wrong, 49%.** The rule that a fetch may flag but
never remove has now preserved 72 working links and remains the most valuable rule in the programme.

Two rows were deliberately left alone: `Renegade Combat Sports Club` (bot-guard wall, unreadable —
not proven bad) and `Silva BJJ Cajon` (a real BJJ site with no address anywhere, which is a record
problem, not a link problem).

---

## Where the directory stands

| | |
|---|---|
| records published | **5,215** across 61 regions |
| with a link | **4,100** |
| deliberately link-free | 1,115 |
| override rows | 1,284, all distinct names |
| identity pass | **1,680 of 2,170 (77%)** |
| removal audit | complete |
| unverified-OK spot-check | complete |
| hidden-spam re-screen | 200 of 1,202 |

⚠️ **Headroom: file 1 397 B, file 3 830 B, file 2 1,269 B, file 4 1,632 B, file 6 4,753 B.**
At ~2,600 B per batch, **file 6 fills in roughly two more batches.** Files 1 and 3 are effectively
full — a name living in either can be *blanked* safely (that shrinks the file) but a **REPOINT into
file 1 or 3 could overflow it.** Watch for that.

## Next

1. **Add override file 7** and wire one `{%- render -%}` into each of the two rendering surfaces
   (`sections/tjjm-state-directory.liquid` and `sections/tjjm-gym-directory.liquid`). Do this before
   file 6 fills rather than under pressure.
2. **Finish the identity pass** — 370 left, about three groups.
3. **The city-correction pass** — still six confirmed record errors, plus five more relocation
   candidates surfaced this round (Precision JJ Spring Mount → Schwenksville, Ranieri Paiva → Tribe
   BJJ Marietta, Renzo Gracie Harrison → Jersey City, Revive BJJ → St Peters MO, Ricardo Almeida →
   Robbinsville). This needs the 45 data snippets edited; city is not overridable.
4. **Resolve the 17 duplicate names** in the corpus before one of them lands in a batch.
5. Re-check the UNREACHABLE rows and the 162 unscreened social links in
   `scratch/park-sweep/social-deferred.tsv`.
