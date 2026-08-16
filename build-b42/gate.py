import re,sys,csv,collections
FILES=["tjjm-gym-websites.liquid"]+["tjjm-gym-websites-%d.liquid"%i for i in range(2,7)]
ROW=re.compile(r'~([^~|]*)\|([^~]*)~')
def rows(path):
    t=open(path,encoding='utf-8').read()
    stripped=re.sub(r'\{%-?\s*comment\s*-?%\}.*?\{%-?\s*endcomment\s*-?%\}','',t,flags=re.S)
    return [(m.group(1),m.group(2)) for m in ROW.finditer(stripped)]
idx=collections.defaultdict(list)
tot=0
for f in FILES:
    rs=rows(f); tot+=len(rs)
    for n,u in rs: idx[n].append((f,u))
print("total rows",tot,"distinct names",len(idx))
dups={n:v for n,v in idx.items() if len(v)>1}
print("names in >1 row:",{n:[x[0] for x in v] for n,v in dups.items()} or "NONE")
names=[r['name'] for r in csv.DictReader(open('../scratch/identity/apply-b42.tsv',encoding='utf-8'),delimiter='\t')]
print("worklist names",len(names))
print("=== per-name presence ===")
for n in names:
    print("%-58s %s" % (n, idx.get(n,"ABSENT")))
