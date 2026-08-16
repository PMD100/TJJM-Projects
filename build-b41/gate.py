import re, sys, glob, collections
FILES = ["tjjm-gym-websites.liquid"] + ["tjjm-gym-websites-%d.liquid" % i for i in range(2,7)]
COMMENT = re.compile(r"\{%-\s*comment\s*-%\}.*?\{%-\s*endcomment\s*-%\}", re.S)
ROW = re.compile(r"~([^|~]*)\|([^~]*)~")
def rows(path):
    raw = open(path, encoding="utf-8").read()
    stripped = COMMENT.sub("", raw)
    return [(m.group(1), m.group(2)) for m in ROW.finditer(stripped)], raw, stripped

targets = ["10th Planet North Dallas", "Applied MMA Austin", "Baker's MMA & Fitness LLC"]
where = collections.defaultdict(list)
total = 0
for f in FILES:
    rs, raw, stripped = rows(f)
    total += len(rs)
    print("%-32s rows=%3d bytes=%5d" % (f, len(rs), len(raw.encode())))
    for n,v in rs:
        where[n].append(f)
    for t in targets:
        if t in stripped:
            print("   TARGET-IN-ROWS: %r" % t)
        elif t in raw:
            print("   target appears only inside a comment: %r" % t)
print("TOTAL ROWS:", total, " DISTINCT NAMES:", len(where))
dups = {n:fs for n,fs in where.items() if len(set(fs))>1 or len(fs)>1}
print("DUPLICATES:", dups if dups else "none")
for t in targets:
    print("gate C3 %-30s -> %s" % (t, where.get(t, "ABSENT")))
