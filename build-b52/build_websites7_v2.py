#!/usr/bin/env python3
# batch 51/52 - append a record-only comment block to snippets/tjjm-gym-websites-7.liquid
#
# This supersedes build-b51/scripts/build_websites7.py. That script's block asserted two
# things that were empirically DISPROVED before it was ever upserted (its items 6 and 8).
# The block below keeps every claim that was re-verified and corrects the two that were not.
# No override rows are added. Append-only.
import hashlib, os, sys

BASE = os.path.dirname(os.path.abspath(__file__))
SRC  = os.path.join(os.path.dirname(BASE), 'build-b51', 'orig',  'tjjm-gym-websites-7.liquid')
DST  = os.path.join(BASE, 'tjjm-gym-websites-7.liquid')

# Pre-state, RE-CONFIRMED against the live AD3 API on 19 Aug 2026:
# size 7018, checksumMd5 c41ce0de2357284f77cc9844274600e2. No drift.
EXPECT_MD5  = 'c41ce0de2357284f77cc9844274600e2'
EXPECT_SIZE = 7018

src = open(SRC, 'rb').read().decode('utf-8')
got = hashlib.md5(src.encode()).hexdigest()
if got != EXPECT_MD5 or len(src.encode()) != EXPECT_SIZE:
    sys.exit('PRE-STATE DRIFT: %s / %d bytes (expected %s / %d). STOP.'
             % (got, len(src.encode()), EXPECT_MD5, EXPECT_SIZE))

assert src.rstrip().endswith('{%- endcomment -%}'), 'file does not end on a comment block'
assert src.endswith('\n'), 'file does not end with a newline'
assert src.count('BATCH 49') >= 1 and src.count('BATCH 50') >= 1, 'batch 49/50 blocks missing'
before_blocks = src.count('{%- comment -%}')
before_rows   = sum(1 for L in src.split('\n') if L.startswith('~'))

