# Handoff: CA 460 · TX 352 · FL 329 · NJ 211 · AZ 173 · CO 156 · GA 152 · PA 148 · MA 140 · VA 137 · OH 137 · IL 130 · NC 125 · WA 121 · OR 118 · NV 118 · MI 115 · LA 103 · MO 99 · OK 98 · MD 94 · WI 85 · CT 85 · IN 80 · AL 78

**That header is a TOP-25 LEADERBOARD, not a done-list.** It sums to 3,844 of 4,519; the other
675 live in smaller regions. The real shipped/unshipped split is at the bottom of this file.

Total **4,512** across **61 regions**. ~~4,519~~ superseded 6 Aug 2026.

MAIN is **"Aug 6 BJJ Gyms YY — 1b/1c/2 verification: 7 suppressions + 2 link fixes"**
(`gid://shopify/OnlineStoreTheme/154658242732`), **published 6 Aug 2026**.

**Post-publish verification, 6 Aug — all green.** Swept all 61 live pages cookie-free
(`credentials:'omit'`, no preview param — see METHOD CORRECTION 7; the bug is used deliberately
here, because a cookie-free fetch is guaranteed to render the *published* theme even if a preview
cookie is still set). Results: **total `numberOfItems` = 4,512**; `numberOfItems` = card count =
body header on **all 61**; the 5 changed regions read FL 328 · LA 100 · MO 98 · NJ 210 · TX 351
with **meta description matching the page on every region**; both link fixes live, both old URLs
gone. Files JSON, theme and metafields now agree — no inconsistency window remains.

**Themes to clean up:** `154658209964` ("BEFORE baseline — MAIN/XX snapshot") and the old MAIN
`154653950124` (XX) are both now disposable. Keep XX a little longer if you want a rollback
target; the baseline has served its purpose.

---

## How to write in this file

Every false lead in this project so far came from a sentence that asserted more than its evidence
supported. The conventions below exist to make that failure visible at the point of reading.
**Follow them when you add to this file.**

1. **Put the sample size in the sentence.** "Validated" is not a claim; "validated on NJ only,
   1 of 61 regions" is. A bare count with no denominator has caused four separate errors here.
2. **Use different verbs for measured, inferred, and assumed.** Measured: "the dump returns
   1,304." Inferred: "which implies." Assumed: "presumably — unverified." The 516 figure survived
   because it was written in the same confident voice as numbers that were airtight.
3. **Date every number and name its source.** Numbers rot: `1,712 http://` was true pre-XX and
   wrong after, with nothing in the text to signal it had an expiry.
4. **Bind a conclusion to its method in the same breath.** "0 mixed-case hosts" outlived "scanned
   via `URL.hostname`" because they sat in different paragraphs. Written together, killing the
   method kills the claim.
5. **Give structural blind spots more room than findings.** Findings can be re-derived; a gap that
   exists by construction cannot be noticed by working harder.
6. **Strike superseded text, don't delete it** — with the reason. Deleting loses the record of
   what was believed and why it was wrong, which is the only thing that prevents a rerun.
7. **Match modality to evidence.** "`fileUpdate` is blocked" became a standing constraint on one
   occurrence and cost a full rebuild. "Blocked once, succeeded on retry, cause unknown" is the
   honest form.
8. **Put the warning next to the action, not in a general-notes block.** Someone executing step 11
   will not scroll up 300 lines.
9. **Say what you did not check.** Silence reads as absence of a problem. Every run should end
   with an explicit non-coverage list.
10. **Rules in imperative present; findings in past tense with a date.** Otherwise rules read as
    anecdotes and anecdotes harden into rules.

# >>> FILES JSON — DONE (5 Aug 2026, 19:23Z) <<<

**Resolved.** `tjjm-gyms.json` is now **4,519 records across 61 regions**, 488,754 B, verified
byte-identical to the local build at the new `?v=`. Theme and file agree.

`fileUpdate` **was not blocked this time** — same approach, no userErrors. Treat the earlier
classifier block as situational, not a standing restriction.

What shipped: 27 record changes + 1 removal, and nothing else. MZ removed (CA 461→460);
Evolution renamed; the 11 `tjjm-gym-websites` overrides applied incl. the blanked link; **15
records reassigned NE → NL**.

**The file was missing Newfoundland entirely** — 60 regions, not 61, with NE carrying the
un-split union of 27. Neither this handoff nor the audit knew. Fixed.

## The old rebuild procedure was wrong — do not reuse it

The instruction to "rebuild the six changed states from rendered ItemList JSON-LD, validated by
reproducing one unchanged state byte-for-byte" **is unsound**, for two compounding reasons:

1. **Rendered JSON-LD does not round-trip to stored values.** The section prepends `https://` to
   scheme-less `w`, substitutes `tjjm-gym-websites` overrides, and fills blank addresses from
   `tjjm-gym-addresses`. Rebuilding from it would have silently rewritten **~1,076 records**
   (821 gaining an address, 277 gaining a scheme) when XX changed about 13.
2. **The one-unchanged-state gate passes on unrepresentative regions.** NJ round-trips perfectly
   because its records already carry full URLs and addresses. It is one of only 12 such regions;
   the method is wrong for the other 49. The gate validated clean while the method was broken.

**Replacement: rebuild all 61, diff against the current artifact, assert exactly the expected
regions differ.** Same cost, actually verifies the claim. Source stored values from
`tjjm-gyms.json` or the audit dump — never from a rendered page.

*Open question: nothing is known to consume this file. If nothing does, the enriched version
(821 addresses + 277 schemes) is strictly better and should be applied as its own reviewed pass.*

---

# >>> METHOD CORRECTIONS — READ BEFORE ANY VERIFICATION <<<

**Six** assumptions have now been found wrong. Each produced a clean-looking false result, so
none of them announced itself. 1–4 were found 5 Aug during the XX build; 5–6 were found 5 Aug
during the Files JSON re-sync.

Each correction below states the method that produced the false result, so that invalidating the
method invalidates the claim with it.

