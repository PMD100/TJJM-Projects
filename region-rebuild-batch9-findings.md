# Batch 9 — the URL repointing pass. Florida + four cross-region debts.

Session of 13 Aug 2026. Built as theme **MM** (`154892861612`), **staged and awaiting publish**
(`themePublish` is blocked).

This is the first batch that is **overrides only**. No record was added, removed, renamed or
re-citied. No data file, no removed-index, no section was touched. **Record counts cannot have
moved** — see the structural guarantee below.

---

## Result

**88 targets attempted → 31 links published. One recovery per 2.8 attempts.**

| verdict | n | share |
|---|---|---|
| CONFIRMED | 33 | 38% |
| DEAD | 24 | 27% |
| NEEDS_BROWSER | 18 | 20% |
| UNRESOLVED | 6 | 7% |
| WRONG_ENTITY | 4 | 5% |
| NOT_BJJ | 3 | 3% |

33 confirmed → 31 published: one dropped on independent re-check (**Paladin MMA**, id 29) and
one held as FLAG (**Renato Tavares Assoc HQ**, id 79 — see below).

Published: FL 28 · AL 1 (`Athens Jiu Jitsu`) · NC 1 (`Ethos BJJ`) · TX 1 (`Ironside Martial Arts`).
16 are clean passes; 15 carry a stated caveat, all recorded in `batches/url-overrides-b9.tsv`.

**Blank-rendering published records: 833 → 802.**

---

## ⚠️ THE BIGGEST FINDING — `web_fetch` serves cached copies of DELETED domains

**A page body is not evidence that a domain exists.** Eight domains in this batch returned long,
detailed, entirely plausible pages — correct branding, correct street addresses, named black
belts, testimonials — while being **NXDOMAIN at the authoritative gTLD servers**:

`agogiac.com` · `gbwestpalm.com` · `ironsidemartialarts.com` · `renatotavaresbjj.com` ·
`toddcutlerbjj.com` · `gradysmma.com` · `tridentjiujitsu.com` · `westvolusiamma.com`

`web_fetch` serves a cached copy; search indexes serve stale titles. On `gbwestpalm.com` a
researcher would have published a dead link **and** transcribed a named 5th-degree black belt's
credentials from a defunct site — the exact fabrication failure `METHOD-RULES-agent.md` forbids,
arrived at honestly.

### The fix, and it is cheap — adopt as standing method

For **every** candidate URL, before believing anything:

    web_fetch  https://dns.google/resolve?name=<hostname>&type=A

- `Status: 3` → NXDOMAIN → conclusively DEAD.
- `Status: 0` **with an `Answer` array carrying A records** → alive.
- `Status: 0` with **no** Answer → no A record → dead.
- Registered but nameservers return REFUSED (lame delegation) → no A record obtainable → dead.
  Seen on `usajujitsu.net` and `rtbjjai.com`.

This inverts RULES §4's implicit assumption in both directions and supersedes it:
**an empty body is not evidence of death** (live JS sites return empty), and **a full body is
not evidence of life** (caches lie). Only DNS separates them. Run it even when the page renders.

---

## Other traps confirmed or newly found

**Stored links in this corpus are essentially all dead.** Across the batches that reported it:
11/11, 8/8, 7/7 and 11/11 stored domains were NXDOMAIN. The "override blanks it" flag was
correct every single time. **Blanking was the right call; the links had genuinely rotted.**

**⚠️ Aggregator boilerplate is fabricated, and now provably so.** The sentence *"passionate about
Brazilian Jiu-Jitsu… strong fundamentals, technical precision, and a supportive training
culture"* appeared **word-for-word for two unrelated schools**, both traced to MatMade. Any BJJ
claim sourced from an aggregator template is worthless as evidence of discipline. This is a
sharper version of the existing "aggregators fabricate" rule: they don't just invent schools,
they invent *attributes*, from a template.

