# Batch 31 — the dirty bucket is finished. 490 links read, 49 blanked.

Session of 15 Aug 2026. Built as theme **III** (`154956824748`), **staged and awaiting publish**.
Overrides only. **Record counts cannot have moved.**
**Publish III `154956824748`.** HHH `154955448492` becomes the rollback.

---

## The last four groups

| verdict | n | share |
|---|---|---|
| OK — a real grappling school's own site | 396 | 80.8% |
| EMPTY — JS-rendered or bot-walled, needs a browser | 45 | 9.2% |
| **WRONG_BUSINESS** | **15** | **3.1%** |
| **PARKED** | **12** | **2.4%** |
| **HIJACK** | **12** | **2.4%** |
| **DEAD** | **10** | **2.0%** |
| UNSURE | 0 | — |

**49 blanked — 10.0% actively bad.**

That is higher than the 6.7% measured across the earlier groups, and it should be: `all-targets.tsv`
is sorted by rot risk, so these were the dirtiest 490 links left in the corpus. **It is not a
corpus-wide rate and must not be projected as one.**

### The dirty bucket is now closed
All 8 `dirty-*.tsv` worklists are screened. Combined with the earlier `targets-*` groups and the two
bucket samples, **2,322 links have now been read.**

---

## The resolves-but-404 check earned its place on its first run

Added to the screening prompt this batch after the owner reported a 404 on the live site. It caught
two more immediately:

| record | URL | why every previous screen missed it |
|---|---|---|
| `GB Snoqualmie Valley` | `graciebarra.com/snoqualmie-wa` | `graciebarra.com` resolves fine — the *location page* 404s |
| `Gracie Barra Puyallup` | `graciebarra.com/puyallup-wa` | same |

A DNS screen sees a healthy domain. A "is this a martial arts site" screen sees graciebarra.com and
may well pass it. **Only reading the status of the exact URL catches these.** Any brand that
publishes per-location pages under one domain is exposed to this — Gracie Barra, 10th Planet,
Arashi-Do, Tiger Schulmann's, Easton. Worth a targeted sweep of every per-location URL we hold.

## Twelve more hijacks — fifty-six total

| record | what its domain now serves |
|---|---|
| `Sityodtong Northshore` | Thai slot gambling, luxury88 |
| `New Vision Academy of Jiu Jitsu` | Indonesian slots/casino, She777 |
| `Private Jewels Fitness` | redirects to PGBET Indonesian slots |
| `Boston Brazilian Jiu-Jitsu Newton` | redirects to Indonesian Togel SDY |
| `Maxx Training Center Martial Arts` | GACOAN88 Indonesian slots |
| `Royal Art BJJ` | redirects to MACAN123 Indonesian slots |
| `Comet BJJ` | Vietnamese Sunwin casino portal |
| `RYSE Academy of Martial Arts` | Chinese-language SEO spam portal |
| `Ring Sports United` | Turkish casino spam blog, Vodkabet |
| `Defense Combatives DEFCOM Alpha Fort Atkinson` | Aviator crash-game casino affiliate |
| **`Cascade Jiu-Jitsu`** | **the school's own real site, with an injected cialis/viagra paragraph** |
| **`Miller's Martial Arts Academy`** | **the school's own real site, with injected pharma links in the testimonials** |

The last two are the compromised-real-site pattern again — **six cases now**. They are genuinely the
school's site, genuinely the right school, and carrying paid spam. No screen that only asks "is this
a martial arts site?" will ever find them. Keep the second question in the prompt.

## Fifteen wrong-business links
Three Indiana schools that teach only Kenpo, Ryukyu Kempo or firearms/church security · a Muay Thai
gym with no grappling · two bare Facebook homepages standing in for schools · a taekwondo and
after-school-care business · a 24/7 fitness gym with kids karate · a boxing gym in Tulsa · a veteran
storytelling brand with a podcast and merch · a sport karate school · and two records pointing at
schools in the wrong state entirely (`Odyssey MMA`, VA record → South Amboy **NJ**;
`Disciple MMA Academy`, VA record → Greensboro **NC**).

---

## What was written

| file | was | now | change |
|---|---|---|---|
| `snippets/tjjm-gym-websites.liquid` | 8,766 B | **16,653 B** | 49 blanking entries added |

MD5-verified against theme III: `27ce9ee8b60612cf2fe28b2e1d18441c`, byte-identical to the local
build in `build-b31/`. **915 override entries, 635 blanking, zero duplicate names.**

Written to override file **1** rather than file 3 — file 1 had by far the most headroom
(8,766 B of a ~24,576 B ceiling) and precedence is irrelevant because gate C3 guarantees no name
appears in two files.

### Gates run before writing — all 49 passed
- **C5** no name contains `|` or `~`
- **C3** no name already present in `tjjm-gym-websites-2` or `-3`
- **C11** every name matches **exactly one** published record, so no row can silently blank a
  second gym
- no duplicates within the batch
- **BYTES** 16,653 < 24,576

### Structural guarantee
Every record-bearing file in III is byte-identical to HHH — legacy blob `1ee054…`, data-45
`8fb61a…`, removed-index `98ee61…`, region-index `8f4faa…`, both sections `633ec8…` / `0cb989…`,
websites-2 `08c171…`, websites-3 `ab606f…`, addresses `031ea9…`.

### Verified live on the III preview
The page was re-merged in the browser using the section's own algorithm:

```
records published   5,215   (unchanged — a blanking override cannot move a count)
with a link         4,373   (was 4,422 — exactly minus 49)
link-free             842   (was 793 — exactly plus 49)
override entries      915   (was 866 — exactly plus 49)
blanking entries      635   (was 586 — exactly plus 49)
```

All nine spot-checked records — including `GB Snoqualmie Valley`, `Gracie Barra Puyallup`,
`Odyssey MMA`, `Miller's Martial Arts Academy` and `Team O'Connor Brazilian Jiu-Jitsu` — render
with **no link**.

---

## Where the directory stands

| | |
|---|---|
| records published | **5,215** across 61 regions |
| with a link | 4,373 |
| deliberately link-free | 842 |
| links read | **2,322** |
| harmful links removed | **242** |
| links restored to a correct URL | 190 |

## Next

1. **The browser queue is now the biggest single job: 223 rows** — 217 EMPTY, 6 UNSURE — written to
   `scratch/hijack-screen/browser-queue-2026-08-15.tsv`. These are JavaScript-rendered, Cloudflare-
   fronted or Facebook bot-walled and a fetch cannot read them. Historically a browser pass converts
   about 40% of these to a verified good link, so this is worth roughly **90 recovered links** —
   the single largest available gain in accuracy.
2. **The per-location 404 sweep.** Every URL we hold with a path under a shared brand domain
   (`graciebarra.com/...`, `10thplanetjiujitsu.com/...`, `arashido.com/location/...`,
   `eastonbjj.com/...`). Small, targeted, and we now know the failure mode is real.
3. **The `https://` tail** — ~2,100 links never read. Low harm yield (measured 1.7% bad, 0%
   hijacked) but it is where the wrong-location links live. **Stratify by region**, not corpus-wide.
4. **842 link-free records.** Every one recovered makes the directory more useful and none can do
   harm while blank. This is the "largest directory" work rather than the "safest directory" work.
5. **The identity pass** — wrong-location and wrong-school links a content screen passes cleanly.
