# -*- coding: utf-8 -*-
import json, os, hashlib, io, sys
ROOT="/sessions/youthful-gracious-mccarthy/mnt/TJJM Projects"
O=os.path.join(ROOT,'build-b50b/orig'); B=os.path.join(ROOT,'build-b50b/built')
NLC=["St. John's","Corner Brook","Gander","Paradise","Conception Bay South",
     "Labrador City","Grand Falls-Windsor","Clarenville","Mount Pearl","Torbay","Flat Bay"]
rows=json.load(open(os.path.join(ROOT,'build-b50b/city-rows.json'),encoding='utf-8'))
assert len(rows)==21,len(rows)

# ---- gates on the rows ----
seen=set()
for n,c in rows:
    assert n and n.strip()==n, ('name whitespace',n)
    assert c and c.strip()==c, ('GATE empty/whitespace value',n,c)
    assert '|' not in n and '~' not in n, ('GATE C5 name',n)
    assert '|' not in c and '~' not in c, ('GATE C5 value',c)
    assert '\n' not in n and '\n' not in c
    assert n not in seen, ('duplicate row',n); seen.add(n)
    assert c not in NLC, ('GATE NL city value',c)
print('row gates OK: 21 rows, all non-empty, no | or ~, no dupes, no NL city values')

HDR = u"""{%- comment -%}
  TJJM gym-CITY overrides. Format: ~Exact Name|City~ , one row per line, same row
  grammar as the gym-website override files.

  WHY THIS FILE EXISTS. A record is {n,c,s,w,a} - name, city, region code, website,
  address. Website and address were already overridable by snippet; CITY WAS NOT, so
  fixing a wrong city meant editing a data snippet directly. That is no longer viable.
  14 of batch 50's 21 corrections sit in snippets/tjjm-gyms-data.liquid, which is 113 KB
  on a SINGLE 113,186-byte line - far past the ~24,576-byte theme-file rewrite ceiling.
  It cannot be rewritten safely, and one dropped character in it silently destroys every
  record after that point, because the JS parser skips any record whose JSON throws.
  DO NOT EDIT THAT BLOB. Add a row here instead.

  A VALUE IS MANDATORY. Unlike the website files, where an empty value deliberately
  blanks the link, AN EMPTY VALUE HERE MEANS NOTHING and must never be written. A city
  override always carries a city. The build script refuses a blank.

  PRECEDENCE. A row here REPLACES the record's "c" for display, the same way a website
  row replaces "w". (The address file is the odd one out - it only fills a BLANK "a".)
  The record itself is never edited, so deleting a row reverts the site.

  NAMES must match the record's "n" EXACTLY - case, punctuation and accents. A mismatch
  just misses silently. A name must not contain "|" or "~". Override rows key on the
  NAME ONLY, so a name shared by two schools hits both. The corpus has 16 duplicated
  names across 17 surplus records; confirm a name matches exactly ONE record first.

  REGION IS NOT AFFECTED. Region membership comes from "s", which this file cannot
  touch. Both surfaces apply the override AFTER the Nebraska/Newfoundland re-filing
  test. That test reads the CITY string, so applying an override before it could move a
  school between the NE and NL pages; applied after it, it cannot.

  BOTH SURFACES read this file: sections/tjjm-state-directory.liquid (the 61 region
  pages) and sections/tjjm-gym-directory.liquid (the flat "Schools Near You" page).
  A file only one surface reads is worse than no file at all - see
  CRITICAL-second-directory-surface.md.

  17 Aug 2026 - BATCH 50. Created with the 21 rows below. Each new city was verified
  against the school's own live published address, not against an aggregator. One row,
  AKF Lexington Martial Arts, restates a value already corrected in
  snippets/tjjm-gyms-data-14.liquid earlier in this batch; it is kept so that this file
  is the single list of every city correction.
{%- endcomment -%}
"""
body = HDR + u''.join(u'~%s|%s~\n' % (n,c) for n,c in rows)
open(os.path.join(B,'tjjm-gym-cities.liquid'),'w',encoding='utf-8',newline='').write(body)

