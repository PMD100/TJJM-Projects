# METHOD RULES — for research and verification agents

You are working on the TJJM BJJ school directory (thejiujitsumindset.com). Read all of this
before you start. Every rule below is here because breaking it has already produced a wrong
answer on this project.

**This file is durable and batch-agnostic — everything in it applies to every batch.**
Batch-specific traps (this region's known stubs, its particular city collisions, any structural
constraint like the Newfoundland city list) belong in a **separate per-batch addendum** handed
to you alongside this file. `METHOD-RULES-batch7-addendum.md` is the worked example.

Do not add batch-specific material here. It was done twice before and both times the notes
outlived their batch, so agents three batches later were being handed Iowa and Manitoba traps
as though they were current.

---

## The single most important rule

**Open the page and read the BODY.** Not the `<title>` tag, not the meta description, not a
directory aggregator, not a search-result snippet. All four have produced confidently wrong
verdicts on this project.

## ⚠️ NEVER STATE EVIDENCE YOU DID NOT READ

**Do not write down a lineage, instructor name, belt rank, affiliation, address or founding date
unless you read it yourself, on that school's own page, in this pass.**

This rule exists because it was broken. A research agent recorded *"Prof. Jay Zeballos, 3rd degree
black belt under Jean Jacques Machado"* as evidence for a school whose page body contains no such
text anywhere. The claim was invented. A later verifier caught it only because it re-read the body.
A second agent recorded an owner's name that the body contradicts.

If you cannot reach a body, the correct output is **UNVERIFIED** with a plain statement of what you
could and could not read. That is a useful result. A confident-looking fabrication is worse than
nothing, because it survives every downstream check that assumes evidence is real.

Two corollaries:

- **Never carry a claim forward from an input file** because it was already written there. If your
  input says "black belt under X" and you did not see it on the page, drop it or mark the row
  UNVERIFIED.
- **If you run out of context or budget, say so explicitly and flag the affected rows.** An Alberta
  researcher did exactly this — it marked ~30 rows "body not individually read - lower confidence",
  and verifiers found roughly two thirds of them defective. That honesty was more valuable than
  a complete-looking file would have been.

Concrete case: `evolutionlowell.com`'s title still reads "Gym in Lowell and Tewksbury" and three
separate directories still list a Lowell address with its own phone number. The rendered page body
mentions Lowell zero times and carries one address, in Tewksbury. Reading the body reversed the
verdict.

Second case: `Unconventional Performance & Training` carried a link to `rodrigopinheirobjj.com` —
a completely different business. The link resolves perfectly. `gyms.jiujitsu.com` carries the
identical error, so the mistake is upstream and propagates. **Only reading the page catches this.**

---

## Screening: DNS first, and a screen never concludes

To decide what order to work in, resolve the host:

    https://dns.google/resolve?name=<host>&type=A

- `"Status": 3` is NXDOMAIN. That is **conclusive** — the domain does not exist.
- Any other status, or a blank/failed body: record it as **UNRESOLVED**. It is *not* evidence.

A browser reachability screen has a **measured 39% false-positive rate** on this corpus (n=18,
against a known-live control), and it is structurally blind to a working link that is owned by
someone else. One batch that skipped DNS and relied on fetch alone returned 70 useless "EMPTY"
verdicts and had to be redone from scratch.

**A reachability screen orders your work. It never concludes anything about a school.**

---

## Traps that have actually fired

### 1. Country collisions — nine instances so far
City names overlap badly between Canada/US and the UK/NZ. Real examples that fooled earlier runs:

- `kingstonbjj.com` and `kingstonjiujitsu.com` — both **Kingston upon Thames, England**
- `peterboroughjudo.com` — **Peterborough, England** (postcode PE3 8AF)
- `resolvebjjacademy.com` — **Cambridge, NEW ZEALAND**
- `strongholdjiujitsu.co.uk` — England

Later batches added more, all confirmed by reading the page:

- `Sydney` — Nova Scotia's is on Cape Breton, pop. ~30,000. **Sydney, AUSTRALIA** is the trap.
- `Liverpool` — Nova Scotia and **ENGLAND**.
- `Brooks BJJ` — stored as Brooks, Alberta; actually **Dungannon, NORTHERN IRELAND**.
- `Lincoln Grappling Coalition` — stored as Nebraska; actually **Lincoln, ENGLAND**.
- `Synergy MMA` — stored as Wilmington, Delaware; the domain now serves **Bali, INDONESIA**.

Everything looks right except the country. **Check the country on every single candidate.**
Be especially suspicious of: London, Hamilton, Cambridge, Kingston, Peterborough, Windsor,
Waterloo, Guelph, Whitby, Brandon, Portage, Aberdeen, Vermillion, Sydney, Liverpool, Dieppe,
Bathurst, Newcastle, Stratford, Cornwall.

**Same-country collisions are just as common**, and there have now been 28+ of them: Bristol
TN vs Bristol VA (one street, two states), Cleveland TN vs Cleveland OH, Newark DE vs Newark NJ,
Wilmington DE vs Wilmington NC, Saint John NB vs St. John's NL, Athens TN vs Athens AL.
Verify the state or province from the page body — a postal code, area code or street address.

### 2. A `<City> BJJ` name does NOT mean the record is fake
This has failed as a verdict three separate times. `Brooklyn Brazilian Jiu Jitsu`,
`Binghamton Brazilian Jiu Jitsu`, `Ellsworth BJJ`, `Saco BJJ`, `Fort Smith BJJ` and
`Springdale BJJ` are all real, operating schools.

