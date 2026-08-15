# Batch-7 BEFORE/AFTER Render Sweep — 61 Regions

- BEFORE theme (MAIN), preview_theme_id: `154865860780`
- AFTER theme (staged KK), preview_theme_id: `154881523884`
- Sweep run: 2026-08-13
- Method: strictly sequential `fetch(url, {credentials:'include'})` requests, explicit `preview_theme_id` on every request, unique cache-buster on every request, counts read from JSON-LD `numberOfItems` cross-checked against the `p.tjjm-p` body paragraph regex. No mismatches between the two extraction methods were found across all 61 regions × 2 themes (122 fetches).

## Control Results (run before the full sweep)

| Control | BEFORE | AFTER | Expected | Result |
|---|---|---|---|---|
| bjj-schools-alabama (not in batch-7) | 78 | 78 | identical (78/78) | PASS — harness is not forcing a fake diff |
| bjj-schools-tennessee | 34 | 52 | 34 → 52 | PASS — preview parameter is taking effect |

Both controls passed. Proceeded to the full 61-region sweep.

## Full Sweep Table

| handle | before | after | changed | expected-change |
|---|---|---|---|---|
| bjj-schools-alabama | 78 | 78 | no | no |
| bjj-schools-alaska | 22 | 14 | **yes** | yes (22→14) |
| bjj-schools-alberta | 72 | 72 | no | no |
| bjj-schools-arizona | 173 | 173 | no | no |
| bjj-schools-arkansas | 56 | 56 | no | no |
| bjj-schools-british-columbia | 101 | 101 | no | no |
| bjj-schools-california | 460 | 460 | no | no |
| bjj-schools-colorado | 156 | 156 | no | no |
| bjj-schools-connecticut | 85 | 85 | no | no |
| bjj-schools-delaware | 7 | 8 | **yes** | yes (7→8) |
| bjj-schools-florida | 328 | 328 | no | no |
| bjj-schools-georgia | 152 | 152 | no | no |
| bjj-schools-hawaii | 38 | 38 | no | no |
| bjj-schools-idaho | 45 | 45 | no | no |
| bjj-schools-illinois | 130 | 130 | no | no |
| bjj-schools-indiana | 80 | 80 | no | no |
| bjj-schools-iowa | 36 | 36 | no | no |
| bjj-schools-kansas | 37 | 37 | no | no |
| bjj-schools-kentucky | 65 | 65 | no | no |
| bjj-schools-louisiana | 100 | 100 | no | no |
| bjj-schools-maine | 23 | 23 | no | no |
| bjj-schools-manitoba | 21 | 21 | no | no |
| bjj-schools-maryland | 94 | 94 | no | no |
| bjj-schools-massachusetts | 140 | 140 | no | no |
| bjj-schools-michigan | 115 | 115 | no | no |
| bjj-schools-minnesota | 52 | 52 | no | no |
| bjj-schools-mississippi | 27 | 27 | no | no |
| bjj-schools-missouri | 98 | 98 | no | no |
| bjj-schools-montana | 33 | 33 | no | no |
| bjj-schools-nebraska | 21 | 21 | no | no — **must stay 21 both sides (entangled with Newfoundland); confirmed unchanged** |
| bjj-schools-nevada | 118 | 118 | no | no |
| bjj-schools-new-brunswick | 15 | 15 | no (count) | count unchanged, **membership changed** — see below |
| bjj-schools-new-hampshire | 33 | 33 | no | no |
| bjj-schools-new-jersey | 210 | 210 | no | no |
| bjj-schools-new-mexico | 34 | 34 | no | no |
| bjj-schools-new-york | 182 | 182 | no | no |
| bjj-schools-newfoundland-and-labrador | 15 | 13 | **yes** | yes (15→13) |
| bjj-schools-north-carolina | 125 | 125 | no | no |
| bjj-schools-north-dakota | 11 | 11 | no | no |
| bjj-schools-nova-scotia | 23 | 29 | **yes** | yes (23→29) |
| bjj-schools-ohio | 137 | 137 | no | no |
| bjj-schools-oklahoma | 98 | 98 | no | no |
| bjj-schools-ontario | 107 | 107 | no | no |
| bjj-schools-oregon | 118 | 118 | no | no |
| bjj-schools-pennsylvania | 148 | 148 | no | no |
| bjj-schools-prince-edward-island | 10 | 10 | no (count) | count unchanged, **membership changed** — see below |
| bjj-schools-quebec | 63 | 63 | no | no |
| bjj-schools-rhode-island | 23 | 23 | no | no |
| bjj-schools-saskatchewan | 14 | 14 | no | no |
| bjj-schools-south-carolina | 34 | 34 | no | no |
| bjj-schools-south-dakota | 11 | 11 | no | no |
| bjj-schools-tennessee | 34 | 52 | **yes** | yes (34→52) |
| bjj-schools-texas | 351 | 351 | no | no |
| bjj-schools-utah | 46 | 46 | no | no |
| bjj-schools-vermont | 12 | 12 | no | no |
| bjj-schools-virginia | 137 | 137 | no | no |
| bjj-schools-washington | 121 | 121 | no | no |
| bjj-schools-washington-dc | 7 | 6 | **yes** | yes (7→6) |
| bjj-schools-west-virginia | 28 | 28 | no | no |
| bjj-schools-wisconsin | 85 | 85 | no | no |
| bjj-schools-wyoming | 10 | 10 | no | no |