# ================= section patches =================
INS={}
def patch(fn, edits):
    src=open(os.path.join(O,fn),encoding='utf-8',newline='').read()
    out=src; applied=[]
    for anchor,repl in edits:
        assert out.count(anchor)==1, ('anchor not unique: %d'%out.count(anchor), fn, anchor[:70])
        assert src.count(anchor)==1, ('anchor not unique in ORIG', fn)
        out=out.replace(anchor,repl,1)
    # ---- byte-offset proof: reconstruct orig by deleting the inserted runs ----
    ob=src.encode('utf-8'); nb=out.encode('utf-8')
    # walk a diff of insertions only
    import difflib
    sm=difflib.SequenceMatcher(None, ob, nb, autojunk=False)
    ops=[o for o in sm.get_opcodes() if o[0]!='equal']
    for tag,i1,i2,j1,j2 in ops:
        assert tag=='insert', ('non-insert op!',tag,fn,ob[i1:i2][:80])
        applied.append((i1, nb[j1:j2]))
    # independent reconstruction check
    rebuilt=bytearray(nb)
    for i1,ins in sorted(applied, key=lambda x:-x[0]):
        pass
    # verify: removing each inserted run from nb (right to left) yields ob exactly
    tmp=nb
    for tag,i1,i2,j1,j2 in sorted(ops,key=lambda o:-o[3]):
        tmp=tmp[:j1]+tmp[j2:]
    assert tmp==ob, 'reconstruction FAILED for '+fn
    INS[fn]=(ob,nb,applied)
    open(os.path.join(B,fn),'w',encoding='utf-8',newline='').write(out)
    return src,out,applied

# ---- state directory ----
sd_edits=[
 ("{%- capture addr_overrides -%}{%- render 'tjjm-gym-addresses' -%}{%- endcapture -%}\n",
  "{%- capture addr_overrides -%}{%- render 'tjjm-gym-addresses' -%}{%- endcapture -%}\n"
  "{%- capture city_overrides -%}{%- render 'tjjm-gym-cities' -%}{%- endcapture -%}\n"),
 ("  {%- assign g_web = '' -%}\n",
  "  {%- assign cprobe = '~' | append: g_name | append: '|' -%}\n"
  "  {%- if city_overrides contains cprobe -%}{%- assign g_city = city_overrides | split: cprobe | last | split: '~' | first | strip -%}{%- endif -%}\n"
  "  {%- assign g_web = '' -%}\n"),
]
patch('tjjm-state-directory.liquid', sd_edits)

# ---- gym directory (flat page) ----
gd_edits=[
 ("<script type=\"text/plain\" id=\"tjjmDirAddr\">{%- render 'tjjm-gym-addresses' -%}</script>\n",
  "<script type=\"text/plain\" id=\"tjjmDirAddr\">{%- render 'tjjm-gym-addresses' -%}</script>\n"
  "<script type=\"text/plain\" id=\"tjjmDirCity\">{%- render 'tjjm-gym-cities' -%}</script>\n"),
 ("  var wov=overrides(raw('tjjmDirWeb')), aov=overrides(raw('tjjmDirAddr'));",
  "  var wov=overrides(raw('tjjmDirWeb')), aov=overrides(raw('tjjmDirAddr')), cov=overrides(raw('tjjmDirCity'));"),
 ("    var code=(s==='NE'&&NLC.indexOf(c)>-1)?'NL':s;",
  "    var code=(s==='NE'&&NLC.indexOf(c)>-1)?'NL':s; if(n in cov)c=cov[n];"),
]
patch('tjjm-gym-directory.liquid', gd_edits)

