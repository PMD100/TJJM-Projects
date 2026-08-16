# RULES — TJJM BJJ Directory

Durable decision rules for the Shopify BJJ school directory (thejiujitsumindset.com).
Last verified **5 Aug 2026** against live theme XX (`154653950124`), 4,519 records / 61 regions.

This file holds *rules and their evidence*. Running state lives in `HANDOFF-next-states.md`;
the collision investigation lives in `collision-audit-2026-08-05.md`. Where they disagree with
this file, this file is newer — but check the evidence rather than trusting the claim.

---

## 1. The collision rule

**Keep the record that names a real, current entity. Drop the one that is a generic city-stub
or a stale former name — regardless of provenance or location.**

Provenance (legacy vs MatMade) does not determine the answer. Neither does location. Both are
correlates that happen to track the real signal most of the time.

### Evidence (all 29 domain collisions where both records existed)

| class | n | resolution |
|---|---|---|
| cross-city, legacy suppressed | 8 | correct in all 8 — legacy was a mislocated stub |
| same-city, legacy suppressed | 20 | correct — legacy was a generic `<City> BJJ` stub |
| same-city, MatMade suppressed | 1 | correct — MatMade was the stale former name (CA `MZ Brazilian Jiu-Jitsu`) |

Plus `MA evolutionlowell.com`, a ninth cross-city case, resolved and no longer colliding after
theme XX renamed the record.

The pattern is visible in the same-city set: `Modesto BJJ` → `Gracie Jiu Jitsu Downtown Modesto`,
`Erie BJJ` → `Mata Leão Jiu-Jitsu`, `Amarillo BJJ` → `Guetho Texas BJJ`, `Everett BJJ` →
`Cascade Jiu-Jitsu`. A descriptive `<City> BJJ` domain outlives the listing that coined it and
ends up held by a differently-named school. The CA exception is the same shape reversed — there
the *MatMade* record carried the dead name.

### Two superseded formulations, and why they failed

