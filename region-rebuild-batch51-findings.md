# Batch 51 — a city filter and jump-nav, and a live rendering bug that predates all of it

Session of 17–19 Aug 2026. Built as theme **AD3** (`155013906604`), **staged and awaiting publish**.
AC3 `155006140588` is MAIN and becomes the rollback.

---

## ⚠️ The important part: region pages have been rendering invisible on the live site

`assets/tjjm-core.css` sets `.tjjm-reveal{opacity:0}` and reveals it by adding `.tjjm-in`.
**`assets/tjjm-core.js` is the only thing that adds that class** — an IntersectionObserver over
`.tjjm-reveal:not(.tjjm-in)`.

`sections/tjjm-gym-directory.liquid` (the flat Schools Near You page) loads that script.
**`sections/tjjm-state-directory.liquid` — the 61 region pages — never has.** Verified three ways
against the published theme: the section has no script tag, `layout/theme.liquid` does not load
`tjjm-core.js` anywhere, and `snippets/tjjm-statedir-css.liquid` does not override the rule.

So every region page has been shipping the CSS that hides its gyms without the JS that shows them.
This is **not** a batch-51 regression. It has been live for a long time.

**Why nobody noticed:** the CSS carries a `@media (prefers-reduced-motion: reduce)` branch that
forces `opacity:1`. Anyone with Reduce Motion enabled — including, most likely, the owner doing the
spot-checks — sees the pages perfectly. Everyone else gets a page whose markup is complete and
crawlable but visually blank.

**Fix:** one line in the section, mirroring what the flat page already does —
`<script src="{{ 'tjjm-core.js' | asset_url }}" defer></script>` — plus an `html.no-js .tjjm-reveal`
safety net so the content is never hidden when scripting is unavailable. **No shared asset was
modified.** `tjjm-core.js` and `tjjm-core.css` are byte-identical to before.

---

## Three wrong diagnoses, and what actually settled it

This one resisted four attempts, so the failure modes are worth recording.

1. **A previous agent claimed "nothing anywhere adds `.tjjm-in`"** after scanning 23 script files,
   and concluded the reveal mechanism did not exist. It missed a 698-byte file. Wrong.
2. **I then claimed the CSS line `html{scroll-behavior:smooth}` was the root cause** of both the dead
   jump links and the invisible gyms. Tested first, as instructed. Wrong — removing it fixes neither.
3. **The measurement itself was broken.** Every "0 of 17 have `.tjjm-in`" reading — including mine —
   was taken in a **background tab**. `document.visibilityState` was `hidden`,
   `requestAnimationFrame` never fired, and **IntersectionObserver cannot fire without animation
   frames.** A freshly constructed observer returned zero entries, not even the mandatory initial
   one. The count went 0 → 1 the moment a screenshot forced a single render tick, then climbed to
   17 under scrolling.

**New standing rule: an IntersectionObserver assertion taken in a hidden tab is meaningless.** Force
a render tick before reading, or the result is noise. This is a close cousin of the page-substitution
trap — another case where the instrument, not the site, produced the finding.

4. **The dead jump links were never our bug either.** A **Klaviyo popup** sets
   `body.klaviyo-prevent-body-scrolling{overflow:hidden!important}`, which propagates to the viewport
   and freezes document scrolling. Proven by removing the class: `scrollY` went 0 → 600 immediately.
   It is intermittent, site-wide, and **present on MAIN too** — a Klaviyo setting, not a theme file.
   The other half of the symptom was reading `scrollY` synchronously after an animated smooth scroll.

`overflow:clip` and `position:sticky` were **not** the cause and are kept; the sticky bar works.

---

## The feature: city filter and jump-nav

Pagination was considered and rejected. Measured first: Texas is 524 KB of HTML but only **~22 KB
gzipped of that is gym data**, and a 33-gym Montana page still ships 288 KB — the weight is fixed
theme overhead, not gyms. Hiding 340 of 351 Texas gyms behind a "Load More" would have saved almost
nothing and cost indexable content on the pages whose whole purpose is to be found in search.

The real friction was navigational: 351 gyms under **134** city headings. So:

- **A filter input** matching both city and gym name, with a live count and a clear button.
- **A jump-nav** rendered server-side as real `<a>` links, grouped by first letter in a `<details>`
  element — open at ≤24 cities, collapsed above, and needing no JavaScript to work.
- **Every gym stays in the DOM in every filter state**, including zero-match. Filtering toggles
  `hidden`; nothing is ever removed.

### Verified on three regions

| check | Montana | Texas | Colorado |
|---|---|---|---|
| reveals reaching opacity 1 | 17/17 | 135/135 | 47/47 |
| `scrollTo` moves the page | ✅ | ✅ | ✅ |
| jump link vs sticky bar | clear by 19px | clear | clear |
| cards in DOM, every filter state | **33** | **351** | **155** |
| filter by city / by name / clear | ✅ | ✅ | ✅ (Clear and Esc) |
| **served HTML** cards / headings / jumps | 33/16/16 | **351**/134/134 | 155/46/46 |
| console errors | none | none | none |

JSON-LD `numberOfItems` agrees: TX 351, CO 155. Zero-match shows a "No schools match" message and
dims every jump link while keeping them in the document.

## Files written to AD3

| file | bytes | MD5 | API checksum |
|---|---|---|---|
| `sections/tjjm-state-directory.liquid` | 13,339 → **20,062** | `ae5415adad8d74a7c297cc58a1cf5b83` | ✅ |
| `snippets/tjjm-gym-websites-7.liquid` | 7,018 → **14,390** | `2e5e4461a80add8d232d36eaf5371695` | ✅ |

Both under the 24,576 ceiling. Append-only on file 7 proven: the first 7,018 bytes still hash to the
prior value and all 42 override rows are byte-identical.

**One deviation worth knowing:** the staged comment block asserted two things that had just been
disproved — that smooth scroll broke the jump-nav, and that nothing adds `.tjjm-in`. Committing that
to the permanent engineering record would have re-seeded the same wrong diagnosis for whoever reads
it next. It was rewritten, keeping every re-verified claim.

## Corrections to numbers I had wrong

- Texas has **134** city headings, not 135 — batch 50's Whitefish → Columbia Falls correction emptied
  a heading. Montana has **16**, not 17.
- Colorado is **155** gyms, not 135.
- `section[data-tjjm-statedir]` is **not** a reliable batch-51 marker — it exists in the older file
  too. Use the presence of `.tjjm-ja` jump links.

## Next

1. **Publish AD3.** It carries the rendering fix, which matters more than the feature.
2. **The Klaviyo scroll lock** is unfixed and not a theme file — worth changing in Klaviyo, since
   when that popup appears it freezes the page for real visitors.
3. **Audit the other 15 duplicated names** before one takes a blanking row and kills a healthy school.
4. **The address-override regex bug** — the flat page's parser needs a trailing `~`, and
   `tjjm-gym-addresses.liquid` has rows without one, so it silently drops alternate overrides there.
5. Continue the hidden-spam re-screen — 742 links left.
