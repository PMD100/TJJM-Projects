# BATCH 42 - apply 32 identity-pass link removals. Script-only edits, no hand editing.
import csv,os,hashlib
LIMIT=24576
rows=list(csv.DictReader(open('../scratch/identity/apply-b42.tsv',encoding='utf-8'),delimiter='\t'))
assert len(rows)==32

# Mandated header, used verbatim in all three edited files.
HDR = """{%- comment -%}
  16 Aug 2026 - BATCH 42. Identity pass, the first content check ever run on these links.
  32 removals; every verdict confirmed by loading the page in a REAL CHROME BROWSER, not by
  the fetch tool. 10 DEAD, 8 AGGREGATOR, 7 STRIKING_ONLY, 5 WRONG_CITY, 1 PARKED,
  1 WRONG_BUSINESS. AGGREGATOR = booking platforms, Google business.site pages and brand
  homepages; by the owner's policy a school's own Facebook or Instagram page IS an acceptable
  link and those were kept.
"""

def swap(path, old, new):
    t=open(path,encoding='utf-8').read()
    assert t.count(old)==1,(path,old,t.count(old))
    open(path,'w',encoding='utf-8',newline='').write(t.replace(old,new))

def emit(path, tail):
    t=open(path,encoding='utf-8').read()
    if not t.endswith("\n"): t+="\n"
    t+=tail
    b=t.encode('utf-8')
    assert len(b)<LIMIT,(path,len(b))
    open(path,'w',encoding='utf-8',newline='').write(t)

# ---- 2 in-place value blanks ---------------------------------------------
swap('tjjm-gym-websites.liquid',
     '~Bellmore Kickboxing Academy|https://bellmorekickboxingmma.com/~',
     '~Bellmore Kickboxing Academy|~')
swap('tjjm-gym-websites-3.liquid',
     '~Atlanta Budokan|https://gamasd.com/~',
     '~Atlanta Budokan|~')

emit('tjjm-gym-websites.liquid', HDR + """  Changed here: 1 row, edited in place, value emptied - Bellmore Kickboxing Academy,
  STRIKING_ONLY. The other 31 rows of batch 42 are in files 3 and 6. Gate C3 holds.
{%- endcomment -%}
""")

emit('tjjm-gym-websites-3.liquid', HDR + """  Changed here: 1 row, edited in place, value emptied - Atlanta Budokan, WRONG_CITY: the
  site is Georgia Martial Arts of Acworth GA while the record says Smyrna. It already had a
  row in this file, so it was blanked here rather than added to file 6, keeping gate C3
  clean - one name, one file. The other 31 rows of batch 42 are in files 1 and 6.
{%- endcomment -%}
""")

# ---- 30 new blanking rows in file 6 --------------------------------------
new=[r for r in rows if r['current_file']=='NO OVERRIDE']
assert len(new)==30
for r in new:
    assert '|' not in r['name'] and '~' not in r['name']
emit('tjjm-gym-websites-6.liquid', HDR + """  Added here: 30 new blanking rows, below. Each was checked against all six override files
  with the comment blocks stripped and appeared in NONE of them, so gate C3 is clean and they
  are added here rather than edited elsewhere. The other 2 of the 32 already had rows and were
  blanked in place: Atlanta Budokan in file 3, Bellmore Kickboxing Academy in file 1.
  An empty value blanks the link only - each school keeps its name, city and map link, and the
  change is reversible by deleting the row.
{%- endcomment -%}
""" + "".join("~%s|~\n"%r['name'] for r in new))

for f in sorted(os.listdir('.')):
    if f.endswith('.liquid'):
        b=open(f,'rb').read()
        print("%-30s %6d  headroom %5d  md5 %s"%(f,len(b),LIMIT-len(b),hashlib.md5(b).hexdigest()))
