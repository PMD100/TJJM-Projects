#!/usr/bin/env python3
# Batch 52 - create snippets/tjjm-gyms-data-46.liquid and wire it into BOTH sections.
# Reads originals from build-b52/orig/, writes to build-b52/built/. No hand editing.
import hashlib, os, sys, json

ROOT = "/sessions/youthful-gracious-mccarthy/mnt/TJJM Projects/build-b52"
ORIG = os.path.join(ROOT, "orig")
BUILT = os.path.join(ROOT, "built")
CEILING = 24576

def rd(p):
    with open(p, "rb") as f: return f.read()
def wr(p, b):
    with open(p, "wb") as f: f.write(b)
def md5(b): return hashlib.md5(b).hexdigest()

TEST = os.environ.get("B52_TEST") == "1"

# ---------------------------------------------------------------- data-46
HEADER = """{%- comment -%}
  TJJM gym data, file 46. Same shape as files 1-45: a JSON array, opening [ on its own
  line, one record per line, closing ] on its own line, file ends with a newline.

  THIS FILE IS THE HOME FOR NEWLY DISCOVERED GYMS. The nightly discovery job appends its
  records here, below this comment and inside the array. Nothing else writes to it.

  Record shape - the only keys either parser reads:
    {"n":name,"c":city,"s":region code,"w":website,"a":address}
  "w" and "a" are optional. Omit the key entirely rather than writing an empty string.

  HARD RULES. All three fail SILENTLY - nothing errors, the page just renders wrongly.
  1. A NAME MUST NOT CONTAIN | OR ~. Both are field delimiters - | separates the fields
     of a row and ~ terminates it, in the override snippets and in the state-directory
     buffer alike. A name carrying either one splits a row and corrupts its neighbours.
  2. A NAME MUST BE UNIQUE ACROSS THE WHOLE CORPUS - all 46 data files, not just this
     one. Every override file (websites, addresses, cities) keys on the name ALONE, so a
     duplicate name silently applies one override row to every record that shares it.
     Check the new name against every data file before appending it.
  3. "s" MUST ALREADY EXIST as a region code in snippets/tjjm-region-index.liquid. An
     unknown code renders on no region page and falls into no filter group on the flat
     page, so the record is simply invisible.

  WHY A NEW FILE EXISTS. snippets/tjjm-gyms-data.liquid is 113,187 bytes and contains no
  newline at all - one 113,187-character line - far past the ~24,576-byte Admin API
  rewrite ceiling. It cannot be rewritten, and a single dropped character in it destroys
  every record after it. Files 2-45 are near their own ceilings. Keep THIS file under
  24,576 bytes too; when it fills, add file 47 and wire it into BOTH
  sections/tjjm-state-directory.liquid AND
  sections/tjjm-gym-directory.liquid in the same change. A data file that only one
  surface renders is exactly the defect in CRITICAL-second-directory-surface.md, which
  went unnoticed for 28 batches.

  19 Aug 2026 - BATCH 52. Created as plumbing only, no records. Wired into both sections
  and verified end to end with a temporary test record, which was then removed.
{%- endcomment -%}
"""
TEST_REC = '{"n":"ZZ Test Academy B52","c":"Bozeman","s":"MT","w":"https://example.com/b52","a":"1 Test St"}'
records = [TEST_REC] if TEST else []
body = "[\n" + "".join(r + ("," if i < len(records)-1 else "") + "\n" for i, r in enumerate(records)) + "]\n"
data46 = (HEADER + body).encode("utf-8")

# self-checks on data-46
assert data46.endswith(b"]\n"), "must end ] + newline"
assert b'{%' not in HEADER.encode().replace(b'{%- comment -%}', b'').replace(b'{%- endcomment -%}', b''), "no liquid tags inside comment"
assert b'{"n":"' not in HEADER.encode(), "header must not contain the split delimiter"
for r in records:
    o = json.loads(r)               # every record must be valid JSON on its own
    assert '|' not in o['n'] and '~' not in o['n'], "name contains | or ~"
    assert r.index('}') == len(r)-1, "first } must be the record's own closing brace"
assert len(data46) < CEILING, "data-46 over ceiling"
wr(os.path.join(BUILT, "tjjm-gyms-data-46.liquid"), data46)

# ---------------------------------------------------------------- section patches
NEEDLE = b"{%- render 'tjjm-gyms-data-45' -%}"
INSERT = b"{%- render 'tjjm-gyms-data-46' -%}"
import re
RENDER_RE = re.compile(rb"render '([^']+)'")

def render_counts(b):
    c = {}
    for m in RENDER_RE.finditer(b):
        c[m.group(1)] = c.get(m.group(1), 0) + 1
    return c

report = []

