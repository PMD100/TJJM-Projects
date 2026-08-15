# Batch 11 — the browser-render pass. The 44 targets nothing else could reach.

Session of 13 Aug 2026. Built as theme **OO** (`154896597164`), **staged and awaiting publish**.
Overrides only. **Record counts cannot have moved.**

⚠️ **NN `154895384748` (batch 10) may still be unpublished.** OO is built on top of NN and contains
batch 10 as well. **Publishing OO alone is sufficient**; NN then becomes a rollback.

---

## Result

**44 targets · 18 confirmed · 2 rejected on independent recheck · 16 published.**

| verdict | n |
|---|---|
| CONFIRMED | 18 |
| UNRESOLVED | 15 |
| DEAD | 10 |
| NOT_BJJ | 1 |

**One recovery per 2.75 attempts**, in line with b9 (2.8) and b10 (2.6).
**Blank-rendering published records: 755 → 739.**

**11 of the 16 published links are Facebook or Instagram pages.** That is the whole point of this pass:
`web_fetch` cannot render Facebook or Instagram *at all*, so these records were unreachable by any
amount of HTTP fetching. They were not hard — they were invisible.

---

## ⚠️ THE FINDING THAT MATTERS — exact-name domains are often parked, and only a browser sees it

`graciejiujitsuocoee.com` was flagged in the batch-9 findings as a "high-confidence quick win":
live DNS, exact name match, empty body to a fetcher — the textbook signature of a JS-rendered site.
In a real browser it is a **GoDaddy "parked free" lander**. It is dead.

Seven more exact-name domains turned out to be parked or expired landers, invisible to every check
short of rendering:

- **GoDaddy landers:** `fabiopradobjj.com`, `rootsbjj.com`, `tridentbjj.com`, `midcitiesjiujitsu.com`
- **HugeDomains parking:** `trainerselite.com`, `storybjj.com`
- **Bluehost default page:** `southfljiujitsu.com`

**Corollary for future passes: a live A record plus an empty body plus an exact name match is NOT
evidence of a JS-rendered school site.** It is equally consistent with a parked domain. Only a
browser separates them — DNS cannot, and `web_fetch` cannot.

**Search indexes remain stale in the other direction too:** `checkmatfresno.com`,
`carlosmachadojiujitsumidcities.com`, `www.tridentjiujitsu.com` and `www.burns-bjj.com` all still
return live-looking search results and are NXDOMAIN in a real browser.

---

## Other findings

**A genuine rebrand, self-documented.** `paragonsimivalley.com`'s own About page says "Known then as
Watts Brazilian Jiu-Jitsu and Muay Thai Academy," at the same 4210 E Los Angeles Ave. Batch 10 had
this as a strong-but-uncorroborated lead from search summaries and correctly refused to publish it;
the browser settled it. **This is what the succession-vs-rebrand test looks like when it passes.**

**`Gracie Jiu-Jitsu North Miami Beach` is probably a duplicate of Valente Brothers** — same address,
16360 NE 26th Ave. Left UNRESOLVED rather than linked. Add to the duplicate-record queue.

**`round5mma.com` froze the Chrome renderer three times** across both schemes. Treat with suspicion.

**Four rows failed only on discipline, not identity** — b9-23, b9-37, b10-76, b10-132. The address
matched but no BJJ or grappling class was readable on the pages checked. A targeted schedule-page
check could still settle them; they are the cheapest remaining leads in this queue.

---

## The independent recheck — RUN, and it removed two

A second agent re-checked all 18 in a browser with instructions to falsify them. **No parked pages
and no wrong-entity matches**: 11 clean PASS, 7 PASS_WITH_CAVEAT, 0 hard failures. Two were pulled
anyway on judgement:

- **`Terra Leon Brazilian Jiu Jitsu`** — REMOVED. Its Instagram is genuinely its own, but has been
  **dormant since Oct 2019**, and **G-Team Grappling now occupies the same address with a Facebook
  page reading "Closed"**. Publishing a six-year-dead social profile for a school that appears gone
  is worse than no link. This is a succession, not a rebrand.
- **`Gladiator Sports Fitness MMA`** — REMOVED. Address and phone match Hialeah, but the class list
  is Judo, kickboxing, MMA and Muay Thai with **no BJJ**. Same call as `Paladin MMA` in batch 9.
  ⚠️ **The record itself is a not-BJJ suppression candidate** — flagged, not acted on.