**Search summaries asserted at least eight dead domains as live**, one phrased "the website is
located at …". Two independent summaries agreeing meant nothing — neither had checked. Confirms
RULES: search summaries are not sources.

**BJJ in the meta description only.** `Hands Down Martial Arts` (WPB) and `Paladin MMA` (Hialeah)
both carry "Brazilian Jiu-Jitsu" in `<meta>` while their actual class grids contain no grappling
at all. Both rejected. This is the discipline-side twin of "title tags lie about location".

**Domain repurposing, twice:** `miamijiujitsu.com` → a different school in a different city;
`braziliantopteamflorida.com` (stored for `GB Boca Raton`) → Brazilian Top Team, a different
affiliation. Both return 200.

**Rebrands are common and are recoveries, not losses.** Five schools kept address, phone and head
instructor while changing name: Hidden Lotus→Zen Ronin, Fight Sports Daytona→Todd Cutler MA,
ATT Vero Beach→RT Martial Arts, Ironside→Double Five Mid Cities, Gulf Breeze JJ→Checkmat Gulf
Breeze. Each was confirmed by matching address/phone/instructor, never by assumption.

---

## ⚠️ The `city` field is unreliable, and this batch measured it

Seven published records have a URL that is unambiguously the right school in a city that
disagrees with the stored `c` value:

| record | stored city | actual city |
|---|---|---|
| GB Palm Coast | **Orlando** | Palm Coast (~90 mi away) |
| Marcus Aurelio Jiu Jitsu Academy | Aventura | North Miami |
| Combat Club Lake Worth | Lake Worth | Lantana (ZIP 33462) |
| Teknica MMA | Miami | Pinecrest |
| Fight Sports Daytona | Port Orange | South Daytona |
| Destin Academy of MMA | Destin | Miramar Beach |
| New Port Richey Jiu-jitsu Academy | Tarpon Springs | (name/city conflict) |

`GB Palm Coast` filed under Orlando is a real defect, not adjacency. **This is backlog item 10's
city/state gazetteer scan finding its seed set** — it can be seeded with these seven plus
`Precision MMA` and will fire.

---

## Duplicate-record leads found incidentally

- `theacademyofmma.com` backs **two** records: `West Volusia Academy Of MMA` (DeLand) and
  `Orange City Academy Of MMA` (Orange City). Yelp places the business in DeLand; **Orange City
  is the likely stale duplicate.**
- `usajujitsu.net` backs **two**: `Robson Moura Jiu-Jitsu` (Oxford) and `USA Jiu-Jitsu` (Wildwood).
  Robson Moura's own association affiliate list names six Florida schools and **no Oxford**.
- `BJJ Academy Of Sarasota (wbjja)` — its domain redirects to a live school at the **same street
  address** (6170 N Lockwood Ridge Rd) branded **Six Blades Jiu Jitsu** under Xande Ribeiro. Same
  mats, different school. Not published.
- `Gracie Jiu-Jitsu North Miami Beach` — the address is occupied by **Valente Brothers**.

---

## Held, not published

- **`Renato Tavares Assoc HQ` (id 79)** — the only page confirming this school in Vero Beach is
  Renato Tavares' own WordPress blog, newest post **February 2011**. It names the school and the
  address correctly, so it technically confirms, but publishing a 15-year-stale blog may be worse
  than no link. Left blank pending a call.
- **`Master Lowell's MMA Academy`** — `jlmma.blogspot.com` resolves and mentions BJJ in Melbourne,
  but the newest post is Aug 2011 and it links to the now-dead JLMMA.com. A live URL, not a live
  school.
- **`Refit Academy - Coral Gables`** — the operator has a live site under a new brand, but it lists
  only the former **Wynwood** location. A different branch, not a rename.

---

## 18 carried forward — the browser worklist

These resolve but return an empty JS body, or bottom out at Facebook/Instagram, which `web_fetch`
cannot render at all. **This is the standing browser-render phase batch 7 recommended.**

