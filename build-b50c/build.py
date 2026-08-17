#!/usr/bin/env python3
"""batch 50c - fix the Murdoc's blanking row: straight apostrophe (U+0027) -> curly (U+2019).

The row has never matched the record, so the link rendered live and resolved to a
GoDaddy domain-parking lander. The name is taken BYTE FOR BYTE from the record.
"""
import glob, json, os, difflib

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(BASE)
DATA = os.path.join(ROOT, "scratch", "raw-datafiles")
ORIG = os.path.join(BASE, "orig", "tjjm-gym-websites-6.liquid")
OUT  = os.path.join(BASE, "tjjm-gym-websites-6.liquid")

# ---- 1. take the name from the record, byte for byte -------------------------
names = []
for fn in sorted(glob.glob(os.path.join(DATA, "*.liquid"))):
    raw = open(fn, encoding="utf-8").read()
    for chunk in raw.split('{"n":"')[1:]:
        end = chunk.find("}")
        if end == -1:
            continue
        try:
            names.append(json.loads('{"n":"' + chunk[:end + 1])["n"])
        except Exception:
            pass

hits = sorted({n for n in names if "Murdoc" in n})
assert len(hits) == 1, f"expected exactly 1 matching record, got {len(hits)}: {hits}"
NAME = hits[0]
assert "’" in NAME, "record name is not the curly-apostrophe form"
print("record name :", repr(NAME))
print("record bytes:", NAME.encode("utf-8"))

OLD_ROW = "~" + NAME.replace("’", "'") + "|~"
NEW_ROW = "~" + NAME + "|~"

# ---- 2. edit ------------------------------------------------------------------
src = open(ORIG, encoding="utf-8").read()
before = src.encode("utf-8")

assert src.count(OLD_ROW) == 1, f"old row occurs {src.count(OLD_ROW)}x, expected 1"
assert src.count(NEW_ROW) == 0, f"new row already present {src.count(NEW_ROW)}x"

dst = src.replace(OLD_ROW, NEW_ROW)

assert dst.count(NEW_ROW) == 1, f"new row occurs {dst.count(NEW_ROW)}x, expected 1"
assert OLD_ROW not in dst, "old row still present"

after = dst.encode("utf-8")
delta = len(after) - len(before)
expected = len("’".encode("utf-8")) - len("'".encode("utf-8"))   # 3 - 1 = 2
assert delta == expected, f"byte delta {delta}, expected {expected}"
assert len(dst.splitlines()) == len(src.splitlines()), "line count changed"
assert dst.endswith("\n") == src.endswith("\n"), "trailing newline changed"

with open(OUT, "w", encoding="utf-8", newline="") as fh:
    fh.write(dst)

print(f"bytes: {len(before)} -> {len(after)}  (delta {delta:+d})")

# ---- 3. diff ------------------------------------------------------------------
diff = list(difflib.unified_diff(
    src.splitlines(keepends=True), dst.splitlines(keepends=True),
    fromfile="orig/tjjm-gym-websites-6.liquid",
    tofile="tjjm-gym-websites-6.liquid", n=2))
changed = [l for l in diff if (l.startswith(("+", "-")) and not l.startswith(("+++", "---")))]
assert len(changed) == 2, f"diff touches {len(changed)} lines, expected 2 (1 - / 1 +)"
open(os.path.join(BASE, "change.diff"), "w", encoding="utf-8").write("".join(diff))
print("".join(diff))
print("OK")
