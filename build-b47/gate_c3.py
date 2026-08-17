import re, sys, collections, os

FILES = ["tjjm-gym-websites.liquid"] + [f"tjjm-gym-websites-{i}.liquid" for i in range(2,7)]
COMMENT = re.compile(r"\{%-?\s*comment\s*-?%\}.*?\{%-?\s*endcomment\s*-?%\}", re.S)
ROW = re.compile(r"~([^~|]*)\|([^~]*)~")

def parse(path):
    s = open(path, encoding="utf-8").read()
    stripped = COMMENT.sub("", s)
    return [(m.group(1), m.group(2)) for m in ROW.finditer(stripped)]

names = [l.rstrip("\n") for l in open("names.txt", encoding="utf-8") if l.strip("\n")]
assert len(names) == 16, len(names)

index = collections.defaultdict(list)
total = 0
for f in FILES:
    rows = parse(f)
    total += len(rows)
    print(f"{f}: {len(rows)} rows")
    for n, v in rows:
        index[n].append(f)

print(f"TOTAL rows: {total}")
print(f"DISTINCT names: {len(index)}")
dupes = {n: fs for n, fs in index.items() if len(fs) > 1}
print(f"NAMES IN >1 FILE: {len(dupes)}")
for n, fs in dupes.items():
    print("   DUP:", repr(n), fs)
# duplicates within same file too
same = {n: fs for n, fs in index.items() if len(fs) != len(set(fs))}
print(f"NAMES DUPLICATED WITHIN A SINGLE FILE: {len(same)}")
for n, fs in same.items():
    print("   INTRA-DUP:", repr(n), fs)

print("\n--- GATE C3: worklist names present anywhere? ---")
present = 0
for n in names:
    if n in index:
        present += 1
        print("  PRESENT:", repr(n), index[n])
print(f"present={present}  absent={16-present}")

print("\n--- exact-byte confirmation for the two awkward names ---")
for n in names:
    if "Murdoc" in n or "Melton" in n:
        print(f"  {n!r}  len={len(n)}  bytes={len(n.encode())}  in_index={n in index}")
        # substring scan across raw files (comments included) for near matches
        for f in FILES:
            raw = open(f, encoding="utf-8").read()
            if n in raw:
                print(f"     literal substring found in {f}")
