# TJJM BJJ Directory Verification Sweep — Batch 8

**Date:** 2026-08-13
**BEFORE** = theme KK, `preview_theme_id=154881523884` (unpublished)
**AFTER** = theme LL, `preview_theme_id=154883129516` (unpublished)

Method: sequential `fetch(url, {credentials:'include'})` with an explicit `preview_theme_id` param and a unique cache-buster on every single request (both sides of every comparison, no parallel requests). Counts extracted from the JSON-LD `numberOfItems` field, not from the header/meta description. Names extracted from rendered `<div class="tjjm-gym"><h3>Name</h3>` blocks.

## Overall result

- **PART 1 (61-region count sweep): PASS.** All 61 region counts identical between BEFORE and AFTER. Both grand totals = **5,219**.
- **PART 2 (name diff, 11 touched regions): PASS.** All 14 expected renames (suppress+re-add pairs) present, exactly as specified, with nothing extra. All "must survive unchanged" checks passed.
- **PART 3 (address spot checks on AFTER): PASS.** All three address checks confirmed correct.

No collateral damage detected — no unexpected name appeared or disappeared anywhere.

---

## PART 1 — Count sweep, all 61 regions

| Region (handle suffix) | BEFORE (KK) | AFTER (LL) | Match |
|---|---:|---:|:---:|
| alabama | 78 | 78 | ✅ |
| alaska | 14 | 14 | ✅ |
| alberta | 72 | 72 | ✅ |
| arizona | 173 | 173 | ✅ |
| arkansas | 56 | 56 | ✅ |
| british-columbia | 101 | 101 | ✅ |
| california | 460 | 460 | ✅ |
| colorado | 156 | 156 | ✅ |
| connecticut | 85 | 85 | ✅ |
| delaware | 8 | 8 | ✅ |
| florida | 328 | 328 | ✅ |
| georgia | 152 | 152 | ✅ |
| hawaii | 38 | 38 | ✅ |
| idaho | 45 | 45 | ✅ |
| illinois | 130 | 130 | ✅ |
| indiana | 80 | 80 | ✅ |
| iowa | 36 | 36 | ✅ |
| kansas | 37 | 37 | ✅ |
| kentucky | 65 | 65 | ✅ |
| louisiana | 100 | 100 | ✅ |
| maine | 23 | 23 | ✅ |
| manitoba | 21 | 21 | ✅ |
| maryland | 94 | 94 | ✅ |
| massachusetts | 140 | 140 | ✅ |
| michigan | 115 | 115 | ✅ |
| minnesota | 52 | 52 | ✅ |
| mississippi | 27 | 27 | ✅ |
| missouri | 98 | 98 | ✅ |
| montana | 33 | 33 | ✅ |
| nebraska | 21 | 21 | ✅ |
| nevada | 118 | 118 | ✅ |
| new-brunswick | 15 | 15 | ✅ |
| new-hampshire | 33 | 33 | ✅ |
| new-jersey | 210 | 210 | ✅ |
| new-mexico | 34 | 34 | ✅ |
| new-york | 182 | 182 | ✅ |
| newfoundland-and-labrador | 13 | 13 | ✅ |
| north-carolina | 125 | 125 | ✅ |
| north-dakota | 11 | 11 | ✅ |
| nova-scotia | 29 | 29 | ✅ |
| ohio | 137 | 137 | ✅ |
| oklahoma | 98 | 98 | ✅ |
| ontario | 107 | 107 | ✅ |
| oregon | 118 | 118 | ✅ |
| pennsylvania | 148 | 148 | ✅ |
| prince-edward-island | 10 | 10 | ✅ |
| quebec | 63 | 63 | ✅ |
| rhode-island | 23 | 23 | ✅ |
| saskatchewan | 14 | 14 | ✅ |
| south-carolina | 34 | 34 | ✅ |
| south-dakota | 11 | 11 | ✅ |
| tennessee | 52 | 52 | ✅ |
| texas | 351 | 351 | ✅ |
| utah | 46 | 46 | ✅ |
| vermont | 12 | 12 | ✅ |
| virginia | 137 | 137 | ✅ |
| washington | 121 | 121 | ✅ |
| washington-dc | 6 | 6 | ✅ |
| west-virginia | 28 | 28 | ✅ |
| wisconsin | 85 | 85 | ✅ |
| wyoming | 10 | 10 | ✅ |
| **TOTAL** | **5,219** | **5,219** | ✅ |

61/61 regions matched. 0 mismatches. Both totals = 5,219 as required.

---

## PART 2 — Name diff, 11 touched regions

For each region: names present in BEFORE but not AFTER ("gone"), and names present in AFTER but not BEFORE ("new"). Region record counts were unchanged in every case (confirming suppress-plus-add pairs, not net adds/drops).

