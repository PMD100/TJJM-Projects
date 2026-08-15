# Batch 10 — URL repointing pass, California + Texas.

Session of 13 Aug 2026. Built as theme **NN** (`154895384748`), **staged and awaiting publish**.
Overrides only — no record added, removed, renamed or re-citied. **Record counts cannot have moved.**

---

## Result

**150 targets planned · 120 verified · 50 confirmed · 47 published.**

| verdict | n | share of 120 |
|---|---|---|
| CONFIRMED | 50 | 42% |
| NEEDS_BROWSER | 26 | 22% |
| DEAD | 22 | 18% |
| UNRESOLVED | 13 | 11% |
| WRONG_ENTITY | 7 | 6% |
| NOT_BJJ | 2 | 2% |

**One recovery per 2.6 attempts** — slightly better than batch 9's 2.8.
**Blank-rendering published records: 802 → 755.**

**30 targets were never verified.** `WebSearch` hit its 200-call session budget partway through,
which also degraded part of group 8 (ids 108, 118, 138 and possibly 58, 68, 148 would likely
resolve with a working search tool). Groups 9 and 10 were not dispatched rather than run
handicapped. Carried forward: ids 9, 10, 19, 20, 29, 30, 39, 40, 49, 50, 59, 60, 69, 70, 79, 80,
89, 90, 99, 100, 109, 110, 119, 120, 129, 130, 139, 140, 149, 150 in
`scratch/repoint-b10/tranche.tsv`.

### Three confirms dropped on independent re-check
- **`Hayward BJJ Darcio Lira`** — FAIL_BODY. The proposed site is Ta Danado Jiu Jitsu under
  Carlos Rocha. The original agent reported the About page named Darcio Lira as Rocha's professor;
  the verifier found no mention of Darcio Lira on the home or instructors pages. **Conflicting
  evidence between two agents on a lineage claim is exactly the fabrication risk this project has
  been bitten by — dropped rather than published.**
- **`Gracie Jiu-Jitsu Vallejo`** — no street address and no phone published anywhere on the site;
  contact routes to Miro's Taekwondo. Identity not establishable.
- **`Gracie Jiu-Jitsu Adkins`** — no address or phone renders, schedule defaults to a 2025 week,
  and the original pass flagged the school as possibly closed.

---

## ⚠️ NEW AND CONFIRMED TRAPS

**Every stored URL tested was dead. 100%, across all eight sub-batches.** Batch 9 saw the same.
Two new death modes beyond NXDOMAIN: **nameservers returning REFUSED** (lame delegation), and
**registered on live nameservers but publishing no A/AAAA record at apex or www** — four cases.
Both look like a working domain to any check short of a real DNS query.

**⚠️ Same-name-different-school is now the dominant false positive — ten cases.** The name-matching
domain belongs to an entirely different school:
- `chriscollinsacademy.com` — a jiu-jitsu academy in **Hong Kong**, surfaced for a Hurst, TX record
- `pinnaclebjj.com` — 301s to **Phoenix, Arizona** for a Redlands, California record
- `nextgenerationmma.com` — a **Frisco, TX** school for a Sacramento, CA record
- `mercedjiujitsu.com` — a *different Merced academy three streets away* from the record's address

**The name alone is never sufficient. Match the street address or the phone.** This is the
practical, testable form of RULES §4's "never judge a link from a normalised domain".

**⚠️ Succession is not rebrand — six cases.** A *different* academy took over the same unit under a
different lineage or affiliation: 320 Alisal Rd Solvang (now Allegiant, no GB affiliation),
32355 Yucaipa Blvd (now Alliance, founded 2022, not Caveirinha), 320 Industrial Blvd McKinney
(now 3 Embers, an Alex Martins affiliate, not Combat Base). **A matching address is not enough —
require the same head instructor or the same lineage.** Genuine rebrands confirmed this way:
Rodrigo Cardoso → Atlas BJJ, Brazilian Fight Factory → Fight Factory Jiu-Jitsu (its own footer
still links the old Facebook page), Austin Fitness Martial Arts → The Void (phone 512-707-8977 on
both).

**⚠️ A live domain can be hijacked outright.** `appliedmma.com` now serves a Chinese
streaming/piracy site. It resolves, returns 200, and must never be published.

**⚠️ Agency spec-builds masquerade as school sites.** `team-mata-mma.vercel.app` renders a complete,
address- and phone-accurate site — but it is a free vercel.app deploy footed "Designed by
Vonroflo.com", with placeholder trainer names, a dummy map embed, stale 2025 events, and an
asserted lineage (Wander Braga via Pete Han) corroborated nowhere. Correctly left UNRESOLVED.

**Search summaries asserted 30+ dead domains as live**, several with fabricated program lists and
trial offers attached — including HugeDomains parking pages described as having "30 days free
trial". The MatMade boilerplate ("passionate about Brazilian Jiu-Jitsu… strong fundamentals,
technical precision, and a supportive training culture") appeared verbatim again.

