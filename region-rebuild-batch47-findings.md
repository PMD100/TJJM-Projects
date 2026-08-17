# Batch 47 — 16 out, and the hidden-spam hunt came back empty. That is good news, with caveats.

Session of 16 Aug 2026. Built as theme **YYY2** (`154989691052`), **staged and awaiting publish**.
Overrides only. **Record counts cannot have moved.**
**Publish YYY2 `154989691052`.** XXX2 `154985070764` becomes the rollback.

---

## Removed — 16

7 DEAD, 3 PARKED, 3 STRIKING_ONLY, 3 WRONG_BUSINESS. All new rows in file 6.
**Verified: 1,256 override rows, 1,256 distinct names, zero duplicates.**

Notable: `New Braunfels BJJ` pointed at **Dalua**, an aquarium lighting and filtration store.
`Mobile MMA Club` redirects to a **population health conference**. `Method BJJ`, recorded in New
Jersey, is an **Edmonton, Alberta** school that closed in November 2025.

Two were deliberately left alone rather than removed: `North Legion Académie` (a members-only login
portal — unreadable, not proven bad) and `Athens Fitness and MMA` (the word "poker" appears in the
owner's bio prose, with no gambling links anywhere on the site).

---

## The hidden-spam screen: 200 links re-scanned, zero injections found

This was the priority I flagged last batch. `Kaiten Mixed Martial Arts` was the ninth case of a real
school's site carrying spam that reads **100% clean in rendered text** — hidden casino links in a
`visibility:hidden` block. Since every screen we have ever run reads rendered text, the concern was
that the eight found earlier were the visible minority of a much larger population.

**200 links that a previous pass had already marked OK were re-scanned in a browser using raw
`outerHTML` and computed styles. Zero injected sites.**

Every keyword hit was a false positive, and the generators are worth recording because they will
recur:

| pattern | source |
|---|---|
| `xxx` | `crypto.randomUUID()` templates — `"xxxxxxxx-xxxx-4xxx-yxxx"` |
| `slots` | Wix `slots=` attributes and `hiddenSlots`; "Time slots" in schedule markup |
| `cialis` | inside "spe**cialis**t" and French "spé**cialis**e-toi" |
| `xxxlarge` | GoDaddy `data-size` attributes |
| `judi`, `togel`, `xxx` | random substrings inside base64 image blobs |

### What this does and does not tell us
It says the injected-spam class is **rarer than feared** in the population we have already cleared —
the nine found were probably close to all of them, not the tip of an iceberg.

It does **not** rule out **user-agent cloaking**, where spam is served only to search-engine
crawlers and never to a browser. Ruling that out needs a fetcher that can set a Googlebot user
agent, which neither the sandbox nor `web_fetch` provides.

Seven rows came back UNREACHABLE and are genuinely unverified rather than clean.

---

## ⚠️ The browser profile is unreliable, and the failure is biased

Both screening agents independently reported that **roughly a third of navigations landed on a
different host than requested.** Every substituted page was a healthy grappling gym —
`mmabirmingham.com`, `abhaya.ca`, `absolutemma.com`, `murdocsbjj.com` and others. **Never once a
parked or hijacked domain.** The failure mode pushes results toward false clean.

Both agents caught it because the probe returns `location.hostname` from **inside the same JS
evaluation** as the scan, so a mismatch is always detectable. Mismatched reads were discarded and
re-navigated, some rows taking three or four attempts.

One agent traced the trigger: **the `setTimeout` sleep inside the probe opens the drift window.**
Reading synchronously right after `navigate` was materially more reliable.

**Both fixes are now mandatory for every browser pass:** return `location.hostname` from inside the
probe and discard mismatches, and avoid the sleep. This is written into the batch-47 comment block.

---

## Where the directory stands

| | |
|---|---|
| records published | **5,215** across 61 regions |
| with a link | **4,114** |
| deliberately link-free | 1,101 |
| override rows | 1,256, all distinct names |
| identity pass | **1,440 of 2,170 (66%)** |
| hidden-spam re-screen | 200 of 1,202 cleared links (17%) |

⚠️ Headroom: file 1 369 B, file 3 783 B, file 2 1,269 B, file 4 1,632 B, **file 6 7,350 B**.
File 6 will fill in roughly three more batches; then add file 7 and wire one `{%- render -%}` into
each of the two sections.

## Next

1. **Finish the identity pass** — 730 links never read, about 6 agent groups.
2. **Continue the hidden-spam re-screen** — 1,002 cleared links still unscanned. Lower priority now
   that the first 200 came back empty, but worth completing.
3. **Spot-check the ~50 OK verdicts from browser rounds 1–3**, which were taken before the hostname
   assertion existed and are therefore exposed to exactly the substitution bias described above.
4. **The city-correction pass** — six confirmed record errors, four high-confidence.
5. Re-check the 7 UNREACHABLE hidden-spam rows and the 7 from earlier rounds.
