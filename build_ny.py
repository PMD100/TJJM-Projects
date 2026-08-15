# -*- coding: utf-8 -*-
"""
Build snippets/tjjm-gyms-data-36.liquid  (New York MatMade import)

Written 5 Aug 2026, step 6 of the import sequence.
Every DROP and every FIX below is traceable to a body-read recorded in
ny-step5-verdicts.md. Nothing here rests on a <title>, a meta description
or a directory aggregator.

Gates asserted at the bottom, in code, per RULES-tjjm.md section 5:
names must not contain | or ~ (both are field separators).
"""
import json, re

SRC = "ny-186-matmade.tsv"
OUT = "tjjm-gyms-data-36.liquid"

# ---------------------------------------------------------------- DROPS ----
# A. Duplicates of an existing NY legacy record. Each verified by opening the
#    school's own site and reading the body; see verdicts doc for the quote.
DUP_OF_LEGACY = {
    "Anderson's Martial Arts Academy":                       "Anderson's Martial Arts Academy",
    "Buffalo Brazilian Jiu-Jitsu Academy":                   "Buffalo Brazilian Jiu Jitsu Academy",
    "Clockwork Jiu Jitsu":                                   "Clockwork Brazilian Jiu-Jitsu",
    "Fabio Clemente StudioX BJJ":                            "Studio X",
    "Gentle Art Studio – Lotus Club Brazilian Jiu Jitsu & Wellness Center": "Gentle Art Studio Lotus Club",
    "Kioto Brazilian Jiu-Jitsu":                             "Kioto Brazilian Jiu Jitsu",
    "Long Island MMA & Fitness Center":                      "Long Island MMA",
    "Marcelo Garcia Jiu Jitsu":                              "Marcelo Garcia Academy",
    "Renzo Gracie Bayside":                                  "Renzo Gracie Bayside",
    "Renzo Gracie Fight Academy":                            "Renzo Gracie Brooklyn",
    "Rocian Gracie Jr. Prof Marlon Colorado":                "Marlon Colorado BJJ NYC",
    "Ronin Athletics":                                       "Ronin Athletics",
    "Synthesis Brazilian JiuJitsu | BJJ Rochester NY 14610": "Synthesis Brazilian Jiu-Jitsu",
    "A Force Brazilian Jiu Jitsu Academy":                   "A-Force BJJ Academy",
    "East Side Brazilian Jiu Jitsu / ESBJJ / RENZO GRACIE AFFILIATE": "Renzo Gracie East Side",
    "Gregor Gracie Jiu-Jitsu":                               "Gregor Gracie Academy Brooklyn",
    "Igor Gracie Academy":                                   "Igor Gracie Jiu Jitsu Academy",
    "Seven Tigers Martial Arts Academy":                     "Seven Tigers Martial Arts Academy",
    "The Dojo NYC":                                          "The Dojo NYC",
    "Jungle Gym Martial Arts – New Rochelle":                "Jungle Gym Martial Arts",
    "Kings Combat Williamsburg":                             "Kings Combat",
    # --- found by the containment pass, invisible to BOTH the exact-name and
    #     the domain check because the names differ AND the domains differ ---
    "Brooklyn BJJ":                                          "Brooklyn Brazilian Jiu Jitsu",
    "Kioto Brazilian Jiu Jitsu / NEMMAA":                    "Next Evolution Martial Arts",
    # --- Modern Martial Arts knot: both records are 103 W 73rd St = the legacy
    #     record's flagship. "73th" is a typo of 73rd. ---
    "Modern Martial Arts NYC":                               "Modern Martial Arts NYC",
    "Modern Martial Arts NYC Upper West Side":               "Modern Martial Arts NYC",
    # --- Serra: the live site lists Huntington ONLY. Both no-address stubs and
    #     the Levittown record go; the legacy record survives and is owed a
    #     city+address correction to Huntington. This REVERSES the step-3 read. ---
    "Serra Brazilian Jiu-Jitsu Academy - Huntington":        "Serra BJJ Academy",
    "Serra Brazilian Jiu-Jitsu Academy - Levittown":         "Serra BJJ Academy",
    "Serra BJJ Academy":                                     "Serra BJJ Academy",
}

