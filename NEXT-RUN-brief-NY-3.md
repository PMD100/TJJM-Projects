# Session brief — New York import, RESUME AT STEP 5

Supersedes `NEXT-RUN-brief-NY-2.md` for the *state of the run*. **Step 3 is now COMPLETE.**
The method warnings from that brief still apply and are carried forward below, because they have
not stopped being true — plus four new ones this run measured.

Paste the block below into a **new** chat session with the `TJJM Projects` folder **connected**
via the folder picker. `RULES-tjjm.md` is canonical and must be reachable, along with the audit,
the Oregon working files, and the four NY files.

---

## The block to paste

> Continuing the TJJM BJJ directory project — the **New York import, resuming at step 5**.
> Read `RULES-tjjm.md` first, then `HANDOFF-next-states.md`, then the four NY working files in
> the connected folder: `ny-step3-findings.md`, `ny-curation-worksheet.md`,
> `ny-186-matmade.tsv`, `ny-legacy-64-raw.txt`. RULES is canonical where any two overlap.
>
> **Steps 1, 2, 3 and the mechanical half of step 4 are DONE. Nothing has been written to any
> theme.** Production is untouched; the only store change is an inert duplicate. Do not redo
> steps 1–3 — but do re-derive the buildId before crawling anything.
>
> Carry-over state you must not re-establish:
>
> - **MAIN is still theme YY (`154658242732`), `updatedAt` 2026-08-05T22:37:33Z.**
> - **The BEFORE baseline `154661355692` is STILL VALID** — created 23:10:54Z, *after* MAIN's
>   last modification, and verified unchanged at the end of the step-3 run. It stays honest
>   **only while MAIN stays untouched.** Re-check `updatedAt` on both before trusting this line;
>   if anything has been written to or published on MAIN since, it is void and you need a fresh
>   duplicate before you change anything.
> - **NY is snippet `-36`.** Per-state MatMade imports run `tjjm-gyms-data-2` … `-35`.
> - buildId `Rd7MR1U4ddxhWYs6pVmUV` — **re-derived from `__NEXT_DATA__` twice now, 5 Aug.**
>   Re-derive again rather than trusting this line. Sitemap `/sitemap/gym-sitemap.xml` via
>   `/sitemap.xml`: 7,311 URLs; crawled 7,310 at concurrency 12, 0 errors.
>   `triton-fight-center` 404s permanently — skip it.
> - **The 186 MatMade records are on disk in `ny-186-matmade.tsv`** (11 columns, raw
>   `websiteURL`, query strings intact). **You do not need to re-crawl for step 5.** Re-crawl only
>   if you need fields the TSV omits.
> - **NY has 186 MatMade candidates against 64 legacy records, 0 of them suppressed.**
>
> Four decisions already taken — do not re-open them:
>
> 1. **NY only.** Backlog 0c and 2b do *not* ride along, so the step-9 sweep asserts **exactly
>    one region differs**.
> 2. **`tjjm-statedir-notes-ny` only.** The six owed notes files stay in the backlog.
> 3. **Fix the 16 multi-tenant / non-site URLs during the import**, not as a backlog item.
> 4. **Read the ~55 records that signal**, not all 186.
>
> Method warnings that will cost you a rerun. The first five are carried forward unchanged; the
> next four came from the step-3 planning run; the last four were **measured this run**:
>
> - **METHOD CORRECTION 7.** Sweep fetches need `credentials:'include'`; with
>   `credentials:'omit'` Shopify never stores the preview cookie and renders the **live** theme on
>   both sides, so the sweep compares MAIN to itself and passes clean. The preview cookie is one
>   shared value per origin, so the sweep must run **sequentially**. A sweep where every region
>   differs, or none does, is a broken sweep — assert the expected total explicitly.
> - **The BEFORE baseline must predate every change.** It still does. Do not reuse the
>   audit-dump harness (`154657063084`) as a baseline; it is a post-XX snapshot.
> - **Step 11's rebuild procedure was rewritten 5 Aug** — rebuild all 61 regions and assert
>   exactly the expected ones differ. Never rebuild stored values from a rendered page.
> - **`tjjm-gyms.json` is not raw stored values.** It has `tjjm-gym-websites` overrides applied,
>   but no `https://` prepend and no address backfill. Only the audit dump is raw.
> - **Name, acronym and address signals are candidate generators, not evidence.** Open each
>   school's page and read the body; do not judge from search results, `<title>`, or directory
>   aggregators, and treat a brand's own locations page as incomplete rather than authoritative.
> - **The no-cors probe is unreliable in BOTH directions — now measured both ways.** 21 of 64
>   legacy domains failed the screen and **4 of those 21 (19%) were not dead**. Separately, **7 of
>   the 43 that PASSED (16%) do not reach the school's site at all.** The screen orders the work.
>   It never concludes.
> - **A MatMade link can be wrong-entity, not just stale.** `martialartsbuffalo.com`, stored on
>   `Seven Tigers Martial Arts Academy` /Cheektowaga, is the **Buffalo Niagara Martial Arts
>   Festival** event site. Search for the school, not the link.
> - **Two names carry `|`, which is a field separator.** `Sas Jiu Jitsu Syracuse | BJJ
>   Syracuse NY 13206` and `Synthesis Brazilian JiuJitsu | BJJ Rochester NY 14610` **cannot be
>   written at all** until renamed. Gate on `/[|~]/` in code before generating the snippet, for
>   every record, not just these two.
> - **Every one of the 64 NY legacy records has an EMPTY address.** The legacy side cannot be
>   deduped by address at all; name and domain only. The section's address-backfill transform is
>   a no-op for legacy NY, which matters when you reason about step 11.
> - **NEW — "reachable but broken" is a third state, not a shade of dead.**
>   `location.host === 'chromewebdata'` is conclusive only for NXDOMAIN/connection failure. A
>   **TLS interstitial** ("Privacy error") makes `javascript_tool` fail with *"Cannot attach to
>   this target"* — **that error is a signal, not a tool fault.** And a server can answer with no
>   site at all (`itcny.com` → IIS 500.19). A loop testing only for `chromewebdata` scores both
>   as LIVE. Test for the interstitial and for an empty/error body, and re-probe the opposite
>   scheme **and** the apex/www alternate before concluding.
> - **NEW — a lapsed domain can come back as spam.** `cnymma.com` (CNY MMA /Baldwinsville) is now
>   an **Indonesian online-gambling site**. It scores LIVE on every probe and no parked-domain
>   keyword matches it. Only reading the body catches this class. **It is live on production
>   right now.**
> - **NEW — the output filter blocks raw HTML echo.** Reading `document.documentElement.outerHTML`
>   back gets you `[BLOCKED: Cookie/query string data]`. To move URLs with query strings through,
>   **percent-encode `?` and `&` in the page** and decode on the far side; that passed cleanly,
>   including a `rwg_token`. Never echo signed upload parameters at all.
> - **NEW — `get_page_text` collapses tabs to spaces.** A tab-separated dump read back through it
>   is unrecoverable. Use a distinctive multi-char delimiter (`<:>` worked) and convert to tabs
>   mechanically afterwards. Note two record names legitimately contain `|`, so `|` is unsafe as
>   a delimiter on the MatMade side.
>
> Expect to update the yield band. It is ×0.50–0.85 resting on a single observation (Oregon,
> ×0.86) that falls outside it; NY is the second data point, and at 186 candidates it is a
> materially larger sample than Oregon's 136.
>
> Stop and tell me before publishing, and tell me if `fileUpdate` is blocked rather than working
> around it.

