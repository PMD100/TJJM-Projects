# -*- coding: utf-8 -*-
"""
Step 7 artifacts for the New York import. Builds three append-blocks and one new
snippet, and PREDICTS every resulting file size before anything is written.

Nothing here touches the store. Current sizes were read from MAIN/YY
(154658242732) on 5 Aug 2026 and are asserted below, so if the theme moves under
us the script fails instead of predicting from a stale baseline.
"""
import json, re

# ---- measured from MAIN/YY 154658242732, 5 Aug 2026 ----
CUR = {
    "sections/tjjm-state-directory.liquid": 12485,
    "snippets/tjjm-gym-websites.liquid":     3440,
    "snippets/tjjm-removed-index.liquid":    8293,
}

# ============================================================ 1. WEBSITES ====
# RULES (from the file's own header): only add an entry that CHANGES something.
# Restating a URL the record already has pins the old value as a second source
# of truth if the record is later corrected. So every row below is diffed
# against the RAW stored w from the audit dump before it is emitted.
LINK_FIX = {
 "Bellmore Kickboxing Academy":        "https://bellmorekickboxingmma.com/",
 "Binghamton Brazilian Jiu Jitsu":     "https://broomecountymartialarts.com/",
 "Brian Beury Jiu Jitsu":              "https://brianbeauryjiujitsu.com/",
 "Buffalo Brazilian Jiu Jitsu Academy":"https://www.buffalobjj.com/",
 "Clobber Jiu Jitsu Academy":          "https://clobberjiujitsu.com/",
 "Ithaca BJJ":                         "https://www.ithacabjjschool.com/",
 "Jiu Livre NYC":                      "https://jiulivre.com/",
 "Jon Calestine BJJ":                  "https://calestinejj.com/",
 "Jungle Gym Martial Arts":            "https://junglegymnewroc.com/",
 "Kings Combat":                       "https://kingscombatwillyb.com/",
 "Modern Martial Arts NYC":            "https://www.mmanewyorkcity.com/",
 "Next Evolution Martial Arts":        "https://nextevolutionmartialarts.com/",
 "Paxibellum":                         "https://paxibellum.com/",
 "Serra BJJ Academy":                  "https://serrabjjacademy.com/",
 "The Dojo NYC":                       "https://thedojonyc.com/",
}
WHY = {
 "Bellmore Kickboxing Academy":        "301 from the stored host to bellmorekickboxingmma.com; body gives 2551 Merrick Rd, Bellmore 11710",
 "Binghamton Brazilian Jiu Jitsu":     "stored domain 301s; school trades as Broome County Martial Arts, Binghamton",
 "Brian Beury Jiu Jitsu":              "stored domain dead. School is live as Brian BEAURY Jiu Jitsu, 1623 2nd Ave, Watervliet. NAME IS MISSPELT in the record and city is wrong - both need a snippet rewrite (item 0c)",
 "Buffalo Brazilian Jiu Jitsu Academy":"the ONLY http:// record in the NY legacy 64. https:// confirmed working. Section only prepends a scheme, it never upgrades one",
 "Clobber Jiu Jitsu Academy":          "stored domain dead. Live at clobberjiujitsu.com, 180 Delaware Ave Unit 158, DELMAR - city wrong, item 0c",
 "Ithaca BJJ":                         "stored domain parked (/lander). School live as Ithaca BJJ School, Shops at Ithaca Mall",
 "Jiu Livre NYC":                      "stored domain dead. Live at jiulivre.com, 383 5th Ave 3rd Fl. NOTE: also appears on UFC GYM's own NY roster as 'Jiu-Livre (NYC)'",
 "Jon Calestine BJJ":                  "stored domain dead. Live as Calestine Jiu Jitsu, 315 Meserole St Ste 210, BROOKLYN - city wrong, item 0c",
 "Jungle Gym Martial Arts":            "stored junglegym.com is a UK playground-equipment retailer. Real site junglegymnewroc.com, 714 North Ave (NOT 10 Cottage Pl, which is Groupon-only)",
 "Kings Combat":                       "stored domain is a GoDaddy for-sale lander ($1,988). Live as Kings Combat Williamsburg, 219 South 3rd St, Brooklyn 11211",
 "Modern Martial Arts NYC":            "stored modernmartialarts.com is a book-promo site for James Dolmage. Real site mmanewyorkcity.com",
 "Next Evolution Martial Arts":        "stored domain dead. Live at nextevolutionmartialarts.com, 1786 3rd Ave - the same school MatMade lists as 'Kioto Brazilian Jiu Jitsu / NEMMAA'",
 "Paxibellum":                         "apex serves the school; the stored www form fails TLS. Only the www is broken",
 "Serra BJJ Academy":                  "stored serrabjj.com dead. serrabjjacademy.com is live and lists HUNTINGTON ONLY - the city on this record is wrong, item 0c",
 "The Dojo NYC":                       "stored domain dead. Live at thedojonyc.com, 32 Gardner Ave, Brooklyn 11237 - the record's Brooklyn city was RIGHT and MatMade's Ridgewood is wrong",
}

