# Batch 30 — Schools Near You rebuilt from the audited corpus. 5,215 schools, searchable.

Session of 15 Aug 2026. Built as theme **HHH** (`154955448492`), **staged and awaiting publish**.
**Publish HHH `154955448492`.** GGG `154955088044` becomes the rollback.

---

## The page now renders from the same source as the 61 region pages

| | before batch 29 | batch 29 | **batch 30 (HHH)** |
|---|---|---|---|
| records shown | 4,493 | 50 | **5,215** |
| outbound links | 4,149, **none vetted** | 46, 6 known-bad | **4,422, all through the override system** |
| data source | Shopify Files JSON + metaobjects | metaobjects only | **snippets/tjjm-gyms-data … -45** |
| states covered | mixed | **3** | **61** |
| search | none | none | **gym, city, state code or state name** |
| suppressed records shown | 692 | some | **0** |

`sections/tjjm-gym-directory.liquid` now inlines exactly the five snippet families the region
pages use — the 45 data files, the three website override files, the address overrides, the
removed-index and the region-index — and does the merge in JavaScript. The merge rules are a
line-for-line port of `sections/tjjm-state-directory.liquid`, including the Newfoundland/Nebraska
re-file by city.

**There is no second data source any more.** Both the Files JSON and the `gym_listing` metaobject
rendering are gone. A future batch that adds an override or a suppression changes this page
automatically, with no separate upload.

### The merge was validated before it shipped
The same algorithm was run locally over the identical files and reproduces the region pages
**exactly**:

```
published records: 5,215      region-index asserted total: 5,215
regions where computed count != region-index count:  NONE (0 of 61)
with a link: 4,423   without a link: 792
```

Then confirmed live on the HHH preview: count widget **5,215**, 61 state options whose individual
counts match the region-index row for row (Alabama 78, Alaska 14, Alberta 72 … Wyoming 10).

### Spot checks on the preview

| probe | result |
|---|---|
| `101 Academy Jiu Jitsu` (suppressed) | **absent** |
| `101 Academy` | present, `https://101academy.ca/` |
| `Airdrie BJJ` (fabricated, NXDOMAIN) | **absent** |
| `Altitude MMA` (blanked) | present, **no link** |
| state = Alberta | **72** — matches the region page |
| state = Newfoundland and Labrador | **13** — the NE/NL re-file works |
| `gracie barra` + Texas | 14 |
| `brooklyn` | 24 |

---

## The owner's 404 report, and a failure mode we had no check for

`10th Planet Jiu Jitsu Boulder - Lafayette` carried `http://www.10thplanetboulder.com`. The domain
**resolves cleanly** — Cloudflare, `104.21.2.199` / `172.67.129.155` — so every DNS screen in this
programme passes it. The root URL returns a bare **404 Not Found**. Yelp lists the Boulder location
as closed and the nearest live 10th Planet affiliate trades under a different name and domain, so
there is no verified replacement. **Link blanked**; the record stays listed with its name, city and
map link.

> **RESOLVES-BUT-404 is a new named failure mode.** A DNS check says alive. A "is this a martial
> arts site" content screen sees an error page and may or may not flag it. Neither is reliable.
> **Future sweeps must record the HTTP status code**, not just resolution and content.

---

## Files written

| file | was | now |
|---|---|---|
| `sections/tjjm-gym-directory.liquid` | 10,062 B · `8fc91b86…` | **17,139 B · `0cb98941ba9c76450eadc5c9260f4ff4`** |
| `snippets/tjjm-gym-websites.liquid` | 7,663 B · `16a71510…` | **8,766 B · `9e24bb087185abd378a7d5e9cb7de537`** |

Both reconstructed locally and MD5-matched against the theme, byte for byte. Archived in
`build-b30/`. Website overrides now total **866 entries, 586 blanking, zero duplicate names across
the three files** (gate C3 clean).

### Structural guarantee
Every record-bearing file in HHH is byte-identical to GGG — legacy blob `1ee054…`, data-45
`8fb61a…`, removed-index `98ee61…`, region-index `8f4faa…`, state-directory section `633ec8…`,
websites-2 `08c171…`, websites-3 `ab606f…`, addresses `031ea9…`. **The 61 region pages are
untouched.** The one link change is a blanking override, which cannot move a record count.

### Page metafields updated
- `title_tag` → *BJJ Gym Directory: 5,215 Jiu Jitsu Schools Near You*
- `description_tag` → *Search 5,215 Brazilian Jiu Jitsu schools across the United States and Canada by gym, city or state…*

⚠️ This adds a **fourth** place a count lives (RULES §10 lists three). When the corpus total moves,
update this page's two metafields as well as the region-index and the region metafields.

---

## Known trade-offs, stated plainly

1. **Page weight.** The page now ships ~676 KB of raw record data inline (~150 KB over the wire
   after compression) instead of fetching a 488 KB cached JSON. That is the price of having one
   source of truth. If it ever becomes a problem, the fix is a `{% layout none %}` JSON template
   rendered from the same snippets and fetched by the page — still one source of truth, but cached
   at the CDN. Do **not** solve it by uploading a static file again.
2. **Client-side rendering.** Cards are built in JavaScript, so this page contributes nothing to
   search indexing. That is fine: the 61 region pages are the SEO surface, they are server-rendered
   with per-region titles, descriptions and `ItemList` schema, and they are linked from this page
   and from every card.
3. **One record lost.** `14ers Jiu Jitsu` existed only in the metaobject set, not in the audited
   corpus, and had no website. 49 of the 50 metaobject records were already in the corpus. If it is
   a real school it should be added to a data snippet properly.
4. **Renders 300 at a time** with a "Show more" button, so a 5,215-card page does not stall on
   mobile. Search and the state filter always run over the full set.

---

## Where the directory stands

| | |
|---|---|
| records published | **5,215** across 61 regions |
| with a link | 4,422 |
| deliberately link-free | 793 |
| links audited or screened | 1,832 |
| harmful links removed | 193 |
| links restored to a correct URL | 190 |
| unvetted links removed from this page | ~4,149 |

## Next

1. **The remaining link screen.** 614 dirty-bucket links (`scratch/hijack-screen/dirty-5.tsv` …
   `dirty-8.tsv`), then the `https://` tail, **stratified by region** — the Alberta episode showed a
   corpus-wide random sample cannot detect a bad region.
2. **Add HTTP status to the screen.** The 10th Planet case proves DNS + content is not enough.
3. **793 link-free records.** ~230 are estimated recoverable with a browser pass. Every one
   recovered makes the directory more useful; none of them can do harm while blank.
4. **172 EMPTY rows** — JS-rendered or Cloudflare-fronted, need a browser session.
5. **The identity pass** — wrong-location and wrong-school links a content screen passes cleanly.