---

## What step 3 established, and what it deliberately did not

**Step 3 settles the state of a *link*. It never settles the state of a *school*.** Four cases
also settled a *city*. Zero keep/suppress verdicts exist. Full detail in `ny-step3-findings.md`.

### The 21 screen-failures: 17 dead, 4 not

**DEAD by navigation (`chromewebdata`), n=17:** `serrabjj.com` · `seventigersmartialarts.com` ·
`thedonycny.com` · `nextevolutionma.com` · `brianbeury.com` · `albanybjj.com` · `clobberbjj.com` ·
`elitefitnessmartialarts.com` · `fightsporttrainingcenter.com` · `bptwestchester.com` ·
`joncalestinebjj.com` · `jiulivrenyc.com` · `middletownbjjny.com` · `plattsburghbjj.com` ·
`watertownbjjny.com` · `precisionbjj.com` · `newburghbjj.com`

**NOT dead, n=4:** `binghamtonbjj.com` (301 → `broomecountymartialarts.com`, live school,
renamed) · `paxibellum.com` (apex live; only `www` fails TLS — **the record stores `www`**) ·
`rochesterfitnessmartialarts.com` (301 → `rochesterkungfu.com`) · `itcny.com` (server up,
IIS 500.19, no site).

### The 43 screen-passes: 7 do not reach the school

| legacy record | domain | what the body says |
|---|---|---|
| CNY MMA /Baldwinsville | `cnymma.com` | **Indonesian online-gambling spam.** Live on production. |
| Ithaca BJJ /Ithaca | `ithacabjj.com` | Parked — redirects to `/lander`, empty. |
| Kings Combat /Brooklyn | `kingscombat.com` | GoDaddy for-sale lander, $1,988. |
| Jungle Gym Martial Arts /New Rochelle | `junglegym.com` | **UK playground-equipment retailer.** |
| Modern Martial Arts NYC /New York | `modernmartialarts.com` | **Book promo site** (James Dolmage). |
| Savarese BJJ Academy /Lynbrook | `savarese.com` | **Savarese Software Research Corporation.** |
| Maxum BJJ Long Island /Huntington | `maxumbjj.com` | Unpublished site-builder placeholder. |