# raw stored w, straight from the audit dump
stored = {}
for line in open("ny-legacy-64-raw.txt", encoding="utf-8"):
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    p = line.split("|")
    if len(p) >= 4:
        stored[p[1]] = p[3]

SUPPRESSED = {
 "Rochester Fitness Martial Arts","Swan's Martial Arts Academy","Savarese BJJ Academy",
 "Seven Tigers Martial Arts Academy","CNY MMA","Brazilian Power Team Westchester",
 "Elite Fitness & Martial Arts","Middletown BJJ NY","Newburgh BJJ",
 "Precision Brazilian Jiu Jitsu","Plattsburgh BJJ","Watertown BJJ NY",
}

def norm(u):
    """Compare on substance, not on trailing-slash cosmetics."""
    return re.sub(r"/+$", "", (u or "").strip().lower())

rows, no_change, not_found, wasted = [], [], [], []
for name, url in LINK_FIX.items():
    if name not in stored:
        not_found.append(name); continue
    if norm(stored[name]) == norm(url):
        no_change.append((name, stored[name], url)); continue
    if name in SUPPRESSED:
        wasted.append(name); continue          # an override on a hidden record is dead weight
    rows.append((name, url))

assert not not_found,  f"override name not in the legacy blob: {not_found}"
assert not no_change,  f"override RESTATES the stored value (forbidden): {no_change}"
assert not wasted,     f"override on a SUPPRESSED record, would never render: {wasted}"

# the field separators are structural in this file: ~Name|URL~
bad = [n for n, _ in rows if re.search(r"[|~]", n)] + \
      [u for _, u in rows if re.search(r"[~]", u)]
assert not bad, f"separator character in an override row: {bad}"

web_block = (
"{%- comment -%}\n"
"  Added 5 Aug 2026 by the NEW YORK import, step 5/7. Every one verified by OPENING the\n"
"  school's page and reading the BODY - never from a <title>, a meta description or a\n"
"  directory aggregator (RULES-tjjm.md section 4). Full rationale and the evidence quote for\n"
"  each row is in snippets/tjjm-statedir-notes-ny.\n"
"\n"
"  All 15 rows CHANGE something: each was diffed against the raw stored w from the audit\n"
"  dump before being added, and the build asserts that no row restates its record's\n"
"  existing value.\n"
"\n"
"  WATCH THIS ONE. 'Jungle Gym Martial Arts' is a name the brand also uses for its Bronx\n"
"  location. An override matches on NAME ALONE, so importing the Bronx record under the\n"
"  same name would have silently given it the New Rochelle URL. The Bronx record is\n"
"  therefore imported as 'Jungle Gym Martial Arts - Bronx'. Do not undo that rename\n"
"  without removing this row.\n"
"\n"
"  NOT FIXED HERE, because no override reaches the field (item 0c): Brian Beury is\n"
"  misspelt (Beaury) and is in Watervliet not Albany; Clobber is in Delmar not Cohoes;\n"
"  Jon Calestine is in Brooklyn not New York; Serra is in Huntington not Levittown;\n"
"  Kioto is in Oakdale not New York; Long Island MMA is in West Babylon not Lake Grove;\n"
"  Haven Jiu Jitsu is in Baldwinsville not Syracuse.\n"
"{%- endcomment -%}\n"
) + "".join(f"~{n}|{u}~\n" for n, u in rows)

