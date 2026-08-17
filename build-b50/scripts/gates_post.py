import os,re,json,collections,hashlib
BASE="/sessions/youthful-gracious-mccarthy/mnt/TJJM Projects/build-b50"
ORIG=os.path.join(BASE,"orig"); BUILT=os.path.join(BASE,"built")
# LIVE state = built where written, orig otherwise
WRITTEN={"tjjm-gyms-data-14.liquid"}
def live(fn):
    d=BUILT if fn in WRITTEN else ORIG
    return open(os.path.join(d,fn),encoding='utf-8').read()
datafiles=["tjjm-gyms-data.liquid"]+[f"tjjm-gyms-data-{i}.liquid" for i in range(2,46)]
ovfiles=["tjjm-gym-websites.liquid"]+[f"tjjm-gym-websites-{i}.liquid" for i in range(2,8)]
def recs(t):
    o=[];p=t.split('{"n":"')
    for c in p[1:]:
        e=c.find('}');o.append(json.loads('{"n":"'+c[:e+1]))
    return o
allr=[]
for f in datafiles: allr+=recs(live(f))
print("CORPUS: %d records across %d files"%(len(allr),len(datafiles)))
ks=collections.Counter(tuple(sorted(r.keys())) for r in allr)
print("field-set histogram:",dict(ks))
print("records missing n/c/s:",sum(1 for r in allr if not(r.get('n') and r.get('c') is not None and r.get('s'))))
print("region histogram matches pre-batch:", )
reg=collections.Counter(r['s'] for r in allr)
print("regions:",len(reg),"total",sum(reg.values()))

rowre=re.compile(r'~([^|~]*)\|([^~]*)~')
STRIP=re.compile(r'\{%-?\s*comment\s*-?%\}.*?\{%-?\s*endcomment\s*-?%\}',re.S)
rows=[]
print("\nBYTES gate (<24576):")
for f in ovfiles:
    t=live(f); b=len(t.encode())
    print(f"  {f:32} {b:>6} B  headroom {24576-b:>6}  {'OK' if b<24576 else 'FAIL'}")
    for m in rowre.finditer(STRIP.sub('',t)):
        rows.append((f,m.group(1).strip(),m.group(2).strip()))
print("\ntotal REAL override rows (comment blocks stripped):",len(rows))
print("blank (link-killing) rows:",sum(1 for _,_,u in rows if u==''))
print("repoint rows:",sum(1 for _,_,u in rows if u!=''))
cnt=collections.Counter(n for _,n,_ in rows)
dupes={n:k for n,k in cnt.items() if k>1}
print("C3 (name in exactly one file, once):","PASS" if not dupes else f"FAIL {dupes}")
names={r['n'] for r in allr}
orph=[(f,n) for f,n,_ in rows if n not in names]
print("C5 (every override name matches a record):","PASS" if not orph else f"{len(orph)} orphan(s)")
for f,n in orph: print("     ORPHAN:",f,repr(n))
dn={n for n,k in collections.Counter(r['n'] for r in allr).items() if k>1}
risky=sorted({n for _,n,_ in rows} & dn)
print("\nDUPLICATE-NAME check - override rows keyed on a name held by >1 record:",len(risky))
for n in risky:
    hits=[r for r in allr if r['n']==n]
    val=[u for _,x,u in rows if x==n][0]
    print(f"  {n!r} -> override={val!r}")
    for h in hits: print(f"      {h['c']}/{h['s']} w={h.get('w')!r}")
