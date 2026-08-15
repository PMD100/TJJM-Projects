# METHOD RULES — batch 7 addendum (TN, NS, NB, NL, PE, DE, DC, AK)

Read `METHOD-RULES-agent.md` first. Everything in it applies. This file adds the traps specific
to batch 7 and **overrides its batch-specific inserts** — the Iowa/Manitoba/`Flin Flon` notes in
that file belong to batch 3 and are not relevant here.

---

## Why this batch is different

Batch 7 is eight *small* regions rather than one or two big ones. The dominant failure mode is
therefore not link rot — it is **the wrong region entirely**. Batch 6 filed nine records in the
wrong province or country and every one of them returned HTTP 200. This batch has more
same-name-different-place collisions than any batch so far, and several of them are **between two
regions that are both in this batch**, which makes a misfile almost invisible.

**Check the region on every single candidate. Read it off the page body — a postal code, a phone
area code, a street address, a "find us" line. Not the domain, not the title tag.**

---

## The four collisions inside this batch

These are the dangerous ones, because a record misfiled between them looks correct from every
angle except the one nobody checks.

### 1. Saint John NB ⟷ St. John's NL — the worst one
Two different cities, two different provinces, both in this batch.

- **Saint John** — New Brunswick. Never apostrophe-s. Postal codes `E2*`. Area code 506.
- **St. John's** — Newfoundland. Always apostrophe-s. Postal codes `A1*`. Area code 709.

New Brunswick also has a **St. John River** and a **Saint John County**. Newfoundland has a
**St. John's** and, separately, **Portugal Cove-St. Philip's**. Do not let the string decide.
If a page says "Saint John" and the postal code starts `A1`, the page is wrong, not the rule.

### 2. Georgetown — three of them, all in this batch
- **Georgetown, PE** — a real town on Prince Edward Island (pop. ~700).
- **Georgetown, DE** — the seat of Sussex County, Delaware.
- **Georgetown, DC** — a *neighbourhood* of Washington, not a city. See the DC rule below.

Also Georgetown TX, KY, ON, and Guyana. A `georgetownbjj.com` proves nothing.

### 3. Cornwall and Stratford — PE ⟷ ON ⟷ England
- **Cornwall, PE** (pop. ~5,000) vs **Cornwall, ON** (pop. ~47,000) vs **Cornwall, England** (a county).
- **Stratford, PE** (pop. ~10,000) vs **Stratford, ON** (the festival town) vs **Stratford-upon-Avon**.

Ontario is *not* in this batch, so a Cornwall ON or Stratford ON school is a **cross-region debt**
to file for later, not a PEI record.

### 4. Dover and Smyrna — DE ⟷ TN, both in this batch
- **Dover, DE** — state capital. Also **Dover, TN** (Stewart County), plus Dover NH, NJ, OH, England.
- **Smyrna, DE** — Kent County. Also **Smyrna, TN** (a real BJJ town near Nashville), plus Smyrna GA.

Both pairs straddle two regions in this batch.

---

## Region-by-region traps

### Tennessee (34 records — the big one)
- **Bristol** is a twin city split across the state line. **Bristol TN and Bristol VA are different
  municipalities sharing one main street.** A school on the Virginia side is a Virginia record.
  Check the address. There is also Bristol, England.
- **Cleveland, TN** (near Chattanooga) vs **Cleveland, OH**. A `clevelandbjj`-style domain is
  overwhelmingly likely to be Ohio.
- **Clarksville, TN** — batch 6 already caught a *Clarksville, Maryland* school misfiled as West
  Virginia. There is also Clarksville IN and AR. Tennessee's is the real large one (Fort Campbell).
- **Franklin, TN** vs Franklin PA/IN/MA/NC/WI. Tennessee's is the affluent Nashville suburb.
- **Columbia, TN** vs Columbia SC (curated batch 5), MO, MD.
- **Jackson, TN** vs Jackson MS (curated batch 5), MI, WY.
- **Lebanon, TN** vs Lebanon PA/OH/NH/IN — and the country.
- **Springfield, TN** vs Springfield MO/IL/MA/OH.
- **Morristown, TN** vs Morristown NJ.
- **Athens, TN** vs Athens GA/OH/AL — and Greece. One of Tennessee's two known stubs is
  `Athens Brazilian Jiu-Jitsu`.
- **Paris, TN** and **Milan, TN** are both real towns. Do not reject them as data errors.
- **Kingston, TN** is real — but `METHOD-RULES-agent.md` already records that `kingstonbjj.com`
  and `kingstonjiujitsu.com` are both **Kingston upon Thames, England**.
- Memphis sits on the **TN/MS/AR** tri-state line. Southaven/Olive Branch MS and West Memphis AR
  are not Tennessee. Mississippi and Arkansas are both already curated — file as cross-region debt.
- Nashville and Knoxville have heavy franchise density. Diff brand rosters against the whole state.

