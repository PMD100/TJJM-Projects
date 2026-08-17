import json, csv, sys, collections
sys.path.insert(0,'/sessions/youthful-gracious-mccarthy/mnt/TJJM Projects/build-b50/scripts')
corpus=json.load(open('/tmp/corpus.json'))
byname=collections.defaultdict(list)
for r in corpus: byname[r['n']].append(r)

TSV='/sessions/youthful-gracious-mccarthy/mnt/TJJM Projects/scratch/identity/apply-b50-city.tsv'
rows=list(csv.DictReader(open(TSV,encoding='utf-8-sig'),delimiter='\t'))
rows=[{k:(v.strip() if isinstance(v,str) else v) for k,v in r.items()} for r in rows]
print("TSV rows:",len(rows))
print("="*70)
ok=[]
for r in rows:
    nm,reg,rc,nc=r['name'],r['region'],r['record_city'],r['new_city']
    cands=byname.get(nm,[])
    exact=[x for x in cands if x['c']==rc]
    status="OK" if len(exact)==1 else "PROBLEM"
    extra=""
    if len(exact)==1:
        e=exact[0]
        if e['s']!=reg: status="PROBLEM"; extra+=f" REGION MISMATCH record s={e['s']} tsv={reg}"
        extra+=f"  file={e['file']}"
        # does new_city already collide?
    print(f"{status:8} {nm!r:50} name_matches={len(cands)} city_matches={len(exact)}{extra}")
    if len(cands)!=len(exact):
        for x in cands: print(f"           other: c={x['c']!r} s={x['s']!r} file={x['file']}")
    if status=="OK": ok.append((r,exact[0]))
print("="*70)
print("OK count:",len(ok))
print()
print("=== Evolution Jiu Jitsu ===")
for x in byname.get('Evolution Jiu Jitsu',[]): print(" ",x)
print("Evolution Jiu Jitsu Burlington exists as record name:", 'Evolution Jiu Jitsu Burlington' in byname)
print()
print("=== American Grappling ===")
for x in byname.get('American Grappling',[]): print(" ",x)
print("name_matches:",len(byname.get('American Grappling',[])))
print()
print("=== Murdoc records ===")
for n in byname:
    if 'Murdoc' in n: print(" ",repr(n),byname[n])
json.dump([{"tsv":r,"rec":e} for r,e in ok],open('/tmp/plan_city.json','w'))