# ---- websites-7 batch-50 record block ----
w7=open(os.path.join(O,'tjjm-gym-websites-7.liquid'),encoding='utf-8',newline='').read()
BLOCK = u"""{%- comment -%}
  17 Aug 2026 - BATCH 50. CITY IS NOW OVERRIDABLE. No override rows were added to this
  file this batch; this is a record entry only.

  1. NEW MECHANISM. snippets/tjjm-gym-cities.liquid was created and wired into BOTH
     rendering surfaces - sections/tjjm-state-directory.liquid (the 61 region pages) and
     sections/tjjm-gym-directory.liquid (the flat "Schools Near You" page). Row grammar is
     the same as this file's: ~Exact Name|City~. A row REPLACES the record's "c" the way a
     row here replaces "w", except that an EMPTY VALUE IS NOT ALLOWED - a city override
     must always carry a city.

  2. 21 CITY CORRECTIONS applied through it, each verified against the school's own live
     published address. Every name matched exactly one record. Not one record changed
     region: region membership comes from "s", which the override cannot touch, and both
     surfaces apply the city override AFTER the Nebraska/Newfoundland re-filing test,
     which reads the city string. The corpus is still 5,911 records / 5,215 published
     across 61 regions, with every per-region count unchanged.

  3. DO NOT EDIT snippets/tjjm-gyms-data.liquid. It is 113 KB on a SINGLE 113,186-byte
     line, far past the ~24,576-byte theme-file rewrite ceiling, so it cannot be rewritten
     safely. A single dropped character in it silently destroys every record after that
     point, because the JS parser skips any record whose JSON throws. 14 of this batch's
     21 corrections live in that blob; all 14 were done as overrides instead. That is now
     the only supported way to fix a city.

  4. ONE DATA-FILE EDIT DID LAND EARLIER IN THIS BATCH, before the override mechanism
     existed: snippets/tjjm-gyms-data-14.liquid, AKF Lexington Martial Arts, "c" changed
     from Nicholasville to Lexington (6,182 -> 6,178 bytes). That correction is right and
     was left in place. tjjm-gym-cities.liquid also carries a row for it restating the
     same value, so the override file is the single list of all 21 corrections.

  CORRECTING AN EARLIER DRAFT. A draft of this block claimed batch 50 renamed a record
  ("Evolution Jiu Jitsu" -> "Evolution Jiu Jitsu Burlington") and added a blanking row for
  "American Grappling". BOTH WERE REFUSED AND NEITHER HAPPENED. The draft also claimed a
  curly-apostrophe fix in tjjm-gym-websites-6.liquid for Murdoc's; that file was never
  written and is unchanged. Do not carry any of those three forward as done.

  Override rows key on the record name, so a name shared by two schools hits both. The
  corpus has 16 duplicated names; check before writing any override row.
{%- endcomment -%}
"""
assert not w7.endswith('\n\n')
w7b = w7 + BLOCK
open(os.path.join(B,'tjjm-gym-websites-7.liquid'),'w',encoding='utf-8',newline='').write(w7b)

# ---- report ----
print()
for fn in ['tjjm-gym-cities.liquid','tjjm-state-directory.liquid','tjjm-gym-directory.liquid','tjjm-gym-websites-7.liquid']:
    p=os.path.join(B,fn); d=open(p,'rb').read()
    op=os.path.join(O,fn); od=open(op,'rb').read() if os.path.exists(op) else b''
    print('%-34s orig %7d %s -> built %7d %s  lines %d->%d' % (
        fn, len(od), hashlib.md5(od).hexdigest() if od else '-'*32,
        len(d), hashlib.md5(d).hexdigest(), od.count(b'\n'), d.count(b'\n')))
    assert len(d) < 24576, ('GATE BYTES', fn, len(d))
print()
for fn,(ob,nb,applied) in INS.items():
    print('### %s : %d insertion(s), 0 deletions, 0 replacements' % (fn, len(applied)))
    for off,ins in applied:
        line = ob[:off].count(b'\n')+1
        print('    offset %6d (line %3d)  +%4d bytes: %s' % (off, line, len(ins), ins.decode('utf-8')[:100].replace('\n','\\n')))
    import re as _re
    names=_re.findall(rb"render '([a-z0-9\-]+)'", nb)
    from collections import Counter
    c=Counter(names)
    dups={k.decode():v for k,v in c.items() if v!=1}
    print('    renders: %d total, %d distinct, not-exactly-once: %s' % (len(names), len(c), dups or 'NONE'))
    assert b"render 'tjjm-gym-cities'" in nb
