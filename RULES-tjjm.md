# RULES — TJJM BJJ Directory

Durable decision rules for the Shopify BJJ school directory (thejiujitsumindset.com).
Sections 1–10 were last verified **5 Aug 2026** against live theme XX (`154653950124`),
4,519 records / 61 regions. Sections 11–16 were rewritten **16 Aug 2026** from the batch 30–42
findings. The theme ID, record count and defect counts in the earlier sections are the 5 Aug
state and have since moved — treat them as method, not as current numbers.

**CURRENT STATE, 16 Aug 2026, theme ZZ2 (`154993066156`), staged for publish:**
**5,215 records across 61 regions · 4,100 with a link · 1,115 deliberately link-free ·
1,284 override rows, all distinct names.**

⚠️ **Batch-48 correction to §11.** Browser page substitution is **not** biased toward healthy gyms —
this round it also landed on a Wix error page and a gambling lander, so a mismatch can produce a
false *bad* verdict as easily as a false clean one. And **hostname alone is not a sufficient
assertion**: one read kept `host` = `www.facebook.com` while silently swapping the *path* to another
school's page. Every browser probe must return **`location.hostname` AND `location.pathname`
alongside the body, from inside a single JS evaluation**, and must never read page content in a
follow-up call — the tab moves between calls.

⚠️ **Before concluding DEAD, check for a REPOINT.** If only a stored deep path 404s and the site root
serves the right school, the link is fixed, not removed. Batch 48 saved 8 links this way.

⚠️ The corpus holds **5,894 distinct names across 5,911 records — 17 names are duplicated.** Gate C11
(name matches exactly one published record) will fail on those. Resolve before one lands in a batch. The corpus grew from 4,519 to 5,215 because the
region pages render 45 data snippets, not the 38 the earlier sections assume. Re-measure before
quoting any number in this file.

This file holds *rules and their evidence*. Running state lives in `HANDOFF-next-states.md`;
the collision investigation lives in `collision-audit-2026-08-05.md`; the batch 30–42 evidence
behind §11–§16 lives in `CRITICAL-false-positive-removals.md`,
`CRITICAL-second-directory-surface.md` and `AUDIT-COVERAGE-where-we-actually-are.md`.
Where they disagree with this file, this file is newer — but check the evidence rather than
trusting the claim.

**If you read only one section, read §11.** It supersedes the DNS-first screening method that
governed batches 20–36. Acting on the old method costs working links: 10.8% of the removals we
have gone back and re-tested were wrong.

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

Six corrections, each of which previously produced a clean-looking false result.

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

6. **A corpus-wide claim must name its rendering surface.** Every sweep through batch 28 targeted
   the 61 region pages, so every "no dead links remain" report in that period was silently scoped
   to one of the site's **two** front doors — while the other served ~4,150 unvetted links,
   including ones we had already blanked. See **§14**.
   → **Enumerate the rendering surfaces before believing any corpus-wide statement**, and say
   which surfaces a sweep covered when reporting it.

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

- **A fetched page body, on its own.** Added 16 Aug 2026 and it outranks everything else in this
  list: the fetcher caches, and it has served full live-looking school content for domains that
  were dead, and spam for a domain that was a placeholder. A fetch may mark a row SUSPECT; it may
  not remove a link. **See §11.1 and §11.2 before acting on any fetch result.**
- **`<title>` tags, meta descriptions, and directory aggregators.** `evolutionlowell.com`'s title
  still reads "Gym in Lowell and Tewksbury" and three separate directories still list a Lowell
  address with its own phone number. The rendered page body mentions Lowell zero times and carries
  one address in Tewksbury. **Open the page in a browser and read the body — it reversed a
  verdict.** ("Open the page" originally meant a fetch. It no longer does.)
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
  The website override is a **family of six files**, `tjjm-gym-websites` … `-6`, each under its own
  rewrite ceiling. Fill order, headroom and the gates that govern them are in **§15.5**.
- `snippets/tjjm-removed-index` holds suppressed names, one row per region code. Suppression is a
  render-time filter; the record stays in the blob. Suppressed records are visible **only** via
  the audit dump.
- Newfoundland records are miscoded `NE` in source and re-filed by city list in the section. Any
  dump that skips the split double-counts NE and NL as 27 each.
