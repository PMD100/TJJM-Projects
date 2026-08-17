#!/usr/bin/env python3
"""Batch 49 pre-edit gates: C3 (name in exactly one override file, once),
C11 (each input name matches exactly one published record), C5 (no | or ~ in names)."""
import os, re, json, hashlib, csv, sys, unicodedata
from collections import defaultdict, Counter

ROOT = "/sessions/youthful-gracious-mccarthy/mnt/TJJM Projects"
ORIG = os.path.join(ROOT, "build-b49b", "orig")
DATA = os.path.join(ROOT, "scratch", "raw-datafiles")
TSV  = os.path.join(ROOT, "scratch", "identity", "apply-b49.tsv")

OVR_FILES = ["tjjm-gym-websites.liquid"] + [f"tjjm-gym-websites-{i}.liquid" for i in range(2, 8)]

COMMENT_RE = re.compile(r"\{%-?\s*comment\s*-?%\}.*?\{%-?\s*endcomment\s*-?%\}", re.S)
ROW_RE = re.compile(r"^~(.*)\|(.*)~$")


def strip_comments(text):
    return COMMENT_RE.sub("", text)


def parse_override(path):
    """Return list of (lineno, name, url) for the file."""
    with open(path, encoding="utf-8") as fh:
        raw = fh.read()
    body = strip_comments(raw)
    rows = []
    for i, line in enumerate(body.split("\n"), 1):
        s = line.strip()
        if not s:
            continue
        m = ROW_RE.match(s)
        if not m:
            print(f"  !! UNPARSED line in {os.path.basename(path)}: {s!r}")
            continue
        rows.append((i, m.group(1), m.group(2)))
    return rows


def parse_records(path):
    with open(path, encoding="utf-8") as fh:
        raw = fh.read()
    out = []
    for chunk in raw.split('{"n":"')[1:]:
        end = chunk.find("}")
        if end == -1:
            raise ValueError(f"unterminated record in {path}")
        try:
            out.append(json.loads('{"n":"' + chunk[: end + 1]))
        except Exception as e:
            raise ValueError(f"bad record in {path}: {chunk[:end+1][:120]!r} -> {e}")
    return out