# B. MatMade-internal duplicate: one business, two domains.
DUP_INTERNAL = {
    "Vamos BJJ & MMA": "Vamos MMA — vamosmma.com lists Holbrook (1708 Church St) and "
                       "Riverhead; 4713 Veterans Hwy appears on neither. Same brand, "
                       "same promo, same phone. MEDIUM confidence, reversible.",
}

# C. No BJJ or submission grappling anywhere on the school's own schedule.
#    A school teaching BJJ alongside karate/Muay Thai/boxing STAYS; only a
#    school with no grappling program at all is out of scope.
NON_BJJ = {
    "Kim's TaeKwonDo":        "TKD only; kids/teens/adult martial arts, no BJJ",
    "Krav Maga Academy":      "Krav Maga, women's self-defence, S&C only",
    "Krav Maga Institute NYC":"Adult Krav Maga, women's self-defence, kids only",
    "Kyokushin Karate NYC":   "kata/kumite karate only",
    "NY San Da":              "kickboxing, Muay Thai/San Da, kung fu only",
    "Fighthouse Systema NYC": "Systema only",
    "Traditional Tribal Fitness": "group fitness bootcamp in McCarren Park, not a martial art",
    "Sitan Gym Li":           "Muay Thai, kids Thai boxing, S&C, fitness kickboxing only",
    "Brooklyn Wing Tsun":     "Wing Tsun kung fu self-defence only",
    "Jiu Jitsu Massage":      "a sports massage practice (Infused Concept Sports Massage), not a school",
    "Victor CTC":             "ctconline.com is Connection Technology Center, an industrial "
                              "vibration-sensor manufacturer in Victor NY. Not a gym at all.",
    "NY Muay-Thai Kick Boxing Association - Judo school":
                              "no first-party site; 32-48 Steinway St is now Kai Leung's Shotojuku, "
                              "a different karate school",
}

# D. Judo / traditional Japanese jujutsu, no Brazilian Jiu-Jitsu.
#    Called out separately because "jujitsu" in a name is not evidence of BJJ.
#    Reversible if the directory's scope is later widened to grappling arts.
JUDO_TJJ_ONLY = {
    "Iaido Kendo Club":                     "kendo, iaido, traditional 'jiu jitsu', karate",
    "Eizan Ryu Jujitsu":                    "traditional Japanese jujitsu + karate",
    "Staten Island Judo & Jujitsu Academy": "Kodokan judo / traditional self-defence jujitsu",
    "Sei Shin Dojo":                        "Goshin jiu jitsu (self-defence) + Pekiti Tirsia Kali",
}

# E. Could not be settled this run. HELD OUT of the import rather than guessed
#    in either direction — a school with no readable body is not evidence of
#    anything. Each needs one body read next run.
HELD_UNCONFIRMED = {
    "Westchester Judo Club":  "site returns an empty body on every path",
    "Pegatessu Fitness":      "site returns an empty body on every path",
    "NY Ultimate Fitzone - Personal Training Bayside NY, MMA Personal Trainer, Muay Thai Gym Classes":
                              "site returns an empty body; name is SEO spam and needs a rewrite too",
    "Tiger Martial Arts":     "site empty; aggregators claim BJJ/Sambo, which is a prior not a result",
    "Nubreed Martial Arts Academy": "site returns an empty body",
    "Blitz Dojo":             "site returns an empty body",
    "USA Karate & BJJ":       "site empty; only an aggregator claims the BJJ program",
    "Ultimate Sambo MMA Academy": "domain expired, listed for sale on GoDaddy",
    "Kai Next Level Mixed Martial Arts & B.J.J. / Fitness":
                              "martialarts4us.com empty on 4 attempts",
    "Red Tiger Jiu Jitsu Ryu":"no first-party site found, Facebook/Instagram only",
    "Gracie Jiu-Jitsu Sayville": "no first-party site; Gracie University network page only",
}