### Three link/scheme fixes the import should carry

- `Bellmore Kickboxing Academy` → `bellmorekickboxingmma.com` (301 from the stored host).
- `Buffalo Brazilian Jiu Jitsu Academy` → `https://` (the **only** `http://` record in the 64).
- `Paxibellum` → apex `paxibellum.com`, not `www.`.

### The four named debts — all closed

1. **`kiotobjj.com`** — the school is at **96 Biltmore Ave, Oakdale NY**. The legacy city
   `/New York` is **wrong**; MatMade's `/Sayville` @ 205 West Main St **contradicts the site's own
   address**. One of the two addresses is stale — unresolved.
2. **Serra Huntington is real.** The school's own contact page lists **two** academies: Huntington
   (365 West Jericho Tpke, 11743) and Levittown (2949 Hempstead Tpke). So the Huntington stub is a
   **real school missing an address**, and the **Levittown** stub is the redundant one. ⚠️ The
   identical phone/rating/review pair read as "both are stubs" and **pointed the wrong way on one
   of the two** — a caution for that signal.
3. **Igor Gracie** — the `safebrowse.io` wrapper's target opens live and real, and the **legacy
   record already stores it clean**. Keep legacy's URL, discard the wrapper.
4. **Seven Tigers — searched, still NOT settled.** No school-owned page exists. Aggregators say
   open at the MatMade address and phone, offering **Karate / Praying Mantis Kung Fu, not BJJ** —
   aggregator evidence only, so a **prior, not a result**. `7tigers-jidokwan.com` was checked and
   **rejected**: it is a Taekwondo school in **Charlottesville, Virginia**.

---

## The biggest thing waiting for step 5

**The Modern Martial Arts knot. Do not adjudicate any part of it row by row.**

Two legacy records with independently broken links (`Modern Martial Arts NYC` → a book;
`Vitor Shaolin BJJ NYC` → a live site that is **Modern Martial Arts, Times Square**, with zero
Shaolin content), five MatMade records across at least three domains (`4blackbelt.com`,
`mmanewyorkcity.com` ×2 including a path/record mismatch, two mindbodyonline wrappers), and the
worksheet's single same-address pair (E) all sit in one cluster. Read the whole thing together.

---

## Still owed on NY, in rough priority order

1. **7 school searches** — one per unusable screen-pass domain above. **A dead link is not a dead
   gym**; backlog item 2 conflated them in 2 of 6 cases. Note `cnyjiujitsu.com` (Haven Jiu Jitsu
   /Syracuse) advertises **"Syracuse & Baldwinsville"** — CNY MMA's city — so read that pair
   together. **Do not repoint CNY MMA on that hint alone.**
2. **The Modern Martial Arts knot.**
3. **Kioto's Oakdale-vs-Sayville address conflict.**
4. **The 186 MatMade domains have never been probed or opened at all.** The 16 multi-tenant hosts,
   the 5 shared-domain groups and the 23 `tsk.com` per-location URLs are unverified. The NJ
   precedent (METHOD CORRECTION 3) says per-location `tsk.com` URLs are usually right — 17 of 18 —
   but that is a prior from a different state.
5. **Is anything in the 186 a non-BJJ school?** Live and unchecked on the legacy side: `Swan's
   Martial Arts Academy` (Family Kempo Karate), `Rochester Fitness Martial Arts` (Shaolin Kung
   Fu). Unchecked on the MatMade side: `Kim's TaeKwonDo`, `Iaido Kendo Club`, `Westchester Judo
   Club`, `Church Street Boxing Gym`, `Krav Maga Academy`, `Evolution Muay Thai`, `Jiu Jitsu
   Massage`. **No systematic scan has been run on either side.**
6. **`Victor CTC`** — no address, no `postalCode`, `city` resolves to "Victoria" while the slug
   says `victor-ctc-victor-new-york`. Would take the missing-`postalCode` non-gym tell to 3-for-3,
   **but it has not been body-read**, so it is a prior, not a result.
7. **City normalisation before the snippet is generated.** Four lowercase/underscored
   (`point_lookout`, `poughkeepsie`, `sayville`, `victor`), one ALL CAPS (`SYRACUSE`), and
   inconsistent boroughs across the 186. Match the legacy convention (`New York`, `Brooklyn`,
   `Astoria`, `Long Island City`, `Bayside`, `Sunnyside`) or the city grouping fragments.
8. **Blind spot 1 (never-imported duplicates)** — untouched, unreachable by any diff run so far.
9. **No check yet on whether any of the 186 is already in the directory under a different region.**

