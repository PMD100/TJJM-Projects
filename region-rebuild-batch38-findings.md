# Batch 38 — 16 more of our own mistakes found, 25 links restored.

Session of 16 Aug 2026. Built as theme **QQQ** (`154974617772`), **staged and awaiting publish**.
Overrides only. **Record counts cannot have moved.**
**Publish QQQ `154974617772`.** PPP `154973372588` becomes the rollback.

---

## The audit that prompted this

212 removals that had **never been re-tested** — the parked, hijacked, dead and wrong-business
verdicts — were re-resolved on **both** host forms and, crucially, **re-read in a real Chrome
browser** rather than the fetcher.

| verdict | n |
|---|---|
| CONFIRMED — the removal was right | 188 |
| **FALSE_POSITIVE — a live school we un-linked** | **16** |
| CHANGED — still not the school, but different now | 8 |

**7.5% error rate.** Lower than the 16% on the DNS-failure subset, which makes sense: a content
judgement is more robust than a DNS one. But it is not zero, and these had never been checked.

### Across the whole audit programme
**37 of 343 removals re-tested have turned out to be wrong — 10.8%.**

### The 16
`Active Martial Arts` · `Black Flag Jiu-Jitsu Club` · `Cascade Jiu-Jitsu` ·
`Combat CFMA - Functional Martial Arts` · `Disciple MMA Academy` · `Elementum Jiu-jitsu` ·
`Gracie Jiu-Jitsu Altamonte Springs` · `Gracie Jiu-Jitsu Balance Academy` · `Hayastan MMA` ·
`Mid Shore Martial Arts` · `Miller's Martial Arts Academy` · `Odyssey MMA` ·
`School of Combat Arts` · `Team Reno` · `Ultimate MMA Training Center` ·
`Wolfpack Brazilian Jiu Jitsu - Martial Arts`

Three are worth calling out because they show the failure modes:

- **`Miller's Martial Arts Academy` and `Cascade Jiu-Jitsu`** were removed as HIJACK for carrying
  injected pharma spam. Both are the schools' own live sites and **the spam is gone.** A hijack
  verdict is a snapshot, not a permanent property.
- **`Odyssey MMA`** was removed as wrong-location — the note said "Odyssey MMA of South Amboy, NJ"
  as if that were a different school. The record says South Amboy NJ. It was always the right school.

### Eight CHANGED — and some got worse
`Torres MMA Sport` now serves fake "MacOS Security Center" scareware. `RYSE Academy` iframes a spam
site. `Risen Jiu-Jitsu` is now a "buy this domain" lander whose www redirects to survey spam. Three
KnuckleUp domains now throw Cloudflare 526. All stay removed — the point is that these pages keep
mutating, so a verdict has a shelf life.

---

## What was written

| file | was | now |
|---|---|---|
| `snippets/tjjm-gym-websites-6.liquid` | 982 B (empty) | **3,212 B · `4b5ae6150166c066773c237df527c581`** |

**25 rows**, byte-identical to `build-b38/`. Two workstreams combined so file 3 is touched once:

- **13 recoveries** carried from batch 36 (the 18 minus 3 that the browser audit also found and
  judged better)
- **10 false-positive restorations** from this batch, plus the 2 that resolved to file 3

Three records appeared in **both** workstreams with different URLs — `Black Flag Jiu-Jitsu Club`,
`Gracie Jiu-Jitsu Altamonte Springs`, `Elementum Jiu-jitsu`. **The browser-verified URL won** in
each case.

### Verified
```
records published   5,215   unchanged
with a link         4,229   was 4,204 — exactly plus 25
link-free             986
```

---

## ⚠️ Two outstanding hygiene items, both documented, neither affecting output

1. **25 shadowed duplicate names.** The 25 restored records still carry a blanking row in
   `tjjm-gym-websites-3.liquid`, shadowed by the live URL in file 6. Precedence is deterministic —
   file 6 renders last and wins in both sections — and the fail direction is safe (deleting the
   file-6 row makes the link vanish, it cannot resurrect a bad URL). But **gate C3 is violated until
   file 3 is rewritten.** The corrected file is built and byte-verified at
   `build-b38/tjjm-gym-websites-3.liquid` (21,444 B, `5f6c65eb7f1b44cb38740eab0330a636`) — it is a
   single upsert away, and it also buys file 3 back 221 bytes of headroom.

2. **`build-b37/tjjm-gym-websites.liquid` is still not byte-exact to the theme** (carried from
   batch 37). Pull `snippets/tjjm-gym-websites.liquid` from the theme into the repo.

---

## Where the directory stands

| | |
|---|---|
| records published | **5,215** across 61 regions |
| with a link | **4,229** |
| deliberately link-free | 986 |
| harmful or broken links removed | 445 |
| links repointed or restored | **274** |
| **of which restored after being wrongly removed** | **38** |
| removals re-tested | **343 of 445** |

## Next, in order

1. **Rewrite file 3** — built and verified, one upsert, clears the 25 duplicates.
2. **Pull files 1 and 2 into the repo.** File 2 has never had a local copy at all.
3. **Finish the removal audit** — about 102 removals still never re-tested.
4. **Apply the last batch-36 recoveries** — 6 in file 1, 9 in file 2.
5. **Then the big one: read the 1,994 live links whose pages have never been opened.** That is 47%
   of the directory and the single largest remaining gap in `AUDIT-COVERAGE-where-we-actually-are.md`.
