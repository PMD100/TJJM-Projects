# Batch 16 — judo is in scope. Reversing part of batch 15, and the metafield catch-up.

Session of 13 Aug 2026. Built as theme **TT** (`154919895212`), **staged and awaiting publish**.
**Changes record counts: 5,214 → 5,215.**

---

## ⚠️ POLICY CHANGE — judo counts as in-scope grappling

The owner's ruling: **"Please include Judo when you see it."** This supersedes the implicit
BJJ-only standard applied in batches 9–15 and **retroactively invalidates one decision that had
already shipped.**

### What that broke, and the fix

**`Gladiator Sports Fitness MMA` (Hialeah FL) was suppressed in batch 15 — and published — purely
because its classes are Judo, kickboxing, MMA and Muay Thai with no BJJ.** Under the new rule that
is a valid record. Batch 16 **un-suppresses it and restores its link**.

Also restored: **`F-5 Grappling`** (OK), dropped from batch 14 as "explicitly wrestling". A school
named *Grappling* that teaches wrestling is plainly in scope under a grappling-arts reading.

| record | region | batch 15/14 action | batch 16 action |
|---|---|---|---|
| `Gladiator Sports Fitness MMA` | FL | suppressed | **un-suppressed + link restored** |
| `F-5 Grappling` | OK | link dropped | **link restored** |

**Unaffected and correctly still suppressed:** `Mega Church Jiu Jitsu` and `Empire Jiu-Jitsu Durant`
(both genuinely **closed**), `14ers Jiu Jitsu` (**dissolved**), `AJW Martial Arts Academy` (Shito
Ryu karate, **zero grappling of any kind**).

**Left alone, now clearly correct:** `Louisiana Judo` and `Tulsa Judo`, both published with links in
batches 13–14 and both judo-only. They were flagged as suppression candidates pending this ruling;
they are not.

### Still open under the new rule
Three links dropped in batch 14 — **`Reeds Elite MMA`, `Lionheart MMA`, `Yu'ki MMA`** — were removed
because no live page named a BJJ class. **Their actual discipline was never established**, and MMA
schools usually teach grappling. They are worth a targeted re-check, but I did not restore them:
unlike Gladiator and F-5, there is no positive evidence of a grappling programme, and guessing
would be exactly the fabrication failure this project guards against.

---

## Counts and the city-count check

**5,215 published / 61 regions / 696 suppressed records.**

The "across N cities" claims needed re-deriving, not just the gym numbers — **three cities dropped
to zero records** from batch 15's suppressions:

| city | region | status |
|---|---|---|
| Durant | OK | **now empty** |
| City Of Orange | NJ | **now empty** |
| Salida | CO | **now empty** |
| Muskogee | OK | still present (had two records) |

None of the three is named as an example city in its region's description, so only the counts moved.

## Metafields — DONE for CO, NJ, OK

Set and verified, `userErrors: []`:

| region | title | description |
|---|---|---|
| CO | 156 → **155** | 156 → 155, "across 47 cities" → **46** |
| NJ | 210 → **209** | 210 → 209, "across 137 towns" → **136** |
| OK | 98 → **96** | 98 → 96, "across 45 cities" → **44** |

**These three were set now on purpose**: the values are correct under *both* the live SS and the
staged TT, so no inconsistency window is open at any point.

**FL was deliberately NOT touched.** Its metafield still reads **328**, which is correct once TT
publishes. It is momentarily one ahead of live SS (327) — a window batch 15 opened and TT closes.
Do not "fix" it to 327.

### Rollback strings (pre-batch-16 values)
- CO title `BJJ Schools in Colorado | 156 Jiu Jitsu Gyms & Academies`; description `…156 BJJ gyms and academies across 47 cities including Denver, Colorado Springs and Boulder.…`
- NJ title `BJJ Schools in New Jersey | 210 Jiu Jitsu Gyms & Academies`; description `…210 BJJ gyms and academies across 137 towns including Newark, Jersey City, Hoboken and Toms River.…`
- OK title `BJJ Schools in Oklahoma | 98 Jiu Jitsu Gyms & Academies`; description `…98 BJJ gyms and academies across 45 cities including Oklahoma City, Tulsa, Edmond, Norman, Yukon and Broken Arrow.…`

---

## What was written

| file | was | now | change |
|---|---|---|---|
| `snippets/tjjm-removed-index.liquid` | 13,882 B | **13,853 B** | 1 suppression name removed |
| `snippets/tjjm-gym-websites-3.liquid` | 6,814 B | **6,951 B** | 2 links restored |

MD5-verified against theme TT by the caller: `98ee615156b26677c99582726f6248d6` /
`f6d9ea297b955017c4a2e03b0cbe7682`. The legacy blob, all data files, the section, region-index,
addresses, websites-1 and websites-2 are byte-identical to SS.

Gate: **C3** (neither restored name already had an override entry), **C9** (neither restates a
stored value), **C11** (each matches exactly one published record). The un-suppression was applied
by removing the name from the FL row only, and re-parsing the built file reproduces 5,215 exactly.

---

## TO PUBLISH

**Publish TT `154919895212`.** SS `154919305388` becomes the rollback.
**No further metafield work** — CO/NJ/OK are already set, FL self-corrects on publish.
Afterwards, confirm live cookie-free that the region nav sums to **5,215** and FL reads **328**.

---

## Lesson worth recording

**A scope rule that is never written down gets applied inconsistently and ships errors.** Across
batches 9–15 I rejected six records on a BJJ-only reading — `Paladin MMA`, `Gladiator Sports`,
`Amorosi MMA`, `F-5 Grappling`, plus `Louisiana Judo` and `Tulsa Judo` flagged as candidates — while
the actual standard was grappling arts broadly. One of those rejections reached production.

**`RULES-tjjm.md` has no inclusion criterion at all.** It should gain one:

> **Scope.** A record belongs in the directory if the school teaches a grappling art —
> Brazilian jiu jitsu, judo, wrestling, submission grappling or no-gi. Striking-only schools
> (karate, taekwondo, kickboxing, Muay Thai) do not qualify. **MMA schools usually teach grappling
> — verify rather than assume in either direction.** A named class on the school's own page is the
> evidence; a meta description is not.
