# Nightly discovery — 2026-08-20

**Region swept:** Alabama (`AL`, `bjj-schools-alabama`) — cursor row 0, cycle 1.
**Cursor:** advanced 0 → 1 (cycle 1) at the start of the run, before any searching.
**Outcome:** 3 schools added — the nightly cap. Staged, not live.

---

## Corpus position

| | |
|---|---|
| Corpus records (all regions) | 5,911 |
| Suppressed by `tjjm-removed-index` | 696 |
| **Published before this run** | **5,215** |
| AL corpus rows | 86 |
| AL suppressed (8 names) | Anniston BJJ, Decatur BJJ Alabama, Dothan BJJ, Gadsden BJJ, Bailey's Tiger Rock Martial Arts, WuDang Martial Arts Center, Guerrilla Fitness, Triad Martial Arts Academy |
| **AL published before** | **78** |
| **AL published after** | **81** |
| **Grand total after** | **5,218** |

Counts were **recomputed**, not incremented: corpus rows per region minus that region's
`tjjm-removed-index` names. The recomputation reproduces the previous published total of
**5,215 exactly**, and matches `count_at_setup` on 59 of 61 rows. The two that differ are
the documented Nebraska→Newfoundland re-filing (`NE` corpus 49 − 15 suppressed = 34 =
21 NE + 13 NL), so the model is sound and no other region's count was touched.

---

## Candidates found

Searched by major city, by association name, by "recently opened", and by walking the
city breakdown of a third-party index to find AL towns the corpus has no coverage in
(Saraland, Semmes, Bay Minette, Brownsboro, Harvest, Pike Rd, Fort Mitchell).
Third-party directories were used **only as lead sources** — never as evidence.

Ten candidates cleared dedupe (normalised name, website host ignoring `www.`, and
street address + city) against all 5,911 records, with fuzzy name containment as a
backstop. Zero collisions. All three added names are unique across the whole corpus, so
no override row can double-fire.

## Verified and added (3)

| Name | City | Address | Evidence |
|---|---|---|---|
| **Gracie Barra Trussville** | Birmingham | 5870 Trussville Crossing Blvd, Birmingham AL 35235 | Own site `/contact/`, host+path asserted in the same evaluation. The page's own schema.org `PostalAddress` gives `addressLocality: "Birmingham", postalCode: "35235"` — that settles the Trussville-vs-Birmingham question from the site itself rather than from a directory. Two GB black belts, kids/women/adults class pages. `kw` empty; all hidden links on-domain mobile nav. |
| **Ohm Jiu Jitsu** | Birmingham | 4420 4th Ave S, Birmingham AL 35222 | Own site `/contact/`, host+path asserted. "Ohm Jiu Jitsu is located at 4420 4th Ave S in Birmingham's Avondale neighborhood." Live weekly schedule (beginners Mon–Thu 5:30pm, Friday open mat), © 2026. `kw` empty, zero hidden links. |
| **McLean's Martial Arts & Fitness** | Saraland | 627 Saraland Blvd S, Saraland AL 36571 | Own site `/martial-arts-programs`, host+path asserted. "Brazilian Jiu Jitsu" is a standing programme alongside Little Dragons / Youth / Teen / Adult — this is exactly the mixed-discipline school a striking-only screen would wrongly reject. Only `kw` hit was `slots` from Wix `slots=`, a known false-positive generator. |

⚠️ **Address correction on McLean's.** The third-party index gave `1490 Celeste Rd`. The
school's own site publishes `627 Saraland Blvd S`. The site was taken as authoritative.
Worth a second look on a future pass in case they run two locations.

## Rejected (2) — see `additions/rejected-2026-08-20.tsv`

- **Apex Academy of Jiu Jitsu** — site is live, is a real BJJ school, passed the spam
  probe, and passed dedupe. Rejected anyway because it **publishes no street address**:
  the site says only "Jiu Jitsu in Gardendale, AL" plus a phone number, and third-party
  sources conflict (224 Decatur Hwy Ste 222 **Fultondale** vs 528 Decatur Hwy Ste 116
  **Gardendale**). Its Facebook page returned an empty body behind the login wall.
  Requirement 3 not met, city not unambiguous → not added. This is the closest miss of
  the night and is worth one retry later.
- **Heroes Martial Arts Academy Trussville** — duplicate. The corpus already holds
  `HEROES MARTIAL ARTS ACADEMY`, Birmingham, host `heroesmma.com`.

## Verified-but-unadded / unreached — `additions/pending-verification.tsv`

Five leads passed dedupe but were **not** browser-verified, because the run stopped at
the 3-addition cap: Johnson's Martial Arts Academy (Montgomery), Fleming's Martial Arts
(Montgomery), Panda BJJ & MMA (Saraland), Huntsville Judo Club, and Rubicon Jiu Jitsu &
Self Defense. **Rubicon is probably Georgia, not Alabama** — Yelp files it under Phenix
City but the school self-describes as Columbus, Georgia's. Confirm the state first.

Alabama towns not reached at all tonight: Semmes, Bay Minette, Brownsboro, Harvest,
Pike Rd, Fort Mitchell, plus the smaller Wiregrass and Shoals towns.

---

## Staging

Upserted to **`gid://shopify/OnlineStoreTheme/155080032428`** — "TJJM ADDITIONS STAGING",
role `UNPUBLISHED`. Nothing was written to MAIN and nothing was published.

| File | Bytes | Local MD5 | API `checksumMd5` | |
|---|---|---|---|---|
| `snippets/tjjm-gyms-data-46.liquid` | 2,751 | `0d639622de64cf416520382337c98d6d` | `0d639622de64cf416520382337c98d6d` | ✅ match |
| `snippets/tjjm-region-index.liquid` | 3,692 | `2eaf0475c59e49b87e45a19b7fb27ac3` | `2eaf0475c59e49b87e45a19b7fb27ac3` | ✅ match |

Bodies sent as `BASE64`. Both re-queried after the write; checksums confirmed.

`tjjm-gyms-data-46.liquid` is at **2,751 of 24,576 bytes** — 21,825 bytes of headroom,
roughly 140 more records at this record size. No ceiling concern yet. Its existing
header comment was preserved byte-for-byte; only the array between `[` and `]` changed.
`tjjm-gyms-data.liquid` was not touched.

## For the owner — needs a manual pass, not changed here

The **Alabama** region page (`/pages/bjj-schools-alabama`) carries `title_tag` and
`description_tag` metafields with hand-written counts embedded in them. Those now read
78 and are stale. **Alabama is the only region affected by tonight's run.** Batch these
when convenient — the page body, JSON-LD `numberOfItems`, and card count all compute
themselves from the data and are already correct.

## Not flagged

No 24,576-byte ceiling hit. No checksum mismatch. Cursor did not wrap — it is at row 1
of 61 in cycle 1, so 60 regions remain in this cycle.