1. **`?preview_theme_id=` sets a cookie** (found: sweep reported 0 changed regions on a build
   that had changed 6). The param *also* sets a preview cookie, so any **unparameterised** fetch
   afterwards renders the last previewed theme. A sweep fetching "live, no param" against
   "preview, with param" compares the preview theme **to itself** and reports a perfect silent
   pass. Re-confirmed 5 Aug: the param is consumed and the browser redirected to the clean URL,
   leaving the cookie set.
   → **Always pass an explicit `preview_theme_id` on BOTH sides**, and keep a pre-change duplicate
   of MAIN as the "before" theme.

   **Scope of the damage, corrected.** The old note said "every past state's double-sweep may have
   verified nothing." That overstates it. The 5 Aug audit independently reconciled all 61 regions
   against `tjjm-region-index` and matched `numberOfItems` to card count on all 61, so **a whole
   import silently failing to apply is ruled out**. What remains unverified is **count-neutral
   edits** in the 27 shipped states — renames, address fixes, URL corrections, suppress+add pairs
   — which reconcile identically whether or not they applied. That is a targeted spot-check
   against `tjjm-statedir-notes-<code>`, not a 61-region re-sweep.

2. **Storefront responses are cached** (found: sweep reported TX unchanged when TX had changed
   correctly, with correct params but no `&cb=`).
   → Append a unique cache-buster to every fetch in a sweep.

