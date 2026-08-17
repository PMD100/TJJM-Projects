#!/usr/bin/env python3
"""Batch 49 builder: 3 in-place edits in file 3, 42 appends to file 7."""
import os, json, hashlib
from collections import Counter

ROOT = "/sessions/youthful-gracious-mccarthy/mnt/TJJM Projects"
B = os.path.join(ROOT, "build-b49b")
ORIG, BUILT = os.path.join(B, "orig"), os.path.join(B, "built")
CEIL = 24576

plan = json.load(open(os.path.join(B, "plan.json"), encoding="utf-8"))["plan"]
edits = [p for p in plan if p["mode"] == "EDIT"]
apps = [p for p in plan if p["mode"] == "APPEND"]
assert len(plan) == 45 and len(apps) == 42 and len(edits) == 3, (len(plan), len(apps), len(edits))

touched = {}

# ---------------- in-place edits ----------------
for fn in sorted({p["file"] for p in edits}):
    src = open(os.path.join(ORIG, fn), encoding="utf-8").read()
    assert "\r" not in src, "CR in source"
    lines = src.split("\n")
    for p in [x for x in edits if x["file"] == fn]:
        old_pref = "~" + p["name"] + "|"
        hits = [i for i, l in enumerate(lines) if l.startswith(old_pref) and l.endswith("~")]
        assert len(hits) == 1, f"{p['name']!r} matched {len(hits)} lines in {fn}"
        i = hits[0]
        new = "~" + p["name"] + "|" + p["url"] + "~"
        print(f"  {fn}: {lines[i]}  ->  {new}")
        lines[i] = new
    touched[fn] = "\n".join(lines)

# ---------------- file 7 ----------------
F7 = "tjjm-gym-websites-7.liquid"
src7 = open(os.path.join(ORIG, F7), encoding="utf-8").read()
assert "\r" not in src7
assert src7.endswith("{%- endcomment -%}\n"), repr(src7[-40:])

rc = Counter(p["reason"].split(" - ")[0] for p in apps)
order = ["AGGREGATOR", "DEAD", "WRONG_BUSINESS", "WRONG_CITY", "STRIKING_ONLY", "REPOINT", "HIJACK", "PARKED"]
assert set(rc) <= set(order), set(rc) - set(order)
counts = ", ".join(f"{rc[k]} {k}" for k in order if rc[k])

comment = f"""{{%- comment -%}}
  17 Aug 2026 - BATCH 49. Identity pass, the closing batch of that pass. 45 verdicts in all;
  the 42 rows added below are {', '.join(counts.split(', ')[:4])},
  {', '.join(counts.split(', ')[4:])}. Every verdict was confirmed by
  loading the page in a REAL CHROME BROWSER, not by the fetch tool.

  THIS IS FILE 7'S FIRST CONTENT. The file was created earlier today as headroom only,
  wired into BOTH rendering surfaces - sections/tjjm-state-directory.liquid (the 61 region
  pages) and sections/tjjm-gym-directory.liquid (the flat "Schools Near You" page) - and
  verified end to end while empty. Files 1, 3, 2, 4 and 6 had 397, 830, 1,269, 1,632 and
  4,753 bytes of slack left against the 24,576-byte rewrite ceiling, so nothing was
  appended to them.

  Added here: 42 new rows. Each name was checked against all seven override files with the
  comment blocks stripped and appeared in NONE of them, so gate C3 is clean and they are
  added here rather than edited elsewhere. The other 3 of the 45 already had rows and were
  blanked in place in tjjm-gym-websites-3.liquid: The Hidden Lotus, Team Jucão Elizabeth
  Brazilian Jiu Jitsu BJJ and Team Nogueira.

  One name arrived from the worksheet without its accent, spelled Team Jucao Elizabeth. The
  record spells it Team Jucão Elizabeth, with an o-tilde, and the record's spelling is what
  was written - an override row only matches on an exact name.

  OWNER'S POLICY, applied throughout: a school's own Facebook or Instagram page IS an
  acceptable link and was kept. AGGREGATOR here means booking platforms (Mindbody, Gymdesk,
  Calendly, Zoho Bookings), Google business.site pages, and association or brand homepages
  standing in for a location page.

  Identity pass complete: 2,170 of 2,170 links read. Browser round cleared 36 of 56 fetch
  flags (64%). Drift this round included same-host different-path substitutions, so probes
  assert host AND path.

  An empty value blanks the link only - each school keeps its name, city and map link, and
  the change is reversible by deleting the row.
{{%- endcomment -%}}
"""

rows7 = "".join("~" + p["name"] + "|" + p["url"] + "~\n" for p in apps)
touched[F7] = src7 + comment + rows7

# ---------------- write + report ----------------
os.makedirs(BUILT, exist_ok=True)
print("\n=== BUILT ===")
fail = False
for fn, text in sorted(touched.items()):
    data = text.encode("utf-8")
    open(os.path.join(BUILT, fn), "wb").write(data)
    o = len(open(os.path.join(ORIG, fn), "rb").read())
    over = len(data) > CEIL
    fail |= over
    print(f"  {fn:30s} {o:6d} -> {len(data):6d} B  ({len(data)-o:+d})  headroom={CEIL-len(data):6d}  "
          f"md5={hashlib.md5(data).hexdigest()}  {'*** OVER CEILING ***' if over else 'OK'}")
if fail:
    raise SystemExit("BYTES gate FAILED")
print("  GATE BYTES: PASS")
