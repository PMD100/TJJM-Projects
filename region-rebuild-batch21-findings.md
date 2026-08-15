# Batch 21 — the hijack screen. Measuring how bad the unread half really is.

Session of 13 Aug 2026. Built as theme **YY** (`154946666668`), **staged and awaiting publish**.
Overrides only. **Record counts cannot have moved.**

⚠️ **XX `154934083756` (batch 20) may still be unpublished.** YY is built on top of it and contains
batch 20 as well — **publishing YY alone is sufficient.**

---

## The finding: 7.1% of unread live links are actively bad

This was a **triage screen**, not an audit — one fetch per link, asking only *is this a martial arts
school or something else?* The 240 highest-rot-risk unread links were checked.

| verdict | n | share |
|---|---|---|
| OK — a martial arts / combat sports site | 199 | 82.9% |
| EMPTY — JS-rendered, needs a browser | 24 | 10.0% |
| **PARKED** | **10** | **4.2%** |
| **HIJACK** | **6** | **2.5%** |
| DEAD | 1 | 0.4% |

**17 links blanked — 7.1% of everything screened.**

### What this implies for the rest
The rate held steady across both groups of 120 (3 hijacks each). Extrapolated across the **4,240
unread live links**:

- **~106 hijacked links** live on the site right now
- **~300 actively bad links** in total

That is the size of the problem nobody had measured. At this rate the full screen is **~35 agent
groups, four or five sessions** — and it is unambiguously the highest-value work left.

---

## ⚠️ SIXTEEN HIJACKS NOW. Six new this batch.

| record | what its domain now serves |
|---|---|
| `Union Combat Academy` | JDM88 — Indonesian gambling / slots |
| `Unlimited MMA` | Indonesian togel/slots SEO farm, SBOBET88 + MAXBET nav, hundreds of outbound spam domains |
| `10th Planet SF` | a San Francisco **party-bus / limo rental** SEO content farm with scraped BJJ filler |
| `Scorpion MMA` | `thebest100hotels.com` — auto-generated hotel-review ad farm |
| **`Black Flag Jiu-Jitsu Club`** | a **genuine BJJ site** carrying an injected **FXPro forex** paid-link article |
| **`Hayastan MMA`** (`gokor.com`) | a **genuine gym page** carrying an injected **German pharmacy / ED** paid-link paragraph |

### ⚠️ A new and nastier failure mode — compromised real sites
The last two are not re-registered domains. They are **the schools' own live sites, still running,
with paid SEO spam injected into them**. The gym content is real and correct; the page also links
to a forex broker and a German pharmacy.

That defeats every screen used so far, including this one's headline question — the site *is* a
martial arts school. **Only reading the whole body catches it.** Future screens must scan for
injected content in footers and stray articles on otherwise-normal pages, not just judge the page's
overall subject.

## Ten parked domains, one dead
BrandBucket, HugeDomains, GoDaddy for-sale ×3, UpLaunch agency placeholder, Webs.com shutdown
redirecting to a VistaPrint ad, "Website Unavailable", and a `.co.nr` placeholder.

## Two wrong-location links flagged, not blanked
`cscmhk.com` and `nextgenerationmma.com` are genuine gyms — in **Kansas** and **Texas**, wrong for
the schools listed. Left live and recorded in `batches/hijack-screen-fixes-b21.tsv` because the
screen's remit was harmful content, not identity. They belong to the identity pass.

---

## What was written

| file | was | now | change |
|---|---|---|---|
| `snippets/tjjm-gym-websites-3.liquid` | 12,559 B | **13,055 B** | 17 blanking entries added |

Files 1 and 2 unchanged. MD5-verified against theme YY by the caller:
`89b19475778c981b77e0b0a59f1ea114`. **785 override entries, zero duplicate names.**

### Structural guarantee
Every count-bearing file in YY is byte-identical to XX — legacy blob `1ee054…`, removed-index
`98ee61…`, section `633ec8…`, region-index `8f4faa…`, websites-1 `16a715…`, websites-2 `08c171…`.
**5,215 published / 61 regions preserved by construction.**

---

## TO PUBLISH

**Publish YY `154946666668`.** It contains batches 20 and 21; publishing it alone is sufficient.
XX `154934083756` becomes the rollback.
No `metafieldsSet` needed — counts unchanged.

---

## Next

1. **Continue the screen — 4,000 unread links remain.** Worklists are pre-built:
   `scratch/hijack-screen/targets-{3..8}.tsv` cover the next 720, and
   `scratch/hijack-screen/all-targets.tsv` holds all 4,240 ranked by rot risk
   (`http://`-only first, then scheme-less, then `https://`).
   **Add the injected-spam check** to the prompt — two of six hijacks this batch were compromised
   real sites that the current wording would let through.
2. **24 EMPTY rows** from this batch join the browser queue, which now holds ~45.
3. The identity pass — wrong-location and wrong-entity links — remains separate and later.