The `<City> BJJ` pattern is a **prioritisation signal only** — it tells you where to look first.
It is never a verdict.

### 3. A dead-looking URL may be a typo, not a dead school
Three Ontario "stubs" turned out to be real schools whose stored URL was simply wrong:

- `Cambridge BJJ` stored the `.com`; the school is on the `.ca`
- `Windsor BJJ` actually trades at windsorbrazilianjiujitsu.com
- **`Oshawa BJJ` stored `oshawawbjj.com` — a literal typo, an extra "w"**

Blanking any of those would have been wrong. **Before concluding a school is gone, try the
obvious corrections**: the other TLD, the typo-free spelling, the school's Facebook/Instagram,
and a plain search for the city plus "Brazilian Jiu Jitsu". Canadian schools stored on `.com`
are very often actually on `.ca`.

But a typo hypothesis does not always pay: `grandeprairebjj.com` looked like a missing "i", and
the corrected `grandeprairiebjj.com` is **also NXDOMAIN**. Try the correction, do not assume it.

### 3b. A resolving domain may have been repurposed entirely
Four cases in one batch. The business died, the domain lapsed, someone else took it:
`delawarebjj.com` now serves a school in a different city, `synergymma.com` now serves an
academy in **Bali**, `kazebjj.com` serves an unrelated business in **Scarborough, Ontario**, and
`ikaalaska.com` now serves Indonesian-language spam. **All return HTTP 200 and look healthy.**
Also watch for parked domains: three separate dead domains all served the identical GoDaddy
parked-domain template, which through a plain fetch is indistinguishable from an empty body.

### 4. A working link is not evidence the record is right
Ontario had 8 further `<city> BJJ` records that no screen ever flagged *because their links
resolve* — and at least two are wrong anyway. No Guelph school trades as "Guelph BJJ", and
Barrie BJJ's real site is 705bjj.com.

So: **check the records with working links too**, not just the flagged ones.

### 5. Brand rosters are unreliable in both directions
A brand's own locations page both omits locations it has and lists ones it does not. Diff a brand
roster against the **whole region**, never against a subset, and expect the roster to be incomplete.

---

## What to produce

For your assigned region, return:

1. **The full roster of BJJ schools actually operating in the region.** Mark each one
   `ALREADY-IN` (matches a record on the live page) or `NET-NEW`.
2. **A verdict on every suspect record** you were given: real / wrong-URL-but-real / genuinely
   gone / wrong entity. Cite what you saw in the page body.
3. For each NET-NEW: name, city, street address, website URL.

**Prioritise breadth of cities over exhaustiveness in the biggest city.** A batch that finds two
more schools in ten towns is worth more than one that finds ten more in the largest metro.

Every rebuilt region so far has come in at roughly **double** its listed count, and that held
across a tiny rural region with 100% broken links, a mid-size one with healthy links, and the
largest region in the corpus. Coverage and link rot are independent problems — do not assume a
region with working links is well covered.

---

## ⚠️ Tooling limits you must know before you conclude anything

- **`web_fetch` cannot render Facebook or Instagram at all.** It returns an empty body every
  time. This is not a per-page quirk. Small-town clubs frequently have no website — only a
  Facebook page — so this failure mode falls hardest on exactly the regions with the least
  coverage. An empty Facebook body is **not** evidence the school is gone. Mark it UNVERIFIED
  and flag it for a browser-render pass, which executes JavaScript and can read these pages.
- **A parked domain looks like an empty body.** Three dead domains in one batch all served the
  identical GoDaddy parked template. Through a plain fetch that is indistinguishable from a
  JS-rendered site. If you get an empty body, you have learned nothing either way.
- **The sandbox has no outbound network.** Do not try `curl`, `wget`, `requests` or any other
  fetch route — use `web_fetch` or the browser tools.
- **Search-result summaries are not sources.** A synthesized answer once asserted an owner name
  and street address that the business's own page contradicted on both counts.

## Format for anything you hand back

Return a **strict TSV**, not a prose table. Downstream parsing has silently failed twice on this
project — once on a delimiter change, once because an agent used a numbered-column layout and a
position-based parser returned zero verdicts for an entire region without erroring.

Columns exactly, `verdict` FIRST:

    verdict	region	name	city	url	action	evidence	source_url

`verdict` must be exactly one of: REAL / WRONG-URL / WRONG-CITY / WRONG-ENTITY / WRONG-REGION /
GONE / NOT-BJJ / UNVERIFIED / ADD / DROP. Do not invent new keywords.
`action` must be exactly one of: KEEP / SUPPRESS / FIX-URL / FIX-CITY / ADD / NONE.

⚠️ **In the `url` column put the URL that should be STORED** — the corrected one, not the one
already on file. Agents have disagreed about this and it produced four overrides that merely
restated the existing value. If you are recording the old URL for context, put it in `evidence`.

No tab characters inside any field. Cover every record you were given, including ones you
confirmed unchanged — a missing row is indistinguishable from an overlooked record.

## Data hygiene for anything you hand back

- Record shape is `{n, c, s, w, a}` — name, city, state/province code, website, address.
- **Names must never contain `|` or `~`.** Both are field separators in the storage format.
- Strip any `?query=string` from URLs you report — the output filter blocks token-like data.
- Do not transcribe listings from memory. Fetch the page and read it.