- Section is 12,485 B against a ~24 KB Admin API rewrite ceiling.
- **There are two sections that render this data, not one** — the region pages and the flat
  "Schools Near You" page. Both must read the same snippets. **§14.**

---

## 6. Defect classes — current counts

Measured 5 Aug 2026 from **raw stored `w`** in the post-XX `tjjm-gyms.json`, not parsed hostnames.

⚠️ **These counts predate batches 30–42** and every removal, restoration and recovery in them. The
*method* below is still correct — measure from raw stored `w`, never from parsed hostnames — but do
not quote the numbers. Re-measure. For the current state of the corpus see **§16**.

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
| batches 1–28 region sweeps | "no dead links remain" | a second surface served ~4,150 unvetted links (§14) |
| fetch-based dead-link screens | "N links removed, all confirmed dead" | 10.8% of re-tested removals were live schools (§11.4) |

When a check passes on one sample, run it on all of them before writing down the conclusion. In
this corpus that is almost always affordable — 61 regions is one fetch loop.

**A removal count is not a quality metric.** For twenty batches this programme reported "links
removed" as if it were a measure of progress. It is a measure of *activity*. The measure of
progress is the **false-positive rate** — how many of those removals were wrong — and nobody asked
for it until batch 37. When somebody finally did, re-testing 343 removals found **37 working links
that we had cut ourselves.** Any batch that changes links must report both numbers, or it is
reporting half a result. See §11.4.

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
wrestling, submission grappling, no-gi or **sambo**. Striking-only schools do not qualify: boxing,
kickboxing, Muay Thai, karate, taekwondo.

Re-confirmed unchanged by the owner at batch 42, with `sambo` and MMA made explicit. It keeps being
re-litigated inside batches; it is settled.

- **MMA gyms that teach grappling are in scope. MMA schools usually do teach it — verify rather
  than assume, in either direction.**
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

## 11. Evidence standards — what a page proves, and what it does not

**Rewritten 16 Aug 2026. This section supersedes the DNS-first screening method that governed
batches 20–36.** That method was right that DNS is *necessary*. It was wrong that DNS plus a
fetched body is *sufficient*, and it was wrong in the expensive direction: it removed working
links.

⚠️ **Two sentences from the previous version of this section are now known to be wrong and are
corrected below:** *"essentially 100% of stored URLs proved dead"* (§11.0) and *"an empty body is
NOT evidence of death"* (§11.6).

### 11.0 The retracted headline

The old text said the method was *"established over ~450 URL checks in Aug 2026, during which
essentially 100% of stored URLs proved dead."* That was a **hand-picked sample of already-suspect
URLs** — domains pulled precisely because something looked wrong with them. Read as a statement
about the corpus it is badly wrong, and it was the licence under which whole batches removed links
on thin evidence, on the assumption that almost anything flagged was dead anyway.

**Never quote a hit rate measured on a targeted sample as a corpus rate.** The corpus position is
§16.

### 11.1 A fetched page body is weak evidence — the fetcher caches

We already knew `web_fetch` serves cached copies of **NXDOMAIN** domains; that is why every screen
does a DNS check first. The batch 37 audit found something worse: **it also serves stale bodies for
pages whose content has changed.**

Checked against a real Chrome load, the fetcher returned full, live-looking school content for
**six domains the browser showed were dead** — `atosorlando.com`, `davestrasser.com`, `dkjla.com`,
`endurancebjj.com`, `theboxingclub.net`, `capemartialarts.com` — and returned **Japanese pharma
spam** for `evolutionfightacademy.com`, which the browser showed as a Wix placeholder.

So a fetch-based verdict can be wrong in **both directions**:

- a dead site reads as alive → we keep a broken link
- a hijacked site reads as clean, or a clean site reads as hijacked → we blank or keep the wrong thing

**A cache-buster does not fix this.** `?v=1` defeats within-session dedupe (§11.10); it does
nothing about a stale body served for a live hostname.

### 11.2 A fetch may not remove a link. Only a browser may.

**This is the operative rule of the whole section.**

