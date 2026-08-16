# Batch 34 — the write ceiling is gone. Override files 4, 5 and 6 wired into both sections.

Session of 15 Aug 2026. Built as theme **MMM** (`154960527532`), **staged and awaiting publish**.
**Publish MMM `154960527532`.** LLL `154960298156` becomes the rollback.

**Zero link changes in this batch.** It is purely structural: no record moved, no URL changed.

---

## The problem it fixes

The Admin API refuses a single-file rewrite above about **24,576 bytes**. That is a limit on *this
toolchain*, not on Shopify or on the theme — the theme happily carries a 113 KB data snippet and a
95 KB product section. But it meant every override batch had to fit inside one of three files, and
on 15 Aug all three filled up:

| file | headroom before |
|---|---|
| `tjjm-gym-websites.liquid` | 544 B |
| `tjjm-gym-websites-2.liquid` | 3,327 B |
| `tjjm-gym-websites-3.liquid` | 2,911 B |

Roughly one small batch left, and the browser queue alone is expected to produce ~90 rows.

## What was done

Three new empty override snippets, and **one** change to each of the two sections that read them —
so no future batch ever has to rewrite a section again.

| file | size | MD5 |
|---|---|---|
| `snippets/tjjm-gym-websites-4.liquid` | 982 B | `861ad36ab762ccc72ce1fd06c6e68808` |
| `snippets/tjjm-gym-websites-5.liquid` | 982 B | `1b5f77e1accd182174b814a4d804a5e7` |
| `snippets/tjjm-gym-websites-6.liquid` | 982 B | `372965fed2920e77f7c4c652630fba18` |
| `sections/tjjm-state-directory.liquid` | 12,906 → **13,014 B** | `c09c2d08b80534af171bb7281e4a88fe` |
| `sections/tjjm-gym-directory.liquid` | 17,139 → **17,247 B** | `197d9262e2f4b19999226b77c3f92567` |

Each section gained exactly the same 108 bytes:
`{%- render 'tjjm-gym-websites-4' -%}{%- render 'tjjm-gym-websites-5' -%}{%- render 'tjjm-gym-websites-6' -%}`
appended to its existing chain of override renders. Nothing else in either file changed.

**New headroom: ~70,700 bytes, roughly 1,900 more override rows.**

### The two sections were reconstructed and proved before being patched
`sections/tjjm-state-directory.liquid` had never been in the repo. It was rebuilt from the live
theme content, and the reconstruction was confirmed **byte-identical before any edit** —
12,906 B, MD5 `633ec853f548328e9c45e1cb78f69fd6`, matching the theme exactly. Only then was the
render chain extended. Both sections are now archived in `build-b34/`.

### Verified on the MMM preview
A missing snippet would throw a Liquid error onto all 62 directory pages, so both surfaces were
checked live:

**Alberta region page** — 72 cards, JSON-LD `numberOfItems` 72, body text "72 BJJ gyms and
academies across 20 cities", **no Liquid error**, links rendering normally.

**Schools Near You** — count widget 5,215, merge recomputed in the browser gives 5,215 records /
4,297 links / 1,004 override entries. **Identical to LLL in every number**, which is the point: a
structural change that moves nothing.

The three new snippets contain only Liquid comments, so they render to an empty string — confirmed
by the override blob on the page containing no trace of their text.

---

## Rule change for `RULES-tjjm.md`

**Fill file 4, then 5, then 6.** Gate C3 is unchanged and still absolute: a gym name may appear in
only one override file. Later files win on precedence, but that must never be relied on — if a name
already has a row, edit that row where it lives rather than shadowing it from a later file. A
duplicate lets a record silently fall back to a stale value, which is exactly the bug C3 exists to
prevent.

---

## Where the directory stands

| | |
|---|---|
| records published | **5,215** across 61 regions |
| with a link | **4,297** |
| deliberately link-free | 918 |
| links read or swept | 4,293 |
| harmful or broken links removed | 318 |
| links repointed to a correct URL | 207 |
| override capacity remaining | **~1,900 rows** |

## Next — section 2, the browser queue

**223 rows** in `scratch/hijack-screen/browser-queue-2026-08-15.tsv`: JavaScript-rendered,
Cloudflare-fronted and Facebook bot-walled pages that a fetch physically cannot read. Historically
about 40% convert to a verified good link, so this is worth roughly **90 recoveries** — the largest
remaining accuracy gain, and now there is room to write them all in one batch.

After that: the 162 social/aggregator links (`scratch/park-sweep/social-deferred.tsv`), the identity
pass, and the 918 link-free records.
