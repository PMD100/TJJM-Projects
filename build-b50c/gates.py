#!/usr/bin/env python3
"""Gates for batch 50c, run against the POST-EDIT override set."""
import glob, json, os, re, collections

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)
GATE = os.path.join(BASE, "gate")
DATA = os.path.join(ROOT, "scratch", "raw-datafiles")

ORDER = ["tjjm-gym-websites.liquid"] + [f"tjjm-gym-websites-{i}.liquid" for i in range(2, 8)]
ROW = re.compile(r"^~([^|~]*)\|([^~]*)~$")     # line-anchored: excludes header-comment examples

rows = []                                       # (file, name, url)
for fn in ORDER:
    path = os.path.join(GATE, fn)
    n = 0
    for line in open(path, encoding="utf-8").read().splitlines():
        m = ROW.match(line.strip())
        if m:
            rows.append((fn, m.group(1), m.group(2)))
            n += 1
    print(f"  {fn:30s} {n:4d} rows")

names = [n for _, n, _ in rows]
print(f"\nTOTAL ROWS    : {len(rows)}")
print(f"DISTINCT NAMES: {len(set(names))}")

dupes = {n: c for n, c in collections.Counter(names).items() if c > 1}
print(f"GATE C3       : {'PASS' if not dupes else 'FAIL ' + repr(dupes)}"
      f"  (rows == distinct names: {len(rows) == len(set(names))})")

# --- the fixed name, taken from the record ------------------------------------
recs = []
for fn in sorted(glob.glob(os.path.join(DATA, "*.liquid"))):
    raw = open(fn, encoding="utf-8").read()
    for chunk in raw.split('{"n":"')[1:]:
        e = chunk.find("}")
        if e != -1:
            try:
                recs.append(json.loads('{"n":"' + chunk[:e + 1])["n"])
            except Exception:
                pass
RECORDS = set(recs)
TARGET = sorted({n for n in RECORDS if "Murdoc" in n})[0]

where = [(f, n) for f, n, _ in rows if n == TARGET]
print(f"\nTARGET        : {TARGET!r}")
print(f"  appears in  : {where}  -> {len(where)} occurrence(s), "
      f"{len({f for f, _ in where})} file(s)")
assert len(where) == 1, "target name must appear exactly once"

straight = TARGET.replace("’", "'")
stray = [(f, n) for f, n, _ in rows if n == straight]
print(f"  straight-apostrophe form remaining: {stray}")
assert not stray, "straight-apostrophe row still present"

# --- ORPHAN CHECK: every override name must match a record --------------------
orphans = sorted({n for n in names if n not in RECORDS})
print(f"\nRECORDS       : {len(RECORDS)} distinct")
print(f"ORPHANS       : {len(orphans)}")
for o in orphans:
    print("   ORPHAN:", repr(o))

# --- BYTES --------------------------------------------------------------------
print("\nBYTES (limit 24576):")
ok = True
for fn in ORDER:
    b = os.path.getsize(os.path.join(GATE, fn))
    flag = "OK" if b < 24576 else "OVER"
    ok &= b < 24576
    print(f"  {fn:30s} {b:6d}  {flag}")

print("\nRESULT:", "ALL GATES PASS" if (not dupes and not orphans and ok) else "GATE FAILURE")