DROPS = {}
for n, why in DUP_OF_LEGACY.items():   DROPS[n] = ("duplicate-of-legacy", why)
for n, why in DUP_INTERNAL.items():    DROPS[n] = ("duplicate-internal", why)
for n, why in NON_BJJ.items():         DROPS[n] = ("not-a-bjj-school", why)
for n, why in JUDO_TJJ_ONLY.items():   DROPS[n] = ("judo-or-tjj-only", why)
for n, why in HELD_UNCONFIRMED.items():DROPS[n] = ("held-unconfirmed", why)

# ----------------------------------------------------------------- FIXES ---
# Renames. Two are BLOCKING: "|" is a field separator and cannot be written.
NAME_FIX = {
    "Sas Jiu Jitsu Syracuse | BJJ Syracuse NY 13206": "Sas Jiu Jitsu Syracuse",   # BLOCKING
    "mma yonkers ny – mma training in yonkers ny":    "Westchester Fight Club",
    "Hidden Fist Mixed Martial Arts Academy 41-25 bell boulevard bayside New York":
                                                      "Hidden Fist Mixed Martial Arts Academy",
    "Bwarriormma.com":                                "Bwarrior MMA",
    "Curtis Tillman’S Mixed Martial Arts Academy":"Curtis Tillman's Mixed Martial Arts Academy",
    "Lotus Jiu jitsu Flushing":                       "Lotus Jiu Jitsu Flushing",
    "Team Demolition MMA":                            "TD Athletics",             # rebranded
    "Diamond Heart":                                  "Team Diamond Heart",
    # the two Bronx records share a name but are two unrelated schools:
    # 1051 Allerton Ave is a Renzo Gracie affiliate; 1621 Crosby Ave trades as
    # "Bronx Jiu-Jitsu" (Vitor Shaolin association). Disambiguated by address below.
}
NAME_FIX_BY_ADDR = {
    ("Bronx Martial Arts Academy", "1621 Crosby Ave"): "Bronx Jiu-Jitsu",
    # COLLIDES WITH A SURVIVING LEGACY RECORD. Legacy keeps `Jungle Gym Martial
    # Arts` /New Rochelle; this is the brand's separate Bronx location. Two
    # records with one name would render twice AND make the New Rochelle
    # website override silently repoint this record too — an override matches
    # on name alone. The brand's own convention is a location suffix
    # ("Jungle Gym Martial Arts – New Rochelle"), so follow it.
    ("Jungle Gym Martial Arts", "1526 Unionport Rd"): "Jungle Gym Martial Arts - Bronx",
}

# Websites replaced with the school's real first-party site, read from its body.
URL_FIX = {
    "Gracie Jiu-Jitsu Victor":        "https://gracievictor.com",
    "Lake Effect Martial Arts":       "https://lakeeffectbjj.com",
    "Gracie Jiu-Jitsu Poughkeepsie":  "https://nationalmartialartsandfitness.com",
    "Gracie Jiu-Jitsu Point Lookout": "https://graciejiujitsuli.com",
    "IJC Martial Arts":               "https://ijcnyc.com",
    "Jkd NYC":                        "https://jkdnyc.com",
    "Krystek School of Judo, BJJ, Self Defense and Fitness": "https://krystekjudo.com",
    "Red Dawn Combat Club- Fresh Meadows": "https://reddawnbjj.com",
    "Buffalo United Martial Arts":    "https://buffalounitedmartialarts.com",
    "Peak Jiu-Jitsu":                 "https://www.peakjj.com",
    "Black Hole Jiu Jitsu":           "https://blackholejj.com",
    "The Grappling Club":             "https://thegrapplingclubnyc.com",
    "Team Demolition MMA":            "https://tdathletics.net",
    "mma yonkers ny – mma training in yonkers ny": "https://westchesterfightclub.com",
    "Modern Martial Arts Tribeca":    "https://www.mmanewyorkcity.com/locations/tribeca",
    "Valor Mixed Martial Arts":       "https://valormmanyc.com",
    "Diamond Heart":                  "https://teamdiamondheart.com",
    "Gracie Barra North Babylon":     "https://gbnorthbabylon.com",
    # no live first-party site exists — better blank than a wrapper (RULES sect 5:
    # an empty override blanks the link; here we simply store nothing)
    "Modern Martial Arts Astoria":    "",
    "Yin Yang Jiu Jitsu":             "",
}