BLOCK = """{%- comment -%}
  17-19 Aug 2026 - BATCH 51. CITY FILTER AND JUMP-NAV ON THE REGION PAGES. No override rows
  were added to this file this batch; this is a record entry only.

  1. WHAT CHANGED. sections/tjjm-state-directory.liquid only - the one file that renders all
  61 region pages. It gained, above the first city heading: a filter input that matches on
  city AND on gym name (case- and accent-insensitive substring, NFD with combining marks
  stripped), a live "Showing N of M" count, a clear button, and a "Browse by city" jump-nav
  grouped alphabetically inside a <details>. The <details> renders open when a region has
  24 or fewer cities and closed above that, so Texas does not open onto a wall of 134 links.
  It also now loads assets/tjjm-core.js - see item 8. 13,339 -> 20,062 bytes, still under
  the 24,576-byte rewrite ceiling. No data snippet, no override file, no shared asset and
  no other section was touched.

  2. PAGINATION WAS EXPLICITLY REJECTED. Measured, not assumed: a Texas region page is
  524,096 bytes decoded and 75,207 bytes over the wire gzipped, and the gym records are only
  about 22 KB gzipped of that. The remaining ~53 KB is theme chrome and third-party script
  that pagination would not touch. Paginating or hiding gyms behind "Load More" would remove
  about 97% of the page's indexable content to save a few KB. It is a NAVIGATION problem,
  not a payload problem. Do not revisit this without new measurements.

  3. EVERY GYM STAYS IN THE DOM, ALWAYS. Filtering only toggles the `hidden` attribute on
  gym cards, on city headings and on the city's grid. Nothing is ever removed, detached or
  lazily built. Re-verified on the AD3 preview in every filter state INCLUDING a zero-match
  string: Texas holds 351 .tjjm-gym nodes, Montana 33, Colorado 155, unchanged throughout.
  The jump-nav city links are rendered SERVER-SIDE in Liquid, so they are real anchors in
  the served HTML for crawlers, not built by JS.

  4. WORKS WITH JAVASCRIPT OFF. Only the filter chrome carries `hidden` in the served HTML;
  JS removes it on init. Confirmed against the RAW SERVED HTML (fetched, not the live DOM):
  Texas 351 cards / 134 headings / 134 jump links, Montana 33 / 16 / 16, Colorado 155 / 46 /
  46. Jump links equal city headings exactly on all three. The section also ships
  `html.no-js .tjjm-reveal{opacity:1;transform:none}` so that with scripting off the reveal
  animation can never leave content permanently invisible.

  5. TWO CSS TRAPS FOUND THE HARD WAY, both handled in the section's inline <style>.
     a) .tjjm-sec sets `overflow:hidden`, which makes it a scroll container and silently
        kills `position:sticky` on any descendant. The section now sets `overflow:clip`
        for itself only; clip clips identically but does NOT create a scroll container,
        so the sticky filter bar works. Re-verified: the bar stays pinned with its bottom
        edge at 65px while scrolled deep into Texas, Montana and Colorado.
     b) `[hidden]` from the UA stylesheet loses to `.tjjm-gyms{display:grid}`, so hiding a
        city grid needs an explicit rule. The section ships
        `section[data-tjjm-statedir] [hidden]{display:none!important}`.

  6. CORRECTION - THE SMOOTH-SCROLL VERDICT IN THE BATCH-51 DRAFT WAS WRONG. That draft
  said `html{scroll-behavior:smooth}` "BROKE the jump-nav completely - the page never
  moved". That is not what was happening. Two measurement traps produced that symptom and
  neither had anything to do with scroll-behavior:
     a) A KLAVIYO POPUP. When its signup modal is up it puts `klaviyo-prevent-body-scrolling`
        on <body>, and its stylesheet sets `body.klaviyo-prevent-body-scrolling
        {overflow:hidden!important}`. <html> is `overflow:visible`, so the body value
        propagates to the viewport and the document stops scrolling. Removing that one class
        restored scrolling instantly (scrollY 0 -> 600). The popup is intermittent and
        site-wide; it is NOT ours and it is not caused by this section.
     b) READING scrollY SYNCHRONOUSLY AFTER window.scrollTo. Under smooth scrolling the
        scroll is animated, so scrollY is still 0 on the next line. That alone looks like
        "the page never moved".
  The rule was still removed, on its own merits: a section has no business setting a global
  `html` behaviour for every page on the store, and instant jumps are more predictable on a
  page as tall as Texas. Jumps now land the heading 84px from the viewport top, 19px clear
  of the 65px sticky bar, which is what `.tjjm-city-h{scroll-margin-top:84px}` is sized for.
  Verified on Montana (#bozeman), Texas (#austin) and Colorado (#denver): heading top 84px,
  sticky bottom 65px, not obscured, on all three.

  7. THE PUBLISHED CITY COUNTS IN THE BRIEF WERE STALE. Texas is 134 city headings, not 135,
  and Montana is 16, not 17. This is not a regression: BATCH 50's city overrides merged the
  last gym out of two one-gym cities. Montana is the clear case - ~Whitefish BJJ|Columbia
  Falls~ emptied Whitefish, and Whitefish is gone from the heading list while Columbia Falls
  remains. The gym counts themselves are unchanged (351 / 33 / 155) and the body paragraph,
  the .tjjm-gym card count and the JSON-LD numberOfItems still agree on every page.

  8. CORRECTION - THE ".tjjm-in" BUG, ITS REAL CAUSE, AND ITS FIX. The batch-51 draft said
  "NOTHING ANYWHERE ADDS `.tjjm-in` - not an inline script, and not any of the 23 same-origin
  script files, all scanned." THAT IS FALSE. assets/tjjm-core.js (698 bytes) is exactly the
  file that adds it: an IntersectionObserver at {threshold:.12} over `.tjjm-reveal:not(
  .tjjm-in)`, plus a prefers-reduced-motion fast path that adds the class outright.
  The real defect was narrower and this batch fixes it: sections/tjjm-gym-directory.liquid
  loads that asset, and sections/tjjm-state-directory.liquid NEVER DID - it only ever loaded
  tjjm-core.css. So the 61 region pages shipped the rule that hides `.tjjm-reveal` without
  the script that reveals it, and every region <header> and every city grid sat at opacity 0.
  The section now emits, right under the stylesheet tag:
      <script src="{{ 'tjjm-core.js' | asset_url }}" defer></script>
  mirroring tjjm-gym-directory.liquid. tjjm-core.js and tjjm-core.css were NOT modified -
  they are shared by every page on the store. Verified after the fix: Montana 17 of 17
  reveal elements reach `.tjjm-in` and computed opacity 1 by scrolling the page normally,
  Texas 135 of 135, Colorado 47 of 47. No console errors on load or during filtering.

  9. A THIRD MEASUREMENT TRAP, for whoever debugs this next. INTERSECTIONOBSERVER DOES NOT
  FIRE IN A TAB THAT IS NOT BEING RENDERED. A backgrounded or occluded tab produces no
  animation frames, so the observer never runs, no `.tjjm-in` is ever added, and every
  `.tjjm-reveal` reads opacity 0 - which looks exactly like the bug in item 8 even after
  it is fixed. Check `document.visibilityState` and confirm requestAnimationFrame actually
  fires BEFORE concluding anything about reveal state. Related: the Shopify preview cookie
  is sticky and shared across tabs, and `section[data-tjjm-statedir]` is NOT a batch-51
  marker - it exists in the pre-batch-51 file too. Use the presence of `.tjjm-ja` jump
  links to tell the builds apart.
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
