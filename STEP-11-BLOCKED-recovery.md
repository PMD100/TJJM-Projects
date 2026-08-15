# Step 11 — STAGED UPLOAD SUCCEEDED, `fileUpdate` BLOCKED. Recovery state.

Written 6 Aug 2026 ~03:35Z. **Nothing is half-applied.** The live file is untouched:
`tjjm-gyms.json`, `originalFileSize` **487,965**, `updatedAt` 2026-08-05T20:58:54Z, status READY.
The store is exactly as it was before step 11 began.

## What completed

| stage | result |
|---|---|
| merged artifact built in-browser | **503,127 B, 4,630 records, 61 regions, NY 182** |
| non-NY remainder byte-identical to the current file | **yes — 4,448 records untouched** |
| file ↔ theme cross-check | 182 names, **sets identical**, 0 duplicates |
| `stagedUploadsCreate` | OK, `userErrors: []` |
| policy decoded and asserted in-page | key, date, bucket, content-type all cross-check |
| **POST to Google Cloud Storage** | **HTTP 201 Created** — the file IS uploaded |
| `fileUpdate` | **BLOCKED by the permission classifier, twice** |

## The blocker

`fileUpdate` was denied by the classifier on two consecutive attempts with no change in approach.
Per RULES §7 this is **situational, not a standing restriction** — it was blocked once on 5 Aug and
succeeded cleanly on the next run, and succeeded again on 6 Aug. The brief's instruction was to
report a block rather than work around it, so no workaround was attempted.

## Recovery — the staged file is already uploaded and valid for 24h

**`resourceUrl` (expires 2026-08-07T03:33:35Z):**

```
https://shopify-staged-uploads.storage.googleapis.com/tmp/63315673260/files/195b5e93-ca20-4035-817c-20ba74077c92/tjjm-gyms.json
```

Also stashed in the working browser tab at `sessionStorage.getItem('tjjm_resourceUrl')`.

**The exact mutation to re-run — nothing else needs redoing if this succeeds:**

```graphql
mutation Upd($files: [FileUpdateInput!]!) {
  fileUpdate(files: $files) {
    files { id fileStatus ... on GenericFile { url originalFileSize } }
    userErrors { field message code }
  }
}
```
```json
{"files":[{"id":"gid://shopify/GenericFile/33943277338796",
  "originalSource":"https://shopify-staged-uploads.storage.googleapis.com/tmp/63315673260/files/195b5e93-ca20-4035-817c-20ba74077c92/tjjm-gyms.json"}]}
```

⚠️ **`fileUpdate`'s immediate response reports the OLD `originalFileSize`.** Ignore it and re-query.

**Verification after it lands** — re-query `files(query:"filename:tjjm-gyms.json")` until
`fileStatus: READY`, then assert `originalFileSize` = **503,127**, and fetch the new `?v=` URL and
assert 4,630 records / 61 regions / NY 182.

## If the 24h window lapses

The staged upload expires 2026-08-07T03:33:35Z. After that the merge must be rebuilt — about ten
minutes of work, and **fully reproducible** from files in this folder:

1. Fetch the current `tjjm-gyms.json` **in the browser** (the sandbox has no network and the
   fetch tool truncates it at ~75 KB of 488 KB).
2. Confirm `JSON.stringify(parsed) === raw` — the file is exactly compact JSON with literal
   non-ASCII, so it round-trips byte-for-byte. This is what makes the merge predictable.
3. Delete the 12 names in `step7-tjjm-removed-index-APPEND.txt` (region NY only).
4. Apply the 15 overrides in `step7-tjjm-gym-websites-APPEND.txt` to the surviving NY records.
5. Append all 130 records from `scratch/ny-imports-compact.json`
   (SHA-256 `ad2672c98caec110bec9d46b41fbf423f3e6ca83b6b717443ee7ef91a19005b9`, 16,270 B).
6. Assert the non-NY remainder is byte-identical, then `JSON.stringify` and re-upload.

**Do NOT try to reproduce the file's record ORDER.** It has 1,055 name-order breaks and regions are
not contiguous, so the generation order is not recoverable. The surgical delete/patch/append above
is deliberate: it cannot silently rewrite the other 4,448 records, which is exactly the failure the
old rebuild-from-rendered-JSON-LD method produced (1,076 records rewritten when 13 were intended).

## Alternative route if `fileUpdate` stays blocked

The merged content is in the working tab at `window.__MERGED`. It can be downloaded to disk from
the browser and then uploaded through **Shopify admin → Settings → Files**, replacing
`tjjm-gyms.json` by hand. That needs no API permission at all. Ask before triggering the download —
it is a file write to the machine.

## Consistency state right now

| layer | NY count | agrees? |
|---|---|---|
| theme ZZ `154665025708` (unpublished) | 182 | built + swept |
| theme MAIN/YY `154658242732` (LIVE) | 64 | untouched |
| page metafields (LIVE, global) | **182** | **ahead of the live page** |
| `tjjm-gyms.json` | 64 | **behind ZZ** |

Two open windows, both closing on publish + this fileUpdate. Neither is load-bearing for the site's
rendering — nothing is known to consume `tjjm-gyms.json` — but the metafield window is user-visible
in search results and its rollback strings are in `ny-step5-verdicts.md`.
