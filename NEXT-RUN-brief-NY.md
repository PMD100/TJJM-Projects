# Session brief — New York import

Paste the block below into a **new** chat session, with the `TJJM Projects` folder **connected**
(use the folder picker — do not just attach `HANDOFF-next-states.md`; `RULES-tjjm.md` is canonical
and has to be reachable, along with the audit and the Oregon working files).

---

## The block to paste

> Continuing the TJJM BJJ directory project. Read `RULES-tjjm.md` first, then
> `HANDOFF-next-states.md` — both in the connected folder. RULES is canonical where the two
> overlap.
>
> This run: import **New York**. It is the largest unshipped region at 64 legacy records and no
> other exceeds 40. Follow the full import sequence, steps 1–12.
>
> Five things in the docs that are easy to skim past:
>
> - **METHOD CORRECTION 7 is new (6 Aug) and it invalidated a whole sweep.** Sweep fetches need
>   `credentials:'include'` — with `credentials:'omit'` Shopify never stores the preview cookie
>   and renders the **live** theme on both sides, so the sweep compares MAIN to itself and passes
>   clean. The preview cookie is also one shared value per origin, so the sweep must run
>   **sequentially**, not concurrently. A sweep where every region differs, or none does, is a
>   broken sweep — assert the expected total explicitly.
> - **Duplicate MAIN at step 2, before changing anything**, as the "before" baseline. MAIN is now
>   theme YY (`154658242732`). Do not reuse the audit-dump harness as a baseline.
> - **Step 11's rebuild procedure was rewritten 5 Aug** — rebuild all 61 regions and assert
>   exactly the expected ones differ. Never rebuild stored values from a rendered page.
> - **`tjjm-gyms.json` is not raw stored values** (corrected 6 Aug). It has `tjjm-gym-websites`
>   overrides applied, but no `https://` prepend and no address backfill. Only the audit dump is
>   raw. This matters when you re-measure defect classes after the import.
> - **Name, acronym and address signals are candidate generators, not evidence.** The acronym pass
>   went 1-for-3 on 6 Aug. Open each school's page and read the body before deciding; do not judge
>   from search results, `<title>`, or directory aggregators, and treat a brand's own locations
>   page as incomplete rather than authoritative.
>
> Expect to update the yield band. It is ×0.50–0.85 resting on a single observation (Oregon,
> ×0.86) that falls outside it; NY is the second data point.
>
> Stop and tell me before publishing, and tell me if `fileUpdate` is blocked rather than working
> around it.

---

## Context the next session will need but may not surface on its own

**Where NY lands in the data model.** Per-state MatMade imports run `tjjm-gyms-data-2` … `-35`, so
NY is **`-36`**. The new snippet needs a `render` tag added to the section's capture list in
`sections/tjjm-state-directory.liquid`, and **the new section size must be predicted before
writing** — it is currently **12,485 B** against the Admin API's ~24 KB rewrite ceiling, so there
is plenty of headroom, but the prediction is the gate.

**The scraping playbook may have gone stale.** `buildId` `Rd7MR1U4ddxhWYs6pVmUV` was recorded valid
**5 Aug 2026**. Re-derive it before crawling rather than assuming; the sitemap path
(`/sitemap/gym-sitemap.xml`, reached via `/sitemap.xml`) should still hold.

**Themes that can be deleted once you are happy.** `154658209964` (BEFORE baseline for YY) and
`154653950124` (old MAIN / XX). Keep XX briefly as a rollback target if you like.

**Two connector constraints that shape the run.** `themePublish` is blocked — you publish.
`themeFilesUpsert` is blocked on MAIN — always duplicate first, and `themeDuplicate` needs ~30 s
before files are readable.

## What this session left owed, if the next one has spare capacity

These are all logged in the backlog; none of them block the NY import.

- **Item 0c** — three records needing a snippet rewrite, correct values already verified:
  `Elite Martial Arts-Richmond` (wrong city *and* address), `American Top Team Aventura` (wrong
  city), `SMAA/Soul Fighters SBC` (stale address, plus a rename to Synergy Martial Arts Academy).
- **Six `tjjm-statedir-notes-<code>` files** were never written for FL, LA, MO, NJ, TX, NV.
  Step 7 asks for per-state rationale; the 6 Aug run put it in the backlog rows instead.
- **Item 2b** — UFC GYM Sherwood (4520 S Sherwood Forest Blvd Ste 110, Baton Rouge 70816) is
  absent from the directory entirely now that both stale LA records are suppressed. Address
  verified; it is a one-record add.
- **Item 1b-follow-up** — `Alliance Jiu Jitsu San Diego` vs `Alliance San Diego`, same city,
  different domains, surfaced but never checked.
