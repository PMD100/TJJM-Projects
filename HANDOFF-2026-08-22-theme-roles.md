# HANDOFF — theme roles need resetting (22 Aug 2026)

**Nothing in this file has been done for you. No theme was written or published.**

---

## The situation in one paragraph

At **2026-08-21T17:08:49Z** the staging theme and the production theme swapped roles. The theme
named *"TJJM ADDITIONS STAGING — reused nightly, do not publish"* is now **MAIN** (live on
thejiujitsumindset.com), and the reviewed batch-52 theme is **UNPUBLISHED**. The site content is
**fine** — it passed the full integrity audit on 22 Aug and is internally consistent. What is broken
is the **review gate**: staging and production are the same theme.

## Theme IDs

| role now | id | name |
|---|---|---|
| **MAIN (live)** | `155080032428` | TJJM ADDITIONS STAGING — reused nightly, do not publish |
| UNPUBLISHED | `155078131884` | Aug 19 BJJ Gyms AE3 — batch 52: additions snippet |
| UNPUBLISHED | `155006140588` | Aug 17 BJJ Gyms AC3 — batch 50: integrity fixes |
| UNPUBLISHED | `155004502188` | Aug 17 BJJ Gyms AB3 — batch 49: override file 7 |

4 themes; Shopify cap is 20, so there is headroom.

## What actually differs between the two themes — verified, exactly two files

Everything else — all 54 other TJJM snippets, both directory sections, `layout/theme.liquid`,
`config/settings_data.json`, every asset — is **byte-identical**.

| file | live `155080032428` | batch 52 `155078131884` |
|---|---|---|
| `snippets/tjjm-gyms-data-46.liquid` | 3,151 B `eba03058b693bc5f5f13b9ca02e897de` — **6 records** | 2,320 B `f8d915f21ce57a5666ee653f5a86e8fa` — empty plumbing |
| `snippets/tjjm-region-index.liquid` | 4,119 B `73e3c05c07281aeaff2904a381d5f4c1` — AL **81**, AK **17** | 3,446 B `8f4faa309ace35a8f6d2738476c47b35` — AL **78**, AK **14** |

The six records are the nightly discovery task's staged additions:

- **AL** — Gracie Barra Trussville, Ohm Jiu Jitsu, McLean's Martial Arts & Fitness
- **AK** — Southside Jiu-Jitsu Academy, Anchorage Dojo, Mat-Su Judo

**Both themes are self-consistent** — the region counts match the record counts in each case. There
is no half-broken state; publishing either one gives a coherent site. The only question is whether
those six records, which have not been through a batch review, stay live.

## Good news: the discovery guard held

`tjjm-nightly-gym-discovery` ran today at **10:02** and **wrote nothing**. Its guard (SKILL.md
line 98) requires `theme.role = UNPUBLISHED` and correctly refused when it came back `MAIN`. Both
checksums above were re-queried after that run and are unchanged. It also wrote no log for 22 Aug,
which is why `nightly/logs/` has no `discovery-2026-08-22.md`.

So nothing leaked to production — but **discovery is now stalled** and will stay stalled every night
until the roles are fixed.

---

# OPTION A — publish batch 52 (recommended)

Restores the design exactly. No file edits anywhere. One action.

### Steps

1. Shopify admin → **Online Store → Themes**.
2. Find **"Aug 19 BJJ Gyms AE3 — batch 52: additions snippet"** (`155078131884`) in the theme library.
3. **Actions → Publish.**

That is the whole change. Publishing it automatically demotes `155080032428` back to `UNPUBLISHED`.

### What this costs

Alabama drops 81 → 78 and Alaska 17 → 14 on the region pages. Those six records stay safe in
staging's `tjjm-gyms-data-46.liquid`; nothing is lost. Promote them whenever convenient through the
normal batch process (they will be the seed of batch 53).

### Why this is the right default

Those six records were never meant to be live without a batch review — that is precisely the gate
the design exists to enforce. Three schools per state, off the site for a few days, is a much
smaller problem than production and staging being the same theme.

---

# OPTION B — keep the six records live

Only if you want AL/AK correct immediately. More moving parts, and it touches the discovery task.

### Steps

1. **Rename the live theme** so nobody publishes over it by mistake.
   Admin → Themes → `155080032428` → Rename to e.g.
   `Aug 22 BJJ Gyms AF3 — batch 52 + 6 nightly additions`.
   **The name must no longer begin "TJJM ADDITIONS STAGING"** — see step 4.
2. **Create the replacement staging theme.** Duplicate `155078131884` (batch 52) — Actions →
   Duplicate — and rename the copy to **`TJJM ADDITIONS STAGING — reused nightly, do not publish`**.
   Leave it **UNPUBLISHED**. Duplicating batch 52 rather than the live theme matters: its
   `tjjm-gyms-data-46.liquid` is already the **empty** plumbing version, so the discovery task starts
   from a clean file instead of appending on top of six records that are already live.
3. **Note the new theme's ID** from the admin URL
   (`/admin/themes/<ID>/editor`).
4. **Update the discovery task** at
   `/Users/Peggie/Documents/Claude/Scheduled/tjjm-nightly-gym-discovery/SKILL.md`.
   The old ID `155080032428` is hardcoded in **two** places — **line 81** and **line 92**. Replace
   both with the new ID. Leave the name check (line 97) and the `UNPUBLISHED` role check (line 98)
   exactly as they are; they are what saved you this week.
5. **Nothing to publish** — the live theme is already MAIN and already correct.

### Watch out

The discovery task is instructed *"never create a new theme, the store is capped at 20"*. Step 2 is
you creating it, not the task, which is fine — but it does mean the task cannot self-heal if this
happens again. Step 4 is not optional; skip it and discovery keeps writing to the live theme.

---

## Verify after either option

Run this and check the roles came out right:

```graphql
{ themes(first: 10) { nodes { id name role } } }
```

Expect exactly one `MAIN`, and expect the theme whose name begins **"TJJM ADDITIONS STAGING"** to be
**UNPUBLISHED**. Then spot-check the live site:

- `/pages/bjj-schools-alabama` — count should read **78** (Option A) or **81** (Option B)
- `/pages/bjj-schools-alaska` — **14** (Option A) or **17** (Option B)
- `/pages/jiu-jitsu-schools-near-you` — should load and show cards

The next `tjjm-nightly-directory-check` run will confirm the checksum map independently; if you take
Option A, expect its totals to return to the 20 Aug baseline (5,911 records / 5,215 published), and
if Option B, expect them to stay at 5,917 / 5,221.

---

## Two housekeeping items, unrelated to the above

1. **`scratch/raw-datafiles/tjjm-gyms-data-14.liquid` is stale** — flagged three nights running.
   It is `d0741daf…`; live is `a87963d4…`. Refresh it from `build-b50/built/`. Also add a copy of
   `tjjm-gyms-data-46.liquid` to that folder — source it from `nightly/additions/`, which is now the
   authoritative local copy.
2. **`assets/tjjm-gyms*.json` — 34 files, ~600 KB — are vestigial.** Leftovers from the pre-15-Aug
   architecture in `CRITICAL-second-directory-surface.md`. `tjjm-gyms-14.json` and
   `tjjm-gyms-32.json` are stale relative to the snippets, and files 35–46 have no mirror at all —
   but **nothing renders them any more**: both `tjjm-gym-directory.liquid` and
   `tjjm-state-directory.liquid` now render the snippets directly. They are safe to delete, and
   deleting them removes a decoy that could mislead a future audit into thinking there is a second
   out-of-sync surface. They are identical in both themes, so this is not a publishing decision.