# Addresses replaced with the value on the school's own site.
ADDR_FIX = {
    "Gracie Jiu-Jitsu Victor":             "8050 Victor Mendon Rd Suite 500",
    "Team Demolition MMA":                 "713 Snediker Ave",
    "Red Dawn Combat Club- Fresh Meadows": "186-12 Union Turnpike",
}

# ------------------------------------------------------------ NORMALISERS --
def fix_name(n):
    n = n.strip()
    n = n.replace("’", "'").replace("‘", "'")
    n = n.replace("“", '"').replace("”", '"')
    n = n.replace("–", "-").replace("—", "-")
    n = n.replace(" ", " ")
    return re.sub(r"\s+", " ", n)

BOROUGH = {"Manhattan": "New York", "The Bronx": "Bronx"}
def fix_city(c):
    c = re.sub(r"[_]+", " ", c.strip())
    c = re.sub(r"\s+", " ", c)
    if c.isupper() or c.islower():
        c = c.title()
    return BOROUGH.get(c, c)

def fix_url(u):
    u = (u or "").strip()
    if not u:
        return ""
    u = u.split("?")[0]                       # METHOD CORRECTION: drop query strings
    u = u.replace("%20", "").strip()
    if not re.match(r"^https?://", u, re.I):  # 2 records stored scheme-less
        u = "https://" + u
    m = re.match(r"^(https?://)([^/]+)(.*)$", u, re.I)
    if m:
        u = m.group(1).lower() + m.group(2).lower() + m.group(3)
    return u.rstrip("/") if u.count("/") > 2 and u.endswith("/") else u

# ------------------------------------------------------------------ BUILD --
rows, dropped = [], []
lines = [l for l in open(SRC, encoding="utf-8").read().split("\n")
         if l.strip() and not l.startswith("#")]
hdr = lines[0].split("\t")
for line in lines[1:]:
    f = line.split("\t")
    f += [""] * (len(hdr) - len(f))
    rec = dict(zip(hdr, f))
    raw = rec["name"].strip()

    if raw in DROPS:
        dropped.append((raw, DROPS[raw][0], DROPS[raw][1]))
        continue

    addr = ADDR_FIX.get(raw, rec["address1"].strip())
    name = NAME_FIX_BY_ADDR.get((raw, rec["address1"].strip()))
    if name is None:
        name = NAME_FIX.get(raw, raw)
    name = fix_name(name)
    rows.append({"n": name,
                 "c": fix_city(rec["city"]),
                 "s": "NY",
                 "w": URL_FIX.get(raw, fix_url(rec["websiteURL_raw"])),
                 "a": addr})

# ------------------------------------------------------------------ GATES --
# 1. THE BLOCKING GATE. Run over every record, not just the two known ones.
bad_sep = [r for r in rows if re.search(r"[|~]", r["n"]) or re.search(r"[|~]", r["c"])
                              or re.search(r"[|~]", r["a"])]
assert not bad_sep, f"FIELD SEPARATOR in {len(bad_sep)} record(s): {bad_sep}"

