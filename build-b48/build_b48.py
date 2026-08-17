#!/usr/bin/env python3
"""Batch 48 builder. Reads orig/ (MD5-verified against theme ZZ2), applies the
plan, writes the built files into build-b48/. Nothing is hand-typed except prose."""
import re, os, csv, json, hashlib, collections

BASE = "/sessions/youthful-gracious-mccarthy/mnt/TJJM Projects"
BUILD = os.path.join(BASE, "build-b48")
ORIG = os.path.join(BUILD, "orig")
CEIL = 24576

rows = list(csv.DictReader(open(os.path.join(BUILD, "apply-b48.tsv"), encoding="utf-8"), delimiter="\t"))
plan = json.load(open(os.path.join(BUILD, "plan.json")))
assert not plan["problems"], plan["problems"]
assert len(plan["edits"]) + len(plan["appends"]) == len(rows) == 30

# ---------------- 1. in-place edits ----------------
edited = collections.defaultdict(list)
for name, fname, newv in plan["edits"]:
    p = os.path.join(ORIG, fname)
    s = open(p, encoding="utf-8").read()
    pat = re.compile(r"~" + re.escape(name) + r"\|([^~]*)~")
    hits = pat.findall(s)
    assert len(hits) == 1, (name, fname, hits)
    old = hits[0]
    s2 = pat.sub(lambda m: "~" + name + "|" + newv + "~", s, count=1)
    assert s2 != s or old == newv
    open(os.path.join(BUILD, fname), "w", encoding="utf-8").write(s2)
    edited[fname].append((name, old, newv))
    print(f"EDIT {fname}: {name!r}  {old!r} -> {newv!r}")

# untouched files copied straight through
for f in ["tjjm-gym-websites.liquid"] + [f"tjjm-gym-websites-{i}.liquid" for i in range(2, 7)]:
    if f not in edited and f != "tjjm-gym-websites-6.liquid":
        open(os.path.join(BUILD, f), "w", encoding="utf-8").write(
            open(os.path.join(ORIG, f), encoding="utf-8").read())

# ---------------- 2. reason counts ----------------
reason_of = {r["name"]: r["reason"].split(" - ")[0].strip() for r in rows}
counts = collections.Counter(reason_of[r["name"]] for r in rows)
append_names = [n for n, v in plan["appends"]]
order = ["DEAD", "AGGREGATOR", "STRIKING_ONLY", "WRONG_CITY", "HIJACK", "REPOINT"]
assert set(counts) <= set(order), set(counts) - set(order)
blanks = sum(v for k, v in counts.items() if k != "REPOINT")
tally = ", ".join(f"{counts[k]} {k}" for k in order if counts.get(k))

elsewhere = "; ".join(
    f"{n} ({reason_of[n]}) in {f.replace('tjjm-gym-websites', 'file').replace('.liquid','').replace('file-','file ').replace('file','file 1') if f=='tjjm-gym-websites.liquid' else f.replace('tjjm-gym-websites-','file ').replace('.liquid','')}"
    for n, f, v in plan["edits"])

COMMENT = f"""{{%- comment -%}}
  16 Aug 2026 - BATCH 48. Identity pass, continuing the alphabetical sweep through R and S.

  30 rows in this batch: {tally}.
  {blanks} blanking rows and {counts['REPOINT']} repoints.

  {len(append_names)} of the 30 are added below as new rows. The other {len(plan['edits'])} already had a row in
  another override file and were EDITED IN PLACE there rather than duplicated here, so
  gate C3 still holds - every name appears in exactly one override file, once:
    {chr(10).join('    ' + n + '  ->  ' + f for n, f, v in plan['edits']).strip()}

  BROWSER ROUND USED HOSTNAME AND PATHNAME ASSERTION; DRIFT SUBSTITUTIONS THIS ROUND
  INCLUDED A WIX ERROR PAGE AND A GAMBLING LANDER, SO THE 'SUBSTITUTIONS ARE ALWAYS
  HEALTHY GYMS' ASSUMPTION NO LONGER HOLDS.

  That assumption was the stated basis, in batches 45-47, for treating navigation drift as
  biased toward false CLEAN results only. It is not. A drifted read can now land on a dead
  page or a spam page and produce a false DIRTY verdict just as easily, so a drifted read
  is simply void in both directions and must be discarded, never interpreted.

  The {counts['REPOINT']} repoints are all the same shape: the stored deep link 404s while the site root
  or the moved page is live. Blanking those would have thrown away a working school.

  An empty value blanks the link only - each school keeps its name, city and map link,
  and the change is reversible by deleting the row.
{{%- endcomment -%}}
"""

body = "".join(f"~{n}|{v}~\n" for n, v in plan["appends"])

src6 = open(os.path.join(ORIG, "tjjm-gym-websites-6.liquid"), encoding="utf-8").read()
if not src6.endswith("\n"):
    src6 += "\n"
new6 = src6 + COMMENT + body

p6 = os.path.join(BUILD, "tjjm-gym-websites-6.liquid")
open(p6, "w", encoding="utf-8").write(new6)

# ---------------- 3. BYTES gate ----------------
print()
ok = True
for f in ["tjjm-gym-websites.liquid"] + [f"tjjm-gym-websites-{i}.liquid" for i in range(2, 7)]:
    p = os.path.join(BUILD, f)
    b = os.path.getsize(p)
    m = hashlib.md5(open(p, "rb").read()).hexdigest()
    ob = os.path.getsize(os.path.join(ORIG, f))
    state = "OVER CEILING" if b > CEIL else f"headroom {CEIL-b}"
    if b > CEIL:
        ok = False
    print(f"{f:32s} {ob:6d} -> {b:6d} B  ({b-ob:+d})  {m}  {state}")
print("\nGATE BYTES:", "PASS" if ok else "*** FAIL ***")