| Region | Gone in AFTER | New in AFTER | Matches expected? |
|---|---|---|:---:|
| virginia | Capital MMA & Elite Fitness (x2) | Capital MMA & Elite Fitness Fairfax; Capital MMA & Elite Fitness Sterling | ✅ exact |
| maryland | Southern Maryland Martial Arts & Fitness (x2) | Southern Maryland Martial Arts & Fitness Bryans Road; Southern Maryland Martial Arts & Fitness La Plata | ✅ exact |
| oregon | EchoValor Striking & MMA | EchoValor Striking & MMA Beaverton | ✅ exact |
| kentucky | Core Combat Sports | Core Combat Sports Louisville | ✅ exact |
| florida | Carlson Gracie Jiu Jitsu | Carlson Gracie Jiu Jitsu Gainesville | ✅ exact |
| washington | Connection Rio Jiu-Jitsu Academy; Logic Jiu Jitsu | Connection Rio Jiu-Jitsu Academy College Place; Logic Jiu Jitsu Spanaway | ✅ exact |
| wisconsin | Evolution Jiu Jitsu | Evolution Jiu Jitsu Burlington | ✅ exact |
| arkansas | Impact Martial Arts | Impact Martial Arts Harrison | ✅ exact |
| arizona | Infinite Jiu-Jitsu | Infinite Jiu-Jitsu Phoenix | ✅ exact |
| oklahoma | Integrity Martial Arts | Integrity Martial Arts Moore | ✅ exact |
| pennsylvania | Zombie Brazilian Jiu-Jitsu and MMA | Zombie Brazilian Jiu-Jitsu and MMA Allentown | ✅ exact |

Total: 14 renames observed (11 single + 3 double-instance regions: virginia x2, maryland x2, washington x2-different-names), matching the "14 records renamed" spec exactly. No unexpected names appeared or disappeared in any of the 11 regions — diff sets contained only the rows above.

### Survival checks (names that must remain unchanged / unaffected)

| Check | Result |
|---|:---:|
| maryland AFTER still contains bare `Capital MMA & Elite Fitness` (Takoma Park) | ✅ present |
| washington AFTER still contains bare `EchoValor Striking & MMA` (Centralia) | ✅ present |
| washington AFTER still absent `Northwest Fighting Arts` (already suppressed) | ✅ confirmed absent |
| arizona AFTER still contains bare `Carlson Gracie Jiu Jitsu` (Yuma) | ✅ present |
| oregon AFTER still contains bare `Connection Rio Jiu-Jitsu Academy` (Bend) | ✅ present |
| oregon AFTER still contains `Northwest Fighting Arts` (Portland) | ✅ present |
| california AFTER still contains bare `Infinite Jiu-Jitsu` (Rocklin) | ✅ present |
| california AFTER still contains bare `Logic Jiu Jitsu` (Sacramento) | ✅ present |
| illinois AFTER still contains bare `Core Combat Sports` (Rockford) | ✅ present |
| illinois AFTER still contains `Midwest Training Center` (Schaumburg) | ✅ present |
| alaska AFTER still contains bare `Evolution Jiu Jitsu` (Juneau) | ✅ present |
| nova-scotia AFTER still contains bare `Integrity Martial Arts` (Sydney) | ✅ present |
| texas AFTER still contains bare `Zombie Brazilian Jiu-Jitsu and MMA` (Abilene) | ✅ present |
| texas AFTER still contains `Red River BJJ` (Wichita Falls) | ✅ present |

All 14 survival checks passed — every record that was supposed to remain untouched (because only the sibling copy elsewhere was renamed) is intact under its original bare name.

---

## PART 3 — Address spot checks on AFTER (theme LL)

**1. `bjj-schools-arizona` — Infinite Jiu-Jitsu Phoenix**
Rendered block:
```
<h3>Infinite Jiu-Jitsu Phoenix</h3>
<a class="tjjm-gym-map" href="https://maps.google.com/?q=4220+W+Opportunity+Way+Ste+103,+Phoenix,+AZ">4220 W Opportunity Way Ste 103</a>
```
Result: ✅ Address shows correctly as **4220 W Opportunity Way Ste 103**, confirming the address is now coming from the record itself (the name-keyed override has been removed and the record's own address migrated successfully).

**2. `bjj-schools-california` — Infinite Jiu-Jitsu (Rocklin)**
Rendered block:
```
<h3>Infinite Jiu-Jitsu</h3>
<a class="tjjm-gym-map" href="https://maps.google.com/?q=6508+Lonetree+Blvd+%23107,+Rocklin,+CA">6508 Lonetree Blvd #107</a>
```
Result: ✅ Address shows correctly as **6508 Lonetree Blvd #107**, and does NOT show the Phoenix address. Confirms the two "Infinite Jiu-Jitsu" records (Rocklin unrenamed vs. Phoenix renamed) have fully independent, correct addresses — no cross-contamination.

**3. `bjj-schools-maryland` — the two Southern Maryland ... records**
Rendered blocks:
```
<h3>Southern Maryland Martial Arts & Fitness Bryans Road</h3>
<a class="tjjm-gym-map" href="https://maps.google.com/?q=3065+Marshall+Hall+Rd,+Bryans+Road,+MD">3065 Marshall Hall Rd</a>

<h3>Southern Maryland Martial Arts & Fitness La Plata</h3>
<a class="tjjm-gym-map" href="https://maps.google.com/?q=140+Drury+Dr,+La+Plata,+MD">140 Drury Dr</a>
```
Result: ✅ Bryans Road shows **3065 Marshall Hall Rd**; La Plata shows **140 Drury Dr**. Both distinct addresses confirmed correct.

---

## Conclusion

PASS across all three parts. All 61 region counts are identical between the BEFORE and AFTER themes, both grand totals equal 5,219, all 14 expected renames appeared with no extras or omissions, all "must survive unchanged" records remain intact under their original names, and all three address migrations verified correctly with no cross-contamination between same-named records in different regions.
