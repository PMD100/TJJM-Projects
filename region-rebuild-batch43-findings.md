# Batch 43 — the rules are rewritten. Identity pass at 720 of 2,170.

Session of 16 Aug 2026. **No theme change** — UUU `154980188332` remains MAIN and correct.
This batch produced the rulebook and 360 more link verdicts, not a publish.

---

## `RULES-tjjm.md` rewritten — 22,133 B → 42,061 B

The original is preserved verbatim as `RULES-tjjm.PRE-BATCH43.md`.

New sections: **§11** *Evidence standards* (rewritten end to end), **§12** parking fingerprints,
**§13** editorial policy, **§14** the two rendering surfaces, **§15** writing to the theme,
**§16** audit coverage. Amended: the header, §3, §4, §5, §6, §8, §9.

### Nine things the old rules said that were wrong

The agent was asked specifically to hunt contradictions, because stale guidance is more dangerous
than missing guidance. The important ones:

1. **"An empty body is NOT evidence of death — live JS-rendered sites return empty."** This was the
   single most damaging line in the file. It was grounds to *leave empty-body rows alone*. When 198
   of them were finally opened in a browser, **137 were broken.** Corrected, keeping the narrow true
   part: an empty body is not proof, so it triggers a browser check rather than a removal.
2. **"Essentially 100% of stored URLs proved dead."** A targeted-sample rate stated as a corpus fact,
   and effectively the licence for thin-evidence removals across many batches. Explicitly retracted.
3. **"Always resolve DNS before believing any page"** read as *sufficient*. Four named failure modes
   resolve perfectly cleanly. Reframed as necessary-but-not-sufficient.
4. **"Open the page and read the body."** In context that meant a fetch — the exact action that
   nearly cut 11 working links in batch 42. Now specifies a browser.
5. **"`web_fetch` dedupes within a session — bust it with `?v=1`."** True but dangerously
   incomplete; it reads as though a cache-buster solves the caching problem. It does not.
6. **Parked-lander detection** was described as browser-only. Now carries the calibrated IP
   fingerprints — with the near-miss GoDaddy pairs called out, because matching "a GoDaddy IP"
   rather than the exact pair would blank live schools.
7. **Hijack removals were implicitly permanent.** They are snapshots; two have since been cleaned up.
8. **"A dormant social page is not a live school"** sat unreconciled against your ruling that a
   school's own Facebook or Instagram page is acceptable. Reconciled on the live/dormant axis.
9. **Nothing in the file said there were two rendering surfaces.** That silence is what let ~4,150
   unvetted links render for 28 batches. Now §14.

I also corrected the header, which still described the corpus as 4,519 records. It is 5,215 — the
region pages render 45 data snippets, not the 38 the early sections assume.

---

## Identity pass — 720 of 2,170 read (33%)

| verdict | first 360 | second 360 |
|---|---|---|
| OK | 285 (79%) | **295 (82%)** |
| SUSPECT | 33 | 49 |
| AGGREGATOR | 17 | 9 |
| WRONG_CITY | 15 | **1** |
| NO_CITY | 10 | 6 |

**The wrong-city rule change worked.** Tightening the instruction to exclude adjacent suburbs and
metro neighbours took the rate from 15 per 360 to 1 per 360. The first 360 were over-flagged; the
second 360 are calibrated. Group 6's agent explicitly listed seven schools whose sites give a newer
address in a nearby town — Dripping Springs, Naperville, Tallmadge, Wheat Ridge, East Brunswick,
Lake St Louis, Waterford CT — and correctly marked them all OK.

### Pending, not yet applied
- **49 SUSPECT rows** need a browser pass before any action. About half are Facebook pages the
  fetcher cannot read as a class and are probably healthy. Genuinely bad-looking so far:
  `Denver Jiu Jitsu` (now scraped retail spam), `DualForces 001` (now an LA branding studio),
  `Cyclone Brazilian Jiu Jitsu` ("Website Unavailable"), `GB Sorrento Valley` (domain for sale),
  `GB Whittier` (ClickFunnels account paused), `Coosa Jiu Jitsu` (gym closed, video library only).
- **9 AGGREGATOR rows** — booking platforms, `business.site` pages and one Gracie Barra national
  homepage standing in for `GB Coral Springs`. All blank under your policy.
- **1 WRONG_CITY** — `Elite Jiu-Jitsu Academy`, recorded in Idaho, site serves **Newark, Delaware**.

### One free find worth keeping
`www.gbheights.com` returns an empty body while `gbheights.com` serves the real Gracie Barra Heights
site. That is the apex/www rule from §11.3 catching a live example — the stored URL just needs its
`www.` dropped.

---

## Where the directory stands

| | |
|---|---|
| records published | **5,215** across 61 regions |
| with a link | **4,205** |
| deliberately link-free | 1,010 |
| **identity pass** | **720 of 2,170 (33%)** |
| removal audit | complete |

## Next

1. **Browser-check the 49 SUSPECT rows**, then apply those plus the 9 aggregators and the 1
   wrong-city in one batch — into file 6, which has ~18 KB spare.
2. **Continue the identity pass** — 1,450 links still never read, about 12 agent groups.
3. **The city-correction pass.** Records whose stored city is wrong are now confirmed to exist
   (`AKF Lexington`, `Brian Beury`, and the seven group-6 relocations). City is not overridable —
   this needs the data snippets edited.