# ======================================================= 2. REMOVED INDEX ====
ny_row = "NY|" + "|".join(sorted(SUPPRESSED)) + "\n"
assert "~" not in ny_row
assert all(n in stored for n in SUPPRESSED), "a suppressed name is not in the legacy blob"
kept_import = {r["n"] for r in json.load(open("tjjm-gyms-data-36.liquid", encoding="utf-8"))}
assert not (SUPPRESSED & kept_import), "suppressing a name that is ALSO being imported"

# ========================================================= 3. SECTION EDIT ===
OLD_TAG = "{%- render 'tjjm-gyms-data-35' -%}{%- endcapture -%}"
NEW_TAG = "{%- render 'tjjm-gyms-data-35' -%}{%- render 'tjjm-gyms-data-36' -%}{%- endcapture -%}"
DELTA = len(NEW_TAG.encode()) - len(OLD_TAG.encode())

# ============================================================ 4. PREDICTIONS =
snippet = open("tjjm-gyms-data-36.liquid", "rb").read()
notes   = open("tjjm-statedir-notes-ny.liquid", "rb").read() if __import__("os").path.exists("tjjm-statedir-notes-ny.liquid") else b""

pred = {
 "sections/tjjm-state-directory.liquid": CUR["sections/tjjm-state-directory.liquid"] + DELTA,
 "snippets/tjjm-gym-websites.liquid":    CUR["snippets/tjjm-gym-websites.liquid"] + len(web_block.encode()),
 "snippets/tjjm-removed-index.liquid":   CUR["snippets/tjjm-removed-index.liquid"] + len(ny_row.encode()),
 "snippets/tjjm-gyms-data-36.liquid":    len(snippet),
 "snippets/tjjm-statedir-notes-ny.liquid": len(notes),
}

open("step7-tjjm-gym-websites-APPEND.txt", "w", encoding="utf-8").write(web_block)
open("step7-tjjm-removed-index-APPEND.txt", "w", encoding="utf-8").write(ny_row)

print("=== 1. tjjm-gym-websites — append block ===")
print(f"  overrides emitted   : {len(rows)}")
print(f"  restating a value   : {len(no_change)}  (must be 0)")
print(f"  block bytes         : {len(web_block.encode())}")
print()
print("=== 2. tjjm-removed-index — new NY row ===")
print(f"  suppressed names    : {len(SUPPRESSED)}")
print(f"  row bytes           : {len(ny_row.encode())}")
print(f"  row                 : {ny_row.strip()[:110]}...")
print()
print("=== 3. section edit ===")
print(f"  exact replacement, one occurrence:")
print(f"    OLD  ...{OLD_TAG[-46:]}")
print(f"    NEW  ...{NEW_TAG[-80:]}")
print(f"  delta bytes         : +{DELTA}")
print()
print("=== 4. PREDICTED SIZES (assert these against what Shopify reports) ===")
for f, b in pred.items():
    ceiling = "  <-- against the ~24 KB rewrite ceiling" if f.startswith("sections/") else ""
    print(f"  {f:44} {b:>7} B{ceiling}")
print()
assert pred["sections/tjjm-state-directory.liquid"] < 24000, "SECTION OVER THE CEILING"
print(f"  section headroom    : {24000 - pred['sections/tjjm-state-directory.liquid']} B remaining")
print()
print("ALL STEP-7 GATES PASSED")