### Washington DC (7 records — one "city")
- ⚠️ **Every DC record must use the city string `Washington`.** The section groups by exact city
  string, so a record filed as `Georgetown`, `Capitol Hill`, `Navy Yard`, `Petworth`,
  `Columbia Heights`, `NoMa`, `Shaw` or `H Street` silently creates a second city heading for what
  is one city. This is condition C8 and DC is the likeliest region in the batch to trip it.
- ⚠️ **The DC metro trap.** Schools in **Arlington, Alexandria, Falls Church, Fairfax (VA)** and
  **Bethesda, Silver Spring, College Park, Hyattsville (MD)** market themselves relentlessly as
  "DC" or "DMV" schools. They are **not** DC records. Virginia and Maryland are both already
  curated — file them as cross-region debt.
- Conversely, do not reject a genuine DC school because its name says Virginia.
- Do not confuse Washington **DC** with Washington **state** (121 records, already curated).

### Delaware (7 records)
Delaware is small and almost every city name is a homonym of somewhere bigger:
- **Newark, DE** (University of Delaware) vs **Newark, NJ** — New Jersey has 210 records. This is
  the single most likely misfile in Delaware.
- **Wilmington, DE** vs **Wilmington, NC** — North Carolina's has a large BJJ scene.
- **Dover, DE** vs Dover TN (this batch), NH, NJ.
- **Middletown, DE** vs Middletown NY/CT/OH/RI.
- **Milford, DE** vs Milford CT/MA/NH.
- **Lewes, DE** is pronounced "Lewis" and is often misspelled that way.
- Delaware's known stub is `Rehoboth Beach BJJ`. Rehoboth Beach is real and small; a school there
  is plausible but verify it is not actually in Lewes or Millsboro.
- Philadelphia and Baltimore are both close. A "Delaware Valley" school is usually Pennsylvania.

### Alaska (22 records)
- **Eagle River** and **Girdwood** are inside the Municipality of Anchorage but are normally listed
  as their own communities. Whichever you choose, be consistent — an inconsistent choice creates a
  duplicate city heading (C8).
- **JBER** (Joint Base Elmendorf-Richardson) and other military-base clubs are frequently
  **not open to the public**. A base gym's BJJ club is not a directory listing unless civilians
  can train there. Say so explicitly in your verdict.
- **North Pole, AK** is a real city near Fairbanks. Do not reject it.
- **Utqiagvik** was renamed from **Barrow** in 2016. Both strings appear in sources; pick one.
- Alaska has genuine **seasonal and volunteer-run** clubs that close for months. A dormant site is
  not necessarily a closed school — but a club with no fixed address is not a directory record either.
- Wasilla / Palmer / the Mat-Su valley is the second population centre after Anchorage and Fairbanks.
- Distances are enormous. Do not assume a "Southeast Alaska" school serves Anchorage.

### Nova Scotia (23 records)
- ⚠️ **Sydney, NS** vs **Sydney, AUSTRALIA.** Nova Scotia's is on Cape Breton, pop. ~30,000. An
  Australian result is very easy to land on and every signal except the country looks right.
- ⚠️ **Liverpool, NS** vs **Liverpool, ENGLAND.**
- **Windsor, NS** vs Windsor ON vs Windsor, England — `METHOD-RULES-agent.md` already flags Windsor.
- **Amherst, NS** vs Amherst MA/NY.
- **Dartmouth** and **Bedford** are part of **Halifax Regional Municipality** but are conventionally
  listed as their own cities. Note there is also a **Bedford, TX** carrying a blank override — see
  the silent-blank list below.
- **Sackville, NS** vs **Sackville, NB** — both real, both in this batch's neighbourhood. Nova
  Scotia's Lower Sackville is in HRM; New Brunswick's Sackville is near the Tantramar marshes.
- Known stubs: `Stellarton BJJ`, `Yarmouth BJJ`. Both towns are real and small.
- Antigonish, Truro, New Glasgow, Bridgewater, Kentville and Wolfville are the realistic
  non-Halifax candidates. Prioritise breadth across them over depth in Halifax.

### New Brunswick (15 records)
- **Saint John** — see the batch-internal collision above. Never "St. John's", never "St. John".
- **Moncton / Dieppe / Riverview** are three separate municipalities forming one urban area.
  A Dieppe school is not a Moncton record. There is also **Dieppe, France**.
- **Miramichi** was amalgamated from Chatham and Newcastle in 1995; older sources use the old names.
  There is also a Newcastle in England, Australia and Ontario.
- **Bathurst, NB** vs Bathurst NSW Australia and Bathurst ON.
- New Brunswick is officially bilingual. A school may trade under a French name
  (`jiu-jitsu brésilien`) — that is not evidence it is in Quebec.