In batch 42, 33 links that a fetch pass had flagged bad were re-loaded in Chrome. **Eleven were
perfectly healthy** — a third of them. Acting on that fetch pass would have cut 11 working links
out of the directory in a single batch.

- A **fetch-based pass may not blank a row.** It marks the row **SUSPECT** and defers it to a
  browser pass. That is the whole of its authority.
- A **browser load may blank a row.**
- Where a fetch is the only evidence available, **the note must say so**, so the row can be
  re-tested later rather than being mistaken for a settled verdict.

This costs throughput. It is cheaper than restoring links one at a time after an owner complains.

### 11.3 Test BOTH host forms

**A domain is dead only if `apex` AND `www.` both fail.** One form failing proves nothing.

**Four of the first eight confirmed false positives were domains that were NXDOMAIN on `www.`
while the apex served the school perfectly.** Half the early damage came from this one shortcut.

### 11.4 Measure the false-positive rate, not just the removal count

Across the programme, **37 of 343 re-tested removals were wrong — 10.8%.**

**Every screening batch must re-test a sample of its own removals and publish the rate next to the
removal count.** A batch that reports only "N links removed" has not reported a result. See §8.

### 11.5 DNS is necessary, not sufficient — and four failure modes it cannot see

Still resolve DNS first; it is cheap and it is the only conclusive *negative* we have:

    web_fetch  https://dns.google/resolve?name=<hostname>&type=A

`Status: 3` = NXDOMAIN = conclusively dead. `Status: 0` **with an `Answer` array carrying A
records** = resolves. `Status: 0` with no Answer = dead. Nameservers returning REFUSED (lame
delegation) = dead. Registered on live nameservers but publishing no A/AAAA at apex or www = dead.
Test both host forms (§11.3).

But **a clean resolve is not a working link.** These four all resolve perfectly, and no DNS or
parking check will ever surface them:

1. **RESOLVES-BUT-404** — the domain resolves cleanly, the root returns a bare 404. We found this
   class only because an owner reported it.
2. **LOCATION-PAGE 404** — a shared brand domain is perfectly healthy while the individual
   school's subpage is gone: `graciebarra.com/<slug>`, `ufcgym.com/locations/<city>`. Any check
   that tests the registrable domain rather than the stored URL passes it. **Test the stored `w`,
   the whole path** — this is §3's "never judge a link from a normalised domain" arriving from a
   second direction.
3. **REDIRECT-TO-INDEX** — the school's page silently redirects to the brand's generic
   find-a-school index and returns **HTTP 200 with a real-looking martial arts page.** A status
   check passes it. An "is this a martial arts site?" check passes it. **Only reading the page and
   matching the city catches it.**
4. **EMPTY IS NOT NEUTRAL** — §11.6.

### 11.6 EMPTY IS NOT NEUTRAL — correcting the old rule

The previous version of this section said: *"An empty body is NOT evidence of death — live
JS-rendered sites return empty."* That sentence was used as grounds to **leave empty-body rows
alone**, and as guidance it is wrong.

**A page a fetch cannot read is SUSPECT, not unknown.**

When 198 such links were opened in a browser, **137 were broken — 69%.** They were Wix "domain not
connected" placeholders, expired Squarespace accounts, Flywheel and cPanel defaults, Cloudflare
1001/520/522 errors, and GoDaddy `/lander` redirects. **Every one of those returns an empty body to
a fetcher**, which is exactly why "empty" looked neutral and is not.

The narrow true part survives: an empty body is not *proof* of death, so it still does not license
a removal by itself (§11.2). It is a **queue for the browser pass**, not a pass.

### 11.7 Five ways a live-looking page is still not the school's site
1. **Parked lander** — GoDaddy "parked free"/"Launching Soon", HugeDomains, Bluehost, one.com
   defaults. **Fifteen found on exact-name domains.** Indistinguishable from a JS site without a
   browser. Calibrated A-record fingerprints now narrow the search cheaply — **§12** — but the IP
   is a filter, never a verdict.
2. **Resurrected archive** — a re-registered domain replaying a scrape of the dead original.
   **Search the page for "Wayback Machine Downloader" and "free demo result".**
3. **Hostile hijack** — one serves a Chinese streaming site, one redirects to an Indonesian
   gambling SEO farm, one to an ad farm. **Follow redirects and read where you LAND.**