3. **Hostname normalisation destroys the evidence for link defects** (found: normalising made
   `tsk.com/locations/nj/hoboken/` and `tsk.com/` identical, so 18 NJ records looked like they
   pointed at a homepage when **17 of 18** already had correct per-location URLs; a "38
   brand-root records" estimate collapsed to **11** on inspection).
   → **Inspect raw `w`, never the normalised domain,** before claiming a link is wrong.

4. **`URL.hostname` lowercases, so it cannot detect case defects** (found: a scan using it
   reported "0 mixed-case hosts anywhere" and concluded the class could be dropped from future
   scans). Raw-string re-scan of all 4,173 records carrying a website, 5 Aug: **3** mixed-case
   hosts. The conclusion died with the method.
   → **Test the raw string.**

5. **Rendered JSON-LD is not the stored record** (found 5 Aug while rebuilding the Files JSON).
   `sections/tjjm-state-directory.liquid` prepends `https://` to scheme-less `w`, substitutes
   `tjjm-gym-websites` overrides, and fills blank `a` from `tjjm-gym-addresses`. Rebuilding stored
   data from rendered output would have rewritten **1,076 of 4,519 records**.
   → Use rendered output to verify **what the site publishes**; use `tjjm-gyms.json` or the audit
   dump for **what a record stores**. Never cross them.

6. **"Validate on one unchanged sample" is not a validation** (found 5 Aug: NJ reproduced
   byte-for-byte and the method was still wrong for 49 of 61 regions). The gate passes on any
   sample where the transforms in 5 happen to be no-ops; **12 of 61** regions qualify.
   → **Validate across the whole population and assert the expected diff.** In this corpus that
   is one fetch loop, so there is no cost argument for sampling.

---

# >>> THE COLLISION RULE <<<

> **The canonical statement of this rule now lives in `RULES-tjjm.md` §1, with its evidence.**
> What follows is the summary and the correction history. Where the two differ, RULES is newer.

**The rule: keep the record that names a real current entity; drop the generic city-stub or the
stale former name.** Provenance (legacy vs MatMade) does not decide it. Location does not decide
it. Both are correlates that track the real signal most of the time.

**Two earlier formulations are superseded, not deleted — keep them visible so the reasoning that
killed them is not re-derived from scratch:**

- ~~"Keep the legacy record"~~ — wrong in 28 of 29 cases.
- ~~"Different city → suppress legacy; same location → keep legacy"~~ — first half right for the
  wrong reason; second half wrong, see below.

### Detection (measured 5 Aug 2026, all 27 shipped states)

- Name collisions (`legacyNames ∩ keptNames`): **0 of 40**
- Domain collisions (`legacyDomains ∩ keptDomains`): **40**, across 19 states

The name-only check found **none** of the 40. **Run both, always** — and see the four blind spots
below for what neither check can reach.

### Why the location formulation failed

Re-derived from live data 5 Aug 2026 via the rebuilt audit dump, the 29 collisions split
**8 cross-city / 20 same-city / 1 reverse**. The audit's own B1/B2 tables contained two
misclassifications that swapped, so the 9/20 counts looked right and nobody checked:

- `OR oregonbjj.com` was filed same-city; it is **cross-city** (Eugene vs Hillsboro).
- `GA sakurabjj.com` was filed cross-city; it is **same-city** (Woodstock vs Woodstock).

Two consequences:

- **"Legacy wrong 10 times out of 10" double-counts Oregon.** Oregon is one of the cross-city
  cases, not an extra one. Verified cross-city evidence is 8.
- **"Same location → keep the legacy record" is wrong.** It rests on the single CA case while
  **20 same-city counterexamples** sit in the same dataset, filed as "cosmetic, no action". In
  all 20 the legacy record was a generic `<City> BJJ` stub and suppressing it was correct.

### FOUR blind spots a collision check CANNOT see

1. **Never-imported duplicates** (`ashlandbjj.com`). Only a re-diff against MatMade source finds these.
2. **Same-city duplicates on different domains** — `cjjftx.com` vs `cjjfntx.com`. **Confirmed one
   school** by the acronym pass, 5 Aug.
3. **Multi-tenant hosts are excluded from matching** (facebook, mindbody, squareup, linktr, site
   builders), or every Facebook-linked gym false-positives against every other. Two records
   genuinely sharing one Facebook page cannot collide.
4. **Single-record brand roots.** A collision needs two records — `GB South Shore` and
   `UFC GYM Boston Financial District` are wrong links no intersection will surface.

**Corollary:** all 29 adjudicated cases are ones where a curator had *already* suppressed the
legacy record. The population where the old rule was applied is invisible by construction, so any
"N out of N" statistic from this set tests the curators, not the rule.

---

# >>> DON'T TRUST TITLES OR AGGREGATORS <<<

`tjjm-region-index`'s header already says never to trust a `<title>` or meta description.
**Extend that to third-party sites and directories.**

`evolutionlowell.com`'s `<title>` still reads "Gym in Lowell and Tewksbury", and businessyab,
beakid and bjjweb all still list 910 Andover St, Lowell with its own phone number. The rendered
page body mentions Lowell **zero times** and carries one address — 540 Main St, Tewksbury. The
Lowell site consolidated years ago. Three directories agreed on a location that no longer exists.

**Open the page and read the body.** It reversed a verdict this run.

Related: a wrong URL can resolve perfectly and still belong to someone else.
`Unconventional Performance & Training` /New Braunfels carried `rodrigopinheirobjj.com`
(a San Antonio school) — and `gyms.jiujitsu.com` carries the identical error, so it is upstream,
not a MatMade slip. **Link-checking cannot catch this class; only reading the page can.**

---

# >>> NEW MECHANISM: WEBSITE OVERRIDES <<<

`snippets/tjjm-gym-websites.liquid` — same `~Name|Value~` idiom as `tjjm-gym-addresses`.
An override **beats** the record's own `w`; an **empty value blanks the link**.

It exists because affected records often live in `snippets/tjjm-gyms-data.liquid` — the 113 KB
legacy blob the Admin API can only rewrite whole. An override costs ~2 KB instead.

**Rule: only add an entry that CHANGES something.** Restating a URL the record already has turns
this file into a second source of truth that silently pins the old value if the record is later
corrected. Diff against live data first.

The section consults it right after `g_web` is parsed. Section is now **12,485 B**
(was 12,028) — still far under the ~24 KB rewrite ceiling.

---

# >>> RUN LOG <<<

## Run of 5 Aug 2026 (afternoon) — collision audit + theme XX

1. **Corpus-wide domain collision audit**, all 27 shipped states — 40 domain hits, 0 name hits.
2. **Adjudicated 9 suppressions — 9/9 correct.** No real school was deleted anywhere.
   *Correction (5 Aug evening): these were described as "9 cross-city cases". Re-derivation shows
   8 were cross-city and 1 (`GA sakurabjj.com`) was same-city. The 9/9 verdict stands; the
   characterisation of the set does not.*
3. **Investigated 3 both-live anomalies** — 1 duplicate (CA MZ), 1 wrong-entity link (TX), 1
   multi-location brand needing repointing (FL Fabin Rosa).
4. **Brand-cluster sister-site pass** — 18 net-new leads, 6 stale records, 11 real link fixes.
   *Correction (5 Aug evening): the 18 is unreliable in both directions — see item 3.*
5. **Built and published theme XX**: CA 461→460, Evolution record corrected, 11 link fixes.
6. **Definitive shipped/unshipped split established** (below) — the old header was a leaderboard.

## Run of 5 Aug 2026 (evening) — Files JSON, harness rebuild, rule correction

1. **Closed backlog item 0.** Files JSON re-synced to 4,519 / 61 regions. `fileUpdate` succeeded;
   it is not reliably blocked. Found and fixed a defect neither document knew: **the file was
   missing Newfoundland entirely** (60 regions, NE carrying the un-split union of 27).
2. **Found the rebuild procedure in step 11 unsound** on two independent grounds — see METHOD
   CORRECTIONS 5 and 6. Replaced it in place.
3. **Rebuilt the audit-dump harness** after discovering the old scratch theme had been deleted.
   Simpler than the original and it reconciles without the −27 NE/NL correction.
4. **Closed backlog item 1** as a detection pass. Plain name similarity does not work; same-address
   and acronym expansion do. 6 candidates raised for verification (item 1b).
5. **Corrected the collision rule** from location-based to entity-vs-stub, on 29 re-derived cases.
6. **Re-measured 4 defect classes from raw stored values.** Scheme-less is 286, not 516.
   Mixed-case is 3, not 0. `http://` is 1,706, not 1,712.
7. **Wrote `RULES-tjjm.md`** as the durable home for rules + evidence.

### What this run did NOT check

Stated explicitly, because silence reads as absence of a problem:

- **The 20 same-city collisions were not individually re-verified.** Their *classification* was
  re-derived from live city data; the underlying keep/suppress verdicts still rest on the earlier
  audit's review.
- **No count-neutral edit from any past state was spot-checked.** The exposure in METHOD
  CORRECTIONS 1 remains entirely open.
- **The 18 brand leads were not re-diffed** despite item 3's count being known unreliable.
- **The 6 stale records (item 2) were not verified.** Untouched this run.
- **Nothing was suppressed, renamed, or link-fixed.** The only write to production this run was
  the Files JSON.

## Run of 6 Aug 2026 — backlog 1b / 1c / 2 verified, theme YY built (NOT published)

1. **Closed items 1b, 1c and 2** — 14 candidates, every one adjudicated by **opening the school's
   page and reading the body**. Net: **7 suppressions, 2 link fixes, 3 false positives, 1 record
   confirmed defective but unfixable, 1 new lead.**
2. **The two "stale record" reversals are the headline.** `Gracie Jiu - Jitsu Summerlin` and
   `American Top Team Aventura` were both on item 2's suppress list and **both are live schools**.
   Item 2 had described each accurately (a wrong-entity link; a wrong city) and then filed them
   under "verify, then suppress" anyway. See the warning under item 2.
3. **Built theme YY** and verified it with a corrected double-sweep (below). 55 of 61 regions
   byte-identical, exactly the 6 expected regions changed, exactly the expected deltas,
   `numberOfItems` = card count = body header on all 61, total 4,519 → 4,512.
4. **Re-synced the Files JSON in the same run.** 4,512 records / 61 regions / 487,965 B, re-fetched
   at the new `?v=` and **byte-identical to the local build**. `fileUpdate` **was not blocked** —
   second clean run in a row, which further supports "situational, not a standing constraint."
5. **Found METHOD CORRECTION 7** (below) — the first double-sweep of this run was worthless and
   said so loudly, which is the only reason it was caught.
6. **Corrected a claim in RULES §3**: `tjjm-gyms.json` is *not* raw stored values; it has website
   overrides applied. Proved via the blank-override record. Only the audit dump is raw.

### METHOD CORRECTION 7 — `credentials:'omit'` silently defeats `preview_theme_id`

Found 6 Aug: the first sweep reported **all 61 regions changed with every count identical** and a
total of 4,519 → 4,519 on a build that had removed 7 records. Cause: the sweep fetched with
`credentials:'omit'`. Shopify consumes the param, sets a **preview cookie** and redirects to the
clean URL — with credentials omitted the cookie is never stored and **the live theme renders on
both sides**. Same failure as METHOD CORRECTION 1, reached by a new route, and it survives having
the param explicitly on both sides. Measured on one page: `omit` → 103, `include` → 100.

Second cause found in the same diagnosis: the preview cookie is **one shared value per origin**,
so concurrent workers alternating BEFORE/AFTER race each other. **The sweep must be sequential.**
61 × 2 sequential fetches ≈ 2 minutes.

→ **`credentials:'include'`, concurrency 1, param on both sides, unique `cb` on every fetch.**
→ **A sweep where every region differs, or none does, is a broken sweep, not a result.** Assert
the expected total explicitly; that assert is what caught this.

### What this run did NOT check

- **The 3 false positives were not re-diffed against MatMade source.** Blind spot 1 still applies:
  `FRBJJ Lake Nona`, `Stockwell Martial Arts Academy` and the Alliance pair could each still have
  a never-imported twin.
- **`Alliance Jiu Jitsu San Diego` vs `Alliance San Diego` was surfaced but not verified** (1b-follow-up).
- **No `tjjm-statedir-notes-<code>` file was written or updated** for FL, LA, MO, NJ, TX or NV.
  Step 7 asks for per-state rationale; this run put the rationale in the backlog rows and in the
  `tjjm-gym-websites` header comment instead. **Owed.**
- **The 20 same-city collisions, the 18 brand leads, and the count-neutral-edit exposure from
  METHOD CORRECTION 1 are all still untouched** — carried forward unchanged from 5 Aug.
- **Items 4–17 were not touched at all**, except that 5b lost one mixed-case host (now 2, not 3:
  `NV Atlas Grappling` and `CO Morning Star Jiu Jitsu`) and item 6 gained a known-good target.
- **Nothing was published.**

---

# >>> BACKLOG <<<

**0. ~~Re-sync the Files JSON.~~ DONE 5 Aug 19:23Z.** See top.

**0c. NEW (6 Aug) — three records need a field that NO override can reach.** `tjjm-gym-websites`
overrides `w`; `tjjm-gym-addresses` fills a **blank** `a` only. Nothing overrides `c`, and nothing
overrides a **non-blank** `a`. All three below therefore need a snippet rewrite and are parked:

| record | defect | correct value (verified from the site body, 6 Aug) |
|---|---|---|
| `Elite Martial Arts-Richmond` /Paducah KY | wrong city AND wrong address — see 1c below | c=Richmond, a=2008 Merchant Dr Ste 5 |
| `American Top Team Aventura` /Miami Beach FL | wrong city (link fixed in YY) | c=North Miami Beach (16215 Biscayne Blvd) |
| `SMAA/Soul Fighters SBC, Brazilian Jiu Jitsu` /Bossier City LA | stale address | a=1156 Airline Dr (site says so; record says 3068 Knolin Dr bldg 1) |

*Also worth a rename in the same pass: that LA record now trades as **Synergy Martial Arts
Academy** (`info@shreveportmaa.com`). Renames are not overridable either.*

**0b. NEW — Files JSON enrichment (decide, then apply).** Split out of item 0 deliberately. The
rendered pages carry a street address for **821** records the file has no `a` for, and a scheme
for **277** stored scheme-less. Both are arguably improvements but amount to ~1,098 unreviewed
record changes. Blocked on: *what consumes this file?* If nothing, apply.

**1. ~~Name-similarity pass within city.~~ DONE as a detection pass, 5 Aug.** Findings below;
verification is now item 1b.

Method notes, because the obvious approach fails: **plain name similarity does not work** —
Jaccard produced 373 candidates, almost all noise, and scored the CJJF pair at 0.2, missing the
one case the item existed for. Two other signals did the work:

- **Same street address within city** (28 pairs). Correctly reproduced all three known Oregon
  shared-building verdicts, which calibrates it.
- **Acronym expansion** — initials of one name vs a short all-caps token in another. The only
  signal that catches `CJJF` ↔ `Caveirinha Jiu-Jitsu Family`. **Needs a generic blocklist**:
  `BJJ`/`MMA` matched everything and produced 28 of its 30 hits.

**1b. ~~Verify 6 duplicate candidates.~~ DONE 6 Aug 2026.** All six opened and read in the body,
never decided from search results or `<title>`. **3 duplicates, 3 false positives.**

| state / city | pair | verdict (6 Aug, from the site body) |
|---|---|---|
| FL /Fort Lauderdale | `Gracie Barra Fort Lauderdale / BJJ Fort Lauderdale FL 33306` vs `Gracie Barra Fort Lauderdale` | **DUPLICATE — suppressed the stuffed name.** Identical `c`, `w` and `a` on both records. GB's page shows ONE school, 5439 N Federal Hwy, and the ZIP baked into the stuffed name (**33306**) is wrong — the school is **33308**. |
| LA /Baton Rouge | `Bayou Jiu Jitsu & Self Defense Baton Rouge` vs `Bayou Jiu Jitsu & Self Defense` | **DUPLICATE — suppressed the bare name.** `bayoujiujitsu.com` 301s to `bayoujiujitsu.us`; one school, and the survivor carries the address. |
| FL /Orlando | `FRBJJ Lake Nona` vs `Fabin Rosa Brazilian Jiu Jitsu Academy` | **NOT a duplicate.** Lake Nona is a real separate site — own phone (321) 270-9809, serves Lake Nona/East Park/Lee Vista, 7466 Narcoossee Rd vs 4085 L B McLeod Rd. Acronym false positive. |
| LA /Bossier City | `SMAA/Soul Fighters SBC` vs `Stockwell Martial Arts Academy` | **NOT a duplicate — the acronym expands to something else entirely.** SMAA = **Shreveport/Synergy** Martial Arts Academy (`info@shreveportmaa.com`, 1156 Airline Dr), not Stockwell. Different entity, different address. |
| TX /Prosper | `CJJF Academy - North Texas` vs `Caveirinha Jiu-Jitsu Family Texas` | **DUPLICATE — suppressed.** CJJF's own locations page lists ONE Prosper school (2361 E. University Dr Ste 70). `cjjfntx.com` is a **dead domain**; the record's 2111 E University Dr Ste 60 is stale. |
| CA /San Diego | `Legion AJJ` vs `Alliance Jiu Jitsu San Diego` | **NOT a duplicate.** AJJ = **American** Jiu-Jitsu. Legion is Keenan Cornelius's academy, 7550 Miramar Rd Ste 330 — matches the record exactly. Unrelated to Alliance. |

*Calibration note: the acronym signal went **1 for 3** here (CJJF right; SMAA and AJJ both wrong,
each because the acronym expanded to a word that was not in the candidate name). It is a
**candidate generator, not evidence** — every hit needs the page body.*

**1b-follow-up. NEW — unverified pair surfaced while checking Legion:** `Alliance Jiu Jitsu San
Diego` (no address) vs `Alliance San Diego` (8990 Miramar Rd #225), same city, different domains.
Not checked — it was outside the six. ~1 search.

**1c. ~~Two name/city contradictions.~~ DONE 6 Aug 2026.** Both confirmed defective; **only one
was fixable this run.**

- **`10th Planet St. Louis` /Washington MO — SUPPRESSED.** Four independent signals: the domain
  `10thplanetstl.com` is **dead**; 10P's own affiliate list (read in full — it carries 3 other MO
  entries: Crystal City, Kansas City, Sedalia) has **no** St. Louis and no Washington MO; the STL
  presence rebranded to **River-City Warriors**, 1721 S 7th St, St. Louis; and its stored address
  **416 E Fifth St is the live address of `Center of Defensive Arts`**, already in the directory
  (its site body confirms 416 East 5th Street, Washington MO 63090). Textbook §1: stale former
  name vs real current entity at one address.
- **`Elite Martial Arts-Richmond` /Paducah KY — CONFIRMED DEFECTIVE, NOT FIXED.** This is worse
  than a name/city contradiction: the record **fuses two unrelated schools.** `elitema.org`'s body
  serves **Richmond (2008 Merchant Dr Ste 5) and Winchester** only and mentions Paducah **zero
  times**. Its stored address, 451 Jordan Dr Paducah, belongs to **XLR8 Martial Arts**
  (`xlr8paducah.com`, body confirms Paducah) — and `Premier Martial Arts – Paducah`, **already in
  the directory**, is stored at that same 451 Jordan Dr. Fixing it needs `c` and a non-blank `a`,
  neither of which is overridable → parked in item **0c**. Suppressing was rejected: Elite
  Martial Arts Richmond is a real school and would be lost.

*(`FRBJJ Lake Nona` also invalidates item 3's lead count — the warning is stated there, at the
point of use.)*

**2. ~~Verify the 6 stale records, then suppress.~~ DONE 6 Aug 2026.** Verifying **reversed the
verdict on 2 of the 6** — both were live schools with a bad link, not dead gyms. Suppressing this
list unverified, as written, would have deleted two real academies.

| state | record | verdict (6 Aug, from the site body) |
|---|---|---|
| LA | `UFC Gym New Orleans` | **SUPPRESSED.** Enumerated UFC GYM's **own sitemap** — 80 US club pages, and the only Louisiana entry is `/locations/sherwood`. Whole-population check, not a sample. |
| LA | `UFC GYM Acadian, Baton Rouge` | **SUPPRESSED.** `ufcgym.com/acadian` and `/locations/acadian` both 404 while `/locations/sherwood` returns a full page. Absent from the sitemap. |
| NJ | `Tiger Schulmann's Clifton` | **SUPPRESSED.** `tsk.com/locations/nj/clifton/` → *Page not found*, while the per-location URL pattern resolves for the other 17 NJ records. |
| NV | `Gracie Jiu - Jitsu Summerlin` | **VERDICT REVERSED — do NOT suppress; link fixed.** The school is **live**: `graciejiujitsusummerlin.com` states 5375 S Fort Apache Rd Unit 104, **exactly the address the record already stores**. Only the link was wrong. Override → `https://graciejiujitsusummerlin.com/`. Also clears 1 of the 3 mixed-case hosts (5b). |
| TX | `CJJF Academy - North Texas` /Prosper | **SUPPRESSED** — same case as 1b row 5. |
| FL | `American Top Team Aventura` | **VERDICT REVERSED — do NOT suppress; link fixed.** `attaventura.com` is now a **GoDaddy "available at auction" parking lander**, but the school is live as **ATT Aventura/NMB** (`attaventuranmb.com`, body: "Premier martial arts in Aventura & North Miami Beach"). Yelp flags the old listing CLOSED — aggregator noise, contradicted by the body. City still wrong → item 0c. |

⚠️ **Read this row pattern before writing another "verify, then suppress" list.** A dead *link*
and a dead *gym* look identical from the outside, and this list conflated them in 2 of 6 cases.
A parked domain, a 404 on a brand's per-location URL, and a Yelp CLOSED flag are each evidence
about **the link**. Only the school's current page — found by searching for the school, not by
following the stored URL — is evidence about the school.

**2b. NEW — UFC GYM is now entirely unrepresented in Louisiana.** Both LA records were suppressed
and **UFC GYM Sherwood** (4520 S Sherwood Forest Blvd Ste 110, Baton Rouge 70816) is not in the
directory at all. One add, address already verified.
*Also from the same sitemap: `/locations/boston-financial-district` exists, so item 6's
`UFC GYM Boston Financial District` → `ufcgym.com` brand-root link has a known correct target.*

**3. 18 net-new leads — but re-derive the count before planning against it.** Addresses and
liveness needed. Arizona dominates — treat as an AZ top-up run, not cleanup.

⚠️ **The 18 is unreliable in BOTH directions.** Evidence, 5 Aug: the table below records Fabin
Rosa as "4 locations, 2 in directory". In fact a **third** record is already in the directory
under an acronym (`FRBJJ Lake Nona`, found by the item-1 acronym pass, invisible to a name or
domain diff), at a **fifth** location absent from the brand's own locations page. So the roster
undercounted the brand's real locations *and* the directory-side diff missed an existing record.
Both error directions in one brand. **Re-diff each roster against the whole state — never against
the collision cluster — and treat the brand's own locations page as incomplete, not
authoritative.** Until that is redone, 18 is a lower bound on leads and an upper bound on
confidence, not a work estimate.

| state | brand | missing |
|---|---|---|
| AZ | Gracie Barra (19 real; 10 in directory) | Arcadia /Phoenix · Ahwatukee /Phoenix · McCormick Ranch /Scottsdale · Scottsdale · North Phoenix · Maricopa · Anthem /Phoenix · Marana · Vail /Tucson |
| NJ | Tiger Schulmann's (20; 18) | Cherry Hill · Marlton · East Hanover |
| TX | CJJF / Caveirinha (5; 2) | Melissa · McKinney · Celina |
| FL | Fabin Rosa (4; 2) | Belle Isle · Casselberry |
| FL | American Top Team (11 FL facilities) | Coral Springs |

**4. Re-probe every past state's links — `http://` handled correctly.** **1,706** live records use
`http://` (37.8% of the corpus; supersedes 1,712, which was pre-XX). Against 2,181 on `https://`.
**Use the corrected sweep methodology (see METHOD CORRECTIONS) or the results are worthless.**

**5. Scheme-less URLs: the real number is 286, not 516.** Re-counted 5 Aug from **raw stored `w`**
in the post-XX Files JSON. The 516 figure was wrong — and it is not explained by suppressed
records, which all carry `https://` (0 scheme-less, 0 `http://` across all 346). They render fine
since the section prepends `https://`, so this stays cosmetic.

**5b. Mixed-case hosts: ~~3~~ → 2 as of theme YY.** `NV Atlas Grappling`
(`http://www.AtlasGrappling.com`) and `CO Morning Star Jiu Jitsu` (`http://www.MorningStarJJ.com`).
~~`NV Gracie Jiu - Jitsu Summerlin` (`http://GracieLasVegas.com`)~~ — fixed 6 Aug by the item-2
link override; it was a wrong-entity link, and the replacement is lowercase. Full raw-string scan also shows
**0** trailing `%20`, **0** `facebook.com/login`, **0** `w` = `n/a`, and **15** names carrying an
en/em-dash. 4,173 of 4,519 records have a website; 346 have none.

**6. Bare multi-tenant hosts — SCOPED, still OPEN (4 records).** Scanned all 27 shipped states
5 Aug: **exactly 4 records, all in MA** — `clients.mindbodyonline.com` (USMMA), `squareup.com`
(Jiu-Jitsu USA), `m.facebook.com` (Team Link Marlborough), `facebook.com` (Mass Best). **No other
state has one.** The scope question is settled; the work is not done. Four-record job.
*(41 further records use site-builder homepages — `business.site`, `gymdesk`, `weebly`,
`wordpress`. Those are legitimate, not defects.)*
*Also: MA has two brand-root links the collision audit missed because they don't collide —
`GB South Shore` → `graciebarra.com` and `UFC GYM Boston Financial District` → `ufcgym.com`.
Single-record brand roots are invisible to a collision check.*

**7. Re-probe every past state's legacy domains and OPEN the live ones.** Parked domains and
directories both score LIVE under `no-cors`. `portlandbjj.com` was a directory and yielded 6
leads; `bendbjj.com` was parked and worthless.

**8. Chase the 6 net-new Portland leads** from `portlandbjj.com`: American Top Team ·
Black Dog Jiu Jitsu Company · Black Wolf Academy · Eastside Grappling (`eastsidegrappling.com`) ·
Oregon Grappling Arts (`oregongrapplingarts.com`) · 10th Planet Portland.
**Re-diff by DOMAIN and ADDRESS, not name** — "American Top Team" and "10th Planet Portland" are
affiliation brands and are routinely listed under a local owner's name.

**9. Re-audit Oklahoma's review-based keeps.** ~30 OK records kept on review text assuming the
reviews belong to the record. MA, WI, WA and OR all proved they often do not.

**10. Add addresses to `snippets/tjjm-gym-addresses`** for the three MA legacy records whose
MatMade duplicates were dropped on a collision: Florian Martial Arts Center (17 Station St
Floor 4, Brookline), Paradigm Brazilian Jiu Jitsu (109 Industrial Ave E #3, Lowell), Boston
Brazilian Jiu-Jitsu Woburn (104 Main St). Format `~Name|Address~`.
*MA was curated in both directions — worth one consistency pass over MA specifically.*

**11. OR squeeze list** (~1 search each): **Full Force Mma /Aloha** — address stale, top of the
list. Then Eugene Jiu Jitsu Club (carries Newport's phone) · Combat Sports Center (ZIP
contradicts city) · White Panther /Astoria (soft keep) · Victory Gym /Albany (soft cut).

**12. WA squeeze list** (~1 search each): **AMC Kickboxing & Pankration /Woodinville** — kept on
merit (Matt Hume) but a Nov 2025 listing says "temporarily closed while evaluating a new
location". Then Urban Alliance /Brush Prairie · Cornerstone Jiu Jitsu /Silverdale ·
Gracie Jiu-Jitsu Mukilteo (URL unresolvable) · Connection Rio /College Place (domain dead).
**`Connection Rio Jiu-Jitsu Academy` /Bend is LIVE in the OR set with 158 reviews — resolve
both together.**

**13. WA soft calls, reversible** (detail in `tjjm-statedir-notes-wa`): Elite Martial Arts
Training Centers /Puyallup · Lenderman Academy /Spanaway · Black Belt USA Battleground MMA
/Lakewood · East West Martial Arts /Vancouver · Alpha Martial Arts /Seattle.

**14. Check for stale addresses on schools whose sites you open.** Three in WA, at least one in
OR. Likely widespread.

**15. Re-verify the 40 NJ records never independently checked**; check `nj_removed` vs snippet −19.

**16. Fix the name-only dedupe in `sections/tjjm-gym-directory.liquid`** (10,708 B — a DIFFERENT
file from the state directory). `sections/gym-finder.liquid` is a 152-byte unused placeholder.

**17. Load More backlog** — MatMade's Algolia index (`production_api::gym.gym`). **Deliberately
NOT used, needs explicit authorisation.** The gym sitemap already gives complete enumeration.

---

# >>> STILL TRUE <<<

- **Missing `postalCode` is a non-gym tell** — 2-for-2 in Oregon, both CTCs.
- **`programs` / `affiliation` are dead as curation signals.** Null on all 136 OR records.
- **Shared address may be a shared building.** 10 OR pairs, only 4 were true duplicates.
  Suffix-normalise before matching:
  `addr.toLowerCase().replace(/\b(unit|ste|suite|#)\s*[a-z0-9-]+\b/g,'').replace(/[^a-z0-9]/g,'')`
- **Zero-review records are NOT reliably cuts.** WA went 3-for-3 cut; OR split 4 keep / 4 cut.
  Do the search; don't assume the outcome.
- **Reviews are the best MatMade-side net-new source, and are often misattributed.**
- **Defect classes to scan for.** Counts measured 5 Aug 2026 from raw stored `w` in the post-XX
  Files JSON, n=4,519 records / 4,173 with a website. **Measured:** en/em-dash in names (15) ·
  scheme-less URLs (286) · mixed-case hosts (3, check the RAW string) · `w` = `n/a` (0) ·
  `facebook.com/login` (0) · trailing `%20` (0). **Not yet measured:** shared phones across
  cities · ZIP contradicting city · **name contradicting city** (2 known: `Elite Martial
  Arts-Richmond` /Paducah KY, `10th Planet St. Louis` /Washington MO) · wrong-entity social links.
- **`themePublish` is blocked by the connector. The user publishes.**
- **`fileUpdate` is NOT reliably blocked.** Blocked by the classifier on one run, succeeded
  cleanly on the next with no change in approach. Treat a block as situational: retry once, and
  report rather than working around it.
- **Never hand-transcribe signed upload parameters.** A retyped base64 policy caused a 400 on
  5 Aug. Decode and assert in-page first — `atob` → `JSON.parse` → check `key` and `x-goog-date`
  match what you were issued — *then* POST. Stash the `resourceUrl` in `sessionStorage` so a
  blocked `fileUpdate` is retryable without rebuilding; it can never be echoed back through the
  output filter, which is why the last run lost it.
- `bulkOperationRunMutation` is blocked; `currentBulkOperation` is shop-global.
- **`javascript_tool` truncates at ~1–1.3 KB.** Workaround:
  `document.body.innerHTML='<main><pre id="D"></pre></main>'`, set `textContent`, then
  `get_page_text`. ~11 KB per chunk reads back reliably.
- **The output filter BLOCKS results containing query-string/token-like data.** Strip query
  strings from anything you echo. (Upload signatures can be *passed in* safely; just never echo
  them back.)
- `location.host === 'chromewebdata'` is the one conclusive dead-domain signal.
- **The sandbox has NO outbound network at all** — not just matmade.com. `curl` to
  `thejiujitsumindset.com` and `cdn.shopify.com` both fail. Everything goes through the browser
  or the Shopify connector.
- **Prefer `WebSearch`**, which accepts several questions in one query separated by `;`. Pass
  `blocked_domains: ["matmade.com"]` on every verification search.
- **`themeFilesUpsert` is blocked on MAIN** — always duplicate first. `themeDuplicate` returns
  **`newTheme`** and takes ~30 s before files are readable.
- **`themeFilesCopy` to assets is vestigial** — skip it.
- Keep the scrape tab separate from the site-check tab. `window` state dies on navigation;
  `sessionStorage` does not.

## The audit-dump harness

**The old scratch theme `154652311724` was DELETED** — harness and the pre-XX "before" theme both
went with it. Checked every surviving theme; no copy exists. Rebuilt 5 Aug as:

**`SCRATCH — audit dump harness (5 Aug 26, post-XX)`**, `gid://shopify/OnlineStoreTheme/154657063084`,
duplicated from MAIN/XX. Holds `sections/tjjm-audit-dump.liquid` (3,373 B) +
`templates/page.tjjmaudit.json` (103 B). Fetch:

```
/pages/<handle>?view=tjjmaudit&preview_theme_id=154657063084&cb=<unique>
```

Emits `REMOVED|name|city|website|address`, records separated by `~~`, into `<pre id="D">`.

**Two deliberate changes from the original:**

1. **Legacy blob only** — one `render` tag instead of 34. Raw stored `w` for *live* records is
   already in `tjjm-gyms.json`, and suppressed records only exist in the legacy blob, so the
   per-state MatMade snippets add nothing the dump uniquely provides.
2. **It applies the NE/NL city split**, so it reconciles directly to 4,519. No more −27 correction.

`website` is the **RAW stored value** — no override applied, no `https://` prepended.

Validated on Oregon: 15 legacy records, 14 suppressed, `Ashland BJJ` kept — matches the audit
exactly. Corpus-wide: **1,304 legacy records, 346 suppressed, 958 live.**

⚠️ **This is a post-XX snapshot, so it is NOT a valid "before" theme.** The pre-XX baseline no
longer exists. For the next build, duplicate current MAIN as the "before" *before* making changes.

## Scraping playbook

buildId **`Rd7MR1U4ddxhWYs6pVmUV`** — valid 5 Aug 2026.
- Sitemap is `/sitemap/gym-sitemap.xml`, reached via `/sitemap.xml`. **`/gym-sitemap.xml` at the
  root 404s.** 7,311 URLs, 1.8 MB.
- Gym: `/_next/data/<buildId>/gyms/<slug>.json` → **`pageProps.gymData`**, no `.attributes`
  wrapper. `triton-fight-center` 404s permanently — do not retry.
- **`state`, `city`, `affiliation`, `secondaryAffiliation`, `instructors`, `programs`, `reviews`
  are RELATIONS** (`{data:{attributes:…}}`), often `{data:null}`:
  ```js
  const rel = v => (v && v.data && v.data.attributes) ? v.data.attributes : null;
  ```
  **`city` is a relation too.** `g.city || rel(g.city).title` silently yields `[object Object]`
  because the wrapper is truthy. Always go through `rel()`.
- Fire long loops async (`(async function(){…})(); 'started';`) then poll — the 45 s CDP limit
  kills the *call*, not the loop. Concurrency 12 crawls 7,311 in ~90 s.
- The JS REPL takes top-level `await`; an `(async()=>{})()` IIFE returns `{}`.

## Import sequence

1. **Crawl the gym sitemap** → in-state list; grep `/^[A-Z]{2}$/` on `state.title`; check for
   in-state ZIPs filed under other states; extract `city` through `rel()`.
2. **Duplicate MAIN** (writes are blocked on it) → `newTheme`; wait ~30 s.
3. **Probe every legacy domain, re-probe `http://` failures as `https://`, then OPEN every live
   one** — parked pages and directories both score LIVE.
4. **Diff new names against the live legacy page BEFORE writing — by NAME *and* by DOMAIN**, and
   for multi-location brands **also by ADDRESS**. Scan for the defect classes listed above.
5. **One search per zero-review record**, plus the address-verified review pass.
6. **Generate the snippet with a script, gate it in code, and assert the size Shopify reports
   matches the local artifact byte-for-byte.** Predict every size before writing.
7. `tjjm-statedir-notes-<code>.liquid` for rationale; removed names go in
   `snippets/tjjm-removed-index` (a new row), **NOT** in the section. Link corrections go in
   `snippets/tjjm-gym-websites`. Add `render 'tjjm-gyms-data-N'` to the section's capture list
   and **predict the new section size**.
8. Region index count + comment total.
9. **Preview-verify:** `numberOfItems` = card count = body header, `.tjjm-city-h` = cities + 1,
   0 dupes, 0 wrong-region, suppressed absent, survivors present. Then **double-sweep all 61**
   with **explicit `preview_theme_id` on BOTH sides** and a **unique cache-buster on every
   fetch**, and assert exactly the expected regions changed.
   ⚠️ **The "before" side must be a duplicate of MAIN taken BEFORE you changed anything.** No
   such baseline currently exists — the pre-XX one was deleted. Make it at step 2 or the sweep
   has nothing honest to compare against. Without both params the sweep compares a theme to
   itself and reports a silent clean pass (METHOD CORRECTIONS 1).
10. `metafieldsSet` using the verified number — `description_tag` **and** `title_tag`.
11. **Files JSON merge — same run.** `files(query: "filename:tjjm-gyms.json")` → fetch the CDN
    URL in the browser → **rebuild ALL 61 regions** → diff against the current artifact and
    **assert that exactly the expected regions differ** → `stagedUploadsCreate` (FILE/POST) →
    POST the FormData from the browser → `fileUpdate` with the `resourceUrl` → re-fetch at the
    new `?v=` and verify byte size against the local build.

    ⚠️ **Do NOT rebuild from rendered ItemList JSON-LD, and do NOT validate on one unchanged
    state.** Both instructions stood here until 5 Aug 2026 and both are wrong:
    - Rendered JSON-LD does not round-trip. The section prepends `https://` to scheme-less `w`,
      substitutes `tjjm-gym-websites` overrides, and fills blank `a` from `tjjm-gym-addresses`.
      Measured 5 Aug: rebuilding from it would have rewritten **1,076 of 4,519 records** (821
      address-added, 277 scheme-added, ~19 other) when the build had changed 13.
    - The one-unchanged-state gate passes on any region where those transforms are no-ops. NJ is
      one of **12 of 61** such regions; the method was wrong for the other 49 and the gate still
      validated clean.

    Source stored values from `tjjm-gyms.json` or the audit dump — **never from a rendered page**.
    Do NOT fetch the storefront `/files/…` path. Record shape `{n,c,s,w,a}` (`w`, `a` optional);
    `fileUpdate`'s immediate response reports the **old** `originalFileSize` — ignore it and
    re-query. Stash the `resourceUrl` in `sessionStorage` before posting; the output filter will
    not let you echo it back, so a blocked `fileUpdate` otherwise costs a full rebuild.
12. **User publishes** — the connector blocks `themePublish`.

---

# >>> SHIPPED vs UNSHIPPED (definitive) <<<

**27 states shipped** (have a MatMade import):
AL AZ CA CO CT FL GA IL IN KY LA MD MA MI MO MT NV NJ NC OH OK OR PA TX VA WA WI

**34 regions still legacy-only**, with current counts:
NY (64) · ON (40) · AR (35) · TN (34) · BC (26) · NS (23) · AK (22) · AB (22) · QC (21) ·
MN (18) · IA (15) · NB (15) · NL (15) · MS (14) · SC (14) · UT (14) · KS (13) · NE (12) ·
NM (12) · HI (11) · ID (11) · ME (11) · MB (11) · RI (11) · SK (11) · VT (11) · NH (10) ·
PE (10) · WV (10) · ND (9) · SD (9) · WY (9) · DE (7) · DC (7)

**New York at 64 is by far the largest unshipped region** — no other exceeds 40. Obvious next
state.

**Yield band ×0.50–0.85 — treat as a guess, not a model.** It rests on **one** observation, and
that observation (Oregon, ×0.86) falls *outside* the band. Plan a range and expect to update the
band after NY, which will be the second data point.

*Newfoundland records are miscoded `NE` in the source data and re-filed by city in the section.
A dump that skips the city split double-counts NE and NL — 12 + 15 both reported as 27 — and the
raw total reads 4,546 against a published 4,519. **The rebuilt harness applies the split, so no
correction is needed with it.** Subtract 27 only when reconciling a dump you know skips the split.*

---
Store: The Jiu Jitsu Mindset (thejiujitsumindset.com), admin /store/7f7e22, via Shopify connector.
Working files in the connected `TJJM Projects` folder:

- **`RULES-tjjm.md`** — **durable decision rules + their evidence. Read FIRST.** Supersedes both
  the collision rule and the verification method as stated in older documents.
- `collision-audit-2026-08-05.md` — the full audit, adjudications, brand pass and build record.
  Still the best evidence base, **but three claims in it are now known wrong**: its B1/B2 tables
  misclassify `oregonbjj.com` and `sakurabjj.com`; its "0 mixed-case hostnames" finding is
  contradicted by its own METHOD CORRECTION 4 (the real count is 3); and its trailing
  "Proposed next actions" list is corrupted (items 3–5 repeat) and includes "fix the 38
  brand-root links", which its own METHOD CORRECTION 3 reduces to 11 — already shipped in XX.
  **Treat that closing list as dead; this handoff's backlog is the live one.**
- `oregon-136-matmade.tsv`, `oregon-curation-worksheet.md`, `tjjm-gyms-data-35.liquid`,
  `build_or.py`.
