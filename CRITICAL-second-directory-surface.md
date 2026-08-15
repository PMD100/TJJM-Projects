# CRITICAL — a second directory surface has been carrying every link we removed

Found 15 Aug 2026, while chasing the Alberta discrepancy.
**Theme state: FFF `154954432684` is MAIN. Nothing has been changed. This is a report, not a fix.**

---

## The Alberta dispute is resolved. You were right; I was wrong.

Batch 26 reported "**0 of 72 Alberta links are dead**" and suggested your screenshots were a local DNS
problem. That conclusion was true **only of `/pages/bjj-schools-alberta`** — the region page. I never
checked the page you were actually on.

`101 Academy Jiu Jitsu → https://101academyjiujitsu.com` is live right now on
**`/pages/jiu-jitsu-schools-near-you`** — the "Schools Near You" item in your main nav. That is the
exact record and the exact dead domain in your screenshot.

**I retract the batch-26 Alberta finding.** The note in `region-rebuild-batch26-findings.md` saying
the report "was not reproduced" is wrong and should be read alongside this file.

---

## What the page actually is

`sections/tjjm-gym-directory.liquid` (10,708 B) renders **two** datasets:

| source | records | links | passes through our override system? |
|---|---|---|---|
| `shop.metaobjects['gym_listing']` (server-rendered) | 282 | most | **No** |
| `tjjm-gyms.json`, fetched by JS on page load | **4,512** | **4,166** | **No** |

Measured live in the browser: **4,493 gym cards, 4,149 outbound links.**

The JSON is not a theme asset. It is a **Shopify Files upload**, 487,965 bytes, created 13 Jul 2026:
`https://cdn.shopify.com/s/files/1/0633/1567/3260/files/tjjm-gyms.json`

Because it sits in Files, not in the theme, it is **outside version control, outside the theme
duplication workflow, and outside every gate we built.** Publishing a theme does not touch it.
Rolling back a theme does not touch it. All 28 batches were invisible to it.

### None of the three override layers apply

The section reads `gym.website.value` and `g.w` directly. It never renders
`tjjm-gym-websites`, `-2`, `-3`, or `tjjm-removed-index`. So:

- **585 links we deliberately blanked** — casinos, parked domains, dead registrations — still render here.
- **692 records we suppressed** still render here.
- **51 links we repointed** still render their old, wrong URL here.

Spot check, first 50 cards on the page: **6 of 50 (12%) are names we blanked** — Altitude MMA,
Atos BJJ Lakewood, Atos Jiu Jitsu Reno, Avenge Jiu Jitsu, Battle Born MMA, Carbondale Training
Center.

---

## The JSON is also a lower-quality dataset than our corpus

It has only four fields (`n, c, s, w`) — no address — and **at least 330 of its records follow a
`<city>bjj.com` naming pattern that looks machine-generated**, not curated:

`aberdeenbjj.com` · `airdriebjj.com` · `ajaxbjj.com` · `alamogordobjj.com` · `almabjj.com` ·
`amesbjj.com` · `banffbjj.com` · `barrebjj.com` · `barriebjj.com` · `brooksbjj.com` ·
`camrosebjj.com` · `cochranebjj.com` · `fortmcmurraybjj.com` · `lethbridgebjj.com` ·
`medicinehatbjj.com` · `reddeerbjj.com` · `scottsbluffbjj.com` …

DNS checks run today:

| domain | result |
|---|---|
| `airdriebjj.com` | **NXDOMAIN** |
| `banffbjj.com` | **NXDOMAIN** |
| `grandeprairebjj.com` (note the misspelling of Prairie) | **NXDOMAIN** |

Alberta has **22 records** on this page against 72 on the region page, and the two sets barely
overlap. Your "most of the AB gyms seem to do that" is consistent with what is here: of the 22 AB
rows, 12 are `<city>bjj.com` fabrications.

---

## Why this went unseen for 28 batches

Every verification I ran — count checksums, override gates, live-page fetches, the region screen —
targeted the 61 region pages. The structural guarantee I have reported every batch ("record counts
cannot have moved") is still true, and still says nothing about this page, because this page does
not read the theme data files at all.

The lesson for `RULES-tjjm.md`: **enumerate rendering surfaces before trusting a corpus-wide claim.**
A directory can have more than one front door.

---

## Options

**A — Cut the JS feed (one edit, reversible, removes ~4,149 unvetted links immediately).**
Delete the `data-src` fetch block from `sections/tjjm-gym-directory.liquid`. The page then shows only
the 282 metaobject gyms. Fastest way to stop the bleeding. Does not fix the 282.

**B — Regenerate `tjjm-gyms.json` from the curated corpus** with all suppressions and overrides
applied, and re-upload it to Files. Keeps the page useful. More work, and the file stays outside
version control unless we also snapshot it into the repo.

**C — Point "Schools Near You" at the region index** and retire this page's gym list entirely.
The 61 region pages are the audited surface; this page's real job is the "Add Your Gym" form and the
state links, both of which already work.

**D — Screen all 4,512 links** the way we have been screening. Months of work on a dataset that is
partly fabricated. Not recommended before A or C.

Separately, the **282 metaobject records need the same treatment** whichever option is chosen — they
bypass the overrides too.

My recommendation: **A now** (stops the harm today), then **B or C** as the permanent answer.