Caveats recorded on the five that stayed:

- **`Gracie Jiu-Jitsu Whittier`** — the site publishes no address or phone, so identity was pinned
  *externally*: a Nextdoor page for the school at 6723 Comstock Ave, Whittier CA 90601 links this
  exact domain. Weaker than an on-page match; acceptable because it corroborates a domain↔address
  pairing rather than asserting an attribute.
- **`Watts BJJ` → `paragonsimivalley.com`** — the page self-declares the former name at the same
  address, but is now run by **Edgar Gallegos under Paragon**, not founder Dion Watts. Kept because
  the successor states the continuity itself.
- **`Merced Academy of Jiu Jitsu`** — Merced address confirmed (1725 G St Suite B) but the BJJ claim
  rests on the page name alone.
- **`Grady's MMA`** — city/ZIP only (Clearwater FL 33764); grappling, but no BJJ named specifically.
- **`Warriors Lair MMA`** — a personal-profile-style page with the address only in free-text bio.

⚠️ **One limitation the verifier disclosed honestly: Chrome was already signed into Facebook, so
logged-out visibility of the social links is untested.** If any of these pages are friends-only or
region-gated, a signed-out visitor may see nothing. Worth one signed-out spot-check.

---

## What was written

| file | was | now | change |
|---|---|---|---|
| `snippets/tjjm-gym-websites-2.liquid` | 21,480 B | **21,913 B** | 10 in-place edits |
| `snippets/tjjm-gym-websites-3.liquid` | 3,301 B | **3,698 B** | 6 new entries appended |

MD5-verified against theme OO by the caller, not trusted from the write agent:
`4d25aaaabb8bf8e2cb3cb00969936b59` / `f6577eb6b3b4c562d2ce21d26a7b2384`.
(websites-3 was rewritten after the recheck removed two entries; the earlier
`e0c5cc80…` / 3,856 B version is superseded and must not be used.)

Override entries now **639** across three files, **zero duplicate names**, 494 blank.

⚠️ **`tjjm-gym-websites-2` is at 21,913 B — about 2.7 KB from the ~24,576 B ceiling.** Only in-place
edits from here. New entries go in file 3 (3,856 B, plenty of room). When file 3 nears ~20 KB,
create `tjjm-gym-websites-4` and add it to the section's render chain.

### Structural guarantee that counts did not move
Every count-bearing file in OO is byte-identical to NN and MM — verified by checksum: legacy blob
`1ee054…`, `tjjm-removed-index` `c6069b…`, `sections/tjjm-state-directory` `633ec8…`,
`tjjm-region-index` `3df967…`, `tjjm-gym-addresses` `031ea9…`, `tjjm-gym-websites` file 1
`065db8…`. Only the two override files differ. **5,219 published / 61 regions preserved by
construction.**

---

## Method note — the browser tooling has a real bug

`get_page_text` frequently returns the **previous** page's content; its output carries a `URL:` line
that must be checked against the page you navigated to. Batching `navigate` and `get_page_text` for
the same page in one `browser_batch` call reliably reads the *previous* site, because the page has
not loaded yet. Working pattern: one batch per site of `[navigate, get_page_text, get_page_text]`,
then verify the `URL:` line before believing anything. **Record this in RULES — it silently produces
a confident verdict about the wrong website.**

---

## TO PUBLISH

**Publish OO `154896597164`.** It contains batch 10 AND batch 11; publishing it alone is sufficient.
NN `154895384748` then becomes the rollback, behind it MM `154892861612`.
No `metafieldsSet` needed — counts unchanged.

---

## Owed from this batch

1. **One signed-out spot-check of the 11 Facebook/Instagram links** — the recheck ran in a browser
   already logged into Facebook, so logged-out visibility is untested.
2. **The 15 UNRESOLVED and 10 DEAD** rows — the four discipline-only failures (b9-23, b9-37, b10-76,
   b10-132) are the cheapest leads left in this queue.
3. **`Gracie Jiu-Jitsu North Miami Beach` / Valente Brothers** duplicate — same address,
   16360 NE 26th Ave.
4. **`Gladiator Sports Fitness MMA`** — no BJJ on its own site. Not-BJJ suppression candidate.
5. The 30 unverified batch-10 targets (groups 9–10) still outstanding.
6. **Record the `get_page_text` staleness bug in `RULES-tjjm.md`** — it silently produces a
   confident verdict about the wrong website.
