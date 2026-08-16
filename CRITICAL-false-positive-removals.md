# We removed good links. 21 confirmed, 16% of the removals we tested. Plus a worse problem.

15 Aug 2026. **No theme change yet** — OOO `154963017900` is MAIN and correct as published.
The 18 outstanding restorations are specified below and ready to build.

---

## The audit

Every record blanked for a **dead-or-unreachable** reason was re-tested — 131 of them — resolving
**both** the apex and the `www.` form, then opening whatever resolved and reading the body.

| | tested | false positives | rate |
|---|---|---|---|
| DNS-failure blanks (first pass) | 34 | **8** | 24% |
| All other dead/unreachable blanks | 97 | **13** | 13% |
| **total** | **131** | **21** | **16%** |

**21 live schools had their working links removed by us.** Three were already fixed by the batch 33
and 36 recovery passes without our realising they were also false positives — `Thrive Jiu Jitsu`,
`UFC GYM Sunnyvale`, `Relson Gracie St. Augustine`. **18 are still blank and need restoring.**

### The 18 to restore

**In `tjjm-gym-websites.liquid` (file 1) — 7**

| record | restore to |
|---|---|
| `10th Planet Indianapolis at Circle City Martial Arts & Fitness` | `https://ccmaf.com/` |
| `Bay Jiu-Jitsu / BJJ Berkeley CA 94704` | `https://www.baycombat.com/` |
| `Highland Fight Systems` | `https://hfsmma.com/` |
| `Martial Arts America Russellville` | `https://www.russellvilletkd.com/` |
| `OC Carlson Gracie Jiu Jitsu` | `https://www.carlsongracieoc.com/` |
| `ONE HEART DOJO` | `https://www.eldoradomartialarts.com/` |
| `Port City Combat Sports` | `https://www.pckickboxing.com/` |

**In `tjjm-gym-websites-4.liquid` (file 4) — 11**

| record | restore to |
|---|---|
| `Campuzano Martial Arts` | `https://campuzanomartialarts.com/` |
| `Fusion MMA` | `http://fusionfitnessandmma.com/` |
| `Gracie Jiu Jitsu Houston` | `http://www.graciejiujitsuwesthouston.com` |
| `New Britain Judo and Dynamic Arts` | `https://newbritainjudo.org/` |
| `Pennsylvania Combat Sports` | `https://pacombatsports.com/` |
| `Renzo Gracie Pennsylvania` | `https://renzograciepa.com/` |
| `Station 6 Fitness and Martial Arts` | `https://www.station6fitness.com/` |
| `Syndicate Mixed Martial Arts` | `https://syndicatemmavegas.com/` |
| `Underdog Brazilian Jiu-Jitsu` | `https://underdogbjj.com/` |
| `Vital Force Muay Thai & MMA` | `http://www.vitalforcemma.com/` |
| `Yukon Martial Arts` | `https://www.yukonokmartialarts.com/` |

⚠️ Two need a second look before publishing. `Martial Arts America Russellville` resolves to a
**taekwondo** domain — confirm it teaches grappling or it is out of scope under §9.
`Port City Combat Sports` resolves to a Mobile AL address while the record says Fairhope; the
batch-36 recovery found `portcitycombatsports.com/port-city-combat-sports-fairhope/`, which matches
the city better and should probably win.

⚠️ File 1 has only **544 bytes** of headroom. Seven rows changing from `|~` to `|url~` costs about
245 B, so it fits, but the batch comment must be kept to two or three lines.

### Also recoverable, found during the sweep
`Behring Jiu Jitsu NY` — the old domain redirects to a 404, but the school is alive under a new name
at **`https://shinobimmany.com/`** (Shinobi Jiu Jitsu & MMA, 25519 NY-342, Evans Mills NY).

---

## The bigger problem: our fetcher has been serving stale cached pages

The agent running group 1 checked its own results against a real browser and found the workspace
fetcher **returned full, live-looking school content for six domains that a live Chrome load showed
were dead** — `atosorlando.com`, `davestrasser.com`, `dkjla.com`, `endurancebjj.com`,
`theboxingclub.net`, `capemartialarts.com` — and returned Japanese pharma spam for
`evolutionfightacademy.com`, which Chrome showed as a Wix placeholder.

We already knew the fetcher serves cached copies of **NXDOMAIN** domains — that is why every screen
does a DNS check first. This is worse: **it also serves stale copies of pages whose content has
changed.** That means a fetch-based verdict can be wrong in *either* direction:

- a dead site can read as alive → we keep a broken link
- a hijacked site can read as clean, or a clean site as hijacked → we blank or keep the wrong thing

**Any verdict in this programme that rests on a fetched page body, rather than a browser load, is
softer evidence than it looked.** The browser render pass in batch 35 is the only screen whose
content judgements came from a real browser.

This does not invalidate the removals — 445 links were removed and the confirmed error rate on the
subset most exposed to it is 16%. But it does mean the true rate across all removals is unknown,
and the honest position is that it is non-zero and worth measuring.

---

## Rules to add to `RULES-tjjm.md`

1. **Test both host forms.** A domain is only dead if BOTH `apex` and `www.` fail. One form failing
   proves nothing. (This alone caused 4 of the first 8 false positives.)
2. **A fetched page body is weak evidence.** The fetcher caches. Prefer a browser load for any
   verdict that removes or changes a link. Where a fetch is the only option, say so in the note.
3. **Measure the false-positive rate, not just the removal count.** Every screening batch should
   re-test a sample of its own removals.

## Next, in order

1. **Build the 18 restorations** — files 1 and 4, both already held locally in `build-b32/` and
   `build-b36/`. Resolve the two flagged records first.
2. **Apply the 34 pending batch-36 recoveries** — file 3's eighteen are already built and
   byte-verified at `build-b36/tjjm-gym-websites-3.liquid`; files 1 and 2 hold seven and nine.
   File 2 still has no local copy and must be pulled from the theme.
3. **Re-check the 5 UNSURE rows in a browser** — `casabjj.com`, `dcbmma.com`, `unitybjjnj.com`,
   `solismartialarts.com`, `bjjpeabody.com`. All resolve; bodies unreadable by fetch.
4. **Repoint `Behring Jiu Jitsu NY`** to `shinobimmany.com`.
5. Then resume recovery: 530 blanked records untouched, plus 275 that never had a URL.