# 2. No stray quotes that would break the JSON blob.
assert not [r for r in rows if '"' in r["n"]], "double quote in a name"

# 3. Every DROP key must have matched exactly one source row — a typo in the
#    DROPS dict would otherwise silently import a record we meant to cut.
dropped_names = [d[0] for d in dropped]
unmatched = sorted(set(DROPS) - set(dropped_names))
assert not unmatched, f"DROP key never matched a source row: {unmatched}"
assert len(dropped_names) == len(set(dropped_names)), "a DROP key matched twice"

# 4. Arithmetic must close.
assert len(rows) + len(dropped) == 186, (len(rows), len(dropped))

# 5. No duplicate names inside the new snippet (the section dedupes by name).
names = [r["n"] for r in rows]
dupes = sorted({n for n in names if names.count(n) > 1})
assert not dupes, f"duplicate name within NY import: {dupes}"

# 6. NO IMPORTED NAME MAY COLLIDE WITH A SURVIVING LEGACY NAME.
#    Two records sharing a name in one region render twice, and every
#    name-keyed mechanism in this theme — tjjm-removed-index suppression,
#    tjjm-gym-websites overrides, tjjm-gym-addresses backfill — matches on
#    name ALONE, so a collision silently applies one record's correction to
#    the other. Caught `Jungle Gym Martial Arts` on 5 Aug 2026.
SUPPRESSED_LEGACY = {
    "Rochester Fitness Martial Arts", "Swan's Martial Arts Academy",
    "Savarese BJJ Academy", "Seven Tigers Martial Arts Academy", "CNY MMA",
    "Brazilian Power Team Westchester", "Elite Fitness & Martial Arts",
    "Middletown BJJ NY", "Newburgh BJJ", "Precision Brazilian Jiu Jitsu",
    "Plattsburgh BJJ", "Watertown BJJ NY",
}
legacy_names = set()
for _l in open("ny-legacy-64-raw.txt", encoding="utf-8"):
    _l = _l.strip()
    if _l and not _l.startswith("#") and len(_l.split("|")) >= 4:
        legacy_names.add(_l.split("|")[1])
surviving_legacy = legacy_names - SUPPRESSED_LEGACY
collide = sorted(set(names) & surviving_legacy)
assert not collide, f"imported name collides with a SURVIVING legacy record: {collide}"
# and a suppressed legacy name must not match an imported one either, or the
# removal filter deletes the new record along with the old one
collide2 = sorted(set(names) & SUPPRESSED_LEGACY)
assert not collide2, f"imported name collides with a SUPPRESSED legacy record: {collide2}"

body = "[\n" + ",\n".join(json.dumps(r, ensure_ascii=False, separators=(",", ":"))
                          for r in rows) + "\n]\n"
open(OUT, "w", encoding="utf-8").write(body)

# ----------------------------------------------------------------- REPORT --
from collections import Counter
reasons = Counter(d[1] for d in dropped)
print(f"source records      : 186")
print(f"kept (importing)    : {len(rows)}")
print(f"dropped             : {len(dropped)}")
for r, n in sorted(reasons.items(), key=lambda x: -x[1]):
    print(f"    {r:22} {n}")
print(f"yield               : x{len(rows)/186:.3f}")
print()
print(f"snippet bytes       : {len(body.encode('utf-8'))}")
print(f"distinct cities     : {len({r['c'] for r in rows})}")
print(f"blank website       : {sum(1 for r in rows if not r['w'])}")
print(f"blank address       : {sum(1 for r in rows if not r['a'])}")
print(f"non-ascii names     : {[r['n'] for r in rows if any(ord(c)>127 for c in r['n'])]}")
print(f"http:// records     : {sum(1 for r in rows if r['w'].startswith('http://'))}")
print(f"https:// records    : {sum(1 for r in rows if r['w'].startswith('https://'))}")
print()
print("ALL GATES PASSED")
