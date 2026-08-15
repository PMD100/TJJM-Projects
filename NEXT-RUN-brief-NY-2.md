# Session brief — New York import, RESUME AT STEP 3

Supersedes `NEXT-RUN-brief-NY.md` for the *state of the run*. That brief's five method warnings
still apply verbatim and are repeated below, because they have not stopped being true.

Paste the block below into a **new** chat session with the `TJJM Projects` folder **connected**
via the folder picker. `RULES-tjjm.md` is canonical and must be reachable, along with the audit,
the Oregon working files, and the three new NY files this run produced.

---

## The block to paste

> Continuing the TJJM BJJ directory project — the **New York import, resuming at step 3**.
> Read `RULES-tjjm.md` first, then `HANDOFF-next-states.md`, then the three NY working files in
> the connected folder: `ny-curation-worksheet.md`, `ny-step3-findings.md`,
> `ny-legacy-64-raw.txt`. RULES is canonical where any two overlap.
>
> **Steps 1, 2 and the mechanical half of step 4 are DONE. Nothing has been written to any
> theme.** Production is untouched; the only store change is an inert duplicate. Do not redo
> steps 1–2 — but do re-derive the buildId before crawling anything.
>
> Carry-over state you must not re-establish:
>
> - **MAIN is still theme YY (`154658242732`).**
> - **The BEFORE baseline already exists: `154661355692`** ("BEFORE baseline — MAIN/YY snapshot
>   (pre-NY import)"), duplicated from MAIN before any change. It is the honest "before" side for
>   the step-9 sweep **only for as long as MAIN stays untouched** — if anything has been written
>   to or published on MAIN since, it is void and you need a fresh one.
> - **NY is snippet `-36`.** Per-state MatMade imports run `tjjm-gyms-data-2` … `-35`.
> - buildId `Rd7MR1U4ddxhWYs6pVmUV` was **re-derived and confirmed 5 Aug**; re-derive again
>   rather than trusting this line. Sitemap `/sitemap/gym-sitemap.xml` via `/sitemap.xml` held:
>   7,311 URLs. `triton-fight-center` still 404s — skip it.
> - **NY has 186 MatMade candidates** against 64 legacy records, 0 of them suppressed.
>
> Four decisions already taken — do not re-open them:
>
> 1. **NY only.** Backlog 0c and 2b do *not* ride along, so the step-9 sweep asserts **exactly
>    one region differs**.
> 2. **`tjjm-statedir-notes-ny` only.** The six owed notes files stay in the backlog.
> 3. **Fix the 16 multi-tenant / non-site URLs during the import**, not as a backlog item.
> 4. **Read the ~55 records that signal**, not all 186.
>
> Nine things that will cost you a rerun if you skim past them — the first five are carried
> forward unchanged from the previous brief, the last four are new from this run:
>
> - **METHOD CORRECTION 7.** Sweep fetches need `credentials:'include'`; with
>   `credentials:'omit'` Shopify never stores the preview cookie and renders the **live** theme on
>   both sides, so the sweep compares MAIN to itself and passes clean. The preview cookie is one
>   shared value per origin, so the sweep must run **sequentially**. A sweep where every region
>   differs, or none does, is a broken sweep — assert the expected total explicitly.
> - **The BEFORE baseline must predate every change.** It already does. Do not reuse the
>   audit-dump harness (`154657063084`) as a baseline; it is a post-XX snapshot.
> - **Step 11's rebuild procedure was rewritten 5 Aug** — rebuild all 61 regions and assert
>   exactly the expected ones differ. Never rebuild stored values from a rendered page.
> - **`tjjm-gyms.json` is not raw stored values.** It has `tjjm-gym-websites` overrides applied,
>   but no `https://` prepend and no address backfill. Only the audit dump is raw.
> - **Name, acronym and address signals are candidate generators, not evidence.** Open each
>   school's page and read the body; do not judge from search results, `<title>`, or directory
>   aggregators, and treat a brand's own locations page as incomplete rather than authoritative.
> - **NEW — the no-cors probe is unreliable in BOTH directions.** The handoff already warned that
>   parked pages and directories score LIVE. This run found the reverse too: **21 of 64** legacy
>   domains failed the screen, and a failure collapses NXDOMAIN, TLS errors, timeouts and resets
>   into one bucket. Only navigation settles it — `location.host === 'chromewebdata'`, which the
>   browser tooling surfaces as *"Frame with ID 0 is showing error page"*. Use the screen to order
>   the work, never to conclude.
> - **NEW — a MatMade link can be wrong-entity, not just stale.** `martialartsbuffalo.com`, stored
>   on `Seven Tigers Martial Arts Academy` /Cheektowaga, is the **Buffalo Niagara Martial Arts
>   Festival** event site. Its legacy domain is dead *and* its MatMade domain belongs to someone
>   else, so **neither record says anything about whether that school is open.** Same class as
>   `Unconventional Performance & Training`. Search for the school, not the link.
> - **NEW — two names carry `|`, which is a field separator.** `Sas Jiu Jitsu Syracuse | BJJ
>   Syracuse NY 13206` and `Synthesis Brazilian JiuJitsu | BJJ Rochester NY 14610` **cannot be
>   written at all** until renamed. Both are keyword-stuffed. Gate on `/[|~]/` in code before
>   generating the snippet, for every record, not just these two.
> - **NEW — every one of the 64 NY legacy records has an EMPTY address.** So the legacy side
>   cannot be deduped by address at all; name and domain only. This also means the section's
>   address-backfill transform is a no-op for legacy NY, which matters when you reason about
>   step 11.
>
> Expect to update the yield band. It is ×0.50–0.85 resting on a single observation (Oregon,
> ×0.86) that falls outside it; NY is the second data point, and at 186 candidates it is a
> materially larger sample than Oregon's 136.
>
> Stop and tell me before publishing, and tell me if `fileUpdate` is blocked rather than working
> around it.

---

## Where exactly step 3 stopped

**4 of 64 legacy domains have been navigated. 60 have not.**

- **Confirmed DEAD** (conclusive signal): `serrabjj.com` · `seventigersmartialarts.com` ·
  `thedonycny.com` · `nextevolutionma.com`. All four were chosen because they are collision
  participants, so 4-for-4 says nothing about the rest.
- **17 screen-failures not yet navigated**, listed in `ny-step3-findings.md`.
- **All 43 screen-passes not yet opened.** This is the larger and more error-prone half — step 3
  exists precisely because parked domains and directories pass the screen.

Five bodies were read. They are characterised in `ny-step3-findings.md`, and **none of them is a
keep/suppress verdict** — each settles the state of a *link*, not of a *school*.

## The collision inventory is complete and sitting in the worksheet

`ny-curation-worksheet.md` holds all of it, measured: **15 domain collisions**, **4 name-only
collisions the domain check cannot see**, **5 MatMade-internal shared-domain groups**, **1
duplicate name**, **1 same-address pair**, and the full defect table for the 186.

Three things in it that are easy to underweight:

1. **The name check fired on NY, and RULES §4 says it found 0 of 40.** That measurement came from
   **shipped** states, where a curator had already reconciled names against MatMade. NY is
   unshipped, so its legacy names never were. Four collisions here are name-only. This is not a
   contradiction of the rule, it is a boundary on it — and it should be written into RULES §4
   with the sample size, because the next 33 unshipped regions inherit it. *n=1; untested on the
   other 33.*
2. **The same-address scan returned 0 twice before returning 1.** First keyed on city, which
   splits Manhattan / New York / Queens / The Bronx; then missed W↔West until directionals were
   folded. **Treat its n=1 as a lower bound, not a count.** It is one normalisation bug away from
   silence, which is the exact failure mode of the `URL.hostname` scan.
3. **23 Tiger Schulmann's NY locations, none of which are in the directory.** Largest single block
   of net-new in the state. All carry per-location `tsk.com` URLs, and the NJ precedent
   (METHOD CORRECTION 3) is that those are usually right — 17 of 18 NJ records were fine.

## New defect class worth recording in RULES §6

**Interstitial / safety-wrapper URLs.** `Igor Gracie Academy`'s stored `websiteURL` is a
`safebrowse.io/warn.html` wrapper carrying the real target as a query parameter plus a token.
Not previously recorded in this project. It also **evaded the domain-collision check**, because
the wrapper host is not the school's host — the pair surfaced only via the name check. Worth a
corpus-wide scan for wrapper hosts as its own backlog item.

## A third data point for an existing tell

`Victor CTC` /"Victoria" has **no address and no postalCode**. "STILL TRUE" records *missing
`postalCode` is a non-gym tell — 2-for-2 in Oregon, both CTCs.* This would be a third CTC with
the same signature, taking it to 3-for-3 — **but it has not been body-read**, so it is a prior,
not a result. Its `city` relation also resolves to "Victoria" while its slug says
`victor-ctc-victor-new-york`, so the city is wrong, not merely lowercase.

## Two housekeeping items

**City strings need a normalisation pass before the snippet is generated.** Four MatMade records
carry a lowercase/underscored city from the relation (`point_lookout`, `poughkeepsie`, `sayville`,
`victor`), one is ALL CAPS (`SYRACUSE`), and boroughs are inconsistent across the 186
(`Manhattan`, `New York`, `Queens`, `The Bronx`, `Astoria`, `Ridgewood`, `Forest Hills`,
`Williamsburg`). The existing 64 legacy records use `New York`, `Brooklyn`, `Astoria`,
`Long Island City`, `Bayside`, `Sunnyside` — match that convention or the city grouping in the
section will fragment.

**Owed to other states, found incidentally:** 10 MatMade records carry a 2-letter code in
`state.title` instead of a full state name — 6 TX, 2 TN, 1 NV, 1 AZ, all with a null
`postalCode`. **None are NY**, so they did not affect this run, but they are invisible to a
`state.title === '<Full Name>'` filter and TN (34, unshipped) will hit this.

## Themes

- **Keep:** MAIN `154658242732` (YY) · **`154661355692`** (the BEFORE baseline — this run's, still
  valid, do not delete).
- **Disposable once you are happy:** `154658209964` (the previous BEFORE baseline for YY) and
  `154653950124` (old MAIN / XX). Keep XX briefly as a rollback target if you like.
- `154657063084` is the audit-dump harness — keep, but it is **not** a valid "before" theme.

## Connector constraints, unchanged

`themePublish` is blocked — you publish. `themeFilesUpsert` is blocked on MAIN — always duplicate
first, and `themeDuplicate` needs ~30 s before files are readable. `fileUpdate` is *situational*,
not reliably blocked: retry once, then report.

## A small dating note

The theme named "Aug 6 …" and the corrections dated 6 Aug have an `updatedAt` of
**2026-08-05**, and the system date for this run was **5 Aug 2026**. The "6 Aug" labels in the
handoff appear to run a day ahead of the store's own timestamps. Nothing depends on it, but do not
be thrown by a "6 Aug" correction sitting on a 5 Aug theme.

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
