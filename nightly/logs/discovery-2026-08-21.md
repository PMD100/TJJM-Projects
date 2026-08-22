# Nightly discovery — 2026-08-21

**Region swept:** Alaska (`AK`, `bjj-schools-alaska`) — cursor row 1, cycle 1.
**Cursor:** advanced 1 → 2 (cycle 1) at the start of the run, before any searching.
**Outcome:** 3 schools added — the nightly cap. Staged, not live.

---

## Corpus position

| | |
|---|---|
| Corpus records (all regions) | 5,911 |
| Suppressed by `tjjm-removed-index` | 696 records (694 distinct names) |
| **Published before this run** | **5,218** |
| AK corpus rows | 24 |
| AK suppressed (10 names) | Alaska Center For The Martial Arts, Arctic Warrior Brazilian Jiu-Jitsu, Eclipse Martial Arts, Gracie Barra - Jiu Jitsu, Greatland Martial Arts, Krav Maga Anchorage, Shoshin Ryu, Shoshindo of Alaska, The International Karate Association & College of the Martial Arts, Tonbo Dojo - Alaska Samurai Arts |
| **AK published before** | **14** |
| **AK published after** | **17** |
| **Grand total after** | **5,221** |

Counts were **recomputed** across all 61 rows, not incremented. The recomputation
reproduces every row of the current index exactly, with the single documented exception of
the Nebraska/Newfoundland pair: computed `NE` 34 = index `NE` 21 + index `NL` 13, because
NL records are miscoded `NE` in source and re-filed by city list in the section. **No other
region disagreed**, so nothing was written on a shaky model.

### One refinement to the counting method, worth recording

Suppression must be counted **per record, not per name**. The removed-index holds **694
distinct names**, but those names match **696 corpus records**, because two suppressed names
each hit two rows:

- `Capital MMA & Elite Fitness` (VA) → 2 records
- `Southern Maryland Martial Arts & Fitness` (MD) → 2 records

Counting names instead of records would have under-suppressed by 2 and thrown VA and MD off
by one apiece. This is the same duplicate-name hazard the brief warns about, showing up on
the suppression side rather than the addition side.

---

## Candidates found

Searched by major city (Anchorage, Fairbanks, Juneau, Wasilla, Palmer, Kenai/Soldotna,
Kodiak, Sitka, Homer), by association name, and by walking a third-party index's Alaska
city breakdown to find towns with no corpus coverage. The single most productive lead
source was **Alaska Judo** (`alaskajudo.org`), the USA Judo state governing body, whose
schools page lists eleven clubs across nine towns — judo being squarely in scope and almost
entirely absent from the corpus's Alaska rows, which skew BJJ and Anchorage.

Third-party directories were used **only as lead sources**, never as evidence.

Fifteen candidates were run through dedupe (normalised name, website host ignoring `www.`,
street address + city, plus fuzzy name containment as a backstop) against all 5,911 records.
Thirteen cleared; the two that did not are recorded below. All three added names are unique
across the whole corpus, so no override row can double-fire.

## Verified and added (3)

| Name | City | Address | Evidence |
|---|---|---|---|
| **Southside Jiu-Jitsu Academy** | Anchorage | 801 East 82nd Avenue C9-C10, Anchorage AK 99518 | Own site, host+path asserted in the same evaluation. Footer CONTACT block publishes the street address in full. Live weekly grid with Gi, No-Gi, Judo, Kids and Open Mat; © 2026. `kw` empty, zero hidden links. Notable as a genuine gap: the third-party index describes this school in its Alaska prose but does not list it on its Anchorage city page. |
| **Anchorage Dojo** | Anchorage | 3707 Woodland Dr Unit #2, Anchorage AK | Own site `/contact`, host+path asserted. Publishes "3707 Woodland Dr. Unit #2 Anchorage Alaska". Site banner reads "We Teach : Kodokan Judo" — grappling confirmed from the school itself, and it is a registered club of the state governing body. `kw` empty; hidden links on-domain only. |
| **Mat-Su Judo** | Wasilla | 650 E Bogard Rd, Wasilla AK 99654 | Own site `/contact-us`, host+path asserted: "Practice Location — Wasilla Middle School, 650 E Bogard Rd, Wasilla, AK 99654", with door-by-door entrance directions. Home page describes the judo curriculum in the school's own words. `kw` empty; hidden links on-domain only. |

⚠️ **Note on Mat-Su Judo.** Its published street address is a school gymnasium it rents,
not premises it owns. It clears requirement 3 as written — a street address in the region,
city unambiguous, published on its own site — and this is the normal arrangement for
community judo clubs. Flagging it so the owner can decide whether rented-venue clubs belong
in the directory as a class; if not, this record is the one to pull.

## Rejected (6) — see `additions/rejected-2026-08-21.tsv`

- **Black Bear Judo** (Ketchikan) — `campbushido.com` turns out to be a *summer camp* site
  (Camp Bushido, July 2026 dates), not the school's own site, and publishes no street
  address. Shares only the sensei's email. Fails requirements 1 and 3.
