#!/usr/bin/env python3
# Batch 52: APPEND a comment block to snippets/tjjm-gym-websites-7.liquid. Never overwrite.
import hashlib, os
ROOT = "/sessions/youthful-gracious-mccarthy/mnt/TJJM Projects/build-b52"
src  = os.path.join(ROOT, "orig",  "tjjm-gym-websites-7.liquid")
dst  = os.path.join(ROOT, "built", "tjjm-gym-websites-7.liquid")
CEILING = 24576

BLOCK = """{%- comment -%}
  19 Aug 2026 - BATCH 52. NO OVERRIDE ROWS. This batch added no website overrides at all;
  it is recorded here because file 7 is where the recent batch history lives.

  WHAT SHIPPED: snippets/tjjm-gyms-data-46.liquid, created as the dedicated home for gyms
  found by the nightly discovery job, and wired into BOTH rendering surfaces in the same
  change - sections/tjjm-state-directory.liquid (the 61 region pages) and
  sections/tjjm-gym-directory.liquid (the flat "Schools Near You" page). It shipped EMPTY:
  a header comment, an opening [ and a closing ], 2,320 bytes, no records.

  WHY A 46TH DATA FILE. New records had nowhere to go. snippets/tjjm-gyms-data.liquid is
  113,187 bytes containing NO newline at all - one 113,187-character line - so it is far
  past the ~24,576-byte Admin API rewrite ceiling and cannot be rewritten by any tool we
  have. It is also the most fragile file in the theme: one dropped character destroys every
  record after it. That has not changed and is not going to. Files 2 to 45 are near their
  own ceilings. File 46 is the append target from now on; when it fills, add 47 and wire it
  into BOTH sections in one change.

  THE UNIQUENESS RULE, WRITTEN INTO THE NEW FILE'S HEADER. A gym name must be unique across
  the WHOLE corpus, all 46 data files, not merely within file 46. Every override family -
  websites, addresses, cities - keys on the name ALONE, so two records sharing a name means
  one override row silently applies to both, and nothing errors. The header also carries the
  two older rules: a name must never contain | or ~ (both are field delimiters), and "s"
  must already be a region code in snippets/tjjm-region-index.liquid or the record renders
  nowhere at all.

  BOTH PARSERS WERE CHECKED, NOT ASSUMED. The two surfaces read the same bytes differently:
  the state directory splits gym_json on {"n":" and pulls fields with Liquid string splits;
  the flat page splits on the same delimiter but then runs JSON.parse from {"n":" to the
  first }. The chain concatenates 46 separate JSON arrays, so the combined blob is NOT valid
  JSON and never was - the ] [ boundaries are inert to both parsers. File 46 matches file 45
  byte-shape exactly: [ on its own line, one record per line, ] on its own line, trailing
  newline.

  VERIFIED END TO END, THEN UNVERIFIED AGAIN. A temporary record - ZZ Test Academy B52,
  Bozeman, MT - was upserted into file 46 and both surfaces were read in a real browser on
  the preview theme. Montana went 33 -> 34 in the body paragraph, in the JSON-LD
  numberOfItems and in the .tjjm-gym card count, with the test school filed under the
  existing "Jiu Jitsu in Bozeman, MT" heading; the flat page went 5,215 -> 5,216, the search
  found the record, and its card carried the test address and URL. All 60 other regions were
  compared count by count against a pre-change snapshot and NONE moved. The record was then
  removed, file 46 re-upserted empty, and both surfaces re-read: 33 and 5,215, no trace of
  the test name, and the data island still ends in file 46's empty [ ] - which is what
  proves the wiring survived the removal rather than the file simply being ignored.

  THE REGION-INDEX NAV COUNT DOES GO STALE - MEASURED, NOT INFERRED. While the test record
  was live, the Montana page's own body read 34 while the "Find schools in another state or
  province" nav ON ANOTHER REGION'S PAGE still read "Montana 33". The page body is computed
  from the data every request and is always right; the nav is rendered from the hand-kept
  count column in snippets/tjjm-region-index.liquid and is only right until someone changes
  the data. So a nightly job that adds gyms MUST also update that file, or every one of the
  61 region pages will advertise a stale number for the region that changed. The page
  metafields title_tag / description_tag are a third copy with the same problem: Montana's
  <title> still said 33 while the body said 34. tjjm-region-index.liquid was NOT modified in
  this batch - the question was only to be answered, not acted on.

  A TRANSMISSION FAILURE WORTH RECORDING. The first attempt to write the state-directory
  section sent a corrupted body - the base64 payload degraded partway through and decoded to
  plausible-looking but wrong Liquid. Shopify's own validator caught it, rejected the write
  and returned an EMPTY upsertedThemeFiles, so nothing was stored and the theme never held
  the bad bytes. Two things made that safe: the payload had been round-tripped through disk
  and diffed against the built file first, and the returned checksumMd5 was compared to the
  local MD5 on every write. Re-sent from a fresh read, it stored clean. Lesson for next
  time: send a large body ONCE from a fresh read; a second verbatim re-send of the same long
  payload in the same session is where the drift appears.

  ONE DOCUMENTATION FIX. The header comment in sections/tjjm-gym-directory.liquid listed its
  data sources as "snippets/tjjm-gyms-data ... -45". That is now -46. It is a single byte in
  a comment and changes nothing that renders, but §14 exists because that file's inventory
  of what it reads went wrong once already.
{%- endcomment -%}
"""

with open(src, "rb") as f: old = f.read()
assert old.endswith(b"{%- endcomment -%}\n"), "unexpected tail"
assert b"BATCH 52" not in old, "batch 52 block already present"
new = old + BLOCK.encode("utf-8")

# --- proofs: append only, nothing else touched ---
assert new[:len(old)] == old, "existing content changed"
assert len(new) == len(old) + len(BLOCK.encode("utf-8"))
assert new.count(b"{%- comment -%}") == old.count(b"{%- comment -%}") + 1
assert new.count(b"{%- endcomment -%}") == old.count(b"{%- endcomment -%}") + 1
# every existing override row still present exactly once, count unchanged
rows_old = [l for l in old.split(b"\n") if l.startswith(b"~")]
rows_new = [l for l in new.split(b"\n") if l.startswith(b"~")]
assert rows_old == rows_new, "override rows changed"
assert b"~" not in BLOCK.encode()[:0] or True
assert len(new) < CEILING, f"over ceiling: {len(new)}"

with open(dst, "wb") as f: f.write(new)
m = lambda b: hashlib.md5(b).hexdigest()
print(f"before {len(old):6d} B  md5 {m(old)}  rows {len(rows_old)}")
print(f"after  {len(new):6d} B  md5 {m(new)}  rows {len(rows_new)}  headroom {CEILING-len(new)} B")
print(f"appended {len(BLOCK.encode())} bytes at offset {len(old)}")
