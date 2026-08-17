#!/usr/bin/env python3
# batch 51 - append a record-only comment block to snippets/tjjm-gym-websites-7.liquid
# No override rows are added. Appends after the batch-49 and batch-50 blocks.
import hashlib, os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC  = os.path.join(BASE, 'orig',  'tjjm-gym-websites-7.liquid')
DST  = os.path.join(BASE, 'built', 'tjjm-gym-websites-7.liquid')

# Expected pre-state, carried forward from batch 50c. MUST be re-confirmed against the
# live API checksumMd5 before this is upserted - it has not been confirmed yet.
EXPECT_MD5  = 'c41ce0de2357284f77cc9844274600e2'
EXPECT_SIZE = 7018

src = open(SRC, 'rb').read().decode('utf-8')
got = hashlib.md5(src.encode()).hexdigest()
if got != EXPECT_MD5 or len(src.encode()) != EXPECT_SIZE:
    sys.exit('PRE-STATE DRIFT: %s / %d bytes (expected %s / %d). STOP.'
             % (got, len(src.encode()), EXPECT_MD5, EXPECT_SIZE))

# The file must end with the batch-50 block's closing tag; we append after it.
assert src.rstrip().endswith('{%- endcomment -%}'), 'file does not end on a comment block'
assert src.endswith('\n'), 'file does not end with a newline'
assert src.count('BATCH 49') >= 1 and src.count('BATCH 50') >= 1, 'batch 49/50 blocks missing'
before_blocks = src.count('{%- comment -%}')
before_rows   = sum(1 for L in src.split('\n') if L.startswith('~'))

BLOCK = """{%- comment -%}
  17 Aug 2026 - BATCH 51. CITY FILTER AND JUMP-NAV ON THE REGION PAGES. No override rows
  were added to this file this batch; this is a record entry only.

  1. WHAT CHANGED. sections/tjjm-state-directory.liquid only - the one file that renders all
  61 region pages. It gained, above the first city heading: a filter input that matches on
  city AND on gym name (case- and accent-insensitive substring, NFD with combining marks
  stripped), a live "Showing N of M" count, a clear button, and a "Browse by city" jump-nav
  grouped alphabetically inside a <details>. The <details> renders open when a region has
  24 or fewer cities and closed above that, so Texas does not open onto a wall of 134 links.
  13,339 -> 19,949 bytes, still under the 24,576-byte rewrite ceiling. No data snippet,
  no override file and no other section was touched.

  2. PAGINATION WAS EXPLICITLY REJECTED. Measured, not assumed: a Texas region page is
  524,096 bytes decoded and 75,207 bytes over the wire gzipped, and the gym records are only
  about 22 KB gzipped of that. The remaining ~53 KB is theme chrome and third-party script
  that pagination would not touch. Paginating or hiding gyms behind "Load More" would remove
  about 97% of the page's indexable content to save a few KB. It is a NAVIGATION problem,
  not a payload problem. Do not revisit this without new measurements.

  3. EVERY GYM STAYS IN THE DOM, ALWAYS. Filtering only toggles the `hidden` attribute on
  gym cards, on city headings and on the city's grid. Nothing is ever removed, detached or
  lazily built. Verified on the live preview: with the filter set to a string matching
  nothing, Texas still reports 351 .tjjm-gym nodes in the DOM and 351 in the JSON-LD.
  The jump-nav city links are rendered SERVER-SIDE in Liquid, so they are real anchors in
  the served HTML for crawlers, not built by JS.

  4. WORKS WITH JAVASCRIPT OFF. Only the filter chrome carries `hidden` in the served HTML;
  JS removes it on init. With JS off the label, input and count stay hidden, and every gym,
  every city heading and every jump link still render and still work - <details> and
  fragment anchors need no script. Confirmed against the RAW SERVED HTML (fetched, not the
  live DOM): Texas 351 cards / 134 headings / 134 jump links, Montana 33 / 16 / 16,
  Colorado 155 / 46 / 46. Jump links equal city headings exactly on all three.

  5. TWO CSS TRAPS FOUND THE HARD WAY, both now handled in the section's inline <style>.
     a) .tjjm-sec sets `overflow:hidden`, which makes it a scroll container and silently
        kills `position:sticky` on any descendant. The section now sets `overflow:clip`
        for itself only; clip clips identically but does NOT create a scroll container,
        so the sticky filter bar works. Verified sticky at scroll 1500/4000/9000.
     b) `[hidden]` from the UA stylesheet loses to `.tjjm-gyms{display:grid}`, so hiding a
        city grid needs an explicit rule. The section ships
        `section[data-tjjm-statedir] [hidden]{display:none!important}`.

  6. DO NOT ADD `html{scroll-behavior:smooth}`. It was in the first build of this batch and
  it BROKE the jump-nav completely - clicking a city link set the hash but the page never
  moved, at any distance, on every region page tested. Removing the rule fixed it instantly:
  a jump then lands the heading 84px from the viewport top, 19px clear of the 65px sticky
  bar, which is what `.tjjm-city-h{scroll-margin-top:84px}` is sized for. Jumps are now
  native and instant, which also makes prefers-reduced-motion a non-issue.

  7. THE PUBLISHED CITY COUNTS IN THE BRIEF WERE STALE. Texas is 134 city headings, not 135,
  and Montana is 16, not 17. This is not a regression: BATCH 50's city overrides merged the
  last gym out of two one-gym cities. Montana is the clear case - ~Whitefish BJJ|Columbia
  Falls~ emptied Whitefish, and Whitefish is gone from the heading list while Columbia Falls
  remains. The gym counts themselves are unchanged (351 / 33 / 155) and the body paragraph,
  the .tjjm-gym card count and the JSON-LD numberOfItems still agree on every page.

  8. PRE-EXISTING BUG FOUND, NOT FIXED, NOT CAUSED BY THIS BATCH. assets/tjjm-core.css sets
  `.tjjm-reveal{opacity:0}` and expects a `.tjjm-in` class to reveal it. NOTHING ANYWHERE
  ADDS `.tjjm-in` - not an inline script, and not any of the 23 same-origin script files,
  all scanned. So on the LIVE theme, every region page renders its <header> (which holds the
  H1) and all of its gym grids at opacity 0 for any visitor who does not have
  prefers-reduced-motion: reduce set; that media query is the only rule that restores them.
  The markup is all present, so crawlers are unaffected, but most humans see an empty page.
  This predates batch 51 and is out of its scope. It needs its own batch.
{%- endcomment -%}
"""

out = src + BLOCK
data = out.encode('utf-8')

assert out.startswith(src), 'append-only violated'
assert out.count('{%- comment -%}') == before_blocks + 1, 'comment block count wrong'
assert sum(1 for L in out.split('\n') if L.startswith('~')) == before_rows, 'override rows changed'
assert 'BATCH 49' in out and 'BATCH 50' in out and 'BATCH 51' in out, 'a batch block went missing'
assert len(data) < 24576, 'OVER CEILING: %d' % len(data)

print('pre-state  : %d bytes  %s  (blocks=%d, override rows=%d)'
      % (len(src.encode()), got, before_blocks, before_rows))
print('post-state : %d bytes  %s  (blocks=%d, override rows=%d)'
      % (len(data), hashlib.md5(data).hexdigest(), out.count('{%- comment -%}'), before_rows))
print('delta      : %+d bytes' % (len(data)-len(src.encode())))
print('headroom   : %d bytes under 24576' % (24576-len(data)))
open(DST, 'wb').write(data)
print('wrote %s' % DST)
