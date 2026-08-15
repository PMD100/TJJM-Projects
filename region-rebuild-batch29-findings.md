# Batch 29 — the unvetted JSON feed is cut out of "Schools Near You"

Session of 15 Aug 2026. Built as theme **GGG** (`154955088044`), **staged and awaiting publish**.
**Publish GGG `154955088044`.** FFF `154954432684` becomes the rollback.

Background and evidence: `CRITICAL-second-directory-surface.md`.

---

## What changed — one file, one behaviour

| file | was | now |
|---|---|---|
| `sections/tjjm-gym-directory.liquid` | 10,708 B · `14bc0e0742efe13d4f274eafa51003ac` | **10,062 B · `8fc91b86e94d131408f4104c43662ae2`** |

Removed the `data-src` attribute and the `fetch()` block that pulled
`cdn.shopify.com/s/files/1/0633/1567/3260/files/tjjm-gyms.json` (487,965 B, 4,512 records) into
`/pages/jiu-jitsu-schools-near-you` on every page load. Replaced with an inline comment explaining
why, so it cannot be re-enabled by accident.

**Effect measured on the GGG preview:** `data-src` is `null`, no `fetch(src)` in the DOM, and the
card count falls from **4,493 → 50**, links from **4,149 → 46**.

### Verification — byte-exact, both directions
Reconstructed the edit locally from the FFF original and compared MD5s:

```
BEFORE local 10708  14bc0e0742efe13d4f274eafa51003ac  == theme FFF
AFTER  local 10062  8fc91b86e94d131408f4104c43662ae2  == theme GGG
```

Both files are archived in `build-b29/`.

### Structural guarantee
Every data, override and count-bearing file in GGG is byte-identical to FFF:
legacy blob `1ee054…`, removed-index `98ee61…`, region-index `8f4faa…`, state-directory `633ec8…`,
websites-1 `16a715…`, websites-2 `08c171…`, websites-3 `ab606f…`, addresses `031ea9…`.
**The 61 region pages and their 5,215 published records are untouched.**

---

## ⚠️ Two problems this exposed, both still open

### 1. The metaobject list only ever rendered 50 of its 282 records
`{% assign gyms = shop.metaobjects['gym_listing'].values %}` is **paginated by Shopify at 50**. The
count widget printed `{{ gyms.size }}` = 282, but the `{% for %}` loop only ever emitted 50 cards.
The JSON feed was masking this. With the feed gone the page shows **50 gyms across three states —
CO, MT and NV only**. The count widget now reads 50, so nothing on the page is untruthful, but the
page is badly degraded as a directory.

### 2. Those 50 metaobject records also bypass the override system
They read `gym.website.value` directly. **6 of the 50 carry links this programme deliberately
blanked:**

`Altitude MMA` · `Atos BJJ Lakewood` · `Atos Jiu Jitsu Reno` · `Avenge Jiu Jitsu` ·
`Battle Born MMA` · `Carbondale Training Center (Rising Crane)`

That is 6 bad links out of 46, down from ~4,149 unvetted. A 99% reduction in exposure, not a
complete fix.

---

## Recommended next step

**Point "Schools Near You" at the region index.** The 61 region pages are the audited surface and
already carry all 5,215 records with every override and suppression applied. This page's durable
value is the **Add Your Gym form** and the **state/province links**, both of which work today. The
50-gym metaobject list adds nothing the region pages don't do better, and carries 6 known-bad links.

Alternative, if the flat browsable list is wanted: regenerate `tjjm-gyms.json` from
`scratch/raw-corpus-LL.json` with suppressions and overrides applied, and re-upload it to Files.
That file must then also be snapshotted into the repo — it currently lives entirely outside version
control, which is how it went unnoticed for 28 batches.

---

## Programme totals

| | |
|---|---|
| links audited / screened (region pages) | 1,832 |
| harmful links removed | 192 |
| links restored | 190 |
| **unvetted links removed from Schools Near You** | **~4,149** |
