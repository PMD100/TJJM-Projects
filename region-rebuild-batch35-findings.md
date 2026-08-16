# Batch 35 — the browser render pass. "EMPTY" turned out to mean "broken."

Session of 15 Aug 2026. Built as theme **NNN** (`154962034860`), **staged and awaiting publish**.
Overrides only. **Record counts cannot have moved.**
**Publish NNN `154962034860`.** MMM `154960527532` becomes the rollback.

---

## The headline

198 links that returned nothing to a plain HTTP fetch were opened in a real Chrome browser.

| verdict | n | share |
|---|---|---|
| **DEAD** | **80** | 40.4% |
| OK | 61 | 30.8% |
| **PARKED** | **37** | 18.7% |
| **REPLACE — school found at a new URL** | **8** | 4.0% |
| **WRONG_BUSINESS** | **7** | 3.5% |
| **HIJACK** | **5** | 2.5% |

**137 of 198 were broken — 69%. By far the worst rate of any screen in this programme**, against a
dirty-bucket rate of 10% and an `https://` tail rate of under 3%.

### We had been reading EMPTY wrong for the whole programme
Across batches 21–31 these rows were logged as *"JS-rendered, needs a browser"* and left live on the
assumption that most were healthy sites a fetch simply could not parse. They were not. The dominant
causes are mundane, and every one of them returns an empty body to a fetcher:

- **Wix "domain not connected"** placeholders — the most common single cause
- **Expired Squarespace accounts** (10th Planet Downtown, Lucas Leite, Ryuko, Yukon, Carlson Gracie Garden Grove …)
- **Flywheel and cPanel default pages**, Netlify "site not found", Wodify "account gone"
- **Cloudflare 1001 / 520 / 522** origin errors
- **GoDaddy and Afternic `/lander` redirects** — a parked domain that a fetch reads as blank

> **Rule change: treat EMPTY as SUSPECT, not as unknown.** Any row a fetch cannot read goes to a
> browser before its link is trusted. If it cannot be browsed, it is safer blanked than left live.
> This is written into the header of `tjjm-gym-websites-4.liquid`.

### Eight recoveries
`Alliance Jiu-Jitsu Carlsbad` · `Brazen Martial Arts` · `Cesar Gracie Jiu Jitsu` ·
`Chris Lisciandro's Street Sports BJJ Club` · `Raven Brazilian Jiu-Jitsu` ·
`Rockland Brazilian Jiu-Jitsu` (now Renzo Gracie Rockland) · `Significant Strikes` ·
`West Coast Jiu-Jitsu`

### Five more hijacks — sixty-one total
`Infinite Jiu-Jitsu Academy` → demoslotjackpot.com Indonesian slots ·
`East Lansing Underground` → Macau casino in Chinese ·
`Pejak Martial Arts` → Babe88 Indonesian slots ·
`Mmaxout Fitness` → Chinese sports-betting spam ·
`Abdias Brazilian Jiu-Jitsu` → offsite redirect Chrome itself blocked as unsafe.

---

## The gates earned their keep again

Four candidates were refused:

| name | gate | why |
|---|---|---|
| `Chris Lisciandro's Street Sports BJJ Club` | **C11** | corpus spells it with a **curly apostrophe** U+2019 |
| `Dan Henderson's Athletic Fitness Center` | **C11** | corpus name ends **"- Formerly Team Quest"** |
| `UFC GYM Sunnyvale` | C3 | already handled in batch 33 |
| `UFC Gym Green Valley` | C3 | already handled in batch 33 |

The first two would have written rows that **matched no record at all** and reported success —
exactly the silent failure C11 exists to catch. Both were corrected to the true corpus names and are
included. The two UFC rows were correctly skipped.

## What was written

| file | was | now |
|---|---|---|
| `snippets/tjjm-gym-websites-4.liquid` | 982 B (empty) | **19,136 B · `ac671a322b366f2839e78aafa6572ac9`** |

Byte-identical to the local build in `build-b35/`. **8 repoints + 127 blanks = 135 rows.**
First use of the new file created in batch 34 — no section had to be touched.

### Verified
The merge was recomputed locally from the exact four override files now in NNN. This is the same
algorithm the page itself runs, and it has matched the live page exactly in every batch since 30.

```
cross-file duplicate names (gate C3)   none
records published                      5,215   unchanged
with a link                            4,170   was 4,297 — exactly minus 127
link-free                              1,045
override entries                       1,139   was 1,004 — exactly plus 135
blanking entries                         838   was   711 — exactly plus 127
regions disagreeing with region-index   NONE (0 of 61)
```

⚠️ **Not verified in a live browser.** The Chrome extension entered a hard "site is blocked" state
during the agent's run (row 197's redirect target tripped Chrome's safety block) and had not
recovered. Worth loading `/pages/jiu-jitsu-schools-near-you` yourself after publishing and checking
the counter reads **5,215**.

⚠️ **One row unverified.** `GB Fulshear` (row 198) was never rendered for the same reason. It is
untouched by this batch, and batch 33 already repointed it to `gbfulshear.com`.

---

## Where the directory stands

| | |
|---|---|
| records published | **5,215** across 61 regions |
| with a link | **4,170** |
| deliberately link-free | **1,045** |
| links read or swept | **4,293** — every link has now had at least a DNS + parking check |
| harmful or broken links removed | **445** |
| links repointed to a correct URL | **215** |
| override capacity remaining | ~5,400 B in file 4, plus files 5 and 6 empty (~47,000 B) |

**One in five listed schools now deliberately shows no link.** That is the honest state of the web
for this industry, and it is the right answer under your rule — a good link or no link.

## Next

1. **The 25 social/booking rows** left out of this pass (`browser-queue` minus the 198): Facebook
   and Instagram pages, `business.site`, Zenplanner, Mindbody. A browser can read these; the
   question is whether each is the school's own page or a bare brand homepage.
2. **162 more social/aggregator links** never screened (`scratch/park-sweep/social-deferred.tsv`).
3. **The identity pass** — wrong-location and wrong-school links a content screen passes cleanly.
   The 7 WRONG_BUSINESS rows here are a reminder this tier is still untouched.
4. **1,045 link-free records.** With the harm work now essentially complete, this is where the
   remaining value is: finding the real, current URL for schools that are alive but unlinked.