- **907 Grappling at Krav Maga Anchorage** — duplicate. Corpus holds `Krav Maga Anchorage`
  on the same host. Caught by both the host rule and the containment backstop.
- **Team Caique BJJ at Pioneer Grappling Academy** (Palmer) — duplicate. Corpus holds
  `Team Caique Jiu-Jitsu Alaska`, Palmer, same host `cjjusaalaska.com`. The names look
  unrelated; only the host rule caught this one, which is a good argument for keeping it.
- **North Star Judo Club** (Fairbanks) — has no site of its own; the governing body lists
  the Alaska Krav Maga & Fitness site as its website, and the corpus already carries that
  school. Fails requirement 1.
- **Sitka Judo Club** — email and phone only. Fails requirements 1 and 3.
- **Sterling Judo Club** — meets at Sterling Elementary School, no site of its own.

## Verified-but-unadded / unreached — `additions/pending-verification.tsv`

Six leads cleared dedupe but were **not** browser-verified, because the run stopped at the
3-addition cap:

- **Redemption Mixed Martial Arts** (Soldotna, 44619 Sterling Hwy Unit 4A) — no own-site URL
  identified yet.
- **All American Training Center** (35930 Kenai Spur Hwy) — wrestling/multi-sport.
  ⚠️ **City ambiguous:** the third-party index files it under *Soldotna*, but that address is
  in *Kenai*. Resolve from the school's own site before adding.
- **Excel Judo** (Palmer) — runs inside Excel Gymnastics; the only site is the gymnastics
  host, so requirement 1 is doubtful.
- **McGrath Judo** (McGrath, 38 Amos) — own Facebook page; needs the browser, since the
  fetcher returns blank for Facebook as a class.
- **Capital City Judo** (Juneau) — ⚠️ **unverifiable tonight.**
  `capitalcityjudo.com` returns `ERR_SSL_VERSION_OR_CIPHER_MISMATCH` on both apex and `www`.
  The address is third-party only, and "#369" at a mall reads like a mailbox rather than a
  training venue. Worth a retry once the TLS config is fixed — Juneau currently has just one
  record in the corpus.
- **KUC Judo Club** (Bethel) — Facebook *group*, not a page, and no street address.

Alaska towns not reached at all tonight: Kodiak, Sitka (beyond the judo club), Homer,
Seward, Valdez, Nome, Utqiagvik, Dillingham, Cordova, Petersburg, Wrangell, Haines,
Delta Junction, Girdwood and Talkeetna. Kodiak and Sitka were searched directly and returned
nothing; the rest are untouched.

---

## Staging

Upserted to **`gid://shopify/OnlineStoreTheme/155080032428`** — "TJJM ADDITIONS STAGING",
role `UNPUBLISHED`. Nothing was written to MAIN and nothing was published.

**Store guard passed all three checks before the first write:**
`shop.myshopifyDomain` = `7f7e22.myshopify.com`; `theme.name` begins "TJJM ADDITIONS
STAGING"; `theme.role` = `UNPUBLISHED`.

| File | Bytes | Local MD5 | API `checksumMd5` | |
|---|---|---|---|---|
| `snippets/tjjm-gyms-data-46.liquid` | 3,151 | `eba03058b693bc5f5f13b9ca02e897de` | `eba03058b693bc5f5f13b9ca02e897de` | ✅ match |
| `snippets/tjjm-region-index.liquid` | 4,119 | `73e3c05c07281aeaff2904a381d5f4c1` | `73e3c05c07281aeaff2904a381d5f4c1` | ✅ match |

Bodies sent as `BASE64`. Both re-queried after the write; checksums confirmed, role still
`UNPUBLISHED`.

`tjjm-gyms-data-46.liquid` is at **3,151 of 24,576 bytes** — 21,425 bytes of headroom, on
the order of 130 more records at this record size. No ceiling concern. Its header comment
was preserved byte-for-byte (asserted programmatically before writing); only the array
between `[` and `]` changed. `tjjm-gyms-data.liquid` was not touched.

Pre-write validation on the local file: JSON parses, 6 records, no key outside
`n/c/s/w/a`, no empty values, no `|` or `~` in any name, zero name collisions against the
5,911-record corpus, no internal duplicates, every `s` code present in the region index,
file ends with a newline.

## For the owner — needs a manual pass, not changed here

The **Alaska** region page (`/pages/bjj-schools-alaska`) carries `title_tag` and
`description_tag` metafields with hand-written counts embedded in them. Those now read 14
and are stale. **Alaska is the only region affected by tonight's run** — though note that
**Alabama** from last night's run is still outstanding if it has not been batched yet. The
page body, JSON-LD `numberOfItems`, and card count all compute themselves from the data and
are already correct.

## Not flagged

No 24,576-byte ceiling hit. No checksum mismatch. No region count disagreed outside the
known NE/NL case. Cursor did not wrap — it is at row 2 of 61 in cycle 1, so 59 regions
remain in this cycle.