def main():
    # ---------- override corpus ----------
    per_file = {}
    print("=== PRE-EDIT: override files ===")
    total_rows = 0
    for fn in OVR_FILES:
        p = os.path.join(ORIG, fn)
        data = open(p, "rb").read()
        rows = parse_override(p)
        per_file[fn] = rows
        total_rows += len(rows)
        print(f"  {fn:30s} {len(data):6d} B  md5={hashlib.md5(data).hexdigest()}  rows={len(rows):5d}  headroom={24576-len(data)}")
    print(f"  TOTAL rows: {total_rows}")

    name_to_files = defaultdict(list)
    for fn, rows in per_file.items():
        for ln, name, url in rows:
            name_to_files[name].append((fn, ln))
    print(f"  DISTINCT names: {len(name_to_files)}")

    # ---------- gate C3 ----------
    c3_bad = {n: v for n, v in name_to_files.items() if len(v) > 1}
    print("\n=== GATE C3 (name in exactly one file, once) ===")
    if c3_bad:
        print(f"  FAIL: {len(c3_bad)} names duplicated")
        for n, v in sorted(c3_bad.items()):
            print(f"    {n!r} -> {v}")
    else:
        print("  PASS: 0 names appear in more than one file / more than once")

    # ---------- gate C5 on existing corpus ----------
    bad5 = [n for n in name_to_files if "|" in n or "~" in n]
    print(f"  C5 on existing corpus: {'PASS' if not bad5 else 'FAIL '+repr(bad5)}")

    # ---------- record corpus ----------
    print("\n=== RECORD CORPUS ===")
    recs = []
    files = ["tjjm-gyms-data.liquid"] + [f"tjjm-gyms-data-{i}.liquid" for i in range(2, 46)]
    for fn in files:
        rs = parse_records(os.path.join(DATA, fn))
        for r in rs:
            r["_file"] = fn
        recs.extend(rs)
    print(f"  records parsed: {len(recs)}")
    by_name = defaultdict(list)
    for r in recs:
        by_name[r["n"]].append(r)
    dupes = {n: v for n, v in by_name.items() if len(v) > 1}
    print(f"  distinct names: {len(by_name)}   duplicated names: {len(dupes)}")
    for n in sorted(dupes):
        print(f"    DUP x{len(dupes[n])}: {n!r}  files={[r['_file'] for r in dupes[n]]}  s={[r.get('s') for r in dupes[n]]}")

    # ---------- input ----------
    print("\n=== INPUT apply-b49.tsv ===")
    with open(TSV, encoding="utf-8-sig", newline="") as fh:
        rdr = csv.DictReader(fh, delimiter="\t")
        inp = [{k: (v or "").strip() for k, v in row.items()} for row in rdr]
    print(f"  rows: {len(inp)}")
    print(f"  BLANK={sum(1 for r in inp if r['action']=='BLANK')}  REPOINT={sum(1 for r in inp if r['action']=='REPOINT')}")
    rc = Counter(r["reason"].split(" - ")[0] for r in inp)
    for k, v in sorted(rc.items(), key=lambda x: -x[1]):
        print(f"    {k:18s} {v}")

    # ---------- gate C5 on input ----------
    bad5i = [r["name"] for r in inp if "|" in r["name"] or "~" in r["name"]]
    print(f"\n=== GATE C5 (input names) === {'PASS' if not bad5i else 'FAIL '+repr(bad5i)}")

    # ---------- gate C11 ----------
    print("\n=== GATE C11 (each input name -> exactly one record) ===")

    def norm(s):
        s = unicodedata.normalize("NFKD", s)
        s = "".join(c for c in s if not unicodedata.combining(c))
        s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
        s = s.replace("–", "-").replace("—", "-")
        return re.sub(r"\s+", " ", s).strip().lower()

    norm_index = defaultdict(list)
    for r in recs:
        norm_index[norm(r["n"])].append(r)

    results = []
    for r in inp:
        nm = r["name"]
        exact = by_name.get(nm, [])
        if len(exact) == 1:
            results.append((r, "EXACT", exact[0], nm))
        elif len(exact) > 1:
            results.append((r, "MULTI-EXACT", exact, nm))
        else:
            cand = norm_index.get(norm(nm), [])
            if len(cand) == 1:
                results.append((r, "FUZZY", cand[0], cand[0]["n"]))
            elif len(cand) > 1:
                results.append((r, "MULTI-FUZZY", cand, nm))
            else:
                results.append((r, "NONE", None, nm))

    ok, problems, corrections = [], [], []
    for r, status, rec, resolved in results:
        if status in ("EXACT", "FUZZY"):
            regmatch = rec.get("s") == r["region"]
            if status == "FUZZY":
                corrections.append((r["name"], resolved, rec["_file"]))
            if not regmatch:
                problems.append((r["name"], f"REGION MISMATCH: input={r['region']} record s={rec.get('s')} ({rec['_file']})"))
            ok.append((r, rec, resolved))
        else:
            n = len(rec) if isinstance(rec, list) else 0
            det = f"{status} ({n} records)"
            if isinstance(rec, list):
                det += " " + str([(x["_file"], x.get("s"), x.get("c")) for x in rec])
            problems.append((r["name"], det))

    print(f"  resolved to exactly one record: {len(ok)} / {len(inp)}")
    if corrections:
        print("\n  --- NAME SPELLING CORRECTED to record's exact text ---")
        for a, b, f in corrections:
            print(f"    input   : {a!r}")
            print(f"    record  : {b!r}   ({f})")
    if problems:
        print("\n  --- PROBLEMS (NOT to be written) ---")
        for n, d in problems:
            print(f"    {n!r}: {d}")
    else:
        print("  no zero/multi matches, no region mismatches")

    # ---------- routing plan ----------
    print("\n=== ROUTING PLAN ===")
    plan = []
    for r, rec, resolved in ok:
        target_url = r["new_url"] if r["action"] == "REPOINT" else ""
        loc = name_to_files.get(resolved, [])
        if len(loc) == 1:
            plan.append({"name": resolved, "input_name": r["name"], "action": r["action"],
                         "url": target_url, "mode": "EDIT", "file": loc[0][0],
                         "region": r["region"], "reason": r["reason"]})
        elif len(loc) == 0:
            plan.append({"name": resolved, "input_name": r["name"], "action": r["action"],
                         "url": target_url, "mode": "APPEND", "file": "tjjm-gym-websites-7.liquid",
                         "region": r["region"], "reason": r["reason"]})
        else:
            print(f"  !! {resolved!r} in multiple override files {loc} - C3 violation, skipping")
    edits = [p for p in plan if p["mode"] == "EDIT"]
    apps = [p for p in plan if p["mode"] == "APPEND"]
    print(f"  in-place EDITs: {len(edits)}")
    for f, c in sorted(Counter(p["file"] for p in edits).items()):
        print(f"    {f}: {c}")
        for p in edits:
            if p["file"] == f:
                cur = [(u) for (ln, n, u) in per_file[f] if n == p["name"]]
                print(f"       {p['name']!r}  {cur[0]!r} -> {p['url']!r}  [{p['action']}]")
    print(f"  APPENDs to file 7: {len(apps)}")

    with open(os.path.join(ROOT, "build-b49b", "plan.json"), "w", encoding="utf-8") as fh:
        json.dump({"plan": plan, "problems": problems, "corrections": corrections}, fh, indent=1, ensure_ascii=False)
    print("\n  wrote build-b49b/plan.json")
    print(f"\n  SUMMARY: input {len(inp)}, writable {len(plan)}, withheld {len(problems)}")


main()