- **"Keep the legacy record"** (original standing rule). Wrong in 28 of 29 cases.
- **"Different city → suppress legacy; same location → keep legacy"** (the audit's correction).
  The first half is right but for the wrong reason. The second half is wrong: it was built on the
  single CA case while 20 same-city counterexamples sat in the same dataset, filed as "cosmetic,
  no action proposed." Applying it would give the wrong answer on any same-city pair where the
  MatMade record is the stale one.

### Two misclassifications in the audit's own B1/B2 tables

Re-derived from live data 5 Aug 2026. They swap, so the 9/20 counts looked right:

- `OR oregonbjj.com` — filed B2 "same city". Actually **cross-city**: suppressed `Oregon BJJ`
  /Eugene, kept `CTA Hillsboro Jiu Jitsu and Boxing` /Hillsboro.
- `GA sakurabjj.com` — filed B1 "surviving record is in a DIFFERENT city". Actually **same-city**:
  Sakura BJJ /Woodstock → KODA Academy /Woodstock.

Consequence: the widely-quoted **"legacy was wrong 10 times out of 10"** double-counts Oregon.
Oregon is one of the cross-city cases, not an extra one. The verified cross-city evidence is 8.

### Procedure

1. Intersect by **domain** and by **name**. The name-only check found 0 of 40 domain collisions —
   never run it alone.
2. For each hit, ask which record names a real current entity. Generic `<City> BJJ`, an
   affiliation-only name, or a name the school no longer trades under loses.
3. **Open the site and read the body.** Do not decide from search results, `<title>`, meta
   description, or directory aggregators — see §4.
4. Same address + same entity → duplicate, suppress one. Same address + different entities →
   shared building, keep both (10 Oregon pairs, only 4 were true duplicates).

---

## 2. Blind spots — what a collision check cannot see

Four, not two. All are structural: no amount of care in running the check finds these.

1. **Never-imported duplicates.** Where the old rule was applied as written, the MatMade twin was
   never imported, so there is no second record to intersect (`ashlandbjj.com`). Only a re-diff
   against MatMade source finds these.
2. **Same-city duplicates on different domains.** `CJJF Academy - North Texas` (`cjjfntx.com`) and
   `Caveirinha Jiu-Jitsu Family Texas` (`cjjftx.com`) are one school on two domains. Needs a
   name/acronym pass (§4).
3. **Multi-tenant hosts are excluded from matching.** Facebook, Instagram, Mindbody, Square,
   Linktree and site-builder hosts are filtered out, or every Facebook-linked gym false-positives
   against every other. Two records genuinely sharing one Facebook page cannot collide.
4. **Single-record brand roots.** A collision needs two records. `GB South Shore` →
   `graciebarra.com` and `UFC GYM Boston Financial District` → `ufcgym.com` are both wrong links
   that no intersection will surface.

**Corollary:** the 29 adjudicated cases are all ones where a curator had already suppressed the
legacy record. The population where the old rule was applied — legacy kept, MatMade never
imported — is invisible by construction. Any "N times out of N" statistic drawn from this set
tests the curators, not the rule.

---

## 3. Verification method

Four corrections, each of which previously produced a clean-looking false result.

1. **`?preview_theme_id=` sets a cookie.** Any *unparameterised* fetch afterwards renders the last
   previewed theme, so a sweep comparing "live, no param" against "preview, with param" compares
   the theme to itself and reports a perfect pass. **Put an explicit `preview_theme_id` on both
   sides of every comparison.** Confirmed 5 Aug 2026: the param is consumed and the browser is
   redirected to the clean URL, leaving the cookie set.
2. **Storefront responses are cached.** Append a unique cache-buster to every fetch in a sweep.
3. **Never judge a link from a normalised domain.** Hostname normalisation collapses
   `tsk.com/locations/nj/hoboken/` and `tsk.com/` into one value. That turned 11 genuinely wrong
   links into an estimate of 38. **Inspect the raw `w` string.**
4. **Never judge case from a parsed hostname.** `URL.hostname` lowercases, which is why a scan
   reported zero mixed-case hosts. There are 3 (§6).
5. **`preview_theme_id` needs cookies, and the cookie forbids concurrency** (found 6 Aug 2026:
   a 61-region double-sweep reported all 61 regions changed with every count identical and a
   total of 4,519 → 4,519 on a build that had removed 7 records). Two separate causes, both of
   which produce correction 1's failure mode by a new route:
   - `fetch(url, {credentials:'omit'})` **silently defeats the parameter.** Shopify consumes
     `preview_theme_id`, sets a preview cookie and redirects to the clean URL; with credentials
     omitted the cookie is never stored, the redirect lands on the clean URL, and **the live
     theme is rendered.** Measured 6 Aug on one page: `omit` → 103, `include` → 100.
     → **Use `credentials:'include'` on every sweep fetch.**
   - The preview cookie is **one shared value per origin**, so parallel workers alternating
     BEFORE/AFTER race each other. → **Run the sweep sequentially (concurrency 1)**, each
     request re-asserting its own `preview_theme_id`. 61 regions × 2 sides ≈ 2 min. Verified
     6 Aug: sequential + `include` gave 55 byte-identical and exactly the 6 expected regions.

   **Gate that catches this class:** a sweep in which *every* region differs, or in which *no*
   region differs, is reporting a defect in the sweep, not a result. So is a total that does not
   move when the build removed records. Assert the expected total explicitly.

### The validation gate that does not work

Step 11 of the import sequence says to validate a rebuild by reproducing **one unchanged state**
byte-for-byte. **This gate is unsound.** It passes on any region where the render transforms
happen to be no-ops — NJ is one — while the method is wrong everywhere else. It passed cleanly on
5 Aug while the rebuild method would have silently rewritten ~1,076 records.

**Replace it with: rebuild all 61 regions, diff against the current artifact, and assert that
exactly the expected regions differ.** Same cost, and it verifies the claim instead of sampling it.

### The rendered page is not the stored record

`sections/tjjm-state-directory.liquid` transforms records on the way out:

- prepends `https://` to any `w` lacking a scheme
- substitutes `tjjm-gym-websites` overrides over the record's own `w`
- fills a blank address from `tjjm-gym-addresses`

So rendered JSON-LD **does not round-trip to stored values**. Use it to verify what the site
publishes; use `tjjm-gyms.json` or the audit dump for what a record actually stores.

**Correction, 6 Aug 2026 — `tjjm-gyms.json` is not raw stored values either.** It is a *third*
thing: stored values with `tjjm-gym-websites` overrides **applied**, but WITHOUT the `https://`
prepend and WITHOUT the `tjjm-gym-addresses` backfill. Proved by `Unconventional Performance &
Training`, whose blank override leaves the record in the file **with no `w` key at all**; the
other ten 5 Aug override URLs also appear in the file. Only the **audit dump** carries genuinely
raw stored `w`. This matters when re-measuring defect classes: §6's counts came from this file,
so they are post-override, not raw.

---

## 4. Detection signals

**Work:**

- **Domain intersection** — found 40 collisions the name check missed entirely.
- **Same street address within city** — suppress-normalise first:
  `addr.toLowerCase().replace(/\b(unit|ste|suite|#|apt|fl|floor)\s*[a-z0-9-]+\b/g,'').replace(/[^a-z0-9]/g,'')`.
  Reproduced all three known Oregon shared-building verdicts.
- **Acronym expansion** — initials of one name matching a short all-caps token in another, same
  city. This is the only signal that catches `CJJF` ↔ `Caveirinha Jiu-Jitsu Family`. **Requires a
  generic blocklist**: `BJJ`, `MMA`, `JJ`, `TKD` match everything and produced 28 of 30 hits.

**Does not work:**

- **Jaccard/token similarity on names.** 373 candidates, almost all noise, and it misses the CJJF
  pair outright (score 0.2). Not usable alone.

**Never trust:**

- **`<title>` tags, meta descriptions, and directory aggregators.** `evolutionlowell.com`'s title
  still reads "Gym in Lowell and Tewksbury" and three separate directories still list a Lowell
  address with its own phone number. The rendered page body mentions Lowell zero times and carries
  one address in Tewksbury. **Open the page and read the body — it reversed a verdict.**
- **Link resolution as evidence of correctness.** `Unconventional Performance & Training` carried
  `rodrigopinheirobjj.com`, a different business's site. It resolves perfectly. `gyms.jiujitsu.com`
  carries the identical error, so it is upstream. Only reading the page catches this class.

---

## 5. Data model

- Records live in `snippets/tjjm-gyms-data` (the ~113 KB legacy blob, 1,304 records) and
  `tjjm-gyms-data-2` … `-35` (per-state MatMade imports). The Admin API can only rewrite a
  snippet whole, which is why overrides exist.
- Record shape `{n,c,s,w,a}`; `w` and `a` optional. **Names must not contain `|` or `~`** — both
  are field separators.
- `snippets/tjjm-gym-websites` (`~Name|URL~`) overrides `w`; an **empty value blanks the link**.
  `snippets/tjjm-gym-addresses` (`~Name|Address~`) fills a blank `a` only.
  **Only add an entry that changes something** — restating a value pins it as a second source of
  truth that survives later correction of the record.
- `snippets/tjjm-removed-index` holds suppressed names, one row per region code. Suppression is a
  render-time filter; the record stays in the blob. Suppressed records are visible **only** via
  the audit dump.
- Newfoundland records are miscoded `NE` in source and re-filed by city list in the section. Any
  dump that skips the split double-counts NE and NL as 27 each.
- Section is 12,485 B against a ~24 KB Admin API rewrite ceiling.

---

## 6. Defect classes — current counts

Measured 5 Aug 2026 from **raw stored `w`** in the post-XX `tjjm-gyms.json`, not parsed hostnames.

| class | count | note |
|---|---|---|
| records with a website | 4,173 | of 4,519 |
| records with no website | 346 | |
| `http://` only | 1,706 | supersedes 1,712 (pre-XX) |
| `https://` | 2,181 | |
| **scheme-less** | **286** | **supersedes 516, which was wrong** |
| **mixed-case host** | **3** | supersedes both "0" and "1" |
| en/em-dash in name | 15 | |
| trailing `%20` | 0 | clean |
| `facebook.com/login` | 0 | clean |
| `w` literally `n/a` | 0 | clean |

The three mixed-case hosts: `NV Atlas Grappling`, `NV Gracie Jiu - Jitsu Summerlin`,
`CO Morning Star Jiu Jitsu`.

All 346 suppressed legacy records carry an `https://` URL — none are scheme-less or `http://`,
so suppressed records do not explain the old 516 figure. That number was simply wrong.

Still to scan for: shared phones across cities, ZIP contradicting city, **name contradicting
city** (`Elite Martial Arts-Richmond` filed under Paducah KY; `10th Planet St. Louis` filed under
Washington MO), wrong-entity social links.

---

## 7. Connector constraints

- **`themePublish` is blocked.** The user publishes.
- **`themeFilesUpsert` is blocked on MAIN.** Always duplicate first. `themeDuplicate` returns
  `newTheme`; wait ~30 s before files are readable.
- **`fileUpdate` is *not* reliably blocked.** It was blocked by the permission classifier on one
  run and succeeded cleanly on the next with no change in approach. Treat a block as situational,
  retry once, and report rather than working around it.
- `bulkOperationRunMutation` blocked; `themeFilesCopy` to assets is vestigial.
- **The sandbox has no outbound network.** Everything goes through the browser or the connector.
- **`javascript_tool` truncates at ~1–1.3 KB.** Write to `document.body.innerHTML='<main><pre
  id="D"></pre></main>'`, set `textContent`, then `get_page_text`. ~11 KB per chunk reads back.
- **The output filter blocks query-string/token-like data.** Signed upload parameters can be
  passed *in* safely; never echo them back.
- **Never hand-transcribe signed upload parameters.** A retyped base64 policy caused a 400 on
  5 Aug. Decode and assert the policy in-page (`atob` → `JSON.parse` → check `key` and
  `x-goog-date`) before posting.
- `window` state dies on navigation; `sessionStorage` does not. Stash long crawls there.

---

## 8. Standing cautions

**One sample is not validation.** This project has now generalised from a single unrepresentative
case four times, and it produced a clean-looking false result every time:

| generalised from | claimed | actually |
|---|---|---|
| NJ round-tripping | "rebuild method validated" | wrong for 49 of 61 regions |
| Oregon `oregonbjj.com` | "legacy wrong 10/10" | 8 verified, Oregon double-counted |
| CA `reddingselfdefense.com` | "same-location → keep legacy" | 20 counterexamples in the same data |
| `URL.hostname` scan | "0 mixed-case hosts" | 3 |

When a check passes on one sample, run it on all of them before writing down the conclusion. In
this corpus that is almost always affordable — 61 regions is one fetch loop.

**Brand coverage figures are unreliable in both directions.** The FL Fabin Rosa cluster was
recorded as "4 locations, 2 in directory" with 2 net-new leads. There is a third record already
in the directory under an acronym (`FRBJJ Lake Nona`) at a fifth location absent from the brand's
own locations page. Diff a brand roster against the **whole state**, never against the collision
cluster, and expect the roster itself to be incomplete.

---

## 9. Scope — what belongs in the directory

Added 13 Aug 2026, on the owner's ruling. **This was previously undocumented, which caused seven
records to be judged inconsistently across batches 9–15 and one to be wrongly suppressed in
production.**

**A record belongs if the school teaches a grappling art** — Brazilian jiu jitsu, **judo**,
wrestling, submission grappling or no-gi. Striking-only schools do not qualify: karate, taekwondo,
kickboxing, Muay Thai.

- **MMA schools usually teach grappling — verify rather than assume, in either direction.**
- The evidence is a **named class on the school's own page**. A meta description is not evidence:
  two schools carried "Brazilian Jiu-Jitsu" in `<meta>` while their actual class grids contained no
  grappling at all.
- Watch for BJJ surviving only in a **stale meta description inherited from a previous brand** after
  a rebrand to a striking school. Seen twice.

## 10. Counts live in THREE places, not two

Learned the hard way, 13 Aug 2026: two batches changed record counts and left the site displaying
three wrong numbers on **every** region page.

1. **`tjjm-gyms-data*` + `tjjm-removed-index`** — the truth. Everything else is a copy.
2. **`snippets/tjjm-region-index.liquid`** — a hand-maintained display count per region, **plus an
   asserted grand total inside its comment block**. Feeds the "Find schools in another state" nav
   at the foot of every region page.
3. **Page metafields** `title_tag` / `description_tag` — a third copy, and they also carry
   "across N cities" claims and example city names.

**Any batch that moves a count must update all three.** Before writing, assert that the
region-index counts **sum to the corpus-derived total** and that every region code appears exactly
once. Byte size is not a proxy: the fix for this defect changed three numbers and left the file the
same 3,446 B.

**⚠️ Verifying a page's own count does not verify the nav.** The page body count is computed from
the data and is always right. The nav list is a different file and can be stale. Check both.

**When suppressing, re-derive the city counts too** — three cities dropped to zero records in one
five-record suppression batch, so "across N cities" moved as well as the gym number.

## 11. A rendering page is not evidence of a live business

Supersedes §4's implicit assumption **in both directions**. Established over ~450 URL checks in
Aug 2026, during which **essentially 100% of stored URLs proved dead**.

**Always resolve DNS before believing any page:**

    web_fetch  https://dns.google/resolve?name=<hostname>&type=A

`Status: 3` = NXDOMAIN = conclusively dead. `Status: 0` **with an `Answer` array carrying A
records** = alive. `Status: 0` with no Answer = dead. Nameservers returning REFUSED (lame
delegation) = dead. Registered on live nameservers but publishing no A/AAAA at apex or www = dead.

**An empty body is NOT evidence of death** — live JS-rendered sites return empty.
**A full, convincing body is NOT evidence of life** — `web_fetch` serves cached copies and search
indexes serve stale titles. Eight domains returned complete pages with correct branding, addresses
and named black belts while being NXDOMAIN. Publishing one would also have meant transcribing a
named instructor's credentials from a defunct site.

### Five ways a live-looking page is still not the school's site
1. **Parked lander** — GoDaddy "parked free"/"Launching Soon", HugeDomains, Bluehost, one.com
   defaults. **Fifteen found on exact-name domains.** Indistinguishable from a JS site without a
   browser.
2. **Resurrected archive** — a re-registered domain replaying a scrape of the dead original.
   **Search the page for "Wayback Machine Downloader" and "free demo result".**
3. **Hostile hijack** — one serves a Chinese streaming site, one redirects to an Indonesian
   gambling SEO farm, one to an ad farm. **Follow redirects and read where you LAND.**
4. **Unclaimed booking stub** — a WellnessLiving/Square page whose rows read "Service Name" /
   "Instructor Name".
5. **Agency spec-build** — a free `*.vercel.app` deploy with a real address but placeholder
   trainer names.

### Identity, not name
**Same-name-different-school is the single most common false positive — 24+ cases**, including a
Hong Kong academy matching a Texas record and a domain 301ing to a school in another state.
**Match the street address or the phone, never the name alone.**

**Succession is not rebrand.** A different academy in the same unit under a different lineage or
head instructor is a wrong entity — 12+ cases. A genuine rebrand states the former name, or keeps
the same **named owner**, address or phone. Cross-checking a named person has repeatedly been the
only thing that resolved these.

**Brand-vs-location is normal and is not a defect.** Schools brand for the nearest metro and operate
in a suburb — `10th Planet Denver` in Wheat Ridge, `GB Tacoma` in Fircrest. Do not flag these.
See `gazetteer-scan-findings.md`.

**A dormant social page is not a live school.** Check the most recent post and whether a successor
occupies the address. Two closed schools were found only this way — no DNS or HTTP check reveals
them.

**Aggregators invent attributes, not just schools.** The sentence *"passionate about Brazilian
Jiu-Jitsu… strong fundamentals, technical precision, and a supportive training culture"* appeared
verbatim for **six unrelated schools**, all traceable to MatMade. Any claim sourced from a directory
template is worthless.

**Search summaries asserted 45+ dead domains as live**, several with invented programme lists and
trial offers. Two summaries agreeing means nothing — neither checked.

### Tooling
- **`web_fetch` cannot render Facebook or Instagram at all.** Those need a browser, and they are
  where much of the remaining value is: 26 of 36 links recovered by browser passes were social
  pages, invisible to every fetch-based attempt.
- **`web_fetch` dedupes within a session** — bust it with `?v=1`, or you silently reuse another
  agent's fetch.
- **⚠️ `get_page_text` frequently returns the PREVIOUS page's content.** Its output carries a
  `URL:` line — **always check it matches the page you navigated to.** Never batch `navigate` and
  `get_page_text` for the same page. It silently produces a confident verdict about the wrong site.
- **Agents can be cut off before writing their output**, losing all their work irrecoverably.
  **Instruct every research agent to write its output file incrementally, every few rows.**
