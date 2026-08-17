#!/usr/bin/env python3
"""Batch 49 post-build / post-write gates. Pass a directory of the 'current' 7 files."""
import os, re, sys, json, hashlib
from collections import defaultdict

ROOT = "/sessions/youthful-gracious-mccarthy/mnt/TJJM Projects"
B = os.path.join(ROOT, "build-b49b")
ORIG, BUILT = os.path.join(B, "orig"), os.path.join(B, "built")
SRC = sys.argv[1] if len(sys.argv) > 1 else "MERGED"
CEIL = 24576
OVR = ["tjjm-gym-websites.liquid"] + [f"tjjm-gym-websites-{i}.liquid" for i in range(2, 8)]
COMMENT_RE = re.compile(r"\{%-?\s*comment\s*-?%\}.*?\{%-?\s*endcomment\s*-?%\}", re.S)
ROW_RE = re.compile(r"^~(.*)\|(.*)~$")


def pick(fn):
    if SRC != "MERGED":
        return os.path.join(SRC, fn)
    p = os.path.join(BUILT, fn)
    return p if os.path.exists(p) else os.path.join(ORIG, fn)


def rows_of(path):
    body = COMMENT_RE.sub("", open(path, encoding="utf-8").read())
    out = []
    for line in body.split("\n"):
        s = line.strip()
        if not s:
            continue
        m = ROW_RE.match(s)
        assert m, f"UNPARSED in {path}: {s!r}"
        out.append((m.group(1), m.group(2)))
    return out


print(f"=== POST state ({SRC}) ===")
per, total, fail = {}, 0, False
for fn in OVR:
    p = pick(fn)
    data = open(p, "rb").read()
    r = rows_of(p)
    per[fn] = r
    total += len(r)
    over = len(data) > CEIL
    fail |= over
    print(f"  {fn:30s} {len(data):6d} B  md5={hashlib.md5(data).hexdigest()}  rows={len(r):5d}  "
          f"headroom={CEIL-len(data):6d}  {'*** OVER ***' if over else ''}")
print(f"  TOTAL rows: {total}")

loc = defaultdict(list)
for fn, r in per.items():
    for n, u in r:
        loc[n].append(fn)
print(f"  DISTINCT names: {len(loc)}")
print(f"  GATE BYTES: {'FAIL' if fail else 'PASS'}")

dup = {n: v for n, v in loc.items() if len(v) > 1}
print(f"\n=== GATE C3 === {'FAIL' if dup else 'PASS'}")
for n, v in sorted(dup.items()):
    print(f"    {n!r} -> {v}")
print(f"=== rows == distinct names === {'PASS' if total == len(loc) else f'FAIL {total} != {len(loc)}'}")
bad5 = [n for n in loc if "|" in n or "~" in n]
print(f"=== GATE C5 === {'PASS' if not bad5 else 'FAIL '+repr(bad5)}")

# ---- assert all 45 resolve to intended value ----
plan = json.load(open(os.path.join(B, "plan.json"), encoding="utf-8"))["plan"]
flat = {}
for fn, r in per.items():
    for n, u in r:
        flat[n] = (fn, u)
print(f"\n=== 45-ROW READBACK ===")
bad = 0
for p in plan:
    got = flat.get(p["name"])
    want_file, want_url = p["file"], p["url"]
    if got is None:
        print(f"  MISSING {p['name']!r}"); bad += 1
    elif got[1] != want_url or got[0] != want_file:
        print(f"  WRONG   {p['name']!r} in {got[0]} = {got[1]!r}; want {want_file} = {want_url!r}"); bad += 1
print(f"  {len(plan)-bad}/{len(plan)} rows resolve to the intended value in the intended file"
      f"  -> {'PASS' if bad == 0 else 'FAIL'}")