**A whole hosting platform is opaque to `web_fetch`.** `rootsbjj.com`, `checkmatallen.com`,
`midcitiesjiujitsu.com` and `stocktonbjj.com` all resolve, serve a `robots.txt` carrying an
`LLM-Policy` line and a gzipped sitemap, and return empty JS-only bodies. Live but unverifiable
without a browser. That platform accounts for a meaningful share of the 26 NEEDS_BROWSER rows.

---

## ⚠️ TWO DUPLICATE-RECORD PAIRS — both in Austin, both high confidence

Two pairs of records resolved to the same school:

| | record A | record B |
|---|---|---|
| `thevoidmartialarts.com` | `Austin Fitness Martial Arts` | **`Austin Fitness Martial Arts - Now is THE VOID MArtial Arts`** |
| `fightfactoryjiujitsu.com` | `Fight Factory Austin` | `Brazilian Fight Factory` |

The first is unambiguous: **a curator's note has been baked into a record name**, typo and all
("MArtial"). These are two rows for one school. Both were published — the link is correct for
both, and they already both render — but **this is a suppress-one job for the next corpus batch**,
and it suggests searching the corpus for other names containing "now is", "formerly", "moved" or
similar editorial fragments.

---

## City and naming defects found — feeding the gazetteer scan

Adjacent-municipality or outright-wrong city, confirmed against the school's own address:
**GB La Crescenta** → La Cañada Flintridge · **ASG Riverside** → Moreno Valley ·
**Gracie Santa Cruz** → Capitola · **GB Austin (Dripping Springs)** → Dripping Springs ·
**GB Westlake** → West Lake Hills · **The Void** → relocated within Austin to 701 Tillery St.

Naming/affiliation defects: **`Gracie Jiu-Jitsu Highland Village`** is a **Gracie Barra** school,
not a Gracie University CTC — address and phone match, the affiliation in the record name does
not. **`Spartan Fit MMA`** now trades as Spartan Grappling Academy and lists no MMA.

Added to batch 9's seven, backlog item 4's gazetteer scan now has **13+ seed cases**.

---

## What was written

| file | was | now | change |
|---|---|---|---|
| `snippets/tjjm-gym-websites-2.liquid` | 20,922 B | **21,480 B** | 18 in-place edits |
| `snippets/tjjm-gym-websites-3.liquid` | 1,609 B | **3,301 B** | 29 new entries appended |

MD5-verified against theme NN by the caller, not trusted from the write agent:
`17fce91d3e6da1ef4bb9ca7b19158ffe` / `66cd0d324dc8afdc5c157fd66ba4e910`.

Override entries now **633** across three files, **zero duplicate names**, 504 blank.

⚠️ **`tjjm-gym-websites-2` is at 21,480 B — roughly 3.1 KB from the ~24,576 B ceiling. Do not add
new entries to it; in-place edits of existing entries are still fine.** `websites-3` is at 3,301 B
with plenty of room.

### Structural guarantee that counts did not move
Every count-bearing file in NN is byte-identical to MM — verified by checksum: the legacy blob
(`1ee054…`), data-45 (`8fb61a…`), `tjjm-removed-index` (`c6069b…`),
`sections/tjjm-state-directory` (`633ec8…`), `tjjm-region-index` (`3df967…`),
`tjjm-gym-addresses` (`031ea9…`), `tjjm-gym-websites` file 1 (`065db8…`). Only the two override
files differ. **5,219 published / 61 regions is preserved by construction.**

---

## Gates

`build_b10.py` — same reusable gate as batch 9. All passed: **C3** (no name in more than one file,
none twice, re-checked post-build across all 633 entries), **C5** (no `|` or `~` in a name),
**C9** (`new_w != stored_w`, read from the raw corpus), **C9b** (`new_w != current override`),
**C11** (every target name matches exactly one published record), **BYTES** (both files under
ceiling). Post-build the files were re-parsed and every URL asserted present and correct.

---

## TO PUBLISH

**Publish NN `154895384748`.** MM `154892861612` becomes the rollback.
No `metafieldsSet` needed — counts unchanged.

After publishing, spot-check one link from each file, e.g. `GB Agoura Hills` (CA) and
`Fight Factory Austin` (TX).

---

## Owed from this batch

1. **The 30 unverified targets** (groups 9–10) plus the search-degraded rows in group 8.
2. **26 NEEDS_BROWSER rows** — add to batch 9's 18. **44 browser-only targets now queued**, several
   on the JS-only platform described above.
3. **The two Austin duplicate-record pairs** — suppress one of each.
4. **`Team Mata`** — decide whether an agency spec-build on a free host counts as a school site.
5. Sweep the corpus for record names containing editorial fragments like "now is" or "formerly".
