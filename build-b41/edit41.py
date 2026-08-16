import io, hashlib, os

LIMIT = 24576

def read(p):  return open(p, encoding="utf-8").read()
def write(p, s):
    with open(p, "w", encoding="utf-8", newline="") as f: f.write(s)

# ---------- edit 1: blank Baker's in file 3 ----------
p3 = "tjjm-gym-websites-3.liquid"
s3 = read(p3)
old = "~Baker's MMA & Fitness LLC|http://www.bakersmmaandfitness.com/~\n"
new = "~Baker's MMA & Fitness LLC|~\n"
assert s3.count(old) == 1, "expected exactly one Baker's row, found %d" % s3.count(old)
s3 = s3.replace(old, new)
assert s3.endswith("{%- endcomment -%}\n")
s3 += """{%- comment -%}
  16 Aug 2026 - BATCH 41. LIVE HIJACK, CONFIRMED IN A REAL CHROME BROWSER, NOT A FETCH.
  Three directory links were opened and read in the browser; each served hijacked content
  instead of the school. The value is EMPTY, which blanks the link: the school stays
  listed with its name, city and map link, only the URL is removed.

  Blanked in this file (1), edited in place so gate C3 still holds:
    Baker's MMA & Fitness LLC   bakersmmaandfitness.com now serves Fixbet Turkiye,
                                a Turkish online casino

  The other two carried no override row anywhere, so they were added as new blanking
  rows in tjjm-gym-websites-6.liquid:
    10th Planet North Dallas    slotdemoonline.com, Indonesian slot gambling
    Applied MMA Austin          Chinese film piracy portal
{%- endcomment -%}
"""
write(p3, s3)

# ---------- edit 2 + 3: two new blanking rows in file 6 ----------
p6 = "tjjm-gym-websites-6.liquid"
s6 = read(p6)
for n in ("10th Planet North Dallas", "Applied MMA Austin"):
    assert n not in s6, "name already present in file 6: " + n
assert s6.endswith("~\n")
s6 += """{%- comment -%}
  16 Aug 2026 - BATCH 41. LIVE HIJACKS. Two new blanking rows. Neither name had a row in
  any of the six override files, so gate C3 is clean and they are added here rather than
  edited elsewhere.

  BOTH WERE OPENED AND READ IN A REAL CHROME BROWSER, NOT FETCHED. That distinction is the
  whole point: the fetch tool serves stale cached page bodies and has returned live-looking
  school content for domains a browser showed were dead or hijacked. These are live now.

  What each served when read on 16 Aug 2026:
    10th Planet North Dallas   slotdemoonline.com, Indonesian slot gambling site
    Applied MMA Austin         Chinese film piracy portal

  A third link confirmed in the same browser pass, Baker's MMA & Fitness LLC (Fixbet
  Turkiye, a Turkish online casino), already had a row in tjjm-gym-websites-3.liquid and
  was blanked there in place.

  Value is EMPTY, which blanks the link. Each school stays listed with its name, city and
  map link; only the URL is removed. Reversible by deleting the row.
{%- endcomment -%}
~10th Planet North Dallas|~
~Applied MMA Austin|~
"""
write(p6, s6)

for p in (p3, p6):
    b = open(p, "rb").read()
    print("%-30s size=%5d headroom=%5d md5=%s" % (p, len(b), LIMIT - len(b), hashlib.md5(b).hexdigest()))
    assert len(b) <= LIMIT, "OVER LIMIT: " + p