- Known stubs: `Campbellton BJJ`, `Miramichi BJJ`, `Moncton BJJ`, `Saint John BJJ` — four of
  fifteen records, the highest stub ratio in the batch. Expect real schools behind some of them:
  Moncton and Saint John are the two largest cities and almost certainly have real BJJ.

### Newfoundland and Labrador (15 records)
- ⚠️ **See the C7 section below before proposing anything.** NL is stored under Nebraska's code.
- ⚠️ **The eight cities currently in use are St. John's, Paradise, Conception Bay South,
  Corner Brook, Gander, Grand Falls-Windsor, Clarenville and Labrador City.** Two more —
  Mount Pearl and Torbay — are permitted but unused. **Any other city requires a section change.**
  If you find a school in Stephenville, Happy Valley-Goose Bay, Carbonear, Bay Roberts, Marystown,
  Placentia, Deer Lake, Bonavista or Channel-Port aux Basques, **report it and flag the city
  explicitly** — it cannot simply be added.
- **Mount Pearl, Paradise and Conception Bay South** are separate municipalities inside the
  St. John's metro. Do not collapse them into St. John's.
- **Labrador** is physically separate from the island. Labrador City and Happy Valley-Goose Bay are
  a thousand kilometres from St. John's.
- **Springdale, NL** is a real town — but `METHOD-RULES-agent.md` names `Springdale BJJ` as a real
  operating school, and that one is in **Arkansas**. Do not conflate them.
- The current NL roster is dominated by schools named **Foley** (Jason Foley Martial Arts, Foley's
  Martial Arts, Alex Foley's Academy, Michael Foley's Academy). This is a genuine local martial-arts
  family, not a duplication error — but check carefully that they are four distinct schools at four
  distinct addresses and not one school listed four ways.

### Prince Edward Island (10 records)
- **Cornwall**, **Stratford**, **Georgetown** — all three are batch-internal or cross-region
  collisions. See above.
- PEI's total population is ~175,000. **Ten records may already be near-complete.** This is the one
  region in the batch where the "every region doubles" heuristic probably does not hold. Do not
  invent schools to hit a ratio. A short honest roster is the correct output.
- Charlottetown and Summerside are the only towns of any size.
- Known stub: `Souris Brazilian Jiu-Jitsu`. Souris is a fishing town of ~1,000 people. Treat a
  BJJ academy there as unlikely-but-possible and require real evidence either way.
- There is also a **Souris, Manitoba** (curated batch 3).

---

## ⚠️ C7 — the Newfoundland / Nebraska entanglement

**Newfoundland records are stored with `s:"NE"`, Nebraska's code.** The two pages are separated
only by a hardcoded city list inside `sections/tjjm-state-directory.liquid`. Three consequences:

- **C7a** — no new Nebraska record may use a city in the NL list.
- **C7b** — the suppression check runs *before* the city split, so **the `NE` removed-index row
  applies to both pages**. A name suppressed for Nebraska is also suppressed for Newfoundland.
  There is no `NL` row and there cannot be one. Nebraska currently suppresses twelve names:
  Columbus NE BJJ · Fremont BJJ · Grand Island BJJ · Hastings BJJ · Husker Combat Club ·
  Kearney BJJ · Lincoln BJJ · Nebraska BJJ · Norfolk BJJ · Norfolk NE BJJ · North Platte BJJ ·
  Scottsbluff BJJ. **No Newfoundland school may share a name with any of these.**
- **C7c** *(new this batch)* — **a Newfoundland record in a city outside the hardcoded list renders
  on the Nebraska page instead.** It does not error. It does not vanish. It appears under Nebraska.

**Nebraska is already curated (batch 5, 21 live records) and is NOT in scope.** Do not research it,
do not propose changes to it. Its count must be identical before and after batch 7.

---

## Names that already carry a blank override

A new record sharing a name with one of these renders **with no link at all**:

`Jungle Gym Martial Arts` · `Action & Reaction MMA` · `Ethos BJJ` · `Alliance Jiu Jitsu Easley` ·
`Ironside Martial Arts`

`Ethos BJJ` is a plausible name for a new school anywhere. If you propose a name on this list,
say so explicitly in your output.

---

## What to hand back

Exactly as `METHOD-RULES-agent.md` §"What to produce", plus:

- **State the region evidence for every record** — the postal code, area code or street address you
  read, and where on the page you read it. "The domain says NS" is not region evidence.
- **Flag any Newfoundland city outside the ten permitted strings.**
- **Flag any DC record whose city string is not literally `Washington`.**
- **Anything that turns out to belong to an already-curated region** (VA, MD, ON, NJ, NC, MS, AR,
  WA, NH, SC, PA, OH) → report it under a heading `CROSS-REGION DEBT`. Do not discard it and do not
  file it here.
- If you could not read a body, the answer is **UNVERIFIED**. Never invent evidence. A research
  agent on batch 6 fabricated a black-belt lineage and it survived three checks.
- If you run out of context or budget, **say so and name the affected rows.**
