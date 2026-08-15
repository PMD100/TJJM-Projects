# -*- coding: utf-8 -*-
import json, re, unicodedata

CUTS = {
 "Portland CTC","Eugene CTC","Müv Fitness","Ballistic Box","Next Level Barbell",
 "Taft Athletic Club","Victory Gym","Budo Fights COM","Martial Masters Academy",
 "Rogue Valley Martial Arts","Team Quest","Oregon’s Elite Training Academy",
 "MMA Hiit Fitness","Empire Boxing and Fitness","Choi's Taekwondo Academy",
 "Spartan Boxing Club","10th Planet Newport","Portland Jiu Jitsu",
 "Ashland Jiu-jitsu Academy",
}

# name -> replacement name
NAME_FIX = {
 "Courthouse Fit Impact JJ South River Lancaster Salem OR": "Impact Jiu Jitsu Salem (Lancaster)",
 "Men’s JIUJITSU School, Astoria Oregon": "Men's JIUJITSU School",
 "RISE Mixed Martial Arts – Eugene": "RISE Mixed Martial Arts - Eugene",
 "Impact Jiu Jitsu Mcminnville": "Impact Jiu Jitsu McMinnville",
}
# name -> replacement website
URL_FIX = {
 "Gracie Barra Sw Portland": "https://graciebarra.com/sw-portland-or/",
 "Mountain Warrior Academy Of Martial Arts (Impact JJ)": "https://www.mwama.com/",
}
# name -> replacement address
ADDR_FIX = {
 "Gracie Barra Sw Portland": "9975 SW Frewing St Suite 120",
 "Impact Jiu Jitsu Mcminnville": "1290 NE HWY 99W",
}

def fix_name(n):
    n = n.strip()
    n = n.replace("’", "'").replace("‘", "'")
    n = n.replace("“", '"').replace("”", '"')
    n = n.replace("–", "-").replace("—", "-")
    n = n.replace(" ", " ")
    n = re.sub(r"\s+", " ", n)
    return n

def fix_city(c):
    c = re.sub(r"\s+", " ", c.strip())
    if c == c.lower():           # only touch all-lowercase arrivals
        c = c.title()
    return c

def fix_url(u):
    u = (u or "").strip()
    if not u:
        return ""
    u = u.split("?")[0]                      # strip query strings
    u = u.replace("%20", "").strip()
    if not re.match(r"^https?://", u, re.I):
        u = "http://" + u
    m = re.match(r"^(https?://)([^/]+)(.*)$", u, re.I)
    if m:
        u = m.group(1).lower() + m.group(2).lower() + m.group(3)
    return u

rows, skipped = [], []
for line in open("oregon-136-matmade.tsv", encoding="utf-8").read().split("\n"):
    if not line.strip():
        continue
    f = (line.split("\t") + [""]*10)[:10]
    raw_name = f[1].strip()
    if raw_name in CUTS:
        skipped.append(raw_name); continue
    name = NAME_FIX.get(raw_name, fix_name(raw_name))
    name = fix_name(name)
    city = fix_city(f[2])
    addr = ADDR_FIX.get(raw_name, f[4].strip())
    web  = URL_FIX.get(raw_name, fix_url(f[5]))
    rows.append({"n": name, "c": city, "s": "OR", "w": web, "a": addr})

# integrity gates
assert len(skipped) == 19, ("cut count", len(skipped), sorted(set(CUTS)-set(skipped)))
bad = [r for r in rows if "|" in r["n"] or '"' in r["n"] or "|" in r["c"]]
assert not bad, bad
nonascii = [r["n"] for r in rows if any(ord(ch) > 127 for ch in r["n"])]
dupes = [n for n in {r["n"] for r in rows} if [r["n"] for r in rows].count(n) > 1]

body = "[\n" + ",\n".join(
    json.dumps(r, ensure_ascii=False, separators=(",", ":")) for r in rows
) + "\n]\n"
open("tjjm-gyms-data-35.liquid", "w", encoding="utf-8").write(body)

print("kept:", len(rows), "cut:", len(skipped))
print("bytes:", len(body.encode()))
print("non-ascii names:", nonascii)
print("dupe names:", dupes)
print("cities:", len({r["c"] for r in rows}))
print("blank web:", sum(1 for r in rows if not r["w"]), "blank addr:", sum(1 for r in rows if not r["a"]))
print("---- first 2 ----"); print("\n".join(body.split("\n")[:3]))
