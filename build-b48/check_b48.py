#!/usr/bin/env python3
"""Batch 48 gates: C3 (one name, one file, once), C5 (no | or ~ in names),
record uniqueness across the 45 data snippets, and BYTES (<24576)."""
import re, sys, csv, json, glob, os, hashlib, collections

BASE = "/sessions/youthful-gracious-mccarthy/mnt/TJJM Projects"
BUILD = os.path.join(BASE, "build-b48")
DATA = os.path.join(BASE, "scratch/raw-datafiles")
CEIL = 24576

FILES = ["tjjm-gym-websites.liquid"] + [f"tjjm-gym-websites-{i}.liquid" for i in range(2, 7)]
COMMENT = re.compile(r"\{%-?\s*comment\s*-?%\}.*?\{%-?\s*endcomment\s*-?%\}", re.S)
ROW = re.compile(r"~([^~|]*)\|([^~]*)~")


def parse(path):
    s = open(path, encoding="utf-8").read()
    return [(m.group(1), m.group(2)) for m in ROW.finditer(COMMENT.sub("", s))]


def gate_c3(where, label):
    index = collections.defaultdict(list)
    total = 0
    print(f"\n=== {label} ===")
    for f in FILES:
        p = os.path.join(where, f)
        rows = parse(p)
        total += len(rows)
        b = os.path.getsize(p)
        m = hashlib.md5(open(p, "rb").read()).hexdigest()
        flag = "OVER-CEILING!" if b > CEIL else f"headroom {CEIL-b}"
        print(f"  {f:32s} {b:6d} B  {m}  rows={len(rows):4d}  {flag}")
        for n, v in rows:
            index[n].append(f)
    dupes = {n: fs for n, fs in index.items() if len(fs) > 1}
    print(f"  TOTAL rows: {total}   DISTINCT names: {len(index)}   equal={total==len(index)}")
    print(f"  C3 names appearing in >1 file OR >1 time: {len(dupes)}")
    for n, fs in sorted(dupes.items()):
        print("     DUP:", repr(n), fs)
    return index, total, len(index), len(dupes) == 0


# ---------- load records from the 45 data snippets ----------
def load_records():
    recs = []
    paths = [os.path.join(DATA, "tjjm-gyms-data.liquid")] + [
        os.path.join(DATA, f"tjjm-gyms-data-{i}.liquid") for i in range(2, 46)
    ]
    for p in paths:
        if not os.path.exists(p):
            print("MISSING DATA FILE:", p); sys.exit(1)
        s = open(p, encoding="utf-8").read()
        for chunk in s.split('{"n":"')[1:]:
            cut = chunk.find("}")
            if cut < 0:
                continue
            try:
                recs.append(json.loads('{"n":"' + chunk[: cut + 1]))
            except Exception:
                pass
    return recs


def main():
    # ---- input ----
    rows = list(csv.DictReader(open(os.path.join(BUILD, "apply-b48.tsv"), encoding="utf-8"), delimiter="\t"))
    print(f"input rows: {len(rows)}")

    # ---- Gate C5 ----
    bad = [r["name"] for r in rows if "|" in r["name"] or "~" in r["name"]]
    print(f"GATE C5 (no '|' or '~' in name): {'PASS' if not bad else 'FAIL ' + repr(bad)}")

    # ---- pre-edit C3 ----
    index, total, distinct, ok = gate_c3(os.path.join(BUILD, "orig"), "PRE-EDIT")

    # ---- record uniqueness ----
    recs = load_records()
    byname = collections.Counter(r.get("n", "") for r in recs)
    print(f"\nrecords parsed: {len(recs)}  distinct record names: {len(byname)}")
    print("\n=== RECORD MATCH per input row ===")
    problems = []
    for r in rows:
        c = byname.get(r["name"], 0)
        loc = index.get(r["name"], [])
        if c != 1:
            problems.append((r["name"], c, loc))
        print(f"  recs={c}  overrides={loc if loc else '-'}  {r['action']:7s} {r['name']!r}")
    print(f"\nrows NOT matching exactly one record: {len(problems)}")
    for n, c, loc in problems:
        print("   PROBLEM:", repr(n), "records=", c, "overridefiles=", loc)

    # ---- plan ----
    plan_edit, plan_append = [], []
    for r in rows:
        if r["name"] in [p[0] for p in problems]:
            continue
        newv = r["new_url"].strip() if r["action"] == "REPOINT" else ""
        if r["name"] in index:
            plan_edit.append((r["name"], index[r["name"]][0], newv))
        else:
            plan_append.append((r["name"], newv))
    print(f"\nPLAN: in-place edits={len(plan_edit)}  appends to file 6={len(plan_append)}")
    for n, f, v in plan_edit:
        print(f"   EDIT  {f}  {n!r} -> {v!r}")
    for n, v in plan_append:
        print(f"   APPEND file6  {n!r} -> {v!r}")

    json.dump(
        {"edits": plan_edit, "appends": plan_append, "problems": [(n, c, l) for n, c, l in problems]},
        open(os.path.join(BUILD, "plan.json"), "w"), indent=1,
    )


if __name__ == "__main__":
    main()
