# Batch 50 — city is now overridable, and a live GoDaddy lander finally got killed

Session of 17 Aug 2026. Built as theme **AC3** (`155006140588`), **staged and awaiting publish**.
Structural change to both rendering surfaces plus a new snippet. **Record counts have not moved.**
**Publish AC3 `155006140588`.** AB3 `155004502188` becomes the rollback.

⚠️ **One manual step:** `snippets/tjjm-b50-probe.liquid` (518 B) is a leftover scratch file on AC3.
Nothing renders it and it has been overwritten with an inert comment, but `themeFilesDelete` is
blocked by the connector — **please delete it in Shopify admin.**

---

## The one that matters most: a parked domain was live on the site

`murdocsbjj.com` redirects to `/lander` and reads *"murdocsbjj.com has expired and is parked free,
courtesy of GoDaddy.com."* Exactly the thing you asked to be eliminated.

A blanking row for that school **had been written months ago and has never worked.** The row spelled
the name with a straight apostrophe (`Murdoc's`); the record uses a curly one (`Murdoc’s`). The
override matched nothing, silently, and the lander kept rendering.

It is fixed. **The orphan count across all seven override files is now zero** — every override row
matches a real record.

**This was found by an integrity audit, not by a link check**, and it is worth saying why that
matters: every screen this project has run tests *whether a URL is good*. None of them tested
*whether our own fixes are actually taking effect*. That gap had been open the whole time.

---

## The second integrity finding: one override row can blank two schools

Override rows key on the **record name**, and the corpus contains **16 duplicated names**. So a
single blanking row hits every record sharing that name. Two live cases:

- **`EchoValor Striking & MMA`** — Centralia WA and Beaverton OR, both on `echovalor.com`. I checked:
  that domain is now a **veterans storytelling podcast and merch brand**, not a gym. The blank is
  correct for both, so no harm done here.
- **`Evolution Jiu Jitsu`** — Juneau AK (`evojj.com`, dead) and Burlington WI (Facebook page, alive
  and healthy, 1.2K followers). I concluded the Burlington link had been killed as collateral damage
  and asked for a record rename to free it.

**I was wrong, and the agent caught it.** A *separate* record, `Evolution Jiu Jitsu Burlington`,
already exists in data file 45 and renders the healthy link fine; the older duplicate is suppressed
by the removed-index. The rename would have created two identically-named WI records and
un-suppressed a stale one. It was refused. So was a second request of mine to blank
`American Grappling` — already blanked, and adding it again would have violated gate C3.

Both refusals were correct. I had written the instructions from stale notes.

---

## City is now overridable — `snippets/tjjm-gym-cities.liquid`

The city-correction pass hit a wall: **14 of the 21 corrections live in `tjjm-gyms-data.liquid`, a
113 KB legacy blob on a single 113,186-character line.** Shopify's theme-file rewrite ceiling is
~24,576 bytes, so that file **cannot be rewritten at all** — and a dropped character in it silently
destroys every record after it, because the parser skips objects that fail to decode.

Rather than risk it, city now works the way website and address already do: `~Exact Name|City~` rows
in a snippet, rendered into **both** surfaces. The blob never needs to be touched again.

**21 corrections applied.** Each was verified against the school's own published address — 69 rows
were shortlisted by hand from 2,050 identity verdicts, and only these survived. The rest were
same-town address moves, metro neighbours or neighbourhoods, which need no change.

Highlights: `BlackSmith Jiu Jitsu Florida` was filed in **Tallahassee** and is in **Niceville**, 120
miles away. `Serra BJJ Academy` was filed in Levittown and lists only Huntington. `Kioto` (New York →
Oakdale) and `Long Island MMA` (Lake Grove → West Babylon) were both called out in the batch-7 notes
months ago, with the observation that no override could reach the city field. Now one can.

### Verified end to end, on both surfaces
The single most expensive mistake in this project was a second directory surface that silently
ignored the override snippets for 28 batches. So this was proved, not assumed:

- Region page: `Brian Beury Jiu Jitsu` now files under a new **"Jiu Jitsu in Watervliet, NY"**
  heading; a control school in Albany still reads Albany; NY still shows **182 gyms**.
- Flat page: the `tjjmDirCity` island parses **21 rows**; searching `watervliet` finds the school and
  `levittown` returns nothing; **5,215 gyms, 61 regions**, and **every per-region count identical**
  to the pre-change snapshot.
- Both section patches were proved by **byte-offset opcode diff** — every opcode an insertion, and
  deleting exactly those runs reconstructs the original byte-for-byte.

**Ordering choice worth recording:** the city override is applied **after** the Nebraska→Newfoundland
re-filing test and **before** display bucketing. That test reads the city string, so applying the
override first would let a city row move a school between the NE and NL region pages. Applied after,
that is structurally impossible.

---

## A correction to my own notes

I told the agent that the one data-snippet write already on AC3 had fixed **Michigan Top Team**
(Detroit → Southfield). It had not — the byte diff shows it fixed **AKF Lexington**
(Nicholasville → Lexington). Michigan Top Team lives in the 113 KB blob and was still wrong; the new
override is what actually fixes it. Reported here because I had it wrong in two places.

---

## Also this batch

- **Hidden-spam re-screen: 130 more links, zero spam**, one unreachable
  (`blackhousemiamibeach.com`, SSL cipher mismatch). Running total **330 of 1,202**. Every keyword hit
  was a known false-positive generator — Wix `slots=`, "spe**cialis**t", and one review author
  genuinely named *Bandar*.
- **A latent bug found, deliberately not fixed.** The flat page's override regex requires a trailing
  `~`. `tjjm-gym-addresses.liquid` has early rows without one — and one row missing its leading `~` —
  so the JS silently drops alternate rows there. **Region pages are unaffected; the flat page loses
  some address overrides.** Left alone to keep this change surface minimal. Worth a batch of its own.

---

## Where the directory stands

| | |
|---|---|
| records published | **5,215** across 61 regions (5,911 in corpus, 696 suppressed) |
| with a link | **4,058** |
| override rows | 1,326, all distinct names, **zero orphans** |
| city overrides | 21 |
| identity pass | complete, 2,170 of 2,170 |
| hidden-spam re-screen | 330 of 1,202 |

Headroom: file 1 397 B, file 3 923 B, file 2 1,269 B, file 4 1,632 B, file 6 4,751 B,
**file 7 17,558 B**, cities file 21,205 B.

## Next

1. **Fix the address-override regex bug** — rewrite the malformed rows in `tjjm-gym-addresses.liquid`
   to the strict `~Name|Value~` grammar so both surfaces parse it identically.
2. **Audit the other 15 duplicated names** the way `EchoValor` and `Evolution Jiu Jitsu` were audited,
   before one of them takes a blanking row and kills a healthy school.
3. **Continue the hidden-spam re-screen** — 742 left.
4. **Six `description_tag` metafields carry a stale "across N cities" count** now that the city
   corrections have landed: FL 132→133, MI 72→73, NJ 136→138, TX 133→134, IL 78→79, GA 78→79.
5. **`Method BJJ`** — recorded in New Jersey, actually an Edmonton school that closed in Nov 2025.
   Its link is already blanked; the record should probably be suppressed.
6. The `AKF Lexington` correction now exists in **two** places (data file 14 and the city override).
   Harmless — they agree — but worth collapsing to one.
