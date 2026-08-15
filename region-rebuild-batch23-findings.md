# Batch 23 — hijack screen, group 5.

Session of 13 Aug 2026. Built as theme **AAA** (`154948108460`), **staged and awaiting publish**.
Overrides only. **Record counts cannot have moved.**

**Publish AAA `154948108460`.** ZZ `154947354796` becomes the rollback.
⚠️ Note the naming has rolled past ZZ — subsequent themes are AAA, BBB, CCC.

---

## Cumulative screen — 600 of 4,240 unread links

| verdict | n | share |
|---|---|---|
| OK — a martial arts site | 492 | 82.0% |
| EMPTY — JS-rendered, needs a browser | 59 | 9.8% |
| **PARKED** | **21** | **3.5%** |
| **HIJACK** | **13** | **2.2%** |
| **WRONG_BUSINESS** | **6** | **1.0%** |
| DEAD | 5 | 0.8% |
| UNSURE | 4 | 0.7% |

**45 blanked in total — 7.5% actively bad.**

### Projection over all 4,240 unread links
- **~92 hijacked**
- **~318 actively bad**

The estimate has been stable across five groups of 120. Hijack rate by group: 3, 3, 4, 2, 1 —
averaging 2.2%, drifting slightly down as the screen moves from `http://`-only stored URLs into
scheme-less ones, which is the expected direction if `http://` correlates with older, likelier-
lapsed registrations.

**12 blanked in this batch.**

---

## Findings

**Twenty-first hijack:** `10th Planet Jiu Jitsu Perry` — `10thplanetperry.com` redirects to
`wargapokerr2.com`, a WARGAPOKER Indonesian IDN Poker / IDNPLAY gambling site.

**Two wrong-business links:**
- `Victory Training` → a Roscoe Village personal-training gym with reserved-equipment slots. No
  martial arts.
- `Patriot Sports and Fitness` → redirects to `strongerfighter.com`, an **unrelated** MMA/wrestling
  gym in Round Rock & Hutto, Texas.

**Seven parked**, including a notable pattern: **three separate records all pointed at
`knuckleupfitness.com`**, which is now a Nexcess hosting placeholder. One dead domain was serving
as the link for three different schools — worth remembering that a single dead host can account for
several bad rows.

Two more on **ExpiredDomains.com $195 for-sale listings**, which is a new lander type for the list.

**No injected-spam (Q2) cases in this group** — the check ran and found none, which is itself
useful: the four found so far were not a systematic pattern in every group.

---

## What was written

| file | was | now | change |
|---|---|---|---|
| `snippets/tjjm-gym-websites-3.liquid` | 13,548 B | **13,887 B** | 12 blanking entries added |

Files 1 and 2 unchanged. MD5-verified against theme AAA by the caller:
`021f5a80a27dac7205220e47fa47b639`. **813 override entries, zero duplicate names.**

### Structural guarantee
Every count-bearing file in AAA is byte-identical to ZZ — legacy blob `1ee054…`, removed-index
`98ee61…`, section `633ec8…`, region-index `8f4faa…`, websites-1 `16a715…`, websites-2 `08c171…`.
**5,215 published / 61 regions preserved by construction.**

---

## Running total of the harmful-link programme

| batch | screened / audited | links removed or fixed |
|---|---|---|
| 19–20 (the 6 Aug flagged set) | 184 | 95 |
| 21 (screen groups 1–2) | 240 | 17 |
| 22 (screen groups 3–4) | 240 | 16 |
| 23 (screen group 5) | 120 | 12 |
| **total** | **784** | **140** |

Combined with the 190 links *restored* in batches 9–18, the directory has had **330 link changes**
in one day.

---

## Next

1. **3,640 unread links remain.** Worklists 6–8 are pre-built; `all-targets.tsv` holds all 4,240
   ranked by rot risk. **Roughly three more sessions.**
2. **59 EMPTY rows** — the browser queue now holds ~80 across all batches. Worth a dedicated
   browser session once the fetch-based screen is complete.
3. **The identity pass** — wrong-location and wrong-school links that a content screen passes
   cleanly — is the last tier and still untouched.