4. **Unclaimed booking stub** — a WellnessLiving/Square page whose rows read "Service Name" /
   "Instructor Name".
5. **Agency spec-build** — a free `*.vercel.app` deploy with a real address but placeholder
   trainer names.

### 11.8 Identity, not name
**Same-name-different-school is the single most common false positive — 24+ cases**, including a
Hong Kong academy matching a Texas record and a domain 301ing to a school in another state.
**Match the street address or the phone, never the name alone.**

**Succession is not rebrand.** A different academy in the same unit under a different lineage or
head instructor is a wrong entity — 12+ cases. A genuine rebrand states the former name, or keeps
the same **named owner**, address or phone. Cross-checking a named person has repeatedly been the
only thing that resolved these.

**Brand-vs-location is normal and is not a defect.** Schools brand for the nearest metro and operate
in a suburb — `10th Planet Denver` in Wheat Ridge, `GB Tacoma` in Fircrest. Do not flag these.
See `gazetteer-scan-findings.md`. This is also the commonest source of bogus **wrong-city**
verdicts — §13.1, where 10 of 15 flagged rows turned out to be adjacent suburbs.

**A dormant social page is not a live school.** Check the most recent post and whether a successor
occupies the address. Two closed schools were found only this way — no DNS or HTTP check reveals
them. A *live* social page, by contrast, is an acceptable directory link — §13.2.

**Aggregators invent attributes, not just schools.** The sentence *"passionate about Brazilian
Jiu-Jitsu… strong fundamentals, technical precision, and a supportive training culture"* appeared
verbatim for **six unrelated schools**, all traceable to MatMade. Any claim sourced from a directory
template is worthless.

**Search summaries asserted 45+ dead domains as live**, several with invented programme lists and
trial offers. Two summaries agreeing means nothing — neither checked.

### 11.9 A hijack verdict is a snapshot, not a permanent property

**Two schools removed for carrying injected pharma spam had cleaned their sites up by the time
they were re-tested.** A compromise is a state a site passes through, not an attribute of the
business. "Hijacked once" is not a permanent disqualification: re-test hijack removals on the same
schedule as every other removal (§11.4).

The converse holds too — a site clean today can be compromised next month. Neither verdict is
durable, which is an argument for dating every verdict, not for skipping them.

### 11.10 Tooling
- **`web_fetch` cannot render Facebook or Instagram at all.** Those need a browser, and they are
  where much of the remaining value is: 26 of 36 links recovered by browser passes were social
  pages, invisible to every fetch-based attempt.
- **`web_fetch` dedupes within a session** — bust it with `?v=1`, or you silently reuse another
  agent's fetch. ⚠️ **This is the lesser of the two caching problems and the cache-buster only
  fixes this one.** The stale-body problem in §11.1 survives it.
- **⚠️ `get_page_text` frequently returns the PREVIOUS page's content.** Its output carries a
  `URL:` line — **always check it matches the page you navigated to.** Never batch `navigate` and
  `get_page_text` for the same page. It silently produces a confident verdict about the wrong site.
- **Agents can be cut off before writing their output**, losing all their work irrecoverably.
  **Instruct every research agent to write its output file incrementally, every few rows.**

## 12. Parking and lander fingerprints

Calibrated across batches 30–42, **each fingerprint verified against a known lander**. Matching A
records is what made a complete DNS pass over the corpus affordable at all — it is a cheap filter
over thousands of hostnames.

**Parking / for-sale — flag the row and look at the page:**

| A records | operator |
|---|---|
| `15.197.148.33` + `3.33.130.190` | Afternic / GoDaddy for-sale |
| `76.223.54.146` + `13.248.169.48` | GoDaddy for-sale |
| `13.223.25.84` + `54.243.117.197` | HugeDomains |
| `208.91.197.27` | Confluence / Sedo — serves nothing |

**NOT parking — do NOT flag. Both of these front real, live schools:**

| A records | what it actually is |
|---|---|
| `15.197.225.128` + `3.33.251.168` | GoDaddy **web forwarding** |
| `76.223.105.230` + `13.248.243.5` | GoDaddy **Website Builder** hosting |