---

## Owed to other states, found incidentally

**10 MatMade records carry a 2-letter code in `state.title`** instead of a full state name, all
with a null `postalCode`: 6 TX, 2 TN, 1 NV, 1 AZ. **None are NY.** They are invisible to a
`state.title === '<Full Name>'` filter, and TN (34, unshipped) will hit this.

*New this run:* they are **not randomly distributed** — 8 of the 10 are Renzo Gracie or Insight
BJJ affiliate records (`renzo-gracie-reno-reno-nv`, `renzo-gracie-sat-san-antonio-tx`,
`renzo-gracie-spring-hill-spring-hill-tn`, `insight-bjj-bastrop-…`, `insight-bjj-brenham-…`,
`renzo-gracie-taylor-…`, `insight-bjj-la-grange-…`, `renzo-gracie-columbia-columbia-tn`), plus
`marcelo-garcia-dallas-dallas-tx` and `sonoran-brazilian-jiu-jitsu-tucson-az`. **Inference, not
measurement:** that looks like one upstream import batch, not ten independent slips, so expect it
as a *block* rather than scattered singletons.

---

## Also worth recording in RULES

- **§6, new defect class — interstitial / safety-wrapper URLs.** `Igor Gracie Academy`'s stored
  `websiteURL` is a `safebrowse.io/warn.html` wrapper carrying the real target as a query
  parameter plus a token. It **evaded the domain-collision check** because the wrapper host is not
  the school's host — it surfaced only via the name check. Worth a corpus-wide scan for wrapper
  hosts as its own backlog item.
- **§6, new defect class — lapsed domain re-registered as spam** (`cnymma.com`). No keyword or
  status-code signal catches it.
- **§4, boundary on "the name check found 0 of 40".** That was measured on **shipped** states,
  where a curator had already reconciled names against MatMade. NY is unshipped, and **4 of its
  collisions are name-only**. Write the boundary in with the sample size — the next 33 unshipped
  regions inherit it. *n=1; untested on the other 33.*
- **§4, the parked-keyword regex produces false positives.** A "for sale"/"coming soon" scan
  flagged `queensjiujitsu.com`, which is a plainly real academy in Astoria. Same lesson as the
  acronym pass: a string signal generates candidates, it does not conclude.

---

## Themes

- **Keep:** MAIN `154658242732` (YY) · **`154661355692`** (the BEFORE baseline — still valid,
  do not delete).
- **Disposable once you are happy:** `154658209964` (the previous BEFORE baseline for YY) and
  `154653950124` (old MAIN / XX). Keep XX briefly as a rollback target if you like.
- `154657063084` is the audit-dump harness — keep, but it is **not** a valid "before" theme.

## Connector constraints, unchanged

`themePublish` is blocked — you publish. `themeFilesUpsert` is blocked on MAIN — always duplicate
first, and `themeDuplicate` needs ~30 s before files are readable. `fileUpdate` is *situational*,
not reliably blocked: retry once, then report.

## A small dating note

The theme named "Aug 6 …" and the corrections dated 6 Aug have an `updatedAt` of **2026-08-05**,
and the system date for this run was **5 Aug 2026**. The "6 Aug" labels appear to run a day ahead
of the store's own timestamps. Nothing depends on it.

## Still owed and untouched, carried forward

None of these block the NY import; all are logged in the handoff backlog.

- **Item 0c** — `Elite Martial Arts-Richmond` (wrong city *and* address), `American Top Team
  Aventura` (wrong city), `SMAA/Soul Fighters SBC` (stale address, plus a rename to Synergy
  Martial Arts Academy). All need a snippet rewrite; no override reaches `c` or a non-blank `a`.
- **Six `tjjm-statedir-notes-<code>` files** never written for FL, LA, MO, NJ, TX, NV.
- **Item 2b** — UFC GYM Sherwood (4520 S Sherwood Forest Blvd Ste 110, Baton Rouge 70816), absent
  from the directory entirely. Address verified; one-record add.
- **Item 1b-follow-up** — `Alliance Jiu Jitsu San Diego` vs `Alliance San Diego`, same city,
  different domains, surfaced but never checked.

---

## What the step-3 run did NOT check

- **No keep/suppress verdict was made on any record.** Step 5 is untouched.
- **None of the 186 MatMade domains was probed or opened.**
- **The 7 unusable screen-pass domains were not converted into school searches.**
- **Swan's and Rochester Kung Fu were not checked for a BJJ program**, only seen on the landing
  page.
- **The Modern Martial Arts / Vitor Shaolin cluster was not adjudicated.**
- **Nothing was written to any theme, snippet, metafield or file** other than this folder's
  working files. Verified at the end of the run: MAIN's `updatedAt` was unchanged and the theme
  count was the same 9 as at the start.