def patch_chain(name):
    old = rd(os.path.join(ORIG, name))
    assert old.count(NEEDLE) == 1, f"{name}: needle count {old.count(NEEDLE)}"
    assert old.count(INSERT) == 0, f"{name}: data-46 already present"
    off = old.index(NEEDLE) + len(NEEDLE)
    new = old[:off] + INSERT + old[off:]
    # --- proofs -------------------------------------------------
    assert new == old[:off] + INSERT + old[off:]
    assert len(new) == len(old) + len(INSERT)
    assert new[:off] == old[:off] and new[off+len(INSERT):] == old[off:], "bytes outside insertion changed"
    assert new.count(b"\n") == old.count(b"\n"), "line count changed"
    co, cn = render_counts(old), render_counts(new)
    for k, v in co.items():
        assert cn.get(k) == v, f"{name}: render '{k.decode()}' count {v} -> {cn.get(k)}"
    extra = {k: v for k, v in cn.items() if k not in co}
    assert extra == {b"tjjm-gyms-data-46": 1}, f"{name}: unexpected new renders {extra}"
    assert all(cn[k] == 1 for k in cn), f"{name}: some render appears more than once"
    # data-46 must come AFTER data-45 and before endcapture/close of that chain
    assert new.index(INSERT) > new.index(NEEDLE), "46 not after 45"
    assert new.index(INSERT) == off
    # untouched families
    for fam in (b"tjjm-removed-index", b"tjjm-gym-cities", b"tjjm-gym-websites"):
        assert old.count(fam) == new.count(fam), f"{name}: {fam.decode()} disturbed"
    assert len(new) < CEILING, f"{name}: over ceiling"
    report.append(dict(file=name, offset=off,
                       before=dict(bytes=len(old), md5=md5(old), lines=old.count(b"\n")),
                       after=dict(bytes=len(new), md5=md5(new), lines=new.count(b"\n")),
                       ctx_before=old[off-40:off].decode(), ctx_after=new[off:off+len(INSERT)+40].decode()))
    return old, new

# state directory: chain insertion only
sd_old, sd_new = patch_chain("tjjm-state-directory.liquid")
wr(os.path.join(BUILT, "tjjm-state-directory.liquid"), sd_new)

# gym directory: doc-comment fix, then chain insertion
gd_orig = rd(os.path.join(ORIG, "tjjm-gym-directory.liquid"))
DOC_OLD = b"snippets/tjjm-gyms-data \xe2\x80\xa6 -45      the records"
DOC_NEW = b"snippets/tjjm-gyms-data \xe2\x80\xa6 -46      the records"
assert gd_orig.count(DOC_OLD) == 1, "doc line not unique"
doc_off = gd_orig.index(DOC_OLD) + len(DOC_OLD) - len("5      the records")
gd_v1 = gd_orig.replace(DOC_OLD, DOC_NEW)
assert len(gd_v1) == len(gd_orig)
diffbytes = [i for i in range(len(gd_orig)) if gd_orig[i] != gd_v1[i]]
assert diffbytes == [doc_off], f"doc fix changed {len(diffbytes)} bytes at {diffbytes[:5]}"
# now chain-patch v1
old = gd_v1
assert old.count(NEEDLE) == 1
off = old.index(NEEDLE) + len(NEEDLE)
gd_new = old[:off] + INSERT + old[off:]
assert len(gd_new) == len(old) + len(INSERT)
assert gd_new.count(b"\n") == old.count(b"\n")
co, cn = render_counts(old), render_counts(gd_new)
for k, v in co.items(): assert cn.get(k) == v
assert {k: v for k, v in cn.items() if k not in co} == {b"tjjm-gyms-data-46": 1}
assert all(cn[k] == 1 for k in cn)
for fam in (b"tjjm-removed-index", b"tjjm-gym-cities", b"tjjm-gym-websites"):
    assert gd_orig.count(fam) == gd_new.count(fam)
assert len(gd_new) < CEILING
report.append(dict(file="tjjm-gym-directory.liquid", offset=off, doc_fix_offset=doc_off,
                   before=dict(bytes=len(gd_orig), md5=md5(gd_orig), lines=gd_orig.count(b"\n")),
                   after=dict(bytes=len(gd_new), md5=md5(gd_new), lines=gd_new.count(b"\n")),
                   ctx_before=old[off-40:off].decode(), ctx_after=gd_new[off:off+len(INSERT)+40].decode()))
wr(os.path.join(BUILT, "tjjm-gym-directory.liquid"), gd_new)

print("MODE:", "WITH TEST RECORD" if TEST else "PLUMBING ONLY (no records)")
print(f"data-46: {len(data46)} B  md5 {md5(data46)}  lines {data46.count(chr(10).encode())}")
for r in report:
    print(json.dumps(r, indent=2))