Note how close those are to the for-sale pairs above them — same providers, adjacent ranges.
**Match the exact pair. Matching "a GoDaddy IP" blanks live schools.**

**The IP is a filter, never a verdict.** It says *look at this page*. It never says *remove this
link* — that still requires a browser load under §11.2. Batch 32 made the opposite trade
deliberately, fetching a page only when the IPs looked like a lander because "if the IPs match
nothing → OK, do not fetch the page. That keeps this sweep fast." It bought a complete DNS pass
cheaply and found 51 dead or parked domains. It is also why **47% of the corpus has still never
had its page read** (§16). The trade was defensible once; do not make it again silently.

## 13. Editorial policy — what to blank and what to keep

Set by the owner. These are **rulings, not inferences.** Do not re-derive them from first
principles inside a batch.

### 13.1 Wrong city → blank the link, keep the record

The record stays; the link goes. But first — **distinguish a genuine wrong-entity link from an
adjacent suburb.**

In batch 42 the classifier returned 15 wrong-city rows and **only 5 were genuine.** The other ten
were **4–8 miles apart**, and in two of them — `AKF Lexington` and `Brian Beury Jiu Jitsu` — **the
record's stored city was the error, not the link.** Blanking on the classifier's word would have
cut ten good links and left two records still wrong.

**Before blanking, check the site's city against BOTH the record's stored city AND its stored
street address.** If the address agrees with the site and only the city string disagrees, **fix the
record**; do not touch the link. This is §11.8's brand-vs-location rule seen from the other side:
schools brand for the metro and sit in the suburb, and the directory's own city field is not
above suspicion.

### 13.2 Aggregators — keep the school's own presence, blank the intermediary

**Acceptable as a directory link:**

- A school's own **Facebook** or **Instagram** page. For many small gyms **it is their only web
  presence**, and a live social page serves the reader better than a blank. (A *dormant* one does
  not — §11.8.)

**Blank:**

- **Booking platforms** — Mindbody, Vagaro, MyStudio, Zen Planner, Wodify
- **Google `business.site`** pages
- A **brand's national homepage** standing in for a location
- **Third-party directories** — Yelp, Google Maps, matmade, "best gyms in X" listicles

The line is authorship: **does the school control what that page says.** A booking widget and a
listicle both fail that test. The gym's own Instagram passes it.

Note this is a *policy* distinction, not the *matching* distinction in §2 blind spot 3 —
multi-tenant hosts are excluded from collision matching regardless of whether they are acceptable
as links.

### 13.3 Scope is unchanged

See **§9**. Any grappling art qualifies — BJJ, judo, wrestling, no-gi, sambo, and MMA gyms that
teach grappling. Striking-only is out. Restated here because it is the ruling most often
re-argued mid-batch.

## 14. Directory architecture — there are TWO rendering surfaces

| section | what it renders |
|---|---|
| `sections/tjjm-state-directory.liquid` | the **61 region pages** |
| `sections/tjjm-gym-directory.liquid` | the flat, searchable **"Schools Near You"** page |

**Both must read the same snippets.**

Until batch 29 the second one did not. It fetched a **Shopify Files upload** — `tjjm-gyms.json`,
sitting outside the theme, outside version control, outside the theme-duplication workflow and
**outside every override layer we had built**. It served **~4,150 unvetted links**, including dead
and hijacked domains already blanked on the region pages, and records already suppressed there.
Publishing a theme did not touch it. Rolling back a theme did not touch it. **Twenty-eight batches
of work were invisible to it**, and every "no dead links remain" report in that period was true
only of the region pages — a fact discovered only because the owner was looking at the other page
and was told his screenshots must be a local DNS problem.

Three rules follow, all mandatory:

1. **Never reintroduce a second data source.** Everything the directory renders comes from
   `tjjm-gyms-data*`, filtered by `tjjm-removed-index`, overridden by `tjjm-gym-websites*`. A data
   file that lives outside the theme cannot be gated, diffed, or rolled back.
2. **If a change touches one section's merge rules, it must touch both.** A new override file is
   not wired in until it renders from **both** sections (§15.5).
3. **A corpus-wide claim must name its surface** (§3.6).

## 15. Writing to the theme — process rules

### 15.1 NEVER hand-edit a file during transmission