**Grand totals:** BEFORE = 5,205. AFTER = 5,219. Both match the expected values exactly (Δ = +14).

**Count-level changes:** 6 regions (alaska, delaware, newfoundland-and-labrador, nova-scotia, tennessee, washington-dc) — exactly as expected, since new-brunswick and prince-edward-island have unchanged counts but changed membership (documented below). Total = 8 batch-7 regions affected, 53 unaffected. No region outside the batch-7 list moved. Not every region changed, and not zero regions changed — the sweep result is a genuine, bounded diff, not a harness defect.

## Membership-Change Confirmations (count unchanged, names differ)

**bjj-schools-new-brunswick** (15 → 15):
- Removed (BEFORE only): Campbellton BJJ, Miramichi BJJ, Moncton BJJ, Saint John BJJ, Woodstock NB BJJ
- Added (AFTER only): Restigouche Dojo, Victory Jiu-Jitsu Edmundston, MXT BJJ Miramichi, Team Flow State, B7 Jiu Jitsu
- 5 suppressed / 5 added — confirmed.

**bjj-schools-prince-edward-island** (10 → 10):
- Removed (BEFORE only): PEI Brazilian Jiu Jitsu, Island Grappling Club, Summerside BJJ PEI
- Added (AFTER only): JM Brazilian Jiu-Jitsu, Renzo Gracie PEI Lot 36, PEI Martial Arts Academy O'Leary
- 3 suppressed / 3 added — confirmed.

## AFTER-Side Spot Checks

1. **bjj-schools-newfoundland-and-labrador** — contains city heading "Jiu Jitsu in Flat Bay, NL" with school "Golden Rule Jiu Jitsu". Confirmed present on the NL page.
2. **bjj-schools-nebraska (AFTER)** — checked for "Flat Bay" heading and "Golden Rule Jiu Jitsu" school: NOT FOUND on the Nebraska page (21 gyms / 9 cities, unchanged from BEFORE). Confirms the Flat Bay section edit landed correctly and did not leak onto Nebraska.
3. **bjj-schools-washington-dc (AFTER)** — exactly ONE city heading in the directory section: "Jiu Jitsu in Washington, DC". No Georgetown, Capitol Hill, Navy Yard, or other neighbourhood headings. 6 schools listed (BETA Academy, Estilo Jiu Jitsu, Highstyle Jiu-Jitsu, N-Flux, Underworld BJJ DC, Vortex Jiu-Jitsu), matching count 6.
4. **bjj-schools-nova-scotia (AFTER)** — contains "Jiu Jitsu in Windsor, NS" (new city heading) and "Jiu Jitsu in Chéticamp, NS" (renders with correct accented é, no mojibake).

All four spot checks PASS.
