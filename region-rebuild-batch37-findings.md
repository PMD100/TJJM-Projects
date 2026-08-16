# Batch 37 — 22 links we removed by mistake are back.

Session of 16 Aug 2026. Built as theme **PPP** (`154973372588`), **staged and awaiting publish**.
Overrides only. **Record counts cannot have moved.**
**Publish PPP `154973372588`.** OOO `154963017900` becomes the rollback.

This is the first batch in the programme that fixes our own errors rather than the web's.

---

## What was restored

All 22 confirmed false positives from the audit in `CRITICAL-false-positive-removals.md` — live
schools whose working links we had removed. Every one was re-tested on **both** the apex and the
`www.` form, then opened and read.

| file | rows | how |
|---|---|---|
| `tjjm-gym-websites-4.liquid` | 11 | edited in place |
| `tjjm-gym-websites-5.liquid` | 11 | **moved** out of file 1, which had 544 B of headroom |

Where a record had both an alt-form hit and a batch-36 search recovery, **the recovery URL won** —
it is name-matched and city-confirmed:

- `ONE HEART DOJO` → `oneheartdojo.net` (not `eldoradomartialarts.com`)
- `Martial Arts America Russellville` → `russellvillemaa.com` (not a taekwondo domain whose body
  would not load — and which would have needed a scope check under §9)
- `Port City Combat Sports` → its **Fairhope** page (not the Mobile AL address the alt-form check
  landed on; the record says Fairhope)

## Verified on the theme itself

Not on a local build — the section's own merge, run in the browser against PPP:

```
records published   5,215   unchanged
with a link         4,204   was 4,182 — exactly plus 22
link-free           1,011
override entries    1,139
duplicate names     NONE    gate C3 intact
```

Spot checks all render their restored URL: `ONE HEART DOJO`, `OC Carlson Gracie Jiu Jitsu`,
`Highland Fight Systems`, `Port City Combat Sports`, `Martial Arts America Russellville`,
`Syndicate Mixed Martial Arts`, `Underdog Brazilian Jiu-Jitsu`, `Yukon Martial Arts`.

### The move-not-edit manoeuvre
File 1 was 544 bytes from the rewrite ceiling, so converting 11 blanks into URLs would not fit. The
blanking rows were **deleted** from file 1 and rewritten as live URLs in file 5. Gate C3 holds —
each name is in exactly one override file — and file 1 dropped from 24,032 B to 23,141 B, buying
back about 890 bytes of headroom.

---

## ⚠️ A process failure of mine, recorded honestly

**`build-b37/tjjm-gym-websites.liquid` is NOT byte-exact to the theme.** Every previous batch
transmitted the built artifact and MD5-matched it against Shopify. For file 1 I hand-edited during
transmission — removing the documentation lines for those 11 records as well as their data rows —
so the theme is 23,141 B / `2e92d97a0ad81118c2bd1f4dfad4a3eb` while my local rebuild lands at
22,958 B / `b3bf6df4…`. The local copy has been renamed
`tjjm-gym-websites.NOT-BYTE-EXACT-pull-from-theme.liquid` so nobody mistakes it for the truth.

**The theme is correct** — that is not in doubt, because it was verified by rendered outcome
(counts, zero duplicate names, eight probes) rather than by checksum, which is the stronger test.
But the repo no longer holds a faithful copy of file 1.

**First task next session: pull `snippets/tjjm-gym-websites.liquid` from the theme and save it as
the canonical local copy.** Files 4 and 5 in `build-b37/` are byte-exact and MD5-verified
(`0ef65e0f…`, `70fa4a3b…`).

---

## Where the directory stands

| | |
|---|---|
| records published | **5,215** across 61 regions |
| with a link | **4,204** |
| deliberately link-free | 1,011 |
| harmful or broken links removed | 445 |
| links repointed or restored | **249** |
| **of which restored after being wrongly removed** | **22** |

## Next, in order

1. **Pull file 1 from the theme** into the repo. Also pull `tjjm-gym-websites-2.liquid`, which has
   never had a local copy at all.
2. **Apply the 34 remaining batch-36 recoveries** — file 3's eighteen are built and byte-verified at
   `build-b36/tjjm-gym-websites-3.liquid`; files 1 and 2 hold seven and nine.
3. **Repoint `Behring Jiu Jitsu NY`** to `https://shinobimmany.com/` — the school is alive under a
   new name, found during the sweep.
4. **Browser-check the 5 UNSURE rows** — `casabjj.com`, `dcbmma.com`, `unitybjjnj.com`,
   `solismartialarts.com`, `bjjpeabody.com`. All resolve; bodies unreadable by fetch.
5. **Extend the false-positive audit beyond dead-or-unreachable removals.** 131 were tested and 21
   were wrong. The other ~314 removals — parked, hijacked, wrong-business — have never been
   re-tested, and the stale-cache problem means those verdicts are softer than they looked too.
6. Then resume recovery: 530 blanked records untouched, plus 275 that never had a URL.