**Build the file. Verify its MD5 locally. Send exactly those bytes.** Do not retype, reflow,
truncate, or "just fix one thing" between the verified local copy and the write.

**This discipline broke three times in batches 37–39, and each time the theme diverged from the
repo.** That is the specific harm: the local artifact stops describing what the site is serving,
which is the one guarantee the repo exists to provide. Every subsequent diff is then measuring the
wrong thing, and you do not find out until something else fails strangely.

**If a file is too large to send comfortably, that is a reason to split the batch, not to
improvise.**

### 15.2 Delegate large-file edits to a sub-agent

The pattern that works, and the one to reach for by default:

> a sub-agent **reads the file from the theme**, edits it **with a script**, writes it back, and
> **checksums both ends.**

**Batches 40–42 did this with zero drift.**

"With a script" is load-bearing, not incidental. A script that produces the wrong bytes produces
them reproducibly, and the end-to-end checksum catches it. A hand-edit produces a *plausible* file
that no gate can distinguish from the intended one.

### 15.3 Gate C3 — a gym name may appear in only ONE override file

**Absolute. No exceptions.**

It has caught real bugs repeatedly. A duplicate name across two override files lets a record
**silently fall back to a stale value**: the render picks one, you assume it picked the other,
nothing errors, and the wrong URL publishes.

### 15.4 Gate C11 — every override name must match exactly one published record

Two silent failures were caught this way. Both would have written rows that matched **nothing** and
**reported success**:

- a **curly apostrophe** (U+2019) in `Chris Lisciandro's`
- a **truncated name** — `Dan Henderson's Athletic Fitness Center` is really
  `… - Formerly Team Quest`

Match against the published record list exactly, byte for byte. **Do not normalise the comparison
to make the gate pass** — normalising away apostrophes and suffixes hides precisely the defect the
gate exists to find. If a name will not match, the name is wrong; fix the name.

### 15.5 The override files

Six files: `tjjm-gym-websites` through `tjjm-gym-websites-6`, each under its own ~24,576 B Admin
API rewrite ceiling (which is why there are six of them — see §5).

**Fill order is 1 → 6.** Later files win on precedence, **but that must never be relied on.**
Gate C3 means no name should exist in two files, so precedence should never be deciding anything;
if it ever does, C3 has already been violated.

Current headroom against the ceiling:

| file | headroom |
|---|---|
| 1 | **339 B** |
| 2 | ~2,639 B |
| 3 | **838 B** |
| 4 | ~1,632 B |
| 5 | ~22 KB |
| 6 | ~18 KB |

**Put new work in file 6.** Files 1 and 3 are effectively full — a handful of rows will overrun
them, and an overrun is a failed rewrite, not a truncation you can spot in a diff.

**When file 6 fills, add file 7** and wire one `{%- render -%}` into **each** of
`sections/tjjm-state-directory.liquid` **and** `sections/tjjm-gym-directory.liquid` (§14.2). A file
rendered from only one section produces overrides that apply on one surface and not the other —
the exact defect §14 exists to prevent.

## 16. Audit coverage — the honest position

State this plainly; do not soften it in reporting. Measured 16 Aug 2026; full working in
`AUDIT-COVERAGE-where-we-actually-are.md`.

Of the **live** links:

| evidence behind the link | share |
|---|---|
| **browser-verified** — a real Chrome load, page read | **~6%** |
| page body read by the **cache-prone fetcher** (§11.1) | **~41%** |
| **never had its page opened at all** — DNS and parking check only | **~47%** |

The **identity pass** is working through that 47%. **The first 360 found 21% had a problem** — the
largest classes being **9% suspect, 5% aggregator, 4% wrong-city.** That rate is the best current
estimate of what is hiding in the rest of the unread population.

The directory is:

- **Safe.** The actively harmful links — casinos, gambling farms, pharma spam, for-sale landers,
  dead registrations — are gone. That was the original harm and it is addressed.
- **Comprehensive.** Coverage is not the problem.
- **Not yet accurate.** Roughly half the links have never been looked at by anything that reads a
  page.

**"Every link has been checked" is true only of DNS.** Any report that implies more than that is
overstating the position, and §11.5 is the list of what DNS cannot see.