FL: Champion MMA of Bradenton · Grady's Family MMA · Real World MMA · Burns Bros Jiu Jitsu ·
Carlson Gracie Manny Soares · Fight Zone MMA · Gainesville BJJ Florida · Gladiator Sports Fitness
MMA · Round 5 MMA · Armory Training Center · Hardkore MMA · Gracie JJ North Miami Beach ·
Gracie JJ Ocoee · Trident Jiu Jitsu · Team Gladiator MMA · GB Sebring · Full Circle MMA
NL: Labrador City BJJ (backlog item 7 — still unresolved)

High-confidence quick wins in that list: `Gracie Jiu-Jitsu Ocoee` (`graciejiujitsuocoee.com`
resolves, exact name match, JS-only) and `Gainesville BJJ Florida` (two live Gainesville academies
exist; a browser should settle which).

---

## What was written

| file | was | now | change |
|---|---|---|---|
| `snippets/tjjm-gym-websites-2.liquid` | 20,524 B | **20,922 B** | 17 in-place edits, 3 stale lines removed |
| `snippets/tjjm-gym-websites-3.liquid` | 826 B | **1,609 B** | 14 new entries appended |

Both MD5-verified against theme MM by the caller, not trusted from the write agent's report:
`0aa76fa96ca66c3cb8132dae24aa1585` / `6ee5c24d714e1386462eadc88300cab0`.

**The 17 were edited IN PLACE, not appended** — per the batch-7 rule. The three removed lines fix
the fragility flagged this session: `Stratford BJJ PEI` and `Team Fortitude NS` each had a stale
blank in websites-2 that was beaten by a real URL in websites-3 **only because file 3 renders
last**; plus one redundant duplicate blank for `Fighting Gravity Jiu Jitsu`. Override entries now
total 604 across the three files with **zero duplicate names**.

### Structural guarantee that counts did not move

Every count-bearing file in MM is byte-identical to LL — verified by checksum, not by sweep:
the legacy blob (`1ee054…`), all 45 data files, `tjjm-removed-index` (`c6069b…`),
`sections/tjjm-state-directory` (`633ec8…`), `tjjm-region-index` (`3df967…`),
`tjjm-gym-addresses` (`031ea9…`) and `tjjm-gym-websites` file 1 (`065db8…`).
Only the two override files differ. **5,219 published / 61 regions is therefore preserved by
construction**, which is a stronger claim than a count sweep and not subject to the sweep's own
known failure modes.

That websites-3 is genuinely rendered after websites-2 is proven on the *live* site today:
`Stratford BJJ PEI` currently renders its websites-3 URL over a websites-2 blank.

---

## Gates

`build_b9.py` (reusable) enforces and passed all of:

- **C3** no name in more than one override file, none twice in one file — and re-checked
  post-build across all 604 entries
- **C5** no name contains `|` or `~`
- **C9** `new_w != stored_w` — read from the raw corpus, not from a verdict file's `url` column,
  which is the batch-7 mistake this check exists to prevent
- **C9b** *(new)* `new_w != the current override value` — catches a no-op re-blank
- **C11** *(new)* every target name matches **exactly one** published record, so a
  name-alone override cannot hit two records
- **BYTES** both files asserted under the ~24,576 B Admin API ceiling before writing

Post-build the files were re-parsed and every published URL asserted present and correct.

---

## TO PUBLISH

**Publish MM `154892861612`.** LL `154883129516` becomes the rollback.

**No `metafieldsSet` is needed** — counts are unchanged, and the metafields were already
corrected earlier in this session to match 5,219.

After publishing, spot-check three or four of the 31 links render, ideally including one from
websites-2 (e.g. `Athens Jiu Jitsu`, AL) and one from websites-3 (e.g. `GB Davie`, FL), to
confirm both files are being read.
